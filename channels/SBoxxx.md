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
<img src="https://cdn4.telesco.pe/file/hl7kt4s1PeHmWzIeqfhHTtAwXVL9a8moU3APpVefCnevrTjXgD05pRN31QO9HFj4K7XqKx_kn1Tos5U6XnMWmEcuLyCynxL3ylThy1dBfOz3tP1hfglbRMWmM6k353Ojn3OOUUfymnUiEDuXH7EsMcM2lGMVCKYCnnRUBsXQuFLJwnYd1ybGI8CAWYjzLhkBMdTnjIDiMJd8kSknL3yEJ3uaO-_tR7AVkUilhL1EycZKu7RByqtDVRzhfRrWHuwyCzQ1uGCkLesMfgjccs6yOfK9eZdoiqvelPnDx4dB8vk3TN1Ek-4h0XxcEhfqO2UWRvpWRvu8LXmFFHHx_vPaHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.8K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 20:19:53</div>
<hr>

<div class="tg-post" id="msg-20984">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">#FairValueCurve  نمایه FVC نشانگر نزدیک شدن طلا به محدوده قیمت منصفانه است و لذا از حالت حباب منفی ارزشگذاری فاصله گرفته است (به دلیل رشد سنگین از پریشب) هر چند هنوز تا تشکیل حباب مثبت و بیش خرید بودن فاصله زیادی دارد.  پس بهترین استراتژی برای امروز:  خرید…</div>
<div class="tg-footer">👁️ 826 · <a href="https://t.me/SBoxxx/20984" target="_blank">📅 20:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20983">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">العربیه:
وزیر کشور پاکستان طی ساعات آینده به تهران سفر خواهد کرد.</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/20983" target="_blank">📅 18:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20982">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران
انقلاب اسلامی ۴ موشک کروز ضدکشتی به سمت تنگه هرمز شلیک کرد</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/20982" target="_blank">📅 18:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20981">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNOBqGd39VbTIecWv47x9zxpxg4zTqDYckbncYzt8lobxrSXMfvtDfyi-YNNA9RUX9UDb6Kpj3htM6Au6Vty8cbtzddy5EufE-qk7fiUnpAnG_t9aub-jc2-8baXBChO0u2ae0Dv7teF57Pbnvjnz_rEsofXPNAxHpX44AtI_gWcYkKRoCQ3QRsYy_i2ZEg_ocupSOe35oaXCiI8ZqbggP9-slBLTrOttg1o2k0xSpAtLD8IXn8vb6_QPoJUgOb-7-D-fKu5dUenC0yD2Rk6k_lTvauCaItaQXvPcH6sIxiIg2Ys99dw3roDxklOdcPVMAH-G_5R_6tp6hV8b3Zvag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توصیه دکتر پزشکیان به جانفدایان:  کمتر مصرف کنید!  (پسر پزشکیان هم دیروز همین را گفته بود)</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/20981" target="_blank">📅 15:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20980">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573e6b119d.mp4?token=WtVekNt6J5hS8lPs12Mr5Dg2ddmiOFhwoenzhtl4zZA9QVOYXBR2_A5zVeFnjt8cHh7f-W0lK6cCbwajLztKdXa9NCzHSmOenfJReFke4GqXxOfa9ByS_jdeI75jJkqQSUSkZd_xO-XHPU3U6MV6eXBHt6wqcIDfqI53mrxc0wnp6kklmF549FrAVAE3piHFKy735yF5OvR3qVbJOpX90-Cyvyhly-_wTlCWx4f_slqJS06q3NSF9cSy5ywyjQdRfM_XZ0XZsFcfpYzdWVHLNKby2RsK933Gr9xID5yQ1_lDMYh0b6XwwT_098CJ1vi-IkXx-1O2f4BOuFQY3o043w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573e6b119d.mp4?token=WtVekNt6J5hS8lPs12Mr5Dg2ddmiOFhwoenzhtl4zZA9QVOYXBR2_A5zVeFnjt8cHh7f-W0lK6cCbwajLztKdXa9NCzHSmOenfJReFke4GqXxOfa9ByS_jdeI75jJkqQSUSkZd_xO-XHPU3U6MV6eXBHt6wqcIDfqI53mrxc0wnp6kklmF549FrAVAE3piHFKy735yF5OvR3qVbJOpX90-Cyvyhly-_wTlCWx4f_slqJS06q3NSF9cSy5ywyjQdRfM_XZ0XZsFcfpYzdWVHLNKby2RsK933Gr9xID5yQ1_lDMYh0b6XwwT_098CJ1vi-IkXx-1O2f4BOuFQY3o043w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از اروپایی بودن همین را فهمیده که یک لامپ را خاموش کند!  در حاکمیت قانون و مدیریت عقلانی و کرامت انسان هم اروپایی بشویم یا نه؟!</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/20980" target="_blank">📅 15:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20979">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ضرغامی در سالگرد ⁧مهسا امینی:  امروز همه تصمیم‌گیران و تصمیم‌سازان، بر اشتباه بودن ‏روش  گشت ارشاد  اتفاق نظر دارند‏   ظاهرا همیشه باید مصیبت‌ها و مقاومت‌ها ما را به راه و روش درست هدایت کند</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/20979" target="_blank">📅 14:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20977">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ضرغامی در سالگرد ⁧مهسا امینی:
امروز همه تصمیم‌گیران و تصمیم‌سازان، بر اشتباه بودن ‏روش  گشت ارشاد  اتفاق نظر دارند‏
ظاهرا همیشه باید مصیبت‌ها و مقاومت‌ها ما را به راه و روش درست هدایت کند</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/20977" target="_blank">📅 14:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20976">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یادداشت بسیار مهمی است و نکته اصلی اش این است:
جهش بهای نفت و افت قیمت اوراق قرضه به تنهایی موجب تسلیم شدن ترامپ برای پایان جنگ نشده و احتمالا هم نخواهدشد.</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/20976" target="_blank">📅 14:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20975">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جی‌پی مورگان از تلاش برای پیش‌بینی پایان جنگ ایران و ترامپ دست کشید
جی‌پی مورگان اعلام کرده است که دیگر برای جنگ ایران یک
سناریوی پایه (Baseline Forecast)
ندارد؛ چراکه قیمت نفت، بازده اوراق خزانه‌داری آمریکا و قیمت سوخت از سطوحی عبور کرده‌اند که این بانک پیش‌تر انتظار داشت عبور از آنها واشنگتن را به سمت دستیابی به یک توافق پایدار سوق دهد.
عبور از خطوط قرمز اقتصادی، به خروج از جنگ منجر نشد
در آغاز جنگ، جی‌پی مورگان بر این فرض بود که افزایش فشار اقتصادی در نهایت دونالد ترامپ را به سمت توافقی برای بازگشایی تنگه هرمز سوق خواهد داد.
مهم‌ترین آستانه‌هایی که این بانک در نظر گرفته بود عبارت بودند از:
• نفت بالای
۱۰۰ دلار در هر بشکه
• بنزین در محدوده
۵ دلار در هر گالن
• بازده اوراق خزانه‌داری ۱۰ساله آمریکا بالای
۵ درصد
شش ماه بعد، چند مورد از این سطوح شکسته شده‌اند.
ناتاشا کانوا، رئیس استراتژی جهانی کالاهای جی‌پی مورگان، در یادداشتی در روز پنجشنبه گفت:
«شش ماه بعد، بسیاری از این خطوط عبور کرده‌اند، اما استراتژی خروج نه‌تنها روشن‌تر نشده، بلکه مبهم‌تر شده است.»
او افزود:
«برای نخستین بار از زمان آغاز درگیری ایران، ما دیگر دیدگاه پایه‌ای نداریم. واقعاً نمی‌دانیم پایان این جنگ را چگونه مدل‌سازی کنیم.»
هیچ نشانه روشنی از کاهش تنش وجود ندارد
جی‌پی مورگان معتقد است شواهد چندانی وجود ندارد که نشان دهد واشنگتن یا تهران در حال آماده شدن برای عقب‌نشینی هستند.
به گفته کانوا، هرچه درگیری به جای کوچک‌تر شدن، گسترده‌تر می‌شود، دفاع از این دیدگاه که اختلال در عرضه انرژی کوتاه‌مدت خواهد بود، دشوارتر شده است.
در همین حال، عربستان سعودی پس از آسیب دیدن خط لوله در پی یک حمله پهپادی که از عراق انجام شد، خط لوله
شرق–غرب
خود را متوقف کرده است.
همچنین شبه‌نظامیان حوثی همسو با ایران پیشروی‌هایی داشته‌اند که می‌تواند موقعیت آنها را در زمینه کنترل یا ایجاد اختلال در تردد نفتکش‌ها در بخش جنوبی دریای سرخ تقویت کند.
ترامپ نیز روز پنجشنبه به Axios گفت که در آستانه تصمیم دیگری درباره این موضوع قرار دارد که آیا عملیات نظامی گسترده علیه ایران را از سر بگیرد یا به سمت پایان دادن به جنگ حرکت کند.
ترامپ گفت:
«یک تصمیم بزرگ پیش رو دارم. آیا می‌خواهم وارد عمل شوم و آنها [رژیم ایران] را نابود کنم یا نه؟ این یک تصمیم بزرگ است. هر اتفاقی ممکن است از سوی من رخ دهد.»
بازار نفت، کاهش بیشتر عرضه را قیمت‌گذاری می‌کند
جی‌پی مورگان ارزش منصفانه نفت برنت را حدود
۹۰ دلار در هر بشکه
برآورد می‌کند، اما شاخص بین‌المللی نفت اکنون نزدیک
۱۰۵ دلار
معامله می‌شود؛ در حالی که در اوایل این هفته به محدوده
۱۱۰ دلار
نزدیک شده بود.
این بانک محاسبه می‌کند که به ازای هر
یک میلیون بشکه در روز
کاهش عرضه نفت، حدود
۴ دلار
به قیمت قراردادهای آتی نفت اضافه می‌شود.
بر همین اساس، کانوا می‌گوید بازار در حال قیمت‌گذاری ریسک از دست رفتن حدود
۴ میلیون بشکه در روز عرضه اضافی
است؛ آن هم علاوه بر حدود
۱۰ میلیون بشکه در روز
عرضه‌ای که هم‌اکنون دچار اختلال شده است.
تصویر کلی بازار انرژی با حملات اوکراین به پالایشگاه‌های روسیه نیز پیچیده‌تر شده است؛ این در حالی است که ترامپ روز دوشنبه گفته بود کی‌یف و مسکو توافق کرده‌اند حملات به تأسیسات انرژی را متوقف کنند.
ذخایر نفت همچنان یک حائل ایجاد می‌کنند
مهم‌ترین عامل محدودکننده برای افزایش بیشتر قیمت نفت، حجم نفتی است که همچنان در ذخایر نگهداری می‌شود.
ذخایر تاکنون
۵۵۵ میلیون بشکه
کاهش یافته‌اند؛ رقمی که به‌مراتب کمتر از کاهش
۱.۶ میلیارد بشکه‌ای
است که تیم کالاهای جی‌پی مورگان در ابتدا پیش‌بینی کرده بود.
بنابراین بازار در برابر یک شوک طولانی‌مدت عرضه، نسبت به برآورد قبلی بانک، همچنان از
حاشیه امنیت بیشتری در ذخایر
برخوردار است.
کانوا در جمع‌بندی گفت:
«خلاصه اینکه، فعلاً هنوز به اندازه کافی ظرفیت ذخیره و عرضه پشتیبان وجود دارد که قیمت‌ها را مهار کند.»</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/20975" target="_blank">📅 13:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20974">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خلیل شیر غلامی، سفیر ایران در ارمنستان؛    «ایران رویکرد ویژه‌ای نسبت به مسئله تمامیت ارضی و حاکمیت ارمنستان دارد و این را یکی از مسائل حساس خود می‌داند. با توجه به اهمیت منطقه سیونیک به عنوان یک مرکز استراتژیک برای ارمنستان، به ویژه در زمینه حفظ ارتباط با…</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/20974" target="_blank">📅 11:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20973">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خلیل شیر غلامی، سفیر ایران در ارمنستان؛
«ایران رویکرد ویژه‌ای نسبت به مسئله تمامیت ارضی و حاکمیت ارمنستان دارد و این را یکی از مسائل حساس خود می‌داند. با توجه به اهمیت منطقه سیونیک به عنوان یک مرکز استراتژیک برای ارمنستان، به ویژه در زمینه حفظ ارتباط با ایران، هر پروژه‌ای، از جمله پروژه TRIPP یا هر طرح دیگری که تهدیدی برای ارمنستان یا روابط ایران و ارمنستان محسوب نشود، از نظر دیپلماتیک، مشکلی ایجاد نخواهد کرد. در اجرای هر پروژه‌ای، تمامیت ارضی و حاکمیت ارمنستان نباید به خطر بیفتد.
علاوه بر این، حضور آمریکایی‌ها در مرز ارمنستان و ایران نباید تهدیدی برای ایران باشد.
اگر این دو شرط محقق شوند و همچنین منافع ارمنستان در نظر گرفته شود، ایران مخالف اجرای پروژه TRIPP نخواهد بود.»</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/20973" target="_blank">📅 11:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20972">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم و پیش بینی میکنم این هفته طلا سطح 4400 دلار را پس بگیرد.</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/20972" target="_blank">📅 11:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20971">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">طنز تاریخ در این است که پیمان دفاع مشترکی که عربها با ترک‌ها بسته اند دقیقا ۱۱۰ سال پس از جنگی روی داده که میان خودشان در قالب شورش «شریف حسین» ضد عثمانی ها درگرفت و اتفاقا نخستین شهری که عربها آزاد کردند همین «مکه» بود که نامش اکنون شده لقب پیمان دفاعی اخیر!…</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/20971" target="_blank">📅 11:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20970">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coK1LljTQ4Ih-_izl3FfNGcMuV40FtGLqIkzihLz0DQkCm1wpFdnEMC7TXicOnrAGuzODChiw8gRh43-fAFSM9SGJgvLWaFfrFpuJ1BN0XCU5ZpNYagqYrmAXT0u1_Ug-XarnUF84bg-Nco0s1gnnXuDrtHdLV_hH0WjBg4iJptJ8PvzknZW6vRZlwWT515L5i8NyckWWT2mWMC9iXt1gALw-sBtTQA9ybDFYgPmmQF8GMw6Quuh-KxKWN6DLBSulj5MoWrsb2S6eg-lSw_llu96jR3fqPeAEAgwEqEtPfzvM65F9Nm1WyWMWzWtiq9RM1v8kU4QOcXdp5kcsl_JGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC نشانگر نزدیک شدن طلا به محدوده قیمت منصفانه است و لذا از حالت حباب منفی ارزشگذاری فاصله گرفته است (به دلیل رشد سنگین از پریشب) هر چند هنوز تا تشکیل حباب مثبت و بیش خرید بودن فاصله زیادی دارد.
پس بهترین استراتژی برای امروز:
خرید پس از یک اصلاح سنگین 400 پیپی است.
محدوده های پیشنهادی:
4366
4355</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/20970" target="_blank">📅 10:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20968">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgeMW1jrtvKogW-gPq7st5EU3tiTV9HLy86rI9K1AApzmgrSbkunoF-mseit-cuMb1HJmivFx9knze48q23_DdnbGt3lSWctVFs4Yt9TwIrrywkF_315Q9fM3mRQ4w93njqWbxg2pKYifq7n1V4NX8-MtgBocEg4jGnYO-8HX0FaZkyRqzk6HKSTOgbVTVExFzNoDxMsUwQJDwUM-xyMfNdLkKp_vnU_J7ueF7rXUXJ89usC-EI3jGki236RMBvs38XwGubdhWCSI9hLpY5vemljp_VIJ9Q3Yow7xT85UFHBP3CRBfPGbv81QOR6sp6Ug3Tv1WFR32BfNHcIo8OX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بالایی قرار دارد و انتظار یک اصلاح نزولی قابل توجه (دستکم 400 پیپی) در طلا داریم.</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/20968" target="_blank">📅 10:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20967">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر دانشگاه تهرانی ها</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1dc786c4.mp4?token=QXk_9ZHECEo0kn5RQEbr8a1DRCxQ53jazwCtrLzrMeNyl6Di6NbFE9KCAxxt9GMST2pXUjcWFqr2TQ67zUFZtv39QZR-RJEhJB9R_zmyYoW5n0SqsYMkjWy7L2AiH40uKPXUQdcKzi-8nBfAdP5evwX-tTFlqVRVeCBI7RzFeRbYquMuIyhWMxSrxfLxZj6Y3AZ10fT2vK8V8mmP88dTPRp8jEwjL8D4PX9bNy1he0RyZ7Bfu9s2nKe-gLKG0UdiMYI-9YboijqKsu_OBenHjJxmo9HCEmjkpxaQXBS8BvPOYqRZyLqHevYqulZM9T4oFP8DQFCcQJWg43tFTvdtbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1dc786c4.mp4?token=QXk_9ZHECEo0kn5RQEbr8a1DRCxQ53jazwCtrLzrMeNyl6Di6NbFE9KCAxxt9GMST2pXUjcWFqr2TQ67zUFZtv39QZR-RJEhJB9R_zmyYoW5n0SqsYMkjWy7L2AiH40uKPXUQdcKzi-8nBfAdP5evwX-tTFlqVRVeCBI7RzFeRbYquMuIyhWMxSrxfLxZj6Y3AZ10fT2vK8V8mmP88dTPRp8jEwjL8D4PX9bNy1he0RyZ7Bfu9s2nKe-gLKG0UdiMYI-9YboijqKsu_OBenHjJxmo9HCEmjkpxaQXBS8BvPOYqRZyLqHevYqulZM9T4oFP8DQFCcQJWg43tFTvdtbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهریار میگه آدمهای پیشه‌وری بچه‌های گرسنه تبریز رو جمع میکردن و می‌گفتن: « بچه‌ها بگید خدایا نان بده». نان نمی‌آمد، سپس می‌گفتند «بچه‌ها بگید
#استالین
نان بده» و نان می‌آمد.
اینها علاوه بر بی‌وطنی چقدر کثیف و کودک‌آزار بودند که با روح و روان بچه‌های گرسنه آذربایجان بازی می‌کردند
_sheshgalani_
@uttweet</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/20967" target="_blank">📅 09:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20966">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خریداران جهانی سوخت روسیه در برابر لایحه تحریم‌های ایالات متحده مقاومت می‌کنند
پولیتیکو گزارش می‌دهد که واکنش جهانی به لایحه تحریم‌های روسیه که به تازگی توسط کنگره تصویب شده، سریع و شدید بوده است:
مسکو هشدار داد که این لایحه تنها جنگ علیه اوکراین را طولانی‌تر خواهد کرد. هند قول داد از منافع خود دفاع کند و پکن در برابر آنچه آن را «حاکمیت گسترده غیرقانونی» نامید، مقاومت کرد.
این لایحه که هنوز به امضای ترامپ نیاز دارد، تحریم‌هایی علیه رهبری روسیه، بخش انرژی، صنعت دفاعی و شبکه حمل‌ونقل که سوخت‌های تحریمی روسیه را جابه‌جا می‌کند، الزامی می‌سازد. این لایحه همچنین به ترامپ اختیار می‌دهد تا تعرفه‌های ۱۰۰ درصدی بر ۵ خریدار بزرگ جهانی این سوخت تحمیل کند؛ بندی که از پیش متحدان خود واشنگتن را نگران کرده است.
از سال ۲۰۲۲، چین ۵۰ درصد از صادرات نفت روسیه را خریداری کرده، هند ۳۷ درصد، ترکیه ۵ درصد و اتحادیه اروپا ۵ درصد. اتحادیه اروپا همچنین در آن دوره بزرگ‌ترین خریدار LNG روسیه (۴۹ درصد) و بزرگ‌ترین خریدار گاز لوله‌کشی روسیه (۳۲ درصد) بوده است.
از سوی اتحادیه اروپا، منتقدان لایحه استدلال می‌کنند که این لایحه اختیارات بسیار زیادی به ترامپ می‌دهد؛ یا برای ایجاد استثناها و معافیت ها برای شرکای بزرگ روسیه مانند چین که واشنگتن به دنبال گسترش تجارت با آن است، یا برعکس، برای اجرای انتقامی علیه متحدان ایالات متحده که ترامپ از آن‌ها خوشش نمی‌آید، مانند اتحادیه اروپا، با استفاده از خریدهای نفت و گاز کشورهای عضو تکیه‌گاه (اسلواکی، مجارستان) بهانه می سازد.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/20966" target="_blank">📅 09:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20965">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">به گزارش برنا، در نخستین ساعات بامداد جمعه ۲۷ شهریور در محدوده خیابان دانشگاه زاهدان تیراندازی رخ داد که این خبرگزاری دولتی آن را «حمله به یک ایست بازرسی» توصیف کرد. برنا اعلام کرد در جریان این تیراندازی یک مامور نیروی انتظامی کشته شده است.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20965" target="_blank">📅 08:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20964">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:
نیروهای مسلح ایران به آمریکا درسی خواهند داد که هرگز فراموش نخواهد کرد</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20964" target="_blank">📅 01:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20963">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حمله ایران به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20963" target="_blank">📅 23:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20962">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یک کشتی ترکیه‌ ساحل اوکراین توسط پهپاد مورد حمله قرار گرفت.
بر اساس اطلاعات اولیه، کاپیتان و یک ملوان کشتی در این حمله کشته شدند و ۱۳ نفر دیگر زخمی شدند.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20962" target="_blank">📅 22:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20961">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ساعتی قبل وزارت خارجه آمریکا قصد دولتش برای فروش ۴۸ فروند جنگنده F-35A به ارزش ۲۴.۳ میلیارد دلار به عربستان سعودی را به کنگره این کشور اعلام کرد.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20961" target="_blank">📅 21:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20960">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ:   من آدمی فروتن و با سطح هوشی بسیار بالا هستم</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20960" target="_blank">📅 21:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20959">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این دیدگاه Secret Box هم تایید شد:  طبق اطلاعات افشا شده از منابع محلی، حدود ۵۰۰۰ تروریست یا جهادی که بیشتر آن‌ها از قوم اویغور و اهل آسیای مرکزی، از سوریه به یمن اعزام شده‌اند تا به عنوان مزدوران برای عربستان سعودی فعالیت کنند.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20959" target="_blank">📅 21:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20958">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این دیدگاه Secret Box هم تایید شد:
طبق اطلاعات افشا شده از منابع محلی، حدود ۵۰۰۰ تروریست یا جهادی که بیشتر آن‌ها از قوم اویغور و اهل آسیای مرکزی، از سوریه به یمن اعزام شده‌اند تا به عنوان مزدوران برای عربستان سعودی فعالیت کنند.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20958" target="_blank">📅 21:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20957">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حوثی ها دیدند هر کار می‌کنند این عثمانی و فاکستان برای دفاع از عربستان در قالب پیمان دفاع مشترک مکه تحریک نمیشوند این بار خود مکه را زدند!</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20957" target="_blank">📅 21:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20956">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20956" target="_blank">📅 20:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20955">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ:
تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است.
هر احتمالی از جانب من وجود دارد.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/20955" target="_blank">📅 20:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20954">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">— اسرائیل و یونان یک مانور دریایی مشترک برگزار کردند که شامل تبادل خدمه و آموزش برای سناریوهای مختلف، از جمله شرایط اضطراری بود.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20954" target="_blank">📅 20:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20953">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ:
من آدمی فروتن و با سطح هوشی بسیار بالا هستم</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20953" target="_blank">📅 20:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20952">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">#FairValueCurve  شاخص FVC اکنون سقف بالاتری برای طلا پیش بینی می کند و لذا فضای رشد فراهم است.  در نتیجه انتظار برای یک اصلاح تا 4300 الی 4290 و سپس اقدام برای خرید برای امروز منطقی است.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20952" target="_blank">📅 18:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20951">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نخست‌وزیر اسرائیل، نتانیاهو، می‌گوید که اسرائیل رژیم ایران را سرنگون خواهد کرد.
«این رژیم سقوط خواهد کرد.»</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20951" target="_blank">📅 16:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20950">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20950" target="_blank">📅 14:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20949">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6jZomfAimuCzmpdFyVUKbkGHjIb5yI4KWDqTgCADJ5scbFm6hDA_gjjJrPAzdWFpG6LJTBGkZ_f5BlFs6xXYTE3kWZqcCxSN_AQ-P5RvvQdoU90xzcm50mMKTzaLX7FsOXzpttVtUrhl3QJ0ufb0krHObn9m-B7bJ7tcLoCTORv1lzJg3ygWjOd--oTlQct7fEa4AvykKs4L-tIb-WHBxxrGt9V_zqn6Wj1JMg9GkGvFH0ZTzmHfWi-5qHAW08bMNgXrpZ7q_dSl_Pxy0RnL5Q0boW9z7O9K4U6vqf4Gz0eepIMzJkYTDv2OcuecvQzakjbbWLwdciKnimJFMW9bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
شاخص FVC اکنون سقف بالاتری برای طلا پیش بینی می کند و لذا فضای رشد فراهم است.
در نتیجه انتظار برای یک اصلاح تا 4300 الی 4290 و سپس اقدام برای خرید برای امروز منطقی است.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20949" target="_blank">📅 11:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20948">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilmLeAlxc6n4TqDYBJNQ0Ni68l6iv0izSWsY6JxeSvSfmCEnH9RIXTV88lxTnTggct7FWMXGkL513oyZgtUxQvajsqRG6SEFBGmc2m-WKxsYR37gi_h3pxo1wA1kKVGMhtzJXBTprowPZIRpEdAXZiPBy2l4JKEyqOhn7xL_Jp8chVRYVR2xghIVC_dLkvmvtGYwcpObX0OBxrO4qHC0Wy6p4aPnEbhgcWtbciyjOg6suZ7rIwIhcrW-ue1Fx29QnlXnhgew3a-8CLDMeUYvdIbEfs1iz2ObgiggYoARV9ZCA79TCz4Ra0A08saVd87mV1hQXH8S3OkAj_hSsbZVZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است و انتظار می رود یک اصلاح نزولی در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20948" target="_blank">📅 11:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20947">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">قیمت : ۴۲۶۰</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20947" target="_blank">📅 11:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20946">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldy5mROgH08-SefYWtzVaSjU-iQ270g9oIdzP0db50iZJVf69bYEOeCHokOaw616t5d-0z77qYAr1QT9eHmG9iUOajpezdtqHv8y8e1S_pxEEz6DX0aYCwg8UX3NZT5Cor03y57eFCCidOIVA4fpnEaLrcLRDrXmcDQpkMEpziQaLJM5OsFcVGUJrs3RqxcpYkccgtg67lE4denSY50JKEqFr4s_b9oFQkCoZb8ZcIqAGRQXyLueWoeRRxtLzm9nKSHb4vJ8Bjx2_yWHsNGTo32pQoBZoDVPVJ_iCIZBN5ZKJo_QiaEBmbzdYJgfY3PNSGR9m8ksowxRwc0uJLSHsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین توییت برگ افکن دکتر قالیباف</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SBoxxx/20946" target="_blank">📅 00:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20945">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شروع شد:  اخبار فوری: کاخ سفید افزایش نرخ بهره فدرال را «مایه تاسف» خواند</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/20945" target="_blank">📅 00:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20944">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/20944" target="_blank">📅 23:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20943">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H19_Z9UgNkP7TlPvND6l8l7NgMr5MbGfozRmjMHSHb7O36mqZO1U23Ud2FMwlN8WnoW2Vxp0X4fqyrHLYyEjwz8InahATUnb9G9tBLAf499y5LlW0rXt4XIt9z71vkWGBIbitWNa-5PL0GaHiYzR1A9xgVTLQP48fHCO-oDm-64AFND_ErYWpIKRvGTBXXzAtTkQJ6nQuwiVMADTyP_0C3MimwBuL6RjpxJuRmE0pWSQYW45yNsACfQ3k9X8_6KB_S8MFmef7HlKf3F8C0OmGuyJa3wlOjP02tMRP4VpKifUnDrvXls10FDFxQZRYujLGv1RwJsbgsFeOhbAottcXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پوزیشن دیشب برای همراهان ما ارسال شده بود.</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/20943" target="_blank">📅 23:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20941">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/20941" target="_blank">📅 23:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20940">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SajMQA4O76VRuJdPP65WxwLuAEZ84VthIzC4ejsR3K00p0wHv4ySd2mVbMwvA7g5bhq-77JtSPWzlsW7ZQ9J0ro_qpx0zjFqUJPZ6aeVc_jJ1obiYLR7WxggjcRK-uKe-9qD1JEBLLnA_Hx5W26RIqM72iXHn_ViiKtTAR-Xe7Ha2ZxUb6BXSeRMWxsba8YXL76qph2dgkdJA0V3by-snlWsLO2tzX7Nz1Hi45FqtZHzN18GyxZyTEWyU5EsWCmX6DF-FTcz2w9X1DyJIfHVBPFgLY3T5U0o5qf85DaPVnDr1V-xcesIbJ7uStNHiaDIfJvPbAzfMTkCfvma5nKgHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/20940" target="_blank">📅 23:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20939">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">قیمت : ۴۲۶۰</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20939" target="_blank">📅 23:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20938">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20938" target="_blank">📅 23:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20937">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شبکه کان عبری:
مقامات عربستانی به نتانیاهو اعلام کرده‌اند که اگر اسرائیل جلوی پیروزی یمنی‌ها را بگیرد عربستان سریعا با اسرائیل روابط خود را به طور رسمی عادی‌سازی خواهد کرد/کویت نیز بعد از حملات ایران همین قصد را دارد/اردوغان نیز با محکوم کردن یمن پروازهای ایران به ترکیه را لغو کرده است</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/20937" target="_blank">📅 22:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20936">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">به دلیل ورود حداد عادل به تبریز چندین فواره بزرگ توسط شهرداری تبریز پرتاب شده است، به دلیل اینکه فردا میلاد و هیچ جشنی نیست مردم تبریز فکر کرده‌اند پدافند فعال شده است.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20936" target="_blank">📅 22:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20935">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">به دلیل ورود حداد عادل به تبریز چندین فواره بزرگ توسط شهرداری تبریز پرتاب شده است، به دلیل اینکه فردا میلاد و هیچ جشنی نیست مردم تبریز فکر کرده‌اند پدافند فعال شده است.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20935" target="_blank">📅 22:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20934">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0siv2HNY-XnThqjRjM6630IU-nuJXhgxtxJWFbEpGOF0POGt5zFqupcJBUR_XfMTHttsHVFhl4tByBLpErBAsSAl1SP413vBQccfIwINyjCkx729fYXxMeED5xAXGjLlmwY-5PYz5vXf1aZ85KcQw-M2d9IVzJE-gT6563J7G0_6TgJa_YTNKetkgcyNaVmdgPgoCtO4nBUt__Q-dIxKLcYzhmjylBDzS7N6XFTxoIRxuCl1wuqU2GrjQg0gQjqlnJeKWOwmbY3pemLVhIM7fJMUYUWPBMYu-isGOZOSRWgf1oYq5YinMFvQPco73Jr08XdT729gB_AHHEMaz3Jng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی در سطح بالایی قرار دارد و نظر به رشد طلا از این محدوده (4340) انتظار افت داریم دستکم تا 4300</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/20934" target="_blank">📅 22:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20933">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AS0qAFf_Twz7VrkR9f3DR-oI5hmvsmKahN4lyGIAxUHCVpGSBkyFq81of-SDszSzpen72KJioMOg6amTk9-lNWSLfF8N-dyR12i2mJoWt5CMIkVPVfaZyjFbUfK1tJ9zeTxBN8CZrHx0XtoE6Rw-hLQ4Crxfow_gOpByYMuXHjNns8RZehQOQ87Nyz_jWVGPgfVDf-z-1m8QVp56WjkTiSiSWFcsyt7EUwREX2Th-cEC3FmZoEi4SWRrwympzsXWNBnf4qo0oTUs172RwO7kqWr2ASY0rxWbI5hTbUAESCFwiI2lAkhlP-ZMNjzvJw6zJuX2Fn4OvMoToqjyNLzunQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SBoxxx/20933" target="_blank">📅 21:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20932">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNeL8UAeF_wjyKFTE3Crc7CeUtqnPShbesSzdx5hjPvpGSsTnBnkzj8oiMd4hyfHzD05_zhMoIRYh4ZYNadSO0yf819dDjCi_SsZWU7y0c4471t-05_I42cWzEy-NES8RwDbpW5v3ctuyGC92FZS_7rrpNPW3zLgczKLE47yxhrEOwL61c5vWL0cXGMhmhgo255YzL73LC9L35WUpzk4sAn8x1IzQGxKxmJNJV2bCDTT7mTad2TPT-5wKjm36mOjR_9hgWMxuFn_VWFjJsVgMMW65rjDkCsDTe6XefZ7X3PToZgoTeD8Nn4ax8pLXedmDK1iAX423d_K9iYnUWOadg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20932" target="_blank">📅 20:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20931">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6727faabd4.mp4?token=NQZNhlC8k5a5ItbI9Vv_4Utcne926rX0eGFSrgey4-nm2Rlx_QnidfhqgLGJBjAHia_O9SvjWXrzbj_DN3DPH2k-l5JGiWSvEcmSHHBvq-AGhn8Zyg4T5Xl50EKa-fDmgKEjF5f97X7Xpj0kc651YFqtf1pj2YNLxHiSe2mrPvz8C1iAFcTBIU_cNCs8mdOQaA3m-VsGumKTPsPysAxb_lxcAZJHQ7WJYtrECu659eB3LR47nCiR2i65dgp5lv9e7elmv67RdXgWCSb4ZT6GsfDWc-skzBSlgyZOkgRNwNUWZxCjIE0CDqzNGrYOkY_8IAsjT9l2-V-1iS1n-aKldQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6727faabd4.mp4?token=NQZNhlC8k5a5ItbI9Vv_4Utcne926rX0eGFSrgey4-nm2Rlx_QnidfhqgLGJBjAHia_O9SvjWXrzbj_DN3DPH2k-l5JGiWSvEcmSHHBvq-AGhn8Zyg4T5Xl50EKa-fDmgKEjF5f97X7Xpj0kc651YFqtf1pj2YNLxHiSe2mrPvz8C1iAFcTBIU_cNCs8mdOQaA3m-VsGumKTPsPysAxb_lxcAZJHQ7WJYtrECu659eB3LR47nCiR2i65dgp5lv9e7elmv67RdXgWCSb4ZT6GsfDWc-skzBSlgyZOkgRNwNUWZxCjIE0CDqzNGrYOkY_8IAsjT9l2-V-1iS1n-aKldQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تایید شد</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/20931" target="_blank">📅 18:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20930">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJkbEH8qAes2Qwm5MFlICvJUGcyZ5GpizIuyvTnusIMv2R1g8cSdKPxIY9rcAZUlPqNg_2mTcMI-mhjogaZVYMf7OVUK8dGXgc-ZtTfP4mDio-dWdFdbYtBFboI8ZYvVrmJY6KRoaghnBgtyRLQSWt7AR_qRNO09e4hB59rI2k12_tQKZaM5OljXKh_G69OM5hqEG3UUO672pSx-ngDbaclucvkUNe37Y0u2_VHZHO2-3z6FgS8uE8yfzX1_7aWkSuTFOVR-KptpkNvqKZPS8Vw0CeMReCWc-ihpB9oVReCGhl-LQhojknBfw0JplhdGh-UXUikJecUDeJQ5ZWITew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یحیی سریع سخن‌گوی نیروهای مسلح یمن در بیانیه‌ای از انهدام یک‌فروند جنگنده F-15SA متعلق به عربستان سعودی در حین انجام عملیات بر فراز آسمان استان مارب خبر داد.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20930" target="_blank">📅 17:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20929">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1D97koXa54f_YcHIy4iAnGJVUR7DT86-NZ_pPXZLzmWscnmn2nJOvG9K3HCgP_eivk-wItVyZGQIJ1MkjyXpdI1RKQBM3qXQUSbMJoJZAkBNXBJpqDTdbFtzfDs28hlccHePTzIBBrRqFURCCX8Hnrj5DE2BTMLNRMjUue3FODWP8J7X1D0ndrNsiBVIJA-mmCoZzv1iQcPewcrBfXn2pTvPtk66_lF7r-VMRNpUqqeBlCfTO3dv1Wmurm4ZYY7OrKGK6lfYP75M3SDP7M1ghziXeKfNIXsL944mAYC1lQ5Jo4Kbu32MQqJK2oGax16DjrYTAevzuf8oiqJTZdIOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی در سطح بالایی قرار دارد و نظر به رشد طلا از این محدوده (4340) انتظار افت داریم دستکم تا 4300</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20929" target="_blank">📅 11:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20928">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzRK7mLCLGXOTlj-_SlwVjwsm0LT-cTbSyr2Zqv_77EQGkHfEVhQ8-sG2HqlAfGNqQoHDHAjuOGlcRUCacvcRt8r7W2PXsaqikHexMGeiu8yRdsr9aGCiT40yDA8KlEBdpiTJj9N2kcByREVSyQ59njN2oiVhY2PjBQhHgMkWisoPZAuQ_iXYMCU5OWsheHqVPXxaoWa0Zf-67YMhaE5sPJm308X-ZEIvc2g3RvI5lKlZLhein2MjgMnaBSwE9NiDhWtJm-kvNEXuLRMwrG8DzFjpTof0Mq7iR8DDUJOyqLWLImkrt6mxrXb6SlS774wa5-XU0ShKPMQvw7WSriRrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20928" target="_blank">📅 10:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20927">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c861857ae0.mp4?token=Z1m4PCWMF2Ctm8aw6GDxJGb2mOtq_k-l95u_daO2Qrf-2ncjbYIixl9xegvaE5ajdY61_toDqa50fL2Ga3JnAs27xg20r76ySCwWIrEHmvIyq6GpKfXJhtfHomnHvMSS3xLPoRpFrO5mMzL8p-BFe4a_WxBE2y9CmLGfENl5SVI3fLFy9PB7QDYIOOWBYjEI_4PziQtqsJrP3fo8D24XgYF4457WKjTr3gtPEJNGTVmwy45wsgsF65DlUe8iJOCD5fNJ57JspP1bIbNP7RztGtz51xvpqxrNtjTW2T0oPhMhiEUhpGYXg_WJfn7UuJb31dFRJG4foX2672TmFngEXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c861857ae0.mp4?token=Z1m4PCWMF2Ctm8aw6GDxJGb2mOtq_k-l95u_daO2Qrf-2ncjbYIixl9xegvaE5ajdY61_toDqa50fL2Ga3JnAs27xg20r76ySCwWIrEHmvIyq6GpKfXJhtfHomnHvMSS3xLPoRpFrO5mMzL8p-BFe4a_WxBE2y9CmLGfENl5SVI3fLFy9PB7QDYIOOWBYjEI_4PziQtqsJrP3fo8D24XgYF4457WKjTr3gtPEJNGTVmwy45wsgsF65DlUe8iJOCD5fNJ57JspP1bIbNP7RztGtz51xvpqxrNtjTW2T0oPhMhiEUhpGYXg_WJfn7UuJb31dFRJG4foX2672TmFngEXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی ها دیدند هر کار می‌کنند این عثمانی و فاکستان برای دفاع از عربستان در قالب پیمان دفاع مشترک مکه تحریک نمیشوند این بار خود مکه را زدند!</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/20927" target="_blank">📅 09:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20926">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یحیی سریع سخن‌گوی نیروهای مسلح یمن در بیانیه‌ای از انهدام یک‌فروند جنگنده F-15SA متعلق به عربستان سعودی در حین انجام عملیات بر فراز آسمان استان مارب خبر داد.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/20926" target="_blank">📅 09:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20925">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20925" target="_blank">📅 09:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20924">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVxcoF9l1ZMVYGHUXTVtA2cNkgVhPXhqd0WNP-A_DIurMtQ2BQQXH3QkjPDRe9QKEGbRDuiZpnN1s8Cc4t29tiIuVsFpsxCMrHffWf_cOgIEZdV1D0op7VPNhzpbNTOF7tpDa2SGD4l3t1NaMIrKQlEH2GP32H0N4ywEwFUuwwm391VRuUhxxDNTUv1U98etcnANTXdC4F7do5TLS27OHBMyQT60v1X33IIdP9fw4kix5QMfF0GMAOD5tSBpbTk4naFRQD9GQZSLKet5OM3cHIk3lAZVGUcj-GU6XLsR-UaruCbWjQylyPWmId00d6_I0geIR-d0a3rmXqfKqJJPRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشتر گفته بودم در عصر اقتصاد دانش بنیان و هوش مصنوعی، تنگه بندی و راهزنی شاید در کوتاه مدت نتیجه بدهد اما در درازمدت نتیجه عکس خواهدداشت.  (به پست ریپلای شده که حدود ۲ سال پیش منتشر شده نگاه کنید)  اکنون این ویدیو را ببینید و دریابید که چطور بسته شدن باب…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20924" target="_blank">📅 01:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20923">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWU1xEVMpKdUC2_9JYAQO3oyqBDuJjTomdTkqtjpR7JXnhPhq3VueSF_gpGkdTLpwzRCCSYrBUo2QkTExxyntNJnVCceYTlfyDBBrske2iV8nD7i4xJFtH9drKDvxw6EqqBFIdBiRLjhmbAZ0g0VOA6tSQgd_K64l0sXJhWVeTFS2nTEwx7RKFEmdkTdt0ZcQciwgG39maFnPYZ2tDDldeMcUfXJDqyVgt4wbQr7Bf_6lJxdFWFVRa6ZIdfa9Hv1iOlGV9ISWHqFVrJ4BGLJFKXbigXu3rWERoDJka5P7JOOO_HGhZsRSC1LjUfKgWpKBqahxlXf1GmB6whKd7Nc4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.  بهترین محدوده خرید از 4280 تا 4250 می باشد.  نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20923" target="_blank">📅 00:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20922">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaP-GwkzJaktWd7NukO7iEsx2jR5daP74ukQWpLLoSw5GpphF4kpJuxeV-abLJm5FXHErhLCF-G1AVtEpvKbqv2hOaSzUOsylj9QbHiq9FMtVVK6QS1SU991GrASRVk7KLhW_fOA-d5dYSgC_1HYMuACJQ3wp1793btfJ_KRKmejISUQVGQ4kWLGMppTHMIROnivVbuu41WCYMr3j0oyZbc-fEJGuC4x_PDiNJAIGja4IiEftTC6pK4kpRpEX5ENJI36A_yY_rCz-6G6iD0PF8uA4qXQInlUECtBbYG-eqE9m_aBkWNn2ZBcWwZsHYCS2zCrO8tQeBSRdhJ9k_ofAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 27</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20922" target="_blank">📅 00:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20921">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZl3P0ZFNOw4o20-J6stINfWwvZHXPmQQ5Y6ieVjlmBDQItO6cf3huGqYN80fSAQNpGWll6BU7p5BYLgatbkZKlY20G6-tF_5pXmhAJEvxVo7R9SzgAlgLfZCXTuEuJYd6kyeKz1acUFVmrRa0T5UreZcOiAnPpcngtqw0gg0FZ1FOkTBlG-GXwDlqeuTf4mfQ4biVivNIPNK3G7z8IJ83P5qm_iFyar-znDRAhTxVvzMiCLJ-9G8LAQsAX9fQ5M4zoi6Ic3jlwzQ82RR7szIan7shTuyR8QmdOsWeLb0MKt7yO3aebvJ5q9N_PasEGsSCx6vgsgwfLuyH6aiSHqiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا امروز برای ادارات و نهادهای دولتی ابتدا کد 100 (تخلیه فوری) صادر شده و باعث ایجاد اخلال در کار ادارات شده و بعد از چند دقیقه وضعیت سفید اعلام شده و با اعلام کد 69 همه به سر کار همیشگی خود برگشته اند.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20921" target="_blank">📅 00:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20920">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">به گفته مقامات آمریکایی، دولت ترامپ در حال تدارک فروش بمب‌های ۲۰۰۰ پوندی به ارزش میلیاردها دلار به اسرائیل است؛ اقدامی که بزرگ‌ترین فروش یکجای این نوع مهمات بحث‌برانگیز در سال‌های اخیر محسوب می‌شود.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20920" target="_blank">📅 22:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20919">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">به گفته مقامات آمریکایی، دولت ترامپ در حال تدارک فروش بمب‌های ۲۰۰۰ پوندی به ارزش میلیاردها دلار به اسرائیل است؛ اقدامی که بزرگ‌ترین فروش یکجای این نوع مهمات بحث‌برانگیز در سال‌های اخیر محسوب می‌شود.</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/20919" target="_blank">📅 21:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20918">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">عراقچی فردا به چین سفر می‌کند</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20918" target="_blank">📅 19:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20917">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آکسیوس:
یک پهپاد آمریکایی پس از تلاش سپاه پاسداران برای توقیف یک پهپاد نیروی دریایی آمریکا، دو قایق کوچک ایرانی را در تنگه هرمز منهدم کرد و اکثر سرنشینان آن را کشت</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20917" target="_blank">📅 18:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20916">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بارگیری نفت در ینبع، مهم‌ترین بندر عربستان سعودی در دریای سرخ، به دلیل حمله قبلی به خط لوله شرقی-غربی، متوقف شده است. (به نقل از خبرگزاری رویترز)</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20916" target="_blank">📅 18:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20915">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بارگیری نفت در ینبع، مهم‌ترین بندر عربستان سعودی در دریای سرخ، به دلیل حمله قبلی به خط لوله شرقی-غربی، متوقف شده است. (به نقل از خبرگزاری رویترز)</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/20915" target="_blank">📅 18:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20914">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.  بهترین محدوده خرید از 4280 تا 4250 می باشد.  نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20914" target="_blank">📅 16:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20913">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وزارت خارجه چین: «ما با هرگونه رقابت تسلیحاتی در فضا و همچنین هرگونه تلاش برای تسلیحاتی‌کردن فضا یا تبدیل آن به منطقه جنگی مخالفیم.   از آمریکا می‌خواهیم گسترش حضور و توان نظامی خود در فضا را متوقف کند و با اقدامات عملی، از ثبات راهبردی جهانی محافظت کند.»</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/20913" target="_blank">📅 16:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20912">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FV1mZStgw3IuKn8fBHlVGiZ5CucIxO98NBX64VUVp4XG-8MZ-qFCD37Y4wa6jW175LD0kkzp3OQlOoDWc9R2sYjulPMS5uZu0KG1a3EwEjEY8CMQD6Tn05W3huSw-XXuUZQFx-B5CWg_ywP9yisqx9LtU2CVpAAzjUKq29muUWQYzPyKUAmO8_5xc8y-3Xs08t_809yolBEu-qEeLhX9CQSPzGqiZPq64JaHSGMAEvTCPvgFhbJ5rYtUT7Bomb7BM4u24gVBtTZGNcZa1c8i5aTDZMVAnFpRbUdMp8K5Ls92On_Lg1Z98YZwofnUdEib-BYSuLRB0APZW5QUeWsmtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سخنگوی پویش جانفدا :  جان فدایان غیور صرفا برای اهداف نظامی به کارگیری نخواهند شد ، به زودی پیام های جدیدی را به این عزیزان تقدیم خواهیم کرد</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20912" target="_blank">📅 16:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20911">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وزارت خارجه چین: «ما با هرگونه رقابت تسلیحاتی در فضا و همچنین هرگونه تلاش برای تسلیحاتی‌کردن فضا یا تبدیل آن به منطقه جنگی مخالفیم.   از آمریکا می‌خواهیم گسترش حضور و توان نظامی خود در فضا را متوقف کند و با اقدامات عملی، از ثبات راهبردی جهانی محافظت کند.»</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20911" target="_blank">📅 16:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20910">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20910" target="_blank">📅 16:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20909">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">به نظرم بین اسراییل و ترکیه و پاکستان یک تورنمنت سه جانبه بگذارند ببینند کی می‌تواند برنده شده و بیشتر گاو شیرده حجاز و نجد را بدوشد!</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20909" target="_blank">📅 16:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20908">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رسانه عبری والا به نقل از منابع:   تماس‌هایی میان عربستان و اسرائیل با میانجی‌گری فرمانده سنتکام انجام شده تا از طریق ارائه اطلاعات، به سعودی‌ها در دفاع از خود در برابر انصارالله کمک کنند</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20908" target="_blank">📅 16:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20907">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20907" target="_blank">📅 16:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20906">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">در سوریه با گران شدن سوخت، اعتراضات مردمی آغاز شده و آشوب ایجاد شده</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20906" target="_blank">📅 15:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20905">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 27</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20905" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 27
سه شنبه 15 سپتامبر  2026</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20905" target="_blank">📅 13:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20904">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گویا امروز برای ادارات و نهادهای دولتی ابتدا کد 100 (تخلیه فوری) صادر شده و باعث ایجاد اخلال در کار ادارات شده و بعد از چند دقیقه وضعیت سفید اعلام شده و با اعلام کد 69 همه به سر کار همیشگی خود برگشته اند.</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/20904" target="_blank">📅 12:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20903">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20903" target="_blank">📅 12:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20902">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGQ-8uD_KpEVnE_gnF6jl0zi6mYshxzsAKJ6ABrMCrezwgGKyeeLO0uRFSHhqB3QUAP3HT80rp7j3Xy88JplWonUzTtEY6Po5ifLQPGTdCKQf60nvMIZHU7v9pmSe0Cbb6Bl1o01EfQA2q7a2T6XzpNxBkHCSu26pvaARle8UU4rRgS8fv6_zFx0LBWsek9X7_G-awzRvoMQpbOy01rDnjOW0iMoAyJZnrHSBZRBNYbsxr5k_6TxOIbvQiNoHf1gIoAYuPxFGynvuSW558Cm8m9pmdjOKglIIl_Zmz2gz-aU2RBPS3cUlAiXvaq-uMxaa_MDMudRstcwj7325ABRAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/20902" target="_blank">📅 12:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20901">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OB0PNaanurawVQy5BiQaAwymD1-jxfn3dbDHcb7Px1ESW27oF6OhJC7EOVTy6D1DsAy5lf5n_5BESXFNaPkjNP7bTBvFyHbOj79jR7ZQNosFjHildRdUBPjrRQ8nT85EoalLQE4BEeCxgh4rZmSYhHT21Dj6DAcSJv6jT8cl62_bvU2ErxHLaRUeERz8chs_65_iDY8rF7Mgzte5GQdoqjpBptn3HO34gB7j5s8fAECAZtV-E3OzlwHEdR8DMAucqzfw5iHt66hxAOElx83jJ2LwdZDBDCC2v8h0AxsW1p0m-tF9sdt7X9tFw0qLdgNzHPIEpkx-VPzEH929seOfgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال: کمک ماهواره‌ای چین به ایران  به گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی می‌گویند ایران پیش و پس از حمله موشکی ۱۷ ژوئیه به پایگاه «موافق‌السلطی» در اردن، از تصاویر ماهواره‌ای با وضوح بالا از منابع چینی استفاده کرده است.  در این حمله…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/20901" target="_blank">📅 11:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20900">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGTAwfChHoELNnb4mzaIv-t-R6k4qWeX6biXhnybLYCwBRfJyOlRcUbFvs5zRIUYlQkT6PRg1BgbQU5vqqxruddXdcnUjyI93XrzUEKvKSGCiMQGxn0VxZX4F1uuCI2sqAw_37PMVJs0bjIHDSAjqY36gEVq3RVd_TPZQXlwSuOUKVL3YhKqnd4pFf8WOdra9chdi2wbmZQew73xXt070Rh_0EHm7EwLViiYvRN32bP3fQaaqdBTs1LslL1CgZrOwoDZFcGK7wc2tAGOwx9m-geoCDfyLIzJMN-jYPWXL-0buNTi9-ngzwQX088s_ctfnl2djnET-Bbehgn7TGmxbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20900" target="_blank">📅 11:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20899">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nE-pQDL0r_SIL15egH4NQFWVPSF56M17f9SuSo9fnKHwrK7zwwNIThd3rSUlyc_2dVMtuCub2UAMrohe83F23Z48lhtRJ4CVGc_a1LfsDAmAOaHwTpaQqdsxZpmec98hzEjiIr3dmqIcw5N1j6BAhj6q3-_YQOmEriyioZjSxsQ3J04QYMmMk3hVToi6Nlxn8ZkOOLtZ3Xhp2C8jH8P0sai7jcMxrcnDRX9TLqIiUg9dr7fhJm5IdtJWt6H0rm7FrLdYkztfWPoFvI84zZNGWKGAeCNYNSZJSWy7IY6HIHg0XW_8USxAHRYP0MfnH5zkpQtT_6howg4oV6ePeKBopw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.
بهترین محدوده خرید از 4280 تا 4250 می باشد.
نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم و پیش بینی میکنم این هفته طلا سطح 4400 دلار را پس بگیرد.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20899" target="_blank">📅 11:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20898">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fg7n-N-QI98lNAuQH_sj7BtwBKTTiyff3h3HxsGVy9YCoS1DtX9u0hGZAW0yM-lQWcIntgtu0YP3GlPfkCtxzAlxvsiBP9ud7pM87iy0W0NPGGmJLQaxLLBFxXzWt2OW-kUtXXyAl9QwQ_f0v0JCEAEMRZtQTEOTYiRmHszUIPyuwvyHGon90kogvDpNrRjMcE2KZ-NxYpCT8PUv0ktQH20JUoBHtewOsF8wGprfhenGPY9nIYAkIsOJRDsUoPVoiWwQY7o6sdKmKQuqGyBHQZByj07IMu9W-wuORqhONo-XG1GsCUyB_GQYlKeNzZaulLtmYz-tKc-Zqry08yHCoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح نسبتاً بالایی است و احتمال فراوان هر بالایی فراتر از 4300 فروخته خواهدشد.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20898" target="_blank">📅 11:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20897">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-t4HN9BeQQ1jXJRk2o1tE9r9gVyACc45biMryXi-d6zmKGO3za5pdAiWX0fhOtWjdL8jEaGnD68ttFBrtiF1GwerxDPxbiuB0PxfLtDbZynATDYdgQoDDYN27HQuxz95WfAdvqYWbf659LHopj8EeaLyvtoIUzOftxA-8-ZQqJUu8Kgd5XfjVf83KUIaM1XrOoNugc3SmeQNeas3vtmtl8B636p-NE2ddefC-cD6nvPMBYv17_JXE-_ncgzEDwWwO56z3EaAeHsXVhErDQ_5IjeYriljjFmak3vAAIoiuXdkg2gyQFAjeTvcwuvVCzrFknmUCc0byKzOJ8kbeVANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله حوثی ها به عمق خاک عربستان در ۱۱۸۰ کیلومتری مرزهای یمن!
و کماکان از متحدین پیمان مکه (عثمانی و فاکستان) خبری نیست!</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20897" target="_blank">📅 09:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20896">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جمعی از نمایندگان مجلس در بیانیه‌ای خواستار تجدید نظر عضویت ایران در NPT شدند</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20896" target="_blank">📅 09:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20895">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">درخواست کمک عربستان از انگلیس برای حمله به یمن
بعد از مخالفت آمریکا با حملۀ به یمن،‌ عربستان سعودی این‌بار از انگلیس خواست که در این کشور مداخله نظامی انجام دهد.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20895" target="_blank">📅 09:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20894">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یک بار از یکی پرسیدند تا حالا اتوبوس هل داده ای؟
گفت نه ولی یک بار تو اتوبوس هل شدیم دادیم!</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SBoxxx/20894" target="_blank">📅 01:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20892">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آن‌قدر به ما گفتند ترامپ تاجر است که قبل از جنگ به آمریکا پیشنهاد همکاری ۵۰۰ میلیارد دلاری دادیم!
- حسن قشقاوی، سخنگوی کمیسیون امنیت ملی مجلس</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20892" target="_blank">📅 01:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20891">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MskZNHA7x2px5RFlF1LnN0mrIAuvIcCgwMBW2iyAXZnq8zoq_7ugBW-z0s2Dzyi7-qc_O65xdtaV6SjXMAB_nGlpwU44oKzMvGdwoXPm3URvPAYD4712farBVPxHOrgUV8fnDS2bTgPCa8vPPCTksmUWdHx_x4NCQwz-m9Ox9I05WgOsExA40IID1ZmXl4r1emMkR4t5k5ODejvV96LsvgcMirJbkUx3Aq3f1eJi56VNqvtFPMysi_sq8sx2fbT54NI1mGB-kWUqLCo52mSNks71yrBmNNesZjFLgR1vLi0SPrWicocIw7GXLwXjNfPxK9l7lHjSKVSX9vGit8iVOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
💙
😀
💙
😀</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20891" target="_blank">📅 00:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20890">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">برنامه ریزی آمریکا و عربستان برای حمله به مواضع تازه تصرف شده ارتش یمن در ساحل غربی
یک منبع یمنی وابسته به مزدوران سعودی اعلام کرد آمریکایی‌ها به عربستان سعودی در مورد مناطقی که مزدوران عربستان آن‌ها را از دست دادند و مشرف به باب‌المندب هستند، فشار می‌آورد تا این مناطق را پس بگیرند
در پی این فشارها عربستان سعودی با کمک نظامیان آمریکایی در حال طرح ریزی حمله ای به مناطق تازه آزاد شده ساحل غربی با نیروهای سلفی و سایر مزدوران است
این منبع اشاره کرد طبق دستور آمریکایی ها به بن سلمان این حمله بزودی آغاز می‌شود.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20890" target="_blank">📅 23:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20889">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پزشکیان:
برخی کشورها در خفا به ما می‌گویند ما با شما هستیم اما در عمل از آمریکا حساب می‌برند و جرئت همراهی با ما را ندارند</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20889" target="_blank">📅 22:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20888">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پزشکیان:
آمریکا چون نمی‌تواند رهبر ما را پیدا کند درباره سلامتی ایشان شایعه می‌سازد</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20888" target="_blank">📅 22:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20887">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران ایران اعلام کرد که نفتکش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در بخش جنوبی تنگه هرمز، با یک مین دریایی برخورد کرده است.  سپاه پاسداران می‌گوید تلاش‌ها برای مهار آتش‌سوزی ناشی از این حادثه بی‌نتیجه…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/20887" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20886">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران ایران اعلام کرد که نفتکش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در بخش جنوبی تنگه هرمز، با یک مین دریایی برخورد کرده است.
سپاه پاسداران می‌گوید تلاش‌ها برای مهار آتش‌سوزی ناشی از این حادثه بی‌نتیجه مانده و این نفتکش اکنون کاملاً در آتش می‌سوزد.
آن‌ها تأکید کردند که تنگه هرمز همچنان بسته و «تحت کنترل هوشمند» آن‌ها قرار دارد.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20886" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20885">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گاردین: طبق گزارش ها نخست وزیر بریتانیا در حال بررسی اعزام ناو های جنگی برای حمله به حوثی ها در کمک به عربستان سعودی می‌باشد</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20885" target="_blank">📅 22:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20884">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">روسیه و اوکراین دارند با پیشنهاد ترامپ برای تعهد به نزدن تاسیسات انرژی یکدیگر موافقت می‌کنند</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20884" target="_blank">📅 19:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20883">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20883" target="_blank">📅 19:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20882">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ادعای ترامپ:   ایران به شدت می‌خواهد در سریع‌ترین زمان ممکن توافق کند.  من تعیین خواهیم کرد که آیا وارد مذاکره خواهیم شد یا خیر، و این گزینه‌ای است که نسبت به آن پذیرا هستیم.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20882" target="_blank">📅 19:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20881">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ادعای ترامپ:
ایران به شدت می‌خواهد در سریع‌ترین زمان ممکن توافق کند.
من تعیین خواهیم کرد که آیا وارد مذاکره خواهیم شد یا خیر، و این گزینه‌ای است که نسبت به آن پذیرا هستیم.</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/20881" target="_blank">📅 19:08 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
