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
<img src="https://cdn4.telesco.pe/file/b2snRIKzu8YmXqAiRsWi7sRdNEVJFWE7mu-JQKahc-VLTGDUynGaVXASL8gHuVkRipsxOt1GD0iKC4tu3dWBhwh-yYOdnHrSZptTtLSZl7kv_7U8XPC9gUHOtuEy8TOY1h1jQorYji1_yg2gkF_HTWPcoAqE-fiHhFn8dEfq7bzUejBwVVGMR10MHhEU4a1MkQd6AwtAaYPIgsEMyiTKyJjTuu9qSh2wbMam-HtMSMh93Kn3IC1i2Y77GE5KqMt38xmxjlkJMqiVsOEDmbhf0t58SUI1eGlsAYP4aV8VlTNPVLQCCcICijALOrLWiW43WhgAhi5ps0rdnKTRJOnG2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.59K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 01:35:45</div>
<hr>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
بی رفرال
🤐
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 52 / 140
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 232 · <a href="https://t.me/archivetell/6240" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">https://t.me/ArchiveTellNews/212
🤨
🤔</div>
<div class="tg-footer">👁️ 359 · <a href="https://t.me/archivetell/6239" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 485 · <a href="https://t.me/archivetell/6238" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app
بخونید نظرتونو بگید
@ArchiveTell</div>
<div class="tg-footer">👁️ 738 · <a href="https://t.me/archivetell/6237" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">StormDNS
a.cyntarix.com
25ffbc77bcfb23b2d4ee225eedcd2466
داشته باشید اگه نت قطع شد</div>
<div class="tg-footer">👁️ 778 · <a href="https://t.me/archivetell/6236" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این پروژه پایتونی جالب هم برای تشخیص اشیاء توی ناحیه مشخص شده کاربرد داره مثلا طبق مثال خودش که با QWEN ادغامش کرده یه نفر با هودی اومده توی ناحیه مشخص شده تشخیصش داده و به گوشیش نوتیف فرستاده و گفته چه چیزی با چه اطلاعاتی اومده توی ناحیه.
برای دوربین مداربسته خوبه یه ناحیه رو مشخص میکنی هر چیزی اومد توش بهتون خبر میده،کد اصلیش با پایتون نوشته شده و از ابزارهایی مث ffmpeg برای مدیریت استریم‌های ویدیویی استفاده می‌‌کنه.
github.com/roryclear/clearcam
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/archivetell/6233" target="_blank">📅 00:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 53 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/archivetell/6232" target="_blank">📅 00:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">هر کی 99 تا رفرال داشته باشه ی کانفیگ نپستر میدیم بش
😌
🔥</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/archivetell/6231" target="_blank">📅 00:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 53 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/archivetell/6230" target="_blank">📅 00:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 53 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/archivetell/6229" target="_blank">📅 00:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBexx7pVTGHI8sHSht-Iv3rRi_MGe5G96whqFjDn6z7jz_YrNSYPL3IWnlTltvG7yA6MSvIMtjk6VWcYhNpv70DjqrkIMR7lKLbef6qUz4E42hIGkhtEDuebQsUORBz-XcrCIbOFPi9Ae2LDs4fHgfLwh3dcSBIbXxxzKLaoW--cbt_W6ETjB16BkmgMunwqUKt4us3nXKKTZre35W_H8uqWFGQsSZwv4le3Zh5qSvpXPOPLtvUY054PDEXCgVU1796DFRUIZGWLUvKH6TlsQ4ttM7lpay6NSAm5SJq-XxhskQPkp4U18985rwFtsFfc41qw0dL0fJwczx2FgHORvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Gitdot؛ رقیب متن‌باز GitHub که با Rust ساخته شده
🔹
پروژه Gitdot توجه زیادی جلب کرده و به‌عنوان یک جایگزین مدرن برای GitHub معرفی شده است.
🔹
این پلتفرم از ساخت مخزن، Push/Pull، ریپوهای خصوصی و عمومی و مهاجرت از GitHub پشتیبانی می‌کند.
🔹
رابط کاربری آن با الهام از ابزارهای CLI مانند Vim و fzf طراحی شده و روی سرعت و ناوبری با کیبورد تمرکز دارد.
⚡️
🔹
قابلیت‌هایی مانند Pull Request، Issues و CI هنوز در دست توسعه هستند.
⚠️
با وجود استقبال کاربران، Gitdot هنوز در مراحل اولیه توسعه قرار دارد و فاصله زیادی تا رقابت کامل با GitHub دارد.
🔵
@ArchiveTell
| Bachelor
⚡️
https://gitdot.io/</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/archivetell/6227" target="_blank">📅 23:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🛑
پایان uBlock Origin در Chrome نزدیک است
🔹
گوگل آخرین راه‌های دور زدن محدودیت‌های uBlock Origin را مسدود کرد.
🔹
پشتیبانی از افزونه‌های Manifest V2 به‌طور کامل در حال حذف شدن است.
🔹
فلگ kExtensionManifestV2Disabled نیز از Chromium حذف شده است.
🔹
مرورگر‌ های Edge، Opera و سایر مرورگرهای مبتنی بر Chromium هم این مسیر را دنبال خواهند کرد.
⚠️
نتیجه: نسخه اصلی uBlock Origin به‌تدریج از دسترس کاربران خارج می‌شود و کاربران باید به uBlock Origin Lite مهاجرت کنند.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/archivetell/6226" target="_blank">📅 23:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=CwOzO0GQRxfEgv0S9uUCevfhtnItNr5SEO464sSCWepen1TglvJHsgETjkjzg3FcpaKrMhJOaTyFS5IzhXS3wz1n8M3xAa7RnXfSXQ7ROM_xlU8MOD6wpEo_vPvdxyqRS3K9juN_1Hf1_jm2zf21MxucAnvs5X6P9-wwJTRsaBnDmpbxKSo4YernisDBtAnqqOJ9WXVEOrLNOeByBrWANKu2WLxMFf37eq7eyQZWvWyslKT7L0fvAw7ncD8Y52b9lLzmWjiP0FLJRm_CGZYpjQsdkSQBjrSfCrx0twdTOkiN0zlLM5ZZ5KvJBdgxGt43CtUqAncYYEdp4FDD4Xo_3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=CwOzO0GQRxfEgv0S9uUCevfhtnItNr5SEO464sSCWepen1TglvJHsgETjkjzg3FcpaKrMhJOaTyFS5IzhXS3wz1n8M3xAa7RnXfSXQ7ROM_xlU8MOD6wpEo_vPvdxyqRS3K9juN_1Hf1_jm2zf21MxucAnvs5X6P9-wwJTRsaBnDmpbxKSo4YernisDBtAnqqOJ9WXVEOrLNOeByBrWANKu2WLxMFf37eq7eyQZWvWyslKT7L0fvAw7ncD8Y52b9lLzmWjiP0FLJRm_CGZYpjQsdkSQBjrSfCrx0twdTOkiN0zlLM5ZZ5KvJBdgxGt43CtUqAncYYEdp4FDD4Xo_3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/archivetell/6225" target="_blank">📅 22:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKI5yClL9KqJYP3VYBMcWXgjYl_WET0MqtlC54l8a91vIYENP_c9i-GCBnqFiFmt-R4hQLQqX5crBZIhfIFbZHq9A_jafqlTo4E-BjZku4HjwhX8irHpVgPruCmFhdq_ZNvANVZFfxKYl43SnxeKaoFvXfRicFVPxgF-ZRrvBW5b0KmXPOnNUtppw0VSKgYOu7JfWootIICNLCBtbSHhbHDb-72RKBTVc6VmRNpjqnqzgINohfaDViax6tAWYF0Bd_v7I7QzLisprlqAjWkmCfGjkQysB2iZM63p-lqMU2Vzj5cv9n9Bi-KqGX15K_Y-Co3DHdrohOH8OO_TSH56CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک ویرایشگر ویدیوی کامل که مستقیم داخل مرورگر اجرا می‌شود؛ بدون نیاز به Premiere Pro یا CapCut
🎥
✨
قابلیت‌ها:
•
🔹
پشتیبانی از چندین ترک ویدیو و صدا
•
⚡
رندر سریع با شتاب سخت‌افزاری GPU
•
🛠️
افکت‌ها، ترنزیشن‌ها و ابزارهای تدوین
•
📱
قابل استفاده روی کامپیوتر، تبلت و گوشی
•
🎬
عملکرد پایدار حتی در مرورگر معمولی
🔗
لینک:
https://tooscut.app/
#VideoEditing
#Tools
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/archivetell/6224" target="_blank">📅 22:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">طبق درخواست شما عزیزان
تمامی سرویس هایی که API رایگان هوش مصنوعی در اختیارتون میزارن رو مجدد قرار میدیم
✨
Freemodel.dev
🥇
developers.cloudflare.com
🥈
console.groq.com
🥉
aistudio.google.com
build.nvidia.com
cloud.cerebras.ai
openrouter.ai
console.mistral.ai
llm7.io</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/6223" target="_blank">📅 21:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uP5un1St2b-QCk-gUBExYpmc5Uzl7mMr5-ggDpcjg7XbsfLBluKjbJm01LpN9a62tGiVe-R5ARGl7iM_H03g-PdCJmOT2Q7NLUla4VcYKSxbIe51uhqn2-oT7VLP33vkk4X2_ZuHpivN1tMFHOxC1dMhNZVFN-QbaeJ2Ubot6UzETd9_CtC_jD8Zp7WIqZA9jbt7U7zlXdblYju-NlcU7XCmmMvERmW7F5U3swyGyTyE3D5gy9t7P-9aG1AgsexMLRFG3Ybfs4Yc2Y5Y6rVmd0DKgwc5eDU-mLw611fQiCOXWb2voedHLUUONeeTs7lNzx_0Achi-C5owJvYH7EF8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
کاهش بار اضافی روی حافظه در ویندوز ۱۱ — غیرفعال کردن فعالیت پس‌زمینه Edge
😎
این کار از طریق ویرایشگر رجیستری انجام می‌شود:
1️⃣
کلیدهای Win + R را فشار دهید → regedit. را وارد کنید.
2️⃣
به مسیر زیر بروید:
HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Edge
3️⃣
روی فضای خالی کلیک راست کنید → «ایجاد» → پارامتر DWORD → نام آن را «StartupBoostEnabled» بگذارید و مقدار آن را 0 انتخاب کنید.
4️⃣
کامپیوتر را ریستارت کنید.
پس از این کار، Edge دیگر در پس‌زمینه اجرا نمی‌شود و منابع را مصرف نمی‌کند.
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6222" target="_blank">📅 20:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">walf.zip</div>
  <div class="tg-doc-extra">12.9 MB</div>
</div>
<a href="https://t.me/archivetell/6221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ℹ️
فایل سرچ پروتکل و سرور ویندسکرایب
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6221" target="_blank">📅 19:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚀
برنامه WALF منتشر شد!
اسکنر خودکار سرورهای ویندسکرایب نسخه PC
اگر از عوض کردن دستی سرورها خسته شدی یا دنبال یه راه سریع برای دور زدن فیلترینگ میگردی، این برنامه دقیقا همون چیزیه که نیاز داری.
کار برنامه چیه؟
برنامه WALF کاملا خودکار و بدون اینکه نیاز باشه کاری کنی، تک تک سرورها، شهرها و لوکیشن های ویندسکرایب رو روی پروتکل ها و پورت های مختلف تست میکنه تا بهترین و سریع ترین اتصال رو برات پیدا کنه.
👇
چطور کار میکنه؟ خیلی ساده:
۱. فایل برنامه رو از لینک زیر دانلود کن و از حالت فشرده درش بیار.
۲. فایل walf.exe رو اجرا کن و دکمه Start رو بزن.
۳. تمام! خود برنامه اگر ویندسکرایب بسته باشه بازش میکنه و شروع میکنه به اسکن کردن کل شبکه تا بهترین اتصال رو برات ردیف کنه. (فقط مطمئن باش که قبلا توی ویندسکرایب اکانتت لاگین شده باشه).
لینک دانلود برنامه سرچ خودکار پروتکل پورت و سرور های ویندسکرایب در پست بعدی
⬇️
با تشکر از چنل
@CubicDreams
که زحمت کشیدن ساختن
🙌
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6220" target="_blank">📅 19:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خب یه پست اختصاصی دیگه داریم این فایل رو خیلی جاها میلیونی میفروختن در حالی که رایگان بودش یکم دیگه پابلیک میکنم
🔥</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/archivetell/6219" target="_blank">📅 18:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qys12a-A-gfNP8Js_bA1qI8W2TBr6eiBTJlQvYQp5Qi1PZ8-KuKp-ZB0tm2KyCyUnhIvO63jv8LKjyDN7U-KxYAkEAGGNFtqcRlHUL8AJIvn-y2prYUoTHPTIZ5M-Cz0CfRIE222RmR4IiCYNChmljvfsgWPE9d_LxsQQyNVUks08hs8jG4_37KNm1aIojD2qQgDYXQjdBsO5xpC2vgFlwFNiTFtGmuWPlusdiOI8nU_WU0rBGYBsHV7mV6bXaz1i3pcKG41zV7l3TQOzJ0aIIlwqL_3HARLGnvPpUvvorW9ix0nSKR42nh5qjQOYKsWNXffOkRGjQlzEDVH0SzLEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دریافت API رایگان GPT-5.5 از Freemodel  اگر دنبال دسترسی رایگان به GPT-5.5 هستید، می‌توانید از Freemodel استفاده کنید و API Key اختصاصی دریافت کنید.
👇
📌
مراحل ثبت‌نام:
1️⃣
وارد سایت Freemodel شوید.
2️⃣
با حساب Gmail ثبت‌نام کنید.
3️⃣
پس از ورود، صفحه احراز…</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6218" target="_blank">📅 18:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⚠️
اطلاع رسانی برای افرادی که اشتراک ویندسکرایب پرو خریداری کرده‌اند:
پروتکل
ikev2
روی تمام لوکیشن ها (تقریبا) متصل میشه
✅️
با تست هایی که گرفته شده با فیبرنوری مخابرات  سرعت همه سرور ها دانلود ۲۰۰ مگابیت و اپلود حدود ۵ مگ فعلا قفل هست
(پیش‌بینی میشه پهنای باند ikev2 کم کم محدودیتش برداشته بشه و به قبل شرایط ۱۸ و ۱۹ دی ماه محدودیت شبکه برگرده)
سرعت کانکت شدن به سرور ها و امنیت ، این پروتکل خیلی بهتر از tcp هست حتما استفاده کنید
👌
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6216" target="_blank">📅 18:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ArchiveTel
pinned «
ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/6215" target="_blank">📅 17:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚀
دریافت API رایگان GPT-5.5 از Freemodel
اگر دنبال دسترسی رایگان به GPT-5.5 هستید، می‌توانید از Freemodel استفاده کنید و API Key اختصاصی دریافت کنید.
👇
📌
مراحل ثبت‌نام:
1️⃣
وارد سایت
Freemodel
شوید.
2️⃣
با حساب Gmail ثبت‌نام کنید.
3️⃣
پس از ورود، صفحه احراز هویت نمایش داده می‌شود:
🔹
بخش اول: احراز هویت با شماره تلفن
🔹
بخش دوم: احراز هویت با تلگرام
✅
گزینه احراز هویت با تلگرام را انتخاب کنید.  لینک ربات تلگرام برای شما نمایش داده می‌شود. وارد ربات شوید و استارت را بزنید
🎉
پلن Pro برای شما فعال می‌شود:
هر ۵ ساعت: ۱۰ دلار اعتبار  هر هفته: ۶۶ دلار اعتبار
💰
4️⃣
از منوی سایت وارد بخش API Keys
شوید و یک API Key جدید بسازید.
5️⃣
در بخش Docs می‌توانید مستندات کامل استفاده از API را مطالعه کنید.
🛠
تنظیمات نمونه:
model_provider = "freemodel" model = "gpt-5.5" model_reasoning_effort = "xhigh" disable_response_storage = true preferred_auth_method = "apikey" [model_providers.freemodel] name = "freemodel" base_url = "https://api.freemodel.dev" wire_api = "responses"
🤖
حالا API Key و مشخصات بالا را به هوش مصنوعی موردنظر خود بدهید و از آن بخواهید برایتان کد تولید کند:
✅
JavaScript
✅
HTML
✅
Python
✅
PHP
✅
Node.js
✅
و بسیاری زبان‌های دیگر...
💡
می‌توانید با آن:
🔹
ربات تلگرام بسازید
🔹
وب‌سایت طراحی کنید
🔹
ابزارهای اتوماسیون ایجاد کنید
🔹
پروژه‌های هوش مصنوعی توسعه دهید
🔥
فرصت خوبی برای تست GPT-5.5 بدون پرداخت هزینه است.
@Archivetell
✨</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6214" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
نپستر
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6213" target="_blank">📅 17:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کانفیگ ناب اهدایی
💎
hysteria2://5z15av99psrlhdqp@32.195.51.20:39150?alpn=h3%2Chttp%2F1.1%2Ch2&fm=%7B%22udp%22%3A%5B%7B%22settings%22%3A%7B%22password%22%3A%22dlxmzvxvcp3i6v0e%22%7D%2C%22type%22%3A%22salamander%22%7D%5D%7D&fp=chrome&obfs=salamander&obfs-password=dlxmzvxvcp3i6v0e&security=tls&sni=32.195.51.20#usa_hesteria-%40u2vpn-100.00GB%F0%9F%93%8A
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6212" target="_blank">📅 15:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پروکسی‌های اختصاصی آرشیوتل
😎
⚡️
پروکسی ۱
🚀
پروکسی ۲
💥
پروکسی۳
💡
روی لینک بزنید و گزینه Connect را انتخاب کنید.
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6211" target="_blank">📅 13:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqMsBg0pSILfErBsHqPOh8_zAj2xoC5zDaW80yxEvrj4mnc8z86FVuw62Q5_1nk-vvLlc6p0_pV6iOpSIn4X39kxUgU2eIVAZ8B3kFgFvP6hszfRf_ScvNRE6NCAwZeKC4G7fgkSGby14js9EfmiLD0GthOf7UlvD9Hb0nJO8yWf_oO2WmGXwShq6lFEg4tIBEBZ0YfKHsDfSlCrHV2-GQZStQzS0fxXc1yJbcGnYJ-b7EVXdDr6lS2ej_1zKgioJP30mcbZDRpGtAkx4rCQaWpjUW_EHG0UkpnEhfpecgESH0p8-5xoMBBjSNv8qiOXhfod03VQ9aplFE87xFONXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب یه روش مخصوص ایرانی‌ها اضافه کرده، رو همه اپراتورها عالی کانکت میشه:
Settings → Connection → Anti-Censorship
گزینه Protocol Tweaks رو روی Enable بذارید، بعد وارد Configuration بشید و یکی از دو گزینه آخر که ایران هست رو انتخاب کنید. گزینه Large TLS رو هم روشن کنید.
پروتکل های udp و tcp رو تست کنید
ایرانسل tcp 587 france
مخابرات همراه اول udp 80
با فیک میل اکانت بسازید
https://windscribe.com/signup
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6210" target="_blank">📅 13:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsYlHkwa80Kmsj9jB6nYfotLleDylvWsauAIL7JkN4D5oO2GxIrA3qBBy_MrBA9h10FJC40XOPNvKawzyf83jo8L8JSavcELrbrpaRS2BJw6bLZhK7Pr6p8vMYzGUyU_rmJaIgMpavP56K2jhewNkWqxU0XU5Z0EnyUR9GHRtPiF8B78R6Lbg5uLeMd7CvpboxwRey_weyrHg4plZYFJQc4-QHSEK88IPASPu_kDjp-GR9N1tf_oq0mMe7f3j2Nx3cylz-wdWjz12ON-CLbtcNjcwDHnrFy2QabTCcdn5C63L-CV_PQOUx14cjUhdt8XBpjIhu4vIjiKEhk9ycXD_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
Impeccable
‏این ابزار به عامل های هوش مصنوعی کمک می‌کند تا وب‌سایت‌های منحصربفرد و بدون الگوهای استاندارد ایجاد کند
🔥
‏
✨
قابلیت‌ها:
‏•
🔹
آموزش عامل‌های هوش مصنوعی برای ایجاد طراحی‌های منحصربفرد
‏•
⚡
کار به عنوان منتقد، توسعه‌دهنده front-end و نویسنده UX
‏•
📊
آزمایش ماکت‌ها، برطرف کردن خطاها و بهبود طراحی
‏
‏
🔗
لینک:
https://github.com/pbakaus/impeccable
‏
#هوش_مصنوعی
#طراحی
#OpenSource
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6209" target="_blank">📅 13:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tKpoHgi3mz7G2XwNTRZppXQi99-K-gINzWr4uUEG1Qym00sYRG0JqlzoHS5JfPV8nAsd8hhBYU0hcfJaCc0Ikgbx46mDs7rJaltA-FCZFYB1YxCzMfmakJxtumQajWWtFOLWI3CRs1oQG9mCqEesJsqh8NNhgD9nVETpHP3E9jHot0QFbJnEyFcZKMsHVBvqOmfDa8UP8Po19ZUvtxJH_iSwdvyHmvONXJsbeLz0UOXIGkqO3S8INl9ayCsextf9C887Iqht6VRIWDcmSjtObTwPygJTsGYszkdcvUOQivSsbqwWjBwoMsKQXA6Foz32uETdRaA_jQdhznLUPAnsFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZXGKwDEgbVs7oIQGBDO-_4zccRY7_il77xejzwMxJF69LmW9DzhbSfXigjSKQSCXFsQXGAy6u04X8AcgWkA5OwjGeNgyqmmnozh5YRxu4zxSS-lJ_OkBfH8BORXMtD1Sk392HhD2d5-A0FuN0CCdQHkegNquoXoozx5Fb4o5NtCaj18-9-ZvidNIZ_GQJD4Re9zUTsMdGZZHi1Mlw_RvT3zUYfAIZaW81H4SehgEQz3d8QlRQxs6liwVW5iU-KPAvczVjm1DioGqh9RIett8KPhGzs1CXAlP6qWNA-_UTmi0ZGFWt3EwA1eNYtaCkPnpJctG4XMMIy-GnmisaqYZXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fpInkTRWOlFgOHhGz5Dz7bLQ9uq6rfCKoiMfoo2J-Z9A9dx5VJSitT44-vsHcTqa7LxNKr_w_etNKq1UukAw541jH4UibwTliQadjsWtbwKubVu1MPp70ZFiCiexuPFKdNbpbLDejjfjZctrM7cnz3HjkXnqq8UmtZ1SiS9IuUuivCXqnCicubF2RdPsKoP7bCYEohVopsKUEH1qzUx8w9UwoLhmk0rxBFHiKKHXyDAwC84Bq9GaDEhv5Em7FdsvFj1WPpejURkT4S3APt5sHSiKHr5v6uUts4m32h-3ELcsYlgm9Ax9y-1yO6_qtWU8LfT8rfu3O6XCAYH3Iq2LYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d97888b48f.mp4?token=IyG0a6CQvuiLf3NZo-53cjr_IDyAfUqBfImv5_-WteP7sPk1s0F7_fi69nd3auqGxst9nxILSr49Cu1oxhX8cDsSrXNPZODoRAXnlsKb2V7fUqyMcQ9yua_Rqn_YCdDvuDjue1AiaU_i7anf-cCNq0jvTkyTrTemwZiT9oGErHtuOiJQdPJ62tQEQnVnAFp_A3TfzzW91gIiceocMjOG1hOHoX_lwXAtrvHxLM9V4HHT7IPAHsEbKxetTgbHMf5ds18abdCMV3PZuCRZ0xDfmkeJV_RWhhMw2C7EoTyEb9WW_YN_Cr6bFRkjSkroV-VFg9b-c2-xJGIM431ErPvO-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d97888b48f.mp4?token=IyG0a6CQvuiLf3NZo-53cjr_IDyAfUqBfImv5_-WteP7sPk1s0F7_fi69nd3auqGxst9nxILSr49Cu1oxhX8cDsSrXNPZODoRAXnlsKb2V7fUqyMcQ9yua_Rqn_YCdDvuDjue1AiaU_i7anf-cCNq0jvTkyTrTemwZiT9oGErHtuOiJQdPJ62tQEQnVnAFp_A3TfzzW91gIiceocMjOG1hOHoX_lwXAtrvHxLM9V4HHT7IPAHsEbKxetTgbHMf5ds18abdCMV3PZuCRZ0xDfmkeJV_RWhhMw2C7EoTyEb9WW_YN_Cr6bFRkjSkroV-VFg9b-c2-xJGIM431ErPvO-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
هوش مصنوعی Siri یاد گرفته است که عکس‌ها را مانند Nano Banana Pro ویرایش کند.
✨
قابلیت‌ها:
‏•
🔹
«بازآفرینی فضایی» برای تغییر ترکیب، زاویه و پرسپکتیو عکس‌ها
‏•
📸
ویرایش پیشرفته برای ایجاد عکس‌های خلاقانه
#Apple
#Siri
#Ai
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6205" target="_blank">📅 12:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBdUlyQ_P0VI62VpLxO162j7zO5cuQLpN9vX3H3qTi9ed_GhbLxSfz4gLDmct1ElUvDlZ8poLq-dp6Jq8RXRwpgLrITuUz7-SPX7ILX83UbWM2PFYoE9-yWChkbiWEoF9uhec-ZOmx5wGITh_qmWzvYU3gfUJo0Z9St1gUWCITud5SU3FLcuf8UcaSYIcnDcpUMESuBc2N8dCGcvWK0hSK3owv_n8Wb5OtPMpkpPP5XGMYiHioZGGNwB3yurkvUyTaAYQ0gOImYd-8ZwmHIfQ0AV8EbNYFZfQFlUKPBtUYHfcqXk3cqfyIqEHTu1oofXLKBoTfVvN5BQXM8DmgEajg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
.FrameCoach معرفی شد!
‏این ابزار هوشمند تنظیمات گرافیکی ایده‌آل را برای هر سخت‌افزاری انتخاب می‌کند و حداکثر FPS را استخراج می‌کند
🎮
‏
‏
✨
قابلیت‌ها:
‏•
🔹
انتخاب کارت گرافیک و پردازنده
‏•
⚡
انتخاب بازی از کاتالوگ
‏•
🛠️
دریافت تنظیمات بهینه برای حداکثر FPS یا بهترین گرافیک
‏•
📊
مشاهده تأثیر هر پارامتر بر عملکرد
‏•
📈
تست تنظیمات و پیش‌بینی فریم بر ثانیه
‏
‏
🔗
لینک:
https://theframecoach.com/
‏
#گیمینگ
#بهینه‌سازی
‏
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6204" target="_blank">📅 12:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">با پلتفرم Cerebras به مدل‌های قدرتمند gpt-oss-120b و glm-4.7 با محدودیت بی‌نظیر ۱ میلیون توکن و ۲۴۰۰ درخواست در روز دسترسی پیدا کنید
🚀
شما می‌توانید کلید API خود را دریافت کرده و پروژه‌های هوش مصنوعی‌تان را با سرعت و دقتی فوق‌العاده پیاده‌سازی کنید
🛠️
. این یک موقعیت عالی برای استفاده از مدل‌های سنگین بدون پرداخت هزینه است
💸
، پس آن را از دست ندهید!
✨
cloud.cerebras.ai
🔗</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6203" target="_blank">📅 11:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32629bb6.mp4?token=eIdhtouwiZhiZc4M_t5lReecmhwpTT-MLLlpzN_HWTgCUCTwskPimVT2d_1FDvVL8fPJ7yAmPg9cp4NGsHo57IU5xk-FMDBcgbmQA7y7D0ExaahKitGiQoar8ZwMcPgLncRWLiDkQCPqDDqmHXkRiSoA5FD3tAbNLaY1-BoZ5nZLn0eL_DIWMnOi-GslnCqnQ6ChREL-758embeusgwFqDqa5MR2ZBKjtNbQ0P45ZMlSG9xpyF50m5b_TrUe5w6qcXZx3dc11v_o7dzRk24n5xSCRbTeWBug3TSRc7QDGFL9Waahn9MJQASy9DlChOx12yQ-LnCGp5qa4dsXkPmoCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32629bb6.mp4?token=eIdhtouwiZhiZc4M_t5lReecmhwpTT-MLLlpzN_HWTgCUCTwskPimVT2d_1FDvVL8fPJ7yAmPg9cp4NGsHo57IU5xk-FMDBcgbmQA7y7D0ExaahKitGiQoar8ZwMcPgLncRWLiDkQCPqDDqmHXkRiSoA5FD3tAbNLaY1-BoZ5nZLn0eL_DIWMnOi-GslnCqnQ6ChREL-758embeusgwFqDqa5MR2ZBKjtNbQ0P45ZMlSG9xpyF50m5b_TrUe5w6qcXZx3dc11v_o7dzRk24n5xSCRbTeWBug3TSRc7QDGFL9Waahn9MJQASy9DlChOx12yQ-LnCGp5qa4dsXkPmoCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🤖
چینی‌ها یک هیولای هوش مصنوعی با ارتشی از عوامل عرضه کردند — Kimi Work می‌تواند تا صد دستیار را به طور همزمان روی یک دستگاه اجرا کند.
‏
‏
✨
قابلیت‌ها:
‏* تا ۳۰۰ عامل می‌توانند به طور موازی روی وظایف مختلف کار کنند
‏* مرورگر را تقریباً مانند یک انسان کنترل می‌کند
‏* دسترسی به داده‌های مالی را بدون پیچیدگی در تنظیم API فراهم می‌کند
‏* عادت‌ها، زمینه و اقدامات قبلی را به خاطر می‌سپارد
‏* با فایل‌ها و اسناد محلی کار می‌کند
‏* کد پایتون را اجرا می‌کند و فرآیندهای روتین را خودکار می‌کند
‏* کمک می‌کند برنامه‌ریزی کنید و وظایف بزرگ را تقسیم کنید
‏
🔗
https://www.kimi.com/products/kimi-work
#kimi
#ai
‏
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6202" target="_blank">📅 11:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Telegram.apk</div>
  <div class="tg-doc-extra">78.2 MB</div>
</div>
<a href="https://t.me/archivetell/6201" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">12.8.0 (6913)
Directly downloadable from
telegram.org/android
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6201" target="_blank">📅 11:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsNfotu1AlTekhXyu5qE8E0iMbKnk0W8wF0B9ukAf4QI_bCB_meJlDFi7yS5PGCJcKm257wot_bd5LqhUrlnnxjEMtbuWmzf4GADDVeNE19F8KLIoGeXuZB-Eh6LtqAmN417kBhJPjrx6z0qGtd8wrCg0UIJ1kytMXTCCT2TNiJu3byPKzSHg9UctbSWrkAqJWgPF6h8taj8c3QjYl5usWtKChZrd-72MdZ3XatTpOIqLKQCCUYEidVDQ6TLtMf_vGmYQSOLahEj8cxWWOVOUSlNSJj9k5j_dtOw3CesQ-2clDQZOpsISFFJatg3doSLLoqerG5Qh3jahVJub5NwDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
گوگل NotebookLM را با قابلیت‌های جدید هوش مصنوعی ارتقا داد.
حالا این ابزار از مدل جدید Gemini استفاده می‌کند و می‌تواند فراتر از یادداشت‌برداری عمل کند.
🚀
✨
قابلیت‌ها:
•
🤖
پردازش و تحلیل بهتر اطلاعات با Gemini
•
📊
ساخت نمودار و تحلیل داده‌ها
•
💻
اجرای کد مستقیماً داخل نوت‌بوک
•
📝
تولید اسناد و گزارش‌های مختلف
•
☁️
محیط پردازش ابری اختصاصی برای هر پروژه
🎯
ابزار NotebookLM کم‌کم از یک ابزار یادداشت‌برداری به یک دستیار تحقیق و تحلیل کامل تبدیل می‌شود.
🔗
لینک:
https://notebooklm.google.com
#Google
#Gemini
#AI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6200" target="_blank">📅 10:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee5737315.mp4?token=KpBb8luDy-OGB5Q4jIYxSc7QREOq-wLUGRzFkQC9qZioy5jdviQC42IOAZyNmDmYWdFxBrO1aEvITBgNDn7KBIg7wVw6BQGWbG3fGHo3wqq5duMzejD-HfhHO0IycfJ4sKqve3zTykmgWo9ERJWcxpy_3Ge5AvvRQChl1N8ek5-13HLlkG6zM5Iky1Av3ev4SGPoHTBKOF4CzV37SAFALpnyMmpu7RgY1mU9WJq-9tNaYYB5jntdKrXme2CIn-H9BFE6UVkKsKCnKm5IPclxazAOMdCBw6WXxmJHy6hO-wkv7iplGqq03O18nFjodtuoXwvpp4Tv-YNTNSSlxi8Y7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee5737315.mp4?token=KpBb8luDy-OGB5Q4jIYxSc7QREOq-wLUGRzFkQC9qZioy5jdviQC42IOAZyNmDmYWdFxBrO1aEvITBgNDn7KBIg7wVw6BQGWbG3fGHo3wqq5duMzejD-HfhHO0IycfJ4sKqve3zTykmgWo9ERJWcxpy_3Ge5AvvRQChl1N8ek5-13HLlkG6zM5Iky1Av3ev4SGPoHTBKOF4CzV37SAFALpnyMmpu7RgY1mU9WJq-9tNaYYB5jntdKrXme2CIn-H9BFE6UVkKsKCnKm5IPclxazAOMdCBw6WXxmJHy6hO-wkv7iplGqq03O18nFjodtuoXwvpp4Tv-YNTNSSlxi8Y7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔤
پیدا کردن فونت هر سایتی در چند ثانیه
ابزار
Font Stealer
یک ابزار رایگان برای طراحان است که فونت‌های استفاده‌شده در هر وب‌سایت را شناسایی می‌کند.
✨
قابلیت‌ها:
• نمایش فونت‌های به‌کاررفته در صفحه
• دانلود فونت‌ها در فرمت‌های مختلف
• پیشنهاد جایگزین‌های رایگان از Google Fonts برای فونت‌های پولی
🎨
ابزاری کاربردی برای طراحان UI/UX و توسعه‌دهندگان وب.
#Design
#Fonts
#WebDesign
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6198" target="_blank">📅 10:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🌐
اختلال VPNها در روسیه وارد مرحله جدیدی شده است.
گزارش‌ها حاکی از آن است که فیلترینگ در روسیه نیز دیگر فقط بر اساس IP نیست و اکنون الگوی ترافیک و TLS Fingerprint نیز بررسی می‌شود. همین موضوع باعث ناپایداری VPNها، MTProto و پروتکل‌هایی مانند WireGuard و VLESS شده است.
#VPN
#Telegram
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6197" target="_blank">📅 10:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚀
پروکسی محلی برای تلگرام دسکتاپ
TG WS Proxy یک ابزار متن‌باز است که ترافیک Telegram Desktop را از طریق WebSocket عبور می‌دهد تا اتصال پایدارتر و سریع‌تری داشته باشید؛ بدون نیاز به سرور واسط اختصاصی.
✨
قابلیت‌ها:
• اجرای MTProto Proxy به‌صورت محلی روی سیستم
• انتقال ترافیک از طریق WebSocket و TLS
• پشتیبانی از Windows، Linux و macOS
• رابط گرافیکی ساده برای مدیریت تنظیمات
• متن‌باز و رایگان
📥
دانلود و مشاهده سورس:
https://github.com/Flowseal/tg-ws-proxy
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6196" target="_blank">📅 03:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">قابلیت جستجو در وب در ربات هوش مصنوعی وگا اضافه شد.
🔍
همین حالا بیاید و اون رو در پیویتون و گروهاتون تجربه  کنید.
😉
@T_Vegabot</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6190" target="_blank">📅 01:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">موتور جستجوی ربات
Vega
چگونه کار می‌کند؟
🤔
بخش جستجو در وب در Vega از مدل gpt-oss-120b پشتیبانی می‌کند که API آن توسط Groq ارائه شده است.
🌐
همچنین در این سایت انواع مدل‌ها وجود دارند که سرویس‌های جستجوی وب مختلفی را ارائه می‌دهند.
🛠
سایت برای دریافت کلید و تست انواع مدل‌ها
✨
ArchiveTel - VegaEnter</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6188" target="_blank">📅 22:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4acdaced3f.mp4?token=g_vNgsAWWwnEFPS8XtsPtN1_iHdlQPmx5ba1pKAHoPDnFNiyzX8C7i7KkEaBfl-g7sGLCdhZqPG4C1cfs73og-RkyZKbHbdEuSNY3l-3troyi-1P4ew1GO0DuG888pbnbZ5cwX8hwKVfVx4fH9gq7IBq1vqBBmzCx1BzqjQ_dT0ZBOFhcLrAxFa2D38iYdycjBaOp18oJ2AYBJirPo46Sw4egO5qgyCuQ46s4xbuMYaoWPpPVPhACvuwcCkCZqa8cBZ63QmaCgYCHgN3HIr2byQL1kWUvZNT-J-2wRT5lhTXVnGpK8bHXPqbyt7zyKDk6VazXjB1xxSjHHLQV-Q29Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4acdaced3f.mp4?token=g_vNgsAWWwnEFPS8XtsPtN1_iHdlQPmx5ba1pKAHoPDnFNiyzX8C7i7KkEaBfl-g7sGLCdhZqPG4C1cfs73og-RkyZKbHbdEuSNY3l-3troyi-1P4ew1GO0DuG888pbnbZ5cwX8hwKVfVx4fH9gq7IBq1vqBBmzCx1BzqjQ_dT0ZBOFhcLrAxFa2D38iYdycjBaOp18oJ2AYBJirPo46Sw4egO5qgyCuQ46s4xbuMYaoWPpPVPhACvuwcCkCZqa8cBZ63QmaCgYCHgN3HIr2byQL1kWUvZNT-J-2wRT5lhTXVnGpK8bHXPqbyt7zyKDk6VazXjB1xxSjHHLQV-Q29Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍎
Siri AI: تحولی در WWDC 2026!
در آخرین حضور تیم کوک، سیری با قدرت گرفتن از Google Gemini به یک چت‌بات هوشمند با اپلیکیشن مستقل و دسترسی کامل به اکوسیستم اپل تبدیل شد.
🤖
این دستیار حالا با دسترسی عمیق به ایمیل‌ها، عکس‌ها و تقویم، می‌تواند کارهای پیچیده و چندمرحله‌ای را به‌صورت کاملاً بومی مدیریت کند.
✨
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6187" target="_blank">📅 21:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/9a53c5a0de.mp4?token=UGVS3qDljt3TScuKe5FQLflUIkUuTzigpdsmjIVTgpBmRDFNkt7Sf8sfsgOSSE3k6Nli-NQQgd1R3jMiSfjPvYAy7T0MV1j334lxocXsBImGHHPAFbaPzE0CGsYYwossN6m-fKVF00x1xAjdWY1t7JJlJ3h1h5QzS6s5Z4USlyBq0AA4UxY0qXymwPx9EUzTl1bB8_bbn7JvogWjrChkUlB10-H554cJxfhI1xP6BXg_7vGg5J0ln6jcWgXN6rMMnLy6Li-Md_jGWmDDH0mM89nqhbzWMUpUAwN9Armo1fgBKUW07im6YdLKM40YkEFkdMulaP4RqG9VmBkgpmOq4A" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/9a53c5a0de.mp4?token=UGVS3qDljt3TScuKe5FQLflUIkUuTzigpdsmjIVTgpBmRDFNkt7Sf8sfsgOSSE3k6Nli-NQQgd1R3jMiSfjPvYAy7T0MV1j334lxocXsBImGHHPAFbaPzE0CGsYYwossN6m-fKVF00x1xAjdWY1t7JJlJ3h1h5QzS6s5Z4USlyBq0AA4UxY0qXymwPx9EUzTl1bB8_bbn7JvogWjrChkUlB10-H554cJxfhI1xP6BXg_7vGg5J0ln6jcWgXN6rMMnLy6Li-Md_jGWmDDH0mM89nqhbzWMUpUAwN9Armo1fgBKUW07im6YdLKM40YkEFkdMulaP4RqG9VmBkgpmOq4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Apple
#WWDC26
has started
Watch live:
https://www.youtube.com/watch?v=hF8swzNR1-o
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6186" target="_blank">📅 21:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfJl2uoG9tPyrILMBizk8eh9-NWEeWjSZJvm9x4hh-LmovG5uNDFyjq71l4vYmzLyauSKlNsnBgXMurEkTn1t_wVRfPhh_PQI6182D-ka0L576sFg9lAnUrdW4VgSluaSmwG2AzJsSQAafz_sHzLXodqDgqL2bFho5XQ9ud1d0JXkBEncmOw5EEC9X4C6-W1QnE5Uzg8JrwfNn7b6SYStvNSUHw-fwAiVedHq5_nAr-VoYf18xALLNkogVu1rUOyzlHU4PbecpdWAmBOnQxyHmMLQIrtITeNp6abf3x4lpLPrQ8PS4H4TZbTacrBnoQFS_3JvlLGXJRKgEZITD0XNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت ارائه APIهای هوش مصنوعی رایگان
🔥
از مدل‌های چندوجهی شامل متن، تصویر و ویدیو پشتیبانی می‌کند و یک راه‌حل توکن مقرون‌به‌صرفه برای توسعه‌دهندگان ارائه می‌دهد.
🔗
https://agnes-ai.com/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6185" target="_blank">📅 20:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🤖
Kimi Work
دستیار هوش مصنوعی که کارها را خودش انجام می‌دهد
نسخه دسکتاپ Kimi Work منتشر شد؛ یک AI Agent محلی که می‌تواند بخشی از کارهای روزمره را به‌صورت خودکار انجام دهد.
✨
قابلیت‌ها:
• اجرای همزمان تا ۳۰۰ ایجنت هوش مصنوعی روی سیستم
• کنترل مرورگر برای جستجو، کلیک، تایپ و انجام وظایف مختلف
• دسترسی مستقیم به داده‌های مالی از Yahoo Finance و World Bank
• سیستم حافظه برای یادآوری ترجیحات و سابقه کارهای شما
💻
قابل استفاده روی Windows و macOS (Apple Silicon)
🔗
اطلاعات بیشتر
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6184" target="_blank">📅 19:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWfQV09mBpFT5hD9gl-Cisz10Icv4x7qEGrAESKr52Vhoze4PS7k1KRRMqVD8KGMihUBEKBVXPPNeHaZT3GEQfUX27HJIvuojCmB-BloqVwdnCtlKtUJ6vgwI_rCP695qCzVzVUXNtO1NA1DDEsR3FLtF_rhC_G8tKAsMPUNvfxbSBRjgDvzazVCDc18AROFWAhMQnZEyk8_MTeqCoGjecMQIpoBpB84VqKFP52QEWkNk_w9G37gGOOhvfsWEjZhE4SjscjfISlVAXY7IYqWixIHHnxfQHB4QRAqiJEstQh14utCklpDS-IlS67GVXryFXVLwag0GOv6Xf1iRoem_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
جعبه ابزار رایگان ویدئو
🔸
فشرده‌سازی ویدئو برای صرفه‌جویی در فضا.
🔸
برش سریع.
🔸
حذف کامل صدا.
🔸
ایجاد GIF از هر ویدئویی.
🔸
تبدیل بین فرمت‌های محبوب.
🔸
کنترل سرعت پخش.
🔸
افزودن واترمارک‌ها.
🔸
ادغام چندین ویدئو در یک فایل.
🔸
همه چیز به صورت محلی روی دستگاه شما انجام می‌شود.
https://www.zipvid.online/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6181" target="_blank">📅 18:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
هکرها با سوءاستفاده از ابزار هوش مصنوعی متا، بیش از ۲۰ هزار حساب اینستاگرام را هک کردند
شرکت Meta اعلام کرد حدود
۲۰٬۲۲۵ حساب اینستاگرام
در جریان سوءاستفاده از ابزار هوش مصنوعی پشتیبانی این شرکت، در معرض تصاحب قرار گرفته‌اند. مهاجمان با فریب چت‌بات پشتیبانی مبتنی بر AI، موفق می‌شدند ایمیل حساب قربانی را تغییر داده و سپس رمز عبور را بازنشانی کنند.
🎯
در میان حساب‌های هدف قرارگرفته، نام حساب‌های مرتبط با
کاخ سفید دوران اوباما، برند Sephora و جان بنتیوگنا (Chief Master Sergeant نیروی فضایی آمریکا)
نیز دیده می‌شود.
🔒
متا می‌گوید این آسیب‌پذیری برطرف شده، لینک‌های بازنشانی رمز عبور نامعتبر شده‌اند و حساب‌های آسیب‌دیده تحت اقدامات امنیتی اضافی قرار گرفته‌اند. این حمله عمدتاً حساب‌هایی را هدف قرار می‌داد که
احراز هویت دومرحله‌ای (2FA)
نداشتند.
💡
این اتفاق بار دیگر نشان می‌دهد که واگذاری فرآیندهای حساس امنیتی به سیستم‌های هوش مصنوعی بدون کنترل‌های کافی می‌تواند پیامدهای جدی داشته باشد.
#Instagram
#Meta
#CyberSecurity
#AI
#Hacking
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6180" target="_blank">📅 18:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIYvHthEqwtL6bOlU6YOOUc9zC9iILbNz2mOq7QkGlZIyVUl0SEbs2YMUieb5p2KsrwHUh0R50qPY6LhbwuIgXqQMnGmcDHCG7CAUx1iXchdYFS4Rf9MElEJ-GSmOUXV93F6zHgDhF5qw-w55riihGvVKNZRLdfJzmKQYk5IuAapjWbDdNU8sPR1WimIw6HIArOACiG1woez0x8119xtKyDTUYNoeL9jXjW5x4U6SRYyw0Bt15gqo7pdO5CGvqnpVDb_cT6lDhN4k_Rw4u1reFe6YPHbQRlR9npm_vFH0i1puC9jm-uwa1qu24GEX1nXoyRoUPLaOZREZmfADjwSjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦾
شبکه‌های عصبی اکنون شبکه‌های عصبی دیگری می‌سازند — با عامل هوش مصنوعی خودکار ML Intern آشنا شوید.
⚡️
دیگر نیازی به یادگیری کد ندارید — عامل هوش مصنوعی مقالات علمی را می‌خواند و مدل را برای نیازهای شما می‌سازد
💎
مستندات Hugging Face را مطالعه می‌کند، مجموعه داده ها را جستجو می‌کند، کد می‌نویسد و آموزش را اجرا می‌کند
💥
خطاها را پیدا می‌کند، کد را اشکال‌زدایی می‌کند و شبکه عصبی آماده را مستقر می‌کند
🔗
https://github.com/huggingface/ml-intern
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6179" target="_blank">📅 18:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
کمپانی
OpenAI حالت Lockdown Mode را برای ChatGPT معرفی کرد
🔒
شرکت
OpenAI
قابلیت جدیدی با نام
Lockdown Mode
را برای ChatGPT معرفی کرده که با غیرفعال کردن دسترسی به اینترنت، Deep Research و Agent Mode، خطر نشت اطلاعات محرمانه از طریق حملات Prompt Injection را کاهش می‌دهد.
⚡
این حالت به‌طور کامل جلوی این حملات را نمی‌گیرد، اما آخرین مرحله استخراج داده‌ها را مسدود می‌کند و امنیت بیشتری هنگام کار با اطلاعات حساس فراهم می‌سازد.
💡
با وجود این قابلیت، OpenAI تأکید می‌کند که Prompt Injection همچنان یک چالش حل‌نشده در مدل‌های زبانی است و کاربران باید در استفاده از داده‌های محرمانه احتیاط کنند.
#OpenAI
#ChatGPT
#AI
#CyberSecurity
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6178" target="_blank">📅 17:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کانفیگ ناب اهدایی
💎
ss://2022-blake3-aes-256-gcm:dxzSnG5le2y16bNqdyL2Hj2b9Qjptq2Ust7li7mLR6Q=%3AGZs23OkRjsO4i11hMhke9I48yENOx6VVuL23GKRXTi0=@37.32.8.201:8080#%D8%A2%D8%B1%D8%B4%DB%8C%D9%88%20%D8%AA%D9%84%20%D8%A7%D9%88%D8%B4%D8%A7%D8%AE%D9%84%D8%A7%D8%B1%DB%8C
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6177" target="_blank">📅 16:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i__JP9BxtSe2zcl35PYGqDv7-mK6f275bmIuv7-mRK4W6upwduBFGtJo6Cp2JQENW3FA_oFF1lUTnR30ijetfTwu7ljr-Wf0_ye6CITwmC2s2kqHdAkK_A87-3UAEttwOMd1SC8RO4TMv1dEaIzdCJ4eorHykCUOr0pW9WxsGuGrseBBZnnF8XPJi4sTFAK-uSUh4bGHR3YpUXrrgctn_d_hKJfr2aJIbQf8MDgVq5FpOOT1w3fO3LC6TRrDLRkxDsbbMXr8oIIrBltDD_3JtcSqx1WmAIR6adYGxEH4d3xjd98h8M5smEl9rHuCKLbp9we_d-YatdSrf8UGL6-RJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخبار تازه و ناب
🔥
@ArchiveTellNews</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6175" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🤖
وگا | نسل جدید ربات‌های هوش مصنوعی  وگا فقط یک چت‌بات نیست؛ یک دستیار حرفه‌ای و همه‌فن‌حریفه که بهترین ابزارهای AI دنیا رو کاملا رایگان و بدونه زیرمجموعه در اختیارت می‌ذاره
✨
🧠
گفتگو با قدرتمندترین مدل‌های جهان GPT-4 • GPT-5.5 • Gemini 3 • Llama 4 • Qwen…</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6173" target="_blank">📅 14:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5635b05d63.mp4?token=iIVcrMw2PJk5AZzaUDo6Edf-il4j7YQ7q-wmlZIiAYu8-9yhGLBzh4JPDCBFIZ2BP6NFYaJWTC2_2beSyPWhievXLy9Ydwib1hgex17pe-aOF-RK1upqiaZVZqowGQzFx3yXeCegRQtVj_30aWXCkmYT7tsAOMtzvEtZKek8aR-UZtYd_lM0Jq2jfGUExduGayCqbKyysPKNgz35BxLjmYbBuG_jRk4wFgdx-JBxq9VJc7FMP86ipw_m6xiILifxkI_IBQuw5ch-4Dkbfk9Ls6ANm7Acamokqg9dPPTrz6Viq1E-qRulwWx5Cebiy5BZdOBEP6Tjo6shqTD-dBXwwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5635b05d63.mp4?token=iIVcrMw2PJk5AZzaUDo6Edf-il4j7YQ7q-wmlZIiAYu8-9yhGLBzh4JPDCBFIZ2BP6NFYaJWTC2_2beSyPWhievXLy9Ydwib1hgex17pe-aOF-RK1upqiaZVZqowGQzFx3yXeCegRQtVj_30aWXCkmYT7tsAOMtzvEtZKek8aR-UZtYd_lM0Jq2jfGUExduGayCqbKyysPKNgz35BxLjmYbBuG_jRk4wFgdx-JBxq9VJc7FMP86ipw_m6xiILifxkI_IBQuw5ch-4Dkbfk9Ls6ANm7Acamokqg9dPPTrz6Viq1E-qRulwWx5Cebiy5BZdOBEP6Tjo6shqTD-dBXwwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
AlicentAI — هوش مصنوعی برای ایجاد محتوای متنی
💎
این سرویس پست‌ها، توضیحات محصولات و مقالات را بر اساس درخواست‌های متنی تولید می‌کند.
⚡️
از طریق وب کار می‌کند که در آن می‌توانید بلافاصله نتیجه را برای نیازهای خود ویرایش کنید.
🔗
https://alicent.ai/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6172" target="_blank">📅 13:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">برای مدت کوتاهی اخبار مهم رو منتشر می کنیم
🙏
❤️
کنسل شد نمی کنیم
😂</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6170" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
تهران پارکینگ‌های زیرزمینی را به پناهگاه تبدیل می‌کند
بر اساس اعلام شهرداری تهران، در پی افزایش تنش‌ها و حملات اخیر، پارکینگ‌های زیرزمینی در سطح شهر به‌تدریج برای استفاده عمومی به‌عنوان پناهگاه آماده‌سازی و تجهیز خواهند شد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6169" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
ارتش اسرائیل: برای چند روز درگیری با ایران آماده می‌شویم  بر اساس گزارش رسانه‌های اسرائیلی، منابع ارتش این کشور اعلام کرده‌اند که خود را برای چند روز درگیری و عملیات نظامی علیه ایران آماده می‌کنند.
📌
به گفته این منابع، از نگاه ارتش اسرائیل، تحولات فعلی…</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6168" target="_blank">📅 12:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
ارتش اسرائیل: برای چند روز درگیری با ایران آماده می‌شویم
بر اساس گزارش رسانه‌های اسرائیلی، منابع ارتش این کشور اعلام کرده‌اند که خود را برای چند روز درگیری و عملیات نظامی علیه ایران آماده می‌کنند.
📌
به گفته این منابع، از نگاه ارتش اسرائیل، تحولات فعلی یک عملیات جدید محسوب نمی‌شود، بلکه ادامه عملیات Operation Rising Lion (شیر خیزان) است.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6167" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نت رو قراره بزنن
ای‌ک</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6166" target="_blank">📅 12:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
منابع ارتش اسرائیل: آماده سناریوی حملات گسترده حزب‌الله هستیم
بر اساس گزارش رسانه‌های اسرائیلی، منابع نظامی این کشور اعلام کرده‌اند که هماهنگی کاملی با آمریکا برقرار است و هم‌زمان برای احتمال حملات موشکی یا پهپادی گسترده از سوی حزب‌الله به مناطق مختلف اسرائیل آماده می‌شوند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6165" target="_blank">📅 12:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی
💎
vless://1b5607ba-c295-43f8-923a-dc633a099276@82.47.63.98:8443?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fp=chrome&host=farsroid.com&mode=auto&path=%2Flokayb&pbk=US5uDp2cCip8cEuQUWEf4o7VbASXg45EeVia_Kz2QTI&security=reality&sid=fc0f43e6354ef57b&sni=www.qq.com&type=xhttp#%F0%9F%94%B5@ArchiveTell%20%7C%2050GB
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6164" target="_blank">📅 12:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شرکت Wizz Air اعلام کرد تمامی پروازهای خود به اسرائیل را حداقل تا فردا لغو کرده است. برخی پروازها نیز در مسیر فرود به تل‌آویو به مقصدهای جایگزین مانند لارناکا هدایت شدند.
در همین حال، سازمان فرودگاه‌های اسرائیل اعلام کرد که فرودگاه بن‌گوریون همچنان به‌صورت عادی فعالیت می‌کند و پروازها طبق برنامه در حال انجام هستند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6163" target="_blank">📅 12:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">📰
گزارش‌ها از حملات به مواضع امنیتی در ایران
بر اساس گزارش‌های منتشرشده از منابع ایرانی، چندین موضع و تأسیسات امنیتی در نقاط مختلف کشور، از جمله استان استان همدان، هدف حملات قرار گرفته‌اند.
همچنین برخی منابع وابسته به اپوزیسیون ایران مدعی شده‌اند که تعدادی از نیروهای بسیج برخی مواضع خود را به دلیل نگرانی از حملات احتمالی ترک کرده‌اند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6162" target="_blank">📅 12:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🇩🇪سرعت فضایی.npvt</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/archivetell/6159" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">حجم : ۲ ترا
💎
متصل رو همه اپراتور ها
✅
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6159" target="_blank">📅 10:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4d671db5.mp4?token=sZv_ihY4Xx4iHmB8KH7qzAQEbZBnaCbbPaPmwcKYDWmoLh9KZ4HTx_Pbisra4RahX2ntaxTXgD9VGFgPsike_TZgL40Q-DU8p8ZRn4uEKQH-bM0T6BvZ-naV4s_1rnOcEYfgtggZqcASCigco0Vqx_DmuyCU5NJyuCOX_pcj7Z9FccXka01NgvOXOrOUkq0RHhPYEBucrrX7RI4hl9UvZDphKUJQwtg1qKaBlKjb0RfAXMMS1qFeEOrXtpvhjLsZ-AMYxatfAG0zlHQmDH64M82ly2HyjmCQVoKPkTVSMpyUIvzjEZfABGjuDh7wU5K1FsgTYIanU3nO0BP9OIWrnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4d671db5.mp4?token=sZv_ihY4Xx4iHmB8KH7qzAQEbZBnaCbbPaPmwcKYDWmoLh9KZ4HTx_Pbisra4RahX2ntaxTXgD9VGFgPsike_TZgL40Q-DU8p8ZRn4uEKQH-bM0T6BvZ-naV4s_1rnOcEYfgtggZqcASCigco0Vqx_DmuyCU5NJyuCOX_pcj7Z9FccXka01NgvOXOrOUkq0RHhPYEBucrrX7RI4hl9UvZDphKUJQwtg1qKaBlKjb0RfAXMMS1qFeEOrXtpvhjLsZ-AMYxatfAG0zlHQmDH64M82ly2HyjmCQVoKPkTVSMpyUIvzjEZfABGjuDh7wU5K1FsgTYIanU3nO0BP9OIWrnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📨
پیدا کردن اطلاعات از یک آدرس ایمیل - این سرویس ردپای دیجیتالی آدرس ایمیل شما را در منابع آزاد آشکار می‌کند.
🔥
حساب‌ها و پروفایل‌های عمومی مرتبط با آدرس ایمیل شما را جستجو می‌کند.
⚡️
منشن‌ها و سایر داده‌های عمومی که ممکن است به صورت آنلاین در دسترس باشند را نشان می‌دهد.
💥
به شما کمک می‌کند تا ارزیابی کنید که جمع‌آوری اطلاعات در مورد شما از یک آدرس ایمیل چقدر آسان است.
💎
فوق‌العاده ساده است: آدرس ایمیل خود را وارد کنید و نتایج را ببینید.
🔗
https://behindtheemail.com/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6157" target="_blank">📅 09:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TE1tjbKcqWU0OSuSml7KFdGBwMrPOJTMioSzT2QiATVCM5nCSVoGFRUZzZ7Hw-EHDZkJteiGsNgKytbJ4dKsLAyIBtzlpFt0K-P9dQd37BGjBwnFUHkQlOEzcomqdcr-xyWdV74ySPdLwuFae2rtgeSHyrmheQLiL_fZQzCUoML_HOme2H6sEKhKjL8g9ICgDmY56wNteWPCIGNbK5yrk59Wm9rZtetjlRSldbrxRdvudwykdym1DH_ZCCO1YYHY-N8t0gyWN-Xsd5UlGCk-OvfTd1e3Q-p6yALB5DUzq4NgQMjplMkTafbKKmCzHF2w1V1KwD9FZ5-LFdeanA00Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
جمع‌آوری داده‌ها از تلگرام به صورت خودکار - یک اسکریپت پایتون به طور خودکار پیام‌ها و رسانه‌ها را از کانال‌های مورد نیاز جمع‌آوری می‌کند.
⚡️
پست‌ها را از کانال‌های تلگرام در قالبی ساختاریافته ذخیره می‌کند.
💎
عکس‌ها، ویدیوها، اسناد و سایر پیوست‌ها را به طور خودکار دانلود می‌کند.
🛡
از نظارت مداوم و جمع‌آوری نشریات جدید پشتیبانی می‌کند.
📱
به شما امکان می‌دهد داده‌های جمع‌آوری‌شده را برای تجزیه و تحلیل و پردازش بیشتر صادر کنید.
💥
با پشتیبانی Telethon، یکی از محبوب‌ترین کتابخانه‌های تلگرام.
🔗
لینک پروژه:
https://github.com/DarkWebInformer/telegram-scraper
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6156" target="_blank">📅 08:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/999b60eca7.mp4?token=GIWPPDZ3uJIc4RbZwKGbLjgCfaAyhTJNcBy9KE1RqdoaBeTCxKl38vfBVgIvg-UfQbIujdJRfffk-bPiUOyYCDqUIRjEY5CgRS0eBcucBGU88pR-5Hqut0CyM-icT8jKBbLPl7YOLwIwhGktHFVwUfTPeya1nnx8p6VvdHXd_PDZQE-8OcIVWorr0Hs-PNGOafh20kJ2Ka_koQUKCblB17tJzBJ9yffjLpVTZPJ6-9jLco_VgCJ4G3Q9FUw529ypeX_kjOxQRq3vdHCBUFMPmC15Mf4yeniwSWHx5981_JCZVlWiVHXneEHbaI4d58pCx3nJ_yH9R8kptcF4G5HDhjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/999b60eca7.mp4?token=GIWPPDZ3uJIc4RbZwKGbLjgCfaAyhTJNcBy9KE1RqdoaBeTCxKl38vfBVgIvg-UfQbIujdJRfffk-bPiUOyYCDqUIRjEY5CgRS0eBcucBGU88pR-5Hqut0CyM-icT8jKBbLPl7YOLwIwhGktHFVwUfTPeya1nnx8p6VvdHXd_PDZQE-8OcIVWorr0Hs-PNGOafh20kJ2Ka_koQUKCblB17tJzBJ9yffjLpVTZPJ6-9jLco_VgCJ4G3Q9FUw529ypeX_kjOxQRq3vdHCBUFMPmC15Mf4yeniwSWHx5981_JCZVlWiVHXneEHbaI4d58pCx3nJ_yH9R8kptcF4G5HDhjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
🔥
جعبه‌ابزار حرفه‌ای برای ساخت AI Agentهای قدرتمند
برنده یکی از هکاتون‌های Anthropic مجموعه‌ای از ابزارها و تجربیات یک‌ساله خود را به‌صورت متن‌باز منتشر کرده است؛ یک پکیج کامل برای ارتقای Agentهای هوش مصنوعی.
🚀
✨
داخل این مجموعه:
•
🧠
بیش از 183 مهارت (Skills) آماده
•
🤖
بیش از 48 ساب‌ایجنت تخصصی
•
⚡
بیش از 69 دستور Slash برای خودکارسازی کارها
•
💻
قوانین و Best Practice برای 12 زبان برنامه‌نویسی
•
🛠
ده‌ها ابزار، Workflow و الگوی کاربردی
🎯
سازگار با:
Claude • Cursor • Codex CLI • OpenCode و سایر ابزارهای محبوب توسعه مبتنی بر AI
اگر روی Agentها، اتوماسیون، کدنویسی با هوش مصنوعی یا ساخت دستیارهای سفارشی کار می‌کنید، این پروژه ارزش بررسی دارد.
🔗
لینک پروژه:
https://github.com/affaan-m/ECC
#AI
#AIAgent
#Claude
#Cursor
#OpenSource
#GitHub
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6155" target="_blank">📅 08:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Always-OBITO.conf</div>
  <div class="tg-doc-extra">532 B</div>
</div>
<a href="https://t.me/archivetell/6154" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@Sina_1090</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6154" target="_blank">📅 07:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6153">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/le7SqC4TwU8rAY_SmyFAk2C2Hp-Ap8z5qyeZ823UpBF-O8-KZpA8I0cSPat4bTlJi2aeyVd6oryTaVS18ZRibq-sYroxvhAzAj-JUO5hHtpZYuIQ79fOO9Mo3kV8_9rLfhPXbrsf3_dZqK-f-FtRJopgava2XVWL51NTwc6N9BXdT3ycPgucllScpdreFhpXImQYFIbDUsXcNJriNxfQAx-GL9o6ELWra8B1cEkjJg8SafHBn8lm0JsCRA22NjoGZVMheXTU36o1teNBnWcOgME_RFNw02n7DulH87pOeinH_hj7vjG146-xXBDXqc7hW50YO9BL39XPBwJADCfieQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی وایرگارد میخواد....؟!
@Sina_1090</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6153" target="_blank">📅 04:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یه اینترنت ملیمون نشه؟
طرف آدم بدام*
کانفیگ فروشارو می گم</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6152" target="_blank">📅 03:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
60GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: 1 GB
⏰
مدت اعتبار: 3 روز
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/6151" target="_blank">📅 01:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">vless://f5ed097b-b078-45fa-bf8b-a534f94206db@85.198.20.217:443?path=%2F&security=&encryption=none&host=play.google.com&type=ws#hetzner - heybaat  نامحدود تانل  وصل شدید دعا کنید</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6150" target="_blank">📅 01:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOM9LJ7h1JMEKavTyoHayvBXWgoReJ2rRtn-1EYmMgyVpyVmnezmAybTinfzn4UncWWdR_I72q0fWjU1O28h_Nwzg_qgfxrz7_xDfz1NmIAAMEGMdRhwdC7PJrXz02lwUl3tqr2hik52YIYfHA2ltqdn5Neg1vtUV3v9dM1GqbBY6dbU_HKqxTsca8-j1Ubcq0HOS-rrLRSz6E5qquiEcwnOOK4jSbVDLIEfMsMrQHxj8Y-_K8ZQ94057IeIFTozRdpw8OMjaNvG1__FgLt3Vj48-E0TwDBnS8PU8LggzPL6H1Qv8Y5aPt1-bkjsznw7HXbm-aqAy3c6Lf_BL9jylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم اطلاعات
قیمت هم 720
سرعت گاد
@Sina_1090</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/6149" target="_blank">📅 01:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">vless://f5ed097b-b078-45fa-bf8b-a534f94206db@85.198.20.217:443?path=%2F&security=&encryption=none&host=play.google.com&type=ws#hetzner - heybaat
نامحدود تانل
وصل شدید دعا کنید</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6148" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نصب انواع تونل های DNS بر روی سرور شخصی:
curl -fsSL https://raw.githubusercontent.com/anonvector/slipgate/main/install.sh | sudo bash
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6146" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اگه نمیزنید ما بریم بخوابیم</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/6145" target="_blank">📅 23:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">Fasten your seat-belts
Pack your Backpack
🗿
😂</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/6144" target="_blank">📅 23:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">185.226.117.8.txt</div>
  <div class="tg-doc-extra">38.3 KB</div>
</div>
<a href="https://t.me/archivetell/6142" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ریزالور</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/archivetell/6142" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-universal.apk</div>
  <div class="tg-doc-extra">16.9 MB</div>
</div>
<a href="https://t.me/archivetell/6141" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/6141" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ریزالور
95.80.164.6
84.241.3.33
185.179.170.127
188.136.174.86
46.143.244.4
46.100.46.8
46.32.4.164
62.60.167.216
185.128.138.250
185.128.138.249
188.121.129.238
93.115.151.185
10.233.249.52
217.170.242.11
185.57.135.72
2.180.21.144
213.176.4.6
93.118.162.116
5.160.162.44
77.238.123.238
216.147.121.66
176.59.222.24
216.147.121.152
95.217.210.65
176.59.31.187
178.252.180.62
176.59.31.198
176.59.222.28
176.59.31.195
176.59.31.197
81.168.119.130
216.147.121.105
176.59.222.30
176.59.222.31
176.59.31.191
176.59.31.192
176.59.222.27
176.59.31.194
176.59.222.25
176.59.31.189
176.59.222.29
176.59.31.186
176.59.31.188
176.59.31.184
176.59.31.196
176.59.222.26
176.59.31.193
176.59.62.14
176.59.31.190
176.59.31.199
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/6140" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ربات تست ۱۰۰ مگ فقط با ۴۰۰ تا رفرال بزن رو لینک</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6139" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/279755f66a.mp4?token=B26buxghlVgziZwL8csfTGG7DWoY4GZU_jn-dAggrXIcFcoGH93QRsO2uzKmL5N0QSlRV3d2Zdu20dGZ1Jf6vKfcC8H9wCitFzAlWuI963K6fvboQ3walsuIJ8xrVvywa_qWL4aurlx1WKeVrVom_Z0OujtgdqdDtwdqYBKkmhi2khwMCdMSTqyGjqcHENgRjIX8K5eaCT7iEZmdmbgx2Aa38khsfDGIXAJiTbLIzljNAmmxvrfcF1ZbMUdxCIIGIENVmKhkcpOpNB_Tptwjq37GsupFviZsckmP1tTsgmMg_gCmeAlz3Jdc2_yZFsnD8yjJXlcrSyAL629zzwnzAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/279755f66a.mp4?token=B26buxghlVgziZwL8csfTGG7DWoY4GZU_jn-dAggrXIcFcoGH93QRsO2uzKmL5N0QSlRV3d2Zdu20dGZ1Jf6vKfcC8H9wCitFzAlWuI963K6fvboQ3walsuIJ8xrVvywa_qWL4aurlx1WKeVrVom_Z0OujtgdqdDtwdqYBKkmhi2khwMCdMSTqyGjqcHENgRjIX8K5eaCT7iEZmdmbgx2Aa38khsfDGIXAJiTbLIzljNAmmxvrfcF1ZbMUdxCIIGIENVmKhkcpOpNB_Tptwjq37GsupFviZsckmP1tTsgmMg_gCmeAlz3Jdc2_yZFsnD8yjJXlcrSyAL629zzwnzAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/6137" target="_blank">📅 22:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی
🔥
vless://8879af15-f3de-4ff8-a4dd-e9ee7f33477f@v2speed.solarmg.ir:8443?type=ws&encryption=none&path=%2Fdownload.php&host=v2speed.solarmg.ir&security=tls&fp=chrome&alpn=h2%2Chttp%2F1.1&sni=v2speed.solarmg.ir#ARCHIV%20TEL%E2%9D%A4%EF%B8%8F%E2%80%8D%F0%9F%94%A5
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/6136" target="_blank">📅 22:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خب دیگه دوران صد گیگ هدیه به پایان رسید
از الان یک گیگ هم غنیمته</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6135" target="_blank">📅 22:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df24a7408.mp4?token=RmOkZWutbByAy79YTFnYse6glFO3FB5ekXuGM-wkpaInBTuAkIr7ecNZOVephc2Kyi3GLPRhlNmVdh5Lbm-rVPfQLfC0YdvKfEZaFA-N4136By45P5fINaplhXicfBsrQ2Qnp9XyR_BneBigHkY1GQpDudEIl-LLBndbPNolAX0dBeY6fkpA6GAKmOEKWv7UQPvCfnJAe3CAlktBsSWo7oPQjtfF766M4ZS1hj285tm7s-UFPXFCOm4q9dWpJQVgDJsc24KLmyIVmst49nKZsf6Pjp_xSVHODpgQad9QpgZBntRHfLH7swx96OC26FpBqNsH7zG14GYYtSnGPJc_5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df24a7408.mp4?token=RmOkZWutbByAy79YTFnYse6glFO3FB5ekXuGM-wkpaInBTuAkIr7ecNZOVephc2Kyi3GLPRhlNmVdh5Lbm-rVPfQLfC0YdvKfEZaFA-N4136By45P5fINaplhXicfBsrQ2Qnp9XyR_BneBigHkY1GQpDudEIl-LLBndbPNolAX0dBeY6fkpA6GAKmOEKWv7UQPvCfnJAe3CAlktBsSWo7oPQjtfF766M4ZS1hj285tm7s-UFPXFCOm4q9dWpJQVgDJsc24KLmyIVmst49nKZsf6Pjp_xSVHODpgQad9QpgZBntRHfLH7swx96OC26FpBqNsH7zG14GYYtSnGPJc_5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6134" target="_blank">📅 22:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/043de26847.mp4?token=nk3gJAEDZ9CWNV1Y_HqLnHjxNCgL0orR5i5DpP5LM-uXbw7jCVLedyOTBOofJknYal8qwHyMGtoWQqJ04uPKHaZy7R0zPvDyLmwy0CnLNVL4qtp-4Glp9NFVVrVh8eD3CtynjlfSg1K9mkkDl5k-Emz55VO-4QaV79bsf-hBwmN_tAY5sVcEK6pxCwTYqT-8nouaEB6nhkQULBPjiFl9Ao0twoYFzN5aALzDLcmwPrGP_IyRvvQEdvQIXNQU0FJ5lIGV78z6oubE-YKrKGWqfPZAx4YDmSzwWl1BIfgF8LKGjOAxR1gsgT0q5wM4gLxOOFV1Yhy9AxTdaJVEhB9-pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/043de26847.mp4?token=nk3gJAEDZ9CWNV1Y_HqLnHjxNCgL0orR5i5DpP5LM-uXbw7jCVLedyOTBOofJknYal8qwHyMGtoWQqJ04uPKHaZy7R0zPvDyLmwy0CnLNVL4qtp-4Glp9NFVVrVh8eD3CtynjlfSg1K9mkkDl5k-Emz55VO-4QaV79bsf-hBwmN_tAY5sVcEK6pxCwTYqT-8nouaEB6nhkQULBPjiFl9Ao0twoYFzN5aALzDLcmwPrGP_IyRvvQEdvQIXNQU0FJ5lIGV78z6oubE-YKrKGWqfPZAx4YDmSzwWl1BIfgF8LKGjOAxR1gsgT0q5wM4gLxOOFV1Yhy9AxTdaJVEhB9-pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6133" target="_blank">📅 22:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">.</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6132" target="_blank">📅 22:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">از اونجایی که بو درگیری میاد نصب کنید
😂</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6131" target="_blank">📅 22:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حال کردید
😂
😂
😂</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6130" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">از اونجایی که بو درگیری میاد نصب کنید
😂</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6128" target="_blank">📅 22:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSlipNet</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SlipNet-v2.5.5-full-release-arm64-v8a.apk</div>
  <div class="tg-doc-extra">25.7 MB</div>
</div>
<a href="https://t.me/archivetell/6120" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🕊
@SlipNet_app</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6120" target="_blank">📅 22:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تا کمپین اوکی بشه این ۱۰۰ گیگ رو فعلا داشته باشید
پر سرعت
🔥
🔥
vless://58e82e36-32e4-4368-8742-f51446c3fd28@45.130.125.66:443?mode=auto&path=%2F476T682e67a4f84a3c838ca94R86273&security=tls&alpn=h2&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%2210-50%22%2C%22xPaddingHeader%22%3A%22apinode%22%2C%22xPaddingKey%22%3A%22domow%22%2C%22xPaddingObfsMode%22%3Atrue%7D&insecure=0&host=ticket.fibernet1.qzz.io&fp=chrome&type=xhttp&allowInsecure=0#%40ArchiveTell%20100.00GB%F0%9F%93%8A%E2%8F%B3
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6118" target="_blank">📅 22:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دوستان ببخشید کمپین جدید مشکل داره از سمت ربات
اوکی شد میذاریم
سرعتش عالیه شرمنده
❤️‍🔥
تا ی ساعت دیگ اوکیه</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6117" target="_blank">📅 21:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کانفیگ مخصوص کلاینت happ
زمان : 60 روز
حجم : ۱ ترابات
لینک دانلود
Google play :
https://play.google.com/store/apps/details?id=com.happproxy
Github :
https://github.com/Happ-proxy/happ-android/releases/tag/3.22.1
happ://crypt4/vfb1onL0njkmd47DHXNPUKKEEPQNrpfahCf5vmgczvqBX6IcP0JkObKmWDw+hAZ2VwZ21pi6REi4WyyLXGQxIbppw+LrTNA2hI/+0Mv4HBgFZV3AEzeh1kgwD0yr9nppZJsSGofePhJLN2CcRV095i4udLU52HxgvaCcMSlW+MxM5BQyQycn0iznnAt+/d3fjhtJbMsGGPwC3VAK25ERXDg4IQVlPdk1K7QOfMqddVfnbPKHx6cYrLbYlh0jQS1ya2pgxEDHAHnKBapy6ldkGRojSL5NkZ0hDNhagnbvlB6EG+7WXfXLGBG4HTDv18z8kKwMcd8SqxlQs7xoZnsmUaMDLdiy7WLZ1feY8Z0upkOTj72B1Iwj1TIShiG1ZNyvKn9pPLCrNhntsChX3ckLrAMCI8U3iIRjoTgfW3WftxxTLfTN45xFAYGkektT1C1z/v1Bs+E5FZujJdzi/rCA+RoFpO8p7CvIbbCizV+dYY5deDml/Y0aBtTcy5J/Haukal2Wsx3Rrhcb8V1+L9FM6PfN0aKuZyzZ6cEZ2BCJTSEG4CAv0PSOwqQHts5lpfRLDdE6M5em9jkYuS5sdwxU2PULK4QDUn2a4LmkW5NMWQq/QOYuNTaiPsN1QqLKsTi0eXaGC9sJNHRLFOXahzwCgnKKr+ios8lIK98MoQ0KoUU=
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6115" target="_blank">📅 21:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsIlv26G0nN-jv7tBwGXk-WIoIvg74JZH84sh_UepJVizoHKXjvGdBjc5h2uRxj2GhxurN0KZ8OJav2rDJfzmWuRy6XINcGzU8qsQ3K7hxB_8GNQeOPfLl12XmEIDEjG7OfC1DCGMdBNuiwifDKnpELWfh0_IR96o1o0W90C0ogq9arqX5OaxtfqGQOvFXRBU_2IO5yhtP5pGW4v6fQXTUjcRUkRkvYkSTDovBYw9c6errfCfV1_B0ORba71EDhkOB55aN5RPjBcv20h2JCyKeLLvzxEMuLqSldWGQgoyTr3cv6dHSkRQVALB6u6naGjNebRW5tNQo40dEtakAxa7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
✨
دریافت 10,000 اعتبار رایگان Figma AI
اگر از Figma استفاده می‌کنید، با این روش می‌توانید 10 هزار Credit رایگان برای ابزارهای هوش مصنوعی Figma Make دریافت کنید.
🚀
💡
کافی است وارد لینک زیر شوید و Team موردنظر خود را انتخاب کنید:
🔗
https://figma.bot/4o7EDMQ
🎯
مناسب برای:
ساخت رابط کاربری با AI
• تولید Prototype
• طراحی سریع صفحات
• استفاده از Figma Make
#Figma
#AI
#Design
#UIUX
#Freebie
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️
کپی پیست آزاد برای چنل عصر نوین فقط
😐
😂
🙋‍♀</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6113" target="_blank">📅 20:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🤔
آیا گوگل هنوز برگ برنده‌هایش را رو نکرده؟
با نگاه به رقابت اخیر هوش مصنوعی، به نظر می‌رسد گوگل همیشه چند قدم جلوتر آماده ایستاده است. هر بار که یک مدل جدید سر و صدا می‌کند، مدت کوتاهی بعد گوگل نسخه‌ای قدرتمندتر یا فناوری جدیدی معرفی می‌کند.
📸
از Nano Banana گرفته تا Veo و Gemini، بارها دیده‌ایم که گوگل بعد از اوج گرفتن رقبا، مدل‌های جدیدی عرضه کرده که توجه‌ها را دوباره به سمت خود برگردانده‌اند.
💡
نکته مهم اینجاست که کیفیت خروجی فقط به مدل بستگی ندارد؛ مهارت در نوشتن پرامپت هم نقش بزرگی دارد. بسیاری از کاربران از قابلیت‌های واقعی مدل‌ها استفاده نمی‌کنند و بعد عملکرد آن‌ها را ضعیف می‌دانند.
🆚
ChatGPT یا Gemini?
• هوش مصنوعیChatGPT در شخصی‌سازی گفتگو و درک سبک صحبت کاربر بسیار قوی است.
• هوش مصنوعی Gemini معمولاً در برخی وظایف فنی و استدلالی عملکرد پایدارتری دارد و کمتر دچار خطا یا «هالوسینیشن» می‌شود.
• هر دو مدل نقاط قوت و ضعف خود را دارند و انتخاب بهترین گزینه به نوع استفاده شما بستگی دارد.
🚀
چیزی که مشخص است، رقابت بین OpenAI، Google، Anthropic و سایر شرکت‌ها با سرعت زیادی ادامه دارد و کاربران در نهایت برنده اصلی این رقابت هستند.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6112" target="_blank">📅 19:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba62c4ab7.mp4?token=LQwI-CqOJbxynuu3Xo_JYg0dKm5HpxMxhV0oIUSkfiyd_-55hoMoWPIkKT7bC-K9smrFc9hQZhMBNLZQYV5Vg6f_mVdri9YRyNj2SUuC1ZthuCKQhNywdu_ZATboxrsnggPa64Z0B0OTX5nDN95BV6kRL9c0kQ9qNpoqoLcWJUjMGuOUGZBJxUfvTRhd6C_v_p2SydACAkKgMrbcn517AADwIz8Kas0EVl-p7F27U9wZ0LhmiZe2SYMJDk6exPH13Ho6kX41OjwaOM0az1MKOBTHBTMTFgY3I0D6Oh1jXT57jr35NQzuXfoRiRTjmC1qKGp9SzSSi7xBdTjtLrH1qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba62c4ab7.mp4?token=LQwI-CqOJbxynuu3Xo_JYg0dKm5HpxMxhV0oIUSkfiyd_-55hoMoWPIkKT7bC-K9smrFc9hQZhMBNLZQYV5Vg6f_mVdri9YRyNj2SUuC1ZthuCKQhNywdu_ZATboxrsnggPa64Z0B0OTX5nDN95BV6kRL9c0kQ9qNpoqoLcWJUjMGuOUGZBJxUfvTRhd6C_v_p2SydACAkKgMrbcn517AADwIz8Kas0EVl-p7F27U9wZ0LhmiZe2SYMJDk6exPH13Ho6kX41OjwaOM0az1MKOBTHBTMTFgY3I0D6Oh1jXT57jr35NQzuXfoRiRTjmC1qKGp9SzSSi7xBdTjtLrH1qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧩
یک نوار بی‌پایان از معماها به جای تیک‌تاک
یه اپلیکیشن جدید اومده که جایگزین اسکرول شبکه‌های اجتماعی با حل معماها میشه. تو این نوار، بازی‌هایی مانند وردل، شطرنج، تتریس، سودوکو، پاسینس و بیش از ۱۵ ژانر دیگر وجود داره که به صورت تصادفی ترکیب میشن و ترکیب‌های منحصربه‌فردی ایجاد میکنن.
میتونید از جریان خبری به چیزی مفید برای مغز تغییر وضعیت دهید.
🔗
https://puzzle.express/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6111" target="_blank">📅 19:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=OE5Lul5bkK-RyXM1P8rgWkJqy__GN1YsLEogQBNrlW24Dn36eUkRzQwmZU2BJItUb0gAB0Jm1m8xDQAy0ScFtlcA7_ipxRtL7NkGHG2FqHwy85qRDvEgYsoph1qCr_YRWcRODs99dvnfev2Mq3SNLa7LvYUiEBd1EiKz76Drlbh-B4dBK9479a4n0NQUTnk8E8UrgrmIGngdl2x2NC2493UcQavP7hH5RVLq1arNBbrDPyikT5ynrLvskha_LgjYBPDAcGvj1gn7x7M5dwp6klpE7nGIYyCXf72i8VOgF8OeCg3GJbWtEmOtZxRO0nbATDHJ2Xdr5gkMt837b_x5Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=OE5Lul5bkK-RyXM1P8rgWkJqy__GN1YsLEogQBNrlW24Dn36eUkRzQwmZU2BJItUb0gAB0Jm1m8xDQAy0ScFtlcA7_ipxRtL7NkGHG2FqHwy85qRDvEgYsoph1qCr_YRWcRODs99dvnfev2Mq3SNLa7LvYUiEBd1EiKz76Drlbh-B4dBK9479a4n0NQUTnk8E8UrgrmIGngdl2x2NC2493UcQavP7hH5RVLq1arNBbrDPyikT5ynrLvskha_LgjYBPDAcGvj1gn7x7M5dwp6klpE7nGIYyCXf72i8VOgF8OeCg3GJbWtEmOtZxRO0nbATDHJ2Xdr5gkMt837b_x5Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6110" target="_blank">📅 19:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔐
دریافت SSL رایگان ۱۵ ساله برای پنل ثنایی با Cloudflare
اگر از پنل ثنایی استفاده می‌کنید، می‌توانید بدون نیاز به Let's Encrypt و تمدیدهای دوره‌ای، یک SSL معتبر ۱۵ ساله برای تمام ساب‌دامین‌های خود دریافت کنید.
⚡️
✨
مزایا:
•
پشتیبانی
از تمام ساب‌دامین‌ها (*.
domain.com
)
• اعتبار ۱۵ ساله
• بدون نیاز به SSH و دستورات لینوکس
• قابل استفاده مستقیم داخل تنظیمات TLS پنل
• سازگار با Cloudflare Full (Strict)
﻿
🛠
مراحل کلی:
1️⃣
در Cloudflare وارد بخش SSL/TLS → Origin Server شوید.
2️⃣
روی Create Certificate بزنید و اعتبار را روی 15 Years قرار دهید.
3️⃣
دو مورد Origin Certificate و Private Key را دریافت کنید.
4️⃣
در تنظیمات TLS اینباند ثنایی، محتوای Certificate و Key را مستقیماً Paste کنید.
5️⃣
در Cloudflare حالت SSL را روی Full (Strict) قرار دهید.
💡
نکته:
این گواهی فقط زمانی کار می‌کند که رکورد DNS شما در Cloudflare روی حالت Proxied (ابر نارنجی) باشد.
🔥
با این روش یک‌بار SSL را تنظیم می‌کنید و تمام ساب‌دامین‌های آینده نیز به‌صورت خودکار تحت پوشش قرار می‌گیرند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6109" target="_blank">📅 17:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyZD5qhptXK1VmygYa6qgpoKR8frtcsb6vG658dg_qIfCrmnVs7a1cqSWN4fwdydnxO89aV6Y0Rq7CmMk3-jyXbEt7VCGzv5PEuzIu6RUuHRGuKkLhd-qcb3bEZSV_qyCwFk7hcni2H6Y-OUBC5XH6vtaaIQlTvmCvl7bUiblNwd3td23Rm-9zU4J-SIKD8phmS3gi4Q6dYU537P9yXhijKf_Xx2NNY8NcWZElQFd0oL1b0F-R5sjHPG23t3_pAoZSgW4V-sJOkvEfeiNt0l5QmPlgBgIhZVXC8RjMkd33gZnYooP9PJIijghSgNcFbjBqMifqqgFnuvnw0IqqttiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت دامنه رایگان برای پنل ثنایی و ....
قابل ثبت در cloudflare
بدون نیاز به احراز هویت و کارت و ...
فق یک ایمیل و یک حساب github لازمه
https://domain.digitalplat.org
https://www.gname.com/tld-eu-cc.html
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6107" target="_blank">📅 17:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: 50GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 50 / 50
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6106" target="_blank">📅 17:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
50GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 50 / 50
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6105" target="_blank">📅 16:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انقار میگن نقز شده این سری     .</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6103" target="_blank">📅 16:24 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
