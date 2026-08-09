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
<img src="https://cdn1.telesco.pe/file/qpbek3PrCLHOuq2AoGgFj8eBQSaSyIqLUM7I2NFtuYdfI8HNrqUQm2QTbApZkX4111HfJeaCqvso8h2J5Xtp7_7Fvs962QGaF4UF2SWKIFwBM5V0dGTEfUA7vMbiP79MIUz2UFwNx6-iqzGGxsutDmZnrwHsotEHvj5M0JFUiuc0x8DZWyUirq8Rnwut7xeHSSWuG-L6XxFuw9IdxvA0cLwopdhTJDPUf_tBWo5de1VK9vIaLzvXxD-e4mAlXiVkCwkgR48H95JmhoW7_m6R1A_BCVFcRPyTZpq_zCxkGWyN9323lpVJrU3WQhhjA33Wc-m7mkVOhlyGy94heawGng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 00:29:48</div>
<hr>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دو تا از دوستای خوبم امروز همراهم اومدن و اذیتشون کردم و کلی تجهیزات گرفتیم
🥰
🥰
به زودی خبرهای خوبی در راهه</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/MatinSenPaii/4879" target="_blank">📅 18:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔵
WhiteVPN Desktop — نسخه ۱.۰.۱۴
🔧
رفع اشکال آیکون نوار وظیفه (taskbar)
در نسخه‌های اخیر، منوی راست‌کلیک روی آیکون کار نمی‌کرد و امکان بستن برنامه از آنجا وجود نداشت — تنها راه، Task Manager بود.
مشکل از حلقه‌ای بود که پیام‌های آیکون را می‌خواند و روی رشتهٔ (thread) اشتباهی اجرا می‌شد.
اگر نسخهٔ ۱.۰.۱۲ یا ۱.۰.۱۳ را نصب کرده‌اید، این به‌روزرسانی را حتما داشته باشید
📥
دانلود:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.14
@whitedns</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/MatinSenPaii/4878" target="_blank">📅 08:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(Dᵢₐₙₐ🍓)</strong></div>
<div class="tg-text">📚
آموزش اسکن Resolver و استفاده در WhiteDNS (cottendns)
اگه دنبال یه Resolver مناسب و پایدار برای راه‌اندازی WhiteDNS هستی، توی این آموزش قدم‌به‌قدم نحوه اسکن و پیدا کردن IPهای مناسب با Clean IP Finder و استفاده از اون‌ها در CottonDNS رو توضیح دادیم.
⚡️
🔍
کاربردها:
• اسکن و پیدا کردن ریزالور های مناسب
• بررسی پایداری و سرعت Resolverها
• استفاده در WhiteDNS
• بهبود کیفیت و پایداری اتصال
📥
دانلود ابزارها:
🔹
Clean IP Finder v1.3.6
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/1.3.6
🔹
WhiteDNS v1.6.0
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚡️
ابزارها رو دانلود کن و طبق آموزش پیش برو.
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/MatinSenPaii/4877" target="_blank">📅 08:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
امروز اومدیم با یک
#آموزش
کوتاه از کلاینت/اپلیکیشن incy
🔥
داخل ویدیو به چه چیز هایی اشاره شده؟
. ایمپورت کردن کانفیگ ها
. وصل شدن اتوماتیک
. تغییر dns داخل اپلیکیشن
. تنظیمات مربوط به تست پینگ(مشکل پینگ فیک کانفیگ ها رو رفع میکنه)
. وصل شدن به پروکسی لوکال(باگ کانکتینگ تلگرام رفع میشه با این روش)
🔛
خلاصه:در قسمت dns از quad9 مقدار گفته شده استفاده کنید،تایم اوت کانفیگ رو بالای ۶ ثانیه بزارید در صورت باگ تلگرام از قسمت پروکسی استفاده کنید.
دانلود اپلیکیشن اندروید
دانلود اپلیکیشن ios
دانلود اپلیکیشن ویندوز
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/MatinSenPaii/4876" target="_blank">📅 19:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CsHl9MmIfWWzKh5DzbcSlHmnUFbadNRE6IuUx_LrcMDSNX5WXp9pNxDfkN6OnIYVQm_FvzLkkmxjeexhqOxWnxSdeSmZ9fceGlH2srgGhdzsSne7KIvPbkHtv_Cw3Wcdf7PuBVPUOtMhdwZpOXxoNFMXHG7oPw13zN0Fl4JUWjY2x29UrhoNhNt7ytsuz80lrGlgF7bdpfdmzLe7ZjgzlqmKDQvQSnD71McynPRClzvlPxidEFPfgoZ8n6SLzsFCvFhJGjfC7_f6c4nQHY7c0JF36iXv8yoUf_2N7QUym_GjMgh4fRdLq5Yzk0M1kSuvVul-X2MnDMoIh6l1fD7ukg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مغز دوم و هوشمند برای ایجنت‌های هوش مصنوعی؛ پروژه‌ی متن‌باز Synapse
🧠
حتماً دیدید هوش مصنوعی‌ها بعد از یه مدت حرفاتون رو فراموش می‌کنن یا اطلاعات قدیمی و جدید رو با هم قاطی می‌کنن. پروژه متن‌باز سیناپس، مثل یه سیستم‌عامل حافظه‌ی طولانی‌مدت عمل می‌کنه که روی دیتابیس محلی SQLite سیستم خودتون بالا میاد. این ابزار فکت‌های مکالمات شما رو استخراج می‌کنه و فکت‌های متغیر (مثل شغل یا محل زندگی) رو به شناسه‌های مشخص وصل می‌کنه تا با تغییر اون‌ها، مقادیر جدید بدون قاطی کردن جایگزین قبلی‌ها بشن. سیناپس اطلاعات قدیمی رو کمرنگ می‌کنه، تداخل‌ها رو رفع می‌کنه و به صورت خودکار مانع ذخیره پسوردها و توکن‌ها می‌شه
👍
این پروژه به صورت سرور MCP ارائه شده؛ یعنی می‌تونید اون رو مستقیم به ابزارهایی مثل Claude Code، ادیتور Zed یا Cursor وصل کنید تا یه حافظه واقعی و تحت کنترل خودتون داشته باشید. سیستم بازیابی حافظه‌ی ساینپس ترکیبی از سرچ معنایی، متنی و فاکتورهای زمانیه که همراه با هر حافظه، یه شاخص میزان اعتماد (Trust Qualifier) هم به ایجنت می‌ده تا بدونه اون فکت چقدر معتبره.
که به نظرم یکی از مهمترین قابلیت‌هاش هست.
با سیناپس، ایجنت هوش مصنوعی شما به مرور زمان با بازخوردهاتون هوشمندتر می‌شه و تمام داده‌ها هم کاملاً آفلاین دست خودتون باقی می‌مونه
✌️
🔗
لینک ریپوزیتوری پروژه:
https://github.com/Danialsamadi/synapse
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/4875" target="_blank">📅 18:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P-Wn3-MeiDX8hrj5RE_W-ZnV-iEmFQf9Ns5wozyOgXuIsvuQbSBa8dqlmQrSW5bpUeJYt-oN7Pgap2mubUEBCd4LnJfj23-OV_0FOdipa0ElX2PYsRwL8_Dda_4TiBe4HhbqCcXvkABvuoPX6Eygm6BS3eN3LqKRdx-Y0zCHxRSwsj_8IyDwd03s4N63cYkvloFTFJ7EqhTMmmkJv6SRH2A3vBKywEkzLBWsa1L4kB3bJmdMWp1DEUAPXatG5zmF03t8ehQv7p4j0DS0FqAMlJyYtRjaXd41q7nZdTwQ-JmQfqTUjR9scVH_vub4pfvgB6KR1ONXaA1bRLMrnTLrgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاملا درسته این صحبت.
به محتوای ویدئو کاری ندارم، اما خندیدن به اینکه "آموزش «چگونه وایرال بشیم» خودش 60 تا دونه ویو خورده، هر هر" قطعا از کوته‌نظریه
و صحبت این دوستمون کاملا درسته.
اون شخص داره این ویدئو رو برای یه دسته‌ی بسیار کوچیکی درست می‌کنه، و کد تقلب نیست که بگی نگاه کن خودش نتونسته:)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4874" target="_blank">📅 11:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نسخه‌ی جدید Grok-Build هم اومده که زیاد چیز خاصی اضافه نشده، همون بهش نپردازیم بهتره فعلا</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4873" target="_blank">📅 23:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jzZV0rN7RL9-q0RcIJkNFnWdun0i_teODKWZWTUlpWzt36jNwB7U6aA-7FWTaVaeTl3Lgg2InXKacIMQaAARzPG9hpC6X9L7EK57p4jMFeqZ_JKH5J19v4johp3Bs3bnjI98SLuB8MGqqUlk7-NObt-DEk4GURwo2Qa9CNVvblCkhHfcRhp4NBDohDtAXMHzYT8K31Z3OV3TYDsMKABXCteJ-gN7jy4cpGivnyNfXpGs2dOW7YsXEfii9yT7tQr2hWIQ5FofERHT5gRYCjLqB8YCy3VQskn4Akx-9PrgLB50OH_1bigcL3sP_ZUM2U7evu967-GZmMEfFY5AD4Vvpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GNhh7BADWmSVi80hDS6CqMShrC309uA-fN5iASv81aQANrZIezwyfjwvxl-CU-ctNZpX9bx11BeQwDuNqskMNboB724D78uTqOIdvhsEAae5uZCjE3RHZzdxF7sxKS_OM4tKD7rkqb4-MxS7M1OP2KhQ2Dbuq9EmM12jSQBc7Y9uNIMFr-KaHOlH6e7ZvUYV8OFVtTWQUL5pQVWag1exnEuvvdrtr7i22zalQy2N8m7lkGFvgtqffoatNoL4JRCaO7Q5aQGn1iaQrL57kXmalWC6W6K5oNZEzoDiZOvRZ4VYglrmpCWKu26wwGkv7AREY_fqbkTnTmWeiIgFFuFdYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دسترسی رایگان 14 روزه به تمام مدل های zed code
ادیتور Zed اشتراک ۱۴ روزه Pro خودش رو به همراه ۲۰ دلار اعتبار رایگان ارائه میده!
​مراحل دریافت: وارد سایت بشید تیک Free trial پلن پرو رو بزنید
zed.dev/pricing
با اکانت گیتهاب ( قدمت حداقل 30 روز ) لاگین کنید
✍️
CypherDeveloper</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4871" target="_blank">📅 23:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یه مدل‌های خفنی در راهن که باید وقت کنم بشینم راجبشون بنویسم</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4870" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انقدر اخبار جدید از AI میاد زود زود که به قول یکی از بچه‌های توییتر نیاز به گزارشگر فوتبال داریم دیگه تولید محتوا کافی نیست</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4869" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4868">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KjU10Wsi30ephFX5XNBW87IneOyb2V8-G7ruEngACun7slCXzfuDiDaj6EArW8-TBHMcq4UCZWNEb9ZiXt-zgjXHqJPXufwOUT5fDUnKrF49wSIamSiun3KHInazHG0jz7GcB0G4cp35vNnMF22XKEoAnbgFEUz8wFqCRMba4Kl5cDOAGDhoGaJW1KQi5-0pwd9pbdQltOkGDGq4W_80ZwtCohz9S-OOxPy2DLY2OpewnAfsbJf-t4eKyLLS2_DbJoYkb0gDUZKPgEaltGKWPMCao6H7ICScTVfG0L8OobhhJ4hqkBIIjWw5vbQFqUdxqxgZDrr6NtrPztoI4_bucQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین اپلیکیشنی که برای نوشتن چیز میزایی که توی ذهنم میان استفاده کردم، TickTick هست. ساده، راحت، بین گوشی و سیستم هم سینک میشه می‌تونید توی گوشی به عنوان ویجت هم اد کنید. خیلی هم سبکه در عین مدرن بودن و چشم‌نواز بودن طراحیش، هیچ چیز غیرضروری‌ای نداره. پلن رایگانش هم از کافی، یه چیزی اونور تره</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4868" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4867">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مارک زاکرچیزبرگر هم muse coder داده که تستش میکنم. سرگیجه گرفتیم از بس بین ایجنتا چرخیدیم.
اما جدی مدل‌هاش قیمتشون عالیه اگه بنچمارکا درست باشن</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4867" target="_blank">📅 05:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4866" target="_blank">📅 05:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4865">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=hG9gTA_lIK-_jTMeqlfozOyyIiB65ci7I0GlgpABNzP0bOQg_dWiTrNyeZgjY2wlOHd5mG816r0mhH3BUT3GMlZxkob6ql-9zdv8ngtYLEvJDGVwncw06wRQhRkRfJwOsuWRx5YUaOoYgSo-1DsMLAFfbRKRhAhR7ZypAMNwwh4lIoOFU1U7reaaWEJzt4J6iR391We4O_PA-GqaiZfR7PUhu6MCDbP88o4FsnvkV0qDuEev9V3CESVO-91MAITTPIXwwRC_IfdoM-8gA70l1UiEyagfEL7YftV0oU2F4EdLFkvFAyLJCtiWLUN5GMiAssN_zbInW1EacOk7HqTglA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=hG9gTA_lIK-_jTMeqlfozOyyIiB65ci7I0GlgpABNzP0bOQg_dWiTrNyeZgjY2wlOHd5mG816r0mhH3BUT3GMlZxkob6ql-9zdv8ngtYLEvJDGVwncw06wRQhRkRfJwOsuWRx5YUaOoYgSo-1DsMLAFfbRKRhAhR7ZypAMNwwh4lIoOFU1U7reaaWEJzt4J6iR391We4O_PA-GqaiZfR7PUhu6MCDbP88o4FsnvkV0qDuEev9V3CESVO-91MAITTPIXwwRC_IfdoM-8gA70l1UiEyagfEL7YftV0oU2F4EdLFkvFAyLJCtiWLUN5GMiAssN_zbInW1EacOk7HqTglA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4865" target="_blank">📅 01:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4864">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یکی از دوستام برای رفع لیمیت اوپن کد روی 9Router، حذف و نصبش می‌کنه و درست می‌شه.
به زودی واسش یه اسکریپت می‌نویسیم که این مشکل حل بشه</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4864" target="_blank">📅 19:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4863">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=gN608jQ2No9MyGtbdheCfL8UUY70cigfNoN44aMH3deuGkyVH6Kk30KC4qxgDn2CKfOwV2bbj5JgOPGuhUqvrV4_LyMFYCML0i2edaZnnIOABJhUIcNHrBtiBlCge9C3G9dIm_hNltlP8o824TTwHuN554lKnOQfVedQYuuJXwfO3EYQPnNlTpeFXReGM8jLs5D0d_lpHcnFPIJeLE_1GySUoCWcJf1smKzcBA5wyOzc6IX_wQvy8I-RztJFiTVeEbGxnz0A1aImEEqNHKT7la-6tKNZy5NXRjnk6cHzp0V1N2WfHOAmdiO3-wDwEjgwR6_LHqhu_GRXmyF-9_USXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=gN608jQ2No9MyGtbdheCfL8UUY70cigfNoN44aMH3deuGkyVH6Kk30KC4qxgDn2CKfOwV2bbj5JgOPGuhUqvrV4_LyMFYCML0i2edaZnnIOABJhUIcNHrBtiBlCge9C3G9dIm_hNltlP8o824TTwHuN554lKnOQfVedQYuuJXwfO3EYQPnNlTpeFXReGM8jLs5D0d_lpHcnFPIJeLE_1GySUoCWcJf1smKzcBA5wyOzc6IX_wQvy8I-RztJFiTVeEbGxnz0A1aImEEqNHKT7la-6tKNZy5NXRjnk6cHzp0V1N2WfHOAmdiO3-wDwEjgwR6_LHqhu_GRXmyF-9_USXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4863" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4862">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cji6ASGwUA6Au5bl1nCHgx8sUSn4m6q8z-Pt--dciBLOmoyhW2jtwN1G0WKng1fooqWjPiKK9q6lawwWh1kcmgQ3IPKJlKxzcTu9QNoyYdSjT0_uXUnEmz4PnirkRv8X4y4_vmE81ghGuqw09SS9BQnNanZ2CSS_ebDDjI392F4hIuOo1_2zsI1f_T3oYu6yk1xUxyIpPX3Vmb50bnt-jC_GA0Gc8VcPP4CqWl1jMOXwOwcLriDy6flySEXNsN1Bqikp7u4iot9SM7xlaVbJgnkAn6O3GIMKiG_XI2XFgapV9Hh74za940XHzKXyi0JswORb_wD4Yq9j2Pixy_yzvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه جوری ما رو دعوت کرده به سان فرانسیسکو، انگار حالا ما میریم
😏
😏</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4862" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4861">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">Matin SenPai
pinned «
خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید: https://t.me/Editor_MatinSenPai شرایط کامل توضیح داده شده
❤️
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4861" target="_blank">📅 21:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اگر وسط آپدیت کرش کرد، یک بار دیگه باید re-deploy کنید</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4860" target="_blank">📅 19:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4859" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4858">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">«بعدش هم روشن شو»</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4858" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oZQPZ2u8T5eaWVtmuHu1VvwTRkqHivHdmW8jtZvrzUxD9R1T5Adhz5UcuWyXAGrS1ssCP7_8_DoRNso1cb08qW0PrTOBcPEW1_vf0EMyOdLsjbiec1RUNbiCZSSPEW4dmHHGHzRppBdUfsdpuZ-S147WD6VcNQpIs0xdFC3ZCS8ggC8BHT4QDkyUSFqiKHTa8l83FjlHsqnufU9uucHxzGWWJ2BRWebTB0AgSwSZChci8lFki6_vAAkP0jXPHaRljZTw5ooh1RLsq1BsvGIvgTC7jkvA6-YPtXJaf0n-ij4Vi9XQDtEYT3ylVCP4pD_CemPIwNYuzKDio6Vvt3o8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TTAb6mmvm9LPKRt1-rXZ7ZfjsKW6taPNgEpIHwlui8EFjOOy2ygGC3Ae87N001vCn_7D03VGszZjItL_obmTG3PLesfTY6uEI8mCFSqoWY4lOXPDZzcHuQc3ZFgotnA43UBvIn4mSZkiZFQ055G5V_5_GdVxwVNBxA9W5ig6Q3zy2JW_7v7GPd7Mi5Afmd-7WmN294bslDS0Kj6a-9a3PCWAGdMDS8RUKmqFDBqjcFOv6XPsUSG31VFp5V5Rfu79pUbyuYsRxoPHQDoXOQosDUnprufg736bp9SZpUgUGeNlJM_q9D796VG05IyPEb6xD1OMbN0PTUBmVLj8hHNhxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متین الان که هرمس اپدیت داده
چطوری ربات تلگرامیشو اپدیت کنیم رو railway؟</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4856" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4855">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cg4pOX-9NmK_CT_M2qh7hlihz86CvipeAwZwmq5veku_ieD0QA7xBxvkUu9D_AGsoh1utxRPCd26tEiM9YMDZYEF85E05DB7InN-PIdyJm-NO1eEjMTVOi648al0rG6i17xZxIT437DzAsVBD7Cv5lNBy-QgpRBD4-YP4GQpzZUiAQe__a8sP-3qfzAwM08sb7ThG7rz6wFQlIGKL_Jq-R3YYU-pfviHFhT286dgsl2SF_aLsWF2_NDqktMHpCIlQR1huFF1G_fI_tvdJTsFFPoIvW7-t17S3QWmMdggGT8pbvXURMYUEF6NahOPrdQjmeYS_HRT6ehHuuDg0qzRBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ Hermes، ایجنتِ دوست‌داشتنی ما، نسخه v0.20.0 منتشر شد!
📊
این نسخه که بهش "The Herald Release" می‌گن، کلی قابلیت باحال مثل ارتباط صوتی زنده، سرچ با منبع معتبر، وب‌هووک، اتصال ایجنت به ایجنت و بهبودهای شدید پرفورمنسی داره
🩰
تغییرات و ویژگی‌های اصلی این آپدیت:
1- گفتگوی صوتی زنده (Talk to Hermes): پشتیبانی از استریم صوتی زنده با قابلیت قطع کردن حرف ایجنت (Interruption) و کلیدواژه‌ای که باهاش بیدار میشه (Wake-phrase).
🎙
2- منابع و استنادات دقیق (Cited sources): توی کارهای پژوهشی تمام ادعاها رو با منابع واقعی و مستندات و سیستم راستی‌آزمایی (Fact-check) لینک می‌کنه.
📚
3- وب‌هووک‌های خروجی (Outbound webhooks): فرستادن اطلاعات و رویدادهای چرخه‌ی حیات ایجنت به HTTP Endpoint‌های خودتون به صورت امضا شده و امن.
🔗
4- ارتباط ایجنت به ایجنت (Agent to agent): پشتیبانی از پلاگین R2A v1.0 برای شناسایی و واگذاری کارها بین ایجنت‌های مختلف.
🤖
5- سرعت به‌شدت بالاتر (Faster everywhere): سرعت لود اولین توکن (First-token) تا ۸۰٪ کاهش پیدا کرده و پرفورمنس اپ دسکتاپ به ۶۰ فریم رسیده.
⚡️
6- پلتفرم دسکتاپ: قابلیت پیش‌نمایش زنده آرتیفکت‌ها، کیت توسعه پلاگین (Plugin SDK) به همراه تسک‌بورد Kanban و پنجره دسترسی سریع به دسکتاپ اضافه شدن.
💻
7- تاییدهای هوشمند (Smart approvals): پیشنهاد تایید دستورات ترمینال بر اساس تاریخچه استفاده و قطع‌کننده هوشمند برای لوپ‌های ریجکت شدن متوالی.
🛡
8- قدرت‌نمایی در CLI: اضافه شدن ابزارهای اسکن پروژه، مهاجرت ساده و اجرای مستقیم کدهای شل.
🛠
9- هدایت بهتر ایجنت وسط اجرای کار: قابلیت اصلاح مسیر و دادن دستور به ایجنت وسط کار بدون اینکه پیشرفت قبلیش خراب بشه. نسخه‌ی قدرتمندتر Steer که داشتیمش
🧭
10- ابزارهای خودترمیم: توانایی خواندن خروجی‌های نصفه‌کاره ترمینال، تشخیص خودکار خطاها و بالا رفتن محدودیت تعداد تلاش‌ها.
🧹
11- اتصالات جدید: هماهنگی کامل با پلتفرم‌ها و مدل‌های خفن جدید مثل Buzz, GPT-5.6, Claude Opus 5, Gemini 3.1 Pro, Grok-4.5 و  Vercel AI Gateway و رفع باگ‌هایی که داشتن
12- قابلیت‌های جانبی: پسورد Vault داخلی، فشرده‌سازی خودکار سشن‌ها، لوکال عربی، فایروال و مقاوم‌سازی امنیتی روی ویندوز اضافه شدن
🌐
این دستور رو توی ترمینال بزنید، آپدیت میشه:
hermes update
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4855" target="_blank">📅 18:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4854">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کانفیگای کلودفلر من هر 5-6 دقیقه، 1 دقیقه قطع می‌شن نمی‌دونم چرا</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4854" target="_blank">📅 17:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4853">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">راستی این ویس با میکروفون گوشی ضبط شده و با هوش مصنوعی رایگان Enhance شده و به زودی AI اش رو بهتون معرفی می‌کنم
🥰
https://t.me/Editor_MatinSenPai/3</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4853" target="_blank">📅 16:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4852">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید:
https://t.me/Editor_MatinSenPai
شرایط کامل توضیح داده شده
❤️</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4852" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4851">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qf9RCVSJpLYbP4IHPl_NlsjgL1CG_d--4KeSGF-f2jVuN8NtiJCOwhtY1mdtxmNBMvcw2MA52VD829H8ErVfw2al_T2IhLkxDL8i4wDGIpkoD_KTsCK8P6N44y5l0W4KbmyQfM4Q1VA5LSihhHl7DUxTyjy3simqTmcOPkSOXDDlHtoX9YGki86RCuLdVEmjjTHYFk0gmj4IctNudqn3zszFWVkbct5RWhL6unI6A6XAiNJSR8a6ONlBOtRzJm2wuC7qie_N6LGyk0uS5H0UFe2hf7yUZXMY841ID1cs6dCmxHKAI8ar_uZJhVo5_xHHwarfOSZ3WiY8P-nB0c4kKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این اپ INCY که امیرپارسا بهم معرفی کرد خیلی خوبه
دم برادران روس گرم</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4851" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4850">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست  https://t.me/RasadAIOfficial و برای خودم هم جالبه کلا به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4850" target="_blank">📅 16:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4849">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست
https://t.me/RasadAIOfficial
و برای خودم هم جالبه کلا
به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4849" target="_blank">📅 16:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4846">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q2a0F1gZPGVf3V1iR_eP3XXH-2oGXkdBm6lisDJuPVg0yqeu9kdhBZVtVkq8NMN4PSEXr-f_kQmyk6h_dsJyiWbuAJYls6CXyvmjZbmEqsNZP_4QSpF69QIA77IPBzd_PG6F0MNA803IEhO1HvWn5Nvos4MwGy1VRqDOVNv943NcHW40EhazDCM-ydLAe9urtCHjINV-DSjECRRA3DSuCq8gM3vtLZNk2vcmAVQfVt2KHFUAqFZBQqmqY8fv3QrLENXjr-jNnDKIXpvwLKhe0wrFmShofqRnDAvKfUFPTQviZNsTVFP8Oo16aJ8QBe8vk89_Qkd7ROAUFdCfeCROOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xw6KGXeXqDKtykKOLSX5Fm6WxzNmK0VQAfetmmJONsmAcJ10XKTpsUhIV6dFkhjWg9AfKuANxjroXU7CyoLXYmyujmrkWie6giw-CxWYPhevwgLgGUrhCEHniDuFYB5UQQWfvWcrbEct_SOCUZewxybatyqr99I1h8Wr3C9oQR5cfkOzaqyc0QDBxE_C5hZiyT1xRMZqyGm63GwkXhwQ6wc_XavexI2i_5FyKkuWw8XTmU_WSFWt93TkXCqm3eCrTgjk8rvPiqjxcsLf957EItIAJ09eN1iU9vwlz73aY_z4naPHdSf09AXYrHiQJx0UOmub-Q7VcfsMk7-itMPXiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qEfIILNahg4hI_wFh7-vmZD1mBGFmgowd9_H2DEcY0FyKgxV1N_E-6tNKxzDnr1UZsIGrIrdQNN21h1x_NnvM_zaZXbJsl3G7O3uwNu9a_9n33GTE7yUaVB9FwBfflCZePXTMyUWXwD5gVw-HSaKjBb70cIVyxJ9Nz5mp2RXJFehGclXW_wtwvtB-_pdM_fgWaUmfEkHMUcE3UCZT0MF3U_mDOX69S2lYxFTdy6IsGDu_5Hpzy9yuk8hYBhYYLLlLPd07uY8yfHtDRtbEOwEdFiw80t4Hsx2KF92yEotKFTAo-fLOXN-17svtl7n_aJj4MmDkmi_BtGtp4FM7AQe6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظرم برای رفع دائمی مشکل هرمس با Antigravity یا مدلهای دیگه، از اونجایی که گوگل داره به پرامپت اولیه سرک می‌کشه، بهتره ما هم هوشمندانه عمل کنیم.
وقتی متن خاص اول رو تشخیص داده، متن خاص دوم رو هم تشخیص میده اگه هممون همون یه کار رو انجام بدیم.
پس چیکار کردم؟
این پرامپت رو نوشتم و بهش دادم:
توی
soul.md
هسته‌ات، برو و تمام چیزی که نوشته شده رو به یه لحن دیگه متفاوت باز نویسی کن. محتوا همون باشه، اما کلمات و چینششون تغییر کنه
و بوم! جمنای دوباره فعال شد روی آنتی گرویتی</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4846" target="_blank">📅 08:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4845">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انگار نتیجه‌ی کارآگاه بازیا درست بود این هم راه حل آنتی گرویتی روی هرمس، با تشکر از سهیل و Moh جان: https://x.com/i/status/2084572159016382738</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4845" target="_blank">📅 08:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4844">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XUHZv9jb6KcxpL_hBwxCkbzk8O-B6g-oSDOtfbX6h_V1k64_kU77y4JtbmCWp2xN3lP92zUvfI-MYwSe6XUIcrrWlNxmeHUMrXyix54dB11T3HOLqPPtPjRZ1MibFnzQNVviTopS9V4ZAsZA3KcOm68FD9gYe0mc18bno0z6gbUkUmEwscCTM76_Erj34TQMmj0Xu_4S63we9qns4H9Y_Ma2rBBlTdS_yLtOAvzY-cNY1TSunqUo9Eqz5sEF-sgRxC6swM0Xd1mPfK39QAqYcsQZfk0ejedx9oGZVWEZpHMK407fEF6K4hkK4AZPHCeWJTuBtB0ZlDGi4ljFHgA42w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم مسئله از خود پرامپت سیستمی هرمسه چون درجا ارور نمیده قشنگ ۱۰ ثانیه طول میکشه. میره فکر می‌کنه و برمیگرده</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4844" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4843">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fFnz67xjTjh3fd3ruaACr5kPu1knTphTGabUsqRCkAeHu0YtRkOa-duZSnSBrAa11R-S5r0KKj-wIThLJVO_bRD1nu-eDgeXPJlDtEYQKT0hQYRhjFH3Cts45-rHNIytWlRLgEEjtLO0sffQSnM_iReYt8By71qQAwkyxbBJAMMXs2Ex2_5L5nBK5izadGL52CiyTC6x0SBxx4lpAUijaD6C-B76S5IzB43Ql8_8J3o3skWxy0bfrpicd0xWuGKX3VAtBE10kgULjlRSMX4xdxNggMIFUzfVB92N8lnhiPcbh5NkAknJ8VGbqAZRBbAP2u7FExGRobQe3ydydT-YRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلا درخواست‌هایی که "Hermes" توش باشه رو رد میکنه</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4843" target="_blank">📅 07:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4842">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router جالبه که روی هرمس هست فقط جای دیگه ازش استفاده میکنم مشکلی نداره در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4842" target="_blank">📅 07:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4841">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pqZembV9rzbB5L0Z5IVaYYopjWkOhCoEJrqUOfostomcpcuMW-nrefqgW5ZEjUu9AfG9XORPUSVifv9vRjqy0l4UD8-nKVu7OxUqPlU5rSjTFiH8qKVqBAv5Ghc6QGVsDFkcGkUyWR4BNlaTmriufgDLLiS1KoQktmyshiPHR2QiiUn-ZzmGr5Aam93KhX8bnSjOItswH9fDtp5WiaOBzu2brfJdMXom8o6IF7GJaK2o58ew7FQ8i7ypfWh80GKVJW2Rs1OEooonr9VRJqbG-CdgZbXIpREcbIuDqCTQuLRUblLxWgk8icSwYDZNY3ffm3oKKmROpXB0VzBxZEfkQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router
جالبه که روی هرمس هست فقط
جای دیگه ازش استفاده میکنم مشکلی نداره
در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4841" target="_blank">📅 03:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4840">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AmfUpuNmmIof-H_b_gUMxXkzQaFepEunti3MMjTPKDA7KEj8zFSE42_ASVuLqEuPxBLpdUeiZI9DpFmgn8sExNg_SzhJTuxRA_5S8zp6XFG2NWS_ob0qQSoiFOqhtoFFcKNZu64UeMv0Vl0dKtI3drAgk91CwRMk5d7qepDB4LP_94ZcNVFt6aNmVFqEdOrfUrJTZr1q-xFApBdbEb6m6rHfwteQFmk_LGpnG0SXcwywoUYd3ENl6LT1pyrfbvvpP-Wlsfx9RDrmlFPz8QljhH8sytf0kMDj_olzmq9SFbh7aS2K604d03X4h7_UYLXL7PSPHEE1rEYxzJ2XPBKq1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچها اگه از pomodorus استفاده میکنید</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4840" target="_blank">📅 00:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4839">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رفقا ما داشتیم خریدهامون رو به دانش‌آموزهای بی‌بضاعت سیستان‌وبلوچستانی تحویل میدادیم که یکی از همکارامون گفت یه خانواده‌ای هستن که چند ماهه وضعیت خیلی خطرناک و بدی دارن.
بهشون سر زدیم، دیدیم کولرشون چندماهه که سوخته و شبا موقع خواب میرن تو حیاط و پشت‌بام می‌خوابن، اواخر هم فهمیدیم بخاطر گرمای زیاد، یخچالشون هم خراب شده. بیشتر پیگیری کردیم فهمیدیم خیلی وقته که وضعیتشون این‌شکلیه و کسی بهشون توجه نکرده.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4839" target="_blank">📅 00:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4838">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">به زودی قراره یه چالش(چالش هم نه) ادیت بذارم، و ادیتور بگیرم
خوشحال میشم که اگر دوست داشتید، داخلش شرکت کنید
اطلاعات لازم رو می‌ذارم تا فردا</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4838" target="_blank">📅 00:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4836">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CUBy-1z7eO8hZjy6dz-qQVdyIuZhx8vHFv6XfC9h7fyyjpnYN29x5mbNd6PimGG_mjCz3WZL6Q4qqKVQOoHYsjFk81gmvhCd9CgPQmzACPzXvjIwVFNuhSl27j9R_q0sDWNPp_0rEflqKoz7nhH83my_uB03QyMBvoXAZG5DjLoezOBk0i0XBeCxUfsm2c4xpN4BV_05RPgegAmk9JZp50Kqd6neE0fZG0bEE6QEU2p42VUwIc_lqRmd2fqkEMqlR_7mKvcIcpMTh7eZ1xaVeBQUUg3IZ7KlVHRinOIII06wSTtkktAIrrREMs8ujJREZldXikOkdWgV3Fpyc7TbVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از چیزایی که راجب کامیونیتی فارسی باحاله و دوست دارم، اینه که زیاد توی کامنت‌ها با هم در ارتباطیم. کامیونیتی خارجی، این شکلیه که ویدئوی تکنیکال می‌ذارن، 60 کا ویو میخوره اما کلا 25 تا کامنت میگیره. یوتوبره اون 25 تا کامنت رو حتی لایک هم نمیکنه. اما کامیونیتی…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4836" target="_blank">📅 21:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4835">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tCqijeJEYpQhRkRhyiy1Je1HJhM62sjFBlMlJnXdNHpc92wVzcqgaQP5SYbibXssAj_Rx0sn5dE7n5Q9rD6yoNORCsTTjt_q2VpeHrkeVUlzv2AHDF_NxbEQOz6xkBwVR0NSbjH2mdXadD6WO7LRXTPIo-ajULhHeKnTzKhKCyHaFS-okRqxbIsznDRv7edRmnpTP24qWmGHbKcDS080gmX4Y7_BgKLdvtGmnY_d1xVLvey5ecxpTy7our2RHHiMQArdtenqekY4_a4TpQN_MLSmsbVu7pMhiBNnXo3-MjJzaNfvIiZpIVskEC0FakWPGyPg1xeWHaKXBiIJYflXLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایگزین متن باز Fonto، رایگان، تحت وب
دیگه برای استوریاتون پول اشتراک ندید
😁
و اگر دوست داشتید، از بالا(علامت قلب) به سازنده دونیت کنید تا لایسنس تجاری بخره و فونت‌های خفن‌تر واستون بذاره.
لینک پروژه:
https://github.com/FontWoW/FontWoW.github.io
لینک سایت:
https://fontwow.github.io</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/4835" target="_blank">📅 20:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4834">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">و به هیچ وجه، به هیچ وجه روی کانفیگ VPS نذارید.
فقط روی ورکر و کانفیگای رایگان
چون به سرعت از طرف دیتاسنتر ابیوز می‌خورید</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4834" target="_blank">📅 19:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4832">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Frq2gydEL4hrD7J_np37VK7I4FIFgw7sAHZWX-YOINbS9DYHu9dkFc__CfiAP9iPcGI7kGe3XfPQnjHCR8Er6QKnslAVxK6HvIrhvvxZwtF7HhGJeQbNjlZITN1tiAt-Z6dn9TUBe-DdkcLNpvIX5mRi6E5hIELE35i8RnSzwFf96mbHJX0t0pJSHnmn1H8PrUeqnlnOa6wtUjoLvNkMrMP32pg8qzEoGksytLETZErMbHsE-Sqj4pw32d926ol5StSKpOoWq9011mMQr_xIJ2CgrOvMYJQw2RezX5VwDC2qCdJnZQ-zISxqUISSS902o78MSU-LZOIKfVQWv28bjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VdvEmUxNUo8RDlzz2nvp5pAjc2zKmiIrgg5HBqLAaSMJHX-3uBqk8NrGufSmLWA2DGjtjMxvYuqR8n_FLT2bobbzAYzO-z3tcRO3yq27dRdsWDClaLDv9JBXeJQEdD7mCF72LjYv-IuUtJDrVNMxnVdew6MDmplxtRC4HMGtsT3cvUftawaQe29a5p7p2kFbWrGXlmNk8fKh3xSkG4gmXW5wyOUPBLOoa-UKppi1BJ-339zFA8ulc8yYbTBlsTtX547y_Nqamk3F9yriKjad9OQDkeirvjoHfWmnvFrFY46JTQ0zy7asWi0SckB5NXGfMY4WB-Xd9mrfj5l0o950Bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4832" target="_blank">📅 19:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4831">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PJSK-vsMiKxcZQ22mQX-ZGTkUZtjqKBXbc1PQijmK9P3eIO4mRbjs92-UlcgOPPz0C0er0fimdVWhZmeEXPm3DRfiVXuHjyWGk2ETBJs0-9dG1h_MNfNEs2tLm6jNMy2VQNAA5Y9hNCHobZfbVsQoVg80xLtB0jdzZUKGryk8lmINmrx4OTXw9iDsAbTQMVx_TmAuS6KLlIj-IJc9R6UR_LSzn1DAXWk_sWz7kkaqw24mG6-vYrRQk9qKTo9kwNQy-LfJ3dZGHXdcl9l0t447LnZKnY6rnXHRJYodZ3aN9yTcAuQmY78sgCAbKNHIDrge7aIF-6d7h7Jgf230agV4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید: https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4831" target="_blank">📅 18:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4830">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید:
https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4830" target="_blank">📅 18:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4829">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خیلیا ایمیل دادن پرسیدن با چه شرکتی کار کنیم
ببینید شرکت‌های ایرانی همشون یه افتضاحی به بار آوردن. یا چنل پروندن یا..
من هم شرکتی که واقعا کارش درست باشه نمیشناسم. ولی خب متأسفانه وقتی مجبور باشیم، چه میشه کرد
الان خدا رو شکر دوستم واسم نقد میکنه از خارج از کشور و میفرسته و دمش گرم</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4829" target="_blank">📅 18:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4827">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OEkpE9jgRks-yeR9w1Z1QEPG6q4uKOam4jfggUCa4mefw50wsgfzKx8gForbYzJHBc6Csq5pgywilEzQReqCo2NRVXpM6vylGqXkGkNKio6ldHS2UEX4apvkkntcKfXRsGxf5FmZhnErOynd5FqO6fYqsDMLxoSP2C9Uq3mEb8mSuF9Ra1qRBI-RZ9U9dUIFh87UPMQST5xrdlQxPMHXrTFs-77Za9Kt6-JzaPm1jvZSBUtRQjiwbUHQ-86WHmgFBr7pxDKzYTUuRL0-g4Ei6mMRTHvgbWIrYXbVTiUsBYyyB4Tm8HCvX8zgVizBmGCfzXH0YusWML6mFCvRQ6nLMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u7nvPxICTgeAR5cmaNWZjKS8tP8yfI8Dzo2Sv4vjdYgdTuDmtfuQPBDwnJ7z1S0VLaa_PK9p2G67WOdI1Czwv5CTqSV1Ktxh5lPrem0QJFW7c9c0tsY1hxOsDTmfrSwPXnJWTjIxyLpju3pt8yp8Y9J0pKzTpDgnMzUdOk2A0k7Dbz1A_Qk6vWPoyY6ohgBlYzc8NrHP3OeNDxCYSqEFFHQvXmd0fESXG7IPhDT6QOaBi1VgpStkPwrmtDXNg0sxkAImmbrfK4qkoeSG-HfTkjG3VRmIVpJGlL3OckK6i6zhG4eo_R0kk5ztmpTRFHyeJcAYbm49LZCzLicvsvH_XQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادش به خیر. زمانی که من یه میلیون تومن هم برام نجات دهنده بود، یوبر این شکلی جوابمو داد و هنوز هم اون سه تومن مال 7 ماه پیش اونجاست:)
تازه اونم با قانونی که یهویی گذاشتن.
همون روز ادسنسم رو قطع کردم و کلا حسابشونو از اکانتم حذف کردم.
هیچوقت با همچین شرکت‌هایی کار نکنید</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4827" target="_blank">📅 16:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4826">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPavel Durov(Pavel Durov)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBGUmd_gBZuy0Dy1G6SigHwA9vdg7FfHMjIaN388JURkzwDcI3a45kB7GBHYriAnljHnBUpCUD-RWZg78fWM7GuFIIDFyHGg7DJKvaMBXpXXlZfkt3rOeNZGN7icltEEogFl1FnCGyUxg1eSVJTmvGu4vRf0SRFxNSsza0wfI0lufUd7wL_L0ANd0i93tvsmOr2t3cR10v6etxfuRP0j12wSuAnAy9m0zzDoR0DlpXFFhPxcxiI1xGVQzH6EVAZ2aUZA3_PYtBuSySgi4N15889la1p6XMg9tf49gEsjhGaq6ha8I_JzYoM5BN6pT3kFIvz-NNTLAYacqQvo-XBm2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
The 2026 International Olympiad in
Artificial Intelligence
starts today.
As a token of support for those who will reinvent our civilization, we'll issue
🏆
240
exclusive
Intelligence Cups
to the winners.
💵
We guarantee minimum buyback prices ($
1,000
per
Gold Cup
, etc.), but the cups' limited supply may make them worth much more on the secondary market.
Good luck, AI coders!
🍀</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4826" target="_blank">📅 15:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4825">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vtps0aKqKdbd51v5GKGqLbaj6NatafpBuW_AXi-pJ3pvuAMU6bdwCdySfK_HGYX99_Kb3Wh6w0Yg_Ij9kBMMwfMCBFtWpTakgRdPCcAYsQkEDawni6Jbn7CCCvgwlNLGJwx2PrguGKx38ELtRlagfaOlAyLejAgE1XQlbVPCEJQ-QkOF_j5rme6PeROBddUHj78HwVWi_n7hB4rfZgSrUDY4WRNJBPPPN8ymFkBxu92k4iCcGZ0W-qgD1vrRQJfLmJU5uafeDPdm_z4fmSXOt6MWafC-0DCVInu3A6DgGh_y-2ocFltlSu0vSrFPsIaBAXNVl4nyBusxd_pDONailg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی گوشی VPN دارید، دیگر لازم نیست برای لپ‌تاپ هم VPN جداگانه تهیه یا تنظیم کنید.
ریپو
Relay
یک ابزاریه که با اسکن یک QR Code، اینترنت گوشی به همراه VPN فعال روی آن را به‌سرعت روی ویندوز به اشتراک می‌گذارد.
اگر زیاد بین گوشی و لپ‌تاپ جابه‌جا می‌شوید یا نمی‌خواهید روی ویندوز VPN جداگانه تنظیم کنید، این پروژه می‌تواند گزینه‌ی کاربردی‌ باشد.
https://github.com/Mahdi-mortazavi/relay
⁠
@RepoFA</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4825" target="_blank">📅 15:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4824">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CNx2GOg7qeCif-f9BOjgyRWfllXzjbI7TYu2oxRdkXW0py2YXyTdV9Wnd-4tfNEfrOllNZSm5j3Fx7Y5-p-NQZLe5ZnQADbcGO-JE4GxIZPviNCmKacQrdqJc1Ycu3WBULHLYQFKirhnEkNvymYNVSPBjjGB_-jpJW9rl61lLbr0qNPgeXCNrw3NGYDJHRuH965l-YZQQonaAModIkDZLtxf-dKfJYRzvTAaFQHSc_iJGb5WFEXscpmw7vQcJNNVxJ_rL4vosutVPKV2pBnV1ShLKu6hVJygMXSK1l1ly-BB8KnI91dxw7YrIcxtRFN5cyPgyl8KsDw5DKcn-CmNkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقااا من رندوم برداشتم از گوگل
برای این ویدئو
اصلا هیچی از F1 نمیدونم
😂
😂</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4824" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4823">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=j22yu2srkU2lub30Po4a5a1CNJ8fUEBpT0ksqFj9mDGaoIzjdia4oGASZ38H9a6mq_ToFZHUhovm-7uBNf1RkUY9YS7Q46vVnjBalDGYUck8RJKQCsvH-SWAX_sAkuUeANH7YXiwV3EZNCHs_uFN9x_-L66AOUKk4Dgmk6k3UWl10YSPRwSosAEq6lOn0CDiWlHiqhGweLPo7da5AJ-z_udwMyknrnj1_CTF27T4zzyOmhsB-RNbwUhX5gnIPhyNLnQFkcWz_77sZNhgRsEuie9D1TmlwXoQ-mCObWSpbfJ6duUQXO9iKGzTgomHhpllUsCMnJEVG15ZwVtjQTNFqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=j22yu2srkU2lub30Po4a5a1CNJ8fUEBpT0ksqFj9mDGaoIzjdia4oGASZ38H9a6mq_ToFZHUhovm-7uBNf1RkUY9YS7Q46vVnjBalDGYUck8RJKQCsvH-SWAX_sAkuUeANH7YXiwV3EZNCHs_uFN9x_-L66AOUKk4Dgmk6k3UWl10YSPRwSosAEq6lOn0CDiWlHiqhGweLPo7da5AJ-z_udwMyknrnj1_CTF27T4zzyOmhsB-RNbwUhX5gnIPhyNLnQFkcWz_77sZNhgRsEuie9D1TmlwXoQ-mCObWSpbfJ6duUQXO9iKGzTgomHhpllUsCMnJEVG15ZwVtjQTNFqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
درود به همه رفقا...
آموزش
سا
خت کانفیگ Amnezia VPN(وارپ)
• صبرکنید ای پی ها رو لود کنه
• بعد یکی انتخاب کنید
• تیک فعال سازی پارامترهای امنزیا 1.5 حتما بزنید
• بزنید روی ساخت کانفیگ Amneziawg
• دانلود کنید وارد کنید داخل Amnezia VPN
• میتونیدم کانفیگو کپی کنید + بزنید بعد insert بزنید کانفیگ اضافه بشه
💡
نکته:روی تمام اپراتور ها متصله هست.
لینک ابزار(ساخت کانفیگ):
👇
https://darknessshade.github.io/Amnezia-VPN-Config/
دانلود اپلیکیشن ios
دانلود اپلیکیشن اندروید
@xsfilterrnet
👑
@ConfigWireguard
✅</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4823" target="_blank">📅 08:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4822">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sIpDqIB2YxhrHmzictEsIxUMsJHbId4iW5f4E7ZdHvayb9e44FiE_bUhlUHIrJx1IWnYLOZZVZuv4qOTgLk0vulpIfwonfKnWoTASHg9Vxqo0BBy9KlG0PA694vz0XZc3T1tjngFAa5D5JVJbnenRp1aFIMWZRMdnMZGV4MTYSQHQWbvpCjMfMmDkRxvyT7bgDWZL7OY_mT38ijghJ1wnB7R3A1-RMa2vYAL52lb30o-BDwFojjL1TPXq04neUZBjuYf9LGEYP4SD8vlnERlG0imJmB5gNoa0eqydSTeeNSCDwpgkce9jxuI0Hzs5jFa0VnZ3ovCL1M5wQ1C6LeVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4822" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4821">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fFjBKgLHLYR3P79psAnuxR_p9ELUcFHDYq82TLvQn38WxzWi6ufRmNIUlJZVwrEdOTVIEW7hcbOQV6qp9iWSnGkTgfFbWD76eC3qgB2owdASWfe_6i-6Vyn6Uq32J04ZCbdgmlOeXEbXiq0lXu74vqCk7bEE-5agxuti6MAKR13vvTrCjQ2yYdrtcIHGr71YP_fS-2hps0TZsaIC5Jg_exht_ad42fvk-viBhqgkX8lRjGCkRuiWFC57dgwL-rYLdvk7DqSOJzE8wOVsD3unazeXsrdUBIfRUKpuP4IQKhWrzaExl0ACU882bGWwJ1GtEYal1c1-kMXi3kBhtUdpwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)
بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.
مهم‌ترین تغییرات:
🖥
یک GUI کامل دسکتاپ برای Windows، Linux و macOS
📱
اندروید از نو بازطراحی شده؛ Kotlin + Jetpack Compose + Material 3، پشتیبانی از اندروید 7 به بالا، APK جدا برای ARM64/ARM32/Universal
⚡️
دیگه لازم نیست منتظر پایان اسکن بمونید — هر وقت IP سبز کافی پیدا شد، متوقفش کنید و فقط از همون‌ها تست سرعت بگیرید!
📋
امکان کپی نتایج (همه IPهای سبز، ۲۰ تای برتر یا یک endpoint خاص) حتی وقتی اسکن هنوز در حال اجراست
🔎
اسکن همسایه (Neighbor Scan) دیگه اختیاریه و به‌صورت پیش‌فرض خاموشه
🌐
تشخیص ISP و ASN چندمرحله‌ای با چند منبع (Cloudflare، IPWhois، IPinfo، Team Cymru + دیتابیس داخلی رنج‌های ایران)
🛡
اعتبارسنجی واقعی کانفیگ‌ها با هسته Xray؛ پشتیبانی از VLESS، Trojan و VMess
📦
خروجی مستقیم به IP:Port خام، Share URL، Base64 Subscription، Sing-box JSON و Clash YAML
🧠
موتور اسکن بهتر: الگوریتم weighted-random برای رنج‌های Cloudflare، جلوگیری از IP تکراری، پشتیبانی چندپورتی، خواندن ورودی از IP/CSV/CIDR
جزئیات کامل و دانلود:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.0.0</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4821" target="_blank">📅 02:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4820">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hallelujah</div>
  <div class="tg-doc-extra">Leonard Cohen</div>
</div>
<a href="https://t.me/MatinSenPaii/4820" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">00:21</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4820" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4819">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه. همینطور قابلیت ip fronting هم داره و سرعتش…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4819" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4818">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⛏
۲ نکته برای بهبود سرعت WhiteVPN
۱. بعد از اتصال روی دکم
ه اتصال مجدد
کلیک کنید تا به سرور جدید وصل بشید.
۲. همچنین میتونید به صورت دستی تمام سرور هارو پینگ بگیرید و به بهترین سور به انتخاب خودتون وصل بشید.
آموزش تصویری</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4818" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4813">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.6 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4813" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4813" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4812">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqfYiIrCqAioZrZsbxcO3esfbpuAo7_4CB6vTsvb7sQznB0S35M7Gku6kXCnFj0IcOEnz0L_GR1YOCg81n-bS4Y5wha-0K763q8e20j7ztKybWJbjq3049YGdoAl2rgsohjz3vh1K_RHe5Pd-t85YUqUNPowH_dIH1CGp5zy64VkidKLAohvMHFCFkNZfvUe-li8lRdGnrDigkJHy__w1rJkuhVmwqcfom6EwiDDcKWzGElccJPuBEuU-X0H9gTJ9F8js43mQ2jCILVG5yYvnkI44tukT87dsx0dtoGeUiald-jTdpbFzHseZw6skOWnPW8rRHNRb-UcvvEv7MWYsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
تمرکز این نسخه فقط روی اتصال
سریع‌تر و پایدارتر بوده است.
امکانات و بهبودهای جدید:
•  شروع اتصال سریع‌تر
•  انتخاب هوشمند بهترین سرور
•  جابه‌جایی خودکار در صورت اختلال سرور
•  کاهش خطا و نیاز به چندبار زدن دکمه اتصال
•  بهبود Real Delay Test
•  رفع مشکل متوقف‌شدن اتصال در مرحله شروع
هیچ تنظیم خاصی لازم نیست؛ فقط برنامه را به‌روزرسانی کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4812" target="_blank">📅 11:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4811">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PiCR5er1ZmJBxLeOy89ADYi_-jI62y8MRxeQ3TLZibIoIy1IKsANnnELK-T44MwZ9KmujCcE_O-gU2GdwDRsPNvggDhHwEM12dEAhSFACd8XmqFNP9rPj2ILPOW_kPBB6ik--rzOEk0NpyQA4wARnZGKOznZjtuhC2W6O8gMoJW74B3k_sEM2BxF9pn3Z4lf7vXVB6F4th63av3XWV6PGmPS0gl7H15Fghr5c_elEZCL9rZ6q8wIOFf_GoM8JI5V5EZMHx2lU8124-u6cjfKULsGOsdxDmOx7N6-ZFvlHIFsIX8VvE4RqXF-2yCLRXOP2sWgM8KAVK3-pemGXvzTDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه پرومو رایگانش تموم شد:)</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4811" target="_blank">📅 10:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4810">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YB63srwPCUXrSttwfrM1CXXV5c5aD9WRKPVGe-a_8G2nqL2CQXTjJ847WffWEYG8hutvvW51Cj8Zbr4v8QRNSPevXiMQI9M3A1JsC3d8PKvxbaSgRm0ur-8VmhXDcTDFMCSSB7dXSXE3bxNzuM3vAo4XOZFh2C_1ZWx6vjEsMWF3DAqHTaIG1SPRjnv8QOt20a5BUZbyWbeEid3529vGSM1zmlOiuUvZ4v7ZNMLsdgeJn_s7ED3-LHlg26mG0PFrzoNshPzs6fPxOH_HkYBBfCVggQuO70z_ic1RqM2uTjUCyuMfPusYvNpgKJKqhWFaksyPI9xtE27wA3aayN_QJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان بیشتر مدل‌های دنیا وارد «منطقه کشتار DeepSeek» شدن.
یعنی مدل‌هایی که توانایی‌شون کمتره و قیمت‌شون بالاست، دیگه رقابت سختی دارن و ممکنه کم‌کم کنار برن.
✍️
Ali</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4810" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4809">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4809" target="_blank">📅 06:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4808">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سرعت آپلودش هم عالیه.
قابلیت‌هایی توش پیاده‌سازی شده که از همیشه استیبل‌تر بشه</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4808" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4806">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LGkexTIBcCAFcbxzugTmyZouXhf_finCpAJlhoZHfseAbWpei68-mLwzQ-NmFW1GzGxRL4oiE2z4DG0s9QW89iXK43NGrir4_BrI3df8UAdtJ4ElidKdx2DicJ0vNDH9BrY0qnjrVwVNOf0Uzk_r0xPmUjJLLZnnb7FZcnzHwn_tASASfMeHD4l6M78-WJbZOGEC9VvwyveoJbUc-JELBwlFUnnbrGqxA8VBlCwMPAqHBCXxkZE_ic65DXNo00ITSm0ZcFBgVhdWa6v9y3O4S64ajSy_VaMMjRYzkRx1SAPknF9lx5DGr0LRBfayU12nweRJg50OPg2LQRx2zh22zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aNS7sMem0hqJ0jSluywrMwcVizaB9AptDHgJAd7itNVtLZ3lV0-jCv94WnUreu4l8EuhJGUjgDlahwrY0bndxkuruwoLcowLe9hHyR9OQhh4auXLSXnxp5nWf-6Qrh-soDSspqw324PTRqyci5VhYxl2APQYKnuKZzrDdgyUL-t8lo3Mo6B0KTR7WbqOZipGKs-AF8Rqwt66zgU8WYNEMzEYSe7W5kjKfqw2atEXBnIaf4PcflxNYxCXe76sSen1ANM65xu54-kiLpmEXNFEyWPORld4i9KOihAoaqmnlmVoRWMnK8Ff4xHXv6cnC2HNCJne8Idiac9dS0C0Os3fUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون
اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه.
همینطور قابلیت ip fronting هم داره
و سرعتش عالیه(حداکثر سرعتی که اینترنتم میده)
دم بچه‌های WhiteDNS گرم واقعا
❤️
🔥</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4806" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4805">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دقیقا این اتفاق برای منم افتاده بود و سه ساعت داشتم میگشتم ببینم کجا پروکسی روشنه که بدون وی‌پی‌ان داره آلمان نشون میده
🫩
🫩
روانیمون کردن</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4805" target="_blank">📅 05:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4804">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Qwen-3.8-preview.html</div>
  <div class="tg-doc-extra">44.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایلی که الان با Qwen رایگان ساختم</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4804" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4803">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Kimi-K3.html</div>
  <div class="tg-doc-extra">41.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4803" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل 4 میلیونی‌ای که توی ویدئو ساختم</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4803" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4802">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4802" target="_blank">📅 04:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4800">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nlphJeN3xO-osl9NPmVELbkNGZIoBUGqEe7BYV6bwjpy7nilVZI5gMARep8ycThRvCOM-_se25vlxrTo9OslehI70cL28WAOcRr73Bop2pL4RSHTl4qsD6pu7slUA7qgVZbsrUc935DCGk6Fwl2LV5eMXKQ2_WlYMJKLdKK4ZXF9RxreQuic0oX7O3qQ9rxrW0Lv55gKfuevHx-J4s7kksoCfzErUiu_dKwTMLXjeVS7lQJVK3Tv89iRhUgXjcFTTXtFqK6DjYDKZmurI1uWKujky_TSXWXanI8dMS0uKiaPIsMA-8tciAvJpMOx0QoMlvT4G9q269wU30f2T--Fmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TsZ6hVaKwyDUzJWOhAkIslJlDpcMwiIrEJ5FUHmoss0gIrAtXdvoEx7DzlrKGcv6hXrnrjBCy35YM0b0lG2X4WslGxCTXhl2y0L5Dy97UU4XxdPV8IgNefjMVY6EYtTGtm0i8Rx9dBpxcFY_i3wA8MT0yiZmzkW34PDxk05tgR8K4kpNw9hF2bzdvaUM_HEBuevIEd29ddzqC21Rl--_dQrQKu1lZ63qiPNUbq7bHlkK9tLYEYEXrz89IIgE_3KFG7p8UiPTnJGRen_vmXaizDvREx-BAyOFDMNxa_gB67b_c__OseLc4cgeeQKiPC_705-bf0pDuF2PgZNLbrbtVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4800" target="_blank">📅 04:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4799">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ebbyixeyl-ZJxEs8ud9hqF-V59vVXddUscax4Ut7n2enU6mLt0g1RRJnF4GcmYhCwpXFueodQ6-y_gtd5SpcfaEa7QJSc9n0htzdOz4rXRZPeCkpec3MabSXcskGkAkXTwRQNL0SB_qMI95uRrfJWCYme3Ho-yslNlTtsyC6_qGX1v5HkJk4FRTUAL9SDZi5Tf5xn-7KtniI6tGKbOk0Qvb83wQx5Y8NfXTrvNQ5hq1cXWJDLNR-F08R7dC7MCezgt7U9HuUhsxcGtV7c8wu_RcRTdhbsfcCd-SJzU0jEaKkGUcdBndnO8bp2a-lHs8VDbQpCOcuz1oZKFTRet6UFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان توی
infron.ai
میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.
ممنون از confesious عزیز بابت معرفی.
فعلا دارم باهاش کار میکنم ببینم چه شکلیه
تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4799" target="_blank">📅 03:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4798">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4798" target="_blank">📅 02:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4797">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت
تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4797" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4796">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-poll">
<h4>📊 از گوشه کنار زیاد میشنوم اینترنت دچار اختلال شده. مال شما چطوره؟</h4>
<ul>
<li>✓ به زور به تلگرام وصلم⚠️</li>
<li>✓ اینترنتم کند تر شده🔴</li>
<li>✓ فرقی نکرده✅</li>
<li>✓ ایران نیستم👌دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4796" target="_blank">📅 01:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4795">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خدا رو شکر توی قطعی نت دستاوردهای بزرگی داشتیم و اپراتورها از وی‌پی‌ان فروش‌ها ضریب دادن رو یاد گرفتن
😑</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4795" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4794">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ggu06VLhNxQnIQ9smkAYk7BJxo8pVWHnKG1OHCR23x7UrnIgqb6wx7g9dubmjeqIvcWCOKabXVBfkmDuApigpQ63Xg2Tft_eb3KJWRxi2RDpx9mXg_KXhWz3SOPwl4VtmXCR9TNpWCObYdNM33U3cyTxq-LGtSQkCOLnr42XLXDR_GnQU5oru1dOMJbZ7OUraJaSBdlyLZ_MGbYmsapaiy2vhB9-uFbFo6WebXNa13tL2owCGu4xVTpUFJo4xqIWCL0-rL7TIuLNlmbnrR1mtA2HoQkBUDcQhU2natfRlUZMFHl52hbftoftOyGGiLHZUixBQT5BuAT8bNMCFP6Q2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4794" target="_blank">📅 00:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4793">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4793" target="_blank">📅 00:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4792">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgX8yt1mH0KmOSitMbDYvfbav0AYHu1rtN2MqxRGhXlHL9sxbMGQi8DkfsiB2yZuUr4RuIM24FXBJNLY_wdhUr6RJYZJyarb_kDuVehhZ62Qdqb5hAUdPEi5q26fZ5P2z_NjcMCiWuHgo6n7q267v8bPxzn1upcsHcc9Xb2lmqEx3nlOKx3whqdbfHNuW59SNOsuTFhQqxHqJlstbR0zPCE32LiZsaiFCeOUmBAlHEGgUvdw0ek9Faq02_e23IksNzMyR4ZDCdCT3kRTU39ZbMii4lD7skQbqXN89YPAPcWg0NQP7TogZviKkko3OzndoSW9EgCQPDEW6h4wy_zqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4792" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4791">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">به نظرم یه تماس بگیریم باهاشون</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4791" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4790">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج 205.252.xxx.xxx داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4790" target="_blank">📅 00:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4788">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AwsLUVhJP__QvQ02yev1BAzVl3JdoRd08lSNw7UQ5tsA6eDvgkGH0Kwfjbz6Uyo-igHTaK1HGz2NM8bAkeAYMikdQSJ1WPMpjuo5s9M2NHejJFJBRzK3NkTDA8EDiAO0phSGpUOVBxXTo3jZo0Q4aKWmY4b1Bk8MYacp2u_qrs2FdQ2Cw_bgASewKncJ0bWpkhCWT6aQpfRT5HiJjfFFBwDp-ekeyv3gWWIswfad6s2GUfrdMJO5h3DDJuf5HI6gyfc4bQecizvmP0n6R-Y35daywnLYFkK9-1rNyzb2hfhAYPi734SG7Eli0YeGnLoFS87bNz4H84e8icIoyp4pHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbywRCnhP0wrfJmp9K1S9f90IPjumsoBNqHM3IUtLJmSd-7r311fGMDtzk-qEgJujVQh6j_PGspg9BBcPCW8p-zxnYOrKzNunfzZqocxAmjfTcBY7Wd6A_8mVGqcKmr1g7tW8j0NDKPnbW229uj2OQczp3BzLLekfMU7tlCK1NTSGc6_DhwZZ4_N17ecvFmaCjvmOISANaH0O2Eh9ub2TsHEt5xnW2MeoTO9qwGJbjIUlw5YhgibelH6S4zVhoqsQMxYakyZvDpcbKk9f7SqLO-zscdaFBfhTwuZH6cCZL7nQ6I68iDrzKUgme0s4ifmNEWWsW59o3T-7UEKQoYQXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج
205.252.xxx.xxx
داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل قبل محدوده 80 90 بود الان 140 160 ، درنهایت این وضعیت nat کردن اینترنت در ایران داره به یک روال عادی تبدیل میشه که جای تاسف دارد</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4788" target="_blank">📅 00:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4787">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OLuVuDIfrl8dtzOWkU-9WXDlE6mTs7RtkVVxVvJzKWxdWmUL6bXC2Vhg47pSGfp3jLLvtxK7j1187W55SLTLvf8xAARZNCjoT1RyiEa7EgVN35RZIXAc5xKTQfHnACaxcqhIO5SZZlN_DYTeVju3AnhD3aL83vSnjgMqRLU5Bi0CtiEui8KHazvEKfKXbOxqFqQ6A9cX8I3GrisuMG8V6WlDm7HP-7vGSgkZfFcgk7WI1tsE4HGwyeASEDnmDTqB7hviv1Jkr2E13IQVCyKjEbh-k-jzatLuhmPSvyyXpP0KDYgn7uDH3WhytNW6-2zLpDhrknuVFBZLrtP34Pevkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فریم‌ورک Science One گوگل
💡
گوگل یه فریم‌ورک تحقیقاتی خودمختار و «قابل‌تأیید» معرفی کرده با Chain-of-Evidence — یعنی مدل فقط نتیجه رو نمی‌گه، بلکه زنجیره‌ی شواهد رو هم ارائه می‌ده تا کارش قابل راستی‌آزمایی باشه. قدم خوبی به سمت تحقیق و توسعه "کم‌خطا‌تر" با AI
🔗
https://research.google/blog/science-one-framework-a-verifiable-autonomous-research-framework-via-chain-of-evidence/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4787" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4785">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kH4kdXNABPDCHunSJM_VzUHjTVfmGnljp3uMmb4jxuoUGH2UBe6RkvCfkaifCZd6lSC56eHKQJIGlsKjRj7eLRFI7sk4zuftqCbYIR-tpre7r3_PGgpEsZNTAA8MFtmgMDuAkCbMtY61bW1q0OBtjCv6w8Q6IP6f1IQFc7jxsJ0inuPxje-RafdH1j2ELoll97fuyws0lYXxyoKvX9SqSeY6qGRa5pS9wvvL9DQDdSrPjmmFSNoA-9FED1lZ8TX3GVP2YJQ7QFIBSSHfoPL-hKHk4Ym2SUl-d-fPWU8rJjhUMkQIN4maASgmctAltLg_3j8xuesCBwhg6X7ywan-Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L3ygUsH4XYYiOQ_Qkr5vYXRuKGBq-S7cBtkuWJk9qTcINc_Ekq2E_Xs2dNSX3XmuOFKD6O3jFnbBh892ZAN5soDSJtam-lG5Hkk__5S9GOxH9K-ppVwr2dx78DR0q2BTUkOcCcWd41wDCNW-anbOvUen8HzAkfBNcVVPsmAnsFaSJv5XVtcCzHEowDn9OVerCG7eD_hA3JgepF7jVAgHY2emxEeEEF-LT4AOaR6mkgHEX0jHbdK2RC017RsMnghGhgiCv3bsHAmAhyM_PtdaVX_LEUSAmFqC_szQsgSWLT1XdsbPaIKkH-N_PYwNK9G_QWNK9-tHDkjWyY7423UXOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4785" target="_blank">📅 21:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4784">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4784" target="_blank">📅 18:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4783">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">برق رفت
🥀</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4783" target="_blank">📅 18:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4782">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">این پرامپت‌های ساخت بازی سه بعدی واقعا به درد نخورن(توی سنجش قدرت واقعی مدل) اما از طرفی اعتیاد آورن. هرچی میرسه زیر دستم پرامپت ویدئو آخری رو بهش میدم ببینم چیکار میکنه
😂</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4782" target="_blank">📅 18:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4781">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4781" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4780">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سلام رفقا
ما به رسم هر سال، نزدیک مدارس که می‌شه پول جمع می‌کنیم و واسه بچه‌های سیستان‌وبلوچستانی که بخاطر وضعیت بد مالی نمی‌تونن ادامه تحصیل کنن کیف‌کفش و لوازم مورد نیاز واسه یک‌سال تحصیلی رو می‌خریم و بهشون میدیم.</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4780" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4779">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">با پنج دلار ویزا کارت خریدم، ایشالا که کلاهبرداری نیست
😂
اگه خرید کردم و اوکی بود بهتون میگم. برای Claude که حقیقتا جرأت نمی‌کنم</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/4779" target="_blank">📅 08:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4778">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یه هارنس چندنفره برای اجرا کردن Agent‌ها. یعنی چند نفر می‌تونن همزمان روی یه تیم از Agent‌ها کار کنن — یه جور VS Code مولتی‌پلیر ولی برای اجرا و مدیریت agent
👍
🔗
https://github.com/yc-software/qm
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/MatinSenPaii/4778" target="_blank">📅 01:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4777">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
پترنیها یه اپلیکیشن مشابه v2rayng زده که به نظرم از خود v2 هم بهتره چرا؟
هسته بروز که توسط خود پترنیها داخل اپ قرار گرفته و بروز بودنش حتی از v2 هم زودتره(بیشتر آپدیت هسته v2rayng از سمت پترنیها بوده)
رابطه کاربری روان تری داره.
مهم ترین نکته اش اینه با قابلیتی که واسه
#فرگمنت
اضافه کرده شما دیگه محدودیت آپلود داخل کانفیگ هاتون ندارید(بیشتر کلودفلره) ولی بعَی سرور شخصی ها هم مشکل آپلود دارن که طبق تنظیمات پترنیها اکی میشه
🔥
دانلود اپ از گیتهاب:
💓
https://github.com/patterniha/v2rayNG/releases
تنظیمات مربوطه به آپلود:
📝
https://t.me/patt_channel_x/94?single
💡
دوستانی که پترنیها رو نمیشناسن:پتنریها خالق sni spoof و شیر و خورشید و همچنین کلی از کارای بزرگتری بوده و داشته از جمله خود v2ryang و...
@xsfilterrnet
👑
@patt_channel_x
✅</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/4777" target="_blank">📅 00:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4776">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4776" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4775">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">با تینا پارتنرم مشورت کردم و یه سری تصمیمات خیلی عالی گرفتم واسه‌ی کانال و چند ماه آینده
فعلا لو نمیدیم
🎨</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/MatinSenPaii/4775" target="_blank">📅 16:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4774">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این ویدئوی پرایم واقعا خوب بود مخصوصا راجب این Demo های وان شات https://www.youtube.com/watch?v=LmXU6SEH3Ks  جمله‌ی کلیدیش این بود: The Demo is cool, but not actually a game این یعنی شما نباید با دیدن یه چیزی که یه نفر با ai اومده کدشو زده، یه وقت این توهم…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/MatinSenPaii/4774" target="_blank">📅 04:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4773">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XB7JdXVVX1eJUW3avdwufHW9GPRTy25_jP3Z74LhIrFAtZXPg0qGrzRfzvTvHfjIYtXRxehuZDjLdH42Wn3HEJK_LMymCaiGM-GhqRta1nsCdwKnnAy7Mzako65hvnM6K0dJB-0TiHbkotOqsKTloO40Xww_yTdH4Kfn1aacLpHtSt5bmeXK4wpgocONpd4HR7miwwrNHBcU48FQ6nsnJXDV3kNmZkOHGvQhyu4-F0qmbLuh3hqhIiaiI7trPUZ-JfTDRVUX4arMo4DFlCrwIStHAE7VYLjs3NlS_2_fCk79bhZouFmRxaN-VnbX34SAgGjRPOvJd89onF0Mg8ICfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئوی پرایم واقعا خوب بود
مخصوصا راجب این Demo های وان شات
https://www.youtube.com/watch?v=LmXU6SEH3Ks
جمله‌ی کلیدیش این بود:
The Demo is cool, but not actually a game
این یعنی شما نباید با دیدن یه چیزی که یه نفر با ai اومده کدشو زده، یه وقت این توهم رو داشته باشید که می‌تونید همین الان(حتی با یه اشتراک 200 دلاری کلاد)، بازی بسازید بدون هیچ دانشی!
طبیعتا کار رو خیلی سریعتر می‌کنه، اما باید مراقب این باشید که ai، لااقل هنوز به این درجه نرسیده(و به نظر من امکانش هست که هیچوقت به این درجه نرسه که دانش پایه حذف بشه از این چرخه) و خلاصه، یادگیری رو متوقف نکنید. حالا توی هر حوزه‌ای که هستید
نه جزو اون دسته‌ای باشید که میگه ai به درد نمی‌خوره و Anti-AI هستن،
نه جزو اون دسته‌ای باشید که ai تبدیل به بُت‌شون شده و می‌پرستنش!</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/MatinSenPaii/4773" target="_blank">📅 04:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4772">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سی‌ان‌ان:
فرماندهی مرکزی ایالات متحده (سنتکام) در حال آماده‌سازی برای یک دوره دو هفته‌ای از بمباران شدید پایگاه‌های موشکی است.</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/MatinSenPaii/4772" target="_blank">📅 03:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4771">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یکی کامنت گذاشته بود، بعد کلی که تایپ کردم راه حلش رو دیدم کامنته غیب شد. رفرش کردم دیدم پاک کرده
😭
خوشحالم که خودت راه حلت رو پیدا کردی مشتی ولی این رسمش نبود</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/4771" target="_blank">📅 03:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4770">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Claude-Free.txt</div>
  <div class="tg-doc-extra">4.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4770" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مربوط به ویدئو بالا</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/4770" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4769">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nyVEI24IepxVOQG-EYkBVnJoSgiSoKXjeK9qdvuhor0d9BHV6Odm5JWuMbNlrWx1VXPv3C3nAsd3IlhLgG4dbDbVbZP0-Qa-12E4M90WeCdvqCUTffJY534BGrFtq4vtjFFRyQB9ebzKczEpmI95qeg6t0_pZLETDAEPUwS7X1wxI8IpcvAZymlwV3iXYN_Gd6p3C9lPKPhINmIvuOycZmJU5BRhzxoa5_yIJb5q4jwA2eNI9JWV617MMvgmaZz3XYfsZZAYvUYbh_VHnG-gmLBjf3lvYfNe_XGXnbyLE7XWKujnXabiUvgYzeZADCXFcXElxcQcBQwcMHCmhbgBlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی:
https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو:
1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت زدم رو بهتون نشون میدم
2- کلاد رو نصب میکنیم روی سیستم و به روش استفاده‌ی رایگان ازش رو یاد میگیریم
3- با استفاده از 9Router، بهش Mimo رایگان شیائومی رو وصل میکنیم و استفاده می‌کنیم ازش توی Claude Code
4- با استفاده از API از Kimi3(مدل قدرتمند Moonshot که توی بنچمارک‌های فرانت‌اند در حد Fable5 قدرتمند ظاهر شده بود) هم استفاده می‌کنیم
5- با Hermes+Mimo و با Claude+Mimo و با Claude+Kimi، و با یه پرامپت یکسان، یه بازی سه‌بعدی می‌سازیم و خروجی رو مقایسه می‌کنیم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/MatinSenPaii/4769" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4768">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/btEaQ5alUaM16T8xZIrsdnEdX69N6t7pnm-fzaYwmswtamU_g-8IAkTRu7s1YTSDBUkzXx8c105JXNOUav59AOAXdWxwGAU3EgygTX3fOYLzcjXmAGoTPB7_s8-Z2B4vDIqIUiynXMhyYgfbIlNoV9Zx-p4x5ieLJ2kBaRoGRmv5jowc02NFvEOHTEnRgG0EoulQuJVF4QgVV1EONQ-hPR3-ReBtvHnkrOu-il7wM5qwMoIFXJD9s7aydNzj1g3O3D8IlFaaNjKFUjZGhrriOdgePWI1CaeR4f6mHqypHknbYabZOwG9nkyhL826-YRgPs9TaubK-Y_8rQuB8F4eAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قراره اولین ویدئوی گیمینگ چنل باشه
😂
😂
(بازی سه بعدی توی یه فایل HTML که 15 دلار پول رفته سرش)</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/4768" target="_blank">📅 00:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4767">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یه آموزش باحال AI هم سر همین سایت ادوبی داریم</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/MatinSenPaii/4767" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4766">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.7.0 منتشر شد!
➖
هستهٔ Aether از 1.4.0 به 1.5.0 ارتقا یافت؛ شامل بهبودهای اتصال مجدد، اسکن، پایداری و امنیت SOCKS5.
➖
پشتیبانی کامل Zero Trust اضافه شد: Team، ورود با کد ایمیل، Service Token، Access Token و Gateway سازمانی.
➖
DNS سفارشی…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/4766" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4765">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بچه‌ها اگه خواستید شما هم توی هاگوارتز ثبت نام کنید
من نفر 37 هستم
🥰
https://potterhead.ir/?ref=WL-1B24AC#waitlist</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/4765" target="_blank">📅 00:40 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
