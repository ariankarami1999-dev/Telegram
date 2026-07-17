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
<img src="https://cdn4.telesco.pe/file/vFfN-ofjbqrxXN6zHW1xch8ZVqBXahE3yy7zaw-d__1ggMSHQuJIjtbzLuH_GKUupeBwUXIvV3-LhyTQadIOS_1mmg-YjkC3L3ecO1hY8tmHQAJ4ao8IuZCnYde2kpcpca2QHmS-RxWJLiImiWJzJBn2njywl4BdAT58QEsS3BKu7KYhrIlpurJKE6QVG1a6f6bl_em_XxcrcaZ0Gg5q8Teh-zUOqfILy8uCp69bZogPLHQ6rfgXGqMI0az60YQuc-CgRYo0ZFVzqo1VLfUonqrsWzOpR8qcXp03YYs_In9xCD_R15-wytM68H8JvwOg6F6kWSUcScItIaCFmM_eOA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.83K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 17:40:19</div>
<hr>

<div class="tg-post" id="msg-7066">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">vless://06069771-bef8-4730-b711-c51efcdad901@onlineprochess.ir:8880?mode=auto&path=%2Fws&security=none&encryption=none&host=tsrety.dpdns.org&type=xhttp#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF  تمام نامحدود</div>
<div class="tg-footer">👁️ 396 · <a href="https://t.me/ArchiveTell/7066" target="_blank">📅 17:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7065">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">vless://06069771-bef8-4730-b711-c51efcdad901@onlineprochess.ir:8880?mode=auto&path=%2Fws&security=none&encryption=none&host=tsrety.dpdns.org&type=xhttp#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF
تمام نامحدود</div>
<div class="tg-footer">👁️ 534 · <a href="https://t.me/ArchiveTell/7065" target="_blank">📅 16:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7064">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lN-oSBvgHC5D41MOvxSfNkGDFxvzKeafIlu_lMs0m7mSibgr-Ky6lHlCdWUk81ezOTPTRbAb1JOVFHlAzoedij1nk2sR_zM1n-IWYGTeOVQKhe5cQybvLTRRhZNKJNKOEU_g033to5HEnC27P55nHAsC-ZqoLMJ_75b9PTyRMIVYOoHYALnSsHbMicHsOXQiPVmeJBwpZcauskzSLQmh7K18HdR-1mLNtcjIZ9y-IqzGKz_Sm7O4-sHhgCgaOlD7C5Fi0fOrEAUNPjcGRShxNB0RYWMf-o45TU4E6j5U3FtEqFp1t5ytnedwKdlb792tJwxrgOB2ertUDFr0OrGRzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 566 · <a href="https://t.me/ArchiveTell/7064" target="_blank">📅 16:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7062">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/01b871c31b.mp4?token=ZlQlDKguwdfpIp-I9fLFKtrWl0sr_hmhYQRFPHLKhqG_pl5lgxyo8rvRJvDfukN5U13yPZeAWCZXpD9oBAIEajvlGYoitxX9rQikfmTrVT-hYxur1C1W7MGwEjUdTUqZAa1TcumDkHlDriCQI4NAeLO5oBC0-q-eR4DEoQdg3WTjUxvakY7jmYq-Ujxed3DbWmLYMbmCX-rY6Qh0jF-67TFUnN8F0W1JSUxQngVPfd8vVrbCRh6wbGf3tRsT7GBd794WJfi44ADsWLqotjp2hdJKoygg3nySjg2nSpu3SAM1VRzI9bLoBp11C4Yy5csa3LqRq-VcMBb6j0IhBAz9rw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/01b871c31b.mp4?token=ZlQlDKguwdfpIp-I9fLFKtrWl0sr_hmhYQRFPHLKhqG_pl5lgxyo8rvRJvDfukN5U13yPZeAWCZXpD9oBAIEajvlGYoitxX9rQikfmTrVT-hYxur1C1W7MGwEjUdTUqZAa1TcumDkHlDriCQI4NAeLO5oBC0-q-eR4DEoQdg3WTjUxvakY7jmYq-Ujxed3DbWmLYMbmCX-rY6Qh0jF-67TFUnN8F0W1JSUxQngVPfd8vVrbCRh6wbGf3tRsT7GBd794WJfi44ADsWLqotjp2hdJKoygg3nySjg2nSpu3SAM1VRzI9bLoBp11C4Yy5csa3LqRq-VcMBb6j0IhBAz9rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نسخه جدید گفتگوی صوتی Chat gpt منتشر شده و انقد طبیعیه، پشمای همه ریخته!
+ خوراک غیبت برای دختراس.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 665 · <a href="https://t.me/ArchiveTell/7062" target="_blank">📅 16:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7061">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 836 · <a href="https://t.me/ArchiveTell/7061" target="_blank">📅 15:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7059">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 922 · <a href="https://t.me/ArchiveTell/7059" target="_blank">📅 15:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7057">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/ArchiveTell/7057" target="_blank">📅 13:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7056">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/7056" target="_blank">📅 13:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7055">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msxrFRzo8l0KgUqJ2knGUC_5sMSlAiNnt6eg8lHFXg5FfI5Br8krD7k0XdHBL2CLri13I2SIpfoAO-DpRTfRXiEZSFRdUOIydWsBb_VbxRW92zcHgbJPnpssgU0w2cPq-5EBZwkB87ptpPVhMVhESnmNSOnlQ01mxrQU3yA8VAbZ1Nsmgnvdvkq1nLwuyhXKhvR1yUwOq2OZs9N-qqRgyWMdFruToi4E5EuFQZOezD9j8UQmGk-y0GujATdbhmH1cx1B2ZzQtk1geIBLfi_5FMcZ5K4lgzv3iHcWzVexKFHMjf6U4hS9U7-OYjUtwyKZt4Nhav_M_AWm7L1IALibXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/ArchiveTell/7055" target="_blank">📅 13:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7053">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7053" target="_blank">📅 12:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7051">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5RxlcfqcXyi2KYWTweuOQ-uHtmXqr_MIx8k1mi55tIRbrbEFeC4f3MwaBtOl51E0mQ06SVqSbvyBTsiQmu396srKtmjcI3YgqnL2Bf0evmy7hOFRLwgue8hb96ry86XX1HCi-1po93tfGOQltYKKsIoFY4OObBm91VDXEFfu2rzHqSKq1CMKwBXiHl6ThIzMAa5N6GavT9-RVg1cMwXsBOKt-jgo-oUV1PVrsqjwloA69497FFdsOdxL7ZrBM24DXw2Yvn2f9mx6TmB5yKv9NKu3UTfdGM5Nx0QOvI7ZHdjJNMotYBT_EgDEMrnD7EN4dMzX1BPx7AkqMJxS1e5Ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/7051" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7049">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/7049" target="_blank">📅 12:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7048">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/7048" target="_blank">📅 12:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7047">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏
✨
فرصتِ ویژه در ‌Kimi⁩
‏با دعوت از دوستان، شانسِ خود را برای دریافت اشتراک‌های رایگان امتحان کنید:
‏
🎁
جوایزِ قرعه‌کشی:
‏
▫️
۳ روزه (۹۰٪)
‏
▫️
۷ روزه (۷٪)
‏
▫️
۱۵ روزه (۱.۹٪)
‏
▫️
۱ ماهه (۱٪)
‏
▫️
۱ ساله (۰.۱٪)
‏
🔗
مسیرِ دریافت:
‏1 -
باز کردنِ لینکِ دعوت
‏2 - ثبت‌نام در پلتفرم
‏3 - مشارکت در فعالیت‌های رفرال
‏
یادآوری: تخصیصِ جوایز کاملاً تصادفی و طبقِ قوانینِ کمپین است.
🎯
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7047" target="_blank">📅 09:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7045">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2PsCCGUgsWzlsmwlrkM0-vhMhUow5-MY588lqGvirFhux_GGRgrK1EzCZ2tJuS0zLHJYgD-y7Hno1q_RJ0FyEqYEp5DiJ06thfyqwyOJCnCKVz8u_szK0Ah7WVeYIuIMIpPWK0d-oEo3uuPk1d3oLr6gGRE7CWGb3qpvPRtO2PhJ-srm6miYaOLwMZVRMi54W2sJltKR7szNmIsYXlpaiX8YsLeFWn6OXUMYjZYgWyO78CzXbJ7WmP42Roq4m69B55CwEa14E3z33TAlpJlItehHoQDbLn9jO-CZGYz6apEeixlDV6LDoPvG2lcgJBr4IgWZNhUIS6UEIpf1hzsmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7045" target="_blank">📅 03:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7043">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">172.64.147.128 104.17.166.13 104.17.166.13 198.41.195.250 104.27.51.177  اگه پینگ نداد باید آیپی های تمیز کلودفلر رو بندازین توش</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7043" target="_blank">📅 00:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7041">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuXoCxCyh7AlAVXF9DO-VFECmbOBQ0NDJWYAE__KFx5Y96Qy7khSgVwT80nDSKUKw6wTcCI7RMpQk6PSdG-ijFER5OrzWAeunphZK_IZBi4gelfpet0xXvaBHcyQWU5WhdCUUSs_YT3TVKxmIWdtdKH2SFjRR6Kf-3ZETo6S-2CsA-bACbF9_tY_Mgp-SJuIP4lutVzOEalvtOrzuFUsU-xPteoK9uJjbvMPQz-lWRb0C8y0Sox1Uy72RTB0nF9gotck9yULMk2zKHV4UbHXxMOAU4WNxsniVoW5_AAYtHFzyePwWe8lrVw2qabeCuljTR0LFuZne7X2o5VUKHy4Fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7041" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7040">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tB7gb11wskHt6lSadNk6n2R5lNz4jewzbzVOdbrQ-ChNaSJInSfyVQP1qAUyhMhcvILKD-hmolQTmqCHzwoE-K2SQtMuNkP9wPcYR3GQusr61WoexeBfTfzF3lM42jgv2VUnAltIOTqAdsQxLokIKTDEPYFVa36gTQPD0-n1bsr_X4PsiVCiftvPyboRqivkvAV2maaRpLwEycM_QzJIByjEPOO0JZ8egoU1eHw5qWqdWAcCZaVujKhN4P0WlYWOmx6I1SDAJ0Mgt9tgf3cahDXuKdKxpOi6iKSoZWbRrupU_uYgFZlfYMJkNmQk7jQUV2W5LVx8vCwkN2W6UL0ZZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">200GB   vless://1c0e84d7-34ad-4242-9b4b-ea81f973e0aa@172.67.117.177:443?path=%2Farchive-stream&security=tls&encryption=none&insecure=0&host=mail.qbo.qzz.io&fp=chrome&type=ws&allowInsecure=0&sni=mail.qbo.qzz.io#%40archivetell  تمام
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7040" target="_blank">📅 21:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7039">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">200GB
vless://1c0e84d7-34ad-4242-9b4b-ea81f973e0aa@172.67.117.177:443?path=%2Farchive-stream&security=tls&encryption=none&insecure=0&host=mail.qbo.qzz.io&fp=chrome&type=ws&allowInsecure=0&sni=mail.qbo.qzz.io#%40archivetell
تمام
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7039" target="_blank">📅 21:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7036">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPdSyiLT0AQreaouiM9z6q3qHm3aJprafe20Z8Dr5yGbLAL4jI1c8jTHevi9fp7JM249KGPYaOsljhtU1dLfC6pj90Hgv7YVdcRpAqGqoGnWtd8RMdVZiKmpjaGaJ3Zqb_2dejavDtYe2vbeaLR262fJTom-Lvx5pJJ17KMBiozKRZu-D0lIctrC2Hs20xPeHOPatOs-swKg9tjlvgpSVoK5jbto8jsDb1wof0L5qtDzGaxWhliqzMBIHJJ1FiGNxeO6d8n1p8a7EuGAy3OigzGZk2l-ymQqw9f6nxr0IWnySJx_YbqyV8dAl02ytwsU7ZEPiV120TQrThqi0vXLMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7036" target="_blank">📅 19:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7033">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5dMpxRl28GrsRa6fTO07zEhlL9s6KiQL9TPghCtuPFKuXpopPkYjeTA-2O9ybYbbh3hzHsvrq5aZUc2Zggnlsbtvj1tLkx1kv-q9zEHc-6cpcMO7UXPs5d87PTwe93Xrb9WtRb2ZGsDXL3A9NH_IZWcUsxEiYN-Sqc0uXHD1wtiy0ctXY5vK6OIFQoC_XnpMp9cpf8Jfk9hUQ23asvgB_NNNhjQOXXssJ1F_YtEA6Zusi62u2OhcLwseNd3BEMHpVUL0EKOKLPcriQbJObwoxS3kJfgV4vETO2K7Dl8ZkIJiXW8AONzVdHiaLxNMotlOMUFRjqJM2bmAlESDKXJwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IoFhYbZn2Qx1A__3FhaeJfLJE7ZSvO0pS-lsBB07xUZvymgIA21DUU4PvRHu11-czINuazQAl3oi5zWE6YBGq2tZZi-Cdyb1zCADMZ5yOCW0ZoMtX2cqwHKdPKu3nhxpQo8ow4OPxfppHq-5yhsdmijE3BCgGegwQkgsYkvA4kauwhOLG-APEqtLP_ad03YjK8GUzxP5YuruARUDOS-zIMzx-7x-CYjbnlI096eF886uk7gW14jswC0Q-kXAgg-QXlMsvPmRIige3RvmPT2qM2l9P_wDDuRoTcA9gguV6qqvhXePL22sfAw1oaHAdXmtJxyyJdCQDMZRaRLaLQkkRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G1gBeo7G_59fNtcWyD1EyX4swoPOdg7NfTJ4yo4_KaCoAef_hzSKLACr27KzMP8NLFkTpWrPoq4-mz-BtO9OqLc9yqjXEKyL05FJB7O11AKJzlZkuAP6YDccl8rvUr8CwpbcXH7TwAqO35LBheJbRv_1U0w-Ydq2uC2m6bMBBTkHy1Dc_WEgV-OvWjlJYs2jmS0n3x49IACZFvi-oC5EGCoyZJq2MWpuW-Re8NCzO_SimvJrN4cYub94p86fX4M98FpoHALNHKdx1VA1wCtRDcVB5X7aZMAUmpIgcD7ArseMWbBGwMSEe0EblC6O31vwYAcCC8QHUHqyDEvTKgbbKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/7033" target="_blank">📅 19:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7032">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🛡
معرفی فیلترشکن GRoute (جی‌روت)  کلاینت متن‌باز، سبک و رایگان (بدون تبلیغ) بر پایه Xray-core برای اندروید با پشتیبانی کامل از زبان فارسی.
✨
امکانات کلیدی:
🔸
پروتکل‌ها: سازگار با VLESS, VMess, Trojan, Shadowsocks و REALITY.
🔸
وارپ و آی‌پی تمیز: ساخت کانفیگ…</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/7032" target="_blank">📅 19:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7031">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtAVZ1kGyZycL6MlxKrI5BXSvUBBsqghIX_BZAQsWfCH0mnJqn1mGUinWLftamLnBUv74pSSsHg4kx3Z4IQd7lIotlEPF49MtSHQ-qnr2iVoQK94FEdfVc6OP7dlTP7KqEfS9F6ri8Pc6FwoSxbTUkKPsvuw8wCf6Dm7Z7rSZUz9hYIfqAT-eqTMYwBnC0v6C2jIptocwXA0AUrb0e_pa3gs58C-U6uehZcAyeD1NxDmFzT2-3S1AxZwJsX2Y2V_Cb0HVaeZ_q50Wc3Mvk4AC6xFT48-fWaHDhHPLrdJMIB6LIy8DMZfL4j-EqtET6TAc-o92UoCCcD5JJX-prqpVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7031" target="_blank">📅 19:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7028">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HMhDqUozHnbHESxnZImMIqQvdrJP_ftjJoRKIs-O_8pTyS7ZMif43-PSWAgbFA82_5aaLv_qwdrNLTic5i_H1LSPUBGSCbBRb2B09wSz68wPwlGhhvH97gA7iuiTNJU6eLC5FAzei8D-DQKjbyAl9hyaEF28G0stpb98e7NqFBS0vb0W1goLmA-uV4UNqA_lh2X2a-ixhLtZZJ7vFLLYJstl18eimYYZGpqu7dyY3zkTYdEQWen-tO1mTUlpA8OYDAZv7tNTI7n4td_sXPJVeTpJjY3cfiiukiIzsplYvpVG9SgtQxoiMcv7dzVOmGNx8n69SCKXsyyw6kRtsPOH9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/op7UlxHQ-VpTOhZcjdeodFRUi0xIvK_oE6zwPwDe1Yh9KS8juunY3-NDP0xXUg4Pl2jBk_5yulCHmPz1kgLCruJOhaT59qK55cglSBJBEKHrQchAXpxwR0Oz2D84Mhp6FuR5GFfNveX0otchgiCilspqGMLqcxdOb5RCvlH6dUEEY4kag9WZI1YcKLhg7T8R9_nsPXPpEqUWAXmBLQ66NHKm4dxYfypNUvWfVBjcA671Ag3hr-8H_tF54yOj9NcJmvUb6LrDntfpWxj5AjA9qknrHg7KLdv_ewBjT1_jqTJzyViX0649KnCC22fU9qQxap5HyI8AfD60w218ICIskA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDFSWFkplHuP_ZKWOqYFBpCLI9E_hc8QaqjLjsMGKlmsDOIZaG-Stq4JDHwqBykGb6RINnv7hebtzRpBTcigAqwyb7xVpzmNNgCe15HIBz7rqY6dhl3sKdwTz609NWnG5dqq-U-kM2UoPerXRnyfoGOzmrR5apYJbmjXxrtc_Tn8iG8YJyQDfm7XEJ404fSQZAUtTn0dOJcdXBI_6LctepbdBMmlgTiI0-FNHOA8Oe6azS8CpZS1rnI4oHig0PP79HurhRBMInjxZWgvsPWty7MlU1FObRdnfnsvG8cut5TPauReTAgMVYq_c6G2RDhsJvoR3Na208PxKWmmJkJfyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
مجموعه‌ای از پرامپت‌های متنی، تصویری و ویدیویی رایگان و قابل کپی برای مدل‌های هوش مصنوعی مانند ChatGPT، Claude، Gemini، Nano Banana و Veo که امکان فیلتر کردن بر اساس نوع، مدل، دسته‌بندی و امتیاز وجود داره.
🌐
https://freeprompts.io/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7028" target="_blank">📅 17:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7027">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCmPGJzwZigNzeKC0LbyZZqExsF0EAJ1p3L5RQoJ6n_XiG3J_YfrvDm_pFr0jlLKW5lPgNPQEqQH4jsLXVIuH_pMZi51bYN4HDNWZcq2IN2ONCnz_cMVqX80LsHhWxnysFQWGAUglf_QpBI0gH7CkdtLCxfweMO5xa8exv8pzjEwskf1tUtOmfVuI2e3Kx90tS3Cm43Bzoje6-Mrthr5PqPAOq_8GiG2ZLR5i1ASSoFnoGS8DPm9uOI_XTI2LUXc7-iN7CFZXER8X5qE9-Nmo4-XTUIQNfADXvHSaOZe_kNu3kX9Et3mmnAgA6j-7KNnc3fE6g1I16qh4ArcUk7_ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7027" target="_blank">📅 16:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7026">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pO7D6qdO0IAXnu5Nxz6OeLKl5_6DftEMjpABkO6U7GofmmxtLYNR5oQ5QJDnCLWfp2GzFEHvTr71Ban7lIJ378RqZmla_w87FAdbe9DXBCF_nrL1yGAnuxFo9hxgaLiRq_FCHd-ALZewnd3TMYnMDZqcRooF_w-dlQDDCfiZV5z4S1guZs1VefRifTYlx2rCHi3CDTvYs5U0tMjGsiVEjtL_kihl9okDVoH6zUvoss65ZzDRtk66mENaw9pdDzHJzeLTKGS1YTPRiTQ41-PfKbT0v2tw_jJFeUVyoxLOp-WlC2BwbIfXAoReVKbjACSlLJ9NEDMPDoTfD6Oeinnrtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7026" target="_blank">📅 15:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7025">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/ArchiveTell/7025" target="_blank">📅 15:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7024">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoFhjQMhPO4IlU6VXOYWVh7pczDZBLm4mqh2ksMmO895rEU0FLULN1HBYOfb_9cQSo16dS4uPL1Y2ngtLKqyNfMjbxPw1I3LIT3hb6Rpd2YerfCoCuNi1e9Cm2coPWJrmXamnmkwhKX43MGTAOADs5W4ArOzugXdNGfDIv9YvcRxoa_Mr2n1kq0CZ72805g6s_wDKBNguvNN7IrnDi07-MymFZk_EF1E49uBgEwLXAEaTHE4FIK9S7qWjTxFZGfUfOYhVSguXNXRxFdDpNnFNpVZhztjbXUNn5tjDg4lhOePTxZIxJ5J5W-bQFsTn5sa-UAm8FEla1wGhQfDAe6aWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
؛OpenAI قابلیت جستجو در ChatGPT رو اضافه کرد که به طور همزمان در چت‌ها، پروژه‌ها، تصاویر و اسناد جستجو میکنه.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7024" target="_blank">📅 14:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7023">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">📱
معرفی Hermex؛ کنترل کامل هوش مصنوعی اختصاصی از روی آیفون  اگر با پروژه متن‌باز hermes-webui یک دستیار هوشمند اختصاصی روی سرور خودتون راه‌اندازی کردید، حالا می‌تونید با اپلیکیشن بومی Hermex، کنترل کامل اون رو روی گوشی آیفون خودتون در دست بگیرید. این برنامه…</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7023" target="_blank">📅 13:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7022">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7022" target="_blank">📅 13:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7021">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ign_P40uifPcP_lsArWm1T9fyoiFnPyRsgkyZEbO2fiessXTdDw6l5ufpdSdVcA1a9P_H6cvJJGiZRmnad8ZuTkmSnAJS4i4e6MiXtCifO9N7inKigTckG5gQqlvjwj-k8quv8HwYNXtOJT2YcJfJfteNMt213KO9Z7AAbIgt03QO_oNFt6UgIU2EoxHozyokavhnX0AOMvzvFwxRpvmJB5VJekIpdbbXqecqxDc01ZjXej3Tm0h312Ba9hANaFwNeI7iTK6Mi0TWaYpZ9E7WhY2hSoVzhpkKLkW49c-geupAun3NYV93TwXFKBvJZKPruzCHus7InnEybZHqE7pkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/7021" target="_blank">📅 13:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7019">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cetkIrvZdFFvI6XOABktjaagfBmysQuQ6VzjwBLQRDgK-jXq4MGFSA73Ahki35KJXE-_GKqchOhNNYZAvyGV7HLelyu3JNbAFvtFlb1nVwIanju4ObjC_JUj-6TLLNxzzPzNYrQGibjeBff_Bvx5KjKk5-KTi0u2QtJvDG4g1rcWl22d1ii547j8Tkxh7d3gz5dEFl-1v-LLWujdcDRHpcJrJsrjtZ47H88fhpHQMxe5QmritybhA37u_5Rk8TFrZDUkpYlOoqjw3vGfWvwzIcjkU3E_Yt3RfFviuHbmvuvhA8iNMitkU4LbvR3lEkEI4RVFEqVJDIgsaWFKeJoQpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7019" target="_blank">📅 12:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7018">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k800JL3M4ql3JT71Xaa7zOzOSyA6tQaHHrwosbBvG5-vnEa6m4y_G8cb99o4hTnXcdhf5mcmD2TfM-pJyN5qwGu4vu6EtC1oSrzvmyP5qgyUrcNAZoK34_8g1XIC6Ahq4Ikz1voZCenBKLimYVfhHLwPSY6PvVvS7OWjH76C_aUD4Ysbx1FiDxJWINAe5WDtyA0AIpuX3ePmKU42UTuKakI6jXe31UvSuq2XpunbvIUO-wCjUOctNFFe0Fino4EufWLIxe34VcSros8gPTk3utDopTG1MgQ36b5DnArL5SGIA9uCsVwYseNld_qcb2P4ecsO5XU9OvQ_91kLZ0i4Uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7018" target="_blank">📅 11:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7017">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XacBMRRAjnKYzczBUsqUyxXRjF5ef23iDwzuXy5iYVfiQ8kzH_jauU2r2E4lze5HQx9S2zU8ZFJTQiNl3S7cGB8gQfbvKrb6uBfEXzIgvU-mrIrs5y5k7wJt6tAXip0794Y84-VF5iQpvv64hxEo_N3aqUQwQjHlxPKOgiRpuVBipdUfF06tJRwoGBYZFofLjGmYPGn_0jB4GZD0OenovmKnXguiChEVM5qWVPGygn0BTzvVr-n2xWX8E8KGXmAOWeKPxlGrEcUU-AuNzcSNadZC62XjeMj_P3n_iAa2ke9GvAKOLamf790mI406cAr-IeGE3QmVW-_fxFHN5MMeDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/7017" target="_blank">📅 11:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7016">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8CH8UA7SIoTXIYf1LmvVbSMSCTwIbryzCFciYVYv7HNuGVUf0-qP8x0Ryxc1RsRhX4w-ZaWkHvnDODJ0ofhLnR2pHuyHH9HHebhT0yPHXtzsou83_J7glfslY31pAyDtiv5oabFUSxvWUbAf-uGILmIqRe69Dg_R3AxUSvEIiJWOShoWZg9-g9jaWVX2zLdDcV_Usv8vUQxVq1lZYGn1_4L-rzU5dECnzx9Sly83SAxWaLceBVHTiPiC7BJgvSdp5OCQ7wwxiBospPfqiLDV9naTmSCK-dF6djTykSAKl_MxMQCUAIgS5Og5PKX5DTuTSqkBlt2rMdPj3bacYbKmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7016" target="_blank">📅 10:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7015">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qw1d-UBiuqh3rz9MMYwItP4P3EK9Ynp4fWv5HtjTvmqWxCw4LNl2OpWhJQNcVxTldd911lJs5eQWednPxcG2Tu-1J1Uv4CshE4U9wKDlNmBMvaTdHPFCoz7MbCTX-wY4EzapA1pGGjm3LXs4b8VjxjcwQIcdRgEGnl5w4kv-B3fyYeEDZW9Kl9gwth-OZNQGMvOEZux85wx2CYIikzyfgozBIDjXK-L5VB9LzOV0FKAia9o36zmT7VCaJqFwjXdloLcqvGXpudtOY_DKVJh1npHuz0yGxaYntP4GR2D8TszVpDcBss4QJM8qHR1YJqcKEB3_nZOeosWsRKIJ9si9aQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7015" target="_blank">📅 09:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7013">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6514ad748.mp4?token=JohjPBrHpXboQ0eXUhAoWjgKblDa_QJxXuD16hbyIYusC1e1Ibkwk-pgA2ttFK2EUxEHLl-yZlhqXP-bZ-pw5RwVaEQgsKU5g3QK015y_Ig6l3T4xAM-fZWTMvUnSIadt2vL0fJNFG4I5k2zg_kDYx7KxTubG5ZJUPEpUBSWQbiWVz0T3tjqBSsmRCTfGkvwO8tBw8ZJvzUPYRmavEbLu8TbvV6ucZhxePh80CnCd0J0D4ladC_TkmzgGWjvG8Zs5PEhQTimhI2EpRCIhhMxA3iLaRXVjKbalCg2z_j7aL6JKi1wIbdgHdfQkQQR3UTu4xQixvVH605QJyk5xKw0Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6514ad748.mp4?token=JohjPBrHpXboQ0eXUhAoWjgKblDa_QJxXuD16hbyIYusC1e1Ibkwk-pgA2ttFK2EUxEHLl-yZlhqXP-bZ-pw5RwVaEQgsKU5g3QK015y_Ig6l3T4xAM-fZWTMvUnSIadt2vL0fJNFG4I5k2zg_kDYx7KxTubG5ZJUPEpUBSWQbiWVz0T3tjqBSsmRCTfGkvwO8tBw8ZJvzUPYRmavEbLu8TbvV6ucZhxePh80CnCd0J0D4ladC_TkmzgGWjvG8Zs5PEhQTimhI2EpRCIhhMxA3iLaRXVjKbalCg2z_j7aL6JKi1wIbdgHdfQkQQR3UTu4xQixvVH605QJyk5xKw0Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7013" target="_blank">📅 08:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7012">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHz2XytyoDjiP7XZrfJf80I_iE5TAltoyTK1Zfg9BXx6Q1OLA18bZo0PqDPrx7Sy7yrRiF_HpqhEU2rm0UcXeFdyAKVntzpGB9r5mFXCAD6MuWT4oXwLTEOaeJA7pkD7kGqczjRJQJ4kMmQuV6AUj0vZ525zvZElMawM0P_Bqmwo_rA7zQ8zD8OkfP9_0Rb_GJWHG8bAtNV4NX-hP4R71xbpMBODgPOVSdxAK7NtsrDLpb3VDt43RaHOnAJJhlsuB91p9Wj-rXshOlULLOYBfx3suvHMeMj2G8h4CJ0qAfJDpN9tFyb-yZf465k4NhlgXzYTOK95IU79JjqJEpPbrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7012" target="_blank">📅 02:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7011">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fi7jRVJ942TvK8o0UUS50V1ADYjr-4OIBtHdy6fa69c1bBZUaBrHVMeNXDZ5yaCK8ICjXoPSAP6Ezvp_Vy8HFOw6wo9UMma6-zI3qgRJMaXL4qUJ5aq_b0u1RFQ48Gyizm5lrnoERwujNC_gGAsc378S_gtPguzU1OAfvSpPLt94Rs4H22cQTFxc_VpbXWLykjMHfcOxZUxwsvuRCuNo42b7Uejy_9OKBGjFjFuc5baEpWnKOWyWhC-KlBSqZu6E_lQ2pDb9IW-cB5nuTqKW_kpfAVseid-NhCGpnwCBHx1u2FTg-6Bzr6FbU8wku-dQQTZiwRpnyDV3vKLBHwBcDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار از زندان DeepSeek
👇
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7011" target="_blank">📅 01:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7010">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🛡
آموزش ساخت کانفیگ Bepass (متد یوسف قبادی) روی Nekobox  این روش کاملاً با پنل‌هایی مثل نهان یا BPB متفاوت است و با استفاده از Worker کلودفلر و پلاگین اختصاصی Bepass روی نکوباکس کار می‌کند تا نتیجه متفاوتی برای دور زدن فیلترینگ به شما بدهد.
🛠
مراحل راه‌اندازی…</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7010" target="_blank">📅 01:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7009">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🖥
نسخه گرافیکی ویندوز فیلترشکن Aether منتشر شد (آپدیت v0.3.0)  اگه یادتون باشه قبلاً ابزار خفن Aether رو معرفی کردیم که بدون نیاز به خرید سرور، فیلترینگ رو دور می‌زد اما محیطش متنی (ترمینالی) بود. حالا ابزار Aether-GUI اومده تا همون قدرت رو با یک رابط کاربری…</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7009" target="_blank">📅 01:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7008">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7008" target="_blank">📅 01:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7007">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUcAiSBEfsGVDF94NRjiuYdk8mWsPqqGV5HLUBUa-ebWLxSN1sdFxylKXG5lp9rGWgPOGmTHn7aA4W7t0Y6J3p8B4xeACwDUh31K4j3jjOpHusTM0DTE6pd5Duh5HyXPiSeZJId64weD8G_sTMBjEUCHanCPUJAr1jllwOTxzddBVd1VKXTRkFeO3ktg0Qx8b5hXUJkAx02XkxleksgZ5_34s0aWHvRTQV-ytiLX7nl-2kE7WT4ER7vRZW4BxWe25UEZUc-potmadybgk2lYk49JxwlTxgV9N3zS4_rbeMhPNmC0qjkX-BsiDPUFrEb0UGl-tRJMemGB3CvIj4RRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید و خفن Aether (نسخه 1.1.1) منتشر شد!  تو این نسخه کلی از باگ‌ها برطرف شده و امکانات جدیدی اضافه شده که اتصال رو خیلی پایدارتر و راحت‌تر می‌کنه.
✨
تغییرات مهم این آپدیت در یک نگاه:
🔸
خداحافظی با اتصال فیک: مشکل وصل شدن ظاهری برطرف شد. پروکسی SOCKS5…</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7007" target="_blank">📅 01:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7006">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🌐
پروژه Aether: ابزار ضدسانسور بدون نیاز به سرور و دامنه  پروژه متن‌باز Aether یک کلاینت شبکه‌سازی برای عبور از فیلترینگ‌های شدید (مبتنی بر DPI) است. ویژگی کلیدی این ابزار، یافتن خودکار مسیرهای ارتباطی است که شما را از خرید و پیکربندی سرور مجازی (VPS) بی‌نیاز…</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7006" target="_blank">📅 23:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7004">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7004" target="_blank">📅 23:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7002">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-rzE0ony8ZchIM2DvadkCr_sdXIQFsUDpkzgWf2B8-ncUl8Mx_CxfioZd-zMV6hVN7zrNJc3aE00JKFWn9OSsiD-y8gsIFoaaq20AOEozDGrZ-DD-cZVu8G1eGK10EOhUQvQNX1gwQCgXlOFtHJUIeXTrVp2raXRiOIcHoIRPquPDAu27Uqb5YfHsguMVDiLJ-KmIAf-vZqidphByiBw6goeUrfWNMQFpJa8pI0vdAWZ242JkZaa2zLyF-dy2DgqUsto2BTl6zYfxFOufpfTUTILAmP7WLcyIZI7AQZ9cCusHgMibwTu4p5krSrVk0_j8q7u65BWKNXqCBBCyWmwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7002" target="_blank">📅 23:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7000">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ1zm2YPJa5ShJht5YIN7P6Nc0girzwghmDNRuv33x9kvgJAp7G3hyzP837fomElDhtBpJYpv34sF698UWHIhal-awxTyJBMq65VWMzeOUOc6yPl1GIyE9l9CfpOkUXuwT6sbjuKXez1RBVEtI8ubq3cpikPKKiLBSVJeP2pN-l38lsfKy5427lj-OSgxbER6PXo1YMf-owwCN1seh-sPdLyq2wFhhGReIgx3gjUq_JwmScpLPVm4yISiS6UQ0SiJlS0GhQTkbOO7LQ-_X2KOH72McTi-AMdGfqp30QFjEs3Y46RPVPqLruMXoPd9acNL9jt6k4Mjzlrw8z3yZOQOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7000" target="_blank">📅 20:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6997">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fu3dfSfAd1GlhEt_GiuM7hFMfl0RQkgUCWWKdDXh7WwORttdlnHQTgEJl-M9m9dOWYfwurJOnbBFofGk7zBs99y9pgg7cksWf3v_KIE9bwzwLLsKg7iIbOI-AYVnnDxzcMX8AxQyMHN62Wx3hUnBPFalKV-d6eaE_ZxjOjVKbH8v-2CWQ0RhSN-bI5KP-wEfpo4k9QqXJNYVMEsdU1eixsKYhibgsXnMkRm6P6wrQdJUQyYO7GJy6eHAMCEXnZh7rhSz9ETXYHdwVMjiDAKEVU9B7raYdsT6EB8x7XH4LSCX4c2Jcf2CALM5pA9c5b66qUk_2IfoFDrhH4BaHwbubQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vxpt284K43htCxYyUhTU7gMXfGc-GAFEdzO1yy5chWBHxifQFlWg5I-DFeI-H5rZnFmMHL1uxC0GJ8EOpmOAgVsvH0YRYLNDdZfbSpI_n3PoK-ginpsPhus6zq7AB4_vVZ8IEGVJavRjwuXd2EwLpbT2UhFiX52tEaA-NWqabMcqIaXTyXD0b_x2o8gGYM4LIS7uO9bNvC7k89I13IJXz9mWe-w4_hHYkQ3sCcb7pwPCVHXzZ1LATVsoh375A0pZLIkGWB1w2ynm0Emnn-d8k85bXOeh9zrl2CJpd7hZdAoQL-6vVdukVFTNK043j7LJaJabYozMxPRW4mfasZegYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6997" target="_blank">📅 18:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6996">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRB2eoIDB0nbdl9qmBum5Q8BKQI42OuGELFso4k0aU0CnOJbRJVE_r-8ISkHalmrobJETi8nVmYV4ivSJDHH_rS1IC_pLnAWTMQzPWZLsn5iG-a0Ng2s4nV0v20hGvaZG2oaMf4nyPlU5AtwYDUVIZM1L51lm_PZ6jL9LAIdZigO9I5OwGF7AQd_Cyx7EpXdcWI8YcCBl-ykMcHYVjtelJseWz4bT4cJUgPNx-QOWzd4V5FJCrdPNzFv0AVfCbzUY4b5vcX1mu2AC8tRgKv1ZMdq_6AMlw9jNYlgpZPXq3WSPGWhBDWjKwjt35QSgrj_s8EDwC7t_THhLHa965JhlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثه آب خوردن  کلا ۱۰ ثانیه هم طول نکشید
😐
ولی وصل نشد رو ایرانسل برام
😐
😂
😂</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6996" target="_blank">📅 17:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6995">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtAnmzfpAU7iXR-d69_yl_uXltjcngqAy8vIoH1KPQ1Fqu5UffKh30OaggvjW2PIUZJ1CQHRW38lnsxt98-ZPsM4up_Sg8uKjG_YA7s2rlCAC1Aie5VQWWyB1Ks5wH0YwoUhyqM8z7aSoSiBUoYwehkuI-1qVxO_sniwKJczHYr1bNsVAPyBHQwlHuYndY1NIUk92wqUdnv6ARxsjZVonQ6cD995wIbJRWjeMgjF1wZ7p2GIPb7DiugrIPOZl8LkVcw19VeydpjBNHFhyLvRxE_Z-SnRPES3jOJFSDRK3pwlznAWeBnNzfOmKVeG7iqupRXZv657FpyktLoLH_s3lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
پروژه Aether: ابزار ضدسانسور بدون نیاز به سرور و دامنه  پروژه متن‌باز Aether یک کلاینت شبکه‌سازی برای عبور از فیلترینگ‌های شدید (مبتنی بر DPI) است. ویژگی کلیدی این ابزار، یافتن خودکار مسیرهای ارتباطی است که شما را از خرید و پیکربندی سرور مجازی (VPS) بی‌نیاز…</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6995" target="_blank">📅 17:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6994">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6994" target="_blank">📅 17:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6992">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2SLK30qHe8ktvjVtHjVVwakiBKJ0eXXUGZrwX2_Nkp2gMFyVQtqtdUqqAhl9QkjOi8cGVpY_f29LGSUHJVeEhl4Xh_ze6vcavowZpLopDzJeP2khAl1IqwBBwop92LLykHDcjaRlt_NxFiNPbj4K3W7hi26tbd2uEt733BSNNRR8dF2T7_3KeuPQdjmdrqXGUw-DZ3VBQcf43akchVjbFwhYtPviJOc1yDf-sItOkWJMErIDBkKBOCNTJCDpBYbS3AOddByhBqLfA_-0znRLMb3MWmcpfEdBAvgCFrehcHU_pcSEXX2lZKO_yqb7gy8p1HAl9UmzDAAZngADpa3wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☁️
اشتراک یک‌ساله و رایگان MultCloud (ارزش ۴۰ دلار)  مولت‌کلود (MultCloud) ابزاری بی‌نظیر برای مدیریت یکپارچه تمام فضاهای ابری (گوگل درایو، وان‌درایو، تلگرام، دراپ‌باکس و ۳۰ سرویس دیگر) در یک پنل است. با این ابزار می‌توانید فایل‌ها را بدون نیاز به دانلود و…</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6992" target="_blank">📅 16:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6991">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-dOY5S7Uxv5kIABmbEUW3s3moVG8ZnSJ5Je6c-tedcqgBjXS4bJqhss_dygbchNvhmsMyyLHmZ4fdeRgg1c_PV-ZnPicTS9q6qbT6FWoFVanr6VwubSMYqDS5ZEiFoy3ZLWBedUeNXbJfS0RoYl8WAAOBjka6ors3PUdZoO01KVdYqx8SD3ug5birheVNSwbpTUqhaeZZ-7id07k_prwZpiIjOLN85cMsn6MWSE9m_2J4ZEJT9utJswpXSVFpyoVx5n2cdEPFmaJg87WpV8ZR8CLoaGaxRC0z-oeylqCv0uD2VZR5gySpvW_9L1yWP__6epOyV0uRpx3qVTdwoMzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6991" target="_blank">📅 16:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6990">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5760952ca.mp4?token=ZX1xpgjaUYpr-ml1rKQnIMlqaeGtyy2t1rW2MSfoOCN61SmFJhHW3gu4cukYW807fwODjkj1ysW-K40zISdxX6WSXKMuEM8PKtGYouL0D0VdptoHS_0g0YvWj9Y9O6oTFAOBxB2nf5MLJLM6ZFRflOqx4TI9cj8aBpr7eF0Rkm97kMDlpTZzO9hX8NnsaFzKsFDUsncvZmlb5ed_iu3_8xkDSGMS3pMIHDcxoVVHLLhEj3qU7V24RjRScz_zXbjEhUmuJYJA-EcsrmwxcQ-SeilkYeYmS64Ry_x1N-YdRjuqp9_YAgwr9-6h2rg7rMIA1vf9a_Istw1K9Qy2Nmkmug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5760952ca.mp4?token=ZX1xpgjaUYpr-ml1rKQnIMlqaeGtyy2t1rW2MSfoOCN61SmFJhHW3gu4cukYW807fwODjkj1ysW-K40zISdxX6WSXKMuEM8PKtGYouL0D0VdptoHS_0g0YvWj9Y9O6oTFAOBxB2nf5MLJLM6ZFRflOqx4TI9cj8aBpr7eF0Rkm97kMDlpTZzO9hX8NnsaFzKsFDUsncvZmlb5ed_iu3_8xkDSGMS3pMIHDcxoVVHLLhEj3qU7V24RjRScz_zXbjEhUmuJYJA-EcsrmwxcQ-SeilkYeYmS64Ry_x1N-YdRjuqp9_YAgwr9-6h2rg7rMIA1vf9a_Istw1K9Qy2Nmkmug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6990" target="_blank">📅 12:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6988">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6988" target="_blank">📅 12:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6986">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6986" target="_blank">📅 10:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6985">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9mA-VsaAckJSAmidqPZTR1ay--4CMXw39MAMSCSAvKdAQ1562BjuBuGu2o_JpVH3MLiroYfSmzJ7kEVrPOetOgVwZitjHPckUVfPzEnTE_KSclOIuzFncSTgtd5yNqp8SzIOkCYj35FWQfS8rbZcclR3MPZD0f3g3lyE4kU7Y78AUCG9XnLc87ftFywTKKOnSVHCZ1p6WQ-o3Y5-ToTuHRIl6NW16HGWa5BSJJhBPwMXVUN5Jey4WvqotIjsgZeWJ1qaWy2Fud9ivhcWPCMuxk0FZVNee9XrNsc6yiEXRjPi_oDgwoRMFLhd7KqL5TAxdva76npaBYH5aiwiq3cpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6985" target="_blank">📅 10:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6984">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJPLy0Z7Vfx3_ci36Y4PryfV734PCNbv7gp0LHoJwtdwpKLXGpZE8mBKH-4L3pgsjEME26qqhHE-lp_rhzuVSKEhFV42TM37NdTQAdxrDMhKDktmnewCPu6q3MH132v6vZW6crfIuNPxdgg9Ce1mXTEOvW4lJYx9N-AqSZ6f5dFhyXKa74nR6Edht9w__E3EDpNNP2e6wAwLlXkoPdlGGmepe2OS31v2slwaHCvmJjUxs_xdTc5hj9wDwzHR6Tid0HXdPC5B-DcfF71PvOImJFv1TYZivymMFDpcGhgqs4Asb1noOuuwUY5fjXuufubyzaJvpDkcuYvdQ0GiplDJAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6984" target="_blank">📅 10:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6983">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnCdX6nAi94gDX5LRQo2Xf0jvjxlq01BdBxraQhrSyDt7_A0-BCWxAiv20plnEA1bZiiAaRNXr-tXeE7Zu7gqMoDAmD1pAf3YyA9YxzTEg9kLtun2EM2ZWVg2BAVTGZpn8IhTWxDRdl_nL9M5KfZePiOqvibZ5rXruuLQccg0H0QvLrqR6I4o_rczH3LVG8xlUlvlqNJ4Fjgq78Jt6D7_kkdIs1wIbPL6O7RfCQyxnZcHyCL9ZX9C-wByYW2nwZsVN1g-9uqn_ci6x1aQ9PuTlOxZPrXjox4Dcaew8krtWCrQ6nmvQse3lRmc9Hkh6xRZj8xHZSuL5S3YNTYE4hg1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6983" target="_blank">📅 08:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6981">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏
🛡
مرورگر Cromite (کرومایت)؛ جانشین قدرتمند Bromite  (جایگزین کروم)  اگر از طرفداران مرورگر محبوب اما متوقف‌شده‌ی Bromite بودید، Cromite دقیقاً همان چیزی است که نیاز دارید! این مرورگر یک نسخه سفارشی (فورک) از کرومیوم و بر پایه برومایت است که با تمرکز شدید…</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6981" target="_blank">📅 02:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6980">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6980" target="_blank">📅 02:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6979">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6979" target="_blank">📅 02:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6978">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6978" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6975">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cenp58LFO5FkOMf5N3lnXPpQ3qyghREno-0Zs5gIjm-RfVRm9ftvOzdgWQ-0P3Mst444h3okIk1wHgRyU0PlBst0mk07XSBzEjZoi9M_bvzXvaSZ_VpqXqgbBvxLoPuewW3-ajX4jiegMqlLKlSE97cbwyXRyb-Rs6gIx4ajavXbWyJTnMg9La4Iq_F8NCPeo426TzUbbV6XDx_MUY4Bk6lw-e6Cm8YGDP9ZhN7e1u4TOSJdz0hjwn0hAJez3eiawhaGXT0v2cFAn65t2YEFzOQ116L2JJMInV8iceVbgEsKbEudocrQMeNY2QoFo_kBTXYFT8t0Py5wwDFJ09Cl-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6975" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6974">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6974" target="_blank">📅 22:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6972">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulCXLGSS3RNVUod1A6kBL8R5Ec-kSqASHSUFbodIgHXmsmpYJL7qIQFSvUD2jMyJ66aSrnuCRHRb6u3JJLLMxUS_vYXcMlN_brRAv80aHWjZNOYUa0eGAdmhWvOdr8ZkBmXl4ImU13_1OcEV0-2tVKXamEZBdWFRFtqrVjj5H7PwGVqJBFN6aAcZRQtsjgcIiVZvx14z4YtWsTCX2N_Yobe_xqjLPcEQHdUu11ChmhTDNLJWDhjOPCQCqbVh4FygOwVfhRivjRfhfLuoZ6sZquu0YBY79B_9bGeWqDWvWZ45iBmLn5ZswBBS76qpjRY0g1a-VVNYGOMo-LmgiVkoAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
3X-UI Manager
مدیریت حرفه‌ای پنل 3x-ui در اندروید!
✨
امکانات:
🔸
کنترل چند پنل همزمان
🔸
ساخت کلاینت و لینک ساب
🔸
نمایش زنده منابع
(فقط نسخه +3.3.0)
📥
دانلود:
F-Droid
و
GitHub
و
Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/ArchiveTell/6972" target="_blank">📅 22:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6971">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgWtwdP4z9JVV_8-XPs8fj7PJ1z7Lwi9zLf1hgiGRF2DmYPa9J6UbC9Vheu7-KwchQdEA0z4fLOoPCKbrHYUenzkdIKo1kIXGr3w6q0CbJRBVAmYRaScnx0EuzyYHiaVlF8p_QVd_O6MqpIbSpjnFTq8IkLJPLJE8UFBfNnwi_MjlvLQTr-LaUmiNs4IoECM_5AOhmqGC3LRLMwj3ZnoQBotLHX1vsgprLJ5FfI04ihfMIy-E_1kNnM8NeZaE2YnWGCC2KhtLSvIflEuczhzFik5_UNsd5zNNtyMYKI00k19RsueQ8FCHV9xncon28IEXSKQYOehMwz96vRGoUxn0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
Droid-ify
یک کلاینت (رابط کاربری) مدرن، روان و فوق‌العاده زیبا برای مخزن بزرگ F-Droid!
اگر از سرعت پایین و ظاهر قدیمی کلاینت رسمی خسته شده‌اید، این اپلیکیشن جایگزین متن‌باز (Open-Source) دقیقاً همان چیزی است که نیاز دارید.
✨
ویژگی‌ها:
⚡️
سرعت بی‌نظیر:
همگام‌سازی (Sync) و لود شدن لیست برنامه‌ها در عرض چند ثانیه (بسیار سریع‌تر از نسخه رسمی).
🎨
طراحی مدرن:
رابط کاربری چشم‌نواز، روان و منطبق بر زبان طراحی Material You.
⚙️
نصب و آپدیت خودکار (بی‌صدا):
پشتیبانی کامل از ابزار Shizuku، دسترسی روت و Session برای آپدیت برنامه‌ها در پس‌زمینه بدون نیاز به تایید دستی.
📦
مدیریت آسان مخازن:
قابلیت اضافه کردن و فعال‌سازی مخازن جانبی محبوب (مثل IzzyOnDroid) تنها با روشن کردن یک سوییچ.
🧪
نکته:
این برنامه در واقع یک پوسته سریع‌تر و بهینه‌تر روی همان دیتابیس امن F-Droid است و امنیت شما را به هیچ‌وجه به خطر نمی‌اندازد. اگر از برنامه‌های اوپن‌سورس استفاده می‌کنید، نصب Droid-ify یکی از واجبات است!
📥
دانلود از GitHub
و F-Droid
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6971" target="_blank">📅 21:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6967">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aOGunqG7Tinr65yYPySXYxO-8r80drnGVthD532v5Xwnj495WpevTL-HS-SN8sD0gr5BaNK0jT3goQxFWvtp0BXcOdeabCJ7AjevpArbBUj3sZQQbZ73j9Bo45nauGqCDYywxJ3YVAlh8h83nxcqHRLjk58DxbcyiXYFDz2MU341nyAdCOigpQnpoKWp4Pic-yjBFrAiHmyV16RI_a85fQOFamieiAQAdwJnmFtbsm6ci5GSGCAmLfM8i_MLQCTPy5BDgos0Vg-ah8KUWrJGMYvsB4jxpijdD4X2jD5OZQ5ooRMAqUfqhWGsVzUacakCIIXkQkxwW5UpvDcSc_rsnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WelWPyaMV0R2GpoQb_AaVadXYYcGiEDv_bpYZOIU4kZG7o0ECku5dfOagYnIYpwK7pn34t67CYEg7R4edfZqU0ivzHGwWxzbnae2H_IWEBC6s3kz4Lv6UWHqoFyFhP_iLBb_OIVli0odPU6dLv6K4INgYLWc13IMvPIKqOWxE1MdUobKYMrv-Dn-H390m7HY6IWvV8p_YuUu51liIe7-WM7jLq9E0lRWId1f0neWZ8Us5c76Qd_KbMDBG4nn2qIEl0oOh8nFa0kWXDcFLRJdnM2HAcro8Bh3CI2SJPwyFEKHU07QSNJeFvx6yscEKn6dzzlwRF6vnW9xlKqnxoo6Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rgxw65jcUB5-kXWm5yEgf6aEwbrSgwVzzuMx7Gt5cxV6jLYim1G11IjAwI8qwn20zXqVFgyBLxhmb_xZuQD15rckZ0Oa8prg7XZKzUBeZZBbmgT9r-aQwiF2t15MYV90K8Y2JRHM_hOFK1i9DWU0et_tyelxJih-1snnqUpEp_8uwRvTwxs1W_VAtuVcGanZTvn2bT7w2m70Ifbn92bmhSsUG4NgSm3lzWXJY8DVVVVcHH6X-N_3Yh8SvwoSYW7lraimpc5i-cjl2B0kylJFUNJJ6E975NWfHo_VRYEXSM7Ddsd0_vlbTmiF81XGzPWQw1Oh9rFYxhzxFSjdAASztA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wA9T5rhdjhcCrgqEMiX5UOBMCH6kGDDHy2OhfRR3UU01c1TOP7H4XjyWw4JpgTvlFTq-Mlo5LqORyBOgZkwYNEONxREMr0gqQUPRYflR-I5GggjKS08VPRlpYUXTroIDIt91t6hsq0CzTy0IMtT1tY_JBG8WQWVX4fCScrBVv5nQ8HWvYazJouiXEI40k_YRuk72AeePBR4B5UZPPGjZvV9XJtbxaQBEEqAnd3BH76AvsofmQvRmX891_g5OMzd_OITVPGBEsLIsxCR6Df3_dCJwdMRBVtNbDdYXylaL-hVHIj1p1EnuQYM5Ryuv6KiQxvHcAk3i2hf5HCGKOh_sdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🚀
آپدیت بزرگ تلگرام با ویژگی‌های بی‌نظیر منتشر شد!
تلگرام به‌تازگی یک به‌روزرسانی عظیم دریافت کرده که قابلیت‌های کاملاً جدیدی را به این پیام‌رسان اضافه می‌کند.
✨
ویژگی‌های این آپدیت:
🌐
بخش «انجمن‌ها» (Communities):
فضایی جدید و یکپارچه برای تجمیع کانال‌ها، چت‌ها و ربات‌ها در یک مکان واحد.
📝
ویرایشگر پیشرفته پیام‌ها:
ادیتور متن تلگرام دگرگون شده و اکنون از ابزارهایی مانند
جداول
،
چک‌لیست‌ها
و
عنوان‌بندی (Headings)
پشتیبانی می‌کند.
🤖
تولید محتوا با هوش مصنوعی:
از این پس هوش مصنوعی می‌تواند مستقیماً بر اساس درخواست شما، پست‌های آماده و کامل ایجاد کند.
🕵️‍♂️
پیام‌های خصوصی مخفی:
ربات‌ها قابلیتی پیدا کرده‌اند که می‌توانند پیام‌های خصوصی ارسال کنند؛ به‌طوری که این پیام‌ها حتی از دید مدیران چت نیز کاملاً پنهان می‌ماند.
🧪
نکته:
این به‌روزرسانی به‌صورت تدریجی در حال انتشار است، بنابراین ممکن است این ویژگی‌های جدید هنوز برای همه کاربران فعال نشده باشد و دسترسی به آن‌ها کمی زمان ببرد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6967" target="_blank">📅 19:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6966">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zhju_XuhiIxbl39QyPLTviDhWi2sU1unqlav-35RPGEunXUUMBOVTDvwU2gR95gdcThOw0qqH-KzidoCAiCk5u5otiRVstzifZEE8GlU_lv3ualcbkElJnWnOQHCO27U6wYsclVfW33zcXcU-M_z5FkYwBKup0zRQj-RqdAi3MBCzaBE-a_LU7uwBUpzPwZCoqKPyCddBzwbAZ-Fn7MK9fzknm6lQKQbj9jXOy-pa8J9Hlk-g1tn4DsBaF4a5MmgQVR6KCCFnqdN_t7uomkvUacdyjWHAUpGyLFdCKS4SqBs8Lcwy3K3DZFrKounZN0fvqP1R18g7PKo3C5kyc4DQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
Acode
یک IDE تمام‌عیار و ویرایشگر کد بسیار پیشرفته (Open-Source) برای اندروید! با این اپلیکیشن می‌توانید پروژه‌های برنامه‌نویسی خود را با امکاناتی در سطح دسکتاپ، مستقیماً روی موبایل یا تبلت مدیریت و توسعه دهید.
✨
ویژگی‌ها:
🎨
پشتیبانی وسیع:
رنگ‌بندی سینتکس برای
+۱۰۰ زبان
و پیش‌نمایش زنده (Live Preview) وب.
🛠
ابزارهای حرفه‌ای:
اتصال مستقیم به
GitHub
، مدیریت سرور با
FTP/SFTP
و کنسول داخلی JS.
⚡️
قدرت و سرعت:
اجرای روان فایل‌های سنگین (بیش از ۵۰,۰۰۰ خط کد!) و پشتیبانی از کلیدهای میانبر کیبورد.
🧩
شخصی‌سازی عالی:
سیستم پلاگین‌پذیر (دارای افزونه‌های هوش‌مصنوعی)، سازگاری کامل با تبلت و
منوی فارسی
.
🧪
نکته:
این برنامه با مجوز MIT منتشر شده و دارای قابلیت بازیابی فایل‌ها (File Recovery) برای جلوگیری از پاک شدن ناگهانی اطلاعات است. (اجرای آخرین نسخه نیازمند اندروید ۸.۰ به بالا می‌باشد).
📥
دانلود از Google Play ،
F-Droid
و GitHub
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️
⭐️
Cyru55</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6966" target="_blank">📅 17:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6965">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKinhi45oAUwrQhV4nki9FXgo1cravmyizZyaWHrqP_lgENUso7hDA4jjoMZlQ5IpIV_hTF-MQpkiu0MTVUmdpAXks4ewgHvLO3ISHIUZJcvSiH-LRvovnSQ76MvTF4mFyegcjLeRGBzR31JzxFc1Bd2sV-L8T-nQn9nlnlHmS32wmZe1dYPdgvfq-w7Ec6MvM5u13JcGlOoyCnXfj2ne5hmaw7inZhnY9f_cxxBtHDdV70cAR7ZymBYYEY1bsTyXp0Re_t1Tte9y4Xk7qFjNJdiEt8EgMnE_2PaIr2iw8Sxz5o90zkZmpsQGnayP-WJYAQgLJoKu6HWoauMXVRQyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
وقتی هوش مصنوعی علیه هوش مصنوعی رقابت می‌کند!
در یکی از آزمایش‌های جالب روی مدل‌های
Sol
و
Terra
، رفتارهای غیرمنتظره‌ای مشاهده شد.
🔹
کارتل قیمتی
مدل
Terra
پیشنهاد داد قیمت‌ها را با هماهنگی افزایش دهند، اما
Sol
پس از پذیرفتن پیشنهاد، آن را گزارش کرد و حتی خواستار حذف Terra شد.
🔹
اتهام به رقیب
مدل
Terra
در مرحله‌ای دیگر، برای حذف
Sol
او را به تقلب متهم کرد.
🔹
رقابت بر سر درآمد
مدل
Terra
با کاهش جزئی قیمت‌ها نسبت به
Sol
، مشتریان بیشتری جذب کرد و درآمد بالاتری به دست آورد.
📌
این آزمایش نشان می‌دهد که مدل‌های هوش مصنوعی در سناریوهای رقابتی، گاهی رفتارهایی شبیه رقابت‌های دنیای واقعی از خود نشان می‌دهند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6965" target="_blank">📅 17:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6964">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚀
مدل بی‌نظیر GLM 5.2 به نرم‌افزار Trae اضافه شده؛ کاملاً رایگان و نامحدود!
اگر اهل کدنویسی و دنیای هوش مصنوعی هستید، احتمالاً با
Trae
آشنایی دارید؛ یه ابزار و دستیار فوق‌العاده هوشمند (Coding Agent) که کارش راحت کردن زندگی برنامه‌نویس‌هاست. حالا خبر جدید و جذاب اینه که مدل پرقدرت
GLM 5.2
به این پلتفرم اضافه شده و می‌تونید کاملاً رایگان و بدون محدودیت ازش استفاده کنید.
🤓
من خودم هنوز این مدل جدید رو فرصت نکردم تست کنم ولی Trae کلاً سیاستش اینه که مدل‌های خوب رو رایگان ارائه میده، اما قبلاً یه
صف انتظار طولانی و رو‌مخی
داشت که آدم رو کلافه می‌کرد. نمیدونم واسه این مدل جدید هم همون بساط صف برقرار باشه یا نه!
🌐
لینک سایتش:
🔗
https://work.trae.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6964" target="_blank">📅 17:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6963">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏
🎙
Voicetypr
ابزار متن‌باز و قدرتمند برای تبدیل گفتار به متن به کمک هوش مصنوعی. جایگزینی عالی برای تایپ صوتی که در پس‌زمینه سیستم‌عامل اجرا شده و همه‌جا در دسترس شماست!
✨
ویژگی‌ها:
*
🔸
تایپ سراسری (System-wide):
با فشردن یک کلید میانبر، در هر نرم‌افزاری (ادیتور کد، تلگرام، مرورگر و...) صحبت کنید تا متن بلافاصله همان‌جا تایپ شود.
*
🔸
آفلاین و امن:
پردازش کامل صدا روی سیستم خودتان (Local) به کمک مدل‌های Whisper بدون نیاز به اینترنت (پشتیبانی از +۹۹ زبان از جمله فارسی).
*
🔸
سبک و فوق‌سریع:
توسعه‌یافته با زبان Rust و فریم‌ورک Tauri با پشتیبانی کامل از پردازشگر گرافیکی (GPU در ویندوز و Metal در مک).
*
🔸
ویرایش هوشمند متن:
قابلیت اتصال به API مدل‌هایی مثل Groq یا Gemini برای اصلاح لحن، یا تبدیل صحبت‌های پراکنده به ایمیل رسمی و کامیت.
🧪
نکته:
این برنامه برای ویندوز و مک در دسترس است. در اولین اجرا، به حدود ۳ تا ۴ گیگابایت فضای خالی برای دانلود مدل پردازش محلی نیاز دارید و پس از آن کاملاً مستقل کار می‌کند (برای لغو سریع فرآیند ضبط، کافیست دوبار کلید
Esc
را بزنید).
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/6963" target="_blank">📅 16:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6962">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZUwZuH7XxgmXRBuAYS_xkN6DpyUMkVfPTRUful8Tx6YZXF_0wJvJnpvDr3qWLDaaganT-NQ-Wb_bI979Y5mlXvQpo3iWYOx74WgjthgaB_vthlC1tSg6e4WdxkZNKrOxSBliNlPkv2FAbV1JgW0rfqO763IkAuSds0P2__1_qbi-L0s4VmiRIaaMGGz9Z4TB_aPXRkdO65eRAVlXnnLT-1Wpd56XgAVRPzczZ9n6KMwa9UjGL3y0Fiwjvyk4RESGnfZLis7VduN_PdwnG99c1Emx5o7n530ValgPSwMZkxnYQxlrmdPQbMUBWAB_rba8bF7QvKc7uwlc7H-BFf_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
TelegramOS
پلتفرمی یکپارچه که تلگرام را به یک سیستم‌عامل کامل برای کسب‌وکار شما تبدیل می‌کند؛ تمام ابزارهای مدیریت، پشتیبانی و توسعه در یک داشبورد جامع!
✨
ویژگی‌ها:
🔸
مدیریت متمرکز تیمی:
کنترل همزمان چند اکانت، صندوق پیام مشترک (Shared Inbox) و مدیریت سطح دسترسی اعضا.
🔸
اتوماسیون و CRM:
ساخت سناریوهای کاری (Workflows)، سیستم پاسخگویی خودکار و مدیریت پیشرفته ارتباط با مشتریان.
🔸
آنالیتیکس و مارکتینگ:
ارائه گزارش‌های دقیق از عملکرد، تحلیل کمپین‌ها و دسترسی به مارکت‌پلیس داخلی.
🧪
نکته:
این پلتفرم بهترین گزینه برای تیم‌های پشتیبانی، فروش و بازاریابی است که می‌خواهند تلگرام را به قطب اصلی و خودکار فعالیت‌های تجاری خود تبدیل کنند.
🔗
وب‌سایت رسمی TelegramOS
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6962" target="_blank">📅 16:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6961">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0feee0c240.mp4?token=DYqKXbfJqLZsiiiTxkyEf5Jhv1WtHcnOg3yACvZhfdRIU0K7ImGUBp7m8LGSI_zcZ17n3yMU1PjHlwS-Je8hpwDSBaanfsdIcMV1rwBSVXzYQA2wQsn4j4e_nYOdJtefaMQfe9fJcSeQI_9Mq7iMLnhXspKwOBnzpUqcwHxnpqqfy566IryTt34LVkdYkZZkRt3mblDIiMl_vaJdrjLahFZ1sNyYgvMjhMNpaOOwfipkrp6EkmzzCG9xfAlho-A0LpK_DnqwIh8d5vUrNItYdLOALdoMkhrs-1zHlWnMbIgEBorajskHiSPgFLefva2D4T_gNyH114_qOJuZkqNT7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0feee0c240.mp4?token=DYqKXbfJqLZsiiiTxkyEf5Jhv1WtHcnOg3yACvZhfdRIU0K7ImGUBp7m8LGSI_zcZ17n3yMU1PjHlwS-Je8hpwDSBaanfsdIcMV1rwBSVXzYQA2wQsn4j4e_nYOdJtefaMQfe9fJcSeQI_9Mq7iMLnhXspKwOBnzpUqcwHxnpqqfy566IryTt34LVkdYkZZkRt3mblDIiMl_vaJdrjLahFZ1sNyYgvMjhMNpaOOwfipkrp6EkmzzCG9xfAlho-A0LpK_DnqwIh8d5vUrNItYdLOALdoMkhrs-1zHlWnMbIgEBorajskHiSPgFLefva2D4T_gNyH114_qOJuZkqNT7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
با یک کلیک، طراحی هر وب‌سایتی را کپی کنید!
یک ابزار فوق‌العاده به نام Ditto می‌تواند در چند ثانیه، سیستم طراحی هر وب‌سایت را استخراج کند.
✨
امکانات Ditto:
🔍
فقط کافی است لینک سایت را وارد کنید؛ Ditto آن را تحلیل کرده و نسخه‌ای بسیار دقیق از سبک طراحی‌اش را آماده می‌کند.
🎨
تمام توکن‌های طراحی را به‌صورت خودکار استخراج می‌کند؛ از جمله رنگ‌ها، فونت‌ها، اندازه‌ها، فاصله‌ها، سایه‌ها، گریدها و سایر جزئیات بصری.
📄
یک فایل
DESIGN.md
تولید می‌کند که می‌توانید مستقیماً در Claude، ChatGPT، Cursor، v0 و سایر ابزارهای هوش مصنوعی استفاده کنید.
✨
بدون نیاز به کار دستی، ساختار و سبک طراحی سایت را بازسازی می‌کند.
🔄
حتی می‌توانید سبک چند سایت را با هم ترکیب کنید؛ مثلاً رنگ‌بندی و انیمیشن‌های یک سایت را با تایپوگرافی سایت دیگری ادغام کنید.
👀
نتیجه را بلافاصله پس از تولید مشاهده و در صورت نیاز ویرایش کنید.
📦
امکان خروجی گرفتن برای Figma، کامپوننت‌های React، تنظیمات Tailwind، Storybook، WordPress/Elementor و متغیرهای CSS را نیز دارد.
https://www.ditto.site/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6961" target="_blank">📅 14:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6960">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">موتور جستجوی مبتنی بر شبکه DHT بیت‌تورنت، که امکان جستجو و یافتن منابع تورنت و لینک‌های مگنتی رو فراهم میکنه
☠
http://cilimo.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/6960" target="_blank">📅 14:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6959">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-6DRPlHNY6IMh9qzAkBerPcs4qHkAQiZ5iSvG8WT_bCjl4nFi1uJljKxO87sO3R4ITiMIFjZGYSfrQ6tqDK24kjSxnEjgByHeLgsHxkFOl7-VR-nKOlWR35QmaOpGw1HsLh7-KTKzdwlYP4cu-bs8PV4I_TELkCIF2Q3ZNiQUzsDM57yi0xp9aZTki5SRBIQabPZhQk27HR3ybDiOSo2HCfjHlyBA-WQzRxr2mRWuHX2uX-GaS6SbP3nI1oWSwRBRL3OkZlCY4KKtNUv8sn5TWSnRnItDP9g5OeGe8QX-FP-e1r4RaW2Dm2MH6lC6GTXjluV07Y670nEa82x9BQnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🌐
Magnitude Browser Agent
دستیار هوش مصنوعی قدرتمندی که با استفاده از بینایی ماشین (Vision AI) به شما اجازه می‌دهد مرورگر وب را فقط با دستورات متنی ساده کنترل و اتوماتیک کنید!
✨
ویژگی‌ها:
*
👁
معماری بینایی‌محور: برخلاف ابزارهای قدیمی که به کدهای سایت (DOM) وابسته‌اند، این ابزار صفحه وب را مثل یک انسان می‌بیند و با مختصات پیکسلی کار می‌کند.
*
🖱
تعامل و اتوماسیون کامل: کلیک، تایپ، و جابه‌جایی المان‌ها (Drag & Drop) در پیچیده‌ترین سایت‌ها.
*
📊
استخراج هوشمند دیتا: توانایی خواندن و استخراج داده‌های ساختاریافته (بر اساس Zod Schema) مستقیماً از روی ظاهر سایت.
*
✅
تست‌رانر داخلی: ابزاری فوق‌العاده برای تست خودکار وب‌اپلیکیشن‌ها با بررسی و تأییدیه بصری (Visual Assertions).
🧪
نکته: این پروژه در بنچمارک WebVoyager امتیاز خیره‌کننده ۹۴٪ را کسب کرده است. برای بهترین عملکرد، به یک مدل بینایی قدرتمند مثل Claude 3.5 Sonnet یا Qwen-2.5VL 72B نیاز دارید. نصب اولیه به سادگی با دستور npx create-magnitude-app در ترمینال انجام می‌شود.
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6959" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6958">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQIBgE0TGdfGXDK_5ftjBs8u3bNhRDw0j0Gz808b2ifSRHSBYcAP-y6sC6cb8SwNcJi4SJ6KU5sO2gvlqEg1FQEjABZ2ytuzsXEoH1yZwUwMywTd3n3i2q-8KdiQ8wCaKjd26SzCmYUCxLRLiXgdUuu78QcsYYb5pMrDA--wmeRvVV5xyxavXBcxQN3RAygobDIsqEzdAt_4L8wU6ffaSW49GyLFfn0TGBDltGSUcZl6kPXXbq5psqfRXd8iH81SAeWlBf0Er4ISbm40whPSy2jmTPXbZspXgAT4McQ1CZO1mC10xBfIztaFLrX06C83mo2w_l1rm_s2_yGYk1esLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار چندمنظوره رایگان برای ویرایش صدا، عکس و ویدیو
سرویس
Magic Hour
مجموعه‌ای از ابزارها و فناوری‌های هوش مصنوعی کاربردی را برای انجام هر نوع وظیفه‌ای گرد هم آورده است:
🔹
تولید تصاویر، حذف پس‌زمینه و افزایش کیفیت تصاویر؛
🔹
ویرایشگر دیپ‌فیک با قابلیت
جایگزینی افراد در ویدیو
؛
🔹
بازسازی عکس‌های سیاه و سفید + جایگزینی افراد در تصویر؛
🔹
مجموعه‌ای از ابزارها برای کار با موسیقی و فایل‌های صوتی؛
🔹
تولیدکننده زیرنویس.
🌐
magichour.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/6958" target="_blank">📅 11:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6957">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">۱۰۰ گیگ کانفیگ اهدایی
🔥
vless://63dc39fe-3bc3-4267-8bf1-4069b47baa18@194.110.172.150:443?encryption=none&fp=chrome&pbk=3sRLbKljY5s7LCik-w9MqgenayhgHgLV0v9lmFGQ9TQ&security=reality&sid=3094219d2cfd2b3d&sni=www.samsung.com&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/6957" target="_blank">📅 11:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6956">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏
🤖
3xui-telegram-bot
ربات قدرتمند و متن‌باز تلگرام برای فروش خودکار سرویس VPN، با اتصال مستقیم به پنل 3X-UI. با این ابزار تمام فرآیندهای فروش، تمدید و مدیریت اکانت‌ها بدون نیاز به دخالت دستی ادمین انجام می‌شود!
✨
ویژگی‌ها:
🛍
فروش خودکار سرویس با حجم دلخواه، شارژ کیف پول (کارت‌به‌کارت) و پشتیبانی از چند سرور (Inbound)
🎁
مجهز به سیستم ساخت کد تخفیف، ارائه تست رایگان و زیرمجموعه‌گیری (Referral)
💻
دارای ابزار اختصاصی خط‌فرمان (vpn-bot) برای نصب سریع یک‌خطی، بکاپ‌گیری و آپدیت
🔐
اتصال کاملاً امن به پنل صرفاً از طریق API Token (بدون نیاز به یوزرنیم و پسورد پنل)
🧪
نکته:
مدیریت کامل ربات اعم از تغییر قیمت‌ها، تایید یا رد پرداخت‌ها، و مشاهده آمار، مستقیماً از طریق دستورات داخل تلگرام توسط ادمین انجام می‌شود. همچنین برای سرورهای ایران، امکان تنظیم پروکسی SOCKS5 نیز تعبیه شده است.
📥
دانلود و آموزش نصب در گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/6956" target="_blank">📅 11:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6954">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoqIuO-3HyIqNUJqZ9z9ziV9G-1qqpunloWetkoqpOfL__sReiKCsABLAXy4f7vT4dQIUdRCEyAaJSchqBaD_9qIV1LKXFLnF5oewebF_i7279rZDRgc6idpKiwwhfKkpWkl_-M1Ay7YlCTiydSDTy6sbDjHjfNhD97oaDewv9yVbOij9FV3inkjNRIX_RzLT4F5Az2leaykLuxafjThGfxDtcEs-y5zFaSEkiy8XCPvHMKUie60YXopCPvDT5KrlonykhyHxdUWobrJqRFSdz4jy7XsrGhyTtTOOISZwkoQ17vPjatHq0fuXR87gyNLOFZUKvUIwbLo6RtKbzJtxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🌐
BrowserOS & BrowserClaw
دو مرورگر متن‌باز؛ یکی برای شما، یکی برای هوش مصنوعی!
✨
ویژگی‌ها:
‏
🤖
BrowserClaw:
اتصال کلاینت‌های AI (مثل Cursor) برای انجام خودکار کارها روی اکانت‌های واقعی شما.
‏
🧑‍💻
BrowserOS:
مرورگر امن با دستیار AI داخلی و پشتیبانی از مدل‌های لوکال (Ollama).
🎥
ضبط ویدیویی تمام اقدامات هوش مصنوعی برای بازبینی.
🧪
نکته:
هوش مصنوعی در تب‌های کاملاً ایزوله کار می‌کند و هیچ تداخلی با وب‌گردی شما ندارد.
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6954" target="_blank">📅 10:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6953">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏
🚨
حذف ناگهانی دامنه
t.me
از DNS جهانی!
دامنه
t.me
(هسته اصلی زیرساخت لینک‌های تلگرام) به طور ناگهانی از سیستم DNS جهانی ناپدید شد! رجیستریِ پسوند
.me
وضعیت این دامنه را روی
serverHold
قرار داده که باعث شده هیچ‌کدام از لینک‌های تلگرامی در سراسر جهان در مرورگرها باز نشوند.
✨
جزئیات ماجرا:
*
📱
اپلیکیشن‌های موبایل و دسکتاپ تلگرام همچنان بدون مشکل کار می‌کنند و این قطعی صرفاً مربوط به لینک‌های وب (آدرس کانال‌ها، گروه‌ها و ربات‌ها) است.
*
💎
ضربه سنگین به اکوسیستم کریپتویی تلگرام و مختل شدن دسترسی کاربران به کیف‌پول داخلی (Wallet) و مینی‌اپ‌های مرتبط با شبکه TON.
*
🌐
دامنه موازی
telegram.me
همچنان فعال است؛ این یعنی محدودیت منحصراً روی آدرس کوتاه
t.me
اعمال شده و کل زون دامنه‌ها مشکلی ندارد.
🧪
نکته:
با اینکه اعتبار این دامنه تا سال ۲۰۳۵ تمدید شده، اما رجیستری کشور مونته‌نگرو (صاحب دامنه‌های .me) بدون هیچ اخطار قبلی آن را از دسترس خارج کرده است (پاول دورف در پلتفرم X مستقیماً از آن‌ها خواسته مشکل را حل کنند). این اتفاق زنگ خطری جدی برای شرکت‌هایی است که زیرساخت حیاتی خدماتشان را روی دامنه‌های ملی بنا کرده‌اند!
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6953" target="_blank">📅 10:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6952">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrCOn9M7yL398KsQaXMYYJAWPhfqrowg4Bd1UBY2XJ8UoGbKUn6WTRUOCjoW1r9BlMT7R9udqgD5R7pCS2K35vPfeIkDnaj4q64YgPsidFKMKF6MP7-keOyT36znZ1K65-zlQohp8zhf9r7Vno7R--GdeMTUra5zdiNl_Sp4hOduutRQxFnwt7FNzdz9gpAagED-AY3Fb2fU7kA22Zin3tgh92l2HSqExSi8hEGmNtPXPXQvRlmBVCMmLTyuCElnfFttpkMNBG-oU3_vAvasCA9546ZR8L7Ah4i2GBQvy4NwM3c8TBYMvHg9P2_g71i1q_v2hw4potAnbaKYHX2bWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛ Google AI Studio حالا به GitHub وصل
میشه
🔥
با قابلیت جدید Import from GitHub میتونید ریپازیتوری‌های خودتون رو مستقیم وارد Google AI Studio کنید و با کمک Gemini روی کدهای موجود کار کنید.
✨
امکانات جدید:
•
📂
وارد کردن پروژه از GitHub
•
🤖
سازگارسازی خودکار کد برای اجرا
•
✏️
ویرایش و ادامه توسعه پروژه
•
👀
پیش‌نمایش و Deploy سریع‌تر
⚠️
فعلاً اتصال یک‌طرفه است و تغییرات به GitHub برنمی‌گرده؛ اما همگام‌سازی کامل در حال توسعه است.
https://aistudio.google.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6952" target="_blank">📅 09:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6951">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A453lSPOlga32u-RL_n3-JbtMFpu0f6LXyD8sQccyRDZxphoqfcndYyuS2-H1_vAZwOGSK8P4paKwqRMzEkd1BwRBXRfPKyJQ7JHVLjDq0UVV5oKAnKBsvrO-THMpzxGtyazvNXlDEPA_LujwBkDEV1DCJJQH1yCT0MeveKhGvqBCSPkk5nPXgIM8-TXMTZuByWdluH4ARezRf7saOk8z-CFH1WQEvymWZs-b7Od6V2rxi_N13J7qKLBARyE21lUJYF7LFSyKk5mwV0Bloi3FQYDQP2HRpwNqxDpHH2k5KOSQoHcA6k_dfvj858oSjsmqOLJF_Bqggo7BEdLowiWyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
بیش از ۳۹۰۰ پرامپت آماده در ۱۶ دسته‌بندی مختلف، از جمله:
• تولید محتوا و نویسندگی
• برنامه‌نویسی
• بازاریابی
• طراحی و تولید تصویر
• آموزش، کسب‌وکار و...
https://xueprompt.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6951" target="_blank">📅 08:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6950">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184a52dda.mp4?token=DiXvnSLl_3PxtZZDtRpXtceF8h72otBGzV7yhSjxK9_j3TBeeZsHnAyxDHQA4oaDGv21Bg8TN6ywYOhy_3Fp9z1foiFYvILGjiJypy-5Jd0jbYRmLlOGBGaURjiJT3XTK0uTWZ-LFgrRBQLaWmhT-Tym8R_lT0Pu12xJ5RqQDhOZapVRXf3hP8frQlOh_wspQYjLX4RvPv0UrDgDbkbro62GRi4qmbhN4bWI59Qovaz_3fpOOdMtAOpKkzxH7du1q_s8bspZKv-pJTFOVBVDOzZ4csC2H85WyBf1J_w_B7fvaq2jbDXhk4KtlH8_aJ2LHMfHX5FcDOiFXGeZ3vVP2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184a52dda.mp4?token=DiXvnSLl_3PxtZZDtRpXtceF8h72otBGzV7yhSjxK9_j3TBeeZsHnAyxDHQA4oaDGv21Bg8TN6ywYOhy_3Fp9z1foiFYvILGjiJypy-5Jd0jbYRmLlOGBGaURjiJT3XTK0uTWZ-LFgrRBQLaWmhT-Tym8R_lT0Pu12xJ5RqQDhOZapVRXf3hP8frQlOh_wspQYjLX4RvPv0UrDgDbkbro62GRi4qmbhN4bWI59Qovaz_3fpOOdMtAOpKkzxH7du1q_s8bspZKv-pJTFOVBVDOzZ4csC2H85WyBf1J_w_B7fvaq2jbDXhk4KtlH8_aJ2LHMfHX5FcDOiFXGeZ3vVP2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧰
۳۰۰+ ابزار رایگان، فقط در یک سایت!
📄
ویرایش، ادغام و فشرده‌سازی PDF
🎬
برش و ادغام ویدئو
✍️
ابزارهای متن و نگارش
💻
ابزارهای کاربردی برنامه‌نویسی
🔑
ساخت QR Code، رمز عبور و داده‌های تصادفی
💰
ابزارهای مالی و محاسباتی
https://footrue.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6950" target="_blank">📅 08:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6949">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">📶
دسترسی به لیست سرورهای عمومی VPN
مجموعه‌ای از کانفیگ‌های
V2Ray
،
Trojan
و
Outline
VPN
که سرورهای جدید و سالم به‌صورت مداوم به لیست آن اضافه می‌شوند
🤔
🔗
نیازی به کپی تک‌تک سرورها نیست؛ فقط
Subscription Link
مشخص‌شده را کپی کرده و مستقیم داخل کلاینت خود وارد کنید.
V2Nodes
🌟
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6949" target="_blank">📅 01:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6947">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">برای احتیاط ام شده برنامه های ضروری رو آپدیت کنین که خیره
🌑
Slipnet
📂
WhiteDns
📂
Resolver
📂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6947" target="_blank">📅 01:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6946">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHRq2iwHSIRuzGQ8skRwsJRjcHz15tkhFya6Wrvx64z9HqYwpK1piTE6Jk7vIIoUedNqHRY0gRkUEXCy1_qXDUvMhy6XdSG4vqeGX4A-_hNdnp_10f4oyKqJ1d0u3W330kfJ4f4maxhCgB0Zk_nkQ28kR7qqoz3j882Pj9OR7yfwG2U3jb0pxyPJ03laPADtVFRP63rtnSXbNMeMyET7V0b4vy29KxLKcSYMLoNi_5Il46YNFOaNKMlMnn8kUedOExFWXnFg3TVcwZjFZz7gl69UsWYX1a8vf7_b0Qb5AkM238qmfBJWktrKoCn714BKicbbm69g77iD-Zxukinbug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🖼
Image-to-Text OCR
ابزار تحت وب و متن‌باز ساده و کاربردی برای استخراج سریع متن از داخل تصاویر به کمک تکنولوژی OCR (ایده‌آل برای تبدیل عکسِ اسناد و نوشته‌ها به متن دیجیتال قابل ویرایش).
✨
ویژگی‌ها:
🔸
استخراج دقیق و سریع متن از هر نوع تصویر
🔸
توسعه‌یافته بر پایه تکنولوژی‌های مدرن Vue و Nuxt3 و TypeScript
🔸
رابط کاربری تحت وب، بسیار سبک و بدون نیاز به نصب نرم‌افزارهای سنگین
🔸
کاملاً متن‌باز (Open-Source) با لایسنس AGPL-3.0
🧪
نکته:
برای راه‌اندازی این پروژه روی سیستم خودتان (لوکال)، پس از کلون کردن ریپازیتوری کافیست دستور pnpm dev را اجرا کنید تا برنامه روی پورت 3000 در دسترس قرار گیرد (بیلد نهایی نیز با pnpm build در پوشه dist ساخته می‌شود).
📥
دانلود سورس‌کد از گیت‌هاب
⭐️
حمایت از پروژه: ستاره (Star) در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6946" target="_blank">📅 23:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6945">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏
🤖
آموزش کامل و به‌روز راه‌اندازی NipoVPN
این ابزار با پنهان‌سازی ترافیک واقعی داخل درخواست‌های جعلی (Decoy/Fake HTTP requests)، به‌راحتی از سد فیلترینگ پیشرفته عبور می‌کند.
⚙️
۱. نصب روی سرور (VPS)
به سرور اوبونتو یا لینوکسی خود متصل شده و نسخه جدید را نصب کنید:
Bash
wget https://github.com/MortezaBashsiz/nipovpn/releases/latest/download/nipovpn.deb
sudo apt install ./nipovpn.deb
📂
۲. ایجاد مسیر لاگ‌ها
Bash
sudo mkdir -p /var/log/nipovpn/
sudo touch /var/log/nipovpn/nipovpn.log
📝
۳. ویرایش فایل کانفیگ
فایل
/etc/nipovpn/config.yaml
را با ویرایشگر باز کرده و مقادیر زیر را به دقت تنظیم کنید:
tlsEnable:
برای امنیت حداکثری این گزینه را روی
true
نگه دارید و پورت را
443
تنظیم کنید. (امکان استفاده از پورت 80 و HTTP معمولی هم وجود دارد).
fakeUrls:
چند سایت معتبر و بدون فیلتر (مثل
google.com
) اضافه کنید.
token:
یک رمز امن و طولانی (حداقل ۳۲ کاراکتر) برای ارتباط کلاینت و سرور بسازید.
🚀
۴. تنظیم فایروال و استارت سرویس
ابتدا پورت انتخابی (مثلاً 443) را در فایروال باز کنید:
Bash
sudo ufw allow 443/tcp
سپس سرویس را فعال و ری‌استارت کنید (بعد از هر تغییر در کانفیگ، ری‌استارت الزامی است):
Bash
sudo systemctl enable nipovpn-server.service
sudo systemctl restart nipovpn-server.service
جهت بررسی لحظه‌ای لاگ‌ها و اطمینان از اجرای بدون خطا:
Bash
tail -f /var/log/nipovpn/nipovpn.log
📱
۵. تنظیمات کلاینت (گوشی)
کلاینت رسمی
NipoVPN Android
(در گیت‌هاب) یا اپلیکیشن
سیمرغ (SIMORGH)
را نصب کرده و اطلاعات آی‌پی سرور، پورت (443)، توکن و آدرس جعلی (Fake URL) را دقیقاً مطابق سرور وارد کنید. کلاینت اندروید بسیار بهینه است.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6945" target="_blank">📅 22:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6943">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏
🚀
SulgX Panel
پنل مدیریت اشتراک VLESS فوق‌سبک و شخصی، ساخته شده تماماً با پایتون (FastAPI و SQLite).
✨
ویژگی‌ها:
🛡
مدیریت کامل کانفیگ‌های VLESS (WS+TLS) با پشتیبانی از Fragment و SNI اختصاصی
📊
مانیتورینگ زنده مصرف ترافیک، محدودیت حجم و زمان انقضا برای هر کاربر
☁️
بهینه‌سازی شده برای استقرار (Deploy) رایگان و ساده روی پلتفرم‌هایی مثل Render و Railway
🤖
دارای ربات تلگرام هوشمند دو زبانه و سیستم ضد-خواب (Anti-Sleep) سرور
🧪
نکته:
این پنل کاملاً رایگان و اوپن‌سورس است و به راحتی از طریق فورک گیت‌هاب و Dockerfile قابل راه‌اندازی است.
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6943" target="_blank">📅 18:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6942">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">archive-scanner_v1.0.4.apk</div>
  <div class="tg-doc-extra">10.4 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6942" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکنر آیپی تمیز کلودفلر آخرین اپدیت
دوستانی که نسخه قبلی رو داشتن هم میتونن از تو برنامه آپدیت کنن هم با این فایل
سرعت اسکن خیلی بالایی داره، دقتش بالاست و ui کاملا ساده و سریعی داره
🔎
Findings:
❌
Detection: 0
⚠️
Suspicion: 0
✅
Not detected: 67
• File name:
archive-scanner_v1.0.4.apk
• File format:
Android
• File size:
10.43 MB
•
VirusTotal link
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6942" target="_blank">📅 17:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6939">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBvYxd9kSC_zyjHtipig76_lA0WZYGqLJjONUBXJWzf7LcA_IdzXMaBQfTAMpmv5aeTpZRlY-iBA6mzZYPYm7X2pzVmkHOT3nvQ0oK1Mope97g26oytqw4QAdQz35dxNi5cZoDiR8dzQwTf1Bku0aZAnU4elGZRAM0wE5Ti_-DG5ohYqbhN3c2AZE9rx7j8d-KVld01LJxoUAINKMkaK1M6hAlI7ns_4E-GxhIBh0ZTNi0OK-cV8t2X_DNdNox0Qv2LXuUjFI643GRB4FdxkU51Pcp1YpguxYXnp67aOYo7HLz1yL7ptaYDwm0iDslVDSTTDX0QYdOWQmwMi-IH_Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZCxS00IbJZ1DcqvAdwAfojlUxkVNFE70JJz1WoYTELCN8vJ7zIgCzI-12LveSA6HjIk5waJcsI6CT_we3CF1dkkNU77rVi3QTEddJ062UJ7OQZxCqk940Et-SDsFlbcJmt2OuLgUCeJyZWuy0koFEX0Q4GH5fW0i_DqMszoQx3_lvHsKHIae_zO90_ISqdl1prgPM9fhp5QUmDatkEM_9sPVWW5djUhRQ4bAgu_s4AYoPWwBC6GDuyJAWyCyYlAJfW2osh-WzdvamB-ua9D36WenBgoPKU7DJlF74ctI1HmtaIwNHCJM1z2a1e0TGGPnacW3683B1Oz6OrWWSVVWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HMncxWc4a21noAfJLYfetP67sIBmFxA3uRBvTMpxvS-k-MrwfaSnge3CKF_xuNBnMWvR6K3fhT6622d-wamgxQheOVGOA4w81W9p6IV_2IfIi65baGzwkrD3hZmWJrAwdTKNIJDUyd-Ar8yjcU0a2NpnTJpn-ELA1cC7T0oKyHP_Fe9n2zXS7pbSTaL-N7vJKUXTm3K6usQmYV3t-VdI38aoDJS9Onx3mJmYi8QgCCG51uedyc-gHpznFubDnGFbYeRHD0PoH7bxTt20YFGpKwalYugrRBVzd9vCvOEytoiMQRPQ0wHBT4j2zMzJITJga0RmOLhvSGyPrNTU9fbKfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
؛Archive Scanner v1.0.3 منتشر شد!  جدیدترین نسخه‌ی Archive Scanner با بهبودهای مهم در دقت، سرعت و امکانات منتشر شده است.
✨
تغییرات مهم:
⚡️
اصلاح کامل تست سرعت دانلود (اندازه‌گیری دقیق‌تر و عبور از فیلترینگ SNI)
📤
اضافه شدن تست سرعت آپلود برای هر IP
🤖
ساخت…</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6939" target="_blank">📅 17:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6938">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">📱
؛NipoVPN Android کلاینت رسمی اندروید برای پروژه NipoVPN؛ یک ابزار پروکسی و ضدسانسور قدرتمند که ترافیک واقعی HTTP/S شما را در دلِ درخواست‌های جعلی (Fake HTTP Requests) پنهان می‌کند.
✨
امکانات:
🧩
توسعه مدرن: برنامه‌نویسی شده به‌صورت کامل با زبان Kotlin و…</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6938" target="_blank">📅 16:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6936">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نت من ترکید
ی اعلام وضعیت کنین</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6936" target="_blank">📅 15:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6935">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏
🔥
ChatGPT Work
اوپن‌آی با معرفی قابلیت انقلابی Work، آینده هوش مصنوعی را تغییر داد. این سیستم دیگر فقط یک چت‌بات ساده نیست، بلکه یک دستیار هوشمند (Agent) است که کارهای پیچیده و چندمرحله‌ای شما را از صفر تا صد، به‌صورت خودکار انجام می‌دهد.
✨
ویژگی‌ها:
🧠
تکیه بر موتور GPT-5.6 و Codex:
ترکیبی بی‌نظیر برای اجرای کارهای سنگین تحلیلی، برنامه‌نویسی و چیدن خروجی‌ها.
📄
خروجی‌های زنده و واقعی:
ساخت مستقیم ابزارهای کاربردی مانند شیت‌های اکسل، اسلایدهای آماده ارائه، اسناد و حتی وب‌سایت‌های تعاملی.
⏰
اتوماسیون و زمان‌بندی:
هندل کردن خودکار وظایف تکراری در زمان‌های مشخص (مثل چک کردن روزانه قیمت‌ها یا خلاصه‌سازی پیام‌های تیم).
🖥
کنترل مستقیم دسکتاپ (Computer Use):
قابلیت تعامل با سیستم دقیقاً مثل یک انسان؛ کلیک کردن، تایپ و جابه‌جایی فایل‌ها برای انجام کارهای پیچیده.
🧪
نکته:
امنیت این سیستم کاملاً تحت کنترل شماست. دسترسی‌ها را خودتان تنظیم می‌کنید و برای اقدامات حساس، سیستم حتماً از شما تاییدیه (Approval) می‌گیرد.
🔗
وب‌سایت رسمی OpenAI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6935" target="_blank">📅 14:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6934">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-_p3rOKFhTowCBA0yENmZ6D9ZxAGHK8YCu-iYtGmRbXtba-Hc2E0y6YHXzJ9WK0xx3DL0gKd8tDcIw6bIH33OQiEQh9mD-6arpE35VR5vlxTVxq7Jbt0h1yZBw-YMLUYlNmQ9ZORjFBEcaNsQhxDxaYfiz43NnwdwF0ly-F5CwpwzrvvDixee0j-V8hR7jc-zzf14OX1gObpZjCbf5yQhh5NxfJJElGsrRdT7Oy0M0juFULpOxlEo5eksLqWHqB5a-njHhvxBxX1UCUsR-cdUvLRbHuQeUWaOLbPOEOWCR7vIbudZRuPMDscWr4tjqWEgZ2H5ru4sTiK5hcS20xaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🕵️
3D Investigation Board
یک برد کارآگاهیِ تعاملی و سه‌بعدی (مبتنی بر GPT-5.6 و Fable 5) که به شما اجازه می‌دهد اطلاعات و سرنخ‌ها را دقیقاً مثل فیلم‌های پلیسی روی یک بورد مجازی مدیریت و تحلیل کنید.
✨
ویژگی‌ها:
📸
امکان اضافه‌کردن انواع شواهد، اسناد، یادداشت‌ها و عکس‌ها روی برد
🧵
اتصال بصری سرنخ‌ها به یکدیگر با نخ‌های سه‌بعدی و فیزیک واقع‌گرایانه
🧠
کشف هوشمند ارتباطات پنهان بین داده‌ها به کمک تحلیلگر هوش مصنوعی
🧪
کاربردها:
این ابزار خلاقانه، نه‌تنها برای حل پرونده‌ها و معماها، بلکه برای داستان‌نویسی، ایده‌پردازی و برنامه‌ریزی پروژه‌های پیچیده فوق‌العاده کاربردی است.
🔗
مشاهده ویدیو و آموزش کامل در X
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6934" target="_blank">📅 13:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6933">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCaKUoHUolchpOIhiCrLWROSEuMRK9MgYWzgCNr1QrsVnKPcecPDVeHMpGOOD0lty5Ec5BZ8owB8yjMapdJzO1j-6zxom7dFKSsipldsra40_U9w8fiTYQJJakXVFj3YcRavEzm-VoezE1XW7jozBDpvA9XF4ZZhiXL0yaD0u-0rhrcjq6XPic28X9UeJbZfH4jMkuZkLyY-kFDnmA8ScPHBfOD89j5jxKsIg0QMV2DBF_HlirgC9Nq7HGCr__45u9YhEjfzwbZP1Y-xcl119SFHLFYUQ9d7wmz4L-Ay2z2wBinDQ5sj1N8v2RcFMPycS6bN3zA2cLfoDItSfTivew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤖
OMG-Agent
کلاینت دسکتاپ متن‌بازی که به هوش مصنوعی اجازه می‌دهد گوشی اندرویدی شما را فقط با دستور متنی کنترل کند! (مثلاً: «تلگرام را باز کن و به
⚡
Bachelor پیام بده»).
✨
ویژگی‌ها:
🧠
پشتیبانی از مدل‌های هوش مصنوعی موبایل (مثل AutoGLM) و APIهای OpenAI
📱
اجرای خودکار دستورات با تحلیل لحظه‌ای صفحه گوشی (از طریق ADB)
💻
سازگار با گوشی‌های فیزیکی اندروید و شبیه‌سازها (Emulators)
🧪
نکته:
پیش‌نیاز این ابزار، نصب ADB، کیبورد ADB و فعال‌سازی USB Debugging روی گوشی است.
📥
دانلود و راه‌اندازی از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6933" target="_blank">📅 13:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6932">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏
🚀
۴۰۰۰ دلار کردیت رایگان API
هدیه‌ای ویژه برای برنامه‌نویس‌ها! دسترسی سریع به قدرتمندترین مدل‌های هوش مصنوعی دنیا برای پیشبرد پروژه‌های کدنویسی شما.
✨
ویژگی‌ها:
🧠
پشتیبانی از مدل‌های برتر جهان (GLM 5.2 ،Qwen 3.7 ،Deepseek 4 Pro ،Minimax M3 و Kimi k2.6)
📧
ثبت‌نام سریع و کاملاً بی‌دردسر با هر نوع ایمیل
💻
سازگاری کامل با انواع کلاینت‌ها
🧪
نکته:
مصرف کردیت در این سرویس‌ها با ضرایب بالایی محاسبه می‌شود؛ پس حتماً در استفاده از توکن‌هایتان دقت و مدیریت لازم را داشته باشید.
🔗
لینک ثبت‌نام
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6932" target="_blank">📅 13:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6931">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O58eQRySpFMRusHSRKlhJKv6vtvHGCWciT2U464-G42OY2bQJT9b2lTk-2KTTmkbHj6yN_LM7mmebg-a4dAqBtWPc30reh8Bmw5crhMQVfRnGqzUCew5yYhQ4Q0zTNqc0gZSi4bZUK50hfvmAiA11rC6eR7cOS6Vezp-ABheCtwIJ0OTcD7u3EWVXN1zgq4HG56pP76-mXCbAR5LGp9D0D4zb9D_M0v524iZXe9fBrJyMIdwtCaDlhUwHOpqr3H1b4C2GIEmUFLejejCpbIfS71207cWKjO6ekrK5OmfFHRlwfhZZp1CSuJ4nJOxDyFV9uWpnHfFfr6z7BtiatlJTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⭕️
Colibri
پروژه قدرتمند و متن‌بازی که با C خالص نوشته شده و اجازه می‌دهد مدل‌های عظیم هوش مصنوعی را تنها با اختصاص ۳٪ از حجم کل مدل به رم (RAM) اجرا کنید!
✨
ویژگی‌ها:
🔸
اجرای کامل تنها با یک فایل C (حاوی ۲۴۰۰ خط کد)
🔸
کاملاً مستقل از پایتون، کتابخانه‌های جانبی و کارت گرافیک (GPU)
🔸
ساخت API لوکال سازگار با OpenAI (تنها با دستور coli serve)
🔸
اجرای مدل سنگین 744B (که در حالت عادی ۷۳۰ گیگابایت رم می‌خواهد) تنها با ۲۵ گیگابایت رم!
🧪
نکته:
برای کاربران ویندوز، استفاده از WSL2 پیشنهاد می‌شود. به عنوان مثال، لود یک مدل ۳۷۰ گیگابایتی تنها ۳۰ ثانیه زمان و ۹.۹ گیگابایت رم نیاز دارد (البته به دلیل عدم استفاده از گرافیک، سرعت پردازش حدود ۱ توکن بر ثانیه خواهد بود).
📥
دانلود از گیت‌هاب
⭐️
حمایت از پروژه: ستاره (Star) در گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6931" target="_blank">📅 12:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6930">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">📈
؛
Vibe-Trading
دستیار هوش مصنوعی شخصی و متن‌باز برای ترید و تحلیل بازار. کافیست ایده‌هایتان را به زبان ساده بنویسید تا خودش برایتان استراتژی معاملاتی بنویسد و بک‌تست بگیرد!
✨
ویژگی‌ها:
🧠
تبدیل مستقیم پرامپت‌های متنی به کد استراتژی، تحلیل بازار و دریافت بک‌تست‌های دقیق
🐝
تشکیل تیم‌های مجازی هوش مصنوعی (ایجنت‌های ریسک، کریپتو و کوانت) برای مشورت و بررسی همه‌جانبه ایده‌های شما
👥
سیستم جالب Shadow Account: ژورنال معاملاتتان را آپلود کنید تا هوش مصنوعی خطاهای احساسی و رفتاری شما را در ترید پیدا کند
📊
پشتیبانی یکپارچه از بازارهای جهانی (کریپتو، سهام و فارکس) با دریافت خودکار دیتا
🧪
نکته:
این ابزار با پایتون توسعه داده شده و به‌راحتی به API مدل‌های مختلف (از جمله Groq ،DeepSeek و OpenAI) متصل می‌شود. برای دیپلوی روی سرور شخصی یا اجرای لوکال فوق‌العاده است.
📥
دانلود و نصب از گیت‌هاب (PyPI / Docker)
⭐️
حمایت از پروژه: ستاره (Star) در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6930" target="_blank">📅 12:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6929">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏
🐋
Orca
محیط توسعه و هماهنگ‌کننده (Orchestrator) فوق‌العاده قدرتمند برای مدیریت همزمان چندین ایجنت هوش مصنوعی برنامه‌نویس. یک دستیار همه‌چیزتمام برای توسعه‌دهندگان!
✨
ویژگی‌ها:
🤖
اجرای همزمان ایجنت‌های مختلف (مثل Claude، Codex و Grok) روی یک پرامپت و مقایسه خروجی‌ها
📱
دارای اپلیکیشن موبایل (iOS و اندروید) برای کنترل و هدایت ایجنت‌ها از راه دور
🎨
مرورگر توکار (Design Mode) برای انتخاب المان‌های سایت و ارسال مستقیم HTML/CSS آن به هوش مصنوعی
🔗
اتصال بی‌نقص به گیت‌هاب، پشتیبانی از محیط‌های ریموت (SSH) و ترمینال‌های قدرتمند داخلی
🧪
نکته:
این نرم‌افزار متن‌باز است و تقریباً از هر ایجنت مبتنی بر CLI (مثل Cursor ،Copilot و OpenCode) پشتیبانی می‌کند. کلاینت دسکتاپ آن برای ویندوز، مک و لینوکس کاملاً رایگان در دسترس است.
📥
دانلود از گیت‌هاب (بخش Releases) یا سایت رسمی (onOrca.dev)
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6929" target="_blank">📅 11:28 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
