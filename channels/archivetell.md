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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 20:40:41</div>
<hr>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBfj9Ot5dU7_yx6suYbWCGRIlf2xHquNcmQ4rKMVyxTpEEU-CQkFj-nF3fsrLok06LFqdHb1ADoxrc_gQ2LIRXPrXlt7b7MPU_uoF-CMPifSuvKTDmCCoaEptBcRqz4uDzp7dPxEloBsk20UL2SXtu7OrxwB9PUlzAre1Vum76iRT_wdQgn9eQTQ3sIz4dAcTIIVKaFngzrKV3iWRzxZqIQeurcjGLTeQ-sUZ5qESxIhjftB1NsbkxIFN6_aAgB48PlxmFvpJ978alO2FnL5Z4KmHxNIUt2lLu5czvBk_s1bSIar0EzsHMsb_n0lOmtWN2KIYZjp0hxoEQMxGS1PvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
ساخت تصویر با هوش مصنوعی؛ رایگان و بدون ثبت‌نام!
🔺
بدون اکانت و کارت بانکی
🔺
بدون کردیت و واترمارک
🔺
تا رزولوشن 1024×1024 و چندین نسبت تصویر
🔺
ویرایش تصویر با AI
🔺
حذف پس‌زمینه + آپ‌اسکیل 2×
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
<div class="tg-footer">👁️ 583 · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 818 · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 899 · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 990 · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqmH-9C509CHVIPz6R3f-_pYc59iHAJN5KkyYsORn7EtcpCvFllL0FlroCLxtVVr6h3TZdldG-gK80DI-CLcyFOhCeixw-AOAVMQ15rT40bV0Uw4u51tXRwxDC7acP2O6wLoEyM6E7V2QBTwdc3gESbaX-RetvAAH-dubbxUU4IuMASU8PMQNwtFzDKDbZV7oPzZ4MFyhfSJaCyAXg9WQoZtX4AVs9gaqTwecc5Y5K0v2p6UwcBPBHECmhmkVgQZ-_x3QvRpdbll42ITCxqElMtIf5VJwt8PbdHCIhp9RB_XxJ7xSRyCJGr0Cbygi_gBgOxYUsX3Zq2yqPHuCX6lXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsZBEHSN0ucZTNKcqNATVG86HCPKvtkby4YtJssT3ti6eMeOMsyIe2lkUuITMNYqrQiAjLTw3fXHOTsgb-KgZN5kEX3qiDW84TvfyfpNYzftga3wERp9-HMA9bXGgV-9AwSiiWJw6P-Aa9uODmNOqLfQ2R9IceT2WzWJ1-eOSbs-Bn4-MgsX1UJ4zsV6oyJ1k04cBGwlBQRX0-9tZBj8o5UDr77cEvtrE9UN74nfp9uRExDSy1It0zyoStXU7NTHkSYzYQIBEc1WWJ7l4ptVSJOyAX89V-cnnAvtANgc6n1NQACPnexSa7kx4PTCyaxm-T11r3BZtlUwKoowNjGAvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oroOlp_EAzpUOJoTvN5rPi0xfjq1wVtdpriRRjM2O8xtuJY0afyIP83A30PggpNK6bQlqCvDQqW-lF_ta3tDzg0mHog6fUNlo_En27PY8seF0YwfYP0gbp4XDpHh_m3XvHHWX1JW9xAalT26jw1ausXRdO-kkepXIiU0909XJ16akirR1EYib4W1nl-VtCwj_q0wBmxmn2LpQ3lVgms-4ROkGyytSksAx_8U8UXWcEdXLIf2rNbBaUrg9cV_mAzDMJe-GTDbDpY6rxl1Aukj9eQgFrFdskNcSm6Qm_0Ww9pdFX4brqIbNqWCHEnixVKfenla_uM_D4y5IQHPFMAdgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFVKzdIyQGlimil1bOKgDMBqDUh6usMJ7ohkqEeW9gC1hVdXYGLzwezzjnMYXmhJB0yrecVMZ0k7WvSN4ZvzOpMFkZNDtSFtrdRXCMg34iowJ5iANzhu_30y7Br7XB32Dysd_t7YXHEFj9iSAx_5F2GybLD9piL4C9iaL6sBpiZcZvIKKV2cF0TBZQMJ8CjeubtYqkWzbmFhKzvQSOjWpaDOxzHGZ7NZk5VpeIQoFwUi_j6sisfXFUzqlzLhluI6kkNEbbq1vlcwem5mSaVu-HhMpsUJ3nfUfba5GoEVT8is6a5MlrUlhR6JXrg5OaQVrfcsjZpHhL0QISXRGMkVYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=TfztMnbauYz379PKjfsitvT5c7mH7dFyeuZii2Wcn2oVQgl48PuIMGZyamsDt3Nm9g4r-QlbPq2uwQofGpfjdtNAkgHWNnLDBiFM6fcXNLwiK2rkMIs9ncXHDw-irQnwU2AlPSi8rNcHA2eo1LCe7AoJraj3EEmEPS6Z6vtEXqK29H4729iQecccT3JjKfCSwRZrOKJysCPad5dcVw_-KG-8k4xizUOZQ1pI38IG_hkri8Iq19nfGBIUtdJHVWJkabSHuBNbcmjMmaMSbTGnmpenZZt3eee-RZM7rMnMlOKxOQTpLXTi6MOlFFSfqIlB7e7-ManipkuWDTdai9jGDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=TfztMnbauYz379PKjfsitvT5c7mH7dFyeuZii2Wcn2oVQgl48PuIMGZyamsDt3Nm9g4r-QlbPq2uwQofGpfjdtNAkgHWNnLDBiFM6fcXNLwiK2rkMIs9ncXHDw-irQnwU2AlPSi8rNcHA2eo1LCe7AoJraj3EEmEPS6Z6vtEXqK29H4729iQecccT3JjKfCSwRZrOKJysCPad5dcVw_-KG-8k4xizUOZQ1pI38IG_hkri8Iq19nfGBIUtdJHVWJkabSHuBNbcmjMmaMSbTGnmpenZZt3eee-RZM7rMnMlOKxOQTpLXTi6MOlFFSfqIlB7e7-ManipkuWDTdai9jGDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=WHoIJpgyOw5TDF7JSHeomm2_RhGbrYjb5wPcLzrgLxymfc5r3l2rsxprhWYyDZiVr7gmzawY3f-xdi_PEHgFDNWHK78pZKUXTNXh3k05da-SnEEyZbKbFH_Ofvjau7qxte4HYh1t7qcdX9ahgkasyYmc51snU7VSVA8CxbzDQCWgpyqlno_8IHYJu1mYFK-G02PoAUa8qB30797SwlFvDML_4iCMNXQQP52sCHqUsvASEj0UPZBsX87Xqp4iyajhuec95nrqe12zGt4NVRfIk3lkEv-Q_546GXHfS2yAXx8iaD5Qp2ZZirBBYxPmXQShsT19tuIORkWWO4Wnhp8-DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=WHoIJpgyOw5TDF7JSHeomm2_RhGbrYjb5wPcLzrgLxymfc5r3l2rsxprhWYyDZiVr7gmzawY3f-xdi_PEHgFDNWHK78pZKUXTNXh3k05da-SnEEyZbKbFH_Ofvjau7qxte4HYh1t7qcdX9ahgkasyYmc51snU7VSVA8CxbzDQCWgpyqlno_8IHYJu1mYFK-G02PoAUa8qB30797SwlFvDML_4iCMNXQQP52sCHqUsvASEj0UPZBsX87Xqp4iyajhuec95nrqe12zGt4NVRfIk3lkEv-Q_546GXHfS2yAXx8iaD5Qp2ZZirBBYxPmXQShsT19tuIORkWWO4Wnhp8-DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwUg0LIIALNmlZrTK0bAwWK9QkXOyJw3KE76D-g0pPPKL7QwMi8_1KiimfosWeiXxq9wtQu-IATdG9p8DGpA6-gAqLRwHeiakC-jNTwUoHK3dYZ5-T_X6wHBw6tl83jtn5irE2_oET0QlmQ9NAEHuRYNqF_-T3h9V0-lvc37qxG7xrM63nyccB8M0F5LghT0qUTh-Wbz9cmxktAJaowrpxl2_x3N9-4rdr7JbRpuTg6hV7VP1lW7Ps6oJsjirMduERLABzpyhZqETpEi-cleILNtWvW6_7szn_uxfbPnK8JTo9RZ3iepTvUkvo-MwAUwA2ishcven4MEVdYx5pL7PQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=MxQi81Jx1yYscKuoQZ_o_nK3-o9xCOIu1hdnjNXqAN74PU7aowF7vO0M9IYFK0ofIfPOUO3sGnCohnc3hWUA1yacunVOseoYpjX2VBjOX86Z7aTimoTL_nJwpgDtLkZ46mUVLYSV7r5dzkSTwqES7CWKpDTtbOHvtIGUg5P95J-UoaA66fkm5cMnXpXSQQHmwO4jqy8jWy6AxRU9Wg8w4STFIAb1ZN-K-torHzTtoJDRR0F_fw4kaovBRsfQMTmj-YKOi-Wroy94ese48o4zXdQoZNp2y59F7DX4AAKYXiRVwy2KU8Nn-R_eb17kMCgAcJovxFx-tqaznV5bxxKG67jTE68xz0dpfhLdFg6pmj-IBrTsmszQOidhbRkYdX_GBASRSUHQpOUUEu-V1dKeK2kjD49_sxJjq7kcVnLHh5m1n4tQRCysAzdkw9uvSVT_hDXS_LnI7t3-eJEzIjPu4Zqpqzm_SmEymtI3jjud978OJfRm3FvFndFReC_L2szmxb3tFli7ZYL2q4pDaATvGWtmdGaeLvhM5d2bus00WLPi-bNuyG-Ic1Uu5mmvcGy0elhU3x-4CkLV7pMpWJUVdONqqlK_jPD6S3NZu6mNOc2Th6JbEoN5b3hsx7E_LYm74LG8ucxpqOhdSsAL7T2bxL8EqwiWLX1P01IKqWwbjvY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=MxQi81Jx1yYscKuoQZ_o_nK3-o9xCOIu1hdnjNXqAN74PU7aowF7vO0M9IYFK0ofIfPOUO3sGnCohnc3hWUA1yacunVOseoYpjX2VBjOX86Z7aTimoTL_nJwpgDtLkZ46mUVLYSV7r5dzkSTwqES7CWKpDTtbOHvtIGUg5P95J-UoaA66fkm5cMnXpXSQQHmwO4jqy8jWy6AxRU9Wg8w4STFIAb1ZN-K-torHzTtoJDRR0F_fw4kaovBRsfQMTmj-YKOi-Wroy94ese48o4zXdQoZNp2y59F7DX4AAKYXiRVwy2KU8Nn-R_eb17kMCgAcJovxFx-tqaznV5bxxKG67jTE68xz0dpfhLdFg6pmj-IBrTsmszQOidhbRkYdX_GBASRSUHQpOUUEu-V1dKeK2kjD49_sxJjq7kcVnLHh5m1n4tQRCysAzdkw9uvSVT_hDXS_LnI7t3-eJEzIjPu4Zqpqzm_SmEymtI3jjud978OJfRm3FvFndFReC_L2szmxb3tFli7ZYL2q4pDaATvGWtmdGaeLvhM5d2bus00WLPi-bNuyG-Ic1Uu5mmvcGy0elhU3x-4CkLV7pMpWJUVdONqqlK_jPD6S3NZu6mNOc2Th6JbEoN5b3hsx7E_LYm74LG8ucxpqOhdSsAL7T2bxL8EqwiWLX1P01IKqWwbjvY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OT5Z2Gqd0MtIyCIeoQZqidQNaaLvcGdYB2nhjaQrLTnG0Gk0xGrrcNcW3EKD37XPwp9Nzs_wZvJcqdmXmcH13Ct0m2jgBEXOh8-DU5WPeCcHyHcc8o3IRp7Kj_Io7IlRQDs_tNLA1Gg2BNN_dU6-LRAI_BaHAv8byD6IfKh902Sj2f-Qz96EaW-bKLIOnk2nXqWio2FeZvzORVTFtyAqLyEpKpyW8UxpFo3JD8LSYzqdeuhNUWdd-Prh7sfYcdBUEnsvoVh6CdbcMCQuydpnO97Ja8imTLIdK6pJKedikQp2zfGW8g8HrCNY-7ebXnK6LNFyvIHByaeSvabTjwSgjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxsHiGJ2zRzLkMnFenog6mlvdpo58JQqAyzhcgsIj5bBqh8LhiiLUiEVEbUEXeaYIcT578EODxtucuWDyyYrjMjH6BXc0v-c3zJ0yHiti8oT3fc5rQp5VrHMrqRgOpzhmz3oeKBgiKhW9LDtkPcaxo_S3My9UcAwxSvjR8uU95ZXvb-BeRwVf0vixoBDziWrhIXTW4Wg2-dqRzkCvwMT2Q_n3Ism_VIy2lmN5LiU1p0vbrKRId3Vt6w3cdjwW-6Rz20zRTNa4ti5wdAzWhSDb2kD1RxdoqdWp9DpAvCMtVocx_SNxyK9rX4x6fvyqRbaea1ZULBJvpb35rU6sG-IYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWg4KAKM_xDqjBXgmRGkGHrA2GpJpzFp-DOqzb99jwstGYvGftlntDL5WLNaQJxjFcCjzu5GiKFl6jej_SC38qn6dZpkzSBIwEDkSCPAqXX2gIlr052zXV0ha4nSHFdVfcwWWgRr2XpInv74vHYYvflUEZ2cvw3vk86UzSRAVZCp9nCBPuBcN_NOw0ATMv6rJ5Wx8tY4XDmOQG8L2jBzy_aQf8_1t6Lr7v67allxa_5JstgdH6oBncDOW7xHx3rCt_RoHk_TqV9EZ-Gfw2_0Jw_ct0NprkQgZCrwqTp4RJ_ZPKiQnrhxiqWmVBL9BF6BQdyTQFeR3MIu1TNrL-zjJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7537" target="_blank">📅 15:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7536">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlE3f0qlaiVMwnYSQwKbTokSKFhWwNOIcp4z0Fjxv647Kj1FO7KB4YMvSsgYmg1WZZN0xkAKuSRhXG9FANrGrBpV1dhJOlOX4iYWEyxf1L_v8VAtm69OOMsatJPZmI5-j37Qs6eQUUhLEYeyR3DOn6243W-NP1rFl6OGdOJQZohBjMTTBwErxjlvn4XuzmzqDF2Om_GytgeFDWVjar3Jpp0DRGguOF0cgQHM32ecMx2gVBYJWltpSeFc0IJw7ohdmW9l0MHm12hAMZhmY4x99E-VgSs6N9ub_5_4frWs7FsRHy-F8MpXYsOTu1U_myAOZ0_HsWwuOxyKXzck5WbzPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kClfWx_hGIWTLVgHpw55NfNx_BaMNxnwARaKIsQAvLwOmaT69adY7W7xYBL9NdF2udzdqCXPzz3S8daWQbjNszfl59Zq2W6fJnPVtqJiLqkCEFbNyI9xrgGHdDAQdmerK1J8_9WsOkUANDEunEBfN5Z-66XMp9AWLNhqNMmuhAil4d9yrlDm6ai1wm-X3Q-v6HrjTl-jlqErS0edjR54mxVhEwWRelcdCUaecVsHMI6fTzB8a1Gw_iThqSKVQ8w-8g08F7fohRWOtUZXr-bs2Q0hWRtAAYEKcyIjhwlX8MR-1xkC2AuHI8XY768ucjgFfLLieN-AeweB35JjsFfxog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4pPjzqse5sBiqFsGhlyWqaRgpsk0HJdLLgP2d7sX1kkr_WAsSMYuaTl4_9OjJJX4CWDRVy3OTFCo17lLaWp-bvVXWffaaYR3bgEo1Sx-HSy_nD07OdQOqysjw7S56A6ldEPR3fVsFVycs5Gh4O_A1aWap-yHiuTNrxrl3ryRSHcCMDdTJACTLayCm5wZxVd0CqLtWLx9DYkJ5zJorkWUOhhqUnY-dKSUyXe1ZmwO2VagDrwGC6TvOQyx1UXO5BD1h9cLV7TxWM8NqV0z3l_WSqPLK4NmCEW2wP55uDXWdUczPCI3YkGRaTInFVqxv6s7Xm2RgXp9iNZ40Ejui-HuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=GP3LBbD2PTr4p8igCIr-njLiANHivRala4S-Bdp4MctrAhBKVmKM6gfbmOqhXBz1Jn_Lptb07kRvYt7RE_u32FEDiVSYOt6PzJL8gbHSS7dCbpxZGgCOeg-_NeiWIjZKROXfHIa3_pJe3XqD5IEWvIrw3eGk5_wq6b3q7LyvJtQ38U4cEmTfYVlrQpYsUVGtvhVmCSw_gsMP3AdRyVkw1hlRnIt19LXx1DX5Nm7YWFG8UAlsi9CUZe4nyR3Kzd_I5NtJEwSSE2aMVQE1XAxZ4_xYHnK0dDYyl4lqPcezS7IjRmOM9f5H0BwU-3_j7Q6XPWazNTjk9ch6tTsZ7IPtpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=GP3LBbD2PTr4p8igCIr-njLiANHivRala4S-Bdp4MctrAhBKVmKM6gfbmOqhXBz1Jn_Lptb07kRvYt7RE_u32FEDiVSYOt6PzJL8gbHSS7dCbpxZGgCOeg-_NeiWIjZKROXfHIa3_pJe3XqD5IEWvIrw3eGk5_wq6b3q7LyvJtQ38U4cEmTfYVlrQpYsUVGtvhVmCSw_gsMP3AdRyVkw1hlRnIt19LXx1DX5Nm7YWFG8UAlsi9CUZe4nyR3Kzd_I5NtJEwSSE2aMVQE1XAxZ4_xYHnK0dDYyl4lqPcezS7IjRmOM9f5H0BwU-3_j7Q6XPWazNTjk9ch6tTsZ7IPtpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCackaeNOJYOGvWwC2hVF1vlkekKjCZqxXH7ziVvfUSdqrMl1TsJGByZxUN0acNKYIpR9RpJ2qyD8bABMYlcrJ6c5gknV-miNttk_01mws3767hm06xEtTZsdE3I4Jmcl_TWBGGsJx5p-KKdr4vvD6h10OVXWApSdj8vqqq5xXdameUe5XKBXafXH17CIluYMq0oCerIg33ALsmbWR1AV1fbsxBap4uTenq5Fk-3QImj7w7C4mD3c_S1ocJLHgVInZKtJt72yyxvy9oKehOB---5OsE2A9ae8ivTBGkMY27UtXh8lcaKTYGzmulAhLNit7xehaWO3lUJ2r2BqRvV4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XU4i0kuc6MrIajI6YwaEY5if2PltvGWaoxtEHGfAJja14L3UPHBuj-_322fmgiKJMoH6JT1or7rERfHfU7mg_EUnGK_mvi4v96VSqvHQpQ6XaokrkmZOUg6zEGJROzmJmasrIHU545Y4U1q8Zep7PTBmXFJS9ye18oezrXHF_7V9hGuzppeVQse_zQ4svjsa-Q8k2_UesoOgpal_ApgSGL5-FttREP1_Yzk9A0ozlVEeEtjBnUnJHbSDRo2xC13HUimM15lZSbsoBjuK56iY2e7MlHV6NEpHLqKqabliOdEuFvkDJ9UqkBj4L4Q5tBZpEA6oMVBFgBnb6Sk6b8XyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGv6M-CVl0XlIM9qYBntMdBFS29FFgo1KAXJ8s_h8MEMDTfZmxeC61FMfYUpMuWTKg7zivwtRytKnKfgNi5NwU8ip-ZQb28VqQpyxDUpNvV11ClDUFJj3we5n2Vwq-8OAUbDWiotXDmwbbI5IgQfDmJSM5QG-hu-2gP-j4QC2uSSAluWvMb8lUdFTiGaGkqYxNPu9ls30UC_dL2jU1okwHnFYT5sc90vhG6cmqLbpcFWMoCW4ZqJAViMNzntHRa9qxteJgOKcOinz_2kR8IUrdfOVl8_TRbXqJywO81MHdjhIW0RHKw1jornFoxCbF5KjSexiL34cw1nRPoBQ52vQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRrrfDLB6jsRaf_Si-FfYl8SXw-9j4PczWiBkkDvjVBY8m9taHygHxRxyEsthjUG_INpukSnw5mL2THy4flS-3HtF3dXVHkVe8gI3iAJ_XCY2wyGpzXET2YytzTaNnwf8hZ6HipAjz9v0zGTqvdO4XZStfLEPISbB1Lun9cGUeLd-wnTduAFr5tEM69yAhalH6lz9Sm2Nawjgq_hd9fnRUhdBFTzCZH3d2P4oGm406dio7mQmVWInwdwevNCmUhHQgqgmk5Pth-bqFERXq0VahmdPJY03WcSgQzffaTOWnHxzdfW6_a-A1kPWcltR2nmCBcKlHqRSzgrcEEFt2lUmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnKCpOifwyGeRQ8kB5CjBaaJ8MpxU9PdEIvC6QaJLbP08AzZrMMeq49uWHmIf5l_VaC54u7YRvnOKiP93veO_mc_s3g5bI_pxAGFEMA-XLGLX9U2qOvg16UK6ROC0p1J8IHHwx093quCnBuYA9f5vFVnKPoBv28AbImeQkG0BMI129sMa1ttzQH01n_pWjF4uep0QX-9sugUvLB06VlerlrmZxdGOehbPM4kbWDXsbe9vZEsPOIXM2dG7WqTbYNFMXm7MyfLgW9WJd4NCCpxZyciuAdkHSXp9YDfSKz-00c7sS22Y2mwO3QXH4kZ7dN7V3dnpZ-OoPJurTkdLKaYIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYMTnYOjzmoZixBhRgKWV2gsKA5h5406m3hspXeAxr31S8zT-Ay86WR2IUluapsbZh3hnTGyNhu5z7g0tDs6TakRyPGG3lpYeNx-M2diLdU2nIguZshBDuIb5ZdBkwEqQzGgYGZInVFzqvP2Fe8uT5wwrJehepA7KrdSNkxAc6s2m2SqLIbllT-hInNouYfYRIuQa3BgIbgwxhF6Mbu6xDdBwTEg6yVbEXYafENE7BYrAM8sBMH138HiTzE3khNKgYW2eNRvFhmrKboP0ZIl_bkwBVRUx-41z8YQ30qGBjOgsMMDf4T-lSg2kp3Pkv3YdRG3udfgr84hYJL-grq_cQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBlJ7IILet4zHIp8xSiEpUVTWnzwlHYs3kkl6n0QOGrDwT9u_AGVUUOEwzgCx8nb5271BsD2Hp85C5BlGnEA-k131YWGTgSA87Wm6NLgKGGf70gFn9TwHbFtWKZujDrhPZRG89uTTT2szdIs44w0ydb1tV_-ZuKTDMvsVE3uMieTThj5QqJEg8Iw2y49ox2fSZxRXBnGixs7FB8BbS9VBm8fjJj2i95Gwj64IpbU11Y1KLrZGrAkQGBifY4Iob0GP3r7oDq53OIyjfkTN677L7L65P5DDcY8WA7IFtl1PTuGhmcbGzUSD5s-sWYhUAZ0pk_-xo-9nkbgTAJ38yLdpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hf_35mPJi-rWL28NesPF6A5hIMK5E-vRRbdrJRORn6beM_0W5Cp3q_q6db_NuNyDR9TjVev0xN-cxwj5rUEQCWClj0YWKhRxFtXyclt_5fSDRvvcSFXl-j1aAQfeyCzHjBnVtuu7HeK5jHv__eHOPdIphiT-XLLrnoGrTmrO4_NuDSGHKxVgUtBkjRS2ODXlMqwPx1oRvFyelUN2p6eKcd1lAvKOhby11Nw0Jz3Ft59LvbiZ1JPgmKPXG9DEjUKFhBctCrKywXNPM6y04C93AXa_sAiYiqat7dsNs6fkiLNAnnE5HPciyiMrDRjqbUdJMUem6FXa7MHUMdI-VVlaow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=Hc6zh0au0fRuxADwFlwVS80yN4touFDJsRGzTSvpjKlxxKu_-lUOOvc52p3RlAw78mBFU0WNMuLRGADVmMquPeM6qTpQSza-M-9epv4-Qi1e9tnxBrGX0WBiwCJ2cMPtmzgvtrNyYeBLhL1xxS_nwU_MlvZ1XdFF1HVkw17Kz5pzat6PKnAcC34CSQhJwXlhus3B8m1yD87eqynPpLBpaO2pBRmvg3iZii2cORvVoOZg1t4U1zKWqB0vaPjTO4f-qQH09AQfvoRqZftBcch-XkvPCh7WgMxetHm5LWE49EzQdssWj_TwOsnT2u8DX2he4rR8GKMzYNHrDtIv5axeNkH5RbjmE5V0kX2T6m3o-i1i-NltHt1cHeUn8OIpg61XJg4FYgIJMtW2j2s0QR0iS8kjqFIvpvoIil1K_nVo8uPzTfwTNO_D0Y3e3y5qRML-Bz9n-gcMA_WTTRi_Nw4w8AkZYlr-Y7wNPjCTH2755Z0T_eO6ZDaXedxkZFPdLoydJ8UpMp6F7Ah514awP5QosGUeHgAeCdoDXtlNLBvRsZsn-_Fb0f4tsiUTYcOtI_JjD6rK2pCUZJGhMUs_3lYO_QLOOqrBAXnvN17W_VEOPqtzj8WsYC55QOSeMTGJTIkUZ3RDMYS1vNAAwzCDK5ip4Xrlfs3cSzmhLEV7plPn2Cs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=Hc6zh0au0fRuxADwFlwVS80yN4touFDJsRGzTSvpjKlxxKu_-lUOOvc52p3RlAw78mBFU0WNMuLRGADVmMquPeM6qTpQSza-M-9epv4-Qi1e9tnxBrGX0WBiwCJ2cMPtmzgvtrNyYeBLhL1xxS_nwU_MlvZ1XdFF1HVkw17Kz5pzat6PKnAcC34CSQhJwXlhus3B8m1yD87eqynPpLBpaO2pBRmvg3iZii2cORvVoOZg1t4U1zKWqB0vaPjTO4f-qQH09AQfvoRqZftBcch-XkvPCh7WgMxetHm5LWE49EzQdssWj_TwOsnT2u8DX2he4rR8GKMzYNHrDtIv5axeNkH5RbjmE5V0kX2T6m3o-i1i-NltHt1cHeUn8OIpg61XJg4FYgIJMtW2j2s0QR0iS8kjqFIvpvoIil1K_nVo8uPzTfwTNO_D0Y3e3y5qRML-Bz9n-gcMA_WTTRi_Nw4w8AkZYlr-Y7wNPjCTH2755Z0T_eO6ZDaXedxkZFPdLoydJ8UpMp6F7Ah514awP5QosGUeHgAeCdoDXtlNLBvRsZsn-_Fb0f4tsiUTYcOtI_JjD6rK2pCUZJGhMUs_3lYO_QLOOqrBAXnvN17W_VEOPqtzj8WsYC55QOSeMTGJTIkUZ3RDMYS1vNAAwzCDK5ip4Xrlfs3cSzmhLEV7plPn2Cs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKq2QUvJRo4FeLXw_aOir6o0Vjg6xKH39ESYY-dklM0Yo7jyeZyE8aZEK6vnQSfwd_4fR_NFnEUrO4Ud8dLeHcFx_hc4P3Uh-t6zYTAstil3VnUgD8xNM6dcOo5dqXcpEqDxwXxt9UGNLVliv5FwYPcRx_xrq4_g1fz10pHgx-_alfsBmoiBgZo-OLn-8M44jr6B33WrVjbrq4nD2CRUQ6Tp_VEr4q6uosb1nblp3m-phX0KmEqD9VLS-FZWV7_G8ea2JUrKI55sMu9mWZLvsdGpZwpBHHwzb5jR6mbTJukINr1NpXF-Ghils_lDFBtio6GYqurj03gTnXJem-8iXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVRl5FCE6XuTBvE-ZYyF7wsnO4ZLKu04HvoQQnsDgsNM5u-Ojp1TnfHlq66WWFMWUZo8C2o1n9MwUaOpv6XsabAkgBu0ljYyBr--Rl4JiZSjbE-C9ptVHPk3m9vH8_ZJ_YC-Ti5LP1kE2vDBjCujQBgJm3dl5HDmJ7Enxaa1QQ0oSMcYW3Nnk0MleK1q-gQRk-HOoRahb5eyCqEmzaf5KY_ZIULOGNQ75zwNnI1BWJhZEqm-2O75rBGKBO2Fqgyg7kdORbGlbfEiuxkjeYCWHU0EWUTC3xOqO0BqmucGgG6fAMvtsu-nFkdwu4FBCQxSpgaiBfMYzaGDF5gQYnesyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LK7_gRqme40lZ-Y_T1fs4SrK-EDy7kRmi6eH5EJ7WIVUrkJcJSbXycQUJP2jMVWKISyTgyY7qBF_ZAKz3JwxS5EYf_t0pd2qe1KD-pCB17s7jivp3jvzO5H0irk8TRJdQHT6CgqJp2Q2ofWJV0wRgHSWaejiKXlEXzRNIw85vhN3jd9puBQghpu06RNrMVOZqs13VhfCgtEXQqzrDs_CK9vxvAuMqSMzDfhzZY4GqyDe-jMB8ZnhCkfkFMoZbVYSBjWTVF4vr0PnwBeDoXX4snbo9DlGfuZnCTJyQVMKKRL6XJ6NGvdQFiCmcfakdpNuotavAfTYPFjrhf9Y0G-gsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwbVf0YUnJm7mReYd0BU6i8VM3eNg0I4PYE4u3ng4bKxl0Y8cwbQM9sI8Pqm29wys4GUq3b48xm9E1jb2ciR0GqhiqoVj9ckVmMYd4M1psegLGI9yqt-FncOr9qsSVevRqnpuCCXP1oo2GO6Ynkn1ia1GjPb0SEVU4komupoloWYqLchm1tJJFzwypxP02ihuKhHVVpG9_xJNvWMYCup1m1OQ_MqsA_s_9XxI0fkerkmy3rfFNAjyXOPgNdZT959cLn0yVGgA9d4q1rC27_64-YUR3zwkN5p9bfkotGgCgqkH7kBdqIy3e_Eb96kKKlt9UCbF51UoZv0CaSfok6kjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7502" target="_blank">📅 10:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7500">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=EXZyvI-XKuT-ejxq2H2ZGvs26B4u49kCaZabU2z_jlxGCxEDIQwLbzXSQ1RIwW5yjNzJ4fe0RxnwaXSRJVOBvsuk8zwuivx8XjzWA24bvYXSfO48iRg5sDd5O3QX3aA9poOo3R4Y_rvW7AY8kka2L-4Tpts-rpd78eFmDJk49TTF4_xaXjvV_GT3pwDiyt8bFcP5Y_DXa2yTcs-X9_DmMVuqkz9sF473HEbF_MH6VfP0LiPzCuConrl7IAD1oiALGXr7A-5FEEHbKSpRRlOIbz1WdDHh2ce1a932Bw-7MAPyjL_xckyaUqWCiEakh624WBXgdQ8HvHwi41gSoEtNtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=EXZyvI-XKuT-ejxq2H2ZGvs26B4u49kCaZabU2z_jlxGCxEDIQwLbzXSQ1RIwW5yjNzJ4fe0RxnwaXSRJVOBvsuk8zwuivx8XjzWA24bvYXSfO48iRg5sDd5O3QX3aA9poOo3R4Y_rvW7AY8kka2L-4Tpts-rpd78eFmDJk49TTF4_xaXjvV_GT3pwDiyt8bFcP5Y_DXa2yTcs-X9_DmMVuqkz9sF473HEbF_MH6VfP0LiPzCuConrl7IAD1oiALGXr7A-5FEEHbKSpRRlOIbz1WdDHh2ce1a932Bw-7MAPyjL_xckyaUqWCiEakh624WBXgdQ8HvHwi41gSoEtNtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDyIVjoVlRuqOZOG0p_eyyCIq6iNLs4Qstqz0tACnXkuyozsnc5WDo-7nhsZZPTHQh93QJXCCJKQZ_LcHocMEquPrTJX9R5XXCyQDXAoE73jq_2Eg-gmAhVGUQWIqGcDrQ-L5Iee4oChG-5UWppcF9sxQtHeJJnLTillNgDsqTbLmoM4LUb0SsTXxE5A0PuSLCY3pYKCzpZt2eFMgDg5dkKKEo_bRpmmHPcp6G121ZfN0FkthrF6ofEfzCkgL5vKgrl1RnZur1EO3G72dT05nGXBB-47HllepsUBU2oYwYqlx3i_JVpb0bjghvJOmZVh5eDAN4rqnlJmuexLifKUpQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=b_ImiD-E7QAGmCV5S5fP60cnC0osbPOtk3FFkwYkQ0faNyTi9CQJWJy6J8pj4YgSEY_NR_I8iNTs8OAxxzws_7pnyDXxQVYKapkvj0B4uxh7jn1mfAYCPQFk1_kv3U8A3GmmyXNO4WZbJ8z-0eOdsOAeeuGdo4JkhA9VQAzQ8PbNXlw2XKF_3AVX4jIzC1cre-D87htmJZ_iBSqeRt7A3Gdxw7bPAC0YZUPpYvmJMAX6b5uAd_ijBWcy83B7srSyXHa4TynxofPFfp4a-s0_9FENB3xq1QRvr1d4VyQzgfYo0FtBcXYB7wvbwxSWJP3QBeRIA6nz4dPE-1-Ex_xlxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=b_ImiD-E7QAGmCV5S5fP60cnC0osbPOtk3FFkwYkQ0faNyTi9CQJWJy6J8pj4YgSEY_NR_I8iNTs8OAxxzws_7pnyDXxQVYKapkvj0B4uxh7jn1mfAYCPQFk1_kv3U8A3GmmyXNO4WZbJ8z-0eOdsOAeeuGdo4JkhA9VQAzQ8PbNXlw2XKF_3AVX4jIzC1cre-D87htmJZ_iBSqeRt7A3Gdxw7bPAC0YZUPpYvmJMAX6b5uAd_ijBWcy83B7srSyXHa4TynxofPFfp4a-s0_9FENB3xq1QRvr1d4VyQzgfYo0FtBcXYB7wvbwxSWJP3QBeRIA6nz4dPE-1-Ex_xlxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGeqV-AGWGmjWLIuoNgvvocdGTeUYdiX3UyJ_Cf5Qb1f0OkB0qo9og2s0H2QY5Z2jKDepeYZOi7iLMItsAA5yJ5wCs6eA3eSHJ0lLxr8paLd3osJqWQlw5UuQGB7YJ9aENNkoOAmthC4aUKo-YiBShPYvYmZZMJaStx7eMI7DW5GQIe-39m92BmNNp_a8iCdduvQgAV4CV25hTbv4NVhOKUa7s3oiYpZd9j0XUxShxhqxOvZgHBLJpuzrYJxeIuGZSS8oSjS7TKEhiw9VjqQK3S8FGRxhpMkFo8Bt3vvSJyhxvhLYnM5kft_7_kObmIefXV4jJIaB5XfZnYwQ9qmyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7497" target="_blank">📅 19:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7496">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwmpngMG2p14KWRmCTPKjvhe9qo1Gp-b6_vvbpQAaGj2Dbkw0OVSq6JmfpHdB6L-FXlTHMar6tsojWKT2CicjaRmVLwGbqh9mXbAZRdQgiGbMoka1UqX1qKVJMixu3KVlD3Vo4ZToMY6ZZhr059rj1ieBunOQBc1fkKIe39ZUaSZYXU6l2vYPR0fLGM1w0AFqykNEJwRLdR--12vQS1ZIxpIohZ54-ULXQC-sgZxHIqdi96sYfqcrxFLaTm6qID1sISq9JRLDQqnq-Blbv2CxlTMFuz_EraAFnsfBVg7nanrWHzYyZm63wZI8toq29KpwR5IE4LTV4WwHlHtQZ1x5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7496" target="_blank">📅 17:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7495">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=EPrkmcN2DA-vjFNOfKk_lL75-nXmbL542Mk_GZWnG3aPG5vLwJnTAOetYGyPBdzIsfuYjmBlhD0pzo-3snOg5xWrsxZAZ5Ah68YTpM7GjmL_aoEkuDLcX7v5yeUORDGZXyrwGv4bxe-A896ytM6wZ1nNaLyqHVOQhUyRxGgZMQkQfZG-sK8UWQQ9D8KzaFjX_AWWifzt_fMhxvP6cWLAGu4sBVz-JQfrbDqc5fQSXIhPmne1jR4pH6m9DaGQ6dFgqcKcQ8r0LJ2aRtrG1aWdOGYiADj4Zezn2KN0-pMF0IH0SKEyYimuMEUFUFCmhe9vaQg1-xqvGRIEyawryDPpvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=EPrkmcN2DA-vjFNOfKk_lL75-nXmbL542Mk_GZWnG3aPG5vLwJnTAOetYGyPBdzIsfuYjmBlhD0pzo-3snOg5xWrsxZAZ5Ah68YTpM7GjmL_aoEkuDLcX7v5yeUORDGZXyrwGv4bxe-A896ytM6wZ1nNaLyqHVOQhUyRxGgZMQkQfZG-sK8UWQQ9D8KzaFjX_AWWifzt_fMhxvP6cWLAGu4sBVz-JQfrbDqc5fQSXIhPmne1jR4pH6m9DaGQ6dFgqcKcQ8r0LJ2aRtrG1aWdOGYiADj4Zezn2KN0-pMF0IH0SKEyYimuMEUFUFCmhe9vaQg1-xqvGRIEyawryDPpvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7495" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7494">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7Np6Nz3k0M-7piiyYKOXWiBvqBce3AOLK7scCqaKDfsoKk7oIKOpTbIGrQj1in9vCdnWyFVwdrdPJI_fQirm0Te3W9K0OtU_nrruTVibx_pFYcRpTEqLkvKrA9KpttsxY5i1NBESmwtK-SLh9PmKe4EjKUgRhvk_H7rAPBGk8V4BPv80gSYEGgOlRxBrHnrot6OsaNaQPC1ZjMvDTrY3V0k6zll3NzwV6z-EYrB-lkhESat6LXS1yYasfl2FlwmrKQ3tDHgg1kabJJ3WNZ2u6mQFPe57iGSHuPCVKY0EG9YJz6ZguxAEgVRQhHr-T2yneWWrzq4Z8W9hZnk3z7wGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rr4Gs_5n2WzBBA4whZXR52ue-XKuNQVfr-qfCKovbf55UGZVTGToIdnTXQ8Y9ksjYqq3oaPJYKmg07tpf7N-pmUYyXdffVfxWklhiGgPrT-IUuKdAOn2oKhdcaESQiD1JCfM2OVCZNm9h9kS6-cFNxRRfGXyxx0TrEPOHJLndwZzvxikRN6CsmfJe8EzdHCOvflS_2k3Pyzkm-1gxhA0qpdtQq28qxp7RyXi5b9OJEGoHB8n5VcoulLl1xi70k8K5Kcj8b15jSrzTm8PlMUwP-UVifB5d90nosWY1vaUIflOvhbzMtrlkAjqHdo-7Ut3b73rVpOF1Km_xYcCC3uIlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7493" target="_blank">📅 12:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7492">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=UpG5AR0nMr-SxwP9tAD8W1_yq63oSdn2pe_NNKLOrWUEo-aG7becCrv-FULBOWo48UAubkTDgNMrm3-QzcruTYHOrpiIeyVJls_QTjqrBXiuu0xvJJ4fHjJNO4wmxSHSgxHF35xSUXxHid_MBOm-o4-WIfkKJrXuZKom9hHmk0wgeIEgVd1i6yey_cKFtZuv01H53uQVmwRKrvPwTMDUWfUOu3K8gNAmrY63iDs2UVKEKr553A9v7WfrFY5WfpOgngWe8T0R9L4S2mGcf71Tha9FIL6rlHTxYiCoejISNSmfPmO7yrGKOFlBXhcqm_J5p-D_bbWLjz5003uT7FY-VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=UpG5AR0nMr-SxwP9tAD8W1_yq63oSdn2pe_NNKLOrWUEo-aG7becCrv-FULBOWo48UAubkTDgNMrm3-QzcruTYHOrpiIeyVJls_QTjqrBXiuu0xvJJ4fHjJNO4wmxSHSgxHF35xSUXxHid_MBOm-o4-WIfkKJrXuZKom9hHmk0wgeIEgVd1i6yey_cKFtZuv01H53uQVmwRKrvPwTMDUWfUOu3K8gNAmrY63iDs2UVKEKr553A9v7WfrFY5WfpOgngWe8T0R9L4S2mGcf71Tha9FIL6rlHTxYiCoejISNSmfPmO7yrGKOFlBXhcqm_J5p-D_bbWLjz5003uT7FY-VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHKedtpCjS8cYf2p6-K04cPZuuDGidsBIkNcuGNOiQ7yEaTNjIhEjzoKrjeTnrQUcQ-4l1QF0wIPPaSQPQ-2hCPlqTOzJj8D0a1KBWSEtQntpud3YkQGZyuuSgeEe-7rpDh4HB2e-uutrqEhjn3ZCyEBzje6pZhNklgb7Aqz4x3iLI3_ZyT2MxfjHb4-CKiyrU91kZ8k8G6i32JIu17GAoD4Emrk-tNBNe1VLcQfhozBmY4dRBc1FGRfxXw1eAoDDFFUVtIxSdI7T1HxlXGBj4ZZzfY6J9Ic8cHfLpLy62vNne_O1SGy6fuC2IEmtSGV-1MNq-87DS5LmqVkWdbujQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7490" target="_blank">📅 21:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7488">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRpljJJKGAlvxTBHG4hMuUxbLbWPRReghEjZ3RwmG8lbTzSGy6noqj0M27JndmexP27EGMWUUO0m8lX22Jh8nYGiDoOikX1CUVNSe33r6MU-8G-BeYNnvMmTJGk9dqLF2czC9fU6X1cu6xitFwuOwIvadGKeq0DOyFd_5h6AFd6EyZ_wwbEm90a_ljSMkmklO3ZnK5Jb8uJKIkvdypv3jC45MONOtwYFbc-m1oV9PO14k-BNxomWN3oDL3BSerczslagi2a755QH42LDKtHTJqp3leT92Mg_t2HS4-l4u5V8_Jq3A_rGf8P_N1FdYgJ4vwQsfeJUHXpSDOpKyfP2RQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWQv95WIuoVkKCnkkBmLgfEvxVEl4YNaw2XqCzp4Zimsrdp0E1ySIOOlyCvwt-vrJUf9ocz2ytwjfQ6J-DxIWHGOIVzemyTADQ3Tb2nslzjaf0iKqeDOhFbVtJlrmfB4eDGUQfIgxoDU_GtBhUlAyM1AehgGcw7JznC77IysBT0Xoa2m9KKOv-P2wGYkN1IGkua-G2PCx59Lbk_bcwgcmdY--Ay3s-yqWv-xfwGK0raseeSBHE7Q-bYj4eWTbV4Xlg06e1iNgX0rFJ5Ot_5oW7yGHyD2rO5nNogk4f1LGx_EEpWU8SDhAm3YDOzosyxYnMM9md6Fd1TtO2_OPmbSAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7487" target="_blank">📅 17:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7485">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_sC2cvAmW9sc6fXsSq9IOghvHisZ2tKMi1QnD5yMLHfJqWPQLvcspQlsoPQH9ulyktu-EgIrJXzmxfY8ixkV32PsIAo651mv3xRvLsRAEOERom8bxPSmo_mtYGMm7XSTdIaXbzLv8nRUx4mqMHkB6u3EHoJqsRAw2b3S5LqMKk0-oG7WWKfTWuciQJTH5uJiWPYFA-2sv6qDcqR1-4-S58yB7BVpEOgTfust-7oPZVVBMuJTC-z-J3fy1MHceJLSeamGpB0JaS-hJsJquF2Spp2w5oC4SFbgvPBN0d3gQhgB5UNcVqKoYeRk_nMU77qJQx4xTXJkbPZ-_BSBqRC9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jw_cfwstPnoG6ZIdChse3cVsCCW75MgE78Lex1lPojgDSG-0d2T5X7KTd4ynrL4cPk2ZSrW9RL1k7PiC36mMrOqYf9q5qIdexheL5HcSAhs9NugaS0MywdFWrgFzPMsdxisPv2nrMAigoo1iO2tfXd359MEQJfFhjGPwMdgFejU6NKmxNzuXHyhhiSLoZw8ewXp5f9a2MSWXFI7EQXuNsZ4UfKHrI32zjllKIsb5e5FW_XoOZDefJQx66wMIrbjgVRnLFa0LGnmxlPt9Z8-w6anrOlZuAPx7BzhkkGApsNvlqnNdKD2qZRXsSVEFxAFTfcRyjIUBSMbNp91QmdLHyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/ArchiveTell/7484" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HA3bJB-z_az_ctIrQn_cpnEQUmjtZ06-Zej11pzALyXFl6rG1Fb2xFALA2Pnn4Wk9-kcvBFzhT1U6FTpBz3YkQ9xGdd-O_BvnKhkSaIYC0FNCST1w5t_oOEvKHbFlPcHhevhdWm5da6mZFeMf1UhFGE9AbROuJDpiJ0Wo2BmfgNz64DJBm5wmln04YQFQDOtgDpM7PFjecICqomvxepYZd2bDsnRg9pp2JVDE67GvJZ-1EQo2q6uKWrw_TSXifGIVA2EUSkkxu_nqw_LsjWeglj2LyhlRo_OjlSnjjf99yRT8wAYIxZWXOdkq6U8iQ7y0oI8OFB61m-DBZl9wh5UYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/ArchiveTell/7482" target="_blank">📅 23:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7481">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhauTbkZ_hjia3eVPfmNlml9RmlUeXorOLmxEvXokuN5K3e36BReUvwXcvA7uIvwYlp2KvV0lb8bI6_GE0LOdJLcIaERRa7CBPBDEdCL9F0WmaGA31LIfB2JlgftgWspJJ995nP985BuJ3qwT6Oi8Qk_bR0s1t7Ohr1LqrMygf9NFdKK6aD2YPSB6pWSA5_ew6NHaSqkPNKeGiVRVZ5rG9bgWmEo-T9BpWrNaOgUZlcspKoefpQaSkfHkyta9c1vV8rIVv-9QJGOa3jtyaBPEdonSFkOj14W6CF-JwsVQaB9tmPav4SCB2oP0OZIGtSfyRGI0SA3QQAzqoVdZ3ylYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsGHSxJCsbTxWKnJJII_Dg9SGSj80fTOI3s26EC3CU25-ZvGTsals9o-wq454KFivu_MMO1mmKClLyUMvN-klMhsZ3LIM_3g3ccvLfTi7cI-h138KGbSv2HtuCyNBGdyG7PH0jbNckdj01GIQDeqEz9_ZSAiWxPeo0Pmf6MH1pDEu34mzVcz74rINDXiMbt0X6qnU686OCLp1-qOsIyyccAVfpOOpdpRfMd8-eayIimMz1yg1aOEoM3K26j3WCQTFoEfmfGPN1B4FPlhhXq2Zmhimumo5SocCYcwwiYZaPN1ZiRYOedSLoZL2dBPDnpVlrLvN43rgTYCLb-5zfko6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/ArchiveTell/7479" target="_blank">📅 13:59 · 23 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTM_sr-nDMYvELPWu1cCyR_iYDyq6K3yKLHNTNfrC5lE-cJk3guWAHWH_sHBYM-Z2JhxZFqnD72kT5_YRlCn2Fdhn3rQFDjkl6hHu5wF__35_cgIIBOHQIhvCYjO25fPHPWKgI2pLs99qj_OJ0c6_TjYNsUlOfMSt5OUFwGjMM5HsaP9cLM4GvlDTDnvwNiFgtWaT2-ZKJb1ASPps8UVFZQkeGcvuNdqTXhfoofoFtN3IsyNlM5BQz3fmAVn2lLa7b9p9SnppXUH8B4lL3Lv6n01i2oTHgi-jZIpCXu3HgbPfM50Lz8zlQVwZI3QmlTqsTDk62EfuO4dRj7lc8AOzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU5GwL3yTZY-oZ4GzFRYBgQ1E5neSYcFh2HLVAZe0uta74xA2vHDhiRgdsUsKwDBg0GU-6xGbK72PBbf32F_PXDZKtBWAbV9orxs2bFFjpKguuGXKj_JPO_3v-JSs0SwM2sY52Vbq8OoYJSF2HTJMKxSc_cAxYuWMZp10UKO4qWRw-FyveqYokoMdtpL_B5A65HKXLpxg00f2D3msRLiNaqzv7sq8UOVkFRMn9WcE0v7y1DcVKn9ZRPam_5To2pDpg9Q-EWdIlCB2Kv6EQzuYsfXkjUBbDcBvAMhaXzvKU3GbY3OPyeyiJTPGRNwX66V7yr-I768MHtH8NRaYT6HpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gh7m700k9NxauwdFY3jUN0Dogatk8QxYpu0oP1hP2umWyT17RqpIHvo44l9SW_KVrdlMi72qxo4ttIVVF7utCSLTYVEfk-Qo8_xqfSXDazFzB5K1zwn4r1EXwBY_u3kGWbUL1gGUXBwttbdAo0LyTaOQauc3448EXVwsuzHu8i5nBEp-NfpkEjUWnSSid969yZnmIbnSslbkV7_53Pj2eOUfjuLoF8BAPU0qkJA6PAINginPTfVwHl-xdHsNGHMt8mOAGBZGicmsePjxgwgQwebIRzcN5sKsyKa-icGFOYcYVoctzhMQ7Mnkajy-5_-_OAJBhOXmNKQwJdjrbWr5Tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpabIksNMei4iHMiX0xI4cBlncYgkwtlqwQdGrASAzol9OVqrL-QJphGHmbUjf0dZFP0U4YLt-u5BsUox_LTbfmLdJdpcyWKSsSWRR2NaZQkW69pkgz40n0fiWNRlV38kFQ4HtxIsfPeEJT0XxJd2YIL5A1nzDBzcOaQKnyBy7Rg9TEhozXzUWCopINr3dsw9mQ3qUijYyW_FsvDkJqRGKvsZDyZo7K11DbJq1XDD9ipA98Ouiip_q0UNjCxRJCOYDq9Yxx03TWQy_67GsUZE2XgERlFXsTIFORlqd1gjv4RtdQ3zRu1-Mg3sJXzLW6IVnGcFArsdiN6CdNleE-oBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kcwz1zvdKaK4VVUHDzoXXod4Mqp5O2JStlt_nDg8oJvKdGNx8u1ue3XQWN-O-vtbWVU0mteLCLR7JzlRiRvxFQFKCDPU54_YyrUMi_j74JVwsHbxKyp9yXFJmw5gIZ6JjYWhyUr9QX-iLMeIJkj3MCyvzS6hwy8jxY9Wr_xxGVTMtetvlqWOu-0j8750Yy2bPT7yugo_E0waTT-rGxNpJ2Q_TDbbZKDLtq6AA4scsZzNUUBNJ2Zf4ft_OW4ZU_av4WVsMKDNeJNY_osH1jZDuOGh-zgJpwfvV891j5pWrc9EQUklsdK2gWuZD9oOHuQWpka84nwJLaj2blOuDHLUig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfcD08XZSVsKPKblHS2s0MBbkGNtyWzxlAj-gcsJm2y2v28nR425SJnJs_jxDEwepwNJ7lFoubWExn9CRkDFSVqidHIO_AxjbH4Nix1TwZlyI0P2RzaJxxVM3I3hcANZisyTPIxjrDualgWk9ErtXRjh8QNvcUs37tDFX32_OPSOf6tQHsrhygyvVnY5Na0J8gyLPRN06NG_K1_yW_2EC5mDhB9ZBjcEzgcsf-KemIqc2B4bEnpeMHz_veCqewajm4IchIPOHutPPZB0-untRkb2qLJtjfLS208Wcmw5VMPxQF2rwM3zABpHLORT7pKRumQpq5yA-VFuNW1SoLYR7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7465" target="_blank">📅 13:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7464">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pENVa4vJI1Gzp_AxUBO5Km-WoC3Y3EZpofLjSoFm1P48qAvbWoegfAoMYh1b9Aj8jHNVdv0ZqRnN9NDikTrKTFeFQgbsl4DetP2nZQY_wH6Eivp7NY3UXiz-Q9VUWdh1unKhAORhYwf0M5BEhU9VhFHtIsdtSBPuZifC8b22ruHMheqI99nT3APgcm227vJ0RTFwTWyKvtQtPH7mQ5nw0ndKCBbs0FXj_LrsZ_AJr_lN_4W-RBxpBv8Vgopem7jDhaKdzCjK65czxO7ZCQe0cZsN115NsgKw3mti19ZpAT3FoCDdKmdBCW-DE4QftZsbHjOr_IRRAJHts8iNF_boQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7463" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7460">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cb-WkKOrrcldyolKy34w7jFyqUGrUrx0cnYbajD79N_fcNEGQAZvkqISDJJkaprKA4_u1gGE1EnK--8cGu4_nkSPicm3XgZ5wYJc-7rv8mLJPaoTSttA1eQVaT6ULmMN0g9VgqJEcdkTt193y6ZnKLRnZLH2nAj_XRUceZj179FrUgr2yXRt2mnId7UNL3tKG4qKkxEifdo2bjHzEKXNQKioEgMrKkzLmkF5Y8FZTSzeF7bQle0GgSzJWYMK4Ur6CiucuD-eZSiZkQ6YLedvOJixXkomMr4Volblu4i6tXZPYzA2jyR-ApOwcctWiXP1RpRbIa8NK_3FNlJ595WUbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtUMoavyS_bsvkkw8Uge__lTV9nFWv8ngUKOMC9CT5MhG_wLhUBFe1y3bfIeXErxSaEX1rAnIgvy3TmqnL_yKNrf-2jdz6o9zE9Y6Xuw7Igzq04nxUj-pRqmxF9MNgL0Q2mUq-xA0PZUIhv850uyTTOy0TRRDXAFCrvJoOOv6epc7Eze6xbSDziWwv4mt16b9WQen-2UhQscB8QITfK2aHyd2jZF6x60H2w_211hxLbvvdssfjOufwtfqvU-QvuUTU_wTXdz6zA_wBvpfFtISZOrf9S71OUJfsF1Nlipj6Qw1yU6QlgkD0hZq1P9mPK4wFQVYgvyKjjJYOQP5ykciw.jpg" alt="photo" loading="lazy"/></div>
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
