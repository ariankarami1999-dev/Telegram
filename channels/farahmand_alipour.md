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
<img src="https://cdn4.telesco.pe/file/bpEiaJBqZUMb9k_GwUxW30hxMdTYUpYZstdaxatDW5NJj0cLoVElwwY91W36SWLTiWH_b-t0OrANjJZcQcBeedh5Ah_J2UiiGAPmPu-pY01aw-f5rk52b1pl-VY5yaOhY1zb9ZPa5Mgdar66ZUQgWnsE_NkbtJMknNmVSw6KLXs844Aua_hDbtj6YXs8hrO-gcBAEyFE94FsX0NP1o2qF-bU9_dS_9G6aSjHvv4hBGVEDFIRZJTbREDTynZeiPc-BklLyvT_yOyiJNG-fZ4Y7n-2zoWm9_rhl5eLfGFgCDdu1y7IoWZuXyMVGqgAGGRo-o7Z-AqYY_GbbomeWAJzKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 18:37:34</div>
<hr>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UniU-uEYV0773F2efC4bfQJnDDp44MlbENld_-xi2zstdhLiwBrzAepqLIQMxW8lI5rZQW3AMcPuS-eYGRRuC7S9Eh20d9-ljfne6EqofLKSnqLW4ieykoI1fDaGKLtz8KCqU9vTsYz9xbdb5mZnUHNIHEOzykJzh0_5UmnT_06in3KLpSQ_7Ap7P2Vz-jfa0bZRZueBh8iWRrlD6okwHSU3yGKjq6_suCoVrHi18Sz4HPkg3Yi0Bu5-lTUUNzp0Nno8pEHjIO1HyVvu3RupNvwes083Ueb-iwkmy3J-FxU0x_FrFZxjDx9kNEx0Htec2xjDPzl2iLtzqanrreR7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=AG5EkUkCCI8xclPl9ny12A_28p9l0185u4ab_blvCGIZiDujcfhWmFqJwQw3ieiWgs4wBX7tTahaE4-KtNHXHP_x55tuofubLxQ7YSyzzCzvQsViKI06laFm49mH6iX_gX4UxxBaNpl_nEFm5En-SbhgNGuju2_PpxYYGMWnI0I9jDAKstEDn9ZlWg386jFN1O1QSK8AkT3gwV1v7NzGQCOZBKprX_yDrHRhTlraEmiqsfEkAM9MBgaYrzHZeZ5hIY2pjAgV_XmV0EjN-BUzHGlprJdQFSbhW-mYmHL3INgGceFYz8hRXVZ7tIuGZzgvO6hlFTWnE4AIQ5qv4jesJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=AG5EkUkCCI8xclPl9ny12A_28p9l0185u4ab_blvCGIZiDujcfhWmFqJwQw3ieiWgs4wBX7tTahaE4-KtNHXHP_x55tuofubLxQ7YSyzzCzvQsViKI06laFm49mH6iX_gX4UxxBaNpl_nEFm5En-SbhgNGuju2_PpxYYGMWnI0I9jDAKstEDn9ZlWg386jFN1O1QSK8AkT3gwV1v7NzGQCOZBKprX_yDrHRhTlraEmiqsfEkAM9MBgaYrzHZeZ5hIY2pjAgV_XmV0EjN-BUzHGlprJdQFSbhW-mYmHL3INgGceFYz8hRXVZ7tIuGZzgvO6hlFTWnE4AIQ5qv4jesJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=EVRLWKK1gxH4nmYi8WrYJtmetFEicLolDhhfT6yy2WnjKjFxnN72Huerk2L_yz793iWaaJpiH6iFrfMLd2P1iQWvo6st2s8EJJaYB4qtqpuyfZF0XaTS2XtZbs4dH12fPSA4kAFUguNw51E2adC6q2JGQUmm2cB3xcTzBGR7amN6IgWgAVsMTYeW0OWEW1AmaA41_0qDk9vobV4k2naQnI-X-u4E66lV_s7iTDkP-ump14tER0MVQ1mGmiHLJQtnJmyWiTr_zgp1VDa0DSsw9_PyKlllcQFWfRM0zY0D2px69kaGtUne0L3HlVHKc62Xr6Mpot1WdizWpCmgsh1cuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=EVRLWKK1gxH4nmYi8WrYJtmetFEicLolDhhfT6yy2WnjKjFxnN72Huerk2L_yz793iWaaJpiH6iFrfMLd2P1iQWvo6st2s8EJJaYB4qtqpuyfZF0XaTS2XtZbs4dH12fPSA4kAFUguNw51E2adC6q2JGQUmm2cB3xcTzBGR7amN6IgWgAVsMTYeW0OWEW1AmaA41_0qDk9vobV4k2naQnI-X-u4E66lV_s7iTDkP-ump14tER0MVQ1mGmiHLJQtnJmyWiTr_zgp1VDa0DSsw9_PyKlllcQFWfRM0zY0D2px69kaGtUne0L3HlVHKc62Xr6Mpot1WdizWpCmgsh1cuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=uquHqQzbEwhtkOxOt_uVeo-8FRNcxGLr9CmO9j2R79RY1fQhq5v8ENXuwhmMxfTqPCirNM8L3_B-MS4n_tZKdSHR3eLpk--4o1XLOmjJJfIU-p0jrSyvuySN2rO6Weigo6d8MqU_nKUKY2MBPrO5u4y6bAv_gsnJw3HswJmNnB1UFZ8fW_Kz7qc0QgMDsgXbU6cIRZGR1gfO6r6_WUPU1xPVpEx-Z8MfX1eImtHe3UezgbhRelLV-5JxIpKYIG0yypnZWZpCNefgSziqPWwdNcsOZmpSTEk8R3s_iiw59BOpWrfHM52f1V3QyubYGjQAKgqfSIGfKs_ZkCuD_R0k9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=uquHqQzbEwhtkOxOt_uVeo-8FRNcxGLr9CmO9j2R79RY1fQhq5v8ENXuwhmMxfTqPCirNM8L3_B-MS4n_tZKdSHR3eLpk--4o1XLOmjJJfIU-p0jrSyvuySN2rO6Weigo6d8MqU_nKUKY2MBPrO5u4y6bAv_gsnJw3HswJmNnB1UFZ8fW_Kz7qc0QgMDsgXbU6cIRZGR1gfO6r6_WUPU1xPVpEx-Z8MfX1eImtHe3UezgbhRelLV-5JxIpKYIG0yypnZWZpCNefgSziqPWwdNcsOZmpSTEk8R3s_iiw59BOpWrfHM52f1V3QyubYGjQAKgqfSIGfKs_ZkCuD_R0k9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOnvpxa3yMMXdMFzGbv7vNk5xdCTrkFF-pF-B691LL-njXx_zK48ITb0b7Wb4fpnecu_uxVscObgyoAiJf-gMEypbFAM9Noe1NPADZno3BHq9_wkY4OiJPXgSn_aOyXROQF--2wctSkrd7O8zoER_KhgMGBOlAodROTaCBJBW6TnZ5zRWX6Scv1fSaZchDASMkJZLjK--5YPTFJrTepEy6SYr8DlYOTmYNkMnGnhKGAod17RLdRFVFguvQyUEdJ2V8BdSb9QwNLSarYYITsO8EPyxhZlXS3ZwduwJHYLPUzR7zmyid4ARVcg5Mgf-FlsOKKPm2pLeTmIhtl5DWXB1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8ENc9FHMupRDworajGVK6jscJpi0uhlxQv95RXHr570s_3DSYqHRildrxUN4Q2VRdPHLGHkQ22RQ2TqbWEpqvZSvcw7qvIXTqD4yPK6tq6r9LaDZS2_pPpHi3dRD6do0wIALoZoM9cT_POnwzwP3Kq_4OdKheJ56FEYBWi3WcK8j8A4YbPn8FBeslffZE41mwgnrwzVjuCPjdepbwBwEJ2ZyXr5o1bnlt47ZTZK5qJ0TXpD5uQcciElkVYxSThYMZpas8h7Lc5dq_epY4VVB99NGxUpcJI2BcrlIlXD7frXWdcMJumDLEaq1kaAh69RcXOSJh2dnnE5Dx4eSlsRqQUE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8ENc9FHMupRDworajGVK6jscJpi0uhlxQv95RXHr570s_3DSYqHRildrxUN4Q2VRdPHLGHkQ22RQ2TqbWEpqvZSvcw7qvIXTqD4yPK6tq6r9LaDZS2_pPpHi3dRD6do0wIALoZoM9cT_POnwzwP3Kq_4OdKheJ56FEYBWi3WcK8j8A4YbPn8FBeslffZE41mwgnrwzVjuCPjdepbwBwEJ2ZyXr5o1bnlt47ZTZK5qJ0TXpD5uQcciElkVYxSThYMZpas8h7Lc5dq_epY4VVB99NGxUpcJI2BcrlIlXD7frXWdcMJumDLEaq1kaAh69RcXOSJh2dnnE5Dx4eSlsRqQUE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=FX0--yIVzTty_e0CyZEfIqykjL7Luki0bnLnOnZuOdDq_S7E-_JmndKaanId45ULsd8s_PdSpkFPN2-cwDHXvH2BvlO-_y7uJ0Ie1CU0gl4ko4vGZPjM06qchSfFvXngAZVIPCF_XD3CdgQIrhOyqrU2ebkqyZRRWJc0xnGzDKJPI9nBBcZUoh1hZZoI37sPbENDBxIl_sAA2WGr17MhOQYC-X-YaMsyAXXibupy9_4fDcHPDnRZMJqGE8Z9_DUiFfl9ufh5UvWNz3qY9PY9Z5ofaFeaTuZ95SY60sfq956mXkgpWV0h9jX17AZvHNiG5cSOimd60kxNAdohPu6dcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=FX0--yIVzTty_e0CyZEfIqykjL7Luki0bnLnOnZuOdDq_S7E-_JmndKaanId45ULsd8s_PdSpkFPN2-cwDHXvH2BvlO-_y7uJ0Ie1CU0gl4ko4vGZPjM06qchSfFvXngAZVIPCF_XD3CdgQIrhOyqrU2ebkqyZRRWJc0xnGzDKJPI9nBBcZUoh1hZZoI37sPbENDBxIl_sAA2WGr17MhOQYC-X-YaMsyAXXibupy9_4fDcHPDnRZMJqGE8Z9_DUiFfl9ufh5UvWNz3qY9PY9Z5ofaFeaTuZ95SY60sfq956mXkgpWV0h9jX17AZvHNiG5cSOimd60kxNAdohPu6dcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUIFPTt3kZkRq5RjumETcNKCTkK33JcQlyruONT3qksb7sHWHt-rf8SsRd81OSHIT1ZXjmrP_HWPWOjma9VwMSb13jlamV68KYwjtFRoVwXSI_yrPWYesdZ9-4w-vhE8aZZ4yf_G0Rg-2zzUbYEchqVUFE8AuJ0xwTK3d_YsEIu28CsoESl8RYBlxL21BuFJ_Th9JaBp2tedq4ApJGtCnLugWehFVGY9fjKZEQJxSz5rmMbzzNeNQXXspOuxTN2yttg879Y4OCjCihgQXlXywaRtNMYRz_xuVHvAfN3jgR9VFF-CKcapgTeDsVMBlcZajPO1jnKWdW5V-GLKbVUhJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=ESnN8mrtxHsd6gN_CB1HZ8Cg3D2ikeXJRfEAGBP9YYp7wZlfUsdMXse38-98nwAwoUfCIcz2CrPVzyfbUbCkAkRkJoilTIfzAfY2iSxjRimYq_D3lhYhPdeNZxMPqjcU3ZHMiRwcstQnMo1inKfB8ueJzPIVLr8ftmViEDhfzhYPenLbEkvSzM-o_AcYPLAKqFXaM1WMVJ_NBwpMiuwomOHaNu24FLtsqRWPqZw-WVDBugGOp5E1nEpEo0Il8Dq4IAA8h5ag93vuie5rjgM29-BkPIozDZI8TDOI6klJhJuRlYKfFnkrjK7Ll8DePgIf7veaKx-3IS2rJ14YRabcDYGbVVgMVYP6XljUsuzobgWcUp78VHP2c4AJAwF3XheGM-36mQtGJBfhd-yefF10NyZhbZ4OFG_WlxxBSZocoNMxOLp5J-W3JuSyNzv7jwefQ0sVyjkByrnvf0EvP-s2VMisdAKk0SrzGEBgyBJAPkpbMAaEHyHjl1oSOUuCK38IqhN3eJOzoqHZOAU6SmJwEAWoTlmzPgQf9XKFRCw0v_wp2H0dVByRCM_8-BNnr4QKuAqHbHE_dfsMW7qP1jbMYK4g-pbsfMYbVd1HjP90vDVcU5LdMaRn6tb3QUN4tP7hUhvrHKaRx-GDSLN5npm7UD3TU74vbVPQ58qShkE5uVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=ESnN8mrtxHsd6gN_CB1HZ8Cg3D2ikeXJRfEAGBP9YYp7wZlfUsdMXse38-98nwAwoUfCIcz2CrPVzyfbUbCkAkRkJoilTIfzAfY2iSxjRimYq_D3lhYhPdeNZxMPqjcU3ZHMiRwcstQnMo1inKfB8ueJzPIVLr8ftmViEDhfzhYPenLbEkvSzM-o_AcYPLAKqFXaM1WMVJ_NBwpMiuwomOHaNu24FLtsqRWPqZw-WVDBugGOp5E1nEpEo0Il8Dq4IAA8h5ag93vuie5rjgM29-BkPIozDZI8TDOI6klJhJuRlYKfFnkrjK7Ll8DePgIf7veaKx-3IS2rJ14YRabcDYGbVVgMVYP6XljUsuzobgWcUp78VHP2c4AJAwF3XheGM-36mQtGJBfhd-yefF10NyZhbZ4OFG_WlxxBSZocoNMxOLp5J-W3JuSyNzv7jwefQ0sVyjkByrnvf0EvP-s2VMisdAKk0SrzGEBgyBJAPkpbMAaEHyHjl1oSOUuCK38IqhN3eJOzoqHZOAU6SmJwEAWoTlmzPgQf9XKFRCw0v_wp2H0dVByRCM_8-BNnr4QKuAqHbHE_dfsMW7qP1jbMYK4g-pbsfMYbVd1HjP90vDVcU5LdMaRn6tb3QUN4tP7hUhvrHKaRx-GDSLN5npm7UD3TU74vbVPQ58qShkE5uVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qU1e212cd_QEG-t8f2VCwgrFuAVeXGmecHuAyhgGtYa_7RinljYpMNqf2UtHx44GEYofxI8L004yhiLhzEZE9FqkKuyURauv4Xni7m6k3jfEnbFCTuRcWwch0Nreastdaa_9BDqIi0bcN_wJAnUXM2u6uUmBHg_UwHwSrkoe1VVW2qQxhFR3yCtu-F_hQH1P5WTQKNy4ceGOOsZumD6GcnCfPR27xEKDGTV832SWgS84GaWsGNhFNcvF7kw1L6TU9YVxAPzGrF4JV2OlzYV3TRjjAx5WnVo65whnkMi8XzfgJ3bGyWDgP4Zw4aOLSMd7t2ZfPt7g2aVsy5BomE_52A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=rF_PUfJyimf-q0CBMHTzXxIQSjJBwdPMdtnBgDDz1TOQUVZYfsole7NNTQe45kZ4hK-dXe0K4CibYDIOJ9Aj1vhRFKszDVBNflN_s4e0YT-Hf4VrHg1TeAXXilwA0C7AboFeHs8XzDHIdHpVgYW4ET0tS2p5fc9uwa9F01jJKix2T6bRQQ68ly57_6oBirK7_jbCWnf0_8DhIgx0B56m9DeoW08Ss1Fs0H1cgcnPGTdKpEYvv4xJ_-_9hB2Npqxo9PcyKqDj-0TMrIJrNUOZYmnUsfCFVtSuZoqBdrx4WSWZ8xSMY1gB2cfTe4VBgy_zePNA4mAvEGB2fDNnIXeASw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=rF_PUfJyimf-q0CBMHTzXxIQSjJBwdPMdtnBgDDz1TOQUVZYfsole7NNTQe45kZ4hK-dXe0K4CibYDIOJ9Aj1vhRFKszDVBNflN_s4e0YT-Hf4VrHg1TeAXXilwA0C7AboFeHs8XzDHIdHpVgYW4ET0tS2p5fc9uwa9F01jJKix2T6bRQQ68ly57_6oBirK7_jbCWnf0_8DhIgx0B56m9DeoW08Ss1Fs0H1cgcnPGTdKpEYvv4xJ_-_9hB2Npqxo9PcyKqDj-0TMrIJrNUOZYmnUsfCFVtSuZoqBdrx4WSWZ8xSMY1gB2cfTe4VBgy_zePNA4mAvEGB2fDNnIXeASw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4QHgHCil5rd4sclLYacHIEjcZTRA31fSEd6RN7LVA-9HKipES_Z9ogd1AelRI1HOFiEdu3z4yDw7tjf-NFA3byiJUJqCt2iJqSkBvYw4AFt8dMbu9oOg1DO_ppLYeFExI6FNWH6Mjox2NQtkD14KLYHL0t_Nc42L2B67n7YNfJrpZl_gBCatKVjzfX-EKN_xI53V6xdzB20DrYrfdgTtoTPshCYZ8UHa2JyF6y73vgTwsGxw8tHkX6qqW-g16Vd3X31gRrG0NDqN6Hfjc_9fGSIog9ccdDbgWKM9ytlEYhEaWhq22N3rso1aJ1qOMnhbpG9wL-3G3JmZHvJ8xa7yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDxH9xYAlPxXFikQvxbNpz4Gc3y_eZ21LMqXDBnKdheNLtVGmmsia-w_iWcitRAJKWO2-WzsdMfbXutzpMOZBgFv_-42bxYmKfkeHbl4n4kkrUkmwhIFHL2cgAr717lYXoXYU9oCecpMJV-2L_qjCG_9J5EPnpEA6Eufrjhcp2lFtCtd_kCK8z2oQVo352cVOeTAEr75dYiHv_k2bARzI41QsIfqbiAiFJ4EqgUKXejuViRhtw0OuVH1E9TvCygPCD7SPC_wtsyA60MTeRSdZxUuguW6qpcqIXQ0YwFV4zRmPT0JHoZWBzIicKcDkeCEeFXj0zj28tMPHHfjOwl03A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mkz72Q0hJEM5YYY1hBAW-dqXjWbEQWV4P51QSENt7MQYl9C4mf712FnkbQSglsH-Qdmn9RcmZoN8lD-dmMwWvgUowhy4JEfR27OCccVK9-zD1IuJYcZ45kr58uyTI6xBg-Fo6_PaqhFT6ZMBFHCeBD7QZOWcAvNDwq-6sDqvjSmqngB_QqwyTaUdBJMswRn0A66uJuYEjh2r8wFV6cKD1ankod9WAvtlCFnzncqcuYpkktunzxx-G-_e38Uy6NDAtlFLXtE1suP8Mc3iMe3mt77_u-YTPzfbTLJqHQdF9_XQ03Ptz4oN8Z6AwVnqFw_R5rS38TXVOMFzHBBBI3J5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=sDUImp91Gp-AIDM2mGjlcYxEUCchgeMa4ElS4kd6c7Tb-fTQ2oIKihWZpXVf9FRkokIiEAIvpoXuR7AROouyRw72RZU1BFSkv0s1kLaYRwF-7XWYflCiKbAgK1vK-GwCOXtGUY-KH1H2hnwFVwxzsbnvwDvhlLHJ98qXAf-C9yyXb5Wso04NpU5mULuJYa_zuXDQFSBr6UnpxEuAgNKzvAqNB-bC_AJzA_GL7MY-toiR84DvLtt0kjhofYCf4qff-Vq2RbdxgPsovuOuE1iQbSUGffZe9BMIAaPz5KZ-rmT4mJ1cAmqSv2rG-nhHU4sf8X59eiYNHknQOdUQNvKlsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=sDUImp91Gp-AIDM2mGjlcYxEUCchgeMa4ElS4kd6c7Tb-fTQ2oIKihWZpXVf9FRkokIiEAIvpoXuR7AROouyRw72RZU1BFSkv0s1kLaYRwF-7XWYflCiKbAgK1vK-GwCOXtGUY-KH1H2hnwFVwxzsbnvwDvhlLHJ98qXAf-C9yyXb5Wso04NpU5mULuJYa_zuXDQFSBr6UnpxEuAgNKzvAqNB-bC_AJzA_GL7MY-toiR84DvLtt0kjhofYCf4qff-Vq2RbdxgPsovuOuE1iQbSUGffZe9BMIAaPz5KZ-rmT4mJ1cAmqSv2rG-nhHU4sf8X59eiYNHknQOdUQNvKlsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJsed52vaHfFkqRmjsKQ4aujzehwNvLKJQmQDP2cz1K0h2S606MGEFRL8Bl1WfoqtWJTXXXu4FHjNsAj-sMJ8BKYRkIn9Q3tykf1R_KuAyHB1AG9-mfnpbHOn7Ug71zdrzbXoq9joXKNa0Wbzl5iZZFDSUpXM648lP4Am3fIp464-BrM3HOutVriIM6rXWGAbYFZw3rNLCTzk_7YO2ztYG28N0yCMLqosJPfutyHjkaxZ82y48Q3Bbom08nFGMARkjY0O8o-htSh8ML9zqC1q3ge0hL6OaZ-dUOlJS8WuCCs0JkZ9c3a21HTzWdJAqu4CEKk5yvlfGdnbf1DWmETTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu1oUWsDn35X5i8AeIb4IMbhCZkW41E1q1fhYEN6CprgObuhRl82wj7PrqKUbPbHcDWnjTVGSQOdRdwYhFMiUPwUaaOsnnvuwBI-BDRfWpSudVY9vNkpx4CkUg5Q_4rkLTIiWOWacQzsSIGJsRNDs4i_LHHwDlLZ-nWBEy83vBjsADjDKDeK6xxd8kBLgOtcc-i539-iK92kOhSOtPO4ILTa_XIZKrjsXcF362gNJhNAL-vUf7BkEalJsy8GWMR5ZMBZFPmxPrFX7nI_M6SJTIFxoL6WPiBPmM11bYupiuUwz1_1e6n-5mvGLOCoYQdTvMT963NzJNDcMOPY_qslYyAU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu1oUWsDn35X5i8AeIb4IMbhCZkW41E1q1fhYEN6CprgObuhRl82wj7PrqKUbPbHcDWnjTVGSQOdRdwYhFMiUPwUaaOsnnvuwBI-BDRfWpSudVY9vNkpx4CkUg5Q_4rkLTIiWOWacQzsSIGJsRNDs4i_LHHwDlLZ-nWBEy83vBjsADjDKDeK6xxd8kBLgOtcc-i539-iK92kOhSOtPO4ILTa_XIZKrjsXcF362gNJhNAL-vUf7BkEalJsy8GWMR5ZMBZFPmxPrFX7nI_M6SJTIFxoL6WPiBPmM11bYupiuUwz1_1e6n-5mvGLOCoYQdTvMT963NzJNDcMOPY_qslYyAU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Zbu7SnijBreEmuhtRsiSw6kJmq8F4XgPlwy7m14KQDTPc2f4R0XKSH7_ketQPNV9cfO-zgMWDeeiaFWkl0zjEIl78DFhg_6g36xvBAEPr3D2pIWq8P6fG07nb4H1fBZQp9PaIi9PrcTMTl9or44vLDtBu0lMof5wLydzWvOvzgTyzi2UgXMRbzGhiMB8ZWgNKTvPLeWR-bS1ikTJy_aBVrMlszBgeSy4z6-q_XC69enDf-6eLZ525tSTX5ZUJ6bGQgpOX_PkdGuu1Zl-15pRSD9ra60MgH0jilJK-NVMAs51YKcZgjwgWDaqLLntYbhkxKiqSTZprahS2cwsU2Ax-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Zbu7SnijBreEmuhtRsiSw6kJmq8F4XgPlwy7m14KQDTPc2f4R0XKSH7_ketQPNV9cfO-zgMWDeeiaFWkl0zjEIl78DFhg_6g36xvBAEPr3D2pIWq8P6fG07nb4H1fBZQp9PaIi9PrcTMTl9or44vLDtBu0lMof5wLydzWvOvzgTyzi2UgXMRbzGhiMB8ZWgNKTvPLeWR-bS1ikTJy_aBVrMlszBgeSy4z6-q_XC69enDf-6eLZ525tSTX5ZUJ6bGQgpOX_PkdGuu1Zl-15pRSD9ra60MgH0jilJK-NVMAs51YKcZgjwgWDaqLLntYbhkxKiqSTZprahS2cwsU2Ax-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=voSumZFrSAk2p1ZDK2AdC02DLVnkaM9s5ZT6zy9qLBitYSFSLLZWnNae6h0V3VNqpsxpM8_5BLNw4rl27XLkcKkDJKjGj0Xszhd_g2tKiU_zRxKkswKOeV50AUpftVC5pTcNmGudysMmhxK0c6-Abvxjkxd8cPl5nON29bur8g8TTMSNT_qo5BAdvWRHe8QBQvyL0eQJfVAOsh0Pnm8gfjCfedIQpUzlKXP8WK6xWijTJqjYxNe2O6xGF7CK24DqL9wbaCuCnBHcgXouO1fEBWCrlbMAxMsJPwomJSlYQbQyaYuXcwg88f7kFCvHoYtrVycE3cEiJfhd89ybHSjMCgm7wEvIAfCK47yfyKZUYxpKk4PSRLJzK8SatCGJ6SVEm2BLOKaDFsQtl81Hfrrvc0pmsT4CRzOAD66pDPjFlmYBo2Fz_mHDljN9TE3o579YrEon7AWQXyJsfyNTQt--gtLSJGqZfg3zjxcHNek85MTV2wjD1jusBMH8pIf32PWgnTEuP8WxXeyICBE7NL0FzrBrXORg-CF9BffOohNanoef5h1W4h72UjysMknYJNDAZD4_9BZw35motrtRQDAQTcjhm-JmBJnm6_mWeFdh83ZpNRWmiNWGBdEU2EINyJtRE0juoIjd-7ExIEQ5T3A7-MyiIngmxFd03SXCgJgTgs8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=voSumZFrSAk2p1ZDK2AdC02DLVnkaM9s5ZT6zy9qLBitYSFSLLZWnNae6h0V3VNqpsxpM8_5BLNw4rl27XLkcKkDJKjGj0Xszhd_g2tKiU_zRxKkswKOeV50AUpftVC5pTcNmGudysMmhxK0c6-Abvxjkxd8cPl5nON29bur8g8TTMSNT_qo5BAdvWRHe8QBQvyL0eQJfVAOsh0Pnm8gfjCfedIQpUzlKXP8WK6xWijTJqjYxNe2O6xGF7CK24DqL9wbaCuCnBHcgXouO1fEBWCrlbMAxMsJPwomJSlYQbQyaYuXcwg88f7kFCvHoYtrVycE3cEiJfhd89ybHSjMCgm7wEvIAfCK47yfyKZUYxpKk4PSRLJzK8SatCGJ6SVEm2BLOKaDFsQtl81Hfrrvc0pmsT4CRzOAD66pDPjFlmYBo2Fz_mHDljN9TE3o579YrEon7AWQXyJsfyNTQt--gtLSJGqZfg3zjxcHNek85MTV2wjD1jusBMH8pIf32PWgnTEuP8WxXeyICBE7NL0FzrBrXORg-CF9BffOohNanoef5h1W4h72UjysMknYJNDAZD4_9BZw35motrtRQDAQTcjhm-JmBJnm6_mWeFdh83ZpNRWmiNWGBdEU2EINyJtRE0juoIjd-7ExIEQ5T3A7-MyiIngmxFd03SXCgJgTgs8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=rmomINW2LF3cYlyypywB_Fv6Y_Ngy2T_eY3kOfKWVszV1_TCGcrqcIy1dVj0of99kYaaBfjDVitMGxvYQhNnH4G-9_RtzODsIgrawbtnVHZW1TOpUh424osbNfM0YwefMltyJtp-E8ik_BG-BXoRCsx8Ev7uXQVKqoan2Vrgqf2c61zUXnP4VpU0lnMA0bd3rneLJQH5sR7mjMfnQeR93q1HZK1_nyrl7gOSiNhxwv8GIo5q9mVWIaKV9AwBDdMyEPI8bizXsBKJsdSHgV-z_7tqFvgUWK7Nt1a28Y_w6uk6iR2NemQGFtlryYPNx7lSeSwwbHu1ozY5Id6WRHHdLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=rmomINW2LF3cYlyypywB_Fv6Y_Ngy2T_eY3kOfKWVszV1_TCGcrqcIy1dVj0of99kYaaBfjDVitMGxvYQhNnH4G-9_RtzODsIgrawbtnVHZW1TOpUh424osbNfM0YwefMltyJtp-E8ik_BG-BXoRCsx8Ev7uXQVKqoan2Vrgqf2c61zUXnP4VpU0lnMA0bd3rneLJQH5sR7mjMfnQeR93q1HZK1_nyrl7gOSiNhxwv8GIo5q9mVWIaKV9AwBDdMyEPI8bizXsBKJsdSHgV-z_7tqFvgUWK7Nt1a28Y_w6uk6iR2NemQGFtlryYPNx7lSeSwwbHu1ozY5Id6WRHHdLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmyAFI44vv7fGnl_HhX8DAugFTcgVRNnIDgun9bOYd53pyEpA3OMjc87lBFx7aXXIDqtBd_wPqvRSgBQaelnftGUywUrsO3BnMMIuqSmhc0xe2CEhotEAF9Ouvbrxgdc0OKt0nP3UZMonowJ6iC370DxLeClQUipBhKx1z90TxF74ZVG9s-nbgaeYkqh548hCXdqa56zvm9Lu3DI4drcczcZleDUAZM_7TQTavvXaqxGvg-d7ZRqh8wchzXPTNPFNLr4EZw9YbcOGq-rxDf0PSCNtzT_WOFDGabp67QUel_lZtRrcCNr0EWQvBSLypa4yD3jPAI9CsL_0sRA0UU7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=mwfyYYVlSq_ouKl_xB8qXhwFFERqxGV0EVih53hUAzJIJhslghzMHTY-74G3mvrWlnNeR69d5q6Wojn_JxsCTVhYCjvvb7d7P1wmWgDrASLKxqPAFyNKcATdFjoLhMqEnghEL5ddhAt9pdj2PuDAXGlyrPuD6-Xz4Cr6p4oqpLKDa46-sBs-kj4CiSU3vs7Z_q3TVMfJAChBj9UchBKoNhax4JPtZ13TIlOHUO-0RShHgl6hBvpIZegs9Yjnta8UabBdifuAftfo13v0AFbkiojCD090FL5W1j-B6FzqhRk0Er0-kB1JdK5jG0a9wpiknyPr7ak0oGyFCL1EyvmYwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=mwfyYYVlSq_ouKl_xB8qXhwFFERqxGV0EVih53hUAzJIJhslghzMHTY-74G3mvrWlnNeR69d5q6Wojn_JxsCTVhYCjvvb7d7P1wmWgDrASLKxqPAFyNKcATdFjoLhMqEnghEL5ddhAt9pdj2PuDAXGlyrPuD6-Xz4Cr6p4oqpLKDa46-sBs-kj4CiSU3vs7Z_q3TVMfJAChBj9UchBKoNhax4JPtZ13TIlOHUO-0RShHgl6hBvpIZegs9Yjnta8UabBdifuAftfo13v0AFbkiojCD090FL5W1j-B6FzqhRk0Er0-kB1JdK5jG0a9wpiknyPr7ak0oGyFCL1EyvmYwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=MmGc3XD-Xmubm60RZvphJAXXu5X6936cRq2iY2BbeFXCMWAYjN0iTl9_Ic-IwHLwd9i-OcbvwLYSSpV66phstg9PEhB9_37wAvhqXK-fMecZdPu-yjxIkK2-az_T0b9A1ifC07_W7xqHnFSzzi-HZU1eYt6Sn6atQsFm9KYrT1MnDxJ0-RVnsCE5AvIRl8iVElWD5ZawryLiZgXAlonbK22UF0WRb4vaB3tCptXhoy3vf6vuUXgA6DA5VGnkjmSQpiDM2_sttXwPYQwSXVDXRUhvpKFPRu5PI6AXcI5vtUylZAAiv3n98vfNGXPUbwG_0LDu26yW8NM2G08N8cljPXA8nNqk-9SxRA_qGvLP1ssfzEBWSMi4Mpxjls_2PIolTbZPH50QU_7G9lEIRdVI9CLiq-QrpUsC956BTMmbB8vWQ-Oez9utoQDu1HDvAXQMmLo9n9xSEF47nADaPgiR5ADMJc0bB6_JS84_KsPlml2_BKiRcHmLS5irkrr2zvzlcmGOZHJkx2R8leQiovdQxxM7Ki-Wlu77oSl8sZEwtyp2WRMXa7FhJhnajGUupz_PyIFJQr0c-39Rzy8tCh5soaxp3FQt9O2XgzUSiL6xY07phbiq-pA7JgeWGoHn0M6_JZ4ppk9Wq4SPHMIPnMHcLqVK2LmnzqMmaS4ZYO0cWBo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=MmGc3XD-Xmubm60RZvphJAXXu5X6936cRq2iY2BbeFXCMWAYjN0iTl9_Ic-IwHLwd9i-OcbvwLYSSpV66phstg9PEhB9_37wAvhqXK-fMecZdPu-yjxIkK2-az_T0b9A1ifC07_W7xqHnFSzzi-HZU1eYt6Sn6atQsFm9KYrT1MnDxJ0-RVnsCE5AvIRl8iVElWD5ZawryLiZgXAlonbK22UF0WRb4vaB3tCptXhoy3vf6vuUXgA6DA5VGnkjmSQpiDM2_sttXwPYQwSXVDXRUhvpKFPRu5PI6AXcI5vtUylZAAiv3n98vfNGXPUbwG_0LDu26yW8NM2G08N8cljPXA8nNqk-9SxRA_qGvLP1ssfzEBWSMi4Mpxjls_2PIolTbZPH50QU_7G9lEIRdVI9CLiq-QrpUsC956BTMmbB8vWQ-Oez9utoQDu1HDvAXQMmLo9n9xSEF47nADaPgiR5ADMJc0bB6_JS84_KsPlml2_BKiRcHmLS5irkrr2zvzlcmGOZHJkx2R8leQiovdQxxM7Ki-Wlu77oSl8sZEwtyp2WRMXa7FhJhnajGUupz_PyIFJQr0c-39Rzy8tCh5soaxp3FQt9O2XgzUSiL6xY07phbiq-pA7JgeWGoHn0M6_JZ4ppk9Wq4SPHMIPnMHcLqVK2LmnzqMmaS4ZYO0cWBo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3UznSWLbpyKqrE0K5eJW1YpwDRd4wLI5QqktmPw43Awe2TSzbflcGLG8_84ebyamXbrxgXiyjpR9g-ne2ev9PnUY4MLUc5FPhHBKAud3A1EGr_NEmM65_fxJhhj0c_8mcDFWY57fNALRPOvyRgfgIm_LoHyItouCZ7AhLsnQrxIGL2S_3rlNsLBX58ZS6kHxuXMx-wUUwcEkAPtb8_XR_TumrVcCELTAZqbONi78elgMD21A3YWdmZ9_r4_s5L_qzQLCmPsZ0mb8aSyfuAOuhSaMtU48P5ajZas2hfmugpQa9aaMifGLYzByv8XI0NW-8YKewL0BWJvbjQaeowfLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=W5IoSntO29lFObl_mvL_QhsWkwFBWflVmq4j5u4Gb-Np-YkUC-oEZuu4sun6629tkLkU7i6kf11aQUs8-ehfRG0YK3X1rNCymeReIMnqeKdzYAmKIFv4V44HKE31afsFIpg7C0-4Mj5JNZG41ugiSpAEr0PF8k8H8u0rbv6mvukRQ1XGBzQ-19fVfjYlnyblRZvtRmTZ22uVi68beT2bq8u3HJC51c-huAdu32QBJoSnQL8V4anu9x8sw1EKea8bq8NMT9vjWsV48xzG9Za2q2mTfCYSM2_N2T157uckXZlIY9Qn94M_NsWzIO7e0UID7ag2ZnBTHN1IrP4-OdAK3xDCaiWPBq5Xxcs5PkyjM3OyzUsOe6xKnlovJCwg3EU--Zmwqko5rdmoY1w8K5Y_Yyi6i8MRmJ896x_vYLEUYK81l_3Or3wSejjphnFZFoblf_5085spj8yQHBkNhPHKonlbFlSYPDyznCc9UnZvMgwEQ7okEJXsM6iOH4f7oR1sAMUoeyG3NQzOgrOpct6uV7NXKhYtNx-jl99xlvSqSqdBW6VQ1koGskbhd-tbhrh0O0TbDXOtVzudJQSm_NA3xNho-hVgBE6Q-GxdoN6dR2whofOLrDiQcbUJ6x3A9akLQt-f3KXEwkkG7zrDAFvTXPoh2XJbswqm7vHn191G_A4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=W5IoSntO29lFObl_mvL_QhsWkwFBWflVmq4j5u4Gb-Np-YkUC-oEZuu4sun6629tkLkU7i6kf11aQUs8-ehfRG0YK3X1rNCymeReIMnqeKdzYAmKIFv4V44HKE31afsFIpg7C0-4Mj5JNZG41ugiSpAEr0PF8k8H8u0rbv6mvukRQ1XGBzQ-19fVfjYlnyblRZvtRmTZ22uVi68beT2bq8u3HJC51c-huAdu32QBJoSnQL8V4anu9x8sw1EKea8bq8NMT9vjWsV48xzG9Za2q2mTfCYSM2_N2T157uckXZlIY9Qn94M_NsWzIO7e0UID7ag2ZnBTHN1IrP4-OdAK3xDCaiWPBq5Xxcs5PkyjM3OyzUsOe6xKnlovJCwg3EU--Zmwqko5rdmoY1w8K5Y_Yyi6i8MRmJ896x_vYLEUYK81l_3Or3wSejjphnFZFoblf_5085spj8yQHBkNhPHKonlbFlSYPDyznCc9UnZvMgwEQ7okEJXsM6iOH4f7oR1sAMUoeyG3NQzOgrOpct6uV7NXKhYtNx-jl99xlvSqSqdBW6VQ1koGskbhd-tbhrh0O0TbDXOtVzudJQSm_NA3xNho-hVgBE6Q-GxdoN6dR2whofOLrDiQcbUJ6x3A9akLQt-f3KXEwkkG7zrDAFvTXPoh2XJbswqm7vHn191G_A4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=JNQ2SUos6zhF9KXEU3cp9dTNG16LebIG1PHW9lPnXIlzHUdtfZA7m33vxlqN2jEiiYmU0sdESnXDSLUJRTvTldcGv8oZlqaHdgiy_l9Heh2jYseEX_jTCvUqxcBuFQCVdH7oWwfvG8o8uksNF38nBWdnN_li1hYy7IR0GFt7B5TPcpg0F71j_wScWpHLZx9pOWY9l8Tn9F4NJc6yGPuDh5bffVqyx7T-AuMHTKUQ_XbOdcFxVsW5hp5gbf9wfM2geEYfMlihtRHTMUVItVIIvK18s2x76SKYqdDj5JSz2IxnFA2Cu312wIQn0BHFvWE6iwzLjH5j4BL4xvRm8i7uLDo-i8g01y2Pkpxo2WbGCf3Q0j9ZtnS4wmRYGx7Q3Oy7x3fT5MLBKki1tJuPk6UyAlqHQuAvPEfUBv_7TRVIinvnzMFwZLlKUDbaFy9nlthrkfNsOS2JCwKAoncTC2VRZWldLL6LHA2WwqdMplKVfSzJ3TcJeStAa7pbsiV_e8iVai_kSEm-KCigqMSUcdIZmdQVUd21ugpc0Ez8u0q7jGIPEokpzF_7-ADlUNq96QI9CE73d1ktmHvgHAXn9kyoBgx7ikn9iekJxpvWa-jg2gg4WCedKkh5xfmS91KlOgK3VeKux3ezZa2FGReuI14nyBSJf8gz_1mCRKLDq41HIpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=JNQ2SUos6zhF9KXEU3cp9dTNG16LebIG1PHW9lPnXIlzHUdtfZA7m33vxlqN2jEiiYmU0sdESnXDSLUJRTvTldcGv8oZlqaHdgiy_l9Heh2jYseEX_jTCvUqxcBuFQCVdH7oWwfvG8o8uksNF38nBWdnN_li1hYy7IR0GFt7B5TPcpg0F71j_wScWpHLZx9pOWY9l8Tn9F4NJc6yGPuDh5bffVqyx7T-AuMHTKUQ_XbOdcFxVsW5hp5gbf9wfM2geEYfMlihtRHTMUVItVIIvK18s2x76SKYqdDj5JSz2IxnFA2Cu312wIQn0BHFvWE6iwzLjH5j4BL4xvRm8i7uLDo-i8g01y2Pkpxo2WbGCf3Q0j9ZtnS4wmRYGx7Q3Oy7x3fT5MLBKki1tJuPk6UyAlqHQuAvPEfUBv_7TRVIinvnzMFwZLlKUDbaFy9nlthrkfNsOS2JCwKAoncTC2VRZWldLL6LHA2WwqdMplKVfSzJ3TcJeStAa7pbsiV_e8iVai_kSEm-KCigqMSUcdIZmdQVUd21ugpc0Ez8u0q7jGIPEokpzF_7-ADlUNq96QI9CE73d1ktmHvgHAXn9kyoBgx7ikn9iekJxpvWa-jg2gg4WCedKkh5xfmS91KlOgK3VeKux3ezZa2FGReuI14nyBSJf8gz_1mCRKLDq41HIpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=IuNOXR2uFWqtP2p25ytjB7GU95e8p1ez2LFu_nCVKRCrG2SJc5Tt1o1AF-fZvyYP21VA3H5Us74XYP-YjjeJ7nP2DwATc44bGtvYQK6SFrvr6dg3x9FAgPG0LR1_5m_vIELD_5XvEZ_TmIVo6AHNHZxb6_fPdOu6QMsjIJv_JrhNFhJ2EDFzw7dIlY2tp3Uc7aT9Awosfq8zjO-mOS_1AWlwINvfxPjXVE6O1gMyOL3VSNdqMg_9nfldlWRn3AkQae7v_4BzkuVCCMIK5WNGTvRdqm_PjLbonNwFpeeBcPtJQ2QJVB4rAiPmrIaO0eILW48iOPDjxxzJnmJA_1z8tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=IuNOXR2uFWqtP2p25ytjB7GU95e8p1ez2LFu_nCVKRCrG2SJc5Tt1o1AF-fZvyYP21VA3H5Us74XYP-YjjeJ7nP2DwATc44bGtvYQK6SFrvr6dg3x9FAgPG0LR1_5m_vIELD_5XvEZ_TmIVo6AHNHZxb6_fPdOu6QMsjIJv_JrhNFhJ2EDFzw7dIlY2tp3Uc7aT9Awosfq8zjO-mOS_1AWlwINvfxPjXVE6O1gMyOL3VSNdqMg_9nfldlWRn3AkQae7v_4BzkuVCCMIK5WNGTvRdqm_PjLbonNwFpeeBcPtJQ2QJVB4rAiPmrIaO0eILW48iOPDjxxzJnmJA_1z8tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=WoSvB0scFDQnR7nwmbn4X4U2iT1QnaYGNfEITLFDzCE5nPhafJq08SDRHy52EpMbzkfQWIgunx3BMJMeAGS6h2fcRORqir6fLW12kjwsyn061qNQsbWClKEh3ywD1BMH8D7iA252jh-MJ7Py1AlbncrAguO8B1Wv63pBQbQO_cnBVSDLtj8Lkgz-qHUFTnEJXQ1y-mihwz8-DLlsLTSxBhmf2t9XL_n0wGNP9WaAd0i6wp5a_B1ief73kZMaAiwHL-1grogZExfqjoTosrMROxTdqkUy4Gv_sWpO5CI_Ghh-7bZ3h9W_Z_pjA76UHGGO1mBNSPdPmpGncjZ6AyvbxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=WoSvB0scFDQnR7nwmbn4X4U2iT1QnaYGNfEITLFDzCE5nPhafJq08SDRHy52EpMbzkfQWIgunx3BMJMeAGS6h2fcRORqir6fLW12kjwsyn061qNQsbWClKEh3ywD1BMH8D7iA252jh-MJ7Py1AlbncrAguO8B1Wv63pBQbQO_cnBVSDLtj8Lkgz-qHUFTnEJXQ1y-mihwz8-DLlsLTSxBhmf2t9XL_n0wGNP9WaAd0i6wp5a_B1ief73kZMaAiwHL-1grogZExfqjoTosrMROxTdqkUy4Gv_sWpO5CI_Ghh-7bZ3h9W_Z_pjA76UHGGO1mBNSPdPmpGncjZ6AyvbxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=rlE5IsVm8u7eyNsZWR1PFAyGc--IJ-RR8Ch-fr-l7jO_VV2wBJN_N1WifuId-f9htSzbjoC9nUHI-8dE4MFd_kWGN-93nZOBNTvtJhHbirk9ZoMEWETHrI7VrAGg-OEYywmLZzbbYT2OGZQgKyo6RRr-rjXZ0grvnPhDUyHdqqzeyi-lBXPPnWjGQTY0vSoKvoUh3VRBi9L7ynJ9OOXmdV4aN6wBYSnDCJM-Fq5zU65h8Zz0qPmCSl2JM4_Q2IWXgs5DAMdbCdx_dt_KlKaKiRm3VHueNuedk-kcLMLXyLu29YTKftlXqbwzpd67sq3fjMFqJQj357Gs9s2QnCbOSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=rlE5IsVm8u7eyNsZWR1PFAyGc--IJ-RR8Ch-fr-l7jO_VV2wBJN_N1WifuId-f9htSzbjoC9nUHI-8dE4MFd_kWGN-93nZOBNTvtJhHbirk9ZoMEWETHrI7VrAGg-OEYywmLZzbbYT2OGZQgKyo6RRr-rjXZ0grvnPhDUyHdqqzeyi-lBXPPnWjGQTY0vSoKvoUh3VRBi9L7ynJ9OOXmdV4aN6wBYSnDCJM-Fq5zU65h8Zz0qPmCSl2JM4_Q2IWXgs5DAMdbCdx_dt_KlKaKiRm3VHueNuedk-kcLMLXyLu29YTKftlXqbwzpd67sq3fjMFqJQj357Gs9s2QnCbOSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=crhb1acnh0GyUZ8ba8AZucrTv4Hg-Ve3S2sZOC47yVipo5PYTDNIpzY1fSDD2_6CE-PR2JKMoII3oeSZhX3x5Tc1q1K_F44-XufuPuYz5dEky_Kk7VQx4ff97107OXqkgMwCemk6cOKyyP2j_dwX0jzW5EMzQr8t44nRhIpM_yUJMR9LGq-kR1p3CMKX_EUKMdNRTrFj-_l_6omVyA3vvm0llpl82jGE9gzmXcPzd3_JOM-nuR5yWw1x37vhkJZsn3w_4NoVGdd4mjOJYkq1RBkjj4pOA6c36EOBqLrzkUjJvCpWM3qdN_oNrK_ATnXRhevLpCOf5nJYFueeX1WM2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=crhb1acnh0GyUZ8ba8AZucrTv4Hg-Ve3S2sZOC47yVipo5PYTDNIpzY1fSDD2_6CE-PR2JKMoII3oeSZhX3x5Tc1q1K_F44-XufuPuYz5dEky_Kk7VQx4ff97107OXqkgMwCemk6cOKyyP2j_dwX0jzW5EMzQr8t44nRhIpM_yUJMR9LGq-kR1p3CMKX_EUKMdNRTrFj-_l_6omVyA3vvm0llpl82jGE9gzmXcPzd3_JOM-nuR5yWw1x37vhkJZsn3w_4NoVGdd4mjOJYkq1RBkjj4pOA6c36EOBqLrzkUjJvCpWM3qdN_oNrK_ATnXRhevLpCOf5nJYFueeX1WM2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=NHjrjPApdyguUOEtF2gabk2q-2dFT19hRNP3CCqhgAhRXGO1LjfhmPYzfljGSMa3v7NrbbxFllZwTHU8KTWlDEEij2wWHvUGCTlicn5cWbaDJWhClAWdWq_L9ZFzli63cPoSAXzgMJbga6Sqn-NGA-2VqHBLWYq6ju00x2oWD56-pnQ143Ht2ZXgkpDaF52DzPTAwGmI8RFpBk7QXfY0y8NmwhbsEL-NHTYcoYMB4nUWjafsU9RJlCuqZermiF6e4m5QdX8rPxq4ZtumhEmb9-FS-2LUpCi50aI3wnCDAfyZJxUO6_uCBWGqIyI1_A6DlK7An6G1NAa7XmXeFJAhtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=NHjrjPApdyguUOEtF2gabk2q-2dFT19hRNP3CCqhgAhRXGO1LjfhmPYzfljGSMa3v7NrbbxFllZwTHU8KTWlDEEij2wWHvUGCTlicn5cWbaDJWhClAWdWq_L9ZFzli63cPoSAXzgMJbga6Sqn-NGA-2VqHBLWYq6ju00x2oWD56-pnQ143Ht2ZXgkpDaF52DzPTAwGmI8RFpBk7QXfY0y8NmwhbsEL-NHTYcoYMB4nUWjafsU9RJlCuqZermiF6e4m5QdX8rPxq4ZtumhEmb9-FS-2LUpCi50aI3wnCDAfyZJxUO6_uCBWGqIyI1_A6DlK7An6G1NAa7XmXeFJAhtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=CsRttsG9vyr0ipl99Kn1E4vpyM59exJ1TNT1R5cCRkV5W-ASEHJhu6q9DvmvxmGblGPoProf1RNTELWurNpwZlfAW1UJU3TJdlQvX2fAb9Wn4tYnQji2F2MYE7xCed-EhC6EDW4wGbwiSFWsY1IW4dO64HuyxB_pLOtta4YWx_5koMBQ3U7A4fXTUVOuz4lvVM_faDjLN2aO9LWka-0WFpzngSg-nxVKMlc_Lvc4FnPfY2-E9tEiAG6xqvNKT7aiHFrKvE_0M3VaVnMDgFBEm00hf5D0e0jTXxjdxCtk9p1ni1qWnjZ3ptxgbdwty3jBHOWSpFxlG4I1Q_jsEX30Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=CsRttsG9vyr0ipl99Kn1E4vpyM59exJ1TNT1R5cCRkV5W-ASEHJhu6q9DvmvxmGblGPoProf1RNTELWurNpwZlfAW1UJU3TJdlQvX2fAb9Wn4tYnQji2F2MYE7xCed-EhC6EDW4wGbwiSFWsY1IW4dO64HuyxB_pLOtta4YWx_5koMBQ3U7A4fXTUVOuz4lvVM_faDjLN2aO9LWka-0WFpzngSg-nxVKMlc_Lvc4FnPfY2-E9tEiAG6xqvNKT7aiHFrKvE_0M3VaVnMDgFBEm00hf5D0e0jTXxjdxCtk9p1ni1qWnjZ3ptxgbdwty3jBHOWSpFxlG4I1Q_jsEX30Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=sP0KWnEgEdiNvVILBqhzqc0sBFWX86suvAuNZJs5FbrHeiRA-Uu1oyNbdPp4edsd0Gi5rlGDyBVFGw_X0jh1oJMuQvtQIChxncT0dXTlUdki0NgV-mwvmNd-eRgPEky8D0igp5wt8Bpq_2OLaW28GEyxXq_yOL0g8TKGA1P9F98F4R5NJQOO1IH7US3t76qk5w2SeF0IWiuaFWxPK_tF5yeT-btcsWpmtq3qFeYBGYYEKsKSjgYLlnMLSBz6vFqIdol9O1Jk7Qms3pbPfQn4htA3akN9jysj48SOca3Bf__Jqpir98N2xFrNY9lFUfGIetbnkluUgEzFQLQR2iXqfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=sP0KWnEgEdiNvVILBqhzqc0sBFWX86suvAuNZJs5FbrHeiRA-Uu1oyNbdPp4edsd0Gi5rlGDyBVFGw_X0jh1oJMuQvtQIChxncT0dXTlUdki0NgV-mwvmNd-eRgPEky8D0igp5wt8Bpq_2OLaW28GEyxXq_yOL0g8TKGA1P9F98F4R5NJQOO1IH7US3t76qk5w2SeF0IWiuaFWxPK_tF5yeT-btcsWpmtq3qFeYBGYYEKsKSjgYLlnMLSBz6vFqIdol9O1Jk7Qms3pbPfQn4htA3akN9jysj48SOca3Bf__Jqpir98N2xFrNY9lFUfGIetbnkluUgEzFQLQR2iXqfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n84yElJVpfkHt3y-LCC952v8LLiERscbXn-Tt6xmcLt_icmTaEfXN5yaZm1tNs73buYRgdpAOi6bdlhIjK9gC22Hb7xOQqpI8Cl1T_AQAsxWqjYXFrmH9mLqtEZtlbRvyedKsJDF0ZaWYYmPGOtsms2Zar9qHRH7HPfAzJiGpmJ51noyJT-ly_dJcCG2cN9gYYxwUvVFRd3H-QHJSFlGbSMKmG91ANOWkkcWic8EFnr7V675pB_cnsCz9myr8g6YGEVIQ9xfo3Vlfy9fJb4TfKT9rBNrMj1Gd7POEEPzcBKbe1IPstZrZOm8AQ4xJF5HIqsTUmnZsE_IdKYFk9n8ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=u1Xt7E_jzY61d7S9mmuXF0SlE6ZB5vnNuSe2QDF_9Sl0A7wsTB_chk7yF25VOp7E3Ox0Z6UPImSex99TjTxtZNVJWmMyBV9E44Tm6gEbpngepu00c3a7D_AcnWOywCrSP30hiCu7QncEooSVNeHoW8VsPDu1JLoIRvwC3Fa04bXHMY5Yl1UgJ4toUr1R1tdA2xHM5nqxQ2XxrHuqxJvocs7fcygKmZKvrUFkeHCbbDCul7Ww6sVlqzTv-WGCddJMzs0eeZu2gCYBrl7KgyBqZKtIGipeNsoJNwvE507zeQwmw2aKjlg8YucHN9amD3_YME40_Yc_Ncop_AmrVlXUag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=u1Xt7E_jzY61d7S9mmuXF0SlE6ZB5vnNuSe2QDF_9Sl0A7wsTB_chk7yF25VOp7E3Ox0Z6UPImSex99TjTxtZNVJWmMyBV9E44Tm6gEbpngepu00c3a7D_AcnWOywCrSP30hiCu7QncEooSVNeHoW8VsPDu1JLoIRvwC3Fa04bXHMY5Yl1UgJ4toUr1R1tdA2xHM5nqxQ2XxrHuqxJvocs7fcygKmZKvrUFkeHCbbDCul7Ww6sVlqzTv-WGCddJMzs0eeZu2gCYBrl7KgyBqZKtIGipeNsoJNwvE507zeQwmw2aKjlg8YucHN9amD3_YME40_Yc_Ncop_AmrVlXUag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=QBiI2TjHaJBE_sH_7UGJHxpZ919C8HFxOSHMOfg8Lbk_GF9kpZXmz2kydMFMPyV2Md4Uyty1rl0aDd9GiE5MU-N8QXEYD3FF82Sh___lfajFxjvXkHRbQfvYRRxlb4nEj8TGOhqvGiRVwqJdq3OyHwtARCL6j39oUQdyKlZyVN4TQ37RmsoLqpfg5irQ70BHbca54ygL3WXSx97YgZsdvHkEI_w8DJ7c8dhXqKTycvDVG6lD0E9zu-k7U5Oeb8yxSKIn2-oCbikor2K5X8AUAmAgOQxU-kNIQkJiFWlU8L2IBbLMOdrrPNlyEB-fCGm1OW0wcG6WiC57xdcoeae4qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=QBiI2TjHaJBE_sH_7UGJHxpZ919C8HFxOSHMOfg8Lbk_GF9kpZXmz2kydMFMPyV2Md4Uyty1rl0aDd9GiE5MU-N8QXEYD3FF82Sh___lfajFxjvXkHRbQfvYRRxlb4nEj8TGOhqvGiRVwqJdq3OyHwtARCL6j39oUQdyKlZyVN4TQ37RmsoLqpfg5irQ70BHbca54ygL3WXSx97YgZsdvHkEI_w8DJ7c8dhXqKTycvDVG6lD0E9zu-k7U5Oeb8yxSKIn2-oCbikor2K5X8AUAmAgOQxU-kNIQkJiFWlU8L2IBbLMOdrrPNlyEB-fCGm1OW0wcG6WiC57xdcoeae4qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=uQMm8hViN8f61w1Tt70t3IeJsW78QNmdxxZ6DIEpk9QbU_E1NZp3BsJ6twGduqyu1pyLMzexVQZnT55WtoTxjJ1bKsA9NsPxFz0Ndi9OV8Yy_s8vIQP0xuYBtaSVWRV6pLg-DyhebaS62TB5m1_dXFUjEpRn5frUKxXaWyPt5EuswGCImAlPwdHTth0CfCk6F1wcyraXSXyEhOmGRjh95Jb_mGnfrNBT_x9A8GRtDUpwZdPmbQDHvUHYQVX_nt9LpBKgHem5q2-64dITNX6Cu_zvt041E_2lGBsw2apXTs-LA36rr3nC9xLAYrRAAmtrGQuCD8rSWi958huKijBBtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=uQMm8hViN8f61w1Tt70t3IeJsW78QNmdxxZ6DIEpk9QbU_E1NZp3BsJ6twGduqyu1pyLMzexVQZnT55WtoTxjJ1bKsA9NsPxFz0Ndi9OV8Yy_s8vIQP0xuYBtaSVWRV6pLg-DyhebaS62TB5m1_dXFUjEpRn5frUKxXaWyPt5EuswGCImAlPwdHTth0CfCk6F1wcyraXSXyEhOmGRjh95Jb_mGnfrNBT_x9A8GRtDUpwZdPmbQDHvUHYQVX_nt9LpBKgHem5q2-64dITNX6Cu_zvt041E_2lGBsw2apXTs-LA36rr3nC9xLAYrRAAmtrGQuCD8rSWi958huKijBBtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=SCRXOkOswXtg1QDVYBp3Bd85kCdcz3zjdBDmcrrVMx8BDTh_353lTz4EZDz5o8Iu9pSg5B84YhQuf0comrtIEFdRrdOdSYQLi20nQZdTw_1MQPJGdsZBP5qUv6ihtgdnG4ObeQGUlIVcX7QbOfITQvSM7rtuLbxBmC0_-iNVh48wv4ZrFbcTwZRZ67IIWevTDL1D_9jaLGpv5kA9YPUybVZfnivHiuH4MSGT-fbY1W_4kbpt1l9xbShfwtAhYa-Qksm8dgGeh3ow_0CsxXkRWvfrTe9PxNClm8eVQTxAtxYExDf1Ksr6hv_fppOTugYm5fpBa35BWFx2SDxSkMqDCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=SCRXOkOswXtg1QDVYBp3Bd85kCdcz3zjdBDmcrrVMx8BDTh_353lTz4EZDz5o8Iu9pSg5B84YhQuf0comrtIEFdRrdOdSYQLi20nQZdTw_1MQPJGdsZBP5qUv6ihtgdnG4ObeQGUlIVcX7QbOfITQvSM7rtuLbxBmC0_-iNVh48wv4ZrFbcTwZRZ67IIWevTDL1D_9jaLGpv5kA9YPUybVZfnivHiuH4MSGT-fbY1W_4kbpt1l9xbShfwtAhYa-Qksm8dgGeh3ow_0CsxXkRWvfrTe9PxNClm8eVQTxAtxYExDf1Ksr6hv_fppOTugYm5fpBa35BWFx2SDxSkMqDCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeB4FcpvgT65vZkjC9pakk6Zdq0LkLasjE3e_r5PHf4FVL2j5g3gzUcSgrta9XDetn-5iOYnuHqgI5Y-l6iYBIMTgLrX0gyojaSRfjCc394NuENBq01J_l39mSFbvHJ_aivRQVuiS5yjzrHyT_avpZfQMoYIqVoof6Az6OOjeukaFBtAljZjvfxkL39ZugNh-gEVs_xu9J0Bp7e6jRjvDJ0KGLq6TwyUYtBTUUw-e2OxeWgyumvMVfz5im4XU2-KwWp131Z5yFrp-hGAOGH2M2Xf18ZUM4Hd8P-H2Pk4aqItQ0pN2_gQc_tS3ygVTexr2qjTMNhgDxpALyXEwuL_iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=gsHNQ8I-nq7FTeOslMHCabYyXLXTZAdfhCEPMrwhX5qRrMwMClXfPB_Y-5MI768w_5sLhoR92BCf60jfjpMtvKwY39Pf1VZaQ8L1TbK6t977ZZ9ct-7QkDZMwxOCCe8RalOovdABQyz3rx40XrRSAb9lahN57mKZGoXXJuduIz1MOG4VRBRxaqCvtJuTe-UnqE9XVCkmcVvJRugwes1VhQe1soSUKx9jeWDx03dko-zp9doezzRJRHyj6Qj4kf09AXMEVoyuOyjJwE-j0mZKZ9UuM0w80NZRgF-m0fHlpHFrFeI-FZYcgIkID3bXua2CDQu5bAajlPKCJ1B-PwvqhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=gsHNQ8I-nq7FTeOslMHCabYyXLXTZAdfhCEPMrwhX5qRrMwMClXfPB_Y-5MI768w_5sLhoR92BCf60jfjpMtvKwY39Pf1VZaQ8L1TbK6t977ZZ9ct-7QkDZMwxOCCe8RalOovdABQyz3rx40XrRSAb9lahN57mKZGoXXJuduIz1MOG4VRBRxaqCvtJuTe-UnqE9XVCkmcVvJRugwes1VhQe1soSUKx9jeWDx03dko-zp9doezzRJRHyj6Qj4kf09AXMEVoyuOyjJwE-j0mZKZ9UuM0w80NZRgF-m0fHlpHFrFeI-FZYcgIkID3bXua2CDQu5bAajlPKCJ1B-PwvqhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=SjA_iqv4ePgLZn26Xs5aQ2aRsM_3RWHxbHWW4TWaMBd85RhXhUOIjop64IOYvEvz4vYP8ypIy8Qe9K17nPWZCZCyUEJ8AuT3nMweAg3oK2HDKxhVUbllk5wEDd-nCd000CRxrJ9-ZTMrwwYa511DLFOqnDe9pfIyVQOjK-8aBGUJXX91IOhPFzhA_xTcc9KCqT9DkZjVcMuWJt84p0q0mYvUy9rgPWZ6MYrpkV5MZf7wCays4-HZSbMwNbMo4LmH89ocGi9k9pMZBewUcfL86C_EXIhHwzhAp4rmmuOnTDo2wPAcuN0OYxO6GFLgPYACYQv2hfYMdVMbnRtQGI_SXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=SjA_iqv4ePgLZn26Xs5aQ2aRsM_3RWHxbHWW4TWaMBd85RhXhUOIjop64IOYvEvz4vYP8ypIy8Qe9K17nPWZCZCyUEJ8AuT3nMweAg3oK2HDKxhVUbllk5wEDd-nCd000CRxrJ9-ZTMrwwYa511DLFOqnDe9pfIyVQOjK-8aBGUJXX91IOhPFzhA_xTcc9KCqT9DkZjVcMuWJt84p0q0mYvUy9rgPWZ6MYrpkV5MZf7wCays4-HZSbMwNbMo4LmH89ocGi9k9pMZBewUcfL86C_EXIhHwzhAp4rmmuOnTDo2wPAcuN0OYxO6GFLgPYACYQv2hfYMdVMbnRtQGI_SXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dpQo9WUTmnBzK2BnnIGx3PRHVTIyg4w4n8cShdypKyOyKSYrZmlqLCkE9Pc4Hxf2Q1eu5XgkGwab_vxCO6EwTbJ0QTa-x-wtmQ4wGRFCkWwlzC-j04XXOtbzlAa9DL2_1i9_ET4eTIYumVLlFv7dGgwdLz9HSnYOnRSWh12DCO7C-QYpFqEF8S8j9EvHOHSaq8iAaqjtIi0TSSwUoIc-vmLL6EDWr6RqxIDY0qLATIypLjO4iXuhD2KnEwaEkEqvp8F3izpulgkkiTHPS4XkEcYvmpjOttyuVFZYQHl1JVmd9Q6KlnodOUl2A8Wjxlm-5-YPPeorf-GWJf7SHOXOfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J60mA-KoqXRpB2thUx7SW26edvl4TnXAS4ianAM5kHmC0twGAxkp8GltKyeYY0ntWsYcQ9I_T2XTdtIeSuYffvTRpCDdfhADIVgYWeRmgbICBHEuKbXetMhVRyCq4_By-zuou9Ks62xJx_CdQYdVYfMr9zEAHrh4QGqytIvzCYkhU9w-EOj5EKXjWRHisFgtlKglHZhXBn8xPn6WceNv3xqidbHySwZBy3RiVcag2B1zo2ourTEq7A8Ii9_y6Q0Huh8b5urt37rxTDPbG1Q0F07YrMYwSQBNPc57xTjq92DY6t11tGFANZ6rzQlMnekQS6ZFx69CrYz2DftC0XaJJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=uHMXX1ii0o5xPYfv-Nc3GlyvrkjLsY2S-x5Qm3fZs9pVv2R3ZuFm47gwQGmr_lekXt_BPK6XNHichHromWvrEm-L3yNbBpeodvcoTqYuytxQmOli2MyS3YQLSy5_SdBz3L-geo6kp88kvppQqO0GfjOV2sNM4GPVge4UT_U9CTzPKeCuGhSMc9aQGVMggLcd1VvPnudJ9htX4qSlniF_21dtafpnELC1nhXzFI8Zp9kk2AjniPR7W8gsOcOFbs3zTsi-NfKuDiMilZNQaAYDAWfyqjPOnAT96WlS6CGqK7tJSQCSrfIm1mu5RyLYC3NTz0Jpb975Ao4bcdjLtiEdNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=uHMXX1ii0o5xPYfv-Nc3GlyvrkjLsY2S-x5Qm3fZs9pVv2R3ZuFm47gwQGmr_lekXt_BPK6XNHichHromWvrEm-L3yNbBpeodvcoTqYuytxQmOli2MyS3YQLSy5_SdBz3L-geo6kp88kvppQqO0GfjOV2sNM4GPVge4UT_U9CTzPKeCuGhSMc9aQGVMggLcd1VvPnudJ9htX4qSlniF_21dtafpnELC1nhXzFI8Zp9kk2AjniPR7W8gsOcOFbs3zTsi-NfKuDiMilZNQaAYDAWfyqjPOnAT96WlS6CGqK7tJSQCSrfIm1mu5RyLYC3NTz0Jpb975Ao4bcdjLtiEdNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHoVypAB039_LqjQy0hKEgLFXM0EWM9Z0yw-oH6rWAIx-I6M_CL97rqhmsldYsy9w_o7Ssfg9N_xRz4EKv5p3lsuk1KGvEMGOAAkpJcFz1yjecS0v6Y5fQGDIgLsy_AjHLeCF7UbyJN7_kHsESk8X8R5C8gZ1_TzDqi3PE-DzFSwzYG4LRY5BuNoVPzswkhE2EEpEL9n4NMFljF3-1iV5e3WtG_Sv48QANvTeMp2tJK7hJ8nSXqccYhO69L59WXaVFOv316uDpzFGcznNYUhQ2tt_6g9jms1KJ6Yzjo-e9CNn0uXK9td1ZRxp9eAwyVCEUdVdB-MtQDmp-FlwpKCrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orw5gG2-foR3FPO8Pu5wWqZzeNWsLmI3WqKIyc4QFIwhiHI0OpM-kzpre2XqxDN6b35E6Q2dajEZ_3A3I-Ubn4x0Jo8H6iYR_9cpY2KRuBuc3qETbEOEBkHIToS9K3ZvOsTj2oBCHBBIEwyIO6DWYfuXn_upObR-z0vVeUhFW5ji8tAEw9hw1Uy9neOtr--Q19CXMrzrLgcu3ZedhoUBh_fffQ68PJKf4TB69sELb7vZ2fks-sG6qnvvpLb5ak47LTEfLEd9al-cmRIrjmryn4hewUr-BewYh-O87LEaERq9JwhjDHG0oVyaBgwrxpJQ8YBhK2nEJ20cJY2s52iGpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMgJb7p3gfbltya6VcBl1OhB7dOIk8fZ8_kEs6tI0N9cIV5W1S7BUvVc9qK3PHjPQfwZoqVgE97hHtV4z0keF1wBZAWGJvLtlM3GBMYF523TUZ0DEIf27qhh8JryQUkUc7LEWmjVP2pvlmayHLm7XhYlvp4yuopUKGlDERA--4cHvA1YLT7ImWtRP8oqHTnQ26GehecSzziH1YuMNPZ-7ZoIRcKd96IyFvEq7J-ZFGDSNom92woqwGDu0E511Yk_NcIRbXeJx-Ww5gpXqLM9rVuhqi9tZcAkR0Rpt4fCOoZ4K2hte7n3OvKd5wWUhIP7QOfjBYV-MJyWts5b9vGsRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=FTK1_N45HkAZgPdhzXfJboYMTN3KsZia8eRpuDKyI9VAueVUl4AadYf9dADR2kXjeMWu2ykRiUeBw4EkOlL8ywM9Px_hCDzCcqtXIvNMOVVlXSr6dSfng_OTe1cOfO-9iiM-J7S1rwKsOkCwDhb3a67PRhf7y6rRGZ9PosPc7su1VOT3T2j6GDylScluFEKkNklo5bjzo72UN_3D9Q4ZjCixDoQQoRzbdOD4MCP2CP82aAJkrUfLje2jJjvn9DBaAEjd5FydfMtv-gh1dTGghFjml7i6SerKdTUxMYyQUGHV2-6Tfky5yB-dobtqlUOn6M15JTuXcOffDQwMwdkXeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=FTK1_N45HkAZgPdhzXfJboYMTN3KsZia8eRpuDKyI9VAueVUl4AadYf9dADR2kXjeMWu2ykRiUeBw4EkOlL8ywM9Px_hCDzCcqtXIvNMOVVlXSr6dSfng_OTe1cOfO-9iiM-J7S1rwKsOkCwDhb3a67PRhf7y6rRGZ9PosPc7su1VOT3T2j6GDylScluFEKkNklo5bjzo72UN_3D9Q4ZjCixDoQQoRzbdOD4MCP2CP82aAJkrUfLje2jJjvn9DBaAEjd5FydfMtv-gh1dTGghFjml7i6SerKdTUxMYyQUGHV2-6Tfky5yB-dobtqlUOn6M15JTuXcOffDQwMwdkXeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=ATvbegffPYyEauCrixFxoy-7KBT3GzOPNz3kJDo9rNTm-OsfsNU6F6fhPtV-ILwNOm0NRhSOjPFs78pBr75PhC6U9aall4YSP6MLdePnzjeIOWHuon2xDjk7OHEbsDSDpwBewi2ABlXQQLvMVgYbh5ky0Ylbobe91XyxKOaZORD-fVmKeMXA2JPsG-5yvpfeLHI5wpmX8C6pMw59MRDra3S_M8C5xO-whQ8-uOd7FJYR7kahPqYtnJ0Lc9ztxtsksK_WOSRGPmHFJI0tiHk1vR0cjjd0RAUCw1ceioeILgqiC80_BqjgXzxoDzLPLf6ZFJAxw9b2qr0vKhkOc7dzoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=ATvbegffPYyEauCrixFxoy-7KBT3GzOPNz3kJDo9rNTm-OsfsNU6F6fhPtV-ILwNOm0NRhSOjPFs78pBr75PhC6U9aall4YSP6MLdePnzjeIOWHuon2xDjk7OHEbsDSDpwBewi2ABlXQQLvMVgYbh5ky0Ylbobe91XyxKOaZORD-fVmKeMXA2JPsG-5yvpfeLHI5wpmX8C6pMw59MRDra3S_M8C5xO-whQ8-uOd7FJYR7kahPqYtnJ0Lc9ztxtsksK_WOSRGPmHFJI0tiHk1vR0cjjd0RAUCw1ceioeILgqiC80_BqjgXzxoDzLPLf6ZFJAxw9b2qr0vKhkOc7dzoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=oDNc614bZvv3SI9AWc3BT-3w66WqVJeim4rAP0-S6DMJnzhSJqueyyJ4i4MUzZTlqONWo_Mxckw6XorMhm72dEfm7gQwRL2MDdrV74kj90vfDp2Vyo8x06LPiYRyWbX4U50hwac3w4zu0KBnvhGDnsNeZUfCVSpUY1ZHjAUc07MsypdL4n8FVHx1CX0tLVhupgaGOQmuO6HfMeQBFFX9qvhsExkqECAK9p8H-0oYUmrdr-ySzvYryxMtOkUZnpY1GzG03PmsOSPSAv1Z1yCmE01AnFK_dLYfv2kn-tlzQQ2r4kbz6DUXTeqt6n7K_PNh3xUpYHH2frTZ_Y5-8SrnG3s1v_a-kytfvUbY3KZtK_dJfo_H8Qe4f3sXIGzi6H94pfQh1qjp5-2xrDhL3KuOJDEXRtsVJON1wlbUVHQuZCYjd21xuqNa0qHoIMxpz239Mph0uDWmP7gMt50a9wqJPN5kysMyv_BQnIyjIyDQ9ssakvYaVbeEVuKtp24g6v3kOaufptr3DBb_m1_JufBY6Drl-Hixltt-O4pIRB3jeHcO5cMtzgxQfMzS17J2TopfQi1d5q9lT8-WxZMQ8h58FnlYnr-ds_-QJQSBIS1hJ2Y_rbsxHPli8H6pisOWXwdjZp48T9W3lx6Qs3Jgot9AaekSTfxeuYAHemJr6queTJs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=oDNc614bZvv3SI9AWc3BT-3w66WqVJeim4rAP0-S6DMJnzhSJqueyyJ4i4MUzZTlqONWo_Mxckw6XorMhm72dEfm7gQwRL2MDdrV74kj90vfDp2Vyo8x06LPiYRyWbX4U50hwac3w4zu0KBnvhGDnsNeZUfCVSpUY1ZHjAUc07MsypdL4n8FVHx1CX0tLVhupgaGOQmuO6HfMeQBFFX9qvhsExkqECAK9p8H-0oYUmrdr-ySzvYryxMtOkUZnpY1GzG03PmsOSPSAv1Z1yCmE01AnFK_dLYfv2kn-tlzQQ2r4kbz6DUXTeqt6n7K_PNh3xUpYHH2frTZ_Y5-8SrnG3s1v_a-kytfvUbY3KZtK_dJfo_H8Qe4f3sXIGzi6H94pfQh1qjp5-2xrDhL3KuOJDEXRtsVJON1wlbUVHQuZCYjd21xuqNa0qHoIMxpz239Mph0uDWmP7gMt50a9wqJPN5kysMyv_BQnIyjIyDQ9ssakvYaVbeEVuKtp24g6v3kOaufptr3DBb_m1_JufBY6Drl-Hixltt-O4pIRB3jeHcO5cMtzgxQfMzS17J2TopfQi1d5q9lT8-WxZMQ8h58FnlYnr-ds_-QJQSBIS1hJ2Y_rbsxHPli8H6pisOWXwdjZp48T9W3lx6Qs3Jgot9AaekSTfxeuYAHemJr6queTJs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=rAfk0Af98qfh53bIjzlu4nXzW2yDybIEE6S5i3FMHAU4HhJ6MHNUgc-SVI5prd_gSsFsIl7TK3jNnAbPY93khURAPB8-75bBbWmCd337qM5ekETVdV7HpK9RXOUWAjntvilokELQhUZ3-hRf_rWx_kV0z3bOCxarTQn86sn6REvTG-D6CgySieXTMQQb8caHO6zHAbkhxH9D-oxv7zyn-e5jc166wmMdqWHIUPadSFzXtuAK9E5KtxXulUYXT3uorVz3UIXKmGmxWU--3oCZw5yDvkBHAwzeUEuctwuEVpT-_knuFIT5f4n2wfEX3wf114I1E46yacztkHcqO01_yjH11fTVzNxmtHACTdaP5_bcob31kOB6gzrjAXPQOik5Zh-K49I1cJv6W4kaVXtkyYDA7ad1dhOLDlgo8HRNrTTMe-M_xlsRObD75NPyo1469IdQY7uZlUizgFQxm-0Ua0Nny3ZJAqyfx7PvWngYUK76eKBZVFnces54kZqRTBEr9K6MtsXYGywnDbsjutj5ICUfmyXW-vEe3CxWWvll3oCpJRsFw7TBghh-XwIqI0k5rRL7VOdHeAnpQG8ae5K2qy_J8-CccvOxJvP8QY_XPm205At8ILUFyJZzmobWHuEuHYZRNxx263EC2E6hWMokX5FWpsIM6OsZapXVQVIWfzY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=rAfk0Af98qfh53bIjzlu4nXzW2yDybIEE6S5i3FMHAU4HhJ6MHNUgc-SVI5prd_gSsFsIl7TK3jNnAbPY93khURAPB8-75bBbWmCd337qM5ekETVdV7HpK9RXOUWAjntvilokELQhUZ3-hRf_rWx_kV0z3bOCxarTQn86sn6REvTG-D6CgySieXTMQQb8caHO6zHAbkhxH9D-oxv7zyn-e5jc166wmMdqWHIUPadSFzXtuAK9E5KtxXulUYXT3uorVz3UIXKmGmxWU--3oCZw5yDvkBHAwzeUEuctwuEVpT-_knuFIT5f4n2wfEX3wf114I1E46yacztkHcqO01_yjH11fTVzNxmtHACTdaP5_bcob31kOB6gzrjAXPQOik5Zh-K49I1cJv6W4kaVXtkyYDA7ad1dhOLDlgo8HRNrTTMe-M_xlsRObD75NPyo1469IdQY7uZlUizgFQxm-0Ua0Nny3ZJAqyfx7PvWngYUK76eKBZVFnces54kZqRTBEr9K6MtsXYGywnDbsjutj5ICUfmyXW-vEe3CxWWvll3oCpJRsFw7TBghh-XwIqI0k5rRL7VOdHeAnpQG8ae5K2qy_J8-CccvOxJvP8QY_XPm205At8ILUFyJZzmobWHuEuHYZRNxx263EC2E6hWMokX5FWpsIM6OsZapXVQVIWfzY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=o5fcYJpPLt1tuT_ueAv_OrAX2TxV9gdOaL6_BFwUg7FqN6TdHlCeezb8niUaxqxsAehzuahlnHnFOHRJ8_pzwmla3KctwhanGQUNYuwOJKkj37lQRMDmqQW8mEHLyoP-AxUbs-Dkp9X2glqt17WFm8s-mckrBQRmg9gsOnelXStHpJmnzMd52JSmUOzbQVY5_6o1x5RqkpOUdI_x96zS96kpcbVBAemC35fWLAMj1jbSZIqTlC2_0K_1st28XaKq5FTEWl65Umlnic_q0INhphKMvC4hTIUn40A3CwycSuHNBMIsuxUJl7b0cP5gS-CVkpj5J4_QS3oPP05pn4GU4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=o5fcYJpPLt1tuT_ueAv_OrAX2TxV9gdOaL6_BFwUg7FqN6TdHlCeezb8niUaxqxsAehzuahlnHnFOHRJ8_pzwmla3KctwhanGQUNYuwOJKkj37lQRMDmqQW8mEHLyoP-AxUbs-Dkp9X2glqt17WFm8s-mckrBQRmg9gsOnelXStHpJmnzMd52JSmUOzbQVY5_6o1x5RqkpOUdI_x96zS96kpcbVBAemC35fWLAMj1jbSZIqTlC2_0K_1st28XaKq5FTEWl65Umlnic_q0INhphKMvC4hTIUn40A3CwycSuHNBMIsuxUJl7b0cP5gS-CVkpj5J4_QS3oPP05pn4GU4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBK6aOmDKwpmDTfj_Mt_SkYrU09GG7lrKia9G0eoPFBX-wQ8UAO1X2tZKZf-31BkADlpZMTopP_QtwzCW3CTNiVpWBC1g4jFTCf5tpUHEf2L9gSj8IW1nWHpeDbzwvY_e4CWmECY0YtVtmuLWVgU5qGzMHyRoo_xU4mwQ0rIblo0I0w1bBzbRGIyv9shgq3rFkj-n8yjPXtQj8W1YeEr1ufyIBKj3VKzmpNzrBd1FmXM3HZGmfSBMZNKXZfhUH9zCTrQMBtGyjhQRDxLh24wtFbJ3uLCJT1qk4tNdRNLlf2xFcV-bq-Z57CzZyShGFlcexYLEGXW7O353T3zlMY-DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=KeGeroUz5QpjSiZuqq8ou4zpUIYF2SQ95-2SKobl8lknSGiSxgRY4R_rY8vjlfJLcSAA4YaXkBP0xCWxCPcQcJRhETMH1X1Zu3eDB8moQGuGqR-w5AGakT6aWzbWLHvSHU3NuQslKfTmGtM3qb4OrrT1knxiTO1LmV4TT7mNnhpY5sEAdDl5mw-gCHh2tpfN9LRXvzq6HhQ7VdaCZR2Ns0t069KxJJuAw0baeHFgvgA6spUCoEuU4CLC4YJDMajEfP9Qik2nS8VRYVzOrwrLN7lNtYRjl79uHk1IfvOI82B6-tJBoKXuZpc376Pf4TbbQHJ3REx3S-srDWrGMBAkfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=KeGeroUz5QpjSiZuqq8ou4zpUIYF2SQ95-2SKobl8lknSGiSxgRY4R_rY8vjlfJLcSAA4YaXkBP0xCWxCPcQcJRhETMH1X1Zu3eDB8moQGuGqR-w5AGakT6aWzbWLHvSHU3NuQslKfTmGtM3qb4OrrT1knxiTO1LmV4TT7mNnhpY5sEAdDl5mw-gCHh2tpfN9LRXvzq6HhQ7VdaCZR2Ns0t069KxJJuAw0baeHFgvgA6spUCoEuU4CLC4YJDMajEfP9Qik2nS8VRYVzOrwrLN7lNtYRjl79uHk1IfvOI82B6-tJBoKXuZpc376Pf4TbbQHJ3REx3S-srDWrGMBAkfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=j0hhoE8pwxtHq8IdnXkzJ5I1hlGWcXvD4O-j9OOC9-_B8xFd18h4EMyBtVvtL9qLDP1N11FdkIlDV4o8dngHIgi_FaouFvWRxqJjfSuSo-dssH_dw2LQCPrK9FalClWepIyCbLXTuwXWUWlQfrML9ucyWN-e1GtnW0PUpKX18cHKZr5KzdNDg5J2GdwoX2P6qF-5TZg-Psb2TukF7tBCjba7-0058b3FzOPQoe_4i4oq03yf-K0Gjgt1U2DGGU3ntwCb62jbxTEYf7SpXRICKgCPIc69aHo-6C4xQWOPPU9vVOSPRbjUzTTXbpwiQYAG85ioFgflRa3vYI1nPjrj0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=j0hhoE8pwxtHq8IdnXkzJ5I1hlGWcXvD4O-j9OOC9-_B8xFd18h4EMyBtVvtL9qLDP1N11FdkIlDV4o8dngHIgi_FaouFvWRxqJjfSuSo-dssH_dw2LQCPrK9FalClWepIyCbLXTuwXWUWlQfrML9ucyWN-e1GtnW0PUpKX18cHKZr5KzdNDg5J2GdwoX2P6qF-5TZg-Psb2TukF7tBCjba7-0058b3FzOPQoe_4i4oq03yf-K0Gjgt1U2DGGU3ntwCb62jbxTEYf7SpXRICKgCPIc69aHo-6C4xQWOPPU9vVOSPRbjUzTTXbpwiQYAG85ioFgflRa3vYI1nPjrj0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L55BAMi1LCvlpTcVgpIRVthIeADxmuyCBDs7_ZPDQgo1oZ-xWaetPDsnbYVR2h9Bk-sJ7-yzqtKginJUnOw_KsoraVPTvDQ9rbv2Cu21DHj4hSWPLmcMPmbLcAEGpzH4Ak2uitNdjVrQIkYBPf1XRc2xIUZwF5KVFtcZLLfTwtXDBH1W2NhzwqErKc69srZKBRp-XNkRrq-UNXSQiVMMwXuSRUX-sRguHHTBO0EN_cNvXVcI9TqKgxSxokyEZZTqZeppq6VcITK7D2QUsKcipWx_UW2XWmt0vB_knaVU97Jg7fTQw8IEc_JPvm4DrO2Wlva0h-cllsc-IitdPOEHdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQ8A7XXW8eYCCt7ThbKWxlLDAIT5D9sicfhFKG0FlFiAf8la6HjWd_nPqGSSxRIgXt3BB5G_2LW2uACgbB_PqKQFydmuvdIRahCEPr7o-avhSl_53xdccT1GxQZU4100x5cwjrHNyua5kf_P5lNr7kthbtHAAyqEK-9ztCXZ1qHXBOjsP_9Bo5Iz-79LQHUuqYwrTAtDW0gCgJUGEn3QCv9e7tdL-PNM9HRtbvrJmDX7R7FwzZnW5n5xHcww45MWYmbtnFfpqUO9mDf1xkZ-bm1BCkuv8SVLo1yhG7ZWPBg3J1L4ragfJnCdPILv0S2Z24KbrMDTDllXMYdV63t3sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1ISrvrvt8klw2GYaBOfCBr4pl3M27JCttW6lxAbOxNsNsM5GYVNetf2CZt1ocPBS125VSPRqzzzODILEmDFV7fVyuK_f3EdtTcf3cliGLx5TDU7bOZBOP3wmXuGkiG8pRPRBVsOe6MFSjfY5BHz9lnh1WgBlUZbvoNZl2kQhGDjQbC9AuvS_t3tv_KWmNwQAnu_IDHsDhn7OG8lettgkaWhPSzSpkmGerP8cpSnGeOFaLw6YZRZMrMhP__OiqtgwRQhESf_C_42uoIjvP73XfpPv9ktwvIodJ_K5mAx5bizC2793Ch7F9-pKgB2Fw3EqdeO1GE1m3hEsbsJZOG7Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXGepMrlac-0s9C8MtHvIKK8483HbyzmCPeJAdVt17v_WzIbQNmRYwYjCP8u9IG2ZUgOr0AqJRlzZWMYzuNtcMDtUo4qg1pOZvsHPoCZxvZ8__k5WDxH_C5_2jDGSWtnvbwPEc50pyMRIjtbcRT6y5hSZWunZubGxbt2cHIhMNydciwavLsLvdXCrVOtzc4JGDwROiL41UYNFY2wj9_2zH_1tkAaRpjrRNuMoJGMqNskM7NlA9vRf3Z_ZlxsExjY-qjU-2Jyr4abx33ww71Eb8KsQN27qhl6PcWfUPR2frYRby3zK0B9xOs0vrZEOFiKIP3imBb6SvLSn2G6PRDq7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_DH7rOt2A_xW8Qnc0_8rgcgZYOhTvwjORkHZBVZyCQAZBeZx3xi8s3yc1lYMSAlS-mbSD-5sBa5ZrrgCThhzERJLSGhipzrFfoA0Z8PSmvLzepBdVeBeV9PzbLjYzKS9_mOWkMe1gYD4qTqzPnne5_tWHkem7BlnVQbypuQjsaQkPX33DOaa1O8unZJ_UgLu-tfJTdcseSECiBWDIo2pEUVsnLq3xAktoXnmq4dxWu4GGXZzdJxsf4nb0AqSIOYP0QKia9HGnLRtQCm6QqXUMTFc_VtYqcjXv34DC2UqpWQCF3QeyIhyzUjIWpZeqBdmq8OWS9rbiZitH4wpS3Pyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DORBMEogQ7fJ0mz2TBXLJi6sgg72W2mwJDgRu1afxXL5KKRcp0NYgucqjf79x1ZMwuW9I046UGF6ztUNusWKt1HJLVgJyNfZ6fFvy4lgVC08lj9vDh-PDfcJA6a8zkj55NBTY0p6Ypdxwqt2Zv5iedd7sXLm4r-X33M1fF13HGIsFxd5wPtIuo0Kb26DLQTAR1cnMJKvhoMmVQSvTJvnWX0rlysiuguyByymKVyobJSmNZupUul7yQJg1SFO9XRQDd3vCWkIHkvSb6H2jIMx9KXLzBHd87C9TFdYeKpHB83fJ3WmpNz3tm0lFTmKwMC3qxf2fz83uDanxuCk-zmAYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UknrxJ7LGWuYILBxIXrhZOorTu7nC2Zk8Vy8DKP_hW6WIaSAcCDkQQtz8vFjcCZnk81hpdYLSMM-7kXz-wk4hkiotv66y1BhBHPTK34m4ugpqp-5347F0wWPxySmOU0H6FFS9g1x63dyiYXUPk5EQoTTOQsGtaeqSU_6ecHkf9djCuRpghLehGKiTH8dpj38iVoZCdSZE4c_XoGen2FeSj6n5Yb3DeQhw-8zVWsqiguKGcHaXoP7DZsUS9iFQtL7vGOHuW-YJNpwAKrpLlw357kSAbJRfHo8fLS89-sMVoE-ZblHOTpaLIPc6nrMj90GKg9NfoEmAiFM__W0iLOzyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kokDy-knkIOpk6De2Vvyp0caEtNEy0rYwgiXZPysfeKTNEoOAlms8fKWTU1rAD1kamzqNSWJiyoCo_qKhxXuPC5aJJ4xK9NqlecYSyrxrEyorZ82FMArE5kYIpMY-7MQ5Iczfqo85p9wdetgT-daJJ2zk9YPBbTy2_5dDnEULFBD9k-2wAfazXv4OWK23kEwaHqkEJPuPJh-sabY5mIFRydYcM5zeSGNM_Zkra-OHc72oflGTuU48bJ_EtMJeeifARsKOLh7-6eugb7aQTmX38oHCSgJRu1mLokLbWbINjnid3xPWjPBVkTH2zr1IKJYJNZrxPZXHESGm3NGG_GnuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kvytCJlCbemJt0MkmNm4NCvWZbOB6bg6ttTkyT0TTj7kh4KxvX9MyBvrVTN1qMihhRSYkSDQwHqDuPk6orYmNtw38k98jCQol0wukCHU6m8niEUY78D8UKxiU9DgpLsYV3KZ4D4NgtUCGKwqUSXOv0hU4IQr6ul3OvDQPYQJD1JxhOvCNX82F9GBveDcQ_RxndHeirWuICbWPt4ajdSQnIlx57YIUUtWrCBbHeyDQwcwzUmxgz-MuczWF7vglQgHaWnzmpCucIPhaQEPVqaYt_12EsN6GM04vWCt8zS03aW0IDJuYL54sXDICFBiZqe_LxsPYetcgaTruaNAVeAqww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KcKeR90ir8FPiDKZVyw6-QpsNQZxntuOzkvkLeA2n7aPNGKaFyOyD_R9lHkQe_ghkdPyrev1imT5Vw5qsBrM2opA7jWE8O88OOml3Y29vPA8JgeQMY34Ua4lTwBH1SboQR6l3cvJq5WMeEjPE1yKIr6eTx1jVUNkzrFWBSTwCb21ayBJEOrHHp-1sRgu6MVScJLCL7bQVxRV5wFE6IbQiQB26V7YFKEWqYPUiaOSGCXIRp-zlFxXdlq75kcX-uluQ7EagMAbMez-__848U_ltux3U6FIPgWlzG3ovIIF8QKIm02cx7FhdffNo2yQlhWSR9uK0yc3IagoxzUkfXG2_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=pk5u602vj7Q5C7v98yu0kAB22NFx4GHShfNtTzXJRp0-vPKG-49en3euNbaaqYF0wvD-QqJ_I78K5elxz_IQ9xE7bKPzos5ytEcR2d3ygHjkNB1DIrsK4ia3P2KzLmYYp2BLp1zCYOfEHVmybpO6QJh_02IH_rZ8GgRkZZwK7ZSH0cvHgjTKuIQIODfQH22r4JDwthEC2AXNpR-9Jp88Jw8e5UeNtGlNf1bzRoG2w4DTO7FfpN6U6yJ2D1GzpynBzL8sl6lkkcM_Q5lWyApyDoJBl6eMwDp82E45Xz28N__pYBCJUX3DyZIHE53rmCrszXF4hC4tOtALosPNB4R41A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=pk5u602vj7Q5C7v98yu0kAB22NFx4GHShfNtTzXJRp0-vPKG-49en3euNbaaqYF0wvD-QqJ_I78K5elxz_IQ9xE7bKPzos5ytEcR2d3ygHjkNB1DIrsK4ia3P2KzLmYYp2BLp1zCYOfEHVmybpO6QJh_02IH_rZ8GgRkZZwK7ZSH0cvHgjTKuIQIODfQH22r4JDwthEC2AXNpR-9Jp88Jw8e5UeNtGlNf1bzRoG2w4DTO7FfpN6U6yJ2D1GzpynBzL8sl6lkkcM_Q5lWyApyDoJBl6eMwDp82E45Xz28N__pYBCJUX3DyZIHE53rmCrszXF4hC4tOtALosPNB4R41A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aO3ufJDClAxPDXJ5Fsngwrj_Pzc8-jNWJ6y9LzOJBBMeHFQLk_kznlNmLJa1cRnS8Sd8iCwqkaPhEc3VIUXRUToradeUZ8OAW5I4DR2mrVSgRxOApqLWgHz7N4si-ZLajdSh-_h8RFil4ZRGGntC5NylaNASZdXc0m5GnSBezMsWHSgJ6QTeu3zDir7YzW6PE_LCIA9kjsZ05q3h03It12b7fZnBFruCOFXBix1hYaVf7JYQm-uPiU7SH-l_bdDiQGoF72QY0hZgF6iDIKC1vMPOE8KOnsHzPnXpPJ6ScFrzjbIEvu4KrIfX2ZEvyWxejU6D9-AI7Q7cEWdv9S22sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LW7GCA5vUru7dWrEmKUdR3XLoTML5-IOeJdmVLg8QbER4uFdOQJ2N0TSnA38772J_sBGzVPe8dvtUvJlMmUxx0pixg_jpAdZF_LK16UgpqbUq9pgtgCNuPoX7VnGUltuNcxfp4lBWERvJtSmfEZ2veRedAanj9qZPBJ2qBsTlUwpPtITtyO92PR0eYFdhA9TFBa0FwkXn_HDm79d0yxsR_zSkowCSTVBNdIsRsSGcOp7PtbqagbWOC-HeuHMlPCh7OGIkbV30QD1Lm9QskCMc1wtrij0nCGJtWj7ny6FHxn7udQwo-OWU3FXBvNYX-qGFHi4unG9RVfY0_hw7eDIbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=E-cTvtmwaEbiq5no6HVh2HjaDBsgh67IRo84QDY7OMbwsvdwH2VJcykx-rsR5IFRNAw-OJ0FhYcLp45xgepIFmRHJjZkLhFc4n-0CdUKV5cMdbxKrTUAi69clLIYb_uUA7vk9H-215AcETjq82_1qzBeT0YAiBhH_0QKrJdjVEDzl3fjUF0ziaIGi6kOmZzRuzek8wm8V7oUDDSebfUIDnomsExHJUBCfV7Owt8SxZbC9WXuV6kwu0Aw3QjiXsvVu9zZIxPoXHMpyCrjfNw5j0_uRacufu67fRL_Pj_68etpqKd0Laxm8EN0hxLi_6zdgSoZl-BWve9W-b82LFCURA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=E-cTvtmwaEbiq5no6HVh2HjaDBsgh67IRo84QDY7OMbwsvdwH2VJcykx-rsR5IFRNAw-OJ0FhYcLp45xgepIFmRHJjZkLhFc4n-0CdUKV5cMdbxKrTUAi69clLIYb_uUA7vk9H-215AcETjq82_1qzBeT0YAiBhH_0QKrJdjVEDzl3fjUF0ziaIGi6kOmZzRuzek8wm8V7oUDDSebfUIDnomsExHJUBCfV7Owt8SxZbC9WXuV6kwu0Aw3QjiXsvVu9zZIxPoXHMpyCrjfNw5j0_uRacufu67fRL_Pj_68etpqKd0Laxm8EN0hxLi_6zdgSoZl-BWve9W-b82LFCURA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=VPZMPWTYuQ1ci8gz2AJ52Nt2r95Z-5KtYryVveus3X-NXfXreVdSBLdMDLr8pmM4Sn60SZveOed8MGU1ra2nvF3c0hquRIIuF9DgVnNkZOO8-CjtKwEi1oK47oUodoGrbPKrdY1VHgWl-XPQDRVQfqhPvEpdXpTvrFfe-XzOPv17mGVDfuVPfJmOUoNVmfpESqnCpJyiSHRqrcRe0WnDq6PVuT8PTxo7W5NoQUgDvxwvI33C0Ji5CfGR80TbI4m_QEnL3S7ImJ0gG9DcCYDhmEGwBXLWzUTf4vuFYcgPmyuMcPKxOb2ng6hbExPMT6DX4M4e7cXgikGPl_Yl-ZL9XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=VPZMPWTYuQ1ci8gz2AJ52Nt2r95Z-5KtYryVveus3X-NXfXreVdSBLdMDLr8pmM4Sn60SZveOed8MGU1ra2nvF3c0hquRIIuF9DgVnNkZOO8-CjtKwEi1oK47oUodoGrbPKrdY1VHgWl-XPQDRVQfqhPvEpdXpTvrFfe-XzOPv17mGVDfuVPfJmOUoNVmfpESqnCpJyiSHRqrcRe0WnDq6PVuT8PTxo7W5NoQUgDvxwvI33C0Ji5CfGR80TbI4m_QEnL3S7ImJ0gG9DcCYDhmEGwBXLWzUTf4vuFYcgPmyuMcPKxOb2ng6hbExPMT6DX4M4e7cXgikGPl_Yl-ZL9XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRhfqIwPhzMgLhEDG-FvMinZNsgNSkgcfg5XZ7DZQyB69Cx8_In5CGYCNJG0_o9ewaswQnUhj56IIjURnyOhEbWcW0wIlM9fwfjwYEHP20nAYQfukWNb24igP5Bb_LDc11TUrfNt90A_JHPB2riMrWe3tb5IlbUQDAJN8ULOfrtXqIci3D5TwEoCh5QIq0FsCni_z6KOH0ThAo9pOVrTWw5AIaQnjIwMEkLdBql9UeqArjey4uicI0RBhuZgXBGjMmJIS5ahqN06EVDzUYnAMCJFa8qO9ULWL7YKMBZT8y_wR1uzu19r9u4RvcRjDBFN85GfkYl4IuHwWtXtpp1nlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJLDdwV7UAELK6s5yrXN1wx3kgAj9LOYwaMMa59XdW6uYJBb1Y8a83uAtVYgyzDd_I21i-fH2v0i-SkfH_lhcNaBWOokp2cD-Mgv1A4jOkbvOuM5ZXJ-6KubSS5I56LnP8KojZ0dODGtOuXtMjm8xwXBr_KUzDTeFAgNHEHDn63yQuKb2gpvmegstrAqrsMeKHPDCsvZjil4gcrePRDoHmjwwM_UIGvjSVRfuc15zOkC_ZoilGd0S2wH8p7d5msP-MU_m7SXuQPkUuyGB1Y7LTlgfP0R8n8nmy-FzaSGbn_GpO1Yz_AsdKkKDwakBA0aBnHjGzEaDoyNGabixw1mxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpfb_n6ggvRPm84fbIX9733FHkvxU6xupXN40MN4xNttfAS4UPa5OtHAcUAA3yWwXUdTdNB_TygtauCPyvOrbtbEvGsSV4fAWUnMEmg3jW_BK-hc0YHJ1D32lscwXwH6qcTVteLJNhmvk5hJBdrjNeI5Y0gxRKHdNef7Q7srw-vzK1YFVyLY_-EZuCArF6bkS7W63lFCL0Kak7WKX-xejVXIh5klGxqZvI86_EMfAynkxwtimSF2KbuSho-Mm0pq7rTS23tNfE_W-TsFFobDHmjQBj2VtH45GVitEZP5tkdhGCglErJeiL3iATm99NebU8mCGR9O13Gksn4eZuypCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
