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
<img src="https://cdn4.telesco.pe/file/Dq17OcqFmiU5UrAyG2iSQi257CmqPGiJqSoO3ByiYqzj3I6QOH0zcsaFBQqPNSuF8f1CgBsG7Bf9X9D02HMvGMFPCe-McFws4zpR3lGQnEdEMbqcps_ek3jjgU8_wUz0vi3kGJUYEbdjsh5dK9JmFT5N6GS8aJbMr0JmumpwHPw-HsMqAJ260zr7BmHjqmVVwBnYL76t8zkkIyJlzPuXnFIRunBP-uYtut4seB2O1xv0Xkyv5Er1AbpHW3AWSC-szIL0tRWWCuEsjfwEvr4yIj_p3i139_nzUxxTiAtNVlorPchLTjjbkJEObHjOXVEyHA8rj0G6DPVkM8P8NfcE5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 05:04:32</div>
<hr>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBfj9Ot5dU7_yx6suYbWCGRIlf2xHquNcmQ4rKMVyxTpEEU-CQkFj-nF3fsrLok06LFqdHb1ADoxrc_gQ2LIRXPrXlt7b7MPU_uoF-CMPifSuvKTDmCCoaEptBcRqz4uDzp7dPxEloBsk20UL2SXtu7OrxwB9PUlzAre1Vum76iRT_wdQgn9eQTQ3sIz4dAcTIIVKaFngzrKV3iWRzxZqIQeurcjGLTeQ-sUZ5qESxIhjftB1NsbkxIFN6_aAgB48PlxmFvpJ978alO2FnL5Z4KmHxNIUt2lLu5czvBk_s1bSIar0EzsHMsb_n0lOmtWN2KIYZjp0hxoEQMxGS1PvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
ساخت تصویر با هوش مصنوعی؛ رایگان و بدون ثبت‌نام!
🔺
بدونه اکانت و کارت بانکی
🔺
بدونه کردیت و واترمارک
🔺
بدونه هیچگونه سانسور
🔺
تا رزولوشن 1024×1024
🔺
چندین سایز تصویر
🚀
فقط وارد سایت شو، پرامپتت رو بنویس، فرمت رو انتخاب کن و تصویر رو دانلود کن
⚠️
مدل دقیق استفاده‌شده مشخص نیست و محدودیت رسمی روزانه هم اعلام نشده؛ ممکنه در ترافیک بالا با صف یا محدودیت مواجه بشی.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 913 · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=vn8ja-e56Fazne_nMQ5sZyopyoI8PCxp9tkfvPhSnskbKQBwLV03a0qQYMJSXiyECSrhf7gpoZwnDa25bhjo_vJEHRE6lp5_WBOj7iQDnYxU4nkH3wbUQUsOrpz_QksqTJVHTnRAjcR5_CoOthWGyabZiioN8kcTvpKrKap8GawXImPuRqTAdnSy1pe3c_yojBsQfYRH4pOqymZRg4BK2mwAbeS7lQAKXx4gCwdOq7KbhOyY0y31SuuAgz3458Hbr-g1M_jbiQ5CQiq-_13ptEUscoFFMOPkBUNth2cW4D_t1aUPAkrO0tt2VYZnQASEDLOmID6Bss5pjzTnMzVl5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=vn8ja-e56Fazne_nMQ5sZyopyoI8PCxp9tkfvPhSnskbKQBwLV03a0qQYMJSXiyECSrhf7gpoZwnDa25bhjo_vJEHRE6lp5_WBOj7iQDnYxU4nkH3wbUQUsOrpz_QksqTJVHTnRAjcR5_CoOthWGyabZiioN8kcTvpKrKap8GawXImPuRqTAdnSy1pe3c_yojBsQfYRH4pOqymZRg4BK2mwAbeS7lQAKXx4gCwdOq7KbhOyY0y31SuuAgz3458Hbr-g1M_jbiQ5CQiq-_13ptEUscoFFMOPkBUNth2cW4D_t1aUPAkrO0tt2VYZnQASEDLOmID6Bss5pjzTnMzVl5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدها ابزار متن‌باز و رایگان، همه توی یه جا
💥
🆓
سرویس NoSignups یه دایرکتوریِ از جایگزین‌های متن‌باز و رایگان ابزارایی مثل فتوشاپ، کپ‌کات و فیگما رو جمع کرده — همشون هم به‌صورت آنلاین توی مرورگر کار می‌کنن.
✅
🔺
بدون ثبت‌نام، بدون نیاز به کارت بانکی
🔺
توی کاتالوگ، ابزار برای برنامه‌نویسی، کار با متن، عکس، ویدیو، موزیک و خیلی موارد دیگه هست
🔺
همه‌ی ابزارا کاملاً رایگانن
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3HIYniLGtb1P1bvynkIE1cpCLiP4cQtsv6vJPYUXQUDCRbrT-yxOispIc6r3qJmPAyZiCHX8FHOzhaMg480fGOjuxE1d4o0ZfotL4RugJ4xz9RzXxUHKWFhkbMGh3HHX28UnUEEwynCMNkZ6Ko6wyESgnbKnO4e9mhffAo2ZtYhBooCGd2pNPEs423PIn07-CzebGr5YZ4zKj_LCGB9vGn9REGsU1hM6SyE5-LuwymGmO8jt7Y0H5PMwNVxwK4Y87hORQ7qQqtT1Qj3DQqtEmVys4WbdOqVw702z10qz3u1voE-bFu8FAcEizmB_FYfe8m6uGvf7RJ0_N6KG0kqIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجموعه رایگان ابزارهای تشخیص محتوای جعلی و تولیدشده با AI
🔍
سایت
forensics.media
یه سری ابزار مرورگرمحور برای بررسی عکس، صوت و فایله که کاملاً روی دستگاه خودت اجرا می‌شه — هیچی آپلود نمی‌شه
🛡
✨
چیزایی که می‌تونی باهاش چک کنی:
📷
تصویر:
تشخیص ادیت و اسپلایس (ELA)، متادیتای عکس (مکان، دستگاه، تاریخ)، تشخیص تولیدشده با GAN یا دیفیوژن (Midjourney، Stable Diffusion)، واترمارک نامرئی، SynthID گوگل، کلون/کپی‌-مووِ بخشی از عکس، و متن مخفی داخل پیکسل‌ها
🎧
صوت:
اسپکتروگرام، تشخیص موزیک ساخته‌شده با AI، فینگرپرینت صوتی، ENF (برای فهمیدن منطقه ضبط از روی هوم برق شهری)، و تاریخچه‌ی فشرده‌سازی
📁
فایل:
هش SHA-256 برای اثبات دست‌نخوردگی فایل
⚠️
نکته‌ی مهم:
هر کدوم از این ابزارا فقط یه سیگنال جدا رو می‌سنجن، پس هیچ‌کدوم به‌تنهایی حکم قطعی نیست. برای اطمینان واقعی باید چند سیگنال رو کنار هم دید
🔗
لینک وبسایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=AE7gB5rcRKytXwFPSlNYulxbeG_bpMtxt-wyC6oSMuElbOxnKnOAW0qw50pxtv_X2UOn38W6vbe0c736euMDf2kLBM-iNtDgr1-k3B9Tc78c8qeNVdjQe0PQ0XhCogCYleURvTxIEppFWIrScnVKWcFr8cXcgHslnP6au02FfNzYZDRwLFMmpupQMwzYIK6unx3Av79r49fx4TbUCVFlkVcakwC0Tndg1tKY5TbNB4Rd_cmxApwmkf_JogY3FBudHIKTheYeLexTImSa0mQdSA8UkomkusCKoMNsXMtGYzhVmez1WDoN7zaXvFVhTNbjtDc2XW8qCDvO3bmDDaykEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=AE7gB5rcRKytXwFPSlNYulxbeG_bpMtxt-wyC6oSMuElbOxnKnOAW0qw50pxtv_X2UOn38W6vbe0c736euMDf2kLBM-iNtDgr1-k3B9Tc78c8qeNVdjQe0PQ0XhCogCYleURvTxIEppFWIrScnVKWcFr8cXcgHslnP6au02FfNzYZDRwLFMmpupQMwzYIK6unx3Av79r49fx4TbUCVFlkVcakwC0Tndg1tKY5TbNB4Rd_cmxApwmkf_JogY3FBudHIKTheYeLexTImSa0mQdSA8UkomkusCKoMNsXMtGYzhVmez1WDoN7zaXvFVhTNbjtDc2XW8qCDvO3bmDDaykEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوی ترین ابزار افزایش کیفیت ویدیو رایگان
💥
🆓
🎬
هیچی نصب نمی‌کنی — فقط فایلو بنداز توی مرورگر
✨
خروجی با کیفیت 2K یا 4K، هر کدوم بخوای
🔍
جزئیات ریز هم تمیز و شفاف پردازش می‌شن
🎁
کاملاً رایگان — نه واترمارک، نه حتی ثبت‌نام
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3I52aHW6riVppT81MUnA75UfoaPuP2D_QyqVh5NkwiwfH5oFF-RVOivqGU7snRK6YVE36zDRvM3KL7ZsL9d3utWP0stTrVgZ7EepCK-SNHop2RjLiykqUXJcOWrqzPhWFG0QUwxsNcCSzl8P0knfYXo_mz4icDvGocmUuWOSUNZjTRWx_3VjOfIUe46bR0CZcRqn8UlECcC4mLvdmY_ko8pOUotAkEIkfsPGaICNDjQ9WucJISPc1u0NDbIoySTJyqvaJnY7-jaD0g9-FEqDFRKVrf-y_73MvCbnvEMOwK6cz_PWtN5SVQwiXuANrPlUOBM29YVUj8ZGvmxZ8pyJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به API مدل های رایگان
💥
🆓
مدل MiniMax M3 و چند مدل دیگه از طریق Ollama Cloud به‌صورت رایگان قابل استفاده‌ان ( با محدودیت روزانه و هفتگی
⌛
)
1️⃣
وارد سایت
Ollama
بشو و اکانت کلود بساز
2️⃣
با گوگل یا جی‌سوییت لاگین کن
3️⃣
از داشبورد اکانتت یک API Key بساز
4️⃣
کلید رو به 9Router یا هر سرویس مشابه دیگه اضافه کن
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjkR9FhwnKk5tmbWA5H0GEj3IZIUUkMqPcTSB6lZYT3F3UMdjZmBEuT_-H-NV85GMGF0IWNu3GR1cm3GgzCIHnwJYOzHJk3spePq4fl4MIdbDUdKL1vSNBZDLPgPleXV5CvspBbUSardbCjbpQV67XKWrHADPVdMPgQ2BytAm7b484Yhp5T-AYE9mn8qx1lnhKZ_xXQM0TI4Ai7eWhw1lNhGZxQoVjIxvI-Q-mzHbICwqJVkEx8WQjRW6tTXZSQXDWKykiCshtOs2e_asfRA1RF1AiXADq9bn-9fGEUWqRG732cMTgI7cow2m9wCQ2tbgD1s6yltVV_IDT0KpRrujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
DeepSeek Harness Studio
رابط گرافیکی ویندوزی برای DeepSeek Harness
🤔
بدون نیاز به ترمینال یا Node.js!
🤔
نصب خودکار در اولین اجرا
🤔
وب UI رسمی داخل برنامه
🤔
پشتیبانی از پروکسی داخلی
💎
https://github.com/ScannerVpn/DeepSeekHarnessGui
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XV4nn8_PT99rHmG9iYJzjk300jaUDbgOdM52yFUYgsWQLSIDVR2xj46Ji46Q0ML1_2FqxgIjZc2hLBWc3O2wqqc8lW9jzKZXYc4XfTKm4ETaFxpafAfT3TAlYjRf4JFNmGXXDMGaEXYiwTGbu6P_feZptYFwcO6m76dgHEF1zyB-pf9sDMgfv502_8_wYVcaCmnAMvwS7OCu8PWUQlITdo-1Knz6bgqKt4SSIeSzDfiaHWPbwmXc_AAX_TmWsysa-crcZvnJxpx5cj9UFW3s93LxEmmf6lburmsKdLXOeYVRijbVEBt8LoqJea5xgrfKQ-J2FfPnhAMLapVRalumEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N01_ySSJqWq4lCm3r3rPqnaBFSKyBZGe5wkq_VJuoRH6PSyW2iH6LPlEqH7HDF36gRUghnrQhPtrcN0voRP1pDE5MmdrR51huzDh1I-QuhQs7fc0IUuBIucr1XMg_UMSRWRmJi8M6q7BshBsH1wEmgj0qc5qGgSfPCu_1g1iR72wzaMJ-VqWrtg1PjATzI1GdlHhAul7atT8u5PSo1Ii68E-i4IQmZVSno774sLPH7yKFmDmdvIambQAJkMYH2Bq7Yr9aMOzrU3N1kDAJNzjsLIT1xVw6Hl3SaRkE3WRicHWD20G6ea-57CwkA3Xf-hS6kdP5T-CvKnYI3lSYggKOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YuQgzgHMcma3qEyH26YChtheIncVvUm_beBz3sSadnVVUTPrel_BEVR1ExvCH1Zw63g_HQmu8nOsudNOvz4GlHwL4pIfHYtrMqluowXlKE58CJhonx3_cV2Bw5UgPq0oc6sy5aKXpO00VGV81COLzviIeiQ3mg5N1LFDRmv7YzXnadoF6_T2Nowa4JLcqXRPmP4yYqxfsl39FmIvbikQB3ZIfws3DQtR3xUEZXYXvdwOo-4wBrTsLbXrkiScUz0Ia-WVGqt3c7GZxfgNi2uJsMMTLsD9orAmhJ_kOS_v3Porefe05ylsSkquCI_DIY-ao3zzuJlAjsRbIxpYIpUgrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qht8_V6ZpQES9WkQ0elz03tXNeuP8bw4c__KGUtIhIvmMF6-xCrHzgtIhxoFsgdAZXaldaVfzZxlSGiubGZZcnzR_Pc8YW6yGwod2uh6frNd1-BQfbEM0CGYNC4bYzs8LjXPCng7ClXycjYD0x7qfjj2WdLoZMx-KjH56kg-A4M-SIr7BN6eMPTB8z_nSNaPkVi9a5QIza_yUgamcEahQW7p0qtcomJqoNfWzVGp19MYUOayWn_DG9NLzGsKzQw30a5IeyjF1tmXPfgLTJJOqlzq1IxV5DX4mB4AwzG_Dp5zFqpkEIyUhktvhjuM7RmS3Sg-r4Qms8WOhu4Q7TdTHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🛍
خرید اکانت
Windscribe
با کریپتو از طریق
Build a Plan
اگر قصد دارید اشتراک
Windscribe
تهیه کنید، می‌توانید از بخش
Build a Plan
پلن دلخواه خودتان را بسازید
⚡️
کافی است مقدار دیتای موردنیاز و مدت اشتراک را انتخاب کنید، سپس در مرحله پرداخت گزینه
Crypto
را انتخاب کرده و پرداخت را با ارز دیجیتال انجام دهید
🪙
🔵
انعطاف‌پذیر و اقتصادی
🔵
امکان انتخاب لوکیشن‌های دلخواه
🔵
پرداخت با ارزهای دیجیتال
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEePLgpwsdLONv6RAeOwRo96IbRZ1uqnLKqIyyh8SLd7hAFr72wQAflH-7SaVl-w3FY7sfsYYUfP-g4dfofPfB7JRypSjd7il3-dcOw66XXbtuzqV9OGdyv6EJTMajJjqvDIBK4SJGjl696jCNJfqAATELiUCmiCBTVMZs5nY1jdaWgjpiblx-tO-f0GCwy3xs3p_D9VUogAcmx3o02eckjrwsW_0Es5YR-WQj7d_6ACMAkQA2HuW1DwsOzmsE3vDalNnPHxz1T-no9Ht2dc15aCv-IBcwkec-MqPXTA-KC_ZvlC_TWv41IAseXQYsGO2BrKUewuK7IjU6cGF6aw9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!
‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون
‌GLM-5.3 Flash⁩
محصول شرکت چینی
‌Z.ai
⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی تست واقعی با ‌Cline⁩، هر دو مدل از پس باگ بر اومدن، اما Ox Alpha با مصرف یک سوم توکن و سرعتی خیره‌کننده‌، برنده بی‌‌چون ‌و چرای میدان شد
😎
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">عکس‌های داغونت رو تبدیل به شاهکار کن
✨
دیگه لازم نیست از عکس‌های بی‌کیفیت بگذری! نورون InvSR رو پیدا کردیم که هر پیکسل رو زنده می‌کنه، بهش عمق و جزئیات واقعی اضافه می‌کنه.
🔥
📦
نصب لوکال از
گیت‌هاب
🖥
آنلاین رو
Hugging Face
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">Avast SecureLine VPN
4KAX6F-Q7LM6J-5LCJ6E
3N7RAW-SG38HJ-5LCJ7W
BJS8N3-NNAVTJ-5LCJZJ
J3BSAR-XJZR32-5LCJME
VUYR9T-JZ5GBJ-5LCJVN
23RWWJ-SEAQGJ-5LCJTN
GFU46H-QA2CDJ-5LCJBE
7SKUU3-S97Y42-5LCJD6
UENGEB-Y9NGA2-5LCJEE
EBF8PY-8CPH82-5LCJ6J
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRyZS9vx1eguJBj_5EeNq1aPuI2rlxRrUzDj1oraU0opzI6aE5lf6PbuaFY0u7D0jqL_J839JqtO1xSzT6ucT9b3ce6WiDcDzfwSwLLxMKyk9G1UQPTV57xyY0WETqm-Vh3eLvYe99Kr8ZK61cXszgDi1SWsalvxRg4YtqJfURzDmEcY3oUVmNTb3ozd3l-dn24wXcysO_856uYCBL2fKe7yvWowo2Nz91IbZv2yfm_Aqp4Tl9BHgrn4wnt9jztA76_O3xSXfa8pBVWKoRTFrgaclfYlp6P1cV2ZM8SSnjgK56tiIIRi_0Goaul6Oe27e4Um8lowZ0_jBFmGHe1y-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب
قدیمی داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
100 دلار
و شخص دریافت کننده
175 دلار
دریافت می‌کند!
فقط در کلاینت های گفته شده در Docs میتوان API را استفاده کرد
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6p9XsWIhyWNEVGsBWDgwJiUkzomhgkImHLhUMO0sJeNZK8Sg-BgKkm9fwiUZRQOat2tQItf2XUy4VFA8nXD9y9lkMXY2FjMb8cYC8SK37lOspR7_UkEy5klOaQD2OmjAwLuIGo_RyApIomjDLAHsn1nCQgx1IOglu7W0ZINiGFQFm-kdPW2xG6q2RKDjdDjZ_dayOJtyrtNyDIJpXXvJgBieypu2k_dd2VdNzAT4vd6il6YSxI6MvdTOau-fydFv57jwoVOBjqciLecW8NvHtSKJ6Xc5EilfHzGEA0cEakIHDSgo_IPpUjsVoyXKjJOT0nulSh5CwjTDcudfp5LkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های قدرتمند MiniMax M3 و M2.7 به مدت ۱۴ روز کاملاً رایگان و نامحدود روی GMI Cloud در دسترسه
⚠️
⚡️
📌
از
۲۴
اوت تا
۶
سپتامبر
🔥
همراه با
Speech 2.8
و
Music 3.0
🪧
دسترسی از طریق
API
خود
GMI
یا
OpenRouter
💎
بدون محدودیت استفاده
⛓
Link
🔝
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dStuYRTxuDXO9Uiww_PbzTXx03jSqHmojQPxdK3nC8nd8rvhpEZmyoD0YsjHmu_P10Rn8sqHtld_75Yauo9jVcirsNNAh9CONehP2mtMWZFgRnvcUwVVHDxjfGzR829hMtrIvpTSGhVyAWDQKMoAzCrbbMgC9sOZpOnLa4Fx8AijQh3aG0CcadXw1M2bON5uHpbuXL5a4_6eyB0-1cJQBnQiKV7R6qXCPDNzGgBdwmDRYaTBdjqUO9Ljyj7oSzHkFgyG1Dg3F23CBfzFg0Evnnu2Ii4djFgM5Tm98QCAWsWT3gL6MRWulNYHIwfRxJ3_II6JeIqN9QkXmWMxvPgoAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API بسیاری از مدل ها مانند
💥
🆓
:
Gemini 3.7 Flash | Gemini 3.5 | Flash-Lite | Gemini 3.6 Flash | GPT-OSS 20B | NVIDIA Nemotron | Nano 9B V2 | NVIDIA Nemotron | Nano 12B V2 VL | Ling 3.0 Flash | North Mini Code
✅
📌
Base URL :
http://aihubmix.com/v1
🔗
لینک ثبت نام در سایت
🔗
لیست مدل های رایگان
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrmoTKAOIRLlHGe2joQTchfHTOlnd-9ovJUUpe851oW1ZRnDkbYi4s5dwFxlWYaLzsV-Bh93vVP9K1pXT-7LyCjEG_z5NTE0A8p9RGPq1hO0a1BNSxCeHsFx5vt9nnUMgkAqhubSHUG0KlTnfKoMPCzGAbGrqiCDexR7Un_0QqlT8D_VJV302htMjTgoWT-jVtKP6igdSOllBB4AfcLxqjnBtQo3wL7WPoW_-vTRds3SyhvQ8aGMLX60I_IBHoFqswmMsIr8Br7tHLzD5wXp2NaCG5u5DHM2i4tApBqsVvabsx8OlARmnh5oi59sAVcRbuEyc4PNFukXcZmN8HREGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به برترین مدل های ساخت ویدیو
💥
🆓
Seedance 2.5 | Kling V3 | Minimax H3 | Seedance 2 | Seedance 2 fast | Happy Horser | Kling V3 Omni | Kling O1 | Q3 Pro Video | Q2 Pro Video
✅
با این سایت 1000 عدد کریدیت معادل 10 دلار برای دسترسی به مدل های بالا دریافت میکنید
🚀
✨
مراحل فعال‌سازی :
1️⃣
وارد
این سایت
بشید
2️⃣
پلن رایگان رو انتخاب کنید
3️⃣
با اکانت گیتهاب یا گوگل ثبت نام کنید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL : https://api.b.ai/v1
📌
Model ID : deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید …</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grIO-0KcgWk6HXmqMf--9KC72Ms4wd1AGGMkGgsKV7Szzxvp6ZzRv36Z8W02Fe1gBxcF4luhGed-dYa6pT_wSMmKWsucHWh18c7hvOy8Wzsk9Tn_JRwYhsbyE5uhC-1HZmn8lonVehOShDI-Pi1WrkO8sIbyOOz03ZqUJ3sX0wZYGaSlfpy8mqbycdAnSvvyaN8owQD0UGD0VSEI_TcoeRNg9MlLPXL_xkj52mxAmu53KbCg4PE9ZzAoozeHq2_NSSWNL0fjke5ZF5sE6fSBLCMwKKWUcn_dlosnR2TkUv_WL6Tz7SjWroAFEt-2RotR1Y7894j4bkPw6htKuhlb_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی رایگان به GLM 5.3
شرکت
Z.ai
یک اپ دسکتاپ جدید به اسم AutoClaw معرفی کرده که یه دستیار هوش مصنوعی agentic است — یعنی می‌تونه به‌جای تو روی فایل‌ها، مرورگر، برنامه‌های آفیس و حتی پیام‌رسان‌هایی مثل تلگرام و واتساپ کار کنه.
😎
🎁
هدیه ثبت‌نام:
کاربران جدید ۲۶,۰۰۰ اعتبار (معادل تقریبی ۲۰ دلار) می‌گیرن که تا ۳۰ روز اعتبار داره و می‌تونی باهاش مدل پرچمدار جدید GLM-5.3 و همچنین DeepSeek رو امتحان کنی
✨
مراحل دریافت:
1️⃣
برو به
autoclaw.z.ai
2️⃣
نسخه دسکتاپ رو دانلود کن (macOS یا Windows، نصب کمتر از ۱ دقیقه)
3️⃣
با ایمیل ثبت‌نام و وارد شو
4️⃣
۲۶,۰۰۰ اعتباری که داخل پلتفرم منتظرته رو فعال کن
⌛
زمان محدوده، هر لحظه ممکنه تموم بشه — الان ثبت‌نام کن!
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کانفیگ amneziavpn
[Interface]
PrivateKey = YM8CabYhib72x4z1G3Tv6YPTzkN1EgieYgzRAiEOXGA=
Address = 10.0.0.3/32
DNS = 1.1.1.1,8.8.8.8
MTU = 1280
Jc = 8
Jmin = 74
Jmax = 195
S1 = 115
S2 = 80
S3 = 44
S4 = 21
H1 = 220741314
H2 = 689752078
H3 = 1491205382
H4 = 2102461473
[Peer]
PublicKey = MF3gfbfjik3PoBeXrASElNP8OOXDlalC1ZCmLfqUuSo=
PresharedKey = 5AUecEnESNGx35D0nM1REFG1HAGtUuLTxlzhUHDhkSM=
AllowedIPs = 0.0.0.0/0
Endpoint = 65.109.215.18:51820
PersistentKeepalive = 15
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gN-71yvK8lRO9PBkeDvLEl9ZjI5OWxuU9LL52hMiKgKes-uZ20At7xt8Zea4vL2XxnIXC75pTBM4HxKpXV6iup3FIZYhixuTAGKz7V1aXRbiAC5rK3RuVFGzh0UkADujcYjV6Pz__Tzl1EP6lm0_fTQbA4YBgAOItfqz-hTz7X6Ad7-T6ua85HPri82ZZ0YASgfzLxxe-DFe8no2L7hT6oEzquDGVRJAHLfuVH2fBv78sZvHJ86bJvNNqBL1I1al3lkjB08nRYUaVfU194fz1NC4vqv7o4jtC_dkh8lE10TooJeGbLsGHaQjWtoBCX6bUFRa5Hh56bA6-8dBVEy59w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)
همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟
پروژه «روح‌گرام» یک یوزربات فوق‌پیشرفته و اوپن‌سورس با اتصال به Google Gemini هست که مستقیماً روی اکانت تلگرام شخصی شما سوار میشه و رفتارهای یک انسان واقعی رو شبیه‌سازی می‌کنه!
🔥
قابلیت‌های خفن روح‌گرام:
⭐
کدهای رمزی و نامحسوس (Stealth):
با کدهای ۳ رقمی مثل 777 یا 666 کنترل میشه و دستورات بلافاصله بعد از ارسال پاک میشن تا هیچ‌کس نفهمه!
⚡
شبیه‌ساز واقعی تایپ و خوانش:
🌹
قبل از جواب دادن، اول به اندازه طول پیام «مکث خواندن» می‌کنه، بعد علامت ...typing رو فعال می‌کنه و با سرعت دست انسان تایپ می‌کنه!
🎭
تغییر آنی شخصیت
🎲
با یه دستور ساده لحنش رو عوض کنید.
دریافت و استفاده از پروژه از گیت هاب:
https://github.com/faithsaly5-stack/GhostGram
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=cSCMkP1lxL-ZlGJ7mMS3D7L7wpZmWqCWUJwR-mhfN-xgER87rPulKH1PVLKKOOAb7Pgj71vxTNLAU7rEVD-HGotN0mQ-MdLROORw5wvtSivqCWI9OtvquihITFLJ3NvB7B3vDBRVs50o6DHAswzvkDxpouJiC6MxUDFDfvqJHS8ByxHY5Ok1M2QqOGeScDO-hGCMIsP2wnI_soBJ7dtDzy2n2oe5PR2B46iLCtSCYPorwVANRX4NyaIQXHwmqUosRgCVN9I1JoSXqL1XhV6z0V_aRKqSWVIVLIp35I2mh9t1c2a4hTqkTTUAgmNNybQeW85bpmTAge4QWLURkSRsnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=cSCMkP1lxL-ZlGJ7mMS3D7L7wpZmWqCWUJwR-mhfN-xgER87rPulKH1PVLKKOOAb7Pgj71vxTNLAU7rEVD-HGotN0mQ-MdLROORw5wvtSivqCWI9OtvquihITFLJ3NvB7B3vDBRVs50o6DHAswzvkDxpouJiC6MxUDFDfvqJHS8ByxHY5Ok1M2QqOGeScDO-hGCMIsP2wnI_soBJ7dtDzy2n2oe5PR2B46iLCtSCYPorwVANRX4NyaIQXHwmqUosRgCVN9I1JoSXqL1XhV6z0V_aRKqSWVIVLIp35I2mh9t1c2a4hTqkTTUAgmNNybQeW85bpmTAge4QWLURkSRsnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡
مدل‌های غول‌پیکر روی سیستم گیمینگ خودت!
محققان دانشگاه‌های UC Berkeley و MIT سورس‌کد سیستمی به نام FreeToken رو منتشر کردن که مدل‌های بزرگ MoE رو بدون کوانتیزاسیون شدید، روی سخت‌افزار معمولی اجرا می‌کنه. سیستم به‌صورت هوشمند محاسبات رو بین GPU، CPU و RAM توزیع می‌کنه.
💻
📊
نتایج کلیدی:
🔺
مدل Qwen3.6 35B روی لپ‌تاپ با RTX 4060 8GB تا ۳۹ توکن بر ثانیه
🔺
مدل DeepSeek-V4-Flash 284B روی RTX 5090: ۲۲ تا ۲۵ توکن بر ثانیه
🔺
حتی مدل ۷۵۳ میلیاردی GLM-5.2 روی یک GPU ورک‌استیشن قابل اجراست
✨
ویژگی‌های دیگه:
🔺
پشتیبانی از ۲۰+ مدل باز MoE با فرمت‌های مختلف کوانتیزاسیون
🔺
یک API سازگار با Anthropic/OpenAI برای اتصال به Claude Code، Codex و ابزارهای مشابه
🔺
نصب یک‌کلیکی با GUI برای ویندوز و لینوکس، بدون نیاز به تبدیل GGUF
🔺
متن‌باز و رایگان با لایسنس Apache 2.0
🔗
لینک مخزن گیتهاب
🔗
لینک وب‌سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=G1XTIYP0OZGBcHy3CUJwa6VV0tgxonjDKnBRdzozvubtCxpfC0zdXeNaPNlXuRQe0dAdgiFKl3zsf1-gPwZJvSbpRCfCeA8fvxlmsVbHVQ_iAIWZ53OsURVAMH2uY5ZcqrL-spPhrqHNM0sGVsJ0hW8YDUuGDl4c5RGYgx0UsRwrycoEOo3isk91r-6ihdgb-Cva-dI_Mhh-DIRKqkM038iv3LR4dUGq3k67fevGVYJINBPksdvuNkJDWiog1bA81wcdUgBP0R0zEnvwxXahS5AbO7jf8fKA8uLF0Y9w6lOb1RZEA1iuFfaKbgB9DluSZQjpi115zcMfCekEMp3pdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=G1XTIYP0OZGBcHy3CUJwa6VV0tgxonjDKnBRdzozvubtCxpfC0zdXeNaPNlXuRQe0dAdgiFKl3zsf1-gPwZJvSbpRCfCeA8fvxlmsVbHVQ_iAIWZ53OsURVAMH2uY5ZcqrL-spPhrqHNM0sGVsJ0hW8YDUuGDl4c5RGYgx0UsRwrycoEOo3isk91r-6ihdgb-Cva-dI_Mhh-DIRKqkM038iv3LR4dUGq3k67fevGVYJINBPksdvuNkJDWiog1bA81wcdUgBP0R0zEnvwxXahS5AbO7jf8fKA8uLF0Y9w6lOb1RZEA1iuFfaKbgB9DluSZQjpi115zcMfCekEMp3pdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE3BTHuaGj2LH7_qwq3E0MjlJxGbDGszI98HsUI7uHYNZRxM78sVZdItGwSpapF11zjtGSAlmaeu5iAPV0FuaAyBcLDnY0f2gqrYp8-Zqc_nKGPn1M7SZzPuoKASH-D0nauz53IZyzu6PuQjilKXJ0Ek-kj8xlOqlsH0E07G4UwxNWTdXqzgsg00i66XvnpdJ7cNHWBryrgF81FnKRkoUUmHPy_Hi2IbUQeBzsIzpcsUTG7jReV_EvAPtyIgWq74OnGOYFBZ6DcPxa60D_LR_GdmovSDfjaHGEKeQHFaDNyf_8tZc6HNuIHPpK-h2Pc3UBxC8xXGSg0SLBJSCmNYSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔬
دانشمند هوش مصنوعی که خودش مقاله می‌نویسه
یک پوشه از داده خام رو بهش می‌دی، یه جهت تحقیقاتی مشخص می‌کنی، و سیستم از فرضیه‌سازی تا مقاله‌ی نهایی PDF رو خودش انجام می‌ده.
🧪
✨
ویژگی‌ها:
🔺
کار با هر فرمتی: تصویر، صدا، ویدیو، اسکن سه‌بعدی، جدول، فرمول
🔺
درک مستقیم داده‌ی خام علمی، بدون تبدیل انسانی به جدول
🔺
سه مرحله: فرضیه‌سازی → آزمایش با کد واقعی → نگارش مقاله با DOI معتبر
🔺
اعتبارسنجی داخلی: هر عدد باید از خروجی واقعی کد تأیید بشه
🔺
سه روش اجرا: دسکتاپ، CLI، ماژول ادغام با ایجنت‌ها
🔺
پشتیبانی از Windows، macOS، Linux
🔗
لینک وب‌سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADShu50gYHU8v_7VicT7CjwZAFi2cwdbeeEV2-puqXyze8mn81Cmz9Q-6vTBnhOJGGEiaLrsz86dHlKFYFYXVmOXfrwI7xVCsBvhAKfnOCH72wcT-eghz3N8VdqYZmQf1RKFllUvgzqw-jlxNoYm2QKedd-9b35knHySoU0WppJqDzN8qOP7NGhLDcJ70BxGnF6fhtNuT120I1R7DyHvGl6pmyak8-E2ob4rdOMbMeDVBTxrXXD6yuD5h02Tw_cqjcnqHkR60ZjCb_EVXZKppYNhIfpTxMKJLJH6tF0A8esM616CZExZjnlQrbUCBJmwEYRCGREfv977ioGbNHATsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جدا کردن صدا و موسیقی با یک کلیک
یک ابزار آنلاین رایگان مبتنی بر هوش مصنوعی Demucs که صدای خواننده رو از موسیقی پس‌زمینه جدا می‌کنه. کافیه فایل صوتی رو آپلود کنی.
🎶
✨
ویژگی‌ها:
🔺
آپلود فایل محلی با فرمت‌های مختلف
🔺
جدا کردن خودکار صدای خواننده از موسیقی
🔺
پیش‌نمایش آنلاین قبل از دانلود
🔺
دانلود جداگانه‌ی تِرَک صدا و موسیقی
🔺
بدون نیاز به ثبت‌نام یا حساب کاربری
مناسب برای موزیسین‌ها، خواننده‌ها، تولیدکننده‌های محتوا و ادیتورهای صوتی که سریع نیاز به جدا کردن استم دارن.
✅
🔗
لینک ورود به سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1ERpR2kjkRF7UOSwVAC12XzVUJXInHV65ZDQA-3AeqsysNlAN7BPQdEJMgvNbmNI0ZyLQzCwqAFKs1RkUqwx3II49xgXswMuB0c5qFXCIoR32dpTsi5RZN03JIaihLjE9-w1RNEnJ13xtvCHXJBY_Ux_SRZPjE3uoU-8eT2hiuZuiCQ-RZ73-Izf3a7mjLQi-sT8MEQXUQyOZ2EIx9jlWmC9T6-sTbrs1RSup_oue5V6LsZJJTvd6GIKWXMIYP_f5AJ6y4D2TzzodMioR_zZfmHyX5b8Tn3dhkfRaPq2acIPNFRv73DA-GyNezDaoz16NiXqHhUODDbujDWBYy3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 دلار برای استفاده از API مدل های هوش منصوعی زیر
😎
🆓
Opus 5 | GPT 5.6 Sol
✅
در سایت زیر با ایمیل یا اکانت گیتهاب ثبت نام کنید
( ابتدا کپچای سایت رو تکمیل کنید )
سپس کلید خود را بسازید
✅
📌
Base URL :
https://true-sota.com/v1
📌
Model ID :
claude-opus-5
|
gpt-5.6-sol
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">DeepSeek V4 Pro
| MiniMax M3
♾
♾
♾
♾
♾
ApiKey
—
sk-dc9d4b7df36ba555-rcaq9e-2790fa25
Model
—
am/deepseek-v4-pro
/
am/deepseek-v4-flash
/
am/minimax-m3
URL
:
https://anymodel.org
♾
♾
♾
♾
♾
Free
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">5 میلیون توکن برای استفاده از GLM
💥
🆓
به مدت 5 روز هروز 3 میلیون توکن برای GLM 5.3 و 2 میلیون توکن برای GLM 5 Turbo برای کاربران جدید در اپیکیشن Zcode
✨
مراحل دریافت :
1️⃣
وارد سایت z.ai بشید و با اکانت جدید ثبت نام کنید
2️⃣
برنامه Zcode رو دانلود کنید…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=ZH9gaiq_CJx_XvtYQrKwm6NDqvV_VKsfnto5P8q6lkOr_vAcFTRCb4Mbg2sgvXRyjGf_VGOi4hAHmwyGlbhm3ROCvTbongMg3sFMxr81pk4e0WGxHoaTCN1g9iuXIgTFE6DBArOr-VxKzMlRW8sq51XCC-NidGrWhVwi7Kn0KYZWHuwOmmOstEEH4j3ic8hYDn2fl_PUpgoCnjvqp69S9CY9uiGWybom6EywY0GsulTekDN84o49Hn9gdYDiACp02P5BvqiTMCa4tNExNEnk3IiKMbkjjV1vaV8cuByp9GQnt_AI-1PPEkGa3yyivV8oc8byjU8I45TbdMHsZH-QukvXLpCH27GK2B69e4gsSH__RBgxdss6DfYO4Ym_rccxPvG7trgKz-ugFfBBi_V1_vsTzYyRdp8pBuOpcelFUHLTF-w67Cds2SOoG0NlU2yb2J8mFXf8vgZCorq0vQkx0TSyhv7UiN-7OTx3k-clqizif_oZzLZPHWDeneAj0acLLaZ4KFqxXkM8obp_PP_BBuw-3ebXoMLC-PiMqlYcMRytgABML9TJSgVMrFeIqHn98sZCIfgpIy8lIrb89DIQ3HnpdVe9cY-9GPDsN2aqae8w4Ms98nkd5tYp0zr6YigmfWy_vkhcqKv9UeMSrmBFkYvAAVwsxdx_ZgR6VSud1eU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=ZH9gaiq_CJx_XvtYQrKwm6NDqvV_VKsfnto5P8q6lkOr_vAcFTRCb4Mbg2sgvXRyjGf_VGOi4hAHmwyGlbhm3ROCvTbongMg3sFMxr81pk4e0WGxHoaTCN1g9iuXIgTFE6DBArOr-VxKzMlRW8sq51XCC-NidGrWhVwi7Kn0KYZWHuwOmmOstEEH4j3ic8hYDn2fl_PUpgoCnjvqp69S9CY9uiGWybom6EywY0GsulTekDN84o49Hn9gdYDiACp02P5BvqiTMCa4tNExNEnk3IiKMbkjjV1vaV8cuByp9GQnt_AI-1PPEkGa3yyivV8oc8byjU8I45TbdMHsZH-QukvXLpCH27GK2B69e4gsSH__RBgxdss6DfYO4Ym_rccxPvG7trgKz-ugFfBBi_V1_vsTzYyRdp8pBuOpcelFUHLTF-w67Cds2SOoG0NlU2yb2J8mFXf8vgZCorq0vQkx0TSyhv7UiN-7OTx3k-clqizif_oZzLZPHWDeneAj0acLLaZ4KFqxXkM8obp_PP_BBuw-3ebXoMLC-PiMqlYcMRytgABML9TJSgVMrFeIqHn98sZCIfgpIy8lIrb89DIQ3HnpdVe9cY-9GPDsN2aqae8w4Ms98nkd5tYp0zr6YigmfWy_vkhcqKv9UeMSrmBFkYvAAVwsxdx_ZgR6VSud1eU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
استودیوی هوش مصنوعی که خودش کارگردانی می‌کنه!
اپیکیشن MiniMax Design یک اپلیکیشن مستقل برای ویندوز و مک‌ هست . کافیه ایده‌ت رو توضیح بدی، هوش مصنوعی خودش برنامه‌ریزی، اجرا، کنترل کیفیت و نهایی‌سازی پروژه رو انجام می‌ده.
✅
✨
ویژگی‌ها:
🎬
ساخت تیزر تبلیغاتی، گرافیک، بنر، محتوای کاربرساخته (UGC) و انیمیشن
🧩
ادغام فیلم‌نامه، استوری‌بورد، ویدیو، تصویر، صدا و ادیتور در یک فضای کاری واحد
🔌
دسترسی به پلاگین‌ها و مهارت‌های تخصصی متعدد
📂
امکان وارد کردن فایل‌های محلی و اتصال به سرویس‌های خارجی از طریق API
💰
بعد از ثبت‌نام، ۳۰۰۰ کردیت رایگان اولیه به کاربر داده می‌شه
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlI3n_MHONiWk-0bqjuUG7iaKObjzFTfTWg5CxgJXjiZNqHqKC7AtihERsV0eOXvsFyisFbYjqcIMeMP5wusnnTBTRkibRZM7SObo_Du1RxTceoKdxGiwI-oEit1uVUPG7e7Y8I1uTLW8byca1yDlLzwfeiiwXwL4qOqrpxGuRRdMOl4CEqONScxaB2NCxBvx2HFmHmIMsG2Dj0hoqLb52TtkHlrhJ1FgEYzeEmuR9hd01H79ON-inoe015dBFZNJSg0wGZsJB1fGrlbZlXXXzK_h2hvF1BzLK7eYDUB5BIfCgnIUgZFBe6W2MQpNmIB4CZgWl5VaKqSULrDno9dzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taUvfa_UqY1gDgAW751MbsK8QE0oR7Ldmkp4qm9AjpfNwPnWzoDR7NOYpSstKM5ejHAPT0tv09AyRCUBVkkd_5-HcbbmZkvYewLhcejp0KA2B-DYDCisWnWRQDWUPTFo3mtmHvbZ1XTOMT7H9NgQMfeGZzucdMyxzCncPI7QlogJGyY4U53yCPMaKeJk11OZQNLndZ38VYc4zhi3M48fCg2vimGsZ6PDfMCwflJI6FCxI2e2RkF8Isp95hunbOTQmq61lId1NRb5xP54E7yBArC1M0z5NBX4nBgnJddhvtIIisPPiuwP9cDOmuFskKNPxzDwL2tTyX2MvVrcYEN6eA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blk-66e9UbSc0cg6uFgopwM3lIoa97AZ0TCVSBXpWqWji75v30Fe7cd1FpeV09FnGNg-xHfgl-MO2nHZiP-g9uT6cY1mG9OsgoicD7eg7GRDXWg_Yim6901GAyVxi2PKq25P7JEyUCqTMN7p91D8kzoFBMSdVnzZN85ErJYehqjHfLjtI2WxglDc97YfVsnt885SPw8qoeQRI9FcoWgLZLP7QBMP27ZO8YsD57II5-6O5e6sWS_AygKjoTsM2xsfXexpzjNiACQg6hp5834IMpOOaYI0yaUeReB_smntkLJLgq_oDDxIIxGtFR8Ugo3hvnfMsGS1_gODwbKIalGiuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7537" target="_blank">📅 15:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7536">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6lJ_GjL6ewTs9xs3ZXRrvFetn0h4WqkIE9A5ImjXOCJ0KVWrwKnl7mRAxsmWqiR2yZHbLx6ryc0yqwL8bhFIYHbp84ZEEDt9H8lRsOdOGIu9Xmhqn8hnoaIf6pV32ak5H7qaRI0A_v7XSYjuq8fCjMdYLwGmG125Y0BWx2bmMDNXkFTVlYuEllX0BAuc_XeioeKLxg25eSpympGD478OevV-mb4kyWJse1JQ34sPClBAvSMz6lHiZqqvExtQ0y9UK9EXwy3TLRUrU7NvNI7vAZblBQfF-ZHtUDJ4tCYpWvsVdSkIQacWV5XtKNGcn1z9vrCaVVAiLKCRxyM7PttzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D64jo8Vpzl_DXtEXVf2gUwwOcrVy1SAAwvizi7cblR5ZI7KwnEh9y-5v2D9u-vQnFmVEfKXCrqicsc39p6oN3AxA3tH_saeoXmor49XSf7JKiY-0KDIsfA3S1LOwBnsOUqczrzWqFmEOKwCBLjRlTwXBp2fEFfufBpjLH6yqTcWfI4E6IOlsMBdm7WwrIJiVb0kJ2pk35FBy5jo5UCRlP3_Mk_HnucGShscceBf5VKQtxBqfhLGGwmQip9xJz-tUBp5nY4tHztRwEo12ZuhKV5RjaZruX_emd65BJ1Ux8xwMd9-NFSZjZM1oX3C_Qn3XSWyLCivrVRAmppxFA1QdeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7534">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVLUTIAFx2Dh1a7miGYxhbKEp-MBCXRrARxlbRRTYkE4f0woPO6_kGoY7o2vRTdj9U_eqojGHi_w_Ue6pDWuXii0VCpbz-qNKu6rUslkGUfFhIq2CN95sdC8KTDycbXjetUhuvvwAe_NqhBddpEIXaP_G1zdV7UJIeTdH_PQO3rPQ_T9rKPutswD3rwpi4v7QEgwdNqw4cplZHRqpxndBoUjfyZcphvr-D6s11Hcdc64nkuIDAhi8F1IwwjsMj6fyVLV0iiU7izY1mSU24Cmg6pRxIqRRsYAVvgHFRIl6Yv9JDn1tqTlS6R63_aDrjjFITVj525nHSF4g08mraFruA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=ha_tMQXL6jQ6zcjNCh2qlLgsOsTZLQHkYGl9z1UpJ2qznvt9t-8hJPW2TwbkDEQnAFPEtTsG9iXGirJZFVsebxVhGt4r4jOMg6ESpr_cBVbyvMzr7rpcl6r3vR7yjSzQuOjkzN-bl3VBeIlkLbGi4fwD_6NAjekgBEauHN2f5K-5diLqOh43O3Fs_IS7-Q1fbks9kvDXzlKPBbvey0UFh9LozMNKx0KdDvVpKBWJKbm2qLBnlddPKbsxSs6Va237H9LXAlud-sf54PYVc0S_xVKe2sGQA9Th1qMZHIjufhRzv6K3t7dOB3SUW6WnO3kETTSH4T1a6OhkBQBNnx3JXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=ha_tMQXL6jQ6zcjNCh2qlLgsOsTZLQHkYGl9z1UpJ2qznvt9t-8hJPW2TwbkDEQnAFPEtTsG9iXGirJZFVsebxVhGt4r4jOMg6ESpr_cBVbyvMzr7rpcl6r3vR7yjSzQuOjkzN-bl3VBeIlkLbGi4fwD_6NAjekgBEauHN2f5K-5diLqOh43O3Fs_IS7-Q1fbks9kvDXzlKPBbvey0UFh9LozMNKx0KdDvVpKBWJKbm2qLBnlddPKbsxSs6Va237H9LXAlud-sf54PYVc0S_xVKe2sGQA9Th1qMZHIjufhRzv6K3t7dOB3SUW6WnO3kETTSH4T1a6OhkBQBNnx3JXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_WOCAZgpihZH9Pux_VJYf5Jtbd9YJIRLqpoUFwmgQJ_LScrQrygjDv0-0EN7qjmDBUeLrMUGRdINXHtmkLAGEy2qs2S0NdWemslVieVVP80bN9OazLoswpXQ0yy5ricAIZfYrLWcqq-VV9nrD4i2nH8GpABn6-I9RNSVzU0ynN_izEWCv5j2gz3_xI4Yg7sl8P_Fv-bFkO_cibaAicWjSITzpJA76ubNeSe5wwNl4x5YhPuZqOsUhW0hXlVz37ykSMrqEbbr-a02GVrUTRyniaEn6dQFMLiVxJCOSWopWia0V81F1CfJqHfFGQhmF7aqUW0m3RSkOo0ZmQNPtKzkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKaNstTPWWX5B1G2CtxJU1B81cuhY91ylHqYQ1pNEgQvgOLtNhi84nScP4EcN0ASBHk-8Y0CwRKhwW3ZInw-Nszm5Hf89Ys9sC5DZo5XZ939yvJO0ezwXnCIfGVHK-XnOOvGFz9wnRKEkLGH-CSQbGt3nqNKQOiAgnz4zQ_3NfoOycDlpYML2AYiKMxLts-EngJtgaz6Zzxxc7ihfaeNnbGUu3zuo-JW4JDTtDkWjmb4ZdRpKrWsi8GP5_EY6kj3_j1g1UJw1qsEwFeNAfEXitcs_IUzcOsXVwd5JBbC47GgG7cE1SyD-y2p808cbXEOI4-szFonuDqIdNcU-4vrdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtlR1dR73KnlD2wW8_RPSgnaY7e1EyxCDJ2CHt0SuJcEPa-N6qhthjjZdLXuuVxlejq2CxkoIEmLJfRBi6Kv9Wqesq1_5Xc-tL09MOu-P12Ps4jGIdzrSUCma7raBlgpG4qfJIozH-L_nbOefGrJeZzLMz6FzL5LXprVjRlM9_L41ZNvM7geMLEeYT3XcaY6k5Le331RzFPZXAdw67wXMlsayZj6wkOlqOFESG-FVQ33m5Eg-AbjNkVaXEgPxlf82FYLrCvM8RafcDpaJKAxy43kFNeE7Vus3mcQ--f7-YfjtkeZQITUhTDNZhv9eqylXvLy9GYqG81C885P5N7Eyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVAAyKLcoT6YApUGn5uwKN9oKI29J4CxR0CduBQOMc1q9_9BE9UmrWIZ_q5nYKoScUB1WKB3iJYXzQqf6rhJ0FaaB6a6IwUboOIXgNXtA18qbk5KE0eWoCLAn9ZYgztUxBTYU9n3wH_8ggrgpx7aSwUP9edOow-W9gtqo6fhf0d6GKV9_XpHaB_apnN-fsrhqqV0s__AGliDqX7tfecPnqtS1rft1sJHhEDmVrq0hAjofkK6j7lXtyrGu5FQ-1fZR8cbhnj88VMkdhw9Pjejmv18Ga8b4IB6skeaRiTjUzTJc_DbtBs6q0PTnKJnDdYrRABRPGRnB6pdIw8qkagBbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7525" target="_blank">📅 20:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7524">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoKPS7w0aqIWhyZVlUdHKmImC-tXGQgUPtavG71h0v8xQXmE7-PDfOPBlng63QCu7dnxWBKvssucaWQse9wOuPAFhidajatVf3Pg7hRBqD5yCjZEXPQUf9e5MCcPV3c-9SCgt_dSYCzeZeUT-7RyxACfbE6gSnGHoyBj71WYeSsmmaXd8uACi_RWV3_DvK4eBIJXq1d0ZuoPaD2NNb7IHLaZycK399f2-Hp4k8ZEnSQ_8kMtYeLYjn13LbXP3AN_fJTgg9JTkF6xcQSiSca5Ex3hoaFq_4BAmDhP-eYeIyhbOoNFCxw1pk3Gk-5j-z0miIrfICXiCiWQDhefwkVdoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7522">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-5nBtuLXPiipIk9hi5FqYcFcYCb4c0UbggTrkLnoVnFxqV3Bh5cg2y-_JZxKajwu4H7M4N2mufv4oJ7JCoYynm3U7SIG50Xp1dWOXgJi-YLeLbdxSdAjTb_JBdlvjORHleH-d9WhagVdMHpjRDhXUVAz69jFkIEoa2TQAOO-Apz7uV1u0ouw8Csnm-v_Gys-T__yP3taYpiV8rODk1_HzBvEjZhp8Jz74PEK26k8NUMg52IP3pE97J5S9gIOY8xa9hnfGKjBJRxmn6v5xonNKfusP2JVs7_Ixoe5Kla7Z5jdFk0TU6gQOrkIzzHCCq_YQ-IGciw9U_KlaAXIzvevA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdleeS4LHjfWXxv1wDHZah9mgPf-u1oTtn-BuUN10Z-n6r2Guf_lL-NPJBCKpgxGShZ0_rOVIqXlCtnYnDLfyV1Zb6kVew3W7XeBQu-bqx5oSK5aY9LKBIt75SehTRv9HCUN3F65JcuCkgUJJBfjWR6JE5r7PDIpHbpBBVjqYFMZNwQ-HG4PanX5Cwgc3JKycXRx5QP9U2kMcPDWgyslxaRztXTWPS4sDx9xuyVlIEoPo9F-B8gssMjPZwrxwqRwK6mMr7W80kuLVDqFUuWlqbEiCgYgtkqa24TB_6ikXH28Ws5tFciA7hyfnHyzSgGdvLpv9uFdz6_GfeEL8UeR9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7517" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7514">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSmfjsgjKnOSXEt_KX6dvFa1AuDouHaeXsEywHG_kSftOyZ_CldizjHB5xIU_ZAVhMTF7rRid0Xe-t0pMEmT0GhAFB1DdCnq-FOYuEaWWIKdyUWLOYHyur77BWPGlDgjxcmGn6mZ3IEoIyLcdHT1Wp-lF18Q9qfthCIE0D5jKuvS84wZhSLZIfbTWgfP3BYi0lnIe6F9o7LtyBqQDyYocYAwQo7nF96HMp5paWLXgUKrit834uZNW54yL5nVSmDnvjOxTVugDR_LBht72vN7DqAgW6QMWkv9v_YqudFnbJxaeYoUbHkPaSuBDOXTGZhrj9JkgS-vT5JYCAebUDoEig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6q6zhBda8jp6dxKLPUnsBW7QQIEBce5pkPtgjKbxpW-n-wCUAaFrnw-q5lcmOncI1nBFHmEMNLp2opQPbN3RRkJdFQrL_UOWoMawTE8s2PtyFG4b3DGsBAIPVXz5aqK4GUZpIG_Xdba09vjxC2tJCU7T9mZ-MdEd84OnKQe9KnOTARfs64ys-m1AWem3SERJdm5JC3PWMO9U6LOOHkIQWKGqWDA7vO3V86GiT_FUV3RPhXFTG0wBa4t4qDOMaNVLOLxiNW8ZtxJ9kaJUXu1tsIu1fuEFijtFJzh-coz6ry_GwzIj6u738DCMmKEgXUEO1gFsOxd5k3qexy6KHaOLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=Cxz56CQKkUgy7Far0VFRsxmhPAzyVU39L-zuKpGLIDQgyiu8TsyJnNZK4HxvOmU2ag-qYdXUSy8B6WCTAs4h4Y5IC7z8NKdm2--V5sk8aJQ1EPmo7IDOd8EB3N_DGME-swUZMmEwu7UBSWf-yXZLDSpOaioJgXGqWmPV-qcxA1ioIjUxm1UqQ4vII8jsTdVjMgWAY75Xqv3HA7-vfZNRl-CS2hrpFMX-q_TAkxtYzCKER7LmCgMYB9rES9KsK3m8R-2VPyZRAGUoC3pCFDnHLlFTYums7Pdzeum_VlQV7Z0yuobjTWQ23IcsQbWp5oDDPnX3sEjhU54bDzp1AMzAtYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=Cxz56CQKkUgy7Far0VFRsxmhPAzyVU39L-zuKpGLIDQgyiu8TsyJnNZK4HxvOmU2ag-qYdXUSy8B6WCTAs4h4Y5IC7z8NKdm2--V5sk8aJQ1EPmo7IDOd8EB3N_DGME-swUZMmEwu7UBSWf-yXZLDSpOaioJgXGqWmPV-qcxA1ioIjUxm1UqQ4vII8jsTdVjMgWAY75Xqv3HA7-vfZNRl-CS2hrpFMX-q_TAkxtYzCKER7LmCgMYB9rES9KsK3m8R-2VPyZRAGUoC3pCFDnHLlFTYums7Pdzeum_VlQV7Z0yuobjTWQ23IcsQbWp5oDDPnX3sEjhU54bDzp1AMzAtYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7512" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7511">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7509">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7509" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7508">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfAy3eQnHvxqkbKA7S2OzR-u7da1O1cOQYkdPNIvVNtnxL6a4beROnI1oEOYLeLw6F14RdsirvCf357f74oHUkyEQ9aRffL9NdO0QnDM4yHAfF_1jmAoZ7WoJ5CXtNzalWY796BajfPAaQDQGbcpeEs0-Z71zG1Cpc_OTXc1J_UzPFra_kKyPwBeqEPSPC0BgSdYPwo-8WftQrh1-oToe1CJ3IuaurKDHtL410H2FEJgrKk6KBTxDD4HqE6TblRzT45IcCyl0YChHBbtOip06knHrxz-MYu_ihgdow18omJlsOx5OckMIRh7fTl7fC5yXI0Aj4yDPLhSEpFLgUXfAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7506">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7506" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7505">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdOslCgvfC0H6bNY_T12nNgUHFBo3Y_XgtcQqNhNJpoJBDixAo2A9jF6wsrPUYzUDGqF81hDDGcfGeo_tQWCBQN_cDpUj55jDCOhRSadg2in34jZEn3y1F5NS8_1HCn7FFQBp5EkR7D_odk-QSCy4-M3kRaxr2uP0AaFrr-Oy2srgZgKfbkSyW7KBJt8p1wLuUbRxWoe747bzNJFkDeCcg-lZbB0uxgIVAiPMRqhEirOuyxC1cRf6poGPrjWMYaGCv-6tEasshN5THjbu_4_lA6Q3Xp0D7fGqc_v2wZrFo2sYrshCa6n-n0NkvV3-0mjbd-zm8Vgcq5uP5fkqW7MAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6IsqVPko2dlWTKanza6CV8WGRl-eOik7X7HguVyaBza6o9DxyxAhD_9zEzTf4FNU0onlULLqqFSenhl4BU3N6DlB_TBpfFDWEJMd0Q7dR0gy8bY9xjNUo0Hwo36Ti1sOBHq1yP3yO3HhhDpeoJpg1_-0ibZ6l5wHAxxXEKW7xWRIrZL5lNMY6qmLFTOK3HGdZvsXVdMYp7RXa7CVZugRSdCEyI4souzwayCO-p9y3rL-WEPsBYGKfGnVsrSPrGxYRw1wmXizqAflPAmUzx6cC-IJkkJdHUjmumvaDSL1jqtuPqJJsKnrbds177cFzZFejfMGPsDPcd9I-676jDJ2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/ArchiveTell/7504" target="_blank">📅 13:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7503">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7503" target="_blank">📅 11:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7502">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbtSvqHcU6XCvgi8-Ean48x9bVENqJ-FSu5q9I0G9s27cr61YRqXR6FnAbp7qVujvxjqEVvilSWYTMjVdn3Bq5wJRK71y-GfJiVJ2GdLHI3P8y_5NpGr5VTRJ7dk28BqlWwyvnCnabXe45VAnQGr1hFDKWgLE-GyuNNoLfvtbj063leb1Mdr5X4QDQ5ViGv1HXkznU-svsKUSMIhr2WzNDSTcHIgo5m5UAingo9noypZlxwRlEO9oXC7dHDeYYoSIKevHytJ9ESKYTVFB97s8SgvoIYOSpsLvq4cYhAH1GD-n7PJcZpTBppQBLmLOMKb23wFXINskNfXLXGwDU8VuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7502" target="_blank">📅 10:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7500">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=UR1A08jGtnOSpaUELcsPlEptYCjGoAqWTZEN0pZtAQjWUSeCBH72B3woyy9EhBBZppfHpDHP3gtbK11VkKhn8PtxqI15_xnGzg6iWkSFkrxNEICycMOa8FSZ3Vj5EUk6jPfzLkOM5OXVVdys2CeWsVVbVN4DPguuSQbKcOQHvJ6G76SH-1jPCt7DOyxdHfVNh6mPIKOskZLY3csTju_TrOsnBlC3FAb8MiZfAERNT9PlHxp7pGJ_u9TaRWxSepsz-J_JARg6gIBhXwMkcSZb-K6iGbM-EyCcNFb1Mj2cDZQGgnpLhNW8Gb86XnvxS2UFLEx9poQE5NCps7V6SvmGPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=UR1A08jGtnOSpaUELcsPlEptYCjGoAqWTZEN0pZtAQjWUSeCBH72B3woyy9EhBBZppfHpDHP3gtbK11VkKhn8PtxqI15_xnGzg6iWkSFkrxNEICycMOa8FSZ3Vj5EUk6jPfzLkOM5OXVVdys2CeWsVVbVN4DPguuSQbKcOQHvJ6G76SH-1jPCt7DOyxdHfVNh6mPIKOskZLY3csTju_TrOsnBlC3FAb8MiZfAERNT9PlHxp7pGJ_u9TaRWxSepsz-J_JARg6gIBhXwMkcSZb-K6iGbM-EyCcNFb1Mj2cDZQGgnpLhNW8Gb86XnvxS2UFLEx9poQE5NCps7V6SvmGPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7500" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7499">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlaQ1iWnfNeDupDSGFnP5UvUxDWNhodBtRW8i3-Xn1fp5RPv_2kpzE1QMalHcvhgtfKNxZEbw0LwErZ_O4YBb0J1ZRM4ahmaclHYuZrUTzeqLzZepAQuSIA03n1O4uRKfnoNkA0lZ0OhbUw-ufZeHJ_bysQD6RyK2gYCMlKd1CYjWRFxLou6ldFYM9q6rm4VYZNmc74rVMLGsolKxSBEOcRtFo5GwYShXClM6ysL-ISahadKyAwSSGHVhTrEjf3bb79aiWFLGgrpKyDo3hSoEmdao66-dMuR4qLoDET0fT5r9goLjkXoyH8WMafUdr1fip070mJdpEKsy65con88Zw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7499" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7498">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=J85C7_kW3Zk90vm7v536KPRlbCq5RAGB5Ruul4prRebjr86ydclT1e-RWkqtq3tg5jRCSBLoxHtsKrXyPYvEZsiWMdaNLdqCxiXhHarBk9b_B5YpUCmOSHOeA_jpB0OiKgZfECVaP0WTCRnmxqQZXaaegoPnRoL7u1nG_w6EKLnuq_0xdViNTb3Rh0fUeC7snjFUuRi6gk_U0UiaF13ZokCRaOp6cqdrHjaHhbIt05RsnukALAw9HzQK6Tdnj9MENTqcaugXRyjfWn9cJUE_1zvE5GwpOVV3tWoifAKnzhdHrOvHy3HoRUy8-YgcHKWvdfVeaDrRgFg-QNW0uCkH8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=J85C7_kW3Zk90vm7v536KPRlbCq5RAGB5Ruul4prRebjr86ydclT1e-RWkqtq3tg5jRCSBLoxHtsKrXyPYvEZsiWMdaNLdqCxiXhHarBk9b_B5YpUCmOSHOeA_jpB0OiKgZfECVaP0WTCRnmxqQZXaaegoPnRoL7u1nG_w6EKLnuq_0xdViNTb3Rh0fUeC7snjFUuRi6gk_U0UiaF13ZokCRaOp6cqdrHjaHhbIt05RsnukALAw9HzQK6Tdnj9MENTqcaugXRyjfWn9cJUE_1zvE5GwpOVV3tWoifAKnzhdHrOvHy3HoRUy8-YgcHKWvdfVeaDrRgFg-QNW0uCkH8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7498" target="_blank">📅 22:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7497">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INdfsOFObW-yrfoRp34W7s-eFXFlWfduykLPeYMVjqdNOeyBXE8c58INMvtzgE8VSn9Y1lEmwmMZM-Pel5hNlLMrGrbQZ6GrF2YqkPW3FktCWYepzd_YlWaZHsGgSUfNCJyWe6Q8yqGRkH69LBMuv7Vcyuq9NkymYe0BqfRgQyOE4-y8KjJ27bv07ofN_aWjQJB5s6LWaMg6DVJ5ueCOV25Q4YWSUEqRyYRdY3arkxj7EJBUG55Pljn4zdR6UifLYzxqmiKePTfKQHTNDPRrKChlruOpesIgoUkAVA36Aadm_KGc9Lp9W6ssSRmwhs-DvpSABgLcSSqZwhGT867YeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7497" target="_blank">📅 19:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7496">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-jtCNeayOjjR7QKilqRmk7ngoF6yg-r5TT3e0R0oS8KzlR4eqUmHYXT5YhlBvju7StqiJzuv9Zgoipi4f1yLGtqnahQuox9e8-N1h1LvtaIy9yrY-gBLqiI2jxA31kZJG2q-FqZnUhQ07OtKOpvmeY8QyPrSevfz5NMxuOX5QVqn5rC4c4b7sKdzT9dhBiYYAVOIPyx9HXRF6G3OiZwzt7jzFJDBh-2TEF9MRdtHmpZMOI5VJrXVX-Ytk0NRV9Rdg1KAFh7tBthomJxnIH0AL4oep72sqtK5T0CM59uTgcfJg8U_8Xnn5hRazJlWEWU7L6MXjq8K6lZ-jXc85xGgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7496" target="_blank">📅 17:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7495">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=AkxeWg2JAwxn43yimKh-eadHMhshvVBgnZnr8Cb0FImSFuelU8a6CwJfenMOhjLQXTJTbAc57GxJw1j_GYhTOc_XNcf26THCqJq8a76fTrHSiTwKeaoJ4-Xj4ACD4fYwbOBa6gIGWwb-JVbxjL0fHt5VvdlzXFhXgIZpl-2RmAcCsG_briJj86nf8RoBaf1HPMHRf5lKlviW9byrhA3g2EhBr5EphunURC0aFPA7mmdc_-DWnsjSTFLXkEwWWb-UL9uTjfYWRiMbXV3t4r6c7PqrTsPAPhYhe5vBFirR590hVTNvxkM1XZYE5MXh-j_TLXKfMF5VPzzo-eqyrXS33g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=AkxeWg2JAwxn43yimKh-eadHMhshvVBgnZnr8Cb0FImSFuelU8a6CwJfenMOhjLQXTJTbAc57GxJw1j_GYhTOc_XNcf26THCqJq8a76fTrHSiTwKeaoJ4-Xj4ACD4fYwbOBa6gIGWwb-JVbxjL0fHt5VvdlzXFhXgIZpl-2RmAcCsG_briJj86nf8RoBaf1HPMHRf5lKlviW9byrhA3g2EhBr5EphunURC0aFPA7mmdc_-DWnsjSTFLXkEwWWb-UL9uTjfYWRiMbXV3t4r6c7PqrTsPAPhYhe5vBFirR590hVTNvxkM1XZYE5MXh-j_TLXKfMF5VPzzo-eqyrXS33g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7495" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7494">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIv0J0um0zO5RV2lt96HwApAYQBfMk_-Axkd2Q1ZuBsQdsePpwrUHseQhJhOCtrdaUHSZ4Ini5C6O1UOw5HlB5qwhIqB7LjR9xcQSUTYw1CDYA5WjtiFqX1sRnEoRQTgb2S5aFY8coH_OvWexitdp-5ecEgZx_3x5KE51hihh67a23nYn3CpUs-4HIpQsPYiLYJewW7n7bRS7TKiOUkN_JF1ssRz7HRDW9sEb2YRhJhoFMk-qB--9gpypuO5RYsvyyl-8TuBnnuj0DHDt94CQe6fmXOs3VpO2vgRMBzJgQjGNfWuaFI7i7k9rgZoEhREKI6da6gJfzsNWvUZPtyBDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7494" target="_blank">📅 13:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7493">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNlSqZLtDvO-LafEbZbdgXc7VVFB83ldtQhrJylJukCHb2h1jreEqwlYnd2pQen_OAo6-CpIKgti3MoZrMYQvQvZWlV62J20LmIh9V-Rt4urszAgy1gJDXen0tOpE_sF9p5oyvkHMs8kIXI7rj0oWCsYj1Qy52jgVV13dDdOd401OQzYxdxAUGs4xigWnG7oUIePC_8Ryj5RAsglc6hwK1wQbBeE47cHJHM604rfRiEP-UsqDdyr2OntemhYxpai9w_xH8zyJ05bzdcyuUeir2pJPdVTC2gdYjxFfqN6GJyIff4WetWDzqf8nUinDvwq3t94yeBcPcOslvaMp1lEsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7493" target="_blank">📅 12:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7492">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=EsdSxO6KEEw4cildeCsuqjxi5MddLqC8zqIRP4UBQc0zDl0DMvkTosQ02hHuLL8eM0z59z2l-xQzOzdgG2E9UbQjbAkSUuX4c_5_4TGSiK32W3UqU8LsbYpxr3V07kG_v9FhidS2T9yzUK-bt4pva3gsLCWiJHkWq0imtErByqNDyjMEqOdDaHWyYKRONQuWPkGY-WHNhrBiae6UOrpOC7Nbg6SAERd8_ngbt0cIDQMPGbHVNGm7dqV64Z9OMlj2YHrBq98fOokFof4qN7sNjGBmhORcym_dQfaj-RqLOuoo9uT5chvQ1dS2hFhHTPUU7Np6Dh7HU2V4K5zawZAdYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=EsdSxO6KEEw4cildeCsuqjxi5MddLqC8zqIRP4UBQc0zDl0DMvkTosQ02hHuLL8eM0z59z2l-xQzOzdgG2E9UbQjbAkSUuX4c_5_4TGSiK32W3UqU8LsbYpxr3V07kG_v9FhidS2T9yzUK-bt4pva3gsLCWiJHkWq0imtErByqNDyjMEqOdDaHWyYKRONQuWPkGY-WHNhrBiae6UOrpOC7Nbg6SAERd8_ngbt0cIDQMPGbHVNGm7dqV64Z9OMlj2YHrBq98fOokFof4qN7sNjGBmhORcym_dQfaj-RqLOuoo9uT5chvQ1dS2hFhHTPUU7Np6Dh7HU2V4K5zawZAdYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7492" target="_blank">📅 12:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7491">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/by--KKYzrMtxcq0IlvJhcpTaYy8LvBVs9SuRniJoJ-o_R-OaNngOIre09XxsvbOl9N3lguvkU7FX7J96X90j7kVTlb4Z8z7Rvl0eMsh31yT8h2ZiuthNOQmp-AcluENvSelhbU4qS7j_kZdln2Dzw9cU4DGP2JDvtFYWCIYaza5hZKd77oLcL2pZY-nciYI0tpmgRgulC75jeMRgcDb4nu6LNYmqnrYaBhrFU-Y4-SW3DaXZrC57mxCljHgHbL1WyhG4WSNRrV-IgxbtSaYWrMlc3RNZaoDp8vbsNvrFuz6ypERnMAyjCI5xCYJt0XXnWJcDkgm3Bph-P0nwKE6bmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7491" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7490">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7490" target="_blank">📅 21:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7488">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWPJlIF91FA2lZ-HAeQGOORe5I1c4IJZQMEZhFxGSKVA9TGdZlcqZJF6cVSiDUf0on1NggCx7waVZddvFXlj3c99ECUy_s_gnOSo-_sweerbsXDsRqiF2OLm9LHIh-SJ9qLcmUGx95vKznhy_Jhapnuq8jv_eIVpMPfM31SxKEJLKR0aTnEk2UF1sOfD1T6ljtlNWeB4dnYpPtKVh0bUdNE-DyRrNY6XmapZyAelb13BcdYWZ9mhYhV28BylOMX8ZgV7WppyNOXlYqO57bzfwzySZpyy1wO7EqwdvjneD-bWByh764yWXv6Cp26LFYLoEeUUQ4JJlb4WlS6RPbcQ4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7488" target="_blank">📅 19:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7487">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syFVLyosItZwy3ZSbKT654girK7k_8H_ZIIa4PllAs1_UZygphgFqLUl1EdXFJgYRn_q84fGMGBZiPEaZPd2ikVI-xvkT0UrH-ijREqPZdgVRPouf7S3G3kyEXnEzm2mZXMfR1XXnIFF9EyKcOBrkHvscdkGIwktZVmGW1VuhBuOBx0DwjrpN1zAHqAqDEiE1Qgx0cF4ExRkNWnUp-OfeU6UDitIpptnIKbrnXpzyhYGIsSu2q4FvOMHUQMGEHe6jsvOY9XprfF-UhR0mgukr2PMHL_NR9vpojmvVLCm02DvPBWqGuPZHC5m_B0t1cPBqcfJwSmxi5uHeNmDmSXDig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7487" target="_blank">📅 17:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7485">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unPk1kKn6JX0pWnz8JreVqjfUQPz4g1n3rpek42rgbgRR0SUvmsCm5vSsyvv7NcICuLYa5Iek2NgDeuQBtrJRRTKZnWDrJVEZhqXSj7C8-eZ6qevoXRhhD4sI-rERtP6WZvYJ9ebRkwbNU4MJxfBwXFHhsWCsa8L3S0CkO151O1ln9_1ic_HpzvxHThXPRagxHowwTkW3GcFNTm65yX8y2tyCHe9mq7FzW1pbcCUcAMfBAD8SNotOQQuKB9EMMlL9FIndjqxbgyKhJB_02BDswPG29jjbqmje89TdGEmDVDvvRT1kiLJJecRWeqe10eg7YeYl1O5s8OPun1X74civA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7485" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7484">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3OVD_HeyzSgZbF_FGHG6CY9iYjnqQ3JOlyKLc95Ey_qkifge96QubTJoySAda8JHILeDld8G7UZwFchaZZrGji_V28Z_TWvUbneYTFbCHh9BRLpgO-wx67HE9WigbgIOzmLKaswj6b6ZUx7SfbtqtTXnZpWDtHe276D2FMeKpegX0cb4obPFrYjDAN9tQPXesh1ymlOY9u8dgHy7QDFrf_77As97SvXucS_TiIC0I7TbnzsGh6QavYpMiyqHIRB6lQEVMltaQ-waB7e0WHFWZnE3wMGWydkIru4pmjcwQ5fiCsIMVbZ4dajP_Ub08lsWBgUR_olySsLFnYqXGJ_5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/ArchiveTell/7484" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7483">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7483" target="_blank">📅 17:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7482">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kt9BEnTh5NdvZPjB3vX9hNaY_kSeXPvbrKa3s3RqMcnLclHK9QQvjq1vZJpilfQel_d9W-wjSdB5CbgT7R1zRdBKfTF08OkEV87z7ZuUIvP1IWNmsoDTHAIsGD4HnrUBp0UQim_JKIbj0zO8gFtnu5lRcLMvPf96QJVavujzI-hlciZoyFRVJJlJdlBsYmoQZzgLL-v5rRN47tOVkdzzjSlRMi85D2tnVpxWjT1Y1ivanNpEBxH6Y-JBVpDchZ00uTOLLdYh11OluLf-OiFWESL4tH0Cd3cwUuj6kvrV1qpcoHH0NetuEsKNS65uQLRAnzs-OQxA3S4Xn6sM9iTu_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/ArchiveTell/7482" target="_blank">📅 23:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7481">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLbuyeTj1gMkk9CZcsFZYk5WuvrqUF0jRTxmuaRGt1d3M_xZ47bJnLt18aXiVxAQTpGsLg91l1cnsDCSasxKIRhhjwAmV3l_QafC7cXnGPn4a6sKYu-hb29Foio_zddtUvEJbtJ_ZEiiy7v2RihKL9cLVDVRY-C59v7ioIzyWX1Q5cZa36P3hOBhIAbLmJdp0NaEPgJg_YdyE0aW3laAj18pUgt7LdeSgRwydcEfKLwJGtVlMXb-P3nP4RapIoU3YYKq3KgmwBjDZTHwC96L9UZu6-UHacD9A7rV60n8q47yxqe099SiuXhGU1cwV0QvjExCOMJbiN_tMngaNzzZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان: امروز از ساعت 12:30 تا 20:30 به…</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/ArchiveTell/7481" target="_blank">📅 15:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7480">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7480" target="_blank">📅 14:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7479">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZaoPyWpxdhLJu-vK5Saae3vQJPFmk5WlZ3RrOLeMZ4ew9-gSi4FRfE_UDAHLE7kBGMgdHcbHW4hHPVefCN2meWc1XBvlARuSD1cVuqnagWpc0whgjiy1SJSf91BmO66d7FjgkwsmSI0H-EbXxEsEeuoTRO1JCgmIMBcoIMS4f8jxfuT2aB4TVVVYak0kgIzTd6YyeA2bdMjfBxh7vqQxVAIOKVXNaSZLarVmfQTF_T5fQHgB0bjmZnV3J0SbFLHWZPRjj5wU7ywGLZYnKErHymWQ3khJ9uTjyv7mW8X1owI0Yh4XtyUD-SBEtyvRDvyydTLhdgvluaGWTJJns9wIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/ArchiveTell/7479" target="_blank">📅 13:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7478">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/ArchiveTell/7478" target="_blank">📅 22:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7477">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">Gemini 3.7 is out now
😍
از اینجا میتونین رایگان تست کنین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/ArchiveTell/7477" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7476">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKUcU0PHCe_xv9rhllxjfnE1G6PLy2grTXhSUveclr5095eUyUUEhgl-mrJKDxpYXy6BHKUPJ1zeDScU6mq8HcShlPeGLpkrXXYHhyaSGgUv2J-o5MZuLJRBaajb-FLZusZFGXc00t-pQGqlz514wPt7oQ84R-sjuUogJNYsD0vxtYoNLdZOtArJC-6LNciybpmuiTiT5AU0Sq2Tw1u_3Nr9LDMwHNB1rZbEVK8BnBuWyzsxqNShaEsa8WbkTix1tfawKjfh2TuGCRGyA0HVOjcXkJWC-b_5sQf1TA50Un9--UwYxQDEvc_RYtiYJRLnw2LKmAl_A7PPbZty7WqYkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/ArchiveTell/7476" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7475">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7475" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7474">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7474" target="_blank">📅 17:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7473">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sATUr0wfyD7Lgql3Q8e4-fkvLQCyFNkxFI9cCho7e3MTRlVGiEC926jK9bcAfGOxFNbp20wx8r98hTy_xwVWvHSDl1IN6wtrjpwe7FWajex05Hz-MBVlu2SQsNt0dlLN5V8iTf-_8nHJ2txlLs1HNkejjwfmUB5i_vGjOgMA8NayZNt1H9Mc2_dMGeMBZuvFVTlJrex4UVzSCPUe4f6m4gloM-KhfWp5FdcDwhna8CSRC3wqTSSRVeNbpDD0UEdt_TfXYyprTUql2Snm1ismsXyRrb8n_xvdWHm1cALNn0uRP_yqbm17BtX6OScLokgT6Ewi81zUHx2wfVXWOWKN-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/ArchiveTell/7473" target="_blank">📅 17:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7472">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCRO-xy2DEj21K2gtSN9k86b32i8jctPgNMGfWoff5XRAyPSRawxUqKrtQ7jTc1pIGZCaa8d8ptFKyhy1E5adCjIE8l-u_klpFAn8doxS2JnjJG-6G39TuQDr_xMzCaoW2TI3c8Nl3_sPKzeKU0u1wyTS6KuwjdMkkQl_6S5NRsGxd_y3K9YGlPMzS0jtMQahPlu58nLKB-desET4mXcQmQUJvvPDhc9puh9WLb4VFsAxGwmhpwZFgDI5A2tzn4D5i3vxJEGGWKMmeupnqeYPBw98O7vq9v6z8Tb7gnxlTeurZyxu1VaNQEimYmE03NcbsSwDt5scDAgzc4UAhwvOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7472" target="_blank">📅 15:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7471">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oa2gTD_kj4YYrwFp9EjVXEHJm7tV81QgiP7GzKFNzneT4sl3TMPX5nu79GMVyySO4Q4c_CE1ZiZi4pPXF5G5NVeFfB48-B-gqGhGQ7MRxQz7G0U3FkQKwKLrNJMAdXmWiqe9xowo8nswkt0HUS8p6mah1xNA2Q6vh5Q6ZLl9OyQ3W3u-i4l3XJSgEN9NOY5PJgVpSVsMLhzxq4vcBYc7jnlhr332If4vwwkW5ku8rbn9WRSc2BJ_qhFDzZoGTXskYhbBGM8aEbJkXVUlodC6n5tG9E9KO8cu8G-Um7BqF6EiwRbsDEhgo3FJcdNiuTcZU0Q8nPJAjIUJc48hYyq84w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7471" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7470">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxDLnJbsXKxkPkQBpckPc6TdTnvvhZIDnGySoeTLIuf4tVMv0dl7Dl8t5GWAu4GwkC1L5kxHAf--KVdV7uEzG6zEniRFNykbzfF9MTNDBSgZvjWg5kXX_fiukl7FtFPcrXd63zaasDgd6c7rSO42_9pTVqnMLFAMMmbVjXhv1geyRnQtn5BoguTycAt3Z7zGLC3Hbhdisg_P9lqSI4rZyZhBuceT0W-B8O-uZpxrN592R5CXraNaR2SmRCcO6kSlF3_eq3_20r5qyDkUe9FELw5awg4uOEUfphlqGPZPHL09r1dUwkb_J8k3hmnPsHt1fjzBCqpJXdpovHCzxM1tEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد  قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود ۱.۵ تریلیون پارامتر داره و قراره در آموزش SFT و RL پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:  چند هفته بعد، Grok 4.7 با حدود ۲.۱ تریلیون…</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7470" target="_blank">📅 23:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7469">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">https://t.me/ArchiveTell/7053</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7469" target="_blank">📅 17:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7467">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOG7xNlZ8n8UF1F-mbRrOdAoTAZ0kOQFh2eL0QocsFTeVzoY4FR5d4U1KxWkuhVuee3gE9d1muZWuAsrIUyLwEQUyxiNkOD9jGkm-wdLYpHkH_Sbqwi-29ytsjBdXP4x6EBiF-9VrSzVvqYAjvSDIzAEznXi-Yejo5C2kRfbcGXqVagRfqMVNWf8s2x0t3rKSSvaoY2PUWgXv2le_RF05Vf8C6sHi_c8J3TOO2LTz-iec9CG07ndhuWG_bC9F5shOF0eb4AlXbAewCV11H_qeAYths3yZ_Nz4yuGqyfdJ4Mk7Q_rhUh2CPP04EtA5K1WbU11oiSJ9vpfVO1RjRTAUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/ArchiveTell/7467" target="_blank">📅 15:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7465">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7465" target="_blank">📅 13:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7464">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAwNi2TQW4IwcB14VYRMaDhawQnK-0HhqC2vfENWfrnDetaHCpRFLBQNm03ESuq_9KC6fMioPUlXOHTRSehCAQOFMoHw879iYZlf1Aq7OGdiAHRbgSKaNvAIFtWHdAsbe8W9mNyS4Ro8poyvnpXBx2ganOR1VopA-Y-Jqs-vTn2W5QFxACwlDhmqR23nXYjNivUGaKXHe3BeIBEVBcL2R5syrsK7Dz8NDkHrKDf_Iil-1fYl0BNmZmC8jJlhAG7K2r5ZErrMkYf9Sr-PsDmTPhMqCSnukztKlra7dXxyeaphC3i_D0mywEQeKBE6orCRS4lEA0qGiNblau3Ft5v_sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7464" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7463">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7463" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7460">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVGDFjqlV48NuOqd2dAOn9AT8NnuQ9hAA3tlmXoJ5U4nv8JP6foDOxcJbcQXpNqTjJhgeqEv1EMpL0ztMwSQWbIrT8Rm-M-OUCm8Ah4Ze45piwOjwG2sgAXLkvW14oV4l4Hj1uFvBIAdZM5YbqRZFkUA5x7KFHFYUDaCAj8u-1QfVzDM5b698GSCgN-Sx5l3ldMgF-yrnpqcBlmCaPN3N8X-kzRUC6FU6KlLWtTSAmetrF43CJsMUmwvFGgpn0pqVw3pJsxCgd6WPdLLq-dSLJl7cNUP0N8QSyBhJI17EfqVqwl_0WEzV_Px4RWfE0ru8hTFLxgBbWS89NpkaaO_NA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/ArchiveTell/7460" target="_blank">📅 16:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7459">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFQ1P2AHbEZ5CVfNbYfe07CjcSQLUfW97ji5f8u12Bynh04Rxjw4UpPOb7_27AYs2fT_04Pvso2ncvTGqVwV1MZdsi1RjibZgpbpoDkD6-QTjmrJoSaNcjIEMF7JxxVQmipQ7a4-H5HS8v6jLeWAOQz2aT3FLo2O4z3gYOBL_4RvYv1aTQFDvaFY07IX7nwAX4XWBI80FI8hZCjb5HfNq2_KsfN1Y-lO7-LqyBPqaW4GYlzloDn5MFjxuve2vNAc_MAZwIhSnR-oiiemlWxmp7bNJ0ds_AeerkMdIBhWAAR08SJEwDfNnau3oQ2-fx2YufX5CP2GcjEUPQrYdLe12Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7459" target="_blank">📅 13:01 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
