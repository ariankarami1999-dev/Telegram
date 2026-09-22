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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 13:38:24</div>
<hr>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOPBe-WsSyKP9b8iFJXu_j5PR_0lIEe2k50pJqHmxjEnlwZ0j94YJGCBG2XZ_m1-E5lIzS-uCEoSAwIqZByjdAtrURxa4361C-j0MHwVOYXc5RHqG5rGl7Nqk58cUP7HiiAmnhLXXhu7jS1wv0McnVMu37vavKH4-rLNI7Y8D81vO04kCcgI_JAejI2Mi2CdGfcTRRRsID6hnDCdvP19ub6N56KEtCwDrDAoeceEfqjYB_EF3YKLkB-FZW5OlDzcmSRzlOveJDK5k_fi52cSTkfDG5YrnnSg0LgXDVg9XtIxKe6YOuSHD_9JrBKpkIrDglDkCtl6QczjuIODYlnyIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=LDIYgDe9SuUlCqlp4ieWPN_CY3E4lTBLfeZFXxLyvHD1Xq_8XjL6StcVXkeVZK_TiSjck6Pj1RXUW9exYO4s28dQt9yO9O8dCVDCbH6OUPA8sHNK2lmQ800ir9ddmurt3NpaEGAgcZGxLB0DqpiRBolhVBC9ankB5LNWhLBuvTjejP90rURznJOE6aIstUf9KDGaXHg6pQiR1ZmEWfuwLova3puwOLe38ozr6HuGPCRTdAWvZ4LTB-xSEqM08_64yCA2GrIBM_UKaXjZ8k2ZoVC0HtoePXGmYpP_DJ3Kz5VaACC-FaibA8TsBVYG3YvGUIA6tpvn97jUYo9WZL3I9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=LDIYgDe9SuUlCqlp4ieWPN_CY3E4lTBLfeZFXxLyvHD1Xq_8XjL6StcVXkeVZK_TiSjck6Pj1RXUW9exYO4s28dQt9yO9O8dCVDCbH6OUPA8sHNK2lmQ800ir9ddmurt3NpaEGAgcZGxLB0DqpiRBolhVBC9ankB5LNWhLBuvTjejP90rURznJOE6aIstUf9KDGaXHg6pQiR1ZmEWfuwLova3puwOLe38ozr6HuGPCRTdAWvZ4LTB-xSEqM08_64yCA2GrIBM_UKaXjZ8k2ZoVC0HtoePXGmYpP_DJ3Kz5VaACC-FaibA8TsBVYG3YvGUIA6tpvn97jUYo9WZL3I9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHX55iI1BW81CKqZcPQdfvzGIWvggqSmU1nk8jeRoAUMzYhE-5I2VOOA1GdJboNet7osvVQAMU8CRVh2-FALND1Kj40Gj4HmQnmz7d1GEJhoyivyTjT4hCOzwFO80UOlf827nJwtFPk4Jw35-7Vpcx7MKoGvsicib76ISJ_WmEd9RFu7bjr-9b97TphtKgt454P-HL6fYokpBvwo3hD5mzVoBJUcEScCaySZVkjgwYdgYKjbE622wtMJkZxebVsikUKWuW6sQLpa5vj_DEFB8OoHd6YUdY49b722YpiGC80j5LyUYJSOU0i_dUo3L9yej4CCNDtRsr46gYvIgPFszw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=ARPRWX9Wj0TsmDf1-MN8c_EKsxPJAdqoMIEav8ezaij96uEpcGpwdnuWoLiyXqThQ1uHF4PAHlLujhTP4q6S7LJTAveG5rV49tJMpblJfrgOPsT2Us6rDMGBMB646sGSlWqQ3t0HAi-IneXWiLmArDpuWAdhmsPDKMErooFUvdby2ylVMWTdkMX9MourW_Izbr9HpuzKRkFc5-I0e_6sl1a9LgosBtCBQdmvupzg0dNwgZCwHt3dkDMdW-xr7R0bxN4kZM9fDx3w-eVEfUjwRtgBgRs9GWbHis8thHngGFIToViMdEldezxuds-3WQmRZeaug4g6-4PBBz3-rikbAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=ARPRWX9Wj0TsmDf1-MN8c_EKsxPJAdqoMIEav8ezaij96uEpcGpwdnuWoLiyXqThQ1uHF4PAHlLujhTP4q6S7LJTAveG5rV49tJMpblJfrgOPsT2Us6rDMGBMB646sGSlWqQ3t0HAi-IneXWiLmArDpuWAdhmsPDKMErooFUvdby2ylVMWTdkMX9MourW_Izbr9HpuzKRkFc5-I0e_6sl1a9LgosBtCBQdmvupzg0dNwgZCwHt3dkDMdW-xr7R0bxN4kZM9fDx3w-eVEfUjwRtgBgRs9GWbHis8thHngGFIToViMdEldezxuds-3WQmRZeaug4g6-4PBBz3-rikbAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmGYFcw9RaxkLeQGdNG3fKATIesq5DCXurXTquc-iZX8cjL5_VEjDiettKKBpkVZ4ZBKlN7P8a8Qkgp2ClqC2ZuFDJv65BWxKkBDaTb2H03XJTXDrfzW1TTG4mXTIQ1OMTthjcMl9wR_JHQaajYFaKnvXBRrpFnIrX2Unu_LJS2ORWXNRGAeuSVKwu665BeyrfKSnWD-tBgHiE1G_siFIjnpkXztaR650vSP_zi40LFhgkWUHXADoM23lbUsfj5VFHyoJlhoukAZhFKQbCBrCKS5APvsPcAyJDagkOvdGo86ntt4AJ7icJZbqRH96cWnv0JuxPKGQWEwK2e_0Nvckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdKPbzmEErCTZFwQ537AKVvhAwK4aHTUBymfylAZL9FIkB51zy8Ffgaw8Bcsp2e73mcAQpJt3c9RiIDvp3Go7_p5Cliq6octkCxfdSxKOekhPeOM44WUx_UdpG_vVagg_1pE-w5sM-2WYgRYjIZTJCsXBwjVLFZhg8oE8TVHQmh0AAZPdTUN-7sPRRQV8rhz11SKd4QEnxxsXExn6_GnhUr5ApoYcT6FDsvHNxFeLQbcOMSx3b8qS3meQyUs22fU1rrbLHaWAIwNjKKRwcEATB6gj3Or2I848nGUJMxYucUlDb1jh0JIOrev_-Pu2Qf4oXsIMdErD1h_x4RW6T_gxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuw_dOgwK_dcNNTqSZoDc8yED3Y5rceeKhZf8192YNAUfZAr7eRmZf3wD6FSgkVtEuqfCcDTetJqCIpYNJsM23vVH_r6_WHP0yXocY7ulPup42Vm-4pj8grNZBTVALlhLOMvAWdYsIT0xidwoi958oLB1uulOIhVoCMGPBf3L_wMLipgJ7w_PBSt5oDhBwJUwR_mdbqAXs9vuvWB38aa65FPJpXoNZI6tsF8B02zZwcL_zUq1f9g8XJjqTsR6I-NW7KkSgZUxALaI1aW4dvItrZNYOQFoId7lFGOY3wGoEOjg2qjwE80PxveEios6zWJD6QwREu_pCZ3xHvhCMb_HYSc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuw_dOgwK_dcNNTqSZoDc8yED3Y5rceeKhZf8192YNAUfZAr7eRmZf3wD6FSgkVtEuqfCcDTetJqCIpYNJsM23vVH_r6_WHP0yXocY7ulPup42Vm-4pj8grNZBTVALlhLOMvAWdYsIT0xidwoi958oLB1uulOIhVoCMGPBf3L_wMLipgJ7w_PBSt5oDhBwJUwR_mdbqAXs9vuvWB38aa65FPJpXoNZI6tsF8B02zZwcL_zUq1f9g8XJjqTsR6I-NW7KkSgZUxALaI1aW4dvItrZNYOQFoId7lFGOY3wGoEOjg2qjwE80PxveEios6zWJD6QwREu_pCZ3xHvhCMb_HYSc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=IREeQp_K4kgSexANmeAwpW_BGqpSf0FOTbXXjLwsl8e7k7omcx7rGhEP8aPvB2XRgsK6T2yrpAgWdRqLynokVjFbargY_VOobt44Qj1eurBEDHxQlvjH61pfkhnBaskPPN1PhN6pQBU5ppU5-t-Q0YiweHZkX3wFd5-pObykIbFEcluRvDJ_GpCSVvNArjfzu_xd47MD2WJaD8jES4OKpsFi1c6TKvziSSv-wWyGb7WWhX72vaXurUh5mracDtmz-q2lJTqt9OSLFBspGaqi9AsAZtv_kguf9n1IP9k0qAzlWFrEWytfwniADnxhyx3YqpPPUeHazQGm8okG2f7D-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=IREeQp_K4kgSexANmeAwpW_BGqpSf0FOTbXXjLwsl8e7k7omcx7rGhEP8aPvB2XRgsK6T2yrpAgWdRqLynokVjFbargY_VOobt44Qj1eurBEDHxQlvjH61pfkhnBaskPPN1PhN6pQBU5ppU5-t-Q0YiweHZkX3wFd5-pObykIbFEcluRvDJ_GpCSVvNArjfzu_xd47MD2WJaD8jES4OKpsFi1c6TKvziSSv-wWyGb7WWhX72vaXurUh5mracDtmz-q2lJTqt9OSLFBspGaqi9AsAZtv_kguf9n1IP9k0qAzlWFrEWytfwniADnxhyx3YqpPPUeHazQGm8okG2f7D-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=VxDmUleXkPFctZLbbzFEtHPkPJbrSkK9CvQ0nJ_VM1QORSn_MxeZhM3d4ybGLeH20dPAmrTBNL6EhQehnD1d_zl1a-sM0jogtGhTCWhARyI66dMjhabCsMENKTO__laXJVQ8dOhSVUZ70p7hL7qBwsQUXNECCkFEJfqvZ1B7q8is1VuNrZXGn-fvflGSmC5xW8cmo0eT5Snq4swMTES9VNFG6Gbwer7qC_-ljHwVLu_XvEft_dzuyrK8TEaEMGqdQClKQDn09j77PRjJmVgDaEmPzkao-AGMZdJKgPNlQTdx0_tlOUwslUbpvpabZuToljwlbLj0PCWCAMVD0qvP8SjgbYvpMFo0FRriCnJxlNpIBond3FwTPmPsh8F9p1INDtMOXLQd9boAOPXc-3b8VyUQ17aevn-Qi1Y4hr571XBTFxJjhkm6yZttTtPFiMBuMuNkqikco9LGFjjxZbH1O-jlCatzHr_fvYXbC7EgkK7WGlbiCNmIC65QYGF7KBULrPz2ZzLVrFy39wte3EoL889yWQ-wQxQSTGTO-0iP7eSPB6hrj05VEMNEHjDTSGShj5BvUzsXV_mNxHwcDzMy6ap7VMC9r2Dh6EEpaw_P-pXhhjNZZjVlonOpcLVsirvZDzIil5god2POnoJn7rKlkvMuUMp6VONGwr0YhjDkV_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=VxDmUleXkPFctZLbbzFEtHPkPJbrSkK9CvQ0nJ_VM1QORSn_MxeZhM3d4ybGLeH20dPAmrTBNL6EhQehnD1d_zl1a-sM0jogtGhTCWhARyI66dMjhabCsMENKTO__laXJVQ8dOhSVUZ70p7hL7qBwsQUXNECCkFEJfqvZ1B7q8is1VuNrZXGn-fvflGSmC5xW8cmo0eT5Snq4swMTES9VNFG6Gbwer7qC_-ljHwVLu_XvEft_dzuyrK8TEaEMGqdQClKQDn09j77PRjJmVgDaEmPzkao-AGMZdJKgPNlQTdx0_tlOUwslUbpvpabZuToljwlbLj0PCWCAMVD0qvP8SjgbYvpMFo0FRriCnJxlNpIBond3FwTPmPsh8F9p1INDtMOXLQd9boAOPXc-3b8VyUQ17aevn-Qi1Y4hr571XBTFxJjhkm6yZttTtPFiMBuMuNkqikco9LGFjjxZbH1O-jlCatzHr_fvYXbC7EgkK7WGlbiCNmIC65QYGF7KBULrPz2ZzLVrFy39wte3EoL889yWQ-wQxQSTGTO-0iP7eSPB6hrj05VEMNEHjDTSGShj5BvUzsXV_mNxHwcDzMy6ap7VMC9r2Dh6EEpaw_P-pXhhjNZZjVlonOpcLVsirvZDzIil5god2POnoJn7rKlkvMuUMp6VONGwr0YhjDkV_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=FDfTo7-jJTMQJ16Nl3QLVWiT46pN4zJDHsoAGXs3qzHxyw-YYbvGtIL8MS-Voaywx9AwrH_kjqV9H6HxrbYp519mNyxEqYBVsq_UTsEW9kvwzqvDAWqE-y-kDyUNKAF3XLTEvudFd-dGp3Xuf-wE4cKFRZTHx9hfZ_-1gSun3iOaEftmDN1SxFmHLwoetPTB4OElmf6-gkjcwtUbFqdaiw-55WvV39_ujURKChGdTnAVkL06Iix6gligTrO1DOHK8XYtWMKL7w9H5hmaGa0S14gjCmocT-GmYtfetFc52dmjgJre7NOzMxSSNuaRUH8iSrAoPInM4QvLdMB2BIoVjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=FDfTo7-jJTMQJ16Nl3QLVWiT46pN4zJDHsoAGXs3qzHxyw-YYbvGtIL8MS-Voaywx9AwrH_kjqV9H6HxrbYp519mNyxEqYBVsq_UTsEW9kvwzqvDAWqE-y-kDyUNKAF3XLTEvudFd-dGp3Xuf-wE4cKFRZTHx9hfZ_-1gSun3iOaEftmDN1SxFmHLwoetPTB4OElmf6-gkjcwtUbFqdaiw-55WvV39_ujURKChGdTnAVkL06Iix6gligTrO1DOHK8XYtWMKL7w9H5hmaGa0S14gjCmocT-GmYtfetFc52dmjgJre7NOzMxSSNuaRUH8iSrAoPInM4QvLdMB2BIoVjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7C-NqRdsHsWewsnRwfWRxGfzyQJ48jXukAPP-bhtbgZYD0AgyKjpMClIggUhhE3Z3sqNJCWu5LyP4FNP_K3_ICl4H2f-jBqUWP1BeEtjHNv3-CNxo1v7KWD2m5qKB-VTGBxdHkQWXUnv_gB_TheE-QN8KrBmaNM7QHk-RqDQSw_7tLv4qdR2c4z_WZENJnp3AGS1P0zshZfVIJ0_uakf7LcP3LgCIQdDZH7hofKIse2Z4tBaEuyjPngs6tRaDcU9fsDvWxQGzfmpOTDep-l5u1lzToyZBt_r89oFpPy4FjX8SQyHjLKKbDI07T2vsgnTqIfuwYflCht3FkFuHTPNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=Xo__Jeqf_bKSHLOwAnON9ZEe__ZOtBZXHXD5kaEqN_4A1ixpq2hNfUmPA4QyTbL6VPKKnReXu8A9leBP-ADb19r_O8_TIooRFk0EVwMFKev47W_mqQIb8rmbpbeflbg-h1FJiKL-7F-rJI_AxOAGrZUlzzsTgpSMas2FVFb_B_GfYZaKeZbaOR0IZYWvpCVmAq0XTCoK3fKPiwZbG9lbYz-vif4onZbKAE8elD0YVrHI3V1TVzwFDtk8PKENzqQJTV1s5VR2vxM81bc0O4CgIp_5fWGQLaGuLFefHlCii_GmSeyqQl0CiyswgIsd3GXQF-frcNP2b28VozS-roI4tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=Xo__Jeqf_bKSHLOwAnON9ZEe__ZOtBZXHXD5kaEqN_4A1ixpq2hNfUmPA4QyTbL6VPKKnReXu8A9leBP-ADb19r_O8_TIooRFk0EVwMFKev47W_mqQIb8rmbpbeflbg-h1FJiKL-7F-rJI_AxOAGrZUlzzsTgpSMas2FVFb_B_GfYZaKeZbaOR0IZYWvpCVmAq0XTCoK3fKPiwZbG9lbYz-vif4onZbKAE8elD0YVrHI3V1TVzwFDtk8PKENzqQJTV1s5VR2vxM81bc0O4CgIp_5fWGQLaGuLFefHlCii_GmSeyqQl0CiyswgIsd3GXQF-frcNP2b28VozS-roI4tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=k44JusPgbE7CiIDamDRg_26z_exzJHvVZjeRorgutw-hUM8YZqJOXv4WYwiT_PaflQ-G5xBmb7zmhAH21wPob1V_Ar7Mp2dIwadcTu467mxbcD0pSPIaS2DayB5qTKxCCKC7cAc8fqusVWrTjw4ZGSzVLxyoTKNacjrFKaxy2pMUoi52fwX7Nr4jSxaJAoEnTU0oRzWUFKviONytzOxvJBNcrWjl2jr82aTGncNLajOIe3FIhawn5qhAMxwEf8NT6QMXdc2CUAq1CUouz0mOYJSapCagMuaN2TzPe6aDfKZcvW-hSi_WWVXt92Bjns7kwx8tkA2-CFxFaepqvcJVAUVWT-7-0aknMMrg8CtvnrqH3ZK-_pX3OkeNXSEFqGPPu7FSvhzbz1UpIgEWBJAUUJgDaHJbC7FD_mHMiP2jN-0rog7_3VxIvgAnPHng6mU0CLXuuzOXJ9eXvaYEG_fSi7bFPKu15fziQ8-XukP32cNFIkcim8G07vmbp4UqATmcEMthsYhvqDTmV-AEzXC4wZ_oRBRtxw8Gh03q6wx0kDCi_YwPBXyUpe4Jzdv52bxlu4nzmFBfiOdOIHXDHGP_VdoWRmR13m6JznzkyW_h2mddo1JENUS-KLY1fl1U3NPGAVCgsOhgiEX34OjHDORFl4ArTxjbJMCKOY6LXUcAxTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=k44JusPgbE7CiIDamDRg_26z_exzJHvVZjeRorgutw-hUM8YZqJOXv4WYwiT_PaflQ-G5xBmb7zmhAH21wPob1V_Ar7Mp2dIwadcTu467mxbcD0pSPIaS2DayB5qTKxCCKC7cAc8fqusVWrTjw4ZGSzVLxyoTKNacjrFKaxy2pMUoi52fwX7Nr4jSxaJAoEnTU0oRzWUFKviONytzOxvJBNcrWjl2jr82aTGncNLajOIe3FIhawn5qhAMxwEf8NT6QMXdc2CUAq1CUouz0mOYJSapCagMuaN2TzPe6aDfKZcvW-hSi_WWVXt92Bjns7kwx8tkA2-CFxFaepqvcJVAUVWT-7-0aknMMrg8CtvnrqH3ZK-_pX3OkeNXSEFqGPPu7FSvhzbz1UpIgEWBJAUUJgDaHJbC7FD_mHMiP2jN-0rog7_3VxIvgAnPHng6mU0CLXuuzOXJ9eXvaYEG_fSi7bFPKu15fziQ8-XukP32cNFIkcim8G07vmbp4UqATmcEMthsYhvqDTmV-AEzXC4wZ_oRBRtxw8Gh03q6wx0kDCi_YwPBXyUpe4Jzdv52bxlu4nzmFBfiOdOIHXDHGP_VdoWRmR13m6JznzkyW_h2mddo1JENUS-KLY1fl1U3NPGAVCgsOhgiEX34OjHDORFl4ArTxjbJMCKOY6LXUcAxTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seBcqgwSr4wVmd8u97-nla57DQzOidltKz4kaogCBn6zZ6JNPSO-k-AB-iCUCvtOeJs50GOfOblM0zpU8rox-N8c5brJdBYv3BWRDt0UUC9b0gV_FIMODpW19XXCtUAA1mEB1p23OmNs2Ype3M6mBCMOQFbPRbtq1PQ0mun09lMo54dHgDenQqCLgYWCuw1iZ0XPYDoh_tLv52UcIRZTJU-dgwhIM4c8X1wDmbJ5nNARyfl_eXmmSUAYKV52urn_7xzugRw5QLZN01ujpAes9CfLgVjNpGcHOE54-BM6dVDSmcjy4Rt__ySwYEn8S2LDr2jdkqWmwt3YlgJNJoOTVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=PhNTVRjprPA7x3NI8oooDGb5IU04-vZE_0weumFxl22MD4rOFqfU6WHn0Xct91UEao51K-GNbZafEKq3CEU-B4S8ejddj8uLyb7AHKe6jBflrO8IijrsE-7YBOxk1XKtd1JVUlM3MtWVp9DI8nQfMM12baKNlPBLN_on93wqOiAL3jseg5UflMLb1jffVcdpcj4kxqLU3xn8DCSJCFM6z-PYnk-vr_FGHsnkStJ279y6VaSm-2yBGY4hxvzTG1Qi032hjdSn9WXFOtz6qrpF0olEscih4RZ_th-dOznPX3p6GptwLMjBoSwJLFzAswYqojUer08zvA_sbKpQbhVaeiB4uOsDBGmlTQGox7jM3lnmQMrG_kBFqOn4SvSGRnFQsNhgk9IxkZ7pvjxXJ-M2FaSxnlxGCOuUHyWpBgl34awPE8HWhG6cFm4iOqoeypTno88H7nfARM2G4P0UMOtOgPk9frnj2-g4VqD1HMSFfRB3PAJzN0ctwSG-7zvg2lGf4i4K9_YyjVdc6F0kaQsH7_kBvlYD7lZMYGb3ovaFjwC7stdxrlpCvz7VUkASjI9UpdJhZ7uDnY26FrhBca1PZbu8tEpwwV4SVs6Db3BiFL1-PbBdgTtC_AgNTBW1n68c_zeUpw89Hxt1ZxKq-SxXmzTFXT9XEVhiFUeBYjZe-n8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=PhNTVRjprPA7x3NI8oooDGb5IU04-vZE_0weumFxl22MD4rOFqfU6WHn0Xct91UEao51K-GNbZafEKq3CEU-B4S8ejddj8uLyb7AHKe6jBflrO8IijrsE-7YBOxk1XKtd1JVUlM3MtWVp9DI8nQfMM12baKNlPBLN_on93wqOiAL3jseg5UflMLb1jffVcdpcj4kxqLU3xn8DCSJCFM6z-PYnk-vr_FGHsnkStJ279y6VaSm-2yBGY4hxvzTG1Qi032hjdSn9WXFOtz6qrpF0olEscih4RZ_th-dOznPX3p6GptwLMjBoSwJLFzAswYqojUer08zvA_sbKpQbhVaeiB4uOsDBGmlTQGox7jM3lnmQMrG_kBFqOn4SvSGRnFQsNhgk9IxkZ7pvjxXJ-M2FaSxnlxGCOuUHyWpBgl34awPE8HWhG6cFm4iOqoeypTno88H7nfARM2G4P0UMOtOgPk9frnj2-g4VqD1HMSFfRB3PAJzN0ctwSG-7zvg2lGf4i4K9_YyjVdc6F0kaQsH7_kBvlYD7lZMYGb3ovaFjwC7stdxrlpCvz7VUkASjI9UpdJhZ7uDnY26FrhBca1PZbu8tEpwwV4SVs6Db3BiFL1-PbBdgTtC_AgNTBW1n68c_zeUpw89Hxt1ZxKq-SxXmzTFXT9XEVhiFUeBYjZe-n8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=p30ADqx3c1-CyS4tcNcQ-qtYI17zh5fluLwYABRTE2l58BKB1fCEC9e4fFjk7rdkA_lTumanBwswkc7j2Ap4LUu963A9Y08Cc_V6RNuxS3fsEpr_Izxr7H9_oiR0UkRQD_uNKgjuit2JtRKU768iraiuWr3VLfotAduivWYtpYEY8inuPMFlhePI3HItkmP_fW7N3oJ0UpkxKoqS8tZDnHbD0Um9r4-eS5q0eOuM0Z390RNvkZ41e5FJxoyKyUQy2MmXmtdE4xaF9aBoeD5aEZX2G3BKw2Q8I6ZAW2EDjxBZn2by4m2WUB-mvqaXXxgxBdIlPQXG-qPfShm879TOI4tK40M8NF7y7V2G3mR0g1YEdfukyooBTKFpLzhgCouoTbl2uiuxp6soui5iI0tlzWJ5brvpU2etsFiYCzSj1zYhsqFTMTtAqTI9CD438psSBCorL1ZxrbaaXEGP87kIOcyMZU4xZWHbHOyXXCJE_p6RKXjPYBh_LxwRPx6ANKenJ6ZoUh1SpcxJ-GyyRMicw_9BOO08H15d9KZDv2lhgEnBfXLjvFIUetviNoEbBKdfrta86AM17kNRGXTEbe5dcs6MsH5UUz_tQCsSfL78y4pSOs6WUQ3yqSvYLRHT8vcQQqBSAFrnmBJj3YLCOGi2wFJi_zOJBDtxqAmlh81OXfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=p30ADqx3c1-CyS4tcNcQ-qtYI17zh5fluLwYABRTE2l58BKB1fCEC9e4fFjk7rdkA_lTumanBwswkc7j2Ap4LUu963A9Y08Cc_V6RNuxS3fsEpr_Izxr7H9_oiR0UkRQD_uNKgjuit2JtRKU768iraiuWr3VLfotAduivWYtpYEY8inuPMFlhePI3HItkmP_fW7N3oJ0UpkxKoqS8tZDnHbD0Um9r4-eS5q0eOuM0Z390RNvkZ41e5FJxoyKyUQy2MmXmtdE4xaF9aBoeD5aEZX2G3BKw2Q8I6ZAW2EDjxBZn2by4m2WUB-mvqaXXxgxBdIlPQXG-qPfShm879TOI4tK40M8NF7y7V2G3mR0g1YEdfukyooBTKFpLzhgCouoTbl2uiuxp6soui5iI0tlzWJ5brvpU2etsFiYCzSj1zYhsqFTMTtAqTI9CD438psSBCorL1ZxrbaaXEGP87kIOcyMZU4xZWHbHOyXXCJE_p6RKXjPYBh_LxwRPx6ANKenJ6ZoUh1SpcxJ-GyyRMicw_9BOO08H15d9KZDv2lhgEnBfXLjvFIUetviNoEbBKdfrta86AM17kNRGXTEbe5dcs6MsH5UUz_tQCsSfL78y4pSOs6WUQ3yqSvYLRHT8vcQQqBSAFrnmBJj3YLCOGi2wFJi_zOJBDtxqAmlh81OXfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=Y7vuKrhJRL-q24DkdUplA96D1U6iOoTatleTOD-75pOdtHnkogGxQ8uNdoSd2-fit7ccXpxq5Int3Un6q3A5eL1RnmyIhkgRh04iZbIF0tAfvMnyMdcxONDo3gQm6D4KfuZv9VfveVC4fk9A0LrNyeUJQ8SOR0lniswtiNfYVzCx6GZm1iUvcf9z7RezCi-o7jrmP61tcFHgf-tZF55NAuEOwpDARZpF62rGLowK6no1pldPYQVTqx6Xjo2LJxLYd9bjt-MzE1T2R-9mT66qKGX7vA3lmbmdEoPFrC4cumLvY8HzSlLEZc3EUI8FNhvZkI2O-PYfHRtAUZB7m9e_3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=Y7vuKrhJRL-q24DkdUplA96D1U6iOoTatleTOD-75pOdtHnkogGxQ8uNdoSd2-fit7ccXpxq5Int3Un6q3A5eL1RnmyIhkgRh04iZbIF0tAfvMnyMdcxONDo3gQm6D4KfuZv9VfveVC4fk9A0LrNyeUJQ8SOR0lniswtiNfYVzCx6GZm1iUvcf9z7RezCi-o7jrmP61tcFHgf-tZF55NAuEOwpDARZpF62rGLowK6no1pldPYQVTqx6Xjo2LJxLYd9bjt-MzE1T2R-9mT66qKGX7vA3lmbmdEoPFrC4cumLvY8HzSlLEZc3EUI8FNhvZkI2O-PYfHRtAUZB7m9e_3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=OBSdMhjuHBnOIifbEmlTVLTwkJK6IFpAJ5FHmAmn4BG7izwE7i_l2uqTRx_CBc552D2x89uWx5oVf-UjHMKD2yVaIdJ1zGgh58t2wllJiNIEub2_XYsgRexdoXKlU8jYe7n8hNSvYJrLDWM5TMlr98Da-b_a_PNYnkSrW1TgWRVJ7T847rYc8pmZLiNTldwQD5Pka-yJF4Rk3SA4eXxWhYYq96YfrNOYrBk1GCyw0Dr74nwTM4tNDylN0UB8Bv9EIFudq8-9v114iX0-6s-5eP5gOJrpzIuEX3rZAK9OFL11InTdncY-j8psNo_8L9FxRzuNOhhHzya7ZbMvoQT9-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=OBSdMhjuHBnOIifbEmlTVLTwkJK6IFpAJ5FHmAmn4BG7izwE7i_l2uqTRx_CBc552D2x89uWx5oVf-UjHMKD2yVaIdJ1zGgh58t2wllJiNIEub2_XYsgRexdoXKlU8jYe7n8hNSvYJrLDWM5TMlr98Da-b_a_PNYnkSrW1TgWRVJ7T847rYc8pmZLiNTldwQD5Pka-yJF4Rk3SA4eXxWhYYq96YfrNOYrBk1GCyw0Dr74nwTM4tNDylN0UB8Bv9EIFudq8-9v114iX0-6s-5eP5gOJrpzIuEX3rZAK9OFL11InTdncY-j8psNo_8L9FxRzuNOhhHzya7ZbMvoQT9-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=AhmGzvuNS7iMoUzyY6-89yOQ5Bsaodp84a0tXVss9rk3gTQ8NL5yQcqUd0ZmtWkfYcnO-yQDyiwvSD3-l-trurjD3g0rKl1MSs1KWd_3lRFmNQ7aSKUeRuUycoDbBXQMcLQ_V9E_G444ouJfnofHKLHwD0aCNSR1q561WOg3gOy21BcTYZdj_pNMrMVTJSkji2UTFrHw6w-wMbai1Ien3KdgT3FRqeGGkizL0tjic51twhiDwpG1V1wXpoGAMDh0VdJHVnyRpKHdhFqj543Lh27TOOAA-PFH2kv1xFu8m3gxR9ABilNGByV9pmx7tq7vouT5xgHaPkBShq0vtP4Huw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=AhmGzvuNS7iMoUzyY6-89yOQ5Bsaodp84a0tXVss9rk3gTQ8NL5yQcqUd0ZmtWkfYcnO-yQDyiwvSD3-l-trurjD3g0rKl1MSs1KWd_3lRFmNQ7aSKUeRuUycoDbBXQMcLQ_V9E_G444ouJfnofHKLHwD0aCNSR1q561WOg3gOy21BcTYZdj_pNMrMVTJSkji2UTFrHw6w-wMbai1Ien3KdgT3FRqeGGkizL0tjic51twhiDwpG1V1wXpoGAMDh0VdJHVnyRpKHdhFqj543Lh27TOOAA-PFH2kv1xFu8m3gxR9ABilNGByV9pmx7tq7vouT5xgHaPkBShq0vtP4Huw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=r1lY-4dcUIK9Vs9V9yBlPooPVwcSgksDTVjNjl4-dalNjMpDgsSQ26pA7PkOmfq5cKuZhcSzJHnAB6ROss9lv2Sgo1rL6k37lybZBFFhZmhylMWlahxVPoj_etCkGkWal0sTFHgxW5eMHClohahpWO2t8gaDrIa8h-GHAtf98-DgOmG-A7TxFaeOHYANb8OS3mStjAitlLsEn4WjEpepD4Q1zw80xAZcIFRiBwOiUwYeYr3_h3pVO4LGYfPLm57Pf5B_g_ZnOYD_xSxkUyGtkS25eGJ1vLNni5mxY896ybl4sCMjr2humZ8gzx07H3dey_UGxnZD2KmIn2sVPul_qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=r1lY-4dcUIK9Vs9V9yBlPooPVwcSgksDTVjNjl4-dalNjMpDgsSQ26pA7PkOmfq5cKuZhcSzJHnAB6ROss9lv2Sgo1rL6k37lybZBFFhZmhylMWlahxVPoj_etCkGkWal0sTFHgxW5eMHClohahpWO2t8gaDrIa8h-GHAtf98-DgOmG-A7TxFaeOHYANb8OS3mStjAitlLsEn4WjEpepD4Q1zw80xAZcIFRiBwOiUwYeYr3_h3pVO4LGYfPLm57Pf5B_g_ZnOYD_xSxkUyGtkS25eGJ1vLNni5mxY896ybl4sCMjr2humZ8gzx07H3dey_UGxnZD2KmIn2sVPul_qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=RZ2IG5aBjg_UDPzHHtEFMdKZhVbjn3jC9LF1y3qTKyaSPWTyVZ8oGIquups9HwVTu7y5AmUiCHf9h0nul2cjVjKSuqok3ChCNFdubOyJqy0qJ4KUn3Oj1mP5DN1QkKOmY6-XQl6FUdVszyvlaMZi_WTJwqycKV_OOxLOPSBMYHlraqTmhCP23OYNXXsCZ3dnYBehf5yp1nWVhRiikSiiOiv36Kc0FT8V1yj-z7nhuuVk8Ks9z_bkchTdVrBKrSQYPWalj7J53E4eIFP3bS6vFCDiKiB41vpx3y57ruvDl4gX3zkYThCeDOSMSSaBx0NhiPRoOz0Zy7vFfrMiUxoh4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=RZ2IG5aBjg_UDPzHHtEFMdKZhVbjn3jC9LF1y3qTKyaSPWTyVZ8oGIquups9HwVTu7y5AmUiCHf9h0nul2cjVjKSuqok3ChCNFdubOyJqy0qJ4KUn3Oj1mP5DN1QkKOmY6-XQl6FUdVszyvlaMZi_WTJwqycKV_OOxLOPSBMYHlraqTmhCP23OYNXXsCZ3dnYBehf5yp1nWVhRiikSiiOiv36Kc0FT8V1yj-z7nhuuVk8Ks9z_bkchTdVrBKrSQYPWalj7J53E4eIFP3bS6vFCDiKiB41vpx3y57ruvDl4gX3zkYThCeDOSMSSaBx0NhiPRoOz0Zy7vFfrMiUxoh4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=UqG94GlPVzeyLKEfBsnFHVj3rdFSbuBc6KtLL7UQ3KitVzwQfjv4pLvjbdKvtfYIcyhlidtySf2pBU7uNNgoUa92qklcBomLzGZL1cxricDsHXulok4b-9_xaChLOwPzbWXM_66XbxIwTngGlqAapqBIj9abw71hGs_LHuDJzTEIbhT4IwovfHPiUfTUf-eNyoIY_BctihU2ndp7RndAc-HR_pNSCJhytzmoouaquR5Uan5h8L0coX2yYA6ueixiUiE-L7BB3tK-E5Zqp5FsezRfTJyj45jmQMtHJZ37MSs9FvjUygvtTt2CuI9NCEoD7f8omBvfdZ4F8c0u2Ip35w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=UqG94GlPVzeyLKEfBsnFHVj3rdFSbuBc6KtLL7UQ3KitVzwQfjv4pLvjbdKvtfYIcyhlidtySf2pBU7uNNgoUa92qklcBomLzGZL1cxricDsHXulok4b-9_xaChLOwPzbWXM_66XbxIwTngGlqAapqBIj9abw71hGs_LHuDJzTEIbhT4IwovfHPiUfTUf-eNyoIY_BctihU2ndp7RndAc-HR_pNSCJhytzmoouaquR5Uan5h8L0coX2yYA6ueixiUiE-L7BB3tK-E5Zqp5FsezRfTJyj45jmQMtHJZ37MSs9FvjUygvtTt2CuI9NCEoD7f8omBvfdZ4F8c0u2Ip35w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=iQ9bm_PsHlKYb069GfFN63Xl4dUhFTymIFVQdRdlVolBRzyxdYTutsM7VdqZ05A34Yf3rjW-t_21vtn8wTbttzLjjCwCIyTdcGnHt5S-dusgXBTvhFzuYtkF8GYI9kX5jbO3M1HeshoXet7kwrMCcIgy14hhzD9c1MhTxONE7h1cUTyGIvEdLMg9NoKryi1DvkVPdJFCflcL3B_09H0eJCxpCAfiKc87FB5-OnMPTogYCBW3IuuDfkTxTXKzn5T4_pN7Z2Ys0vkIYtDHO_FyLjlAPZX8ices8d2Z86Xanax5Yo__NuVun7YND-5kvUPNOPLECIMeLO4g4fqvzWC5IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=iQ9bm_PsHlKYb069GfFN63Xl4dUhFTymIFVQdRdlVolBRzyxdYTutsM7VdqZ05A34Yf3rjW-t_21vtn8wTbttzLjjCwCIyTdcGnHt5S-dusgXBTvhFzuYtkF8GYI9kX5jbO3M1HeshoXet7kwrMCcIgy14hhzD9c1MhTxONE7h1cUTyGIvEdLMg9NoKryi1DvkVPdJFCflcL3B_09H0eJCxpCAfiKc87FB5-OnMPTogYCBW3IuuDfkTxTXKzn5T4_pN7Z2Ys0vkIYtDHO_FyLjlAPZX8ices8d2Z86Xanax5Yo__NuVun7YND-5kvUPNOPLECIMeLO4g4fqvzWC5IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gbj9pUzs-PVamza8ui_-HPlds8eucgnZwGkUpW7LSB021-BVoxN3hAm7IbzOos766RPjh0YeGmkht8XNAfpD0zQJQF_oUlkaq9Aw75CCvA5R9TLwSbhgw9lnGM0HTuCsUT01NeWg4RTITgNwYiO8SnxgolyG5sqT98jBGYJMpf-pjrDS--xS3rg4dJtxQ7LaZE0IBOsJVFaDxaH2p_AmMf1nKsWuFq_cBhpUDGNhD6v0u3CEFN3Zn8fhP8ldCeXhhTmENetp39AEg2X4bgSRT6A9Bpejg2QwOzTZcGqFk1dAr9TOcLUhibCG48krLpMitigehPYYXmizBzIUBRC7Og.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=X2QZlgiUpKxLXHZ_iLJ96_RVE2yxErUPeBD2V6taYVdsAAefI5D-YNmHY38b2Vwv6cuSDPtSUToSR4HPQhQ5CBy3yPXRYzKo5PO9vHQ5Tb6ZUMZlopa1BWYlGevei5xO16MkxXlOXtWYQjBo9dAzTndLYRq_6SVoTj_D5-XIZmsiBeFHJS3WEk-xL67gZRWufWNR-d2AJALjPaofkQMwbIH2N71RW3mqdlNSO9dGM365lKFz_l8FD7AoicYOcRj5abgowg0BvmunAbxbFZMnP2FU5JpWpXByd2egIqPNauqdwF7NDIG2tOxJVDrrnFf2uGbqqoj1q-Bp-j336A447g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=X2QZlgiUpKxLXHZ_iLJ96_RVE2yxErUPeBD2V6taYVdsAAefI5D-YNmHY38b2Vwv6cuSDPtSUToSR4HPQhQ5CBy3yPXRYzKo5PO9vHQ5Tb6ZUMZlopa1BWYlGevei5xO16MkxXlOXtWYQjBo9dAzTndLYRq_6SVoTj_D5-XIZmsiBeFHJS3WEk-xL67gZRWufWNR-d2AJALjPaofkQMwbIH2N71RW3mqdlNSO9dGM365lKFz_l8FD7AoicYOcRj5abgowg0BvmunAbxbFZMnP2FU5JpWpXByd2egIqPNauqdwF7NDIG2tOxJVDrrnFf2uGbqqoj1q-Bp-j336A447g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=FOs_DNcWgLVkKBboD6r4YLb0H5bnnpNJkHCU_e3dKB6wDUpeJQX7b-cT6YlC6vFQccLCXDNOOvlKqLPehQL5CLfhkLBefTCzR3J2gshBWHAmCjKC9Dc1ZwE0n3bSV5jMTG7mPhNzdZIYnqk3FZsSa04pBte-qVrHUMYkGIICM4FJIFtHYg5eWmJLssdVMABkHEP6s8-jYzoIvG6siELRBizC33sce9iwUldU2pn-eibNmrQKZxs2G-Ndshg6WMpGlXszt-ndpbOXVm6xjTtTfgBs0FIFK5sIJEhDQjbEywA9b5J2yNB23oakSDC_eca3cqHuAr6E9mACYnWU9HV7zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=FOs_DNcWgLVkKBboD6r4YLb0H5bnnpNJkHCU_e3dKB6wDUpeJQX7b-cT6YlC6vFQccLCXDNOOvlKqLPehQL5CLfhkLBefTCzR3J2gshBWHAmCjKC9Dc1ZwE0n3bSV5jMTG7mPhNzdZIYnqk3FZsSa04pBte-qVrHUMYkGIICM4FJIFtHYg5eWmJLssdVMABkHEP6s8-jYzoIvG6siELRBizC33sce9iwUldU2pn-eibNmrQKZxs2G-Ndshg6WMpGlXszt-ndpbOXVm6xjTtTfgBs0FIFK5sIJEhDQjbEywA9b5J2yNB23oakSDC_eca3cqHuAr6E9mACYnWU9HV7zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=R6KS7CGgzJ7lPlMLZiZ6tTuFFTx_4LR10iEAybi98bo3kgCxjNRmPhhb8_MSrmYeVZTSPmA04u5pY2_1fn0vLcLeIEdPtgO6fequf4nMnXG4XbqA7hnws3SwVs-sSCW6brzpK_mJvNXujiFOzpcnVDUaBMN7csRj3sn6XtUkWLKPDTXDWop8ukKYZvMznZZgVIp-JQwlVNZt_EMR8_sapT3g-RaI4g-iUKBZRGw4cIGi5Sb-kMSP9agkw-4yaZKunTdYfLciZpEXLAstd_eHTMsjZdkelhPty-ZiRz_ik_5KORnyPqwH7Vzo2vjIVP5ui0TOygZa-GqMf3xUXPtl1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=R6KS7CGgzJ7lPlMLZiZ6tTuFFTx_4LR10iEAybi98bo3kgCxjNRmPhhb8_MSrmYeVZTSPmA04u5pY2_1fn0vLcLeIEdPtgO6fequf4nMnXG4XbqA7hnws3SwVs-sSCW6brzpK_mJvNXujiFOzpcnVDUaBMN7csRj3sn6XtUkWLKPDTXDWop8ukKYZvMznZZgVIp-JQwlVNZt_EMR8_sapT3g-RaI4g-iUKBZRGw4cIGi5Sb-kMSP9agkw-4yaZKunTdYfLciZpEXLAstd_eHTMsjZdkelhPty-ZiRz_ik_5KORnyPqwH7Vzo2vjIVP5ui0TOygZa-GqMf3xUXPtl1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=DpKjFi0OYytWSvKEMcEWDCmU28rAWfCF21uCIb-BMmCJWP3lZXKHE45NhGknpoYmVVYJg_qa92rm_qmkQJ9jcR1QPNvsZRqTQGlZ1hpZlVt3z_yOwtX3MLk5b6qUHLhFaSIATxQYJ26lu5O_lVPnpXMjh54iQ-5EwLNMWau-eVF69vuRte5L4EVbikTmduuntUuHnIeXh8_s8BhHzdv36xpEyixTZSFHlCV5M4amJ-hEN14ttqSkys7RBXh7m3K6roSkEqty_QfxRAGrito5U5V_w3IFXngr0_BGoUW2sGV7IzDgn7qE9JNySI9_KW2fIQVVSIODaMApGRVmAvb_lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=DpKjFi0OYytWSvKEMcEWDCmU28rAWfCF21uCIb-BMmCJWP3lZXKHE45NhGknpoYmVVYJg_qa92rm_qmkQJ9jcR1QPNvsZRqTQGlZ1hpZlVt3z_yOwtX3MLk5b6qUHLhFaSIATxQYJ26lu5O_lVPnpXMjh54iQ-5EwLNMWau-eVF69vuRte5L4EVbikTmduuntUuHnIeXh8_s8BhHzdv36xpEyixTZSFHlCV5M4amJ-hEN14ttqSkys7RBXh7m3K6roSkEqty_QfxRAGrito5U5V_w3IFXngr0_BGoUW2sGV7IzDgn7qE9JNySI9_KW2fIQVVSIODaMApGRVmAvb_lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mW-nsIng5OyzbW8kV-bzj6Ue0B7-eNYnGmMXANMq4hSF-lA2jSc3THKwIgIrD8qzw1hDrTtu5XLYDe90kANpK344FLejZRWWu_hgG2efBb_USnGn5iMyWH3xjkfh7ZEu_K6nLzgnzqxlGBimIFKSGzhgOADgBaPC7BXIINzqT8NesdfP14YvlvIPBWtRbSk3RIIgRIPVenHnRAkJj9BNQspRriB0tItH6TotbqrJukHb0qqzeyYsgw17ZQBxRsiAE7K9odWetWjUwtY4GTCmXWQZI_m0yNI2Srx2of0XlVAD3XcHksvA7pwqNYB0EGZ-dK-mZM3Id8S0uyD05isEJw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=dN646UOGf3OjNW3Webzc3WBjQHVVZdEbhSWrifspOEfDJEF1whDpoQ8dkHAQ2KjQr9Qn3_D-C-SfI6INIvbwuGvy8dpADAzHUAtP7PbNZK1t_oR7mpAOQt5-0mZH5UzMxWxPzKy-Sw7Z2bZaVE7jA_bq6LMxAxDIs8TQtPGH8y2rLl9hm34aZy-lEZXvdZigYpBn2xnq-Qf4u3hyHuQsJCtbfGzMGAuH6S9JnPP_X3GcxMjHBSerGz0leTi-T7B9kOJoSyb-hluEy3_SMZh0OwU7_6F7A4Fm-aOFNS-O6ldc_L_LQCip2yusG9RfyUp3APsVGQ4Un5slVZwwl42xJ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=dN646UOGf3OjNW3Webzc3WBjQHVVZdEbhSWrifspOEfDJEF1whDpoQ8dkHAQ2KjQr9Qn3_D-C-SfI6INIvbwuGvy8dpADAzHUAtP7PbNZK1t_oR7mpAOQt5-0mZH5UzMxWxPzKy-Sw7Z2bZaVE7jA_bq6LMxAxDIs8TQtPGH8y2rLl9hm34aZy-lEZXvdZigYpBn2xnq-Qf4u3hyHuQsJCtbfGzMGAuH6S9JnPP_X3GcxMjHBSerGz0leTi-T7B9kOJoSyb-hluEy3_SMZh0OwU7_6F7A4Fm-aOFNS-O6ldc_L_LQCip2yusG9RfyUp3APsVGQ4Un5slVZwwl42xJ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=psQhNzlVthg7jzkeyV0cxZrW8T4UGTjHzCv9S3D84Sd3eHLPlyoLN9DRPH1C_p8YM_d-omJssgCP6XfCpqCt4ejrH2_N9Lv-A6PAJ9u2oY2fbqd3q4f4qji-wwLDIJem8lfDzUyTYuHYzxrcgPiXhC14wbDGln4ztMpd27Cg-aR0KP-vhGMVdb2tCixqw2dqzLIxWavEvEf2aOq1C1UBAVrKv5b0eqxLZo1Z_pYgSqxUUQsI5xReUh7g8FrMYd7KwDEl1nW0qytguW04WPPbSISP0pihjM26dXghL8-zufDSO-FJ744fU83w6-5k7eHwKhVXy3XXQf6VSr-NXabg9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=psQhNzlVthg7jzkeyV0cxZrW8T4UGTjHzCv9S3D84Sd3eHLPlyoLN9DRPH1C_p8YM_d-omJssgCP6XfCpqCt4ejrH2_N9Lv-A6PAJ9u2oY2fbqd3q4f4qji-wwLDIJem8lfDzUyTYuHYzxrcgPiXhC14wbDGln4ztMpd27Cg-aR0KP-vhGMVdb2tCixqw2dqzLIxWavEvEf2aOq1C1UBAVrKv5b0eqxLZo1Z_pYgSqxUUQsI5xReUh7g8FrMYd7KwDEl1nW0qytguW04WPPbSISP0pihjM26dXghL8-zufDSO-FJ744fU83w6-5k7eHwKhVXy3XXQf6VSr-NXabg9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNHhoP-wztsrvtnVypJHbKh6PseyyxHpAAOhcKexR5EzpnpynXluSt-afTXvpq8svq4tUTzWtEkVnTqjJe8unhQ9xxg-10b7JP5ECO6GZSAXMxtVVem-JYqL9xeXxLawU_adIbapxOa9U_Xw8RW0IP14fAwIXddM78Ed0NrXaEegCvsNVjASO5zm_7tk2Gnu0wd8rIEoootpJDLTI_36F1xBGw4wJWckDEv2r5vtQ0O_WODQvpvvOqnLri180ZOeyKhfUcD50KKY5U399uOHcCBXJMiOu-nqpTGkUaCvExq3T8bvXrmAILMJoIpF-HV2AcRFv0N2-M89Udff26WkGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XoxCfWryyfLo-D4By3Mqkl2LU7ZvltcsJc2ICRecUcXS0d7W3mfWYKp5rTieNArtsbtt_Gm0ADc8yLOP-wOXOmLrfv7U56Shl-x_TYPKKA-ru89mM9wFd2RgYNc34ZyNqD9hqRQXkZG9l7PLalKEA78rz-JcSmWa9437Ppz8a-092RKjbPgB0LsgjnsRMjKgVNuwHOsDz27E6D8CmjFulckSiz_iP24fJWo6vlHVWTTaaEHVb8lOcSk6DAoflkX9L6qnRjLck8S3RZPH1twplW5Ws9EWuXLxLlbgnLEET5f5ODJOgdDorTaBgo2O1ipl6S5S_UWxuVV-_nDbys8moQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=cRa6DST_exvmK8mSRRj7MtLSLVlgXSajZU0EfcMZBy61_cYjZhyX6tRt0E6PvxES55O-MwM7EEvpjS0FlZMfoVWjM0sJKpYnfzgx5gn8vNn-ekEW1cWvz95UDyVp9eZsY0PLF9drKZcd2B9bUv7XFc8qlmRADz3uz3wflCDPFx64al3bAJO135rwuh41Zkj6s5coWuGKgAt0yWH0Km4OmGzL0j0YXhjO2anPLcdal9pUYhwqzvmPj2NfqMVBNSwHOWLvPGVy_tMyiUoDNHiO86eLyI5fCwPIN8MBTs4SPhYEr3zpXmdDnAZ3mpVjBy88Tj7CUD8Uq7kM4pnA68gy1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=cRa6DST_exvmK8mSRRj7MtLSLVlgXSajZU0EfcMZBy61_cYjZhyX6tRt0E6PvxES55O-MwM7EEvpjS0FlZMfoVWjM0sJKpYnfzgx5gn8vNn-ekEW1cWvz95UDyVp9eZsY0PLF9drKZcd2B9bUv7XFc8qlmRADz3uz3wflCDPFx64al3bAJO135rwuh41Zkj6s5coWuGKgAt0yWH0Km4OmGzL0j0YXhjO2anPLcdal9pUYhwqzvmPj2NfqMVBNSwHOWLvPGVy_tMyiUoDNHiO86eLyI5fCwPIN8MBTs4SPhYEr3zpXmdDnAZ3mpVjBy88Tj7CUD8Uq7kM4pnA68gy1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIQT7bJmFL_NLuvb4iLvHCQJkk0tflvmlpWciMPL1ilxxVGnKZ58FATKD_S1FR0Mn8s93ocnakAU5N5GjoGNViAbuuLYrlPZCC7Aks-ufJI5pUl7BXhtSwCIo2EBYKCdsjSZkGQGM_kZraOb6AnKa7pZoeWEePaRkOITU6q3tWttTcEo2DKOV802OUj2GhuxVC5zvB-e_Hayt5SpC4W7vjKSrUEiDNJZqrUK5o3yFbFlNup-S8LR-lTRCfowR6F9s86IlE4cZuO9LIVZz5Uem8gK9ngQpEb75-aEIIROElwZE4gNQm8uh5uG5-bUXs8i4W4vz_OmWdkCGVK2lmEw5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgsnnB-XBc3Z6BsTehIOaCusVthDk9xik_rR7LLusJcygmErOtkWpM5M82c1W-6M5cXBNOf24B-LdB8EHOYUtrsT4M5qPsIAABhvzwQC1EV-TYNhwHtgCdaFF42-inE0hHRdNucf4gdYCZKSW0Ged5jmrEKWXzKM6HbMZFiUi5pVzUHOf2GH3pBmq1qwvouSTA6MryC4yn1Jb1jyuFM3L82qGabjE4zJ5oHQhsv0Ldt4swkEVJGKYdaIdcUo0ynHwzasvZrrUFb1QHtsnsoqzjoFHHTmjQLWk0OiUsd5aj3UUGCkjOM1GzlMRtX-Lz6gHKRjnlKzSlB_-MsDLB5yxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6G4sLgoyJEG9aRrMOuI5kHHBeR2KdITqwsdty6GUURHhSJzfPCQ4uyoh-kGWs-UTcpxFV83ptzGZAcaFll6cuMb1Z70_nGwAQLNw0faXRoa0khlvCxm-0v9PHkU-ZeKEuShnUUDcfH8R1I5DggnFb5USZVRVt0DWg8P6Whq5V14WPeKmzPCg44zIFIuGe7mFe9ZSeSuRuVYGMcnUGJvqzhIgEm3zEYYvlGhmGgE2LOpuAgOBgVxwuNOgVZq-dtJMOxpc_jO6RDSLe2sszM3u2NFPtuN9NSDNL23YTtzwGDKI9Mx9Kwkx_9wYnMDjbUDP9gOHdsFaL8a-ulohj6Aiw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=Uha4-O4S0Ze-OHtSv7yA1mqxY_avjFdXI5hW9haCieVUhkM1mIHm5jqMfInxRZG9Ig5krNRXEqcLCoQds-PxA2GR89OXsxeMGAjFIkTrCXwA_oygkWxfmflhKMeQ9nDrzqW4YIovaw58VdFaEpBGi5TMG56MXEo-v7L670Xyt79wjamIcEwz5Uo-x33-OJp64xXMV6lJ_P2_KWHccEZ6me7xoiN9KPi7HuHsKoNI7Hl5EYQBVqM61KiEsrIWJJ2wKsRANxq9E1rPwdikEEvzST6jhtv6MJcwb6_q-sGmtjobV-5beH05PWn2PE7YADUZccsLvyUrf5qhTfRRtbocnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=Uha4-O4S0Ze-OHtSv7yA1mqxY_avjFdXI5hW9haCieVUhkM1mIHm5jqMfInxRZG9Ig5krNRXEqcLCoQds-PxA2GR89OXsxeMGAjFIkTrCXwA_oygkWxfmflhKMeQ9nDrzqW4YIovaw58VdFaEpBGi5TMG56MXEo-v7L670Xyt79wjamIcEwz5Uo-x33-OJp64xXMV6lJ_P2_KWHccEZ6me7xoiN9KPi7HuHsKoNI7Hl5EYQBVqM61KiEsrIWJJ2wKsRANxq9E1rPwdikEEvzST6jhtv6MJcwb6_q-sGmtjobV-5beH05PWn2PE7YADUZccsLvyUrf5qhTfRRtbocnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=RbLN5WKxsvxWi7h4uE5tBmk-YejWrt3Jjiwkw-XL4VCqSiG42aJ_w2cE2p6Cth0nb3XFsujxdSmOb_BSVFtbdhhfViB4VvUhZQ5iBuc8Y7dkvxtjzrOPrbBP4YjvfO1vJPPfS18l7m9cD1Gws-ra7CPATDPMV0Zs_DMXSyqDPceq-IpoaAMmg0Lfmzlc8C14vvcd2KnsvK468BHddLxppji0uqhSS0sCbpSn_smYDWa4kNBLKh3Fgjm1IGM_-h_VSbKr-73hnxID0ofC3JNKjeGU-oKrFb1g2w9KsDLtxRUFlGZmA3r6d3eE7rst_ZHMC5L1x3GWpdY8Fcinrfwxpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=RbLN5WKxsvxWi7h4uE5tBmk-YejWrt3Jjiwkw-XL4VCqSiG42aJ_w2cE2p6Cth0nb3XFsujxdSmOb_BSVFtbdhhfViB4VvUhZQ5iBuc8Y7dkvxtjzrOPrbBP4YjvfO1vJPPfS18l7m9cD1Gws-ra7CPATDPMV0Zs_DMXSyqDPceq-IpoaAMmg0Lfmzlc8C14vvcd2KnsvK468BHddLxppji0uqhSS0sCbpSn_smYDWa4kNBLKh3Fgjm1IGM_-h_VSbKr-73hnxID0ofC3JNKjeGU-oKrFb1g2w9KsDLtxRUFlGZmA3r6d3eE7rst_ZHMC5L1x3GWpdY8Fcinrfwxpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=C0orcmkxvPCSS6dbQSfQrYxphpxsK1s8g9MCGTyNKRJxa6rRcLHf53bW7okzcOI3tknQpLjCb_NeIk7yr_zLPUlY5niIh_3oIyj0-lTGoiRG_z-uGkBOgz5YEZvaUYKgzvWhr5vTZEFai_aPqk_mGv6A9w-E0WFJwcC6GaQ4imDw0lHhMVfuzYYVXZmPMMUiTVfhy7oGD0ytEiQygD6Wu5qOlttzCvr51gniuxksdXKNiGQnqY6IdwpiDb_z7vRf_f72Sbi8_Y5B2peVA-HQgM-qKVBfaqv8RE6wI_zJd2fVA_R2RXa4RXReOrnB4GGdgZ6eRiZZxDBlHRhkrCEQfYuizJ1N_O6T4s3XftwUcytG7E1lhziN-bS6va_B8mSF13coabsO6Hu-eobua2Cu4tGaeJKS18jxH8Ld8Q31n46p9eCWsuE0qAbYiXWlYuqh8YJ30LeIdEdQ0BCAWdeXlMUlgmLLIa3lPkaDtpj5Gz5Fs7vOQ_k7K39Sb-yEw_kVI0LDsrO01ET0QJi78fFfTuF5kua7jOgG3v9ZGzhlWbsyJaUXHPbbLUk278rDxJZRqE5KCLmYXjVrT0wAWfmRXPKKGurFmW4dkU20s4JYbHsmHhdX1XmZE2faaKfD3EL5z10v1CVq0v1ig6eL3sB5TAHPTdK7pbVdUlnMEjPQAHU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=C0orcmkxvPCSS6dbQSfQrYxphpxsK1s8g9MCGTyNKRJxa6rRcLHf53bW7okzcOI3tknQpLjCb_NeIk7yr_zLPUlY5niIh_3oIyj0-lTGoiRG_z-uGkBOgz5YEZvaUYKgzvWhr5vTZEFai_aPqk_mGv6A9w-E0WFJwcC6GaQ4imDw0lHhMVfuzYYVXZmPMMUiTVfhy7oGD0ytEiQygD6Wu5qOlttzCvr51gniuxksdXKNiGQnqY6IdwpiDb_z7vRf_f72Sbi8_Y5B2peVA-HQgM-qKVBfaqv8RE6wI_zJd2fVA_R2RXa4RXReOrnB4GGdgZ6eRiZZxDBlHRhkrCEQfYuizJ1N_O6T4s3XftwUcytG7E1lhziN-bS6va_B8mSF13coabsO6Hu-eobua2Cu4tGaeJKS18jxH8Ld8Q31n46p9eCWsuE0qAbYiXWlYuqh8YJ30LeIdEdQ0BCAWdeXlMUlgmLLIa3lPkaDtpj5Gz5Fs7vOQ_k7K39Sb-yEw_kVI0LDsrO01ET0QJi78fFfTuF5kua7jOgG3v9ZGzhlWbsyJaUXHPbbLUk278rDxJZRqE5KCLmYXjVrT0wAWfmRXPKKGurFmW4dkU20s4JYbHsmHhdX1XmZE2faaKfD3EL5z10v1CVq0v1ig6eL3sB5TAHPTdK7pbVdUlnMEjPQAHU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=nG_9Mx7M_DzdugbUByHbeaYbab7gA6zEntChG0kI3HYNI7DA86hwvVZr9KXPU59H4tPNLpyLq4aQ3UW9U5j9J8wt3AwdFMTinOtLQjr-Mj1OqzSgWl405qJQXBXcXXAf93bsr-Kf5H0dT5tjFZDj66r1edeTkUixKYo0ZfOrI2kyLHPJ6mbimcOw56b3vC8VQnJzeLeupqYyuLdNXY4VzDk3OjOOB7HUMrFwdHQoPMSJZKDwOYaa2IZCW5amdmf24JF2_Z8KAbV-_1FbA0AiWI5CGmgB7QWASjK1R4wPLDZ8ga1Tvp1xp__7ZL4tUeCj7snAvCLxxiFdTyY2qZ2DCjFpuVQD5GwPm7fzyczpIQtihf-SF3J2zWRpVTQ_jl2pKxY2owjU_N-HSLzVuIVJ3g97yvwxGMEpPkomIIyWPqM-8RPbrvxe-04lDQXdQn99v8X_bKUipQXeX8XJ8rtzQ7C-f2CIJQZCfdnXysvGHEqap91dndqjWkzO8LQEMQsvuPopjBU5pv8C6HRqnSHO21LbxS0EQOxsd-pymDZ7uEemEcI9-EUddOjM6aPTK1QhzyY7MBlt_eIn00CzZdl-3NJZ_ohtNCC4ByMKEVTyhnbl6vXHeOVjf9AReZyRY-v-LwjaV51uv4pNuwl9Ud0Sxzn8WeEoVTIZn3jOwFxPZPU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=nG_9Mx7M_DzdugbUByHbeaYbab7gA6zEntChG0kI3HYNI7DA86hwvVZr9KXPU59H4tPNLpyLq4aQ3UW9U5j9J8wt3AwdFMTinOtLQjr-Mj1OqzSgWl405qJQXBXcXXAf93bsr-Kf5H0dT5tjFZDj66r1edeTkUixKYo0ZfOrI2kyLHPJ6mbimcOw56b3vC8VQnJzeLeupqYyuLdNXY4VzDk3OjOOB7HUMrFwdHQoPMSJZKDwOYaa2IZCW5amdmf24JF2_Z8KAbV-_1FbA0AiWI5CGmgB7QWASjK1R4wPLDZ8ga1Tvp1xp__7ZL4tUeCj7snAvCLxxiFdTyY2qZ2DCjFpuVQD5GwPm7fzyczpIQtihf-SF3J2zWRpVTQ_jl2pKxY2owjU_N-HSLzVuIVJ3g97yvwxGMEpPkomIIyWPqM-8RPbrvxe-04lDQXdQn99v8X_bKUipQXeX8XJ8rtzQ7C-f2CIJQZCfdnXysvGHEqap91dndqjWkzO8LQEMQsvuPopjBU5pv8C6HRqnSHO21LbxS0EQOxsd-pymDZ7uEemEcI9-EUddOjM6aPTK1QhzyY7MBlt_eIn00CzZdl-3NJZ_ohtNCC4ByMKEVTyhnbl6vXHeOVjf9AReZyRY-v-LwjaV51uv4pNuwl9Ud0Sxzn8WeEoVTIZn3jOwFxPZPU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=IiooMR32rXW1Wdo1T1KZ1varoyiIzrSIKRNh2VCsel9F0GU2If3j7q_jfi-AJNIn_nthtQzfYKT6gaQzszjxjqw8kKskCPNhC8XjLtO9LHq1O8OZ-EqiHmiT5meh1-8sqUIAHI4WO5x0ImBs8H61m65AayepESF3eo-SP4rZcydNjCUzHZszdLgvKcpaJECCQqdDFJWFPmbpYbo3Xn0NDl6kWBHi4InuCnpGpPP-GZ0Zohgwb-8jjZwU_0CQEdCWYPnlvPUbyBpwPZm3u0sW5kOiFu2toX-m41cqpyXQTVfGAy9e7FKn-R-7DUJkaVOGm0gPYemV6q4nZ_Mv5BCjhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=IiooMR32rXW1Wdo1T1KZ1varoyiIzrSIKRNh2VCsel9F0GU2If3j7q_jfi-AJNIn_nthtQzfYKT6gaQzszjxjqw8kKskCPNhC8XjLtO9LHq1O8OZ-EqiHmiT5meh1-8sqUIAHI4WO5x0ImBs8H61m65AayepESF3eo-SP4rZcydNjCUzHZszdLgvKcpaJECCQqdDFJWFPmbpYbo3Xn0NDl6kWBHi4InuCnpGpPP-GZ0Zohgwb-8jjZwU_0CQEdCWYPnlvPUbyBpwPZm3u0sW5kOiFu2toX-m41cqpyXQTVfGAy9e7FKn-R-7DUJkaVOGm0gPYemV6q4nZ_Mv5BCjhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHjJPhn_Lf42gvM3LZ7iXib4zq5h-cweto63753cExAoJe5QcL2IoM0RdWlW4bkpd7WfxtGP2p5rNTjBeOxy0bsyNGtsuzoUPXkVLkO0b1S7SQeWf7Z635NOjHBeRq3xZ0DGeTjv7OCfsRyauO00PVTfV5OKEaw5ah9CnFrzii_wXedlepQRPueORXFsOm7KxaBVd9mb0FgmFL6M6p1E6VCpAeymEENPrr_I70INw6Jab7j9tHdJBpjbeKHavZeaZObTp-3h1BqQToC7eK7r5PO2YT2qwanzQdGqYQdpDsk1ohtD52hBcQUzz2KsCYs6hYzAv2qhWeYQ_nQFyehuGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=hYp4PoGMEbNJYAemcxBxFy2M89qPLGcza71Yt5QPLgT_ljk4R6sumeR2V1LARauOMfquQYnOSnX1yJPNnu6a63XshpEX072KfVaQtBeRgBFYRVQXeNJo1_SlZIsSiYWN0nuYOPGcpSvc0F7FpKwSn-tRQglGmPr9FQ7ctS-fGZgzh45d14vtfmPRBmRGIDeB7ug8gB_ZDqHQ36rmMbtJC5oMqyNNuRgNuBXoP9Rr4pFepFHDo6M2-2KhVaNIIFFV6wa0rhlSbAtSn8lVK861y4pzkBI7g26hjiSpI4HnpgV_Rr88CMUH0sQC5eA1S0br1BO6bYUcjpvvOpA-Zmmetg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=hYp4PoGMEbNJYAemcxBxFy2M89qPLGcza71Yt5QPLgT_ljk4R6sumeR2V1LARauOMfquQYnOSnX1yJPNnu6a63XshpEX072KfVaQtBeRgBFYRVQXeNJo1_SlZIsSiYWN0nuYOPGcpSvc0F7FpKwSn-tRQglGmPr9FQ7ctS-fGZgzh45d14vtfmPRBmRGIDeB7ug8gB_ZDqHQ36rmMbtJC5oMqyNNuRgNuBXoP9Rr4pFepFHDo6M2-2KhVaNIIFFV6wa0rhlSbAtSn8lVK861y4pzkBI7g26hjiSpI4HnpgV_Rr88CMUH0sQC5eA1S0br1BO6bYUcjpvvOpA-Zmmetg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=L74gpmiZO1tMMyMAoWvwhme0FldzJxih9KcwLCmn--Pys2bdF8wRa7-Om5YFfz5UFDo8FPtJrC2mYIKJG0HFVlPxqWFcX4bq0VGJe9ecfMVVDAsS0-YvixN3C6ATiwg7IRG-uJq9d9E-mGV7dm8eEllPZMaav3PTUELFHjCNIqzbjGRhL4x3yXC8HESuHK1Moetgi0SnUun_eaIubp2K9ankWAdTjRcoAKXldTaZndGTJq3nFdc3yPDXl57zBbEtK6uyiXb0jyOaDUOL8LnKAfM8v8XoE4rFA2YcbjAY_uD2u12ED5cBPSOvpa-ZZyKDmw7CZRlTroxm6_2Y4h6dtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=L74gpmiZO1tMMyMAoWvwhme0FldzJxih9KcwLCmn--Pys2bdF8wRa7-Om5YFfz5UFDo8FPtJrC2mYIKJG0HFVlPxqWFcX4bq0VGJe9ecfMVVDAsS0-YvixN3C6ATiwg7IRG-uJq9d9E-mGV7dm8eEllPZMaav3PTUELFHjCNIqzbjGRhL4x3yXC8HESuHK1Moetgi0SnUun_eaIubp2K9ankWAdTjRcoAKXldTaZndGTJq3nFdc3yPDXl57zBbEtK6uyiXb0jyOaDUOL8LnKAfM8v8XoE4rFA2YcbjAY_uD2u12ED5cBPSOvpa-ZZyKDmw7CZRlTroxm6_2Y4h6dtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwMKWUEwoalcImFnOZdoVeClpetOY0od579j7PAP3AYfDRmPqtIxNLvds7oLwVW2mJDqd8csUa45lmBgb9ztQ2j-0NeVLr9kTIHcIwJcKS9nKknJKDG0Et74HIuRKEQn2H7CWp5DKjvbjgKOUbPYmvwEDDy-kphEeMIUEJgi1cHBSNKCyTD__OW7A4xlSV3oaauROaOPrseyJOmdFcE2j7Kj6-9F4J6wvbThpSV-g-VhgoessHOpYXN20Vv1hbFTuyWsErnGtl6baYh46IzU7v8nIrAiE40eZYowO4d48MGM9XoLtTsQsAtO4MXIoVTB9ImvVdqTE1k5QuO0Xm5cRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgZuumoJY28kTUjIUXAkKQIRPBuqMjBLOt1wmVAr3fGWtkTP1hH_gx2ULfaY19aAVBSLu0lKac0XDRgbJrFpNf49GgkjM-4_983cUNPhETV1eey4dfjWCSezCj7SJS89nsjK4p_WzQUcR-J5qKwiDOTXByChKIZMqWaJ9E-BZXLRcOX5XaM_CRhRM2kR3ksyymlbKH-c_eqmA8KEqVUMVpQ8GCYf-8SOJMrMTAStMpotnpAm60Y8852mUSoJlr22jZibovw0NQC73blSEvn9J3DcmbasFlWQdCZm8bo8k8pUcCxTUMB62OcjDOxE8odZQljQsx29bm3mMC-819xIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ig5Fg80dXSPvZ_uR34sBDdSsC5_yHj5t_EZj8SAkY2NzMMmCjDvwnIJ3JnVnU84l_1t6FCAi5jrLH4eN5_78mK_Ialvax_4JmyeJgunQXHmYu7UYd-q3MUvxzuGhPpMMSy_SPJie_2KKl8VkihQfqz9hUG4EwT-CqZ0MiMuayGJ9xhOIOpJGD8rrK9jGAgwYiCBjuHypikFJU_OS2gnZAoe6tSldnNP4V95FMSiy_Lrw54tDmQhRjcuDHZk1jbxx6R9V5OCU10QiSxZ0JhnlSlDq5aVx-kRaSOfaaUmT170L02dgZqQMzad1ZpiN21eBJqkdKeYNqFovJ2GaBPTVPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHM7xaLr83qb_XuAMoTttvJ0MiUwgQhVct3p50gjKyzqUf0Y0vQMvmXrNvNeT8xSKNO0bBe76DjRIU8QumFX-g8CMy3sHHvP3ofHFoj_4UIdGv-rMP2InmUWa_JJrYJsBZHkGJLxnZdycEkyepoTxvapHHUQg5exl7YXZAXcBoL1UgaFZtwYSN5oG-NqSSWdbORJa0-9TCyvn4AbMxKDkFXKKybBt2cEgCzC3ueQA6AS2YvNcSiU5e04QtzKnJz3FCbIdLpozT-VD42mb1bKj_Dqx71qDxCTFYN9Advs20BFDWrGE1sj65j5TZPFpFhkNMqXODEZgaujsDu5Q8E67w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjfTSszl37lcTuwk2uG2N8qZ0Gvy8KHf_i8JtreD2iSfFsTB-nYl-KqIDGojhXxv7FLfPKvQBlOBXa5PRpB_K_TNO1L0BoVbPQrEypaXExPWtxCL9reeis0SqkwReFXcgrPuh7ZEhe7Wo0emlMnsu9oxgxNo_gHhCuOQWkYYSy8LjC2HgLpuQgJO8tBWMJ4tQYOgQWnYYhHGjb0SPyqBKtkWVokLbELesyArDho5YS6B3jVU3EHdpeUGgidZAGeqHiKI1PTn33ZXFguHLijRDezNF58gxZsRIDBCZO2nLSI7qwR4QduBtXUTqDf_sQ-Lv_lbVH2NzUuQn65MhoRyoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIkbbJuBnhEBEIqyYKrlToFRUSheHYbHsZ7dtjn49al0jAWBmBUHzMuaemcbinXKkzbDpBXbahmEA71XJhz5P0Lj8JfJHTKmNvQRTrhjM7OkOeMm_2xEFKzfpEHDavpF7dJJmA8cZC3ejnfj1E4a6-eTIFfBL2Teap0Pj7vFWpFTGLpVHdQ9nQEef_yNN4RDge0-396RMA7IOYhzEhnoWZHHc6-MVN-mm6vxqTS_h9xEw1Xo1GtT78KUTMlgotz46x8ucSTeGBI4kPjfNasZBIGQ5x06mqQwuXTqpluPYJdNFbU6I7beaK596NXq5XEeFkSqdqQe-1YXjohMfmumAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjtDX3NSJS6oFuQR2XN0nIFT-75vN-Hses43UCkodz3x13eK13twCeyx5TKR13C0hVADFb145cfAzU1B9pw4XMzO1jjL5NO9nSoJ4q7o_aUhwAe0DlELt0mWg-stNkYQfITV09sgQXCMCe8z10yIQ-kDcMIq1K7aPKyGpoISZOJ7Gx3PaaCMclAreX1-HeZMAyEIciuYsV27GUgXwJhviaKAgSRBwAzSC57uLUUk7joXbYhwnog6SFYRoSYVFklStRBLZwBCbcbk65jFUqupv1MY1SBj4DzJ7WJJB-CWwQiAeG-UgTkgdp_dag7OfUpYRCA8dQL1TIeVCU5CCdUcZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxrqKQOeMuSQStM1S5jXoyUB0WT_6mPwRoP4z-5FFhBVdTro8gZfE4QIEy2C4ZqWYmqGcZhpJqW9uSbtXsxwV9gvZ9FT90KUBxy2_CsGbHzJkIMH5Xn3FgPnEypABEovpv0gXnwAreRUMN2s5P49j0PzbwKWYi3F5vdfxyD7NeP3B4gWFRfmM899o5X1rOuG1F4moFZgeKbpxujQ8etpgwy4Q7YOBPpa7TLIwr55WoCQ192zwSa-YbG21ej98NwlXizw-GDTHNSluMzAfWUHUK7gcZKuHp-5r9zQA4OS8QsEAhrO-XtcLsqUCBweMxizEVJZ7rTncs3atk8TcV23Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VY7SknurbF9HD96ksk3nG49frqdwPJGb-HQQuwTpvB3iLWKKancOrDqY_SL2lo-4WR_WJnDYrASBVmiTOkUybVf78r9cG41S2UJE75lAQbHIimW6FhF7JRCwOBh3Ql9LRaz9R3rNI9EiRMVbuQrsmmxV9ZQIDfl8h9ZD-wh8qSG1_8M7nSXLGBiRS8aZbMoys6kWqu0MDGAB4pM7udw__brD7qgDY1E8xBR9mFcfc0b3jev3uoU6k25ipiiltEbXVdtboBZR7xLgxYecZtF4xNUCNgJBrHHdj_mVDdSVkqg4abSC8PP8b8tIU0XHHtRbndHWLz5opByxvSRLNhzy2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSMt7juKahS88bIrGIBM8y3aak-FXDkWewfBCi5MyIHLo1bE6EF6ZeZRpcUYxjSxxgi_rK_1ZaI2Hi7jYbtV1-_TNu_ewOyThiTJdMHNp8sxK6vU71uj9ubV_Hu-eM59bYgwrT40aukaHJTcrCYFZ7QbSTXMhTcHjCPHofVp0tqtxum0o59In8zyDS3FkqCO60y8KkGDUSDQ_8weBTHqO1CeXkYo-uTlSE2eEg3jGhgRQ9f3rjgP7g4h1bvRwh_TFgH5MiLqCOFbc_hkyczzBrvQH9mbK6SiGzbJ434i2J7Wbl8U2Yl9tCP3_DUynBSI64dSzh-ciY9K3VM-QSE5yg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=I5Vvf126EY_efEIgWUomAx7fYUkUzmU0-mcu-43RRu_hacuuDUSuoV_Ow0NB7i32ihJnmB5hlBUBgQZxdW40VJQdIEhTTl-e8WI1pYzP7a5NnVbqO0EgcnG6m1DraYSaS_oc2HzuhqW9dS7-KpzGj-G4GGXTzVS-kHn9cjAL6bLJGaCTZ2HMGsMFFHsF7qI8FdDzEf6urwxUEdvQ71sk5WSbQFBU4vNCVQG0_oSap928xci6cKUR4uORkPj9YBwWMsrB2SOeo3vfqe5dtezhLjstkNHRxDlvdjzsK0Syx7ksl3ZYpkUCvz2E77lI3-eFcuQ0-yeR_pX3RoWOeAU0Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=I5Vvf126EY_efEIgWUomAx7fYUkUzmU0-mcu-43RRu_hacuuDUSuoV_Ow0NB7i32ihJnmB5hlBUBgQZxdW40VJQdIEhTTl-e8WI1pYzP7a5NnVbqO0EgcnG6m1DraYSaS_oc2HzuhqW9dS7-KpzGj-G4GGXTzVS-kHn9cjAL6bLJGaCTZ2HMGsMFFHsF7qI8FdDzEf6urwxUEdvQ71sk5WSbQFBU4vNCVQG0_oSap928xci6cKUR4uORkPj9YBwWMsrB2SOeo3vfqe5dtezhLjstkNHRxDlvdjzsK0Syx7ksl3ZYpkUCvz2E77lI3-eFcuQ0-yeR_pX3RoWOeAU0Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOoz3mkDOKqwAAKYZGVqalGuD4DlB73cdkgt3Dy_m3bxBtHt8aPsi4lBpV-QIvRsmoEyX0nwdesfQAbqxZVZwZ7_FTWcuMu9EAC2xCil8t5sVlfQWqVfrMhqD1mBJ8GXhnHpVOV3jvn6LD7fe6iVEsyU39A6KwROX9j0lJc5i1ZxuTCz-VHTRId4YjrfmWPhNuRKGAH0MLD_aU5P7w9ruqzLI3gWnPkiKUcXaWENPSf00OoecRU5nr1wgEX6alflOxT-n0m0Ufvkcq5LQXFunL0yMq-Rh3SoNaMQ7rfR8EqgSNaYu0EzWIBCbdF31s1uMgMoY8BK9-3VzDh0uw3kcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Szj022bJW2sEjyAKh1mONtjoqxOGx5VyOpbr9ewTA7fGxW7rluE2NXqtb163aHBkocqRthkbW6_dhjugWbZZVHXRiGx_lrcOmkCw0jDwmEPCFZyS_IhaRNzaN3v8o5sdSbESE6VlsZjOnv09euAfxjAiHOTlDS-0NXPWLhTKZYqd8YM8Jjw_tpZcCG-TiavXjJyb_DfKdmRhnJPJdMI-QSfYL5BtnFptAHtDNMWnTF-fzmZ6GD5I5Wsub9V5l5SF8jr2pa5qPsrG0VmNUUiTdOXShc91DrmZXJEVsyJ9Pr8ZJeKfSOK7meEMehOfMvBvGpFXSOow3WJm4OIcui9vdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=l302iQcGORwK2UC-PYqc--WA7vaye5oOCwDZpNgjLvy7NtG7nG0ABF880IWb8u1A_7BCQSR6qa2PSwd5VqpEAN8aha0nj8CiW2lZ2U5GEwWdaNvceaPVCY-eqxbLdw4K3MMdwjAuvou0eS3xri0KGcPxyOIjmv7hNvxwudHaoeqvEWqjrGplrHxH4eFzKnmzZiRh47cz-Vh5ICNlL9DvuHbyogFvbLCMHWKGtjaX6dZ2Mdpq34ZG0fy7zLjX0WR9bfltJnF4vbuYpHQSOUv51tNiyPP8F2qys5firmlRY-uyzuvFG_bUVO_Bf9uhSqcOIT93a4_9hJLEcuVkj2Dqyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=l302iQcGORwK2UC-PYqc--WA7vaye5oOCwDZpNgjLvy7NtG7nG0ABF880IWb8u1A_7BCQSR6qa2PSwd5VqpEAN8aha0nj8CiW2lZ2U5GEwWdaNvceaPVCY-eqxbLdw4K3MMdwjAuvou0eS3xri0KGcPxyOIjmv7hNvxwudHaoeqvEWqjrGplrHxH4eFzKnmzZiRh47cz-Vh5ICNlL9DvuHbyogFvbLCMHWKGtjaX6dZ2Mdpq34ZG0fy7zLjX0WR9bfltJnF4vbuYpHQSOUv51tNiyPP8F2qys5firmlRY-uyzuvFG_bUVO_Bf9uhSqcOIT93a4_9hJLEcuVkj2Dqyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Y1STPjN1Gl2nG9qLxKNuSc52w_oe5qVczc-nCdwareHWSvWjRgUgA1Qb6O71jKS2d6xNKFn9vyNAWaqb14FK_4EmeIQoOIJLP32IXXH5ISwOsviB3lQqP6tK40ml6WpR0_sLZLjQUpbGtRwfHN3urRZOgukV0QJq1HFDSNUwrPXDL4o3Cc777kNhYn4AB7pEWJ5YzNJdiD8x3xVugMGs1DF0AAslxoGhEjGGk3yslvG37owAwTdd8egxVPwEFPs_lEmjwX-SjfWpHtB717JxSV1Dx_PyZKW2p8G_T0aTjfr1cBwgflpvZDeKD1T02T6wGOgDIBPbDPwBklY3zyHssg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Y1STPjN1Gl2nG9qLxKNuSc52w_oe5qVczc-nCdwareHWSvWjRgUgA1Qb6O71jKS2d6xNKFn9vyNAWaqb14FK_4EmeIQoOIJLP32IXXH5ISwOsviB3lQqP6tK40ml6WpR0_sLZLjQUpbGtRwfHN3urRZOgukV0QJq1HFDSNUwrPXDL4o3Cc777kNhYn4AB7pEWJ5YzNJdiD8x3xVugMGs1DF0AAslxoGhEjGGk3yslvG37owAwTdd8egxVPwEFPs_lEmjwX-SjfWpHtB717JxSV1Dx_PyZKW2p8G_T0aTjfr1cBwgflpvZDeKD1T02T6wGOgDIBPbDPwBklY3zyHssg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0SpDyT59AXoaPHiUxmFQTNqv9A5VGY1VfJsQjQfQUH91zn4vBm5jLt16azzweD_gw-if_lHa5NIPMMoU7XgLhMbwqfTOayvTmhYjC0U3-cKNxuI2dggedyxzGk76s9XslQixxWYHrZyL2uApxkvs0dhkCgnH_tTcCjh_g9C8mY9pay1Q-oz35qrwrsXvgbiVSTHOAVF-Omws2wvlumS_-xKweW5mMUkSBQI6PQCbUFhjMUJYB1H_VvbrSB6buGHYar98x0H8oo-rx3UaoDu8ug5MFtWaHRgI10mB48P5AMmBFZz2BOLIRnyiwyeOVuoHG28h1nOIB2TJSAftU4C0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9KuiqVP_jf6rpKx8p8Dw0ds61UmyN8QMYl4FM336GXVKM12j_e8WmfcRrAC-WHlaMeiQRtoSvfJkVREgw_Rq9fn7TSOmAoEJ9RwU_vybXRrdiUOYlYeYgynnn9QvPsEPyX-vT7fo5ADFmCORfnByDJ2IRFfug25iKcQhMqnF844b0FZzAI3siB93JezF2R2hawdY-RvhQBhXc-ciu7dkl5-IUu2e2Lrt7xBzJnIZuYG-8E9qCovAPM_iJQIXG3qji_ju-R5xWoOd-JgfLC3zh1bBLaGa0Yc3_pDM1U-VTnftQqb586F7HyMV6Gqv_1bZX9Qq_yGc3dFIuFYeejyrQ.jpg" alt="photo" loading="lazy"/></div>
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
