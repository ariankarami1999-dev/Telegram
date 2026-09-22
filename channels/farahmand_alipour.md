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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 18:34:28</div>
<hr>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOPBe-WsSyKP9b8iFJXu_j5PR_0lIEe2k50pJqHmxjEnlwZ0j94YJGCBG2XZ_m1-E5lIzS-uCEoSAwIqZByjdAtrURxa4361C-j0MHwVOYXc5RHqG5rGl7Nqk58cUP7HiiAmnhLXXhu7jS1wv0McnVMu37vavKH4-rLNI7Y8D81vO04kCcgI_JAejI2Mi2CdGfcTRRRsID6hnDCdvP19ub6N56KEtCwDrDAoeceEfqjYB_EF3YKLkB-FZW5OlDzcmSRzlOveJDK5k_fi52cSTkfDG5YrnnSg0LgXDVg9XtIxKe6YOuSHD_9JrBKpkIrDglDkCtl6QczjuIODYlnyIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHX55iI1BW81CKqZcPQdfvzGIWvggqSmU1nk8jeRoAUMzYhE-5I2VOOA1GdJboNet7osvVQAMU8CRVh2-FALND1Kj40Gj4HmQnmz7d1GEJhoyivyTjT4hCOzwFO80UOlf827nJwtFPk4Jw35-7Vpcx7MKoGvsicib76ISJ_WmEd9RFu7bjr-9b97TphtKgt454P-HL6fYokpBvwo3hD5mzVoBJUcEScCaySZVkjgwYdgYKjbE622wtMJkZxebVsikUKWuW6sQLpa5vj_DEFB8OoHd6YUdY49b722YpiGC80j5LyUYJSOU0i_dUo3L9yej4CCNDtRsr46gYvIgPFszw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmGYFcw9RaxkLeQGdNG3fKATIesq5DCXurXTquc-iZX8cjL5_VEjDiettKKBpkVZ4ZBKlN7P8a8Qkgp2ClqC2ZuFDJv65BWxKkBDaTb2H03XJTXDrfzW1TTG4mXTIQ1OMTthjcMl9wR_JHQaajYFaKnvXBRrpFnIrX2Unu_LJS2ORWXNRGAeuSVKwu665BeyrfKSnWD-tBgHiE1G_siFIjnpkXztaR650vSP_zi40LFhgkWUHXADoM23lbUsfj5VFHyoJlhoukAZhFKQbCBrCKS5APvsPcAyJDagkOvdGo86ntt4AJ7icJZbqRH96cWnv0JuxPKGQWEwK2e_0Nvckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpPkCi6Ga6SfV9mV-B0SEhrqF7smrHQFD7yi4g3ZOzp-4RikBbytVBQhgN4FR1GuXdNe-mFmFrX23I7-WpO2f3ybCoqIbtCUZs_iO2bNXN0hQLmvC1EZXXGHUk8A9ICnBhE8A3ff-X5wOxB1UnlKj6hQk71sVef_uMUncTQoxX_c2rDaiUA0Z1QR0pOY7U0sZzusfirDrL8u1tusufh4m0jYtsd3YsNo-Hy0nT76WP8LQObMz7iq1y84_GSsULrWR4YTeZQoYvAsi6RQegBXcNtk3aNXFoz8D_V8kfejZ4sKlzJxIkpMuicFePryabqD40PmEMZkpGP3l1uYojbIpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCYnw5nC6iOqeL1-bE3P6_QkgoDFqK-km6_FX6iTuyWNfvy3hFc8_SmRATthCWsIQeBiR6rnAeGHMwju_pK1bDmo9HvYC9KhqC4FLdp5FT53vKHOliaTSUEqjYYbINt-quEWCc69x1BIDWnMKwg3DPDiAeWMqp4lda1U2tzo3MjrGkjeWDBGJaX6CIC8mvVlRmx1ctJaCgpd71a4gfnrUK2KfkwsWmBAJ1rxQOCmpsJ8Ux-KRHISc-rrqIr5okhoHRBLOn5pJEyquFn8QUMFnEXc0IrAfHC6vOCyKKx2ron1aiQqCAz81wYSOR-tDhIr2FR0-dT6SDtzzfrxpeHUdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFKumJh0jtPD5hI7214SmXhA5LqaHQQIhuoQJu4Qi2VFXgbvPizUzVf81cBSgCweoPBrMk4gIlM6J0pd9JmJ5Akc0OOXoeWSnAx5wlisMPiGlj1TYVjWuGvsYrtN5cfFjY7bSctJy3IquUfiXEKntgAo-7uX6fo12UMuPUE6cjKYQsnHoRLpVW1JoJi1bk4YBOFEMBAjfpVidccrkzpIcH96KCNJP1HCNGdi0cpCPfbUBwj7c3mT7XIG8XeXxkRGX22hdfU3BQCawb5Qn_RT3Cfy3P0pDh6Vhwlf282137zUbn4my7KbQ_LE4lIS8q5_tPLaOKgS5P5jx9Lo517tjRNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFKumJh0jtPD5hI7214SmXhA5LqaHQQIhuoQJu4Qi2VFXgbvPizUzVf81cBSgCweoPBrMk4gIlM6J0pd9JmJ5Akc0OOXoeWSnAx5wlisMPiGlj1TYVjWuGvsYrtN5cfFjY7bSctJy3IquUfiXEKntgAo-7uX6fo12UMuPUE6cjKYQsnHoRLpVW1JoJi1bk4YBOFEMBAjfpVidccrkzpIcH96KCNJP1HCNGdi0cpCPfbUBwj7c3mT7XIG8XeXxkRGX22hdfU3BQCawb5Qn_RT3Cfy3P0pDh6Vhwlf282137zUbn4my7KbQ_LE4lIS8q5_tPLaOKgS5P5jx9Lo517tjRNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Yl6kGiMke0lE1k1azQN_gHwEF5AqeUAmS_MgobUhre1wgUde3htjfwZrKF7Ccxsb8tGmg0WJC7rav9s681iGHbMcD_lXbrLRZIUFMlrPf9KqPUdzg_R9BuURBhaiZA6sthZudX-XC0hP3_vE_aziW1wIRjetmSITbLG9VcW6MlxEy-2SsKWrkgsvsCD7FGzksg-uJUl2DKXkSZpGnNIAVXKPEQ3rqHxhi--1SINkae0gnsOmEpeGS3jSygbiFdsffltgosnkhh-5TvCsPAfwHM9TzLGa8PuaZ508pW5HTzjuxw0mMUdieGIQwoYqVpq8cqsxhsCB6sOp9__QfZmUcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Yl6kGiMke0lE1k1azQN_gHwEF5AqeUAmS_MgobUhre1wgUde3htjfwZrKF7Ccxsb8tGmg0WJC7rav9s681iGHbMcD_lXbrLRZIUFMlrPf9KqPUdzg_R9BuURBhaiZA6sthZudX-XC0hP3_vE_aziW1wIRjetmSITbLG9VcW6MlxEy-2SsKWrkgsvsCD7FGzksg-uJUl2DKXkSZpGnNIAVXKPEQ3rqHxhi--1SINkae0gnsOmEpeGS3jSygbiFdsffltgosnkhh-5TvCsPAfwHM9TzLGa8PuaZ508pW5HTzjuxw0mMUdieGIQwoYqVpq8cqsxhsCB6sOp9__QfZmUcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=d5c93_5KQQ7jThPK0FOfdIqxlGXnbb2MoE9vquFNbG99okYFfDFZaXBAUa0kxeSg9eklXfMhw5F-jjfgkBzikbRpuoZOu86pUGFyUKknInGZkajrdEDtDjc6ptU5zb-hqK5uTakFaghpfJIPITL2ojcvJ1uz1Mj7o_ruyzznRbrwNx77Pj4cVa9C-Iwnm4PT6RHg7UDb34NnqsLqU32VrxrBtJqvtvDTmjZ3d3q5j3CN0TF8cKrnyiJ7dnVws2QZb5V66mqKKC55P2_4v_PIQ1crqDq_XIMy5OyFUsiAC3_4kbrVL1k11x5h__HKSUE6aygABeC8kQrHFK2aTtBP8iFSmpt6m6WfGA1rlqumcwuGi8mwFLvUHTPtT6iPLdkqxdQxYoEVCn3EAVpCUT39nVQChPNjJlAXNnngmwzPxxHKblObJuT7d5mzrRrKaFhaFPOeMi10-0CQkb2McX1n7aPrILzXVSIKXqu8vz5UqfNdD48g2sWd8m8HUjypNlm6a-08o3UVxZooigZtocgO3pKv7jD3c4UiS2Te8Us6k7RXIHHbMjXgrj9hmyZwNrDYS57mwe3p71mXZw67R9Popl-1pQzMiMMvxzvQcPzEIIqdqgLdFkDl0bGkyLgTtAM5pzPP5LITSFJRywSYa7WBxkVYj-Nw5BAJHbmlDAZzCd8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=d5c93_5KQQ7jThPK0FOfdIqxlGXnbb2MoE9vquFNbG99okYFfDFZaXBAUa0kxeSg9eklXfMhw5F-jjfgkBzikbRpuoZOu86pUGFyUKknInGZkajrdEDtDjc6ptU5zb-hqK5uTakFaghpfJIPITL2ojcvJ1uz1Mj7o_ruyzznRbrwNx77Pj4cVa9C-Iwnm4PT6RHg7UDb34NnqsLqU32VrxrBtJqvtvDTmjZ3d3q5j3CN0TF8cKrnyiJ7dnVws2QZb5V66mqKKC55P2_4v_PIQ1crqDq_XIMy5OyFUsiAC3_4kbrVL1k11x5h__HKSUE6aygABeC8kQrHFK2aTtBP8iFSmpt6m6WfGA1rlqumcwuGi8mwFLvUHTPtT6iPLdkqxdQxYoEVCn3EAVpCUT39nVQChPNjJlAXNnngmwzPxxHKblObJuT7d5mzrRrKaFhaFPOeMi10-0CQkb2McX1n7aPrILzXVSIKXqu8vz5UqfNdD48g2sWd8m8HUjypNlm6a-08o3UVxZooigZtocgO3pKv7jD3c4UiS2Te8Us6k7RXIHHbMjXgrj9hmyZwNrDYS57mwe3p71mXZw67R9Popl-1pQzMiMMvxzvQcPzEIIqdqgLdFkDl0bGkyLgTtAM5pzPP5LITSFJRywSYa7WBxkVYj-Nw5BAJHbmlDAZzCd8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=IDWJs8boJAC4iihSkPgBRnOjvKOwK7Kgj5XNfdbuMkXVg-_QFMdCOJlbn1248uKoVyFc_WdTfpy4d1MgambjT4lDyVv6GXIdKdcTLFAK9mXyhF8SuZm121HOvT2oCFO1PPvNF4azhn5NH0mGg2nGYVocd-T1eQ7Z9RNdqXEWC0Aezhpdss9J7V1e2iTr1AMMGXt7s0ndPym_ybtpOLzvf0aaAwYG1nRY96CA9LOEQiP3lxCTIyPr8oNt7UMm-oNvGQeb9YQ8vNS1lRpyIXeUIHeh-X7cHR29pDT5a1lSKell4BxYNenwqeU0Uj_YKfNzaIt8gy42efNWd1Uc-FrYig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=IDWJs8boJAC4iihSkPgBRnOjvKOwK7Kgj5XNfdbuMkXVg-_QFMdCOJlbn1248uKoVyFc_WdTfpy4d1MgambjT4lDyVv6GXIdKdcTLFAK9mXyhF8SuZm121HOvT2oCFO1PPvNF4azhn5NH0mGg2nGYVocd-T1eQ7Z9RNdqXEWC0Aezhpdss9J7V1e2iTr1AMMGXt7s0ndPym_ybtpOLzvf0aaAwYG1nRY96CA9LOEQiP3lxCTIyPr8oNt7UMm-oNvGQeb9YQ8vNS1lRpyIXeUIHeh-X7cHR29pDT5a1lSKell4BxYNenwqeU0Uj_YKfNzaIt8gy42efNWd1Uc-FrYig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLUCHCmzmmhxmdjD0Tven0QzfHKoNZ6CcGgem1tsJVs9ZvM66nVbGzxRV6i5K3W8YGvCYrhbmFXpXXs41kEpljjfewHBMbbREyDH0T-ed7tz79bMlCf7_gu3wu1fyTz-cYOPFbGeElr4-dshxWZZocq-jIFDTAa1U3_L3s8xplWCANV30MzXMbut7BC2HVHW5tbdqugZBlSXOBUmPlhKkSX0PRutMk-Uo_kafnaKe7g4AQBhSk8wfyVdFa7bsIywUICmIe5KkRSZvBMstEGpP_aJlZFcaIxNE_JQnkgOeZOXE3ii69Vs_0Wqgctd6_J88SEY0_M8o0_oCzjuPeT_ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=CWmW9BM3S714RAAIjgYczVOr8Df6Wm7Mov4Xi-cfsTItqbihPd8hUVQl2ifSyBD4Cn-pwgy8JKafFGo3M4E4i1v-nXV8r6K_uaA2c4z3NplCGCrj8f-tw6bMUm07vQSrg3SBuC_Nu18fnTjXqahabBMwCpLvGWVMWs6OFaeETbaEZNmDOyByTXGWH-wWK2q92fmroJ08aJLatmuz3BA7zB5Nfd5Ju4vLelFQLvNM86Y5o0PyzFsDPs-xyimAkcYTfdlcfeuNwbED3j92XdpIagHA3oEYBdGKeWKXNImJ9PCG48FQiUJ_elgCn1BZtgu8_cfazFsNt9r1SMLnQj0x0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=CWmW9BM3S714RAAIjgYczVOr8Df6Wm7Mov4Xi-cfsTItqbihPd8hUVQl2ifSyBD4Cn-pwgy8JKafFGo3M4E4i1v-nXV8r6K_uaA2c4z3NplCGCrj8f-tw6bMUm07vQSrg3SBuC_Nu18fnTjXqahabBMwCpLvGWVMWs6OFaeETbaEZNmDOyByTXGWH-wWK2q92fmroJ08aJLatmuz3BA7zB5Nfd5Ju4vLelFQLvNM86Y5o0PyzFsDPs-xyimAkcYTfdlcfeuNwbED3j92XdpIagHA3oEYBdGKeWKXNImJ9PCG48FQiUJ_elgCn1BZtgu8_cfazFsNt9r1SMLnQj0x0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=l8IHqV927rb51ctCVDmMMXYjY_TUidV0j76qC6F3lEKgMwuNAUHQV8lv9SG03NxeJcMsMuTv0hqwiAUAwBt_qkSEPAe-HIN6AkNF0KJY4xlRcAhGwcN5icqF9ZuNxt6rFDPhvi1WGHNl_vt5sm_kmvMR6bAvzDEgCjB6fKM9KghaHSWNGSg6L3WxKi_5sT2ZcblBHHyp8DqO-GUoHVk0RTZhtHDB6_VmCVJPEvSf1mq9fPbOjd7_k0JLTlYOkk1oQbnDzupfvURWNVpf6AYQdiIQ2xLsLuuJljb3o-h7ijmn--W6TUsJFtnQJ8ufX_yXnkeHG2Z3_qiz-OVOl8i0hje26zZLix1ZwuiGd7favjxHKlmLCGnh9U3XYtygkKtaA7jXiBsYDga0T6rqCiraI679KOw5jua1QWc4A2neuuS8b_GAJhPJ6c8pw-BKt4bxwOWxh0bz2CgVwUE72SO1N8X03stjSryrX3diiDI5uK7tiEAjyHp6LxVY2Ru95fnz5LDcmxzJtEu9qVUI_VSo7BAhesCnE5cFknAkYSpOKmWBb4ThwFHVTifZvNOSZf-WFJZi_sepeB61Q8CQ5MatJITBbdD5GOdNIiD1kwNzwUrhoDl7AG-a0JFuOsRLRLJ9-U-19K5SZkhSyRfNyTbFXIdEuwqM6Wk23zQppzq3fHE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=l8IHqV927rb51ctCVDmMMXYjY_TUidV0j76qC6F3lEKgMwuNAUHQV8lv9SG03NxeJcMsMuTv0hqwiAUAwBt_qkSEPAe-HIN6AkNF0KJY4xlRcAhGwcN5icqF9ZuNxt6rFDPhvi1WGHNl_vt5sm_kmvMR6bAvzDEgCjB6fKM9KghaHSWNGSg6L3WxKi_5sT2ZcblBHHyp8DqO-GUoHVk0RTZhtHDB6_VmCVJPEvSf1mq9fPbOjd7_k0JLTlYOkk1oQbnDzupfvURWNVpf6AYQdiIQ2xLsLuuJljb3o-h7ijmn--W6TUsJFtnQJ8ufX_yXnkeHG2Z3_qiz-OVOl8i0hje26zZLix1ZwuiGd7favjxHKlmLCGnh9U3XYtygkKtaA7jXiBsYDga0T6rqCiraI679KOw5jua1QWc4A2neuuS8b_GAJhPJ6c8pw-BKt4bxwOWxh0bz2CgVwUE72SO1N8X03stjSryrX3diiDI5uK7tiEAjyHp6LxVY2Ru95fnz5LDcmxzJtEu9qVUI_VSo7BAhesCnE5cFknAkYSpOKmWBb4ThwFHVTifZvNOSZf-WFJZi_sepeB61Q8CQ5MatJITBbdD5GOdNIiD1kwNzwUrhoDl7AG-a0JFuOsRLRLJ9-U-19K5SZkhSyRfNyTbFXIdEuwqM6Wk23zQppzq3fHE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKeapmW6bQAl8Ruvm-hOvU1BptfVw4aXUxSy8yF00kdOY54xsy5Md-hucaaUHtK5DeqRtO6CVdktS5ZAGHEGmlVBEETNIH3OYLIwL2e68UObDBO-FTJRDx6LSL3Hov70xmHxuDmJUcUb5Ay3KFqt1Vg22hJpaqzNE6L0FNxRi2SxtnzbgXxSKwwe88RzVHLX4JN8iK2byFOqs4aB8iLPT04IROdLWYjRbpoFLGm2-1pHBczbZjfTr3JI6S47EQmOiOmcaYr31rXnZy73xDsqo0N1jYPhSZBM-eoveZgjxJLcGir1kEaAda4sjZyqskI0V_6a06Gd1Ht61owAPlfycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=SCfZowVvrYS-u2dwlPqYyvDpWpIhSejPf3LJ2eS45rM4ZJCjB6eSgzKSesXh8791bjl-4MEX_HCTD4Z72UO5WaxnZxS6FfS5oZWZMG8aejTvludPtSPljwxj8rPF963LP0MvYiPSuolat_hcadusjjGdfmGf3Qrea2PSFWRZAt87ycFvQPc_Nn0yEl0IZ5Jc_5woGJ4UUooo8CbpAmg5XuGWGWXumNiv_w_STSyrT1euXbc9nPkGO5jzo_vDBIUebc2WZPb359mvJxhV16dRy6Wvt2C9xLG5BaXB1Qf5xeUApdLAAqqUiHv0H9_mWUUejJcjFOaYwu5eWbBPcF-qK6hr3vbalVgKz9dyhpnn_BjqQ7hcXivx2FIK4_eLy7MQ9esW-zOkmYLclyjSN9h79fNNI42CWkRbJek6C9BCVGxIgvpRF3yLZ1Xcm5BC_h6j0W74VlSh0DvHcRudJ4-12Hoh1accTOujBm2VaKsAcEUFGPdYaAKy1jxfzKAdGrD6A3qMZ8-c_zNHqUCAiuuDrNfLgmQGsv_O4LOoi8bc9cW_G166XIhp9eNWP36p3dUu3cycWDJHHOFILky5Ejc8pX7eNyk9e9IeLyw4M-kzR9xtzTI_oIZ-vrsul7WEvdqUOSb70rphDlYhwtqe7H7qRyXvpk_ehyLaU9y3tPth2_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=SCfZowVvrYS-u2dwlPqYyvDpWpIhSejPf3LJ2eS45rM4ZJCjB6eSgzKSesXh8791bjl-4MEX_HCTD4Z72UO5WaxnZxS6FfS5oZWZMG8aejTvludPtSPljwxj8rPF963LP0MvYiPSuolat_hcadusjjGdfmGf3Qrea2PSFWRZAt87ycFvQPc_Nn0yEl0IZ5Jc_5woGJ4UUooo8CbpAmg5XuGWGWXumNiv_w_STSyrT1euXbc9nPkGO5jzo_vDBIUebc2WZPb359mvJxhV16dRy6Wvt2C9xLG5BaXB1Qf5xeUApdLAAqqUiHv0H9_mWUUejJcjFOaYwu5eWbBPcF-qK6hr3vbalVgKz9dyhpnn_BjqQ7hcXivx2FIK4_eLy7MQ9esW-zOkmYLclyjSN9h79fNNI42CWkRbJek6C9BCVGxIgvpRF3yLZ1Xcm5BC_h6j0W74VlSh0DvHcRudJ4-12Hoh1accTOujBm2VaKsAcEUFGPdYaAKy1jxfzKAdGrD6A3qMZ8-c_zNHqUCAiuuDrNfLgmQGsv_O4LOoi8bc9cW_G166XIhp9eNWP36p3dUu3cycWDJHHOFILky5Ejc8pX7eNyk9e9IeLyw4M-kzR9xtzTI_oIZ-vrsul7WEvdqUOSb70rphDlYhwtqe7H7qRyXvpk_ehyLaU9y3tPth2_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=jEx8wDEhdUcGp8ysl4WAyIcmsSLltK2DI_gEWD2NVJVKtfgsvjEPsBLArOXMQBJcm5kfzGH5o0Q96rIubSz3vpFIiN02LFwufjUe8FYWQpf7O7MsUw6s6Otva5Km9YdjLyd0GMxDXyN08XVxEKirIEiMZn-WjRsbedE22CdiLk-UocAV3HCR3JSkggsZaJlR_LY4mqZaGmIiTGGuSAo2Gg50xYiR0oJ1tinbCrVEXjHMfquq7x_ZNBBWVBhTRdkhfyira8ehACm0fl3aLCyijRjn4aRwxz1LrLkYsWV-lnDFCFZU5XhslObGiXIiJytiKP0MWIlFkOJzNWZvG5UsakUsKYkzekUMl3ss6P5_N45iJrSx1jL3R8lUsCKW017dfmj7ok3qQXo1TpMdpeP2Mmar7hRHC6inuSnmlhei96mZncgNnRZjfKB1O2p69tCeJiUyeS9F60CxSi2EYsTxbMNJ_el4Ml07TqvVERmr6N8KvGekyHw2nUCBg1sjUMiD5UrtRaM081X0XpSq7-YezlMZgZQTTkffBMF-2XYEoBLEE_OT-sauAo9Eo0L7f4rTZ3yi9Tn8CtJJEIqj761WVmz5v18eFplktA_V7nc_4RC4rm2yWiPkvEwWY3rJY-1GfITHB1aBzAUygkb-r3ze-N6wA05kfTNpqhpcu_mv1Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=jEx8wDEhdUcGp8ysl4WAyIcmsSLltK2DI_gEWD2NVJVKtfgsvjEPsBLArOXMQBJcm5kfzGH5o0Q96rIubSz3vpFIiN02LFwufjUe8FYWQpf7O7MsUw6s6Otva5Km9YdjLyd0GMxDXyN08XVxEKirIEiMZn-WjRsbedE22CdiLk-UocAV3HCR3JSkggsZaJlR_LY4mqZaGmIiTGGuSAo2Gg50xYiR0oJ1tinbCrVEXjHMfquq7x_ZNBBWVBhTRdkhfyira8ehACm0fl3aLCyijRjn4aRwxz1LrLkYsWV-lnDFCFZU5XhslObGiXIiJytiKP0MWIlFkOJzNWZvG5UsakUsKYkzekUMl3ss6P5_N45iJrSx1jL3R8lUsCKW017dfmj7ok3qQXo1TpMdpeP2Mmar7hRHC6inuSnmlhei96mZncgNnRZjfKB1O2p69tCeJiUyeS9F60CxSi2EYsTxbMNJ_el4Ml07TqvVERmr6N8KvGekyHw2nUCBg1sjUMiD5UrtRaM081X0XpSq7-YezlMZgZQTTkffBMF-2XYEoBLEE_OT-sauAo9Eo0L7f4rTZ3yi9Tn8CtJJEIqj761WVmz5v18eFplktA_V7nc_4RC4rm2yWiPkvEwWY3rJY-1GfITHB1aBzAUygkb-r3ze-N6wA05kfTNpqhpcu_mv1Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=u4XZytzUMwD_wInCw6Ke_yeULGbKrKv2NvA5cyRuCmRmkaFDJTP4ot4ZIG9j9OSOP7sYXMzsYWfY2yFK9uCrwO4N_Nk_nQ9EuNcFIXzlw7NxR4YkxSG5Xy82ez24TRXouQIexpJljCga_BmZ0qMt2lXVwhSmxQ3bi3SyA6o13MxOtRwykGN6qq4ojg-itlcc8kAzGZ8k8MujfcF0Gu1Vl3JPL4tN-nTDdl_XL-fIOqwav6AYKOxQiPZy5TOtZO_A_kuXs_mlIE_9FjuECFI6umOMJe8YCRoDWvNZgoxmYPf0C6ZVkmmXm7FTTmNu7ASrHQJ8brev6hR40_UxfKZb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=u4XZytzUMwD_wInCw6Ke_yeULGbKrKv2NvA5cyRuCmRmkaFDJTP4ot4ZIG9j9OSOP7sYXMzsYWfY2yFK9uCrwO4N_Nk_nQ9EuNcFIXzlw7NxR4YkxSG5Xy82ez24TRXouQIexpJljCga_BmZ0qMt2lXVwhSmxQ3bi3SyA6o13MxOtRwykGN6qq4ojg-itlcc8kAzGZ8k8MujfcF0Gu1Vl3JPL4tN-nTDdl_XL-fIOqwav6AYKOxQiPZy5TOtZO_A_kuXs_mlIE_9FjuECFI6umOMJe8YCRoDWvNZgoxmYPf0C6ZVkmmXm7FTTmNu7ASrHQJ8brev6hR40_UxfKZb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=cW_SjWoPKcLjCwocESvuUYL2pWBUiUj8WnYSughuvB9RCCb1mvI77b1XI_3V_wfWcb7aXWqzvBMla-Bmw3M7jR9YC8loDTNPRn_e9R-mMW42vLXJUylJcYzgvozbMqDLwETk4Y8N0L59bwFJQrfpiBoon7_ccTukyUHLg3S28uV0NQaq7qM3bsOhMf1MNLEAnHUfIxRu79p8hTBOXNKzJSkFaCv5e0FzlVfHqH-rODyIrMDRPgjKnBR2WAlhOxuyxRoQ-VECwiSTeDIUgiEm069JDEsxupmQtVLSLLd5ffFB6FKIDCZ49sJVCIF0g6aCYM2gYTwXToBIiL3bRnr48g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=cW_SjWoPKcLjCwocESvuUYL2pWBUiUj8WnYSughuvB9RCCb1mvI77b1XI_3V_wfWcb7aXWqzvBMla-Bmw3M7jR9YC8loDTNPRn_e9R-mMW42vLXJUylJcYzgvozbMqDLwETk4Y8N0L59bwFJQrfpiBoon7_ccTukyUHLg3S28uV0NQaq7qM3bsOhMf1MNLEAnHUfIxRu79p8hTBOXNKzJSkFaCv5e0FzlVfHqH-rODyIrMDRPgjKnBR2WAlhOxuyxRoQ-VECwiSTeDIUgiEm069JDEsxupmQtVLSLLd5ffFB6FKIDCZ49sJVCIF0g6aCYM2gYTwXToBIiL3bRnr48g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=oy0pPfnJrZv4YzxfolXJQu5kgDUXLTMmrE6XPCm_V-lbEM-P9Hayuol_Kycv8vJO0SR9Dz_2gNur5FvjoIf94FbNeoAOvuTveFf8ctIg5IXhcTMfygBFV8yyYktQf_psvp6ktVT1EkWtkVZ6Of2x7btVp9ZbB7vIUX0G0tqViR7O0wtSdJw7K-m3_NDyiTjWTj_T1dd_dtRvSbnmGkIEFsvK8-XGFkMClfTA9dwxFFJVDQNTlgh7-ZX0FS4gihNC1HLfq0yKmlzOpPJt-AATKv4G264XGChrq1v7Qf08bGRE75WdauBD4_wOZf0bwtaN93tklFTd2vdq9haGVmG6AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=oy0pPfnJrZv4YzxfolXJQu5kgDUXLTMmrE6XPCm_V-lbEM-P9Hayuol_Kycv8vJO0SR9Dz_2gNur5FvjoIf94FbNeoAOvuTveFf8ctIg5IXhcTMfygBFV8yyYktQf_psvp6ktVT1EkWtkVZ6Of2x7btVp9ZbB7vIUX0G0tqViR7O0wtSdJw7K-m3_NDyiTjWTj_T1dd_dtRvSbnmGkIEFsvK8-XGFkMClfTA9dwxFFJVDQNTlgh7-ZX0FS4gihNC1HLfq0yKmlzOpPJt-AATKv4G264XGChrq1v7Qf08bGRE75WdauBD4_wOZf0bwtaN93tklFTd2vdq9haGVmG6AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=B_MhotVg-KV_2DhcEW9FEefIqoxJv2f-E2Ok_F6tnMwHqP7YN4LNhCwrnGKVahMVLzBJIDTDXO_P_bHm00nxx0o-WsPO_m2OUArSccAXYQ_guM6RjNJQO46PeATONmw6tZhcuO5rzqjJUMulUzqEFOZkXbAl1EW-0H0yD8jUSx21i9g9QE66s_b4NWTc2raaPD_4Abuw31fld81B_AK3TLa2Ry5g19DFoLQ59Qs5aWhooGkDZAvkG8WtZQh1INUUBP_x1MFUi0MKXImJKcXCA3bVEMnHiCWXl05OJJW4wwyroJBG6RBTiX0xBfF0zWza1MK6HApdEPFky6QGmAftOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=B_MhotVg-KV_2DhcEW9FEefIqoxJv2f-E2Ok_F6tnMwHqP7YN4LNhCwrnGKVahMVLzBJIDTDXO_P_bHm00nxx0o-WsPO_m2OUArSccAXYQ_guM6RjNJQO46PeATONmw6tZhcuO5rzqjJUMulUzqEFOZkXbAl1EW-0H0yD8jUSx21i9g9QE66s_b4NWTc2raaPD_4Abuw31fld81B_AK3TLa2Ry5g19DFoLQ59Qs5aWhooGkDZAvkG8WtZQh1INUUBP_x1MFUi0MKXImJKcXCA3bVEMnHiCWXl05OJJW4wwyroJBG6RBTiX0xBfF0zWza1MK6HApdEPFky6QGmAftOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=YMXTWBVfwqBhVBdCqLZmcs7ave2xVQ0eFgrRvo-CayuoK3O2hZQ30Ad63XXm8_MNBodpFkUG91wHtj2YYblco1mm2HR-4OKKJbTMzF_4f8ZJU0uacWDjtccvCfUoYoZ745lh-2N1UgFSX0yq3iUpwsf7f1s-uLol7XeDd8sbsoEfIb3VC4iWXXpLlaYBrI_RUAlKWYtEUVPLBlHSu0ZnEMEMPhlWyA5uZHeWiRIC-kOqqX7DWdhvbIBbqrEXB4IWFjh_XmZcn847NggUnIIfMU4KY6s1r1emcZK0Kcn21yHrCTbu5THL0fDSy40kc70GsMAMSpyA03zgejQn4cnQ4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=YMXTWBVfwqBhVBdCqLZmcs7ave2xVQ0eFgrRvo-CayuoK3O2hZQ30Ad63XXm8_MNBodpFkUG91wHtj2YYblco1mm2HR-4OKKJbTMzF_4f8ZJU0uacWDjtccvCfUoYoZ745lh-2N1UgFSX0yq3iUpwsf7f1s-uLol7XeDd8sbsoEfIb3VC4iWXXpLlaYBrI_RUAlKWYtEUVPLBlHSu0ZnEMEMPhlWyA5uZHeWiRIC-kOqqX7DWdhvbIBbqrEXB4IWFjh_XmZcn847NggUnIIfMU4KY6s1r1emcZK0Kcn21yHrCTbu5THL0fDSy40kc70GsMAMSpyA03zgejQn4cnQ4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=WsNPmrSQeB5tFE_RUoHpveUYfDjpqS2LuO5POm0891liRy5zEBs057Fj_hPTmFe0ZaJj8ttLIxoqkg3i8uohRavdHJwYz6aM_GA6TnFvvo_xg2FM0UrpdMM8BCsx2_gsKyOLYI9IS9BeVHZpRnOaclZNi9up2l2Em3NqwLkZhjv2Ylhmm1q9KZaoAqsFU4RgpBNuOjX-BwRbjvPCJhbDiKGSoVJ40vo6PuU2k44HtIMRs-UYonZ7y_4-KA_t7W-ffU65EHXO2eYROnl-tOqlHdYC2yXqVK0QcfYYm3CB5xFAsVLr8unOoZIxWUZVKXAqflIOO1ATanIUkOinLQ58sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=WsNPmrSQeB5tFE_RUoHpveUYfDjpqS2LuO5POm0891liRy5zEBs057Fj_hPTmFe0ZaJj8ttLIxoqkg3i8uohRavdHJwYz6aM_GA6TnFvvo_xg2FM0UrpdMM8BCsx2_gsKyOLYI9IS9BeVHZpRnOaclZNi9up2l2Em3NqwLkZhjv2Ylhmm1q9KZaoAqsFU4RgpBNuOjX-BwRbjvPCJhbDiKGSoVJ40vo6PuU2k44HtIMRs-UYonZ7y_4-KA_t7W-ffU65EHXO2eYROnl-tOqlHdYC2yXqVK0QcfYYm3CB5xFAsVLr8unOoZIxWUZVKXAqflIOO1ATanIUkOinLQ58sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=qbgkuQF8mu_DaItGinM_Y2vRRoy-ewUwhlS9PsPO_5EgUYXI86sLcYoNIc5L27Nteqz2z37NCTjwOk3ji3zw9Ioejtr9tg14trjsPGnH-K7QHsHFhE946c6rZZVa7rJ3wL5PDOWLCnI_BxeKhy_SGNe_TiGyNax7J2XPh8aX5iQtTqDW55QJGr86JAnYSSYql1SVUCLTi_QS1FgTLhiMelnAl-hGQxjLAoMUeRHvMk7R2m3mkes3_4WOblwnKj5TUKByaGXQtOYgjw_uskkYyqE9RtxGDjRJRgM9bjMWohtjYUwzLcRmAOn97c2fAaNsSWRo_B2eKcal85-29SOjOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=qbgkuQF8mu_DaItGinM_Y2vRRoy-ewUwhlS9PsPO_5EgUYXI86sLcYoNIc5L27Nteqz2z37NCTjwOk3ji3zw9Ioejtr9tg14trjsPGnH-K7QHsHFhE946c6rZZVa7rJ3wL5PDOWLCnI_BxeKhy_SGNe_TiGyNax7J2XPh8aX5iQtTqDW55QJGr86JAnYSSYql1SVUCLTi_QS1FgTLhiMelnAl-hGQxjLAoMUeRHvMk7R2m3mkes3_4WOblwnKj5TUKByaGXQtOYgjw_uskkYyqE9RtxGDjRJRgM9bjMWohtjYUwzLcRmAOn97c2fAaNsSWRo_B2eKcal85-29SOjOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW77E1jXd83_Ub_cjHO0NjoNcKyd9YOZ-AWfLdflflhfZBaeQy80jrut4U3J8uopajvzrqprg0WUOYGb8tdnXcBBzyCee9YAVv74cMJcSbwLFAjaTpbvDcoXxdp7YZ7Pocg6zMOA18oTIXXQxlxNWPpkcXpaU0pi1mM0ivevj_rS-MrEYyFk1deadST89uZDJGyX5Pq38-6evBqTuGdR61DmacQ3mp6tmvbcViOWtrlWyIUJHz1OB3Nbk01UQ6JqWJ5DAtcDoLDj6j9b5BSEw7Vqo6a-smWxE0PHZ3PIEQhs1S8KznB6jsOUEya69PSYlhRvL8fzYbox7XVWgEfF7w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=rNu_0Ew_OdAwINmle-gGXaXqA-mx7CRsSh6jAD6dExFpcuUrSdCibCTthIH6ID8O2TE98gdRobvZeO9tb7HX4Nm4WeWa3YBhVSMOOxYip3gMgnzPyx23LAkA_xX5M8XRrXTpO2Pnc8BbIpwIHf8gxxF-F7ZAllsdnFMAYSqV1mPvJ6Fx9SQoTV-cPgZ4lgmoHqilAnjClO8N0TJthdlo4WalRYShhvEWz4KHGkg2EAFqTlY-md6jcdgHP3JYSHcxkSNfutmu44iu55LoiZkQWnIYznawjB7CyMOIrviKRJNQfwTRN3EvzmY8mB9eIlgR6i3dvU812Q7ksXmbl6447A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=rNu_0Ew_OdAwINmle-gGXaXqA-mx7CRsSh6jAD6dExFpcuUrSdCibCTthIH6ID8O2TE98gdRobvZeO9tb7HX4Nm4WeWa3YBhVSMOOxYip3gMgnzPyx23LAkA_xX5M8XRrXTpO2Pnc8BbIpwIHf8gxxF-F7ZAllsdnFMAYSqV1mPvJ6Fx9SQoTV-cPgZ4lgmoHqilAnjClO8N0TJthdlo4WalRYShhvEWz4KHGkg2EAFqTlY-md6jcdgHP3JYSHcxkSNfutmu44iu55LoiZkQWnIYznawjB7CyMOIrviKRJNQfwTRN3EvzmY8mB9eIlgR6i3dvU812Q7ksXmbl6447A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=jOEbguoIm29dpoj6lzq4IqVMm-Bkp1ojUlmPdT3o3d-dM8oj2nvRwReQJMZQ-PgwXtgDBXIx-qO-55ewYsTj7jT4rcoqJMFyvb2ZCJSf2s-6zgAGzSPNW4WRAQVvDy0lC67c9HIef73JFRdGeEf2E0A_3H9iEzLknMp5wRg7GLPu9guDyZVGZxdG2WDKOTyTeziKXMxvNnVhLRg50SptYB33bglf8rsr3uJNjpXlMPGJmhFm3NS22SeOXebHFa0qXdikWR2H_7qE64PouYxIWC1DF7U9Z2b7zNXTopgzPkxwkAiLDZ_zRK0cONl2b3wwIfOPWPQAGgJ2Oa_tIq4gVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=jOEbguoIm29dpoj6lzq4IqVMm-Bkp1ojUlmPdT3o3d-dM8oj2nvRwReQJMZQ-PgwXtgDBXIx-qO-55ewYsTj7jT4rcoqJMFyvb2ZCJSf2s-6zgAGzSPNW4WRAQVvDy0lC67c9HIef73JFRdGeEf2E0A_3H9iEzLknMp5wRg7GLPu9guDyZVGZxdG2WDKOTyTeziKXMxvNnVhLRg50SptYB33bglf8rsr3uJNjpXlMPGJmhFm3NS22SeOXebHFa0qXdikWR2H_7qE64PouYxIWC1DF7U9Z2b7zNXTopgzPkxwkAiLDZ_zRK0cONl2b3wwIfOPWPQAGgJ2Oa_tIq4gVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=hraMBDJJb2q-jGP8xD80pKxMN44uBbDUZYljZrOZOl_kggyI0mdCFi_fmyKHJYRoExTWBBvOSnJ5Wx8guQPhm_Bfxs21TfAZLkvw9ZDATYeHrHBrQ7WRRcyDXG1LmJouuHWnWoTuwXe9giFHqgCE5ITd5Ma8CRPAHYb6uh4eW1sZaBwtJbQqjn7cT8T96PcDVE9ffJ9jDSwwJiwMgDioPK8BtS8sAP39n5PU1vda3FaJQtQj7LU9V7GMXAGTZll4v_9-EmQWOSn5rNgQi0Iv8O1Gu-65FnVNgjiJtQcqngSGsUruvw2hEQS9Mf5liRsqPcHwDFs9tVQcYNN04au1Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=hraMBDJJb2q-jGP8xD80pKxMN44uBbDUZYljZrOZOl_kggyI0mdCFi_fmyKHJYRoExTWBBvOSnJ5Wx8guQPhm_Bfxs21TfAZLkvw9ZDATYeHrHBrQ7WRRcyDXG1LmJouuHWnWoTuwXe9giFHqgCE5ITd5Ma8CRPAHYb6uh4eW1sZaBwtJbQqjn7cT8T96PcDVE9ffJ9jDSwwJiwMgDioPK8BtS8sAP39n5PU1vda3FaJQtQj7LU9V7GMXAGTZll4v_9-EmQWOSn5rNgQi0Iv8O1Gu-65FnVNgjiJtQcqngSGsUruvw2hEQS9Mf5liRsqPcHwDFs9tVQcYNN04au1Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=E0x_LMlEdNme5oZLAyrBAXk8u07HRIF0j17NL44H-GKdwDSJwb_f0Zii_VLmZFWoNT8IFqqVSjSreZC8lzGKQSTTIvviYTkn7nyQXmovXSwejYHule5dfw4MzHiAESZmLYb4-sO9RB9chUT7GiDwNf3whZP8lGKbDva8y_ByPkY9k2NRRB066lc5Q1yiYRS28Y2PK6SFQldI6l54bvlUVB5RIvACHUicuX654YngaWHGxdoZC3NI5xbubMD5vUI5QK5-larMtZHkiZaoDoDp9Rlr4ntVkRq1pFTFcqbeDW4ZlrymoFmli00FKG3zXyT5j-t90_kAgtzIjDvDox4Fuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=E0x_LMlEdNme5oZLAyrBAXk8u07HRIF0j17NL44H-GKdwDSJwb_f0Zii_VLmZFWoNT8IFqqVSjSreZC8lzGKQSTTIvviYTkn7nyQXmovXSwejYHule5dfw4MzHiAESZmLYb4-sO9RB9chUT7GiDwNf3whZP8lGKbDva8y_ByPkY9k2NRRB066lc5Q1yiYRS28Y2PK6SFQldI6l54bvlUVB5RIvACHUicuX654YngaWHGxdoZC3NI5xbubMD5vUI5QK5-larMtZHkiZaoDoDp9Rlr4ntVkRq1pFTFcqbeDW4ZlrymoFmli00FKG3zXyT5j-t90_kAgtzIjDvDox4Fuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWeAcVMNmzvLapzDY0ncfkA6_RN2rctKTaCUfgiapxkuLiy-3zZ_XZoN0TxG-dbCMgMU8c8Jz79Lw93KpjK2-81QTQxQJ6oNXhgxGG70NCI9BQxlNfS6hmuXkia9LicTyr_eK7dSMnGVD42QCEh-jDTCR_9V7yirP2WjxhCscNI4nQmedQGHfvuvOBLRLPFFTWmqU-1hpOTEeleM6Qclz67ogYhPZ-jgFYDNwy8t_wK7gaCIqLeGijiUDuTzq_LMKLJKxo-bqCmdstlQSNwwquOfvIzSLbF5LYDX8L1oukJ82jovJxjIGiz2EU0XQhYpu--uw13PBk9g0LntS_ZP-g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=K4i6_TWEFAndeVdL_As0LG7D0mvIHPy8J7_PEITrro3bj38SX_wcvbm5t6LBYUoUhbt90EW2T_Qy7NRtR0lIA5fH6lzQvIcxvzKYs82jsN1eqp9RL1WAo8pfULB-rphmCnfgfF7XvXGnHAv-BiE2wPzi-pJQxJ-NzfweSDNEwsTf25ggcZSKyl6J8qXAhTvT6A1Pb86T3kQlYOAVB1eBim6Laql6dTFkRm8gHT7SuyV1dprBOWgwElLerLDeBm_jP9rcIWkon6OkgzdWy36w74pT-ZJLmVXL1eGLgzr9tKtvUoUcfV1IjL-tv7ecfpPJyBpEKlbam3iGEgUmP6-aBzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=K4i6_TWEFAndeVdL_As0LG7D0mvIHPy8J7_PEITrro3bj38SX_wcvbm5t6LBYUoUhbt90EW2T_Qy7NRtR0lIA5fH6lzQvIcxvzKYs82jsN1eqp9RL1WAo8pfULB-rphmCnfgfF7XvXGnHAv-BiE2wPzi-pJQxJ-NzfweSDNEwsTf25ggcZSKyl6J8qXAhTvT6A1Pb86T3kQlYOAVB1eBim6Laql6dTFkRm8gHT7SuyV1dprBOWgwElLerLDeBm_jP9rcIWkon6OkgzdWy36w74pT-ZJLmVXL1eGLgzr9tKtvUoUcfV1IjL-tv7ecfpPJyBpEKlbam3iGEgUmP6-aBzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=CR2oA-35HSArCXYyUGHRtaa9HDTiro4kNTaJHHZRSW-ZMwLgCWouCMlSzU6uS--LsjL9ASlTkB_CCxRTFB27wGaECyJBrOBJtVLh1mZ6wzqndWC5I2jhTeAiOoUhM34TZRJrZR0NqNyW3vDIgtJUs2DHaVk0hiHNGL1ox2HEoDv4jYmmsj5DhXUDGy2Ci5f5Yn4kCDNtBR9xG2c3vtHOt0Cnl6273Q1oSKjEZB2MR0em1BVhO4ZKOMLrTUXGHmGIf3P_oX_YU2YiDk0ui60YqjoVK3jSb7wNEj8oV67ELZotsx5YEHFATWZ3tlFp6IxbVGjn7Bpjrd2MlcwbtLn2rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=CR2oA-35HSArCXYyUGHRtaa9HDTiro4kNTaJHHZRSW-ZMwLgCWouCMlSzU6uS--LsjL9ASlTkB_CCxRTFB27wGaECyJBrOBJtVLh1mZ6wzqndWC5I2jhTeAiOoUhM34TZRJrZR0NqNyW3vDIgtJUs2DHaVk0hiHNGL1ox2HEoDv4jYmmsj5DhXUDGy2Ci5f5Yn4kCDNtBR9xG2c3vtHOt0Cnl6273Q1oSKjEZB2MR0em1BVhO4ZKOMLrTUXGHmGIf3P_oX_YU2YiDk0ui60YqjoVK3jSb7wNEj8oV67ELZotsx5YEHFATWZ3tlFp6IxbVGjn7Bpjrd2MlcwbtLn2rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UTlz5py8mQLKwBVP-XYoIwHQNHQSCdL1YHtCKI7ESJwfS1Yko11Ro9Bl4N_O3mqpVh626PU7jwMCmmwRoflqeSSmjTq1GCIrcfkoWd3QEf5Xq06rBH0i2l5xIRx6bHUk33G_MqsQE8qsa0taYDBdlRapm7i2hUq7G_v8upxl7rN2pdqrjBY8Dpr7BpNVsoXJunvQ-QJF9rxeMKtCNS4jWChTUVtQbA10sil1Oz_TRCkSw9wKqibK4eZvQQC6zdaCx1n1UFMQFfgCcLH9Jxu9OaAufBDuFLzk57dku7VMg43NqdDqt_hspWQr4Hc2Cnz-5CGxeIClvn8QUs9YKKpKtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o4zxFUcFH2QUGj30Ai9ti0K1aYfqkf12sfL1gb336gTckdLfsta38KuyBY-PbGvPDI4EpIfIkExhvEeuTpZ9tr6GLtO23biY9uIRDSb7gpFqEvuw_0UKWRmzlHLmOzqTjLZi_K4lVxgDVvP7qwnJ64oHbm1q-hs9LMxOSMK9kse2Rm_8gCaCcWlwDyQWfV4bQ2zyWm2ktaNDFJbyPM3boMXtA5yiyEXCO9jUN91I3RDfxnFMSPbdcU4bei272tShkl05Q7r_ry3L_eeNulmYi8TxUST9NBTT1-J_xgwm-FINKhnHl_5GJuoB_AVF2b3m4mrx1Aw-Hxrax195BtyxeA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=BcmZPlwiiy0LDYLh9DNNxxC-NtfZXVCK3eNrlYagCQ29dOeDwJKM5Q3eMGQyjtNesEMLYfvZJ6i02er0Dwu0oaOa31tF5ym5moW6L93o6KK6totf3RdS8qrEH28TojnvtT3G6Wf9rPzlAl2baAet5HnISstjB6QG5PmNsmZ9t3QNPqN2PVtzVFul0Mk1MJb34Z_WOMF6c-rN1DR3hULGg0OnvIimNo5d6rL3-dILnzFUf2ghjXQVGBixCq6mSQxlPYgQJsaMmobPCgagDpnwREuDVXPXxs2tu-LTcpEJCkuYSwTw9uQaigGcdfki-qGdba1jhWz1kGAR4e48V0J7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=BcmZPlwiiy0LDYLh9DNNxxC-NtfZXVCK3eNrlYagCQ29dOeDwJKM5Q3eMGQyjtNesEMLYfvZJ6i02er0Dwu0oaOa31tF5ym5moW6L93o6KK6totf3RdS8qrEH28TojnvtT3G6Wf9rPzlAl2baAet5HnISstjB6QG5PmNsmZ9t3QNPqN2PVtzVFul0Mk1MJb34Z_WOMF6c-rN1DR3hULGg0OnvIimNo5d6rL3-dILnzFUf2ghjXQVGBixCq6mSQxlPYgQJsaMmobPCgagDpnwREuDVXPXxs2tu-LTcpEJCkuYSwTw9uQaigGcdfki-qGdba1jhWz1kGAR4e48V0J7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qob7gmQiXOdT3Ed47eXHDsEK1pnIUvNiM-q-zI9XLbxaS2_b50yBiZfmYrVFnK7sv2nXmykr_gONhardh-JFuzeNQWfvrhk8oigQ7FYsgmaQxJt4HiuBaTkIYjZiw1Dalhyu0YIh50Taq26VmD2Co-KEL8BFyFnrno4NZmTH4_8rHan5yk7YSfIlsUJU0fGqT0nYl2ihoCdRnj6zbubfnTdJaqg1oBb69k_fQzVT3AwQTLKF-o42oQEv7lmDcbifBOHUezBV3SYZaLFd-oqakC3Mx8lGhjQJCWDp88VllL8Kz8vrsdBJoVzFcnj0HeYjnv0IW1gSKX6uLYZ3UMmScg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rE3xY65WZrpixPqXvgQisltNOet72BPIu2oNy1HCg8LhcaYBfDMzJ5yz1un2gKb7FXm7T9WUCORseh3DH2RbxlAy9fdx-ZvJBNif2kF_8vN7nLPFXVpMss3hbP6SN3WpLPyIung_Ze3rv5lHUQk8n9MJFh6wefq1hCSX55VmRlswLaNJy_gsXe7sWt7I39a_P_WoNYH5ChiA6tafS7PP92zl-f02t126gOd-jZ8EuI66TQ2QecAYnaWwEyVtr29fXW5gSH45gsg4rGx4GdwJZ6neD6Uyg9K3RI3RaO_LiSryXcEO2JT6IUI2Qj2PUluVnhGa2eJP4Vb-hJBNLK0L6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaZLfdKsoiWWvk0yqQctuKOXAwvGiDjawNcH7TYbBWA9qDYFOviwzbg6VF1wJd3q5aEuf8t_clQvMWwAjPEfVn85gU9aL_gLN41cm54CsacLPuN3gUJetIZgMOHkcWT9yitkMxGA63bYJzKAB790RjdcDA9P74KIFg2jD29F3B4r6vEc0pWDk7hBQKxNrncuZ4B1EapzE9MDs_78m6nHvRhmgj_sWVHShcMT9VEDptf_zrgG76Mvm8Ss6scjRVx2KYrQAzHrGJdPv3s-kFgWHmI6idajyEUcUNfeGXOl9NSHhCIK5ASMTZXs8WizWkN6rkO6lii4FyS80z3DrqEmBw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=isZVGH0UDfh5S4Pkej2WhY1xW6uMszYc-U8obLNaY_-ATVAIOY6exwRFwpODKb_BdcZLqAIQhm07e4sxUuJu-Jb_y8WEfC7KheRVG-4rGeRVe0e19d-s-mtq_kH1FMp5RiNNpVvU50S3YQpAkvL-tgOkx6EkmadSRus1ttB-1VHrFBD5CohT4df6-q6wnJSYH6xSgTFupVtbwVXoGHO8bAM0kK0uCy_qlVKC27GPWNAkNS1pO9clG4CDzjijWDmG0j-k-VkSzM8NjU29H_ngTzvWR_Rbjd1ZmxDFqk-6BbDYCVfO7JLaeqgWnezvHN27DMn7qfirGlh9STfjie0vsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=isZVGH0UDfh5S4Pkej2WhY1xW6uMszYc-U8obLNaY_-ATVAIOY6exwRFwpODKb_BdcZLqAIQhm07e4sxUuJu-Jb_y8WEfC7KheRVG-4rGeRVe0e19d-s-mtq_kH1FMp5RiNNpVvU50S3YQpAkvL-tgOkx6EkmadSRus1ttB-1VHrFBD5CohT4df6-q6wnJSYH6xSgTFupVtbwVXoGHO8bAM0kK0uCy_qlVKC27GPWNAkNS1pO9clG4CDzjijWDmG0j-k-VkSzM8NjU29H_ngTzvWR_Rbjd1ZmxDFqk-6BbDYCVfO7JLaeqgWnezvHN27DMn7qfirGlh9STfjie0vsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=cLis2VbQzEwqmP3KPR8SXrMJm55W89Ni9F-sipjpM8E6qcuLS6ptxaTsJgtBhG2Ec3Z8ZhqF91yAebIV20GK0tKGDhtJd-mmApWpimBwLI57CyxuGjyNnbW4HE5t3aRr4jwHbcs9IBKF8XqEtTI2wQ-9JEux6bkKuYAOXvfNyiF6UbD10w9ntdqjl00B2GUlX01WcQ1R6CIaSt3n2wwJ6uMX1Bem22YJF4mcXyLGY54rgHFKsPeS_47PjZQ8ELiQ7buQS3iQ4NAq5TR0VJsSzvOQEVgJc0dAzwt7frh6SmLLilrpaIStzOXnWK_BNP0J4okVC1kCGtNjgH5Fg8mY1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=cLis2VbQzEwqmP3KPR8SXrMJm55W89Ni9F-sipjpM8E6qcuLS6ptxaTsJgtBhG2Ec3Z8ZhqF91yAebIV20GK0tKGDhtJd-mmApWpimBwLI57CyxuGjyNnbW4HE5t3aRr4jwHbcs9IBKF8XqEtTI2wQ-9JEux6bkKuYAOXvfNyiF6UbD10w9ntdqjl00B2GUlX01WcQ1R6CIaSt3n2wwJ6uMX1Bem22YJF4mcXyLGY54rgHFKsPeS_47PjZQ8ELiQ7buQS3iQ4NAq5TR0VJsSzvOQEVgJc0dAzwt7frh6SmLLilrpaIStzOXnWK_BNP0J4okVC1kCGtNjgH5Fg8mY1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=ASTKJ18jXT-dxIrImSCSqigeWvok4YUdgQcGJ-W1o3CA2OiM_du-ebFI0aSbxNEQKC6kFQKY6sVQ9l7D6n0GDTiiKAcja3NgrP7l81jQPWsA6tl5iUisojz5k810bsLqprIxiMe-cb8prkQCA6STMHk-4l-ipKdyrVxf5B8RQkzH66-Pe6m-J641msY4YpOLDsao-sAVG7yIBx4Zbr0GgprqTljtfdZrLY3vpKJ2pVQN9F3EU85EfwMM-cTCKcV9BxhCgKR_VEP6HQhVHq42OczzQAi_wI0UtvKy_jHTp6chIBZ_x9_7rvl8mCffiNAHQFDBEtvRsRpeS0KUu6Tg0xoAo023JXP1o6Wlt5oJZrp7gcg5jhU4ghjJSNd_QCGpzUqLh0fRC8M7X9wRJp9RXhrgMdx9lvpR02ZFPUqhRZm5ltCjgFeLyRibYOH_cBIkP1gfh7pO_UrUDgdgIUltK2B0Z-MrNcyKVbDLDC5vm8iLsEy-6z_Y76zSyMUpYpIoF7TPshSvNW50YndW7SQ9p6hvvxWpb5uxbZ0RaxSj9634bV-TJp7CzPOUCEiBUbMBt7cKu5tlqpbRNqRu3fGOWXw6pKTsFb61XphEmUV725cBT8ozMKoju2wxbdfLGUG9qQ7Hfws_AiVQ6zdphqiUOxci2Zp_CJyMltt50blJ8Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=ASTKJ18jXT-dxIrImSCSqigeWvok4YUdgQcGJ-W1o3CA2OiM_du-ebFI0aSbxNEQKC6kFQKY6sVQ9l7D6n0GDTiiKAcja3NgrP7l81jQPWsA6tl5iUisojz5k810bsLqprIxiMe-cb8prkQCA6STMHk-4l-ipKdyrVxf5B8RQkzH66-Pe6m-J641msY4YpOLDsao-sAVG7yIBx4Zbr0GgprqTljtfdZrLY3vpKJ2pVQN9F3EU85EfwMM-cTCKcV9BxhCgKR_VEP6HQhVHq42OczzQAi_wI0UtvKy_jHTp6chIBZ_x9_7rvl8mCffiNAHQFDBEtvRsRpeS0KUu6Tg0xoAo023JXP1o6Wlt5oJZrp7gcg5jhU4ghjJSNd_QCGpzUqLh0fRC8M7X9wRJp9RXhrgMdx9lvpR02ZFPUqhRZm5ltCjgFeLyRibYOH_cBIkP1gfh7pO_UrUDgdgIUltK2B0Z-MrNcyKVbDLDC5vm8iLsEy-6z_Y76zSyMUpYpIoF7TPshSvNW50YndW7SQ9p6hvvxWpb5uxbZ0RaxSj9634bV-TJp7CzPOUCEiBUbMBt7cKu5tlqpbRNqRu3fGOWXw6pKTsFb61XphEmUV725cBT8ozMKoju2wxbdfLGUG9qQ7Hfws_AiVQ6zdphqiUOxci2Zp_CJyMltt50blJ8Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=klSoefXqhmW1xnx7WUhFBpoWXW0w_nN-K3J9mhEHpMMtC21SEhjBDBZo_qX6FN4rOeXFD76X1QpbkT-sHH9K5eXuyA1WBImHLMmK8drL243ZJ3DzlAmO2vgaAMCHDN5Q3FiPQL-THmOKkA5iYw9WW-z-1rgPf9B0_YadnErLLvdSuNDBE3amveBmpScqkSbo1znGE0usz1Gx2yxwsR4BpBtpoBHiW4f5j5yBUDS97Rev6DN_bFBxWWOC0u5NuDMmIb_NhSMOFalox-zclH-l6--xUMyBSSIfOfBQB_-jgOrmjfP2Gh6hVKEMYiIOH_k05e4_CWe--NKiRdX7Zq0_LbUH3knG8vW9w0nt31TmY1PTPpRXrvPGGt8zEXBxuVkn3cm_7YJ6l14J9iTmHJcFGJkH-5MQI2qwIXAmF-WZnMMj4482q1cyorG1COzvsPfKTmx0vmUkcwv630M5oimc1tN-t_bxcgpEqdjHYz4YPuOpA1BIT1E_oVg921H9HzY765VmI-Kh8Xsh4YtazRO9txKgheSzoZ9bmSNlUZW3pjEazGfztyMwo0kPSZWcX2aoDqWpbkgZXu19kgiIdQDbcfUt2dl7PWbPdiaN7uDbcxV9eqvUIeaXY0hYO17qE6mZx4191oVVvCsFbiEmqRz02yLpvGIpU2bBSqck36AU9_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=klSoefXqhmW1xnx7WUhFBpoWXW0w_nN-K3J9mhEHpMMtC21SEhjBDBZo_qX6FN4rOeXFD76X1QpbkT-sHH9K5eXuyA1WBImHLMmK8drL243ZJ3DzlAmO2vgaAMCHDN5Q3FiPQL-THmOKkA5iYw9WW-z-1rgPf9B0_YadnErLLvdSuNDBE3amveBmpScqkSbo1znGE0usz1Gx2yxwsR4BpBtpoBHiW4f5j5yBUDS97Rev6DN_bFBxWWOC0u5NuDMmIb_NhSMOFalox-zclH-l6--xUMyBSSIfOfBQB_-jgOrmjfP2Gh6hVKEMYiIOH_k05e4_CWe--NKiRdX7Zq0_LbUH3knG8vW9w0nt31TmY1PTPpRXrvPGGt8zEXBxuVkn3cm_7YJ6l14J9iTmHJcFGJkH-5MQI2qwIXAmF-WZnMMj4482q1cyorG1COzvsPfKTmx0vmUkcwv630M5oimc1tN-t_bxcgpEqdjHYz4YPuOpA1BIT1E_oVg921H9HzY765VmI-Kh8Xsh4YtazRO9txKgheSzoZ9bmSNlUZW3pjEazGfztyMwo0kPSZWcX2aoDqWpbkgZXu19kgiIdQDbcfUt2dl7PWbPdiaN7uDbcxV9eqvUIeaXY0hYO17qE6mZx4191oVVvCsFbiEmqRz02yLpvGIpU2bBSqck36AU9_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=sCtQ8ig9rXaGh3IRH8GT6gSsg4ceeL-zj_vcQHas3Mz5TX9BPa6PGCgDZFdhHoLrgjFf-2MBAmuV1QD06n1c7uoGrtHEI6sCCuHQVtt8V-DZAKvOfY7XMzEtb63ijAI3onE5EkueiYMXVeYYMLSfC9qevC6CYvCGTsmzYt3BusE4SMrIifhXEV6bAG3jOk4vZHyKAi2cuK8fEbYxbBlh8Ymhu49u8ptnSmMMygALBhOIfVDUtlH9rwF-aHh6EcWt6pXWFANHFfLZTjuq0lkQve33K4A3fnOwzOW1vrNPIWMLJFI5JPaNiv6IHv9Xw-QTjko32S1UR9916lv8TLTrYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=sCtQ8ig9rXaGh3IRH8GT6gSsg4ceeL-zj_vcQHas3Mz5TX9BPa6PGCgDZFdhHoLrgjFf-2MBAmuV1QD06n1c7uoGrtHEI6sCCuHQVtt8V-DZAKvOfY7XMzEtb63ijAI3onE5EkueiYMXVeYYMLSfC9qevC6CYvCGTsmzYt3BusE4SMrIifhXEV6bAG3jOk4vZHyKAi2cuK8fEbYxbBlh8Ymhu49u8ptnSmMMygALBhOIfVDUtlH9rwF-aHh6EcWt6pXWFANHFfLZTjuq0lkQve33K4A3fnOwzOW1vrNPIWMLJFI5JPaNiv6IHv9Xw-QTjko32S1UR9916lv8TLTrYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXjcIkzk66J9bJgfoR9Oo5gFEwd9snK_tQeMmz40LrpK91atlGWLQzOudSZ6pz9wHMsG4BpbgVhMtRayfnKCR63XXq9HQQztkdSJtYnBrs2IJAmDacoChvqEv4VnlVxJUKIOsiBHaBfE8I0rkp9sManFB2Z6IkBLEsmkSan76hrwyXBN-S-Khb7sexJ5hBFLvLVQkfKmmuBtS8WRF7EsP7xqQVejVTKzuXXDGP_MNftzMMrstHbh-TzLnGVvYJYdkRoNezmrZDfa3CacVYH88oCmESt5AkpLePsQGsZCXs3Y8AwCjQuNqgHQlvvmpbn0qu3JGoL9bIAUWA-DQr8OFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=giPLZ39_gTmoWxaLQA9iEaVP70VbCcpRGejhA_9q_F0UEwevs3wFt99bOQ__wPABv3Za4nATfqffKWqgOY5qwQrt0e836uM-7lHdtrOKyLLMzDjVHeSjVwu_k7gTSvGtKsx1R7tBH4RXnzhhL9M6R4l3tokDDiG-lkXwtO_jS5M71q8HEntEIsjX4qWbJvv1eMlRc8PPlo13T3v_l5aX0t_Mya1Di0-Wm-qYQ6_h7dXjavJ8TM2Clcn2ksHujvVZSad0LPU1A3k39c5pVQXS_-hbFahZRW6N2Q8GLihVfFwFmsNjI5Id-DBCut5ZDIngJrTT1ylvo6HORc7T593_TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=giPLZ39_gTmoWxaLQA9iEaVP70VbCcpRGejhA_9q_F0UEwevs3wFt99bOQ__wPABv3Za4nATfqffKWqgOY5qwQrt0e836uM-7lHdtrOKyLLMzDjVHeSjVwu_k7gTSvGtKsx1R7tBH4RXnzhhL9M6R4l3tokDDiG-lkXwtO_jS5M71q8HEntEIsjX4qWbJvv1eMlRc8PPlo13T3v_l5aX0t_Mya1Di0-Wm-qYQ6_h7dXjavJ8TM2Clcn2ksHujvVZSad0LPU1A3k39c5pVQXS_-hbFahZRW6N2Q8GLihVfFwFmsNjI5Id-DBCut5ZDIngJrTT1ylvo6HORc7T593_TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=fjdFyhScbNItPKZBzUHVgqQcZMh_Nps1eXVOPX4gb0Iz7w33Yqa08z4m2wLa_OiaQzJQOxIXtTGlcSLU3kL-kkeXoOJdef0lx9B1vnPcqbqst0n-wwzxOH8SUNOMNOPknxuLNojkEpGQtRLjbPOJmq1a0OBIGw6L7kAX51mIpR9eALQGxXp7ZJOjYQOgLPmlzQ19rTg_HsrjE4AH8y_ji1QoRQBihvYVRTBL15SXI_itBkGTT1jrhwCOTvrhyzG05V5ThLYIej-N3LX6Q4--Iv85Gp1JdbUdLIKVkm8ItSKYWm6z1Ze4Te4yIHkK_uEMV8AIWhIoW54-H2_kqlxhGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=fjdFyhScbNItPKZBzUHVgqQcZMh_Nps1eXVOPX4gb0Iz7w33Yqa08z4m2wLa_OiaQzJQOxIXtTGlcSLU3kL-kkeXoOJdef0lx9B1vnPcqbqst0n-wwzxOH8SUNOMNOPknxuLNojkEpGQtRLjbPOJmq1a0OBIGw6L7kAX51mIpR9eALQGxXp7ZJOjYQOgLPmlzQ19rTg_HsrjE4AH8y_ji1QoRQBihvYVRTBL15SXI_itBkGTT1jrhwCOTvrhyzG05V5ThLYIej-N3LX6Q4--Iv85Gp1JdbUdLIKVkm8ItSKYWm6z1Ze4Te4yIHkK_uEMV8AIWhIoW54-H2_kqlxhGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oh1ZSJaILmRSIYzbPjfklow6tsg0OukYRuf0bSPcBhbfaI8YABstkUpzqi9JHHKzdGauvYiLCLjmkuXj7SJHihLFtRiGsJLUDi7LqKJdsyplygjhnuMkMbfb1z1LTZgV-yjjPj7XwbupyQiwx6QzD4pStjAlS3WvmD2vqb3053rZUopjPCphXZNtmQVM3Dec7s_7ETIUjl3pMRL4cGb-zuYt2eT0rv1t6PZDk5SKuah_5dzThExcp_74p72EOMyV78LSPswm_Wb8zEsG3BumzkOj_5gUcFvr27LaXpmT6-VsSjUH9pzO5D6esUmKEWS05gTsqUV29SWPcTcvgy8Zrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFF115N1-2nIXT5KU0F7l5hbfS--ehxDYmRrncc5pll-Thtb1xySP4useMIG19S7RGktbejOsLwIj8T-2io5hxatbOEt_9KbL-XtBK3ZL24i0ihKtU7BnzXO1qK-2B3epgGCYfZMBf4EGB-B9sMGYJ_MeA6jLEn-4QsAVhXwOofumDnOVhxdKl0pzowkznsQ9cVH2sAiLccWAEqDS3NNNwf0T96UTXRiCRTOiyMd11GPQROH7iMPGVtHLvhhf26dM7wwAmZqo833J23NeykhzN-CNp71hVakTaNdphjKCXQxtEvpX2XjcV_pixM2a6Gzz1TR1PvajHTJCzP4OJgfLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuTH5r4WyKcsl77Yc4xQ3VoIyyCy3sL3ggABeBHlaa6MfXEv_UlOanff5V4lbXN_yskL71KtFW3ZfustSI8NcfFC4Ywkisk_RqRJIwaKdtRmF5M8IlU4iLksOSPITkXhB9eAA35bsv1t5Q05Qp1Q7exR2czGL9mifjDMrMo0LyizidkwGiP_zTZAFA5yWbeqtrYuoBQyUo-1HVAxIlvR6jcikcJupIrScf5XK25yA0wIWlFYMG9P-JQ4zOZjP2tdoN8ED1n0LmC2aLTyNvPvsXK1LSWbRp--mB4QsIb2tEeAvcHca3zXAvjHCj5EpZNb7pMZvHoo8VkmJ8XmPw1Juw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGb4ebVsgqM8ll4u4ajFt0QSoPkR2Sq9gT9m9dxiqtc4FCkNBH7Ggdwn32s8pfZnq6VfTEeuhm1JgaiLsnUU6onUT8Kqs2qjDEmmxlCezFGhjy83stERAxFy684eSf6I3FCqHECjRG3OcXwecVBRlvgcLN6rMyfEgaRpgP7Whu73yqeJ_v7gDaeg_knbxoCpMH-4nvXlV2n99tIA6C6aU-OSA3N7bxiYWFq7sIdFQ39_nw7OI3XmHhyDhfqNBs_bMgTMNbIwIEBTc_eAxE00SDjv5_E-DBktuPISmN-U5xhxD0Cr_5YxvqmrVUJ68KCdtJxJw3k0blYqPyH7Bwyhfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVzAfHMiHNIw5Ta28ewIQeSKofE9DfKPZ_TLSqnQlIe9chOw_eZFTivnLVAd2g6omdOxowpOQHSwiA-uv0d8Tf2yvpFLe8uK6CJPvt3tqjVL6Ay_tPrRJZ8Fuh_iiPLZvASFqc6kKT_pS7rX8zyoB3xU0IJjP2CIUewP5rxP5ySPf5xmC-hxbVBN2vtjqUiGOwAvxyzK0oJPPAHA84oXHTOSCoRG8Scp0jK8JnZHjunYY9E8vLa_qqf6HvxOgztEmfKALHgcVdzlGPy0fuAPpyg0Zn9xr_HiPOL0S3qiyZRBPYKMNMS-J7ES1v6FoU3jSkDyh-USQHrpLDFLouC77g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1Ru7gGRDHEPRUUyN8CxjhiRfNVVxdNr6LFR_0T_Wdu5_AeuscWQ5XlU6ymYZJN3dJk79tL1P_MYVCPsDTTUgYi8_LnUEvNP2V205lkrsJcFy2uzBXUbL334eQQncnK66EAntLSgHBlSHzbsVKjBzhMcCdkffalzkvUVpfXBPqNtdueBLrpvXDjEhAmkoNCho5dIP2xvkvN6E8VzhLhGUvdXrPXL2ZdwL1AaOe4OmNyzJkXcv1BlKtfo-OdNQEk1a7YR5PQksu40Npke4wqpjOt7hCtOaM9N6HSdeQGIQ1muUt5ro3HVxqlJvSzvbk2eB_DyVj6R3zTagYcpuBWFhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ha4jX0Jq9QxQfOG-X2e_VSMkWjIexbPyziv-DzsUADud4tMkJneNbj85swQyHPlKwNEKfSaLDxQE4UNUXG06Ual2lUmNhMlMLiS5NmCzFTOVKo9Tc-q598BVre1MOkDFLJh2vIEC1A7XT7OPc2wNcHpuMdEyORWCgDpKTHmKNlx8TpCt9OZQNB8-4VXKIIWRWFqvgwpPf0PjyMHuNXonZfXVUMDxe61aqV1wPqg9pmuxNGUoBK_DzmVkYAiqRupSnBt9iW2iYrOeZKEoMUyUE0GfLEAWmPky8qZhTqRsygXIE0P81o6hdCsfTAhbLY890daOr0uKY0m0V1_5sEWAog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkOL8yGeCKcuDYPDTpEG5EzkMVkBi_6M7WBDWwr8IsHE-oqxsc62269hipFiQW6C9AqgMoWGPcELVX-qbbeR6s0KwivqAl4PDMFf7QpTbLLLcQT3GkgSapya3jFcGDOGC-zn9sE4IT6teM-taDek4V1o5AVOAQoAUflr38CdWNYQI1_xKhwtlK_VeK3zg-95SPUwfP1k2I3dnN2Eo6zBmid9g-v0MzA2bRn7GwbunZ1Q50VvF0FPx3lz5ButwUm9g5xchaXXgKLERBZG7IWHRbyG6vBLMCTmZVwdRMmJDnvSeV84U7G5PNa4SD6Q3Wp3q6juky3HGVCLcpG0f2bfNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_i5ZKtpQTy58IR7cdAfWixgE1BfUMPpokaD90c7n79mCqAtWnaBo4eXlVLcCss0jqEaoCk5EC6gQQH_Xh9WYLybNcvyJDlG0CSzRqo7uXBF0uD7VWyJu1jvnIGpdlM3DPdimHh59aTQCBw3XZOMv5HQ5MLYqWhTw407111aYwNRXtAylZllQic7h20nvameLeiVzpVlfmZYaeXZW7K0_7r5vR6DHSIxaI7mz7f5MLmdXtdaEQc4OcmkRhh00YHZGZFKqM6HKMhyxrU9NGq0xOA-e6dxsFrjTzj6wL9t8M2SZKnmsTnp0epCA-8WNL4dFeYUchCp__RmaOjD-sXF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/deVUS_E1BrOV__ismX1XBqgbw3SGsPyZp6IyynHh9ow8LLOmtUOTpXXCKQzZifXRuEpW2-eh0A73Jk-1yMXqh6VrJsJ6RWzTK8UtrPYi-UkA-VODn_QvzGcuTGA78L00tj9n-LT6ClfVmVdCgIOIkUTg6VmwP3S1MtdJ-v83-VHemeLtF1BazB5mFloQdee6xkjhsjpoEj5Zi9GQecjS6LlaSh0_FTHvJ5amnLpwzZ7NeoL7EVdV-mvA65MYsQst2mGxVGU5yFz6rY5A2VwL3_k0ylHC-qTgWWTDid5DmaPqfISH0T-hRfjErmZQWsOhZbyM1GqP-BLFfdp7lWtRAg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=ZXyHWrJoZ_vbX8_3zJXYlW0Zz1CtoUD1pU8w9xNCg5TgaPXdoc-NYgtBi_e9m_kPeSpIHxnh8wf9mUYFRp71FP7f6I-hIHtr9ELE9WoMr83OEkB5Fw3y1z7IoJRYE-aAwUWiKN5zSZrvA3-6VYcmSKT0Mmn1wJQxa05ubZwqI4MPlVoZ7PvgZPW9C9yrHCqd5Mj8MNiLeQTZUdncRa-d0mQNPX0-eRnrpnlxeamg6xEiJv4g-Wr8u38Sz8m387F6h4tk-_JQKf1UNdozHDGeMj5mDfkUDDRjOTmSXyyV62fhwk4UGGC9W_NCwpsr9AB-SUbKZIGrKOgm1mUsuoDwzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=ZXyHWrJoZ_vbX8_3zJXYlW0Zz1CtoUD1pU8w9xNCg5TgaPXdoc-NYgtBi_e9m_kPeSpIHxnh8wf9mUYFRp71FP7f6I-hIHtr9ELE9WoMr83OEkB5Fw3y1z7IoJRYE-aAwUWiKN5zSZrvA3-6VYcmSKT0Mmn1wJQxa05ubZwqI4MPlVoZ7PvgZPW9C9yrHCqd5Mj8MNiLeQTZUdncRa-d0mQNPX0-eRnrpnlxeamg6xEiJv4g-Wr8u38Sz8m387F6h4tk-_JQKf1UNdozHDGeMj5mDfkUDDRjOTmSXyyV62fhwk4UGGC9W_NCwpsr9AB-SUbKZIGrKOgm1mUsuoDwzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYE3gZbwXTzmcatsMj8lqAPjB_k2mWyzUAQKtCPN2VnMk_WcCnGBbVv9HNhrpJnjW4HcvEUmDLwf-Wa9cdHK0v0V1o6_I6yimaGD2sZWmni80XesSh_j7KZKzbCqa3Zq30ym1SUI_GyVouwqB-wl1D_ZvE8QoYJwmSlxGCGivqIHClIM-bGDTSMfmAc7cLx1fn-Vi1S5TmWAbsudTeUaDtbWB_I5SKhKjBEVJZaTQnUZ3gEn6jAVLI_AeQHmjdgeUVd2W0s3qXIos0CtUllPLGEJDlVRLptfD7A5Q_y677AsbvI_MFVEw6-290-DOPccJnkGu0VIY0hMHhhaspBtOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hC5d-7SnhNdaONC3l-eRbFTj6sCPk2_AOd5NZ8wW9xtltKVcbx9S6dgQF7muDUchhAHGth80lNrccGaIqC2DsBUR0bHPViTGrzx_C_xpWf7EEwKJgHEEGJz046kRtqsQTFBbXipL1-s8eTsxwV5CqeIhCDegLvpJazWZI3bu-GnPYitVSsa1i3hG4nxFCtt1csyMvFNr_cVKGJsW91CxEUqH4qEyGa4Za5wNOQG_-Ems6Zg5yoJwmXHShaNYm_tjFDEU3hHsWASrojIkNx7B2wRyXbIAWy6PNJySbS8s6RM8Lf7Dbokl6lnqsTlUD4wss9-oq6HLctYZbomZA2vuaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=Pbat9k6Cx8bbXJfOn0CaxaHJPggTJ4jJwgjWXeAJyaMBfUbu6z3MOr02KViqEOkg5GbakIIaUT_he9S3EtOlcmMe2ZuoRX11C8G_hwdk2HEfdUr2FCtTmmODdQVwb0FD8nU8KTtlWro9fOGS7rvwML6DLGoP_yRWfdW3OXP0najiCcZa02otaU1HdhwNZGDSVvgabKpYTlXcJTIf0O_AZumeIV9VuU3DY36aj9eQxwZr00mxG13DHfBE9Ryx2E8oOcVz777Fq0HJT-fbLlcXlzQvi0uSwlrk71hXOowOWukFXraRQ6ucbQXBnAvEkSdY0RsuCWrGp4TB-NPhRe1Osg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=Pbat9k6Cx8bbXJfOn0CaxaHJPggTJ4jJwgjWXeAJyaMBfUbu6z3MOr02KViqEOkg5GbakIIaUT_he9S3EtOlcmMe2ZuoRX11C8G_hwdk2HEfdUr2FCtTmmODdQVwb0FD8nU8KTtlWro9fOGS7rvwML6DLGoP_yRWfdW3OXP0najiCcZa02otaU1HdhwNZGDSVvgabKpYTlXcJTIf0O_AZumeIV9VuU3DY36aj9eQxwZr00mxG13DHfBE9Ryx2E8oOcVz777Fq0HJT-fbLlcXlzQvi0uSwlrk71hXOowOWukFXraRQ6ucbQXBnAvEkSdY0RsuCWrGp4TB-NPhRe1Osg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=fkjIMDuS0dAW7gZUrUUfi4qr9aSiRLezEeuZEmU2eFJestGFRBa2aDSA9j6RrMs9FKutT6w_NBcoUHsHlNGuj8Kst1lKYSFx5mePMq9vO5cvHwUczVY5srowkzNarmCKG76NlFv-hSft5A6E7WPXe0HCUV7NjHqiJkxhwfQ8qB7si6NLfWduSypZkAcImL6-CEnwn26WV68UIuo_11lenTn5LkJ-JH8k2ZhQEWVEQeBc6FRHVS877rQ2TgOPiE_Sqi3PsD69Iwijfyyoc7ONgc2fhpTm0UIDUdkyzpHervIH3eridR72auBoc25ImsuGbkponity3I3PCxzOr7j4Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=fkjIMDuS0dAW7gZUrUUfi4qr9aSiRLezEeuZEmU2eFJestGFRBa2aDSA9j6RrMs9FKutT6w_NBcoUHsHlNGuj8Kst1lKYSFx5mePMq9vO5cvHwUczVY5srowkzNarmCKG76NlFv-hSft5A6E7WPXe0HCUV7NjHqiJkxhwfQ8qB7si6NLfWduSypZkAcImL6-CEnwn26WV68UIuo_11lenTn5LkJ-JH8k2ZhQEWVEQeBc6FRHVS877rQ2TgOPiE_Sqi3PsD69Iwijfyyoc7ONgc2fhpTm0UIDUdkyzpHervIH3eridR72auBoc25ImsuGbkponity3I3PCxzOr7j4Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXzB340xyX7TILMBYqcUC7CG-_gfqHYN68razAugMXd1U1b7QohkJewdjB1F-kShx7jLXUq9kp1El0-OZVbL98wQNQ2lDczwRBvGXH4LWx2JxpUmWqG7Bryhpsr3hUm5_FYtWcEGlRrK_tRvajxluy8GACVjyXhSfVAomEGbdwQmFV4bvc8UGSXvuvI7LTJtF1_87ApLr24BrLupjmMICRx_AVTaYAkr-uX7k_4L7JlSEHEmZWGQqqc8YuIE9ZLYV0QsSUI-DpHXaegCIYvM1C01DSCxdpneLQKiWbcsfWKodWlmaIKyg7ErlB8qd0riQWTQBnuYXHvUvW03E213Aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ij4u1ZFqdCKL2y1wJ7sdCgtmj_KRUYJY2SyIMmawCTLW4ZD9j7NJoBcyo7ki9eu4q6vdkl0lrsBZ8tyzlRhIOydHBnLP0q5Uk_sPFmpQ0x64yiq50-Uj4MEWwDnWlHgkO5fP_VMFQAk4gI75FshsiX4_haHX3rbXs65CGUhzMF4SGefmuCeezP-gNiYGZeSqtseQJVI5CCA6Do8cgn3o5TQkNeJsCf_UZXPMJkvCymnq2y9vMOkgLkKDHuu0dH8kZpkAlt5KZJNvcMzmkn2lEe43jUrOso3vEJFgCZSVSwm8dQyzbBEyW39jKt4KKO3lW3UssoJvXRPUva-AgposmA.jpg" alt="photo" loading="lazy"/></div>
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
