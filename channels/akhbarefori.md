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
<img src="https://cdn4.telesco.pe/file/O1Pr5_Mi2_gIV_f_6QVQGagTiV3XtIV7Sn-7hMkatfTMScX28YRRw5Z0Z1VXqFSfBWQPtr0LaUSB1kK_xPkpI4DjCCLTD9MKQm9jVQkOxDKvhydOu29PHAIEznjUZqMLF9Iqotyv7rnMHLTt-_8t-no7IrpjBE12MAHCQqRQnUvNaNSaGRsBCvbqt65-9YQXozgqEheTVyk6i7i3f3m8-zatXoRGU9AROMd5AyDv8CyA0-5tE2tGmfAbl8X_jPU2CHpbQ5-V-NSZJ3H1lR46VqG9xYK0hyKM_OhZVOku9fLhr8nqSrsY4RZks0nCVpWlkK23fDieNa6UoNHDQh-PHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.47M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 13:44:06</div>
<hr>

<div class="tg-post" id="msg-661058">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ترکیب تیم ملی ایران برای مسابقات جهانی کشتی مشخص شد
🔹
۵۷ کیلوگرم:
میلاد والی‌زاده
🔹
۶۱ کیلوگرم:
احمد محمدنژاد‌جواد
🔹
۶۵ کیلوگرم:
رحمان عموزاد
🔹
۷۴ کیلوگرم:
امیرمحمد یزدانی
🔹
۷۹ کیلوگرم:
محمد نخودی
🔹
۸۶ کیلوگرم:
کامران قاسم‌پور
🔹
۹۲ کیلوگرم:
امیرحسین فیروزپور
🔹
۹۷ کیلوگرم:
حسن یزدانی
🔹
۱۲۵ کیلوگرم:
امیرحسین زارع
🔹
مسابقات جهانی ۲ تا ۱۰ آبان در قزاقستان برگزار می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/akhbarefori/661058" target="_blank">📅 13:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661057">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrrZu-r3IjgAt9A_3ro1LfUPjtOfjRB3GxqxVVfQpYQ5lm2nH4N8LWiU2B5avww1LtvVcTNoKkNsf-gvhzgQCfHhakNj625Wk5IlV8dKbcBNRh3-_rHcgSgkYA3kLW2CiK4kxlTFobirv6ZMYrCelQQ43HQRUXTLlP2EV37attr9QqckkKG30Ilrn5IYQr4Syjs5Rnz16mqSskPcV0ML6GcRH1q1rFCzTFx8TjN7hK28zGN7s22HBigQcygiqhPtbqjaljFKiQFfXPToDOaBXx6NEGYPY_z_KA2FwZpEn__UDhGgyV50--xPGdhNXTXjkK5URvpjyXz38d36r00FJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
هدیه تهرانی در سلامت کامل است
یک منبع نزدیک به هدیه تهرانی:
🔹
خبر منتشرشده درباره وضعیت جسمانی این بازیگر صحت ندارد
🔹
او در سلامت کامل به سر می‌برد و هیچ‌گونه مشکل جدی جسمانی ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/661057" target="_blank">📅 13:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661056">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ثبت‌نام در قرعه‌کشی ایران‌خودرو بدون نیاز به واریز پول/ تکمیل‌وجه تنها در صورت برنده شدن
🔹
اگر قصد شرکت در جدیدترین دوره قرعه‌کشی محصولات ایران‌خودرو که روز یکشنبه برگزار می شود را دارید، نیازی به واریز وجه، افتتاح حساب وکالتی یا مسدود کردن موجودی در حساب بانکی نیست.
🔹
متقاضیان در این مرحله فقط درخواست خرید ثبت می‌کنند.
🔹
پس از پایان مهلت ثبت‌نام در ساعت ۱۲ روز شنبه، فرآیند قرعه‌کشی روز یکشنبه انجام خواهد شد.
🔹
فقط افرادی که در فهرست منتخبین قرار بگیرند برای واریز وجه و عقد قرارداد فراخوان می‌شوند.
🔹
در این طرح محصولات خانواده ۲۰۷، تارا، دناپلاس، راناپلاس و سورن پلاس عرضه شده‌اند.
🔹
مهلت ثبت درخواست: تا ساعت ۱۲ روز شنبه ۳۰ خردادماه
🔹
ثبت درخواست:
ikcosales.ir
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/661056" target="_blank">📅 13:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661055">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ضرغامی، وزیر دولت پیشین در برنامه «وضعیت»: بعثت مردم یعنی مشارکت مردم در رهبری. رفراندوم در قانون اساسی به رسمیت شناخته شده است. برخی می‌خواهند مردم را پایین‌تر از خود نگه دارند تا حکومت کنند؛ قرآن مردمی را که فرعون‌پروری کنند، فاسق می‌داند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/661055" target="_blank">📅 13:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661054">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68cbd488c8.mp4?token=ehjrzwRDkXBePiTWDpIooAU4Q0u-yhZVj-tmpldLRHKRrbwkMeHgoJuwbs27aos2nlOUmgpRALtS_XAdpAxyKxuW868VE61ArbR2VhBsqrpfKz-JyH8R-8yhO877dlhPxttCyJNMSia5c56Uy8EnjINpDmI5pPta_ro5kpY0B4KzvIPw4l4BcKQhe63xDIn5SsJA-ZQsG6abXXhXcbFq0JRnhtAMcrgA7Teg1jX2BqXc-ST2WcB996PaAtdo5d4pPBDV6T_i67_M6u2uqsu8GWbdP6QbTlujooXOHMLXuBrNYRCvcsaSFBGNeqzScfe8qZ4GzwmE-R6UcCMVaqD5Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68cbd488c8.mp4?token=ehjrzwRDkXBePiTWDpIooAU4Q0u-yhZVj-tmpldLRHKRrbwkMeHgoJuwbs27aos2nlOUmgpRALtS_XAdpAxyKxuW868VE61ArbR2VhBsqrpfKz-JyH8R-8yhO877dlhPxttCyJNMSia5c56Uy8EnjINpDmI5pPta_ro5kpY0B4KzvIPw4l4BcKQhe63xDIn5SsJA-ZQsG6abXXhXcbFq0JRnhtAMcrgA7Teg1jX2BqXc-ST2WcB996PaAtdo5d4pPBDV6T_i67_M6u2uqsu8GWbdP6QbTlujooXOHMLXuBrNYRCvcsaSFBGNeqzScfe8qZ4GzwmE-R6UcCMVaqD5Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جایی شگفت‌انگیزتر از اهرام ثلاثه مصر!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/661054" target="_blank">📅 13:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661053">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای ارتش رژیم صهیونیستی: بیش از ۸۰ نقطه را در لبنان هدف قرار دادیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/661053" target="_blank">📅 13:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661052">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
فارس نوشت: یک دیپلمات آگاه از روند رایزنی‌ها اعلام کرد ایران پیش از بازگشت به مذاکرات با آمریکا در سوئیس، خواستار دریافت تضمین‌هایی درباره پایان یافتن درگیری‌ها در لبنان شده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/661052" target="_blank">📅 12:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661051">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
نشست امنیتی صهیونیست‌ها در واکنش به ضربات کاری مقاومت لبنان
🔹
وب سایت واللا به نقل از منابعی گزارش داد که فرماندهان امنیتی و نظامی رژیم صهیونیستی جلساتی برای بحث در مورد چگونگی پاسخ به حملات (تلافی جویانه) حزب الله آغاز کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/661051" target="_blank">📅 12:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661050">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
فارس نوشت: یک دیپلمات آگاه از روند رایزنی‌ها اعلام کرد ایران پیش از بازگشت به مذاکرات با آمریکا در سوئیس، خواستار دریافت تضمین‌هایی درباره پایان یافتن درگیری‌ها در لبنان شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/661050" target="_blank">📅 12:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661049">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJugMewMsmZRqgBabj9sweSw5oj_MapDgVybULL0rhAhI90vM4iHBfpxFqYtsaI7FBRnxG8VXC68VAFsSUDyeV8dYRJ7F6pmkrLi0D_FldP3fc8nNfUA5r3jPn5r2-5Rf6ZTAiEgS2vNtfjDdr-ZkvJNNlV1J9vbNjNvRu7pYL-ATpT3Z-e0r4-u1paVwO-K2CMIWhiNhej4hCntECxguDwf31iiJ_hnED6vUj_ZdeTrvExAmQPorQFA43qgiOiGH3z5MjmVPqW6H06piGlmbR74wRWJZnRf9jPPNKSjsGvyx-drDusFTfiN9uGYu1XJ3tSyDn2cwB61FKog_1GHXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بخشودگی ۱۰۰٪ جریمه بیمه شخص ثالث!
📢
فقط تا
شنبه ۳۰  خرداد ماه
فرصت دارید
❗️
اگه بیمه شخص ثالث خودروی شما منقضی شده، الان بهترین زمان برای تمدیده
👇
✅
تمام جرایم دیرکرد وسایل نقلیه فاقد بیمه،
به‌طور کامل بخشیده
می‌شود! فقط کافیه در این بازه زمانی، بیمه‌تون رو تمدید کنید
✔️
تا ۲ میلیون تومان تخفیف با کد
pnsc
👈
تمدید بیمه شخص ثالث
#بیمه_بازار
#بخشودگی
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661049" target="_blank">📅 12:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661048">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ضرغامی، وزیر دولت سیزدهم در برنامه «وضعیت»: اگر آخوندی خارج از چارچوب حکومت از نظام انتقاد کند، به‌تدریج تریبون‌هایش را از او می‌گیرند؛ ما کاری کرده‌ایم که روحانیت مجیزگوی نظام باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/661048" target="_blank">📅 12:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661047">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e99d6354.mp4?token=vMkO-NHrElic5AYtr9qLfC3a2NiQCageUFO1WkYHfDwBn1lQS5zLuA0vXMKe76qFlTP8UJOeDuRFWGJKLoePiGZnMPJK-B014JQuNwsrKHOqiMUhoiOwJSh7iPyro5_4sS-MWML45Iv_lGVmgLOKi3O27pcaQS21_BYH1H5ixKOC0Tua5jlPwG5Xqq_YvdzyuN-5MSemLxxxrJUOoO4X7FVNJ0zDRnVl-e5RArcldWFtwi4MYyUCVVpXVL9p91IfKgVca7NazYDyRF8DtXjcBJNJnBCMDaoiVhH9H3vpodsME9VrMwVCS7t5qNMCc-jhAR5nfSFbJkDfcDuXm4UfCWH40tnW64kMhdbuv_fM_IHlsjLEJqcyWFDsT292WEnXJqLDyVSFrI0yl-6yUexXnLIMIu-ATuRlkXreZaa9oBUFrp4tO3lsxBXspv9s5Vzq5SbobS7Z9uW1Ejz98OiajO72LEWmfkef0zjU7gVLCUSnIFlO-5SjvBlvqd6YAfUJLS34WbDrYzFEA7L7NNFvH4vYeNnI7gvaUIsAEIxVc1UpR_gw1lmsmXkX3Idut8k_nXk6k7GhiER7AYDrPZnGfEi48TmRXMMYzOmJhDA33mSDR3Ru6_8teeTlyPpeeSlKQ0HpjVgSqSrEVow5Y8SQDRfzQ9XINVR_Us386AFY82Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e99d6354.mp4?token=vMkO-NHrElic5AYtr9qLfC3a2NiQCageUFO1WkYHfDwBn1lQS5zLuA0vXMKe76qFlTP8UJOeDuRFWGJKLoePiGZnMPJK-B014JQuNwsrKHOqiMUhoiOwJSh7iPyro5_4sS-MWML45Iv_lGVmgLOKi3O27pcaQS21_BYH1H5ixKOC0Tua5jlPwG5Xqq_YvdzyuN-5MSemLxxxrJUOoO4X7FVNJ0zDRnVl-e5RArcldWFtwi4MYyUCVVpXVL9p91IfKgVca7NazYDyRF8DtXjcBJNJnBCMDaoiVhH9H3vpodsME9VrMwVCS7t5qNMCc-jhAR5nfSFbJkDfcDuXm4UfCWH40tnW64kMhdbuv_fM_IHlsjLEJqcyWFDsT292WEnXJqLDyVSFrI0yl-6yUexXnLIMIu-ATuRlkXreZaa9oBUFrp4tO3lsxBXspv9s5Vzq5SbobS7Z9uW1Ejz98OiajO72LEWmfkef0zjU7gVLCUSnIFlO-5SjvBlvqd6YAfUJLS34WbDrYzFEA7L7NNFvH4vYeNnI7gvaUIsAEIxVc1UpR_gw1lmsmXkX3Idut8k_nXk6k7GhiER7AYDrPZnGfEi48TmRXMMYzOmJhDA33mSDR3Ru6_8teeTlyPpeeSlKQ0HpjVgSqSrEVow5Y8SQDRfzQ9XINVR_Us386AFY82Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناخن شکسته‌ای که مادر مینابی را به فرزندش رساند
🔹
روایت مادر شهید امین احمدزاده از نحوه شناسایی پیکر کودکش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/661047" target="_blank">📅 12:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661046">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
معاون اول قوه قضاییه: در برخورد با همکاران دشمن در ایام جنگ ۱۲ روزه و جنگ رمضان کوتاه نیامدیم و قطعاً کوتاه نخواهیم آمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/661046" target="_blank">📅 12:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661045">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66931f0591.mp4?token=YX5-7hklF1ftyDY3rAkEbNssqJVJ8u_RPAMbJy3kgiwOVzdwQMQq-OJKgICb0lPO_T1C4X83osTxVzeD1RvvJPajljZqcXy1pi4BPJdMGCpgVTKWjFn8m2U0a7HeE1tm3fS0DMMlOUZXSYW99PqXy9B-a3IVgN4JM4F5Ss1cQPTYE1Rwy-kUNOOr1mHMnc9rXB_MfO5YX-gsKbrmj5vWHToKrrLgsEGClOcBXNnFn70bJJxyZI36vvXLc8K_bJoddAu54hwdOXu5MyIBMj6w-oGBPuEixCvysbKpVf_nNWH6b4DYeNzeAOE1vENa_aZrQiLr0_FWlP0M_EJOCMPw_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66931f0591.mp4?token=YX5-7hklF1ftyDY3rAkEbNssqJVJ8u_RPAMbJy3kgiwOVzdwQMQq-OJKgICb0lPO_T1C4X83osTxVzeD1RvvJPajljZqcXy1pi4BPJdMGCpgVTKWjFn8m2U0a7HeE1tm3fS0DMMlOUZXSYW99PqXy9B-a3IVgN4JM4F5Ss1cQPTYE1Rwy-kUNOOr1mHMnc9rXB_MfO5YX-gsKbrmj5vWHToKrrLgsEGClOcBXNnFn70bJJxyZI36vvXLc8K_bJoddAu54hwdOXu5MyIBMj6w-oGBPuEixCvysbKpVf_nNWH6b4DYeNzeAOE1vENa_aZrQiLr0_FWlP0M_EJOCMPw_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
هم‌اکنون بعلبک لبنان
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/661045" target="_blank">📅 12:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661044">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
تبلیغ این ۱۹ کالا ممنوع‌ اعلام شد
🔹
دولت فهرست ۱۹ کالاوخدمت آسیب‌رسان به سلامت در سال ۱۴۰۵ را اعلام کرد. تبلیغ این موارد در همه رسانه‌ها ممنوع است و تولید و واردات آن‌ها مشمول عوارض تا سقف ۱۰ درصد خواهد شد.
🔹
این فهرست شامل سوسیس و کالباس، پیتزا و ساندویچ، نوشابه‌های گازدار و انرژی‌زا، برخی نوشیدنی‌ها و سس‌ها، فرآورده‌های سرخ‌شده و حجیم‌شده، سیگار و محصولات دخانی، همچنین خدمات و محصولات مرتبط با تاتو، رنگ و کراتینه مو، کاشت ناخن و برنزه‌سازی پوست است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/661044" target="_blank">📅 12:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661043">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a48403a0d9.mp4?token=M8mj9XHNmdTYUeGyP-XT05jAooClr57xX5Njh3CSCcMp65QrqhxJ2hBeDPTUr128Q2XagVjSVrjWntXKoL0VNdNRvz9NlvHSD4SIqmUCwGXqOXVczDQArEbBVL2hfwh-vKavzpYkf0o1NM9tDs9h0uyUzhE1ik767zdbSIR8OWuapol1muOgOOvQ3MDGTKFd7R8CsKBf2UVuu8ps-thgcJatdziOMJYmXD8iis_-SLr0HGJ6Ihj7RwjfelT7Qc5U-ydYnnAwkMXDH2NwV_dj3_X7MdVj-ldQktC89sFhwmSQS_RfIyR-DFSSdmdYlnaxpQ3tRlP1l8ml99GiTi9A8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a48403a0d9.mp4?token=M8mj9XHNmdTYUeGyP-XT05jAooClr57xX5Njh3CSCcMp65QrqhxJ2hBeDPTUr128Q2XagVjSVrjWntXKoL0VNdNRvz9NlvHSD4SIqmUCwGXqOXVczDQArEbBVL2hfwh-vKavzpYkf0o1NM9tDs9h0uyUzhE1ik767zdbSIR8OWuapol1muOgOOvQ3MDGTKFd7R8CsKBf2UVuu8ps-thgcJatdziOMJYmXD8iis_-SLr0HGJ6Ihj7RwjfelT7Qc5U-ydYnnAwkMXDH2NwV_dj3_X7MdVj-ldQktC89sFhwmSQS_RfIyR-DFSSdmdYlnaxpQ3tRlP1l8ml99GiTi9A8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسرائیل کاتس، وزیر جنگ اسرائیل درباره لبنان: «ما می‌رویم داخل، تخریب می‌کنیم و بیرون نمی‌رویم. این همان کاری است که الان در لبنان انجام می‌دهیم.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/661043" target="_blank">📅 12:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661042">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/to3fF8SVRLbzA2XARPxVwq88AZk3Dy1qc0aefBmoas0CqCPtn0HQQvq9eMm8mKc1AOxsK0ifHPIwfsOX111lFu2PXzABWX_Dvcn3pixsjgdt3JGHSyjhEltgT5F9uVwrDHD6Oa5Q43aHBn_tuPdr7_CLO5LPwOuR6LgducDGMELfmwjGIT4Act0p9bF0OlhzMjVho7Arp9fVU9M8hqVNqEirZUaqxts63qoFVW8UwX5Q-LOha2aJqc4gEiizhkXxtVv4SmyjANOYdlrXJGadL8-eOkEy7pYGQzdYH077IV0KkY8uXguJV3zYcQo79YRBOeLFS7EwbfOjt7JZ3a_BcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
هم‌اکنون بعلبک لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/661042" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661041">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پزشکیان: مرکز ملی پایش مصرف انرژی تشکیل و عملکرد استان‌ها برخط رصد شود.
🔹
شهباز شریف: از طرف ملت پاکستان در مراسم تشییع آیت‌الله خامنه‌ای شرکت خواهم کرد.
🔹
۲ شهید و ۳ زخمی در حمله هوایی رژیم اسرائیل به بعلبک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/661041" target="_blank">📅 12:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661040">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ضرغامی، وزیر دولت رئیسی، در «وضعیت»: فضای مجازی آمده است تا انقلاب اسلامی را نجات دهد؛ اگر سکوهای خارجی وجود نداشتند، مردم نه با رذالت پهلوی آشنا می‌شدند و نه از مظلومیت مردم غزه آگاه می‌شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/661040" target="_blank">📅 11:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661039">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
تکذیب وخامت حال میرحسین موسوی  یکی از نزدیکان خانواده میرحسین موسوی:
🔹
او به‌دلیل سرماخوردگی و با توجه به سابقه آنژیوپلاستی قلب، برای مراقبت بیشتر در بیمارستان بستری شده است.
🔹
به گفته وی، حال موسوی خوب است و خبر وخامت وضعیت او صحت ندارد./ جماران
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/661039" target="_blank">📅 11:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661038">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
مکرون: درباره توافق پرسش‌های زیادی وجود دارد و معتقدم که جنگ پایان نیافته است. نتانیاهو باید در ارتباط با لبنان «مسؤولیت‌پذیری» نشان دهد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/661038" target="_blank">📅 11:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661037">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
تصادف مرگبار در آزاد راه مشهد-باغچه
فرماندار مشهد:
🔹
تصادف صبح جمعه در آزاد راه مشهد-باغچه بین یک دستگاه کامیون و دو خودرو سواری، پنج کشته و چهار مصدوم به جا گذاشت.
🔹
جزئیات بیشتری از این حادثه منتشر نشده است.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/661037" target="_blank">📅 11:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661036">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
حکم پرونده «کنسرت کاروانسرا» صادر شد؛ شلاق، ممنوع‌الخروجی و محرومیت هنری
🔹
پرستو احمدی و هشت نفر از عوامل «کنسرت کاروانسرا» به اتهام «جریحه‌دار کردن عفت عمومی از طریق تولید و انتشار محتوای خلاف اخلاق در فضای مجازی» به ۷۴ ضربه شلاق تعزیری، دو سال ممنوع‌الخروجی و دو سال محرومیت از فعالیت هنری محکوم شدند.
🔹
ویدئوی این کنسرت آذر ۱۴۰۳ در یوتیوب منتشر شده بود./ جماران
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/661036" target="_blank">📅 11:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661035">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_wzokcaXGyuCGpODmPrVeaDypEGdXyNOJbNF8tcOTldvIDnX3NSLUXZakxmlpaYGTMdiBjeM2Vs9cIJAxl_tdF_40GQaRGnHcozdWJKovbWO359UTxqwn4Db8cx6Nwu9_g1Klow9qf9rJ4NjuNHrzmrbakpe-t-sxowvezCiUyJ-gKdj1E4N63Xq_hiCXxtquv4vf54QezZQC6MJrUFCdxPiEg7_Q666eIS3oxU83EtW-wXkQoxAFt9dGuaQJrFbd_i0clJPJn99x9eEaMz2O1Q0vdQ0BNhBvlLUbMniAoY26q80J1fzDfSCy6fZRx48wQ9rNJD16YjFL71j09azQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ونس: ایرانی‌ها مثل یک کشور عادی مذاکره می‌کنند؛ تبدیل ایران به لیبی به نفع آمریکا نیست
جی‌دی ونس:
🔹
تبدیل ایران به «لیبیِ دیگر» و یک دولت فرومانده، به نفع آمریکا نیست و مشخص نیست که بنیامین نتانیاهو نیز چنین هدفی داشته باشد./ جماران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/661035" target="_blank">📅 11:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661034">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZCEkirjWNFrwJitVzEgsjaDJu4ZU-ZZHMfkQF_8jMj0kD3dGr29uEdlChaNBC7aoCQGBiim_IgavwtzPR_ips459QcEmy4sElG3aAUoMByw1DHNWE19vwW6hGEcECXepfvWvaUznGI_mE0Mhpke8y7QxXNo_uDkeS4GV7pMSGG3Y-1sfTOGxogmQe4-9I8THpsPR2BDbfIZPn-XVts5By4jiH11KsyxgPOAC_FJ6L0Bhlcvqb741o35IlkgL4_IVUEO1nKjXW3otbUCvJjIzmj7bBnK4Og9Ov_x_3gi8tEwVIbiEcEkkEJfRBhZmXzUFuVZseSFbCT_nTi6ZNZgVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبر لغو مذاکرات نفت رو به بالای ۸۰ دلار برگرداند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/661034" target="_blank">📅 11:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661033">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
انتقال ۱۰ زخمی رژیم اسرائیل به بیمارستان‌های حیفا
🔹
رسانه‌های اسرائیلی در ادامه سیاست انتشار قطره چکانی شمار تلفات ناشی از درگیری‌ها، اعلام کردند طی درگیری‌های شب گذشته در جنوب لبنان، ۴ نظامی از جمله فرمانده گردان با درجه سرگرد کشته و ۱۷ تن دیگر زخمی شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/661033" target="_blank">📅 11:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661032">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
عزت‌اللّه ضرغامی، عضو شورای عالی فضای مجازی، در «وضعیت»: بر سر اینکه معتقد بودم باید برای حمایت از پلتفرم‌های داخلی، سکوهای خارجی محدود شوند، با حسن روحانی دعوا کردیم؛ به‌طوری که جلسات شورا تا شش ماه برگزار نشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/661032" target="_blank">📅 11:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661031">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
نرخ عوارض خروج از کشور ( ۱۴۰۵)
‌
🔹
سفر اول: ۹۰۰ هزار تومان
🔹
سفر دوم: ۱ میلیون و ۵۰۰ هزار تومان
🔹
سفر سوم و بیشتر: ۲ میلیون و ۲۰۰ هزار تومان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/661031" target="_blank">📅 11:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661030">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68f3c87e16.mp4?token=LkTBE46T0dqBBwKq96LukXaWumARKBEZAytCoXhVO0_vZBqkvk_qcBowJo8KTuAkbW0SckBPPJqIz5VpVtMVRYPt1mhfwe9GksMK6fG41lPdhV3jKWAzfMD8Uvh83scwupi-fYRCloH2KH4xXTyM5Eyxsgr3Mdf8JzWYc5n2b_FY9KjcqpM2cyRS-iGBlgKyag9gaE5fAGtjEIQCVLTV0QarkDZ2l1h6-v-OpVq1m5fJtNnVPj27qXv-FRGnOgUweUnOV1EQpOMVzbNjaqzuT470MzjGf1VspkPCixn9oind3ujIhm54J4kBUlu0Pr7Tb3W9UxlsFeNd3-_7fQ-ing" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68f3c87e16.mp4?token=LkTBE46T0dqBBwKq96LukXaWumARKBEZAytCoXhVO0_vZBqkvk_qcBowJo8KTuAkbW0SckBPPJqIz5VpVtMVRYPt1mhfwe9GksMK6fG41lPdhV3jKWAzfMD8Uvh83scwupi-fYRCloH2KH4xXTyM5Eyxsgr3Mdf8JzWYc5n2b_FY9KjcqpM2cyRS-iGBlgKyag9gaE5fAGtjEIQCVLTV0QarkDZ2l1h6-v-OpVq1m5fJtNnVPj27qXv-FRGnOgUweUnOV1EQpOMVzbNjaqzuT470MzjGf1VspkPCixn9oind3ujIhm54J4kBUlu0Pr7Tb3W9UxlsFeNd3-_7fQ-ing" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حالا وقت VAR است!
🔹
آمریکا و اسرائیل سال‌هاست از صلح، امنیت و حقوق بشر سخن می‌گویند اما دستشان به خون هزاران کودک در ایران، غزه و لبنان آغشته است. کودکانی که هرگز فرصت زندگی، بازی و رؤیاپردازی پیدا نکردند.
🔹
حالا وقت VAR است...
🔹
صحنه‌ها را دوباره ببینیم!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/661030" target="_blank">📅 11:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661029">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBoXbAF90g7FYCyb_WjUlcRfZ1NhwBc1h3VRzVBMQ7j4phC7EOGaT-l1OwhLBy843sr7kpOMzS84YrQt0_XFJea50JC6u3xkB0hevljAJ6DwoRBrM_8tnp7qUFOfCZnchp0H0pVMGDkVQspS7z-nx3EvZjlDKIO28xEKszV7SIxWwBHZvK8IYQDn360ih385CBpWUtJNE0fdFXWDXt6Q4XgdkeeyI725CNprWCqtECz29YjOCGa75wXrwNMMfkGw0cbHw7JsoNfrtQEulUu3nu9ERO86MKlSLcbVyTW-iCU0HQb_lqfEHHhJnbfZwBRUXQPOG0GH4x7A-w17XRmVUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر اپوزیسیون اسرائیل: دولت نتانیاهو در انزوای بین‌المللی قرار دارد
🔹
یائیر لاپید، رهبر مخالفان اسرائیل، هشدار داده است که تداوم دولت فعلی باعث نابودی کامل مناسبات خارجی این رژیم خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/661029" target="_blank">📅 11:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661028">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
دونالد ترامپ در مراسمی هنگام تلاش برای نصب مدال افتخار بر یک کهنه‌سرباز، موفق نشد و در نهایت مدال را به گردن او انداخت
/جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/661028" target="_blank">📅 11:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661027">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5867926d65.mp4?token=dnlOjZ-YNJSZkELWp95p8mlnmJke7kvGJ49GH-O-BrgG2FN2OCXKJSt0IvyPHoUco6wKgRB8f2kEWLVT4WRGZL-txdrS78V63S0yM8fwnYEFt1YIG6orUBjCRyhTfbIWmg8xWNg4Iuk2Svm1_XG-zx9u9DyF-ShlogCX1TUU05bkWiDvXmIOa7Me_CjQEfVlw64upv49dzpYgHmzXeAx7X2mi5xkCVuf0Yr77YwDE2hTbnHxEPiOUqSzATtJSMvVvWA4LIUtvzrKHqJCYxeOQzbqgYiunt_fN9Ld-aucFcCR9PfRhdogjiP4mSTO8PEonjbVohR_BnaSAlPCvfoR6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5867926d65.mp4?token=dnlOjZ-YNJSZkELWp95p8mlnmJke7kvGJ49GH-O-BrgG2FN2OCXKJSt0IvyPHoUco6wKgRB8f2kEWLVT4WRGZL-txdrS78V63S0yM8fwnYEFt1YIG6orUBjCRyhTfbIWmg8xWNg4Iuk2Svm1_XG-zx9u9DyF-ShlogCX1TUU05bkWiDvXmIOa7Me_CjQEfVlw64upv49dzpYgHmzXeAx7X2mi5xkCVuf0Yr77YwDE2hTbnHxEPiOUqSzATtJSMvVvWA4LIUtvzrKHqJCYxeOQzbqgYiunt_fN9Ld-aucFcCR9PfRhdogjiP4mSTO8PEonjbVohR_BnaSAlPCvfoR6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی روسیه به تاسیسات انرژی مهم مرتبط با نیروهای مسلح اوکراین
🔹
وزارت دفاع روسیه با انتشار ویدئویی اعلام کرد که نیروهای روسی یکی از تاسیسات انرژی مهم مرتبط با نیروهای مسلح اوکراین را در منطقه خارکف با استفاده از پهپادهای "گران" هدف قرار دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/661027" target="_blank">📅 10:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661026">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/408e952ef4.mp4?token=iFHFnUYYoYTRDHAlLmeL2yDdsMZOu40uZn1T9fPmCTcTCE13RidN3tnO4QnWeMBv9bMWyQf9aZG7PcC6_hK8py5YMQhXzrGBVNeaJTOcIcFVFfkFxdwfTv3ba7aJC-d0PfxyRNJ0-tbqmDvFuhppUcUFai9ZDmPZ5CtS9VPlnwA-i_McKU82BmRTgK2JCq91DYPd77qypdmtjjmXWWQ_jG0CQbtzMSi13erS-i--X_B0XbY4YBiclI2LeFlmW97_VpdubnYm2UD-BDpd6PEe71qoxwRiWyDiFseXMWKlUQVPjPRoBGfNAJ2_dRm2V_wCXrolzexAdT_Hw8Yu1TiVyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/408e952ef4.mp4?token=iFHFnUYYoYTRDHAlLmeL2yDdsMZOu40uZn1T9fPmCTcTCE13RidN3tnO4QnWeMBv9bMWyQf9aZG7PcC6_hK8py5YMQhXzrGBVNeaJTOcIcFVFfkFxdwfTv3ba7aJC-d0PfxyRNJ0-tbqmDvFuhppUcUFai9ZDmPZ5CtS9VPlnwA-i_McKU82BmRTgK2JCq91DYPd77qypdmtjjmXWWQ_jG0CQbtzMSi13erS-i--X_B0XbY4YBiclI2LeFlmW97_VpdubnYm2UD-BDpd6PEe71qoxwRiWyDiFseXMWKlUQVPjPRoBGfNAJ2_dRm2V_wCXrolzexAdT_Hw8Yu1TiVyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جوجه‌فلامینگو‌های دریاچه مهارلو، فارس
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/661026" target="_blank">📅 10:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661025">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ic57Yd50ki1J5SeUSan1HtPOlfAJ4UVJvpCMIHP3S4P6AyOd5pB-fumSa7Rfh312yRzhXLQbc8SlgBZ65K62WXjnEu-HXf93Gc8at_RtasaQTE6c6u1Irw1vLa2fQmR0HZFwdB63FC6PHJWi7-hyMBND4dvd7L-rkn-Mjd64sBt_RwhXMF5Surew0eJjb_u3sQPLqePxNML-Y-sB0UCHDARj04uvb8JWZfV0tao7JwQit46XwOLMbZ_DjF2ALS7lAa2WuT1duKXGuz8Rq_bZSJvNzRhlMfdtGpsJqgiOxJNvgUuvVf8NQN2ROs_ZrhRqzjayZy8ylGC8qIrruNNkog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون ارتباطات دفتر رئیس‌جمهور: بدخواهان و یاوه‌گویان خارجی و بعضاً داخلی که از پیام رهبر انقلاب برداشت به اختلاف میان ارکان اصلی نظام کرده‌اند، آب در هاون می‌کوبند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/661025" target="_blank">📅 10:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661024">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgV2-GhgvCiE-6846K6G-VgZM3Ov84m3AyU0AbYYl6I-Ik4V6a_l_Q0HGVteYXi8PV7mOuG3AjDhgSv50fayZo8Uj6w7ZyRikSTlnSmID0XSZt4efzbarepzaopCyVnrtpVHXIzmLz8Wow2gC4x81qcVYYptCjboG9Nw1_lu2DNYf_sPrfRfe3DC0h_NwU9vjzfXGJeYG77bCZDIAvTraz0SVHy0vd2Iu1P-R90RgSD9rhs4pv9_l8CVaOtrrIOY24ThCpR6IpZSzx8F4EfJ2KistiwHPiEUXA-sAqMR2-Oj8q0aNWpCtMLG3fTBOvTHj3Y0Xhm_xEZxQvhwgnarvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایتامار بن‌گویر، وزیر امنیت داخلی رژیم صهیونیستی در واکنش به درگیری نظامیان اشغالگر رژیم صهیونیستی با رزمندگان حزب الله گفت که باید کل لبنان را به آتش بکشیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/661024" target="_blank">📅 10:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661023">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Szc5g_AT7e0B2E9W7JYVSWgFfIH1Rc43-xxGR7LuVz4nFlMnRWhQPUvWQ2qfEfy9vPEUfPAs106KCuHcp_L-QMa9BLVsOSbqZUPwzXjVY5cfV1rrxBo3Z25I0NPG6qBkEZTdfTRh34INGjdgkxVTbThVE6tpFnY3-Pn57Dfgk2LoZZsfCDZxkHEzEIEbwlPoACoPyxDiAjqJ1kVy4i9_i8vD4O29I299tDMoKqK-3nyqluFDuSDOS70BgndXTrBrPYpmQi_zfwBV3N8SCqfhI_mo80r48p_n6b4-VyOOWvWkzQCo6P1NqPNkw3z8uWsErO0Lue-LM2pZabYBgrC8Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بن‌گویر خطاب به معاون ترامپ: هر کس به ما پشت کند زیان خواهد دید   وزیر امنیت داخلی رژیم صهیونیستی:
🔹
هر کس از ما حمایت کند، سود خواهد برد و هر کس به ما پشت کند، زیان خواهد دید؛ بنابراین ما را تهدید نکنید.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/661023" target="_blank">📅 10:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661022">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
وزیر امور خارجه فرانسه: اسرائیل باید تجاوزات خود در لبنان را متوقف کند و واشنگتن باید تل‌آویو را در این باره زیر فشار قرار دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/661022" target="_blank">📅 10:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661021">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
فراکسیون مقاومت در پارلمان لبنان: اسرائیل باید ظرف دو ماه عقب‌نشینی کند
رئیس فراکسیون مقاومت:
🔹
مقامات لبنانی نباید قدرت ایران را درباره تعهد به مقابله با دشمن صهیونیستی در صورت اصرار برای ایجاد اختلال در توافق دست کم بگیرند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/661021" target="_blank">📅 10:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661020">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
حملات هوایی طالبان به مواضع داعش در پاکستان
وزارت دفاع حکومت طالبان:
🔹
نیروی هوایی این وزارت شب گذشته مراکز وابسته به گروه تروریستی داعش را در ایالت‌های بلوچستان و خیبرپختونخوا پاکستان هدف حمله قرار داده است. به گفته این وزارت، این مراکز برای طراحی و سازمان‌دهی حملات علیه افغانستان مورد استفاده قرار می‌گرفتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/661020" target="_blank">📅 10:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661019">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDDCq-HhqfYrndlSXb-DF4HcRfOSIfd2odCVOzvAi41cw4TyP8ry5UurCsUllImwXp03ZVhkVJQ6cup0SJ91LBqfgqHjXykAx8pKB7YYzRyJfno1PQyqkIINk-FAW9JQNsx8V4Y3SpHKJz7917XeJVe3LNQXzU3QpO2kO6M68NrPGydHpm9JVpiVuDPhwJicskgFSziatHEgn_NO_pq-atFKOz_vzpdNo8ZLyd_W104vv8sNVbJX3qWP4XAcjus1LeEDQ0ySTDnlgIEEtwp2QY3XiM-XWzkQs6ISU3eHGgaScUtd5SNhaCRU41zpfXY395-QYSTbQ6dv4wbu3dzbcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت جام جهانی فوتبال ۲۰۲۶
🔹
همراهان گرامی خبرفوری؛ برای حضور در این پویش کافی‌ست یک پیام صوتی ۱۵ ثانیه‌ای ارسال کرده و پیش‌بینی خود را درباره دیدار ایران و بلژیک با ما به اشتراک بگذارید.
🔸
نتیجه مسابقه چه خواهد بود؟ پیروزی، تساوی یا شکست؟
🔸
نتیجه دقیق بازی چند چند می‌شود؟
🔸
گلزنان احتمالی تیم ملی ایران را حدس بزنید.
🔸
لطفاً در ابتدای پیام صوتی، نام و شهر خود را اعلام کنید.
🔸
پیام صوتی خود را به آیدی ما ارسال کنید
👇
#برای_ایران
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/661019" target="_blank">📅 10:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661018">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
تصویری که ترامپ همزمان با لغو سفر ونس به سوئیس منتشر کرد
🔹
همزمان با اعلام لغو سفر «جی دی ونس» به سوئیس ترامپ تصویری از امضای یادداشت تفاهم با ایران را در حساب کاربری خودش در تروث‌سوشال منتشر کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/661018" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661017">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
بیانیه سپاه پاسداران اتقلاب اسلامی: ملت عزیز و رزمندگان اسلام چون کوه استوار پشتوانه دولتمردان خود هستند
🔹
اینک که دشمن متجاوز در میدان جنگ شکست خورده است و و در مقابل عظمت ملت ما زانو زده است، انتظار همه ملت و رزمندگان این است، عرصه سیاست‌ورزی نیز امتداد آن میدان شکوهمند باشد و به احقاق حقوق ملت سربلند ایران بیانجامد.
🔹
ملت عزیز و رزمندگان اسلام چون کوه استوار پشتوانه دولتمردان خود هستند و اگر دشمن عهد شکن بخواهد به زیاده‌خواهی ها و تضییع حقوق ملت ایران روی آورد، پاسداران انقلاب اسلامی آماده‌اند تا با کوچکترین اشاره آن فرمانده شجاع و حکیم شکست تاریخی بسیار بزرگتری را به آنان تحمیل کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/661017" target="_blank">📅 10:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661016">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/920c65dfbb.mp4?token=UeSvGr07HBDIkDRL9-XqWlY-rqIkPt1WB4J1J4C2pcDAH-nOB7XVYfobLMtBG2PMOqfcguUuvl5HHFipNsqHX79aLDM4BnFiiV9gv7QZIjMDazqHeK3P9G4CXtlP-DGOfWaysPtgpIRXoDDXAJWuBp14I8ZEEdOsV2FyEVeaXl0k5duXFmXTUE5LWm3JgDsyKSUfG_TipBXycXZEhtjyno4SMDozBX68PNSID37QiypGW82WIc66z721bhdalxys4MlCKXjivbIef_z6bYfZ9zAt8sRY9dQdnJKeddcAKymC7n1ooXHWBWm9iABWJ7HQMMrCGo9lAoWaoxJ8FU322Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/920c65dfbb.mp4?token=UeSvGr07HBDIkDRL9-XqWlY-rqIkPt1WB4J1J4C2pcDAH-nOB7XVYfobLMtBG2PMOqfcguUuvl5HHFipNsqHX79aLDM4BnFiiV9gv7QZIjMDazqHeK3P9G4CXtlP-DGOfWaysPtgpIRXoDDXAJWuBp14I8ZEEdOsV2FyEVeaXl0k5duXFmXTUE5LWm3JgDsyKSUfG_TipBXycXZEhtjyno4SMDozBX68PNSID37QiypGW82WIc66z721bhdalxys4MlCKXjivbIef_z6bYfZ9zAt8sRY9dQdnJKeddcAKymC7n1ooXHWBWm9iABWJ7HQMMrCGo9lAoWaoxJ8FU322Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیلی‌ها می‌پرسن چطوری کوکو سیب‌زمینی اینقدر پف می‌کنه و ترد میشه؟ رازش فقط چند تا نکته کوچیکه که خیلیا بهش دقت نمی‌کنن!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/661016" target="_blank">📅 10:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661015">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عراق بازگشت صادرات نفت را به شرایط تردد در تنگه هرمز مشروط کرد
🔹
پاکستان تردد تجار از مرز زمینی‌ به ایران را از سر گرفت
🔹
هلاکت ۴ نظامی دیگر صهیونیست در جنوب لبنان
🔹
یک‌سوم مطالبات گندم‌کاران پرداخت شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/661015" target="_blank">📅 10:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661014">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
درگیری تن به تن رزمندگان حزب‌الله با نظامیان صهیونیست در منطقه مرزی
🔹
منابع خبری از درگیری‌های تن به تن بین رزمندگان حزب‌الله با نظامیان صهیونیستی در منطقه علی الطاهر در جنوب لبنان خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/661014" target="_blank">📅 10:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661013">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
مخالفت آمریکایی‌ها با سفر ایران به آمریکا ۲ روز قبل از بازی با بلژیک
فدراسیون فوتبال ایران:
🔹
قرار بود تیم ملی برای دستیابی ملی‌پوشان به بهترین شرایط فنی و بدنی، دو روز پیش از هر مسابقه راهی شهر میزبان شود؛ اما در آستانه بازی دوم مقابل بلژیک با وجود دلایل فنی ارائه‌شده، این درخواست مورد موافقت قرار نگرفت.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/661013" target="_blank">📅 10:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661012">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2IQg6CbUsDGDgMFz2SGHJrlMfgYTjUxgU2K2Tyuqdfmr1zJuiJFVY4WZkWmPbvpSkMt3n4mSz0s7FjXG6CCHSReO467ILzLdocT4fxNEJT9KNp2hsPNYzt2sa4YisBxkDC2dOugNWru5L8MTK-CM2i6mB_cRCgapykMOv1wLRs20l4xDt_Ic6bCmo0_OeaEwyLmJU27vXvI4f3dCfsB0rsVJn46oRUMuybbEHEKx_y0fvmdElAp-auogAZYRMOCpRSm64B61F8mrdajhzS26IdEGUqM1-nQ4kmeoziy4ItNsFRmiweQLfzrcP9ow8vDcePcrsx5_R2nAzxxX7Rycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر منتشرشده از محمد محبی فاقد اصالت و اعتبار است
فدراسیون فوتبال:
🔹
در پی انتشار تصاویری منتسب به محمد محبی در برخی شبکه‌های اجتماعی، به اطلاع می‌رساند تصاویر مذکور کاملاً جعلی بوده و با استفاده از ابزارهای هوش مصنوعی و تکنیک‌های دستکاری دیجیتال تولید شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/661012" target="_blank">📅 10:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661011">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCre3EnlszvUViFhfq3Hdz9JdWvJhlLcuu2V-kVT_w_8cWpvX21TT5wT_0LQs4YaVlfEhskITvaEXSwSqmNSXEYgdVFL1wp1B5qTVhi6P7nCDwbdggntXGns28t2KsXPb1gUHsJsdP6wjgyBX5IvY5LfFH23tNpw_CO9IP-xdVf2PePRnBZMt8VdQfoMS7fZ102CFLgpvScFJsAAYIPva4NXyujvfSH6_iKzYqn0Sb_hG2PP9nMu-A1_gd5aoI2b609GmSthcmGNbXuORyv5q6FR7Rwd8kQgiaeeR5ZY2t5q0QNja1rnbAuH8WEUhl4yOKy-t69VGr5gYgeUKGsM9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بن‌گویر خطاب به معاون ترامپ: هر کس به ما پشت کند زیان خواهد دید   وزیر امنیت داخلی رژیم صهیونیستی:
🔹
هر کس از ما حمایت کند، سود خواهد برد و هر کس به ما پشت کند، زیان خواهد دید؛ بنابراین ما را تهدید نکنید.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/661011" target="_blank">📅 09:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661010">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6572c6674a.mp4?token=fthA14aDBeXQig_HR6MYV1Wk0DwUx38r560vBWj64uQ6QGRBWtIdVTjsttLcti5yq70A3s9wTKl-af4ZIT7vMtn7hw9QH3Ium3y_RPzeCfKv6i6s-tzBhFLxTziYdNhptN6C4Yqc68DTf4lOr6eCWIVizpstvVAf75d8HnSQCeF9MCc97aPt8zGMc4VHSI0l2m_TNCbudiVbEzGfDCPWKE191fP580_VTFpjbeqYwyzyg43gfYoCNZUvkva3Ipx1QrLEaYjD6ObCHZ13ZPCwOfqkKLEFGJVDYUyK_oYWfFlVJlfxtvlKqrqHykrndnRQeczJOD4t3Lhh6y54LckgDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6572c6674a.mp4?token=fthA14aDBeXQig_HR6MYV1Wk0DwUx38r560vBWj64uQ6QGRBWtIdVTjsttLcti5yq70A3s9wTKl-af4ZIT7vMtn7hw9QH3Ium3y_RPzeCfKv6i6s-tzBhFLxTziYdNhptN6C4Yqc68DTf4lOr6eCWIVizpstvVAf75d8HnSQCeF9MCc97aPt8zGMc4VHSI0l2m_TNCbudiVbEzGfDCPWKE191fP580_VTFpjbeqYwyzyg43gfYoCNZUvkva3Ipx1QrLEaYjD6ObCHZ13ZPCwOfqkKLEFGJVDYUyK_oYWfFlVJlfxtvlKqrqHykrndnRQeczJOD4t3Lhh6y54LckgDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشویق وایکینگی هواداران نروژ در شبکه‌های اجتماعی بین‌الملل ترند شد #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/661010" target="_blank">📅 09:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661009">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkdPEDgzqqpZX4HeTojkDICv4nRyTQ9GdLQqjP6ZSR5WOQ9clI-IngtiEcrmUrU_Nu9yZGCf3hHs7xWyJ35GPk0_CFbZOIO8wYpx4xFSf8WMULV_7lo0Q6i1DttFiT74gsrh_AuEZ3HaDSulyHhQHXEbYnyO9LmDgSFa06iM1jwtvYvfVT48lzLkwLcQIFEdvjkIzrb_haG6_TkN8gKoFgjgB-vsfVGtJIBd-5n6bKroiXzcVfBtNi55ozdS68O445qrlQtevY53kT5PIFfM3sC-EGq4fPOgNmw5yhU_QuT7TpeuDH_4b3T9_ySY9q6p0-DDkgsqePmoBgoIye1Jvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سوئیس: گفت‌وگوهای میان ایالات متحده و ایران که قرار بود امروز برگزار شود، لغو شده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/661009" target="_blank">📅 09:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661007">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36d057c139.mp4?token=WMAbVb4X2JQ1Unq5FHzIfnY2Sebw15Yk0PO5ZD9JxmMx7yKmAW8RN5nkXcSGg5Aj2lhTk7nSNAE_MyvVNvI3vgohhoU4C42fyaO9DkOSviGV-vz1iSFVeXHZEkO_GdfS7psjidesi7pIKIZfI9FU4T0HMkbjodX0dfIDKMmo9N2CAM0Dl9WsRhdB9MBfNQhjy1JCexYYP88Vzw8IvVeOH76dIsPS3yaxdzGgpB5CsKt5nUUs4Cl7tKIGvw6_9Sq3P5t0IdaqzYYvnF0b11fyJtvsZ2gmaanrUi9Sb0yL7V_KnUH0LB-veQQPyzBDMGBX_XxUmSm-wDTZOKbYI8An6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36d057c139.mp4?token=WMAbVb4X2JQ1Unq5FHzIfnY2Sebw15Yk0PO5ZD9JxmMx7yKmAW8RN5nkXcSGg5Aj2lhTk7nSNAE_MyvVNvI3vgohhoU4C42fyaO9DkOSviGV-vz1iSFVeXHZEkO_GdfS7psjidesi7pIKIZfI9FU4T0HMkbjodX0dfIDKMmo9N2CAM0Dl9WsRhdB9MBfNQhjy1JCexYYP88Vzw8IvVeOH76dIsPS3yaxdzGgpB5CsKt5nUUs4Cl7tKIGvw6_9Sq3P5t0IdaqzYYvnF0b11fyJtvsZ2gmaanrUi9Sb0yL7V_KnUH0LB-veQQPyzBDMGBX_XxUmSm-wDTZOKbYI8An6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
قابلیت جدید
اینستاگرام؛ برای هر اسلاید پست‌ها کپشن جداگانه بنویسید
!
🔹
اکنون کاربران می‌توانند با فعال‌سازی یک گزینه، برای هر عکس به‌صورت مجزا متن بنویسند. این ویژگی در‌حال عرضه است و به‌زودی برای همه فعال می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/661007" target="_blank">📅 09:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661003">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mnCMqaKTwgbbghITF88ayoUPSXY2t4IAkFC23QvqeTlDsMieEfF4GRCv4s8PMiPPG-9m5bcWnGthwkYF_OAMEyr2z4F9JKztsSCoStgCmWvcEwRefmx7rm2CLjqF2gcV5Ah6_iytZ9koI4-Xp4HSZTYDDijkLcyUKgpL5gZAkxdr_Xpe5TIRtpUtOzlbeUbz48-7H56mCktPantg_94FI9Bg2zXn-onZ6oomkV0kTq3VIhh4yfn4kIDMrm8jOGUwpXrlwsHYeIZc3Cbihy1-1Cubttat2ZVy2d1z95pwZ_Sa1ciQw1u4427UjEAk_aM8d5hLSEj79_QG73Enq8fFdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qE5zVS9hByAPeJa4UtCSTE3hFaTfd1xm3pIB7GeF3SJPrwK22NS3HZh4WzRMSVCMcBp1DfGQOX-lJEAsMH-U82k3zzfC-0bAKXn2AQgPcX0gbu2ZKl7_EIpfMrWcvRalUwAxTj5Yr5lNF_pL9eigCjrVaXfXyV4MdQzW4Qdx8AYfYozRG7XrHu3GQ7T1mZsr9xgIZIUfo0UHmpH2UL5F4Rp4RzCCUuJIF5FXLNebaVgYoL0se_lBz660KHsujFB3c-EuscSlu54KbrTkIf1i6DpiO26F_GSLO0xyTIJhvh_STz-msKGFijDphtKefbmVqUNsgYTzVyv0NgAn3IrRQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TOEngCfCpHieR6I1n0DfPyNMt4xy9CAWTXr3HDv_DK9q_eI9dEm_Tbadh-KHn9IYjk-POG9FDGrA5N2B-qHkQe4uvBEWNerNpMB424zbA0MoNyLTcSYz2rUd0s4W4ZU3yF4tui5_Kh7RVwaSJO3ZVXI8bw-aAh3XWfU3PZfRTD5mht5X-Xj6RhprvjAXpV_JC242BqLXUO0G1MlDHht4bO9lV58rSEn4-1g0TfqW0qu_Syvnu2qWuQmLe-9oRCoJNaI8AQhCaS-yyxLvvPpNHust3bzkpq27js6uu1CnNTZqipZYuBKGk5V5vmiEb0W1WMpLlHLqBhy0w3bG5HLrJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ادامه حملات شدید هوایی و توپخانه‌ای اسرائیل به جنوب لبنان
🔹
همزمان با پاتک شدید رزمندگان حزب الله به نظامیان اشغالگر، جنگنده‌های اسرائیلی مناطقی در جنوب لبنان از جمله استان النبطیه را هدف حملات هوایی قرار دادند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/661003" target="_blank">📅 09:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661002">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✉️
متن کامل رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا
✏️
بسم‌ الله‌ الرّحمن ‌الرّحیم
🔸
ملّت پرشور و باوفای ایران
💬
همانگونه که مطلع شُدید، تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و امریکا امضا شد. در مسیر رسیدن به این…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/661002" target="_blank">📅 09:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661001">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVxrRDSubXnyjvE1BoSdENJDFMDXO-W9Zd5-ki2eYPJYgxQ_c2Yvz-s4tnu7Ox9Qq3JN0dRFZlncOj5ILR27J7B5nCRDKSuZFGu4b05FsPeXsHwW8xf7pjm8QNEVrwPKhXdAx6KEUOGiD8qATMZEXTy7j4jkn7U0FGYSOI6y7HbmxFYpqr4sWJuhMhx5ThDm_KMo9Gm7Hoh6V1VAsIb0u9iJPvzJ7liUt6mMfPD9Co1I34YNq3hFW4VhoxIPLDf3qX8OY5GGMMAQyULAssbINAop3tU_enhEFB6dhkeCFeq6PaKVW5E2bdO6rPsIZ30M7ireSkLbo_bQ4Qn3hcrYLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقدام خصمانه ایکس علیه معاون حقوقی و بین‌الملل وزارت امور خارجه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/661001" target="_blank">📅 09:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661000">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd2c324c23.mp4?token=LsxDjEN0JMWV_BFvr7BB5G2bHKKsudRiOb6LjaauJzMc_G4seMQgQDe66vwK-BYQ-on2TFDM2KEW9-_pAw5atb6eUMWb_35WX25UZOE2J6MrSNG_oLfwsCWqmSoKSnZWI3uo3nPLtkVBRXsB_8RT9fciNfLBzWB-Sg9kjmzae2neLqQ6PQ3u_P7GJyYWSPACTr3owbbyU3wHiqvtVMXtFAsq6tl4M5kIE73QejV1-UY6zWS7-lToCqRnjHgYFRO2jK9-X0N4Vi7mh0woZq1_yAoedQMSZN_N_ecXPwXq-EpvBNQ4YIfx0SO4VRJnWfPc6ppqOdNbQN3nkYKJ8sAl2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd2c324c23.mp4?token=LsxDjEN0JMWV_BFvr7BB5G2bHKKsudRiOb6LjaauJzMc_G4seMQgQDe66vwK-BYQ-on2TFDM2KEW9-_pAw5atb6eUMWb_35WX25UZOE2J6MrSNG_oLfwsCWqmSoKSnZWI3uo3nPLtkVBRXsB_8RT9fciNfLBzWB-Sg9kjmzae2neLqQ6PQ3u_P7GJyYWSPACTr3owbbyU3wHiqvtVMXtFAsq6tl4M5kIE73QejV1-UY6zWS7-lToCqRnjHgYFRO2jK9-X0N4Vi7mh0woZq1_yAoedQMSZN_N_ecXPwXq-EpvBNQ4YIfx0SO4VRJnWfPc6ppqOdNbQN3nkYKJ8sAl2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نسخه ترامپ‌تر از ترامپ پیدا شد! تقلید لوئیس مک‌لئود از ترامپ پر بازدیدترین ویدئو این روزهای فضای مجازی
شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/661000" target="_blank">📅 09:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660999">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYOIyjf2E1PlJcuRCAzCJPNGZm0dgOOL2kgHCL_BmDgrK-36ryWUXegfCfskqKjvMErgAEgnkZsFkjqUYGQj3a-CWoCCy3awdSzP1eVO1rth0RjXupzmHqQzTeMltmqb5T6Iz-OuDQcv-GnQBO0pZ9W6UhaubU0XrQ3WYh1wc45KgByGWgx79u3i97elUh81gMH3NirxDoAYAQdoiy2V1_6P5uEFzfJe7fo0r0KpkplcSISVFhSN0zTjICbBNiegsSvjTANMQ78Nw3XYcCXQqIM-oBE_Y41elSyZYbUHCYGdCFl65lDFTqhQv_IjMWRkuJgt4R9cEf22R9c8Y8YyaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/660999" target="_blank">📅 09:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660998">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dv2Gi7UVlJQPmZwPiZV2koJlUV_m9GFtM-7b6UQmZYa13AdVn4oBYBi7BV3bQ42j6nKHVgJ-lQviqmmI2dX9IugBYapIIgw9ABJIwiVvQjI5z27DgaZAS77tDlNjhSm4RgeF4XcBskUobeMC5AwnybdvEOIlX_QV8TMJZwdcr2tOE2oeJE8G_yiZiFDf30j_CoWfsVi0sCoPdwk4ipSgXnVXiD5yiukuNaoBXf8xiDjKOFYkuDYDDiQ61z-QBzH7ERQbDhZkxvyh0rKOST-kQiKRYE8fuLxAcGWVSh9_EpAw_-i3k8UTDISi_6jHmpRo7bstuBE0aZaVv-rSu8W2Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت مأمور پلیس در حمله مسلحانه در شهرستان خاش
پلیس سیستان و بلوچستان:
🔹
ساعتی پیش ستوان‌سوم «عبدالسلام کُرد» هدف تیراندازی مستقیم افراد مسلح قرار گرفت و به درجه رفیع شهادت نائل آمد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/660998" target="_blank">📅 08:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660997">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aexFo_sLR_IvY0CNMWO2Mhg8jYeQzHJzzRBVcDwBujOWMCdxVbq1Aan0lMy9Qf69D3lG7d_-y0MC9N_3plGM9R1yOqhB2Cd2sFyAIweAtTmllRZHT_Pm3AOJuGX3ioYLtBpt7l-gc4xcC0HdyikJa3dqQa7zmRu2K7L4FpfiSSjj_JXg0D64SfJFwyExU5LFyZjfvtc2MoA9Wl-T6rGPQs_f0_UQfBL8qecLy62DuDGcvDUjT2m8QMu8_fOillDpB844ZzDE_HyZtxlV2YLrbjEJeYph-P7vCiNo09--fxkmhDzrH7uEZp2lw3yilvt6bLlFIKEFukDE4_ZRXe6rzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عقب‌نشینی تل‌آویو در پی هشدارهای ونس
🔹
در پی هشدارهای «جی دی ونس» معاون رئیس جمهوری آمریکا به مقامات اسرائیلی درباره توافق با ایران، سفیر اسرائیل در سازمان ملل ادعا کرد که تل آویو به «دونالد ترامپ» رئیس جمهوری ایالات متحده اعتماد دارد.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/660997" target="_blank">📅 08:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660996">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رهبر اکثریت سنا: توافق با ایران گامی در مسیر درست است
🔹
۱۶ شهید در حملات رژیم صهیونیستی به جنوب لبنان
🔹
رقابت بیش از نیم میلیون داوطلب مدارس سمپاد و نمونه دولتی آغاز شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/660996" target="_blank">📅 08:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660995">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtD_qLhdA4nQfwjEHYQBh9_UqZSIw5dZ30loJmGZWo6LbxnO0ZEUiiVxexX3XkCXGJSfs62w7uzrmy6blIXhPM75HquM-jvJswNxDVMfzulkDI87cnahBMNyHXov2WmJBJNLTGPaI-w4Oqssmxa4PjNNBUEw8Z9Z2FFVA8yvHtWUmdYeql0c09G7H5hR0vFipPzNBWyfSqZm1N7xgeHPI7AwZ6oZFylH1EwPlLAeK2w4bNsvBTDMxSfaDZwEAvf6RlDrvYmC7h9H8Vzr6td5N-LBi2b9tlRHV69qR47yNQ1mhrOlAarQxgx1Ale01bDMrN3zdSL9fREHQ2O9kGT9EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمار عجیب جام جهانی/ مالکیت توپ بیشتر نتیجه بدتر!
🔹
پنج تیمی که بیشترین مالکیت توپ را در هفته نخست جام جهانی ۲۰۲۶ داشتند، پرتغال، اسپانیا ، ترکیه، سوئیس و اروگوئه، هیچ‌کدام نتوانستند بازی افتتاحیه خود را ببرند.
🔹
این پنج تیم در مجموع ۱۱۷ شوت زدند، اما تنها ۳ گل به ثمر رساندند.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/660995" target="_blank">📅 08:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660992">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
درخواست بودجه ۸۰ میلیارد دلاری پنتاگون از کنگره
روزنامه وال استریت ژورنال:
🔹
وزارت جنگ آمریکا به قانونگذاران گفته است که برای نیازهای مربوط به جنگ با ایران و سایر هزینه‌ها به ۸۰ میلیارد دلار نیاز دارد.
🔹
دولت ترامپ پیش از این خواستار اضافه بودجه ۳۵۰ میلیارد دلاری برای وزارت جنگ شده بود که تاکنون با مخالفت نمایندگان آمریکایی روبه‌رو شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/660992" target="_blank">📅 08:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660991">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krLa8tRTiCCCHsM-A3EOZ6pA3xCCEhM4XEIBueNUehZ38piY_iP4D7s9fUEJCdDV0LSydp88Y0LZklc12E1lS405AewsAaNy4I5lEaxVE4x6My87C3q463UEnAkew0i2Ht3scKuVAqCcF2gYa54BRwsMZomymrca4UQVRmZNzfK-T7SnBzQ_Ab7kAbOn9S0hd-tCVavq2jZYD3zo9z8K0QG-UNwVGwORQ-ph6rQgTh0bIrA5riif_ogtVgB9mJdOTIfJGvImL2U4TGExa9wJf_blfvLTybSN5soO6Z8AZ-YuWGf32dHl6GzjlzBPy7C_qf4PbJ1j8O3R5Dj06mjsOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✉️
متن کامل رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا
✏️
بسم‌ الله‌ الرّحمن ‌الرّحیم
🔸
ملّت پرشور و باوفای ایران
💬
همانگونه که مطلع شُدید، تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و امریکا امضا شد. در مسیر رسیدن به این…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/660991" target="_blank">📅 08:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660990">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f86b954120.mp4?token=gV5RW4eJf4q9QMRHMWFASYbHvezgCZUovHxAsiDhxus8lNSYmkYVD9Ff71Uqj1rwyRZYVOG_3dQ5hn9XUQqa0q6iyQpEin5NSul7ZimEKamTQtRZjB_924A0o68wn4U-_nHMCqNtw0sqN3XIGoE1WQFfj05SIhJWpzx0TRJyskMQ945zQZadolP-f9r5f0oTn3Str8tHjscmjfSZ6Icl6IGecd_cuQ1l71a7TTzhes-yUYBGGGbwwkRnMRTe78aunJDc6QEr-_ZtNjHzLcsZMNECHMTqt_6GAVi27eN5V1Vz6BFn8r16iH_msymPTnc-PxE4cu0s6VmNpU4tUh1DDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f86b954120.mp4?token=gV5RW4eJf4q9QMRHMWFASYbHvezgCZUovHxAsiDhxus8lNSYmkYVD9Ff71Uqj1rwyRZYVOG_3dQ5hn9XUQqa0q6iyQpEin5NSul7ZimEKamTQtRZjB_924A0o68wn4U-_nHMCqNtw0sqN3XIGoE1WQFfj05SIhJWpzx0TRJyskMQ945zQZadolP-f9r5f0oTn3Str8tHjscmjfSZ6Icl6IGecd_cuQ1l71a7TTzhes-yUYBGGGbwwkRnMRTe78aunJDc6QEr-_ZtNjHzLcsZMNECHMTqt_6GAVi27eN5V1Vz6BFn8r16iH_msymPTnc-PxE4cu0s6VmNpU4tUh1DDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در مدرسه ابتدایی توکیو
🔹
رسانه‌ها از وقوع آتش‌سوزی شدید در یک مدرسه ابتدایی در توکیو خبر داده‌اند. تصاویر منتشرشده نشان می‌دهد شعله‌های آتش بخش‌هایی از ساختمان مدرسه را دربر گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/660990" target="_blank">📅 08:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660989">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
کانال‌های تلگرامی صهیونیستی: «برای نجات جان سربازان اسرائیل در جنوب لبنان دعا کنید»
🔹
رسانه‌های عبری از وقوع تلفات گسترده برای نظامیان اشغالگر در حملات حزب‌الله خبر می‌دهند. آمار تلفات همچنان تحت سانسور ارتش صهیوینستی قرار دارد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/660989" target="_blank">📅 08:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660988">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
سوئیس: گفت‌وگوهای میان ایالات متحده و ایران که قرار بود امروز برگزار شود، لغو شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/660988" target="_blank">📅 08:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660987">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGeCShDkYfSPL_swNg0vEAOIfBF7BejKJrKR3SehSHRRu8NJvezekQskUbMJWUuqpxHL_BGeKXdD6YR117RnF92OJyFpbMtM0Sr2hLYJY9-wAgdx7nOkQHkTkyIkaa0dO8WLSSt-Vu1sypmOksSfuSWsijVioNQNle0Q5OpH1H5AOhXb4CIhZDNgTdsOas0cdY2tflBtpYeSNHaws9K8SAZqQL6xWVMpl1zu_2qbacUGUhO0TSu3Hj71LpJcxX5d8oF24mbDQfRH_WddVlQjG-6EKtkRaZDdhoy5yH82fgwJLDRM5Psuwomr_nj6q2FDZ_LV4QDNNBJ8phlreQrpGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کانال‌های تلگرامی صهیونیستی: «برای نجات جان سربازان اسرائیل در جنوب لبنان دعا کنید
»
🔹
رسانه‌های عبری از وقوع تلفات گسترده برای نظامیان اشغالگر در حملات حزب‌الله خبر می‌دهند. آمار تلفات همچنان تحت سانسور ارتش صهیوینستی قرار دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/660987" target="_blank">📅 08:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660984">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7Fj7ropIX3eZkVcBRtT8-cp6EI0F5Ur7N1LGBd-t3FvzOLLfZ1e64kKGQ7YmPDFAKRc3ttYWqYQl_fYlDEfP0WSF28tU-xLrkVEg60O5zcx5xZcW4nyK14TGbpHdOWWYnR-yjyWACVn59LesRQ_XR6vTnAyCgVnDncsLf5Ns5kXSCPvcc85geDQyH7c2VQPa_Oy7x28qF7RciJuJB6S7KPXgZP5Mw47fDEEljtarhuwbVleMw2tKLXK_eWAbwOCjNe0w7lPppjBxa2JLMWJ_NahqWnViPRvVcFRXUfzvDND4QbdlSyyo2pSl0ZotChKYGMLolCrbSkUSuzn13I0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dh_mpzYbXfDk-9h1W_XOE1uFZ-ZySpQFB-L10mmPuSig4Ea7zLLPkqaKTxjalkE4l_BtfqVSmn-o4MRN_DecUc5bOWMrwfEgE9Blg_vg1mt830GgPLUXEKGEv7j-0K_q_JNC59LcmZv4QWIIi-ODbGqKQ1psSZC8z-sK4qJPWTh-fhMNXGq6P2Ai9YlpuTryn2ag43DpVr-jQuRlz8S3x_mhfOXUaX76iY-dlqvTdyQrSFMu8VzoY1iWnrPFT7GFD08KKoUlLKxxLegavmfeZHMJdwTMvsnqaOOD9t0jUQV_0GnnkaZXCoGVGMhBuoLgk9_42kLS7mOX073YmsDN7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/923742a447.mp4?token=P9WbcBJbHTXQptaG4RUH8HhX60tZS3qHIZDYK1eTqj1rI5JFtS5bQa17XJbbRdjhV3Aj-DLO865PJ2wEoabadv3ZTFvzgLh6eRp5UUIVGsKpv7l6JJPBLs4GzRc9h8iNbTLob2SU6mYxTlvlpvtVsIA0aZ1az8U8myut4Sgd1cWkLJugvJl7RKJ3xCo7cDK0AYOKK9u55bbLAla9u5jhmUCkWGpe6CmF_6m9puz-X6ErumUSrZQs5bOByJ8TFx8nBxIS0k5oLwXvUsUTV0wPafPUe3MkaPOxPscul1dpkSoP_b9YBJWQOOB1nuByCNCvyr9EscmXPd1U6c_yrQfUdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/923742a447.mp4?token=P9WbcBJbHTXQptaG4RUH8HhX60tZS3qHIZDYK1eTqj1rI5JFtS5bQa17XJbbRdjhV3Aj-DLO865PJ2wEoabadv3ZTFvzgLh6eRp5UUIVGsKpv7l6JJPBLs4GzRc9h8iNbTLob2SU6mYxTlvlpvtVsIA0aZ1az8U8myut4Sgd1cWkLJugvJl7RKJ3xCo7cDK0AYOKK9u55bbLAla9u5jhmUCkWGpe6CmF_6m9puz-X6ErumUSrZQs5bOByJ8TFx8nBxIS0k5oLwXvUsUTV0wPafPUe3MkaPOxPscul1dpkSoP_b9YBJWQOOB1nuByCNCvyr9EscmXPd1U6c_yrQfUdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادامه حملات شدید هوایی و توپخانه‌ای اسرائیل به جنوب لبنان
🔹
همزمان با پاتک شدید رزمندگان حزب الله به نظامیان اشغالگر، جنگنده‌های اسرائیلی مناطقی در جنوب لبنان از جمله استان النبطیه را هدف حملات هوایی قرار دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/660984" target="_blank">📅 08:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660983">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NO7gxytpxjWlEX65xE-n3Ez0P0YmwFuEpHZDdbiAT8zJwLOuZoTXTOVkik6HOe3o2EMPmWDjnWlWv6RfygIuTYU2KNYtC8jau5a9HwJ-egXA56ALU4G4kUgk7CzYip3zJHjyFHnu-Mg2qTW6busGBnLGzTL9ZMC4UCHc_2fRxw4Tt6J3w3SmYKZap-xiyXg3TPTS3RJGfZaNx3z1072fJvqmftrKwm6zm9pcQHGih0t_54w-7wyOoM-VKM1SQ329ptbNwmVY1Fx1d_gfsH36JrxSWOhWScJ7RE8nRGq1M9f6MYkP4-VfrRoPdQ_A9nhQ0yRSFFCstYwNp8Q1VInBKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف در واکنش به پیام مقام معظم رهبری: گوش به فرمانیم/ اگر بخواهند دوباره همان مسیر را بروند سیلی محکم‌تری خواهند خورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/660983" target="_blank">📅 08:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660982">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
عقب‌نشینی انگلیس از مداخله در تنگه هرمز/ کوپر: مین‌روبی برعهده ایران است
🔹
وزیر امور خارجه انگلیس در اظهاراتی که از عقب‌نشینی لندن از مداخله مستقیم در تنگه هرمز حکایت دارد، مسئولیت مین‌روبی این آبراه را برعهده ایران دانست و نقش نیروهای انگلیسی را به ارائه حمایت احتمالی محدود کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/660982" target="_blank">📅 07:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660981">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ترامپ: از اسرائیل در صورت حمله به ایران دفاع می‌کنیم
ترامپ، در مصاحبه با کانال ۱۴ تلویزیون رژیم صهیونیستی:
🔹
چنانچه اسرائیل تصمیم بگیرد به صورت مستقل به ایران حمله کند ایالات متحده «قطعاً» از آن حمایت خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/660981" target="_blank">📅 07:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660980">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_iGwk8UAO64g7yGpQNatOK1tiQwb0PXCP4sBv2tMDfkvoSp7d7KeN66x3NPyTVyzTo7hfw3ieSPzTdsg-fC1Sn_m5X8pKkazj_zlu7p-GQSoNEXSLoUD3CEtZZqhR322Z_JgoV4SgbHvGIjak3NHIjFIb2m1X9mzcrc_CqkUi2Nk3LPBrbVfNZkP2MlzIF6T_nYhmyI_nAfmBn9pr6KSoqglr_M5RzuuO8ZkWTrHXSVtFpyzlQGiDWvTPSGlPMY_0oPkA-6AIHBgvdAAP6LVRTgsow1gGx7Jv9fA3qtlSoH0p-CTPunKMvVui1WB-7zGcxaihzY-tCfOaFCdl0sKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۲۹ خرداد ماه
۴ محرم ۱۴۴۷
۱۹ ژوئن ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/660980" target="_blank">📅 07:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660979">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه مهرمبین</strong></div>
<div class="tg-text">🔶
فراخوان کمک فوری برای یک بیمار مبتلا به سرطان مغز و استخوان
🔸
یک مرد جوان اهل یک روستای دور افتاده ، مبتلا به سرطان که تاکنون هزینه های زیادی جهت درمان انجام داده است، جهت ادامه درمان نیاز فوری به کمک دارد.
🔹
در این مرحله از درمان نیازمند مبلغ 250 میلیون تومان است که هرچه زودتر باید پرداخت گردد.
❤️
هر کمک شما، امیدی تازه است.لطفا این پیام را برای دوستانتان ارسال نمایید
شماره کارت خیریه مهر مبین:
6063737004808968
شماره شبای مهرمبین:
IR820600260201108691003001
پرداخت آنلاین و اطلاعات بیشتر:
https://mehremobin.org/help/
📢
گزارش کمک‌ها را در کانال خیریه ببینید:
💖
@mehremobinn</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/660979" target="_blank">📅 01:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660978">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7ca1e367.mp4?token=AQz-MkBTv28y-UOP_jaDZ9utBf5kyU06Kj-dXw0YUvDZ2D5FWzENVhIpEV6vSikVUQ45FLz2sH8_i0xsdIAlfG2-z5I34YvZlJ4ZuGq4DS9GaKREvD4taTy9NzDu0cNwWa_-PKZyCkxVlxhD_IoWI6D-PjPW-c64E-CIAy1V4qxngBc4VlnLPldgX0lpm2YeMHKNf9yCJfPE9Nz526qg1lrR5RVGCfW4ykGljnOwL38z2sI81lwROgmqQMXh-z_SxMfsm3DnK4hrExa7AtPbflEnpRE2lUmbr0TJV0xAMB835OiMrmX6RcH9QDMUgKoR2A9jNPN4e8sU_tL1VknXrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7ca1e367.mp4?token=AQz-MkBTv28y-UOP_jaDZ9utBf5kyU06Kj-dXw0YUvDZ2D5FWzENVhIpEV6vSikVUQ45FLz2sH8_i0xsdIAlfG2-z5I34YvZlJ4ZuGq4DS9GaKREvD4taTy9NzDu0cNwWa_-PKZyCkxVlxhD_IoWI6D-PjPW-c64E-CIAy1V4qxngBc4VlnLPldgX0lpm2YeMHKNf9yCJfPE9Nz526qg1lrR5RVGCfW4ykGljnOwL38z2sI81lwROgmqQMXh-z_SxMfsm3DnK4hrExa7AtPbflEnpRE2lUmbr0TJV0xAMB835OiMrmX6RcH9QDMUgKoR2A9jNPN4e8sU_tL1VknXrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور فرانسه: در مورد لبنان، نتانیاهو باید مسئولیت‌پذیری و عقلانیت پیشه کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/660978" target="_blank">📅 00:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660977">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
عقب‌نشینی تل‌آویو در پی هشدارهای ونس
🔹
در پی هشدارهای «جی دی ونس» معاون رئیس جمهوری آمریکا به مقامات اسرائیلی درباره توافق با ایران، سفیر اسرائیل در سازمان ملل ادعا کرد که تل آویو به «دونالد ترامپ» رئیس جمهوری ایالات متحده اعتماد دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/660977" target="_blank">📅 00:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660976">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55984694b0.mp4?token=CtFTAHpLnXm9VEFLpEVU0GcjJ0sjA0SdLaY4jcUN0XL6JnxXChdyT8MGZ_fCcBM1f2A_NE-uBMDZ5kbY7WOyy3uqnA1Wvk7OTrNcwW0h578zQjbHYBuNgH-44uLrZQv6jl6BiCGZZSF9oPZU5699pmcoGtwOQJ2DbUgCwQU4wylezDs1_iVXppcxq1ostMa9pcZgyvi_1Q0XblHKqL4TORUAlr4RTLNjpfk7pVB_wz2OeA1XfkjfffNylzLCP6n2p1KAyBwmILINS2fmzFw9_tg5fqfBgTUi7nEaZZaiU25mhBFAKEdYRXyZtDS_t0HT-w3O4P8FkYcZTII1sMJdGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55984694b0.mp4?token=CtFTAHpLnXm9VEFLpEVU0GcjJ0sjA0SdLaY4jcUN0XL6JnxXChdyT8MGZ_fCcBM1f2A_NE-uBMDZ5kbY7WOyy3uqnA1Wvk7OTrNcwW0h578zQjbHYBuNgH-44uLrZQv6jl6BiCGZZSF9oPZU5699pmcoGtwOQJ2DbUgCwQU4wylezDs1_iVXppcxq1ostMa9pcZgyvi_1Q0XblHKqL4TORUAlr4RTLNjpfk7pVB_wz2OeA1XfkjfffNylzLCP6n2p1KAyBwmILINS2fmzFw9_tg5fqfBgTUi7nEaZZaiU25mhBFAKEdYRXyZtDS_t0HT-w3O4P8FkYcZTII1sMJdGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیراندازی در میدان تایمز نیویورک
🔹
طبق گزارش‌های پلیس نیویورک و مشاهدات شاهدان عینی، صدای تیراندازی باعث ایجاد وحشت و متفرق شدن جمعیت در محل شده است. مظنون دستگیر شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/660976" target="_blank">📅 00:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660975">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
نورالدین الدغیر خبرنگار الجزیره در تهران: «اطلاعاتی حاکی از آن است که دیدار ایران و آمریکا در سوئیس برای فردا جمعه دیگر برگزار نمی‌شود، اما مذاکرات طبق تفاهمنامه ادامه خواهد یافت، هرچند ممکن است به سطح کارشناسی محدود شود و احتمال دارد بازگشت به پلتفرم قدیمی در مذاکرات صورت گیرد.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/660975" target="_blank">📅 00:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660974">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
سی‌ان‌ان، به نقل از سخنگوی کاخ سفید: هیچ توافقی فراتر از یادداشت تفاهم وجود ندارد، اما بحث‌ها در مورد مراحل بعدی در حال انجام است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/660974" target="_blank">📅 00:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660973">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✉️
متن کامل رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا
✏️
بسم‌ الله‌ الرّحمن ‌الرّحیم
🔸
ملّت پرشور و باوفای ایران
💬
همانگونه که مطلع شُدید، تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و امریکا امضا شد. در مسیر رسیدن به این…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/660973" target="_blank">📅 00:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660972">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6d947988c.mp4?token=JvxrO5-hfF48F9UwUwt1M_WMIWTBuYbOBYV82np3jVULnBoDIA1UXvua2-UuxpWHZLd9Mq3tAuFtmDBmiZMOQXxznAcwr7kPxOke0ki3JtK7hVS6ZqGGSMSuiunVdJgbLPs3_IYEnggGC7yiWC0SyiJ7GuiB5WumNnbFtgggFZYObxg9VquYDk6etuUyXEubm9hRuJNMMpHvybzz27p0G-pruZr4uPNJcDNIFMVDxD3YMs_EXU-n_TLkZ2c318AoXaEC3wmuhueeyhsq9J2JzpLD5EyEW_xth2X6apg5iYE5C-FXKL3TtAvLIVe3-5shC9Jc2tMdY_jNeEvrNG1B1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6d947988c.mp4?token=JvxrO5-hfF48F9UwUwt1M_WMIWTBuYbOBYV82np3jVULnBoDIA1UXvua2-UuxpWHZLd9Mq3tAuFtmDBmiZMOQXxznAcwr7kPxOke0ki3JtK7hVS6ZqGGSMSuiunVdJgbLPs3_IYEnggGC7yiWC0SyiJ7GuiB5WumNnbFtgggFZYObxg9VquYDk6etuUyXEubm9hRuJNMMpHvybzz27p0G-pruZr4uPNJcDNIFMVDxD3YMs_EXU-n_TLkZ2c318AoXaEC3wmuhueeyhsq9J2JzpLD5EyEW_xth2X6apg5iYE5C-FXKL3TtAvLIVe3-5shC9Jc2tMdY_jNeEvrNG1B1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فشار کره‌جنوبی بر فیفا پس از حاشیه نژادپرستانه
🔹
پس از انتشار ویدئویی از برخورد نژادپرستانه با یک یوتیوبر کره‌ای حین تهیه محتوا، هواداران و فدراسیون فوتبال کره‌جنوبی از فیفا خواسته‌اند این موضوع را بررسی کرده و با هواداران متخلف مکزیک برخورد کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/660972" target="_blank">📅 00:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660971">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqwiWzJEQbuLd1RNez_NFi0pMZ73XASh9mF32SP1FAoZPHItgOtXVePp57cUpGRrLmNLKsfmJc5BIPGxLFnFrm1qlZU6cbnlYg4mASzgmDs_w9-CLjOKO23EePq08vRz-KjHsIp3YVY46hhavWtpEZPcHWSQcb0yFErt8ixe8etmOxGb7saxS1oXTfgUxtZFuwgGvV69fNTlV4swSoC7gOZNkWCeCfhKa8cv4GlprCYXxF5mf4wLXnS9wlhBhRGD2wwFex17IIuSeXqh26nGGTitu_TpGoUwa648Aog2NTzNLi-a2rHAFuj-CN5x2fzHyJTsRbT3ed_9fmdTT5ublg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
برای اولین بار در تاریخ، تیم داوری یک مسابقه از جام جهانی با حضور سه زن
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/660971" target="_blank">📅 00:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660970">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
آغاز واریز حقوق خرداد بازنشستگان کشوری
معاون صندوق بازنشستگی کشوری:
🔹
حقوق خردادماه بازنشستگان کشوری آغاز شده و تمامی واریزی‌ها تا ظهر فردا واریز خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/660970" target="_blank">📅 00:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660968">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiU4lLEgHnJYgOfOIarz-a9aNtSOL6H3Mk92kgDqOrNt6ZE1xYS_mhsMe4pV13gX-PFEsnoQNarLhIuvlu8k5d7I81ZiEVCP8neFioZCVT2KWYBev1qqWt6fQU1JfznXB4ZGHEHkIZQ2fX2yp8oVs1Oe5x8L9Aq6xXJ0lqTYWpD5XQrzHdiFpKkHLZVUmexP7MaWPTkbssqCqRRKIXelEyVoCTJiGLG9NsVPiXs66ze2_FZEpxGqwrQu9eLfdYg8goh4pK4eqF62NVaG2S8Dvpc1GnA20WWUXLXFPZknKolSSao0BLIY9-mt2othurxJq7f6YYqmeMZcOvjfQEFE4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/660968" target="_blank">📅 00:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660967">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
سرطان در ایران ۲ برابر میانگین جهانی رشد دارد
دبیر کمیته ملی کنترل و پیشگیری سرطان وزارت بهداشت درمان و آموزش پزشکی:
🔹
ابتلا به سرطان در ایران تا سال ۱۴۴۰، دو برابر میانگین جهانی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/660967" target="_blank">📅 23:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660966">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ویتکاف: بازرسان آژانس راهی ایران می‌شوند
آسوشییتدپرس:
🔹
ویتکاف اعلام کرده که ایران از آژانس بین‌المللی انرژی اتمی دعوت خواهد کرد تا از تأسیسات هسته‌ای این کشور بازرسی کند و روند شناسایی و کشف محل نگهداری مواد غنی‌شده ایران را آغاز کند./ نسیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/660966" target="_blank">📅 23:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660964">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
مکرون: درباره توافق پرسش‌های زیادی وجود دارد و معتقدم که جنگ پایان نیافته است. نتانیاهو باید در ارتباط با لبنان «مسؤولیت‌پذیری» نشان دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/660964" target="_blank">📅 23:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660963">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrZa4HLPq8xBTc6ab1WsBNgEBdLPp_9zFIQhH74TzS4_1zpd5jZNwuxFzWlVXko98MYpm4bLwKjUoJbGZXzFN-DG_BjSCuY0a2-BPEQ1j1XKUQujZWeTUhlRPxaqjlDc9WS1xNo7qwmwKqbvf2A3nz9RAcNY2jkxLwi_d49ZeZZMQwmEN70nuFyWzfBNKmAKpas6pK1dQEKbntXfaI0Bv1eiuOJcrQICW1bR1nd8zwUpH64v49GzUAH1-qgbHaH-N0PhNbtUfxmTxCDBRWx-X3m-l4CmU1W5AjOY2d4-ZwYuqkiTnXUOm-GB-N8e2rbayFpOs-yGCgu3SrVEhlXugQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترافیک دریایی در تنگه هرمز پس از امضای توافق صلح میان ایران و آمریکا افزایش محسوسی پیدا کرده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/660963" target="_blank">📅 23:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660959">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نوحه</div>
  <div class="tg-doc-extra">میثم مطیعی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/660959" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پک هیئت قرار  ویژه شب چهارم محرم
🖤
#محرم
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/660959" target="_blank">📅 23:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660958">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLtanKFisfcjCj_9u2WeKKkueyDhqFTvjs-yQpKRVbs4jQ4FUVf9cxronn66Nw1yCopvDaOIM2Fh72_zJsudXT0U7dkv5OkQijXSQkJLjlPUhdDmAni6rudW7p4lZrdCthhDMDgZz-Pl_F1uK0gO84GB-aufB8JDAycj6_S1PD1kUUG9qyXL9HxBavh8Qtsv0VDdBTHVQqN3MxvlnojiDUwgDWXNIrnYL7tbZdvy7R87W5ZvYf2QZ0XYf-deWMCIEcOF1lpN63tl4q8Y08PN1WfNNVkgMCXT2pEMEPsAhofkqXYoP1UId-V_ITX4VbICWVtlzwQDHF4iRhJyZol1Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصیبت‌های کوچک؛ آزمونی برای شکر و صبر
🔹
امام (ع) هشدار می‌دهد: اگر انسان مصیبت‌های کوچک را بزرگ کند و ناشکری نماید، گرفتار بلاهای بزرگ‌تر می‌شود. زندگی خالی از سختی نیست؛ این حوادث گاه آزمون، کفاره گناه یا بیدارباش‌اند. صبر و شکر در برابر مشکلات کوچک می‌تواند…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/660958" target="_blank">📅 23:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660957">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-pvCh7H1TopgjApBrc5wAXfvNFioe21qAD1gqqvZXu4YacV-2Jpfhfu_8nAcgel_uYsnMKEyC4CE8ppuRuJZR9eWah7vu_DQV9DrkwlD-FKj5D4-A9Lfr0u21-jRJvaNhq58-dkzTHCKZ145huFwa_gLowRv7MLYwKAefdLPbELYNM0T2-AEeYQQdwdGfKP4HIYuMGFXYPy9nmFFUZJb1jhgZ_eaPjGGl6L6iaAUKHHMPULTG7gF2pY4FdLk2V-6KgZEb3OBtzZFvl4xWnAxeLq2EGoBgdZwzu1UAdsv6gB9AsWDwLec4Kh_YXLQV_SQO-sAA8S8UXzwvE1D3UNCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر فدراسیون فوتبال ایران برای بازی بعدی در جام جهانی ٢٠٢۶ مقابل بلژیک
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/660957" target="_blank">📅 23:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660956">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkT-R5PDsMEyvRC8wEjVmfN6zx2odBEg0DijJzAEqWeLUd3foqgIuH0AO7w1T5c7k8zHQlPobAlIk5g13YJeUEyDTELf7q3vyMbpzX5F95tVCuz9Cd1ULSnEbXTpggZjafg7WpPJE5-lAIr0TGZB5u9fLUNWBqdZHYY-l8Aj5B7tvI98uPuzF8FHpkWP12JJcLJZJx6jCtVJ2IpiueA5MG4nuw5MelIB0tQFVFsFDd4XVNpPP9txm4RwNTOjamKTmNsGgaKiqIwH9fnanGSn2PFnCDCmFCtwS3iruSPfiKvG7ibd46_pFmB64Fhz996rg-9GwmRB1RwYRScNNC_rOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیرخوارگان حسینی
🔹
مخاطبین عزیز خبرفوری؛ پویش بزرگ شیرخوارگان حسینی جلوه‌ ارادت کودکان شما به آستان حسینی است.
🔸
برای شرکت در این پویش کافی‌ست  عکس‌های فرزندان دلبندتان  را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/660956" target="_blank">📅 23:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660955">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
نقطه عطف روابط ایران و آمریکا در روز سرنوشت ساز
👇
khabarfoori.com/fa/tiny/news-3223984
🔹
پیام رهبر انقلاب درباره تفاهم‌نامه ایران و آمریکا/ بنده نظر دیگری داشتم؛
👇
khabarfoori.com/fa/tiny/news-3224046
🔹
افشای جلسات فوق‌محرمانه ترامپ | خشم ترامپ از افشای مذاکرات جنگ ایران
👇
khabarfoori.com/fa/tiny/news-3223914
🔹
ادعای عجیب سازمان اطلاعات آلمان درباره ایران
👇
khabarfoori.com/fa/tiny/news-3224032
🔹
پسری که همه چیز دارد | رضا پهلوی؛ شاهزاده لاکچری و روایتی از یک گسل طبقاتی
👇
khabarfoori.com/fa/tiny/news-3223831
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/660955" target="_blank">📅 23:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660954">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1E3WSYcPfjuEbYUuIRTgmVO5VRDqo9CzHdGM64qzWP2nwOh6bgNfVCTjD8o7vAE0kykIE_97_aBhxiVezcr3ESqLLQ183HuFkTdPVlNQVMerjZBJhUacir3oZ1KIsGH_At-R9ODhAKVs51sxtP2-zqWXW4Pf0MmedfrWviuTl-eo_FU3PjKqd5Mst6ia9quAmonXmHY0xqnr2ppY1yzNCjnvb3zi6pg-x7Umkve-YKK018hY2jNx0NLIrT5Faks0JlurVlgbiKYv-ELVhK8hfy_GYX8CukasywzpqB5avHN8U7ZFZHRnUnAV5Nllob00h5WJKZpWNziUddYR9rCtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیت‌کوین به زیر ۶۳,۰۰۰ دلار سقوط کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/660954" target="_blank">📅 23:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660953">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
المیادین یه نقل از یک منبع آگاه:
هیئت مذاکره کننده ایرانی سفر خود به سوئیس را به دلیل تداوم حملات اسرائیل به جنوب لبنان متوقف می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/660953" target="_blank">📅 23:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660952">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
نبیه بری، رئیس پارلمان لبنان: تأکید می‌کنم که موضع لبنان و
پایبندی حزب‌الله به آتش‌بس، تا زمانی که «اسرائیل» به‌طور کامل و همه‌جانبه به آن پایبند باشد، ادامه خواهد داشت
./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/660952" target="_blank">📅 23:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660951">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✉️
متن کامل رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا
✏️
بسم‌ الله‌ الرّحمن ‌الرّحیم
🔸
ملّت پرشور و باوفای ایران
💬
همانگونه که مطلع شُدید، تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و امریکا امضا شد. در مسیر رسیدن به این…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/660951" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660950">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a555eaaf9e.mp4?token=YBa5yOjcPFsJoM7uM3sDKT4VgjVCwM7i8dSksn4rXKPft5PnfetM8_mzXvOgIptScpLurUDgeFL9lPoCng835bOUrH_0o9S3390TgYQX_tE2YY_zk_l-rCldUH0ysfIcRn2j2Ie4DbyD8Rvuze50IVz8_LTPBtvb8JVLUI8DAEVCrTYDQEVSqbhUcB17uL1rqS18nhiDX-fvx7pV4Jx01aO-EPD1hFwhK8RSWfbRwdgmqDkKGuRVRuSIgnZAaatZVtZ_-AGBKwY2zkkeeU-Kn8uSdNCk9odMtrMPJkwrSWmTKGQXfQhpgC5inf6-wVLYJ2ySgCxfLrnshppYCSSO3bcAVRaJ2IgiFoWIiXxQQTiV7f-juIWau5VrxGbfGN-GC6Lw2wSqbtv1Pnjbn14-0QNS7kG1YKkHifQ4J0SHf4SO3cR3zJDhOXaG6YO4J3UGu7Nux5Qaac8Z_Eg6qiqWTTUK4mhmd_4tYEgKjgREHPxRmotcgv9MNH9txObm00Y36_LHhafoiiU_an-ogbKmQdLUKw61ok92gbuluVpzYG5Z3N5oYG_-AL2Ozs7ce4CydRNyC6OoODubQGtRmvGTaZ5Te7DjD01zaCA7xgIHUm76bMzAiW3KDrioXEw5oxUOKX-snSyvmKeDvTClo3RDdiaSSYd7x92xyJynYYo1hLc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a555eaaf9e.mp4?token=YBa5yOjcPFsJoM7uM3sDKT4VgjVCwM7i8dSksn4rXKPft5PnfetM8_mzXvOgIptScpLurUDgeFL9lPoCng835bOUrH_0o9S3390TgYQX_tE2YY_zk_l-rCldUH0ysfIcRn2j2Ie4DbyD8Rvuze50IVz8_LTPBtvb8JVLUI8DAEVCrTYDQEVSqbhUcB17uL1rqS18nhiDX-fvx7pV4Jx01aO-EPD1hFwhK8RSWfbRwdgmqDkKGuRVRuSIgnZAaatZVtZ_-AGBKwY2zkkeeU-Kn8uSdNCk9odMtrMPJkwrSWmTKGQXfQhpgC5inf6-wVLYJ2ySgCxfLrnshppYCSSO3bcAVRaJ2IgiFoWIiXxQQTiV7f-juIWau5VrxGbfGN-GC6Lw2wSqbtv1Pnjbn14-0QNS7kG1YKkHifQ4J0SHf4SO3cR3zJDhOXaG6YO4J3UGu7Nux5Qaac8Z_Eg6qiqWTTUK4mhmd_4tYEgKjgREHPxRmotcgv9MNH9txObm00Y36_LHhafoiiU_an-ogbKmQdLUKw61ok92gbuluVpzYG5Z3N5oYG_-AL2Ozs7ce4CydRNyC6OoODubQGtRmvGTaZ5Te7DjD01zaCA7xgIHUm76bMzAiW3KDrioXEw5oxUOKX-snSyvmKeDvTClo3RDdiaSSYd7x92xyJynYYo1hLc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظم عجیب و با شکوه افغانستانی‌ها در شب چهارم حسینیه معلی شبکه سه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/660950" target="_blank">📅 22:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660949">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
عبور رایگان کشتی‌های تجاری از تنگه هرمز به مدت ۶۰ روز  شورای عالی امنیت ملی:
🔹
طبق یادداشت تفاهم اسلام‌آباد، کشتی‌های تجاری متقاضی عبور از تنگه هرمز باید درخواست خود را به مدیریت آبراه خلیج فارس ارسال کنند و به مدت ۶۰ روز هیچ هزینه‌ای از آن‌ها دریافت نخواهد…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/660949" target="_blank">📅 22:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660948">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d77b8275dc.mp4?token=g6LglDqqm3Qqh6bboBnExpWNG-WO4s-FPhXt8xDs4RHKNMhiu7snvHVjrDpcJ1YrKOTiBftqi9DgCz0TRAfarv8p7EKAVZ--h6FC4myWLwBRo-xYaXed7PYgId3EDDFgpPerWrrQMr8ymuhaCK0hNYhEPGCx3IFcbwrRgMLgEq83a2EAXWz1Cc691jjmiLWFebXn2Bdaoy6BhtuffOK_tkFWh9fFLSMh9vfBWJB-XyaSVNHGiH5HSLe1Lm-2L_x4m9K6sT4EMiC_xXwrFKx7EqES3TaCrQZ5jagQEnVE2UNMfEaZP7zAYGPRA8vrEq6Kmkj3Cd_BnBQ0dN8rRIKP6Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d77b8275dc.mp4?token=g6LglDqqm3Qqh6bboBnExpWNG-WO4s-FPhXt8xDs4RHKNMhiu7snvHVjrDpcJ1YrKOTiBftqi9DgCz0TRAfarv8p7EKAVZ--h6FC4myWLwBRo-xYaXed7PYgId3EDDFgpPerWrrQMr8ymuhaCK0hNYhEPGCx3IFcbwrRgMLgEq83a2EAXWz1Cc691jjmiLWFebXn2Bdaoy6BhtuffOK_tkFWh9fFLSMh9vfBWJB-XyaSVNHGiH5HSLe1Lm-2L_x4m9K6sT4EMiC_xXwrFKx7EqES3TaCrQZ5jagQEnVE2UNMfEaZP7zAYGPRA8vrEq6Kmkj3Cd_BnBQ0dN8rRIKP6Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شریعتمداری: با مصادره اموال آمریکایی‌ها و متحدانش از طریق تنگه هرمز باید از آمریکا غرامت بگیریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/660948" target="_blank">📅 22:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660946">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S987nQZYpUk2UGjXQx8_nqUGqyCOZLiveodwMysFkLQFluWnG3IZca-U3P0_TU1BLQHCIiejESWZzS5FrkskYJw8p9krfpyWI24qGZS-BDcCYUnHTndWs_OBKswe-0tpHQzH_sC6gy8zJ0mNtz_8BgSjLlAQgmyun9NwrAwIguqBSPvwcYNAZ-OXqX7IlHRULLe8_rDdh5mgOYvMachDkNa02Ctme-R9oCcqyuU95qDJdkr06x0XOpsgDAlpOne29HEcqGBWigBPfi_UvtS7G8SanBF5FrqoWd2aLmRutPJ5t1XreXDpWiHJZ97427Gd4e6XVwHWWkaMUxmrJ6N11A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
رامین رضاییان بالاتر از اولیسه در صدر خلاق‌ترین بازیکنان دور اول جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/660946" target="_blank">📅 22:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660940">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImpBFIpRPXpceBkv_RlEEt70OpOjpNr90qmAGq49wuexjv_qXCPxvGpGpmCs6HB4YnkfDLwfU2jD6-1zB-C9FQ8BbL2NYYXrn3ZSzVzY1ISeEa0dVuGEOrkoE9S3nJ7P_ztD77VPF7wZAw-kwDTphMo1pFpwg38rQqSsWsOaFkOXJrgDWuJdEl83okJ9t-kAh_w0SDhF5Mi9Y2oyB4iW5rUwAsrGO29nwrXPp2-GNUX2Xmx9pWWvqGLnofJEi2S7LxoOnrBQxII2P78D94wRgEI05V3E7-ZMg_Ms8-jVcsQkcBXBA205QUxFE_6ONjilVyX-svuVy_mLhTtT-bHEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/925a0b51a7.mp4?token=YQIn3DVSDqetukUgLqJytoxhMgS3tqPUKDI67bfMvFqPtVeiTG1Lm-6F1W_0E-enz7caNWaAPWC0-NG3j7mJ1PlvZQb0TWMRH0vKUmCFl3iydn-hysADxcMmhEIyef-VMuZh9WasuxFDhGpbwmkzOMAEQIz5J9LYa3t0Yyo0I8HwoZV0q_aM5x-ERTKLZySYqJhIsZqAwytyxEcxTiZS7peEiREHTeJdSDJNQzZD_s6J7aAkhe4s9-Vziz0bECzkXwxKj-PCeBOKkbq90RPJOq9OnoPUzG0NqJlFRK5CpryjVTg8QyzPSsbtvzGJUlFgI0BtdMfHm_VfpT3WYZ4XlHgmzIoy6CUQM-Rwz6gyyWj3pe9CGpWMSUlEy9qkzAPNW6019rtVXqoUUUUwDTe_vpEUrg4eNGgwRnLN3WQZpwWCwky0nWpPC3hl6iCP9t-cG2eGnJunR8wd2Py-0xaNJgl5SzAP_OpcM20PfaOEb4YwTB8Um_h4x7QqTgy1MQrKG_Q3_zF9cAQ6GGtgZdM7XDcBca3Fewh-_kKvjv2eYLLpAemWBhlDKqw8rsDFZjxhNVrNOnYn3SHzMp4or15GUmJSO2x5dVxZZSGI-E2ZGPMPbpdDQTecilYw3o1qEcyeKbg0rH-I3HzKiVFdScMVm9GMbVU9CRR9INS0V3NDeQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/925a0b51a7.mp4?token=YQIn3DVSDqetukUgLqJytoxhMgS3tqPUKDI67bfMvFqPtVeiTG1Lm-6F1W_0E-enz7caNWaAPWC0-NG3j7mJ1PlvZQb0TWMRH0vKUmCFl3iydn-hysADxcMmhEIyef-VMuZh9WasuxFDhGpbwmkzOMAEQIz5J9LYa3t0Yyo0I8HwoZV0q_aM5x-ERTKLZySYqJhIsZqAwytyxEcxTiZS7peEiREHTeJdSDJNQzZD_s6J7aAkhe4s9-Vziz0bECzkXwxKj-PCeBOKkbq90RPJOq9OnoPUzG0NqJlFRK5CpryjVTg8QyzPSsbtvzGJUlFgI0BtdMfHm_VfpT3WYZ4XlHgmzIoy6CUQM-Rwz6gyyWj3pe9CGpWMSUlEy9qkzAPNW6019rtVXqoUUUUwDTe_vpEUrg4eNGgwRnLN3WQZpwWCwky0nWpPC3hl6iCP9t-cG2eGnJunR8wd2Py-0xaNJgl5SzAP_OpcM20PfaOEb4YwTB8Um_h4x7QqTgy1MQrKG_Q3_zF9cAQ6GGtgZdM7XDcBca3Fewh-_kKvjv2eYLLpAemWBhlDKqw8rsDFZjxhNVrNOnYn3SHzMp4or15GUmJSO2x5dVxZZSGI-E2ZGPMPbpdDQTecilYw3o1qEcyeKbg0rH-I3HzKiVFdScMVm9GMbVU9CRR9INS0V3NDeQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
ویژه شب چهارم محرم طفلان حضرت زینب (س)
🥀
رو سفیدم میکنند و فخر مادر میشوند
نوجوان هایم سپر های برادر میشوند
این پسر ها پیشکش های من و عبدالله اند
صحبت جنگ و جدل باشد قلندر میشوند
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/660940" target="_blank">📅 22:30 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
