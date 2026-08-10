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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 03:27:22</div>
<hr>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دو تا از دوستای خوبم امروز همراهم اومدن و اذیتشون کردم و کلی تجهیزات گرفتیم
🥰
🥰
به زودی خبرهای خوبی در راهه</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/MatinSenPaii/4879" target="_blank">📅 18:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/MatinSenPaii/4878" target="_blank">📅 08:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/MatinSenPaii/4877" target="_blank">📅 08:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/MatinSenPaii/4876" target="_blank">📅 19:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/4875" target="_blank">📅 18:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P-Wn3-MeiDX8hrj5RE_W-ZnV-iEmFQf9Ns5wozyOgXuIsvuQbSBa8dqlmQrSW5bpUeJYt-oN7Pgap2mubUEBCd4LnJfj23-OV_0FOdipa0ElX2PYsRwL8_Dda_4TiBe4HhbqCcXvkABvuoPX6Eygm6BS3eN3LqKRdx-Y0zCHxRSwsj_8IyDwd03s4N63cYkvloFTFJ7EqhTMmmkJv6SRH2A3vBKywEkzLBWsa1L4kB3bJmdMWp1DEUAPXatG5zmF03t8ehQv7p4j0DS0FqAMlJyYtRjaXd41q7nZdTwQ-JmQfqTUjR9scVH_vub4pfvgB6KR1ONXaA1bRLMrnTLrgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاملا درسته این صحبت.
به محتوای ویدئو کاری ندارم، اما خندیدن به اینکه "آموزش «چگونه وایرال بشیم» خودش 60 تا دونه ویو خورده، هر هر" قطعا از کوته‌نظریه
و صحبت این دوستمون کاملا درسته.
اون شخص داره این ویدئو رو برای یه دسته‌ی بسیار کوچیکی درست می‌کنه، و کد تقلب نیست که بگی نگاه کن خودش نتونسته:)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4874" target="_blank">📅 11:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نسخه‌ی جدید Grok-Build هم اومده که زیاد چیز خاصی اضافه نشده، همون بهش نپردازیم بهتره فعلا</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4873" target="_blank">📅 23:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4871" target="_blank">📅 23:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یه مدل‌های خفنی در راهن که باید وقت کنم بشینم راجبشون بنویسم</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4870" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انقدر اخبار جدید از AI میاد زود زود که به قول یکی از بچه‌های توییتر نیاز به گزارشگر فوتبال داریم دیگه تولید محتوا کافی نیست</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4869" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4868">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KjU10Wsi30ephFX5XNBW87IneOyb2V8-G7ruEngACun7slCXzfuDiDaj6EArW8-TBHMcq4UCZWNEb9ZiXt-zgjXHqJPXufwOUT5fDUnKrF49wSIamSiun3KHInazHG0jz7GcB0G4cp35vNnMF22XKEoAnbgFEUz8wFqCRMba4Kl5cDOAGDhoGaJW1KQi5-0pwd9pbdQltOkGDGq4W_80ZwtCohz9S-OOxPy2DLY2OpewnAfsbJf-t4eKyLLS2_DbJoYkb0gDUZKPgEaltGKWPMCao6H7ICScTVfG0L8OobhhJ4hqkBIIjWw5vbQFqUdxqxgZDrr6NtrPztoI4_bucQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین اپلیکیشنی که برای نوشتن چیز میزایی که توی ذهنم میان استفاده کردم، TickTick هست. ساده، راحت، بین گوشی و سیستم هم سینک میشه می‌تونید توی گوشی به عنوان ویجت هم اد کنید. خیلی هم سبکه در عین مدرن بودن و چشم‌نواز بودن طراحیش، هیچ چیز غیرضروری‌ای نداره. پلن رایگانش هم از کافی، یه چیزی اونور تره</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4868" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4867">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مارک زاکرچیزبرگر هم muse coder داده که تستش میکنم. سرگیجه گرفتیم از بس بین ایجنتا چرخیدیم.
اما جدی مدل‌هاش قیمتشون عالیه اگه بنچمارکا درست باشن</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4867" target="_blank">📅 05:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4866" target="_blank">📅 05:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4865">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=oHM6FB7Jru07cZSApK0LmZl7LyTuk28T6mQvy7K7v3rAcBWGLkJj1i4wmnc3P3GM1lHy8RUfLUz79Qnc4faaHjBv_7C0o7UOortvYBSg7AMQP6GDu0-NJ43sKfUr2NYMgYKQfLk0KI2Lw4vgLPBmXZSOveqTnvPspEoMMqewpOvyNnXEK4xI0b_WT0WjdLMl8EsQLMkIzLw3T5ufIRW4_mHHKzB3bBGiLHsMW48F_tNvdOKVjNFeRNgZz0va9SOelKWGn7XENJuf2APRcj9fOSRMIEmhkiKA_2JZ5cDZUsp8grK2tni5sXbRT6Q9nO028wx0SVTOLW5Q5oJip14Yvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=oHM6FB7Jru07cZSApK0LmZl7LyTuk28T6mQvy7K7v3rAcBWGLkJj1i4wmnc3P3GM1lHy8RUfLUz79Qnc4faaHjBv_7C0o7UOortvYBSg7AMQP6GDu0-NJ43sKfUr2NYMgYKQfLk0KI2Lw4vgLPBmXZSOveqTnvPspEoMMqewpOvyNnXEK4xI0b_WT0WjdLMl8EsQLMkIzLw3T5ufIRW4_mHHKzB3bBGiLHsMW48F_tNvdOKVjNFeRNgZz0va9SOelKWGn7XENJuf2APRcj9fOSRMIEmhkiKA_2JZ5cDZUsp8grK2tni5sXbRT6Q9nO028wx0SVTOLW5Q5oJip14Yvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4865" target="_blank">📅 01:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4864">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یکی از دوستام برای رفع لیمیت اوپن کد روی 9Router، حذف و نصبش می‌کنه و درست می‌شه.
به زودی واسش یه اسکریپت می‌نویسیم که این مشکل حل بشه</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4864" target="_blank">📅 19:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4863">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=gN608jQ2No9MyGtbdheCfL8UUY70cigfNoN44aMH3deuGkyVH6Kk30KC4qxgDn2CKfOwV2bbj5JgOPGuhUqvrV4_LyMFYCML0i2edaZnnIOABJhUIcNHrBtiBlCge9C3G9dIm_hNltlP8o824TTwHuN554lKnOQfVedQYuuJXwfO3EYQPnNlTpeFXReGM8jLs5D0d_lpHcnFPIJeLE_1GySUoCWcJf1smKzcBA5wyOzc6IX_wQvy8I-RztJFiTVeEbGxnz0A1aImEEqNHKT7la-6tKNZy5NXRjnk6cHzp0V1N2WfHOAmdiO3-wDwEjgwR6_LHqhu_GRXmyF-9_USXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=gN608jQ2No9MyGtbdheCfL8UUY70cigfNoN44aMH3deuGkyVH6Kk30KC4qxgDn2CKfOwV2bbj5JgOPGuhUqvrV4_LyMFYCML0i2edaZnnIOABJhUIcNHrBtiBlCge9C3G9dIm_hNltlP8o824TTwHuN554lKnOQfVedQYuuJXwfO3EYQPnNlTpeFXReGM8jLs5D0d_lpHcnFPIJeLE_1GySUoCWcJf1smKzcBA5wyOzc6IX_wQvy8I-RztJFiTVeEbGxnz0A1aImEEqNHKT7la-6tKNZy5NXRjnk6cHzp0V1N2WfHOAmdiO3-wDwEjgwR6_LHqhu_GRXmyF-9_USXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4863" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4862">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cji6ASGwUA6Au5bl1nCHgx8sUSn4m6q8z-Pt--dciBLOmoyhW2jtwN1G0WKng1fooqWjPiKK9q6lawwWh1kcmgQ3IPKJlKxzcTu9QNoyYdSjT0_uXUnEmz4PnirkRv8X4y4_vmE81ghGuqw09SS9BQnNanZ2CSS_ebDDjI392F4hIuOo1_2zsI1f_T3oYu6yk1xUxyIpPX3Vmb50bnt-jC_GA0Gc8VcPP4CqWl1jMOXwOwcLriDy6flySEXNsN1Bqikp7u4iot9SM7xlaVbJgnkAn6O3GIMKiG_XI2XFgapV9Hh74za940XHzKXyi0JswORb_wD4Yq9j2Pixy_yzvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه جوری ما رو دعوت کرده به سان فرانسیسکو، انگار حالا ما میریم
😏
😏</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4862" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4861">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">Matin SenPai
pinned «
خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید: https://t.me/Editor_MatinSenPai شرایط کامل توضیح داده شده
❤️
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4861" target="_blank">📅 21:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اگر وسط آپدیت کرش کرد، یک بار دیگه باید re-deploy کنید</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4860" target="_blank">📅 19:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4859" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4858">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">«بعدش هم روشن شو»</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4858" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oZQPZ2u8T5eaWVtmuHu1VvwTRkqHivHdmW8jtZvrzUxD9R1T5Adhz5UcuWyXAGrS1ssCP7_8_DoRNso1cb08qW0PrTOBcPEW1_vf0EMyOdLsjbiec1RUNbiCZSSPEW4dmHHGHzRppBdUfsdpuZ-S147WD6VcNQpIs0xdFC3ZCS8ggC8BHT4QDkyUSFqiKHTa8l83FjlHsqnufU9uucHxzGWWJ2BRWebTB0AgSwSZChci8lFki6_vAAkP0jXPHaRljZTw5ooh1RLsq1BsvGIvgTC7jkvA6-YPtXJaf0n-ij4Vi9XQDtEYT3ylVCP4pD_CemPIwNYuzKDio6Vvt3o8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متین الان که هرمس اپدیت داده
چطوری ربات تلگرامیشو اپدیت کنیم رو railway؟</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4856" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4855">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4855" target="_blank">📅 18:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4854">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کانفیگای کلودفلر من هر 5-6 دقیقه، 1 دقیقه قطع می‌شن نمی‌دونم چرا</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4854" target="_blank">📅 17:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4853">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">راستی این ویس با میکروفون گوشی ضبط شده و با هوش مصنوعی رایگان Enhance شده و به زودی AI اش رو بهتون معرفی می‌کنم
🥰
https://t.me/Editor_MatinSenPai/3</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4853" target="_blank">📅 16:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4852">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید:
https://t.me/Editor_MatinSenPai
شرایط کامل توضیح داده شده
❤️</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4852" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4851">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qf9RCVSJpLYbP4IHPl_NlsjgL1CG_d--4KeSGF-f2jVuN8NtiJCOwhtY1mdtxmNBMvcw2MA52VD829H8ErVfw2al_T2IhLkxDL8i4wDGIpkoD_KTsCK8P6N44y5l0W4KbmyQfM4Q1VA5LSihhHl7DUxTyjy3simqTmcOPkSOXDDlHtoX9YGki86RCuLdVEmjjTHYFk0gmj4IctNudqn3zszFWVkbct5RWhL6unI6A6XAiNJSR8a6ONlBOtRzJm2wuC7qie_N6LGyk0uS5H0UFe2hf7yUZXMY841ID1cs6dCmxHKAI8ar_uZJhVo5_xHHwarfOSZ3WiY8P-nB0c4kKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این اپ INCY که امیرپارسا بهم معرفی کرد خیلی خوبه
دم برادران روس گرم</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4851" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4850">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست  https://t.me/RasadAIOfficial و برای خودم هم جالبه کلا به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4850" target="_blank">📅 16:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4849">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست
https://t.me/RasadAIOfficial
و برای خودم هم جالبه کلا
به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4849" target="_blank">📅 16:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4846">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4846" target="_blank">📅 08:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4845">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انگار نتیجه‌ی کارآگاه بازیا درست بود این هم راه حل آنتی گرویتی روی هرمس، با تشکر از سهیل و Moh جان: https://x.com/i/status/2084572159016382738</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4845" target="_blank">📅 08:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4844">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XUHZv9jb6KcxpL_hBwxCkbzk8O-B6g-oSDOtfbX6h_V1k64_kU77y4JtbmCWp2xN3lP92zUvfI-MYwSe6XUIcrrWlNxmeHUMrXyix54dB11T3HOLqPPtPjRZ1MibFnzQNVviTopS9V4ZAsZA3KcOm68FD9gYe0mc18bno0z6gbUkUmEwscCTM76_Erj34TQMmj0Xu_4S63we9qns4H9Y_Ma2rBBlTdS_yLtOAvzY-cNY1TSunqUo9Eqz5sEF-sgRxC6swM0Xd1mPfK39QAqYcsQZfk0ejedx9oGZVWEZpHMK407fEF6K4hkK4AZPHCeWJTuBtB0ZlDGi4ljFHgA42w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم مسئله از خود پرامپت سیستمی هرمسه چون درجا ارور نمیده قشنگ ۱۰ ثانیه طول میکشه. میره فکر می‌کنه و برمیگرده</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4844" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4843">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fFnz67xjTjh3fd3ruaACr5kPu1knTphTGabUsqRCkAeHu0YtRkOa-duZSnSBrAa11R-S5r0KKj-wIThLJVO_bRD1nu-eDgeXPJlDtEYQKT0hQYRhjFH3Cts45-rHNIytWlRLgEEjtLO0sffQSnM_iReYt8By71qQAwkyxbBJAMMXs2Ex2_5L5nBK5izadGL52CiyTC6x0SBxx4lpAUijaD6C-B76S5IzB43Ql8_8J3o3skWxy0bfrpicd0xWuGKX3VAtBE10kgULjlRSMX4xdxNggMIFUzfVB92N8lnhiPcbh5NkAknJ8VGbqAZRBbAP2u7FExGRobQe3ydydT-YRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلا درخواست‌هایی که "Hermes" توش باشه رو رد میکنه</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4843" target="_blank">📅 07:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4842">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router جالبه که روی هرمس هست فقط جای دیگه ازش استفاده میکنم مشکلی نداره در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4842" target="_blank">📅 07:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4841">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qyS12M9E6eR7gdAE_e3FjdKrmiBqvl696LJwbzoi7dX6AaKnOXyfW-19WY5ec2nL5nOW9uyZBI7pcplZU5AAnSiYtm9Psbcn19RvrUJQMZL9eTbZaCqOV3Zk8cFE89gY4pl3YekIBzCtyeOyCVcqdhu7YXUDIicxnhQx5ID8VENHpCufdQ6JwpzaqrylvUWbH4wpnwltUu8APzzfc1R_hhGVUVW4OS6o2J4-8L6M7StJpnwl7GqG4FRgQvPkck2N8MV6hN9-nTnwfEVEPnYSmAY7xlE-vB9XzJCbA-uA7PL_j6Run0DfQcJpNjACQczSDEYS6OPP60d2Q5_quozssA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router
جالبه که روی هرمس هست فقط
جای دیگه ازش استفاده میکنم مشکلی نداره
در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4841" target="_blank">📅 03:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4840">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AmfUpuNmmIof-H_b_gUMxXkzQaFepEunti3MMjTPKDA7KEj8zFSE42_ASVuLqEuPxBLpdUeiZI9DpFmgn8sExNg_SzhJTuxRA_5S8zp6XFG2NWS_ob0qQSoiFOqhtoFFcKNZu64UeMv0Vl0dKtI3drAgk91CwRMk5d7qepDB4LP_94ZcNVFt6aNmVFqEdOrfUrJTZr1q-xFApBdbEb6m6rHfwteQFmk_LGpnG0SXcwywoUYd3ENl6LT1pyrfbvvpP-Wlsfx9RDrmlFPz8QljhH8sytf0kMDj_olzmq9SFbh7aS2K604d03X4h7_UYLXL7PSPHEE1rEYxzJ2XPBKq1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچها اگه از pomodorus استفاده میکنید</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4840" target="_blank">📅 00:57 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
