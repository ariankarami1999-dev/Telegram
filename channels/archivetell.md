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
<img src="https://cdn4.telesco.pe/file/u6v_PWscPdHxQRLRtzC6hsKAZGngIVUifBye2WlS5HcOzIdydatekAAWqAbuWT50theiMDOx2eI7iIx05v4-XripLm5LDJK_Y9pgWJ-zbAIBjoKpCTMNgB2iHUqEKnmt5ES4TxaGkLFt-N8CHdfEtsUXNA6hCknzzJgh3f0OhzGuHJi0n7uphAljkGrQ0VWaF64Jjm8nG8Gud4Qtu74yusLlglbiv5ZYlZii5oYRUVXP1dFtRe6swecQ65fOEtddLuktr_ea9LFsMhBY5z2mC7_MfFH8i-PHIqP9pGDG_CEFu1IQ9tMnVdJ6uUrTGsjEaBQUt515b1h2jf3mXZWw3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.83K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 13:15:04</div>
<hr>

<div class="tg-post" id="msg-7108">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxQVuf_EVL042FM6CR2slZX1cMQMQ4kmG8KAfgfnHX80LKnA_J5_93PIkAndXa9k_z3HfDLwqF7Iehk84iMi6DWJcZHuMC48KpDSrmlLOXwVcMraH22zO3HHvD1YTWg7MXctjbzz1w8LwxFfM2F8GOxRavAnFyGQA_zzgttjVWMEex3wq73baCfEzhdNsDMQjRTQ4XRL7s3lISGsSrp-MR2XGnZSqf9uyYhsIFMsF39Zq8xo04GVQ3l3wfe0fqm8VwXEPgney93H4DcYcFljXIpoaIWZBbrARiB7C6P6R71cyvyyry9HXUYwWjQJJGOi29jMEiC-_w72oLKFxDh3ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 377 · <a href="https://t.me/ArchiveTell/7108" target="_blank">📅 12:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7107">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng8WIGXUPv9GqNmNYcqnmQ8CH417i2O7FwiME5KlQW12y4m0mMiwoYqfuw5ULUSr2siUnyBlvhc2NqOq9WxZM83f1dRu2K2MyQFqoSAxGhQnG9pVu1hOu-8h2P2ET_k9r7bOrVYRzdbPNYeIXauuXHvOocQ4qcVqghiPK2ZAtB6rd0Y_Z6XtIdjgmvoAn_wULFaKAD460eFwfC4aZD7kSJcvIuF8K5IT0ihbXaguadQ6ul6Aw3_FRkIuK5AtXQ-drvNo38VJUPiFIZfVjTR-uYCYNwXfWoeHPQH9SqRtotvEXEyIYGEFDqXG9OAr8Lr_nZYccmXqY4fM3ZgpypmYVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 605 · <a href="https://t.me/ArchiveTell/7107" target="_blank">📅 11:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7106">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 608 · <a href="https://t.me/ArchiveTell/7106" target="_blank">📅 11:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7105">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 777 · <a href="https://t.me/ArchiveTell/7105" target="_blank">📅 09:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7104">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-Bx9ZSK9l43i9DZZlPx59_8E7AX4wuhypYM0_7nWLzXkxRZeJV877glX3NqriK83bxehMGnbDKOwRxkz3kfQdBGXPc62bhgz1gfMJ1k0csbvyrthmYj-ILW0sEV2Ux-7hQwovwIWEFQ_QvdiRCjlpVOYlDzGmRoPGBHysyn8zCmkqQSBDnXnP6ZCGidEOwkEjFhhgiokdD8mifAUbocBZOrpJ0W0O2swDecgkmSmNFnY6Lq4ur-ocro7FOFbrR9KpZ8EKl2J0Iull1r94DItGNov32yZDyNJzpmJLwvFxn0-PdJMS1rNfDcFi3ADUgwHSFiIavpLUZTP8Rehn23TA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 784 · <a href="https://t.me/ArchiveTell/7104" target="_blank">📅 08:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7103">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 845 · <a href="https://t.me/ArchiveTell/7103" target="_blank">📅 06:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7102">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b91143b5e.mp4?token=gya4vb1qdd_ppS7i4GQdA78Bdiymt1j9_GaVKFXKWwPEdJoJwLprBWQHCbWqIKeUG-g3thTZo8M4eXaGucW4WOLZ5z6oaPi-Cs5qsyc92R4C_mQiZI7SnURwb5S_bRdu-HQGXOpgLBt_m--y6l6qNKCo_qPVrVyMrdBWtt4O6H2rpfTz2rW8dBv7ybt1Yq603G00dsAyOMn00eubHWuC2QpIQniT_6fkQJ4JHEGS-WD3IjminSBaIrm5w2TaiIbIjEs32DfWEKzy2TRgvKF-VivOKFupU8sjSPh42qo88IUoNM8zuLZXq53DtHFofZqBnikjlrJh64nj0sTG-H1w0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b91143b5e.mp4?token=gya4vb1qdd_ppS7i4GQdA78Bdiymt1j9_GaVKFXKWwPEdJoJwLprBWQHCbWqIKeUG-g3thTZo8M4eXaGucW4WOLZ5z6oaPi-Cs5qsyc92R4C_mQiZI7SnURwb5S_bRdu-HQGXOpgLBt_m--y6l6qNKCo_qPVrVyMrdBWtt4O6H2rpfTz2rW8dBv7ybt1Yq603G00dsAyOMn00eubHWuC2QpIQniT_6fkQJ4JHEGS-WD3IjminSBaIrm5w2TaiIbIjEs32DfWEKzy2TRgvKF-VivOKFupU8sjSPh42qo88IUoNM8zuLZXq53DtHFofZqBnikjlrJh64nj0sTG-H1w0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/ArchiveTell/7102" target="_blank">📅 03:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7101">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 977 · <a href="https://t.me/ArchiveTell/7101" target="_blank">📅 02:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7100">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 903 · <a href="https://t.me/ArchiveTell/7100" target="_blank">📅 02:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7099">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0afbe9c883.mp4?token=YHDiwq7eUknMXg9qLXfR-c-IscUsDtNyzcQ11sJ3cwuOrtXfXLc4mVD-hYWD1eWR4g7OTuQyb4AuqQExX8trAWUBzLsamKztIq9wtaU74nFXpR7EAelbMtidFxg0xGAAq9C37_XAw4nb58BJ5iWDJpImD8tMs60b6EmkLe1GEQfWze5b3gkg0_kZ0qbS2eD-4usZhEwiuIT964eRppwLO3qSbAKF53D-W25sxa0zvU5IwAh1wLx09aTpgWkmK6uiipLe6Katz9eASmZx64j5Fne1Yc8HZLVrHEpSCZ16QblVj6Jg2J7y2iVk8PsQuq6JVRAzJ5ALALDJy16cdpNoGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0afbe9c883.mp4?token=YHDiwq7eUknMXg9qLXfR-c-IscUsDtNyzcQ11sJ3cwuOrtXfXLc4mVD-hYWD1eWR4g7OTuQyb4AuqQExX8trAWUBzLsamKztIq9wtaU74nFXpR7EAelbMtidFxg0xGAAq9C37_XAw4nb58BJ5iWDJpImD8tMs60b6EmkLe1GEQfWze5b3gkg0_kZ0qbS2eD-4usZhEwiuIT964eRppwLO3qSbAKF53D-W25sxa0zvU5IwAh1wLx09aTpgWkmK6uiipLe6Katz9eASmZx64j5Fne1Yc8HZLVrHEpSCZ16QblVj6Jg2J7y2iVk8PsQuq6JVRAzJ5ALALDJy16cdpNoGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 914 · <a href="https://t.me/ArchiveTell/7099" target="_blank">📅 02:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7096">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/ArchiveTell/7096" target="_blank">📅 01:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7093">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WiJv654IFmxFr72YnnENT6nUMAoVjEceoU1CSsyWhOeXzJjWsKs6X3h4T7rSFXFQWH7DxaKXo84wdHEDg9JtFsu9JfuuhwN0fR6SswwdIwDsOioHTTL1-97Ht6ruI8beEcgIX1C1UfMpyXDjM3xP6dikHzljt5t8rpQYV94KthPO0I6Kl_btgY1hISgpgmCfK-6XIj03ZY10N8NVrpwokASgcqfinBKEnfuKyi6QNsSuMoShaz2CpluLFtRda_lbV6tayvFVBuMMTj_KtAYGtNCxAQ_eR4_4QYJ9OClJEEw0Dpmwn_TTpzZjmKDg20eXxrPq5eOqovKJH10ASGkHKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jcj0ohlIQURh-n-2TDSriTKlBhDeCKbk7z_wjdvrd3lLzKl2nyGUJAWlVVUX5je3V3DokvNi3NilSPUthMLr9mCr5-ZnFaapB5kswRyZW-0cbcmZ4AoxqIuhyK0jK9CgRHuA1uZgzViYQcsYERqU3mnekeRvUbWeR2BFwY1PMqcTS0ci5LPCAcv5HPC_guygFsBYDaYsoVuARESop22qEe3vlT4B18kX1AhcT8eYw1xI4ORH4nl7Wu0qscHsE8lJCRsrFuMqv0FOgg97tZwW9JFtyIPcKsnmxF5oulWthMHi5NtJCRIziY2Tu4CK_6K8epLXU7NcH_-hHp1Rs-l28A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏دسترسی رایگان به اکانت یک‌ ساله ‌ Notion Plus⁩
🚀
💎
‏با این ترفند، تمام محدودیت‌ها رو بردار و از قدرت مدل‌های پیشرفته هوش مصنوعی مثل   ‌Opus 4.8⁩ , GPT 5.6 Sol , Grok 4.5⁩ , ‌Gemini 3.5⁩   برای مدیریت پروژه‌هات استفاده کن.
⚡️
‏برای فعال‌سازی و آموزش گام‌به‌گام،…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/ArchiveTell/7093" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7092">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7092" target="_blank">📅 22:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7091">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX8oHlhISpw8wg0jiAw3uzDQ0Qn-eJZqjEbNX30gb2hsCJtvyJHRBiGJKNdupfxZs0WRxWd_FllI_6Zl_OnRLCjjcbkUlYfVHpEPOXvid0yZofwesyVhL6J0zjGGRE_28jB7K34hK_m20npYBwjcSUHHJaK9AGITdMH2udSgobKlY6X8lm74xGtl-WEx4Gi0i67RKABuOFP75zPfJafBomjnUiK0k-XbBFaX1I2_yLNn7LA06kQ9cSBNRS82_4cp7q7hugS2x4_ZCrO6WWlFWtewxMlkYn5Yem75LV5vVIUXX8-WpBvGP6fUGaepZBn0H7SZh0_X1tjE6ECNUvOw_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7091" target="_blank">📅 22:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7089">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZTMw-SNHC23jLzTnjJgQKv-BOcjNweXUPVbgU2xxJvNVfvwvRISvBTGCcA3yiiG_eZ5xkAAGrBLV8e-BIeOipyVVdDQh_CXIrSVph40DatifW36JeNOopAgmutiYJB20KF9CSa6aYXDlD8dXnh0J5vBp39dby2jiWAqLORQdsegje4GGAeenj5CI164cZnw-Vo7WM0MKDIboM_Fo8GfwxKze5qBZxresU8Y5o5d4X8oY1BdbwOlpY6SzZvuvtZrEeD9Yl0aUaNbG21iJPc1O4VI7KDR8QeGprzzVRDe3xpoGdz-aEPvWqs9QPUb-dy9_NWkSiaGpMfrXlsSAjDG0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7089" target="_blank">📅 19:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7088">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🤖
دسترسی رایگان به مدل قدرتمند Kimi K3  یکی از قوی‌ترین مدل‌های هوش مصنوعی رایگانِ حال حاضر با کانتکست عظیم ۲ میلیون توکنی که در بنچمارک‌ها رقیب جدی مدل‌های پرچم‌دار محسوب می‌شود.
✨
امکانات کلیدی:
🔸
تحلیل داده‌های حجیم: دارای پنجره کانتکست ۲ میلیون توکنی؛…</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7088" target="_blank">📅 17:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7087">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7087" target="_blank">📅 17:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7086">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7086" target="_blank">📅 13:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7084">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">📱
اپلیکیشن Aethery؛ نسخه بومی و گرافیکی Aether برای اندروید منتشر شد!  اگر یادتون باشه قبلاً برای استفاده از فیلترشکن Aether روی اندروید باید دست به دامن برنامه Termux می‌شدیم. اما حالا با پروژه Aethery، این ابزار ضدسانسور و خودکار (که نیازی به خرید سرور نداره)…</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7084" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7083">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7083" target="_blank">📅 00:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7082">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🎁
پلتفرم Gab AI؛ دریافت صدها اعتبار رایگان برای تست پیشرفته‌ترین مدل‌ها  یک محیط چت و ورک‌پیس جامع هوش مصنوعی با دسترسی به بیش از ۱۰۰ مدل مختلف که در بدو ورود، ۱۷۵ کرَدیت رایگان (بدون نیاز به کارت اعتباری) هدیه می‌دهد و حالا با به‌روزرسانی جدید، راه‌های بسیار…</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7082" target="_blank">📅 00:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7081">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7081" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7080">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRMb_hZMYWMx8skg9TDNDfC80xDLoPz9AerAm2-ogwxfIM1hQVwdeEcHamRdIn3j4z2fz_dCvUjo5Mo77PITqtWA8EnU1AQ2mb2td0lz3K5ofq-PzK2vTsCPxNRo0qW0Up8997qpa3zgjfHztAQp0pyJleOQwDEL9DidDz_DAMvNVTFisdMhCZNixgoHMwJnDcIRWNZ2enAKmMghiQCiRDqOctwQkJGNCiI2Zzk_rOXE8sEbWgsf3NlqYfWg43knlHU1-kSIFpRcxOrm1aeeNIK3mHo4cqu9IJAAicNMkp_cjUiNSmQP9bKGdKqgm_IyOf5t4-ndcS78Nm0GzoHE0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/ArchiveTell/7080" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7079">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🌐
پلتفرم Api.Airforce؛ هاب یکپارچه ۲۰۹ مدل هوش مصنوعی  دسترسی جامع به برترین مدل‌های AI جهان در یک محیط واحد و بدون نیاز به حساب‌های مجزا.
✨
امکانات کلیدی:
🔸
تنوع بالا: پشتیبانی از ۲۰۹ مدل مختلف شامل Claude (Opus 4.7 و Fable 5)، DeepSeek v4 و ابزار صوتی ElevenLabs.…</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7079" target="_blank">📅 00:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7078">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">Gemini 3.5 Pro
از درد عشق تو خوابمون نمیبره چرا نمیای لعنتی
😂
💔</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/7078" target="_blank">📅 23:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7077">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7077" target="_blank">📅 23:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7076">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDhGuyYlC1BwS0i3jn5VRCJOKvxo6YD_7bs2I0ogfkkG0oz-dVZwYqQ4p2iPk2QdcwPNMQ9PyQkSwSZR6Q1xl7TxA0oHDrAW-XK8Ng2e651Z3cSvCGOfkcf71u3O7bfxhzCSMOab2n7G312G2PGMFPrGNdv7kT1eglHUD1Xg2awUKokY9L6czN6hKd7o6DENzZ3luIAtUCWWeNAukFRNNHeAgrE5HLyYBy_lxLfC3JdzR4Y3y_T1a1ebYqDQ0WqYolc6Q4z8o1P7Rg4SlCDwv2EtVCB0ADvh_G7s-qLrkb9YEWEJIA19HiW__KUw1QVm49Hy0sjAEqB5ZwrYcdEO6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7076" target="_blank">📅 23:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7075">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7075" target="_blank">📅 23:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7074">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">vless://df4bda66-59d7-4b79-abd0-0e4ee14d7c70@188.130.207.217:443?type=ws&encryption=none&path=%2Fws&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF   بزنید عشق کنید زمانش 24 ساعته</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7074" target="_blank">📅 20:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7073">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">vless://df4bda66-59d7-4b79-abd0-0e4ee14d7c70@188.130.207.217:443?type=ws&encryption=none&path=%2Fws&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF
بزنید عشق کنید
زمانش 24 ساعته</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7073" target="_blank">📅 20:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7072">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7072" target="_blank">📅 20:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7071">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7071" target="_blank">📅 19:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7070">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">؛MIT OpenCourseWare یه پلتفرم آنلاین رایگانه که توسط موسسه فناوری ماساچوست (MIT) ارائه میشه و بیش از 2500 دوره آموزشی رو شامل میشه
🎓
🌐
http://ocw.mit.edu/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7070" target="_blank">📅 19:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7069">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hk-gQ4PXK81bUI7jai90_dQzWOyYfw3o753PK84JR_uKj1z0YvxREHp8IqUp8KQyr5wK2taYl_hLHYtM2a8CKo6Y_98DEWGRbA76JaTo0Ayt-er91slLN5mO0lllcdq89QAYYonhFV73hIGBb-ykxD4OhhIInB0wCRhZ_Qw0z2-lzSNNsYtf1mfCqe8mJXcDSvoRdY9DuncTd3VUBwGXEIWXnPfKj6TAqXIN_Me89V1-KBeYrqqQiR2BEP49cxktnyXSmu9Vl6DLd7YVVMzJx5hz4V-CYbU63DAgnxa3h6sjk-tN7MwQS549Oh1z2tpZnus1Giaa3JPX_w4N79JI_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛Oh My HuggingFace برنامه کاربردی و متن‌باز برای HuggingFace که برای مرور و دانلود سریع، محلی و خصوصی مدل‌ها، مجموعه‌داده‌ها و غیره استفاده میشه.
🌐
https://ohmyhf.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7069" target="_blank">📅 18:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7068">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7068" target="_blank">📅 18:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7067">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2c18bdbfa.mp4?token=vBb8ZBfFisW32MLdYY7BiotNqTqlegMX8vQrHpHEKRXH4hm_VHw9Cmk-V7_T99F1htSi4PY2RSZuNtllI2AaudWhmOC0BnKm9SzmBA-v6g_PndCL6qwUbwgKPT7baLjzo-AweLLJ_OHqLjPl1dJ0RIsEcZBk9qh_MmAa_Y6GL6Jd7uJ-hKfDoMhwIYNzRASneXkeidEGez5U93p_LvnIxAX3ToroTb3qZVeENqslajvlBl9MkXKskPNcUm9c4Mxe_5EAeU8SoEAF21mmEH5r5LSTddrwMwR0IFXvobCdVUJ4bQoJ-qGGf0IeEmDgIimGT-jjHBbBC5ljHE9anaoPLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2c18bdbfa.mp4?token=vBb8ZBfFisW32MLdYY7BiotNqTqlegMX8vQrHpHEKRXH4hm_VHw9Cmk-V7_T99F1htSi4PY2RSZuNtllI2AaudWhmOC0BnKm9SzmBA-v6g_PndCL6qwUbwgKPT7baLjzo-AweLLJ_OHqLjPl1dJ0RIsEcZBk9qh_MmAa_Y6GL6Jd7uJ-hKfDoMhwIYNzRASneXkeidEGez5U93p_LvnIxAX3ToroTb3qZVeENqslajvlBl9MkXKskPNcUm9c4Mxe_5EAeU8SoEAF21mmEH5r5LSTddrwMwR0IFXvobCdVUJ4bQoJ-qGGf0IeEmDgIimGT-jjHBbBC5ljHE9anaoPLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7067" target="_blank">📅 17:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7066">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">vless://06069771-bef8-4730-b711-c51efcdad901@onlineprochess.ir:8880?mode=auto&path=%2Fws&security=none&encryption=none&host=tsrety.dpdns.org&type=xhttp#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF  تمام نامحدود</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/7066" target="_blank">📅 17:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7065">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">vless://06069771-bef8-4730-b711-c51efcdad901@onlineprochess.ir:8880?mode=auto&path=%2Fws&security=none&encryption=none&host=tsrety.dpdns.org&type=xhttp#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF
تمام نامحدود</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7065" target="_blank">📅 16:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7064">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIYuSr7cqNf3Q8VGR958aQZAxYH_juScF1boN0m5SX3Nx8OFQ8e8O-UMUAFQDrnCXeYYBkSnAK7kU2tYGsk5jiYpskyZ7E1ncNiok2d_HCnvjVj9kDFKeGu-lABeUOZOWfErgU_iydi2K2TWgZu0HFO20IkB1YxlbYJm_XPpXcvILY3EMzV4tvsd_yWgMimBJDszazGNfEbn9zCHPkT8HtDXSFB3Ny202phdDV4QGJFHXHtwij489i70DSxYl5f4Ye1EjxGtyvNiHSsBY491bTmlEKs115V8_SFRmDc0v9KbQfgkqnmHsfCmOUFj8dL8I1B6D9qfy5Eq5mW0OnGBvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7064" target="_blank">📅 16:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7062">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/01b871c31b.mp4?token=YHivzP56CeBCgJGILKlmg_4aziuXZTjgu5paiwEz_Wv8jWj_2jiFjChhrdw7AYiWo1zXr3wrqHrEJs6GenKVsdkR-pmXjP73oAziwlRBp7-37NeGPSt6P6_LFHsBCaUzvqq_RJTwIhXXh2qGsKOx1ArT7IDTzDWMq3vJ2b3eT3Bpo9u6WxW-A2cV4G2dc2jxUpoq9kxCJW5i66Mw2-R5NMmIWgHEytsxud6K82ErBOQZhW_Dlw0H8rB8DQovQCpG7RamZ6xWT2UYgVn85awFk_JkqMaZLBTvyehx_iywPuxDFBhjkEDxJnzpOuznnbL6s-ORNHCdCWJ8tnJGnWH4Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/01b871c31b.mp4?token=YHivzP56CeBCgJGILKlmg_4aziuXZTjgu5paiwEz_Wv8jWj_2jiFjChhrdw7AYiWo1zXr3wrqHrEJs6GenKVsdkR-pmXjP73oAziwlRBp7-37NeGPSt6P6_LFHsBCaUzvqq_RJTwIhXXh2qGsKOx1ArT7IDTzDWMq3vJ2b3eT3Bpo9u6WxW-A2cV4G2dc2jxUpoq9kxCJW5i66Mw2-R5NMmIWgHEytsxud6K82ErBOQZhW_Dlw0H8rB8DQovQCpG7RamZ6xWT2UYgVn85awFk_JkqMaZLBTvyehx_iywPuxDFBhjkEDxJnzpOuznnbL6s-ORNHCdCWJ8tnJGnWH4Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نسخه جدید گفتگوی صوتی Chat gpt منتشر شده و انقد طبیعیه، پشمای همه ریخته!
+ خوراک غیبت برای دختراس.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7062" target="_blank">📅 16:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7061">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7061" target="_blank">📅 15:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7059">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7059" target="_blank">📅 15:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7057">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7057" target="_blank">📅 13:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7056">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7056" target="_blank">📅 13:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7055">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKEj-xu-ZdvM1iqvijZg_PCVqOG7QXkF6p3jsQ0kxLJ2SeC2Q_v9t0QGVNS7RaqoFUSSbvAh7O8uZ2oOlinvQy1ZWUG_d80T4LIG16ZMmm2ND1zRi4rcKqHDLtXxXDqoaFd8wojKg7K4wBijya1bQVJHyZg37gZXoXHHCezFBjS-hrpveAf6b3zhsf2KzX-dlYSzFTUM-HE7B3aZS6Hwb2qOzmPfgLzN1UlapTGqztH7PMyK2obkfOJ3GZnQ8qmfbXwAM3pN6_Clxgqfnws_32iOP5NFhkEAo9iUffisWqlVTekykB-VLzMsDMZiwg-7u8sjpi3KLzDDW9tyyGI93g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7055" target="_blank">📅 13:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7053">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7053" target="_blank">📅 12:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7051">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxCLU_BFg2MHUzeF1rZVqgAMUHXM-RmbepXzyDirZKRR6Kzz1bfNNwRuUm5RNk37p92kt9ho1ukDbjLSWeOoPRbJ4JD6wU290V3eUyPNUGwYLAL99Xg0-PST-QJzk6znYwRrheTEQe9y56kyqGHbiN7tfhUo-mPwULLZDQ1WXZWKQAeO1p4CYTGEh2WOGvpumPz20uVx9Vt84AYPazkMWnEMb6SFpWbvKrAksvAfNJMSGjSCsCV0gJ6doZvVyiKKl5YBzrCuRGyOiUZYnfH1Xg9uVSMgtksMvvBoz7vSd5nbzBaOvK0QrB21F1aeGF8GO6zXzvRnrWCVii64c2R4YA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7051" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7049">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7049" target="_blank">📅 12:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7048">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7048" target="_blank">📅 12:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7045">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRfUCdRDy4E2CPipWnE1jqdV2JG_TU7UKOllwPvZt4lPGB5Vpdm6k4jt94JpWe1HQWg1X9cn1o68nOlT50_PufJrflCKUzlTqDUSQpglWRjOazSPLLtTn5jgGCNIiRhMZ14w0TfzP3LEmT_K372ZWOQicLka9x_jQhOBXa6bDjXOkYLt_laOKphtfAc7QHUiQiDGLWmGXj1u3Q7aJtvGq0oE6ztDsAIZ0pOH8VYANP29ncjnGbxYqRv0EX2OWfe3TboaHOyE1v6CTJF8LFMAGyh4t3xeEWymACwvd7sroE8of1PIRlA2xNk1mdSU4pqNxLHC99bn1jTqD_f6r40nOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7045" target="_blank">📅 03:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7043">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">172.64.147.128 104.17.166.13 104.17.166.13 198.41.195.250 104.27.51.177  اگه پینگ نداد باید آیپی های تمیز کلودفلر رو بندازین توش</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7043" target="_blank">📅 00:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7041">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojWb5kRuclE2WbYf1-dRg-aEgjNhcTLqUAblF7diEe-Ib_bkAKJxLOV9ooQUUcB3TCUM-fBfZEt-fXHx-6sFI_HoJj7bR2jHlPZaAtrjlBtqdrDMAtMfRrYxmizv3cYZ8nwoc6F0K1M4fkSOgevavPsCqSZxwcQ5eWLLv1y0uSFQOAFj21m-A4AR1c6WLRQeVUZ_ZNG58DtVIqZ0PmFbjfQ2e1RIjGX9eFLJ7PBJN9PQrYj1I3KFzxbXOtnNHhlUETC8_x14t0LI2PMtuxENH-idu_7J0KxUI9Nb3oPAgO57r-fW1S4Gj_4e3qNjjbCc4Hi7ZJ-MWpt7G_-hA9tNTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7041" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7040">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYHIy1wx0L530PnuD8cFJ8qqHOALcBdYNuOufPMYcTsUPPQKlLnKIpOQ4BCH4UJvCXSOdGARWsa2La54hIZQP9fGBoSHWTwAW8GeDHUUsFwRb76O_ISOYXl7ElEM5g8C7DAeZkKFOLI609oNi7SmB6ziQr2JMbUsbeVgLcpRFAceAUoeLIC3uNMpQmU8L_Yl9WGFZSiR4HOM7r10rGLXzE4lkU2PmXtcPI0BoEaAvWxEYKPEZqmo8Jlk6SOcv7Q1G7-HvDKeAsb9Zqdz7CxIfJ-i4oSdJqLEkRL7jBdqtuFXSW0DorraoWpj9ZB5wv9P8wpgCYmQv2WFftdOWZu0IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">200GB   vless://1c0e84d7-34ad-4242-9b4b-ea81f973e0aa@172.67.117.177:443?path=%2Farchive-stream&security=tls&encryption=none&insecure=0&host=mail.qbo.qzz.io&fp=chrome&type=ws&allowInsecure=0&sni=mail.qbo.qzz.io#%40archivetell  تمام
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7040" target="_blank">📅 21:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7039">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">200GB
vless://1c0e84d7-34ad-4242-9b4b-ea81f973e0aa@172.67.117.177:443?path=%2Farchive-stream&security=tls&encryption=none&insecure=0&host=mail.qbo.qzz.io&fp=chrome&type=ws&allowInsecure=0&sni=mail.qbo.qzz.io#%40archivetell
تمام
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7039" target="_blank">📅 21:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7036">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrmoySon97epASL7ynetCse2BelZ2TJZruF2RAVrQdT1gRotmITJ7JridwjRQAmfPSzxOqUxWcunI0An2CYo10Zzk-niIG3169oTK5x-CxEBUg7YnxKucRg4oINpZdzi_2o_cbZ7dKyZTEeGpxt54FtnGEba5sxmSVEW5KYrEA8ZBF6QFu_NS1XQ7z5OLKUqZ6M48z-n4HR0Ba3BXo43wZlWhPVGpZrZGHIMH3XVhbqRAYDZJtn9_ySnysAOtXRBkTeX-DkBJAVzuxslV0cYrJxFoPkLKjiKN3bJ-rH3Xx4K0wH8OBZpVyuvMu-8o_zpKSd31HHdXD6hV9EsAa1XgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7036" target="_blank">📅 19:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7033">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UrZcNPvDNqJb-Tkn_bp_LlgL_G3zhdPaZNH-Z0tGKy90cBNdViP378G4dt6Gs6KkQrtxDreikJyMeFTUvvcKPjWa8NQhMg-e074DeNhNiX71keU7Nt4wsk6n2bhGl5xm510S_xfQqRBDg6-T4zsMw-IQekhb-_F-jmmLja39p6hLkvvPo8fO0tW6_U4ES1N-9TUb9lEFsTm0XoxJzbje0_DbmFHj5G5aKlNb64st5IkZoGATehaGwVio4vpOwnXEyhX7pcxqMLss8pQ9IZNenG6kw9uFdMmU-elQRE5c0M9BCSwuU2KxuwdDQRacs4FvGCv1sorGB0jk5cDasOzPPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WakPPZ9m_1qZ89iBj7sva2XSnCuDVaKnoW4F5z59TT9debTpm4SUES6khsBJ0lqx2OrGnGEgU52c7F6kiCWkHDNJEAPhHLOqrVhmE60FK0fvy67COvwsQktN5yUvNRg1llSP549iQsXLDXQiBqWVfLxi1Wd00c1z0xn-h2XZnmqoXKxtvf9u0gxwwk7GaRs5kjfZOMN0NMgHqRDn_AoGDpqH9ZqF0lEgP3HpsQpgK6zFWNYos2lZLp5MPJtjThN1MmkDJjnoWHX60Zs8D5U2XUDpYSqdmkLUU6mNNZJWA51AwK6qj8jLeExRtXkn2zyS0FN2QH1TyAkhkhC4yWfEhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_UDzFsk23gjOHXtllabmO8Si_6gyljRF2j7kAOdGrhvcLFKQ3p92bBMiMbRY8i_xbf7BRlSJAYCJX-SSsP0umvAqmZD8bhcbYDKVrjzKsjCXD2WpVzSRwbSS91v-3W6IqPLdMG332NfLFDgHGthzsb4gJa3rprqCdYDfygz2PYfdytoCXgLu6xB7prTR_1QZlzNu9eWOW_k5NLfrRtYxb-1KKGTA1HLiP-BSMmgT2d-UQ0pGrvhd6382zccOoorsBkGjITwd-Y1PgSCRmWsCfDzDlTuPMQiWSmtzChxDCRv-xhOezz5Xx__t9IQW63LpO3GHfVjUMcglk_eGDN4vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7033" target="_blank">📅 19:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7032">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🛡
معرفی فیلترشکن GRoute (جی‌روت)  کلاینت متن‌باز، سبک و رایگان (بدون تبلیغ) بر پایه Xray-core برای اندروید با پشتیبانی کامل از زبان فارسی.
✨
امکانات کلیدی:
🔸
پروتکل‌ها: سازگار با VLESS, VMess, Trojan, Shadowsocks و REALITY.
🔸
وارپ و آی‌پی تمیز: ساخت کانفیگ…</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7032" target="_blank">📅 19:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7031">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkbwxdjZBIyTjSJqjtILTTf6dyuCch2T_ssp1_0eyPnGFcSqyYh_9VHalcs5tYdF_cy17qqKK7Af0UQcDFzQa-VkkDPlLB5OD6kQRiJwvRHb-ihjaAfbQy9pc0B9yQQscVsEFTZXCPrA0e5OoLuh1KJcArB_d3nog5hwVWW8WWoiF_tNsc1DbAC-Dvjd0QvWIjMo5r0HYfENurZjo6epVIslp05L1_tiEc-Qa2DCluZ_iYpUFYYFMczTPt-YINbNCx_1VO9fZFk-99XynP8CGX2GLUaSM5-OHLK2-PhaNnUMs7XE-UKR58E6SUnRM8IWXyL88_O5v887wxM3WLy1IA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7031" target="_blank">📅 19:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7028">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rlp8k5GHFbXFDRUwk8p2KGSMWjLrKHc9wReExs1RjndiBge5znAWmt-JyN4xj396bSzkQ4C7bbabXXJA8vYHNXlQk9auQOtLBixZTxuY0RjLk575gimWSClCo0mZkSOzOcWzROd1qod3OFRSQoEVGuc0xVY4l8VWEyv8vB4_tJaNrd8FDryPdWPvEaZma4WNPArjpSX_5Qvg6StCKBkfh9JOWHk5yt0corCWSBwo44QT226OJwyun2WM1aN45lLVNw1VmeelMRmrCfLD1BwJU2Cb43K696jKX3-MFeY41izTNUCFIysBUl0FvO4hHa75PnAF4yXxyehFCKtpzwIphw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KEMtCEdti6KDmOnpoRLRZC2bVVJRCd_LWATilsEvQQJ5fqSNAHyfJYLZmtFZPX-l8p3twoXOILvdZZL2uawWSZ0r5bRTEPFNJmUBsFxPL1K3zqyxMrGvhQNciPqZZJlntn45PLqUL6qqr5LgLd4uFZnk_9XnT2eDhBb_WkeZ_jMYF42tCHWJvJsd2HFzVrRTO4l6qHIojk2ZtYAsc8lmF0Vymf8ZtQPczm5M9oSWkQbEGVXoGn2FAEfa6p_nJYQ4jH-8akrgiFZz2kpiQDDozYF-9RtVDG8i8BNBdh87hkuvtzVePl2VV8OHG6OYSrWhlNFPTEXqD3BsIcZaDnx9sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P_E-Zrz8yOUs8_mqYJfFTDHGuTdljDU4DVxa9Rlk2UJy7UCtXvJg6pMAZpP1Y0dVtTITpc6jAFXC29WHc7ImPlm_fo5KWJBZrHrGZFm4Khii__U5fiQl4tvoZBHB0NEP7fpBTn8qMrP0ITvxD2OvJDJ9Of3l9gHGzb9W82cK4dVVLwH2oq9kP847YgH8Vc5fDaiGinf754l2CIiDGjaJzMPo-WqKlOd9CCoA2O-XsUw7tDFwvkrQQwkFAkocpKqG3Kimz_uPrRJzY1jEiGKPekrXz70C_ByEkHRzpvO8qDmzjqq-LtzrllMl2rLIzxyOcu0g1yvAcj4ML2fjb-CHYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
مجموعه‌ای از پرامپت‌های متنی، تصویری و ویدیویی رایگان و قابل کپی برای مدل‌های هوش مصنوعی مانند ChatGPT، Claude، Gemini، Nano Banana و Veo که امکان فیلتر کردن بر اساس نوع، مدل، دسته‌بندی و امتیاز وجود داره.
🌐
https://freeprompts.io/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7028" target="_blank">📅 17:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7027">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9lVcj7KcudTcnMf6y4kB7nG7hAvkfBJt85YFpICeu5j7438cGxTJ9i_FgKQ7YjE4kh0bGxtrSMz7vkb7HRKte1dp6rb01hsi3xM4m_ZKtH95LjHNdWdzsyOVkimCfh1JT9EvHEkC1qcNO6TcMdpYWpyV3KJmhR3pME0WYoniQlgFR9gbP-OAAETumG2Kwsd3dNU4wUpt6ZK2D0Bk3m0EOLe3xiBEQFyGtFrbggDMnvGEyeb3wCQuNdy6AZwYTixnrcgS2WxF2DZ9sNx__gKywn-pLJhArIRfQNgJZDzI022n5WJztShXk8pmpigmqu5s-IMerG1rQM-uaNrgrN2fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7027" target="_blank">📅 16:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7026">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXdwNPuABRqDro4kW4u7qpS4XrUjIU7gdJB823OUSfLdj_imuL67Liws5-iK3dM03Kt4QXohn5SZEDmmzm_6U3Ys6Dmbj8eZ2vsigZynRSl2ukrGnZls7vJCukIVUzE2tNRheR1NDA0NzDip0O-nhZ5PLeug1JuOdRxiDBEQpkqYYZ9gjz4WQLKL0esMkaBwmJ5azjNWZQLTk_UJ6HrA8MC6EEk451niXgWHKYH7xAdmAASp8VCTmpZG64AyF4YbHkQP6W6cxqah5bksPKXeXqvJ_eP9rnk_8F6HGj77SqzyB6WeOafr6_ttKKH4ZU-5DcmVzncIozMwn1ADN5fbSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7026" target="_blank">📅 15:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7025">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/7025" target="_blank">📅 15:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7024">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dN95Umj33uNNsFiKDc7Kw8oF4qHFCxWYzVGMfjwtCpBTgim-nNCUwFHjVn810J1UhIbiyrWks-IS_XRpjxGHS9SgeoYBkLM1NBdRv5j2A6jj52-LaPVRpREs_JOCe1UASnKp03_w9mdHG6TFljcFRyHy04vB-e0FqM8vIaq3TOsV51w1--bTt8wcOTzLrWXMnj5YJMIeqQVHKYVjbCR47weuf-XVe_VGAjLlkemrRY_3fbTvSW63c3dXhp4JqSz5M3lSx6Xy9LAoTBUMCS9zT_Te6IijGzfaQ0eIsifvCw3VIxXbJq4RuZxiUl7sCwxbXAAx_xXU3tiexh24TfHMyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
؛OpenAI قابلیت جستجو در ChatGPT رو اضافه کرد که به طور همزمان در چت‌ها، پروژه‌ها، تصاویر و اسناد جستجو میکنه.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7024" target="_blank">📅 14:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7023">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">📱
معرفی Hermex؛ کنترل کامل هوش مصنوعی اختصاصی از روی آیفون  اگر با پروژه متن‌باز hermes-webui یک دستیار هوشمند اختصاصی روی سرور خودتون راه‌اندازی کردید، حالا می‌تونید با اپلیکیشن بومی Hermex، کنترل کامل اون رو روی گوشی آیفون خودتون در دست بگیرید. این برنامه…</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7023" target="_blank">📅 13:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7022">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7022" target="_blank">📅 13:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7021">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_H_47rJbBh6aw1JwirfUqB6rDTetWljYoB5ZheLUjDe60Vngx7sefBwdMDNVZalgtCQsOUAWdTuNshsa_KpFCEkZeMzKKH1bqbMF_Ig7hnd06kb4K_DJbVlak9vjfns9hJakNOuvJWE8Al0RWkUknrfHOciuqfNfw32htb-ofe1lbcQ8DTj6RNA3buZ-zVm-O5NUFp-8P9CPR9lVTXlu4EwitTlhJ8fHfso2Krf9FCZhatpRvSGqslRFMmgzKV5xMVm8IlgpypSm2mfzlAwEyFRipL3_8J1KN__uEAM1vfLWk0wKGsjGi6LtP5RVsbYq1rc5pd_4N9bDuoVLB7FKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7021" target="_blank">📅 13:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7019">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_SQln1KPxdAshmEHniiDq5jYUiMG48Mjs0rqqkWfY2CzaHyTH55Nh7Qj51steZWnDFqebrBK_zbX7NDVTtCKWaemajLZNpWr95Xpz9pIXT7qmH8R9xUUJn9DkIHMOf1Sfn1cxwUeVboZhxrFYUwLONuZephuud_8YOMgROdxeeKdiEnlTsUVU0CV5D9tWJntuLX0_DFduwFkzxdBuClJtiC0iT-cx-4Kns7cOyiXxs6ZZEUoEgnlA-NIKaWS6Li68up8diRNvaVpIbgh5j81Pfl1coiRhZUSR_mxZDyxosPhmQymNtuOXluXgvNqgv0DHjpWo7Gp-1bbReMG54GDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7019" target="_blank">📅 12:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7018">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUugp7jpHpjnzHHgbLrWPSD5hOPooDgkcAU-_BRE5wzKfxLetpSzkMAnGw5eOQMnLxhxjc5oyNdTi_awjDGX7fDhvw5QdAem6G8jspFvhVeAx276hJTZ_hTo_ftUGKGeWIUhjVJTMoQo2XzKrwVzf2RgZaAt0cRPvc0-mo9AZlgQ3WPO2eK2lqWH4-RH6mqELmmacsR34ByAFQ8fHM4_GlaN7JKVhQCbsxPatiReza8daG3vyVlFQbaAap_Q0kITP5viC68_4vf42WJz5CarmJF6as9bWllrk45X5kS5M8Yc2pYwKYq_Sysaj1izBFe8QvMgijt5FHER1C4ppI77TQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7018" target="_blank">📅 11:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7017">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0B6jHXefvFOAfL20p9z_wQhqyvh7wv9Nizz7aXKLkDErdQXXfuuGrYmSS0HScAAKJFxe_jhJLkVRwTaXeFxd30YmikAzN7VtJ_Q0KjuLoKBXWYhGCvNLgYa8VBnnirafPp2QK0T8JwjZi-B6A9IDZdznadasnOkQ3u-NUXtbtBxdzXuwHBt30lt6xNOWeYmVAmBYw_c9XPVmmr79D6htGWHC3bKE6jcjfzeGS9_aFjbC2VNxBPpz2ee53Nm9DocjRxFnAKSssom2fxHHldEGs0_RzRcT8dGdrpuSxYds7U-Y86ESGEK4ab7jnpPPD1eMwxkTLIhSPGoXvvxfDfpxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7017" target="_blank">📅 11:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7016">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgqRQFDwb5PbY9ZtKm7gi-KmS1awAprnreXof-D4p1NMgf_Lvx1rAVZVq7fzbxAKgxMUbznOJx4zbHQmlxa2x6-x-t0MWU4otKLCfHVDj5xuUfjKgoiL1mWAKn_b9qeBcvHulYEBxCYAD-OjhkxZes9iBFfpzYY6COdGuXeuGbqa6-DrMM0rQrwCV6MYakxIWt5-4QP3cNj-ymJlHxfM99sg8rGpn1CIMs-QMLISJYjdOs6DuO5R2iQ5_BzCF5ccPq-eNJcomJb-J9eJAJEoL-jPtJdzCDqz9pVfFpimswDaYla0DBG8A11zsAYnynQJtXuVD4bKOF_2MLiKoG4HUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7016" target="_blank">📅 10:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7015">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFp8f2iohUDv2irgnsbGNj1B8VW_vyK2i_km6yWLk1ztHFb-9AvdsCUqCWJZFoGGjicjON6kbkEEwhOxHvM7xgqW32kWYArGZT-5OHlmqoazirrJjZgBgFIDQ3kqY8YJTv1slG6nusdPBCkeNuMrLKutXwE2nsqVnqUwuLL8d19i2VjdkLpfZQWWfMvv3tEdmwi16WovQ8dVlW8t8N1P7J4sYEo_Frg5Uik0EERT-i2yIjnnBbwvYV0h7htI_J7I4UyIcZ_cYoYnnj3b9z83GJnqtr69S_q4EoZs03radVrJr3bvrp-Kz4WlqyxTt7TvkU3HrqQwwZiCc1NEy7J-LA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7015" target="_blank">📅 09:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7013">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6514ad748.mp4?token=WXEAcZAMVYksIqOsiL7bYQpZY2xiHGWscH62iMeL4_ma6sE7-kIbX6Ek5nVU0odatc2dLDq_Ojzx8QGn3yYCD8kJyCmZv16Xx1GQEo1YmCzOm-kbGV3-7IavGfL7tcSwOY6FXAhieUl1yJA49qxGsncuSEU8om_Okv3AXBI5CCGTaJA7LwaZ7cLv6XoN3Xt13SeQta430aROyrOtyQaXtAzhVAix4mDPM_tEUjbif93u7ojWEI0ghmxcG4sGmRLLNhTmLS4tRHII5qYVqRnOY5lHQ2RjFhfZt5-SLrVyc6xWfCfXCYk-CKoB2DSEOzPLJf35ujaybZHEQgq4MMHmfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6514ad748.mp4?token=WXEAcZAMVYksIqOsiL7bYQpZY2xiHGWscH62iMeL4_ma6sE7-kIbX6Ek5nVU0odatc2dLDq_Ojzx8QGn3yYCD8kJyCmZv16Xx1GQEo1YmCzOm-kbGV3-7IavGfL7tcSwOY6FXAhieUl1yJA49qxGsncuSEU8om_Okv3AXBI5CCGTaJA7LwaZ7cLv6XoN3Xt13SeQta430aROyrOtyQaXtAzhVAix4mDPM_tEUjbif93u7ojWEI0ghmxcG4sGmRLLNhTmLS4tRHII5qYVqRnOY5lHQ2RjFhfZt5-SLrVyc6xWfCfXCYk-CKoB2DSEOzPLJf35ujaybZHEQgq4MMHmfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7013" target="_blank">📅 08:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7012">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDQkUhLaq1dApi0WzLf1K6MFI01Gk1TRmhWJoeROg5auXRbYGKlqosIAFql5XqDWpNVX3sNJWR1FSYD67_qvHnLy70YyGDVwEKiCHIOSvGb56cAZsLI8eSQo2jlmOQWfp627_cDPNUVkkv0AY1pe12RTT8GaHvAU-FBPVkSxf4OpNg3Q4fzpll_aNTxkBo7LJMUZyHNl5ed_PcdYp_eCBCOL1P-quFf8iAhAT0d16GLhF-xBzdChwri-40EZrYFA_P_X8_qX80e30I45BO1dJbjyElGLUBdsHLJJWcHBeh1gpWTnCVyQUnn5-y5V1pkOa54jKvPbXfbFgvQPatG5PA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7012" target="_blank">📅 02:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7011">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ucx1ixxWNTh8km06faWBPbNme5P-5LIeuMpbOCQwtDF4fiSftlL4yc6MZWULarEdv0poiwSmPAZsZHpE-rix3VK1rdUi7mmlZBLWxZBM9InBHA4DhJFsvIlqpXeIq845F7o8RrVhMVMSywetFDV17C6D_vGx4dvFJ_pZwItg16G8nMdf9TTMdoyVIImQFxOZXbUHuAIPBKFHqaAHG5KY3jCKTYcQRpGvO0QiKwi7oX0R_62YEN8fcx379XITTn23hFxZNxo6nPqOfwUw2aryuQ1KJWGHq-a74t3nsCA0OUnVhK3Ma22_7W8EWGjtZvI0aSl5SUlQwPTZQh2tw9v1Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار از زندان DeepSeek
👇
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7011" target="_blank">📅 01:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7010">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🛡
آموزش ساخت کانفیگ Bepass (متد یوسف قبادی) روی Nekobox  این روش کاملاً با پنل‌هایی مثل نهان یا BPB متفاوت است و با استفاده از Worker کلودفلر و پلاگین اختصاصی Bepass روی نکوباکس کار می‌کند تا نتیجه متفاوتی برای دور زدن فیلترینگ به شما بدهد.
🛠
مراحل راه‌اندازی…</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7010" target="_blank">📅 01:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7009">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🖥
نسخه گرافیکی ویندوز فیلترشکن Aether منتشر شد (آپدیت v0.3.0)  اگه یادتون باشه قبلاً ابزار خفن Aether رو معرفی کردیم که بدون نیاز به خرید سرور، فیلترینگ رو دور می‌زد اما محیطش متنی (ترمینالی) بود. حالا ابزار Aether-GUI اومده تا همون قدرت رو با یک رابط کاربری…</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7009" target="_blank">📅 01:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7008">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7008" target="_blank">📅 01:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7007">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuBwZMmiPsdcyN7RP4dwfurucMrIZGWVbjyDgCjlCFnU8Psy5wbZIFP98MkJv2G351GX9PlXZwCgcXOKhP9hSRZLaMHR0C3Krr63xJ5G7JS_v-Mo80kecolobpmi1YIPGgx-sEieLR835EU9pxM2szMSkOr5OVDoUAYqcekQ-PPEsGQnJulFOEjeRlRZOdf60Ds2UY6wQDGDKJKTwQgFbYH9iD-whGMfFGJAECK-wWBev77hR6JW2Ve_yTZRFifTv2mMxqMxnx1TEPduZ-xCSMrvPvsLi4m5gDdrgzBkEVqE7ifUo6awg6IskOijTkzM7CMEXq0ZDCu3ditEPU98pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید و خفن Aether (نسخه 1.1.1) منتشر شد!  تو این نسخه کلی از باگ‌ها برطرف شده و امکانات جدیدی اضافه شده که اتصال رو خیلی پایدارتر و راحت‌تر می‌کنه.
✨
تغییرات مهم این آپدیت در یک نگاه:
🔸
خداحافظی با اتصال فیک: مشکل وصل شدن ظاهری برطرف شد. پروکسی SOCKS5…</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7007" target="_blank">📅 01:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7006">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🌐
پروژه Aether: ابزار ضدسانسور بدون نیاز به سرور و دامنه  پروژه متن‌باز Aether یک کلاینت شبکه‌سازی برای عبور از فیلترینگ‌های شدید (مبتنی بر DPI) است. ویژگی کلیدی این ابزار، یافتن خودکار مسیرهای ارتباطی است که شما را از خرید و پیکربندی سرور مجازی (VPS) بی‌نیاز…</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7006" target="_blank">📅 23:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7004">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🛡
آموزش ساخت کانفیگ Bepass (متد یوسف قبادی) روی Nekobox
این روش کاملاً با پنل‌هایی مثل نهان یا BPB متفاوت است و با استفاده از Worker کلودفلر و پلاگین اختصاصی Bepass روی نکوباکس کار می‌کند تا نتیجه متفاوتی برای دور زدن فیلترینگ به شما بدهد.
🛠
مراحل راه‌اندازی در چند قدم ساده:
🔸
۱. نصب پلاگین: ابتدا پلاگین Bepass را دانلود کرده و داخل برنامه Nekobox (نسخه ۱.۳.۴ به بالا) فعال کنید.
🔸
۲. ساخت ورکر: فایل Worker را دانلود کرده و یک ورکر جدید در Cloudflare بسازید و کدها را داخلش آپلود کنید.
🔸
۳. تنظیم آدرس: به انتهای لینک ورکری که ساختید، عبارت /dns-query را اضافه کنید.
(مثال: https://name.workers.dev/dns-query)
🔸
۴. ساخت کانفیگ نهایی: لینک به‌دست‌آمده را داخل «فایل خام» که در این لینک (Rentry) قرار دارد، جایگذاری کنید.
🎁
راهکار سریع‌تر (کانفیگ آماده):
اگر زمان یا حوصله ساخت کانفیگ را ندارید، می‌توانید مستقیماً از کانفیگ‌های آماده‌ای که در همان لینک Rentry
قرار داده شده استفاده کنید (فقط فراموش نکنید که حتماً باید پلاگین را روی نکوباکس نصب داشته باشید).
با تشکر از یوسف قبادی عزیز
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7004" target="_blank">📅 23:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7002">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEhonuW59iQddb0ecJLEV66EwlH7uCD1f4kB9oAOk3n_1i8JlXc3aqDsf1M07Cu_P6kU55AMLL6FWmkms7GBqAvJO-Doh44BMGjXAIqhAu90H3SX9M89j_cWFl4Ogn0-VllQQxnmAC2TYrfFVwsZE7KER5EeVug3O62UQ1HeIgQaF5rCXJZ_xFrXf4zKsN-hl815M8hVwA14Bju4_BXQysQBfDpNcG_fb2FdeQs1MqW5GbHeQYjWN4xx-eakQQBG5LzgcgYjTQ0QS3fY6GlblxX0sFlbCiCLxxpBHyWcdW1RQWs3RCZcgF-iKDWhMv-kKoZDu_5ZRQvqLSlKP-D3eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
معرفی Consensus؛ موتور جستجوی هوش مصنوعی برای تحقیقات علمی!
اگر دانشجو، پژوهشگر یا حتی یک فرد کنجکاو هستید، Consensus یک موتور جستجوی مبتنی بر هوش مصنوعی است که پاسخ سوالات شما را مستقیماً از دل مقالات و منابع معتبر علمی پیدا می‌کند.
✨
ویژگی‌های این ابزار در یک نگاه:
🔸
دسترسی به پایگاه داده عظیم:
جستجوی هوشمند در بین بیش از ۲۰۰ میلیون مقاله و سند علمی معتبر.
🔸
پاسخ‌های مستند و واقعی:
ارائه جواب‌های کاملاً مبتنی بر فکت و شواهد علمی (به دور از اطلاعات زرد و نامعتبر اینترنتی).
🔸
استخراج هوشمندانه:
پیدا کردن مرتبط‌ترین تحقیقات و استخراج نکات کلیدی آن‌ها در چند ثانیه.
🔸
کاربرد همه‌جانبه:
یک دستیار عالی برای نوشتن پایان‌نامه، مقاله‌نویسی، یافتن جدیدترین دستاوردهای پزشکی و تحقیقات شخصی.
🔗
آدرس سایت:
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7002" target="_blank">📅 23:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7000">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3hjEoWnZoA66lQybOE1TmULFW08DZN5_CrgfhgKkAgUxN0NfY9BNteJRcWXPZqiWy9jUNc-qR04CNSI2dBnr_KK8mzY8N6UfK8xksyMokUzdqM8HxyN6wiAzDDxXVyXr3tuczZ30r2lrzt8u-FbxdvwCj9rHykHLNWGai6YGr6vshE-PRamh7KKak4mSJzp0VI6rw8h6YiTmiDOb0mT8woOzkCs5iI42wKPhGrEUomeaYdLyclQBleZHFzncSEUZvKxFbnCUaozxfE5M06_1E57E2XBZNcXQ-YRVGJlajXDm0Yg_y22dRvAMPE26_yxjcQL4xPrs2mdID9368-aQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📦
Universal Installer؛ همه‌کاره‌ترین نصاب برنامه‌های اندروید!
اگر زیاد برنامه‌ها را خارج از گوگل‌پلی دانلود می‌کنید یا با فایل‌های چندتکه سروکار دارید، این ابزار متن‌باز جایگزین بی‌نظیری برای نصاب پیش‌فرض گوشی شماست.
✨
ویژگی‌های اصلی در یک نگاه:
🔸
نصب هر نوع فرمتی:
پشتیبانی کامل از APK, APKS, XAPK (همراه با OBB) و APKM.
🔸
نصب خاموش و گروهی:
نصب و حذف بدون نیاز به تایید مکرر (نیازمند Root یا Shizuku).
🔸
جعل هویت (Spoofing):
گول زدن سیستم برای اینکه فکر کند برنامه از گوگل‌پلی نصب شده است.
🔸
شخصی‌سازی نصب:
امکان داون‌گرید کردن نسخه‌ها و دور زدن محدودیت‌های SDK.
🔸
سد امنیتی:
اسکن خودکار فایل‌های نصبی توسط VirusTotal.
🔸
انتقال محلی (LAN Sync):
اشتراک‌گذاری و نصب راحت فایل‌ها بین دستگاه‌ها از طریق Wi-Fi.
🔸
طراحی و پشتیبانی:
رابط کاربری مدرن (Material 3)، بدون تبلیغات + نسخه مخصوص Android TV.
📥
سایت رسمی جهت دانلود (گیت‌هاب، گوگل‌پلی و F-Droid)
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7000" target="_blank">📅 20:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6997">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/idPnLJtej_3v5Nk9-m08pJDld51O0f6LTaPFLMeawPwsXyEktKjp7iMLqVDItT5WcH_uYyp-wpBRYkdLEy8AJPuYxBGaG2d0zKxbo-Rhxif-XpwTx2i44zF2ARJj_cxn8IeHxhnWepT1zx3s2_IkhwLTCisthMhIcNw03dzquUBZpd75wOcLnBX3oGUYVGgNKSPotVw2Or1qFQ4zgxHPah3BPpdFMuiE5v-WUKmQNNQoz-QE99tQjTlCENYvEeJBMXhFzYEXSIXXcUq-RuzMRjgwEhHa8DMicqlhSnzuRbVNBm5_0-_KaS1szDGqglQAP9IS2T_jbRvDrNo8nXewHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LkNWXNxe5GjMb63f4xOxA1XTnqMr62Biq6yGbMOXkx6gQtd0fXwIy0kFX-WFLqZboW0latThW68TCUVQ4eusg987m817Uvlx0c7XGlNSbugRBqK0xXzRIuQ3trTXuhkawttkko5d4H9dlySYgKfq796cR1QFI4TsIo2k2N2StrXDmiKAQJxIug-bOCH5QELjHKJ99qrjFu5JEf4-7-BKzysZzxgQJClse4NovfGIjQaKWKd5lXPlGDpRdVjWxYsaAngoip2ELOl0Rv4JkTBIJ07zF7qZbOgrf9o4O_g41pGi5SVRPV7jvZK9qwx90DQtvks4zigCjST9UOiRW-tysg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
گوگل برای ۲۵ سالگی Google Images سورپرایزهای بزرگی
معرفی
کرد.
🔹
تولید تصویر با مدل Nano Banana 2 Lite داخل Google Images
🔹
طراحی جدید و مدرن صفحه اصلی
🔹
گالری شخصی‌سازی‌شده شبیه Pinterest که با توجه به سلیقه کاربر تغییر می‌کند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6997" target="_blank">📅 18:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6996">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbvu4cs2oO-nD4FjGL2z5zV2Wx9Vxg2rqV42kDAFV5Ec72Z07YNe2W2u7xxHyRvGh1AM-bi8X0V-u2s5oNtRTk8iSjHkce5lmP-TQ-wQwESrn00s7wxd_f1hIcWsHYFe7gOZC6HEmm_Mzn17vi0eZ_zhx87FlZvW6LhyzgJATsYuX7i1o-3HfKEnMsG9q80DFRj5MtaQCHHnkTuPLTRVhdEUjCc1p52HRHw__uld594kgS-1UqIqUypUQWf3onhK--5Cietdg8jtKrpYkDhPxt8sog1OH1GzaFlbYAmmdNa8r1MThTde79rOeqBUVtx83pttrj1NwMEJ7OlmBvlG0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثه آب خوردن  کلا ۱۰ ثانیه هم طول نکشید
😐
ولی وصل نشد رو ایرانسل برام
😐
😂
😂</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6996" target="_blank">📅 17:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6995">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2lE_fZlnXpHbpdO3UG1-i0dzIy1RORDkwjARui91P77ac0DpTtuBKCmR0YcBmPowdbshJwWw6xKM_Gme116PVxvvQETO6iVclwMihk6Swbx43x3cdD8IUIrDL1PT2X80j6rnShH5COxepTv3cjXCcAMBjTWm9DqEum4PJhMhaDFi6N9z4uC4xSlMkTs_vmrwaQmGY9JdfYS9gz4-BcXxCsPAA8unxsIO8ChDxAwhlvxshVvJG_IKiiKlNDIs8R2NH-xeTSZ0mqXR-wJ2IDfvLPM1BhtCpWFyP6DGftVNjMCqrvqM7tI68kyh3ywzdLVMNJw4QdL2vW0mRpXG_PzSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
پروژه Aether: ابزار ضدسانسور بدون نیاز به سرور و دامنه  پروژه متن‌باز Aether یک کلاینت شبکه‌سازی برای عبور از فیلترینگ‌های شدید (مبتنی بر DPI) است. ویژگی کلیدی این ابزار، یافتن خودکار مسیرهای ارتباطی است که شما را از خرید و پیکربندی سرور مجازی (VPS) بی‌نیاز…</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6995" target="_blank">📅 17:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6994">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🌐
پروژه Aether: ابزار ضدسانسور بدون نیاز به سرور و دامنه
پروژه متن‌باز Aether یک کلاینت شبکه‌سازی برای عبور از فیلترینگ‌های شدید (مبتنی بر DPI) است. ویژگی کلیدی این ابزار، یافتن خودکار مسیرهای ارتباطی است که شما را از خرید و پیکربندی سرور مجازی (VPS) بی‌نیاز می‌کند.
✨
ویژگی‌های کلیدی:
🔸
بدون نیاز به سرور شخصی:
سیستم به صورت خودکار سرورها و مسیرهای سالم (Endpoints) را پیدا کرده و متصل می‌شود.
🔸
پنهان‌سازی ترافیک (MASQUE):
ترافیک شما در بستر HTTP/3 و HTTP/2 کپسوله می‌شود تا کاملاً شبیه به وب‌گردی عادی (HTTPS) به نظر برسد و مسدود نشود.
🔸
امنیت مضاعف (gool):
علاوه بر پروتکل WireGuard، از حالت وایرگارد تودرتو (Nested) برای ایجاد یک لایه رمزنگاری اضافه پشتیبانی می‌کند.
🔸
کراس‌پلتفرم:
دارای نسخه‌های آماده برای ویندوز، مک، لینوکس و اندروید.
📱
نصب سریع در اندروید (از طریق Termux):
برای نصب خودکار، کد زیر را در محیط Termux کپی و اجرا کنید:
curl -fsSL https://raw.githubusercontent.com/CluvexStudio/aether/main/aether.sh -o aether.sh && chmod +x aether.sh && ./aether.sh install
پس از اتمام نصب، کلمه
aether
را تایپ کنید تا برنامه اجرا شود.
ابزار پس از اتصال، یک پروکسی SOCKS5 (به عنوان مثال روی لوکال‌هاست و پورت
1819
) در اختیار شما قرار می‌دهد که می‌توانید آن را در تلگرام، V2ray، Nekobox یا تنظیمات سیستم وارد کنید.
📥
لینک گیت‌هاب (جهت دانلود نسخه ویندوز، لینوکس و مک)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6994" target="_blank">📅 17:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6992">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3g5Yt7u7-dCC5S8m3B1rv-qTlPKKiVtpXf4KRZTci1A14N3KxFt6yivqUjghyqQfw-jaLiVvw9P9ljiB1KEi8KOuSaevyzMm28ptoauQrV47uj403XJMv8zwxGkOZU1dGzTUC3mrha4b3fZAk2YUK3jfLTTuzjrTDf29biHMegR6YWvO7dkGtkEIxy1JIHe4kf3mkG-0Js2ydmyWCf_PcTK8NuNtaaCkFWV6jqylXHGsLU4aQEHu94oU0hycajKFfrzdkFIDU8T9U4wVeqHk3SQrh6_t_6et55lGLLYhZSRY08CcIyRL1L0V-GUlz30bWopNvkvqZxSaiFbOUIhxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☁️
اشتراک یک‌ساله و رایگان MultCloud (ارزش ۴۰ دلار)  مولت‌کلود (MultCloud) ابزاری بی‌نظیر برای مدیریت یکپارچه تمام فضاهای ابری (گوگل درایو، وان‌درایو، تلگرام، دراپ‌باکس و ۳۰ سرویس دیگر) در یک پنل است. با این ابزار می‌توانید فایل‌ها را بدون نیاز به دانلود و…</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/6992" target="_blank">📅 16:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6991">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsdkIsaGj1FQItS-2PM1-B8Y6InikLLIBHX267nPDj2Yxod_7YffRMiTns34yq-dCbBNAbYZ2JKt1ErcsbKTA2CpLcaQ9YD37BAZr_GkRnKIFXphP2pu0lRwVfDXwbvqsqYWpgztrcDHgteEpqJM1gIwlIih66giszHjxS8Snjp7J9eFUMNYtZn-QB3w4OxBpTBPNKohNjVDeUmwaXtTdLGiB-LyMwdNhDj9m6rhOrkO-0OtHI5_NDr3yKcH4A8Ed6qXvUWd-9kJ0YI1RDT_A6UfWNqRixE9M1IcEomo-gLdlCdu_cLrWJ_xBsikWMo_JM9gKKG8P0MAZtrZ_FDvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☁️
اشتراک یک‌ساله و رایگان MultCloud (ارزش ۴۰ دلار)
مولت‌کلود (MultCloud) ابزاری بی‌نظیر برای مدیریت یکپارچه تمام فضاهای ابری (گوگل درایو، وان‌درایو، تلگرام، دراپ‌باکس و ۳۰ سرویس دیگر) در یک پنل است. با این ابزار می‌توانید فایل‌ها را
بدون نیاز به دانلود و مصرف حجم اینترنت
، مستقیماً بین فضاهای ابری مختلف منتقل، سینک یا بکاپ‌گیری کنید!
🎁
نحوه دریافت اکانت پرمیوم ۱ ساله:
🔸
وارد لینک زیر شوید و یک حساب جدید بسازید.
🔸
در پنل کاربری، از منوی بالا روی آیکون کلید (
🔑
) کلیک کنید.
🔸
کد پروموی زیر را برای فعال‌سازی وارد کنید:
BAAYK667N5K3K0N6
🔗
ورود به سایت
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6991" target="_blank">📅 16:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6990">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5760952ca.mp4?token=hHcbzB5pPryQGSBLruv3pzHAq_9VWqM-3E5Z_MUPvNS3FatwsyJq9fh25qOUMMUQvwht9s5KqpWZKT4jkyldW6_zOcFvpeDiV3MxQ2z5ZN1qnj8L5VuFpvJj5ogvtlv_KnVjNe4BPNSen8xqQbw1QgZ3JXyrpxq5-pXKuMb-qK_gqIS7J4zzuTwBTSSaE-9KYil9Xs-4kQFoEukXB9BW1jZk8o1zoG6OEZY9OGyEL8p6oweYYqxIQkWdKESRHd7_bWzvEja_AVQRsFtkjogbYjrqdXCH0k4jGI1owKOaEepkM1x1peRjWarKAAiigFy9SFd4QlrvxAMxxc6J6bct5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5760952ca.mp4?token=hHcbzB5pPryQGSBLruv3pzHAq_9VWqM-3E5Z_MUPvNS3FatwsyJq9fh25qOUMMUQvwht9s5KqpWZKT4jkyldW6_zOcFvpeDiV3MxQ2z5ZN1qnj8L5VuFpvJj5ogvtlv_KnVjNe4BPNSen8xqQbw1QgZ3JXyrpxq5-pXKuMb-qK_gqIS7J4zzuTwBTSSaE-9KYil9Xs-4kQFoEukXB9BW1jZk8o1zoG6OEZY9OGyEL8p6oweYYqxIQkWdKESRHd7_bWzvEja_AVQRsFtkjogbYjrqdXCH0k4jGI1owKOaEepkM1x1peRjWarKAAiigFy9SFd4QlrvxAMxxc6J6bct5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
نتفلیکس شخصیت رو تو چند دقیقه بساز!
با Reiverr همه فیلم‌ها و سریال‌هات رو یکجا و مرتب داشته باش:
✨
امکانات:
🔸
جست‌وجوی هوشمند با پوستر، تریلر، امتیاز و توضیحات
🔸
ادامه تماشا از همون ‌جایی که متوقف شدی
🔸
پیشنهادهای شخصی برای وقتی نمیدونی چی ببینی
🔸
رابط کاربری مناسب برای تلویزیون
🔸
اتصال به تورنت‌ها و سایر منابع دانلود
🔸
نصب روی کامپیوتر یا سرور شخصی تنها با یک دستور
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6990" target="_blank">📅 12:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6988">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👱‍♂️
پروژه Ponytail
برنامه‌نویس ارشد تنبل برای هوش مصنوعی شما!
✨
ویژگی‌ها:
🔹
جلوگیری از پیچیده‌نویسی (Over-engineering) توسط هوش مصنوعی
🔹
کاهش حجم کدها تا ۹۴٪ و صرفه‌جویی ۲۰٪ در هزینه‌ها
🔹
افزایش ۲۷٪ سرعت انجام وظایف، همراه با حفظ امنیت کد
🔹
اولویت دادن به کدهای موجود و کتابخانه‌های بومی، به‌جای تولید کدهای اضافی
🔹
سازگار با بیش از ۲۰ دستیار هوش مصنوعی، از جمله Cursor، Copilot و Claude Code
📥
گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6988" target="_blank">📅 12:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6986">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏
🤖
پروژه Hermes Agent (نسخه اندروید)
🔥
پیشرفته‌ترین ایجنت هوش مصنوعی خودآموز (Self-improving)!
✨
امکانات:
🔸
پشتیبانی از انواع مدل‌ها (OpenAI، OpenRouter و مدل‌های Local)
🔸
اتصال مستقیم و مدیریت از طریق تلگرام، دیسکورد، واتس‌اپ و اسلک
🔸
حافظه بلندمدت، یادگیری…</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6986" target="_blank">📅 10:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6985">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O36P8hz8DJbj8UR1NwbBSVBNbBqlwi2csqZbixYoIoSrZl4SymaK3djA9_RHKMY44IfDCWrAD81_UoXGaE7i8RPZ-OvRX9Wbsm2j7SKvm3qR8TYadytZ3A0_aWTU3EVk6uvP6rzNmxHJcuwo0OYC_R624lq9H2W7TuLK7I0e0Q7M0IypNok3zPxJRpoDA5Ux7PdtOzwwwh8ndRYYFoKiT1h_kctdCHV87c8lun3HgoDCeF6FQSzvJiTj1s-pmzVuvyIiDSjov_9k5qQ2r70mF97rSCaUIbU5JLWM42JLunISQ5oqYjVzqnH4pKCt51sQqixnpuxw3pZ3uH6MfgJBLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤖
پروژه Hermes Agent
(نسخه اندروید)
🔥
پیشرفته‌ترین ایجنت هوش مصنوعی خودآموز (Self-improving)!
✨
امکانات:
🔸
پشتیبانی از انواع مدل‌ها (OpenAI، OpenRouter و مدل‌های Local)
🔸
اتصال مستقیم و مدیریت از طریق تلگرام، دیسکورد، واتس‌اپ و اسلک
🔸
حافظه بلندمدت، یادگیری خودکار و ساخت مهارت‌های جدید
🔸
اتوماسیون و زمان‌بندی وظایف (Cron) فقط با زبان طبیعی
🔸
دارای اپلیکیشن بومی اندروید برای اجرای مدل‌های آفلاین (Gemma و Qwen)
📥
دسترسی و نصب:
GitHub
,
F-Droid
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6985" target="_blank">📅 10:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6984">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Db8qzmEoRfYIjPr5aduauGdms_SQrPm-8LEG55DHl43-E2pdP8ALIQzVzE0MKdBNV2AGeksxCC--aQv75PsQdfq8kxUcqujstMRPB-oT7_Eiph4VlXQ7lp0gHqa2UXkFLcVqGJRUNjvx0wTNnICLIC8pn6jP1avD1xr7vYufquFZ2kHdYtNKLK6VFE1zLoLhxd1_3sbEQQcXd1sj6It1kwXGUEYFDBEnFgkDsKfaU9HHe5zmBJm2v_X4jQ3tx3Lh7pvzbm6q1NnCcJs7k2ZIj-vHD4n5m4trWmBxfKtxY6hooRz8yg0hwIbJdyYgQztBbMQ9OQg-h65WdivfQmsvdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💎
Google Gemini API
دریافت رایگان توکن‌های هوش مصنوعی گوگل!
✨
امکانات:
🔸
دسترسی به مدل‌های Gemini 2.5 Flash، Flash-Lite و Pro
🔸
بدون نیاز به کارت اعتباری یا اشتراک
🔸
ساخت کلید API رایگان در چند دقیقه
🔸
توسعه اپلیکیشن با جدیدترین مدل‌های گوگل
📥
دریافت
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6984" target="_blank">📅 10:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6983">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AK6KwNvMzxYasM4RQgTyCqMKhSepqIKCbrRMTCOE074rfTyxo9w6JnFj73SG05P3Hw9-rQ8b0IotRrD19iFEjUm51r_DOgP4BNSVGOJNw5QA0Py-UT3pXhl4imHs39YUEZENj89UcDc1N6TEyAJ5aX4vECXu7ii8kbXhvb9Mlteujpu3y9pbIJDxvsDUjBxukJW7tq-I2RdJiU-23GEtyfS38nBpcKzC37WdOE1AB6LbHtci0Wjp_8cj-O8GXaL553lhCB2mYF_Th9oJN5aca-M-DVWzGHNrkQgZ2qPHvATHD6ohDkPhyJ06ryVTypwOLKRhM2UldcKtXYNQCdaJCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
هفته توسعه OpenAI
شرکت در رویداد و دریافت ۱۰۰ دلار اعتبار رایگان Codex!
❓
نحوه دریافت و جزئیات:
🔸
ثبت‌نام و ارسال درخواست شرکت در رویداد از طریق پلتفرم Devpost
🔸
مراجعه به تب منابع (Resources) در صفحه رویداد
🔸
کلیک روی گزینه "درخواست 100 دلار اعتبار Codex" و ثبت آن
🔸
مهلت ثبت‌نام:
تا ۱۸ جولای ۲۰۲۶
🔗
ثبت‌نام
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6983" target="_blank">📅 08:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6981">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏
🛡
مرورگر Cromite (کرومایت)؛ جانشین قدرتمند Bromite  (جایگزین کروم)  اگر از طرفداران مرورگر محبوب اما متوقف‌شده‌ی Bromite بودید، Cromite دقیقاً همان چیزی است که نیاز دارید! این مرورگر یک نسخه سفارشی (فورک) از کرومیوم و بر پایه برومایت است که با تمرکز شدید…</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6981" target="_blank">📅 02:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6980">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏
🛡
مرورگر Cromite (کرومایت)؛ جانشین قدرتمند Bromite
(جایگزین کروم)
اگر از طرفداران مرورگر محبوب اما متوقف‌شده‌ی Bromite بودید،
Cromite
دقیقاً همان چیزی است که نیاز دارید! این مرورگر یک نسخه سفارشی (فورک) از کرومیوم و بر پایه برومایت است که با تمرکز شدید روی
حریم خصوصی
و
حذف تبلیغات مزاحم
توسعه داده شده است.
✨
ویژگی‌های برجسته کرومایت:
*
🔸
ضدتبلیغ داخلی (Ad-blocker):
مسدودسازی خودکار تبلیغات و ردیاب‌ها بدون نیاز به نصب هیچ افزونه اضافی.
*
🔸
پشتیبانی از افزونه‌ها:
امکان نصب و اجرای اکستنشن‌ها (Extensions) در حالت توسعه‌دهنده (Developer Mode).
*
🔸
حریم خصوصی حداکثری:
محدود کردن و غیرفعال‌سازی ویژگی‌هایی از کرومیوم که برای ردیابی عادات وب‌گردی کاربران استفاده می‌شوند (قطع ارتباطات اضافه با گوگل).
*
🔸
مقابله با انگشت‌نگاری (Anti-Fingerprinting):
جلوگیری از شناسایی و ردیابی دستگاه شما توسط سایت‌های مختلف.
*
🔸
آپدیت خودکار:
دارای سیستم آپدیت داخلی در اندروید (همچنین پشتیبانی از مخزن رسمی F-Droid).
*
🔸
پشتیبانی گسترده:
قابل نصب روی اندروید (نسخه ۱۰ به بالا)، ویندوز و لینوکس (۶۴ بیتی).
🧪
نکته امنیتی:
این مرورگر برای استفاده روزمره و وب‌گردیِ امن و بدون ردیابی عالی است؛ اما خود توسعه‌دهنده صادقانه تاکید کرده که برای خبرنگاران یا افراد تحت محدودیت‌ها و سانسورهای شدید، همچنان استفاده از نسخه دسکتاپ
Tor Browser
پیشنهاد می‌شود.
🔗
[سورس پروژه و دانلود در گیت‌هاب]
🔗
[لینک مخزن F-Droid]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6980" target="_blank">📅 02:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6979">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">net.yukh.xui_81000@ArchiveTell.apk</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6979" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‏
📱
3X-UI Manager  مدیریت حرفه‌ای پنل 3x-ui در اندروید!
✨
امکانات:
🔸
کنترل چند پنل همزمان
🔸
ساخت کلاینت و لینک ساب
🔸
نمایش زنده منابع (فقط نسخه +3.3.0)
📥
دانلود: F-Droid و GitHub و Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6979" target="_blank">📅 02:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6978">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏
⚡️
پنل نهان (Nahan Panel)
ساخت و مدیریت فوق‌حرفه‌ای پروکسی (VLESS/Trojan) روی کلودفلر!
بدون نیاز به خرید سرور و درگیری با ترمینال، یک شبکه کامل و ضدفیلتر بسازید.
✨
امکانات برجسته سیستم:
🔸
نصب تک‌کلیکی:
راه‌اندازی خودکار Worker و دیتابیس D1 فقط با دادن یک API Token.
🔸
مدیریت آی‌پی و شبکه:
اسکنر داخلی برای آی‌پی تمیز (Clean IP)، آی‌پی پشتیبان (Relay) و مبدل پیشرفته NAT64.
🔸
مسیریابی هوشمند:
جداسازی ترافیک سایت‌های داخلی (GeoIP/GeoSite) برای اتصال بدون مشکل.
🔸
ضدفیلترینگ پیشرفته:
جعل اثرانگشت ترافیک (TLS Signature Chrome) و تنظیم دی‌ان‌اس اختصاصی (DoH).
🔸
ساب حرفه‌ای:
دامنه اختصاصی لینک ساب، مخفی‌سازی با تغییر User-Agent و نمایش حجم/تاریخ انقضای فیک برای گمراه کردن فیلترینگ.
🔸
امنیت بالا:
دکمه توقف اضطراری (Kill Switch)، مسیر ورود مخفی به پنل و استفاده از پورت‌های امن.
🔸
مدیریت همه‌جانبه:
اتصال به ربات تلگرام اختصاصی (فقط برای آیدی ادمین) و مدیریت همزمان چند پنل (Master/Slave) از طریق API.
🔸
نگهداری آسان:
آپدیت خودکار مستقیم از مخزن گیت‌هاب و بکاپ‌گیری/بازگردانی سریع با فایل JSON.
✅
تا به حال مسدودی روی این پنل گزارش نشده است.
🔗
اجرای مستقیم نصب‌کننده (وب)
🔗
سورس پروژه و پروکسی در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6978" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6975">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJMNOqpHacviHYz-hqAqYZ1BnD-fssXpxIiG5TGxXW9YJXSpvMvoR5p7MOSXRA3gEpRxeN7CxjZTYAerPX33R4MCRDCji91u4AUkdJ_CfSs5DkG9oUzJY9W_8XDv_85NqgqtlBWHC6hRZDHaXRK_sUBbVOrIe_TR1l-lSDnodm9g8mXFtrG6fZtlyv7_SKplhcwEUIy0xhxuSAefNjBNlaMBvznmFiU9o8y0klJIE6oTZnPwGmjF-wEUVl_1G9L4W9SXwq67zyDK3TRkzkqMHwS6J-L-qsgy0XdNfPWPAtbtT4joqUVrB7facigaq9sIoupvJt5xqFVnomxgKUqL4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
تلگرام دیگر برای اجرای ربات به سرور نیاز ندارد
❗️
با قابلیت جدید و فوق‌العاده
Serverless Bots
، از این پس می‌توانید کدهای ربات خود را مستقیماً روی زیرساخت خود تلگرام اجرا کنید.
✨
ویژگی‌های این قابلیت:
🔥
پشتیبانی از JavaScript:
کدنویسی مستقیم و سریع.
🔥
دیتابیس SQLite:
مدیریت داده‌ها درون خود اکوسیستم تلگرام.
🔥
میزبانی بومی:
اجرا مستقیماً توسط سرورهای تلگرام.
🔥
کاملاً رایگان (فعلاً):
صفر شدن هزینه‌های هاستینگ.
🧪
نکته: این یعنی ساخت و اجرای ربات‌های کوچک و متوسط، از این به بعد بدون هیچ‌گونه دردسرِ خرید و مدیریت سرور امکان‌پذیر است
🟠
⛓
منبع
👉
🔤
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6975" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6974">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏
📱
3X-UI Manager  مدیریت حرفه‌ای پنل 3x-ui در اندروید!
✨
امکانات:
🔸
کنترل چند پنل همزمان
🔸
ساخت کلاینت و لینک ساب
🔸
نمایش زنده منابع (فقط نسخه +3.3.0)
📥
دانلود: F-Droid و GitHub و Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6974" target="_blank">📅 22:37 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
