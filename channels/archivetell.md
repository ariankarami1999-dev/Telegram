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
<img src="https://cdn4.telesco.pe/file/UQ7VuJU0q3KyPSn2NK1IunUH7FOx-lVJBniobtsxCsUzIS7s-wp1P9nmEmfPxr4aLmHN0YC3gEBIYqfZj_pUQVxx7AgXHxLJMK476k8gc-GSNA6sGm_eRFRYgBzz9iBv3PUSBQx5fB9i9jBddzLQ4v31FB2zT4I7u28v3elxt5uOGQJNgRck_3RYrWx3aowE5qbCToOA0mbdgKGocYAYAB0D-zIxkD2neM1YkadUkzlkKF2ZQd9woIqC6OTHiKrrHzdRUBQle5Nlrh15sB7-vLZL5GikGBBdiJekynJ9mrYL2sZRapnVFuiR0mEpg6qmidd7PBohsgRbZMtChWPdEQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 6.43K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 02:28:21</div>
<hr>

<div class="tg-post" id="msg-4842">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEUDNg-JBmDlhoLP_Rqudxbzu6c5icfDQPSecvdFm6WsEkCIUU8FsqHY_xpaXTZdBH1QQnLY9_-4h15QjsSgsO7N9CcbnKPGVVBjmx7vz1FOcaV3p3plt1dK9cpYBZXuiHxChIRQ5KxDjv5Xrl7cI9N3eAob0rwkuZ_k0bKZQ0ZtpAVL_w1ZULnA7jiTTWNj3uEdfKlJVgaoo7CjHVi8tnp135SVQx_9dbjfKSCFaxeTXSxv8u6SinhkznRx0dr8wTIPTijtRiLpJhGZrLUMuj1yOP0p1qyVkdsRGNS-2G2orrhdO7kF5yXQAakPnNcuWPY3kyW4JPGA5dx7xgg5-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
20 سرور با قدرت متصل
📌
فایل برنامه
📌
لینک سایت
☕️
اموزش ساخت دامنه نتلیفای
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 263 · <a href="https://t.me/archivetell/4842" target="_blank">📅 02:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4841">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqe5nHlgPy1V_eVeCODxk6NXLVJbJ9qT9OfoYBE3zGb_faw-TFtDCHYAHxdMLUooPNnWOqtp6ZDgR_fhKYkHZWCE2DNpZXxW6SWBGbUH_xvVtXd0SHuiuwaXOKU0opAPneezO5mkrCsylpB4Rc6QJq7BWnOI68mv3HWPUOWM92BHsvOm063EzSZXRHQkdK6y3ua45lD9UWHIDJhYHdqCxzZTwr-PCSd3CyDbsOEJlIdUXW6ATcGxPA3wwyW6YazKfFCCEsYOm5NMcgsMN-Y82_To8zyMBmlfL90GRZTnZPIC051Zjw8UAnL5W5wzJqaRaFrIgTIEFXf8MW09saM0pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔆
سایت و برنامه کانفیگ ساز آپدیت شدند
📌
فایل برنامه
📌
لینک سایت
🌐
اضافه شدن سرور های تازه نفس
( اهدایی عزیزان
❤️
)
🔺
اضافه شدن کانفیگ ساز قدیمی
☕️
اموزش ساخت دامنه نتلیفای
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/archivetell/4841" target="_blank">📅 01:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4840">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔥
بهترین ابزارهای تحقیق، جستجو و تحلیل اطلاعات با هوش مصنوعی
1) Perplexity – جستجو، تحقیق و تحلیل سریع با منابع معتبر
لینک:
https://perplexity.ai
____
2)
ChatGPT Search – پاسخ‌های عمیق، تحلیل داده و جستجوی هوشمند
لینک:
https://chat.openai.com
____
3)
Andi Search – موتور جستجوی مکالمه‌ای با نتایج دقیق و خلاصه‌شده
لینک:
https://andisearch.com
____
4)
You.com
– جستجو، خلاصه‌سازی، تولید محتوا و ابزارهای هوش مصنوعی
لینک:
https://you.com
____
5)
Scite AI – تحلیل مقالات علمی، ارجاعات و منابع معتبر
لینک:
https://scite.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/archivetell/4840" target="_blank">📅 21:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4839">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIAZotEVsof0KiWjyt6fSx-2_G1BoJWm7YRFE1hGA7XSAmadU9-su--_7cMlVL8zzLohgeMPzeKTzcB_q4KBarn_3ZFYl6SQlfKL3F8RLe6sDpajf3gQv0MLJ2LcuQ8TuW0Sui39Pn31Ogv1lVON64ZjfhWsuCMoQf2DTdLiJ3dxo5tEUXyIdaAT0Pi6zSJRY9_Vi3pXvCJLenWtwWNBoNuEuXSvtQSlEeWb0ddqllkiXjAgl7lQMz7FR1GTBjoebA_KBurdCPPZn-0-p4rh-Rdm9FzvQk6Vi1n8uScwbJsIdZy2GP4QOY0qldlsWE7YUIsnwc4kXiSuQxbr0-R93A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ساب های کانال آپدیت شدند
🔺
لینک ها تغییری نکرده فقط اپدیت کنید
🔥
ساب جدید https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR_NETLIFY_SUB_new.txt
🚀
ساب قبلی https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR_NETLIFY_SUB.txt…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/4839" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4838">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رفع ارور No Internet در ویندوز  وقتی اینترنت قطع یا محدود میشه، ویندوز ممکنه اتصال وای‌فای رو ناپایدار نشون بده یا مدام پیام No Internet بده.  این روش فقط بررسی اینترنت توسط ویندوز رو غیرفعال می‌کنه و ممکنه مشکل نمایش اشتباه اتصال رو کمتر کنه.  مسیر: Win +…</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/4838" target="_blank">📅 19:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4837">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رفع ارور No Internet در ویندوز
وقتی اینترنت قطع یا محدود میشه، ویندوز ممکنه اتصال وای‌فای رو ناپایدار نشون بده یا مدام پیام No Internet بده.
این روش فقط بررسی اینترنت توسط ویندوز رو غیرفعال می‌کنه و ممکنه مشکل نمایش اشتباه اتصال رو کمتر کنه.
مسیر:
Win + R  :فشردن کلید
regedit
:وارد کردن عبارت
بعد برید به:
HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\NlaSvc\\Parameters\\Internet
مقدار زیر رو روی 0 بذارید:
EnableActiveProbing
بعد سیستم رو ری‌استارت کنید.
برای برگشت به حالت قبل، مقدار رو دوباره روی 1 قرار بدید.
@archivetell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/4837" target="_blank">📅 19:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4836">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👀
کروم اندروید رسماً هوشمند شد!
"گوگل جمنای رو کامل وارد مرورگر Chrome روی اندروید کرده و حالا مرورگر میتونه خیلی از کارهارو خودش انجام بده"
مثلاً:
فرم پر کنه،
خرید انجام بده،
صفحه‌ها رو خلاصه کنه،
یا حتی از داخل عکس‌ها اطلاعات استخراج کنه
📌
یه دکمه مخصوص Gemini هم کنار نوار آدرس اضافه شده که باهاش میتونی مستقیم درباره محتوای همون صفحه سؤال بپرسی!
🗣️
ولی قسمت عجیب ماجرا اینجاست:
جمنای فقط داخل مرورگر نیست…
به سرویس‌های گوگل هم وصله!
یعنی میتونه:
» رویداد اضافه کنه به Calendar
» لیست خرید بفرسته به Keep
» داخل Gmail دنبال اطلاعات بگرده
عملاً کروم داره تبدیل میشه به یه دستیار واقعی که به‌جای کاربر وب‌گردی میکنه
@archivetell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/4836" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4835">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رادار وضعیت اینترنت
http://radar.chabokan.net/
@archivetell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/4835" target="_blank">📅 18:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4834">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/archivetell/4834" target="_blank">📅 17:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4833">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQaci9ccmplpfqE4b6cm1dEZs2Uo-HtlbueATakbBuREpfvT6ZCs5e5Yawy5xZmBpEOd-MgrsFRyKjg_shKVNAFQLF3L2PKSDjCfqmwVq5Ll8vjiyw4Yvyo9h5E7WLRdanRZzdBAtUJEcQg9xno7gWlSbOwEF0WhKcB8nfGewk4rhD2nRfpwIFHyXQ7cVejcAI3mblpYoQsotyje95ycREau0ftYBY9vz9OrmNxL796pvG1jrFEoJCzhpmmtKwsKyOTwX47yPQ4XdHUDC5gFRw54y5xmeKEMeppUYd5eB7lHgCLD_6aFq36kMksqN6_CO_MF2qZZ4amewc8DBoD-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
میگی g2ray ساختم وصل نمیشه؟؟
🚀
دوستان، اگر بعد از اجرای G2RAY در گیت‌هاب کداسپیس برای اتصال مشکل دارید، این آموزش کوتاه رو مرحله به مرحله انجام بدید تا کانفیگتون بدون مشکل وصل بشه:
1️⃣
اجرای سرویس:
ابتدا پروژه رو در GitHub Codespaces ران کنید تا اسکریپت اجرا بشه و پیام G2RAY - XRAY SERVICE INITIALIZED رو در ترمینال ببینید.
2️⃣
پابلیک کردن پورت (مهم‌ترین مرحله
⚠️
):
به‌صورت پیش‌فرض، گیت‌هاب پورت‌ها رو پرایوت (Private) نگه می‌داره. این یعنی کلاینت شما به‌جای اتصال به پروکسی، پشت صفحه لاگین گیت‌هاب گیر می‌کنه!
* پایین صفحه سمت راست، روی تب
Ports
(آیکون آنتن) کلیک کنید.
* پورت
443
رو پیدا کنید.
* روی اون کلیک راست کنید (یا نگه دارید) و گزینه
Port Visibility
رو از حالت Private به
Public
تغییر بدید.
4️⃣
آپدیت هسته Xray (Xray Core):
چون این کانفیگ از پروتکل جدید xhttp استفاده می‌کنه، حتما کلاینت آپدیت کنید. قدیمیا این پروتکل رو نمی‌شناسند.
✅
کانفیگ رو کپی کنید، توی برنامه ایمپورت کنید و متصل بشید. لذت ببرید!
✌️
@archivetell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/4833" target="_blank">📅 17:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4832">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">۱۰ دقیقس دارم پست مینویسم، ارسال رو زدم تلگرام کرش کرد. درباره g2ray میخاستم بگم که میگین وصل نمیشه‌.
ولی نمیگم دیگه</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/4832" target="_blank">📅 17:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4828">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pg1sa45QQE6pN6EzHMlbn56x5W0zFnD2tRvCFcN-4lf4iOxTQs-pce9Xcpo9jZ1zFtNGDkWAYPXqZ5fXDQSnz__B7jUZ19fjFIMGNo3mUdo6CsToTgfyWLFkzRMtEJtvgGUWmyWB5CHyCBMkBbdBGYolBXdHyf3Vre_st4MQB9fs3UsdZrv4Xv5mM12aiwWiBqo3J5RL7CvwAnKRrv8EstRPFoDlMrKC4mLHbwgAamY20vJ9FNEpeYXPjtWJqa6NEbXR86w0qjHjCIvuuCzM_T4G5b61VL3BoukAWB9Z6FQkSOitig02Y3mgXQY-Xq4rwAk8SRi0r7HuZuSQx8ExVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید UI جمینای  با الهام از open ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/4828" target="_blank">📅 16:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4827">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">لینک داخلی آخرین نسخه Happ اندروید
دانلود
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/4827" target="_blank">📅 14:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4826">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚀
ساب های کانال آپدیت شدند
🔺
لینک ها تغییری نکرده فقط اپدیت کنید
🔥
ساب جدید https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR_NETLIFY_SUB_new.txt
🚀
ساب قبلی https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR_NETLIFY_SUB.txt…</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/4826" target="_blank">📅 14:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4825">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-text">🚀
ساب های کانال آپدیت شدند
🔺
لینک ها تغییری نکرده فقط اپدیت کنید
🔥
ساب جدید
https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR_NETLIFY_SUB_new.txt
🚀
ساب قبلی
https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR_NETLIFY_SUB.txt
🚀
ساب های متغیر رندوم ( با فیلترشکن باز کنید )
https://sub.ir-netlify.workers.dev/new
https://sub.ir-netlify.workers.dev/
⚠️
: ساب قدیمی نیاز به اهدای دامنه داره شدیدا لطفا
ورژن 1.0.2 پروژه
رو دپلوی کنید و دامنه نتلیفای اش رو بدید دایرکت
t.me/IR_NETLIFY?direct
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/archivetell/4825" target="_blank">📅 14:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4824">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">VaultGram
یک ربات تلگرامی برای ذخیره‌سازی امن فایل‌هاست.
@VaultGramStorageBot
- فایل‌ها در «حساب خزانه» جداگانه نگهداری می‌شوند؛ حتی اگر حساب اصلی‌تان حذف یا مسدود شود، داده‌ها ناپدید نمی‌شوند.
- رسانه‌ها (عکس/ویدیو) و اسناد (ZIP, RAR, Docs) در پوشه‌های مخصوص خود سازماندهی می‌شوند.
- با نام کاربری و رمز عبور حساب خزانه می‌توانید از هر حساب تلگرامی به این فایل‌ها دسترسی داشته باشید.
- یک کلیک کافی است تا تمام محتوا را بازیابی کنید.
به‌صورت کلی، VaultGram داده‌های شما را به‌صورت مستقل، منظم و با حریم خصوصی بالا نگه می‌دارد.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/4824" target="_blank">📅 14:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4823">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ClonethBot
رباتی برای ساخت هوش مصنوعی شخصی در تلگرام
@clonethbot
- مدل‌ها: شامل
Minimax M2.5
و
Nemotron 3
؛ هر دو بدون نیاز به کلید API کار می‌کنند.
- پاسخ‌ها: نامحدود و رایگان؛ می‌توانید به‌صورت مستقیم در چت با ربات گفت‌وگو کنید.
- راه‌اندازی: فقط کافی است ربات را به‌عنوان منبع مدل انتخاب کنید و از دستورات ساده برای تنظیم پارامترها استفاده کنید.
برای شروع، ربات را در تلگرام پیدا کنید و دستور
/start
را بفرستید.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/4823" target="_blank">📅 14:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4822">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">📌
ربات برای ssh زدن به سرور:
@EazySSH_bot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/4822" target="_blank">📅 14:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4820">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxDUSL2tDvW9MLttsTaigtSWKaa0-qEQPAJimYJEhmxxYwEQvOduJwQqVLl_H48smRlggl4nQ2jCZc-2LiwtbOZbQ8yDGivusztLDKhlYeOocYstuMEq2jlyNM1FcMwP9urMUxeCyjU8mUwSx-ASYIaj9yXrtHSFduwbnIW0CUHVvJaleWKB1BNmvU64IQGAd1fB8R49JQxyamGg2KYVcBFiM2Bvx-yhaHF2aUc-jcxYvgJ6Edp-pfO9BgF_hQUgFpPdrZJgmc8EMOM5lhuIWOdP4qFNaFrXiny01pa8-w4RZmNBCdpp347FKl9Maeyo387sjRVMbtUyO8uWxPMkiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔆
سایت و برنامه کانفیگ ساز آپدیت شدند
📌
فایل برنامه
📌
لینک سایت
🚀
وصل شدیم (بقیه سرور ها هم بزودی فیکس میشن)
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/4820" target="_blank">📅 12:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4819">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دوستان ، تغییر نتلیفای کسایی که قطع شدن
نمیدونم با این تغییر چقدر دووم داشته باشه من که فعلا وصلم.
یه تغییری باید سمت سرور و کلاینت بدید
اگه سرور ندارید صبر کنید صاحب سرور انجام بده خبر بده
سمت سرور
:
اگه پنل ثنایی دارید ، قسمت inbound
یه فیلد هست نوشته
padding bytes :
و خالیه شما بکنیدش 1-1
اینجوری میشه :
padding bytes : 1-1
اگرم xray دستی نصب کردید و پنل ندارید باید فایل config.json ادیت کنید زیر path همینو اضاف کنید که احتمالا بلد باشه هرکی دستی نصب کرده.
حالا
سمت کلاینت :
کانفیگتون رو ادیت کنید (علامت مداد)
زیر path
عنوانش نوشته Xhttp extra raw JSON...
داخلش اینو بنویسید یا اضاف کنید
{ "xPaddingBytes": "1-1" }
اگر خالی نیست هم همچین فرمتی میشه(البته من از فرمت بالا استفاده کردم این پایینی رو یکی از بچه ها فرستاده تست نکردم) :
{"headers":{"x-host":"netlify.parsashonam.sbs:444"},"xPaddingBytes":"1-1","scMaxEachPostBytes":"1000000"}</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/4819" target="_blank">📅 11:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4818">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نتلیفای وصل
kubernetes.io
،
50.7.5.83
65.109.34.234
،
kustomize.sigs.k8s.io
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/4818" target="_blank">📅 11:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4817">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👾
لیست دانلود برنامه ها با نت ملی
1️⃣
WhiteDNS
1.1.0
(نسخه ی رسمی)
4️⃣
NekoBox v8a
●
NekoBox v7a
1.4.2
7️⃣
The Feed
0.17.5
📱
Telegram
(گوگل پلی)
12.7.2
📱
Telegram
(رسمی)
12.7.2
📱
Telegram
(Windows)
12.7.2
📱
Whatsapp
2‌.26‌.17.‌72
💬
Instagram
v415.0.0.36.76
👑
ShiroKhorshid
2026.03.17
5️⃣
Mhrv Rs
v1.9.14
📶
Npv
123
📶
V2box
5.3.4
📶
V2ray Ng
2.18
📶
V2ray Ng
(Windows)
3️⃣
Am tunnle
(pro)
37
3️⃣
Am tunnle
(lite)
🕊
Slipnet
2.5.3
2️⃣
Masterdns
1.0.9
📶
Open vpn
3.71
📱
Happ
3.20.4
💻
Happ
(Windows)
📶
Psiphon
462
📶
Psiphon
(Windows)
8️⃣
Bd net
104
6️⃣
Mahsang
15
📶
http injector
6.5.0
📶
Wireguard
1.0.20260315</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/4817" target="_blank">📅 11:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4816">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">لینک داخلی V2rayn ویندوز
دانلود
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/4816" target="_blank">📅 11:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4815">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">به زودی جنگ میشه..
دارن همه راه ها رو میبندن تا دوباره فقط آیپی های وایت وصل بمونن و قیمت رو ببرن بالا</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/4815" target="_blank">📅 08:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4814">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">جدیدترین سریال ها
https://www.nilfgaard.top
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/4814" target="_blank">📅 07:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4813">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یه سری گفتن نتلیفای وصل شده دوباره ولی برای من نشده. برای دوستانی که از نتلیفای لعنتی رکب خوردن:
(شکن ظاهرا تو این قطعی نقشی نداشته ولی از کجا معلوم پشت پرده یه صحبت ریزی کرده باشن!)
یه راه حل
موقت
(امیدوارم آدما‌ی نتلیفای اینجا نباشن) که کانفیگ رو دوباره زنده میکنه ولی Pros and Cons خودش رو داره از این قراره: PaddingBytes رو توی کانفیگ غیر فعال کنید و کانفیگتون به کار می‌افته طبق مراحل زیر. قبل از هرچیز: من اینا رو با شکن تست کردم و جواب داد ولی شما باید خودتون اینو تست کنید. اساسا ایده‌ی xPaddingBytes برای مبارزه با DPI بوده و شاید این روش مناسب نباشه.
۱. برای سمت کلاینت v2Ray، این بخش رو به XHTTP Extra Raw Json کانفیگ اضافه کنید تا پدینگ بشه فقط یک بایت. (و بعد مطابق معمول کانفیگ رو به صورت لینک یا JSON بفرستید برای بقیه)
{ "xPaddingBytes": "1-1" }
همچنین ظاهرا ویژگی‌های ظاهری پدینگ هم قابل تغییر و رندوم کردن هست (پیش‌فرض فقط ۱۰۰ الی ۱۰۰۰ تا X). با این من راهی پیدا نکردم که پدینگ رو کامل خاموش کنه از سمت کلاینت.
۲. مهم: قاعدتا باید سمت سرور هم همین تغییر رو بدید، چون سرور Xray حداقل تا نسخه‌ی 26.3.27 حتما چک می‌کنه که کلاینت این پدینگ رو با سایز درست (که پیش فرض اندازه‌ی ۱۰۰ تا ۱۰۰۰ بایت هست) داشته باشه. دو راه پیش روی من بود، یا این تنظیم رو توی سرور عوض کنم (و از اون ور هم سایز پدینگ بشه ۱ بایت)، یا کلا سرور رو پچ کنم (و البته ظاهرا یه درخواست از طرف توسعه‌دهنده‌ها هم هست برای Xray Xhttp که الزام داشتن پدینگ از سمت سرور برای کلاینت رو حذف کنه).
من سرور رو پچ کردم چرا که می‌خواستم رفتار سرور عوض نشه (و نتلیفای حداقل
هنوز
رفتار سرور براش مهم نیست یعنی پدینگ‌های از سمت سرور رو کاری نداره)، شما می‌تونید تلاش کنید که xPaddingBytes رو توی تنظیمات سرور بذارید "1-1" مشابه کلاینت (من با پنل ثنایی و اینا کار نکردم، یحتمل از اونجا هم میشه این تنظیم رو داد).
اگر می‌خواید مثل من پچ کنید، مشابه تغییر branch پایین (نه main) بیلد کنید برای لینوکس یا غیره و باینری رو جایگزین کنید (فورک از ورژن 26.3.27). بیلد کار پنج دیقس، از AI بپرسید.
🔹
به هیچ وجه باینری از کسی نگیرید! خودتون بیلد کنید.
https://github.com/Sprimesson/Xray-core/tree/feature/no-xpadding-checks
اگر میخواید پچ نکنید و بجاش کانفیگ سرور رو با کلاینت یکی کنید (من تست نکردم) باید ذیل xhttpSettings توی config.json همین اضافه شه مثلا:
"xhttpSettings": {
"path": "/s1",
"xPaddingBytes": "1-1"
}
۳. یه موضوع دیگه که من به نظرم مهمه: من کانفیگ‌هام دو تا نسخه داره Normal و Slow. توی Slow، تاخیر توی ارسال POST اضافه کردم و این باعث میشه پینگ کانفیگ بره بالا ولی روی سرعت آپلود تاثیر ملموسی نداره (برای دانلود هم به نظر میاد فرقی نداره). استفاده از Slow باعث میشه تعداد ریکوئست به نتلیفای لعنتی (که سرگردنه وایساده و قیمت گیگی/ریکوئستی‌ش از رقباش که اونم حرومزادن و دامین فرانتینگ رو بستن بالاتره) کمتر بشه و به عبارتی اقتصادی‌تر باشه. مثال برای XHTTP Extra Raw JSON:
{
"xPaddingBytes": "1-1",
"scMaxEachPostBytes": "4000000",
"scMinPostsIntervalMs": "500-1000",
"scMaxBufferedPosts": 30,
"scStreamUpServerSecs": -1,
"xmux": {
"maxConnections": 3,
"hMaxRequestTimes": 0,
"hMaxReusableSecs": 0,
"hKeepAlivePeriod": -1
}
}
این JSON ها وارد لینک کانفیگ میشن و مشکلی نیست.
Source</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/4813" target="_blank">📅 07:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4811">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">aio‑downloader  اسکریپت AIO Downloader یه ابزار متن‌باز و کاربردی برای دانلود فایل و محتوا از سرویس‌هایی مثل یوتیوب، گیت‌هاب، اینستاگرام، ایکس، تلگرام، گوگل‌پلی، تیک‌تاک، پینترست، ساندکلود و ... هست، که فرایند دانلود رو از طریق GitHub Actions انجام میده. این…</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/4811" target="_blank">📅 00:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4810">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">aio‑downloader
اسکریپت AIO Downloader یه ابزار متن‌باز و کاربردی برای دانلود فایل و محتوا از سرویس‌هایی مثل یوتیوب، گیت‌هاب، اینستاگرام، ایکس، تلگرام، گوگل‌پلی، تیک‌تاک، پینترست، ساندکلود و ... هست، که فرایند دانلود رو از طریق GitHub Actions انجام میده.
این ابزار طوری طراحی شده که در شرایط محدودیت شدید اینترنت و وایت‌لیست فعلی بتونه بسیاری از فایل‌ها و لینک‌ها رو دریافت کنه، بدون اینکه نیاز باشه سیستم یا سرور شخصی برای دانلود داشته باشین.
با توجه به اینکه این پروژه به GitHub Actions متکیه، بهتره برای استفاده ازش از اکانت اصلی گیت‌هاب استفاده نکنین و ترجیحاً یک اکانت جداگانه بسازین.
لینک پروژه:
https://github.com/ProAlit/aio-downloader</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/4810" target="_blank">📅 00:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4802">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I__83P7Oc-WN91j4YyWrwTEqiILqOnNgfemeOoBEaE1Yxtq_xnv3yDghmt8aP2umYEKD23Rkkn-jLcqI1DEu9imSkrnT4F9gCydkOYFVzRmC_Ir2KMZy0WS-MMO_zpw81gpX-oTasKZcnOx8cx_IBc2_xhmdeYVVxDY1jKbhhiUgA_oYrhDPo6WrFKVegc3pen9d3t2CZh47tpQ-3sn-_5yZR4gTs5oB1UvW_P9Su6n8yLcESW_sV-amHpLsUdIHiKz75JmAjUqNZ1IlzRFXK4wh41MD2iSa0TzreH6mP5Z5dyX1A0uJhCBmP4TbYiv9-GspKzQl2ezNv7hoDiRKfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتلیفای بای بای       @ArchiveTell</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/4802" target="_blank">📅 00:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4800">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تا ۱۰ روز دیگه جنگ میشه..</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/4800" target="_blank">📅 00:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4798">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نتلیفای بای بای
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/4798" target="_blank">📅 00:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4797">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سایت های موزیک بدون فیلتر
http://toogoosh.com
https://rozmusic.com/
https://upmusics.com/category/single-tracks/
https://musics-fa.com/download-songs/
https://bir-music.com/
https://biamusic.ir/
https://mahanmusic.net/top-songs/
https://radio.biato.in/
http://Sptfy.ir
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/4797" target="_blank">📅 00:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4794">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فیلم و سریال بدون سانسور
Movieyaab.ir
f2mux.top
www.myf2mi.top
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/4794" target="_blank">📅 23:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4793">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سایت داخلی برای دانلود frimware ios
https://ipsw.top/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/4793" target="_blank">📅 23:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4792">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">چطوری تشخیص دهیم سرور شما اسپوف خور هست
؟
روی سرور مقصدت بزن
tcpdump icmp
بعد روی سرور ایرانت بزن
iptables -t nat -A POSTROUTING -d TARGET-IP -j SNAT --to-source SPOOF-IP
ping -c 10 TARGET-IP
تارگت ایپی ایپی سرور مقصده،
اسپوف آیپی ایپی ای که سفیده میخوای اسپوفش کنی
اگه تو ترمینال سرور مقصدت پکت ها اومد و ایپی جعلی روشون بود ایرانت میتونه اسپوف بزنه اگه هیچی نیومد تو tcpdump اسپوف خور نیست.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/4792" target="_blank">📅 23:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4791">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ربات جمنای
@Gemini_PV_bot
@NewGeminiAi_bot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/4791" target="_blank">📅 23:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4790">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ربات های هوش مصنوعی همه مدل ها
@chat_llm_100_bot
@GPT4Telegrambot
@GratomicAiBOT
@GPT4_Unlimit_bot
@GPT4AgentsBot
@grok_gidbot
@ChatGPT_grok4bot
@ChatGPT_General_Bot
@Javidiran_bot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/4790" target="_blank">📅 23:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4789">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">آموزش_اپلود_و_استفاده_اسکریپت_در_کولب_گوگل.pdf</div>
  <div class="tg-doc-extra">2.5 MB</div>
</div>
<a href="https://t.me/archivetell/4789" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
دانلودر حرفه‌ای و پرسرعت یوتیوب مستقیم به گوگل درایو! (بدون مصرف حجم اینترنت) خسته شدید از سایت‌های پر از تبلیغ، قطعی‌های مکرر و محدودیت سرعت برای دانلود از یوتیوب؟ ما یک اسکریپت اختصاصی و هوشمند برای محیط Google Colab آماده کردیم که به شما اجازه میده ویدیوها،…</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/4789" target="_blank">📅 23:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4785">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ربات تبدیل ویس به متن
@VoiceToTextMasterBot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/4785" target="_blank">📅 19:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4784">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
امروز می‌خوایم درباره موضوعی حرف بزنیم که احتمالا از این به بعد بیشتر اسمش رو می‌شنوید؛ مخصوصا برای کسایی که خرید
کارت به کارت
کانفیگ از شخص یا ربات انجام میدن
❗️
یه سری گزارش بهمون دادن
از طرف No Caller ID براشون زنگ زدن و سوال‌هایی مثل:
● شما به شخص "برفرض قلی زاده" واریز کردید میشناسیدش؟
بدبینانه ترین حالتش اینکه:
● ما از تماس**** میگیریم شما از کجا کانفیگ خرید کردید؟ بیاید اداره تعهد بدید و بیاید اینجا توضیح بدید دارید چه کاری با vpn انجام میدید.
اول باید یه نکته مهم رو بدونید:
خیلی از فروشنده‌های کانفیگ، پرداخت رو به‌صورت کارت‌به‌کارت انجام میدن که بتونن مشتری بکشن این کارت‌ها معمولا دو حالت دارن:
۱️⃣ یه سری فروشنده‌ها مدت طولانی از یک کارت ثابت استفاده می‌کنن و ظاهرا مشکلی هم براشون پیش نمیاد (پارتی دارن)
۲️⃣ یه سری دیگه مدام کارت عوض می‌کنند بصورت روزانه و هفتگی ؛ بحث اصلی ما با این دسته‌ست.
مشکل از جایی شروع میشه که ۱۰۰٪ از این کارت‌ها اجاره‌ای هستن.
معمولا بعد از مدتی حساب مسدود میشه و صاحب کارت باید بابت تراکنش‌ها توضیح بده و درگیر دردسرهای پولشویی و قضایی بشه.
از اون طرف، تمام تراکنش‌ها داخل سیستم بانکی ثبت میشن:
شماره حساب، اسم و شماره طرفین، مبلغ، زمان تراکنش و...
حالا اگر مشخص بشه اون حساب برای فروش VPN یا کانفیگ استفاده میشده، طبیعیه که تراکنش‌ها و افراد مرتبط بیشتر بررسی بشن.
که ۱ ماه پیش خبر این تو کانالها پخش شده بود از پیش شماره Vaja برای کانفیگ فروش هایی که مستقیما از کارت خودشون استفاده می‌کردن پیام رفته براشون
🤔
حالا میپرسید راه‌حل چیه؟
تا جای ممکن کارت به کارت نکنید.
بهتره به جای این مدل پرداخت‌ها از روش‌هایی استفاده بشه که مستقیم به کارت‌به‌کارت نباشن؛
مثلا پرداخت از طریق تراست ولت یا صرافی‌های ارز دیجیتال مثل نوبیتکس یا بیت‌پین و خیلی صرافی های دیگه که ثبت‌نام تو این صرافی ها هیچ سختی نداره و عرض ۵ دقیقه ثبت‌نام میشه کرد
در نتیجه پیشنهاد میشه تا حد امکان از کارت‌به‌کارت به حساب‌های متفرقه خودداری کنید
میگید به خودتون چرا مشکلی نداره که؟ اینم فکرشو بکنید که بابت کانفیگ ۲۵۰ تومنی برید خودتون رو به دردسر انداختید و حالا باید جواب هم پس بدید
🥴
این موضوع احتمالا در هفته‌ها و ماه‌های آینده بیشتر درباره‌ش خواهید شنید که  از No Caller ID تماس گرفته شده. خیلی‌ها الان جدی نمی‌گیرنش، ولی بعدا درگیر این موضوعات میشن که دیگه خیلی دیر شده
ℹ️
هدف ما ترساندن نیست و صرفا جهت آگاهی و امنیت شما اطلاع رسانی شده
❤️‍🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/4784" target="_blank">📅 18:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4782">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚀
قابلیت جدید Codex
با یک کلیک انتقال پروژه‌ها/گفتگوها بین Claude و Codex
- استفاده از قدرتمندترین مدل برای کدنویسی هوش مصنوعی
- صرفه‌جویی در زمان و بهبود کار تیمی
https://chatgpt.com/codex/switch-to-codex/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/4782" target="_blank">📅 17:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4781">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Balancer_ArchiveTell.html</div>
  <div class="tg-doc-extra">28.3 KB</div>
</div>
<a href="https://t.me/archivetell/4781" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Balancer.html</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/4781" target="_blank">📅 16:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4780">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎉
۸ ابزار هوش مصنوعی فقط برای سرگرمی
1️⃣
هنرمند تتو – طراحی خودکار تتوهای خلاق
🔗
https://tattoosai.com
2️⃣
صحبت با کتاب‌ها – گفتگو با متن‌های کتابی به‌صورت صوتی
🔗
https://books.google.com/talktobooks/
3️⃣
عکس‌های قدیمی – بازسازی و رنگ‌آمیزی تصاویر تاریخی
🔗
https://myheritage.com/ai-time-machine
4️⃣
سلام به گذشته – تعامل با شخصیت‌ها و رویدادهای تاریخی
🔗
https://hellohistory.ai
5️⃣
جعل خود – ساخت صداهای مصنوعی شبیه به خودتان
🔗
https://fakeyou.com
6️⃣
وعده غذایی غیرواقعی – منوهای خیالی و جذاب برای لذت بصری
🔗
https://unrealmeal.ai
7️⃣
تغییر چهره با هوش مصنوعی – سوئیچ و ترکیب چهره‌ها به‌صورت لحظه‌ای
🔗
https://hey.reface.ai
8️⃣
تغییر صدا – تبدیل صدا به انواع شخصیت‌ها و افکت‌ها
🔗
https://voicemod.net
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/4780" target="_blank">📅 16:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4779">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Balancer.html</div>
  <div class="tg-doc-extra">13.2 KB</div>
</div>
<a href="https://t.me/archivetell/4779" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
ابزار اختصاصی ساخت کانفیگ بالانسر برای v2rayNG
🚀
> خسته شدی از بس دستی بین کانفیگ‌ها سوییچ کردی تا یه سبزشو پیدا کنی؟
با این ابزار ساده، تمام کانفیگ‌هاتون (حتی لینک‌های نامرتب با پروتکل‌های جدید مثل xhttp) رو یکجا وارد می‌کنید و در ازاش یک «کانفیگ کاستوم هوشمند» تحویل می‌گیرید.
>
⚡️
چیکار می‌کنه؟
> این کانفیگ به صورت خودکار پینگ تمام سرورهای شما رو (مثلاً هر ۶۰ ثانیه) چک می‌کنه و ترافیک شما رو بدون قطعی روی
سریع‌ترین سرور
میندازه (LeastPing).
>
🔒
۱۰۰٪ امن و آفلاین (توی مرورگر خودتون اجرا میشه)
>
📥
کافیه فایل HTML رو باز کنید، کانفیگ‌ها رو بدید و خروجی JSON رو توی v2rayNG کپی کنید. فق دستی کپی کنین
‌
🆔
@archivetell</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/4779" target="_blank">📅 16:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4778">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دوستان برنامه نویس خیّر اندروید کسی هست؟
کار اونقدی سخت نیست
دایرکت یا پی وی پیامم بده
کار عام المنفعه هست برای اتصال به اینترنت</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/4778" target="_blank">📅 16:02 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4777">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gn0X3W5Tmr3SoivEv-v8MuJdqP996PQ4_3KHzMdwqZBNepG0kYX6Nr81IoPFvARNbuVcbeNdT-rTPgP9eo78JNZov8mYPKJTCJIzzVMwhQIjI7U8gltG06b2JPvwHZVU4HXuG0jxwJCMi-K4lCHYhqtsu48srApdd0Dh0sIO6yVFX1JljRO3tWcpJasoQBza14vQVDvNtdDIdDKfNbAr8usGE9IYWUAOuWmtDZn4euBdGRqj7FMKlz5NTIxD4Q0Lv-XIKXgkDbIudwHVYbyGscj2vOE8GEW8rOrUMjrGr3yA7h56fz5waGCWLSUeCoDInSlKjB3DljNWyogn4nxdKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔆
سایت و برنامه کانفیگ ساز آپدیت شدند
📌
فایل برنامه
📌
لینک سایت
🌐
اضافه شدن سرور های جدید ( اهدایی عزیزان
❤️
)
🔺
بهینه شدن لیست BEST
⚡️
اضافه شدن sni های جدید
●  کانفیگ ساز جدید فقط روی
نسخه 1.0.3 پروژه
کار میکنه
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/4777" target="_blank">📅 14:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4776">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ربات فشرده‌سازی فایل‌های PDF
📖
📚
@PDF_Compress_Robot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/4776" target="_blank">📅 13:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4774">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UgVfHDoIRWuY-diQ8v4vThPVkvFBgtteQQZk9HDmrCPyP4V2aDi6Ig74XPxvcRb90XKsTq5QO2TCtyzs8loh_QGYJ_NWP1j13qc1_mFAI6hsR9CvCZNbnJT0YRPJfBOJeajCAuF6UvH7I4Bnb6cZj9mSCd1c-Yf-0QqtdhdnqqqgkAuFMOCMNsBljNqi5CdmUNyA64uZ-tWpZcfJudNZO6sHxKYYvfCPNo6DxMWVihoMoz4jFmuWJ-HG6IUsWmVp_Xnkyjp6GISlDVjVDmHpoQpwcj9JCL4hm1GRW0Jg6DOrXAul2x_jo0cVW8aomc3tZS1jRKr063joI4NHNpXnKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
MattDownloader
نسخه اول منتشر شد
❤️
می‌خوای ویدیو از یوتیوب (یا هر لینک دانلودی دیگه رو) بدون VPN بگیری؟ با MattDownloader این امکان میسر میشه:
GitHub Actions روی فورک خودت فایل را از اینترنت دانلود میکنه و آماده‌اش میکنه؛ تو فقط با اپ از همون گیت‌هاب بدون اینکه روی گوشی VPN لازم داشته باشی، فایل نهایی رو می‌گیری و ذخیره می‌کنی. یعنی گوشی بیشتر با گیت‌هاب حرف میزنه، نه مستقیم با سایتی که برات مسدود یا ناپایدار است.
چطور کار میکنه؟ لینک را به اپ می‌دهی (مثلاً لینک ویدیوی یوتیوب که به لینک مستقیم تبدیلش کردی)، ورک‌فلو روی ریپوی تو اجرا میشه، بعد اپ فایل آماده را از مسیر jobs میخونه و روی دستگاه دانلود میکنه.
🎬
مناسب برای ویدیوهای یوتیوب و لینک‌های سنگین
⚡
ست‌آپ یک‌بار با توکن و آدرس فورک
📥
دانلود نهایی از گیت‌هاب
🖼️
امکان ذخیره در گالری برای ویدیو/عکس
راهنما و APK اینجاست:
https://github.com/matthewnet/MattDownloader
آخرین نسخه برای نصب:
https://github.com/matthewnet/MattDownloader/releases/latest
تجربه‌تون را بفرستید
💙
برای دریافت نسخه‌های بعدی:
@mattspoof</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/4774" target="_blank">📅 12:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4773">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚀
دانلودر حرفه‌ای و پرسرعت یوتیوب مستقیم به گوگل درایو! (بدون مصرف حجم اینترنت) خسته شدید از سایت‌های پر از تبلیغ، قطعی‌های مکرر و محدودیت سرعت برای دانلود از یوتیوب؟ ما یک اسکریپت اختصاصی و هوشمند برای محیط Google Colab آماده کردیم که به شما اجازه میده ویدیوها،…</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/4773" target="_blank">📅 12:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4772">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLXGDyp6-2l9idUZnkJCTflofFazmDeCxWmQwOrNiKlkV-aqQuwUIBxKDksPIv8QMiWMnZOMIQjfl87CDHF0QCoaq9hUK1ix2nF1gVDCV_fGHCeb5cFiG608XbqghFI_f5q-NOIQeiXZxxO6qERiFEXngh9e52Kdn9XN-qIhz5HIcUAmti0cDM-v8lH-oC_q7r-VfTsGA-Z4sI6iJreQRArbpIwHGxkaTNU0dzeIvWkklekJLUbeIbnCzX-_oHTZDhbZgh6tBf5D94Ce0OgkBOWvIoBXJyPxo85QGOgaU2QSin37tLLbaRUG_NKlDJBJYX-k6GNxeHaVWM_VHXsAYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت درحال احراز کردن IP سرور های ایران هستش. اینطوری صاحب هر IP برای حکومت کاملا مشخص میشه.
قبل از این، دیتاسنتر ها احراز رو خودشون انجام میدادن اما برای اکانتی که میسازید نه IP سرور. اگه حکومت هر دستوری بابت پیگیری IP خاصی میداد، باید از فیلتر ISP عبور میکرد که میشد با روش هایی دورش زد یا گردن نگرفتش
اما الان خود حکومت دیگه میدونه کدوم IP برای چه شخصی هستش...
@ArchiveTell
Source</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/archivetell/4772" target="_blank">📅 12:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4771">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ربات تبدیل صدا به متن رایگان
@sedatextbot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/4771" target="_blank">📅 11:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4770">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚀
آموزش صفر تا صد راه‌اندازی تونل ریورس (Reverse Tunnel) در 3x-ui
---
رفقا سلام!
✋
امروز یه آموزش پایه‌ای اما به‌شدت کاربردی داریم برای راه‌اندازی تونل Reverse بین دو پنل 3x-ui (سرور ایران و خارج).
ممکنه بسته به شرایط سرورتون نیاز به یه سری تغییرات ریز داشته باشید، اما ساختار اصلی و تضمینی همینه!
مرحله ۱: ساخت Inbound روی سرور ایران
🇮🇷
1️⃣
وارد پنل 3x-ui سرور ایران بشید و به بخش Inbounds برید.
2️⃣
دو تا کانفیگ باید بسازید:
🔸
کانفیگ اول (برای Tunnel):
• Protocol: VLESS (یا پروتکل دلخواه)
• Transport: WebSocket
• Path: /tunnel
• Remark: tunnel
• Port: حتماً یکی از پورت‌های پشتیبانی‌شده توسط CDN (مثلاً 8080 یا 2082)
🔸
کانفیگ دوم (برای User):
• Protocol: VLESS
• Transport: WebSocket
• Path: /user
• Remark: user
• Port: یکی از پورت‌های CDN (مثلاً 8080)
⚠️
نکته به‌شدت مهم: حتماً از پورت‌هایی استفاده کنید که CDN (مثل ابرآروان یا کلودفلر) اجازه می‌ده؛ مثل: 80, 443, 8080, 2052, 2082, 2086, 2095.
مرحله ۲: تنظیم Reverse روی سرور ایران
🇮🇷
1️⃣
برید به بخش Xray Config و بعد تب Reverse.
2️⃣
یه Reverse جدید بسازید (بخش Portal):
• Tag: portal
• Domain: یه اسم دلخواه (دقت کنید که روی سرور خارج هم باید دقیقاً همین باشه).
3️⃣
حالا Mapping رو انجام بدید: کانفیگ tunnel رو وصل کنید به user (یعنی Tunnel ➔ User) و ذخیره کنید.
مرحله ۳: انتقال کانفیگ به سرور خارج
🌍
1️⃣
از کانفیگ tunnel (که تو ایران ساختید) خروجی (Export) بگیرید.
2️⃣
وارد پنل سرور خارج بشید و برید به بخش Outbounds.
3️⃣
یه Outbound جدید بسازید و لینک ایران رو اونجا Paste کنید.
(دقت کنید که دامنه‌تون باید پشت CDN باشه و به آی‌پی سرور ایران اشاره کنه).
مرحله ۴: تنظیم Reverse روی سرور خارج
🌍
1️⃣
تو پنل خارج برید به بخش Reverse.
2️⃣
یه Bridge بسازید:
• Tag: bridge
• Domain: دقیقاً همون دامین/اسمی که تو سرور ایران گذاشتید.
• Interconnection: همون Outboundی که تو مرحله قبل ساختید.
• Internet: روی direct یا freedom تنظیم کنید.
3️⃣
سیو کنید و تمام!
✅
نتیجه چی می‌شه؟
سرور خارج به ایران متصل می‌شه ➔ تونل ریورس برقرار می‌شه ➔ کاربر به سرور ایران وصل می‌شه و اینترنت آزاد رو از سرور خارج دریافت می‌کنه!
💡
نکات طلایی و عیب‌یابی:
🔹
مسیرها (Path): پث‌ها (مثل tunnel/ و user/) باید مو به مو یکی باشن. یه اسلش (/) اضافه یا کم، کل کار رو خراب می‌کنه.
🔹
نقش CDN: بدون CDN این روش یا کار نمی‌کنه یا شدیداً ناپایداره. حتماً پشت CDN باشید و تیک WebSocket رو هم تو تنظیمات CDN روشن کنید.
🔹
نیاز به TLS یا Nginx: استفاده از Nginx الزامی نیست ولی برای تمیزیِ کار، روت کردن پث‌ها و استفاده از پورت 443 خیلی جوابه. TLS هم بستگی به شبکه داره، بعضی جاها فقط با 443 جواب می‌ده.
🔹
مشکل وصل شدن بدون اینترنت: اگه وصل شدید، چند کیلوبایت سند و ریسیو داشتید ولی اینترنت نبود، شک نکنید مشکل از ایناست: اشتباه بودن Path، مشکل تو هدرهای Upgrade/Connection، مپ نشدن درست Reverse یا گیر دادنِ CDN.
📌
#آموزش
#تونل
#ریورس
#Reverse_Tunnel
#سنایی
#3x_ui
#vless
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/4770" target="_blank">📅 11:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4769">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سایت ارسال کانفیگ
http://m.ulni.ir
https://sphost.theazizi.ir/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/4769" target="_blank">📅 09:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4768">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آپلودر های فعال
https://up.zaringo.sbs/
https://rozup.ir/
https://uploadgirl.ir/
https://seup.shop/
http://uplod.ir
https://up.20script.ir
https://punkpaste.ir
https://my.files.ir
https://toolschi.com/tools/upload-center
http://nixfile.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/4768" target="_blank">📅 09:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4767">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ربات کاهش حجم ویدئو رایگان
@mediaEasyBot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/4767" target="_blank">📅 09:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4765">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کاش زودتر آیفون ۱۸ بیاد که آیفون ۱۷ ارزون‌ تر بشه بتونیم تن ماهی بخریم.
@archivetell</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/4765" target="_blank">📅 00:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4764">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">IR NETLIFY V10.2 • BACHELOR EDITION
⚡️
تغییرات اصلی نسبت به نسخه‌های قبلی: ۳ تب کامل و حرفه‌ای:
⚡️
Generator — با پشتیبانی از چندین دامنه نتلیفای (داینامیک)
🔄
Replacer — جایگزینی دامنه با قابلیت توزیع خودکار بین چند دامنه
🔧
Tools — ابزارهای پیشرفته (Rename…</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/archivetell/4764" target="_blank">📅 00:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4763">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👾
لیست دانلود برنامه ها با نت ملی
1️⃣
WhiteDNS
1.1.0
(نسخه ی رسمی)
4️⃣
NekoBox v8a
●
NekoBox v7a
1.4.2
7️⃣
The Feed
0.17.5
📱
Telegram
(گوگل پلی)
12.7.2
📱
Telegram
(رسمی)
12.7.2
📱
Telegram
(Windows)
12.7.2
📱
Whatsapp
2‌.26‌.17.‌72
💬
Instagram
v415.0.0.36.76
👑
ShiroKhorshid
2026.03.17
5️⃣
Mhrv Rs
v1.9.14
📶
Npv
123
📶
V2box
5.3.4
📶
V2ray Ng
2.18
📶
V2ray Ng
(Windows)
3️⃣
Am tunnle
(pro)
37
3️⃣
Am tunnle
(lite)
🕊
Slipnet
2.5.3
2️⃣
Masterdns
1.0.9
📶
Open vpn
3.71
📱
Happ
3.20.4
💻
Happ
(Windows)
📶
Psiphon
462
📶
Psiphon
(Windows)
8️⃣
Bd net
104
6️⃣
Mahsang
15
📶
http injector
6.5.0
📶
Wireguard
1.0.20260315</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/4763" target="_blank">📅 23:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4761">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtW_bVZnqqReSGjLNyP2pPJn-IgcI4FZij0vab3D_mX_PQHS6toJwvQWUvbbboIPRWESV4nAdhXop3NiXv54aGi8YhT810wt-xMGtIUAjpgfKXa3LMlWn7WSWpVYvybAIMoQ-VdxybDnTyTVEX0Qj02MzodWPuSraLv7QvYXAB0l16pwD0g4_vaKSoRWLfk97660KQL2yaoBFgfukZi6u4vmIC2mm-Wdj2axGquMYrTFf0-ZyOvKqRg1TyhRjkFUewkK8lUBVOLbg0uc96Glv--4DibtVGJ1IZIiNnO8FINWm_O8DYClxCHEJEbjYmysK4SxO83669h_yndsOEfc2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌍
بومی‌سازی هوش مصنوعی برای توسعه‌دهندگان.
ترجمه YAML، JSON، TXT و محتوای چندزبانه با حفظ ساختار، جایگزین‌ها، متغیرها و قالب‌بندی.
@LocalynBot
⭐
کد منبع گیت هاب
https://github.com/LocalynAI/LocalynAI
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/4761" target="_blank">📅 22:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4760">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">YT_dL.ipynb</div>
  <div class="tg-doc-extra">22.5 KB</div>
</div>
<a href="https://t.me/archivetell/4760" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/4760" target="_blank">📅 21:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4759">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚀
دانلودر حرفه‌ای و پرسرعت یوتیوب مستقیم به گوگل درایو! (بدون مصرف حجم اینترنت)
خسته شدید از سایت‌های پر از تبلیغ، قطعی‌های مکرر و محدودیت سرعت برای دانلود از یوتیوب؟
ما یک اسکریپت اختصاصی و هوشمند برای محیط Google Colab آماده کردیم که به شما اجازه میده ویدیوها، فایل‌های صوتی و حتی پلی‌لیست‌های کامل یوتیوب رو با بالاترین کیفیت ممکن (تا 4K) دانلود کنید.
💡
هدف و مزیت اصلی این اسکریپت چیست؟
تمام فرآیند دانلود توسط سرورهای قدرتمند گوگل انجام میشه. این یعنی شما می‌تونید ویدیوهای چند گیگابایتی رو در چند ثانیه دانلود کنید، بدون اینکه حتی یک مگابایت از حجم اینترنت گوشی یا سیستم شما کم بشه!
🛠
چطور از این ابزار استفاده کنیم؟ (بدون نیاز به کدنویسی)
استفاده از این اسکریپت به شدت ساده است و دارای یک رابط کاربری (فرم گرافیکی) است:
1️⃣
اسکریپت را در گوگل کولب باز کنید (فقط به یک اکانت جیمیل نیاز دارید).
2️⃣
در فرمی که می‌بینید، لینک یوتیوب رو پیست کنید.
3️⃣
کیفیت ویدیو (مثلا 1080p) یا فرمت صوتی (مثلا MP3) رو از منوی کشویی انتخاب کنید.
4️⃣
دکمه اجرا (Play
▶️
) رو بزنید و تمام! اسکریپت به صورت خودکار ابزارهای لازم رو نصب کرده و دانلود رو شروع می‌کنه.
📁
فایل‌های دانلود شده کجا ذخیره میشن؟
در تنظیمات فرم، گزینه‌ای برای اتصال به گوگل درایو وجود داره. اسکریپت به صورت خودکار به درایو شما متصل میشه و فایل‌ها رو در پوشه‌ای به نام YouTube_Downloads (یا هر اسمی که خودتون در فرم بنویسید) ذخیره می‌کنه. بعد از اتمام کار، کافیه برنامه Google Drive رو باز کنید تا فایلتون رو اونجا ببینید!
🔗
لینک ورود به اسکریپت:
[لینک گوگل کولب خود را اینجا قرار دهید]
👇
اگر سوالی در مورد نحوه استفاده داشتید توی کامنت‌ها بپرسید.
Developer : Samad.R
@ArchiveTell
‌
#یوتیوب
#دانلودر
#گوگل_کولب
#ترفند_آموزشی
#ابزار_کاربردی
#دانلود_از_یوتیوب</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/4759" target="_blank">📅 21:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4756">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c7bc1a6d.mp4?token=V7nRmsA4PL3ynyebdTO2_KgWigLdG0Mn8uLiFNVRSr_YAResow6Jz1Wi4nwCjeJHhTisYIUaN3qQ7JT-sQUPEgvviMAd-j5mvfwLV_uOeoVLGLITdv2Cgl9LZaUGtcjEtFyZfGrIO310ORnVaBPv0MW4kYCYp4ZaqT6cSl1sFnOyYVq8Ua6JFpmyjJjHiR5rjGSs91bFMywVbLLozKThVnqVmp6Xl7TN-KRZGBK6P-x_MC8O_DkxBLG1AHlzKkh89NRZ7T9bdl_IotsdcBUm7he5Yt5-depr-EUHFLys4-mu_fc2VWqMt4UaFyjSdtoHWKog-nAjyCHudt33mh8CbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c7bc1a6d.mp4?token=V7nRmsA4PL3ynyebdTO2_KgWigLdG0Mn8uLiFNVRSr_YAResow6Jz1Wi4nwCjeJHhTisYIUaN3qQ7JT-sQUPEgvviMAd-j5mvfwLV_uOeoVLGLITdv2Cgl9LZaUGtcjEtFyZfGrIO310ORnVaBPv0MW4kYCYp4ZaqT6cSl1sFnOyYVq8Ua6JFpmyjJjHiR5rjGSs91bFMywVbLLozKThVnqVmp6Xl7TN-KRZGBK6P-x_MC8O_DkxBLG1AHlzKkh89NRZ7T9bdl_IotsdcBUm7he5Yt5-depr-EUHFLys4-mu_fc2VWqMt4UaFyjSdtoHWKog-nAjyCHudt33mh8CbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
گوگل در حال آزمایش Gemini Omni
✅
قابلیت تولید ویدئو – جایگزینی مدل‌های Veo با یک خط تولید یکپارچه.
✅
همزمان خروجی صدا و تصویر – ترکیب چندرسانه‌ای پیشرفته.
✅
معرفی رسمی – انتظار می‌رود در Google I/O هفته آینده به‌صورت کامل اعلام شود.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/4756" target="_blank">📅 19:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4755">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Telegram-X-0.28.3.1785-arm64-v8a.apk</div>
  <div class="tg-doc-extra">56.6 MB</div>
</div>
<a href="https://t.me/archivetell/4755" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لینک داخلی Telegram x
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/4755" target="_blank">📅 18:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4754">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPYDDhsuPxDVr_hvLk1Qt7XyvHXlNanQalfPncYDGQ_hhXUMfYzx_rlMhN5ERvajbMfjaTNfNe2JCG2J_OkP3xnGonZFoWZcbtcGJJaUr6NtSLvBgs-spH1q_zSzAKlOnJBnwXR9dXvkZL2b0VMMvguLb6ypXaF2-jOhkKYO6V_ED7i27zRE2TpUXMKBUGClKTIFc7wrppw5F84T_jgHDgc9MjVJeyq5jTSf6YrTg4i69JxHzyBJEhFugLh6_H5-ea2KKV7luRrlmXi--XKM8rcdfVg_Ki8t0a4iahCYg3AkRk1GaQ89DZjR0C39hHFA-P9n9FHh0ByAFgjlQxl73w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
ویژگی‌های کلیدی در آپدیت جدید
🛰
امکان اسکن با DNS شکن
(نسخه آزمایشی، ممکنه کار نکنه)
⚙️
کنترل دستی پردازش‌ها (Thread Control):
قابلیت تنظیم تعداد تردها توسط کاربر برای جلوگیری از کرش کردن (خطای Signal 9) در ترموکس اندروید.
💻
نمایش زنده در ترمینال:
نمایش آنی کانفیگ‌های متصل در صفحه ترمینال، علاوه بر ذخیره در فایل.
🛡
عبور از فیلترینگ هوشمند (DPI):
تست واقعی لایه اپلیکیشن (HTTP Status) برای جلوگیری از دریافت پینگ‌های فیک و دراپ شدن پکت‌ها.
🌐
دیتابیس داخلی غنی:
شامل بیش از ۷۰ دامنه CNCF/Cloud-Native و بیش از ۱۰۰ آی‌پی‌ تمیز CDN (بدون نیاز به فایل‌های متنی جداگانه).
https://github.com/johncarterjourney-rgb/NETLIFY-SCANNER</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/archivetell/4754" target="_blank">📅 18:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4753">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تا ۱۰ روز دیگه جنگ میشه..</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/archivetell/4753" target="_blank">📅 17:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4752">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Telegram.apk</div>
  <div class="tg-doc-extra">77.9 MB</div>
</div>
<a href="https://t.me/archivetell/4752" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لینک داخلی Telegram 12.7.2
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/archivetell/4752" target="_blank">📅 17:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4751">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یکم زمانبره. لیست ایپی ها و sni ها افزایش پیدا کرده و تستش هم دقیق هستش. برا همین طول میکشه. ببرین تو کلاینت Exclave یا V2ray همشون پینگ میده.</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/4751" target="_blank">📅 16:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4750">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbpqXrI5xjhhczciguUP2NaBSMUZND4XSJeKOCKqcxCd9OEXzK6OUI4z6grcvyX0jITbpIDnC1xHmjrtjOzfBYLB16AvlelZNGYptYvZ_0sKpGsHggHrCDvb14FoTYeyXjOZ3r-njLBmG_EmwGmwvOmxbdQa0_Bw0dtSPv73W69dljQV09UTyqCMZgEKCwHy0EUHYdflNLDw3JNUDVFJ7FGynPtTkIVyNaEL4FIyN0rJsZ0J8fENbMg0I_ogSEcgrLb_mVKTGB8FtjB9pfTM5ONEh060yc9Qs_LkGUeng7tvVlqIAXVrYN0ASlVgyR7oc5Q2EYjKyILA5Wy6LS2-0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ابزار NETLIFY-SCANNER (نسخه V1 Pro)
🔆
اسکنر IP و SNI های نتلیفای  ---  رفقا سلام.
✋
اگر با کانفیگ‌های نتلیفای کار کرده باشید، می‌دونید که خیلی وقت‌ها پینگ دارن ولی عملاً وصل نمی‌شن (پینگ فیک). این اسکنر پایتونی رو برای حل همین مشکل آماده کردیم.  تفاوت اصلی…</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/4750" target="_blank">📅 15:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4749">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_eYGSSAwoz-tclTwFs0OUYphsBmb_sS67UzZkrxb3u3mrH8r3xBmAToquAj370mUzQMXneGOLtysiuENGyKbix2VAEBPbviGEoxvbbBiBXjrnvtZSlmz-DpsEnVpqTLg7D6UzEqVcL--DzxGltvu8tNWAJujzNV9Tfm5C45ADABqMqltKa1OLkVSzTNGErytl22KBbO6PkZWmHipvYJkBCI2HDzEhQyd46tgtdG9jTO_D2eqwgPmqR7DnotQACdM7UzQaxrmIVqpIzJkoSXDxQEzGVXP-J9-qxiOQ9J4cZ8A6yq4iuQPPUQzoeXVOt3nwLHV_4qwkOqEPx6VfUMjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔆
اسکنر IP و SNI های نتلیفای
📌
github.com/IR-NETLIFY/NETLIFY-SCANNER
🔺
مواردی که ok میشن بدون نیاز به شکن وصل میشن براتون
🔸
دی ان اس شکن رو کامل حذف کنید از سیستم
🔹
یک بار مودم یا نت رو خاموش روشن کنید تا آیپیتون عوض شه
🔸
بدون هیچ DNS و فیلترشکنی اسکنر…</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/archivetell/4749" target="_blank">📅 15:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4748">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-mqJ4fJIBpweJqKsvSiT6FHSP6OHX4ks1MXnl1UImcisduGz24Zvr3UdxWKGt1BsGwYtI9VI46VxJCq8qUa7WyE-Ykq3sPbc7sx-fw4xgV0KHCpkRtmKOuLTcS-KWUwNzN-ic05VJjZMykZ-_HjCkZRBznywQG_BP03lTRF6-FoDPa48nrxHZLYyRcFEoRoGfRj8s3BJuk7rPXVlQQ8t2zBA_PMfjvYoqFEi41ix-C266us-UnS7eCH2Dim0qTy4Fr2mgGlq07KpfXtcyPXg9MfaCB21r98IqLHhBHWx2vN6J-9XILDcLgEsfcr7wv666nHiWPxQJjF_XkxJDOA-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔆
سایت و برنامه کانفیگ ساز آپدیت شدند
📌
فایل برنامه
📌
لینک سایت
🌐
قابلیت انتخاب چند سرور
🔺
اضافه شدن شمارنده تعداد کانفیگ های ساخته شده
⚡️
اضافه شدن بررسی کننده لینک نتلیفای
●  کانفیگ ساز جدید فقط روی
نسخه 1.0.3 پروژه
کار میکنه
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/4748" target="_blank">📅 13:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4746">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⛈
کانفیگ اختصاصی StormDns  قطع شده
1️⃣
در قسمت Profiles ، گزینه import رو بزنید و کانفیگ رو اد کنید
2️⃣
در تب connect بخش Resolvers ریزالور هارو اد کنید و کانکت رو بزنید(1 تا 10 دقیقه زمان میبره وصل شه)
⭐️
لینک دانلود برنامه مورد نیاز
📱
لینک ریزالور ها
⭐
مناسب…</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/4746" target="_blank">📅 12:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4745">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">install_3x_ui.sh</div>
  <div class="tg-doc-extra">22 KB</div>
</div>
<a href="https://t.me/archivetell/4745" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این اسکریپت نصب آفلاین پنل ثنایی هست.
برای افرادی که اعتقاد به بکدور دارن و به میرور ها اعتماد ندارن.
فقط کافیه که توی بخش Releases یک نسخه انتخاب کنید و متناسب با CPU سرور یک نسخه دانلود کنید. و انتقال بدید به سرور.
در نهایت این bash اسکریپت رو اجرا کنید.
bash install_3x_ui.sh
به شکل اوتوماتیک بدون ssl نصب می شه.
فقط بعد نصب با دستور x-ui پورت و یوزر پسورد تغییر بدید.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/4745" target="_blank">📅 11:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4743">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLs6fCx6CwG44MFhRr4fbfp8cwGz1at19sy9xzAxaR3GFIbtPaoMFASgfFFOqJhV2NSkN5tAuLyyiPz5fPlP8TYZ-qyV6buWVMI5tGFcgbv3hmN4Rxdl6CVY8cEVFjWk6yrJVESVKU2jLHpxjaVxhPqpuOwcp5pqr61tmk9oj_acMYdleNC0HJ4sF2rJzHs-7BBqHIcCVaDSSymtOTwqt-10hQ8jC5ve_1FI8kJIwwjfDjpCKf-9EJGR6ovuCD_KvfNvUeqJkJWnkI0KivsKsw8KoUS44Vt0c5RoLQO467pQmcf_8Do7hZm02_kcMmrewUaPUoxxlpoOfeKp7xy5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۳ ابزار هوش مصنوعی که ارزش ذخیره در گنجینه شما را دارند
💎
1.
Claude.ai
— حل مسائل
2.
PicWish.com
— حذف پس‌زمینه‌ها
3.
Perplexity.ai
— تحقیق درباره هر موضوعی
4.
Suno.ai
— ساخت موسیقی
5.
Canva.com
— طراحی گرافیک
6.
ElevenLabs.io
— کپی صدای افراد
7.
Grammarly.com
— اصلاح نوشتار
8.
Luma.ai
— ساخت ویدیو
9.
RecCloud.com
— خلاصه‌سازی یوتیوب
10.
Runway.ml
— ویرایش ویدیو
11.
Descript.com
— ویرایش پادکست
12.
Syllaby.io
— ویدیوهای بدون چهره
13.
Skysnail.io
— تصاویر کوچک ویروسی
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/4743" target="_blank">📅 10:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4742">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚀
نسخه کاملا آفلاین 3X-UI (ورژن ۳)
فقط این چند دستور رو به ترتیب اجرا کن
-  دانلود فایل نصب با نت ملی
wget https://boto3.s3.ir-thr-at1.arvanstorage.ir/3x-ui-3.0.tar.gz
-  استخراج فایل‌ها
tar -xzvf 3x-ui-3.0.tar.gz
- دادن دسترسی اجرا
chmod +x install.sh
- نصب یا آپدیت پنل
./install.sh
📌
نکته:
این نسخه کاملاً آفلاین نصب میشه و نیازی به GitHub یا دانلود فایل اضافه نداره.</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/4742" target="_blank">📅 10:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4741">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سایتی جایی که دامنه رایگان (هرچی) بده بفرستید</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/4741" target="_blank">📅 10:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4740">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مجموعه‌ای از برنامه‌های کار راه بنداز آزمایشی!
سلف‌هاست شده، به رایگان، برای همه.
https://hxlab.ir/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/4740" target="_blank">📅 08:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4739">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5qIyNMJSoP5BHxKGDaBlxa0l-EA0Dz8oDiLR_36ug-vY54ThnJYrujfrTK4vUjHtZtmQ7JKrwYAccxVcwnafyYTpNWeBFsziqX_endAhAuEAZ5Nn-WJk4KWvdlB49lN0ImKAUOw7VtOIDG__Io9sphaqj1e5vazE2b2bwRFT-sYL3Vr1uA7KtroeOMV6BVWeSkBtoAcBRV1l_IGXvJojzhyCtx6GNeoHJRgkLIB-rj0cNNJ0WYYaK6pqNQyvr_vzARtgXTsa9lsvB1SoJU3773zQknELg8JzkDY-UcRcCA58gBJo-xeG4eBaWEafPOhp1UPvmFZrpbuUYQ_KCnRLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔆
اسکنر IP و SNI های نتلیفای
📌
github.com/IR-NETLIFY/NETLIFY-SCANNER
🔺
مواردی که ok میشن بدون نیاز به شکن وصل میشن براتون
🔸
دی ان اس شکن رو کامل حذف کنید از سیستم
🔹
یک بار مودم یا نت رو خاموش روشن کنید تا آیپیتون عوض شه
🔸
بدون هیچ DNS و فیلترشکنی اسکنر رو ران کنید
🔺
می تونید کد رو روی سرور ایرانتون ران کنید اگه چیزی پیدا کرد تونل نتلیفای بزنید به خارجتون وصل شید (
یه کانفیگم بدید دایرکت
)
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/4739" target="_blank">📅 02:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4736">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ultra_downloader_pro.html</div>
  <div class="tg-doc-extra">34.5 KB</div>
</div>
<a href="https://t.me/archivetell/4736" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Untitled 1.mkv</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/4736" target="_blank">📅 02:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4734">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فکر کن عراقی که سنگشو به سینه میزنی تلگرامش رفع فیلتره
افغانستانی که مسخرشون میکنیم برای اومدن به ایران 5g اوکی کردن
سوریه ای که میگیم آدم برای دشمنشم نخواد پرداخت با مسترکارت اوکی کرده
اونوقت ایرانی خوشحال میشه که گیگی ۱۸۰ رو خریده ۱۳۰....</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/archivetell/4734" target="_blank">📅 23:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4733">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">میگم شمام دیگه خسته شدید؟
😕
@archivetell</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/4733" target="_blank">📅 22:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4731">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XPfG29f2g7abnyU0TLG7Rga5NhrdvznzMFbi_bKnePkE6hiiwb13qPWphaYc4aNyxvHb62e0zloukITpLQAf5y0N9B-vtUJt_jwonOhNjZOlF34Xx2D_zZncocJ5QP0bzZCFyWxrPl2bNBJrnnukqUljAhc3Xtd-xojHVuIjkFlz3LOM357VgYcM19oTWJ79isuBYY4gB6T0wwPxjPjvHxQ4TZ3rnXtijQgqRgh25ac79jS2QG23vEiz-BrRCMDXU-57JYyh4-c9xSxKgPhPmBuBrPPFA3CsLWsjPUVPRjOOTG1I8rYbKloYrE5-Q_rLBrvHW8PLfvAmblt7oRvlyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jxaqRbuvHfZFFSZYkNFOmS8p5_p94jkrLkUl3IxVSEAT6VbAuk-p8klGY9MyH903O2q88MiK59wbQONCPxY1qsYS-Zbb3zDJWyA7RmfVlxPhjDWwxx-HQAzm8h98blzMh15vhl9sHNe0MNMlRgUgo-_y46_fBpnHxWdVAq2h0iMG7cpWalsp0bHcimj5cNH39umLGj3-1uxsA0yZeZeSa5PT7vgVK1Re59AuSB5Nc99AYlg0LCwPfAqG0fC_goUCGBFLHA6dXVcKFV7KspVPqU9UUSVwKRZCBMxVZZnrlKUNvTjXqbXVbnOkBXCjhN0nUa2utOEPMbwrFhwYQCCbrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⛈
کانفیگ اختصاصی StormDns  قطع شده
1️⃣
در قسمت Profiles ، گزینه import رو بزنید و کانفیگ رو اد کنید
2️⃣
در تب connect بخش Resolvers ریزالور هارو اد کنید و کانکت رو بزنید(1 تا 10 دقیقه زمان میبره وصل شه)
⭐️
لینک دانلود برنامه مورد نیاز
📱
لینک ریزالور ها
⭐
مناسب…</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/4731" target="_blank">📅 22:29 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4730">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">client_resolvers.txt</div>
  <div class="tg-doc-extra">9.7 KB</div>
</div>
<a href="https://t.me/archivetell/4730" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⛈
کانفیگ اختصاصی StormDns  قطع شده
1️⃣
در قسمت Profiles ، گزینه import رو بزنید و کانفیگ رو اد کنید
2️⃣
در تب connect بخش Resolvers ریزالور هارو اد کنید و کانکت رو بزنید(1 تا 10 دقیقه زمان میبره وصل شه)
⭐️
لینک دانلود برنامه مورد نیاز
📱
لینک ریزالور ها
⭐
مناسب…</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/archivetell/4730" target="_blank">📅 22:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4729">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⛈
کانفیگ اختصاصی StormDns
قطع شده
1️⃣
در قسمت Profiles ، گزینه import رو بزنید و کانفیگ رو اد کنید
2️⃣
در تب connect بخش Resolvers ریزالور هارو اد کنید و کانکت رو بزنید(1 تا 10 دقیقه زمان میبره وصل شه)
⭐️
لینک دانلود برنامه مورد نیاز
📱
لینک ریزالور ها
⭐
مناسب برای
🌐
وب‌گردی،
📱
تلگرام،
📱
هوش مصنوعی و ...
(بدرد اینستاگرام، یوتیوب، دانلود فایل‌های حجیم و کارهایی که نیاز به پینگ پایین دارن نمیخوره)
✔️
اگر برای خودتون و دوستاتون  نیاز به سرور کامل دارید، سرورهای StormDNS به همراه پنل مدیریت در اختیارتون قرار میگیره. کاملاً مستقل و شخصی
برای خرید سرور شخصی پیام بدین:
🚀
@Mo3inh</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/4729" target="_blank">📅 22:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4728">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جایگزین گوگل میت
https://meet.theazizi.ir
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/archivetell/4728" target="_blank">📅 21:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4727">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ربات سرچ عکس در Google , Bing , Yandex و TinEye
@ImageEyeBot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/archivetell/4727" target="_blank">📅 21:18 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4726">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فشرده‌ساز رایگان ویدیو و صدا برای کاهش مصرف اینترنت
📉
📶
@Compreseebot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/archivetell/4726" target="_blank">📅 21:09 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4725">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NecioQerrp2j6UxnsJVOKzX0ZzAPkZdgSW-M0jwtmI7jtCxiSHh-KtVtPQBo0MRAagI9QSPixiJkq0qNvSRMkEMQy_Ip59rNS_fhwUBJeD5FwTCuJQ7ij2uzY6xY4B6JdNe5EvEwvo0hdcU4iDGB9Kx6-o-oCfQBFL5S8n6EDsRsarK6jIWpl-Lmpgk4XShWTrWYE3Ovg9Uzsm6kYTWrM9c1JdDLGrIu7MkP_EoAlvjcaRW4CBBAXBSyzbKpsmNx2_vrtKLTfAhjkLHdIs-bKabLgtEILV569Fp6Jw7bNnRLX49CDfR1anwhlLmx7SphHfYwlnNMWraRio5V5XZMtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامپیوتر شخصی
عامل هوش مصنوعی مستقل از Perplexity برای macOS - تعامل با فایل‌ها، برنامه‌ها و اینترنت.
https://www.perplexity.ai/personal-computer
• کار با فایل‌های محلی و برنامه‌های بومی مک
• ادغام با ابزارهای وب از طریق مرورگر Perplexity Comet
• استفاده از بیش از ۴۰۰ اتصال‌دهنده برای هماهنگی ابزارها و فایل‌ها
• در نظر گرفتن زمینه شخصی کاربر
• پردازش داده‌ها در سرورهای Perplexity
• اجرای وظایف به صورت از راه دور با آیفون
• مقایسه فایل‌ها از برنامه‌های مختلف، انتقال یادداشت‌ها
دسترسی از طریق اشتراک Pro یا Max، در Mac App Store موجود نیست — از سایت Perplexity دانلود می‌شود. کلاینت قدیمی به زودی منسوخ خواهد شد.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/4725" target="_blank">📅 20:54 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4724">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2jmBsnc5t20y-zTA4TckqSmNtty_t7sA43MSrsopBXFrTUTSmr3E7aLFrU2U_U38_CCqNDhjtn9OT17G-4LZfmtyoMIn9dNiCcFHbCPIJgvyTkCyTrMJXGpVQDMvoObPp627eCg5jZTKmGE8h6QZeZSBRuWVv9OdRKTQ0RJBUpDzHUacAf5mxfcRCMwdsri5TFZmkwIe1brz9QaBkrZvZB0LUeJ78RtzLaPCBSakf2UzGlZng2JT04ViULxdxhyJUHzviO1WhL2STec36hJa42zRSuEQhcvkrV0cCi0iNfHm7-V53QoPUTyzNTRmD1IGZ1Lv3G0WUBxa-rhPufniA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادمین گل خیلی دیر پاک کردی پیامتو
😂
چون پاک کردی گذاشتم وگرنه مهم نبود واسم</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/4724" target="_blank">📅 18:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4722">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚀
دانلود مستقیم فایل‌های فیلتر شده با سرعت نور (بدون نیاز به VPN!)
---
رفقا سلام!
✋
خسته شدید از اینکه برای یه دانلود ساده از سایت‌های فیلتر شده باید فیلترشکن روشن کنید و سرعتتون نصف بشه؟
امروز یه ابزار پایتونی به‌شدت خفن و خلاقانه براتون پیدا کردیم که دقیقاً برای دور زدن «نت ملی» و فیلترینگ شدید ساخته شده!
🔥
این ابزار چطور کار می‌کنه؟
شما لینک دانلود رو به برنامه می‌دید؛ برنامه به جای اینکه با اینترنت شما دانلود رو شروع کنه، به سرورهای قدرتمند گیت‌هاب دستور می‌ده فایل رو تو خارج از کشور دانلود کنن و بریزن تو اکانت گیت‌هاب شما!
بعدش شما فایل رو مستقیماً از سرورهای گیت‌هاب (که تو ایران فیلتر نیست) با سرعتِ نت داخلی و بدون نیاز به فیلترشکن دانلود می‌کنید!
🤯
🛠
آموزش
راه‌اندازی قدم‌به‌قدم:
1️⃣
ساخت کپی (Fork):
اول وارد لینک پروژه (در پایین پست) بشید و دکمه Fork رو بزنید تا یه کپی ازش تو اکانت گیت‌هاب خودتون ساخته بشه.
2️⃣
گرفتن توکن گیت‌هاب:
تو اکانت گیت‌هابتون برید به مسیر زیر:
Settings ➔ Developer settings ➔ Personal access tokens (classic)
یه توکن جدید بسازید و حتماً تیک دسترسی repo (تیک اول) رو بزنید. توکنی که بهتون می‌ده رو کپی کنید (فقط یک‌بار نشون داده می‌شه).
3️⃣
تنظیمات برنامه:
پروژه‌ای که فورک کردید رو دانلود کنید (یا با git clone یا دانلود فایل زیپ). فایل
main.py
رو با یه ادیتور (مثل نوت‌پد) باز کنید و این ۳ تا خط رو توش پیدا کنید و تغییر بدید:
🔸
REPO_OWNER
= آیدی گیت‌هاب خودتون رو بنویسید.
🔸
GITHUB_TOKEN
= اون توکنی که تو مرحله قبل گرفتید رو اینجا پیست کنید.
🔸
REPO_NAME
= به جای کلمه random، اسم ریپازیتوری خودتون (یعنی
downloader
) رو بنویسید.
فایل رو سیو کنید.
📥
چطور باهاش دانلود کنیم؟
1. اول فایل
req.bat
رو اجرا کنید تا پیش‌نیازها (کتابخونه‌های پایتون) نصب بشن.
2. حالا فایل
run.bat
رو اجرا کنید.
3. لینک دانلودتون رو بهش بدید و اینتر بزنید! برنامه به صورت خودکار فایل رو دانلود می‌کنه، اگه حجمش زیاد باشه پارت‌بندی می‌کنه و در نهایت روی سیستم شما ذخیره می‌کنه.
⚠️
چند تا نکته خیلی مهم:
🔹
ضد فیلترینگ هوشمند: اگر دیدید وسط دانلود سرعت کم شد یا دانلود چند ثانیه متوقف شد، برنامه خراب نیست! این یه ترفند هوشمندانه تو کدهای برنامه‌ست تا سیستم فیلترینگ (DPI) متوجه ترافیک سنگین نشه و سرعتتون رو محدود نکنه.
🔹
یوتیوب: این برنامه لینک مستقیم می‌خواد. برای یوتیوب باید اول لینک رو بدید به ربات‌های تبدیل فایل به لینک (مثل
@file_link_irbot
) و بعد لینک مستقیمش رو بدید به این ابزار.
🔹
امنیت: توکنی که ساختید دسترسی بالایی داره، پس فایل
main.py
رو به هیچ‌کس ندید.
🔗
لینک صفحه اصلی پروژه در گیت‌هاب:
https://github.com/soheilditf5-svg/downloader
📌
#آموزش
#دانلودر
#گیت_هاب
#بدون_فیلتر
#نت_ملی
#پایتون
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/archivetell/4722" target="_blank">📅 16:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4721">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فیلم و سریال بدون سانسور
https://www.sorkhcloud.top/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/archivetell/4721" target="_blank">📅 14:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4720">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">g2ray generator v3.html</div>
  <div class="tg-doc-extra">70.2 KB</div>
</div>
<a href="https://t.me/archivetell/4720" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚙️
g2ray Setup Generator v3.1
یه ابزار رایگان برای ساخت پروکسی شخصی با GitHub Codespaces
بدون سرور، بدون هزینه، بدون پیکربندی دستی فقط چند کلیک — پروکسی آماده‌ست
✅
─────────────────
چی داره؟
🔑
هر بار UUID کاملاً رندوم می‌سازه
📁
۶ فایل آماده برای آپلود در GitHub
📖
آموزش تصویری قدم به قدم برای مبتدیان
🔋
سیستم Keepalive برای جلوگیری از خاموشی خودکار
🔍
راهنمای تست اتصال قبل از وصل شدن
─────────────────
پروتکل:
VLESS + xHTTP + TLS روی Xray-core
بستر:
GitHub Codespaces رایگان — ماهی ۶۰ ساعت واقعی
─────────────────
⚠️
برای هر اکانت GitHub فقط یه Codespace بسازید</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/archivetell/4720" target="_blank">📅 12:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4719">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ربات یوتیوب به لینک داخلی
@downloaddockbot
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/archivetell/4719" target="_blank">📅 11:46 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4718">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رونیو ابزار توسعه دهندگان وب
https://ronio.ir/fa/
اگر توسعه دهنده وب هستید و به ابزار های خاصی برای طراحی نیاز دارید میتوانید از رونیو استفاده کنید که شامل طیف وسعی از ابزار های آنلاین می باشد.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/archivetell/4718" target="_blank">📅 09:15 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4717">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlqdHQ3MJ6GybXEwUa0U7UOFY-lM-UcXJmos58ykv_lXvxz19cxe-wdJVBRIbNMRpUVoyb7gRh8ej96ZK35bjH3mziRpvC3H8cEy0-vo5leOXRfTwps0sGAMbssR6yQoXcPidDeyoohU3bntfK0xJAiDw4E8mg4egcyvpOHHiivC5Sh7dzK0nyhE-hnkgmwey0BicHlFoW-KPLkeh25gbf3nHJgpJwH-Rmd8ixtju617XXZMcMdOzKj8_RTU2B4V2_E4ptKfjiWQCpkkT2krvL-IdjGTrHmXZXEjqmlxeQ6YbZTecY2mp10mF9v-6_FepLZw_EaGODxbm_QmJg0ujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنظیم NTP سرور داخلی برای تنظیم خودکار ساعت و تاریخ
با تنظیم کردن این دو NTP میتوانید در ویندوز و تمامی دستگاه ها و مودم ها و روتر ها قابلیت بروزرسانی خودکار ساعت را بصورت خودکار انجام دهید همچنین اگر میکروتیک استفاده میکنید هم میتوانید از این دو سرور داخلی استفاده کنید.
194.146.239.1
194.225.150.25
ntp.day.ir
ntp.time.ir
@ArchiveTell</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/archivetell/4717" target="_blank">📅 09:09 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4716">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ربات ادیت موزیک
@musiceditor_tgbot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/4716" target="_blank">📅 08:59 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4715">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMarwinVPN🌓</strong></div>
<div class="tg-text">چندین سرور رایگان با متد Netlify بدون نیاز به شکن
🌐
لینک ساب زیر رو کپی کنین:
https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR_NETLIFY_SUB_new.txt
توی برنامه های زیر میتونین بزنین، پینگ بگیرین و استفاده کنین. قطع شد به یه سرور دیگه متصل بشین
• V2rayNG
• MahsaNG
• V2Box
• Happ
• Hiddify
• Streisand
....
منبع:
IR_NETLIFY
🧡
اگه خودتون هم با همین متد کانفیگ درست کردین میتونین به کانالشون اهدا کنین تا توی لینک قرار بگیره و ساب مدت بیشتری زنده بمونه
❤️
🛜
@MarwinVPN</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/4715" target="_blank">📅 07:20 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4714">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اگر کلاس دانشگاه شما در بستر adobe connect برگزار می شود برای دانلود فایل کلاس، آخر آدرس کلاس این متن را اضافه کنید و به جای filename در آن یک اسم انگلیسی دلخواه برای فایل را بنویسید:
output/
filename.zip?download=zip
مثال: اگر آدرس کلاس مجازی شما مانند زیر است:
https://vc4.uni.ir/s14042-23027551-1/?proto=true
آن را به شکل زیر تغییر بدهید:
https://vc4.uni.ir/s14042-23027551-1/output/filename.zip?download=zip
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/archivetell/4714" target="_blank">📅 02:15 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4713">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sL_tnkrWNUi0OwB1uEvmb1IW914DAT2QUsue7dcQmjGzZXuwNU0cWgBEQ6l3mZubsRFLHlSvlxLhIHJKV1VA6hHplpmhfIjboPLoGUHaX4KZD02HNM4l7EC71qGzKEirRGWOYFbKlHQcAHv4aNKIqkcgqLMDq0YhhFGVrGeTB9oUu9Kyc5B7IqFM84isTTidnIKyW68iWhVte2NKUCiWFJFCEwo1emaKXdtVDqZH50-ajbLToe-BGfzQ4V9p47C_YzYpe0rBcwtiy6v05YMB2KDPB_P_YQ1_rx8daLJG9AxHJYTeaVcihX3ymWA31MYZwu48CuohKEWGbuPVdS-wGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
Canva AI – دستیار همه‌کاره برای محتوای تصویری
✅
بهترین برای: تولید، ویرایش و خودکارسازی پست‌های شبکه‌های اجتماعی، ارائه‌ها و مواد بازاریابی
- نیازی به مهارت حرفه‌ای طراحی نیست
- ایجاد طرح‌های سفارشی با چند کلیک
- بهینه‌سازی هوشمند رنگ، فونت و ترکیب‌بندی
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/4713" target="_blank">📅 02:00 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4712">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/archivetell/4712" target="_blank">📅 01:43 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4711">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ربات دستیار هوش مصنوعی میرا
@mira
🔺
تو شرایطی که اینترنت برای خیلی‌ها محدود شده و اکثر کاربران ایرانی فقط به تلگرام دسترسی دارن، وجود چنین ابزاری واقعا کاربردیه و می‌تونه کمک بزرگی باشه.
🔺
می‌تونید Mira رو به گروه‌ یا کانال‌تون اضافه کنید، ازش سوال بپرسید، باهاش چت کنید یا حتی بخشی از مدیریت کانال‌تون رو بهش بسپارید.
🔺
امکانات نسخه رایگانش هم واقعا قابل توجهه، از جمله:
• پشتیبانی کامل از زبان فارسی
• چت بدون محدودیت
• تبدیل ویس به متن و متن به صدا
• جستجو در وب و پیدا کردن اطلاعات
• تحلیل عکس و لینک و توضیح محتوای اون‌ها
و کلی قابلیت دیگه که رایگان در اختیارتونه.
🔺
در نسخه پولی هم امکانات پیشرفته‌تری مثل:
• ساخت و ادیت عکس
• تولید موسیقی و ویدیو
• کدینگ ، کانکت به گیتهاب و...
• اتصال به جیمیل ، گوگل درایو ، گوگل داک و...
در دسترسه.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/archivetell/4711" target="_blank">📅 01:09 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
