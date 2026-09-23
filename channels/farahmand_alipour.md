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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 04:16:56</div>
<hr>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UniU-uEYV0773F2efC4bfQJnDDp44MlbENld_-xi2zstdhLiwBrzAepqLIQMxW8lI5rZQW3AMcPuS-eYGRRuC7S9Eh20d9-ljfne6EqofLKSnqLW4ieykoI1fDaGKLtz8KCqU9vTsYz9xbdb5mZnUHNIHEOzykJzh0_5UmnT_06in3KLpSQ_7Ap7P2Vz-jfa0bZRZueBh8iWRrlD6okwHSU3yGKjq6_suCoVrHi18Sz4HPkg3Yi0Bu5-lTUUNzp0Nno8pEHjIO1HyVvu3RupNvwes083Ueb-iwkmy3J-FxU0x_FrFZxjDx9kNEx0Htec2xjDPzl2iLtzqanrreR7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=jfeq90OnC9iVPk6w_ysqzNLND2mo-7Ewzahn7-lfRD5MJTuTklhz-KWdTEXQj9mI07XwRpXDuuBLFb2cVcr9OOiBL1aOmCAQbjhL9wxme7x6AeIU0jnOB4olD-QQUIDu7FphrXN8gvjgR24AaY4c0iDajZuFn8gGXggCMLIv8AQUpoY6mRnA7_X9t17yavi6fbr5wBjFSR5j3VIKJ921TUmXDIGSepk2XsUf6-KQ3NGZy-Tlq7jEubSTiIh6DFekww5WIUkxDgTItGQkyp9enLN5mirZJtMXB-92aQ-xL4EAh6zbgbtgzd54D_T7oPJnpd9mFvusY55rAyCe166F2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=jfeq90OnC9iVPk6w_ysqzNLND2mo-7Ewzahn7-lfRD5MJTuTklhz-KWdTEXQj9mI07XwRpXDuuBLFb2cVcr9OOiBL1aOmCAQbjhL9wxme7x6AeIU0jnOB4olD-QQUIDu7FphrXN8gvjgR24AaY4c0iDajZuFn8gGXggCMLIv8AQUpoY6mRnA7_X9t17yavi6fbr5wBjFSR5j3VIKJ921TUmXDIGSepk2XsUf6-KQ3NGZy-Tlq7jEubSTiIh6DFekww5WIUkxDgTItGQkyp9enLN5mirZJtMXB-92aQ-xL4EAh6zbgbtgzd54D_T7oPJnpd9mFvusY55rAyCe166F2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=U5CkOahV_Wx88n2JSsg6xLtYy6KGaEqBhcmtvZGhDXQVa9_JF2DvNti58YtaPmzywTWL1THiJ-TCVXfDndMXDxSZZ9_t9juOHH8WuHDXN60eXgLbvmHiEv_v-gDPInPgGAHOGbx8i3ctMH4U2DRPg2jS_y-vapCST-NLhQ-JDotd9UYqoqClQZszWOcAey40_lM1ayEenfF_DFkYoYuSIVV8ollpBJE-qU0CbIPFO6XAS3PKW0Fs1fCVdYJHnyCgK40bwkhaTEzNX_7TpgVcwed1sE7F8sO8zQvDTKz-GeckTXE8u3eqS3eIAIJRbYzmxZ4kKTVWMaBb6NERagFrmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=U5CkOahV_Wx88n2JSsg6xLtYy6KGaEqBhcmtvZGhDXQVa9_JF2DvNti58YtaPmzywTWL1THiJ-TCVXfDndMXDxSZZ9_t9juOHH8WuHDXN60eXgLbvmHiEv_v-gDPInPgGAHOGbx8i3ctMH4U2DRPg2jS_y-vapCST-NLhQ-JDotd9UYqoqClQZszWOcAey40_lM1ayEenfF_DFkYoYuSIVV8ollpBJE-qU0CbIPFO6XAS3PKW0Fs1fCVdYJHnyCgK40bwkhaTEzNX_7TpgVcwed1sE7F8sO8zQvDTKz-GeckTXE8u3eqS3eIAIJRbYzmxZ4kKTVWMaBb6NERagFrmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHX55iI1BW81CKqZcPQdfvzGIWvggqSmU1nk8jeRoAUMzYhE-5I2VOOA1GdJboNet7osvVQAMU8CRVh2-FALND1Kj40Gj4HmQnmz7d1GEJhoyivyTjT4hCOzwFO80UOlf827nJwtFPk4Jw35-7Vpcx7MKoGvsicib76ISJ_WmEd9RFu7bjr-9b97TphtKgt454P-HL6fYokpBvwo3hD5mzVoBJUcEScCaySZVkjgwYdgYKjbE622wtMJkZxebVsikUKWuW6sQLpa5vj_DEFB8OoHd6YUdY49b722YpiGC80j5LyUYJSOU0i_dUo3L9yej4CCNDtRsr46gYvIgPFszw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8GlGzw1nBK5JXaSGjgRxOFCgTcpC0xWaxW4Wg3xoXq3uhZkhVtT-DfJZNn2GS0kheq8RsVFqLEZ-qznhx8HNZSIn1EnMJ5QMiOQz-ULtwqkG5Jrm0dZGKimSS0I4dB59DI3fA6ZUKuBQrCVRUHXLPNF6lbKpWt50UYPAv6riilK4Mm-hRg0J59a75Z2Yzdqfe3M9KTAcM8m_tW7ozVV4P2bAQGZUQkWRMO02snS_L2bONBcROFY5FXQlifa2j0sxW-MTU3OoKlXofzICA3RnSOFIhujgXMpQisYOAwCFbQovwiD2WX_HCb7P96QdZlfVh87DASESsN0oLBHyw161zmE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8GlGzw1nBK5JXaSGjgRxOFCgTcpC0xWaxW4Wg3xoXq3uhZkhVtT-DfJZNn2GS0kheq8RsVFqLEZ-qznhx8HNZSIn1EnMJ5QMiOQz-ULtwqkG5Jrm0dZGKimSS0I4dB59DI3fA6ZUKuBQrCVRUHXLPNF6lbKpWt50UYPAv6riilK4Mm-hRg0J59a75Z2Yzdqfe3M9KTAcM8m_tW7ozVV4P2bAQGZUQkWRMO02snS_L2bONBcROFY5FXQlifa2j0sxW-MTU3OoKlXofzICA3RnSOFIhujgXMpQisYOAwCFbQovwiD2WX_HCb7P96QdZlfVh87DASESsN0oLBHyw161zmE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=W7u5dc-51Dt-LHWC-WFuw9Ji-jL0BcN025g-K8BByOcfqzmBFoeVPANjG1Xh7TRlfq2Dc-lPwPNJ2DrNql5cxKkk8xf09IIeLppghI4swgEpCRChHFA2oqQqpr_19CwOgXsuIhPDgNUYgqQc7zV5BnFDj0zuUdt4aeltjDUwglpo3uTvntnA7kRE6KJJKZUb9u7a8eTX8od1znulb7TnRWuxIixubgst0w_weVQGV5xLiGoC5kvCXO7-WAGWusHX3njT82vQSNLcOxqmYUs9b2mUIA8fW9WvMV60G18IOe8ZcK0CZnXs6Q7eXmaizPHgJH8oRJxUvg0SWCsnCKR0Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=W7u5dc-51Dt-LHWC-WFuw9Ji-jL0BcN025g-K8BByOcfqzmBFoeVPANjG1Xh7TRlfq2Dc-lPwPNJ2DrNql5cxKkk8xf09IIeLppghI4swgEpCRChHFA2oqQqpr_19CwOgXsuIhPDgNUYgqQc7zV5BnFDj0zuUdt4aeltjDUwglpo3uTvntnA7kRE6KJJKZUb9u7a8eTX8od1znulb7TnRWuxIixubgst0w_weVQGV5xLiGoC5kvCXO7-WAGWusHX3njT82vQSNLcOxqmYUs9b2mUIA8fW9WvMV60G18IOe8ZcK0CZnXs6Q7eXmaizPHgJH8oRJxUvg0SWCsnCKR0Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmGYFcw9RaxkLeQGdNG3fKATIesq5DCXurXTquc-iZX8cjL5_VEjDiettKKBpkVZ4ZBKlN7P8a8Qkgp2ClqC2ZuFDJv65BWxKkBDaTb2H03XJTXDrfzW1TTG4mXTIQ1OMTthjcMl9wR_JHQaajYFaKnvXBRrpFnIrX2Unu_LJS2ORWXNRGAeuSVKwu665BeyrfKSnWD-tBgHiE1G_siFIjnpkXztaR650vSP_zi40LFhgkWUHXADoM23lbUsfj5VFHyoJlhoukAZhFKQbCBrCKS5APvsPcAyJDagkOvdGo86ntt4AJ7icJZbqRH96cWnv0JuxPKGQWEwK2e_0Nvckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=fEsmx-kOPr6SWmyIVh-DhKhHgevv4-ekGwwpUZfgeq1tFAvkRtF-MXZUnSulprgsB1wRSQSaGgrIrxC_RWLs-OabyZ9edvj6Qy9TlW_coRZqcQXScguzIn2DwvxltfJTtVSu9XRVTwz3pOcgMlO2uGkCNeScehMxkWFQnJcC5D34qa5dKSUozweevny632hH6feyYrj9bqmb0aI1eKSs6afojFCx93vMNgVRG8_lycfhCx02u00UndrMEbMuF18PfF1WLxufs09RoS1xYqFczJQh_nMupx90LzZRmqV7SGjy1g454c183MfWEGIZ-92gb1i678V0GB5qOQjJijC2Yp20s7TfdABeTjkkY2HW61wwunhZL9BtcwzZSVzIKl4EwFcVrdhH61d6UqtIjlCtHr42DVwlLjT_GFT6Xbe5fMij2dca-7-qJAfB_b7FOergkjZATLy0Vw9ZcAZQyoJLnWeGbhbl9DZ5aiJWJlXrjP2FWIFXkXqF_h4bzNbp_n6e1c_gOZpGJ9DXe5-qjwHWi3mAmjHz5JIf7EGHoqTlLZjcTSDKCq64s_ZDQDTCVvZGo9Xa00QJN1I6EIQWF5TBYq93KeCZc8d2sT0rHSKFGH4WiNlcbfGCW_lTAwtQaHzH3a3PuBfKMLpKLmHB-ijJ7kkoAC2sB8VSKltPH9KllBU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=fEsmx-kOPr6SWmyIVh-DhKhHgevv4-ekGwwpUZfgeq1tFAvkRtF-MXZUnSulprgsB1wRSQSaGgrIrxC_RWLs-OabyZ9edvj6Qy9TlW_coRZqcQXScguzIn2DwvxltfJTtVSu9XRVTwz3pOcgMlO2uGkCNeScehMxkWFQnJcC5D34qa5dKSUozweevny632hH6feyYrj9bqmb0aI1eKSs6afojFCx93vMNgVRG8_lycfhCx02u00UndrMEbMuF18PfF1WLxufs09RoS1xYqFczJQh_nMupx90LzZRmqV7SGjy1g454c183MfWEGIZ-92gb1i678V0GB5qOQjJijC2Yp20s7TfdABeTjkkY2HW61wwunhZL9BtcwzZSVzIKl4EwFcVrdhH61d6UqtIjlCtHr42DVwlLjT_GFT6Xbe5fMij2dca-7-qJAfB_b7FOergkjZATLy0Vw9ZcAZQyoJLnWeGbhbl9DZ5aiJWJlXrjP2FWIFXkXqF_h4bzNbp_n6e1c_gOZpGJ9DXe5-qjwHWi3mAmjHz5JIf7EGHoqTlLZjcTSDKCq64s_ZDQDTCVvZGo9Xa00QJN1I6EIQWF5TBYq93KeCZc8d2sT0rHSKFGH4WiNlcbfGCW_lTAwtQaHzH3a3PuBfKMLpKLmHB-ijJ7kkoAC2sB8VSKltPH9KllBU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_4S1-Ixn4V2WL9cRyWZo7pb2VaNjZmJzLT46akFi1MuaZmRg2pEL_2Hebzl37i3uO66HJySCOJuTY9EvLZFpIc9pnrEpr9CiXHama4fG7Ftci_dimoO_XCSPoAxn06KDXdILz1ifSmLhB9MWD1ctZQyAzHXilJ5C9aPib_UP2dlwsnr7Pz97ZuPAbDcXdE8enIKjYwTlg0x__yZ3Q5sgYusq45GOpTMGPfCs_BmC4DIPO45ng_9QoOYsc1D_UY5HsawqZ_JPQSiHLMUFyBCt7YemfECKSonCbGitskpQR4-XGIM-jVS0jAcnAdbvUA6jLZWqSZn91bnsN3H7TurLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=ns_7W9afxidnvyVFI0qqE-7gkDg5AL15fBMwiJKr3a58Ku4BDUCYy9APNBKVXWoxCM8ZiK5_PEJBiq4NNhQSnrD1CpR7958vVh7tpQD4yxsSChlfhV5RDwb-_1xWgwLgZ1VY813SR7RjXpXwsdpeeCP9yEjgzR8bW3ZiHH_pfQqGEt-FVo20_gc0TB7vwyg_M8sTNH-9K4Lk6kLn6Qg4pj3jXRzMGWPypPkHWnZqucgbDIlViqnhnkcflkgzOxyZenXEwEUuvDLFz0LEQ5_LiY0_BJRmRN80d2MRj0tbe9XNBaYVGzOMsubu2-kJo9jA53rcObAF_n6gYZ-5KfdfTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=ns_7W9afxidnvyVFI0qqE-7gkDg5AL15fBMwiJKr3a58Ku4BDUCYy9APNBKVXWoxCM8ZiK5_PEJBiq4NNhQSnrD1CpR7958vVh7tpQD4yxsSChlfhV5RDwb-_1xWgwLgZ1VY813SR7RjXpXwsdpeeCP9yEjgzR8bW3ZiHH_pfQqGEt-FVo20_gc0TB7vwyg_M8sTNH-9K4Lk6kLn6Qg4pj3jXRzMGWPypPkHWnZqucgbDIlViqnhnkcflkgzOxyZenXEwEUuvDLFz0LEQ5_LiY0_BJRmRN80d2MRj0tbe9XNBaYVGzOMsubu2-kJo9jA53rcObAF_n6gYZ-5KfdfTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpPkCi6Ga6SfV9mV-B0SEhrqF7smrHQFD7yi4g3ZOzp-4RikBbytVBQhgN4FR1GuXdNe-mFmFrX23I7-WpO2f3ybCoqIbtCUZs_iO2bNXN0hQLmvC1EZXXGHUk8A9ICnBhE8A3ff-X5wOxB1UnlKj6hQk71sVef_uMUncTQoxX_c2rDaiUA0Z1QR0pOY7U0sZzusfirDrL8u1tusufh4m0jYtsd3YsNo-Hy0nT76WP8LQObMz7iq1y84_GSsULrWR4YTeZQoYvAsi6RQegBXcNtk3aNXFoz8D_V8kfejZ4sKlzJxIkpMuicFePryabqD40PmEMZkpGP3l1uYojbIpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6_KD8FkGiLJf74A5dr_aRp0tuwUDPnUpS9sqF96ss7SAMH5xisms3cMpaJ4GYeNW2CKvFlHA4TTBlIuENTpxsU7c4CCOzD_i5PXI1460TulnApB44saZNnT5dnfjH8yYt7kYZXIuIe7EKgMJYWf82lCOyyOrpFTvsY957F0jIplyXZKR5PI5xfLETCF5A1JJ9AdzyS0QvB-Q9ZvjiWuWdaOK6yrTGQEoe6VlGFh0x5pyxC0FsX485t7OHsV2MIbxajapEfi280XBh3egK7s905Hig51Mg_l-0fteYagVushPGYilGMQh-IMbtp_ipjFOWNPQve-nbKidfLLzVkIyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiUmfhrIZO9V_gu1TzncRpWNBC14hOLBzNsc1l7oGKksMYMM0o4HEX5tODnaNFZLhFTMHeFpNV9APWSKQhK7hIl1JFzy1MLy8C5IxTOpTGo1t1iN7VLwMnYohD2xtaJxhByBmjlNvEsUWX5Ac4RrAuJ9i9hkRbLi3hE21ycg62Qj6RWJCAqjxYoPKmMG9DMomOjV-I_XuVBczZoSxnIYlaIm7Z58HLrUb7IgLZw0KZudx-j0LvrulLdLjIODrYR74zCTcRKtaERh_6J2g-ZrbycOyhDzrSc63q7DTRjioyQudsqGozjtWjy-sc3NWkybmWuQUf50yy5en4QBv5W5xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=qmYbdjiaXgjp2FzIgZDW0uNp5DN8QQqdzTiWcbtdX_da99JN7tcQgmWLrxGTNrDNk4RhF2AeX0mSVZg3v522m4idbW7H1AtjHqnUg5G41xxO0cIsegp6XvwTqcsE-ZfnjEO57X4sAnLuS9tLIaQ2Xyw_bD0nTGlNnuCcDGbN64zTYJGytHdbVgucxxkI6jT0wkLCCTL3QlI2tunIZaoF7X8f9_ZXNDp9oRS-dfKVlUIDMEB8HaPbuM-MBvQmuGgcV-XK_ISLZlVHO9PJhPZSnDyPzAVSP6k6wax3kUyBLn4FD4EAnjgmyDwi7a4np5GJC9kdUP-tcBNTyZz5_kx_Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=qmYbdjiaXgjp2FzIgZDW0uNp5DN8QQqdzTiWcbtdX_da99JN7tcQgmWLrxGTNrDNk4RhF2AeX0mSVZg3v522m4idbW7H1AtjHqnUg5G41xxO0cIsegp6XvwTqcsE-ZfnjEO57X4sAnLuS9tLIaQ2Xyw_bD0nTGlNnuCcDGbN64zTYJGytHdbVgucxxkI6jT0wkLCCTL3QlI2tunIZaoF7X8f9_ZXNDp9oRS-dfKVlUIDMEB8HaPbuM-MBvQmuGgcV-XK_ISLZlVHO9PJhPZSnDyPzAVSP6k6wax3kUyBLn4FD4EAnjgmyDwi7a4np5GJC9kdUP-tcBNTyZz5_kx_Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9NlIE8kuAJ4MFH_-CyiBiPg3orGokQKZHLnCfxeR3LBm1puVCnKtpk3_9jrmQnfKUMyZfeE2-5J2Mq1YAOAdHSolui7wJcIar24C5dwzszlVMZpfM6hLCBbifRJbuDyGYzlskITQTTISZWgPHMTzNeYwD9uPZ2Ap0gOht6oBAjGNFE_syn1k0wDNMPNQ1DNJ-CSjNSL1z5pVIWa189cfJPEGXZJStHf4dWIWkSv6fjEfwNtt8Gwy98ZVCcSJq5SX3rKXI_9n-9fFekTqfHJBnNiupXS94sEc7IDeBXjEn7jgw2-ft7s0zNuFxnKPJHu6ouQbct8uEBPJwXR0ns69Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFL7ob7HoJLPc8L0w11yem6kRrdte95OhMpxvvDdubARTrzYbgHeJLwtBtvXwlIC1b8mU9wPdvqOxO7acqVxx_fTHwJhl_19PpiiYhi3AfLSiIgz_d72D9IDPY2nZzyVvIZo01HykVCDzBBjNBLn3S6pen3k6FfPx-Phx3TET-nqL2Tps6FORNVPDQ_CScCmt7dLKEqdUBZfd4gVK8WJoLmhwwxVREEvmD5xlVWhmLrmXf8NIHcS-eIyaz5FGJlQeJi5pLTRCKZXgg_Dv1B9ZfL9xLoaCJDKhWd6BB01FcBPHv09wRwtM8J-PI1264aSc6zKrSb_xg1o6qw4cEt4eowY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFL7ob7HoJLPc8L0w11yem6kRrdte95OhMpxvvDdubARTrzYbgHeJLwtBtvXwlIC1b8mU9wPdvqOxO7acqVxx_fTHwJhl_19PpiiYhi3AfLSiIgz_d72D9IDPY2nZzyVvIZo01HykVCDzBBjNBLn3S6pen3k6FfPx-Phx3TET-nqL2Tps6FORNVPDQ_CScCmt7dLKEqdUBZfd4gVK8WJoLmhwwxVREEvmD5xlVWhmLrmXf8NIHcS-eIyaz5FGJlQeJi5pLTRCKZXgg_Dv1B9ZfL9xLoaCJDKhWd6BB01FcBPHv09wRwtM8J-PI1264aSc6zKrSb_xg1o6qw4cEt4eowY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Ig1vsifTld1al6wUZ_d1EdZJgQ_avVatFZwWN4IYG8DFM-KUHtGmAN9a21Wzpb_sWBL82CKFpvm5pBYCfvXmUZo-gZeeaEHm-XyN8R043PqF3XlArMhfLP3pppnYyqymFgBmiRQPJY-2RWcHXu88eZzfykTNNxpJkDpQ1vgmcFvaXilnH038llVCSBjYc3TDX4jOp_UjtCfjcJP6hRJexCrPLM81Mmfz8R7xKqHvxH-LXF2naD4R0wAStb5US3KR9po7WIN_Ei_MfvmHsPyLa_vFcm96OucUiQo7nMrsotN4LzGQ0lvbVfltnYCdiUO651OG7rXyjWcUFCsHDCIwYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Ig1vsifTld1al6wUZ_d1EdZJgQ_avVatFZwWN4IYG8DFM-KUHtGmAN9a21Wzpb_sWBL82CKFpvm5pBYCfvXmUZo-gZeeaEHm-XyN8R043PqF3XlArMhfLP3pppnYyqymFgBmiRQPJY-2RWcHXu88eZzfykTNNxpJkDpQ1vgmcFvaXilnH038llVCSBjYc3TDX4jOp_UjtCfjcJP6hRJexCrPLM81Mmfz8R7xKqHvxH-LXF2naD4R0wAStb5US3KR9po7WIN_Ei_MfvmHsPyLa_vFcm96OucUiQo7nMrsotN4LzGQ0lvbVfltnYCdiUO651OG7rXyjWcUFCsHDCIwYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=l3G-_KTi5I-DE7NYuqHERFq3S_lq3xCTsDFaf0MnY7fsq4tL9W6tRtc3aby3fT-mjBW3JxUXIpzCkVTW7yG-dyWhZ3X_jF8UuL0jiBiUCob19LCX2eKYru2G1glc_5lmsLEJ9iL4Oy2jJFScZMbRkrDe8ehL_ETmtMdLnkH64MAaStJQfyXDEj7QmVZRx5q9e9jiKDdJiNXS1ZX_NZHEXDmi-6lNNrOl6V7QAHGQ2LUO36yt3FzfY3EGnGHZ64Xl0ut1P16inaCFS85U1pafkpOk9b3uvtUD3luVm7sqqhp1YYuAMU61VnM9u9evQ1yDXy1r-6U-BlQ-61hDQQOeYArTg7rnVxG6caw7qfiX2ULwQTCB820Z2FZjpOpS1NTeN4-x34_5gmDpYnqyD_BGtArVfWTqV6Befqs77MZNyQ3QP18CSFonO0piGHlU2QicNZl0HqE2VwX1q-KEJRj98IkOnU_T6NPnSAi630rJlgnLYa498KWKdT11VwgVp0Bt3dEWX9Lltfo-W_MPjlWXHAOKcZ4_I0mLZCkpVn9PpZwtBdxbHdDCNK4SdSjR2yc7bhA0CYe1uRcSyms8ev-QO-QoqoJAnqYUo8863iEfWWDL39cfeMMgGlg3Aw44ayngTfyAAVSLQ9j60nexdHCQJHP-8878S2_z4Y0GEjzdxsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=l3G-_KTi5I-DE7NYuqHERFq3S_lq3xCTsDFaf0MnY7fsq4tL9W6tRtc3aby3fT-mjBW3JxUXIpzCkVTW7yG-dyWhZ3X_jF8UuL0jiBiUCob19LCX2eKYru2G1glc_5lmsLEJ9iL4Oy2jJFScZMbRkrDe8ehL_ETmtMdLnkH64MAaStJQfyXDEj7QmVZRx5q9e9jiKDdJiNXS1ZX_NZHEXDmi-6lNNrOl6V7QAHGQ2LUO36yt3FzfY3EGnGHZ64Xl0ut1P16inaCFS85U1pafkpOk9b3uvtUD3luVm7sqqhp1YYuAMU61VnM9u9evQ1yDXy1r-6U-BlQ-61hDQQOeYArTg7rnVxG6caw7qfiX2ULwQTCB820Z2FZjpOpS1NTeN4-x34_5gmDpYnqyD_BGtArVfWTqV6Befqs77MZNyQ3QP18CSFonO0piGHlU2QicNZl0HqE2VwX1q-KEJRj98IkOnU_T6NPnSAi630rJlgnLYa498KWKdT11VwgVp0Bt3dEWX9Lltfo-W_MPjlWXHAOKcZ4_I0mLZCkpVn9PpZwtBdxbHdDCNK4SdSjR2yc7bhA0CYe1uRcSyms8ev-QO-QoqoJAnqYUo8863iEfWWDL39cfeMMgGlg3Aw44ayngTfyAAVSLQ9j60nexdHCQJHP-8878S2_z4Y0GEjzdxsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=VIPryFwA7USuuA5upTme1Hy8CXRb9jTbwMh00wS9fhyGyrK3JkBbxGOTkgQUCqEaLHQ9lEiq3yJB2AEntuQJF-wbqJ2bqDZpvclUetPE2GFOic1fIjpm02HsylCSKqPmYIFNlZxfpfKpmuJiswPMvj9CoTGQVpZCa8XMn8z7iWPtuY4uNwH0SfYra9a6eMqZtN0i8cVmTFWtQB1ohV-U_YD02XKE-wxYzKjcadKxan-mwyaOtxj5PgPaC4rqcO3ug_h9KYQYCG7ocv2JHsD9Q2hJ6xGq2ITfn9O8PpAxGY3Kw86aipuEba0__f5yhSrwZf8Z5wfRIwfV05hHJ7nJGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=VIPryFwA7USuuA5upTme1Hy8CXRb9jTbwMh00wS9fhyGyrK3JkBbxGOTkgQUCqEaLHQ9lEiq3yJB2AEntuQJF-wbqJ2bqDZpvclUetPE2GFOic1fIjpm02HsylCSKqPmYIFNlZxfpfKpmuJiswPMvj9CoTGQVpZCa8XMn8z7iWPtuY4uNwH0SfYra9a6eMqZtN0i8cVmTFWtQB1ohV-U_YD02XKE-wxYzKjcadKxan-mwyaOtxj5PgPaC4rqcO3ug_h9KYQYCG7ocv2JHsD9Q2hJ6xGq2ITfn9O8PpAxGY3Kw86aipuEba0__f5yhSrwZf8Z5wfRIwfV05hHJ7nJGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7kfQs5t5V3aitacB3k70PyVppbncoWpHbU9VBc42KiczhkVx2oP0Yld8JsO36GSi6UcSCwkTJHtwugcv34N8hZh86SAVyX0mZhElwpT64WOz97s4q7LNie5HKwxk9eBqJg5ffAPsmUkdDfREJF1zrkMQNo7ZO47PZoSjMSVl5mwunYBFL4XhIGaQ4zcOFI4JTR2VFSS7WM5-Vv88qa5xSlsz8h0PmlNTb8FmNaE5iZFFiA4Ck88APT3OoJ3vO52-vDkmM2vAkdCtRibaLraVvj5HHhp-tRZhwUo3ZB6DTnw_OyZEZ0tPUDbbb7ItTrle3VKbigWVknR4pdDoDjfcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=BnTSXpLbIUQFDU-Cu_tcePIhrCbRLlINN23xekfdnOnQjfEnUHdyxU_R37YDDqoP7TWQxa0z9KNkHP1fVBPRDKySFBHcQXD6Dw5tqcSjl1JETvNnzR2XUUgSqr_uYTI5hJs2z_Q8byNX1PjYxwSLs1QgFc1wHp1e69J5iq2eoezk-Qxk14QngrtJFseLMrsQOJJVWhGcGTUBFMynEl1cKD705nO6kNE-CbOXnBt-lvh6fdV18t_8mEqM_rrMphoREkJRooVgccyyiJbxhnX2mS2UH1wF2vcD9U2-FnmI5eQIhargAz4kvrogWMI6DTlwa3vC77ib0-YotJhg_v1ipw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=BnTSXpLbIUQFDU-Cu_tcePIhrCbRLlINN23xekfdnOnQjfEnUHdyxU_R37YDDqoP7TWQxa0z9KNkHP1fVBPRDKySFBHcQXD6Dw5tqcSjl1JETvNnzR2XUUgSqr_uYTI5hJs2z_Q8byNX1PjYxwSLs1QgFc1wHp1e69J5iq2eoezk-Qxk14QngrtJFseLMrsQOJJVWhGcGTUBFMynEl1cKD705nO6kNE-CbOXnBt-lvh6fdV18t_8mEqM_rrMphoREkJRooVgccyyiJbxhnX2mS2UH1wF2vcD9U2-FnmI5eQIhargAz4kvrogWMI6DTlwa3vC77ib0-YotJhg_v1ipw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=LOd1obijZ_S2WcGiVEAyDYDfC8U9HhbPCWwz3xEBhGM0djb3izO_MdTYLT-we-03dyEOoOMNmet5jho0dIUgEnliXEDMT5N22QKTTfEkvIwb2422hUEKLQY0y_BC6XVhYZ12C-LCB0Ci4b9Ij-wjSbstagEcbQdVKJIDHve35w4hurVuxsaxlPQWjCxDLYmK-Pb8QjswMbDoQ5dLrdB-q_Dj-3HkFipaxmlPC7J1lG3ylAMX0p0dE6fj4tZVLKW_8ggP8ucic1bZhiUMB2pNZXs0jyhH_sToWL_3RSvmK4CRZyPS7nsosPkQr-X2wza2sAVnaIOUl4yjBxU62VUZ5kkAyQ_NAIeHh_R8XD_b5eA0dVIY2DIB7t4czUDHMT2n5wXVwtLHS7hmPN5RkV0cJGfLoPg26PEddCgINwTkKx-46Y6uPWKodtkvzO7iD8AgPYdEC-ONiz6qg0jjnZknVlk-JDiUhEQGkzcnw33WxKzi2fFr8xwTJzcFZlrsws6ZnJP82NaorYJC8XV-pqxDsil3UGQJ3HrztYBBg-uVIKCODbNwowAziZpNoDa_9hc-k7TPbAIittQTl69DNKxOQYNkDelgmzKyrhe4S_tbIAlF0huhjC7nM_-kkc6H1RrdPv-Byy8NNosldjz3AgT9sUyIWHJP2T12RHHTF8NjhhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=LOd1obijZ_S2WcGiVEAyDYDfC8U9HhbPCWwz3xEBhGM0djb3izO_MdTYLT-we-03dyEOoOMNmet5jho0dIUgEnliXEDMT5N22QKTTfEkvIwb2422hUEKLQY0y_BC6XVhYZ12C-LCB0Ci4b9Ij-wjSbstagEcbQdVKJIDHve35w4hurVuxsaxlPQWjCxDLYmK-Pb8QjswMbDoQ5dLrdB-q_Dj-3HkFipaxmlPC7J1lG3ylAMX0p0dE6fj4tZVLKW_8ggP8ucic1bZhiUMB2pNZXs0jyhH_sToWL_3RSvmK4CRZyPS7nsosPkQr-X2wza2sAVnaIOUl4yjBxU62VUZ5kkAyQ_NAIeHh_R8XD_b5eA0dVIY2DIB7t4czUDHMT2n5wXVwtLHS7hmPN5RkV0cJGfLoPg26PEddCgINwTkKx-46Y6uPWKodtkvzO7iD8AgPYdEC-ONiz6qg0jjnZknVlk-JDiUhEQGkzcnw33WxKzi2fFr8xwTJzcFZlrsws6ZnJP82NaorYJC8XV-pqxDsil3UGQJ3HrztYBBg-uVIKCODbNwowAziZpNoDa_9hc-k7TPbAIittQTl69DNKxOQYNkDelgmzKyrhe4S_tbIAlF0huhjC7nM_-kkc6H1RrdPv-Byy8NNosldjz3AgT9sUyIWHJP2T12RHHTF8NjhhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DG72Ez0K4yb6f8PSFGU9AcRSCoSYtTni9ttzvnFZ11fPAVb_K2hzYBRkYcfuMGEDQUddze91g_IRfRk0HwMzK13m0dP99pW33lxfMJ_coAlW2ydKNGNzRF1e0Kjnq3FatHWnzlF5OWck3u9ODLOYPy3jkM5SSjk57fngBcDHiY0aJdvPcQim5gEHX7sQ_uiP4V9tdhtLPFOBOIjHExOoUeGkYUMr0hKLe4yl9q3Km-ymXOFJI29GT6B6arPqTKq-vGeocvDHGO4fwlTCAg3RrP0G5q3Ov5HN9qVYQnZFbMOL5H1GAb6bnZIon7y-Uodgtvs-9yuPhoW_SpH7QCmcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=dYrqo3Uw0i_QkbbKX6HIKeWwWl2GsFtGJC7fBvTAiHV69iJtT73kS_yvyk_2aqF11JKV7XjL4oQteDviOfNRLhkQJnhZGrHtfsT-qnpQNNfhp8e2iT1tS3qqhRCRiWrz4NDlwkHy9IMqJEhqBvHRoZLKn_JF6nJ0q743KSoZJbF0_P1eZRgmr4elFfnmgP8A5OOxZwHZfElxwzK98uAdgC8RxXhDDjzNkvMqwaZR8ZZOJGuW-gMQ7nOEeTSNwVpGGNW4skjypI3twv6dePCZHKu61tJqxmXqo4DKhPyiXeTZ1HoSPgHa9u1cVE_XjBmldS3cXJyoIWQ21cqavTPlr2btgnBay61BLUErB1o9nCKsKD_VEmuB1zYz7H-12Hhs0h27ElkC0WDOSAauDZnm741du5aFj0fMsYm_jMXFvrjE1xb1STsPN0rR3xCd3mSZF2xDiU2JmIKSlUcMjvykS2HXPuN6WR7uCVAQVNxOnkaazJ2htlxHzkQW76K2croPtChTP_gL6ySW4EdefDLqVIVzv2h8TXJxUyvRWiTIF6LL8L_Z3FETh98ZQpeW8W6pHH-AFLisfIZrl-QEM4zVF813DGMSDLSZryBa2CKjVmpgJT0me8R46MgVQvrBC9K9HFdz1AGTnmFb9FBa0qww77dSeJBWrBAeRX8RmEQjpNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=dYrqo3Uw0i_QkbbKX6HIKeWwWl2GsFtGJC7fBvTAiHV69iJtT73kS_yvyk_2aqF11JKV7XjL4oQteDviOfNRLhkQJnhZGrHtfsT-qnpQNNfhp8e2iT1tS3qqhRCRiWrz4NDlwkHy9IMqJEhqBvHRoZLKn_JF6nJ0q743KSoZJbF0_P1eZRgmr4elFfnmgP8A5OOxZwHZfElxwzK98uAdgC8RxXhDDjzNkvMqwaZR8ZZOJGuW-gMQ7nOEeTSNwVpGGNW4skjypI3twv6dePCZHKu61tJqxmXqo4DKhPyiXeTZ1HoSPgHa9u1cVE_XjBmldS3cXJyoIWQ21cqavTPlr2btgnBay61BLUErB1o9nCKsKD_VEmuB1zYz7H-12Hhs0h27ElkC0WDOSAauDZnm741du5aFj0fMsYm_jMXFvrjE1xb1STsPN0rR3xCd3mSZF2xDiU2JmIKSlUcMjvykS2HXPuN6WR7uCVAQVNxOnkaazJ2htlxHzkQW76K2croPtChTP_gL6ySW4EdefDLqVIVzv2h8TXJxUyvRWiTIF6LL8L_Z3FETh98ZQpeW8W6pHH-AFLisfIZrl-QEM4zVF813DGMSDLSZryBa2CKjVmpgJT0me8R46MgVQvrBC9K9HFdz1AGTnmFb9FBa0qww77dSeJBWrBAeRX8RmEQjpNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=oiHOw3tc4dn2FJ-H5nho6F98YTpPf-5qFCpj6xxOU_bSWKgiSo1V8F4R_bXVDxUX4M8ryM1F5ziivAC6PfOjADjA6SsFvHWh3uxkuqMWO-trLexJRcCySe4uMo9SvF_jMjU6OS0JbEftRaQ-1LGkMrZtRFfqOBTfcX0saexC5DMq2vWbD7aD3b0LdYFH4fmrfYCjVfRyKCaGub9G6JMu-huOdZ62yCOu1UI63GhZaOjDCmPOvWOABbAObxZIfNbz04XCOGCErzorxvMERLdqgZKFKeKGdmb3QRJV6eh2HqOC8maGasE9q8HjgeviY4JhJUNeTg4UksILthzRoivB-wquUd1DGFZgfLF-1gPOtoLZDCTET-NCaNJLS9xN_ZHVWhTYqLChyGn4gy0TV684bxTW0fjwV6NyP5PvB08zEvZ1ycW4_r8zIbESQ2vfsoggPsTa2LjeStvCiaKRTO9FgCAJ3RpG0gQkBel1SoiGZTNa10RrbaJdDe_jGFJKV9kpMCFeeyMiLSF_4oe84CcXKCB3CWmBAwpM8WnScvJ3F9QPKeNVQwXYv2aSf5QnT9VF-6jrkqbrAJpqcIywdutvvRIEEK1MEabx41kGZ8CeoD7e83AFpWJ_3nQUQEmEHJXZ7Cn5-ZyZ1fR7-y7JfL6jb9SCCwaHyZ8_hNSqAemq1mk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=oiHOw3tc4dn2FJ-H5nho6F98YTpPf-5qFCpj6xxOU_bSWKgiSo1V8F4R_bXVDxUX4M8ryM1F5ziivAC6PfOjADjA6SsFvHWh3uxkuqMWO-trLexJRcCySe4uMo9SvF_jMjU6OS0JbEftRaQ-1LGkMrZtRFfqOBTfcX0saexC5DMq2vWbD7aD3b0LdYFH4fmrfYCjVfRyKCaGub9G6JMu-huOdZ62yCOu1UI63GhZaOjDCmPOvWOABbAObxZIfNbz04XCOGCErzorxvMERLdqgZKFKeKGdmb3QRJV6eh2HqOC8maGasE9q8HjgeviY4JhJUNeTg4UksILthzRoivB-wquUd1DGFZgfLF-1gPOtoLZDCTET-NCaNJLS9xN_ZHVWhTYqLChyGn4gy0TV684bxTW0fjwV6NyP5PvB08zEvZ1ycW4_r8zIbESQ2vfsoggPsTa2LjeStvCiaKRTO9FgCAJ3RpG0gQkBel1SoiGZTNa10RrbaJdDe_jGFJKV9kpMCFeeyMiLSF_4oe84CcXKCB3CWmBAwpM8WnScvJ3F9QPKeNVQwXYv2aSf5QnT9VF-6jrkqbrAJpqcIywdutvvRIEEK1MEabx41kGZ8CeoD7e83AFpWJ_3nQUQEmEHJXZ7Cn5-ZyZ1fR7-y7JfL6jb9SCCwaHyZ8_hNSqAemq1mk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=olcRTv4rsSStiJeJ2lYM6cTxumJzHLL-Irs4NaYa6tB9py6YybiiiOPeaWbO50NeV3YkV9AMJHijxWuve0YE2VEDaU0MFgbzxR89ewqKemII26dwBFEjXiEMWO7PykH-oakiMW27dd-JPWqmtODki3WzFw_gMYIhish-vXyEqg3SEJRY1ANn1hXLJlW_gljmxcCF5xX8LeGlyBiuCqmULCDyRq0SVlRhwwO4GgiIFarc_38wUBAzNn3sipwfMPRzREPMpORTTnIudmzCL8e55XaUeZV_0cqQ3Pnduo_F2U_8J3pXQGV5-SREwk1ftXSVtoiwyEe43FXc96EhNw9Htg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=olcRTv4rsSStiJeJ2lYM6cTxumJzHLL-Irs4NaYa6tB9py6YybiiiOPeaWbO50NeV3YkV9AMJHijxWuve0YE2VEDaU0MFgbzxR89ewqKemII26dwBFEjXiEMWO7PykH-oakiMW27dd-JPWqmtODki3WzFw_gMYIhish-vXyEqg3SEJRY1ANn1hXLJlW_gljmxcCF5xX8LeGlyBiuCqmULCDyRq0SVlRhwwO4GgiIFarc_38wUBAzNn3sipwfMPRzREPMpORTTnIudmzCL8e55XaUeZV_0cqQ3Pnduo_F2U_8J3pXQGV5-SREwk1ftXSVtoiwyEe43FXc96EhNw9Htg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=BgOOQjBTwxQEqTyBywMDKWS40dnxSwUI3CfKgtjTb6bID1vRgmYz4B7RjvYhmisTD3L4KaB9WGDfsN7X5kBMEXpjDT9nmyGBGeNNkiQroauZ7vUr3InaSQYt0744DmQpoSZu9BWw_PE9gPGHhnvHDdf5UXopQq3xvzTeQwpYBiSwZgI4lsQkcyepdg4FqBhly2YhDoWXb9Jk2_lUdsG0dgYPO_L6uAPIcgUQ3T63MvI21W5_p0IDqj87HJ0MlJWbNw9ZGBdCik--GlfdzVv33Y_KM_wQ43xpCJKrCv53PNGnooJRRVoDzkf9aSoUyaLrjM1dfKosR9-P8cxkABW9Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=BgOOQjBTwxQEqTyBywMDKWS40dnxSwUI3CfKgtjTb6bID1vRgmYz4B7RjvYhmisTD3L4KaB9WGDfsN7X5kBMEXpjDT9nmyGBGeNNkiQroauZ7vUr3InaSQYt0744DmQpoSZu9BWw_PE9gPGHhnvHDdf5UXopQq3xvzTeQwpYBiSwZgI4lsQkcyepdg4FqBhly2YhDoWXb9Jk2_lUdsG0dgYPO_L6uAPIcgUQ3T63MvI21W5_p0IDqj87HJ0MlJWbNw9ZGBdCik--GlfdzVv33Y_KM_wQ43xpCJKrCv53PNGnooJRRVoDzkf9aSoUyaLrjM1dfKosR9-P8cxkABW9Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=qrtmq9LyN5CTKidDLE0QbhQpMczvc-NJsqMiujPayCS_Ucp7zZTlEwA2qNDQLMat8DgG961W9gfnSB1OPmYnlOhcs4NVY49qcU75RNSu26elKm7EkSUwl1hrsut057YU2erULHjoY2XhK9a0hRCT_3zd53Odl2wl6nGiAbp6hfa_PxWsXSS8UPW8W8karLLKFVdBSZDiGWotYCVJ4n9V2goVbqUANYMEWUzVjQET-2Jt_trsn7RvA0Hz1f1wRYsJ3_x0efee6FzrwUKpjX5TqFiJ9stFn2p8BQSWI87I2VIspysvOYziwu2QFOoT82bBbxyMZ_4a1k6Ennygtj7djg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=qrtmq9LyN5CTKidDLE0QbhQpMczvc-NJsqMiujPayCS_Ucp7zZTlEwA2qNDQLMat8DgG961W9gfnSB1OPmYnlOhcs4NVY49qcU75RNSu26elKm7EkSUwl1hrsut057YU2erULHjoY2XhK9a0hRCT_3zd53Odl2wl6nGiAbp6hfa_PxWsXSS8UPW8W8karLLKFVdBSZDiGWotYCVJ4n9V2goVbqUANYMEWUzVjQET-2Jt_trsn7RvA0Hz1f1wRYsJ3_x0efee6FzrwUKpjX5TqFiJ9stFn2p8BQSWI87I2VIspysvOYziwu2QFOoT82bBbxyMZ_4a1k6Ennygtj7djg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ceXN5qb4kzsTzCGp6AWo-0ZmrLaIsTZskfSq3EfyS3aOJANsUNra0Ex5qfbYayErK5BbipXBdR1jasA_7NAmYhHH-a6npVgBDFQ2OCTCJpmup0HhGhPO_BkFLld9Dj8YZbWHYwK2y0dZgtQBlaafBbMVXD2fcUP8WbArlQxLbCL931Pm0wGYaMzc4dDX0l-H8an8ynmwSfgsu3Jm1Buu8aKSclhDMVuAxg1UWVG582D4lpgRSQpeusKZ4iVp_fkt_Ia3wx2rQhENGB5kMNxGLodaIjyJEaMZIUzzV4RwoynXNR2KyLqZVvKT4xwDY6iCSMJvLIXYqMjlZ_vWBxPHtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ceXN5qb4kzsTzCGp6AWo-0ZmrLaIsTZskfSq3EfyS3aOJANsUNra0Ex5qfbYayErK5BbipXBdR1jasA_7NAmYhHH-a6npVgBDFQ2OCTCJpmup0HhGhPO_BkFLld9Dj8YZbWHYwK2y0dZgtQBlaafBbMVXD2fcUP8WbArlQxLbCL931Pm0wGYaMzc4dDX0l-H8an8ynmwSfgsu3Jm1Buu8aKSclhDMVuAxg1UWVG582D4lpgRSQpeusKZ4iVp_fkt_Ia3wx2rQhENGB5kMNxGLodaIjyJEaMZIUzzV4RwoynXNR2KyLqZVvKT4xwDY6iCSMJvLIXYqMjlZ_vWBxPHtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=IwXpH1qOe-xML7M0QKc_8LQQnTHjDmYlFJhwwUU5P16P3uLxXVpSx_QWK4Xjbt-TsqFUrL_MntQFXSS2giuYyAoMl9d8ZhkiccNKpLATVGW_fKGHzOa9YztynM3kKvEB-E_zAyXSpijKUgx_kAFXKZKJiqU9kRJfLZP_gVkX2oujirmPQlWgdrNRLtS5zy9OvAzHIPq5L_tCvRwdMNs7zgF2hmFx8UrfwqDQv3feZDIUR7S6jUJ4Ovi4DqqBL7ajH5HhRNuBORNTCO5_wvG5hZihQ-wwDBJMoJhPkFrjFvwUayjwoN8DkoaPEaDeImxEjMjbfLkiqBlNe-ESLIX9qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=IwXpH1qOe-xML7M0QKc_8LQQnTHjDmYlFJhwwUU5P16P3uLxXVpSx_QWK4Xjbt-TsqFUrL_MntQFXSS2giuYyAoMl9d8ZhkiccNKpLATVGW_fKGHzOa9YztynM3kKvEB-E_zAyXSpijKUgx_kAFXKZKJiqU9kRJfLZP_gVkX2oujirmPQlWgdrNRLtS5zy9OvAzHIPq5L_tCvRwdMNs7zgF2hmFx8UrfwqDQv3feZDIUR7S6jUJ4Ovi4DqqBL7ajH5HhRNuBORNTCO5_wvG5hZihQ-wwDBJMoJhPkFrjFvwUayjwoN8DkoaPEaDeImxEjMjbfLkiqBlNe-ESLIX9qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=FGuyMNAHe4EUfwrg39u9ZWr9Yh1aC7P6z5T43xVW7tm-YN__GEcbRtOvufWGEa_ch1qjvT0Kc_XSkF_yzn_iwrEnIy4T8-0iHcLg1_vD8OEqkcbplyf26yIIl95_RD8eDZWegOyBOsyeBlcjEH9r_rvGir4o60m9xRHgNJ3fsyrItvXTzGyDwTZwNUJ6NaGp7BYw3Fg-NX4Ai8ghFXmIGyxzp4HfFFL_wO3jPirxZkVPX7gAJJWUoV-4PTZ6IkOxW-LASbULVHjLigo1Qgr5uDYyHt0fYASv-g36A9LXG0EIc3pnvpG2r7fQmrJJ1UjmnKyRcHQ2knaRFwYdB8gCaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=FGuyMNAHe4EUfwrg39u9ZWr9Yh1aC7P6z5T43xVW7tm-YN__GEcbRtOvufWGEa_ch1qjvT0Kc_XSkF_yzn_iwrEnIy4T8-0iHcLg1_vD8OEqkcbplyf26yIIl95_RD8eDZWegOyBOsyeBlcjEH9r_rvGir4o60m9xRHgNJ3fsyrItvXTzGyDwTZwNUJ6NaGp7BYw3Fg-NX4Ai8ghFXmIGyxzp4HfFFL_wO3jPirxZkVPX7gAJJWUoV-4PTZ6IkOxW-LASbULVHjLigo1Qgr5uDYyHt0fYASv-g36A9LXG0EIc3pnvpG2r7fQmrJJ1UjmnKyRcHQ2knaRFwYdB8gCaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=C475hB0YBRubRUQbualOVdxpqrYuEblB30ZhzYpZdKC8_Vx1wzkexAkNIbQh-942GVglWujJNikcSulsU6l4yWeIcL3IcxwPxUUh8aHPK0h8fn7qYuvIpOyH0WFxNAlxv9wNFKbSB2TOR8H43QlVAOaVdI_RG6zrkstNyuje1WEEKT3QeUGlrMV1lkKM0Iy5_ptXQQ8hxeiDOrVaZbCCFBeUFMLOEaG1gIwEXsd3PNEkpwBO-h7K_-XlGdaL6T6AmRreTt5BO-T6pBlSjSpjDUf6yrKhR961P9gH668gRvy0HppbbNmA2eNoBg0HUmINcmWqf4dssXV_iwIdm8yE_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=C475hB0YBRubRUQbualOVdxpqrYuEblB30ZhzYpZdKC8_Vx1wzkexAkNIbQh-942GVglWujJNikcSulsU6l4yWeIcL3IcxwPxUUh8aHPK0h8fn7qYuvIpOyH0WFxNAlxv9wNFKbSB2TOR8H43QlVAOaVdI_RG6zrkstNyuje1WEEKT3QeUGlrMV1lkKM0Iy5_ptXQQ8hxeiDOrVaZbCCFBeUFMLOEaG1gIwEXsd3PNEkpwBO-h7K_-XlGdaL6T6AmRreTt5BO-T6pBlSjSpjDUf6yrKhR961P9gH668gRvy0HppbbNmA2eNoBg0HUmINcmWqf4dssXV_iwIdm8yE_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZb7qRjeFvaKGbJs_jvJqPZYVpxbF0TB36qj8ltud2gFSZQlF6msi9o0gpiErtix1Aw-b5KfhIBB6HM2v6NVhEeKXSyTzRSN0CWpP3uwxFCLV-UT42o52xraJEo0pZjT2qQ5wkJHIqZ31GI1frg15xOaD2BtYMHQ7a_mdn5jj0bwK3qf0uSmEH9K-wdjXAg_kMrhRsppwuJDVdX8oTdaFz3CmJ4I9FXYyWjOjpqOOlP9AGKo3FfP_Vr75tDuz4ZcULNcZwTOnFWPPUUpaSHpRoMzcTtF3CULVKlCuFV3baJNTKti5Kl1agVrB-y4XZjntpf_skv07VtzmRuiWJwcXg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=q3FEDzsXiLsMqNgS5jEepAT2C3NULxUWfabGsCzhzECKJbW7cxeYMSFcpVHSDuFP-r5AL3URUKSpqthA4GKoNmDMxQab6PYbtDVM6I2ReApmqcfK8awGmDSiq7hCOoN6EEI0qnxQVeNLdikjVXvbqA_KY7g10ktv5Xa8qRfcC5tWrkE5APWtPSATxjfE7DYJXNIqAOcW9yw0VWkr1Vx1ERr3HoZaNc2OUyt2E-4-4neftZWqumHbNPI6LAD90vJfnywF2inh2K0QS8JJGnRZh0sEVQs-GvVbRL3jsMscYZvK6DfTCBNqFzXANNo_Af9YAlmvP3qaKBDTdNogCGYzjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=q3FEDzsXiLsMqNgS5jEepAT2C3NULxUWfabGsCzhzECKJbW7cxeYMSFcpVHSDuFP-r5AL3URUKSpqthA4GKoNmDMxQab6PYbtDVM6I2ReApmqcfK8awGmDSiq7hCOoN6EEI0qnxQVeNLdikjVXvbqA_KY7g10ktv5Xa8qRfcC5tWrkE5APWtPSATxjfE7DYJXNIqAOcW9yw0VWkr1Vx1ERr3HoZaNc2OUyt2E-4-4neftZWqumHbNPI6LAD90vJfnywF2inh2K0QS8JJGnRZh0sEVQs-GvVbRL3jsMscYZvK6DfTCBNqFzXANNo_Af9YAlmvP3qaKBDTdNogCGYzjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=t_phdvW5ScZQKP6cvan6f-P-Ef7V9AEIEC2g5Yd-LAROLY2iyyh2_ynItTXIX_Hx0B9oKef4fw39scg5GR6iNOV3Q6UOGeYFtbbIB7FQ7HJabg7m0yA0K2SfL9i1D-ufoJgIhLNo04BUYbbrINdA6Ubsd7K0VNC3lI5HzO3AQ3799ZztoiQ6dQ_IpkpAUbdpAs6iMhguUq0BXv4CfuRRNQGj-IX9LYzsXFH-ajUlVjnLv_5hedPrAI1wsjiQwbkOF6QXGEufi9n-K6x-NU02ffDFOo7IgbZrZO1X45ILVWTabLPzDoERgY3awpE-r5oSkmkL8cLdLyazhCYLikToYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=t_phdvW5ScZQKP6cvan6f-P-Ef7V9AEIEC2g5Yd-LAROLY2iyyh2_ynItTXIX_Hx0B9oKef4fw39scg5GR6iNOV3Q6UOGeYFtbbIB7FQ7HJabg7m0yA0K2SfL9i1D-ufoJgIhLNo04BUYbbrINdA6Ubsd7K0VNC3lI5HzO3AQ3799ZztoiQ6dQ_IpkpAUbdpAs6iMhguUq0BXv4CfuRRNQGj-IX9LYzsXFH-ajUlVjnLv_5hedPrAI1wsjiQwbkOF6QXGEufi9n-K6x-NU02ffDFOo7IgbZrZO1X45ILVWTabLPzDoERgY3awpE-r5oSkmkL8cLdLyazhCYLikToYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=dDMPOniln1BdkI3k-pcUorJOzY3oPtOpW8QCw2BFkPJJCw0j4aA85Z0gM2f9uy-CzE0aIvR1yx9zWXQd009YdgakinB8qwLp9NZ-ar-pCwaOsejm-A1O_HLnI8wIEfGnd_EP-Oy33E3Mn6BJYoresvChxs_Ya_bVgFpIZ3xMBzOccAxY85SonrSa4lv_wzJ7X9Lmm4lpWK3pqivV9WQvMJ245BAaiovn2J0OvoLppCukG2zM8mL07L0PxiWjh15t2xe4GSi7jCnvE27HVJlLCY7CxvmquCQec7BO8-OxSsITnzcOxcBsTmUScJqhP-WNF0qWOKVN9zW3cezdoKoQug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=dDMPOniln1BdkI3k-pcUorJOzY3oPtOpW8QCw2BFkPJJCw0j4aA85Z0gM2f9uy-CzE0aIvR1yx9zWXQd009YdgakinB8qwLp9NZ-ar-pCwaOsejm-A1O_HLnI8wIEfGnd_EP-Oy33E3Mn6BJYoresvChxs_Ya_bVgFpIZ3xMBzOccAxY85SonrSa4lv_wzJ7X9Lmm4lpWK3pqivV9WQvMJ245BAaiovn2J0OvoLppCukG2zM8mL07L0PxiWjh15t2xe4GSi7jCnvE27HVJlLCY7CxvmquCQec7BO8-OxSsITnzcOxcBsTmUScJqhP-WNF0qWOKVN9zW3cezdoKoQug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=EhsC5TQb1tCyGVO1kRvKyK-sTwYj5Lc9SO4WMI7Fea4NUNq4DMVszyZuw2s2L98VqjRFrf2zOwHLwvqZ5dhGRvv9DCteh3Oo-lUiSQC7WH8JTSx1-H1rmYo-Y_IabtLEPIkc41ubJSHp2p2507siPhyn3BQ8j2g-iwygSOkD6-gZGkK1B9iIl3i9RhKdxvMqERXtBU4PuZ5zEucdtMm7jVWvnv-HjAiA1w9mrLq9a8GzJXGMCwSjzjUn_HuJHSetGmwQvu1UiEO4E1DuQkR65lJAsAC3xaTPWuIj2vokzxVwxlnrpb5GHKMaG-Gc_JPZSn3LI7UeGv6bZ0TVHAAv9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=EhsC5TQb1tCyGVO1kRvKyK-sTwYj5Lc9SO4WMI7Fea4NUNq4DMVszyZuw2s2L98VqjRFrf2zOwHLwvqZ5dhGRvv9DCteh3Oo-lUiSQC7WH8JTSx1-H1rmYo-Y_IabtLEPIkc41ubJSHp2p2507siPhyn3BQ8j2g-iwygSOkD6-gZGkK1B9iIl3i9RhKdxvMqERXtBU4PuZ5zEucdtMm7jVWvnv-HjAiA1w9mrLq9a8GzJXGMCwSjzjUn_HuJHSetGmwQvu1UiEO4E1DuQkR65lJAsAC3xaTPWuIj2vokzxVwxlnrpb5GHKMaG-Gc_JPZSn3LI7UeGv6bZ0TVHAAv9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syJUUQOO4aPj4br1hsiASm3kvTXwfG18EcvqUyAUtaHAWAhD9akSeURHi_VWBS-kGKGzcVkPM4yhblRmZbZDpV2O2fnw0PgCtSeaREkuAuAUNQg9S6wYDlbuKCh7dJuV7a2USwvEQgLtV3aNVEEZvnQwao-qp2qIq6tTe6L6Y54UWK563lXpA-n5yG0gShawNjjSI5nVyiIhO8izozUbpP9fjjcdHfYOFeAUGQnW5k8S_jYL2QF31i48Qx2Alvqv7nZ-mVrYzXcWASrBoUQfLXkFdGROIdjwIROjfJAXXSQ7BQnV6JkjevZPzR5rqQNgWAk8YaohZjzSHuQtrm_NyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Pg2BIDIo3Spnv4FyrMnWlft_ql3q_OrYs3A63iDM-63bnAmpi_weTEAqb1RM3maz49StdfTuwzl_D74TM7dsv07rmQbrjleInbQjXZeSyDtBRDEI-_CsYx3DxTyfybcQdt-OlWXEkG_7O44VgF-rGHAJDinkJuliOOSA5j84_diBimY9PDw7bu5H2XK9uB6jM4-2yYJaz8g8EWSEefBSB6o3nYQKLp2AbK1HoYiBadzPWnfShm2rGja7494IEo0oBYn5WUb8uyph-hD-mtCX0eQuWixDzGr1pPv4Hwy5n_minYYm-k_41s4sZVQPt4Bd59WgjasBnpI2bS4tA8IjfzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Pg2BIDIo3Spnv4FyrMnWlft_ql3q_OrYs3A63iDM-63bnAmpi_weTEAqb1RM3maz49StdfTuwzl_D74TM7dsv07rmQbrjleInbQjXZeSyDtBRDEI-_CsYx3DxTyfybcQdt-OlWXEkG_7O44VgF-rGHAJDinkJuliOOSA5j84_diBimY9PDw7bu5H2XK9uB6jM4-2yYJaz8g8EWSEefBSB6o3nYQKLp2AbK1HoYiBadzPWnfShm2rGja7494IEo0oBYn5WUb8uyph-hD-mtCX0eQuWixDzGr1pPv4Hwy5n_minYYm-k_41s4sZVQPt4Bd59WgjasBnpI2bS4tA8IjfzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=iD4fONJRD5V1SWo0kFaJ9nXWP12D7FBhViye4nKr29-OQAAO2QHCGEek3m_CE2EYKJzgUpmftciPul-E-sH6ZvVhgtGEc9vaHHYtSM2LdWsk_6GMg4bz2CP-LDaNPLFkzuqv1M2g7c3afzMsrHjjm7PfXXhFTuxunvSu8bePfNeyRyw8Ja5Xx9Zh7A1-tkbFyqeHTTHSqiK0iD6yvslUir7DxtxshPULKo0OrdfljRd6ohR1CaJ3G5nwmm4wkhE3thSRkMHlCh_F-AyOrMBSDn360krUs7Jb8O5KF0OKfAZnW9nNGxsB00O9JWO5B1l5_PPPZvfJzffjeDzV7cFRSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=iD4fONJRD5V1SWo0kFaJ9nXWP12D7FBhViye4nKr29-OQAAO2QHCGEek3m_CE2EYKJzgUpmftciPul-E-sH6ZvVhgtGEc9vaHHYtSM2LdWsk_6GMg4bz2CP-LDaNPLFkzuqv1M2g7c3afzMsrHjjm7PfXXhFTuxunvSu8bePfNeyRyw8Ja5Xx9Zh7A1-tkbFyqeHTTHSqiK0iD6yvslUir7DxtxshPULKo0OrdfljRd6ohR1CaJ3G5nwmm4wkhE3thSRkMHlCh_F-AyOrMBSDn360krUs7Jb8O5KF0OKfAZnW9nNGxsB00O9JWO5B1l5_PPPZvfJzffjeDzV7cFRSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DApIBqR3ozLXzpd-u64_MNucb1kfMdeIVnnCzbxtM8iBU-4Gc4sZrv-IhJHCUESSDbkQDiT2X9GQEKIB6_bsTW-kezvrc-UG0yfNikpNw3ayfnxOAQ4wJywB-P35T_Lk8ZA2GUBwc2Kx6uP6rN02LIuA3riTPBasXiW4O3BvAMatEJhMBFKo5efeNjNGPzhcU5n6_cezYaVqvgXdYXzIHLj5AFYTMXTBFmi46Sos50umCcwKfcOF4aMem7x0Lq9J0NNjOFIbdC5LmSogIIMSGonoH_d4Tyyh-SeJrAqBiXPRptNuIjk7B17ErMZsKTaXTw-aIhGdmbbRMah62wEbCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PN3L4P-Ux6g14UM4ckFfNUFrxVmTDfpHnYtz86BaTSjbtaREf1TkNPEvoclTZbmhOx_8FkeXsiHklrTmc8bC18gExNfegBhSqr7cHnPE2utv2OPLnxEMRFaWGlOHG6MZOxUG4qkKYNi5WoKWQYugLwFY6PkQBsxKJY4V2Jf5RsJ3t4MlskB5ijFjgqY3vgosWQKD_jwI3q4nWT4cOCPWeWGADzvKT9CGJSuF0u4R4dAh0r9RqIOBZI-p8hLZKH1PueCHRXjjVCZxLXM-NFt8FOimVSt4WGpVvYiK-Vj91G28FZ_L9ohN2-Obry2TmNdPCAMxdti1l7dpQMxBio4ybw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=VaJsj8zxOOedHPaubOXrXqkOM-9IvHaLv_V0nUrHTs2Wy2n1-NVdrMEoL74xubjdKAFpe-wG6Ss5NsYE2SJfl8slTWS__IEeV0DBTjIWNv8Y73v0dqTElA95QLl-KqDpqyydBEkOb5Y4qv1xe629_wd7AngZt1oogYIi-Nr9G2EPzcqEjCTLOgVlNZTlqciYaHpFYaGYIaBI25qsiBHfFfnbIY49Sa9KhE8oM3SM7wDQp_QMD1I1HdW-1jtK-Am8tGsm2Dwhoi5sLQdWqDqVNtttd0zYJsqnqBdxqAnpz0BnUEWn6dIEBvuLukw737BUVeIS82RxAIhmfGB-dVEMWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=VaJsj8zxOOedHPaubOXrXqkOM-9IvHaLv_V0nUrHTs2Wy2n1-NVdrMEoL74xubjdKAFpe-wG6Ss5NsYE2SJfl8slTWS__IEeV0DBTjIWNv8Y73v0dqTElA95QLl-KqDpqyydBEkOb5Y4qv1xe629_wd7AngZt1oogYIi-Nr9G2EPzcqEjCTLOgVlNZTlqciYaHpFYaGYIaBI25qsiBHfFfnbIY49Sa9KhE8oM3SM7wDQp_QMD1I1HdW-1jtK-Am8tGsm2Dwhoi5sLQdWqDqVNtttd0zYJsqnqBdxqAnpz0BnUEWn6dIEBvuLukw737BUVeIS82RxAIhmfGB-dVEMWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DX-mx9LJ0qDxG0qQLEK1MVCuxxWYW8zxw3y_i7qHeZU2NBugxYl3O_Y1f3c90dfWoHz2kw4dqUvVcM4OPUkcsz4YA58_MPBB8SbwTKeGxtXXhX5ehMI-as5miGTyETWiq8Hvq_QGg_G310zKQBsc2BpGBQTitJLnbZrYzjTC5h0tUCsQEn8M_LtRq4SbkfTPYEIL7BFG3addLekUC9dRbxKpgNmaBqjlm6zmHve6p4oIK4xoIcES4-Cb31IfVHndK1Om4dZFqe4q2HcTIgjky1xvJVoevu6MUeD8hZiH5xovTLdwOzlB1IGa96Tmi4FSlONqHn6HU_9a_28Zu5-AgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L31iFprIsWCD5SMcrmtzSRTivcNvOxAi3OF3zAsiKXwtyDehrCr4573IPUUVpsuOQwaaWSeH1k72-Tzr7AmtZ-orPKcBbT2CYFUl2QUFrcTkr0jWP78g9Iya3WnGs-WNuz-Y9036l5YjX_4QchL6ssfEfPxGYTkOvPhv7YqBZbbJP2zOGsIPnWzWCCoXn3U6v89nHSLzxX9Ns_plb8eqTPJOZQSbxzp44BHiD80zcg6Wl043am6q_3gF44ABLeSymURHvroWQInMMeDLzqB4xLaNhwFPLuaRtzMtb6uks2c12o9_OnI3U3a-zNwKlxEiQxnLHT2S2ockKl6sbXrMbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8e_5yRjH89zp7gV_C7XLXHigeVs44xrTllP4GuOPtGehiilB4v9S8wKuk9hNIihXIDH8Aq2u4wR5db7LXQ8DCXPdvBOYG81p1EEYnZnOz1cQnB1I8swERqlfaXMYQFnTT8xKzDCZH0cl2rbhdYKz1rmwT3XxWUqkn-_Gf-gEYgsHx7Ljy-Eu8uSnbCNOgNpaDR8Ervu5Hhcme7KxTgjrrzgjt1C3xDVhVfvArdx91y-fHaAIv6iMzkxLJspq19vbnuy0hkDgXY9KYPMaaIHGVBl_CpshNbj0xlP-OI-Z8Z0YqAy-UUf7RiuaB-mwigGolGi44gyfZS0U54Ry0c1RQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=qaHvkQIa1HWM6heW8cb0S4_m9hBEFFFey5jNzzXgymKgtwA248qEU4huOixxVFiwBoBtkX87p1885yFl06uyXy0af7LCreVMY2VHKoaHeC1eHHXDbkIEzB2oyQbhH7hKvnnJ7k1Jtke51Bfa_nKx6rEU6jiSskNlEpG2ARjVlLqjbhEj3THn3P7EEHJUFWlZ1K-LBBx49aT-hF1o7vVLleFPO1dsoiVTfeOqsev9dx631OQfM8WkA1tDyYY6LrDj1yRLX_3w1QI90ezcoMgJEfv-bpXIugwAfJ1os-ffzFpgNu_mwTwwTZn7YAMqFP0GOEFI1rJ1gDqu7ZtAEqbaxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=qaHvkQIa1HWM6heW8cb0S4_m9hBEFFFey5jNzzXgymKgtwA248qEU4huOixxVFiwBoBtkX87p1885yFl06uyXy0af7LCreVMY2VHKoaHeC1eHHXDbkIEzB2oyQbhH7hKvnnJ7k1Jtke51Bfa_nKx6rEU6jiSskNlEpG2ARjVlLqjbhEj3THn3P7EEHJUFWlZ1K-LBBx49aT-hF1o7vVLleFPO1dsoiVTfeOqsev9dx631OQfM8WkA1tDyYY6LrDj1yRLX_3w1QI90ezcoMgJEfv-bpXIugwAfJ1os-ffzFpgNu_mwTwwTZn7YAMqFP0GOEFI1rJ1gDqu7ZtAEqbaxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=lWzyQJYNkRnoHRJIjlrX7d4LZlkKc6_Q3DrvOjwg5yYmgt7BCmXpQXFnwtOYW4e-BArkRNikE7FO8nRLeFdDtKfJVj-HbF1_QQIzbpwxPKbj5ept0qMkmgV-Iw9QzP6juPGJt0EHOgppAoH2bUXoyp8Z_9K6OaN-MFuFnIEl6ZmwJ4-9vkUxE8hEZQxPl4KLiO8vs9pbjj2RTUCC2A46B96gJt9q0ccasSHI3gr_NqnWrVes-U--sRqmBgkxlaN2EpKu-i4vw24wR0Rp5QJ6eRWm_ofLMLk1JUv47DnQO1xBHv0IoIJUuhGw0coI4E5XAcEJWC053FvnWtjYZ5QhvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=lWzyQJYNkRnoHRJIjlrX7d4LZlkKc6_Q3DrvOjwg5yYmgt7BCmXpQXFnwtOYW4e-BArkRNikE7FO8nRLeFdDtKfJVj-HbF1_QQIzbpwxPKbj5ept0qMkmgV-Iw9QzP6juPGJt0EHOgppAoH2bUXoyp8Z_9K6OaN-MFuFnIEl6ZmwJ4-9vkUxE8hEZQxPl4KLiO8vs9pbjj2RTUCC2A46B96gJt9q0ccasSHI3gr_NqnWrVes-U--sRqmBgkxlaN2EpKu-i4vw24wR0Rp5QJ6eRWm_ofLMLk1JUv47DnQO1xBHv0IoIJUuhGw0coI4E5XAcEJWC053FvnWtjYZ5QhvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=hk-wROBlQXeLBRXhEn3_r_m0MzItp0lGZwVEymtLZS7AB2zjY4cwwdTis4eUeUIzehqmu02qKJfbnRYJ8qharfjgk8kTwO06FuRrlP_MuC9dR1_tw0UK1AKRQ2FBY9GBX1gFKhOAfn9xargwJ9P8sHmiFsdXGtpnsj9AT0m4lA10K6UPX2uolMSh1uA7f6UQYXrYPtlKavVjFnbtEamiWB7NrohRQ7RNBHyzrABOnnsOP0VeSD0Rss1ePXH2147whiUCb8E6vpj2HUYTHgf8bNk0IRf7farjulZdi3R5zZOSXDWmHSN_21V6H3_qaxzC1zifGHyq_Eb21xucDUS5v0hxWgpSJ_6ybeNS4lvgGp3IJZm6zn5n_PnsWA2jZrFJOMl_drDOPlnVemwIcVRU0El_xbbBn_Zc3si4Kiq3mmzC_NYjy9b4B8pOb5yCHuTZV8gnQZxlKJoGDyri78cIsFZh7-ZfBRNu79OKONkXQf_tIgfDQTOuFzawuFkC4oc3odM0JS7bVPsNZKVaLgO_juNzsoHLo3Vk7HJFgkQ01CsRTctgmrwTE2ATOiUZ27Tg91cxUG-rbErBP3pG_dnCRVAt0lu23bzjkGz4sV6Z1KSHKlkqQk7051PdF4fE552WbLxZnf2TioNZnwNIPYYC_71SZwiaTp6kJWVrUMToIuo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=hk-wROBlQXeLBRXhEn3_r_m0MzItp0lGZwVEymtLZS7AB2zjY4cwwdTis4eUeUIzehqmu02qKJfbnRYJ8qharfjgk8kTwO06FuRrlP_MuC9dR1_tw0UK1AKRQ2FBY9GBX1gFKhOAfn9xargwJ9P8sHmiFsdXGtpnsj9AT0m4lA10K6UPX2uolMSh1uA7f6UQYXrYPtlKavVjFnbtEamiWB7NrohRQ7RNBHyzrABOnnsOP0VeSD0Rss1ePXH2147whiUCb8E6vpj2HUYTHgf8bNk0IRf7farjulZdi3R5zZOSXDWmHSN_21V6H3_qaxzC1zifGHyq_Eb21xucDUS5v0hxWgpSJ_6ybeNS4lvgGp3IJZm6zn5n_PnsWA2jZrFJOMl_drDOPlnVemwIcVRU0El_xbbBn_Zc3si4Kiq3mmzC_NYjy9b4B8pOb5yCHuTZV8gnQZxlKJoGDyri78cIsFZh7-ZfBRNu79OKONkXQf_tIgfDQTOuFzawuFkC4oc3odM0JS7bVPsNZKVaLgO_juNzsoHLo3Vk7HJFgkQ01CsRTctgmrwTE2ATOiUZ27Tg91cxUG-rbErBP3pG_dnCRVAt0lu23bzjkGz4sV6Z1KSHKlkqQk7051PdF4fE552WbLxZnf2TioNZnwNIPYYC_71SZwiaTp6kJWVrUMToIuo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=Nk9t9IyWOB4dJIcNZ749CZ5HKipWnkkuMJrRf0P_j4DoGQPdqXjqLWSyUzOj9XKC6yzPdHkJstDCTS9PfGaNHR5Bb9pLKbTpcXaCt-F-Y5LPm8ZhaiX5lb52krlyEF-efI1_W8gZN9Mf0N0lnI2ib-Ygy4PLf0HqDO9IriEXfserb04zoJziO-PRysyr68Z94Ikx-d6fNQjWylGfeT_PSu99hmcSm1XXAZMDUw1fcGj1hOL6ToTH3u6rzn5wYsGNWDHVJhxHMhkF3IlCFUA18DJ-1hr7ISQ0z3UNyhgqL5LOR9NjkMhg2v3-oBccF6Ze46U7XwePtZ1zTs7VAPyvyYN6RYpurTWxs5n8DHJ9kmTUf44LWN9y41Oe5oFDRbgH35TeYiOO5pxkz5Jp14mPkNi2H2Y3Z6o8s0HYFHRoYU6bLl4A4VKgUGHvyveESYA5SLXbKg9gbWhp4Bu7ugKYrTMKxXmI9Ic1lAkhL8Kn6mPq0mKeWr1lH9NLHulsgX5QhELZY2AnHHQ5JzZR0efPxIysFnV5qLl19GwpxXwyyiAZ-Cm8t5ZqObWTHNosCmIR1suQP8Gvrwf-c4N2I92-xDwRgzGuxlGmC3qjqbpKG7fsLOw3w8tTM96jIeSG8EhLdQLyJqxIWN9TucSA0rZg_GhY8iE-1clFqZfzMON4Zhc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=Nk9t9IyWOB4dJIcNZ749CZ5HKipWnkkuMJrRf0P_j4DoGQPdqXjqLWSyUzOj9XKC6yzPdHkJstDCTS9PfGaNHR5Bb9pLKbTpcXaCt-F-Y5LPm8ZhaiX5lb52krlyEF-efI1_W8gZN9Mf0N0lnI2ib-Ygy4PLf0HqDO9IriEXfserb04zoJziO-PRysyr68Z94Ikx-d6fNQjWylGfeT_PSu99hmcSm1XXAZMDUw1fcGj1hOL6ToTH3u6rzn5wYsGNWDHVJhxHMhkF3IlCFUA18DJ-1hr7ISQ0z3UNyhgqL5LOR9NjkMhg2v3-oBccF6Ze46U7XwePtZ1zTs7VAPyvyYN6RYpurTWxs5n8DHJ9kmTUf44LWN9y41Oe5oFDRbgH35TeYiOO5pxkz5Jp14mPkNi2H2Y3Z6o8s0HYFHRoYU6bLl4A4VKgUGHvyveESYA5SLXbKg9gbWhp4Bu7ugKYrTMKxXmI9Ic1lAkhL8Kn6mPq0mKeWr1lH9NLHulsgX5QhELZY2AnHHQ5JzZR0efPxIysFnV5qLl19GwpxXwyyiAZ-Cm8t5ZqObWTHNosCmIR1suQP8Gvrwf-c4N2I92-xDwRgzGuxlGmC3qjqbpKG7fsLOw3w8tTM96jIeSG8EhLdQLyJqxIWN9TucSA0rZg_GhY8iE-1clFqZfzMON4Zhc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=az-meyQ9STaaBw8MOujXBTp4pvuhV6qWdcNvx2E1XUdeSqmXuG07K7nLCIsKIkbv8V4uT-i2UU0stODZlCEFDZtdwK6PPfuqOpBrRnwEgjo_58lLSdL0kHDnp8zpb9r4Dqtze7rLTa10b0AsEmyS_8YPI3V6JrJvJS1aoDfwv-AYRNDfU3GvohR_mjLylbsXkdts0tpXICjR-t-i7HHW199lHME8bbFwfVLMCjdmoryBRyBfwdY8yF1Mb3cVgul4yzKEaZHrLd4XEBsR3y6KKVyGHHAGfaJxyZP0D90NvjYBLqvWSQdllUZxxxDLbTFdqRO5hSmnaysLukCKOMzGEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=az-meyQ9STaaBw8MOujXBTp4pvuhV6qWdcNvx2E1XUdeSqmXuG07K7nLCIsKIkbv8V4uT-i2UU0stODZlCEFDZtdwK6PPfuqOpBrRnwEgjo_58lLSdL0kHDnp8zpb9r4Dqtze7rLTa10b0AsEmyS_8YPI3V6JrJvJS1aoDfwv-AYRNDfU3GvohR_mjLylbsXkdts0tpXICjR-t-i7HHW199lHME8bbFwfVLMCjdmoryBRyBfwdY8yF1Mb3cVgul4yzKEaZHrLd4XEBsR3y6KKVyGHHAGfaJxyZP0D90NvjYBLqvWSQdllUZxxxDLbTFdqRO5hSmnaysLukCKOMzGEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIJKOxsBVmzyvP_uSpmBBM4wL3qqVFBSLGp-qM2aen6kdUW7elY3Gdtt49bNVzYCfWHVkNqMqdhIHHjlBV7vTeriSxepeUEW2sR4Z625dW0MvjvxmclQHSeCKFrM5RkD5sUOzSxnPKh8VnR3wDdZ12M2bUaqITKwiufy36mdE7UMQH_3MSvsi0mtgXgv299I9EDMwz5FL5NmrKmnuu1oZ85-urZSQwe8BkUiHgJBTe6WxKUxZJGekEH_oL2NZuC5oo0HNPCPLVNC6FLEeqndeiQ0_wwDHlcZa-xg6dzK5J5AsYmm6JT3HqzzsQIWCvPiyZGKInK5yLQ5b9ktDDAw6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=UJxoMbIeDrspbHtfRd0VA9PWC-H0YTyG-WwneVmgrvc6mpwu9yt9imWkUPw_JFN30HS5UZV9KzU2VDpDIIhjTsqLOrzu4GaHOdkgqTJRt1XiSAfBiGMXic2SFKWBA1ABJ85ksTRWeGZXV5jKpNTm_NJip5AsoLJLlfDAuCFoFb_qXzd78VpKFCm20rPZ8-qlnae3BMMXLoWjP69wlC9Br_KQ_dIiLjaIAofiPO3BRHDJw9KRxyiAw8Ehjb910IutmvVT6dzoYyY6QRDG5f4BKPC4DRteWyAZYyehlAJd9fBRPqFN3m1ij22m7a-dGIiVYn9dblMNdWO206yfYSCQUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=UJxoMbIeDrspbHtfRd0VA9PWC-H0YTyG-WwneVmgrvc6mpwu9yt9imWkUPw_JFN30HS5UZV9KzU2VDpDIIhjTsqLOrzu4GaHOdkgqTJRt1XiSAfBiGMXic2SFKWBA1ABJ85ksTRWeGZXV5jKpNTm_NJip5AsoLJLlfDAuCFoFb_qXzd78VpKFCm20rPZ8-qlnae3BMMXLoWjP69wlC9Br_KQ_dIiLjaIAofiPO3BRHDJw9KRxyiAw8Ehjb910IutmvVT6dzoYyY6QRDG5f4BKPC4DRteWyAZYyehlAJd9fBRPqFN3m1ij22m7a-dGIiVYn9dblMNdWO206yfYSCQUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=oaquaUZBXUO8WQGeo8cxlyNrNDBHzUXGHHkzKpOdOzhP0gGHoOTBa9IlJtig8k0yGdgqFxv2C9tpwwwsutjMxjXRbDBeMB_FUveQo9V4Tpki_V_i-ByEqNJab_pr7zgbXPbJrGpQJgdk9AG4fuaq9_9qB83t_jp7yEIOfJ0aLkj5HFMd-MhSJhTY9Ma1tLZ2MsGSADGIL3nzWl4dN78EFFk_K4nEs9_Mf_eB_ewAO8Xu3xt6RPH4wcDoMgtga2cH4QSshwSgCAzYQHiSxIblAyxTQv0b7okfkYC0-2AOi-NjGGPLqLqvdN0tqSLs58BPJ59YzT43AE9D89jna9-Gjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=oaquaUZBXUO8WQGeo8cxlyNrNDBHzUXGHHkzKpOdOzhP0gGHoOTBa9IlJtig8k0yGdgqFxv2C9tpwwwsutjMxjXRbDBeMB_FUveQo9V4Tpki_V_i-ByEqNJab_pr7zgbXPbJrGpQJgdk9AG4fuaq9_9qB83t_jp7yEIOfJ0aLkj5HFMd-MhSJhTY9Ma1tLZ2MsGSADGIL3nzWl4dN78EFFk_K4nEs9_Mf_eB_ewAO8Xu3xt6RPH4wcDoMgtga2cH4QSshwSgCAzYQHiSxIblAyxTQv0b7okfkYC0-2AOi-NjGGPLqLqvdN0tqSLs58BPJ59YzT43AE9D89jna9-Gjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDckXgshcn_TJ8BdLEZRXiFtih_-ISqZAF0IDPaW6TMCcB7-RXbprO4ntiGgEqmpsuIoUoY1SvqXPlwfcxdYL21sP1Cx1XiJmJ-NdA6XNr_PpxGRkzQ5lVNVlWc_Yxzf50MikyVZ-m1ztXbAUHbRcga-LQkBgpBGNcdaoZpuhS1ypfrAM8JelQ4Mvpbt4SKDyRWM-DAF_3OCUtBS_AYDmVCRlHdZN3HbOZepEWEu1t6kIeK3fsbRtcsWAa3aGX6Wfva4bei8TT2iqJ1k8oz4TjMOPxqJisJ6tLCyzsQzuugN0WMBThxKuZJMcrAstgeB8USa6oZPYTF41MMs3FZrXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTFi3sM0651I6s51nLzWaY83a28TwYy7LZUxW3MI6XNZLZt3sP_4OMc-BJJwGJ5FiJ5-NpYt-P-lf0AF0x9FyYJXf8lsGUBkxpIalkwHLFfjslrInwWrSIOMFh6pvzZIl8OowZ3LlgNy3wiMotkTwSMa7B2Pv6ZnBixcfuOxmxQuTTtzSIxlg7K8C6lISXIrDtIv7ZHuMnEi9qaFWFr7XgyeV-_a7xakaAO-DEW3NJ-lC2PxmCrhWSpOqic24cOiID3_Iukyzsh3mO6LcUiDVvNen8SH9gwyCdifr0bvGtX2QimJazzogz8xISIGvSCnHqmX-1pKEkIFfhHKMiv-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDx9GqcSttORoutmhYFxpn6Kp3lme85qn35pu8aP65XwoWVZ9lfo1bMQsBsxcBb7ozYPqz9yQ4hzg7caH6qbcrn9bTvGdVRzZgo8Owyd-IrcdT9LrhX9zatK8LR2GwHZkasQsTQ4SWimyqr25uVseQjZ5As4WNEeFv8msZpVzHqQgreK1C_4dU3pZJlTl3T6MY-S1xIwAg9O7U2YkO6vsZ2ixffWlPjlrjjUIMxkUB4QXe-ImM-ngjpQZ0CIQ5qCzN_WVERtFfX-O8Jug4EX7s1uUSa3iVfuKII3kKIp9v31fcljxAvipcfxisCc_VejgNSUEy_RA1HL7_1kav_jXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0hcamDaM_5QvcjckJVARHp7epEVvJtEx0n1gkBYVS122qrdWbJqc-K_4yEW7hSe1zZCezS6QirZRE40y6hmCiJz6veDdlo_jfJBJRmKtn1ipeKXDdrZ_Y08MyuOBJu909KVPi4UELLjsRQ043KP8mjzIKVrWpq9q6iGMY_0jLIJvbYEgA_JpKG9zw7bew13WdYqFrxyTsEU_E6ANDaRVJWy0Ybo2tVVkTU7ZLneQnhg1lR-chUfsxxj-u-PziVn_Q_8BMkPru1lHxlwi7iBDJpfz6kAQWllqtmliVI_rP22yRAdQvTrbxmFBG04HBB6Mf8_bnr5wmTO3xw5ofhZOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TX3ciwg4oxyrZC-gzx7lQoSNTkYH4xXlemNVhyBJTVr-qTtdqbu8dkmnxhJQgYM-7FetfVmnP3Qak1JHw8y5yrnLgR9k1qcqdxGCwQ0EkKBOhieZsTvOmzKpaiwI3eZ5IfflThgPzrDmzcsK2WTnfWqkK3Fl7nYENFfDrfsc0ETCaOjk8LZQ7TejUl4bcDbI2hzqT5dfTAxcS0OxjRF5QHvJ7wzmQ_vyI2hVimCfWnP4_z65ylzQhY_PR9BEC8Q5jy0cec4P9ZohIydYLYqNXePXdx0By_cKLqm9nMVnZkEjYXxHshgC7WzxrNulQaEZUr9wxi0Qnl9jC6z4qOXzGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpZdb9gWvlkIci8HZSt-WdJArQx5jRNx8AmCBEXyyWTY38jNZIqClcECosabhsPyNGs1zAXPqgFtH0oL1DdL20r8Tv8krU7Ne9rxXe3aFL6J1VSzVoMLrN29KVxXsAdGV96oHoJPUIaCqSiXB7otZ9YoqOSh_eVpglsEsyaDXsiS7dyAj-pVWZMtxXRcOK3WuFh5tLz2a4I6-9U469g0XDPNN1nWA2n-mC8XhpaK1wC3jq7BD2BwLSRKLJU2M3AvnI9d_bvkHBmDE326vudAwEBoMr34W5S64ly98ueE_BnTgBw7jj-jkQBHeJm2TiggO6JoAX5vSksh4j3qbO7eMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYlzpENeZYSn3IRQ6yz5OGRajULv7dVmu0HawMCk89GbpNGCiHzn3hNWK7wpePA7r-nfbWWeJIFhVW4f6K_Q3aazP_kE6PRYTwvoMfj6A-WTDiX2ygkNl1ARnkC0x1ws20ap_2zw4ZBwIh0Uo8VQYiwZfKoX6p0b_HVKvPsS88ku2V5QYRxDa7MrHVk0HiTctgIbTdlK6lGExa7sarfG_LgZiS01rc1PCkYEckckjkraQ0P3p26zrZdXKD5eUQUQiX6OvALBgjMG3fz_rYQQ2iZsaUyLa_U8hgcgIG99R6iuJ9NsoryKJ47uiKfbRjpk52GfwXxQBmyst_sL6RRUYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMiDfF-SN16arpHKPwCR-HmM1HHsOSGdUm-Jz8GzWp0T6bY_5_saljfd3jBaSC1H6fRwxh3lPhqywfmXu8CG5byDwdOv4lWRRZyD4VasMQ7TkvvNebpeyCOcQVvz6g0yY1tdCZkKOeehffJCi0_GjPIZdCs3T1rKAoWeQDyIHHM7mAt8TB_l74opz4xKR_frsK6rkusbRGza9rtCpm0-ai1v9gYzAilHj_yfxbaXd35nLSVUHZExkmTcCnt7tZuW4jk2oDjglqhib-UPGLPP53LuRGJUN9AZPqt5yvtqIP0ntHA8smJWEDlP5ldLQ5l1TBSX0hB1k51TCebzkE7jhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r3Is-nHAGHCcI-1BByrm3kX3eXCdD9TQ-FeMthKtBI1gkYzj2qLC7q2A6zlZ_ZOjbRLPbmyWBaCqejAgcys075gctA7sxIiMdIx1_qzKPy1y3V5LkJlqTji270t5ja3Qs3fphj8w_jVRNZnMiv49erpQzOukXekl3a-KFDBFXgohR2QS0ChnOKTWBXknBBDYIGUKuczQaAMsMv_XBSgU9KrX5JIZy9NKDKnQxp3dWveTfOLyHaPzr0-rwzINxWwzBQ8VHr7ftL7x462AvSbKja2kJ0XnrJwpEhsHwfViqBa0vWzz_tixOZEkepx5ldLQA0_0_q6ZPWNIPloRgLQCzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hBEaeW_4d2hqLsFS0ZIQeiHI3RMDLSGNXxXgxCcQkVCZ1rkT-kPHVo-WI7T6YpU6EuR0awX283kRaTDCs-aMBQ1w6fyx1mKkACFjSNkxCjvvnVd8HJNwn_pnx-Hwf8KoFosHZ67CoHSxkD1iXPtXujg9XovX2ZYe7muzoCFKIinpIN6N__vzdb9wOC7HAPe-2NqJQ7IAvwFQgEY2U0AihHp0KY4qtgr3we-Ku4awgoKI5FU1xkxQZEyKarxvFq7t_v8XGt6JKRXmV1VfyHPmvFTcAtun6a5qRg-RSUcUw-dr-KygUpZY78TerK6uLO6fiwwqw9Lwk1VFS_YcKU6dIQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=YuoC6cb8uA8ez6TltgBMmvZ6gEsFO5bWCgF07ciEFm6xHbo3bedS53OrSKLZmBXoQlgcdloAq5TMQy4c2f-cpk7iJQyFDlpkDJ52fm051MZ417CbhcRykhGFztW_kDwmg_VQ8vxVfwdJK_J5psRngzLxJSPkiDGSn8BIfgp5LFs3uO1JlJRZyLmyfJTHZQdY3USoS7Fh6hFgtMvV7pQ4P_VbgUJXJ2BlTNUphN9lsjAI7JvfIRx1WbNogbc4kHh2dbo0k0V7xu6IHc3K4Pi1CFT2LV6Sw46lcA-ykKFax5cen77_eVSqqR6IW1Lw-81cx7FYgeO_TIR-Npfu46aUDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=YuoC6cb8uA8ez6TltgBMmvZ6gEsFO5bWCgF07ciEFm6xHbo3bedS53OrSKLZmBXoQlgcdloAq5TMQy4c2f-cpk7iJQyFDlpkDJ52fm051MZ417CbhcRykhGFztW_kDwmg_VQ8vxVfwdJK_J5psRngzLxJSPkiDGSn8BIfgp5LFs3uO1JlJRZyLmyfJTHZQdY3USoS7Fh6hFgtMvV7pQ4P_VbgUJXJ2BlTNUphN9lsjAI7JvfIRx1WbNogbc4kHh2dbo0k0V7xu6IHc3K4Pi1CFT2LV6Sw46lcA-ykKFax5cen77_eVSqqR6IW1Lw-81cx7FYgeO_TIR-Npfu46aUDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGF2VjNnuIwRjtqa7rzT3EAlS5peWCTNFCXBezNxCgUTY-FzPC80g6DxJjLEMZvSoWUU3Ok3AsW6r4ashVsK1_zHvKHB96aQcYdpWQRqxjFXVeblmChQ6pF8NRks0kqze8K0PpcEw-raVxJXNu470IF-3qlj9S593IyiiP-ymo3XQprdeGcJk6rA-PHvXbAbkZJ2MWPtx8BqKiXimuLLRaI4tYINyrMTD1vs4ClL3wTfFA_KU7bffEv8CyUZnaL0ou8Mb9FkeKTKqXXwIANS-Obe5PGgoiBfRtm0JDk-GkOxlYYPwbv89FG1tECiR2B3Wb0kHGiPMEkpbeH_I_FwYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukXTKniSRNDT9kYKQI9BNp31uCq2pzlj-WJHFB0A0-KK4aMxS3zJqZEnW6nLKEmj2bFOZq18rtJGWLEiBGOwtUofwnht12nFHio-Pf7Rrt1luprNTbymGoMdwymsh5tanmuUNmPEakYPFRqDniQML5ExhYD3D367ZoXLtqDVnpQ_NCWP0xBbLRN-9J0__2MF7LadjrwJO_lrnkBG8AIJQZR9TlXOKs2RAbVBkajxvC8qH3Lb57CDQHDyqpPJ6wFeOYa7fpw-DsxQubToLN-j5-JkN_xJJ74UwHbKnlvC-tj3rSGmrQP_DwnevxB-tegZ88wjGXTxBs1ibRLdXjmDtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=YH2FfMaWR-6eATfG28oD70gCpf9AHwT9TeQb228J7ua91qGI6-S9fftwcJSNOdY4_MQEXcPV9T5FZCkXdI5XSf41OnFCEf5cEl-KRV2wp_1IwSyJ3y3I4n5SMfm4jYLuNZMBvXj4O9C5xwyrmXT5sg15MtOfb9hk5NCfhvH8jz0zic_uy38lOBpjg0BOWIU7_AOhMjq0cWcWjZErbu4wacQg32TX6DaKzfH3Lc3ohGRwu7FBPkdmaOmHJwWMzMmq4erx6iz2dGf4zRFCrXNSz358tjJJxEmjlV8DP1fV0jEo04YoMHT2MJvf4Sq1-t7gVnDHYtwaOMJ_RMpSyxKPzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=YH2FfMaWR-6eATfG28oD70gCpf9AHwT9TeQb228J7ua91qGI6-S9fftwcJSNOdY4_MQEXcPV9T5FZCkXdI5XSf41OnFCEf5cEl-KRV2wp_1IwSyJ3y3I4n5SMfm4jYLuNZMBvXj4O9C5xwyrmXT5sg15MtOfb9hk5NCfhvH8jz0zic_uy38lOBpjg0BOWIU7_AOhMjq0cWcWjZErbu4wacQg32TX6DaKzfH3Lc3ohGRwu7FBPkdmaOmHJwWMzMmq4erx6iz2dGf4zRFCrXNSz358tjJJxEmjlV8DP1fV0jEo04YoMHT2MJvf4Sq1-t7gVnDHYtwaOMJ_RMpSyxKPzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=g6x_1VBlC7oAOxjq-wtVOgsNgzI0QM8ZnQG3w3GOAo57KD9BC3OLKioY7qcIRP0PmlOnkdPdNobVT8wOTq4Rz04ULzyht3R1qpvtDc1TKweMvds9bsPMPDHdsJXfROxqEw66GUmssWgeyaSMTXjWf9HyeZXtnGBAVFGbwI7d9HQfkG057jkUSUyAXkYaK_4RYRUdHpHG1bSKCjywk_gWUucedrMjcOjkv-rbG-QcGc5GALo9MFxd5lD2MlJX6OnC5hJkJm9WACfFsqnJsFZJVLwjaj0HiDyWYqZ9kIls794F5d3JEnAn2Hccqv7osaH7AcJx_wgoC-csvDC4944h0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=g6x_1VBlC7oAOxjq-wtVOgsNgzI0QM8ZnQG3w3GOAo57KD9BC3OLKioY7qcIRP0PmlOnkdPdNobVT8wOTq4Rz04ULzyht3R1qpvtDc1TKweMvds9bsPMPDHdsJXfROxqEw66GUmssWgeyaSMTXjWf9HyeZXtnGBAVFGbwI7d9HQfkG057jkUSUyAXkYaK_4RYRUdHpHG1bSKCjywk_gWUucedrMjcOjkv-rbG-QcGc5GALo9MFxd5lD2MlJX6OnC5hJkJm9WACfFsqnJsFZJVLwjaj0HiDyWYqZ9kIls794F5d3JEnAn2Hccqv7osaH7AcJx_wgoC-csvDC4944h0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgkiASlsqMWt8-SiN4rYadJ4FoK2qQxgWwBkmQZIqWmLh7gRclcqAiYlpPVAFMRGPyPJ1kzFpCGN1YFgYm20pjgdHPk3kQNf4B4SC6NCUaCsmRybpPpzRABlKWhc1yNDExc2-L8BV3V09hF4N3F915Ja-OmlfKpKSJaAMwVZt1JGnjWA0M_fivP5iogO39hxxauMWTl2RsnNm4gbDuN7737_gfeM-iYR9gYCG9MXdvVuJRn8k6oGC2Xy2yyz18tH3pSMP82n43-pStMef3Y1yZCWJ7WJu6XH1MvD9FHdUyHhmPnkuKZREIZvWxFGrI5nj1nxxHQnupR-nbRWCnHL4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzexUX3xEBf8QWLsC5k8PkFNKPEx6Ar1JslVX1i6asAsVChG-c1rlmrXQrnTt_JKMaa0-iMUYN0_aeKV69x6h_haIoPntnENDdI4yhGLh7If7HBZbb1XTG-TIisefUnEMIfAVN5CA9Ew1hx7O5ktcn6RPX1js-XiKFO06Q-2_1U-3SJupw7QCmJfFjcW-QY0Qk_PNYy3cmejaM39iKwvyX_kSvwJZZi2JERWZzgxr10FsDgKi48LIK5a87FOI2fP9QSLlwf-xN-5FHwmmPqVAsATaivci0c-NTWSQTSHoaNIwwvfAfewPUMujiTgWuIzPsdI0BJiLyGFMoD5GX9jtg.jpg" alt="photo" loading="lazy"/></div>
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
