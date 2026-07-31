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
<img src="https://cdn4.telesco.pe/file/jzgVPbyU1DDeXZwZWIyF5-IMwSOTVweNrNxilHDNV0X7BZijn-0TFUQIkPDeuaBbrfth20WjyxhxfYv7gY7r3DvzPG3YhrzvsPvtQEzSGnUmBYw3Gw2-oPu10ETEGq0FGMJFFwPJbTmmDDUO5493H0sKSBgg50J5SI880HlQhCBST8Dci3vC-CcEWaHdKjQ73R946UNXs0JTlS7dGw0SUHl9wusA-nBxnCzPOXeRUtPy-0G6FuIvYZBFD4SvQfpS3lCEcskI_420-4oIJRNvTZqZeUa77cKrHmsq3-0uPEo70p5-_hOcmKJMhA5ET3f1mbpwF3lOp5VpvMFQY3FG8Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 981K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 09:26:41</div>
<hr>

<div class="tg-post" id="msg-138800">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0085b8d38d.mp4?token=oF-YIWqIxoN5e3_G6-LqTN_IZNtiuU097GYda19E89H2ye7u4ImhHngKUVw4EaDdt7_X3kjQdUqnCi4_y55D1woLQszprQysA8V34YqqSloRGB_L7a4x89wQeDFhoRnmZHQ2AejkKTxwVNMjaXEGpGpItk2fCbGEK0xUCKkLLdyp6T8lsn-6R8BFyJxpePyZH98wMK36YQFr_dnQkyjvMQmHza-DjVr23hhwouhW-aS0hZP1bec-WmQRPzO4hxk250sR8Wh0QFcUAgHctr2M1Jq9g4cjktF2zicbkM5j1d5OkL-ifOm6peCfKJfrDhsSYIvrkw_dKVaRb53vUNc6JwSBM_niMTq_R5DpEaFPQbZckn90mq-vSpU3x1eLLzs3ZkcLDb6DBhCTdGLIwuHCRUu21QyqAJJ-uLh1KtQXMmylNdiCn_XBKO65zgF5IuRsaFhO9wQiewoMDWg1XJvnPulipWPwWPcYnEbVaDJe9qejQrl7I7TyD6B5mWnsflTafkHwLWn94dgsBLe0udppaxRgxywweVJVneeR_HsHvmwFlw8XykVxSApsENMDfyTTeOzArB94eXbobzfsCLW5sLLLcoKrFzWbMJwVbo28jlsTri3QjK98jWFf-wtOwI9DoMFyKJjjQVNYpdseVTdq07zxVaBfrAUeLwHuTDh1Bao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0085b8d38d.mp4?token=oF-YIWqIxoN5e3_G6-LqTN_IZNtiuU097GYda19E89H2ye7u4ImhHngKUVw4EaDdt7_X3kjQdUqnCi4_y55D1woLQszprQysA8V34YqqSloRGB_L7a4x89wQeDFhoRnmZHQ2AejkKTxwVNMjaXEGpGpItk2fCbGEK0xUCKkLLdyp6T8lsn-6R8BFyJxpePyZH98wMK36YQFr_dnQkyjvMQmHza-DjVr23hhwouhW-aS0hZP1bec-WmQRPzO4hxk250sR8Wh0QFcUAgHctr2M1Jq9g4cjktF2zicbkM5j1d5OkL-ifOm6peCfKJfrDhsSYIvrkw_dKVaRb53vUNc6JwSBM_niMTq_R5DpEaFPQbZckn90mq-vSpU3x1eLLzs3ZkcLDb6DBhCTdGLIwuHCRUu21QyqAJJ-uLh1KtQXMmylNdiCn_XBKO65zgF5IuRsaFhO9wQiewoMDWg1XJvnPulipWPwWPcYnEbVaDJe9qejQrl7I7TyD6B5mWnsflTafkHwLWn94dgsBLe0udppaxRgxywweVJVneeR_HsHvmwFlw8XykVxSApsENMDfyTTeOzArB94eXbobzfsCLW5sLLLcoKrFzWbMJwVbo28jlsTri3QjK98jWFf-wtOwI9DoMFyKJjjQVNYpdseVTdq07zxVaBfrAUeLwHuTDh1Bao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روایت حمله به خوابگاه دانشجویی اهواز از زبان یکی از دانشجویان
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/138800" target="_blank">📅 09:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138799">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
عبور ۲۵ کشتی تجاری از باب‌المندب
🔴
بر اساس داده‌های شرکت ردیابی دریایی Kpler که خبرگزاری رویترز به آن استناد کرده است، روز پنج‌شنبه ۲۵ کشتی تجاری از تنگه باب‌المندب عبور کردند، در حالی که تردد در تنگه هرمز همچنان بسیار محدود بود و تنها دو نفتکش از آن عبور کردند.
🔴
از میان این ۲۵ کشتی:
۱۸ فروند وارد آبراه شدند.
۷ فروند از آن خارج شدند.
🔴
این کشتی‌ها شامل چندین نفتکش، از جمله: دو نفتکش بسیار بزرگ (VLCC)،
یک نفتکش سوئزمکس،
و پنج نفتکش آفرامکس بودند.
🔴
در همین حال، هیچ‌یک از دو کشتی عبوری از تنگه هرمز حامل محموله نبودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/138799" target="_blank">📅 09:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138798">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
واشنگتن پست به نقل از یک مقام آمریکایی گزارش داد که واشنگتن از اسرائیل فقط می‌خواهد که با طرح ۲۰ ماده‌ای که قبلاً به‌طور اصولی با آن موافقت کرده بود، کنار بیاید. این مقام افزود که دولت آمریکا اطمینان دارد اسرائیل به این طرح پایبند خواهد بود و اشاره کرد که اگر چنین نکند، دونالد ترامپ، رئیس‌جمهور، «به‌شدت ناامید خواهد شد».
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/alonews/138798" target="_blank">📅 09:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138797">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
یک منبع اطلاعاتی آمریکایی به شبکه نیوزماکس گفت:ایران از داده‌های مربوط به فناوری تبلیغات برای ردیابی نیروهای آمریکایی و هدف قرار دادن آن‌ها استفاده کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/138797" target="_blank">📅 09:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138795">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cb5776e72.mp4?token=GwzdLQYz2HkBQo0VpGCVyR6kk7XTryzSzfe8z5xpHWlu39oy8JEg6RU_3msH2OEKFggVQfkIckMHIaA-6lPAV49y0whhHQxgGanhuC3oSgnPL9i2NSX78xe_aPr9yrHz65vj3tukbvcU8EiZIbe0Y24ReoomhogKdURafgutz7IsZ4L8abbBGon40iVbeWwDmCHFVL_g90TT8YZ_r7oEo0uQFXX1EwI27cN6arJPqAdls82nkhV78GUIahqfu7DinHEqwVw7Pe3vWVZj3pfh-qlxWiR6OsXtAthJ3CEQcJG2UDCIK5477XEUvcF4ku-NWkyzlf_y8CTOa7jNZk80Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cb5776e72.mp4?token=GwzdLQYz2HkBQo0VpGCVyR6kk7XTryzSzfe8z5xpHWlu39oy8JEg6RU_3msH2OEKFggVQfkIckMHIaA-6lPAV49y0whhHQxgGanhuC3oSgnPL9i2NSX78xe_aPr9yrHz65vj3tukbvcU8EiZIbe0Y24ReoomhogKdURafgutz7IsZ4L8abbBGon40iVbeWwDmCHFVL_g90TT8YZ_r7oEo0uQFXX1EwI27cN6arJPqAdls82nkhV78GUIahqfu7DinHEqwVw7Pe3vWVZj3pfh-qlxWiR6OsXtAthJ3CEQcJG2UDCIK5477XEUvcF4ku-NWkyzlf_y8CTOa7jNZk80Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات ایران به کُردهای تجزیه طلب در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/138795" target="_blank">📅 09:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138794">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
شمار قربانیان زلزله ژاپن به ۳۴ نفر رسید/ ۳۵۰۰ خانه هنوز برق ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/138794" target="_blank">📅 08:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138793">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
اکسیوس به نقل از مقامات اسرائیلی و آمریکایی: ونس و نتانیاهو عصر سه‌شنبه در یک دیدار دوجانبه در واشنگتن، گفت‌وگوی «مستقیمی» درباره اختلافات خود داشتند
🔴
تانیاهو با ونس درباره انتقادات اخیر او از دولت اسرائیل گفت‌وگو کرد
دو طرف توافق کردند که به دنبال فرصت‌هایی برای همکاری اسرائیل و ایالات متحده در حوزه‌های دارای منافع مشترک و اهداف مورد توافق باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/138793" target="_blank">📅 08:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138792">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
وزارت جنگ آمریکا در به‌روزرسانی آمار تلفات اعلام کرد شمار نظامیان زخمی این کشور در جنگ با ایران به ۶۵۳ نفر رسیده است. بر اساس این گزارش، ۱۱ نظامی دیگر مجروح شده‌اند و تاکنون ۱۸ نظامی آمریکایی نیز در جریان درگیری‌ها کشته شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/138792" target="_blank">📅 08:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138791">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ: مطمئن نیستم به اوکراین اجازه تولید موشک‌های پاتریوت را بدهم
🔴
این یک سلاح فوق‌العاده است و باید کمی درباره اینکه به چه کسانی مجوز تولید می‌دهیم، احتیاط کنیم
🔴
تمرکز اصلی من پایان دادن به جنگ روسیه و اوکراین است؛ کوشنر و ویتکاف، برای نخستین بار طی روز‌های آینده به اوکراین سفر خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/138791" target="_blank">📅 08:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138790">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4HjegrVMafhGPBKSal5IQyggi6H34plkNOZyfuagTpPtyFmUnyscJN0rVq7I-3szKXM9K1VgnAHsJLYNpI8X9aXmcwbIxXCQjhdQkWXaYAnYbOUiHanwpZDHDvY2k4bSaMYVRUu6YwIbEJrTicUtB3ZhUNKMxm9sk-EayBQyrFbybZTuWV-jZxbuB-c-WFEedOkk7WtcH5gc8ULcs3hN8BseVhr4r3vyu134QWoANG8BhfZqbyng6JOPhRrGFlu9GVvicjiYfMEk7qf0ys-Bfr3K5VAOfIisph9Pfb4LmE6CsZ23eAVjJsKQuVF4lD8pwYfPWuARnL5Y6xMEgTetg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت اینترنت استارلینک در عراق چقدر است؟
🔴
یک ماهه سرعت ۱۰۰ مگابیتی؛ حجم نامحدود: ۹ میلیون تومان.
🔴
یک ماهه سرعت ۴۰۰ مگابیتی؛ حجم نامحدود: ۱۵ میلیون تومان.
🔴
میانگین درآمد مردم عراق: ماهی ۱۰۰ میلیون تومان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/138790" target="_blank">📅 08:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138789">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZtQSu4TNL-AhKf0tisfBcWhWlFiwWj4eE3YcLGFGJHU2EYWkqaUic1Rcc91n3B-nCdENVw03C3Gla2Z2GQEhIKoPhW0f1DwOEEy0nLrc_k8iiWR8fUVZ0KLjL0E_vMQMWIQRnKy6v9hIz7ZAjljlACG3ytyDvpeUQ19vLZ7xIJgKLmC05bYvlNc3pe7Bv4AxCjasVbVNwQL0j7AwOSYtyJDrq88KTtpYQt_4O3p7ZAKD_cYQNwJb-n8Jga0r50LUiy0RPQJkWCdNE-NN8VyTWe7CJ4_rFekW1sFEySelrWsTSqTU44v_NVXg7nu_B98N7Ll2PdIbzONLnXxUz_oXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: حماس خلع سلاح شد
ترامپ:
امروز، شورای صلح به یک توافق تاریخی در مورد خلع سلاح کامل حماس و تمام گروه‌های مسلح دیگر در غزه دست یافت. این یک گام بزرگ به سوی صلح و امنیت پایدار است.
این توافق، یک گام حیاتی برای این است که دولت فلسطینی جدید، که با شورای صلح برای کمک به مردم فلسطین همکاری نزدیکی خواهد داشت، سرانجام بر غزه حکومت کند. در عین حال، اسرائیل امنیت مورد نیاز خود را به دست خواهد آورد، زیرا غزه دیگر به عنوان پایگاهی برای حملات تروریستی مورد استفاده قرار نخواهد گرفت.
این یک نقطه عطف مهم در اجرای طرح 20 ماده ترامپ است. این توافق به صورت مرحله‌ای و با ساختاری مشخص اجرا خواهد شد. با تکمیل فرآیند خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و نیروهای بین‌المللی حفظ صلح با پلیس فلسطینی جدید همکاری خواهند کرد تا امنیت غزه را برای ساکنان و همسایگان آن تضمین کنند.
یک سال پیش، جنگ وحشتناکی در جریان بود، بحران انسانی وجود داشت و افراد به عنوان گروگان در اسارت وحشیانه نگهداری می‌شدند. ما به پیشرفت تاریخی دست یافته‌ایم و هنوز کارهای زیادی باید انجام شود.
می‌خواهم از میانجی‌ها - مصر، قطر و ترکیه - به خاطر تلاش‌های مهمشان تشکر کنم، و به ویژه از تیم برجسته‌ام که تلاش‌های بی‌وقفه آنها، این پیشرفت تاریخی را ممکن ساخت.
تهدیدی که از غزه در 7 اکتبر ایجاد شد، دیگر فرصتی برای بازگشت نخواهد داشت.
در چارچوب این توافق، غزه سرانجام به دست دولت فلسطینی جدیدی خواهد افتاد که به مردم خود خدمت خواهد کرد.
به همه تبریک می‌گویم برای این دستاورد شگفت‌انگیز که، همانطور که همه می‌گفتند، هرگز قابل تحقق نبود
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/138789" target="_blank">📅 02:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138787">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCr3j0tZP6G6zshzRt9ErmlS4yWqE3aESY7Ap8T8O5zaFo4gv-yRQEgM8Qq83l4olbvvM6UwRGh4YQRDmNbjwPYW_GJvNZ1W1g8z56WjfnNnT_8ddimSnVUk5ZD8Rn88EIWVNZdXaWddUxTEl_B12mdTtMzJ9nbVrN8cJyZUO5Ji5tsA8ppEcXAY7whwf8ilf4uWF02H2ycYF_FxczMvb8v2DK5ZkZbNtsMR3ktnpT3-CUqHbNqIuolNY5QMbsJzySf8J9_7jIxHvf_OLweE4YTAGrMghn5ZhXBA3kPkJtxIxkfAn0fEy1ztOo9CM8QDXw2J48ijyhGPmFqe8O-0cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=v9f32ZroOqYdYNS_Vq9c9gRgj8XoAHkoJZrybIspJmjiHuZbjhPrfBAmuG-HUS0X-r2_GzS_Ua-EHN0TG84isogCeKWVHUtwX7Bqobz5zSSP8AfpApfHw0aR3OeYg8UeALeWsasaMtJ3ZzPqgf1M97uVcYrULSC9aasmeGt8_1Dcx6hwqaXo936FOUozK7HpM_fiN9u5gjPsD02hgmd_0jQe-BTJ8K39n_YfleEQzOKp5Wsht_LzARvawsCCcJDI74Cg-3PdHQZVcJtOrvRnrr-YnH-iQcof_iKtX7gSTd-LgRY2ZCmYUQHO33CLN53Ns8n5EtJCVj8vffW5hwVwBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=v9f32ZroOqYdYNS_Vq9c9gRgj8XoAHkoJZrybIspJmjiHuZbjhPrfBAmuG-HUS0X-r2_GzS_Ua-EHN0TG84isogCeKWVHUtwX7Bqobz5zSSP8AfpApfHw0aR3OeYg8UeALeWsasaMtJ3ZzPqgf1M97uVcYrULSC9aasmeGt8_1Dcx6hwqaXo936FOUozK7HpM_fiN9u5gjPsD02hgmd_0jQe-BTJ8K39n_YfleEQzOKp5Wsht_LzARvawsCCcJDI74Cg-3PdHQZVcJtOrvRnrr-YnH-iQcof_iKtX7gSTd-LgRY2ZCmYUQHO33CLN53Ns8n5EtJCVj8vffW5hwVwBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار عجیب نتانیاهو با یک سناتور!
🔴
امروز نتانیاهو با جان فترمن دیدار کرد و طرف با شرتک نشیته بود و سرش کلا تو گوشی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/138787" target="_blank">📅 01:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138786">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
دقایقی پیش، یک پهپاد در آسمان اربیل، واقع در کردستان، مورد رهگیری قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/138786" target="_blank">📅 01:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138785">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8935b48fd.mp4?token=hdFzeIjcUZoxcgMQzh8cCS-vtpSHTUHM33KOPMfjZ025ESVfcljrA_znjaY4QL5PEql0MCsiqwBHdTbC5ZHjQWvkhuxYGTq6tc9IVxCs7CB7SmrZYSBVtqYnBNl4Ym7uQrvFagC1O8C244Yh4FNQTxnrdhoXLEBXi5X9IKz53eOXRNwhrmaUQChuonzDjC1wqgD4gkKrSHFtyX0d07lDLw6I6TdGpHMAkDPHnQQxQsbIrYffuXR-QASh4v0y8aK6P884pVjAM-CnzQmJ9VlXjpsBpD2JeKD-wFeovMp2Np9NDZ_8e8OCGcL2GnRxokXf-ROPQF4e9ogyxE9h_MVuVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8935b48fd.mp4?token=hdFzeIjcUZoxcgMQzh8cCS-vtpSHTUHM33KOPMfjZ025ESVfcljrA_znjaY4QL5PEql0MCsiqwBHdTbC5ZHjQWvkhuxYGTq6tc9IVxCs7CB7SmrZYSBVtqYnBNl4Ym7uQrvFagC1O8C244Yh4FNQTxnrdhoXLEBXi5X9IKz53eOXRNwhrmaUQChuonzDjC1wqgD4gkKrSHFtyX0d07lDLw6I6TdGpHMAkDPHnQQxQsbIrYffuXR-QASh4v0y8aK6P884pVjAM-CnzQmJ9VlXjpsBpD2JeKD-wFeovMp2Np9NDZ_8e8OCGcL2GnRxokXf-ROPQF4e9ogyxE9h_MVuVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل: تونل‌های حزب‌الله تو منطقه بوفور جنوب لبنان رو با حدود ۷۰۰ تُن مواد منفجره منهدم کردیم
🔴
این عملیات در واکنش به نقض آتش‌بس از سوی حزب‌الله انجام شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/138785" target="_blank">📅 01:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138784">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
دادگاه دختری که از پسرها سواستفاده جنسی میکرد و فیلمش پخش میکرد بزودی برگزار میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/138784" target="_blank">📅 01:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138783">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
دختر ۲۰ساله‌ای که تو خراسان اقدام به تهیه فیلم‌های جنسی ارباب و برده میکرد بازداشت شده
🔴
محتوای چنلش هم تو بات گذاشتیم و میتونید ببینید  زیر ۱۸سال
⚠️
⚠️
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/138783" target="_blank">📅 01:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138782">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e924ddde6.mp4?token=LTfJJ02ABsVxDGCBpEdoq6lDPznQjCdn5mTKmaUjmEP58m42KAFn360-2Fht7Up7T8mm6ySMaKQ4RJNia74IiqclH07oOcbp7jhVBjaKLQqQt3thC2yIzHaL-GsTbpAAhz_M8B0JFVkQ22PZhnCbVlgk3mLPFn2Lmt949SurUoMIhc89qBS-3o-YDjzpkJS4Ra8Auxtxn-z5TWh_v35H1Q0Ve4-9odp7xFAtQt2wyc1rmsIEy8kMkG-xfiHFcOAa0GsGMkIVwlbCw8pgE6hio_Cu-EW8oodpIKjG7pjEBSa-b7Tb6pcUvacNvNVWjKzbfs6_iCviHPRfZallLG5icYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e924ddde6.mp4?token=LTfJJ02ABsVxDGCBpEdoq6lDPznQjCdn5mTKmaUjmEP58m42KAFn360-2Fht7Up7T8mm6ySMaKQ4RJNia74IiqclH07oOcbp7jhVBjaKLQqQt3thC2yIzHaL-GsTbpAAhz_M8B0JFVkQ22PZhnCbVlgk3mLPFn2Lmt949SurUoMIhc89qBS-3o-YDjzpkJS4Ra8Auxtxn-z5TWh_v35H1Q0Ve4-9odp7xFAtQt2wyc1rmsIEy8kMkG-xfiHFcOAa0GsGMkIVwlbCw8pgE6hio_Cu-EW8oodpIKjG7pjEBSa-b7Tb6pcUvacNvNVWjKzbfs6_iCviHPRfZallLG5icYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسین جنتی شاعر: سال ۸۹ تو بیت رهبری شعر خوندم و کمی نقد کردم. آقای خامنه‌ای علنا تهدیدم کرد و فردا صبح مامورا ریختن تو خونه‌ام
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/alonews/138782" target="_blank">📅 00:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138781">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
دادستان تهران:هر کسی از اعدامی‌ها، چه به صورت مستقیم یا غیر مستقیم حمایت کنه جرمه و براش پرونده قضایی تشکیل میدیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/138781" target="_blank">📅 00:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138780">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gIFxAjynHEYVzSX_ihYba3Rk-lAKLi9FPXsJXHOjqC0r_gPE5Y_K6s2bEE573XiA2iZMdUsHvnh1JmktCy1h-CR9F49UWue8z_pVdZRaR-VR06AUNLe1eTAcEGwED7U8z4r7joZ29KiUCzIShxGgqW7oRTmGczI2t94cjp_5GNxksz43UH0wFjEBAzWTURsBSMKz0_v-zrEhaNqP_GL-JughZYk2dlMxAOvGGMZ4a2vUggbATiejFGkvvnyqqAbtlLc5cCuaYPIP9wUELpgkH958mlL4bLCp1CgNoN1OMQIL_OeHzhd1KxOQ11kMO9K0gXTYKGOcoZbY8VyNir3xtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رائفی پور رسما تریاک کشید
‼️
🔴
‏استراتژی جنگی عوستاد رائفی‌پور:
حمله زمینی عراق از شمال و یمن از جنوب کار عربستان را یکسره می کند
🔴
‏عربستان بجز توان هوایی که با هدف قرار گرفتن فرودگاه ها و پایگاه های هوایی اش در همان ابتدا فلج خواهد شد هیچ چیز دیگری ندارد
🔴
‏پاکستان هم به دلیل نداشتن مرز زمینی با عربستان کمک خاصی نمی تواند بکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/alonews/138780" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138779">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
واکنش عادل فردوسی‌پور به ویدیو جنجالی که امروز منتشر شد: ویدیوهایی از گذشته من رو گزینشی منتشر کردن. کاملا تصادفی وزیر ارشاد کنار من نشست. اگه قرار بود من چاپلوس و دست‌بوس باشم، الان صداوسیما بودم و نود رو داشتم. چرا باید دست یه مسئول رو در مقابل جمعیت ببوسم؟…</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/138779" target="_blank">📅 00:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138778">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t81pf5opezJSvIFLRv2BaS-lhRJOB312DPaAejxm4ezVshZkVPNENnRcwlTh_19NSiCDfpzw3ADc7mPfS1Pqs3erc_5OoNpX_CQYA8ju-J1qwzprd8F4OZAdj0Wni8r_X-nSYJ6z2kYHaZEjvRGuKE5yEvWmg5GYSFDq8P081US84ORh3ur8FE0G0VtadrR4fhYsPAXgpfbXjhcW9tIzpZ73RhR0tl6yjmplLvQgaqf9ee__HIH1dRr7yVDTrh3tqOcN5I2f-dz8dJTNSO12a58PZRg76Lw3ZWv3542pTknSnqpoU9Ktiap2x-uYHFoI8pOW5-LenWFOnT4x9BcaFKpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t81pf5opezJSvIFLRv2BaS-lhRJOB312DPaAejxm4ezVshZkVPNENnRcwlTh_19NSiCDfpzw3ADc7mPfS1Pqs3erc_5OoNpX_CQYA8ju-J1qwzprd8F4OZAdj0Wni8r_X-nSYJ6z2kYHaZEjvRGuKE5yEvWmg5GYSFDq8P081US84ORh3ur8FE0G0VtadrR4fhYsPAXgpfbXjhcW9tIzpZ73RhR0tl6yjmplLvQgaqf9ee__HIH1dRr7yVDTrh3tqOcN5I2f-dz8dJTNSO12a58PZRg76Lw3ZWv3542pTknSnqpoU9Ktiap2x-uYHFoI8pOW5-LenWFOnT4x9BcaFKpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش عادل فردوسی‌پور به ویدیو جنجالی که امروز منتشر شد: ویدیوهایی از گذشته من رو گزینشی منتشر کردن. کاملا تصادفی وزیر ارشاد کنار من نشست. اگه قرار بود من چاپلوس و دست‌بوس باشم، الان صداوسیما بودم و نود رو داشتم. چرا باید دست یه مسئول رو در مقابل جمعیت ببوسم؟ چرا اصلا چنین چیزی رو باید باور کنید؟ دست هیچکس رو نمیبوسم. هجمه عجیبی علیه من اومده. همیشه کنار مردم هستم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/138778" target="_blank">📅 00:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138777">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAazcBfjS7i5c3aDpMFbDwJHineDTDXs55T8OqxnBqYUd-cw40Ja8jEEjR0i-c1HGBdAjEX3bfMq9v-1z8d8tk7BE4PsMu5wYY8eDLAlltQtbTTPJQNVaLI2ORC6YT-XK4dn37ztcbvx_0BdPFKku9_MblWQwOz2s5nwmkG3ZbdU0jJX5c3gRdi_dDSULlEOFSvWumMfoG556DLFyaFTLYrAnrvexk-rQGQzKqKmMXQ4YOlG5Ytjv2X8rXWLihWhnS_hyH1EwEw2FmPW7q8Tu0pSvH5Hs9FVJvBRrZea5RSXxLvZo-QeZTl5XZJGY67Rn1MI_gYclqjKw31t3jC1eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
جایزه بزرگ شهر هوشمند
🥇
نفر اول 500 دلار
🥈
نفر دوم 250 دلار
🥈
نفر سوم 200 دلار نفر چهارم وپنجم هم 100 دلار جایزه
به هم پوک بزنید فالو کنید
پوینت کسب کنید
🎮
لینک مستقیم بات
https://t.me/POUYAM_APPBOT?startapp</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/138777" target="_blank">📅 00:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138776">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
فایننشال تایمز: حملات پهپادی اوکراین ۴۵ درصد ظرفیت پالایشگاههای روسیه را از بین برده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/138776" target="_blank">📅 00:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138775">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ubn6zMpn-DMRszUO7Y_-jcIGWUBzJXTPiom2s6fpKGuApeylO_9L0_FNwQxre1p4I_h-Lf85CNZHYh8Rj6zSKm9M4Rq6k_roLZM_GAZlMFjreIZ_dl0Fxz9bC1sewAI2VODtQdPLP25VszuZcXhGADa3PsAqpraGgfoaR2Wkk0ajgCt6eKx8YmwhMlR_xEE3kOD9UKdxFlSGmNKIKHTYyIEMPyHmGSnr6S4GkCuaLW2o8IfUyWEMcY_GrTyoaZo1VOe6mr1fLfqCqzq1j4o9KmAihsNIsf3s9dLsg_uHmua8j2sqmmXMux1ILIZf5vLyWeozehuLuBfDw-iZWhR90w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی : مصر برای ما یه دوست و شریک مهم توی منطقه‌ست و امنیتش اولویت داره
🔴
همه باید حواسمون به نقشه‌های اسرائیل و عملیات‌های «پرچم دروغین» که هدفشون به‌هم زدن صلح منطقه‌ست، باشه
🔴
تهدید مشترکه و از اتحاد مسلمان‌ها می‌ترسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/138775" target="_blank">📅 23:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138774">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhJxFaKXESIMgNpgHz499_A0Fir1--fnjAyM-GZMMAC7YCWZIUt4QByNO8yKbRpCe2JhQyGxcVS0M3vayPk1dtsusWTymB-Wq4feaigw4fT4PCr5C0ZedOrz7PtdRJXxv7UyPrvne7xc1CMFU8uD-Fc0eOPbTA-z6iLNNIsyEmj3c-g56P4XvlShWNRtRMQGDVypBeQJusPArnubpsqxkq_5ppUfAsYDb36whd8UC6xRBjkKEONIWAqWXPxXmdpeZqsq1iVb6oyshYYBQuj4m4SjlBA0DErupsmYn0K5nWgZcA5z524WqsWDozPPTsgPe-qDsflLdJCSLA0m-l8Ffg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابطحی: احتمالاً احمدی‌نژاد جاسوس دوطرفه بوده است که کاری با او ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/138774" target="_blank">📅 23:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138773">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9bkAgF-duUKPS2aS0LBTuLglRXARJOypEke6tCKzXL5mflXYAGDbBULypDLJINX-Z616ioF5pBaAxmjj-glvbNv94bN3t3WrCuP1KuqNBbrYuGQf50UcPUrKs0cYlx0cniP_5zTosKe1qP3sIgRCLO2IlTKk03MQwHwG9w5mwa0Cv6TUOIbANdEhuDYWy7riFQPggfe4aUY2yJwVcRbZefPFPWqkafbgfmY47rKjh2YB2LKWu70k60-H_Nrj8FYkkjCCUxq_LD7UaVzxZxmMuHxGhYi42YaQrd9YZitLLoAuBmxF_VtVgq42ZODMNNxZExeoZT913M8l6OL2sL0YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۵ماه از غیبت صغری گذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/138773" target="_blank">📅 23:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138772">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
آی۲۴ گزارش داد یسرائیل کاتز، وزیر دفاع اسرائیل، به همراه ایال زمیر، رییس ستاد ارتش اسرائیل، نشست ارزیابی امنیتی برگزار کرد. در این نشست، آخرین وضعیت اطلاعاتی و عملیاتی، سطح آمادگی ارتش و طرح‌های عملیاتی برای سناریوهای مختلف بررسی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/138772" target="_blank">📅 23:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138771">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
اسرائیل منطقه المنصوری در جنوب لبنان را بمباران کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/138771" target="_blank">📅 23:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138770">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
فرمانده قرارگاه مرکزی خاتم الانبیا:
آمریکایی ها متوجه شدند تابوت هایشان بخشی از تجهیزاتشان در منطقه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/138770" target="_blank">📅 23:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138769">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwuiLwAav9qsSEJGuywz632qWP9mfOgXonV6vF-ogRi_SsYzdleOL6nBzW6VupyzIDLU7WRh5VCgZdfSIrd3LcI_rGzwy7G-Jcnlto833-pwJ1FrFjk-bGPlC2LUKoQWlzE_N5KZQya6pTlk_-Y6943a_YQEjscpQC_4X0d4Y2KgvuUuahT3v4VZPX93FPa3Hs9uClopdt2GSQj7XBSPdE2IXyizNzvTnyLkSKiqt5wH8bpV8I76MNtkLYkMTmKAd7Sj8fjIvD8tcFTjyHoUpHF3-LHlyhB_XL1m6YYEAeTqY30f60JbNNpduJHJulIHFhlTN5oFaTyrDJdR_cf5nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: تنش‌های آمریکا و ایران ممکن است همچنان مهار شده و بخشی از یک استراتژی مذاکره باشد.
🔴
مذاکرات با مسقط در مورد تنگه هرمز متوقف نشده است؛ نتایج آنها آینده تنگه را برای سال‌های آینده، فراتر از مدت زمان تفاهم‌نامه، شکل خواهد داد.
🔴
هرگونه توافقی در مورد تنگه می‌تواند راه را برای لغو محاصره دریایی و تحریم‌های نفتی هموار کند.
🔴
خوش‌بینی محتاطانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/138769" target="_blank">📅 23:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138768">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سیتنا: طبق گزارشات دو روزه سرعت اینترنت سراسر کشور کاهش پیدا کرده و اینترنت دچار اختلال شده،پروکسیا اکثرا مواقع قطع میشن و یا به زور کار میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/138768" target="_blank">📅 23:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138767">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
حیدر العبودی، سخنگوی دولت عراق، اعلام کرد دولت این کشور هیچ‌گونه اطلاع قبلی از حملات انجام‌شده به خاک عراق نداشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/138767" target="_blank">📅 23:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138766">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏
👈
وزارت امور خارجه قطر: هدف قرار دادن دو کشتی در بندر دمیاط تهدیدی مستقیم برای تامین انرژی جهانی و رویکردی غیرمسئولانه است که امنیت منطقه را تضعیف می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/138766" target="_blank">📅 23:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138765">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ناتو: ایتالیا، اسپانیا و ترکیه جنگنده‌های خود را برای تقویت گشت‌های هوایی، به جناح شرقی ناتو اعزام می‌کنند
🔴
این اقدام با هدف تضمین بازدارندگی انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/138765" target="_blank">📅 23:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138764">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f455635e8.mp4?token=RuuAs91IJxt2It7SLkzWPip4RXS6W081Vdv5kWGPAjep6JhP6JaI7SpgIxKh58RsFbLGaVBDipFL8x1QUKoWHDqA_4OC4QLkcMHeuOtyUVwbLuZKRw3wBU6hQFBdhGEWK92kQmNoMRPEj7O0MXWySlF5YJqx3gGuUFt164vLUnlhYwzQb7N1sJ_QB_x0LWUCJDSL4fG1wdJhBLmdu3fp5vRc9fzaOV9DY4ywICkEyGWvMZXbBJY0L_h74peNHgeOT4R7lTeQozSHDwfWxpgk1ORtYRJWwttD4kvOvP7hN7QmzHuUSERRvlxdn29FUSh-DSJ9uEBb81MB0azC_XSgTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f455635e8.mp4?token=RuuAs91IJxt2It7SLkzWPip4RXS6W081Vdv5kWGPAjep6JhP6JaI7SpgIxKh58RsFbLGaVBDipFL8x1QUKoWHDqA_4OC4QLkcMHeuOtyUVwbLuZKRw3wBU6hQFBdhGEWK92kQmNoMRPEj7O0MXWySlF5YJqx3gGuUFt164vLUnlhYwzQb7N1sJ_QB_x0LWUCJDSL4fG1wdJhBLmdu3fp5vRc9fzaOV9DY4ywICkEyGWvMZXbBJY0L_h74peNHgeOT4R7lTeQozSHDwfWxpgk1ORtYRJWwttD4kvOvP7hN7QmzHuUSERRvlxdn29FUSh-DSJ9uEBb81MB0azC_XSgTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نوید کلهرودی: ایران با جمهوری اسلامی هیچ آینده‌ای نداره و مردم روز به روز بدبخت‌تر میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/138764" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138763">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری/شبکه 13عبری: ارزیابی‌ها حاکی از آن است که ترامپ دستور گسترش دامنه حملات علیه ایران را صادر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/138763" target="_blank">📅 22:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138762">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hGu3j5M-yEcCRHuSWIZ1ZQHdMDi_hkNBNO0ksHhram7LjtLkqXngA7mnplF81WmQC44dr_pJZSC2sR5HJGnMfWaMavB_DOL94bvLz5RzdBpOVGDsuXT2kUFCxtObva66VfSRaKc6VMQalITiIycmo_Qvuh9U4lI3vlbGTA2lsb8Qk_gispdwURKUgZ8nJBz28ist2xaKMUgGcIzv0yzkif0SfXf29_hZmy0meIOr_eVAKvcur1upwnzjbjiI3J7M-9bGjOPNjSwcVGUsLbfdoLQXBfcBqEvvDQaveK0BqPz_ixz39L7Svl6wvMsqPDpNIO_IElzlU9DLmo0KWx9qxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه تایمز : سیا و موساد در جست‌وجوی آیه الله مجتبی خامنه‌ای!
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/138762" target="_blank">📅 22:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138761">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت…</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/138761" target="_blank">📅 22:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138760">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
جای اشتباه دلار بخری ضرر میکنی، جای اشتباه هم بفروشی سودتو از دست میدی !   قبلا بهتون گفتم روی ۱۵۵ خرید بزنید حالا خیلیا جا موندن!  ببینید فرق داره شما روی ۱۵۵ خریده باشی یا روی ۱۸۰ خرید بزنی، سود بهینه تر توی نقطه ورود دقیق تر و خروج بهتر هست ( کاری که…</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/138760" target="_blank">📅 22:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138759">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
مصر: عامل حمله به بندر «دمیاط»‌ هنوز مشخص نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/138759" target="_blank">📅 22:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138758">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uH7EIHcsSasW1nTrnen2_VDCosSSNjDm4Xqt1ecmoj8WkvN3S4XaEbzJZO5fg7WMC3FvzqwGtsukid_4tUnxqYvMibPuP12cQl1BXsKkt2cJ91q6bUD_8Ett-hG7an2PEH9CfQnlrm_9FmCsDN2ayeJhzK45_bdjOZxLWAjyxtz5hNahztr8IgBKje2FqsENpNt3jyN0rI5OVxkrSdFB-tGQCiKy-OQBpYnLm-6kXUnmTiRbzUo-2G5TuJgUxgfdMip4bRWFrfMC0UZa7VsMzIIZPpL4eCuQWI5EwxKHifZTt-mxr6Vj5WtkteutEAzOCG-HfDjtr9rDHPNE0ebqzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی: ائتلاف تحت رهبری عربستان حتی حاضر نیست کوچکترین اقدامی علیه اسرائیل انجام دهد؛ اما در عوض تلاش خواهد کرد مردم یمن را که از غزه حمایت کرده‌ اند، هدف قرار دهد؛ همه چیز اکنون برملا شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/138758" target="_blank">📅 22:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138757">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سنتکام :  کشتی تجاری رو تغییر مسیر دادیم  ۲ شناور را از کار انداختیم و ۲ کشتی رو بازرسی کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/138757" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138756">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
گزارش کانال ۱۲: جلسه هفتگی کابینه اسرائیل که قرار بود یکشنبه برگزار شود، لغو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/138756" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138755">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
گویا رژیم جمهوری اسلامی خیلی احساس خطر کرده و داره از همه ظرفیت‌هاش استفاده میکنه.
🔴
دومرتبه مجتبی شکوری و ژست‌های فرهیختگی‌ش رو از توی صندوقچه درآوردن!
🔴
باز هم ظاهراً قرار نبوده چیزی بگه، ولی یهو بار امانت روی دوشش سنگینی کرده، گفته بذار یه ویدیو از کربلا ضبط کنم.
🔴
یه‌سری کتاب جدید خونده، اسطوره‌های ایران رو با عرب تازی درآمیخته و به این نتیجه رسیده که اهریمن خواب‌های بدی برای ایران دیده.
🔴
حالا اومده می‌گه بیاید همه احساس وظیفه کنیم؛ به‌خاطر ایران، چشم‌مون رو روی همه بدبختی‌هایی که توی زندگی‌مون کشیدیم ببندیم و پشت جمهوری آخوندی بایستیم.
#پروژه_حکومت
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/138755" target="_blank">📅 22:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138754">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIeMD023xu_EqO3Hu2Act2SGosZvHWQ7GH8z_sWmdTyPRv5cH-qVZlcfoFhPlcHJNOK0GdgST5YC6OAeym08TxGscC0GpK4LoN3Qc-crPYj05DBJ3foUtSZNqAmdbtXh6NVXBU-iFTbOSgIQWNBb9Mc0EceI2GGPIIsYOsCk2Yqjj5vYIHmCaB-jNSp1UfKPS6Dv8B8RU7eGczX-oTUNbHHYvyfr_c2_DkNWe_UDx1IhMK518exA6a4CV5lizynGrVreiQ0bmyt1hUH1qwjTpbunZkTYbbPjgrGDs3lA33C37USTcEyuOPfwhnnzRvbw4Bn9tvrn0QRTrJ-_1oIomg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمااااااااااااام
😂
خانما تو فرانسه
🇫🇷
کامل لخت شدن رفتن زیر برج ایفل که اینجوری از
ایران
حمایت کنن، ولی همه جمع شدن دورشون و به جای حمایت از ایران زل زدن به بدن لخت زن‌ها و این کلیپشون نزدیک 15 میلیون بار تو جهان شیر شده...
+مشاهده تصاویر بدون سانسور
‌
‌*_*</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/138754" target="_blank">📅 22:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138753">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
زلنسکی: روسیه در حمله موشکی که منجر به کشته شدن یک خانواده اوکراینی شد، از موشک های کره شمالی استفاده کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/138753" target="_blank">📅 22:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138752">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مذاکرات ایران و عمان ادامه دارد ، تنگه هرمز همچنان بسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/138752" target="_blank">📅 22:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138751">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
منابع العربیه: سفارتخانه‌های غربی در بغداد ترددهای خارجی کارمندان خود را محدود کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/138751" target="_blank">📅 22:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138750">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: چرا سازمان ملل اسرائیل و آمریکا را محکوم نمیکنه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/138750" target="_blank">📅 22:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138749">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
به نقل از یک مقام ایران: ایران هرگز آتش‌بس به سبک آمریکایی را نخواهد پذیرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/138749" target="_blank">📅 22:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138748">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUbADb_4cBzOuvWr1_hZrP63RdVxTWRYGes5cyILZK86uVY5-qs535h1cRGg1Igu3oo2s4LIo1h4vsvm0uonmc7cwmPDIiEbw7hUYcCFylCVNUfoObTYNwNBsvhhH6bYJV83JhvS3WA3xMRCJNb7nAen1lYJUAZsBQxl07xsNNBq43my2_zcl6VCYVg7QpKApeMgaVHW5yk6-ZrjL4MiK4hZ85ZWzZ54eiockR4_YVmNucIPKlD0ETG0CaPf4ib-fWav3VTxKX1R1F92laBuao5eLrNqt9z5p8m5pb0yV36deFBiQDCjly_bznLhXXDp_glOIYCZTmnU2iAXvtLQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای سعودی در نزدیکی مرز با شمال یمن ماموریت جاسوسی انجام می دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/138748" target="_blank">📅 22:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138747">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
کمیسیون اروپا: هفت کارخانه بزرگ هوش مصنوعی را در سراسر این بلوک با ۱۰ میلیارد یورو تأمین مالی خواهد کرد، تا تلاش‌های خود را برای کاهش شکاف فناوری با آمریکا و چین افزایش دهد.
🔴
در پی استقبال شدید کشورهای اتحادیه اروپا، تعداد کل کارخانه‌های بزرگ از پنج کارخانه برنامه‌ریزی شده به هفت کارخانه افزایش یافت.
🔴
این کارخانه‌ها علاوه بر ۱۹ کارخانه هوش مصنوعی موجود در کشورهای مختلف اتحادیه اروپا، به بهره‌برداری خواهند رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/138747" target="_blank">📅 22:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138746">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd67ebb5e.mp4?token=EdHHjx17Ym2TJbuMsPVktVFXaaAYeGWwP9HDNb1zR9vu9AzGmol0C-11v2teeWkhRnpj6JIt0o4kFAeG4xT0eOCM78x5VBWVctwapT-Nc7OAhEwJs2hsdYWpg6Qntd5ZZ1-1a-_CQkx0YncyJ-oSsS8NdMNGtRYzFRW4Ak6auxxMrOO52EDWOY0uFFexqLxnlOU4V9MxzRLe_M8eaELxvzpLI80hAdfNQAcZzscHgEqS32gSoy7vhjREKL4Jr4w74onz8f9Cm4czQMMvdCFftxI18sncsjj6Y0gw47uEqEwcb47_XszAN3PVIoZDt56q8lhramo5z2rWeoGPulaMYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd67ebb5e.mp4?token=EdHHjx17Ym2TJbuMsPVktVFXaaAYeGWwP9HDNb1zR9vu9AzGmol0C-11v2teeWkhRnpj6JIt0o4kFAeG4xT0eOCM78x5VBWVctwapT-Nc7OAhEwJs2hsdYWpg6Qntd5ZZ1-1a-_CQkx0YncyJ-oSsS8NdMNGtRYzFRW4Ak6auxxMrOO52EDWOY0uFFexqLxnlOU4V9MxzRLe_M8eaELxvzpLI80hAdfNQAcZzscHgEqS32gSoy7vhjREKL4Jr4w74onz8f9Cm4czQMMvdCFftxI18sncsjj6Y0gw47uEqEwcb47_XszAN3PVIoZDt56q8lhramo5z2rWeoGPulaMYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش ایران اعلام کرده است که مرحله بیست و ششم عملیات «ساعقه» را با هدف قرار دادن تاسیسات آمریکایی در بحرین با استفاده از پهپادهای «اراش» انجام داده است.
🔴
به گزارش‌ها، این حملات به ژنراتورهای برق، سیستم‌های ناوبری و ساختمان‌های اداری و پشتیبانی در پایگاه شیخ عیسی وارد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/138746" target="_blank">📅 21:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138745">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
آمار کشوری میزان سرقت توسط نیروی انتظامی منتشر شد:  بیشترین دزدی تو استان های تهران، خراسان رضوی(قطعات ماشین) و اصفهان رخ داده و کمترین دزدی در استان های قزوین، قم و لرستان رخ داده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/138745" target="_blank">📅 21:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138744">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/138744" target="_blank">📅 21:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138743">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a94fdaf26.mp4?token=Kav3-Ipx4e8fQPV7WfEaTadnjNcuqjEVnKuerY3OhL7BvAlFxlkXpnjVGkaxrSzG7bOAqFpZ7jkGY34pJ-6kASMu-3m6Uj_8bppCHuhAdg2FK1MmRrZslmy5JQlF_XH_UC5m5FhqSAy1fOeNgwFcu_Y2lpAhIVat7fLV7pZ_pxxNwY4cfCpGQfOmdHw73y3YInnxoRGszmnc1Elxk1IVoAe5-YycHVnnq_p-iXReUR-d5m0MRrOkAJ_QXFlN5N2gjfVWW9xLEKska7m99FHLeDK9bJW_HE5yHAoTPvqBPmEafByviE5DWtgN7ssQXBOkoJP50voDSQ_l2FM3RMrPeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a94fdaf26.mp4?token=Kav3-Ipx4e8fQPV7WfEaTadnjNcuqjEVnKuerY3OhL7BvAlFxlkXpnjVGkaxrSzG7bOAqFpZ7jkGY34pJ-6kASMu-3m6Uj_8bppCHuhAdg2FK1MmRrZslmy5JQlF_XH_UC5m5FhqSAy1fOeNgwFcu_Y2lpAhIVat7fLV7pZ_pxxNwY4cfCpGQfOmdHw73y3YInnxoRGszmnc1Elxk1IVoAe5-YycHVnnq_p-iXReUR-d5m0MRrOkAJ_QXFlN5N2gjfVWW9xLEKska7m99FHLeDK9bJW_HE5yHAoTPvqBPmEafByviE5DWtgN7ssQXBOkoJP50voDSQ_l2FM3RMrPeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: انتظار دارید جنگ با ایران چقدر طول بکشد؟
🔴
ترامپ پاسخ نداد و رفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/138743" target="_blank">📅 21:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138742">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
گاردین: عربستان سعودی در حال آماده شدن برای حمله‌ای بزرگ زمینی و دریایی به حوثی های یمن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/138742" target="_blank">📅 21:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138741">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgOSfpIMN8KYJe7BSWn1rDCCPeG3JbrIR5VA-6d-t6fRaoxe4MAe-CogNfy7fUm04YMx3kgGIBq_7-nY2uZTUJvwI2g4QMhN-u2bWFsEE6mNwtuxZZUUo6ecAsByV0RNIJuUGDTqXDrmjK6dDCXRlf9Dgp9olm4SbSzVag-BrJIWsgrKZudoNvtXohyIKh5t3SACtRSCpbIk_xH423Ctdedf2yTD-RDei1YqhEl8hLF_Ap0lGaR5R_XIGExdwaZaV2tUu6sOf9big--rvXKc3dpHS1iOP2Ce5FPfSly2Mm3cryjDQ76BpoieW0yRFdD7ChYrYyWL2dMfFA61luGw5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
گلایه کاربران از زود تمام شدن بسته‌های اینترنت
‏
🔴
بر اساس گزارش‌های غیررسمی، ضریب مصرف اینترنت بین الملل به ۲.۷ افزایش یافته. یعنی هر گیگ مصرف ، ۲.۷ گیگ حساب می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/138741" target="_blank">📅 21:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138740">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOo9iPVqGwazQLcMn88vnbcmpa9zJcOs01xKbHG6eJ3YFQoLQCb0VUcwgrQ46mvJlArbRh2_2wyGmg2ukp6j9Q5jrWr-eP-7hEu7XyOINuPWRQUjoJkpA2anbEBGWH3Ff2HaUKwUHK7xKA9F00g-oQSeRLvW3ZjCVxfDSC1n_M0gTQZ5fvIe32bXO1Ze6gKTaAcA0jADsAcbLfl-c6QKHLTg0TUgy8YM8vrOkKYxPBj6lqYtSbdo3miy7MlXMgO28R30NCXcbKfHWza_LadDP0fzxWEdpo7a9dKl3zJH1kqUDKCHq_qzFXqHMQIMmEXpB8By6tFgBlWK91PimEhzVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه خارجی بستنی شکل باب اسفنجی خریده و از انباکس کردنش پست گذاشته؛
🔴
و اما کامنت یه ایرانی زیر پستش
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138740" target="_blank">📅 21:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138739">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
گاردین:
نیروهای سعودی در حال برنامه‌ریزی برای یک حمله بزرگ علیه حوثی‌ها در مرکز یمن هستند.
عربستان سعودی در حال آماده شدن برای یک حمله احتمالی زمینی و دریایی برای شکستن محاصره صادرات نفت از طریق دریای سرخ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138739" target="_blank">📅 21:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138738">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⭐️
اگه فیلترشکنتون اذیت میکنه پیشنهاد میکنیم یکبار امتحان کنید
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید (برای شرایط اینترنت ملی هم اوکیه)
(همراه با تست رایگان‌)
خرید وتحویل فوری از ربات زیر :
🤖
@SafeVPNXBot
✅</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/138738" target="_blank">📅 21:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138737">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scJwI2elfscniN_nlSVOaqNQFvPTceXZLn1BWZHHjgy5SZKlaxzE-ZjydD2dPHj-Z49knT3gAyoyLlpAUi3jTSVI66ElpjQZxCIsSGThh35VOQkEHDUiGxa0M1zJ93fGCyGrEatpExuKUPV7iykb4XdY9rB1n6eDeKMSD7TuAARHKZclDzIW1-W8f5TFF9EOpVcwosvo6GXH049bwUbzH-mLoQGteUN_hBzPYL9lUTZoG1F2cnNVrDWEEqbMcOtJ6bkllOsH9PmmWECP1BxX7hiDzuSMinUqDWJ2J87ulvohD9SRUrlvDY-7RKi4LEb_xb7qmsjEOTfvygo9DdccNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📍
تعرفه سرویس‌های مولتی و تک لوکیشن SafeVPN
📆
پلن های یک‌ماهه
📍
10 گیگ
➡️
35,000   T
📍
‌‌20 گیگ
➡️
50,000   T
📍
30 گیگ
➡️
75,000    T
📍
40 گیگ
➡️
100,000  T
📍
50 گیگ
➡️
125,000  T
📍
100گیگ
➡️
250,000  T
📍
نامحدود
➡️
400,000  T
📆
پلن های دوماهه
📍
10 گیگ
➡️
75,000    T
📍
20 گیگ
➡️
110,000  T
📍
30 گیگ
➡️
145,000   T
📍
40 گیگ
➡️
180,000   T
📍
50 گیگ
➡️
215,000   T
📍
100گیگ
➡️
390,000   T
📍
نامحدود
➡️
550,000   T
﻿
✨
ویژگی‌ها
✅
اتصال پایدار روی تمامی اپراتورها
✅
مناسب استفاده روزمره و شبکه‌های اجتماعی
✅
دارای ساب‌لینک جهت مشاهده حجم و تاریخ انقضا
✅
تک لینک اختصاصی بدون نیاز به بروزرسانی
✅
حجم واقعی بدون ضریب مصرف
━━━━━━━━━━━━━━
مشاوره و خرید
🏪
@safevpn_secureSupport
✅</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/138737" target="_blank">📅 21:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138736">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ارتش ایران: پایگاه شیخ عیسی در بحرین را با پهپاد هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/138736" target="_blank">📅 21:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138735">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGF11-xJdA8Zo4FOkbYmM5RvRdhn9PKRBLAygSEhqKXPhYDRvb9Hpnji_5aXGL3iD8u9n2fInxk-ISmV69iTiH4-1DxD8DVr_sfP6DDP6JGwDoCdGfPn5SUcnAVQHoj7CDML_1AJra6blvcDac4TinSEUN9P5NTnmdTp-EqJz4a5eGp3c3q6IjyYY34Tdfj8rBzFqtjXaeWJ2sX0eA72VC_Yag9CwVUlonsTqkvwgqSpF9uWJAf2oJy9Hr6Ar-L9BPFQiodyATEK6IaKwqL93Vitw2UDj9XhzmHx3eudLudg-3wm50ZxMLPHbF11TdTMH2yoeOBKroTPeNRaQBn84w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجله تایم
:
حجم فزاینده‌ای از اطلاعات جمع‌آوری‌شده توسط سازمان‌های اطلاعاتی آمریکا نشان می‌دهد که روسیه، حمایت‌های حیاتی مالی، اطلاعاتی و نظامی از ایران ارائه می‌دهد.
🔴
این کشور از افزایش قیمت‌های جهانی انرژی و کاهش تحریم‌ها برای تثبیت اقتصاد جنگی خود استفاده می‌کند، در حالی که درگیری‌ها را هم در خاورمیانه و هم در اوکراین طولانی‌تر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/138735" target="_blank">📅 21:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138734">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
نتانیاهو پس از بازگشت از آمریکا، مستقیم در پایگاه هوایی نواتیم اسرائیل فرود آمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138734" target="_blank">📅 21:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138733">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd5adde968.mp4?token=pk23CaJ2XiADpe4uLc9rOndTd4HQsaVzYia7XnjDcxF2rfW1gcdu5y4ocbU0XBkikYMaA_p1FowLnQpWFDzNwDz2agsy7Zgzcoa3y3Wz8lhwq551bKYOcehj4gG38TYEWVi-alA_SnKpNQoYxNfS2bxgnjVcUJzjrW8VGr42AC7bjrN0G4lMq24k0-WQ6db9KL8ABhGkk1M9msxLYGlQvWbA9LqokJtpILtcR8Jz8_GlV3KNcUqRi8PjxVjGdTS7U6_Bqerf_aNebIcUkpIzW_JcrO9VWx6eqkY3NVOzLk8EYvAs1yMuaqK99GeukMRvM0lTIIIgCzuZRIHgPmOLBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd5adde968.mp4?token=pk23CaJ2XiADpe4uLc9rOndTd4HQsaVzYia7XnjDcxF2rfW1gcdu5y4ocbU0XBkikYMaA_p1FowLnQpWFDzNwDz2agsy7Zgzcoa3y3Wz8lhwq551bKYOcehj4gG38TYEWVi-alA_SnKpNQoYxNfS2bxgnjVcUJzjrW8VGr42AC7bjrN0G4lMq24k0-WQ6db9KL8ABhGkk1M9msxLYGlQvWbA9LqokJtpILtcR8Jz8_GlV3KNcUqRi8PjxVjGdTS7U6_Bqerf_aNebIcUkpIzW_JcrO9VWx6eqkY3NVOzLk8EYvAs1yMuaqK99GeukMRvM0lTIIIgCzuZRIHgPmOLBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنای آمریکا با ۵۰ رأی مخالف در برابر ۴۹ رأی موافق
🔴
طرح محدود کردن اختیارات ترامپ برای اقدام نظامی علیه ایران رو رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/138733" target="_blank">📅 20:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138732">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا نام یک فرد و ۵ شرکت مرتبط با شرکت هواپیمایی ماهان را در فهرست تحریم‌ها قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/138732" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138731">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/140b26266f.mp4?token=Vl_siB5Rb6X5a2byc6qD-R5AfjRCfgGFRHTsblhJrLoD3DQArben6hl4IkZ0K0sk6JTNlCNkfMmrO4WW62ekvXNLSl24dMyajdyCwMnvxoWWMi-tHBq4V8utNYEy1EclVkXKYYbQLU76FJJpqLp1q2Iv-bNGZWIgbKCpzal6nMj9HcN9g2ViJ5N2fX9gExuoGnAplanJhsNk01vi2dJenohCFwu6nkHX-sKVvDmxwovOt8CB0dUFAkJs1AE4uJigbWtAmLUfzCj4vktUtMFQ0FhOFbz_gdgkYcKDgd1tEIRatIuMWXfkwlV6h1fQ47EwzVhReiMga6-8_LjfQaRkdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/140b26266f.mp4?token=Vl_siB5Rb6X5a2byc6qD-R5AfjRCfgGFRHTsblhJrLoD3DQArben6hl4IkZ0K0sk6JTNlCNkfMmrO4WW62ekvXNLSl24dMyajdyCwMnvxoWWMi-tHBq4V8utNYEy1EclVkXKYYbQLU76FJJpqLp1q2Iv-bNGZWIgbKCpzal6nMj9HcN9g2ViJ5N2fX9gExuoGnAplanJhsNk01vi2dJenohCFwu6nkHX-sKVvDmxwovOt8CB0dUFAkJs1AE4uJigbWtAmLUfzCj4vktUtMFQ0FhOFbz_gdgkYcKDgd1tEIRatIuMWXfkwlV6h1fQ47EwzVhReiMga6-8_LjfQaRkdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
المیادین: اوکراین از طریق میانجی‌ها در تکاپوی کاهش تنش با ایران است
🔴
ویدیو منتسب به تهدید ایران توسط نیروهای اوکراینی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/138731" target="_blank">📅 20:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138730">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwCb3xRFG3-2MtF84f5e8-fhHA7EO-_K4vSMR8VI8MEcWtHNbBE1svu6NbD4V6cotGFsSUI-Ij9P8chc3Js4QmHJfVnM8S0o-W6PBo6Bkilr8XP0OFFV_v4NEqzoKDsyuAAXuiIbSHK4JBDDdljndNAU-0qF_jHgb3S8KRTFhhNOpkV6kpPxtuCrAPxC2XIO1mBKPlwXBRzpe6AK0RX6BLJwhgmVL_wWqAOKqYqjCdMKJ62bLTA-QPKFlYfGrQY3taSN_7CVtCZs72Y3pL___t8ejYRb3rWS1kksHhmbNyeHL0sWEP2swBO4ieHp6UCLy0zHP75LOjW8C9FPKD9DVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاول دورف، مالک تلگرام مالک تلگرام با انتشار این عکس نوشت: روسیه، من را به عنوان یک "تروریست" معرفی کرده است، زیرا از پذیرش درخواست‌های آن برای نظارت گسترده و سانسور در تلگرام خودداری کردم.
🔴
طبق قوانین روسیه، من از "انتشار اطلاعات در اینترنت" ممنوع شده‌ام.
🔴
به نظر می‌رسد مقامات روسی در مورد اینکه چه کسی می‌تواند چه کسی را از اینترنت منع کند، سردرگم هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/138730" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138729">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ao0H8uVrxkh7YdJiAQ94cBIQoqw2qX15RP1sZN_wk1epEJbOIid2M-sIlnMeyyTNrOhWRwigOs_Czl5JGO1TVHsJbBNl7WgDTTbmw36ovRIHQi_e6OA9k5EQTRCXDZt7phldsVzcu7qBmSg0RhjLcileHh1ayraTtxwvb6FiDG4VtFQHJYqD9sLtHz5xFhhXTsS90VVN3Sx-MlqCgeOB9BF_KrzI_asADFF1fbyHNVScgr7jURp2d6UZKb2Le8Tq8NnWlWFfdHu70astPqovkMWOCKhfL2SnS4Ig6bsqbVXYq9V5OEfvA_sA_X8nmphvtT0Kd8QaiDMVjZm2PVFuKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایلان ماسک کمپین خود را برای تقویت جمهوری‌خواهان در تلاش بزرگ انتخابات میانی احیا می‌کند
🔴
ایلان ماسک در حال فعال‌سازی مجدد کمپین آمریکا خود برای تأمین مالی عملیات گسترده مشارکت رای‌دهندگان جمهوری‌خواه برای انتخابات میانی ۲۰۲۶ است که هدف آن تضمین کنترل کنگره توسط حزب جمهوری‌خواه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/138729" target="_blank">📅 20:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138728">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
عربستان سعودی رسما تشکیل ائتلاف بین‌المللی برای حفاظت از تردد کشتی‌ها در دریای سرخ را با حضور ۱۴ کشور اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/138728" target="_blank">📅 20:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138727">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
آمار کشوری میزان سرقت توسط نیروی انتظامی منتشر شد: بیشترین دزدی تو استان های تهران، خراسان رضوی(قطعات ماشین) و اصفهان رخ داده و کمترین دزدی در استان های قزوین، قم و لرستان رخ داده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/138727" target="_blank">📅 20:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138726">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6bbb7af4f.mp4?token=gJLjzfZLvI3teUMeAUcxxTqJ1uYdDKGafVeiyQn_entyM6kQ0YcOpKFEOD-Ph6njQrhL31QYA3W0pXZ4xbYumV35-Kz49MgjEeAYp6F39qt2VqgJEsAd4lPM-actzEOlYMkWnFJByqjztmXazaJKZ62NQRujeyx_aySl0D5cIYeCI0rZXeLgw3Vt7DcIG8-eOgOBHEXhQcJtiD7Q2f5tpLBudsHxosrWGTcDWLLIoUd9wIMlqCNkcQnuzQqlGasERpShWZZ9jyx0cJnZJZnHDGYbPzW8F3qTw0d44_nrw49QKHXI0Kp3Kvs7ByI8oPa1NJA4Nd_uO0Q_NtnyrfewIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6bbb7af4f.mp4?token=gJLjzfZLvI3teUMeAUcxxTqJ1uYdDKGafVeiyQn_entyM6kQ0YcOpKFEOD-Ph6njQrhL31QYA3W0pXZ4xbYumV35-Kz49MgjEeAYp6F39qt2VqgJEsAd4lPM-actzEOlYMkWnFJByqjztmXazaJKZ62NQRujeyx_aySl0D5cIYeCI0rZXeLgw3Vt7DcIG8-eOgOBHEXhQcJtiD7Q2f5tpLBudsHxosrWGTcDWLLIoUd9wIMlqCNkcQnuzQqlGasERpShWZZ9jyx0cJnZJZnHDGYbPzW8F3qTw0d44_nrw49QKHXI0Kp3Kvs7ByI8oPa1NJA4Nd_uO0Q_NtnyrfewIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
میلاد کرمی(وضعتان چونه) داره واسه رفتن مردم از مرز مهران به کربلا تبلیغ میکنه :
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/138726" target="_blank">📅 20:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138725">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حوصلم سر رفته بود این گردونه صراف رو زدم، 5 دلار داد
😐
😂
گفتم لینکشو بذارم شما هم بیکارید یه تستی بکنید ببینید چی میده بهتون
👇
https://r.saraf.app/s/agrd220</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/138725" target="_blank">📅 20:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138724">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
نتانیاهو آمریکا رو ترک کرده و الان به اسرائیل رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/138724" target="_blank">📅 20:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138723">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
( فاکس نیوز) هانیتی : اگه نتونستن جلوی هسته‌ای شدن ایران رو بگیرن، چطور می‌خوان تنگه هرمز رو کنترل کنن؟ هیچ اهرمی ندارن، همه‌چیز تموم شده.
🔴
نتانیاهو :  نمی‌تونن، اما من خیلی خوش‌بین‌ترم، چون روحیه مردممون رو می‌بینم؛ اون‌ها خیلی شجاعن
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/138723" target="_blank">📅 20:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138722">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
الجزیره: سنای آمریکا نسخه جدیدی از قطعنامه اختیارات ترامپ در جنگ با ایران را بررسی می‌کند
🔴
این طرح رئیس‌جمهور آمریکا را ملزم می‌کند که در صورت نداشتن مجوز رسمی کنگره، به درگیری با تهران پایان دهد
🔴
سرنوشت قطعنامه مذکور، به این بستگی دارد که چه تعداد از جمهوری‌خواهان بر خلاف موضع حزب خود رأی دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/138722" target="_blank">📅 19:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138721">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وال‌ استریت ژورنال : مقامات مصری، ایران را مسئول حمله به بندر دمیاط دانسته‌ اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/138721" target="_blank">📅 19:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138720">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
نتانیاهو: زهران ممدانی، شهردار نیویورک، ایران و حزب الله و حماس رو حمایت می کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/138720" target="_blank">📅 19:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138719">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
زلزله ۳.۹ ریشتری عراق در مرزهای کرمانشاه احساس شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/138719" target="_blank">📅 19:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138718">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe1662f40.mp4?token=t2oF5JsvB29OA8wKBOJrzeKgAw2PPuPjjhreLRuQPtzNarYmv58DgPvZzbtsNv3sj-EcUQUueS5pTJQQKUGNwBJyqEFuzcxzpttrq_WqMvqFomoxxDAiIXQFiThqucU4pz2jECGN59NPNN8NeNoipOppuFYIi5dw3Us2vyqaxpUuVBXOVmGRR8N2UrxNJvjX4HXdlbxnAO3Jp8U6oov3xsdqcxiOpP0kjqauLz4BorXGYtPu8bPggGlWKPffHPayQZgvZJcPgZrj4j_X8KJm7obo2QciqjZs8mU1H-NlxbknZZy48tjvRaTY9qjEeC_ZEhbRZGMSDtDZBENkRLQ9D48sA8M4-tOyNTy2pTby6S0uCsOGd9rafhSrshvKPaFSnmYwrBAdep6g99FgQz8VwgPt3017kK7HQXZ-W0Kuex5xevvkqCAPEoUfCRhXFzCGXkAPdtaMK7WS9ES_f7N-os1vjBy0XNHuhjMnBj0Q84d7t2Iofg-2bRz4kIl1wUWdV4PvCmnSzt_zOqBshCk-BkOPkPHaWyTyK-UhXIm2Ndfg48dTXMb-ZyimoKAALF37zEWDKb-acrDnEWOj8cQw_tjGclexKNFWFF9MUDA3nH3as4AqsUmMyMsmBy1IRQq-foLU_7yqOtD8KJX-qOG0ATa2OIdquaGyvq0KjlnbDg4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe1662f40.mp4?token=t2oF5JsvB29OA8wKBOJrzeKgAw2PPuPjjhreLRuQPtzNarYmv58DgPvZzbtsNv3sj-EcUQUueS5pTJQQKUGNwBJyqEFuzcxzpttrq_WqMvqFomoxxDAiIXQFiThqucU4pz2jECGN59NPNN8NeNoipOppuFYIi5dw3Us2vyqaxpUuVBXOVmGRR8N2UrxNJvjX4HXdlbxnAO3Jp8U6oov3xsdqcxiOpP0kjqauLz4BorXGYtPu8bPggGlWKPffHPayQZgvZJcPgZrj4j_X8KJm7obo2QciqjZs8mU1H-NlxbknZZy48tjvRaTY9qjEeC_ZEhbRZGMSDtDZBENkRLQ9D48sA8M4-tOyNTy2pTby6S0uCsOGd9rafhSrshvKPaFSnmYwrBAdep6g99FgQz8VwgPt3017kK7HQXZ-W0Kuex5xevvkqCAPEoUfCRhXFzCGXkAPdtaMK7WS9ES_f7N-os1vjBy0XNHuhjMnBj0Q84d7t2Iofg-2bRz4kIl1wUWdV4PvCmnSzt_zOqBshCk-BkOPkPHaWyTyK-UhXIm2Ndfg48dTXMb-ZyimoKAALF37zEWDKb-acrDnEWOj8cQw_tjGclexKNFWFF9MUDA3nH3as4AqsUmMyMsmBy1IRQq-foLU_7yqOtD8KJX-qOG0ATa2OIdquaGyvq0KjlnbDg4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شان
هانیتی
: اروپا قاره‌ای در حال افول است.
🔴
نتانیاهو: من با شما موافقم. و می‌دانید، مطمئن نیستم که از خودشان دفاع خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/138718" target="_blank">📅 19:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138717">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سنتکام تمام ادعاهای سپاه پاسداران را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/138717" target="_blank">📅 19:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138716">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mg1ZJJSewzYUo2eVNWhzKkM0RqWG4R72wOYaemY7XYyKFGmmjUUQ2Zp-FwOF3-M_S2ADVE26w9vmy023kqJ29_0eys27WkLQ8k-RTwvSVUWhLw-eJqcsHhVj699GTF9Lth9iY_Iy5xA2F7gTTivjgcSlMZjrMNyH6pnDmJR9XiP8iTmavqlRBqDIInDjOUE-BOgawcNBzT1wgvTvLbQlfq0_Ae7Cex0xYsAL4uJoBYCswJFJE3nyoHDh9UgoAvvIPnadmWI-SaBgO5W4Qu7XwYhKpB85ZZuJh9YY7O69VvE6hju8ybDaXK_HKRJgYT4BrSrn42Ewd2xLnfhP0U6gjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام تمام ادعاهای سپاه پاسداران را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/138716" target="_blank">📅 19:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138715">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cmS2IuCNDB_f9I2aCL-cACGzom2ZO6iF7VQ-RbCvsoWveLR1Rj6lenZAzCeort90CoohqXTyLmxR7a5zZq7Bfj_qbMX5iy20n3Vyk0hNLf9CvnoWzrmmwT7kf1e7UKw7lBKxyy1hk2pGp5q2SXQP1gmDcvmacvojGM7-T6Uv6-H1n2SC48t2qj5x44K-uATIsuw-ut4huyMAfADRbeYc2q1DuLroeNHmIV0B0_eqqpT8Tt1L7E4f-OP_ySKeGenc4fTCnUNOL-6Ie2wuz7y0Li05Twl3nN6ISdCFHKFQtub_Xupii44VCOJR3P3OdvAmbNWdE5_-Vml66FTwgbE4SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز، با استناد به دو مقام در غرب آسیا، گزارش داد که انصارالله این هفته از خاک عراق و با هماهنگی گروه‌های مسلح عراقی و نظارت از سوی سپاه ، به عربستان سعودی حمله کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/138715" target="_blank">📅 19:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138714">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGLksFHrKlN3XlfK8jFJWLHpwgH1heQucoojoibU3dAySwtf2ORBk7UyktmoaZjajDuSPO3lU-mBO9ZTsTAG2mrxj_xGlYEKCHGc6-QqLMtSILzegoTCcT1Csui0DOeKN5IckrTGIpAMSIomYI_en8f8s4m1xSCmo6uubNAXRcPrjnTpkirotYjistbq4szIT7VGc6NoRUOr9DCyjFdC_ycr0ilUyAbTfcFcqMlveAnJUWylx40FhQpTPhcEBnLdTAlcD4-jhkhKerRm1SDC6lZxzz2JFLkH0ThLcZw_9J3fyG4zsvqILW_cnwd6Rgp82kI8zROG6Ed8Sk6lz1Fd5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ،  از طریق شبکه اجتماعی Truth Social: تاد بلانچ یک ستاره است و همه این را می‌دانند! او پتانسیل این را دارد که به عنوان یکی از بزرگترین دادستان‌های تمام دوران شناخته شود.
🔴
با این حال، جان کورنین از ایالت تگزاس و تام تیلیس از ایالت کارولینای شمالی، که هر دو نفر از آن‌ها را من از حمایت خود منع کردم و اقدامات من باعث پایان دادن به فعالیت‌های سیاسی آن‌ها شد، از رای دادن برای این نامزد برجسته خودداری می‌کنند. این نامزد در هر صورت، به عنوان سرپرست موقت باقی خواهد ماند. به یاد داشته باشید که هم کورنین و هم تیلیس، به مِریک گارلند و دیگران (که تعدادشان بسیار زیاد است) رای دادند.
🔴
من هیچ اعتراضی به این ندارم که به طور موقت نام تاد را از لیست حذف کنند، اگر آن‌ها کار درست را انجام ندهند، و پس از خروج کورنین و تیلیس از سمت خود، دوباره نام او را به لیست اضافه کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/138714" target="_blank">📅 18:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138713">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJscOglPKobap4lJxJhC0pAg2WIjc_YCuh3XyWfLlIjYSZaGz33zzVr4rCq4qyegvnfz-nS0N346iby4rjHAgIgorQmDb5LIjhrUsNq_T40jC1tnem_m1GZZRVflSWaq2crvExqViLqi1rqHsIWjb59I0xDUeh7FqsaAluw-zzoD3EMd0eg1T82hFP3OUK3nhLUgFW6x68wIECkSXU0i1SJwrX215Z0iLsNJ58F9Of00Ykox7qMWjmzYpxfUNIxydJ2UOc9TzZHeMSk66xAnQg0ptJmUEZzs8f8qrp_HDHmICQaxxG3SVJr7mkL1GIXiHSx2X5D4NifkQSLD38IJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویری از صنعا، پایتخت یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/138713" target="_blank">📅 18:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138712">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04131030f2.mp4?token=EbgBLqoX3ogo4Ta6NGiJUuyMU5ZA9df6WuoHkpgAkpjq7rGGShPpNZ7UNH2dRYRsTNI49BgxhzLeII7rrUIIufmUVP4sBJwpYuen0AWRRVwFJGqaK2aoterY4oRVq4ppIPwZjEeK_OhOybAWMzrJGjSWM_8mIMSUSapkW1Ha6hrlZERpc2tyuwy0xtBaY5HSjMWNmCB0D7nj8wyk8NMArEPREzrFJByrKGCy4vmVc5qCR78SB0AXioXHFmhcAGqwtwiiOY3DmhR4KJAt7dPxHsIiypuQTWkul3hxgs4MzB59SDx-FmyeXyLl5wJ7EqmANk_fEjj7YzqdkO_XWwsPMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04131030f2.mp4?token=EbgBLqoX3ogo4Ta6NGiJUuyMU5ZA9df6WuoHkpgAkpjq7rGGShPpNZ7UNH2dRYRsTNI49BgxhzLeII7rrUIIufmUVP4sBJwpYuen0AWRRVwFJGqaK2aoterY4oRVq4ppIPwZjEeK_OhOybAWMzrJGjSWM_8mIMSUSapkW1Ha6hrlZERpc2tyuwy0xtBaY5HSjMWNmCB0D7nj8wyk8NMArEPREzrFJByrKGCy4vmVc5qCR78SB0AXioXHFmhcAGqwtwiiOY3DmhR4KJAt7dPxHsIiypuQTWkul3hxgs4MzB59SDx-FmyeXyLl5wJ7EqmANk_fEjj7YzqdkO_XWwsPMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عبدالملک الحوثی: حتی چهارپایان و الاغ‌ها هم از دست رژیم سعودی در امان نیستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/138712" target="_blank">📅 18:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138711">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
اکسیوس: چین با ۴۰ درصد کاهش خرید نفت موجب جلوگیری از جهش شدید قیمت‌ها در پی جنگ و بسته شدن تنگه هرمز شد
‏
🔴
چینی‌ها استفاده از ناوگان عظیم خودرو‌های برقی، زغال سنگ و انرژی‌های تجدیدپذیر را افزایش دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/138711" target="_blank">📅 18:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138710">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فوری / گزارش ها از حمله به صنعا پایتخت یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/138710" target="_blank">📅 18:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138709">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64267a25b.mp4?token=BiGRpJa0KFR76ZMhd5oscl-sxtoOXsOo0peR5TH6dz4Y1A7RmNu6h4Ch6tCWeAVyMzcu0MGKREdE48SwNh-okzV3jRJ0SzfSDFWH5ajvsdmYtxWreBOwAkbJ1HfEa-4wPaKmjrEYP8XZLQse9MctOtX2qVrd791eGy-IIVg5GVeojeXOJxxhqFghC13dNWYNME5vo0Y50pVhy3g52htst48rLj5RQK-IYxLLMvj8GIqCfWb00A_iio78_Sz2GSes5nAR_7G-8kIbOOLVZKqzsP2Cb07qelGVaHhxNXq6KeA1EMzf6JlIEDMSAR2NKOeYyyUvi09JlP0ubD8zplzp8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64267a25b.mp4?token=BiGRpJa0KFR76ZMhd5oscl-sxtoOXsOo0peR5TH6dz4Y1A7RmNu6h4Ch6tCWeAVyMzcu0MGKREdE48SwNh-okzV3jRJ0SzfSDFWH5ajvsdmYtxWreBOwAkbJ1HfEa-4wPaKmjrEYP8XZLQse9MctOtX2qVrd791eGy-IIVg5GVeojeXOJxxhqFghC13dNWYNME5vo0Y50pVhy3g52htst48rLj5RQK-IYxLLMvj8GIqCfWb00A_iio78_Sz2GSes5nAR_7G-8kIbOOLVZKqzsP2Cb07qelGVaHhxNXq6KeA1EMzf6JlIEDMSAR2NKOeYyyUvi09JlP0ubD8zplzp8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عمران عباسی، عضو کمیسیون آموزش مجلس: یقینا در مهرماه گشایش مدارس را نخواهیم داشت. تمام تلاش ما بر این است که در اول آبان یا در آبان ماه بازگشایی مدارس را داشته باشیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/138709" target="_blank">📅 18:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138708">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری / گزارش ها از حمله به صنعا پایتخت یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/138708" target="_blank">📅 18:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138707">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
جنگنده‌های ارتش اسرائیل شهرک «النبطیه الفوقا» در جنوب لبنان را هدف حمله قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/138707" target="_blank">📅 18:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138706">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NllvpJEKVEC_hTgT1s-igfjKA7UkGFOAczC8P3rmq9Rk9yK_Tw9vajsP0X7LmcIwoIEUMuqbwq7iCDxhPzKCHBGjwv8jJQ_gpmS7Hv_3wc4g7PIJUnD0oy7uIRlXeRLY-HCGxBESWR-MyqkNFqsTSvFeXr3jH9CuXPjdi7sg7tS3wk3wZO2z_5JXRpA4xw-oaTASZPz35gRAZTNhLrmwNXWD__Meh1yfqbuatRKW5iRNYF7PKxNLtUiKgRL7VPffrlbWxXuiIyK60l4KgmD7O0QT9eER_BCj6I-N5M-dWc_4WKHt2VKVipLcdiyOHB9Qive0SQdM_R-tceXTlwilIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبیل فهمی، دبیرکل اتحادیه عرب پنج‌شنبه هشتم مرداد هدف گرفته شدن بندر دمیاط در مصر را اقدام تجاوزکارانه غیرقابل پذیرش، محکوم شده و علیه امکانات و ظرفیت‌های مصر دانست و درباره توطئه‌ها برای گسترش دامنه جنگ هشدار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/138706" target="_blank">📅 18:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138705">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
فاکس نیوز:ارتش آمریکا ، امروز گزینه‌های مختلفی را برای انجام عملیات نظامی گسترده‌تر علیه ایران به ترامپ ارائه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/138705" target="_blank">📅 18:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138704">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
دولت روسیه صادرات بنزین، سوخت کشتی و گازوئیل را تا پایان ژانویه ۲۰۲۷ ممنوع کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/138704" target="_blank">📅 18:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138703">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e39f1520ea.mp4?token=FWKMqZ1YTm_rxrGg-7C11ASH5b916z9T4UoeokSBM2k142RuQsg2S91D6iAvfA4dUhNLcTmcJ5ODklsEPqGHm19SMYoABlnqROR-2zefqkkJ9NkmbBP4etzXe8GCAq9nv_J4fGYPY0rpG9klGu-HTXYNU-7ozoRmBRUEn-4Cn0cvE_EqvJdWgHuaCeOaOpxWcYVAFwmM-XdP5WlJlgn8BO8BpQyJ63NO1WWgH2Kfhemi2WjMwnT3_bXTEHrektmCo1pB-tNAljWDcw8uGZpE0GBeIVpM1JjKf0boIBI-9JuGRiNw8q1ShZtnGpCEh4Ja4JDmDO02RJy32X9pKJCb1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e39f1520ea.mp4?token=FWKMqZ1YTm_rxrGg-7C11ASH5b916z9T4UoeokSBM2k142RuQsg2S91D6iAvfA4dUhNLcTmcJ5ODklsEPqGHm19SMYoABlnqROR-2zefqkkJ9NkmbBP4etzXe8GCAq9nv_J4fGYPY0rpG9klGu-HTXYNU-7ozoRmBRUEn-4Cn0cvE_EqvJdWgHuaCeOaOpxWcYVAFwmM-XdP5WlJlgn8BO8BpQyJ63NO1WWgH2Kfhemi2WjMwnT3_bXTEHrektmCo1pB-tNAljWDcw8uGZpE0GBeIVpM1JjKf0boIBI-9JuGRiNw8q1ShZtnGpCEh4Ja4JDmDO02RJy32X9pKJCb1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عبدالمالک الحوثی، رهبر حوثی‌ها (أنصارالله): عربستان سعودی همدست ایالات متحده، اسرائیل و بریتانیا است و مطابق با اهداف اسرائیل در منطقه فعالیت می‌کند.
🔴
بریتانیا و عربستان سعودی پیش از این تلاش‌هایی برای اشغال یمن انجام دادند، اما به دلیل مقاومت مردم عزیز ما در برابر توطئه‌هایشان، شکست خوردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/138703" target="_blank">📅 18:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138702">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436447c59d.mp4?token=Hku_G4Q9ceBooBSzT8oo0cWrNUx0AMsnqOMWHWQGspRf4DD_xLJ3XL39Iibyd6jXAV9zhMf5sziWUy2hjBZMFfybOoIMNpQR_G9FDkffD1oyXVzfyHvpjEsFUicTBarnSvWwynTbj11HqY2J9NTKFp-ie2fKjpnAWvSPYibFlPN2UWXYDPepcboBBYGMd7z_tJEx8Oir6QIiddQBFOnp9gCGYO6efyk60HWo7NGpNw_ikpnppbeeJ1nYaOSLi1Yh91YQsMbFbRAYjIrRoPCXq9iHjcMLGxm4PBlWE7MPJLPyED_ROEaWTHex9s8pB7beKAnykiqH_CNbsMPB1I9c9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436447c59d.mp4?token=Hku_G4Q9ceBooBSzT8oo0cWrNUx0AMsnqOMWHWQGspRf4DD_xLJ3XL39Iibyd6jXAV9zhMf5sziWUy2hjBZMFfybOoIMNpQR_G9FDkffD1oyXVzfyHvpjEsFUicTBarnSvWwynTbj11HqY2J9NTKFp-ie2fKjpnAWvSPYibFlPN2UWXYDPepcboBBYGMd7z_tJEx8Oir6QIiddQBFOnp9gCGYO6efyk60HWo7NGpNw_ikpnppbeeJ1nYaOSLi1Yh91YQsMbFbRAYjIrRoPCXq9iHjcMLGxm4PBlWE7MPJLPyED_ROEaWTHex9s8pB7beKAnykiqH_CNbsMPB1I9c9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که ایران شب گذشته موفق به هدف قرار دادن پایگاه هوایی "علی‌السالم" متعلق به آمریکا در کویت شده است. هنوز مشخص نیست که چه نوع تاسیساتی در آنجا وجود داشته‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/138702" target="_blank">📅 17:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138701">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df21da311b.mp4?token=p6O5eVHfaF1xF907cTd1CVc7dhdp5MulDOcWoncozUle3Y13PF0zkN3D82l0hegwF8LycK4QnE7gj5uV82X-Ic4RU9LqzglTiIJGnBEYBWteeLwjWykV4KJx9ODzwmqIDcA9_3Y0RWUZrzJw2LhculEV8gbazAFUP17_pNmBq_o3-eFn5Q-XWcTy6dpDiOj78M0KsWJ72Gir5tsXUGJCsxm6MFf1WCWPBWeU6IwXeZijyTCuwdUYLzZfxOmtyYtzjw_ZaxpnRUTiEgV2Ur5UkcxqFJllI3rsvP9pLrcInjGDr-XIODtHgWslco2BGAwtAoIv5KQWFY_cWm_BsBbEMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df21da311b.mp4?token=p6O5eVHfaF1xF907cTd1CVc7dhdp5MulDOcWoncozUle3Y13PF0zkN3D82l0hegwF8LycK4QnE7gj5uV82X-Ic4RU9LqzglTiIJGnBEYBWteeLwjWykV4KJx9ODzwmqIDcA9_3Y0RWUZrzJw2LhculEV8gbazAFUP17_pNmBq_o3-eFn5Q-XWcTy6dpDiOj78M0KsWJ72Gir5tsXUGJCsxm6MFf1WCWPBWeU6IwXeZijyTCuwdUYLzZfxOmtyYtzjw_ZaxpnRUTiEgV2Ur5UkcxqFJllI3rsvP9pLrcInjGDr-XIODtHgWslco2BGAwtAoIv5KQWFY_cWm_BsBbEMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گفته پزشک های اورولوژیست؛
این‌ روزا بیشترین مراجعینشون مردهایی هستن که میخوان به آلـت تناسلیشون فیلر تزریق کنن تا قطر و اندازشو بیشتر کنن.
این تزریق معمولا بین ۳۰ تا ۵۰ میلیون هزینه داره و ماندگاریشم فقط ۱ ساله.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/138701" target="_blank">📅 17:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138700">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqEV0sdvqmtMpKgJxV7qZs8seClmSHMvOm3BqFkk84z80Fgxcmhlz7aHWAOLGm8BLd7WLURgxm3fQyztj2zoBfgu0Gyu93v2l9uRATpU0-g0nO45pbDBhrEttvij0Gm7Zavqa6fnfWQrnJqZHP0Bw_mJgNA51ilgnQNwt3r5bI5mUvjbAzEjNYfTUYPl45K-AUOHn8zviA8KOhu-dTmnwmakBeiG2pNC_QFtTw690K3cZ_LwH33sANliwXmt-1fEf_ElGX6vHN9bfIh0bGuAyg4F7mVdUk4x-XAjGgeJptIHiGf69Lccc_MuyLG8xjOS7wxE-9KVE_nbrDsM1qUFhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان از تشکیل یک «ائتلاف دریایی» برای تأمین امنیت دریانوردی در تنگه باب‌المندب خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/138700" target="_blank">📅 17:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138699">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fdadc251.mp4?token=YWhb-ToaOfcDLEpWysKlMjsDy4VZCSdZ9pTJ0jyY0VHXVFS0SORzZAAg7jXrjfzM9m4aRXkQhq7Xmc8nteJodSwvmw8KSgk4o8GZoAso6Xyp8Q4kJfQvNiIFFh42iA5cIOccE-iMdN0TqP8gdfLYNQPA0p2n5FLg2rTowXvZpcLmQ4KkRH67nVzXJn3xW_G7oP8qNZ7JaON0b4KZAILBBThP4Wv9kwcWPb4GOvpXTgGpI70xTiuIhXVCoqed689r33bWnn7QjruJSh2QBL7QIVEgLJa51ZC6KcxamY5tuajol7KIiY4X3tFzDD8WM6kde7zHabzEweuSdvp-n4K-hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fdadc251.mp4?token=YWhb-ToaOfcDLEpWysKlMjsDy4VZCSdZ9pTJ0jyY0VHXVFS0SORzZAAg7jXrjfzM9m4aRXkQhq7Xmc8nteJodSwvmw8KSgk4o8GZoAso6Xyp8Q4kJfQvNiIFFh42iA5cIOccE-iMdN0TqP8gdfLYNQPA0p2n5FLg2rTowXvZpcLmQ4KkRH67nVzXJn3xW_G7oP8qNZ7JaON0b4KZAILBBThP4Wv9kwcWPb4GOvpXTgGpI70xTiuIhXVCoqed689r33bWnn7QjruJSh2QBL7QIVEgLJa51ZC6KcxamY5tuajol7KIiY4X3tFzDD8WM6kde7zHabzEweuSdvp-n4K-hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک روحانی یزدی: جوانان مردم رو اعدام‌ نکنید اونا آینده سازهای کشور هستن، ظلم‌نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/138699" target="_blank">📅 17:16 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
