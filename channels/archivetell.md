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
<img src="https://cdn4.telesco.pe/file/HhBU0acL8QVs7aFvguatiobFGoJd9Y-YHuHPGRlebS-WlBBhZUkNX0Ks3GI9SagBbdD5NeU_bAwgrD1pMHZblNhNJttQwknu-lIhKYjwLWHCbT7eXlkLi-lnth2hB455712GYSHJXO2H29DPYxx_Yk80MCQ7GlvokO6DL9fjzzAgfybGxO1owP_kQJwyiew48UTlrYKlKMVOfgUIQ0zHnTkarN93YCoIy7Anzyr0CHPUhU-ecZhVvWNTVy-pMHopCt6MgDrSu4aOB66CBtJv7zsBH_jmVM5l-OZlVBQUXbbLssyKwhXndDABGzYJkw6WG_6hR6d2vydbg43Auezc_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.86K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 18:55:36</div>
<hr>

<div class="tg-post" id="msg-7132">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEklcQZ1b9Kox1mHHeQxvVEKR3V3dohaeTYCzHkUjaiPrNWBc5OYcD06TVOdqZTvSqoSeAbeJxrD6xIodE-WcqARgKYSqMMT79Ts8oqHnWQYOkNL1pN-mD5ZUeJ_FEDi-NSqKm8O9EeE9GdfW7bc7bdBY1ES7SSf-sdRUyALjPdhQMkQZpEZTKlQH4lGRaqbmU9oD3B98S08DPKnTTllALSNDmxgBvN0UZqfpzfcBIgEe8D_MsKIYMJcQycO8YtHz-Zmg3FJ_FL6fPof9_kWt-BhTI1SMq594pxXi9ArGngFNUCGOgYo1Zj4-5Xk4FpjsdOZMrzZZSuwuHPcAmW8qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت از دسترس خارج شده یا روی ISP شما فیلتر است؟
🔍
🚧
ابزار NodeLook یک تحلیلگر شبکه برای اندروید است که به این شک همیشگی پایان می‌دهد. این اپلیکیشن با بررسی دقیق ترافیک، مشخص می‌کند که عدم دسترسی به یک وب‌سایت ناشی از سانسور اینترنت است یا خطای سمت سرور.
ویژگی‌های آپدیت 1.4.0:
🛠
تشخیص نوع اختلال:
تفکیک دقیق قطعی‌های سمت سرور (Downtime) از محدودیت‌های ارتباطی فعلی.
⚡️
توسعه بومی و بهینه:
برنامه‌نویسی شده تماماً با Kotlin برای عملکرد سریع در شبکه‌های محدود.
📦
توزیع چندگانه:
پشتیبانی از مخازن F-Droid و IzzyOnDroid همراه با سازگاری کامل با Obtainium.
🔄
بیلد مستمر:
ارائه نسخه‌های Nightly از طریق GitHub Actions برای دسترسی آنی به جدیدترین کدها.
🔓
شفافیت کامل:
پروژه‌ای کاملاً Open Source که تحت لایسنس MIT منتشر می‌شود.
📌
مشاهده مستندات و دانلود از ریپازیتوری گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 219 · <a href="https://t.me/ArchiveTell/7132" target="_blank">📅 18:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7131">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHbEn2RwL8TPgdkCLTAEEStML7cJJC_WhSRow0kFXGbuaK5CnDj5rg1CFcW-xaw5KhZpMwiJr-2lAfl8wubxzmqEjxVMEfvvGr4wWU-9O4g3jBZ3CKGD4ug9T-iolVQdhCEtN6vRLF77yQwaHpUqP78yma6cRZt95uSN8eZ1JwdsPiPWEXhKNMSbetyPkxpJSKo0GZOZsI9FwiSDY0HnEWrI1CSH4_GhnSIMJ6fkImxh9lSEW_-arjYx2EovaJByvHBFFKYBuB1Hb6WSKvs-EzukaYiCgs5Uzz_PdI7OZz4rqh8Epm-JOuKMtO5ZmDefLSfgyCXnPCU5z_mrv-qkjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در CodeBuddy (محصول Tencent Cloud) ثبت‌نام کنید و ۲۰۰۰ امتیاز هدیه بگیرید.
🔹
با ورود روزانه و فعالیت‌ بیش از ۵۰۰۰ امتیاز جمع‌ کنید و به‌صورت رایگان از مدل Kimi K3 استفاده کنید.
🌐
https://codebuddy.cn
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 490 · <a href="https://t.me/ArchiveTell/7131" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7129">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ByL_vblbx6Ccy8-6xHOtO7DOFbkmFLMhG07eIVrB2iUC5qKeaAkl_WicHdi3D0Pc0FDg0WINda13oVt9mQ6qwREH86KdSajFFOOoDuPRK297orwFkIJRRePxI1tyDZsJHHKyTWGrLJcii968wG4As4upitxUv3Hfk9MGLMuwZ1qU-iXAD2LAniNt-Q5Ge0Uk0SDzsxUExdQe9DYpWSVPFenPR8CQPdBZh2qOR-TohZ-E5JP46xDETyeT0DlJQoAVJPMP4z4fBHH1kzKgoHe7WetyHy-VWTh0NejprmxufwMf9xBP997Pqlo_xfBSecDec0LSqOqffrWCjLtzRWZezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/asJNttiFPWCHdRvDftV8EZzrp3po8_qtMq86exYqt7jawDdLKbLbp210-EDEvI9AzJ4c5VmVfeJBROAcNZepW0T3HtXQ5qP_39jD0XygTw1GRPAwhXbWwg3ZrE4XPuoZldO66bpca-xSqbqGUxsRLuIw0EZuJgezcEpiGFomBlDpYiyLjcuC98gbaPddm2vGbpjpktz1Vbfsp5cahHpstrb3RMcF5XOjRdFoc9kaYoMetl6L--yfjt-hL3iG2eoPgb4B27kUO2kN8MdE8_5ad-qnim-SnKAGFwcXvGXLvCvG06_ZcqGQegefsrBgAlG5I9IxxGDPGmeC09RbH_qU_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔄
آپدیت جدید ابزار Obtainium (نسخه ۱.۶.۱۰)
ابزار Obtainium (که بهترین گزینه برای نصب و آپدیت مستقیم اپلیکیشن‌های متن‌باز از گیت‌هاب، بدون نیاز به هیچ مارکتی است) تو آپدیت جدیدش حسابی بهینه‌تر شده؛ بالاخره می‌تونید برنامه‌ها رو برای آپدیت به‌صورت تکی انتخاب کنید، حجم فایل مستقیم روی دکمه نمایش داده میشه و ظاهر برنامه هم خیلی جمع‌وجورتر و تمیزتر شده!
🌐
گیت‌هاب: ImranR98/Obtainium
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 625 · <a href="https://t.me/ArchiveTell/7129" target="_blank">📅 17:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7128">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رفقااا
❤️
یه خواهش کوچیک داریم. اگه از پست‌هامون لذت می‌برید، لطفاً شیرشون کنید. همین یه کار ساده باعث میشه با انگیزه‌تر و پرانرژی‌تر براتون محتوا بسازیم. دمتون گرم که همیشه همراهمونید.
🚀
✨</div>
<div class="tg-footer">👁️ 852 · <a href="https://t.me/ArchiveTell/7128" target="_blank">📅 15:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7127">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏
🚀
200 دلار کریدیت رایگان برای مدل‌های قدرتمند ‌OpenAI⁩
‏آیا می‌خواهید با مدل‌های پیشرفته‌ای مثل
‌GPT-5.6⁩ (نسخه‌های ‌Sol⁩, ‌Terra⁩, ‌Luna)⁩
و
‌GPT-5.5⁩
کار کنید؟ فرصت را از دست ندهید!
💎
‏
📌
نقشه راهِ دریافتِ این هدیه ویژه:
‏
🔹
گام اول:
ورود از طریق لینک اختصاصی
‏
🔹
گام دوم:
انتخاب گزینه
‌Sign up with Username⁩
و تکمیلِ سریع ثبت‌نام.
‏
🔹
گام سوم:
مراجعه به منوی همبرگری و بخش
‌Personal Settings⁩
؛ با فشردنِ دکمه‌ی
‌Checked in today⁩
، کریدیت خود را دریافت کنید!
💰
‏
🎁
نکته طلایی:
این یک فرصتِ تکرارپذیر است! با سر زدنِ روزانه به همین بخش، اعتبارِ بیشتری دریافت کنید.
‏
🔹
گام چهارم:
ورود به بخش
‌Token Management⁩
و ساختِ کلیدِ دسترسی (‌API Key)⁩ برای شروعِ کار.
🔑
🔗
Documentation
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 929 · <a href="https://t.me/ArchiveTell/7127" target="_blank">📅 15:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7126">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🛡
یک نکته بسیار مهم درباره امنیت برنامه‌های معرفی‌شده!  همان‌طور که می‌دانید، بیشتر ابزارهایی که معرفی می‌کنیم (مثل برنامه قبلی) اوپن‌سورس هستند و کدهای آن‌ها به‌صورت شفاف در گیت‌هاب قرار دارد. اما «متن‌باز بودن» به‌تنهایی تضمین‌کننده امنیت مطلق نیست!  قبل…</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/ArchiveTell/7126" target="_blank">📅 11:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7125">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🛡
یک نکته بسیار مهم درباره امنیت برنامه‌های معرفی‌شده!
همان‌طور که می‌دانید، بیشتر ابزارهایی که معرفی می‌کنیم (مثل برنامه قبلی) اوپن‌سورس هستند و کدهای آن‌ها به‌صورت شفاف در گیت‌هاب قرار دارد. اما «متن‌باز بودن» به‌تنهایی تضمین‌کننده امنیت مطلق نیست!
قبل از نصب هر پروژه‌ای از گیت‌هاب (مخصوصاً برنامه‌هایی که دسترسی‌های حساسی مثل Accessibility می‌خواهند)، حتماً خودتان این موارد را بررسی کنید:
🔸
اعتبار پروژه:
به تعداد ستاره‌ها (Stars)، فورک‌ها و کامیت‌های پروژه در گیت‌هاب دقت کنید. پروژه‌های معتبر توسط هزاران نفر بررسی می‌شوند.
🔸
پویایی و مشکلات:
بخش Issues را نگاه کنید تا ببینید کاربران چه مشکلاتی گزارش داده‌اند و آیا توسعه‌دهنده فعال است یا خیر.
🔸
منبع دانلود:
فایل نصب را همیشه و فقط از بخش Releases همان صفحه رسمی گیت‌هاب دانلود کنید.
⚠️
سلب مسئولیت:
هدف ما در این کانال، صرفاً کشف و معرفی جدیدترین و کاربردی‌ترین تکنولوژی‌های روز دنیاست. مسئولیت بررسی نهایی، نصب و دادن دسترسی‌های حساس روی دستگاه‌های شخصی، تماماً بر عهده خود شماست.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/ArchiveTell/7125" target="_blank">📅 11:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7124">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cf_O-aFw8j2JBiM3Trvot6p0BqB80DeDLd09HP3DxbyzgxxV3GVOtn5OsTI6uXfMa6xGgFAlVQxMEOx1v0u87k3Iyxf_GhFW7OGFhuvT1kRZfj8fu2RR35rWRY_kM7KS0tHGy6eT7SC3sSIgNKumK4FR-i4kUnbr9N9AyUBJVBk4_tRuizItqkXppNNokYsumCxAyuMWU67HdE3Hs0SBu5jUwgfIc7aKTp859WJM6tvcL-EuDpGSL4YEvKoEbO89gqytt5b0CifOcRQgplVbetZFYGJjOvP0cn43WQYzD4DnIbLl47Cw-SBx4QinKrxyiNwbpJMm6HvevL914pIBIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
اپلیکیشن OpenDroid
ایجنت هوش مصنوعی اندروید که خودش گوشی را کنترل می‌کند! پیام می‌دهد، برنامه‌ها را اجرا می‌کند و با مدل‌های ابری یا لوکال (مثل Ollama) کار می‌کند.
🌐
گیت‌هاب: yashab-cyber/opendroid
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/ArchiveTell/7124" target="_blank">📅 11:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7123">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6f7RVuEJqzKvz80-aDVhdSk2fbLRpI2zPxTbMXY1xhNCnwLDKj90_-koJvVtOCbSbwnfShTQMbwUqKO8c6yu9Kf_GBP4x-kW2PEqg_mI-lPgTk2mpUpBLJXVYaN5Y_cD_qUMaNFy3eeeJc9CyWkqh8OlahI58cr58_9QWuikM4VLe_Zb5B9snGAmoGTYP8ui9xQzXP3djCK3ok5v7-ZwONeVUZFGN-AHKtrFftqonwkk2V6odyDihnv7nz4wiqKSwD5UJ53SczN-QL9has5ejlRw0DMch-9EnYm0KkFrRhPecwgXy6z5KDc_HRMGhymRLtn0nbvOi-v0_hpXSgV3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
خرید دامنه com. با کمتر از ۳ دلار (فقط برای سال اول) (تست نشده)  یک کد تخفیف عالی برای ثبت دامنه در سایت Spaceship پیدا شده که می‌تونید باهاش دامنه .com رو با قیمت حدود ۲.۷۰ تا ۲.۹۰ دلار (فقط برای سال اول) ثبت کنید. این قیمت حتی برای ساخت یک ایمیل اختصاصی…</div>
<div class="tg-footer">👁️ 921 · <a href="https://t.me/ArchiveTell/7123" target="_blank">📅 11:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7122">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juajtwpxpsEOxtEvdSOyRtX-3mMrk-5HFq3VCGVrxM3uLnBr9qoSeHOvA5YPl3Rq0W3dCRQKE43O0BGSJQvt4v_yJWxUxvXGkQ-eZaZVWGorF4Ua8HbgQz6tS7Zpe3i2LKA3DMPx3a4OfambrwdkgozSjF2G2ORmGBgkEI9dFDFIUBlz2RhSHzTRdGF3lkkDwKuCr6H8TanNCtQmnHwBCOXz18y2V3HwH2lJilwDsAeu4M_KQEGcz6LldTKsBmjKMb0vFsHi-JpNfSM-7r5qHqKdIgV3AM44fMAH259FcfeBilNHAvPGUOIw4Ce3s_HT6ZXevqCIVi5L7yYE3Bb1dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
خرید دامنه
com.
با کمتر از ۳ دلار (فقط برای سال اول) (تست نشده)
یک کد تخفیف عالی برای ثبت دامنه در سایت Spaceship پیدا شده که می‌تونید باهاش دامنه .com رو با قیمت حدود ۲.۷۰ تا ۲.۹۰ دلار (فقط برای سال اول) ثبت کنید. این قیمت حتی برای ساخت یک ایمیل اختصاصی و فوروارد کردن اون (Email Forwarding) هم فوق‌العاده‌ست!
✨
آموزش استفاده:
1️⃣
وارد سایت
https://www.spaceship.com/domain-search/
بشید.
2️⃣
دامنه .com مورد نظرتون رو جستجو و به سبد خرید اضافه کنید.
3️⃣
قبل از پرداخت، در قسمت کد تخفیف عبارت COMPROS رو وارد کنید.
4️⃣
قیمت باید به محدوده ۲.۷۰ تا ۲.۹۰ دلار کاهش پیدا کنه.
نکته: کدهای تخفیف ممکنه هر لحظه غیرفعال بشن، پس اگه نیاز دارید سریع‌تر اقدام کنید. (دامنه‌های ۵ حرفی هم با همین قیمت قابل ثبت هستند!)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 965 · <a href="https://t.me/ArchiveTell/7122" target="_blank">📅 11:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7121">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">📱
اپلیکیشن Aethery؛ نسخه بومی و گرافیکی Aether برای اندروید منتشر شد!  اگر یادتون باشه قبلاً برای استفاده از فیلترشکن Aether روی اندروید باید دست به دامن برنامه Termux می‌شدیم. اما حالا با پروژه Aethery، این ابزار ضدسانسور و خودکار (که نیازی به خرید سرور نداره)…</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/ArchiveTell/7121" target="_blank">📅 10:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7120">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFdJT423CS8RtrEe_5BTEAoroYWVeBoS29oYz2_dWINcMoJBw-jIU2fUkxp-6lZy2DRcb7nNgYAN81l0oVeBftZNd8gjy_XiNJEckoo4WooK0th26YPJDohjCc7E8aO1H-UJJUGDYnf-079INUk_NwMT99Tp_PSyiZdHOHrlsDmA4QOOZM1-v8HA8Fa2ciWkjtvk-KmN9wsLcuupjnURKLXC4od85LC-wjFUxmb-yrsAQpmtup5j8NkMnaU5AplnC8eY8TkxURIH9n53YsCvp5sfTqTPahvC6V_DQNL9cO1PC2IdbI9g8gswwgXe0XCTszevv4Cx2KjX1mZZyA_W2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ابزار MTProxyMax؛ مدیریت همه‌جانبه پراکسی تلگرام
یک اسکریپت همه‌کاره بر پایه موتور قدرتمند telemt که سرور شما را به یک پراکسی فوق‌پیشرفته و ضدسانسور با امکانات کامل تجاری تبدیل می‌کند.
✨
امکانات کلیدی:
🔸
ضدفیلترینگ (FakeTLS V2): دور زدن سیستم‌های فیلترینگ هوشمند (DPI) با شبیه‌سازی دقیق ترافیک وب.
🔸
ربات تلگرامی دستیار: مدیریت کامل سرور، کنترل کاربران و دریافت گزارشات مستقیم از داخل تلگرام.
🔸
کنترل دقیق کاربران: تعیین محدودیت حجم، زمان انقضا و تعداد دستگاه + قابلیت تعریف ساعت‌های مصرف رایگان.
🔸
امنیت و پایداری: کنترل سرعت (QoS)، مسدودسازی اسکنرها، بکاپ ابری و امکان کلاسترینگ (اتصال چند سرور).
💡
مزیت اصلی: نصب فقط با یک دستور! دارای یک پنل ترمینالی (TUI) بسیار ساده که شما را از درگیری با دستورات پیچیده لینوکسی و ابزارهای جانبی بی‌نیاز می‌کند.
🌐
گیت‌هاب: SamNet-dev/MTProxyMax
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/ArchiveTell/7120" target="_blank">📅 02:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7119">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBreak The Barriers</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGM1N3cDXSLDvljfUZw6DHA_jECs92sAAcS615All9m0DR3r1eK_VVCd1Z6pkYLSviey4wntLx7hJHemTJ06jDlxrxkDef7QmmURhBJhScgxszhe75rxsTxKwgGX0DTWZn62NUjW54Jx1JgIxFE2FRxEQD1nO84ZYhekujNb1lxx4Q0LDQ3xTMmOmEX-xKU_8J8in-9gOTNAXUl3ZRtjMCw_yuoAOJOwFJ7dBTL379M6c7sB_L0K8MkAo6R0szGVWyN-KAe1UVoPu-7s36ZyTRn5lAHw85VE8OFOXqMzim3quP_oWQx3pir9aDRgRro_-ovSgUSk_3yTWCsPN0WryQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسی که هیچ هزینه‌ای نداده و فقط متد بقیه رو منتشر می‌کنه، به کسی که صدها دلار برای اینترنت رایگان مردم هزینه کرده میگه «احمق»، «مزخرف» و «پولکی».
در این حدود ٣ ماه قطعی من حدود ٣٠٠ دلار هزینه بابت سرورهام دادم.
سرور و اتصال رایگان، با توییت و فحش تأمین مالی نمیشه.
بعضیا فقط بلدن حرف بزنن، نه اینکه بار واقعی چیزی رو به دوش بکشن.</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7119" target="_blank">📅 00:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7118">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6hQxpJzg6bXFRoUocaFp6_CvA70qVJzu01aBKVlBp5Dvi4NloCAVNNO529OBe6us6bTpIgKvV6jcWUvc_igiI3nTZ-lSsXWbOwv4NAp2CDfqep_u1OtNFgyBhHdgnv6Znc_ihATA44sEMCPAhkWly5BswFGGiZixWgxBJWfKD_NmrxqGKLsDkUaADgUJN-PFcKNzXMDrzszW7r991zXqTRxUSiN_MA74k4R0kpI9uGQeyIMdE63GLhJSqe9QJUAMfbuqud5irvNjEnv7NYd5bH4zJ9DLF10tzrJYc4QRtHfq_Xgt8VYDnXrzYdh0ymL6Iqjzwg9BLESG7ZZ5Dia3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسی کانفیگ با تست میخواد به ایشون پیام بده
t.me/c/1234006192/1364116
گروه چنل آزادنت
کارش درسته همتون میشناسین
سن.پای
۱۱ دی
21 January
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7118" target="_blank">📅 00:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7117">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7117" target="_blank">📅 00:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7116">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xx5lXUU5Pq7PM6mEXzJs-LtR2dFlKJT9N1g3aCN9skzkearFLvCSj3woaSdeuabtE-j5DT8bcGtJ8_w4t2jBduvDOwRvwQJ8kLm3xWM9ebSPeFZW63SQ2QYaU-gUdZWimtIxAfF7I_Qr59eqeG_8GR2sylcVVSj7XHjPybd-BcWomVKZ5toyttCvNH35lkAFniNaF8M83DTklIwLcwxomiQNY3Qed6stCtTDb_3bqNprP-thVLhXcDcKwFnTm9WuSNFmQaEdxN3ujyZGGzvMHAnf1BwKJAfoO_lvvsxU-DY0HPP6aAmn7B-rtkE4C7cE2YxEs0KK2NgE7TDVNrTX4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
ابزار Vane؛ موتور جستجوی هوش مصنوعی شخصی (جایگزین Perplexity)
یک موتور جستجوی کاملاً خصوصی و اوپن‌سورس که روی سیستم خودتان اجرا می‌شود و به ردیابی‌های اطلاعاتی پایان می‌دهد!
✨
امکانات کلیدی:
🔸
پشتیبانی گسترده:
سازگار با مدل‌های لوکال (Ollama) و تجاری (ChatGPT ،Claude و Gemini).
🔸
جواب‌های مستند:
جستجو در وب و مقالات با ذکر منابع دقیق + چت با انواع فایل (PDF و عکس).
🔸
رابط کاربری کامل:
دارای ۳ حالت جستجو (سریع، متعادل، باکیفیت) و ویجت‌های داخلی (آب‌وهوا، ماشین‌حساب و...).
🔸
نصب سریع:
راه‌اندازی بسیار آسان با داکر (Docker).
💡
مزیت اصلی:
۱۰۰٪ رایگان و بدون ردیابی! تاریخچه جستجوها کاملاً آفلاین و روی سخت‌افزار خودتان ذخیره می‌شود.
🌐
گیت‌هاب: vane-search/vane
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7116" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7115">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⚙️
RyTuneX
ابزاری متن‌باز برای بهینه‌سازی ویندوز
✅
اگر احساس می‌کنید ویندوزتان کند شده یا برنامه‌ها و سرویس‌های اضافی منابع سیستم را اشغال کرده‌اند، RyTuneX می‌تواند گزینه‌ی مناسبی باشد
این ابزار که برای
Windows 10
و
Windows 11
توسعه داده شده، امکاناتی مانند بهینه‌سازی تنظیمات ویندوز، حذف برنامه‌های اضافی، افزایش حریم خصوصی، پاک‌سازی فایل‌های غیرضروری و ابزارهای تعمیر سیستم را در یک محیط ساده و مدرن ارائه می‌دهد
✅
💬
این پروژه کاملاً
Open Source
است و اگر به دنبال افزایش کارایی ویندوز هستید، ارزش امتحان کردن را دارد
Github
🌐
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7115" target="_blank">📅 19:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7114">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ftd06WMAni5U9ddrSwgXjfa5MG3tkmbA1oS8ZbLGL4NQodsGhyeJVajF3m4A-rPno9s7Q8ualHcJlAYSddTb0iTnPmyOBxg9PR5Ph8sOO9M8PUMCaQLQLzoxZWtuuWUA77GY3ypQsbhGwBhJ4c4Jzd3ItME3Mz8h1CS-LfeFxpb9KLF5svxCDjEylwJBsYWLPLB1DcdTShZjdAunFOHBQxnlPtqPiojqKrhbbhv2l24j-vIIbjiJFfFey0Yul53gi_KzVBTHs2dGQyaCKocFJH1OX9GtaaBaVd0yeHpbeIoRdHjDfaKj3AWOCrJVmDNCddGl681sdvULXYFdRerxhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">PDFSummarizer.net
v1.1
این ابزار رایگان فایل‌های PDF، پاورپوینت، تصاویر و... رو در چند ثانیه تحلیل میکنه و نکات مهم رو به‌صورت خلاصه و مرتب تحویلت میده.
🌐
https://pdfsummarizer.net/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7114" target="_blank">📅 18:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7113">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLJQTwEcX35YlPNFUDKWtsepQM5b5r-6noMg6waKXeyiHItneBcskh1HdQLNjsUFCnEXGwmnQ6RQc58lVmnmyuTawgYDnrPzPeLyn5OjyCBrpRHfnwjMocE46-P8gKBVNb6W4NRcPQH604ObIAqUQxXB5KdCOiZjbA5_MaTZeOZd2t_B2dL7oBpQFRz8n8rGsTjyTtPvw8DJR48DMxsV6JpzJzyw9KehszOcLJvq8FOH32s1axBHhyXZ-vAHHWjOHTHeywkDcTjaLXkrPRt-YnKbTPgiSOePP6syJo82bwy7sTKaos9nSXmwRzG38KUnd1m8godhJrd9g1cwYfWEdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📧
ساخت بی‌نهایت ایمیل بدون شماره تلفن! (Atomic Mail)
بدون نیاز به شماره موبایل یا اطلاعات شخصی، خیلی سریع ایمیل ناشناس بسازید:
1️⃣
ثبت‌نام:
در سایت روی Create Free Account بزنید و فقط با یک نام ثبت‌نام کنید.
2️⃣
ریکاوری:
به‌جای ایمیل، یک عبارت ۱۲ کلمه‌ای (مثل ولت کریپتو) برای بازیابی بهتون میده.
3️⃣
منوی تنظیمات:
وارد بخش Settings شده و سپس به تب Address and Aliases برید.
4️⃣
مدیریت راحت:
بی‌نهایت آدرس فرعی بسازید؛ پیام همه‌شون میاد به یک اینباکس اصلی!
💡
مزیت:
ایمیل اصلی ناشناس می‌مونه و برای ثبت‌نام تو سایت‌ها نیازی به ساخت اکانت‌های مجزا ندارید.
🎥
ویدیو آموزش کامل
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7113" target="_blank">📅 17:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7112">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a78a415ea.mp4?token=K4ADTYB0gf79hzXOzCplOUUyGqdsuvt1pJGg5K2ZOoPwSqL9FsjcY-GXb174XvdyDxk02TQ27E3ZE7-nYYIfMrP2ExiL4Bfs5IBTfju35FNVqMuIg-8iiTIJO8ocVPWowh1kkGuZcAoKEYkLRV9YThQ2uJB21aPI5IVn7QFdgtPlTR6mh5XM69L8lpEuTxxXUzyQiHFMQIRRVSCz8UCf9xyZb5JnUHKFYcv3Miur32Pf6WiLKzQ-WtuwZ3dhFG2hmX5zYsviyJzwhnHlFSpy_swlESj_TXdMHr-l79dBfvz7PbQqwHoERQMllDzGUJf4MreV_PsCqSsAK6baX72aQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a78a415ea.mp4?token=K4ADTYB0gf79hzXOzCplOUUyGqdsuvt1pJGg5K2ZOoPwSqL9FsjcY-GXb174XvdyDxk02TQ27E3ZE7-nYYIfMrP2ExiL4Bfs5IBTfju35FNVqMuIg-8iiTIJO8ocVPWowh1kkGuZcAoKEYkLRV9YThQ2uJB21aPI5IVn7QFdgtPlTR6mh5XM69L8lpEuTxxXUzyQiHFMQIRRVSCz8UCf9xyZb5JnUHKFYcv3Miur32Pf6WiLKzQ-WtuwZ3dhFG2hmX5zYsviyJzwhnHlFSpy_swlESj_TXdMHr-l79dBfvz7PbQqwHoERQMllDzGUJf4MreV_PsCqSsAK6baX72aQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📦
ابزار ArchiveBox؛ ماشین زمان (Wayback Machine) شخصی شما
یک ابزار اوپن‌سورس و قدرتمند برای ساخت آرشیو دائمی و آفلاین از صفحات وب، مقالات و ویدیوها روی سیستم خودتان؛ حتی محتوایی که محدود شده‌اند!
✨
امکانات کلیدی:
🔸
آرشیو محتوای خصوصی:
امکان ذخیره صفحاتی که نیاز به لاگین دارند (مقالات پولی، شبکه‌های اجتماعی و...).
🔸
ذخیره چندگانه:
ثبت همزمان هر صفحه با فرمت‌های مختلف (HTML ،PDF ،PNG ،TXT و WARC) تا در آینده همیشه قابل اجرا باشد.
🔸
رندر واقعی و استخراج هوشمند:
اجرای کامل سایت‌های جاوااسکریپتی با کرومِ پنهان (Headless Chrome)، دانلود مستقیم ویدیوها با
yt-dlp
و کلون کردن سورس‌کدها.
🔸
ورود خودکار لینک‌ها:
دریافت و آرشیو پیوسته از بوک‌مارک‌ها، هیستوری مرورگر، فیدهای RSS و اکستنشن اختصاصی مرورگر.
💡
برگ برنده:
همه‌چیز ۱۰۰٪ سلف‌هاست (Self-hosted) روی هارد شماست. اگر سایتی از اینترنت پاک شود یا مراجع عمومی در دسترس نباشند، آرشیو شما برای همیشه در امان است!
🌐
گیت‌هاب: ArchiveBox/ArchiveBox
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7112" target="_blank">📅 15:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7111">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3590ba4a.mp4?token=TEw59Wxb1aGKwD1qCQ1O0QkKuqcEv5LAwJuY9CPrr6hijnQYkVv4jGnHfwEi5AXT_7kHSpLvwgG9qJDO21LFmkooeDzL6lK9NIucSktoJxZS8y612FRJfOEb70WD-qfRbP5rOQV6qvm5sbAEi864t5jb6RKWtpH_DOEf7bMMfT5H6WzqIqt-aHV1wT4pG3aSwntzIbu97LBfONPCETWCshiX2NPKhsYyC64wH5k3WPCFpgGehzgVGr1pxxRko9c-2RaMOIigkE69bT91LVBJ78Yt31u5mUYlU3HWtoFVpgM4ABrwh2x6py3WCU9BlumACTvgkTKQsDzO_2p1bVxQAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3590ba4a.mp4?token=TEw59Wxb1aGKwD1qCQ1O0QkKuqcEv5LAwJuY9CPrr6hijnQYkVv4jGnHfwEi5AXT_7kHSpLvwgG9qJDO21LFmkooeDzL6lK9NIucSktoJxZS8y612FRJfOEb70WD-qfRbP5rOQV6qvm5sbAEi864t5jb6RKWtpH_DOEf7bMMfT5H6WzqIqt-aHV1wT4pG3aSwntzIbu97LBfONPCETWCshiX2NPKhsYyC64wH5k3WPCFpgGehzgVGr1pxxRko9c-2RaMOIigkE69bT91LVBJ78Yt31u5mUYlU3HWtoFVpgM4ABrwh2x6py3WCU9BlumACTvgkTKQsDzO_2p1bVxQAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
هشدار امنیتی برای کاربران وردپرس
به‌تازگی آسیب‌پذیری خطرناکی با نام
WP2Shell
در هسته (
Core
)
وردپرس
شناسایی شده است
🤕
این آسیب‌پذیری به مهاجم اجازه می‌دهد در شرایط آسیب‌پذیر، بدون نیاز به نصب افزونه یا قالب مخرب، از طریق نقص موجود در خود وردپرس به سایت نفوذ کرده و در نهایت کنترل آن را به دست بگیرد
🔓
اگر از وردپرس استفاده می‌کنید، در اولین فرصت هسته وردپرس را به آخرین نسخه پایدار به‌روزرسانی کنید. این مشکل در نسخه‌های جدید برطرف شده و آپدیت کردن مهم‌ترین راهکار برای جلوگیری از سوءاستفاده است
🛡
😎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7111" target="_blank">📅 15:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7110">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
:
10 GB
🧭
: حداقل 1 دعوت
👥
: 22/50
💾
: 10 GB
⏰
: 10 روز
🟢
فعال</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7110" target="_blank">📅 14:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7109">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚀
550 دلار کریدیت واقعی برای API بهترین مدل‌های هوش مصنوعی دنیا!
با این کریدیت می‌توانید به مدل‌های قدرتمند زیر دسترسی داشته باشید:
GPT 5.6 Sol | Claude Fable 5 | Kimi K3 | Claude Opus 4.8 | GLM 5.2
نحوه فعال‌سازی
:
نکته : مراقب باشید و اطلاعات حساس در اختیار این سایت نذارید
❌
1. وارد این
سایت
شوید و با اکانت GitHub لاگین کنید.
🔐
2. از منوی بالا وارد بخش Settings شوید.
⚙️
3. در قسمت Redeem Code، این کدها را به‌ترتیب وارد کنید:
IamSorry
DataWipe
💵
ارزش هر کد: 250 دلار
1. سپس به بخش
API Keys
بروید و یک کلید API جدید بسازید.
🔑
2. از
اینجا
مدل‌های موجود را بررسی کنید و شروع به استفاده کنید.
✨
🎉
به خوشی استفاده کنید!
🔗
Docs
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7109" target="_blank">📅 13:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7108">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSlaPPYlBWpQYS9dHo-wPGuCunzX6E2afJ9mdMIokDsMtZcmyJ6A6Vrrslsqq8RcgbjQDbksXImc0mZoY5o58gVw8ks7MMy6fEvzsxC-OK9JQ3kZziFXNPgGsUXux9LQGdgYyTw1L0sANyHhyhxQ_39oAZcRSC0HaE75CLvAVyLhxQipclh6S2Igiqzda5bjIU5jpvUsPKz33ENl8g3okXWwFwLPWd1DPqbEIMqhydpEO-guJ4iRXRLD5vt34YRbqEMneiA4UfOhooVDnGzcQELpBkmHBP1Ymt_oGESYwdTfS9FBIXxr6yFlplYhenvwSS5HEiyBt9_9-BtcMHTelw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
با ‌‌Hyper Research⁩⁩، ابزارِ قدرتمندِ ‌‌Claude Code⁩⁩، پروژه‌های تحقیقاتی‌تان را به یک تیمِ متخصصِ ۱۶ مرحله‌ای بسپارید. این سیستم فقط اطلاعات جمع نمی‌کند؛ بلکه با «منطقِ تقابلی»، فرضیاتِ خود را به چالش می‌کشد تا سوگیری‌ها را به صفر برساند.
🎯
‏
🔹
مهندسیِ پرسش:
تبدیلِ ابهاماتِ ذهنی به ساختارهایِ عملیاتیِ دقیق.
‏
🔹
فیلتراسیونِ هوشمند:
غربالگریِ منابع و اعتبارسنجیِ داده‌ها بر پایهٔ مستنداتِ معتبر.
‏
🔹
دیالکتیکِ دیجیتال:
به چالش کشیدنِ فرضیات از طریقِ تحلیلِ تضادها برای دستیابی به حقیقتِ عینی.
‏
🔹
خروجیِ استراتژیک:
تدوینِ گزارش‌های جامع با رعایتِ دقیقِ پروتکل‌هایِ آکادمیک.
🔗
‏
لینکِ گیت‌هاب ‌
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7108" target="_blank">📅 12:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7107">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImIjyr4h92pVsaAyL7Gb_m3-yu0v9VsqvRDOtnvQW63HnOIomAhvBrA4ngJDLgpJQzA4EyLsnQESWC_kiUa_QaeUq-z80oV_AlftBFU9pEY96vy5H4urnIoW7UvQdY9uUSWz0bv9CzKhS-pqe1gO6igmAFg7eltpC-sBTwZT4Uyqg9Jfb5Ov3kC6YoAZn0HEYBXIY9WY9BQBHBBLD_dzfu6TDf7HYsQ0GarO4o8osQn8YHBuNLDFXlrSDKI61xTGbwwHMtqkKZsWN7FEo_J3AD_aPCd6bPAFvA9yEuOUSZO0pTC_Ya3ZeUcRB5nqtLGdqTc739irMGg5-Eyf_kNVzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
پروژه Mobian؛ سیستم‌عامل لینوکسی (جایگزین آزاد اندروید)
یک سیستم‌عامل متن‌باز بر پایه دبیان که تبلت‌ها و لپ‌تاپ‌های لمسی را به دیوایسی امن و کاملاً دور از ردیاب‌های گوگل تبدیل می‌کند.
✨
امکانات کلیدی:
🔸
محیط لمسی:
رابط روان Phosh (گِنوم موبایل) برای تجربه‌ای شبیه به تبلت‌های هوشمند.
🔸
حفظ حریم خصوصی:
بدون گوگل و نرم‌افزارهای انحصاری، فقط با کدهای رسمی دبیان.
🔸
شخصی‌سازی:
پشتیبانی از پکیج‌های .deb، کرنل‌های سفارشی و اسکریپت ساخت فایل نصب (Image).
🔸
پشتیبانی سخت‌افزاری:
معماری x86-64:
سرفیس پرو (۳ تا ۱۰)، کروم‌بوک‌ و لپ‌تاپ‌های لمسی (مثل XPS و Thinkpad).
معماری ARM:
گوشی‌ها و تبلت‌های لینوکسی (مثل PinePhone و Librem 5).
💡
کاربرد اصلی:
انتخابی عالی برای احیای دیوایس‌های لمسی با سیستمی امن و بدون تبلیغات؛ کنترل واقعی سخت‌افزارتان را در دست بگیرید!
🌐
گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7107" target="_blank">📅 11:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7106">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏
🚀
دسترسی به هوش مصنوعی‌های برتر!
‏با این سایت ویژه، قدرت مدل‌های پیشرو دنیا رو یک‌جا رایگان در اختیار بگیر:
GPT-5.6⁩
|
‌Grok-4.5⁩
|
‌Kimi-K3⁩
|
GLM-5.2⁩
|
‌Claude Sonnet 5⁩
|
‌Gemini 3.5 Flash⁩
‏
✨
ویژگی‌های کلیدی:
‏
✅
60 دلار اعتبار تست
✅
دارای API keys
‏
✅
قابل استفاده در تمامی کلاینت‌ها
‏
✅
سرعت بالا: 60 درخواست در دقیقه
✅
درامد از طریق رفرال
‏
🔗
لینک ورود به سایت
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7106" target="_blank">📅 11:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7105">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🧹
ابزار Kudu؛ نرم‌افزار جامع پاک‌سازی و امنیت سیستم (جایگزین متن‌باز CCleaner)
یک ابزار قدرتمند، ۱۰۰٪ رایگان و اپن‌سورس برای بهینه‌سازی، پاک‌سازی و اسکن امنیتی در سیستم‌عامل‌های ویندوز، مک و لینوکس؛ کاملاً شفاف، بدون تبلیغات، بدون پرداخت درون‌برنامه‌ای و بدون هیچ‌گونه ردیابی اطلاعات (Telemetry).
✨
امکانات کلیدی:
🔸
پاک‌سازی همه‌جانبه:
حذف فایل‌های موقت، کش مرورگرها، برنامه‌ها و بازی‌ها، رفع خطاهای رجیستری و مدیریت استارتاپ.
🔸
امنیت و حریم خصوصی:
مجهز به اسکنر بدافزار، ابزار مسدودکننده ردیاب‌های ویندوز (Privacy Shield) و قابلیت حذف ایمن و غیرقابل‌ریکاوری فایل‌ها.
🔸
ابزارهای مدیریت سیستم:
آنالیز گرافیکی فضای دیسک، مانیتورینگ زنده (CPU ،RAM ،دیسک)، ابزار Debloater (حذف برنامه‌های پیش‌فرض ویندوز) و آپدیت گروهی نرم‌افزارها.
🔸
کاربری آسان و حرفه‌ای:
امکان پاک‌سازی سریع با یک کلیک (One-Click Clean)، اجرای خودکار از طریق خط فرمان (CLI) و قابلیت افزودن برنامه‌های جدید به لیست پاک‌سازی تنها با ساخت یک فایل ساده JSON.
💡
برگ برنده:
این پروژه توسط توسعه‌دهندگانی ساخته شده که از پیشنهاد دادن نرم‌افزارهایی مثل CCleaner (به‌دلیل حجم بالای تبلیغات و نامشخص بودن عملکرد داخلی) خسته شده بودند. با Kudu می‌توانید تک‌تک فایل‌هایی که حذف می‌شوند را بررسی کنید!
🌐
گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/7105" target="_blank">📅 09:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7104">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjjGAQRtsN-A8I4NPTWya-rDszZ_RkVU0HZRVsacIGGmlCAiZgeFefCAQgCHlKDnT9xKvmmS5Is-JIsOjz5FQWp7bFGCG1-IYWpWxtUGDKT1Vq-rSSs9LYZHaiRqUlIRzVqM7-BudbpmbqtY3yBRKWoxoIgNXi2NWxk0PnT-PRk55GArGmlZRQmjHjWHJjmGAu4A0hDOr09FxmqELh16nwUB1otlLA-vCoUZ52CXu3sSfSJNi-cd-FREJV6S7WwZdSmJcBl-ZUjGVOrGz4g6jhcnHOWmkr6nU7R795xJ600G3JGW09JlmXzGH3k3f3gbkVMyWBGK3EkDpy6n1mSaOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
؛Tensor.Art تولید تصاویر حرفه‌ای با هوش مصنوعی رایگان
🔸
بدون نیاز به نصب یا سیستم قدرتمند
🔸
اجرای آنلاین Stable Diffusion
🔸
تبدیل متن به تصویر (Text to Image)
🔸
تبدیل تصویر به تصویر (Image to Image)
🔸
پشتیبانی از ControlNet و مدل‌های متنوع
🔸
سهمیه رایگان روزانه برای تولید تصاویر HD
🔸
هزاران مدل و استایل آماده از جامعه کاربران
🌐
http://tensor.art/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/ArchiveTell/7104" target="_blank">📅 08:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7103">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🏆
بهترین مدل‌های هوش مصنوعی برای هر تسک (جولای ۲۰۲۶)
مهم‌ترین درس این روزهای دنیای AI این است: «دیگر دنبال یک مدل همه‌کاره نباشید!»
بهترین بازدهی زمانی به‌دست می‌آید که هر کار را به متخصص همان کار بسپارید:
🎨
کدنویسی فرانت‌اند:
Kimi-K3
⚙️
کدنویسی بک‌اند:
Claude Fable 5
🐛
دیباگ و رفع باگ پیچیده:
GPT-5.6 Sol
🖼
تولید تصویر:
GPT
🌍
ترجمه:
Gemini 3.5 Flash
🔎
جستجوی زنده (Real-time):
Grok 4.5
🎥
تولید ویدیو:
Seedance 2.0
💰
اقتصادی‌ترین و باارزش‌ترین:
DeepSeek V4 Pro
🖥
اجرای لوکال (سیستم‌های سنگین):
GLM-5.2
💻
اجرای لوکال (سیستم‌های سبک‌تر، ~128GB رم):
HY-3 و DeepSeek V4 Flash
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/7103" target="_blank">📅 06:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7102">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b91143b5e.mp4?token=QuXgUuqq71ubZJ-qOwkdSq-a3iT1NO3BzYAH3uuBrkAPtkKjJ_am8_5FXycKUL64RSoysWSSx56Epc3Af3YxzvKIsXlutASTg2TMmvR6rm_Ob41vptPoms9T_Gje5aKvGjwvUaVujU3N8t7o9GFS1Y8yuJMX8YUn_mUFVJ14AEOToEQns5IEF8cPMBMNsHSM6mA_Kf9XaoWKPLQQGQcs6igQnJ8LOoYU4e5nJjiNNZQ6SCRJnK013JxEjB_8Bdyzw08ANkGh9hgeBTUKVt8_xVtavDA3WA7mLKurtH4ew8R1rOraaa2XOvWwzJNcwmwg2-Fepiry7NcGMQNuZE2FOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b91143b5e.mp4?token=QuXgUuqq71ubZJ-qOwkdSq-a3iT1NO3BzYAH3uuBrkAPtkKjJ_am8_5FXycKUL64RSoysWSSx56Epc3Af3YxzvKIsXlutASTg2TMmvR6rm_Ob41vptPoms9T_Gje5aKvGjwvUaVujU3N8t7o9GFS1Y8yuJMX8YUn_mUFVJ14AEOToEQns5IEF8cPMBMNsHSM6mA_Kf9XaoWKPLQQGQcs6igQnJ8LOoYU4e5nJjiNNZQ6SCRJnK013JxEjB_8Bdyzw08ANkGh9hgeBTUKVt8_xVtavDA3WA7mLKurtH4ew8R1rOraaa2XOvWwzJNcwmwg2-Fepiry7NcGMQNuZE2FOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
شرکت ‌OpenAI⁩ از «‌ChatGPT Work⁩» رونمایی کرد؛ یک ایجنت هوشمند که فراتر از یک چت‌بات ساده عمل می‌کند. این ابزار برای مدیریت پروژه‌های سنگین طراحی شده و قابلیت‌های خیره‌کننده‌ای دارد:
‏
🔹
دسترسی یکپارچه:
کار با فایل‌ها و اپلیکیشن‌های مختلف شما.
‏
🔹
پایداری در اجرا:
توانایی تمرکز روی یک تسک برای ساعت‌ها.
‏
🔹
برنامه‌ریزی هوشمند:
شکستن اهداف بزرگ به مراحل کوچک و عملیاتی.
‏
🔹
عملکرد مستقل:
پیشبرد کارها حتی زمانی که شما آفلاین هستید!
🚀
🔵
@ArehiveTell
‏</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7102" target="_blank">📅 03:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7101">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🖥
ابزار DesktopCommanderMCP؛
کنترل کامل سیستم شما توسط Claude
یک سرور انقلابی MCP که کلود (و ابزارهایی مثل Cursor یا Cline) را به یک دستیار همه‌کاره تبدیل می‌کند تا مستقیماً روی کامپیوتر شما دستورات ترمینال را اجرا کرده و فایل‌ها را مدیریت کند.
✨
امکانات کلیدی:
🔸
ترمینال و پردازش زنده:
اجرای مستقیم دستورات، مدیریت پروسه‌ها و نشست‌های تعاملی (مثل SSH و دیتابیس) در پس‌زمینه.
🔸
مدیریت همه‌جانبه فایل‌ها:
خواندن، نوشتن و ویرایش مستقیم فایل‌های Excel ،PDF ،DOCX و جستجوی پیشرفته (ripgrep) در کل پروژه.
🔸
ویرایشگر جراحی (Surgical Edit):
ویرایش هوشمند و نقطه‌ایِ بخش‌های کوچکی از کد بدون نیاز به بازنویسی کامل فایل‌ها (که باعث صرفه‌جویی شدید در زمان و توکن می‌شود).
🔸
امنیت و محیط ایزوله:
قابلیت اجرای کامل در محیط Docker برای محافظت از سیستم اصلی، به همراه لاگ‌گیری دقیق و بلک‌لیست دستورات خطرناک.
💡
برگ برنده:
این ابزار برخلاف سایر ادیتورهای هوش مصنوعی، نیازی به پرداخت هزینه سنگین توکن API ندارد و از همان اشتراک عادی Claude Pro شما استفاده می‌کند. به‌علاوه، تمام عملیات‌ها کاملاً محلی (Local) و با حفظ کامل حریم خصوصی انجام می‌شود.
🌐
گیت‌هاب: wonderwhy-er/DesktopCommanderMCP
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/7101" target="_blank">📅 02:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7100">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🤖
۷ اسکیل (Skill) کاربردی برای ایجنت Hermes
ایجنت قدرتمند Hermes بیشتر از ۱۰۱ مهارت رسمی داره که فقط با یه خط کد نصب میشن. اینجا ۷ تا از خفن‌ترین‌هاشون رو معرفی کردیم که حسابی سرعت کارتون رو بالا می‌برن:
✨
معرفی اسکیل‌ها:
🔸
ابزار Unbroker (حریم خصوصی):
اطلاعات شخصی شما رو از دیتابیس ۵۰۰ تا سایت دلال دیتا (Data Brokers) پاک می‌کنه. یه جایگزین کاملاً رایگان و لوکال برای سرویس‌های گرونی مثل DeleteMe که خودش دوره‌ای وب رو اسکن می‌کنه.
hermes skills install official/security/unbroker
🔸
همکاری با Claude Code (کدنویسی):
تسک‌های برنامه‌نویسی رو مستقیم می‌سپاره به Claude Code. تو این حالت، هرمس نقش مدیر پروژه رو داره و کلود کد زحمت نوشتن و تست کُدها رو می‌کشه.
hermes skills install official/autonomous-ai-agents/claude-code
🔸
ابزار Unreal MCP (توسعه بازی و 3D):
موتور
Unreal Engine 5.8
رو فقط با زبون ساده و متنی کنترل کنید! شما صحنه رو توصیف می‌کنید (مثلاً یه جنگل تاریک دم غروب) و ایجنت صفر تا صدش رو براتون می‌سازه و باگ‌های ظاهریش رو هم می‌گیره؛ اونم بدون اینکه نیازی باشه به محیط آنریل دست بزنید.
hermes skills install official/creative/unreal-mcp
🔸
ادغام با 1Password (امنیت):
کلیدهای API و پسوردهاتون رو تو زمان اجرا، با خیال راحت مستقیم از ولت 1Password می‌خونه. دیگه نیازی نیست توکن‌های حساس رو به‌صورت فایل متنی (مثل
.env
) روی سیستم ذخیره کنید.
hermes skills install official/security/1password
🔸
ابزار OpenClaw Migration (اسباب‌کشی):
یه انتقال بی‌دردسر! با یه کلیک تمام تنظیمات، حافظه، ورک‌فلوها و مهارت‌های شما رو از ایجنت OpenClaw به Hermes منتقل می‌کنه تا مجبور نباشید از صفر شروع کنید.
hermes skills install official/migration/openclaw-migration
🔸
ابزار Blender MCP (طراحی ۳بعدی):
نرم‌افزار Blender رو با یه پرامپت متنی ساده کنترل کنید. مدل‌سازی، چیدن صحنه، انیمیشن و خروجی گرفتن برای یونیتی و آنریل، همگی فقط با چند خط متن انجام میشه.
hermes skills install official/creative/blender-mcp
🔸
ابزار Kanban Video Orchestrator (تولید ویدیو):
کل پروسه ساخت ویدیو (از سناریو
⬅️
استوری‌بورد
⬅️
ضبط
⬅️
تدوین
⬅️
رندر نهایی) رو مثل یه تخته کانبان مدیریت و خودکارسازی می‌کنه تا پروژه‌تون منظم و بی‌نقص پیش بره.
hermes skills install official/creative/kanban-video-orchestrator
⚙️
پیدا کردن اسکیل‌های بیشتر:
اگه می‌خواید لیست کامل ۱۰۱ اسکیل رسمی هرمس رو ببینید، این دستور رو بزنید:
hermes skills browse --source official
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/7100" target="_blank">📅 02:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7099">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0afbe9c883.mp4?token=V2FPukMCbq5S64wp9GAOXpw5bQPCZhKpceXcWQ5M9bYMEukTaZPVBZ731ZPrdQOnif89R6nI3vhGB439EtznBohSBq-mhYa5wpoFWQqIWEt1fIl-cf0DuAiKqBDKxlk9MOHqS_6_89dc-rD5NddxXEsnljiZ6mP8MYP3IbrtnfWA554q-fZxJgFCrkxFTuZPzS-N_okSkzJJdECOmOqH1PcnF8wEZtKQxY5VrjIv2Q5AJiX0cRuhOoOeVdLTWoDaUc-Fha0pGCXWoAJRxr10vg0B9VtoW2KbFKtDOjITIZIzl2u-dfkH4mq2ohGWP65mJ4UtxS2EbUf2qayAOHdMnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0afbe9c883.mp4?token=V2FPukMCbq5S64wp9GAOXpw5bQPCZhKpceXcWQ5M9bYMEukTaZPVBZ731ZPrdQOnif89R6nI3vhGB439EtznBohSBq-mhYa5wpoFWQqIWEt1fIl-cf0DuAiKqBDKxlk9MOHqS_6_89dc-rD5NddxXEsnljiZ6mP8MYP3IbrtnfWA554q-fZxJgFCrkxFTuZPzS-N_okSkzJJdECOmOqH1PcnF8wEZtKQxY5VrjIv2Q5AJiX0cRuhOoOeVdLTWoDaUc-Fha0pGCXWoAJRxr10vg0B9VtoW2KbFKtDOjITIZIzl2u-dfkH4mq2ohGWP65mJ4UtxS2EbUf2qayAOHdMnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚔️
نبرد غول‌های فرانت‌اند: Kimi K3 پادشاه جدید طراحی 3D!
مسابقه ساخت جهان سه‌بعدی (Three.js) در یک فایل HTML بین ۳ مدل برتر، با داوری کورکورانه هوش مصنوعی Qwen3-VL:
🏆
نتایج نهایی:
🥇
مدل Kimi K3: برنده چالش و صعود به رتبه #1 چارت Frontend Code Arena (بالاتر از Claude Fable 5).
🥈
مدل Opus 4.8: رتبه دوم با فاصله‌ای بسیار اندک (برنده رندر قلعه زمردین).
🥉
مدل GLM-5.2: رتبه سوم با خروجی ساختاری کاملاً سالم و پایدار.
💡
نکته: مدل اپن‌سورس Kimi K3 (انتشار وزن‌ها در ۲۷ جولای) رسماً در کدنویسی فرانت‌اند و رندرهای خلاقانه تمام رقبای قدرتمند کلوزسورس را شکست داد.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/7099" target="_blank">📅 02:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7096">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🤖
۱۰ اسکیل (Skill) و ابزار برتر برای ایجنت‌های هوش مصنوعی
با گسترش محیط‌های توسعه مبتنی بر ایجنت‌ها (مثل Claude Code و Hermes)، استفاده از مهارت‌های جانبی (Skills) به یک ضرورت تبدیل شده است. در ادامه لیست ۱۰ اسکیل کاربردی برای ارتقای عملکرد ایجنت‌های شما آورده شده است:
---
۱۰. ابزار Loopy (چرخه‌های خودبهبود)
تبدیل یک پرامپت ساده به یک چرخه خودبهبود (Self-improving loop). این ابزار کارهای شما را اسکن می‌کند، الگوهای تکراری را پیدا کرده و برای آن‌ها چرخه‌های ایجنتی می‌سازد و در نهایت آن‌ها را ممیزی می‌کند.
npx skills add Forward-Future/loop-library --skill loopy --agent claude-code -g -y
۹. ابزار Claude-Video (تماشای ویدیو توسط ایجنت)
به Claude Code اجازه می‌دهد تا ویدیوها را "تماشا" کند. استخراج فریم و زیرنویس از یوتیوب، تیک‌تاک، X، لوم و بیش از ۱۸۰۰ سایت دیگر به صورت کاملاً خودکار.
git clone https://github.com/bradautomates/claude-video.git ~/.claude/skills/watch
۸. فرمان last30days/ (دستیار تحقیقاتی)
اسکن همزمان شبکه‌های اجتماعی (ردیت، X، یوتیوب، Hacker News، Polymarket و...) در ۳۰ روز گذشته، رتبه‌بندی بر اساس تعامل واقعی و ارائه یک گزارش مستند. ابزاری فوق‌العاده برای مارکترها و مدیران شبکه‌های اجتماعی.
npx skills add mvanhorn/last30days-skill -g
۷. ابزار Kill AI Slop (قاتل متن‌های ماشینی)
پاک‌سازی متن از عبارات کلیشه‌ای، افعال مجهول، خط‌تیره‌های اضافه و نشانه‌هایی که دست هوش مصنوعی را رو می‌کنند (در ۸ دسته‌بندی مختلف).
npx skills add https://github.com/hardikpandya/stop-slop --skill stop-slop
۶. ابزار GOG (مدیریت فضای ابری گوگل)
دسترسی کامل و مستقیم ایجنت شما به سرویس‌های جیمیل، تقویم، درایو، شیتس، داکس و مخاطبین گوگل.
openclaw skills install @steipete/gog
۵. ابزار Unslop UI (اصلاح طراحی‌های کلیشه‌ای)
آموزش‌دیده روی شکایات واقعی کاربران از رابط‌های کاربری ساخته‌شده با هوش مصنوعی. حذف گرادیانت‌های بنفش و لوگوهای تکراری، چه در زمان ساخت و چه در زمان ممیزی پروژه.
git clone https://github.com/JCarterJohnson/vibecoded-design-tells.git
۴. ابزار Shannon Pentester (هکر جعبه‌سفید خودمختار)
یک تست‌نفوذگر جعبه‌سفیدِ خودمختار برای وب‌اپلیکیشن‌ها و APIها. اجرای این ابزار روی هر پروژه‌ای که با هوش مصنوعی (Vibe-coded) توسعه داده‌اید به‌شدت توصیه می‌شود.
npx @keygraph/shannon setup
۳. ابزار Security Unbroker (محافظ حریم خصوصی)
حذف خودکار اطلاعات شخصی شما از سایت‌های دلال داده (Data Brokers). شامل اسکن، درخواست حذف (Opt-out)، تایید و بررسی مجدد دوره‌ای. مراحل پیچیده و نیازمند تایید، به صف انسانی ارجاع داده می‌شوند.
hermes skills install official/security/unbroker
۲. فرمان improve/ (بهینه‌ساز اقتصادی سورس‌کد)
کل سورس‌کد شما را ممیزی کرده و برنامه‌های بهبود می‌نویسد؛ سپس پیاده‌سازی و اجرای آن‌ها را به یک مدل ارزان‌تر می‌سپارد تا در هزینه‌های API صرفه‌جویی شود.
npx skills add shadcn/improve -g
۱. ابزار Taste Skill (فریم‌ورک ضدماشینی فرانت‌اند)
یک فریم‌ورک فرانت‌اند ضد-ماشینی (Anti-slop) با ۷ سبک مختلف (از مینیمالیست تا بروتالیست). طراحی‌های ژنریک هوش مصنوعی در وب، موبایل و تولید تصویر را اصلاح کرده و به آن‌ها روح می‌بخشد.
npx skills add Leonxlnx/taste-skill
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7096" target="_blank">📅 01:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7093">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gxB37I0z3sjYmt7wAgCDVCdGRhniBEhUctnzrTotkFmf3UYvs-jvCyxl7Zf9bxDUS8UmWpv_y1HEHEoCge4i5YjGm-BGUYwOdtN3wA22YFoGMTgrc-Ni5EF9tCpQ3S3qd6v01lfq1NtGulR7R8Di8z2IqM1HiDzGPLN4q46PuH8dc737faeVdT6n7_nvyGxO7jyvg3rXGVFBad1EOkZw3Z59IOD8ToOj8I0unjE6pykt0ySlbFBSzARAlPswtFAWMKtT3iRG3FoUWMWRQ4_h5e_lrgkfc_N-IXf5ZcZ-zFWUhiSFvxhm3zG072a74q2s3ncs_-jIpbD6u3OIsSYocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uy48sxdf7gaIZpDrwUw0BpFr_cqr99JvEXRq54dxPvYTxFLUI2u_-K71W8pnYcRSR8Za-sZqkqVfckmEMT0KChDW6m1-gy8-WOpg--QeL054IEq2hSt8V5xviJdXwd4XXraWlPwdR2M0Df-9yUesoSxZQUPE9RguzZZ8MJf6Eac7kVcuUs8gmQOr-RzwsBdjJDPsthOHna239eq3vTBe6x07F19eN7yCGB89l6EcRcZNyH9uXBB8D5aQW06QSNlIfn6r-3iSb2HEry2-i4t43_OgnTu8PoXFPpKFYrIwahdWwiE1_2L6zlTmps0u2kaQsqgqrBIn1CBa-W26RI2IdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏دسترسی رایگان به اکانت یک‌ ساله ‌ Notion Plus⁩
🚀
💎
‏با این ترفند، تمام محدودیت‌ها رو بردار و از قدرت مدل‌های پیشرفته هوش مصنوعی مثل   ‌Opus 4.8⁩ , GPT 5.6 Sol , Grok 4.5⁩ , ‌Gemini 3.5⁩   برای مدیریت پروژه‌هات استفاده کن.
⚡️
‏برای فعال‌سازی و آموزش گام‌به‌گام،…</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7093" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7092">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏دسترسی رایگان به اکانت یک‌ ساله ‌ Notion Plus⁩
🚀
💎
‏با این ترفند، تمام محدودیت‌ها رو بردار و از قدرت مدل‌های پیشرفته هوش مصنوعی مثل
‌Opus 4.8⁩ , GPT 5.6 Sol , Grok 4.5⁩ , ‌Gemini 3.5⁩
برای مدیریت پروژه‌هات استفاده کن.
⚡️
‏برای فعال‌سازی و آموزش گام‌به‌گام، روی این پیام کلیک کن
✅
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7092" target="_blank">📅 22:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7091">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqR-C1PHPc-qVuA061Qwx43MXKyGooMd6Jln-Oxy-MUEvGxTSnxn815nDfaEhA41cGv893f1CYQ0suZ7hWWXtxXCAV8nF8eizN2j1MlnUTytcjJUCAD-L_rA-aujAt2qQGWrHA9YaBKo8CtTX1sI1weZcicv3Js46GELGvH3tMYpSxuAI4YpYpxbZzWxrWmpJStJvN2PwIjSQz6cnRfRFkivQa3mU15h9dopmjQJmrWekh6SjNHItgfp4eaB647a30dtrfmhBGAg9OE1KqPREwne-kUnFYMkM2zop0isxkgafFDyzAlNRclw1jZGvjfX2WFSux-bTt0rfM6cV4AwDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
پلتفرم OpenShip؛ هاب متن‌باز مدیریت سرور و اپلیکیشن
مدیریت و استقرار آسان پروژه‌ها روی سرور شخصی (VPS) و بی‌نیازی از سرویس‌های ابری گران‌قیمت.
✨
امکانات کلیدی:
🔸
دیپلوی حرفه‌ای:
استقرار مستقیم از Git (بدون قطعی) همراه با امکان رول‌بک یک‌کلیکی.
🔸
سرویس‌های آماده:
نصب سریع دیتابیس‌ها و ابزارهایی مثل PostgreSQL, Redis و Supabase روی زیرساخت خودتان.
🔸
ایمیل‌سرور داخلی:
ساخت ایمیل و دامین نامحدود و رایگان با پشتیبانی از IMAP/SMTP.
🔸
مدیریت هوشمند:
پشتیبانی از پروتکل
MCP
جهت مدیریت سرور و دیپلوی‌ها توسط هوش مصنوعی (بدون نیاز به SSH).
🔸
عملیات یکپارچه:
دارای اپلیکیشن دسکتاپ و وب، مانیتورینگ زنده، بکاپ خودکار، SSL رایگان و کلاسترینگ چندسروره (به‌زودی).
🌐
گیت‌هاب: openshipio
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7091" target="_blank">📅 22:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7089">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyXil8REAoUddApDeUWg-hh7ZiI2eWyFqkJTTe351oWC2FLdL95B59cgEFn5IK8o3NMxvYay7nH_6ZzmWckN3p9gFl__LT3rGuoqysQFZEVWT9sDpIHPea6QEPtTnxtVFJcRO4Y5k1guf7yCNrfQMH_KAunensJbntTVmNsCR8uDWnca09ITGUAp9x2T9oA7D9vvZpoGKD40FNkayWi1f_fUN5yYxMzGOC7JVaNxeFCisu9WTbz9Ju6Nk7r82GA3VdCDwCOy6fWoppXLVdhjV4dnSiRKPdFm25BUplDUxnJpkcJBuC0ZG6Ex4x2J1SZGozW490orwCFFMxZX4AIv2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ویرایش عکس در مرورگر رایگان و کاملاً محلی با پشتیبانی از زبان فارسی
✨
امکانات:
🔸
افزایش کیفیت تصویر.
🔸
فشرده‌سازی بدون کاهش کیفیت.
🔸
تبدیل بین فرمت‌های رایج.
🔸
فیلترها و سایر ابزارهای ویرایش.
🔸
رایگان و بدون واترمارک.
🔗
گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7089" target="_blank">📅 19:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7088">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🤖
دسترسی رایگان به مدل قدرتمند Kimi K3  یکی از قوی‌ترین مدل‌های هوش مصنوعی رایگانِ حال حاضر با کانتکست عظیم ۲ میلیون توکنی که در بنچمارک‌ها رقیب جدی مدل‌های پرچم‌دار محسوب می‌شود.
✨
امکانات کلیدی:
🔸
تحلیل داده‌های حجیم: دارای پنجره کانتکست ۲ میلیون توکنی؛…</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7088" target="_blank">📅 17:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7087">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🤖
دسترسی رایگان به مدل قدرتمند Kimi K3
یکی از قوی‌ترین مدل‌های هوش مصنوعی رایگانِ حال حاضر با کانتکست عظیم ۲ میلیون توکنی که در بنچمارک‌ها رقیب جدی مدل‌های پرچم‌دار محسوب می‌شود.
✨
امکانات کلیدی:
🔸
تحلیل داده‌های حجیم:
دارای پنجره کانتکست ۲ میلیون توکنی؛ ایده‌آل برای آنالیز اسناد طولانی و پروژه‌های برنامه‌نویسی (Codebases) سنگین.
🔸
رایگان و بی‌دردسر:
بدون نیاز به وارد کردن کارت اعتباری، همراه با اعتبار رایگان روزانه که هر روز به‌صورت خودکار شارژ می‌شود.
🔸
دسترسی آسان:
ثبت‌نام سریع با اکانت گوگل (مدل K3 به صورت پیش‌فرض برای چت فعال است).
🔸
پشتیبانی جامع:
قابل استفاده به‌صورت تحت وب در موبایل و دسکتاپ، و همچنین محیط خط فرمان (CLI).
⚠️
نکته:
پیشنهاد می‌شود پیش از اعمال محدودیت روی پلن‌های رایگان، این مدل را تست کنید.
🌐
وب‌سایت
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7087" target="_blank">📅 17:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7086">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
:
نفری ۵ گیگابایت
🧭
: حداقل 1 دعوت
👥
: 38/90
💾
: 5 GB
⏰
: 7 روز
🟢
فعال</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7086" target="_blank">📅 13:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7084">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">📱
اپلیکیشن Aethery؛ نسخه بومی و گرافیکی Aether برای اندروید منتشر شد!  اگر یادتون باشه قبلاً برای استفاده از فیلترشکن Aether روی اندروید باید دست به دامن برنامه Termux می‌شدیم. اما حالا با پروژه Aethery، این ابزار ضدسانسور و خودکار (که نیازی به خرید سرور نداره)…</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7084" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7083">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🌐
معرفی OrcaRouter؛ روتر هوشمند و هاب یکپارچه ۲۰۰+ مدل هوش مصنوعی
این پلتفرم یک درگاه (Gateway) قدرتمند برای توسعه‌دهندگان است که به‌جای درگیری با ده‌ها API مختلف، همه را زیر یک سقف و با استاندارد OpenAI ارائه می‌دهد.
✨
امکانات کلیدی:
🔸
مسیریابی هوشمند (Smart Routing):
با استفاده از مدل
orcarouter/auto
، سیستم در کسری از ثانیه پرامپت شما را آنالیز کرده و به‌طور خودکار بهترین، ارزان‌ترین یا باکیفیت‌ترین مدل را برای آن درخواست انتخاب می‌کند.
🔸
تنوع بی‌نظیر (۲۰۰+ مدل):
پشتیبانی فوری از جدیدترین غول‌های بازار مثل Kimi K3، GPT-5.6، Claude Opus 4.8 / Fable 5 و Gemini 3.1 Pro.
🔸
بدون کارمزد (Zero Markup):
شما دقیقاً همان تعرفه رسمی شرکت سازنده را پرداخت می‌کنید و OrcaRouter هیچ هزینه اضافه‌ای روی توکن‌ها برای مسیریابی دریافت نمی‌کند ($0 Routing Fee).
🔸
پایداری بالا (Auto-Failover):
در صورت قطعی یا لیمیت شدن یک ارائه‌دهنده (ارورهای 5xx یا 429)، در کمتر از ۵۰ میلی‌ثانیه درخواست شما به یک سرور سالم منتقل می‌شود تا کاربر نهایی هیچ خطایی نبیند.
🔸
یکپارچگی سریع:
اتصال در کمتر از ۶۰ ثانیه؛ تنها با تغییر
base_url
در کدهای فعلی‌تان (کاملاً سازگار با OpenAI SDK، Cline، OpenCode و...).
🎁
طرح‌های رایگان و هدایا:
🔹
طرح Hacker:
استفاده دائمی رایگان از زیرساخت روتر به همراه امکان ساخت ۳ کلید API.
🔹
امکان
تست رایگان ۲ مدل
به صورت آزمایشی در بدو ثبت‌نام.
🔹
دریافت تا
۱۰٪ اعتبار هدیه (Bonus)
در صورت استفاده از پکیج‌های شارژ خودکار.
🎁
پروموکد
KIMIK3WITHORCA
پنج دلار شارژ رایگان برای تست مدل Kimi K3 به شما می‌دهد
🌐
وب‌سایت:
orcarouter.ai
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7083" target="_blank">📅 00:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7082">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🎁
پلتفرم Gab AI؛ دریافت صدها اعتبار رایگان برای تست پیشرفته‌ترین مدل‌ها  یک محیط چت و ورک‌پیس جامع هوش مصنوعی با دسترسی به بیش از ۱۰۰ مدل مختلف که در بدو ورود، ۱۷۵ کرَدیت رایگان (بدون نیاز به کارت اعتباری) هدیه می‌دهد و حالا با به‌روزرسانی جدید، راه‌های بسیار…</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7082" target="_blank">📅 00:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7081">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎁
پلتفرم Gab AI؛ دریافت صدها اعتبار رایگان برای تست پیشرفته‌ترین مدل‌ها
یک محیط چت و ورک‌پیس جامع هوش مصنوعی با دسترسی به بیش از ۱۰۰ مدل مختلف که در بدو ورود، ۱۷۵ کرَدیت رایگان (بدون نیاز به کارت اعتباری) هدیه می‌دهد و حالا با به‌روزرسانی جدید، راه‌های بسیار جذابی برای دریافت اعتبار رایگان اضافه کرده است!
✨
امکانات و راه‌های افزایش اعتبار:
🔸
تست مدل‌های پرچم‌دار:
دسترسی رایگان به غول‌هایی مثل Claude Opus 4.8، Fable 5 و GPT-5.5.
🔸
ابزارهای همه‌کاره:
امکان تولید تصویر، ویدیو، موزیک، مدل‌های 3D و حتی ساخت فایل پاورپوینت مستقیماً در محیط چت!
🔸
دریافت بیش از ۵۰۰ کردیت اضافی:
با انجام تسک‌های ساده می‌توانید اعتبارتان را بالا ببرید. مثلاً انتقال تاریخچه چت‌ها (Import) از ChatGPT یا Claude معادل
+۲۰۰ کردیت**، فعال‌سازی تایید دومرحله‌ای
+۵۰ کردیت** و ورود از دستگاه دیگر
+۵۰ کردیت
پاداش دارد (به‌علاوه تسک‌های روزانه).
🔸
سیستم دعوت (Referral):
اگر دوستانتان با لینک شما ثبت‌نام کرده و اشتراک Plus تهیه کنند، به هر دو نفرتان
۲۵۰ کردیت
هدیه داده می‌شود.
⚠️
واقعیت‌سنجی (Reality Check):
میزان مصرف مدل‌های برتر بالاست؛ ارسال هر پیام در Opus 4.8 و Fable 5 معادل ۱۶ کردیت کسر می‌کند. همچنین طرح رایگان صرفاً برای محیط کاربری وب/اپلیکیشن است و دسترسی به API نیاز به خرید اشتراک دارد. با این حال، برای تست سریعِ جدیدترین مدل‌ها بدون دردسرِ کارت بانکی، گزینه‌ای بی‌نظیر است.
🌐
وب‌سایت:
gab.ai
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7081" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7080">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uY4svDDqYWVimaoQzLXdicEW-bfhLHRRKQKo-X3Goop9BIaXXRiYzH43fd2XeMYz1Ex0Ix0AphaoYe1sI8oDiVulyV2yMLoMutFKmjJdfIOAcISJGLYbOuqPlQK4Z7KTECrPL2Yf1cvz1VSt4yMMvMaAki2SI8bWu5f2G8THf8h-kmRTtAdLO8X9j7NHmTFw_svBCc4_CyD5AaZuTDhAlrvXd4rjb5u9fBJDwS0HSh4QcyFi3bL5B-yCmHa27BdJqVjOmvZToJM3nlRyvRUdJf-GukUn8irbkgDl-kN6jQV6gnJlwqSpMZnH9B6XyNFZS3zP-fIVX2OkiwNF_K-vOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/7080" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7079">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🌐
پلتفرم Api.Airforce؛ هاب یکپارچه ۲۰۹ مدل هوش مصنوعی  دسترسی جامع به برترین مدل‌های AI جهان در یک محیط واحد و بدون نیاز به حساب‌های مجزا.
✨
امکانات کلیدی:
🔸
تنوع بالا: پشتیبانی از ۲۰۹ مدل مختلف شامل Claude (Opus 4.7 و Fable 5)، DeepSeek v4 و ابزار صوتی ElevenLabs.…</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7079" target="_blank">📅 00:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7078">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">Gemini 3.5 Pro
از درد عشق تو خوابمون نمیبره چرا نمیای لعنتی
😂
💔</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7078" target="_blank">📅 23:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7077">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🌐
پلتفرم Api.Airforce؛ هاب یکپارچه ۲۰۹ مدل هوش مصنوعی
دسترسی جامع به برترین مدل‌های AI جهان در یک محیط واحد و بدون نیاز به حساب‌های مجزا.
✨
امکانات کلیدی:
🔸
تنوع بالا:
پشتیبانی از ۲۰۹ مدل مختلف شامل Claude (Opus 4.7 و Fable 5)، DeepSeek v4 و ابزار صوتی ElevenLabs.
🔸
پلن رایگان:
۱۳ مدل رایگان (مثل gpt-4o-mini و تولید موزیک Suno) با سهمیه روزانه ۱۰۰۰ درخواست (۱ ریکوئست در دقیقه) جهت تست اولیه.
🔸
مدیریت منعطف:
ساخت بی‌نهایت API Key بدون محدودیت آی‌پی (IP Whitelist) به همراه داشبورد مانیتورینگ.
🔸
سازگاری استاندارد:
پشتیبانی کامل از فرمت OpenAI API جهت همگام‌سازی آسان با کلاینت‌هایی نظیر Cline و OpenCode.
🔸
کسب درآمد:
دریافت ۱۰٪ از مبلغ شارژ دوستانِ دعوت‌شده (به‌علاوه ۱ روز اشتراک Premium رایگان برای آن‌ها).
🌐
وب‌سایت: api.airforce
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7077" target="_blank">📅 23:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7076">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slSHN6rbcs43OF_QV27m6MvQvYWng0BIplRGToTkgCca_kT2yRgq-clfj_bviHq1fcOgFK563Xf8euq3dKBRxTdo2qPT-VpFqDeDq52MIXZ-p9NXd8kmiWxtXQCIZrdvvhfNVFCE4Lc6NB7j_WgWRPDMN_nQiZuAmu6EYpLGArqPNlqHrN0NqMdeDqbTusyH4Ld0VFaZwwUUH4vJgwl3bmeby8uk4JQR_OJ6rvM0X__WGqz8eHh-krNOr5uMl2In0owHDG0xtgC5X3JcC2b65JRwrGJVrnxP-QhCCXVya4uQFXsO9oKeKTXvdiR74FLEjrthcdb2DVzoXqNxO30wCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
معرفی افزونه YouTube Subtitle Pro؛ شخصی‌سازی زیرنویس یوتیوب
یک افزونه کاربردی کروم برای کنترل کامل و تغییر ظاهر زیرنویس ویدیوها و شورتس‌ها در یوتیوب.
✨
امکانات کلیدی:
🔸
فونت و فایل دلخواه:
استفاده از فونت‌های سیستم و امکان بارگذاری فایل زیرنویس خارجی (SRT).
🔸
استایل مجزا:
تنظیمات ظاهری جداگانه برای زبان‌های فارسی و انگلیسی (به همراه اصلاح علائم نگارشی).
🔸
تغییرات ظاهری:
ویرایش دقیق سایز، رنگ، بک‌گراند و حاشیه کلمات.
🔸
فیلتر هوشمند:
امکان تعریف و حذف خودکار کلمات تبلیغاتی یا مزاحم از متن زیرنویس.
⚡️
دسترسی سریع:
فشردن کلیدهای Alt + S هنگام تماشای ویدیو.
📥
نصب از کروم استور
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7076" target="_blank">📅 23:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7075">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7075" target="_blank">📅 23:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7074">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">vless://df4bda66-59d7-4b79-abd0-0e4ee14d7c70@188.130.207.217:443?type=ws&encryption=none&path=%2Fws&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF   بزنید عشق کنید زمانش 24 ساعته</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7074" target="_blank">📅 20:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7073">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">vless://df4bda66-59d7-4b79-abd0-0e4ee14d7c70@188.130.207.217:443?type=ws&encryption=none&path=%2Fws&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF
بزنید عشق کنید
زمانش 24 ساعته</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7073" target="_blank">📅 20:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7072">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏دسترسی رایگان به مدل‌های هوش مصنوعی با این لیستِ کاربردی!
⚡️
‏این سرویس‌ها بهترین انتخاب برای دریافت ‌API Key⁩ و تستِ مدل‌های مختلف هستند:
‏
👑
برترین‌ها:
‌
Agentrouter⁩
| ‌
Iamhc⁩
| ‌
Google⁩
| ‌
Groq⁩
| ‌
Nvidia
| ‌
Cloudflare⁩
| ‌
Freetokenfaucet⁩
| ‌
Dahl⁩
| ‌
Tokengo⁩
| ‌
Opencode⁩
|
Unorouter⁩
‏
✨
سایر گزینه‌ها:
‌
Kenari⁩
| ‌
Cerebras⁩
| ‌
Nararouter⁩
| ‌
Llm7⁩
|
Openrouter⁩
‏با این ابزارها، پروژه‌هات رو بدون هزینه پیش ببر.
🚀
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7072" target="_blank">📅 20:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7071">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔓
آرشیو کامل پرامپت‌های سیستمیِ لورفته هوش مصنوعی!
ریپازیتوری
system_prompts_leaks
یک گنجینه واقعی برای توسعه‌دهندگان و مهندسان پرامپت است که دستورات مخفی و پایه (System Prompts) معروف‌ترین چت‌بات‌ها را جمع‌آوری کرده است.
✨
محتوای این ریپازیتوری:
🔸
جدیدترین مدل‌ها:
شامل دستورات پایه‌ی مخفی GPT-5.6, Claude Sonnet 5, Gemini 3.5 Flash, DeepSeek و Kimi.
🔸
تفکیک شرکتی:
آرشیو کامل و تفکیک‌شده‌ی مدل‌های OpenAI, Google, Anthropic, xAI, Meta و Perplexity.
🔸
ابزارهای توسعه:
شامل پرامپت‌های سیستمی دستیارهای برنامه‌نویسی مثل Cursor و GitHub Copilot.
🔸
یک منبع آموزشی ناب:
بهترین رفرنس برای یادگیری نحوه ساختاربندی دستورات و محدودیت‌گذاری توسط غول‌های تکنولوژی.
📥
مشاهده پرامپت‌ها در گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7071" target="_blank">📅 19:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7070">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">؛MIT OpenCourseWare یه پلتفرم آنلاین رایگانه که توسط موسسه فناوری ماساچوست (MIT) ارائه میشه و بیش از 2500 دوره آموزشی رو شامل میشه
🎓
🌐
http://ocw.mit.edu/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7070" target="_blank">📅 19:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7069">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-AfcAZlWU1PrKL0zLj8zjveZVZ0RBqlFgLAbygCXzVHiFtUcYRy8h6VYCPlW7xydpC5oXcOBHOjbXNTldJUGVDtRjHR-WqMTd_oGLJmkbS3n604jOIKRL2rYnthwhRjhwZxPyB-WHtaX9cN3ZmXKJMAV2E2zUrfopZxjevuyxDMxa3t1kEOzFN6YnEmy2oyK250po2nyUXHH890-U_2rcQvfNabRj4_V1eBfukrLBro5b9vqlbFoKGZ-ouJsfU6At0-Mfldj70HQS2fVtqPEzBBCFgGJ_IWZvrdlz6ooPVjkh70v-0rBtHtvwWhdMIz_71Ly-MOlBdKL-XRvvN3NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛Oh My HuggingFace برنامه کاربردی و متن‌باز برای HuggingFace که برای مرور و دانلود سریع، محلی و خصوصی مدل‌ها، مجموعه‌داده‌ها و غیره استفاده میشه.
🌐
https://ohmyhf.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7069" target="_blank">📅 18:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7068">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">happy کنترل ai از راه دور
🧠
Happy
یک پروژه
متن‌باز
است که به شما اجازه می‌دهد
Claude Code
و
OpenAI
Codex CLI
را از طریق
موبایل
یا
مرورگر
مدیریت کنید
⭐️
ویژگی‌ها:
✅
کنترل سشن از راه دور
✅
دریافت نوتیفیکیشن
✅
ادامه چت از موبایل یا وب
✅
پشتیبانی از مکالمه صوتی
✅
رمزنگاری End-to-End
✅
کاملاً متن‌باز (Open Source)
اگر از
AI Coding Agent
ها استفاده می‌کنید،
Happy
می‌تواند مدیریت تسک‌های طولانی را بسیار راحت‌تر کند؛ بدون اینکه همیشه پشت سیستم باشید
Github
💻
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7068" target="_blank">📅 18:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7067">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2c18bdbfa.mp4?token=CP3UJa4fWru3W_sQ2cqZmt-VRwzdXZXP8bAoLYGX1aYldjZL7edJ1r5CfEqBkEXDBqw5N1PWFMiwzkLuRLdMdZpJekR_X2CEt_kMAf1q3NAsZ1dQElitz8Xz1W00WMvaXuzc5Jnde4b4C24-b-0m4sXAtZu9Jf3B01F6CJj3ibfXx1AvUOoAPnphAz6IQXbk5CLs_Et6DEV1R6OXRv-qnxqZDCY_74EfA-HuXITsF3TESGiOXcZE32yGt0y-yZhnivYyOELPQXB1ieseURyFYA2NgqWCzm5KBoCaACqN1QFLZDW0GpNVKe1TD9fiMEvV6gN5xzICawGmHzK4KfUEnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2c18bdbfa.mp4?token=CP3UJa4fWru3W_sQ2cqZmt-VRwzdXZXP8bAoLYGX1aYldjZL7edJ1r5CfEqBkEXDBqw5N1PWFMiwzkLuRLdMdZpJekR_X2CEt_kMAf1q3NAsZ1dQElitz8Xz1W00WMvaXuzc5Jnde4b4C24-b-0m4sXAtZu9Jf3B01F6CJj3ibfXx1AvUOoAPnphAz6IQXbk5CLs_Et6DEV1R6OXRv-qnxqZDCY_74EfA-HuXITsF3TESGiOXcZE32yGt0y-yZhnivYyOELPQXB1ieseURyFYA2NgqWCzm5KBoCaACqN1QFLZDW0GpNVKe1TD9fiMEvV6gN5xzICawGmHzK4KfUEnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جستجوی چت‌های قدیمی در ‌ChatGPT⁩ بالاخره راحت شد!
🔍
✨
‏دیگر نیازی به اسکرول کردن‌های بی‌پایان نیست. ‌OpenAI⁩ قابلیت «جستجوی یکپارچه» را برای وب، اندروید و ‌iOS⁩ فعال کرده است. حالا می‌توانید از یک پنجره واحد، میان تمام گفتگوها، پروژه‌ها، فایل‌های آپلود شده و تصاویر جستجو کنید.
📂
🚀
‏با استفاده از فیلترهای جدید، دسترسی به پیام‌ها یا اسناد قدیمی که ماه‌ها پیش ذخیره کرده بودید، در چند ثانیه انجام می‌شود. یک آپدیت کوچک اما به‌شدت کاربردی برای کسانی که زیاد با هوش مصنوعی سروکار دارند!
💡
✅
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7067" target="_blank">📅 17:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7066">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">vless://06069771-bef8-4730-b711-c51efcdad901@onlineprochess.ir:8880?mode=auto&path=%2Fws&security=none&encryption=none&host=tsrety.dpdns.org&type=xhttp#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF  تمام نامحدود</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/7066" target="_blank">📅 17:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7065">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">vless://06069771-bef8-4730-b711-c51efcdad901@onlineprochess.ir:8880?mode=auto&path=%2Fws&security=none&encryption=none&host=tsrety.dpdns.org&type=xhttp#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF
تمام نامحدود</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7065" target="_blank">📅 16:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7064">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgvOQd9q2Cb42rVWAnAyhF9auPVBLt7A4SPMdHNyAkjFgqMh20mHLJ2hQ3J4RbwwCWWZcnf4KZ-_8lNKKLsJ-lomTTAq4GBLTBBcabHIndqN6KKkEq2-zIsWtwerZHAPPvUre6wvvYPrdUluLytcmwjuaQppjG2KnjKWVgN0-MDZvc1cew75Vjqyn35_Bh1ThQjr1MZde8Cox1xy1RX9BXjTrQlCNBjuKbDo7Mfiy_znVUkeUBWwvyVHEq1rOYr6j9aTxR5cWpy_2SCyLrpkPI6uksX4MT6nMIK-kM7U_0hJJZn9NfCnvMlEbmmf3RKzhNXnORXGlyxsmBQtnF7P1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
معرفی SHADOHDORKS؛ موتور جستجوی قدرتمند گوگل دورکینگ
یک مرجع فوق‌العاده و ابزار تخصصی برای OSINT و جستجوی پیشرفته (Dorking) در گوگل که برای محققین امنیت، باگ‌هانترها و تحلیلگران شبکه به‌شدت کاربردی است.
✨
ویژگی‌های کلیدی این ابزار:
🔸
دارای بیش از
۱۰۰۰ دورک (Dork) پیشرفته
و دسته‌بندی‌شده.
🔸
پیدا کردن هوشمند
ساب‌دامین‌ها (Subdomains)
.
🔸
جستجو و کشف
پنل‌های مدیریتی مخفی یا در معرض دید (Exposed Panels)
.
🔸
شناسایی
نشت اطلاعات و کلیدهای API
در سطح وب.
🌐
آدرس دسترسی مستقیم به ابزار:
🛠
مشاهده سایر ابزارهای کاربردی OSINT:
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7064" target="_blank">📅 16:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7062">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/01b871c31b.mp4?token=Lgc65AzXk53R48GAQy-IUG3HTZroa923vUdzp-LzENZQ32D5xhyb60G6f82MMA9ozLYMiMXDPaZoFQjoiXG47QQsudo9jaL7QXO7P3H2SG2Bw3XdfE8KVlx5iSEFi1ye4aUpRdy4xr8eLni_tN5RzYDEvQv6cpG4s8nSJw13klgA_ECWL6GT-s8mPnutiE7FMAnEJ0z2XiHDoia2elDOq2pg4CZNP_39tYeYWCC4haXO9BHxMdbDQ_mn0ocRWGEzTDQBmfSiTw5TtTzCb3DNyRLXY_34XaXog3K-kFJYt-skUGictNMh8XmMqGjEWbWlAYcMv_4erebsokohxafr7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/01b871c31b.mp4?token=Lgc65AzXk53R48GAQy-IUG3HTZroa923vUdzp-LzENZQ32D5xhyb60G6f82MMA9ozLYMiMXDPaZoFQjoiXG47QQsudo9jaL7QXO7P3H2SG2Bw3XdfE8KVlx5iSEFi1ye4aUpRdy4xr8eLni_tN5RzYDEvQv6cpG4s8nSJw13klgA_ECWL6GT-s8mPnutiE7FMAnEJ0z2XiHDoia2elDOq2pg4CZNP_39tYeYWCC4haXO9BHxMdbDQ_mn0ocRWGEzTDQBmfSiTw5TtTzCb3DNyRLXY_34XaXog3K-kFJYt-skUGictNMh8XmMqGjEWbWlAYcMv_4erebsokohxafr7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نسخه جدید گفتگوی صوتی Chat gpt منتشر شده و انقد طبیعیه، پشمای همه ریخته!
+ خوراک غیبت برای دختراس.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7062" target="_blank">📅 16:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7061">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3X-UI-MANUAL.fa.pdf</div>
  <div class="tg-doc-extra">1.9 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7061" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آموزش پنل ثنایی به زبان ساده
✨
منتشر شده توسط
@ArchiveTell
❤️‍🔥</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7061" target="_blank">📅 15:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7059">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تغییر ریجن گوگل در ۳۰ ثانیه
⏱️
به لینک زیر بروید، ریجن را انتخاب کنید، دلیل تغییر را بنویسید و ارسال کنید .
https://policies.google.com/country-association-form
حداکثر تا ۲ ساعت ریجن به جایی که میخواهید عوض می‌شود
✅
.
از توجهتان ممنونم
🙏
.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7059" target="_blank">📅 15:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7057">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">معرفی Ghost Downloader؛ جایگزین مدرن و متن‌باز برای IDM
🚀
📂
نرم‌افزار Ghost Downloader یک دانلود منیجر پیشرفته و چندپلتفرمی است که با رفع محدودیت‌های ابزارهای کلاسیک، تجربه‌ای سریع، پایدار و بهینه را برای دانلود فایل‌ها ارائه می‌دهد.
🛠
✨
✨
امکانات کلیدی:
🔸
…</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7057" target="_blank">📅 13:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7056">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">معرفی Ghost Downloader؛ جایگزین مدرن و متن‌باز برای IDM
🚀
📂
نرم‌افزار Ghost Downloader یک دانلود منیجر پیشرفته و چندپلتفرمی است که با رفع محدودیت‌های ابزارهای کلاسیک، تجربه‌ای سریع، پایدار و بهینه را برای دانلود فایل‌ها ارائه می‌دهد.
🛠
✨
✨
امکانات کلیدی:
🔸
سرعت خیره‌کننده:
قطعه‌بندی هوشمند
(AI)
فایل‌ها برای دستیابی به نهایت سرعت،
بدون نیاز به زمان انتظار
جهت ادغام (Merge) پارت‌ها در انتهای کار!
⚡️
🏎
🔸
پشتیبانی جامع:
سازگاری کامل با پروتکل‌های HTTP، تورنت (Magnet/BT)، FTP و فرمت‌های استریم نظیر M3U8.
🌐
📁
🔸
دانلودر اختصاصی یوتوب:
قابلیت دریافت مستقیم ویدیوها تا کیفیت 4K، پلی‌لیست‌ها و زیرنویس‌ها.
🎥
🍿
🔸
امنیت و عبور از محدودیت‌ها:
شبیه‌سازی دقیق اثر انگشت مرورگر (TLS Fingerprint) جهت جلوگیری از مسدود شدن دانلود توسط سیستم‌های آنتی‌بات.
🛡
🥷
🔸
افزونه هوشمند مرورگر:
شناسایی و استخراج (Sniff) خودکار لینک‌های مدیا و ویدیوها از صفحات وب.
🔗
🧠
🔸
پشتیبانی چندپلتفرمی:
بهینه‌شده برای ویندوز، لینوکس، مک و دارای اپلیکیشن کامل برای اندروید.
💻
📱
🤖
این ابزار کاملاً رایگان است، رابط کاربری مینیمالی دارد و در پس‌زمینه کمترین میزان مصرف منابع سیستم را به خود اختصاص می‌دهد.
💎
🍃
📥
دریافت فایل‌های نصبی و سورس‌کد از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7056" target="_blank">📅 13:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7055">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0kYTU7DDCZDPv4EoI9pkWtLgWzr9wOIFpADMptcfc1VMawpFayWOiONWd3aTSaqcQ-lIt8K1hIawWt8kfec9EI15tHOBPjsdeHlNUSDM86DNNERoj4IS9FFVLu2pwXjI0o_Z99_F_VRVKVHSYmr1GLNQz2YizrmCjMCAxX_2x8u2qZQwJiU0HHcz2EiGveO7nPQRSM7cpjxVROxYQk3ljHV5_hRAMzu6aRNC6KtJWa7n8IxP5aW8qHbVggePFoybjplZX5Y5dqVSlMyet5hJSBqLzPHx3s6S7_eZOoszO8KAiWcogiovLABnPvwIhw2axnJ0HNp7iYIAR0_ta4W2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7055" target="_blank">📅 13:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7053">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اشتراک Gemini pro برای ۱۸ ماه فقط ۶۹۹ هزار تومن!
🎉
💰
اینو قطعا این روزا زیاد دیدین تو چنلای مختلف. خواستم بگم ماجراشو بدونین.
یه شرکت تلکام هس تو هند به اسم jio اومده با گوگل قرارداد همکاری امضا کرده.
همکاری اینطوری هستی که هر کی سیمکارت jio داشته باشه، و ماهانه ۳۴۹ روپیه معادل ۳.۷ دلار به صورت مداوم شارژش کنه، میتونه اشتراک ۱۸ ماهه جمینای رو داشته باشه. اگه یک ماه شارژ نکنه، اشتراک جمینایش غیر فعال میشه و برمیگرده نسخه رایگان.
این جیو تو هند تبدیل شده به اسکم
🤑
هندیا میخرنش، ۳ دلار شارژ میکنن، میفروشن ۵ دلار (حالا فمیلی هم میشه اشتراک گذاش، اینم حساب کنیم میشه یه ۳۰ دلار)، ولی ماه بعد تمدید نمیکنن!!! یجورایی کسب درآمد میکنن باش.
۳ دلار میدن ۳۰ دلار کسب میکنن. دلالی عالی.
خلاصه به احتمال زیاد فقط یک ماه کار میکنه حواستون باشه.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7053" target="_blank">📅 12:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7051">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ii25cZ59pAJF3ALu77jE5NOt0RlbMG11N4jJTt2G1q9Y9fJhhRm7WbFU8NYc9AuyRfUUs_ULpdhtTvCGSTN3SDVESJ6vQW7yJC73ebd-SUwePkGFcwPnL-1TGxjkoBaXGdD4HXSrKEU0k_PeJpI4Au3w2PWaodvzZOEQjgELmCCd7HLj8QhO88wOLLTe259WjLZJn1_gSYAW6sn9dNrScyv7Ix-uwUK3OvFLoxQRDv0fEbUIeUXF2JhkqRtCeHP1goDpZpX3RZmCvelanPRwvPPMT0KRjut9czyJwn7xm_3okVfkQ-om56sKYTHciPCu0KxuEkpzsjshEBz0xAVT2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
امروز باید منتظر Gemini 3.5 Pro باشیم؟
طبق جدیدترین شایعات، احتمالاً امروز گوگل از نسخه جدید هوش مصنوعی خود یعنی
Gemini 3.5 Pro
رونمایی خواهد کرد.
✨
ویژگی‌های لو رفته و انتظارات از این مدل:
🔸
حافظه ۲ میلیونی:
دارای کانتکست ویندوز (Context Window) عظیم ۲ میلیون توکنی برای پردازش یکجای داکیومنت‌ها و پروژه‌های حجیم.
🔸
حالت تفکر عمیق (Deep Think):
اضافه شدن قابلیت استدلال پیشرفته و منطقی برای حل مسائل چندمرحله‌ای و پیچیده.
🔸
غول فرانت‌اند:
تمرکز ویژه بر روی کدنویسی و عملکرد فوق‌العاده قدرتمند در حوزه فرانت‌اند (Front-End).
🛑
احتمال تأخیر در عرضه:
با توجه به رقابت بی‌رحمانه در بازار، اگر گوگل احساس کند این مدل هنوز توانایی رقابت کامل با برترین‌های فعلی را ندارد، احتمال تأخیر آن بسیار زیاد است و رونمایی به هفته آینده (۲۴ ژوئیه) موکول خواهد شد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7051" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7049">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
: نفری ۵ گیگابایت
🧭
: حداقل 1 دعوت
👥
: 0/90
💾
: 5 GB
⏰
: 7 روز
🟢
فعال</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7049" target="_blank">📅 12:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7048">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپخش کانفیگ رایگان🔥</strong></div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
:
نفری ۵ گیگابایت
🧭
: حداقل 1 دعوت
👥
: 0/90
💾
: 5 GB
⏰
: 7 روز
🟢
فعال</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7048" target="_blank">📅 12:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7045">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGct98wXtGO3hEzPAX6ylbj1nk86cXStbU8tj_0JAXRFH4MfX-6dsFh-lkCeVSF5od-IQ3y-InyWwMaTesF6jFFikE4cKsMl_OTvPR14jac_2Nx20iUzUI-eHtnAFTDwjG_bnRy-vGv8cl3j5Shq3i_nfmaVIYUaBs5TDKAB5_ruNjGYO3xwN3susX4lWP6HpqJr7vIw_kWB-j88DFx3LSG-66lulJltwRu6Oyr3u_iUK8zJyXbfOJh7I74D5u366Zeqf-7UX5rtg8lSoPyEraXcYb0dKNNH8XRnra7wx-TYuoNPAC9jFKx6HrLyPZeNk7Wanas5aBMzHqkiMl3t3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔎
Google AI Edge Gallery – اجرای  هوش مصنوعی بدون اینترنت
📊
💡
گوگل پروژه متن‌باز AI Edge Gallery را منتشر کرده؛ اپلیکیشنی که به شما اجازه می‌دهد مدل‌های هوش مصنوعی را مستقیماً روی گوشی اجرا کنید، بدون اینکه به اینترنت یا سرورهای ابری نیاز داشته باشید
🌐
🔻
قابلیت ها :
🔹
چت با مدل‌های هوش مصنوعی به‌صورت کاملاً آفلاین
🔸
تحلیل و درک تصاویر
🔹
دانلود و مدیریت مدل‌های مختلف
🔸
حفظ حریم خصوصی، چون تمام پردازش روی خود دستگاه انجام می‌شود
🔥
با توجه به تجربه اختلال‌ها و محدودیت‌های اینترنت در ایران طی سال‌های اخیر، چنین ابزارهایی می‌توانند گزینه‌ای کاربردی باشند؛ چون حتی اگر دسترسی به سرویس‌های آنلاین محدود شود، همچنان امکان استفاده از هوش مصنوعی روی گوشی وجود خواهد داشت
🟡
🧪
این پروژه هنوز در مرحله آزمایشی است، اما می‌تواند یکی از مهم‌ترین قدم‌ها برای اجرای مدل‌های هوش مصنوعی به‌صورت کاملاً محلی روی موبایل باشد
GitHub
🐱
PlayStore
📲
ios
🏬
Mac
💻
⚡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7045" target="_blank">📅 03:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7043">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">172.64.147.128 104.17.166.13 104.17.166.13 198.41.195.250 104.27.51.177  اگه پینگ نداد باید آیپی های تمیز کلودفلر رو بندازین توش</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7043" target="_blank">📅 00:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7041">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZv9ycBSCOwZdO8KbpEIriKcxprLvEbj9ewjnOwpiAeSLWbursLLzq8O045unsAQtTPT6hJ_EiL-TOZ03kkjQqs0bqjloYTgBCcVUQUKgwzgBHWCB6R4SJxHCYYda_pETtPRBotypR3-LLhBi8vMmxAQuKyeJVXHrtlRwfZ5mmWTrodoob93X5uyZAFkTfDgF9jVxS21AjXyWSyTLTBoAJa5CX2-DD615YVcqneDc-6f5DtjTs79jF3ecvqBPLTnzEd_MLNJ_U8P-OJQtcwHkpVRgYgzCW6l9stl0KygALnFGOMXePy5C7LaI7B199TF0h3Pv-GZDkkYS_y79DCQVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛HyCanvas جایگزین Open Source و Self Hosted برای Canva
🎨
مناسب افرادی که میخوان طراحی گرافیک، پست شبکه‌های اجتماعی، ارائه، ویدئو و اسناد رو روی زیرساخت خودشون، بدون واترمارک و رایگان انجام بدن.
✨
ویژگی‌ها:
🔹
اجرا در مرورگر
🔹
پشتیبانی از طراحی پست، ارائه، ویدیو، وایت‌بورد، اسناد و چاپ.
🔹
خروجی در فرمت‌های PNG، PDF و سایر فرمت‌ها.
🔹
پشتیبانی از "Bring Your Own Key" (BYOK) برای قابلیت‌های هوش مصنوعی.
🔹
امکان Build در محیط Production به‌صورت یک فایل Go.
🔗
سورس پروژه و دانلود در گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7041" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7040">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRRhvDzOFW2hiTGIaw0jxZPP6NWDlnYIFNOk2mzH_hXCq86N-Qi5hnaDxkf-iKOo5B28pfB7nPph5uPZ3xXkncGzQOwhPOBC-a_1yYJivpHM3ShJJRuQ2qsmB2L2TM1llti6UVt8_3ISfcVLm19ZA1oLsJuoIKVa_Sh_A5Im6DBnRpaDsNytjkEjX5am7an7NllAZ9NNSz-pRzgdd2Iv6EE1SEzbA2r-yyi8w3lsKlvC03L7LDIvZn41Hb0JMTQWXbBsM21ceYdJ8U1CitQkY_xlEVLAWyuxnLGWLw2DiMTCSigoXFskNQ61QCxNkJA536ZYNl-1L93KcwLgJGcaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">200GB   vless://1c0e84d7-34ad-4242-9b4b-ea81f973e0aa@172.67.117.177:443?path=%2Farchive-stream&security=tls&encryption=none&insecure=0&host=mail.qbo.qzz.io&fp=chrome&type=ws&allowInsecure=0&sni=mail.qbo.qzz.io#%40archivetell  تمام
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7040" target="_blank">📅 21:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7039">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">200GB
vless://1c0e84d7-34ad-4242-9b4b-ea81f973e0aa@172.67.117.177:443?path=%2Farchive-stream&security=tls&encryption=none&insecure=0&host=mail.qbo.qzz.io&fp=chrome&type=ws&allowInsecure=0&sni=mail.qbo.qzz.io#%40archivetell
تمام
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7039" target="_blank">📅 21:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7036">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/af0-r9akvJPeZSTifEcSw1c2W8ikcfzvdsNdW7jWPvTWVOgsClGRPTK_oY7gX4tBmS4y-NnBAmUP2A9a0kpfXp2HsLle78BxU7FFtG23-e3OjzVWyh7y5xW4WuvOIrGj1EzGXt8tvLTgm3LlDbzxYK_oE7TqdWepr8jpcmzTJTge2CS-6GTf6YNkbpr1S5GqpDNiz6k6EICZZDIhoa6cY5QnK3sroW7FH-CiCizlCHPxMxF8QdX1nZuTPkudXksobCYzHA3X6h4rIsWfl3hEMr2FUOWWDBiKs4KLRIcCss-_3_pN-HJ4L8g6DZQnVAN0H-eWhP-FOvw-PArZ45gV7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
هوش مصنوعی Kimi K3؛ رقیب قدرتمند چینی برای Fable 5 و GPT-5.6!
استارتاپ Moonshot AI از مدل زبانی جدید خود رونمایی کرد که با مشخصات خیره‌کننده‌اش مستقیماً غول‌های هوش مصنوعی را به چالش می‌کشد.
🔥
ویژگی‌های کلیدی:
این مدل با حدود
۳ تریلیون پارامتر
و پشتیبانی از کانتکست ویندوز
۱ میلیون توکنی
، توانایی پردازش حجم عظیمی از داده‌ها را دارد. Kimi K3 می‌تواند اسناد بسیار طولانی و پروژه‌های برنامه‌نویسی سنگین را بدون فراموشی یا از دست دادن رشته‌ی کار، به‌خوبی تحلیل کند.
🛠
امکانات و قابلیت‌ها:
🔸
نسخه Kimi K3 Max:
دارای رابط کاربری چت (Chat Interface) با حالت‌های اختصاصی و بهینه‌شده برای برنامه‌نویسی.
🔸
سیستم K3 Swarm:
یک فریم‌ورک پیشرفته برای کار با گروهی از ایجنت‌های هوش مصنوعی (AI Agents) تا وظایف پیچیده را به بخش‌های کوچک‌تر تقسیم کرده و تحقیقات گسترده انجام دهند.
🔸
دسترسی API:
به‌صورت کامل برای توسعه‌دهندگان در دسترس است.
🚀
لینک دسترسی و تست مدل
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7036" target="_blank">📅 19:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7033">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fQxn-CFyfDpAw8PDyCRMvqiGEdVrC3j4sg3YdqVFUrWN9_qlG5tZg4z8NeSfLiNSHtjuQ8HzMUGxxF75wYrkS2RvoUemrBT_o8VavPb0cmuKqZM1PW3hxMAdWp8EBgJf93A5bBlC0tsEzU4lheB9MpkwRc41oW70xhoVhO89AO4T60I_6IfG4ilRW1L4-QS9BNAbSFv5AG3NVtv_Og-80Ri8TK67lRtS43Q2mp_8P-3zp_FdafuYytoscFSxWHaFlYZtv1Ycj223H_Qsc7BgLnXttxhn_pE84HKj939WPn7Y5DWy600cu67EIZWIg9L8jcKrmbzbhQ3x1Mv3LUXNKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OABiuEtf2onZxj2dr9-psc-pG1Mk7AzA0191wDeheOdI1Vki7io7ejVAYij5C5n0sVw9Utw-8JmuifWs62Zr8Yemx5UG57Hiv2n_dH07RDQic-75bmsMF3wn7b_w5cl3gUEvPDT6kJLpOz2hF06qWg5-UmRrSHpkPJ5vtYHNRjdd-EiVx_fVc1iVkoGVCJS2vAWNPXCEBmIdmyssiplxdV2FvhO6c1zw375OMubElPZAK-Q5JqVfuLsiY2su1boy7NcmLG7VBOIc5gGtXJOqNXzps0Hn2WutReWhiSJG5tOVE09teKy1stvO4oyQXco7j__l-a5IpQiw7ZVrg5m6zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RaTHcu4ZNyI4GKH23BPML4r3Zx8FtNwwMrKe7qk-MDPicZzFzFxx9SSYQPmHr_brfVZztVBeGMqHWRtnhtG2WudndEKH-sbPvGZfdTBSVz4D1FkUCCzw6Od_gcqLle1O-d5fEkcGvTKu_xcMNU7Fx7ixcblz-M1ZnHIS4xiHi6KAuuwYLF0bnRrJF6W1-mzRkMlXKBPB7HlPDqeimGkiZxbCnpeWSGp9XYGRndBhJGOT2LIj-lbrAhukfkOwxVG7NdvfnLoqcHrqNptF3gUCTqU3LvzpG_JhOU-mOtqgrwIifpo0Kd65Nb_3vfoUy4kqBo0EmGzH4Y11Q9NwAvcI0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🤖
دالتون بات (Daltoon Bot)
یک دستیار هوشمند و متن‌باز برای ساخت، مدیریت و فروش خودکار سرویس‌های VPN (از طریق ربات تلگرام و پنل وب).
✨
امکانات کلیدی:
🔸
پشتیبانی یکپارچه از پنل‌های سنایی (3x-ui)، ریبکا و پاسارگاد
🔸
کیف‌پول داخلی برای شارژ حساب و خرید آنی اشتراک
🔸
داشبورد مدیریت تحت وب (React) با قابلیت کنترل چند سرور همزمان
🔸
مانیتورینگ زنده ترافیک کاربران و پشتیبانی از زبان فارسی
🚀
نصب سریع با یک دستور (لینوکس):
Bash
bash <(curl -Ls https://raw.githubusercontent.com/mdaltoon10/Daltoon-Bot/main/install.sh)
📥
سورس‌کد و راهنما در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7033" target="_blank">📅 19:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7032">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🛡
معرفی فیلترشکن GRoute (جی‌روت)  کلاینت متن‌باز، سبک و رایگان (بدون تبلیغ) بر پایه Xray-core برای اندروید با پشتیبانی کامل از زبان فارسی.
✨
امکانات کلیدی:
🔸
پروتکل‌ها: سازگار با VLESS, VMess, Trojan, Shadowsocks و REALITY.
🔸
وارپ و آی‌پی تمیز: ساخت کانفیگ…</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7032" target="_blank">📅 19:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7031">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeviZWafemYOJtymuPSzA9caaECMiHKY0nc7_Md8iL7wefzo5320_CMteLQ11IYm3KrIzW6vWBTxH6E-RDRdLWtysXTnqTfXVaFXm67QEujgGTAhVWr53Zv2_Ympz-BqrVh_OeHRYWKpNHA47h_xBsU15yO10Qqpl397fIVQBzS6rtpbFO0pYLVhKSpgKTfC2MEe4VyN8GiFBjphl70IuBMKfcvBXt1KqHIHs38FTZOJhwmiac94PowkAw6fbSkLx6QI-CLJ7V4DNJQYVsG7hIYd5OipKWcJBxkFQpKSrp4oK5TPDJrgIv3056ShCho90RGPfjpcJYZoOB3Wq-oTMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
معرفی فیلترشکن GRoute (جی‌روت)
کلاینت متن‌باز، سبک و رایگان (بدون تبلیغ) بر پایه Xray-core برای اندروید با پشتیبانی کامل از زبان فارسی.
✨
امکانات کلیدی:
🔸
پروتکل‌ها:
سازگار با VLESS, VMess, Trojan, Shadowsocks و REALITY.
🔸
وارپ و آی‌پی تمیز:
ساخت کانفیگ WARP با یک کلیک و دارای اسکنر داخلی Clean IP.
🔸
مقابله با فیلترینگ:
تنظیمات Fragment (ضد DPI) و Sniffing برای اتصال پایدار.
🔸
مسیریابی هوشمند:
تونل کردن برنامه‌های دلخواه و باز کردن سایت‌های ایرانی بدون مصرف ترافیک.
🔸
مدیریت سابسکریپشن:
آپدیت خودکار لینک‌ها و نمایش حجم باقی‌مانده.
🔸
ابزار تست:
قابلیت تست سرعت، پینگ و نمایش لاگ شبکه.
📥
دانلود فایل نصبی (APK) از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7031" target="_blank">📅 19:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7028">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LfFk6QlF2JKQ7c06nCxFnDynbisvalYcQLk8rftCDA4lvCv2hOBJUFtqhunod7vtAs_RScxkmAaE7DHLsHABofHuCANyvM5v_pjxtnGcZhznkvn_TdkyGoo1hOUncOdfmlg6tBmbkFWRjF45DGJmrYXcxGpMMR7kwN4uVGRQoxasjKkdTtnm4912tPVUeWrPyQuC2SkCWTWikNJCq2Kl1dCuiiwTN54gs1ksS8V-hRkOgQKSEo7abRRrOxwrfsaVmSbG4upn0cwaeBdiU-SvL2ojyo7ORZXc_nBLaMYon7UNFgOAIjdLMR76_4kSBECEZdKXmZF8MCjkX3bKbsgyjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W9jxefaJ2VU5TKWaLFuSDWZPNXsNMBRr6eFNYGaC-VpGpdg7gWiuK3xq05vdwgxLWPLKvVc_5FpQnDN_CtdHpN38DfGSk6QmPM6cwMBtOJ9h1qqAn1CtKj0qDhCCXOcXzx6qMtTnZtQqyBqfW26k32icQX1FCmkj-N7NQOczg2-oTfFAOg7yUQpg8vZ_PlECbP9IiO-Ku7okwcYB5QjSj-0xmK3_38hFfYfSdqJO6vakwMyB59yrirN0JanO7tPylfsZLIyeREibKDnDm-dABtCDLvFcMxLnIi4JeismNr-mE-XwqV-M7USe8779UKhSsSII-2zkucocJjIEAcnxtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BzjyovEzXA79-WcmqTrs7FHFCqPy4czocFvE7T3WBNTmP8jyT1MN3ZrdpX-76hzLfKo6vGFDGiJ2DXWW7H47itXKw_FEf2m5HXWYFB_lMF00BImO_XxfXjdQmyEnMHksvpU7K_HreeP5NOzeMm_u7mj4SZD7r5C-7nqdClbbo0S-QVDx7MYb74ZBfOdehAXr7WrR2pY_LiI7QmXL-sQnCxuRYH4GxFRLr4-1To-ORXYG4Dlj30S1JyiryWtSoudcGAL1RBTFbdRwhlepoCw9WTZTmWkx5IpiY843ayQ92K-oxFZ3l9vgCoGjdrCeKv2BLvsui5TB4eXDEEKf-65a0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
مجموعه‌ای از پرامپت‌های متنی، تصویری و ویدیویی رایگان و قابل کپی برای مدل‌های هوش مصنوعی مانند ChatGPT، Claude، Gemini، Nano Banana و Veo که امکان فیلتر کردن بر اساس نوع، مدل، دسته‌بندی و امتیاز وجود داره.
🌐
https://freeprompts.io/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7028" target="_blank">📅 17:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7027">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSPHpELKHNgCu3r4OEOE_UKSWpp0bJUkakrj9JWH5jZQLRX54FwwjAGDk2sbXBe0Ll8MJY2U8yEO6Rs86EkqXAegGzGO6xAGayNlgPrqwexTtWIxec5XU_A6-7yN_tR0Zza94qE4pfX83KTBz7kZrk79TixFdnpoSOnjEeqjnmd8J2kPAiJgjUV_oHHFHzeS5jVsRE0lJeAtB5a6ZKXeKD7lTeUwT6LQulEP2Z7W2cGkXP17DEhr_wLuzN12KjiBYFV5yUMjt0Txf42mG5E_UFlYU4aefjmJbc0VzmVDfYMXlxtevcPsjoeEiAm5fHQL5vESFpcT3QC-ZCHxzbkELw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛠
استفاده از Claude Code با مدل‌های رایگان و لوکال
محیط Claude Code عالیست اما استفاده از API آن پرهزینه‌ست. ابزار
Free Claude Code
یک پروکسی هوشمند است که اجازه می‌دهد این محیط ترمینالی را به هر مدل دلخواهی متصل کنید.
✨
ویژگی‌های اصلی:
🔸
پشتیبانی وسیع:
اتصال بی‌دردسر به API سرویس‌هایی مثل DeepSeek، Gemini و OpenRouter.
🔸
اجرای آفلاین:
پشتیبانی از Ollama و LM Studio برای کدنویسی کاملاً رایگان با مدل‌های لوکال.
🔸
پنل مدیریت (Admin UI):
رابط کاربری تحت وب ساده برای تنظیم سریع کلیدهای API و تغییر مدل‌ها.
🔸
مسیریابی هوشمند:
امکان تخصیص مدل‌های سبک برای وظایف ساده و مدل‌های قدرتمند برای پردازش‌های پیچیده.
این ابزار روی ویندوز، مک و لینوکس به‌راحتی نصب می‌شود.
📥
سورس‌کد و آموزش نصب در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7027" target="_blank">📅 16:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7026">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2mqryos4Y4KTpWJb0C2IiBH9vtdejXbMUufkvp8VzUK4TVwtr7QWPzR12kDVQq7DI1hppNrD9-UG4Zh_Sx8mVBvR1WWHlkdgcYRwZ5dLgsWuIayarW8CEtNqe2IarZyDbkp8aBVB_H0i19AVJGj7pQ_qjPdILYcTulN4oliGiur9HrsHWHdxp6KrjzWOZlDaVxPVUAbxi4t60GNisWpRDyvonPnDSYHO2QVE18TlJc1cFhf2tvcxeijC-qv93GbCe0rUKRpmKJGwuX5Z7ErEcoSgDTvaBAfQ8bQKb0vmMX5zI62taxeE5oyXoKKoKZpvw7MEe5P5AD2NLVFS3fLlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
معرفی و آموزش راه‌اندازی UAC SNI Spoofer برای ویندوز
یه کلاینت متن‌باز، سبک و دو زبانه (فارسی/انگلیسی) که با متد SNI Spoofing و هسته Xray کار می‌کنه. تو آپدیت جدید فایل‌های پروژه،
آموزش ساده و قدم‌به‌قدم راه‌اندازی
هم قرار گرفته تا خیلی راحت‌تر بتونید وصل بشید.
✨
ویژگی‌های کلیدی تو چند خط:
🔸
پروفایل اختصاصی اپراتورها:
تنظیمات کاملاً مجزا و بهینه‌شده برای همراه اول و ایرانسل (بدون تداخل با هم).
🔸
اسکنر هوشمند:
تست زنده و پیدا کردن خودکار سریع‌ترین SNI و مسیر.
🔸
مدیریت بی‌دردسر پروکسی:
ست کردن خودکار پروکسی ویندوز و بازگردانی امن اون بعد از بستن برنامه.
🔸
بهینه‌ساز یوتیوب:
استارت سریع‌تر و روان‌تر ویدیوها با قابلیت گرم‌سازی مسیر.
🔸
نسخه پرتابل:
اجرای مستقیم بدون نیاز به نصب پایتون (فقط کافیه فایل ZIP رو دانلود و اکسترکت کنید).
📥
دانلود نسخه پرتابل و مشاهده آموزش راه‌اندازی
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7026" target="_blank">📅 15:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7025">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBreak The Barriers</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3X-UI-MANUAL.fa.pdf</div>
  <div class="tg-doc-extra">3.8 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7025" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دفترچه راهنمای کاربری پنل 3X-UI ثنایی به زبان فارسی
✔️
راهنمای جامع پنل 3X-UI ثنایی که برای نسخه‌ی 3.5.0 نوشته شده است.
منبع:
https://github.com/yukh975/3X-UI-Manual
@break_the_barriers
💎</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7025" target="_blank">📅 15:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7024">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i19IeDHEGsrcumpZ5y8bnpi17oOJS2dlspSG8rNuNiRLjhZAH6_TBtCEZgPw0YsX8Xyo_O2wrqCaQvXjSNjAji9xzS4LMIPcOcKHBrsBkrj4o4ieg6A0UGY1pb5c2zfeCLPdv3AZVrBZH6xZRDaT07MqRKv0Q3QFmHweYOSA7iVK3bmQ-GCtbxY9Y6sYStH3r_D6U8CMzOdjSfzMbvM7Oq1ut44asaMr2-K_B0PwgP9cNKnSZlLih5050lgMTzCKMsjoGukPNrdJ75tMbq5ZQ4OLiyYFgw8Tq23t8QL06u8RWrgVGw38-c6z-gCYpNiV7-801MhCjg1s5cbZbRPbQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
؛OpenAI قابلیت جستجو در ChatGPT رو اضافه کرد که به طور همزمان در چت‌ها، پروژه‌ها، تصاویر و اسناد جستجو میکنه.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7024" target="_blank">📅 14:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7023">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">📱
معرفی Hermex؛ کنترل کامل هوش مصنوعی اختصاصی از روی آیفون  اگر با پروژه متن‌باز hermes-webui یک دستیار هوشمند اختصاصی روی سرور خودتون راه‌اندازی کردید، حالا می‌تونید با اپلیکیشن بومی Hermex، کنترل کامل اون رو روی گوشی آیفون خودتون در دست بگیرید. این برنامه…</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7023" target="_blank">📅 13:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7022">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">📱
معرفی Hermex؛ کنترل کامل هوش مصنوعی اختصاصی از روی آیفون
اگر با پروژه متن‌باز hermes-webui یک دستیار هوشمند اختصاصی روی سرور خودتون راه‌اندازی کردید، حالا می‌تونید با اپلیکیشن بومی
Hermex
، کنترل کامل اون رو روی گوشی آیفون خودتون در دست بگیرید.
این برنامه کاملاً رایگان است و هیچ اطلاعاتی رو برای سرورهای واسطه ارسال نمی‌کنه؛ یعنی گوشی شما فقط نقش یک «ریموت کنترل» رو بازی می‌کنه و تمام داده‌ها و پردازش‌ها روی سرور امن خودتون باقی می‌مونه.
✨
ویژگی‌های کلیدی اپلیکیشن:
🔸
رابط کاربری بومی (Native):
ساخته‌شده با SwiftUI (مخصوص iOS 18 به بالا) با طراحی بسیار روان، بدون نیاز به واسطه‌های وب.
🔸
چت زنده و هوشمند:
ارتباط در لحظه با دستیار هوشمند، امکان ارسال فایل و عکس، و مشاهده روند استدلال و تفکر مدل.
🔸
مدیریت همه‌جانبه:
قابلیت مدیریت تسک‌ها (Cron jobs)، مشاهده مهارت‌های نصب‌شده (Skills)، ابزارهای آنالیز و بررسی حافظه مدل.
🔸
شخصی‌سازی کانکشن:
امکان اتصال به سرور از طریق HTTPS، پراکسی معکوس (Reverse Proxy) یا شبکه‌های امنی مثل Tailscale.
🔸
بدون هزینه پنهان:
فاقد هرگونه تبلیغات، سیستم ردیابی (Tracking) یا پرداخت درون‌برنامه‌ای.
📥
دانلود و اطلاعات بیشتر:
لینک نصب از App Store
(یا جستجوی Hermex)
🔗
سورس کد پروژه در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7022" target="_blank">📅 13:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7021">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmfcn6RdtgZrz0EARjBCM5Qp_g2H3bZqvTk_KuhYmcdjbwKrlL0j9OmNwnQtqCYOkCtkB_vd2NvqQoCssH-FtzlvXsNqi-stsKYY-poy0rTmkph-lxJwOzIngNSPF2YdOL7cxPPZFk4Jk1KDK3RFw-Yfop-LcltHxjD1BUPApeCkKrmLNDhWY6Od4JFuwtMZwczLiUiM22Pt_yqC2MrSmE9rP9ZE6OhOoplQXYhAsRcO3UKlA66IBMDMlJqzMZQj7wXfd_4rX6lFOHq6WKKXzoUkluSTBBqxk6Omlz4vE_V4ms99HyGg4Iq43t5ITJOWQIMSQrDNuca8b4x7occ4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7021" target="_blank">📅 13:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7019">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDXnvZ54RWjFMsQqnZlxAwAdhf_hz4Kq2i4C-g_-1RMGCGt2ZY58Tn1Hb29auvkoneKsKT9hvh4LqR4qLuqVEubE-3yv1MSpS5xhGJZ5EXljAfjs0bcMXW1OqwOa_R62AZAq6k5PV1QOn2MliLqYXRMZQ6ury-WhKxwFfLkyUSiCSyJQPSbRtrtq881JiNONQ3SY42lNg2F6y_XbfBjN6PRIDYTcARVT8yWA7RfCQFPOp2fs-AwKy4ZNSbHfU8kdm9HDIamW4Md_jGaHx-3Z3X9U7SRTBtoVLwid1Yzo0smOL0KGYG80dBbRKUfLavvtFuf6UUmLBFbRmFEyfMaZog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">RohanKar Launcher
🎮
یک لانچر دسکتاپ برای اجرای مجموعه‌ای از بازی‌های کلاسیک
PC
که روی
Archive.org
منتشر شده‌اند. با این ابزار می‌توانید بازی‌ها را از طریق یک رابط کاربری یکپارچه مرور، دانلود، نصب و اجرا کنید؛ بدون اینکه نیازی به ساخت حساب کاربری داشته باشید
👤
مناسب برای علاقه‌مندان به بازی‌های کلاسیک که به دنبال دسترسی ساده و سریع به آرشیو بزرگی از عناوین قدیمی هستند
🎮
Github
🐱
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7019" target="_blank">📅 12:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7018">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElEc8MZYYvsSmqt_ogbe9O-4I3vQxzED_KmGgX6DnC736EHaraTQaV3_WYaYrTgoOqr4oj09Oqgf51-sFb3QX4WXJ0xCP51QwMdtfVK2SdvZfhdl_5R7WNvASmZM-9QxHvrT9KM1SqAuZ8yO_hHbEaW_Nn0bz01WBS7Q_J8UP2zTDSt5liGocBa0j_YxRXORXTseezf7PPCAxvilRoJVMYLokfhmROuj6LtDJa8cTbkDXvHZ811I54cHpH9n0cqwZ7qHC73a8LJGrTwmx5yFebBA2ynWJbj7_FbwnZwdsU81pKL_c97M-nM4cTZdj1gu2ZjKBeK_PAsFvwdB4Qbyvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
هوش مصنوعی برنامه‌نویس Grok Build متن‌باز شد!
شرکت SpaceXAI دستیار قدرتمند
Grok Build
رو در گیت‌هاب منتشر کرد. این ایجنت (Agent) هوشمند مستقیماً تو محیط ترمینال اجرا می‌شه و مثل یک برنامه‌نویس کنارتون کار می‌کنه.
✨
ویژگی‌های کلیدی تو چند خط:
🔸
همه‌فن‌حریف:
درک عمیق سورس‌کدها، ویرایش خودکار فایل‌ها، اجرای دستورات (Shell) و سرچ در وب.
🔸
انعطاف‌پذیر:
دارای رابط کاربری تمام‌صفحه ترمینالی (TUI)، قابل اجرا در اسکریپت‌ها (Headless) و اتصال به ادیتورها.
🔸
سبک و سریع:
نوشته‌شده با زبان قدرتمند Rust (دارای نسخه آماده برای ویندوز، مک و لینوکس).
🔸
متن‌بازِ یک‌طرفه:
کدها کاملاً در دسترس هستن (لایسنس Apache 2.0)، اما فعلاً مشارکت و ارسال کد (Pull Request) از سمت برنامه‌نویس‌های خارجی پذیرفته نمی‌شه.
📥
سورس‌کد و دستورات نصب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7018" target="_blank">📅 11:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7017">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMk-xt3r11fv2_tbdADA4dgnH3aH0Pfo2fy_JEkz8-OAdrKkI67U_KN8j4DcObk-ZAxH7VpUhOG95o3Kgrn8w5hmX5meK1cDN-ThmkeU39YtsCEDy4GpmzQTHq9hX4xVIUb5p1kh49YPtmdvAhVmafy-bK_2qb1_xTPqMdqBtzlgDiSiFn2FbxNnt38eLeWBePsB7T8cOVJex60mQNNHFdnSDqg94i6zd1ZtgXjwBIZ0G_Nq7glReMfEmkgjkYuswD8WjzsBH5wy2Pb39tpUQXuzm2M5BV91giHlMjufh1VpbC5HM4HDH_zMUD9p9yjch7PBaRhGqL2_-Ya8uIpEfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛ OpenCut جایگزین رایگان CapCut که متن‌بازه و مستقیم در مرورگر کار میکنه
🔥
🔹
این پروژه هنوز در مراحل اولیه توسعه قرار داره، توسعه‌دهندگان وعده دادند که امکان دسترسی به ویژگی‌هایی که در CapCut فقط برای مشترکین پولی هست رو فراهم کنند.
🔹
در حال حاضر تمام عملکردهای اصلی ویرایش، تولید زیرنویس، تنظیمات خروجی و .. در دسترسه.
🔹
به زودی یه کتابخانه از جلوه‌ها و انتقال‌ها و همچنین یک سرور MCP برای کار با هوش مصنوعی به این نرم‌افزار اضافه میشه.
🌐
https://opencut.app/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7017" target="_blank">📅 11:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7016">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLKvdlfLIOqIxI2Rp4qByfmfURqEbvwHyzMREW5EVXe6zFPVzC8Frjsl09AwbpntvnvJGzcylWXVETVGUK6kxWF5BE3SsQwtaPVlbrt5Ps-Ne1D8HEfhHIAxPFX_hBpacUqkX63pjga3sgoYKeoiNXhmzHi12ZrZE8Sr5aM3UA-YGZgBAgW4GDvuvQVdH2hpgO-KcBXMr1hBU7nqyMqjPBMPTJdF4YaatH_BRYh4ssqq7EnQr63vwHiVviRu50j7WjuQF7GdFlcNbs4GMV7LNFLG47vC69q5O5bcvh9ULZ-6Gq2Duyb8ElshhDLG9RLmsEuzANl-5vcc2AHn4AyDUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
یه کتابخانه عظیم از دوره‌های آنلاین رایگان
با CourseCorrect میتونی هر مهارتی رو یاد بگیری
🔎
فقط بنویس چی میخوای یاد بگیری؛
سیستم خودش دوره‌های مناسب از منابعی مثل Coursera، edX، یوتیوب و… رو پیدا میکنه.
✨
اطلاعات هر دوره:
🔹
زمان تقریبی یادگیری
🔹
سطح موردنیاز برای شروع
🔹
چت با هوش مصنوعی برای بررسی اینکه این دوره مناسب تو هست یا نه
🌐
https://coursecorrect.fyi/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7016" target="_blank">📅 10:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7015">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuQMTA28r5Ls1Re1YY0aL4fjP7r69-3P95HGEpYjVJQh5QzRIgOQvUJ-Qr9PclUDRdUmdLLWhtrvXlh32uy1eTa0RN3lc7V-TiDJYkzH_wW6sn2-yL_wenDCcx6y5k1TA0j6Hv3xy3gF45gojHWbnoMq9a6b-1RoKaC6I7ODbhwLvodkdRz4UkQNDAqX4oBIoXQhXUpmGeep2t0QJZKfYNA8pYInIIeWxOZA-XI5Crex3ry2Pp6zSOBNeZRgLDs95HlHCCzIZltfyIsBzxIaByb9G7qDia_6plCIX7L-lEu2N9gJBcSapJmgzdcA3o-QZud2PasrNg3t6LGMH4GDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔓
دور زدن محدودیت‌های پولی مقالات با یک کلیک!
این افزونه مرورگر به شما کمک می‌کنه تا بدون نیاز به خرید اشتراک (Paywall)، به متن کامل مقالات در سایت‌های پولی دسترسی پیدا کنید.
✨
این ابزار چطور کار می‌کنه؟
🔸
فریب سایت‌ها:
افزونه خودش رو جای ربات‌های موتور جستجو جا می‌زنه؛ در نتیجه سایت‌ها تصور می‌کنن با یه ربات طرفن و کل محتوا رو رایگان نمایش می‌دن!
🔸
استفاده از نسخه آرشیو:
در صورتی که سایت خیلی سخت‌گیر باشه، افزونه به‌طور خودکار می‌گرده و نسخه ذخیره‌شده (Cached) همون مقاله رو براتون پیدا می‌کنه.
🔗
لینک دریافت افزونه
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7015" target="_blank">📅 09:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7013">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6514ad748.mp4?token=jjgDuvEL0jUQnjcmjrQ1qHNfbnZlE0FuyArHqvfp0CQNiiBy4QcAwmUwVdTRCVKt-wkGCnAkUo3Gg8VRndzviTM5t4oLbrXaIDWNWhrFnZHd9Qa-zrbktWkTmFFBCytDLfdrANuC1GDcFcOukbxHx7DpghM-oNemoqXHXw_1nuErhmgvv_nxQonuapbMJaAToydQdqcqDdlVCGMM6THHaRpOh4Xcwn6RqMkFUsvw3UnuZ6YIbOIzDIAKznXZNCwdjFmLUc3jaEOQc9hGuSoNPouoMje2qzbG5bicpUQzUxwOIqMzKgmHcL88d6eLJOiGbrtj7T9l7j4zBLN8u--7sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6514ad748.mp4?token=jjgDuvEL0jUQnjcmjrQ1qHNfbnZlE0FuyArHqvfp0CQNiiBy4QcAwmUwVdTRCVKt-wkGCnAkUo3Gg8VRndzviTM5t4oLbrXaIDWNWhrFnZHd9Qa-zrbktWkTmFFBCytDLfdrANuC1GDcFcOukbxHx7DpghM-oNemoqXHXw_1nuErhmgvv_nxQonuapbMJaAToydQdqcqDdlVCGMM6THHaRpOh4Xcwn6RqMkFUsvw3UnuZ6YIbOIzDIAKznXZNCwdjFmLUc3jaEOQc9hGuSoNPouoMje2qzbG5bicpUQzUxwOIqMzKgmHcL88d6eLJOiGbrtj7T9l7j4zBLN8u--7sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
انتقال فایل بین تمام دستگاه‌ها با PairDrop (بدون نیاز به نصب)
ابزار متن‌باز و تحت وب
PairDrop
سریع‌ترین راه برای جابه‌جایی فایل بین ویندوز، مک، لینوکس، اندروید و iOS است.
✨
ویژگی‌های کلیدی:
🔸
انتقال محلی:
شناسایی خودکار دستگاه‌ها در یک شبکه Wi-Fi.
🔸
انتقال از راه دور:
اتصال دستگاه‌ها در شبکه‌های مختلف فقط با یک کد ۶ رقمی.
🔸
امن و مستقیم (P2P):
ارسال فایل‌ها بین دو دستگاه بدون ذخیره در هیچ سرور واسطه‌ای.
🌐
اجرای مستقیم:
pairdrop.net
🔗
سورس در گیت‌هاب:
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7013" target="_blank">📅 08:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7012">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yi7acFJjFA5brtz4O2Plwm3XlJ5_P2NfbsBWc7t3Kz29nFWDqcNmxsZ3Smf3F-5WT7ydAw9-hGH-vlxzAUHvruyPZDOSUJ70qbW6U40jna_YzR9IqYQ76BHvJXKT9Ero-XLCAEorFOM8qzmzEC_MngylLVnNVo69EA4z0WDZ18zCch11p8RxD2iS3vvRiR6fGJu-YlPwA_tov8y79xnM1C6zQKQt99WT_JIUkqDR6tMij-FHCKtvxF06R9zxjLbVHIc1Umi6MgCJEuu6IhaWkfHiGRrew37IN28UoXzzeoVYUqoBQ_k6ZHsKZmOCmKlUY78SL3M4-NB9DJkrGex9YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دریافت اکانت ۳ ماهه رایگان Avira VPN (نسخه Prime) (
تست نشده)
یه فرصت عالی برای دریافت اشتراک ۹۰ روزه و کاملاً رایگان فیلترشکن قدرتمند آویرا، بدون دردسر و خیلی سریع!
✨
مراحل دریافت اشتراک:
🔸
مرحله اول: وارد لینک کمپین آویرا بشید و با یه ایمیل (واقعی یا موقت/فیک) ثبت‌نام کنید.
🔸
مرحله دوم: ایمیلتون رو تایید (Verify) کنید و یه پسورد برای اکانتتون بسازید.
🔸
مرحله سوم: وارد داشبورد بشید؛ تو بخش وضعیت اشتراک (Subscription Status) می‌بینید که اکانت ۳ ماهه شما آماده استفاده‌ست!
📥
لینک دانلود اپلیکیشن از گوگل‌پلی
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7012" target="_blank">📅 02:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7011">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4yaXNcuM-7ap_cbWRgSGazO9oXal2ETLX00VleOVKGj3jn3iEzD1B3sGT3VhmP8x2L0kl4U3Rsvc42U6N5HGvishW_9QkjInGvI8PxnhzLhgpbdP-mchlcHpoHCYwK8zGxnqiI_NrJzOeW7Xwr6gadxpg7AUPRHo03M6-BD3o7YP6pScBl4mbG7xBQ2W0OdUUUib2RFqLkQM1-f4LVKytCsww9TCFHC7pGQTEF8YJm4zVHm61rHC8A7gQMdzG5PDVq5BbnZvjgU2hGm9nq8-4DjHa2X02HlVDBxz_4g-L5o3dRpWHlRVq0oFISx2YwjeTldIA7gVbHSx8FgpD6eCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار از زندان DeepSeek
👇
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7011" target="_blank">📅 01:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7010">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🛡
آموزش ساخت کانفیگ Bepass (متد یوسف قبادی) روی Nekobox  این روش کاملاً با پنل‌هایی مثل نهان یا BPB متفاوت است و با استفاده از Worker کلودفلر و پلاگین اختصاصی Bepass روی نکوباکس کار می‌کند تا نتیجه متفاوتی برای دور زدن فیلترینگ به شما بدهد.
🛠
مراحل راه‌اندازی…</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7010" target="_blank">📅 01:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7009">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🖥
نسخه گرافیکی ویندوز فیلترشکن Aether منتشر شد (آپدیت v0.3.0)  اگه یادتون باشه قبلاً ابزار خفن Aether رو معرفی کردیم که بدون نیاز به خرید سرور، فیلترینگ رو دور می‌زد اما محیطش متنی (ترمینالی) بود. حالا ابزار Aether-GUI اومده تا همون قدرت رو با یک رابط کاربری…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7009" target="_blank">📅 01:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7008">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🖥
نسخه گرافیکی ویندوز فیلترشکن Aether منتشر شد (آپدیت v0.3.0)
اگه یادتون باشه قبلاً ابزار خفن Aether رو معرفی کردیم که بدون نیاز به خرید سرور، فیلترینگ رو دور می‌زد اما محیطش متنی (ترمینالی) بود. حالا ابزار
Aether-GUI
اومده تا همون قدرت رو با یک رابط کاربری تر و تمیز و فقط با یک کلیک در اختیارتون بذاره!
✨
امکانات برنامه و تغییرات این آپدیت:
🔸
خداحافظی با ترمینال:
دیگه نیازی به دستور زدن نیست؛ یه دکمه Connect می‌زنید و تمام تنظیمات و اسکن‌ها تو پس‌زمینه خودکار انجام می‌شه.
🔸
ارتقا به هسته جدید (v1.1.1):
مشکل اتصال فیک کاملاً حل شده؛ پروکسی SOCKS5 فقط زمانی فعال می‌شه که تونل واقعاً تست شده و ترافیک رو عبور بده.
🔸
ریکانکت هوشمند و اتصال سریع:
برنامه آخرین مسیر سالم رو یادش می‌مونه تا دفعه بعد بدون اسکنِ کامل، درجا وصل بشید. اگه اتصال هم قطع بشه، خودش خودکار ریکانکت می‌کنه.
🔸
فوق‌العاده سبک:
مشکل مصرف پردازنده برطرف شده و مصرف CPU برنامه وقتی مینیمایز (تو بک‌گراند) باشه تقریباً صفره!
🔸
پنل پیشرفته:
می‌تونید پروتکل‌ها (مثل MASQUE یا gool) و نوع اسکنر رو خیلی راحت با رابط گرافیکی تغییر بدید.
این نسخه در حال حاضر برای
ویندوز
(فایل‌های نصبی exe. و msi.) آماده شده است.
📥
دانلود فایل نصبی (از بخش Releases)
🔗
صفحه اصلی پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7008" target="_blank">📅 01:18 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
