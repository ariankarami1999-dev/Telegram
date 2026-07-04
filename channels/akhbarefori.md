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
<img src="https://cdn4.telesco.pe/file/D_LKKWV7a9LL7VQdBcI-CRi0Xpl6zVcC4pni9CbKcYhlQtc3IGbh0uYZuUcKvASv-GwqjZvsD0GYeBiWPmu8bunj-a-AMZykpLbSbb3kzsM6KIylkTwVZ2lVt84gyC5setlLn3IJLqhFbad0PhyjHQcRlqjjhXvq4RCnEYVRPv7UInQ6MWHmqklUtalB0wnvX70FVI9_-QTcLCsRcihMpf-lt72bV8_6YjOWb9_CtTSMEVL6mw8-LbN-8FnXzoM9eUCi8KkfSvE2OVM1nEjRmlEwCrgt-KrDkKhrS6VLViS4fklY5Cy2GL-sPRy75Lj6MX8cAU3EV_hxFWLsflyk3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.27M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 00:56:25</div>
<hr>

<div class="tg-post" id="msg-666649">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2c2c91744.mp4?token=DHcNoJKNCUA8_xgl3SKreTlmCawiGhKUIes74EC_t7PXGp5pTjgVeV1PXaszOLljxzezhfMdzAMA8-0uV2-Y6zmxSK5iHzKHmHcKvWqo70wnwTCOHnAWW3AqJxp4VvgkxVWicxmG9wZsejlHF27rNkbDZYM05vJYhQ9gf4pWCfJ-_rVl0j_t0A5w8IQJ91diBHjEkK0JH9dnqtltZoSQqddBezR4uadBQAU7d6FZsFwQFejsS3VwAWHWOMHrYh04nleLeefDuhECDTpmD7UPNGrj7LnnfWBubHHAmLnc5pFq2yYNXbYIRkHpuc-0rQv24X2FKzaZl9LmkNNfC3-rkIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2c2c91744.mp4?token=DHcNoJKNCUA8_xgl3SKreTlmCawiGhKUIes74EC_t7PXGp5pTjgVeV1PXaszOLljxzezhfMdzAMA8-0uV2-Y6zmxSK5iHzKHmHcKvWqo70wnwTCOHnAWW3AqJxp4VvgkxVWicxmG9wZsejlHF27rNkbDZYM05vJYhQ9gf4pWCfJ-_rVl0j_t0A5w8IQJ91diBHjEkK0JH9dnqtltZoSQqddBezR4uadBQAU7d6FZsFwQFejsS3VwAWHWOMHrYh04nleLeefDuhECDTpmD7UPNGrj7LnnfWBubHHAmLnc5pFq2yYNXbYIRkHpuc-0rQv24X2FKzaZl9LmkNNfC3-rkIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اباالفضل علمدار خامنه‌ای نگهدار
🔹
نمایی دیگر از فضای حماسی و جمعیت باشکوه مراسم وداع با آقای شهید ایران در مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/akhbarefori/666649" target="_blank">📅 00:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666648">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4225985517.mp4?token=V9cHEbAU5Dl3cFg223xMX2NwTd_qu_jIEPsc_xPOFmH7j7mLr0AAJ82B9kAqKC74yKbD2rPkowcLZTTuh7HC_twrAV8N7hJpIw6hBVVeLbgq1ajCbEf_dYQiCPT4kpvYDP7HbgsWamADwj8Kr8DLySK0YnZwOsJ7uE-hih8Vsm3pGkGnq1uGWkbxH6A3BSGdp7eS_zfMf9qgFPXfzCazHMreK3-yJ0-X0lZ_LiGHlXOh4MbrKp7aj5EOY0Mz74G9lJpLJLn4HuuiYlchzqmhWsQ_frDAELIQwarplecHuuDm7GcH_6vmGKnVyVeChLpPTcZt6UVFGSLH0fgHHojIUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4225985517.mp4?token=V9cHEbAU5Dl3cFg223xMX2NwTd_qu_jIEPsc_xPOFmH7j7mLr0AAJ82B9kAqKC74yKbD2rPkowcLZTTuh7HC_twrAV8N7hJpIw6hBVVeLbgq1ajCbEf_dYQiCPT4kpvYDP7HbgsWamADwj8Kr8DLySK0YnZwOsJ7uE-hih8Vsm3pGkGnq1uGWkbxH6A3BSGdp7eS_zfMf9qgFPXfzCazHMreK3-yJ0-X0lZ_LiGHlXOh4MbrKp7aj5EOY0Mz74G9lJpLJLn4HuuiYlchzqmhWsQ_frDAELIQwarplecHuuDm7GcH_6vmGKnVyVeChLpPTcZt6UVFGSLH0fgHHojIUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای ورود عجیب عباس موزون به بیت رهبری برای دیدار با رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/akhbarefori/666648" target="_blank">📅 00:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666647">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3751ef30.mp4?token=p5fN4YZvlFEruUf2Eao14fjOx60F0XgEfjmng3vwtY-Dl5xIBXmTRzbUKKnKAD1MV1_tYaw7ZhvNL_k5Em1HZbc1hz0MtquHrbccB9_QnBIb-SQcREwhkXUbzdq0ngGNXS7rBjgR9g_eJRlrTBB3b5tR3GYuuiByjjR7o9wTxjfwjtQ2UKb1A_E6fuiOzae6VJoqfIEVkjSwRvAgpEL4YeWiowGY2DrtQGrb2jQAhTbeAGokD-12KO_wJZvaMW2RilWkbB9rUIARe0B1zBfa704Xd6vV7MCdgFUe_57SmV8pWi_t4VWHm7W1v3xrsdTtXf8FCi6V8vWG7wYa49wzfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3751ef30.mp4?token=p5fN4YZvlFEruUf2Eao14fjOx60F0XgEfjmng3vwtY-Dl5xIBXmTRzbUKKnKAD1MV1_tYaw7ZhvNL_k5Em1HZbc1hz0MtquHrbccB9_QnBIb-SQcREwhkXUbzdq0ngGNXS7rBjgR9g_eJRlrTBB3b5tR3GYuuiByjjR7o9wTxjfwjtQ2UKb1A_E6fuiOzae6VJoqfIEVkjSwRvAgpEL4YeWiowGY2DrtQGrb2jQAhTbeAGokD-12KO_wJZvaMW2RilWkbB9rUIARe0B1zBfa704Xd6vV7MCdgFUe_57SmV8pWi_t4VWHm7W1v3xrsdTtXf8FCi6V8vWG7wYa49wzfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ ایستگاه مترو شهید بهشتی ‌و سیل عاشقان امام امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/akhbarefori/666647" target="_blank">📅 00:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666646">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JR1dHmg8GWDvD78yBG_6JX8n1BQUMWmNqO532inGenEgAvx6b962VSudGJPZAqM8K5H0v-lcwfV4mse_F2hJxXOuajjdq1LPTlWG3uDje28U3HKreXQDu3SdBhxBF93OQxnpg4ipjQu80wAQYx6j9TK0O30KpnMVvu8sATJB_yR0HBYoQxa702e52gud2Qn-Dph8vGQKhexx6dOXydijKNONKW92ZcjFdN2aYyA7eeV_CmxBMkhxQQu0ADeoJQWoWlK1xYPH3SHi7ctiMSkj12BD9uxv2PyWuGUST4NPk6YCQCPXV1P18cFfIqL-uGYXYDfGUmEH3Zxtey4PqeLTlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گرمای جهنمی در دیدار فرانسه - پاراگوئه
🔹
دمای داخل ورزشگاه محل برگزاری دیدار فرانسه - پاراگوئه به ۶۰ درجه سانتی‌گراد رسیده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/akhbarefori/666646" target="_blank">📅 00:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666645">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fb608438c.mp4?token=srTSZCbdfrHIZSJGp8B3vJVrK0F74YIcM4pQroRY4JqHN2FFzt4r5AsLdGzYvHPUJ1x3YIyCVjDROmC9Nx_16Iqrnsax0Qg1we9XN5ul_lcUT-TLXZoYhPWY_N487Novxx2t640BQyc7XWqEoNs834DpDcMbHGh4dvUuJ8OIbjKwL44cn52hUR4p2PWKlZ97lS_cICTwYeZjtg7agUtZb3FjG67YldMYe5ZfGsUfQ4NYO2L00OFMTL0FnpSkosDPimVGAliiaDCdKYj7rsdqwSkl8nT4k6T3lCNs4ds2zckMUdgf_iY0WLn6PSYc8dHI2lTB7hxNzZothVaBiJLTGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fb608438c.mp4?token=srTSZCbdfrHIZSJGp8B3vJVrK0F74YIcM4pQroRY4JqHN2FFzt4r5AsLdGzYvHPUJ1x3YIyCVjDROmC9Nx_16Iqrnsax0Qg1we9XN5ul_lcUT-TLXZoYhPWY_N487Novxx2t640BQyc7XWqEoNs834DpDcMbHGh4dvUuJ8OIbjKwL44cn52hUR4p2PWKlZ97lS_cICTwYeZjtg7agUtZb3FjG67YldMYe5ZfGsUfQ4NYO2L00OFMTL0FnpSkosDPimVGAliiaDCdKYj7rsdqwSkl8nT4k6T3lCNs4ds2zckMUdgf_iY0WLn6PSYc8dHI2lTB7hxNzZothVaBiJLTGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیت‌الله اعرافی: رهبر شهید، ایران را به یک نقطۀ اقتدار جدید رساندند و معادلات اقتدار ایران را تغییر دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/akhbarefori/666645" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666644">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت-عاشورا-pdf.pdf</div>
  <div class="tg-doc-extra">115.8 KB</div>
</div>
<a href="https://t.me/akhbarefori/666644" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
فایل pdf
#متن_زیارت_عاشورا
همراه با ترجمه
@Heyate_gharar</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/akhbarefori/666644" target="_blank">📅 00:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666643">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-زیــارت‌عاشـــورا</div>
  <div class="tg-doc-extra">علی فانی</div>
</div>
<a href="https://t.me/akhbarefori/666643" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
صوت
#زیارت_عاشورا
🎙
#علی_فانی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/akhbarefori/666643" target="_blank">📅 00:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666642">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2329cb39e.mp4?token=BetVlPdzGUeCCz2ZKbLMoM3q4KFJXQXXJagUPriOrGtXu2csYZWpWmLsS36dcq34BS7u3XH_cJbQO6iv_xb5MHsPNremMk5G31kwROKmRo-FB20trE7c_X31YEYwvqQdXNtaavHdPt84iKOPqqQ3wSkYrTzCHuF9It9ksOXIdirNLSgGgggnM-J8clisLAQiPS3w_Q3-Y8I2fF9a4AdIF21WFyTbxmG6W7rPdkTYmCIfIg9WAbbu84O-sTsDA9uM9gFKWF15tZKORqB61t1IYSSIjpLYrj2ekzylIx64n-Cli74XXzVBS8uT_AJJS1UYczR3uJXNmNR6by8jYGnQgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2329cb39e.mp4?token=BetVlPdzGUeCCz2ZKbLMoM3q4KFJXQXXJagUPriOrGtXu2csYZWpWmLsS36dcq34BS7u3XH_cJbQO6iv_xb5MHsPNremMk5G31kwROKmRo-FB20trE7c_X31YEYwvqQdXNtaavHdPt84iKOPqqQ3wSkYrTzCHuF9It9ksOXIdirNLSgGgggnM-J8clisLAQiPS3w_Q3-Y8I2fF9a4AdIF21WFyTbxmG6W7rPdkTYmCIfIg9WAbbu84O-sTsDA9uM9gFKWF15tZKORqB61t1IYSSIjpLYrj2ekzylIx64n-Cli74XXzVBS8uT_AJJS1UYczR3uJXNmNR6by8jYGnQgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باران‌های سیل‌آسا در چین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/akhbarefori/666642" target="_blank">📅 00:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666641">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
باز هم نقض چندین باره آتش بس و تفاهم با حمله توپخانه‌ای رژیم صهیونیستی به شرق اردوگاه البریج
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/666641" target="_blank">📅 00:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666640">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22e9711db.mp4?token=njezoSGEZ93vxyxiLW1CVkqJxXjlYTAWuNc5zm5GTtaGSXHILhXRrNb8rkmiPVb53UftUOjT81C7zFkZK8_grK5QXVY9S77mPuKBaupBhFRq-Hu2YIcMVinea5I-LHwZaZjuyhdPou22-visdKIJN6xoIQVJ6PRSesyvRYTrOl3ytAJm6j6_4EnxRtOZhlDCuxzlWMhSpuIuNv37Bdj8Yfp8nmxJ9FplYr6-pDeG580rpXVhtsBvvGDyMFGnmBaWYlGs7BpbRGQgOuQyxWJ9gTiVj1yQ6VcidW5H0XRYV579CetE8GkmTU83zdXaIZGzHj8cD05BWQOZ2JqLSm1MpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22e9711db.mp4?token=njezoSGEZ93vxyxiLW1CVkqJxXjlYTAWuNc5zm5GTtaGSXHILhXRrNb8rkmiPVb53UftUOjT81C7zFkZK8_grK5QXVY9S77mPuKBaupBhFRq-Hu2YIcMVinea5I-LHwZaZjuyhdPou22-visdKIJN6xoIQVJ6PRSesyvRYTrOl3ytAJm6j6_4EnxRtOZhlDCuxzlWMhSpuIuNv37Bdj8Yfp8nmxJ9FplYr6-pDeG580rpXVhtsBvvGDyMFGnmBaWYlGs7BpbRGQgOuQyxWJ9gTiVj1yQ6VcidW5H0XRYV579CetE8GkmTU83zdXaIZGzHj8cD05BWQOZ2JqLSm1MpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین یکتا: وسط جنگ جهانی در میانه بازی‌های جام جهانی، در ایران یک اتفاق تمدنی درحال رقم‌خوردن است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/666640" target="_blank">📅 00:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666639">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769f973c05.mp4?token=bsAP2C5gs5c0c1nYeNfC5iOr386Z8-c9m-Q3vphMjnw--LV6LZkGjkzg5h_dkgie9uqoDz7ZrE6vi0XNPHezxwtVD3dRF8xKnvBg8820idm5PDw0nsjuPQpmEE_X-feblK5IoLxk_9dYaBVcLr48yhe9l9smPXrsjwMU-NsrSqNez5l4n1mjIckfhPYJpXDoo_GjBDsdMraOzpXNXEom0J4ggMVAgodZ09fY2bkon4JUPHN3p1jql9W5klRD2NtjbOTk4OQDArasu6TjcSsN7KkdRtUP_0aoQlLTS3ccr_zI-DOmB9tcN1uVCs5wJywMFNwIPvPWVcHqq_Vxymokdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769f973c05.mp4?token=bsAP2C5gs5c0c1nYeNfC5iOr386Z8-c9m-Q3vphMjnw--LV6LZkGjkzg5h_dkgie9uqoDz7ZrE6vi0XNPHezxwtVD3dRF8xKnvBg8820idm5PDw0nsjuPQpmEE_X-feblK5IoLxk_9dYaBVcLr48yhe9l9smPXrsjwMU-NsrSqNez5l4n1mjIckfhPYJpXDoo_GjBDsdMraOzpXNXEom0J4ggMVAgodZ09fY2bkon4JUPHN3p1jql9W5klRD2NtjbOTk4OQDArasu6TjcSsN7KkdRtUP_0aoQlLTS3ccr_zI-DOmB9tcN1uVCs5wJywMFNwIPvPWVcHqq_Vxymokdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین دیدار با شاخه گل‌هایی که روایت دلتنگی می‌کنند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/666639" target="_blank">📅 00:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666638">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa61908915.mp4?token=gOe3FGXkL0YT3oBxDINU27MZZEzMAo-K7fOYAzBJwdjexF4BaZtUeug6g01I1sN_S97Edo7OFuKp-lJVVrp9Cq2C_s8GblTaBgDgf4uwAICXc3XI4QnDOXqVCn_-VY8QXAtE4EZr22KnquiWzk0j0b3SOgKUosetPV8Tp52MuGCOKGXb7m_PCSwHuBwE5tKT2idpieTczxt3hIh7H8KeUritC-bL0uZLBbtAHOcHssd-cbvjpavC3ZFOJ27h5geRm0R9qOIbroIxVuuCEju4c2GIRM8nK18AdkzhK48TN92r8cLd_zd6ufrr8jy5VPhqiQ5tE8h--hezFoAPtKxo1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa61908915.mp4?token=gOe3FGXkL0YT3oBxDINU27MZZEzMAo-K7fOYAzBJwdjexF4BaZtUeug6g01I1sN_S97Edo7OFuKp-lJVVrp9Cq2C_s8GblTaBgDgf4uwAICXc3XI4QnDOXqVCn_-VY8QXAtE4EZr22KnquiWzk0j0b3SOgKUosetPV8Tp52MuGCOKGXb7m_PCSwHuBwE5tKT2idpieTczxt3hIh7H8KeUritC-bL0uZLBbtAHOcHssd-cbvjpavC3ZFOJ27h5geRm0R9qOIbroIxVuuCEju4c2GIRM8nK18AdkzhK48TN92r8cLd_zd6ufrr8jy5VPhqiQ5tE8h--hezFoAPtKxo1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه وداع، قاب‌های متفاوت از حضور بانوان در مراسم وداع با رهبر شهید انقلاب در مصلای امام خمینی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666638" target="_blank">📅 00:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666637">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
استان میسان عراق چهارشنبه و پنجشنبه را تعطیل اعلام کرد
🔹
استاندار استان میسان عراق روز شنبه اعلام کرد که روزهای چهارشنبه و پنجشنبه آینده به مناسبت تشییع پیکر حضرت آیت‌الله خامنه‌ای در عراق تعطیل خواهد بود. #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666637" target="_blank">📅 00:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666636">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
المسيره تصاویر فرود هواپیمای ایرانی در فرودگاه صنعا را منتشر کرد
شبکه المسیره یمن:
🔹
با فرود هواپیمای غیرنظامی ایرانی و اعلام نیروهای مسلح یمن مبنی بر ادامه دائمی پروازها و مقابله نظامی با دشمن سعودی در صورت تلاش برای مانع‌تراشی، رسماً نبرد برای شکستن محاصره فرودگاه بین‌المللی صنعا آغاز شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666636" target="_blank">📅 00:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666629">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qe8dR9FWuuE8ZJT5DnZr3qAdFx-6_OG1V2B3IXMjn2awfw4D7qam7P_8LOKPyBDtIXPmbznA0KY9E-K7zsOpUaSF87JdLX_jGqLScyLNt6L1OMuItZzPX-kmjuxAcGQ-auETkxnQqsjxRuns26kVRy2vJJE9LxYamb8gLG2zlqAVxOtI4NuewMMb0n6IG4rJvNu6WhUb8DOiBGrH6Dt4JLpP1X0XTVtKfkydJ79Wcg7IUrdu3hMFbSHAJV7j2gdrOSKZWdtPqgNKdZYYm1zbuJgd_xX5Nz6Zgks56xV4Jtk1id7ulcDFbpMkqgb6ZEIGXou5UzQkciRUZassItG7Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kq6TVoVQyV0xrhV2ZX0Xj-1CQ3t1mTdVjfo0kHEHYmebbO2lY3eZZ3szos9fewX6wbWTpsW6rZuqujeCBHgfZyjnkNWtI54b21Zz2QmH-WgT4eFfOM4bTiMH1eaeSC03gIH_ZpRoZS-aEZvcP0USVFx6ZJSwV9xrTxuBnBdfkkKZxyWG7RmbzhYU94BDTjHbWYSLDEfFpWRLOzIzBoKS2Mvk0_bPsmEK3KDgzF5yWMlzSUnb_3Bi8yxIS2XEp9fnr4uBBCW-ImxFZWzax2Vr_5TEpAk5Qlhx96DK_SUwQjzmBboD7ihe1Jjh_j-NeSdLop9iM1jc1kjRrZ0T-7IzjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n0-n36SYAzG6PF7WebU_CJ1xZQGvoZBAPAMYDAgGEZORx2km2sw8JqJGc98fVbqO5maTpsmmawJDsuXFFhgaSO3rNeaPNPN4FOWCrG6sET5IAFkOPsAw4YsXoCsi8Sie4a655g-S2LjLN-y83BbTzQMQ82PEFJgymsT-Jr_gY7gF_bT08KHY1Pvc2z6-b3REFQ3_Ne4pbbAZKadU8KUqDnbabmpKJOiI5a_Q07J4c4bOy1oJQc-iRenayPfDN_ZyksVAjMWNRnOK8-aXbsKcisLhbgziAbwSEWJqguofrymSgfBK2aHAtPxIn3soPvgaVeTwKMT4MBe4Z6YEPuuSLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSnS1psJorHUFAoKx7jQvBGJvVJed46h5la58dbW7qv6CFMBd5GdGb4ZxiFWEXOlvqZ6j1rwJ50EYJM3RTZhvi_-d_Zqe-4fbZXT0jhQqWsHYoa8i-YuDiej1K-N4zqpOdc0p_Omskkc3PMu0l1G-rI5P26KmYQlk50A2XnUtP40ASRBu4vSfX8i9ndHb9boDiqZArxS8Cki5e2JKSIsK6oCVHpEnO506mSt-rfMRtZB2ABU7Ynm-Ajc1AScTBe3_lvaIQwTD93fTBtyaXytj254p0wuGyU41El9A-1H6cYEuRNlF-7nyHWA7f9jBiTYjQOdqAW7phvIXy8jTubkQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ri6VMe2TZch9aJFE2WMbHNzITOb_xLjdIyRpkVTkXZPMf6kHYxUTFxJfuvZw9TzBNaH2blBcF20DUXYLuP4jjD_Gf9yv91D4gOywMyQj-K3CijtB635JLOAbuc2CqNk63vm-eEbeIkqZ39F_JJ0UlKrrh40qVwmi8ZqPaaqSXl3DrZJOp_yaQkmetNmb45hS6RG-o0bUrOS2F2o2h91_SU49D8vEuOQIzFplcZ_rW551EAHQ5Ri18rA9p8_t52ogmu-WLERkkHa3P_5cftIo90R58R7wRXF5hn8hO-f0jOIpZVRdEaiKWtYcUb_4P8_is2Goqe7tKLBh7fHmxHCTHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tF78CnRObChqp2f4QpsHGaDuIF_19jLxzjyysfEMMPGqSwe810UTsr4dhNFuE2KZ0Uy6O_AqnjemI38CPgQHDVZfq7Hn5UyM8rgHBuq_ThNFvAboDqJ44I8rq3uxCYc7EyNhFaK6OIRg8aewUlUP6UqUtpt4UVlw_1_iXi7iW6M7YOBOWOLWLTVxdUWEidQIHhEplLRJ-TQD1HOUY4eFovo-G_Oil8BPIIVHyzqcKbnEDj9wjFMWRGOFklxQEkFODcy9mtVhJhVpV7bOi-0a6QFviP1dXR66MZ8r7Hj41QpaNovlt0lpb6dB6wP_ZMh3tzFtqkYJivmCuA0UywYmKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n0-n36SYAzG6PF7WebU_CJ1xZQGvoZBAPAMYDAgGEZORx2km2sw8JqJGc98fVbqO5maTpsmmawJDsuXFFhgaSO3rNeaPNPN4FOWCrG6sET5IAFkOPsAw4YsXoCsi8Sie4a655g-S2LjLN-y83BbTzQMQ82PEFJgymsT-Jr_gY7gF_bT08KHY1Pvc2z6-b3REFQ3_Ne4pbbAZKadU8KUqDnbabmpKJOiI5a_Q07J4c4bOy1oJQc-iRenayPfDN_ZyksVAjMWNRnOK8-aXbsKcisLhbgziAbwSEWJqguofrymSgfBK2aHAtPxIn3soPvgaVeTwKMT4MBe4Z6YEPuuSLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اولاد حسینیم و خون‌خواه رهبر شهیدمان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666629" target="_blank">📅 00:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666628">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5f384d1a.mp4?token=vuO1RR8IOOWO5w_IdsxHcurZLijh_yOyIO_PRDFlKfktsvqVwHWbu-ashvH3ALkti-mHjQa9ZZ1pw0LOYDRlTOutGrfcENAZsLVKln9JLTe6wjBs2_xNIeU2TENxWobb2SKCdL4pWThwddFvWJ9cm-55AzhfVY-X3o-c-11lzCo6UaAaDMDjS7nnUv_0tbv_vRc1zGLT3VXrRIlxbLH2JHKQrxE6wOuFh1y06y2f0N4DKJZuB10PTh1_lTyLjUQJQi9MHNdrjkeqoHGvR5yXjB-am_2yvgTS9T3flfzikmxrv9X85swNTo2Qt9NYMDihk-KpXBydhgY84x1OHz_ooA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5f384d1a.mp4?token=vuO1RR8IOOWO5w_IdsxHcurZLijh_yOyIO_PRDFlKfktsvqVwHWbu-ashvH3ALkti-mHjQa9ZZ1pw0LOYDRlTOutGrfcENAZsLVKln9JLTe6wjBs2_xNIeU2TENxWobb2SKCdL4pWThwddFvWJ9cm-55AzhfVY-X3o-c-11lzCo6UaAaDMDjS7nnUv_0tbv_vRc1zGLT3VXrRIlxbLH2JHKQrxE6wOuFh1y06y2f0N4DKJZuB10PTh1_lTyLjUQJQi9MHNdrjkeqoHGvR5yXjB-am_2yvgTS9T3flfzikmxrv9X85swNTo2Qt9NYMDihk-KpXBydhgY84x1OHz_ooA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات حمل‌ونقل عمومی تهران در روز دوشنبه
معاون حمل‌ونقل ترافیک شهرداری تهران در برنامه پرچمدار:
🔹
در روز بدرقه خط یک BRT مسافر پذیری ندارد اما مترو همان مسیر برقرار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666628" target="_blank">📅 00:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666627">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/va4z76lR3asxCwhzScyUzHzXDSFWblMLJFlMfcYHtMuZH7_PfKFK8FvGgCdbISjZgezTr3imyNhsdLw2MsHUh4c-CwCRaTEfqJ5weWRIAiBU7YcovLCa_SsU-8p4BcQ_x0TbZRpPeJYiqE4wXr4b5Kirg-zTpN-G758OjAe74pXgpI2F0FIT3Fb55khSD307WJolj3bMhCSqM7sMvwgVk0grgDqbY0ap-lp6PRutai5d_K1WOHTUudjS0bBzBzWGLhNZhdybf66GylnEXs68MFmrG1Xc9_z4A3nNlW8GhJBUQfWXgnYw4ogE-ch_HUmPQ93UdAS-ImKqx_FxkY-ebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
به تو از دور سلام
چله زیارت عاشورا تا اربعین حسینی
#روز_دهم
▫️
امروز با خواندن زیارت عاشورا به نیت شهید محمد رئوفی نیا  ، دل‌هایمان را به سوی امام حسین (ع) میبریم. امیدواریم که ایشان ما را پیش اربابمان شفاعت کنند
@Heyate_gharar</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666627" target="_blank">📅 00:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666626">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d2d2c1542.mp4?token=fk5AAEDA8XEynNjnBLe2SO5HLkOagSTQmy_cnTfe264lK6Dcu8ebQu0_lPwCX1NaJbYgPVUwp-PR3PaerulN6SKHJaSXn_Ela59K0RA1JjKX70xGq3JsG0le7qRDI1C20SI5y3-oGDFbd-4M3MF_83c5BHa8IH_SIgxHmO-8GXqijt4FrJuxyqRfef1PxkQurw78ZS8a0n-VYI9S4ejJY0vYbv0BKkDHoCq_l7S3qExQX2u7h-7fvDb_vJbBAKGugf_OkMnl0jUSw9lacmreZJePbrSaELwGUwo5yQQmVo7kQrfwj4n7U8KjCHuaHoLBoKLrDah3bVtB6VkIfU3ffkDqpQsZJHPRxyFDl9ZO0za5s0cYGWtg0C1odOe2oIOoGG6iVRJ2Qb5tyGYzRJPg-BkZta1ZZ-M-g51tcVRnxaYG86JMsZMbcq_29kd-EXt4lqrSJXvF4cuRF4mHAjDjaoVmUR563ndF6DAAusazwXV56Hs5ONxQ9F4HQV_WZowrEIczZRJIQyy2EOSSTkwiO7LlFfYDKcnoZQXFCgWtS-Ag_ltC-tGieh-hL5lYMiR_sLpaiMCv0rFJz482IxY_sq5peppKwAstxuE4kh7wE1BFTI8hr359RvQfrQlm47Z54KdB9fGHBRxJH9_Ld0LFaJHjh-l9dw7VdCmj50ecnBs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d2d2c1542.mp4?token=fk5AAEDA8XEynNjnBLe2SO5HLkOagSTQmy_cnTfe264lK6Dcu8ebQu0_lPwCX1NaJbYgPVUwp-PR3PaerulN6SKHJaSXn_Ela59K0RA1JjKX70xGq3JsG0le7qRDI1C20SI5y3-oGDFbd-4M3MF_83c5BHa8IH_SIgxHmO-8GXqijt4FrJuxyqRfef1PxkQurw78ZS8a0n-VYI9S4ejJY0vYbv0BKkDHoCq_l7S3qExQX2u7h-7fvDb_vJbBAKGugf_OkMnl0jUSw9lacmreZJePbrSaELwGUwo5yQQmVo7kQrfwj4n7U8KjCHuaHoLBoKLrDah3bVtB6VkIfU3ffkDqpQsZJHPRxyFDl9ZO0za5s0cYGWtg0C1odOe2oIOoGG6iVRJ2Qb5tyGYzRJPg-BkZta1ZZ-M-g51tcVRnxaYG86JMsZMbcq_29kd-EXt4lqrSJXvF4cuRF4mHAjDjaoVmUR563ndF6DAAusazwXV56Hs5ONxQ9F4HQV_WZowrEIczZRJIQyy2EOSSTkwiO7LlFfYDKcnoZQXFCgWtS-Ag_ltC-tGieh-hL5lYMiR_sLpaiMCv0rFJz482IxY_sq5peppKwAstxuE4kh7wE1BFTI8hr359RvQfrQlm47Z54KdB9fGHBRxJH9_Ld0LFaJHjh-l9dw7VdCmj50ecnBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایندۀ اهل‌سنت مردم کردستان: شرکت در مراسم تشییع، ادای دین به رهبر شهید است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666626" target="_blank">📅 00:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666625">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDVuvhK6rCGYZxWk8zqYlrgiwOgcIM4tXWPwIKdHCIxQdYd1pN6D1oi7QXDm21IySXLAcZWQtCRsPP5kR25Cbky-CiRNykJ2h4eFxq6PaPawZpOakd-GSRAp87lBoLrUWsFgRx-Thar4GJiX_ndoboMtDpPB_I0x5T2k_f-kkTEUEvSN5ruio-9tNd7qlHEVht7l_qxqzwiYODXaCqTajHN_77zOiRilUjsgyE9j2pLXZ6xCjc14R2BYzHmMIYk66yoh76rO3OYu6hknw31aq3rbU0EbM1ouskfCCiHl29Nhuxj7xhF3btYh_E6IJLU8HamUUFHe5bWV0lleMkfkAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/666625" target="_blank">📅 00:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666624">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9f3489673.mp4?token=Qp0b2S9y9XSc6zcNuwwwhGiGWFG7CThHKLAGgdrqM-cmDa-t5DYnogD3AiEMFhbGeYxENQloGYEIb547h_DU7KQhVO6DDSVFQetH1abWR3uKmhIYfvvbnU-uUV_WQlOKfbY7CWSTA3pMNHM8oTwm9Ad8HTTveXjsflQ-Wj87MITSUMZ8S0W_uw5Vfvzc5GG1tli6IP8r-W3sZBs-ImNbPUsInJoZsnLZpJ6Nns_3juyNtn949J7Mb7sVdTXXYkQmNBJcrHYT0N4G2i-aVuUT8wfGTra3QMrvky7WA53tXk8UG4H6GK8EKK-3Ip2RVdKBn63itx3KWScoXT4Jrc8uxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9f3489673.mp4?token=Qp0b2S9y9XSc6zcNuwwwhGiGWFG7CThHKLAGgdrqM-cmDa-t5DYnogD3AiEMFhbGeYxENQloGYEIb547h_DU7KQhVO6DDSVFQetH1abWR3uKmhIYfvvbnU-uUV_WQlOKfbY7CWSTA3pMNHM8oTwm9Ad8HTTveXjsflQ-Wj87MITSUMZ8S0W_uw5Vfvzc5GG1tli6IP8r-W3sZBs-ImNbPUsInJoZsnLZpJ6Nns_3juyNtn949J7Mb7sVdTXXYkQmNBJcrHYT0N4G2i-aVuUT8wfGTra3QMrvky7WA53tXk8UG4H6GK8EKK-3Ip2RVdKBn63itx3KWScoXT4Jrc8uxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک نماینده مجلس: شخص آیت‌الله سید مجتبی خامنه‌ای دستور تشییع پیکر رهبر شهید انقلاب در مشهد را دادند/ اگر امکان تشییع پیکر رهبر شهید انقلاب با ماشین در مشهد نبود، از طریق بالگرد پیکر منتقل می‌شود
حسنعلی اخلاقی امیری نماینده مجلس شورای اسلامی در ستاد تشییع رهبرشهید در هلدینگ خبرفوری:
🔹
مکان تدفین در حرم مطهر مشخص است و نماز نیز خوانده خواهد شد.
🔹
بنا بود در مشهد مراسم وداع رهبر شهید برگزار شود اما با فرمان شخص رهبر انقلاب وداع به تشییع تبدیل شد. رهبری دستور دادند که در مشهد تشییع انجام شود.
🔹
باید تجربه تهران و قم دیده شود، ممکن است در اجرای این موضوع کمی تغییرات انجام شود ولی در حال حاضر قرار است به مجرد ورود پیکر به مشهد، تشییع برگزار شود.
🔹
در این زمینه اگر امکان حمل ماشینی بود، اینطور پیش می رویم اما اگر نشد، از طریق حمل هوایی از طریق بالگردهای خاص این موضوع دنبال می شود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/666624" target="_blank">📅 23:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666623">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74f66194c8.mp4?token=ZfXwjSvh6XDZ37ZaC8ecNb3XH4Y5fE5AEq5h4vdtG-8sZuZcEz-STNxHQ-PpH5JZIPPvIQf6paK5q3pw6kjjYzdGewtIjkUpqVZmf_fRcjU26qOp1akCl0B5IzsqzShPUTR1-57Ra_pKMxiRaeQlpWhYa5TGS89nsujOhjr8ITjNvUSWom8ZRA5i1_bNq2zmt22P0UysroGSL3SjGIVJkx-lWq1FvptL8mXRURmwd7kzmLiWrMsULt8zb60mvIEEEH0q-5ghGdykiLm6z7G0sYnmrBnXgY7WS3JxBH0R3w53PNw9SrZtix2cTmJZ7rwmPUfmlfhnaOnp0wHVvgK0oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74f66194c8.mp4?token=ZfXwjSvh6XDZ37ZaC8ecNb3XH4Y5fE5AEq5h4vdtG-8sZuZcEz-STNxHQ-PpH5JZIPPvIQf6paK5q3pw6kjjYzdGewtIjkUpqVZmf_fRcjU26qOp1akCl0B5IzsqzShPUTR1-57Ra_pKMxiRaeQlpWhYa5TGS89nsujOhjr8ITjNvUSWom8ZRA5i1_bNq2zmt22P0UysroGSL3SjGIVJkx-lWq1FvptL8mXRURmwd7kzmLiWrMsULt8zb60mvIEEEH0q-5ghGdykiLm6z7G0sYnmrBnXgY7WS3JxBH0R3w53PNw9SrZtix2cTmJZ7rwmPUfmlfhnaOnp0wHVvgK0oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اهتزاز پرچم‌های سرخ در مصلی امام‌خمینی (ره) تهران به نشانه انتقام‌ خون امام شهید امت
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/666623" target="_blank">📅 23:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666622">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb1dcd259.mp4?token=n9ym0nqKIjUm6JThX8OJ3B05irER-m6KIbivHyoorsUYTxmVntF4Jvtqt3dq6MQIWWVHjEkx6ApDWwjg7DgUSUPxfIiqov3v7y-RWx5nfggQGYPz2JMexytzZ71e_FQj5ITdsrImm8rIHpdS9pJeTt_FZWenWIUqAMg97lJSRzXUc_5trPIXm6SmSQiRVFi3oa6iEDLG156brSt8wpGhj47DzJwPoHaBz-bv9i8_euKn86hDBI0f3hW5M9U26xJfrKxmYI3LA7Nimhe1OKYDaV6w7anUsM_pphLDT4gWfmGu-1Zg4SzdkRUNVMdoQqwkN3sgA_2i9UAdj7pe3_AsZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb1dcd259.mp4?token=n9ym0nqKIjUm6JThX8OJ3B05irER-m6KIbivHyoorsUYTxmVntF4Jvtqt3dq6MQIWWVHjEkx6ApDWwjg7DgUSUPxfIiqov3v7y-RWx5nfggQGYPz2JMexytzZ71e_FQj5ITdsrImm8rIHpdS9pJeTt_FZWenWIUqAMg97lJSRzXUc_5trPIXm6SmSQiRVFi3oa6iEDLG156brSt8wpGhj47DzJwPoHaBz-bv9i8_euKn86hDBI0f3hW5M9U26xJfrKxmYI3LA7Nimhe1OKYDaV6w7anUsM_pphLDT4gWfmGu-1Zg4SzdkRUNVMdoQqwkN3sgA_2i9UAdj7pe3_AsZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین یکتا در برنامه پرچمدار: مردم عزیز! خدا به ما رهبری عنایت کرده که فرزند شهید، همسر شهید و دایی شهید است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666622" target="_blank">📅 23:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666621">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
حملات جنگنده‌های اف16 عراق به مواضع تروریست‌های داعش در کرکوک
روداو:
🔹
نیروهای امنیتی عراق روز شنبه با اجرای رشته عملیات هوایی و زمینی در استان کرکوک، مخفیگاه‌ها و مواضع تروریست‌های داعش را هدف قرار دادند و در عملیاتی جداگانه در این منطقه، یکی از سرکردگان این گروه تروریستی را به هلاکت رساندند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666621" target="_blank">📅 23:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666620">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_lFwfbxK7sgk56irwjJWcYB34lRjnISR46YQio_bqvBH2fnCL-iq5nfeky4LFf80GsgQ9NQA0jCgQvTfhmR_wcu5bZE1YH_4vXAN73HYo6EtOSKzZ0Dtlx0n59kasQGshyDsVGd9jsH8XbI-ywsXp0cirL8dfnmbxW1K0g4PVelxXikLD7-lqLOorL9MrAyiDhP4XhMsMbodAt4DLilcl37ZPk2eLY734LEILbPj8u2Znu_gXTPY93BvdmOGEYLTrFKNEAy_yjClAcbGLkBcvbyddYA35sYUQlhcFDBplgSpf5KsYPFLrazmcpzz3m1IomTXR08M1E512x-1r-LKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ای قلّۀ سرفراز ایران بدرود
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666620" target="_blank">📅 23:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666619">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔹
از خبرهای پُربازدید امروز وبسایت خبرفوری غافل نمانید
🔹
🔹
متن و حاشیه مراسم امروز وداع با پیکر رهبر شهید انقلاب + آلبوم کامل عکس و ویدئو
👇
khabarfoori.com/fa/tiny/news-3227648
🔹
خون‌خواهی؛ آرمان مشترک میلیون‌ها آزادی‌خواه | سرنوشت ترامپ و نتانیاهو چه خواهد شد؟
👇
khabarfoori.com/fa/tiny/news-3227630
🔹
واکنش ترامپ به مراسم وداع با امام شهید: یک هفته مرخصی دادیم!
👇
khabarfoori.com/fa/tiny/news-3227705
🔹
ادعاهای تازه درباره استعفای پزشکیان
👇
khabarfoori.com/fa/tiny/news-3227847
🔹
کالابرگ این افراد حذف می‌شود
👇
khabarfoori.com/fa/tiny/news-3227640
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/666619" target="_blank">📅 23:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666618">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
پاسخ سفارت ایران در ارمنستان به اظهارات ترامپ علیه شرکت‌کنندگان در مراسم تشییع رهبر شهید
🔹
انسان‌ها را می‌توان کشت، اما آرمان‌ها را خیر
🔹
شما آیت‌الله خامنه‌ای را ترور کردید، اما در واقع، شیشه عطری را شکستید که رایحه آن همه جا پخش شد. شما این چیزها را نمی‌فهمید چون نه تمدن دارید، نه تاریخ و شرف!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666618" target="_blank">📅 23:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666617">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f2df4beb.mp4?token=g5IpaM_wtHt7YChzyeM7qs3nmA7hXHbSKo55GbVbzCcdGzztVP2SH2PwvXMoqC8WOfmR7h06RroEZJtdlbeFln0x_-S9cMxpSQhqr-RDj-P-7aZLHSYHtct1EpO3tZ2gr3SpaEn700GW9BPdWpzEQVCXgrM03sXZaAJvJEA425NGuf1N14sn8b0QzDl5fJoqFt7_QVSy-Vu-4I45xapOZjGDGJ3mMfjOgIwa154dVWOiZ3-XI1L0cWwQxE3aCDCHldQvbJrgZowSysIXfdgi3jP2URxVLu0qbUXJxmlcwOVgmqUqQ8v-94aXNGPk01orsPCAkZckyyugdPtYFhPYQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f2df4beb.mp4?token=g5IpaM_wtHt7YChzyeM7qs3nmA7hXHbSKo55GbVbzCcdGzztVP2SH2PwvXMoqC8WOfmR7h06RroEZJtdlbeFln0x_-S9cMxpSQhqr-RDj-P-7aZLHSYHtct1EpO3tZ2gr3SpaEn700GW9BPdWpzEQVCXgrM03sXZaAJvJEA425NGuf1N14sn8b0QzDl5fJoqFt7_QVSy-Vu-4I45xapOZjGDGJ3mMfjOgIwa154dVWOiZ3-XI1L0cWwQxE3aCDCHldQvbJrgZowSysIXfdgi3jP2URxVLu0qbUXJxmlcwOVgmqUqQ8v-94aXNGPk01orsPCAkZckyyugdPtYFhPYQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجموع سفرهای انجام‌شده در شبکه متروی تهران به ۴ میلیون و ۹۲۰ هزار و ۶۹۱ سفر رسیده است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/666617" target="_blank">📅 23:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666616">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83029552c0.mp4?token=j9i_Dnr02QbfwbKIof_qz8e9DkkAk_X5LZdb59Y3HeMX4jRWzbbcMTKm_kx0Q24FDi0CEL78iR1Yv9Yag0524dP0zqrKXkIbs99h3Z1xuUFkjHy_diaZ-0vHoYTIXWRTSXW5FLKqDSbD1j4B4c08mHxxj99QOCsUxm15djlJGWpWH9ayOu-LDNZMDfIJOB1KYIGc84SFXc2cn0klwXCWoEAvTzd6ubEnf-gmPr929A4tLE0bwOpzs5ndiHpe0aq9uUlteO07WepL6Qp4NIRhWy2uxSyhL_8y26AfFKPGyHtICYlt2ElfYp-XzEl3EDHXSBOYEmFmISymfuGDF19Qtb_GVaXV2BXnm9sCxaNQzulgY76G5MwBrAYFJqFMD82Di923ZiC54xK6q-I4QyxE52vj2C3iagBiAFBBUASNG6rxG-3-WZvjSYEyI4aiSczyfxoMBx2LnPhHJhqPu61yd8fpBo1mRCqPEU7kCX1vC5pyHiZC8HsfkR1zdBbLyR9xNpXlUTdwEzXaID0AAToyMtgknke7tsmbiQjlE1Tgr1k1u_ITQ-LaDCnSbZmKAmusxVEdM-dAZTS46RSQFKutCZMjHrP17Hp9odxLDgKXF1IdaaoU7H3x3W_fjXOp0lFSJX3qjso05SyxKDSmDMAT9xl2aQwo72kGa7c_fjKH0Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83029552c0.mp4?token=j9i_Dnr02QbfwbKIof_qz8e9DkkAk_X5LZdb59Y3HeMX4jRWzbbcMTKm_kx0Q24FDi0CEL78iR1Yv9Yag0524dP0zqrKXkIbs99h3Z1xuUFkjHy_diaZ-0vHoYTIXWRTSXW5FLKqDSbD1j4B4c08mHxxj99QOCsUxm15djlJGWpWH9ayOu-LDNZMDfIJOB1KYIGc84SFXc2cn0klwXCWoEAvTzd6ubEnf-gmPr929A4tLE0bwOpzs5ndiHpe0aq9uUlteO07WepL6Qp4NIRhWy2uxSyhL_8y26AfFKPGyHtICYlt2ElfYp-XzEl3EDHXSBOYEmFmISymfuGDF19Qtb_GVaXV2BXnm9sCxaNQzulgY76G5MwBrAYFJqFMD82Di923ZiC54xK6q-I4QyxE52vj2C3iagBiAFBBUASNG6rxG-3-WZvjSYEyI4aiSczyfxoMBx2LnPhHJhqPu61yd8fpBo1mRCqPEU7kCX1vC5pyHiZC8HsfkR1zdBbLyR9xNpXlUTdwEzXaID0AAToyMtgknke7tsmbiQjlE1Tgr1k1u_ITQ-LaDCnSbZmKAmusxVEdM-dAZTS46RSQFKutCZMjHrP17Hp9odxLDgKXF1IdaaoU7H3x3W_fjXOp0lFSJX3qjso05SyxKDSmDMAT9xl2aQwo72kGa7c_fjKH0Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خرج زندگیت کن
🔹
اینا تجمع هم می‌رن شبی دو تومن میگیرن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/666616" target="_blank">📅 23:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666615">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2d6a8980c.mp4?token=MDBuwsxGLecl0IFSDWRVHHgUWI29fV7sZhwjcHCip2VaGQLunJQBuX2kCNcHdAn5W7MwbJMK2LgUBptB6AUy8zsiWd5BZ2D7ay355_u3vy-qsfyohlvqCTGf0XQ0zr8GieYbUneX5bVKq25SYuzpkAx3rg27JgU6hkTYtYeJwqW3Uksawt77ZO4R37C-m-pG77-ICg9gyGm3W6_G0l3aZxfPdr9Uvfu5LXxpSuS8GXhsrXFqkAIZnQIZsqxQtgQzx8QqOUDRVGKbc7TdEwqw0tD5PCRY6aqZHPzxdyNR0u6ASIJvAkND-0vhjeebnjYRAC2JflUsVjf6JNbr-Emx8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2d6a8980c.mp4?token=MDBuwsxGLecl0IFSDWRVHHgUWI29fV7sZhwjcHCip2VaGQLunJQBuX2kCNcHdAn5W7MwbJMK2LgUBptB6AUy8zsiWd5BZ2D7ay355_u3vy-qsfyohlvqCTGf0XQ0zr8GieYbUneX5bVKq25SYuzpkAx3rg27JgU6hkTYtYeJwqW3Uksawt77ZO4R37C-m-pG77-ICg9gyGm3W6_G0l3aZxfPdr9Uvfu5LXxpSuS8GXhsrXFqkAIZnQIZsqxQtgQzx8QqOUDRVGKbc7TdEwqw0tD5PCRY6aqZHPzxdyNR0u6ASIJvAkND-0vhjeebnjYRAC2JflUsVjf6JNbr-Emx8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام عابدینی: رهبر شهید انقلاب در ما باوری ایجاد کرد که امروز حتی کودکان ایرانی نیز ناوهای آمریکایی را به تمسخر می‌گیرند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/666615" target="_blank">📅 23:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666614">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KN7Sk_Tqvj1dDUQ88f494gKzMN02a1ugy8VXqvKmM2mqlx1SRvhdChcoIYIyfi-ikTlZbDc2VkolhoyLU1aJh8RmtDkXI21w6fIvjcO2N1h3UTeVwIqSTWaSkN7ADrnslFZaHiOFjW7QFaVfVHxexJs4IHDAZnVxZ6uUXASs_V99I8HQYMBVUdjFkn00Ws8IRc52lTtM3TVB6VPWu37IVSdOADxIABVvUfVHm1W_we9dFWvJ4yFJbJJiJJIq8HWqzfPamvGUwYWJGgLMbgQsprtkmBR0s5tMvfP_Ij596cqT2lUhTkSXPbkX-_0K3eEtPIKcQwZYrwRvmbokAYdWUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقرار تیم‌های تخصصی ارزیابی خسارت
#بیمه_البرز
در محورهای مواصلاتی تهران به منظور خدمت رساني به زائران مراسم وداع و تشییع رهبر شهید
همزمان با برگزاری آیین وداع و تشییع پیکر مطهر رهبر شهید انقلاب، کارشناسان و ارزیابان خسارت مجتمع تخصصی خودروی
#بیمه_البرز
در پلیس‌راه تهران - قم و سایر محورهای مواصلاتی منتهی به پایتخت مستقر شدند تا خدمات ارزیابی و جبران خسارات احتمالی خودروی زائران را در سریع‌ترین زمان ممکن ارائه دهند.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5055</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/666614" target="_blank">📅 23:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666613">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
استان میسان عراق چهارشنبه و پنجشنبه را تعطیل اعلام کرد
🔹
استاندار استان میسان عراق روز شنبه اعلام کرد که روزهای چهارشنبه و پنجشنبه آینده به مناسبت تشییع پیکر حضرت آیت‌الله خامنه‌ای در عراق تعطیل خواهد بود. #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/666613" target="_blank">📅 23:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666612">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/539939e159.mp4?token=R6AVhE6594_LP4pLMLSAGjpHV6y20qwklWY2uhSXR0iG3yPuHNB5iSqCby8Da2xF9_sPNqRhr_OrQXV-osIF8lAMWjma6NsHD1D_-_VIVHs-I7N93nkQapfpZLudjwztYtlUjYNnhjuwtBb-yPEadLQT2gFP1oMaRHpDCuW0esrj1BCP5cRyJ-aC0D4I66w5LZjmbuQrhzM-3PFMCA6gG8OJeB5Er4vLnmxgvPs9mOwbawmsu-O-yYTWhHTumSN1WyheNgD_2lc3zfcowXTYQCYvbmFOOMwlWwIO6EyHa6p4AMMGL1JtyKsLMiXwMWO8zi1w5hQiXvdrB3oRzIIviDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/539939e159.mp4?token=R6AVhE6594_LP4pLMLSAGjpHV6y20qwklWY2uhSXR0iG3yPuHNB5iSqCby8Da2xF9_sPNqRhr_OrQXV-osIF8lAMWjma6NsHD1D_-_VIVHs-I7N93nkQapfpZLudjwztYtlUjYNnhjuwtBb-yPEadLQT2gFP1oMaRHpDCuW0esrj1BCP5cRyJ-aC0D4I66w5LZjmbuQrhzM-3PFMCA6gG8OJeB5Er4vLnmxgvPs9mOwbawmsu-O-yYTWhHTumSN1WyheNgD_2lc3zfcowXTYQCYvbmFOOMwlWwIO6EyHa6p4AMMGL1JtyKsLMiXwMWO8zi1w5hQiXvdrB3oRzIIviDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جامانده
🔹
رهبر شهید، دل‌های مردم را از گوشه‌گوشه ایران به هم گره می‌زند.
🔹
اگر از قافله عاشقان جا مانده‌اید، دلتان را به ما بسپارید؛ و اگر توفیق حضور دارید، به نیابت از جاماندگان قدم بردارید.
این پیوند، از دل‌ها آغاز می‌شود...
🖤
🔸
ویس خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/666612" target="_blank">📅 23:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666611">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b89806084.mp4?token=UUNklu4K1a_aavGiNV1hoEv80yFb-bMDKxp06q6bO8xU3TYeQIKNIBihuC1NybAUXZ7pFEisQYFy1HtZDOQzHziDhykHEkUAC7hXmN2TGoZcgEq8zZSP5rvdy1xnl1oqlDE2Q1JpLkRsGcv_Zoow_SQPdf9DYb9Ilvd4ydbw3OOSYNVIsQ9gfHiPsS3pXN4lzoMABnokBDFbkECwRlEg53kXy_z_cuaYRNhRWFcxaYPfwtqqFxpcNHkwr7fyFSscqxkE2I8p94tyTf0FowA-_jrfOFkbfYmf9eYq0nOWhcC7coC4pwCCiYy8dLvYCRc8TYcaiIpdot4-6TgzObheoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b89806084.mp4?token=UUNklu4K1a_aavGiNV1hoEv80yFb-bMDKxp06q6bO8xU3TYeQIKNIBihuC1NybAUXZ7pFEisQYFy1HtZDOQzHziDhykHEkUAC7hXmN2TGoZcgEq8zZSP5rvdy1xnl1oqlDE2Q1JpLkRsGcv_Zoow_SQPdf9DYb9Ilvd4ydbw3OOSYNVIsQ9gfHiPsS3pXN4lzoMABnokBDFbkECwRlEg53kXy_z_cuaYRNhRWFcxaYPfwtqqFxpcNHkwr7fyFSscqxkE2I8p94tyTf0FowA-_jrfOFkbfYmf9eYq0nOWhcC7coC4pwCCiYy8dLvYCRc8TYcaiIpdot4-6TgzObheoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همونی که براش نمردیم، آخر سر فدای ما شد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666611" target="_blank">📅 23:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666610">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/395e2222e3.mp4?token=JU-2kK7pgALGgeuyAX9YLcCtpdABZXW7IYKHhwyDr5UT4AOjsH2mInFoR7F6HKau6sqiqe3F65jifEscXBnb4yeT-VCJdj9TBG9J1GV3yn1-6igJKZa1g_NT9X5I69nQxilYgNN8gXoFiQ6bPVPTh2RK4epyKVS3mRxTtxHdl93oFCFNPzwsZHWKPnlw9IWQMBp8-ao_tDxF6BRu03-XgdzlefGEaCoy-1-v4S2iY7TmVLK73lnnQ2vOlQ5Rly1alqeYIBJn3hoofgt-FBIl1OxMsqhCNQ9C4SNme-cWi2SvBPcfu4_nbpjsVJ5rBMSY_S5xQ1FOVmMowc1i0j02uiGa0esRKuKFXStZz54at_5XmlU111hRkW99fXAsT0DpQd0UgQvggFVEpMFDOlqhPw7tw5Jve_VRV6ON571-K-iCvf95aSbYMd4_TzYeIuy7GCqVQLVfjreAesxBj5sJ6OQr3bi2v8PShRWnJ8qlabTZsubu9n-ZQo9Raa2QswvA4P3yFHYvXYVPtcPHx550OrBqFr-51EBzB8Hmj-b-yVJpMpQTu1hGnKqTv2NwQ3wlKWBVCPC3_aMTpK0FHXYo4DRUslk9ORBklOwMvZT5fRcM56e73oY20b98tsrfrR2U-J-JRgMoqol8hbX5GAMl32rRayESB0ti6j64lD9srSY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/395e2222e3.mp4?token=JU-2kK7pgALGgeuyAX9YLcCtpdABZXW7IYKHhwyDr5UT4AOjsH2mInFoR7F6HKau6sqiqe3F65jifEscXBnb4yeT-VCJdj9TBG9J1GV3yn1-6igJKZa1g_NT9X5I69nQxilYgNN8gXoFiQ6bPVPTh2RK4epyKVS3mRxTtxHdl93oFCFNPzwsZHWKPnlw9IWQMBp8-ao_tDxF6BRu03-XgdzlefGEaCoy-1-v4S2iY7TmVLK73lnnQ2vOlQ5Rly1alqeYIBJn3hoofgt-FBIl1OxMsqhCNQ9C4SNme-cWi2SvBPcfu4_nbpjsVJ5rBMSY_S5xQ1FOVmMowc1i0j02uiGa0esRKuKFXStZz54at_5XmlU111hRkW99fXAsT0DpQd0UgQvggFVEpMFDOlqhPw7tw5Jve_VRV6ON571-K-iCvf95aSbYMd4_TzYeIuy7GCqVQLVfjreAesxBj5sJ6OQr3bi2v8PShRWnJ8qlabTZsubu9n-ZQo9Raa2QswvA4P3yFHYvXYVPtcPHx550OrBqFr-51EBzB8Hmj-b-yVJpMpQTu1hGnKqTv2NwQ3wlKWBVCPC3_aMTpK0FHXYo4DRUslk9ORBklOwMvZT5fRcM56e73oY20b98tsrfrR2U-J-JRgMoqol8hbX5GAMl32rRayESB0ti6j64lD9srSY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاج حسین یکتا: وسط جنگ جهانی در میانه بازی‌های جام جهانی، در ایران یک اتفاق تمدنی در حال رقم خوردن هست/ در مصلای امام خمینی یک اتفاق الهی در حال رخ دادن است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/666610" target="_blank">📅 23:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666609">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e9a8d5f77.mp4?token=ZseJsZBG9qCvQBLVbVaXnq-35ek8MiZ-x9yaxjdfpQ1wn3cXB_Hs6w_NXz3Qg-3utlj_ekbcvd_LqJwyrOturt55JHi_3ItM0wbyprd-q2EZzrpQ4JZNgeGa_M0KQYrIg8CkGhrzZoZpY-_iwr_kFtzWdse4_zi-CMH9iQALlnbKJjOo6LbM5v29EKZaiBg4r32I1XHWNKyggxvhFnEhSash0TQxIvNeUDzCqRup1VZv8ApCyGnK7SREzpbiiGrQZXOm8lKMDZzlvmzvGHnOC2dt9ZuiRh2DAy0jzzb7Js1hCbTIECzEByftjaFwPjdrhW9Hd9JOiwZ-4pnpIjQGoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e9a8d5f77.mp4?token=ZseJsZBG9qCvQBLVbVaXnq-35ek8MiZ-x9yaxjdfpQ1wn3cXB_Hs6w_NXz3Qg-3utlj_ekbcvd_LqJwyrOturt55JHi_3ItM0wbyprd-q2EZzrpQ4JZNgeGa_M0KQYrIg8CkGhrzZoZpY-_iwr_kFtzWdse4_zi-CMH9iQALlnbKJjOo6LbM5v29EKZaiBg4r32I1XHWNKyggxvhFnEhSash0TQxIvNeUDzCqRup1VZv8ApCyGnK7SREzpbiiGrQZXOm8lKMDZzlvmzvGHnOC2dt9ZuiRh2DAy0jzzb7Js1hCbTIECzEByftjaFwPjdrhW9Hd9JOiwZ-4pnpIjQGoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ای ترامپ این پیام یک نوجوان ایرانی است به تو:
داغ آقایمان را به دل‌ها گذاشتی؛ انتقام خونش را می‌گیریم
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/666609" target="_blank">📅 23:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666608">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/174a13c993.mp4?token=JTb4y79AJ1KyQEtznrwGDbvf48S0YcwZYmYpDqYBkkh8TodMaaAw5W2m_yZd_tNx3LnBCRQV_XiLg546Ly8gXumDxzHSzubxkE2XF3QOC_AlUfI_GoTOTPKqQutWZ8lsb3QyW3BOdLfzeWjzPC7QaDF4KtW-bi_yFPE_PhkV_ANHKa5Ji5taDCMOt0V8KAAQah38_YbieG08s7QmU22b1eL767LQEE_R9bLbj8g8B2V1fsK0zCK3kaqBJXLgIl_PDg8Gkr0ycL-mG0t39V_VEldp3Fh8qdTUtyP38QXtHBcBUu3tHzzsht8oTpy-9zGJqg8PJzBQ_zpgYEY3GoErRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/174a13c993.mp4?token=JTb4y79AJ1KyQEtznrwGDbvf48S0YcwZYmYpDqYBkkh8TodMaaAw5W2m_yZd_tNx3LnBCRQV_XiLg546Ly8gXumDxzHSzubxkE2XF3QOC_AlUfI_GoTOTPKqQutWZ8lsb3QyW3BOdLfzeWjzPC7QaDF4KtW-bi_yFPE_PhkV_ANHKa5Ji5taDCMOt0V8KAAQah38_YbieG08s7QmU22b1eL767LQEE_R9bLbj8g8B2V1fsK0zCK3kaqBJXLgIl_PDg8Gkr0ycL-mG0t39V_VEldp3Fh8qdTUtyP38QXtHBcBUu3tHzzsht8oTpy-9zGJqg8PJzBQ_zpgYEY3GoErRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن محمدی‌پناه، مداح نماهنگ «باید برخاست»: ما مدیون آقا هستیم و نتوانستیم حق ایشان را ادا کنیم
🔹
این داغ هرگز در دل ما سرد نخواهد شد و سوخت موشک ما برای حرکت‌های آینده می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/666608" target="_blank">📅 22:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666607">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b464301f47.mp4?token=CXW-HzZwizfS231FitrIdPchjOUpUZ64WkuRmraF9TqRU86Q47cbOAHlDNTa6fZvK3AQNnKka4y8WOXHbcD1HfRMUHnIt-duxJavKxUrP7GYym02gv7iDTvemev3gUbnwOvMSZH7j0x_XAl0gbOe4JvLivzmLzKUVxteUudBJXDjoCGNVZhlyugG2DZZ46RthmV23Nl6hGn3MrURKRx3GxYeaNKDUtqLZl2T4gwLIYh6orundN2qH5zK5deNkikqRvtB0CnADXIl5XmS06Gxr1tiGGXJYdZDWeZgm8HhVxFedSE2rxb7-w7EcMHXKSOMcvAwOok2xotAdStLl3niZDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b464301f47.mp4?token=CXW-HzZwizfS231FitrIdPchjOUpUZ64WkuRmraF9TqRU86Q47cbOAHlDNTa6fZvK3AQNnKka4y8WOXHbcD1HfRMUHnIt-duxJavKxUrP7GYym02gv7iDTvemev3gUbnwOvMSZH7j0x_XAl0gbOe4JvLivzmLzKUVxteUudBJXDjoCGNVZhlyugG2DZZ46RthmV23Nl6hGn3MrURKRx3GxYeaNKDUtqLZl2T4gwLIYh6orundN2qH5zK5deNkikqRvtB0CnADXIl5XmS06Gxr1tiGGXJYdZDWeZgm8HhVxFedSE2rxb7-w7EcMHXKSOMcvAwOok2xotAdStLl3niZDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقاجان بانی این روضه شمایید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/666607" target="_blank">📅 22:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666606">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
اشعار حماسی محمدرضا طهماسبی در مصلی امام خمینی(ره)
🔹
از بامداد امروز تاکنون ده‌ها شاعر فارسی زبان از ایران و چند کشور دیگر اشعار خود در رثای رهبر شهید انقلاب را در رویداد ادبی آخرین دیدار خوانده‌اند.
🔹
در این محفل ادبی که از بامداد امروز در شبستان مصلی امام خمینی برقرار است، ۲۰۰ شاعر در ۴۸ ساعت بی‌وقفه برای رهبر انقلاب شعر می‌خوانند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/666606" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666605">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJE3nbuJlXs6XNtq471E3_fFNJNvNTJioyO3pNtZ-mI7vk6XrFETO4GrCku98oZ810ssrrX0NxKJbJPBFArUKcUI-5Q-Q6w9qaf_CdpgxwMgXhLiQSwmcQFpccO75HLNtqaVwyGtd6nC286Hu8d-J6YHwOB3OIe3Ula3sDq_UX0UC0an0vZYuQYWNUIpN4lFrjavTgzUIU_eBXkvyyyX42_cpNuIxbgGjVqzInrx3J8KpfsTsx8l_Cobr3IfYEy63HfneSgoQLxMUSRDznNZVeaC8mAcj30hC0WG10cmoRlhg9MtUqty6TXQdd0-Bu1SgAs1Er83Hn1lq9zX1DmOvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار نخستین‌بار
تصویری از شهید دکتر مصباح‌الهدی باقری در کنار رهبر شهید انقلاب اسلامی در حرم مطهر رضوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/666605" target="_blank">📅 22:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666604">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cq9pSj4N7J2DOOVHzSJR9o7-P2JNoxdPKWJOHz5_b00FnBUa-3IXZlrHY3PUQ3L1Y4mvux9W2AnGlSqjlO4fdRsM3dLOH6e_FzlW7rnNg4x7b7vmjnFPuziH4U8amn9-NKa4FyKoVN-ajB9Z2CTDjNKG5HM3qdx13HESbmDOI0B0qTJ6DVZU92d1wJgv1Di1lmlsES_-UX0HR-xXwbe_8wCiO1wmXaWb8C48RtX8m1f_dBchTIKPePIKj0ywAGPZ_hIbO6VR3aF4w33tAZmuhyl26mdx8fWhfyx5iym6HOjr1qAJ1iPnmuilUtpoR4y6llMBr797i9RtgVDoAsw2KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مچ‌بند سرخ، نماد عهدی است که فراموش نمی‌شود
🔹
با این نشان در مراسم تشییع حضور یابیم.
🔹
تا پیام عدالت‌خواهی و ایستادگی را به نمایش بگذاریم. #مچ‌بند_سرخ
🔹
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/666604" target="_blank">📅 22:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666603">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiKRoO3g-jpRx8TbPQ3CRvaPKAgloy1of_YUo_iKvdyPAseladpSVXWHJGCq-Aqnq-bFoqKU-MVZm9XBodsRZ0IRQDmGIBPE9IVs1LCzhyWnVDGNcS1YYM4gh6aMqR1OqiwOYkem7mLDA2eZu1l7S4_98V2jlK-TpFMcJFKCBBOpIB31Io6IehV5FDMBtgvmm01-2piUjv5p90aRXDw6c3XmGdGpVNKhItMrKmF4f_kkL47ecLX2nB_RE2AIUcnPeaRZR1RScNZVbmbQZmhYhqZh5N2xQ6_Pado1RzZS7iUW7nxZQpKgu3yTprL6gmwkQavJigV_6uURYboHxRvsiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در آغوش ایران
🔹
تهران امروز صحنه یکی از ماندگارترین بدرقه‌های تاریخ ایران است. از نخستین ساعات بامداد، مصلی تهران میزبان خیل عظیم مردمی شد که برای وداع با رهبر شهید انقلاب اسلامی گرد هم آمده‌اند. این حضور، تنها به مردم ایران محدود نیست؛ مهمانانی از کشورهای مختلف نیز خود را به این مراسم رسانده‌اند تا در این آیین سوگواری سهیم باشند. زن و مرد، پیر و جوان، در کنار یکدیگر پیکر مردی را بدرقه می‌کنند که نماد مقاومت، ایستادگی و پایداری به شمار می‌رود. امروز خیابان‌های تهران در میان اشک، نوحه و شعار، روایتگر پیوند عمیق مردم با رهبر شهید خود است؛ وداعی که تنها بدرقه یک شخصیت نیست، بلکه تجدید عهد با آرمان‌های اوست. تصویر ماندگار این روزها، همبستگی و حضور مردمی را در حافظه تاریخ ثبت خواهد کرد.
🔹
هفتصدونودویکمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/666603" target="_blank">📅 22:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666602">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
حکم سنگین دادگاه کویت برای یک شهروند کویتی به اتهام ارتباط با حزب‌الله لبنان
🔹
دادگاه کویت، یک شهروند کویتی را به اتهام ارتباط با حزب‌الله لبنان به ۱۰ سال حبس محکوم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/666602" target="_blank">📅 22:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666600">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f415f88f0.mp4?token=sVhpXXBLvXZtkxJWYDp71q5N6gZHewjzSxmkcsB1Y7jvirF9HW0YupYH_UCpaKEpzY56hvKE6JQ9KxZn8hZSJexO9T6hkgo22vdsigMh_6VYLVkrIvFwYsbCeFwpPW6z0jsaKWjHeVEyDRQI8-EGKMlkiQJUhMA0OlGlGgrxGT2yL95suxpG8pVajNKGf7ntbLszPpR8xmdwy6RgrbqKmz9t-orxEpvlZxLkp5aRLhmUyg4G1ClkwgDgxwGeFTvdquqUSIbDISVFowALnhwUVdhvSIXYzuoN_sLXa1L4PYXxyHVmSxf5-pDzZJfolLgyYtjqA1rmLl9NuuWY1-_crw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f415f88f0.mp4?token=sVhpXXBLvXZtkxJWYDp71q5N6gZHewjzSxmkcsB1Y7jvirF9HW0YupYH_UCpaKEpzY56hvKE6JQ9KxZn8hZSJexO9T6hkgo22vdsigMh_6VYLVkrIvFwYsbCeFwpPW6z0jsaKWjHeVEyDRQI8-EGKMlkiQJUhMA0OlGlGgrxGT2yL95suxpG8pVajNKGf7ntbLszPpR8xmdwy6RgrbqKmz9t-orxEpvlZxLkp5aRLhmUyg4G1ClkwgDgxwGeFTvdquqUSIbDISVFowALnhwUVdhvSIXYzuoN_sLXa1L4PYXxyHVmSxf5-pDzZJfolLgyYtjqA1rmLl9NuuWY1-_crw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراکش مقتدرانه نسخه کانادای میزبان را پیچید؛ گل سوم مراکش توسط سوفیان رحیمی در دقیقه ۸+۹۰
🇨🇦
0️⃣
🏆
3️⃣
🇲🇦
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/666600" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666599">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bl6k_n7vA0mLG05QUPBm4YeqEe0KUwavFYlZhmAtX4z5WKyI4nHcpyDesPmRF8gEvNAE1XtdMhUoPMJU6MpecUdc7Onp7JHENgCkHLeuy-v19EBtKvuSfDRnTNuYOtB2u2AtQEXytizZYK4BrOcO35SP2zYqS3uNd8d2JEY-jeNyObrheFKKu23q5bVf_iIc5Ags9qnBjwysOfX8n5BFSdG6DEsGwH2sDxp3vLlp8_mP2CRFQq_Rbq2ZXBiWpdim7yGivCG8EhsDNbro4N7waWS_TcIa4TLdIiLnDzCOvnDPBlefZq8QiTzdWUAsuPdm0xo0lLI74EbOQRLBcHn72w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راه‌حل امام برای خلاصی یافتن از ترس‌ها
🔹
امام عليه السلام مى‌فرمايد: «هنگامى كه از چيزى مى‌ترسى خود را در آن بيفكن؛ زیرا سختى پرهيز از آن از آنچه مى‌ترسى بيشتر است». ترس اغلب زاییدهٔ خیال است. انسان تا وقتی از چیزی فرار می‌کند در اضطراب می‌ماند؛ اما وقتی…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666599" target="_blank">📅 22:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666598">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
یدیعوت آحارونوت به نقل از منابع اسرائیلی: تاکنون هیچ‌گونه ترتیبی برای برگزاری دیدار میان نتانیاهو و ترامپ انجام نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/666598" target="_blank">📅 22:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666597">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2-m97smM8CmAll730-yXQzspZyPvH-7h2ILaFDvSGQ95ZYt2A4kWk2xeLvncTtk3TVjlwsjTOLXaYp3cw1Uw0lzN8ooXxJ4_I4qLm_iub-lHN7BA6YhCJRuSrhOumdEjvy_oc4ftKPTfzwcYMqYg6yjonxTHEKyKBiXfCbTWdY5Zj6dJR9TGtj1LgU28scYWtRep0cl8aHNOo-QUQEQoyEhFOSCogVmmouzGD4ZtL8Fg4F91tJUo1l9kVRlDPXimI7H4nObdXM0TYQgLa_V_wXQCR1e3xPlPU5qF4rD6-YefdAa9cSUyof48rma2zmqKMu2Vd3wJ6kzmaOY4Z-IVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قدردانی عراقچی از نمایندگان کشورهای شرکت‌کننده در مراسم بزرگداشت رهبر شهید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/666597" target="_blank">📅 22:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666596">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
سخنگوی ستاد بدرقه: مراسم وداع با پیکر رهبر شهید انقلاب امشب تا نماز صبح ادامه پیدا خواهد کرد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666596" target="_blank">📅 22:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666594">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
شب نورانی مصلا در هنگام مداحی حسین طاهری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666594" target="_blank">📅 22:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666593">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c52c1e47d.mp4?token=QLSjloMXPyZ4gyuFX5myHr_JJbUNuwTMJxRt5uFGawEhUY_qN7XIKCO1YuRY9JXdPYd4Puw-dv7Xm4M4U8jj2r3po67uGHdsH1hkM8qlzDP0M_Yf1J60b3RRahaE9kgG7g_fxj5TouOwpmjfrTZ6_arC8f2wsJMKtcR9SkjadRB4WE5lGPOssQK7SqebAmnXd8CJ3BPk0e9J7e9_CbDA7xn9Cld2awyvwOzhDXr11YAH0_m1SzNjJU3NAGxVR7eJELZ-q_Et3iuTvJVnrIqp6olrWYd6hv0GnMhnBNcpFiZqMrBjYb1Ag8lAZ94t9zfBR4XQgjFEMBPPabiui2F3SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c52c1e47d.mp4?token=QLSjloMXPyZ4gyuFX5myHr_JJbUNuwTMJxRt5uFGawEhUY_qN7XIKCO1YuRY9JXdPYd4Puw-dv7Xm4M4U8jj2r3po67uGHdsH1hkM8qlzDP0M_Yf1J60b3RRahaE9kgG7g_fxj5TouOwpmjfrTZ6_arC8f2wsJMKtcR9SkjadRB4WE5lGPOssQK7SqebAmnXd8CJ3BPk0e9J7e9_CbDA7xn9Cld2awyvwOzhDXr11YAH0_m1SzNjJU3NAGxVR7eJELZ-q_Et3iuTvJVnrIqp6olrWYd6hv0GnMhnBNcpFiZqMrBjYb1Ag8lAZ94t9zfBR4XQgjFEMBPPabiui2F3SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضد حملۀ برق‌آسا
،
گل دوم مراکش به کانادا توسط اوناحی
🇨🇦
0️⃣
🏆
2️⃣
🇲🇦
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/666593" target="_blank">📅 22:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666592">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ca5Y5b10rQWGIG2rPbt2hTgotktq5RWPozw8Huk6wwyYuepimphsz1LZjEu-9UlTRXT2W0VHm9-mb5HqEtf7N9LaSOY6Cfc9kl5nFx0EPxIOR6Ect0fKBC7w1Sfqp_VtJnQm6moFQ9TchMDQawYOlQuKwF3tMd3S680ePjxjwaM6sCpKlty8i4NhAfd5-03KKqXSJg-P7Jxz5SwS8J7pSS_BLUX7HlJdFgrTiF1qVHXMLq4F-0323Ezt8VWLFjmDQHXCOuzf5LMTp_M5zv_GhLu_rKdZz1fqD9Oc8T5wG4a0oPWfemTYlNc4cfzVkhigAARGCF4zt0NcWYG-4BF7fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/akhbarefori/666592" target="_blank">📅 22:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666591">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36cc42a03c.mp4?token=KWRGteJBvAw2GaFDWR80ZxQnEI8I_B9qPeIEz0yLpCrTmQnVPxiHJovei-UlVgNLauB1yDo-1zdC4FVj48a7vUbPtWdFoSaLcUyB9qGAvQJzd25d0DYXjQ8hlCabwLGjcFS-1WIqyVEqNRdOHZrMQnAWHeuUz_dkm-PEDGg3EUGdoNcuFNEeQNq8p1zBQ88iJMpQ22LCt64yBcqpw2-F2VlppbLkB-F9a81J6gnE3p0P8Y2NnbiKAApenGD3sf4H_8a_z1-Gp0-SB5OfwBDJXOmsHC3icogKhpmjkt8U18aFCxBqLC6TfGgH7AzRmA15XcN8pcAyjWfyCxhu7aczjHMmGnL7EbvVv_YR6H90M9hIs9VgVvnNs8x_UY6bO_zdKoMYdWiy_qyIkFfQ1jIHNCq98c8n8-hEH_2w8LmGsgiyBbac96qBmxkeNxNKR56J_IogWQD5Qchh6zXFo9falCb6Bnltknm0Dfj4cFdip509JJtCTvYaywTNE7bMDOXORoIufVvG9TR4Hl7ng3R8DYK1x_GrPY9gXFIZugKCxdRGRngUH82qF5QHA6znInjh3ixviwPW6nT4UBdq-soKyZWoJYd69JTfy5-QjfHM5REnQVCbby5CgEKxoC_LnwlIPYmjPYmMX3SjD53ddhDaOWeej_H33uel5NLPBZ_cApQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36cc42a03c.mp4?token=KWRGteJBvAw2GaFDWR80ZxQnEI8I_B9qPeIEz0yLpCrTmQnVPxiHJovei-UlVgNLauB1yDo-1zdC4FVj48a7vUbPtWdFoSaLcUyB9qGAvQJzd25d0DYXjQ8hlCabwLGjcFS-1WIqyVEqNRdOHZrMQnAWHeuUz_dkm-PEDGg3EUGdoNcuFNEeQNq8p1zBQ88iJMpQ22LCt64yBcqpw2-F2VlppbLkB-F9a81J6gnE3p0P8Y2NnbiKAApenGD3sf4H_8a_z1-Gp0-SB5OfwBDJXOmsHC3icogKhpmjkt8U18aFCxBqLC6TfGgH7AzRmA15XcN8pcAyjWfyCxhu7aczjHMmGnL7EbvVv_YR6H90M9hIs9VgVvnNs8x_UY6bO_zdKoMYdWiy_qyIkFfQ1jIHNCq98c8n8-hEH_2w8LmGsgiyBbac96qBmxkeNxNKR56J_IogWQD5Qchh6zXFo9falCb6Bnltknm0Dfj4cFdip509JJtCTvYaywTNE7bMDOXORoIufVvG9TR4Hl7ng3R8DYK1x_GrPY9gXFIZugKCxdRGRngUH82qF5QHA6znInjh3ixviwPW6nT4UBdq-soKyZWoJYd69JTfy5-QjfHM5REnQVCbby5CgEKxoC_LnwlIPYmjPYmMX3SjD53ddhDaOWeej_H33uel5NLPBZ_cApQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به رهبر شهید ایران سلام / سایه سیدمجتبی مستدام
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/666591" target="_blank">📅 22:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666590">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/0764895667.mp4?token=GXh5oguN4VB61HgPXbMnKe2FGv9jg9wAxL1kIwO_ISz5A5nJJrVRy_V9SUAIJ1Y0A8q5uVyZ6t-jQUsDLM4C8rrA1ib37ayX-Vpez70xhXizmBYl7suEziiiGTOZIsH6PyzfRoAnKyZdJIhLbmAaLsc2_AB1ifNM7GZZb7v3Iq9hW5FkptzJLdHIcKKn5PEABLRF-dJTDSUlvDKJgUEYZGAdRXcDmQ-ikiHSfBp6Th_fyoGGWOnZUsenQbf9Al_7R7hpIO9Fho4TIUUHzEOd-e2cMbnzF-0agu3FJy47VaQBfezZhfE6IkcQZKJ1b4r4NeTCgj2Whf5FUKjIHdTksw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/0764895667.mp4?token=GXh5oguN4VB61HgPXbMnKe2FGv9jg9wAxL1kIwO_ISz5A5nJJrVRy_V9SUAIJ1Y0A8q5uVyZ6t-jQUsDLM4C8rrA1ib37ayX-Vpez70xhXizmBYl7suEziiiGTOZIsH6PyzfRoAnKyZdJIhLbmAaLsc2_AB1ifNM7GZZb7v3Iq9hW5FkptzJLdHIcKKn5PEABLRF-dJTDSUlvDKJgUEYZGAdRXcDmQ-ikiHSfBp6Th_fyoGGWOnZUsenQbf9Al_7R7hpIO9Fho4TIUUHzEOd-e2cMbnzF-0agu3FJy47VaQBfezZhfE6IkcQZKJ1b4r4NeTCgj2Whf5FUKjIHdTksw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار تانکر سوخت در آمریکا
🔹
این انفجار حوالی ظهر به وقت محلی رخ داده و علت آن نقض فنی اعلام شده است.
🔹
این حادثه منجر به قطع برق چندین خانه در منطقه شد. پلیس از مردم خواست تا از ورود به این منطقه خودداری کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/666590" target="_blank">📅 22:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666586">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UluqC2xGBrY9GmqIGeK2umximGchPreCgYgVc6NuTs2muz2oFHcYIbjrefD6gefLwsLz1cNuCGA-K9HLtS0nXirdk9nWKXIeZKmwwzqvmTDmy5kJ6dClTk5M85IhJLyBkBeISozT6OJY6GZfbCHiAHkACJ0UVH2_-WpfNsTJ9Ii31N1Ry-JGnlKnxnmQok0u-J5X3M-oZlhL6o7FbGRhbnXGTSe1sIJzKKfPo2OIaLhfTQ0lTgL-dGGb3gwKcd49BX9f8ujSxDhaqQam4k93ysPdF6WbcsZYxHoFllVH4ymviQx9fJaVG2I21D8xb9QlNuOkGICEzSYS-qYptgvEhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lm2ud66OhaZlcPTB7cqR17Lmd9St0Z8HUYhJjFUhubJhS1cn_1S_mKVmFkznyrASCj656UBbmRXT0kJZWSAjwIGV6jr_hIvFZ8YGZy6e-fmcnHGOXPvXJnyhyABVJ33nXAOZmqwwOu6fTUU1tLCfsR_AMjsrNl34lxOIV2mGIt-lrA8mPSt4TmYaQBAH8ViJe6dVKhCV65BPYMTMhJvmhZUxgXo53JY1Ee_6W_rVLBQqICAjLU7YFYCtQwg2tf8CdQUqWosojLHOVopq5OTRYmjlNH2zdklphRKIQLAX4jLARkq6ScXREFLitniQdKo1JFhTo3e7SZW72G4x2jDRsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s2XuSozGut7Xyb3v7ajrls7qs8VfMWOz8IucLL6yoPQqQA_Nl9jCUQft2238-lq6L60jh3MXZ6UWtRXB0MxenTPXe7hW2XkxObu2b7HN1komFwz0WPlE5fuCcqY6QiIUO2OiTITkzQLZwWBHKIJCWrZ9x970qNcdSK4u9uaTrtEuynwc4Pes9WXJmVUrbPzpbK0upR6aw56qfCtFAqxx0CQV6gVklXYHpE6tDsw6H5sP6INNBJmdUFaoL6OcDCKSr0l4Uyt5PBzbB19VDowl2dnGeI3BGjMcWK14dTXv014pydKN-o0LYUbG0YI4IFkpIW75pmwI0otW39zfb-Y9wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D61d7ASC9n5WH6eX_Ccw9lVMIR-y1B7HHRvGX_bQLKbh6tCR6YVjXM6LZROJrcbf6B55CcY4x1iuPykmDf7DC01TdllTHwt9NXbTR-MVW5T8ROj-yW3pXDpb34Mj__tAlWbwcgaZo1Z_0bvguP0nYb9szA-6aGDe8qivoUxuuFqbFh2XPmbvylF0VwJB_4ITP1e_1t17vp10JlX-qeLY-AW6UaZWPLQh7wOEFwKOf1VrR24wMEQbH5B9---CR2S1SxsCOkj3hNLRdVLPwtzKzpfQHQKqYeXLpnHM6pjAeedRxaVKg7Jz6JQ1NoVKj7cDhFi1hQlAEfp5LJf5N5ISJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
طرح‌هایی در راستای راه اندازی موج خونخواهی رهبر شهید
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/666586" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666585">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4722481f4.mp4?token=NHH8c_u0NBfWch8ctqmyj0tdD8zc9bkoDb5NGKgaZWbAZyW3M-vJs7x8GVeGcwJd9B9WyqZ7ddT_VMY9IHOHDz_DFjOy4GBv2UDPWiGSvJ8wVB4lbXrZewKi4IJPPbnOScPhiBRUwh_n5sftVZRLJWnu6gKVe3cNmWy_-F983-G8UYN4OGFNryRTiRAtQJe0gogcfbtt8ds6wwxwTFutOUaiePnvcpf4S4-v5XXrN1nBykokg0YgpWGWiOnG18RZX0DvEqBtjOJrMBcl0nqjm3HJpJy0YU6QpG_doJbWl0CkImPnaiFEB5WAQVgs8M6cQBvqa8uRPKIWnQF03zv_xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4722481f4.mp4?token=NHH8c_u0NBfWch8ctqmyj0tdD8zc9bkoDb5NGKgaZWbAZyW3M-vJs7x8GVeGcwJd9B9WyqZ7ddT_VMY9IHOHDz_DFjOy4GBv2UDPWiGSvJ8wVB4lbXrZewKi4IJPPbnOScPhiBRUwh_n5sftVZRLJWnu6gKVe3cNmWy_-F983-G8UYN4OGFNryRTiRAtQJe0gogcfbtt8ds6wwxwTFutOUaiePnvcpf4S4-v5XXrN1nBykokg0YgpWGWiOnG18RZX0DvEqBtjOJrMBcl0nqjm3HJpJy0YU6QpG_doJbWl0CkImPnaiFEB5WAQVgs8M6cQBvqa8uRPKIWnQF03zv_xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جکسون هینکل، فعال رسانه‌ای مطرح آمریکایی: سید علی خامنه‌ای در مقابل هیولایی به نام آمریکا ایستاد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/666585" target="_blank">📅 22:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666584">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815c9ff5ee.mp4?token=nNyVOxqrVmI4oEwFvPQuSrvkJdWRZJI8QdEnW38PuGnXsNz5vyvo7ReuBOhDbPwjq52Q1WP9GApfR5foOw-oGDKLWfIYlTGcE58TDPWyXdzuIq6R6do6BjtgUFRIv-aKvUwqr_q6BT6c-VChSCwYEfkJSyfbJ0xzNXV34zjAnwewjfGhxkFRokGiOCtTbCbzmY8Lopb6wXSNhxSsEo149w_qADX0UROiaLBGk0n-yad4LK-2MtBm2IXfGknhJhQQQd11XIanr3dGfCzAMEVByCXQkKxPuSSO-shyAr-c6f_Grj0LzGOpzfWa9BVTjp-lVnEy76564Gk1Cs0K9NTqrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815c9ff5ee.mp4?token=nNyVOxqrVmI4oEwFvPQuSrvkJdWRZJI8QdEnW38PuGnXsNz5vyvo7ReuBOhDbPwjq52Q1WP9GApfR5foOw-oGDKLWfIYlTGcE58TDPWyXdzuIq6R6do6BjtgUFRIv-aKvUwqr_q6BT6c-VChSCwYEfkJSyfbJ0xzNXV34zjAnwewjfGhxkFRokGiOCtTbCbzmY8Lopb6wXSNhxSsEo149w_qADX0UROiaLBGk0n-yad4LK-2MtBm2IXfGknhJhQQQd11XIanr3dGfCzAMEVByCXQkKxPuSSO-shyAr-c6f_Grj0LzGOpzfWa9BVTjp-lVnEy76564Gk1Cs0K9NTqrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار مردم در مصلای تهران: ما همه خون‌خواه پدر، گوش به فرمان پسر
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/666584" target="_blank">📅 22:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666583">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
استان میسان عراق چهارشنبه و پنجشنبه را تعطیل اعلام کرد
🔹
استاندار استان میسان عراق روز شنبه اعلام کرد که روزهای چهارشنبه و پنجشنبه آینده به مناسبت تشییع پیکر حضرت آیت‌الله خامنه‌ای در عراق تعطیل خواهد بود.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/666583" target="_blank">📅 22:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666582">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
تأکید عراقچی بر ضرورت خروج کامل صهیونیست‌ها از لبنان
🔹
وزیر امور خارجه امروز در دیدار عضو هیأت رئیسه جنبش امل با تمجید از پایداری و استقامت مردم لبنان در برابر تجاوز نظامی و تهدیدهای رژیم صهیونیستی، بر موضع قاطع ایران مبنی بر ضرورت پایان قطعی تجاوزات این رژیم و خروج کامل اشغالگران از لبنان تأکید کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/666582" target="_blank">📅 22:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666581">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/splcktFa8bjGSb6xchVx_-IB-n9CHQNTe_Bymc_DrZBPKgDt0Lp3NdKSZs73V1MQdnHEvfk0niW-K9RIf6gBo5DNx0ajRW_CVWF_mPAlotkUDpAjC0HG2vZlpSrV6kMs0171yfzus4-NaZtyB85SFX9bekSObJqgsjqg42WrhWfLtqXYg20yIkdBL4VAJjMm5TW8YtHUytcm8XZsNvsI4umMTZhofkaLYio6shlfJ4UPUWJeidOty2w44BBrHRUrtGgwbJCFqkd5GxVwBogy6ujRBGyCWyjVpBwG0cF0UUp4ymt2W7kOM1PpTR9VReFbMyZEpuLZJ8B9H2GY9WoKFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
هموطن گرامی در صورت
سرقت یا گم شدن
تلفن همراه،
امکان ثبت و پیگیری آن از طریق سامانه کشوری
همیاب24
در دسترس است.
اعلام سرقت از طریق لینک زیر
⤵️
https://hamyab24.ir/l/kbi
https://hamyab24.ir/l/kbi
سریعتر اقدام کنید؛ سرعت عمل در ا
علام مفقودی، 50 درصد احتمال بازگشت گوشی را افزایش می‌دهد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/666581" target="_blank">📅 22:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666580">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqbJYzzKRoikUmJH-iYrb6ikZzlklRHYg9XZHYGIC0JuLOJOWI46tFBvclmSU9o3i_eFqrJVOGEgYFDM8rpJPvjUluqtK6RQzHzfsuGMKbNfjJeEpyd8MR5ro6Ji2tt4YeqLMb0WyoI78iIfvQ_Cn8P5pq7XW8dZ7rTYGt-V-Gzq2kKrvhqW55eqSCmhZcPH_eIG1Jd01PIFYKvUgFokpmE7sDUFXRLon3WvWYoD4Zc5OJcnwJm2gYW9nFN9b0baT3spvualpfNNXh8anDU6NfxPdMY1q5mkke6b_fsTkhl5tofDsZJNnbTuSp320ypT7MePRwLtT6Nmy77ZesxKOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر شبکه خبری الجزیره از مراسم وداع با رهبر شهید انقلاب در مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/666580" target="_blank">📅 21:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666579">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
محاکمه یک ایرانی‌تبار در لهستان به خاطر انکار هلوکاست
رسانه لهستانی Notes from Poland:
🔹
دادستان‌ها در لهستان، یک شهروند آلمانی متولد ایران را به دلیل اظهارات انکارآمیز درباره هولوکاست تحت پیگرد قانونی قرار دادند.
🔹
او سپس این اظهارات را در یک ویدیوی آنلاین منتشر کرد. در صورت محکومیت، او تا سه سال زندان محکوم خواهد شد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/666579" target="_blank">📅 21:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666578">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حضور رهبران تاریخی مقاومت در مراسم وداع قائد شهید امت
🔹
از امام موسی‌ صدر تا نلسون ماندلا و.....
آزادگان عالم در خیمه حسین‌اند
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666578" target="_blank">📅 21:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666577">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f8803cf1b.mp4?token=nSrqFcXr8gQ-9YTpIZiz0bjZwjT8BXf3qprR5XUkYESAF_JjPOkpR_tMzYtQyvSRmEPTjMZJNLLAideKZmCVAQmp7Wa_3UEoOGxczkd9_VnCS6BYPnFMQTf4wyVdf9bArjUm1oWQ0jQh53Fu5LqaGHaIARQVP_mTiJ_UWQ2BV_jnAa0Vy9xeYpF8pD4cLqch46sSUgQ_sGt2OEzPIjRuZinAc31Iwt67JdWz8__F0UfYtzbzNo0aUAQFfHA0pKNewvBfkZgvHzcC6QiEEP7ev3gnkSzn248q6OHINybL9z3cGSnsxQk8hINtRpSn20cRNX5tzDb7PVDkxeLIh5319w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f8803cf1b.mp4?token=nSrqFcXr8gQ-9YTpIZiz0bjZwjT8BXf3qprR5XUkYESAF_JjPOkpR_tMzYtQyvSRmEPTjMZJNLLAideKZmCVAQmp7Wa_3UEoOGxczkd9_VnCS6BYPnFMQTf4wyVdf9bArjUm1oWQ0jQh53Fu5LqaGHaIARQVP_mTiJ_UWQ2BV_jnAa0Vy9xeYpF8pD4cLqch46sSUgQ_sGt2OEzPIjRuZinAc31Iwt67JdWz8__F0UfYtzbzNo0aUAQFfHA0pKNewvBfkZgvHzcC6QiEEP7ev3gnkSzn248q6OHINybL9z3cGSnsxQk8hINtRpSn20cRNX5tzDb7PVDkxeLIh5319w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول مراکش به کانادا توسط اوناحی
🇨🇦
0️⃣
🏆
1️⃣
🇲🇦
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/666577" target="_blank">📅 21:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666576">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5762c89eb4.mp4?token=KBUdz4Z0BMtXGF918y24OCDgtkOAGbHAsGYFHru6SIC9sfIYOZQJrR8spZGau2v9jsRZhsp8vj0JI2uGtq3HQdjJkeMIVUoHG6IuppXH-Je_AdKToRNVWdORA9eOt0FK33HQH9dniXloSZBtpn-86a6USR7OLolFL2Flz7hZ8bkq7dFJHCBFG-GBQRYkwVFFJchZTGuZ73QSjX5fv_Yi5AFQmobRgdpYASI_rUgXswKew2rUEp76Bltr-YGy5UJEw41sMhZW8VIT7l_ZbT62YZ4XMZJkGqMcewrVw8PxP45q2pHUjmJR4gvg6dMmwJC47R-1DU-5Xp9hOcH4-7LfaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5762c89eb4.mp4?token=KBUdz4Z0BMtXGF918y24OCDgtkOAGbHAsGYFHru6SIC9sfIYOZQJrR8spZGau2v9jsRZhsp8vj0JI2uGtq3HQdjJkeMIVUoHG6IuppXH-Je_AdKToRNVWdORA9eOt0FK33HQH9dniXloSZBtpn-86a6USR7OLolFL2Flz7hZ8bkq7dFJHCBFG-GBQRYkwVFFJchZTGuZ73QSjX5fv_Yi5AFQmobRgdpYASI_rUgXswKew2rUEp76Bltr-YGy5UJEw41sMhZW8VIT7l_ZbT62YZ4XMZJkGqMcewrVw8PxP45q2pHUjmJR4gvg6dMmwJC47R-1DU-5Xp9hOcH4-7LfaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دکتر حسن ابوالقاسمی: بمباران بیمارستان‌ها و کودک‌کشی‌ها و افتخار به آن توسط نتانیاهو نشان می‌دهد که دشمنان رهبر انقلاب چه کسانی هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/666576" target="_blank">📅 21:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666575">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2869806eb4.mp4?token=eYSs-GfVb0rza8uvVQM5TR92_7TQ9HSzCCf3JmEV-gk9eMNboI1aV8podfrjQnCuGbecWTedDHYagohiDayxPhnsPyppcBjMJWRmuWDdCOFyeKcX2kBRu4J9Pkg6ugbYMBtSyNHyRwrPmIwX-rlM1rRIY2Fud_GmgC4gd7FHDMbj30rbZ64ccEJCz_ZNOa7F5X76ZjaBCixig3J6vFkRCY5klvU6pF767EhR5fIeiGwh2N8GGgS_ljSxlHqyCbKPMDdbDXEOVU1g6yTggdwdYGsGhPg3l6dRSm388nw_-2R5PyBDKrgmq7V_xFXlVeiaN3tNSEoT3ZxV2mPSAmCL9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2869806eb4.mp4?token=eYSs-GfVb0rza8uvVQM5TR92_7TQ9HSzCCf3JmEV-gk9eMNboI1aV8podfrjQnCuGbecWTedDHYagohiDayxPhnsPyppcBjMJWRmuWDdCOFyeKcX2kBRu4J9Pkg6ugbYMBtSyNHyRwrPmIwX-rlM1rRIY2Fud_GmgC4gd7FHDMbj30rbZ64ccEJCz_ZNOa7F5X76ZjaBCixig3J6vFkRCY5klvU6pF767EhR5fIeiGwh2N8GGgS_ljSxlHqyCbKPMDdbDXEOVU1g6yTggdwdYGsGhPg3l6dRSm388nw_-2R5PyBDKrgmq7V_xFXlVeiaN3tNSEoT3ZxV2mPSAmCL9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخبر: ملت ایران عاشق رهبر و میهن خود است؛ مردم ایران خواهان انتقام بوده و خونخواه اصلی رهبر خود هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/666575" target="_blank">📅 21:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666574">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ممنوعیت پیش‌فروش خودروهای وارداتی در مناطق آزاد
🔹
دبیرخانه شورای‌عالی مناطق آزاد تجاری ـ صنعتی و ویژه اقتصادی، هرگونه پیش‌فروش خودروهای وارداتی در مناطق آزاد را ممنوع اعلام کرد و نسبت به فعالیت افراد و مجموعه‌هایی که با عنوان پیش‌فروش خودرو اقدام به جذب مشتری می‌کنند، هشدار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/666574" target="_blank">📅 21:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666573">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94b7c265df.mp4?token=tc0FKoxOdE4r9D1DRx7eW1AeEBTrXn_mGXl_Bp80nw_onZPxpvbOdYaI7bi9Zk_jEPD9F8VvleOfpmpS_xwCoV2JtPh7GesivK3TE5YG5m2hfgg97kyDjPUj2OholOZDtgm6sNlO4aNL1JQvjOtOh43yiYom58ITmxYiUact0X5a-uqMBSgeHlRzs7SmcX68yeCoVwIZZtyvLYBGuBT3Ml44Y_mfQKJJbl9w52VnsUYFH0na2ibWRo_CzS65_3zeJsl2ZykbiR7tQF5EwmeEQeFKfR7dH0aEc_uAawo0aiGea5UlVhj15lj6MKr4K7jTxJxtf_ItH4jEeEE9bWDikg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94b7c265df.mp4?token=tc0FKoxOdE4r9D1DRx7eW1AeEBTrXn_mGXl_Bp80nw_onZPxpvbOdYaI7bi9Zk_jEPD9F8VvleOfpmpS_xwCoV2JtPh7GesivK3TE5YG5m2hfgg97kyDjPUj2OholOZDtgm6sNlO4aNL1JQvjOtOh43yiYom58ITmxYiUact0X5a-uqMBSgeHlRzs7SmcX68yeCoVwIZZtyvLYBGuBT3Ml44Y_mfQKJJbl9w52VnsUYFH0na2ibWRo_CzS65_3zeJsl2ZykbiR7tQF5EwmeEQeFKfR7dH0aEc_uAawo0aiGea5UlVhj15lj6MKr4K7jTxJxtf_ItH4jEeEE9bWDikg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی ستاد بدرقه «آقای شهید ایران»: مراسم وداع با پیکر رهبر شهید انقلاب تا ساعت ۸ شب فردا در مصلی امام خمینی (ره) برگزار می‌شود
🔹
بدرقه آقای شهید ایران در خیابان دماوند بعنوان مسیر اصلی تا میدان امام حسین، میدان انقلاب، میدان آزادی و به سمت بزرگراه شهید لشکری صورت می‌گیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666573" target="_blank">📅 21:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666572">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55afbb1663.mp4?token=T2TBlwLXzWCfT7nOAjsJJeRI3jTwh8l7QMrxGNZKhSROc19bxsrEiLzq3YVSsPBDTHCF2OhWFM208l4vC6Zp-U8_O5fUuPcuDhb4xx__GF2thr9lZLXZ28yVlRiPOBP3hS9xdi1IER78NG6pAsZD9Dj8oqTAq64HrgITtGXnkvzNIeJrScC9cv6mRsrLsoxeFJgBppVkEgq50gf5k2ttmjILJ3NUx90CYmTQCuIRIl2T7f0jr0YlVyqYhT-N5JLgPYKSRUKOqFqG8hkXzPO2bGfZnaUkv1bPEtJnMDrVrURqdixtLRVvAQvdQehXIvO_KknHKiyUA6CvU-vsSwOyKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55afbb1663.mp4?token=T2TBlwLXzWCfT7nOAjsJJeRI3jTwh8l7QMrxGNZKhSROc19bxsrEiLzq3YVSsPBDTHCF2OhWFM208l4vC6Zp-U8_O5fUuPcuDhb4xx__GF2thr9lZLXZ28yVlRiPOBP3hS9xdi1IER78NG6pAsZD9Dj8oqTAq64HrgITtGXnkvzNIeJrScC9cv6mRsrLsoxeFJgBppVkEgq50gf5k2ttmjILJ3NUx90CYmTQCuIRIl2T7f0jr0YlVyqYhT-N5JLgPYKSRUKOqFqG8hkXzPO2bGfZnaUkv1bPEtJnMDrVrURqdixtLRVvAQvdQehXIvO_KknHKiyUA6CvU-vsSwOyKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعضی رفتن‌ها، فقط نبودن یک نفر نیست؛ انگار بخشی از وجودت را با خود می‌برند. بعد از تو دنیا همان دنیاست، اما دیگر هیچ‌وقت برای ما مثل قبل نمی‌شود. دلتنگیِ تو پایانی ندارد
🥀
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/666572" target="_blank">📅 21:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666568">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9160db867.mp4?token=b-IkF9ji8PGkqZ9GRptU6S9b3dw9GTg8YS7z94GVRZBupJeZ_Jq_jIyBivoV1T_4ykIJQTffa2OWAP2zyDLUzvp4IR4szsVU7JHDz4eTnl3f6Bp1YFKwkBnNl-UHKxsK3DSGRaDpVZyfZltPagLwmnTzGlEvT9Gohh7whEPRQVj3qSFQNo-rxvwWH0MXC2wVRhL3ZNQ9NjxphpKFfwurSeKoKFSIvVzqFmDrLrCFqi626EwW7H3b_tRRYOtPicUY2hXnyk_xHw21--xrpTXWVnu_eVEbOSyXvOSHS9L3asFoXAuNlbUnoEDPrPCR6CjvI1e6u-QM5buLJ6MTtRF6SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9160db867.mp4?token=b-IkF9ji8PGkqZ9GRptU6S9b3dw9GTg8YS7z94GVRZBupJeZ_Jq_jIyBivoV1T_4ykIJQTffa2OWAP2zyDLUzvp4IR4szsVU7JHDz4eTnl3f6Bp1YFKwkBnNl-UHKxsK3DSGRaDpVZyfZltPagLwmnTzGlEvT9Gohh7whEPRQVj3qSFQNo-rxvwWH0MXC2wVRhL3ZNQ9NjxphpKFfwurSeKoKFSIvVzqFmDrLrCFqi626EwW7H3b_tRRYOtPicUY2hXnyk_xHw21--xrpTXWVnu_eVEbOSyXvOSHS9L3asFoXAuNlbUnoEDPrPCR6CjvI1e6u-QM5buLJ6MTtRF6SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥀
کلیپ های رهبر شهید حضرت آیت الله سید علی حسینی خامنه ای
همونی که براش نمردیم
آخر سر فدای ما شد ...
#رهبر_شهید
#استوری
@Heyate_gharar</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/666568" target="_blank">📅 21:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666567">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d6d4fa62.mp4?token=LQEk7VBvd6Niym8yJSWrgPJxH3DCBaOlhC3JsSKD50bDh6UkExq5sLL1kicSG0yyxhjp8hHjHnEWlZro4N1qQ-RUglVytES20pY0xI6KaqcEjx2XYlnswnJL06PaeJvJqVzlq9dob2gaMnbMoIxlGDt1r_civZ0Ay_gKhE-YQlz1ToYqkRv8v9BrohWcdF87qZbTgtvMNANqdMu3gXV59IGSOc1mNMniqNnwwSvuWDH4DPmIjL4vbxPo6klnSuvWW2ZEvyfGshgNQsmwZsXPGflYwMTXeBPaSrvUs9FMDAAUNYA0K1HKiFkuvfve2zwvEibA460X-J0gKqi10zpFwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d6d4fa62.mp4?token=LQEk7VBvd6Niym8yJSWrgPJxH3DCBaOlhC3JsSKD50bDh6UkExq5sLL1kicSG0yyxhjp8hHjHnEWlZro4N1qQ-RUglVytES20pY0xI6KaqcEjx2XYlnswnJL06PaeJvJqVzlq9dob2gaMnbMoIxlGDt1r_civZ0Ay_gKhE-YQlz1ToYqkRv8v9BrohWcdF87qZbTgtvMNANqdMu3gXV59IGSOc1mNMniqNnwwSvuWDH4DPmIjL4vbxPo6klnSuvWW2ZEvyfGshgNQsmwZsXPGflYwMTXeBPaSrvUs9FMDAAUNYA0K1HKiFkuvfve2zwvEibA460X-J0gKqi10zpFwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقامیری: مردم با حضور در مراسم تشییع، غیرت و شرافت و هویتشان را سر دست می‌گیرند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/666567" target="_blank">📅 21:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666565">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
حرکت دسته خانواده شهدای میناب به سمت مصلی تهران برای وداع با آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666565" target="_blank">📅 21:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666564">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0cc9eb971.mp4?token=V1NUqLvVZoPzXFZwjHccrXuQ3XbIId6JLzDmRNz7S0vG9Q2s22Xr1r2yQTJcSv3v4GvgMkRaIxxr_7IZ-xi5If0DIscplkoA6M4Gq8sa4bcV_e9dpurzTUYvWgZUmjCo8hXdWWRy1PqLT3B8Zg4_zD1KT63U-M-rzNU4Wm-GLfzi4bHybjQAdzbXTeHnlAj-VmnLtW9FVt2vmKZAM92StHjdKwH8SWWqzsgR63pR57PQfPzg4SaUS_aVJ6ouiq-I94jBpTcgIQ4LeY399Ugn6tFuLeqWKcF6NCxS0wnv-KEOzsUX-VyTbbkfTSswfVTT0h-xcl_wZacHd2NJ7XjByA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0cc9eb971.mp4?token=V1NUqLvVZoPzXFZwjHccrXuQ3XbIId6JLzDmRNz7S0vG9Q2s22Xr1r2yQTJcSv3v4GvgMkRaIxxr_7IZ-xi5If0DIscplkoA6M4Gq8sa4bcV_e9dpurzTUYvWgZUmjCo8hXdWWRy1PqLT3B8Zg4_zD1KT63U-M-rzNU4Wm-GLfzi4bHybjQAdzbXTeHnlAj-VmnLtW9FVt2vmKZAM92StHjdKwH8SWWqzsgR63pR57PQfPzg4SaUS_aVJ6ouiq-I94jBpTcgIQ4LeY399Ugn6tFuLeqWKcF6NCxS0wnv-KEOzsUX-VyTbbkfTSswfVTT0h-xcl_wZacHd2NJ7XjByA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عباس موزون: رهبر شهید انقلاب تجربه نزدیک به مرگ داشتند و یک بار روح ایشان از بدن جدا شده بود/ بعید نیست اسرائیل از نیروهای شیطانی کمک گرفته باشد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/666564" target="_blank">📅 21:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666563">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادعای رسانه عبری:  نتانیاهو انجام حملات در جنوب لبنان را به تعویق انداخت
🔹
رسانه‌های صهیونیستی گزارش دادند که بنیامین نتانیاهو،  اجرای عملیات نظامی در منطقه «علی الطاهر» در جنوب لبنان را متوقف کرده است.
🔹
بر اساس گزارش‌ها، این تصمیم پس از درخواست دونالد ترامپ و در سایه هراس از پاسخ تلافی‌جویانه ایران اتخاذ شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/666563" target="_blank">📅 21:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666562">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
این سلاح ایرانی لرزه بر تن دشمنان می انداخت
🔹
سلاح بومی که در اواخر دوره صفویه و دوره نادرشاه افشار و کریم خان زند به کار گرفته شد، سبب پیروزی ایران در جنگ های بی شمار گردید و توانست ضربات سختی به دشمنان شرقی و غربی ایران وارد کند؛ این سلاح بومی که در جنگ با دشمنان داخلی و خارجی به کار آمد، «زنبورک» است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3227867</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/666562" target="_blank">📅 21:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666561">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e8c0f03e5.mp4?token=NV7pKstA0w3gGDXxL8udutGk79c2L22ny72NBCZ1ISFE_1M3Ru8Pl1-ZLgpaVU3VehqnLnvD4HF_HZw5ij-S_sauYicQZJtOtdEx8aaj3gAK6DubTEF1KAWDW2CHnJqEkAEcDXWveTh74PoHvg_RHVPb6Y5yy1OzP26hdDgrgvozgiQ98mEMyyo6aw0aeiVq_WE-XqLgFnCcwQVCYUH4VPcBKBvJOebMHMBLKG-58ERdOWU0wYd_gTEpvOFAUiDrgXu1HmJMOv7zPXy4CHMw4BX2shnmr-EMl3nG9JXTs66Ms35x9MfsrYWh-CKSk-RvNEYhmghm_-PXMj-1fTb0CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e8c0f03e5.mp4?token=NV7pKstA0w3gGDXxL8udutGk79c2L22ny72NBCZ1ISFE_1M3Ru8Pl1-ZLgpaVU3VehqnLnvD4HF_HZw5ij-S_sauYicQZJtOtdEx8aaj3gAK6DubTEF1KAWDW2CHnJqEkAEcDXWveTh74PoHvg_RHVPb6Y5yy1OzP26hdDgrgvozgiQ98mEMyyo6aw0aeiVq_WE-XqLgFnCcwQVCYUH4VPcBKBvJOebMHMBLKG-58ERdOWU0wYd_gTEpvOFAUiDrgXu1HmJMOv7zPXy4CHMw4BX2shnmr-EMl3nG9JXTs66Ms35x9MfsrYWh-CKSk-RvNEYhmghm_-PXMj-1fTb0CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پخش صدای دل‌نشین قائد امت
و گریهٔ مردم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/666561" target="_blank">📅 21:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666560">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfef33bb16.mp4?token=sTLcOOhXOxjRi2a14BLz3TdWUIsIUH9PO0264ebRqDChsebAqQ1a5rUh97W7_Y6tEurdreVUW9-h4px78CsrxMWl7jLZPGzhlc7Yh5GRiEsSMFInXPjvPF52ImYqeWd331Z3Z3nAgSnfCOT1qxLOHksCiHr-wPCJckSu8Dj6naT2dtPU8xTL_6ccTc0N_OuS2YzlMvDcGROdDl5rAqJvkSHPRGDsf3UOnj1sI9Rvb8Fj5rnLtW-yy5oqMeUEDbBvXcl25I2lIyFiRdWaRgsMWGs3dZCxgZr3Hb3wv6TiMZtw1V_Eu6sGGx9aGjB9OgXxFpjIcYhPEIYv3uu6j2mI4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfef33bb16.mp4?token=sTLcOOhXOxjRi2a14BLz3TdWUIsIUH9PO0264ebRqDChsebAqQ1a5rUh97W7_Y6tEurdreVUW9-h4px78CsrxMWl7jLZPGzhlc7Yh5GRiEsSMFInXPjvPF52ImYqeWd331Z3Z3nAgSnfCOT1qxLOHksCiHr-wPCJckSu8Dj6naT2dtPU8xTL_6ccTc0N_OuS2YzlMvDcGROdDl5rAqJvkSHPRGDsf3UOnj1sI9Rvb8Fj5rnLtW-yy5oqMeUEDbBvXcl25I2lIyFiRdWaRgsMWGs3dZCxgZr3Hb3wv6TiMZtw1V_Eu6sGGx9aGjB9OgXxFpjIcYhPEIYv3uu6j2mI4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقامیری: مردم با حضور در مراسم تشییع، غیرت و شرافت و هویتشان را سر دست می‌گیرند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/666560" target="_blank">📅 21:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666559">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
روایت الجزیره از مراسم تشییع رهبر شهید انقلاب
الجزیره:
🔹
پرچم‌های قرمز، که معمولاً با شهادت مرتبط هستند در تشیع به عنوان نمادی از انتقام تلقی می‌شوند.
🔹
این پرچم‌ها در سراسر محل یادبود مصلی بزرگ تهران و دیگر تجمعات مردمی دیده می‌شوند.
🔹
«ما باید برخیزیم»، شعار رسمی مورد استفاده برای مراسم بود که با تصویری از مشت گره کرده رهبر شهید ایران بر روی زمینه قرمز و سیاه همراه است. /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666559" target="_blank">📅 21:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666558">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e0a6909fd.mp4?token=NVrVyoZxy4UdE0cfI-Ol_KE6QzgNfkW1Y61s0uemsBzNEviE5ZZLyZaeskJsiwDuPEHM4DvS5V4WTiV9fzlNEsFAPzo5KpLs70QcaoyLHq9TdU30bQNzVWFMWObTMdt8kXcByk5y1Fj3WMg4RQggWKstXplMXsLSMN1Z9ZLYI6faJgyicN-HpUP1aGDcibvqpjsq7yveVZugfaIJggE9_ax6OjtaJv7LlT-hdR1dmGqFd5Ee341MK_bpphZGBZgEDTzs2CAuNna_h6WcjvXVFaBu7n2j5dU5K4da903YV-GSrPfHtxNBW9mCPuKeyeU5moIWrKQ5DikLUfAP8i479A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e0a6909fd.mp4?token=NVrVyoZxy4UdE0cfI-Ol_KE6QzgNfkW1Y61s0uemsBzNEviE5ZZLyZaeskJsiwDuPEHM4DvS5V4WTiV9fzlNEsFAPzo5KpLs70QcaoyLHq9TdU30bQNzVWFMWObTMdt8kXcByk5y1Fj3WMg4RQggWKstXplMXsLSMN1Z9ZLYI6faJgyicN-HpUP1aGDcibvqpjsq7yveVZugfaIJggE9_ax6OjtaJv7LlT-hdR1dmGqFd5Ee341MK_bpphZGBZgEDTzs2CAuNna_h6WcjvXVFaBu7n2j5dU5K4da903YV-GSrPfHtxNBW9mCPuKeyeU5moIWrKQ5DikLUfAP8i479A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصلی امام خمینی (ره) میزبان نخستین شب وداع با پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666558" target="_blank">📅 21:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666557">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ادعای ترامپ: ایران و آمریکا تصمیم گرفته‌اند تا  یک هفته به مذاکرات وقفه بدهند
🔹
در این فاصله، هیچ‌یک از دو طرف به سوی دیگری شلیک نخواهد کرد./انتخاب
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/666557" target="_blank">📅 21:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666555">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gY9U5x-9Vpa9FLLQKXpI6TnnQku_e-y0SVDlW3k8pMePdZizOuKB68z8Zy_wleewSPg1IzlDxqn1njKP2GbSCblpF09IsmE15jyaI_aE8Zi2r3BotRnTOp1_cEDEquFMnj3mvlnjHgKywKCDR0zoZMX1HpTjNs1keHMKsuKUGrDoOUUspgM5_L-f8mt92UYpFVbaazL6OI8Pau92_fsovQKaNYjVbzhRj21QyBoC9EmYMo0jXZEfe0AmukSIaTmH00ltDM3OOtlHimkpSJ5CxYp9aLj47LSvGiVOTplumqoVV3BBp2YHynZc8c9yq-YQfokEDYa0jiAmiBgEarfYOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی سریال: چرخ زمان | (The Wheel of Time)
🔹
ژانر: فانتزی، ماجراجویی، درام
🔹
امتیاز (IMDb): ۷.۲
🔹
خلاصه: پنج جوان از روستایی دورافتاده، ناگهان وارد سفری می‌شوند که سرنوشت جهان به آن گره خورده است. زنی مرموز از فرقه «آیس سدای» باور دارد یکی از آن‌ها همان…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666555" target="_blank">📅 21:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666550">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0K6UHy0TLJGJwmJH0atGDRxXtdIC6HTVjx5UITjcf0kmKHjx2_slC8d2PDDImM6hZ8tvMra_-WpnYppaB7oFqlHHTVyktbqTUrBmRRQ92oHHAU95uyhmRCS4DlrPwWalVTRgjef8MTpaaxaBh1GPg-tVQra6ijvl0BxH1TjLNz6dzugGwHCZShl8j75eKrYni3zaQ-RcM0aoyQXzDD5Jkl1km1LUFjwfxXyVky9XqnLJgbzrLG8XhWCRacZ-RASYwoDKiPL90UhLcU6PvNqkr0nX3Be_ssOGyzpMU0n_SvdMmrqRzbAwqKJnCmAdo2jpP5je1aObGoj0EJE9tEj1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r7YPhor4gX5G-9MGK3ltMiRbqfdSpPzAgjSY21W_DrfWSsZsnRXq_maPordx3MnLACbWTwivKkxyrRd4n0MNx86k8MurbXrckjV1LzkiozDI4kqcvx5yPuW4AgiK2yktVj5MApgtDCZSL88mmsmIXrOH3j8BRrX7GZwgKT0Xcg2kNU7j2eLXMQy34ExTrcEePhfihEd8iJD8G2tpKeTTJPjPlJt1hr8C0MArV09OFfHxE9hhjnXwjqD3zanvNt8QHUJjiwkTQRy_s8dPvQsz4ZRF9yPhDDHqT1d6I2zMlgErBmeu4EiYD6-K_E5pPOh0hqKEc9-3OoefGI30dkgnEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LaAgYSRkxelAw1p7zXrQvyGaMQt0ZNq40fLPp0cTvzxgOozZ7JCeVTTGOVy5WVZ16QsIOcHRhs2f-hufeMfpPSi-D7OV-nw3MutU4ht6UG30rFzqib4_i0aeAgo1moQdrbDwMewmGKw4NZnx2s3f9VCValzDs6eGL1swU2C1-tdhNhE7NFTbQC1_icviUEVhPHaGhpyQDCXIBGsKgr6gVSgXXPaUUBaQe6V7fjMpB_Ykoyb-VedggVfTCG93vVZZL6fgLRawoXQk4isab-3yXGDdm0afzDk2ltfpKJVtMqvppzPJlgdfysu0Osly0-4lHwH2RfKRxB1pbq1LDQbQuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pbpLvZFYuox2QyNiRqNA9YadY-YoVStBN9cwLZ5GzPYwlzxZzj6vP9EqWUfVWk84Y8xdH9GMRWLujm5ntUEV2ycaO6aviXRInBMKjMFXsE3PjQGrJaLPux_1fVa8p4D6-2fJjay8XYyC-iIFkLyKuc3gEZeRv5K2YFi6zrfWB1L-oJwbMSHRIcUyx42hmf9mIkNkl2D1Q-EXwTouGxg1vz9JbxPMB2aB3Iz4JMkR-i6pSqnskndynFixnvnz5CvUEgBuK4CnonWEU3we4ltYSPwDrqsHlEZSGSgLuz2xe_MhSxE1_7LJA15pjureHsCMVmo1qqavWMk0Gv5o2qRsow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vmVDNYHgd_8g4EHnfeuEVZYQvylcpjOuNsWt9YdGPT_GuPC6pEujIYeOilunSsmV-xeIzTj1tOhAUgAzLMQnhc3rVgN6bC1gWQZln5QvoUj9Sfk4ZlgFlX3-0sQvG5mmAZyVgJzyG0ZfFLL7SlIkJ7qQLX5TMs2wkKQiBHsbkVHgaIwDfOHkoV3e8WocMFQi66MwNHtHLzfa0beEFZEdiQ46EGdVNxGOjjwujQp0iKEur2X77L4F5A94Pf7_uahJ_Mboicd6HkYAfe_14btLDwyLrjR65euRYjXjBxU67ryQ3SmWmCGCxqb4yVwI--sz7hMr1PSYVJ5ImKci7YT-wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرگزاری الجزیره از روز اول مراسم وداع با رهبر شهید در تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666550" target="_blank">📅 21:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666549">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
بانک مرکزی شایعه نیویورک‌تایمز را تکذیب کرد
🔹
بانک مرکزی ادعای مطرح شده از سوی روزنامه آمریکایی نیویورک تایمز درباره نامه عبدالناصر همتی به رهبر انقلاب در خصوص ذخایر مواد غذایی را تکذیب کرد.
🔹
یک منبع آگاه در بانک مرکزی: چنین نامه‌ای درباره کمبود ذخایر غذایی به هیچ وجه صحت ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666549" target="_blank">📅 21:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666548">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
پنجره‌ای به مراسم وداع با معلم شهید خانم زهرا حداد عادل، عروس رهبر شهید انقلاب و همسر شهید رهبر معظم انقلاب در مدرسه فرهنگ تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666548" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666547">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70caf986c.mp4?token=NcYhWtNvpZt7mZR4-VuRtWfvEE_zL5QZw736At8S1_D-xfRvdGd2wgbycABsFFkZYHAULbJ4NbZ9Re1XoLQgEGKMs72DSwUoHO5SU1u_JXw2zHUDmp82WJzRSmhstLqC5fLht7lEV7Tnhbnf5LhR70cVK-ATagdIW4ui1mdWyeQWf82ZrX_7McfF1PoZmhRseSEjnLCCqWpUTGNMpmUATBzKma2IDflGdhVkVlbBfX_vD5EGKwBNOMiW2j-gotjOys-KlbKhvzMPsnqa85No3EnUkYRLGpIW4Ox22LabVl8u5vT6v6XuJITNh_QoWywLKCsjI7t0KA90kugSaDpGYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70caf986c.mp4?token=NcYhWtNvpZt7mZR4-VuRtWfvEE_zL5QZw736At8S1_D-xfRvdGd2wgbycABsFFkZYHAULbJ4NbZ9Re1XoLQgEGKMs72DSwUoHO5SU1u_JXw2zHUDmp82WJzRSmhstLqC5fLht7lEV7Tnhbnf5LhR70cVK-ATagdIW4ui1mdWyeQWf82ZrX_7McfF1PoZmhRseSEjnLCCqWpUTGNMpmUATBzKma2IDflGdhVkVlbBfX_vD5EGKwBNOMiW2j-gotjOys-KlbKhvzMPsnqa85No3EnUkYRLGpIW4Ox22LabVl8u5vT6v6XuJITNh_QoWywLKCsjI7t0KA90kugSaDpGYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی شورای نگهبان: رهبر شهید می‌گفتند در تایید و ردصلاحیت‌ها قانون‌مداری و رعایت حقوق مردم حفظ شود
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666547" target="_blank">📅 20:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666546">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmNGxJykqBfYf5SWed1VcJmS1gdTc1071Ghz3i9rwy5Xh_f_Gf46O1gxXlH81-mXdBFtJ9-5NQxtMqsRsvBL_JhDtgB5omSSepzgGLm22QZnqfEiAbB2amoy100crSf6HBISAB5FP54U9e0jIoEHWi3yBosJwymQES-tEWjJP-iBehzOjOWDIsS1GAn1hmtlM0ZBohvr-J2JqfijUJNp-5KFmjKFXEW0Fb1mA1H7RjY1Y-XqlEqeUSpM_1BacRKYIcVJtovNKjSCpPk-Rcb8nZr8OdtdsjH1j889yEOiGvSD4zNUgsKUjXvsEeTi1IaudDHNfTa2VBhFzpEKIBF6RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فردا؛ مراسم اقامه نماز بر پیکر امام مجاهد شهید و شهدای خانواده ایشان
🔹
یک‌شنبه ۱۴ تیرماه ۱۴۰۵؛ مصلای امام خمینی(ره)
🔹
شروع مراسم از ساعت ۶ صبح
🔹
اقامه نماز، حوالی ساعت ۸ صبح
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666546" target="_blank">📅 20:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666545">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ترامپ: از دیدن گریه مردم ایران در تشییع آیت‌الله خامنه‌ای غافلگیر شدم؛ چراکه فکر می‌کردم مردم از او متنفر هستند
/فارس
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/666545" target="_blank">📅 20:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666540">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MOjh4MDo8OZdB_ZwkGAG_Gk0wdOCHSM7TN9qlesudk_4I5XKQWDwXKUADmDpz6OyyQBqTjZd2EEMB-gnBKuZzLP5SMlDE-_yZJjnbdi9hW6GfHmn9R0q7no46gz6RlD3a4RtHw4RiBjJ5CJtrDBY4WkKYpUG5yTng1SJx8_P4cyHHdL3jSyRgi__JcNpSU459Wq6U-R4nsRyiCzCd-nrnm2v3OvZRw6F9AI4mg0-sJoQncoM8mh95pALPL9ikYDu9WH317UuVf6T6NeLIJyYS16EjVG-FA3-G-O-Su4JSX47ESUJgO6swtZQtCjq3mSom99q171DK8mFjNo7hx72MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pS9VSuos69j6G5OguHl-gdifXDVPjYbN3tAx4XrCM77pKhqKudDpfC_sirun57_76oJ1iKZ3GqQ37LDLS1NMJNhoE0WCJ3A_5TjUu0Y09MpsssppVNOKwHHrgT_TVKl0Mw5aFkguTdJdRMn6ewOlywMT48SADknCUIaWflSs75StrXRtlLLy_gqIcJYmqbpCwqua-l-wlvfv-NPlF6jt6fjxRr1FHSHUE_ThvMnSZ72EX3lKYgGUV8XL0wGGK3yvRMzGGpogjwhu7JkmSdTLW7okl2ygL-iRyuOPZniWba8V7wMJPsvf4ZBNmUPxOONGfQCxS8iBplGkqyFEwzt_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sk4v--PhwA_urdOnFuz6_DKp3rvxxJlZgUY7cDbHaTrI-LmYHy78xuWChu3WcGKjZvhdEO5T8Xp_PuoDI5u3-No0ihrmaQX7MBBCwaTDwGV7YcpSVx3E1nXV1Grj6eytNsyEJ0jCNNxqbpSzaUmv2Bdmzh-l8qb6S8G0aopkX2lKTYZTntRFbgwTmcYxwszArcCYM2v3vWiRM_-OSUjD9xXcg8KVkxmtlrBymVTf9qGjAb4iShPmHq8QOmVFQWo9Thgrt2M10PQWtfsMP8qYqcUY7pkSakFk5NbahJY4eU8atAN5rqyNq7lOoZBoUmYF2H4IfCxGkaQUSaxlKtLeuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tuwKowWpAsMPKaQx8MCIyjzPNkwIFFZjryqnIc20hvPs3lbXyzjmUCeXBFIjlz8MsmuQWlQ0UyM5PElQYMWVKQYzsiGr2ufZo-T37UDdGFJgU0HQVBBq5chmXgePfxFn95byqQeZU5F62skFYYB6PtkcsQLgZWvxvkpt2nu8IPWwRMUwW5yGb9rlqz3_cGq_EZYxViLbykuv_mPyQ1rJENIH-TA2xn_OUyVRxA0Dz4AWBE89huR3OyEK4qm_Pu7GukQVSB_ZLwNjXs_Mo2j-weZUSz9PjllvYVNCyAuQosBsZWC1S57XEjRqrts--bJkQ8OgZyooWLseeGKjxTdCqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PPHqK3pjjwSQJZQhng_wxyqBTJ4dABnIet6mvbhb_aXrSnN2u9_paJPKby1HlTjk0a6DVwXKEJ6FAZPEI__cCMaOBv7tyx_kxnJoBXITRongsWMxrg2K9C0SN7HBQFRq0OH83iTMpn2CQbVYnStDRhoYSJWJB3Raxy1B0XCCOBmhaPoWy1C_nF6jrW7Hj0iAauQfeC-lJaeNNXcyKZjSUFHco0L5AiUoc3Ci5-_zRWIz0Qk9os_S8Q_W2oz3C0nCSWBurcPdaJmyZwnaI_QSKBc1o-Rq3lAYFHAZGe2Xo8YTrvgHClYGpKuP4yE7HJeFn5kIdF885wLKHSzU-erw2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور شامگاهی انبوه زائران برای وداع با آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/666540" target="_blank">📅 20:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666539">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
الجزیره: ایرانی‌ها خواستار انتقام شهادت آیت‌الله خامنه‌ای هستند
🔹
احساسات مردم در اینجا رنگ و بوی سیاسی نیز به خود گرفته است و فریادهای «مرگ بر آمریکا و مرگ بر اسرائیل» در میان جمعیت طنین‌انداز است.
🔹
بسیاری از سوگواران حاضر در این مکان، خواستار انتقام برای کشته شدن آیت‌الله خامنه‌ای هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/666539" target="_blank">📅 20:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666538">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
مراکز شماره‌گذاری وتعویض پلاک کشور فردا تعطیل شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666538" target="_blank">📅 20:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666537">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
کرملین: شاید زلنسکی به مسکو سفر کند
دیمیتری پسکوف:
🔹
رئیس‌جمهور اوکراین ممکن است به محض اینکه آماده تصمیم‌گیری‌های مهم و مسئولانه باشد، برای مذاکره به مسکو بیاید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/666537" target="_blank">📅 20:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666536">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4003ac89b3.mp4?token=ZdFqTnuSdEziUoRV_9XH-sZTsHCS_-e1FV2OxNGgcX4BiJ_G4FPsxjtDXL1ORKqg5M23C4NCs4a35HGlYW5udlUBo-AaY-_JWmTuV7AophHF0nrDGyETl2BhWX9eMpEfRMCZfJ-7uUSVBcZdmvL_jl1pxAN2TXc3SPQd-50iKsBf3nTlvpm9n809NtEa3ThP9s7IIi6KbtfdyyfKmjhBb393-COoRsnES7qG6HgERvbKpIcYtkWyqG_Z5lI3HB_eMQLBhjnCaUB8oIVEDIy6C7mqfwZXKn2oK9G0UJ7i2NXmKZKjeU1ZCL4y8-C_rwHflxjZU1Hl_ZSyO2RVEe41GYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4003ac89b3.mp4?token=ZdFqTnuSdEziUoRV_9XH-sZTsHCS_-e1FV2OxNGgcX4BiJ_G4FPsxjtDXL1ORKqg5M23C4NCs4a35HGlYW5udlUBo-AaY-_JWmTuV7AophHF0nrDGyETl2BhWX9eMpEfRMCZfJ-7uUSVBcZdmvL_jl1pxAN2TXc3SPQd-50iKsBf3nTlvpm9n809NtEa3ThP9s7IIi6KbtfdyyfKmjhBb393-COoRsnES7qG6HgERvbKpIcYtkWyqG_Z5lI3HB_eMQLBhjnCaUB8oIVEDIy6C7mqfwZXKn2oK9G0UJ7i2NXmKZKjeU1ZCL4y8-C_rwHflxjZU1Hl_ZSyO2RVEe41GYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری از اقامه نماز جماعت مغرب و عشا در مصلی امام خمینی (ره)
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666536" target="_blank">📅 20:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666535">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ترامپ به آکسیوس گفته است که بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از او درخواست دیدار در کاخ سفید کرده و این دیدار ممکن است به محض بازگشت ترامپ از نشست ناتو، حتی از هفته آینده برگزار شود
ترامپ:
🔹
ما خیلی خوب با هم کنار می‌آییم.
نتانیاهو می‌داند رئیس چه کسی است
.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666535" target="_blank">📅 20:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666534">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aU8lVvxB-OT48q2TJFGHUgkFLfKj5oFLawIx-5wgPGhqZEaoi7B3FeN-YbKkQgHHoEiLzoepTAmdug7dJejfep0yHdQjqDTsdV6tjTaiNjZ9WpnSlY0-7DLTIGJWkoiuC7QONgr6IcvRUtnQi7Qtk8EL2MOm3sfWQbwFiC3kNTfLs5C9k1iE7W1yZGD4tXSQtEcVsrYYyG09bz1ljg6xWoZ30QpmQ719OpdXw5VjHwRxiV_EOEMcdklBDUy4p56QyO9elsybwzy42ibqdlT6ie3_44kFqssGNU7zSZfETte7e0iYsfX9RSc87QJt0OQqjL29w-INKRtD7eiV0D_7Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقش شما در بدرقه (۴)
🔹
اگر نتوانستید به تهران، قم یا مشهد بروید با اکانت خود در شبکه های اجتماعی و انتشار ویدیوها، متن‌ها و تصاویر مرتبط از شهرتان در این بدرقه همراه شوید. در انتشار عکس و ویدیو از استفاده از هشتگ های این روزها و کپشن انگلیسی و عربی هم فراموش نکنید.
🔹
از الان شروع کنید و راویِ حال و هوای شهر خود در بدرقه رهبر شهید انقلاب باشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666534" target="_blank">📅 20:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666533">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
تعویق برگزاری امتحانات نهایی پایه یازدهم به دلیل تسهیل در تردد زائران مشهد
🔹
به دلیل تسهیل در بازگشت زائرانی که به مشهد مقدس مراجعه کرده‌اند، امتحان نهایی پایه یازدهم که برای روز شنبه برنامه‌ریزی شده بود، به تعویق افتاد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666533" target="_blank">📅 20:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666532">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
توصیه کارشناسان فوریت‌های پزشکی
🔹
اگر در مراسم پیاده‌روی وداع با رهبر شهید شرکت می‌کنید، حتماً یک بسته پودر ORS (او آر اس) همراه داشته باشید. پودر را در یک بطری آب حل کنید و در طول مسیر، آن را به‌صورت جرعه‌جرعه بنوشید.
🔹
نوشیدن محلول ORS به جبران آب و املاح از دست‌رفته بدن در اثر گرما و تعریق کمک می‌کند و می‌تواند از بروز کم‌آبی و خستگی ناشی از گرما پیشگیری کند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/666532" target="_blank">📅 20:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666530">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vwglro26Nn3eGq8wZevggNV60WqSxVUrMzKOuGoU7kcy4RVjxmLNR9igvi7kFfRjMSPbyVoHXxUhAly3tqJu10I5YZPYkeHoJ74WcYQO9LvffLG_mOjUk_I0E2o6sNn2kUx1C6gZttRsjilAuN4SPQkR16siN0yHWBuDrx9o6XChXbdfkc9NTjNnmFRde88m3ALYyKSn-nf2sddFGxspIXR563YcD3dNLOFIkoFFQwe2DPsLX0F17Xs9hZTpaju9CCsF_bOkvJkr3Mn9ahzfPTutoUn5Qrevn3x2N7LWVdRtXZqNvwHhJgcb2LPYNgFUP4pn7iGKIYy2TsTPVImxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G88AsN8dEmsUIOloCt1JEp8fNAhkbO6FGIygrqFsCubAUHMtHbFaI3RtWFTSla9ZGJDLqWp0cIRO8TPawVeZzuF1cjS7SwReV1y8wmkq6yn7m46CACLz9V3PdWrA_QXraaaOA72hRC5bMq54HR8ocUU_j-sdfxKR6DDwkNHTjWD-aAHKS4Uajm3iqlSrvuIj3cEhW9yzOHnmKqjXHqjfKdd3VK9rtvsZ-cgoYHl4SfEx3SyiYKSiCZsf-dlESf3uI23OpFha_ut9_5WD7T6hWqvR_A5e90K6g4i-WGp2pobVfKW0_O8481dyrxLMW74zDQWJoCllVyJsfs_JIPnNuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
برگزاری نشست قرارگاه مرکزی حمل‌ونقل جاده‌ای وداع و تشییع رهبر شهید انقلاب با حضور وزیر راه و شهرسازی
🔹
نشست قرارگاه مرکزی حمل‌ونقل جاده‌ای وداع و تشییع پیکر رهبر شهید انقلاب اسلامی به ریاست وزیر راه و شهرسازی و با هدف برنامه‌ریزی برقراری سفرها در حوزه حمل‌ونقل عمومی و جابه‌جایی عزاداران شرکت‌کننده در مراسم تشییع به میزبانی سازمان راهداری و حمل‌ونقل جاده‌ای برگزار شد.
🔹
وزیر راه و شهرسازی از انجام هماهنگی‌های لازم در خصوص تأمین سوخت تنخواه ناوگان اتوبوسی خبر داد و بر ضرورت برنامه‌ریزی دقیق برای تأمین ناوگان حمل‌ونقل عمومی جاده‌ای در سفرهای بازگشت تأکید کرد.
🔹
در ادامه این نشست، رئیس سازمان راهداری و حمل‌ونقل جاده‌ای به ارائه گزارشی از روند سفرهای هموطنان به شهرهای تهران و قم طی روزهای اخیر و بررسی ظرفیت ناوگان حمل‌ونقل عمومی جاده‌ای برای استمرار سفرها و بازگشت از مشهد مقدس پرداخت.
🔹
معاون وزیر کشور و دبیر ستاد ملی مراسم وداع و تشییع قائد شهید امت، معاون حمل‌ونقل وزیر راه و شهرسازی، معاون نظارت و بازرسی امور تولیدی سازمان بازرسی کل کشور، رئیس سازمان هواپیمایی کشور، مدیرعامل شرکت فرودگاه‌ها، مدیرعامل فرودگاه امام خمینی(ره) و اعضای هیأت عامل و معاونین سازمان راهداری و حمل‌ونقل جاده‌ای در این نشست حضور داشتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/666530" target="_blank">📅 20:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666529">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
خونخواهی، میراث کهن ایران؛ مسئولیتی بر دوش مسئولان
🔹
طلب تقاص خونی که به جور ریخته شد صرفا مطالبه‌ای ملی نیست؛ بلکه ریشه در فرهنگ تاریخی این ملت دارد.
🔹
سیاوش در فرهنگ ایرانی با مظلومیت خود به نماد جاودان عدالت بدل می‌شود و کیخسرو با برپایی داد، نه تنها خون پدر را پاس می‌دارد، بلکه نظم اخلاقی جهان را از نو استوار می‌کند.
🔹
ملتی که سیاوش را در حافظه خود زنده نگه داشته است، ظلم را با سکوت همراهی نمی‌کند و نمی‌گذارد گذر زمان، حق را به فراموشی بسپارد.
🔹
مسئولان این نظام به عنوان وارثان مکتب رهبر شهید و وکیلان این مردم در قدرت وظیفه دارند این مطالبه تاریخی و ملی را پیگیری کنند
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666529" target="_blank">📅 20:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666528">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_FaLJ9l34sZmX9DNyta3O9CiOJpmmfzrzlSxWzOG5vCJNf-w2LL_--V0m4mdmWvab6troTuErQck6mgHGUKA7cFZX1tIRaLNDZVGVx1jsy8Srydmd_Q9LeCDTsemetXC8yUIGtxu_TmvJ6AtJZgBmMgzkBLMBawxUe-yFvvA0a139FQcXI6UwNHYn-Ce9avZtGhRiKR1BaFxwLlK8vIEAzcXiLRWshpoUsDgU6JZ9iq4J8lzXgvEN1wVU96z1BWttZWqDHZlrel7nLTaNMg3s_OV9oOcELIZIjPCitpGt1AM3EZSmO8dYYSJaiw_L0RwP9rbp7c9hFBpIT4mOP8mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهان در نبودت دگر زیبایی خاصی ندارد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666528" target="_blank">📅 20:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666527">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
رئیس‌جمهور: وحدت و انسجام را در عمل نشان دهیم نه در حرف
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666527" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666526">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e948877e53.mp4?token=ZGJ-I-RyGq-ku0zCTDMwn-mX7cvwiiOQ8AeNjc4gp7utrLzB3vRRMbDTVnbher93J8FAsmX0oIGyUBerHk7p0RDdwuLvNf_de8n3I9Iox0gOzWjcOtdeD9QWAFnknjZh2PzY6zsfnhqPwM1my3hlBmuh5ewuwd1XgbA4WK7qktf7qnk1JZYlVucnfqZSJ_i_e6K1sn4DsHeNzOe0pw1irRVnAdX6NXwPL4vIJAtEa0y6OZU0RZ1fyNEUIFV1YDER78Uu5BNqHQy3IrArx9GmUESLHZfdBswA5oFJfBxAyc8LHCrdm9jPs2dbLuGAaujMJBR5qtIA3pTqQuq2moMoXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e948877e53.mp4?token=ZGJ-I-RyGq-ku0zCTDMwn-mX7cvwiiOQ8AeNjc4gp7utrLzB3vRRMbDTVnbher93J8FAsmX0oIGyUBerHk7p0RDdwuLvNf_de8n3I9Iox0gOzWjcOtdeD9QWAFnknjZh2PzY6zsfnhqPwM1my3hlBmuh5ewuwd1XgbA4WK7qktf7qnk1JZYlVucnfqZSJ_i_e6K1sn4DsHeNzOe0pw1irRVnAdX6NXwPL4vIJAtEa0y6OZU0RZ1fyNEUIFV1YDER78Uu5BNqHQy3IrArx9GmUESLHZfdBswA5oFJfBxAyc8LHCrdm9jPs2dbLuGAaujMJBR5qtIA3pTqQuq2moMoXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ازدحام جمعیت در مترو شهید بهشتی برای رسیدن به مصلی
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666526" target="_blank">📅 20:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666525">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
نحوه فعالیت بانک های کشور در روزهای  یکشنبه و دوشنبه، ۱۴ و ۱۵ تیرماه ۱۴۰۵
شورای هماهنگی بانک‌ها:
🔹
حسب تصمیم هیئت دولت مبنی بر تعطیلی روز یکشنبه، واحدهای فنی و پشتیبان ستادی و شعب منتخب بانک های عضو شورای هماهنگی بانک ها در روز یکشنبه ۱۴ تیرماه ۱۴۰۵ در تمام کشور به صورت کشیک از ساعت ۸ الی ۱۲ فعالیت خواهند داشت.
🔹
اسامی شعب منتخب در وبسایت اطلاع رسانی بانک ها منتشر خواهد شد.
🔹
تمامی واحدهای ستادی و شعب بانک ها در کل کشور در روز دوشنبه ۱۵ تیرماه ۱۴۰۵ تعطیل می باشند.
🔹
نحوه فعالیت بانک ها در روزهای سه شنبه و پنجشنبه در استان های قم و خراسان رضوی بنا به تشخیص و اعلام استانداری های متبوع است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666525" target="_blank">📅 20:05 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
