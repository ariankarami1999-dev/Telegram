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
<p>@archivetell • 👥 10.2K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 21:34:41</div>
<hr>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 893 · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDkz79Z3NmIelZ_f1FqXey6ZO14d5G9mNgcSQ8WyiJOZfUnG4kSQEU9uUB2cjEnTBQZIJWHvwjgUilFl9yKWjrL2ELy21hjdl4LKB8cUG86vRcDr1jskZpxkW0tmUbE4P9FRG7CyYQgrAC4bT9L8jRyo36XKD4MccYfFTfdCUcRrTi9GaBapryJ1EXAEEwuRLqd07D12lOPoD9COpQBKnbE0BB_7CaNNP1xCscbrvdw-Ua4-ts8OVKmKRgbsHbQEnM7utLaPKJnf4jPnRoac1lgo4-dW3QtOsmCEiQpuD7qZTmN2arZKKNJgKD4TnQ1M9UIq_W-fkLBuwchUi0uwXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚡️
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
‏
📌
گزارش کامل تغییر سیاست
‏
🌐
اطلاعیه در کانال AI Copilot
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpOdGyIzDD4eZvAsI0AIfHf8GH2HaW5CgKsSYUyBHCx2NjPL1azXLigTOzo5jsJc-jM3Ehio6QT-0x41MdUUzeOPKjjIeljXvPdlOswf2jLdh9hbYVZbqIZCQHm47_pBzq1gFjt51YHbuNCdKYOVy0a7-MOQ1ZGTvGuG5UsvkZluUrwb9pZS-GWew27maZ-ETrcpcagJvX8MrFfpND4Uw21NniE25ke8Bl1sVquXXZY72tT_DMudjWjqh-79jlB_QETAnFVgh40s3soLEA0Im7ctggs9E6BlcK0VzIUFFt30vv-dweMXzzIfm4uiXb6zw9wwIZmj00-n9o0U4h97LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOagb_vLCD5vpB4SSRC_OiX4I8w4iTtrOBGQiGkByFRt0PFvbT-m-FzLdiJVh2xGSJM6SOorhWG5oW2roF59GNf7p4XYO05bhNn_up_kadv9jKu4unMttJICdF0Jwn_xyFT5rSY_EkD77CLKOHrOSb5bJctKe_txZ2q1bwpWG8ZTJDZFe7EwYlcjPnFOvAH30lYdsdE1O0RG30Pdj6d899i0HRdeL9_xWrKaQqzCbi3yLNtFdqRoqeYqvtRke3o77cWr5sbtvF4mvqVPR8_0d0ANUWGtmX3PDMS-1QlT1FpHq5ILPTpVJMCnsT-LoNiSRPka0e0YHbDWWH-RlXUSEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By_mwIKZaErkyMbaLhDbfIUboxJa1JABxg65vS3m25bRyz6ahKF4PpcA73mvLTGEJ7fI1W2Wls6n-5UfjUCHQjZWOmdYnYMcmi_Xahm3xUXaJdQPyAbkQtdAc4CPt53cz4xvAo00YtdY3Kb8eFYNJ-hRgfLnCD-_ZOYewMcr3J8sLBjsi3nCuzx2bx-7NxRlhgiheWkDxni_BhsfYGfi6p8s_zf8jqK46wzSxVDe7LzjUYJYG02_iRaJ4UDZ96DfmfgXpbxSyIRmbTCYmHFzCKD_K1a438_kXqvAqJEa8dE7L82QsvzOBiXxDAFSCw2jYj_sWoqyLe7WH6f1OrlrMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sujCjJhGW-Wgi0ukNMBwTLMNmXTWUW1LbusKahT3rS66qje974nv37f3-jjs8AmBhApYGoxSNsg-ZUhMVcioTHfVHZP3FDraTsZeEsXpkMNR7lO4VbT7nlU8eFGVEEZERYtu2lyor9pfXjUAeoOHhVrtr2CvuDkGcVrCJQpLjPimQWri6Gc28L1DXT4hzhOMP8GE7dW6viHOjZ8aJ2ZCPoMMROdfy3Ggul1CcRF2n5bEEZk7vUDbr-B8Lk6Ie6paU7HaTJuL4F4Ln8xd320SPqSWPvMPlsWFOc_bgZVQudMAwO180-ugB3x4Iku1kzEaSy5DvQrG_ed8DXGQd60Tdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwN9fI66lxk2kd41wDDtLNBNB3PXHUap_xAS_U2-9yPLPsZBiqR-rpmlxb6YQoQKqLy7gqdjBil-51h10oHwScWoWYLZcxze5l4At65p2nGhaomhwtyjCVRIlaPj6DyYE9x7Tpb5z_GvSJdq2yRmQcUFRvQLou56L-9EJCQaKd838wlwHb6_tcmxcR5KVsah4nfOHdUyUalVm8tWaVHdNWc7Hb8PXLnQ7OeHZLuVjr5SW9EhYO3gSmNkFjCkakPdrppAfZui6pczr9uc2xmyuMbY69oTSkCV7uZWIcN654urzxbQwSNVOcaIzLohbqOTBdnpDjQ9fqxjTBAlny2qRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tK12YRxTjJDo_SfS_6NqDH2jNmAraTExl9aINmMVx9OZDu0B6eSaYE8l-oeoD4-TgWDzdw0Zylx-cCcyHRX3fLvlcJTxCFkl-FUw5WPqfNUmvoxyuzt8kWQjab5ldCKwXlbPPGrJRYPTyS5KSXpPJS-kefAvqHW9Gnz5yhjAXBzv_MhGEU1MZNY9CUTo1G50O6QOynG_jw8dQLR3sDkX4B5ME5Or8L6O5oaP86n5vJwrkoWYxg6kd8suVaIvk5KqNvU-NzIu8GPnoCGOWqy_7wtCT03lfqp2puMKigmDS556FE1ViHgwhrzcLNRde2wJl9kZWvOyMHRG6dy9nI4deA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q8uqE7eXaaGR3_6nrqX6IGI87u_0fq_vEwb4YXUY2YqaINLD-i0Vm5eKHRl2gSkqges3bMjcl_GRrlaSU4TpyYEKuQgrwHVE5A2WK37yjivg9TkIXayX8ejlv_GVqfalHk0W_URnaLFyWHtCJSIyvo_S_hGm9uKcdZhesmmJ8JrjtiNI9qs-PBtEKwOaBlXrCROaIOdTgGWfY14eWGSyt1WtL6KMisULjiRfrEVXT7KpMSOVIo2Xd4YI-FVdXDUuOaPPKxVG7LU_M0uAIkoJKgtvhCI5-GfQtIGuKhw4Bsa8jzcuic_XfAUq1OepcycHHaBeq__rYUbY1waoM8Bv0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-2u2dRwNVPL20JBGn0M0MPSmxAQ5cCQLoy86d7gUUyQMs6bbNULffcAhkfDlxkH6tYqMJiId0a9kBAVAyZf4BRPf2GPVqzY3ghW_Bu3biHYp_2q4sW3H-G2lEFmfkSHvEOZnv4AEQfduZzOCJ9rC5boybdLUxehlZy48pSHlByay_eW8AlNfuDYS1eOy_XpeLSuyqzJS-kHczRrALTO8l_4lo0kSer2-4W9SngzGCd7-OvNL35oagp4yvVD3OuXSegU3Fub0AQXIPanh47JUEkH-YEf7L7xxFcxKY6WlUooAQogbX_KIDfRGA9f6ODEnXv8jFqutywW6GVY80ZSbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMtyXQMeJB0OPZ8bObH7rKtXhZeui_dnjMb4R2pVS7aQ2aESHSbB87gFAuqUwvx6Fzjqoc-KbVOKc061Rn5BECKh2oS_mX_07SRWaEH6eZ-Pm-Sbgu_KZ_G_630RGqWX3PozG_3YjNOAyOr9yEMmwk3ZucO7JkywHGzclsF4vD49WkqrbE-NiUh934bwH1NqvzdCNZNMB7WLsr-zZWu2Bq3tWryfG_PWVxIEN2KoOB4WBFfKZ_wdZFkooKf8XboZkJwKg1nfoHOdu9veVbeG222-d6ZDLUGrlhqQBZeshrnG3mlQwM8_FhUaDgzIAwzu2ZYC-SHq9BfFktgoOSwdaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DXtU7pF5pvJBKJSCxTKfqt0pCU8MccHrUYhA93JWHMWEdaU6j6zng7N_Wz_1NNgbc-iAcVDhxPPkPTqx4nnT3mBQLG_TtzMw4q9ZxF9CZxsVC-Q8YoHgAMAVBJdIL1LJSapJyN-yxWN5cUn6w5XgaYAEz9tvrNttKwUWfuIixn3YCtvU_h_ecrvZvA80aD63PRgyX8KnOcJ6c_t-ie0aaXLJdtCRbFBSv_3LJunJGLDahO3Gc882C3eCnqTgS_KkQ7zRm8UuW_rplKt0V8ZN6n8N4b7XIO_ZqzJIcOG8EmX8hb9hOMXMTKaAkyMECijcNqa3YpzYxHQIe-kbjaQ-gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GevjdCzUNJEm2LaqN8dRwwRabpWUV67k3GSdVQp6TJjMzT-F5jiZ1HhoU7kUmQhpn7fmK7GHLEfvjmif9ggT84ctgRYRHJjJ73pjLgG1FmlFJUTVX7co7iSqTQ7NY8951qtleOk1TXySppsDeZSYNKuXi_6IFXmtAfwFofxHf70LcUsLOrQlvqMpc-JLjCdo8LAilZTLegi6gqY9uu78UIBPhn6gFVTZdYENMbAyo-FC1U8dSwbnMKgbsWPwCOLNJsX8zpqVL8iP_vyeM1hWCUWSfGkHe47_QeZMCZN1gIg5DoXtvv9S3g2UYFZM3qp6zecOfs-xi0Ly8CHK_DI33g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rozgtkFTL3v8ciZo3XH95yac0Palqo2huK4jlc7D-PUjlIY5Gm_BiiXM_GW7pYm8JPBR5HwgbgxhEbKQ45__uFBL-u2c66h6UHsyZkbJl2492jA_NLCWwkMDjvnZ73tatiPgglHjr5B-MhvMngHcKvbGOgSEvKgwOURVNErzZrCHNhoR_G4_j6qrtkyAeCnf6XMdj0e6ETpXRylSeP0qs8huqGGasLZQhGwAHdHeqU5BEcFmHloSzIab7WNQPBxW5lmSuE5sAGkw_neH_iFOCycjoNxEMGEB0fV7owOVLucaxqcOxJ3IlBoXGm5TWEjtGwzYCJscTLunpRvs4J-JjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/npIFBivjVPB4bJytNi78IdVjRGy_tvDjaAABR1NLbi4Nxgq3KM9m5XdwR75jvp6huzA12UZgM9Qpfztwr-BA6IlQwZjjEUuK0E7Pas5TIXhAMcV-fCvF7NLOjslUl8eqromOHfbcv7WYctpF9OYv2SegkTuVHvmJdSpjX6IvWm04MMGDR8zEpvv3B2gcUuagn1J0LseSB35N_cK071J1eSug_U_aSdFGVumUtFGyWYCpHW6FyZ6kWH1nXTEbfEFPoJ1iduNey_4acz_zD7wqI3oC6HWycJdO5QxJ84lO_Zni5Jo1yhWR4ylpAUe4BkMV4fGtCozo3gM4H3q59mArrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Opv5GktO2LtZ6DvG3_FHuZ_eZDW7u5pYjmFN8jHJi7eIYEM-mXZH1p_YXA32fYGNLv1oyfPoD-gmO3k97twOXCU8cEJYCxpRafrPaA8onF_foC0sKC5jPhPEzu41MrP9Z1MSSfhE7EIIpty0uoZnMvE9E18HtQSO-XN8-M1WlCmtO-W4peXa4LyKeNJlJqIXz8TcBUDilqgiynsgLVCYuEYphwYpMzdsPzgi1l72NZ_kSgBTb1Ccl9EeenoB3ABMsWDXJQomsv4XtQd_O5Cb7BcF7OpoRpjSW98DFyp-0v5i6OwCOzJSj-nj2BVA2V4ZjyP_kHG-0xXQPC-eqmPCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AydhqWzbU2yel3FpPI1o2O1WeNst49LOKJ4Oqv1VOgRS948z3g2dNeZaZ1T7d3x8R6arL-FT0YmRjNjneuStg2tZScLQUxKSUFujNyzgleD4JuZ2bRBpMcpqaYIqwJsJT0SuqnTJ99fIGMSu7CDQS5DTLQKsW6JCoBy5cbV07iSFjH7_ndlEJmEpwmPV8E2qqs10Sc585x7L3TfLat7thw8YybtTfMMLi6VDXDjvWhGhvWYWkJZLmuAQkze2p7BhRL_AGtG09yi66URdDbw5QAUVms39JZx7nyL6WLYj5Ce3BpgoSO-sqhrolZgPZ9zNG3xYJmc8Gcu_Xe8X_GXhGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FbXA4gF2r5c3lI2UI9LC1Qj59Z3lNo_Jt0U5DACX_YhXxn2ZjBoglDfB07gWdAKV0VEZ7eAqu9sInJB12rlT3M2WuvujG1nsmQYyXfk6WPnx6sjLbfoCQbsyk2t04Ie5gc8tWI49PdmpEp_bKtn7mrl2XMkhG19SdJzcyupIQw4mNY6BsvcBEx56BIU2aSpDlgzwC0Ijo9ofVRTuyf1aq5Muev1672dIpLOpg5M9Ie2b76zajQq05jQKkBaEXtn8yrUkUIWly_L3gbTcfejGbgZhHIomJQeKoozel60-pMV8wWfndQTMkFbrCG4qLVJ4B4qqGg17L1zzexhSYg611A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EFGUe9TU__u669a9gVy6k27o7AiMV-9PqLz18VWolJ0PiDts1ckE_zfrjP9mZ9p1n0ZPQf7NTZQLwEkrgl6zHtGPkmIYdmtLcf_MOlHdA9HW8L-GthfN3y6zP-ykpIufI8Snr7FY20W251WC_fDOR3cU52gmqjn-2dMvd3bjdA2so81_4FLsmwp-3-N4ZDn5cl6Mjplt1ZWk8bLr6IXpoEuy4pZG6ALF6W52jRHjSE8RvxllCHepjzi5Xzdg6J3x3EYrSkgyvl_4izwi63aYOKdVc6f7dE9SrnPOt3z6HuMlaehp8G5Do1ophcePJc0ROyK9k9AUhS2wBDXaZ7KOWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jN0KnKuUyJDHOlf6fKynkQRpj6I8eU1eKoaRRpvcRLJcN2hGjosjm6H4SudJZfKsjvAAGIU_Pjmfq_x5Jy5YUIQgFQZcms8MU8KVH_y5XpP_iDKjXzJLD4wDhPvjYBr2GW_GCDTWJOyzeQd2U6hCUWQh5jAVmx_TEWLBmv4kXsI1qtYRzDvuS-IR73YhqAbD_kRzz3fIwYXV99RI7970o68Cmer3E4w8qnucKjPkjMMEMVzWQ41_txY3enHjfkr541mCTka-UuwiFAErVayh5W0ajv2_xXXEc1jVjFCPfMGDTOJvVHnJ0UXNFPeeL8_X4nU2iR3Fv24YlmvxUJVgPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anxLVFrYAwu5wpwarOYYsjQi1nLeaxKBCNjiWFYkVC1WeE9raCPnrA76_GkraW2TdEEOL9iM72vMJz2i5tctCKlsF2YmvydyzcCTrpPR0-I8xUdaEwvtDvApZwsYvA0t9x1E4YsvWtp6eh3mfcfOdDuFYswKGY4SJA0BkTgXpx7s4UJg02dCSQnvskY4o1uSUQ97skUqeCRALeoAN1IP0qp5sVLcAxrrqmoamg0PauG633UU3-K91zwOZ4Oz7-BJ88jonOO0p_CR_N-8e8smWmCksk4KTROaR2jYhT_KWAlHkgctA_CzMAxWDTxGQjBhY1H0qELqe6x65ihWD_LD_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POILBQf9ULTnV2Pzn_b7-SIBnWslchgHvtkW5wZdNzNGi1mye1yZ_dMppi58LaxAWw5knWjFN1EMKrXlnmHqfdaMCenXitZ_Sy7JQpLyduDhphy6fX0DkGtMqMwULY-I17xEzvkvUGVusHz0pNdla-foBuYIr8tQijtOg4KF59sUxc34eY11dvSlCKCvw5buHi15Q3tzuM7kz6vDoUEJ_uTsk2dhpjtQUvPutq8-sUtchW29IUVEQiO4IoM4WPiru9pFIunSYZxjOwDWIRcBf-p2psMyBBKdiPObXOiLtBoniu4N6RcAnXolZXgUe4OUapMcSII6jENrqMdkjrHPwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9pC-yfwWVyCCrOigNNWWFP4uOWTZaThCBv0WkZ35YJ2EMILMbkRCAPI7VXhDLk35bJRZMAV4a6XyIBtM3f9Lpm1vBLgXOJ5P1NM3heRM3n0K1MbQqrY4UL9SKmGuPNpoSnMjNgKn_12uAlhGBDD7RDuLiC5iyinVXKUGmJgQQOLtlveX63-FCiaCYPRlBDzjdOrGPEIVbJK-ifNprL5wUcyXg3H8TburCE80Ijlz6NAaJ2WbPgkkH6u_IAc_k5__Qt4tcNK8wQ36PR4IG9KvmmPFRLeXOAuShZzdV1ZXR6ItXBnBpgn4jfsaMEe2nLsPneKSyJyzYiUdvHozSzaiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b2PxsOez7oNrqMGoxbYTXz3nq0j7SoRJ_7Z3Qac0PgLE7fL8uGJ3MlbqQUwm311i7mTVWjonQQ0qp2qq2rTCPMWhTr0EfmvAmWizceItO75ekhAgwWt_cxvFy3vEGF4a4ABVqI1J5Fta4JixqNweagDI-OPMwY3LnoFFaBtRyHh5Kpnj34mMtkoU6T_lSwKRso4aRtCyHj2iNm1md5CsVQH9QD1UW0NkF0nh0BpG7bWEo6uOeQZN5SFjFu44jpBY9bm7Tn3Di_BhaicZX7qbKlaBvt7yFgEUPf39TPAet5RzoJ8zXyZc4p5nCAftBm5X7z2U2tmhTlJ_FAsHGZ4sSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FZvgC4RZ7FMl-aLaexUYP0LKOLiNb6TvlyEuGDlLhhj7DTdLJclqJIuD6qpwwZnwI-d1k2vaIN5kY_yH5R16NOtXNb-HvM0qY9FZCZwDFySpcnoVt2TXdyhpwuvgD53v6TC2eZ-3tmB09tTZpGphE_64XdIF0FuzG25-Z_sxZJuO2X4S08dZYiaNm_abcA3dDNMVEQhsSP3PB9-w8lpohuwcpneFBUDRu1j4apASHT90onl4pfvo2wOUzParcFZS2g_rdbO4gv7DSp2hKmz1IJONW4yM4Sh5MZ5CZcKwa1DdFki0H43XR3YRUM5idIBbVsBaKX9-XJot80AYxj4qWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ld51jimdpElXld5MHXt6nOEOs8lvflUJpZ3gd_RuoqQsCYhGADeBngOIrJ3NZNLAMFItDa1cyNmNLsE7b2-GW2IXpLy3ECmtL_IpLyv4tHTuuhE93PFi3eOeBXDDjUa57og_siOnJ1jY5IFCEeM-yqAUvIh22SuCDz0ymYg5sjXvkfu5AXq0kIixPbo-zxCt_w1MQ2NcJ9cwHEZ0P3nrbj1LoBVPnaoiXaVWj68lLgquT7J3VLLiJ-JfzD2oo-Fxu2y_GcjVOs8kOVSWDViNGxPeLDgciH_4ntmSMU0bvNqqmLdAZq1zUsbJDkDMYKLGFMHJaX5js8j2yJZUWbYxFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yf4vw_KSLB1uCd1-bxqy5a74gGJP5Vpoc5EkEtoNMfgWJTo44U51yvXO7AoS7Ba4TeqRSNmI6fc-9NlJsVhrUGX40r-sciKS1iSE_9FuJ2uv8tU-3KgnatgSPRQfZPqDEJQybAyGEZhoCe3wie-pkmsaXzN2CNoSJuAK2MBcUkGADAjDubhSEJgSGL0YPWDDTW3iQW148UlADhnIpZ3PArlZhFO3ax_JVP0YjGuD2zB07P_fFOMoo1k7YLKdIvbsOEsb_7UNSQPBSRdDEtaEcNw0aDMVxmsncxzPjq5eVQBu9Ewu7S59I1FvpEXSLOHf3nhA1dsHzsvQ2A8RNdMMEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l8U6UoLRk2HUI2Aa6kpHdjxxzE3M-cANGuRxacveaJVORyCj4Ao-vQjfn-MzxwhTW5IeLoQ6n2eg_kUmZieRbUuIx5Zx0cZcO6weCGd9XRIAkdqbtes3MuMbmX2xm_BBDrM7Krrnn7Xyg7_4soadoF1oEO8lC3pBlw4hfEtxMmAtrHaV81212I5MTwRELDrPxvqAOxeYdZ3Oza44ftMwAigKPu66UYEd7SOp_gWCIT1lgEMO_f_As7MTBK8qFAYXTMAHiSLA2uUpoZuDr_VqlAkzHylAiaVMJxwj5H7CSTcsBpNDcHGXbMRK4GJSMB2oVaUICPjYImSzwNtvgnQp7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3SBgU3iTah9WEgV5GLiC4D5qrNPla6qizvMi810elNdziDCyksDhHUFPS8VXGrC9EBOxGkPe9TyMYcB_nGGk6eWepgsQ05_DqWDfAhsxpE2Pagh-iGPRiQxa9y3UGIbt7Ig7TETHeBBPTwLEWbVTXJPXGuMvE44qSC6uqX3cWcgKKsI9U-SZskHSuZhGUPy9PqCDsk_IndkRjzDFGx57HsQQ9yGJ9H-qPF8RJM1hAF3PEn00TFC8DN-zL6q67DkbaP0qZds6K8Pn4GZKQJkJ-SKGV8BZV2QmJyFOqXL4OW67VGmxEvdYPL6JszfDpCIsq9O7ppAFpiZXApFckDugg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMuVeZOHZoZHbvX7MUfzRLTieNFLEM3-Y9hJjEyUdj9n_h_wPR9bFGJLtxGdKFQtKD1eFxUo6gNkA4a1_Y_2bxTvcAixzIWeORwvXoZBWzPA_37bO_Ou1ZHJ6ZGJmt5pzzlBwTJJOUGvTjNiQUQGjBzmcUuNgL-vQY8wfEokuIWvvmW9tZaFpQUP0HIxZ2uiA-XfCUzAnwe32-quIrNrjz6VlKEFJj7kxf0raTSy8jzwMngKs1Z2caEUBWKZhRgB87RK_A4LUIGAz8pkfxju8lR_4GC5imkuHxvRPJhdYzmep3aGVA9keeYuwYvORW4gRHoA2MWsAiyMEe0JktrLEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enRcy2w3GqslTf02mXuRdEB3dAtQeKgUnAXQYdogjAMnEfVVa8V-dnhl3tKqbsiOdGbnjtG0l6p5ojEzbDLMq5rENBz74VxvFDxGnDZXjusSrwDAXTYsqOuHYw_l8FmHUh1sOlEYYvZgJjx_FV2oTaUvcoqXgnm3Uue61JpE4W9rDH_9xF7dqCr8PTOy4tukaGSt4rnn2vdYaW7gryFdsfeiHvtOnrpd0hpS6mX5M3bc7O0-VISoSa9-IgDWLokNpjsMSsTu6pvw_xMXaUsRloYtkC4vhOBhbz_tsYLJ-G8mfgKQedXXw6BOV8VTflgCSuGdQLQqEGS_mv1kGkBHHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkAjDqU5582ihO2A07DD8FI7iLah79O7vnqYz3zEN1tvM1Y7JJvs9GdhLd2BzMnOPEXO_jSOhniCw-Nj95chRdnVirxDs95wqZ1pRmrMzNtVoDWOMpOFUXEsq0bdKy3UjGNnrz1OzOY5mcQOhAtZxbnTEt9t0VYG_Ex4_uliNBELSgnxQjkdbJXJ8mhG_U8yAL_EYvSPTx7o3LElroJhu4G7dbkjyRXE21SQj-9U9TvjBxe6ukUBif4bU9Yss-xxfHXanWqEPp65bY6QG0AYr7ISUpqlVGNZk61nLqMbHk4OlCwfuiFLiYQuag1QRRKudmByh0e0T3Wu28ycwyboWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkfkTqz9mQ1smsk3r2UUDaoOTuy-MnxWhesXqZo-jRuUTg3t8GXujdR5kyUa10t3PX9c7ACgOPu6-p4c_fi_fuD8jClp-x-V5RO0wj7tBvN8ghuXhfL6qhzL_1YgcQJIxWdH7dIxzVtWRBkbK2athsuqyaUHn7VmQNerkd3-D3rUunWR9xm5XKDjqxo8SMMHa-Y4GayHsI4S6RTiunK77Pdnpe9gVmcMXOc1fvNO_BNh7qJ144_k_1uy1tfdSkfA6erSqFuGv6U7yfbRKI2q6VnSlylHCNjJT12Vz4-qUPhxDMXk5ujbSa3_NtP7k3BYzoGLXui4JfUApSaBh3EUdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nv29TrB_uNfvBKf5cfCT2EFtS81St4Umf-yawY125kIf6cVdQQTXyYsuJ7109F-lKxDfNiquQ_28SQe34sTl_ijfJA12M0SxrH3hPsxzqnCMR4dHT7-0lUxBdIhf1uVfWPvxCzqHLgO4Yz8IjTQjyxn37vdbq11eI9Xu5FYVp0EzoqNttjwznkLGMyGraZnrtFYOar95vchqTKgnJXGJNg4D1xz0VOIcCEvScBCSSqwQ6aR4JeiXt7ISqEiKdWgh9TdORNPfdnqZxbYvwtbE53qTAWM4wbQlfMD60lN7DQAEKoQlAdEmb1MPUpbqOdivh7yZCECuVYlmnTJQvMwkzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=f4HjaKkL9qfpiY6kybKoovOenDW5sC3pRfQ02jBi9OPQdNIDJam0vgF2CfdFwTuFiXopWFSO-PHrPvHHmYAXq1prUiw2vCmZ8OEwHnE8sd5b2FNHcNunjle4Pw2nSZpYixWBMj3pvmR8QO-6hbGtYcGJu8lpGwoHSmIhHXBlr0N80KMD4NHdu80gW9zWljazq039DtC93QU_aAdWziQkpkNiNcj4DUn-dzs4XNM5476RY5SlL0nwcJy7vKA9O6hA4AJVvA5fzmo0C0gueksM2EqVjvpXiVkjz0D-0tBHMzsevPXxm5wYlAl8atL_REpiQaneGVV0A6KEtR73WxkApw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=f4HjaKkL9qfpiY6kybKoovOenDW5sC3pRfQ02jBi9OPQdNIDJam0vgF2CfdFwTuFiXopWFSO-PHrPvHHmYAXq1prUiw2vCmZ8OEwHnE8sd5b2FNHcNunjle4Pw2nSZpYixWBMj3pvmR8QO-6hbGtYcGJu8lpGwoHSmIhHXBlr0N80KMD4NHdu80gW9zWljazq039DtC93QU_aAdWziQkpkNiNcj4DUn-dzs4XNM5476RY5SlL0nwcJy7vKA9O6hA4AJVvA5fzmo0C0gueksM2EqVjvpXiVkjz0D-0tBHMzsevPXxm5wYlAl8atL_REpiQaneGVV0A6KEtR73WxkApw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2anBJ3mj32VH-fx7WrBgMtWeOf7LwGXr-YY7NV5esEbpwphOR-Ow4tEpSZUyvi5wHlKkRjMt8GSYvGdSOa9zwpEAvqFDNebTJuA1TMvtRmKAz4CNkVQT98-wd_EN_lPcuQFMvV-RBei2--VxIbWuy_s6TLfAKKzJzvGsnPUzsZgJGQT3tz-glh2D1JIFMLD7vyyng6x5CC26NS6ZWH3HgwhNifVIji6Cj8GUij0orSXLLTKTIQeMWVV4am5qSD7yzwHgnazn7mLzgv3EZ6fRPiMdRwTIvEKtqJ4-ZDxtNKFHOdqDW5qKL9qMSRIW4PCroQHvNQTzEZsPKurWJULiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f49pZ061_wPF-t4g9KHm7sjPPWINpiES5Hrm9-uZIM3KiH6uZ_mWFyCap5t63dcwT8TlNQIxqmxhEgRxwVPoEdy-_qQg0Mw3QmoVrQCSzsHDSVhdJtFcdeVfwV9x_EVKLsp9zM1_Xv8s8GaIFcEURH5I_0RVozqHPz41fDKNlrHF0r8YLeMya1hAVee9Y8esIGEEvsILXcmz01Yup94dIaWL5O9uxVaYE-kucKuas91i6wncuS0btpxh_Y_uiPd5b1zFx_d_iiiTaH4m9Np-lxR4n6ol5h-3nop-WlprtS7dBDukHOhbUEe5LP-BM_qybFU7DnpDi4i6grhVbI0ezw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oL7TWufkowuDMirAS1ManTXlS6e6bMsSxko67V2dM7axt30ILA1r2dIXEGE_1o1LW0Im-7GXDXYS_UdjyquWghaA9uaiQtIg_6wRYlz4C7mpUJXXAiwVKJ7dWGICAHoWYtHzqTH9kViV_QadHu0Vnl-DjF51bdszkrmMtzzT1uxvdKeCiTOphfFEBRfgelVUq_A2CqGms5lXJ38_tEsVaHi5ibVCZOWtRh9pcGTh-AvItLYfOFXq5QuSXASo0nSGsguUcACu5bSOSTWCxp_Nrg5sVwT9WYC1goWyxVnIECV6E3w76VrH4hCSjUwV55RulKK4UdE8SAG8u_sIg8x_-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSyPXpNHO_VUdyGjBulN0D-MG1FaL079NypDwqzaAvNGkhCLbrC2h03tR2v9Mgbw9H4tC0F4U5xUvWaeUw-q8htctC4snSJeLw48hqSpe2Rkmt3qhV1neGg0o77VjDoISjc3wIm4C6kZxg_jBaNjTfITa96D6HsXwkjwIbz9wGMsWjCtnIKw0KHhq3R_ufvzMhmqHSWR8bXOnrlomGHx_VcFmbIu-FB3bBBWiZ056X0yVtcX2mH6RzNYTowm-_nkhtPcB0QFPzxbSgy2NyTL5PIeSDMcZJzbm8qMec0zcKv_BcrBYUr2a420wVp4iPk_INxOoqwDEQfXJB3hHxqcJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWygCzMUUZ9e_Smc4Uvg9CvCZu5L1MP-u94pHwV2HflVgAW_EyLNoa1y0lye_Cgwwtm_ViJjxj91TRXGXi8tfGnJscpiSnk13K7lv3fxtgJHYsTMUeOJbmVkxHWQyONpLz8Uw1XQ2R_Er83RpEJDKOv0moa73fOuAz8SIyYzRi98p0dPFbGDdh56g-COcZwZzIM5JumS3LmiCW8ayrSIjX-rBN8JiFZUPMZGDIMkzSdC42vRlIFEC41U3KVD7l3lLRFWzDRKfStpa_aC7OeHUZoOlEfuIRxBocLt99SZNgoQ2_nJWh8J7SzrcZJOOnFKrS-AYBx-b8hNwpLwT7KaYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1Hhkeqg1KEfqRWlH2RogdKn4NSjRRKsnBwIOXnSqf0H3XKcOuaXFKCOn49WAF3aDrOLdfAfhwj3XJtrT0jeoLRsFzwqw1WwB8cw29sVGThBk8LB5L6eliLAhRJQCqWScpucZsrMDRxzE-neNmtQN7JC9wQHG7TSEngO-mT3xX_GcwaS69Pzxfsclo_TNRHZFaJCMQFT8uXw41ALLcljlOHdhbUscOEzjw_YnPHybsn8iElh3P9wh_0r13AFupg6sCwpv8ALssPlmo9KrP9L43yajgMiEEOswb7EXuNrz__jWfXkldHaog3k08pYkN_EcNMTYz7G1jxu0fpS6PPzJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7I3lp8LwiyLnpaxKb8zmeFAeqSWdQgK8lZ2WyYRUBiaKOtl-sr2qFk5l0v7MdhlZhp3zdYZjI4aWYC0ncVrEHLxx0dDo5zV2P-Ek7r-WPgtGnKUuxgjvnZGTMEfSDVczk9q4C9rtVTRr7s26VNBXM79cG-zD-dJaBNJObecz2ip670_YtC685_yEFe0FICv0xdbmxWai7d3gXRZTOgfBTK8JdbX9Fi6HlEWGE0lAwYrwnqxvh44wfVsRUPZYWAeZ064b5KM43ygZN6wJOCplOIrjvfDmoYYkSPY2MtgCO9_9ESKPUnFL1XSD8s-GjUw3pn5c_DWvu6D8KmUDuFNtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzMVxcQL3V7iefAL3oBWydYXUsClN-jBx_N4fpdzgAxs-xzNHj4DXg1lVAPRU8KHCqyIb7x2wnrGexpiDyDGsrZZR-svhv6KGPFQuuAyDBsTIa-vwscYnf3b1o0d8BtP6GcycX9GoBdxGR7S5DyJhvqp7HbtSD4yXjwkv0WUNlAUgpUQeJQfHJOlXFdR-N3eIDmNZreTMevaP7QSemUl9DfY-9ue3tFZCOe4AVcNYpLrxSO2r8xzRA-BHcIksmtUyE8Hkxnv7pSoHOSxSsq_q8_FK_z_8DskpNV7KmDC1na7_O-W-C-X5faPngIZtgVg5-Ha1HZXp1j0V-1wUHJBQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcJ7y9BUM6OJBHq9HMzlFNggfR8t56tLvsUUkASKn3Qa5vW8xmWlmZj53VKpgQ8-ALlvxbWpWfjwx0SuzKkCTz2k0miobUMy4O-hOxKER-yHxI2mxinJpKdOq1njLWu3eA8JGf0UeZVAfwyB7kzo00gAFOhJzx2QJv3QesFMgrRquXCaRIJsWzuf_ZV74Nr0RnwNmM5wxBluI6MfIpgonkCrV-7up2AhkyG9e3nzPN8OxFoThLcmdxAtp-2IX98c3RfdSxcVRwmjIOF-iUDEl773Nm06ubb_n2dpK13pcGYclA7_S6kgI09s2KX_xOmN3OltF4QX3dKWKsflIKjEuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpLq4SlSNWjM-KTnXaXUuhCjiWGKdlM9ZaSVleaD455IwgxVwTUnyIHBD5TcUxCYrxm8-j9E6vFeV-k4ttNU-kyyBRfqu7-elisQCLt_Ms9h3bPfecspxHoPnJrwLCd9muZtwgB2_DBI7_w-wAzJMqX-ysuioQ_8Kkf6CLKfjSFRK12vHUhP7yM9EJiMcF4FjSfWb5bBe1xx7RtzrHa9-55a_KsLouDQwvK0McyPtqtxPEUz-l3z25Rk0tdqzlaX9JLye2dr5jtCqfB2dyBjfu8DFGIvLtQWdh0Yz03jHEFTBG1GB9zl4yi7IWFBDnZelNGwFhMuW1VwIJxcCMg7GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ss7NC380yZCzXkFGv5b0PYMuaVUVo84il8gQxr4eYdLTtWotHt65cW5xcMopRPjdlTwdFZC7xf0nHrfWDGUkjgXEbKdHn_VylpouhfG5XsI4EA3pB2muTfh2OdE0jDDalLXKAYgA5VDy5B4sE3UdAM1r1HSPLvJXTaUJKGyAVdUXr8PsQJAUxsZT7Nw_DWNj3A0MgvMOnvGlxAc8VOIcvvLo_HfuwhXVvv-xDY3leH8dZomrQjstMwo05BYXLvsdJpl2Kkz2fKMrZLkc4caWiJx5b1hHvSV564JeLleOSYrdsnSYgoiFuaImaJGyBWGsFUcWs3XoMJbtRKRw-I4mHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZy-6gpRONn3DSjbi4d1OU3XeBugEepou1oyOfkSb_q5Au15GyqTZ22UUsRFTca6e1qI5GW4nrSuD6Vlwhe3Lxhk9kYAVT3QHP-dx_6kScVQKe0wpu9eUUU3wHQ_tOzo5SxCN6xs4c8OhDT1AaQRaRL-p1bQXRaKizkUJgHRMAaAcaRCsHVkpykdHQ5so4ch1aijX_Quoji6-nW0QgcTeaHG_p5_6cqX2UPGJKrUNmyCmPLEAummlw2WReot6ETai3XrF710S6WVFCqqJR5Jg02KX41hwgmbR566fOkpiu_sbA7888Hq3vgqGUeCQ8uKimivOyaNYlqPulP_XdNVig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIdq17rT_f1XfgV8rs2vTvm1tzs5uPddBTHpdNrzrzLIjDQ_7L9XKHnZDBhRHW6rhXRqi6m7_5vb0IVjKTc6PIc_3WJnZ3Z1nnoG6_KaUrvAPkGd7ltvkFvEGJ-hT1-ca0ZpsP3aSiwTYvKcvyXVxorMEW7KDs-vLwNWmeoVhmjx5cSyiqA7HeMnUvHPcnZ101OigAplDXR0T4cYG1-yA76XUXLkOtarmQmVfpaJEdIkrJrSEv9fO1Vx_DA_v4Pv0NS9hr4IWG9sBOhRivUNvh4HIWi-FqAgqYrhY43RupGy_yI7ckqfbo4ofcyQgAFRdISEfjTQJ_q5fSRU-5XIQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGyHYzYHFvczw-vi3SNbZPjIdLCk9yUWTxbWJer6zGQtOVoe8Yr0vn5lEWLc49NMbLgLFOr629WJwtMeTHS2x56j-U2KwvmRH6pOx6LI7nCJjMDKA2QlhtA-t_6CRbZJ1XzYk1bC1HzrwyT0l33aX-JpfBOWHWvubDrwoKUJiJKy64rf0r-Q8LJJt3FByxeazOSDmd1Fevjm2rhhYkmKjgyxN1R0jDmsyJ9dn2__TbkljPjkuux9rSbHHcKhW0e2RfcxuS_m0IfuGrxtv1aHxHI4AmvCidoLi2Wmq2kzspSVn-26UDKaAQEE9UERbTav5RU3J9jqaEjgX58euhDGtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usRFl76zbxnVHjahLjJrEE8dxSQb1PnHBEIHNyHYKzNSdQK242FSWNt14DwedD9blnqqEdFojNl7hUejrd_i5Y59vEQPLmmkFK0tiMNzt8G_jj-cdJKHVHo5v40f_fo5WPztbV5N2CxTNZRLPWy-etul7urKLWd0xILIsJlTdXM27fKJOdDvpgciBXQK9JAMT4AnU4o96LP3lM_zsKitJngfMGEReK-8Lh05ccPKu5Mc7gxZgBZwAqgGLVCrz7095SJRou5nsoYYGKn8a5TEUp2GJmxQ5XOdGdYX0RtNUcjYbegyqvZj27zWbpaFeaTbIqtNw_fqZ4pWXmlVaGlvtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7869" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7868">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jd2Y_UqphGPAgrXiHDs9L0dN4dDoO69GGAzHwg04bZjz8bNtQRS_zdw3SzgjF_hKy5AYxYc8ei0h9IzKUPQD0i5cpEhzSVkl92qnR_Tw5qpA24yceMORA44kEV_tW2B0aiUFIMUVRd51KZOlaqbCPXE_d-dzp9goc9TDhpkzBk0Ic-B1nOJX1c2PJDc3zvrjwqXbhJ8OZfaLCPdbJSsJEt_5rApIC-6kUWnj7-3aWKBfHXDlen8NZTiv_Mky5WiOerfA9q6F51TpjcaF4SKKv-O4ad9iaIDiXXDLxT_H6JYYNELBKPfrNvzD0o0Qmn4KGlcRU7vjew2PxExcY-na6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7868" target="_blank">📅 18:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7867">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJ_pALGxeM1LU8QX64sxn6WRc-jOwJEcyTe51_x1Vc1a1eLFzKsEffFi2zqeNxAAYNxDC3-FEfDNKjjgga5H3c8BhDhdZ5EP9Db9ZQ4pMtUiIFAEZpBc5tbczzVynIi83-fFP2Ho-9S9QTVHQrZM9vhAFMrh9SIP2wW47sdai5rYCBDnLGQuVCushFhcVzp9hiRVPW78g7LWCKmHBrMjVK3apoOWUDRBqTBkCLPSuiVnADRspuAea5lP5spMZU-y7RFitkPV5dXjsEzzTnTNEtuKYcK_ykqJjI7gsWWQ-QIeFC740d6rOwcP6dLEeZeBZ-8EQ6Dj53ZBPNzOioklcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7867" target="_blank">📅 16:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7866">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBiHt7pdGoEe1Xd9Ah7uqPZoaR9PFB3kfnLcNETCGxNWxf_Pgq5xbtmIhnQH88aslIc8hhXEYQzK1YRe4b_kveT7Ez7nofk_jXC71NNI3rb7FSp8gZpIuPQt-R-fN8a3gST4-CMaKXyUJ7i6Vkv0kGBlBQn75Dfo_2PpAjMS_vi1kMeHcB-OhAww_s9lnpGn8rQupel53FPVXH514bpUsAFb67v3LYBXNV1WrlvBs1K5biiK8Ssx1gzPMiOkliMHB7mDpavVeIbwtCb8ObUC_wkXkFCEdGX78qN-jZeR0w4sMJ3mRjZkV_p7LSGRW7J6v19qEjK5dbFkmzU49Lqzeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7866" target="_blank">📅 13:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7859">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YqxsBi95kAiaceWT83J1s5gMfVcLUhjV0pI43TkxpY44DOFReyld-OWHZOfTzw36EIxZrSkXz3RntslNC3fD75ptgQibs69y9oxalPgfpSL2SIbkLL8vE4jIDp3SOpHykdqLf_7HcgPlyF37L560UDUpDjHQkSE8l2_D6VfY-12wBjNaorJ1-HrZe2kj7C2WBqeZweWo42VaNtP2KD6wl0uwCZTDLG2JN9Oe7ZarsnxegjjHcwzj5YZuDNA-mVroQ9M_pQ5v_YD8vT3pCr6gNXdcjIVzjwLXhyjaxGcq8Dc4i7QQDECFcDgJjMrCXGOBwAV3px63ds8ObufnKB4h8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VeUYZloMUrf3fAYFDkTOusnpMYPChgpGwl5QnwerIacxUxt3QbXy3fjsx88OOnsLSn6cmihJdzxT7TABj5CCuSsSvzhEn7e0YzsWxH17hUSqao9VrOtpRWHjAiYjMWzEW2x117EtSDfyu1dLPZ6c9F_s5vGo6QThyJSr1kH4OVXaMZ8pzK-lMPl-_ZIGPPbKHW6hmTcH_kULqNWYTOCo4D5v55jGJzOjVcyWkE0HWGr3SG_j3J8v7RYIPUq3kw2lrPX-7a4eQcR2Tv8x-baaHm3tKleBcyK4JGYcx7bfzkmiIC0EpA_LvKV8D5_Ux6mJV541_RxUZ_siVWDojEflDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VgAonxr_XCp-jveHpKaqGUcc9AzcWK9WDCCwM3K856_jSgTiM-WmGl0BT_QKihe3KnL39CCsnMjid64W83FDshVJQJZ-a7bqlepnAnNzpHf9rs0r-AJ_zu1r0rrLSvp76jMt7V-YFiT2JxQWdKghMTTaP9hKydN9rfJISvt7Sen0DXRV13xND3lo4cpmOhEO2Ou1hXUQ5UjwVkQylYUyMCwGgtekIQVMWq3phPvhOl2xjrE7iMvCLJgTvW2zMDpGAqE2BjEcFmJJwL4luTpbKacYVk7qpYC1a8O0hB37WOt3dD91xYBov6eHY42qnGO58RaZbh0hdKMQmTnynOUCSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=RcYaGx2YCyzqcbtJ7uYmzZiANex3oxTiWuobSd7cJRl06ml_ZAicefiI22rWuNxWbDzuPtNwplmdTqZEemTCO-dbDZf7UOJuzJQNO_7ZoqDXGizeLLmBPyE1VqjDk9jbXeN3IyFcEHltduvqi9XQbUMSR3npz_n-YtRn2TkVIEYKsmHqPj3yXpekIf1OObrQqL1HC000Kz19Yy_oFBUwtgtpgQ8dRDVU89IBpLTO798APXQU-UyktCc5BnVoBnmyEzUzSH0TYVHR1xm59SYXOAjQUnl_edC38qst7O2mcQiX3y2m1_Zm7YQ4vw9RL_LygJ3SL0bjhU6l6kL5XokbRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=RcYaGx2YCyzqcbtJ7uYmzZiANex3oxTiWuobSd7cJRl06ml_ZAicefiI22rWuNxWbDzuPtNwplmdTqZEemTCO-dbDZf7UOJuzJQNO_7ZoqDXGizeLLmBPyE1VqjDk9jbXeN3IyFcEHltduvqi9XQbUMSR3npz_n-YtRn2TkVIEYKsmHqPj3yXpekIf1OObrQqL1HC000Kz19Yy_oFBUwtgtpgQ8dRDVU89IBpLTO798APXQU-UyktCc5BnVoBnmyEzUzSH0TYVHR1xm59SYXOAjQUnl_edC38qst7O2mcQiX3y2m1_Zm7YQ4vw9RL_LygJ3SL0bjhU6l6kL5XokbRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7859" target="_blank">📅 22:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7858">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYsiHpJzgYjTeIg5e7SSZiO3R949p_LJ8hQwtxoLNqT2ELeQhYkvE8nh86AJURiIUKbsDNGxyTFGT2dpI8HOQC7ilpBECMGnef19qY7fRDT8G_pElDSvU1Sqge997eDmUKTBPndUtz6yxElkVSUrS9jY5Ps1dMem5L89KagLLSFvMZPOdY8KIa1hh7TG09W_JwgwazIMLyH7oZg7p9fMJKk3u0rhaGjrIEeYt3sQFUBrlg-_82AXML0KdtFF3mPMJCAd5SdFiIRhkl_IwV74JU-7Hsk9sp5i3YHYNUYvE0h6VAau0kt7xGQcj9UboRuhVlCLP8jzyULyJrX6_N6u_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام دوباره یه قابلیت جذاب اضافه کرده
💥
🔥
حالا وقتی وارد پروفایل کسی می‌شین، بالای صفحه می‌تونین ببینین شخص معمولاً چقدر طول میکشه تا جواب پیام هارو بده
🥵
حتی یه رتبه‌بندی هم نشون می‌ده که سرعت جواب‌دادنشون نسبت به بقیه چطوره
🤐
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/ArchiveTell/7858" target="_blank">📅 20:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7857">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMSUGivuUGgPgso81Xs3tD9tFY8XQSN2JGVYL5uX7d0gudgSYA8TQVFq9ZzmQSGwVnd88x_A9rIlnU46eVoWGq4VSRnia2FAuqFQ5E58RUriY7G9mgkavM5qabRT6lanPntvtjWvwv7GeiC1WdR0BlSubqdi8ESNhortRK1NXCfIlhkCVv3AmVCt20VvIAWKW_mLfrMs7p4X7TifbLJ1LF3rM9k-PSZL808k4V5Iy5tYXovnEWBoW_1wvexbmHONwOB_hr02-vm36J2J-ILoR35vG7ws3EhWBJfTQGKYop_iC-Kx9m4JbskB9XVB1RrTi_c6ng1l4vpeEm92YfkELA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7857" target="_blank">📅 16:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7856">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7856" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7854">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWBiisFr451ALv6ymQw4gcKduXwgZbI5jeYX0UbP22Do6826owyrAL80CL4a8KkSB7tCDsFCKECYtmPBfYAQPs37bMoWq656FYSTBaoz8bajR8peoRZvcwy_-88kHdO17GkCdzVn2UEiicxErYrt8z5ds1jvHzAGzVUh0afan6UeABidzQqzVJYSNhaHPD2CKye6BzD4edFlIWZPcx8Xvpy44OuXxXExttuYYjwSVGDhnTg4mW-DP6Q-FdKIWrXl2eGDfCigqTV92r_h3GGPqv5eMO6JLNdRwg4ZeET6ewKhDHkGkN-By1e6cp60C_pY48uZkNVXGem_oERbf0BfmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7854" target="_blank">📅 12:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7853">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7852">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7852" target="_blank">📅 10:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7849">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=Yd3obn6Z1rXyPA4vwr6TsfV1l6Abuy0btZ6kf6BZ2SBADonkRcuEv4CVJ3oQgxKXBYizGoceBUVUDH_PXA7JHU9eZMupjWLluWDrYYWsuK_99_6rNcVAPUv9meMCaVTX_AC4FHyzB-SOzOJrhTsb3tqwWc3DD8uSsMUsqdXop6JxFLC3VqYv4mF4v1csUi_0RbZaRQHWPzGg45a-cGaVSpH5qwglE8qNRpgv1yj9eknqAyJepbntWQx6zN0FJXBw57AyB29h6YLw4lLFegU2qK1Qx5uMkFg-GpSQNe3S6iKUBWR86A_KqfuMAuw-cEBDmnizRdDFnVNuR-xW4_uxfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=Yd3obn6Z1rXyPA4vwr6TsfV1l6Abuy0btZ6kf6BZ2SBADonkRcuEv4CVJ3oQgxKXBYizGoceBUVUDH_PXA7JHU9eZMupjWLluWDrYYWsuK_99_6rNcVAPUv9meMCaVTX_AC4FHyzB-SOzOJrhTsb3tqwWc3DD8uSsMUsqdXop6JxFLC3VqYv4mF4v1csUi_0RbZaRQHWPzGg45a-cGaVSpH5qwglE8qNRpgv1yj9eknqAyJepbntWQx6zN0FJXBw57AyB29h6YLw4lLFegU2qK1Qx5uMkFg-GpSQNe3S6iKUBWR86A_KqfuMAuw-cEBDmnizRdDFnVNuR-xW4_uxfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦀
کلاد Opus 5.5 می‌تواند انیمیشن‌هایی را از کد تولید کند.
کافی است موضوع را توصیف کنید و از آن بخواهید از پایتون یا جاوا اسکریپت استفاده کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7849" target="_blank">📅 10:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7848">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7848" target="_blank">📅 23:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7847">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbvPqc-Chu7skRHmMdFdd3lKMKSKIOy1AwJ9mlC1Rbh3z89eIwt8qOiPh8dx70t_MukrXen7Mj31CXAi1wXG3jOBQepjKc7n-TKqj63CaqMD9AW4X6MRsSr9Ta0ruxAkd83m-gPAtEiqGR0-Mb48AkfLXfJ_Yq7AtLuXuABAoWloSearfC9mkv5KLw3kWsTYdiRxnAx4wTo_NOkSvMopsL9ZSW_kf-3Ir6FGuqVuYXxOqVBghoB1_QYr4e_xNYeu1Lud_O4ANUPH2z93QP1B3sy3IDJ6MWUy65X7vYexXoKWjoVPkccD_xAFdR0GaihM-9hOx4m0hzJ9aeyrtzZNCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک 3 مدل منتشر شده امشب
🚀
مدل Opus 5.5 با اختلاف زیاد در صدر جدول
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7847" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7842">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EHZd1jiK8HVYVpqQVJuSWPVf2DWBzm5E4FW4V1WVfq5QdmHt6eMEOrgCCls7j-FmQAWUVParjBxXaPwGncrvXCNWOGNy3vNDgfjYdiEUVhHKfd1Uuu6o28100E0dgNh70wrCrm3_vFhraaIXiCFON5gPcQC7IMbDaT8T2psygb7NAG0TNvnX4fqjgDE2o561wfXH6dLZFDYej9Ayh3NqidMqdXucIazsgWWdg5DhkmLIncdZnenHU7SsNi7htBQRM2l0h-rgcAJhdmuL0f4J3ZoVaGxoaPuF7n9HswJqv4NjOVSar9GnmD1fO6jBdkhxwq0NGDzl2OzV6IoWLQsBLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PFT4WmNHRo_Nx0mdTV2piC9-RXNYaDaDjQ9dXb0rYTqqdwlCV2gccmLlLSFuEv1mrOe3Dnl1lSDsRp03QMH3m9L2wCkDIx6QDCRUD8b8N84U8MYnwid4bWfKfQQouL1XateneUOoBJf5vQMLPdTs-jZcDi5a1XCIU1yapTVyKP9uLDKoiTlPtdmBOBHur6Bqkf_DNQastfk-UfouwqTmAgzQOTwul1PZzx4QHR9QqZ4Cpxp1WDJHvGG3CTevwfWKzJtEhvZbpVwkCd8IkAtDyCOdIO7mX6GLKqvA9INp8JnrF40E1xsc3zWdRndyMjZlkCmMhz-mOp9ePLf5OIyYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OvdLOqTTqAyJ37akScbiICcC28zv6x2JcoHpXenmWptTCt-Kv0jeg-rHtfU-vjS_52t6kE5sHgqkvxvZSErppw3qoi7Zn-T0jlzyfbgEJ-hnnrTtnvCIyZF7TS3BDv5N3jK47C5OL5LloF1pYuzUxGZBS85QHV-e9qdEi06y4MSFj_0hvFNha2bm3euAPLsBWEPqbPoNopyinYuQeu4qXOTI2dhfrXDpThbKh2H2RvZn2XkX7eRddZppjQgQKILTHx6BR7UN_PaIhrWc3Gi3g4vBgOEaKvjPm7hQ0v-rLbQFYkOA8_3qbKnA51mXRo6vtL-w575D2m1xtg_5A3KYKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oy76q0CFBQYEfbNhXQHsH2c3pi1U2C2wzy2F_BJcINY_GX1FbU3tin2FB7aMGA4LzZUm9GSh5dFI9cesyV0n0fS0B464hnDiI2E9-ktmuo6fZSe2h4M1GGQXcHwn2Ny4nqPtIkvtIqAA2fVszg9CiAL7Ef1jApMBVOrkXI9Gpp14ExkYH1ySZY6umkbNhm6ZK1V9JIWK32phxbDa81OveVk69dY-R-wSKhOXJIrWICWTUdVFvr8i1qvuyCp-hFXNodn3tkOXKZ8kmzbNIQ9iUUfBOJFHmfTokZdzeU0yApPedJh05H0p9tWZR0unauGC7OVxGanRIUisKgRBDfQHwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kyvc-mBqT0XDPjQBY0izcirLVpcxZO9cengW8s2v_9HeZNlGtTrEDLvlkSXV3thquB9xdLt4UXV9H1ML-d6vgzsmznFdkX8xRnmmJz3ipFLZKecWZKVJZnZPQSOsJcHf_hyQ9CdcSvw_wHO8IxIlMBfl9bxWe4az87xXNPz7xjAamCpCUlLfEVGshQZKaWHsg-amdHLXrlfYN1EWw4qZ_NHAf37ZvBIN8XeO3NPxEj8fuBLym1kpMOBDl64XoWBeXeYRjESqd5YjV4VLxaIYFYLVXNh35Q-vgnWJKuHos3pcEieIyaK9OsrEZn73ZtGn9GsRBlBEPWswx5QREvplLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aseNtcIGb_BCcm15spk2whXuVeQzo1NmeNFI6P5wUWAWg8XvhbWXS3reRtMJJVlDKOVbzd6l8Q7Peg17V49s7To_SXQFb0mf8txvbnXOHuQh61_QntekGEMjArCOLLLX7eGfQdYc6TLbHbSSZAEnTadlNeElYKMSxvJ0amb55HfnWZGRvxvPFcZ5RNW3Ae8m-LGXc0nHSFwsYkCj2TgIWHrkbi3YURd_qDUOKyQCHqDDt64_nFIu5nHFtcmFTkZnPLcJlVjlhh7N_ufDtPKss09ubNAtLLOj1ZDprU4MWYqA-68FNaOu2OB3BwsaIzdeghofjxvLH0CEsEhLPPSlcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7841" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7834">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=kb4OXdzjgcOVmWsHYJlLv1z6J8IAOJ0sHtwqg0lBZgMmquvf1Pm0UH-usgGP-CHt_nVkFjbY8C9x9MydrK2h5-91MmhIoeFbjLMRelQ2oUoAorl0biUfmbM2ZsJb2jGUhR0c7YiSkQmVGVBHv0o31pIlXe4cz1Bg_7RW_1g9VOOcg4eRe27YcwfAhTJBDvfb9ZXJhWfgmKfIVhNF_zHO1l4XW5va8-AdNKwo_Ahh-nFwvUermhgAWHTQSrqJM26MD6iU0sJwIbO758bH61C4ACKnccCD7flu0hM3xGIQXU6Z0mF8TZhb-68ZCOqRT1mNtGMrio1lMVCVn1zNWUXQoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=kb4OXdzjgcOVmWsHYJlLv1z6J8IAOJ0sHtwqg0lBZgMmquvf1Pm0UH-usgGP-CHt_nVkFjbY8C9x9MydrK2h5-91MmhIoeFbjLMRelQ2oUoAorl0biUfmbM2ZsJb2jGUhR0c7YiSkQmVGVBHv0o31pIlXe4cz1Bg_7RW_1g9VOOcg4eRe27YcwfAhTJBDvfb9ZXJhWfgmKfIVhNF_zHO1l4XW5va8-AdNKwo_Ahh-nFwvUermhgAWHTQSrqJM26MD6iU0sJwIbO758bH61C4ACKnccCD7flu0hM3xGIQXU6Z0mF8TZhb-68ZCOqRT1mNtGMrio1lMVCVn1zNWUXQoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNwvQ46mYfyHIiGPWj4DHDE-v_fO1HZqzNghMXCHt-UUc2uTBS6nHD9z2JRZqSnqB-dy3ihJFuRDWS5Ef6JeGdseHI_akDBrDhU4BLTpc_OmQbCgdfr0mWVuYrj8da45-9FzgNTw_P-kYlvBH7v4RN-mMJRzZii0yK-CisOEDN2vouA0jjxqOBTbBdNvPB9v6QWpZIrXWBbCYUW2sk3aVOMkCD8_lIHba9VafE_QqOT79B8DU4MPT6pakAjfYHOUcJc0OXpegIoaw9ZVfpsJRfVslSqW4gtk7FSlfCeKTy30yZ8aJNVm5JDVBFPqgb4wAiLs7459ltWGD4aYipIxvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود آپوس 5.5 منتشر شد — شرکت Anthropic، مدل پیشرفته خود را عرضه کرد تا با OpenAI رقابت کند.
بر اساس تست‌های انجام شده، این مدل از Fable 5.1 و GPT-6 بهتر عمل می‌کند. همچنین، 20 درصد ارزان‌تر از نسخه قبلی است.
این مدل رو
اینجا
تست کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7826" target="_blank">📅 20:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7824">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihyld7dCUpbfjYK5jOhoD0oP5xpjOM2c0a57xdCrtrFuth3CgHvFLxLKzIiQ3MC8OIpqaogQkLxF32xhliGANXG7HNj_wQ51uErC8C2Pvu9Z1EYSUbXlWsSBbrIDbPhQSy6KlvlUNdk1gG8FzneEuaT8tZ6VH1kJdQXuRp3J889Ch0XA59Rwki-w3DzbmisZxosM0ZDaZRnUmE3af7ZTEjRGpu0czPLfeyndk_RfShzb1fl2mPujEOayoNFRtZl-eGR_cMNyulOjulLtiMXoo0KviF7hvLjYM4i4czUQ435se9ZLDGGi6WS3AGY62gOwQBbN6ZNkTmDU4wl2aHkohg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5uvkhDycgtwPnAbYTuRNnXGg7BP3OImedbUJcFilWAImuK-KrHtJRsebEYPEgil2WBn2SppxyE8znVkHqAdxc91Wfg4I2LZGOTI7q9By_IiIvD2PK7XdlYL-onuqE3d_Xl6cI837VLtQTwQ8Kbjr-gnLKZJ3wExQCM4R1kagjjs52iO7Xy2cBs87ESyVEo0XAuc5wFWhIExnCdntecyxBGT2f6JDWEER5wkmkQYYip6RrTCzdtRGdAAb4UhZ8qgoHfofZPB_v94BgLlEov7ZFg4T_XHcCSvPXgNzYqrqKw7cv_X-b7d0YAiUlPjbHw7IkPP45ozpegqZ0DeadPBQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7823" target="_blank">📅 14:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7822">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2hNkyArtB5Su-eBKBkb9j3kCk_aHTK5wdWrSlFWrnEe96cnpVBmIZ4mh60wmnC7VnsQQsUvPvN-025KFueU0eFP9I1Wbz4WwdOKMLY35kXMUsf-ZJX02MPEqj1aoWIuGDi1ubQEvKCaYlYTETJecQkjY_FxjVaz9ZbkYk_c0M3QW8-VYPRfd61OPjE05gJukQEz0_3YcY28A13-TuKF89kM0Ufuoj2fAYOG42w1OlUJpRwtLTTLCvYc6SUu0jBFLTOFsEmiYU0lHYNB4kc89M0n6Ezpz27P_L5Jg3fjjpYjKUH36u9H06MgwOTpMlVbPHZ_fR5W6FEDJ3ycvSVImw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
وضعیت فعلی بازار هوش مصنوعی
💀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7822" target="_blank">📅 12:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7821">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7821" target="_blank">📅 11:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7818">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0ZFz5vmmaxbXoSiJzs9tGU70m4G9O2El0nz9wAnhrbZYeXgvsFcV9HOg4iGaGVrPKPZ-MKS79tKMJdd2VDTOtnycyW3bkrUxGcUqMnP6KdLIhsQHyhP2_QhfUT3XuKeiq7d9yhZ7FsxgTkXiNNFOa1eoQUYuBPM-O-vaV48ZY0RFRRU6Ldh3lPB3v3cQSITxRj_okLriSMvjxrFFq4ePPV7RiSEUE8rhlt6n8f-FeFhb28qwniopYmMUp6E9TxuScdvjh9EPpUxH-7t1j5D13daEUJEXyWCyaN-t-qJ_HMRqrMOKP1HkTaGlxbD0bXaV20hKPzLY8JtROZQcsi0Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EFRLsV6cs39V4rp8QGhBYeO2tMLXp9P5P89yXDu4XfTmg1YqGycfAjQFQ1-e5DWctaYaCaUwEEqc-ZC5HibGrKQLzy00yoQ2EKzpEvd8RsEEdQqdEG4RITYx0GO5cP7xaoi-pyYvYiEHWO1RPfjOqxtUaGgbAoC2TJ7xkSKvad7tIj8MiIKgDloYZk2TAObA9WlZLslsqBcp8gg0E9QJjrgVfOwto-IZGOHqMW7S_3ISf9WDLgm4m3xCVVC0FrVkU505uE9-zI3AmoCU7AaBLfUzMeXfHZxVwVCGyzqiIKvzdAhchDNRxcRCIhlABKmRrSQa8sdHm1IGuJVwZp2zoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBj_9tN8D1Z0GXReYhSBjqZ9RhJBxj9Av3VJdE3--zrY-4kuVZcB0QCWbwrBOseLsUuCC5IKVHhxpkieyftoE6q2dns_FIHC1H3iY8wPBH96q4OYhwPqlcf6cORVscbFPsx3cNCszAGFTvt6IiwXQSTdlOsdc3blJWDow8L_O_iGfmGJUZebopnBMHAzMVaLsQHFs10evxbFDpCRaqVcRgxW4mrqPeoUOsiJ6FmK-dYyW8_yjHgYnQ6WqFDcTvEfHaWXbnb3_HDvZgpkbiYZYOwViwkXaNcAq0JYRIqGJGwH-UCU8QQfPoyeNi1H5NuRkH2akQLpT6dsYK-r0bMVCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4cW_BqsrPYW4oOPyWwFWKbGNK8KUvriS7j0D96XEm8xepHh4Kin46duaHEPUyEyF-GmySx3k5hLmXc8M3JsAfZAKLTCLXzBpLRfFtoSjSDJ5sg3yiLeNaSAmLwbZCEtDTyr80z2idG-YYLioyjtRAX1-JloIeAmueuvCUaE9pAjCFw1y3ndCHUdZlonitew2p2lj7jcOkFF8-lXQ0ZgFyApXCmLFzid1D3kNTu8jjeX1VGq_8_cJOU4XxAY1OOhdQjqYbTOlDB3uD0GLmttiWs4to3ojCcCa5P9UHZmWC9Q0KyaKGwWCUFwN-xtTWp2ihmBS08cvaIfG6x1nw_5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی
یه پرامپت از ساخت بازی مار بازی توی حالت ultra speed mimo 2.6
توی کمتر از یک دقیقه واقعا پشمام
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7817" target="_blank">📅 01:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7816">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCMsjCZBh0VkgeLOaTqJ0LTgkUAjoxu-UkFAfrjyCgEZLUwwkLKGNfiRJFfuAL6-2FlOfa-4TrWV9rCYBZ2B-XEm92p6BpsRdjvuhoF99sLD_N9v0tjGcc2slS8p0RRCdgSO7s24Rpggy1AkYVbLzdKmOH_4X2p2nRfvKpynkl1pW7wsTUpUOoSdgqqFRi8MfapMVvww5lsfYB5lgnU2c8xMXNpOdbGmoxqhYHlI8wtyxdJqCuepcJPJiUM2FFlmWtszCUsFnM2uVMfhr9PJjevGIOl4f1Bp95wC7j_g0duzCUBUBiQI_4w1rqDl1goFta8k4Y4PnmXVKZDb4ywcFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد   درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در…</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7816" target="_blank">📅 01:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7815">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد
درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در API منتشر کرد. سه نقطه پایانی (endpoint) جدید در کنسول توسعه‌دهندگان ظاهر شدند:
؛ mimo-v2.6-flash، mimo-v2.6-pro و مدل پرچمدار با سرعت بالا mimo-v2.6-pro-ultraspeed.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7815" target="_blank">📅 01:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7814">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=WC-sflmJ_hvqiEdYhXN_qZE-JTQrMZrvkpnXoHvDFtDaiw49CmS8Hhglc6JYkkIDvy5EubV52Ns1UA5HdooDZAti1IJD_H7R6YJioe1sRPXtRWSu30I86ZUqAIczr_PGkdvNcINTaqfH2FDPZtJGwBAebH03ALpS842Hzb_JQJzS8qosMlm2kLStPWP2yMd2FlrKcHRdDpY0eIEnTXUdaGIB8p2MAuBVIKiphhGdiXBRopElIdBSksAMQLAB8BnHUf5A-F-bbX2MJzkbfE3vuS4r7OB0zJS8FIThOSmAeOAP3FxNFF-_MfTtmS1LjuObK0PJGJrtTawE54GmOSNYgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=WC-sflmJ_hvqiEdYhXN_qZE-JTQrMZrvkpnXoHvDFtDaiw49CmS8Hhglc6JYkkIDvy5EubV52Ns1UA5HdooDZAti1IJD_H7R6YJioe1sRPXtRWSu30I86ZUqAIczr_PGkdvNcINTaqfH2FDPZtJGwBAebH03ALpS842Hzb_JQJzS8qosMlm2kLStPWP2yMd2FlrKcHRdDpY0eIEnTXUdaGIB8p2MAuBVIKiphhGdiXBRopElIdBSksAMQLAB8BnHUf5A-F-bbX2MJzkbfE3vuS4r7OB0zJS8FIThOSmAeOAP3FxNFF-_MfTtmS1LjuObK0PJGJrtTawE54GmOSNYgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل در حال ترین کردن
Gemini 4 pro
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7814" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7813">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">😎
از 265,000 اعتبار رایگان برای استفاده از مدل‌های برتر مانند GPT 6 ASTRA، CLAUDE FABLE 5.1، GLM 5.3، و غیره بهره‌مند شوید.  یک حساب کاربری جدید ایجاد کنید و فوراً 250,000 اعتبار دریافت کنید. با ورود روزانه 15,000 اعتبار دیگر کسب کنید و با انجام وظایف، اعتبار…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7813" target="_blank">📅 22:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7811">
<div class="tg-post-header">📌 پیام #3</div>
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

<div class="tg-post" id="msg-7810">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAAz-gwPWEoBjDEFaBgmCU7ZBan_UzcNmeInck8BVDvbK1CFCbM-33NgDv83onwmNRjIOKNFx5Q1fqhhKD_eLxVbmOiTe_I2yH5RFM7NwQka-JL7SO1533ZE53tS0Yf4FFe44U7sndpKGbOA7afdIYtxIhlQE5KKppH-gRy25z5w2UNhTbi4h_z7QWk4lh_6PtvA3jgHkHtx6AXZUefKW7KuIYDFOICCUgjpnqA2ejFZaTMRPIMrp-sMMFKprQQDCOEtINCYlaRaNcF2LjkQ-gdlEiwssP9y-CrQMADNgx1VgUNzx-wXRfF6hOayDOR3dypRWBG3D-T-7Y0GnLYj_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥹
نسخه 4.7 از Grok منتشر شد — قدرتمندترین نسخه Grok
🤔
پیشرفت چشمگیری نسبت به نسخه 4.6 در تمام جنبه‌ها
🤔
عملکرد عالی در حفظ متن‌های طولانی، کار با کد و اسناد
🤔
مهم‌ترین نکته: قیمت بسیار مناسب — قیمت همان نسخه 4.6 است.
🤔
با توجه به پیشرفت‌های چشمگیر، نسخه 4.8 از Grok به زودی منتشر خواهد شد.
🤔
برای
تست
اینجا کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7810" target="_blank">📅 20:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7809">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-dwuDq3XTy-IXulRa8XrSvkfasWVZpbVVCyrVENBA78P8tdgyUI60S9Z80icS26HUi8XvsMR6Ze-kKIZkpPWn_ZGGxP4L6XpX-GCoYVa-LitWl4Dl4_boh_M1uTRDnnMOhem4bu5cp7KzMWVizeryG-jeBSKdB2Fa2QNCRJTEqdmGvCyDr_JGURdax02yIfHISAnT-hcBxFvaQuHDbCiNombBkLGa82Mu3-Xgk6WRL4S-qtC9jxLDN37IP9gjIPEyo0Lo2V12I3CAof-BJ3SLMNIx_8GJOWRlGd9uMhoPlkiSHGpZHl9v8gf2E0xko9cQyCwATdrP6EighjpBbFaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
500 میلیون توکن GLM 5.3 Flash
؛AutoClaw دوباره توکن توزیع می‌کند، این بار به طور همزمان 500 میلیون توکن در دو روز
21 سپتامبر: 200 میلیون
22 سپتامبر: 300 میلیون دیگر
درون آن، GLM 5.3 Flash، Deepseek V4.1-Flash و V4-Pro وجود دارد.
🤔
دانلود
AutoClaw
و ورود به سیستم را انجام دهید.
🤔
بخش Credits را باز کنید و روی Redeem کلیک کنید.
🤔
روی Claim کلیک کنید.
⌨️
انجام شد! حالا ما نیم میلیارد توکن داریم! مهم این است که آن‌ها را در طول روز خرج کنید، زیرا در پایان کمپین (23 سپتامبر) از بین می‌روند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7809" target="_blank">📅 19:32 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
