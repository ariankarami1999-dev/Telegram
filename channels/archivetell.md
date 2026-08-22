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
<img src="https://cdn4.telesco.pe/file/D7ndzD-nCApJYkwjPkMUiX29zZQ4-LqeTM7yjRPaT4lfnfRFJZI2X5OghhzrrQxb6_sx4z4d8CB-4eDaJtqS0mRUSwaAvPKc6iXka4hmkQf9bH1IygE34FoGW4cbXIh5vR-CZc4UMkVB5MYSvwmg5sljzdM7d3-KWPAOFUghcWL6lYjkh7LyfnwHZoYF11Krwa6_C3d140sCcHt0CJzCoZ9Hs4UtnQBz9jCEtdmFlvmSR4m3RWcfqs9tm6lMvXrc7PQGsuHox-jBSeSG74MedID-X0yPKjCnmp28OJKumHICzDaBYDUt9Og0oAjG43GBBXm7sNA3SOJG_Ub9mG30bw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 18:14:28</div>
<hr>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tv8favytHCLWVvTfchMdXv56ixPvmUbo35sLJo9hT3SmmqxmkyQVOMma85mRjeGbvtf9m7PD49L1rxpWu8p2BnMFRr0FOulLYzR3PaM0L1mLCWqmMNGJNqHBb9J6s7Y4hsmgOVPN_PegUDX0boKZfxIVdclpdTEciMSFMcGdk8OR340BSXtaSAmxXFleCfgnS3sNqDEFhIvm3c2U0U2XxYo2bnBl9vUqRHFkt03co-NciEDZ0638lyFMaw4uo-TJrwuls3n6ZpzzP8BuA1lwHYxy_c3J6TSVp5fH7cTCNptHeJLN5fbz2q30HLW5rZFx0coI-Zhcj57f2Ukf9DC9Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐳
۹۷ ابزار جادویی برای DeepSeek Harness — یک دستور، قدرت نامحدود!
یک لیست باز از افزونه‌ها برای DeepSeek Harness (dsh) — با یک دستور می‌تونی قابلیت جدید به ایجنت اضافه کنی.
🔌
✨
دسته‌بندی پلاگین‌ها:
💻
بهبود رابط کاربری — TUI، پنل‌های کناری، پالت دستورات
💬
نشست‌ها و پیام‌ها — شاخه‌بندی تاریخچه، اشتراک‌گذاری گفتگو، حافظه
🛠
ابزارها — اتصال به دیتابیس، CSV، JSON، regex، آمار
⚙
اتوماسیون — هماهنگی چند-ایجنت، زمان‌بند وظایف
🔔
اعلان‌ها — اتصال به تلگرام، هشدار دسکتاپ
🧩
توسعه/رانتایم — ممیزی امنیتی، sandbox، ابزارهای گیت
🎮
فقط برای سرگرمی — بازی‌های کوچک، استیکر، پت مجازی
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 242 · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-rAdhOBBO9gS4rV8ImSmER1p7GzJgBPXx_b_1TwMTacrgkuV2QMSAZtLYpEbtrvm0_PmqPfiUiEgGPWhpEJyYHdgRsh5hT-tM2jp1hs7qwZd0KxnPJBHLALKBXVHTLWBi6Ac9X_DjJgo4grHvQ79y_-NIO_hmE-ApC_RJW0m9nj357gNo67Icm8l0JNnWZaEN4Km3M1svMcHoxDBiweedOXZeuW5USjmZe_npToP-NMQR8o0ShLxRQLMlUkoz-1JcFd7jfRNWkfsly56JXKfZvjGtD9bVGnx_41rgro1ngPUNIyq_dVxdLXhGCT6fDzTt3mXcfKuNAJokImdyLliA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
پروکسی وب جدید تلگرام — پنهان‌شدن پشت سایت‌های معمولی
تلگرام یک روش جدید برای دور زدن فیلترینگ آماده کرده که ترافیک پروکسی رو کاملاً شبیه ترافیک عادی وب می‌کنه.
🥸
⚙️
نحوه‌ی کار:
🖥
تلگرام دسکتاپ یک مرورگر کوچک داخلی باز می‌کنه و یک اتصال معمولی HTTPS/WebSocket با دامنه‌ای برقرار می‌کنه که ظاهرش شبیه یه سایت عادیه
📦
کل ترافیک MTProxy در یک جریان واحد بسته‌بندی و از طریق این کانال مبدل ارسال می‌شه
↔
روی سرور، یک نود واسط (relay) این جریان رو به اتصالات جدا تفکیک می‌کنه و بدون رمزگشایی، به MTProxy معمولی می‌فرسته
🌐
دامنه هم‌زمان یک سایت عادی نشون می‌ده، و صفحه‌ی «پل» فقط برای تلگرام و بعد از تأیید باز می‌شه
🎯
نتیجه:
کل ترافیک از دید ارائه‌دهنده‌ی اینترنت مثل بازدید از یه سایت معمولی به نظر می‌رسه — یعنی پنهان‌کاری تقریباً کامل در برابر فیلترینگ.
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 716 · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8Kd_694NocST5NIG0s700KpGmUkY3rclmHcjadEcttrdsnKYqQRjC3ErpYEV-eLeBLct9aJJQSX4z-cBXaneu5JosuqQgTsGgZ2yVE9lnRoEFMXm1k2FNW7HR8bZG_gv-SeAlv5KmEEzF16lbvSQVjbwwbXPEuGh2Tm8lE3HNW6k3VKs22AKG-4WZYhuC2hjBTLVdP6rLS0c7xh_7u36d0v7TDldIpiNjfxudMj4cqQdic47dQmwWaBESWYmVzZKwpii-GRlqaHxmdffy9J1TvxhgH71C5NBXpWat_d0DaAqNazujViySezZgxXTMIwytZcwO-xIZqBD8cCOXz2JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
زمین بازی هوش مصنوعی برای ساخت چهره و آثار هنری
سایت Artbreeder یک ابزار رایگان آنلاین برای ساخت تصاویر با هوش مصنوعیه که تو ساخت چهره، کاراکتر، منظره و هنر انتزاعی خیلی خوب عمل می‌کنه.
🖼
با کشیدن اسلایدرها می‌تونی ویژگی‌های چند تصویر مختلف رو با هم ترکیب کنی و یه تصویر کاملاً جدید بسازی.
⚡️
✨
ویژگی‌ها:
🧬
ترکیب و «تولیدمثل» تصاویر با تنظیم سن، جنسیت، حالت چهره و...
🖌
ابزارهای متنوع مثل Composer، Splicer و Collager
🤝
کامیونیتی فعال برای ریمیکس و اشتراک‌گذاری آثار
⚠️
نکته‌ی مهم:
تو پلن رایگان، تصاویری که می‌سازی
به‌صورت پیش‌فرض عمومی
هستن و همه می‌تونن ببیننشون.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/ArchiveTell/7537" target="_blank">📅 15:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7536">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGobVP0Olafp8mTAz0hsJKOh5cePBpwEX1mTw9NX9-uhr5MV6pc670FgZqL9SNWFvTnazZRemn6SH7V6ILQ3rDpl03L_tzwrtB0NpdU-c9kFXgeMWfIskdKuxGYimn8Lqk_P3LOLOKAMQ8NKcvAcg0knN_BjP7AK9MkM1M6uuNk6hB5EZ-ymJVdSCSmdWNG4IhdgTFyaQKVg-WVd2p-N7Jt73F5ofqyk_ODcHqwr_X4wU6Hgvm08WXj28dCUtfRaQR1CfAlt0QrVc4fR_KGmphxehcRq29TdsoUkF38RpgDz07SOCFFhvFNGsiKKeZp7A6dD6bqA3dB-VA65oLrv1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
دروازه‌ی رایگان به میلیون‌ها مقاله علمی
سایت CORE یکی از بزرگ‌ترین موتورهای جست‌وجوی مقالات با دسترسی آزاد (Open Access) در دنیاست.
🌎
بیش از ۴۰۰ میلیون رکورد علمی رو ایندکس کرده و برای بیش از ۴۰ میلیون تاشون، دسترسی به متن کامل رایگانه — بدون نیاز به اشتراک یا پرداخت پول.
🆓
✨
ویژگی‌ها:
🔍
جست‌وجوی پیشرفته
📥
دانلود مستقیم PDF بدون پی‌وال
🎓
پوشش تقریباً همه‌ی رشته‌ها
اگه دانشجویی و داری پایان‌نامه، مقاله یا مرور ادبیات می‌نویسی، CORE می‌تونه یکی از منابع خیلی خوب برای پیدا کردن رفرنس‌های معتبر و رایگان باشه.
📝
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MftEhM3Xjqh4feRz9KjgIM0xE711FajL9J_XU0zoEy5rIYu2tB8KLgoDzLonRHgT8CKYez_iuVZA99_y7ZerzCP0M5KqFmVM3cWsxvcVnGP9X2Nr2u6dEdMZs3kbo7J5GZtUJ06H0h7dlHM9VH7WiSKFUs_W3Fit6nYilQGjHYXfYuZiH2up_ChF3Pa57DgFPrW36eET_pvvkYYmrY5J0IK0HdrtTpBz5gc4APz2-2Ea1CFtEY4-LgXYcSpQR2Bb1LgeYtHlz1mycv-JsFs6scU80TVsWPuh_irhqtNWJE1chymwjFTldm8bHczqjH9Ssl-EkYrzq98B7tyaOEAkGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتبار رایگان API تا ۳۰۰ دلار بدون نیاز به کارت بانکی
🆓
🧠
فقط با اکانت
گیت‌هاب
ثبت‌نام کن و بسته به سن
اکانتت
اعتبار رایگان بگیر
✅
با این اعتبار می‌تونی از
مدل‌های قوی
مثل
GPT
،
Qwen
،
DeepSeek
و بقیه استفاده کنی بدون اینکه هزینه‌ای
پرداخت
کنی
🟩
Link
🔗
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7534">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-text">🚀
آپدیت جدید ربات وگا
🧠
حافظه هوشمند وگا
از این پس وگا اطلاعات مهم شما را به خاطر می‌سپارد تا گفتگوهای پیوی طبیعی‌تر و شخصی‌تری داشته باشید.
💬
حافظه در پیوی:
اسم، سن، دستورات و قوانین دلخواه شما ذخیره و در گفتگوهای بعدی استفاده می‌شود ( قابل حذف کردن هست )
👥
حافظه ماندگار در گروه:
دو نوع حافظه مجزا
• حافظه عمومی: قوانینی که برای همه اعضای گروه اعمال می‌شود
• حافظه فردی: اطلاعات هر کاربر به‌صورت جداگانه در همان گروه ذخیره می‌شود
از بخش «سرویس‌های هوشمند» گروه فعال می‌شود و قابلیت ریست نیز دارد
♻️
📊
حافظه کلی ربات نیز گسترش یافت. وگا اکنون پیام‌های بیشتری را در گروه‌ها و پیوی‌ها به خاطر می‌سپارد.
🧰
جعبه ابزار جدید در پیوی
پنج ابزار کاربردی اضافه شد:
💵
بررسی قیمت ارزها
📰
آخرین اخبار
🌐
تعامل با وب
🌎
مشخصات IP
💱
تبدیل ارز
🌐
تعامل با وب:
لینک هر سایتی را ارسال کنید تا وگا از آن اسکرین‌شات بگیرد، لینک‌های صفحه را استخراج کند، یا به HTML/JSON تبدیل کند
🌎
مشخصات IP:
آدرس IP یا دامنه را ارسال کنید تا لوکیشن، دیتاسنتر و سایر مشخصات آن نمایش داده شود
💱
تبدیل ارز:
به‌سرعت بفهمید هر مقدار از یک ارز معادل چقدر از ارز دیگر است
🛠️
بهبودهای فنی
✅
تمام باگ‌ها و مشکلات گزارش‌شده برطرف شد
⚡️
ریت لیمیت گفتگو از ۳۰ به ۴۰ افزایش یافت
🤖
مدل هوش مصنوعی جدید DeepSeek V4 Flash (0731) اضافه شد
✉️
هر مشکلی مشاهده کردید، به پشتیبانی ربات گزارش دهید
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
🧠
Vega AI
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIiy9E17uwLIpQNz71NG1--49VqjRONogGZYFthjM0EfvYPKrF87BqWge7EMi00TeG591bYIVpihgohyKkUiR-wJcRJelRqKMGR9QkPQk26plm2Azhpve0ooxwUOD7feAvTC5zRQXfx2MDZpw6rpJ50jDBaiz8D1WGKqpGQyFvx5aLUyNpf7Yw-oBDjvzJXYUscfzrIFDHCvEaiWJ1kcSvP2wUmgCmukzj8bBcFJh2c24lBrPsKUtMMqV24am0JcXc4kqippQT09ja-NNW7hFBqVoP9B4bTFLJN0l9OVmEvke_SqU7hSc-lqI7V-1MHEnG6dFI5Z9H9s9SEpwRtFvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی کاملا رایگان به مدل های هوش منصوعی زیر
💥
🆓
Opus 4.8 | ox alpha | Kimi k3 | GLM 5.2 | Deepseek V4 Flash 0731 | muse spark 1.2 | Mimo 2.5 | GPT 5.4 | Grok 4.1 | Haiku 4.5
✅
📌
Base URL :
https://api.yjs.im/v1/
موقع ساخت کلید حتما گروه Free یا Free lite رو انتخاب کنید ، قبلش به بخش Playground برید تا بفهمید هر گروه چه مدل هایی رو پشتیبانی میکنه
✅
برای استفاده از مدل های رایگان داشتن کریدیت نیازی نیست
❗️
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=DVSKMLL871QtS_xqbuKbvUDN-9dliMyI79dQMJgwaw8EqCTQOjmoXRyMA5vPerIXsFEeKLGf2DXu1KQl2umVr9UkVwutRPLAndgiS3SBsWreCIHsJ1OAO4QN7Omz9R9Z4ZsHWsegV_dtebqBVZIlU4HqnF4P827mNF0W1IcJRFRUYPocg44b59Vc9TPausAgvnWFqvtlES_DthIXhwxdZd-zOt0MgIpPMbPVMwX1AiNXBOUcbXtbE90FJ93kB482yiS4p-AVlRJo9lTMHiCbYijkFZOTFt51RmNLhFEe81wXXW7pKbmjzbfthLq-TSBTbuMENjJSS7ypjw3lgXf7Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=DVSKMLL871QtS_xqbuKbvUDN-9dliMyI79dQMJgwaw8EqCTQOjmoXRyMA5vPerIXsFEeKLGf2DXu1KQl2umVr9UkVwutRPLAndgiS3SBsWreCIHsJ1OAO4QN7Omz9R9Z4ZsHWsegV_dtebqBVZIlU4HqnF4P827mNF0W1IcJRFRUYPocg44b59Vc9TPausAgvnWFqvtlES_DthIXhwxdZd-zOt0MgIpPMbPVMwX1AiNXBOUcbXtbE90FJ93kB482yiS4p-AVlRJo9lTMHiCbYijkFZOTFt51RmNLhFEe81wXXW7pKbmjzbfthLq-TSBTbuMENjJSS7ypjw3lgXf7Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
بزرگ‌ترین نقشه جهان منتشر شد
دانشمندان بزرگ‌ترین و دقیق‌ترین نقشه‌ای که تا امروز از جهان ساخته شده رو منتشر کردن؛ حاصل ۱۳ سال رصد بی‌وقفه با ده‌ها تلسکوپ برتر دنیا.
📊
اعداد و ارقام قابل توجه:
🪐
۴ میلیارد جرم آسمانی
☀️
نزدیک به ۶ تریلیون پیکسل
📷
برگرفته از ۲۶۳ هزار عکس
این فقط یه تصویر ساده نیست؛ دقیق‌ترین و جزئی‌ترین تصویری‌ه که تا حالا از کیهان ثبت شده و بعید هست به این زودی‌ها دقیق‌تر از این ساخته بشه.
🔭
می‌تونید خودتون توی این نقشه کاوش کنید و گم بشید توی ابعاد کهکشان‌ها:
🔗
لینک سایت برای مشاهده
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPeN3L7UHtcZNn8xF4GlUe6KJuzAWpaqGcSVbYMUPLPvKfAPOo4aG0zdbSWx58kHtVMYHgseSDE2KJl6LhZO4XsAoJtDMcNyi9goWNUwGhXbOrm3VsYH_RSDhzj4x9FFzRLJ0dAzU_oDKw-1lvO-Ohyx5vrEoK57nXpSqu61i7kSazENFO-hbGURRjcw3rLrcJLxj72QzOjug_JFaoubp5lrzkE5qELql635B3vxClao9iJzhYPupNg6Jc-qcKk8VhxDpQMlgTgE0OGV9FDXkirAj2YZQmblDUwu9r3YP328VmydOPaoMvYDYahdz4QEJWPmNeJmT7WpvVcJ0YKcNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل استلثِ ناشناس Ox Alpha رایگان شد
🥷
مدلی ناشناس با نام
Ox Alpha
، بدون هیچ اعلام رسمی از سمت سازنده‌اش، روی OpenRouter به صورت یک هفته رایگان و OpenCode منتشر شد
⚡
✍️
مشخصات فنی:
🔺
پنجره کانتکست: ۱ میلیون توکن
🔺
حداکثر خروجی: ۱۳۱ هزار توکن
🔺
ورودی مولتی‌مدال: متن، تصویر، ویدیو
🔺
قیمت: رایگان طی دوره پیش‌نمایش
🥸
سازنده مدل مشخص نیست. این یک انتشار «استلث» است — یک تأمین‌کننده ناشناس در حال آزمایش مدل است، و OpenRouter صرفاً درخواست‌ها را روتینگ می‌کند، نه توسعه‌دهنده یا مالک آن.
🇨🇳
❓
درباره منشأ مدل، برخی کاربران گزارش داده‌اند که در پاسخ به سؤالات حساس ژئوپلیتیکی (از جمله تایوان) رفتاری مشابه مدل‌های چینی نشان می‌دهد. این صرفاً یک گمانه‌زنی است و هویت سازنده رسماً تأیید نشده.
📈
طبق ادعای برخی کاربران، این مدل در تسک‌های کدنویسی agentic عملکرد قابل‌توجهی داشته، هرچند این ارزیابی‌ها فیدبک کاربری هستند، نه بنچمارک مستقل رسمی.
🔒
بر اساس توضیحات ارائه‌شده، داده‌های ارسالی طی دوره تست برای آموزش مدل استفاده نخواهد شد
🔗
لینک صفحه در OpenRouter
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7W8FzPRWm-8hGFtqSp9j10o9OafAuCJcrcCIk3nzf1IXIIc2Pxl9bNBXFyVArusiHEx05AB91XsDSSA7DKb62z1Ijx8UDMTz3LHUClIq8TLt5x44xkI71Ov200P-iU-uGSvgpZo5Gk5-Dz38_0XUdxKONxhCtwHag1nW8hQ8pDi_jJQrvICwpt7OSWnGkYajXpiBTRdZjJL_pav0sulDcPXPtgy6Nlibh3yO_r4rL3ExiDzcP6mi0sCVIYDiv0BGZuMx_TY-sGDsvKKY1FESQGuXCesv0mPjoU5LyChLTSG72JnN_1KSLimPPf1OQu-054xbW_MEid_GdOBYpe5Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">70 دلار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله باشه )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
40 دلار
و شخص دریافت کننده
70 دلار
دریافت می‌کند!
همچنین تا 25 دلار پاداش لاگین روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjjfFEDnpgwAKBNzXtMB9BIvBkeoPqywWAfzWjTFZ4rjJAVqOn0JogOLYYcAJfS-wzQGtqmSjjk-4kjMZIxo4k1mawIg6px2VufqGKqXgJZQCSA23VgBO2OJREjadHOfKtVsrrCw2F41jZ7Nh2ydVCaTa3cZkHdnkAzGRTIi_pVL6vU6zsWEMDR7oUUN1xJwCG_eKpmTlIgJhXMCPBazs7MxS9xljGZM_bztTgWp21LQxyiyCnZKsafiLLP6GHsEiwFgWaQvYWs5aLhHBXN5vRURunwtxp29wzsRwjZzoy9zHHPNUXbyEhVgVRD-5ZJIalTtBQIhOKCFTiCXZNCFPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu_qb4y0-2eq2xN2Cr5NtcyBsX1-QPIQCGIOZsiIMOVZhHegmnWSvhpxkSXXOGxXTfEB9d2UWmM39Kp4JM6_CNirMxzKXf6BfTCnyPeWpaWcDybmnE4l2vLVALt3CAeaxRZSwCYR5TumVtjMfZWfhZhdfvJpPPxVF8OuOvgJKy4-Vwr14fD1a391UjaJRjoa_5ogo4PjtEl9zw7iTtb72FO3cBNqmjVCumiEklsYi0C3J4413_4sf8XEyVlYhk1Qwbtz33GgCTU_CB-czxu-TDfAjvXmRm21mPx89mNyY5Lu1peCXlnDyLbb2cWbY3YJBUYO0jlL54gjMr_lieQo3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 میلیون توکن برای دسترسی به API هوش منصوعی زیر
💥
🆓
Deepseek V4 Flash 0731 | Kimi k2.6 | MiniMax M2.7
✅
📌
Base URL :
https://hskyauefqcgbvgvxkluj.supabase.co/functions/v1/gonka
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7525" target="_blank">📅 20:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7524">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔒
بهترین ایمیل‌های امن و خصوصی
اگه دنبال یه سرویس ایمیل هستی که حریم خصوصیت رو جدی بگیره، رمزنگاری کنه و داده کمتری ازت جمع کنه، این‌ها بهترین گزینه‌ها هستن
🛡
🇨🇭
Proton Mail
— معروف‌ترین ایمیل رمزنگاری‌شده، با پشتیبانی کامل E2E
🇩🇪
Tuta Mail
— تمرکز کامل روی حریم خصوصی، رمزنگاری در هسته سرویس
🇧🇪
Mailfence
— پشتیبانی از OpenPGP، مناسب کاربرای حرفه‌ای
🇺🇸
Riseup
— سرویس غیرانتفاعی با تمرکز بر حریم خصوصی
🇳🇱
StartMail
— قابلیت ایمیل مستعار (alias) برای حفظ گمنامی
🇩🇪
Posteo
— بدون تبلیغات، حداقل جمع‌آوری داده
🇸🇪
CounterMail
— امنیت بالا، پشتیبانی کامل از OpenPGP
🇨🇦
Hushmail
— مناسب استفاده شخصی و حرفه‌ای، رمزنگاری‌شده
🇩🇪
mailbox
— سرویس قدیمی و معتبر آلمانی با PGP
🇨🇭
Librem Mail
— از تیم Purism، تمرکز بر حفاظت داده
⚠️
نکته مهم:
داشتن رمزنگاری همیشه به این معنی نیست که ایمیلت کاملاً end-to-end رمز شده — یعنی گاهی خودِ سرویس‌دهنده هم می‌تونه محتوای ایمیلت رو بخونه، هیچ ایمیلی هم امنیت 100% تضمین نمی‌کنه؛ این چیز به عوامل زیادی بستگی داره: تو کدوم کشور سرور داره، چطور داده‌هات رو ذخیره می‌کنه، و حتی خودت چقدر رعایت می‌کنی
❗️
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlexmhdL431ieDjIQhKHzW3Q_1oVwh_nzUZcBt3fmUuFdN6wZxAGT3AvOGfmUeIhGKA6A-QPPvELOwFS8pt7bcZ1McgivXKAS-oaBs2HchVQE-3RMzhMAnOHZPz8cHmVdQ4FuiYOibkuQbNCdEflXsv-em7Frzs3CcliqMgF18YzP3rN-S0RDQttZEqOgmNIXOh0TOWuxdq1KH1rxgiDwPoRg6X8caCWFc2W0tTKV_bFS62qCsQyBe0LtP2ndSWPfUkT8-vMsEfWu6skOf6WGRhqR4BBV_cILd9KtdyVRwJnUtjioigMi89BeavbBRocm0WGBYecTl0e0uB4mnNcew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">60 دلار کریدیت رایگان برای استفاده از API بهترین مدل های جهان
💥
🆓
این سایت 50 دلار + 10 دلار هدیه رفرال و هر روز 5 دلار بهتون میده تا بتونید از بهترین مدل ها استفاده کنید
✅
Opus 5 | Fable 5 | GLM 5.3 | Kimi K3 | Qwen 3.8 max | Grok 4.5 | Deepseek V4 Flash
✅
✨
مراحل دریافت:
1️⃣
ابتدا در
این سرور دیسکورد
جوین بشید
2️⃣
حالا در
این سایت
با اکانت گیتهاب ثبت نام کنید
3️⃣
حالا سایت رو به اکانت دیسکورد خود متصل کنید
تمام حالا برید
از این بخش
کلید بگیرید و استفاده کنید ، همچنین به بخش پروفایل برید و 5 دلار امروز رو دریافت کنید
🎉
📌
Base URL :
https://tokengate-cqt9ivzs.manus.space/v1
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7522">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دو سایت عالی برای گرفتن دامنه رایگان یک‌ساله
🎁
با این دو سایت می‌تونید کاملاً رایگان دامنه بگیرید، فقط کافیه مراحل زیر رو دنبال کنید
👇
━━━━━━━━━━━━━━━━━━━━
سایت اول (ساده و سریع)
✅
🔺
دامنه‌های قابل دریافت:
de5.net
–
cc.cd
–
bot.cd
–
bbroot.com
–
ddns.ge
–
l.cd
–
ccwu.cc
📝
مراحل:
1.
وارد لینک ثبت‌نام بشید
2. یک اکانت بسازید
3. تا ۳ دامنه رایگان می‌تونید دریافت کنید
🎉
━━━━━━━━━━━━━━━━━━━━
سایت دوم (کمی زمان‌بر )
⚙️
🔺
دامنه‌های قابل دریافت:
indevs.in
–
sryze.cc
–
ryzedns.org
–
nx.kg
–
ryzn.pro
📝
مراحل به ترتیب:
1️⃣
وارد سایت بشید
و با اکانت گیت‌هاب (GitHub) لاگین کنید
⚠️
نکته مهم:
اکانت گیت‌هاب شما باید حداقل ۱ ماه از تاریخ ساختش گذشته باشه
2️⃣
بعد از ورود، یک کد QR نمایش داده میشه
اپ Google Authenticator رو باز کنید و این QR رو اسکن کنید
3️⃣
کدی که اپ بهتون میده رو داخل سایت وارد کنید
4️⃣
به این بخش برید
و روی گزینه Repo Star بزنید و برید به ریپازیتوری گیت‌هاب اونها
⭐️
بدید
5️⃣
در آخر روی گزینه Verify کلیک کنید
🎉
تبریک! حالا می‌تونید از هر ۵ دامنه، یکی رو انتخاب و دریافت کنید (در مجموع ۵ دامنه رایگان)
━━━━━━━━━━━━━━━━━━━━
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxGPwaSQ4kvq7Qaz3CXL4yll_zFkHu4cQ9uJ6qHkvBvr8JGfUKyNlGK-5hstAwIbe6jl7IX07G_1g9TRyczLdb380QpcloPqQgdGNRumHI4PZ2yUdSuIcVDdcmH4fUyXlcY8fNBsz6Qt9ntT12ZQu17d-ydSMiGDSiPpHZdQjlI7BtazwoQNElP0jyeSzCnf8V69lWqt8-P48Qjan2hKVvYuJXFaquT-nGwuZeA0VuEVyuX05FsntSw2LsDA9_IbUSPclxoTLVAMp_ZG8sUtc-OiuGkqThuMPTfRZX-pWXkteNu4iLcGzHcRmahJawHke6xfhQ10rzkbbhrMsv0B6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون توکن رایگان هر روز تو xkiro
🔥
مدل‌های
Qwen
،
DeepSeek
و
Grok
4.6
رو بدون نیاز به کارت بانکی امتحان کن
😤
برو
x
kiro.com
،
ثبت‌نام
کن، پلن
رایگان
رو انتخاب کن و کلید
API
بساز
🔻
هم می‌تونی مستقیم از
API
استفاده کنی، هم بعد از ثبت‌نام با اکانت
تلگرامت
احراز هویت
کنی و 5
دلار
اعتبار هدیه بگیری
🎁
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R97rHt2yuKC_O3WlPTEarhUXcWN4vqEYteIzRdvf1b1cdRvWAavZLhw8Ami7PnG4i7VaH1M95hSuA4aTbuiJKs-2E4mzSWMVaFEJno2N4qJf9jH-GDZXbu4is2y4zkvZyvLi4INwFvVw8pI9Ok_lQpWXIZjxQgHIpAMOWGSlkoFuss7IPt1W5Dl2GHBY31579rwfqt6oJpy8z3ZQV_nrAMr599CCwnZw94h2LowNe1v_mkAM7-um2f2ZJ5Wi4A0-qEF0gvWeBAGODLhFMgZZzjVAvmYjELDpomqH_sqBSzY2ejstjMxZ10qjOnrBZGkuAMiqpJ2pWc1B_4Wq4RlsDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به برترین مدل های هوش منصوعی
💥
🆓
Kimi K3 | Qwen 3.8 max |  Gemini 3.7 flash | Sonnet 5 | GPT 5.6 Terra | Deepseek V4 Pro 0813 | Deepseek V4 Flash 0713 | Gemini 3 pro image
✅
با این سایت میتونید به کلی مدل قدیمی و جدید دسترسی پیدا کنید این سایت هر روز به شما 100k کریدیت میده
✅
📌
Base URL:
https://api.anyapi.ai/v1
🔗
لینک ثبت نام
🔗
لینک گرفتن کلید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مدل قدرتمند
Qwen 3.8
با ۲۷ میلیارد پارامتر الان رایگان روی پلتفرم آزمایشی هتزنر در دسترسه
☑️
اگه اکانت
هتزنر
دارید، فقط
API
رو بردارید و به هر ابزاری که با
OpenAI
سازگاره وصل کنید دیگه لازم نیست پول بدید
🆓
مستندات کامل اینجاست
➡️
experiments.hetzner.com/docs/inference
اگه کسی بلده چطور راحت‌تر اکانت بسازه یا ترفندی داره، لطفاً اینجا بگه تا همه بتونن استفاده کنن
🤝
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7517" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7514">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGtcraZ0F5Sm9cKwdo06QZtg_n18OBWt3NhRrJVNvqn1S2dVrpPOyu5rrvBoZzYd53cTFAXiA1POwcwQRuhk4bnbfeoF7NsKClWTE5L1NcvCE5wsF2HFXTACjpmzX6_YJwFnlS_2hluy5NyEspX4-gz5hmF3y-hpyAvgdFt-9iyPeluNp5r8qIqnpOhzs4UMa5yIekhQlAthyLNSi81Xuxa0CAFrh2w6j40cqVi6PpI3LVjCaYXePK2PVyeFLv1jEHmrqhYZLukp8sDATSQPyaGK3ytk1S1Fhs7CQuoSixfgp0qdJS16uua-3I_VZzfOPrhonh5bX1IArVAaNtliyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLK1OzmNvtQjQXLs1JBIQivyytaVtCWBOki7qVQ3TtJJwxnEkp1YjsekmjPyCAhEIy4GV2tUJex39iJLhACkI0Yy1b8TsMEcFtZRB-9OpU8Cy0mb9ACgRiOELvlqjHgoPp9WamqHJlcLXDrSVNUSlDhsj8UPwxDqsuq-C4Sy6ZWHVh8-s0CxA3q1hgIiY8SZb8cSkZkiYSuNsxRbq3u0FGxJBlIxOykLG6pfAoGx2XVRDs89tf3qx0fWNaZRTBVJrQdkfoNNrXX-_RY1qRGvsWZCQ_5YTYxwcOUaGU9FTDt7HSHdG8NCebW8Bzg5HCaBelbK-jWk0KN__leJCMO9nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت دامنه رایگان مادام‌العمر
💥
🆓
با این سایت یک ساب دامنه روی دامنه‌ی
kdns.fr
رو به صورت دائمی و رایگان دریافت میکنید همچنين میتونید اون رو به کلودفلر اضافه کنید
✅
✨
مراحل دریافت:
1️⃣
وارد
این سایت
بشید و ثبت نام کنید
2️⃣
به بخش
My Domains
برید
3️⃣
روی Order a domain بزنید و دامنه خودتون رو بگیرید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=HHBpG5pp-edN0bK575wdy2jK8JrEh91iWi33YXilwWWWdM-tdvOz88M2QSvb9Kf5tEHsx_p77kPDFI0MH3XCT5apJUnRXpD30MHncMcXjqhCY-DvPnGQw6EQ18a4IpyIDcL01hrzDOsTO7fU67gs-svy4JC43FZwyiAHYhf_Dl_5ZJxQHsvsLdG3Nxo7vUFvr6sSJIma9qN-9eGQ9jjAIuBvAuOVKM7br2ZQJ_Wen46xq9cg2IFAXw0NzTQPczZOy0NGcfpiyxNTuosyjL9ss5lBqDvRib4mMrTrnSyqBo4fT11yzakMyQF20JSf__0bfrrGlJeObJ1HU3gvEfnVhDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=HHBpG5pp-edN0bK575wdy2jK8JrEh91iWi33YXilwWWWdM-tdvOz88M2QSvb9Kf5tEHsx_p77kPDFI0MH3XCT5apJUnRXpD30MHncMcXjqhCY-DvPnGQw6EQ18a4IpyIDcL01hrzDOsTO7fU67gs-svy4JC43FZwyiAHYhf_Dl_5ZJxQHsvsLdG3Nxo7vUFvr6sSJIma9qN-9eGQ9jjAIuBvAuOVKM7br2ZQJ_Wen46xq9cg2IFAXw0NzTQPczZOy0NGcfpiyxNTuosyjL9ss5lBqDvRib4mMrTrnSyqBo4fT11yzakMyQF20JSf__0bfrrGlJeObJ1HU3gvEfnVhDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
📱
وایب‌کدینگ حالا رو گوشیته!
ابزار HAPI اومده که به‌جای جایگزین کردن ایجنت‌های کدنویسی، همون‌هایی که روی سیستمت داری رو مستقیم از موبایل کنترل می‌کنی
🔥
سازگار با Claude Code، Codex، Cursor Agent، Grok Build، OpenCode و چندتای دیگه
✅
🎙
کنترل با دستور صوتی، بدون نیاز به تایپ
📂
دسترسی به ترمینال، چک فایل‌ها و اعمال تغییرات — همه از گوشی
💻
سشنی که روی کامپیوتر شروع کردی رو بدون قطعی و از صفر شروع کردن، رو موبایل ادامه بده
🔔
تایید هر درخواست هوش مصنوعی فقط با یه تپ، حتی وقتی پشت سیستم نیستی
🤖
حتی از تلگرام هم قابل کنترله
نکته‌ی جالب: HAPI کاملاً local-first و متن‌بازه (AGPL-3.0) — یعنی داده‌هات روی سیستم خودت می‌مونه و به سرور خارجی آپلود نمیشه.
✨
🔗
لینک سایت برای دسترسی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7512" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7511">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الان سه تا مدل قوی رو می‌تونید کاملاً رایگان تست کنید
🆓
برید سایت زیر ثبت نام کنید و به راحتی از مدل های زیر استفاده کنید
✅
✔️
مدل‌ها:
•
z-ai/glm-5.3-free
• dots-studio/dots3-note-prev
• deepseek/deepseek-v4-flash-free
🧾
Link
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7509">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تلگرام برای دریافت پسوند دامنه .gram درخواست داده است
🉐
اگر این درخواست از سوی ICANN تأیید شود، بیش از یک میلیارد کاربر تلگرام می‌توانند دامنه سطح دوم اختصاصی خود را داشته باشند
💎
مثلاً
@durov
می‌تواند durov.gram و
@monk
می‌تواند monk.gram را ثبت کند
☑️
علاوه بر این، کاربران فقط با نوشتن یک
پرامپت ساده،
وب‌سایت‌های تعاملی خود را مستقیماً روی زیرساخت تلگرام راه‌اندازی خواهند کرد
🤯
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7509" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7508">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgWcr6fqBDZ_ABoTVwgE66sHRkiTzTdZPLxv4D4bLPNmVBJ7oW5_f5YIo0e32ouCkX5kYVYxHOYlE1gMaZVwz0gL70rIiIxiPxQc69wGW1qhDUlMnXl3jGCpp15zj-M6FqDNOSVX4Sn9KcYZCZkfccm-mQv-3rh_e7YeLdDo9HXDKa7b533TQB66_bno1HpFwPAYNJIc34GCGL1i0KO8NuNOZMY9ytU7NyAKnhLkSYbYwY3v-GKvjN8NCXEOLMqdflMBtTz6VV3wEqeTouRBgQB7wL_g80fVamvFgelp2AQvkL5W6OWxGeUt6jQm8vIB0BVe8DL8tWrDNuSEe9nzxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلود کد ابزار قدرتمند طراحی گرفت
🎨
تیم Anthropic به عامل هوشمند خود قابلیت جدیدی برای طراحی رابط کاربری وب‌سایت‌ها و اپلیکیشن‌های موبایل داده است. کافی‌ست دستور /design را وارد کنید و تغییرات موردنظرتان را توضیح دهید.
🔥
سیستم به‌صورت خودکار کدبیس موجود را می‌خواند، خودش را با سبک طراحی فعلی تطبیق می‌دهد و پیش‌نویس‌های متعددی را در قالب طرح (artboard) تولید می‌کند که می‌توانید به‌صورت آرتیفکت به‌اشتراک بگذارید  (The Decoder) . کافی‌ست طرح موردعلاقه‌تان را انتخاب و ویرایش کنید، سپس آن را وارد فاز کدنویسی کنید.
✨
این ویژگی هم‌اکنون به‌صورت پیش‌نمایش اولیه در دسترس است  (The Decoder) ؛ برای امتحان کردنش کافی‌ست دستور claude update را اجرا کنید.
✅
🔗
لینک دیدن جزئیات
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7506">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تست کردن مدل‌های هوش مصنوعی
🚀
حتماً براتون این سوال پیش اومده که مدل هوش مصنوعی‌ای که از یک سایت دریافت می‌کنید، چقدر به مدل واقعی نزدیکه؟
🧐
آیا واقعاً همون مدلی رو که ادعا می‌شه دریافت می‌کنید، یا یک نسخه‌ی ضعیف‌تر و متفاوت؟
👀
✨
توی این پست، ۲ سایت معتبر رو بهتون معرفی می‌کنیم که باهاشون می‌تونید مدل رو تست کنید و خودتون نتیجه رو بسنجید
🔗
لینک سایت اول
🔗
لینک سایت دوم
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7506" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7505">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGPnflRpv5j4hwTvspar8wcuv5_38qtrJyVhdZ_BdxWW1qa6_UVkAVXcSbFe72fkVTARy1L76fapZzSQtohFyMfX_Mry7YFrHOi0GailwNUlQp8YwVI_t9qtlaF3L5Zj-OkrcevJ918whqUZRPZZZXWOUzoTDc7_1mvAsHK1dLzP3G_OjkLR7J5aIWFdRh6UdqbV9k4LbeUMPCSQM642nytXmCuHjdpyOjF7AX6JaacIp-I84YKAh3mGZ7h6r9G2QkHbl1Mnq4OYaaRTuXJAveQHQhequqQEfONGN9aljPX_-Vi0r3i7nr8YVp1BiNGDmAwivJQLRO99uE-1XauRRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL :
https://api.b.ai/v1
📌
Model ID :
deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mM04CJZdHkSrwD7muHzBPokkHg8W5_wyTKD9la4t0Z4XjGjXY3K1fmRVQd7ttNTQNvYh7aXkwHAPKq-rq7-7cmOc2yMGd__lVkv-eandIfMa1fA8y2lT2l10PfsLTI35Xef_FGS-o_AqkD-tuZT1NPOC3-N0YK8gkMR604tzvJw2IUi36BKWt7nZ0xoGnC4zJCoSVku81P1sLCCANb_n8kwvOEyeutg64ckKnI93cajmyZOV8y-jxfY4t4Hkc4m6VekFuNZSe7xBJa1ZOvzCxNnj0k-D-R9oRBO2g0IZ1VCV793ohFfVRP50Aq9ixsF2J_SUkhQaL_qK0DGz_nZpEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.2 الان روی OpenRouter رایگانه
💥
🆓
هوش مصنوعی GLM 5.2 یک مدل Reasoning قدرتمند برای برنامه‌نویسی، AI Agent ها و اتوماسیون پیچیده‌ست. نسخه رایگانش در اینجا با 128k Context عرضه شده و از طریق مرورگر یا API سازگار با OpenAI در دسترسه.
✅
❗️
از مدل z-ai/glm-5.2:free استفاده کنید — بدون پسوند :free نسخه پولی اجرا می‌شه.
⚠️
محدودیت اکانت رایگان حدود ۵۰ درخواست در روزه
🔗
لینک دسترسی
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7504" target="_blank">📅 13:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7503">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هدیه ویژه برای شما
🎁
3 هزار دلار کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
sk-IXNxrDiaLV2vNxU73TC0Y4zSW1uPrXj0a24SxG8LbD4TYkfp
🔺
Base URL:
https://tabitoken.com/v1
🔺
Model ID: claude-opus-5
ری اکشن فراموش نشه
❤️
توی کامنتای پست چندتا کلید دیگه هم گذاشتم واستون
✅
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7503" target="_blank">📅 11:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7502">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwENdM1AH1T5cYtpYAnuq5q84u_FZ02Mm4U8Pd9XWhjeEJqX3zeQlCMoDXNh5D0fnVy5v5m4uaEeq1ydnSGN58uOjf5CFj-i5uJc8JjPFkCR0Evfz-8UepqTstMAqgWrpLGob15yrjriyJN8yqvQ2dePIOTJnvtRU93JUX0qKD9hbZjzpYydq1eqg6UF61OxAKjQiU-Y_GbKqrUlFC-g2zRz6fU_0PeAhiiQvAkruQYhM4AWrpLURlDgtLfoYO8tSDNfnZ02M-hXRbFWze4v6FsBiegWrLFrEIsyGfsmAgWuRZFi47dEu5zX_FRn_QC71NvhLv0rxERBSR6lxnve4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4 Pro 0813 و Qwen 3.8 max به صورت رایگان
💥
🆓
این دو مدل در این سایت به مدت محدود به صورت کاملا رایگان و فقط از طریق API در دسترس هستن
✅
📌
Base URL :
https://api.tokenrouter.com/v1
📌
Model ID :
deepseek/deepseek-v4-pro-0813-free
|
qwen/qwen3.8-max-free
⭕️
محدودیت ایی در میزان استفاده وجود نداره اما به دلیل شلوغی بسیار زیاد سایت مدل ها کند هستن،  پس باید در تایم خلوت استفاده کرد
🔗
لینک دسترسی
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7502" target="_blank">📅 10:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7500">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=teXdjStNrzJDFiGINDVQrD66f8EMynjdred41ab48MfxaB_WSBnoJ5XCGJlSPt5qbAGSnkILsog7CvYmm04P3yUZ2Bm9uzpXaxFeEBhXTSP-lli-Mypa_UKq35T3GdY_QsI1OCYKfVzzwDq_3Wx0jTgFJYmGlfAzJN9bU0xA_mTYoPFZRlufmxl4TAm9tL-U80p9YBHOMwTkSoRs9Ve3b50DJYdV1YOkrXrmGJmtHBY-N7Q6kOBydnTZ8EOk1MVT9ESoNqNzk-ObDoXdQtPVlwIrr7Ev8qp1T2ejG5tLTKf-KROOb4wWtvg_c6py-2ZVYVIxbub1a2MH9hwNq6-4Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=teXdjStNrzJDFiGINDVQrD66f8EMynjdred41ab48MfxaB_WSBnoJ5XCGJlSPt5qbAGSnkILsog7CvYmm04P3yUZ2Bm9uzpXaxFeEBhXTSP-lli-Mypa_UKq35T3GdY_QsI1OCYKfVzzwDq_3Wx0jTgFJYmGlfAzJN9bU0xA_mTYoPFZRlufmxl4TAm9tL-U80p9YBHOMwTkSoRs9Ve3b50DJYdV1YOkrXrmGJmtHBY-N7Q6kOBydnTZ8EOk1MVT9ESoNqNzk-ObDoXdQtPVlwIrr7Ev8qp1T2ejG5tLTKf-KROOb4wWtvg_c6py-2ZVYVIxbub1a2MH9hwNq6-4Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎧
این اپ کنترل موزیک رو مستقیم به تسک‌بار ویندوز میاره
ما FluentFlyout رو پیدا کردیم — اپلیکیشن رایگان و متن‌بازی که پنل کنترل موزیک رو دقیقاً روی Taskbar ویندوز ۱۱ نصب می‌کنه. کاور آلبوم، Play/Pause، Seek، تعویض ترک، Repeat و Shuffle، همه یک کلیک اونورترن.
🎶
با Spotify کامل کار می‌کنه
💻
با Windows Media Player کامل کار می‌کنه
🖥
با مرورگرهای Chromium و Firefox هم کار می‌کنه (بدون Shuffle/Repeat)
🎬
با VLC هم کار می‌کنه (ممکنه Plugin لازم داشته باشه)
⌨️
با هر پلیری که از SMTC ویندوز پشتیبانی کنه سازگاره
سبک، حدود ۵۰ تا ۲۰۰ مگابایت RAM مصرف می‌کنه و عملاً مصرف CPU نداره.
✅
🔗
لینک سایت برای دسترسی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7500" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7499">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0f-DMqY_XV2wTYcf6wA44MbvSYdQMW3WVMaenVtNxumjlQOcGmIVBIn5azG2zDoiao89mfXLN-CmrTucs8Kc0oMTVULtPPFSLArXOUywry16tfrD8uDEgrash9cJgyyHLdFwxXAN4V55rsdeNsNM_w3MR69Rb2Njw0qm3R1cCGCuON-bzHcPGRbhACpWYiF7jqovXt74AxAtwBn7tTebi_TJXVzKWgr1_0OjIUdIOJRKJHRabFec-yUfFJb4kWb1l3rS3JMgwnoFX2muO0YYkSk7oHpoelVU5SThDZeQLm8mDszjzeZcu-4mdPWeJ5QTA6pLpckbZNWmWIEFcCZig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
این ابزار خط‌فرمان، یوتیوب رو مستقیم توی ترمینال میاره
ما ytsurf رو پیدا کردیم — یک CLI رایگان و متن‌باز که ویدیوهای یوتیوب رو تمیز و بدون حواس‌پرتی مستقیم توی Terminal پخش می‌کنه.
✅
👥
قابلیت تماشای مشترک با Syncplay
🎶
پخش و دانلود فقط صدا (Audio-only)
📥
دانلود ویدیو یا صوت با یک دستور
📌
انتخاب تعاملی Format و Quality هنگام پخش یا دانلود
📃
تاریخچه پخش با امکان تماشای سریع مجدد
📂
تنظیم مسیر دلخواه برای دانلودها
🔄
بررسی خودکار آپدیت برای نصب‌های Manual
📺
پشتیبانی از Subscription کانال و Feed شخصی‌سازی‌شده
⚙️
نیاز به چند Dependency داره: yt-dlp، mpv، fzf، jq، curl، ffmpeg، chafa. روی Arch (AUR)، Homebrew و NixOS هم قابل نصبه.
🔗
لینک پروژه گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7499" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7498">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=IQFxmmOtfyP45g7Thlnxk0OK5QAKWFYsYR8df6kfe5UwyQYEY_VFuTm7YXP_zXEnBdSMCovzeoF5jMb2LLLy0POtFGaV5iMVEd9rzPL3nHc8MbDT60TYQmXBA1wj1Rry4CEOYPZOltyb2r6bZAtN3_33BMVMJQ2SZzb5As0g4mmdZyaYSJhm4bKs_O-CEMQf6V3Fjsi_aD-gVFSClMRcBPUiEGAUL-Yrb7x2bp_uLZysKv3lt1EDHeMQcR5Ns3J_rtETtbSbrzWBRcL340bYCU3aFYM9RxCWzDiGu9tBbUdYxToD_-b7n9a_RBIdZMPUwG75B3U2xYit6zgrR3qCzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=IQFxmmOtfyP45g7Thlnxk0OK5QAKWFYsYR8df6kfe5UwyQYEY_VFuTm7YXP_zXEnBdSMCovzeoF5jMb2LLLy0POtFGaV5iMVEd9rzPL3nHc8MbDT60TYQmXBA1wj1Rry4CEOYPZOltyb2r6bZAtN3_33BMVMJQ2SZzb5As0g4mmdZyaYSJhm4bKs_O-CEMQf6V3Fjsi_aD-gVFSClMRcBPUiEGAUL-Yrb7x2bp_uLZysKv3lt1EDHeMQcR5Ns3J_rtETtbSbrzWBRcL340bYCU3aFYM9RxCWzDiGu9tBbUdYxToD_-b7n9a_RBIdZMPUwG75B3U2xYit6zgrR3qCzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پرامپت هر ریپازیتوری رو به یک نقشه سه‌بعدی تعاملی تبدیل می‌کنه
🚀
بده به Claude تا یک شمای ایزومتریک از پروژ با Dependency ها، مسیر داده‌ها، و توضیحات کامل بگیری
💥
📐
معماری رو مثل یک شهر سه‌بعدی روی Grid می‌سازه
🏢
هر بخش از Infrastructure = یک ساختمان با شکل متفاوت
↔
مسیر Control و Data رو دقیق دنبال می‌کنه
📄
به فایل‌های واقعی Reference می‌ده
✍️
پرامپت:
Analyze [لینک ریپو] at latest main. Create an isometric system map with legend and explainer panel. Show infrastructure as varied 3D buildings on a grid, with dependencies and payloads tracing real control/data paths. Cite files.
✈️
@ArchiveTell
|
#PROMPT</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7498" target="_blank">📅 22:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7497">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhpmsAD7wn7AjN0lb9qclqh0exI7v_NRD360HNYEK9b_Lqr1hs6umes8o2_D4HWP-CgcALtKkppGAQxnQfwju3GFy1JrqXcZk9YQEv7h27TMfBRFqJeSUwcaZzK8ep47eVshS1nT8QjpSKVx0V7d9rU7eax33LJICuJ3_X3mJ3o514B41eBJx8SRhujXqIZnz8yUIOKtmglTxkIKkx_yPpIrmXnDq49AMlQx5iF2ynMW6lkW8UQlsHuoE9WAKiAf7cphwjoOXstd1O50Gbe_-_nRLFE7Lxt4pTj4q9-2b17ZaMERvYXV1nRGZuYaKE-Sjwcrpz67UmAEkn-SnRMOKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧹
این ابزار متن‌باز، ردپای AI رو از فایل‌های شما پاک می‌کنه
ما watermarks-remover رو پیدا کردیم — یک Agent Skill به‌همراه یک سرویس رایگان که Watermark و اطلاعات پنهان تولیدشده توسط مدل‌های AI رو از فایل‌های مختلف حذف می‌کنه.
✅
📄
ده‌ها فرمت رو پوشش می‌ده:
PNG، JPEG، SVG، PDF، DOCX، ODT، HTML، Markdown
🔡
کاراکترهای مخفی Unicode و ردپای متنی AI رو پاک می‌کنه
🖼
متادیتای C2PA/EXIF/XMP رو از فایل‌ها می‌زداید
⚙️
کاملاً متن‌باز و رایگان، با پشتیبانی از Claude، Gemini/SynthID، OpenAI و مدل‌های Open-Source
🔗
لینک پروژه گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7497" target="_blank">📅 19:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7496">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6E5CWJG-9D6wqKb4QHrx2NCd5w6b3wJohIXL3qf4FDcpuTVyJ6Y6XTFhTRINH8KGtiiL7-j0Cv-cNkx1bZXpJTKiblSupAWn67XxB8q8Qk5hH_Dlb5O98XbHs3UeCs4DiTHN5dEsQ78FIIpENAQlOvNcvRS0opaTWNqsfj_zS8Q3_ZZzrJim7ZTF6T4CY_jXBDvhg5zP5MF5UJTqv2Ajm_V3GIoUcAX0vIeJMNRW6OPHlRsF6BXgw-Y-Hx8NNV6jX9T81FDM3sj7RX4s2bzywD6sfMKDrsmZ6UQDvWAQs_4TjozR6FmfSq3wqtQivScoIonV8GjRrn_-zLPYrYlAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به برترین مدل های جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Grok 4.6 | Kimi k3 | Qwen 3.8 Max | Deepseek V4 Flash | GPT image 2 | Seedance 2.5
✅
این سایت بهتون 5 دلار به مدت 7 روز میده تا بتونید از این مدل ها استفاده کنید
💵
یکی از بزرگترین فرق های این سایت اینه که مصرف مدل ها به شدت پایینه و کریدیت خیلی کمی رو کم میکنه
✅
📌
Base URL :
https://heyroute.ai/v1
🔗
لینک ثبت‌نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7496" target="_blank">📅 17:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7495">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=Md1LONgNYl6ekW3JUPKQBZh_linQ1V1QhSlYGqCiBPVydBT4_cA6kd4A4DBUpYU0JOuIBJQQQAxCzRhaiZDfgjNGnRfN6c5bVkz9Kvg3Z-regSLZ_0nTN03u-PA1HCWYjnPdzn1mFfU15DIO9IzqzQvbnAnOUDjo10YGvBEHd1cvVpe2xgEKFQIS7kpqZIO183YPjN-1ONhpbH92Er2wy4QRTsGvzVg4ImGvV5vKYAniyp-8qyoC-93ZmDW61MD046cmUeaEpHtCWyj7dIhk_OngwcRaDqrmMgys8KqwU3WQZ51BUJZ3hAL5MdziCVS7an1Ei_IGxDx96CNvs7KNDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=Md1LONgNYl6ekW3JUPKQBZh_linQ1V1QhSlYGqCiBPVydBT4_cA6kd4A4DBUpYU0JOuIBJQQQAxCzRhaiZDfgjNGnRfN6c5bVkz9Kvg3Z-regSLZ_0nTN03u-PA1HCWYjnPdzn1mFfU15DIO9IzqzQvbnAnOUDjo10YGvBEHd1cvVpe2xgEKFQIS7kpqZIO183YPjN-1ONhpbH92Er2wy4QRTsGvzVg4ImGvV5vKYAniyp-8qyoC-93ZmDW61MD046cmUeaEpHtCWyj7dIhk_OngwcRaDqrmMgys8KqwU3WQZ51BUJZ3hAL5MdziCVS7an1Ei_IGxDx96CNvs7KNDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پرامپت، کل معماری پروژه‌ت رو نقشه‌برداری می‌کنه
🚀
پرامپت رو بده به Claude، بذار کل Repository رو بخونه، دو تا خروجی حرفه‌ای تحویل بگیر:
⚡
کل کدبیس رو تحلیل می‌کنه
🔗
ارتباط بین فایل‌ها و کامپوننت‌ها رو کشف می‌کنه
🗺
معماری رو به‌صورت دیاگرام تعاملی می‌سازه
🧭
مسیر کامل هر Flow رو ترسیم می‌کنه
💬
برای هر Component یک Tooltip توضیحی می‌سازه
📤
خروجی:
🖥
فایل HTML مستقل
دیاگرام تعاملی با Node و Connection، پنل Flow کنار صفحه، کلیک روی هر Flow → Highlight مسیر کامل، طراحی تمیز و Responsive
🧬
فایل JSON برای AI Agent ها
ساختار: { nodes, edges, flows: [{ steps }] }
مخصوص Agent هایی که باید معماری پروژه رو بفهمن
✍️
پرامپت:
Analyze my entire code repository thoroughly.
Generate TWO ready-to-use deliverables:
1. A single self-contained HTML file containing:
• An interactive architecture diagram (nodes + connections)
• A flow panel on the right
• When a flow is clicked, highlight the complete path
• Tooltips for each component
• A clean, professional, and responsive design
2. A JSON with the structure:
"{nodes, edges, flows: [{steps}]}"
The JSON should be specifically designed for AI agents to understand and navigate the project architecture.
✈️
@ArchiveTell
|
#PROMPT</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7495" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7494">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWmwQtg9OPn3M5Pd6YCbSN4BmEwubBC0bgJGLo7V6tUZbRfHcpQd-s4atNXtdDJrILUjBRMpK4K1Vo57mAhUdSRPtXcuU7xIr_SJq36T18-WYMKGy_EUJ2RbTqPq6c5h7SWZSTk-KWWiFdaHwmw3eL5gVy4Jb8amfc-F2GnOWTp0aLaom3tsLuAc1j2GqbNfLY1KFI23-c8Ify5keMjX-lZEfPjrCer9hF5k_hwQcYLejL4-XO3mWvgTzPvv7hrji9_yC4nAEgsQiqqKcKEQE_u-7Ff8vvLH6XJAs6KQWAsqeG2RwpmKkJ_q5Bvcxe1b6QAcjrv2ifPzP1eUTh282Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی رو به یک ایجنت هوش مصنوعی تبدیل کنید!
🚀
دیپ‌سیک با معرفی DeepSeek Harness یک محیط جدید برای ساخت و اجرای AI Agent ها راه‌اندازی کرده؛ پروژه‌ای که خیلی سریع مورد توجه جامعه اوپن‌سورس قرار گرفته.
🔥
💡
ایده اصلی Harness چیه؟
تقریباً هر چیزی می‌تونه به‌عنوان یک Plugin وارد سیستم بشه؛ از مدل‌های هوش مصنوعی و Sessionها گرفته تا Skillها، Sandboxها، چرخه‌های اجرای Agent و حتی رابط کاربری.
⚙️
معماری Harness بر پایه‌ی Cordis طراحی شده و این امکان رو می‌ده که کامپوننت‌های مختلف حتی در زمان اجرای Agent هم تغییر کنن.
💥
چیزی که Harness رو جذاب کرده اینه که محدود به یک مدل یا ساختار خاص نیست؛ می‌تونید اجزای مختلف رو با هم ترکیب کنید و Agent موردنیازتون رو بسازید.
🧩
حتی جامعه‌ی توسعه‌دهندگان هم دست به کار شده و هزاران Skill آماده برای Harness ساخته شده که می‌تونید ازشون استفاده کنید.
📌
خلاصه اینکه DeepSeek داره یک رویکرد متفاوت برای ساخت AI Agentهای ماژولار و قابل توسعه ارائه می‌ده؛ چیزی که می‌تونه برای دنیای کدنویسی و Agentها خیلی مهم باشه.
🔗
لینک گیتهاب پروژه
🔗
لینک سایت پروژه
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7494" target="_blank">📅 13:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7493">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McW6xf4OFvxlslXKtVYEpkptGuSUYKJGaneOsO-BcU5cIjDXE5EGJnmyIswjfWjQolDfTArsllJ6TKRKul8HuVgrClhi4F1l55YR_jG-9pdrJQzIAoICyZlQZCvvZnlPztL6FsSwi9hXI2JwaRuYfkrVnNS-ZF83tIkRiqqtwpakWJhHR3l1ETo-PKaUH7oUuVmul7HHv-HRTKlbT3tlEsh2wBxcLefb-R4qsd2ipnQvX8oJrI1xFHk5rT8K3G6rdsiRmERkAAiZFW6srdWxTCW-R2f9WZDFzp5CH8GsGMr59kiP_-tLfwBbTXENZ0irgMc367hp2uWJMvVmXBIlqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست طلایی سرویس‌های رایگان برای برنامه‌نویس‌ها
🖥
سایت
free-for.dev
یه لیست
کامل و مرتب
از سرویس‌های
ابری
و
ابزارهایی‌ست
که پلن
رایگان
واقعی دارن (
نه فقط تریال چندروزه
)
🆓
از
دامنه
و
هاست رایگان
گرفته تا
دیتابیس
،
CI/CD
،
مانیتورینگ
،
ایمیل
،
ذخیره‌سازی
و
خیلی چیزای
دیگه
🔸
اگه دنبال
ابزار رایگان
برای
پروژه شخصی
یا
استارتاپت
می‌گردی، حتماً یه سر بهش بزن
💻
⭐️
Link
⭐️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7493" target="_blank">📅 12:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7492">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=fXx2oGL1Ve-8phubWmYb4wd5sMa7ml8o9JFT0rlDUJGWHbh3HBMzvG6mbRPwhPS5ZxXeiw_kVcNoaKa2mxcjLnmoWmzYfBwJRU-FwKqmTADqL6SwbS59n_GenlKEMNHm9LLT5iLMHYUwEIR6vGATgNaVSykylGjh0Ypb7wRPWBNywzHXZ_YTeNllWbUqaUN3Vf6J-5XfFP0qI5iRIYTz3GTw5TCZ_Uhw_PHSqkuitqF4MXsy8C2fLH2alBBSnt7OdWB4zfpILX-xlU5owezDko8nc-SjQMgebGCTAwDWS-V_jRaDYySC-2HEsGJhHPfLXuil583TSUFkqa4pi9HZtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=fXx2oGL1Ve-8phubWmYb4wd5sMa7ml8o9JFT0rlDUJGWHbh3HBMzvG6mbRPwhPS5ZxXeiw_kVcNoaKa2mxcjLnmoWmzYfBwJRU-FwKqmTADqL6SwbS59n_GenlKEMNHm9LLT5iLMHYUwEIR6vGATgNaVSykylGjh0Ypb7wRPWBNywzHXZ_YTeNllWbUqaUN3Vf6J-5XfFP0qI5iRIYTz3GTw5TCZ_Uhw_PHSqkuitqF4MXsy8C2fLH2alBBSnt7OdWB4zfpILX-xlU5owezDko8nc-SjQMgebGCTAwDWS-V_jRaDYySC-2HEsGJhHPfLXuil583TSUFkqa4pi9HZtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📝
♊️
گوگل هر ریپازیتوری رو به مستندات تعاملی تبدیل می‌کنه
گوگل ابزار جدیدی به نام CodeWiki معرفی کرده که با بررسی خودکار کدبیس، در چند دقیقه یک مستندات کامل و قابل‌فهم از پروژه می‌سازه.
🚀
🔺
ساخت خودکار دیاگرام و نقشه پروژه
🔺
توضیح بخش‌های مختلف کد و نحوه عملکردشون
🔺
تولید راهنما و آموزش مرحله‌به‌مرحله
🔺
تحلیل معماری و ارتباط بین وابستگی‌ها
🔺
ساخت یک چت‌بات آشنا با کل ریپازیتوری برای پاسخ به سوالات مربوط به کد
یعنی به‌جای ساعت‌ها گشتن بین فایل‌ها و کدها، می‌تونی پروژه رو خیلی سریع‌تر درک کنی.
👀
📌
این ابزار رو از دست نده!
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7492" target="_blank">📅 12:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7491">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTJN61LopJrE6P4rrgRf3mL4vi1bFIgsHt65BIkByJLB8CUOncsbiU542f6m4BVxQ0gnErAYFqsUh-x1h0ep5ehiyhk1FxcT7wYgxDm6uzR-ZAW0AnyBF_Nx5GeH_LM9toDBEjsPRAXRZN3TO7rcHtZZ0k4UWj_NPPvz5Pjb8egAnlFLDL476Foshohq2-oBPttWaaXH7Yqs7UhrgbwHtH0rqND7R1ZgWky6D_G9Xqs5zNX3iX7NxPPkwOuzBaKl7T5Vf8ezPc4pPfIKFNptz35Sk-CR2nMn6nptV5n3xtUUF-Km5aCZv17GmPGKAd3Um8Ic8dJ8W9rM0dtmT1W-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">TorrentSearch
♻️
اپلیکیشن متن‌باز اندروید برای جستجوی همزمان تورنت از چندین منبع
📱
با
TorrentSearch
می‌تونی
خیلی سریع
از کلی
سایت
و
پرووایدر
مختلف جستجو کنی، نتایج رو فیلتر و مرتب کنی و مستقیم مگنت لینک یا فایل تورنت رو بگیری
⏬
امکانات اصلی
💭
جستجوی همزمان از چندین
پرووایدر
(قابل روشن/خاموش کردن جداگانه)
🎁
فیلتر بر اساس
دسته‌بندی
(فیلم، سریال، انیمه، بازی، کتاب و ...)
📁
نمایش تدریجی
نتایج
+
مرتب‌سازی
بر اساس سیدر، سایز، تاریخ و ...
🪣
جزئیات کامل هر
تورنت
+ صفحه جزئیات داخل خود
اپ
ℹ️
ذخیره
بوک‌مارک
+ خروجی/ورودی گرفتن
🔖
حالت
Safe Mode
برای مخفی کردن محتوای
NSFW
🔞
پشتیبانی از
Jackett
/
Prowlarr
(
Torznab
)
🦾
طراحی مدرن
Material 3
و
دارک مود
🎨
⬇️
دانلود از گیت‌هاب یا F-Droid / IzzyOnDroid
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7491" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7490">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⚡
پرامپت‌نویسی تغییر کرده؛ این ترفندهای قدیمی رو دور بریزید
بزرگ‌ترین دلیل جواب‌های پرت و توهمات هوش مصنوعی فقط یک چیزه:
وقتی جزئیات بهش ندید، جاهای خالی رو با حدس و گمان پر می‌کنه.
❌
ترفندهایی که دیگه منسوخ شدن:
•
نقش‌دادن‌های کلیشه‌ای:
نوشتن جملاتی مثل «تو یک متخصص ارشد با ۲۰ سال سابقه‌ای...» تاثیری در دقت نداره. مدل به فکت و داده نیاز داره، نه عنوان شغلی تخیلی.
•
تکیه به
Temperature = 0
:
صفر کردن دما جلوی اشتباه رو نمی‌گیره؛ فقط باعث می‌شه مدل خطایش رو با لحنی کاملاً جدی و بدون تغییر تکرار کنه.
•
پرامپت‌های ۳ صفحه‌ای برای تسک‌های عادی:
طومار نوشتن برای کارهای ساده، تمرکز مدل رو به‌هم می‌ریزه و احتمال نادیده گرفتن دستور اصلی رو بالا می‌بره.
✅
فرمول ۴ مرحله‌ای برای گرفتن بهترین خروجی:
۱. هدف دقیق (نه کلی‌گویی)
❌
نگو:
«این قرارداد رو بررسی کن.»
✅
بگو:
«این پیش‌نویس رو بخون و فقط بندهایی که بار مالی اضافه برای خریدار ایجاد می‌کنن رو پیدا کن.»
۲. بافتار و مخاطب (Context)
«مخاطب فردی بدون دانش حقوقیه؛ توضیحات رو کاملاً روان، ساده و بدون اصطلاحات پیچیده بنویس.»
۳. بستن راه حدس و توهم (خیلی مهم)
«اگر پاسخ یا عددی توی متن نیست، به هیچ وجه حدس نزن و صراحتاً بنویس: "اطلاعات در متن موجود نیست".»
۴. قالب مشخص برای خروجی
«پاسخ نهایی رو فقط در قالب یک جدول ۳ ستونه بده: [شماره بند | ریسک موجود | متن پیشنهادی جایگزین].»
💡
اصل ماجرا:
هوش مصنوعی ذهن‌خوان نیست. هرچقدر دامنه حدس‌زدن مدل رو محدودتر کنید، خروجی دقیق‌تر و کاربردی‌تری تحویل می‌گیرید.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7490" target="_blank">📅 21:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7488">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REll01cRvKr1hd62zcQdb4joJbjOoC9pN_RuhGhglF2tk1MrxUwhQBK_DzSGQ5DyFeLCWiHt0aTHwkNehT7b7ctt2wddoyu4--idboG-Ev7bhKyjIC0l1AK5yJKCqtZU8xeb4wXXbWgBVIpk_nVn4qmhLkG1m54Me3v9-zAVaxotfcrwiqg0FYyYmVx8-G4yJfkMjTiWBsbD2kh5fQXjrlhMGu6RZJ1CoykhabNUw_iLDMrqcZuc7miD_B084Rptd4cM0vH78gsZzfI7QEgOgstggXkj8XzwCpixdtFb_bTHO8RGFSejULl2fX1Ha6JpJC8CtmtGrOUTn6RFOHFxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به برترین مدل های هوش منصوعی به صورت کاملا رایگان
💥
🆓
Sonnet 5 | GPT 5.6 Terra | Agnes 2.5 | Mimo 2.5 | Gpt image 2 | Nano banana 2
✅
📌
Base URL :
https://ai.furry.vg/v1
حتما در بخش انتخاب گروه ، گروه Free رو انتخاب کنید
‼️
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7488" target="_blank">📅 19:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7487">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBtqwGF9KY35xl0R-2wnJL4Oa2DtZb9MFRUTyYBrlcG1stexcMbYlChulfcrQ7RPxebGDa_tSC97VmEPvJrWynqe2uUMp4KDG5SVdwgt3V9R8yeJ6I60SC1dbCZclr-StggWAX7M4N6hai01IOoa0UbxYrcJGb0y_hCLZ9refdaxlLObCQTkSJGdgralp2Qdamf11dtsFYkwdpPDQqv0z29BQTD8UAmDWD5wAC65kT7rPOp9i9DgmOdulpfIPFx1-5EzuE520u67LMKNo7VGYu6cWAjEcWWXE1h1jZhpqusiCPzDoU8lalv9uFYkD97yvMW6zFbjVju2wjCeZgn1tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل Qwen 3.8
💥
🆓
با سایت Runinfra تا 48 ساعت آینده میتونید به API مدل Qwen 3.8 دسترسی رایگان داشته باشید
✅
📌
Base URL :
https://api.runinfra.ai/v1
📌
Model ID :
qwen3-8-27b
به دلیل شلوغی سایت ممکن است پاسخ مدل کند باشد
‼️
🔗
لینک دریافت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7487" target="_blank">📅 17:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7485">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8dGRzxxCkj59_NUOB5s1YBcYXbelg_QkkhYMNxM7-jVr_R-RP4g_yB7thZfhOZ83L0Pg8azsxpkWtVrX2t76s38LR-qOAadEJIlzFc9NGeTwfdUzS0K5FyatoCB0pUTPOwKAWJs8uuMoEh2A8NXORiJlzM-yLLlygqG6UTJCFER_bm9NaG89YUudsxRuIOs75XIkO7Xgo8hpfddBKmrIBB_iB82mz456jsdsNhEyNRdC_5piDnYGf-MaA2_5VLjALYtv0pLTVwLa0hC-Bs2NfVrIwMD3ZeD5cEdVejkoLkAAvyG99GuvFNUjVBTff8u209xjj3prDvz991uinQQYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های هوش منصوعی محبوب
💥
🆓
Qwen 3.8 max | Deepseek V4 Flash | Deepseek V4 Pro
✅
📌
Base URL :
https://api.orcarouter.ai/v1
🔗
لینک ثبت نام
🔗
لینک دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7485" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7484">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqfBeWHJmsa5YiSLAXc2Zp4FFdeRB73a_xnURqRpJqRnKc25mpQvTHI3S4NbgnBMIVTRG5pwccFEM7tf8g6E5Wd_roAXPxBh_uEvNGtxyPErGHrpjriZoIIWMLyrE3U8_Gn_IdJcY5bq7V05wJ8xjEUQ35htRcn-q0V3auAXW2H_SJlhAXIRfoebxUY4SpVTRt34BHnV-o8eyjixUcBrD6OTlGO_bd1jeMkudJNEaTWdjfopB7bRQI5rNqY4K19-UTILNAkpfoI1j3qQCPNOE1KaDiZ5DupgVcFrb1yxZ-g9PDcNVusrCeeNcEzJ0qfp3l7tc3DV4Gs6UzI6JmO4mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون توکن برای استفاده از GLM
💥
🆓
به مدت 5 روز هروز 3 میلیون توکن برای GLM 5.3 و 2 میلیون توکن برای GLM 5 Turbo برای کاربران جدید در اپیکیشن Zcode
✨
مراحل دریافت :
1️⃣
وارد سایت
z.ai
بشید و با اکانت جدید ثبت نام کنید
2️⃣
برنامه Zcode رو دانلود کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7484" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7483">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">هدیه ویژه برای شما
🎁
100 هزار دلار کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
sk-bY9B0parF18s5v1wasRyzRZsVLzICaSVfZNVEMrqG2Rlt7dH
🔺
Base URL:
https://ai.venlacy.com/v1
🔺
Model ID:
glm-5.2
به دلیل شلوغی ممکن است پاسخ ها کمی کند باشه
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7483" target="_blank">📅 17:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7482">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKggzSViydDaeqOyWxZFVpVbQOVbvDMFY6gacKTr1TxYeffJ4BhsICiEXOSFsUHZha8Twbu0J7_Ih7PDN0xE2wta3w5dOhT0EzhJVDDruonL0s4tYBGmPb5ZqErBVC_w_JwBqBxjYAcCbBWvFEY23NnhZRXpV3j3AEmX2ET5Y-S5DgSjJ9G0Ut_vJeMT7J1aJddqRawI2uEVXwPIXgblcHK3sEmk3l-5FcGQCG8cQuWlmjeBWK0Mm6x93CL6evmc7m_8LhasUNWD7PnSfc-jBtuvHY5aEbhUQye-VYlIGOvx13_z9U9erAJNKrjV7eJhOs_O6Pw1FA0jNXBDc7Ka3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 رونمایی شد
🚀
نسخه جدید GLM با نتایج بسیار قدرتمند در بنچمارک‌ها عرضه شده و در چندین بخش از رقبا جلو زده است.
🔥
در مقایسه با مدل‌هایی مثل Kimi K3، DeepSeek V4 Pro، Qwen 3.8 Max، Opus 4.8 و GPT-5.6 Sol، GLM-5.3 در بخش‌های زیادی عملکرد بسیار رقابتی و حتی برتری دارد.
⚡️
🔗
دیدن اطلاعات بیشتر
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/ArchiveTell/7482" target="_blank">📅 23:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7481">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-qFy8KWoQhtE7GVHGnYW8iEEWpKq0P56BZkh699-WycFzSsHhP29GvFX2lqh7nynpIu-Z_GHjJYTROEcdtAXbS0NC9FMr5H-67CZ7yuC4gu59E4U7LXE5rcn43fcH8ONLiYn1w391b8LvFl7UGsL1QH6K6Bzf8QI2KxK0p3UrRTze1HP4GlwrymU5FYCUi_88uL0Y8IquymlvbpyLVQQgQJqmBJkCFjSBMmFeZIngVbV7s3C3TaSi8-SFwNq4cMBdn_WxHK6GdvcDnvK8HXWUq0qC1sdhUYCITz-Uz9O9wHYZpAJ_k2xfSFBxdIwjp4LqRVMzZwH-aH_c_GyczrIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان: امروز از ساعت 12:30 تا 20:30 به…</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7481" target="_blank">📅 15:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7480">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7480" target="_blank">📅 14:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7479">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rl4chbo3FKEDwX6V8NCndkls_diVLfTnS5RCPya1MDjh6-wlqfYlOkh1M4R-sm45HB-KVUmCXZB-0hHaZzplFGPY-8fDo1WvBhYaWIL27-g6FKXFxqvXtHXwWLJyftj6TLdr_DcCHeX8OtIwTSCgqVvlUYK0-KgSxz4IolxAXix_CU795WPaEi1HQzDylVmnEPO_lNDht9lzMGDToZDs5TIRvwyxlmb4d9wlTlPBccTFp6oZTZrYmL1zypm4jtMcGSns77K0ZsItE4SM28n2XO2g37UO7ZOh7GY9YyjqrV82ASHsyh4xkSrH4LtpC-juc3OoiY1mtBPLZeoAkrV0FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ تست رایگان مدل ‌Seedance 2.5
⁩
💥
🆓
‏اگر دوست داری ویدیوهای سینماییِ ۱۰ ثانیه‌ای با کیفیت ‌480p⁩ بسازی، پلتفرم ‌JXP⁩ این امکان رو به صورت یک‌بار مصرف برای هر حساب کاربری گذاشته.
🎬
✨
‏مراحل ساخت:
‏‌
1️⃣
وارد سایت
jxp.com
شو و ثبت‌نام کن.
‏‌
2️⃣
به این
بخش
برو
.
‏‌
3️⃣
متن یا تصویر دلخواهت رو وارد کن.
‏‌
4️⃣
دکمهٔ Generate Video رو بزن.
‏برای این تست اصلاً نیازی به کارت بانکی نداری و کاملاً رایگانه.
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7479" target="_blank">📅 13:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7478">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پرامپت تولید شعر بی نقص پارسی!
از پرامپت زیر استفاده کنین تا ai براتون شعر هایی در حد شعر های حافظ و سعدی بسرایه:
تو یک استاد مسلّم عروض و ادبیات فارسی هستی. در سرودن شعر، اولویت مطلق با صحتِ
دقیق وزن عروضی است. پیش از نوشتن هر بیت، آن را در ذهن تقطیع کن تا مطمئن شوی
واژه‌ها (حتی کلمات غیرفارسی) دقیقاً و ریاضی‌وار در جایگاه درستِ وزنی
نشسته‌اند. خروجی نهایی نباید حتی یک مورد سکته، لکنت یا ایراد وزنی داشته باشد و
باید کاملاً روان و موسیقایی باشد. حالا یک شعر شاهکار کوتاه و روان درباره مناظره یک قناری و دایناسور بنویس
.
﻿
تست کنین، به همراه مدل ai استفاده شده شعرهاتونو کامنت کنین، بهترین شعرو که لایک بیشتری بگیره بش جایزه میدیم
🎉
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7478" target="_blank">📅 22:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7477">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">Gemini 3.7 is out now
😍
از اینجا میتونین رایگان تست کنین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/ArchiveTell/7477" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7476">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lU2YyunFHH59fPnM84osVwKKX8CCFXKu163ruUXMerSFrvSganXzp_1R26wuCbupq41mKQeBtYcUpol517Cb27ZsH4toO7ROCgVpq1EYiS1tofvi_FHkpsUlTtddyHfTjXegDVNFpHKozjiMWL0FUm4oj5N_QNSsAkuryNLP8LalH0Zt_vgBV9v6_8FHqbtz8C8xnAFd8VfWg5AlA4xY4yFUgZsJ7SxEeojx-jmo2_oWtmTIhBL0T0Vlp2OtMp5mkROXkZWkGf0ro2fBZg8SBLIyZBTJHyW787E45QvCc4uV2vBYPUPtNGRtDPKkQxhgM7Vv0IUV2-YlK0g5B1RnOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
CiteSeerX گنج رایگان مقاله‌ها
یک موتور جست‌وجوی تخصصی برای مقالات کامپیوتر و علوم اطلاعات که فقط به جست‌وجو محدود نمی‌شه.
👀
🔺
میلیون‌ها مقاله + جست‌وجوی متن کامل
🔺
پیدا کردن منابع و مقالات مرتبط از طریق شبکه استنادها
🔺
اطلاعات نویسندگان و تحلیل تأثیرگذاری
🔺
کاملاً رایگان، بدون ثبت‌نام و با دانلود مستقیم PDF
🎯
برای پیدا کردن سریع منابع علمی خیلی کاربردیه.
🔗
ورود به CiteSeerX
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/ArchiveTell/7476" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7475">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">20 دلار برای دسترسی به مدل‌های هوش مصنوعی GPT مانند
:
💥
🆓
GPT 5.6 Sol | GPT 5.6 Luna | GPT image 2
✅
وارد سایت شده و ثبت نام کنید سپس یک کادر میاد برای جوین شدن در چنل و غیره ، کافیه فقط روی دکمه ها کلیک کنید و پس از ورود به صفحه بک بزنید صفحه قبل ، سپس روی Claim کلیک کن
✅
Base url:
https://apimaster.ai/v1
قابل استفاده در
Vega Agent
✅
🔗
لینک ثبت‌نام در سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7475" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7474">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7474" target="_blank">📅 17:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7473">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpXDUfze4Y85jaO1IL8Fyvrdo3AfIP-sQrdr5gwAY05VAWDegL5PQe2GIJN_WZbhtnxHuYOSdNkYCuzUDoGwfQfU7sovQV-UI6SdF8wQkeKbiRYBDgEggTLJlMQwjOSDSExFofp2FwDSU989gcp2WQJoKX0so2t-ATe2mct8KoNAHaKkSQrbbI0NNWFyNhZKdZu1dQFoJvlAd29yFVtFOKY5Zx0b1gAk094ZsBuI-vEZfN39VduVe_mFCpRBHkMoPSEOw8AkSGr339U707ZtMV0b5p7IoGZ_EsWTNEzmnMVymKDxPy4huy0foFPdqlpYqDx2m7ZtLmXEOfMBCNd0qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4 Pro 0813 وارد رقابت شد
💥
مدل جدید DeepSeek با قدرتی در سطح Kimi K3، GLM 5.2، GPT 5.6 Sol و Fable 5 معرفی شد.
🚀
🔺
سه سطح Thinking: کم، زیاد و حداکثری
🔺
عملکرد بهتر در تحلیل و برنامه‌نویسی
🔺
اجرای خودکار وظایف و ساخت گزارش
🔺
پشتیبانی Native از OpenAI Responses API
🔺
اتصال یک‌کلیکی به Codex
🔗
تستش کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7473" target="_blank">📅 17:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7472">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrFzhIY5yyOWB8OSFXteuV6NPQ7I_LlN3RySp8ZnkLFhD5iEbPR_TBn7N1wmIJeCNlaDGjVWEcsRd8z7a_8wYApicL-GxXF_ZA3QapH_0sNPgyP4xgYCXlJ3_l8myzLcueUzjl1JevuBCNYWza453zNgCrqsnoniA0zmvGEX0s7BMomYYiwy_P8Jd_kSDO6VU6lKhupoctPNoHbIFVyRYyTuDAAtoCgYF2LwLgXh9dJreVLeH7h_eEM38kRk-bKZmjlKhar0cShjNborC98ZII8s4WHnaF2Yxw2JZTWnnrKsmuAdfM4fXZIXm4PXTFCwwcbbca8M3jpky0DmZOv5jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های هوش مصنوعی محبوب
💥
🆓
با این سایت
روزانه
300 کریدیت رایگان دریافت کنید و از مدل های هوش منصوعی زیر برای کدنویسی بهرمند بشید
✅
Sonnet 5 | GPT 5.6 Terra | GPT 5.6 Luna |Gemini 3.6 flash | Gemini 3.1 pro | Haiku 4.5
✅
🔗
لینک ثبت‌نام
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7472" target="_blank">📅 15:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7471">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L01PFq0BHvHt2Jqp3NawQ_x73QCakTBiQYhF_ikC2pTJyoY2nqq8Cq3G0k8fNIYnrwVzvVg8tt92iCwE7hNPbs1eI097wBRU6W0RkD52qBDkFqBUxWf1nGIwzHak2Qf_Ji8BslJCIEBC_OPeZfCle57YwAc1xEVRvvPLIAj4m5XTsekB8RH1b9sSujCQ5xuNo4t11uzDi48NVEVBj1q-BIIMEFgYLh1l2QGcL_A7HRUZyq68rQaQ2ZgQElhQ8liTRxZS7GxZzLfPQVEAGIeFgLfN9WPZiuUbWs8mnbvrf1fDwqG0mVaJyhcugGdDC4d-LJC1iXd3Qhbg7hU16Oh8Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کریپتو‌مارک مخفی Claude حذف شد!
🥸
هوش مصنوعی Claude روی متن‌های تولیدی خودش یک نشان نامرئی می‌ذاره؛ چیزی که با چشم دیده نمی‌شه، اما در الگوی انتخاب کلمات پنهانه و می‌تونه برای تشخیص متن Claude استفاده بشه.
🧑‍💻
حالا چند کدنویس ابزاری ساختن که این الگوهای مخفی رو در متن تغییر می‌ده.
📥
فقط متن رو وارد می‌کنی و نسخه‌ی جدیدش رو تحویل می‌گیری.
🔗
استفاده از ابزار
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7471" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7470">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4oSoakAxBB2_QqQIp3LLXl0suNPwLgT40RSxBOYtib5GtzP9QKgGhA2mJtPQaxs1WN3K_Jscy-iAXscfHfkdtB9LRJeZOma5ORVR7ugxBGeg4nE_iXdsLqG4rqgUNsktugcND-Ttb11aq1n2ilOJIc8aFAJMF51W4A2rEhsF4KBq8-ZawU21DXzuduFjLp5vHpFPHMj35hdoCDRblia8-EqBqZHiGYFvfKxQ09yiKPtRGyFcVwh4fBDh0O7b8xPFXTupA1IssIbLB_rb9IBBMN45Mf-ZrHPyn7THedfITWvhHjYXwqhvVzKVAVvLm9cAxyXojNJF1nfY3VuKhtmKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد  قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود ۱.۵ تریلیون پارامتر داره و قراره در آموزش SFT و RL پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:  چند هفته بعد، Grok 4.7 با حدود ۲.۱ تریلیون…</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7470" target="_blank">📅 23:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7469">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">https://t.me/ArchiveTell/7053</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7469" target="_blank">📅 17:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7467">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCroylOUxTy--evyDXItkivoWqLlgXR00unJK1gqhC82LvJHWd8lA5wQeCVT4F7T9TTsGTTycoFiAjPwEeu0C6tCiRoOHX5r2oF0ihOZhHgUodlqvojh57m6vCpUW93zixHpgSQlzUyK-reboUCPrS-DAxgjjHVXUQ_9JNxruhfhqksLaw2Qtj606KECKrF24GCosxBDywwRn0a8oTkfLNigUe1udWRQPpuRIm8672ngBLzRsD8b6Y8tfioXkAdyVs1to1oy3HDXg1lhKsNr-4Cm1xDHf8jCR21KH07FCrWN5focWhv-RCEOcA7MRC6hbsCNIywmMU8Itr-AvsP8FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد
قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود
۱.۵ تریلیون پارامتر
داره و قراره در آموزش
SFT و RL
پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:
چند هفته بعد،
Grok 4.7
با حدود
۲.۱ تریلیون پارامتر
میاد؛ قوی‌تر و بهینه‌تر، ولی کمی کندتر.
✨
👀
باید دید xAI این بار چه چیزی رو رو می‌کنه!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7467" target="_blank">📅 15:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7465">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🎙
LivDub | ترجمه و دوبله زنده با هوش مصنوعی
با
LivDub
می‌تونی ویدیوهای خارجی رو
هم‌زمان ترجمه و دوبله
کنی؛ بدون اینکه مدام به زیرنویس نگاه کنی
🤯
✨
قابلیت‌ها:
🔺
ترجمه و دوبله لحظه‌ای ویدیوها
🔺
استفاده از
Gemini Live
برای ترجمه صوتی
🔺
پشتیبانی از
۷۸+ زبان
🔺
مناسب یوتیوب، دوره‌ها، مصاحبه و لایو
🔺
پشتیبانی از مرورگرهای Chromium روی اندروید
⚙️
روش استفاده:
مرورگر سازگار رو نصب کن → افزونه LivDub رو نصب کن → Gemini API Key رو وارد کن → ویدیوی خارجی رو پخش کن
🎧
🖥
مرورگرهای پیشنهادی اندروید:
Cromite • Helium • Ultimatum • Quetta • Yandex
🔗
افزونه کروم
🔗
سایت LivDub
🔗
گرفتن کلید جمنای
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7465" target="_blank">📅 13:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7464">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7ObsSYqUQ8fMFU3gMOiPyNQ4AbCKWLHNVJuVaUgpapMp5Q9H2A8Qj1EM3evJ1J4_2JjCZjEIbSugBq106d0dchycarEN6JBW7I2C3Mz8VE0DahzEPw39UL8UUtajJfIBmjWtsfbgHGT-i05d31GdMuhs1KQGVXb5cFMFEnX2fVwxE9sC9bh6fG2N8Fqss4Ku2e9EPpn8Fv-4s5DlP-1bmxcFKivSdFDf-Bj4tBeYctFEKus9_sWZV2UnU-G7W5z12UA4kHbAYu-HHzAmb_giaMLV4vdMybKAyhRPAdQ1bYfE7cNt2qoA8TgvgOsn8pSxqL_OhTiBDEKAc9fYIUx6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
FLUX 3 Video رایگان شد
؛Black Forest Labs برای مدت محدود، FLUX 3 Video رو توی Playground خودش رایگان کرده
🔥
⏰
فرصت استفاده رایگان تا دوشنبه ۱۷ آگوست، ساعت 10:30 به وقت تهران
قراره در ادامه قابلیت‌هایی مثل 4K، ادیت ویدیو و استفاده از تصویر/ویدیو به‌عنوان رفرنس هم اضافه بشه.
⚡️
✨
🔗
لینک استفاده
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7464" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7463">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آیپی تمیز
✨
188.212.97.3
94.182.177.92
185.50.39.15
103.25.85.84
176.120.17.44
45.146.240.17
45.146.240.70
77.237.246.20
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7463" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7460">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kz-5WefUjtaKrhsO_-hdydmR6GWiIEtPH3j5UVWL73U1OF9N_tRgonKEJBcP39qr40417sT7f-Ao7hx-KpFZSdo6-QYPfRMmxxN8ZQFteiTkiOcEe8slMfrDxPg63r5kQNl-DP2Ee0EVGk8mz7_W1i-jCnrvUTSm6grWGUmxTf3JTKocguq5k0ISuKtM8jst06ooI9WT9AgQF23TC3bkyMWQg_TT8Z1XDlMju_BPQr-40D7z7Jq5s10bUXOlmG6K5cVLIDuGfz6R90JTg0QRm_B4KxGDGySKc8NJb9Z1psWbk3A6HV3NApaCrISH8MKcohqEWIoDH4ugkz2L_b14yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از 1000 پرامپت کاربردی برای هوش مصنوعی!
🚀
یه سایت که مجموعه‌ای از بهترین پرامپت‌ها رو یکجا جمع کرده؛ از درس و برنامه‌نویسی گرفته تا طراحی و Excel
⚡️
✨
یه جور جعبه‌ابزار کامل برای کار با هوش مصنوعی
🧰
🔥
🔗
لینک سایت
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7460" target="_blank">📅 16:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7459">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHn3JakMpqjO-owyRKYiVwhYoW9B48C8lcH9L9aBEY7OlzBMl92ol_JhE-nOZJGbpTSqUuFJI3HqOeP_2TK65EZLhHgDiSUoumQ7vY82EcsUfkFu-IzN8P5wcSx2eIMCR8gtv7tqbGkf_qsgHX59dar6rDYOn9NzlRKyTt9EPRFPnLdQWhN4f4O8mOQBzCytIYWrsOJbBrTKLL9yTs4yziz7ak5cGyc2hjwzDGh3aJF4JeuMvc8XlKVx3Z1o4eudDO7fDXwroXddjGrBhTY_xwZzx8wVR3EP848XgCRDOIS4jZpjJfde_Kmea0Q6PbhgzunPCaSOuiETGnNQtKL1Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤔
گوگل قید Gemini 3.5 Pro رو زد؟
گزارش‌ها می‌گن گوگل عرضه‌ی
Gemini 3.5 Pro
رو متوقف کرده تا مستقیماً روی
Gemini 4.0
تمرکز کنه.
🚀
گفته می‌شه مشکلات عملکردی و سخت‌گیری‌های امنیتی در مرحله‌ی تست، دلیل این تصمیم بوده.
🛡
حالا رقابت جدی‌تر می‌شه؛
Gemini 4.0
می‌تونه از ChatGPT و Claude جلو بزنه؟
🤔
🔥
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7459" target="_blank">📅 13:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7458">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7458" target="_blank">📅 11:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7457">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYGDqV2M3pU1cq-CmkGpnd4XoVeOJP-O9EesiM7Ht6WMGBVre1g7VBc-pLtuElsXhuudI8YLAceuUlU0gIZMPdlr61AVV1ruvFL4ztiUMoiSPgT8ByKVD5utVoWSbE9h-amAZZQ8uYCvnfIUthEsAO-7ImDnBwFHp5l1e5F92DBlu47BXT1oe2GEcDTmUy1JEQNn4Z1Cf68k8ySzvslix5NijLmh4guovnFitZd6czi6q8WxVBml52HdeRa0-JX9oYY3RiHUkOtR5p7pWyNZ2Pqp6d-fVl9gpOK-k3gKnMvbU69n49r5Vq_G-XfHHcYHPmHNFf58QVNVvO_PJSDNog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">40 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
✨
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدیمی لازم نیست )
داشته باشید و از طریق این
لینک
وارد شید
✔
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
40 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/ArchiveTell/7457" target="_blank">📅 11:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7455">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eriZazi-Uhy2YDq5j7v9DtpsXLTTRK00PK1Z3Oq62UbaexR-K_4d6B8aM1j8OpZ22nIGLRHg24kPUf4gFSBV7f1j0qePba9SJpLBT9BDVfOVhw0H5h23veAbcD_ejBgLxzF_-qtrigovjGXFtljysmiFjoUNTYaKv58PqJEFPUFAKouyOFIKq9TymaolXR3DgIz2cM9h2olAsRA73m5vatIGMbexl0z5KuK46pQgNDLgpYj7kkHNGykOCmkqFe7EUkX0wcZ4pdAz4PofGjnSayumT-RDV3T4LqyXRiwVE1zaeD2jFfmBIfWneNPD1BQLDfGtPSqdPbcwIOItNo5XBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع بزرگ یافتن سایت های API رایگان
💥
🆓
💵
با پوینت های این سایت میتونید کلید های API خریداری کنید و یا کلید API خودتون رو به فروش بزارید ، همچنین میتونید Redeem Code برای انواع سایت ها خریداری کنید و کریدیت دریافت کنید
🔍
همچنین این سایت منبع بزرگی برای یافتن سایت های API رایگان هست
🎁
موقع ورود مقداری پوینت دریافت میکنید همچنين هر روز میتونید از بخش Daily check-in ده تا پوینت دریافت کنید
⚠️
🚨
نکته:
حتما با فیلترشکن وارد شید
🔗
لینک ثبت نام
🔗
بخش خرید و فروش کلید
🔗
بخش خرید Redeem Code
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/ArchiveTell/7455" target="_blank">📅 22:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7454">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iu_MOWzZd_0ICkKeb9D0_UyA4cnQ5-JWO_8gpHzCUFEuDhSkkBD2SPaTIPE4U3l7NtOWJYYG_tyyPMAi-SP5EBlTvYxEqDG3LaH-09ZLITZCdoGppFdBJenn_FG0K0iddlxa6OVA0nUG7DRZg6rbIb2HaIrB44aF3zHNTvFidjp_HxFCcJPhn6KClVhFuxcV-ZOaolt20GULc1rL3Kax8TyMaOKLpM_MKRLfxMeCjywtMxk1j8tGwMK5H8QQ9oC4e9I67pkYMk3opZtKwlv1jOBqY0uZyWBNJCo06JnOza6N4ioEv8Bt93aHTpXzNjQXpMyy-xHFQeUov8dhxVR4zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های هوش منصوعی قدرتمند
🚀
🆓
Opus 4.8 | GPT 5.6 sol
✅
وارد
این سایت
بشید و ثبت نام کنید
سپس به
این بخش
برید روی Upgrade کلیک کنید و پلن Enterprise رو انتخاب کنید و روی Start Trial بزنید تمام حالا به
این بخش
برید و در صفحه چت یه چیزی بنویسید و Let's Go رو بزنید
✅
پیشنهاد میشه که اپیکیشن Postman IDE رو دانلود کنید
‼️
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/ArchiveTell/7454" target="_blank">📅 20:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7453">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8cY1KH7BTG-Yjs32uB4xYkBRZTouyXku6ht00UA83nicYDsXODz9IPnPFBYLp7LyWE8Fd2KOyjQACOkeoM3pIEzD-NaZdOSG_N8AY6ZhWgIz1coqxyYi84r8zEyMBTRoZtWK5EZdvUbwwEi-gFnLUYwBgwH5_BvyrmSe-GM6DzvV1ahpHxK1tknoMXxlCfdjPIRb_FHlUlLqIwB3M_f_wICE8aI1cbNUlFB0aeXkaa8_1HxUkTcHsyPhoHqkbNZT2oCqCxx-9YJy9ZjU8mOkj8lsPR52QU3mj02iKuqik6_oCnev9XYFzE1c_xe3rZFwBtJxIjVjBpawgdqnvXxtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدیه ویژه برای شما
🎁
3 میلیون کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
dxai-sk-5feecf996d141afae9e16f8bc072d49a692312d7452a4043fd055c37aba2c8a9
🔺
Base URL:
https://airdropdxns.my.id/v1
🔺
Model ID:
grok-4.5
|
qwen3.8-max
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/ArchiveTell/7453" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7452">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">جزوه ساز پرومکس
❤️‍🔥
از این بعد لازم نیس سر کلاس چیزی بنویسی، فق کافیه فایل صوتی کلاسو بدی اینجا و  با کیفیت ترین جزوه ممکن رو تحویل بگیری!
📝
https://github.com/faithsaly5-stack/Study-Note-Maker
تست کنین نظرتونو بگین
❤️
⚡️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/ArchiveTell/7452" target="_blank">📅 22:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7450">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پایان دورانِ عذاب‌آور جزوه‌نویسی دستی!
✍️
یه متد خفن طراحی کردم که می‌تونه ساعت‌ها ویس و فایل صوتی رو به یه جزوه‌ی تمیز، مرتب و آماده‌ی خوندن (Study Note) تبدیل کنه.
✍️
فرض کن ۲۰ تا فایل صوتی داری (مثلاً ۱۲ ساعت ویسِ کلاس یا ویدیوی یوتیوب) که نه وقت می‌کنی همه‌شو گوش بدی، نه می‌تونی کلمه‌به‌کلمه بنویسی. با این روش،
بدون اینکه حتی یک نکته از قلم بیفته
، کل اون ۱۲ ساعت تبدیل میشه به یه جزوه‌ی شسته‌رفته!
🤩
فرقی نمی‌کنه دانشجو باشی و درگیر حجم سنگین درس‌های ارشد، یا دانش‌آموزی که وقت سرخاروندن نداره؛ این ترفند کلاً سیستم درس خوندنت رو عوض می‌کنه. کافیه صدای استاد رو سر کلاس ضبط کنی، بقیه‌ش با این متد!
🎙
دارم یکم دیگه روش کار می‌کنم که حسابی کامل بشه. اگه پایه‌اید و می‌خواید امشب تو کانال بذارمش، پست رو لایک کنید تا انرژی بگیرم.
☺️
✈️
ArchiveTell | S</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/ArchiveTell/7450" target="_blank">📅 18:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7449">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpbVVfbObMKdARnyDXNEVv5o_VQmniKujGjQqcFgo_9XZJVRxXBB4QIx8cAsh7it6AhqxGm7A61CR4KN2TpAdfHl3kthGfzmAZGf2xd1j5A76UcSWJTmacfpJZYjSdBROBQY9gmAuf0pj0_cKCCr3btiA8CcE5NSr75L8JxAt3btEHKaXRbln80klDlPgqb2IslS29jGpmUJQRBf97oD6ex7SwFhVHaC7yso_-ZVkXXxJpAmKjLDjc9eTIcBhbwUmEzxsVhGMLN6CT71bAxrDURBSy4TSRUO0lIYvloCRA5OiwdgKj-Ha37hMOJdtjcmVWBdm8f49R9Ux7Wpxx0hvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://tabitoken.com/v1
قابل استفاده در
Vega Agent
✅
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
120 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/ArchiveTell/7449" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7448">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRVQrYSKYJANMbXEnNiMe4m4tidoZuQ1eHrn-j1wOP-9ZYHpW7YTs3q3fYOtFDLbk_OXLO-PvTO-0IIOFswpiuzK2BVutLuF03WirVT4g5MosLsgjqOiRgWW1q5Ms4ccbZ2BIDdEzOAomjTYHMZO-aNJgE3mfiS6Ox8IutxuPJpE4647-txNSAb-HMdD-FusQip88vqlgCOqvdvnWtmyZS5ZgaT5hMp0-5-oZfOuvVDP8dAuj9N8kHfDI6KNoEU9LfjKeO94ygVSX5wtoQ-ulnLyao7OcL0Il91Jmf44m291UsaHIVD8iQk_UtnwUMgp-9bL835tnX9guiEp8R9qmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20
دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
GPT 5.6 sol | Mimo 2.5 pro | GLM 5.2 | Gemini 3.5 flash | Deepseek V4 Falsh | MiniMax M3
✅
برای فعال‌سازی فقط کافیه یک Gmail یا outlook داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://fapi.leileihog.top/v1
قابل استفاده در
Vega Agent
✅
🎁
با هر رفرال شما
10 دلار
و شخص دریافت کننده
20 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/ArchiveTell/7448" target="_blank">📅 18:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7447">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJ6soOWqAUbsshiDTn58pmJuCGvcXW8IUUrIL2yVbsrdXVIihAFspHj5NvSvUN8IZIACMEV8nmHt-i2CMyZ6AN9n635tOjfAFVIK2WZsgQsQn5HAlQd_9UySxoASLTwYXe8a9Q7jls7MlMnqxnTTwDMDVOrchYnVJhMErPPv_eC5Nr-WfvNK0SBa25AFd0mOWSk9-aJe9Cgjk4rOJMw52pUOC5MFfpHFHIGSQQCL2lnBQREH7Sk0bF7kg9wcOUoM2aTZZ9E9k3a62FoEXt39TyIaHQtpMSUg41ANX4wyAma66SU3O1wN6SDxOu9MTipB_yOBeM3xHrkHQCEQPzJsLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10 هزار کریدیت برای دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
GPT 5.6 sol | Opus 4.8 | Deepseek V4 Flash | Kimi k3 | GLM 5.2 | Sonnet 5 | Grok 4.3 | MiniMax M3 | Gpt image 2 | Seedance 2.0 fast
✅
قابل استفاده در
Vega Agent
✅
Base URL:
https://www.getunikey.ai/v1
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/ArchiveTell/7447" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7446">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2cMGicEWZWeR_V1cNr32oFDUh4-j7I3YBFK7aR0TrI3nWnh0a6omdpYtiBEo3v86paUCNsOtlPJzBUmYldDGwa7GKfqfZey9GUze2j-E1n_6dvGy3U2P0-Psm8sOoscA_vkfeRsMLngAu5xW5qbaTTf3gbQsElYFiFPbqd1pJU4TbwBByvAIVM-QTz8ZKmsjmBLOBhqR2-s7yF-ok-eMc5mHKOn-SBJFSvw8b3CXpSIpSLqbGHhM2DfbifHTc74_dWNhRz0MPoTRpAbF93g9ctFtqyEjUerD-c51jvpJ2tvws2HuVUp5IUmuTP5m3gcDIGrsv5ikIc5_BSOGizGpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان نامحدود به برترین مدل ها برای چت کردن
⚡️
🆓
با این سایت میتونید به 35 مدل هوش مصنوعی به صورت رایگان دسترسی پیدا کنید از جمله :
🚀
GPT 5.6 Terra pro | Grok 4.5 | Deepseek 4 pro | MiniMax M3 | Gemini 3.6
✅
🚨
توجه برخی مدل ها مانند GPT 5.6 از کریدیت شما کم میکنند ، این سایت هر ماه 3057 کریدیت به شما میدهد
💵
😎
🔗
لینک ثبت نام
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/ArchiveTell/7446" target="_blank">📅 13:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7445">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">💥
🍌
نانو بنانا پرو نابود شد!
کمپانی xAI مدل Imagine Image 2.0 را معرفی کرد که با قابلیت‌های خیره‌کننده، اینترنت را منفجر کرده است:
🚀
🎯
پیروی دقیق از پرامپت بدون افت کیفیت
✂️
ویرایش دقیق و حذف پس‌زمینه پیچیده با حفظ شفافیت
🔗
پشتیبانی از ۵ رفرنس به صورت همزمان
✍️
رندر بی‌نقص متن روی تصاویر
📈
آپدیت و اسکیل عالی تصاویر
این مدل قدرتمند هم‌اکنون در Grok در دسترس است!
🔥
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/ArchiveTell/7445" target="_blank">📅 20:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7444">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=HeKeCbbOBPs-UXe1F-Wx6gF8l_wqvEpqISZEe6txtn5_Y2x7HQqJga3GMj8GnEPymOJZNbBKoKZU_a59LbpxwAiVzgXMG2c94jwRhc9jnj73R35cY1sODdLvGa_dVPYdb4qLHpSJbur3avGQYjjH87XaZTNMjlygu9lcAqyhXXaDX3Nvu06r4gBd4_5TczyfMTchi0HlR1MxIrKulKmuHdDPeCgtWAZZMJNXRthCqbKvs8YixVA_jOrVV1nsJSWFcZwdkMwsCVLP3ecWR43aP2FKAfdCAUVABueTNLO7C_J3KJasqTkNsVszaKuLJ2v-ywDIWrRSC9C6D2eu0HwVTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=HeKeCbbOBPs-UXe1F-Wx6gF8l_wqvEpqISZEe6txtn5_Y2x7HQqJga3GMj8GnEPymOJZNbBKoKZU_a59LbpxwAiVzgXMG2c94jwRhc9jnj73R35cY1sODdLvGa_dVPYdb4qLHpSJbur3avGQYjjH87XaZTNMjlygu9lcAqyhXXaDX3Nvu06r4gBd4_5TczyfMTchi0HlR1MxIrKulKmuHdDPeCgtWAZZMJNXRthCqbKvs8YixVA_jOrVV1nsJSWFcZwdkMwsCVLP3ecWR43aP2FKAfdCAUVABueTNLO7C_J3KJasqTkNsVszaKuLJ2v-ywDIWrRSC9C6D2eu0HwVTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهندسی معکوس پروژه‌های گیت‌هاب با GitReverse
◀
☁️
بچه‌ها اگه یه پروژه خفن تو گیت‌هاب دیدید و خواستید دقیقاً همون رو با هوش مصنوعی (مثل Cursor یا Claude) از صفر کدنویسی کنید،
gitreverse
خوراکتونه!
🔺
چیکار می‌کنه؟
لینک پروژه رو بهش می‌دید، اونم کل فایل‌ها و ساختارش رو آنالیز می‌کنه و یه «پرامپت» جامع بهتون می‌ده. حالا کافیه این پرامپت رو به AI بدید تا کل پروژه رو براتون دوباره خلق کنه!
🔺
ویژگی‌ها:
پشتیبانی از مدل‌های مثل Grok-3، Gemini-2.5-Pro و GPT-5.4.
🐱
دانلود سورس‌کد از گیت‌هاب
🌐
سایت رسمی (نسخه آماده استفاده)
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/ArchiveTell/7444" target="_blank">📅 18:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7443">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فرار از زندان برای مدل های Sonnet 4.6 و Haiku 4.5
⚡️
💥
📣
🚨
حتما با اکانت فیک تست کنید
برای دریافت کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/ArchiveTell/7443" target="_blank">📅 17:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7442">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فرار از زندان قسمت 3 رو بزاریم؟
تو این قسمت Sonnet 4.6 و Haiku 4.5 از زندان فرار میکنن
😁</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/ArchiveTell/7442" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7441">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKpzeWbrRaA0wu7VDAwKVXFoSElhAAOLEAC-7gWKCCit1TlK6dnZXVpCGjCNWPc9iKWMsTblwEhz2s24e7iCWQ37Z_Kc7K4lUTXWC-Ts0wloJNXb6t-sWyALFV0a7lXVa_wAgMvAXIMIQ67yva6qdUg-ue3wrAwWQXsQTLKO0daf2qxp7QoMMC5ow1pqQ8zegEFJbjqwb3DQrOaO2tkusrdaTvUO6-6GIokIOL6hCOcQ2E5xlT7RkVQOkBcmqHBZAuROgWXBNCgMwwKLFDDjQJ1Hz8dvfXRZ7O0EM7WOk9M1oGo2ALgooNK66l8ZuEy6ee2bXefLtenANx_rkIZmoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
با این سایت میتونید 5 دلار اعتبار رایگان برای بهترین مدل ها دریافت کنید همچنین این سایت 3 مدل کاملا رایگان بهتون میده
💵
😎
Kimi K3 | Deepseek 4 Flash | Mimo 2.5
✅
Base URL:
https://tokenharbor.ai/v1
قابل استفاده در
Vega Agent
✅
با جیمیل وارد شید سپس لینک ارسال شده به جیمیل رو باز کنید و 5 دلار رو دریافت کنید همچنین تیک Free models enabled رو بزنید
✅
🔗
لینک ثبت‌نام
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/ArchiveTell/7441" target="_blank">📅 14:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7440">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فرار از زندان برای مدل های Gemini 3.5 و GLM 5.2
⚡️
💥
📣
🚨
حتما با اکانت فیک تست کنید
برای دریافت کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/ArchiveTell/7440" target="_blank">📅 22:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7439">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شرمنده دوستان
😢
بالا باشین
تا چندی بعد فرار از زندان flash و glm رو میذاریم
❤️‍🔥
بدون رفرال
🥹</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/ArchiveTell/7439" target="_blank">📅 22:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7432">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=DiNApqF_jluT-LXTfHYfGcjZy3f4vBNuqiiyvyVBaVs1zbxUSDsBUD73UksMVsbkJKeIiF8YF6gfsiEQdfksFesyBdK0hJso2DZqQTOFqfE089hVbEui9EsjPtMaNnRzJ64Up4_X0pBB2Vd6_Ho2VmlWldU8HoX619PfUEkVDB8L45pP0me0jbBEWs-36t0uLFm2-XwI88O9pJAaXBZCqZJfKSHlvg3pDIEwMZy4yGIFsuEgBcS0UTVum0PgTFMlH8NSz1ZPEQuMwO4jxIRNtAgn8jkeEu-ymYBIPuq0PTkY4sIo-kKaIcI23vrHUPKl-nqGzzP83E3rillIR7hs5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=DiNApqF_jluT-LXTfHYfGcjZy3f4vBNuqiiyvyVBaVs1zbxUSDsBUD73UksMVsbkJKeIiF8YF6gfsiEQdfksFesyBdK0hJso2DZqQTOFqfE089hVbEui9EsjPtMaNnRzJ64Up4_X0pBB2Vd6_Ho2VmlWldU8HoX619PfUEkVDB8L45pP0me0jbBEWs-36t0uLFm2-XwI88O9pJAaXBZCqZJfKSHlvg3pDIEwMZy4yGIFsuEgBcS0UTVum0PgTFMlH8NSz1ZPEQuMwO4jxIRNtAgn8jkeEu-ymYBIPuq0PTkY4sIo-kKaIcI23vrHUPKl-nqGzzP83E3rillIR7hs5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمدید فرصت ساخت ویدیوی رایگان با Gemini
♊️
🆓
بچه‌ها گوگل مهلت استفاده از ابزار خفن ویدیوساز Gemini Omni رو تمدید کرد!
جزئیات:
حالا تا
۱۱ آگوست ۲۰۲۶
فرصت دارید که
۱۰ تا ویدیو
رو کاملاً رایگان بسازید (قبلاً تا ۴ آگوست بود).
❓
چطوری؟
تو اپلیکیشن یا نسخه وب جمینای، برید تو منوی ابزارها (Tools) و گزینه «Create video» رو انتخاب کنید.
جا نمونید، برید تستش کنید ببینید چطوره!
😳
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/ArchiveTell/7432" target="_blank">📅 19:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7431">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENFSkfFYDGynERDm5WJU98scgnSSoitTAtxPC7mhPTNnWj3Xev_Os4hxdTK7j4SI2WbaTo_-zb400D8d5Bj4q4LpD_sME1jODJxX-kxl3KepJUoiyv53IfcaCynhmKFOG17xW7spDyUa5xAEjachAOvCODfNR1UxCCvylZX3fJkG-jUWCWddOCh1Sx_ABkCcrb8Dujq4wu6iR03v0vqja71DPgCPFGS_D6-yfDYLmxmWK1PMBqhFmhSAC757TFEG35aqTD0xQa3A2AHk6pt0c7LVKgMqe-DS7XSkpudn6zCIgIZ7hN6xYOkjM31ncSTWj9vPBtu4jzcrRRMsvESFBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن خفن و متن‌باز بدنسازی با openGym
💪
💪
اگه از اشتراک‌های پولی و تبلیغات اپ‌های ورزشی خسته شدید،
openGym
یه جایگزین رایگان و کاملاً شخصیه که دیتای شما رو تو سرورهای غریبه ذخیره نمی‌کنه!
📌
چرا باید نصبش کنید؟
💠
دیتابیس کامل:
بیش از ۱۳۰۰ حرکت ورزشی با انیمیشن آموزشی.
🗺️
نقشه عضلانی:
روی تصویر بدن نشون می‌ده این هفته کدوم عضلات رو بیشتر درگیر کردید.
✴️
پیشرفت هوشمند:
خودش حساب می‌کنه جلسه بعد باید چه وزنه‌ای بزنید.
👾
بدون نیاز به پسورد:
ورود امن با اثر انگشت یا چهره (Passkey).
📜
انتقال دیتا:
می‌تونید تاریخچه تمریناتتون رو از برنامه‌های Strong ،Hevy یا FitNotes بیارید اینجا.
✅
صفحه همیشه روشن:
موقع تمرین صفحه گوشی خاموش نمی‌شه تا راحت رکوردها رو ثبت کنید.
💡
نصب:
می‌تونید فایل APK رو دانلود و کاملاً
آفلاین
روی اندروید نصب کنید، یا با Docker روی سرور خودتون بالا بیارید تا بین همه دستگاه‌هاتون سینک بشه.
☁️
دانلود APK و آموزش نصب از گیت‌هاب
🌐
نسخه دموی آنلاین (برای تست محیط برنامه)
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/ArchiveTell/7431" target="_blank">📅 19:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7430">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GC7eA-o8KKwmZq2QmpXpRJkQZ-6iKijIWGl3pSMJS4cHxB_fleHjsFZ1ceLHah_4qJrqGK9WLEJbBPxISBRPpcm7uSazNExBb9l2VEv-CaVmBhOUDK-5VTmCa-5aZr1y-efRKVgcTszlLbPcr1fLjE1Ydw_OsIgHsfGgPYCd4GYyHdexFTGn-MtWnBOrnnCjPCX7kojIwKGrTx5bb7tHlSgeMOxIZE3yztyqymRl7fBB0EgltgKYRF-Q98nzq5U1y4TURlLsI5MOj7Peno4ol19gHU-3OTMnidgIK6ibz-ty8yNIj-wV_UIAniPrnjv-eJav8L41jpy0MbFIvaO7sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😺
چت متنی داخل ChatGPT نامحدود و رایگان شد.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7430" target="_blank">📅 18:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7429">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4tIuaKHIW9hMOX72JDh6xUpbj5UB2VIlnTKyMFifDjjqfTnxGjp1vycHpcymEs0VOYpkGse_ExAutT3-4gQmnDk4Q7hQbRPfWoslXghCrCQ0TjuzuLDbu6QdhDDDZ2bibM0LOoLz4RmEN7bJAKRLD-cluoQu3aO_zLr9Rg3PnrFXWWDgcdnno94INlZ50Vjenyfju6lWovGpq3Vu-SW8WYHVznxP1vgwSDgyzdDEMhdmmQwWc0FQIcVDHqOANSFJZd6PSOvgR9vNxyt6SBzVS-UqckFPsy_VPH_7wiTMhClHtb-MUrG3TbqjaI2qYFehE5lwIscrbUxq0K1RqUTHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
🆓
دسترسی رایگان 14 روزه به GPT 5.6 sol و Claude Sonnet 5
​سایت و ادیتور Zed اشتراک ۱۴ روزه Pro خودش رو به همراه ۲۰ دلار اعتبار رایگان ارائه میده که به ۱۶ مدل برتر هوش مصنوعی مخصوص کدنویسی دسترسی دارین.
💵
😎
​
📌
مراحل دریافت:
1️⃣
وارد این
سایت
بشید و پلن پرو رو پیدا کنید و تیک Free trial رو بزنید
2️⃣
استارت رو بزنید و با اکانت گیتهاب ( قدمت حداقل 30 روز ) لاگین کنید
3️⃣
از داشبورد برنامه Zed رو دانلود کنید ( برای اندروید در دسترس نیست ) و تمام!
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/ArchiveTell/7429" target="_blank">📅 15:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7428">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=kbrLraH_fgmhFU8PiRxO7Yvw71zTwCXDyuwz9FA1CaZqYo44TID6f1tLBMUjWn9iZeMIGKziiRJVJf7l9X0LmeaJD5vJkPgzDxNAS44fikn7PisMM4VtoW-JuP810YwSFA2qvtG3k_nvSelj2I4Z-UaHeJUinnvvHRX9nVu-1-RXaCjMBPIYE9ekKd0faRyqIONlQKy4pnmut2L_hOQ6mPdGtuHZjCa4bL6PJT5gGfb04ML3ceq4J6wTVQcHu78IWnsMDo6fR540x88y-CL2zCP9hzOMsiKkw_XScJGvZ8vBy8OjxbggOtC2fiS88I3In81gVmT3_0qGuetSpnI-sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=kbrLraH_fgmhFU8PiRxO7Yvw71zTwCXDyuwz9FA1CaZqYo44TID6f1tLBMUjWn9iZeMIGKziiRJVJf7l9X0LmeaJD5vJkPgzDxNAS44fikn7PisMM4VtoW-JuP810YwSFA2qvtG3k_nvSelj2I4Z-UaHeJUinnvvHRX9nVu-1-RXaCjMBPIYE9ekKd0faRyqIONlQKy4pnmut2L_hOQ6mPdGtuHZjCa4bL6PJT5gGfb04ML3ceq4J6wTVQcHu78IWnsMDo6fR540x88y-CL2zCP9hzOMsiKkw_XScJGvZ8vBy8OjxbggOtC2fiS88I3In81gVmT3_0qGuetSpnI-sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چت‌جی‌پی‌تی رسماً تبدیل به فتوشاپ شد!
🖌️
⚡
ادوبی یه پلاگین جدید منتشر کرده که ۷۵ تا از ابزارهای حرفه‌ای خودش مثل Photoshop، Premiere، Lightroom، Illustrator، Acrobat و InDesign رو مستقیم میاره داخل ChatGPT.
😺
🔥
کافیه توی تنظیمات چت‌جی‌پی‌تی پلاگین Adobe رو فعال کنید و با نوشتن Adobe@ توی چت، از تمام این ابزارها استفاده کنید.
✅
این قابلیت از امروز برای تمام کاربران در سراسر جهان فعال شده!
🌐
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/ArchiveTell/7428" target="_blank">📅 12:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7426">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-10aGHDHaB0iBVwGC1nPRRj6c0842wQVJsHlsJLXS6fdzZUb5atN97VAOJVJQtsHe5quH3fy_wXqDWP6O8Zy0xC9p0SXxrvcqz9FoIvDyYVY6cdk3-cbTMlJVRdAsjy-qLXt7WQNl0vCplf-_9mtMMJVFYfUlePiILqNW1xqztu-QU8e6nN0FLk3MOWyRcHsr_cPLzeGYb2QHm3QjkTtGNfhluORPhUoe23Sw3X_Kj1XkZamXSPkn8fu9SV-jgLRLUd7jdti3cElXePbddc54l3ZL_A-fE59RSvnQwoTXsts7_XO_yr8nvYH547Z34Ah70X42_ub3FPDbwBSP2hMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک ساز خفن گوگل
🆓
🎵
🩵
با این سایت میتونین با یه پرامپت موزیک و موزیک ویدئو های خفن بسازین و منتشر کنین.
با لینک زیر ثبت نام کنید و ۵۰۰ کردیت رایگان دریافت کنین:
🔗
FlowMusic
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7426" target="_blank">📅 00:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7424">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXv5vW4P_DhHp8JLbTeDcTGr1BhHD4c49Q2zcNms5_ssJYIPCPDhfqRccQBtMQOAXF_iaR2_lolfd3S2F7M9JcsN5NxNW2rEMmOz_NI8KcbPP-yW8Smojq7e1fACbDloapI0-w1kSmxO6262YUTWpO5C4ihZUphzEfCh8JdNwUn48rcguYrgvHkP6W1xwqv2S1kDq-TA5yYuqJ1UQ7UcWvZGLGxLPXMGbOhBFA5UgoYVWUL1BbbYfSBnI7hnU8Y4JpTeRBifvEYG2DaRnnQSSA4VHj4-eFRAaPqmd2Se5cMjTxL4VrOmHqaCxq6qHlPTsMlXe6f54EbhU2dY3XivKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1500 کریدیت برای دسترسی رایگان به برترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.5 | Sonnet 5 | Gemini 3.5 | Haiku 4.5 | Gemini 3.1 flash lite | Nano banana pro | Nano banana 2 | Nano banana 2 lite | Gemini Omni flash
✅
1500 کریدیت برابر با 15 دلار برای 7 روز
💵
🗓
برای دیدن آموزش کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/ArchiveTell/7424" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7423">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjTLvUheV0K0M1cr-0l9i2wWHFWrilphpN0jnwZqPxgkwHJzGwvtuB3o3lquE16R5SvJKaR9ajH0S3DNtRL2SABQgbg6YKAnun420iia-xmTwY-vjiyJYJc_sSj_OhDrgIOpR6f-1SG7Jl1JwJovwJg-oLD8YMoptXJeR6bbpVn0VVBSzbQ1WBIoT6lq2eR4bcFa-m2mPkMjjU-ASuCcQuDGFgiEwON8N6K3yx2dDPpafp-jTWktj6C4rtg61Wi9emSqkC9MI-X3RsKIhzwBCJJ8ci7nBxobIT0PUvnCFJpzvFUaoCsMtct3SGSQl8u3jkj7EGvwFxbIkVqoRiTsvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به Kimi K3 و Qwen 3.8 Max
❤️‍🔥
🆓
بدون نیاز به کارت اعتباری کافیه وارد
app.clusy.io
بشید، با ایمیل ثبت‌نام کنید و توی پروژه جدید مدل مورد نظرتون رو انتخاب و استفاده کنید.
😎
⭕️
فقط ۲ روز از این فرصت باقی مونده! به دلیل ترافیک بالا ممکن هست سرعت سایت کمی کند باشه
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/ArchiveTell/7423" target="_blank">📅 15:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7422">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTsRlB3QJSL3jYFPD8LfQBRCWD2j8fTATT5gWKFGKHdRJvfMfWJrqGc785INVguEuAaCz9K1rZwt6LljRsyqYRdF4hmx8GptfSVI5jK46FBs65PugjkvSJpRXyYZ0lydQq5_EfpvMp9wfYRnxi3rVbdFPHrOOV7Zbe04gzqSFefNCoqrMQ0hCMOiYGp8a6lPmQtizqhiYAcUxOWhlkxjMOnjLn8kzGdpNMWcb_09bhTp42TxTCMZ1JTmDaRBMjlu8uT5WVrIH8u4fHrglNBN8fhuPDXcz-BhKRwIJWeVK9OaSWO68Sa1BO2cZ943SLlK6uH1htoX6szkdYtMAqJwag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان:
امروز از ساعت 12:30 تا 20:30 به وقت ایران
⭕️
🛠️
مراحل راه‌اندازی سریع:
1️⃣
وارد
سایت
شده و با اکانت Google ورود کنید.
2️⃣
به بخش Account رفته و اکانت خودتون رو از طریق تلگرام فعال (Verify) کنید.
3️⃣
به بخش API Keys برید، یک کلید جدید بسازید و اون رو کپی کنید.
4️⃣
برنامه OpenCode (یا محیط دلخواهتون) رو باز کرده و اطلاعات زیر رو تنظیم کنید:
🔺
Base URL:
https://api.aigate.shop/v1
🔺
Model:
muse-spark-1.2
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/ArchiveTell/7422" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7421">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWBi8mnVNVitpfooFXMCw83nmDu4dJUDk3dFmnzhTAVFe5wgPZ61ZGo-9t_3Xb1LZF4d8vH_4eG651qxcQ83zE9UqZ8aTpT2wFC2ktiHKz7HTk6vk5dI9JSHF6dWAGnEtTLh0hl6uyGNPfPlEAcC9QNJEB4bB9lvj73OSobt4g5gnrcDNFhJReL4tnYLTInpNiGPjqP7-TeBcAgKtG2RoCog6Q39Z4E0YcU4xTgNRkCLCkkFe_O3a9k-cemi9FW3xWAxr9TlMH588Kmd4iUJC2ied-U7RaDlQ1j9S8JJdaJZKLBm85VwNk6MTalaiw9cWaFKNo2WjmU2NWgC9TCz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ‌سیک V4 Flash
به‌صورت
نامحدود
و
رایگان
تا
پایان
سال
6️⃣
2️⃣
0️⃣
2️⃣
به آدرس
cnb.cool
مراجعه کنید
➡️
هر
ریپازیتوری
که خواستین را باز کنید
➡️
عبارت
@codebuddy
را تایپ کنید
➡️
حالت
Work for me
را فعال کنید
➡️
تسک
مورد نظر را وارد کرده و اجرا کنید
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/ArchiveTell/7421" target="_blank">📅 13:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7420">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اگر دنبال کانفیگ میگردید و حال و حوصله گشتن ندارید یه بات پیدا کردم خوراک خودتون
😆
میتونید با رفرال جمع کردن ، گردونه چرخوندن و دیلی چک سابتون رو شارژ کنید
⚡️
🤖
@survpnbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7420" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7418">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftyPC3A6u3iH6PV8MyDZVOPJtBo6pNCU-irsQOQ2gH8H4jhvETReRUDr5QTku6iwNhqtpbEwz-prYSbhFlZO0xRQPoWhQ0o802Ua0MvBEkg5M8_8oNrQymrenc2T4yRkemokdpxZdY5dld-Vv5iRwfQ1ciHAUfUP_CrYJbjV019AsM4lf0YhLL3VP1R5nx4HwVq16Oi4vdwwfiKptWoTQ9OxUZ0ADRdF3YYpHJGPF2N54TxjDAlMDvAl-V-9AyHrDNAgs1HBOLr8h3ohtppsM1Ln8a7-d073qbACqkmRjqKiE8u-MxwDozSNS8ro7iL48wb2BnHfKLc00WCM0VhMuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کامنت یه کاربر زیر پست تلگرام در ایکس:
من آدرس مخفیگاه پاول دروف رو می‌خوام
😕
💯
اکانت رسمی تلگرام:
مخفیگاه رو که نمی‌دونم ولی من رو می‌تونی تو خونه پیش مامانت پیدا کنی!
🙈
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/ArchiveTell/7418" target="_blank">📅 00:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7417">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLSuDmkeCzbpkFD4uVHFbcswzQ9mYaPnMc4NMcy9MowgfarAeTwUnQebKkWk3u8ythS54LvHdAdrWTtJgNJyE1rYn-YIGmW-UWVwqXXa__nr5kRZmo0UlOPgCxL2vPFqv1m1V80p4QHRIv4W3BhdF4BlxKxYWuNjB6Qkz8Lzp4Vmfu1mQQmBOYCcn8eWd19ONa_YvJqJ-9hxJeEc-6Q31TCftatxPziD_38Xm23E87TT1d5ya35Ybx1GnqNS-83kOt1mjRGNWcxo0YD3rrF5FsLGfXzSqlagWdWCjKz5-s2Z9EUyhZCvnv0sxt_YiMqUOdPTU_pljEBiPs7qQG_LeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف فوری واترمارک تصاویر و ویدیوهای Gemini
🚀
🔥
دیگه نگران علامت روی عکس و ویدیوهای جمینای نباش؛ با این ابزار رایگان خیلی راحت حذفش کن
❌
😎
✨
ویژگی‌های کلیدی :
1️⃣
100% لوکال و حفظ کامل حریم خصوصی (بدون ارسال به سرور)
📶
💯
2️⃣
پشتیبانی از عکس و ویدیو با کیفیت های 720p و 1080p
🎞
3️⃣
کاملاً رایگان، سریع و بدون نیاز به نصب
🆓
⛓
لینک سایت
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/ArchiveTell/7417" target="_blank">📅 21:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7416">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtBECwjL32kUYYajn6OBjwgOp_RKk9YQ5fcZFCTddkur9AYBqDRHlWIhE6yv8x93w-BqVFzcI4jTEMJpJnt8EwDNAYTQOUGQwzWJR1G5rpuKjlyebzSt4Y5Qa4kN7m8Q46PgQN6dOIcy6jNmAkl4Sn34veQFkcD3KWA8FgpVCHxgHAYlh5LUFG1v1MeUtJLRO6oHieiMvFYCi6s2QBBWtymDnOJa39VYtg5YzpJ27ilatTyBp6fL5nKhdlT9wYSBiqGE5RGGheERoe5JpsdTKtIAW3ApQFuNOfm2S71iqPTnXyMRuHKzqNIGJNv6N2y5LvScvrQ55deZ5MMIKiqhnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت
Dola
مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت روزانه و رایگان
🔺
کیفیت و قدرت بالا در خلق ویدیو
🔺
استفاده آسان و آنلاین
🔗
لینک سایت
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7416" target="_blank">📅 20:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7415">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J18c2zSp521WUXm7_6ZoUVAPusgNgOipQzZuzJXpJVtnLZj-iXnRXKXCfmbT2qaDcwOsj5aOaNr4TZcJ97cwPwru8Dlwe9piLmSFOJziFs4eyTmlKiSbvaTdGOAv8W2wpZsrO0DgKoi-eV7ShPagLoc1ab5PauLNPq5EKIZQ_u-nzhRQ3efJw8JOdkDwOgDnbhkZOyH4t1048YVm4-Kpl4-CQ1tzcWUW-tmexQDF8ovq6CJDBMJlA9imh_5YLVVo-townUMxG_90IvEmBo3N72R1ua0eO4ANdJxn0txVvSx8V2h5GEB37Qqw3i1CtldV1apHRNu0DUTGUoDAPBQSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
گنجینه API‌ های رایگان هوش مصنوعی
🆓
یک مرجع کامل برای پیدا کردن API‌ های رایگان مدل‌های زبانی (LLM) بدون جستجوی طولانی
🔍
✨
🗂️
1️⃣
freellm.net
بیش از 424 مدل رایگان از +30 ارائه‌دهنده با اطلاعات کامل شامل محدودیت‌ها
📉
📊
2️⃣
freellm.sh
لیستی ساده و سریع از سرویس‌های رایگان با نمایش وضعیت و محدودیت هر API
⚡️
🚀
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7415" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
