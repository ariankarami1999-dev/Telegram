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
<img src="https://cdn4.telesco.pe/file/kYmTTZr2Mtk2V3rx2IfN9-MdnG6mnZus1SsllUABY792GXI0aZBg7DrLApwjjToqRjvdLneMO5ivcC36YyoZvwXMQ-EjK39ftHzLDuoeMMkW8tQ2gLaoSHorwgSQU51HnnephB4J1cnM6xySeIyQjt8mHjwA6ki4OYmhF6bAo70ymN-D3mMNn6Ow1QuPB3-QYB-zKTn8omVURsVKOXAcNGCgVHogPNBEj-WxxV9qV8M_UhMLmvqPw-j2jgRTf9WGOQUrnvE_i-Q3JWF1ho_7kXFoCuSKUuBHynGSQybZ1GYihoLznfKGJAryKE5SmigLziIf94xwDPX2re2zmnlOzQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.2K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 16:08:11</div>
<hr>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8m0JWbOhctAf_HMNC5D31kv4qcebW6_-UHWkGTCUgW24OAxegon8jWm0npAc2DG_RHiMsR6ct2D7jiQqrG1njjwZydYXAB4sAHh17u68zouU_UpNYC_xO0Vr1uL0MOZLahthOcU-UnmfObJT0oxxnAKhxIqSb4u2zvU61jcRyKTE--iHf8ZOORMZ-pJX-WylSR3fed3XI-GuDvSIN6T0DydsrU5wIHhxush2I3JkT7W2Yc1YWSwwIMAHQcuR70oZi5KcyIwdeIEYxEiBJg-txg5urObKvADeJ2gEXQrdPiZu3YmifbcxHgaWvjXF0PV5XeJ3gUvlJ2rneOStt7YIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 193 · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J9KQIjrNxrg9zFRkRX1qBIsLCeOgm3Gvf0oHfPWD3E7_DOIt8boaNNJvXnEDsUz-KVQ-hopgxAUdCzKRMSJ5InmayQQlcZIZMt7qsXX80aapdAT66yr7hYTzqw-TbRhARN7X-B9AEjzIuTO47RfAfjPtB-lqMjkIrsbG4lyscypoflYnMwOgrHgXkf5fJ7XJxWbOXBaXrAvNq6rL1wR7rAS77l7MxkXejEibbY5_45DJfEv5PMHIzSJEeW-zFuw2TPEDghawnxz4veAC5JKE7ZFnwrkGv0oZ5PdFVIQxyt5XD8WIWm77Wcz7iG90mMPqYqQ5A8YXZrLvNxmpLp7pDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
☁️
اکانت تلگرامت رو تبدیل به فضای ابری کن
⠀
‏یه اپ دسکتاپ که تلگرام رو به یه فضای ذخیره‌سازی تمیز و منظم تبدیل می‌کنه.
⠀
‏• مدیریت فایل‌ها داخل Saved Messages و کانال‌ها به شکل پوشه
‏• پیش‌نمایش، پخش ویدیو، همگام‌سازی پوشه، WebDAV و REST API
‏• ویندوز، مک، لینوکس و اندروید؛ همهٔ قابلیت‌ها رایگان
⠀
‏برنامه اوپن‌سورسه و مستقیم به تلگرام وصل می‌شه، بدون سرور واسط. ولی دو نکته: برای ورود به api_id و api_hash از
my.telegram.org
نیاز داری، و فایل‌ها تابع محدودیت‌های خود تلگرام‌ان — پس «نامحدود واقعی» نیست. نسخهٔ ۵ دلاری فقط تبلیغات رو حذف می‌کنه.
⠀
نکتهٔ امنیتی: اطلاعات ورود تلگرامت رو فقط توی نسخهٔ رسمی از صفحهٔ ریلیز گیت‌هاب وارد کن.
⠀
‏تو تلگرام رو بیشتر برای فایل استفاده می‌کنی یا چت؟
👇
⠀
‏
📌
مخزن گیت‌هاب
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 504 · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXhzzuKF9r6jVlq5_J7MdkHrPTwgHvEF4DpCkAZlc05qdv9zOYXws0owcCM2IeJ2oU6ysFdweInMfHkJOK4Vth2SsHkoppv2T5Gne61HCbRZMlUFKUE-Y8xeGujFJz7g0LXVx8YxE6MFsvEdrLWA9aGM0xpAJ7hqDrFIS65D4QTQG-iBkeltIX_ZCh08dUOJbqUSIWp24Dac5jXI66GCe2SoipzNtkN5v9nPSRMPOrOn6cUGT18bLEmr_0rLdZGGA8L956bvE32j4_Ii7N7uu8ixgnYmCFjFxcymCst15sjsktOKLYwOVsAsO-dxDttINsiof-YY_jpDH04XqGc7DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش
‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.
‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری
‏
💸
کم کردن هزینه با prompt caching و compaction‏؛ به گفتهٔ اوپن‌ای‌آی ورودی کش‌شده تا ۹۵٪ ارزون‌تره
‏
✍️
پرامپت: هدف، مخاطب، محدودیت‌ها و معیار تموم شدن کار رو روشن بگو
‏
⏳
کارهای چندساعته: عوض کردن دستور وسط کار و سپردن بخش‌هایی از کار به agentهای فرعی
‏تمرکز راهنما بیشتر روی API و Codex هست و برای کسایی که با این مدل‌ها ابزار می‌سازن مفیدتره. قابلیت multi-agent هم فعلاً آزمایشیه.
‏
📌
راهنمای رسمی اوپن‌ای‌آی
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ffh7S_Y7j3GacrSHdbuJFgGj4YPwYAZMc7PbMcrkkflvtlpkwi0t6Mn5DBnc5prdrk0BqMTubPOHDuGSItBk3N0KPiWFFTrAegcAAIcvOjDixDWWBJ4opXhiqkpm7jzwAwRWBrT7Szq2_0QVTDFcjgjS4krEBeuSiouwOPap__m2Xn0Jsqr7A0OuOZzMkazB2ziyuBsKEAQvvuVJbrzuh5vomTVNHZDBae17hqreuMabTagC2uGtajCPLainP3vA2b7l9gK2SGqsRFkue1DTciSNPpHm0JYIbfDFa2a62GgeocE-wRKm9TUPrTzEK_57FP1Imhny4gomSTT8nzvPoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚫
انتشار Grok 4.7 در اپ‌های گروک
⠀
‏مدل جدید گروک حالا توی اپ وب و موبایل هم در دسترسه و مدل پایهٔ همهٔ حالت‌ها شده
✅
⠀
‏به گفتهٔ xAI، نسخهٔ ۴.۷ روی یه مدل پایهٔ بزرگ‌تر ساخته شده و با یادگیری تقویتی طولانی‌تر، توی کارهای کدنویسی چندساعته و خود-بازبینی بهتر عمل می‌کنه. پنجرهٔ کانتکست ۵۰۰ هزار توکنه و قیمت API مثل نسخهٔ قبل مونده: ۲ دلار ورودی و ۶ دلار خروجی به‌ازای هر میلیون توکن.
⠀
‏
📌
یادداشت‌های انتشار xAI
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRBUb44WyTUtzvT_pGYWqV5ryjpVW_KtVSVsZIj5zbeoLrdjSoBdD85y--WqPgfhunYjjo2KYszkUCMd9bZMpLy0iZzMy1wMahoZVV5v9_dvYNZIBRrZtN4lgwDbVv6m0PTSfKaiNRbp_mQGn-7ocj0GMs3wof8lYTBBAxJsN6M3GZCqCadCMOn5rIx4X6T_KLY7Z2LO5NeAYj1bxbGOMVqo2aVophS4Tz2hY0c3I2jizOsNuqv9xWpxPcMOqO1gFBvJIi7S3VChtrae5SZcdx1Ad4sBax2vFJ_Pv3MdWfZdPNQN4OdJ1e7NIQY8nvYnxROyN6VVQdvHavYlk3qhtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان و ممبرهای عزیز آرشیوتل،
😍
ممنون که تا امروز با حمایت‌ها و کامنت‌های قشنگتون سرپا نگهمون داشتین. سعی کردیم به قول نیچه «با خون بنویسیم». راه سختی بود، ولی به لطف شما هنوز زنده‌ایم.
ممنون از ادمین‌ها و کانال‌هایی که با فوروارد و تبادل منصفانه حمایتمون کردن، مخصوصاً تیرکس نت. دمِ توسعه‌دهنده‌ها و همه‌ی کسایی هم گرم که تو روزهای قطعی، اینترنت رو زنده نگه داشتن.
تیم خفنمون هم که جای خودش رو داره:
احمد، که داره به مو می‌رسه ولی آفتاب شکوهش کانال رو نورانی کرده.
وگاس، که تو روزهای قهقرای من پشت کانال رو داشت.
«اس»، که با اینکه گوگل‌فنه
😁
یه متخصص واقعیه.
محمدجواد، معین، ایلیا و همه‌ی کسایی که سهمی داشتن.
خیلی‌هاتون دیگه دوستای نزدیکم شدین. امیدوارم سایه‌تون بالای سرمون بمونه و مثل همیشه با لایک و شیر پست‌ها همراهمون باشین، تا روزبه‌روز قوی‌تر ادامه بدیم
❤️</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDkz79Z3NmIelZ_f1FqXey6ZO14d5G9mNgcSQ8WyiJOZfUnG4kSQEU9uUB2cjEnTBQZIJWHvwjgUilFl9yKWjrL2ELy21hjdl4LKB8cUG86vRcDr1jskZpxkW0tmUbE4P9FRG7CyYQgrAC4bT9L8jRyo36XKD4MccYfFTfdCUcRrTi9GaBapryJ1EXAEEwuRLqd07D12lOPoD9COpQBKnbE0BB_7CaNNP1xCscbrvdw-Ua4-ts8OVKmKRgbsHbQEnM7utLaPKJnf4jPnRoac1lgo4-dW3QtOsmCEiQpuD7qZTmN2arZKKNJgKD4TnQ1M9UIq_W-fkLBuwchUi0uwXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کاربران رایگان جمینای فقط فلش‌لایت می‌گیرند
⠀
‏از ۹ اکتبر به بعد، کاربرهای رایگان جمینای فقط به مدل فلش‌لایت دسترسی دارن.
⠀
‏
🤖
کاربران رایگان: مدل‌های فلش و پرو حذف می‌شن
‏
🤖
مشترکان AI Plus: فقط فلش‌لایت و فلش می‌مونه، پرو می‌ره
‏
🤖
مشترکان پرو و اولترا هر سه مدل و قابلیت Deep Think را دارند
⠀
‏به گفتهٔ cnBeta، گوگل سیاست دسترسی حساب‌های شخصی جمینای رو چند روز بعد از معرفی مدل پرچم‌دار Gemini 4 Argon تغییر داده. خودِ Argon هم فعلاً فقط در اختیار سازمان‌های امنیتی و شرکای گوگله و به کاربر عادی نرسیده.
‏گوگل گفته زمان دقیق اجرا برای مشترکان پلاس رو با ایمیل اطلاع می‌ده.
‏این تغییر در مرکز راهنمای اپلیکیشن Gemini اعلام شده و کاربران AI Plus زمان دقیق اجرا را با ایمیل دریافت می‌کنند. سهمیهٔ مصرف از ماه مهٔ امسال بر اساس محاسبهٔ هر ۵ ساعت یک‌بار تازه‌سازی می‌شود و سقف هفتگی دارد.
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIve4QABb6AleZxHagHrrgY_Y5Eudss2M4IF2fLL_90LSbK8QEsOJ7Z6cMSBl2LExjsUvA2kMvIFk8eHVoqo13R6cVZ5newkZjRx_L9E4CouFd1x1tG2xgNyVdQebvSW2ZZ3GNr45F36u1h9Wlx6BstWsDt6rxmc4frb6HW5MXKtr_bGUnIWEEchZz3DFvDlSrOKdvJQSX-zcigJyWeRlOyV_1LgSmIQCQdAZqqGRRixJKzRKdHiEbhcPOvf7Uk_LzNUhmvu-aAzC2H85GyNybLhDLf5IPGVZmpaD9wQFMH2v3uufH1SkQ2lB1ORZo39MNJKjCvxtVC2qGedCB4YcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🟠
مدل‌های Claude 5.5 به Antigravity گوگل آمدند
⠀
‏در محیط کدنویسی هوش‌مصنوعی Antigravity حالا می‌شود از Opus 5.5 و Sonnet 5.5 استفاده کرد.
⠀
‏به گزارش سایت appinn، دو مدل «Opus 5.5 Medium» و «Sonnet 5.5 Medium» به فهرست مدل‌های Antigravity اضافه شده‌اند. Opus 5.5 برای کارهای پیچیده و طولانی طراحی شده و Sonnet 5.5 برای کارهای روزمره و کدنویسی است؛ Sonnet 5.5 نسبت به Sonnet 5 بیش از ۳۰٪ سریع‌تر است.
‏نکته: برای استفاده از Antigravity باید با حساب گوگل وارد شوید.
⠀
‏شما Antigravity را امتحان کرده‌اید؟ این مدل‌ها را تست می‌کنید؟
👇
⠀
‏
📌
گزارش اضافه شدن مدل‌ها
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h1P-KBcCN9EaAo2kUgcVsdCR3F_KaXwRQaJGGXAIuw62uhMKjs3fytSfGdFIgG4KyLAaCt83jlIaYXjMcVYX8BfPM9G0lfdCrIYrFOiTgGrszArnGbU9v_6RW6F-Sv1VP0AGA0O2SgQXx0PEbF_oNVEKXkwku32sy0fT-0t6tcS6KsBv1OUiyScPUqeJCNgNTuny3RHBwmkTaXWPe_qVt9acjIfCA2MwHDv4jDUe17uZ26eKHUu00Dl4yat-GYwrpTmAAmYeJa4s4jtNCyt7h4ZXadixFnW6qOSwtKROFpwi_mSMkDUl9sqUpKnzcRnPEG2jwP_NAFNYJIjf-vNP2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
مدل GPT-6.1 Sol اوپن‌ای‌آی رکورد زد
⠀
‏سم آلتمن می‌گوید ۶.۱ Sol سریع‌ترین رشد تاریخ مدل‌های اوپن‌ای‌آی را داشته و مشکل کندی‌اش هم حل شده.
⠀
‏رونمایی در DevDay؛ هوشمندی نزدیک به آسترا با یک‌پنجم قیمت
‏کانتکست حدود ۱.۰۵ میلیون توکن و خروجی حداکثر ۱۲۸ هزار توکن
‏ابزارهای جست‌وجوی وب، جست‌وجوی فایل و استفاده از کامپیوتر
⠀
‏به گفتهٔ آلتمن، این مدل در ساعات شلوغی کند می‌شد ولی حالا «باید خیلی بهتر شده باشد». قیمت‌گذاری‌اش هم برای توسعه‌دهنده‌های ایجنت جذاب است: ورودی هر میلیون توکن ۲ دلار و ورودی کش‌شده فقط ۰.۱۰ دلار.
⠀
‏نسخهٔ Ultrafast هم در راه است که تا ۸ برابر سریع‌تر جواب می‌دهد، البته با قیمت بالاتر. نکتهٔ جالب: قرار بود نسخهٔ ۶.۱ آسترا هم بیاید ولی به خاطر نگرانی‌های ایمنی فعلاً متوقف شده.
⠀⠀
‏
📌
گزارش عرضه در DevDay
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ke8qcfHspnzH-Fqj5ExEQfw_23hR8yzUbTqgzDG28Ia8R90Qmc7SfQUUMZqO18oTUO8RuQfTcXeKlvu6x2cllnmz-aChWd2VW6JW6fiyYCbEFYC8JC4_5n3ICgieehcS2Ve3aLZY_CeoyUe5tptIBQUBWE2x_ly9GLzJzQUM2GEDy9lZIH-Z_w30Pmhg6oQ2qOQ4-HGtP4KBMI4PbxbdOeCCYrExC1KgP3KO11HcuMOSDFpYja3kL_6ItXcjHmCtN-7XY8PP11Ba-NvaWRF37UWlmYnnYq-GH5l_crnnnQX1auMAHU0Gtgy_5sWGB_FMNENvvcEqxvc3r0ZVzoYr8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔢
مدل Muse Spark در حل مسائل باز ریاضی
⠀
‏متا می‌گه ریاضی‌دان‌ها با کمک مدلش شش مسئلهٔ حل‌نشده رو پیش بردن.
⠀
‏• شش مقاله در حوزه‌های احتمال، معادلهٔ موج، نظریهٔ گروه‌ها و جبر
‏• مثلاً رد یک فرضیهٔ ۲۰۲۴ با ساختن گروهی ۳۸۴ عضوی
‏• و اثبات فروریزش در زمان متناهی برای جواب‌های معادلهٔ شرودینگر
⠀
‏نکتهٔ جالب اینه که توی هر مقاله مشخص شده کدوم بخش رو انسان نوشته و کدوم رو هوش مصنوعی. البته خود متا هم پذیرفته که بعضی از همین مسئله‌ها رو گروه‌های دیگه به‌طور مستقل حل کردن؛ پس این «کشف انحصاری هوش مصنوعی» نیست، بیشتر یه نمونهٔ جدی از همکاری انسان و مدله.
⠀
‏فکر می‌کنی هوش مصنوعی کی اولین قضیهٔ مهم رو تنهایی ثابت می‌کنه؟
👇
⠀
‏
📌
گزارش RuntimeWire
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiIt1vKvgfncPe-P1NNBRdz7KH-yD9ej3Z2AG67IKf09WsK_DW1XwG-GH_EGOJjjZoyoL-YublZVNyCY6Vyz08LZWAiNeN8ldtCBSViiWa8PL3hVZ8nf-rfT-CxekzrUyOhSgEfSB6IbdQS3w7hL056HkEaf3OpZKSD3an77YhdlbjO7xw_kBH2_4dM5fdebOLw0KwkPUBDtIdIVC_KRX_vFH_K8RzQrCvInMxi1Nh1DGandQ07OLhHRdn7ZSi-AZkW2TJ2ki7_Zw5DIa2Ikc1v18FkeQ4B2EjE5yooBKgyrW76GoidUk0zJwsMeDtxdscLW0QA-PF6uT5HgWZIdLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">📨
ایمیل موقت جیمیل و اوت‌لوک رو با temp.tf بگیر
⠀
‏یه آدرس جیمیل، اوت‌لوک یا هات‌میل برای ثبت‌نام‌های یک‌باره می‌گیری و کد تأیید رو همون‌جا توی سایت می‌خونی.
⠀
‏
✅
نه ثبت‌نام می‌خواد نه رمز؛ آدرس رو کپی می‌کنی و تمام
‏
📎
پیوست هم می‌رسه؛ عکس همون‌جا باز می‌شه و بقیهٔ فایل‌ها دانلود می‌شن
‏
🧩
یه API رایگان هم داره، بدون نیاز به کلید و با سقف ۶۰ درخواست در دقیقه
‏
این آدرس‌ها با plus alias و نقطه‌گذاری جیمیل از حساب‌های خود
temp.tf
ساخته می‌شن؛ یعنی ایمیل‌هات مستقیم می‌ره توی حساب اون‌ها و چون رمزی در کار نیست، هر کی آدرس رو داشته باشه می‌تونه ایمیل‌هاش رو بخونه.
⠀
‏
📌
سایت ایمیل موقت
‏
🌐
راهنمای برنامه‌نویس‌ها
‏
🟢
سیاست حریم خصوصی
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnF_tlZXrXam_xfo-D85QtTdxhqm_XTddMDJahkpWqYE09wca818AcHXBlgxEZ2vY-KQzkK33513c-61eO9Ri1s0EzW6aSvW9HEJhKnzDi9gbHKu8K_1mZ6uTUfZTVskKGkt1Kktv6h6NbE5v_OZN4h1WgIjvHDcLg47Z9eDkEjlQMBePShELENWmb3PyOFCJC4f5fHpDVvDRlwLol8_z6t46efVL4SjUvd7CcJEI3-ER9AKih3dcBvDaPQRmVi5OSYRW8dccoun384gJKa0XkEbVoNvCw15qmA5RMoyZT_n83Iate9yi119sdgNTu6hcDKRodVdo3ohYo1kMyBt0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های قدرتمند هوش مصنوعی
💥
🆓
GPT 6 Astra | Opus 5.5 | GPT 6.1 Sol | Sonnet 5.5 | Gemini 3.8
✅
با این سایت میتونید 7 روز مهلت برای تست مدل های بالا رو در پلن Max دریافت کنید
🎉
🎁
⭐️
قابلیت ها :
🤖
چت با هوش مصنوعی
⚡️
تبدیل لحظه‌ای صدا به متن
📢
تشخیص و تفکیک گوینده‌ها
📖
پشتیبانی از ۱۴۰+ زبان
🗣
تبدیل فایل صوتی و ویدئویی به متن
📞
تبدیل تماس تلفنی به متن
📝
تبدیل جلسات Zoom، Google Meet و Teams به متن
⏲
ثبت دقیق زمان هر بخش از مکالمه
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJMpDPrAZjzjzCoHSoX6Tuwzkks9e-ITaPFkp17V-0LUTQ310W5NLXEUSyOezoC7zxHac3oUPyzqvL0izM4QYbAWepqepY1PKBaYzqcGIOiWhD1pKab0jrthAag2Vfw2dDe7uv7v3zjtB9QKYIQmHz02pbM-GQpi0bmqLVgL249XYKRUrBnzdjEcru4zdso_BqNWAiO7gh3af8gWvfRd15ZRDHnF2aLL4scoH8IuN0QmbA5kuDk5Tuqjy4WE84f71Y2qFY4-mvGNk0uw7Oy98yBYkZXt1xJYrKLbzCn-3YBuWkvpS6GQeac4pKSaZ6fYW_JUfyhjiUzJAIx7gxcjIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSoULZMrdJyKPcYYLdEzFA1h2Jx-F55ZOj1Hydiqwpdx8coq3LvgvRHZ83euJPiY0t4kW4vcLfGLQG24J08h80-a1KR2DJyFskFwjjR5HpXdCF6jTcesL5S41hRK_mTMLxoaaXWYI6pd5oODhp4NNWFnh0hh0l-3ezKOw4pBPoy9TPKrk1Sv2uEb6g3sDPKledLV5yYoSWdggcAoqYni_7GcWFHRnoTyYTwjbaole9HOZJAz4YSQhtqVya292QkqbCb_vJLnXFcxxLOXu7afiArpVXTMyWYrM1OWjnEU64l3m8a5miGD5IDIT32KokDktdorIbIxAvIOrjoflVTyhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⏰
سهمیهٔ ChatGPT امشب ریست می‌شه
‏به گفتهٔ مدیر OpenAI، ساعت ۲۰:۳۰ امشب به وقت تهران سهمیهٔ همهٔ اکانت‌های پولی ChatGPT ریست می‌شه.
‏
‏این ریست ساعت ۱۰ صبح به وقت غرب آمریکاست که می‌شه ۱ بامداد فردا به وقت پکن. Tibo همچنین گفته مدل GPT-6.1 Sol اوایل عرضه به‌خاطر بار زیاد کند شده بود و الان سرعتش به حالت عادی برگشته.
‏
‏
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0zCHXIs7oI5ni-HFfyGOyvqI9wo-CPoCb_qHY2RkrpjTU6tgqrSE5IvGvSFIKdf1HSaICJfMDXy4xVSS1Fo-zCDRaFdkZDUj5gxWKHyDIJnaMF6qLxaUcGz9DmJQaFCbMEFE-8YdFXfftxd-D5BnkO0Hksf6WxICuugagwolqFOhDNXDxaPeXwZZMYAVI50QlYicxU7AQFjfDSGoxWXatmXK3Av7VJiVaWAbo9_Qg3ZoKIW4SH285_BpnHm8qajrhHMap8q2-lBu5YG514gGroQKWkWcypE7rtt2cLRPLu4Mtt2uOgVqC1fycntFiELQdEGi3ByA7vmykENUF61Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚡️
ابزار InkGist برای خلاصهٔ صفحه‌های وب
‏لینک هر صفحهٔ وب رو بهش بدی، تو چند ثانیه نکته‌های اصلی، کاربردها و کارهایی که باید انجام بدی رو تحویل می‌ده.
‏
🤖
مدل‌های Zhipu و DeepSeek و Gemini پشتیبانی می‌شن
‏
📚
خلاصه‌ها تو بوکمارک‌های ابری چندکاربره ذخیره می‌شن
‏
🧩
افزونهٔ مرورگر بوکمارک‌ها رو با یک کلیک وارد می‌کنه
‏
📷
از صفحه‌ها نسخهٔ آفلاین هم ذخیره می‌کنه
‏
🏠
می‌شه روی سرور شخصی نصبش کرد
‏به گفتهٔ سازنده، متن صفحه اول با Defuddle به‌صورت محلی استخراج می‌شه و بعد برای خلاصه به مدل زبانی می‌ره. پس حتی تو نسخهٔ شخصی هم محتوای صفحه برای سرویس مدلی که انتخاب می‌کنی فرستاده می‌شه. نسخهٔ نمایشی آنلاین هم روزی ۱۰ بار خلاصهٔ رایگان می‌ده.
‏
📌
مخزن گیت‌هاب پروژه
‏
🟢
نسخهٔ نمایشی آنلاین
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sujCjJhGW-Wgi0ukNMBwTLMNmXTWUW1LbusKahT3rS66qje974nv37f3-jjs8AmBhApYGoxSNsg-ZUhMVcioTHfVHZP3FDraTsZeEsXpkMNR7lO4VbT7nlU8eFGVEEZERYtu2lyor9pfXjUAeoOHhVrtr2CvuDkGcVrCJQpLjPimQWri6Gc28L1DXT4hzhOMP8GE7dW6viHOjZ8aJ2ZCPoMMROdfy3Ggul1CcRF2n5bEEZk7vUDbr-B8Lk6Ie6paU7HaTJuL4F4Ln8xd320SPqSWPvMPlsWFOc_bgZVQudMAwO180-ugB3x4Iku1kzEaSy5DvQrG_ed8DXGQd60Tdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nq9xkiaj-e7zb6ocOa76C6uo3mhcoJDyRI8_CbAqhfEIgPrMw77YqXtihEFOcyxayFS39eUzGGdeXOi-sUbyo4dDjYVj8pidsch-es29I2RCw8BxymMaMsT4Fmv5eZv3v2OtN8DH68wl5upDWY4ToIdTnG59ECKxPiDMlyOcy31-QWCOgmVDSadCdW6326D9H8XZClbdbyPv9s4HSXyv2MW1DltLZwYGPfsn0WoCvvqPd4hpKBMw0NroKSQb0uPeqZrWxx89ukhMWAemW5GULcqDGe5arv1Pa_sGOCP2WW7s7Ec_Y2M7SOx5JDzlNrmC37gdyVxQZo2ix2FLNiJDfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه
‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.
‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد
‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد
‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه
‏به ادعای Anthropic‏، نسخهٔ Sonnet 5.5 بیش از ۳۰٪ از Sonnet 5 سریع‌تره و هزینهٔ هر کار باهاش تا ۳۰٪ کمتر شده. این عددها رو فقط خود شرکت اعلام کرده.
‏برای Haiku 5.5 هنوز تاریخ دقیق، قیمت و شناسهٔ مدل اعلام نشده. حرفی هم که می‌گه این مدل از Opus بهتره، فعلاً هیچ منبعی نداره.
‏به نظرتون مدل کوچیک بعدی به کارتون میاد؟
👇
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgIqPOBH3zzS__rhNxUl2yD2kxY1rSytPyJSVq8T73kkio9h7kuwlL6m8pvcFcL7qN7sMw-ESrb0VhP6BTRGTaa7-NF7ogLM51YjP5oGXqGU_sz_M8X06Q94CBFdH0xUdNZCDpTdTpm1Zcbk-Mgwmj9O96TNjUK3OU6oR8X03ND9Zdsc-7PofKweh-5UunZzdKinjfcYW6r6wOWidXZaIDRKkRm9Ic3zXHx7yfeUxxeR9aecGKrYRIpuYFJsZ_lLdvyIefrg6flk5at5oh0DAafdL8ZpEMo7pEsMavX7I20SGxnY-GAmNjnzIvxs1r6TFpgJfh0GQU3Js2yX_iBzjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Claude Sonnet 5.5 روی اوپن‌روتر عرضه شد
⠀
‏به گفتهٔ Requesty، مدل Claude Sonnet 5.5 با قیمت ۲ دلار به‌ازای هر میلیون توکن ورودی روی OpenRouter عرضه شد.
⠀
‏بیش از ۳۰ درصد سریع‌تر از نسخهٔ قبلی
‏هزینه تا ۳۰ درصد کمتر در بیشتر کارها
‏پنجرهٔ کانتکست یک میلیون توکنی
⠀
‏این مدل دومین عضو خانوادهٔ Claude 5.5 است و به گفتهٔ Requesty در کدنویسی و کارهای ایجنتی نتیجهٔ به‌مراتب بهتری می‌دهد؛ قیمت خروجی هم ۱۰ دلار به‌ازای هر میلیون توکن است.
⠀
‏مدل هم‌زمان روی پلتفرم
B.AI
هم در دسترس قرار گرفته است.
⠀
‏
📌
اعلان B.AI در ایکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAleNtmdJ7Qdkc9h2Ug1Ld3uvIUHGd9Ve9JSzXgWfKWyVRUYNDunRcmdvdkZTaGmGu6PNQGjUi9fEp1jvlK2F-HuRKhomL_za29LGne3jcI0JJno8ESjUN2KJ1XdDyGv_od4j3ywfmKfWmam3yDL-tYcD6FcR-hLKhaHIpUBiO-Q3TpNRNBnVgdR9wj5rAD1pTl2fklJXFIh2zZqtGudPO0mPsbpkDOdl2dE4bE0xoFROF4umd5v__6pJKl7d-fmkBiteG1Vk95hiTPVvPunRDeX5JI2D6CbZYovDpS2mXqVNDFZDZquOhW1n34QGrmJjDPLZhQH-oXN60-vtA37MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💻
همهٔ دستیارهای کدنویسی توی برنامهٔ ccgui یکجا
‏اگه کار با دستیارهای کدنویسی توی ترمینال برات سخته، این برنامه همه‌شون رو توی یه پنجره میاره.
‏
🧠
موتورها: Claude Code‏، Codex‏، Gemini‏، OpenCode‏، DeepSeek Harness و چندتای دیگه
‏
🫧
یه برنامهٔ دسکتاپ که با Tauri ساخته شده
‏
📦
نسخهٔ مک، ویندوز و لینوکس طبق صفحهٔ دانلود
‏
🔄
آخرین نسخه روی گیت‌هاب: v1.1.0 در 28 سپتامبر 2026
‏کد برنامه روی گیت‌هاب بازه. ولی ccgui فقط یه رابط گرافیکیه و خودش موتور نداره. برای هر موتور معمولاً به حساب یا کلید API خود همون سرویس نیاز داری. کدت هم برای پردازش به سرور همون سرویس فرستاده می‌شه.
‏
🐱
گیت‌هاب ccgui
‏
📥
صفحهٔ دانلود برنامه
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIcWfLs5po8CCJxISGqYUNZ0ci5jvTjLuiHZ-lOqHShvvuK6cRAewpSSFyOZ3UZmSHDjO-oJFsGdFfkTQxxMS6AcecNtWxF0iUS5ko-ET65Ya1b3P-n7dS1_ER9Oe4Q-ORhkBgfZV95wjmz5O4TbHvDc54fVDT6BaJ49hAJ56CosK1WV_sq3VQIEyxilPrlz8CwUuvYCwib_eZYj6XznT5_f4coYSSqvKohp73vmpsetgeGgswDpER31HwRsBovn8fx8v7LPWTr3jYXiVFFe0sO-NXfa1RqK04mLtFU5gTVf92Us4STNbZlUz3XDPqQ6FV7cwd94upQlq0Q1kZULiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/COpU7uiU4tIRpgKYCV47NM7P7zKnEPNdNO2FXiB1vcgMJUOSiY2eKEMjbphgUDcJuNViOjPlQNNiFicC9OkDVBCAiuh-TCUl5tfrgU7WOM_WOwrDqvY2F8Y6PQZPdB8xIugi4kWFM-KybpndMyaOP0Xu6SJJTRu49q2HsPkK3yGg1j_h0dsmBP8AlGBEQWOPU92vmi23R5ro2kvdg9FMo4SqrOj8qeGFBK-wkNiMBT0nc3Vr-lf_SQzh4dBbz4NVY0W6zdmMdHO2e0YLG9TFP1T10PjPYlMyJU7i8faK8J5JWd-VFN0tfXMBuntgLF6alR4RyVpIJUca0G4d_TDXRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qAEn49Y-r7Q4dYod8Vt2mZaa-UX4JUCyjsBtBv2jzOvEmZzRSEvQOSwkVmbvrVr3Mi4QLM064RoBZGjBWhfboVYYQgl06n6_6U-JhJzcWgWNeIOvT24AINV5s7BW2Qyz7XKuSy-WzzQBY-U52WlUy8Th8obvZ4SyDA_T97HUi31CvPmGO-Nl7cnEXPCRTg83rP5Fo0CJRg7787f6MvYrwD_6wZFQsy1W1B1RSklNovgZVLw-hHPlcx3DE-8U2HMmEggLA6ChKuE7D6-dwJrN-QhInxKX5YAspVZCFCThyFnlGhjJ1Ef49wk96ZtXjDF60E2IiZHcC3zON7QW1aVglg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3tr2RfA1-m3fscnXVoRZ63j65hHZk-9r6MJ03bRY5ARuq1bkZJQ91fm2LIzKd5IhX3vJlNeHDbEIpEt3f4fmd1HyLIa2vZ2E-ZYlYzzfmmKRvXxZ8vfDNG8dTJapPecCA7PFWhJTMgMSOEtJtj9D8ezyV0a2KrI0CRt_udtS0WdHirwIoh9LwpUFfFVF29cemIsFmoc94SI3AOzZOWpE9U5MXTiBsOPncpe5WOmPVO8WcQLfw86G9wImpvJ-jUboNgf06Kwx9Na8W3DNSm-rYw54hyYrgvdkqvwcGdNa5cL_iIRAxl96w11E3ekeoh7qXDolBaS6sO8sRFwGN8Szg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCq9dzIyw-AGYGKJ4SpCtmjpmdt74bHQmWSZygikBG0ydqh7fVJypDmKMKDsoncp91gEjYkzRYaEonBIeVvom8CPaAZbrO8kwo2g3GTCT60c2y3aBMg1X0cdNxXFxtig1SxIcqAsz5ajv3H8T6F9MYN2iNSfKKNGBNzJbmc2r0bFBhMu_Pqayme4S_tHd-vJByRyCpAzGimiQF2hxXVd3Ds5jrc5P_r7AgM90kyClQUSmg3Cnv-bNzMKtzM8bUw0NswCqq7Uvy04O5PDl2DEl7GLK_EyBzJUc2cg9Y7y34SvrNGoxCkp0h8jrrP3pAujXF2NQVex9CjhF9Iege51bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F04-5Kh4g_U2PDwui9f_uCGVRVf1aih73S69gsEPRQ3MmKjI39FB-Hav9XEldY3nm5Deo5an0flBHqYWZHhkGxjWiaki6BxaJaoH5jvO1m55z_CniwvIu8HN4_7sM7a9Np-f-sFq_MDnpGwKiCZ1tu_6YccHOnyc-Ncbu_wMLAM5W2eFmB4RRjaS6gPk-08FeVHuF85A0YzXsogQHpXigR2PIFz6A0WtsykeA2ExAJtiHFqQ3KgzIwvIWa-TduxXt3LPylxM-xRG8wnC-ioRkIDf06U2emK4FNXucBVoJlnn2kNMGUOLHfGDg_DGRnNeiYz2k-4gC-AG2ri9KnNcyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBiR9Cqtxr095mWlOpytBXrb4ME_nIF2yjvn7-IW4izj7D7Bm4nAPsdXIFCn7KzgSAFx_18LxX0czHR8e4RxZZFqTmpSSS3fLJmceWWrX6kKre7VKp1G1KHDlRKHZyrauGn7OxtvtIbgIMfEucOwhrw0W2BcVe24LmHvbp2IUWMZrPCDnig3szU3VI4Fkim63OdgMIkd3r-2Kr7ROAZvt1DtwM96cmt0Js-ZVR_rZZmwSo-lqOgPJjUNqWR6xjikQ5JUDapWQoRwJzjzOw5QfwVDdOeaSwAcYvur6XCbqLVIz3ZV2vFwfDXeG6W-WqdEARzQbc7Ysibd7fGcZi8Q_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
اسکیل‌های Gemini برای همه رایگان شد
‏⠀
‏گوگل قابلیت اسکیل‌ها را که قبلاً فقط برای کاربران پولی بود برای حساب‌های رایگان هم باز کرد.
‏⠀
‏
🫧
با اسلش در کادر چت، دستورهای سفارشی‌ات را سریع صدا بزن
‏
🫧
جم‌هایی که ساخته‌ای حفظ می‌مانند و از ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند
‏
🫧
فعلاً برای حساب‌های شخصی بالای ۱۸ سال است و انتشارش تدریجی پیش می‌رود
‏⠀
‏اسکیل‌ها نسخهٔ ارتقایافتهٔ جم‌ها هستند؛ به‌جای گشتن در فهرست بلند، کافی است در کادر چت اسلش بزنی و دستور دلخواه را انتخاب کنی. گوگل می‌گوید جم‌های قدیمی‌ات هم در مهاجرت ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند.
‏انتشار هنوز برای همه کامل نشده و ممکن است دکمهٔ ساخت اسکیل را نبینی؛ چند روز دیگر دوباره سر بزن. ساخت اسکیل به حساب گوگل وصل است و حواست به داده‌هایی که وارد چت می‌کنی باشد.
‏⠀
‏برای چه کاری اولین اسکیلت را می‌سازی؟
👇
‏⠀
‏
📌
صفحهٔ ساخت اسکیل
‏
🌐
گزارش نئووین
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/up7rAk9lGI8N9KPiHjdNWipuXaGiX7BpL52ivYRGvDvMuDfUeYoscrsb2Xdf0RVcB5SD3VKic-NXAviEFjNpaDRKzh5oTAPu9NNkdDqgyTiVFtDAPQlu2MjIPZA0Kzoj5jo-CuzrhrP8ZjFZSime95aXbLq4mI9jKU99ErRKfTslyi02EB-AtyOKZPytanucceHJRsWzmBypqV93LFfgqcdcAOpMn1a3GyAgaxUE_uf-XcajT_NXLjvkwYOp9_9Ckj_ex_bjmXfOg6sz5HVJ4O_6Qjem6yYiYdarOv6Y-qlzf5TuESuYs46vpmQRGdWR_cCY-4RC4V_g9FbGZL6AJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
حل قطعی مشکل باز نشدن Gemini در پنل 3x-ui (ارور ریجن و لوکیشن)
خیلی‌هامون این روزا با ارور رو اعصاب "Unsupported Country" تو جمینای درگیریم.
داستان چیه؟ گوگل آی‌پی‌های دیتاسنتر و IPv4 وارپ رو شناسایی و بلاک کرده.
😀
راه‌حل قطعی:
باید ترافیک گوگل رو از یک
IPv6 تمیز وارپ
عبور بدیم و برای کانکت شدن خود وارپ، endpoint رو به صورت
آی‌پی عددی
بنویسیم.
بریم سراغ آموزش قدم‌به‌قدم:
👇
قدم اول: تنظیمات خفن Outbound وارپ
تو پنل 3x-ui برید بخش Outbounds، یه اوت warp بسازید  و اضافه کنید، بعدش روی ویرایش کلیک کنید
🧪
سه تا فوت کوزه‌گری مهم
تو بخش ویرایش:
۱. حتماً تو قسمت
endpoint
از آی‌پی عددی (
162.159.192.1:2408
) استفاده کنید، نه دامنه!
۲. حتماً
domainStrategy
رو روی
ForceIPv6v4
بذارید تا ترافیکتون برای گوگل فوق‌العاده تمیز بشه.
۳. مقدار
mtu
رو بذارید روی
1280
که پکت‌لاست ندید.
آخرشم بلدین دیگه تو Routing rules بزنین کل سرور از اوت باند warp رد شه
هسته و پنل رو یه دور ریستارت کنید اعمال شه.
🚀
بفرست برای اون رفیقت که سرورش تو جمینای بلاک شده!
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚀
شرکت OpenAI از "داتس" (Dots) رونمایی کرد، دستیارهای هوش مصنوعی شخصی‌سازی‌شده که در ChatGPT در دسترس خواهند بود.
آنچه تا کنون می‌دانیم:
🫧
با استفاده از فناوری Astra!
🫧
داتس می‌تواند در انجام وظایف طولانی به کار خود ادامه دهد.
🫧
احتمالاً فقط در طرح‌های Pro 200 در دسترس خواهد بود.
🫧
از مکالمات صوتی پشتیبانی می‌کند.
🫧
دارای یک ماشین مجازی (VM) اختصاصی در فضای ابری است.
🫧
کاربران از امروز با یک داتس شروع خواهند کرد.
🫧
به زودی از طریق پیام‌رسان‌ها قابل دسترسی خواهد بود.
🫧
از بیش از 4000 اتصال (کانکتور) پشتیبانی می‌کند.
🫧
بسیار قابل تنظیم است!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mbOcYB4tcZ5oWBKWmJJbLGMhu5AU80wtDueFqkhS6OJIZcVvvOuPYzlbupBRxSSrt5a7m2Eo1GUxKv4HN1ns94c4ZtunIlxMudaykU-3kf-QMfHNUamI8M6TpURQxezQtKqx-Cjpys7yRYClxYoemq2EAHAs9j_odo5kCrLK2xLhNNdERE_82PL5p6UTL9xYi72mB-QlQ4s35zYkrXFvvLugoEWTVVlcbf2TXbn7iKytzljDu73rZho6cgjGLijzny8KCaEyLnuNYwdGtCEDpOEDekG4wteIvVbD1YEwG6IMc920RH4H0e1y-GODW9I2PpI6q8v4xv31K4u_7AAitQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C4-z3KBj3GuoKferz5J3Daff2zMYN7gupBW5EreXz07ey9tBBotUEmO4IYOGihwN978qhgF1ynOBiN10FiSJ6Tn56eWYKVHMWqlM9FWEA0rF8agehmV5FNaw5sHGgbw0GiOzdZy4Cu4Jr555HcoGOauNQ5gX87vtJUsVKy6A32AG_b8JIG0z9bGzIoYtyeXl5Wi09qrBHvxKcjOxNjJciJIf8k3H2FGJzkYAovJKBvNIiVQPocRQjDs7T9AwNFq1RVn_s29tXhwHiqzX_FrXXmKcx73NwpPjds_0Fqc93LjU4pDVwUs9RQvNp5Ku8UlLysJzNhMAszBVBaWPkTxVDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kIiDsHrchSa7oRqaqLWOISYVWwwnVEgBdMVjdLbtiekB4GN9EfLJyfP-Qwt0RK7AU4VjjMttsrinp5KpRxTv6g9jT2wmI2EuOmqLWaCtMt1fq2wIV1zZav0OOXEGD2jmlLUAa8hUcaPnj_yvV37UKwZT3sdZrMRMcuH4ukoJJT0R35h90ULTQdN0Ul3Xhc9WlI4b9RfzQIxBTmi3f64-CAdLW2q9lZyyakEzrIVQe0yzrh4nb4oMMmSZYBARv2MR_U5iV2KQ21JPOzEi_SP-vOWjAdcSpX0MhW4cb4bGHp-ddaxEuUemSbd0Et5zdNT0cBf-EBNB3v9EkcgtUv0bmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmkOQU9inFrXqR11qC_M4HwnsR7b_LOtPllxRF_K9oWUkfz0FQDDJb7S5Rzaw6_YFH2OZvY06mPEXARDDHCyoEocFCdRgGvxs6CiLhDjrzhdDWfjlurPjl-XRMlla0JtFRs6OWSog_XAYuw4Fyl3onZ1KSoU3BSMc4ySSaY4yTPq5olbGejnbhAI9oErYLVtI77wNzHrYabLo4Pl9uh9Ohgjwz3hqYxMX9Ka7FNo4_ZbEILSKdDUO76ge6i1h2bTPieVmZbijflMGoT72hViiAcIkkpTVRbUpiuEHAlvBy210AGupIIda_YT0my6sssW8wgUwBBQH_Ay_iTDz3nSYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/De0a7jaTcQ0AwdsPBvBJuRBeZLnWmQU1DagE95XG9fzLx_ntYhCAJZYthpXZ9pSbvZ39wuSaCTkHhr5nXVeahK_Z3xaJBjgP4FM90XJ-yvNpXdpGqxO3WWd6X_5vt9nuhll-rdplItonnF8YM66T-VgaHMsbyS6BhmVaMqEhuofCHg0eXz9lyyx8qsBpHtzLGPh-3E5vtCDFb35zB8SdN_pEtEJXNXP95I_W--kow-OPRbrNBUCxZmt9IjFMBThBBC3AsqNTV6ufVRw6z6c6WCDzaynJN9AU2ruWXDyW5q2Ida_qiUIXr5-8Lpw4wRD2lrjc8-tMjluKVbofConVPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsQWkfv3vFHxAM-geMA_zfg39k00QKE0lSwTLSiOC5yM8dwZyE6ks7Ontd5XbakKQCHLycFg_7rlan01KXE8G7Cd0XobcoxBJcihQflyhzSAiAQOI-8nimgOIf3FX9uDu5kcy8p1ZfePFcMVzd4AJTzC2YJiGVp_r8zMPso1-pzB-NxjaSxRrfjG0FU6sVZp917HhzVBPd0UegDlav1a3ZgJ38fPCcqJhHC5EcypcM7Pjnc_47g6sQR8s6in9fZUIs7n5B1GjfzMW5_0RPOo_ikL_UTGM8X-qjV8xhLKriSMvP_fPTWwzDly3kdRQw7NmUuRNnm-ZlT-R1Q4Qg73Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awQzkdPrUUgKDc6ww40IiXMTDzpmnMaks2u0KP84o30qVAUIdueQKpdYGogV5qDMFfiXWz1LRvxFmwPCsU7_mlVunl58t5K3iQtT6lTmcloXXZfLBDVCYkiZNnZwKzyKrH0sFvui6lf4EgQ3wK6LbJ6LH4fNdhACPcjCUz3dwz84Lhui-RX767-M0I5pUjALzcEkymzUUB03fbTElyp86sgfHU2UuUQyYKYhq-9Yeip8w2K0wqFEtBlE_duslMzaTGDn45nvpvv2J2C09acRK_9OkomshlXLl38cAphs53mnp-vTN72brgWm-tjigFst2HzuXnMMZcJ6aar2qS5l-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Relapse – PS5 Jailbreak Exploit
🎮
یک زنجیره
Exploit
با نام
Relapse
برای
Jailbreak
کردن
PS5
منتشر شده که
Firmware
های
7.00
تا
13.60
را هدف قرار می‌دهد
🎯
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyuTld9uJLNRgZATsgvBDU6IMqTkw_CEKkI2wcPb1e8X8Xosk7JysPo8v_UF-L1KY55-NBALlVIbFqoac8kgkB7JJXNt31IckLvedK7Qs5VT26ilV5xzRuTXrAKq-63Q9RoVkdHVimQVFGrfuvLCLHKSM9auCTzyYm0wW_HXwOP0XHveFkTEA9jummz4E7_Ju4dLPbS-fWk16wBRSDKGzzbfZAr2J4CD-8nifqYcJEXmLQFY7YsezuXFWwYNR0mGq7yUVoqVBlbAml3lv75byu6v-kc1NX7djZzpoIF0k22oDw9UluT2IEF-VFJ04-woIMlcQcNBjNoRVUARpD6Q6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های زیر
💥
🆓
Opus 5 | Opus 4.8
✅
با این سایت میتونید 100 دلار API برای مدل های بالا دریافت کنید
✅
⚙
پیش‌نیاز ها :
اکانت گیتهاب 1 ساله + یک اکانت دیسکورد
💵
هزینه مدل ها :
ورودی 2 دلار خروجی 10 دلار بابت هر میلیون توکن
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBdVLYX0Td_7pUdkX9JRmKAnfCj7fuZ5UvbJOkl8sorS5NYP_RDbjKwcAYNRRGXvST8P8Lz61bKKaIahXa4CG-MuFtU8YklB2N3l99lU3Q6hyvV9jx0Uv6hq17VNcEsko4fEdIpXggM5H43NzT6ZeSYBT4QaVKzkyPIzt4CzT3JG7VVg8mR4ebL2jCHFOeVGM9HAwq6Z3Y8aEzQwIhDb6hD8y9w7-s8t4rz-3B4a7rSPiMzKAxysVD5uDHoHMIiYn5FOheUiSozfZpsdHyIykbfE7zsXzN9QXw2JMDKx1GH7oDPtoucT9VtPZhVC3rEmkajynUxZJ-IrnNPB-ESDDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلودر دسکتاپی deviload برای یوتیوب
⠀
‏یه برنامهٔ دسکتاپی که yt-dlp رو پشت یک رابط گرافیکی ساده می‌ذاره و دانلود رو به چند کلیک کم می‌کنه.
⠀
‏
🎬
دانلود ویدیو در MP4/MKV/WebM و صدای MP3 و FLAC با انتخاب کیفیت
‏
📃
پلی‌لیست، زیرنویس، SponsorBlock و تفکیک بر اساس چپترها
‏
📺
ضبط پخش زنده و رصد کانال‌ها برای دانلود خودکار موارد تازه
‏
🎛
ادیتور Devil Cut برای برش، ترنزیشن، سرعت و تغییر نسبت تصویر
‏
🔄
کانورتر با هدف حجم مشخص برای دیسکورد و واتساپ و ایمیل
‏
📱
فرستادن فایل به گوشی با اسکن QR روی شبکهٔ محلی
⠀
‏لاگین یوتیوب و اینستاگرام داخل خود برنامه انجام می‌شه و کوکی‌ها همون‌جا می‌مونه. صف دانلود تا ۸ مورد هم‌زمان می‌گیره و خطاها رو خودش دوباره امتحان می‌کنه.
⠀
‏با Rust و Tauri نوشته شده، yt-dlp و FFmpeg همراهشه، تلمتری نمی‌فرسته و رایگانه. ویندوز نسخهٔ اصلیه و مک و لینوکس هم بیلد دارن.
⠀
‌‏
🐱
مخزن پروژه
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏
🧠
اکوسیستم GLM و راه‌ های رایگان استفاده
⠀
‏مدل GLM 5.3 شرکت
Z.ai
حالا یه اکوسیستم کامل داره از جمله چت، کدنویسی، ایجنت و API
⠀
‏
🧩
روی همون بیس GLM 5.2 سوار شده و همه پیشرفتش از پست‌ ترینینگ اومده
‏ به گفته خود سازنده، بهترین مدل اوپن‌ ویت برای کدنویسی و ۵۰٪ جلوتر از نسخه قبل
‏
🪟
کانتکست تا یک میلیون توکن و ۷۵۳ میلیارد پارامتر
‏
✅
صدرنشین بنچمارک
CyberGym
در کشف آسیب‌پذیری با نمره ۸۴٫۵
‏
💸
قیمت رسمی هر میلیون توکن: ۱٫۴ دلار ورودی و ۴٫۴ دلار خروجی
⠀
‏
⭐️
برای تست بدون هزینه،
NVIDIA
Build
همین مدل رو با کانتکست یک‌میلیونی و endpoint سازگار با OpenAI می‌ده
روی API خود
Z.ai
هم مدل‌های
GLM-4.7 Flash
و
GLM 4.5
Flash
و
GLM 4.6V Flash
همیشه رایگان هستن و وزن‌های خانواده
GLM
روی هاگینگ‌ فیس منتشر می‌شه
💥
⠀
‏
📝
معرفی رسمی GLM 5.3
‏
📊
قیمت‌ها و مدل‌های رایگان
‏
🟢
تست رایگان در NVIDIA Build
‏
📥
وزن‌ها روی هاگینگ‌ فیس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EApwKRXabLSDay3zv-YFE4qlYEih8UB83sfRTdSu7G0q6xmlmIPBEsVnSWQeSy5vKNQD_lvA6q8VUhaDyRIn4Lgc3DwlZSCNe2Rani7yfUOhmoAPopO4gyyAMphIP_RryuabHS5wuEbQtymDpvl3fBvlr1e-yq2-YEoctMi7tWf_UkxBbntxRJPff_kWNlE9xbTYgHNxN5g33qSaAWyByh23Mr1NrR6lihHHofmJGWOWdjjFOoeSkiunoTepLPvnonPyfkdvZiIfXo7ZOABkcAtMugmBPR288DC_bbr8KV48_JmNm7zO2DDdx9gA_GU1_0OGdZrtltgP21azQb8V7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QPiJ958upHnS4LwQoSz1Xy0G5MUdHsNmTCrLyuwE7lSDhELeAyx3f3bDB7aZ12JtrTxaI9NJGbOGCwCqQpLF8T6OdnHgHrT2PIkKlKuXHD-7Ya4BBU0LLXA1k02GvRCMWiinxlkpeEaRjvqQvxK2FDTZOlgt_4kcoSYUuvRWfbAt3j-lH08i7zxdnTPG6eJT2zdoZauK7GC7dkIHUN8VVStxuf1hzgLuUw1e5U011u5yJJd2E2NFC2xEcwP7lnvLp72tSfA2neE_o4AF-MTCYukqd0GVAsPO9tzP9nLOfI39Ry5Ds28lFug5397PkSt3rIpIW2ZfALgiWmSRHKhoIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E6UaYwEy_qB4rWw2LbhrF4-R8UudW5JH_z-fX1VjuiaIRQsE_sBZOT8vQ_rxWh7trvuxT8nPHroELbULRcO_x_Qs0xsKE9z-HBIYBUoX0TaDASo9Bqw4PBwuj5tSK-gJP6lB8jUrtWRLtaOs8jb0e_bBhePhYarFYiKIsSgIR8dD4THp50qWU2WZyuib38aI3nQJvyfw_BpJaAuDl_qFwwTptUBih8eS1J8-Pkcj3jlw0nmTybSOsCELWcxRN3O99o6CHLplhu_7SBk89J70hGVPQmx9xh52r1QQPhHur7kL1HDrw-gthwTnfd3e9JIJIygtgxu9hY-RQhH9U5nh9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIBpkvubS90AwF7xAfFWHHCt9Z18xSSc1VwpPmpcf9w3iE6HPwGlOSsSSsxCJ3E9lHgbdj3751mYhrTUlJbuaQybk4vT8Tt4AG5nEWmw5S3Pwf3_hTrQv86Xkd5hXg5guvbfuxgy3HQTvEKLYsEndbfUqTL0s2Ijk2SvwxNEYiLPyD0po_iVBA-CJ_S0sq_qYuTzYehzR2LAR-Z3FUk80C_AJr954Hw4Z-tARr7sk0meQlVE2GXgDQGjraxW87ClYvjiu_uF-lk2gPjW--GPcSKrdHvt9rTW58ULDwOrxPIV_cnVflZKFbQ9CpPTA37rqYg_UvQLw1M-sxu9xcyEEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aU22JqJF3lZER3QTci5WfmBvOBSnwace5_kD-zk2F6yIyDTCTf9iO_sEgm98k0fNM4NuvenYlHVyHt9AQZzPw4ZynV0jjPppuRxrulU1F-da1OsFDFvzliX6iEmJ7eKFRSmVve4uD8ks6IuEf84vOAVUhIBWGUIqHNLq7C99NadD91RbUiJ4h6fWU5ZaC82QUw7RmjBMkvBQgxibrqf3m7yQjD1i2o4KPuzVe_ziDGA-5fmrdg4KcDh-LamGSImJINs_10eDeZefrzJmLAykYpe2o-1uUNS-8MN-bky8Bw_p3hJ7f1sxKbB9PinCpf2dhLxJEbMaX6VW45GIjf41hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiIwVrAL3GEXm45_2NUbkOcOifLVbiAWWW7FShykaLx35wBgSEuLrQta20bRsFcv7g_6wze762HnCpwdxGHs7T-QX-iL0n6LteW7TX8cbRWx3DwZijiaA-i5wFMsGXx_UfV1alfWoyqJOfemu30b_YGu7f9LV7EcEeBbZGjvxCiHYUWfl9yV46YAtZP5NuNlzfZ_P1_68tICp00uw-kJpfSg517uP6hOoWUKoeal89nNdnFpIOb3z77cU_MoS4UOPQNmFJ5b-PyG8On3c3PBYebKjsCr9mDze6AZefLDyC5yzbsbjsBs50So_BY4d_Pfc5VOGMsw75SPrIj0kjloAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RacjlOQAj2EyKcWXqyIKxboZvhzoBnlt9TD1cWhGJyBs6X_-jGcvhX5CPxLWTacQ5KNfh8GFoRva4hwWXqayuCAUTUsVd_ZMJAsVJMllcYwpIL9bRDWmXU2e1Lzce-8dU-wv82JAEclsR7aD15yYyJ525QqxOQuOQpYCWC93t6wnT0D71V5SRB8xlOl3710wjjDvhCS_8cdZ_Kz6q5wZ4Y-_qaoeedxK9-KM576fZeHFANpU0f-FIgYXnwxEf2NdI67jkULXcczgHgsS5MNXkIWo2PruvSNqiEZDzFnqrXnGCoJh-ZOSz2F3tgFSutIzJc2k8wo0vBwvWJ9IHeSFyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_-SqbdXSxYp4QkvdWGgY998UZEBOqZvY6_OKJ9lgnoWOG2czrl-uQTROh0A8N84Oql5J0-WXyvG0q6qJ1Sw6FdXsaWk-JcPDpOLe1hDcx5GCbpBjPhUUWWLPRejAxz3CCsBduE4-O2EvEd7bOp_GOKlO9ocY92Ifc-JlcyrRkz5OVP1ZbyCgA4ty3JHQqIQCC6022XCi7d5N_jB4OR9UcKC9Jsr9c0FtWw13S_YKOgqMGqeD0ore4glmPsasospDpQhz-hjmBPoiMBIPeP31rsjRIvOMf8aWLJHNOaVTf4z8sla-JApMlhwTlIZppKzofEhtVktagxG8OwprXamSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fP6EdEtF9RBSbqA3KHmD2Wbe1fOyBmcsuV_A5l8LexISDCiCTU5FXBVCHaaLYZwA5kEwGcQpRrOdjDkAVZMDXOBPNEJritXJzZwOnXIvAVhbFe0s8xD48JooPHCqT1OBpuboSRfyeLv2lLOMsyUAYu7YXbzlnDr0nIeF8BdoI402rE87b0TCQ2EWXvGn_gBN-w3WfIBbsy7tYff0kfwB7zAJN6850INih0D2qKbVv2cjGOo3AY_whOXHyQKjQfXCG3aD1UAcQzlXjzsL04MTFez6q10zYhBJW-uE2PG0qcQiOY7aJbsNrlCzBfGNg9-nMrdjEKN59hUuA0-LP_OAcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
ادعای نشت اطلاعات کاربران صرافی والکس
⠀
‏لیک‌فا، سامانهٔ ردیابی نشت اطلاعات ایرانیان، از دیده‌شدن حدود ۷۵۰ هزار رکورد از داده‌های کاربران والکس خبر داده.
⠀
‏
🗂
داده‌ها مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱ عنوان شده
‏
🪪
نام، شماره ملی، تاریخ تولد، تلفن، آدرس، ایمیل و مدارک احراز هویت
‏
🏦
شماره کارت، شبا و مشخصات صاحب حساب
‏
👛
آدرس و موجودی کیف‌پول‌های رمزارزی
‏
🤓
حساب کارکنان و بخشی از داده‌های سامانه‌های داخلی
⠀
‏این مجموعه تو فهرست فروشنده‌های دیتابیس غیرمجاز دیده شده و لیک‌فا می‌گه نمونه‌ای ازش رو بررسی کرده و صحت داده‌ها تأیید شده. والکس تا این لحظه واکنش رسمی نشون نداده.
⠀
‏اگه اون سال‌ها تو والکس حساب داشتید، کارت بانکی قدیمی‌تون رو تعویض کنید، ورود دومرحله‌ای رو روشن نگه دارید و مراقب تماس و پیام و لینک مشکوک باشید.
⠀
‏
🔎
جستجوی نشت اطلاعات خودتون
‏
📝
فهرست نشت‌های ثبت‌شده
‏
🌐
سایت رسمی والکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYL69HSBn0W9O4mtwVzomL1E7rvOAB9LoH1j075gIqJmrBkw_rSyhAtVbZMJBs8mYFatacFs8KzSk0tsQSbxsjFLWJVzzzgfdzyUQ0DgoEX2MNioOBsZwQWrZEKXs5c94ZlEBZCbSnfDfzXy0jHcdVOsbRuELa11c1oDOs5ZChi29RFnG0mvd5o4pcd1nKpf6SaMIcm8NW4SXUuE1YKJku8wQdrPyIXZvBP4pFAqsqT1PRDujfgu9l-BjKMJQc8Mg2T4VrQKRBxTbyOPCw8TdJtLmFNcibnT1Enqifq7tCKbbd1l0NZSmU1s62rDEuoRQWg27cQQjYqiXJacZiwHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎬
اسکرین رکورد با Recordly و ادیت خودکار
⠀
‏یه اسکرین رکوردر دسکتاپ که خودش لحظه‌های مهم رو پیدا می‌کنه و روشون زوم می‌ده.
⠀
‏
💻
نصب روی macOS 14.0+‏، ویندوز 10 نسخهٔ 19041+ و لینوکس با محدودیت
‏
🪄
زوم خودکار از حرکت کرسر، اسموث شدن حرکت، موشن بلور و افکت کلیک
‏
📷
وبکم شناور با تنظیم جا، گردی، سایه و زوم واکنشی
‏
🎛
تایم‌لاین با کات، ناحیهٔ زوم و اسپید، متن و عکس و شکل
‏
📤
اکسپورت MP4 و GIF با کنترل کیفیت و فریم و سایز
‏
🧩
سیستم پلاگین با مارکت جداگانه
⠀
‏بک‌گراند و گرادینت و پدینگ و سایزهای آمادهٔ شبکه‌های اجتماعی هم داره، یعنی ویدیوی آموزشی رو بدون ابزار جانبی تحویل می‌گیری.
⠀⠀
‏
🐙
مخزن اصلی در گیت‌هاب
‏
🌐
سایت رسمی
‏
📥
نسخه‌های آمادهٔ دانلود
‏
🧩
مارکت پلاگین‌ها
⠀
‎
✈️
@ArchiveTel
l</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwZCPEK3z-EkUcKpVOrrmHw46DsFNv5kQFJTmMXaPPsy3RfluHBlDfykXXXjDUkp3ZoLk1feDB6VnfWrhrWE0sYJnaXZF89gIzGF0hq1GclgycRkNuh_Q3TAaF8y1fW9IUwpm5BvF4aYZKxtn0uIg0vN4MlsJo4Jge96rJ05IcUDdBxNVApyyOsVY3K2C0xQ7ZKQbTo8gR6J10nSJv1hNX5f1tfhkK3pJGBX3VVecVRIp5QGr8BQ5cc_TePu72uqnFJIjifPDxDKqWq3WdblLYQTLoF0TXAQ-EdsQ3rQkRRnLPI54nL8B1_Q-krAbIw0WUgwFmP4enKFsgMlZZY8bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به بهترین مدل های جهان برای چت کردن
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این سایت میتونید یک تریال ۵ روزه بگیرید تا با نسخه اصلی این مدل های بسیار قدرتمند در درون سایت چت کنید
✅
این سایت یک ویژگی دیگه هم داره ، شما میتونید با مدل های GPT Image 2.5 Flare و GPT Image 2.5 Sunburst تصویر بسازید
🚀
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=u6-zKgnfqF7vrBMOMJe43OE3JXuuBHJBXefEdsgAW3wbipTQMWs0bvh7tJSscsc4KcNlx9KTEa33b8G4V2zPEmcOgLtYPRIr4lNPIqvxyDeCUlQWg9mi_m5kxN27eCHh8vwK1emZUxsFuu75_ICZ5VUpMo5EfyJllcebpaFtUj36J0fiH9Fdrbccxp7rO6YPxHr79V1NhtsucMZw7sFtAaYRqcdrC8TdiPYPR_f6e6OYaOdzMSpZGEkBk2kKwlNe-807Vv4Ls7uz02mcyQHrT4jgezkmDSx9nkxAy9U8x8tUpaJqhkn_QGV0Z6_QdYEWFtC-lb1AXppv3A1OQHHbMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=u6-zKgnfqF7vrBMOMJe43OE3JXuuBHJBXefEdsgAW3wbipTQMWs0bvh7tJSscsc4KcNlx9KTEa33b8G4V2zPEmcOgLtYPRIr4lNPIqvxyDeCUlQWg9mi_m5kxN27eCHh8vwK1emZUxsFuu75_ICZ5VUpMo5EfyJllcebpaFtUj36J0fiH9Fdrbccxp7rO6YPxHr79V1NhtsucMZw7sFtAaYRqcdrC8TdiPYPR_f6e6OYaOdzMSpZGEkBk2kKwlNe-807Vv4Ls7uz02mcyQHrT4jgezkmDSx9nkxAy9U8x8tUpaJqhkn_QGV0Z6_QdYEWFtC-lb1AXppv3A1OQHHbMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
کتابخونهٔ رایگان Melies برای تکنیک‌های سینمایی
یک کتابخونهٔ آنلاین با ۴۲۴ تکنیک سینمایی، از حرکت دوربین تا نورپردازی و رنگ، هر کدوم با پرامپت آماده.
هر تکنیک شامل:
🔍
تعریف ساده
🎭
اثرش روی حس فیلم
🎥
مثال ویدیویی
✍️
پرامپت آماده برای کپی
این مجموعه رایگانه و نیازی به ثبت‌نام نداره، ولی خود سایت Melies یه سرویس ساخت فیلم و ویدیوی هوش مصنوعی هم داره که پولیه.
اگه دنبال اینی که یه حس یا نمای خاص رو توی ذهنت داری ولی نمی‌دونی چطور توصیفش کنی، این کتابخونه دقیقاً برای همینه.
📌
کتابخونهٔ تکنیک‌های سینمایی
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SC3EHjKFwbIeJ1l88QrQAhpccHWdDqaE7qdH9h_Zfi1fH8vRm2MZ9yql1NW6QNvOHP53IAp9B8UJRwxaHndfKXa6Rd76p904MRkLnNCfjzmiXed0OUJ3cXpDP3Dcl3H2WhyqsiiVJ9IuDXJ_7IvvNLeHaUCIx7GTQmA3Di-Q1X6s6RyzqbZGSkZCg4-1bE91XkAL-xCw4UOkvXPffOah_36Dr8stmeY7gbkf09bGDaYjNHsetkr0PfFcQsMkXoUOwmpmUc7j_LPkxsVdUKU2dPFn0Xxlm6XPCTmyHyQYFJldmpL1-JgZ3fthrqAi1u5Wkj35z8vP7cQDNkIVF0XP2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🆕
مدل MiniMax M3.1-Flash-Preview بی‌صدا منتشر شد
⠀
‏مینی‌مکس مدل سریع تازه‌اش را فقط داخل MiniMax Code فعال کرده، نه روی API عمومی.
⠀
‏
⚡️
ساخته شده برای کار روزمرهٔ کدنویسی، از رفع باگ سریع تا پیاده‌سازی یک قابلیت کامل
‏
🎛
در انتخاب‌گر مدلِ MiniMax Code کنار M3 و M2.7 نشسته و حالا گزینهٔ پیش‌فرضه
‏
🎁
ورود روزانه ۴۰۰ پوینت می‌ده و روزهای چهارم و هفتم ۱۰۰۰ پوینت؛ یک هفتهٔ کامل ۴۰۰۰ پوینت
‏
⏳
پوینت‌ها ۳۰ روز اعتبار دارن و روی کدنویسی و سند و تصویر و صدا و ویدیو خرج می‌شن
⠀
‏قیمت و سرعت خودِ این مدل رسمی اعلام نشده؛ عدد ۱۰۰ توکن در ثانیه در مستندات برای M3 ثبت شده. روی API عمومی هم M3 با تخفیف دائمی ۵۰ درصد، هر میلیون توکن ورودی ۰.۳۰ و خروجی ۱.۲۰ دلار حساب می‌شه.
⠀
‏به گفتهٔ PANews از ۲۸ سپتامبر تا ۷ اکتبر اعتبار ورود روزانه دو برابر می‌شه و سهمیهٔ Token Plan هم ریست شده.
⠀⠀
‏
🟢
ورود به MiniMax Code
‏
📝
سند پوینت‌ها و اعتبار
‏
💵
تعرفهٔ پرداخت به‌مصرف
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8b_sh2DascSraRhQniJ0KMPPzIglmDOsR9gnK7y9l4ZCXo4L0DxUrsTlU5R8v3YaQCr2mMp2-51BeOq0sXAhlDKB_RvxoXsf8g4HFae2kWSlYAc6ivvHdqXnOA45V3ILAGBp_6OspPc-S8u-1lDDHl9kf8dWa5Z6AEh4C8onat3thERfqTffebGRx_yFh8z4kUFNk2CVHg2n6Rh8aj1GhifMa-q2RHquJXDK50BV75B8cfdoGJIOV1eQ0wAA5tcmkrPDDmLr9cozFtoiAZIDlgePrtxJXxOKcnAbEAGtDr6ogDcFROwtUR1-ZTXpscFSdq0PAl-zkEtP8AnVl89tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Railway.new
یک VM لینوکسی رایگان در فضای ابری
💻
از حالا railway یک ماشین مجازی لینوکسی به شما ارائه میده که از طریق SSH میتونید بهش وصل بشید
💥
برای استارتش فقط کافیه داخل ترمینال خودتون دستور زیر رو وارد کنید
⌨️
ssh railway.new
⚙
مشخصاتی که این VM در اختیارتون میزاره :
• ۲
هسته پردازشی
• ۲ گیگابایت RAM
• محیط لینوکس
• دسترسی SSH
• Python
• Node.js
• Git و GitHub CLI
• Chromium و Playwright
• Railway CLI
• چندین ابزار AI برای کدنویسی
🤖
بخش جذاب ماجرا چیه ؟
چند
AI Coding Agent
هم از قبل روی محیط آماده شده‌اند؛ بنابراین می‌توانی
Agent
را اجرا کنی، پروژه‌ات رو به اون بدی و داخل همان VM کدنویسی و اجرای پروژه را انجام بدی
⚡️
🌐
برای پروژه‌هایی که اجرا می‌کنی، امکان ایجاد
Preview
آنلاین هم وجود دارد
👎
تنها عیبی که داره :
شما فقط 60 دقیقه فرصت دارید ازش استفاده کنید ، وقتی 60 دقیقه شما تموم میشه به شما 24 ساعت فرصت این رو میده که فایل های که باهاش ساختید رو claim کنید تا در ادامه بتونید ازش استفاده کنید
❕
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXx-Riww0v15qZwhxGNUYruWaOCm66eW-oM1OdSQJKcTIWIYR8WHDiR3ZTkXNI7A9dIc1ipFk0idnKEKql2lbcbk3lh3pr1Lba6mjdDUA5m7zB3wXLP8JfLrK3vBQek34XIOTgue7hlMfQWiyM2z3IBFbhvEbjVpdLh3pVN_8Y8akF1DF0rYK9feFRddxpEi04oHZqt6hWAE5bmZ5wINBOpCUUrDZyKvfAj1quWlgoi1tjGnpZkC80wcxIfFM1-ooquXVwepyZmIy9wCRPv2hcpnT0pHqCk54lTL0wiKzM3SrginJNrcFC00UUUiCjWmGD2tkZ2liND5u5P-HXbFsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#حمایتی
‏
🏔
آرشیو Afsaneha برای افسانه‌های محلی ایران
⠀
‏یک سایت متن‌باز که افسانه‌های شهر و روستای هر کسی را با نام خودش ثبت می‌کنه.
⠀
‏
🗺
نقشهٔ استانی ایران با SVG خالص؛ روی هر استان بزنی افسانه‌هایش میاد
‏
📨
ثبت افسانه بدون حساب گیت‌هاب؛ فرم سایت با Cloudflare Worker خودش Pull Request باز می‌کنه
‏
🗄
هر افسانه یک فایل Markdown در پوشهٔ استان خودشه، پس با رفتن سایت هم آرشیو می‌مونه
‏
🎙
پشتیبانی از فایل صوتی برای روایت با لهجهٔ محلی
‏
📱
نسخهٔ PWA و حالت آفلاین، دو زبانه با چیدمان راست‌چین و چپ‌چین
‏
📖
حالت مطالعهٔ بی‌حاشیه و تم‌های فصلی مثل شب یلدا
⠀
‏فعلاً فقط سه افسانهٔ نمونه از تهران و فارس و کرمانشاه روی سایت هست و نویسندهٔ همه‌شان «نمونه»ست؛ یعنی آرشیو تازه راه افتاده و جای افسانه‌های واقعی خالیه.
⠀
‏
👇
اولین افسانه‌ای که از شهر خودت شنیدی چی بود؟ همینطور شما اسپوف‌نژاد؟
😊
⠀
‏
🌐
سایت افسانه‌ها
‏
📌
فرم ثبت افسانهٔ جدید
‏
🐱
مخزن پروژه در گیت‌هاب
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IF0w-3SuygGLaE7FyTfx6DksqXk628Tr057m9a3qXFBB4c_OarmrV6zUfBTE_3gPwiM8t-J-u2_SJmtjBn7F5ZeAaRAUkeBBDf_FqvmAzDXxTcJ9StCky-9TgNKassx4Hm4afp_lrK3no-6wm0_7ubE7agqySmuuN18LRoeIzrDBrpjMnw1B0Cd1339HpK3zYWR8P-5KVCQfJUymGhB44jBxN82pAd3BjTAUuI6v8BTEZGrNa-rwn5ZTmbQV2IDJCwZCOSm0dyvBypZ4igyKJUsQI4_ChCDNc2lo-PefwuqhcQ4zXSRiPYiJ3r0ueq-tbEgMWR5E3349alp6E2ZvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API برترین مدل های جهان
💥
Opus 5.5 | Fable 5.1 |  GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 Pro 0813 | Sonnet 5 | Gemini 3.6 Falsh
✅
با این سایت میتونید ۵ میلیون توکن بابت تست مدل های بالا دریافت کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6YQiDQavm31bP7kBJ5w1AeujMrOgyq34hR1biFP_ta_6Oz39Ay7uAEjVRsdeC5g08U8zCgLipMNjL1he6J0YkrhKYSLZB_6AtzZAaWbaQawCAXF1ZRNXpd5MEajgsvaXQ--hEri_X4nimMdlAln6LEbYsKFqDIZK8PPz-lxpeLakIDc1bdCiRn6gqVUomFVMppmwQ2wtYq41Hf3SQ9n7zhvMnR2XMFIpKXfqJz2BRJKVVj1vBth7yRsDowp8VItoJHI8OhjwJqa37qrlU4NAVgC9FCUGdrBju7a4ItCBkJojnxRa4I_WoEV16HgHi7hUPOE-f1EGgUPCslH7JoIfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل‌های هوش مصنوعی زیر
💥
🆓
Opus 5 | Sonnet 5 | GPT 5.5
✅
این سایت بهتون یک پلن تریال ۱۴ روزه حاوی ۲۰۰۰ کریدیت میده تا شما بتونید این مدل هارو استفاده کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3q40tFt_TAdgC4hp0qFJEeketdShFoMW7DrAUdeLjDtW979WV9LmeOyax4jDuWJ1oxYIWLaOLgwZAs_0d2X4ASa4PMI_PZKfrVbwuyJ9FQzAxPxJQZA5q3HJrYOAYGCzMfcUuJygeC6w84R9hTmt00SOSHW8iz0NAoAebY-SEkVX7M62wiAsLo5Kq1dDpCyn8AUG69T1_gO_c41bwgqE1XO5CWxYR59dcA6GneDdWAgXW5cbIeL9g6e-h9b3Lm5DYzxJ2Nvn-3Jsab1i22_Yqjaq7Rnk_TC5NlxICx-g14WbJSY-Leu47SJgcM88Ojm-QZwwrH5ynJ6gn4Hg-iQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
ادعای نشت اطلاعات JumpJump هنوز تأییدنشده
⠀
تصویر فروش دیتابیس کاربران این فیلترشکن دست به دست شد، ولی هیچ منبع مستقلی پشتش نیست.
⠀
💳
شمارهٔ کارت ۶۰۳۷۹۹۱۲۳۴۵۶۷۸۹۰ آزمون Luhn را رد میکنه
🏦
پیش شمارهٔ ۶۰۳۷۹۹ مال بانک ملیه، ولی زیر شماره اسم Bank Mellat اومده
⠀
آزمون Luhn یک حساب ساده: رقمهای یکی در میان را دو برابر و همه را جمع می‌کنی و جواب کارت واقعی بر ۱۰ بخش‌پذیره؛ اینجا ۷۷ درمیاد، پس شماره ساختار درستی نداره. ساعت ۹:۴۱ و محو بودن دادهها هم نشانهٔ قوی ماکاپ بودنه، نه مدرک قطعی جعل.
⠀
اندیشه معاصر نوشت هیچ منبع مستقلی اصالت دیتابیس را تأیید نکرده و شرکت ادعا را بی اساس خونده. بررسی Tom's Guide هم سابقهٔ نشتی پیدا نکرده، ولی ۴۸ از ۱۰۰ داده: سیاست لاگ مبهم و بدون بررسی امنیتی مستقل.
⠀
پس ترجیحاً از سرویس های بررسی شده استفاده کنید و اطلاعات کارت را داخل فیلترشکن وارد نکنید.
⠀
📌
گزارش اندیشه معاصر دربارهٔ این ادعا
🌐
بررسی Tom's Guide از این فیلترشکن
🏦
جدول پیش شمارهٔ کارت بانکهای ایران
⠀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nef8OGoKYnKWyb5g1hItek4Txa7XVXAv0W-G6fsyF7tTCxneUM_hJiFU5onTL3fZAp_unQs-xJ6fg6oJlVFomHO73vkXzTBTso0ulWWebTmtL8FmrvJ5syQP4OmnerHmo_brPK4EFs_xSbBgsmf3xsErd6QhLCA6piv39zb6WDkfo8CF2RPBtsXnvdXTi3vFW54cfzUfuF3Lrm7vVgYSbaQnldJpNUI9yFX_L8QzrJMjPurW5llHceUVxY2h6uTfSb2xP-X3HSPcupRF4s8oWZThGuQFA5kJvj_gMDr7FgQXQRytpVYId7zIHUMGLJEXBAg1aLjVTSTyd9eBL_k4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های SI در یک بنچمارک سلامت روان، از پزشکان متخصص امتیاز بالاتری گرفتن
‼️
- اپن OpenAI نتایج یک بنچمارک جدید در حوزه سلامت روان منتشر کرده که توی اون، چند مدل پیشرفته هوش مصنوعی تونستن امتیاز بالاتری از پاسخ‌های نوشته‌ شده توسط متخصصان سلامت روان کسب کنن.
🤖
مدل GPT-6 Astra: ۵۷.۳
💠
مدلClaude Opus 5.5: ۵۲.۴
✨
پاسخ متخصصان: ۳۸.۵
- البته جالبه که متخصصان بالینی در واقع جریمه‌های کمتری دریافت کردن. طبق توضیح OpenAI، دلیل پایین‌تر بودن امتیازشون تا حد زیادی این بوده که مثل زمانی که واقعا با یک مراجعه‌کننده روبه‌رو هستن، خیلی کوتاه جواب می‌دادن؛ گاهی حتی فقط با یک سؤال یا یک جمله.
😁
- در مقابل، مدل‌های AI پاسخ‌های مفصل‌تر و کامل‌تری تولید کرده‌اند و همین باعث شده در این بنچمارک امتیاز بالاتری بگیرند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7ThWMlNx3nRo-jK87uZn1Oj1cwHplMsZy8NbLiQiP3Ra3oA46RJnYlIsxUlCDl4zz3xi8YdPBflHJMXlxBlBguSK-iqoXR4psI4vj2tBJhlDdylQ9BaPJn-ZuxSXNahJsHWBKgE2dYfO6ulJkQo-eYV6aPwg9IJm9tfssUX9Wv7y8QrOYBpdNefGA9QnRd4gRDWIWGfVrHU_J1U1khSLcwDPAdmjCpdcRz9Ihwsm_CIbMW42W9bGQ6LkDtgn_Tn9nmwL6W7BO5S6peznm851k47KVU-I3d_T7uhLomJB_5eHR5YUEH1FKVevidVleQxsGTdSrKm2I0WUNWXY6clIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
مهساNG ویروس نیست — ماجرای اون عکس چیه؟
چند روزه یه عکس از مقالهٔ MVPNalyzer دست‌به‌دست می‌شه و می‌گن «مهساNG ۳ تا از ۵ لایهٔ امنیتی رو رد نکرده». مقاله رو کامل خوندیم؛ اینطور نیست.
اول از همه:
این مقاله اصلاً بدافزار بررسی نکرده. فقط رفتار شبکه‌ای ۲۸۱ تا VPN رایگان گوگل‌پلی رو سنجیده. پس «ویروسه یا نه» اصلاً موضوعش نبوده.
دوم، اون ۳ تا اشتباهه — ۲ تاست:
تو جدول مقاله، «Leak (29)» و «DNS Leak (24)» یه ماژول‌ان؛ دومی زیرمجموعهٔ اولیه. کسی که شمرده، یه ایراد رو دوبار حساب کرده.
واقعیت از ۵ ماژول مقاله:
❌
ترافیک رمزنگاری‌نشده
❌
نشت DNS
✅
نشت ترافیک کاربر — پاکه
✅
قابل‌شناسایی بودن (۱۴۳ اپ گیر کردن) — پاکه
✅
ردیابی و Advertising ID (۷۶ اپ گیر کردن) — پاکه
✅
کانفیگ ناامن OpenVPN (۱۰۷ اپ گیر کردن) — پاکه، چون اصلاً Xray استفاده می‌کنه
یعنی نسبت به بقیهٔ دیتاست، جزو بهتراست نه بدترا.
اون ۲ تا ایراد یعنی چی؟
🔹
نشت DNS: محتوای مرورت رمزنگاری‌شده می‌مونه، ولی ISP می‌بینه چه سایت‌هایی رو باز می‌کنی. برای فیلترشکن ایراد جدیه.
🔹
ترافیک cleartext: مال خودِ اپه (مثلاً گرفتن لوکیشن از
ip-api.com
)، نه ترافیک مرور تو.
یه نکتهٔ مهم:
داده‌ها مال نوامبر ۲۰۲۴ و با تنظیمات پیش‌فرضه. اپ از اون موقع بارها آپدیت شده و نویسنده‌ها هم ایرادها رو به توسعه‌دهنده گزارش دادن.
✅
کاری که باید بکنی:
۱. بعد اتصال،
dnsleaktest.com
رو چک کن؛ نشت داشت، DoH یا Remote DNS رو روشن کن.
۲. سرورها دست آدمای ناشناسه — بانکداری و اکانت حساس روش انجام نده.
۳. خطر واقعی، APK تقلبیه. فقط از گوگل‌پلی یا گیت‌هاب رسمی نصب کن.
💡
و یه حرف با کانالای عزیز: ترسوندن مردم ممبر میاره، ولی اعتبار نمی‌سازه. وقتی یه مقالهٔ علمی رو نخونده تیتر می‌کنی، به همون کاربری ضربه می‌زنی که ادعا داری ازش مراقبت می‌کنی.
اصالت مهم‌تر از ویوئه.
پستتم ریپلای نمیکنم. اینکه خودت اپلیکیشن مود شده خودتو میذاری چنل معلومه چقدر به فکر پرایوسی و ترکر هستی.
📌
فایل کامل مقاله
🌐
صفحهٔ مقاله در NDSS
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyhJPwrElCmwfGgOq317nPkEiONjyUwQP6mN1uhPsZZU6x2xFu9GEIXTscww6w0VeSiwQjYn7IVJVFlLnf3o4aNpHWz0l_JAC5ggWt3jmmHvw0S9R_B7jQbkuoIJx68DN6ErYSRnQrBVVI6eb2trjsZtld_j8laQhNJhR2zBV0ilhkJefmAQ05IxBHWhORace9TRNLk9WeTXXTkhB6y4pL0xKiKSGTFy3-MCmYfNeq4RIDDdc9cuQq_8EqtBDjCsl1k1TxFlihImTutwxsgC9bZR_PgQfUujr_7z_zZDasbAStoQclEldgD-BSV50rznV_HQdq1F6ss4PWOyanIP0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">500 دلار برای دسترسی رایگان به برترین مدل های جهان
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این متد میتونید از سایت معرفی شده ۵۰۰ دلار برای ۱ ماه برای تست بسیاری از مدل ها دریافت کنید
✅
📌
دیدن آموزش فعالسازی
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4WB9D6ekuP3XIi16yUVQpQOgXcSE7er9qhebRoqUVpe9Ew8bi9OauXmLWZzJgoiQBB-Ti3YmI3nxnNyroTCj6NnS2QbaXf4bpeDtfhaIwsMGbZJac7TIv_Id3Iv7uhLDmuqQ35eEswCYyW0WvbEpgo7K7YuEywVJ7xtlq7ZTTOUL01PCZrZgoabYrGKf543K7cgz_qUV-b5DZLK_T1rZHFkXSaKPpVzmhXQqQFMdVxcUr6z6wNTdDiWnUzUUI3TbZfxuPeKBNje6Qxh5S-zyvwlg4Z0OdCqa5Jvi1jiO2CdDHRF7NO7qMzZNTDAMQ5NBsXRk_1zQ8Zg4L-BTcvsHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkuO1zMO-HqXRyg5qxH7_WTr8VtfUdBBhjkPVYu-F41D9-K8xe6hmvThza5pN4bkiC1z08SBBELxCPR8_1xXlH5xAex19QGRWWmgX0hcdTCfsVSbi2s65l4n9h8kSoDhfenLWbf5z6CxrLcVnVx1MEwOSof2bLLT1DN7N6MMjPaX3UHLhNn3nYquVBWQEFycqXJ-ljDPth6eVdtbO5Bz0Yz1kWc7NUK7yVj2aJgCB7gU94kaBvUtqyHotakgIpRWnPo1VWn42VapLsZMjPvsJbz73fUVyo9M2lo2hBCQLbYUaayVpZ-yPVFgLR-qvEWcTSZigGjvj7tx1jUtwBpHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌈
کنترل نور قطعات با FullRGB بدون نصب
برنامهٔ FullRGB نورپردازی قطعات رایانه را با یک فایل اجرایی و بدون دسترسی ادمین کنترل می‌کند.
🤔
۱۲ افکت
: کالیبراسیون جداگانه برای هر زون نوری
🤔
پوشش قطعات
: مادربرد، رم، خنک‌کننده‌ها و فن‌ها
🤔
دوزبانه
: رابط انگلیسی و فارسی
🤔
فقط ویندوز
: نسخه‌ای برای لینوکس یا مک اعلام نشده
💡
نکته
: موتور OpenRGB داخل همان فایل تعبیه شده و نصب جداگانه نمی‌خواهد
📌
صفحهٔ پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFlPvMc-ME6NQbjE8CB1ox_YAAc1evVAN6rW53_TUHdCUnaLCX3vG32Dvv2stFUn12zwlGKJ_SWdvevYqDKYbhXuTV6Zh4sutyAoY6ZkXTPC2ummq9F_zD8xmT2CuLmMQF4d81jrSDWIi3ZMAT8kjB-H-JXUNpNF3taezNWNBzvisfgRDdEkbJgeQUisYgprXVkJSWGpOXC-vK4eunXAF-C05X6foO7LZ1K7ahT1GdnPtg0MHGmwIavllx_AkzKU3NfGlQt9ziQmK0Uo3AHMJupkrYyPQtQpyLUXB4WSbN2OWhIYGkd6rfrGlz036AqeNBgvMpiB55aJpqyx-FneoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧩
#حمایت
| پچ راست‌چین هوشمند آنتی‌گراویتی؛ خوراک بچه‌های برنامه‌نویس!
‏رفقایی که از آنتی گراویتی استفاده میکنن این ابزار خیلی کارشون رو راه می‌اندازه تا بتونن فارسی رو درست و حسابی و راست‌به‌چپ بنویسن بدون اینکه کدهای انگلیسی‌شون به هم بریزه.
‏•
🧠
هوش مصنوعی دوزبانه: با فرمول نسبت ۷۰ درصدی حروف، متن‌های فارسی رو راست‌چین می‌کنه و کدهای ‌LTR⁩ رو دست‌نزده نگه می‌داره.
‏•
📦
فونت‌های ۱۰۰٪ آفلاین: وزیرمتن، شبنم، ساحل و صمیم به صورت ‌Base64⁩ تعبیه شدن و منتظر اینترنت نمی‌مونن.
‏•
🛡️
امنیت کامل کدها: پنل‌های ادیتور، ترمینال و لاگ‌ها کاملاً سالم و چپ‌به‌چپ باقی می‌مونن.
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sr0qARX7dAaH9bQ5yPI5N2KY5MH3q2hAPu17sm11r-jxTkoec3khY265SEvoV64ZmucZ1PoBOf_Vf_ZTkG0XuXtHqsBXhG3fa5_CZeoLD6vdsZGk5axzbLpjTaPPcaRU_fDSJv8ETCkKbKQYfFGwSK6YLIyQLFPvXx3XKGmdTirHAmE8wxZqToClPpcw_wREK-34HJOVavUyd_1qBboSDykUGpRsYRgmgN5dfV9e3ilOe-yh30fkr1ORbQNACJSJYxb2QWlO79VULOik0xsvKna9AyPf1p_EAQO3igA6wgtLZOcojNv5apX0cyC5_vXcOdVDUidZw-ZPwD98Z0rVGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HS8hECLLYbZwVsfY6RVN2DJ0BwqMhJRBJX3qlt4uoqjsiTZ6DpHKKr5rGmEsG_lLBd62ZuTg9yCFPe6Taxv1mkXroZp5_j_gIqPbTf8yYzgsEYvenpoYB3w3Mswql6S8CkLchd4YWoKkwQWhij0HHtBRUcJOMV7lqUJKJjA_lJBqjsn28TiCSw_edrQRaNMWuZ5gFerYvg2CuILfuqy-COQx5pei0NKVF2TPpR58fBtF1VF_ULEn9Cc5TvbNsO074UqUqPh6XATnQbBVCk3wjhpYkANJbwvh6Br7jSzgA-cKsHlJeHdx-fjhYOtQpnIp9Yg7rBLTdNih-i7cjZ1wAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
در
یافت رایگان ایمیل دانشجویی اسپانیا
با این روش می‌تونید یک
ایمیل دانشجویی اسپانیایی
به‌صورت رایگان دریافت کنید و از اون برای
وریفای برخی سایت‌ها و پلتفرم‌ها
استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell
| METHOD</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
نکته مهم برای کاربرای Antigravity
اگه اکانتی که باهاش کار می‌کنید عضو یک
Family
باشه، حواستون به این موضوع باشه:
لیمیتتون در حالت فمیلی، به‌صورت
اشتراکی
بین تمام اعضا محاسبه می‌شه. به این معنی که اگر فقط یکی از اعضای فمیلی مصرفش پر بشه و لیمیت بخوره، کل اعضای اون فمیلی هم‌زمان لیمیت می‌شن و دسترسی‌شون محدود می‌شه!
💡
پیشنهاد:
برای جلوگیری از این مشکل، حتماً از اکانت‌های مستقل و خارج از فمیلی برای Antigravity استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ox7m7yfELdieeLBH-Qy0HKgDnHtbT-TsOVmQKhX_VU75YUt4dsv27NHHghNWnCPnOfX9d4yb7QjdsYA5twqt4cdKO7XXaqsBsi0if-pfpXM40BaDHV1QwdSI7G_VXYCvK2UbYiaZRiLuX0EJjWxTXWFp153QiZkGpF0ruHcPXESgheIQiIswILwu1dBwuiCaDsEr7ZGFM6oEkD9tnrOTsgXho_FiurFsMaYivWWq2m8qZguTa7tLjHqHfvrkRi0ZkvgrFgVtHqRsk5_e8eUnh5Bp0Shup3eZ7-PHWMK3C8JduntJTqLqIB7iaTNLSkA9bXpwLLJehKqz_YhpmiVlLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
طوفان جدید گوگل، جمینای ۴ به زودی...
💎
کوری کاووکچوغلو، از مدیران ارشد و مغزهای متفکر گوگل دیپ‌مایند، بالاخره سکوت رو شکست و تایم‌لاین اس آی به شدت مورد انتظار
Gemini 4
رو فاش کرد!
🤯
اگه فکر می‌کردید هوش مصنوعی تا الان پیشرفت کرده، کمربندها رو ببندید چون گوگل قراره بازی رو کلاً عوض کنه.
⚡️
چرا این خبر مثل بمب صدا کرده؟
🤔
پرش کوانتومی در منطق:
جمنای ۴ فقط یک آپدیت ساده نیست؛ قراره مرزهای استدلال و پردازش داده‌ها رو به طرز وحشتناکی جابجا کنه.
🤔
تیر خلاص به رقبا:
با این تایم‌لاینی که DeepMind منتشر کرده، گوگل رسماً شمشیر رو برای بقیه غول‌های هوش مصنوعی از رو بسته تا بازار رو کاملاً قبضه کنه.
🤔
یکپارچگی بی‌سابقه:
حدس زده میشه که این نسخه خیلی عمیق‌تر از همیشه با زندگی روزمره و اکوسیستم ابزارهای ما ترکیب بشه.
نانو بنانا ۲.۵
هم احتمالا باش عرضه بشه شایعات میگن
۱ اکتبر
میاد تقریبا یه هفته بعد
👇
به نظرتون Gemini 4 می‌تونه رقباش رو برای همیشه کیش و مات کنه؟ نظرتو تو کامنت‌ها بگو!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7869" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7868">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzfpKY7wCQRHAawG47KoiwWFAAdgp3JzO0ot4rNRZ-eTA57xKMMuYE5lmgxoVKrdYPwT-dM5MLVGoUhE9Pe_7O-t1yddvVTGIzGCNSTu6K7t3cFObm5eRoBC-OWvYvnmELR1EsDaxE6JEC0Lsoc4mtcChVrFrIsKnpdPbZnmEtsE6wmKXQCzDyGUNui6x0H4VVHc5uN0B7uf-0JxKfvIZv9DrI3DZE6qM0aXwvDegV5tEL-32sWmEtYGtFgxw54halmYOUwHcvy-ZCb7M4r2EXfu9h1BT1U9cjdMizYXqbF26av8EaMRoFxb3sV6XtpFRXp7g_joP9UPLFZC0OBsuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت
| کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی
به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک
: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
داوری میان گزینه‌ها
: چند راهکار یا مسیر پیشنهادی را می‌سنجد و برنده را می‌گوید
🤔
شکستن حلقهٔ تکرار
: وقتی دستیار یک کار شکست‌خورده را تکرار می‌کند، متوقفش می‌کند
🤔
نیاز به کلید پولی
: هر میلیارد توکن ورودی ۴۲ دلار و نصب با پایتون
💡
نکته
: مجوز MIT برای خود کتابخانه است، نه سرویس پولی TypeSafe پشت آن
این پروژه یکی از ممبر های چنل هستش.
جهت ارسال پروژه هاتون به دایرکت پیام بدید
❤️
📌
سورس پروژه در گیت‌هاب
🌐
راهنمای رسمی فارسی پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7868" target="_blank">📅 18:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7867">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awjb9j2JXe1VskkvvBee4w7NOhr-GpZiof7GzDanDSiUMbhWn7Ha6dEHCGPG6y8elrk19KoHAv0PkVS6XRkQEJcAaUkbiFlpVE7DU0jTW68e8xiWxsc_dAadBh_xouuSy2GZNLlFPd5vRL4pq-idlZgu5WmcTIlD5TUzdmZhMdxGaaNluBqk6fLk0LQY6Ki87myp8c8aW1FlOH9ndkfZzeV1ysYOL9v2EH5oOrgmgzj0PvQfMhbn2sTznLav_Pijyyh--iRLOWxa5q_fA6Av5jdf4SX5-cimJiR-hZmwCKN8WuC7frR5pP2QhZD27YHVSXkgwk2JjF08mhFnfB1xOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
ابزار Perfect Windows 11 برای بهینه‌سازی برگشت‌پذیر ویندوز
با دسترسی مدیر روی ویندوز ۱۱ اجرا می‌شود و از یک منو هر بهینه‌سازی را جدا روشن یا خاموش می‌کنید.
🔺
بستن ردیابی و تبلیغات
: تله‌متری، جمع‌آوری داده و تبلیغات نوار وظیفه خاموش می‌شوند
🔺
پیش‌نمایش پیش از اعمال
: فهرست تغییرها را ببینید، بعد اعمال یا بازگردانی کنید
🔺
پشتیبان‌گیری خودکار
: نقطهٔ بازگردانی ویندوز و نسخهٔ پشتیبان رجیستری ساخته می‌شود
🔺
خاموش‌کردن هایبرنیت
: فضای دیسک آزاد می‌شود ولی راه‌اندازی سریع ویندوز از کار می‌افتد
💡
نکته
: مجوز MIT دارد؛ استفادهٔ تجاری با نگه‌داشتن اعلان حق‌نشر و متن مجوز مجاز است
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7867" target="_blank">📅 16:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7866">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbkSwuZUNivh4U3302dE0EbVKxSkKoYK639itNUtYOuVKmuxnBJvRqTyXACEG_j-Z5PmIBvi_bRfl3l6x2GQjnfulWnBGA6UWjHX2x3ysc2m_HsPmh6galx9k_DFvFV0g6JiP58dnnoFmgjnrPnv9Hgxn3rP2JriHygTvzxcMJsKS5WIMlbYqSnJqmIVY7NfY_xIBk92ZY4CterQsv9ZvJ_ksBwn0VCoboP1AauzGG0_CxW9qf-IMfiRjO82GEholUUQGoBpkxYMDjTPd4Nv_hFRg9g15TYBTECqKLX8CvirIaPGmHxLR1zbzIdQyQTZ6mII2sbx9Jd6wvj36QQ9DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧮
مدل Laya که به‌جای نوشتن جواب، تصمیم می‌گیرد
یک ایمیل و چند پرسش می‌دهید و برای هرکدام گزینه، نمره یا بله و خیر با احتمال می‌گیرید.
🤔
پاسخ در ۳۳ میلی‌ثانیه
: زمان اندازه‌گیری‌شده برای یک پرسش روی کارت گرافیک
🤔
بیش از ۱۰۰ زبان
: خودش زبان متن را می‌شناسد و مدل مناسب را برمی‌گزیند
🤔
دانلود مدل و اجرای محلی
: بعد از نخستین دانلود، روی دستگاه خودتان کار می‌کند
🤔
نیاز به پایتون ۳٫۱۰ یا بالاتر
: با دستور
pip install laya
نصب می‌شود
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری با نگه‌داشتن متن مجوز و اعلان‌ها مجاز است
📌
اجرای زندهٔ نمونه در مرورگر
🌐
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7866" target="_blank">📅 13:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7859">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iD4nHxkMHTjp0SG7jVJB94C0pgBN31VqgeuYnOwwNvk7vCXF1J6VuLjY_HwlwY0os8h5dlTIaEJqFUrFvMJzsewTgqn2PEOKI3C7H6nugrcvWozC_beq5yo7MKyaE_-jyluvaNrEIrNVfJ7RgVhTQUEWYPa9fB1g16m2U2_HRKGpWa3t4rnfWAhk3C8yL-qPBxIRDIQgiPFzzSBC-BTAUK6p5jGMEF0tN54z5dKPkadCInQGHov11YnhIaSOFQGxW3LLyLYvM1T-CL8_WAizNuHVrZ8IKUtPrgMB1dWeWgycf7DQEaytwMcfzk5LSSQXAOgmVsl_eaTlxiZP-KaX3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K50zOlio3hG-0m-SnGZVZukRJmido9WWyVbafnwqQU2BFFu9h--qKtKqKpzgMInOvS07_fi4NFf7P-iCzy5FOCT9rVRuXGNn5CZneYclYDbeRLjfx7sSreTZj3RzuETa5lVtZ6IVo5aB-zml95hqgV_3zmvzlVhy0DBfGqzA-YGLqZdq2TpRoOYQDcEWYm8oiXE0Sj9d9wztSeRHEWRpdaO-WhUVw33BTzmOSdxJfqi-It2hmVqlEiVEqm-UFbQCOiuSAIWF5_sMZeC_ACSE0mRxUvGVVS_fkgUia0FF25F4OQLSBqJmRocxQr_ZDTLrhXMaIpXGp4tjr8VvxFCOaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YrMbW5nwuxEEdLllZvoaOexOuorSqPlxz2s4JuZYoLDCbmaL3I4qQ7UTahZ5iSSiBzm6xwTAtSC9PfeDSL4P2_LaLdgBvI73NrV4HwULWttEUZzHEp8_SaPq60V4Gqcws-1wn1cxVRdsgMYFiGMBot_EQNa4qVdr29ueYzixS3EIEuwtVJy6nICeVn13B_wZVHabJy60KgxClHTarzUHpZXtQY8WNKjr-RQVUua2fr21do-afdPi2PnQIg-pDo4lRI9sNDqaNtURPzVP1LQkYZN9M988-YBWcv3T1M5CfBr-pkolZPwxjet59MT5SYY1lnkmc9nhEPRqkGEBeNESaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=eoITJoEUpOV-jWddpHUAQrzXjCZfDfdOQT6OX-iakVMldTyig6VcQjarjxxgXN9j7P8BaE-kXlisKNcQXm_J4mhKjB5oKYZRmiUXVmgtIDVfkRGXlhaJJQs7L4C_xkaQCf8ueTPSUPHinSenvhsSwEXfbyxaOOoK8Ow9zQrbDNVPDfZ1ikBHGCkGuNDI_cc0aoHwxNqR1l18leX8pczDVZoME51_OL150h5ajGMsbERO1-WhHlBioDW4yjAWa_BKMH3kcg0AkWTYsImXHFdPpXPiGyHrLdi2gcJxV6egHzhBNfSPFRCVApRvv3BMnkxfAzUYTSgS_cZzuqgZv3ULuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=eoITJoEUpOV-jWddpHUAQrzXjCZfDfdOQT6OX-iakVMldTyig6VcQjarjxxgXN9j7P8BaE-kXlisKNcQXm_J4mhKjB5oKYZRmiUXVmgtIDVfkRGXlhaJJQs7L4C_xkaQCf8ueTPSUPHinSenvhsSwEXfbyxaOOoK8Ow9zQrbDNVPDfZ1ikBHGCkGuNDI_cc0aoHwxNqR1l18leX8pczDVZoME51_OL150h5ajGMsbERO1-WhHlBioDW4yjAWa_BKMH3kcg0AkWTYsImXHFdPpXPiGyHrLdi2gcJxV6egHzhBNfSPFRCVApRvv3BMnkxfAzUYTSgS_cZzuqgZv3ULuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
مدل مخفی Space Bunny Alpha رایگان شد
مدل مخفی Space Bunny Alpha اکنون روی OpenRouter و OpenCode در دسترس است و فعلاً رایگان ارائه می‌شود.
🔺
پنجرهٔ متن تا ۱ میلیون توکن و خروجی حداکثر ۵۲۴ هزار توکن
🔺
پردازش ورودی متن، تصویر و ویدیو با تلاش استدلالی قابل تنظیم
💡
نکته
: رایگان‌بودن این مدل روی OpenCode فقط برای مدتی محدود اعلام شده
📌
صفحهٔ مدل در
OpenRouter
🌐
مستندات رسمی
OpenCode
✈️
@ArchiveTell
#Ai
#هوش_مصنوعی</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7859" target="_blank">📅 22:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7858">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvwvD9WBbq58LIUTTP8IRL63rBDMbqW1h8-kFJcUO63KHWW82JyvtOo-EbDGXZ4Ehupf86udD0euzAPiJ2qJKIYQovifu1DgCtStXptGd3SX7uSSQzhTOu_PJGyjqpK_sfdjCFG5mKH4KRppwxszY0NAZbcEYWVKrONgJZ-KdA4ULjYA7orxesvI5A3yyDhHyAzoQIVFQaTGTiuo84xQMOWq_FbOpYU8dK-uTKwRO6EffHmNJqJNa3TQ_Nuda-LNJjiN5zr39KvYZpCtk5afOcuD40wYbEDiXiC0KQcQ46EMIPMq8jJzda0_510-0WIa2QBYjbqnPljzIKeC1iKjnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام دوباره یه قابلیت جذاب اضافه کرده
💥
🔥
حالا وقتی وارد پروفایل کسی می‌شین، بالای صفحه می‌تونین ببینین شخص معمولاً چقدر طول میکشه تا جواب پیام هارو بده
🥵
حتی یه رتبه‌بندی هم نشون می‌ده که سرعت جواب‌دادنشون نسبت به بقیه چطوره
🤐
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/ArchiveTell/7858" target="_blank">📅 20:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7857">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSccgjbh0NCCK9a7656oeftMak3QgYuGMZmwSpNHKfO5qC1XzXm3D_5qldiJ2sxxVFcgUPuIiWQXnLnssktjucshA-RwdRCSird7yPmu34Qce5Cwim8fn0vehfjLUhBC_f_IKovoAvr51aainQHeKGB48C9DX8AEi2XpN8z0TvGwLceF6i4E-O1aZ5ZxnHmm9QyUKA9XRwihuCUJe4iPajqmQErNLVWL_FxduiRQS4Ir2hPrPGy4WQeYBxBnWAk1QIGJqIdd1oYQIIAPaYRrRzY-VqxUEAmM0aXOd5jdu0ZYJfVMwE0KMDqexoYCVbiTzlxo0Us8di0p_1z9OpdpOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✈️
نرم‌افزار TeleDrive برای تبدیل تلگرام به فضای ابری شخصی
فایل‌های شما را در یک کانال خصوصی ذخیره می‌کند و ویدیوهای ۲۰ گیگابایتی را یکپارچه نشان می‌دهد.
🔺
پخش مستقیم رسانه
: ویدیو و صدا را بدون نیاز به دانلود کامل پخش می‌کند
🔺
رمزنگاری انتخابی
: نام فایل‌ها، محتوا و پوشه‌ها را با استاندارد AES-256 قفل می‌کند
🔺
همگام‌سازی آفلاین
: فهرست فایل‌ها روی دستگاه می‌ماند تا جست‌وجو بدون اینترنت کار کند
🔺
نیاز به کلید API
: برای اجرا باید شناسه و هش شخصی تلگرامتان را بدهید
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری با حفظ متن مجوز و اعلان‌ها مجاز است
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7857" target="_blank">📅 16:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7856">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7856" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7854">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YArutFjFWZS6Jgihyep_EEx0VC-SzxrY1wHdEIHcvMa30tkJvL7tuPxhzA1xu0U0jq7XmfPVcwB6Oa8oNWYf-DMhKJHJhC9OyyQ_fWZW5q0RdE1Fpx9ggcGaBq7xgXv5a-t1kSzukpflq0DRYp7GInjFyz-d8DTBlWd6YuKGRrda65FU_ZnkGpmklLpUPF0fLNuys2dERyMw10BnFTgF3FiQ1xKd0spZLJ94HH1qbwBwstctp_SEAZva7XW7KsjHvNDHoeiUUZsl3mM9_hVLr6UofWhsKsYCmSfTGUz1VfPLrpsyvsh3Nn-9Ki9csZzeigdBu3_ZLRXFeIPPQP-YKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7854" target="_blank">📅 12:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7853">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7852">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7852" target="_blank">📅 10:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7849">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=Ae2ccs-rE9_t4OODHy9lPyGrusnBaunbfJitYobzB6AHwf4ZxwFh8m-UMEs5lwBc-_HhvFM0wLOk8QSkBHyzkA4nZG9GBVSIRgvlurUTl_DpOXqb4X7z70Pb5tD-Bw4zaxTCRFjVVyKXFv1H-AMMz03PapfCQZ6vaNmSV1K2cbQaW30-kszy-ZkvzFwuyqnLmZvlgJhXmjf05OO1-u-97AiOK2zur_05hcKOH08YkSa-bL134kEKkf_vWhZxpbgEP_HPdH7DtRHcijajNb0W2ozle4ZsEnHW2o8KdPQyLJRyNODdowjiXb-6wUj8mpcolpnp0g-jaZ3OPUmC1licyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=Ae2ccs-rE9_t4OODHy9lPyGrusnBaunbfJitYobzB6AHwf4ZxwFh8m-UMEs5lwBc-_HhvFM0wLOk8QSkBHyzkA4nZG9GBVSIRgvlurUTl_DpOXqb4X7z70Pb5tD-Bw4zaxTCRFjVVyKXFv1H-AMMz03PapfCQZ6vaNmSV1K2cbQaW30-kszy-ZkvzFwuyqnLmZvlgJhXmjf05OO1-u-97AiOK2zur_05hcKOH08YkSa-bL134kEKkf_vWhZxpbgEP_HPdH7DtRHcijajNb0W2ozle4ZsEnHW2o8KdPQyLJRyNODdowjiXb-6wUj8mpcolpnp0g-jaZ3OPUmC1licyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦀
کلاد Opus 5.5 می‌تواند انیمیشن‌هایی را از کد تولید کند.
کافی است موضوع را توصیف کنید و از آن بخواهید از پایتون یا جاوا اسکریپت استفاده کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7849" target="_blank">📅 10:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7848">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">چند API رایگان LLM که شاید کمتر شنیده باشید
🆓
💥
اگر به دنبال API رایگان برای مدل‌های زبانی هستید، چند گزینه کمترشناخته‌شده وجود دارد که در حال حاضر دسترسی جالبی ارائه می‌دهند.
🚀
🔺
Atria
بعد از ثبت‌نام، 100 میلیون توکن رایگان در اختیار حساب قرار می‌گیرد. مدل Atria-Dawn-Preview با کانتکست 256K و حدود 50 درخواست در دقیقه در دسترس است.
🔺
Routeway
چند مدل رایگان بدون نیاز به شارژ حساب ارائه می‌شود. سهمیه فعلی شامل 5 درخواست در دقیقه و 200 درخواست در روز است.
🔺
Selora
یک پلن رایگان 14 روزه با مدل‌هایی مثل Claude، GPT و Kimi دارد. سقف استفاده 30 درخواست در دقیقه و حداکثر 5 دلار اعتبار در هر 4 ساعت است.
🔺
ShareLLM
120 درخواست در 5 ساعت و 600 درخواست در هفته ارائه می‌کند و مجموعه متنوعی از مدل‌های GPT، Gemini، Kimi، Qwen و... در دسترس است.
🔺
Vireonix
بدون ثبت‌نام و API Key قابل استفاده است. یک route به نام "auto" دارد و طبق محدودیت اعلام‌شده، تا 20 میلیون توکن ورودی در ساعت ارائه می‌کند.
🔺
OdiRouter
مجموعه‌ای از route های "free-*" برای مدل‌هایی مثل Claude، Gemini، Qwen و MiniMax دارد. البته پایداری مدل‌ها یکسان نیست و بعضی مسیرها ممکن است با خطا مواجه شوند.
📌
جمع‌بندی:
برای تست API، پروژه‌های شخصی و ساخت نمونه‌های اولیه، این سرویس‌ها می‌توانند گزینه‌های جالبی باشند. Atria از نظر حجم توکن، ShareLLM از نظر تنوع مدل‌ها و Vireonix از نظر عدم نیاز به ثبت‌نام، ویژگی‌های قابل‌توجهی دارند.
✅
⚠️
سهمیه، مدل‌ها و محدودیت سرویس‌های رایگان ممکن است تغییر کنند؛ بنابراین قبل از استفاده جدی، اطلاعات به‌روز هر سرویس را بررسی کنید.
﻿
✈️
@ArchiveTell
|
#API
#AI</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7848" target="_blank">📅 23:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7847">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSuycu_IWxTDuGxOb_laSV6j6YrYYnIRt161xSJgRLi__HN-p0dWYqXbtHBvbkCryQxD5q8S-tUXEHF7fn2-MhQicffkJzdMVS3Tg9ghI7mOXGOSqrXd_Z77Uxiiggf-tH2HjODJKdiRUhmiGidjiivsJy-HRRItWjRo7IGG_302OJeJruKOkiCHjMiZxn6zIJZGMSZdluiOP7j19zKRhq-6Ox7ZuthAZ2SywxEr5Zcy47tdqxTSqkm45OXZEcbEx5NE8rakQY7uc4X9hMgoxLRtdV3Vf0RU5FqOP-udiqAfr4rfESJnB4yE-EM-V1csGhhdLHixynXat73PmDcXoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک 3 مدل منتشر شده امشب
🚀
مدل Opus 5.5 با اختلاف زیاد در صدر جدول
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7847" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7842">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tE60tML8nuWOMBYjpvftmB17WS1JGxtA9IyVRCCiHxjQTuubeHtldNVpeOd6lt2NLHFS0ntp8oGeUIT-0fyXGjcbX33OW4a3uwRyb3Kie2HTjP1jntB7wQoSMcVhUQN9mLXCbatIAgnLdoPSLZTTnuPsKwApQTmf6seU6l3XT1OWkkzTRM5yIYL3_phqv0hNb8CY-gUvKSWhzv2uzJm9DtLM0G9C789m2-aCYwWHtKvG8_qzOs6Dnt-NSvzbCF_L42E9IM6vdtKdWmX3e5CZgEvSKNRrKlLgqkn8p48NFH3PNOTzFWvo_3UVUCfk9do8pQAeM5CXA_rCQN95aKry8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pTQK5rD__afGYxcPhUZuMlml7UB1yiyvSndWFVULzFswCazl-tuhoQveFlfPf59Hrho8lPFPYiFMtcC4s544r6mkEejCfIfwEARZY8UEEwu0emyXu7htUaUbW0hVEGAypUF4uMJ6_NWI8aINGH9Cse8Qxhjhd5AmNipBBbLzcKto7xm26SzezWY3whD0n4dA6bDH3sizcX5skB-B9cbQ4QAA0dXf6tP5rWzW1lsBWd0tuHgeC5D4SbqUvOTPZhxMmbuTuoq7ZP19eyUqYs8sL81-EWkC8FZ6P9c0jWC_2BFbnTpndW-6-A2igtNmCIXHc7WKh9sN8goIzvOcKPqoMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n9TdcTsnDYcZ1T0CP72XBzpO_mWT5EKPco6s27FgIDgofl0zBDjTcTAYrSui07A4Py3VHegKW8_7nYnk-4HsvBgrSL9OeRqY7B95CwA0wm7xO7FgMP2YII-XxY-7PEcXY5Rf2v9UPEXdyFXcO292mVfeUsDhGOdndKNo6SsooDqza8pO2LhrFe46IhmcJj9HlzVhlOTBqFAsL129Dtc3hmbiyKHx_QnONEUinxzqnAP3xQMHg6WGZaybFPeE_RZEixEAjM03mRR4Dmx4o8DhWFnqzFNri2APRd5snezApBFi7gy49JVKVetBT64M4q9nXK6ZXn0NCY71f549cDL_cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fkP7YhYIPtKcceqf5_2MG1fxcfM1shJVNk04W0_7FBRvMAxuRsSbUl0KPUIbWGa6feJb8zieyUQzylpNkzAJMBgNYR4RlpzPZgY2ND7cfwMmuWK-qHfi9VKezgN67M-pRdbLLH-cMTRhXaakSvVY5Z1GJaww2f6UJ2ifYDA19SXQwXV5JUtS3vpvkpbUR5NKhEvFheyzHkNKJwpyLnUfhf7uJceH6rtbjH0aHZbsUiXHRHTosOf8YWlvPIlAmVqfcf6xO21yR0gajY4Y48jLE4xJUUPvJ4zA--Fntzj98hzXuIK7QFYMJf5quan6X5Gf6yGtvL_xb5vVL-Lb7JiGJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/myGqqD6YKAZRa4iExyf5OpI0GdI2utUkK1Qc-zgXXpGTd7PUnjOcBdUZoReNGaULia414usH-rji5hMtwMg8NcOjGsIJxE_XPrEWJy156DcgLTFPAm9KfIL0tBf9JJZSGfzF-m3i1AiwWzxqvCg2YqJDUgK8BvZObHGwMaS7fbm14GX-3TXBjozXXxaOeqNkP5XXx80Yu5mz7jWl4aGFcAx8BNevQ8VL2TIouwMCZGYAzcoaw7dNQ4bskyopPxB873fPjtR7qB2Pqk42oGIibeAAEf0CWMCbb2tcIfpqnKU1LXxvkV_564BDy1-E3ImX18sNVPCpTPfSChBl8M849g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8Xro91yN4_H4vjVNA1QB6fpgiY1EHrJ3LsUDlvPhfg23BhBrvCrmJ5JiKLL24LXXhxdBcGPpQCFsg76Q_V-GILqQjwpV_FRN69Fc4229gBoWKQL9SnIxFwHvIE_-t4hyh373cfGF7-xEyI5YInpMBVDH7nkZUcZ1zV5FajGeITn8qm2BrXp4UKskjhRVC4C_U1w07vge1jyXVhUoO4n6F5891C7ZDcDyfxBHrSHaVzgkULUyGAdglFixY5SmAEPgiPtA66PlsmtnQfxHVoYzDtuD61_7j5lDpdNl5P6AOxrFCkBAKyMD48baIpCvryq1-PddKcQn6zMQbuIUchKAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7841" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7834">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=KHVb_4v-DqM8y9WUE1L-gUmSYCs25yVkrHPYgL9dMigf1UYA1CUSuv_0cN9QhoFKBHI0YA3wP_CqAjV4l0fY91u82mZiDEbQhii8QTbMy3P99PHmJ3_FklmmtjevqXJx1uyvRk2FpLyoJeIGNBisj82Pe7L7du4kunIQ5RqrkbQn6jUGGUFJXBBCsoefEYylPdb0WRRaUJNNZP01smPwPeU7BY71XxbruGfkAxIJve1_0R8TmsdGNsD-nCz_PYkFW0CYH2IPCxFWi5EdzEFmcAOr5k70CifewZn7xVFYjPeINH81niDEKMMGczKOjcyW2WmV43HmANDp0G0sOIHhnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=KHVb_4v-DqM8y9WUE1L-gUmSYCs25yVkrHPYgL9dMigf1UYA1CUSuv_0cN9QhoFKBHI0YA3wP_CqAjV4l0fY91u82mZiDEbQhii8QTbMy3P99PHmJ3_FklmmtjevqXJx1uyvRk2FpLyoJeIGNBisj82Pe7L7du4kunIQ5RqrkbQn6jUGGUFJXBBCsoefEYylPdb0WRRaUJNNZP01smPwPeU7BY71XxbruGfkAxIJve1_0R8TmsdGNsD-nCz_PYkFW0CYH2IPCxFWi5EdzEFmcAOr5k70CifewZn7xVFYjPeINH81niDEKMMGczKOjcyW2WmV43HmANDp0G0sOIHhnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnMVNLCQIchVACga72MvK6mEi3d7yqP-vQxQzxEVSlK4Gx4XJjWprvkp9yivi8oAiZ2U19VOSxt3Qyrj0Z0bZxZrxyGhudujwHSTPzfIAqZJ5-VUtFy5GmspDCUN6_C12sA8knlbsOc6WHrDVSjJ-X04whf3gZFfModtbdn3CaCu117rOrTAgEQfNn7NPG9IviOOQLYIY1mZwh0DOGtu9FLSN9GIE25QRBoku84AvU_BN4Atjij8FCJ9uLG06Duf8wt_8CVtRvV7K7fHFanC_zPTn8Z_sn9PRiRT_vtNcXKeyX8koxsiz0R8IVmRPKM5eEIu9YdT-F6Z8gQ9UBIm7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود آپوس 5.5 منتشر شد — شرکت Anthropic، مدل پیشرفته خود را عرضه کرد تا با OpenAI رقابت کند.
بر اساس تست‌های انجام شده، این مدل از Fable 5.1 و GPT-6 بهتر عمل می‌کند. همچنین، 20 درصد ارزان‌تر از نسخه قبلی است.
این مدل رو
اینجا
تست کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7826" target="_blank">📅 20:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7824">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlGDgiraMH3zTpC_SqEy-PEuY3k-BxK5924Nifj4c6wgiqYiKLcnP2ciDUW_Uqak0mC23dFTAm4zDJKGuv-jHaqr4WeVFrfLT7m1Oxb_2JLd4jLXfy4wPPqOMNYYvLKV8zJiOttb-4dpHknroJDrQ4kJLGzu-Qt0rk-FOMq_brdbhj2Yu31wNzpGN4_xBRhq5d2VWyRxvhut6Zg_7VY0dkkWs0llxQ641VKmn2tpvtC4yexMXt3dCpXgalLns0X08TsI9enVDSIKzrAgLv19qx5oIseoRRMXAPQlArgJTs-cdpzapU6Z6jWMc8NQ9oz_6AFeXlE99yhZlhSzhbc_Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
10 میلیارد کلید API رایگان MiniMax M3
👾
📌
مدل‌های موجود:
🤔
MiniMax-M3
🤔
MiniMax-M2.7-highspeed
🤔
MiniMax-M2.5 و مدل‌های پایین‌تر
💎
کلید API:
🆓
sk-cp-jqkYZKrokpSo6XdjlPb7cHA2kZfLdhdZwgtX15DsiwBAbFjb221rKvZtuZvPk0xEy7AaEZnD94ugiuDisZ8U1sLs5qfzCAHog6ti5fjjUsqZprpRqiNzdBg
⭐️
Base URL:
https://api.minimax.io/v1
(سازگار با OpenAI)
🍀
✍️
همچنین با موارد زیر کار می‌کند:
👀
🤔
MiniMax-H3 / H3-Max (ویدیو تا کیفیت 2K)
🤔
speech-2.8-hd / speech-2.8-turbo
🤔
image-01 (تولید و ویرایش تصویر)
⚠️
نکات مهم:
🚩
سهمیه هر 5 ساعت یکبار ریست می‌شود.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7824" target="_blank">📅 15:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7823">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gc3tkyYC57jwkZWnoR8ZCa188gI7Ario4xJOfyYUBFaDLv05FdYE4cA-fEwbzpLl1OMvYBzDzbJG2Mv1smxqHLid2Bw_s8Ew2l8I8OOL7rwfi85vc58nyoUI1UtqIjoSX93bsz0rjSEjtOZgn3dFE1H62r_mGNI00cS1qUwnvjS61kxA2RsIA1qRU3OwbfhWLXrtmeMt8f3gpOJpCFh9WZDOcwW2Jb61MyOMu8ucEryidZlythwpC7ir49iC1P0sySWs5-ApNoxvujIMVRm1hhhqYmIWfHZjm4LmLvHUGH5jHoqqCWaAX-Qgok6DYlHQVBKuQgtfWmHVzJgFTwk21w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚙
موتور Agent Executor گوگل برای اجرای انبوه عامل‌های هوشمند
هر عامل مثل یک فرآیند سبک اجرا می‌شود، پس یک مجموعه سرور میلیاردها نشست هم‌زمان را می‌برد.
🔺
خواب و بیداری زیر ۱ ثانیه
: عامل منتظر تأیید انسان، هیچ منبعی مصرف نمی‌کند
🔺
چیدن خودکار محیط
: مخزن کد، سرورهای ابزار MCP و مهارت‌ها را خودش نصب می‌کند
🔺
جعبهٔ ایزوله
: کد ناامن با سقف پردازنده و حافظه و شبکهٔ فهرست‌سفید اجرا می‌شود
🔺
هنوز نسخهٔ آلفا
: روی سرور خودتان با فایل پیکربندی
ax.io/v1alpha1
بالا می‌آید
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری مجاز است و اعلان‌ها باید بمانند
📌
سورس و راهنمای شروع در گیت‌هاب
🌐
صفحهٔ رسمی پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7823" target="_blank">📅 14:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7822">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyGfEDmxAiw5Y3A-xnM0XeuSedl8nilFS-3tTIc3GGpzkNEiCySaNle_-OjIlJLe_y1TiPzFRXuDwyIRVdTM2ixoUe-Av1Wzix-_Siwb8MS8yqInK92iVNrlrb-lLusqQgVYVxPh0zKL6Cy3-8eUBMejFjfTwbBxVDsAky5hfXrjs7XP8LyVk986o6lGoqkR2Iy7NURBBWC39L1f2DgxRDbTwYknyXw3kcgUeuWprjvzTajqAxHycH0YAY0ztiNw2Oh8pqo93BKSsG4y2XGmjpzlnrNt2Nk-G-Qlop9MiCVC4SLVC92X9OSMAfENzWTgLreY8q_SPk3Pz8oNrp8cGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
وضعیت فعلی بازار هوش مصنوعی
💀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7822" target="_blank">📅 12:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7821">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🥹
2 روش برای استفاده رایگان از Grok 4.7
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
1️⃣
Grok Build (رسمی)
نصب Grok Build
ترمینال را باز کنید.
دستور زیر را اجرا کنید:
curl -fsSL x.ai/cli/install.sh | bash
به پوشه پروژه بروید.
دستور grok را تایپ کنید.
وارد شوید و از آن استفاده کنید.
💬
نسخه 4.7 از Grok در Grok Build پشتیبانی می‌شود.
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
2️⃣
XPLabs
به
platform.xplabs.ai
مراجعه کنید.
لیست مدل‌ها را باز کنید.
؛Grok 4.7 Free را پیدا کنید.
آن را انتخاب کنید.
از آن استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7821" target="_blank">📅 11:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7818">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/om2B2_tGi8Ek2hKG8qZNbcDUtTJaL-DcFthJ6PN1wrE6N8NkZ6fgF8QtaSi3VTApUzEmIjd6ndr8C9BhjrLnWjKyVlQI9HKSnvzb99SGLnHocqqaqB4ycrBNNIeim88YgXENs-FrHBd39tvn9exOH6O-45SyakN65cbpEYw3Mx3fmFHIe9NrVmp_H9wvovbUwqxqW6fo0I6EWHvfysAPPBiMwODCFd439_634kv8lyPTPDt1bFXPwMQDAXTRIThx8YNQTqnWAQ2Psx6KNRCgpAazMvPYcdaNoHG4TnQg5XyvDOzxpP7CaAcN2xdNL-q1R-te3_o0-Mt3zdbIlAb3hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ExFX2GFCT6Ob2AR5I-RSKwpmdtVToFaB1sHKEXozqya1dAyW7H8DYhsjKOXom-uS2V240isr7gt9pRHlMvGAlZ_zHDMhn89QqRzf4e_-YZx50b1BajzshLQtyAYuv0GS0S9EKYxrgj5lZjfLJ1lFtiUJRXLVPzB2k_bfAFYRNEv3hT6AKUHC32TSnWWdbTnonuQbC9wDs4Pswlee-TQ0m94o4g2moOVI1OFlw9IMyaKOdB9OncSdVX83kzWOEzB-MwpZDZrbAHoS4UR05Jkqk9yvCdQbYoYtMFIT_tZ8Vw84bMX7P_xAPweXsw6hcqVfpAv1at3nmRk3D00hVck_kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BtNcq_lcBbhTDmJx3TN0Q7Fbgl5lQ4uiEK1Wy5AYrD8r1nFc8xH5s4Fur9lD8zQO6AkMqeTeBWzJCmBzqwpqOzPMqxjEsASdH0z7ZqG1DGyaBFmwvO8sOsnq1DcZIsPbzqRATgb74zK80EnSiYOiM1P13zQ6E556IxNlZw27rqllJjmsWf1RMqeyAf80-FvRhcbWQU-whrSjwKUpOV6VT7WL9TItc9qHzfl4DKLcjT3aVsACzqOWHUEqOvkIjQtRQH7qsfbmsIlG6HjlDx2kQfcQN-d_SPUV7wc1RK3-uoag-0a5KVV905us_fmnCsphRmuaXerM63qZYyJDj1ahig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😎
دسترسی رایگان به mimo-v2.6-flash-free
🤔
نام مدل: mimo-v2.6-flash-free
🤔
ارائه دهنده: Xiaomi MiMo از طریق OpenCode Zen
🤔
رایگان برای مدت محدود
🤔
صفحه مدل:
https://mimo.xiaomi.com/mimo-v2-6
🤔
OpenCode Zen:
https://opencode.ai/console
🤔
مستندات:
https://opencode.ai/docs/zen
🤔
برای استفاده از OpenCode CLI:
curl -fsSL https://opencode.ai/install | bash
🔥
تنظیم مدل: mimo-v2.6-flash-free
⚡️
میتونید این مدل رو در
MiMo Studio
تست کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7818" target="_blank">📅 10:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7817">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltwgXgNAXli3WyMFnpP9XrV4_ahPyds7Q_CjiqwulEb4ifIDBnJYg-HV59JSJ_ljOmPTsLUelkZCf-3ul_rRqEEoP1h-Qxdt1lD0WB8tm0hiF-0koyFuXwLhkb-7DuPkGkVqJshMc1o-79pRXbELw2bS-cMHBwllD2liPYu-41Wb6mIGAgK6cuJeC2LQDXpVKIIAolKPtNCGku_8ljTQsTPgHuhtENi4fdtVxyRvWu0FrxoqKq4Z7hI0n7522VQudG08jLcHjoF6XfrNYSrk2461ym4ziI0RQVKifIiiyHN8c3uPzvVTUHQ0fMlxDNyrk72KHlg17Z78e-knLyolcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی
یه پرامپت از ساخت بازی مار بازی توی حالت ultra speed mimo 2.6
توی کمتر از یک دقیقه واقعا پشمام
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7817" target="_blank">📅 01:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7816">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap20cn6YgaX1V-RRxGLXGEb4hn42dpFbFb97m-n3t4rVAV6wb1xgpKIckur8cTpMYBBq4JzrhCmmmCUHmZy0-byjmwuvPe77c3YqPmf0MlYL1gMIgsWSnlQkMhjZu7gIlwes8r2xkg7RLHqdFzHJDF7PaZXp32tU8Fb4YLugltmsGs3hjNE_zOj-2wrR0PcuV5M_75m0nLxCT2ZkDrDtzOkpPmwXRoVU7wzwCiYRmq4aPSYMcNSRwUq9xEp6RQrQzDNay9gafBzyV7UYpDRTxXWfjVPrEnSYOgaYdqnsAlzcozhqfY8Q79NThYsmET0I4Y9-O2GnYUsdBF-isb7g_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد   درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در…</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7816" target="_blank">📅 01:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7815">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد
درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در API منتشر کرد. سه نقطه پایانی (endpoint) جدید در کنسول توسعه‌دهندگان ظاهر شدند:
؛ mimo-v2.6-flash، mimo-v2.6-pro و مدل پرچمدار با سرعت بالا mimo-v2.6-pro-ultraspeed.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7815" target="_blank">📅 01:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7814">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=mDkT5Y9bBiueIqqfKi4EWZHStdpBGQlpRMVyPv7IMa09qSDF6xhsMVefUqLrhnlMDv-shx_5xCSsVdmzX5NY1JGxqYuhYDckeBVj4k4chCIytfNH4FRttJys4rJIkCqweg0662utSjwze6wuy8lhHEyGbQCkzbFbPt86P1OizJl1WK8jjxpDmSVCyi5Gbh_ISbYfYPwY28otzhzrsupigW_lvICcvmbXbi9zAWECTSdI-dqiMKjb352d2kyfxMHx_EBGyxyS88NsSOkoiymNi97hDPP0hezJNNUN7eagnEPDJFD7tvZf25eO2LKGFwTsgmUU2cirZkzd4AoziS9MFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=mDkT5Y9bBiueIqqfKi4EWZHStdpBGQlpRMVyPv7IMa09qSDF6xhsMVefUqLrhnlMDv-shx_5xCSsVdmzX5NY1JGxqYuhYDckeBVj4k4chCIytfNH4FRttJys4rJIkCqweg0662utSjwze6wuy8lhHEyGbQCkzbFbPt86P1OizJl1WK8jjxpDmSVCyi5Gbh_ISbYfYPwY28otzhzrsupigW_lvICcvmbXbi9zAWECTSdI-dqiMKjb352d2kyfxMHx_EBGyxyS88NsSOkoiymNi97hDPP0hezJNNUN7eagnEPDJFD7tvZf25eO2LKGFwTsgmUU2cirZkzd4AoziS9MFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل در حال ترین کردن
Gemini 4 pro
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7814" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
