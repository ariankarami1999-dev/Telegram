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
<img src="https://cdn4.telesco.pe/file/COUeBOHS89lnRK1xf9cHnOL__ll_W_sm3n1t06vwbpUDJr3Mylx_AhC9GzRdIKHozcyjGWUOZShI_wL7wFUNr4wzB1dIjZTmuwLa1Fs1A6hah6wBTLbjkm3gB5WzbNOs52utfIyV1veXQdzvWV8DGuu9ArkPDFqNjxR4k_GOnGaNqiHfN9PA2Bd3xW7BlRhNRHGaNRPQvI0E5mT0z7zmGTOsdCh4bF_LvQ4Ui7l1689Gzyz7Wvjo_BHzG3jL8IT8Mm5tloC5Ts9Rn2Sw_4aeQfHP581eBDsatVFPLiKwR0enivG_IYzYYlz-I0VcRvD_-bqwTdrJAyh7hW0OGIpnLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 932K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 22:23:15</div>
<hr>

<div class="tg-post" id="msg-137290">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
پدافند کویت مجدد فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/alonews/137290" target="_blank">📅 22:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137289">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ایرنا : آمریکا امروز بعدازظهر دو موشک به سمت یه نفتکش گاز مایع که از خلیج عمان نزدیک منطقه می‌شد، شلیک کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/alonews/137289" target="_blank">📅 22:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137288">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409d06d604.mp4?token=Hy88GxpUcAZpVUvL63Cc9c0ohJji2H48vrmvg4frtrgSi5KylCuWfJnUwO968ujavJV-LK_07QIV5QSqzxZvEIW7FEXyDmcD2Cb2kmoQaN8XE9fa_1hX4Iu4OaZLKNWNVXu4GqPRhKP41Cjdm7JQ5XYinsEQsOrE-thy5FkUcMUwuh_ADvt-xR_o4MI0QrMoiNOGTEA8LxNfKEx4VCp6oZ3rn2CFcv5BsElrXe0Fr43g5q1Q606N7F2kGS2zpVJO-KZBwqQCkLGY_qcNVDJGolkv2FfJKOdHACK9oQtSI-5u1ylqDQBPn6MsVmBOuT8lX0AEFyQyM8u64x4xCGcy4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409d06d604.mp4?token=Hy88GxpUcAZpVUvL63Cc9c0ohJji2H48vrmvg4frtrgSi5KylCuWfJnUwO968ujavJV-LK_07QIV5QSqzxZvEIW7FEXyDmcD2Cb2kmoQaN8XE9fa_1hX4Iu4OaZLKNWNVXu4GqPRhKP41Cjdm7JQ5XYinsEQsOrE-thy5FkUcMUwuh_ADvt-xR_o4MI0QrMoiNOGTEA8LxNfKEx4VCp6oZ3rn2CFcv5BsElrXe0Fr43g5q1Q606N7F2kGS2zpVJO-KZBwqQCkLGY_qcNVDJGolkv2FfJKOdHACK9oQtSI-5u1ylqDQBPn6MsVmBOuT8lX0AEFyQyM8u64x4xCGcy4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راز شلوغی کافه‌های شمال تهران
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/alonews/137288" target="_blank">📅 22:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137287">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
چندین انفجار شمال کویت را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/137287" target="_blank">📅 22:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137286">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
قوه قضاییه: شعبات ساعدی‌نیا همچنان پلمب هستند
🔴
ساعدی‌نیا هیچ امکانی برای فعالیت ندارد
🔴
موضوع مصادره اموال در حال رسیدگی قضایی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/137286" target="_blank">📅 22:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137285">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdN-xr1YiKohgGensCHCDbCON_ZGe6BhF94HzGmTrILaDDgKVNVdlP8STH3FMlMYdTp8gqxgYY8IpNI1UVndxM6yXNz4CRamj8f8kxgXj-9H_sv6SrqXDlUFIOjdX75Ghux9ZT9344JGcfOJjmA_cnrbXcbSGej_OPggVgsAAVhD1L7n6X-rUorGwNXzAB6MuI2oJfDNQqfOdB7J-Ko2xhX3CD_LZC4vNSBKyN7fkQ8qLTrSigqgZDsibsu3uUStmoW860KWik6_1NCRRKJsGKiks0ZMcL3N9Q5CNO93a6GsEi1_80P2peM3nl01fgOiqPP3A6iSzzEfqvUVQeyjQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
با سرویس های نامحدود ⅓ بهای مخصوص نت ملی هایپرلینک از شر اختلال ها و قطعی های اینترنت خلاص شو
🌟
با ۱۴۷ هزار تومن سرویس های نامحدود و ایپی ثابت هایپرلینک همیشه انلاین باش
✔️
همین الان تست بگیر
کد تخفیف ۳۳ درصدی فقط به مدت ۲۴ ساعت:
Code
:
w
ar33
⭐️
🤖
@hlink_robot
📢
@hyperlink_ch
💬
@HyperLinkSupport</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/137285" target="_blank">📅 21:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137284">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نیویورک تایمز: ترامپ روز جمعه با مشاوران ارشد خود درباره تشدید حملات علیه ایران دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/137284" target="_blank">📅 21:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137283">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
مقام آمریکایی : ما یه سایت امنیتی ایران رو تو نزدیکی یک گذرگاه مرزی بمبارون کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/137283" target="_blank">📅 21:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137282">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_lc1V2eOSgE3rzUgAp4wJzBxYBeVZByvZQ0y_gqi-QzFbc2deNOBjF6oWKo7dpbGzmTQ2SqdbKiQ68kd1CDteZGfUET_-ih5oE3QJsi5cYFC6LFRs-cXYkpB1h97O67y7Gv9ECZ4X7tH_97Bqxxt2anB3MT0_y0vybeRkOnWXy2oKAp5TkHrfTI49LbgYn6YjLjBVHcBXwhUKxIXz8E1Pr8pwsclY0BS9V-xEwr6gJcLsiWMkSQA3bXkf6DwRH5fwg6sFBhCqCfQyPPN8Do2yJWfcIzoJAp5SDnTK445aHm3EPNSmRXFomrGG4TlpxJ8SRWhhhqs9n1G_x7M9x4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین پست اکبر عبدی در کنار علی دایی، نوشته بود: حالم خوبه نگران نباشین
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/137282" target="_blank">📅 21:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137281">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
فرماندار جاسک: ۱۰۰ شناور در حملات اخیر آمریکا آسیب دید
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/137281" target="_blank">📅 21:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137280">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ: انتظار داریم به‌زودی تعرفه‌های گمرکی سنگینی علیه اتحادیه اروپا اعمال کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/137280" target="_blank">📅 21:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137279">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
العربیه: اسلام‌آباد از تهران خواست تا بر حوثی‌ها فشار وارد کند تا از حملات خود در دریای سرخ دست بردارند.
🔴
پاکستان به ایران هشدار داده است که بستن تنگه "باب المندب" وضعیت را پیچیده‌تر خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137279" target="_blank">📅 21:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137278">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYqNJJK-yLmJLtwnOCT-a5r62ec65R9FWOi7hvVKW8Ry_l_7fJyf06ZIT_FAog32XzWX8eYp3RSO9djoEshjSu196yzOfH9Vd8d-UV5DrRZNyes323ge5FOEEJWIFJp-6YGQIgrTKg5nD2tgkfNNod3DdS4yaRFd-bamfa010kpn3yBpUdkHBPnckNJA9ZGGhjRNrkq0sYajkz4vKNQYhAgxlV1Suuf4Oa3rtwfitr37o1lcE-btP-oEcxw6O7z4ikjQVSXRF5lWxKJbm4grri7IKTcuZ3uw5H1m2OG7e4UD8Sk4rKE1_l-7ikQrD7nXqmZFBsh0FyfKa6Fsa254Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، از طریق شبکه Truth Social:
از تمام سناتورهایی که با تلاش مجدد دموکرات‌ها برای تضعیف امنیت ملی ما مخالفت کردند، سپاسگزارم. تبریک می‌گویم به آقای مایک جانسون، رئیس مجلس نمایندگان، و نمایندگان جمهوری‌خواه به خاطر موفقیت بزرگشان در برداشتن اولین قدم به سمت تصویب طرح بودجه.
🔴
از آقای جودی آرتینگتون، رئیس کمیته، چِپ روی، میشل فیشباخ، ویرجینیا فاکس، جیسون اسمیت، مایک راجرز، جی‌تی تامپسون، برایان استیل، و همچنین از آقای تام امر، رئیس گروه اکثریت، استیو اسکالیزه، و همه کسانی که برای برداشتن این گام مهم همکاری کردند، سپاسگزارم.
🔴
این طرح، یکی از مهم‌ترین طرح‌های قانونی در تاریخ آمریکا خواهد بود. این طرح، به تقویت ارتش قدرتمند ما، ارائه کمک به کشاورزان و، مهم‌تر از همه، اجرای بخش‌های قابل توجهی از طرح "نجات آمریکا" کمک خواهد کرد.
🔴
مردم ما بسیار خوشحال و حتی تحت تاثیر قرار خواهند گرفت! از سنا می‌خواهم که قبل از شروع تعطیلات تابستانی، یک مصوبه بودجه را تصویب کند، که می‌توان آن را با اکثریت ساده به تصویب رساند. ما آماده‌ایم که در کنار سنا برای انجام این کار به نفع مردم آمریکا همکاری کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137278" target="_blank">📅 21:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137277">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7XtOx5nIsqfax0ICETaFzU3vci2qxj4Fp_ZRL8qIWUAorCrgdb7pdzb8P_ZJeTZQlVd9gen6T26gbrR-dT7mBSu_NJx4psAgdWcBlAzWnxVVz_uRIKBA5Ghachlh-Nda90Miv36_fcYRBoNvJ-0xOg2tT-YTWdz99YO3wgQZKzJixekCB6bluhJCCIulEQpr0-40BgZcsi5JbQS3EpRMLd8tuFtynPUIcs-6SRCAhJoOcRpijY_xRy0roPfdEAs7h2EMEF4ORKYu-4NfUzbGE_LXbmORJ4SwWieceVWC-X4EIh2-uzOMbuYXof8hXIetxYe1Nw41NXasxIPR0Kbrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137277" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137276">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJwjNJeJk5GHe9EAzCw7ZME_L4NJmOHga93HbDWjfsL7GlJ1Mm95Lz9AJYrMwrgeuixkixZmGj7NffX5Pb3I75iDgTMnhZ37aZn_1K-ogCR9IPTxxOEZyP65Vb7rwcGSXAHTPRGVCcNYfVcHzTTFQp1GW9DC8eKXi31jQJTOXM-TgtKSX2QXOYHcaa14HRLmCuUs6voNbKssGOvxF0i3PxrAyMb6MkxcPs6O7HuHEWSFC_j7J5LU5PWFBWz-ubwHGe04JmTI1LZVTcGRj-yfQrBnBvcoo5zDxUFK4awlVZqzIGGTGxTh6tnmkJQR8rvlpA5PptqxyMW9A56a1Tsxhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: تشکر از نخست‌وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137276" target="_blank">📅 20:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137275">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp3MvUbfv3Fik1wU21LW1PjeshpaQdfj46-Hx70Keypcs4Zwtrx0lLFYB3e4mj-Dsn-t0CaeIZ9hxqB-ho52xnpAOuap5ppMSvARAF8uNZzDjfitXiqvY6BUjmjoQ-z4eTxZqZiyeojt7cCSTMaiYasAt_Gd9rWCHfW6-CZ2O6BFhE-Vp0K72ZWUMXgeA3QXsAiGlmN8eS_To_W71YNvGFBt6TRDxZkQMD5rv2C69a_awk_Q7e1xt2vtTi5lf0lHcL0YH3QLQnSjy1mvQwx35RHclbeKgnm-Fwc3ButWrrYDwa4gTahNy6mQ0NBTTquEqyioWRVei0-JebnougLWjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همراه اول قیمت بسته های شبانه خودشو یهویی ۳ برابر کرد و اعلام کرد با مجوز گرون کردیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137275" target="_blank">📅 20:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137274">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afacd735eb.mp4?token=YTuUdk3efqx1sr9gTdgmW4OnBb9ze5usmpqHOArVb5ZtSME98otv_0GVcB8Y5viKpc95udjcc7f30BWrX3S25d7kg4oaTJxSxj7C0uDGjwWEo8jp1m1qU_rHRATzU9-DGqh714z-FE7tlPKymR1A9lf9iLeCheT8uup9PwVOSLn7DzaXpI3WNsXC55DuTSKEIDXINiUnLUM6fhKVNAUcURMIjx1IWDwlBsK5kFHvpGaUBvuXdXG1YJh9nLXSCRdavZcVGuaHFT9-1kjZOiURcQZORVXc5giOaD7Sn2EFwZw-a7DnVOiW7nlfIyTnwyfUySlUs2nCnDkOz3q812KQ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afacd735eb.mp4?token=YTuUdk3efqx1sr9gTdgmW4OnBb9ze5usmpqHOArVb5ZtSME98otv_0GVcB8Y5viKpc95udjcc7f30BWrX3S25d7kg4oaTJxSxj7C0uDGjwWEo8jp1m1qU_rHRATzU9-DGqh714z-FE7tlPKymR1A9lf9iLeCheT8uup9PwVOSLn7DzaXpI3WNsXC55DuTSKEIDXINiUnLUM6fhKVNAUcURMIjx1IWDwlBsK5kFHvpGaUBvuXdXG1YJh9nLXSCRdavZcVGuaHFT9-1kjZOiURcQZORVXc5giOaD7Sn2EFwZw-a7DnVOiW7nlfIyTnwyfUySlUs2nCnDkOz3q812KQ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از انهدام سیستم دفاع هوایی پاتریوت در اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/137274" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137273">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: بحرین و کویت در حمله به ایران مشارکت مستقیم داشته‌اند
🔴
وال‌استریت‌ژورنال به‌نقل از منابع آگاه نوشت: کشورهای بحرین و کویت در اقدامی مخفیانه، جنگنده‌های خود را برای حمله به اهدافی در داخل خاک ایران اعزام کرده‌اند.
🔴
امارات نیز با ارائه اطلاعاتی از اهداف و تأمین پوشش هوایی، در این عملیات مشارکت داشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/137273" target="_blank">📅 20:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137272">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpVmnPuGrFPV0WokRDr9FCzrrDXOusGbeSa1XeGPFjJNa88MyP4Pffpj8tKYvGwVPWkCL5fB81pCALYJ3qcpHynhwtH0R_IVWBFvHV_AuUtD3RLSDer3GdcFkZDTWmvkq7y3L6CH32fOU3do1YMhFjlkskJ5AsOKRru3x8qeTwtlnlEtRfz4u2sT82ikzq1IwXQvVo-UBvhD4ubq8W9UgVsRPTutZd6JKnWMFhTfXGh0duJWKrh3Fz6wYFsUqPcS6JvGcrLP8DsCpyP0vhL7ypR96f1V3w9zl_ayjVyjbyyAuUdWH3SSCrenr_BTrq2X3JbwhbM6oD469WpJOHXVJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخورد پهپادهای انتحاری سپاه به مواضع گروهک های کرد  در شمال عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137272" target="_blank">📅 20:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137271">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDtztLxgB1cMWWb2NRT0bWsGQoYt1FM7AUYmYsl8Jxh_khmSk5OEYbNTOG-IW84p9hn48rQ8MWwS83BycwCddNNZpzzM3v5tDmFXtj_NiH3X5exgH9pOBszSWqAG00iUxkYXK8yeyBiq8dRl1IWD6EEItoESGuDUcMYyZtLVBvigBHZseOZTBymVJ1Q_vcn-FTaJLzWGnYl3WGgs4dhBf35pycD0LZ1zcJPNdAb4PltSkBhVJZhvj_bEj2LZbMnnj6xDZr3Y6LZYASedwyscE-9ZupXhfe9uIDzMp10__bBrvipOW452DYyyDB7g-nG-OVQdob_WAqQZ98qO6YIoGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخورد دیشب پهپاد سپاه به پنت هوس یک برج معروف در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137271" target="_blank">📅 20:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137270">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWuTf1S3YFZKViPjfCsZQ1ELluPb3s84o4H9zuTqGVXp8DLfI2ZStvVYlS-y-Kcd2k1J7DLW5Q0o1vbDu6XMbefnTQzbqSl6ppuFkwX5j0-6dTXN7GctptqF3yyb3DYcsbAHDNQbSqEbT2t3mClTZXn2s62pdjcGJnU4x-K8NpoEpnOakHWX-ufmuObpghsCCmnAYyFlZ3rbMRSqZ96x7k3fVA-RHq5T7xsyi9MwCqdhLP_9-pAhecRUSskvm5iacGBolLQFCDaPxbssQ5NiKnOIcgmdsLrUgbWHlPtvH2eCVC69_qFVFR4AzpOPWw3Su3aJrhk6jJjAtjPB34VLLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق شبکه اجتماعی Truth Social: کانادا دعوت آمریکا را برای افتتاح پل گوردِی هاو لغو کرد، که البته جای تعجب ندارد، با توجه به اینکه آنها مبالغ قابل توجهی به عنوان تعرفه به ایالات متحده پرداخت می‌کنند.
🔴
توافق اولیه، که توسط دولت قبلی به طرز فجیعی مذاکره شده بود، دیگر اعتبار ندارد.
🔴
ما شرایط را تغییر دادیم، به طوری که اکنون ایالات متحده 50 درصد از سود را دریافت می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137270" target="_blank">📅 20:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137269">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
حمله پهپاد های شاهد به اربیل، هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137269" target="_blank">📅 20:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137268">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
منابع عربی: صدای چند انفجار شدید در کویت شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137268" target="_blank">📅 20:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137267">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
گفتگوی تلفنی وزرای خارجه ایران و عمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137267" target="_blank">📅 20:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137266">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
آکسیوس: ایالات متحده و بریتانیا در حال برنامه‌ریزی برای برگزاری یک کنفرانس بین‌المللی درباره تنگه هرمز هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137266" target="_blank">📅 19:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137265">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
فرمانده مقر خاتم الانبیاء مرکزی: به ازای هر شهروند ایرانی که شهید شود، یک سرباز آمریکایی کشته خواهد شد. ما بلیط‌های رفت و برگشت مستقیم به جهنم را برای شما آماده کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/137265" target="_blank">📅 19:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137264">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
منابع عربی: صدای چند انفجار شدید در کویت شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137264" target="_blank">📅 19:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137263">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFAV3LiUUO6zp-SYADyjjLUZZogUHKcRTy-2dhvjQuV-5FpMq6c4AW6r_simyuwwoieXC8FO9oGeLGtZrItmpgKHuL2991o3TDT2w7njVDWFICnQVfjrohYQw05GCGPZOFbqzBuKACQu3egubbLPZGN8MmPE2zfQS1kjt6nNkEAa73pxgnYxhJnRTDjKwsszwwQio8k1AXeHmwJ1m4wKOUlue2oPbg2yvSKWK7wVYnxDwwViFJu_wcDBMjSzKop37Cwdy5rOI-Kh-umHaLB2_RMa-xYIlQw6X-UikaujY4up8V_3drxNDu0Ps7lcYumXRLFjVycNbbBkr5jQvmUE7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش قیمت نفت همزمان با انتشار اخبار مذاکرات
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137263" target="_blank">📅 19:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137262">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD6TbQ3fnqM9l5JuAXXP6-ZUSs_jNGrFNeuMuriA1IzzZzKVWlUPl0JuSRavxdk6aiw4CCr6uCUckPx60dp-60xL_P6T-cUQn4kuv1bM91XtiLKP4I2sq7DgYH6Gzm_IlkSDk9oEonkMBQS1eedCOzcMmLZAB3nt42Yno3-uQPNzWWSBzxBokuCfP3VU6Uc1iPPsS6TKVQfhDNw5JR4-5SdWkFNNXVclDOP2O4peGBQ_E8GAVsTsMdMkp5oE3ehDBRf-4mn4yXdxcpPrQ-fe73L90CaBvrgmZ9o0aAn3vOd66QSIhNJEpt4KYmn86I4zA0ohAxk1PV51H2aPEicTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش رویترز، قرار است رئیس‌جمهور ترامپ و رئیس‌جمهور زلنسکی روز سه‌شنبه در واشنگتن دیدار کنند.
🔴
مقامات اوکراینی و آمریکایی در حال بحث درباره پیشنهادی برای آتش‌بس هوایی هستند تا آن را به مقامات روسی ارائه دهند؛ این اقدام بخشی از دور جدید تلاش‌های صلح‌آمیز برای پایان دادن به جنگ است.
🔴
برخی مقامات اکنون معتقدند حملات مداوم پهپادها و موشک‌های اوکراین به روسیه فشار اقتصادی را افزایش داده و ممکن است مسکو را برای مذاکرات مجدد پذیراتر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137262" target="_blank">📅 19:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137261">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رویترز: مومنی وزیرکشور تاکنون ۲ بار در  ۱۰ روز اخیر، به پاکستان سفر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137261" target="_blank">📅 19:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137260">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سفارت آمریکا در اسراییل: آمریکایی‌ها باید به دلیل تنش‌ها در خاورمیانه، آمادگی لغو پروازهای خود را داشته باشند
🔴
آمریکایی‌های خارج از خاورمیانه باید در مورد سفر به این منطقه یا عبور از آن بازنگری کنند.
🔴
سفارت آمریکا در اردن هم اعلام کرد: شهروندان ما باید اطلاعات دولت اردن را در مورد تهدیدها دنبال کرده و از دستورالعمل‌ها پیروی کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137260" target="_blank">📅 19:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137259">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری/چین وارد شد
🔴
رویترز: چین در کنار پاکستان در تلاش است  توافق ایران و آمریکا را احیا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137259" target="_blank">📅 19:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137258">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
برخی منابع:ترامپ به میانجی‌ها اطلاع داده است ایالات متحده حمله محدود به تاسیسات کوه کلنگ را خاتمه جنگ با ایران اعلام کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/137258" target="_blank">📅 19:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137256">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Opm61FuF__JkT-tBup_JW5p9HL7q6mf8z7vaqXUKEIH-zsPN2FhQJD3sMVfER9QPC1oIOyFTwATIC4OGN1AeizGpp0SmwvBV4Frd--7fuG7XowPnjqpqtsyeGyteMlAZPfrPFZZWjTemYRbvAtkFFXO7nQtJE2bznBAoJjhvp0pdbztilntUWVNgc8PL9dLebOd9sZuW6xevU9umNmlitLhjcPuo6CPCZOnQ9wpfW3u931NvNwAXneoOc9MPHfhaANSkrhx6XJMFbauESXBPc3wut2FCxq5DpqEmov1poGPOR_v1rKg3MW8j1E-n_lDNPrmf0hKIx2s2Ynu0VBi9RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی به سیم آخر زد
‼️
🔴
عباس: اونایی که تو کف خیابون و یا هرجایی مردم رو به توافق ناامید میکنن و باهاش مخالف هستن از اسرائیل خط میگیرن
#حق
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137256" target="_blank">📅 19:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137255">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ay3FRzQ5zvor7PqIf3a0LA429dFaWAtb_QZR5rLBT6rHlxcbRR5se936ny1pWvRG4-JKXvAeumHDC_nAcTt4u2rWUZh6-o0qHkDdFBJbFqlgod35zpze_aEtxA6hHHFpQz8taCrdSkvMQJArEPuCc5hub_fGDKa2jtqf7lLzJUGljcgaR42p8alZ-1X3fQF2djSb2q2JAWF3JmJKcACnG54ScpBX4pqbduDLluf__TSOUovXqdJ8rbk2mcSLJ85SCQtLxjyX06oprtzCU4kooLHHM389infmw1_49Tl4elydto1fRYoPmoCA0txRDsVdYEqm2wzreJDLgNLHX-lD7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: رئیس‌جمهور شی، در دیدار اخیر ما در پکن، چین، به من گفت که تحت هیچ شرایطی سلاح به جمهوری اسلامی ایران نخواهد داد یا فروخت — و این بیانیه شامل شرکت‌های چینی نیز می‌شود. با توجه به رابطه ما، من به حرف او اعتماد می‌کنم و علاوه بر این، من نیز به او امتیازات بسیار بزرگی می‌دهم.
🔴
همچنین، رئیس‌جمهور پوتین، با وجود جنگ وحشتناکی که در اوکراین در جریان است (رابطه همچنان مانند رابطه با رئیس‌جمهور زلنسکی باقی مانده)، به من گفت که سلاحی به ایران نخواهد فروخت. او درک می‌کند که من سلاحی به اوکراین نمی‌فروشم، بلکه به کشورهای ناتو می‌فروشم. آن‌ها قیمت کامل را می‌پردازند و اینکه چگونه آن سلاح‌ها توزیع می‌شوند، من هیچ ایده‌ای ندارم.
🔴
بنابراین، دو کشور بزرگ که مردم اغلب در مورد ایران از آن‌ها صحبت می‌کنند، به نظر من مشارکتی ندارند. اگر چنین می‌کردند، برای آن‌ها بسیار بد می‌شد — قطعاً در بهترین منافع آن‌ها نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/137255" target="_blank">📅 18:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137254">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سی‌ان‌ان: ترامپ با اعلام شرط پیوستن عربستان به پیمان ابراهیم، توافق همکاری هسته‌ای با ریاض را به حالت تعلیق درآورد
🔴
ترامپ از این که، وزیر انرژی اش، بدون اطلاع قبلی او این توافق را به طور عمومی اعلام کرده بود، ناراحت شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137254" target="_blank">📅 18:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137253">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcMN5bjHWWJvkJK_V67HXaiI3Juj220x4NHG8zy-JxqLQJUFHfWp9cG_3cUcLFjD38MTikdZMUprBQmbnunvt_17-5muoKz54LGpQAABYuoz-PiU8FWznslHlux3Y6ZZ9KMpbhUXHjV6v89xdTTkk-He-0wR0aTLtykF_F-IOvljlTLVa9JWa9azxotoN3LuQsUV4opob_G5eu56TMMydA_24KnQeNBnTRw-sRnP-VHFFY5sQ2ANDk2WRin4dmxulP4R3uPHZOc2YR4j5OdQo5XGm5mhtVEDTUwdkd2QIlemtA9yqId3M-RkvSesPOCuUI9fCcVFvhC3OjWqRSrrOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرویز پرستویی:
تا ابد بر پهلوی و طرفدارانش لعنت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137253" target="_blank">📅 18:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137252">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
رویترز : پاکستان و ایران دارن راهی پیدا می‌کنن که دوباره مذاکرات با آمریکا شروع بشه؛
🔴
این روند هم با ابتکار چین داره پیش میره
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/137252" target="_blank">📅 18:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137251">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cf8ecb014.mp4?token=sCLBNv-yL2zWdQr5nc9OjrChOplyInyD__JUxnkF6hU9mnFSg20SW4qpEzC3bo4hLUKIZ1C3iBSdZxfjhk6JMGoH1leRacCwCrsRKkfuBFy_E44GRu4lA8sj3XoeWsAy-E9uGS7x44BFoZlhUnb1HT1UUJOhzUDqeQcpPWEgTbSVGtCTT-08-Tcrfzgz9Uc0kAUyMk1vc5UuXD7FKj9t1OnJmFWXohI17_teapQk4T_CorqOPwYf8oaXPlLTZudF2XU6XAUhQQVdCojMqxk8AKaAChXU0G-5EeVm2IeQZFSihZRg2I0WX361XFY1a2sKEBN3K9tRXvuG15BC37iwGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cf8ecb014.mp4?token=sCLBNv-yL2zWdQr5nc9OjrChOplyInyD__JUxnkF6hU9mnFSg20SW4qpEzC3bo4hLUKIZ1C3iBSdZxfjhk6JMGoH1leRacCwCrsRKkfuBFy_E44GRu4lA8sj3XoeWsAy-E9uGS7x44BFoZlhUnb1HT1UUJOhzUDqeQcpPWEgTbSVGtCTT-08-Tcrfzgz9Uc0kAUyMk1vc5UuXD7FKj9t1OnJmFWXohI17_teapQk4T_CorqOPwYf8oaXPlLTZudF2XU6XAUhQQVdCojMqxk8AKaAChXU0G-5EeVm2IeQZFSihZRg2I0WX361XFY1a2sKEBN3K9tRXvuG15BC37iwGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کپلر: عبورهای تأییدشده از تنگه هرمز به شش مورد کاهش یافت که نسبت به روز قبل ۶۰ درصد افت نشان می‌دهد
🔴
به‌جز یک کشتی، همه شناورها از مسیر یک‌جانبه تعیین‌شده از سوی ایران استفاده کردند.
🔴
در مقابل، تردد در باب‌المندب افزایش یافت و به ۴۹ عبور تأییدشده رسید.
🔴
داده‌ها نشان می‌دهد  بازگشت به تردد دریایی در منطقه به‌صورت محتاطانه و گزینشی در حال انجام است و شرکت‌ها همچنان در حال ارزیابی شرایط امنیتی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137251" target="_blank">📅 18:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137250">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
حملات اسرائیل به خان یونس در جنوب غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137250" target="_blank">📅 18:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137247">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mmjPIk1UwUeHY3ci_2Yosc5GPvJrrSbsNcjMwSUr387nbaD9ovdJwpwlLTsg-3UMKtbzuqp5aDMlK9z7J4-6eBClJ2jfg_GB9Qjzp4SqolgwLKWCd-Weu8jZC0KtJKsyEROYSsklEi469HWHg-nKWsy6BcHXlcyFBA_61hqTVyDfSkpPocwGI0DellMLpSan8qPBC3woQb8nSXI_qSOoRqQ8L56yZIzoPI1qBcYLPG3yqDBV9UxzaDX__KjnQkUYQRWJc62MqniH9B3zY-S4uiU3c8weRigrda0aBYb5iHhxvzKEd5dsrK23O_9GT0rA_K349f3XFCG-DahuB6assA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CEZtWYz6rInDufSMJlqHEm0dPMHS7mNYhH246sdZSSZPY35OHRhGL3FZwaSqSwAhUs2Hx8O3V1t-Mbk5E3KklxUc1NdelU9bENtvzIMQu4G8imTz9vniS5boEhbygNTIitOaNjZtD2MkpRdRBRvAl3IkiflM4I4qhxAcFECBBwMEN5c8c94pxSTah69uuQCzmfBjpv4ArJMHLdGXncOwi1nQaJbxChr9Na77GO_js379jTIrnvTyemvm2LIPZPnZQTDjxIccWnOO8In8DIC4oJO-jGgaX-GlvufqZ3TnNF9OJXoWFfqhnP7dd4Z9i9OpATrPl1U_ibIk6uLceY1l4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VL0Gi7Pdbd-yUA2cU4-lWQIsoP6sRLXL7SlFFKlNcXywIgHMVAkX24LV49ujoknZD4JftSsjWn4tq2wzoJOvucEF8JcMN5v1pb2cl-JMyD_VnyoSq48HWWoAPkl4Zrb8Kn5Cw8osjk82F--hTpZWAxKAN_sJpTiF2scGWVwvZaTy16Au2TtM77k9JReFRM4Nn_Nuu5Advlpv_z0me2veOVWj0lSqW0lyHV89LBS8iaxh_M0vY4P0vUDuk2Mu7D39KoE3uttkrh0MyCx8r0QTdJGPDM3Cl_KilUnoQM-_3oAVcs10AWVV1PLsRxwtuOpZMkSBeL-uJx8f0-SzC5_TWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سنتکام منتشر کرد :  تفنگداران دریایی آمریکا یک سامانه موشکی هیمارس را در جریان یک تمرین آموزشی در خاورمیانه سوار بر هواپیمای ترابری KC-130J سوپر هرکولس کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137247" target="_blank">📅 18:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137246">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3927f843ee.mp4?token=lu4eSGaKYSPhmOyBAWYx5N11uxlKLlmz4zTxgHx1pW9ulml6J35VU74lDSZ76iiBgDZcTBmmylKI4ULKUOKzLWGac1uSAw3iuQ5RAToelpwV7OYE6ZGuPV7EVCYRbT4a6yAc6zrOmzIeBZJ6nA2fdjn44NFkMTNBGqqjgCQ1Ez9n0wrESg_JwcfKnKjHzjrHOFDH19Ahu2uWQFSnIzeYI6egxFEuA1Tf9NKQQPfEFlMs-2pfe3QNdxO1mmZPmKAJsXgqh2tfqbXh57utFwIVhmUM1aLq0_6t8OuVC6SD_XrQDO7Ef2-vWib4uVoX65rgmtZyBKv1grQNN5YOYDrs3ii0izKIoYyIh83xm48jU6iYf8TSILF8baueyOktSAMkYhmpc-GEyBqWzsObHgy0H1knIiva5EZy56VOgjr-ktKljiNYtkDTha7HGU2EbtScQRQ0Lu2lMGE2aK5GQLJ8E0Ao0Ad-fYtVqwPIcKEFyKGfh1R-4Ph9NaIdgJ0g1qfWtA-z9iuwMtziGbSuhY0jMJh8CyOv5fqcG9PTk-D_rOg6IHwl2JNep_pvSkhfndVFayUymO4lmIGVMzOgKTDWt_X_i7ObxwIJRmUMUiIkbvYRglmPsv_WgcPe2sIkpVcHmfesQe67yKX7dPKIIyFfSGHz4a6RPdnZThhAp1lJ3mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3927f843ee.mp4?token=lu4eSGaKYSPhmOyBAWYx5N11uxlKLlmz4zTxgHx1pW9ulml6J35VU74lDSZ76iiBgDZcTBmmylKI4ULKUOKzLWGac1uSAw3iuQ5RAToelpwV7OYE6ZGuPV7EVCYRbT4a6yAc6zrOmzIeBZJ6nA2fdjn44NFkMTNBGqqjgCQ1Ez9n0wrESg_JwcfKnKjHzjrHOFDH19Ahu2uWQFSnIzeYI6egxFEuA1Tf9NKQQPfEFlMs-2pfe3QNdxO1mmZPmKAJsXgqh2tfqbXh57utFwIVhmUM1aLq0_6t8OuVC6SD_XrQDO7Ef2-vWib4uVoX65rgmtZyBKv1grQNN5YOYDrs3ii0izKIoYyIh83xm48jU6iYf8TSILF8baueyOktSAMkYhmpc-GEyBqWzsObHgy0H1knIiva5EZy56VOgjr-ktKljiNYtkDTha7HGU2EbtScQRQ0Lu2lMGE2aK5GQLJ8E0Ao0Ad-fYtVqwPIcKEFyKGfh1R-4Ph9NaIdgJ0g1qfWtA-z9iuwMtziGbSuhY0jMJh8CyOv5fqcG9PTk-D_rOg6IHwl2JNep_pvSkhfndVFayUymO4lmIGVMzOgKTDWt_X_i7ObxwIJRmUMUiIkbvYRglmPsv_WgcPe2sIkpVcHmfesQe67yKX7dPKIIyFfSGHz4a6RPdnZThhAp1lJ3mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاژا کالاس، رئیس سیاست خارجی اتحادیه اروپا: ما با آمریکا توافقی داشتیم و به آن توافق پایبند بودیم، به تعهدات خود عمل کردیم.
🔴
منظورم این است که مذاکرات آسان نبودند. برای شرکت‌های ما مهم است که پیش‌بینی‌پذیری وجود داشته باشد.
🔴
به همین دلیل است که شرکت‌ها می‌گفتند: «به نتیجه برسید، به یک توافق مذاکره‌شده برسید،» زیرا پیش‌بینی‌پذیری بهتر از این است که نتوانید پیش‌بینی کنید چه اتفاقی خواهد افتاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137246" target="_blank">📅 18:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137245">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
عباس عراقچی وزیر امور خارجه: رایزنی ها با روسیه و چین مستمر و مستمر است و ما به طور مرتب با دوستان خود در چین و روسیه در هر فرصتی مشورت می کنیم.
🔴
طبیعتاً با پاکستان به عنوان میانجی در مورد ابتکارات و پیشنهادات آنها گفتگوهایی صورت گرفته است. مشکل فقدان میانجی…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137245" target="_blank">📅 18:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137244">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
عباس عراقچی وزیر امور خارجه:
رایزنی ها با روسیه و چین مستمر و مستمر است و ما به طور مرتب با دوستان خود در چین و روسیه در هر فرصتی مشورت می کنیم.
🔴
طبیعتاً با پاکستان به عنوان میانجی در مورد ابتکارات و پیشنهادات آنها گفتگوهایی صورت گرفته است. مشکل فقدان میانجی بین ما و آمریکا نیست، بلکه مشکل رویکرد مشکل ساز آمریکایی هاست.
🔴
تا زمانی که اهداف و خواسته های برحق مردم ایران برآورده نشود، طبیعی است که به تلاش خود ادامه دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137244" target="_blank">📅 18:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137243">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ایرنا: حضور هیئت دیپلماتیک عمانی در تهران
🔴
یک هیئت دیپلماتیک عمانی برای گفت‌وگو در خصوص ساز و کارهای تنگه هرمز به تهران سفر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137243" target="_blank">📅 18:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137242">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tt4NvkNuhuNef7m3rO5H98z5ok8tiL0dcIr8sRqFjVYsEtEkRpF7xZj5QZvOFsjqx8fGSgGok9q7l0JqlyMu2InjGyY3WRIaeeK40KeTdTtW1_zkyLdeWAI9_ZacoiuJhpYGpcg9f-2wQFbSIvOI-lVW5mSgoIOaIAtkH4rlWX9ri4ZG9eMN23TE4g8BY9Wn0YaxWvBw_x2l9wkqgn7aEEEtFBm5p-cCb6I3tzNhmL2hDdpyB47FL8NECA2TgG4OKetVG1MbZxsxqGO51kDWLSGWONhrVwHOzXu41UMM3pecQeT35ClhxWjKIEVXCpdZ4wsefeUozs_zamQmd3V8Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی هوایی متفقین ناتو اعلام کرد که امروز صبح دو فروند جنگنده اف-۱۶ رومانیایی و دو فروند یوروفایتر ایتالیایی برای رهگیری یک پهپاد ناشناس در آسمان رومانی به پرواز درآمدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137242" target="_blank">📅 18:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137241">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXifYFdKxfIXDUdUIds--JWNVbO4NY3BpcOy7aHcjQFrGoUpYLVR6CWrb2hhT2rePrA11uLvNGXJDSLvSd0s6qhSVOZYSsx6JjcSduotkUbFpuCrMc9h_Sz45KbxOKHF56XUcnkIInlW5YWGqkkyM715KoOEFWr8BlpZ468HZTelmr91zwt9pNI4OoB_Zb47gYapNOM8-uocM6LEQ79qTgD5JTr8TcPdKMn6FDUre3Yt6M9tPnEXCssBS-FAB3ngKy--RbhltO73_UNnKwam8IneGyOBqNy6MmdfBZlhxGtjaUvFPgspaAy0MHNBmfADIBTRImLZ-RRLjR2ZgX17Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز 2 مرداد تولد جاویدنام نازنین‌زهرا صالحی دختر 13 ساله ایه که در اعتراضات ۱۹ دی تو کرمانشاه کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137241" target="_blank">📅 18:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137240">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا اعلام کرد ۴ فرد و ۹ نهاد مرتبط با ایران را در فهرست تحریم قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137240" target="_blank">📅 18:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137239">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
عراقچی: ما آتش‌بس موقت را نمی‌پذیریم و این موضوع مطرح نخواهد شد مگر اینکه خواسته‌های ما در مورد تنگه هرمز برآورده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137239" target="_blank">📅 18:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137238">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری/ وزارت دفاع کویت: درحال مقابله با حملات موشکی و پهپادی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137238" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137237">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
بنیامین نتانیاهو روز دوشنبه آینده به واشنگتن سفر می‌کند/وی علاوه بر دیدار با ترامپ، در مراسم تدفین لیندسی گراهام نیز شرکت می کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137237" target="_blank">📅 17:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137236">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
شورای اتحادیه اروپا امروز با اعمال تحریم‌های جدید علیه ۶ فرد دیگر به دلیل آنچه که «نقض حقوق بشر در ایران» خوانده، موافقت کرد.
🔴
بر اساس بیانیه این شورا، ۵ قاضی دادگاه‌های انقلاب در استان‌های مختلف ایران در فهرست تحریم‌ها قرار گرفته‌اند.
🔴
اتحادیه اروپا همچنین یک مهندس رایانه ایرانی را نیز تحریم کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137236" target="_blank">📅 17:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137235">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
نیویورک‌تایمز: پنتاگون در سایتش آمار نظامیان آمریکایی کشته‌شده در جنگ با ایران را از ۱۸ به ۱۴ نفر کاهش داد.
🔴
۳ مقام آمریکایی گفته‌اند که دلیل این موضوع این بوده که مرگ این ۴ نفر پس از اعلام آتش‌بس توسط ترامپ در ماه آوریل رخ داده است!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137235" target="_blank">📅 17:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137234">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WA60LtHgGNA6EzwRhq_KjxwKBM-xqFsAK0mYQ1aL0RVdgKGD3y5BVtAOa751n8RbCw1iP6LOFUvZJCiK_3nlZ5KKqpWb1b3pdQx0BSCnmpU2hH_VNpLU9xglWNIbw1ZHcXQxJt6aJo5c04a0B53j99pREM4y7rgBviOeH-47RX3_O-HmF_Axh9c08rFCR7lL8PmPMYBqWTnDehGmKjQiFWsG4-IiFERQLsdw0hO6MqgcMUKkvipSjNJ-JYOzPspqkQqe5RWsHAdnguo-XmYnSFWJdEvdbQo15Z7ulNUSLCHO87gxKNwet7QsBBQJZP4XUH2ZhrAcQyTAw4YLxtSVBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جبهه پایداری افغانستان(طالبان) اعلام کرد در صورت حمله زمینی آمریکا به ایران ساکت نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137234" target="_blank">📅 17:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137233">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وال استریت ژورنال:
ترامپ در مورد ایران بیشتر به گزینه نظامی رو آورده و فعلا پلنی برای مذاکره با سران جمهوری اسلامی نداره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137233" target="_blank">📅 17:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137232">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سخنگوی وزارت کشور:
برای هرگونه عملیات زمینی دشمن آماده‌ایم.
🔴
روز رزم ما، روز عملیات زمینی است، اگر بیایند به خدمت‌شان خواهیم رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137232" target="_blank">📅 17:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137231">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سخنگوی حوثی‌ها بسته شدن تنگه باب‌المندب برای همه رو تکذیب کرد و گفت محاصره دریایی فقط عربستان سعودی رو هدف قرار میده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/137231" target="_blank">📅 17:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137229">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMcFkLdNZlPuHqunJjCoG2qtFXGy7-Gt8eQSBi79X455R69Cinl6WE8asBtzbQNOEqjD1L32BCMl-2Rht2hWahaN_LRJC9AK11yaUtLcaFrW04peso0mqFg_0dGbk_2FeT92PkgQvVeY18v50A2m_0gVsi_ZD_BlShGW-_1EUQs4FQFxKo6QFwOnHV_cMUZIeGNtnuzTM_wViPL3_JHrvUYXUrzHzvguQNQHVH8a-ypwyL0wmdBJPkyCiLAKvCR9lvoZvvlkRXO9ivrec_mDx7AmwWsfaM1YDWvRFKbetbbAE5CVMgbpxe8GFkh2rr4YX7v4QHCF-jtOMi3QELfLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZyPnV6fv9DxUDhGBtLgW8f5VNg48UPQg9kW-6Zwdg7up0ST2RC08W6_fTlf73TjqDMmq4KRtiP9RYvNyom7D8V0XPMX3SpddiqgaaQNaH9MRg9PZ8EuTyL8vhzLe3MzN5KHIKnodPCr2mPLZ-SiYNgxmV0B8A3TMomxbJi-qAcyKwO-qc3tk5AaUUJlEnwVzdvFg0m3Va0mv6FhouMfAlNbhuQ6puJ3RWqCJyvEBuAHsK6lbfZRltyTU89NTX30u8BOgHAcplD4Bpjx6Wo137FV3_Tu-Bc0WKCaUFlHvg1YVD6LVEZ9Ptv-Tz1yQXqiMHMxJFo2-CfVIf7oXERO8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برند معروف گوچی از پوشک جدیدش برای بچه ها با قیمت 88 میلیون رونمایی کرد !
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/137229" target="_blank">📅 16:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137228">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وزیر خارجه عمان:
تنگه هرمز باید برای دریانوردی باز و قابل دسترس باشد و از هرگونه اقدامی که مانع آزادی دریانوردی و جریان تجارت بین‌المللی شود، خودداری شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/137228" target="_blank">📅 16:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137227">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2ad0195b5.mp4?token=OJ4VIcQ5L9NKeLr6LeevKw8Ga558m0dRm9XGGfRy96n_e4uoUmo5eeBpJT0jiysfVidmFWJT5yQY4EmL3yKwCjJxHKx3y7VnZcxViXLC48GbBpsekmLFOrewVIOngeDo13sYWF5S6bzirrcsM1F9N7EF7m_bsWvQFC1PBxxLh9bsZvW9vRiADD7dAGk0zCBdE4PaP-Q-dJ5EnACjGFMwhUgJ59wu43sZuqLi5a6Uz3TMB7-0CMtRAxf4MgVGSswOHXblA0snGG6NpOx1AZru9bsq6sUpl1rho5lVv1sQCCIZqmrprT6vVMpCnYN1EIUY-fQ7nCmmomuE9UHtzrV2Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2ad0195b5.mp4?token=OJ4VIcQ5L9NKeLr6LeevKw8Ga558m0dRm9XGGfRy96n_e4uoUmo5eeBpJT0jiysfVidmFWJT5yQY4EmL3yKwCjJxHKx3y7VnZcxViXLC48GbBpsekmLFOrewVIOngeDo13sYWF5S6bzirrcsM1F9N7EF7m_bsWvQFC1PBxxLh9bsZvW9vRiADD7dAGk0zCBdE4PaP-Q-dJ5EnACjGFMwhUgJ59wu43sZuqLi5a6Uz3TMB7-0CMtRAxf4MgVGSswOHXblA0snGG6NpOx1AZru9bsq6sUpl1rho5lVv1sQCCIZqmrprT6vVMpCnYN1EIUY-fQ7nCmmomuE9UHtzrV2Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو عجیب از تجمعات شبانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/137227" target="_blank">📅 16:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137226">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
چندتا عکسای صحنه‌هاش که منتشر شده رو ببینید
◀️
مشاهده تصاویر  زیر ۱۸سال نبیته</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/137226" target="_blank">📅 16:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137224">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/beaR2rpytZf1KsyWvZRkp9SaJ8DoH9YxsUsYYZ71cfPgV9s8JViupuA2ry5IYGfD1QeRSewTg7EpC0fwAXQ0a5BchkR89MMRdBAp5CQEMOZQ0L6g1-1oEiPXbQJP4WnvmbYIQrF374y_Sh765OztxvP7XgjZRHdt4AC_kZ_-yjSjorMjtJPE7rI9BGOANnlxtIhooEx291raxs4Clv_40qY1E3wZvzfU1dCyzjlNLoFJ6S_echerFzT2tLuWZBrSFX0Sa3lq4CBTNx9EraSngohXnJyGY7GeBh3LP4tsWrPA11HyvqXkNVFwRc-mvioihCbANHaJybEwX2AItcKUGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h0Pul3TrsIAi4Cksr2gVZn1QJupDmMzo6sHLQr1bhL7BLfbdt31L5-av7dA7e3RK3lROOGfz6ne1a0nxOQDVcuQ9LdMGcm0w6IZSGHzPbSqnKb4deQmkj9U4Y-GNq53J_Xa7YO70SbMXX1LTpBAjLKpdpNL5zK3I_j1BkWdEc3bSHnBpl_wCS0ogCbaLCX1pVrBL3LifslUwmmacDkRzHZPvOuNBj-gDn0ZbnSLC-ogLXOfoI5wvXDv-M5Qc5XDN76pn-cITvtHE-S514-nq_cgJUFDKHZTnfNyWVTDWWITky-MshrGpgVtC18NYoBeHYG2MuS8xDY8-cMzaI7VHCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بمباران فرشی یک پادگان نظامی در غرب شهر اهواز توسط بمب افکن استراتژیک B1 آمریکایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/137224" target="_blank">📅 16:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137223">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7qzwrc-Ce0M8z8qVRZGHEJwhA9-2p5r0CauCYCq2F6zIxrnapim-w2by9VPL07HPgsE3UVadSsemTvRFdwWNOPDjWQCgPpPOnZeBmlR7Dv--IwLYy__54v2CrUtin9gq12zUsjkOvkiyWsfjHCWEAEtgdiEuIBEtWaToBNyTRcQYPODvDqjmH4di1ES7OtjKCwXJK_wZmeP-zcbmS0WwkD6AqtyXYjVsK1oLu2MdY03IA4mTWkFF6IvcMzOMlu3GwpaeMZNP1YTVypmGLbhjFeZeycFKfx9N1sa6oMylmdZS-kKfWIr2Dh5FK_9vr_PBtv93mF1RWCMEtxdeTNucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی:
آمریکا پول داره اما ما خدا رو داریم
🔴
پ.ن: فعک نکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/137223" target="_blank">📅 16:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137222">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51678b4c9d.mp4?token=lqb31H9uKeFh9D2TQ0QFhFeSOrJ8kJMXmjFuvOb3smLRWKQQW4rwlJozkU9rpvrZzLYytfImWlDjLpaaoa9bbcc6troeiwbTNJtHhl6dv1CXE4ATB-UGNDOaQxRlvrz6VDGLBk5W-WSk4B86ngi978KTXoecEYREPZ1EfnDD91AfnuSDSQPwwZiGCXhRp-csIMUASgdzlkz2anl2Cty-_2lZ-68gMUNX_1NovnuKIfMkcnxezUosat-nygfTRpaV3sUj0Rt0-z6MeKv8ABC2C3coJ4mnofuSnZwKtzPB_V9n2i6msan3O70kybL0Rdd8QNVdlfiLEwFTvmJ1xtwIBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51678b4c9d.mp4?token=lqb31H9uKeFh9D2TQ0QFhFeSOrJ8kJMXmjFuvOb3smLRWKQQW4rwlJozkU9rpvrZzLYytfImWlDjLpaaoa9bbcc6troeiwbTNJtHhl6dv1CXE4ATB-UGNDOaQxRlvrz6VDGLBk5W-WSk4B86ngi978KTXoecEYREPZ1EfnDD91AfnuSDSQPwwZiGCXhRp-csIMUASgdzlkz2anl2Cty-_2lZ-68gMUNX_1NovnuKIfMkcnxezUosat-nygfTRpaV3sUj0Rt0-z6MeKv8ABC2C3coJ4mnofuSnZwKtzPB_V9n2i6msan3O70kybL0Rdd8QNVdlfiLEwFTvmJ1xtwIBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این مجری تلوزیون داره دم از فرهنگ ایرانی و اسلامی میزنه و میگه غربیا و نمادهاشون بدرد نمیخورن و ....
🔴
بعد خودش رو گردنش تتو داره و سعی کرده بپوشونش
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/137222" target="_blank">📅 16:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137221">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080c6cf800.mp4?token=VosMTjXL_jqAQ-O2prDiHQV8jEawUofalAFjYkGjsPv0T5wi0jehryDuS9Xxkd5dGhAvQ7_EOzg6DFaS27xJskS49cUyo49pOi0NkFufQpDoaNuxdnmEzc4JVcv6-12LJY0BN56ym0rQ4-BkHrrPluEV6kKlRqffbO6kGmIU0oa_ksjY3hfOdmbUYsgH32FmsaIb9mTiu6zeBckNv_KDa7LSNj_8NiLBZWR4Iw8w9O6o3SQjE_3b6bhVqR1ymvPoMf3UMz6RrfRJGR0xurJr8k5Nfi-1pHQ5Krr4QHpzeolKTKJLmkXaIWafeZphDQkBVws2YBtXxMtPDMmeGZsJDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080c6cf800.mp4?token=VosMTjXL_jqAQ-O2prDiHQV8jEawUofalAFjYkGjsPv0T5wi0jehryDuS9Xxkd5dGhAvQ7_EOzg6DFaS27xJskS49cUyo49pOi0NkFufQpDoaNuxdnmEzc4JVcv6-12LJY0BN56ym0rQ4-BkHrrPluEV6kKlRqffbO6kGmIU0oa_ksjY3hfOdmbUYsgH32FmsaIb9mTiu6zeBckNv_KDa7LSNj_8NiLBZWR4Iw8w9O6o3SQjE_3b6bhVqR1ymvPoMf3UMz6RrfRJGR0xurJr8k5Nfi-1pHQ5Krr4QHpzeolKTKJLmkXaIWafeZphDQkBVws2YBtXxMtPDMmeGZsJDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مردم ایل بختیاری: علیرضا بیرانوند از ما نیست و سر اون به ما توهین‌ نکنید، ما اونو گردن نمیگیریم چون با آبروی ما بازی کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/137221" target="_blank">📅 15:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137220">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
دقایقی پیش سپاه هشداری عمومی صادر کرده است و از شهروندان در سراسر منطقه خواسته است که حداقل 500 متر از پایگاه‌ها و تاسیسات نظامی آمریکا فاصله داشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/137220" target="_blank">📅 15:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137219">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
بنیامین نتانیاهو نخست وزیر اسرائیل و وزیر جنگ یسرائیل کاتز در بیانیه ای اعلام کردند: ما به ارتش دستور داده‌ایم تا عملیاتی گسترده در روستاهایی که منبع تروریسم در کرانه باختری هستند، انجام دهد.
🔴
ما به ارتش دستور داده‌ایم که سلاح‌ها را از برخی روستاهای کرانه باختری جمع‌آوری کرده و مجوزهای کار ساکنان را لغو کند.
🔴
ما به ارتش دستور داده‌ایم خانه تروریستی را که حمله تیراندازی علیه اسرائیلی‌ها در روستای تل را انجام داده بود، تخریب کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/137219" target="_blank">📅 15:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137218">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Il327xU6sXI5O9tFqVcSZmuRi9y49isW5ccd8PDatsemeuDkNWMGIFIzIWvLuRaMNZ_DNSbYhUHDE7IaxbsiY9R2_V_W_1IWO1p1JwEbcbdnXvZykFtg2BT4oeu6OxAHdMDUNVinbFOivQkzzY6DRa4-yhh-GZQNzLVe_EInh3mX9rT8fg5lkbxNW-kSMidkL7rZFJdaZs9WH1zq7Ka0GNM-MQ7B_7IRdUkChuor4bgxv7WSVyS2Myap1-yzzqbJV40YFU44hxgSiGqK8WHzMWHXTmWli3_g4UWulKqeLnQjO8ioG5u29Z2YO84us6j6sIJPlzTg6Gim_EHZ2uHGew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طالبان آرایش، موسیقی، استفاده از عطر، رقص و انداختن حلقه در عروسی رو ممنوع کرد و اونو خلاف شرع دونست.
🔴
همچنین نشستن عروس و داماد کنار هم در مراسم عروسی رو ممنوع اعلام کرد و گفته هر کی اینکارو انجام بده جرمه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/137218" target="_blank">📅 15:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137217">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ویویان نریم خبرنگار نیویورک‌تایمز در ریاض: شایان توجه است که با گذشت چند ساعت از اعلام دونالد ترامپ مبنی بر اینکه توافق هسته‌ای آمریکا و عربستان سعودی مشروط به عادی‌سازی روابط ریاض با اسرائیل است، دولت عربستان هنوز هیچ واکنشی نشان نداده است؛ همچنین هیچ نشانه‌ای وجود ندارد که سعودی‌ها هنگام امضای این توافق از وجود چنین شرطی آگاه بوده باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/137217" target="_blank">📅 15:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137216">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
صدا سیما : صدای چند انفجار در جاسک حدود ساعت ۱۴:۳۰ شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/137216" target="_blank">📅 15:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137215">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKPUVlPJ9_4Cy9ttF2QF9zQxohAudWsJ_jM3VokMX8MQ_nCJjKBndHkYwRVcjQUhrUeWW8Mc4MH6g-n3zk305d0FySu-vnbcGld0TiPslKB2YlUG647_oTZE5KADBp-UqCfKBll7FhRK_Ir4_ZJRfyICMyWJuTyKTFmt5veNsTndtc2K5DfR6y_fTC_hd2Em-CZcUSZxI3FKBJTv3RtaaVrOwBahCl79dMFqVRGAq1W5NqX_7kQeI35isOyizu0J7X0QjDmg7qmw_Kcm1VK7zsOSt3Acm5RG3j9SB3ZnDRhV6AXnAblvlO9SX_W7AZIINtraHaJ5nZMDvYOG3zsHLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت تورم دانمارکی:کشتی حامل محصولات نفتی به نام "تورم اینوویشن" مسیر خود را تغییر داد و به جای عبور از جنوب دریای سرخ، از کانال سوئز عبور خواهد کرد، به دلیل تنش‌های امنیتی
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/137215" target="_blank">📅 15:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137214">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGIItF5tp9fGn5XqihIIyJ3y_SHcdR00k4u6Mlf1OJZwA3O0rDhuxaEZU8qr8wNdx3THrm3uPUn3E8-31qSk75XIVqlh-yzGR0ItxoPv4iGbnMmT7Ih3pTU0ggakCS9XhfGvQ8VHWI34j6u_uJL44zDvyMWy1wO5EKer19eOFzT4UcfqUbTITN2vPo4arDlnTq2T6tM5Vq-LcTPko_kuiYALEDFmXDlN7W02o_BRJDZ-tKrPWYtPDrsm7ZtqzK38ja8qH6rfbQeluG0MfiYLd7ieQRt-swOf6qk1qHWvl65C8He66F8_IfuVtXpAQTyaQ4A9RnMgqs2w7RwYxUnJ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برنامه امتحانات نهایی پایه یازدهم برای استانهای جنوبی اعلام شد
🔴
مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش، برنامه امتحان نهایی استان‌های خوزستان، بوشهر، هرمزگان و سیستان‌وبلوچستان در پایه یازدهم را اعلام کرد
🔴
این امتحانات در روزهای ۷ - ۱۱ و ۱۴ تیر برگزار می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/137214" target="_blank">📅 15:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137213">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/672cf5b815.mp4?token=bhi2jP7UgJeuUeq_Qv4dWo9smsmf_fiSnE7eXUgTEH4Liik2HTL9s0TNH-CAUKdTSc-FpjFz-9hLvpRaLLN8tbzhvV3dFKJ104_n0kngnzfnSyh7z9VmOiyMwBWDoFNs1u_wfb2UYK3BKVZ_cDCMsyLiYapWBa0PCRIbTlzUZG_XWtVDm173DQpXTfT1FdioqX4AN63ijKTkiH7SHL70W4igaX8vD3oHW46UJSXlD_Jck7zn8PlX6VhNHrNPSNOC7QlJljzUbgOLugVONx5iokiqdn-Aeb2bT62DnImYrHcxX7IL3a5U0nWOr8rJm5KYfaDUKl2g6nwHEzCEBmyYGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/672cf5b815.mp4?token=bhi2jP7UgJeuUeq_Qv4dWo9smsmf_fiSnE7eXUgTEH4Liik2HTL9s0TNH-CAUKdTSc-FpjFz-9hLvpRaLLN8tbzhvV3dFKJ104_n0kngnzfnSyh7z9VmOiyMwBWDoFNs1u_wfb2UYK3BKVZ_cDCMsyLiYapWBa0PCRIbTlzUZG_XWtVDm173DQpXTfT1FdioqX4AN63ijKTkiH7SHL70W4igaX8vD3oHW46UJSXlD_Jck7zn8PlX6VhNHrNPSNOC7QlJljzUbgOLugVONx5iokiqdn-Aeb2bT62DnImYrHcxX7IL3a5U0nWOr8rJm5KYfaDUKl2g6nwHEzCEBmyYGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از سوله بالگرد در خارگ که مورد حمله آمریکا قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/137213" target="_blank">📅 15:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137212">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزیر خارجه پاکستان : با عراقچی برای کاهش تنش‌ها صبحت کردیم و نگران تنش‌‌های منقطه‌ای هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/137212" target="_blank">📅 15:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137211">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d26cedb2b.mp4?token=CFydEWDGfFjzGqPCeJUydM3ypUwNmAkBmNdS-2KxdSFHzJfN1xwG1ua4xpF7POUzBxmJW3YDMc_JFqYfa9gy2cEh_95A3LmlXZ0igIalAtYb3quN9TMzrbHF_8FnFKGduV2xuWhvJeUxtSPk8mH6rqu2MQbTVQsm1VJ2_jA5AHnAKjITJJFb2LpdmybyPTkukjQaHsgZM-ir34-VxlHo0EFWidfkpdTEx9nM8gf8elrMmW7-K-zPyTQ6H_JsPQ5S0NP6C5HoLx7CRXwyQVQR2Gp6qt9bR9F-ud1wxM81b-V9Pt2bkQiBIF5xw295-eyMC3aQRlB14dwwIgy4WjEpXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d26cedb2b.mp4?token=CFydEWDGfFjzGqPCeJUydM3ypUwNmAkBmNdS-2KxdSFHzJfN1xwG1ua4xpF7POUzBxmJW3YDMc_JFqYfa9gy2cEh_95A3LmlXZ0igIalAtYb3quN9TMzrbHF_8FnFKGduV2xuWhvJeUxtSPk8mH6rqu2MQbTVQsm1VJ2_jA5AHnAKjITJJFb2LpdmybyPTkukjQaHsgZM-ir34-VxlHo0EFWidfkpdTEx9nM8gf8elrMmW7-K-zPyTQ6H_JsPQ5S0NP6C5HoLx7CRXwyQVQR2Gp6qt9bR9F-ud1wxM81b-V9Pt2bkQiBIF5xw295-eyMC3aQRlB14dwwIgy4WjEpXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه سرباز روس، بعد از شنیدن صدای نزدیک شدن پهپاد اوکراینی ، قبل از برخورد پهپاد با خودش، با سلاحش خودکشی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/137211" target="_blank">📅 15:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137210">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
فوری / وزارت امور خارجه جمهوری فدرال آلمان از تمام شهروندان این کشور خواست که فورا ایران را ترک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/137210" target="_blank">📅 15:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137209">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
کان: پناهگاه های بمب در جنوب اسرائیل در حال بازگشایی می‌باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/137209" target="_blank">📅 14:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137208">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
در پی اعتراضات مردمی در هند، وزیر آموزش این کشور به دلیل انتشار غیرمجاز سوالات امتحانی اخراج شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/137208" target="_blank">📅 14:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137206">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n6IaRiud4zpcB8D6zDHYwEbRLx28bdqGStfcLHCXpUCzw4_LjlPnizb5AZVCvYVVBSgCtLr9IfIfm8dupWUZqPdttUQUt5ws8-HLzhei4mwEC7mkyoSfEXvifQIGtF3KLvFegZXTzE6Ntqw8P99UWufaFWZ5G2ToLB_UG5kaJCId_UcgPVto7wnb2C8R_GyEa-0VdfkNJiacsNWDrc3sUcT5riydTiNE9G7qK3kIbzd-MpSkxHX3mY7aIk1PY9Hbv_495bv47nN1NM7_Isb-nu9kvJL4meqOvUzonZd9SeiT8Ad0i4guTc-rtNMT-qwppkbU1yysRou6daxZdL6WXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QlJDQdRpKzDRMNMFuga8SY241ErqNP_xj-O_XgdPObtFFC6UI_Kn0gd0mUR6zBDzSzL7-1MQRwM2vuFkYWcJTh31qqexkRzDqomPzNeVN-R5lt4h7kMvbUjBI6UtBAC6_ODHsElcbW9zWapG-laDVByKucbLTyYMER4glt5N3G2w1LeSkuj0QBMATFQXYXpu-h-z5cvLULOONxes4R4ved6XCkXEd55touNyPMrNat2Ru1HrwlUepyxSZ1lo6jGQrR31QdrAuqCzjUJr1CkT4_Erx058aMcA8GYUvZFCoShQf8Own9XpACMXRrZqos1akQDC9Wfaxg3G8RPeSQLQmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/137206" target="_blank">📅 14:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137205">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5Ge4FENWBXsCKnusfx3EmJPPZYL_Qe6IftsTXjFL8dymG7QGC5itFIaZg8KDejtFP2625NhBLY7hx47a_s_Y5nqlRpGDeSG_OOxV7JTva7vXmn0nXEPjYYKGg3f8MK7mXvqXKcnDR6xlpYCQPeeTNBoc7Kpg7iqwgXc6Ztn2vxQ9aVbDmJmu7IhTS7YF98d7ysFDAcKczr_LcyZxoXIXHsV4hvsF6sSMeV0JAi_tauYEukVlJ7qY98vthDbrbAA6ba4x5ZH2vAyh5yeKuXDuajJFEBjoyN27fEHxLhqzJ3z4xYasWP44rytfFovL0-jZ9AvI-VJKR0sRti21_Vqng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دوباره عجیب اما واقعی
‼️
🔴
تو ایتا یه پوستر برا ظهور امام زمان منتشر شده اما این پوستر برای فیلم اونجرز دومزدی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/137205" target="_blank">📅 14:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137204">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bmd_qGF_4RxExHGm9rmBVVCrhHh1UCUoFoSG5ewSXsULvN5dewtoHvF369sSG5hxJNHw_cQTUbyvWpWYN-CUUpfdFRO3eDtRj9xg_VVGx6qYQ58s_YVAK4wI7lUlcX0OqztpDlSQ9giDlUQmOldWQI1v3e4uLrSB1IaN72QvMFnV6CIE_7rkrJaxluEvz0-SH84P8d0B2c5VaGQ29Hb9Eg5Rmos73wLpGhDyR-UWa0ycji3Z3ZAOqfKjMbggVCRKH0ZNPOYXssgSmvHsTfocLBhtvUW6VkZG5FDo4gMmT8fDFTYKMSdEZs16QRk7Gi0vNC59bAMxNEXCNqWStpx7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
روابط عمومی سپاه تو پیام رسان بله یه حساب باز کرد اما به دلیل ریپورت زیاد دیلیت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/137204" target="_blank">📅 14:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137203">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
رویترز: ایالات متحده واردات سوخت عراق از طریق سوریه را آغاز کرد. در ژوئن و جولای، سه تانکر «آفرا ماکس» حامل سوخت عراق در بندر بنیاس بارگیری شدند و به سمت سواحل خلیج مکزیک حرکت کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/137203" target="_blank">📅 14:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137202">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/882fddeff7.mp4?token=UpKwPu8mwkMrUi18NT_BQ94v5K_pezlOaiLBNr0XPZLHVZr3X1e1V58UGUdPDAx1GKRT1yuDwzBefif3WdOBa-G8c6KLr1Xv8i8qVjghIOuMDfOXEE7e4szGw23ZVfJnTMN-HBWMZV4xWddSeEBzuDwP1oqtYPMiKkHObtBRzjEOAsfaUqW861iz763W9FtKWvYqh3z61d5c0xaW90pjFQ1NS458kzaW3-pOla2RDYXgKKJQOA9AMrJZD5y1ivawNbAtlSVDydRUtRpFbDgo_xRkKrKmqoGZwUhgY_b5HGzsvDmNXhhanbCQ95uZeVq8FP7lme5Vv7JfGgbM7WhaBXKJRb9Z3M4LfdwXblcjbiAtdn2jVRJytyAMTvGuqEH_VcHhtBNXxEZLzL7fpC7NyEalOY0TzYBooFU8QjOuCRdZ9t1keAXMODDNA1dmd2F3-ESuMSlIe0Kp9l-tZJJOwQdBCwmBCUsTdAVLhi199XW141tZUGl17Fl3fIVr4wFM88ynF-GAx7thOxossGCLnT5mec_Pb21hIg_Azezzhv38se2l56mGOk0kJ-llrcgnTiTsP0uHVg8Z2bUJI5BMPuFQz93jfnlcMmZH8Xcu0VXu-y9ngdFhaFO62r7Wj-3tQEKtUNUzD6izJnL47II5jKWoyZ_E5bitSBKpxneP5K0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/882fddeff7.mp4?token=UpKwPu8mwkMrUi18NT_BQ94v5K_pezlOaiLBNr0XPZLHVZr3X1e1V58UGUdPDAx1GKRT1yuDwzBefif3WdOBa-G8c6KLr1Xv8i8qVjghIOuMDfOXEE7e4szGw23ZVfJnTMN-HBWMZV4xWddSeEBzuDwP1oqtYPMiKkHObtBRzjEOAsfaUqW861iz763W9FtKWvYqh3z61d5c0xaW90pjFQ1NS458kzaW3-pOla2RDYXgKKJQOA9AMrJZD5y1ivawNbAtlSVDydRUtRpFbDgo_xRkKrKmqoGZwUhgY_b5HGzsvDmNXhhanbCQ95uZeVq8FP7lme5Vv7JfGgbM7WhaBXKJRb9Z3M4LfdwXblcjbiAtdn2jVRJytyAMTvGuqEH_VcHhtBNXxEZLzL7fpC7NyEalOY0TzYBooFU8QjOuCRdZ9t1keAXMODDNA1dmd2F3-ESuMSlIe0Kp9l-tZJJOwQdBCwmBCUsTdAVLhi199XW141tZUGl17Fl3fIVr4wFM88ynF-GAx7thOxossGCLnT5mec_Pb21hIg_Azezzhv38se2l56mGOk0kJ-llrcgnTiTsP0uHVg8Z2bUJI5BMPuFQz93jfnlcMmZH8Xcu0VXu-y9ngdFhaFO62r7Wj-3tQEKtUNUzD6izJnL47II5jKWoyZ_E5bitSBKpxneP5K0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما کدام بخش از صحبت‌های پزشکیان را سانسور کرد؟!
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/137202" target="_blank">📅 14:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137201">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tE8Y8PyRrUWlIAYEOOZzoeHilW-CpGAPURGYfqHichgtn7SWnHRKNH73hpIgva9OiGjpn9sTFbXBnQy-_87dtk2vzuYZqXi8FULADxwscxBYdgLnNr48PhKF81_MYul2__xf06BmhL9QIsUAYSbbQeRnafNcbEbUsIxfpKTWJqFwMaymUAhaxAHHqSTEAiDavxCM9yI4cWH_CIrhaiSTgXn0WPllp9X1jMT4QO3bwUChVLKLpGvWQCBCD7cVP2L8ZQN_Zq1EBm3D9q4U4Z38B7Ib8RzIbobUFFl8nddWroccizIF0829iOyX-L3rPpdJ0nX5Lct3hWY1F8uyJGEkfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مبین، مدیرکل تولیدات رسانه‌ای دفتر رئیس جمهور: سانسور سخنرانی رئیس جمهور پزشکیان در جمع تولیدکنندگان و صنعت گران توسط صداوسیما عجیب نیست، وقیحانه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/137201" target="_blank">📅 14:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137199">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
دفتر الزیدی گزارش نیویورک تایمز درباره میانجی‌گری میان ایران و آمریکا را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/137199" target="_blank">📅 14:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137198">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
عراقچی: کتاب نوشتم، «قدرت مذاکره» نتیجه‌اش هم داریم می‌بینیم.
🔴
همین دیشب یکی از وزرای خارجه آفریقایی به من گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران برای آموزش
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/137198" target="_blank">📅 14:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137197">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ab99fc66e.mp4?token=RfJCs0q_-RxSuF7I1BACYdJGdwGoBaRmEdxY8-zLEQ2O_o47rTr4jee28Ubn5EL2Uxw4Gf5GPBcBLzVKGSy_3uUrduSdF1ypAQgo97594p_Ebr0_D8dkYtD8fcErPGsY-UA00DArrGprOrv3LbbyJktDnFYjcRudSPUzX9tgZVFPSveBCpraliVXjAu2siA4ZZWH9NZ93xwNVbjOi8M41IwXt-VR6f_0d7uJxuRlFL2lJt6cMDXoYobQZCdqJ747rrWaWpqv5sSxbT1g9Ku3Hiuhwe6WxuWjHoOFINbU6JiU8RNP_4wfWPwZZoWih5zToDatc5KmEb8HbfN5HHtn0JiM9w0R0cLyqbjc9eSrsj9ZzwR_9fCppkHz7bwsbjIeU9VfBUHRFu5QpV1d6GB4hliZxHHiTdbV6lnXS5Vd8X0c4C2CyZbP5W3wzLbOHjyX6GjupMvPPKptsv8dQKqUAHvhdw-beBe3TSuC5nHg4rxz1-zjgqN9c-Zv4CSyjbSCSIAg8ffNH8oFQS8fUAM1ZTYeAcWayIsNKwWAjS-dVaI0FWSEeb2Zcv2_fEkeDX5iMRi-TUCJjBMoa8JVpP0LReRJri0hgjD8QKVhvcIULHfpaUEUf2JzCqDO-bXd87UFBfxccTJCKjGT-Xl2xLx7X5KzEto6zcu_3suaMCri4gM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ab99fc66e.mp4?token=RfJCs0q_-RxSuF7I1BACYdJGdwGoBaRmEdxY8-zLEQ2O_o47rTr4jee28Ubn5EL2Uxw4Gf5GPBcBLzVKGSy_3uUrduSdF1ypAQgo97594p_Ebr0_D8dkYtD8fcErPGsY-UA00DArrGprOrv3LbbyJktDnFYjcRudSPUzX9tgZVFPSveBCpraliVXjAu2siA4ZZWH9NZ93xwNVbjOi8M41IwXt-VR6f_0d7uJxuRlFL2lJt6cMDXoYobQZCdqJ747rrWaWpqv5sSxbT1g9Ku3Hiuhwe6WxuWjHoOFINbU6JiU8RNP_4wfWPwZZoWih5zToDatc5KmEb8HbfN5HHtn0JiM9w0R0cLyqbjc9eSrsj9ZzwR_9fCppkHz7bwsbjIeU9VfBUHRFu5QpV1d6GB4hliZxHHiTdbV6lnXS5Vd8X0c4C2CyZbP5W3wzLbOHjyX6GjupMvPPKptsv8dQKqUAHvhdw-beBe3TSuC5nHg4rxz1-zjgqN9c-Zv4CSyjbSCSIAg8ffNH8oFQS8fUAM1ZTYeAcWayIsNKwWAjS-dVaI0FWSEeb2Zcv2_fEkeDX5iMRi-TUCJjBMoa8JVpP0LReRJri0hgjD8QKVhvcIULHfpaUEUf2JzCqDO-bXd87UFBfxccTJCKjGT-Xl2xLx7X5KzEto6zcu_3suaMCri4gM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دومین پرتاب استارشیپ از داخل مکزیک این‌طوری دیده شد : استارشیپ بزرگ‌ترین موشک شرکت اسپیس‌ایکس متعلق به
ایلان ماسکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/137197" target="_blank">📅 14:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137196">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
ویدیوی جدید از پل کهورستان شهرستان خمیر که طی حملات دیشب منهدم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/137196" target="_blank">📅 14:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137195">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXIJ744eJPvyrNJMkx6TaCsam4E6FN7nc4jPRuX05Mi558Hoy46twNmSwt0vJiigi1iQ1c4hZppUskdTYVFYg6FbzIBtcUCnxwXA4fA4Q_hR_0dUrOpUVQsA6M041bVAGzeguW8SWwJDDMT-T23a7kPzNl-ogwcdUbh2npm-XracZw9YSWFa9OR9Gn8Ilijwqgr02i1fuOlBnkpy7n668TJoFDxRs4IIZAPk3W0dZGEwx9YVoCrFVNlG4DSi8sJt2OXgulSieMvhxZRCMYiWY-VEBNS_CEL7c5xeGjJaRnIKW6WlERA3RG7c8DYwwHYd-1oklP0kdlZdZehCsbB2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واردات LNG چین هم به بیشترین میزان در ۲۲ ماه اخیر رسیده است
🔴
چین از شروع جنگ ایران واردات خودش را به شدت کاهش داده بود و جهش تقاضا این کشور می‌تواند فشار قیمت به LNG در جهان را افزایش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/137195" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137194">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeDXL546OlbgIKZ5swibT3peGzldPIYGw07cBUIPdfE9uRL1-g1l2vb6oA1ULnXlaIJFFpoVJY1kaUXxYgS0uK31_HF2grqkXxzxbeUoEf5qvLOS4zx85cfq5b-te6lEhnQO7HsGCvzcg0b-Vd5D4yGye530GK24nPv5rxdE3h2bQ9tWhTm7UZRbNJrfQpiam3CiUmMLIlP5_la9KIj43lxVoft2qFHLRcCnERWhZbS4ScDyHvnTOqdPCbV5MZC7ki2oO8NCOyq9J92dNw0JJKGsej0PyyBI01ZUmRS166fiVamxEPg0puDpBx4JN3JyKBCMlZmEqTKgKFZw44UCjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آرامکو عربستان فروش نفت از طریق خط لوله سومد و بندر سیدی کریر مصر را شروع کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/137194" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137193">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Grrhtd0GffkJ-u5kpTYMSoIbCsdyY8_ZmFiKYiSVac_-csbzbjpnct9qrltw5QjUhC9qQidzSv4TFVCBBDlOXCgHFsueH-6Y1sl3BN0oy2aN-Mj0Q1CdayBTS9b8TqaKchgveQ-H12Vyw_CHmo68mevuhJaM7D2gwlnCX3u42j_G-g7IQVHLy7taHrIhGyxz6g-tbrPThjUiIcH-i_jJB6C6TEIkOQca-6QxzYB5NpH44dPD041DpjYm83sQF7jRh-2vRqtGdbLLpIsuUEcsKRHE8Z59szyG_H0NdKeHiQJ41Umcj8yfLcL-NGVTRzF9LC-gQwLzKqrI5EwyT_xqrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما  :  یک سر در برابر هر چشم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/137193" target="_blank">📅 13:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137192">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VR-Cak1co2_z7RmTm9QF1q6Qv7DZZJe7NGzaKeM4eRwu8RFDo3_UJoqzaCVB_-mwp0KXyn5nyvdzeDj-lFLDnsmWq5dc6JrhaagdApXRe29hsWuSQntlHIZhJqPASAJmTUNDGvUoGNBay0uECAgNHabAgybm9bWEo0rrtzQSOUqALXw7AmbKhtwyTvs_6tNaAt476-Q0GkBTOOrfgxS585s5Sw2zPc3lj1vrHzMV6Wh4JWBw6WUBbRcgW0G_y5pc-5rLVGA4zY43ROWhmiygKU3mnS4HEeJqowytBfYPW2VcZPz7E-4TaZSEF_nULtP_e9Cwm7DQzWlDQ2tb5HAjFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو هواپیمای جنگ الکترونیک EA-37B کامپاس کال دو، مقر انگلستان را ترک کرده و به سمت خاورمیانه در حرکت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/137192" target="_blank">📅 13:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137191">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
عراقچی: عراقی‌ها استقبال عجیب غریبی از من کردند
🔴
عراقی‌ها من را قهرمان خطاب کردند
🔴
صداوسیما سانسور کرد و پخش نکرد
🔴
برخی به ما شعار مرگ بر سازشگر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/137191" target="_blank">📅 13:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137190">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
پلیس فتا تو مشهد یه دختر ۲۰ ساله رو دستگیر کرده که پسرا رو میاورده خونه فیلم های سکــسی ارباب رعیتی و فیتیش پا و... ازشون ضبط میکرده و بعد به قیمت های بالا میفروخته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/137190" target="_blank">📅 13:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137189">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myL47O1tp2WCo6r6NpUslScm_5R_rJyqkwwbefHy2gZkfKyyRLxJhhvjcAxJd3j4SrG34W7i2nNQlE7oQUCLczYRWGO9BH-PyhcjMlwQS-SjRBPli4c-j7ugB5V6ore57VS2Ay43qML45wksrCaF9Fh8ijMOJHZBf9TXM4L-ngYyPp8RwZdNE8PdDxMxCDX3b8ygkuPQweWvmJ443MvmkIA4yJH8arQjIl1ftRBGW_h2M13rU7EpcKMvyVRSUhehRXBDnaB1ciYTPeHWLrS4H29gnv0flkk8aE_hZj2LQZ8-n80xcgaeidAAIa3O6PqBUxAWnxXp88c00vBODs4Pvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلیس فتا تو مشهد یه دختر ۲۰ ساله رو دستگیر کرده که پسرا رو میاورده خونه فیلم های سکــسی ارباب رعیتی و فیتیش پا و... ازشون ضبط میکرده و بعد به قیمت های بالا میفروخته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/137189" target="_blank">📅 13:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137188">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
نیویورک تایمز: ایران، پیشنهاد آتش‌بس موقت آمریکا را که توسط دونالد ترامپ به تهران ارائه شده بود و توسط نخست‌وزیر عراق، پس از بازدیدش از کاخ سفید، به تهران منتقل شده بود، رد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/137188" target="_blank">📅 13:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137187">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
رویترز: در ۱ مرداد، تنها یک نفتکش از تنگه هرمز عبور کرده و این کمترین میزان از ۱۷ اردیبهشت تاکنون است و هیچ نفتکشی نیز وارد این تنگه نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/137187" target="_blank">📅 13:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137186">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYkqfdZeCV0QfGv0Am33gFDvAdSwI2v0Xpx0u7R3JJVCXjtQNwXQGyWG8jmAXytNo4f8K3ABCzWSXpN7LAvSJk4Q3xIuA3knSG6wndCnf7yI4bab9fTc-VySQAYc3hdRIyMvEVZ44o0mROQD3UJJ8PG8MzKvN5zDQ5t2_BRj0FGalTE3jCSl4YhTvLpIxM4iykwRdS7OSvFhNpBF8pRj5o66GqE1VbKjm_-LswOba4IQjDH7T1Rzb6MR1qyQUSFjKgPq1_LHhyr-Y4FBGigKofOhKlf7i3LococfAqG52TF7BJvfr2sMVqaUF9TCvyLkTBdMvKsS2_eT70zOq47IEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بورس آمریکا همچنان سنگین داره می‌ریزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/137186" target="_blank">📅 13:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137185">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2EojfSDvHyquYhE0CsqIwL6OTcAigk3X8oSIBP_2rprSnLRwOFGX_BbfWLrKUz070JA2B_ZHTo3oCDBKmXUrMn-E9EKzFVe2OR73YIaoOBhmdntR1iJwOw_qrm6dpdV_4VKeuTut6B4MQ62CSrq1l-tkhr_xJuWtCnd-79deYv_DwKnwyhh93JhYa9BKd-tDHkb6BSsSQtzRkglhalpefV42aeG2ZHsM8m1XPBowBVzBa0vAJg-Bzq3YD54wQnvE91VWoLQLBJVBWCE80t8NDwGUIbVLoLQvbwjJ5cYIulk6Laa7SYslali5dVDtdBoQFKfsHAml23KX_6FWjWJDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منتسب فیروز آباد فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/137185" target="_blank">📅 13:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137184">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=KqcKjSrJGWgMVatgGLMeoNB1sDYSlFo46yyHsbS4zc5oxFt1fLARm7-LF8MxBjPxhKYn5rrukYvoMERfHz5JRHv4hOx2gI5Qr-F0nqzvFATAsIQWmkSzSJmCEfe96pkJTdSxj3rTSIbtFURYHr9jdRw0VtThhJisON2OhF07vssO9Y-Grua9elW5wS7jEk-HX4-jb0cSJ80Sba0USr6YE00G56mntYa-0uY64VBsxuUUJsdSyN1yKpHFT_oUuEF5_hjyqLsnaxfzZVYln_UecWjXqayulFQ5QpyFytLwNvtTM11nRfQhLQu-_zZwaXYlf_zTW-q_DsMtPGypvCYxIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=KqcKjSrJGWgMVatgGLMeoNB1sDYSlFo46yyHsbS4zc5oxFt1fLARm7-LF8MxBjPxhKYn5rrukYvoMERfHz5JRHv4hOx2gI5Qr-F0nqzvFATAsIQWmkSzSJmCEfe96pkJTdSxj3rTSIbtFURYHr9jdRw0VtThhJisON2OhF07vssO9Y-Grua9elW5wS7jEk-HX4-jb0cSJ80Sba0USr6YE00G56mntYa-0uY64VBsxuUUJsdSyN1yKpHFT_oUuEF5_hjyqLsnaxfzZVYln_UecWjXqayulFQ5QpyFytLwNvtTM11nRfQhLQu-_zZwaXYlf_zTW-q_DsMtPGypvCYxIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رائفی پور: آمریکا به روزای آخرش رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/137184" target="_blank">📅 13:08 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
