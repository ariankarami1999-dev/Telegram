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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 05:39:25</div>
<hr>

<div class="tg-post" id="msg-7534">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 655 · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsJIrlFf2Yw4HQCpUCyR_LUP38GcIbAXa5Keu8zo2bQhqAXXFfkl6Xiev2QJpc1KrUl7S-05iNJU8SoUGeJlEmNhrKkAg2EXZ9GtoOidLKV1R1ObcXmpxsQZwKXrNqFFrKQ21DT36c8UIUO9GsQgJg-aI4m6LRJUhv-APkkSMniIewZV0MChRwv_BEo3G_lBQ8qrLgg2woPT4fp-Ml6STasnzBgRHTQ-yeAJ7waJEtdOWaLHpwOcCZbrMlAvmhwvefAEQk0qdh7cfm_7600ZAsypjfExGWLyzOo2ontyyo6W81VIi-YMEYFa08iN3rMRh-nJAMx50kGSmLskZmV91g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFrcIHtr6s_UXseiz3ZcizVHVdYZLRrGZxWkD6LDvX4WMan7eqmQAvP5yg3xO8QOuuzmnAQHshaYo5AMPpvALXSuhqoZn076lLbXy3S1lWc_Vl4BcOy9s-IQg4aBB1UINOnvroV3f1_zYm0iyIgHevadUm7cUJlM2GmaB0JG_V42033pd62pw08JSqfuALYIVG2AmeX8LgbY1KxFe8xs68W9vP-0Lu3j9LlW4yolN-V9I_VzcWRuSI-U5BDknEawPcEYHFq0t59SkAGkNeJEBRh9Qr4T4KqS9xCI_jlz5QU9mkjuoXhpAsdgW0o8ZWzPvVN0_eKae_81-KZfMNhUsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjjfFEDnpgwAKBNzXtMB9BIvBkeoPqywWAfzWjTFZ4rjJAVqOn0JogOLYYcAJfS-wzQGtqmSjjk-4kjMZIxo4k1mawIg6px2VufqGKqXgJZQCSA23VgBO2OJREjadHOfKtVsrrCw2F41jZ7Nh2ydVCaTa3cZkHdnkAzGRTIi_pVL6vU6zsWEMDR7oUUN1xJwCG_eKpmTlIgJhXMCPBazs7MxS9xljGZM_bztTgWp21LQxyiyCnZKsafiLLP6GHsEiwFgWaQvYWs5aLhHBXN5vRURunwtxp29wzsRwjZzoy9zHHPNUXbyEhVgVRD-5ZJIalTtBQIhOKCFTiCXZNCFPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7525" target="_blank">📅 20:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7524">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZtw73xIMXVL0VvXg5TQG11Bosf1yEZEjY6AaWYVaAYX0r4PHOFR2AJwzNYUvNL0JufxKC-5QIUs1sVSBlMQzKxGEDDD4HcshW2f1cdpikSOsMkkZVphbD7uhLu7fRwi_c5wMpKL824EYSvxLCQBwR6QxyBRmdG_nDFZFy3BfYULTOXUYS4TmEIAcpzZXu50vBwqqrtEQjtrT7KA1p3K8p-wQ20bMDh8m_7y5CZ9DRdFQTGrP1MoAP7ydw9o32k_XF9MRVCHWOGNfdeUrTI-vshZ4r3MOjPn0K0eQGKEHepTpo9cZ7xO7bzwLWuFWUu_fJZ9pKa1wQjcOfWQ_FblmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7522">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8lDh6Tz5q_TilujWQ-zzlTJok39I5hNLPEoG9WGP6OqofguvvNbukLNe5Xvgb7iNFvfczKOGNPZomdYh848NlaVln1reF-_YQll9eHEjDIjse_NESlqV1n6edmc9C4v6LqfdK5HZVa-LXG5JY1XHL8G5EmPACe9OQCpOjjGJaDf6Zcz9gzGp7Z45oAV_2QOmDCNWaASDhTHfX8BbhiHtkffwPBAKvJNbtA-heHkN9QwdG8oUKF24kIzGU1MMbvWzFfIgxjfSboRnsG2SWGaxSLTAMcZ15IxPQsHfNqZaWmbIiwDclpQZwzB3Pvgkdrs_RN-JHArbX_3csNv_yRi3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-NftJ2Vtp8uMz-_9KhuCzIX65sfLI9uF_HZFAuT94tkvHCRR2Pbcbb9qG-Ojyh132iiK1mt9l4ohXL1Y--DwBQRdvihUqT0zCJEF-x_5n62sJSNvphFbp0khdg9YxkJWgH0mTeD7DxgQt48SlOu3vuzTQd1BUfaWstO7DOUUvfi52FCTsFJLN1TYOhATqPLtNRtuLTFgI__dneIa2qDV_Cvg-nSvWcZ0uQr7T1WdSDjkOnEDviVk71Z_FzO8I8cAOgt8uLDxt45jxpX3z6ot-9OoUWRuU6_GDJCfHbtjWE_f18O40-Qy5A_Nd7zpP_UHg8EQq7_HpRxVYJ8nqnLHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7517" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7514">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDOAPvfwyxyn5rbSK83mrCA56F_jJaJS8LjwHa4MVxUSFcN_feGHbZQJdA5gm6-Gxif_v5J8zDsVvKJzrfF9WUZjUb4OUhfH_RcJGT5ylkQ6ronx5GuNWBGnCKXHs7v5M4CkccYdCWISle2EptNiKRF2SC7spkyEcsNnlyxQqPzS_xSwJ6vqC8f3ymZVCWxeYoxfqVHa4IoW0P-ZZzHYcOxybgByd4lnk-dg0z2JS0g4YJaffh4lZGO5MuGxXJtUltUzW3l3OtZhv3833fQ0yJ_a4Ykrf7xR1U1twfnFE8q6YTnM6ldecO43xBpWfFOgYii0I8hZPq2_dG41H7px5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKQHPJBLxu1Vc3WSZlL_r9bVYkwy-Zj7OjuUjyVVd7_DZPp5u7gAChhtqDDDag5L1GprYoVs2XRZnzoO7yH1Ppr-kRGV-PVN8vH55UjyxCvaF1i5xWtCjjA8EkGS1nDHQOyCStqou4c0gi8d2L4G30QTt2JJT_kcwCBuCqssN_qan90S7Cxofumcf6Fx6yFt1CLHqY8P1lQ_VVi3VtCbITooFCRHsXYVDOj8kkgwPEHVnwza3eMFgEGrXuNXuHPAUBBZyy4L2OHQ2quUHX_NXUDN-lW7Adz6BJKQAb4WsekZFHBCeyjp25jyrVhEzyx70QL9GW0zjL3KPH0nJZB0JA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=q3QEw9KD4ygh8OSKteEk2bo9WDFHIO8yXYEd4tRO1tQxS0q7elk31GU0c0jXk5TaAF7c5a3TQievlzQhzELGk9HDWQ3ftF5qAt9tqayVNFoqoiM4y8QI458h4jKnr6uTdjpPejV5GonQ4ganIKp6_WfcAvfyCyPu8ZaCBhkQFQTS5pYryTNI3VXEq9FHmcr8Tx0zNuYZlX_gf1W67IZdL9q5vm_H5AUcbUTZK1nOo9hq2Yaj_4mbpqqtPUGhXg20gjegfR0Qu7kM8uqQhhMfGR8uA5pBwq-2B09Bu936YfJiVx8jz09kzcPj9-4FExYpX54FSDiHZLmTTMjNHX6jUIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=q3QEw9KD4ygh8OSKteEk2bo9WDFHIO8yXYEd4tRO1tQxS0q7elk31GU0c0jXk5TaAF7c5a3TQievlzQhzELGk9HDWQ3ftF5qAt9tqayVNFoqoiM4y8QI458h4jKnr6uTdjpPejV5GonQ4ganIKp6_WfcAvfyCyPu8ZaCBhkQFQTS5pYryTNI3VXEq9FHmcr8Tx0zNuYZlX_gf1W67IZdL9q5vm_H5AUcbUTZK1nOo9hq2Yaj_4mbpqqtPUGhXg20gjegfR0Qu7kM8uqQhhMfGR8uA5pBwq-2B09Bu936YfJiVx8jz09kzcPj9-4FExYpX54FSDiHZLmTTMjNHX6jUIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7512" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7511">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7509">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7509" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7508">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7506">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7506" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7505">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MY88h79ZQv4IqaEvN1gJlm_lWtmNg426YXF3Msx7RxuhJbyIZijFHVkEq5RZWwUWLtpxHUU-DYfYqb9778S_5Ze-3PLUfY4rNmUwx-3Eo1xKBmtmHa_LsrRNdOxY1E6elbxMowJALIsr68HcZWQklK0y_AQPMYRxH5BNrepzTfvs13P8nkzg7FrtlbntCmieSkDe7iqqE01Rx52TMj1J213Qtlg0QsBwJ99ZmpcBqC4aKPilovu5dcEx-uDhmx66q3yeXCD0ObFrsU6QEsxSVs4UVq6SX0VAHWXwWw4f1w05xjRPIU24cIGJjds8j-B08-CQs34Y9U-OH3CvnRGALQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3QxsAPQd5mE4opDmG5oRVdQ6x8z1uEhTqeujhPNB7pssAQMMEqOWWW9kbDi2mNG7aNwQq8DpwLG2HvgB6a9uwgdb1ysrNTCoW7jvOb5QDUv6vXu_Lu5SlFVsruZDNGxffE0r6LBepdJYG4shaSOjR1id3XTe0_jRHsnOO9vQF_LAF0SWH12_Y5au_QzhpIL-eB8_M15IM_TgRfj4WM8MynwxKq8vwV6hv4HKTNAFLed7emqLtP96G1nWCU4NrfvjR7Gka3F5iYkcXOkdQjzMldNsD1IQwwjx9obGMeZ9yVaI1zaUKlaaYAkt1rC661cSPhsa7l09BV-gbCkdvabfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7504" target="_blank">📅 13:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7503">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7503" target="_blank">📅 11:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7502">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhqACfw2wmbRNzMyUSU4GyvAcQiaSkc3_pOPeSGhlyS_uquk_lgzNZnLgtyrTVr4EJp4Cg9mF48gnpSAUXUbPrOylJKNx8Oa_8CDtQSKg7imToQLxuSI_n_vpWpSVczL0ukfUfKd9dxd9JsMkHOfDzi83FRq8XZ1jLh7RVfZRJvfUFnlp0GrAQ-fYD08a9Uz9CBX63RLOUOAqLxozfoLXIuSEV1_NRCSXudFahrT0t1JGgmdOXdVQG_gaRaQVC4sh2f1UdqYufGWwpD8nstFIq6lW_xBbuFw7OZN1s3EY4YoVnW105zmOm_XEIK8l1ier8qmT34CWg2SyFU6u8MjWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7502" target="_blank">📅 10:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7500">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7500" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7499">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7499" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7498">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7498" target="_blank">📅 22:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7497">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7497" target="_blank">📅 19:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7496">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEjvq6TdxAIaFiPG67VoxrBGpKevyZkAgRqYNH1HEHoXczGIbMF_4lR8X8ndqLG3_p4TJmALs5Se9O8WgHLk-UjZIfAFrUpHJNou8F3ys4ms2ZnCizjuKgsBMVH4-T8M-_J7DC10woSYHbCxD5ytasaNWo9Y5DIFDgUzZYJoQJE6wJSi5LsA8F9HqGjuOPwuRJGn-rg-eAMkGusllTBhHHoE_b7CiReBSL1X4KMU7oZXagVvlmyr74oxvGeX6aWDSFOZjjuaBp6aMNz-auPX4gZPkz-doZjo-aO6WyaQTa3AjUyJqaUuM8C-H_Gp2QzcG03oyT-jAYE_tGA2wynYGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7496" target="_blank">📅 17:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7495">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=uRPks-lAxvi3ZHIvgpxiU657WCnxlai7uUvg5ZSPwRuz54Q5FIs80pGF1VL_utlfx-X8eYtVIXfv9LbCsgQL-CS98BuZJ_gEBDxB7dXB-UCZ_aa4FwtGcUsvT29qFQjWJcHf8QRP9lUJjWnIcHejxxjwkG-mLddOMcg5DLROYEGGCOBVUvpXxEYQZsT1S3q1cpt6JJVYyLWBBdEZHNnEUVp88h7AhGTcrDyYQxV-VFuosHcbmdvX9dPjjXJThqBTQbtXPNQXl8Sxvx-6X_cuT8QgJNrRSSZ3fLTN6bQVo_OXzKz5phGtXDIRvwxDJjTBjWonXL_478a49fwAzP1gmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=uRPks-lAxvi3ZHIvgpxiU657WCnxlai7uUvg5ZSPwRuz54Q5FIs80pGF1VL_utlfx-X8eYtVIXfv9LbCsgQL-CS98BuZJ_gEBDxB7dXB-UCZ_aa4FwtGcUsvT29qFQjWJcHf8QRP9lUJjWnIcHejxxjwkG-mLddOMcg5DLROYEGGCOBVUvpXxEYQZsT1S3q1cpt6JJVYyLWBBdEZHNnEUVp88h7AhGTcrDyYQxV-VFuosHcbmdvX9dPjjXJThqBTQbtXPNQXl8Sxvx-6X_cuT8QgJNrRSSZ3fLTN6bQVo_OXzKz5phGtXDIRvwxDJjTBjWonXL_478a49fwAzP1gmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7495" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7494">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snHIIChz6f2AyDEatYFDoTW6HQD9u8ECEjyql914fkVhgXV-ZGzm2RL8ggFWUbfEb5tBzuJVvGhUvGHODy6J-nTypWOG5xYSRMtltwDoy1FPaOkPBEiaRK9ChDsCorYJWX8NBgiD5hXZhhxnFlkc4nzm09_vejM3tUemFdvw_q9Fe9QHhw2D3dqg3j5Amc6asP8Ip04uEDaVydecWBVlYfVSC-BjnBADXR6lmx8le0z9Ec9wfnBEMoSsyQoZItIRlZybWj0GFfmuU5gt56qu0C_t_JEJFXan7btVfvxR-SS_hyEzc5e8H4uqOrwah8YwD6MVWbGg-BE6dyBxwvmHXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7494" target="_blank">📅 13:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7493">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAYgaXeNzZCgG5H9JLtR4bBekplCfrawEUt45Vw8O8Gn1pUZrlorddX_kkOc5aR2e8mlISi3KSCMb9aHWQRIUlSeCqtqOsdEazt8QtOXKvrZZqhoaE-J21SXItYKtUELM8JV66cJB91iuZRYDD34hzTxuodMPctchMyXlsKbtsS5XI9HuwHpV_cB454-WJTnZ_hvXfd7Z_PudsqeYhB3cTThXzBTi4Ly9jv2UDbjeWTWKP2sa80AyqkC2loVbRUd2XgYIQ1_dsk8-i9bNhVnR04U1_zu0nsK5947hBdUIiz_m8MBNTtlcTdCIBEQ3EnpFnq08BUhEjui3iCw37KV3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7493" target="_blank">📅 12:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7492">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=oo9ve-PPMWUHqTaagMpBqyqQl4ANRm0hPAc94aAGMPoH32WomWE9iRfEnNK-W625QZOzd8TJtjC5dDfA7STYszk0V0pA5MGc_LLzXKUhZTdOEBNxw49_q74ue_mTjaPXROlxTST2g5atNrCvt0b18O-j5kNWPmVXIScfUO_hWaMIov3AxgMZbUDMAyXdTilm4FoQXdodj422H0uCkxncHoju1nsIXYGBdLwOOJ_mWPpTbIqqQ_Ny2B2lol3-ojvMV-HaOxjsejhRm-51QabMMmSkyTXbFrCVFZfXf9ysPAxAtRwst77_Gn9CBRWNF4u4b5W78kKiN9SCK2ltSsFIfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=oo9ve-PPMWUHqTaagMpBqyqQl4ANRm0hPAc94aAGMPoH32WomWE9iRfEnNK-W625QZOzd8TJtjC5dDfA7STYszk0V0pA5MGc_LLzXKUhZTdOEBNxw49_q74ue_mTjaPXROlxTST2g5atNrCvt0b18O-j5kNWPmVXIScfUO_hWaMIov3AxgMZbUDMAyXdTilm4FoQXdodj422H0uCkxncHoju1nsIXYGBdLwOOJ_mWPpTbIqqQ_Ny2B2lol3-ojvMV-HaOxjsejhRm-51QabMMmSkyTXbFrCVFZfXf9ysPAxAtRwst77_Gn9CBRWNF4u4b5W78kKiN9SCK2ltSsFIfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7492" target="_blank">📅 12:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7491">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_D7LdwtZ95axac8BMSdVauopaYuvYvqWoJggiK80kWl6ZvnUrG4TRsXRalJXykeeNaqV8wDD1t7c0szjvqNGnFGc86D1nH2v8Ifb5Cz_JDzFrAby9YL5GXDIuL2GwB92Mzxj908slo3N8nSxPsCvTM3upO3lS5JH7K6ByDG2IFJCqIjfF97CqogmKQk1YZi5GjJbeo7WJnr89N2ov9wkr2k2fXxU4WlWnTsls-PLCjLTm0XqVdCXz0muvss9v-fgqoF5A_QtSapwnp4TSGixrhWV6aQBQM-BaPRv7iL3cvPDaKrtaLvV7echGNMAy9VHc1HbZMAG_DgDZLyxcLQJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7491" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7490">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7490" target="_blank">📅 21:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7488">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7488" target="_blank">📅 19:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7487">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYjL-NJu09ReSlBxkKSug2VCXCaqc3OLWDQ-yaMSOm8qgxB-axz1O6rZZ__J-xLurdvGlVFxGEsigh_BDa5L6mgvdNwlwEv3ufVRXLHWM6xAVRigUzpVI4lgdKHY6px3WPOyU2PF5WGRjRRVrJVT3h5GwYx18I5hkDPcamReKe_4ghefIIU8FTaqcBCK6AUcVL7qf0MO4VNPbp0YgDK_2RBwUHKi35fL0hm3VhO3Dpzg6oAf8PotfLogr2KJ36Ar8oriZXlPkwmE2MsETg1j_z5Abib71J9wuseHjoKBfDfX0Eb5dNqan1wswi-9kI_I1wA7HHHoxr3DTjXNw66q3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7487" target="_blank">📅 17:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7485">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W72UArX-ifUNmC3ga5T8xG0FbFVM6kGr3afzfx_6HEldMSwxY66RfZxvxIAMOUbWRj1tMI3I3W4pPR_d4NzxpeSu28Ltht7ZGbwy7wDDsNd_u1Pi-51gr3VHQKw0JZ76_yAG5ytBXBgpGuOR1ZLtql_YqenT_f9UlXLaYtaqYkzljBqd3dBmAZpxYu9sR98b-ETLk31ZQKU7PNEuEJ0fFKDIn-FmuSp1Zcs-aW2CAi9ovGkzrfjlp2T8aYSF3sUhJ4wkgCOHjhaF6ZFJjQuBkT8V2X6RuRrAn5V6YliULeSS_-cCFQHKzf5gN_1oBOZETH4WQCNkdoN2O-J28JzJVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7485" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7484">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFWyawhIPJmm6n8Rtg_CuH8Cqu3F7NM6ySQGWAF7Ql7ZGlxYlnPOw_tEfS0BCqtZEqGxrGoLIvn5GD2jpnj3P5SDon0IFGf3SYNSgolz3zGuRbzB-GHZb0l17tC1lWr7B1a0oyI_0yJLn80OlS0cBGhrbcRuLKP334ha6bILSzX4s6cRypM1RNdd1m83OsSyQmMBwuYwa19-_gtp4AkipWIbSy1N6o687K-0FudgA2KRB9TxwXy7L7Yx-5qkwNG-oqYNmfo9J2K8b5xh8fOCKp0dS_rgF-mLJjSzk5D15JijrsAV38TcAio1gJucwpl2w56ctTG2xGhFUujiQcmvrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7484" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7483">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7483" target="_blank">📅 17:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7482">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/ArchiveTell/7482" target="_blank">📅 23:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7481">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KblaTUkCqHsJplC6znsWobz9JHk_ePem0KWU9CrHpoI4YS2BGhAHy2uUeaHvwDEl0CXTyqjTvIOzLBrmnUyl2VV2dC7tY99-lG6Y3LIbrWTUNaDrrxtQMm2usLoCy1_RdLUOC48KufYIrM26GqY38RAmaDwmUWROdXHWKdub2YsjPuxmEggxN6Xj9AG2aaicp5P3enIcwLab_8Y4aQNlqr4MaKJ9ZEjDru8y96qJ56H4tD2OcdxoK557HDEWrdvg0qsOqlDLeSc0J5a4dv1chj--oyHzxWO8vpwRN8SX3JIHBoASPvLdRCQdzxoBlq6YyltDWPHXGoxKRsafwgRhIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان: امروز از ساعت 12:30 تا 20:30 به…</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7481" target="_blank">📅 15:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7480">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7480" target="_blank">📅 14:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7479">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuma0CEDKXMp2-PmQQeih0pNnj4esM4dbjkyndv98vr4WcTXg7kDTPLo2vfDRJ3XS5MxMvByJdrwaqys1GDGCNjA6ClFDsy3e-A5sINFm_78gI4QJS3u1KX1AIiQU59dlzKl2ABh0OZ2f3wz5IHa8erkh6Frrh9YLSWqanhHBH4fdc2b21i1juj8nO3UIKVoSkiVwQ5q67wGwsnkWSxi6edRsweeAPaiUbx1eyyPsXDycZe6Vp0mE-joB7-J-BNkzY-ngUlfW8hwLEONIgA83Ds1GJEP-KDBbmsTviAxWCQdKxm2JhJT71N8D4YibDNlKgPRxt1XGytsdMVFC-jRRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7479" target="_blank">📅 13:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7478">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7478" target="_blank">📅 22:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7477">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">Gemini 3.7 is out now
😍
از اینجا میتونین رایگان تست کنین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7477" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7476">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/ArchiveTell/7476" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7475">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7475" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7474">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7474" target="_blank">📅 17:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7473">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goi4qEOYFH19k-wjbXFN1vjYjJxbwuf_o7Qi5k2DWA7tpuKHRnt87YA2EjNHC0tQ23Ya8054-2vKx57GserrAMAnOEhUqgpBA6EwpiAk9nplqeUXQq925Eyae953OJ65alACfZmJtXEz9AD3E8fBIB4eJpH411nOlYRUeP36prJ8Ggz11iebUcnyvlLxnFSgmB5b_yv6ZX62AWn8U3EDh7W_QWlnM5c9m86eMN-h7h5JPDb7sm8gZ1fSzohNlEhVVyMEKatN6MQ-lKQrahvtVtm3-9Mkel1mdbnv6bPhUBvGLGowmCAsoZM4GQe5tzKQL5CEHKEzzmvqkLTdsZ1_YQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/ArchiveTell/7473" target="_blank">📅 17:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7472">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8BE8rB-Yndwas5zk-KAd2JG-nRT5dPpmG5875ohZFCjOR3GshYHF1Ur-pKrt9v8fIpSi9bDeFh5-tMqirC34H17aepoPTWWjTVTLLDh7gU_i69wHmXqtNiGgI73LNswR1YWxG4n29XtfP99z0rzX5zH53ovuMOxNyjdhEJpV_khwnLkcLGIurdLdAlXC2XYFT3tXicroFP_cuLiImgTY-0GHKd56sv7Yv0WGnd92FYYwT0txCwUenGLO0Uj1DAFJHwNqeBt-vuw9F9SmrHOigXcOsL5wQY-UdY3ERerW6o_A3IzCCFBhvAmmWcPnQDL_np_ZgdzdngUPkN9C9I2lQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7472" target="_blank">📅 15:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7471">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9LMsY-5Bba8NYpSGd3atOf-lTLVk8Dbg2HDkpbuUtebTpNrwGYi0MdhKsqVPNmTd7xFQV_JkaRchl9MMFb2o_4nGzDjFoifZw3qM40AOtGBFiu7pnjq-g5LEGEkfuDDpQfbG4qaNoGeA2Twd3WXkCQGOr4jZLkb1NAiF7Y5tOXKqFkdkXTKWTqQqVu83XLu7minMvbz5md5zssCqvny83OdMolLwKzfEq2y3tjRmidl3wk04dY8tWcGyKeUcixo3NNUortrc5dEfFaH5bY0gFjpqQTS_x0jfkjJ5xXaptGwdPbaZPt1yPwiGb2g_TlHZxjKwHpLeKSU-Iek4zDDPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7471" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7470">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4oSoakAxBB2_QqQIp3LLXl0suNPwLgT40RSxBOYtib5GtzP9QKgGhA2mJtPQaxs1WN3K_Jscy-iAXscfHfkdtB9LRJeZOma5ORVR7ugxBGeg4nE_iXdsLqG4rqgUNsktugcND-Ttb11aq1n2ilOJIc8aFAJMF51W4A2rEhsF4KBq8-ZawU21DXzuduFjLp5vHpFPHMj35hdoCDRblia8-EqBqZHiGYFvfKxQ09yiKPtRGyFcVwh4fBDh0O7b8xPFXTupA1IssIbLB_rb9IBBMN45Mf-ZrHPyn7THedfITWvhHjYXwqhvVzKVAVvLm9cAxyXojNJF1nfY3VuKhtmKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد  قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود ۱.۵ تریلیون پارامتر داره و قراره در آموزش SFT و RL پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:  چند هفته بعد، Grok 4.7 با حدود ۲.۱ تریلیون…</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7470" target="_blank">📅 23:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7469">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">https://t.me/ArchiveTell/7053</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7469" target="_blank">📅 17:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7467">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdLtWDKoVu7Bv17K6KHS97FKVIQncBs4rYz92-AYvIae6Mb75PQ-ZU69SjN3D6Ni6jig0DVJDUKptpMviqbfW1IjRDFmNv2TpzEzZF6KQLVIGM4_JTWEkYLoUP1OBJ9cZMbir9OdwaC0Mrye2dd25oJ6o-pRqCTZG8MGneDOQ5ZI8GaPwOUIaetQhLQAvvdQDzcGJKDY-IQCI87uslTYzSzrVq30SHh1KOAq3RgHvKdd2TWHqM3obLeHkFlOHLvJ5QgXBLFXofX-CywLdjtaT8ZtpsDCWqer57GvEIO1fl200K9eqgXeo6eZUlzOzHKvTcNT3zd_gkZHBrxPBkcABA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7467" target="_blank">📅 15:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7465">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7465" target="_blank">📅 13:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7464">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_QLDaSEI20CPBnHd-QxLl6E0iJ74LqjNIQKpHISveTaQr5BgnQphiNRbJclw2rliI_w_IsYE_kbqseNtQNKH0nuD_BH16lBfEmfPLbfpf8b5aupCg0x1KBaTpW9wPtJjaCkibCfzd4Qp4kZRsqvl6OnKUwXJ_aZCcheVikN8a8blW2fRkbB-9O3Qx8u5ugikqDmG3Q7aqN3Qsqu2AFrw9MvAU0p8zut1ACzIxAleVLyQMBBmuII84lRreKZpk9-57OM5uh_T9mXJzaeGDJqDGgwBld8qAivVMNAjU8ABE1eHGhS6aMRClEiKOgku8BJr1l7RiI-sUbg8zczTDOYVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7464" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7463">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7463" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7460">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-1jdYR95BvXhHRllhLigG58OVzX76QwJz3GDhjFJ4hkApTR_r9sTQI7DxyhumzownuGRJl9FC2bU9mDdgvuUmYUPEMywwk7mEFPMwIpRWydPGky1gaZX_hO4b_RELvymoNOPwyUysasG_xhgu5kGrQEGUqqSJTkLItj_OPzCxv7yNMqeLIRcHYFsgCvTzLNf4VNj5Z1pnlfDa15akMaJW8YROVRQuoKdru6eaic0ddPxqPIMSO1VquPhGYeMi7Bh4fhna-5fmpgOQ-xgpKvYoqZsWhAC2uhPWM_Zml9jjVVzFqfDu33qiqgnMnIToa4uNqxWEcj_bi65o1zZly7bA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7460" target="_blank">📅 16:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7459">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OV-vIPztrO8o-m4TjcF4JQQDHFC3YAMHReiEqRPmqL9Bbg6Y9HKsVN6J0trk4Lr6E7l9BwmMQa8M09KNpvlaMmTvIQZD9v9E4t6cNxn2ym0zFe5OXVbOAJCm8fB3gEYig8J8K-sC3tLHewrKsuS7hD9dZU-tHQ0YbxH5qFk_lHCovAI6I514kkxPjpZ1HTZqFaLdnI0L7qIZ1_nAcdf2XhwdoOTVTRQRw7OuNKe6r-T1413RLt5GQk_WhtjpONR1U80AgIWma9E-WSjnWARZpVX89nFP_jdmQU9_1-OPNce884VL8y_1pGgF6uuwrb4pFRdR_KN8XVep6ReqQ9g4_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7459" target="_blank">📅 13:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7458">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7458" target="_blank">📅 11:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7457">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyrPzY_02yTmtEJc_zsiEVzoLpQLad3v1UjuANhNxiOB_cjRrLMVfNmvEBbBCW4D4c6RBH3LS1nxLocZsj-TetR4DT9ckWKLVClTkDzvrerqHPMwtZs2TVnuvOK9cxgcVBzkPGLtiXEF-ELV7z75HPYvl7sq6qvdknwDqWaa_SoU9d5POVwPhQs1u_S3Gd1BJjsa1gm7MCrGZSvIs8HAzorAOZBf8psxBFpTgs8fyE1BccRYeqXcymC9jVtpJNoc_FYMAWgKHp71MBWyzpMi2DLUkerh11JK8j_c-q50pFlpv16YcXDvPArUZAlw93pcxzHXxKaavBPTjL8NDLIqzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/ArchiveTell/7457" target="_blank">📅 11:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7455">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/ArchiveTell/7455" target="_blank">📅 22:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7454">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/ArchiveTell/7454" target="_blank">📅 20:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7453">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FITO6ieiSUDjHYk1Jk3p3f0wbpEp9DllZNrLSjOfe-XiwjVsNhKIQXc4nApJmIxjXgZwxbAGFB_A5UeiHxgD9cAc6hXkZPB9eNPQJBzYLVMl-34CyKJgN4AeLMjTeIDCao1-_pk4KMLv6KgmkHiWSdzaYPqeNNmWu_VCT7k2fcecFqtcH93blpy-nwXYuOv30MJ3A9kltM9YFrdhC7IlP0p26b36JihCBiEKY0CT-aZR2QbdQkyP8oWfwTUjvWMdBiInuWpKII5pxl5il2mTacSEz_B3g5HGIIY-KQfV4IhO1mzr24D9OL-NAAj1umjX1F3kubZUbmYFxm7CNI9bYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ArchiveTell/7453" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7452">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/ArchiveTell/7452" target="_blank">📅 22:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7450">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/ArchiveTell/7450" target="_blank">📅 18:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7449">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLNiKXxVpHrLMY_qsH_NfugGpsLvuiPrydTmHoH3DH8fWffogcfG797DhHu8blssERZGWmJRpaUmctTyOnqYNo4LT65WaWgQGCy5DxxsUw_Ia0zCORYtrQhA_u6qlJWsqiQxSOY8VFXm-8fG3BPimeWpgro1qlw15kZMbbnN0fD5UqujP2vXAj0PLb9AX2yuREbdwvYi_xoE_ydl8bcnk9hdMa0AShfzzXf7B9QTJwcqXhlb0VDQEX47eLK9V9qQ3r8sa9tHb1f6vP0pCUAKbH_ph6uebcjWhoJqWGSeiZtTumw40aXkY2VnGHPfnDj8cseaQOdUebl07qag240J8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/ArchiveTell/7449" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7448">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6Yc9tzBehDns_Cd_3LBv6ft17j6elyTNnNlrtgNYIzXOhEvWBqF3-u2eTgmSf9hE7wQFFFTIEpiBJhyPEFD5lMyStrYbFo-J29pyBhGl0lPfQbMBrj-Gdb-1rL8JtqOMURE6I4VpHpnBymFkN7iHfkALp1Z_nJ860K4IrT1RLq-KePEUEKcR1hTqAGm5rVTXNGlkijh2_TlC8j1cLi2Rz58Xn-FXPttnKvygz6OpZRDCCXNVhulbR3zrAqO5JUlukJkevYVzyN1HIdfHyvbeHUwm_Dkr0SmylB6r0XGSiwRCy3Nib6ayvr6xfhVoiObHDPIqS5EoAlPl0Fp2zujWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/ArchiveTell/7448" target="_blank">📅 18:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7447">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFtRKNvMqBQXl4NwXxSxl7x3xIkCLGubGVRnaOCtKWFUBRIYQZWg8aRrnh1Be-Yk_Fc66Ya_Te7WkKGS6z6T1BLuylw0IRJILmCAcq_5OC3jsfW6VgYzpRM8VgwFNgjFHmPXPp_BEHTQr3LGkc42lcp7Rf-K-NCrzDJUpYpDkWty7B4kP16nle-FAVySJX83lm-mU36YfNsvJ3b07aVMXpCZ3MEOlPZMJRu4QWYdC-3AWytlfdgk_vsNnIGhpVhrvSH3PYASCmmjMyytvCYsZvB7HtZQaTXOklEp7o1sGjs7Eb811Sa3f-BE0RKL1BKvOGp_4rJdHeneS5U4i8Owmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/ArchiveTell/7447" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7446">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHctJDT0IFzP1zf-cImDXv5mQe_tQSK7jA1l8oY-PyfdFYObgiMHoonJ2sLsBIkF4mNYNe0J27MmGMIgWSdYTGEwAYlMW_NUe3KTtDU8TwTjjgd2vaPiMqEN33_6kPHn0tImoc6INJNwrcrFt_l-2micIl1_aALn4zAueeqNjSyiw9AcI71FqEhFc3X6dhzr44lrdLqiNeMxq42T6L25A_sfKl7pTtXhxEONJEhM3nrhNy9Z9TWmagd_MO9_vuhRSpaDZXyN_u-5FYEbH4tigxIvn3AtjqC6vfSRvTAPMVzG2kSAaRt16H1pd8VV6Tw4iuKZa7gWPsGoiDAKXByf_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/ArchiveTell/7446" target="_blank">📅 13:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7445">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/ArchiveTell/7445" target="_blank">📅 20:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7444">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=bIXGbohYvOZ2YdcNfcVKKM8jt6O6sBWNxwBKYmHifqHiG5r6CEWS41CUM7k8gmwbHi8wjamHzMUEFbgXrPcMIGY747tVdDjIvjoEjwgRRs5FymHvafhtet3BKj_Sa35FglYanqdNimzuTx_dlEvu_5uckcpxxU4uDiWjvRLL6wYALQDOPUc3pPDMEAHphnzBTnUYw6AeYXYxE5zeWLPIUqMmvRnH-O0j17Pje_OPuMHIvXV30LvMQEijye3jgHKLd4MA7Ji2Iz4-DcDQxNAW2wT_AfqBoV5vTp7iTvTpeYO7bLEmgEd7awX6WnpedIp5caybdh8njgvX9QfOnpGeuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=bIXGbohYvOZ2YdcNfcVKKM8jt6O6sBWNxwBKYmHifqHiG5r6CEWS41CUM7k8gmwbHi8wjamHzMUEFbgXrPcMIGY747tVdDjIvjoEjwgRRs5FymHvafhtet3BKj_Sa35FglYanqdNimzuTx_dlEvu_5uckcpxxU4uDiWjvRLL6wYALQDOPUc3pPDMEAHphnzBTnUYw6AeYXYxE5zeWLPIUqMmvRnH-O0j17Pje_OPuMHIvXV30LvMQEijye3jgHKLd4MA7Ji2Iz4-DcDQxNAW2wT_AfqBoV5vTp7iTvTpeYO7bLEmgEd7awX6WnpedIp5caybdh8njgvX9QfOnpGeuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/ArchiveTell/7444" target="_blank">📅 18:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7443">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/ArchiveTell/7443" target="_blank">📅 17:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7442">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فرار از زندان قسمت 3 رو بزاریم؟
تو این قسمت Sonnet 4.6 و Haiku 4.5 از زندان فرار میکنن
😁</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/ArchiveTell/7442" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7441">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLJcqDb8XJAmwjJmZO76Wu2RsIR7Fntg3xZJlHtcFwdLu_ripY0SCQZEJu-c7GEQz5Z8ifcrIDZ4wtvMPiQ-faFH-w2ZJDbK8lyuwZm71qxpDkRgRkz28x0D2pc1769Ak20Mv_ALrlgxvsRy04d9x3dJVmt7tLKPSrkSU81ALD0OOxQaIdHPqHg3FAOmCtdXioibxjUh4JBLoPBJdtMa2aP6-AtmXrlo7gTC6eLSjNkVDUpHcap10x92fA12oAoBw1PVEVap9pxDe9pJu23TE61zFJU4DdeaQR8K_m0r8azXwENOrU4eICOVhrhr-Kv8MYZFGk6JO_Pg0RApwIxdig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/ArchiveTell/7441" target="_blank">📅 14:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7440">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/ArchiveTell/7440" target="_blank">📅 22:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7439">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شرمنده دوستان
😢
بالا باشین
تا چندی بعد فرار از زندان flash و glm رو میذاریم
❤️‍🔥
بدون رفرال
🥹</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/ArchiveTell/7439" target="_blank">📅 22:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7432">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=YhGZ31kaUVpt2kjrmPU83AQ3nsJtp-nLDBts46kZEOk-xBs6Rc0mkTzixltV7VB26ejgS1-Va4s4qbNOg-knPQuufyM54m0PZizVR1FRhbsr0xo-KvE-UJG_B0NmTukZds3QglsSNnFkdqr1L5HMUzIOnLTYqAJhV5q9oWuTlkZJQDZZrKl4pPwbnOZzz-rB1ycbSOcjWbovjtC-HTvmgiemqy4D-YNsFRqfvSEyALYVZUr4BslP6oBvAfi4WwOWv5T5n9wDnJa4LYkkzLbR9lGqJOq7WDHCi9U2ahzdDH3Olaa631JLyyE0Pj-0eBITW_M_G5bCFWV_OR9u9rGxoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=YhGZ31kaUVpt2kjrmPU83AQ3nsJtp-nLDBts46kZEOk-xBs6Rc0mkTzixltV7VB26ejgS1-Va4s4qbNOg-knPQuufyM54m0PZizVR1FRhbsr0xo-KvE-UJG_B0NmTukZds3QglsSNnFkdqr1L5HMUzIOnLTYqAJhV5q9oWuTlkZJQDZZrKl4pPwbnOZzz-rB1ycbSOcjWbovjtC-HTvmgiemqy4D-YNsFRqfvSEyALYVZUr4BslP6oBvAfi4WwOWv5T5n9wDnJa4LYkkzLbR9lGqJOq7WDHCi9U2ahzdDH3Olaa631JLyyE0Pj-0eBITW_M_G5bCFWV_OR9u9rGxoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/ArchiveTell/7432" target="_blank">📅 19:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7431">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZ1riOjEB6DQTtKnoIx4YlYyb_b365USj7DedXOcHribCixaLn4R3qJMwwdqAeij7cXF6PgQ6fwYZR-8w9cc_QQEjbQKZKv5GihJXGp1W3MACwS-MtcvUUjbQvteYz68BZMGn8TXN_9p18bw3aptXnPpAsLtnHFHn2g7VveNmBjMKhNxN6YDMKiu3jN2RjKJC9ARAe_1SyPvMFK2YzRZKXIe9p44ILB8ivNKNdZhu6AvW9LNUUELQ0xMxkG3QGeASUHnh_wEuNrs5Gbf6VlzqXboQYeX8I3zp52bDQgwjCQhJo2SZuppA3jubX9xYVEtiSL9sgl_-BFbPrMoLOm6gA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/ArchiveTell/7431" target="_blank">📅 19:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7430">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZigqtajsOIa-6IX9kZCB3cRzwd4lpy25lLWC7RzQqHaHoPH1y50BZc9NiYlicjzyz4Lugjp8hE0OoYWJYVg9beiNT_OQGnE0Tak6lRp8JD7ueLmdVp4KKOpFNvTdkoKr2iIVB0qYg-4eXFI7_A4u4HLML1b-QVckpljSQRMpXMV75tv8DUHNBaed_8mKWlNW_DpgSsCXQ3FfrhQsuyd2R6JGDR4DRRSMut6rorlq4f4VKkHux8LEAgbKuB5kLAJrNaNOdokI1XcucyPSQ9o8bYQNJZCgQ2SYvo1lEhZKqC3hOd3uRFpj-keHKVsMjhL2YZmAyQql62OYm9ldTvBIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😺
چت متنی داخل ChatGPT نامحدود و رایگان شد.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7430" target="_blank">📅 18:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7429">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPVBeZ7dIK67Mrl785DZHDN9XydMTHDTLK1SdDfwjOHZWyG-bOA6MIhXuH2KCSMx8bpvUhB3Y7OBF63fF2QLEgunknjQMoTcI8ZR8e2ng8dXgFy0bihA0gxKkhrEM_JeYqF7li9YmhcC7yQyOMfRwzhsUv5rtSPJPuWKcJK7u3id6b_HH1rVrgwtAlOt1gBBgh_6fe5kG5tX6aIY-Z8kMhjAJpBR6CMSWu9zbKkfHuOiZjEltXKUUp4fcYTiUKOdW5raTTIRbaym3-y7Jwl1lLT2CWZX1euUB2_5adlazaDQkVr8UARB5VxsrPyP2kabVgWR6FqsNvej-lWyXKvhOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=bsmYSu95jhR_hyWZsOpM668GcVBAim3QHSQBDDnsXy78DIH3Ngd0LqUwZWPSuidU9QUTr3_HjkEBO6MmOGHzlNNJJNjKOQ-5CJ0UFvtCq1mdrA_qyx-6Gd_wFrkJqwQApSPLfbdQrwyVazc1eqUIfkdqwLJagBu97blEwZVXYmKNIh7czuDRP_RD0lFHgrQ67PUQC_AyE5cibt6YfpVmIMNTjAleW7rUwbIv-koVMqicVlhqGqMZHSyvIDHWkJgedeTQKtq0d394ydb-OKPDv6_dHpO7T4vJFfoUs9OJT1pYuhHKRUwTsaO_IYMo7qJmV251lEsx5DCaJaAVMYiNYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=bsmYSu95jhR_hyWZsOpM668GcVBAim3QHSQBDDnsXy78DIH3Ngd0LqUwZWPSuidU9QUTr3_HjkEBO6MmOGHzlNNJJNjKOQ-5CJ0UFvtCq1mdrA_qyx-6Gd_wFrkJqwQApSPLfbdQrwyVazc1eqUIfkdqwLJagBu97blEwZVXYmKNIh7czuDRP_RD0lFHgrQ67PUQC_AyE5cibt6YfpVmIMNTjAleW7rUwbIv-koVMqicVlhqGqMZHSyvIDHWkJgedeTQKtq0d394ydb-OKPDv6_dHpO7T4vJFfoUs9OJT1pYuhHKRUwTsaO_IYMo7qJmV251lEsx5DCaJaAVMYiNYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/ArchiveTell/7428" target="_blank">📅 12:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7426">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMHRqxhceUiYsZi-9XhHA86Ta55RZojwWDJgGV0Jy5lR50Lzbq97Y9nwrtyBMF5TcBSFVFFgtQ7C6CTNC3C2noGgUlnySJjfE_6Yq-y3AYm4gXI12a4uks91k9-AGu0DSY7TUlyECKwOK70JdAPkBKzj0kyQ6QUAcP0ahHnwLiNepD9O9fPXAgvq5t2u-jhnqq7a32vs7a0R22ZRYdpqvgib6McL4aDttLHdwEuunudAiStFaoeO46NYKK7E-_fN64sKeZp2EazEC07AfopyHh11GLD4A9PxS1jO4TbcH0K2QrY139F1v1n_9Gfi8HqkLFcHZo7FfUoek2vPLqN5GA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/ArchiveTell/7426" target="_blank">📅 00:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7424">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRDZoSVDz03k8071vysgY-IVGVLfuIcbUlnGNlagmZhBbG11nXXXKK0088-9PCyxYioI3t8p_0vtRbjTc56-SH8lwMlDrVcJLGfw1K3UPN-mfouo8nHJnzdLVX2x3a46W_PRDiE9iRDJD5opoOUsI5a15f9tPzc8ggIuOMsczfVw52agZ9ZML6U6srgkaG1nqaIn3gjBiB85BeTx3-VC9G2VEBM6zuaSmG_zVM6I3i58j4EdAlx5rqdmSm4FrRtKgPbtBBGLZlJ1cfMtbv14WhhS2sT3ajBe9zQtK0n8IHNpeVf3eoIkKCGZMjp4ML7ZA0rpE-3yF7loFzFkOKxXNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmPQeyUDDik0PexzCGcQt8YXdKYAJL3VYizkDyWHe3Lqikq_hBh2VTXOMifztQwqnPWgXXSRQDLIQjV8sWJK-4DSkZoJ82MzEMIjc-qTWfpJysUXBnRicajvAqKW1_pIC-6EoVM-4KbXylbIZATxzp1iLRSbq4ozPG84KlnxVzb8CLywEr_l_7g5_5CV5ksv6aE3jthqZuFMvzJtc9M1CrfCqo7NTx-xO72PZqu8Kx7mcanBdQh8C5cfYApUuoM5XWGru7HDs-p2HdPTvBqOdTibwkkWxrVI_w-xCOlNV3v4GmkRpJvlXhcDnHArmSM5qdQkIzdAVWHuZMDKLCK5nA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/ArchiveTell/7423" target="_blank">📅 15:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7422">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beV5pclpH55wMAdDLSQM4j3v35t6FAmsEYNd6EkBaFTYJaIpLr94CU2nvRLQcZxkIb85rcN5wovlto6aejPqKqBAKnEInmN3SR_Xe-ZApEWe92gWH7vF3MRTO59j-nouznn_FaqzV7hvZ6JuAzwCFH4qNMgY2QpcQ1kLtQ6J5e70xWsIa5KK0tpiJ4ferfzJOj4XmfgzA5k_MEExhZOyO4uWmy29RHblcK4dJ3G-w_IOrNy3Mbhf7jug8L4rb1DTBc4Ein0bkIiHL_HCtaCoPn-Im3eG5y5kXW9j0sDNWGx6YeeYRs6zK4p3R7MJ8TFOnNpmhALXCUha2e_mbsBwuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ArchiveTell/7422" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7421">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/ArchiveTell/7421" target="_blank">📅 13:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7420">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اگر دنبال کانفیگ میگردید و حال و حوصله گشتن ندارید یه بات پیدا کردم خوراک خودتون
😆
میتونید با رفرال جمع کردن ، گردونه چرخوندن و دیلی چک سابتون رو شارژ کنید
⚡️
🤖
@survpnbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7420" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7418">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/ArchiveTell/7418" target="_blank">📅 00:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7417">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/ArchiveTell/7417" target="_blank">📅 21:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7416">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7416" target="_blank">📅 20:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7415">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvLh7IxkFWeoA6OJvT5uY9V2t6aOjD7mvysPXyHwkLtqiI8jWrnosqHdev-JbFZXVh5O9yXhAhGpfHklWC9zvyl-ewqANnJHT-_X7sFICjUqEDibypyE2ru424B1oraHSM0HFDUmNmgCC2ghQRMEBRHAs5NUTLJUFqG5LFT4xHqe4aw6v0amkZFfZ9Dsnoe1chKfmU-PnUqQLEaC8bCDdqf5JnYAhUrCgj-Hg3f159bJSkB3--LVT-O6d1R5DtSpS3-HRLDsXON1_X8h_1kmbal_3SBCXwxW-71-SaiskqRhTqYS5gtiqZV2CU2WYHPBiupCB3vYPEqWyi7lrf5TWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7415" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7414">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k588RkkygtQ4sMiFfAs_sDH8DoYloTY8yI26sE1dYJvWIKfCV1siVWUPNC8Hya22lCr5rjWCcrjhLVGlmdnXAnSt8QfgCtkO4mrC9S4-gBrJyTSCmQg0fvpaAN81aW04F2FRnu6mvgMYwSm24TeyWi986KMAB_DWQH3GuLcVqYAFyW2KVqpZoXdE4Em4xKVewsUc33QzFNQxO7s2zzLwL0lDqYDnpZEnrmNAjIRBXPcgIOg6R10XuvgKWEQf5Ght9_QYEEWkByZUrViXLyBAM4WLMogVGxnYkufu0EkEhrDpY46jN9fY7HVP-pLgDbBxRaTf4xERsSlN8MgxbXe3WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمینای اسپارک (Gemini Spark)؛ دستیار هوشمند و همیشه‌فعال گوگل
♊️
🔍
بچه‌ها گوگل با «جمینای اسپارک» رسماً داره هوش مصنوعی رو از یه چت‌بات ساده به یه «ایجنت عمل‌گرا» تبدیل می‌کنه! این دستیار کارهای روزمره و گردش‌های کاری شما رو به صورت خودکار پیش می‌بره.
✨
قابلیت‌های خفن اسپارک:
📄
اجرای ساختاریافته:
اهداف شما رو در قالب وظیفه (Task)، زمان‌بندی (Schedule) و مهارت (Skill) دسته‌بندی و اجرا می‌کنه (پشتیبانی از اجرای همزمان ۱۵ وظیفه).
🌐
وب‌گردی خودکار:
می‌تونه کنترل کروم رو به دست بگیره و پروسه‌هایی مثل جستجو تو سایت‌ها یا رزرو رو کاملاً خودش انجام بده!
😨
مدیریت ورک‌اسپیس:
خوندن و ویرایش فایل‌های Docs و Sheets، زمان‌بندی تقویم و مدیریت کامل ایمیل‌ها.
💻
کنترل مک از گوشی:
اگه اپلیکیشن جمینای روی مک نصب باشه، می‌تونید از راه دور (با گوشی) فایل‌های سیستمتون رو بررسی کنید.
🤒
شرایط و محدودیت‌های نسخه بتا:
❤️
فقط برای مشترکین پولی (Google AI Pro و Ultra) با اکانت شخصی (بالای ۱۸ سال) فعاله.
🔛
ویژگی Keep Activity اکانت باید روشن باشه.
❗️
فعلاً از زبان فارسی پشتیبانی نمی‌کنه و تو بعضی مناطق (مثل اروپا و بریتانیا) در دسترس نیست.
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7414" target="_blank">📅 17:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7413">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7PM0DEf7z66KNZyxZBoCAjPI-4tlXzikBH-lEkVBxqfi87oiFYT3U8ME7kjYfF-wcnRDB2e460I0arfEKZ4NEjpZOCNCSvInN43td9Q-Jg_-CdFqytV6fHkuDALbnkOMdz_54kXmi00II41Vm0_T6BI744UqYZJesgVajERijZiudzkyQQBc2Enb5AZqkXCr0o0GDdvpB0pJBx7ZlCuuE7oyicJMbPoX97pcWb6jNM-EjgU51pzcU0Qa8D46gvq22sHQGZFlRKI4bTFsL_1XqVLBqXLvi8CPEWdRhjgxNAtD4kKPijAUpTC2crRJ-LGyWavqbZwzvkIVy_eq_r0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌اندازی سرور اسپیدتست شخصی با OpenSpeedTest
🚀
🌐
〰️
بچه‌ها اگه سرور/VPS دارید، ادمین شبکه هستید، یا کلاً می‌خواد سرعت واقعی کانفیگ‌ها و سرورهای خودتون رو بدون وابستگی به سایت‌های عمومی تست کنید، ابزار
OpenSpeedTest
دقیقاً همون چیزیه که دنبالشید!
🚀
این پروژه یه ابزار متن‌باز و بی‌نهایت سبکه (حجم اسکریپتش کمتر از ۸ کیلوبایته!) که با جاوا اسکریپت خالص و HTML5 نوشته شده و بدون نیاز به هیچ دیتابیس یا فریم‌ورک سنگینی، سرعت آپلود، دانلود و پینگ رو اندازه می‌گیره.
📶
👩‍💻
👩‍💻
✨
چرا این ابزار خیلی خفنه؟
🔺
اجرا روی همه دستگاه‌ها
✅
🔺
نصب بی‌دردسر
✅
🔺
تست فشار (Stress Test)
🔤
🔺
بدون ردگیری
🔞
💡
کاربردش کجاست؟
برای تست سرعت واقعی ارتباط بین دو تا سرور، عیب‌یابی کندی شبکه وای‌فای خونه (LAN)، یا تست کردن افت سرعت موقع استفاده از تانل‌ها و پروکسی‌ها.
📌
👩‍💻
لینک مخزن گیت‌هاب و آموزش نصب
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7413" target="_blank">📅 16:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7412">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔥
یه
پلاگین
به اسم
oh-my-hermes
برای
Hermes Agent
معرفی شده
🏥
این
پلاگین
سعی کرده چند
قابلیت
مختلف رو توی یک جا جمع کنه تا نیاز به نصب چندین
پلاگین
جداگانه
کمتر
بشه
✅
😍
از جمله امکاناتش می‌شه به اینا اشاره کرد:
✔️
هماهنگی کدنویسی و مهارت‌های codemode
✔️
سیستم مصاحبه هدف و پرامپتینگ برای برنامه‌ریزی و مهندسی حلقه (ulw-plan، ulw-goal و Loop Engineering)
✔️
معماری حافظه پیشرفته (شامل Dreaming، Pruning و مدیریت کانتکست)
✔️
سیستم حافظه لایه‌ای (بلندمدت و لایه‌های L0 تا L3)
✔️
متخصص‌های دامنه‌ای و قابلیت‌های تحقیقاتی
⚡️
تنظیمات آماده‌ای هم برای استفاده
سبک و سنگین
داره که می‌شه فیچرها رو
روشن
و
خاموش
کرد
GitHub
🐙
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7412" target="_blank">📅 14:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7411">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCw-7KLWTYYPb9yGM3VAgKs-1YfFFT8CGn2QA88M3wAz8A1jBtO5SEwhNEjg3Q98kpV6AV5tEsDM86vrzrZBEJ6annVMVuAz21ziT97y3C8FSz7tKyM8VXOcj7OIfP9FWt7bXot7YWxblpV2VGH1TqGcpOe2QpOOx9Ppq4vZgj-_d1lSRN5Dno_3MTPn68FSWIo7djziECjFrzX-NCECqmxWaYyx_fkvGAztn1hnMbioiPIYC2pQcIH49Bi6QLz2U1ERmhYuQ-anI6FPaWr4jfYGVT21vTZaWnE5X2qAj0jjpexRre9qDgfK_rJNVEUOghthsW9BXCaku3Yfj08i5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱ میلیارد توکن رایگان  تا ۱۲ آگوست
🚀
🆓
پلتفرم
InferX
یک کمپین محدود راه‌اندازی کرده و تا
۱۲ آگوست
امکان استفاده
رایگان
از برخی
مدل‌های هوش مصنوعی
را فراهم کرده است
💥
از جمله مدل‌های این طرح:
😐
DeepSeek V4 Flash
😐
Gemma 4 31B IT FP8
😐
Qwen 3.6 35B A3B FP8
و چند مدل دیگر
😍
طبق پنل سرویس، برخی از این مدل‌ها با هزینه
صفر دلار ($0)
برای ورودی و خروجی قابل استفاده هستند و می‌توانید آن‌ها را از طریق
API
سازگار با
OpenAI
در ابزارهایی مانند
OpenWebUI
،
OpenCode
،
KiloCode
،
Dify
،
Hermes Agent
و سایر پروژه‌ها به کار بگیرید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7411" target="_blank">📅 12:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7410">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVERfJ-b6MylaT-hHf3QmqFnmveagWi152sDEhus6bYceFlkj5qKNlaDygHcTe5Y3W1cOHbfDOEBxRxNrO1n19jNpTND39qlyYZ8WxhStXvWk8S9F7uzcyrcRyOuXtChimEspmb_rCdZHuLc5BPBIfobrDFKEAaZIV5rI7Q4U2tqzhTjhxLcNvv0zFfy1owzwNiGgg3i_cAvfKb8BUxHduE2tRBOBNqRsC6ZPRAyj84C4Qh5JSxWCkRVNVmxB-6kHFU9AywUgg_r6EPXwtCeJ8yEnjgUs9QCzrRCkBNXZRgV-Pc5Sjgs70zgH6t2Ey5C-N7PqWqn_xVl7K2MeJx73w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی CloudSSH؛ ترمینال قدرتمند Web SSH بر بستر کلادفلر
🎶
📱
پروژه متن‌باز
CloudSSH
یه ابزار Serverless و فوق‌العاده برای اتصال و مدیریت مستقیم سرورها از طریق مرورگره. این پروژه با استفاده از TCP Sockets در Cloudflare Workers، یه تجربه کم‌تاخیر و سریع از اتصال SSH رو ارائه می‌ده!
✨
خلاصه‌ای از ویژگی‌های جذاب:
🔒
کاملاً مستقل و امن:
پیاده‌سازی خالص SSH 2.0 با TypeScript (بدون نیاز به کتابخونه واسط) همراه با رمزنگاری اطلاعاتِ اتصال در مرورگر.
👆
رابط کاربری حرفه‌ای:
ترمینال سریع بر پایه (xterm.js + WebGL) با پشتیبانی از تب‌های همزمان (Multi-tab) و تم‌های متنوع.
📁
مدیریت فایل (SFTP):
رابط گرافیکی کامل برای آپلود، دانلود و مدیریت فایل‌ها با کشیدن و رها کردن (Drag & Drop).
☁️
همگام‌سازی ابری:
پشتیبانی از ورود با اکانت گیت‌هاب (OAuth) برای ذخیره امن کانفیگ سرورها.
🤷‍♂️
دستیار هوش مصنوعی:
پشتیبانی از API مدل‌های OpenAI برای کمک به تحلیل لاگ‌ها و اجرای دستورات لینوکسی (مثل Docker و systemctl).
🐙
لینک مخزن پروژه در گیت‌هاب
🌐
نسخه دموی آنلاین
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7410" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
