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
<img src="https://cdn4.telesco.pe/file/gTOIanrsI1ly7AImjH5l-r6-FiuqlGSWtyUP-KWSmLmpESTfDeIUU_WzlR_MvKBmvBBmBwBy9xFJ7v71dLMMexw5kA9HTQRqfXcEf0BNjETyOWpYgIFhpX4tMMySIxYbfuzBh6jgtnVgCHIhVkJo0sKI3CT_Sy1hj2K7D7VIQEK0o9TdJZ21y67VmWlwW0GrlS9arBAT4R4yGtrcC3RHzDpxXoIIFC86RQhfcw3YzIZ8VwOuEEhgKeXbqiGeO3eS6ASTD2-VxXfY_fQfjmWwG9jOM4qGMSlZjMSfkzXMhBoERHPML90RNP8K4gpXV3MSwrpvNaQdTYCwwmjUBBMGnw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 125K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 04:40:56</div>
<hr>

<div class="tg-post" id="msg-70019">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/news_hut/70019" target="_blank">📅 01:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70018">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=GZ-BQqJubhi7EbwL2979754gvGVsudG6JM0mShYliFBJpIfwDJv3dpRBUYcvqRat5zeM_IxLbzewUsw0BpCJyssi_0qtlp9Jix7LTDuBAeNkQHpOvEQfU8A8W6GUMtzt4P1VXLxvhOWaEeeU7QGebyk0j_98NsbLrb9nEia3SUygX3MQo7aDVeZt5tfX3VctDWYysW72Y7YBimo_Kp4FMZ_H00ILAGMytRRmvp0s_rjjpwrVPYiJLnnXKkSMhsUmwXAh3gJHFTamlcJ6f0XHk-1hAShaBIVdzfcfUmFyBa71G7OB9vsqux5NepQExQmgDSHW51xFfnKI17JURrfiMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=GZ-BQqJubhi7EbwL2979754gvGVsudG6JM0mShYliFBJpIfwDJv3dpRBUYcvqRat5zeM_IxLbzewUsw0BpCJyssi_0qtlp9Jix7LTDuBAeNkQHpOvEQfU8A8W6GUMtzt4P1VXLxvhOWaEeeU7QGebyk0j_98NsbLrb9nEia3SUygX3MQo7aDVeZt5tfX3VctDWYysW72Y7YBimo_Kp4FMZ_H00ILAGMytRRmvp0s_rjjpwrVPYiJLnnXKkSMhsUmwXAh3gJHFTamlcJ6f0XHk-1hAShaBIVdzfcfUmFyBa71G7OB9vsqux5NepQExQmgDSHW51xFfnKI17JURrfiMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a22
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/news_hut/70018" target="_blank">📅 01:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70017">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0J8Rq0PlguRrEgYQpHQ1xOjn13It-87v4Ipw87Qlq5KpL6c7UIwrB5neTetkUlOcNRlB9ERRYkc-ZAGVbVWtjEYbBIG21PfFseOP6rKUDF9jKslbAyGQq8HUvI54ey9Vyv-rgazyWVRlZlXRNLSg_q5mkas_PTqs-VFB-0ZuUoXtgIP_oosj1M6X87X0IyO0jKSkhvpPbxpweQUp2web2SZmF6NY9FtgL1hrUQMNFf5T002_1xHhn9E_9JbJb06dHYI3OWEV9P9WzdtPARDl3IY7bn7XnBGKG1435nmV6PRUY35O4RJnHxlquxqoEbiq_aargbr1TZi5avWnH7wGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
محمد مخبر، دستیار رهبر و عضو مجمع تشخیص مصلحت نظام:
راهبرد قطعی رهبری مبنی بر تغییر وضعیت به حالت تهاجمی در صورت عدم تحقق شروط ایران، بی‌تردید موازنه قدرت جهانی را دگرگون خواهد کرد.
با توجه به اینکه ایالات متحده ناتوانی خود را در حفاظت از متحدانش در خلیج فارس به اثبات رسانده است، پایدارترین مسیر برای دستیابی به نظمی منطقه‌ای و جدید، پیاده‌سازی سازوکاری اقتصادی-امنیتی برای تنگه هرمز است که مستقل از تضمین‌های نظامی واشنگتن باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/news_hut/70017" target="_blank">📅 01:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70016">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ed6d62f0e.mp4?token=PqY8yhTzDWw-DtEYuYHnzyswRrVHuOGoWC-3BerP63E9pAKNm3OdIO11CX3YXaoUGkdZyPG5tYnn3B7BlQedws5GC_tPThQlREyprMeQZViJaxU3fjkn8AorfYG_aKbATf-Pbgj5iS2C_PYl1OQWHEN3Lu8v4LzJpGi-BkzCnF--0-WTJSpbjWisgvQbi-35rNTOdug3XY64kMhojR_IcuYfUbXYazXhP4mA3Y9KouK6KY38DXJthW-rVz-9p55oF-c8mblc2pgCqikIEhFFs9irm-42s8j2eiftvAT2ha8nbfL6wjrfVP6Xw7HXf2jEPRaGvuI1ijMr9FnN-i5pgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ed6d62f0e.mp4?token=PqY8yhTzDWw-DtEYuYHnzyswRrVHuOGoWC-3BerP63E9pAKNm3OdIO11CX3YXaoUGkdZyPG5tYnn3B7BlQedws5GC_tPThQlREyprMeQZViJaxU3fjkn8AorfYG_aKbATf-Pbgj5iS2C_PYl1OQWHEN3Lu8v4LzJpGi-BkzCnF--0-WTJSpbjWisgvQbi-35rNTOdug3XY64kMhojR_IcuYfUbXYazXhP4mA3Y9KouK6KY38DXJthW-rVz-9p55oF-c8mblc2pgCqikIEhFFs9irm-42s8j2eiftvAT2ha8nbfL6wjrfVP6Xw7HXf2jEPRaGvuI1ijMr9FnN-i5pgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
📰
آیت‌الله ونس در گفت و گو با فاکس نیوز:
قیمت نفت امروز به شکل چشم گیری نسبت به روزهای ابتدای درگیری کاهش یافت.
ایرانی ها غیرقابل پیش بینی هستن و گاهی به تعهداتی ک میدن عمل نمیکنن.
این بحران با تقویت موضع آمریکا و با جلوگیری از دستیابی ایران به سلاح هسته ای پایان میرسه.
ثبات تنگه هرمز یعنی ثبات قیمت نفت و گاز شهروند آمریکایی.
ابزار هایی داریم که ایران رو وادار به قدم های بعدی بکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/70016" target="_blank">📅 00:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70015">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23ef24fbad.mp4?token=GAG0m2DOeZ_M8uNz5POGNwxjFtzfhj2HmWZB1DJkWRJ0hGLgj2UrbT6yCkcBqnClcv5F9cEYnjb0EKqYbOSSj_k2HT5ddU6AJX30LF8gUCZpy6hktXH748vZQWAD2ildkGa3T281tKeKMXOfXAZaa_zMcJxX4dEhTAw7tk1GLjeHjFw1RKcKBdhERVwcVjQtQLKN0KZofgBwtpKbjaTxHdBn7Frhb6QrzuF08VaupN5bYB1MwJ7auuM4TNP0ykDr4SuKGvA0UqHoJL_uLFiCVbHnRiitM3xkB-hx4hnYdX2271Ytb6CebnBqN4wmSbNkgtgj-Td3xcsn5FVXN0K3Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23ef24fbad.mp4?token=GAG0m2DOeZ_M8uNz5POGNwxjFtzfhj2HmWZB1DJkWRJ0hGLgj2UrbT6yCkcBqnClcv5F9cEYnjb0EKqYbOSSj_k2HT5ddU6AJX30LF8gUCZpy6hktXH748vZQWAD2ildkGa3T281tKeKMXOfXAZaa_zMcJxX4dEhTAw7tk1GLjeHjFw1RKcKBdhERVwcVjQtQLKN0KZofgBwtpKbjaTxHdBn7Frhb6QrzuF08VaupN5bYB1MwJ7auuM4TNP0ykDr4SuKGvA0UqHoJL_uLFiCVbHnRiitM3xkB-hx4hnYdX2271Ytb6CebnBqN4wmSbNkgtgj-Td3xcsn5FVXN0K3Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خورشیدگرفتگی دیروز از نمای کابین خلبان هواپیمای A320:
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/70015" target="_blank">📅 23:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70014">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c94cf4401c.mp4?token=grueWc6SAv8CE38LBLQQhkP9ub_qWcRYoGzBAHG23RoeDje-s-Ky8vxeYCZzSmjmdbE1yjxrDrW5q9IaXE1V20VWZuoQ6VL3kjWoN4PzLTABHBZjCyP-Nun5qe_dCEJ_CyOQObJxUT-TDkxcKT0JqwqbJTqr_LZDGQCVVruWweVtTCYI72TqvGblhMQGAkNqfgJ9PlcMkxGdWGOZBWo-nk1eXk81XVrNrtbHu55wQu7SWKhSffI4Sz7-sfXPfLY8RRJ9bxaHfnqwxUXXz7B5BnMihA6u-18I7VX7zLECMWOM-8wQrjXCalFk-j-nmQ0KI_-_YNL6FK32hsR2Sle55g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c94cf4401c.mp4?token=grueWc6SAv8CE38LBLQQhkP9ub_qWcRYoGzBAHG23RoeDje-s-Ky8vxeYCZzSmjmdbE1yjxrDrW5q9IaXE1V20VWZuoQ6VL3kjWoN4PzLTABHBZjCyP-Nun5qe_dCEJ_CyOQObJxUT-TDkxcKT0JqwqbJTqr_LZDGQCVVruWweVtTCYI72TqvGblhMQGAkNqfgJ9PlcMkxGdWGOZBWo-nk1eXk81XVrNrtbHu55wQu7SWKhSffI4Sz7-sfXPfLY8RRJ9bxaHfnqwxUXXz7B5BnMihA6u-18I7VX7zLECMWOM-8wQrjXCalFk-j-nmQ0KI_-_YNL6FK32hsR2Sle55g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه وایرال شده یه زن باحجاب با یه دختر بی حجاب توی میدان علیخانی اصفهان:
زن محجبه: اینجا همون جاییه که معترضین، مامورای بدون سلاح رو به قتل رسوندن، نظرت چیه؟
دختر بی حجاب: من خودم ۱۸ و ۱۹ دی کف خیابون بودم، ولی اصلا این کارای وحشیانه رو انجام ندادم.
پهلوی مردم رو تحریک کرد بیان تو خیابون، خودش جرعت نداره تا ترکیه بیاد، چرا باید طرفدارش باشم؟
مشکل ما داخلیه، اصلا ترامپ کیه که بخواد دخالت کنه؟ اگه یه اسلحه به من بدن، با اسرائیل میجنگم.
آخرشم یه دفعه متحول شد و اشکش در اومد و باحجاب شد
🥹
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/70014" target="_blank">📅 23:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70010">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONoBqcWRYNG-eMu3ie1Zd1asoX15_ow2AlVHLC37S_fJ7k_ZSDHu9NniJlBZ8Wj_O28D9G8B4OW2TVSDxzjHW4oW1VDemPnHEl1fROcdrCyru1N6eKnLNjJGSesNx47kD9CMAtEuQVZNgFXS_gCl8ju-B8bo4XtSOrRjRKk23LB8uxILK_fM86cFJcGKITz1OyVBnHy7MiW8VyhR94E6ceFRDbi45k6coBdAJQkBrQNeX-EXgtpe3kYmKGnyGNBUeTYKBtCFYm2a7MF7x5z8fTAaa0Nyw8743OcBeE2v445OW7fGVzyMv2c6ag8O2fhKvxf7nguP2WRE7N5-utceBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LM9e-pn-n8QohzLnh1pQPMtE3cmuLY2TRlQKON6RzCL0zvkKmNuhpiVpHrwzdoW-cwDLTEHc7Zfk0AqpCX9CsGWUgzNP8QxR7u-Hu27NO_iapu4Gc-ojbTw_3azx7yuNdE1VyJ9ZouLAiqouy6eG9NZFP5cYbCeb-1MljO7oVWbDIQfcN_-zZ2FHkYzDhI3XWGr--o0bdG60K2Ln0rChvHUa7fcjaHv29z2gwwRGm4sHS3-zrd6bmvcvLiM-XHWOJUewRXeKUf9Mbi9QS0dYh4eo5EdnR2Xv3FAljHF9QEvbviYMhzpma9VLt7TNT6xLU3NXbQEkrvnpPvu9Uh0yxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T__-2BUel3DqUwAmE1q7A-zzOC2PseFUlQhiJBOVdYxsbfwRHWP78LspM2v3SnrxXrCli_FZ4xm7COP_kOV7Qw4TMnk9l1X-6IWVU1R2TT0QYg16yPAPtdoXhazSp9a_XPGCd-6hofS0GvFDadtRbO4ZTK_EGBuhbFc_r4e-NKxOAzL6ydyRL8oVETeGVYd0P8MBy5hTsYi7kOv0xIh0YFcnEeFgVE_yPa1VvLpIpqbgMK6uQ2SCrzzNXHwdre1yOswXs4lty0WVW_j4GXMVtym1CeM_AnNW7ZUnXypkEEm68SwndKAGj9kmrQJEhzMpeq2rkThR2grEB9GU5X82QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f63b04c02.mp4?token=M1nkmh1wz1ejtbWOGyHytu7Q2Ty8ivyYclpFYVFQ5uw1yJ7VpZKrxW1NRClqwsTllW76P_4DAieBGgC9yjhBj00f_gxYnwaFvtCGnn0Z1v-AU18lLwkTyQp2WJmQuI17u9en4dybms-qrrN3mpjwYPDPpu8BE83T9dQBuEOwwn1vnwzVrHB5JZLrXrkBCXsUFHuulZ22eI6pKnIdEMoyy7KV-4cQEF74HFwuYiaT1lBy8G8gNWN3AQyLgHc8dUnNwyqGRJ7X4GcJK6BkUuEMCENgHNpFd_2msV9j_WhQrR5LOv6JrX0KwoacDMiJZz9i7BPaF8HXtnTKNFqmx_X66g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f63b04c02.mp4?token=M1nkmh1wz1ejtbWOGyHytu7Q2Ty8ivyYclpFYVFQ5uw1yJ7VpZKrxW1NRClqwsTllW76P_4DAieBGgC9yjhBj00f_gxYnwaFvtCGnn0Z1v-AU18lLwkTyQp2WJmQuI17u9en4dybms-qrrN3mpjwYPDPpu8BE83T9dQBuEOwwn1vnwzVrHB5JZLrXrkBCXsUFHuulZ22eI6pKnIdEMoyy7KV-4cQEF74HFwuYiaT1lBy8G8gNWN3AQyLgHc8dUnNwyqGRJ7X4GcJK6BkUuEMCENgHNpFd_2msV9j_WhQrR5LOv6JrX0KwoacDMiJZz9i7BPaF8HXtnTKNFqmx_X66g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🔥
🔥
🔞
با انتخاب کاربران کوماتزه یا همون Comatozze اهل کشور روسیه به عنوان بهترین پورن استار برتر سال 2026 از نگاه طرفداران انتخاب شد
ویدیو های کوماتزه بر خلاف دیگر پورن استارها، فقط با همسرش ضبط می‌شه و بقولی به همه نمی‌ده!
بخشی از ویدیو های معروف کوماتزه:
🔗
پارت یک ویدیو ها
🔞
🔗
پارت دو  ویدیو ها
🔞
🔗
پارت سه ویدیو ها
🔞
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/70010" target="_blank">📅 23:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70009">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e68930a72.mp4?token=E-ioqqTQXH6XiGbgxW2tA3FwRJI7ahgwSz3XDtM8x7uSsHGjPca2-RZefHYwNxPXvJePNb4yekavvUfMcg8gebNK3JFVnliX6gV6eN6vNZlqvPlw4IjQWhDn2ohg9AEWfAgaC4g0yV6p4d4bFeTOQsw7JkxNULTe888h52QGTDeVCmSjlcT_m87xPe3qYmb0s1Nl_oHTyhkXGumdpehdgVoJaX9DtsqXeLnuzuUnTm5SqKQ7mafSKYSk5Ef8H3QOLlpzrInTe7iH6SyESeAsv0VdA5rk31rfZtpNEY7UIJBpU7DPiLJ-JzlFjO0qitLF4gCejYT4RJZ6f1hODZflxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e68930a72.mp4?token=E-ioqqTQXH6XiGbgxW2tA3FwRJI7ahgwSz3XDtM8x7uSsHGjPca2-RZefHYwNxPXvJePNb4yekavvUfMcg8gebNK3JFVnliX6gV6eN6vNZlqvPlw4IjQWhDn2ohg9AEWfAgaC4g0yV6p4d4bFeTOQsw7JkxNULTe888h52QGTDeVCmSjlcT_m87xPe3qYmb0s1Nl_oHTyhkXGumdpehdgVoJaX9DtsqXeLnuzuUnTm5SqKQ7mafSKYSk5Ef8H3QOLlpzrInTe7iH6SyESeAsv0VdA5rk31rfZtpNEY7UIJBpU7DPiLJ-JzlFjO0qitLF4gCejYT4RJZ6f1hODZflxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه مرد روستایی در چین با استفاده از تکه‌های ضایعات فولادی و فقط با کار دست، یه بازوی مکانیکی غول‌پیکر ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/70009" target="_blank">📅 22:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70008">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⏺
🇺🇸
پیت هگست، وزیر جنگ آمریکا، گزارش‌ها درباره وخامت شرایط و بروز بحران سلامت روان در ناو هواپیمابر USS Abraham Lincoln را رد کرد و گفت وضعیت موجود «کاملاً نادرست بازنمایی شده است.»
او تأکید کرد که در این ناو، «هر چیزی را که در توان داریم در اختیار خدمه قرار داده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/70008" target="_blank">📅 21:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70007">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
کانال13 عبری:
برد کوپر، فرمانده سنتکام، به مقامات اسرائیلی گفته است که برای انجام حملات مجدد در داخل ایران تلاش می‌کند و معتقد است که ازسرگیری جنگ می‌تواند موضع تهران را در مذاکرات تغییر دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70007" target="_blank">📅 21:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70003">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7qtNuN1XxPxIgpjGKtit_nD2ltwLhnG-0xL-NKDhv_IKM9ZX40nC0c6LBcF4VJXfyNzo4CRRxQ6s103ZvHWfn8T4Em8_G2JTWWmfdPVqRER5NqOEc6ZPpAJw-EMvrl8lWzR3mr4BLoeOMAKGWmnc1KhURdvnE_JFaTe5CgI4c0n74Wm8l4K4jVGfchLOrKfLPqAMbLDRDqktoZT1LBiFK2ZXSSHZOUKa9vKAjeC1otRDT_uRuo1S0aIBto0E7-_AejGnt0iX5NPrnxaoLQJ7L1FuQABfukaoWtI3czOxcwJctMbCGT4Lhp6b3c4a3HkF8XYnTlNC5B_v8kEblKzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1c5b26c54.mp4?token=UpfcJSxWtMvJdg7K9HsUySPfoSJBEpHTZt6cAOCg-zCY7fL-FNVSh8hIR4IoIr3NR_tvresomAGyt9506ws0PXioxidoM_Z2OVQidjuHr_itXB4RN9try-djtc4JEXN5qEjzcm3_jKL2EvYGtRUAaMKIquAWujFW5YPAiPWU8x2b7lwR4qgPonuczpnVoURwyFqiUxJx5vSuAuVxTh8vJ85nf47Ap9nmiza6lRwCyPq0fx0CwRWxMH01O0sEEVb4IlicpcqNrq1p8Nyqb-Pn4dCtYtjo0qZHp2dayhG8-bbkc1LRfd1s6rzziz0qBSc63kict-HeuIKmeNDWYwqAvoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1c5b26c54.mp4?token=UpfcJSxWtMvJdg7K9HsUySPfoSJBEpHTZt6cAOCg-zCY7fL-FNVSh8hIR4IoIr3NR_tvresomAGyt9506ws0PXioxidoM_Z2OVQidjuHr_itXB4RN9try-djtc4JEXN5qEjzcm3_jKL2EvYGtRUAaMKIquAWujFW5YPAiPWU8x2b7lwR4qgPonuczpnVoURwyFqiUxJx5vSuAuVxTh8vJ85nf47Ap9nmiza6lRwCyPq0fx0CwRWxMH01O0sEEVb4IlicpcqNrq1p8Nyqb-Pn4dCtYtjo0qZHp2dayhG8-bbkc1LRfd1s6rzziz0qBSc63kict-HeuIKmeNDWYwqAvoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
این شما و این قوی‌ترین دختربچه جهان؛
🗣️
لوسی میلگریم دختر 9 ساله‌ای که تو نگاه اول خیلی ناز و گوگولی به نظر میاد، موفق شده رکوردهای زیر رو بزنه:
- لیفت : وزنه‌ی 81.6 کیلوگرمی
- اسکوات : 67.5 کیلوگرم
-‌ پرس سینه : 33.5 کیلوگرم
لوسی پاورلیفتینگ، کشتی، جوجیتسو و MMA کار میکنه و تو کشتی هم جدیدا داره پسرها رو زیر و رو می‌کنه...
نکته جالب اینجاست که این بچه فقط 27 کیلوئه و کلا 127 سانته، یعنی چیزی حدود 3 برابر وزنش رو لیفت می‌کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70003" target="_blank">📅 21:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70002">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_cEJxL_bMYVKaIIbWLp6n1Rh2x3U3S36RlvvUVXsMeBEI1DK37x93HlWYu3fnzBnIWBlM9yyk0U7chIXYlOlHBxLF6EGlOJ7AfbwPuGo92NzxD178IGGVEA4_VftHLWK3mor6tlJ7XBvyQZsw9VWzpslDdU82UTbX4Ovx1RUYQ3wPDfBnhK7iO7PmHnVb9QnkqjAS_kanaBFTV7TfYeVYtAwIjUVJtOFFRnim2g0LBIoGC77xCh5BI-A9Iw1bi-U-OWGlKsXXfQYGZgkpGXBphZIQw5krDT-Ddy3dhSG3S1Pfmh_dOOZwR_pOeuPPBV3x6QuN1cSMm8odfmDyKqbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
فرماندهی مرکزی ایالات متحده از برنامه‌های خود برای ایجاد نیروی ضربت فالکون استرایک، اولین نیروی پهپادی تهاجمی چندملیتی و چند دامنه‌ای خود خبر داده است که پرسنل آمریکایی و منطقه‌ای را برای بهره‌برداری از سیستم‌های تهاجمی یک‌طرفه در هوا، سطح و زیر آب گرد هم می‌آورد.
این نیروی ضربت به رهبری فرماندهی مرکزی عملیات ویژه ایالات متحده، بر اساس نیروی ضربت اسکورپیون استرایک، که پهپادهای آن قبلاً در عملیات علیه ایران استفاده شده‌اند، بنا خواهد شد.
سنتکام اکنون رسماً از شرکای منطقه‌ای دعوت می‌کند تا با هدف ایجاد یک قابلیت پهپادی تهاجمی یکپارچه در سراسر خاورمیانه، به فالکون استرایک بپیوندند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70002" target="_blank">📅 20:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70001">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e87ab5b1d.mp4?token=ESw-GoFk_MWD4hAWEraJeCbrZdfyuO6H_XsbMN0psoA4vcmP4_MMKbMo8f3RTBXvWKROrEGHWRROBIMdVdAjmEksHmjTG7wDOOr-2NEYOp8SmA3ySLyMk-qF4jxxNBh043THWQ5yewf-R1EdR_TYW8ENsQmkIwrXzG2RgvBX6NkIEpxLX1g4AM9mobEMVEJkuZTosRN7eb86ci_nBRc4zEAz4TyvY6Kcuh2_lcKi2a_odKQMP9n12n05iEz5cFqtbP3PnuRDXPPiA0p0HNp2V_s_fFFsJ_10zciJEIZ71nRtX5PJS3HmZbq-s-ZvXw3GL2UOw0c-MsaVcKcTquQhvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e87ab5b1d.mp4?token=ESw-GoFk_MWD4hAWEraJeCbrZdfyuO6H_XsbMN0psoA4vcmP4_MMKbMo8f3RTBXvWKROrEGHWRROBIMdVdAjmEksHmjTG7wDOOr-2NEYOp8SmA3ySLyMk-qF4jxxNBh043THWQ5yewf-R1EdR_TYW8ENsQmkIwrXzG2RgvBX6NkIEpxLX1g4AM9mobEMVEJkuZTosRN7eb86ci_nBRc4zEAz4TyvY6Kcuh2_lcKi2a_odKQMP9n12n05iEz5cFqtbP3PnuRDXPPiA0p0HNp2V_s_fFFsJ_10zciJEIZ71nRtX5PJS3HmZbq-s-ZvXw3GL2UOw0c-MsaVcKcTquQhvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
چرا ایلان ماسک ثروت تریلیون دلاری اش را نمی بخشد؟
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70001" target="_blank">📅 19:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70000">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59a534ae94.mp4?token=PvPBz8ol60_nXIElsMbjjCJfEsy4IeAV6fB76nCzVPOnJUUtKx4Sn7eKqNMfoEJxrP0DrTFajdMbbe0eNdMAR7H3zABstv5ggU42cUxmqDLtUnmPP5gXgFQVGBu_2NrlDWBkYZpEkhNzWQ3AkYoUxgSS7d_4eRKQs-fGKbyFZrYEJgRlv0_-BfEJ6wT6VKSslyM1_I0f2vMyBMTpVczYM7llOTUOkZooZumPdSWGb9Ul3TVotlthZImw09ZvErn7WJETIfLmjGED6Ttt81biN1kC1Yho2uB0Xa1rJ-zfR13HHyIooqXKigTvuESrDkjtIJQrbVApr4GhBqQwtRQ8jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59a534ae94.mp4?token=PvPBz8ol60_nXIElsMbjjCJfEsy4IeAV6fB76nCzVPOnJUUtKx4Sn7eKqNMfoEJxrP0DrTFajdMbbe0eNdMAR7H3zABstv5ggU42cUxmqDLtUnmPP5gXgFQVGBu_2NrlDWBkYZpEkhNzWQ3AkYoUxgSS7d_4eRKQs-fGKbyFZrYEJgRlv0_-BfEJ6wT6VKSslyM1_I0f2vMyBMTpVczYM7llOTUOkZooZumPdSWGb9Ul3TVotlthZImw09ZvErn7WJETIfLmjGED6Ttt81biN1kC1Yho2uB0Xa1rJ-zfR13HHyIooqXKigTvuESrDkjtIJQrbVApr4GhBqQwtRQ8jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش جانشین فرمانده انتظامی به قتل حمیدرضا رجب‌زاده:یک اتفاق فردی بود مثل بقیه مواردی که در سطح کشور رخ میدهد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70000" target="_blank">📅 19:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69999">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:ایران به کشور های منطقه اعلام کرد در صورت مداخله سوریه در پرونده لبنان، به سوریه حمله گسترده‌ای خواهد کرد.
خب ما بهشون هشدار میدیم که هیچگونه دخالتی در پرونده لبنان نکنن.
اگه گوش نکردن 100هدف در سوریه رو ویران خواهیم کرد.
این اهداف استراتژیک خواهند بود از جمله کاخ ریاست جمهوری سوریه که میتونه هدف قرار بگیره.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69999" target="_blank">📅 19:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69998">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/69998" target="_blank">📅 19:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69997">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkG2da5xKHyZKeI25eJe4g91qx_NcK9ainNoTocVPH9SBW4QWlVgqNptSH16HJ8d0jroC4XT3i2twpGRSHAeXXUU27cOMo-rhob1D3P-jXnHPFsvuuHfUmgvALNSZZ-UZkQkwZ50ASynCB71Y1I0orC9W58xvJdnFDINOUK-UfkjT4Gufn0jjwbnPf-de4KvQVLhj-V_oJT-yQZcgF5R3wi_iFDrfIbopoAoP6Lz4VP4xc6A4knwY7xvm5IbNm1t3jvX13wsGI9LRXb1mKy3C5s-6VCMcI9O4NaHQHovjaNLQKDCi3a0vDZtMhoV0kjkjaqgsfVng5v4bRwbSZ2R-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g22
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/69997" target="_blank">📅 19:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69993">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd8b0a970.mp4?token=ZDaK4ZOKFPpuyfivpgutrb-PMNWMXBWeiP3L4Mfctd9oSDwYPCRToau6xD3AlYEh2fTbegy_5dFXOEOhpE4fO846vQ-C37IKAtkkc6zwNQZ7UdczVwFfCzJfeIdt0TdtI02ZqpAvp9L87IV98iZR1bMfVLbfDH2LjOJ_lmB7HJOlc21QceXKd77uaUu5lAlriMSxUw3ZEp8wIz0Md2YkX9B7AvLsqvcx5_FPXanPEqQz5xFxqHMgT3FDzQ5nxWOj5l76ylgr5DiNZFTe66CixVHCs77fv6hIBzkQxCHkrZGvvdNv-BK0TsHEatcoa1ypATNyLklcS3XiVI-7r26EfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd8b0a970.mp4?token=ZDaK4ZOKFPpuyfivpgutrb-PMNWMXBWeiP3L4Mfctd9oSDwYPCRToau6xD3AlYEh2fTbegy_5dFXOEOhpE4fO846vQ-C37IKAtkkc6zwNQZ7UdczVwFfCzJfeIdt0TdtI02ZqpAvp9L87IV98iZR1bMfVLbfDH2LjOJ_lmB7HJOlc21QceXKd77uaUu5lAlriMSxUw3ZEp8wIz0Md2YkX9B7AvLsqvcx5_FPXanPEqQz5xFxqHMgT3FDzQ5nxWOj5l76ylgr5DiNZFTe66CixVHCs77fv6hIBzkQxCHkrZGvvdNv-BK0TsHEatcoa1ypATNyLklcS3XiVI-7r26EfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طغیان آتشفشان در جزیره سیسیل: بسته شدن دوباره فرودگاه کاتانیا به دلیل خاکسترپراکنی آتشفشان اتنا
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/69993" target="_blank">📅 18:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69992">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‼️
تو برنامه عشق ابدی ورژن صربستان یه پسر بعد از اینکه توسط ی دختر رد شد سعی کرد دختره رو خفه کنه و بکشه که در نهایت نیروهای امنیتی دستگیرش کردن،بعد از وایرال شدن این حرکتش الان مردم سراسر جهان خواستار این هستن که برنامه ی عشق ابدی بصورت کامل جمع بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69992" target="_blank">📅 17:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69991">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766cf940aa.mp4?token=ehNHtC1BjmPS47JkS0lCLZxV_O4VcPBtAs7t_72ua40vNaXV5GWp61QEKSz3nDShb3aiFT9HCrDHzNzQIAYWK6PzCdk_Hw4ScKqdo71hqqTfwVmUu4VsZSV6hhFVF__iM4bUGKctKX3Ay-4qhN88U6M93zuqrlgeAhSnPx6oeIqFAhbOAvtw5CLfee4oK8orUgheTkODCFdH3MVSyh9oKl2d63rMSOA_sbOCq9D4MSdgz6t_XVNOQqLaO6jpllWwz2j1rL0DctiNrzu0xrTKaQjugL60ooauNBDDMDpuruYFNPoSBcfh0igKZr90BLzofDZxJ9PTFoqThU2BovM77Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766cf940aa.mp4?token=ehNHtC1BjmPS47JkS0lCLZxV_O4VcPBtAs7t_72ua40vNaXV5GWp61QEKSz3nDShb3aiFT9HCrDHzNzQIAYWK6PzCdk_Hw4ScKqdo71hqqTfwVmUu4VsZSV6hhFVF__iM4bUGKctKX3Ay-4qhN88U6M93zuqrlgeAhSnPx6oeIqFAhbOAvtw5CLfee4oK8orUgheTkODCFdH3MVSyh9oKl2d63rMSOA_sbOCq9D4MSdgz6t_XVNOQqLaO6jpllWwz2j1rL0DctiNrzu0xrTKaQjugL60ooauNBDDMDpuruYFNPoSBcfh0igKZr90BLzofDZxJ9PTFoqThU2BovM77Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
تهران نوروز 1356:
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69991" target="_blank">📅 17:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69990">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f015c6551e.mp4?token=u2T4Obxv79ZxSbcq8dQ56ZQrQJTX4bgCcNH6Mf8cr8RHEy-DOXMk1VCzsPM2Vpk_bp2q_X_DLxYK_l0mKl6wf8Xl3fZdYQVvWnR2AbkW0BcNHC1McMz_NaJVbVM0sl3ud-IC0cB_ie1FvapP2P_WDs5WgQXWwzTXjilrP3sr3JrIkCtpoCGtgJCg1iN5hduI20Is0_zyH2ywJHgOtfXFBrJTB7Du8m00_V09RqaOLeXdj9g31XVFffzoAkGb4hdw53cwx2P3TP3DvS47zZWUTCIPd4-ccgo5GNmLV3T9Run77Jt5DveLJTQKThkMM_qc6clnbFlEROS37hYQlROqyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f015c6551e.mp4?token=u2T4Obxv79ZxSbcq8dQ56ZQrQJTX4bgCcNH6Mf8cr8RHEy-DOXMk1VCzsPM2Vpk_bp2q_X_DLxYK_l0mKl6wf8Xl3fZdYQVvWnR2AbkW0BcNHC1McMz_NaJVbVM0sl3ud-IC0cB_ie1FvapP2P_WDs5WgQXWwzTXjilrP3sr3JrIkCtpoCGtgJCg1iN5hduI20Is0_zyH2ywJHgOtfXFBrJTB7Du8m00_V09RqaOLeXdj9g31XVFffzoAkGb4hdw53cwx2P3TP3DvS47zZWUTCIPd4-ccgo5GNmLV3T9Run77Jt5DveLJTQKThkMM_qc6clnbFlEROS37hYQlROqyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سامانه پدافند هوایی خودکششی بسیار کوتاه‌برد گیبکا-اس، که بر اساس یک خودروی زرهی اصلاح‌شده تیگر ۴×۴ ساخته شده است، در حال انجام تمرینات آتش واقعی دیده شد و پهپادها به عنوان اهداف اصلی در آن خدمت می‌کردند.
این سامانه از لانچرهای سقفی استفاده می‌کند که قادر به شلیک موشک‌های دوش‌پرتاب ایگلا-اس یا ۹K333 وربا هستند و از موشک‌های زمین به هوای ۹M336، ۹M342 یا ۹M39 استفاده می‌کنند. این خودرو می‌تواند چهار موشک اضافی را در داخل خود حمل کند. لانچر آن دارای قابلیت چرخش ۳۶۰ درجه و برد ارتفاعی از ۵- تا ۸۰+ درجه است.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69990" target="_blank">📅 17:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69989">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">📌
فقط ۲۴ ساعت عضویت رایگان باز شده از همین امشب چک کن ببین چجوری میشه پول دراورد
💵
💸
🛒
این فرصت محدود رو از دست ندید
https://t.me/+MT03hkV78q9kMTc0</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/69989" target="_blank">📅 17:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69988">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0106cebdea.mp4?token=Wq5U8hsquDI-u7VdiLCP1eTI0H2FfQ5-YgpJO4ggxhQezmblp_f_V0Z9Wwf3LbNugDqqWJVx7EMY5ERYoCxv3CtiQ__MyjoMFFBYzRvbYfF514VxIr2k3k99dAydamdC90BkP4HW6IPq395aCEzze9B2oCRoxdepjDKc9XLQPuS2Mmn8lPA00YMIgvX_pbGEB5erAoTS7fUgQ5E-QQjIx9E-oPFs5-i0adHfrhyvfrClOwLUMIVO4S05_MA0g3PHwuWlEAqOZDrZ8aOGG0c789BGSEEk-EPKGCmIb022T6hFpxjDTi86sKQg0iuh1gWyz_eYWQj7k1moCLH3_V5ZWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0106cebdea.mp4?token=Wq5U8hsquDI-u7VdiLCP1eTI0H2FfQ5-YgpJO4ggxhQezmblp_f_V0Z9Wwf3LbNugDqqWJVx7EMY5ERYoCxv3CtiQ__MyjoMFFBYzRvbYfF514VxIr2k3k99dAydamdC90BkP4HW6IPq395aCEzze9B2oCRoxdepjDKc9XLQPuS2Mmn8lPA00YMIgvX_pbGEB5erAoTS7fUgQ5E-QQjIx9E-oPFs5-i0adHfrhyvfrClOwLUMIVO4S05_MA0g3PHwuWlEAqOZDrZ8aOGG0c789BGSEEk-EPKGCmIb022T6hFpxjDTi86sKQg0iuh1gWyz_eYWQj7k1moCLH3_V5ZWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💯
تنها کانالی که حتما باید توش عضو باشی
✅
چون راه پول
درآوردن رو بهت نشون میده
📝
حتما آمار کانالشو ببینید فعلا به مدت محدود عضویت رایگان باز شده فقط تا پایان فردا شب
🚫
⚠️
نمونه آموزش بازی Apple of Furtuneکه سودش تضمینیه رو براتون گذاشتیم پیش بینی های معتبر فوتبالی هم دارن
z22
:
📶
https://t.me/+MT03hkV78q9kMTc0
📶
https://t.me/+MT03hkV78q9kMTc0</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/69988" target="_blank">📅 17:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69985">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EcmagH-lRxxRIzXaBUeFnmvYSVcJXHxQpTYYqYqD8h8dLz_VhAFKP1rK4TTk5bwuSUSZ9zTUFCDNfOiJVRj2tUp29vM3gDK6TWAtUOOFFsa99zlJfAjBva7X5Pu1bW8Z3u8uF9GPbSpu5lHY4hzQiFiiU0zO5du0npCdaFcj6Sj656iQLO0QAaNaohkAoPFsXmA08IUvlQ8AgE2E0Lv_XUeY0B43-nWWmuMORKmxVrKEKi_kUuRDjk6gNPttWPXiWgRMVS7eEtOZKiOtBrvUkTQ1ik9qqnMnHgz0_lTBG9cdtY4fNESWxe-Tfl1EJSrN5ABM9VicRXAIKvvce-r67w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKVc7WUlW5pNAtLXCWu6dRBFCDqZaRPEziUd4HyTs4a6fRALj2V5gcmaiMbXdEBq5MkQyKG-iiTTub3D7nK6D0_N_ofOUVNBsythzfH_XrFCvUvlddMQnscWIOCrH-LEkINUC7QlFGd6xca-IxB1OnXf_49HGKyZvEYheQkCjbvpLIu4VEcJCEqi4Cf3tFgcO6ISlIwKiSvEr_qZtuTgkBncXsyWXh9jXCty-Zm6Jx7Bdruk3neSu4m5AY7C9_iqyWFpxWeevp9aaPL20In_-NNhTJagyyHSbaPZUM8JXcpLwJ8kPNpaHpAY-Qq33uQbh_s5dk-liB6z_CE20JEeeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qWUg_NKvR8EiV9oDsAnTtPLJB5Wq6O_o6EZYYrz9TomxDZJFCAXqNcYx9xgsjhcsAITga4hnEDy6H4uBfLx4xW7IyhNLzzGE7UlmNjFrefNWAUHSxg5KG73484abzXGLFLB4d1pcLXSHYcQjzRedKWNptCwbdiLpBZkYFQ9PONumNUmelzOy3nSHKdVTr2AwAtkNOswb0EWxihvKtfRLtcxqs42kKe-odLXj4zTtSTsgjybo0h9ahmGlfOae0Kt6dNbobbAnE5gWtfsmLg1Y6qrE6TGm3qUgkR7skE69-7vp0_wcLNJJZQiUfBbwBkhHccsAWMA6hwDZtZgJ2brDYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
❌
#فوری
؛ناوهای جنگی یو اس اس جورج واشنگتن (CVN-73)، یو اس اس شوپ (DDG-86) و یو اس اس رابرت اسمالز (CG-62) از تنگه سنگاپور عبور کرده و در حال حرکت به سمت خاورمیانه هستند.
ناو جنگی واشنگتن، ناو اصلی گروه ضربت ۵ نیروی دریایی ایالات متحده است که به طور دائم در منطقه هند و اقیانوس آرام مستقر است.
عبور از سنگاپور به سمت غرب، این گروه را به اقیانوس هند می‌رساند و مسیری بالقوه به سمت خاورمیانه را بدون نیاز به عبور از شرق تنگه مالاکا در جهت مخالف فراهم می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69985" target="_blank">📅 16:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69984">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961a7bc8c4.mp4?token=lyenlJF_hcD7GOT6hzaRDtCahuMniEISSWl1sWZG9Lqh1szjAz2Tzl_OQ3rk4ALiECnRW5nV3bT0s8MdS4GmPC49PJ-l4CSdbmMlwj8ujDlk_nIBd-TfvTRUQ_OvJujaMewX5m6AgOg2NQieT4mbdeiLDGWWBbEtr4hveGj7LUgI7gd7daNW7JYhPsw5a1C1Pa8dtIa3AjRUnzDt8wgrJSs9TxhjeN5koZGhQfFRPzuUfGv-Efyxpe_N4OIqmnWtu91I9zDSknJvkrdwYYXorsY64QsJBi_BUBi4jWuc4ICfHCw-Oa5ZUqm22_SNnZ6vm24NcSD0KJSCNTR66mQGDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961a7bc8c4.mp4?token=lyenlJF_hcD7GOT6hzaRDtCahuMniEISSWl1sWZG9Lqh1szjAz2Tzl_OQ3rk4ALiECnRW5nV3bT0s8MdS4GmPC49PJ-l4CSdbmMlwj8ujDlk_nIBd-TfvTRUQ_OvJujaMewX5m6AgOg2NQieT4mbdeiLDGWWBbEtr4hveGj7LUgI7gd7daNW7JYhPsw5a1C1Pa8dtIa3AjRUnzDt8wgrJSs9TxhjeN5koZGhQfFRPzuUfGv-Efyxpe_N4OIqmnWtu91I9zDSknJvkrdwYYXorsY64QsJBi_BUBi4jWuc4ICfHCw-Oa5ZUqm22_SNnZ6vm24NcSD0KJSCNTR66mQGDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک بالگرد آپاچی ۶۴ در تگزاس آمریکا سقوط کرد و خلبانان کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69984" target="_blank">📅 15:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69983">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b49c38bef.mp4?token=k93NLyokREnYbbFyvUPUMT8nAD7wdSOrqqU37034RC6y0YkA8752yMvDxIzDy9Z5Upyq3vIb6NNkvRzw0k9B2E44HhyafnNu4jyKKPr2wTgtt9YfrzWCUKQQVRL3CBCowqhx5v9XDjG3bTK-XmujQuo9OAbkpIXvSaGZPybRceoOHKptosT2cRLNKkD7rQxN1EXvNFQ4QC9ayFD28mcHpQWZG5D4B8JE2fqX6KpRgBzVY0MLEuAwCqBnFm0sacd8RAAMlaHzKWz1awJSU0ONnIYWOMBped96jeA5KdikAD3qapK94HwcJsn0ASuV_LzeWo70qKQrJY2c5PZU54a-fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b49c38bef.mp4?token=k93NLyokREnYbbFyvUPUMT8nAD7wdSOrqqU37034RC6y0YkA8752yMvDxIzDy9Z5Upyq3vIb6NNkvRzw0k9B2E44HhyafnNu4jyKKPr2wTgtt9YfrzWCUKQQVRL3CBCowqhx5v9XDjG3bTK-XmujQuo9OAbkpIXvSaGZPybRceoOHKptosT2cRLNKkD7rQxN1EXvNFQ4QC9ayFD28mcHpQWZG5D4B8JE2fqX6KpRgBzVY0MLEuAwCqBnFm0sacd8RAAMlaHzKWz1awJSU0ONnIYWOMBped96jeA5KdikAD3qapK94HwcJsn0ASuV_LzeWo70qKQrJY2c5PZU54a-fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تاکتیکی که قراره برای بنزین اجرا بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69983" target="_blank">📅 15:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69982">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62cea94911.mp4?token=v7wWXJFkCf735lNmQqIlUirBpQITuTvmxmb0HSvMuYtDMwhwGPyG0I-nMsZqrom2ykSsSZAgdfAd6Kd142VS-CwSm72C50T7aqqhmH_bBPc4ujcsHnTa6Co_V_43fOXPVr7AILNAWH-nM_OzQXVCSIXyDHYfpH4uRbR80pXY3_DVANpAai5GMJyNX7iBhfUYLC27LVSzHq7rWY__NousbLcQmwfEVNECzbmF_E2LJaIW4vBkczi_s9sXIIGO3LWAVX4b3Bpl0_gaTOby-e5aMKCHqKxOIqbsq9bzxfsgzf29MX-C1iJUItWSytgSZVFylLCsf5EirdhXAyU-6c8DRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62cea94911.mp4?token=v7wWXJFkCf735lNmQqIlUirBpQITuTvmxmb0HSvMuYtDMwhwGPyG0I-nMsZqrom2ykSsSZAgdfAd6Kd142VS-CwSm72C50T7aqqhmH_bBPc4ujcsHnTa6Co_V_43fOXPVr7AILNAWH-nM_OzQXVCSIXyDHYfpH4uRbR80pXY3_DVANpAai5GMJyNX7iBhfUYLC27LVSzHq7rWY__NousbLcQmwfEVNECzbmF_E2LJaIW4vBkczi_s9sXIIGO3LWAVX4b3Bpl0_gaTOby-e5aMKCHqKxOIqbsq9bzxfsgzf29MX-C1iJUItWSytgSZVFylLCsf5EirdhXAyU-6c8DRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره بریتانیا:شاید بتوان بریتانیا را «جمهوری اسلامی بریتانیا» نامید.
کسی گفته بود که نخستین جمهوری اسلامیِ دارای سلاح هسته‌ای، جمهوری اسلامی بریتانیا خواهد بود.
ما اطمینان حاصل می‌کنیم که مورد دیگری وجود نداشته باشد؛ می‌دانید، در ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69982" target="_blank">📅 14:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69979">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g2XH_lCAApFhQXOZ-z3_3xipA7IYIKRSzal_7EmAh0LzYU5UDMwEqDKsg-QEPEB4ktFrlN19NvQ_NL203rDZbfdcNMpFN91AgiQKn50IVQZZZnuqrOF8spI4BoZAcWxWBBRM2QccNGu3kCKvMEKtC80OShu7K36x874Qs0Lg44RtOnF682L6ugVymyoPs1vgMdg8voJsw5h9J9koW9qGSbV4nTf8KaVoslgjL4F5PkSG0_vx4sj1-WEdXrTSxSAl6Bo7jfc6zE30FlX74BT73pK1JkydiqbpCMRSadFgTJjsuM4gEC-Mfzh_XgV11SnJx5RGfirqGiJuRwXnYTm5Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohuBpCvW2IfxdCgC-w9-AVJdCsBA5ijutWN8yFScQu_OI01FnI9wGeo9IqKLHsK7qOTPC0EGix1TGYXvt2d8U2HpUBiK6brsJH98WfiDXf0FP3JqyW2KLV8HvWm5ZY-W0Hy6JG4OdIMA8HS8IU-JMNE42jWQBSJBMJ5M1F0CzQJ4CnaWsqQKUrqWumJNXplD7EdlkYWH7qv90nHhFYonW_iWTVQ0ToKdwQxmDPsvgQ7pXT0YCd_HKr9C7v2YvCSs0HBGtpMvJSOseGXsoiGhlytvcxHSyM8D17hQ_6iWynxMIQTAk5fHDg7HElmx_JtPNrvPlBjBZcOOXVBi2LRTeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8342b1a3.mp4?token=FXZuK87lSP5UOHyfAPKcx9tBsDhEU9xmK5zrucIAAJV2vHvPQKh1hZXodh87Etk3UKZFBm5tNKnqa5pDrEwz-EXwGCh5JCFDtXSpQQm3v2UpiTpFjyAZm1AibXPi-hjPOhTu381MNXa1uFoGTitxLDQgzdLFGOON8OpYK9RG0qvxzNnrYzBZ3-5wzGMAYRti4cW-cMYSdXjIG3DkAztvC3pbwxKtG7ADRZ9NGDqrt24eSUuWU4vDbVD4c8rgZPvRnTrf8ZwZWE483L8A1MYi4_HkoUcx1f6EFWXMB8w3NXzfzyj8dOf75O-ERAsCqMCbIGXFOA9JmOE08uS7jNoEjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8342b1a3.mp4?token=FXZuK87lSP5UOHyfAPKcx9tBsDhEU9xmK5zrucIAAJV2vHvPQKh1hZXodh87Etk3UKZFBm5tNKnqa5pDrEwz-EXwGCh5JCFDtXSpQQm3v2UpiTpFjyAZm1AibXPi-hjPOhTu381MNXa1uFoGTitxLDQgzdLFGOON8OpYK9RG0qvxzNnrYzBZ3-5wzGMAYRti4cW-cMYSdXjIG3DkAztvC3pbwxKtG7ADRZ9NGDqrt24eSUuWU4vDbVD4c8rgZPvRnTrf8ZwZWE483L8A1MYi4_HkoUcx1f6EFWXMB8w3NXzfzyj8dOf75O-ERAsCqMCbIGXFOA9JmOE08uS7jNoEjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
صحنه‌ زیبای خورشید گرفتگی که امروز در اسپانیا و آلمان رخ داد و لحظات زیبایی رو رقم زد:
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69979" target="_blank">📅 14:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69978">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b397a0c033.mp4?token=DeYLib1Ai3VOkdJitqon0Tpwa3zYRaROIVAupsBT5-rVXfk8dwyScGH9psm5UgSQV5pgvP4E7VySDYkk_jyeMJ5xRa1_WB3mcA7G2oVZTKzz9-N9NYo_PdaIwnjXxKwI74yWPnWN0sVkGGx0NUnWPwkP_usGvHL3R6WlESugfUgJnjyK3H31Rq3ri_IYZlDK8tRlIjn4YpKF_OepvwdN2LboZDSe3LqtcafVinMsWMYpjyUxADVK8PSj_Sgog8mFWMUP2Qu-uFPPtqqqdcAlyrDwa4vW5IyV9a_txZs4qrm47wgV4O2sPYNzr0F63LMWhiMTy6cEYUYGk4OX53IQ_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b397a0c033.mp4?token=DeYLib1Ai3VOkdJitqon0Tpwa3zYRaROIVAupsBT5-rVXfk8dwyScGH9psm5UgSQV5pgvP4E7VySDYkk_jyeMJ5xRa1_WB3mcA7G2oVZTKzz9-N9NYo_PdaIwnjXxKwI74yWPnWN0sVkGGx0NUnWPwkP_usGvHL3R6WlESugfUgJnjyK3H31Rq3ri_IYZlDK8tRlIjn4YpKF_OepvwdN2LboZDSe3LqtcafVinMsWMYpjyUxADVK8PSj_Sgog8mFWMUP2Qu-uFPPtqqqdcAlyrDwa4vW5IyV9a_txZs4qrm47wgV4O2sPYNzr0F63LMWhiMTy6cEYUYGk4OX53IQ_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی اصفهان، چند تا مرد عرزشی، یه دختر تنها رو نیمه شب خفت میکنن گوشه دیوار، و اونو مورد آزار و اذیت قرار میدن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69978" target="_blank">📅 13:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69977">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo4kcRBf3Qs60g7rp_1Wx8oVop-L3e6x-AZLsxDaORlbNmAAZKO3BqxDGA10p_XCCI4QoIisti7scTv2NnMvRWRX54HB7IA6DmpJHgxLIyKZFo2cJ31OTexu9T-zIX7vWfY0y2uWwVGGjL64njN92NcXFxEp9YJgFTbQXgpotdvs7dbVkmCu6YZuh_gNTtoeN7AdfET1KQSunOe9tTHYt2ZMdFSgmA4TlABUNjdpc5rEzBBBOEjRct7lxiveZ9tjqLn4KprG9pePfy1HwhbNwYOqIWxREgi8264L6FaND9iSoLACblXRklt_PAUtQlHmIAu6XIu877ycmR-Wq50FqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
به گزارش نشریه "آتلانتیک"،
دونالد ترامپ، رئیس‌جمهور آمریکا، رویکرد خود را در قبال ایران تغییر داده و به سمت یک استراتژی "منتظر و مشاهده" حرکت می‌کند. او به طور فزاینده‌ای به تحریم‌های اقتصادی و محاصره دریایی توسط نیروی دریایی آمریکا متکی است تا تهران را تحت فشار قرار دهد و آن را به سمت مذاکره سوق دهد. این در حالی است که تهدیدات و حملات نظامی نتوانستند به پایان جنگ منجر شوند.
اسکات بَسِنت، وزیر خزانه‌داری، استدلال کرده است که تشدید تحریم‌ها می‌تواند در نهایت ایران را مجبور به سازش کند. در عین حال، کاهش ذخایر موشکی دفاعی آمریکا، گزینه‌های نظامی ترامپ را بیشتر محدود کرده است.
بَسِنت همچنین به ترامپ گفته است که تنگه هرمز ممکن است ظرف دو سال آینده اهمیت خود را تا حد زیادی از دست بدهد. او ادعا کرده است که تا 70 درصد از انرژی که در حال حاضر از این آبراه عبور می‌کند، می‌تواند در نهایت از طریق خطوط لوله زیرزمینی به مسیرهای دیگری هدایت شود.
در حال حاضر، دولت آمریکا بر این باور است که فشار اقتصادی مداوم می‌تواند به دستاوردهایی برسد که تاکنون اقدامات نظامی و دیپلماتیک نتوانسته‌اند به آن دست یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69977" target="_blank">📅 13:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69976">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e944d4e8ac.mp4?token=GUum3lt-hCK498YdJrR5linZb4VrE3qCaaImzHtHDECHRwbWizjgMeKUNTq_viWOT5Q6uFGwwZMS7y1tAUcic8YSEo-fM6uGsc0hDDeXE_9UQE5UnoGnM1W6hhznqO7znBqn7OWEuoXsetm9qpRCMBQuQTqvRzhyuZpJB5lmG7uG_kw3uWatoOLeuRubPrbTjbuPHTEjYnI-yeia9sX4_UyQoipsMXR9oZhfxfxR6O-3kWP8XBhKFjd7priet4pX0RHtJyn-OlWNnjIdiA0kAX4Ej9AnlkhZBrAOTKyCIKQi2Jm4wBppNidnMHXdK0Jn1a8W-bqOUba-FkWsWhacVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e944d4e8ac.mp4?token=GUum3lt-hCK498YdJrR5linZb4VrE3qCaaImzHtHDECHRwbWizjgMeKUNTq_viWOT5Q6uFGwwZMS7y1tAUcic8YSEo-fM6uGsc0hDDeXE_9UQE5UnoGnM1W6hhznqO7znBqn7OWEuoXsetm9qpRCMBQuQTqvRzhyuZpJB5lmG7uG_kw3uWatoOLeuRubPrbTjbuPHTEjYnI-yeia9sX4_UyQoipsMXR9oZhfxfxR6O-3kWP8XBhKFjd7priet4pX0RHtJyn-OlWNnjIdiA0kAX4Ej9AnlkhZBrAOTKyCIKQi2Jm4wBppNidnMHXdK0Jn1a8W-bqOUba-FkWsWhacVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در سال های اخیر با ۵۰ هزار تومن چقدر گوشت قرمز میشد خرید؟
سال 1390 ؛ 5 کیلوگرم
سال 1395 ؛ 1.26 کیلوگرم
سال 1400 ؛ 355 گرم
سال 1404 ؛ 64 گرم
سال 1405 ؛ 28 گرم
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69976" target="_blank">📅 12:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69975">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f12d9ffb23.mp4?token=KsW1DInHL8WAnSj8gCc5Pw6yjuUwKua2WbGxViEGfDD-Qbab5aGJMOGr5OfoyJn5K5ibZA9TlEeYGQwvm-RsSfJjDujTKVqL_Q4rmaQ9TjThk18lEtE0sNp6YlMncnH-IVpzhlcuYr83oA_gu2FSEx_eqvWgONqB8U0qsaHE1CbhCYBL3dTBgT4-eybfholBYMB5M9RgVmCi4lU-Tsu7X1YvGKPlsY_mHXXsa0nwT9cCtqa_vM0jaxHWs7_il7TwRIGsz9-xXC4wc_GFTqS3vd4OcXs6tQIyg-q7rjlgrJw3rcEzuAQrUu39_fRTuZNWRIwUiLyvB4vWNFnLJbvcQA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f12d9ffb23.mp4?token=KsW1DInHL8WAnSj8gCc5Pw6yjuUwKua2WbGxViEGfDD-Qbab5aGJMOGr5OfoyJn5K5ibZA9TlEeYGQwvm-RsSfJjDujTKVqL_Q4rmaQ9TjThk18lEtE0sNp6YlMncnH-IVpzhlcuYr83oA_gu2FSEx_eqvWgONqB8U0qsaHE1CbhCYBL3dTBgT4-eybfholBYMB5M9RgVmCi4lU-Tsu7X1YvGKPlsY_mHXXsa0nwT9cCtqa_vM0jaxHWs7_il7TwRIGsz9-xXC4wc_GFTqS3vd4OcXs6tQIyg-q7rjlgrJw3rcEzuAQrUu39_fRTuZNWRIwUiLyvB4vWNFnLJbvcQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لعیا زنگنه، بازیگر:
سال ۱۳۷۴ که سریالِ «در پناه تو» در حال ساخت بود، آخوندا و مسئولین میگفتن که دخترا با زیبایی پارسا پیروزفر به فساد کشیده میشن و کارای بد میکنن!
برای همین دستور دادن با گریم زشت ترش کنن و آخرشم ۹۰ درصد سکانس ها رو حذف کردن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69975" target="_blank">📅 12:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69974">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNcWq1hROnGpAF9ez7FfW8qUp1WJjVE-Etipqg0EYSX9Dlc32AEC75kUIL4MdZyzGjya_n1YO_VVptoPvOIhhzglvNNGwfhs4rngVUdCpq2AIlQo6gwXWug7mkCUfezJa6pycveJ07Pr5DHjPBGdarrZ0sU1N5JPGKR3NNY3gYGu1Z_PvZGHmLQw9uoShRPkndh6zqm29w_KnB_Iz_sy6uAMw35ltfr2zv-PbLHgIEj3OINNFSvOQsWsov6aXlwmnl5JkQuu8kfWRG1GmbfhHwcP6w-hFUb7OtavEEWd6wmrrE4t_qaEf72nHi9GFH3-U-7Qw8CNk_YjyFlC_4IkCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
ایالات متحده مدت‌هاست که به دلیل ناکامی‌های اطلاعاتی، محاسبات نادرستی انجام داده است.
مثالی واضح: جنگ علیه ایران. حالا، یک محاسبه نادرست حتی بزرگ‌تر در مورد تنگه هرمز.
بدتر از اخبار جعلی، اطلاعات جعلی است. مراقب باش.
الله بزرگ است، بزرگ‌تر از هر قدرتی روی زمین. ما به الله اعتماد داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/69974" target="_blank">📅 11:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69973">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/69973" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/69973" target="_blank">📅 11:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69972">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1IKHhLpFzB1JHO8qE-909b5SYVF5AvXvXH2ryqOlCl7JUxLq9CQvcr4cVwhu54TRvGP2FS8TTFnBPoGVWanOH_Z_DIkR3XEMEwFUbfrdLjQV-9AAOF0zHmJE4zDuHi8kRMx1ZPhP6l30H8m1tEm8HfbpA4jMKVEp62OG-XHJl69z84R_8gVEfVO_1BtEOB5q3Lox97V7toMJngitPakVJQ5z9ZEIiyHfKNgwf3wtbOkeWmcKWRFb1Nnix0nrc8nFMwDvBi_KryisRn-2GbhA95s1fWNqfXqgxNP9QQ9puXHjwxTUfePOBtF0BGaYBR7Sla4uC1gqgtYtSb0sIw2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r22
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69972" target="_blank">📅 11:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69971">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77c4997c0d.mp4?token=QG9oCgz_7ES11IwRfq-8AcHzKGENjY0OyRjJUJtLxKGWTMbSKHYVq11rbj9GoHBIvE89E9k-BlYFwVzTTL9W8EjSkIKN4FW6JvydBMSr4W6YBz-AkSBqmBfTWtApQ07Hhz5hFKoCGPwNvfcELe-WNalQn6cHj2D9uGA4R_dWMVek4enaELqcE-fqrC9UQEyo30zzjpOiIhB7rl1ZqHxNbuN73NcjeOR7kR0I4d-1Ptg2Vv8oy8J7Wi-mXmx7o_544xBEhXriVkzol_UMlV0UWdVBguN2Z4xYx7IEbdtsR67YkPu_qYxCcC8iDev8ccsQI1k-LwgvSMv8wIWWZ3t5GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77c4997c0d.mp4?token=QG9oCgz_7ES11IwRfq-8AcHzKGENjY0OyRjJUJtLxKGWTMbSKHYVq11rbj9GoHBIvE89E9k-BlYFwVzTTL9W8EjSkIKN4FW6JvydBMSr4W6YBz-AkSBqmBfTWtApQ07Hhz5hFKoCGPwNvfcELe-WNalQn6cHj2D9uGA4R_dWMVek4enaELqcE-fqrC9UQEyo30zzjpOiIhB7rl1ZqHxNbuN73NcjeOR7kR0I4d-1Ptg2Vv8oy8J7Wi-mXmx7o_544xBEhXriVkzol_UMlV0UWdVBguN2Z4xYx7IEbdtsR67YkPu_qYxCcC8iDev8ccsQI1k-LwgvSMv8wIWWZ3t5GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی کره شمالی اینترنت قطعه و مردم فکر میکنن رهبرشون خودش میره با قطار براشون غذا میاره و تیم ملی فوتبالشونم هر دوره قهرمان جام جهانی میشه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69971" target="_blank">📅 11:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69970">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJNeVXnA0Ssofz3XqDi4GTQZNHlcSvlF7wuuat9tmH_e0TCFIk2MIjru1YKmFhauQCcc3XJbfA7x7I1bJTJrD59gEDTK3yBWU45zYkbkWHwkjLN8NHI7YNOjQb2fINfQ2L-8yv4Kd-_zzMb7pStKu4cqwKcZXKJW7QofNYE4Xremq5ZxR4-U5rhciDul3kR0WEsr3ioaECp62N7QTjl_k_T7Ox1nkW3u6lcf-qpUtp8mkZE9rxuCfynDMw5vZuYIbqyM_68mhBljRaqxvhHHv-_uFbNeIibHQVonJpp00P3kfeqVzhwAbga_TBMdaCgg_T9FDVg33Iz3aYl-ll93wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نشریه گاردین: چندین ملوان حاضر در ناو جنگی "آبراهام لینکلن" تلاش کرده‌اند تا از عرشه به دریا بپرند، زیرا خدمه این ناو با فشارهای روانی فزاینده‌ای در طول این ماموریت طولانی که برای پشتیبانی از عملیات‌ها علیه ایران انجام می‌شود، مواجه هستند.
حدود ۵۰۰۰ ملوان و تفنگدار دریایی حاضر در این ناو، در ماه نهم حضور خود در دریا هستند و رکورد ۲۵۰ روز متوالی بدون توقف در خشکی را ثبت کرده‌اند. خانواده‌های این افراد نگرانی‌هایی را در مورد فرسودگی شدید، شرایط زندگی رو به وخامت و حمایت ناکافی در داخل این ناو ابراز کرده‌اند.
گزارش‌ها حاکی از وجود مشکلاتی مانند سرویس‌های بهداشتی کپک‌زده، توالت‌های خراب و امکانات شستشو، کمبود آب گرم و محصولات بهداشتی اولیه، و محدودیت در تنوع غذایی است.
چندین تلاش برای خودکشی در این ناو جنگی خنثی شده است. یکی از همسران گفت که شوهرش پس از تمدید مکرر ماموریت دریایی خود، تلاش کرده است تا از عرشه به دریا بپرد و افزود: "او می‌ترسد." او پس از اینکه شوهرش از عرشه به دریا پرید، با او تماس گرفت، اما از آن زمان تا کنون هیچ تماسی از طرف نیروی دریایی نداشته است.
در یکی از حوادث متعدد، یک ملوان که در حال نگهبانی بود، متوجه شد که یکی از همکارانش قصد دارد از عرشه به دریا بپرد و با مداخله، او را به عقب کشید. در حادثه دیگری، نگهبانان از پرش یک عضو خدمه از عرشه جلوگیری کردند.
این ناو جنگی در اصل در نوامبر ۲۰۲۵ برای انجام عملیات در اقیانوس آرام اعزام شد، اما پس از آغاز جنگ با ایران، مسیر آن به سمت خاورمیانه تغییر یافت و زمان بازگشت برنامه‌ریزی شده آن بارها به تعویق افتاده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69970" target="_blank">📅 11:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69969">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a118468ed9.mp4?token=ndCl6IIdu8BlcU07A_fqpR8lN0EOxBUSzG0bznwSsQTzy4c-bTfEjr7yWTxqZa4xD22e5C4UBbBMujhPUHiKurY1ydoEMs5ikPp31vGMKKortWvkEzhV84dfoDwIt3r1T6SmQ1C5Gj1Sp6GeZhHrO4Rx5PL-EpZz8c76CI6xP87wnWbeAzNnZf8kTlSzr6ML_6WnSm3uqQ-gk9PsF4cQM3zsB09Dl3UVZJWiw-cDNMdZfWByfsyvfcTUvjSk3Dym0f56YeVKn9jeG9WJ8RnMT7kEJHkr18ZlVX7Mcltnff-2OMpJLT-W3NZOIslnRfrMwDuWT8CzfM7teU7Wq0MEgA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a118468ed9.mp4?token=ndCl6IIdu8BlcU07A_fqpR8lN0EOxBUSzG0bznwSsQTzy4c-bTfEjr7yWTxqZa4xD22e5C4UBbBMujhPUHiKurY1ydoEMs5ikPp31vGMKKortWvkEzhV84dfoDwIt3r1T6SmQ1C5Gj1Sp6GeZhHrO4Rx5PL-EpZz8c76CI6xP87wnWbeAzNnZf8kTlSzr6ML_6WnSm3uqQ-gk9PsF4cQM3zsB09Dl3UVZJWiw-cDNMdZfWByfsyvfcTUvjSk3Dym0f56YeVKn9jeG9WJ8RnMT7kEJHkr18ZlVX7Mcltnff-2OMpJLT-W3NZOIslnRfrMwDuWT8CzfM7teU7Wq0MEgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستانی از زبان یه دانشجو-معلم در زمان پهلوی، که برای اینکه مخارج تحصیلش رو بده، شب‌ها مسافرکشی میکرده، تا اینکه به محمدرضا شاه برخورد میکنه و...
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69969" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69968">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4765f0c41.mp4?token=IU-KL0qoe2_-7fRmDHXSVQG89vVSqSmZJUDoeX5_Tv6v8CTfG9EJUsuz4aLdoPHPawPPfNc9RRgCOVvn6uqoX3PS-j_6q4MeFsnROzzGAFQoN4817d6lxd98680S69ie7bczhQFWRW9tz7kl47TEzngqHHiE0QdXU8-mQC5twSjy8bwdfOWCCStPLyMurg3ZD1XAoAxNgV24HMGVDyle-ade96MQuT-ro9Ojy5rkNg_x-h-d9Gxsw6IZxxB_Hof5tQggkCNi4n35pCdqlQsHZPXgZa0c9Y-A2N948g5ftQJGkbf5MNkCP34ze4VvwxLNl2rwjpwieTtJdQwo1q4u5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4765f0c41.mp4?token=IU-KL0qoe2_-7fRmDHXSVQG89vVSqSmZJUDoeX5_Tv6v8CTfG9EJUsuz4aLdoPHPawPPfNc9RRgCOVvn6uqoX3PS-j_6q4MeFsnROzzGAFQoN4817d6lxd98680S69ie7bczhQFWRW9tz7kl47TEzngqHHiE0QdXU8-mQC5twSjy8bwdfOWCCStPLyMurg3ZD1XAoAxNgV24HMGVDyle-ade96MQuT-ro9Ojy5rkNg_x-h-d9Gxsw6IZxxB_Hof5tQggkCNi4n35pCdqlQsHZPXgZa0c9Y-A2N948g5ftQJGkbf5MNkCP34ze4VvwxLNl2rwjpwieTtJdQwo1q4u5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زاکانی:
موشک دقیقا خورد تو خونه مجتبی خامنه‌ای. زنش که معلم بوده اون روز سردرد داشته نرفته مدرسه که اونم شهید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69968" target="_blank">📅 10:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69967">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcec26005.mp4?token=dLXA4XCQPFKob_d-SUGq72llxlkz6UvmqcaDCGLV5SAfY1zairf3vme_HH5VjhCu8EV_RQjaCHCTElbFSOW1m0pwxTmPOgD1H-Rdxey10_tMGujFrYsLVKpgznYFyL9axVkDS1SYKYUP_01mEe8caWWePKNsGFrPyBBu23fMMr5v1wT9oQjjSQiYaci3E1S-rUFK-k1GcWJ6U7fhAFEbN4l3QiJgUwc4tkkOdM19aTVx8JY7vpXga9fIk1Lei8fH-xmKIelPDBf7Mu8EBMBBIbpUCEBpBS0fdh2kNE7yMlzPbfzL_h1SQEFCLDxN8eJrXcDYT5RBySU8J5RkRH0MPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcec26005.mp4?token=dLXA4XCQPFKob_d-SUGq72llxlkz6UvmqcaDCGLV5SAfY1zairf3vme_HH5VjhCu8EV_RQjaCHCTElbFSOW1m0pwxTmPOgD1H-Rdxey10_tMGujFrYsLVKpgznYFyL9axVkDS1SYKYUP_01mEe8caWWePKNsGFrPyBBu23fMMr5v1wT9oQjjSQiYaci3E1S-rUFK-k1GcWJ6U7fhAFEbN4l3QiJgUwc4tkkOdM19aTVx8JY7vpXga9fIk1Lei8fH-xmKIelPDBf7Mu8EBMBBIbpUCEBpBS0fdh2kNE7yMlzPbfzL_h1SQEFCLDxN8eJrXcDYT5RBySU8J5RkRH0MPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاید فک کنید هوش مصنوعیه ولی نیست
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69967" target="_blank">📅 09:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69966">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f39fe0991d.mp4?token=DwBxCnhSIWFuYYMaRtl4vj6GMDuWjtJdf0uEttd-Kf4iYPJeyLDpDoz4Qepj-t2PFq-YrFxNUJ1FrRJ2lY2WBiPt4l4-EP6V0yscAYvXrRbV8uiqk_YshoZ-ROIMsY_9d8HJ2oKPc3g3hv-AogQNPXDVTUdfQZeAu0GhTj1TTSDaHeeJAlnK6KlRsmrx8dwfbW4LAdFWK387pPSngayWqAcEC9gKombgxNFFj16d7aOOMj5e4N1w6WIDKgEEkGjPujWARXYpTb-o1i0GhWDPFufA_OzWJs254VW6a-JSjWQCxYEkZg90BBiD6oC2RN7_5jMSb7ahfDFxhB-BK8m-3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f39fe0991d.mp4?token=DwBxCnhSIWFuYYMaRtl4vj6GMDuWjtJdf0uEttd-Kf4iYPJeyLDpDoz4Qepj-t2PFq-YrFxNUJ1FrRJ2lY2WBiPt4l4-EP6V0yscAYvXrRbV8uiqk_YshoZ-ROIMsY_9d8HJ2oKPc3g3hv-AogQNPXDVTUdfQZeAu0GhTj1TTSDaHeeJAlnK6KlRsmrx8dwfbW4LAdFWK387pPSngayWqAcEC9gKombgxNFFj16d7aOOMj5e4N1w6WIDKgEEkGjPujWARXYpTb-o1i0GhWDPFufA_OzWJs254VW6a-JSjWQCxYEkZg90BBiD6oC2RN7_5jMSb7ahfDFxhB-BK8m-3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های داخلی با انتشار این پست اعلام کردن که کامنت گذاشتن و لایک کردن پستای رضا پهلوی و اینترنشنال و... جرمه و کسایی که اینکارو بکنن دستگیر میشن.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69966" target="_blank">📅 09:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69965">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69965" target="_blank">📅 01:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69964">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=j0qSpNJCvmwL59HnNQJAQxTT47VNL8E756zv-POePEtgqMxRx953niX4QwP79N4HXGIYBbPBMzQyqJCSioSdLys-xWmEXszCudkJZ4XxPX0CrVucT-DH5L1TVIRh78cEalT7iITmHulYex-qfB1SWmD2baNKWIwTrITIbOJ-9xZZFaiTp0ICn4G_tJ-RCkqCsmeSf0jfc8qO2I3OZY2mBCxlBJhO-uu0xs6fc0471zcUSGFx932eDJuq4mKn0sDhAipWxfWTYnGPuvKSivfLIMSIYDJ7i488sVH9zYSMguumwVWUxdbXlayMherVwpU0byCRZc3veP8pgF7585jvGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=j0qSpNJCvmwL59HnNQJAQxTT47VNL8E756zv-POePEtgqMxRx953niX4QwP79N4HXGIYBbPBMzQyqJCSioSdLys-xWmEXszCudkJZ4XxPX0CrVucT-DH5L1TVIRh78cEalT7iITmHulYex-qfB1SWmD2baNKWIwTrITIbOJ-9xZZFaiTp0ICn4G_tJ-RCkqCsmeSf0jfc8qO2I3OZY2mBCxlBJhO-uu0xs6fc0471zcUSGFx932eDJuq4mKn0sDhAipWxfWTYnGPuvKSivfLIMSIYDJ7i488sVH9zYSMguumwVWUxdbXlayMherVwpU0byCRZc3veP8pgF7585jvGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a21
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69964" target="_blank">📅 01:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69963">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/056e9dab31.mp4?token=BPluoKfIpCccSbOrS2bRCBeYM34p-NkfyTrulQE96hxGwWD9RCJe4wos0npYMAFiRxoXIH8wWNZQ3_oPxc45gFdHS6uLYsRA7ysFacN7cNjfVAoaB-Lp0_mt91d3iPk9lrCfUWjkeFnfHIf6txRGb3KXnv-ye-En1uQXC6UvUfDSQxLY9IuNn32lpkTcPQ5Ain8JTLzOkuA-MBzSJnUHRFKETJD5_pmIqohscQBS9xQ2fpP-dInkhTy9u2ztpSycUMHPeLejgTiAL6d-Gcb07TmWQ5cUUYTL8jn6NmwmzpQx7Rurx-vbOx1bj-DxNGg-csY7mEIJ9LC5V1HTxEPRZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/056e9dab31.mp4?token=BPluoKfIpCccSbOrS2bRCBeYM34p-NkfyTrulQE96hxGwWD9RCJe4wos0npYMAFiRxoXIH8wWNZQ3_oPxc45gFdHS6uLYsRA7ysFacN7cNjfVAoaB-Lp0_mt91d3iPk9lrCfUWjkeFnfHIf6txRGb3KXnv-ye-En1uQXC6UvUfDSQxLY9IuNn32lpkTcPQ5Ain8JTLzOkuA-MBzSJnUHRFKETJD5_pmIqohscQBS9xQ2fpP-dInkhTy9u2ztpSycUMHPeLejgTiAL6d-Gcb07TmWQ5cUUYTL8jn6NmwmzpQx7Rurx-vbOx1bj-DxNGg-csY7mEIJ9LC5V1HTxEPRZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنر نصب شده در تهران:
پزشکیان راستشو بگو، مجتبی دیگه نیست و فقط وحیدی بهت دستور میده؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69963" target="_blank">📅 01:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69962">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
#فوری
؛خبرگزاری فارس:توقف اجرای طرح عرضۀ بنزین با نرخ پالایشگاهی در کرمان
مدیر شرکت پخش فراورده های نفتی کرمان: پیرو مذاکرات امشب استاندار کرمان با مقامات کشوری و نیاز به بررسی بیشتر طرح مدیریت مصرف سوخت و مقابله با قاچاق، عرضۀ بنزین با نرخ آزاد پالایشگاهی در استان کرمان متوقف شد.
تا اطلاع ثانوی، فرآیند عرضۀ بنزین در جایگاه‌های سوخت استان مطابق روال پیشین ادامه خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69962" target="_blank">📅 00:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69961">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184379545b.mp4?token=UUUo_Enb59_88OF5eEvXXZk-9W_SdI1ZMSCRk8zCdHkMSXl8s3D1O1BHt1qE95vJUXTHiNwiLRorZnDhsfu-CjPrW4FfRQLYsk_Y9FsfrJlw1iaZ-UwnTPMD5wwP_bhLz5T30_YO5dLdBuz6hAgh-R-Frmyojiz-TPkVGJJcA1dYrl64BmvibjkrozqCPV8u3EPR1HIpKJ8QmPa0puzC3p42boY1zazsMPvL5h6EhFCcjd2739Qyma_kGJGjb8Zaghbf7YvnYDB7humbZM8VJaF6bAsi8h93G8nOQytOpQrNpmmZcBXfm-s4nO1pUor79iX27EijtwyaTH2HSj8JNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184379545b.mp4?token=UUUo_Enb59_88OF5eEvXXZk-9W_SdI1ZMSCRk8zCdHkMSXl8s3D1O1BHt1qE95vJUXTHiNwiLRorZnDhsfu-CjPrW4FfRQLYsk_Y9FsfrJlw1iaZ-UwnTPMD5wwP_bhLz5T30_YO5dLdBuz6hAgh-R-Frmyojiz-TPkVGJJcA1dYrl64BmvibjkrozqCPV8u3EPR1HIpKJ8QmPa0puzC3p42boY1zazsMPvL5h6EhFCcjd2739Qyma_kGJGjb8Zaghbf7YvnYDB7humbZM8VJaF6bAsi8h93G8nOQytOpQrNpmmZcBXfm-s4nO1pUor79iX27EijtwyaTH2HSj8JNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خانعلی زاده کارشناس صداوسیما:
افزایش نرخ بنزین و گازوئیل بالای ۵۰ درصد مردم آمریکا رو شوکه کرده
زندگی اونا فیکس هس یعنی پس انداز ندارن وقتی بنزین یهویی از ۵۰ دلار میشه ۱۵۰ دلار ورشکست میشن
مردم آمریکا مجبور شده ماشینش رو بفروشه خونه اش رو بفروشه بی خانمان شدن از گرونی
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69961" target="_blank">📅 00:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69959">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7326381213.mp4?token=UraAWwI_sZx6bqf2L-XUnxmgIQK2hy8XWCQESYC0enWw1WEEWY2enQZ3EfFKSHp-697gakw9bhNs7Z7zOUy3Lu31yT9GWZG_CN6QjaGdtfVWwWPmxIviKZe4BQ64VoMROzTnuBl_Wxw9AywBzfE4Ys1qdz1Kj1ABAI2t7ZKp6VcKfHGU4nBJPnp3nQWgKWhdg7UiWELBT5QpoBUHTNMlp74HYBxjr9-Q6i9-se8nJqA_TTsHM3ozZ9mdPy3rFnbmCwgg3ofexlNxIsun7w2SalCN9n4Iawd51hv1pgLwBoop0VamfFMmMTWjITTdRs4wubCiM-57Rh0qRAXUIuWDsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7326381213.mp4?token=UraAWwI_sZx6bqf2L-XUnxmgIQK2hy8XWCQESYC0enWw1WEEWY2enQZ3EfFKSHp-697gakw9bhNs7Z7zOUy3Lu31yT9GWZG_CN6QjaGdtfVWwWPmxIviKZe4BQ64VoMROzTnuBl_Wxw9AywBzfE4Ys1qdz1Kj1ABAI2t7ZKp6VcKfHGU4nBJPnp3nQWgKWhdg7UiWELBT5QpoBUHTNMlp74HYBxjr9-Q6i9-se8nJqA_TTsHM3ozZ9mdPy3rFnbmCwgg3ofexlNxIsun7w2SalCN9n4Iawd51hv1pgLwBoop0VamfFMmMTWjITTdRs4wubCiM-57Rh0qRAXUIuWDsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🌓
لحظه زیبای خورشید گرفتگی در اسپانیا:
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69959" target="_blank">📅 23:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69957">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aRdLzSzwBaxM-cFTYSGe1yOI1y5UlBir_QJ0EVaDxqK0GvvPVRyN-Vxz87V9zj5k97Uro1qRFqzDemslXmT2QZ0kbl9vIwOzD_WwnFGpgp1bOn50a83_BsZcRXjWX2aQDS8eXSUHKY6c007PkmkhYpmQ3hy6AJs3e6_W93ZzG-IPzMJ_CuBTJdgzS6jf3sHE7hWezx5838bmyRL6iZjAWoWFGzMjZyu72_ppqoeJtUNGH_89oIsXSXzU2wgSBdN3w7Con7qmSURZYnRUgmdIryKKNZa3Vfy3zeYQZTkA7CTrViXIZ-IJwsQNf3hZFpLEAJDpRzBG4DCNO7sWl3UzyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJGAlMH2iQD2Z0t1-nNVX3yJ4EKCr2Vd4EFK_wJb5kI3JDVhuM3F5bsZTCBrFCkMQnx84SivlbZCE1sggYHBhSOqyDpqFuiBAyZNp6aCf8QWTHbs6MGzoY1C7QSYOJkIqZDIom-PdNTMSuZLluHtvJ0vqnxEik--grWmKsyHVRwOHiwM4ASU4yPKVKQQ8tt56xHPtxRkASCZJMkGwvq7BoPLpoMn7uXqbf9fMMkD1IUfT-A1R5tBM_zd5yYNxs81YTqWkni9wQ__4AEueLhhIHZ-S_quhE2XeYKZnkRVbZtJId7RefMp3y5AfcGIS24SjMvlnsHjFTp5Tgefag0SQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇺🇸
🇺🇸
با اعلام ترامپ کارولین لیویت سخنگوی سفید کاخ سفید این ماه بازنشسته میشه تا با خونواده و بچه هاش وقت بیشتری بگذرونه
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69957" target="_blank">📅 23:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69954">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rraL96QwAbwAyYGfsKTr6Rj6Jtm-2kTaiF1nPEJJIaXg4gJYyaooZ1KcdPjEyGvW6kkvoKVjEIN6789dpMiiLp8wpmSMVF0JYE__wdfNZVu1-CjXW0pcoa9k03VKM0FHlRI8ibtd62Kk1mWJxMDWZZrBM0mf6k7iiBDgvziD6qcT4TbfIjPD3KBxm5aYpN_j6s08hH-FzGyzCEok9BaTQujJSCp_Ogu-0ZXIlFkdL2v_PbIHi7fdxPFjeS7JxwoSuK_mRgpZSYWvDtRDx90aEgffuiDR0-LYrOOtBMB5TfgLyC587PL7NOWBtByEJ231uHIVP-rRUeVRpF2KkkVNdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EqZbwrDBYHU9a3pgyqpcp3U9USSmOYdKNiol_qKDVtEavytW9U6NvQFSwXKci6pMh-1SZAFw2kg4MK7BGXTeMUY7hDCT1McfvC2J5bBOYSAcXirvKxY9Pn3VrQJ17zKBarGeO9TbWC2OyvEWrZ6GpJfme9WgcU893z--8tEZwzi1YIJWSSsmiuqwrHgiDmnBh4PJ-OoTBC4L6MpymjYsnKrOjfAD4MNemkpGV15YxSrHvBaIeoGvaMfu3zI7SK6Dz7yG_KH7kuvN56ka049CVQt6Qg-TIHRD9JYmOgOw4MYpo4uL3niXcMUFFe3SWtY6dl0jBjuTn9WFt-HBs_mtWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ewnCLvII8xr1dymIg5UUKmDC1bo2_KEZJQh-QtlutlgD8vqhdvb_Jvu2C8aOfKNkYwgDw1wGVKrysLaczJheoMtPpIQzRcPG8ESzSWkZQdZ5nJKHeNPv5AN-amp9Kw9cD_mLFKahrD76FbGy05haKROUjJedmFCCNfx6N31VC2lru2W4AAHBGiefTgJleXe90kuf01ZxwvfK5fJFc7ASISImiPva1AjXojh6jCM9ZFXaKr4W8bdHvPO-jO7GJk4efRKLwd6nn_0jubyQRBDJ1sGzRDwmFbeq370Y1fwWBlNfgqx3qUkJNfMdW84k9Yn6ph6JyWfjAziuQXXvLM5hng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دریک، از بزرگترین خواننده‌های دنیا؛
با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]
وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69954" target="_blank">📅 23:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69953">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpV841KNzGccQtkdluHbJQWVEh_-x31J20HKtAyYUgSkMxH1n04sqjoJK9aokp6-2nMEDpAVRlq_dcZezIpQwLSWmmRx07SZgpWfbXz31aiojM8E_LlArjm95iC5ZPYdnYu_4vaa2Bydf6gt_G2cN6kRBmTJkHZYEpUOhMJKge3KdENb6FujeMKAdOJfeNtaipK48wN0jqWZdHrMJzDEIbRKhTo_m9Jfua2VvwOSDT9zMkBq_BhE_VzXJjYDiLn-N2d_-h8ZC6oQnr-nk0leE1fF56fsfzJT80aMEZrmtWpEcgs5ODL4t7r24bC7LQIV3nJXSGdBVVXY5L-HRo0ONQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
یه اکانت تو ایکس:
ایلان ماسک باید بریتانیا رو بخره و آزادی بیان رو به اونجا بیاره.
🏴
ایلان ماسک خیلی جدی:
[بریتانیا] چند
؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69953" target="_blank">📅 23:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69952">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
تصاویر منتشر شده، مجموعه‌ای از حملات هوایی انجام‌شده توسط نیروی هوایی و پدافند هوایی روسیه (VKS) را نشان می‌دهند، که به شرح زیر است:
• پنج بمب FAB-500 علیه یک پایگاه نظامی ارتش اوکراین در منطقه نووژوینکا، استان خارکف؛
• چهار بمب FAB-500 علیه یک گذرگاه خاکی در منطقه مایاکی، استان دونتسک؛
• پنج بمب FAB-500 علیه یک پایگاه موقت نیروهای گارد ملی اوکراین (NGU) در شهر دوبروپیلیه، استان دونتسک.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69952" target="_blank">📅 22:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69951">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
آغاز عرضه بنزین با نرخ ۸۷ هزار تومان در کرمان!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69951" target="_blank">📅 21:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69950">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mo6U1koR9m_8A6NJl2NtYGgDs2LJD8qA0_FbhpQP72OsKQOn4mt05_d2tGwTjPizRF00UXHArrYYlPVahyAjoFi_-ySnwgUI-_Qu4251-eEX63W5JvPVMEsCw0jCSduxnnMN9PhgmnHmwHZMAovN1AWKbwpJ3-eFyfaf4v69vEKahRd80pj_OMbY4Hw58RZqwXUZWJYZ63LooWyFekbBH6oL-HNMBflL2rWO2L1l4juLmpW2zsCglbGhyGAfN-HhpxnOq4NmaDGcFGx-KcWen91R8Mmkbhf1IHLHc86RedIoFEnTQTkb8Sv-VM35J59WFUbHcAAUYgrSBPvGQNf9Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آغاز عرضه بنزین با نرخ ۸۷ هزار تومان در کرمان!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69950" target="_blank">📅 20:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69949">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4147c4b4.mp4?token=juAldvgChnSFMrBDecRH8BM0i81foKoSZDcZ3-6Jg7OwA-adBUkOEAOxM-ewBBgClGfU23ySQlj1AGv1UzQm5Qqg6EP0stJ_05GQCY0LXzrIgckP6FYgNY248aJiKs7uR9x-JBjgxG9OmIzdBJeXlfoUjkQogEJK8ubWn9lPEEZ7fZNfPpICDgdMrjaOSKn3Om8g3eD_OjboFTD7Kdfr84dA96T6CHtkGwVABd1alr06kmC65OLP1PX_-ieNk-McQgFYaltoteAfH-Y-mMIvRtavbVyX7nOuB2fdGagY_Wpr-t3fabTrfTANwQGqrT9z_O0iaRCWOHfA3mwSbFPGRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4147c4b4.mp4?token=juAldvgChnSFMrBDecRH8BM0i81foKoSZDcZ3-6Jg7OwA-adBUkOEAOxM-ewBBgClGfU23ySQlj1AGv1UzQm5Qqg6EP0stJ_05GQCY0LXzrIgckP6FYgNY248aJiKs7uR9x-JBjgxG9OmIzdBJeXlfoUjkQogEJK8ubWn9lPEEZ7fZNfPpICDgdMrjaOSKn3Om8g3eD_OjboFTD7Kdfr84dA96T6CHtkGwVABd1alr06kmC65OLP1PX_-ieNk-McQgFYaltoteAfH-Y-mMIvRtavbVyX7nOuB2fdGagY_Wpr-t3fabTrfTANwQGqrT9z_O0iaRCWOHfA3mwSbFPGRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محمود احمدی‌نژاد درباره حسین طائب(شهریور1392)؛ «مشکل روحی روانی دارد»
ایشان [طائب] تعادل ندارد؛ همه مقامات کشور می‌دانند.
اصلاً کارش پرونده‌سازی است. از وزارت اطلاعات انداختنش بیرون چون دوبهم‌زنی می‌کرد. باید معلوم شود ایشان بر چه مبنایی در این کشور کار می‌کند.»
❌
حسین طائب به دستور مجتبی خامنه‌ای به فرماندهی بسیج گذاشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69949" target="_blank">📅 20:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69948">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4396720d1.mp4?token=re-rjUjA1V89IzBhBLzaidtP57kuX3WufaXALl6mxA-pXNIs17u_TNrJ5wsr7fYiA2LSJ3Dtw2nI86Kd1hHO45yo4yvK6AJ8NFTbLTEW4DaO9b9EXuLCvZOqmMsg5htzSshd6QYVGCvF0xKcgp31Woj6-gEJW-SvCRQI8W1YIZUOMKsai_s2gGeJWM8ngKWRFyU0Ngc-wMN38QBX3yZi7pavT1mTU_xHdUhhGSHf06R4hm1fiS2BadYH-VtYWnnKedu9ADpzY5HxtbuN1YIiNZxUJ2O-4--VkF4l2Rg1nfiRFHifRLY0S4m8pgDG_F9q4efcwEFafSTcTp2b0lqSrXYutMxBxMIHR_KmvKPN-YQI-b0kG51VSo3GGw1-HUd2d7no12XhJ0ux69StLgU5YOhcYkXJpTen8-pxG69aH_fCuTgLbVjGWCVJkpXvbQHgnQaNhk8bIaHXXCC0YDRHhPbL7SHTW38l2x4ON_8Fl9aQH517zzH6KeY8HA7u8I_CaKSb86t_EolZPtc_seD6rvqDsWY4fkkR0f5vKK4yhh_TC2kqvYGQo3GH52i10YVNxpUfwEmu1P159qUUjI1A9pRkc1crcnMZ76fdKPUlXdGrG06aZovJAEr7Tc32Vy8G4b0JjtaXh4SD-Lc8khJ8UTl8xfx7VaMuzCIPfnqojuo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4396720d1.mp4?token=re-rjUjA1V89IzBhBLzaidtP57kuX3WufaXALl6mxA-pXNIs17u_TNrJ5wsr7fYiA2LSJ3Dtw2nI86Kd1hHO45yo4yvK6AJ8NFTbLTEW4DaO9b9EXuLCvZOqmMsg5htzSshd6QYVGCvF0xKcgp31Woj6-gEJW-SvCRQI8W1YIZUOMKsai_s2gGeJWM8ngKWRFyU0Ngc-wMN38QBX3yZi7pavT1mTU_xHdUhhGSHf06R4hm1fiS2BadYH-VtYWnnKedu9ADpzY5HxtbuN1YIiNZxUJ2O-4--VkF4l2Rg1nfiRFHifRLY0S4m8pgDG_F9q4efcwEFafSTcTp2b0lqSrXYutMxBxMIHR_KmvKPN-YQI-b0kG51VSo3GGw1-HUd2d7no12XhJ0ux69StLgU5YOhcYkXJpTen8-pxG69aH_fCuTgLbVjGWCVJkpXvbQHgnQaNhk8bIaHXXCC0YDRHhPbL7SHTW38l2x4ON_8Fl9aQH517zzH6KeY8HA7u8I_CaKSb86t_EolZPtc_seD6rvqDsWY4fkkR0f5vKK4yhh_TC2kqvYGQo3GH52i10YVNxpUfwEmu1P159qUUjI1A9pRkc1crcnMZ76fdKPUlXdGrG06aZovJAEr7Tc32Vy8G4b0JjtaXh4SD-Lc8khJ8UTl8xfx7VaMuzCIPfnqojuo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش شهروند اماراتی به شلیک به پرچم امارات توسط مجری صداوسیما در پخش زنده:
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69948" target="_blank">📅 19:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69947">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d7922013.mp4?token=Izv_BcgvmCeiflsaocYa8j0n05RpUB6LxbRzQ2eRAHFA6d_HeMaXaWdnWZEaR0tKv9CN0_dlbgfvwYF3Nbplxo8rDPCuOR8uv5N9W24wrG5DXA7n5gmS4D5ASHfaMJF6sjdXClCGgx9u3BcZihngEWwv6vv5BPeAsUbBXCBlfFI9xC-5NXyjf8rSrnhu4hmMFMMoWqga86P7R3ujWHYmt61p79wWp8UF4g6rawyjD3M16c7rU6DpQGHOVjSvEJj1-1-5CORrxTTruBGHG0V5VrkNJ-v_qfCg9gapQtzC580_We8ZrwGFkHOASSWMovEF9sGaCKR6s-l9BM4gvlww6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d7922013.mp4?token=Izv_BcgvmCeiflsaocYa8j0n05RpUB6LxbRzQ2eRAHFA6d_HeMaXaWdnWZEaR0tKv9CN0_dlbgfvwYF3Nbplxo8rDPCuOR8uv5N9W24wrG5DXA7n5gmS4D5ASHfaMJF6sjdXClCGgx9u3BcZihngEWwv6vv5BPeAsUbBXCBlfFI9xC-5NXyjf8rSrnhu4hmMFMMoWqga86P7R3ujWHYmt61p79wWp8UF4g6rawyjD3M16c7rU6DpQGHOVjSvEJj1-1-5CORrxTTruBGHG0V5VrkNJ-v_qfCg9gapQtzC580_We8ZrwGFkHOASSWMovEF9sGaCKR6s-l9BM4gvlww6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه کافه مذهبی با آپشن‌های فوق العاده توی تهران راه اندازی شده:
نوشیدنی‌های خارجی مثل کوکاکولا حرامه.
موقع اذان، توی محوطه کافه میتونین نماز جماعت بخونین.
پرسنل قبل از پخت و سرو غذا و نوشیدنی، حتما باید وضو داشته باشن.
کافه، نزدیک مزار شهداست و میتونین دیتِ خودتون رو اونجا ادامه بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69947" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69946">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69946" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69945">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0GiaF1d4P80bxX5q4-nY2igCa7TZcY1eDPcJFze6p1cEsZFx5Hzn55F7MNFWMNvVjpC770M-ozu2Y6vg5vSPPy6vC7fTI0vA20V-QJ-HrPvGDTNgKVZo39GCcKiRKLNgg_3Lt-25msq8GQAhu7W22YkWQfbZ6l8f7YCX_KekSVZ1xbe0i1XXSxlWWSfh099VHA92zPSZpN_2UiBtJIoQ4UvnlpDMflues0LDGyDjrvKtwdiZWyKUxHaINJXujpUAgU2E_mzQykEg8jcwRSgqtnNo-Djzykj80b5lkQEnklfLMqnd7SbSf9fWBtgeuxI4zEK9Ivfub9dtuPmEN-ACA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g21
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69945" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69944">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qq-RTAoL-1WVNY_1Wzoxa-nbIYjUSsrm5eF_ONoC5NKlwpLqgbCiSCIyWtvCFx8pCQVnwG2qqLlAEijrUeVB8UDWqOIcO4MfX7r6h42SbwPbkFMoWH05lxrkVS6q5b-y2uOxN7UBBeiUtKU9V3Vt_MGfo4IhZ74T43jB9YPvyY1etkAxOWt2u6a6ATPxQmWO_hh6gWxi-A0ft9MLhyMvEdcZOQJL7sJncuDB-pRFEjKXDLGhBgNo2YsOleqFAxzLMd49ACpHZ4klKrMrzUZrRW26ba1tn4QD0ae1DtZZPkWltnTygqy46H9_WtyloK3rn5YZZd-ZqzT_MUkxIi1H2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ایالات متحده کنترل کامل تنگه هرمز را در اختیار دارد. فکر می‌کنم آن را حفظ خواهیم کرد!
همه، محاصره دریایی ما را «دیواری از فولاد» می‌نامند و ایران هیچ کاری نمی‌تواند در برابر آن انجام دهد.
آن‌ها نه نیروی دریایی دارند و نه نیروی هوایی؛ سربازان باقی‌مانده‌شان حقوق نگرفته‌اند، سپاه پاسداران درهم‌شکسته و در حال فرار است و وضعیت «رهبری» آن‌ها در بهترین حالت، نامعلوم است!
آن‌ها پولی ندارند؛ کشورشان «از هم پاشیده» است. تنها چیزی که دارند «اخبار جعلی» و تورم ۳۰۰ درصدی است که روزبه‌روز بدتر هم می‌شود!
ایران فقط حرف است و عمل ندارد؛
دیگر خبری از آن قلدرِ خاورمیانه نیست.
ستایش از آنِ خداست!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69944" target="_blank">📅 18:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69943">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/265374f5d2.mp4?token=hZFDnJASfVNJztuyP1NYz9DwQIrPZ7JyW2m-RAo4dop-7L4aGftalBm72Bs_b0Q7IQaszbVvCycAqXYMwhzZyHBp9bZKb8nF_kR0UA18WL_O6uaklGXV5lXO1fECGlCbTxDbLcW6jOY3qyoNeTvlHnJtmL4zH8C5FN8X1oCoRfPshEdatA1BLPV3pVQlDcppYILQnC1nANvco3zq-tLya7c4B_B5rN6_4O0vKUxZgwMHvp-SCTqpBBMU_gmImnhySLqlcrsKFblzUymXCV6TZtGX_py5_lMAAuwHnSxjd34NtoW_yXx_2h8QyXUtuaNgeI3U4Ntd2CINFTb3X6BQMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/265374f5d2.mp4?token=hZFDnJASfVNJztuyP1NYz9DwQIrPZ7JyW2m-RAo4dop-7L4aGftalBm72Bs_b0Q7IQaszbVvCycAqXYMwhzZyHBp9bZKb8nF_kR0UA18WL_O6uaklGXV5lXO1fECGlCbTxDbLcW6jOY3qyoNeTvlHnJtmL4zH8C5FN8X1oCoRfPshEdatA1BLPV3pVQlDcppYILQnC1nANvco3zq-tLya7c4B_B5rN6_4O0vKUxZgwMHvp-SCTqpBBMU_gmImnhySLqlcrsKFblzUymXCV6TZtGX_py5_lMAAuwHnSxjd34NtoW_yXx_2h8QyXUtuaNgeI3U4Ntd2CINFTb3X6BQMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
روایت دختری که در 13سالگی به همراه مادرش از کره شمالی فرار کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69943" target="_blank">📅 18:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69942">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c105f96b5.mp4?token=U8eSdcOVOjKkTzG9Iuo6i-Z7YBRlxS6uccLvB2CwhewrK-1HUS7xGJRt4Z8Sp7-oWBZs4do4tQ55oexjcskZSh52FrRyc6dJM6PPU7uOV-3PRWzMsBjNUdah290CPegalnf88YIizZOCyQjM0lKsGUB8SC0IKyvF_N10lXU2UjbYdaGbx8PuFuhmVG5y3HM_9hYTFKLVq5tYItcT26jaJZBi-d9aNh5eV47gLTt9_9293xnK_RRwdSF8vKZKpB-3fh45sZeLwTsAkeeAPGtWNjUOvwDok_qXzf5T8plBLiHamziYnnU4C4-_jcbfDt4PXUVCBdJdrhb6WjrRWtkkNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c105f96b5.mp4?token=U8eSdcOVOjKkTzG9Iuo6i-Z7YBRlxS6uccLvB2CwhewrK-1HUS7xGJRt4Z8Sp7-oWBZs4do4tQ55oexjcskZSh52FrRyc6dJM6PPU7uOV-3PRWzMsBjNUdah290CPegalnf88YIizZOCyQjM0lKsGUB8SC0IKyvF_N10lXU2UjbYdaGbx8PuFuhmVG5y3HM_9hYTFKLVq5tYItcT26jaJZBi-d9aNh5eV47gLTt9_9293xnK_RRwdSF8vKZKpB-3fh45sZeLwTsAkeeAPGtWNjUOvwDok_qXzf5T8plBLiHamziYnnU4C4-_jcbfDt4PXUVCBdJdrhb6WjrRWtkkNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه روش فوق العاده برا تقلب در صورت آموزش تصویری
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69942" target="_blank">📅 18:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69941">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⏸
صحبتای یه فرد رندوم:
سوال من اینه؛ چرا بعد جنگ 12 روزه خبری از این تجمع‌های شبانه نبود، ولی بعد جنگ 40 روزه شروع شد؟ دشمن که همونه؛ پس چی عوض شده؟
دلیل این تجمعات شبانه مخالفای داخلی‌ان یعنی مردم خودمون؛
مخالفای حکومت هم مردم همین کشورن، وطن‌فروش نیستن. ممکنه با حکومت مشکل داشته باشن یا طرفدار یه مدل دیگه حکومت باشن؛ خب حق دارن نظر خودشونو داشته باشن.
اگه واقعاً می‌خوایم بدونیم مردم چی می‌خوان، یه رفراندوم برگزار بشه تا نظر اکثریت مشخص بشه.
سال 57 یکی از اعتراض‌ها این بود که مردم آزادی بیان ندارن و مخالفا سرکوب میشن، اگه الانم مخالف نتونه حرفشو بزنه، پس دقیقاً چی تغییر کرده؟ مخصوصاً وقتی وضعیت اقتصاد، روابط خارجی و خیلی چیزای دیگه هم بدتر شده.
در نهایت هر ایرانی می‌تونه کشورشو دوست داشته باشه، ولی در عین حال منتقد یا مخالف حکومت هم باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69941" target="_blank">📅 17:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69940">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eq5p2ZlqsJFWncNwXzF1Pc7_3AmRsJD5BCqvLy6RPW8RavzuAHvxXC3i975Ahr6WOEYviEgQZA2FYkCiIYMCa7jZ4o6wGveGVxzXfTfF6cP_4SgUJ-ISS1Vs14GAPfUpJDviJIFcQpSVtjokLX97rGDA9RP-bNJyp4niJ71dL5adAFCvK-pI-kk8S6PKT93lx42XDLtC7JQg05l8omBE_z2rQkYfRe4VdgUfJxSkrFt7XVmV5LDkCuU9-lEZnoDG0AgRb9GCDHfWmxJRBWwjRSaNjNQwW3zLRsPfjOS65SQv8NRdI42HbceIX-LgIoyujEDD3ydb_CJpVco6uR9Zbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو ایتا، یه آخوند به اسم  "شیخ ‌احمد " چنل آموزشی با موضوع مقابله با غریزه جنسی فرزندان راه انداخته
😶
مادری که پسر جوان تو خونه داره، نباید با آرایش و لباس آزاد تو خونه راه بره، باید چادر بپوشه چون باعث تحریک شدن فرزند و راست شدن شومبول وی میشود!
همچنین پدر نباید با شورت جلوی فرزند دخترش راه بره، باید حیا داشته باشید.
پدر مادرا جلو فرزندانشون همو بغل نکنن، وگرنه میرن جهنم
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69940" target="_blank">📅 17:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69939">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9298752134.mp4?token=rO1oEOvQwt5h_0jMBdJ0ivMFbzRp_5VUI5Cbb5-54BLsR9SfYtiYPADoRc2nEZy8OZBDhYkNeOFNbvXAcR0LM2hUHoIZSEKcCsrBTVmHT-SfIZXVmr62vr4AQQKcVz-SSyt4m9RD-93ehHJk557TVgUrA2bXjhpSAiZ0evWTobc9S3QJlAxUMMXFFZuYKYJbZambTFguE3-WWH5ozswQ9mE6pYn0uKaxHSQuK3vt7yTbBJNXeDlQdshRUTXSOt5JoRgru27hV5Bop2FDPgc9rHJ-5UDZerDnS-FFE9WtqV5R0dQw-83VSoOy_Mxf9QuQ82nJT9cXQrj8-vZxZ4jO9oFk3SLm1P3IiPkCLw7RtL6LoTzrjq7Q9vekMiVjc1_OH52gZ7D5tjyvniHHuh68ERVF-l39A8j1C9ZGRXi9D7yH2MvSSOwhRqIYYATItuP7bLyzpng9vDsqx_RDeZljVAaItas7bABXG-jlglOxXoG4K0IKxND4IWn4f78QNQyOnRO2bJ5OgK9ALhQehnmYst3OhuWKsCMJctYLxMoXUygv3uI0UgJJcslDa2YswIHHXyhBUQT4hdiLxQ5RdXVAudGJdxyp_oqNiYsJv8qH4QNt3VEWORBKsZTUVHPC6C8UZCvUt481DgJ7IB9qH3LiQ67UsOf7mo4vk1wCVB3d3KY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9298752134.mp4?token=rO1oEOvQwt5h_0jMBdJ0ivMFbzRp_5VUI5Cbb5-54BLsR9SfYtiYPADoRc2nEZy8OZBDhYkNeOFNbvXAcR0LM2hUHoIZSEKcCsrBTVmHT-SfIZXVmr62vr4AQQKcVz-SSyt4m9RD-93ehHJk557TVgUrA2bXjhpSAiZ0evWTobc9S3QJlAxUMMXFFZuYKYJbZambTFguE3-WWH5ozswQ9mE6pYn0uKaxHSQuK3vt7yTbBJNXeDlQdshRUTXSOt5JoRgru27hV5Bop2FDPgc9rHJ-5UDZerDnS-FFE9WtqV5R0dQw-83VSoOy_Mxf9QuQ82nJT9cXQrj8-vZxZ4jO9oFk3SLm1P3IiPkCLw7RtL6LoTzrjq7Q9vekMiVjc1_OH52gZ7D5tjyvniHHuh68ERVF-l39A8j1C9ZGRXi9D7yH2MvSSOwhRqIYYATItuP7bLyzpng9vDsqx_RDeZljVAaItas7bABXG-jlglOxXoG4K0IKxND4IWn4f78QNQyOnRO2bJ5OgK9ALhQehnmYst3OhuWKsCMJctYLxMoXUygv3uI0UgJJcslDa2YswIHHXyhBUQT4hdiLxQ5RdXVAudGJdxyp_oqNiYsJv8qH4QNt3VEWORBKsZTUVHPC6C8UZCvUt481DgJ7IB9qH3LiQ67UsOf7mo4vk1wCVB3d3KY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
کلاس درس «ریاضی ولایی» با تدریس محمدباقر خرازی:
«شما اگر ولایت داشته باشی می‌ری زیر خط کسر...
اگه شما به این دکترای ریاضیات رو بخونید اصلاً این‌طوری نمی‌فهمن...
حروف قرآن از راست به چپه اما انگلیسی که زبان شیطانی‌ست از چپ به راسته...»
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69939" target="_blank">📅 16:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69938">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
🗞
رویترز به نقل از یک مقام ایرانی:تهران و واشنگتن در مورد تمدید آتش‌بس گفتگو نمی‌کنند.
این منبع افزود که از دیدگاه ایران، هرگز تاریخ رسمی آغاز آتش‌بس وجود نداشته است و بنابراین، چیزی برای تمدید وجود ندارد.
این منبع ایرانی، ایالات متحده را به نقض توافق‌نامه همکاری متهم کرد، این در حالی است که این توافق‌نامه تنها ۴۸ ساعت پس از امضای آن نقض شده است.
این منبع همچنین گفت که مذاکرات فعلی بر بازگشت واشنگتن به توافق و تعیین یک جدول زمانی برای انجام تعهداتش متمرکز است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69938" target="_blank">📅 15:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69937">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27e246580c.mp4?token=m1NHS7AypvnrjNFervCvnFj52XX3kArYJZgkTaH5yc_1_0eDUWrxePDHFe3bpjbziGlPFZquGbeqAIHreeFwvQD_vUkPQvmJGQSk_6uwDqZNVh5hb1SnMAWwCljKVicRHr7oVRIMSQh2GjZYHylT0fcgjoxfp2cYUBtRs6hjItM246SjllhUUsjZ5ZQIF1qbLA_l5G17wyGxb2V1ACWMtHtui5CB_pPpW7PPFjlsr-j1ZpnMvom49DvgPLZM5_SsmTb6N3Q0PLU6witjUOZK8o24r83Jccpotod6C09B-r9VwawjyKp6fIZ9My2vCxk_SSz1_rmB5o8l9-3Gbk9IdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27e246580c.mp4?token=m1NHS7AypvnrjNFervCvnFj52XX3kArYJZgkTaH5yc_1_0eDUWrxePDHFe3bpjbziGlPFZquGbeqAIHreeFwvQD_vUkPQvmJGQSk_6uwDqZNVh5hb1SnMAWwCljKVicRHr7oVRIMSQh2GjZYHylT0fcgjoxfp2cYUBtRs6hjItM246SjllhUUsjZ5ZQIF1qbLA_l5G17wyGxb2V1ACWMtHtui5CB_pPpW7PPFjlsr-j1ZpnMvom49DvgPLZM5_SsmTb6N3Q0PLU6witjUOZK8o24r83Jccpotod6C09B-r9VwawjyKp6fIZ9My2vCxk_SSz1_rmB5o8l9-3Gbk9IdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حرکت عجیب مجری در پخش زنده
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69937" target="_blank">📅 15:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69936">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMo031n12AHsRO78pIvDlLta1CDdlvWSXp3kSz5wp2YywxV8gT8_0NcHI4L_gxSPHiLZ9tuvRYFG3PzhVwJqo2nZasxaf3Qr1KU_Ak4RGccV2ioiinWGrHVN9t0eBW-lYuuWkGBnN3A_4us38lX13v400HBRG19CQYkvFqUXhEj2okAHBra-QkshAMN_LsqmhSGqHM5vj8dZkxKGOiKawcRa5fWXuAgC0dIwA-ACovNPpFND6tWroelo63T6pzcXfCm_ivPULnLcxSGmI4Duio8PuUZFM9fU-0B6yA1eixg1wFi9NZiHnLob5Ra9Wl2_XvZLZxKa5Y6cToCRrZNdug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
🇹🇷
🇺🇸
نیویورک تایمز:تهدیدی که از سوی ایران مطرح شد و باعث شد رئیس‌جمهور ترامپ ماه گذشته به طور مخفی هواپیمای "ایرفورس وان" خود را تغییر دهد، زمانی آشکار شد که او در آخرین روز حضور خود در اجلاس ناتو در آنکارا، ترکیه، در تاریخ ۸ جولای، در حال عزیمت بود.
اطلاعاتی که توسط سازمان‌های اطلاعاتی آمریکا جمع‌آوری شد، نشان می‌داد که یک تهدید خاص از نوع موشک‌های زمین به هوا علیه هواپیمای "ایرفورس وان" وجود دارد، صرف‌نظر از اینکه کدام هواپیما حامل رئیس‌جمهور باشد.
همچنین، فردی که در نزدیکی محل برگزاری اجلاس ناتو حضور داشت، در حالی که یک موشک قابل حمل روی شان خود داشت، مشاهده شد. در همین حال، عوامل ایرانی دقیقاً می‌دانستند که ترامپ در آنکارا در کدام محل اقامت دارد، از جمله طبقه محل اقامت او در ساختمان.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69936" target="_blank">📅 14:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69935">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7465fa629c.mp4?token=UDFkuUq8wnM0-N_XtNG3skThhHTdfvwEC_4k_1Kw_nET8XYkqSaRQ04GCTvOrkXj4n6RUt6DDaqpEpn5uGOCDlI8hpogGPfKc6jk0-376Z4u0oEGHU_DViXtx0_Vp-RfFgJTFlaYS6O80YVMfASCmC2xywWVKnH_FSD6_0sYpW9J9AjpX1qiexEoCVTWGU8qWKjTuWy6aYkbX18KuVKh_napMLl7I13tfFb7pOmw87dOU0fRtJvnNxvZ3I-WPM3dm3tfCHQ3X6sMfbdhySUYqj6h9V8s9eDrUQcF59gLdSazBXzKP94bNQxS_hnzmKSkQUpW_m4NkDTAwXCMexBQ15IKPox6MB6c_ehv6b7yGHV9arHOGZ33vQ3-9OTvwjeoTW2Hlt9ezmxus7i1gPPtTFAmdCS7vCDbHx3q0yYDAy6TTOHJB-vTSEON2-j3vXQ3QCBHtojUtmTi1uXatJ1dBWPq52G1BwnIiY9gTtX-agwCCaxo9iBdjah4ap4Y6u_1mHtEPR0nBZrIGim-BWA3qrVETtYwR465yRTZjgeAkGxQkAk-gvBHld-pPSWUUC-apexsCuaBk9w2qJw_PA2BrPPHklq1nGwCMsvyMMuMsm1mGkoS-eux48W4te18mTiRaFDZxOf6qlw2MiUxRLrdSbBZSdDMOsvAAykm-GhZuKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7465fa629c.mp4?token=UDFkuUq8wnM0-N_XtNG3skThhHTdfvwEC_4k_1Kw_nET8XYkqSaRQ04GCTvOrkXj4n6RUt6DDaqpEpn5uGOCDlI8hpogGPfKc6jk0-376Z4u0oEGHU_DViXtx0_Vp-RfFgJTFlaYS6O80YVMfASCmC2xywWVKnH_FSD6_0sYpW9J9AjpX1qiexEoCVTWGU8qWKjTuWy6aYkbX18KuVKh_napMLl7I13tfFb7pOmw87dOU0fRtJvnNxvZ3I-WPM3dm3tfCHQ3X6sMfbdhySUYqj6h9V8s9eDrUQcF59gLdSazBXzKP94bNQxS_hnzmKSkQUpW_m4NkDTAwXCMexBQ15IKPox6MB6c_ehv6b7yGHV9arHOGZ33vQ3-9OTvwjeoTW2Hlt9ezmxus7i1gPPtTFAmdCS7vCDbHx3q0yYDAy6TTOHJB-vTSEON2-j3vXQ3QCBHtojUtmTi1uXatJ1dBWPq52G1BwnIiY9gTtX-agwCCaxo9iBdjah4ap4Y6u_1mHtEPR0nBZrIGim-BWA3qrVETtYwR465yRTZjgeAkGxQkAk-gvBHld-pPSWUUC-apexsCuaBk9w2qJw_PA2BrPPHklq1nGwCMsvyMMuMsm1mGkoS-eux48W4te18mTiRaFDZxOf6qlw2MiUxRLrdSbBZSdDMOsvAAykm-GhZuKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇷
محمدرضا نقدی، مشاور عالی فرمانده کل سپاه پاسداران:
«ما بیش از نواخت شلیک موشک‌های بالستیک، در حال تولید و تحویل آن‌ها به رزمندگان هستیم.»
«ما فقط ۹۵۰ شهرک صنعتی داریم به علاوه صدها مجتمع صنعتی که خارج از این شهرک‌ها هستند.
اگر روزی برسد که ما هیچ موشکی هم نداشته باشیم، ما خطرناک‌تر می‌شویم چرا که دشمن با تاکتیک های ناشناخته ای مواجه می‌شود که می‌توانند منافع آمریکا در جهان را به آتش بکشند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69935" target="_blank">📅 13:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69934">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TholqMOu9FC3VQvZKKVNN9NPiPW6wxkAcjt3nLS6knMCseWJrkM_Tua8eNkdOyTbe6QjKzq984HOLDBqnL2O4h1lRxQlJ8FKpXnVoemLmTcg1b5imZ0FoMzDBTEzJzLj4R5TPxqwhESLixuSFwyl54igNWHG8xX83mi1XzRlAzE4DMcBhhaazdTzAkkIeJKRxZFPmo_WJRRrlGwtrf1cQv7Ywr3QmiWNd0h1DXofGO4scK8YzWoxiMZUNyykuQoAqY6aP3HuFBrA-Zi9Ubg-W1h6_E8jg583E4uLg56jAqTKUZqPdnmz0QDDkzB2VoNCpWAcUVsjeXEKXK7dFWoivw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
امروز ۳ تا اتفاق نجومی قراره همزمان تو آسمون رخ بده:
خورشیدگرفتگی، هم‌نشینی ۶ سیاره و اوج بارش شهابی.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69934" target="_blank">📅 13:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69933">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae5c53c68.mp4?token=XCqwvx9qlTV2uv6MDBaBnXnPwCzfKn53oaiYnacMx5LZ8o6bqdlDkoa5DYFIx58P8JtmfgPZ_WFmPQhcUQxjVr70BgzGMlFY3-Z0cOXwP6qc_LJD7_rZIRW_PYp1PwevnrQIwtzLnySPSJV5F14xDOmJGG2fzcTI1_xSgxuyXqdvFnQKl7tGJvCtgCtpFZCTV4tBDV_xX8ORP3kPbQY_tLqHGGWTlNQ5I27WDKbX8A8Z3nhDWje4eL2ztaZkEW3Njbl1X_Zc7I30zk-QCDYvOpdmWi2gxRTd5V69ztjUvAnaneStoCOLMhMk3xOycM0SgaT5USOtTXAQkNQaXFuNHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae5c53c68.mp4?token=XCqwvx9qlTV2uv6MDBaBnXnPwCzfKn53oaiYnacMx5LZ8o6bqdlDkoa5DYFIx58P8JtmfgPZ_WFmPQhcUQxjVr70BgzGMlFY3-Z0cOXwP6qc_LJD7_rZIRW_PYp1PwevnrQIwtzLnySPSJV5F14xDOmJGG2fzcTI1_xSgxuyXqdvFnQKl7tGJvCtgCtpFZCTV4tBDV_xX8ORP3kPbQY_tLqHGGWTlNQ5I27WDKbX8A8Z3nhDWje4eL2ztaZkEW3Njbl1X_Zc7I30zk-QCDYvOpdmWi2gxRTd5V69ztjUvAnaneStoCOLMhMk3xOycM0SgaT5USOtTXAQkNQaXFuNHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سفره‌ای که واسه عرق‌خوری تو زندان پهن کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69933" target="_blank">📅 12:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69932">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca7afc613.mp4?token=CXH-wJZeguasAfk0kiuPg126yFnYu-D0pkvSOkU1b8NVSzoQDZZO9ds1Ja74yfroo7hHWE1YMLSfwwh24vgNyWN3_mXIwXCugizhA7u2o8IstJzgXQgRDTOiLZxejUZAIks_PRJA_bJNaQ7wRO_a8b28lfXFme5i_o31PQZufvf7DREe2tj37t-ZGWxNvJ-Tg05Jd4mgYtVKeINizt7dBrMOX9pY0hCl4JPA_IOpQyKTzyqT1dAklUcbNDaIvn0_SBrHa1uw6NVy31TLsj7XKvFa8Sjcavd9hpRPz3w3Dh9u9V7hBB-TY6Jg8UNQN__VpoMWQ6DfORpPn4M4mKbmzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca7afc613.mp4?token=CXH-wJZeguasAfk0kiuPg126yFnYu-D0pkvSOkU1b8NVSzoQDZZO9ds1Ja74yfroo7hHWE1YMLSfwwh24vgNyWN3_mXIwXCugizhA7u2o8IstJzgXQgRDTOiLZxejUZAIks_PRJA_bJNaQ7wRO_a8b28lfXFme5i_o31PQZufvf7DREe2tj37t-ZGWxNvJ-Tg05Jd4mgYtVKeINizt7dBrMOX9pY0hCl4JPA_IOpQyKTzyqT1dAklUcbNDaIvn0_SBrHa1uw6NVy31TLsj7XKvFa8Sjcavd9hpRPz3w3Dh9u9V7hBB-TY6Jg8UNQN__VpoMWQ6DfORpPn4M4mKbmzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
تصاویری جالب ، از تلاش ناموفق یک تیم آتشبار سیار روسی برای رهگیری یک پهپاد انتحاری (کامیکازه) در حال عبور را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69932" target="_blank">📅 12:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69931">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd2c3a8ef.mp4?token=cx-NMJXYKPS78w20h2ARTEgmzmywlHHfNxulqFOmeu1kyh8JVpUNQUxUy5K2XnL-YkVQqCl498tqR-TyCMRXGQvGM8Ih_jxwKnwu8TRJ907oCTE1BN6fktXjybzqxhMRpWDsAojkH1llUAC2kgZ1NbemQHGLdBnzWFS60qUdZBerCJM_1ov-mvXP_H-qmWyqiO-MFZCftyxZjwsZb0KQ7y0_fiVa6aOVb0npLI2Nfs2Qx01eCJZRUWkX_WdfaGovgWcLFuvtG3JbHtho4H8cTEEtORQFtKP8cyjjgrDI1vpeYZQgvdf5xF5Vf0ZoWQzmOhKxXoi8I74aYtHy5Dan3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd2c3a8ef.mp4?token=cx-NMJXYKPS78w20h2ARTEgmzmywlHHfNxulqFOmeu1kyh8JVpUNQUxUy5K2XnL-YkVQqCl498tqR-TyCMRXGQvGM8Ih_jxwKnwu8TRJ907oCTE1BN6fktXjybzqxhMRpWDsAojkH1llUAC2kgZ1NbemQHGLdBnzWFS60qUdZBerCJM_1ov-mvXP_H-qmWyqiO-MFZCftyxZjwsZb0KQ7y0_fiVa6aOVb0npLI2Nfs2Qx01eCJZRUWkX_WdfaGovgWcLFuvtG3JbHtho4H8cTEEtORQFtKP8cyjjgrDI1vpeYZQgvdf5xF5Vf0ZoWQzmOhKxXoi8I74aYtHy5Dan3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیویی از هجوم انقلابیون به کاباره های تهران و نابودی هزاران لیتر مشروبات الکلی، در سال 1358
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69931" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69930">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/69930" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69930" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69929">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LAlhFF0NBPL3YzqknkaKm46AkBhIsIYMQ1vJyUlr58_Wiz3vr5lBsewITtTu9YVXeLE5lkaeZf-yWjR_5BJx_ULErkqHKQbcNZV1DSl7rUuJAjsTQQktQNIve6utpY26XjGJFjLOwsO46-nRUGoX6XexsFUFTBhuM93z4hM2x-5mYaCaD_mhx8uK_pfcxwSZcLZJ8BNi7AqnaPeA-h88Zj_3jMzVpbj_doIkZ1crN5y2wfUEL5l556B0DQBVrRfmxrsCtnaTWpO2ol35GYf9hYMAgQDpMEohHhjwhulirBtAAXAQvOpclv6vC9fckyMVkjh3zKptXi7F6DxzeW_nog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌     ‌ ‌ ‌ ‌ ‌    ‌‌ ‌‌‌  ‌
💯
‌
فینال سوپر کاپ اروپا
💯
🆕
دیدار فوق حسااااااس
پاری‌سن ژرمن
و
استون ویلا
رو با آپشن های تخصصی در
MelBet
پیشبینی کنید!
💯
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69929" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69928">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=Ht039rlGj66RWn6a9v_zTIVpLU44iIu_aqnCih7u39EaK5QxmxJ_jga6wFFSkvyh116clKkL0eYSzDCkSO4C8-qEVODUWcn5KQRVqAadPD14JMcg7CEQLVMvvEucsorjGgsFFmkKpeJQp8HArfkKjY4ge5EYo_UlBb4YEIEC6V7j7SeLWEfCf6e-OREgqr6GWzE2DEP-4bNLhPE9_1TxqNhOrUMIXY7rDJE-GcHtxTx77fOkzH2Xf8SQv9oHwO3veSyOxDuU4W5xTr3BgATGyAdEaYbwBpEgVddTPZutVXs56wkH30Lv9mVTN6r2iNXM6nMrDc_jPIVvYEb6XrSYnw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=Ht039rlGj66RWn6a9v_zTIVpLU44iIu_aqnCih7u39EaK5QxmxJ_jga6wFFSkvyh116clKkL0eYSzDCkSO4C8-qEVODUWcn5KQRVqAadPD14JMcg7CEQLVMvvEucsorjGgsFFmkKpeJQp8HArfkKjY4ge5EYo_UlBb4YEIEC6V7j7SeLWEfCf6e-OREgqr6GWzE2DEP-4bNLhPE9_1TxqNhOrUMIXY7rDJE-GcHtxTx77fOkzH2Xf8SQv9oHwO3veSyOxDuU4W5xTr3BgATGyAdEaYbwBpEgVddTPZutVXs56wkH30Lv9mVTN6r2iNXM6nMrDc_jPIVvYEb6XrSYnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قیمت های پشم افکن خونه و برج توی فرشته تهران بعد از جنگ که به متری 2 میلیارد تومن هم رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69928" target="_blank">📅 11:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69927">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6983998d5.mp4?token=Touz0T4P2yeEYHYeN4CCl0AIk159RACmpkE2PFZXD5l_N_9AZFWdp0sUVb--irA53e-gYpWZo8QXOYjrxWE1PVoHmfjPJdWGbSdjZuBjkZNrgD3383rQ-xDKdAvudwtOZoRIOsfiEir2jw1aNn1oo71yy26p1TSzA9I-FY3GuRKmvFnnzCjLTf6FowRRN0xtWKxnCSmn2ZutFCL0WkQPzFDOgKFsVSMnPzJ6jXZWqdEylhPAEGg9jtnGg9TvCiVJb0AOXj9rFqvXkiqxmZ_bu1FCx9Pkmv1zUxQeIdjzjHxAI28HVEp5TQXeF165MmdK2xNd-WxR3DQ7dx_CS3ne_TRGYDOz0JKVubeNl7MhEZiWx2emkeKK-eANFpiQb2bRJp--zf49IBttC4QztueUuxDVDf7bKhWYi12RaXXHC2VUpW48lmOou2uMcHIs5_oOYgOnyL2Zf9EmLOtJBChpermzxwM2Ms3-dzclokVyR-9rKqQO3ab41YHP_t0x7hUNO7gsp3dZ7jp7f1wCjpkb_OTctAiISpHa_VhkVw84Zy3fsaTeBmHUq2M9CiXFt2fj_myZbMymFWfB23-_67F5ECSVx58S0RvJffPAJi4G9IrjKRJpiMd4oRgYEYn12dbpUW22viMQY539WbqvtudrMtjLNy58Er1xJaRlV-Fcarw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6983998d5.mp4?token=Touz0T4P2yeEYHYeN4CCl0AIk159RACmpkE2PFZXD5l_N_9AZFWdp0sUVb--irA53e-gYpWZo8QXOYjrxWE1PVoHmfjPJdWGbSdjZuBjkZNrgD3383rQ-xDKdAvudwtOZoRIOsfiEir2jw1aNn1oo71yy26p1TSzA9I-FY3GuRKmvFnnzCjLTf6FowRRN0xtWKxnCSmn2ZutFCL0WkQPzFDOgKFsVSMnPzJ6jXZWqdEylhPAEGg9jtnGg9TvCiVJb0AOXj9rFqvXkiqxmZ_bu1FCx9Pkmv1zUxQeIdjzjHxAI28HVEp5TQXeF165MmdK2xNd-WxR3DQ7dx_CS3ne_TRGYDOz0JKVubeNl7MhEZiWx2emkeKK-eANFpiQb2bRJp--zf49IBttC4QztueUuxDVDf7bKhWYi12RaXXHC2VUpW48lmOou2uMcHIs5_oOYgOnyL2Zf9EmLOtJBChpermzxwM2Ms3-dzclokVyR-9rKqQO3ab41YHP_t0x7hUNO7gsp3dZ7jp7f1wCjpkb_OTctAiISpHa_VhkVw84Zy3fsaTeBmHUq2M9CiXFt2fj_myZbMymFWfB23-_67F5ECSVx58S0RvJffPAJi4G9IrjKRJpiMd4oRgYEYn12dbpUW22viMQY539WbqvtudrMtjLNy58Er1xJaRlV-Fcarw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداشمون در یک دقیقه به ۱۳ نفر پیشنهاد رابطه داد و  همشون هم ریجکت کردن و تونست رکورد ریجکت شدن زیر یک دقیقه دنیا رو بزنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69927" target="_blank">📅 11:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69926">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
لحظه نابودن شدن خونه های مستحکم و نوساز توی کلمبیا بر اثر زلزله!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69926" target="_blank">📅 10:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69925">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72ecf27139.mp4?token=tZy7tTT4XWAkpxFHIYKeha2jEfhyv6_qqxiFRokN181d0moPkFhrY5w9MNkxKHti5bAsVW46psESn0Lgw_Yy1DDMRtlNTpzaE6kNs7nnfMZYT2WcnOiEDRkNS7ykD8xlK1OAon_zJN4Ox2xj5iJL1uckP6BBmlWWITt4Gb5PFVMZlzkmUSt8pneXolsty3M4PGJRY813id2Tdt3A90yngB1N6oUtU6wrcVJC4hWl6DEtG8lpcPwwBA9qP9TVE7BLrQ1hSPaPhxag9yPj2vU6lIupZPnVcGCiXyzCTgYs6caOYkCMBL1ANA8qHPaw0tyzuUBH-j8w2oyxnUtUNDjXsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72ecf27139.mp4?token=tZy7tTT4XWAkpxFHIYKeha2jEfhyv6_qqxiFRokN181d0moPkFhrY5w9MNkxKHti5bAsVW46psESn0Lgw_Yy1DDMRtlNTpzaE6kNs7nnfMZYT2WcnOiEDRkNS7ykD8xlK1OAon_zJN4Ox2xj5iJL1uckP6BBmlWWITt4Gb5PFVMZlzkmUSt8pneXolsty3M4PGJRY813id2Tdt3A90yngB1N6oUtU6wrcVJC4hWl6DEtG8lpcPwwBA9qP9TVE7BLrQ1hSPaPhxag9yPj2vU6lIupZPnVcGCiXyzCTgYs6caOYkCMBL1ANA8qHPaw0tyzuUBH-j8w2oyxnUtUNDjXsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های یک مقام حکومتی رو ببینید که باخنده درمورد شلیک به سر معترضا صحبت میکنه:
ما به پای معترضین شلیک میکردیم ولی میخوابیدن میخورد به سرشون
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69925" target="_blank">📅 10:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69924">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a54f6b8d.mp4?token=tiaxcKyIpUM57JYVcxMbbD6S4HL9VWaWLZMPnVk-Ms0-PSLRUVU6uUBafICxgmysvi-juavJLQ-8GdLvygc78eCfbiOCzk71-zed1E4f83JsjDdMqfe8znHmsWAWNQdFKOIpz44jwy8riusHPxyl7IkRYAaEPYv8LNYB3EDHs-bvrwncnFAfQCr9pW1IlK6Io-R5pEIEBsxMMqzLCacJiHexSLgq5bdhZffII8AJ6gzvPpHxeRV_qAef3uhUf6bXbygv2fRekQ3Oobc8bKKnraH7FNt6TK3MlZ_W3tY5C3XYUPDQUJCr7ivuSla13LSnhrTFxMAjlDcIkAjVnBcb1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a54f6b8d.mp4?token=tiaxcKyIpUM57JYVcxMbbD6S4HL9VWaWLZMPnVk-Ms0-PSLRUVU6uUBafICxgmysvi-juavJLQ-8GdLvygc78eCfbiOCzk71-zed1E4f83JsjDdMqfe8znHmsWAWNQdFKOIpz44jwy8riusHPxyl7IkRYAaEPYv8LNYB3EDHs-bvrwncnFAfQCr9pW1IlK6Io-R5pEIEBsxMMqzLCacJiHexSLgq5bdhZffII8AJ6gzvPpHxeRV_qAef3uhUf6bXbygv2fRekQ3Oobc8bKKnraH7FNt6TK3MlZ_W3tY5C3XYUPDQUJCr7ivuSla13LSnhrTFxMAjlDcIkAjVnBcb1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:«بازندگان و برندگان انتصابات جدید در جمهوری اسلامی چه کسانی‌اند و آرایش جدید قدرت چه چیزی به ما می‌گوید؟
🔴
انتصاب محسن رضایی به دبیری شورای عالی امنیت ملی و حسین طائب به فرماندهی بسیج، دو پیام مهم دارد؛
یکی رو به بیرون، درباره مذاکره، جنگ و رویارویی با آمریکا
دیگری رو به داخل، درباره مهم‌ترین نگرانی حکومت: خطر خیزش دوباره مردم ایران.
در حالی که هنوز درباره زنده یا مرده بودن مجتبی خامنه‌ای و میزان سلامت او تردید وجود دارد، سپردن بسیج به حسین طائب، یکی از نزدیک‌ترین افراد به مجتبی، یک پیام روشن دارد:
نگرانی اصلی حکومت، خیابان است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69924" target="_blank">📅 09:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69923">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa002b9fb9.mp4?token=eazNROgSt1opMgwK7Lmh1vtUbqSQyhhl5b-j9bobtf7AOg1iirv-lh0metgM1NYV8MbOmJTKHmh-0d-sRCzd-V5l_4jl034i0iu9XUhbFZ2Sh8KADMpT-GFKKYXu2-fqWLyzT7IZg4woQ4i0RLsbI99zznDNvYOepasvOMS2LYeVqWy-Te5yUsYc3RUj1mXhpTcyWGyc_St1F5ATdKRXOXVT_3-Ue2KsbH0yF_QhAUBH5fZw-pFO98V-aj6qa88tA6AiFra8j7FLlBwPF7HQlty2pJAhc3DEvGOlgPIXSBSzTkvWqMSv8yqCtBmn_5jzcP2mrB6D-3G3vJ3-H2PwCxA_tqaZKiqH2-JMZgRqlE7sJSzM0SUV2RPsQ4FSnQ2G94-Y2MotVoceTJe0Q4jwz7jS6xnvg9pvntu5cC1K8-4LTmk1RlKjGSf8nhbf26cxGnxX-hxzF_gT7e-Q8NQMuF6_9vUkj03jX77DsrfoV5fVAXbsY63k03-VnhOyqu9XpsX_d3PwlNVS3s1J9i-bxRz9jizl6CtkYhPevzGOVnOQ7NlQ4G4Dqr86NeM_VPmfdMtvhDYhXOvvGEkaVT4cnObo2W82P5RmhJeqzIO_iYsVt6NxI1hz_rm0UFsyZ3yaJEmSZnXM038kJZfWJh0HcaKT3hzhAE5plgtwH8E6nrk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa002b9fb9.mp4?token=eazNROgSt1opMgwK7Lmh1vtUbqSQyhhl5b-j9bobtf7AOg1iirv-lh0metgM1NYV8MbOmJTKHmh-0d-sRCzd-V5l_4jl034i0iu9XUhbFZ2Sh8KADMpT-GFKKYXu2-fqWLyzT7IZg4woQ4i0RLsbI99zznDNvYOepasvOMS2LYeVqWy-Te5yUsYc3RUj1mXhpTcyWGyc_St1F5ATdKRXOXVT_3-Ue2KsbH0yF_QhAUBH5fZw-pFO98V-aj6qa88tA6AiFra8j7FLlBwPF7HQlty2pJAhc3DEvGOlgPIXSBSzTkvWqMSv8yqCtBmn_5jzcP2mrB6D-3G3vJ3-H2PwCxA_tqaZKiqH2-JMZgRqlE7sJSzM0SUV2RPsQ4FSnQ2G94-Y2MotVoceTJe0Q4jwz7jS6xnvg9pvntu5cC1K8-4LTmk1RlKjGSf8nhbf26cxGnxX-hxzF_gT7e-Q8NQMuF6_9vUkj03jX77DsrfoV5fVAXbsY63k03-VnhOyqu9XpsX_d3PwlNVS3s1J9i-bxRz9jizl6CtkYhPevzGOVnOQ7NlQ4G4Dqr86NeM_VPmfdMtvhDYhXOvvGEkaVT4cnObo2W82P5RmhJeqzIO_iYsVt6NxI1hz_rm0UFsyZ3yaJEmSZnXM038kJZfWJh0HcaKT3hzhAE5plgtwH8E6nrk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
من به ایران اعتماد ندارم. من آخرین کسی هستم که به ایران اعتماد می‌کند. آن‌ها مدام به من دروغ گفته‌اند.
ما در حال حاضر کنترل کامل تنگه هرمز را در اختیار داریم. آن‌ها کنترلی ندارند؛ ما کنترل کامل داریم. آنجا در اختیار ماست.
و شاید زمانی آن‌ها دست به کاری بزنند و آن‌وقت نابود خواهند شد. اما فعلاً در موقعیت بسیار خوبی قرار داریم.
ما با کشوری سروکار داریم که ۵۰ سال قلدرِ خاورمیانه بوده است. اگر دقیق‌تر حساب کنید، در واقع ۵۱ سال می‌شود، مگر نه؟ ما چهار سال بود که می‌گفتیم ۴۷ سال؛ و حالا دیگر آن‌ها قلدرِ خاورمیانه نیستند.
🔴
ترامپ درباره تغییر هواپیما در آنکارا:
این موضوع صرفاً به «سرویس مخفی» (تیم حفاظت) مربوط می‌شود. من فقط از تصمیم آن‌ها پیروی می‌کنم؛ بنابراین تابع نظر سرویس مخفی و ارتش هستم.
آن‌ها می‌خواستند که من با پروازی دیگر و هواپیمایی متفاوت سفر کنم ــ که از نظر ایمنی تفاوتی نداشت ــ اما چون خواستار انجام این کار بودند، من هم پذیرفتم. من هر چه آن‌ها بگویند را انجام می‌دهم.
گمان می‌کنم تهدیدی وجود داشت؛ البته من خیلی پیگیر جزئیات آن نشدم. من با تهدیدهای زیادی مواجه می‌شوم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69923" target="_blank">📅 09:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69922">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69922" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69921">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=i7iyDmh94i8o8XLMuGp_ShnFx3r4p1iAG1czI8ZJ3Fcb6jkFTOixxTI-vGrVkCS2sqsneHm8Yj73c7iB_4U6CuFWlo8xztWYF39FWxqwCNOAaX8U9kXQjdGyVq2-cvpDIdXwCDs3TTRfwbKPNp-1MOwVJphAul2cK3-AHDmOnfl_kaXF5CkOGQtY-aN80m5Icf5YDPbQ-FFS8BLMhEfxjt-Fpdu_iSDgrp42cbNhWJZl_y1_rOppBjIP_SC_thM0jJJHI6QzOwFjH6HA9wTMqwANQW1V41P6McdVge8_ZbMBI0gIhDqsadnbXz2gGPOjF2wGn4dI6Fa6KAh1yoKS8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=i7iyDmh94i8o8XLMuGp_ShnFx3r4p1iAG1czI8ZJ3Fcb6jkFTOixxTI-vGrVkCS2sqsneHm8Yj73c7iB_4U6CuFWlo8xztWYF39FWxqwCNOAaX8U9kXQjdGyVq2-cvpDIdXwCDs3TTRfwbKPNp-1MOwVJphAul2cK3-AHDmOnfl_kaXF5CkOGQtY-aN80m5Icf5YDPbQ-FFS8BLMhEfxjt-Fpdu_iSDgrp42cbNhWJZl_y1_rOppBjIP_SC_thM0jJJHI6QzOwFjH6HA9wTMqwANQW1V41P6McdVge8_ZbMBI0gIhDqsadnbXz2gGPOjF2wGn4dI6Fa6KAh1yoKS8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a20
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69921" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69919">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=pAhSsm9bm18VvsRyME66Np3vV_Tc1MaxX60Vm2tpv1OvkkQv0MflNmRn_GFii9LG1247ewF9XJJM2v7vG_TZhpIJCrZuFTcH9rv_9NCOhoy4tQ-BOy03bN3kzobwqbMeqnO23d5Ktyb5zMD_wTRpmLasgKLhTSNQg5iZsKNUKRTovIUB2SJ5VyDhp0YfEF4W7Dib0WmYx9G8fEYTHMOB-Nzc4fIUaIj-AOVg_qhYHyOIa3B0Hr82mE7D6i6vVeyYzvdMo8uVfQM353ihfOWlx-jRkImxUeuLUxtH_hIyS18k3iCgvgaGUQJe4PjEiN9bUV-FWHB_XCvzFulHvvQRfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=pAhSsm9bm18VvsRyME66Np3vV_Tc1MaxX60Vm2tpv1OvkkQv0MflNmRn_GFii9LG1247ewF9XJJM2v7vG_TZhpIJCrZuFTcH9rv_9NCOhoy4tQ-BOy03bN3kzobwqbMeqnO23d5Ktyb5zMD_wTRpmLasgKLhTSNQg5iZsKNUKRTovIUB2SJ5VyDhp0YfEF4W7Dib0WmYx9G8fEYTHMOB-Nzc4fIUaIj-AOVg_qhYHyOIa3B0Hr82mE7D6i6vVeyYzvdMo8uVfQM353ihfOWlx-jRkImxUeuLUxtH_hIyS18k3iCgvgaGUQJe4PjEiN9bUV-FWHB_XCvzFulHvvQRfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی یک مخزن در اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69919" target="_blank">📅 01:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69918">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=n4EEiq9CoPvM4Hr0rKSFL4NnzQiS9EbTzLPiK-JhaXBsejoAHLUFabFV4kXHI38Kw6_lh_bZZDHXAMwzLDP66uKuforjNJdC4FXpO7GaEHcODc9iJlCotdvrzevTtPqC70BvkI02Ym9NwLxZ1mbpXU5sQ5oNylpgDVj5Z-BdOyiKVozYuMncZ_zBZ1Nj2oyqWR8TZnkpWqIxZ_PiY_5pmXzNOPwuS0HClnNm1WQQBuHbZ7Zctt6g1c5QbNZJ8ZMOtblYL6QRnC98Bbp-AF5S75CJ7Inf2TItBBCmED5mxReuv2izne0i5_JvEluCq4Q7fAw9tq6w60w9HCj9cFsdhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=n4EEiq9CoPvM4Hr0rKSFL4NnzQiS9EbTzLPiK-JhaXBsejoAHLUFabFV4kXHI38Kw6_lh_bZZDHXAMwzLDP66uKuforjNJdC4FXpO7GaEHcODc9iJlCotdvrzevTtPqC70BvkI02Ym9NwLxZ1mbpXU5sQ5oNylpgDVj5Z-BdOyiKVozYuMncZ_zBZ1Nj2oyqWR8TZnkpWqIxZ_PiY_5pmXzNOPwuS0HClnNm1WQQBuHbZ7Zctt6g1c5QbNZJ8ZMOtblYL6QRnC98Bbp-AF5S75CJ7Inf2TItBBCmED5mxReuv2izne0i5_JvEluCq4Q7fAw9tq6w60w9HCj9cFsdhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اولین ویدیو منتشر شده از عروسی رونالدو و جورجینا:
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69918" target="_blank">📅 01:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69917">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=RjGQLk8qno1kwQ2BFlKmr3OPPJRGJp3b0243rP1sArIn9IVcX02NFU3D-Z7G3KB0gBfDLhlrg-GionDTEPbc1b_asY1djBRZRSRLaLsos-Ua9tJBZkj9sGtUTx8fRsykzxyDMtTsAoeDH5qW5VcTaHnIff-5SrTpOS5_dTwsloiw5VPik6zTRYdHD6cMr4r7APvR2xo7LVPmkL8b97G8_sc7RXZuZQRxQzSOWDHtHX3zaMCdNfszBrNyjizTVg2zQHui-IDQykHOmbmmcL4P2hsDwGt4FofwNgL4Q-LSCDp5cwesPXvnYwD_temxIHXJAranm4urXyRm62Qtfz0t-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=RjGQLk8qno1kwQ2BFlKmr3OPPJRGJp3b0243rP1sArIn9IVcX02NFU3D-Z7G3KB0gBfDLhlrg-GionDTEPbc1b_asY1djBRZRSRLaLsos-Ua9tJBZkj9sGtUTx8fRsykzxyDMtTsAoeDH5qW5VcTaHnIff-5SrTpOS5_dTwsloiw5VPik6zTRYdHD6cMr4r7APvR2xo7LVPmkL8b97G8_sc7RXZuZQRxQzSOWDHtHX3zaMCdNfszBrNyjizTVg2zQHui-IDQykHOmbmmcL4P2hsDwGt4FofwNgL4Q-LSCDp5cwesPXvnYwD_temxIHXJAranm4urXyRm62Qtfz0t-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر محمدرضاشاه پهلوی درباره نفوذ لابی یهود در آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69917" target="_blank">📅 00:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69916">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGBdgJhd27FwTxilA2bJ9GOQEnZMgaxOQpe0gteuvGKXL4Um4tTMicsE374UBTXGHeeDOOqMh3o1MFYLdYna1TgJv8iiO3iWByiGlDCr2O44qL0yVC-b5GoCwzQxVLEuO1yTkRBdmS0G71XTgPFXwfPgLD3_Gys5J0CSitBlZcWxj3awi57kACFsYizkEFPVwCRK5y_bZCRPHt8jNS9_GSIZd2y7rNcafnlcP2RYrWYF3wC7f0iYkPJ8Qg-UAW8cNmxVRUqV0nbnBRmneMiti6DMEdU-B1gVcvi37MjAygAG2LaYcSGsazyD4D0cir55j0ZZXKVryWw4TPtK2pZJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونالدو و بانو جورجینا رسماً ازدواج کردن.
رونالدو هم گردن گرفت بالاخره، دیگه وقتشه تو هم گردن بگیری
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69916" target="_blank">📅 23:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69915">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=sT6oflNvm4Uudt2r0qHmmwEGpMYdRwufC84_DZu7X3s6dYvtdJcz-jPhZ8Za7-r2yGe39vcZvJcZsONxnBHQqgNO1ucUorUBULB3N8xm7SoW62SVaFWXZ8DCNntn7GtIeEyvgTL9mowCI--VMDPkKv0Q15pSTj-vZYRSGg5l-YbF2RZYtuKPIkFsRaemEqDs5QXvBHKqP9QMOva_MeY7_aKZGK8_g9ccwPwQff6LJZOMb7bmeGOppfIuxqadvguafKDD3iWHvDUjL8veKfcN3X4L6b2uxK0763YYCZLtd-Qhj6ur8AfZURZNOT4zz7bNFS8Rfy465JZTM3LznbhSsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=sT6oflNvm4Uudt2r0qHmmwEGpMYdRwufC84_DZu7X3s6dYvtdJcz-jPhZ8Za7-r2yGe39vcZvJcZsONxnBHQqgNO1ucUorUBULB3N8xm7SoW62SVaFWXZ8DCNntn7GtIeEyvgTL9mowCI--VMDPkKv0Q15pSTj-vZYRSGg5l-YbF2RZYtuKPIkFsRaemEqDs5QXvBHKqP9QMOva_MeY7_aKZGK8_g9ccwPwQff6LJZOMb7bmeGOppfIuxqadvguafKDD3iWHvDUjL8veKfcN3X4L6b2uxK0763YYCZLtd-Qhj6ur8AfZURZNOT4zz7bNFS8Rfy465JZTM3LznbhSsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
روحانی:
صدام پس از کویت به دنبال عربستان و امارات بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69915" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69914">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🇺🇸
سنتکام اعلام کرد نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۵۵ کشتی تجاری را بازگرداندند، ۳ کشتی را غیرفعال کردند و برای اطمینان از رعایت مقررات، ۲ کشتی را بازرسی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69914" target="_blank">📅 22:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69913">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWgawQF2wv1Wrj-06pyrJsZQZ8ojoIaAN1jPbHQIu1nABAS-rBWeMGnkAoGPiC7GNu5hjWidL3Vndc2R8zH09su28mZSzAVik0ySIOiUHevEABYA6d4G6APwAc4HetFMQ_Rgv7X1-c-2kI1ubGIPVqf2kENnBnSzR4ds4zKzZ-c_9vhVPEEQeHceY_mm77xoprNuJ-XZPAs99NORcR5vBS0KgSyD1z1F-rRiAAtkFQqlyoGllX9wrZSuf7d9hXs09dsuJH6TYT9rnW54cOP-eYp9T7Bqsr9GBYmw5sqftJDS-vn_sA0tKReh3u5hTDUFEghlxmqFB_FYnTlcOH_D5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
وال استریت ژورنال:اسرائیل دولت ترامپ را در جریان اطلاعاتی قرار داد که نشان می‌داد توطئه‌ای احتمالی برای هدف قرار دادن هواپیمای ریاست جمهوری با موشک‌های زمین به هوای دوش‌پرتاب وجود دارد.
مقامات امنیتی ایالات متحده متعاقباً پس از اجلاس ناتو، رئیس جمهور ترامپ را با استفاده از یک کامیون پذیرایی فرودگاهی در آنکارا به یک هواپیمای نظامی جداگانه منتقل کردند، در حالی که مارکو روبیو، وزیر امور خارجه، دیگر مقامات ارشد و خبرنگاران به عنوان بخشی از یک عملیات فریب در هواپیمای ریاست جمهوری باقی ماندند.
در نهایت هیچ موشکی شلیک نشد و هنوز مشخص نیست که تهدید گزارش شده چقدر معتبر بوده است. این عملیات اولین باری بود که چنین اقدام فریب‌آمیزی در دوران ریاست جمهوری ترامپ استفاده می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69913" target="_blank">📅 22:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69912">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=iuwZmfjFUSYn4gk_2XU_xlv8Me2IJZSaW6QHuxHxFNaDt-p-py-u0245Haorr4UCKmMIWd7m9wPOBEirzF8LPIQfYHl7b9VgyTzJTw3tIgvFNKOBxinVEjma5EkPZm_oUDk3jcb_42mQpqtuXNaSwoxnYuj8k03__xUKUMMzsg4tuzydz7r_u4vbVr6W2b_QbnHP0Nmx0r7gQVdgSiKkuIHDlGGERKQKL3xUOdr7MVoW24b9mVzBRuobkQ2Pas1yEWDeeT8aoy8DV2fCwtFtVs0unblMWhucE8gj8dYAC3WFQ3J3o61rFTMYLC3m78v71JLHN4noczLKtKbOqqxUplRAwmyH3oGf_hhgJ1bc8oqecxSjBqwaKESO_YO5ifpSBkji8VHc3jPhleraljTUEO9gG_PYdcPHXT2Ri7bCRx3roaUthSgtrVTCYOO1c_gDOsq-G6DIcFpZYdS-RKKidooCNG6Z3Rb1GSHp3pyfRNAk79sSiGG8C-iLv2nlp25xmfx9sIttTF-p5fvZvuw5zkO6pCjJfeqveFC-eGtrgxXFiGIt_2ap42bP1U0GqaSXUrzcjTwYMXsGolUFpk_doLqYWBXHOIqs_6V_nKYUA26xo83G2bwtqngcsnhYNRycXw0jp086dLD4_ojL89QlkvPfM5qP20vCPb3howGw0-M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=iuwZmfjFUSYn4gk_2XU_xlv8Me2IJZSaW6QHuxHxFNaDt-p-py-u0245Haorr4UCKmMIWd7m9wPOBEirzF8LPIQfYHl7b9VgyTzJTw3tIgvFNKOBxinVEjma5EkPZm_oUDk3jcb_42mQpqtuXNaSwoxnYuj8k03__xUKUMMzsg4tuzydz7r_u4vbVr6W2b_QbnHP0Nmx0r7gQVdgSiKkuIHDlGGERKQKL3xUOdr7MVoW24b9mVzBRuobkQ2Pas1yEWDeeT8aoy8DV2fCwtFtVs0unblMWhucE8gj8dYAC3WFQ3J3o61rFTMYLC3m78v71JLHN4noczLKtKbOqqxUplRAwmyH3oGf_hhgJ1bc8oqecxSjBqwaKESO_YO5ifpSBkji8VHc3jPhleraljTUEO9gG_PYdcPHXT2Ri7bCRx3roaUthSgtrVTCYOO1c_gDOsq-G6DIcFpZYdS-RKKidooCNG6Z3Rb1GSHp3pyfRNAk79sSiGG8C-iLv2nlp25xmfx9sIttTF-p5fvZvuw5zkO6pCjJfeqveFC-eGtrgxXFiGIt_2ap42bP1U0GqaSXUrzcjTwYMXsGolUFpk_doLqYWBXHOIqs_6V_nKYUA26xo83G2bwtqngcsnhYNRycXw0jp086dLD4_ojL89QlkvPfM5qP20vCPb3howGw0-M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
پرواز بالگرد آپاچی۶۴ آمریکایی در نزدیکی قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69912" target="_blank">📅 21:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69908">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uIdeGzC2CIL2yaPHR4xOsW4ngxGusiagXGHoMjDbtubH-K96BTe8oCBBTLkWc43l1WrW2J0JU_F8ANcCJfeSoeLPPIg9QoQ5glOHNLNfzh1L57hsyxePBtDOZK5i51SZYtXjweuiQAq7YHDWzmVQ-AMfPy1r0SXyOrEk-StlKgr4udmi6mn-By-4GypItqc45MewUNJzotYNyoMNvVvRtpTcGofd5vxcXwLXiOh9UgAJO1-6rj4nLzeZdbN9Oap_wVNbubOjpqFoXn9dJlKwZHgZF3ub3KYPrNo8U9D2WMtEnsCVySByV24hOet82zIqQWY9zgaZTs0HbYGuLEW2ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TUbBLKknuCLw3dWLoxtS0Qju49pdNvw3KZqbZiF5BApQcIScUDUcR8XbgtZMiGAV8B0NU57Z4lmeW8OUsltR0qBiXFpZTyMTN09vyYJ285gx-qc1yYO8owgjuke7CTpBzSp8ofvNm3oxuza-leOJJJPLwHsZ3eRM6XiJ7b_cWdWbBLrhjTa481-tl_S22N9-RiPkN_Qp3DN0Y4ow8s-4_GFpbjoVWQfSmR_KjS7K86YCKyDyK-21HXPo10gM9WD6se99LF-_-KVKsMik8IWSbAkBruYws6oF-B90JdnCcM5Nzu1005KTZs3CYpStG9C8HA98OpluKmK-JBFkTdIFrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rowASBnVklpn53f5UtwdFIpT62uAqlT9TQ0CMdS0ZKPMVPDZzyqC0GNGWyKlUiYad0PdDG_jwNYbYXhtuyHuwA9p8aNZ4oxJfDtdJrRBsG2Gp5nEkxtLsekHCBc9OgeoFa7wfw1Z1LKkhUwhYSz0ruxZIQmccFj4XQL3jfdCSzjEY2i_1jogUs81aN5o92OOBPKMM-nYxEi6xGXRqCD8AAZvPakvCuGQZ5SSw__QXoVOJC_myVdTp8Vg9IOE512CIA43wgmmNq6lXb9PzbhgbaagQ9P1ZdSj0edZUoVEuXSfVoVN2QMhMvlPYliPyL3YfkxSkKCGqAELfCHHxMSeHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbbe5c4282.mp4?token=TKopMOlv-kVLPVAQwgvLqx0oXoqxCxEhuoq-Hp9HB4vLqZnVr2cZDaPULMxUJec6owaHiGBcncaAwvlEvr2AgC4747lAZ_gf8t6yooflAH8jyQl7L8shZYEFRxWizLCgzpZB5fl7SdOrj0o7ak6JveCNcr3IvCE__PPy5GHtKeXC0q2sl-juVOkhk17N00mvYM1uj-JbjRZBInMYLb4KObhpkSaKERjb6TxPLOeDFIDMm5xob9zIgFuZFSSPsgXTo4b8OgcyAmO8W6dRi2ui5pjVfMWsTyqaiLqX-Leh13sIOsTsvzpBOx_Tu3dRpDmqUhzW86cYhRQt0vWFh3oQJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbbe5c4282.mp4?token=TKopMOlv-kVLPVAQwgvLqx0oXoqxCxEhuoq-Hp9HB4vLqZnVr2cZDaPULMxUJec6owaHiGBcncaAwvlEvr2AgC4747lAZ_gf8t6yooflAH8jyQl7L8shZYEFRxWizLCgzpZB5fl7SdOrj0o7ak6JveCNcr3IvCE__PPy5GHtKeXC0q2sl-juVOkhk17N00mvYM1uj-JbjRZBInMYLb4KObhpkSaKERjb6TxPLOeDFIDMm5xob9zIgFuZFSSPsgXTo4b8OgcyAmO8W6dRi2ui5pjVfMWsTyqaiLqX-Leh13sIOsTsvzpBOx_Tu3dRpDmqUhzW86cYhRQt0vWFh3oQJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک، از بزرگترین خواننده‌های دنیا؛  با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]  وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد  @News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69908" target="_blank">📅 20:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69907">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=TgCpiNjiXLP-I7qNU5A49TZlWgvXrRJDwMwRzFKf4uzbiReuYwtwilUZS_A37jwJgmmli-JbDxyVpORimwqrSErkLr3UUiGeOl8U2ZMG2QmZS5_fUQuCVm4uMWiPxtDgzf8zb7ukQvI9EQqMrPSlBMM2E4NjLngJyKBFLSHPwGSD0-VMyR-58Mwj0dBF6UmHVDyaLa-n1HjlgpVuhjMfjkbkK7P9hZkAN0OQiKuvD4gPMyEC-FALloXtoM-39KiAQFkFMlxmE_1C07lHSZ7BUdjuSE6JV1rP3391S2I1cm9HJCQzg6LlaNqFtCSqK23rIl1_vJtyVCAE6hT_GpR1lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=TgCpiNjiXLP-I7qNU5A49TZlWgvXrRJDwMwRzFKf4uzbiReuYwtwilUZS_A37jwJgmmli-JbDxyVpORimwqrSErkLr3UUiGeOl8U2ZMG2QmZS5_fUQuCVm4uMWiPxtDgzf8zb7ukQvI9EQqMrPSlBMM2E4NjLngJyKBFLSHPwGSD0-VMyR-58Mwj0dBF6UmHVDyaLa-n1HjlgpVuhjMfjkbkK7P9hZkAN0OQiKuvD4gPMyEC-FALloXtoM-39KiAQFkFMlxmE_1C07lHSZ7BUdjuSE6JV1rP3391S2I1cm9HJCQzg6LlaNqFtCSqK23rIl1_vJtyVCAE6hT_GpR1lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
رامین رضاییان:ما خودمون از عمد به بلژیک گل نزدیم و تیم بلژیکو نبردیم.
🔴
چرا؟دلیلش:
جلوی بلژیک شما دیدید مهدی طارمی یکاری کرد تیمه ده نفره بشه.
مهدی بخاطر تیم به بلژیک گل نزد.
من باهاش صحبت کردم داداش چرا نزدی گفت داداش اگه گلو میزدیم فشار وحشتناک میاورن و جبران میکردن، حقم داشت مهدی
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69907" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69906">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🇮🇷
فیلد مارشال محسن رضایی دبیر عالی شورای امنیت ملی:
آمریکا باید جنگ رو پایان بده و خسارات رو بپردازه.
به هیچ وجه کوتاه نخواهیم آمد.
تمامی جنگ ها باید در کل جبهه مقاومت پایان یابد چون شرط اصلیه.
شروط دیگر را نیز از طریق میانجی ها گفتیم به اونا ک باید بهش عمل بکنن.
توافق با عمان ربطی به باز شدن تنگه هرمز نداره.
پول های بلوکه شده باید آزاد بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69906" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69905">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/69905" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69904">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oChDsTQFLABEzvClFAhfK7JaL2kPcn7udzujJfDhSjLunozEF-Ph3kLVOC_4-1w6r0n0y6iPexUTTi_YwmwZttKq1kX4LCQl463AqGGb7Xhq6hGHzGz-KqAuUJ0KLVXcB2WVls3Zz0uttySwvU2FGwhAEDQ2z294E8kFHtn8pAL2Av_CI7YD1xJ9X4ASq5YZUXJhBVUp9icbzVnpB_OGoOspqKX5U3cHssqGoEF0GuMOTjl-awknetSy4oJEZiYcDZhIoRE8FUdeWqYMsmxRqWvHh1-FF63cGgFXv87ZNHSVq6jjOukOYTGGBFmIqP_cyBkICqmkBSDAroqnNtRsUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/69904" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69903">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=aglInKe5fWJV789d5YpnuVEFwEsEnV_6hGRW8gcuTfFpQsPUMUOjMXUTa0DmqF1mJn9HHA4xob02IVepgJV5q8QI4mb0XhN-l7QW6HwxqZOMuAoUhsOW6rhgdx8r2dpxEnqqqUoHprfltpA2IO4MPbPDEJ4n8b8SZNAMNlzriVC6xjJCe8e3ECeq9OrWnBSTsdtw4zdzdS_UxTNz1p2isRw_Z3hoGy8dJ21t7xlw-JPG01MdTWJ1oCu7XXz1PFgFUXRBAjqj9O9HA0N3KpwxKKwDBjqSeLz_e_lFwlqV7ffPmpKU6aJXledv23H0TwjwMO-VLOxqNVuCZqLUOM8K4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=aglInKe5fWJV789d5YpnuVEFwEsEnV_6hGRW8gcuTfFpQsPUMUOjMXUTa0DmqF1mJn9HHA4xob02IVepgJV5q8QI4mb0XhN-l7QW6HwxqZOMuAoUhsOW6rhgdx8r2dpxEnqqqUoHprfltpA2IO4MPbPDEJ4n8b8SZNAMNlzriVC6xjJCe8e3ECeq9OrWnBSTsdtw4zdzdS_UxTNz1p2isRw_Z3hoGy8dJ21t7xlw-JPG01MdTWJ1oCu7XXz1PFgFUXRBAjqj9O9HA0N3KpwxKKwDBjqSeLz_e_lFwlqV7ffPmpKU6aJXledv23H0TwjwMO-VLOxqNVuCZqLUOM8K4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
روایت تلخ یه فرد نابینا:
اینکه من نابینام به عقیده پدرم کارمایی هست که دارم بخاطر کاراهای اون پس میدم.
پدرم وقتی جوون بود نابیناهارو مسخره میکرد و بهشون میخندید.
مثلا پدرم بهشون میگفت بیاید جلو بیاید جلو و وقتی میومدن میفتادن تو چاه و پدرم مثل خر بهشون میخندید.
پدرم بهم گفت من این کارارو وقتی جوون بودم انجام میدادم.بعدا وقتی تو دنیا اومدی دیدم نابینا شدی و این دلیلش کارمایی هست که من باید پس بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69903" target="_blank">📅 19:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69902">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=JbgBwYC9ehq9ZYw1opfwsKjuefEtfBXV-S91EaBMsRbCVDgMqdAAx__jjFLqNGXPa2Ucr7w0sfnP4sNyS37Wa8eaLmcWnZd0gigFOh4aDSMgMfbu28aIV1S_4AEP5-MRd76eg8jBbdX7hEkhEW7aPumchMrpXJMRjMhToZ-fidNRAvVIrMiryYMMT2zPExWa5KFXrKJVEAr7SUwCZm_4Z6Lr1JeK_d5MJGeHFCyCK8948ivwxpMnX3ErfKw8ZN9Mwmy6SgAftPR4xRKI4TTKM4dpB1tf05HQEXknm3Yhrs1T62UlWuvzRiFdTahYpVSKUs9eeCH7t6cPpEFy80jB92nvq-AOCflRcdpsac9Xe9rhpm8-hXXIS4iPUurvvtpuktyYiQ36Ex9ypZ8BDtIFGNfCfy4dQCoL5DGncUizxXtLeKqJ8SrofzuwB9vbI1p_J7R626K-Op-T1S2PqBPytFkQt0ffzPYIPXc61848_Ny1fB2u3Bnl_l2efc71iJkEItN9YwwLt0rLN4kyTOMfR2pr9fxx_8pkhQysa3PVBUpNykHHrlUsiFMJD-dRLqliof17vhhFhoVaiIobcuEyIrIhlOlanXIX5rZuVfFfETFyKUhqm_p1aG_X__A5XIBlKyoB7rFbuF8HIIf1LVrJRnbti7yH0UZJ8ByORrsFbYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=JbgBwYC9ehq9ZYw1opfwsKjuefEtfBXV-S91EaBMsRbCVDgMqdAAx__jjFLqNGXPa2Ucr7w0sfnP4sNyS37Wa8eaLmcWnZd0gigFOh4aDSMgMfbu28aIV1S_4AEP5-MRd76eg8jBbdX7hEkhEW7aPumchMrpXJMRjMhToZ-fidNRAvVIrMiryYMMT2zPExWa5KFXrKJVEAr7SUwCZm_4Z6Lr1JeK_d5MJGeHFCyCK8948ivwxpMnX3ErfKw8ZN9Mwmy6SgAftPR4xRKI4TTKM4dpB1tf05HQEXknm3Yhrs1T62UlWuvzRiFdTahYpVSKUs9eeCH7t6cPpEFy80jB92nvq-AOCflRcdpsac9Xe9rhpm8-hXXIS4iPUurvvtpuktyYiQ36Ex9ypZ8BDtIFGNfCfy4dQCoL5DGncUizxXtLeKqJ8SrofzuwB9vbI1p_J7R626K-Op-T1S2PqBPytFkQt0ffzPYIPXc61848_Ny1fB2u3Bnl_l2efc71iJkEItN9YwwLt0rLN4kyTOMfR2pr9fxx_8pkhQysa3PVBUpNykHHrlUsiFMJD-dRLqliof17vhhFhoVaiIobcuEyIrIhlOlanXIX5rZuVfFfETFyKUhqm_p1aG_X__A5XIBlKyoB7rFbuF8HIIf1LVrJRnbti7yH0UZJ8ByORrsFbYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو ای از لحظه حمله آمریکا به پل B1 کرج:
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69902" target="_blank">📅 19:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69901">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
🇺🇸
پرزیدنت ترامپ:از شیوه مذاکراتی ایران ناامیدیم.
ایرانی‌ها بازی فریبکارانه‌ای با ما در پیش گرفته‌اند: در اتاق‌های مذاکره موافقت می‌کنند، اما در رسانه‌ها [توافق‌ها را] رد می‌کنند.
ما از هیچ کمبودی در ذخایر موشکی رنج نمی‌بریم.
ما می‌توانیم با نیرویی عظیم به ایران ضربه بزنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69901" target="_blank">📅 18:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69900">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=WSpNfABydgLKIDgC56xJQL7pax2WKQ4WtjUJbZkh9X_2S8as2qMOAo6rpTthMp53qQ9aj_fwfH3pAi5K50MvJssccU3Hr6hj2VLt9czpv51K9whPf2T06AQ35wghOY2Fqu4jU-ZObl5fMAYi3E6YR0Wq4tV0gSl8VXKmSYIS6XQMefKzsuEETSQOJIUbLlR0_Qkd9EZ2GhGfOxi7SPlozGbk5kkHmLsu5cztBl27gsdMa-JAhrAX-3vdrcoRDXY1qInAJ-3ZijsdmNJLITWK_7wOBpTnozU4MCe6XFWAC1mvrQmVfVlNnkjNh6tqpSr7IVeVU9ozetdRhQboN_0juHEiNiHJqloC3ohZ9VpQHjhmPsqj8V8sWuHqbOcfkpwZtOamZ8iLpEsmnoyuRR_FP2CDu4gM6Jt6MqKaPUnTbqpnGy7kSWoG99p5CuczOKAzO7PGKLz0HELg-Se0qxf3829zzjqduaHYQonwvGMIUoeQQJeQ7WJEU0sQiREoS_Vcb_MR3a3w2QNqBQ0zXwa5pU8MTNZbEDTgZhe9mlz9JQI5hkmAsZL_kEnSK30UNlfSMd7zbP_oGFFGC7JsQ7GqzC400pgcW2Ms_Gswrc7NySC-e2_Sd1HtnrNEWG7exzQEBoAkS9bSwuClkWZh30NfLjUuo-ImS70MS311MNFA1eo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=WSpNfABydgLKIDgC56xJQL7pax2WKQ4WtjUJbZkh9X_2S8as2qMOAo6rpTthMp53qQ9aj_fwfH3pAi5K50MvJssccU3Hr6hj2VLt9czpv51K9whPf2T06AQ35wghOY2Fqu4jU-ZObl5fMAYi3E6YR0Wq4tV0gSl8VXKmSYIS6XQMefKzsuEETSQOJIUbLlR0_Qkd9EZ2GhGfOxi7SPlozGbk5kkHmLsu5cztBl27gsdMa-JAhrAX-3vdrcoRDXY1qInAJ-3ZijsdmNJLITWK_7wOBpTnozU4MCe6XFWAC1mvrQmVfVlNnkjNh6tqpSr7IVeVU9ozetdRhQboN_0juHEiNiHJqloC3ohZ9VpQHjhmPsqj8V8sWuHqbOcfkpwZtOamZ8iLpEsmnoyuRR_FP2CDu4gM6Jt6MqKaPUnTbqpnGy7kSWoG99p5CuczOKAzO7PGKLz0HELg-Se0qxf3829zzjqduaHYQonwvGMIUoeQQJeQ7WJEU0sQiREoS_Vcb_MR3a3w2QNqBQ0zXwa5pU8MTNZbEDTgZhe9mlz9JQI5hkmAsZL_kEnSK30UNlfSMd7zbP_oGFFGC7JsQ7GqzC400pgcW2Ms_Gswrc7NySC-e2_Sd1HtnrNEWG7exzQEBoAkS9bSwuClkWZh30NfLjUuo-ImS70MS311MNFA1eo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رونمایی صداوسیما از «قوی‌ترین سیستم جاسوسی جهان»
تماس با پذیرش هتل عمان برای جاسوسی:
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69900" target="_blank">📅 18:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69899">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=l_btcotVq-5B0T7Lvlv2uiqe0ytzc65k1MxHGcWZbwvlwe7qXfCg7lXnXXcHAUwwf0QIgSmfh_Ytb99M2KQhG6t6NTPoUVS5RTHOrhRqrSOARsCPYD44JwCwkYzZeyTyw4eBPDgQIicHvRoxngVwuDSTQPF2i9jrYunChFsJ7yeehK1rdHE7NcUzWgx7Una6CYHxON3DfnUH_2-W8MMGk8ZG2gVQqIaJtGf_bKrsaLFn-sWLQW0TCzG6wupYqkWsJLsjkz34TKZWI4hjOFHDNJj9T9rREb8JS1vTRX8OyJ6OO-HCPgyluKNs-UmZ_0tAxFmUB4DjqC8Fp0JN-NLraA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=l_btcotVq-5B0T7Lvlv2uiqe0ytzc65k1MxHGcWZbwvlwe7qXfCg7lXnXXcHAUwwf0QIgSmfh_Ytb99M2KQhG6t6NTPoUVS5RTHOrhRqrSOARsCPYD44JwCwkYzZeyTyw4eBPDgQIicHvRoxngVwuDSTQPF2i9jrYunChFsJ7yeehK1rdHE7NcUzWgx7Una6CYHxON3DfnUH_2-W8MMGk8ZG2gVQqIaJtGf_bKrsaLFn-sWLQW0TCzG6wupYqkWsJLsjkz34TKZWI4hjOFHDNJj9T9rREb8JS1vTRX8OyJ6OO-HCPgyluKNs-UmZ_0tAxFmUB4DjqC8Fp0JN-NLraA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
مشاور قالیباف، مجید شاکری:
هیچ کس نمی‌تواند با ترامپ به توافقی برسد.
این تیم فعلی با هیچ کس به توافقی نرسیده است.
او هم با ما به توافقی نخواهد رسید.
همه فقط در تلاش هستند تا "تحمل کنند و صبر کنند" تا پایان این دوره.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69899" target="_blank">📅 18:10 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
