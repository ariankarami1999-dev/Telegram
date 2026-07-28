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
<img src="https://cdn4.telesco.pe/file/li5gdq7LJk4jqDFPBT3Xwog_LsHcchQDUGaupdzRu8keTQpOiNn6bKqeQmU7T6VdJ65Eb5_0Lal_ui3bvOEl49Si1Z0uZF4zb83bp97uanxfdi0y3LEqtny7Fztkqhag17BXBjaPjYlMT7iw6h9i2bufAqo3YQQAx2MqimkbCYrFPDlTjIxh-X_vBmi8pSScrC9iGVCcgSg1EB2D5d7CCdeSTcgRZWoFoTjzSbLMC3pLhqCiFYLhJY-2TgWg-ZsAVhXiz1Wgf0zk-nENA4AXuR_ZbBI-iDAn7vy8uKyzMil9ccufvRCL727NkR28u8DdGHovNLQh0usWDyeP5Vtapg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.2M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 16:18:26</div>
<hr>

<div class="tg-post" id="msg-676053">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ff15358f5.mp4?token=YcHc2hhxtgOr32BL9ALKwAj7Ch74jwo-3W-535G-FdUG-cMjumAbj2nV3ODT-th96RXmfWI5criPaF6bbbp07EVA8wp4Pl5zL1XMMPe0EWGcAbAI2DuT-YFJeLxTcaIjMoOvVO0f93UAZDFKxxfOdoPQy8iPzA94kj5G7rn1JIbGxiJ_fGzQzpYFryrVi0EMXC8lvD8J9gHkVIkKWbaQ7LnDo31Z7A_CQxFoCGzVAWDeifElgd13lS6Xmo-FGS9rMg7xSggLPa4U8pMKqM71I3GM92aMsiUUvxLDqxTCfYzrBqOczsm25P6kAzanAA5t18XcSOc7Cj0FxWj1hq4y5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ff15358f5.mp4?token=YcHc2hhxtgOr32BL9ALKwAj7Ch74jwo-3W-535G-FdUG-cMjumAbj2nV3ODT-th96RXmfWI5criPaF6bbbp07EVA8wp4Pl5zL1XMMPe0EWGcAbAI2DuT-YFJeLxTcaIjMoOvVO0f93UAZDFKxxfOdoPQy8iPzA94kj5G7rn1JIbGxiJ_fGzQzpYFryrVi0EMXC8lvD8J9gHkVIkKWbaQ7LnDo31Z7A_CQxFoCGzVAWDeifElgd13lS6Xmo-FGS9rMg7xSggLPa4U8pMKqM71I3GM92aMsiUUvxLDqxTCfYzrBqOczsm25P6kAzanAA5t18XcSOc7Cj0FxWj1hq4y5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور بعضی از وام‌ها به صورت نامحسوس بیشتر از سود، ضرر دارن؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/akhbarefori/676053" target="_blank">📅 16:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676052">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
حکم اعدام ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی دو تن از عوامل جنایت فجیع میدان شهید علیخانی اصفهان در کودتای دی‌ماه سال گذشته اجرا شد/ میزان  #اخبار_اصفهان در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/676052" target="_blank">📅 16:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676051">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
یمن به عربستان هشدار داد
🔹
صنعا با محکوم کردن تهدیدهای ریاض علیه عراق، اعلام کرد در برابر نقض حریم هوایی خود پاسخ می‌دهد و این اقدامات بی‌پاسخ نخواهد ماند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/676051" target="_blank">📅 15:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676050">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
نتانیاهو نخست وزیر رژيم صهیونیستی وارد واشنگتن شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/676050" target="_blank">📅 15:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676049">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
برگ‌ برنده‌ تنگه‌ هرمز را از دست نداده‌ایم
جعفر قناد‌باشی، کارشناس مسائل بین‌الملل:
🔹
همچنان همان شرایط سابق، بر تنگه‌ی هرمز حکم فرما است.
🔹
بخش عمیق تنگه‌ هرمز که کشتی‌های بزرگ می‌توانند عبور کنند، در اختیار ایران است.
🔹
در بخشی که عمان در اختیار دارد، کشتی‌های بزرگ قادر به عبور نیستند.
🔹
هنوز تنها مسیری که ما مشخص می‌کنیم، امن است./ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/676049" target="_blank">📅 15:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676048">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
زلزله ۷.۱ ریشتری ژاپن را لرزاند
🔹
زلزله‌ای قدرتمند بخش‌هایی از ژاپن را لرزاند و به‌گفته مقام‌های این کشور، در برخی مناطق قطعی برق، آتش‌سوزی و خسارت به راه‌ها و ساختمان‌ها گزارش شده و بیش از ۱۵۰ هزار نفر هم دستور تخلیه گرفته‌اند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/676048" target="_blank">📅 15:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676047">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGdQ0-3wmZNYwiT1K25_NStEW9YErIxXw2dj9boA7-TrFYG-um48gOb8lIaxtzN8ciPXoTXlE5310SeAxF-Y8YWm2da9Xvv3uuzmT_0iwkPZ8Gc3y9NT6TqNlY00RijpNTur3yANaNVFzxsgWOm--g2-emfsQQgKHd4tLK8Tj2TzFsnG80iv7oJqtP_FSDhHzZeISmPv4PZUemTGtTpsZ3vavOvo50fSg9S6CGRB1r5Ruov6U1sARZLP245u1x8gOxFhoYDTb00z_6lbRx2EPj3yDLIgn-B7UDQHtICjnD9rUa5L8Q7cjeSQ2QjnPE2GwShuQojPmo59wq9W0d2WyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام بسته ارتباطی اربعین برای شما مناسب‌تر است؟
🔹
با نزدیک شدن به اربعین، انتخاب بسته ارتباطی مناسب به یکی از دغدغه‌های زائران تبدیل شده، به‌ویژه برای کسانی که می‌خواهند در طول سفر بدون نگرانی از هزینه‌ها به اینترنت دسترسی داشته باشند یا با خانواده و همراهان خود تماس بگیرند.
🔹
مقایسه بسته‌های همراه اول و زین عراق نشان می‌دهد برای اغلب زائران ایرانی که به اینترنت، پیام‌رسان‌ها و خدمات آنلاین نیاز دارند، بسته‌های همراه اول انتخاب کاربردی‌تر و به‌صرفه‌تری است، درحالی‌که بسته‌های زین بیشتر برای تماس‌های محلی داخل عراق مناسب‌اند.
🔹
همراه اول بسته‌هایی با ترکیبی از اینترنت، مکالمه و پیامک ارائه کرده است. در میان این گزینه‌ها، بسته ۵ گیگابایت اینترنت با اعتبار ۱۴ روزه و قیمت ۸۰۰ هزار تومان، برای زائرانی که در طول سفر به اینترنت بیشتری نیاز دارند، انتخاب قابل‌توجهی است.
🔹
در مقابل، بسته‌های زین عراق تمرکز بیشتری بر مکالمه دارند. برای نمونه، بسته‌ای شامل ۱۰ دقیقه تماس بین‌الملل و ۳۰ دقیقه تماس درون‌شبکه‌ای زین، با قیمتی حدود ۶۶۵ هزار تومان عرضه شده است.
🔹
زائرانی که بیشتر از پیام‌رسان‌ها، مسیریاب‌ها و خدمات آنلاین استفاده می‌کنند، باید حجم اینترنت را در اولویت قرار دهند./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/676047" target="_blank">📅 15:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676046">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ادارات کدام استان‌ها فردا چهارشنبه تعطیل یا با کاهش ساعات کاری فعالیت می‌کند
🔹
کرمانشاه: تعطیل
🔹
مرکزی: کاهش ساعات اداری
🔹
کردستان: تعطیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/676046" target="_blank">📅 15:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676045">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5MBKmncn3qz49qxnEvt8QXzTCtXuoNbTJk-sNFX7yfNfcp6cNiHC7Y47Jm-qWqmw0ACUT-EbpOJyvnGgjvH4QJY4vNOIoz4J-k7zRcY_3M27vdrW3a2o_lThjkFmXqLc0W1MldtTq-oLcq4ysHpjadiWxxTWjVHJ1Fade0HhMjqbKSiWjZy0nAJ-4IAc5iiRaoHVBZvZSZ9WczF648AKrd4SSudPk6e9QkaYolrjen-4uG2idYajRpbb1DHHZX0XOf7rpdSMbdXhCPRZa7U2Z2ZUO8vJn0xF7oJKFNsoy55W9atpbHD0mMrPXlp4MyvUS0ZqqiRGBJBy4p4DuzP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت ۸۷ دلار شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/676045" target="_blank">📅 15:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676044">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBhAa3RRWBS0clYgAoTNo5TzVPxA_FE2skP-udNeJTk-a3J3wuQ0WGgjDe6zwrCAUZKOMwdeIj75t8tbeHvNNucBmx8qbQQi_qB_asq4GlWtCv9o4IDAMUNk7XiG8_BXPjZQZmFR_j7FTUg6IbJmqH3qGl3VkJxAE7-E7j81TDIeutUr3TfXSPgDs8B1TZyShxCuJrxl59zwFJrjRPsNWtYZcNHsiPsm9C3YPshG3GUdf9sgNcS_7xRScTZzvd1Ok1t7tTCORdzp8nR3lAuYdTI9IeqQtacHjZx-46dnaanJLzNmRPxHnXq4bXipBp52UOIwFg8GqwFAgfmTp7VRvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕌
برج ساعت حرم امام رضا (ع)
حرم همیشه نزدیک‌تر از آن چیزی‌ست که فکر می‌کنی...
یادگاری ماندگار از بارگاه امام مهربانی برای خانه یا هدیه‌ای ارزشمند.
💰
۵,۷۵۳,۰۰۰ تومان
🛍
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/676044" target="_blank">📅 15:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676042">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
امارات به دنبال احیای کانال‌های دیپلماتیک و اقتصادی با ایران
فایننشال تایمز:
🔹
امارات در حال بازگشایی روابط دیپلماتیک و تجاری با ایران است و همزمان همکاری‌های نظامی خود را با آمریکا و اسرائیل تقویت می‌کند؛ راهبردی که نشان‌دهنده تلاش ابوظبی برای کاهش تنش با تهران بدون تضعیف شراکت‌های امنیتی خود است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/676042" target="_blank">📅 15:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676041">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
تبادل پیام ایران و آمریکا ادامه دارد، اما بی‌نتیجه مانده است
🔹
به‌گفته یک منبع آگاه ایرانی که العربی الجدید به آن استناد کرده، طی دو هفته گذشته از طریق میانجی‌ها پیام‌هایی میان تهران و واشنگتن رد و بدل شده، اما این رفت‌وآمدها هنوز به پیشرفت یا گشایش قابل‌توجهی نرسیده است./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/676041" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676040">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/285d386062.mp4?token=NcXh8ko1FHchy4Z5WwGlt0lEd0rJqrYrxhuCNnD0i47KyItqUZuFdog8RXGYUMH7T130Jk0C5Wn8dUdAb1IlrRJ3-ZSX1FGyB_29wAUSDriFzEfFQSS4MQwOSr2KBd0LP6XKMs7AbW4yF478dh_Z49qYvnJi1TijDITvUEO0qcvkIizP5bzpAiZ7Zo1kzm8V04R87AwMVeb4sQPlzq_Ebao2ndWjzz-KJtz3yeaiHjSiRux2M34wR5eYG2k5C4zlAB-74HK6wdtfDQrv-vMYp9bX22Mk8rAppwxTxcW45_LLbEvSXY6B47KPh1b_umnLL2-iuFYXkl2fQihqH_DTkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/285d386062.mp4?token=NcXh8ko1FHchy4Z5WwGlt0lEd0rJqrYrxhuCNnD0i47KyItqUZuFdog8RXGYUMH7T130Jk0C5Wn8dUdAb1IlrRJ3-ZSX1FGyB_29wAUSDriFzEfFQSS4MQwOSr2KBd0LP6XKMs7AbW4yF478dh_Z49qYvnJi1TijDITvUEO0qcvkIizP5bzpAiZ7Zo1kzm8V04R87AwMVeb4sQPlzq_Ebao2ndWjzz-KJtz3yeaiHjSiRux2M34wR5eYG2k5C4zlAB-74HK6wdtfDQrv-vMYp9bX22Mk8rAppwxTxcW45_LLbEvSXY6B47KPh1b_umnLL2-iuFYXkl2fQihqH_DTkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه وقوع زمین‌لرزه ۷.۱ ریشتری ژاپن
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/676040" target="_blank">📅 15:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676039">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UU80t5E2QyxWxH8ItDMtnJKdVA0o5YREcDQXD_elkon3nRoL6xXfWZG243YWwRaU1cc2YY5jfltAY9JTKbwH-BJngHRY9IBOhkz5AEHDWcygVEATXQa2W06zj9gqi01VSuP5YtusGiHRo-cqqdBgwJs3OleeWJcAHkQy6IHGvIjIyyGE-mBI_BLX63CsV_EPj2CF2lO18_eopjxVbC5ktQTCiFn9g-5f6HqdYwK4Q_3JGgODFd0NxpA5aiL8n7SAtz5U2TJY2K7pgeFVDMn3CXFGse5GOtdB3IlWI9YAXmqUU_-G-uCTQ9yCmYUZi8XWk6xqayM2HwlRavUvN9ig-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آپدیت جدید و جذاب اینستاگرام؛ اضافه شدن یادبود
🔹
در آپدیت جدید می‌توانی یک نفر رو به‌عنوان «یادبود» انتخاب کنی تا بعد از فوت بعضی کارهای پیج رو انجام بده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/676039" target="_blank">📅 14:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676034">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/arLda7LH83pCa3KvCeSdfIeWWD-ur9K2JhlHtMP_ecLcPsihT2HywlcJv5rZ6BgX4ht2wlCDLSvDcb6qp2R98_CfBo3W8ynLWXRd_7RM2Wrbdv5D98RxPrCMdaMGAPXghYo0a8tQpJ4ptkJ4i2SuWZCK7IkLaWPxYeWjjJeVxdAHfZG8M473f6kdetbj4gaz-p5hdoi-Zgxiq7G-qb_42g8wE5bJj64ZoZ3uXBC6-9nwqqTXABeqyf2ePbld052sHzWHUjAiS0-_vd5pnv3ZLvwEGRtqGBpVbCw9IvF-w8c3XQAYdXiSGDWsYbB_LRMpFZF1Qo5ti8XzoQLbjiD_aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UN4zukuzh9pOy5unC36_1jP_dTWCOQgQ9Z1iP-GG6t7UB0w5ZrW_X_2lysv4DIRE8HLdYcSYCIFTUHOeNKB_UxE2ONoUa1nnvLdos97A9vNhmFdxNNz2OmPsW4KBzyPsjwRVPhcFH5wvgK-HyTS_eiXUi8cLEi8ftkU1vW9JspY1HH2t7tUOddaXKKOo3po_Kpa9-3VqJGOmaB9oBJ_gylDtgCM7LSktKBM1BkH_mHtb0vWAk68dc8pvB0GkQ-yB-QwPNvrWHArQ3Jpp-nsjyHP_LOZsQfJQbkf8zqohfIvlypQ7dEA-1L-yFwY55GxPjU5jAMaf25HHCOYDlsyv3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bjsbvF9lWWOmcaiUmnMq_PfjUtJC3K8JkuH_LURpKvn4N4y9jpZvBE3CPmBK0QeT2xdbme-vXQpsdgsUsMCiItWnmnsSqx4awm_5hWKyprhem8EEK4n3DLyaV9XN5o4hEVsYgza4OXnCY8-85mNW5HyGYNT_hjadGyMToxvBUNvBFpPYR_TSTlinMLSopLWbD3Vp058APJE9Lz7BvNk7rJmwNXk1ZtTH3Ji-Iv-xY5y54iXOP_AQwKXaOyzNJ1f3-6e2pM_blxwqHt5mbhFMowr_9SuN_dNtZITjDdPGU-bFWFhyu215_O0UoNqyzOIEr5is7Yp4TfLXO_Bcxrfx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lz8H-ePBoBZ4JdpWCmxUF1phEEtHqLXgRcdyHtaknFLLKQUNUKF4sUr-b8CHUIvNbPZk1eebpUHdvoi9VG_sjViuepj92kmXcXlC1OcwfyqYdVvcF4fq13O_1Ucl1SVt43aWBYIK7QsGij-174PITUqXsUcV8tMpL-S9Q0M4Ra5m-MdVP7o7Skp1L_l1Y_MX6pVD2Z831hIZG3AQqh_hZC8jrcfMXAIBV1y8Zd5cnw-7ddIUEIjZBELrnTSRls8BBw_xiD0CmTF4BSye-nPWG5_8LT3ozXoiY3wvQSk5sc_QXhd0t_ZXHw-yB1I-VwPUqHIa9w7A46-9nVhRYtrarA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y84Oa6s4kCH5z2CYbkz1H420kxQ3wbPEEUpINUJsehBklTuTXswr1wZuuJgcVKCKJpSeXOGi8VFmwrOAYzuZviHE1jAJHURSAjv6o19DC1zjHr8CHI7_SllMh-HBEqbX5tn6mTPXWog4Met-AxlYzl0mCElITl0y8twJ0f05QzlkEKoykylOD33vKxwXVIDVravAV7Vxdpyu02OZNoDeGo4Cz6jYJ60H991vA3DKw4R8zYumURJlO7oJb9qRVoEer0Q3YBOAvXWVrgoP8YQX1VYPz6T58mcLbVALqJlqiAlmGvLXS0sI9mcm5oEaefNpG45Rtfddhu01Ci6lsFgkrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هشتگ
#یالثارات_الحسین
در شبکه‌های اجتماعی ترند شد
🔹
در آستانه اربعین حسینی، کاربران شبکه‌های اجتماعی با داغ‌کردن هشتگ
#یالثارات_الحسین
در شبکه ایکس (توییتر)، فریاد خون‌خواهی سر دادند.
🔹
این هشتگ طی روز جاری به یکی از داغ‌ترین موضوعات شبکه در میان کاربران ایرانی تبدیل شد و کاربران در محورهایی مانند تبیین ماهیت اربعین حسینی، خون‌خواهی رهبر شهید، بیعت با رهبر معظم انقلاب اسلامی، تأکید بر وحدت جهان اسلام و... به تولید و انتشار محتوا پرداختند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/676034" target="_blank">📅 14:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676033">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
آرامکو پس از حملات یمن، پالایشگاه جازان را تعطیل کرد
🔹
شرکت آرامکوی عربستان سعودی، پالایشگاه جازان با ظرفیت ۴۰۰ هزار بشکه در روز را در پی حملات اخیر نیروهای مسلح یمن تعطیل کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/676033" target="_blank">📅 14:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676032">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4cdd20aa.mp4?token=joyUGCfn_eTrdqaz3hgAgvUuKFWirsPQpnhbMla-MQkLx1cCmb57UPa3eAJQaHniGQj5VQiCp5ACVwRGqBtpewVJOsGmRsK9ViV8qSpo900mIzrrP384MBCgZLfLexNdBNd-DHRrbmvYoVVgI5KeWOoTLqDAKnfuS17DjWejESqqOY0mw-Q49-tlEJL2G-t-34SBOLCOCnG2B88W9-vfdn9YRR4NxJtXTBeHEDS5ophd6X1o0j3Ea7hNE_2hzvlR7zDQ-WHCr04H0OMYrQbZDqn_oFp9MY49l7ixFMEXGE-1khNJ6CNHEn4-pwY4Uj9JrSIQRZPqPwT-cDK29LDzRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4cdd20aa.mp4?token=joyUGCfn_eTrdqaz3hgAgvUuKFWirsPQpnhbMla-MQkLx1cCmb57UPa3eAJQaHniGQj5VQiCp5ACVwRGqBtpewVJOsGmRsK9ViV8qSpo900mIzrrP384MBCgZLfLexNdBNd-DHRrbmvYoVVgI5KeWOoTLqDAKnfuS17DjWejESqqOY0mw-Q49-tlEJL2G-t-34SBOLCOCnG2B88W9-vfdn9YRR4NxJtXTBeHEDS5ophd6X1o0j3Ea7hNE_2hzvlR7zDQ-WHCr04H0OMYrQbZDqn_oFp9MY49l7ixFMEXGE-1khNJ6CNHEn4-pwY4Uj9JrSIQRZPqPwT-cDK29LDzRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تبیین آیت‌الله جوادی آملی درباره شهادت رهبر شهید انقلاب در راه صیانت از اسلام و قرآن و اهل‌بیت(ع) و وظیفه امروز ما در قبال رهبری حضرت آیت‌الله سیدمجتبی خامنه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/676032" target="_blank">📅 14:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676031">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6502e21a57.mp4?token=O7EKYFo-wFh6vo9x_Zt7TFK9j4luA4I4w3dfPobkzjCiEhvY-05vGDaHkrMKxzytptaVddBUOLpZpEF6zt8Dj4RTyMFGVlqF4oTU87eM3HwYPqoKLkDmRz8GFFLrzhq_gZRjvIRKp5W0S_V6qJD0sEE85GiN_FZaVtub1TC2_usMDg8CWWNNgbuvve3CiZPLJunhTauhu8bpjXYUEigcg9yn4l29Ke6IrfFDeoTJfAC06dBg-z_bjIr-gw7tC1xvoKBqE4tZ2Kq5TCFZOTYs9QHfKVcc1drTWRo0YnYzatdI_5MI7hpMo5h3PxanY_OgBQw68uTcAV0m5x5jcXZ3SWqUkBI5pXOuhiOO_eXemzuZSe9um-nHYey_CRNZEmf4iTRFDEpseu2hO0_roVIOZmI49cxIrUJHRWolHuaAUJgMyw_v4J1WsMULTyTOZGnUF6NxB1yTin73UKpZz8qSQsZ2f3w7cqGyrBToh-rURl-mqtMY6foDu2uNvwdwHj88Oows1ogo5I5BboXDMcr-iHMFlC8Ak1lIvIalCIVu_80fYkoxYqDY-wOT3Rfd4CF4aeRK3rSMzpDJbJ5-602U2228oH5QnJdbWKVL5V2vpIn_lo2hDQv2XRpGYJXzt9XjcFsCiGAi75uh561nujes7U-UXtvrgmR-lU5w3QDJXME" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6502e21a57.mp4?token=O7EKYFo-wFh6vo9x_Zt7TFK9j4luA4I4w3dfPobkzjCiEhvY-05vGDaHkrMKxzytptaVddBUOLpZpEF6zt8Dj4RTyMFGVlqF4oTU87eM3HwYPqoKLkDmRz8GFFLrzhq_gZRjvIRKp5W0S_V6qJD0sEE85GiN_FZaVtub1TC2_usMDg8CWWNNgbuvve3CiZPLJunhTauhu8bpjXYUEigcg9yn4l29Ke6IrfFDeoTJfAC06dBg-z_bjIr-gw7tC1xvoKBqE4tZ2Kq5TCFZOTYs9QHfKVcc1drTWRo0YnYzatdI_5MI7hpMo5h3PxanY_OgBQw68uTcAV0m5x5jcXZ3SWqUkBI5pXOuhiOO_eXemzuZSe9um-nHYey_CRNZEmf4iTRFDEpseu2hO0_roVIOZmI49cxIrUJHRWolHuaAUJgMyw_v4J1WsMULTyTOZGnUF6NxB1yTin73UKpZz8qSQsZ2f3w7cqGyrBToh-rURl-mqtMY6foDu2uNvwdwHj88Oows1ogo5I5BboXDMcr-iHMFlC8Ak1lIvIalCIVu_80fYkoxYqDY-wOT3Rfd4CF4aeRK3rSMzpDJbJ5-602U2228oH5QnJdbWKVL5V2vpIn_lo2hDQv2XRpGYJXzt9XjcFsCiGAi75uh561nujes7U-UXtvrgmR-lU5w3QDJXME" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
این روزها با قطعی‌های برق، داشتن یک چراغ‌قوه معمولی کافی نیست!
🔦
چراغ قوه دستی ۸ کاره LED Torch
هم چراغ‌قوه است، هم پاوربانک، هم ابزار نجات!
✅
نور LED پرقدرت
🔋
قابلیت شارژ با USB + استفاده به‌عنوان پاوربانک
🧲
مگنت قوی برای اتصال به سطوح فلزی
🔨
چکش شیشه‌شکن اضطراری
🔪
تیغ برش کمربند ایمنی
🚨
چراغ هشدار برای مواقع اضطراری
🏕
مناسب قطعی برق، خودرو، سفر، کمپینگ و نگهداری در منزل
❌
قیمت قبل: ۱,۴۹۸,۰۰۰ تومان
🔥
قیمت ویژه: فقط ۹۹۸,۰۰۰ تومان
🚚
ارسال به سراسر کشور
💳
پرداخت درب منزل
👇
قبل از قطعی بعدی برق، این ابزار کاربردی را تهیه کنید.
https://memarket24.ir/product/brief/30291/180124/</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/676031" target="_blank">📅 14:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676030">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c0728305c.mp4?token=J3ksSUsuc3XTeCjG7kTFwRop03fEiv3OyKQEbkhRskAA9-rHwURb7s_NVMDPcpwRxDb5VzKoYZ9ncHKRmK19zuZNE51wquRmveBgmVMiaDP6fKYZlPGurh0nJFI7J03teZvcZwQ9l2kiaGLPT1TC4fjlVrASVvKfaZnWTfq899wjH5BEZaVtaHB0L9jy_YAE3qRrZPLtE0bsj0VpzFEOl1SrnZpIPSf_Ni3yfem3oqWAcd_hd9S3FUcCf4Bh0k6bFSE6euD_WvdUIh_SY8P_zz5zR5xr1bdcAurTY8izimyZqKc6-nK_a1IygBxQWb2-yqy9KDEeFFl3-803VRdBoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c0728305c.mp4?token=J3ksSUsuc3XTeCjG7kTFwRop03fEiv3OyKQEbkhRskAA9-rHwURb7s_NVMDPcpwRxDb5VzKoYZ9ncHKRmK19zuZNE51wquRmveBgmVMiaDP6fKYZlPGurh0nJFI7J03teZvcZwQ9l2kiaGLPT1TC4fjlVrASVvKfaZnWTfq899wjH5BEZaVtaHB0L9jy_YAE3qRrZPLtE0bsj0VpzFEOl1SrnZpIPSf_Ni3yfem3oqWAcd_hd9S3FUcCf4Bh0k6bFSE6euD_WvdUIh_SY8P_zz5zR5xr1bdcAurTY8izimyZqKc6-nK_a1IygBxQWb2-yqy9KDEeFFl3-803VRdBoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچ وقت در هر شرایطی بد ایران رو نگو
🤩
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/676030" target="_blank">📅 14:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676029">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
پشت پرده تکان‌دهنده سریال بامداد خمار!/ فیلمنامه دزدی از آب در آمد؟
🔹
از حذف ناگهانی خبرها تا ادعای نویسندگانی که می‌گویند نامی از آن‌ها در تیتراژ نیست حالا اما حواشی این اثر هنری بیشتر شده.
🔹
سؤال اصلی اینجاست: آیا حقوق نویسندگان اولیه پایمال شده؟
🔹
پشت پرده حواشی این سریال را در این ویدیو ببینید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/676029" target="_blank">📅 14:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676028">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEdY3oBLFP4s0cXJ7rzuPYlL8Qm6xovoOfbViBVokhg8HMBswL4tzjDA6EX1weBi2Po3a7Sv3P4raghO7bBJ9XFNQj5y5kQzl5CVKhBuWN5R34-Tq2x1udACdp71ka0XUR8mBCq4dnd9ytGmFAiyRf8CwFuNBTViRJ3G86w3UftGhQiQZUwrPRxG0AEf8z6Q_UcDZ9nX93A4BYcF_mdhM7_MN9qSaL9Y98e_DomgGoJ1hkV0p-5ITCyHEODUa3x1IUBjlIx1jfyDTDcR8N9X6g661SA8GRQpqsYi9s5nsOupovis3wInclQx6YvCzfHu1Cmi0dIkLZl90Jc1W1vWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: سپردن کار به مردم و اعتماد به نسل جوان باید دستور کار روابط‌عمومی‌ها باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/676028" target="_blank">📅 14:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676027">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUUUWOYCIeGKpDVcNDE-kf2lGcPy43M_ynQpiJr1eSaHveVIrbcAxXGQUcm10ax78SDe2rAYSXm11szDk_oRs8Szp2SEDcoChptqfwwtlWMV1jM2YL-dD-rO2g9mLP9eACopmRebrqBk6771OYDsYDwNtoxityjEZ7wqDIwicudoT20UcnDAXiG21GQ7UxAVdwA5zqVfTovPdCtInAt-DRjHehHBllbF5ZeZGO5A2H2LiHf6GhFDb4-ntEIvCnidpG7cLlrKuzYP7ye5QSa2ZT0-r0gWu0iuF1p6B0BzjTJ02DD6r9AkKTAw36pBbSrSRHGPjutyPWB3HS6MFU8cIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت روز طلا در ۶ مرداد ماه
🔹
بازار طلای امروز نسبت به روز گذشته نوسان چندانی نداشت.
🔹
قیمت‌های اعلام‌شده از اپلیکیشن میلی، به‌عنوان مرجع قیمت معاملاتی طلا استخراج شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/676027" target="_blank">📅 14:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676026">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
قالیباف: تأمین معیشت مردم در دستورکار حاکمیت است
🔹
لازم است مسائل به صورت کاملا تخصصی در کمیسیون ها بررسی شود تا خروجی آن به صورت یک کار کارشناسی شده به صحن برسد.
🔹
برخی قوانین را نیز می توان به صورت غیردائمی و برای اجرا در مدت چند سال به تصویب رساند تا در…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/676026" target="_blank">📅 14:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676019">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s9-RNQQUu605cJ6r-FNMl-tTQbI7-11TgSKDK3EKlRO0XAtlx5K6cbDOr3wtgzenRcwIORYP3Tf-CFipmuwDn6RoIcG5ErgTgmVpkfrk8JEHTwgFdNjGNuPCKKgyoiYoeaNcEHHEksCCKpLw6I-qxum6J-xXNV5G4sXlKEKDVSQmYBW1fqTVMJ0gCE-136hVhpb6otPMv7lSqv02b6JqEdhLi1xAVGaX-EQl12RU8N_9R-QybSCC9_cwMQNMMSiUnDDBlSSXtJOSwYE4QoKo_1dCHLAk9GIay1pqwisoCgUZ4U4UaLCspzXY6fhGanV_G7eZvfVwLLwZo7sVo6HnsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DvtJh78vxEXOSVo-E80RI1barcnGLsvsX4G82OZeOs1u-5dM4SwhynapOpM2un5ETAlD-3jp7aQTERQh3dZREkx_OXhOKBSrXiRccBG573Vf_2DGKWkEe_cBONQKkge-DrFX7DTR4-aXv9JkStlktusHmUMjuZ8FR5moHpb5_MaFNM1g_d1MiyphDJqntg8AjVWsD0YnpGjjV01lZAjQsO5PCCqk9PC297H1h4s8oDmSx2B6I2dHUK1djKPxYjDXPh6ND3p2IK_YHafrDoh68eAZlk1gwaDAlQkLy6VmEJOpXEI2d89AGQf9e3GuuXV6MqBKOcFwldP1umpfe_dt2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dhK9J7uWIng2jUyLdnZw29gqB5ap8GQVJPAokhVU38ZZAlRs62XdVMxxOKP1VU9hklDoAdlSYcCulYT9xIY0thVxFuL9l2p8G-zWTqvIo0Uf1j6G-HjN-FQwMtANUGgsOEAc-GekvIbFfbRIHLhq94IowH84ntaYLvIqLhUbaTqUEdOYW-ITCZ2za4LuALBtWBmbAbpE0HZw5F_A5fCrnrSzeXIyPx01ozAnvrsfmIhf9Y1vAUkuTVBToAaS-dmLGFzf0Hr520pswSG2xl_dmLLeX5h-rcSMRvtaTONnU_gLnTM8FHLvi6-kSwMrS7jowEena-3GE3_drQj_zmjfSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rg6qyqziPgBQb_VbXz0as_lFoyda28oyhuqwlDs4wFvxKyqzyenrV85bPwNfQswmBi09DTrG1T6C9s6LZ80WNtnqYdOiQWja08DVDXSXr3cLOFPUM5jmKZ00yhmKA1BZQcULlUhEfpIlScnRga2t3dxy5yuU4TC1DYaOvAVgx1keml2J3Ly0tz2bOM8V0iGgxyfD5ZJ_1YwZn-K7HT62wLyo8ykl1R9sv2f16dwIPjBi71L4Ff3W5nIkF86f-H8RYv4J-PToqlS0GbKWh0DvSf6bcb1IQ2aBuD_HVI9WBguuDcqxc1j0qzh0dS9-OXcmELUxxaA7wPmASZHube_Upw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RWPH2CJCj9zTTJcjPe4EbriXeX1gcrYk1UzKIUnJQS7-gqPdLz8BMpdc13elY6dHnXKfQWR_qyRBO3xlpbe8xyVMrcAcSAtKM6E_apUpcdt5stBqWhTiPG1CyhU0jWTCs-kcRRDUFgf6pRCMJNPtJKUy5ND-JcSlzvhzdmk4KQzKY9CcJvxwfAqwNMPcBP1knuaYJOWRv4Kjoj4Zk5VkDIpatL3_6r2zUkl-WKk49LX3atyZM5WNhHUdI3pjCpfRtfYFFgJKE6JIN26P2PhkcnE9mBcgNROF5ExGwKooDB936pRJULbsXWGt56pwu-ygbfoxJLNS6fiT1t82E4c9wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qagLfIjWxBDyTnSL0UMR9whHuLrGicW8sph3GFuy-jR9atx6pbvoPsLkKJsiwNe-W6iyCRNG8XuCArwbU1x0OEjU_kHP4O00-nY-CYQ29EDFXBy7nae3nb_7DO7rEHPFX3WarsATWdHnov40UL-wiD2X7mFgHRxsB3gE7nVmsxyBD8OS15ZH4du6-e0WDcwF7sLIDFsMX69dG858dFV7LTtUmzF-sTB_vhcsoKVy1cev163qpPfWJFdNXY-aHxJH0GUvyq2SSw15hyRA4uX34YG9YoA1eBga5Nxhpp0o73z5AsXMjT2nxGwncQ0ShsyhMDNE-BAYwVIM_rHGlyJy3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c7r9zzHztlvagt3zYBq1tHVnCj96guCoqIqDb2ULAISh5KjEpybk-jmYKgqYZRzMADBQxQTLoJ0uJqRwYArvdoL2uy7b-0les-2Jg_iY3gAdODK0_e0uJ-5ZvxlEu3EuUEMH337NqT6rW2JlBBrjmTOyGc5PbzQ4mr5-xkuxbLvuXshtXYjkFXL1uJThuYxVMTQLOA4BSnLOoP_fziP8vh0QaedKxnGdR996tMFCHctwPpZRvh_sa6obB-7kCRml_pHMxc-UyOtqjFt3_QPCcpmfP_gHRpcOFfKooA7jBhiVc9rU1OOat5xr9o24hoqfzVbhn94H0vsV0YHhsHvXcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اکسسوری طلایی یا نقره‌ای؟  راهنمای انتخاب اکسسوری برای هر رنگ لباس
✨
💎
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/676019" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676018">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله طلاسی | پلتفرم خرید و فروش آنلاین طلا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2V_g-qfNdSDk5v37KSkLOpS6kiWwOD0hD_RtY8MzORaoZPwryCPqOYAwHP9KvsDI7LmfGyUq7eE88D3l_yOepUv_e32Akvf1pBB7aWbz6nF9X_0s_jiZ8jSCWg_dJPs0aK2nDwObCmFqO7_UONBylXdNzyBOkRR5zo7Ikl6hD4H0b06akY-iAr7eSqwcUu9ueyB95ErfnOuPWZBTd-Gz9_NBG3wQGxlx9oafLkc1wzqpooSQwAu4ILAQ0L0dffVNzR2XPoit8K_7J9tHuICjN_QPAKX3up0pNp_f_atGF5hHUcMsmjFQ7dU4Gq2xBL5C-EuxiCMFgvRWeufkH5Ofg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین فرصت ثبت‌نام در وبینار رایگان
🎓
از اولین خرید طلا تا سرمایه‌گذاری حرفه‌ای
👤
مدرس:
هاشم آردم
🗓
سه‌شنبه ۶ مرداد
🕗
ساعت ۲۰ تا ۲۲
ثبت‌نام تا
ساعت ۱۸ امروز
امکان‌پذیر است. همین حالا ثبت‌نام کنید.
🔗
لینک ثبت‌نام وبینار
🔗
لینک ثبت‌نام وبینار</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/676018" target="_blank">📅 13:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676017">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5eYvkR825k38BLrXhFObys3Sh--2OfE4ce_NTk-Axrd9YaODnjQ913vmqI6LT322VB_l1D_K4ouIIwRIEq7jCcl71ZFJlVg9bDly61ZeyT4FFcVuVG7dKmkNXqr2qLoPELFn6szzf82if2g7lxT1a80cb6lQQMNujtqC07NF-Y8BbIxuH6QS020dXe4lIf71pU5U8Sy4spZ_0eaiypDs3CSuhc5fq64OU1n1_UDy5wY1GjfV1UIDiXFYKBMgyH6jL_bYFmtJ4jEJQCqzzQs1mLjD6ojqa9zgN0Xn7kWxJUFRjE7YlnnDbY1S3WItMwD5iPXyu9VJldnTtiR1F4FMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: تأمین معیشت مردم در دستورکار حاکمیت است
🔹
لازم است مسائل به صورت کاملا تخصصی در کمیسیون ها بررسی شود تا خروجی آن به صورت یک کار کارشناسی شده به صحن برسد.
🔹
برخی قوانین را نیز می توان به صورت غیردائمی و برای اجرا در مدت چند سال به تصویب رساند تا در شرایط بهتری قوانین دائمی جایگزین شود.
🔹
باید با ملاحظه درآمد ارزی و ریالی که اولویت ها را مشخص کنیم که البته همه این مسائل قابل حل است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/676017" target="_blank">📅 13:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676016">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بیمه سلامت: ۵ دهک‌ درآمدی اول و بیماران خاص و صعب‌العلاج از پرداخت حق بیمه معاف هستند.
🔹
معاون شرکت منابع آب ایران: بارندگی در ۱۲ استان پایین‌تر از میانگین است.
🔹
صنعا: ریاض باید محاصره را پایان دهد و بهای اقدامات خود را بپردازد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/676016" target="_blank">📅 13:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676015">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ادعای وزیر جنگ اسرائیل: ما قویاً خواهان حمله به تأسیسات انرژی ایران هستیم، اما ایالات متحده در حال حاضر اجازه این کار را نمی‌دهد
وزیر جنگ اسرائیل:
🔹
۷۰ درصد غزه را نابود کردیم و الگوی آن را به جنوب لبنان منتقل کردیم.
🔹
ایالات متحده در موضوع ایران ملاحظات و منافعی دارد که با منافع اسرائیل متفاوت و فراتر از آن است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/676015" target="_blank">📅 13:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676014">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeaMh7mqFqe_6yO7Jn6okW2dIMSjV8TQkQipei5lW5RUfRpTqJ9zhTAmIkAK09xEtu51v47hXURuU9x4I_s7ZUhmhnpe9skX4YcDxLrvuUVFm9Ji-gdxUMq7X0jPnadVb1_rwDI3GZQR1zCEIsZx--kF3cGFwlvMkgCpgV-rIS6KEk9TAp3ib8ilBNt_Jd-My1c2crm7G3zZbh-FQnr4pPp3MElJrxZGkugB0TbiocW204D5vajk04ZS_72urgaRu5TNp0WK_GT-oilX8TBn5uurC2-v8ZOSiFayJMIeS9eHy3Kp-uY1iMS6Vr7LFENQOLQWecIJA5Jr23EDW7E6qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۶ مرداد ۱۴۰۵؛ ساعت ۱۳:۳۰
🔹
قیمت دلار با ادامه مسیر صعودی و افزایش ۲ هزار تومانی نسبت به روز گذشته، به ۱۹۰ هزار تومان رسید. با وجود کاهش نسبی تنش‌های منطقه‌ای، نااطمینانی‌های سیاسی در کنار تورم مزمن و افت ارزش پول ملی، همچنان محرک اصلی تقاضا و انتظارات افزایشی در بازار ارز هستند./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/676014" target="_blank">📅 13:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676013">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
مهاجرانی: تصمیم دولت درباره بنزین جمع‌بندی نشده است/نتیجه نهایی به مردم اطلاع‌رسانی خواهد شد  سخنگوی دولت:
🔹
دولت حق ندارد منابع نسل‌های آینده را به آلودگی و بیماری تبدیل کند، برنامه اصلاح نظام توزیع و مصرف سوخت از قبل در دستور کار دولت قرار داشت.
🔹
در ایام…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/676013" target="_blank">📅 13:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676012">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbCp9FcYWP6ZIbsVP4Ja4F-abtY23y7XwoFqIkqHMOtbl1MJsvVkfD4RMc1Gokfwzva_AiIfuI7OEqPxBGyxiHf_XtKc1_EtRHMebv4MLj0yKcZRY7Mc2YamixTsFbOAzZis0nKqhKHO5DLtryge3o5UID9VcKsKZnWK3tSCQviKiuxPsSADDRhEd_sYVeXVFMlZiyVZg33v6rmXUcIiONiP_AghcDM7HKSnOsqhKcr6YDyZw_DrlSeNH7cQRz62ueH44R_YSQAOOm6QvtDwGpJPw7mdHNL_OEV4Rfvx9j7du18gGt6_vglOrRR1V-fu074d3Vb_TAO5R8eLMnfj4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکورد ۳۰ ساله مرسدس بنز به عنوان خودروی ایمنی معتبرترین مسابقه اتومبیل‌رانی جهان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/676012" target="_blank">📅 13:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676011">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtrFRXhbbu-0rsEdAGFd-iW-b2pb3IXj9zZhzFvAwOba7hv3RH-e7jIjOMynAZ3i3tZP9-RXWueeTmmYI9gn3kvdHbumtSr0Wk-RCA7Pj9b3v1MvCcpI3TrPM7lbdDHuywU2RJl-7zstOquqScGlAfZ554PiiJYSyIb0OH-zN75ppEoDxrl2dbmP_9gse_a-u-g0GY_oAuY0iBmxzyCXi9OcNoRl1L2RCmsoXmO5T7N1_Ci1vS2Z7DX1pjCW08x7DW0JHKYNgM-mc0WMJ4w372j8spVuSmcVq9yktKlJ_XKZEWmr52LvpW-ki_zCjfX-rTC7QpmEdah5JxCJzXi8bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شوک جدید به بازار موبایل؛ آیا گرانی گوشی‌ها در راه است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/676011" target="_blank">📅 13:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676010">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FR6vKqZvX2vVVSnmt9_NSczrUYm99rFKQZrZfLIrtXOqYECTiXVLZZunrRiDBDUif1Ezcc9wOUeea0l4j2Z9B5PoFD6I4Ne26A8vrSBqSZ2keNM-oja3pjZzIsH2EBbtA0X0SnB_qiCXZ8ArEx_k6xSpGCiMGCWBPzQnR4dlHnTlAjx3uHQ0ZzH7R0lqU6AD15Jx9BuqCWkHB8GoJ2DOyCpQIBkiOr5Aw5hOXS1L7rM-4efEs2nRhQ31fVAG4bvNg1pkWctoqHOLACfWDMP0FfPTYPgemDaJuueA8h69HnSoUeWlbOaq-B61Ga9BlOTZe8wZY_noisDCsY7tH2c0jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ای‌بی‌سی نیوز دلیل پا پس کشیدن ترامپ از جنگ با ایران را افشا کرد
یک مقام آمریکایی:
🔹
تصمیم به عدم تشدید تنش پس از جلسه کاخ سفید در روز جمعه گرفته شد. دو منبع اعلام کردند ژنرال دن کین (رئیس ستاد مشترک ارتش) و جی‌دی ونس (معاون رئیس‌جمهور) نگرانی خود را از تشدید جنگ ابراز کردند.
🔹
کین به ترامپ هشدار داد که اگرچه ارتش قادر به اجرای گزینه‌هاست، اما پیامدهای منفی از جمله کاهش ذخایر مهمات وجود دارد.
🔹
کمبود مهمات یکی از عوامل کلیدی در تصمیم‌گیری ترامپ و تیم امنیت ملی بود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/676010" target="_blank">📅 13:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676009">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U72i8VE9i73Fh3W58HGKO4HKznARYrlwHlG7C3Xcu1Z7jP6Ib094gvdngVEMPmmuWjIv6pi1IiJ5K4IoZ8TL0L5x61LzT6SFr6OOUcTA3Qf4dGA8B-AEH14LtO-SSDbtYt0eUSN0l6DH0f_0JUxm7lR-9iEO7BfhrvRNHUQrzfqMbKTjbzW-RQVjmKErQX2LUDzQVPbapex1BEMIRL0QRiQN7V3oI-vco-9Px1Crjey10JoZStlunwhcgphZYt9KZAh9vXyJ7Ists3c7kbuiDCrjL2HIm2alCzsjqh3fVX3mdhMCZxqGwNqEyZwBKPFq2X_iBEGhGh4okwKH-jmo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مس رفسنجان نقره‌داغ شد
🔹
تیم فوتبال مس رفسنجان در دیدار پلی‌آف لیگ برتر حاضر به حضور در زمین بازی مقابل صنعت نفت آبادان نشد.
🔹
بر همین اساس با حکم کمیته انضباطی، صنعت نفت به‌عنوان تیم سوم لیگ دسته اول به لیگ برتر در فصل آینده صعود و مس رفسنجان به لیگ پایین‌تر سقوط کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/676009" target="_blank">📅 13:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676008">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlE28wZZvj4k8IqKAidfMy7TyVILdbkpQrGsjJiB-WFIlRVa7plg1xy2gVG5QpeLzBnETjcYzY6zG-IyBXmxwG_e-235054WhKrGWYXEgQX3RE1FuxIQAXTlNA9Vs0J0A3Zzl0L1k1Pz_rD5aMdHHlt8W_gW_ic44PkyOOh7DQkhY3fAvWzpc6DVTuudzeO7cBOn-YKqlHdrb6ybwjLlf3AQDNIaFcBm8LuyGWXf3y0DkIfxxplky2QFafY-0h2GYWodWmMw35td6nZv47t26IYekwQRbrYhi9WrH94lIG_8c7wljfZiIqlT7Moj2LzBPcVpYaBPh1xD2JjGZE0Juw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دنیای شیرین خرماها؛ آشنایی با انواع مختلف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/676008" target="_blank">📅 13:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676007">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6XB1HZeflRaomm9Al9w5WfowGlaN979Z4PXglJnJZaZ24kFC-lR4OfSLJUyZ_-gW4BDma9UgTsWMinPoUcOVTtWtW8EGX9ezkwky3WCIUiAkYMuIX0ubSW3ZhCNVb4DHLiRNTheaCXHrxVFf5y_DFZVA_mxymJjklL5fr-8UMNrTDPV_dMhi0j1DQNJCuucVsBZWq47QAx7n3mHnNcRvYu_BVJ1TJ-cwvp6ErRVnrmI60w1Jxj5zFud_g-YBNeEaRb_BxklwM3ZpUQ4Ps4gNuUL3qqBF3A532u0CVBUNdEwYHHlPVvqUriubpr2TdBavVfT93K3jGk2ImrZfarp7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طارمی به برزیل نمی‌رود
🔹
سایت «GE globo» برزیل گزارش داد که انتقال مهدی طارمی مهاجم المپیاکوس به تیم واسکو داگامای برزیل، به دلیل عدم تمایل مهاجم تیم ملی ایران به انتقال به فوتبال برزیل منتفی شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/676007" target="_blank">📅 13:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676006">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8890acae80.mp4?token=OtsByabGJ5MsJyAe9E1V6Cwioeht1jq__nejpZQ_zSy9lhLhE1BIYUOQ_hTBWgI0uWuCERCqHMg77uLn2hhah14UwL6zZHwfM3QEWAjxEEpKDXa-6n4baosAKSc9Q2EDZO-31_pM3T6LBn9BLBNPAIrNESbGD0l-yD9SbeKOWUj8AJsakykzmAraE4PaeNsQ80afoxyr5IgBlUxORjwGr1QLnFs1TjSmNfDYQ-CVkFlComoFJY99kU5ee7OX3YwvuC4Hp8j68IEt5uHHg57ZYij5AUjcBmXNNTTES4KxNMGKIWibg5VseMwuZESwXfCZCuOLJyiqbULpb_jlMcFb0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8890acae80.mp4?token=OtsByabGJ5MsJyAe9E1V6Cwioeht1jq__nejpZQ_zSy9lhLhE1BIYUOQ_hTBWgI0uWuCERCqHMg77uLn2hhah14UwL6zZHwfM3QEWAjxEEpKDXa-6n4baosAKSc9Q2EDZO-31_pM3T6LBn9BLBNPAIrNESbGD0l-yD9SbeKOWUj8AJsakykzmAraE4PaeNsQ80afoxyr5IgBlUxORjwGr1QLnFs1TjSmNfDYQ-CVkFlComoFJY99kU5ee7OX3YwvuC4Hp8j68IEt5uHHg57ZYij5AUjcBmXNNTTES4KxNMGKIWibg5VseMwuZESwXfCZCuOLJyiqbULpb_jlMcFb0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهترین واکنش به شخصی که به شما بی احترامی کرده...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/676006" target="_blank">📅 12:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676005">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahvacomplex</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd22100af.mp4?token=aK8JXJzKjEzJ79hhOflGyP_2EE0PjcIzvwC8GMQfcUWv427Ubl_wPaCWt9z3sNlCPda2xbyHVxQbZ2MI4qgDcTiS14tklgAkRFWwSph7JBv7kfdeLRhdaarlpeVEM8xEfwagEOJvA-VxEXkxKV3CYbXH_bYO-W-rQvrpxtZleZX6pfZ2TX8wtuTuCSjwsRmTDjH51v1gBL0QfTl_BTG6EYykif_LS4tgEB5RryCGzezs0hPhFwT2PhiywSuqAzjkbGtiixesAouWhhCrkfyvqHWcF8bEgfeyt1Wi1tP3j0ddKnc-uSLaCXeoHimkJd_BCcK1PdYa6TW8TwivAktDJwYHuBIHLW_4iUsorSg7xyId0JLi5naI9QRK7ygQ2W3MI6fVXWS-wU9_HGMmB9Q2KH4jXdozuNcE_gWJBJqluFHHpLE2xv8dK2vyj8YRRSkD0VZb9DZhkO7bcm0v_hL1BmqURiltelzj-_ng5gFggkOK0b3GYavee_CJSvmW62JDvNhRqpGTsa79j9Fr0XPMXV-S2yG0BWXIqzdhWr-ewUllJAgPkUuMjtYCN9uAa9p3NEopGV1Td3n_azvjFPD8XNQNbzeAH3GsSLu0JdvNGxun5Qz70l6SYx21opq7FE7bwaooQPAOAPcPwsesrxeGWVRQqEHKSy-YY8RWpaBjbuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd22100af.mp4?token=aK8JXJzKjEzJ79hhOflGyP_2EE0PjcIzvwC8GMQfcUWv427Ubl_wPaCWt9z3sNlCPda2xbyHVxQbZ2MI4qgDcTiS14tklgAkRFWwSph7JBv7kfdeLRhdaarlpeVEM8xEfwagEOJvA-VxEXkxKV3CYbXH_bYO-W-rQvrpxtZleZX6pfZ2TX8wtuTuCSjwsRmTDjH51v1gBL0QfTl_BTG6EYykif_LS4tgEB5RryCGzezs0hPhFwT2PhiywSuqAzjkbGtiixesAouWhhCrkfyvqHWcF8bEgfeyt1Wi1tP3j0ddKnc-uSLaCXeoHimkJd_BCcK1PdYa6TW8TwivAktDJwYHuBIHLW_4iUsorSg7xyId0JLi5naI9QRK7ygQ2W3MI6fVXWS-wU9_HGMmB9Q2KH4jXdozuNcE_gWJBJqluFHHpLE2xv8dK2vyj8YRRSkD0VZb9DZhkO7bcm0v_hL1BmqURiltelzj-_ng5gFggkOK0b3GYavee_CJSvmW62JDvNhRqpGTsa79j9Fr0XPMXV-S2yG0BWXIqzdhWr-ewUllJAgPkUuMjtYCN9uAa9p3NEopGV1Td3n_azvjFPD8XNQNbzeAH3GsSLu0JdvNGxun5Qz70l6SYx21opq7FE7bwaooQPAOAPcPwsesrxeGWVRQqEHKSy-YY8RWpaBjbuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📣
اکران «افسانه سپهر» در روسیه
🔻
انیمیشن سینمایی «افسانه سپهر» به تهیه‌کنندگی مهدی جعفری جوزانی و کارگردانی عماد رحمانی و مهرداد محرابی، از اواخر مرداد ۱۴۰۵ در سینماهای روسیه اکران می‌شود.
این اکران همزمان با پایان تعطیلات تابستانی کودکان در روسیه برنامه‌ریزی شده و در کنار نمایش عمومی فیلم، یک رویداد ویژه با رویکرد همدلی و یادبود کودکان میناب نیز در حال برنامه‌ریزی است.
نسخه روسی این فیلم با عنوان «Легенда о Сепере» ثبت شده و تریلر آن نیز در پلتفرم کینپویسک منتشر شده است.
https://mahvacomplex.ir/n/938003
@mahvacomplex</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/676005" target="_blank">📅 12:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676003">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmY16FdUXq5coJL3dBXjzw8ppl5PIKkPYmOTDDHyUB_mk7pHnh6nq1lwYQ4TnO15lXB2nV8XmjNM5ZhSbcH025BcMErOHU4FvY5eklqfabkMwHXimXsKp2YRpzUx6bDn-I-sY7V9ZdIREo-jMpSewwJkbyo46dvlwdF32Yy6X0-XAWB15mx-cEXAHRx_MYoZP2U-aCs6HE9InH2w1zhla3UMVP_DlFXwqM4bT-xm8LF00rP41wBLhKvZmoCMdlqjYMrcNCLvLR7XH60zrUBEYyFnwuqChPG2JZw_XKJGdwR5w-OHrVYgC-Tc-RvkOCx3GOg_5UDYAngg2E7QhwuSCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سه کله پوک
🔹
ترامپ، نتانیاهو و زلنسکی در کاخ سفید؛
یک میز، چندین نقشه، و کلی خیال‌پردازی درباره آینده منطقه، اما مشکل اینجاست؛ دنیا همیشه طبق نقشه‌های آن‌ها پیش نمی‌رود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/676003" target="_blank">📅 12:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676002">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXaqmJK9aIe8kqdjl7ULfius7eR953_vtxg99v_QICNk5o2EPiZJTJlyk6I_3DoJjLWNf3V-nrHHIYgYnSgmW0BBWeXufkJodDgzfvNGGZj4BWkKZnjoE68FqukYxdebBElc1qu8Zd9z_iwroZPeIhywxeyKFLG7Iavnl3ULI6rLJC5xIgDpTMIxPLZHPhPH9Z-zQgf-ZDUDq7K_kdCMbhTdUEAuBAKqoi4eyI66uKWvtgH_PlJKEoZxYXrNb3NHS3cKgL6-E7h1_HjcGlpGlN14x78K4iSyj4Y84y-hw6OMPobQ1kD4ZJnokyFbBuWv1zx8k303Rgn3tBKm1yLNMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زین الدین زیدان رسما سرمربی تیم ملی فرانسه شد
🔹
با اعلام فدراسیون فوتبال فرانسه، زین‌الدین زیدان تا سال ۲٠۳٠ سرمربی تیم ملی این کشور شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/676002" target="_blank">📅 12:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676001">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9233560c18.mp4?token=YTC1rXC7AkxKbOzFtwT4bEryyscHXCoCyjq-zjRKUPGBO_Kb7ZvIMPhOddQVjvdGOB3juCnUTaI_t-pb9QNDfyQezI8dsiI3mCpSaxf576V83SJzZdCVtfX_qAW392pnVGcnwHc6XhcovREYbRGhmGO1ooPM5CDQUDXrtKTlQ3Ys0dTwQhRxhgNolsGL4M-Lo5henAnkv8KIVRx1Lwgy11hLKa1A5-pxnPuw8F4KyjF1cYaFtT6_fjAgx-A1H7fsChpkvTeMxzms7RXfx-MapNPYhzj-T0ZyqC3YfzoNEsHNGcf-CGD5ejdTn5Qtpw1BYi0FyRudgJPvCt5cnQWoQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9233560c18.mp4?token=YTC1rXC7AkxKbOzFtwT4bEryyscHXCoCyjq-zjRKUPGBO_Kb7ZvIMPhOddQVjvdGOB3juCnUTaI_t-pb9QNDfyQezI8dsiI3mCpSaxf576V83SJzZdCVtfX_qAW392pnVGcnwHc6XhcovREYbRGhmGO1ooPM5CDQUDXrtKTlQ3Ys0dTwQhRxhgNolsGL4M-Lo5henAnkv8KIVRx1Lwgy11hLKa1A5-pxnPuw8F4KyjF1cYaFtT6_fjAgx-A1H7fsChpkvTeMxzms7RXfx-MapNPYhzj-T0ZyqC3YfzoNEsHNGcf-CGD5ejdTn5Qtpw1BYi0FyRudgJPvCt5cnQWoQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهران مدیری چرا به مراسم خاکسپاری هنرمندان نمی‌رود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/676001" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676000">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac175e4e98.mp4?token=VUeXZqs1d12xL__mLJ1X3ET3kZn83f3sz_fRsm23AGGzSxxjJ0d4Sfgdy2nml9Ka-Y51Dk0Lhv4A45Qvz8YZ0sLmmcW_m2D-QBt5UbGF4GPLL2SsoUIzVmQdM9Gqst0p1Ax225R3KguM6r33HzwztwKBWLEpTAjntVQ1o8bEVhuLN_18HYBxI_R3JVgOZEVIphxI39465RchW3EPViUymcTKRO6Vvp6g--7sz7PBn0wAiFV3n0t-uc_A4fGmS36aKZl9-u8JtRdNSYkhd6aMLunycE4KX8eecVgQrDyWzCOyBH8GvII9K1Akqi_cdVH_tuwsytX3bGIwEl6t2bL7kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac175e4e98.mp4?token=VUeXZqs1d12xL__mLJ1X3ET3kZn83f3sz_fRsm23AGGzSxxjJ0d4Sfgdy2nml9Ka-Y51Dk0Lhv4A45Qvz8YZ0sLmmcW_m2D-QBt5UbGF4GPLL2SsoUIzVmQdM9Gqst0p1Ax225R3KguM6r33HzwztwKBWLEpTAjntVQ1o8bEVhuLN_18HYBxI_R3JVgOZEVIphxI39465RchW3EPViUymcTKRO6Vvp6g--7sz7PBn0wAiFV3n0t-uc_A4fGmS36aKZl9-u8JtRdNSYkhd6aMLunycE4KX8eecVgQrDyWzCOyBH8GvII9K1Akqi_cdVH_tuwsytX3bGIwEl6t2bL7kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب ترین متولد تاریخ رند (۰۵/۰۵/۰۵)
🔹
این تولد صبح دیروز رقم خورد ، نوزاد دختر در حالی متولد شد که مادرش متولد ۸۸ بود یعنی ۱۷ ساله و مادر بزرگش که برای مراقبت از او به بیمارستان آمده بود متولد ۷۰ بود و تنها ۳۳ سال داشت ...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/676000" target="_blank">📅 12:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675999">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
رشد بیش از ۵۶ هزار واحدی شاخص کل بورس
🔹
در جریان معاملات امروز شاخص کل بورس با رشد ۵۶ هزار و ۹۴۸ واحد در سطح ۵ میلیون و ۱۰۹ هزار واحدی قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/675999" target="_blank">📅 12:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675997">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
احتمال شنیده شدن صدای انفجار در جنوب و غرب اصفهان
🔹
پیش فروش بلیت‌ قطارهای مسافری برای بازه زمانی ۱۷ تا ۳۱ مرداد از روز چهارشنبه ۷ مرداد آغاز می‌شود.
🔹
شهدای غزه به ۷۳ هزار و ۳۳۳ نفر افزایش یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/675997" target="_blank">📅 12:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675996">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
سارق سنگ‌قبرهای بهشت زهرا(س) دستگیر شد
🔹
سرهنگ سید امین موسوی، سرکلانتر دهم پلیس پیشگیری پایتخت، از شناسایی و دستگیری سارق سنگ‌قبرهای مقبره‌های خانوادگی در بهشت زهرا (س) توسط مأموران کلانتری ۲۰۵ صحن مطهر خبر داد.
🔹
پس از بررسی‌های اطلاعاتی و بازبینی دوربین‌های مداربسته، متهم دستگیر و در بازجویی‌ها، محل نگهداری اموال مسروقه لو رفت؛ مأموران موفق شدند با حکم قضایی، یک قطعه سنگ‌قبر سرقتی را از مخفیگاه وی کشف کنند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/675996" target="_blank">📅 12:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675995">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589965cc.mp4?token=e4FnkwX4rDLH6Yqs7OIJMqinbrjwglML7gL2USKHFkTTpE_D5oCzu7ztca439pzTcSqwV6Uh9rZnYaMPXSSXssdIo03whQAQ5hx7BppdFBAY6UZVgWK20cwgW2Yqkd9j-c4l9aC0XaN5oLI74oVEzm86HwRSQ5NX6VPkU12kqAw75eRkPk84RcK5YhV3_xPb9BtCzgJZ884FIpjaOpiiG1ALdjyZx58JwwA-ITTNi3bEDOJm0GBnj9JZPn-q79tVmd_l-f4Wp58zZyyBWfdnk44Wmu4OR8qNpM8AMLXYmLL50V2TIgTwTzf5fo5oEX4yodRJHMKIshwgBtfYABeN7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589965cc.mp4?token=e4FnkwX4rDLH6Yqs7OIJMqinbrjwglML7gL2USKHFkTTpE_D5oCzu7ztca439pzTcSqwV6Uh9rZnYaMPXSSXssdIo03whQAQ5hx7BppdFBAY6UZVgWK20cwgW2Yqkd9j-c4l9aC0XaN5oLI74oVEzm86HwRSQ5NX6VPkU12kqAw75eRkPk84RcK5YhV3_xPb9BtCzgJZ884FIpjaOpiiG1ALdjyZx58JwwA-ITTNi3bEDOJm0GBnj9JZPn-q79tVmd_l-f4Wp58zZyyBWfdnk44Wmu4OR8qNpM8AMLXYmLL50V2TIgTwTzf5fo5oEX4yodRJHMKIshwgBtfYABeN7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غرق شدن تلخ نخبه ۱۲ ساله ریاضی در ساحل انبارسر
🔹
عصر دیروز ایلیا پایپر ۱۲ ساله قهرمان مسابقات جهانی چرتکه ذهنی Ucmas ، در دریای روستای انبارسر غرق شد و جان خود را از دست داد
🔹
تاکنون پیکر وی پیدا نشده و نیروهای امدادی همچنان در حال جستجو هستند.
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/675995" target="_blank">📅 12:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675994">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3762790f.mp4?token=lJq494EuDmuO1Jsiss83VrtThsky4-SToITa4w__Ekl9mYYYA0T3kqVAm1_rqPB-pEsCzpcbkknBkrYtWRxLriQWZd90EHddKCRUl1OXepZW0QS8baCrmrZ3NcocJ5QBp3kg4MQZDADn5kHMz5gQXThpgida5UuPE1LDZcP2nGI25sjqyEGHwOoDTLul0iUqVI6mOxYIifcZjVp1T59LrD9i0ui1h7Kqim4BO-D-abTL6vgjzpMVk0sBAlJ3jIqEF4m-hrUEDRDzgf8vknryYuY5RWDAWjlsWTEEZWjUiDrnVu9-1Ls9GJIDe4NMNDffq-DFfOzlaBsRzrzKe8qg_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3762790f.mp4?token=lJq494EuDmuO1Jsiss83VrtThsky4-SToITa4w__Ekl9mYYYA0T3kqVAm1_rqPB-pEsCzpcbkknBkrYtWRxLriQWZd90EHddKCRUl1OXepZW0QS8baCrmrZ3NcocJ5QBp3kg4MQZDADn5kHMz5gQXThpgida5UuPE1LDZcP2nGI25sjqyEGHwOoDTLul0iUqVI6mOxYIifcZjVp1T59LrD9i0ui1h7Kqim4BO-D-abTL6vgjzpMVk0sBAlJ3jIqEF4m-hrUEDRDzgf8vknryYuY5RWDAWjlsWTEEZWjUiDrnVu9-1Ls9GJIDe4NMNDffq-DFfOzlaBsRzrzKe8qg_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تفاوت استرس و اضطراب به زبان ساده چیست؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/675994" target="_blank">📅 12:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675993">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
کاهش ریسک‌های ارزی و بانکی با خدمات مشاوره اتاق تهران
🔺
اتاق تهران با ارائه مشاوره رایگان در حوزه بانکی و ارزی، به فعالان اقتصادی کمک می‌کند با مدیریت ریسک‌های مالی، انتخاب راهکارهای تأمین مالی و تصمیم‌گیری هوشمندانه، تاب‌آوری خود را در بحران و پسابحران افزایش دهند.
👈🏻
کسب اطلاعات بیشتر: ۱۸۶۶ | ۳-۸۸۷۱۴۴۷۲(۰۲۱) |
www.tccim.ir</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/675993" target="_blank">📅 12:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675991">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401dd7515c.mp4?token=VV6ZyHs3OV81LjNPggk51uowkGIwHUmMUZPWN1nQmd8GaNaZ1Ch3rg7wPgjZji8z2iv0T0i-hlahR5Ny4Px6hzT9_0b1vrIZr3VbXBwz5qGsW3QCqJUJK1bz1CSR9Bt8i5TxY4Rue8aGQYIAkDagEUQeBj6fEOWP6GzDWbCio6coLjR2PK60ZFG1TyMGIKVoa4WLLW4o8ChF-CEh-VtsJrbMLM84KTXaCakqUWcXOL0B6__6PovXzgW9otxgWrV00NWMPO8AOcrEmZicardIde1qQkjpQ7DdITofvW3wMACxJIBplZpClCCWDTDCBAULtuKBo62qxwFvEDbW4Av34g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401dd7515c.mp4?token=VV6ZyHs3OV81LjNPggk51uowkGIwHUmMUZPWN1nQmd8GaNaZ1Ch3rg7wPgjZji8z2iv0T0i-hlahR5Ny4Px6hzT9_0b1vrIZr3VbXBwz5qGsW3QCqJUJK1bz1CSR9Bt8i5TxY4Rue8aGQYIAkDagEUQeBj6fEOWP6GzDWbCio6coLjR2PK60ZFG1TyMGIKVoa4WLLW4o8ChF-CEh-VtsJrbMLM84KTXaCakqUWcXOL0B6__6PovXzgW9otxgWrV00NWMPO8AOcrEmZicardIde1qQkjpQ7DdITofvW3wMACxJIBplZpClCCWDTDCBAULtuKBo62qxwFvEDbW4Av34g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع زلزله۷.۱ ریشتری در ژاپن
🔹
زمین لرزه ای به بزرگی ۷.۱ ریشتر جزیره کیوشو در ژاپن را لرزاند.
🔹
در این رابطه هشدار سونامی صادر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/675991" target="_blank">📅 11:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675990">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d47105a77c.mp4?token=RVjh1-7wtZ_xtHCbRxnsEGIqdXZ6c4L35EKVetFf9SY5yQJtM04EZ8AyOUcrqfBms1wrGlmPShjIMhMq82A0GfQ1xPFvyxmAsxwQLZJrq3Pc6ozE0QSXnNFIg2VG_-ssrodi4Qene_GG2DFiTYOP5R2DbX9Ltez8dNSHhIovQplSfFbVDLst3f02o2iAOiawJDsTL8fHP6NR00FiaNOxCp2BsVr7A8xOAiABtCnO-AtF0bkI0NuOwMmxDPTuyU7POOQphB3NuT7pHZ9__5mtqAeIVBJeh4X-0niDjpCcspsPqCfuLVD7ndRUSXVcyur3OEhnP5G71-tpaTVQU7xNRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d47105a77c.mp4?token=RVjh1-7wtZ_xtHCbRxnsEGIqdXZ6c4L35EKVetFf9SY5yQJtM04EZ8AyOUcrqfBms1wrGlmPShjIMhMq82A0GfQ1xPFvyxmAsxwQLZJrq3Pc6ozE0QSXnNFIg2VG_-ssrodi4Qene_GG2DFiTYOP5R2DbX9Ltez8dNSHhIovQplSfFbVDLst3f02o2iAOiawJDsTL8fHP6NR00FiaNOxCp2BsVr7A8xOAiABtCnO-AtF0bkI0NuOwMmxDPTuyU7POOQphB3NuT7pHZ9__5mtqAeIVBJeh4X-0niDjpCcspsPqCfuLVD7ndRUSXVcyur3OEhnP5G71-tpaTVQU7xNRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معروف است به قدیمی‌ترین چای فروش ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/675990" target="_blank">📅 11:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675989">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
یک‌چهارم نفت دنیا قطع شد
🔹
براساس گزارش روزنامۀ وال‌استریت ژورنال، حملات نیروهای مسلح یمن به کشتی‌های مرتبط با این کشور در دریای سرخ و تنگۀ باب‌المندب، ریاض را با یک معضل راهبردی جدی مواجه کرده و مسیر جایگزینی که برای دور زدن تنگه هرمز ایجاد کرده بود را نیز با تهدید روبه‌رو ساخته است.
🔹
اختلال همزمان در دو آبراه استراتژیک تنگه هرمز (۲۰ درصد) و باب‌المندب (۵ درصد)، حدود یک‌چهارم (۲۵ درصد) از عرضۀ نفت خام جهان را مختل کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/675989" target="_blank">📅 11:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675988">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNz06GsxLGRykpaIXW3ZpA9u04Zio2fPJv44bmhfA7SjsSR3VwXIeM9K5QNIoIlPgIKbWk4UxpnnDSbRI_r1Dy4sHk56ZCbaGHG3OnRK0WiT2ZikJaQC5ncvShQgUJWiS5RMKBnV7YQDuU_spO9DxEQTGrbEgh-0tQOpzqGOxdJGLQt0FDHXuw9xW8WK1foaiMKORjeAdPwvuiBVH2_TY5ElQBTwv4HJd4gduxFXn-BQa1_4eswhvkSLIhCy2uoHYxSp-Lt217GARiGgIZIpd0xCwwiopCRKziAEQdni_k9If5PlvpMeyLVpMV5D7wLw9Lwc_Qdmpoc12AQowVdksA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
غاز پا آبی معروف به کودن‌ترین پرنده جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/675988" target="_blank">📅 11:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675984">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uL2tmH_6GvIv-yIYUBj83fYxTKxpT_8_2UVUI13bw5SmnJqJqjjyITP7rtxG9tQB89qNOtnXoSGW4vnef__1rG4xy3RR_-0QL1Nu3wV4iaOraJofNbbWn3xyNRyBROQUG6aVVk6a_RGvNSz3r6fzusP-RAbIJmLGDot6umb2u1trdvaWts-O4LzUTixF7MYijnF9IzS5nRATXqu9ogmQSAWVgL9mosWsLUpItiMfMtNdij6ycc729H2GmpjyG00xAiAl-jfHbRlw3aB9kWxwy9gcYCTB80C1plHYxo8I9PwG9PsXqxLo--sEfpaKedooB6VR4_Ulu8jfCOa_BaD4qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TzS026CQKDXNROlmUp9y7bwcXtDLhM5ic8X1r3DerF6Py9-7pztP1rpaP9RElSHuWPDCbwn5b_TntZndyKMjxVQhZ7nJ29J0YaGCU9M0Jp_6pMFGdcp2zFuwT8tlzQvRbAv1ANaIMmi9YotnXlOXm2M5LVp3fklGIfHNLlZo4Ch6ukk_rf18T6srcP4TsXfJSehiAoEYmFIW_iqifiFT-4hfSWN5DOsQEBMQKqo3fXXUnCxZaJb7gDaaWTfzKmX1-zWMG29qq_-4of28AlxMLKfQS3IDRgoQad8jyAj6a5w6flC2FKlJRnoQcvZhTObGASBXMijpTzTsoJYo2_Q1BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4UrdB8Jw3ddDQ1xDkSbu6O_M-OhwEMOF3mRlT-oRVQDHVHW37k5BehqNNKvCHpaitG1hGhGWZX_vkeOVpGKC2y4TDpt0RYVn7OYaugAiUxd99IF41mKqfSxn8INlxL_xGDNVi-Etf0paJkoXZAVFNPJkBKl5pcdHDTxpyYLRzDMCPXjiUjymjT5xCeYNbahCUujv3qDF7SdvUmylnIrcjp2K501C9e0u4dTTN-g9D69ezjO-SjsFzkTv2ob_jcrAQGbtuG0KVtfpI2Y_0Gywmg_AfzbdBJ073eo0FyuUdsOT5XKbQ9t96cZj2Q70vL7rOpy-R7M2mg6TzMyEAkDmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DEytCAtmf-NWf67BvQ_7M3fU8SO54BPJOf357JjM_PzEKrV5ka0j3SndeEozLurHpcYhnJhHMur0aB0ACO0Bs1EEg3jH4rt43hocVtQy_q3o3FeL5MCrUKF8i_TBfJRKcaALQUB8_ZyBBBD60SwJet33DdeW7myrVEw8F-B67s2S--4k7zQGrCJKYaE4pODiPij0a4uDuCQSBmQUX0QnPmYGkZ93_RYkSePqBScYGP5iTreYYzerzWWuW_EAJo5DYN7RF-CfMM3ucvhfvNSkjnDXCBaYKo_DpH6f1FC2oCcNlUmsCoMK-bwpkDJFLpEDYG0bRMTzIBjp2f_Sgkh04Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
مدیریت صحیح مصرف برق، با اقداماتی ساده و روزمره از خانه‌های ما آغاز می‌شود.
🔸
استفاده از نور طبیعی در طول روز
🔸
روشن کردن کولر فقط در اتاقی که حضور داریم
🔸
تنظیم دمای یخچال روی ۴ درجه و فریزر روی منفی ۱۸ درجه
🔸
خاموش کردن تلویزیون وقتی کسی آن را تماشا نمی‌کند
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/675984" target="_blank">📅 11:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675983">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/141a9579d9.mp4?token=F2NT3HLD4x0EKRXTFhp4JSQAcSfm9JPsuf-OlD9_l3bumK3SLZhFyUrxyivPC7_eNyiPZqXlZ3HQ9nGRJ85s0ncM9WX3B3uk6J2hp2kIRYUSo4MlS9QrquppNdcfKGtuZ3uSNZMbjwu45yr4k9-F01NSaTxbHVv9KnQq8vFjIphoqKa6Dj09r7neNgVqhq-7YqkU_Wyok9cevdck1C0EkEBMKULuec5VobTn9s55iwqRmQhkm43yU_XjBxtoWz-FoaQE8Vhdz6lAsUK0LZAnRPN9DeMEtn9lO2U8iqWwz6vYhbGUxN_1BDpAwJEPZDx4b7rDOT7F45D0MbTpLZHrHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/141a9579d9.mp4?token=F2NT3HLD4x0EKRXTFhp4JSQAcSfm9JPsuf-OlD9_l3bumK3SLZhFyUrxyivPC7_eNyiPZqXlZ3HQ9nGRJ85s0ncM9WX3B3uk6J2hp2kIRYUSo4MlS9QrquppNdcfKGtuZ3uSNZMbjwu45yr4k9-F01NSaTxbHVv9KnQq8vFjIphoqKa6Dj09r7neNgVqhq-7YqkU_Wyok9cevdck1C0EkEBMKULuec5VobTn9s55iwqRmQhkm43yU_XjBxtoWz-FoaQE8Vhdz6lAsUK0LZAnRPN9DeMEtn9lO2U8iqWwz6vYhbGUxN_1BDpAwJEPZDx4b7rDOT7F45D0MbTpLZHrHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفندهای هوشمندانه برای ساده‌تر کردن کارهای روزمره
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/675983" target="_blank">📅 11:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675982">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
اژه‌ای: حقوق مردم در شرایط جنگی هم نباید نقض شود
رئیس قوه قضاییه:
🔹
حتی در وضعیت جنگی نیز حفظ حقوق مردم و ممنوعیت هرگونه تجسس غیرقانونی باید به‌طور کامل رعایت شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/675982" target="_blank">📅 11:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675981">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKFOT6GEY9LsDUmcyTcOICEpwdbDjcptWm_lqCJTiZiIaOk9KLRKOFUfCZLbTkqVuiypiCAb5SPyzbt8VgZH3R2Xs4CMO_oaHdpYvrObDCboraTsN0AMPCMQZNMBnKto7Uc6AAooIk4CZ4J4X5dWDs3IhP9q_MfDeG4aqee18-hDudTRhV-PpcI2NEOzs7rXFrA2G0a74zQb6nNakuobbOlQVQ3nWksE9LzlxACZ3Z_pQmtWuZ6C4MWSUSHv8aA7VHU8OMm2JaLHYVolv5u11kzxL_QEQzUbDNHWzZnq8Y-o4YOzI1KoIi_Kj21GKt1mxK_yJZlb6ZfER3qSUYanyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
۱۰۰۱ سفر کربلا
✨
▫️
همین حالا با ارسال عدد ۲ به ۳۰۰۰۱۱۵۲ در پویش «زیارت به نیابت» ثبت‌نام کنید و شانس خود را برای ۱۰۰۱ سفر کربلا امتحان کنید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/675981" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675980">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88bbba788.mp4?token=fPE7JZBqcm-A02eq7tz3GoPBRhL_vmyCQH0nXMNV_gcK2LhvVZJ9jhjplMo8XPUz_jc9OnPTxUmanFcb5ywKs63Xllnbu7nXV-60bZWWMmw6m-cA0hQTjE_ahqiahOH5XRRk06GjxJy8oJCKh4TJJVI34sOoUgd5D2bKa6aIvse_6o97eoR8Nt_EaLGJ2oif-7j0-qhpBAc37PHS2uk9HK9N_u3GW4Eh7uaQn442s6m1L4P7SeRia11K3IvYpP3sScjER6qXyngvlC9WivWfqdL9V1vZ7ka1NPWjF8i4_DPZYtB1rC29FZef6ugYGHfU8qyxMWoEJ_nydXxpVPB1Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88bbba788.mp4?token=fPE7JZBqcm-A02eq7tz3GoPBRhL_vmyCQH0nXMNV_gcK2LhvVZJ9jhjplMo8XPUz_jc9OnPTxUmanFcb5ywKs63Xllnbu7nXV-60bZWWMmw6m-cA0hQTjE_ahqiahOH5XRRk06GjxJy8oJCKh4TJJVI34sOoUgd5D2bKa6aIvse_6o97eoR8Nt_EaLGJ2oif-7j0-qhpBAc37PHS2uk9HK9N_u3GW4Eh7uaQn442s6m1L4P7SeRia11K3IvYpP3sScjER6qXyngvlC9WivWfqdL9V1vZ7ka1NPWjF8i4_DPZYtB1rC29FZef6ugYGHfU8qyxMWoEJ_nydXxpVPB1Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهاجرانی: تصمیم دولت درباره بنزین جمع‌بندی نشده است/نتیجه نهایی به مردم اطلاع‌رسانی خواهد شد  سخنگوی دولت:
🔹
دولت حق ندارد منابع نسل‌های آینده را به آلودگی و بیماری تبدیل کند، برنامه اصلاح نظام توزیع و مصرف سوخت از قبل در دستور کار دولت قرار داشت.
🔹
در ایام…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/675980" target="_blank">📅 11:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675979">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
وقوع زلزله۷.۱ ریشتری در ژاپن
🔹
زمین لرزه ای به بزرگی ۷.۱ ریشتر جزیره کیوشو در ژاپن را لرزاند.
🔹
در این رابطه هشدار سونامی صادر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/675979" target="_blank">📅 11:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675978">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16c2169df5.mp4?token=feddCCmPQ7iqBjuMif1j5EOGLvGlJug6v17FXtJPyNcmBbCDz5vtHaTNmzdJFG1sSKlkdykfYZpaulSw_aZBx6JkXiokg0qKgfpxP97gMD5NrRE4NMWVlWX1a1s7Or-uPtYAJoREnQRTpOYKfFsFb-slDMSmA2UUQgMynawDF9iSLdgywzSTKpk6R0A3NNTugJaLidR-gf751-szwokuJIcpuDIxVzZ_15y-fyFtZN9ivzO52p36k1yeRposbz2eRjWerlv72mI1KbDcl45r9pjSZn6r9mAsh_ND3Gtk8KIyOQy4E8RXU_qKDHti9puxxpQMGtxFXEx6NqRZABFZwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16c2169df5.mp4?token=feddCCmPQ7iqBjuMif1j5EOGLvGlJug6v17FXtJPyNcmBbCDz5vtHaTNmzdJFG1sSKlkdykfYZpaulSw_aZBx6JkXiokg0qKgfpxP97gMD5NrRE4NMWVlWX1a1s7Or-uPtYAJoREnQRTpOYKfFsFb-slDMSmA2UUQgMynawDF9iSLdgywzSTKpk6R0A3NNTugJaLidR-gf751-szwokuJIcpuDIxVzZ_15y-fyFtZN9ivzO52p36k1yeRposbz2eRjWerlv72mI1KbDcl45r9pjSZn6r9mAsh_ND3Gtk8KIyOQy4E8RXU_qKDHti9puxxpQMGtxFXEx6NqRZABFZwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای کشته‌شدن یک زن در میدان علیخانی اصفهان کذب است
🔹
از ساعتی پیش، ادعاهایی در فضای مجازی از سوی برخی رسانه‌های معاند مطرح شده و عنوان شده شب گذشته خانمی با هویت معلوم در اطراف میدان علیخانی اصفهان کشته شده است.
🔹
براساس اعلام دادگستری استان اصفهان ادعای مورد اشاره کذب بوده و گزارشی مبنی بر کشته‌شدن زنی با هویت عنوان شده در محل مورد نظر واصل نشده است.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/675978" target="_blank">📅 11:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675977">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfiXGFMxIEUdXvLyB0ZZUHFh82Y6N6tVCVCHGXXq59v7G94-0ndh3ckuTLHQhwSTsSsXu2pm6G-IUZdB7_sTnK08r0kkHssJgxN31QcBK4WUIx91Ftq5w1nOyCm2lohxUtu28VDY7d14t-yGxh4v5wLzMferwwSn9zrSY5rWPm515MVhAG5mgZJv-gpxtZhLfWTlVJEf4xaWXPX9fjprqTBEqQJzWQwQTmpv2pXZ7JnpVgjKcsbs39DhmLkZ29JhPIE4BcuniWJPXnJVPzd5Gh6MJmcG8vER9sjkYxfDnyH3bqPlbU9EcvCd7wHRW3Fy5BSLLL_CHxco071R7o9eaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برق؛ عامل اصلی آتش‌سوزی خانه‌ها
🔹
بیش از ۴۰٪ آتش‌سوزی‌های ساختمان‌های مسکونی ناشی از مشکلات برقی مانند اتصال کوتاه، نوسان برق و سیم‌کشی‌هاست.
🔹
طرح «پلاک ایمن» امکان بازدید رایگان کارشناسان آتش‌نشانی از واحدهای مسکونی را فراهم کرده تا مخاطرات ایمنی ساختمان‌ها شناسایی و پیشگیری شوند.
@amarfact</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/675977" target="_blank">📅 11:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675976">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buheFm2qeDIQTPtyeqvuIKnkw60B4ibH7tws_nyg6x2auzMrSVJC4Vhh5L4yRgxtjD4go82g0ox2WccjKZGDousmF_jG9bEZKNqkp_OcH5zcWQF8zoDqOQmfnXd2MN8O-TYfQD0gDeB03KmWeA--Bzk7VRBhJlVlTAKN8Gfc4yibneKIO7noZjs-IySVgutBMF_ONoD8LAcwXt4-YKCUfi9OQiDKNBLk8SXglRpU4JAFiACe_VXcZAtWcsSilSWIcTUQc_v_lX4Q1tL8RoM3JuP8RAxfFX7jvcIoX6Dg-fYmc7dia6CWq-P-xfqzF2P2wEyqFSLxrHU984TIvDMEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا نشنال اینترست آمریکا را «بازنده» درگیری می‌داند؟
🔹
داشتن قوی‌ترین ارتش جهان روی کاغذ، لزوماً به معنای پیروزی در میدان نیست.
🔹
بر اساس این گزارش، ترامپ در رسیدن به اهداف خود ناکام مانده و توان بازدارندگی تهران همچنان پابرجاست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/675976" target="_blank">📅 11:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675975">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
عرضه مرحله‌ای بلیت پروازهای اربعین
🔹
سازمان هواپیمایی کشوری اعلام کرد عرضه بلیت پروازهای ویژه اربعین همزمان با صدور تدریجی مجوزهای عملیاتی شرکت‌های هواپیمایی و بارگذاری برنامه پروازی در سامانه‌های فروش انجام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/675975" target="_blank">📅 11:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675973">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعایی عجیب؛ صدور شناسه برای کالاهای تقلبی
سید احمد حسینی، رئیس اتحادیه لوازم یدکی خودرو در
#گفتگو
با خبرفوری:
🔹
اجرای نادرست قانون مبارزه با قاچاق کالا و ارز و صدور شناسه برای برخی کالاهای تقلبی، زمینه عرضه لوازم یدکی تقلبی را در بازار فراهم کرده و کالاهای اصلی نیز توان رقابت با کالاهای تقلبی را از دست داده‌اند.
🔹
افزایش شدید قیمت خودرو و هزینه‌های نگهداری آن نیز باعث شده بسیاری از مردم به سمت خرید قطعات و کالاهای ارزان‌قیمت و تقلبی بروند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/675973" target="_blank">📅 11:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675972">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
سخنگوی دولت: سهمیه بنزین ۳ هزار تومانی از ۱۰۰ لیتر به ۵۰ لیتر کاهش پیدا کرده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/675972" target="_blank">📅 10:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675971">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
سخنگوی دولت: فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است/ در این ایام ۳۵۰ نفر از کارکنان دولت به شهادت رسیدند  فاطمه مهاجرانی:
🔹
فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است و هواپیمای نویی که به تازگی خریداری شده بود مورد اصابت موشک دشمن قرار گرفت…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/675971" target="_blank">📅 10:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675969">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoF06wrR_DKPTK6jGwL1AuFeewOwv6t1y-H8haO_j1eqqV32Um7hO9iwEiB_LrEL1sAyemv5BM8kitQWJQLLuj7izZldVtoDE4cX7_SH9Eh93NNKS_4VeGOTdREyVTTAjFYrTXO3vzSRU48fBKbsLsI83bmDCTWcWBmGIFq6z7wgXfCYBChrand2GJ2M0larIFkzE6rrRw7K61Cwdr8wLlxVLVOwiy2mI-j8mH46IfRKQIBf3h2-yXIOaeKaDykRTBi0eUXdMqX367Hve_sMe-yatFWQM3IrB5ATXa-jS9WYU78QewM1R-1NeKFzw22bbFQ29x0JDQqFyZ5zj41afQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ebc664648.mp4?token=IpKBjpmDXlb64U9QCHa0KPRfv-a22-KSjXz5_Jtng1gMe7zMGSqbXP7o6NROYv8B_i3terqepBjXHGGhadRHjOvsHonhp0GukhgMsOWmfJpqZg6mB_hkVPB8D9LULVuCbEOta599M_igWpI0XN1Ilvw08oliZ6c0PPIepqEX4u3iQhBrO0Pir264ay9bSCy_8DE-W7WLZVzKo0U2ZKb43-LVGUiYBHNo0N6MsGYdb-RDnG3sI7bl14qMuXau9QQ4rnsso4X3QY_-qjg3i0kOvsJyr0bi73iiCNDO2cqYtOkEoFYwEuGcSod1xe6utTaoQrPowuCZESz1zR4Ub0zYUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ebc664648.mp4?token=IpKBjpmDXlb64U9QCHa0KPRfv-a22-KSjXz5_Jtng1gMe7zMGSqbXP7o6NROYv8B_i3terqepBjXHGGhadRHjOvsHonhp0GukhgMsOWmfJpqZg6mB_hkVPB8D9LULVuCbEOta599M_igWpI0XN1Ilvw08oliZ6c0PPIepqEX4u3iQhBrO0Pir264ay9bSCy_8DE-W7WLZVzKo0U2ZKb43-LVGUiYBHNo0N6MsGYdb-RDnG3sI7bl14qMuXau9QQ4rnsso4X3QY_-qjg3i0kOvsJyr0bi73iiCNDO2cqYtOkEoFYwEuGcSod1xe6utTaoQrPowuCZESz1zR4Ub0zYUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طعنه گرین به کاخ سفید؛ مردم آمریکا نان می‌خواهند، نه انیمیشن
🔹
مارجری تیلور گرین، نماینده سابق کنگره آمریکا، با بازنشر انیمیشنی که حساب رسمی کاخ سفید درباره دستگیری آدم‌فضایی‌ها در دولت ترامپ منتشر کرده بود، نوشت: مردم توانایی خرید بنزین، مواد غذایی، پرداخت اجاره خانه و تأمین هزینه‌های مراقبت‌های بهداشتی را ندارند و این مزخرفات عجیب و شرم‌آوری است که حساب رسمی کاخ سفید منتشر می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/675969" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675968">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
سخنگوی دولت: فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است/ در این ایام ۳۵۰ نفر از کارکنان دولت به شهادت رسیدند
فاطمه مهاجرانی:
🔹
فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است و هواپیمای نویی که به تازگی خریداری شده بود مورد اصابت موشک دشمن قرار گرفت و تنها قسمتی از دم آن باقی مانده است.
🔹
در این ایام ۳۵۰ نفر از کارکنان دولت به شهادت رسیدند.
🔹
برج مراقبت دریایی چابهار با اصابت ۱۱ موشک فرو ریخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/675968" target="_blank">📅 10:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675967">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/be688382c3.mp4?token=Owg5lI5iOpk4S0wgcZKxXSveXHPTWD5EwD42jF5oi6t_ffT7vAx04T1Qs3MAu_CFHQGK1pcxQgF-31WujR1oOrWUswnTWh3yGLhclCfcD0NRHDM7BjKtVjK6x-YMszi5C_JDWPIhB2LJG_XZmTcVKeVhOJ7cz73KgH9KCrCXnOscFYImgNSwYLNdYcTuEKXZTYARtLzLAddb-inYRV6aNbMUP9VoeLqOE5E2KzqiONj_c4_4ciJejlpVOklOSqIgoH14s4kLJ409HNOwGUvfAr_uKzWJ_egTXl5EJKwb9BECTAJRyLZYHYso3J4H2fdCyb1tltWpHgZZlYMG3jVhHg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/be688382c3.mp4?token=Owg5lI5iOpk4S0wgcZKxXSveXHPTWD5EwD42jF5oi6t_ffT7vAx04T1Qs3MAu_CFHQGK1pcxQgF-31WujR1oOrWUswnTWh3yGLhclCfcD0NRHDM7BjKtVjK6x-YMszi5C_JDWPIhB2LJG_XZmTcVKeVhOJ7cz73KgH9KCrCXnOscFYImgNSwYLNdYcTuEKXZTYARtLzLAddb-inYRV6aNbMUP9VoeLqOE5E2KzqiONj_c4_4ciJejlpVOklOSqIgoH14s4kLJ409HNOwGUvfAr_uKzWJ_egTXl5EJKwb9BECTAJRyLZYHYso3J4H2fdCyb1tltWpHgZZlYMG3jVhHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عارف: اهل جنگ نیستیم اما اگر جنگی به ما تحمیل شود خیلی خوب دفاع می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/675967" target="_blank">📅 10:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675966">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
فردا ادارات کرمانشاه تعطیل شد
🔹
ادارات و بانک‌های استان کرمانشاه، فردا چهارشنبه  به دلیل گرمای هوا و ضرورت مدیریت مصرف انرژی، تعطیل است./ایسنا
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/675966" target="_blank">📅 10:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675965">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dca2821921.mp4?token=W2oyY_lN8iczLWMGJdEos37wLECkfAw7jZ2fgTA4paELEHrtyL_p5Q1gED-fYNfOWRdwsPW2Mc6ypKiGSj2A3g7dcmwgggs4dI7NxrRkHAlRWn3VGDkhjFnw7SR8FN3my7R-rHtWm9E9gSb_qVijYTBGceaFLN3SmByo52UGN1DXF9qqhDY7X0gOvDUIaMQHeHQ07hlZQY68p7LGdcXv7z0Bz5M_WEGEINxWgKeTPw8r6wkftmf65BeJ4vEnfYWuFjOmGSHBnVMCTILOHpOCHLlvXrviKa5q9MX9ounRz32BVRORtsZWDKST6PXz0t-jlV4K1QmyYrEQDtiX5EcVpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dca2821921.mp4?token=W2oyY_lN8iczLWMGJdEos37wLECkfAw7jZ2fgTA4paELEHrtyL_p5Q1gED-fYNfOWRdwsPW2Mc6ypKiGSj2A3g7dcmwgggs4dI7NxrRkHAlRWn3VGDkhjFnw7SR8FN3my7R-rHtWm9E9gSb_qVijYTBGceaFLN3SmByo52UGN1DXF9qqhDY7X0gOvDUIaMQHeHQ07hlZQY68p7LGdcXv7z0Bz5M_WEGEINxWgKeTPw8r6wkftmf65BeJ4vEnfYWuFjOmGSHBnVMCTILOHpOCHLlvXrviKa5q9MX9ounRz32BVRORtsZWDKST6PXz0t-jlV4K1QmyYrEQDtiX5EcVpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ قلاده خرس قهوه‌ای در ارتفاعات جنگل‌های هیرکانی لنگرود مقابل دوربین‌ها ظاهر شدند
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/675965" target="_blank">📅 10:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675961">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2185a55d9.mp4?token=MoVdaWp2DzWS-dlx-5wxXkJaPNtrV45IFfLLJkSJLm0XSOfY4dbS02IIWjw-yoO9s-11TeC0L7Cbtophw4wsQu0q_aPV1RswYxIcBRDH5rnPijYBg5uuYE4iC23Dwn5BnHyf3b-tl42Ab-Jysz5JB0On-6iDhK8Eeh3BI4Aw9sDnX0XeK6ypxqAu2u6XfbJHbGhROc2nPa0hLBwgH6ybpE2R-8FGQMGMdDzOiK81Xc17TrfQslNEMWAxhoJwNreyMGXtS7gd4Lg_8onPyBkHz8TCc7xN_lylVt9igsJxiCtDsxXxZEwX3k_uwXJ69s_7gSRaUVeh4FoHCI3rXgFpmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2185a55d9.mp4?token=MoVdaWp2DzWS-dlx-5wxXkJaPNtrV45IFfLLJkSJLm0XSOfY4dbS02IIWjw-yoO9s-11TeC0L7Cbtophw4wsQu0q_aPV1RswYxIcBRDH5rnPijYBg5uuYE4iC23Dwn5BnHyf3b-tl42Ab-Jysz5JB0On-6iDhK8Eeh3BI4Aw9sDnX0XeK6ypxqAu2u6XfbJHbGhROc2nPa0hLBwgH6ybpE2R-8FGQMGMdDzOiK81Xc17TrfQslNEMWAxhoJwNreyMGXtS7gd4Lg_8onPyBkHz8TCc7xN_lylVt9igsJxiCtDsxXxZEwX3k_uwXJ69s_7gSRaUVeh4FoHCI3rXgFpmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاستا آلفردو رو با این روش درست کن ببین چی می‌شه
😍
مواد لازم:
🔹
پاستا یک بسته
🔹
سینه مرغ یک عدد
🔹
قارچ به تعداد دلخواه‌تون
🔹
خامه نصف بسته
🔹
شیر یک لیوان
🔹
سیر ۱ یا ۲ حبه
🔹
کره یا روغن مقدار لازم
🔹
نمک و فلفل سیاه به مقدار لازم  #آشپزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/675961" target="_blank">📅 10:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675960">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a0a93054.mp4?token=q3bea-qD2-rp7Q_y1jcHOWWb7s4WGey74LvaX--8mUTXxqR2cjpplpMLl9IUzDIpTOgw5tIPUuz1AdddUny_ZQzIVJSa8kEcDwrUFKGG3dhroMfe7dnnjHdIuRwH9u7w6IaZ5uDNbQVgicHPEl46hN_eO8SoXkUBpTn_KYCwB9z1X8lZxPFiFrUtqJ5o9oULigSuWsTs2Y4XqQgI62bVgoNE4xkfGIjBe75RUOeybHemN8Pp0ffNu8_0HhUVcZvBFCjVJMOubwjHh2xwthkrkpmrofDvBmvUQLvv5EGfBKRONGCk7kWzjJ3f6xgV8ZBrF7k56ojYm8bWZg6eGJXUZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a0a93054.mp4?token=q3bea-qD2-rp7Q_y1jcHOWWb7s4WGey74LvaX--8mUTXxqR2cjpplpMLl9IUzDIpTOgw5tIPUuz1AdddUny_ZQzIVJSa8kEcDwrUFKGG3dhroMfe7dnnjHdIuRwH9u7w6IaZ5uDNbQVgicHPEl46hN_eO8SoXkUBpTn_KYCwB9z1X8lZxPFiFrUtqJ5o9oULigSuWsTs2Y4XqQgI62bVgoNE4xkfGIjBe75RUOeybHemN8Pp0ffNu8_0HhUVcZvBFCjVJMOubwjHh2xwthkrkpmrofDvBmvUQLvv5EGfBKRONGCk7kWzjJ3f6xgV8ZBrF7k56ojYm8bWZg6eGJXUZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخازن ذخیره‌سازی گاز عربستان هم منفجر شده است
🔹
نیروهای مسلح یمن دیروز تاسیسات بقیق را با پهپاد هدف قرار دادند. سعودی‌ها مدعی بودند که پهپادها را رهگیری‌ کرده‌اند اما چند ساعت بعد فعالیت بزرگ‌ترین مجتمع فرآوری نفت خود در این تاسیسات را متوقف کردند.
🔹
حالا این تصاویر نشان می‌دهد، سعودی‌ها روی دو مخزن ذخیره‌سازی گاز، پوشش‌های خنک‌کننده سفید و سیاه نصب کرده‌اند تا از گسترش آتش یا انتقال حرارت به سایر مخازن جلوگیری کنند./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/675960" target="_blank">📅 09:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675956">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
صدور آنی کارت سوخت به کجا رسید؟
🔹
متقاضیان می‌توانند با مراجعه به سامانه درخواست خود را به‌صورت کاملاً الکترونیکی ثبت کنند، رمز کارت را از طریق پیامک دریافت کرده و گزینه دریافت حضوری کارت را انتخاب کنند.
🔹
زمان صدور کارت از حدود یک ماه در روش قدیمی به یک روز کاهش یافته است. امکان ثبت غیرحضوری درخواست، پیگیری الکترونیکی مراحل صدور و تحویل حضوری فوری کارت، بدون نیاز به ارسال پستی، فراهم شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/675956" target="_blank">📅 09:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675954">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26251840a6.mp4?token=K_bF--DQtwUkaCdxXnGscNOFni-GwYkTnAf1I4bY5pUFGhUOD-spzTByMCxU5-mTLPnClQyU4RLp57Lhfp4aq65vkQwPWtBD3jDbGeigw4q5Wi0z3K4grm0xrIOR76dror8zuNJvi6eQlX8gTre7ifj10B43qKgkh_cxyehpT7CAPQHnkxESJ0FtrQlwBkYuz2_XEju-vmkvf2ls-EzCjULjPQ64gKGqzho8Se0NKSSkuCJ1AQC8NvxtZAjEomoh7AWmbD6zFQh0BsJwQln6gXzM8YLE32yVzbCg5NmPDZ1xKw_v4uFMtFqB0k3OqMUCqkUk7X9wcDz_TNn84NgATw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26251840a6.mp4?token=K_bF--DQtwUkaCdxXnGscNOFni-GwYkTnAf1I4bY5pUFGhUOD-spzTByMCxU5-mTLPnClQyU4RLp57Lhfp4aq65vkQwPWtBD3jDbGeigw4q5Wi0z3K4grm0xrIOR76dror8zuNJvi6eQlX8gTre7ifj10B43qKgkh_cxyehpT7CAPQHnkxESJ0FtrQlwBkYuz2_XEju-vmkvf2ls-EzCjULjPQ64gKGqzho8Se0NKSSkuCJ1AQC8NvxtZAjEomoh7AWmbD6zFQh0BsJwQln6gXzM8YLE32yVzbCg5NmPDZ1xKw_v4uFMtFqB0k3OqMUCqkUk7X9wcDz_TNn84NgATw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با دوتا متریال ساده، یک آباژور مینیمال جذاب درست کن
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/675954" target="_blank">📅 09:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675952">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6f327b73b.mp4?token=GFZIlwIg4KQje3CqW3r6M3vC8kH-P_miOJdnt70DktZSPVqq6Cgqyb10RDSOn53tFDtlcd0pidRc9Ar0j8JC24d2iER4ZGcJ2D5iMi55pq-QyorKPESHJ0JiSTG2stMooPjt284IP4UYVn-dUjHb6wFUaKiHAiY-9SZyp_mq0k0TRj2d5Ux_pYH7JNMAfMLh4Im_2WBGgqCbvFuSnA2558UmHjBQUOQRNjDOfdqFm0fPvNAeijO03DD97fdCNqzbteFAGJqSD92pU_q-GV41Pyx8wRlQHNYlpB1ITkQat5oKYFZKhyvRUSdmANSqL5TDRvkyKzEQGHs7wCLOwHrlI3LG1QHVmPqBbAG1jVcklAYd_duSwNxsUsmWv8ImINIxJOPpkT55NbrEMSjTIXNsZOlSt5K1Iwg5HpkESW6UrkRaP8rllCGwXtGiVne1Mk-SuqXH49fSPpRQz_qIa3unpZqftqP-Qf30-LwF-4AvmXDEL5lHlmhaV2-rpQiDjw2zkcYXrEPXZEoKSU6zALLkpQTQokLZthOy59JR2Ng4dJbrNH9jw42qGS_XY_40tUEbnRPrDjfImLi-jx7bzs-8hWBcYctITTaPm27j8wO2keXDO-HZNdckwiXk_Pdgzlxr1nvqYxOypU_I148zNkJHC_s1Ijo-AfPxT-tZDWjZbfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6f327b73b.mp4?token=GFZIlwIg4KQje3CqW3r6M3vC8kH-P_miOJdnt70DktZSPVqq6Cgqyb10RDSOn53tFDtlcd0pidRc9Ar0j8JC24d2iER4ZGcJ2D5iMi55pq-QyorKPESHJ0JiSTG2stMooPjt284IP4UYVn-dUjHb6wFUaKiHAiY-9SZyp_mq0k0TRj2d5Ux_pYH7JNMAfMLh4Im_2WBGgqCbvFuSnA2558UmHjBQUOQRNjDOfdqFm0fPvNAeijO03DD97fdCNqzbteFAGJqSD92pU_q-GV41Pyx8wRlQHNYlpB1ITkQat5oKYFZKhyvRUSdmANSqL5TDRvkyKzEQGHs7wCLOwHrlI3LG1QHVmPqBbAG1jVcklAYd_duSwNxsUsmWv8ImINIxJOPpkT55NbrEMSjTIXNsZOlSt5K1Iwg5HpkESW6UrkRaP8rllCGwXtGiVne1Mk-SuqXH49fSPpRQz_qIa3unpZqftqP-Qf30-LwF-4AvmXDEL5lHlmhaV2-rpQiDjw2zkcYXrEPXZEoKSU6zALLkpQTQokLZthOy59JR2Ng4dJbrNH9jw42qGS_XY_40tUEbnRPrDjfImLi-jx7bzs-8hWBcYctITTaPm27j8wO2keXDO-HZNdckwiXk_Pdgzlxr1nvqYxOypU_I148zNkJHC_s1Ijo-AfPxT-tZDWjZbfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقایسه‌ فرود اسپیس‌ایکس استارشیپ بین پروازهای ۱۲ و ۱۳
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/675952" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675946">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
حکم اعدام ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی دو تن از عوامل جنایت فجیع میدان شهید علیخانی اصفهان در کودتای دی‌ماه سال گذشته اجرا شد/ میزان  #اخبار_اصفهان در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/675946" target="_blank">📅 08:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675945">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/382e9450a5.mp4?token=k5s5oETII_Wm1I3PjoUqD7vQvmTrfRXjSRqA6p7pacsvPU8kogI1lyLyZ7Z4D1KfnYt2lGErkJN_ONPxTGPa7OzR0RMna-u16Kv_kcLBP0BE_JekketQ33agQeQ1iKisCphJQkof4GnW0x55RBKSAbGScNaYZ-dkAuZg9ADTGUbluTzbUIH7ROcQztSHgixNsVJEGMBvNt_hjZl43_TpCwGKM4oNa0nwI17QlUJrF31i-pA-sxIyG9Ogpb-5NbN6dlefPaKUSIeUv716X08ORaeddKquwu1te-Kj4wwejeKWRUJv6d_j-G41QjhZNxMiufmcD6YRupRDwiUw8mw6iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/382e9450a5.mp4?token=k5s5oETII_Wm1I3PjoUqD7vQvmTrfRXjSRqA6p7pacsvPU8kogI1lyLyZ7Z4D1KfnYt2lGErkJN_ONPxTGPa7OzR0RMna-u16Kv_kcLBP0BE_JekketQ33agQeQ1iKisCphJQkof4GnW0x55RBKSAbGScNaYZ-dkAuZg9ADTGUbluTzbUIH7ROcQztSHgixNsVJEGMBvNt_hjZl43_TpCwGKM4oNa0nwI17QlUJrF31i-pA-sxIyG9Ogpb-5NbN6dlefPaKUSIeUv716X08ORaeddKquwu1te-Kj4wwejeKWRUJv6d_j-G41QjhZNxMiufmcD6YRupRDwiUw8mw6iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زانو درد رو تحمل نکن
🦵
🔹
گاهی با چند تغییر ساده و انجام تمرینات صحیح، می‌شه فشار روی زانو رو کم کرد و درد رو تا حد زیادی کاهش داد #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/675945" target="_blank">📅 08:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675943">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaEOB7vRsoRP6w-wz-cOpV61FAMno6d5vgye-l1T5efWUVVDDsD9EuFpjzCWPtGJGJVzYC1QnbCd6aoSxW-SbNoEEQxk6LayY9YU_mtvpCfrBuH_GF77nQ8ID77gW_Vgh9FoMr9cInRYjTt6MrJbjBqXwBWx8dajMiQkejESqfkrKLToAEuYd9yrsz1Hq54xz3Tof7xTEqCNceYyZdmTtLOCKg_p8NU56zHhCLFHLXnBKWnryeoeQsUF6grBFMWjjtahgwBYfOAu3gqyxhAhTr_gQ5RoIH5kKNE8RxH-7Z4PAiyQo3cKaKbCW2nimKxLVca6qSqPBBvuLag_cY9UgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۶ مرداد ماه
۱۳ صفر ‌۱۴۴۸
۲۸ جولای ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/675943" target="_blank">📅 07:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675941">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
مدارس از مهر حضوری هستند
وزیر آموزش‌وپرورش:
🔹
تلاش ما این است که تمام مدارس کشور سال تحصیلی جدید را به‌صورت حضوری و با کمترین دغدغه و مشکل آغاز کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/akhbarefori/675941" target="_blank">📅 06:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675938">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
حکم اعدام ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی دو تن از عوامل جنایت فجیع میدان شهید علیخانی اصفهان در کودتای دی‌ماه سال گذشته اجرا شد/ میزان
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/akhbarefori/675938" target="_blank">📅 05:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675936">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czo0vE-CeWlggnZ67Lv3CtMoZmnOqNuVVWu_RhY6ABy80vo4i3KFBSfwVr8xhurVSescAg53lXs9m2F92_82X1v1Fix0JkPWajUcKPETQy3nPctUPo3UXVr7eBIF3Dsmu8ccwJaOZdT29-jHJdASpi72DuCgcEoNwkSVzw_An5g8FmJZLJ2QwvXz1AcPkkd7D2g4tvsX6xVbzNaZoXlHm-dPXjGCd8t2KBa9Ox05vIr8Jgctfm7ldA1aPFuM7s2739yYUeMgBXO6GwCi6vjPpTk3rJECyDyWF1XrE3gvpLnjSe8Yl37fBDelKFhxFmG4ME7fyv2MCh-fX3LKg2BCbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز حساس واشنگتن؛ از موجودی موشک‌های آمریکا چقدر باقی مانده است؟
🔹
وال‌استریت ژورنال در گزارشی به بررسی وضعیت حساس موجودی موشک‌های آمریکا پس از حدود پنج ماه درگیری در جنگ با ایران پرداخته است. این گزارش که روز گذشته منتشر شده، بر نگرانی‌های داخلی دولت…</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/akhbarefori/675936" target="_blank">📅 04:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675933">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
بزرگ‌ترین تأسیسات پالایشی عربستان از کار افتاد
🔹
شرکت آرامکوی عربستان پس از حملات پهپادی یمن، فعالیت بزرگ‌ترین مجتمع فرآوری نفت خود در بقیق را متوقف کرد.
🔹
ساعاتی پیش یمن اعلام کرد که با پهپاد خط لولۀ انتقال نفت از شرق عربستان یعنی همان خط لو‌له‌ای نفت را بدون تنگۀ هرمز به بندر ینبع در دریای سرخ می‌رساند، هدف قرار داده است.
🔹
حالا شرکت آرامکوی تمامی فعالیت خود در این تاسیسات را متوقف و در چندین سایت تولید نفت، عملیات مشعل‌سوزی اضطراری را آغاز کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/akhbarefori/675933" target="_blank">📅 02:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675932">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7j7Gj3ZO124eubdh0utRnBAUKL1mf6vB3-oUM1BClUYI7tnKip1YR7OYa43T_EyBIOrG8LLVvNEVtPIAtrGJjO67B3UJznvpcdQ-WSVeow9hxeTh39pkz4ftuF0S-VVnlin0sIclFgCMMdNAVD3MNPJHQD5O9raxwnKjnIBLc4GVeFWqHPILxKN_j25j7lp8UtAgJfddUwlrKYIhLQof6hhpJfgCVrZBoc5Ah85rd--GJMB69fmcMIOQ21WaY65LUiUlWjC7mlIr7KjlpePS13SL3y20u4-xOGiE1KPdLapavwa24BOG9_Hjy3cBQba6tg5l4_1eITIwb_HFWN7HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز حساس واشنگتن؛ از موجودی موشک‌های آمریکا چقدر باقی مانده است؟
🔹
وال‌استریت ژورنال در گزارشی به بررسی وضعیت حساس موجودی موشک‌های آمریکا پس از حدود پنج ماه درگیری در جنگ با ایران پرداخته است. این گزارش که روز گذشته منتشر شده، بر نگرانی‌های داخلی دولت آمریکا در مورد کاهش شدید ذخایر مهمات دقیق، به‌ویژه موشک‌های تهاجمی و پدافندی تمرکز دارد.
🔹
طبق تحلیل‌های مرکز مطالعات استراتژیک و بین‌المللی (CSIS)، ذخایر برخی از این موشک‌ها به شدت کاهش یافته: مثلاً حدود ۳۰٪ تاماهاوک‌ها، نزدیک به نیمی از Patriot و THAAD، و بخش قابل توجهی از JASSM کاهش یافته است. بازسازی کامل این ذخایر ممکن است ۳ تا ۶ سال طول بکشد، حتی با افزایش تولید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/akhbarefori/675932" target="_blank">📅 02:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675930">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2952ea4a.mp4?token=jRRVHdjLYgPqAGC4JLx2pFvzaoiEIb-oGJJMCuexiIesaDwonu-iR3s6AQ0GJi3YYuZG5t85YIhHmo15viJ93uN49ZE6YPUEKzdq9PZiaD8IYKZKcyE_5L4FoP0HsYCV9OXLkNRAKTfxWHtJ4Cm3rzKp4XKwzA5Wzn8yh2tohfOxNHxOCnr6Xme8XVIxuTTICXkL1OlMA4SHc4bMH-ciKAVZrlQ0kn6zzSb-Pck1CVTkdewNW4jhGmybMVf-ptTz99mp1oyureu_GCD_AYkpMA6_AjGM6Kfsjjp9EUQL45QqbR-rXpn-Z8Q0t6zq_Lh8UuYjXLYl2NdLJcdHLTGckQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2952ea4a.mp4?token=jRRVHdjLYgPqAGC4JLx2pFvzaoiEIb-oGJJMCuexiIesaDwonu-iR3s6AQ0GJi3YYuZG5t85YIhHmo15viJ93uN49ZE6YPUEKzdq9PZiaD8IYKZKcyE_5L4FoP0HsYCV9OXLkNRAKTfxWHtJ4Cm3rzKp4XKwzA5Wzn8yh2tohfOxNHxOCnr6Xme8XVIxuTTICXkL1OlMA4SHc4bMH-ciKAVZrlQ0kn6zzSb-Pck1CVTkdewNW4jhGmybMVf-ptTz99mp1oyureu_GCD_AYkpMA6_AjGM6Kfsjjp9EUQL45QqbR-rXpn-Z8Q0t6zq_Lh8UuYjXLYl2NdLJcdHLTGckQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو نخست وزیر رژيم صهیونیستی وارد واشنگتن شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/akhbarefori/675930" target="_blank">📅 01:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675925">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05b88909c6.mp4?token=p3BWW9Dov5L33xEIrPgj-lJtqpiakpLlKhIchFzxj7Mt6-qC5vIyuaS9oN_ciMPV3v25qi4YUI3UbPOB-uQWYjraaIO5Mt-0GsFkwJXnvsUWA7ytzDmeFzN67hEWHrKX2tItM2GXgHHSxVg9V3l9M2Sdr30j6CEKE4Ke2nHqokkOl3isc8uSfLdKi8CWF-sCyhRmASDqIH7niZ3FmXPBtAh4WSN9ovi0AUDHI-_Ruzl60oz0y9xfkzu-CJ3MFppZsk_l-d9D84DgdyF6caMllEzc_0aM1GZMSDLpgff6fCyc9qBBIYTamnPkYUGfleRVDIEmacecoPZ4aT24H8a2_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05b88909c6.mp4?token=p3BWW9Dov5L33xEIrPgj-lJtqpiakpLlKhIchFzxj7Mt6-qC5vIyuaS9oN_ciMPV3v25qi4YUI3UbPOB-uQWYjraaIO5Mt-0GsFkwJXnvsUWA7ytzDmeFzN67hEWHrKX2tItM2GXgHHSxVg9V3l9M2Sdr30j6CEKE4Ke2nHqokkOl3isc8uSfLdKi8CWF-sCyhRmASDqIH7niZ3FmXPBtAh4WSN9ovi0AUDHI-_Ruzl60oz0y9xfkzu-CJ3MFppZsk_l-d9D84DgdyF6caMllEzc_0aM1GZMSDLpgff6fCyc9qBBIYTamnPkYUGfleRVDIEmacecoPZ4aT24H8a2_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از انفجار و آتش‌سوزی در مخفیگاه‌های جدایی‌طلبان تروریست ضدایرانی در أربیل عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/akhbarefori/675925" target="_blank">📅 01:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675924">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
گزارش‌ها حاکی از آن است که کنسولگری آمریکا در أربیل
هدف قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/akhbarefori/675924" target="_blank">📅 00:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675921">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a40bf5ed3.mp4?token=mU3CPxXyx93B2Vgu0AXkdCtgR1eUY7n8f0jqSOPGg3wOMDW6ALyr1dhAm1RhgWOef2YmXlS7CKVdHBYQ5H3b65Ub0n0PqpGyLM0NwuEeYy32hXMAuIjXTTTJmbbVK6vSVslszj_jFEUQcQNxyUF1-7--b1WOaPrFdoxKSa_d_BVKqVIHubRCOvzWGjtn0eWU5H9m-uHlOvul0Cl0hndfmLJTiwSXhxmtK1_UH4kYvyEs6ZGnJ2AixGSgbYCreGw5X2HWFoUOXyABT3ZhFa-svPevHFJYHRlL8ygCi_ZcgJCgdbAlUgSGA_BCJckB8_kfPUNlyyPd49i7pLiVZGfAbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a40bf5ed3.mp4?token=mU3CPxXyx93B2Vgu0AXkdCtgR1eUY7n8f0jqSOPGg3wOMDW6ALyr1dhAm1RhgWOef2YmXlS7CKVdHBYQ5H3b65Ub0n0PqpGyLM0NwuEeYy32hXMAuIjXTTTJmbbVK6vSVslszj_jFEUQcQNxyUF1-7--b1WOaPrFdoxKSa_d_BVKqVIHubRCOvzWGjtn0eWU5H9m-uHlOvul0Cl0hndfmLJTiwSXhxmtK1_UH4kYvyEs6ZGnJ2AixGSgbYCreGw5X2HWFoUOXyABT3ZhFa-svPevHFJYHRlL8ygCi_ZcgJCgdbAlUgSGA_BCJckB8_kfPUNlyyPd49i7pLiVZGfAbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات به تجزیه‌طلب‌های ضدایرانی در أربیل
رسانه عراقی:
🔹
تاسیسات راداری و مقرهای تروریستی در مناطق خلیفان و سوران در استان اربیل هدف قرار گرفتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/akhbarefori/675921" target="_blank">📅 00:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675917">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e4fd2715.mp4?token=gYW0WXLXVZ5A8buYUtn-kFvQP_peULaQT5f-NadHXUezLqnDEZzH6ITmzDkBwjudzFPpbNb23j-IPHXWHosVejqnRM6jKDDesiY6ybRNJtlVd3F2bSPdWgaOrS3SR0VCBXoi6lANNt3E8a20W9NV4j9RA4ht4TwOAOI03qxBlncVmic0SLwTEmGhlkjZSy9hFmnywKINOW-TA2wJ4qlBa2vsc3ATJaFuxWpuSbdGABiBFPnPZBgICXtRTt8PifNKcMAfocwAtBjx0tv9U9GMUTrNwpIS6ALsztq3Uxr6Xo2xFDK9AwehT25u5vGmLUo-MXBVL5L6dGOfoCnh07iRrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e4fd2715.mp4?token=gYW0WXLXVZ5A8buYUtn-kFvQP_peULaQT5f-NadHXUezLqnDEZzH6ITmzDkBwjudzFPpbNb23j-IPHXWHosVejqnRM6jKDDesiY6ybRNJtlVd3F2bSPdWgaOrS3SR0VCBXoi6lANNt3E8a20W9NV4j9RA4ht4TwOAOI03qxBlncVmic0SLwTEmGhlkjZSy9hFmnywKINOW-TA2wJ4qlBa2vsc3ATJaFuxWpuSbdGABiBFPnPZBgICXtRTt8PifNKcMAfocwAtBjx0tv9U9GMUTrNwpIS6ALsztq3Uxr6Xo2xFDK9AwehT25u5vGmLUo-MXBVL5L6dGOfoCnh07iRrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاجی بابایی: نباید در مورد NPT کاری کنیم که بهانه دست دنیا بدهیم
🔹
اگر حفظ نظام جمهوری اسلامی نیازمند حرکت جدیدی باشد مطمئن باشید مجوزش را خواهیم داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/akhbarefori/675917" target="_blank">📅 00:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675916">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/587a803682.mp4?token=ipLE_i9SpGjzlX9pQ_IMJVoGTnfQu2y2XkxfuZSQSku0RhYnbBfyRvfcpbJq2DKMYPnjFa8QGGg13jzT1tYa5mnzXNdvlYtzcqIFF00brjTuK3tgPBkimJQolzEc0vPN9q0Jn63qx9FRcu59mtx3gG3GawbvKrEJMKdCBYg9jYGCEd17ma3YlOH4L9sxJRskdO8NzpL3pe5Ct78IOq8PpXeqnSohdzTiiecMIaP-O576L1Kjgqi4oT7HtDllHgiyI2ZduyGhu2os1JMgCJtTiOrL0QX7TnQEUwcsb-v-h07TZgCOl5g8Lk3Z3KIGPl0RSs40OBH0scS5Mmz-T_1ZTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/587a803682.mp4?token=ipLE_i9SpGjzlX9pQ_IMJVoGTnfQu2y2XkxfuZSQSku0RhYnbBfyRvfcpbJq2DKMYPnjFa8QGGg13jzT1tYa5mnzXNdvlYtzcqIFF00brjTuK3tgPBkimJQolzEc0vPN9q0Jn63qx9FRcu59mtx3gG3GawbvKrEJMKdCBYg9jYGCEd17ma3YlOH4L9sxJRskdO8NzpL3pe5Ct78IOq8PpXeqnSohdzTiiecMIaP-O576L1Kjgqi4oT7HtDllHgiyI2ZduyGhu2os1JMgCJtTiOrL0QX7TnQEUwcsb-v-h07TZgCOl5g8Lk3Z3KIGPl0RSs40OBH0scS5Mmz-T_1ZTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیباترین گل جام‌جهانی به انتخاب فیفا
🔹
گل سیدنی لوپز کابرال، بازیکن کیپ‌ورد به آرژانتین در مرحله ۱/۱۶ نهایی، عنوان زیباترین گل جام جهانی ۲۰۲۶ را به خودش اختصاص داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/akhbarefori/675916" target="_blank">📅 00:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675915">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4dR7K84yk4kezEYOuIMtrXK-bdlKPf3jJy1rJbnXh6TbNAmeHvI_Cv53pNVuzdagoKB2f3s1ixdrkMsYk4-QF46h5Trk2FFQjyH-NXglyMTOraFZi6wMfNceiFecaGcS-IRrqgynPatRxuhzyR8bcQjR-Azmers6chLqt1dEJm2GRuy5UGZ_E8c6rBepCZ5zFVtqfBrmPgl2PGAIyvehw-XDlKJLSA801ZKJzmnGrZi1JqohCw5_nz0zRMq52qTgNK9pmzjBBaGyEN3UIL5yrwu5svIAVkdBafsZFgPxY_EWlxgqYLti69phSS72f157iCX9OV-Ur5gcSX244kSZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/675915" target="_blank">📅 00:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675911">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c19b8a98.mp4?token=H_wXjxao2VnGO9u9jGWsR_Z1qF49wNtGjcJvNXeHg9Q8GHkKCZvBBK_HiOCUF6pN6zCo84qhgMZHrg4AwPePw48m3iKROSxmCtA13q0QM2-C1v6laJDWMkh54elxfUKEgHkWw2nJSjiyZySafMFgy1j02ggykmyhAfY25DZMKWYLTZprRsHeVczGkkrvgKxa-SJ1qNY42uEJhHiOULSp2X5mXcvh7dTXsKSKvOpWqOL9ayDP4RK8rxB4cEEiW9iYFG7Ox7ehdA3buG7g3ueQdl6WwdoFDVeQe2zDBnODF1B10q53DYNymWwYwzgGst785s3NVFl262ZEczjyCRGO7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c19b8a98.mp4?token=H_wXjxao2VnGO9u9jGWsR_Z1qF49wNtGjcJvNXeHg9Q8GHkKCZvBBK_HiOCUF6pN6zCo84qhgMZHrg4AwPePw48m3iKROSxmCtA13q0QM2-C1v6laJDWMkh54elxfUKEgHkWw2nJSjiyZySafMFgy1j02ggykmyhAfY25DZMKWYLTZprRsHeVczGkkrvgKxa-SJ1qNY42uEJhHiOULSp2X5mXcvh7dTXsKSKvOpWqOL9ayDP4RK8rxB4cEEiW9iYFG7Ox7ehdA3buG7g3ueQdl6WwdoFDVeQe2zDBnODF1B10q53DYNymWwYwzgGst785s3NVFl262ZEczjyCRGO7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پهپادهای پلیس چینی «کلاه ایمنی» را زیر نظر می‌گیرند؛ تخلف کنی، هم هشدار می‌گیری هم امتیاز منفی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/akhbarefori/675911" target="_blank">📅 23:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675910">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQsPF2bN2ogJtjMGYbqCvtwiUsZpzuxpJQoWGmYCBdfLORsWitfGbsNNUnhgHkqXmcCGPxWkJxn3WZGB0HmXbAMG1QdxhV_TCJHKOJC46zni_xEaBMdnJYc69AJ_1-RhcUFs6mGwbOaA_RiVxrlTfWjbxDy9XRsZoDLnweqGoaAoYZk7lxpsn4VREwd4W8N7G6nj5mSFafst4C2h4QyNNSNWH3meEZ5hbeQuU-J35a9sWR-kkaFk45KIlbW_OJIll_fkrITK0Qy7B6KjpbiBc7LvXf5C4CMzfusALOMMCyESBUgP2kS4gROz_59QfL9vN3HXcIWyEZKOQf_TTq7z5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقاله ظریف در الجزیره: پنج دهه استراتژی پنهان اسرائیل برای سوق دادن آمریکا و ایران به سمت رویارویی دولت‌های متوالی اسرائیل تلاش‌های دیپلماتیک را تضعیف کرده و تنش‌ها بین واشنگتن و تهران را تشدید کرده‌اند
🔹
در حالی که بنیامین نتانیاهو، نخست وزیر اسرائیل، برای دیدار با دونالد ترامپ، رئیس جمهور آمریکا آماده می‌شود، دلیل خوبی وجود دارد که انتظار داشته باشیم او از این دیدار برای منصرف کردن هر اقدامی در جهت پایان دادن به خصومت‌ها در خلیج فارس استفاده کند. این انتظار ریشه در یک سابقه تاریخی دارد که بیش از پنج دهه را در بر می‌گیرد.
🔹
اطلاعات از طبقه‌بندی خارج شده، خاطرات مقامات ارشد آمریکایی، گزارش‌های تحقیقاتی و تحقیقات دانشگاهی، این ارزیابی را بیشتر تقویت می‌کنند. در مجموع، این منابع به یک الگوی تکرارشونده اشاره می‌کنند: دولت‌های متوالی اسرائیل، اغلب با حمایت عناصری در درون تشکیلات امنیتی این کشور، بارها تلاش کرده‌اند تا مانع تلاش‌ها برای پایان دادن به درگیری‌های منطقه‌ای یا تلاش‌ها برای مدیریت تنش بین ایالات متحده و ایران شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/akhbarefori/675910" target="_blank">📅 23:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675909">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔹
داغ‌ترین خبرها را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
ترامپ: در حال انجام مذاکرات عمیق با ایران هستیم
👇
khabarfoori.com/fa/tiny/news-3233599
🔹
۴ سناریو پیش روی جنگ ریاض و صنعا/ مهم ترین سلاح های یمن در جنگ با عربستان
👇
khabarfoori.com/fa/tiny/news-3233622
🔹
دوئل‌های توییتری قالیباف و ترامپ و الگوی جدید گفتمان دیپلماتیک - نظامی ایران
👇
khabarfoori.com/fa/tiny/news-3233428
🔹
نیما تکیدو؛ ستاره‌ای که رسانه‌های رسمی نمی‌شناسند اما میلیون‌ها دنبال‌کننده دارند
👇
khabarfoori.com/fa/tiny/news-3233431
🔹
پایان ۵۰ سال فرار؛ قاتل خواننده انقلابی به دام افتاد
👇
khabarfoori.com/fa/tiny/news-3233468
🔹
برای اطلاع از تازه‌ترین خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/akhbarefori/675909" target="_blank">📅 23:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675908">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d817e971db.mp4?token=rdLIFUFYTLushI6SWQ9JXHEzWcADYrKydTSMC8uDqZaPMB7YUnROiFeT83I7yiVoO3U7krLF4O7265WIjG9J12W2jSaRG1HbWyDnxNXMjSAc_Wf0ZvHfmar7sCtFnjwZJ6F7wHKoqRfFrXL3INYON5cSGJeEGTsRUsJGd2LuA9UpPN8t8oq7tCyl81E-J_6ZlVQCmk8zA5KK4_KXeVqnwaKgal5anmcd3IQj4VUCmyKq0quGHKU_zhKKSotEEjfaYd0yfhGR7qtuBro19sfcMvvI7Jy9y5S8fNwYCL_yieSi0raDk6w-sOr4h-piNROK8VfqfS4rY_DpJUkd9ByEjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d817e971db.mp4?token=rdLIFUFYTLushI6SWQ9JXHEzWcADYrKydTSMC8uDqZaPMB7YUnROiFeT83I7yiVoO3U7krLF4O7265WIjG9J12W2jSaRG1HbWyDnxNXMjSAc_Wf0ZvHfmar7sCtFnjwZJ6F7wHKoqRfFrXL3INYON5cSGJeEGTsRUsJGd2LuA9UpPN8t8oq7tCyl81E-J_6ZlVQCmk8zA5KK4_KXeVqnwaKgal5anmcd3IQj4VUCmyKq0quGHKU_zhKKSotEEjfaYd0yfhGR7qtuBro19sfcMvvI7Jy9y5S8fNwYCL_yieSi0raDk6w-sOr4h-piNROK8VfqfS4rY_DpJUkd9ByEjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌گویی‌های سگ زرد درباره ایران: در حال حاضر، مذاکرات سازنده‌ای در جریان است. ایران می‌گوید: "لطفاً، لطفاً، هیچگونه محاصره‌ای اعمال نکنید."
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/akhbarefori/675908" target="_blank">📅 23:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675900">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XwxJYvu-p2G5C8w0Oc4ZD_OUsgPKkYdiJK-bHXWKwzU1HOKu2h8MFxZY7YllCzaYldvHjLweQH6ZO32VfWnKoL9uoGB7Og5_pGc9CHYk76vomOI50vLt37zNFqW31WdV7eYFMtoG6nwHOaD17haLx0uPflDxuTO5qAWLY86Zxynl4Y6sT0x4KvjIEhzddjyliZTA1BI4t8-11rxyWjon9XjnLZyN6gSESjhhpi9yXoeKwZGjXHDkgF1tNWa7rE8UkJDHD5G_jjORbFstz0UIQOPFOkXJTTNoQeCIxMbpu-o3ycYNNbjaX1CNR3MLvA2HPAuCBSHZwd4yaLneo0Z8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XrJn_3ExNKnYwnLbiKU5F3for4upt1sNb3G_HWUmnz7l0PjNDQeQVP1qAr2tRPAjB9FH18aIMJ_cUTNTmaV36hwqZv8zu91MgPtRSWGvWKrSO2xo5CHN1v6Uw8KL1nuZsV6HwJ_u3pfz7yyg3svH7nzBHr1C1-9YuGrq-VeB-uZa4rtvSCtTfjAFNF617cuYjuPTMG8X2pHV94Q5RKAnN7IKqOz7Wno53rCgsByM_sptCi78k4Lwt23bQ4euncQEN_DXiCNwjAbIcvD0FZToFtQibbKh9PXo-b7pAssqarfnKBv1d-O4XDMXm-tLBxYNRNLm_vRj46w92h4tku66ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-4sYnb9mvT5Fcs8nJX9_1-aPtquVOM-AMuOzXdPYk7geJnlD_lNKXwjLCygbaIKjzuJtBet3KXS92rTQOHLz2EN11R9_Gp-n-vlbiGbz7HEcwPkbTRv9y_2odi0g0Sh9s7mcuVHgc1z6myF1-TFCS3fv_ZWk67jmfxLCI61oGIxgcz_fAm3aI-ObXhEE5tswYv1cwbyf7tmh-dD8v1G-gCY9aGpMVxS5Uh5IfjFxBuBp9DMYDSNQQtfd79KrIFXFabRBfI7eLK9x2jv1uK7RTF5-tbxcS7WHKiPJ1Tth_I8xvGp4d3GsuN2xrc62vUMsCxuX5n3Fg_d4sdNhPStIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SKecR7AtOcy32c9-VhPdbMBaCrj5gT65yakjXLFdbof8_7-knvSUvvISfphfMNmo3PEBypCJzTGPQRrqygG9CLuzySXu3gxE9d5sYYHybdPACq1_Q0EXvUSr6R8ta6r5W7QE4_gO77g9uk7oSlkaJ6wOvFL7YkTkscA9OKW4ek9FgF0w-WavyuhxhD7pGO6qqiBdzXokTJhmwFTFjda1kSpywX95V9ik3I07-qE1z9i8GBSl0IZ861S3BnEpnus-gBbgcBMIalA5A5SejkMPLLXA2c1z6beRQZoVMsMVCS9g98mR2B7fOfpBs6Sk4cI-N944sguJjsYSEETJ7cu3mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujv_ZrxAU9d-yS-TIMqRw-faGaQaHIFdtQerQNkXGrLBS_jg1h0AuNyoYxLKGVPhbGt80J9Tu-wTvcnA_mqpJ-0k1G42TMYqx_ikeCPqeGt67pUr37-tbiPwf9GW4yVJ9UUr0ybYSYjQux_cddqi6UlMSlIbIazUQv9s4YX2M2GOs3Ilv_cUG9P1-IUARMrl6QBhw05ggGD5qNHZQTFa1v8XLDs7r9p8VmjIJJIvSekGOXxfkpkwGNvPdCDgh_aBj-G3d5LdE-ycd_zcjXetn5zFvG202a2IDZXGCYIeCZtv6kKh93AfBDrMUASdrV1yXTCkvPkOAYDOqJfeRzZCUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fs_bjuNLz2oGfgi7uMrJk2dY6Y9DyTLtVi1BTQMDD1u3Bk9ZSBz8wLZybMP6Hdq-SPKURgARLZ19Q4Yf-55EKUlTOHpfwESD98dMDMWMPMFEZBFLg5RSDo-rcpjNbhG0E9guI4yoAYedud2e285tqaMy64-p65wTkc5mtW-jFmSYGKWV5KVYFNDAeuVyfT4qqb4gjl4rTULp26MJKPtbX8iTZofFSwk1dnWqdkwob5hMXTg3krb-BeSWAM-cTutpTN9tkHk0usZr9dCGqPVYm4tlPV92HasJyMAbB8s278B-IIk7bdSwUhFlbmyxVcYdHe611XTACOA_Hk1yYnXETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TvnUlNzabJd3jK7CQ4_facXdnf7zZIAN0NqLP9o3GNuwKI7I-z3zx8bmfyT_Nk1ICPizgNxICsRKCQL1YcxngXIUkqBhqIAbpT_FOSqGmzxoxw6uV6iBLPJDgVrFk3up6qTgXRMYb4wpmH_1oPbA26dkyuWWmG87H4itmNVQywc3DXxHCBLHKRjKa9b_sv7kcMM8fu0zgpYzYZIY8CtbFIfvpg_kVHk717nwwV4FSC0XWgDA-z6uWkJkQzyvhCD7Dun2atyZqyZglahcZ2RwHI7pgm83eQ8t-Iyy6aC904eue-eja7aIZtyn_z3S2OPjOgY_42HMeL_igrANSP3Gtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vRkRYovyK3PSC6dRq9P68SHlggLsECK0W1L5SosMoviKG5WjQQzpH2qavx1Lj_-Ip_QiuGJRlgl-GJ7jWqnfVk_MGF_eAuAyq8YfAE3d8iF6Emwd9Ubu2FKtAZsg3wGvN9HBj95bVWyAcrJhu7b3AabKfTVAnNOT1-wa7kdWFjtwN1db8wGl0PgI4bWhJ4IVOwOlEEmIPrcDosGuivgDJP2z5qUsAzfsjkeh_XywDu4K2SgP7wOWjMv5-dISNhHDYPZvd-h3Z3mCz2JlFxE-iO3FEj6-aUbnBSQ001xzlGh-QYjGUwLWz7_mFn0Xq8zJBtRbNvBXV3gy9vw9l5LgNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۸
عادت طلایی برای بالا بردن انرژی و تبدیل شدن به بهترین نسخه خودت
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/akhbarefori/675900" target="_blank">📅 23:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675897">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5c64910dd.mp4?token=Krw8_6346LvPHayxKRXpS0trLoE9zss_sNWuqZ4K33xu5Rv9N_jOM0I1t-p5g6BCrFVmgZlshX92i_ooUjmuJ4jccaeH4Q90saTmKC2wwWHoB1xZLGmiEK5jpjn1vM3ZPrxMcQIWGbL0kxvwiOT3Lgw6Lnu4q01REIGoIhGW-WozUHWGxMPdfdw6O-2oZ8ao2749uDe9U90muUBBGhstHXsavp_33HAnNmksQPiwE92RZn4Ib7O4VTs26hnR6qWaJEwusFD8UnQVGM3YxVMcXkMvzLPVAOVKMO_jmYF5-QEwuGeMwT4HuaOxJehpWK9p91G7R6QiAR3wuGp7waWsPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5c64910dd.mp4?token=Krw8_6346LvPHayxKRXpS0trLoE9zss_sNWuqZ4K33xu5Rv9N_jOM0I1t-p5g6BCrFVmgZlshX92i_ooUjmuJ4jccaeH4Q90saTmKC2wwWHoB1xZLGmiEK5jpjn1vM3ZPrxMcQIWGbL0kxvwiOT3Lgw6Lnu4q01REIGoIhGW-WozUHWGxMPdfdw6O-2oZ8ao2749uDe9U90muUBBGhstHXsavp_33HAnNmksQPiwE92RZn4Ib7O4VTs26hnR6qWaJEwusFD8UnQVGM3YxVMcXkMvzLPVAOVKMO_jmYF5-QEwuGeMwT4HuaOxJehpWK9p91G7R6QiAR3wuGp7waWsPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سگ زرد: نمی‌شود ایرانی‌ها را خرید باید شکستشان داد
ترامپ:
🔹
نمی‌شود آن‌ها را با رشوه خرید. باید آن‌ها را شکست داد و ما داریم حسابی آن‌ها را شکست می‌دهیم. خواهیم دید که نتیجه چه خواهد شد
🔹
همان اتفاقی که در ونزوئلا افتاد، در ایران هم دارد رخ می‌دهد فقط مردم متوجّهش نمی‌شوند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/akhbarefori/675897" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675896">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZnEchUP1VwfLHlRgMiBXma-6C7Vu9QKv_wDJk4aTv3tQLhB3Ntz5y-2HxMP6mSodQ5Mbhb2S2II6Y8CY2P4iyvEntBArEg1zBacaWC9o48gB53NS_fgtY6jdE7NyDcXw_Iq5OQrxSZpETfaGv3l4b8N6-YU82NVNN2fs9Jz-_vIvejF2vum1v_0uQ36IuWOF7gvLNhoAj_iqf3wUU1rkDmT1zmdJrjRN-URMVbo4ezo2l4s3xqkGRXIPnKhl6SLaaMIGHUlpv-GKuUryhbGlofR1mmd2R3aLv9AcdQfOuuxOEQvfXFNOYkxBV7SxkZiW2ZDtsdhhY5Oei3vXzz8NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دینار تو بازار کمه؟
🤯
هرجایی دینار نباشه، توی دینارز هست!
خرید راحت و بی‌دردسر دینار از دینارز برای سفر اربعین.
🏴
@dinarz_app
🔹
نرخ و ثبت سفارش:
https://dinrz.ir/9v6
🔹
تلفن پشتیبانی
۰۲۱۲۸۴۲۸۴۱۲
🔹
پشتیبانی در بله
@dinarz_support</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/akhbarefori/675896" target="_blank">📅 23:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675894">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66ac763ce4.mp4?token=Bgyn60I5_ug5F9BBP46HC5pggGkR2uwBS6IwUQUK5bcxr4kgXEWFVCWqLcqGSBqcZwVj4snSdkOquBLHsMvU2C5L5IjZyF67bP1M8VP0-sY-zfxPOspVApigjCBGqJSTzQOX-nmzvJaL0ppgoUjuXYJbxoU5_LLBGApX7il6nsVfuZC50HvYio6rlnYQKRLKxb9zbzjinU3tpiEHgwps9wTFBamjMNd3Y1_A70kMcTD_U7ZPhz8py6sfdomZk7AiVLByTpzlfJ8JwTBHoiUxOFsW6rxgEOtD7FILQWmIyNzSL2Cp2SMIyc3L1eAxoO5EHRNwyQNZuAMDgNZLRlKvmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66ac763ce4.mp4?token=Bgyn60I5_ug5F9BBP46HC5pggGkR2uwBS6IwUQUK5bcxr4kgXEWFVCWqLcqGSBqcZwVj4snSdkOquBLHsMvU2C5L5IjZyF67bP1M8VP0-sY-zfxPOspVApigjCBGqJSTzQOX-nmzvJaL0ppgoUjuXYJbxoU5_LLBGApX7il6nsVfuZC50HvYio6rlnYQKRLKxb9zbzjinU3tpiEHgwps9wTFBamjMNd3Y1_A70kMcTD_U7ZPhz8py6sfdomZk7AiVLByTpzlfJ8JwTBHoiUxOFsW6rxgEOtD7FILQWmIyNzSL2Cp2SMIyc3L1eAxoO5EHRNwyQNZuAMDgNZLRlKvmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنرانی سگ زرد با شعارهای تند معترضان علیه او مختل شد
🔹
معترضان او را با عبارت «حامی آزارگران کودکان(پدوفیل‌ها)» خطاب کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/675894" target="_blank">📅 23:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675893">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
حاجی بابایی، نائب رئیس مجلس: ما هیچگاه با آمریکا به تفاهم نمی‌رسیم
🔹
ما نباید هیچگاه با آمریکا در آتش‌بس باشیم، اصلا آتش‌بس با آمریکا معنا ندارد و این به معنای آن نیست که مذاکره نکنیم، و نباید دوگانه جنگ و آتش‌بس را بپذیریم.
🔹
نباید اجازه دهیم آمریکا هرموقع دلش خواست حمله کند و هرموقع به مشکل خورد عقب برود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/akhbarefori/675893" target="_blank">📅 23:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675892">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7Zqz2flf1VLx9VTkWmDa1Q_2QsiKFhwhn1ShqGyGq7synaaCA_tlaVjWtDFOgcrr5bz04xIAcUEG7RFDZY4z5nsOYrhBppjmV8oOlRG6-AvotNFeYceh04xS-nJdvQCwJ6xRIprHyjlnksql4b-08wofyOLsJ9oqqVQGLzd8mXcyH5wI5EdXoj3XejHDFbezQ-w7fFsUkx5nRYo9KW3CIvhCDH2VkP3JkkiUuIUy-BnZGpYa72eOrxIK-2iGvZix9APtZyH0fFiV81rh4v9DQHtQ7BSvRWSswDirbfyGf6J6DFHanmLGvukqYjclTJLjr3ZSMPgq5BhggvzudIc6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴ سناریو پیش روی جنگ ریاض و صنعا/ مهم ترین سلاح های یمن در جنگ با عربستان را بشناسید
🔹
یک سناریو در رابطه با جنگ عربستان و یمن، از سرگیری جنگ زمینی است. دو احتمال در این رابطه وجود دارد. یا عربستان مانند جنگ قبلی مستقیم وارد جنگ زمینی با یمن می شود و یا شروع به تحریک شورشی های داخل یمن کرده و آنها را به سمت جنگ با صنعا سوق می دهد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3233622</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/akhbarefori/675892" target="_blank">📅 23:08 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
