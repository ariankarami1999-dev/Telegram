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
<img src="https://cdn1.telesco.pe/file/SY1I8IwYNk49EQ6L4mroM7CMOK8fRBWxXBGgj5Jna0DSJYOR-k8_eqA3Wca54HG1lM5_ECq4sLSW1ZmoL4Jw73gaahCnMdg2fP_v7RhgQADoSzU6Q_Efyxvtchx4A3glpFP8KP_FF0EVX6enSs3-sjhuNgH0RULF2bqiDxmpIW8LJO_SUQR2ZewOJkfLle94zfIALhTfgcfXVbaP-v65aBfKmJ-JyLAMmFT-vwggDwu727LGU6KU28_VwGwWrMIhvhl3CHlm3__N-bx7HFFGw1O5-vdJqOrIDQiayH7fMTwR16UU_7HztsoBr05J8Ya3CZZeakiaA1YZFvt0aUZ4Rg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 11:15:23</div>
<hr>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/MatinSenPaii/4878" target="_blank">📅 08:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/MatinSenPaii/4877" target="_blank">📅 08:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/MatinSenPaii/4876" target="_blank">📅 19:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MTe1a2k8IQyE1nFGztdaneJWfkCAuRNGxK_l-FHRaw0jdzZqu2qZ3XKi4WEvLewDCpemw_sv206RRKTsedAnCNIihZWF9_lFgUElQl1jB1DwOQtAjtJG-xlfgltLFXD3RaDqFQq5lSnlSx6vCxUkor4BBDOowPxsgKrczhb8OHllGIouA9Gg4SQWeQOJYjqPmtcMejEeK8WeXuzAym9SrmqRsA7irds4anf9TataEZuyWqDx9c1ZfcySI8Qo0aE0NcmUkuCvW3r5QPzOtVBP9k0bTdW3JanV4j3yssvhRZoDiK8ZCNspmRPReznlunmBjssO2XER84dr64MYbC1ORQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/MatinSenPaii/4875" target="_blank">📅 18:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P-Wn3-MeiDX8hrj5RE_W-ZnV-iEmFQf9Ns5wozyOgXuIsvuQbSBa8dqlmQrSW5bpUeJYt-oN7Pgap2mubUEBCd4LnJfj23-OV_0FOdipa0ElX2PYsRwL8_Dda_4TiBe4HhbqCcXvkABvuoPX6Eygm6BS3eN3LqKRdx-Y0zCHxRSwsj_8IyDwd03s4N63cYkvloFTFJ7EqhTMmmkJv6SRH2A3vBKywEkzLBWsa1L4kB3bJmdMWp1DEUAPXatG5zmF03t8ehQv7p4j0DS0FqAMlJyYtRjaXd41q7nZdTwQ-JmQfqTUjR9scVH_vub4pfvgB6KR1ONXaA1bRLMrnTLrgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاملا درسته این صحبت.
به محتوای ویدئو کاری ندارم، اما خندیدن به اینکه "آموزش «چگونه وایرال بشیم» خودش 60 تا دونه ویو خورده، هر هر" قطعا از کوته‌نظریه
و صحبت این دوستمون کاملا درسته.
اون شخص داره این ویدئو رو برای یه دسته‌ی بسیار کوچیکی درست می‌کنه، و کد تقلب نیست که بگی نگاه کن خودش نتونسته:)</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4874" target="_blank">📅 11:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نسخه‌ی جدید Grok-Build هم اومده که زیاد چیز خاصی اضافه نشده، همون بهش نپردازیم بهتره فعلا</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4873" target="_blank">📅 23:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UXw3uJ2QxkhO8OWJelXs2TVUfBiIwGJn0jn_rGvQXaw90xwTmZjdCq7eB6XTVaJiNX5h5kZK3d7qftgpIGyVluSZ_RMsCcMrDaDd42zkC97zyKZjeSiz-vH7851S2n4fi8mEPY4kvKa75sx1xMVcgEBvAMZ7KVQ_afo_8HfK4JjGutyexz3E8X_YKqypEltIc5MRwnlZWuUE5adKxAi5DLRACH18VnCCGTYHpK4PjXv2fRbg_27m4EgC0xb4fWuHhA_yNlBk688SbIbidJEMutgzwY_s7p4CQVGZhoTtNXpiO85HGVUdhkFSxg0w3mXl0EkEZKhssgRnjgsdvnBwTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qAixp45A3vSsrnQ7X2VphDgm40aifE2NOvdaA7V36-14m8eRK47bvP2hyysQQgSQz3LMu9eFOX5-SRlJeLbaMg8rVkPcR-xER7dsBooxkbrWc0m8DNhCJzH4SOhiIRBjV5HRicOxa0jcqZHsXOWe1_S1ZcoRqFNdu-rX6oyd7CwLpBxOjUY_eXkBEjY07plmdjt-9QMkPN0cfDEevdh4rDgKbBaz3R8z3R5OOan4lh3bvtPRpYC3nJK6kfj2ulASnB8JLbi65cn23QmGczYyglVU3ikE9qmGAVAU3LR-EUf5RPi4sEOwD9HD76-D-P8ByhUvi0klvMAPLULkks6_dA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دسترسی رایگان 14 روزه به تمام مدل های zed code
ادیتور Zed اشتراک ۱۴ روزه Pro خودش رو به همراه ۲۰ دلار اعتبار رایگان ارائه میده!
​مراحل دریافت: وارد سایت بشید تیک Free trial پلن پرو رو بزنید
zed.dev/pricing
با اکانت گیتهاب ( قدمت حداقل 30 روز ) لاگین کنید
✍️
CypherDeveloper</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4871" target="_blank">📅 23:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یه مدل‌های خفنی در راهن که باید وقت کنم بشینم راجبشون بنویسم</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4870" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انقدر اخبار جدید از AI میاد زود زود که به قول یکی از بچه‌های توییتر نیاز به گزارشگر فوتبال داریم دیگه تولید محتوا کافی نیست</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4869" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4868">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QWydbBoODPfECJoI1aiTGtKoZyV8iz1NVQHhqsKPm1DQqJLGr_7PSMEObC2Meo4bC68Iber8lCfh8x4M4_wmuGMOMdF_0zGpnK2lH444sO6waLpYu8uziZypiGVt9RCAdN9XhTLXkh7qUmpTspLlH7S0bZIsEEd0Tp5uPmetfX0u5XajxGeYnDsHKtsgnJ0QWzqCSQuFKh8NaIJTHWw1c0JUZF0NCGcl-0dRYc3v3A9wCSDi6EFPJtTZ0Rsr3hiPyY0lr6N-6shAXcIUsf78pbnE2W_8GQwxK17ehQo5n6ro3IaN7rf4umwaQWgvp9KxPOOlXTu7n2U6VIWfa6Vr-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین اپلیکیشنی که برای نوشتن چیز میزایی که توی ذهنم میان استفاده کردم، TickTick هست. ساده، راحت، بین گوشی و سیستم هم سینک میشه می‌تونید توی گوشی به عنوان ویجت هم اد کنید. خیلی هم سبکه در عین مدرن بودن و چشم‌نواز بودن طراحیش، هیچ چیز غیرضروری‌ای نداره. پلن رایگانش هم از کافی، یه چیزی اونور تره</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4868" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4867">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مارک زاکرچیزبرگر هم muse coder داده که تستش میکنم. سرگیجه گرفتیم از بس بین ایجنتا چرخیدیم.
اما جدی مدل‌هاش قیمتشون عالیه اگه بنچمارکا درست باشن</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4867" target="_blank">📅 05:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4866" target="_blank">📅 05:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4865">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4865" target="_blank">📅 01:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4864">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یکی از دوستام برای رفع لیمیت اوپن کد روی 9Router، حذف و نصبش می‌کنه و درست می‌شه.
به زودی واسش یه اسکریپت می‌نویسیم که این مشکل حل بشه</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4864" target="_blank">📅 19:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4863">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=fOX_zcHYMqZy_62OXyx97TzMyYclcaiu1l3eJFORk1QUqqBneRL9MgNuI6AQc_06Ng_T1bwo5gqmp6O6TSmSyOWymqZ6QGbQ33jR1cnL0Pab4ubEI8HlRvsmJ_8ZqPFngh1hmD4OdG6rloQN1kJ4-Ygp4IaH9HHDe8RL7eXHfOZWKnYYIgyoZlUKtwOkjhUPsqVGJScotyoZeJ8JB0gGZtAF28NDPH01tw28YkonS-XyXz_nVIGbHwsZ9-i3KPvYDHoMtGTjhD2VhqLfotMeS-ocuzdAIn29fIC8LWxHaBGilZ5fQdpiIPjs44XYQ4k0ODQBv2i2bFHbKcdC3ar9uA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=fOX_zcHYMqZy_62OXyx97TzMyYclcaiu1l3eJFORk1QUqqBneRL9MgNuI6AQc_06Ng_T1bwo5gqmp6O6TSmSyOWymqZ6QGbQ33jR1cnL0Pab4ubEI8HlRvsmJ_8ZqPFngh1hmD4OdG6rloQN1kJ4-Ygp4IaH9HHDe8RL7eXHfOZWKnYYIgyoZlUKtwOkjhUPsqVGJScotyoZeJ8JB0gGZtAF28NDPH01tw28YkonS-XyXz_nVIGbHwsZ9-i3KPvYDHoMtGTjhD2VhqLfotMeS-ocuzdAIn29fIC8LWxHaBGilZ5fQdpiIPjs44XYQ4k0ODQBv2i2bFHbKcdC3ar9uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4863" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4862">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s5YESl9vT4uP-0ZxYEp_lfSzSQuQibwytqw-0YkcUjQo7v4wxLxGbBTtDHJ2vbVsGK8YDQRcyubduW4JAOABlxYU9MyZR0G3vIO2Svinn_2PYgS5NGoa9LS-0yynkKAAwUUiFu4RJIR7vQk90MdPIven1rPuKSfBs85aV4xz_fz1znX-DhQvr6sYJmSXrrHhZGLOavOwLcOpin-3-Ve1DgzCdAi5SAera9DLMuun_rNJ2bg79S-JDxLj9kW4BZzOYrYnHZ4tr-zv7ZTDCnlU5OC8UhKDHqDJaFjD5ROZ-EEGmXm7TQF5dOpzJ84XoIBQIzEhtU4XKP6yKr80S4E3yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه جوری ما رو دعوت کرده به سان فرانسیسکو، انگار حالا ما میریم
😏
😏</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4862" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4861">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">Matin SenPai
pinned «
خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید: https://t.me/Editor_MatinSenPai شرایط کامل توضیح داده شده
❤️
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4861" target="_blank">📅 21:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اگر وسط آپدیت کرش کرد، یک بار دیگه باید re-deploy کنید</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4860" target="_blank">📅 19:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4859" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4858">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">«بعدش هم روشن شو»</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4858" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V1lne3xmP7TbUU5_oh_JtmnFMsaIp_ml05QzEnmNvlXFcxfK5kJCJ3N-bdN6O2Qzs-ctRm7HzfGb6OBsz7D7yRzb9KJYzO19qTw3LQiaV28x9wl1dqNwrA9uioyl6KSxI9zRvzn-FgFcoPgTeA8Fwkifvaacfb_LwWemrIPpa0vWt8DNfKH92uBN1N-PSzXbH588L-pUs4Z_sbJ7mxYrtFDebobLM6ceJUghJzYVdtlLj2NPnYJt9Nn4V2sL7xNBjwAMQE3lP6xjhYHtVvJ9eeJpJiCDlcyeC8LZLR1r81GLwQiAsXzDtoN3YmvlqXTEfsRdxmu-Efobl7Tphz9bYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DItjSnBw4UGEYdqd-jRMPCLg3G8-70rvlEksEdThZ42T_7sW-8CvdySwCp6qMlizqSENcGW00hiU81RbMwUza1dJOe_g_-6W3d-Xc2rLGCZRkDnj7_tZhK5A9VAEOXwmYWsW6Gj0A1HqJiVQ9Cb-Gzpc46v15-ltF1RR9yNIzBptiAFnryhsnNbvjHetayv0RM4Sxf4jhfou7fNN8-fWb1KvGedFPsmmkOUfdPyuEUE79BecEhEo9DZsvlT197DZcGrZE3hfZMGRSEUqbjWy_dSM9gTddJASOaXZiyN1jLmG9YEgl7825BnDD19lnZEitlDNrCK2H2NxePsnjTBjdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متین الان که هرمس اپدیت داده
چطوری ربات تلگرامیشو اپدیت کنیم رو railway؟</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4856" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4855">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jny39uyNF31IaaVyqFHfu7_d9eTxraLUUk_PsVvwYFNQbp3-95Ty47cTEBQa3Fp51pv7gWCjmdAtEX2ERARYg9agBR_KysTaOER0K_aSNn1rGYcUvaihC6Xhm-HRQZL5NxaD0kO3A7xrpE4JGHJFw_YVQGY5WbnGhj2x5Efr9lr1uMoaI-QYUwx8lQp_goYhqYJBz7WmonLmez8BtV7L_uaDyM2RRVdKBv5i8pjR648Ljg-uxduMTCAp1nx0vUR5FkxRSrh16rMwQnzcUC2H4L2h3vubL1RK313BPr8_Axe_EXwy-zHmOUpnNkG4RUC9P9vbK8vhD3FwiC2lNOzQOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4855" target="_blank">📅 18:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4854">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کانفیگای کلودفلر من هر 5-6 دقیقه، 1 دقیقه قطع می‌شن نمی‌دونم چرا</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4854" target="_blank">📅 17:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4853">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">راستی این ویس با میکروفون گوشی ضبط شده و با هوش مصنوعی رایگان Enhance شده و به زودی AI اش رو بهتون معرفی می‌کنم
🥰
https://t.me/Editor_MatinSenPai/3</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4853" target="_blank">📅 16:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4852">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید:
https://t.me/Editor_MatinSenPai
شرایط کامل توضیح داده شده
❤️</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4852" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4851">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WOSnVauE1ppPPGnSdC7gtQRSdGIIQSRVsKNpqAqYDzuVAyxCdlvXrk8N1OCzdaK3l8xjxqaoFOQTVy-3zwfAvuCTOwSeZuGym-WpYxDzpU1L5UI1FrmYjRMuocpxoxFRrT8QNnAK-qmS-_H-jkRW4JbzA5V2Zb3OwSm5Sorh2LgjtapfJkWjH5eH3SllY-T4IOR1_Fmf_MyaKXDxocUEcA89zIZegDWC3JGJ2zI3cJvVDWnNiiDdjs18ZUHOWkEqgVfDlSRphuITOEAwynYWtrF5cLZ6lLTihInx1aE-Rin0OXKfPBHuHjQvMe6BtII7KkZns75oIAvL5afy_xArdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این اپ INCY که امیرپارسا بهم معرفی کرد خیلی خوبه
دم برادران روس گرم</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4851" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4850">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست  https://t.me/RasadAIOfficial و برای خودم هم جالبه کلا به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4850" target="_blank">📅 16:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4849">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست
https://t.me/RasadAIOfficial
و برای خودم هم جالبه کلا
به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4849" target="_blank">📅 16:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4846">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4846" target="_blank">📅 08:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4845">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">انگار نتیجه‌ی کارآگاه بازیا درست بود این هم راه حل آنتی گرویتی روی هرمس، با تشکر از سهیل و Moh جان: https://x.com/i/status/2084572159016382738</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4845" target="_blank">📅 08:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4844">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XUHZv9jb6KcxpL_hBwxCkbzk8O-B6g-oSDOtfbX6h_V1k64_kU77y4JtbmCWp2xN3lP92zUvfI-MYwSe6XUIcrrWlNxmeHUMrXyix54dB11T3HOLqPPtPjRZ1MibFnzQNVviTopS9V4ZAsZA3KcOm68FD9gYe0mc18bno0z6gbUkUmEwscCTM76_Erj34TQMmj0Xu_4S63we9qns4H9Y_Ma2rBBlTdS_yLtOAvzY-cNY1TSunqUo9Eqz5sEF-sgRxC6swM0Xd1mPfK39QAqYcsQZfk0ejedx9oGZVWEZpHMK407fEF6K4hkK4AZPHCeWJTuBtB0ZlDGi4ljFHgA42w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم مسئله از خود پرامپت سیستمی هرمسه چون درجا ارور نمیده قشنگ ۱۰ ثانیه طول میکشه. میره فکر می‌کنه و برمیگرده</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4844" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4843">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fFnz67xjTjh3fd3ruaACr5kPu1knTphTGabUsqRCkAeHu0YtRkOa-duZSnSBrAa11R-S5r0KKj-wIThLJVO_bRD1nu-eDgeXPJlDtEYQKT0hQYRhjFH3Cts45-rHNIytWlRLgEEjtLO0sffQSnM_iReYt8By71qQAwkyxbBJAMMXs2Ex2_5L5nBK5izadGL52CiyTC6x0SBxx4lpAUijaD6C-B76S5IzB43Ql8_8J3o3skWxy0bfrpicd0xWuGKX3VAtBE10kgULjlRSMX4xdxNggMIFUzfVB92N8lnhiPcbh5NkAknJ8VGbqAZRBbAP2u7FExGRobQe3ydydT-YRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلا درخواست‌هایی که "Hermes" توش باشه رو رد میکنه</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4843" target="_blank">📅 07:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4842">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router جالبه که روی هرمس هست فقط جای دیگه ازش استفاده میکنم مشکلی نداره در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4842" target="_blank">📅 07:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4841">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pqZembV9rzbB5L0Z5IVaYYopjWkOhCoEJrqUOfostomcpcuMW-nrefqgW5ZEjUu9AfG9XORPUSVifv9vRjqy0l4UD8-nKVu7OxUqPlU5rSjTFiH8qKVqBAv5Ghc6QGVsDFkcGkUyWR4BNlaTmriufgDLLiS1KoQktmyshiPHR2QiiUn-ZzmGr5Aam93KhX8bnSjOItswH9fDtp5WiaOBzu2brfJdMXom8o6IF7GJaK2o58ew7FQ8i7ypfWh80GKVJW2Rs1OEooonr9VRJqbG-CdgZbXIpREcbIuDqCTQuLRUblLxWgk8icSwYDZNY3ffm3oKKmROpXB0VzBxZEfkQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router
جالبه که روی هرمس هست فقط
جای دیگه ازش استفاده میکنم مشکلی نداره
در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4841" target="_blank">📅 03:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4840">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lfDwJWiN8ImHovGNifP5qxg5b1dcMrHY-7Wy2s8NRoxzUy5re2ZK0q6os6j9cL998NY3dHFFovodeLoGcmDerJuDLW8MYNb78VKHFoT-0qEaF9xRBnr6f7bvTRFVzfFP2mHfeqsqBSWr9ov4Mk_xFk3_ILQOzrwxXLkNVIs0xU1kekDvt5iLoJNVOQoryHzY0ywQ79Dl0v4zcmOst-JMEwJYbr7B1TsTOHJqVgkXUI2Lr3CeYmWjRWhScdhZ3Bza9oI2lMWeGFISoidfpoWUnMkkrHoBBVZM2WmEi8PNkT0qghKwRmljWYedGwY9YjrP7CBsufm3JWGUZw8U2OtFvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچها اگه از pomodorus استفاده میکنید</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4840" target="_blank">📅 00:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4839">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رفقا ما داشتیم خریدهامون رو به دانش‌آموزهای بی‌بضاعت سیستان‌وبلوچستانی تحویل میدادیم که یکی از همکارامون گفت یه خانواده‌ای هستن که چند ماهه وضعیت خیلی خطرناک و بدی دارن.
بهشون سر زدیم، دیدیم کولرشون چندماهه که سوخته و شبا موقع خواب میرن تو حیاط و پشت‌بام می‌خوابن، اواخر هم فهمیدیم بخاطر گرمای زیاد، یخچالشون هم خراب شده. بیشتر پیگیری کردیم فهمیدیم خیلی وقته که وضعیتشون این‌شکلیه و کسی بهشون توجه نکرده.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4839" target="_blank">📅 00:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4838">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">به زودی قراره یه چالش(چالش هم نه) ادیت بذارم، و ادیتور بگیرم
خوشحال میشم که اگر دوست داشتید، داخلش شرکت کنید
اطلاعات لازم رو می‌ذارم تا فردا</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4838" target="_blank">📅 00:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4836">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cuHkp_ICLskGNyS8aoqaDxWkN3p9IC68Jf5EyZl49Or4rLaHxTSiU-CEsBSf2nILyUx-yoOBfJxLHsg7L4VQ-HcgWOS0j16Q5qeHJIjdHRFIrRwaxmBLMY6Vd24_zWvFuBflswbY6y4hI9E1d2kkGbAKyqNGuoUQvM5s5SQhTWXIw1ilnauQ7LnZ0BKTXlLwqrERQ880mohKx2aS1kw_ZFoxzanDV0MLkDUnZDR6zjm3a-ti1vqotil4m3GkTXFQA0Rv-JnzgnFhH8nu4U7KO2FRBDqGjJgCp8ZANuyGflD5kDwpQR2cTokt4Rx4I-wASZZ5Kn61WggSKRvHNtbJXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از چیزایی که راجب کامیونیتی فارسی باحاله و دوست دارم، اینه که زیاد توی کامنت‌ها با هم در ارتباطیم. کامیونیتی خارجی، این شکلیه که ویدئوی تکنیکال می‌ذارن، 60 کا ویو میخوره اما کلا 25 تا کامنت میگیره. یوتوبره اون 25 تا کامنت رو حتی لایک هم نمیکنه. اما کامیونیتی…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4836" target="_blank">📅 21:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4835">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/diDS24EBhL5MSLl1YPiy7PNWj4j5YBKj_ChIqn3ZF4vKxbneNaMZax6uGfs-QnN-0j18qRzSIvFwYbl0lfLwKIpPrUB4quorMsBkVoyaABT4xkBn6yvN7_faK_x3Kx5YJqES6bz0y_tREJLImVoNWkGmml91cGc6KXg6fAjavbi9_ve7bNNCe0sNfjN3Xv1NPG0Tucih26zeB5BoPFHa9oyYXY5cSsak86pBgp73vSR5Ovn2H0PR2-kpQHAhwCpyxXHoOeTUjXM93mfnhb1c5VxhwD11ZwiNRpjujgLK0J5ATlEbanvHaiWWlJfvs5v_LL3qJZurUPKKEPRxUcl99A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایگزین متن باز Fonto، رایگان، تحت وب
دیگه برای استوریاتون پول اشتراک ندید
😁
و اگر دوست داشتید، از بالا(علامت قلب) به سازنده دونیت کنید تا لایسنس تجاری بخره و فونت‌های خفن‌تر واستون بذاره.
لینک پروژه:
https://github.com/FontWoW/FontWoW.github.io
لینک سایت:
https://fontwow.github.io</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/4835" target="_blank">📅 20:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4834">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">و به هیچ وجه، به هیچ وجه روی کانفیگ VPS نذارید.
فقط روی ورکر و کانفیگای رایگان
چون به سرعت از طرف دیتاسنتر ابیوز می‌خورید</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4834" target="_blank">📅 19:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4832">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Osol_q_WUh-UFPQABGoJq4v-iw0lYEbRWZbg1PA1qSEqoc9IQ4COLW_IXxrvEfgy_WoTNs9OvGpcQOws5CbPrUcNjUaY7astVqQhU6Y3-zttsTVsvFYxJVYw8aaT4kaxSFXpikIwER-DIXBWQz6mFzvcz-Ccpw0HwjXB8wMvtLVEjdpOmgews6thOdOPoQ1vjJG16-Mx8xgrtOy2QFMHlfOqpRrdKSnYoENhMTkVldRPUnVbsKOJ8g8nQmx2YI-xdsU8_Bkh2sFgRyv4UjbGDwkTFc9cUqaSP9_aUnM-YYFMBUJdHwA-8ZxyCodl9EKk6swTNSXvFgsNlt95dskN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ow4XB-zMGIXa68pOEPp1CzBWQIQv9We-cuJufhp8Be9OhfaY7204XfD_89tTydOwFb138-lyhVSAd9CKhzKxSSUKyNJwk3M2N8nK-NHfeKvCn1QVFB15AsWzdOxVlcPpdIv0lEBsalNk7VWlufc3gQxbUNHc-bEckZvokF713jWUqiypC3fzyA4qs-0ckGUHMiAqUXF3W1mMiNoZrbDHTltdEJUGDWLS69goGehaxq5DhYrK1Fsv_GnHaX1XU9D1ILjOYkBW8N-jh4BfgED6nf9JFHxYOb8O4KwMdx-z4eQkTVI_z149yS3hc9ZUg0gHpxU9BIB9akdct90yUxF2zQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4832" target="_blank">📅 19:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4831">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mTISyQsR5rW9sw_xD4e4Gzn3Tyc7R0JQECHHac8b68C6iyOt7dQWRorXvcmLYFNuks8bfXCjVDQWwMptvJvRh49OIsnG-ZjQ5VMIu5wB2Op9Ya_w4cn5m_939q7HCIe08wqI-kvkiDZ2CJelfsVJBcoce3afa3gQrFTGezRtIBn-h0cRmFoMOLgkAvoxi6UnepwMoA4BZ3rP_a-meWYcuSZJnZ0oV5iSJl3k48d-sjiVS6IvnppFqnrIgXfwbv77n3MAaYLH8ErmPH0xmsqN-sUPhRcwcLGg-x0XzT3_VzVKvGX98LROcL2vMfG_agnyCPeD1jyU0Koqz56EE16v-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید: https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4831" target="_blank">📅 18:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4830">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید:
https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4830" target="_blank">📅 18:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4829">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خیلیا ایمیل دادن پرسیدن با چه شرکتی کار کنیم
ببینید شرکت‌های ایرانی همشون یه افتضاحی به بار آوردن. یا چنل پروندن یا..
من هم شرکتی که واقعا کارش درست باشه نمیشناسم. ولی خب متأسفانه وقتی مجبور باشیم، چه میشه کرد
الان خدا رو شکر دوستم واسم نقد میکنه از خارج از کشور و میفرسته و دمش گرم</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4829" target="_blank">📅 18:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4827">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nLJSZjKIjL2HZyIh7trSIianodAcIOpvV0Vl3_eDL4mOdlyDUDLuLGpCbLTvuX3pJ6OFesKOmThaReXVQBXnLWRN9A8UsGEksu2yx54Y7xFZ6AETC_CwlQxi2IQSwCzKNS-w7ledJHLW39O8BdqTzxCApyqpjfUA-OGCKwdQxsNhBk_bRuIxI7e1DAukqtnQN8lu_DgIS2iW6VgvHW49LAPBWZKvqUD_HrHYN9d2E8KF8oVOdcsXRlDA6Pg6ucjSnDwz6ZSCtzaVAZvZPQiG1dR_m-vifIEfTlz12CadtCpCMQxLNxbg6CsfLa5buk4uJaQYV1rkVicH2RGgrG8Osg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ldja5C0MuJHYqDgEyGe_kUGHuUXnKDDFDgizAmLzp86Nd8WSoZHnJ-3AFXogxeiKtbPr1Hld0wfLQzXffATpv2xkO-mUYQBB68Out21Qqyvm5lSC6pQFXNmI7eG-vSP0F3M7hhIov0U-N1JabBK8FtUwYT-DeGgd4SXI2FXAZvFUG6EnlBZ8o2I-Sb6C6Xbx4EUcF-z1ZwUnwGv0yHIdK55O4_T1qYa3hdKBwh6_gbILJz3waQ1ptcMaG3bgIRPLC61dscDeG3oEZVbJPHceyzxF3lQNgdEyJ4zKme5H-CQ6je6kzbd68uzRjV1pnmuGBaoJiX0tpUysIdFqRNhMGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادش به خیر. زمانی که من یه میلیون تومن هم برام نجات دهنده بود، یوبر این شکلی جوابمو داد و هنوز هم اون سه تومن مال 7 ماه پیش اونجاست:)
تازه اونم با قانونی که یهویی گذاشتن.
همون روز ادسنسم رو قطع کردم و کلا حسابشونو از اکانتم حذف کردم.
هیچوقت با همچین شرکت‌هایی کار نکنید</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4827" target="_blank">📅 16:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4826">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPavel Durov(Pavel Durov)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUl9k5Ck7pMvRIMw4YW54Cqsk7rqrug9Mt_7Oi3J0Slclo8qEUHDG9yLcW6blTnDGfDTYu3vZQ2Z0QoJkmnAdR7lZaYVQni9WPDb_H1QhsRjcjxqvL8aSx_4zqElG3K-yQxvv9_3ubx5lz3DJnWEkn9K4Yiw8IX0_wdZraZV0AE3nfltr9_raJ9ZLyZcWLHVdqIjGanLapdqDRfxe8UL-HBYbmnvPaOoBPb5Y4YCa3swwCMzaxSl_LHTkJAFZCGjiFFWMXtY7hui3NcgnW4WftASgHNGFWWwDw7u0ys7fEE22fUl5-Pds_lZMaJ90H_jbXZdSIy7UuVe2CMZ-vhNEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4826" target="_blank">📅 15:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4825">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGUi9X8YCHXj-Fl0OPGC9geSpAR6RRQnsCeOc76eHuadblwAF0XhVNxxezqFg5zpINf7sDE1mwwX0Ha5spmBGljjkpPGZRpLAP69qFynlOt73wNK_iJkEknaV0unQp8l_woWRTBGc8VPXfzD5-ATL8fvlB4CvyASgqOe5t8U8E6G5xWb4t5Pq2B0e-Ez9pvDOSPFaeggNhKSNJEgJCt9yhjAZVeJgDiS-Mlz1jSyFZceAZldc-ZMDkb3dCuQdf7IA5oVpnHTW4EUvKlfMlTHA1Z-gcUvNwHEAuFoqpW8cTZeAde6TJij8VTGMK-YCIlsr2oOdCFmf7JpOM43MR2hYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی گوشی VPN دارید، دیگر لازم نیست برای لپ‌تاپ هم VPN جداگانه تهیه یا تنظیم کنید.
ریپو
Relay
یک ابزاریه که با اسکن یک QR Code، اینترنت گوشی به همراه VPN فعال روی آن را به‌سرعت روی ویندوز به اشتراک می‌گذارد.
اگر زیاد بین گوشی و لپ‌تاپ جابه‌جا می‌شوید یا نمی‌خواهید روی ویندوز VPN جداگانه تنظیم کنید، این پروژه می‌تواند گزینه‌ی کاربردی‌ باشد.
https://github.com/Mahdi-mortazavi/relay
⁠
@RepoFA</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4825" target="_blank">📅 15:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4824">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BhnMMuB8bUhwiL-gaPmq3-OtYr-_rASb5nKNAXraHW6nD4OFVgw0Vt602TmrDXg3i6o__InT8pddCzqkWvM_0SNltVDQReqGRGfqIELeH6Ch_S4zXJxytSOYgoS_fXQM6DdWKkSs0jOWvmfv1Kliuzo2DCMeoJ3N1yP3g0N7WnQ-6qZtRD282oh_oipBXkmuvONMs-QAVzSaOR__2_BgdK3jDHi3_xNiLVoBHPd7dkHksGgTCF25BQyeRHtEMeeT-Mg9pIKuQMvWGfT20Rz9-DkvYq_vfQmJbhKxeWxtf5clsJ8pXO5zifgiBzNyRfXFB5TaeuP8zcspP1IcPNTOoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقااا من رندوم برداشتم از گوگل
برای این ویدئو
اصلا هیچی از F1 نمیدونم
😂
😂</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4824" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4823">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/4823" target="_blank">📅 08:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4822">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sIpDqIB2YxhrHmzictEsIxUMsJHbId4iW5f4E7ZdHvayb9e44FiE_bUhlUHIrJx1IWnYLOZZVZuv4qOTgLk0vulpIfwonfKnWoTASHg9Vxqo0BBy9KlG0PA694vz0XZc3T1tjngFAa5D5JVJbnenRp1aFIMWZRMdnMZGV4MTYSQHQWbvpCjMfMmDkRxvyT7bgDWZL7OY_mT38ijghJ1wnB7R3A1-RMa2vYAL52lb30o-BDwFojjL1TPXq04neUZBjuYf9LGEYP4SD8vlnERlG0imJmB5gNoa0eqydSTeeNSCDwpgkce9jxuI0Hzs5jFa0VnZ3ovCL1M5wQ1C6LeVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4822" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4821">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4821" target="_blank">📅 02:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4820">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hallelujah</div>
  <div class="tg-doc-extra">Leonard Cohen</div>
</div>
<a href="https://t.me/MatinSenPaii/4820" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">00:21</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4820" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4819">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه. همینطور قابلیت ip fronting هم داره و سرعتش…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4819" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4818">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⛏
۲ نکته برای بهبود سرعت WhiteVPN
۱. بعد از اتصال روی دکم
ه اتصال مجدد
کلیک کنید تا به سرور جدید وصل بشید.
۲. همچنین میتونید به صورت دستی تمام سرور هارو پینگ بگیرید و به بهترین سور به انتخاب خودتون وصل بشید.
آموزش تصویری</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4818" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4813">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.6 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4813" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4813" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4812">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4812" target="_blank">📅 11:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4811">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PiCR5er1ZmJBxLeOy89ADYi_-jI62y8MRxeQ3TLZibIoIy1IKsANnnELK-T44MwZ9KmujCcE_O-gU2GdwDRsPNvggDhHwEM12dEAhSFACd8XmqFNP9rPj2ILPOW_kPBB6ik--rzOEk0NpyQA4wARnZGKOznZjtuhC2W6O8gMoJW74B3k_sEM2BxF9pn3Z4lf7vXVB6F4th63av3XWV6PGmPS0gl7H15Fghr5c_elEZCL9rZ6q8wIOFf_GoM8JI5V5EZMHx2lU8124-u6cjfKULsGOsdxDmOx7N6-ZFvlHIFsIX8VvE4RqXF-2yCLRXOP2sWgM8KAVK3-pemGXvzTDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه پرومو رایگانش تموم شد:)</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4811" target="_blank">📅 10:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4810">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YB63srwPCUXrSttwfrM1CXXV5c5aD9WRKPVGe-a_8G2nqL2CQXTjJ847WffWEYG8hutvvW51Cj8Zbr4v8QRNSPevXiMQI9M3A1JsC3d8PKvxbaSgRm0ur-8VmhXDcTDFMCSSB7dXSXE3bxNzuM3vAo4XOZFh2C_1ZWx6vjEsMWF3DAqHTaIG1SPRjnv8QOt20a5BUZbyWbeEid3529vGSM1zmlOiuUvZ4v7ZNMLsdgeJn_s7ED3-LHlg26mG0PFrzoNshPzs6fPxOH_HkYBBfCVggQuO70z_ic1RqM2uTjUCyuMfPusYvNpgKJKqhWFaksyPI9xtE27wA3aayN_QJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان بیشتر مدل‌های دنیا وارد «منطقه کشتار DeepSeek» شدن.
یعنی مدل‌هایی که توانایی‌شون کمتره و قیمت‌شون بالاست، دیگه رقابت سختی دارن و ممکنه کم‌کم کنار برن.
✍️
Ali</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4810" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4809">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4809" target="_blank">📅 06:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4808">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سرعت آپلودش هم عالیه.
قابلیت‌هایی توش پیاده‌سازی شده که از همیشه استیبل‌تر بشه</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4808" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4806">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4806" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4805">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دقیقا این اتفاق برای منم افتاده بود و سه ساعت داشتم میگشتم ببینم کجا پروکسی روشنه که بدون وی‌پی‌ان داره آلمان نشون میده
🫩
🫩
روانیمون کردن</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4805" target="_blank">📅 05:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4804">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Qwen-3.8-preview.html</div>
  <div class="tg-doc-extra">44.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایلی که الان با Qwen رایگان ساختم</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4804" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4803">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Kimi-K3.html</div>
  <div class="tg-doc-extra">41.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4803" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل 4 میلیونی‌ای که توی ویدئو ساختم</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4803" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4802">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4802" target="_blank">📅 04:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4800">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nlphJeN3xO-osl9NPmVELbkNGZIoBUGqEe7BYV6bwjpy7nilVZI5gMARep8ycThRvCOM-_se25vlxrTo9OslehI70cL28WAOcRr73Bop2pL4RSHTl4qsD6pu7slUA7qgVZbsrUc935DCGk6Fwl2LV5eMXKQ2_WlYMJKLdKK4ZXF9RxreQuic0oX7O3qQ9rxrW0Lv55gKfuevHx-J4s7kksoCfzErUiu_dKwTMLXjeVS7lQJVK3Tv89iRhUgXjcFTTXtFqK6DjYDKZmurI1uWKujky_TSXWXanI8dMS0uKiaPIsMA-8tciAvJpMOx0QoMlvT4G9q269wU30f2T--Fmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TsZ6hVaKwyDUzJWOhAkIslJlDpcMwiIrEJ5FUHmoss0gIrAtXdvoEx7DzlrKGcv6hXrnrjBCy35YM0b0lG2X4WslGxCTXhl2y0L5Dy97UU4XxdPV8IgNefjMVY6EYtTGtm0i8Rx9dBpxcFY_i3wA8MT0yiZmzkW34PDxk05tgR8K4kpNw9hF2bzdvaUM_HEBuevIEd29ddzqC21Rl--_dQrQKu1lZ63qiPNUbq7bHlkK9tLYEYEXrz89IIgE_3KFG7p8UiPTnJGRen_vmXaizDvREx-BAyOFDMNxa_gB67b_c__OseLc4cgeeQKiPC_705-bf0pDuF2PgZNLbrbtVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4800" target="_blank">📅 04:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4799">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ebbyixeyl-ZJxEs8ud9hqF-V59vVXddUscax4Ut7n2enU6mLt0g1RRJnF4GcmYhCwpXFueodQ6-y_gtd5SpcfaEa7QJSc9n0htzdOz4rXRZPeCkpec3MabSXcskGkAkXTwRQNL0SB_qMI95uRrfJWCYme3Ho-yslNlTtsyC6_qGX1v5HkJk4FRTUAL9SDZi5Tf5xn-7KtniI6tGKbOk0Qvb83wQx5Y8NfXTrvNQ5hq1cXWJDLNR-F08R7dC7MCezgt7U9HuUhsxcGtV7c8wu_RcRTdhbsfcCd-SJzU0jEaKkGUcdBndnO8bp2a-lHs8VDbQpCOcuz1oZKFTRet6UFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان توی
infron.ai
میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.
ممنون از confesious عزیز بابت معرفی.
فعلا دارم باهاش کار میکنم ببینم چه شکلیه
تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4799" target="_blank">📅 03:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4798">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4798" target="_blank">📅 02:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4797">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت
تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4797" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4796">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-poll">
<h4>📊 از گوشه کنار زیاد میشنوم اینترنت دچار اختلال شده. مال شما چطوره؟</h4>
<ul>
<li>✓ به زور به تلگرام وصلم⚠️</li>
<li>✓ اینترنتم کند تر شده🔴</li>
<li>✓ فرقی نکرده✅</li>
<li>✓ ایران نیستم👌دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4796" target="_blank">📅 01:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4795">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خدا رو شکر توی قطعی نت دستاوردهای بزرگی داشتیم و اپراتورها از وی‌پی‌ان فروش‌ها ضریب دادن رو یاد گرفتن
😑</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4795" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4794">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c9KF_si7E0NsCiMuPc4r8qOoHqKCJekV2M5grdiQfCyHqKkImfS4XP4gIUb01jMXP8u-L_Le_0r3EYOCWZBRM1tFebWlJ2n8hBpL9hQYGVwQkSzhSw0G3CwinzqRkdaUd4PRaNKNVTvGLyGAwJmfHKlg15e4ygICyfRkg-EEyv6T27Dt23qHGo0EKRuGTcPtUebn_-rlSzlI3DnSgFvHrJfeUmElN4CuNqZCcZkspTl6RMMeOkDWdFtjMQC-DtDdNpXiw-0lhLM44cpYaBxqynNL6N9hwNU46DFlNT0roFBJrtuIHui7S6La6IVUQOGm7Opdboki3oA64lkb3HVJpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4794" target="_blank">📅 00:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4793">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4793" target="_blank">📅 00:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4792">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZgMIRZ-PWRbkX8jkw6Qip0Zda3BJ8gsrpMwsgofWSgcWhs73mvG9Jyqt8JA7bpiRGRFn29vafmbaVKI_R14umFN9ZYBa7TUYang-Ml9osAfQEik-y8dg-auwxElPYuupd4wyxU8nFA0De7o0V1UkQAxlOLuCPZrGm68ZeKZW7fPdt6zNOrJrP0kU0QwoOrxFDPGme4mFtnZHxdyjkrUG3_ElCtPcIQWWkrWIg5HYmWZtYJmYRWQWArXAG9yOAq19_TWt6dExoNj_TVeVpl9VohsYup22WXoY-L5qfBZYQ5nyioylsjBAdafwpC2zAjytQfB1TfxUrMmQ0LDoO4y8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4792" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4791">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">به نظرم یه تماس بگیریم باهاشون</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4791" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4790">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج 205.252.xxx.xxx داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4790" target="_blank">📅 00:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4788">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R-cAV_a1nwIS9Bh1E02SNq5n4rKqfB5csTOI0M9EavPTGMKf-4XaqOJaCCnUlSrunF2i8ibdIBnNsGz3RTUHWhogP0G-s_nZ1b4khXSpgT7KFQYN0ltnyUo5VPtAndoVxDxUt-REI24ygVbcbd1kQMsfJNvGxf1Z2emj3Ax0K-ljNR7yakns2BR_F-dtxl14IlHgY5WMmP9xBg5NWkRQs8kteWaKyjFxFhqOodfi7uzAW1_WPaZ3Lh-L-zNvC2cUwjUI88VTpDcFTEzvIxpWrUUV4MBwv80cBzeVDqinAeIgSQpCe2ynyNxsHfmSqtffOUZqTkbNY4zzuDRmsxTMiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zi5VgXJ3QiofwvkA2caE9F1z7NvLCSVKm05d2Kh_qyEi9CxQxwR766hdTi1qiqrgeVrlwD_dev7gPbJ1n_WsOh7ImbFwR60zUhe_9zQ0op_aUW6jO9WaXzCBTj6lOaZErAv-G_ARAcmrY1JLS8y46xMesL-KuZT7KB7pTJQm5DwCIKWXiZXT9cXi9YA02Jb-trGN92DkA2bR-izKTCP7NaSMr9GzFYrqjQPaCK0zadG-AFRe6jIAIh687pnSDbmb_jZMUuP4I0z4BQCI-QhYXjsgcuGr3YA6IoMN79dIhSELGJhxjZMfGkCm-9EKCt3TZ5M5Y3T_Xwanqrf3WK1OJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج
205.252.xxx.xxx
داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل قبل محدوده 80 90 بود الان 140 160 ، درنهایت این وضعیت nat کردن اینترنت در ایران داره به یک روال عادی تبدیل میشه که جای تاسف دارد</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4788" target="_blank">📅 00:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4787">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hmr12TdpBSzvAtBDKc2oWMzmInS2qJM7-HQlqsfMtStduQk8owL1soIgGLptqpE-mETYc7F9-fpgUJw7SGUCnRiXwwQuE7Y_tz2obUwTPd04EyKT_NuNTM1U8lwFbJ0P-cxCsZ8OVgdRRSwSVdq6e_IutpVFqKJXkqByPFZCFIoYyHbeIZ5FYxcn6nzAmh1Nvv5wgh_4ZIxicf-m_S3uiNMq9j-FMGicFfChc7mmUYHS3rLC9qKP86IDYFMmgzkA3uWffQLw8RZSZ4IaT0zoaztRjBIpq_EJtHln1Y8p_qpV_A2d0CNsBszgWFuZ-9IXYe5ZSTziYBlMI_80pwkp2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فریم‌ورک Science One گوگل
💡
گوگل یه فریم‌ورک تحقیقاتی خودمختار و «قابل‌تأیید» معرفی کرده با Chain-of-Evidence — یعنی مدل فقط نتیجه رو نمی‌گه، بلکه زنجیره‌ی شواهد رو هم ارائه می‌ده تا کارش قابل راستی‌آزمایی باشه. قدم خوبی به سمت تحقیق و توسعه "کم‌خطا‌تر" با AI
🔗
https://research.google/blog/science-one-framework-a-verifiable-autonomous-research-framework-via-chain-of-evidence/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4787" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4785">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Oqrp9Db5YYy9L9IFyWVX5FThBoGB3SptC8B-fUjKppjSl30TKfSQoQDP_r_IsEwss-TKd8eUmS-QfGJrvVCnbsIIACpjrzpQ-sJIdGi-zfksNIYOJkCFkBYuNM7kf5rrsw_A_Vh__N32ZVc6UNd6_XfnjV1-jYPAF2PX1oQctn3G534Kj4lrluuo3YdDNldFbkubCCOQ4Kt5S2-xs3wtQyNK7LyobZQSGC4Cdy5lho3Emhe-b10DfFUlK3eQbk-CXJQmJJf2HfJZTA1Q8cfw1rNgO7yObCdVuLH123BqX1T-i-jcRl-2HcmKk9-EPhiVF-HNMT6luOWrhCUevj25YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MZytFFjqQA9yoJ3rNSiF5LF_k2bLnxh7lEqKRce9A0ZgTyniOQwyMq591j0mn_LoSlWALA2w4aftx-64i9M6DeEq99dyj8ajydyR-iD5TgnpfAvtnlHCvjVR57iRxGAfjU-dv-XmdwQ4_nvCh78xeCBJc2PdQpgEeVC50de-ZT4bsV2wl3KDe0U4A6PY1eMNS2V6GF5kKaWGmQRXfiCwGHB4N6SK3LtZIbxamG38uNJnr4E_RfEH56XIIC8R-e3ky72Vq46qX-mI5EKLsVwEFasOM5TFKUFwO62PsPVcSa7MAgAPNptqSI2o2PFgFAcjmxFCecwBSfBn4tvok3Kidw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4785" target="_blank">📅 21:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4784">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/4784" target="_blank">📅 18:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4783">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">برق رفت
🥀</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4783" target="_blank">📅 18:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4782">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">این پرامپت‌های ساخت بازی سه بعدی واقعا به درد نخورن(توی سنجش قدرت واقعی مدل) اما از طرفی اعتیاد آورن. هرچی میرسه زیر دستم پرامپت ویدئو آخری رو بهش میدم ببینم چیکار میکنه
😂</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4782" target="_blank">📅 18:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4781">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4781" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4780">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سلام رفقا
ما به رسم هر سال، نزدیک مدارس که می‌شه پول جمع می‌کنیم و واسه بچه‌های سیستان‌وبلوچستانی که بخاطر وضعیت بد مالی نمی‌تونن ادامه تحصیل کنن کیف‌کفش و لوازم مورد نیاز واسه یک‌سال تحصیلی رو می‌خریم و بهشون میدیم.</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/4780" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4779">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">با پنج دلار ویزا کارت خریدم، ایشالا که کلاهبرداری نیست
😂
اگه خرید کردم و اوکی بود بهتون میگم. برای Claude که حقیقتا جرأت نمی‌کنم</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/4779" target="_blank">📅 08:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4778">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یه هارنس چندنفره برای اجرا کردن Agent‌ها. یعنی چند نفر می‌تونن همزمان روی یه تیم از Agent‌ها کار کنن — یه جور VS Code مولتی‌پلیر ولی برای اجرا و مدیریت agent
👍
🔗
https://github.com/yc-software/qm
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/4778" target="_blank">📅 01:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4777">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4777" target="_blank">📅 00:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4776">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4776" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4775">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">با تینا پارتنرم مشورت کردم و یه سری تصمیمات خیلی عالی گرفتم واسه‌ی کانال و چند ماه آینده
فعلا لو نمیدیم
🎨</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/4775" target="_blank">📅 16:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4774">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">این ویدئوی پرایم واقعا خوب بود مخصوصا راجب این Demo های وان شات https://www.youtube.com/watch?v=LmXU6SEH3Ks  جمله‌ی کلیدیش این بود: The Demo is cool, but not actually a game این یعنی شما نباید با دیدن یه چیزی که یه نفر با ai اومده کدشو زده، یه وقت این توهم…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/MatinSenPaii/4774" target="_blank">📅 04:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4773">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 49K · <a href="https://t.me/MatinSenPaii/4773" target="_blank">📅 04:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4772">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سی‌ان‌ان:
فرماندهی مرکزی ایالات متحده (سنتکام) در حال آماده‌سازی برای یک دوره دو هفته‌ای از بمباران شدید پایگاه‌های موشکی است.</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/MatinSenPaii/4772" target="_blank">📅 03:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4771">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یکی کامنت گذاشته بود، بعد کلی که تایپ کردم راه حلش رو دیدم کامنته غیب شد. رفرش کردم دیدم پاک کرده
😭
خوشحالم که خودت راه حلت رو پیدا کردی مشتی ولی این رسمش نبود</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/4771" target="_blank">📅 03:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4770">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Claude-Free.txt</div>
  <div class="tg-doc-extra">4.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4770" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مربوط به ویدئو بالا</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/4770" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4769">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lQNNPCOfmtDli5REqLDuWOKKmf-cHBt3J_JRputt6WRfJId19eM-dq8ozMaL6_5PpbZASoseWASx93nAZlMJYND85xAuI1LFtr6ad-1i-Nm7YeYnBpJJdNrC24ajBGeMjZBGEErxCDMt6NwhkIrC5A6akFvWBCnnA1KXaak3JKCdyp_RycXcSzYD0FuJOzUz-SWJVS-s7BQPVdV9EondNhzx5KneJ8s-x673qP589EJptQLLzl1dIa2i154zK0RPCvorFhqGvxtyauv5duBMWm4EbegulNBHoiNB1Mr1olz_u-1YjmasbI87scqDNU2RXgQea_jvFWeswQGhVcPDNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/MatinSenPaii/4769" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4768">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bVMHVIV0kwmctWDTyxVnrDHWZeLhFAHxk4YFYUaHWObmUjoLWHJ_EV05XV3AP8He_SXiGuTe0LfLrSPctA_R2vo1oIxSYUvCnAiFfYbWdJ5m8UR8qOOZkQzW563aUWSmZWW64yoXUNd4P1eHepLDbN3b2qmAebkcW6ooLn2utMMaCXO8lqswt01REGH3V4-ckZ9_xX6Etdl-GrcuK6zvpQt-P0n911YJekGcr5y1HlxM2XQwglM9qWvSY-6jUaoRNw5GQ9DOPv23tbj2e07TaFNSU9YhxGL9KZZn2wiOAhAVpa0pxFQA5zQ-Uc81vHzkIuOSsZGkqDY_tTtma1WupQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قراره اولین ویدئوی گیمینگ چنل باشه
😂
😂
(بازی سه بعدی توی یه فایل HTML که 15 دلار پول رفته سرش)</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/4768" target="_blank">📅 00:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4767">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یه آموزش باحال AI هم سر همین سایت ادوبی داریم</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/4767" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4766">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.7.0 منتشر شد!
➖
هستهٔ Aether از 1.4.0 به 1.5.0 ارتقا یافت؛ شامل بهبودهای اتصال مجدد، اسکن، پایداری و امنیت SOCKS5.
➖
پشتیبانی کامل Zero Trust اضافه شد: Team، ورود با کد ایمیل، Service Token، Access Token و Gateway سازمانی.
➖
DNS سفارشی…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/4766" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4765">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بچه‌ها اگه خواستید شما هم توی هاگوارتز ثبت نام کنید
من نفر 37 هستم
🥰
https://potterhead.ir/?ref=WL-1B24AC#waitlist</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/4765" target="_blank">📅 00:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4764">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">(با کلاد رایگان زدیمش ولی)</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/4764" target="_blank">📅 00:22 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
