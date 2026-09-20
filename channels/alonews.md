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
<img src="https://cdn4.telesco.pe/file/ZPSi90vRTDu91IdczzyjE9fw1FWiyCs2jDhaycyQK1U3sOidwlYF83dvDkwBfMmKM_SR7h-ydBliikj3CZvytwqdnHuT6u91Ogrlvt108zv0-jMkpPA6jyK-sNdHQ7LX7xroOg7r5dL7URCrmVKcvpSJzpa5jzzxYhmJidIqIVTRfe0huENWHehycAXVtemd9-G8RQHl4ff2C_uBEIjvqCqom8EJfMpuQ0MToUeyK1qQ2EW_H2KhGjkLAk_teovl5acPVX0d3nHEcRuNNbsG5CMunicQ1RkIWqQwCOlUxBRD7qYhJCOmAM79aiwTf7pUB7JMwcclVxps4Ht8wzEQrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 986K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 17:47:22</div>
<hr>

<div class="tg-post" id="msg-148396">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
رئیس سازمان سیا، اطلاعات مرکزی آمریکا به صورت ناگهانی وارد خاورمیانه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/alonews/148396" target="_blank">📅 17:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148395">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7129a2730c.mp4?token=JCZH1tA2GwKvvqzy46-xfzpFwczqUHFthzmHqy_SDvmd9yrEOJAICCrifjgjsRTxVuSCz6S8Yaz3wyekzaE2MubNz-CMW_sWontigDGIBXPCXLlULhNwc-uQH-Q5b_sTbbTagcMLQJtIBXNythhU6wrl2X0LNBrXr5fqaFjkTbapnGwFdKK62kfO1l-T5ZpWKx2WxEJ525YQwjlXVi13wTP5Qn8fpm5wNtFgaIgWL8yyvQcro_XMZuvvczhjl53uI-M0xIYWkxAtPDNftI3ki3sZDBaTzjo4dsGmylq-yZYxjwcu6Cyt9Lw1r-aOfJDRGKrk3iGPkCQPTZwLc9bSCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7129a2730c.mp4?token=JCZH1tA2GwKvvqzy46-xfzpFwczqUHFthzmHqy_SDvmd9yrEOJAICCrifjgjsRTxVuSCz6S8Yaz3wyekzaE2MubNz-CMW_sWontigDGIBXPCXLlULhNwc-uQH-Q5b_sTbbTagcMLQJtIBXNythhU6wrl2X0LNBrXr5fqaFjkTbapnGwFdKK62kfO1l-T5ZpWKx2WxEJ525YQwjlXVi13wTP5Qn8fpm5wNtFgaIgWL8yyvQcro_XMZuvvczhjl53uI-M0xIYWkxAtPDNftI3ki3sZDBaTzjo4dsGmylq-yZYxjwcu6Cyt9Lw1r-aOfJDRGKrk3iGPkCQPTZwLc9bSCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز:
برخی از مقامات ایرانی مانند موش‌ها پنهان شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/148395" target="_blank">📅 17:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148394">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7979df2c0d.mp4?token=LFZI5FbFyMnS1Ekz4mWbDYvBs4-_Bnh5G7xWk7PgIIPeqIgl3vIQ0L3J6c2OBFKP73_D1as562hyqatFdMEWuPIvR4YOc1X0KiZ0X88H0FfnZnuZ2WXv9dY6c4Nig7kk2futYrN8WD6tIl3M3feeX83Q1Dwn_s8MWbbxEFXWueI3Rr8tFGywW_352Tc89KoimAW__nfvX3J9yN8QioBVMEliIPRR83u4QSrKHYVT4aROdfxKyDF29C_ot5GnCHl-rXX3xVwNBvuqAlHtvcuE7sLMMzCvkR_KiXEGL-QAi_QZZjdi5M393oiZO3qKDLD9k2ICSuRP0gLSbRvMC95A3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7979df2c0d.mp4?token=LFZI5FbFyMnS1Ekz4mWbDYvBs4-_Bnh5G7xWk7PgIIPeqIgl3vIQ0L3J6c2OBFKP73_D1as562hyqatFdMEWuPIvR4YOc1X0KiZ0X88H0FfnZnuZ2WXv9dY6c4Nig7kk2futYrN8WD6tIl3M3feeX83Q1Dwn_s8MWbbxEFXWueI3Rr8tFGywW_352Tc89KoimAW__nfvX3J9yN8QioBVMEliIPRR83u4QSrKHYVT4aROdfxKyDF29C_ot5GnCHl-rXX3xVwNBvuqAlHtvcuE7sLMMzCvkR_KiXEGL-QAi_QZZjdi5M393oiZO3qKDLD9k2ICSuRP0gLSbRvMC95A3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز:آمریکا در ارتباط دائمی با حوثی‌هاست، و آن‌ها توافق کرده‌اند که با آمریکا نجنگند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/148394" target="_blank">📅 17:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148393">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: برخی از مقامات ایرانی پنهان شده‌اند و یافتن افرادی که قادر به انجام معامله باشند غیرممکن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/148393" target="_blank">📅 17:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148392">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: گزینه‌های فعلی روی میز، محو کردن ایران، رها کردن آن به پوسیدگی اقتصادی یا رسیدن به توافق است.‌‌
🔴
سوال من این است که کی و آیا قرار است تمام ایران را منفجر کنم و آنها بهتر رفتار کنند.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/148392" target="_blank">📅 17:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148391">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏
🔴
فوری/ترامپ:  ممکن است به‌زودی اتفاق بزرگی در مورد ایران رخ دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/148391" target="_blank">📅 17:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148390">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏
🔴
فوری/ترامپ:
ممکن است به‌زودی اتفاق بزرگی در مورد ایران رخ دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/148390" target="_blank">📅 17:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148389">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1502a1e1.mp4?token=oHsxIYa-a2E9iGSaOhddAQOUw-jhaNywkted5lmVuxGdlbIjwiDNUuHAcTUEaMy3CZxuY5k2CDw8UUd54-nR2cHgs0dEvz0Cd1S0M3Rb-J9KWxkvTC8-dYrfLAJXHQCulwNEJ9C4gLvKj-RbicEwcpw5-kBtvXDF3h57AVnOLnNJzCW2pRQCHjxMfT6d6qqnQw9yx8fFOfqw9mm1ReD0V8p_60yFMK7YmYIH90MGcybe8ziJzQ1OvAWas_PM34DQtr8TnktPt10WYqclehnJSX27v3FzisCE-_zUozHCGcltAVgXA4KhI9IwEqFXFTF4uzkXZTh6Y_mFHouzVrB-3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1502a1e1.mp4?token=oHsxIYa-a2E9iGSaOhddAQOUw-jhaNywkted5lmVuxGdlbIjwiDNUuHAcTUEaMy3CZxuY5k2CDw8UUd54-nR2cHgs0dEvz0Cd1S0M3Rb-J9KWxkvTC8-dYrfLAJXHQCulwNEJ9C4gLvKj-RbicEwcpw5-kBtvXDF3h57AVnOLnNJzCW2pRQCHjxMfT6d6qqnQw9yx8fFOfqw9mm1ReD0V8p_60yFMK7YmYIH90MGcybe8ziJzQ1OvAWas_PM34DQtr8TnktPt10WYqclehnJSX27v3FzisCE-_zUozHCGcltAVgXA4KhI9IwEqFXFTF4uzkXZTh6Y_mFHouzVrB-3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تداوم حملات عربستان به استان‌های یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/148389" target="_blank">📅 17:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148388">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
پزشکیان: صلحی که دشمن تو را به آن دعوت می‌کند، نباید دفع کرد
🔴
نمی‌توانیم قانونی بنویسیم که ضمانت اجرایی ندارد؛ گاهی به نام دین بر روی مسائلی متمرکز می‌شویم که اصل نیستند
🔴
ایجاد توقع در بین جامعه بدون در نظر گرفتن ردیف بودجه معین و پشتوانه مالی، نادرست است
🔴
از بیان حرف‌هایی که حتی فرع هم نیستند، دور شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/148388" target="_blank">📅 16:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148387">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
خدمت اجباری سربازی در آلمان مجددا از سر گرفته می‌شود
🔴
وزارت دفاع فدرال آلمان در برلین: نیروهای مسلح فراخواندن مردان ۱۸ ساله برای خدمت سربازی را که علاقه خود به خدمت را ابراز نکرده‌اند، آغاز کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/148387" target="_blank">📅 16:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148386">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t51QJlrCKsXNmUXnG2uW6jMTrPbHEFqhmWfZjVAAqcjfuHCCZ5vcdy4FyVrefVtCl4Zztz6QZWsnzkG6g6HcsTJg-A-L7f-6e1zN-oLdUQVn0aPYceMRMQMAj4FvQb6Ylb0UencDz6P0Kv5nm069Vs6Wb00S56dyQ7w4pktermER0_JAAUbTJokNJ6cBtYslXWb_IXSXVkmjJasgW24p7rNGsf5-feiQyi5pW7yCyNafEc6F8QuuofoXHf5G8RiBmUz3A30bW4Pg3gOwdap7RDmv9y4rHiHHZdhn0E9Svss2ReiXp7ZLgDIFZ94dzSGGx_Pg1VIhNb68zzl4egt7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تاکنون، بیشتر هواپیماهای تانکر سوخت از قطر تخلیه نشده‌اند و بعید است که ایالات متحده قبل از تخلیه این پایگاه، حمله‌ای را آغاز کند، زیرا تقریباً 20 درصد از هواپیماهای تانکر سوخت ایالات متحده در این پایگاه مستقر هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/148386" target="_blank">📅 16:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148385">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1d9cbe58.mp4?token=i7JUNN2brRQkO6wGJuf8xdxQQ9btRt8Pu2BTnjEPtSMhDAlKAnNKLhNtOvx2elxATVtpEhuzhxCFMQzQnQ4vwv6YItAffwzcecW_2DtBdGGWcgYDIdv0vkMQaX-in4VwebgyEGC-kbY2M9zcxY-x_cHyZYFnKwcgHqF9NhxA1DIpxOwiby86eJTOmxJ3PkvvMkiW7ebTITaqjpV8n80mjAGO3QLy53tjMO_rX5VkLf2YNsBBlwW2pd2IVrZFzsgnlu2JpCOkvTjOSDzmcEbWs2JxUe0JU7ANaB4R3P3xwT1uDgYjgG_JwaR5a80KGI-zho0zSU4gUHKNucX-n4A7tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1d9cbe58.mp4?token=i7JUNN2brRQkO6wGJuf8xdxQQ9btRt8Pu2BTnjEPtSMhDAlKAnNKLhNtOvx2elxATVtpEhuzhxCFMQzQnQ4vwv6YItAffwzcecW_2DtBdGGWcgYDIdv0vkMQaX-in4VwebgyEGC-kbY2M9zcxY-x_cHyZYFnKwcgHqF9NhxA1DIpxOwiby86eJTOmxJ3PkvvMkiW7ebTITaqjpV8n80mjAGO3QLy53tjMO_rX5VkLf2YNsBBlwW2pd2IVrZFzsgnlu2JpCOkvTjOSDzmcEbWs2JxUe0JU7ANaB4R3P3xwT1uDgYjgG_JwaR5a80KGI-zho0zSU4gUHKNucX-n4A7tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان به فالوور گفت تعقیب کننده
🔴
پزشکیان: حالا فالوور نگیم صداوسیما گیر نده بهمون
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/148385" target="_blank">📅 16:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148384">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
فارس: یگان‌های واکنش سریع ارتش در مرزها مستقر شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/alonews/148384" target="_blank">📅 16:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148383">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد که بر اساس اطلاعات دریافتی، ایالات متحده تصمیم گرفته است اقدامات خود علیه ایران را از سر بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/148383" target="_blank">📅 16:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148382">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ارتش اسرائیل: نیروهای ما در تمام جبهه‌ها در آماده‌باش کامل، مستقر و آماده هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/148382" target="_blank">📅 16:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148381">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر حملات توپخانه‌ای اسرائیل به مناطق یوهور الشقیف و خیام در جنوب لبنان منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/148381" target="_blank">📅 16:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148380">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
تا دو انتخابات تعیین کننده و مهم در آمریکا و اسرائیل به ترتیب ۴۴ و ۳۷ روز باقی مانده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/148380" target="_blank">📅 16:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148379">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzxfyISyh5TI4kFzicyUftTmtLSXWGA6coW7v4EnL-l1y4LXkQkAonu5TD6V5hfeBbeyykL8uuSRsU5miTUNvQDCX6GBng8HiEMsVhFmdi6pB41Hru08rohyiprB4nxzW0nJzKZOmDmWS45tTrk5glQRlCFtG-sf6GEWAPfC_Qz76n98rJe1jQp2Btwzh4JZtbNMwPBK4Y8DP4GqX45q9aG2BsDKU0ALYcEsA4zOeA9emeoUvgpmQnLla16pYAkmDHE6EQ6_0PwYcQ6NPJW20NKIK3EtGl_L0ovXMckiODCiB8vUt59PYB4r1QWRg4HUatzW74yGIveSCD4fMbuh0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💱
بات سیگنال و تحلیل خودکار
💱
اگه دنبال تحلیل و سینگال دقیق هستید حتما عضو ربات بشید
🆓
آیدی ربات:
@Sygnl_bot</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/148379" target="_blank">📅 16:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148378">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
اوکراین خطاب به پوتین: از پنجره کرملین سوختن مسکو را ببین
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/148378" target="_blank">📅 16:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148377">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ژاپن: کره شمالی دومین موشک خود را شلیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/148377" target="_blank">📅 16:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148376">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
فارین پالیسی: ترامپ و پوتین در جنگ، شباهت‌های زیادی به یکدیگر دارند
🔴
در تحلیلی در فارین پالیسی آمده است که هم دونالد ترامپ و هم ولادیمیر پوتین تصور می‌کردند جنگ‌هایشان با مقاومت جدی روبه‌رو نخواهد شد و در مدت کوتاهی به پایان می‌رسد.
🔴
نویسنده این مطلب معتقد است هر دو رهبر تا حدی تحت تأثیر روایت‌ها و تبلیغات خود قرار گرفتند و برای یک درگیری طولانی‌مدت آمادگی کافی نداشتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148376" target="_blank">📅 16:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148375">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
محسن رضایی:  اگر آمریکایی‌ها جدی هستند، بگذارند سربازانشان بیایند و وارد ایران شوند، چرا نمی‌آیند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/148375" target="_blank">📅 16:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148374">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
مرکز زبان وابسته به سفارت فرانسه در تهران با دستور قضایی پلمب شد.
🔴
قوه قضاییه اعلام کرد این مرکز بدون مجوزهای لازم فعالیت می‌کرد و پیش‌تر چند بار درباره ضرورت دریافت مجوز به مسئولان آن اخطار داده شده بود.
🔴
در گزارش قوه قضاییه، اتهاماتی مانند استفاده از آموزش زبان برای پروژه‌های علیه امنیت ملی و تسهیل خروج نخبگان از کشور نیز مطرح شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/148374" target="_blank">📅 16:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148373">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
پزشکیان: باید راهی پیدا کنیم که مردم ما به عزت و سربلندی و قدرت برسند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/148373" target="_blank">📅 15:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148372">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نتانیاهو برنامه سفر خود به آمریکا در روز های آینده را تغییر داده و بلافاصله پس از سخنرانی در مجمع عمومی سازمان ملل بدون دیدار با ترامپ به اسرائیل بازمی‌گردد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/148372" target="_blank">📅 15:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148371">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ra-M0eoynHmxgSCqVAfR3ZDtvK73FWawA3z0mSgs2W_vXGuhoZG8gjCqFcfBpiwrCW9DRft5Ihc9CzoQhFq1MeJfJIe83MF6US8ywaEpUe7KqqxfpSj5J0XiVvm0vmVuY-6jueOF_gb8kQJxQLi-7fSL92KGU59iCldcHFzsA6sGahnEpEPZuUctJumyBaAHCURcjF3F9t_cE7rKe0HPUYxT8cNJid3AmBzbynXOX1YKY7-4CC_TqczhoJOeyJn12kg23TbnOOLEVidl1WTL5wwWo4mFEqtoBozmQxPc1uR2YXrCT1aEaIxPlUDinKlJdUvegdRz4a86VavHdr2vsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : به درخواست قوی ارتش ایالات متحده و به منظور حفظ امنیت ملی، من موافقت کرده‌ام که بنای باشکوه "طاق پیروزی" را که از دوران جنگ داخلی، یعنی سال‌ها پیش، برنامه‌ریزی شده بود و در محوطه "دایره پذیرایی" مجاور پل یادبود آرلینگتون قرار دارد، به یک مجموعه نظامی/طاق پیروزی درجه یک تبدیل کنم. این مجموعه برای نگهداری، ذخیره‌سازی و استفاده سریع از تعداد زیادی پهپاد، به همراه تک‌تیراندازها، در مناطق سقف و محوطه، و همچنین ذخیره‌سازی مقادیر زیادی مهمات تک‌تیراندازی، طراحی خواهد شد.
🔴
هیچ سازمانی مانند این در هیچ جای دنیا وجود نخواهد داشت. از بین 59 شهر و پایتخت برتر جهان، واشنگتن دی‌سی، تنها شهری است که طاق پیروزی ندارد، اما اکنون این مشکل برطرف خواهد شد و این طاق، بزرگترین طاق پیروزی در جهان خواهد بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/148371" target="_blank">📅 15:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148370">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
صداوسیما: حمله به ایران قطعی است و در وضعیت آماده‌باش هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/148370" target="_blank">📅 15:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148369">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
فیلد مارشال رضایی: آمریکا و ترامپ خواهند رفت. همه می‌دانند که اقتصاد آمریکا در واقع در مسیر فروپاشی قرار دارد. در طول 10 سال آینده، آمریکا آن‌طور که امروز است، نخواهد بود.
🔴
اما ما و کشورهای عربی باقی خواهیم ماند. ما هستیم که باید این منطقه را سامان دهیم. ما باید امنیت را در خلیج فارس برقرار کنیم. ما باید یک پیمان برای همکاری اقتصادی ایجاد کنیم و در این منطقه با یکدیگر دوست باشیم.
🔴
ما یک خانواده هستیم – خانواده خلیج فارس. ما هشت کشور هستیم و باید بر بازسازی و توسعه اقتصادی تمرکز کنیم، با یکدیگر همکاری کنیم، در سرمایه‌گذاری‌های یکدیگر مشارکت کنیم و حتی یک ارز واحد و یک بازار مشترک داشته باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/alonews/148369" target="_blank">📅 15:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148368">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی، دبیر شورای عالی امنیت ملی : اکنون به تمام کشورهای عربی و تمام کشورهای همسایه می‌گویم: اگر آمریکایی‌ها تلاش کنند روابط تجاری و مالی ما را مختل کنند، ما دو کار انجام خواهیم داد.
🔴
اول اینکه، حتماً به شرکت‌های آمریکایی حمله خواهیم کرد – مانند شرکت‌های حفاری آمریکایی که به طور گسترده در اطراف ما فعالیت می‌کنند، شرکت‌های تجاری آمریکایی و کسب‌وکارهای آمریکایی.
🔴
ما آن‌ها را هدف قرار خواهیم داد و خواهیم گفت: حمله به اقتصاد آمریکا در پاسخ به حمله آمریکا به اقتصاد ایران – حمله به ازای حمله.
🔴
از طرف دیگر، ما همچنین به کشورهای همسایه هشدار می‌دهیم: با آمریکا همکاری نکنید، زیرا ما به طور متقابل پاسخ خواهیم داد. اگر یک کشور همسایه با آمریکایی‌ها در تحمیل یک محاصره اقتصادی به ایران همکاری کند – به عنوان مثال، در مسائل مالی و فعالیت‌های مرتبط با ما – ما به کشتی‌های آن کشور در تنگه هرمز تذکر خواهیم داد.
🔴
ما محدودیت‌هایی را بر تردد و عبور آن‌ها و همچنین برخی از فعالیت‌هایشان اعمال خواهیم کرد، یا ما به طور متقابل در مورد همکاری‌های اقتصادی پاسخ خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/alonews/148368" target="_blank">📅 15:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148367">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
پزشکیان: ما باید طوری کار کنیم که چرخ تولید بچرخد و از کار نیفتد
🔴
هر جایی را که می توانیم قطع کنیم ولی نگذاریم چرخ تولید قطع شود
🔴
دشمن به دنبال این است که تولید ما از کار بیفتد؛ نبود تولید یعنی بیکاری و تورم و کمبود و گرفتاری
🔴
همه کمک کنند که تولید کنیم. باید این فرهنگ در جامعه جا بیفتد که ما خودمان در سرما بمانیم ولی چرخ تولید متوقف نشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/148367" target="_blank">📅 15:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148366">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
صداوسیما: حمله به ایران قطعی است و در وضعیت آماده‌باش هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148366" target="_blank">📅 15:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148365">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
پیشنهاد ایران به آمریکا به نقل از ارم‌نیوز امارات:
🔴
توقف غنی‌سازی بالای ۵ درصد
🔴
آزادسازی بخشی از دارایی‌های بلوکه‌شده
🔴
بازگشایی کامل تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148365" target="_blank">📅 15:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148364">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5da053393a.mp4?token=GYycMQryVydDrhYZw7vsbPjKVcO4i2_-wfamoFH3L4J72Bk8dqbP22FrOOzlUbgFy3npZAoJZw4gG2vWE2BOUf9xxj5XV9kzZtBPKTLOx1ju-IF_fqvJ0j7YiUtq-jVZMOkru7eeCtEsQphsPphxPDfScfhcVmVSEdEOmx01YfYT9QX-m-ZF7W0pL0QP0QJGmz5KvItGU1jw83DyMk1wuZxoANkghuvtyi_PHBXyKyFhapoYY6dcgUIw8tWuvf6UG_ejWOS-nEW7YpGWO8JqnRnDLYvRitPer78RFE4Qt_MNJlLiHHNLDtO-wnD3oFjnZpDsFnU5y4E0mdEUWmVGRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5da053393a.mp4?token=GYycMQryVydDrhYZw7vsbPjKVcO4i2_-wfamoFH3L4J72Bk8dqbP22FrOOzlUbgFy3npZAoJZw4gG2vWE2BOUf9xxj5XV9kzZtBPKTLOx1ju-IF_fqvJ0j7YiUtq-jVZMOkru7eeCtEsQphsPphxPDfScfhcVmVSEdEOmx01YfYT9QX-m-ZF7W0pL0QP0QJGmz5KvItGU1jw83DyMk1wuZxoANkghuvtyi_PHBXyKyFhapoYY6dcgUIw8tWuvf6UG_ejWOS-nEW7YpGWO8JqnRnDLYvRitPer78RFE4Qt_MNJlLiHHNLDtO-wnD3oFjnZpDsFnU5y4E0mdEUWmVGRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148364" target="_blank">📅 15:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148363">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
تسنیم: در روزهای آینده پزشکیان قراره توی مجمع عمومی سازمان ملل در نیویورک حضور پیدا کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148363" target="_blank">📅 14:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148362">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
رئیس سازمان سیا، اطلاعات مرکزی آمریکا به صورت ناگهانی وارد خاورمیانه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148362" target="_blank">📅 14:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148361">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
فایننشال تایمز: عربستان از برنامه تحت رهبری چین که بخشی از تلاش‌های پکن برای ایجاد یک نظام پرداخت فرامرزی جایگزین دلار است، خارج شد
🔴
ادعای یک منبع آگاه: خروج ریاض از این برنامه به علت فشار واشنگتن، نادرست است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148361" target="_blank">📅 14:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148360">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d8158ff0.mp4?token=TsjK6fl-DM--pOIXux1eBXUCXgsUncXqMppVANG0t1cM1HOtA7u5Ugq_-ZOzRKHMs5Rszvf0UGHnWJjgfRbVR2lFPAERZCkplTqRznmgmXvuWOOSWt5BcOQ-CneuNZvuEQniNpmfdS6EZS99HC-bu8L32755B6fXT1R54hpv6Wc-A7gwUN3XctkDD28hgyyUDcSmzHR8cm0t39ST6u8tfYGo00umuURalpHPU5SydpMDciTMjxHwKzcViOp5Hi1ZYKOJyrhS8LutPK6iBEmxNHCi0sFu3B1iKXMRqTv5kH9LCu2dpp3g3P9MauF4GB7dvGdUPG7Ku-D0iGxgt3dBaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d8158ff0.mp4?token=TsjK6fl-DM--pOIXux1eBXUCXgsUncXqMppVANG0t1cM1HOtA7u5Ugq_-ZOzRKHMs5Rszvf0UGHnWJjgfRbVR2lFPAERZCkplTqRznmgmXvuWOOSWt5BcOQ-CneuNZvuEQniNpmfdS6EZS99HC-bu8L32755B6fXT1R54hpv6Wc-A7gwUN3XctkDD28hgyyUDcSmzHR8cm0t39ST6u8tfYGo00umuURalpHPU5SydpMDciTMjxHwKzcViOp5Hi1ZYKOJyrhS8LutPK6iBEmxNHCi0sFu3B1iKXMRqTv5kH9LCu2dpp3g3P9MauF4GB7dvGdUPG7Ku-D0iGxgt3dBaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چین ۹ ماهواره به فضا پرتاب کرد
🔴
طبق گزارش رسانه‌های دولتی چین، این کشور ۹ ماهواره را با موفقیت با استفاده از موشک حامل «لیجیان-۱» به فضا پرتاب کرد.
🔴
به گزارش خبرگزاری دولتی شینهوا، این ماهواره‌ها عمدتاً برای پایش محیط فضایی، پیشگیری و کاهش خسارات ناشی از بلایای طبیعی و انجام آزمایش‌های علمی مورد استفاده قرار خواهند گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148360" target="_blank">📅 14:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148359">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2zdX2O8glrKCdH7qRo9QmNJMWyIKy7OcgfRrqmSCJmHBJTPqUKtt4fIgmRdbEW8SeIWIqWvrJluTyceKhlBAduVoW8QEnQqFMdxK4osq3dxnSMt3USUgvyHjBC7DAnl5baGokzCi6saKzj4hov9N3pTkUmITozibRX32iFWAF-9c9uSDYtT1O33nZWt0ZBKJytoIdUK2D3bTmdpqp2nUb917CsMNg4hPw9XvZVbrcvJVhyqjD7EMRQtLM_J6-D2jBnZIfwZzyUeF6kfYimUVT2pytSHGyXp4LFfaX969ZJZkKoxwS54afuXuH3ZM9pPvjnbnS2AiW_LhL70u_BhGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فکر کنم اگه روسیه بمب اتم داشت، اوکراین جرات نمی‌کرد اینطوری به پالایشگاه‌هاش حمله کنه...!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148359" target="_blank">📅 14:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148358">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سفارت آمریکا در امارات: با توجه به تنش‌ها در خاورمیانه، وضعیت امنیتی همچنان پیچیده است و احتمال تشدید غیرمنتظره تنش‌ها وجود دارد.
🔴
شهروندان آمریکایی که در حال حاضر در خاورمیانه حضور دارند، باید هوشیاری بیشتری به خرج دهند و نسبت به احتمال لغو پروازها، بسته‌شدن حریم‌های هوایی و اختلال در سفرها آگاه باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148358" target="_blank">📅 14:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148357">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سپاه : به ایالات متحده هشدار می‌دهیم که اگر هرگونه اشتباهی علیه ایران مرتکب شود، تمام مراکز و منافع آن در منطقه مورد حملات مداوم، موثر و دردناک قرار خواهد گرفت.
🔴
همچنین هشدار می‌دهیم که اگر کشورهای منطقه با ادامه سیاست‌های دوگانه خود در تهاجم به ایران، با این اقدام همسو شوند، ما آن‌ها را شریک در این عمل خصمانه تلقی خواهیم کرد و دیگر نمی‌توانند انتظار خویشتن‌داری یا مدارا از نیروهای ما را داشته باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148357" target="_blank">📅 14:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148356">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
حدادعادل: بنیاد زبان و ادبیات ترکی در تبریز تأسیس می‌شود؛ تقویت و حمایت از زبان و ادبیات ترکی ضروری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148356" target="_blank">📅 14:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148355">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
دولت کویت مدارس ایرانی فعال در این کشور را تعطیل کرد
🔴
رئیس مرکز امور بین‌الملل و مدارس خارج از کشور وزارت آموزش و پرورش:
دولت کویت در اقدامی غیرقانونی، مدارس ایرانی فعال در این کشور را تعطیل کرده و مانع ادامه فعالیت‌های آموزشی این مدارس شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148355" target="_blank">📅 13:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148354">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
رویترز: سهام عربستان سعودی و کشورهای حوزه خلیج فارس در آغاز معاملات پس از حملات اخیر به ریاض، پایتخت عربستان سعودی، کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148354" target="_blank">📅 13:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148353">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a87d1892.mp4?token=J37FSYtRWcqO_P-dZdYBYSTR0dFuKXJ3huiRgVw0l18My_i_3sI_JofGwBMF043fpDRigRP6LV65BYWz5iRGoXMJIyvYD-JTbd2aXtBZ1uPYMPnpA43gXx75b-1yg1RTFC35Bo2o-YFmKlXOBp0gXQbPm2mRGwcUfXZ0bHQPCAYGH_4FA4ErKCN4Qa94ET4cUzW7QaG28ZG4ad60v9q_biWmpXX2uXF0sdc1JN-GzAwPkgzLlAhtOFqWFkwn9R7CbzvocCbNOTl3K7fLBkcNY2f7RFWiQGQHH9XA88Flyj3FU3uwhi2JXRYebIM-NU3wRYM0YKM82-XfIxsY7d1DPbjfQtvJCWnzpbJW3oawVCfvpowuwJ2geUW3a5tF5ml0nOj6bATnVr7nWWs_DQExm8fOxbm8t5jHohRKQekuIhOWq6m1igTepaLkl5g8Z9ymwJCspYnXDBJYHLGUbA0NJBlkg3pxnvn9kycF1_Uv4ePIzjw7DulDuZOsRwYymj8Chs7ismJWaYUSWzQSpg0Sz3DePD22kn3gV_WsNT3DX421CwE0hmcEnrQujW1290B6PiG4ywIHBcp7Dw0nCGYVd3B3RBGFoveUCtjq97A0tC1BLlDHYKnlasqrVkg7ZA4oOCsXwpZGG4hQYhBAbYZI4E7DVh_yx3IaSA1FZwnZMVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a87d1892.mp4?token=J37FSYtRWcqO_P-dZdYBYSTR0dFuKXJ3huiRgVw0l18My_i_3sI_JofGwBMF043fpDRigRP6LV65BYWz5iRGoXMJIyvYD-JTbd2aXtBZ1uPYMPnpA43gXx75b-1yg1RTFC35Bo2o-YFmKlXOBp0gXQbPm2mRGwcUfXZ0bHQPCAYGH_4FA4ErKCN4Qa94ET4cUzW7QaG28ZG4ad60v9q_biWmpXX2uXF0sdc1JN-GzAwPkgzLlAhtOFqWFkwn9R7CbzvocCbNOTl3K7fLBkcNY2f7RFWiQGQHH9XA88Flyj3FU3uwhi2JXRYebIM-NU3wRYM0YKM82-XfIxsY7d1DPbjfQtvJCWnzpbJW3oawVCfvpowuwJ2geUW3a5tF5ml0nOj6bATnVr7nWWs_DQExm8fOxbm8t5jHohRKQekuIhOWq6m1igTepaLkl5g8Z9ymwJCspYnXDBJYHLGUbA0NJBlkg3pxnvn9kycF1_Uv4ePIzjw7DulDuZOsRwYymj8Chs7ismJWaYUSWzQSpg0Sz3DePD22kn3gV_WsNT3DX421CwE0hmcEnrQujW1290B6PiG4ywIHBcp7Dw0nCGYVd3B3RBGFoveUCtjq97A0tC1BLlDHYKnlasqrVkg7ZA4oOCsXwpZGG4hQYhBAbYZI4E7DVh_yx3IaSA1FZwnZMVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از لحظه وقوع تیراندازی در شهرک اسرائیلی نِوه تسوف (Neve Tzuf) در نزدیکی شهر البیره در کرانه باختری منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148353" target="_blank">📅 13:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148352">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cExOGfQhBj-mNfylYL7rOKZ2ibCqBZ08mh7n2Va3scXcFct5cv3XivlOPVBmjd1sEGTnG6oPq5phvjMgu2NK2fZ8470tPHAgy7lUO_SOZAcCbQZzis1NR-e1nUPW6IgdVQlwesmfeqK_jgjXgC15czdIyQn422vPMZ5sRAsLDPc3ZCzz4wpDw2lrYMEUjUwz4294V6cXAWlnDlhW07yzFUK1D7JcYKDhuiu5z8rCicbBETulpRmejbvQCTKRLb9EAuAZMYAdH05eWknIYTaeHUrTcmC8tDNaFEpv91UfpKiIdSv-bF3TSEjfiWuUH1lYca8BLT9GprL6xKU61awV3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه فاکس نیوز با انتشار تصاویر ماهواره‌ای از تأسیسات هسته‌ای طالقان مدعی است فعالیت قابل‌توجهی در این محل دیده شده و یک سازه بتنی روی آن ساخته شده است
🔴
آنگونه که در تصاویر ماهواره ای مشخص شده است؛ ایران برزنتی را بر فراز تأسیسات تخریب‌شده و مستحکم‌شده‌ی مدفون نصب کرده است که فعالیت‌های بازسازی در زیر آن را از دید ماهواره‌ای یا شناسایی هوایی پنهان می‌کند.
🔴
فعالیت قابل توجهی در سراسر محل ساخت‌وساز قابل مشاهده است.
🔴
وسایل نقلیه ساختمانی، از جمله کامیون‌های کمپرسی، بولدوزرها، کامیون‌های پمپ بتن و میکسرهای بتن و جرثقیل‌ها، به طور فعال برای بازسازی این تأسیسات در حال کار هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148352" target="_blank">📅 13:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148351">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
حاجی‌دلیگانی: طرح سه فوریتی خروج از NPT تقدیم هیات رئیسه مجلس شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148351" target="_blank">📅 13:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148350">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری / ایلان ماسک مجوز اتصال مستقیم گوشی به اینترنت ماهواره‌ای رو گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/148350" target="_blank">📅 13:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148349">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=Au41B8w9cDVsrQysuwJSwvwZV9qrYTe6hL7rZZIhGdx6uWTPJ60U5yRZ6kiRwOv5P-lbeRII0CVRHxwqS32OqRg6jJCrZvlHgLxTukENoFQxoqQKwqk8ApQd43O6euEIVx553bagxY-S8GqWQ3OC1_VzT8Q_RObA6KUVlcky8vRx1sv2XiG2F6UFNDf5WNhAQ7JZvhzSqAPh6rSEJVbIDGh_bubRIugNiR7yS0XmGcJx6MACxKnvnDfzyc9M_1VlL8ZBsCtg-86E3-D9jEHpkIq_3BI15kCiUEF4yENNvQ91OC2uYQTCWuOS1sobMjGfGa2Sgk8Pb0NPMeJKDNzPKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=Au41B8w9cDVsrQysuwJSwvwZV9qrYTe6hL7rZZIhGdx6uWTPJ60U5yRZ6kiRwOv5P-lbeRII0CVRHxwqS32OqRg6jJCrZvlHgLxTukENoFQxoqQKwqk8ApQd43O6euEIVx553bagxY-S8GqWQ3OC1_VzT8Q_RObA6KUVlcky8vRx1sv2XiG2F6UFNDf5WNhAQ7JZvhzSqAPh6rSEJVbIDGh_bubRIugNiR7yS0XmGcJx6MACxKnvnDfzyc9M_1VlL8ZBsCtg-86E3-D9jEHpkIq_3BI15kCiUEF4yENNvQ91OC2uYQTCWuOS1sobMjGfGa2Sgk8Pb0NPMeJKDNzPKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توی برلین آلمان، یک دختر تریان(آدمایی که فکر میکنن حیوونن) به یک خانم تو خیابون حمله میکنه و گازش می‌گیره، زنگ زدن پلیس، هر چقدر از دختره اسم و فامیل پرسیدن فقط پارس کرد، پلیسا هم بردنش به ی مرکز نگهداری از حیوانات
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/148349" target="_blank">📅 13:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148348">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
گاردین به نقل از وزیران بریتانیایی گزارش می‌دهد:بودجه ماه آینده در بریتانیا به دلیل جنگ ایران ، دشوارتر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148348" target="_blank">📅 13:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148347">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
فارن پالیسی: روسیه مایل است ایران در شرایط جنگی‌ بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148347" target="_blank">📅 12:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148346">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
قالیباف: جنگ بعدی ناوهای آمریکایی را در هر نقطه اقیانوس هند باشند هدف قرار می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/148346" target="_blank">📅 12:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148345">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
زیدآبادی در کانال تلگرام خود نوشت:
احتمال ورود نیروهای زمینی برخی کشورهای منطقه به خاک یمن به قصد تصرف پایگاه‌های حوثی‌ها هم دور از انتظار نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148345" target="_blank">📅 12:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148344">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
شرکت برق البرز: در یک مزرعهٔ استخراج رمزارز که در پوشش صنعت فعالیت می‌کرد، ۳۶۲ ماینر کشف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/148344" target="_blank">📅 12:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148343">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
واشنگتن‌تایمز نوشت: ترامپ قرار است چهارشنبه، شخصا در فرودگاه پایگاه مشترک اندروز از شی جین‌پینگ، رئیس‌جمهور چین، استقبال کند.
🔴
این کار غیرمعمول است، چون ترامپ معمولاً از رهبران خارجی در کاخ سفید استقبال می‌کند نه فرودگاه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148343" target="_blank">📅 12:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148342">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
با تصویب مجلس، وزارت کشور مکلف به راه‌اندازی «سامانه نظارت بر ارتباطات خارجی» شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148342" target="_blank">📅 12:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148341">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
پیمان اکبری، مجری انقلابی: کلیپی که از من بیرون اومده و کنار دوتا دختر خوابیدم هوش مصنوعی هست و میخوان خرابم کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148341" target="_blank">📅 12:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148340">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v291EQp8hiDgQsqLCEXRyAXzGkcPKXToJyUMd7MKetFyw-6hj8trJk-cP24lBCmnYeohTp31dUxmye2BV0Q5oCbDllhWBTLNPYBjviS-KHANZyvOlRjboC8suzUyG39ki-NOpFHVzvXKsdrsWgWY1UjzrLbbhNLX1y2pWaVJ-ctZRBgUUp0PWRERz2mSMVsQJBoCFaPOySpmzKVYPO6Sm3atvTeGzETSv_LMGZMplGeeHuOaOlfOozlf9uMs_G69kX01tvVvlqdO7EEhWA6h1jmwoy4ukdkXOyWxe3h0C3blDwrGzmz3uQMdQegcWNe6jsgvxgBtMjRuyIR4qtUkeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیمان اکبری، مجری انقلابی: کلیپی که از من بیرون اومده و کنار دوتا دختر خوابیدم هوش مصنوعی هست و میخوان خرابم کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148340" target="_blank">📅 12:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148339">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
روزنامه کوریره دلا سرا: ایتالیا آماده اعزام ۴ کشتی جنگی به تنگه باب المندب است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/148339" target="_blank">📅 12:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148338">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c84f4e05.mp4?token=d-dTBoQgR6I2w__mnTogNNyCEkuxDXz7snQS6NOwBGqyv-HBkV0mCKmU8JUyqVdMbFyqFl2AZ0onzaQeFxe30wvUuDHPDO7GjuoYqP-dZOsZjvHyH55fLN6W0ZJpUXk0UI1-OVStjQDuxt9t1Xn2QxRPQy3GfCQ0caOiZ_0nYXeJuFgUvEB6mYjcnV9mETqmA9UWm0vX78krVsTHk9fyXgJh3yLaKZ7n6e0ERPMe9St31X4KboRlpVvLBatSXdngn_WZ8MPo-wb0rfZcl_HyAiaHhNpUm6Hno8kva_85nKEt_c_MwRoYF0VkLZfm0QHglnZbC6p3TiNAoCnRco_Naw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c84f4e05.mp4?token=d-dTBoQgR6I2w__mnTogNNyCEkuxDXz7snQS6NOwBGqyv-HBkV0mCKmU8JUyqVdMbFyqFl2AZ0onzaQeFxe30wvUuDHPDO7GjuoYqP-dZOsZjvHyH55fLN6W0ZJpUXk0UI1-OVStjQDuxt9t1Xn2QxRPQy3GfCQ0caOiZ_0nYXeJuFgUvEB6mYjcnV9mETqmA9UWm0vX78krVsTHk9fyXgJh3yLaKZ7n6e0ERPMe9St31X4KboRlpVvLBatSXdngn_WZ8MPo-wb0rfZcl_HyAiaHhNpUm6Hno8kva_85nKEt_c_MwRoYF0VkLZfm0QHglnZbC6p3TiNAoCnRco_Naw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: نظم کهنه‌ آمریکایی در غرب آسیا فروریخته است؛ مسیر آینده نه با التماس، بلکه با عقلانیت، شجاعت و مبارزه رقم خواهد خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/148338" target="_blank">📅 12:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148337">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
دراپ سایت : بازگشت زودتر از موعد ترامپ از کمپ دیوید، ویدیوهایی از برخاستن بمب‌افکن‌های B-1 از بریتانیا و هشدار امنیتی آمریکا به شهروندان این کشور در خاورمیانه، نگرانی‌ها درباره احتمال آغاز دور جدیدی از تشدید تنش علیه ایران را افزایش داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148337" target="_blank">📅 12:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148336">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbmMebhKS0tHj_BE7kBAMFV7EPOyc7UWSFnrkqe7r_Bg957TkXFxm7jljVldDNyAJbtRG_DPrkR0CMzdw2vyP2AibsAQxj3ys9LKw6-DZwYoaeamHMZxFPsVbg8iFr5UzALRD0KxuYy9vIoqRTD1c0pyH5oVtu_3l2xrrj4Av9c9euRbkcF1UoxsKcsUDjGR8TVCcYanSY2R8kNQxzFR6lSQ4cYZcfSAs7s4KrU6RmJgcsrWOkPw9tmqreJYwNWAcAkqV3MgifqPGfymNu1zsMsEfe7HJWZiXIwqIgczi9inTOTd-NUJYN2s2ZqXX-yDuzOt-ZJxOcO4u5XxXRo4SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیمتی: ارزونی تو راهه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148336" target="_blank">📅 11:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148335">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhcbmknLCu97SNdYaa7P9_bbboaZlbMVmEbL9jo3yLdmWk63am5cC6wB_EWvsT9xR1wHh4KU1yjwJS_-1dBYCMszUer4ULxWiZT7WfIPqhZ2mzOol_RmzhP5Wby0QD2uGXeq5VvzWWAt4nJUb0rtEXVmyeI-lj4ej1ORguMLSFeIV437DNwygQdUnBLgvFfvdZagg_ulAxqbH_Rdwdc2UvSDBqq44bXK5PXgb_HKyt-AXdNnqu2qL_7hqx_12iryZtMQ1nb2Xw__e87UxYqZ5c_utgqM8a2nCiVgVhOnES6Tw_tKIveTptOZ4-EQAefWoX1BNIqNc0Yp3GffT_aF2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در حالی که تمام نگاه ها به قیمت نفت دوخته شده کمتر کسی متوجه است که این روزها حمل نفت در یک سوپرتانکر حامل ٢ میلیون بشکه به مقصد چین بشکه ای حدودا ٢۴ دلار یعنی بیش از ٢٠ درصد خود نفت هزینه دارد. رکورد بی سابقه ای است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148335" target="_blank">📅 11:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148334">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
مدیرعامل مترو تهران: ساعت فعالیت مترو از اول مهر بدون تغییر، از ۵:۳۰ صبح آغاز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148334" target="_blank">📅 11:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148333">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ارتش اسرائیل عملیات تخریب را در مناطق مجدل زون و طیر حرفا در جنوب لبنان انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148333" target="_blank">📅 11:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148332">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
تا ماه بعد وضعیت طلا چجوریه؟</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148332" target="_blank">📅 11:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148331">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANHwb3QrFwwpfadeW4KzTaSRgvuSEtamSX02KBsJrP4toHrkVPiMPpuMHNNLp6W-jilMKk5gySHQovBh0TBv-LEq1ClY0xRwly-QPuD-HTmbqgC_3CllUncBeQLb0MTmdj_Y6ynoYMW7LPElt6gDP21qW52i-1StFw2nHOqmQwID6xf8KkHHHWjzmUGDDgcmnwnSkSyyYedhoGJ3moq92tqr365UgP4QajZQGlj6zb9l0Xy_ERipDFfCatt3cTmvi639qenA2bKfD3q5yOkTj4A0tfbHnqjESRwnaLOqRk3MOWb_O2UzU__SyOYVbmsUYgR9Pmk8t5PoIx1F1_IFaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار بزرگ امنیتی آمریکا در خاورمیانه
🔴
سفارتخانه‌های آمریکا در سراسر خاورمیانه امروز به‌طور هماهنگ هشدارهای امنیتی صادر کردند.
🔴
رویداد: با توجه به تنش‌های موجود در خاورمیانه، وضعیت امنیتی همچنان پیچیده است و احتمال تشدید غیرمنتظره تنش‌ها وجود دارد.
🔴
به شهروندان آمریکایی که در حال حاضر در خاورمیانه حضور دارند توصیه شده است سطح هوشیاری خود را افزایش دهند و نسبت به احتمال لغو پروازها، بسته شدن حریم‌های هوایی و اختلال در سفرها آگاه باشند.
🔴
ایران: سفر نکنید؛ همین حالا کشور را ترک کنید
🔴
عراق: سفر نکنید
🔴
لبنان: سفر نکنید
🔴
سوریه: سفر نکنید
🔴
یمن: سفر نکنید
🔴
غزه: سفر نکنید
🔴
عربستان سعودی: در سفر تجدیدنظر کنید
🔴
بحرین: هشدار امنیتی صادر شد
🔴
عمان: هشدار امنیتی صادر شد
🔴
قطر: هشدار امنیتی صادر شد
🔴
کویت: هشدار امنیتی صادر شد
🔴
اردن: هشدار امنیتی صادر شد
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148331" target="_blank">📅 11:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148330">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
روزنامه عبری تایمز اسرائیل : عربستان سعودی برای مقابله و دفع حملات یمنی‌ها و به دلیل کمبود موشک‌های رهگیر، خواستار حمایت بین‌المللی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148330" target="_blank">📅 11:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148329">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnZbLr1UPur_zeSoaGZXRAAMrke3-Z-ZtWm93kpBLkENvJmKUUCckllTxp_iWToAZa8iVkp7U9-POdNjbxOzKZ91JRJGAnETgo4960U2zsYMk0ghKeNEqvtMih33FLmC0jVGcjC7Y75qiduxWbUgz64eNIpNUo9hrQNEjcpDyqUs5zBqqv0acfSF84H0WNHTdeZZ8H7sYVFFE9NcctMKiAC9yrE38OqH6KwSnTilj6Rc3_nE6XY3W-x61PZ1RZd08hc3AYR7rYEXsl3hlGkoRgvwju5059d5EWD7Fe0SjtFEgT0c8pWfe1L7FWv6z29cTU-Lx-3Q77VfxehALtXJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده جمهوری‌خواه آمریکا: یمن را از ایران آزاد کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148329" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148328">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوری / کره شمالی یک موشک بالستیک شلیک کرده است.
🔴
این موشک به احتمال زیاد به سمت دریای ژاپن در حال حرکت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148328" target="_blank">📅 11:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148327">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UpYNeK_EV_rbf7a-fjc__wEWpQYZG8d8LL9C8F5wxmuVOtraPByZEz5ZKyDxGwglYdTS5qkwCHb8iHAHdoZswdOA0TLhXbOcIFXGrPjIpKaDiNKhUM1ZEeG71bnkvvsjQh8m-8-kgHEdF3AeI09MZiYcOnTeDPp5yFYRJwcWHTJOqHf3a0zgYzaANI1VTVmkJcH7zcoVuJESySnOxaM-pa7K35kq7J1C42x4ANJ-M4t_ujihIg95JNx2462evu37jaxiC7j7t0dgiQ0RAk_Sgf_MrgPf7o_e124-3JmtOIIi2GDSjjoNDYJR-_wgmJF1hW5GsfJndN0msXCbtpZjIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فایننشال تایمز: عربستان سعودی از پلتفرم mBridge برای ارز دیجیتال فرامرزی که بخشی از تلاش‌های چین برای ایجاد جایگزینی برای سامانه‌های پرداخت تحت سلطه دلار است، خارج شده است.
🔴
بانک مرکزی عربستان اعلام کرده که این کشور در مه ۲۰۲۵ مرحله آزمایشی (Proof of Concept) خود را تکمیل کرده و خروج از این پلتفرم نیز بخشی از برنامه اولیه آن بوده است.
🔴
این اقدام پس از خروج مشابه بانک تسویه‌حساب‌های بین‌المللی (BIS) در سال ۲۰۲۴ صورت می‌گیرد؛ اقدامی که در بحبوحه گزارش‌ها درباره فشار آمریکا انجام شد. همچنین دونالد ترامپ، رئیس‌جمهور آمریکا، کشورهای عضو بریکس را در صورت تلاش برای ایجاد جایگزین‌هایی برای دلار، به اعمال تعرفه ۱۰۰ درصدی تهدید کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148327" target="_blank">📅 11:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148326">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/af2be236d1.mp4?token=WxulCYRdIaNmYsAU1aJj5FWHFy_44ifZU1R9eoalgQGeYm90AdfVrCQ35_fbNwpfaLdXHehtHIDrpuibjKTh9lVe7j5gFTabLEcO-rVXgHhakxhhwVpvP3suDvL8J5F52IIMkurzoFSSvqSQN74J6nOHwaU35hoNs1mmRhNmnxvG3c0YAgyuto12xSJIDlFi-WGXgFwVCnOvS8ud5z-Elq2lx9G_DfT4fZKPzD8_mI_zl-XWc5gMG9BOe8CuBjj45J5KsgVbAqEwR_YA_QDgVTDAQVahfrmrGcOsYQavT3aqWvGQuik-cUbnO1txrYj_BkU-KVleZ_KhtMzeekXTxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/af2be236d1.mp4?token=WxulCYRdIaNmYsAU1aJj5FWHFy_44ifZU1R9eoalgQGeYm90AdfVrCQ35_fbNwpfaLdXHehtHIDrpuibjKTh9lVe7j5gFTabLEcO-rVXgHhakxhhwVpvP3suDvL8J5F52IIMkurzoFSSvqSQN74J6nOHwaU35hoNs1mmRhNmnxvG3c0YAgyuto12xSJIDlFi-WGXgFwVCnOvS8ud5z-Elq2lx9G_DfT4fZKPzD8_mI_zl-XWc5gMG9BOe8CuBjj45J5KsgVbAqEwR_YA_QDgVTDAQVahfrmrGcOsYQavT3aqWvGQuik-cUbnO1txrYj_BkU-KVleZ_KhtMzeekXTxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک بمب‌افکن B-1B Lancer آمریکا شامگاه امشب در حالی که با پس‌سوز کامل از پایگاه هوایی RAF Fairford در بریتانیا برخاست، فیلم‌برداری شده است.
🔴
گفته می‌شود این بمب‌افکن احتمالاً عازم خاورمیانه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148326" target="_blank">📅 10:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148325">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
پزشکیان: قابل قبول نیست که ما مسئول باشیم و فردی با مشکل معیشتی مواجه باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148325" target="_blank">📅 10:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148324">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083f6484a3.mp4?token=IVdRy1J7p69OPSRCVY09wKaYoh3t3YZjgr7RPEICJXvbAV2y63uNLRAVMUGGJSrGHdlmIlmCjfzIF3nV_P1mZvTDE919pPLx6XKMDjYUspn3ZfEqauQsCcnjXnFYeZasl7bctKfi-RTINaX4wCd9_W8LTqezIa21KULchxbTCneZeehOz4HBIneeA71yX4AUbyg2GXKJ6s5NV3PKvZrp155QL6Ws5ue-9SI-Y4Q845WbN6_3YkM_eZ3yzv_kCR2Yvc8T-BzG9HvhAtkbQRo_ra41bOLd7d3_vbY_M4Geb1jHwYVbeWohbAXJLin0bF2u02rI3RFtRfhpXqvzGFfhbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083f6484a3.mp4?token=IVdRy1J7p69OPSRCVY09wKaYoh3t3YZjgr7RPEICJXvbAV2y63uNLRAVMUGGJSrGHdlmIlmCjfzIF3nV_P1mZvTDE919pPLx6XKMDjYUspn3ZfEqauQsCcnjXnFYeZasl7bctKfi-RTINaX4wCd9_W8LTqezIa21KULchxbTCneZeehOz4HBIneeA71yX4AUbyg2GXKJ6s5NV3PKvZrp155QL6Ws5ue-9SI-Y4Q845WbN6_3YkM_eZ3yzv_kCR2Yvc8T-BzG9HvhAtkbQRo_ra41bOLd7d3_vbY_M4Geb1jHwYVbeWohbAXJLin0bF2u02rI3RFtRfhpXqvzGFfhbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر نزدیک از حمله پهپادی اوکراین در منطقه کاپوتنیا در مسکو منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148324" target="_blank">📅 10:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148323">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
رئیس مرکز مدیریت بیماری‌های واگیر: کرونا بومی شده و مانند سویه‌های اولیه مرگ‌ومیر ندارد؛ اما برای سالمندان و بیماران مزمن همچنان می‌تواند خطرناک باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148323" target="_blank">📅 10:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148322">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7442de3f9.mp4?token=QBR_J_e-HIRysr4lNcWMo-Zn_eCAP14su8Qzx61FIicy_cMgOhnDDRM_-VJmvGs0zTkP31cOZ9rRFOoRN_M4u1EZ1dHHqo3a7dhe12WCO78nvBHFJYTgVYj7bpPDsfkbtfzlF-I_zEGnKGtDZZkJ9wGduzDl6nCURDA0Cp_Hl5W547rla-ak0BnVpDZBqCNvhaMlR_ge9uwb-rqCWUG8zevjDT3xITI8gJv2wHx1GKzuTCZrTsgXNmHjOTv1UgxfO9ESyostacEngcCZgbezGmksYOCYlk_7N4rQLiVKVizjI9cFj_u7tYXBoEPHGsA7LnOwZtgXxr-JBmjiES2qNZbg40AVVRm9ruds1NfciYKvWFt2XZaWr1ifnlzo5sLfZ9YcFoJVpE2JXCgEAhVGViP3OQtnu61eXJckzmzScM_7Kv1hogqdJx57UF1d3ig3TmeWWTG68nmOUCM7R0jg8OLCZQHzPuAXN8_8bGPgUrmPNcRB8s5CU2Z-bTNqalsHUONukoXuhHo-mSRgA9dDP9pRuDC2w5pal7NDfexsdd75Bkx8J3-WpGf8mERTeGdM9KVDpZ3Y2ETUK5g0zj4J596hPbPlEc1acvkHyQ51M82cF24QiBVxGNst3Jp-tZj5jUL2zkxFVKFd4di3hTaeufomRX-uTYyW9LpEmByKyeY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7442de3f9.mp4?token=QBR_J_e-HIRysr4lNcWMo-Zn_eCAP14su8Qzx61FIicy_cMgOhnDDRM_-VJmvGs0zTkP31cOZ9rRFOoRN_M4u1EZ1dHHqo3a7dhe12WCO78nvBHFJYTgVYj7bpPDsfkbtfzlF-I_zEGnKGtDZZkJ9wGduzDl6nCURDA0Cp_Hl5W547rla-ak0BnVpDZBqCNvhaMlR_ge9uwb-rqCWUG8zevjDT3xITI8gJv2wHx1GKzuTCZrTsgXNmHjOTv1UgxfO9ESyostacEngcCZgbezGmksYOCYlk_7N4rQLiVKVizjI9cFj_u7tYXBoEPHGsA7LnOwZtgXxr-JBmjiES2qNZbg40AVVRm9ruds1NfciYKvWFt2XZaWr1ifnlzo5sLfZ9YcFoJVpE2JXCgEAhVGViP3OQtnu61eXJckzmzScM_7Kv1hogqdJx57UF1d3ig3TmeWWTG68nmOUCM7R0jg8OLCZQHzPuAXN8_8bGPgUrmPNcRB8s5CU2Z-bTNqalsHUONukoXuhHo-mSRgA9dDP9pRuDC2w5pal7NDfexsdd75Bkx8J3-WpGf8mERTeGdM9KVDpZ3Y2ETUK5g0zj4J596hPbPlEc1acvkHyQ51M82cF24QiBVxGNst3Jp-tZj5jUL2zkxFVKFd4di3hTaeufomRX-uTYyW9LpEmByKyeY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ آمریکا، درباره گزارش واشنگتن‌پست مبنی بر اینکه شمار بیشتری از نیروهای آمریکایی در خاورمیانه نسبت به آمار اعلام‌شده عمومی پنتاگون کشته شده‌اند، گفت: «این یک دروغ است.
🔴
این فقط یک تیتر است که آنها می‌خواهند با آن ما و رئیس‌جمهور ترامپ را بد جلوه دهند و تلاش کنند موفقیت تاریخی ما در این درگیری را زیر سؤال ببرند. این واقعاً مسخره است.
🔴
شاید مردم باید فقط دیگر حرف‌های واشنگتن‌پست را باور نکنند. فکر می‌کنم شروع خوبی باشد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/148322" target="_blank">📅 10:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148319">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ce9J_xARZYckUdJiemVG9rjKnnP5pgTy13S_3og2go1brrF5foeJr119oDQo03jpe8qRg8ym6b8ELEWJVtuRUw5EwiiGkP8LWwk1ua_ZgX2aDfwbrgRjazeqzPXkZ32ybhtoFHXuiMhbNnFJgNxS4Z0mEaq2xCTVSYifljZYVMW3uCwD4oKxb6vbIwp5KlccvUQFQ1PYLbTL4Zj3EpbXujkzC_kAewkVC4-dRNNC2nR7NlksOROqkI7NetnAoGWa3p-7L-4LJ3H_AOvjeMLRvh04OfPMi8j_l5c47aI7y5g9241813yVHEf-BMFxidhxKQNgp5qGDSE1jQ8JDpq_Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uh_LrAGUIrebFDTRmbVbZZ61L9mcasLUFn3e-PjXLKG_808Jxj1gDfoGRbVk_TftGIsMBq7HlDVMyeAPLYX7cV_FGytihFQdC2qpRq3LdxhBhphT5QOHnhiAu9QaaB59DyesSKGtxw9pUnTCA4FTlujKczCqpauNTerBh655hoBZRtuIbPMrvOUXuwulyLEY9QlOUestJRjAEc_kUt4y4g9NSdl_R7XDU1lsx5vxBc2pNLv-AAGeuNdeJLxr-SX5WaD_4PDDr5Q6AJfpTl7Pe38uhpk3re_4vh-a-wqYfwdbY4hZIvTTIKDHZNuuV60XomoLiWHbJE_Dn4siFP56sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Om-P21r0lIK7fOV1jxvJNDJ9xtkDeE6uIfh-w4AYeH5dlDLOBbz-lhfBFn-cTETDtotw1AOvtweDcMzx1u-oRtYCwxqde9mEigoGQQHhtBFiB5-vgT_3idGOu_uEe6GUz6BtvqC5heQyFdnkn5DRTMC74oA34CfNA_qDbN-BWTCLTNHk686eb6eYvI6qlOz3TSI4SahYRyQ434JMHciKxSOBhjl6GgYvFg2b5HVBrIh-fZUrkaytXbBgbQcNOU_EEFooA0o3fMwAkTUVcLl7ap2MogQ8h-MxfJ8SEm_hrCL2vHfDxFrRbQmfVgY6kidvHV6U5IPeYjf3QiCK9zxCpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر دیگر از پالایشگاه کاپوتنیا در مسکو، روسیه پس از حمله پهپادی اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148319" target="_blank">📅 10:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148318">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbq-UKv30mWCaKbh7fDa-04YS0AJLYrOgQdY40UP1cqYgOAdp2COw3S8DabQ2IKpYb3fuolqhadMtBoj7rSMRo-oimBRxP5wOCD1XoYVHgjIJrWPDSHP6IWtjoyXXSN9ud4XT2PSKqYi_R6ESJh7hZL9gwDs9H1iOgpJzF1ArGbIJjhsJJKjxKAFqb8UzoYye0opsRSn7ScGFvD40R1bjPU3uv0BFbR6JYrq-ug7tv2LaSXqvoiF6z6hQkzeHwBcD1elvTiSwdr9CjmAJXNngwvQe4lMuxjZpKD2nNkoKJvHhc4ScTdNQzLHXTIOEw6IOygIS0O3hf2JdO0QYadqEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
تصویری عجیب از پالایشگاه مسکو در آتش
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148318" target="_blank">📅 10:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148317">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
قالیباف: نگاهی وجود دارد که از جنگ سخن می‌گوید، اما هیچ سازوکاری برای پایان مقتدرانه آن ندارد؛ این نگاه با نفی دیپلماسی، عملاً کشور را به سمت فرسایش و درگیری بی‌پایان می‌برد
🔴
انتقال پیام‌ها و تبیین شروط ما از طریق میانجی‌ها با صراحت به طرف مقابل انجام شده
🔴
معتقدیم دوگانه‌ جنگ یا مذاکره واقعی نیست، بلکه هم باید جنگید و هم مذاکره کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/148317" target="_blank">📅 10:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148316">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146935a692.mp4?token=HOTKkFBJEI46GrlSLsdEXTJnaWsJjxzk3SvR4lI52iT8-pFCYRc73owqzRw5uc5LV3P3TxrJLAsEVSsZ3Bt7tzzgZuNHWol7xyjB39Fq-5whOtxdJU1vsfvZDfNlH4KRV4_KSc9cR9NRW8pA7rilMOnBkG6sUpar6zbYNf7-Lgt62aMgDC8AsMqkoRoidUBu3Hg9l5jRkPLr_zkS8G9s3rt5LqqPJYwe1VUphD-1RhER6QGYfVH3XDw1_OiFV-5VSjQthEGDO9Blpm6M5DhvORaXhULY8ZR_7BHj7iWsDnKCD5qERFU5HKPIn9kmkC_5Gkc3iRKL4KMzBu-76oiObw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146935a692.mp4?token=HOTKkFBJEI46GrlSLsdEXTJnaWsJjxzk3SvR4lI52iT8-pFCYRc73owqzRw5uc5LV3P3TxrJLAsEVSsZ3Bt7tzzgZuNHWol7xyjB39Fq-5whOtxdJU1vsfvZDfNlH4KRV4_KSc9cR9NRW8pA7rilMOnBkG6sUpar6zbYNf7-Lgt62aMgDC8AsMqkoRoidUBu3Hg9l5jRkPLr_zkS8G9s3rt5LqqPJYwe1VUphD-1RhER6QGYfVH3XDw1_OiFV-5VSjQthEGDO9Blpm6M5DhvORaXhULY8ZR_7BHj7iWsDnKCD5qERFU5HKPIn9kmkC_5Gkc3iRKL4KMzBu-76oiObw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراین یکی از بزرگ‌ترین موج‌های پهپادی خود را به سمت مسکو پرتاب کرد
‏
🔴
روسیه ادعا می‌کند بیش از ۱۶۰۰ پهپاد سرنگون شده است، از جمله ۴۵۰ فروند که به سمت مسکو هدف‌گیری شده بودند.
‏
🔴
حملات به پالایشگاه نفت کاپوتنیا (بزرگ‌ترین پالایشگاه مسکو) و ساختمان‌های مسکونی اصابت کرد، که منجر به کشته شدن دو نفر در منطقه مسکو و تخلیه ۴۰۰ نفر شد.
‏
🔴
محدودیت‌های پروازی در فرودگاه‌های مسکو اعمال شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148316" target="_blank">📅 10:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148315">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزیر خارجه ترکیه: شرایط جدیدی برای مصالحه بین ایران و آمریکا پیشنهاد شده؛ امیدوارم آن‌ها این شرایط را بپذیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148315" target="_blank">📅 10:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148314">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
توقف پروازها در فرودگاه‌های مسکو در پی حملات پهپادی اوکراین
🔴
آژانس فدرال حمل‌ونقل هوایی روسیه:
در پی حملات از سوی اوکراین و شرایط امنیتی، پروازها در دو فرودگاه مسکو متوقف شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148314" target="_blank">📅 09:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148313">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/057ccc8854.mp4?token=BAkWGJWVf_50S3hiBVBttT_8xZVHxU7y5Z5Fd7MiB05Mufmem7VXQ7DGPh3qakFlm7lbTwq8G0w8U0kotb561hL0CIpPcft5-OYP83HKlQVYQ8snm9GPYjpV6a68XQ8fRiSawWeMX3Fa4MwjxrQ1H7yyWA9sstue1xjr4oWgRH1JEAcAbYVPxR7TdE9NN0UzUlIX3A2AKlmHR5YCDTN0HIxxvybapNPTLGsfx9wLMKvKdxyxQ5zi1reWRal_lfBphiTu_8sHk8KUM0aApsQIs_u_QcNAXXVY-n3Lge6EWqBgHZHlK2h7yWIxzbML23mpHk5gN-mPteHRHEpzBgNM4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/057ccc8854.mp4?token=BAkWGJWVf_50S3hiBVBttT_8xZVHxU7y5Z5Fd7MiB05Mufmem7VXQ7DGPh3qakFlm7lbTwq8G0w8U0kotb561hL0CIpPcft5-OYP83HKlQVYQ8snm9GPYjpV6a68XQ8fRiSawWeMX3Fa4MwjxrQ1H7yyWA9sstue1xjr4oWgRH1JEAcAbYVPxR7TdE9NN0UzUlIX3A2AKlmHR5YCDTN0HIxxvybapNPTLGsfx9wLMKvKdxyxQ5zi1reWRal_lfBphiTu_8sHk8KUM0aApsQIs_u_QcNAXXVY-n3Lge6EWqBgHZHlK2h7yWIxzbML23mpHk5gN-mPteHRHEpzBgNM4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ژنرال حوثی الزبیدی ادعا کرد که امارات متحده عربی از حوثی‌ها خواسته تا پروژه نئوم عربستان سعودی را بمباران کنند و در عوض قول داده است که رسما حوثی‌ها را به رسمیت بشناسد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/148313" target="_blank">📅 09:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148312">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4Ng-ncEdq7vsJ3hZ8RzUzqfGKwtukd4vYEFmLKpL8KQMxB_mAQ1hia18TXIkOCsTlLuk-70C5yVJZ8qPsbhBEKEKamO2_tSfpHBOJB0GIK2ijnH6hVIXE2BJPbbibeDc0AeTHoUjqlw9MD1T_dqy5zTCaDHNzOD9xv2K6F9WV_xulVRxPBa_JrMkwXHMzNXDdBOTVVrou-CpNHUHpsnC7ZWMWUz8EHKGM9uX8HTV-Ly7luVp6JcJoJfJ0fcuYqv5TSrj9Fj3N0S5q4cWgh6oDuM1cAEuqSADLr8k_M9983DPKqo3hFr7qauTST6abThsfWMnO-lRQTev5CSPVUkWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای نظامی آمریکایی از مدل‌های C-17 و C-5، به همراه هواپیماهای تانکر سوخت‌رسان KC-135، در حال حرکت به سمت خاورمیانه مشاهده شدند. در روزهای گذشته، تعدادی از این هواپیماهای تانکر در تل‌آویو نیز دیده شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/148312" target="_blank">📅 09:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148311">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: صدور هشدار سفر برای سراسر غرب آسیا به علت احتمال تشدید درگیری‌ها میان انصارالله و عربستان
🔴
در بیانیه وزارت خارجه آمریکا درباره احتمال تشدید درگیری نظامی میان انصارالله و عربستان سعودی هشدار داده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148311" target="_blank">📅 09:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148310">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ویدیوی وایرال شده از ارزش پول ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148310" target="_blank">📅 09:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148309">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
4 کشته در حمله آمریکا به یک قایق در دریای کارائیب
🔴
فرماندهی جنوبی نیروهای آمریکا اعلام کرد که ارتش این کشور یک قایق را به زعم حمل قاچاقچیان مواد مخدر در دریای کارائیب هدف قرار داد.
🔴
حمله آمریکا علیه این قایق در دریای کارائیب دست‌کم ۴ کشته بر جای گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148309" target="_blank">📅 09:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148308">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzyJtHL2z4BdaM8ijh7scME_caTZTK1nTDWz5EJZSFtHpV7Fe2VdXdXN5giiRwtpwP8iBYoMpE9ZxM2ILSQh8837vy1TyQiuss1PDt8TqIls_KBbUaxb4QUJjBPDKTrEW-bZ55YQyZZ4jbghBetKJ0jffsQTT588Rh5ZvnkswJz3YVY_uttc-XouTzGZZenZhRzOJ8zvjyqlOhKO32zd9JW-P5qAxKzuZN2saSNAzmx7-d3xrXPnUp_1IDt1tUTBrULUSKKnmqq-raESXYvrnFzXaAHoAUerWEH5qSwtCxMw1IcDF3VC3FGG5nIcdMxVUOe_GpheZGXRGMKk4mjFzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
6 فروند هواپیمای تانکر سوخت در حال پرواز در خاورمیانه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148308" target="_blank">📅 09:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148307">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D08VHPkSwx3qqZZ20cMI0sHqihfyC9zhH7_yWoLS5Upi7jApwNJ2IsX0gVxgA9G2-SmHrw6q8yHd4wUfVayE4Hb-lEmbZbVsKtH2nZmBAJqmZWcXzXWkX2WPngL5Lk-TapdUQyNXmtY5-NTj-yh0tVh0xVBU7CtmeHF96WZ9uim83zOYyPRVHOsI5PugFQUNYIF4kLYykzF6vPDlpElf6wIuordHEAfW2E6NlBhqEW7EK3av2tCOjYhm6EKrGDvxnq6RiNcmfYG2xckQHaXIteTF3QHUaetM1t2v7OCmdc8q6VxRnLw7broizUJl-7kjZ1l74sp9lJopON2RSiLhHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای نظامی آمریکایی مدل C-130J-30، هم اکنون از پایگاه هوایی مک‌دیل در فلوریدا (محل قرارگیری فرماندهی آمریکایی) پرواز کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148307" target="_blank">📅 09:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148306">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
تردد در مسیرهای دریایی و هوایی کیش بیش از ۱۴ درصد افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148306" target="_blank">📅 08:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148305">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ترکیه: اسرائیل به دنبال شعله‌ور کردن فتنه در منطقه است
🔴
رئیس پارلمان ترکیه: هدف اصلی اسرائیل ایجاد فتنه میان ملت‌های منطقه و کشاندن آنها به جنگ با یکدیگر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/148305" target="_blank">📅 08:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148304">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BE7rUSAuDD4VMp34F7Za1JonCmWb6GOJPfMdK6fGuflItdFUTzS1znyy08C3FseLYMUf8hTJvCbldf04DuN8vkXrEPnPcMYdl3gUyTbMaHpLJ10Z9Ur0cRGq_Vjvs1yeBlMce63elV7ZS9J0GecfmbExxB0S_u3RoF76li4kUJGtW_6fJbY6ugykbnSBP5zvP_2ia7I6o5RK5SmwVQExqLVGerxjeTK_AzZ3KBV3h8zIRQM8W1BbbQVX9GnzP_u4kN-2lx4XrI96t554cR4nAjwFLJ-wm9qtIv7hj1fIhTuZaeeMcRHJoOuCHHsqMFp5IHq-3jQr3Z1rDAaZDdbllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید از لغو تمامی برنامه‌های امروز ترامپ خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/148304" target="_blank">📅 08:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148303">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
آکسیوس: ترامپ تعطیلات آخر هفته خود را در اقامتگاه کمپ دیوید نیمه‌کاره گذاشته و امشب بدون هیچ توضیحی به کاخ سفید باز خواهد گشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/148303" target="_blank">📅 08:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148302">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OtDo16zMaj9m9VSoe-Koqk57amvfyA3wJO3m48XASOqq-4BKPzmlJrpQIs8uCaX8VFR7XekuKkrr_wFIMnTU6hCC2HehI94nQAyO_wOyyrfSTpx69Cg1xXpw4ALZzzSi1ASHOkn4uaW7HC7Mzci6zB4Xww-JGiulsAWlDIaned_bPTh-ppmwOd_FGPh7JDmn_CYWthGw_n8We2txjdenYASqqLvlqx47g_R4dmkg2AT6Vgk9wUAttc4RK-AyA8XoAJ-2b9u8bm-UaMX-AcKmj5qwdcSpvWdHDeTpaeZJGMThUJUNJ8rfewFwnHWMONw_my8yapMnlYXbMmYcvME4fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / خبرنگار سی‌ان‌ان: نشست ترامپ در کمپ دیوید به دلیل بررسی گزینه‌های حمله به یمن بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/148302" target="_blank">📅 08:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148301">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
العربیه: مذاکره‌ای در کار نیست و فقط جنگ تکلیف را مشخص خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/148301" target="_blank">📅 07:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148300">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ct3lbqAUAxLZMPdcySovJhKmx4Uq3pIsgta8sGn9S5B0mnfRb1jrRuknWiYAthRFE5RFwnx9smny4arnypSiYAngEVCsFdQt3X15xa1FBxQxQ02RfcLD_bKQBjpOSQ2HFR_dzUedzb_x8Cb5bkMikb-mmNcsG80w53aD0sX3wvbOqqI6JBqJaLeDWU9xf8TVy7W8HyXC7wH-np88T-BwxuAI3vPElrt3tW7-qPI8m0I3POtCVt2GhHfpnn0duxlmmPsihwT3EgiZJn0L-lweR67fxN66YkFgleD5DoI3f1bn9ZUkWlkYWeLTYY01lPxbHy6fH6CJxTGgOj5JDbszJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ان بی سی: کوه کلنگ هدف اول آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/148300" target="_blank">📅 07:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148299">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوپینگ | EcoPing</strong></div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/alonews/148299" target="_blank">📅 02:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148298">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaQEf3LoftGghK7xAeP2kMxP2wKA07Bg5jpCfNkai5VHPMc-HRpUkowY-0ZLOjSNQZ7WuKjTqdJfun3k0BnL-LunqDezA1figjjst5RKmB1c-1SOr8qqMSSVLzpFYZnXPsGfuMYoIzZdZRhwdT_Dy7gy4ZNhw_WzcrEJmwcBLtjqIbQHsCI_i5hA78XybhmVl17tqfBk6U5lYPAc8GVOi-iczRpw6W9P5uEnbCrKpV3mTjC-7usQVyeNkBExIcUsPs8S9-aUUNhpGI0sqH61gNEb6DEKJl5rd8zkI_ZKQDgTv8tSG0GMpa2-GpSpkhTICvc3Bo4hdK-_OFAdJgnTSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افرایش شاخص سفارش پیتزا اطراف پنتاگون.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/alonews/148298" target="_blank">📅 01:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148297">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/148297" target="_blank">📅 01:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148296">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
فووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/alonews/148296" target="_blank">📅 01:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148295">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری/سفارتخانه مجازی آمریکا در ایران، با توجه به تحولات اخیر در منطقه، یک هشدار امنیتی برای شهروندان آمریکایی صادر کرده است و احتمال بسته شدن فضای هوایی را اعلام کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/alonews/148295" target="_blank">📅 01:54 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
