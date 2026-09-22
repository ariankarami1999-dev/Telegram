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
<img src="https://cdn4.telesco.pe/file/faq5W5V7_Zgni-YoUHNNOmFH_-waiFFQXROGd0eCYCPKbfy7zd-p2tYA9VUvlhor1QsqtdmUzjyIqNegJk3elgNhjRQ8FjQ2K3x-YnjVH0NhmVincRo8RrfDgPOe0XW3L0--RaiSUZNnsvFUerpHsS9zd7Bwwl7A-kPmC7TRs9Py6pnMdA8nuSDfK-jjDX5jNTnYV-cG-RyFalkNkBycX2gHNh53X0XwEg2M5FuxoNXQ7k78a87Ju_llULuuZIfsbLOeN7ltq1PZSOFx709KHDPZX_SZwM5b6YFbHwDshia9QFJleEFAZ8nGX-V2g-NW-nT1cvpofyyFqG8cjAm8UA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 22:30:47</div>
<hr>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UniU-uEYV0773F2efC4bfQJnDDp44MlbENld_-xi2zstdhLiwBrzAepqLIQMxW8lI5rZQW3AMcPuS-eYGRRuC7S9Eh20d9-ljfne6EqofLKSnqLW4ieykoI1fDaGKLtz8KCqU9vTsYz9xbdb5mZnUHNIHEOzykJzh0_5UmnT_06in3KLpSQ_7Ap7P2Vz-jfa0bZRZueBh8iWRrlD6okwHSU3yGKjq6_suCoVrHi18Sz4HPkg3Yi0Bu5-lTUUNzp0Nno8pEHjIO1HyVvu3RupNvwes083Ueb-iwkmy3J-FxU0x_FrFZxjDx9kNEx0Htec2xjDPzl2iLtzqanrreR7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHX55iI1BW81CKqZcPQdfvzGIWvggqSmU1nk8jeRoAUMzYhE-5I2VOOA1GdJboNet7osvVQAMU8CRVh2-FALND1Kj40Gj4HmQnmz7d1GEJhoyivyTjT4hCOzwFO80UOlf827nJwtFPk4Jw35-7Vpcx7MKoGvsicib76ISJ_WmEd9RFu7bjr-9b97TphtKgt454P-HL6fYokpBvwo3hD5mzVoBJUcEScCaySZVkjgwYdgYKjbE622wtMJkZxebVsikUKWuW6sQLpa5vj_DEFB8OoHd6YUdY49b722YpiGC80j5LyUYJSOU0i_dUo3L9yej4CCNDtRsr46gYvIgPFszw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmGYFcw9RaxkLeQGdNG3fKATIesq5DCXurXTquc-iZX8cjL5_VEjDiettKKBpkVZ4ZBKlN7P8a8Qkgp2ClqC2ZuFDJv65BWxKkBDaTb2H03XJTXDrfzW1TTG4mXTIQ1OMTthjcMl9wR_JHQaajYFaKnvXBRrpFnIrX2Unu_LJS2ORWXNRGAeuSVKwu665BeyrfKSnWD-tBgHiE1G_siFIjnpkXztaR650vSP_zi40LFhgkWUHXADoM23lbUsfj5VFHyoJlhoukAZhFKQbCBrCKS5APvsPcAyJDagkOvdGo86ntt4AJ7icJZbqRH96cWnv0JuxPKGQWEwK2e_0Nvckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfybZB1XUBfVqswFk_RPCE1cXU_1qmViOTQg7hGXCH_yy-6OOaSasG9tZaLuRblF0Yo77CusIqteqUgqHVHJ9ksyIytVu1PP_Y38TOrGCjMuOAZKt3cxcu88vo5UfQGSvg7YkKHzqkHrJGVn4tiHeJJxhf9wyTHHdiDxLQ5XxS8tFwoWOLaPLwefS_-WZzZWMpd3VmwhT_gvtnhrUpfHThGXK-IEtpNiMakFX-bG4ORjMfOXS9gL1RwtXa5ESsbhfCMLpD5pV5Ae6qZ9Vkjz-6h7et4h1hBaWXgXRrn3ELwXIHHkYBTfcEyGstZ0ht5-ECFPGs-BPByQyGUF_HNWyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu2bwnyJwa19vUcFWo-aEXc-DOiXMRJ3Aly99sMn8R6QFNOPMNQgwiOUNLczkos1QhN75NHCNptrqFVg8BjUzrzJmCObSXoKSLxbh-sOsLFx_pFiG53gNMe4MPoX1RxRzd2ZjJBSc6VCxO4TIC2lDEXjN5TA0x09mhNlKbF7NoJSWCaP9a6ZM9KSOHyrvWcXnI2F1wkU-xsTvI2FhPwDV2NOrCr6PZlOfblPlWHkqRkK-Uwdd9R6mDIQVp_37ThUI3VuMJasQdCbdxermwoq4rHbt9ynScBwzxycWKc7vJ-L5F8HqHWsPir1dxnMLyMSIhmLa9SJaNjabCiFclwkxTc4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu2bwnyJwa19vUcFWo-aEXc-DOiXMRJ3Aly99sMn8R6QFNOPMNQgwiOUNLczkos1QhN75NHCNptrqFVg8BjUzrzJmCObSXoKSLxbh-sOsLFx_pFiG53gNMe4MPoX1RxRzd2ZjJBSc6VCxO4TIC2lDEXjN5TA0x09mhNlKbF7NoJSWCaP9a6ZM9KSOHyrvWcXnI2F1wkU-xsTvI2FhPwDV2NOrCr6PZlOfblPlWHkqRkK-Uwdd9R6mDIQVp_37ThUI3VuMJasQdCbdxermwoq4rHbt9ynScBwzxycWKc7vJ-L5F8HqHWsPir1dxnMLyMSIhmLa9SJaNjabCiFclwkxTc4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=X6_BB6gkJiSABsUORcfhGJkqaTYGyoX8CKT3KYsq40OeXmKxck5ZZEfAx5MHqUlWBrL96oW731iYuRK57GXcdCeDclVq2NkCxU_JfMdS3zlkjO9zCDgIwhS6jd1cHUByFvoYoc3cI0jfb8quXYhMyaYc69JCy6pEa2VktxOrm-60cGC0A1DqChqoANAOY9hC0ivHfk0eln9BqW7mSqgi1g68t9qAkenHgKzhKkjuPT9L_4wD23UnowcW35r6epql4-7s4_9HYQk65PdwgVLjz4R6cC60Ct69nxYU5Oy_fMLrHyk1E4QCNp6VqqeCgqgLUShxxlKhvIGh1zx_5GCVEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=X6_BB6gkJiSABsUORcfhGJkqaTYGyoX8CKT3KYsq40OeXmKxck5ZZEfAx5MHqUlWBrL96oW731iYuRK57GXcdCeDclVq2NkCxU_JfMdS3zlkjO9zCDgIwhS6jd1cHUByFvoYoc3cI0jfb8quXYhMyaYc69JCy6pEa2VktxOrm-60cGC0A1DqChqoANAOY9hC0ivHfk0eln9BqW7mSqgi1g68t9qAkenHgKzhKkjuPT9L_4wD23UnowcW35r6epql4-7s4_9HYQk65PdwgVLjz4R6cC60Ct69nxYU5Oy_fMLrHyk1E4QCNp6VqqeCgqgLUShxxlKhvIGh1zx_5GCVEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=H-W5rpnZvYmjCpF1D0Wp-7igePcz36M23QpftoYD29iRF3Dd9vchcU-Pg3LmdkZy4b2Vn51GVWqv2MnWaS0cV8fbbtKDux8dfvBoxf-YXNwiYP73CkL56Ew_YD7cDUm1J3oSAa9SRqaivnHM6Tb48_zY3wDlpr5DKpt1EJm7C8nrKeAwsYssoxRYYE-fjwvrmbkU8t5hQeb9fBae1zxqmLj2Dnv7EXZ_yfRzTufMH5OnMpBZhggQrsp90QS-mm0FVVTL76cttsHV2UzpS3LXrAlayObhEvle3ftc9UI9BaTWRjWZPTmuHzfpgHBpFd86EuqW9YpgHPN8cUqSSyG3IX_MamjWwcjjDD6q6GmUoqBz3YZrwbuN-MHh9J2obZx2OUSc7GekE-4X8zDUE4vgzdHGlju81jhVgHAFSC9QG0y6S3Q1A5Skk7UuWh9IzZ_YNkQK3cVeJsJ1os2xuFpMNUlhp4heebSunZ7w-NtD4jzBpyvcfgyaiVyIgiokLTqrqHKYnUczhvosKVLBIn3hipJ1T_FIsyYlyfapLP0bKzFPCGNB8G5AU6OXghWURIv3eYJduqHuLsVNLVwMQN1NJrUoKGUSg5J-Gtzgyqc_LkFnjbasLc0pvi1VW_AtvPgN1XDn-QZnW4xE2jDyB1VFDqZBsZkX1M1Ohouq2atYYJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=H-W5rpnZvYmjCpF1D0Wp-7igePcz36M23QpftoYD29iRF3Dd9vchcU-Pg3LmdkZy4b2Vn51GVWqv2MnWaS0cV8fbbtKDux8dfvBoxf-YXNwiYP73CkL56Ew_YD7cDUm1J3oSAa9SRqaivnHM6Tb48_zY3wDlpr5DKpt1EJm7C8nrKeAwsYssoxRYYE-fjwvrmbkU8t5hQeb9fBae1zxqmLj2Dnv7EXZ_yfRzTufMH5OnMpBZhggQrsp90QS-mm0FVVTL76cttsHV2UzpS3LXrAlayObhEvle3ftc9UI9BaTWRjWZPTmuHzfpgHBpFd86EuqW9YpgHPN8cUqSSyG3IX_MamjWwcjjDD6q6GmUoqBz3YZrwbuN-MHh9J2obZx2OUSc7GekE-4X8zDUE4vgzdHGlju81jhVgHAFSC9QG0y6S3Q1A5Skk7UuWh9IzZ_YNkQK3cVeJsJ1os2xuFpMNUlhp4heebSunZ7w-NtD4jzBpyvcfgyaiVyIgiokLTqrqHKYnUczhvosKVLBIn3hipJ1T_FIsyYlyfapLP0bKzFPCGNB8G5AU6OXghWURIv3eYJduqHuLsVNLVwMQN1NJrUoKGUSg5J-Gtzgyqc_LkFnjbasLc0pvi1VW_AtvPgN1XDn-QZnW4xE2jDyB1VFDqZBsZkX1M1Ohouq2atYYJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=OwLSuuGn6UZp8mSB7dfl3Li220SVbxkZTMP22WX2ZPNtHp16qR6WM8Wt4JIhvXA07PWurigxy85JX0NAHCsBOigMYSuBdlpyz9FSBAHoS7T82dDQ5b9diwUTXmx2EQ2T_vpQRKYdBiw4OC6e1-rn6AzKYbhdaqVNg_M0xWsCjvh0B09tTFj6VGvIqIgxviIyT0DuxTgr5rgzaCikSBVtzGZfg144Uil7Ze5c0u7T-hKx_9wCjoeIX-Q1C3ttnzUpk86o7hbAAgmy1g5i9yzVfRRrVXbjECNPxh3nsuYZxH-p0Bg6IK1W_UwXJquls__Yv0LfIW8uof9pmjaM1Xe3Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=OwLSuuGn6UZp8mSB7dfl3Li220SVbxkZTMP22WX2ZPNtHp16qR6WM8Wt4JIhvXA07PWurigxy85JX0NAHCsBOigMYSuBdlpyz9FSBAHoS7T82dDQ5b9diwUTXmx2EQ2T_vpQRKYdBiw4OC6e1-rn6AzKYbhdaqVNg_M0xWsCjvh0B09tTFj6VGvIqIgxviIyT0DuxTgr5rgzaCikSBVtzGZfg144Uil7Ze5c0u7T-hKx_9wCjoeIX-Q1C3ttnzUpk86o7hbAAgmy1g5i9yzVfRRrVXbjECNPxh3nsuYZxH-p0Bg6IK1W_UwXJquls__Yv0LfIW8uof9pmjaM1Xe3Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1uafBCIUHn2od0goCVT4uZteg6GLieWYlwK-8D47bDxeSU0ev_JbLBwfgrPd0cGFAzGJZgOiemsGUXKkDPa8dUXDkmIimXdltlbMmdklOfE9F3ZO_SUR3WJpJAEXVfrKLgY_UthJssTicDAuiI0SQMym9FvTY4PQjqdAoSMWeQgH86GigD2ZnQqJlGCCSF5OFI-f4ys3saILMhyiSQz3Ub_dW_NGaXVh5WByN7qY52NyJldF03S_-xJRL0KwB9T7NzA03KwEI7uRb-syDQhTUZYqR32UpxT7hBKi8hC31-SvrsnciYYfbGcn0g2vRVHZwEgmXs4RPxJfpBgYjp5kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=fPSy0mQv6LJ2D46Rbb_honmgXZicuDIAmqbqw0G38kSknf2LxDr6ZcW7T38u7IOrrf_o7opqUVSu03Xr8fzZX32OLr4cUfT2Uvtp0uLYYFR28_BMMdGLzFpYjk-PN8WInkHYOQWI_mQ7HgCMIfuW6P2JMrOEXWbnUtoDdS0pPTNlZ4BsSK1LbM25-Z-TBk-ZAQgSXT7NC87E6vsj-0OSZhmOr_oU4bT-pyXnjcvHpcgJlNyxGl_pnPXLrsmBH6enJp39kL7KmB8q4yMcxZG2gBnOQREzfsdUQJ3rzLiQo96SQWNGqypE3pspgOnFJVGbcDkqi8l2OGqC33jxW6BPbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=fPSy0mQv6LJ2D46Rbb_honmgXZicuDIAmqbqw0G38kSknf2LxDr6ZcW7T38u7IOrrf_o7opqUVSu03Xr8fzZX32OLr4cUfT2Uvtp0uLYYFR28_BMMdGLzFpYjk-PN8WInkHYOQWI_mQ7HgCMIfuW6P2JMrOEXWbnUtoDdS0pPTNlZ4BsSK1LbM25-Z-TBk-ZAQgSXT7NC87E6vsj-0OSZhmOr_oU4bT-pyXnjcvHpcgJlNyxGl_pnPXLrsmBH6enJp39kL7KmB8q4yMcxZG2gBnOQREzfsdUQJ3rzLiQo96SQWNGqypE3pspgOnFJVGbcDkqi8l2OGqC33jxW6BPbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=C3iTz6fJjLquhc3jZ7FGPcjBnqEeZj6VG2g36Lvtu0evJktIZPjw08V-ungQ4W43vmZ2n2qc1vsWXvDDrLVj-wcCp_5U-cRC_D3sgKFkkS-k-xXqzXIAiNtM-wggEob0kvmyhA8oAaz0FDhTSoYlEfxeD1sTMC2n8p3ULJdhQ48ZawPo0gWXGAakutY2rfGUkANq3TMu9EkWk-KDHEorjpsxEv47FL7gHLvQg9--pGm0PlCLSNgUkmXHfDvahMg0W2tcq9DmbPT7yj5eBqblxMOWxSdba-Si73TEympa-ETMU94_XWmHGKkYeP6wb2JLtub_hjPrMLhlgNPij4zXWF1kTwszOAPlGvBPrQ-KOlfyq96TFsthgGPMAvoIrXq4exzcYwXbcYqsNBERk8VzwbA6JbQHSf8ObTxSzaWIPXMJ6BzpgKntpVmT_fvyuiIpRT33YbetisXkC0wwFYguIvw7hu1jj0PBUtOgVtS8s1U1GxU6NNAfrn3v0eTY88keDWrYKXiaJxJYFrOh8O2hSNNdNGhKH-8shLLi1etFYBrxkLC6xAMxDj9zlvHn3TBs4um_s8xTcOc-7ivwnSv_knvmHtO3yHNU2U4zoAgNJ0F4sTWYnlgr1QkwuHU0MtAWKNVPXkbYnqOPtCyH0ZNpcsD_ZYgnpVbJ2GrIfGvNLDM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=C3iTz6fJjLquhc3jZ7FGPcjBnqEeZj6VG2g36Lvtu0evJktIZPjw08V-ungQ4W43vmZ2n2qc1vsWXvDDrLVj-wcCp_5U-cRC_D3sgKFkkS-k-xXqzXIAiNtM-wggEob0kvmyhA8oAaz0FDhTSoYlEfxeD1sTMC2n8p3ULJdhQ48ZawPo0gWXGAakutY2rfGUkANq3TMu9EkWk-KDHEorjpsxEv47FL7gHLvQg9--pGm0PlCLSNgUkmXHfDvahMg0W2tcq9DmbPT7yj5eBqblxMOWxSdba-Si73TEympa-ETMU94_XWmHGKkYeP6wb2JLtub_hjPrMLhlgNPij4zXWF1kTwszOAPlGvBPrQ-KOlfyq96TFsthgGPMAvoIrXq4exzcYwXbcYqsNBERk8VzwbA6JbQHSf8ObTxSzaWIPXMJ6BzpgKntpVmT_fvyuiIpRT33YbetisXkC0wwFYguIvw7hu1jj0PBUtOgVtS8s1U1GxU6NNAfrn3v0eTY88keDWrYKXiaJxJYFrOh8O2hSNNdNGhKH-8shLLi1etFYBrxkLC6xAMxDj9zlvHn3TBs4um_s8xTcOc-7ivwnSv_knvmHtO3yHNU2U4zoAgNJ0F4sTWYnlgr1QkwuHU0MtAWKNVPXkbYnqOPtCyH0ZNpcsD_ZYgnpVbJ2GrIfGvNLDM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_79v0EpvMUjiE9_wwk_W7nlJkMwddyNi6vGF7q27DIspOYnfAowucBxtwRlxVySKni6Svf90-ZaJK0r38_sN6DPLOLAzCpTcSIsmGdlssMp5BEc_I_PF9a1IRj2USnl_EQeKSk_FkrRMOcgDRUxoXvtQwFuUlO1tNGvmTSQNli2OTou_OOxm_fmnHKOWiYj8eGvn9m5jCoegdpO9WHXH22vkrGPboynu8_amH_P6KiB7pQ9AUCpcFNnW3G0B0xOC5tcJbjudiKgzFq9ep-_xWrk72pznjLPXXPtPLQiVdqpP_k47RFwrUFYKdQAZUTQjQ9OPxoKFVlNEeQLTkHCDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=ieQghEYeR3TYG1-MlP9NImaLq7gqt1JNc9P51Zf9_TCABecOXbNpRS5ImYeBDDq7LQkl9a5tzM_5HaXq-ljK9Hd14KDVC6iGCQ1apskvTFZjIXJRW5bBFvy3cj4nn9jrs0MZC1pOkV5jwh7-5yaG-LLXnCf2hdG_DmgEgFX9h_TlQpbzSkCGD3b_b_bAMrQPxMnpKSbBgKPen2HbU3EqR2L_J59i61bJThce7wm2YjDrYPrBzzleQWc7mmWRNwUhxa02glKoku7Djc_mz3iMKmJV8hAbhM7AiBDXhTYWfDERK44oXX9jpF0veK3m9_twFxGbQTR02lAasatpIDsycmUL7Rl5j-m4oeTcaVG9CS1mxFePcJLhwGgRqJCwEu0oStWetsCH5j5eclnQCon0vvVtHVpiu87y-ywMU8IWK_pw1B8AJF0nbYiznphibgdUs5f2fyZwPEjuls2AmbkN-OHtePqirMSpIIDPW5_ZUZ6-yaGPBGSa24EWGOm9uthOf01UTmgG2jZoQQXK3qRbHOvvKO_VShyhpqwr2nYLjzDjsy4ZvcfAYC6Zz62fBJ9vt_mNEHpVykZmG07bis86bfeu_VN_NRdVscdpJ4MfVOsb9CMeXDopqUpYRleIWMMM6fFj2GuTZMLdNp78vA-bWIQO7Xb4bupPiy98hyaIqqk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=ieQghEYeR3TYG1-MlP9NImaLq7gqt1JNc9P51Zf9_TCABecOXbNpRS5ImYeBDDq7LQkl9a5tzM_5HaXq-ljK9Hd14KDVC6iGCQ1apskvTFZjIXJRW5bBFvy3cj4nn9jrs0MZC1pOkV5jwh7-5yaG-LLXnCf2hdG_DmgEgFX9h_TlQpbzSkCGD3b_b_bAMrQPxMnpKSbBgKPen2HbU3EqR2L_J59i61bJThce7wm2YjDrYPrBzzleQWc7mmWRNwUhxa02glKoku7Djc_mz3iMKmJV8hAbhM7AiBDXhTYWfDERK44oXX9jpF0veK3m9_twFxGbQTR02lAasatpIDsycmUL7Rl5j-m4oeTcaVG9CS1mxFePcJLhwGgRqJCwEu0oStWetsCH5j5eclnQCon0vvVtHVpiu87y-ywMU8IWK_pw1B8AJF0nbYiznphibgdUs5f2fyZwPEjuls2AmbkN-OHtePqirMSpIIDPW5_ZUZ6-yaGPBGSa24EWGOm9uthOf01UTmgG2jZoQQXK3qRbHOvvKO_VShyhpqwr2nYLjzDjsy4ZvcfAYC6Zz62fBJ9vt_mNEHpVykZmG07bis86bfeu_VN_NRdVscdpJ4MfVOsb9CMeXDopqUpYRleIWMMM6fFj2GuTZMLdNp78vA-bWIQO7Xb4bupPiy98hyaIqqk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=qwH3kLRkfFOnAqFHYI8SBlUKDX2hqnKVRSmEUeVr5H8HMPZp27rbHsgeytn0EqynxwlR0YDMqawYboQLLlUVv-SFTVH0vhgymbt-m00ru4pW58_T3j2mRMBzDvthYe7uhPgPUmbmS4-o0_wJdsJtovkSVKoGeUpo-QJxfesAEgRzsF_quY91o-QAw-k9pp3IuyOpYXqoGKXMnVV53KRlQ0DheYXqf0N8jOKziH8EX2q-GAuhk6LakdWAdw7daOUDj3YhaMUZptdYQ-0y3UBa-uMKHf-OhCRQ61jd7fK0VjqF_vDvdgKhTqjoqErNnnX_-oF9yx5KIAG-N91uXk4gbW1mQUJUkOgPgtr_zexkeXYmQ_j4cUK0CI6bruDcl0DKjZGGzkYGOnGKhK7KCIm-IE_ak544MmnPAMu62fPzvqybxOOry8h7LraTum9r9-YchR50Su8hj7TiK4p-YH2ZwR9jI4daHhpddk-rlxSjMxAClfSNXF4aXdu0yStbqGn9Qccz5sdR8L6q61KNKxpbH5m7jyjmh3zRFSxLcgcxcr3HgU6cmag62-4Tg2Arjth5m7QcCO7r4dERZO4RqYWoWp81R0j981eS2rg4Y27o9bnP_lmW47ge5jjL83RnlP374r_jUhRRysrpj_2XkK1T6tq28YgUfIvAJ_VOF4p0LqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=qwH3kLRkfFOnAqFHYI8SBlUKDX2hqnKVRSmEUeVr5H8HMPZp27rbHsgeytn0EqynxwlR0YDMqawYboQLLlUVv-SFTVH0vhgymbt-m00ru4pW58_T3j2mRMBzDvthYe7uhPgPUmbmS4-o0_wJdsJtovkSVKoGeUpo-QJxfesAEgRzsF_quY91o-QAw-k9pp3IuyOpYXqoGKXMnVV53KRlQ0DheYXqf0N8jOKziH8EX2q-GAuhk6LakdWAdw7daOUDj3YhaMUZptdYQ-0y3UBa-uMKHf-OhCRQ61jd7fK0VjqF_vDvdgKhTqjoqErNnnX_-oF9yx5KIAG-N91uXk4gbW1mQUJUkOgPgtr_zexkeXYmQ_j4cUK0CI6bruDcl0DKjZGGzkYGOnGKhK7KCIm-IE_ak544MmnPAMu62fPzvqybxOOry8h7LraTum9r9-YchR50Su8hj7TiK4p-YH2ZwR9jI4daHhpddk-rlxSjMxAClfSNXF4aXdu0yStbqGn9Qccz5sdR8L6q61KNKxpbH5m7jyjmh3zRFSxLcgcxcr3HgU6cmag62-4Tg2Arjth5m7QcCO7r4dERZO4RqYWoWp81R0j981eS2rg4Y27o9bnP_lmW47ge5jjL83RnlP374r_jUhRRysrpj_2XkK1T6tq28YgUfIvAJ_VOF4p0LqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=G67fgBgF0TMMQSwWKPWN5sTGWutEvVRvA_06PbZy_FGx8WIfXWwQiX-akzTAdAzag077hbyMxtERZwS5F8O-0Tm0m1u5rhAOPBVZu4zxg5FIi4_3-fTvhntEiuDU2VRVDqO0U2VXGn2JfG2iPEduIm0D4Ilb-XqibNMBzjDGNYsvdWveVXLBuMXmImXQGHyR-TTl4ehFroDpJ5cXvex_NcMmyiDYY3Pul_1AN02U7Qgsxe3YmCd3Rt961yyWkR4Fsp1u0EH5_wp7TTd97jjaPFxPrZrwj5JYbEv3pJMLH2cWJ-_CT3HS_GPQ5ClbKBAgcx9SlMN2EhXGAjoBv1HzHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=G67fgBgF0TMMQSwWKPWN5sTGWutEvVRvA_06PbZy_FGx8WIfXWwQiX-akzTAdAzag077hbyMxtERZwS5F8O-0Tm0m1u5rhAOPBVZu4zxg5FIi4_3-fTvhntEiuDU2VRVDqO0U2VXGn2JfG2iPEduIm0D4Ilb-XqibNMBzjDGNYsvdWveVXLBuMXmImXQGHyR-TTl4ehFroDpJ5cXvex_NcMmyiDYY3Pul_1AN02U7Qgsxe3YmCd3Rt961yyWkR4Fsp1u0EH5_wp7TTd97jjaPFxPrZrwj5JYbEv3pJMLH2cWJ-_CT3HS_GPQ5ClbKBAgcx9SlMN2EhXGAjoBv1HzHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=IS92pdcKHGQtFm2S-tOGWxJY4KcOdiFVR8jgesmHs6eFvMXSyARgztFNJdWSBdXv5YA6GMYqxkqeGspQ_0XI4204o0b2QOXFAUJWutR7TNzXqGss3vB1-4QgvFlgR7sQvAwby8lboy45l8WP9K06RMCUqitStwq04jwhAjJMy7bigTQ4bPedkAjikfK8nBw2qnag3Eeqt4CVvxtD_QwRZMjuQDR3DxZUYu7GwmkrP5HOGAib9A3FC3XJ860NKEQkPUAhpHi1TsO6pPZGYrGPc6ObWcjMQQ7gxyvYVngX2dI87LB_QIP5knTCZKf0wBF897b4P4QK3WejGUgDy68BvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=IS92pdcKHGQtFm2S-tOGWxJY4KcOdiFVR8jgesmHs6eFvMXSyARgztFNJdWSBdXv5YA6GMYqxkqeGspQ_0XI4204o0b2QOXFAUJWutR7TNzXqGss3vB1-4QgvFlgR7sQvAwby8lboy45l8WP9K06RMCUqitStwq04jwhAjJMy7bigTQ4bPedkAjikfK8nBw2qnag3Eeqt4CVvxtD_QwRZMjuQDR3DxZUYu7GwmkrP5HOGAib9A3FC3XJ860NKEQkPUAhpHi1TsO6pPZGYrGPc6ObWcjMQQ7gxyvYVngX2dI87LB_QIP5knTCZKf0wBF897b4P4QK3WejGUgDy68BvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=OAKx2yQ3sbDHvlcu0cptkthiXO7ZPqHGKPjZ9Xewko-KD6nyE6KTspBBy7T2-U1njCZ20s3fnRZ_mHiRhdZfZaZF8XT4rovs3GBMRv2s_ROliNa4bctp-UQJDhw0zGBOjXL8ulMPnUJq5G1dObcKwjieaSEfJN8thPOv7IwtnaSlUKPQEfg1Za7xHB1CrdraCE5pKJCX63LBh1iYGy97N7KnNnyr1GxJEYQBEaPsgQXnWUnrvinmpZcy1h5uQXxCsfZwWkzYumJJUB8NwQjah7o-JB8fa4dJsRRSbsNC3pd7zzXgoOlwbm5M0tLNxTdwV50hg0Q1E-kJh_gh-P-DNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=OAKx2yQ3sbDHvlcu0cptkthiXO7ZPqHGKPjZ9Xewko-KD6nyE6KTspBBy7T2-U1njCZ20s3fnRZ_mHiRhdZfZaZF8XT4rovs3GBMRv2s_ROliNa4bctp-UQJDhw0zGBOjXL8ulMPnUJq5G1dObcKwjieaSEfJN8thPOv7IwtnaSlUKPQEfg1Za7xHB1CrdraCE5pKJCX63LBh1iYGy97N7KnNnyr1GxJEYQBEaPsgQXnWUnrvinmpZcy1h5uQXxCsfZwWkzYumJJUB8NwQjah7o-JB8fa4dJsRRSbsNC3pd7zzXgoOlwbm5M0tLNxTdwV50hg0Q1E-kJh_gh-P-DNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=Q2p2p1J9GCbyR6Jz9Z0J5Tgk1I-wKWB6r6MQxMoqBPuOk0t9APArh2RRKzWmgi3Fi0_p5F6ed9pd_cDWus20vRZ4W0JR9DL4TSKssuJNTbnSehxiuw_HXayMtLOUEh7SjhBeSNj0EhAdG-wzSFKLhTGmwMDcXBFBlIPzZX3ok5Ub3Oo3gJs0aeonwBpZu8JL-3Fj1jo7Mlom2Jm3CHHy9z8SI-BcpCJ2d69U3f-gnuo7DKvwEJaZ9d_XvuVT6lzAO6NoStTaQKNoRyW4ui8J6z7gKkyg9jWsu-wIqltKQEnVcwVKCKtLiNaK_kCE4kzrakVzdpnn0C7YKWZSoc6dSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=Q2p2p1J9GCbyR6Jz9Z0J5Tgk1I-wKWB6r6MQxMoqBPuOk0t9APArh2RRKzWmgi3Fi0_p5F6ed9pd_cDWus20vRZ4W0JR9DL4TSKssuJNTbnSehxiuw_HXayMtLOUEh7SjhBeSNj0EhAdG-wzSFKLhTGmwMDcXBFBlIPzZX3ok5Ub3Oo3gJs0aeonwBpZu8JL-3Fj1jo7Mlom2Jm3CHHy9z8SI-BcpCJ2d69U3f-gnuo7DKvwEJaZ9d_XvuVT6lzAO6NoStTaQKNoRyW4ui8J6z7gKkyg9jWsu-wIqltKQEnVcwVKCKtLiNaK_kCE4kzrakVzdpnn0C7YKWZSoc6dSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=LBX_4Nr4wfGtpAFOB3IoVnrTMK1p4RS1nz4Kyp6YPggv7ncqaIxw9Z2s2nkeT9ZqMt9o-Y8lyK3GsPkQ-vFBnbGEDYutkVzC36KOkjMoL4UJRvsoKvMVnMLPfwCRZQNFpzZZKBsi5LPjCIq68cvz4hAOMiB7z4xAQHxJ5FFuLlElFIsWcqfce1oorV2Ox6JEt2MKpU2I8nU7R5XLJp6YAnLRYSew7z3Qxw4hXs3PcU1ivhJz5hKPgyzN4MmEHNILyxOmfAlqpgFOJ0hnDTgK7WdYr9rHldTXpXd3lnY4Bwvuxc0zpUfSAfDX69BYQflqBOu0uK3Wen3vAiZnKSKTmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=LBX_4Nr4wfGtpAFOB3IoVnrTMK1p4RS1nz4Kyp6YPggv7ncqaIxw9Z2s2nkeT9ZqMt9o-Y8lyK3GsPkQ-vFBnbGEDYutkVzC36KOkjMoL4UJRvsoKvMVnMLPfwCRZQNFpzZZKBsi5LPjCIq68cvz4hAOMiB7z4xAQHxJ5FFuLlElFIsWcqfce1oorV2Ox6JEt2MKpU2I8nU7R5XLJp6YAnLRYSew7z3Qxw4hXs3PcU1ivhJz5hKPgyzN4MmEHNILyxOmfAlqpgFOJ0hnDTgK7WdYr9rHldTXpXd3lnY4Bwvuxc0zpUfSAfDX69BYQflqBOu0uK3Wen3vAiZnKSKTmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=GpFeFZxNWvf9FAdjCW5g13HmO80wToEgE-S01Kb6opj8_LoTcSCsYkUithOSV098M5uTfZmxnxuCVOlhCzvUbtJYlsQI-XOxgphkJ8N4rA32g4NjOGzJfNZC8CacVxspslx0rHrVGBmnksyj7P2CH2TOYlYCYnOKOni1HnK0gHWjFKs79lrF3OMbmJLeDsZnknaz-4yoz38rLv0ZxLG7D13TGKrGMLeDI-XTfsNokJtxVfZe5YkfFHUWVIT05yWngbF0jecvN2WqysbzfeFQTT6cigIYVP77KJeFc3Hxqe4c7AtatKXlSXZyMky8MbGvxb13vc5zBpeDUdH33VSUCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=GpFeFZxNWvf9FAdjCW5g13HmO80wToEgE-S01Kb6opj8_LoTcSCsYkUithOSV098M5uTfZmxnxuCVOlhCzvUbtJYlsQI-XOxgphkJ8N4rA32g4NjOGzJfNZC8CacVxspslx0rHrVGBmnksyj7P2CH2TOYlYCYnOKOni1HnK0gHWjFKs79lrF3OMbmJLeDsZnknaz-4yoz38rLv0ZxLG7D13TGKrGMLeDI-XTfsNokJtxVfZe5YkfFHUWVIT05yWngbF0jecvN2WqysbzfeFQTT6cigIYVP77KJeFc3Hxqe4c7AtatKXlSXZyMky8MbGvxb13vc5zBpeDUdH33VSUCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=CYLadeEA9tZ2hVxiDsRO4m0yHi_bR_qXFsEkm0i1-MLois5aADKgmMqWBl7GngZKh1jU3BQA9ToDhZXX30FU3JmJsnSzbMgXBOLLikRUHTv9fUkRQJOR6TAAYXTSj7Y5g5Q59T-84vfKbT-BYAXUEsyHStLbi7hQX4-NOo9oJvrqRhahb5Qg_w92T26Q9K9NAlzsHe4JFrjuAffEeGXP8rbu-K55hhhJgNC8H_1tjJSOEYE7o6lFmiT4NMaPboWjnrEsTp31pARxwYZ-ydmU-e4yvvrYf8giLF1cKUvrp_8QcOyli0EnSbvB2J3u8Ag4wazp1NQ1puTudwwIms6qPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=CYLadeEA9tZ2hVxiDsRO4m0yHi_bR_qXFsEkm0i1-MLois5aADKgmMqWBl7GngZKh1jU3BQA9ToDhZXX30FU3JmJsnSzbMgXBOLLikRUHTv9fUkRQJOR6TAAYXTSj7Y5g5Q59T-84vfKbT-BYAXUEsyHStLbi7hQX4-NOo9oJvrqRhahb5Qg_w92T26Q9K9NAlzsHe4JFrjuAffEeGXP8rbu-K55hhhJgNC8H_1tjJSOEYE7o6lFmiT4NMaPboWjnrEsTp31pARxwYZ-ydmU-e4yvvrYf8giLF1cKUvrp_8QcOyli0EnSbvB2J3u8Ag4wazp1NQ1puTudwwIms6qPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtpHLd4G_yv4rhGS3jBXqMIKZu3TIuylt3iT-9vgZSyrz5KlOcrHtuQKmPTm5o2epmk1ZaSnhG0XQRB2_3L7ao9l0LgK2JLRY28IMbYXBi78KphE8yMZoa8QLq9b1h2AgswC9pg5aSjjX3mM7JvCZlmjI-aDcQgPmOhDR7HtADWAvzRnDClhe6a_fcwqwHpHbv2wioBanWNpmgkmMkP8lz_u0SPTgWbBmf2pix9r6Q7s9m9sEF3aLvUoQjnvVCHmfdPJYTOIhtcZ2qjfKJzhEXpth9kykpwWES27CePWMQH4MaBtY3F_MkHTOkywF70iMP-ZGtzEUPMuB8iDP8jzRg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=EYjpBu7XwIAgA3Q_2Pkmqx7bGhgR_irpehnO5gzWtvIZ2Ed2Dg7O5Zn9tYrIzUU8QHxMCEMWZyS-fkBlfrewbmfxi0nTfnAqPxf7yPOBYCcBuBli_R9PUjh4cOW1jCwydFeOvHOcmjmXl8F84mLJJHAIK416ykLii56LKEej9Fgia42TSLmtASUp8b0R4hNsMQSz6OT1mpdP2yURLpt0h9RgYEfCivg6DKV3ZF-7uHJnbVI6HPK-u74_ZnSLX05_SPIHnZ09vk_4Ze-gWQF3gdtLxfL8oPjXrtN1EuaTaRczOBlViYO2dX-Igt_KPR_BTpGeppet-8ywQunZWo7MqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=EYjpBu7XwIAgA3Q_2Pkmqx7bGhgR_irpehnO5gzWtvIZ2Ed2Dg7O5Zn9tYrIzUU8QHxMCEMWZyS-fkBlfrewbmfxi0nTfnAqPxf7yPOBYCcBuBli_R9PUjh4cOW1jCwydFeOvHOcmjmXl8F84mLJJHAIK416ykLii56LKEej9Fgia42TSLmtASUp8b0R4hNsMQSz6OT1mpdP2yURLpt0h9RgYEfCivg6DKV3ZF-7uHJnbVI6HPK-u74_ZnSLX05_SPIHnZ09vk_4Ze-gWQF3gdtLxfL8oPjXrtN1EuaTaRczOBlViYO2dX-Igt_KPR_BTpGeppet-8ywQunZWo7MqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=Hgigy2Ya4ulWMLz1_LducXO_fkECIFPe7bH8cKplpmVMKOb4PZczP_viOrC3jyOtR-UBlz10-EtzxfoNXWC_bbgQ50jwXMF6uBj5BA3nR50kRYrbCtLhC40FB2I7_HlftdNyIu-ZiGmV4DOtiVSl0d5ZKVd7pNF4vfQRKyzaLwPHwDrP9mU5bXzFYbhueyqE5NZJg8k-Ov1TUnXqHmZF7Xk63TFC5oSiY7XKUysbIkEywvla29NJHCcFGKToFobLVMmbS7Xz361-v19CLVH4hAiX5ns3ieFdCT5Fkoqqh1-DJ2g0xyukol-7hP_8iVEO5Fol0SeYbhM5y0z_Hv9Cig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=Hgigy2Ya4ulWMLz1_LducXO_fkECIFPe7bH8cKplpmVMKOb4PZczP_viOrC3jyOtR-UBlz10-EtzxfoNXWC_bbgQ50jwXMF6uBj5BA3nR50kRYrbCtLhC40FB2I7_HlftdNyIu-ZiGmV4DOtiVSl0d5ZKVd7pNF4vfQRKyzaLwPHwDrP9mU5bXzFYbhueyqE5NZJg8k-Ov1TUnXqHmZF7Xk63TFC5oSiY7XKUysbIkEywvla29NJHCcFGKToFobLVMmbS7Xz361-v19CLVH4hAiX5ns3ieFdCT5Fkoqqh1-DJ2g0xyukol-7hP_8iVEO5Fol0SeYbhM5y0z_Hv9Cig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=g6kl1m5FGFIjL-yemfatOl1Nw0tFJLwNWVuEOqKcfAy4tts6OcT10pgd66MOMVttjSwRkvl-XlQFhmfiM6YhvYb2b38Jshw5V1FMtmmPL4qf72s-DdS7oOTPYbBP7KoAQvg19lgBRmDFESCGgcUsJWVJUVM38nURjhyXozhiIB4shXBLtSYM4SWoRjCoEYgmgL0ZcFjGMvf4BkwgxeDxCkMQ2gmk5AzxMtcklcCGxifNyFc7K-l4shusMP04dwtPxVGoG81NlVHZb28HLva4aYbn9MTAwNljorwmG4SCOvVBsDwb3k9GXwb_7RCoZ-LFjlskKmdaIKaS_UD3tqORsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=g6kl1m5FGFIjL-yemfatOl1Nw0tFJLwNWVuEOqKcfAy4tts6OcT10pgd66MOMVttjSwRkvl-XlQFhmfiM6YhvYb2b38Jshw5V1FMtmmPL4qf72s-DdS7oOTPYbBP7KoAQvg19lgBRmDFESCGgcUsJWVJUVM38nURjhyXozhiIB4shXBLtSYM4SWoRjCoEYgmgL0ZcFjGMvf4BkwgxeDxCkMQ2gmk5AzxMtcklcCGxifNyFc7K-l4shusMP04dwtPxVGoG81NlVHZb28HLva4aYbn9MTAwNljorwmG4SCOvVBsDwb3k9GXwb_7RCoZ-LFjlskKmdaIKaS_UD3tqORsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Yy0gO_wQrCc-9PNk1DpdmyHu0q4XciekvRjS5PoLYB6gJ2xtlaT__7bVWzbm7ROvY6_a8AQdBvuzALiNnO_cJPP_RNQlVp6JXKIlFciL9zn-TLBhESP7eVkhyDR-kmhsJQAtOqnJP8YcOaEoDn8c-sCt4ppUL8TSXCZaOFdtSSMgX89uH4JKIxxn_vby5Why4tZodEXdnmxQRW6BijWblwL4w0a7bbVOSoYtg-BH0nF83XDKzhQQn71W9Kl6uO9kacelZS6qjMgO6f-QFqxx5iHN54d44c96onUTThLa9IOhbj9vbNl0rmAsqAKg_OwckXL4UV83KdzKuaCZjGR2cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Yy0gO_wQrCc-9PNk1DpdmyHu0q4XciekvRjS5PoLYB6gJ2xtlaT__7bVWzbm7ROvY6_a8AQdBvuzALiNnO_cJPP_RNQlVp6JXKIlFciL9zn-TLBhESP7eVkhyDR-kmhsJQAtOqnJP8YcOaEoDn8c-sCt4ppUL8TSXCZaOFdtSSMgX89uH4JKIxxn_vby5Why4tZodEXdnmxQRW6BijWblwL4w0a7bbVOSoYtg-BH0nF83XDKzhQQn71W9Kl6uO9kacelZS6qjMgO6f-QFqxx5iHN54d44c96onUTThLa9IOhbj9vbNl0rmAsqAKg_OwckXL4UV83KdzKuaCZjGR2cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErAAySqAIg9kPjMVpWSbikOA1DBU260dciRGeDLiWqOThiyuvxMArDKZKBhliIk7zi8iT6EWwMoqgWmV1GmweR5JdyKNodwP0LUWH_gTuiQcl7jcGw_TYmxM8NfhNLdXmYrdbQcg_OBO6ZL-rzKe31ckY9DfONyGRwgwyUcSj2c0pCNKD192etqRHOkv5efxGj4z0AiYPIJUnJJcc_74GmuYl-54AUfwWmjJzIKwcHCV43JPqpdp3DZU14rBFSe5XmuqeSRPoII10TobKybs3wGIjR2ln9TG2MpUTg5D9o3PoJ5ueC8oY9L-z2QULeRthhw02cT2zB6CLi6UPtDvJQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=vu96LlGkv3JUiFP_7AKRqMPKR9c8n5TRqDwh2XwJLgqoeWI40qXfZgpgCk16SYAPhC7FqLnKO8wKe22yPahzjdzk1jzZ32cI6tRcgN0apq6f-rfMZ72UevPqX2j8H0OUIcdvvf0DWIPdSKEIG4VMqR6Ke96KzEEmrcKz69iFAaRC4NWcUP2M5gSuK9MIyrgsztcrpjrnliWCJ7O6rRcBy3SbB7q_-KA310VQXOMkKl5rUlTQQfT3uHpah6DeG8wNpu5K3201oHMJykHLkQslrkXkE34UEHfu8P9rDBnAPCLTbgEpNRq0YfsZib-g3A7aqPzteaq8nMOFv4d9R8lwIoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=vu96LlGkv3JUiFP_7AKRqMPKR9c8n5TRqDwh2XwJLgqoeWI40qXfZgpgCk16SYAPhC7FqLnKO8wKe22yPahzjdzk1jzZ32cI6tRcgN0apq6f-rfMZ72UevPqX2j8H0OUIcdvvf0DWIPdSKEIG4VMqR6Ke96KzEEmrcKz69iFAaRC4NWcUP2M5gSuK9MIyrgsztcrpjrnliWCJ7O6rRcBy3SbB7q_-KA310VQXOMkKl5rUlTQQfT3uHpah6DeG8wNpu5K3201oHMJykHLkQslrkXkE34UEHfu8P9rDBnAPCLTbgEpNRq0YfsZib-g3A7aqPzteaq8nMOFv4d9R8lwIoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=RCiil6T-nFRFTyfy-8K96kd3E-cPeBwd4X5Ms17UPWFnduBcYHFCwWKPG-NVul3pJbfg23SPUqej7TVxa_BnvNe5oiyC-OkRBtO0E4sRuzUme5t_3lORGSKsAcJTVamPzIg3Wg9SP_8xIwXPQUESnA9mXybmY0BBzLgxvHgEL4005bh--h6U4VilDnvz3AmIOXiRiStd5T_gPgEknMK77oGsfXsiy43QKa3bS57wW4QsAmixqxxcppBMQB9L1NMQ9xkntmzaWMeP1E0nC5ulpFmaLTT32Qp3i0sTYliIuviRDeLsKZHuXS7rIrO1n71_IU-Xp8p3NOUmEsd4rGQ0Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=RCiil6T-nFRFTyfy-8K96kd3E-cPeBwd4X5Ms17UPWFnduBcYHFCwWKPG-NVul3pJbfg23SPUqej7TVxa_BnvNe5oiyC-OkRBtO0E4sRuzUme5t_3lORGSKsAcJTVamPzIg3Wg9SP_8xIwXPQUESnA9mXybmY0BBzLgxvHgEL4005bh--h6U4VilDnvz3AmIOXiRiStd5T_gPgEknMK77oGsfXsiy43QKa3bS57wW4QsAmixqxxcppBMQB9L1NMQ9xkntmzaWMeP1E0nC5ulpFmaLTT32Qp3i0sTYliIuviRDeLsKZHuXS7rIrO1n71_IU-Xp8p3NOUmEsd4rGQ0Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/co7UeHvESbNEvZ7vfiTfytcmA_sJu7Tn1TxIfIAWYAUgZUKQ7sSCoHcmNuajjkgzyFLc-oJyVWAs5LZ6LtmudIf8t4uKJQjw7tcexLqGfD2NoHpffZ-21p5Hsd9swltDGxb5AR3Cp3QxtUFs-ms0HGgrCNQWqjxCe5_pvffELqb7DI_c357hbkHFt4R-TmI9gFgoSI2pMulOkH5jjsvowO90jLBuyXMn5sbDzOM57rJc_6l69fI9dpUIenlyMmy1KQNTRS2CRQf9F5pdmfNhFTlGlrQre1Yoo_BpPq6dfqbGoRiodXtCJWAo64ResGmTll7kfGCa7bL6t_Mgu1gjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MxZoqOXjI7wPhxlp9R0Jv_bb-n1JhzBAkOybPOhBRFmrA2gDzFf_UtMq57QmC_EyyL3jKd0PLJNwIs3ojvAe9UdzqlZ8iyMwEi2GxyJflAhCdtVWUrX_Hze0LumCVv4YcYbGrlR9gR9EQBlVNKmlee8Skbq2Do-T-MpgZ8oCgZr4ZSTg97duXRUdm7XblsF7MYeU1A8GYcUJoja4dPhRuR5v0ULWX9K4OvTsH3RemQpqTEMzitmFNhNhPSvjnBsTvnzSgO5mtIQAyxKzYijlWW2YesiPwuEg8GFH7Ar6xtsHCPSlh5hD_Te0yPYyy1LcGh2kkB9vYR6qrkSotP9rQg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Xw98M7ByUt17sTARTIPrEQzw4P7jRheQ7kIklK2r8FeUyePxiOdWToakqK1EyRf-g9qkKLYRpNLPxRCiYEN5-uYSlxKeeYSu58J3ELbb3gAGqTJs0dLlhhEWXToqZRsXWq8XiJd2cyXFyQF8lJKWjtP73wFrj5ConuqhsqM_fbUMOoZUU5z_CPiXXOpkufXSV7D50h3MXUI9YCt3-tuHAJALPlc1zC-ha5WfRe88nY7O5lnqRGUkUqVMNdC1krP1TwUDXo4yP_qTUwEep_qTTVpEkAy5M3H0tLJUcGyI_owZaGakTOb8umLAtG5ZgLsk9lg5gBUYTnrbWSWdD2JipA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Xw98M7ByUt17sTARTIPrEQzw4P7jRheQ7kIklK2r8FeUyePxiOdWToakqK1EyRf-g9qkKLYRpNLPxRCiYEN5-uYSlxKeeYSu58J3ELbb3gAGqTJs0dLlhhEWXToqZRsXWq8XiJd2cyXFyQF8lJKWjtP73wFrj5ConuqhsqM_fbUMOoZUU5z_CPiXXOpkufXSV7D50h3MXUI9YCt3-tuHAJALPlc1zC-ha5WfRe88nY7O5lnqRGUkUqVMNdC1krP1TwUDXo4yP_qTUwEep_qTTVpEkAy5M3H0tLJUcGyI_owZaGakTOb8umLAtG5ZgLsk9lg5gBUYTnrbWSWdD2JipA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mknjvS3LSsneYzpldUKe7azFep_tOwLRsc2fs-W_lxdzZqm2_WASdgC3XBMh9SldnqjuIdAFqTBhmybHV6yIB3qq7kkzBiMh3DnUXCKoyt-KSnYqjdtwGnv1W-N0H4CS7cB3Pc71wp1iwoemVLIB1444jqZ8sF6MQ_Ch01IF7DUGcbhghK_2RnhT9zJMCVTRfS-69X4Y0QuoxVLWAMN0EkHD-G2ZvDL9YpVqUv5ebZcdS9B4uTfFYp0r83V0xOv5_rcmB2I2mA_0fkoJMLjv4J38-1VuS1Uhs_U3dReqitnl3DDK8fLCkYNL0XEwWFR84fQONHTVSPjNe3pA2z6zAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8Bzb1s9p42odrLLUWznUdiWS2ThSNKrdxOwyZynM5yi-IyiAPe7qjsqXDasPkRsMTqkSC-YQ2m2XDZszeQTP5PGceOwcpyclRhfP49w1flRhA9KPS99Tvtqf2p-jRxAOhR08hzl5ROaOt8PkQo9YA4uzYINkZBw6eQ7UZlTqkG7jLKKwr4DH8_wnh-S3HcQ3QwWWKZ9WkA0SmfgRq0GSLPcbVFKbC9z4n4rhoLK7HldEnJVQU7XRP66uuI4vvpeA7Oisp-HepAekct2oW4klpT61wsdKwUXQ_3xIc9pkSBDpgMTGvndV4OHXQZTwj0TiutHY2wlcgPilrJcqgWphA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkBZ4Pf0s8I0JgUjmwf0ED0hG3VCDX6A3DJXcYv5UaKLLY_POLCuZxk1U1uJxswA6uUavSQxp6osJKsn0oWp7tGDs7qjaPfSi_gnzmdei_GsOe44t8xlDDM1wZ6cUtYArpJAOJZ4cIR0CjV-soa1RyXTNWAi2unUeaHXYClPrGpMo56SzjNvY-9kZStsmOQ7k79xbwOgsrnIikK_oQndJtK_8TyilY2QCmbHFbuwR9tWwFI_WP9xCa6E862EDZfVFHwwwNjXl2_c27Fu2zMi5N4avKT_3DztoF1hzFDLBkQmiGTtYxzrClV83oVj3QSVhOBrbHd1GNet7GkIyczfnw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=bV78Q1-KJaWBYPHbjEu9D8dBkM48DRlDfe3NPsgbBO2wOCjs1tt5QwaiD5_UkHOTAhNH0nS6Oh3eyANGE--T6P4vsCCj27fzZh5L9zDPcV5NrGv9yS-sH8v5lMsOmH-N7ixJ4_NeONFuEl2fYz26Y-Y_DeZtx-Z7JHG2bBdWn1UrpRae7MZS3lSyitoh6NyX4cPXPyw6RloSYTEDXQhLp4EAqYblMy-ihKpNKUNJJODgxxU6Mf6zwAOiQdI-xupzITycTmIs7JVitRdiiU3z74K8BoS1toxIfM2SoLvVI3tTarssWATaFJx3Q_CFhvEme-kWusxEtCygnNWmD5ELSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=bV78Q1-KJaWBYPHbjEu9D8dBkM48DRlDfe3NPsgbBO2wOCjs1tt5QwaiD5_UkHOTAhNH0nS6Oh3eyANGE--T6P4vsCCj27fzZh5L9zDPcV5NrGv9yS-sH8v5lMsOmH-N7ixJ4_NeONFuEl2fYz26Y-Y_DeZtx-Z7JHG2bBdWn1UrpRae7MZS3lSyitoh6NyX4cPXPyw6RloSYTEDXQhLp4EAqYblMy-ihKpNKUNJJODgxxU6Mf6zwAOiQdI-xupzITycTmIs7JVitRdiiU3z74K8BoS1toxIfM2SoLvVI3tTarssWATaFJx3Q_CFhvEme-kWusxEtCygnNWmD5ELSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=pH_xyBRfT6L188JJiRUKCkyfQfdhyepr3_yvbSaEC5Gq3SzAc4By28rqFdy6Zy3Hn1qFS3PkPqbiUVMiXrA2haS9e7I2U-pPrkiRz0fX2v6q4OMJ0iETF1iGyQnJddF23zjO1rCsO3gCXFGm5P7zUiYhGwzSLPM5F6plKMUOGl0a1mRAiQsFRloLOyv7YmGa-06Zl7-Jq-7Ej2zLYGqYOfdefCzbJb3Sx8e8P611OeRqd3cnaNZG9DmLwxtml2vMJNrhGJW_euPVyqSJb5n6oHD674OIVNimV775gt9_ZHVdzcI_1BlPm9TR7ADiI3nDyoQimeBdEyPg2TjxKOWFew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=pH_xyBRfT6L188JJiRUKCkyfQfdhyepr3_yvbSaEC5Gq3SzAc4By28rqFdy6Zy3Hn1qFS3PkPqbiUVMiXrA2haS9e7I2U-pPrkiRz0fX2v6q4OMJ0iETF1iGyQnJddF23zjO1rCsO3gCXFGm5P7zUiYhGwzSLPM5F6plKMUOGl0a1mRAiQsFRloLOyv7YmGa-06Zl7-Jq-7Ej2zLYGqYOfdefCzbJb3Sx8e8P611OeRqd3cnaNZG9DmLwxtml2vMJNrhGJW_euPVyqSJb5n6oHD674OIVNimV775gt9_ZHVdzcI_1BlPm9TR7ADiI3nDyoQimeBdEyPg2TjxKOWFew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=l9Jpzex0ibSsoEskYah2FIxqSr9_cMOBBOQBcxjvejEY1Df6wl_5JA-Abdv4BuvPQLu_ICPOpvQH18tP-tErdaA8nPYrVmQfVMPkP3xJWynY7A5zSiYZo39QaJZZdDT77t5TKwDLmxzuWcZ0_Gg9kZX1NXdKVsKDvo3y13sKVXJDH7n3pIP6GQmBy35_Z76e18ErLURlUlPtgjjAkO6weQiqSkhgRFBjiW7HtNR29VdIFqmVNivENrRIz598VMlRBSuS3VUOvuRHgQJZLsrJZrh1aH2B2zPBf57Dv1-mFBhxlMz_R3b9wg66jR5G2jmu35JUS2-_YTVSwvYm-BrzO6YEE3CyHdu0E5b46sGUGAArWcD8Xip3fILQ2GuZVHYd3v6VlxOJVzGMEfSyVIGOuAVy0b4NFDfcCQd_PyMLUq1wobRpJPPX-dY8nbcRPSMtrcT9sXiQppbn1TPLm3m2JHeS-s4FCJcShpPnBn4dMtc76Kg56soLQ9fjilrpDPjkEDJ6TG_QONxIvDehTkPZ_soJeA-veuCDi3-ibG0SxZmD8t3xxOJav-6Y2d9oBFh4Wivk9gyW4z8ScYBc6VCcwj8_n4M_yMYA8imGjeSpuILCP84nS1XCGNVlXIqc2GuzZtCpLgULWCWXgGewwVIkwc8wX58lYqHJaNA8Pcw6cBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=l9Jpzex0ibSsoEskYah2FIxqSr9_cMOBBOQBcxjvejEY1Df6wl_5JA-Abdv4BuvPQLu_ICPOpvQH18tP-tErdaA8nPYrVmQfVMPkP3xJWynY7A5zSiYZo39QaJZZdDT77t5TKwDLmxzuWcZ0_Gg9kZX1NXdKVsKDvo3y13sKVXJDH7n3pIP6GQmBy35_Z76e18ErLURlUlPtgjjAkO6weQiqSkhgRFBjiW7HtNR29VdIFqmVNivENrRIz598VMlRBSuS3VUOvuRHgQJZLsrJZrh1aH2B2zPBf57Dv1-mFBhxlMz_R3b9wg66jR5G2jmu35JUS2-_YTVSwvYm-BrzO6YEE3CyHdu0E5b46sGUGAArWcD8Xip3fILQ2GuZVHYd3v6VlxOJVzGMEfSyVIGOuAVy0b4NFDfcCQd_PyMLUq1wobRpJPPX-dY8nbcRPSMtrcT9sXiQppbn1TPLm3m2JHeS-s4FCJcShpPnBn4dMtc76Kg56soLQ9fjilrpDPjkEDJ6TG_QONxIvDehTkPZ_soJeA-veuCDi3-ibG0SxZmD8t3xxOJav-6Y2d9oBFh4Wivk9gyW4z8ScYBc6VCcwj8_n4M_yMYA8imGjeSpuILCP84nS1XCGNVlXIqc2GuzZtCpLgULWCWXgGewwVIkwc8wX58lYqHJaNA8Pcw6cBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=qbM6pZTAl-cO6AjXP8hXrqWCdUQ9Y92h1uku63iPXAu6-jpXToC2dBex1NrXBJNnPUOPkTvLDWIfx78aT0LS1tFEzRl-WGNvgpRkzQISKlHB0eGiVMvI2ra9-RAHid6eSM_ZaEAiUpDv--56g9fw_G5vFaMbQnAmsOaZW08riQnbmhUnzNy-s3Qb9oHcYeR8Jqw9Sw_HUy6pSl5sAVy_vfPn-X65BYFt8N3gGED5ofO3X6iHvBQqCz5qde9FFs8Xhjo4i7t5gGw3t57Wgvru4aeD8T2iaCti-mj8zHZyrF-VdyTZc1cuRY6HHvHhLj9bXNEo68WulFv914UsZg9N93B4Uf7LayG6S_b7Lp9sWXe84Pf76Ap8OH1Jwed7St71jUWO5n3NbW9ddvJZgJG5ng_20dodapX48kZfUy8zY_GhFq6w9QmZT7LF5kmBDPFoccrNk7zUpdqdcU4GOdQCRV1smM2ut1_lJAZOV2DyGDTYyhgQcMExHnYKB7TsAu85vY9--dgW0epFp3lYrlfmmkDqXJuEAoczzgS0ramFgSrvjkZXzeqvuIkYESvx-kaxp79qBO7PxzOKnqvlsio8Kxo7n-MWeWXVZ3xQh_YDaa2NmNk-0Dflfca_in0oF5it05cbO-Dw6u3p1u4GzJvxGD1h9ppEtWt6r29pyjw4ZMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=qbM6pZTAl-cO6AjXP8hXrqWCdUQ9Y92h1uku63iPXAu6-jpXToC2dBex1NrXBJNnPUOPkTvLDWIfx78aT0LS1tFEzRl-WGNvgpRkzQISKlHB0eGiVMvI2ra9-RAHid6eSM_ZaEAiUpDv--56g9fw_G5vFaMbQnAmsOaZW08riQnbmhUnzNy-s3Qb9oHcYeR8Jqw9Sw_HUy6pSl5sAVy_vfPn-X65BYFt8N3gGED5ofO3X6iHvBQqCz5qde9FFs8Xhjo4i7t5gGw3t57Wgvru4aeD8T2iaCti-mj8zHZyrF-VdyTZc1cuRY6HHvHhLj9bXNEo68WulFv914UsZg9N93B4Uf7LayG6S_b7Lp9sWXe84Pf76Ap8OH1Jwed7St71jUWO5n3NbW9ddvJZgJG5ng_20dodapX48kZfUy8zY_GhFq6w9QmZT7LF5kmBDPFoccrNk7zUpdqdcU4GOdQCRV1smM2ut1_lJAZOV2DyGDTYyhgQcMExHnYKB7TsAu85vY9--dgW0epFp3lYrlfmmkDqXJuEAoczzgS0ramFgSrvjkZXzeqvuIkYESvx-kaxp79qBO7PxzOKnqvlsio8Kxo7n-MWeWXVZ3xQh_YDaa2NmNk-0Dflfca_in0oF5it05cbO-Dw6u3p1u4GzJvxGD1h9ppEtWt6r29pyjw4ZMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=N_wNn6tQNFLfoA4E-qu8ELd3p_e0vN1ZvGLlRB12vciX4FBVkvBHFR4MxYy2NkYW3DYHl5xckzgeEkpVrEiH7g3xAQyl8HjXeSUA8pllw0T7ar4duSG0vLhOPXOirKgNPc9ba2N0uoMWqHtL0YHv4IU2pwJZYGzagu1NrafraOOTKbG6_aa1INHW058oi0W97K4_uoW8yAkwj5oHyfHPdEFRGxj1fEwgViliBq9txcx9LyFUfg0hm2b-Zik1ah2ajsq5h7nySGbTyj3htxrskwm0K_xVcZpwyly9mbhU7V8u5OOg3rONQYNO8mN5nQTsNt0g317J9hC9Dtui2AP3bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=N_wNn6tQNFLfoA4E-qu8ELd3p_e0vN1ZvGLlRB12vciX4FBVkvBHFR4MxYy2NkYW3DYHl5xckzgeEkpVrEiH7g3xAQyl8HjXeSUA8pllw0T7ar4duSG0vLhOPXOirKgNPc9ba2N0uoMWqHtL0YHv4IU2pwJZYGzagu1NrafraOOTKbG6_aa1INHW058oi0W97K4_uoW8yAkwj5oHyfHPdEFRGxj1fEwgViliBq9txcx9LyFUfg0hm2b-Zik1ah2ajsq5h7nySGbTyj3htxrskwm0K_xVcZpwyly9mbhU7V8u5OOg3rONQYNO8mN5nQTsNt0g317J9hC9Dtui2AP3bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pun0EFVDAd__8Io9e37t6NkZgBFm3F5L5w3ZQfhgELtBjs-4ZIdOgtpiMXQkHJ41oR1zoP9Pvv56c7e3gUXRZaddJ0G83TeCmMdH39Uvqt8Z0R2ukPiPGBxC9BtMMdGryWk8Qc9XcUl2Z6ZGXF8hwrsCALHw1LC2WgGBPNB9aoj453AlaUH4dJo2Uqsw26gLBIiv4Bipi_wcUEH-F8ZQaKN84-8eGaKiFXpkz6t_UhvZ_5e_ERWs0lEeo5gIHpbGQ2xjD3cRtqFnOza8Tyi2YIsgXtrNF66TUmNgVtYzCy0HsYyFurdjYE51SR11-TefssK4n8J5YkOPhBtkCuEU5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Tsro9dmrUZl0oO0Sf1QyHZdoJT6dkK8fdtpF2rypCchi4qrYHKKnb0Ltt8aN_JxCgs0RiJL03bAqwEbJAUlh_QQdog844kXuMQfP0-1J-IOdu43jhJDxUUYswMy7fYyqgcNrU6mV-h9Z_Bhong5vk9Py-gtNr1Bs6Exx2YZzqKo-yENRIc0eYDyMs5LgDg0XdI0WsOxCUqt0Rk5BXEYlWPymn45ajBhEoRvoCl-x6MAX-7V_OYnCM96G4ZethI3UCb8gs76Yy0XRVTdlId_dMXzvyGHcULcXeADRbPyPa6uYZBWtlfOl-h0GNdt_ZOePmry6rdf6fN33fFAX9Mg_tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Tsro9dmrUZl0oO0Sf1QyHZdoJT6dkK8fdtpF2rypCchi4qrYHKKnb0Ltt8aN_JxCgs0RiJL03bAqwEbJAUlh_QQdog844kXuMQfP0-1J-IOdu43jhJDxUUYswMy7fYyqgcNrU6mV-h9Z_Bhong5vk9Py-gtNr1Bs6Exx2YZzqKo-yENRIc0eYDyMs5LgDg0XdI0WsOxCUqt0Rk5BXEYlWPymn45ajBhEoRvoCl-x6MAX-7V_OYnCM96G4ZethI3UCb8gs76Yy0XRVTdlId_dMXzvyGHcULcXeADRbPyPa6uYZBWtlfOl-h0GNdt_ZOePmry6rdf6fN33fFAX9Mg_tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=kPTfPFXOXPehvNoUddeHXbIPMamads9iuZYLjNkcM-ADgEDDr_ZXU3QITiTn5SJQTkqW-UatlxcFDkO4fXB_GL-Axh5WgiXyp_VCLlYLlDK_y6y7oelVbDVyM0bkpJlZ5pmSjpUyxt0GXUzk4UFZwCdVAfrK7QLUOBkEvHWEKx4Fuc3UXc4Em_KkaGnZmy0JkWaoFwka3T8Zwm2ICyxBkcW0kKhNI8fN9OZGiZv56ETgi2l3qmguoO4DoxvuiVU4H0EsbKSkbScCl1hbGcIbGDJn03XX6D9XGCoe0p-PsGt10XMBLmoFQ6x8Mp83MG1nLSLPCWE_x6an1Rs4nVCXVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=kPTfPFXOXPehvNoUddeHXbIPMamads9iuZYLjNkcM-ADgEDDr_ZXU3QITiTn5SJQTkqW-UatlxcFDkO4fXB_GL-Axh5WgiXyp_VCLlYLlDK_y6y7oelVbDVyM0bkpJlZ5pmSjpUyxt0GXUzk4UFZwCdVAfrK7QLUOBkEvHWEKx4Fuc3UXc4Em_KkaGnZmy0JkWaoFwka3T8Zwm2ICyxBkcW0kKhNI8fN9OZGiZv56ETgi2l3qmguoO4DoxvuiVU4H0EsbKSkbScCl1hbGcIbGDJn03XX6D9XGCoe0p-PsGt10XMBLmoFQ6x8Mp83MG1nLSLPCWE_x6an1Rs4nVCXVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jvnu9qgerzEtyWSyhOt-5sIylPKRigRwbuTVY3w18Mb4k6W5sQD9uejE8NrCsz31qna3nTSmm6k57iEm8KMbL3driGa5AzXdGWG0KaaOCSAJi0zfBQiZ63dm6u9rOfUE6WjipNZrmjjzy8_6eeWkN-T72APSp5tRd0D3v_AfGLvqbc27GL7ppQwiNlwRGNomYpnR0Jx1AshGqO0H6qqQJ8pkBbUaxqCLd-LWn8acZRxHxnt6geYIRljlGFX9Ik6Wp5n2eACJS5kyypP2IWqylEAnu0G2JiJopodiCXoGmZ6G5ioE9ig4wZmZxe6EgL2s6BYCKJy4tFy2hyhmn_OXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdJGGp5ayoMwh1W1xi4ib8tn-aFvpM4-IESZ9eSfFlOYw4PtmQnRPx7mjJ-K-nnJN1k10QTcjEesMDOkw4vZ9RooHnb7Gjm7cjcIpoNc8tesR9uTrL80LOU3iykB12Olm8D3x0V0x2GnhkIl29ONcq1osxzdmpjb9S6z25cfrAiz157Fk6oZYXiSteBc7zbOhdrIrSds8ArpG78fXaA8M909HeUcqVVQZPWi7b7OUtM4ygtbog2DdKufP3ajpE2huEPg9LHOsSOZGDk74uEx0p1zd4I3aiLG2HJuzR5g6paCZ1XhcVbjNTz--UMj1WbkKlAcY8M0Tm6SWC2qips0ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUhxBH2m92Cr3tDgKNpgwUr1_M6fk6UjC_i5d3ae5q-j6bC0ekZay2FULE2yn8P9S89TgYGLV6AJyA9x-Nad5nrf6yB7e7wC23S5W0jv2BKKGwXRfrGuzmy5B8EBb-2vAJ3BkNHg8Srr1RYwKaRjmHxJZgVadnB89MdSnrqL3LkGUqikCuIY0-QKAu4MmmdlnQV74UOtQNyP1TCO-tkbbvfBpNgz3oeQf1f4PiPIdlqKGdq6rOZ7DY7lZa0LbJooy_C8KQNdWrmSjmB8mv0dVWFe0qJQ8PlcPVVK-ToVfCNlky0NyuaD2bKisjxH_D7kmDuhvtHxDYnnmuOSgvS_Uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgmusY3ctNir7z39SRQHB8a7rnOGYMm_gknMn6s5O1__HWcfJ4riSb9aJ9_4uiZ7RLs5_CRy8V2cYFMpQMnexB2Bc09UanfkJX5uAbM5RFM5ARgO76tLnlfDEZIWNJ3CqhNoFb8PeNbqv4hFDckk9dgUqvQuu_si2jcVEXKam2-f5Kesl77TV927PWfiq_BduBgNQkSWgzCxXbJAe3Vj6zhz1n8hPUsndRHh-38yePXBYgfhWy68OZK-fSnGPliB88khp7PKyq8pej2RfcA9zHOCs3DCickKJgzDWSzj2QGiLuq54jUCPhmQkJGgXThzUXpZgcjLliNT8QO9R1V4xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_l3V_N5BTGEp6IQekXjQ4eTFMWGKRbgRI8G7RhSN8SvrJIxOgl83HzhKeg4n_8i-ZjFD8kaoOL33afePTDqIn2KNCOFE6PhXD-wcYORbkkE-aikSQfxKirt1nChZ8xqDLnkhKCcDXEEPLJVI0OIj3M16kkOkpSat8tWC9LJWwfHP2uphAp_qb6uwE4Ns85JyY8koA3uMluP2v45KXIR8OozPdjOoKrmcTRPIumBST8labeAOOnJjWMdRSwOiR3J3tZ8dz5DJf4RiTCzVatqxReAj5ILl_qT3McQ5uUYNP7nnzgXUYyJX6HBOq01vC_zilPIIgCFMiglkZkL3BqraA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IW9JtjXRK9tpIFtL_0gwO9zSfXrvwWG7gQIjCH0voWNASGa9kK1QujmdlVvbJetOO6KJHdCUrVClPuHPnMMD4jixvY47bCc0BZUn7WBdrg3Qy6EUFL84cu7Cna5cHT9gB7uI8e_9QQn4uRZcb2VCIt2X1i0AUApUjMqiGgy8SVAExYAmvCNIfsGtAA4PvCTs11BNEOnvBlkbK0X860h12aBK0k0DT_Glxy5FJ_Ovb1umBGoFgEn_NPMi97MgkvT-S3hEKZviQNxJ6YAS2ZTryReQ3HF_o7Su7r-WcjTHgVJLcymfyS8zXvHqCxehCodiFg21mperuGL8UHYkzdiJCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQ3UsJpkqduEzeTm647beM6X2GjJMFY2TVFqXM-d_sLv1M1dDmQdS0eQQUjBJBZgAEClb5r1Vb-wye03z3wWlDWUfkW2xGcndE5dLSU187h16VypTQD5F29GSII-OB9jYr_cboysy2OSfWesl2lADT5dnFUWLwzJnmKSYJYYA_7Lh6Tx7QyCp4OQ677RPfRnqCmvSeXsvSnpHaOdRspS0_LTLHav9oCJzOuicTxjqoqh0CSpHgv10M15ibQYIztv_3zGCvFvOMSz6bq8fuVvyg4Q1SUwGt1IFFjGslLnXCmzkno6qdeKnC4JuFqPvTSAk93M-ZKBk1B9JzObpfxBtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDPaclmFficsQa2f0lP-pTwJNaWeOyUEa8o2Zrxk8LcmtNrog6KUlKEecpLdhhys5HV2pijvyEdk_IxSrNzgnB6OreDj1EiT9lWRrzr-95qf7MG_JuFnbLxgM_cosFIoiYGbiO1BEpxnDlqFaNJqrPl6vc6IRQm5Go7dzuowvyUgxhvxR0GMkoWbZjxQiKKsO-ae8HKO_HjPg52Egk7LWHeUozAihHvgs56-VD_jBloPFOzQd2-05e81b1PCmiJN_re-ltbRW7ETl0YNVstehNMOb2XrSWBzhizjw4Rma2gzSaTz2TJWX_RcUr8Vq_tfiE6GQU6zo-r2dW5Om2KP1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mbQeyDLWkTZFqFUMIsvRTTrurX02dNf9js0wyIcvBh0KuDkSz8lJcNPWgA9nZUORhnIvxWq_zy2n-cTPvzzJ8PCr9lFIKSqyA3NAAW1x7dtafJBxNHUhk3UfVAIycg80nf3stV5gPNNClqR1nuaPMtYzEJXmGNE3gWwIxBLO9Fb3_L4YAz2ne7aMnZawBAM1fX4ghXvQ2Tc_aSTNIF_6M2ix4wHEtIO98oV0PPslMRxWBW_0yfgL7Ik-7VvZFXK7OwtLinBLhzLYTjWWZzq2r0jxslyVDs8Sx5TSAJ_GFsrCWwDCMK93L3hC5I_pbVapIRGmYOf55kR2ALf4DQO3Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mfLkAQoF-xMJuprbFoP3ZBgKk3XXy4EGP7G-rjZAyqeJ_TuBzGgyG0j4nfxA1dACIi9z5kRg3QRPfq7BnnOJcf1eGpJLvPS1t3HgVAX0Q8DHj10KCQJih0PtYm0LgeyNIynHb59TcOFnG5ZoIwAq9tSjd3TWHnnMnuQ8WJdA74gSO1lAoi7tgy9mD_kADxhJhPSBpDsr5db4f8ucmhWSxX3jFlz3kXvX9-nrhXD2A2cheU1P--12xqNdqKIrzuR9IgxmUR3rrfYmJleu_hPpBtya41oAi8silwWz8n7wAxe_0-JdT0_YsEqXYu6NntTGTDaQjQkrevfCC1OFaTWQKA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=FeGdskJu-ALhoX6ABGakbV1wTWuiQ80SzikwaFT0_Tm4re5hhxf7dsouje_dosaoC8jAy_QHcwpTCk5xjonruNG7leVZkbzH_QMxueoKrlmIIDf4nOWUnkx3dqyRF-YioFUBNjJmPowEOFlt3vy3IuwVYRJpvIHhe42hCv34yul9RdmBOzvSdiH7SZVBktTbMgBA0C_OHrm316YEucHjPJZd6-sIq6ZewkodTEU06coa5AznS29sn_poVyBfzjXTtD1LGiB0OfTua4DO7PkVh_K6S4ryx1j4QD6uMJW8Bp-RHZnEo6KpEmUUHX73kdimwKXjodoLZoTv3u41dWkVwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=FeGdskJu-ALhoX6ABGakbV1wTWuiQ80SzikwaFT0_Tm4re5hhxf7dsouje_dosaoC8jAy_QHcwpTCk5xjonruNG7leVZkbzH_QMxueoKrlmIIDf4nOWUnkx3dqyRF-YioFUBNjJmPowEOFlt3vy3IuwVYRJpvIHhe42hCv34yul9RdmBOzvSdiH7SZVBktTbMgBA0C_OHrm316YEucHjPJZd6-sIq6ZewkodTEU06coa5AznS29sn_poVyBfzjXTtD1LGiB0OfTua4DO7PkVh_K6S4ryx1j4QD6uMJW8Bp-RHZnEo6KpEmUUHX73kdimwKXjodoLZoTv3u41dWkVwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEq3SxvfXCujl_fA9nrmIuDbcUsv_U3U6uzQIpxoOENohljQMhHCssedkU5c-MfnvrNtxu_S86R_db56izJsAKswfjsDkwffb1-gkiQLpctnfK9A2vwVLm1nDHVI5LZ5c-jSsVr0reokzzJGlW4VkjsFQpTm8Wo7jDPrg5ZH06o_zMlHb0f_I_H3q4EyQaCAxaBJqNFdxesgIZpMKw5BlRmCTwcrvQ8vzjHZ5CKnV683jNjRh3yGbGUuU1dP68qd-Ssat6LNCPmhs_mrYL501eI2nWlXaR41GKDADPVtxJfJE-Jswml0Nj1QOL8dM4rh89ICzS2fNlHYmzfMLoF1mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYLDE4DFKalBw2y8s0Kq_GseK6wqNhHfWnS0efh_tX8IiCCoRAtaCi7ho0_Oqdj7ypDM_XGNp3CLfwyCTxtlf8wHfzpQm3IArux-kGMVanQIdE6Q4NIaNmFBiZvwpVRsucNh5e515ncFQMDWcTvMX6CRmVstCy5gwmF66trxyW_n2_Hashp-vBrND7Byy1mFpaCHzmeWq9AxwTq1-UGridU9-Ou8D6MxdE1bhvcSXn0xgcUY7tLGUV-h9hesOnZtnS9fdhXVer-Kurf1QjlALYo_MQjm8g-SQIMk1GqXh6Ut7-C6KiA9fvHfq1D-dP4u2JYt2GUZGJaHWAVRRQ-YuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=M_f6_BaSkWHh5l6p09_OV3LmscHn_rD9GUCCZ63kj43yD2RxDcsZE9p1HTDa06cFGkeN-m6eFS_rI4_hvnGTdl0J1drF-cIUL71kZtlh-PEv-odos4GeY8cnclW_DeX6TRczvw0FI8KkputBc-LX_6sq6DPdYtuRyh5Aql9mTam7viLPDASEB0ReZAmq7yzfsqoQ_fqhPElxAhOX25LQm1e8QQ-7kxoqyAmMhUC_9XVAGnN9iDl-1LVgUdj4VfzzCuGH1nOj0fzbxNCVr93K9fmBwd8VW7OFWkAgp2_8jI0sz4PdSeNHSNqggNHLsi395Z2YZLvMXs2aXXFD7a75ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=M_f6_BaSkWHh5l6p09_OV3LmscHn_rD9GUCCZ63kj43yD2RxDcsZE9p1HTDa06cFGkeN-m6eFS_rI4_hvnGTdl0J1drF-cIUL71kZtlh-PEv-odos4GeY8cnclW_DeX6TRczvw0FI8KkputBc-LX_6sq6DPdYtuRyh5Aql9mTam7viLPDASEB0ReZAmq7yzfsqoQ_fqhPElxAhOX25LQm1e8QQ-7kxoqyAmMhUC_9XVAGnN9iDl-1LVgUdj4VfzzCuGH1nOj0fzbxNCVr93K9fmBwd8VW7OFWkAgp2_8jI0sz4PdSeNHSNqggNHLsi395Z2YZLvMXs2aXXFD7a75ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=mOF83kVh32XikwC5ZEDFIiHBXIBEMi6WkNKrLQy_aX99XRZAJDUv2kgIj400icWT95atZkvzFo66AOZwzZAfFLNvuW6K-ZJ1-Xu2FaiNXaOWcFEKtTcdAwtFlq_K_aGDcFnwlKjGcLJYIHiDp4vxc4TA2kE8MP9GtzBZPsWyXKPGh0Yp9BKqdZ4H8QwwXouczk61yBVYqGozc27MDYCLT_29sFWlkIcvflMBgkwZGuXJYLbKfpRr6bs_yvBlek6YKWppnNfcfyxjoLPXD5UAvBJNesZp4kA1_9Cbt-T0KU-D40-be4A7bykq3CaXEVdjNoDfXYdyCXreClWtWtUHpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=mOF83kVh32XikwC5ZEDFIiHBXIBEMi6WkNKrLQy_aX99XRZAJDUv2kgIj400icWT95atZkvzFo66AOZwzZAfFLNvuW6K-ZJ1-Xu2FaiNXaOWcFEKtTcdAwtFlq_K_aGDcFnwlKjGcLJYIHiDp4vxc4TA2kE8MP9GtzBZPsWyXKPGh0Yp9BKqdZ4H8QwwXouczk61yBVYqGozc27MDYCLT_29sFWlkIcvflMBgkwZGuXJYLbKfpRr6bs_yvBlek6YKWppnNfcfyxjoLPXD5UAvBJNesZp4kA1_9Cbt-T0KU-D40-be4A7bykq3CaXEVdjNoDfXYdyCXreClWtWtUHpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3ozXZLZq0WfFMKTYt9Yr4PrCiCUV1c_vO076E8nPjpLea2Kr8bY0tznBx6Q79DuUQVUBKz5HNsHYCtA9eHZS_2NDPpwhludJDpkThjx5UZd4x_R3KuUtPjMNarcZfhRPwyEsT-Gru_2XyRCA3TBbtNWpPXv0LsbRIInl4ZlQpuvHAITa8rzuYAbFbBbq-XzrrmyOqojsng9S3hebFpznyl3X_QpGo7RF4funSQNE0bx7asZayFcVd5-ulZ_EEjD5a-m4-XIJeyWrCSPR93tEwHuaEey4aCGejL_-pwq-qjEVhZVXxcsLJWxm80eUjuBPPjqJEULqoxys3DOme9MGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQ8nnUyHBKLzh_jgOnvk3uw3R6Qcj4Qq9UaUGCdQAfwLRLxoBYmX_NMTAQ9rWf8vS-epdzgG6RaqJWDQW1uNDOiCUuas0EgvW3QY51GTpi_EchcWQAtbuKwYa2_OSq9OfNiyp0MRXrnpRKyM8yCRtKUaV__GXNY7LvjfnH9hiexYYjQsUJdm94aqn82EnzyMvUHnz6aM7jZHiB9iNfskbjlbIlMXMUPoF5jn0J6iis_-VrtS5VrUSOq5XOpsH9zUhfo9GIhlxMuhexhGLYQaJz1USax3ahKtaHv73Kj0DrLwrWksbcFqdUATpHz1NnDWU4TjQXXEPjYv3Ow8Qog4sA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJHPee-zvdsmsy4zcuPDyW96UbG42UwOcO32IA6VK9TIVJLa_MQWsiMYpz1vb3WtFB804da9ECJCesq_3wKrvrj2gqKRXBSo6YuQHNPAYZ2vILmy3Jqy8C_aOLRz01E2HvnU0uPighp6ReL7QbAihE1H-cHKvkuBEtiYRvxJrxiYaYa7R-qtvjZFu-zsMKuMIgUiRVjZ86MxpphZmrU8f9tAoR_H6f5V_X-ncEbF2GFD-mGMWQ5lhkAf2mO5Pwb3ivscm1abWwo9vf7jaLI5xg-OHbUjQcUVOKrUTnUY0NxWCmqNjVCH6i9HSm1y0jI_vquSBgL-XPbVH-b_w2PT6A.jpg" alt="photo" loading="lazy"/></div>
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
