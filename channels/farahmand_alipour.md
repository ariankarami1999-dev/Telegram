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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 13:40:22</div>
<hr>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UniU-uEYV0773F2efC4bfQJnDDp44MlbENld_-xi2zstdhLiwBrzAepqLIQMxW8lI5rZQW3AMcPuS-eYGRRuC7S9Eh20d9-ljfne6EqofLKSnqLW4ieykoI1fDaGKLtz8KCqU9vTsYz9xbdb5mZnUHNIHEOzykJzh0_5UmnT_06in3KLpSQ_7Ap7P2Vz-jfa0bZRZueBh8iWRrlD6okwHSU3yGKjq6_suCoVrHi18Sz4HPkg3Yi0Bu5-lTUUNzp0Nno8pEHjIO1HyVvu3RupNvwes083Ueb-iwkmy3J-FxU0x_FrFZxjDx9kNEx0Htec2xjDPzl2iLtzqanrreR7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=glDRJTdZEiezms-vXMOE-bqmjSFv87zuhlSGNJx1Vl_XsQRwpHq3KvcCh99eABn4pMfZdE3BVRrGP3N9XbGbXg01F4voUW04uhI9jOM3YHM3sCamadLb02jOvfiN8aCoHhpaiJ7RH1ERk__NLhazciPygO1qrz-_vNsbSP2FRQN3M88prtk1-ZMgvFQCMgccLOt2QcV4d9yOIp1GuXmq-iXb1YW-b0GfjZzeCj7lADn-ozAwlA2CqqqxuQ8SCgzJEzJVmxq0DCgojHKcEfepH5hOuMWLnJIbFsJf4g_IEMv3HUS9gBnxqOtbFiE0OjnNXWOP-pBmjiPnQUmvwkhHzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=glDRJTdZEiezms-vXMOE-bqmjSFv87zuhlSGNJx1Vl_XsQRwpHq3KvcCh99eABn4pMfZdE3BVRrGP3N9XbGbXg01F4voUW04uhI9jOM3YHM3sCamadLb02jOvfiN8aCoHhpaiJ7RH1ERk__NLhazciPygO1qrz-_vNsbSP2FRQN3M88prtk1-ZMgvFQCMgccLOt2QcV4d9yOIp1GuXmq-iXb1YW-b0GfjZzeCj7lADn-ozAwlA2CqqqxuQ8SCgzJEzJVmxq0DCgojHKcEfepH5hOuMWLnJIbFsJf4g_IEMv3HUS9gBnxqOtbFiE0OjnNXWOP-pBmjiPnQUmvwkhHzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VI8vQEAt-E2li76QtfDcQtnLLw59fr96mn3g24Fyy0rLzQxm_s1yuFheu4JmAEDAl7RqW4W21cawsPnnP-y4dvMqrOFq38dKf4xrMDhuRIcpB4vrzt4JOEfM5FwumePdKEszrSO1q28ZwlSyIEEYzAoFGk2DqpiIIKtP2MfM81LAEiCR4Zl8bHkUTlsB8uTvCcdmgpy4p_BNAIrW00op1OC2J7xPTD7Y2AvRxDadJb_mxXvShL99N6nRgfv-Qo-Q37NpGjmimD_udlsfO3QqawqSWCPMbparTC9rnOUwXUKqYEIY0E2MG1QiSrPb5RoBiEHe-wUuoVLBqUmjK6F-TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu1xqaZJ4lC1nfZ006J3jlYJ2ifMwo18mqeMFQBOkFwUeTOvrDlTSc2pRGD0yPXszCiQhhxuuUSb6AbmI_SPrRgqNX9fWq5-wkfoOrzkRhf0PORLRCCLgFNm2uLlHI2n6gKkdwgkJJyyr9r1u2MgjA-3zbdPJVn5gMiZLbe1m1WH_PGALe-JSE2Xh_LOWHNFDYa3W4NcG2q3l8Lw5a8Thrax2DeJzpdJLnyQ7mujEQqYt5HG7I7cbAczDHLGnV12-I2_CJEqaBZ0ufsNt4uBXjdq70rC_UMHC4r7y7fXz_PDOjSGGktgl9nMUu0qZcssUeB07gxKSEMa0xA76JFGoE3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu1xqaZJ4lC1nfZ006J3jlYJ2ifMwo18mqeMFQBOkFwUeTOvrDlTSc2pRGD0yPXszCiQhhxuuUSb6AbmI_SPrRgqNX9fWq5-wkfoOrzkRhf0PORLRCCLgFNm2uLlHI2n6gKkdwgkJJyyr9r1u2MgjA-3zbdPJVn5gMiZLbe1m1WH_PGALe-JSE2Xh_LOWHNFDYa3W4NcG2q3l8Lw5a8Thrax2DeJzpdJLnyQ7mujEQqYt5HG7I7cbAczDHLGnV12-I2_CJEqaBZ0ufsNt4uBXjdq70rC_UMHC4r7y7fXz_PDOjSGGktgl9nMUu0qZcssUeB07gxKSEMa0xA76JFGoE3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=ncCnt_2_yPeEIq2SIbaCcaICSVKOd5Gfgf8cXrshp0Je4mD64y6zZ03AVCMDU8mBxKmmgjpHU-KvcUIl78mkdTkDRNYaseqSILxfk_jQMWnMaTSP7SHUR5Muoto8vLNg2eL-cNYF2504UzmNs83bCFZ98wG__FVIcMNFk2zJAbDyIeyjbDCjIUOUcZrgYgKD7PslImL1D_mumr45NTWFjvleXM-RrC67O-p1hRoiLRo4BsWOGFj2gtjdTaHsn47E-g4ikpXqDpBg3E4ziBEPATLadDWKxwWH7E6QIMu9xUpUZkWH6vnB9OJuliG3RP2sywUR-t7_Bi2P8TwrbX3-7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=ncCnt_2_yPeEIq2SIbaCcaICSVKOd5Gfgf8cXrshp0Je4mD64y6zZ03AVCMDU8mBxKmmgjpHU-KvcUIl78mkdTkDRNYaseqSILxfk_jQMWnMaTSP7SHUR5Muoto8vLNg2eL-cNYF2504UzmNs83bCFZ98wG__FVIcMNFk2zJAbDyIeyjbDCjIUOUcZrgYgKD7PslImL1D_mumr45NTWFjvleXM-RrC67O-p1hRoiLRo4BsWOGFj2gtjdTaHsn47E-g4ikpXqDpBg3E4ziBEPATLadDWKxwWH7E6QIMu9xUpUZkWH6vnB9OJuliG3RP2sywUR-t7_Bi2P8TwrbX3-7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=nWKbOCdCA4uv0Ud_N1HGItoXkeHvsVfdtQN43ZRP5f8mWzxIyblXDQ7nvYGbxgeyHZtoK74gtj6E3niMaxBUqjCbcJOqBQTLqqnyIvlfdTzauNHjYhwrz0n3wmhikixTYZzf0PkzqaRoWSyb5pKxsoHRwIpA-W7YE6O2LW9Sh42O2UBLltLBGo2v9PgVuEZVJtU65QDKv7pJOOeuE7CFym4BHNfwnrL9P1qFU6gqyCF8J92zsEoOwlJDsbCJwzGsAw9CLJAEL58_NyAxt83pcjvUvIJef_OWD3MtFkZuffC5qIa3YQoYwlabjds7kTM38_BYeW4ih4jGTJngooeHEIcCHfaYpGyzwNf898ZdxL1Qra-aJjtfBJ-WmMjkvbXDELLxJ3G86FpScHigzvvb_BLSUjYiKOU0qdtqynixMAZwsFgZokL91Um9vcb_GN5CFGw2nTDmAMrRrMyiZmL91tSMbRo5NZ5idg5w3vdFcsULAbFr9yuPsQDo26taOrzVOhq2mVNspbxWGkZU-5OintmgWTpVJOo2P-g_vX57FcBnUDJBhe5VWC5cS-mR0kacY6ScWYaFAviEOSMiIAOEuIugQp8490H5Z45rZqlobe02pBOET5o7RrV3Mil3VCdqo7_mj4j0S6jDGnRYzPpy39DMq4DDY2uxLGCe6CUZG4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=nWKbOCdCA4uv0Ud_N1HGItoXkeHvsVfdtQN43ZRP5f8mWzxIyblXDQ7nvYGbxgeyHZtoK74gtj6E3niMaxBUqjCbcJOqBQTLqqnyIvlfdTzauNHjYhwrz0n3wmhikixTYZzf0PkzqaRoWSyb5pKxsoHRwIpA-W7YE6O2LW9Sh42O2UBLltLBGo2v9PgVuEZVJtU65QDKv7pJOOeuE7CFym4BHNfwnrL9P1qFU6gqyCF8J92zsEoOwlJDsbCJwzGsAw9CLJAEL58_NyAxt83pcjvUvIJef_OWD3MtFkZuffC5qIa3YQoYwlabjds7kTM38_BYeW4ih4jGTJngooeHEIcCHfaYpGyzwNf898ZdxL1Qra-aJjtfBJ-WmMjkvbXDELLxJ3G86FpScHigzvvb_BLSUjYiKOU0qdtqynixMAZwsFgZokL91Um9vcb_GN5CFGw2nTDmAMrRrMyiZmL91tSMbRo5NZ5idg5w3vdFcsULAbFr9yuPsQDo26taOrzVOhq2mVNspbxWGkZU-5OintmgWTpVJOo2P-g_vX57FcBnUDJBhe5VWC5cS-mR0kacY6ScWYaFAviEOSMiIAOEuIugQp8490H5Z45rZqlobe02pBOET5o7RrV3Mil3VCdqo7_mj4j0S6jDGnRYzPpy39DMq4DDY2uxLGCe6CUZG4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=BxPy6fSNdie7c_vQGSWhB8SkjaISo9nWtEMO5MW7R_P4yc1VuhYKkaReIf2cQoz9lNrljr9jdw61lHfnblO4Xsd4DdkE5yNUWWufehW3JE7d0QVunK5lzl4W_SLQqOu7d-YApxNlUmUnw_B_E0nEDIa7awtmCA3pVW1eY5GUqkrgyxzgBDwHVvJ71pJewvtYx3hPjnzqj6TdZCthEGAEo-2lbJ96PGhyR3GDiUV72aPap1cgTDKrlD1dwkD5DLtS379zGNAQhMHBMC5YGhSbTtZPeoRC5lfdRtyQ8N5jBUCOtkFXRyUv9VNw1eZEaOHnz-CATx2T7278RSI8IxRQnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=BxPy6fSNdie7c_vQGSWhB8SkjaISo9nWtEMO5MW7R_P4yc1VuhYKkaReIf2cQoz9lNrljr9jdw61lHfnblO4Xsd4DdkE5yNUWWufehW3JE7d0QVunK5lzl4W_SLQqOu7d-YApxNlUmUnw_B_E0nEDIa7awtmCA3pVW1eY5GUqkrgyxzgBDwHVvJ71pJewvtYx3hPjnzqj6TdZCthEGAEo-2lbJ96PGhyR3GDiUV72aPap1cgTDKrlD1dwkD5DLtS379zGNAQhMHBMC5YGhSbTtZPeoRC5lfdRtyQ8N5jBUCOtkFXRyUv9VNw1eZEaOHnz-CATx2T7278RSI8IxRQnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttIXj2MSG6rK8Z4s8JsftZRFJRa-xNScrKgzAvPmapmZuyUvLjQGPh0uL1pjHekJrftVNCn1XIdWxQiUggBKRL-q86Lyw9NU2z4HtddHck6lBBiO4RMfpuScaVPIo7ttK_XlOJdWBTrTXJlJ32g4q3dR_iQ4-MMH5j5chhtleQUeEPKtB-7opiJo9NCaZSJ5VEbo2X6kSpeeoauwQkmotMTMrCEkgiXQD2jU0E-tXMh8FWWS_86eET1mKi3CDOfbj4MZyhWhaxYLUmTvXBt8MGfHciMq8k3pXbGfGrsFNL1UL3IsA2164CRxCVOPttMqz60IIYPyaxpiZQv42aToCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=JA5oguv1rxu0Nz3D2y9gOILC52CDTnFB44WJo3q2FanA56GS2y4lq8awHepnMKbuVeCqpQxJKt7LqsovzfXDL8VCYdF9sYqE44mTqUewN5JCD5WCMtIQFRDecgU0EkUsdMb9F_3vI-WKgH98y1EbUONnqISNzDLSSeyKFJHNqOvWt9hRoI4lHbkKqtFn-kfzpo5PXEwm4ABJQxIFfaSAFXXH4Y4zMzu_eKU7og_4RpPraBVVOIR1Y382vfSaIwjdVPGXT1cKla10Xw44KjSA6fRrIoSvlrMfBhQhSt-qvVCHcj91Q2nCqxb-wyRcpStuMpZbvRzxEJ0mD3WxQ25gxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=JA5oguv1rxu0Nz3D2y9gOILC52CDTnFB44WJo3q2FanA56GS2y4lq8awHepnMKbuVeCqpQxJKt7LqsovzfXDL8VCYdF9sYqE44mTqUewN5JCD5WCMtIQFRDecgU0EkUsdMb9F_3vI-WKgH98y1EbUONnqISNzDLSSeyKFJHNqOvWt9hRoI4lHbkKqtFn-kfzpo5PXEwm4ABJQxIFfaSAFXXH4Y4zMzu_eKU7og_4RpPraBVVOIR1Y382vfSaIwjdVPGXT1cKla10Xw44KjSA6fRrIoSvlrMfBhQhSt-qvVCHcj91Q2nCqxb-wyRcpStuMpZbvRzxEJ0mD3WxQ25gxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=L7AwpMmy8pXv3D8PBBPYoemi6cYz--mQVJAnmWVnaMD4hDosREtLkBTTea9R0wRZTkns1IOhpY7tiqaA1gjs06aYNl419vpWve4FxZ6DyFJ9LEBHQBFXujXmlr8TJNNlf7GIdHHIAywOLFSh9tzvs7NX4T1LqjVCPoMmAAqQFz2na_WGKKSvZ_mwTyJrARy7wxxPwgYPZlK2w5aG1x676K6BYLkXZmS0Fzm2fmOtKzD4YiCLINlGtGhZduRlmzXmetZUdvwW_-ILn-ErFlLFrYHY2e2o7w5I3u2g1WgTB9lrPNKct-NX4TQw2s79LZgd44Z-x2zb9uNd9S1BV3wu32F-GfjAx2O8bgAGyzT8TsF0QMp3uxRNyQSJ90b3XKDYS8N8Xgc5z4_jy5Ql1mj_UgrIHwyw1KWvWkhBIWk7gq8Vd1scTIlRTQ5yWSMPzAz_W1koelZGwl_jBAOXWv0DoG8ThTBGjP8zkujL_TQoJLDlplolCeymDrF4dB43seV0DKZvTu2snUX_nj7ukTbpS9dawCWuDi4m1Rnz70suvciF-P5SYseHFvA23eB1DXTgydAPUUf0JP9bYNfmyOwje3elcDRafmEVGZCStOlB9MJlUrReGMQ9frB16RZfteIp37R4Ycq5gVuYp5FfPhoB-SjfDgokwrXxU4290QNeBLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=L7AwpMmy8pXv3D8PBBPYoemi6cYz--mQVJAnmWVnaMD4hDosREtLkBTTea9R0wRZTkns1IOhpY7tiqaA1gjs06aYNl419vpWve4FxZ6DyFJ9LEBHQBFXujXmlr8TJNNlf7GIdHHIAywOLFSh9tzvs7NX4T1LqjVCPoMmAAqQFz2na_WGKKSvZ_mwTyJrARy7wxxPwgYPZlK2w5aG1x676K6BYLkXZmS0Fzm2fmOtKzD4YiCLINlGtGhZduRlmzXmetZUdvwW_-ILn-ErFlLFrYHY2e2o7w5I3u2g1WgTB9lrPNKct-NX4TQw2s79LZgd44Z-x2zb9uNd9S1BV3wu32F-GfjAx2O8bgAGyzT8TsF0QMp3uxRNyQSJ90b3XKDYS8N8Xgc5z4_jy5Ql1mj_UgrIHwyw1KWvWkhBIWk7gq8Vd1scTIlRTQ5yWSMPzAz_W1koelZGwl_jBAOXWv0DoG8ThTBGjP8zkujL_TQoJLDlplolCeymDrF4dB43seV0DKZvTu2snUX_nj7ukTbpS9dawCWuDi4m1Rnz70suvciF-P5SYseHFvA23eB1DXTgydAPUUf0JP9bYNfmyOwje3elcDRafmEVGZCStOlB9MJlUrReGMQ9frB16RZfteIp37R4Ycq5gVuYp5FfPhoB-SjfDgokwrXxU4290QNeBLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M78KqwHDXYfj-UY2PwA8JPP8YFJFASgExIdXHuKouVR70DJfkqnm17JjmhM2YpF-_4dRkGhbLEXghcrto0pygFxavK9Yz3rEfPGntoJJ1_qkdKqAdNeXs2mYDvM-dPD87uVMKlPIDyBh1Mo_hNqmEfyIr957-29hzFUQFyCIhhD7Ny9NU-UEfVEe1Oo8wdHRkwOpL757NhQLYV9fCU5LIYfvsWmUC634zyQg-ip-VpGVPAUYWaWigJzIb_6T0zaROa1TYoncYqGbwXQR6TZ9r0e60cbmZWAkFCpjBGy6KzLUAKX077fRdbmbopQoOmBkN-y_D56NvIh66XN2KzY8GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=p3zH9GBy6Co4BrFeiEzqpG7PlolRJfs_No2yBBid3pPb_3i4yle6TfXVUSAze6Rq8TXUWqFKjWXBgU-5k0jIjVfcD4wJj-vjDv9VfQ1Zl_7drTIzEWbueqSwMmJZ7K-cRjGKfkkJRKc2naDZ5yBG4owrBJdp60gtVqbtgVbYt74n9J_laSxHnCfcm56eCpgF9GvygiYLQZCOyC7R0cmxeVsgYlDQzbSAhg9lUUP2igtARbEVB4OqB9AcNyA9lgRqw5r9FsOhdMOV0NPbR3e_7mdD_PiOwExLGdKbeysx5T9-_zwMNbWqlr8uWuksztc_zleZd6UheHkFvLZzg2EDiFfb27CgHiwou-pPPE6vKQwJCWXx6sLAS6nmDZ8YE6QLrCOLZKI6PsXqgOfNJ67G345KOzvOdGO4K2Bj-cL1aRELf9f8JNR5Bm0OhYi3A2CGLn9WGpedPBF9xer7F64rvh7uQplqPPwtH2VWoWFiuxZq6_4pStj8rH-0VwCVBCjViSzgxitpjfVWr2b3PR34Fac3_RVIzr2lrfy7h9TQUb2e1fuhG3yxVCvOofRvFBTV4tB6RqpBD5SftjJkClUUsGIMVKM5-nBvEUuQJ7wVnREvyTfZ1q9QGKmW5vZ5xA9USKUvRQ6HNOnox_e-7odI_DFQpCULHXuDvqhZpmkKBkI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=p3zH9GBy6Co4BrFeiEzqpG7PlolRJfs_No2yBBid3pPb_3i4yle6TfXVUSAze6Rq8TXUWqFKjWXBgU-5k0jIjVfcD4wJj-vjDv9VfQ1Zl_7drTIzEWbueqSwMmJZ7K-cRjGKfkkJRKc2naDZ5yBG4owrBJdp60gtVqbtgVbYt74n9J_laSxHnCfcm56eCpgF9GvygiYLQZCOyC7R0cmxeVsgYlDQzbSAhg9lUUP2igtARbEVB4OqB9AcNyA9lgRqw5r9FsOhdMOV0NPbR3e_7mdD_PiOwExLGdKbeysx5T9-_zwMNbWqlr8uWuksztc_zleZd6UheHkFvLZzg2EDiFfb27CgHiwou-pPPE6vKQwJCWXx6sLAS6nmDZ8YE6QLrCOLZKI6PsXqgOfNJ67G345KOzvOdGO4K2Bj-cL1aRELf9f8JNR5Bm0OhYi3A2CGLn9WGpedPBF9xer7F64rvh7uQplqPPwtH2VWoWFiuxZq6_4pStj8rH-0VwCVBCjViSzgxitpjfVWr2b3PR34Fac3_RVIzr2lrfy7h9TQUb2e1fuhG3yxVCvOofRvFBTV4tB6RqpBD5SftjJkClUUsGIMVKM5-nBvEUuQJ7wVnREvyTfZ1q9QGKmW5vZ5xA9USKUvRQ6HNOnox_e-7odI_DFQpCULHXuDvqhZpmkKBkI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=EX7pYdhdmY8lkiH2VqtD6jpW557I3qKJz-j95xMJfs3AVA2GJHXL6yTJ_WXb7HQJV3eQVYQavVaHk_RkHk8d_2ijlnhWUooMb0JVxgv6UwOqybbbrgxQiz6dPwLi5KEvwfSWjMASP-IDzzvMt36rBpHK6T8WbSmrU1g0PkJ1BvcOEFq55MOyKcVqKjQx0OLwbQt63GvKMiy-_qZS2tSsm86Ls-dpgS-nkq99o3Q4vxCnqdvgDsp5cSBxAG_t_7_z9-IrqQTFas-Q-Rr983nDzV1CvKm0vFMMoiZVGasoITNVlXmeRFuU-34aJkLu7gcJZ-mlVoa8s_hHb3y-LocsgTubRjITINo0JtnaLiM4LeIhi1DRzPYc6o4MJE9LLMgVWaXfYGW2YjoQ3qfAKwck1IS6Z3xhDI8D8FEbcylKLNasHApHenKoSqo9FOeMy_dA8qOW_Gn0hYL42oLhQ6-Aif0ngFQFzxDr9W5EFHdTyrSZqGUwxWrNmI0-QB0UE-NHXbCVjnPNKkhJHCcV1alzwipCAMCrURcVEk1QfoIrP0xA_olTasiLufIj9YANp-z-8a7d01gpu4RX8bDnekD3tpBx0N7jG6rAnnTcOVr4wP8AFxqvsPkdz_K7yySlaYm9mEpEuJtNsta_mhMg3LuS1EZHqnW_6wURpSvbwOwHq5c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=EX7pYdhdmY8lkiH2VqtD6jpW557I3qKJz-j95xMJfs3AVA2GJHXL6yTJ_WXb7HQJV3eQVYQavVaHk_RkHk8d_2ijlnhWUooMb0JVxgv6UwOqybbbrgxQiz6dPwLi5KEvwfSWjMASP-IDzzvMt36rBpHK6T8WbSmrU1g0PkJ1BvcOEFq55MOyKcVqKjQx0OLwbQt63GvKMiy-_qZS2tSsm86Ls-dpgS-nkq99o3Q4vxCnqdvgDsp5cSBxAG_t_7_z9-IrqQTFas-Q-Rr983nDzV1CvKm0vFMMoiZVGasoITNVlXmeRFuU-34aJkLu7gcJZ-mlVoa8s_hHb3y-LocsgTubRjITINo0JtnaLiM4LeIhi1DRzPYc6o4MJE9LLMgVWaXfYGW2YjoQ3qfAKwck1IS6Z3xhDI8D8FEbcylKLNasHApHenKoSqo9FOeMy_dA8qOW_Gn0hYL42oLhQ6-Aif0ngFQFzxDr9W5EFHdTyrSZqGUwxWrNmI0-QB0UE-NHXbCVjnPNKkhJHCcV1alzwipCAMCrURcVEk1QfoIrP0xA_olTasiLufIj9YANp-z-8a7d01gpu4RX8bDnekD3tpBx0N7jG6rAnnTcOVr4wP8AFxqvsPkdz_K7yySlaYm9mEpEuJtNsta_mhMg3LuS1EZHqnW_6wURpSvbwOwHq5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=jszNev1B3-00EQncAjyovFccp6l2vR-Bi7Dij5qe_NQK-PQR7E5m-OnYlH5Ow1TldwBtF8xQFEFjtK7jMDDrrM74LMT-ejbA0k7K1cGDfbLdWHqVElpQsohBitsoE-UIWHtUg8O22v26xG2Q3fxLkt3Yqwpa6zAA3i7Gb0yXG8pyUCTvrpMhILXXAHSYkGWRpnlVxwvgiCS717MbWV3870e1RjVkm11pha0fAECfiYAq8uW9JYmDGAaq7rxXPG-wHh_w9RPnJHz4pqe2WDjQlnGSyGsYq3-cbQk7sOJr6ACfgBSs0GEEjPDsA5tpMfCDVBdo5IM1skaEns5jb3dYmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=jszNev1B3-00EQncAjyovFccp6l2vR-Bi7Dij5qe_NQK-PQR7E5m-OnYlH5Ow1TldwBtF8xQFEFjtK7jMDDrrM74LMT-ejbA0k7K1cGDfbLdWHqVElpQsohBitsoE-UIWHtUg8O22v26xG2Q3fxLkt3Yqwpa6zAA3i7Gb0yXG8pyUCTvrpMhILXXAHSYkGWRpnlVxwvgiCS717MbWV3870e1RjVkm11pha0fAECfiYAq8uW9JYmDGAaq7rxXPG-wHh_w9RPnJHz4pqe2WDjQlnGSyGsYq3-cbQk7sOJr6ACfgBSs0GEEjPDsA5tpMfCDVBdo5IM1skaEns5jb3dYmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=M6HR6-Bhx6pXCX2jxxP3juSWmha7a_WidKCB8hqv92eJVmQ3blRKk_ZQVwPDSqz1DN4ZxDVgLdNUNH0FMgpNJlTSpmK7PCJFBIuhUpWJrB8GrOvERY3QWgo-bDtbrfXy84-9Kh4aSMuobR1mnVl-kR70eI8si3r6PoELbPX9zFjaHXMKBKlZcV8PWZ46mfLoHw7e8_eZ9P12L9EHEmIYNm-X6vVlagy-Jpf7HzCq4DyK50UZhp28Ge2ph4GI599WpItX2qEE8Xt4V357PeKPAwvf3wnMaTeUoj975XibypbDdk4Oa4CQOH9euoizyrujuowgD-3VK-h2i4NFPD_ivQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=M6HR6-Bhx6pXCX2jxxP3juSWmha7a_WidKCB8hqv92eJVmQ3blRKk_ZQVwPDSqz1DN4ZxDVgLdNUNH0FMgpNJlTSpmK7PCJFBIuhUpWJrB8GrOvERY3QWgo-bDtbrfXy84-9Kh4aSMuobR1mnVl-kR70eI8si3r6PoELbPX9zFjaHXMKBKlZcV8PWZ46mfLoHw7e8_eZ9P12L9EHEmIYNm-X6vVlagy-Jpf7HzCq4DyK50UZhp28Ge2ph4GI599WpItX2qEE8Xt4V357PeKPAwvf3wnMaTeUoj975XibypbDdk4Oa4CQOH9euoizyrujuowgD-3VK-h2i4NFPD_ivQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=LmRSrxp33q5K-irt8xlq_MUDr2WtQE1VIzrU5rbXpPQCoB606TdRZYcs6jekzo_1CTsxFcFwysu5IVzmZ1cL8qKh5WpHzXGpxSXUuPKV9uK8joOK8oqV2wgjZHP2ivdMFp_5J2ILuzj0Kk4ApUyesJPNDZv3HG-R7IMTl8l_01oiHTXRVBs1qhKnwC0vatT0e1kHDKJppQAKIdY0cnwRx2T0OvptLPHLXt8RmkJdtsRxSuo9JT2EYYvkTToE0bqpjUzENVmlT0YGbhMJBBNClaovLnVUJ6FddkUUHXVV5y20Ay4hHzrwkwRad1L-_y9N6N_5T17nhKKBs4u4uuuXBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=LmRSrxp33q5K-irt8xlq_MUDr2WtQE1VIzrU5rbXpPQCoB606TdRZYcs6jekzo_1CTsxFcFwysu5IVzmZ1cL8qKh5WpHzXGpxSXUuPKV9uK8joOK8oqV2wgjZHP2ivdMFp_5J2ILuzj0Kk4ApUyesJPNDZv3HG-R7IMTl8l_01oiHTXRVBs1qhKnwC0vatT0e1kHDKJppQAKIdY0cnwRx2T0OvptLPHLXt8RmkJdtsRxSuo9JT2EYYvkTToE0bqpjUzENVmlT0YGbhMJBBNClaovLnVUJ6FddkUUHXVV5y20Ay4hHzrwkwRad1L-_y9N6N_5T17nhKKBs4u4uuuXBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=VFmt1FFguaT87iybA5kUyZ6avApVLf7wsxuy1VnNxewL3w1xsWwwyvO1MbaNPxkyekLUIqczm-t3Cd0NAb9N6nvddBPYmQ0wJtswF1UKhOvO15zRYBSFF64owtBwA6dRSc6mvR8OGDYvb0D88rPn5UcYIR7MlG8JDWXadmLhPZw8IooCqzcKo1uEIDJegrmcjvTZ-roRwbYY_rgoQNtUUmioe1BoEpNygSC7v67qIFvpHTvns_GSebKk-WzUOcvZMPvmfaSUpI9L_sDq2ixL_arbtYh3FXT83manXlUsrbc99Zb7r9bSxhZeOT571fLZRqeIdZ_KzjIhi45MAfqn9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=VFmt1FFguaT87iybA5kUyZ6avApVLf7wsxuy1VnNxewL3w1xsWwwyvO1MbaNPxkyekLUIqczm-t3Cd0NAb9N6nvddBPYmQ0wJtswF1UKhOvO15zRYBSFF64owtBwA6dRSc6mvR8OGDYvb0D88rPn5UcYIR7MlG8JDWXadmLhPZw8IooCqzcKo1uEIDJegrmcjvTZ-roRwbYY_rgoQNtUUmioe1BoEpNygSC7v67qIFvpHTvns_GSebKk-WzUOcvZMPvmfaSUpI9L_sDq2ixL_arbtYh3FXT83manXlUsrbc99Zb7r9bSxhZeOT571fLZRqeIdZ_KzjIhi45MAfqn9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=iUSBYwzwzNwr-fhdAt8TZDzO7ICbINE3JtbuAAdG5uVlnHIfGddF3t8-7xioSjOq5MzaDmdWUuAHDWXcnFpXVxov5WI1s_-87_dcsQ46vaEmAphaR2cE-zt3snoBfjlBHpxD5Du-uilKT1Gy3UqlSb8_k6ZrqGyhkk0n136aOFX4TpKoAP8_SBWB2oxjBneRo4eQ-ygyCz7bralfyR8Cgj-JgqZnLOq5PNfsB_eQZqMNSKsa7kQnffpebECOGnReB-I5WGtW5Bs8-FkWD9b7smYtwjjTzYEeTuWmtGF0eMwE3k1k0vhF7WO1uu5OTTQ_eGxxbXjv0YL5QKbdLD29rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=iUSBYwzwzNwr-fhdAt8TZDzO7ICbINE3JtbuAAdG5uVlnHIfGddF3t8-7xioSjOq5MzaDmdWUuAHDWXcnFpXVxov5WI1s_-87_dcsQ46vaEmAphaR2cE-zt3snoBfjlBHpxD5Du-uilKT1Gy3UqlSb8_k6ZrqGyhkk0n136aOFX4TpKoAP8_SBWB2oxjBneRo4eQ-ygyCz7bralfyR8Cgj-JgqZnLOq5PNfsB_eQZqMNSKsa7kQnffpebECOGnReB-I5WGtW5Bs8-FkWD9b7smYtwjjTzYEeTuWmtGF0eMwE3k1k0vhF7WO1uu5OTTQ_eGxxbXjv0YL5QKbdLD29rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=OOtQnlbZSaeY6Y4cCKmrKawvCZri0YwM7ZdHkKETUQDaZzhBVP93D-hI-k-plYGTPt5bSErPScm_q8onfhmRs8LDcq0_xOZoptxAk3plXDqulmRSLRdEuUVPXmPkEkmnkTcutsXJd7JH5Wq159NXsyriejBQdBLGUmINy7C9QW0oXgivU8-8EgHKIbWc_O59YirhlaDhNMuWc6T0FMwuBfp8YmEx2fY_ZzgOVk0R00IFXNdl6GGRTmXW-A_EpGo5tb083-ExlaQLP8CD4-Vx7tBijKW6TuT_cqhFTMnKU_ByMn0faUaXtdSkcZAvWvHsAedC2fhQAK4WQqh81N0kig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=OOtQnlbZSaeY6Y4cCKmrKawvCZri0YwM7ZdHkKETUQDaZzhBVP93D-hI-k-plYGTPt5bSErPScm_q8onfhmRs8LDcq0_xOZoptxAk3plXDqulmRSLRdEuUVPXmPkEkmnkTcutsXJd7JH5Wq159NXsyriejBQdBLGUmINy7C9QW0oXgivU8-8EgHKIbWc_O59YirhlaDhNMuWc6T0FMwuBfp8YmEx2fY_ZzgOVk0R00IFXNdl6GGRTmXW-A_EpGo5tb083-ExlaQLP8CD4-Vx7tBijKW6TuT_cqhFTMnKU_ByMn0faUaXtdSkcZAvWvHsAedC2fhQAK4WQqh81N0kig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=svgs9-JZjCI6eGa270aLTTreMF-pM9Tn1hj6mvtfzFSHWUktoP37wUUjRouVgI1p8kEzWIad1QJdJ5uMzHSV2A5O-GZ-PYC0hKbCxUE8k9skTqAbjY0Vm69HcFf-diWMNT2R-MhXq8TZ4PLoOSxaBJvYGsmKJUK3w4bb5I6yoNwCegB6UyYZ_EoCfBz88kXIV1GUSSDnTkAQ9gKBi_AmJ1zvell1wOehPOl8MIQjch03r-Hxqz1Q82_emkFkX80ZROr4VAjMFeVRtgmplELET0u835_FHhp46pTSh01Z7iGNDY3nIxay3CRR7CiSEwcycOCdrGupFHWCwuDlqiylwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=svgs9-JZjCI6eGa270aLTTreMF-pM9Tn1hj6mvtfzFSHWUktoP37wUUjRouVgI1p8kEzWIad1QJdJ5uMzHSV2A5O-GZ-PYC0hKbCxUE8k9skTqAbjY0Vm69HcFf-diWMNT2R-MhXq8TZ4PLoOSxaBJvYGsmKJUK3w4bb5I6yoNwCegB6UyYZ_EoCfBz88kXIV1GUSSDnTkAQ9gKBi_AmJ1zvell1wOehPOl8MIQjch03r-Hxqz1Q82_emkFkX80ZROr4VAjMFeVRtgmplELET0u835_FHhp46pTSh01Z7iGNDY3nIxay3CRR7CiSEwcycOCdrGupFHWCwuDlqiylwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTAby6GG9tnEO4vKj4J0rE08sTUHKU6h7owPZcQDcYdSm4RlEjV9pdvxWAUpn9ndUcIg8s8ENo_5hSbtSu8LvXVSpiMwDJIKKM_Chve99Q7SIdiD4-iI6k9kkkMhhdWuS2nmzMe8wSrOlctXnxF1xQIDPSsgP2MPGVKUGSSnfCvwVae7gNtJGX6tV4NZegtICt5c2Smcj2JhSqSF0h8DgNOyefuXn7lSkKbUSXMmdxz4pXHLo9uTw6VWUDD7TfExUPX7ER-EKtKFMh4SeJg_eH24_4LkPWqZX5y91I76iFncVuCewoW5p0OlWO_FRQRDwJt8kEyr5ZBlAbJRJ5qtFw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=J6NK800VpO9knS0PMFyxDsnKoK44tkNVemDf0Qaw8OxXA1kiS0l1ZnPQuUPJ4MvpK7eTCpgojp-tI90Q1j5zxbAAKxxT_jV7Am2liXV8vM2_h-_bnRERy8yVkpGoKJtf265CGe9YRzU-Tjbkqi0HNTuuH0JZktqeFKhdhYlOzhzc_7z_mmnXLBBTUuVJDUXxwJ3dhoQ9bi3boGai0RInae06qq6vzl2AkR7thbIRdJ1naPmSHqTUFDUh5FlRIs1KusiwkZ6vlhLqDv12qMw46TiuWiDtI07ZprznhCnaR_Z2QYZSNp_sghwju7NnSVs8pNQEp-QsmUmYkFyEEAkHgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=J6NK800VpO9knS0PMFyxDsnKoK44tkNVemDf0Qaw8OxXA1kiS0l1ZnPQuUPJ4MvpK7eTCpgojp-tI90Q1j5zxbAAKxxT_jV7Am2liXV8vM2_h-_bnRERy8yVkpGoKJtf265CGe9YRzU-Tjbkqi0HNTuuH0JZktqeFKhdhYlOzhzc_7z_mmnXLBBTUuVJDUXxwJ3dhoQ9bi3boGai0RInae06qq6vzl2AkR7thbIRdJ1naPmSHqTUFDUh5FlRIs1KusiwkZ6vlhLqDv12qMw46TiuWiDtI07ZprznhCnaR_Z2QYZSNp_sghwju7NnSVs8pNQEp-QsmUmYkFyEEAkHgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=AxBxH1p7JdoWWc7oExdJ-nddveOhRRS_T8xaCoTBWLsO4SiGxOblVbs0k3epveTe6rUybjmfYDWgnxKqX6MxSfv5NuL-YRP1m8o2I5lrmcj7PrDYsFMgB2EX2_-OS9YRDC3FS7e7lFCnrpmFw4vHhinkm944dtsf1vHVKCEYoprZmcfHxptjjOIQNnQRS4sxRP3hPIAgbO2Fwd6yw2fU8Zb3Vv-QTJMimB2Zeh2Gjppjd6L1EMMNF9nrlg4IOyhPeY_OeNcWTSC5Q0DLqmH_wvvHg_t402-q0PLHrFTb530Skq5LQeenFtNNBK-xUoxmy7yn82YYkG_oOritCiBtfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=AxBxH1p7JdoWWc7oExdJ-nddveOhRRS_T8xaCoTBWLsO4SiGxOblVbs0k3epveTe6rUybjmfYDWgnxKqX6MxSfv5NuL-YRP1m8o2I5lrmcj7PrDYsFMgB2EX2_-OS9YRDC3FS7e7lFCnrpmFw4vHhinkm944dtsf1vHVKCEYoprZmcfHxptjjOIQNnQRS4sxRP3hPIAgbO2Fwd6yw2fU8Zb3Vv-QTJMimB2Zeh2Gjppjd6L1EMMNF9nrlg4IOyhPeY_OeNcWTSC5Q0DLqmH_wvvHg_t402-q0PLHrFTb530Skq5LQeenFtNNBK-xUoxmy7yn82YYkG_oOritCiBtfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=PAudv4pvdneJ1SPItfHfIymVG651rbSOzTLbRKABqP4TAGt4DsePZ_CUevM6zwom3ddr9bVCBF_ZFUWnMIFWz6L7A0w08vSLzbdK8Z19kP9sS4pT246aDnnmuka8TxKl4VBtYnQ6TCUmK30SMshHCyjAV_KZ97B9dzb7DGBX9vRhdzDTr899M_p67u0n7bWjDrOmL5ECpBmF0v2yN4u9sD_DO0EOCi8yBIuPw6mO60WfHKhGo_IHMs5EHmUhP-TpE2fUtnIWYMBTxsN_5-836-ombSF_odvi-MqNf1Oy5sjHEtNc_kezJVYd5UZU1O6neAy1OBH-lmFklkW_1ksDNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=PAudv4pvdneJ1SPItfHfIymVG651rbSOzTLbRKABqP4TAGt4DsePZ_CUevM6zwom3ddr9bVCBF_ZFUWnMIFWz6L7A0w08vSLzbdK8Z19kP9sS4pT246aDnnmuka8TxKl4VBtYnQ6TCUmK30SMshHCyjAV_KZ97B9dzb7DGBX9vRhdzDTr899M_p67u0n7bWjDrOmL5ECpBmF0v2yN4u9sD_DO0EOCi8yBIuPw6mO60WfHKhGo_IHMs5EHmUhP-TpE2fUtnIWYMBTxsN_5-836-ombSF_odvi-MqNf1Oy5sjHEtNc_kezJVYd5UZU1O6neAy1OBH-lmFklkW_1ksDNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=CabIXDB2C9WX8IgL9esXr-AiUkrXk0TDZNNkJfivbJfbftGmsD2qUgZLmXhoWs6O94viWxbDlwLXeA_e5cb1Dfsz__NahuH9wFmD8sfvzj5mzPf5m8wLSZlHtajpCyJeeyTIgYInfuBFFNlPq3Gp0gFgyDZRfBwu_eD_YWqnViXa1q3-eokTN8fhmrLXVITPpmM1_nqmMM3gv-sgkZS0GYls4dE5rMgs5s82zKTYnSJbC_lQCIkgrygEsERU6ldl9UtctFiLgq1UsugJewRmzPct7nsho-vZKgzO2SZIV_QV7kWRix4kuCnd2rttQrU0SyNcxrrIqkufsX-CEffd7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=CabIXDB2C9WX8IgL9esXr-AiUkrXk0TDZNNkJfivbJfbftGmsD2qUgZLmXhoWs6O94viWxbDlwLXeA_e5cb1Dfsz__NahuH9wFmD8sfvzj5mzPf5m8wLSZlHtajpCyJeeyTIgYInfuBFFNlPq3Gp0gFgyDZRfBwu_eD_YWqnViXa1q3-eokTN8fhmrLXVITPpmM1_nqmMM3gv-sgkZS0GYls4dE5rMgs5s82zKTYnSJbC_lQCIkgrygEsERU6ldl9UtctFiLgq1UsugJewRmzPct7nsho-vZKgzO2SZIV_QV7kWRix4kuCnd2rttQrU0SyNcxrrIqkufsX-CEffd7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnUFQMBHB8srTFna_MVwrG1dJUSUOemU-obuj_LoId1LfjJwUPPMMnnVziS9yiKMaI3QCpa8Cv4smx364s5HkIn7Y818oY0YgEdv5wP4NAjzjR3r287aTxCom8iOB6k84-dayXEtUjRUlrOnT_YaFNW2DB5VQxAP0p8aO-ovSuXwBYf7Zi6_CgUMc6SLBykDx2KxkhCzL22zUUI_PHpD3TsNg47EcPjvj5MJ_Lz2wr4WTaMrYo3NyMsbGMjrvyy0_tjontSOp28KcSou8GG2gGTUJTEwoIJKuUZhTGWoG9nky-rPqHZL5g6WxFyPCXmH5Tkl42aPagFgZZQYWymw_A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=DzA5Nq3G6QfbpKPxk8r0PPOeziIDKHOW8QI2Q7__vj2CsQZWPyAuLAhfMAkbBZI3EHWko6T6J_6837kDWnZVfW-3yvxDukUIj3wj9XJXgUdRf9RmNc7puoSoWp5RTwZkzktB3zQQ-wdmWQtc7dSjQpRh-eSrDcJM5R6SQlQ2GqHYD3AK3eFX2RttuuvjX_D7A6dMrImPVoawDTnxmxds-v15HP6IHTyb5ZMUEN7QxCfsP7J_RuzYxtSlbptkJDv_NUvDjb7uMWcErwW8VPsAxZAq_2OU2cWcjhdR6txznxhJxdcMdrc_8mtF7C2af37grUXUdmVSP9I4cMt4lw9SPjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=DzA5Nq3G6QfbpKPxk8r0PPOeziIDKHOW8QI2Q7__vj2CsQZWPyAuLAhfMAkbBZI3EHWko6T6J_6837kDWnZVfW-3yvxDukUIj3wj9XJXgUdRf9RmNc7puoSoWp5RTwZkzktB3zQQ-wdmWQtc7dSjQpRh-eSrDcJM5R6SQlQ2GqHYD3AK3eFX2RttuuvjX_D7A6dMrImPVoawDTnxmxds-v15HP6IHTyb5ZMUEN7QxCfsP7J_RuzYxtSlbptkJDv_NUvDjb7uMWcErwW8VPsAxZAq_2OU2cWcjhdR6txznxhJxdcMdrc_8mtF7C2af37grUXUdmVSP9I4cMt4lw9SPjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=t80dvfwyadi5Mp-znpwynp3CNy7suipFEjPQysgnlNtmPb2Ri-5GKh26eqkqQnDDesoDLzzFzxi1719AlGa7XSIRUSGu9msnb4K7zHUMPz1AKmGIMI8ktbl5mnDjejy0a7pAscQrAtdtAGredaUfWdjITnr4sydzwm1roxkqUDXi88SWed7qbOLnf-RJUYxlwU5CmXX52FyclNC4TihclQS6bbQllXJQGSLWXVxIozaXkehjqKsDkPtf3Lf2NRCWgjRg6A2OTgf6iboK-a_5_5-jfRbQ2G7giSle6q_HDxQc6cHm8qFlp7C02R6wwFGvjgb0Fdz2o-mf5XKfPtZ3Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=t80dvfwyadi5Mp-znpwynp3CNy7suipFEjPQysgnlNtmPb2Ri-5GKh26eqkqQnDDesoDLzzFzxi1719AlGa7XSIRUSGu9msnb4K7zHUMPz1AKmGIMI8ktbl5mnDjejy0a7pAscQrAtdtAGredaUfWdjITnr4sydzwm1roxkqUDXi88SWed7qbOLnf-RJUYxlwU5CmXX52FyclNC4TihclQS6bbQllXJQGSLWXVxIozaXkehjqKsDkPtf3Lf2NRCWgjRg6A2OTgf6iboK-a_5_5-jfRbQ2G7giSle6q_HDxQc6cHm8qFlp7C02R6wwFGvjgb0Fdz2o-mf5XKfPtZ3Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kFF5i0LZVVdUDUSx9ZVgyTAK-KecdAkj6HfZNRMrAH5CFtQc6L50sfVf1ps6PjSLeVVLccuVJ6Aaru7Z9Mn3zHxHR3oayZsXvqQ-0XGQaHRngbbuBpbEcDYiJkYAVI97OY_b0qroW3vJpVvz7xpBFRTGvCRc5SR23IPj14AEUkjbJPzANsNo7LI7l_SUFFIzNWdFXcsp-7Sgie1Qs31DIlBepBcTVYrNQT_Zc7V6W-7q6LKviMZflsOzQrqmnywmeQ2Qr1Qr5rQvA3h52t4AuPdGGLp1R7g4_y0ZEov4HYjoq9ap2bbkzeQn4hREaWClIOT9N2OTeg_s4IEOsnnCPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_7cXXkZ4Qo_fbTh8ol_Y0YmgMF0il2o6RT8fDYuLRRo2cN-3urm7WvYbIs7W2HcHaWsjZax75I2eIAnBk2l_ahsRfmjpjWR2kpHnIpXn58HH0zazBAgKDB9WEe3dzm2GN9rGELQVWVOTtQt6FYtVBzj6GuvA-hp8etJQIWt4eMSlBQE2wSZpKyyPC54kNaK1Ts8C5KMznYwqTIdMReZPq3xTG6CJ97FjIN65FUT-Dv2zyMzSbKMeeNaw07h3JZchnUxhaSKy6TCrcHj7L_3ITuNfkCn7yn0pOS4Hf3OqA4dEKTdIJcZjlyBzpY6EqM9FcqfPb5l-BQ-ZS0tYq8jmQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=rqwiNkBpaSyLzcZ7AtvYyCb5XEVlhrcZJvJGzrKWIJX_KwdhWiboMl4no0f_7FAZwYEBRlykcTmRXu1ZMhYJ3XkfdqEWeIhy_Q6qh_3yn-Uo1sdhUBx10TlRNQMjHZI7gvm3YIvSQcZeCSskxdfwhYOvtWoZDuuTynS6EUSopZeqoKTDPCwn1sRjJqoUd4Mu4wvv1vHnsmplIKmHf4cfTs8KHi3tmtj7cmeATqwpLMJOT7Syh29OG1_5lRa1okAVRSb71o9fdbN8nKvUB6hBBolaanrawnCN2V_4ihqkjF_b426ex9uTYUowweVMhOA5jiAfn4WKivfS9tZd1cVlww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=rqwiNkBpaSyLzcZ7AtvYyCb5XEVlhrcZJvJGzrKWIJX_KwdhWiboMl4no0f_7FAZwYEBRlykcTmRXu1ZMhYJ3XkfdqEWeIhy_Q6qh_3yn-Uo1sdhUBx10TlRNQMjHZI7gvm3YIvSQcZeCSskxdfwhYOvtWoZDuuTynS6EUSopZeqoKTDPCwn1sRjJqoUd4Mu4wvv1vHnsmplIKmHf4cfTs8KHi3tmtj7cmeATqwpLMJOT7Syh29OG1_5lRa1okAVRSb71o9fdbN8nKvUB6hBBolaanrawnCN2V_4ihqkjF_b426ex9uTYUowweVMhOA5jiAfn4WKivfS9tZd1cVlww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnNmbv_qP-8VMxvZ3oRUfwqjLEmZ8h8C38t23BQzhfXC1WVy0DN5HE_Vov9jDCMYdggHy9RJskrX1s9gAsv5cLvR12QZFhp51CfV8Ab7-fkYPUD4sdt4u8l-oUbu1tW29qJu_MyrkVDgXu7mayKKYmCS7RxGu6OMlODssoCMcVpws9xOGPq18TtPIitqye447zS412vAaRaWUweYX1dDigtuk1jAolwCY49y4B_Hr8gn8wwb2sZdo3yMAEFLpb-CP3UDfF41hvHuY7QCxAIzMmhNAw3hDZ05dHv_e3XsEXkgbstpBH824tlBqsVmq_ltJ09QJ1Q-FgaCXHX9QNrGlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIdAthGb9ZJeHC7neRawEkgXFGI0sFvsfMzYpVewT6y9sxB7eU04-Dtfbu1R7d-oJ4DI6vnTs24ZfBvQ2tTC-3hUAKr905zehSxVSHsCd8ZTZylmMY70FSO7OONDaILL9zSZt1XZoN28jwNSRHizB45Nj9PZNsBWZQyamirIlBx8CxiUH7EXPjlhgT2KALNR4HeQkLkqMohu6A5STtJJ_j6NQ6kvH5ag2M-MwH0x1v3ESc5e2Bbjegkn5BRQCCFcm4L90M21i_OpheyiBH4WUskKHhczdPLwWlIBwweeSJcSG48Ut34_Xg6j_BgG2ZyUiklO9grTPi2RHfZZzmGMnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5pFVNFboVFC9Ibkjx2ELvEo-04rzZ7_ZxJuzoxfAYHobjNb9zziqWIo97OHnEAW8AtwCKeXLlo_UCjGcAFlSonHrikBRmVz4nuT3LJGlx4BHVCbsHmV-uJYmhVtoC_YWHZsKx7wc7qxj6wRRbTOck1MqXOcYt0JwEqPR5hUGrjSUVFxy9jw9wzFA9Kox_uP0yhacFLROte9LPxBF0NQm3roOZ2YxprTlrZLESTeWNLAxdyayTktPXpONibIswGozhwrRMCzDlHEYVYUBJZbjRQhcdJXw8yZ7YRzf4qMe6knc_sZO6h9x9hNvbS71eNAhGjVY3hE3oCtmIuk1Zg_EQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=ZgzigyaQJOj5cfEBV2pjQbb8shDESQ4b3gssQFvClfJ9wyj_3q1vWYfrlXWThLV4iYBN0V1L7de1nNlsuypR3pUrRfB_QQGwT2xK9QXR6WpMZPZhRrToyREtfDDYCGCdbQMLoE_3xZG_wlsmDAOt1pRRwUs8vBVRXoybIDRfCSiqJ28yybQ16tRK8GK6mixx-vby7uhbSZ8iFMFPWzYha1Q7MEdmlQpVhTyYqcrQ4VY90ZHGKMoN1--XX_L7y6tOnjpTG-8W68qxQcjBeCAH7ESgvXaZVxWNw2kOyfzx0FZFnDuuDQVDQzB8-gpA2vhdDsfBmHnBM5vnP_81lr-x5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=ZgzigyaQJOj5cfEBV2pjQbb8shDESQ4b3gssQFvClfJ9wyj_3q1vWYfrlXWThLV4iYBN0V1L7de1nNlsuypR3pUrRfB_QQGwT2xK9QXR6WpMZPZhRrToyREtfDDYCGCdbQMLoE_3xZG_wlsmDAOt1pRRwUs8vBVRXoybIDRfCSiqJ28yybQ16tRK8GK6mixx-vby7uhbSZ8iFMFPWzYha1Q7MEdmlQpVhTyYqcrQ4VY90ZHGKMoN1--XX_L7y6tOnjpTG-8W68qxQcjBeCAH7ESgvXaZVxWNw2kOyfzx0FZFnDuuDQVDQzB8-gpA2vhdDsfBmHnBM5vnP_81lr-x5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=g1AHlUoqWD6Lqiwp6GdqRL2j3DFgFCR-rYATEaS3MrHz2xfFYRquAkNF_SgFOk6kHlxPWkZArjFJEbEE_8bHSX_Lr2NR5q25IlTv7qPbfywV6ll6J-C4jJz5K45n6XUY1qNXVwofy9Fp1E3ER3mQakfZrxzaHgZm64rPO_ZDc549_8r5HHQb2WxGbij6EdiZwl7buPFGJGCj4m4VfRVGljQorG6yY6GbLz2A9x5gwyYlXzk6lWSRHecijnYRQhOnB8_YjQeSOCJXDvUajsJmQy83r80VzQwupjqmRDM1PMb-R9tga4LJ732ogeNLFC2Fgi_hgONin2lCxPn2tZL1dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=g1AHlUoqWD6Lqiwp6GdqRL2j3DFgFCR-rYATEaS3MrHz2xfFYRquAkNF_SgFOk6kHlxPWkZArjFJEbEE_8bHSX_Lr2NR5q25IlTv7qPbfywV6ll6J-C4jJz5K45n6XUY1qNXVwofy9Fp1E3ER3mQakfZrxzaHgZm64rPO_ZDc549_8r5HHQb2WxGbij6EdiZwl7buPFGJGCj4m4VfRVGljQorG6yY6GbLz2A9x5gwyYlXzk6lWSRHecijnYRQhOnB8_YjQeSOCJXDvUajsJmQy83r80VzQwupjqmRDM1PMb-R9tga4LJ732ogeNLFC2Fgi_hgONin2lCxPn2tZL1dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=G7oLKzQZhFi0ocyQ3-D5eyKrlZUzhCr59ivhxBpt4dQE3vFU9Wpg_-d9uLnYrzKaUJkkqZV1gCticcm2lwH36mP5x2LgSaxetriNt5_KiwIm7CfpLzH9xeO7A9BbGppPQyWCx3yilaEUR4OxZLGtmpRVLI__rsmUidSLaOXnn5cElyniuO8wpbDpoCOw8Y8KkyrfzOfZMDrvCeBupp0H-wyBpnOXw2lKClwFaVr4C-DX3D3zst8edkFIs8UAL4BObmi12bd7qrH9HuPPYDmFDgGo7et_KxeHsOC_yCDN6Gx9KDeoRQ8i4Ad8nat50JrlsrLRklKXIhw6xPZZVOWBCIiwsBVDPXh4UIxDsIhS_L2NjM1lM557-ziFuh1HU5wlj7OK5oJt1fCumkgjHaJXYx6aBdLD8HmdS-LS4Q8nyL3Zg-Cc_kdinJGpCPGXY10ME5uA51wkoKSLinZYp8xZ3rNJLSe1VKY8WMzDf0oznZxYzSs-cuKZjJ4GKPcVZPUxoCn259XXUddP35mBMuZEzkq4gsB3x1BeRbz9RqO6QtjGgqiVMOsrwdGmmDGKW3KV6nP1P3gjrJdUks3OkqUZgVlTqRTKS4JP3s5Ng7nS9BR-yj0SDdCstgProQyhtgR7xUf4bWCJ0Ie_qhE-_VADxGdMHuKaDGBkAHebvKqN134" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=G7oLKzQZhFi0ocyQ3-D5eyKrlZUzhCr59ivhxBpt4dQE3vFU9Wpg_-d9uLnYrzKaUJkkqZV1gCticcm2lwH36mP5x2LgSaxetriNt5_KiwIm7CfpLzH9xeO7A9BbGppPQyWCx3yilaEUR4OxZLGtmpRVLI__rsmUidSLaOXnn5cElyniuO8wpbDpoCOw8Y8KkyrfzOfZMDrvCeBupp0H-wyBpnOXw2lKClwFaVr4C-DX3D3zst8edkFIs8UAL4BObmi12bd7qrH9HuPPYDmFDgGo7et_KxeHsOC_yCDN6Gx9KDeoRQ8i4Ad8nat50JrlsrLRklKXIhw6xPZZVOWBCIiwsBVDPXh4UIxDsIhS_L2NjM1lM557-ziFuh1HU5wlj7OK5oJt1fCumkgjHaJXYx6aBdLD8HmdS-LS4Q8nyL3Zg-Cc_kdinJGpCPGXY10ME5uA51wkoKSLinZYp8xZ3rNJLSe1VKY8WMzDf0oznZxYzSs-cuKZjJ4GKPcVZPUxoCn259XXUddP35mBMuZEzkq4gsB3x1BeRbz9RqO6QtjGgqiVMOsrwdGmmDGKW3KV6nP1P3gjrJdUks3OkqUZgVlTqRTKS4JP3s5Ng7nS9BR-yj0SDdCstgProQyhtgR7xUf4bWCJ0Ie_qhE-_VADxGdMHuKaDGBkAHebvKqN134" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=OhiiZyrimjaLscJl218k1or0UqS_ZKmOXchsiiG6zhfXQFtCMtOuM_CIwzZooA97IHfuEHhZQI2wAyFfKZY-Fn5GJdlYfsSDORp4GOa36-z2nDfzI-8Ub5rTuKHM6VrVLEKdWj_WbmRXhUUt5Fxo3XA9ghFyX76KWeWy_7AXe8ZGo8W9KhEU8YmsJWtbfc4ijKHVcGZ7_faynACI63mifeCnvlU7Ounm6QSJXs_vbbneNqgOi1uDoQ5vpfTRPdkXGoomCqVRblOoCcTNsB2VHfadDvo-zqMbtx6F7W90ZGvXK5lNY5uvby01aEE7JZxtaM8xRmjjk-XmYYuIc-_u_EAAd0pAWyXeOQ8W_izYLLv5pSBrNTcfzCAXnwagrpysX4pJxTMJpPi6hREiCItGVIDUgb8zOXvcCoFdyU51QLeXPTRkqJwefvY8g-EowU2fMIccUxMqIKfF_GyxVMpiAF_nK0A9hbDrmV1AX_WVoZDwfO5Lmw6qWiX2Tch5ilCEwgc54LGgUDwu0JgElYxny0zLGMPjXYy74TPMEidGQ21GcNi5QSD3OFTiGX74-2hfTXmrGCeSGt483QW8hZ_bb0rikPsvSYyd5nLsQJ6i1iNt88w3gCI4C67bJMmC4NEiy-6UR8pnPKC7sfWygZU2qyuAwv1NQQ2PzjRQJuVZ1p4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=OhiiZyrimjaLscJl218k1or0UqS_ZKmOXchsiiG6zhfXQFtCMtOuM_CIwzZooA97IHfuEHhZQI2wAyFfKZY-Fn5GJdlYfsSDORp4GOa36-z2nDfzI-8Ub5rTuKHM6VrVLEKdWj_WbmRXhUUt5Fxo3XA9ghFyX76KWeWy_7AXe8ZGo8W9KhEU8YmsJWtbfc4ijKHVcGZ7_faynACI63mifeCnvlU7Ounm6QSJXs_vbbneNqgOi1uDoQ5vpfTRPdkXGoomCqVRblOoCcTNsB2VHfadDvo-zqMbtx6F7W90ZGvXK5lNY5uvby01aEE7JZxtaM8xRmjjk-XmYYuIc-_u_EAAd0pAWyXeOQ8W_izYLLv5pSBrNTcfzCAXnwagrpysX4pJxTMJpPi6hREiCItGVIDUgb8zOXvcCoFdyU51QLeXPTRkqJwefvY8g-EowU2fMIccUxMqIKfF_GyxVMpiAF_nK0A9hbDrmV1AX_WVoZDwfO5Lmw6qWiX2Tch5ilCEwgc54LGgUDwu0JgElYxny0zLGMPjXYy74TPMEidGQ21GcNi5QSD3OFTiGX74-2hfTXmrGCeSGt483QW8hZ_bb0rikPsvSYyd5nLsQJ6i1iNt88w3gCI4C67bJMmC4NEiy-6UR8pnPKC7sfWygZU2qyuAwv1NQQ2PzjRQJuVZ1p4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=pPwAsTQ-CEfSGKM6ovjPkmR0MHDnoNixZTo_9Eqsbikp6osxdfUFaUwRKwSNMb-zNDZfvm0rp7e9RYkXS18_odY4s_qZJh2ALJICIfJkfKPC1kUEQXLieozv5z21-Gr92llbrW-ntYtPMi5K37laT1-rI4m_dqPb0jqHcKqktD6LRLWJxXOYiLPuYNmcX_G2DAcgf3a3N0jW8tIeGbm8E_B65D_BpUcJsoH9KVKQMrlT1DKhEnXNA2nazPBvlmjzBMyY-PtH9Lf9n72Jl2okaRKGPrdTE7o-trnNt-54Ii8qjrwNIIsTFfVA31-GEPiDWkufhwFlebfqk6xgaY2FPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=pPwAsTQ-CEfSGKM6ovjPkmR0MHDnoNixZTo_9Eqsbikp6osxdfUFaUwRKwSNMb-zNDZfvm0rp7e9RYkXS18_odY4s_qZJh2ALJICIfJkfKPC1kUEQXLieozv5z21-Gr92llbrW-ntYtPMi5K37laT1-rI4m_dqPb0jqHcKqktD6LRLWJxXOYiLPuYNmcX_G2DAcgf3a3N0jW8tIeGbm8E_B65D_BpUcJsoH9KVKQMrlT1DKhEnXNA2nazPBvlmjzBMyY-PtH9Lf9n72Jl2okaRKGPrdTE7o-trnNt-54Ii8qjrwNIIsTFfVA31-GEPiDWkufhwFlebfqk6xgaY2FPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdZHRx9QMJJ-TyM8ldieM0BZM5vvM0F5vB163AdCt4QAj_j75Pu1mBvJTqqedJyzwPNqQLhQjkLARrzINznakIcazwJ9Uex3ciruN4dRx9ut1-k3nA7mrtp44Cq9f9CWVov5GJ3fHAkfQvdy7IJoLYW0vQVagwqLCtedJaPM4xbREECZRSd2cAIyJgtJnU5og21aqBnbW7T-gktIh28hriG5UQpsbFoyMC3FXNju35rUpcpmH42t8YUlRR_oQKN-naz9xFV21Zo0LgjGP7yHk9XjjcVTxfk0sEXflmfA8MS8w9pxab1Ie4I4PTFPLxOK369XqqNgY-cPUMvIXBATCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=pEW5FJ2oJ6uMBjHSm1xhdBnxNLsTugcmX_nT2t1fFjSe431ziR5dWumWvNO-RLya1lgjSDrwGe7cgd71S4T4rGnTgEQjoxxjJaoRMXrbbmO4ZHB6ohoD76kLHjJvmWZc7IgRiarNFvRfR1wPf-302aN4c2M3c9n22HbgGJkUYYDewChLA6V2xiiQPhENyF9l4MJISTY2FIT6ntgP1Ljbpg57JOJQZmPItnfUu0xqM2UZnfp_3z93lVPxaaDNUulaM36oVtFUoTK4ZwUGyxE7rey_7aFDbCjdeJmHYTznE1yJC1pnPukSXaQnQDRBCctuS5XLEerBuki-izAXLapPTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=pEW5FJ2oJ6uMBjHSm1xhdBnxNLsTugcmX_nT2t1fFjSe431ziR5dWumWvNO-RLya1lgjSDrwGe7cgd71S4T4rGnTgEQjoxxjJaoRMXrbbmO4ZHB6ohoD76kLHjJvmWZc7IgRiarNFvRfR1wPf-302aN4c2M3c9n22HbgGJkUYYDewChLA6V2xiiQPhENyF9l4MJISTY2FIT6ntgP1Ljbpg57JOJQZmPItnfUu0xqM2UZnfp_3z93lVPxaaDNUulaM36oVtFUoTK4ZwUGyxE7rey_7aFDbCjdeJmHYTznE1yJC1pnPukSXaQnQDRBCctuS5XLEerBuki-izAXLapPTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=PnCp5NprI-3BvTFgrl7_Vo6cHs2tZe0E9khwlwBAaaELAaVFhDpju4zgF7yrCq6xCvQVYCD_9lFgYcviPlTiYeuYpbgQZ3fnXAzzQ3xkeYWnifUoDOpQ5k9EVurcVgT8CtIECUx24htvkkmA6VCA5lnlIvFZpT3dSZ2CZ1m2tnu4up6vxOA-SpMTAgwNa1AQx5tm_ltXwpxP61FYWliH5Qraa_aEljlyJoxayIh_cEgyxmK9ZKFaCQx276wPoiet9luSx78Re2-wCDR0nSYP21y4jsWBYqjxriPyOI3kNpx93vzlB0aMLJzbEkX81H8oBX5vRFZ1YOZzWDUMMu6GSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=PnCp5NprI-3BvTFgrl7_Vo6cHs2tZe0E9khwlwBAaaELAaVFhDpju4zgF7yrCq6xCvQVYCD_9lFgYcviPlTiYeuYpbgQZ3fnXAzzQ3xkeYWnifUoDOpQ5k9EVurcVgT8CtIECUx24htvkkmA6VCA5lnlIvFZpT3dSZ2CZ1m2tnu4up6vxOA-SpMTAgwNa1AQx5tm_ltXwpxP61FYWliH5Qraa_aEljlyJoxayIh_cEgyxmK9ZKFaCQx276wPoiet9luSx78Re2-wCDR0nSYP21y4jsWBYqjxriPyOI3kNpx93vzlB0aMLJzbEkX81H8oBX5vRFZ1YOZzWDUMMu6GSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPTMX9JuWdxf4I5NuSaeJy7MbmWMNI9hxBe2OOStM_wfmmmCUIkSctSK_MOTrPrfIIVrvmRA0gwlejv1ang0p91sxag6bzeJ7Ox3b97Alx8PUTYVnlbife0dDiLFRFrnOFSlxh-UAQlZSa0LpQSxSYLd8dMmyyHpV0nmitdXjiB9Rrq9GGHpUVfdaj-1ao4WdNe2TgsRCVjsqP1sVW9CR9hJ_fRXInzZtoxxd_2KBjxYZ_BnLzZo3rlmq6zlDx3ysPYDQqvl5fcXniGXx-POrsuoefd_vpDPv3dbH3gDMvICI7NaSvmH6CLCdLOI6_6wgEWRmr_FNQ1xd2iRbugkSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PosYsbTgXKvOl_aU1heLJS0fbxv9QGB6kVAtJmO9WHLGKUYiFqiQbNnidN48gMukR8LdUDl70aVUoN-sFSTgkuVxwJEu8SBnAS-fzQhglL81I3vhdIELTkhluD4x_vd58npligfaarwjqeEoqf5ZMP35N61db08GBkgda6wWWys8lj3lHAIVRCOkMwrphHjlw-N-UEQN-5X9_Q4XOC-QFg0U_iCg30cDz2pUA2YMOo6ClFFZew_ej9CoqGWWZR-ybdGCFpqG1b-6L_5hpqozhpfqH4fi-1mb6CzJoRmkaBbRAKPLQ7NeB3vjbiQdI6ST4BH3Es7vJAdIjIC27ozbsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hO0dkRkJCWC4wdbMgzLYoeigoKCbGdDIRt4FXEz23wIREEWrQCAouL5xY4fS641xiKPIFruF3FC8F4eoXMHV1xgKRntE2X9Ne5XC8L1Y5XB0Aj20gaOuPtdCMaHE77WYzfgmbeH_8RKMGiGXthctmrjmhxFNa-ryUwx5tdGFdw7WLXlzLaj5MSKbxolfj-FxKG7u9Bd-q_pA4yfnsBhftwPyAbzqjkPtzxODYSBoWab5U8isRaxXzVUyquVv4VZEribASrmSL2BAYVwDhnbwlXooetbG1wpy7lmUQze2yvP1PlfRt4z1rdJ6HD-5FfbKKA0Ys59yTFauKsgkMkIDRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKZj1QyL_1kpCRedW39vV8D5EpC6K_x7GewPKRQsta3mZKOtO_Nlgu1WTA3VJJwmrafybSxm9yvRloxk8DLggAWHokAjFEsI3R1qXe4kk4K4AzsBznR0uFD3N_xwmmZvfTA9zMUGmtFfdWChHDg94XBTBsp08aitq-gYNtHZT09HPbOyTQzRvJNWIXpM4eQ3mE1DMQWQSiaZsS6Hn-DKts2b6YlZAIAJaRktV3p09hY-JfWAQEL7SPxoPrSNCyrp7mrIOuarq6AWGP0M1fRBKCFEJ-CAEfYj56U19kfpFN0OsBEfN8efBkWtAXT09G6rLryX4dD9g1cbV-jSqu_1sQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgmVkNQNQ9jb8tL7DOhDK3vOYTEN5BHTyrOPbqfu4pMT0GruHuUYMCmXowM1Dwr6Rc21KB1GjMrtW9wmhcoMFMyAy0qvFukHuDv6lIJD6rYF-bzgZeAx1CAgomzc5sjuiAd3k8r2VCng7PGWyp4aVhr-C6_RDe_CtEWnNy-fP64TG4Cs-r8aa-tOLPaH8t0j7r03RU4fN-b1m0-_uo1zETtGvr0DjcDCs4_4LTHwiPCM6vRsXWuUBM8dwhRM11wpeNKYw5pakry_VEFbF5tk5hQ_eXEqyTxz28RWBCb8R2yRoSSildXD9-NxB10cG90wVngwHhTfchuZY09Q-Fc_Kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYIUnSvFTJJ_MPhjvMj0xukS6wLceI1iDZBxxS83khSYUlCdC7Sf2QDxHzEd0lcRtQVT8r1pz7YkeCCp2LfXWH4aO3BhOq_FLTLJ9w5HfL6-r82a7OEybjTq2bh_SoYrIze1PvehOU7qtIuKAHO1OTiq1Gtbk7Y7vLgJkAOljYc-rpGty00jZFyrsMUz9Ql3OluG5yJcZ_kKNtoF5Ldj3ih_PBUALMeV8eLsfX4CV1ItXC9Z0gl4WDrxIB7sBMejqD9_nFIVneLzhI34aFxV2vo9SCKyKOeCXDANlC6jPJKeoeXILIK48OmnfEFYKR4srhKAXB-uwebWNKONsDpHqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAM8QUJf1oB_UlnkJgL0r27NCF2Ri8CQSv3NyXDEuj4vi5x3XIOkLsBe9WgjVK6sgermKTaojZvTkiAzYqfDUsNzuY13vdRqHlvAxEGUSS77K3b5JI1w6mOEsfbQ2AnuWgoemwrO_B-q84WV7Gj7p5Prf9qSQH-4_uIgJjsuTXk65uTKyn7uXJLbDaqr1Movo5k9k6WsOggzoOApGRLQ_hi3oBHc1HK9I-5PYh2fVyRulghxCAGzc658UAEQlIKaOEyzE6dcQR2SCJZ8q_qFuFWMJl1RmbqhL4PhMCVYGtAC2k1oHc9w_HOBvwrMkCq_67YTS6XzNQ0LQLJc86XtCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AMn9xORqO6vApUQDD0WmGZU-vArh9GcSgVT1NEQxJVLL2qFpe5gZNCyh8oxZcmU0LnUnYTNBVAAqNT-Jmm2K2zYOgnAAAPYXqY51foPwwG1R8HEPCS7irLeUnlvAsoSw_oUlWkw0qoPEMf1ejO312LtRP0LN5Iib-pzhQiEbHHInw-COKoN_TsF4cDCerPq0PzI6D-6JH4gp0fOvfd3TM6nrNv88Az2ozv1eMTmqTRuBkFzoF5-r-MfcXVGVG6jaFTYnLFUGyiUtmYzQ7sjgZ_oPPHx_eZbSRA3CKX6oJUBn-mIfOm8ogjz7xX6sbHGIp8qZV8n-qLlmXOe4Ak827Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/caULMWK2GaEQ_xyb4Gg8MRBpO_N4XxOK8sEWqX50nHLCG3OqAZP2yBEstljmPTGa0U5POiTPByQiGWl9MKR8iraarpngBCjdrpL8dRlhvlNv5_Kj09a4nJ047Q7DNQIsUBft-oJnId8JT4bsbSfwghCzByp9YfPYmKtQgZKnHi6cd-ohoLAwqt3zY36a0JuJ59DSFXvYwPxUfVEUJBB4l67x2tT4eUe0iZL2aULTTQKykYrInFkMptOGk6MwzVtJ8DQ66pygJ5pYULtS4ZhLbO4ytP-WMms8oMP3W_S5f6HAkIPrYbXUTGuvh3dekkiTTEXFeQC9d2HQuMqjzxxdTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NuNyiq5N0z5rEteH7zmF-XeFcgWdl43wsjJ3VkGakm99gBvzVaCQjLqOrmvJMxJESnwagBVRMpbbkBJ_TEbJEuOTgLm-MMw8eAYbJs837mdRxCfXOEtDxRUFqapWvsRlp1aBYuTauivLwL1owqUPa7L67FN2c9mdYMFcrPKtozLewUY_lE8y8EwAH0VL9Hta-gKN9FkwA-wup-cUZt91C4G9VdKQJU_EvqEGHV8KI1CB1km9hSCn_VpPXZzOptkLRc-veqErFak6AXDp2AeAfJ9E9Drb35prIkn5K5TeOlJwe8lnTdt5d3a6_EoB2eaMPtPFFrHpUCuIUx3fBSWrGQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=ZtKE5ZYkMxdH36msxvKIhexsHXxvjnrn2M7yeaAJwmlnvuAXIeF_t-y1K5sIK_KbBjI0cujP9IJzKSyJckqivBjSKh74xvzM6jX2HyFH2HUPE7T7fBqVFpyuzY6k4ae82J3xKm_LyBVpXWHvZZLHcwVMcYczFycVJtzFzhLYOhhQZFHa2H6m1oLS-Mor6vILy87BFJVKe6xqHas6f-u3HGE9YKq1gOElfHPXkgqNUeQUgHMWyljFpG8BWNIzWYOfmhCEcUUuz-9DijBgi1TmdYKFHfABoOgn3eSzexzIDw5QU_dISCN8ueR7Q2xFDm0hGowGRerirnzASXH7CvIpAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=ZtKE5ZYkMxdH36msxvKIhexsHXxvjnrn2M7yeaAJwmlnvuAXIeF_t-y1K5sIK_KbBjI0cujP9IJzKSyJckqivBjSKh74xvzM6jX2HyFH2HUPE7T7fBqVFpyuzY6k4ae82J3xKm_LyBVpXWHvZZLHcwVMcYczFycVJtzFzhLYOhhQZFHa2H6m1oLS-Mor6vILy87BFJVKe6xqHas6f-u3HGE9YKq1gOElfHPXkgqNUeQUgHMWyljFpG8BWNIzWYOfmhCEcUUuz-9DijBgi1TmdYKFHfABoOgn3eSzexzIDw5QU_dISCN8ueR7Q2xFDm0hGowGRerirnzASXH7CvIpAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrXtjiCQAoCxK9RFcRkSKQyzd8PYP3MA2AGGGU44x1_w7NZ0e2aM9oP0SjO0MsRZtzBlVBRlLLTnAi0zigbECRX1lebgdYSXNEdDeKNqSJ7XfCwQ24x2em7WFptYPCDOH-MWNzJutvlHN1TKtbpv4qPejD-F8Rm955TP1jdyNI8ms5sYlpjFLOQIUXyeF-pxPfswjovayQ7oc2VxDqm_4qtPvRYcP1kqLoVTjyCy3gBmRrXQQJAHYyqS3G1ALtLdp97O8V722qpBzU4GTP2s3I8dXiUU9bMkj-TRHdMG53TTPus8OHMobwXFoHLQWUVYraCiMfpzmSQ1dR-72LATsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3ZIUuDCGGcRjyDogkkq8G8KIi3WnZDqUE8g05CoGuQXrJ8dLASfeVllm2SqcGhBwcwafu5hwNHsjbIHWMnwTbylJmXtONnePBMmwqHtZY6iAOYKFxhju9jhtaGZ06cP5MjJa1ys0qhjhqy6tSV-nfh53zhPFEQu03mwjUMUeqxbYQu97EqagVi9WS59FsKR4dEVPWewSlE15fa5kz5BpyOOTRhxEIX2Bxdw8Mej-0DnOeebfEUJqDeKj8MCpKLGrnZydePJZ2ycDSDd2FWuKDF6rkff_XaejDbVA0j-al04fZVvmDqjo96vgosh7UnETbL_loW5i-yc2gAT8ofDWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=Vx-Bk5YuA2y8Up1dTzVohr_Tj5D2KuEVJMurbhcMY8bppvtJlAUAN67wEM0LXOZNB8hvI-I7kGK8e2WYlIxzX3CJTeQRpbAh-DI3rQ4oz2yaRPXMCnE9TQyn3yY_RTKsRD9kMb7EG48zjQ_wvcAX8-rLRH9bFemLYqhWAJ5CSufHTk6MbeU2VAsRxYdLeL76QEnRTqLUY6P9Qt_fE0EuIg8LyO1z4BfoX9ATXCVfiqgsoYqEJ1oOK8Uc-DbqQyl5nWfbsa7VsfU5PeJlN6vlB8oulAKgT6xiFyQpuMH47f-iXsBcCS9BpeHHHUQYmSGy3JsJXBhfAN6ZigqYcm62Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=Vx-Bk5YuA2y8Up1dTzVohr_Tj5D2KuEVJMurbhcMY8bppvtJlAUAN67wEM0LXOZNB8hvI-I7kGK8e2WYlIxzX3CJTeQRpbAh-DI3rQ4oz2yaRPXMCnE9TQyn3yY_RTKsRD9kMb7EG48zjQ_wvcAX8-rLRH9bFemLYqhWAJ5CSufHTk6MbeU2VAsRxYdLeL76QEnRTqLUY6P9Qt_fE0EuIg8LyO1z4BfoX9ATXCVfiqgsoYqEJ1oOK8Uc-DbqQyl5nWfbsa7VsfU5PeJlN6vlB8oulAKgT6xiFyQpuMH47f-iXsBcCS9BpeHHHUQYmSGy3JsJXBhfAN6ZigqYcm62Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=rqGkfpRMm0TZlp85RprFdB3VkIxqa2KTxDmDEPiarkd8_Sx4UP5KNHB7zuaNGQC259gHikN7KA7FNZ5xYMxoqFPNwzVv0nmzmTuC0x9dsYdODwAKDgkNnFMAoFqoq87ynJgr_-M9K5uFS7A9JJyhBidArvYBLMnyfSnwRc78MUPOj2l5740gCrX0brES2NbV0RhYygMvDTldceNKvWT26SXNcDBWOky6ydbQT7vv9mk6jr3Qk1p7EBNQL8DlYe6LWO9FRJDUSKj15cOidDuCtK-ySYcYIz6_U_MCZX6Oa0d3RWDpM976KYgGyccdHh4vILmHibnc8K_5E_QCf6i-jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=rqGkfpRMm0TZlp85RprFdB3VkIxqa2KTxDmDEPiarkd8_Sx4UP5KNHB7zuaNGQC259gHikN7KA7FNZ5xYMxoqFPNwzVv0nmzmTuC0x9dsYdODwAKDgkNnFMAoFqoq87ynJgr_-M9K5uFS7A9JJyhBidArvYBLMnyfSnwRc78MUPOj2l5740gCrX0brES2NbV0RhYygMvDTldceNKvWT26SXNcDBWOky6ydbQT7vv9mk6jr3Qk1p7EBNQL8DlYe6LWO9FRJDUSKj15cOidDuCtK-ySYcYIz6_U_MCZX6Oa0d3RWDpM976KYgGyccdHh4vILmHibnc8K_5E_QCf6i-jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqy87XqbsvimfGQiBarFWtQ4Ez0bbTr-Viy4CtrUo5z5qUCynjC0xu_ObwEtroOWmAscN3B1NjNqAArWQtcdTX0F2TXF4CjKpo-PeD15nMHZdBI7mvMYS-6FCCnwyREAcvTP92zd8V1Qj8UX63xA5Iyr45He8YrBXfYNp55uAUaK8peHFHj1uhgfWGBjMqBDkJJhk0uea4MHSv97f4yY4io7233xEvQDfaBhzQjkNQZi9htM865yvqPbN3i0YWWhN7J18Iz2ulpNZGIiodlpNGESEM6cRxXWSOxp7c2FpbQuANbskqSEdJZirHKs-jWO5Btp58x8QFaeucXMnXetBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgojVoNytRLF_9Rz1xVCV316xpkOVarQuJ1qLenpgwYxDyrF3Z-uhn7i75o5Iy4khrO6UBz0kfy1Snp9JiBH1uWTeBZkTVh1EyfOELp_dY3UFf4jxy40GbzMj33k3VMq7i8YAED-1eZRubpOoZ5vLhECfHkcFxaueYn7tspxeBcFXdWCGpzG-K_y7q_siOHmduPS4oTgT5XuYjFCBBn2k4mFHJ35ujIU2nJVdmGIv-EjbUKGwgP-aK8mLPxYGCe7ryH6q1BttZaCvvj4e6cskMukD-1EbW7qx96Vxc4srXFtwMIC-eVUgdr8w8Fodgp6JB3onorKKG27VGnVPP5lOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bk7oCARHj2PEceRqRmc5SIGLHoTcXk8aHyk12FwLqZBQiHhg8nZMlsE0MHl228g1BAyoygloqzGUJR6EKhMq_G0oXiBCaAMC_XHaUeApyUUv9MJ2ia2yw5mQVZlxsaL9vfFdgucewL5ne3VO8DbMSgWgiOAz7c6hSJJhP7f-67clQmWJY2J85q30QghXyYsDrRtaZBWqAsewEr_SWCCEgZb4zR9uSgxUKkYzwLh8or24x6feCrvNFjSuQQeNwP0WNosn2NjuSEQ71EX-ubGbV9TxjAN6vyphv0A_RgUv2Jjxo0fHq4B_FStwClTcHFWk4AOIN6NmzX-CClT0vVvrGQ.jpg" alt="photo" loading="lazy"/></div>
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
