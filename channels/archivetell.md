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
<img src="https://cdn4.telesco.pe/file/Hv6kUFaq0ka-1DMYkyQXnYK4kMwn0D4BghdVQBh1dnn3MnlJmA54cVtodKbQYh7oLPXHItaRzq5vxOO2fPiwNFf1rzoSm8Kc8p6sVT7OvJAymazMJZOibF6CWCNXWNU4_gTxWyPMcbVzBGxXuc5asys7JjvvIo9EfnPeO8cnNUH2PxTsRw3kQf5_JmWYb70pHoiRSftI4vE4f4nUPQOIun0xP-QLYLwXr5reojHxauL6L17elShfYpuMaMvUPZe9-q7Ggh3tVfurilG1axcJrgm3i_5R-97K8xH5Nx2QPyaS58LoBjwjnm_y4AAFS9OLR1JwkIkeosa1MRgebhtAIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 09:36:27</div>
<hr>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 572 · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hZb185HkmbVh6nxojS6hqkuRvrTWwQH-FReHgO7dZRr8V9sVHDaDRQf670tCD0u7IbakLTpfxUk98XZV7gqabKwyIGycx3EJ3-ntA5Bq87dr26BmoE3WZy_NxkXnwxIykWmEGQU2AYJodNLlECxUhovd9xeMTwnD-N3ItPViSg9MZNPn7ZvSX6aRtx28d7l4TfOdyBLFl-MASIsT0Pv9-hFM-CaR9rQ4sWxu7I5VYr58YRXZsecoabevxHOuboAZFm4nju9zD5NpHa_WuyxPZdtJt-RR0baoqGCtrlsYfOIJzEW0qWLXtfIOmKgMRgEiS3s7wOF8qzZVUSsB4JGJhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/anwphxjQ4onNZKSYFq21oCWXw06dtCn1Z6zAg_gdbayeN42hbHMCzJlkc1TToDPkwmET6kBsTYeg-4p1LBsWRK5CdJZtPP5imll-gHp4VujGuzx40WjALAWCH9ICMvzx5scWFncEu4U3Zi2V7ywqxZHGKznzbEC4SWil3TVpsuC3U4QTQI-KUiGnSFj-XgSmRKg52HSqcDXQiGEajXju28ynqJm0kzHaroe1EvBhEYQROI7tATBeE3qLkJwQb-RCVFaehDim49GzZMgggz5RzhM_Pff88LH1frLnkr14nS_cZphLck2VJuJHZ_6youcrSW47nZrk0TAsEhsygf90qA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpOdGyIzDD4eZvAsI0AIfHf8GH2HaW5CgKsSYUyBHCx2NjPL1azXLigTOzo5jsJc-jM3Ehio6QT-0x41MdUUzeOPKjjIeljXvPdlOswf2jLdh9hbYVZbqIZCQHm47_pBzq1gFjt51YHbuNCdKYOVy0a7-MOQ1ZGTvGuG5UsvkZluUrwb9pZS-GWew27maZ-ETrcpcagJvX8MrFfpND4Uw21NniE25ke8Bl1sVquXXZY72tT_DMudjWjqh-79jlB_QETAnFVgh40s3soLEA0Im7ctggs9E6BlcK0VzIUFFt30vv-dweMXzzIfm4uiXb6zw9wwIZmj00-n9o0U4h97LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJMpDPrAZjzjzCoHSoX6Tuwzkks9e-ITaPFkp17V-0LUTQ310W5NLXEUSyOezoC7zxHac3oUPyzqvL0izM4QYbAWepqepY1PKBaYzqcGIOiWhD1pKab0jrthAag2Vfw2dDe7uv7v3zjtB9QKYIQmHz02pbM-GQpi0bmqLVgL249XYKRUrBnzdjEcru4zdso_BqNWAiO7gh3af8gWvfRd15ZRDHnF2aLL4scoH8IuN0QmbA5kuDk5Tuqjy4WE84f71Y2qFY4-mvGNk0uw7Oy98yBYkZXt1xJYrKLbzCn-3YBuWkvpS6GQeac4pKSaZ6fYW_JUfyhjiUzJAIx7gxcjIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TB2QqxVFB7RMLmVskE5jhQ5FEF4ZVeQ-E-U0RXSlEyD7QG2AliE6Fs94Mx-HcoD52oBQrIrDK6J90KPlQPDqhDE1gB2sXTSSIJm0FjQRiDc1v3NpcRflj6s3xq8HcWhJP2k-bZXvSfw-pXo8T269JWxKYw9ZvTq0VutQnBiSTnqwE0Kda8DrA2qNGUNB3lKuCIiJr_GzCAikdx2CNoEeDhML2ZMkq2XoV1dNA-6upxxZu_nsRRtpQzP4Gy5y8TXpjxE6eOdynWlD0lCCa4j2mIm09RBNf3qGLw2EobHawTajpcbchxR45PI9hf90L67w27wuOYfwdYIkogjX75PWig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sujCjJhGW-Wgi0ukNMBwTLMNmXTWUW1LbusKahT3rS66qje974nv37f3-jjs8AmBhApYGoxSNsg-ZUhMVcioTHfVHZP3FDraTsZeEsXpkMNR7lO4VbT7nlU8eFGVEEZERYtu2lyor9pfXjUAeoOHhVrtr2CvuDkGcVrCJQpLjPimQWri6Gc28L1DXT4hzhOMP8GE7dW6viHOjZ8aJ2ZCPoMMROdfy3Ggul1CcRF2n5bEEZk7vUDbr-B8Lk6Ie6paU7HaTJuL4F4Ln8xd320SPqSWPvMPlsWFOc_bgZVQudMAwO180-ugB3x4Iku1kzEaSy5DvQrG_ed8DXGQd60Tdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kL-SFW0AlQHkfbMdDSjaR3tcd-h0yWPRtrnh7C9ZEh49dEby99Btqf1f6jOxcMhiqMCkG-W7HiwWKW50pWkSrjhVtxrbPRD-NrwZXQf6uE7CJi0Sj9A4PP_alWqTDZ269Xb88rpj3rNExTkstfwP9cRxPtEbICLfzYnH90lvx-XkdpYCjnIGWC6wu7AvGDYj0HbrxhCV_7378SDL32445O2WyckbH4H9_3vgvZAVeX6gtsDqwAF8Uo7Yg65QtM3KnsnNHYdpVEJ-Gg3ZtwxQA-x69TFcHSyAemRXL8RjwFfSZ0Rtj2qWA1HlQ3LZxdWvjvjTh6wO0jaLAsJTtr-FhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2DDCa3BFHiLJp7i1iLc-sYgfwrB1F2jlreAD8z4mtThafjfpBXMFFnk-5JZJpkjV16cEPRh1a-O9bD123yE_tne7auOxty7Q2HfyeLAfFLN0xkcvglG5ns8A1gK0JfP_GNhq_kyIAng_6eBCTPT7_PnrKTYicyIteUhUjbvihUbzNXzAHOC-qkr5Qm8_eRIpR-Rf8Rw8sDsqudyLoGQ2wb1zFcONHkCqq2J4QmjkSbYWMu_qu6mDkf1TA9yHvKyzmFcJdHVx_y_74gZgZfVEu-PuYg0rS_dnHQv1Nwegp-tN1lfqCgSEKyNsHTJogrAAwZWwy1GWJKxBWLm9sbO_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwLJxcm71aHILOg6B6GkhUJ4MnphiNq2i3M6tYv53eXBP4JPp0DCZDEspaNOr5vVCMlw6Y9uVpaHrsN4FrEsaadBZ1fRKWfDt-sCUdgViKxNduiqsGF2rU8Zwe5oZJxncQRd00C-PK1p7QLohCUeXNwqqdH2Ss25kuMQQBBEoVSbWmAkG35d2i45-hYdxlXSU_nv2ru1kbVt8JUr7rzGJC4EmEp9878eLmyS9sStDxCzQQXUUizbYMeUR4Todw1jFiu-5nxEGJMdJpWO7PF4vElZx3Owi0NKeLyJysuiYrK-IfJ3kcOjEz2c4nExXmt2blfDqg3yMeAaLcqQ69d86g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZ_no4uEJy3_woW53ibggQfePPDPXCtQGvEynt9NGoey1NvFXaPjgA1W1Q5ALuEuGt5ufeKS6jgnLXrdCxwBfIFTXUxAKmVXA7qhyIrOoRdBwZ2OEJDAFkR1v0rJ7gMJRXScnmGXeX2dFVhi_qVSiFziBh21pLl6LoBPDI2itGpMrRH7cIakRHSlpkSRSqpqyfIkOBXzTSDfkbWFzeqGFOhfeMSsZcj1Ax4m20g71tbMVccmcJkpoGJQCb5mwO2BnTsBMaPOfhqtGy_lUDWlBCZk3v1LdSU8g2cMeokpsDXycFhaUmpTud3shDz59bE4hK3hWORtH-P6qVrhMmIuOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MrqFo7RV1cIiQCjjMqG-4XYmCquePrH-jY6B6zLulZXkO6JbZQivwBRqvgxaqEtlZHdOP87SzaIVA5EOxGUkUBTsXdMMa2swJrsaQ-7lv1sm6EzkA43uONUt1oy65InzEnQYyI6FNL7rZiKI3SWhh1FNFBiic3oU8o57ymxQHo0tEMP-Q1uvdv490klKXcHfpgxpDqbcDHMgzRib4V9Otxa-eg2c4KrA5XOE4IVq4es_oKeXtvI4NTORw9eBQ-Zc1kdEuJbmQtVhpsr5Lv7NNP4LncEs3u-b6t90JgVmoo9AbDty6spg40d2uSKOHTZyHIyTTHoEW_TGROvM6stZxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tYX8iZYpfLcZ4FAOfsd4Pd5uc3cImSggaFLWWDokvmMKkPAjpSAA-EYwGnEPMXtmz6VO3NEcnvyw7GPa286imyurmvsvcc83S3DrSUV_QwaB9NwKKCz7dTPnriZTwUGDoqWk62l0Awl2HWfLdZzRTc1AVGY5UeZmqSUHqkV33QXni95A_Z6p9-lO3kPRpCrX8_07WfZ2U-HCQpmlHaQq-WAlrfHIAMlNHgVoIII_z3seN2uObaift8X-I_CXj4ZNAnqqUY4yARCz5qJzpktCKWMiZyIFp54xWumo_0nHqEPVuap37nnRGPykPZHxg4_ndxOklOtb6WsaXULD99GqVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlgUvwXkVEYDhM47CAWkaxAMHODT4N2IMe55YITADMj_iGjOwxAIzppA6lLhmbBWWXzJ9dVdCJNZMxzT_dKrp-et6bjOSiU8KVJLG61LURtAtjbZ6t6UcsYYluslzAT27rswuhAg8-BNsuTW8uD0fgqHQycch_TzpUF_gIzMa-FJqG4H-myiTe8RpcAASQ-0bY33jsbfLW5Paw8uHBHXm8YzZbIm-MDr_ri8wlyOqTG8dDM1bJk9aXn8TSMvCqd_6WBUylH2CQTYsxZ8R9zMtPGGGEC-cjYr-jgXiWqQPcIDN9jUw_Qq4Z7LGqWR43sbqIrXcc8V91HboQbbQepT5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMtyXQMeJB0OPZ8bObH7rKtXhZeui_dnjMb4R2pVS7aQ2aESHSbB87gFAuqUwvx6Fzjqoc-KbVOKc061Rn5BECKh2oS_mX_07SRWaEH6eZ-Pm-Sbgu_KZ_G_630RGqWX3PozG_3YjNOAyOr9yEMmwk3ZucO7JkywHGzclsF4vD49WkqrbE-NiUh934bwH1NqvzdCNZNMB7WLsr-zZWu2Bq3tWryfG_PWVxIEN2KoOB4WBFfKZ_wdZFkooKf8XboZkJwKg1nfoHOdu9veVbeG222-d6ZDLUGrlhqQBZeshrnG3mlQwM8_FhUaDgzIAwzu2ZYC-SHq9BfFktgoOSwdaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DXtU7pF5pvJBKJSCxTKfqt0pCU8MccHrUYhA93JWHMWEdaU6j6zng7N_Wz_1NNgbc-iAcVDhxPPkPTqx4nnT3mBQLG_TtzMw4q9ZxF9CZxsVC-Q8YoHgAMAVBJdIL1LJSapJyN-yxWN5cUn6w5XgaYAEz9tvrNttKwUWfuIixn3YCtvU_h_ecrvZvA80aD63PRgyX8KnOcJ6c_t-ie0aaXLJdtCRbFBSv_3LJunJGLDahO3Gc882C3eCnqTgS_KkQ7zRm8UuW_rplKt0V8ZN6n8N4b7XIO_ZqzJIcOG8EmX8hb9hOMXMTKaAkyMECijcNqa3YpzYxHQIe-kbjaQ-gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwjP8bhzILOW0576SwRY1R24gtTwftjejlT5UX-NJ6GT-8uKDIbxXyDCgaLbq8HR_bO9O3x0fwZfKMs6VUWmmVnZbmVf6TiaOq-k4eJVZmEMZh3O2bMGdnzLY_Rpc7AeJP9lGdH6SId1GK3vvJlE4aKHWrodpyd85CE439RDP8UvCbzMY71nF5TOAe4oXDAVdrfqlLt-963Szp1mrx2ZVuhZqW9l0Zz5kv0Oh3qz4BZhjDTIj308Ha3HDN6IywklWnmk2ItlA9Phmn0JGsKiCkjMzvqx0GaODTG6d1of2gMX6NBZ50xq8zCM8TRV-jHtSgd07KaA3vgd7m1O9w8ZBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSE06QbXj0C8Z7qdbZ4mJzSMdsVoO8S46NpA1YSg-3rkNGKqZoDV8OSV9tGMdpEc8vBDcw9M4gMZdmIj2cKj0pYXmGj5MMMgIbc0dOJ0khdkuYFFa6zJ6Tf-HPBeLHA4FTZWOneFDdxPnYjXPj9gcktDiBtnvFU4D__tBTZ3zf6BF-7HuFG_PuYw3tn2pytfM_mloQ2nP9TM72Sh_aLNCxdFZCbrx7Joy8Wc_BJuvdkCnHP3v9m99CdI1GDBrCgZEIM3lvz_AYX3nREp9btoFrO-ZiIfB5flJOQA8wEU_KrMAZ_zYCj8Iab3p05eippU4PhlME9Emtk8PbMfV0Mj4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/npIFBivjVPB4bJytNi78IdVjRGy_tvDjaAABR1NLbi4Nxgq3KM9m5XdwR75jvp6huzA12UZgM9Qpfztwr-BA6IlQwZjjEUuK0E7Pas5TIXhAMcV-fCvF7NLOjslUl8eqromOHfbcv7WYctpF9OYv2SegkTuVHvmJdSpjX6IvWm04MMGDR8zEpvv3B2gcUuagn1J0LseSB35N_cK071J1eSug_U_aSdFGVumUtFGyWYCpHW6FyZ6kWH1nXTEbfEFPoJ1iduNey_4acz_zD7wqI3oC6HWycJdO5QxJ84lO_Zni5Jo1yhWR4ylpAUe4BkMV4fGtCozo3gM4H3q59mArrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l5zoE1hLcYjd6GuD8DnjMYe8T3trpt0js6OIzJ5AGLEpWYD6F7UO2f06cDZlE8REbwNZsW8a2nJbiuhgdBCdq30eL5VCcg9pDuaiQ4EkX2LboeeFCrlouPrhJvWg1SIAFNTvZSRq4jlhlZ7ECmhHLx8mmkLDWEsWZZ3PNRlE6edn5ajCEye7Uj6qksJMDKuCqYn1GUo83v-wdd0JODsgcAaEHGTLmIadAcgq7BE-uhZq7d_STRKNJFqCdgzrot2RDfVDvLqauEMU4sI5F8RQyoZdMCfEoYyJGtamfZAu0YBmspRS763lCiB0eSOAocOWicIwpIUNv5B00GziJyC7Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NLNkKH8iR4DrC9MPHv0lG4-XigTcsgk6N5XjHwCJDNn0zhW8qO6ddSdUrGhM_Yi_nTDRPulRsJs1HzrvRohY6KkjTbpu3WBx5YM2dcyx5OuwRZ_mKhwA2_XMo8Kg6J3aSolFW41pyGVES1H3oquL5bgX-WqyV3VChMk7CvQizjqD6bx-sbme6rZQn484uhyV1jX50W5JhYhauKpudgvG-vvSKo9rnVgYSN5v745cYYU4W3v8uaRN8PcuvtXl6GMQ6_luYtgqdsFKzpr2NxvBrrfzyymO4gEanjJ08g9o_nc3CwMNi0hHTtTPD5H-8GKVxPoKAmUrtOmwLoD5PF1-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j75UHI5Ah8NqmYtxDsxZ0OYLhPNIU2cvat9ya4P478TcM9dN4hlP2HWSxIbW5qOy8JlR52TCeZSqM7vIR2N3jT87z323wfea2TpfHOMP04MAvWJC1Ytw1Jq7svCb75pNMkCJQdtP8zZvTB1SfiFcUMsUjSqMqtaxbSySD7_0DQH7rr1JJtGU0Gxl7c6P8DoEZa9Ufgdj-GJ1pJd-rPIBGRTrLDPiSVWQ90jSf_mWutBGx2ossnEMCew0wVVMVpsresH8yez6MAqjZAhYmTEWF7LuEEPoLZ5mH7p6vVGh56reKKX0XTfkPD-Z1KZUpU0nui9P7UUw8VxnsOhwnrDayg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/svLjm1BB6bh3oeuVcja5J_3sTZSifl0VNtL3tn6rDYS10Yxcf5gL14fUAjj9SJENYfQCRtCkd9kiwRSy0rUkQfxBO_tcGTSH5CpL5RgBRCtkHVqUFxM7NPoD35hC278RulKuLvHAtQkCTk0Bf5OOSWIRoMpol693H-zKMcKsiX0o0-as8OiGWolbs3t4nyBePhmGiNdqopz9kb0qOfxybvsmcuFEQLNYHlQ2YsVKLCTtSw7Sopk3rmoVSpvkqoBfeg6Vk3KTOh-WarnxY4jpfe4HtjFnn0u5XHC4dwIfqDD4rgeltn0ps7WhMjFHCLsTGy6tAy_zsaa4VivkZXasHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A87ctAWVBw4KSrkRppOWEHzegHjTOyWwBnVuU5b7b-L-bhvZISija1U9xiCUdHqppechU9Prhh1e-n-cSMCWz9ZkqBFEhNEDkAa1HZPQeNknx84e7taAAbvndZJ-QB58XY8RwuQ4DZzl_eiDcgfo1Aqpb8z2XyOQUt_0W-BZ-DSTejD0spRoibPKaR-VJtXTYbLIpjuIr8GZ3TqndkwCoH58mv8QdLr1Zp8V98PwmQEACYkrTUuwuOJ4Oi4LqDooQq53PqbJXy7CExwOGKVm4-mVGIAzt2DhVSUK2mfHu_so-sFHAq2nQ-Osx6R6rqFsJJdlEm1EJrJTW4cVTbcS-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opRx_PsVZciKPhI0OEwCldCwxyVes9GNZTqpQizXLCqlu4Bs2ysBtbMFaBV_xduc2krjZX6AbFDMIz0aAMRbYqd8CdRpWYxWjZFW1_tKNYfRqLyl6fodemcjiL671pdHlioTYFh1HQbFMG1ANSwZr9uebgzeqYAZXmKfGgVIxmFkkyMIRZCCuC1IMQ6A9WKk7dfhKExU3eub6YC9dcvgSElkLbgc01kY8Xci9ehJ66IzzHD4wQNpUOywCOzMgKY3YJLOJBrJRj_wZ1_NubHKUPvDYkYYh3hIvgs_gTno3AZFvRmdovuG3-NUpMOMNxF6r6O8s0Vm4BPL6-b6ADpztA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQ6U6ffz54pfZqL6cHZXDNAAaH1kRj1yyDio8tIOWtV8p1F-EGLqH4UHlZ3XQifBA0Sa1lGjdFnanny8H6xSKkYguJv4JxUI_xABxS4Esptrc0AlV7Yy53eQmZlBR9m3FVBIBxEPNAe2M8ihyqfA-4kI9QuzCIYWkNI0D-tSchpHlfWGLmNdi5kBCZPuHLIb-J9RbNVDgqyOOSgCwNyukpSX8V6dV76AfuzgNsmlvyM8SR9E6bDlZlDyN9GfYZDWez3hPWNDwKFBnLCkZ0L2-QSzlbAXIe-Ruw7TCxn_ZRbfQqGZtEILf709C-_2AxpuuELQwdMrt4igoUN8evQBJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgC5v96RpS0gI2mqmIor-eCMRkWR14tfbT0Jme2UuC9DjFQzTAuzq5iLkgmWYbvzWRhAhxVdXc4Kjkvnl-3qMocDaIdRDy-smf-uCjW1AsK0JzbNo4bJmnb7cYbbDM7pKeoNZjFYkEiZUtXwpCRUIDBIblZ1oKnS15lqqYvixpzXI6gnt3G3MQYV7MTxZURZgfThDX7P-KSEaPkJD5sTgtl7o68SMIB28Js1K2ik4rmNhFfg5Ros3d-sSI4dNPfDW8-6ExulKhhOOjrHYqAGtQOVgWy26h_BlgaUOXSl3OL7-EgrYwhyd2hnCBFJT7xxmaJgQyN3xlsz61M5c0wGOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bIH7jgY4SX_kSwix0Gzh8JrgkDw-v14_E8A7Bae6xTkq6IKCS-7jA0E_36hHLTiRCnShSQZlWgfHK6pETfSZ9s7iJI1tRv6a1cdrmv9gWiCyPBwq5FVxyI3LNZ5-q_cVXLcmJKfjoblyq7eDwcfICkaz-0V80c6YpXgJce98ouMpjKeIqxqHp_qYeRXZTlupMZelm5uBAcXGz_SzM2ubc_8XkhkCL41PBlFld_AcVN9JsOMMiOnCOsJ97Sgfo2ouNghVVWAsxzJ6um2Mcm3VQoycJVPdgeeoZS51iQaA82gvSR3sjBampmBS0mp25BQzEGl_x7TLBW0m7wDQOy5F2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U3I7lzFY0auaBQuJ8ep4pRlXwO5dm3tkNTxgcxAEYw0VwTPqQkkWdNByxvApYre1Ym3ZRR8wtmY1DL26s35E9D04YQyyQCWGzUYC3hZiFZTbaosXBQFp-KRiW5iY6cOSCHvjaBOsb6tvkrWrK1k6v7bB1ChTsgMbyrUgdbIoojUHy39NkLKcmCgqppOcTrJdJaoWSFruPTz-1ZZ4cfc_ekrqUaTGf-U-z6DrUn2SIzmbj01LOp-Ag_oQB9xBB24zzqVWW7r3fLuf0uiFHfFfgBf5J09idVE-0sgr2cz4t-_5ZgmuoAh8jhnGj48I7PAYNlKf3dn-tUQiH4B20RoxEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bit4c1T-dxWhIfcoDzFoBgDZqiwNgnmf5RbBPpnMF6UUTUqMU0vRYePUYggjJ6HHRelmSbD5BrXdwtUwPPTl5xNlofyvlszirlf6zVSRJBrhOcEw8M08O1th4fH3qZNxr_6ZNZgDXLqINSSdEKEUWv2hF4ghIH3pDgrfziEa-WZT5Zss68JfF7FYfAS1om7JmLEXFl1Z0OSiLCqgkD5RA-FenbxW_pnclCrkPjcpbUSY12QhgcT0zKUxC1rawVl4KyKIHWvDqr4avodlufo0JembtKuyLBus-z8VOTBVgCE678sRKXJJGnx_pjqnzgO7j8xD5v1vDKEbPta9RzC8Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMD5rUgWCyujpq-waLA80xiTUt7Te7P01zm_BbUQtvCMK8ve1g2DMkL_PjtqA9g6OHm1ZsZkoOoMUrVNXdY3mJMgYz2eGkGv5dck-pChJ250B9Uip8T8-WMpYedGgGJo9xhPfmQEy7MRaYV11qsWkYInhj4NcZCxyGtJqGPvvXg9vqCkfPXo4UG9y2c8i_jVFEuTOJngG44IP8gyHtwBc1AU9XSjBDX7ur3FkjZPGhdfVlE9m8rHCIVrwgpr-2Z1A--VtjBkgAqq8ferX6nWGjLz2ocFp1UG-j5e6WIHNVaSxZ_DOsc4ByPv9Kr4yPg9kjfpLIF3fW986t29LE71FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XshXEmL-g0RVnfbwHDj5LNgLis4ES78yd0R0u5UZYauf84gaKjDEYdIFQnFtIgMpPF_7yXnkrIYpNzijgfuwhAvXwfzEJgRd__MtTFItV5Tet92_Fy7An4txk4YVvOqKI-bb0X0V8nawKSurqosRpkoTNkOWY1eGjllPFbzWhwPEEGVH2Zh5h8RU_5yGxPbgC-N3iROEhdFuM1spxMRVJT3J0PhXjQkv1gFmnsScEcvxH50h6VeGSKN-PD7d28EHleDtQDkLc9mSTPnJAbHgZqGPAG0AIf5OOhKQmWTEONmWhnGGFCSPL4nP92ztNoFmASndllDqEb_3ORMroLaHTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8BHPtpzxT2l22FusiYW75U6_HPBeaFl9S8w_99ig8hMgpepUVHxGPgiM5UPMfbTbO20l-7QOdMGDCQW2kLRmIfIi5WJSnQewKrdBuBs4uQ6L7LFjUi18108Oh8oTHzDsCOwHIPRdc-aGJOy6VA9LICQblk7qdYdqKiPEbqBm3A_9GCsvamfq8Ow0V6kEFOeicYIO8JvWgCBbaOWQvNNvvyade0YaXp7mkER2oPof7thBwXD6CCPgpU57KJJDENHwINMGTrlhJNGFX3y4gEZS5mSc4VExSpUNJHakY01GQRtUvz_2AYOtWqe8xbUKoQDDbGngI8aXvCpmdE1BQ52_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWdf8DmZTgNbDH6GlRizKZlncNjHzlI7OenInSI7wqPsS294jCcvFPVibUbhL5o8Sng22cELwMERsrFyu2ttwdWvZWYr7wUsZwKMnwM9UZJ34dtaXWN-JGegoYowH1yVyv75YrTgo7wgAnpKgJ8f2AkHTsKJpwBWxGZfrNJB67NEadBLlbIOk0rzTaU6WSq9xxnFPdNu0oIM5uLPsXWG3DIg0DekPofWVsMJ0hlIk9Ph-iexaYSEO8ulzYXqTqRFItmLZpxN7nfNlEVKgRMWuk3_Z6OGSXJddXpoMaR2XcCV_Un6SiLrjxaiHvmS-_oNe5Mx8I99mAaS2D619dRx8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO__xPHri786uFl2Y5zpVCSNZrcNcMWg4q3u1D2KaqDRZIwndq7fQyXh719Hzeo5-jNf01P5z7tltPNE55XDR3ff9sCMYDNlRjL0RgjWbAI2d6hdciwD9Yw6X3JwK5a4i-VKhhmp3NLTlkNFJhLwlUUSbsLR5QfL3InZy2LIlD52hCLtgpzNbAmaxPTnRhzW-a88AhKz_4a_D0GGpQFrXIvFya5Gds5QPDa-4290Vg_GD48UpgUrIia6n-NXp64Qwlx5j4zA6GW1c817aDrGN1K-osqALrL4bcX52Qs1M-_2QHH2nggOcZzfVmSLhkY4nXAuoON1lVuZ0d8X0sd-2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iihmE9Jblhh932Z4liOSFIv5rCT1VzsOCqNE6a4wqRzJtMOFK9_hRCO2Qb0d_iNbuoeN4j4fbGIYHHc1sOAicRXbeg_b55npQ8gvGfqGVVPuWI-Z7zuDeelnw84-xs9ZsUXIURhDaoCMiOEU11rn69Qq0PvJw-g7-cZSzvCu0Z2n2oUjBJQUNnKPJGUXqwAXRbTdnDgh_gp1IwrcsoEVd1DxAXqVIW7w5btuWsv8Dg3wSmOfTRHPUXlDrNAKQr3mjEOZspsniwxOLEWGfsRHhgk6GEuFPeEo5KiFSZS0xEUDUIiClmSsDrx55PFnzqAK03S3wk5_c8U5lBlRXImsEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwUdZZ0u1mRykNRXtax63gnSYR-Ngc1b1r-ugcpg9R6F4HhTCyZmrAROfQHKgv2Egv1PUfYE1L1Sd6oOqg_sSXwb_tTeAC6VUn4vSsL1ZOgupl8EVDj6vrOhPV3Gg16MCnE8CLBs6cTkPThs5s-6I3mq6pkkMgca0JssnsbiahVKy380sMphyFIX4G-xMsfv0fw4vdG1JaICGN4Nvoh62k5ZrE42PbJAnRHPvTuqpn8c8STnUt83UyMx7Fu3I3UY547SzLbAL0IJB1jDoB7tr4WH4LOvpPRsmLuS9XBq-0Jz2u82VYzHFBzc0oCtsZj541-RjruWnualbkNQ5yiPhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2GUstXuK1la2OB3pNbB4ToEFOPPYMqlA0YbT3FhtisjkBbSHWW2rG7oz1ZSp-CYudawbLhPE8mLZg5RDQOxim4G2-6CrWEIDl7277b_VHEo3Pw0oVq976M2RTsB3lh2t3Q2YvBUDbVgwJ9XUBnLSGEO-LA8sRbL_XUJFKOEolTTZKoaxnTdQCuusakU7CkA1WY3qj-HiWuk1NyuaQDRWjjGGbKMZ7MZ3sliLKmIkMW2EJkQlBuyvphF0nTgsYNRxb2oHnYrjUZlHF8lsXJQBsSK1KHff-5FKU1Q42iN0wUXuF7eJyN8BbD7tpDAuJo5Q-MRWr8qiFoS3Ab0b6oUxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=FiBvkhIcEJbp43h802fpsdIHS7ElWE95US9d8hPM-OpXMwGeYv9VfyY_lW-ZIyQUf_8HivfjalVTY9ZJrtHjK1KyErSt7PlLRsZjpwIpNq3GbOJXaAQjax06KAr84qopctGY9LT5ey7Cod_QYLWlO7Eam4Hfyy1X_4yZPfqcuSg9QLd3hhJ8RnC2SyNBXOnNItcnqlsyEJ-h09TkCBw8AZ-OOGLs089Zx4eGpYF0KM05DPfKCQj-SqDyrd-6M1KhpzJZmp8I7GMg7ulmyb3B-0D7aBzODBeUwxHBfUsXb5wW12BEPcBu3Y7yqz_EQzFe_D5kEKg5OHlrRwehBmGi6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=FiBvkhIcEJbp43h802fpsdIHS7ElWE95US9d8hPM-OpXMwGeYv9VfyY_lW-ZIyQUf_8HivfjalVTY9ZJrtHjK1KyErSt7PlLRsZjpwIpNq3GbOJXaAQjax06KAr84qopctGY9LT5ey7Cod_QYLWlO7Eam4Hfyy1X_4yZPfqcuSg9QLd3hhJ8RnC2SyNBXOnNItcnqlsyEJ-h09TkCBw8AZ-OOGLs089Zx4eGpYF0KM05DPfKCQj-SqDyrd-6M1KhpzJZmp8I7GMg7ulmyb3B-0D7aBzODBeUwxHBfUsXb5wW12BEPcBu3Y7yqz_EQzFe_D5kEKg5OHlrRwehBmGi6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ez8qMear0_F9GpmuztJHyuH3fn4FpqkIbkFzyNkCcdsArySf1QMtahnTfGdluJlypVt7MCytJ51ol5pd3wXhke6F-w3YabQIuIyBc73zF0rHNPfW2rnPnkVoU94Z25e_KJ7fgP39BB-Dbp7KZbYcQrjFmokCi5s0Vw5KP9nJAqFjKZKFB2t7fPPt-NNpH-XiKp5IvncTXuM2BhTqBFP-g-oFhoXJo-pRmgSPZgXEnMWmCx05Fd5kAZlZnxyrpN6qCpeB3fx5g16NfQW7Bu0F3CXZFbrpO2oYC3HfFfz9bRM04CI5eQ1r4ohkj2eE-UOjUgGmucdbPXeoVdiAto9b6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVTMHvQpu3m0tvwgypavsiFUrM-QwFP75qWRCFWlFWMuq6_sCn8pNtb6FrU0-kKta6XspfQnSi_nxQmrRIZD0MLNWhl7HvNmRDsg0pbWDwcyR4POi86Rui_NtPs7PYpQrlycOmG1TjUXkRmYnug9ZvnEtCmyM7XDHeSJ5XvTvKXJqVQncnTq4LMqDT0LGOJgXvHuhu0Z3JMAYSRYuwh7cfl5nQX_8p6GKp5csYGc4qoSfeQAgRtPIEVPUhLEFPGiNqIN4aVEJ8KKlSY0lX-XrGSA4YH_cVspmH2-pMRxERedUEjClOQ6lgN1OMPtHpV4oVyW_9fa0ygJWhtGxkPJVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdwbK_V2Zejs_NPMBSc-TmpgwkRW1w0JGhgHgjgZxsqt_jjhBIaoqatksc9UPLcbm9cTwhnBBzhFesCGBKoyG1dRLUnQbNPQ_9jFfmTQKasPpGeYIVffu211dpAb0xqflBpMLTfV6A94UT4KamPi7VlD7wxVGwRC9Qn3ci9ag57O01q2dKV7I4r4qEn3CijW3Wx-HPrfgkr20kJE--_H2Su-4Huez5DhGE9E-jjt5IP8lcjjbsilzCVWvuOIrve4tNAc-P_eWE8xIA8Qzbr__dBu7FhY435mJXuZPZKTUgyJEg8gtqCQ-MMln9N9jy-GK_4L1Jy8aZnjY7V2MtCJ8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMl11Q-0l6-YY-aKFrA-vFoiWMP4oJ-8igq30SxiQ529bp-gQWwvujrEToqIx16PmFhetKrUnvxfiS16MxO-6KfB4zhugGl6TjRWuskhIxe8OUrUdl55lBt0lhBmfbbN7T9Q_KjwpXemrbBIl97KkxoF2G8j6jMGXP3DPpByZyda8ruuh8ncoMVHR8zF09pm0E790IEp0xkX6TU_1utcUuCiTh94yCJhAGx6SXefa07CGtU3IPcuTtZG9FG8QIYKMOPtUgdsLcVFzJdpSZD9uEcDG7hQTpQ3cKdXj9LhP4yQB1jRpGQhbwC8gJQBiFbvO29pSO1WbjUee9ffwLOxiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCFBxEtdEl5Mq8cvhR-5AJBjXr-hAqOQrGqBMhPuxPZ661q9O38iXb1NE39NxqA5i2TpYsR8emDC5kNKgKjE_cetdjIrDQQw9fizTzuCtqm-JdXPqdvXL9aPHgu9oWMb410lnqVQD2Gh1s73QjyYWstl_In8WJFgGEtRMsQF8CqAWcYc0ErVCidP6IpUFJjorFHRPxOalusMYS0zAAlf15YoCWnUFiNl0xzdvA7Yls30oNhUTzLEljul_fz0bpZL2wk6g-0hO2X8ZTVNPTOKKdKBCicOcMfI2fw8LeukjDusRXD7Kf3J8Q8t7uU3F7_V2tY_zQVAva0OzF3XXdecsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8qx3g4_8sC1JlxUbjtMO4TK9AfJp8pZvoKldsgtqcxU2x-yQjNSYUnc51hzn7_Y7r0X4gWb_YRGXjEoMLQ7NTUerDcqpsOwzHEJiz8t96fFpP9Qz6pWyr0_l3Gx8-Wi8FzUp2XFbmR9kkgBBSDpxQBK6JJFibX7FvBm2iWx2lVEtba3KIQLuziX2M_59HLIwFzG9T6BNfEEQ1AXmp_Rzy2z1XCJgIFB98a3gaDuHFtGO5lCb5gd6qaCILk0prvFDLK5r1L3TO1XmYoZTQEtIo6YJJM9JSazYKDZKqJau2LelWa_rsMN3kbowaCrZavG9eYwMN3S4t13yZu-A172TQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PahItEOztz_-LzkOm6-SaLmfpVwkk62VwXP_751LP0ZReQ-AZCPSers7KvdhrattrCmI6PqqMMf1A4EGG2U8jJ0jZE_Fh1fKIwE-xfgdnX3KtCG9tez07pSA2Ub8hx9OLRGEknWyD0hBNUavHG-B89qRYbe0pcG1q1WNWROAfPyRU955t-Ba9iNTQp0z1UyqK6oCgbM1a_eK0X98FK1cf8nTTMxRvsWSOBZNQ0NYhsC_aFMRaZROwmdSCmtUIKm5duwe7wzSoPDLqY8Ycej5Mp9WkcdOvX-_QYQWaq8zE2GSux8F3cuOdxKK-WftVS7ntOSrhR_wlwqoaVwZTrXfRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_Qibl2vrLcNEUObWW8gkyXU8fFQPTJ7Q7jGXbcmu7jygn3wbOszYH2iYNnqZoK2KRBHMPFdz7mVKtehJQHsSmkrm4dxiNeuZZSIb_XkRZkU33b49xxDcWriWosrD96kQOrzcbLAGkUNsA6wvktfQ-P431nboCmu0gDUQcXrbQ-jgjiMkxntWrD0VYE-UrCd9NWLGqBuZ3jJJgXrNqotUxA0I4Jjs7SUTf6nTRzjSRH3vsg5_iTlBf8qbQhiIZD_oQe44G3dwPwBXqJ0MYizvSx-g1DTqEFiDEfUi8w4h-HcHnmcz9LbTyZwbR2y5kLxrToFvWCV_wx7rI8yTiohlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMoQ675kN2LsyrIEjwWGchXzb6DKbQ9rx3YaPOCbqd5AmGVLg9an6AELb0F_EigR7BMpvyPJ2elRm9hAmHRhhUYKWCq5d1eRXCfZqB8_DxkPB0Go1NK601lHWZ4-oLpzPQCrv8YMot2E1lmUJpVGXMQt7YWVr2gBCnQQXjXl_2uWiTCcVUOfvsMBy5_1jcgQonGD7wqzmsexI6OqtSFGWkunj8nzOMDl00vwWoAUgkeF2dMK4a18D-E0DkLkFPCDdOojKlOwRWjpza9ettvDg00RR9ZxEv6SwAuS_xWgXGxqOjvYhrrxYg6k9wwXbcbWgLlguRON_yJVa5S-77ZNbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBkko6nrK4ubExW5nG04sQuH-gSRqmqrNhmloJ0KeAsE14D0_OvEVuCPboXaHgyA7k33PAOzIwBV-kREoj_Qmgil8Mc_ielMDX6vnOa5eoMCTehIW6TPjGfzJhddMeBvvRrUuEXVSZQgV0h1j5hrME7qM7-c2dHET-1F9Qny7O7TW0GYvsmNymKotcL_uctaDIr8fn7NcxvdulqeDiscpTZhR_M60FcvfZYUpqQ4P10_udJpt-n9wzx6HiH8KA84ZyURWfvdpsucUWj5-O6vBCHnbB7u06VkRkagzxUVurWq2BISTj4RKmf9As_ymYUZoBKPpU2iRizqHhNG6LHXqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jg042pIZ1C6j7jXl-HSylOeFGvGHWGqjatC4obaTDfgt25oez4xTDqXCwTMvEtLi1tZU1Xpq4kc27Y3P74W_quGclScd8gqeuuMuRdz1EZy5LjRuTfpCcEMK_HfQulNCq1kQjk5hrmuuMbV2MP3ku2CalNPZjn_4RIyI0_SzdBjgA89rGQ68cHZ9nhExha4rh0pqMbMdwhmsaTQwWocRBYVq2nsSSBkK0ShbU_SG4cHwyrcdDpI8HBN5g2kzVfmgC-wXblQVTHWS5uHerJTs5tdPIY62Gyt4V9B4gJipK0sUIDHvueCCYsZcpUUJHnIZh_UYgMZ_RbInT6ZyQ4ogFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiGWRhSKa6LvqNShYhx1RtitvknsetULt9Dd9YS0ObT8KYySFaMbsvUcKeE9ZoHyOCaOua0lQYjhwI8MIY8CDIVzPUTX8A4RTYH5YtYSqPUYYsrS6De9Aes29lRtymp2KwAMm04kKlLwQ0L9ZgbZ8Zu9TlCjMpa-GM8Y7zPdFDWMj98X_vV4yctK_--LgbMuke9ma50Kpu-SlA4MZKU2y6Jd1UpXDNHfP9VjpZ-sEX0CG_17tmfUey6eLXaH-EtoJz8cf4EI8OpFiFHiTNZHUoQ8oVY4vRZ5qU0wo6nh4QeaKf6Ed8sObEOiAjHbitVgmhLBy4Eaq61Nll7ZlTUJQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMebcj5BRhgKvCzPgMiY5c8_XQ-zAALrsVDQoSPfCgsuA_xLqNrj-ft91V4OTr2ojyb3HxzPkwZIP5ubQre-0rGyiFdYJ_X99K6oII1N1LNEpesG02ydjGkAx1CTRZDV32rkpIFNSKfWxnnZMkz_lko59mAK95ZOUyoF7-zoCyPbv3xp_WbhvrhiHmedb3OGRa8pONOcBLHo0bleRhOw9S4AkhpxcLf7uYECz8P4ikcpPOziTGEVAT-gxlA8XWJClD-qBjvlsZwwL9LIkOfKH4-8Ir8WFuWok6hLUm4Xwqm9fjRYS2NF2ZFa8Kk_VhSAVIer0cwQdGFjLyuFnlPgqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8lvPHwyVJS6JZFg-REOnv9a0wYjwyFeHiHvhFTFGNIZNWYnmtFDjvsa8upcVgKkzqIC80Op9qm9FUCddoJiRWQea3e4YYcmP-BjKfZv2Mq3Avsh6o1nPh0BtH13C_DHxxR2-O7F02iBQgx61pn2U7jk5rKc0q1Jy651xpyJB4Wp13Eb9_7F8Vovhq5VQG3K6p0kChRBiq0_HI3ieV3qq_Tk33c3apqeRnVJjZA7vkWnDb7_Poai-JZta2FcusABZpU1Z-hRYcjhuontlMl5GF8kG_GeymMrJ4TlxYJifb0FfctRfSU9CdtUdvzT0nuCOVVYDpu9-LYsfYS-IYe7Pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5KjV2Z3cBuYeAbda429O8a_Rvy0Lmr1X7BaITIPL40373x-mPDFrgWbm32pjvpJ2eDP4cIm09SnKahN030rOYheiSl3bMhMdBPCqSIaXFb8Ix-B8xbJozfCP9PhbN3BUr9V2-zmP22bBZWj4FcqCXTnbd3xt6p-g1PuvHMConK5x2M4HYjHDE6YzUxceR_y3tcDcs81xS_huqqxfBMKGh02q_yKeydlA3RYoOBNDf53siGRKb_G6II9jKxfxHX_d3RoUDhI4odK1am8k-HWX3ttKjrs4Y7Yh9SS8BXtPq2intTfsy3JHH332E9lozFgdUuFXRWXj4NR952wT2rzig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pw0Zi-kDSEt_YfQQVO_BxIV-gTyuPZw6UY-5E5NBHw3Kn7oUWEriYK66Txpg84_CcYY-e0Ac9Ht2E5xNbaglzlM8qWIbOOp2MmGBmIlLK7xLsWs89y6vs5lGe1Np0osCV_l7inyWnpALyHNSJRUoYoGBZ343j3eh3rb-FvW1IGDBuAMV1S_WGJp6Ior_oub9ut77lIQRlEDn1ho468XWsk--UESrB37sQ5yyUwQ4BwYl0yEbzSC1fro8FsEATBNX3_zHaXLKKsNxyey5kdPy90agxRf6SbF7FySNZvFficPUyydsKjb17_AdH1MhinBoRTuVrmWbLyL9loEFjh9xDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pzo0TVulCYfaCwOrco2f-Qlib_UY4FNpduWTWI1alRJm6ix4Oo8jEsER_MuyJzY684S0CDR4mtSTPHE4i8Scui6m38nqfVyhjNMc5FYz3liHOaI5dzDUlO1O4FEMLaIIC2vV-CTezyhYHY7JZcWppHlgPeTt2V62_pBw3z8B7RfG4c0np01LVOEbIdNbSydOT63W7szO9tSNixEaF5phR9RIqLTV3sM_Cn0bDkyk1MXW8pNdP6OyJjG3xUcr8yjMswpbKGizU60vPVlQGM5LvyRJSQuXK8Qe3GDv2buw0ga3pHAOfYKQfNK_-KvisXpgggVDS1CDw3363i-oze367A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7867" target="_blank">📅 16:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7866">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRheD2B3eZjnfHtzrUGvevOTF9WZJ5HqhyuQj4sWoR0Ez5VY3OcStZhIdoMmYsxyMH3iW108-QTmjeincphRSV8FDrvNej47D9RDXwDRXStF4p2TSQ5o_xyofv4XTtMeaech80BIYeqfs1ROtgbUzKm82gjx3VBO_bWvdFxUCLDg3JjbDlvBKouwzM8-SlhzWDUeHzsIsjYC2fW7_WyxK84WxOqSKMaCrgOpvPLN0P3EGYGf8lU7hGRwj84N6qbTcMBo-Hi4nCmoxuYytgX4fHr27iriPzIaDhfgpGTE9auesNcnfFQ96cJZSTXpqC25oUc4gztlVYuHdTOx83zm5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9r7JMvQV3JIKVBbz4RkLRW44bc5bvyZABfmxm79B7vlFzmreVvA2uEYkJX0S_GdBavioDQhwWE7yrrCBloX76ZA4lxxtuSBlgENll7n7LwD4-EGvxT7bRkC9ZU2NV5dZSA9KmbTLfSa6fWGsNUhQ58IaZVi5vHMEsn070gJnkpKIo6TZQvaa4D2dROSsdwDS6NM4C9iiZ5-4sPNcJgSZpU_2IdwxS9mv2Y0bI8uady3tJKl9cN4GST_dhp4DmtCtZudG1RixqLZeCtBRErkckNCbhXt9k6s2YqoB0WFu1fHbWgrDTzsqx6qpRC7R0g5zMFIaoP1fzHc5y4x1A2Fdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/prn9vrMdekaZ5pVFtYJHY5TJCeI0QGVPCrV05i6GamjPKrapyULR4RYyWMJ3MwIejOMzlSW6sjEmEOkUZfJc2rK_DrF6unQoPNVHA7zjABa-E5ZVUl22ggr1AizLhAtAopdSq0d1psWkanw2AcZEoHnJdoanfcYjGbnirj5zgLD08LL23eTx8NTTdXDEdCZwoq5RgZGG6FFt5bL80VyYDrML7ZwTP7SrRHBk9Rwz_eo05bvG5LFr8pnKezlg98g_tUKgJ9eZP21ymueVytacfIQWd8LWrd8QsmzBPT2P71vwE_9S1WVI24qB0VlFMzL5klceZPBWeyWCA0HuzVhpQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iSQr61AY6hhZAyqiUo_4jhuxCP96ArfblaYpPi1UkJ9Ywyy0Z62-8R5V-faXc_NYwh17vDfnLFWRjBBE__mHD4Lv55-6uowvEX17jdPwdIEf8T8xJ4l5Ndk6OpQiIA128pzlIIJMrazF0fqB-AJZSw6e6igDau8pJiMH0rgZ20ztLDtJMJsyWpq8GyfWyBqdfikZBzOxgix0sldV-iLBFjHth7aWl597Vq344joiWpc_0n1LPG-1wpQBYTAvdO15ReaixNB6ke1r_p0peA6whSdkzyBtI4fjW5NrgdKAJiK1ZVDLcKg0X3X92zudh2CFn11--cPdg3V6yHOWhcjVNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=PZjKYZsCbTUmFsoFJCb-I2eNAS2d1bKGxwn5HGyg7mwhXdUgAZDoyetvkgz5fbyrZ2IAerzmqHEEpDOS5EMHqRAoPTUDvOwH9WiDrHv41Wll692oHOo5UwqqvxXb6mU4JkZXVlMPJzghftufqzuLj4IjMvOfW19exMoiYY322UB8dx18OXmcCH9tEXq-px5s_AORURG-yHml_4TuJITNwLP36KehkSGNfKKBCDQOITMdhzi5U2vcfQfSVEPRRgwq69THfAusWJBj5ooqDZDDtzH2TGy0Fl5vNw6QOMgSircuKrm7pSBYqJCUWak3FKj6grVGUgQRJyWNYHNPZczOVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=PZjKYZsCbTUmFsoFJCb-I2eNAS2d1bKGxwn5HGyg7mwhXdUgAZDoyetvkgz5fbyrZ2IAerzmqHEEpDOS5EMHqRAoPTUDvOwH9WiDrHv41Wll692oHOo5UwqqvxXb6mU4JkZXVlMPJzghftufqzuLj4IjMvOfW19exMoiYY322UB8dx18OXmcCH9tEXq-px5s_AORURG-yHml_4TuJITNwLP36KehkSGNfKKBCDQOITMdhzi5U2vcfQfSVEPRRgwq69THfAusWJBj5ooqDZDDtzH2TGy0Fl5vNw6QOMgSircuKrm7pSBYqJCUWak3FKj6grVGUgQRJyWNYHNPZczOVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7859" target="_blank">📅 22:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7858">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ll1VL8ZA97j5a-oDnwwwd-01vyuE5345pilyPdyjVdhPCIYx1ta5x-6w_xZ12TM7M4MJxEbDB2G9wQMz-uF_-MVuzCQRX9MQeO4EK3vxnWWtr1CKLwMR4gto3IysCLuR1n2PgXYYqx27jiFAzre0coZ6VknMcipiPP6JUgPChB9XG3D5OiRqruAkEMsUjWDI5eZsjQFBZONPw4SOsXur9fqCaC0jJKl07dTJfUpy8EqiTFwKSBUcTi8SH8qaeZnZJ3F0DNbB5DMUJpIpbsNMr8VURS4W-P7SJPwjDedSP8IhxtCoYWbO82n0NDPKYdsPQxI2fY2xcazpoZNQhKG3Eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Noqy2WETVYOhESyHniOnDgI0G3REEGF6TFr8-6dmr7JrLxt_E16YV36-SaufxECH5QKT-QDYEieF_Xbu_myxzgGND_5dgL1uYdYXsPcjKsBNbAUMW0Co9ZCvF9KGq1S08aKfcWMGQS6tjlz9vdyj2RY_XvVNUkByLQ4NfklQIntH1dOxjRG7G9-hXwyyDESD335GEVoa9wWmLWFoloKgcrVCPaiw7CrW7djlgJHThlVTM0KEmyLTh5_G4yUzoZV1MZbtf_IG-2mFJEEmfw5-5uLYzfzodp4GjjX7Z1jqgv1p1VA0SyxIle8iqyJOSj7e2UWrjI6IVnogK4_fW6HTxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7857" target="_blank">📅 16:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7856">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX-Ssj3AHsTogJE0JKkgfgc0TBAAcLi5o_PX3ORUStshX-FJva_B3EKXRsk4fSSZgMj5nfyb8bU_fNX020owuVcDv1eyKx9EzANZfJRle8x64iRS8i4wCowcxEi06VwMJ0h1vw8J5D5Hh1Bje33kHjs15wU463VBntisyfHbFS0eHpX9Zzc5h43ACFPGU2CFc_s36HZUQs6ozb_1B_VRDlAT3HjWS5RCL2tnuxi5YFv5DRY7oPqb2Uxqp8rS_00FhdVKv1ThRKN5ldRWIksvAozPIUCuKzBf4kk_L6HCErSteljtiH59HkeX0jAAxeeUo1cNuY2aSbpXrwQ6Yeanpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7852">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7852" target="_blank">📅 10:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7849">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=nA8KQR28Ewr86_ky8_KYdeYDz-7RoAaGsnTOy0gmTxJMLbYZsBQMmnpngVVT1Y9Hyed51_lODpH5KYN3VjGhK4uqX3Ujw_-JXEvPSZ06pz6MI_2dwI2OGWU9zQWmsWTSFch3wELdHcW87Hllu4Gm7X4eSwZzx8AbdowFyUSXTwsgA4tWNki1y9MRhNniG6QZcX4LGEdiqlObbOf3Q4OomCJbMmhydDvW41oO7d-2tJQNfJlxysqlBNigS1Ya6bmjmen6Du7RPMb3fnJIWyv1d1x38ogbMBYKbYNNPRgy3PSEDOZL_TxTK-V0j6WoE03xcbzS-PS6izKW2JjBsGKf-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=nA8KQR28Ewr86_ky8_KYdeYDz-7RoAaGsnTOy0gmTxJMLbYZsBQMmnpngVVT1Y9Hyed51_lODpH5KYN3VjGhK4uqX3Ujw_-JXEvPSZ06pz6MI_2dwI2OGWU9zQWmsWTSFch3wELdHcW87Hllu4Gm7X4eSwZzx8AbdowFyUSXTwsgA4tWNki1y9MRhNniG6QZcX4LGEdiqlObbOf3Q4OomCJbMmhydDvW41oO7d-2tJQNfJlxysqlBNigS1Ya6bmjmen6Du7RPMb3fnJIWyv1d1x38ogbMBYKbYNNPRgy3PSEDOZL_TxTK-V0j6WoE03xcbzS-PS6izKW2JjBsGKf-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦀
کلاد Opus 5.5 می‌تواند انیمیشن‌هایی را از کد تولید کند.
کافی است موضوع را توصیف کنید و از آن بخواهید از پایتون یا جاوا اسکریپت استفاده کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7849" target="_blank">📅 10:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7848">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7848" target="_blank">📅 23:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7847">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyLMpU33rV9yXo4wH1ba3jgTzyB53q8eA0xEDn7CxHoF_1359dt7KlERJbP3AEsrb7BBtsa81bgA3cAYwQYtB6hmz4rl76oRND8zt3ni--C7dgbM8kg_qs9-JRqWA9I-o7_d9e_iz63uaiFC3t52n5XTb0xEAlYS24FNKCyt6wYGHQZHoxW6V9m9DU8k3rqNm89WNZ2MHVwY50VkVcKYt8tcFe5f0Audih3J_cHBn7DmWlYFGDM-3iuLaGqg0FheK6F4VFWGL7AbzaWF7kNCOM9Qro5LIqsls0juEFk9_AnFwvITN3o2JeB3dldrUm4JCnR-_PNIWSmYr3nlnVgrMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک 3 مدل منتشر شده امشب
🚀
مدل Opus 5.5 با اختلاف زیاد در صدر جدول
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7847" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7842">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LWiM04N7zWgXBrWd64T_cYPHoF12cf0xAm8UbBMhsStwKyhpzGI6MEgzHhFg-TqSQnfyuCROSmvqT0hCKrReb-wX7qCLYElfXv8QErPCLW3DF6i6CdQd5NtUCWDt7UJL3Ux2gWuWOXGn5sfBo99AyPIGdRBRVj1S6udUNRxljA6Qc95FZ7_SgEWG5_yi0BXGQLyKBRaxXrAckJFzYM77lq5H7v6osbjKDPzWIGPlkBMyhchrnycZfZeYIsSwsBy7GSGbq-XS7fHgx88ITtxJTJ0GzJaxmKk9krX1jxMMTJVeO5E4K7WhoWiI2diRypu6h52HISGJf1Cixez66Y_lSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k_ZOeUo8vrNYdxdj--RLyBvWFafVgPsq6GK8FlJcsJXRnnb5qNfRdbjbgXsw2xdWAVj9lsdwAvlO27dO_vLmx9CopTsoMw6ouaELGCSntUckVRwh2J-dhjzLRoFIC52f8tLvz_ESmhJMC6W0Ggt-9kQEL5z8rbBIGxc4EsN6NrjkYycD7-aaEKQ0DhV-2pG7InD1OjwcyXOwMwoU8vf9W7_mnDFzj10buqya1DX_1VhAFOyjj9SEQd42qnNBPbEki9Ayw7CyCXpW6wVdQNoOVWEQv5j1mO127-7-CVT4nJ7lG7efLGX7prgfsfNiDjZNzYV0zBLug2Er2BdZreb1Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OOfEbUiUvrl9400P7LAEWnU1uVmHjxv575zU_Md28COFcf2ZgVr3MnXK7zEPx3h5PYp1Nb6P5_nZLRrcGQPTkPLh86EEIDc4IS55qaOQ2S0ynxP2rJIIZ9s-l6mBwycNEvrojHQHDrNE8M9Mp5MPbrJhtLxWFbSFr03Qa3Ko4SpFT_6V6nyVDGchRzMa0ISl8Vf-hOkcPrLQVO3ELEl7VhVxyoZTwYRH3L0mLxsxw5D-DugVsyJ49RGZAJ6bbiirfPv3AAHMXmrM1hhnGRzdzQmFZsVxoNk5NB_fjEO8YFg2b2h3_A1IN_7GSKHxevHQF_NzaqjALDATYuKBkzK2CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUpfK5M60kSUK8zjL3jOzVixGqbuKbTPsmo8mmdIUpAkgVxi1FjVm0FMgfrbsKaZV7QXKT3VkeNMRLjnWUd4ndvK3j-tyJgkBZX77fPnuajFR7zbXGCsNVONduJGlkFXf7R49_PaYc0V6jTtFaD-OjLL8D_H2bbx4nns7enylXJvR2uYv02tQMFw5v_JZ7MJQ8zfyprzRe7rSUc4mMItKGNdunxzFCVbucepFPt7Wkhkg9zxHEb4MTF_0rwPH36tqBgfqbdTvApSHx_-TJtZ4UyBZIzY3SlJ3mlnRIvyxxNAQfmFyHrdOgYhzqyfjgncI18rOFABsP94sm0fJmv7pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZZr_ClqbL0v8ysf7QiUCBDstUxdptYnsk7D7VlT0G8aijbyRt3jYpJ51jMra7gF2b5IbfiTnnAAd7X0WN5wuE-8rc_0DXZPErDGJ2kefIdoEpyi69MiOWxVDltb5F2rOjF6WYWTuEgG55nzkipedRKCHRYumE3qS7fQ7smyULwQdVJlf56RTuyU6oAfStEFH5-gm03KRMHmqkF4ppi3fSZVxSCRHS8pp5Znh7AoLYVvZK9mi0uqnfHUVmhrNorLt6BJpgo2-_M0mMgREPELA_nYm4Y8mQuZfICZtwbpfpjeuTHFZAaw8fqzLUoYu-PW4XHJv8cf8myb5cdnwfAaBVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJ-JQWzX6Wc19xIcxg-X9jW3wwa03HD0p-beMxSiDDzkGXRUXN9-lnz0ijIHKZ8Y44wtEkEFIsBcEv9gBSttxB4SI0NEb3KOz0IbXnGzikFxxBO4ZhNmXKfISyIbHvSIbQJ95VSo6-CjBf5WnjzRaxahVqDZecXATk64EIR5ZR6CKGr-Su5-QhCK4jiPr7n2yWNLrtYV0lR-tDP8akyKsFxB3g8HQEw27ZuPDoNs8_EUfPbmQmoSDauTKC2ZR0Bo32JURal1_QrmJnuy82czBEDKpfhFm2zFAP2dN9o8U67OXn75lCDK62DlryF2j7-DElgjcIFT5h7KQ3deGs26_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7841" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7834">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=hAv8XIoqsvU6pxMG4M2cxzsF9DMxquIp-bPZQ5qMjCSEE0tDV-GguY4X0ZuE-HpCGWURwgt-Wg43Q-SHczxJQeguv3vjhS9LzlJ28rEhbBlv-tpL4_H0bLO7O-Ol-2lJf4moZ9tcDJQ8PLmzT6a_2tiylntlX-2JNL7R6QUH7iWMErxjHAuNiJ_4BFxoE3hLsxfKF8Pzqz3udYG2Azph8Dioek3EaVkyCjrpQvV_mRCIoA8QbQ8nj8IDOOuU22iyZA6EzLuLd2hqCOG5ns0X2l5Hn3J7FrwvrNLYfMgNiMnj3JrFpMPhCEEjDZNHAaNX-FEs2bOMM8tRJbtknDMrcg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=hAv8XIoqsvU6pxMG4M2cxzsF9DMxquIp-bPZQ5qMjCSEE0tDV-GguY4X0ZuE-HpCGWURwgt-Wg43Q-SHczxJQeguv3vjhS9LzlJ28rEhbBlv-tpL4_H0bLO7O-Ol-2lJf4moZ9tcDJQ8PLmzT6a_2tiylntlX-2JNL7R6QUH7iWMErxjHAuNiJ_4BFxoE3hLsxfKF8Pzqz3udYG2Azph8Dioek3EaVkyCjrpQvV_mRCIoA8QbQ8nj8IDOOuU22iyZA6EzLuLd2hqCOG5ns0X2l5Hn3J7FrwvrNLYfMgNiMnj3JrFpMPhCEEjDZNHAaNX-FEs2bOMM8tRJbtknDMrcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJODsSuW9lUsAw-3Ma0JI7BQse_IxGu6hmVNRlUzT3Ce0yHrmbYNY-UXmNLK7jWzh6-f58jrSexxUm_G_CSkQf0iclNrOA6R3BR9LC2PaTbLIhCfpigrhMOBSRczYkLxUP-Zw8TXwZZ6u4wPIjfRHLtVKBmWy49pl4eRmncYp9XzGVgiN4qz5pZJ_dhK4muYIoWoYp_lSX5SY3Q637iGQEfE_IL7y8OpAlzvywmmfZmn_DS0bKJSlT84mgjHt2ceE21iIGf2okYD9EVr7BcFhR0JnT7f0nvSMB9l3yjia5bQmnBPa5hJ88gWIlsXWyce1_-RnBWJP3a8lBld_UMsPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfXWRdWqUrydfpQcF3a1Q3NUv8IcjH9W7cHQ-OQqztWZsElQuIvBYYostIQ6JGQppihp6VPo3Lq6BaKxvpqdB-wAKj2Mk52QDTxYzXKNJ41fwotxzzArA5nKymhGHEOlesPzqOdfSJ70-1FusDKAiUDBfc1pS1LB2okSHzfw8SzG2T82bISvQVapqRqlh6mZ2osEnGbhi2f8882Tt8LPm27GQCuR0C-AI7wjLArGUUPX2Sh7EVyjfjBVgDgN4qiK_qKqqNUG5nvrC_BKi332iLjj2-zcIZ1jDx3WcbLHag6NMBWAj9m4GHTHsiA7_DRC6acfOTHUNGq8QTDpARGBKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7824" target="_blank">📅 15:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7823">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrqLSd9LgN3-yQplruH_KSC64q9aDUd_LNo0DdumkrmkSym2bBLYQSKWZGaVr4SIbKOV1ZAmtrRanaqLLxyfhcx4tnYD2B_e2OSc5AxxECuYBkMPilAi0ZkyuKaC7eSZDyVCDH6_97U1cdxBTKgAY7BaumHRgVLqyZB9wgRHYkq6gNbwWGzSN8GGrIyFdzfvP1MI5ZJOhdmzHW8oQwo8DmKhe9SoLwIXP_uuR9IdR5Fl5wrNUDmGncvvEUuvkvtTHP0kPWzQX1yJ3gSr02ikHKUgp3zxTE7wJ8kwno67LTBTzvMKzFY5QTmbkyiPscHV6k4FBUgxxcLIVCkax5XrWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6HUNy94-H-Cn3uDzfqAWgnrY1xSRxVMmqzC2Lx7umoC8vDvBTGmbVNdk2kA5YmUeUQ71tjFRtO6tI2gL4MFjXwLgMD_TW6nW6gUAOS-wzy2mMCPGIu649EHCFO9ZC8eT_fBtrMLXuRBA5FH1bezFJ4l7X2m1ftNmizkCpDoDTevtv9immWs4-2jqRJd9TOXF6cd-WxWmyPqM2rCwlDS8m0xLKBaKBmG6Mf2JWxqdcZe2mF8atcWUEnns3JhJSdwE0K6_ftG5YCaiY0BcBsmYG7BWnDz_9NwA7P5xYalkzPspjSeS5mrWcjEr6WWzjf1EWyVQ83jgxi1MruxJOPLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
وضعیت فعلی بازار هوش مصنوعی
💀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7822" target="_blank">📅 12:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7821">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iVzNgXetbIbQJXniT38-R760EcISd4xfmb3pgzkaqvTSklLGfq24AI5GlZaYEQivBMDa_Ftnmo3lYFyFELK3wQrJQXQn6T7mUXuaa5reaqGP661dv83PE-HqkySVNBEV90_hUyEqCMpmUHJghdnBs0r-sGQ3kF16m1hzdmrPWMNTJ22CZkSuH0bM6rTwJoHh3cQHiyepJHDBYlPv1ajFt6NctU5BhkvwsYQJX-Isg3eWV7f3Dw1nSTiW_tHcTgz2rjtnqrghYDAJqUoa94ziaI1bH17B-917D8pPBTkIjneXc6zfnboIMH2bOWm9nTGAaHEynoV8hr__ISQgoAyg2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WaBujTtsS4-wwCevkApbYOcCJnk1eCvID8ZlUt8BkFZ4GvBSYuNAeGm-eUB_m9JfbuDN36byYvT8dTTsh8IusMxFeTBxlV8Ofo2A1BW9nxgDDmb9dDsX9Zg90zM0mWh7sXINaiwI8_dDpBHB-AaFGe25qiz9-e328NlZTKh7hL2S4RZWYu7-tI2Cf8oxascZy4IGN3eQmrWrLpxFCa9awmT_HvOJ0szjndVlzSW3ln26ofY6rFdROFRa0KPf3XM0thN8AGLrAz52GZmF5m4Cntcxkvo2K-ShzMvmgvcaWPArSgoht-ggibLYOtn99e6KkZjhaLf24TH4XPAv9bOxcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VT6tAJ8quAqTjS7G8WjuP69AzrtdADuQBDQjelEZ4XlpCnGnpmgEj2PGZlAPFi_g1NAARl5o5i2QZmAPNkVwjuV8kPDjJZTCECbwowqgeBIRzb8RYKIMLtzH-LJbeSd25Pss1hAjTD2-eirhDgP-G3gZOywE9lfsUGep25c-WLLVgaakO-4DKkwbCox9Q02Mj6tXXanTMYGbiAeFvApiYxV3sXztfTv_TqFWrwm6cEtvZ9fpzyd-fk1hGf4sU_Cm-vFSiTe383u87DV7_ZEum-aOddx8lJlqxt03QAXsMkReOpUIgpTIdAZPzvEsQXtMqSBlebBOmuSM7c0wa0sm6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7818" target="_blank">📅 10:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7817">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elvaYK8D0DhqOj_oDIDNGBK7ErCiLHdwlmq8UwR-kHIxZAVZHEpG_4dgL0cnSIGto6S_cYeNXG7P1f2EtsbLH9xzlgVZU8KQFdhqR1f08kKOZeyil-v4a24bw11Q-trWSy0UvWULXdj2C2e4sH2Fhu9ORH1cqYXzN3ZKZ36f_l_gMepHy9Do5ZBhdUf3PQOL23moVOx3efht2DHTB73pKhyXTIsvAxZaJNWeygAeC-zJrcwl3ngQAwfe8waRl5aRn9EIQjlrhaDJmOac1Nix3OPruPuuenG8V7KDlapD0Xm6Ue_MdPa_3gdHFxDSYDvuu5HMf-CENAL3Jf3UzIQ0RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی
یه پرامپت از ساخت بازی مار بازی توی حالت ultra speed mimo 2.6
توی کمتر از یک دقیقه واقعا پشمام
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7817" target="_blank">📅 01:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7816">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXRuARszpsR35uuOAVdn2Oo8GwJnGqwsyP6yDOVJh3kiu_TgSOLD83ql8wcNpdiYMmcjGoYXDIfDyUDTGMD_evUclm0XO1-634vvqhhas-Hnga2pPvCc_6MUWPa3y1l2GC05t4_9bQEIZpDGOKi9guxqcCwpdTbM9_WL5U3jT_DA05lDwvj2fIct1f89Ba1STVjiVFVomBrhDwGj_ypJRtjQdGDhDU887M3XvvNqRZsOQs3S0HEw3VZ0ViVVKdzI9QatyAceUEJKpHfdBCj_Dohn0ZT8tVa6f3hYpeL8GFGiwIoNu7qOK9HMKu2o5QFEei1eK9s8hefB5krGXMZw1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد   درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در…</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7816" target="_blank">📅 01:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7815">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد
درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در API منتشر کرد. سه نقطه پایانی (endpoint) جدید در کنسول توسعه‌دهندگان ظاهر شدند:
؛ mimo-v2.6-flash، mimo-v2.6-pro و مدل پرچمدار با سرعت بالا mimo-v2.6-pro-ultraspeed.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7815" target="_blank">📅 01:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7814">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=h732AVC4cPfXvtdo63KQ7fuqiuFJzY66pUIgpiqXOw6HHPRgK5lMgk-XG5pCoZD9-emMDxuOl8B2YDaBkWHWLIcVQ6rH69cv5c3wHbrq6SJv_DT_h-OobfhLOayGcmTZlmSN92AyXDeFulsLBlaf1lE4ZqeDG0jBEQs1H_qHR3rBjHVvP0HwzwQ0GLSYOu1GL9cK2gBhOseezuGDli7uyFLi-R9vr6u5_5TIVQL4SFuAcBI-pd1kiSeSe1pzyXF3X-CAy26fpqv_fxl7eaXs9s7eGIX2dhwIMDrOw7tcS9DJAMOeOS0TNQGZ_b7qRmHVQisA9bNnO9BgDuI5t8ssyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=h732AVC4cPfXvtdo63KQ7fuqiuFJzY66pUIgpiqXOw6HHPRgK5lMgk-XG5pCoZD9-emMDxuOl8B2YDaBkWHWLIcVQ6rH69cv5c3wHbrq6SJv_DT_h-OobfhLOayGcmTZlmSN92AyXDeFulsLBlaf1lE4ZqeDG0jBEQs1H_qHR3rBjHVvP0HwzwQ0GLSYOu1GL9cK2gBhOseezuGDli7uyFLi-R9vr6u5_5TIVQL4SFuAcBI-pd1kiSeSe1pzyXF3X-CAy26fpqv_fxl7eaXs9s7eGIX2dhwIMDrOw7tcS9DJAMOeOS0TNQGZ_b7qRmHVQisA9bNnO9BgDuI5t8ssyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل در حال ترین کردن
Gemini 4 pro
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7814" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7813">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">😎
از 265,000 اعتبار رایگان برای استفاده از مدل‌های برتر مانند GPT 6 ASTRA، CLAUDE FABLE 5.1، GLM 5.3، و غیره بهره‌مند شوید.  یک حساب کاربری جدید ایجاد کنید و فوراً 250,000 اعتبار دریافت کنید. با ورود روزانه 15,000 اعتبار دیگر کسب کنید و با انجام وظایف، اعتبار…</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7813" target="_blank">📅 22:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7811">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⚡️
یک خبر خوب برای طرفداران VS Code و GitHub Copilot!
اکستنشن
🔀
Router Models منتشر شد!
با این اکستنشن می‌تونید مدل‌های مختلف AI و Providerهای
OpenAI-compatible
رو مستقیماً داخل
Copilot Chat
استفاده کنید؛ از OpenRouter و Ollama گرفته تا APIهای شخصی و مدل‌های Local.
🤯
🔥
قابلیت‌هایی مثل:
🤔
مدیریت چند API Key و Failover
🤔
تشخیص و فیلتر مدل‌های رایگان
🤔
پشتیبانی از VS Code Settings Sync
🤔
؛Import تنظیمات 9router / OmniRouter
🤔
ذخیره امن API Keyها در Secure Storage
با دادن
🌟
دلگرمی بدید.
🔗
GitHub:
https://github.com/web-elite/router-models
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7811" target="_blank">📅 22:09 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
