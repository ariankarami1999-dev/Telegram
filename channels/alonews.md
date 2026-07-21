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
<img src="https://cdn4.telesco.pe/file/DGuTU-AmW67wLSqyIDJBbm3N1Yt4345HJCPahSokEtGFL2nxz_nFxcuQXC-snOYwJGdCjrU_2dX7F7EJQn2RrftnuCmwwQcY6MwdD2d5mekoj-XLSw2oUVVxpteKCXj5HPLVI2inDzVXggJ0RFHHTS5jEaZkimS5TUxizHP1AQ6Pvza9kXKvJSN601ICXyzY6JsJ2I_GYDRbRxm2cqARdVcKb4W61OmWgBfWavYEb6RZ7J8adOIjw--tY6MAyBW3fuKS_9LokFTky5YjEQ2sg6poWWpaHrjql-ctA1DARqhB_kmloUNF1pYWTtDky2rErLtEZh-zqB0qT5ptF0b3dg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 935K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 03:19:12</div>
<hr>

<div class="tg-post" id="msg-136538">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
جنگنده از آسمان قزوین رد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/alonews/136538" target="_blank">📅 03:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136537">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd3f23e865.mp4?token=N61KQxWuptSCRHqYtViNXT_KnCF5rGJirMm9xqzyAlxD7ihMhxTG5o5DqqoqpiP1F87bbInHn_jsTU-M4zX29Y0zyMxtocAzMQnol-SD_F1H9ttXvkH89k93PV2i9Rb0FQdB5dQsYnu70G9M6pu3YiNpMZLElEZRB2hlrgX3UulsvLUtWg9c75N09GTrIZYxTnBqAAhUHXs6IiaYI3jRvHTuN910ImQ-3fRZJJPUgPW00AUa1IUB8jyOM17FYDqZwu-C4RItqcbGTmQHUYhXT-Z_f_JkWT6mwBzg0Pg0ALkpdGcScRhj0sePijC5zQFlq6zrWYO7u7CrkAhKtJii2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd3f23e865.mp4?token=N61KQxWuptSCRHqYtViNXT_KnCF5rGJirMm9xqzyAlxD7ihMhxTG5o5DqqoqpiP1F87bbInHn_jsTU-M4zX29Y0zyMxtocAzMQnol-SD_F1H9ttXvkH89k93PV2i9Rb0FQdB5dQsYnu70G9M6pu3YiNpMZLElEZRB2hlrgX3UulsvLUtWg9c75N09GTrIZYxTnBqAAhUHXs6IiaYI3jRvHTuN910ImQ-3fRZJJPUgPW00AUa1IUB8jyOM17FYDqZwu-C4RItqcbGTmQHUYhXT-Z_f_JkWT6mwBzg0Pg0ALkpdGcScRhj0sePijC5zQFlq6zrWYO7u7CrkAhKtJii2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منتسب به ماهشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/alonews/136537" target="_blank">📅 03:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136536">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
خوش چشم: آمریکا توان حمله به تهران رو نداره برای همین داره جنوب رو میزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/136536" target="_blank">📅 03:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136535">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
دقایقی قبل آمریکا نقطه‌ای در شهرستان کنگاور استان کرمانشاه را مورد حمله موشکی خود قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/alonews/136535" target="_blank">📅 03:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136534">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
پدافند کرج هم فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/136534" target="_blank">📅 03:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136533">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b55cc12d69.mp4?token=gviYY_gK99dzwuGMBQj3Cxq7My2xuDZP1aGJbz946cOlgCdcGKBM-NAOKuzuDcoHnWAy89XKlFsWGPIgyB-2Ii_lSZlYFuFtJ289QFCE_wvmxP7c8h-DlJhxjzp2X0eMPdYnp6jr8Ekzzl3FDoavLoau3uq8hB2pdRrdLd9jA3pH1-eQgXJwGvKDbiR3exDLcDZ36KhP0AtiS3BUfcDKKg3e3lU_ddNhdVIlaeK651gxHAXIy1Rn3WcGvxzpH3pZI9cJ1ElWfUTAvavSVzO-nqT61UNfGS1otctHOpnXIxPi-BJMWTOG-7jCH8by9g5AtkVxefJnWd2kSJaVObZMyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b55cc12d69.mp4?token=gviYY_gK99dzwuGMBQj3Cxq7My2xuDZP1aGJbz946cOlgCdcGKBM-NAOKuzuDcoHnWAy89XKlFsWGPIgyB-2Ii_lSZlYFuFtJ289QFCE_wvmxP7c8h-DlJhxjzp2X0eMPdYnp6jr8Ekzzl3FDoavLoau3uq8hB2pdRrdLd9jA3pH1-eQgXJwGvKDbiR3exDLcDZ36KhP0AtiS3BUfcDKKg3e3lU_ddNhdVIlaeK651gxHAXIy1Rn3WcGvxzpH3pZI9cJ1ElWfUTAvavSVzO-nqT61UNfGS1otctHOpnXIxPi-BJMWTOG-7jCH8by9g5AtkVxefJnWd2kSJaVObZMyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت شدید پدافند در تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/136533" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136532">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
انفجار مجدد در تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/136532" target="_blank">📅 03:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136530">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فووووری/پدافند تهران فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/136530" target="_blank">📅 02:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136529">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39b2530c00.mp4?token=MxbrCXxInQsF7cYi3Gu9fWEs127ikYOBZjFpHht4wli8Yr7JQQb6sv-R0Sjg23529sbf8uQVJEVVhOL5jDk5kqOLj-emB6UjZo6fC4FdDhj1BHGjYvYA4nT-htFIr3MZ6tmAiUtIomezPug4p_LWvFQfTyrc9ED_KHPNFir3201nYtvlhtSWY-MViiSPukr_m05qYKx4CSqXa3BmpM135yeFlIJJmbKU3pjPkucmtKhhfgdq018cP1AeE81vHOL7c_0iNV_iE0Pu3lYxsm4166-XUkH1mz6YYmT6G_ZnyAO0i8leDTXe5l5MoY3hKgLlvfQRHZ2T9T-TccDE39gnNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39b2530c00.mp4?token=MxbrCXxInQsF7cYi3Gu9fWEs127ikYOBZjFpHht4wli8Yr7JQQb6sv-R0Sjg23529sbf8uQVJEVVhOL5jDk5kqOLj-emB6UjZo6fC4FdDhj1BHGjYvYA4nT-htFIr3MZ6tmAiUtIomezPug4p_LWvFQfTyrc9ED_KHPNFir3201nYtvlhtSWY-MViiSPukr_m05qYKx4CSqXa3BmpM135yeFlIJJmbKU3pjPkucmtKhhfgdq018cP1AeE81vHOL7c_0iNV_iE0Pu3lYxsm4166-XUkH1mz6YYmT6G_ZnyAO0i8leDTXe5l5MoY3hKgLlvfQRHZ2T9T-TccDE39gnNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از حملات امشب تبریز :
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/136529" target="_blank">📅 02:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136528">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
بوشهر رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/136528" target="_blank">📅 02:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136527">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
همزمان جنوب و شمال غرب زیر حملات سنگینه
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/136527" target="_blank">📅 02:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136526">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
چندین انفجار سنگین در تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/136526" target="_blank">📅 02:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136525">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوری/انفجار در نارمک تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/136525" target="_blank">📅 02:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136524">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
انفجار در امیدیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/136524" target="_blank">📅 02:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136523">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/136523" target="_blank">📅 02:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136522">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/136522" target="_blank">📅 02:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136520">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری/انفجار در نارمک تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/136520" target="_blank">📅 02:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136519">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تهرانیا تایید؟
👍
👎</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/136519" target="_blank">📅 02:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136518">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوری/انفجار در نارمک تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/136518" target="_blank">📅 02:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136517">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWsBvTtqe2iQn3VWCqhZqOut74Yhz4wH_MWsOsmJRnu7NM_GZquu5JgDOc_VRCKIea_uY7p_07vk5-6fdr6K0a7theLGZWuqxgca6EYyPhHsihkvqyPwA4XckHfQn1bHi3ykA5fhQnljnKhwEvQS9GOzH4r13mGPV7FujspSUiffrO_W22uNzMoI7IWPd_nPHNpuRSzGU8jS4mbVxPzQcrI50l29MTBcfVi948s8hjnIM65GAfwT2P-XVKXgx2gC-VSKfkYsvjwDC8PA5xt8dnzik5MYhUgA-c7HEqL5OgUnINwRLQnX1eDwwFdHshmlWgWtwbHTWMP1J2TVL6jOoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک پست:
ترامپ، می‌خواهد اینفانتینو (رئیس فیفا)، دبیرکل بعدی سازمان‌ملل متحد شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/136517" target="_blank">📅 02:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136516">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
خبرنگار:
آیا فکر می‌کنید ایران با تهدید به بستن یا تحت تأثیر قرار دادن تنگه هرمز، تلاش دارد بر انتخابات میان‌دوره‌ای آمریکا تأثیر بگذارد؟
🔴
ترامپ: «
احتمالاً
. اما آنها هیچ تأثیری بر من نخواهند داشت. من فقط کاری را انجام خواهم داد که درست است. من به این موضوع با این دید نگاه نمی‌کنم که "اوه، ما در آستانه انتخابات هستیم." فکر می‌کنم مردم بسیار تحت تأثیر قرار گرفته‌اند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/136516" target="_blank">📅 01:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136515">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">استوری دنیا جهانبخت از حضور در مراسم عزاداری.  وقتش شد یادی کنیم از ..... زدن دنیا خانوم جهانبخت برای تتلو
😂
😂
😂
◀️
◀️
مشاهده فیلم</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136515" target="_blank">📅 01:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136514">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136514" target="_blank">📅 01:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136512">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvHbkLTvKVraKTdWHuJpQPvmdyabOuqtkTOQ0Gu2edc6fknHSXF_HyzTsZ4c52SoPZPsDKTWDq1-m4lmSI3Vu30I5sr6mUfv9lrLUsK9aFBLJshaQnrkb1uvabWoIKGwyQF8NJqvTfH5-6WyUovvK18l75LG94c_tTzQm9KPbgRG0zHO1rySg4oZlh2U5AuXra16JYDet_m-0c2KksiSHEoeFlFL4d6_yHhDrvHNi2bXdZBqKurN5D0GZTJDcFHCKyplM96EculrHGA3LvVQuzxxGeYuF4mTrTjn7ZVN4cyvvJgogtAD2zzcDAMQhjrH07ofak6kCs0dcECnyqiygg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور قالیباف: دیپلماسی به پایان رسید، جنگ بن بست شکن است
🔴
هیچ ایده راهبردی وجود ندارد، احتمال حمله متجاوزانه دشمن به کوه کلنگ(تاسیسات صالحین) نطنز در ساعات و روزهای آینده وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136512" target="_blank">📅 01:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136511">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">طلا بخریم؟ نخریم؟</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/136511" target="_blank">📅 01:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136510">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
به کویت حمله شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136510" target="_blank">📅 01:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136509">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aed34ebad0.mp4?token=UFhCoCf6scwt3AQilSCqlgrbYUmPOOtFkgAZS5LVZ3qE75uWdADBxGCgAf4HxPi2vc57iC7cc9bqe5rKLo1ZzqMuxdOgzgOYEjS1plYyaQYcrPOe2DfzgARgCCC-VKgni9dUv5wUEzEMWp8jv6_a4kZ9W9kMAgL5c0jeEgtSoXLx8QQt8F_w2gX6tbgxDju-ZYs11HWajuNx3EqlqFb9MwYgY6a2SMVqMsmdK3d1otRXAUhTFHXvaKpJgk5m3A7w_HAb-r_COrHO3Y-Xi_LitKncoKyNeWSkclWIeg3t3AICfgSOiZMxXPvsj0jvXHrKx-9VcX_abHHJgpuwdrGj1jn0AR7-kOHi1AYKfOL38oEyp9uXSgNdDMyDqlByt2L_5fSxz5JBw2l0WUqE99EcKE5yuhBqOONIh5hSYWUFcf00BcOIIavPmZ0th3SAbY37FOyp7ICEhsE9HS7BfT1KcDVe7hHdNV2MPFefqpMq8LuEvX9QUKP0oLTtGVj2jP71nhewXxGLSwi3jHXqqTEswlvjIEuaM1k5PB4RZEWa_N42XohqGRm4eEiebrN04xyvkk2NkrxDpPLVlZ_HwBRq66-pcPZq9cG0ThnKZFLcHSH-V07Qn3ATes_3oihJsx1FF_uMmrWzINHaLsVOmbkUkhIZB-2eqDHZq8iiNC-oaGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aed34ebad0.mp4?token=UFhCoCf6scwt3AQilSCqlgrbYUmPOOtFkgAZS5LVZ3qE75uWdADBxGCgAf4HxPi2vc57iC7cc9bqe5rKLo1ZzqMuxdOgzgOYEjS1plYyaQYcrPOe2DfzgARgCCC-VKgni9dUv5wUEzEMWp8jv6_a4kZ9W9kMAgL5c0jeEgtSoXLx8QQt8F_w2gX6tbgxDju-ZYs11HWajuNx3EqlqFb9MwYgY6a2SMVqMsmdK3d1otRXAUhTFHXvaKpJgk5m3A7w_HAb-r_COrHO3Y-Xi_LitKncoKyNeWSkclWIeg3t3AICfgSOiZMxXPvsj0jvXHrKx-9VcX_abHHJgpuwdrGj1jn0AR7-kOHi1AYKfOL38oEyp9uXSgNdDMyDqlByt2L_5fSxz5JBw2l0WUqE99EcKE5yuhBqOONIh5hSYWUFcf00BcOIIavPmZ0th3SAbY37FOyp7ICEhsE9HS7BfT1KcDVe7hHdNV2MPFefqpMq8LuEvX9QUKP0oLTtGVj2jP71nhewXxGLSwi3jHXqqTEswlvjIEuaM1k5PB4RZEWa_N42XohqGRm4eEiebrN04xyvkk2NkrxDpPLVlZ_HwBRq66-pcPZq9cG0ThnKZFLcHSH-V07Qn3ATes_3oihJsx1FF_uMmrWzINHaLsVOmbkUkhIZB-2eqDHZq8iiNC-oaGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست : من دنبال بمباران بی‌حساب نیستم
- می‌خوام بمب مناسب، در زمان مناسب استفاده بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136509" target="_blank">📅 01:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136508">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O71v94k5NuUlcHWa8mtpd1xem9NRaPcS7r7oRUs7gYsVWKJFZ5XElfV-HUDQA21aHc2QF0931X44AE7dWgroCKJG1z3ok6BAJOhLRBwhgc-87ywZC0WNq18CcVMN4JmZrozTvr2HkpPO9X8fRqvA6qmRWV31eYigRMRbPygpveD3_efQ4ygRspqCR-7bVI4oO0O-A0oXvlyw4AwJvjeakpBGRUZGkCQy7BzGgXysUCQ5AS1AdlUJ6DeRoNUprosudFQvNsESsWP4wdc0kTodMoVqNL6oamVqHxXULqpVBpjocuyBKB3UkoUEkJRUmcU28IB1TFS6cPxNFkAZPn5Dpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از تاسیسات اتمی کوه کلنگ با هزینه ساخت Nمیلیارد دلاری که بزودی نابود میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/136508" target="_blank">📅 00:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136507">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967f594caa.mp4?token=htNojYV1GtP0mOKBBfyROfhGHTTHJb5gRT_qnA0uT2AL_tVCm9zA5jI6k_Dph1VK6oUcEgDV59uWkecZe2A3JoMZ52VB1lVfQ0nfWLPoo8VKcEQx5VBaFfJQ3aTEBQuUB7pUe0TD23KmkkECWgRt1EpWYl7D0KApRRU38ev-PNJ0Sas8NjpsP2otBTV2Nei73rkAcWA8DQR9W-gB9wXNESPaFbOIK6nWENKQW-56w4DcPLLqkm71xD_0aiP5yxbwRpROPWH0ZSV0XkA8zhl69EFHxE34aBQnzvMBWl7S1O_6pTV0F2N8vWY66kpLtc0af65dF_wshzNdxoYBTp7CWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967f594caa.mp4?token=htNojYV1GtP0mOKBBfyROfhGHTTHJb5gRT_qnA0uT2AL_tVCm9zA5jI6k_Dph1VK6oUcEgDV59uWkecZe2A3JoMZ52VB1lVfQ0nfWLPoo8VKcEQx5VBaFfJQ3aTEBQuUB7pUe0TD23KmkkECWgRt1EpWYl7D0KApRRU38ev-PNJ0Sas8NjpsP2otBTV2Nei73rkAcWA8DQR9W-gB9wXNESPaFbOIK6nWENKQW-56w4DcPLLqkm71xD_0aiP5yxbwRpROPWH0ZSV0XkA8zhl69EFHxE34aBQnzvMBWl7S1O_6pTV0F2N8vWY66kpLtc0af65dF_wshzNdxoYBTp7CWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست: ما این جنگو شروع نکردیم، ایران 47 سال پیش این جنگو شروع کرد
🔴
پ.ن: ایران‌ نه! یه مشت عقب افتاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/136507" target="_blank">📅 00:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136506">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
هگست :
- ما دیگه وارد جنگ‌های احمقانه نمی‌شیم و دنبال تغییر حکومت ایران هم نبودیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/136506" target="_blank">📅 00:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136505">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
بیانیه قرارگاه خاتم‌الانبیا:
آمریکای جنایتکار مراکز هسته ای و حساس ایران اسلامی را تهدید به حمله نموده است
اعلام می‌گردد چنانچه ارتش متجاوز و تروریست آن کشور وارد چنین مرحله ای بشود، آن را به عنوان توسعه جنگ در منطقه می دانیم و همه منافع آمریکا، هم پیمانان و حامیان آن کشور یاغی و شرور، هدف هجوم قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار خواهند گرفت.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/136505" target="_blank">📅 00:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136504">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">💢
فوووری/۵۰ هواپیما سوخت رسان آمریکایی در اسراییل مستقر شدند
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/136504" target="_blank">📅 00:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136503">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwM0n920otYpHMGm38kcB61dVRmICw-7u8TT7SFxKiSDxzbvFUga-oNbY301ANBZ2yxfr63-TGgj748su5QTYTdZ9nxx5cuxJhv-cNIG6i_7donUPZ5X3IkGOBDsXPpN3sBaFnhhiMOL0bRtEqNu-EcbqIqhQ5LIt7kkqWMJv4fYZcQ2LCerJrRmf63LQ_UUhCvpE9vezSHRGaCz7PWpsAuUF3uEgJoGFVnr-uJG70B5_gDHZ1EGEHdpBGfZBZGBekAMmfrznEAhfLnA8s4y7utGetqGfeK7uNlj98byo4PGFSb-MwCz8YDwogFr9zAzyhm_9DEdM2qWlYraGRM2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش چشم: آمریکا توان حمله به تهران رو نداره برای همین داره جنوب رو میزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/136503" target="_blank">📅 00:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136502">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سخنگوی هیأت رئیسه مجلس: دولت پذیرفته است که فعلاً هیچ‌گونه اصلاح قیمتی در حوزه بنزین انجام نشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/136502" target="_blank">📅 00:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136501">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDqTR35M3tg6lO2x7a27eOkMSRPn0YgnjN6eJYlwWzRRgR3-G0Evdj2GlcxmkpWxwyFCjjIAuvssusD5Eywy3PmyqZkTZe8piDVjUcxIMCr74YTH_Q2pbU6xnAXpZofEoTHJgi7xnhm3VYlZ4Ev3REmzPx2He_UgzDbGlceFfiw1qX679zigsTm-fdHbQQ2Fhd3w0NhfVgbIn-L8uJndqEYJK4wb7jRlC5RHsvZm2tZ8L2NaKEbUcXR_exg54zULUEUpaQTmevjpujdIrO8I6w5PP6dY7UpJ3rG7Z5CaH8n77JWywujBKItCoQtww6gzKqlWC-WO2MPnYWztOWfUXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۶ فروند هواپیمای KC-135R/T Stratotanker نیروی هوایی ایالات متحده بر فراز اسرائیل و اردن در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/136501" target="_blank">📅 00:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136500">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: روسیه و چین در سطوح مختلف به برخی از فعالیت‌های ایران کمک می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/136500" target="_blank">📅 00:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136499">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: روسیه و چین در سطوح مختلف به برخی از فعالیت‌های ایران کمک می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/136499" target="_blank">📅 00:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136498">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79ff20b1bd.mp4?token=kjEjTMTiEPReNn5SnaFqSOz_qIaIJEfWiXbIpanqCpz5mic-tPZUqXFFrsFT_iYdaytUkNr1YN-J-4oOuGnKHPZLsoMp70ThcHxpxJKMckv7iOEqitJNBybvTqZfSNFsN7HELZBjywDb50SQc_ced9eUNO27LYYqNSvtNiXMPjKE_jfVbkP09mrz6VlQKVFXvoJIFfNMRC5FdWa79-Y3Ir8JOL-Sa74VNxPF8vdyJdxOXGiX2nen7Dp19uP2u5FxSsY59sI1263yMtopVNNyugojLXZioKJw-bihwL3bwcTHnKYTyoeggA2Ist4GeuDX9mXhtFclOCWdLkkVXaZToQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79ff20b1bd.mp4?token=kjEjTMTiEPReNn5SnaFqSOz_qIaIJEfWiXbIpanqCpz5mic-tPZUqXFFrsFT_iYdaytUkNr1YN-J-4oOuGnKHPZLsoMp70ThcHxpxJKMckv7iOEqitJNBybvTqZfSNFsN7HELZBjywDb50SQc_ced9eUNO27LYYqNSvtNiXMPjKE_jfVbkP09mrz6VlQKVFXvoJIFfNMRC5FdWa79-Y3Ir8JOL-Sa74VNxPF8vdyJdxOXGiX2nen7Dp19uP2u5FxSsY59sI1263yMtopVNNyugojLXZioKJw-bihwL3bwcTHnKYTyoeggA2Ist4GeuDX9mXhtFclOCWdLkkVXaZToQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
آه مردم ایران بد یقه جمهوری اسلامی رو گرفته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/136498" target="_blank">📅 00:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136497">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953ccf337f.mp4?token=DEGlQO2VnCZydkrDJgfslJacHUACYqEQlKnUTsUdwwgsrB-waAqJ1jFiyaF222AINHH-ttGB3PUP_4fTUmv7iQwcBjci6Nt4cmmJHp7ueQW1UFdUWeKf_a9g3uowim9ejr3sdrpaHQPfce0i6i9RVFtJ1A123z1ryTK1NwFQ9JJq8y7UnCXdTRwNWvN2Ee6V8H-nCGM8-BukVCCGF1AoFxkgTwgvQvDJZek7BHyVa_e6r8Ut-tQ-kSikav3GQNDg8wPkXRnNS_JqdUKOREF9__9IHapXEZDW-5edtu51ajppC04apQJG5jel3vS8PFeGBAuoXOQZCRJOSFBiS6M6TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953ccf337f.mp4?token=DEGlQO2VnCZydkrDJgfslJacHUACYqEQlKnUTsUdwwgsrB-waAqJ1jFiyaF222AINHH-ttGB3PUP_4fTUmv7iQwcBjci6Nt4cmmJHp7ueQW1UFdUWeKf_a9g3uowim9ejr3sdrpaHQPfce0i6i9RVFtJ1A123z1ryTK1NwFQ9JJq8y7UnCXdTRwNWvN2Ee6V8H-nCGM8-BukVCCGF1AoFxkgTwgvQvDJZek7BHyVa_e6r8Ut-tQ-kSikav3GQNDg8wPkXRnNS_JqdUKOREF9__9IHapXEZDW-5edtu51ajppC04apQJG5jel3vS8PFeGBAuoXOQZCRJOSFBiS6M6TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معترضان ضدجنگ در جلسهٔ سنا، سخنان پیت هگست را قطع کردند، آنها می‌گویند: «بمباران کودکان در ایران و فلسطین را متوقف کنید!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/136497" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136496">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/136496" target="_blank">📅 23:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136495">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76819af5e7.mp4?token=QtENzswrRdsGMzpzH4Ctg6PHg56QTyZeH5HrR8pn0A6goiP2mjpLTwVI_qmA83yTSHpJONwlALxQG1Z9nMIRKzMk3Tn7zYXWUUYRuH472ERLFpVzBhTr7AtQC-nt0zZLMcBznq0-om43njVoccJcAGhar6848bK-7Ek0Yt5dbKMi7Da2b8u6jv9LzBtQzI2dJOtckF9mGnTCpBBzZ0eFnd4PSV6NYMvKD6U_TiJpLXTaxfU6qazQMKpN7GW03c7DjYoQEtM1f85xhzbRMWUTz-iNiQmt_7KigQWg-CBHSlTSav6YR0hYdtV2inXQVmuVDSdkq5KQ9of0MStb_wZ_Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76819af5e7.mp4?token=QtENzswrRdsGMzpzH4Ctg6PHg56QTyZeH5HrR8pn0A6goiP2mjpLTwVI_qmA83yTSHpJONwlALxQG1Z9nMIRKzMk3Tn7zYXWUUYRuH472ERLFpVzBhTr7AtQC-nt0zZLMcBznq0-om43njVoccJcAGhar6848bK-7Ek0Yt5dbKMi7Da2b8u6jv9LzBtQzI2dJOtckF9mGnTCpBBzZ0eFnd4PSV6NYMvKD6U_TiJpLXTaxfU6qazQMKpN7GW03c7DjYoQEtM1f85xhzbRMWUTz-iNiQmt_7KigQWg-CBHSlTSav6YR0hYdtV2inXQVmuVDSdkq5KQ9of0MStb_wZ_Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست: ما باید دونالد ترامپ رو بخاطر شجاعتش تحسین کنیم
🔴
اون نمیزاره گروه های افراطی اسلامی به سلاح هسته ای دست پیدا کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/136495" target="_blank">📅 23:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136494">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
وزیر دفاع آمریکا: ما در حال حاضر محاصره‌ای مؤثر علیه تمام کشتی‌ها و بنادر ایران اعمال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/136494" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136493">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-2LgnMZBaaLEfu5ISeD4lAemUdXk2rBrHq35E8FRAABvsAKj6HeAaa0oAt2OrpjwRcFQokXCndd9OwNzWm0cAwVEli_N-zb_dv08RRToq7pJdehpzbZfF82ym1YhKsmHdmhFRt0JojwxBYCGLXHfSR6B_hCT5hHOee5D32gXrlZ6-5YYncsPOqCM61BimUwVDWJn_NUBFihf4HnBPlVnIEOZvHqxtQxrNg-vhPUJ8_YH49V05U0LHwZ1rjejd8PaD7QaL5mwO-SI9hCDsWoZa4GPBV1njAPeJGNmy3t9Y1g6qkSfwZdPstNcO455TjxCknpKFtdGOt1n3MRviSfUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۲۷ درصد نفت جهان از تنگه هرمز، ۱۱ درصد از کانال سوئز و ۱۱ درصد از تنگه باب‌المندب عبور می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/136493" target="_blank">📅 23:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136492">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/atvFK_kWTtlnfDh8kJIayreunHiXGhELeoOwdhnK2VDp4FV_rqv4tXwXbuIm8JZlHIF03qf-_za8o89FlB3_4GZH0WxsI1XjK4YXPJ3kis-U0cZxS53bdVJtDcXTRJavNCV7oU0yWJiX_tVZDdDy3ZTxXOQOhMKO4h2ZgzO9OlquZV5y1yf-fX7piaiEov3S8J1llkgDxln71iFNEV-qGrXjMt8rFKsYMdNWEnx96UK28g3T2nc_GH3UsPtt-47KvSxgTzA9dB940ODBeYqHq0kI71lgj_wr6ZJgl7dbE2wCKO5MeXv5lmsXKqeT5F_CUoMUE6ILIuOMxATx42P3DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای E-3B Sentry AWACS آمریکا در آسمان عربستان سعودی
🔴
سعودی‌ها بارها مشارکت در حملات به ایران را تکذیب کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/136492" target="_blank">📅 23:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136491">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
هگست : جنگ در ایران برای آمریکا حدود ۳۷.۵ میلیارد دلار هزینه داشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/136491" target="_blank">📅 23:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136490">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRzJGsKvbl1U66cHtf6HQVO7BueERNRSCotx5sLDjeuUoFheh9FNsGtJEf4p-EInqPJAeDegTarAQxOvpjPmuvjwTDSvhQvcO-zmR9VwL9ElOa-FCx_vmfxU77SzZcgYSJ4dnh3i2E1Yl8_kxP5vzfoCzntU03MOsmxJTG8Pmmr7knf59tLULBrgMjxcX1MaJ7VjbdtUKS9KHAq3eL8iQYzJbVRkaAJ1IqFUDZxZ8Qfk722suM6DVW19L2hx5nInq7RoraoWont-UESCbiJcw-Eo-VSOcZOsCzeWCcV8HGPitRev8_MTzjL2HzmH1_74Zd6ccGP-hVuCVpWZBqvlpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
🔴
جنگ در افغانستان: ۲۰ سال، ۲۰۰۰ کشته.
🔴
جنگ در عراق: ۹ سال، ۴۶۰۰ کشته.
🔴
جنگ در ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
🔴
جنگ کره: ۳ سال و ۱ ماه، ۳۶۵۷۴ کشته.
🔴
جنگ در ونزوئلا: ۱ روز، ۰ کشته.
🔴
درگیری نظامی در ایران: ۴ ماه، ۱۸ کشته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/136490" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136489">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29916de006.mp4?token=H357Iu0z5kp14kPnF-w6Nm0UOACgIDrSQA65O37LyxI-sLDoNwJuiqWYC7V1NVxrBxpo2-iUdKSiQnG15yCqagGqVSCHBk7ICBi-yazs3JHLMaSw3_2T396Em2BjUorl2HDONOW0xNpd7whMKFL4lo8CnGRNRCB40brsUU-SEZs2YkOHu74fWlYYQhygg4-YJn3GGqsg9EtW1We-_ZEAh-66N-up--wvRz3zGtY3mV1tbLNbMvGJXoXDwWyqf6V9xzAmt-vf7bWd6rhLj0dT0a_r4jU5phC0m-FYVLg4RP4IgOu83X1npkQA19K4RcV6p5iemLHN4oman9sqUu2V_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29916de006.mp4?token=H357Iu0z5kp14kPnF-w6Nm0UOACgIDrSQA65O37LyxI-sLDoNwJuiqWYC7V1NVxrBxpo2-iUdKSiQnG15yCqagGqVSCHBk7ICBi-yazs3JHLMaSw3_2T396Em2BjUorl2HDONOW0xNpd7whMKFL4lo8CnGRNRCB40brsUU-SEZs2YkOHu74fWlYYQhygg4-YJn3GGqsg9EtW1We-_ZEAh-66N-up--wvRz3zGtY3mV1tbLNbMvGJXoXDwWyqf6V9xzAmt-vf7bWd6rhLj0dT0a_r4jU5phC0m-FYVLg4RP4IgOu83X1npkQA19K4RcV6p5iemLHN4oman9sqUu2V_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر هگ‌ست، وزیر جنگ:
ایران از نظر نظامی در ضعیف‌ترین نقطه‌ای قرار دارد که تا به حال داشته است.
🔴
من اذعان می‌کنم که آن‌ها همچنان از قابلیت‌هایی برخوردارند، بدون شک، اما میزان خساراتی که ما در طول این مجموعه عملیات به آن‌ها وارد کرده‌ایم، آن‌ها را در بدترین شرایطی قرار داده است که تا به حال تجربه کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/136489" target="_blank">📅 23:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136488">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/695fafa7f7.mp4?token=k8eA0_8GKNUCvlMzv5f2p6BG4WtrAHUQC9klwZIJtteiVHx-q5AuSVlV5ctFIuT8W4r1UABaLrMYRpbDLLJQpyudYA6FWzprUnl5Pci30KYFuE66pS0sNqNvG-L-tlUGTiDuWNX0vj97D2zfjPFZGkDK-577AC0dhkYgpY-bqpPkv9YNH-2Opprz3FOYFM6uOJM01MDZvYyAPsjNsNQD6a45KHwWhW_AXjCQ8_diPgt_nPnIWFc4bZ_Hy0sRCVFy6yhEuNzWTzdBJXt7bricaVReCyhUPokEasCP8LwE6wdpPhMGlPRMsenwk21Bl8iyxouSMIMPBwYOvxIo6-iXSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/695fafa7f7.mp4?token=k8eA0_8GKNUCvlMzv5f2p6BG4WtrAHUQC9klwZIJtteiVHx-q5AuSVlV5ctFIuT8W4r1UABaLrMYRpbDLLJQpyudYA6FWzprUnl5Pci30KYFuE66pS0sNqNvG-L-tlUGTiDuWNX0vj97D2zfjPFZGkDK-577AC0dhkYgpY-bqpPkv9YNH-2Opprz3FOYFM6uOJM01MDZvYyAPsjNsNQD6a45KHwWhW_AXjCQ8_diPgt_nPnIWFc4bZ_Hy0sRCVFy6yhEuNzWTzdBJXt7bricaVReCyhUPokEasCP8LwE6wdpPhMGlPRMsenwk21Bl8iyxouSMIMPBwYOvxIo6-iXSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر هگ‌ست، وزیر جنگ: پنتاگون دیگر توسط کارمندان دولتی اداره نمی‌شود؛ بلکه توسط نظامیان باتجربه و مدیران برجسته کسب‌وکار اداره می‌شود که این بخش را مانند یک شرکت اداره می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/136488" target="_blank">📅 23:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136487">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
بحرین: هدف حمله جمهوری اسلامی به منامه سفارت اسرائیل بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/136487" target="_blank">📅 23:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136486">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری / خبرگزاری کان اسرائیل: نیروهای احمد الشرع، رئیس جمهور سوریه، در حال آمادگی برای حمله به حزب الله لبنان هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/136486" target="_blank">📅 23:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136485">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvLz1kUwLsID-_eShgRlyIP3vbriLOx9JVPu8bfNWHYVgKxAPRNdhbu-I9Bbpu4UO2I9St0TNktPlOHoVwk9OaQ3hcfwFx8MxI7vLREvEWACHS45rCBN6V1hSR4u4g87Iw4Zq28RK6YV7L4OdiqPmgZpzxqpnYiRtPAUEGAe97BZQIEtPhueXZDVnd_UGXhgAfj1Sh97RB4u-fGEN2tazZvBNRodr1BbrjcMOlfa6VLLs64darQ2OPr9ScdNwlJ15qRcn1bj8BxXIvnEwK-XlAwz1VmYMMxxykrwcTkLYHf_FEKS0BCwQ97GhKsi-QlkgF3SBLY426i82JkuXhUdXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: پرواز مستقیم شرکت‌های هواپیمایی آمریکا به لبنان از سر گرفته می‌شود
🔴
دونالد ترامپ اعلام کرد: «به دولت خود دستور داده‌ام که به همه شرکت‌های هواپیمایی آمریکایی اجازه دهد پروازهای مستقیم به لبنان را برقرار کنند تا شهروندان آمریکایی بتوانند به‌راحتی از این سرزمین زیبا دیدن کنند.»
🔴
او در ادامه ابراز امیدواری کرد که سایر کشورها نیز تصمیم مشابهی اتخاذ کنند و در پایان گفت: «از سفرتان لذت ببرید!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/136485" target="_blank">📅 23:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136484">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
منابع ایتایی: در صورت حمله به کوه کلنگ، ایران تاسیسات اتمی در نیوجرسی را هدف قرار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/136484" target="_blank">📅 23:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136483">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_yd9zJ2Ia0uKGQkLtNE1bzE8PDEcZoSV2_LxYoIU4TCa-0tQifO8J19_YkB4TmdrSE11sQCONFJpjbyLvssVzy6OSrWYi5tHCfbF33eZQIDagDnkW76nWbYiNZYwQisz0hLaFvoH0-lBlRMz15KhR4hGB69JZExD8KCErTCHixqkvF_gQhqltmqwDsG8toaq6kjIWkGQ-HdnGTTux_5gcgg4HGo4T8zJ2gMTBTNEiupgep4im23lFpaCtk5pWCgG_5tSdLyJAC9qBA0zSGsSYtUac0-A2wK1wtbjhzTZ9BXgf3IFV8tGKA7xw9sIoO1jfVNrgAeM4POUCLwlJ7fwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: بعد از دیدار با رئیس جمهور لبنان، دستورالعملی صادر کردم که به موجب آن، به تمام شرکت‌های هواپیمایی آمریکایی اجازه داده می‌شود تا پروازهای مستقیم به لبنان داشته باشند تا مردم آمریکا از این سرزمین زیبا دیدن کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/136483" target="_blank">📅 23:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136482">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سپاه مدعی از کار انداختن چند رادار تاکتیکی در کویت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/136482" target="_blank">📅 23:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136480">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4wjZhpPhIjvafDpAcDuZJKsI10aBeqt9Q5eNfJBCbjOfa1OLm_B1dftRIN1jAy1n-dCLNK5KBOhOK_hFxQKln5w-rDQDzkEX375BMHfgNT2Dbi4rrtdJw3IN01LKJkfVXjmKTdafKkSrYfN0o8qhvoUDtLMkvwQJumocjQet-6vVaHi_KczY3HHcmzmrMJYBb04NrAv2oMRuPIaeS7ERqHDu0jgsyly4CSeMi9DwP56tX7E3R8YoSsik_w82rPyoJL1N3lnqZvCnLJUfABjfa3ylAZ4yBCjr8EfhNOeeA2IxC8Oi4PXe3FeHN9zMRza9iApBv6PZcAX0C-Y1gcoCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/alonews/136480" target="_blank">📅 22:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136479">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/136479" target="_blank">📅 22:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136478">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری / نخست وزیر جدید بریتانیا با استفاده از خاک بریتانیا توسط آمریکا برای انجام حملات هوایی به ایران با استفاده از بمب‌افکن‌ها، موافقت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/136478" target="_blank">📅 22:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136477">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
برخی منابع ادعا کردند که امشب آمریکا به کوه کلنگ حمله خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/alonews/136477" target="_blank">📅 22:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136476">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
فوری/گزارش‌ها از پروازها تانکرهای سوخت رسان اسرائیلی برای اولین بار از زمان پایان جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/136476" target="_blank">📅 22:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136474">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سپاه پاسداران، بلغارستان، یکی از اعضای ناتو را تهدید کرد و گفت در صورت اجازه بلغارستان به آمریکا برای انجام عملیات علیه ایران، این کشور را شریک جرم آمریکا دانسته و اقدامات لازم را انجام خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/136474" target="_blank">📅 22:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136473">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری / ادعای کانال ۱۴ اسرائیل: پرزیدنت ترامپ، گسترش دامنه عملیات علیه ایران را پس از حملات اخیر، اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/136473" target="_blank">📅 22:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136472">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
کویت سفیر ایران را احضار کرد
🔴
وزارت امور خارجه کویت : نفتکش «کیفان» عصر دوشنبه هنگام عبور از تنگه هرمز هدف قرار گرفته و در پی این حادثه چند نفر از خدمه آن زخمی شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/136472" target="_blank">📅 22:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136471">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yma0cWwvWPJj3lRtvwmNnA4pkCRaMPl9ijixu0t-lIvb9fzY3I2AxCooUtrwGeqavL86IcwMzxiyfExO4q0hWXQOH0NFbFDEf-lkng5jogUdOMp8sGUNHIY7wxmWm6WjE-bGpWcpJgwG9NN82y0rqkxQ5mLx8zNqaDYbJVsHIcBtMBp3mGrZk2_e20YA08b_gKDIb27tVQiGuus5zAtdu0lvVcE3lSAPGAp0q2MIfz17VIxjiPJdQn-XCznSgMnguvIvp_d1_yzvORNX7mkj-KPN0S4AEjPCe2d8a-yWempsrS9piyLWLZnke922juCglhZ4MJ_TMxtNOZe2QlYmgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش i24NEWS می‌گوید که OpenAI در حال گسترش فعالیت‌های خود به اسرائیل از طریق ایجاد حضور در توسعه کسب‌وکار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/136471" target="_blank">📅 22:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136470">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgHKrwTSgNH7gLiFzZfL0DTETIX3xNs9t1psBdVlAnEoHVz8SEpBi209UkPrAF0fAKWOYXb4ozM-l_eyTtFTcZHlAm8tQA4oPeM_7-e4_SqfMIbCkkQ9O-53aRg2As070v6vqNGZgNTq9mMZ_EHlZ4JntUY6hyFe6EnuYMYWLsqYYtOY4-ZbIcGVn8-zy2pe8h98b95JZew60rJShcMCwWgd_AGy4M1qJB9H2iy4cBJdh5jo7-P0pjc9_yHB_GOuxU4tIeD2pg5Idz9UEgzM4zPXh5VpJfRH5mGfb7GhgeocMo20tUX29NEJNl-7XB0zHg4LxTBD_huVuKngcjudDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۲ تانکر سوخت رسان آمریکا از رومانی به سمت خاورمیانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/136470" target="_blank">📅 22:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136469">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
طبق گزارش رسانه‌های دولتی عراق، فرودگاه بین‌المللی اربیل به دلیل حملات پهپادی ایران، به طور موقت فعالیت‌های خود را متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/136469" target="_blank">📅 22:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136468">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل در خبری فوری از وقوع حمله احتمالی در اطراف سفارت اسرائیل در پایتخت بحرین خبر داد
🔴
این شبکه مدعی شد گزارش‌های اولیه حاکی از آن است که سفارت اسرائیل در منامه هدف قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/136468" target="_blank">📅 21:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136467">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dad9abeee3.mp4?token=BO0MK_fM9TAtZ6ggUf2-AxpKItbXJIRXOX1gEpaL8Q0Os63OuM1daNi1UfYbm4aSyLUj2fZMvMVOEdV8zMJsFoZ_ULOjr5e1sVW94Prc2UQ1y4vzG51__GeK42MOUXGubJp9Ivm991rM9ysbVDCUQOo-1vTIRJ_hITPH3F5Xsn53Iyoc9Os4_B0WNWhlT4ySLSy680QBV6Dxj8MZuHz4p35Znz-D4qHXTdo6DgxuoAaJ7rj4pQomjPxs1Ra-dm8huBFGfE8e8TaSuUd2dRU0XqMgeK91eBavQWZEm6TDR327cH2iQrxz1wGL0adtu1vfYXgbsQbgJRIsvve4Bizk0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dad9abeee3.mp4?token=BO0MK_fM9TAtZ6ggUf2-AxpKItbXJIRXOX1gEpaL8Q0Os63OuM1daNi1UfYbm4aSyLUj2fZMvMVOEdV8zMJsFoZ_ULOjr5e1sVW94Prc2UQ1y4vzG51__GeK42MOUXGubJp9Ivm991rM9ysbVDCUQOo-1vTIRJ_hITPH3F5Xsn53Iyoc9Os4_B0WNWhlT4ySLSy680QBV6Dxj8MZuHz4p35Znz-D4qHXTdo6DgxuoAaJ7rj4pQomjPxs1Ra-dm8huBFGfE8e8TaSuUd2dRU0XqMgeK91eBavQWZEm6TDR327cH2iQrxz1wGL0adtu1vfYXgbsQbgJRIsvve4Bizk0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در نزدیکی شهر اربیل، واقع در شمال عراق، در پی سقوط پهپادهای ایرانی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/136467" target="_blank">📅 21:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136466">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc1fb8bd4c.mp4?token=MKW8YYCt3riOAtvRaL1bzSPGkEmjA5RHCDqWquB46Q_LhIn2HIAxtZlUKToOV5_Q1v4d-2bDR7x64WDiwpLT5DzJwGRIUvY5X1ti5Z6vECSdA8KQlayRtKw8dM1CfBzpc9itsbxVkN_Tm8O78gpFW25u2hvNUVO8DlQF33KqlM4-5Wg-6ydj-PQ8OJpoPUmBnyA5VVCGfjJm0__mdYLBNHehyJu3Ve54T-3vSNfHassOY-MYLOWndpQehfEBBDU3El-ymCrKYntGeNdYx9VQxfFnNZXjo-j-s5UdMiNAC1675QpXICD_mnQYKO9jxJLrf0DMxZDDGjagJfx0YLXjJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc1fb8bd4c.mp4?token=MKW8YYCt3riOAtvRaL1bzSPGkEmjA5RHCDqWquB46Q_LhIn2HIAxtZlUKToOV5_Q1v4d-2bDR7x64WDiwpLT5DzJwGRIUvY5X1ti5Z6vECSdA8KQlayRtKw8dM1CfBzpc9itsbxVkN_Tm8O78gpFW25u2hvNUVO8DlQF33KqlM4-5Wg-6ydj-PQ8OJpoPUmBnyA5VVCGfjJm0__mdYLBNHehyJu3Ve54T-3vSNfHassOY-MYLOWndpQehfEBBDU3El-ymCrKYntGeNdYx9VQxfFnNZXjo-j-s5UdMiNAC1675QpXICD_mnQYKO9jxJLrf0DMxZDDGjagJfx0YLXjJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌های انتحاری در حال حاضر در آسمان اربیل در جریان هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/136466" target="_blank">📅 21:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136465">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb8d1b726c.mp4?token=YHeHsQ5y53fMrybMuJrtmNPTT-4ew0W471KzN62SmvlB-qvkyxVi1fnXBKD0PWFo5lgs8qDMfLbszMJX-tZyr43duyErhkeukCjp0gYj-POZxIarnEQEIeEIxherDJQULbKLMnmxoUahBGnhPsos6VjYG9MYJFepC_71sqX45n0kW6pmiFDux_oVv5-vZJtCEavl7G0OtOCH-xf_XFkJw7ZEnLu3oagLoFQKWfszUU7gezhVedxM9Tx-g4YARmxtDOmsIV2Nk3Jn901762WNgpchInZ32m3cp9dwHZ5KL-wJ8xhdszx9X97lrnqXGWFwb4nqOpmoFZiJ2QQJzIIHYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb8d1b726c.mp4?token=YHeHsQ5y53fMrybMuJrtmNPTT-4ew0W471KzN62SmvlB-qvkyxVi1fnXBKD0PWFo5lgs8qDMfLbszMJX-tZyr43duyErhkeukCjp0gYj-POZxIarnEQEIeEIxherDJQULbKLMnmxoUahBGnhPsos6VjYG9MYJFepC_71sqX45n0kW6pmiFDux_oVv5-vZJtCEavl7G0OtOCH-xf_XFkJw7ZEnLu3oagLoFQKWfszUU7gezhVedxM9Tx-g4YARmxtDOmsIV2Nk3Jn901762WNgpchInZ32m3cp9dwHZ5KL-wJ8xhdszx9X97lrnqXGWFwb4nqOpmoFZiJ2QQJzIIHYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آسمان اربیل‌عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/136465" target="_blank">📅 21:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136464">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
فرودگاه بین‌المللی اربیل بسته شد
🔴
منابع عراقی گزارش دادند بر اثر حملات موشکی و پهپادی اخیر در اقلیم کردستان عراق، فرودگاه بین‌المللی اربیل بسته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/136464" target="_blank">📅 21:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136463">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhqeZL2uQXLmajz0gPs8DOw2nAbXVIemzUlXAHaQnYx9n79vJJSaxRSPCfjNBJn1JxXBFnIl2vJpZ3Y20MQwT5uWgFIBzkvw74cAjvSB-CVViK0XtoAaz-faBpxliz3iPMqygxID_7r-VWCgVpuS0uHOq81DrJPvCA-NvYaBegcqictJNRg7bydmvWILsO_zKePY1POjJfvmGIcL-3PH_QxbK42SS8iYS8_IHNd_imoyNAY1-40-5p1hJ7AwK2fysjAgHVPRbIZO_7iW9-piyKZwDx-ky0rLTRzToGMwHKquqNTSVN_g8hKFqmjntEUuQ-x7Y1MjcMMZrqihhhpdOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد رآکتورهای هسته‌ای فعال در کشورهای مختلف جهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/136463" target="_blank">📅 21:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136462">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سخنگوی ارتش: اجازۀ نزدیک‌شدن دشمن به مرزهای کشور را نمی‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/136462" target="_blank">📅 21:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136461">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از منابع امنیتی گزارش داد که سه پهپاد حامل مواد منفجره در نزدیکی کنسولگری آمریکا در اربیل، شمال عراق، سرنگون شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/136461" target="_blank">📅 21:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136459">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b0e9aeb4d.mp4?token=ibwDyDcenBz-2BIi_UgCeeec8_x5yC72Q4bEw-Xbh8wYk1-fgtjp_emqW_Uq4biB-UpPiWYMRggcQ5fIyuKSMqhHJoieI7UOOGxL7LUKlKIm28JWfi2GZ_OGC-Q4zqcyfq3IcK4B7PCJkDm_ktOdI84DDnEquwADki4X2OdV5DJgvXifwgg11EVXRFrX2JG60ujZI8LSaSWALDk81kSQUzj91044liJ1yeg8MJCM9jnrk2dQk2wjRnejeFJKrzswAfGNBRHZk-NQp-RwAMrZdTl-ogbMV_YgZdd75npWA8KXr7gkqnuN7Y8ZSiifGGpA5somOT4r-zUCCs0TtVFMxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b0e9aeb4d.mp4?token=ibwDyDcenBz-2BIi_UgCeeec8_x5yC72Q4bEw-Xbh8wYk1-fgtjp_emqW_Uq4biB-UpPiWYMRggcQ5fIyuKSMqhHJoieI7UOOGxL7LUKlKIm28JWfi2GZ_OGC-Q4zqcyfq3IcK4B7PCJkDm_ktOdI84DDnEquwADki4X2OdV5DJgvXifwgg11EVXRFrX2JG60ujZI8LSaSWALDk81kSQUzj91044liJ1yeg8MJCM9jnrk2dQk2wjRnejeFJKrzswAfGNBRHZk-NQp-RwAMrZdTl-ogbMV_YgZdd75npWA8KXr7gkqnuN7Y8ZSiifGGpA5somOT4r-zUCCs0TtVFMxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از رهگیری پهپادها در آسمان اربیل، کردستان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/136459" target="_blank">📅 21:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136458">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
بلند شدن ستونی از دود در پایتخت بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/136458" target="_blank">📅 21:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136457">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f99c9d3d0.mp4?token=kyNwiMERP4nckc21djojBi3StYoIPf2nRFxCO7YZlVn_FywI7ryA7lXeRIM-9E0LN6UK4ZF6fgoQXukJ3671p9ktPchscodo6K6-9IhklKadRprBL20_3c1StN2bW04eB0SX-LgjsGEDr-mGLXIu5-jlB5SYaWgPmEjDAfmUVOLOe4XhF4ShSFaFcYMC2JE-pUrEfuImv6JXcXq159UgUQUKNz7BK-oHWAv_uENGRHlROmfQaEhBHfxVz77GEq7afekvoOKxM019ejInFys5ySoePr6p_BhwJv4I1pTerAKqTvLaq5NGFxue6urqbvTD4zs3usD_sth8jGYgNCQPRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f99c9d3d0.mp4?token=kyNwiMERP4nckc21djojBi3StYoIPf2nRFxCO7YZlVn_FywI7ryA7lXeRIM-9E0LN6UK4ZF6fgoQXukJ3671p9ktPchscodo6K6-9IhklKadRprBL20_3c1StN2bW04eB0SX-LgjsGEDr-mGLXIu5-jlB5SYaWgPmEjDAfmUVOLOe4XhF4ShSFaFcYMC2JE-pUrEfuImv6JXcXq159UgUQUKNz7BK-oHWAv_uENGRHlROmfQaEhBHfxVz77GEq7afekvoOKxM019ejInFys5ySoePr6p_BhwJv4I1pTerAKqTvLaq5NGFxue6urqbvTD4zs3usD_sth8jGYgNCQPRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بلند شدن ستونی از دود در پایتخت بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/136457" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136456">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
منابع خبری از شنیده‌شدن صدای انفجار در نزدیکی کنسولگری آمریکا در اربیل خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/136456" target="_blank">📅 21:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136455">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZb6aP1w47Jiw_Fi0oxJ1rz-3TulT5lJxvGvBOWVHjbWGei75j9Qx-nzM7doqgSykcEMX-VzkPOBGUPml3f8DMQpNUJ7dZ-WKCAbk-qT7HCKf-h0wCEmCYtn5l30O7OZOzRvyKPWi8L__bFbDZO3uvbCGB2DMFy5CB8jcNKEAZtBvNVWFwOM7rZxkfZ34Nj9Q6KpMZ5LaeV2PW5JtBhj8yOrIcBNvTmjJLFpcyG30S3jvSA2ffBbeUYnq9PuNnKMuLDyratT3MKJV36qptvEUzN60kdsEDRnT5wRAuijsgCzmxNjF1fmwez2YEU0f54begZNYWAz7TXiRfWutkd13g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت سیاوش اردلان، خبرنگار BBC: ابتدا همه فکر می‌کردند حملات اخیر امریکا مقدمه حمله زمینی است ولی نتیجه ضربات ایران نشان می‌دهد امریکا باز هم بدون برنامه وارد عمل شده؛ یک مقام نظامی آمریکا می‌گوید ما قابلیت دفاعیمان در برابر موشک‌های ایران مستهلک شده اما کاخ سفید به حرف ما گوش نداد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/136455" target="_blank">📅 21:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136454">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l83jJbXMeMTzAyBi45P0dHjrD23hcndKQdUgQsMx7l9LCW93G0YzZ1F4PuljKNfY1kpv7gwZPGq-ibmKRzdLEro1076kRc3U21-YM3z7JjMu2TLHE6BYfYI1_PWavxUOJF4DQT4DDp9pWlXek_rvAz_C861z_9DKB-SIGAJaw53j2AQly5wUYSVfIH6d4I8CNKA8OAUrozuBhq_dqHmSAhsaIlkKctdZR2pqcAdamPE4Q4UZG8G63dpTSKyYlp9kZQz6fsF4hWtTGOxL9Vk4MY6BboRH59WqB88JvyjWAKRyTomUdpaXWnl38IMkh-sAlxjCQSjpR_L23GGRDx3L7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آتش سوزی وسیع در کوه دراک، شیراز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/136454" target="_blank">📅 21:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136453">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f59fef3ee3.mp4?token=O0BYUGlvkD589R-vNngxJu7g4-gvvYwKEK2ncz2B2yLQKo2w7Rd1m4umvOsWv0bn1kNlDTIEJAIGoonZoDACmLE105gBSm8_RJMraQLuMPFdWkBqYbjCXyfSBrI9aaGbmgaLhK5b7AyIixnV2l3qXEZV3GEF_p9VkxvjkkqtqWWxg_FW0bRY8TesEdsy8mTMQVaRp-ofQOb1m7hViba3XHrCH1W-30BV2_L_1rkNfqEfwsJuh6gYNaa-49xUnwdcyOnrlXsTpd8HFl5IEEiEv5eDwgrH4aLF1KnM8mK_WxIvsqk82qNZGSk-wu_fs74L4bN8TvM_zvPiMcCe9kfxDw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f59fef3ee3.mp4?token=O0BYUGlvkD589R-vNngxJu7g4-gvvYwKEK2ncz2B2yLQKo2w7Rd1m4umvOsWv0bn1kNlDTIEJAIGoonZoDACmLE105gBSm8_RJMraQLuMPFdWkBqYbjCXyfSBrI9aaGbmgaLhK5b7AyIixnV2l3qXEZV3GEF_p9VkxvjkkqtqWWxg_FW0bRY8TesEdsy8mTMQVaRp-ofQOb1m7hViba3XHrCH1W-30BV2_L_1rkNfqEfwsJuh6gYNaa-49xUnwdcyOnrlXsTpd8HFl5IEEiEv5eDwgrH4aLF1KnM8mK_WxIvsqk82qNZGSk-wu_fs74L4bN8TvM_zvPiMcCe9kfxDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منتسب به شیراز
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/136453" target="_blank">📅 21:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136452">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
انفجار در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/136452" target="_blank">📅 20:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136451">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۳.۳ ریشتر شامگاه سه‌شنبه ۳۰ تیرماه، حوالی تازه‌آباد در استان کرمانشاه را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/136451" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136450">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
کوثری، عضو کمیسیون مجلس : آمریکایی‌ها جرعتِ مقابل مستقیم با مارو ندارن، فقط هیکل گنده دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/136450" target="_blank">📅 20:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136449">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
کانال ۱۵ اسرائیل: برآوردها در اسرائیل حاکی از آن است که دونالد ترامپ به‌زودی حملات علیه ایران را به‌طور چشمگیری تشدید خواهد کرد.
🔴
به گفته این ارزیابی، هدف قرار دادن زیرساخت‌های حیاتی و مقامات ارشد ایرانی، می‌تواند ایران را به واکنش نظامی و شلیک موشک به سمت اسرائیل وادار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/136449" target="_blank">📅 20:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136448">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
حمله اسرائیل به شهر المنصوری در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/136448" target="_blank">📅 20:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136447">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
گزارشگر کانال ۱۱ عبری: گزارش‌هایی از منابع غیررسمی در عراق حاکی از آن است که سه فروند هلیکوپتر آمریکایی نیروهایی را در صحرای البادیه در عراق پیاده کردند. پس از حدود یک ساعت، این هلیکوپترها دوباره به پرواز درآمدند و به سمت اردن حرکت کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/136447" target="_blank">📅 20:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136446">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
حزب‌الله تهدید کرد که در صورت عدم اجازه فرود هواپیماهای ایرانی، فرودگاه بیروت را تعطیل خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/136446" target="_blank">📅 20:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136445">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70432ee662.mp4?token=jZL5oI-jhLfLE6FJv7M86d4UsOJfaSTgF2-GeCLFlQXKF-Yav4owZX_UwMY6YnKuQnuyEJjmkiGe_zHQuOKDHggzm_qiXaV_j8eBlh4LKrmv3tgx6NJasRS7VxAop_SRkDroPTxuEdsi3_zTlCQqG9vNZfQ6Qlv5JJPusSbDjTZq-Lmujzih8lj0pQ41lh6YJcS0eioCZ6AP0paLCjP61K0Msg3ZaOmq1fCRyeBNOcfoUxCHBqIx_QGfM7w-ELLwxrKG_5MKRHGdhytRdCOgMCFAHkWg76EA_bMmGyYFwOetjYZ7VGGxBFzhpAru_eKbpUmurdVnagXNchrHF1xjLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70432ee662.mp4?token=jZL5oI-jhLfLE6FJv7M86d4UsOJfaSTgF2-GeCLFlQXKF-Yav4owZX_UwMY6YnKuQnuyEJjmkiGe_zHQuOKDHggzm_qiXaV_j8eBlh4LKrmv3tgx6NJasRS7VxAop_SRkDroPTxuEdsi3_zTlCQqG9vNZfQ6Qlv5JJPusSbDjTZq-Lmujzih8lj0pQ41lh6YJcS0eioCZ6AP0paLCjP61K0Msg3ZaOmq1fCRyeBNOcfoUxCHBqIx_QGfM7w-ELLwxrKG_5MKRHGdhytRdCOgMCFAHkWg76EA_bMmGyYFwOetjYZ7VGGxBFzhpAru_eKbpUmurdVnagXNchrHF1xjLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست: ایران فرصت‌های فراوانی برای مذاکره داشته است، تا نشان دهد که در مورد تنگه هرمز رویکردی منطقی دارد.
🔴
اما اگر ایران به حمل و نقل تجاری حمله کند، ما نیز به آن‌ها پاسخ خواهیم داد، همانطور که رئیس‌جمهور گفته است، ده برابر قوی‌تر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/136445" target="_blank">📅 20:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136444">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فوری / تعدادی از بمب‌افکن‌های آمریکایی B-1 هم‌زمان با اظهارات ترامپ درباره هدف قرار دادن کوه «کلنگ» در ایران، بریتانیا را ترک کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/136444" target="_blank">📅 20:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136443">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
توی همدان، بعد از شکست مسی و آرژانتین توی فینال جام جهانی، یه پسر نوجوون نتونست طاقت دیدن اشکای مسی رو بیاره و از شدت ناراحتی ایست قلبی کرد و فوت شد:// @AloSport</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/136443" target="_blank">📅 20:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136442">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
پزشکیان: [عده ای] چنان وحدت و انسجام را تعریف می کنند که اگر  کاری آنها می خواهند انجام نشود یعنی تخلف، یعنی عدم همزبانی، یعنی وادادگی که [این‌گونه] نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/136442" target="_blank">📅 20:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136441">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ:
ما اصلاً کارمان با ایران تمام نشده است،
ما در حال حاضر قصد ترک خاورمیانه را نداریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/136441" target="_blank">📅 19:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136440">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YztRtTMK_iswEwTGs1lO758dbY-nnCRdisDakIYckdmoO8B5BYLjFHXQ6QOXmhPY52hxQrwGFvfjVtU8SwEbS3BXoJu54CmDAYUB58VKtwLXu2qnIJjD5uzp6NGhyP64UqS68ONlk39yJGjRhBEAP9I-d36wrrAzrjvmyuG8OC-j3JHE2Pi5YTvW-sMf2Tw3UVsjG_GJIaRJCjH38PMV-0lFMVXPpie8W5ydHHILdiOjdFxayRT-Cs50r_zN81jEWipDQwV6UVOrS61vUqQMtbTgfXZKPkNVuvFb6-dxOcwnieu_lV7mgSx1RFa9RAVq3wpoMeHreAE2YOps5Uta1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان:
حرفای زیادی تو دلم دارم ولی الان نمیگم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/136440" target="_blank">📅 19:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136439">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ: اون‌ها حتی به بچه‌های کوچیک هم رحم نمی‌کنن
مردم معترض رو می‌کشن؛ بیش از ۵۲ هزار نفر
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/136439" target="_blank">📅 19:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136438">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
دونالد ترامپ: اگر اکنون از جنگ با ایران دست بکشیم و برویم 20 تا 25 سال طول می‌کشد کشورشان بازسازی شود اما کار ما هنوز به اتمام نرسیده است و ما جایی نمی‌رویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/136438" target="_blank">📅 19:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136437">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/136437" target="_blank">📅 19:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136436">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ: اگر نیروهای ما بودند، حمله مرگبار اردن رخ نمی‌داد
دونالد ترامپ با اشاره به حمله‌ای که به کشته شدن دو نظامی آمریکایی در اردن انجامید، گفت:
🔴
«آن‌ها توانستند از اردن عبور کنند و حمله را انجام دهند. اگر نیروهای دیگری مسئول عملیات بودند، چنین اتفاقی رخ نمی‌داد. وقتی کار خود را به دیگران می‌سپارید، گاهی نتیجه آن‌طور که باید پیش نمی‌رود.»
ترامپ همچنین درباره ونزوئلا اظهار داشت:
🔴
«در ونزوئلا اتفاقی رخ داد که شبیه جابه‌جایی زمین بود و هیچ‌کس تا به حال چیزی مانند آن ندیده بود. فکر می‌کنم بتوان اسمش را زلزله گذاشت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/136436" target="_blank">📅 19:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136435">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
سی‌ان‌ان: اسرائیل معتقده که ایران نه تنها سانتریفیوژهای پیشرفته خود، بلکه بخشی از ذخایر اورانیوم غنی‌شده خودش رو هم پس از جنگ 12 روزه سال گذشته، به یک مرکز زیرزمینی عمیق در زیر کوه کلنگ منتقل کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/136435" target="_blank">📅 19:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136434">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d51992207.mp4?token=B3A_x6F2CuEjem0dFuC8XlzS3QVdcU4zsqvx2IrUXuk-ENsG04hMlLFOljRvO1mcQ49_kG9fLatlqINkPDtr1vUMUBtn4h-Tx7m64PknA6IpiwJOAKBgia47zt6mCOAszv2OvL6Vj5dTVMd8NdPcXtSHVqXdADTZZN8EuSD_x2YafenxzSA74_-8urg-Xyt68Q56vtKnhQ8CQ7_nVungBoBAjl8S-EpuMKGrK8hdSbv1xvea7-h23sNGAaGNNkCS1m-55hQAw6i90VqAVx7HWxKtYztjsFeVaVuLlIp_oKXLqDUht4cpSW2GsKaTCEtK1-dB7do7zqVZ2V1fbzb76Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d51992207.mp4?token=B3A_x6F2CuEjem0dFuC8XlzS3QVdcU4zsqvx2IrUXuk-ENsG04hMlLFOljRvO1mcQ49_kG9fLatlqINkPDtr1vUMUBtn4h-Tx7m64PknA6IpiwJOAKBgia47zt6mCOAszv2OvL6Vj5dTVMd8NdPcXtSHVqXdADTZZN8EuSD_x2YafenxzSA74_-8urg-Xyt68Q56vtKnhQ8CQ7_nVungBoBAjl8S-EpuMKGrK8hdSbv1xvea7-h23sNGAaGNNkCS1m-55hQAw6i90VqAVx7HWxKtYztjsFeVaVuLlIp_oKXLqDUht4cpSW2GsKaTCEtK1-dB7do7zqVZ2V1fbzb76Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر جنگ پیتر هگستث در مورد جمهوری اسلامی ایران:
ایران هر فرصتی را برای مذاکره و نشان دادن اینکه در تنگه هرمز معقول هستند، داشته است.
اما اگر قصد دارند به کشتی‌های تجایی شلیک کنند، همان‌طور که رئیس‌جمهور گفته است، ده برابر سخت‌تر به آن‌ها ضربه خواهیم زد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/136434" target="_blank">📅 19:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136433">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf5a9d4c8.mp4?token=c3hXlmViwHoAgO0CUZsYcyMaInTCTfv-XVNkE5uu3-VAo2IPQ67YOwEdbsjINv3KXbSKOWqyU6DPOiIF1yRTqJzFW-9RzMxEDxkrNG8i28u218o9r6CcY8BUUpZph6MN7I-z9DxSRv3jkV7FPNapovxFXwM_UFXZoVvhow-0jmgmTt3o6GS3v7fVySHTaZE8n1oGQleuxTyS48BFj8fSBwMTNAWRY6x5eqiL2T5EqLwIP--kWCHS92cFnqR9VVPGKTTxNm8T0HZKQDSfzqnst-iFseVjvbnkRyA0M_RRjC40toRwiXx-6YpIqP9wGxNTisCEw4J_Mlaxfwa1HDYizy979Uh9INTzs3QULj1aOvEgh0MNpnZZsflvk79SCEe4s7qJSs7C_WTOoxLOwTPwfos5VomNdrk8uGf8Tx6IYXKzxr7TAtgh-bEcYngO6TmNSpTIbq7oJI4Ro69ycBBRzqzrgTc8Llsq0EujKdFIlzvLAFWz-HfOworCEARgBCHdPemzxrqg3byljbDrG-F7fdQatAkEwEqlEmSW4ABrsUnT2hjGFfo1OyQaYlvN_Bmt0a1v_bnsw2DKJFJDz8Ff50atGOyv5VH0i6Aw9iLnpNa3hzJDK3TE3_1j2vT7DYb_x9lJGCz2mwFTsV56-gcl2aZ6M0YZ4S5pbKg0-lhXg_8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf5a9d4c8.mp4?token=c3hXlmViwHoAgO0CUZsYcyMaInTCTfv-XVNkE5uu3-VAo2IPQ67YOwEdbsjINv3KXbSKOWqyU6DPOiIF1yRTqJzFW-9RzMxEDxkrNG8i28u218o9r6CcY8BUUpZph6MN7I-z9DxSRv3jkV7FPNapovxFXwM_UFXZoVvhow-0jmgmTt3o6GS3v7fVySHTaZE8n1oGQleuxTyS48BFj8fSBwMTNAWRY6x5eqiL2T5EqLwIP--kWCHS92cFnqR9VVPGKTTxNm8T0HZKQDSfzqnst-iFseVjvbnkRyA0M_RRjC40toRwiXx-6YpIqP9wGxNTisCEw4J_Mlaxfwa1HDYizy979Uh9INTzs3QULj1aOvEgh0MNpnZZsflvk79SCEe4s7qJSs7C_WTOoxLOwTPwfos5VomNdrk8uGf8Tx6IYXKzxr7TAtgh-bEcYngO6TmNSpTIbq7oJI4Ro69ycBBRzqzrgTc8Llsq0EujKdFIlzvLAFWz-HfOworCEARgBCHdPemzxrqg3byljbDrG-F7fdQatAkEwEqlEmSW4ABrsUnT2hjGFfo1OyQaYlvN_Bmt0a1v_bnsw2DKJFJDz8Ff50atGOyv5VH0i6Aw9iLnpNa3hzJDK3TE3_1j2vT7DYb_x9lJGCz2mwFTsV56-gcl2aZ6M0YZ4S5pbKg0-lhXg_8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار:
آی معتقدید که ایران سانتریفیوژهای هسته‌ای خود را به کوه پیک‌اکس منتقل کرده است؟
🔴
پرزیدنت ترامپ:
ما بر اساس مواد عمل می‌کنیم. آنجا جایی است که اقدامات انجام می‌شود و به احتمال زیاد به زودی به آن منطقه حمله خواهیم کرد. آن‌ها کار زیادی در این باره نمی‌توانند انجام دهند. معمولاً من چنین چیزی را نمی‌گفتم.
🔴
اگر فکر می‌کردم آن‌ها می‌توانند کاری در این باره انجام دهند، هرگز چنین چیزی را نمی‌گفتم. اما به زودی و به شدت به آن منطقه حمله خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/136433" target="_blank">📅 19:27 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
