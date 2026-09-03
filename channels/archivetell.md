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
<img src="https://cdn4.telesco.pe/file/rcoA2gZhZ88SlLdbouj5XH1fC7fDbaMaYNxzR5yXbfRLjY1EoWZR0mIBZCyPsrKxLB59OselWa4VFNJy882CAzALMfFtxm79tzPpEwthq4SxpyaYkVtVjr3QSbYdZKPLYTHQz54Ysfz-V2kQldj2EuN6P74ZfcfKHkB-B6mIaXO33OtypBKfgLHJFuxTSgyyLHROfTD4G0PoE_KFciey22cEBfqX3IM3K85lGnoP0G2XHHj9hxJCkuMa6OH68pUP67FlT8KAozvbjCw6dysMMCeAASMpB5xzItu2HAt7i3f8cvZycKK_mumS0-uTULXcx4Jz5P9exP7GWnOpyiOCQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 17:11:05</div>
<hr>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRp3ubGymxqnOBDYJz_gUH1G7b0B1KGGIYR-McS-O3x-rrBumqnt6DfwvoDPxsKBWasHtiaJoiTqhy8WQWAztnEGFTaO8c4tEjxJg7Sf1n94mAkYVG8yOd34Y3_PhSF1z-hrYMdFuGrj6szDIskLmOU0rxhanSwG8AcCpGDc-KdP0GyORQZlMGBmCi-tzElcU6qo1tTc-AJPKDlUKecG-TEYxzIZOey8GqhZE3gWg4J_0C4QnSgm9TKn5E_05DVikwO9UgBUyVYHJ45HEnOLDfxouWHuH6jQz0ulpRy7gNCLtvykdVyxqF-i5wzb_ZxZ2QlALod2IMGRxMiya2r-gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه
سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت، Prisma، Supabase، و اتوماسیون‌های ClawHub (اسلک، دیسکورد، نوشن)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 642 · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL: https://syntro.up.railway.app/v1
🔺
Model ID: claude-fable-5.1
🔺
API Key: sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell | #API</div>
<div class="tg-footer">👁️ 963 · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV7ySSh1RgkoDxmzlbZR9cbMRlAhuD6_VNOmmgP7EpBn3Ogws5gDusvHjfkldpWF849DnIDx9h4lytVn5py1kaY8dxt8Pw3T6MNkgcc5D-O9JDYCrhuqeWZmEgtodIcQnkGCa_ZFgukczsxfLnTMoFZo05-80YdPitPKcDtfKxxDLjVHo9nvvOrggWp1G4z5R12sqZ-JHhiDkcF8w82o-gQRfh9_P7BgcNK51GV4gnlmWMP9nx2tAh08Gjp_oV-y3uVOGdeX3Yw7SyN-Eidx92YZT6__Nq_tfNz0RCCMhW6Hav8qPd9kJNdE67cmE0Z_WVvIIL7WiE3sPYgP4XOCww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL:
https://syntro.up.railway.app/v1
🔺
Model ID:
claude-fable-5.1
🔺
API Key:
sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">Free Deepseek 2.5 Billion Tokens
🌊
Base URL:
api.pkay.fun/v1
Endpoint:
https://api.pkay.fun/v1/chat/completions
Key: pkay_f38d9bbbfdaea88a190f415eb007ef2ffb74bed33961c366
Model: deepseek-v4-flash
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7607">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTirexNet(TirexNet SUPPORT |)</strong></div>
<div class="tg-text">«
🦖
TIREXNET SELF
اکانت تلگرامت رو همون‌طور که می‌خوای مدیریت کن.
⚡
🎮
یک پنل شیشه‌ای برای مدیریت، شخصی‌سازی و خودکارسازی اکانت تلگرام
👤
پروفایل و بیو |
⏰
ساعت و فونت
🛡
بلاک و سکوت |
🔒
امنیت و AutoSave
🟢
آنلاین و Action |
⚡
ریاکشن خودکار
🤖
منشی و پاسخ خودکار |
📢
تبچی و تایمر
📋
ابزارهای کاربردی |
🧠
هوش مصنوعی
﻿
«
✨
همه‌چی یک‌جا؛ ساده، سریع، حرفه‌ای.»
🤖
ربات:
@TIREXNET_SELF_bot
📢
کانال:
@TIREXNET
💡
پشتیبانی و ثبت پیشنهادات :
@HRMP1386
»</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7607" target="_blank">📅 22:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7606">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7606" target="_blank">📅 22:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoYtTVf4FoCSR66_1Ak5mjuzD7zy25d-pbel1-ZqesXEPsjsIFeNsghly_xZN0cPS4KU4RubSdQCxFMQFKb_qiXZYsrWDtybv02UxYgJLS6r5MlxNoYd_NYFif9S7u_K6_ZwRpNP9WibAzEwSSn90Ua_y7oL-Y_5JwW-re2u2VMsygXFUksaKGSdM7_jebXR05e7ilSxNeijEQbshr8TmmmSzT5zpR6WgL2VOVPTQwedmc_S3unyGRfxeRwSLQgwzZQPsKmrsL3A6trN-omcUIwWDZcSUmygVjeecXWS7ZLhncceyIt6Uy3m2SJU8y2Np31LwDuiiJPE5uANpsrAHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Gemini 3.8 Flash در برخی موارد از Opus 5 پیشی گرفت - با قیمت 0.75 دلار برای هر میلیون توکن
شرکت گوگل، سومین مدل Flash را در عرض شش هفته منتشر کرد. Gemini 3.8 Flash برای برنامه‌نویسی، کار با ابزارها و سیستم‌های عامل مستقل طراحی شده است.
بر اساس تست‌های گوگل، نتایج به این صورت است:
⚡️
Terminal-bench 2.1: 89.4%
در مقابل 89.1% برای Opus 5
⚡️
Finance Agent v2: 61.4%
در مقابل 58.6% برای Opus 5 و 53.8% برای GPT‑5.6 Sol
⚡️
HLE-Verified: 54.9%
در مقابل 54.4% برای Opus 5
⚡️
پردازش ویدیوهای طولانی: 87.8%
در مقابل 75.4% برای Opus 5
اما این مدل در همه زمینه‌ها از مدل‌های پیشرو پیشی نگرفته است:
⚡️
DeepSWE v1.1: 71%
در مقابل 74% برای Opus 5
⚡️
Terminal-bench 4.0: 19.1%
در مقابل 51.8%
⚡️
OSWorld 2.0: 59%
در مقابل 75.4%
به عبارت دیگر، این مدل "جایگزین Opus" نیست، بلکه یک مدل سریع و ارزان است که در برخی وظایف به مدل‌های پیشرو نزدیک شده است، اما در کارهای پیچیده و تست‌های جامع سیستم عامل، عملکرد ضعیف‌تری دارد.
قیمت این مدل تا پایان سال 2026 ثابت باقی می‌ماند: 0.75 دلار برای هر میلیون توکن ورودی و 3.75 دلار برای هر میلیون توکن خروجی. پس از آن، قیمت دو برابر خواهد شد.
همزمان، گوگل مدل Gemini 3.8 Flash Cyber را برای جستجو و رفع آسیب‌پذیری‌ها معرفی کرد. این مدل در CWE-Bench امتیاز 47.2% را کسب کرد، در حالی که مدل پیشرو امتیاز 47.8% را کسب کرده است. دسترسی عمومی به این مدل وجود ندارد: نسخه Cyber فقط به متخصصان امنیت تأیید شده از طریق برنامه Fairwind ارائه می‌شود.
در حال حاضر، این نتایج توسط خود گوگل ارائه شده است. هنوز هیچ تست مستقل از این مدل جدید انجام نشده است.
⚡️
جزئیات بیشتر:
Google
⚡️
بنچمارکش داخل سایت
https://artificialanalysis.ai/models
اومده
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYU6x0rLjfLC1MpW2NPGnrJwnt801H-tJ27WIxqcf1TruQXTMbfpkb8nwaLiqugN3KH8xGiTzjitvGBvCVnsCDFzqDLFWnIuTN-T_8c2n87S6zZgCjBlAlQfu_FmsfAnRzYEbjhuMvWrOcKI-YZLPSP7Q8iNGtuzbMcNvQtuet14QFptAv7a1RakX7EE0-WkUr9CutrIt08qnN4J9gty7H6dJVl9Ajvjt7IkRWgbYEubcTKy5v_lWBNSFfnI707o6sGR543oguBj1Z9J7M6N9e2B0Notkc_myzhPkA_2OttWT4Downdh4oMdg82NM3pYFvqzJRiIx-6Ldksxu4frcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBOif0M9BOc3xvMRCxKzas0eLr2hsNg4ZbWdDow3ayZyZk8HT4c1M4Z3t1dOPwYps3IVSDBXfY5YEq8F9l0Of6GRuzBoSl-bEU1Sq4_ri4BATrV0SOHuGgc-S4ILdzYNY1gocOZ2pzOgt6d8xKjX8AdL1dA2xmLAi80etsaP-qsdG8Wj92bda0dH__sPKpWChbcoaz4F0vgS2WrrFdPgVU5nqQ2TFjGIdzosW-VnKsK5R1uXBnW9hi6mvPQEWoOlVMI1c39l6wE_HpNCOdmFDjJGYRmVaKuaAfKlYLjfSdB85Bcx848fADXq7pwp_rrJydwBABzwpBrxnw8QebW8EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTeCOF-Zw5M9-aNpfBqJJuRaRg__pgFmI-y7M6o9qOsx4EGxb2t9B5xOETj4pqOm_PfhfJP92E_4vN7SN2S_WX4U0EeFI8rajfpdbhSg8Nt30NfCvuw1MkQ_McJtn51fUgtjdu7nanNYXkDOqkA3LdqIrogT_NTImt8mLyzYwBIzuG4CsfpyydnqTjQwvmVcvl800F6bu6CXRlFJNpXstg4ff271MJsjnILLGqjmTqeqQ_KYBFuwzuJyQBRQBidF_vM8aZDmA2pMZ7DprfithI7woy80ghBXnH70RFdgJtqMkJBtAbNyIGeqsT3aIu9pAVBP3Io7INMBBpLRYpnySw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ریپوی ArasClient پابلیک شد!
بالاخره سورس کامل کلاینت روی گیت‌هاب عمومی شد
✅
🔗
گیت‌هاب:
github.com/ArasTey/ArasClient
📥
دانلود مستقیم:
github.com/ArasTey/ArasClient/releases
فایل arm64-v8a برای اکثر گوشی‌ها
✅
فایل universal برای بقیه دستگاه‌ها
⭐️
اگه خوشتون اومد یه Star یادتون نره — برای ادامه مسیر خیلی انگیزه میده
❤️
━━━━━━━━━━━━━━━
چرا ArasClient؟
چون کار چند تا اپ رو یکجا می‌کنه:
⚡️
اسمارت کانکت
یه دکمه: همه سرورها همزمان پینگ می‌گیرن و سریع‌ترین وصل می‌شه
🔃
سورت سراسری
بعد از هر تست، سریع‌ترین کانفیگ از هر سابی بالای لیست قرار می‌گیره
🔓
فرمت اختصاصی .arasc
ک
انفیگ‌هات رو تو یه فایل رمزنگاری‌شده امن ذخیره و به اشتراک بذار
حالت Protected: طرف فقط می‌تونه وصل شه و پینگ بگیره — نه آدرس، نه URI، نه اشتراک‌گذاری مجدد
📊
اطلاعات ساب
حجم مصرفی، حجم کل و زمان باقی‌مونده ساب مستقیم از لینک ساب خونده می‌شه و بالای کانفیگ‌ها نمایش داده می‌شه
📣
اعلانات ساب
پیام‌های سازنده ساب خودکار نمایش داده می‌شه
🏳️
پرچم کشور
کنار هر کانفیگ پرچم کشور سرورش (از روی IP واقعی سرور تشخیص داده می‌شه)
📊
آمار اتصال
تایم اتصال، آپلود و دانلود لحظه‌ای + آمار کلی در تنظیمات
🛡️
همه پروتکل‌ها
VLESS • VMess • Trojan • Shadowsocks • Hysteria2 • WireGuard و…
💎
پر-اپ پروکسی، روتینگ کامل، بکاپ و رستور، تم روشن و تاریک
━━━━━━━━━━━━━━━
🔒
ویژگی‌ای که هیچ کلاینتی نداره:
کانفیگ‌هات رو با پسورد به دوستات بده — اونا فقط می‌تونن وصل شن و پینگ بگیرن. نه می‌تونن آدرس سرور رو ببینن، نه کپی کنن، نه برای کسی بفرستن. مخصوص فروشنده‌ها و ادمین‌ها
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmKfk_G-vPoZKLFDNushz4KhbspM-DhybiszR4RJdCxPByXyJF795gZ3XEmQjluz8OLdq59RU4fFZqtcNYJudXRNWOsdgMPH8E5RNWYXt_MGZRHwLLVV84XbfQXAkiezGqJCcrczdUNiynVXRWV86H7gP-p5FUIkJY1UyfEqN_RHEkwmNZ6XBdiGDTIJp4Z5Lu-VLJhAHpz3llUZM2U3P1L5xV4TT43Fxg_cTQkGT8KmaK5QI-OVKaI2dF2qyJ6o7Jj7rDQzCpF28dmaRGtKydI1EUiu_GeDzaRfYbQmUpb7t8Gvq21oMYZCxjjQ89qrjwG4XA09erHFDXd-w0GTcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧑‍🎓
✨
OpenMAIC — کلاس درس تعاملی با هوش مصنوعی
هوش مصنوعی داره تبدیل به یه دانشگاه آنلاین کامل میشه!
OpenMAIC
یه پلتفرم متن‌باز برای ساخت دوره‌های آموزشی تعاملیه — شبیه NotebookLM، ولی با کلاس درس مجازی واقعی
📚
📤
چیکار کن؟
یه موضوع، فایل PDF، اسلاید، صوت یا ویدیو آپلود کن، سیستم خودکار می‌سازه:
✍️
ساختار منطقی دوره + اسلایدهای آماده
🔤
آزمون، تمرین و سیستم تصحیح خودکار
🔬
شبیه‌سازی، مینی‌گیم و مدل‌های سه‌بعدی
👨‍🏫
معلم‌ها و همکلاسی‌های هوش مصنوعی برای بحث گروهی
🎙
سخنرانی صداگذاری‌شده + تخته‌ی هوشمند با نمودار تعاملی
📦
خروجی:
فایل
.pptx
یا
.html
قابل ویرایش
🔌
سازگار با:
ChatGPT، Claude، Gemini، DeepSeek و مدل‌های محلی (لوکال) هم پشتیبانی میشه
⭐️
۲۰.۷ هزار ستاره روی گیت‌هاب
— پروژه‌ی فعال و پرطرفدار
🔗
لینک سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvEgxWxRzDC9lJtB3gmeBm4BsweKFp0rN-qEzaTEjuR2rgoFbrxrxQgNp_n3sFSm79ifvZI-C6elJNdYBFE41B9dYOni-oACFsCWDW4zzGUkxhxQXrM9EHNzlmGPU6YkKp5lKYPyvcpwUbPEdJ0dkf0flmmQtMwyGi3UhavO4FYRS2-dpynGDBStOBfmYzGz9FivcMRweaX71q_6C73dQ2w73banGz5yUyl52xd8y2I1B2aKaBVvriXncvw9CSSuCM1H4bqZSr7MPJvjwxDJC4Im33rhenlGe6d6eCBXOLCYyKX35nTbljCL453MOFVOkwi_3Snm3xBvsXY3ydnIMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
✨
۵ ویدیوی رایگان روزانه با MiniMax H3 Max — بدون ثبت‌نام!
با این سایت میتونی این مدل ساخت ویدیو رو به صورت رایگان امتحان کنید
🔥
✨
ویژگی های کلیدی :
🔺
روزی ۵ بار تولید ویدیو، کاملاً رایگان
🔺
هر کلیپ ۵ ثانیه، کیفیت 768p
🔺
صدای طبیعی همزمان‌شده
🔺
متن و عکس به ویدیو
🔺
فریم اول و آخر بده، مدل حرکت وسطش رو بسازه
🔺
نسبت تصویر: 16:9 | 9:16 | 1:1 و...
بدون نیاز به اکانت برای ۵ تای رایگان روزانه — با لاگین هم ۵ تای دیگه اضافه می‌گیری (تا ۱۵ ثانیه‌ای)
💡
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZLDM7h6j00ok5Y1OoNwHcUCKsngx2ZqJ1lxSGSTlHkTq1ZYJm_vzBiW2OR-qs1o5KCzhXYIwex7sI_AFdEJ_2VEU57bZoUr_ksfOcgukVOa009UIkZpBilgp6ZDPNFlF-_HzAuzLWmM3MQtyVayiCRix8XeaU9y3m3vRGZ2jBB77PPeUMET8rV9e2ODqinQVXL5w14iGsWOVG0Z8eqAMsJEF-we4BB4ccTSXxjkJ13032RGrTAwxWHtN229sOnVvD-raPPf1QZrRfQjE15EjqrA8FoVSVcs9tTBneL3Y9rbM1aeCCe8Ow9sMbj_n1gPWC6WumPOYCxB1bdIVW7oUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔧
✨
دانلود کامل گفتگوهای Claude با یک کلیک!
معرفی
Discussion Downloader
— یک اکستنشن ساده و سبک برای Chrome که گفتگوهاتو با
claude.ai
به فرمت
Markdown
ذخیره می‌کنه
📝
📥
چیکار می‌کنه؟
کل گفتگو رو استخراج می‌کنه — همراه با:
👤
مشخص بودن نویسنده هر پیام
🖥
بلوک‌های کد سالم و دست‌نخورده
✍️
لیست‌ها و جدول‌ها با فرمت درست
🏷
هدر YAML با متادیتا (عنوان، لینک، مدل، تاریخ)
⚙️
چطور کار می‌کنه؟
برخلاف روش‌های معمولی، داده‌ها رو مستقیم از API داخلی
claude.ai
می‌گیره، نه از روی صفحه! چون توی گفتگوهای طولانی پیام‌های قدیمی از DOM حذف میشن و روش‌های عادی نتیجه‌ی ناقص میدن
🎯
🔒
حریم خصوصی در اولویت:
✅
فقط دسترسی
activeTab
و
scripting
✅
بدون آنالیتیکس، بدون تله‌متری
✅
هیچ داده‌ای از مرورگرت خارج نمیشه
✅
رایگان و اوپن سورس
⚠️
محدودیت‌ها:
🔺
فقط شاخه‌ی فعال گفتگو صادر میشه
🔺
آرتیفکت‌ها و بخش thinking صادر نمیشن
🔺
رابط کاربری فقط روسیه
🔺
نصب دستی (unpacked) — توی Chrome Web Store نیست
🔗
لینک مخزن در گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuihkBCA5hp-5gn2W5zs0UUCBnpQErHNRl1il7A1ckpSkjQFCNBGMNS9929m-eDw1rgBh2WPKBLQAMehfDQ3VpXw5IiU4XVtT8Q6prwlRlqqoptHmvbGylGVM4JHNaW4nJwJXa8yZeOdMYco63KkUZRWCwsWQH3y8UsIL1MULE9C_GIsbG9yHmm5BmOUtscyLw_iBxrUFigk-2BbEtBltaAJ5UyfYKkXZ-2kQ2AfX54Y6SnV-JpR-yOQQrJhc8qNuyIc11-44sV9j3Vzwa6VWgVyABS3wz4o6-eSaw2uou7rKP8IUPC-KkK56tkZBsMNR8OVoyL8Ug-bi7oi6JdXng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦆
✨
حریم خصوصیتو با هوش مصنوعی معامله نکن!
با
Duck.ai
بدون ثبت‌نام، بدون اکانت، بدون هیچ دردسری به قدرتمندترین ابزارهای هوش مصنوعی دسترسی داری
💥
🆓
💬
چت و وب‌سرچ با GPT 5.6 Luna
🎨
ساخت عکس با GPT Image 2
🔊
ویس چت با هوش مصنوعی
سؤال بپرس، جستجو کن، تحقیق کن، عکس بساز —  همه‌چیز رایگان و خصوصی، بدون اینکه ردی از هویتت جایی بمونه
🥸
🔒
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKT8O54F1ZcWnGCjIDPDMjAZ_QIV71-K2BakV8M-eFgfQz-KNDqLEm86gYbtRPX202RnXqZHiuk3o4OoOf1e4CbH6LVDoijdeQ2qbnP_iSRFguzERclGHNTe-Rui5bS664jyAPCwJyRc4l-jSIg8Op3zxQ5RWg7F8qUZW9PWC3-B-x46PQVZ-_cxK1SuJ0X4EspeXRTFimM03MybUp89PobMdEO2i1SEhVIeAHK0yQeOSe69d2_tVb-2KBG4W9eU_qnAxQEhE8KlOdno0P3F6Ip47KDDwVCpuTNdJLSsZHk4N5ypUpqm-GpE4c6PjGH9NEi9ZNe2eGdN6DXaPIxNPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Hy4 Preview: رقیب جدید GLM-5.3 و Kimi K3
شرکت تنسنت، مدل جدیدی از خانواده Hy را منتشر کرده است که قبلاً با نام Hunyuan شناخته می‌شد. این بار، برخلاف روال قبلی، مدل به صورت عمومی منتشر شده است، وزن‌های آن در دسترس قرار گرفته و به سرویس‌های محبوب اضافه شده است.
اطلاعات کلیدی:
🟢
770 میلیارد پارامتر، با 49 میلیارد پارامتر فعال به صورت همزمان
🟢
ظرفیت پردازش متن: 1 میلیون توکن
🟢
حداکثر طول پاسخ: 64 هزار توکن
تمرکز اصلی این مدل بر روی وظایف پیچیده و طولانی است: کار با کدهای بزرگ، تحلیل چندین سند، نمونه‌سازی بازی‌ها و تحقیقات علمی و غیره.
در یک آزمایش کور، شرکت تنسنت 203 وظیفه مهندسی را به 163 متخصص ارائه داد. نتایج به این صورت بود:
1. Hy4 Preview – 2.99 ( از 4 )
2. Kimi K3 – 2.94
3. GLM-5.3 – 2.92
این مدل در تست‌های منتشر شده نشان می‌دهد یکی از قوی‌ترین مدل‌های متن‌باز موجود است.
نکته جالب دیگر این است که این مدل به طور جزئی در فرآیند توسعه خود نیز نقش داشته است. این مدل نقاط ضعف در عملکرد خود را شناسایی کرده، پیشنهادهای بهینه‌سازی ارائه داده، آزمایش‌ها را انجام داده و به افزایش 31.8 درصدی سرعت پردازش کمک کرده است.
نحوه تست:
>
WorkBuddy
– به صورت رایگان در دو هفته اول پس از انتشار
>
CodeBuddy
– دوره رایگان دو هفته‌ای، با تمرکز بیشتر بر روی کد
>
OpenCode Go
– مدل به اشتراک اضافه شده است
>
Hugging Face
و
GitHub
– وزن‌های مدل برای اجرای محلی در دسترس هستند
برخی مشکلات شناخته شده وجود دارد: مدل گاهی اوقات بیش از حد طول می‌کشد و نتایج نهایی را دوباره بررسی می‌کند. به همین دلیل، این مدل در حال حاضر یک نسخه آزمایشی است و نه نسخه نهایی Hy4.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udhzGkO_WCVHjINWzEQ6SNtLX5UhXps5ipB3MOndhevZJS2HUF3rURWMp97f75I3bnZgmwhqmWaovrCkaAjy3RCWXeWvI8nKJL_K393haeILzpujJs9AVhRs8WRfToo0aoPJCS1z46Z0bM4nxVj1mM8I5SQEwRq6BZiA2c1b1bwm7q8DjtbjcNQ2Kh-Cwx5kIvY4eQt6MXI3mBKLmsVVEGghDFQA8oUbJGYpsf_wOq0VczV2PXliGaDWLiHzUweTU15ozgk2csmK1oTRj8uJsxzSKGDXZsjGT-Wk1ZFkcODczQ2C62vgKArfIFDkCDxCdLrhGowfsHPCVpYCelUuwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تبدیل PDFهای قطور فارسی به متن تمیز برای هوش مصنوعی!
نرم‌افزار ویندوزی و رایگان
PDF2MD Studio
. با این ابزار، PDFهای ۱۰۰۰ صفحه‌ای رو به متن استاندارد مارک‌داون تبدیل کنید.
فقط در ۳ قدم ساده:
1️⃣
تبدیل هوشمند:
PDF رو بکشید تو برنامه تا به عکس‌های سبک و باکیفیت تبدیل بشه.
2️⃣
استخراج متن:
عکس‌ها رو تو Google Drive آپلود و با Google Docs باز کنید (بهترین OCR رایگان فارسی).
3️⃣
تمیزکاری نهایی:
متن خامِ گوگل رو دوباره بندازید تو برنامه. نرم‌افزار تمام خطوط و نیم‌فاصله‌ها رو مرتب می‌کنه و یک فایل فوق‌العاده تمیز میده!
حالا این متن رو بدید به AI تا براتون خلاصه کنه یا تست امتحانی بسازه!
😍
🤔
پردازش امن روی سیستم شما
🤔
بدون نیاز به اشتراک پولی
🤔
اصلاح خودکار باگ‌های تایپوگرافی
دانلود رایگان از گیت‌هاب
(ستاره
⭐️
یادتون نره):
🔗
دانلود نرم‌افزار PDF2MD Studio
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0zIWjOj0k8SI4oY1kDMbw5HJ6_yGg9CTj_MXcWeQDX-tEl9aQD6X1D1mJkUXTTC5OoPWIlfKFGr7S7y_b15kK6C6Vhwj0HMzomUA-2KFj0eJQM6zIfLG_uigSv4XNCrXEewSP3aSBjiw8Ee5WZVG1vYUc03hSrVu5bcFtrYQWEUS9EZ-kA2XgMjRzbqvDrs_QLwBp0-aG7yJb7Cspjs5qRfU0YCA74Qbcd0c4czLuWHunKSJuQDaD2NIKb_fP8J1B21DzZ4ztKiPZQT1LDHmJCOe7A50qU0pcftDaAkQNreG4kbQdg33pIoo3v3uxn85PgPqs79jpnEviwOvk6l6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100
د
لار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
25 دلار
و شخص دریافت کننده
100
دلار
دریافت می‌کند!
همچنین 20 دلار پاداش روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKsRp3ImPrsqkioYjNg5GHQgw2Zcz4oznRywdgsyVblgxvFxGqaBoPIMWBUIqwFrv_kTrdVB8rue9fx6sF6jntSiuJ_hsS8rBqAJpURQdn1SS4v8643VRmhSTSfean3Y-0Mkifo922mwDMQ_AhlTtnssVegzZzAwS_WWHMhh4SPvIzDtsFUKiFHJCnRFtAWN8I0DCpB_B9DJnwAo-iTQkhQyDew3OSdDFeZ2Lwat6EYXPYFUobv0rx2_C7yW_eNpRAb0ZosdoWVKU8voSTLG4SYQxa-czzmdYi2bp_vuFc8JWuEs4_wEiMUJcQK08kfy3shmEKICIcTftj_i_1yBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت 10000 کریدیت رایگان سایت Genspark
💥
🆓
با این روش میتونید داخل این سایت برای مدل های زیر و دها مدل قدرتمند دیگر 10K کریدیت ۱ ماهه معادل ۲۵ دلار دریافت کنید
💵
😎
Opus 5 | Fable 5 | GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 | Nano banana 2 | Seedance 2.5 | GPT image 2 | Gemini 3.1 flash TTS
✅
❗️
نکات مهم :
چت متنی در این سایت نامحدود هست ، محیط وب سایت یک محیط دارای Agent هست ، همچنین می‌توانید از این سایت API بگیرید ، همچنین این سایت یک نسخه cli هم داره
برای دیدن آموزش کلیک کنید
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtt4PbDI4sKqwhnJal0chDUrl2aErxyKSa7tD7qr4MNKfFyXyIdzMLpKST7ep6ObQ3p1WzNENXero-GV7BrM4JXgnq1hFj0QQ2nnBipVXLhYk066euoIhY4APfb9Vf7hlil63BBMoPEfWVHm4fnh8wKodJgpDMe0NZcJL41WCKIyjAmVfQLlJymjoqhA_ggFUqtPcQ8GYor-NleuxqXrO_V6vsyCqICGGD-9dls49Zf6v8Z_-fTtMhVJcnidXy9ZdpDjpIOJ3bth_XUOL2M5l8VrS5Aj4mcimYp-nKDfPKmSeB4eNN9kbYFrOudQDHjV2mdNvn3WSrky91EGgoaLXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=kIolBwgdVXJ6JJfrYTOkDG2d_EonWn44X0cqHu1rlfGgpVnyTbEus8ym1te41nZgSfY5pT1mc7jHydmNiNhtpA_CuldnPRMoaq2rH9KwtHxCEN2u67spYvJy92DMo502TjVCwBxuNJxb2sY999rC4gW9oSkMsIUCGAK0JvDaz3kBOl0kPlOoHoyFr3qSll4glwPYaNV2LrGHLbRnkdI4W1-LBiUijAN2oV1KaRFK50G9jDZHv-NhrL-yQlTCvaXX44myDKyGkj0f_FJU9BqIPSYDZQreJmQbPhZ65dAQbMSDsJLsduJZ0dceio2dD40KonRPuegOxJatE6pb0XbwIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=kIolBwgdVXJ6JJfrYTOkDG2d_EonWn44X0cqHu1rlfGgpVnyTbEus8ym1te41nZgSfY5pT1mc7jHydmNiNhtpA_CuldnPRMoaq2rH9KwtHxCEN2u67spYvJy92DMo502TjVCwBxuNJxb2sY999rC4gW9oSkMsIUCGAK0JvDaz3kBOl0kPlOoHoyFr3qSll4glwPYaNV2LrGHLbRnkdI4W1-LBiUijAN2oV1KaRFK50G9jDZHv-NhrL-yQlTCvaXX44myDKyGkj0f_FJU9BqIPSYDZQreJmQbPhZ65dAQbMSDsJLsduJZ0dceio2dD40KonRPuegOxJatE6pb0XbwIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UN6lrVZ47fBidb62HEn68JvKcu7h2sNequRp_NNs47Kxb6n7PqFRILIITz9rbSalWpQSR2qa3bf-jGhF3C201HOt4jliGAi03tZjavdB7H5j9sW5pvH35L8LpFQ9yvTzNEp0YmY_sktBws4-usd2FJOhNgJQeLSWVTegLMr74FtUur1Hv5Zu64c7GEHHo5H_yZZ9PrzqrxZZg3Nop3VrrVs1_CUb0z0NLrcE4i4GGNMUinLhYmiYqi2Nz5Dl2t-vqfPahd9hQ5d_eh5m_C3X79ImrtTYBm9H93zMXNO74kdCJScDQfmvz6AJWwSR6M-hMJPVnGX2LoLMeVgEseezZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=PXv0Ulaz8VALp3SfHkXfWRdBfm8OT6h5V0229GN6oB8_YJwPDHvVOpYAMBoXO7UTg8iLXmoAJTylUamSpiMjVrx-74GpBDKHoSKwu5IbejudU-fZpkigUOyLwrT7A_m84abXmqnE3dfTgXn27mqOUJzQ4eI786B8HxymrzXFnMp7nzmo7lc729UyWvmGFuQF0PdzlNiKsgPEC8MP1l86WKURxVS1Q9jiHCXC2y-yxQA51jP_3e3WjVtUXCBqxz-YrsmZNAUBDTpZyo_1AoGTSZpr88DT5PnVfI9eZUHxY_nlamYYcp866Dcu4bNBGW8CkSkPZpS5Eo7DcR-FUIK-Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=PXv0Ulaz8VALp3SfHkXfWRdBfm8OT6h5V0229GN6oB8_YJwPDHvVOpYAMBoXO7UTg8iLXmoAJTylUamSpiMjVrx-74GpBDKHoSKwu5IbejudU-fZpkigUOyLwrT7A_m84abXmqnE3dfTgXn27mqOUJzQ4eI786B8HxymrzXFnMp7nzmo7lc729UyWvmGFuQF0PdzlNiKsgPEC8MP1l86WKURxVS1Q9jiHCXC2y-yxQA51jP_3e3WjVtUXCBqxz-YrsmZNAUBDTpZyo_1AoGTSZpr88DT5PnVfI9eZUHxY_nlamYYcp866Dcu4bNBGW8CkSkPZpS5Eo7DcR-FUIK-Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpO0TLTmYk-ZZrMUCKHbvNBxDtkPv37AFYv8iWweizdqWY-0p7i0lLy72M5ih-LEV7YMeaMsJBjtDPZhU2twYoVS1uaxWN4hSAX36kq0o4pZj_ZREoIUgDP1VF649ro-heAXK1KGYvborGF4oma6_3eSJN2r9ADO_2mBBX29zQLR42w4kU3-JIx9T9TwPFg-VKKvvfmWVVJj2oEOaJAMj9bOTXFH9jKvYTdw_tZjc8gsQUcmrVtjjsc3efheT1mCKg3c4J0sb90hHiwWwM14UbWids2VXZq-UvgBWQyGXnTZ_D4BYr4gq3L1SnGwemZyM7fpuvkzgmKLX-HsGRIkig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RedhRQabfUCEmPp7J18eFfqF6LQvnoDx8yUKOS-avDE72SRy4cRpg9qvtkAWI1Qg9_pBcOz-sQ4kw10U506LDqVnswSa1Ym2ueqBzjrddOvBoOZqU_2Z5hnbFgtBDTmdtzCyaQzNQzPPdiXKPxoh2cIq0OdEnjg-kpFjovansPjiTjBnN7bI-c4NPkYhlyT0J9tZ9AjUNOuUzj9YHk9o-K6k0d1ow9YhRJm7fFJwNlYSsAzaweRpTr2LziDyWibdnG71QMvXYxCcTDkWZTv3j2XwSo-vkoDRUrMNqQEwvP_1XU4WmfbhmYKY_MpRWgjO_TJh5CZu5j0kR9uejVE2oA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lzn47rnrOMeH9hCbSNdHM8hd9MDj6guvFlpfT4i9w-UeHtKhdSRyPJ_pTXpJud64koYHvvp_M_5imfkORXx3dNtPYnkMiv1MoshbSzGON9jzsNGN2ukpYUsHgSjMl-wISYgiR13iKObxxUtNClty13Dt6e3fAscvlHn0F-upFRJri8ElZoGqyxlSeszTxcpNFHJoh4-JuNMSJih8REv_sOwl67oTyMp2dH279UxAdGY406FmugbHLtcLinQs3HwbXRXmHHGpgmyUj7N8Z1uh3IpRLDN7C9wO_xt5ewOmQpZsE7cSiEW2dfbPQ4vG678seBLSmk5pAsGPInzR_YzSCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lk-dh_kzLQ0OhfD1asZZHNU59JWjWXCEEFyh2p3jaEJFHNG8h4abomkX-a-YhVtb5Q0cyf3kwX_raxssL0CZHr6IClqevrxZtbspn_K70is5iM8kDZ9-ZVoYqNidx6MDHGR8TX5GP8ALd9DsuQMJZSYMM29qv043l1ExFTQ6Q-1-n6G7Z_hf3yBTsuhf0BFOZ2JkO8kwsXWyLUsMy8g-auxZjxLln7tz3oPjKsWTRXhk1qru94P0HHVDpRVZxFwFELmvnf7O0XIcjITVBo7zdaIr3EgRmmPaXe0eHwyoD9VDXA9V43IyZceP4rB_6yL9mddwNpeblPIjK8KZuHtWRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXLqt_1BjJFx_S0CsVDweehZ_AC9thqKiVPnDp0HNf_-5GKsm7xh2z0GX9TSNKs4SQ75WthbveZe9TqLvKK1_P9HyYI1n7NU1dvslvGx4sqkmmSDXqRXoGLUgGrba4-4bxitL4rCjdnZE8jNxczjyLDr3_9U65hR0fcV9W37YWYDo1W2bNdOUf-jS-xpz3r2SephCAGg4RjYOzYGwoOOPD4FPQhh4GsXoltWxD6_b_qMFvLW-bD_teXwJpq2hSM8rv61Mx57yli-bsX575xWhYrSK-xzUjPrDPlMqJq80mVRiO0fftJHx1RrigR7PKa7SYmoMCDP8-XtbIbMP3KC7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohVqpD15LSEyhljvFRdk3FjREsVh0sg6iLkFDN2bwirAGYnCXyUwi0S4by7sRjjS9h_z_cqhBup4pkfC44vQUyMeqE1Ba06Eqepmjc4255hb9KO8KDK1E6tbetnoh5vqyjciw4uclEiY5fqsyex6ZSOqd7x4GvIZExgaL_ld3hNjI8bR8teqYEjrHR_lsNntrkBLIzH6CmsCUzxiUnXEqlexJO7e5rJHFLYUcvGlBe-nXgu4NtfD0BmQmVT6OYghGPrvRbl-zaEZN_OsDwaOHpQ4Iz3gF1acaqM5kuYFEVRGhuBTADJs3mxCfZXkjL3B80fsSlsdDnBhRflPhTLz4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2HL97tfBlINoh0vyicwJfQVoVn_qV_Sll1Gri0E7eL0BVMJv77cxpEFE5LIo20qP-LMVCYWLnAkh60TH1au1uRUm6xL8v_gF4_PjDrwZAEsmdmZehXRViYa-HAs_uFTb-hHXRlMi7vbMrtXm8zlSzcgKx9ABTu6kP-ixNqbjJV3rUr9zyY6C-dw2Oh2hBM4Bct57v7O3BbC7giETofgbnO19nthgriDS57SiIvG9NQclV2auSbf8W9N2XIFpsNlS2JAI6blehW8wizAEXCMBT6pkZXTclXeg51wWlNN549m4c10sArfXilQCnI-xmSU8RkYEz3SzzXXfQbtBbnzfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOiP11VCx743KJb6nB2Rpvt4MysRF3SdgNJXneC3dWqItuGCDLwEtupQEENkYTV3xfXcO-kaabLOkQZ6IqNYtiHyA5iVN1nz274C0rO13wDEaO2zAI-XzTIcMzr-e-54z_gFDtVwHBVCrHM-kPtbQOM_UN2rOCuai3oBQ1D_kneTaPbWZ8-C3KYJiNEQAqR-htr04mS0c_itNDVwCPfX3dIpatDvczj8exbbTPsYGfdIVyuko0INxspmXYkHLLmnlPk3RBR7C11LRD_mIeJ_yDzd8jdVqF2RSD3FWfoEMah9SALnSHAPtF2ZJFb_t6iguO134s4Ttf1dLcikWu-3SA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZVqpAtyUYCUI1SaWUoLnwBv-yHJktu7ejXRIQ2-aPViUTsuc3BrNMSCvoRoarmFdK4cwsg6UBfkdl8sohYLYcwmLweZKWfphOe8E8eiEenP15D9O4pT3-0VfeCpd5-RckjV_Y-6e1i76AxMlAN-Kp0r-YQi3d9iOpWPPKAOe1bA2-SvlZ-v-a1YTieO-8UAKk_-V0yVt77rYjQnbZQvdxrcq_RCZMy_4BxP4QFJbM91ddM6ubn36LKJm_A-NkQc1NzBtK22cyBDejr4Q6hQnvFo3wuP0gXpYtnw4DGHTx2PEHwaNMENKAoGDnSJwu6095adtrwSQyMubDRYDyFtLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jwx7HcBoSyq9a2ITTNwL8appaiBFVBsfG7urHsB3RsjGSVIl6dIUuj3ou2iNbNzXkU0lmL2fTLpRD6hPpkYog0wLqcPRZeXB2w1VSWwtp6DQffx4bvvz1KRagwca2Ajl00lMBGyfB5SNdLTuqQIv2jhdZQ_9nDKp8rDh-hhElmNaTwTSo5ZSfAHxZHlqiZCeob7HetRkxOWQzik_tdwjHu9shiWEz8OqeZ2gsVA4PVt7IVPnwmdcF_CcdCWYGIiCxVqL5TVy3En9MeUDfjpYXPeC-6XO4kgkjqVEAyZx_9v040ixT9uow7aFS1ALkg2vh81_2XrDM2_KWQPCOAHm2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2doZbhmUPanBwqNhsLYSA8jKHEoGKLCpvN-WgynM7uWfb2JnvaojmAdpw4ziN_80BC963-QB_2qcKYPxsIhasiCgfnEEFbL5Y_xIXG2WDxeBMpjmlY66XF10yMgLfTXc6XsYDEmUXoLpZAyZqsv_YIwMVLs-BSh4BOFSdySHn9vdDynUgdpOj5VEJ_rTnWh7iqk9hOE9yjpulOyk4OMT80px0kDStbTtDkDXSklg1ofKFTPQ2L80wvRWpYf27SHvh4CtODr3q57jujHCgLnwTbkJYyeg5pQa7yV7oERiZHryNrXb85doogTjU_4up7YxB88uA9Di2NilifcAiVMwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4qZQ52_tA0BkLaLBkuloBwXgQeyWAJ6yMLcEfoORmwK0e9PoUeCJ9lT9xqR1tQMlcTWkDiSNJ2fMt4-aCwThdmmcaA7mh6epUCZFycjETzhuDqc3BNn4SeRuvFL1FMN9DRL-oQ7oz_jzR2ftjAlnU_uAlCLkAQ80vdyaVgukjUEjYV-XY7FkMqCT7MgK4ems1AESctRDAAi5SKh8IxeELMqtqDSNM2QemZMQ7NFkVltFiOMksz92W0F3j3R-wopeWL67IGOA4Id51IPksZdZ9bgnH1SwqRq_Rtz0kdGatXt9uELdLJFMF-ggCOxD43UxHH_kch_XFmnSLBhTp0L-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNTcLp6jCO0NO7gkkJvuTUggiJb0WGKhmv_KZRlFbEMY4Jbu0bvXrjJcgyDbwZkxJhx0-K7JaaaRbQRN-UTARHKMT_5D28SffMbsnZQ3WGtqwKqg1kuZeZnh0o3GDFQWIZn8RqTVr52AO_zNutqVhqwOdFW1fX_lQbYJ3g8MzzNpB9plbaowH2F9YkIxfmNMpV8Y5NRIv4-1Yk1BERnEYX9KGS_qomLC7ERBSPFCimJJFtfO0glAuecKljIkGB_alyu8uaJbuoA-G0LR0Pj4Whw9sLSL_RnZ2hZtqq6j5uVPHcrI5Ob6SsnItZIUcKnQBluTtkmcC3YhfRSYQZYsQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=UbXASmFN3vvCtUfFPtv4nrbhqsMCCiSBjjt0VHJrxPWLtmDjO-fJNzqRYBnjVAWuuIiP2PZaKhBBc4SS334LAyQw7P9kN-ojphRV51U-KINIV5oRImcTQbfF82sebT6TEgRGOdGTu6jtNj6koiQ8HgYq7WKV6QK6TFHh1aTvFo5hTl9FOOqq-4HtmBdQ-lzhtR557kSYLP1MCkvldP3aWwPDCfuUBqqRXB1t9VSAMmrawe9TeYbTIo26mHum85xuLC7FPFNBbj6PXhitBFS54jW1G1_ORS-lmzYipFAOK12zX-YxF-I7JnwqQNu9CBXch_n2P8jU8FTJy12xhdYl8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=UbXASmFN3vvCtUfFPtv4nrbhqsMCCiSBjjt0VHJrxPWLtmDjO-fJNzqRYBnjVAWuuIiP2PZaKhBBc4SS334LAyQw7P9kN-ojphRV51U-KINIV5oRImcTQbfF82sebT6TEgRGOdGTu6jtNj6koiQ8HgYq7WKV6QK6TFHh1aTvFo5hTl9FOOqq-4HtmBdQ-lzhtR557kSYLP1MCkvldP3aWwPDCfuUBqqRXB1t9VSAMmrawe9TeYbTIo26mHum85xuLC7FPFNBbj6PXhitBFS54jW1G1_ORS-lmzYipFAOK12zX-YxF-I7JnwqQNu9CBXch_n2P8jU8FTJy12xhdYl8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=PEQrH9ckMZxqA9FaUTNaYRzER_fymyk86hWldedvocjR9QgEqfaaJclvxLSQJvybdEXz_BvqYVKR1dPG56MVvjFNSDFSSb01GV33bcMb-LpZQ0cQH4YKF0uPTyUaFn5NddrpTDDyN3BS7qDIPeSNTTdB9c5dHs5_f024r0VMAjdINN0Q0_BhFA8-_Q_rM9dE8EAr7umasDflpdRG-2xZsC1FCkBYcalA7VgmBeYLPiiLHxhIvsPMrQJSIbJEwt7UnaR1_VxhCTwpgzB6BIR2VpdljU1vWXIQh4XF1kYg1lJcwQBSXS-RXc9HoJDOrzqIhuNH1yXYzW3GluU1wKX9jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=PEQrH9ckMZxqA9FaUTNaYRzER_fymyk86hWldedvocjR9QgEqfaaJclvxLSQJvybdEXz_BvqYVKR1dPG56MVvjFNSDFSSb01GV33bcMb-LpZQ0cQH4YKF0uPTyUaFn5NddrpTDDyN3BS7qDIPeSNTTdB9c5dHs5_f024r0VMAjdINN0Q0_BhFA8-_Q_rM9dE8EAr7umasDflpdRG-2xZsC1FCkBYcalA7VgmBeYLPiiLHxhIvsPMrQJSIbJEwt7UnaR1_VxhCTwpgzB6BIR2VpdljU1vWXIQh4XF1kYg1lJcwQBSXS-RXc9HoJDOrzqIhuNH1yXYzW3GluU1wKX9jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlVtaQVe_wlFhltFoJSeloOmQiAFqMJ1SwejvdI1ug8h4jyQslXJRkMEHJ-GcGeyOgFxevKYW8aMyUybdVaDNR-74iV0Jf_PawWDsy1pkUeOlVaauxb7NXdyeK4ujgiZEThjsZss5_z0fcjZKmba6u6m_l1wVbGGyGQyFAe2-pMcBOdZ2oBvHfGO_RF43PRDcwuuiP6zfulP2Ua2TxetNx3R7-m8_XQUD-hgofKsSXJFu4hjDwgUMojNmtCyj7sXe0ae5jC4jSSmsIAS2n179TPc0pd0GLqCxuMpo6P8fk4RYavWo-mcLi6Hd_xqjaN-YcG4oZRa8uRKntrClrSc-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nv4KaiV8sp4zx7_grO7bo_R7CIrbRp-mU-x-lLg8RCROthL-QCCKGOWECDxCjk7g7VOm75VP3nnfgUDZuS65KZ6L0IdO6LZIgutca-aNkffuC5El9biC-DiocVukmXwxOzvG3uFml4t022vzkylB767e2fp-U51g_v7z7FVVIMcAi1LulNMmJZ7PN7L3OYsctqRPOGnVQZ5G-Gpv_SH3ASSvycE-PcXYtzK1SYUIFUtTZ9Hfm5CqgZNAowpE4y40CXmnHnwiY217LcmwZuInzy228pLWsqWWxZatfZInqtKOk4QlXvClDBMdnH43kLrYfR7s4ariOttnLZzyPTYyWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNoaGPARHmwS5smpaz29ZGC0y0yf2tFQ6sfAJNJlAeIaLymPGUhPmldfO6KD34Bxfu7m1ugDdjEmXEVy4MjHeb0show7Vxh2atBZVEhWbPPkfCadc04iLkFfCfoPYD3Lj2x27nyOqBPA-jJW_TGao9x1Miuwhu8oIU2U8wVWwO9lwCCOrBiNgcvPnY5kLoDtc5IGNe5ivjvNp_r28G4gSnP8slbYFbWAtKJ0C3ZbMexfCIMBReZIBwLizv0lNJ2HEtmEeW1O1TZwQ5Nki28PlHw8x1Wy_fxn6Fn-TxMfhS08D-j49Yiv0ZDCXUb7BfBH1MXPQGhDE6dIE7WUjvm5yQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=MwKOvb7-Oa18HYGS3dnCPG924J8PXU4gXtM8UkSRqxGnkCqr8aed5E7gPjrK55LCslHdM5kmgIvIwmmX4jSOoUlpWNS818vTDW7UjdJpv_qHjXmabxbSaRZ9656n_cc1nVHpqrpXKHXVsvr0sg1NbpLtru6MYy_f3MMIZGvtGHyQwFfmh5cP-QOQ4C-Mvh20N9jEoiz9jRZn_Yio5ieLJ9PClqPT1sRqtImlk5Bu3fmBx1LsoMaPS7K1WF-VXiZbmo8_fvc-p_zFpihgDz4bgTWo2tMyseIlxpCM7gj75uWmjF3x1GIoSiPciC268R8IfbLDh7OuPCo6OFZquL6J8iOmL0avvMgPn_VHxIx7UpW8D9W2EfGrIjNbSxA3cctPejaqd0aCPJaVNoU2wI_u5p7CD-O4N2eMR0jiWm-DVDy5kTDDs_yePh7Ze-Z_M4LYsUE3S8iPVZh_ybuKAd__59CpqAzIfd04FEHWJjjSVWv_7YsKuooiG9mjk4YgA0qzFh5T2tGXGhad9mq6itNyUhcXjL2npeD8R4lSW8eB02jwWP8yHLqgS7tBQXromGjKF3poiQSt2ehFm60xNilR2QYMl9s2ZuKD1p-CUHVNIWu_xZ2hU8WkxwXfwrhMmfWm5sSlsAUrPEicChiKoP4CFImHkLuhulVavQvHioLH1sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=MwKOvb7-Oa18HYGS3dnCPG924J8PXU4gXtM8UkSRqxGnkCqr8aed5E7gPjrK55LCslHdM5kmgIvIwmmX4jSOoUlpWNS818vTDW7UjdJpv_qHjXmabxbSaRZ9656n_cc1nVHpqrpXKHXVsvr0sg1NbpLtru6MYy_f3MMIZGvtGHyQwFfmh5cP-QOQ4C-Mvh20N9jEoiz9jRZn_Yio5ieLJ9PClqPT1sRqtImlk5Bu3fmBx1LsoMaPS7K1WF-VXiZbmo8_fvc-p_zFpihgDz4bgTWo2tMyseIlxpCM7gj75uWmjF3x1GIoSiPciC268R8IfbLDh7OuPCo6OFZquL6J8iOmL0avvMgPn_VHxIx7UpW8D9W2EfGrIjNbSxA3cctPejaqd0aCPJaVNoU2wI_u5p7CD-O4N2eMR0jiWm-DVDy5kTDDs_yePh7Ze-Z_M4LYsUE3S8iPVZh_ybuKAd__59CpqAzIfd04FEHWJjjSVWv_7YsKuooiG9mjk4YgA0qzFh5T2tGXGhad9mq6itNyUhcXjL2npeD8R4lSW8eB02jwWP8yHLqgS7tBQXromGjKF3poiQSt2ehFm60xNilR2QYMl9s2ZuKD1p-CUHVNIWu_xZ2hU8WkxwXfwrhMmfWm5sSlsAUrPEicChiKoP4CFImHkLuhulVavQvHioLH1sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVkJueq2N8o5B87O_tikO9JxgqsB5OB84wyDewG8FgB7RzfMgnIGOXZqlE6z8_bCC1ezlKT7WHI9MTwQ7D3U6KRcURbX_jMpZjuQt7g-gJ0Y5JyyecGN6Md9bhc9--NjAb38UinMC8Vwj4vs6u_uzNayZPBtds9QLfqrpHg5WT5QXnqcnRAboReLruKTBuiITbHHQcgotI4sgVWGMnW_7rm3fIuO9v2AOltarpzkAmY7eGFlMMaI6OUOLOJK6sBhfKc2XSqYpBKCuLR_pafnNXjC7DwzQdn2bWFMpKNlRva2GCuFDIYUcR5OQljUMN28QD3PUa94TxCjwwcd1sBEqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fL0Yj1M9EbiqLRmhM7p0Q-xjVGrj-UDKdPY0qMeLiiXODG0A2GWbezvD4DEIc0J7Z8xvS0DxDp-uI9tMEeBor9JNT1zg1F1c1pbNDbMSfXLp-braGQtha0nQFqlZW4E8pZ-vU97ga094k4tZdiMGWcoK_Qre-dI-Hcho1fNCckxUtPRWqKqErOjHGSRNZ7S0x_qUEL9pqpxKhdCwkJ7wAK7TbbAGoJwuhi5_TpLyE7cOSszUdsyztgTl73iJcwPW9Jpc-Q5H5Fsr1OL7U-NCxX0VvF9ePG0NV0FgVXFo9hBNqeIGZerFKewLchb3Rx5kXkdjyFxgrzfstaid3NrZvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZw9z-q4KwukodtsJhE4CbfPYgRmhxKH_pthQ_6JM3iemiWed3p50LI2iGayC8hUkBFZJU9TKSbNAPta2VjBd7WPnaxJePaTvmBBtxJzi_JNscm5XO3F0vnrdpSJHLiUPW0MGR47NI80z0IdtI6iFXWBNr_-l9-wPaFHXfwsy9K-GW0d3j-i4ZhAu9GuJzzpNOjYCBMQLLTuCM28P6xW67XlFRvkM3Lft1WGpPy0obMglczDzR8HVJ7XLuGTpoDvkGY1Z8neK8gZG9BeykrIGlCtmM8PvO1DfRIN82bWTB-63kriwAtQ2H-V-tFlMLetf0I_mMP7sjkXKtW1JPQXSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7537" target="_blank">📅 15:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7536">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdO0CdL-UDS_kSj_DkVt_toCh1JzZkiw3NeDjKDJhId4ZS1suWEa9pfEMTKlPV7bRglS0lIbNhHTNPlE5TpuhMloQ5WIoNv4SicCmydibIzTtV-RvI-1fI8p9Qt9hRuaZpQLSMwnJAHDCyoeizqT3VcU4UucIfLfi_xHs4dxGr-PK-kt-SsGNBu3Ne6QHNLJO_-FLnV7t_AfzjJkH117XXofBgU1VUWmDo3sQsYa3s3PQl3GowxQvMT9ESdtzYLQqycp-RourgFkEjs7sRkQMpNtV27vfIN8bgLr3WEgfs5d3uGMbjBuw-Q1ZKLKAc5h4osvQgUWsOt3oHbu_4l8lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdIHcJx_L8a4V0iz6k0V24H1lpYoONvhXhIO-6Mmqu8Rjyq9ExlCEYr7aLBn2KSub34qjcQsxx0sBjT5ILPvaDNRzmnyBjPDW4CeWItZsRFPRTlmLtYCUg_lwGZGTMEk9Z9vAUM4aWBr7-omeV3SdUSuKP3fziPxyG98jWQptOlr4JFGTEgUZYwFwld4BZWbL12V6ENaKB14qBWH0H_ukq1jFfsCA63-rWn4Y4C0NxTbND-hxOEWni1oFTzrwRcMvLd3-1fRfW69-7jXSVBc8YJnfxjxvlpTgLVGcgyyZAC678bp36D3UNVQKMFc8KKbitL107EUmK13Mu8aG0_oeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7534">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYlP8aa0Zl3h-6cJXaw3mJmdkF7pke8IZ2f7ua_jbkdm9nXtz67cZDrSmIxpO8R1Gj3Pm4nSD05zDoHlULXpS6so_jWej5X-t3URxubZcusu3OXY7U4SuK6fw68fDdtPpOAwH1eTZ-IAdxIpu81gKfAhArVn1Z3q4I7cp_tb59Ed-AdzSHrHAKTDUyO4pNFZloBrFOwpZKIGt4Su0cxNrmxARu-DvQWTZ157fT7OUaBMcTu2o3ZqbhBWQHKypJ7W5yet1f9TsRotuJqCkleLDXXQ5LRBhLEpVG2uAJeFy6LUKP3aVz7At6CO99XOolEQ-f9SUp_j4m5qR4fzH9R8nA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=GLXdj5YPjcJxqBKXFatBd0pAFno1LgrfNrJf5SSWW1kgUr431IN2olsBnDsUCDgTGreU_tYqNXMxRjHavOkOWbObOQtFA0Iz2g4z3hYmZCb6u5T7u-0oQFvyN3kioj1j4SbeWFGu6wkgzkCvtEXBGc1HQN0nXTkxAekxfcHGLD6yuxtvh_0VxQXCIKfH4XnJ1fwkQLhkyCtWu5F8rIV48vbj5EQMQmdtfmmh7kbkMZdBc8N8jnn9Je-Ai3tC1qwi0EQ_Pj0rHl8nnqNwAAN_9uCu0mAccYmw6Kkn8z0wQv2TxE6qjCIUXYjIYIkgKRLmb3MDsBjRHuNU24NtXSD9pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=GLXdj5YPjcJxqBKXFatBd0pAFno1LgrfNrJf5SSWW1kgUr431IN2olsBnDsUCDgTGreU_tYqNXMxRjHavOkOWbObOQtFA0Iz2g4z3hYmZCb6u5T7u-0oQFvyN3kioj1j4SbeWFGu6wkgzkCvtEXBGc1HQN0nXTkxAekxfcHGLD6yuxtvh_0VxQXCIKfH4XnJ1fwkQLhkyCtWu5F8rIV48vbj5EQMQmdtfmmh7kbkMZdBc8N8jnn9Je-Ai3tC1qwi0EQ_Pj0rHl8nnqNwAAN_9uCu0mAccYmw6Kkn8z0wQv2TxE6qjCIUXYjIYIkgKRLmb3MDsBjRHuNU24NtXSD9pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRUU3BySlYK7L9rcPY8A19F3UMyQvSJl7Xs9Bj0ayGubmIdF4DUxZCDhZMl6p_98P1hhpqZjf_A8ii2g9Qit-hbKyphAt1brpEx_BONX7czkedaP5OnOH5RKNl-KnsrQrsYEIPGH-VTGwgklEYL5TZG-vVctL_auA9SFZEnhRjjOnRtwNFfWi3oZOyy8SIXEdIAXIJj2R-n7tbtmvgbNSIhuWAfoThdKb3AAizQdwJ89iwD2SBt4NxlUU30qV3A4EbqMi5g9igPO4lt4SWYG97X0WSsecKVJykQpeV0X7NmFe4eDqZ-MaosTNjFoZ-l0EK3EC_aUElq8ePo2LWdniA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdExpO7eUm-LMRpnMhim2YyyUrbxcgsr85E8TFt-Te2fofpGXbPQATvlnJbjQbgta1OOuWIQrhchA_4ux4xMrcs_XjMSH440YplS_7itqBqOraRd8NrMjQmJJ4Te_q3vx9kPg3ZtABLNH9v-LQiJKKD9QDt3FtrIAeuy-bzGtoIo3ZITsmdKHWKi7wnbdTUn-BdnhoyaX0XgXqzja7HFth-_O42JHlqnnI1-txlrh6h0jlIcKf5DZlFFQEVCtvWIbfpGzbl9gZ_Yc39rpWiSL42eSQA5xe8mT73COX75Rgxae3ZZOLuPD7Zbj_e2C5ugKRAnx542eSTCeTph0CvROQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzFqhSzHnrSZYwz9dfXFxHmwZlKHvTlAksOQ-DJ7eVkjqlJB8p0p3wOb4_dYfc679PEJpjP2CMDl3n6gecDcr6v2prETWhGhPR0hZdTe5fLNPR95CVbstLNTaoR683s42zJSu01DH_f0u8pr6l-lchXrA7yeP-1eODdhuPM3M9iMED0g029WtYga5YKIpTrUApKBP4lkQDRZBxSLOvz_Nc4g6GGcVELVeYS2m985ApmQTcdRLyNQORNdUNT4lZacizKCdRzqyDLIKw5x967gFMF-EsYrdurPyDeoRKpeNTsVMxkk6cLz061vBgJyVEMbLpjs_f-lgMftoYIHy_1-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTjOIu_h75eepR976lO6G-aKkmH8ElYodxl3nBqD03PloqxDcxDbeGbFImSfhAtsx6lA-Wf9IPjxAprxFJic8i4DTFe8sccsV5rE78swLyBtmRkCfgQbFp5gMZx7I90I4jYc2bPYEY6ilxdgUq1UolPafAlVJw8bnNl1kc9qDt8VCSrdZdCMRnA6VDaZ8WJt7xm_DkRehIDtkG1VHtzu5UFN1LJVavAZ6G1vATScTbcawCDHwa61vcoh26eQT5_pawfUdokGqz5uW65xMl0fIpS4mrDx3h4qw9DAvjIwaO8ijZ7N2exYBXEzyHPI7jQU51Rs4Nb5O68EcwuPylX3xQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7525" target="_blank">📅 20:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7524">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHFuPJl6DYOjYj24rYJ-oe4skuPLPp13j2CUeiKOmU1T4Vp64eQYsqIz5Hc3E3yfc_lta1nNRfRa4Qfims3L6J_MlCChSkPjs2TBDjMvvk7WZKV1ZYA9wJMDmXf2GPz72irUluY5X2D4_0lRPc5-OyJiEYKdxDa-pF4Ou0dGgPmFxZsFpY28LyRRTPWDJW-sEZ6_3PE-IBqN9StwqPjRCUEXWlTXt0MtShpVB54cYIXA4qzbAtVokMOR4Fi8397qFg5UNGIUKWX5fpZJta-dh3CddZx8fdfR-Lg-I3McYmJdZYkdp_zUFufjZ19mAWK_Fazga007wUM64vSw3E6mAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7522">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8hAzkrqyJLUNVgVBlDEl1HGymRFMxmq2q4UHJdaNKnSsINz0lMB9n_Vh-zKgW-QazPvCM2xrIjmTn5OVm9ilhbX4UVubwHmFYD6a1KCsuJ2UW_SXXBuRvgoKc3uBSNyoRbZWQk9mxRieEnkV6tMx5L5REOImKa8Xkl95ASjUC-4m_TxurhMKhtM-mNf3vyER31Eir6i1NAk6z0CkBnX0TO63pUKWaWSK_0-bVDok1briy0XMt9c4CvhCqAPPR3WdiR2_TDBXUqvfj2L9BmWEC7KQGw2aYoJhAZJzSeiSNcY3hzMPTPLsP62fUtWMPGoZAjolC3RhTMfE-XXxJTKBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAy5u7rn4-H1D3vN_SfSadLoLSRJwVrucan4gZ8_QTlfV5WZTD2E1_MvGpwIrJrFu_hvYDe5Ku1gBFIirOm-rt26rxSSwPcWvHi4C9xuiSdnUaPH71ibhukRaDqKTPVDm1mzSU82PePTmxvC4TduGEgOouUgN2C5DLBydioRRKZ3G6MNhGGhP5G3Yd9vy2bHA1o2GF9aoWJ2y61jdWSSGuS2LT6-X8VgxuknQnL6GBOdunannUxgWlnuJrc8QSFKOOKIOQkOCzhZW3AY_ybjyQ0WE8WL3W1BdG_eQeUo5zpE51NS9-m6IYafQIjujKLlwf7KOjEDee8Ok0Pbr7KtIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7517" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7514">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1LdWl-sSKsT77sUz4x8sUBQ6sgpAJRrVtTSx63J0Kj3C4oy6fSVDD90jN3ZF60XjRgq5JPcJHD5qiwDyGs46jMRxVBrgxuNWAuRSSHw7nAab5S5ogtd0iuikMgd-u4aVq42_uNVFpGXhJQASbMAbGL6gIz1e4S9b0FRGdXnYc9x4gufkLMmfbpao0wZMHHbq4XmlGFwW_YQdVOo5KLToyn_wSHaroj3AICuz1GZANBEryTA6YTiaFsicYbLUW58oxuAeEfRGjPDrFyywLkCPHuOmnCEZsiYWNob5aczSO2iwwC6H-t3LwafqZJ2od7ElBs9ja2-qNnzHnK1CZKwYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2GQaSn2R6gIToC2KIY-4avFqlZFoPthhLKrzkd02TAZakifTdFx3sxPp-d58lBYj0m0SfFUOirloDhhGz_s-rqvp8cH9irna2j3plzJgAHj-wH-ZBHN43hCpFfomMXI8Vovb2gpGy4TwWYKky81fCDuwyaAT5HwZAYtPdX3qBpvdwniBAINkoMKObZFaXLcO3PqyT-2Zsg-X9_CE8haVWNYnZogm0oBEVSAA_yVfvD0g4Y12z_3S4794m94pkFiAZZAenv4K7pjcN5Jh2vZl5ea7Isy2LnTXWhgeu6U8a62Z0QCh6uMe-lQMv3Y6czMPhA4Pei4vfHlhFEOrG4RFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=NMmsjdMNtm2RaTj5YMumSnbtOqJaSZ3UCx77W7r4JKudy8-W7rcd2uN0lfqG_27g9RV5v1dC3emBti_4yzFivJR5_voDOn0JCt-7ci81ac8LOC_WRgPsbpEYu9ev4eLkl-m_w3OP5wRbMJHiSy6REn9aE5OgGVnnOgxHEmuwGui4OyIYrSWvqV6P56b-A1_EyvDhu9EwkqQjsO2a9u42PKh_B2IEkN0BRDoRyLI_rP61k15cDxVo1B0Fo1KqRcLueDuRAC8BsMLMT3917SqEIgqC1PlsRwpvGuJcLWC0cdT0jLKI_vSFA_4nQjHaQKHZLmzuFD5_6Xw5ivqmsyPZ7KoDgsQRBo3lCLHOIW-eisNa_DRq4_HHuAk4ou01IPydU7TTl_gcB5_g9tFlyhyDNYdl0DR5Lcfr7irpdobpk-p1XUv53jaMoGhANfomJiIMG-3mY5AINjNf8aqixDpvir86oyqtpS5_Cf-YVHRSLX4LuwG1XiQFNS1WYVHVnRxGNGbWB69y_WXPYWEpjfe-b4irGBpvyuR86HwRFEXk8qcEdL56HkQl_3P_sVBUpm7b8HTLpBTNY7yIL87vVZuA33Nib7oNeNOFqVPUieT4GkRNkAjeafdzO_zVF3begKuWtGAvXmYmEofiaoEz4wYufp9t_d3hwr_xggE04QCvk0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=NMmsjdMNtm2RaTj5YMumSnbtOqJaSZ3UCx77W7r4JKudy8-W7rcd2uN0lfqG_27g9RV5v1dC3emBti_4yzFivJR5_voDOn0JCt-7ci81ac8LOC_WRgPsbpEYu9ev4eLkl-m_w3OP5wRbMJHiSy6REn9aE5OgGVnnOgxHEmuwGui4OyIYrSWvqV6P56b-A1_EyvDhu9EwkqQjsO2a9u42PKh_B2IEkN0BRDoRyLI_rP61k15cDxVo1B0Fo1KqRcLueDuRAC8BsMLMT3917SqEIgqC1PlsRwpvGuJcLWC0cdT0jLKI_vSFA_4nQjHaQKHZLmzuFD5_6Xw5ivqmsyPZ7KoDgsQRBo3lCLHOIW-eisNa_DRq4_HHuAk4ou01IPydU7TTl_gcB5_g9tFlyhyDNYdl0DR5Lcfr7irpdobpk-p1XUv53jaMoGhANfomJiIMG-3mY5AINjNf8aqixDpvir86oyqtpS5_Cf-YVHRSLX4LuwG1XiQFNS1WYVHVnRxGNGbWB69y_WXPYWEpjfe-b4irGBpvyuR86HwRFEXk8qcEdL56HkQl_3P_sVBUpm7b8HTLpBTNY7yIL87vVZuA33Nib7oNeNOFqVPUieT4GkRNkAjeafdzO_zVF3begKuWtGAvXmYmEofiaoEz4wYufp9t_d3hwr_xggE04QCvk0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7512" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7511">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7509">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7509" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7508">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cg-yutX61T_jWyFmcLVBGji7VCEmXbiJBtOEWp3B5y7Ql3LtLzxpPUF5N3QSbcaRQOoALfnPZ_muYqIkzWa_uanIS4s9yiSShhbSj9Dglk-wmTZ3uUNvbT628wLoz0Byty8p7FekQOZVoepru2BxjeY0Js3rLIUnboNMOhubGq9U0Bzmc5d57RQ2K6DOh6BXQ2x7nsv0bHNwSuWpZXTjKT2MFsabzgQg6gaJQXHGXxlw__hoBAKyR3MS8dodtkKWh3HL75AGYNmnvK1R0Ul2bjg7gC-Jiw2FZ4n5urHoHeKim2bEmvLPkuB5PgQmNiq16RogrFBlwp0ue9Z55EoxSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7506">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7506" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7505">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKJJx18clGVdLcc_RDkr0kW_MWwAH8IOPMWsKM-KF48YIgmwIS6BVlWs8Mj-Wl_3EKdwq7NWO6MR76FZ5NA9FEM3A19dGgQdsjxVZ626VFUVXRMt6eeEZYiEVki4s6RgCJ-RTx3CmKPbrafzVBjlBZdUt4ng5rO6v501jrbi6rR2SHdrjzyU7g5axdhzRaIqe_AfADBO-YmhjCZWERrEa0fgZVvI9ZVQvFDq09bqu-JZB5ws2vtBhX9lCYvtFjpz5VY-dlSnm83KcBAOy7dRKoOA4OXoQyMbBypG6yMrPolCt23kntMU39338jyzA87eJPog5oMWQlhaPOCIuOpgqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQB-9CYuuLPXCw6ddu57uB0qecREUBD3XgIUEhrvmEdSOBODRyBotSeeajsh1o5wI7JI3YwLXNatCZyUhiqbHrgCaE3WrNDL9-hT6ryZE9FPNxv5HVIsXEEAjY71KILYkY6P27x0Vhxms_bxknxor2vowKC2a6YhAdJgTA6AjvbX82DGCRfxb3XtjT1OoKPe9tkFsSf4z7Ae4DKTAbGAwd5hCwOo2e5-0hmzcW3LfSwk-MVJCjvdPENd4bAhRC7UKAD9u9isFbOcWuseyo2wnIb8o70lN7zmjqQ1jtwTGoF4gP7_muOy5KQixJu1v85IGTxASfbnS-G024xx3bY4CA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/ArchiveTell/7504" target="_blank">📅 13:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7503">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7503" target="_blank">📅 11:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7502">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXResaW1-Tr7l8VmapqdIj9y-A8oGOMdQ8Xw9q58_jOnTK2eg9-agFnocuM5lMFzr0C2EijO1WPoOiUVOwt_wl17R0KmWl4OqbskNWL5lAwecoGi5TQ3_YojorgswE3UpUjOHO-GgsZFv_mH02pSwqU3tSuHDIfE_thsFqiY1vZkhMGnyZp1xGQCpPU0BxqymXUgyS7S-Wz2UfCWW4rjiokaK18dPQojsqW7nNazw4kFmw7kCbWQSzUURJIGFiEABmb5Mg3u7UD3Yas1lFAa4-lu8lgkHLIC3hQpZE0iDazFik46ixxtbobPFXvrr8ZX7CYYvPzE2Y5i2rEr8mQdyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7502" target="_blank">📅 10:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7500">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=FHeMgWmxEPu-_8FIjelmahev6iDvqr1CN-W1tktBd6TT3y2MCyHcmbH1jcnMWgYu7WTpjRgvgr2HRZsMQV-HDXXx2pc6HvxB8s2xAsVniVCFV6jQUP9wUMWCHBUEdoTc-4IVQuTjDB4FIccDU8-CdUln0TKnLAZUkD6Oz7l246xQF7xW6rBLL8fcU_Yxv0VNbEAxm_zmEtmOcsN5iA9axBCzOLUv9hP3muC6OCrc1iNQdFQ70FrRqXt8LxhelWKrJYmMKt5YYo2F1GTERRoS06qCQ6Tuud6cBpSIWnur0SCc9JVGZ8cEExZsn7f6Gsoji7h91jnHRj7OX4nVSLd6PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=FHeMgWmxEPu-_8FIjelmahev6iDvqr1CN-W1tktBd6TT3y2MCyHcmbH1jcnMWgYu7WTpjRgvgr2HRZsMQV-HDXXx2pc6HvxB8s2xAsVniVCFV6jQUP9wUMWCHBUEdoTc-4IVQuTjDB4FIccDU8-CdUln0TKnLAZUkD6Oz7l246xQF7xW6rBLL8fcU_Yxv0VNbEAxm_zmEtmOcsN5iA9axBCzOLUv9hP3muC6OCrc1iNQdFQ70FrRqXt8LxhelWKrJYmMKt5YYo2F1GTERRoS06qCQ6Tuud6cBpSIWnur0SCc9JVGZ8cEExZsn7f6Gsoji7h91jnHRj7OX4nVSLd6PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7500" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7499">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLUXIjPzAxY6JHFXA-dBc8Z8cY_UKATjCo0TOMg8EoxzpYwqU5-CSG0VDfNMTNU5jP9oM4dBJkwVM4oF8UPiCBPQej9Irt_YnRTB7OQbLVBQRBNeVdLIYvzVeYRU0P5IqLz1Y9tCFAxSLJndVHSmPNptKMyLAYflLtBKM-y0kkh879InHIPoyJMOhDMtPDiKgNv_YziTRJ2NVO71X5Dv8OQis_k-qDF6bon6ZefSXKVWT5qUhtCVVeR5NVSxYvU9mLd__pHki0BGnN3ZI51Ny_9hJZiyC_CIFly1_qCeWYyKciG-3W8KC0zDPgkJu3Rph79nCekgqrr6ajvWdkup6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7499" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7498">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=n6-Zc5k3ky0WSOsixBAL00738z6lffFcpkJIg-7FYCWEInWhzXDmWuxi-2AEmP6VwdW5cS2kwb--kxPtv5W71E10tBhyTgAZukZZfBBSe4RPBmQnUif_ALCYbU7T2fKUIFFJ_ifXWimnbkSbiWNKsRaGMv9pX0s6WunWcPqJQuIOTBDWhXjyvn5gO68hY0TC83omS0uU6uMp5UocgxNAvOAgR0U1BixlrktAp6QsRz_yrPbkFPl6rO_mEDDoox6xcZNh9OTlN-6hrxfohSvqnbhHxd31CI3PpuYx2nKMjSUE4Q9YxEfjIyhwlaIJnMkASrZOx52Y2xkGBGdURElq5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=n6-Zc5k3ky0WSOsixBAL00738z6lffFcpkJIg-7FYCWEInWhzXDmWuxi-2AEmP6VwdW5cS2kwb--kxPtv5W71E10tBhyTgAZukZZfBBSe4RPBmQnUif_ALCYbU7T2fKUIFFJ_ifXWimnbkSbiWNKsRaGMv9pX0s6WunWcPqJQuIOTBDWhXjyvn5gO68hY0TC83omS0uU6uMp5UocgxNAvOAgR0U1BixlrktAp6QsRz_yrPbkFPl6rO_mEDDoox6xcZNh9OTlN-6hrxfohSvqnbhHxd31CI3PpuYx2nKMjSUE4Q9YxEfjIyhwlaIJnMkASrZOx52Y2xkGBGdURElq5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7498" target="_blank">📅 22:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7497">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBwXoRy5mkDv-PYGfmIQ9iWZmhy7eTQqtuPlvobrQmsIRgiU3fMg9VqOP3q1z4XUTF5RBvP4OjY-KzPOLq2ad0MJwgdkkOUIP3vxdcCU1NdLxc_mbqgmBmR7wNgxx0_PkM00clq5uyYTbqSCgM_pLWRkfvIvBzrpZXKDYVCWaXc8o62xsjpwDf-7LCW6IQ99hxvYl3tjJx5o35mH4N5LeUmArPKbPYJdXmkxVBd1M8GWNvt6NtthEhl1TUUi-x3elKNrq9wolP0-NwbHv2jpxQ4J5HjvgvBSbsOuuWT9awVpSQhbQfRrMP7xrpYqcI3pMBFqHoYlTHa1jsIXiqQHhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7497" target="_blank">📅 19:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7496">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SY6wtR9vZbXfe4Phuhcqqi_yqg-gPTL1ieDHPMEMVk30zrYOlVEeCXGTUy1l7HQC-iJcKdOMunIVquSWzowEZG2l92PBcZ_ga4oTEzzDoWO2jc2_H1tPkCEPnst-5V6aZKc-wXnmwYizuQGAyDE_AFgF0cDoAu-h3GpyPSkm7wm-i_LxmfmYm3KnVil8Yh5JT4GdZ6upPCrBLSRpFQ3DcdrHWsxFNAe6q-DLzW_r-f00U57r7MFMCYQSEWyXKvO1ug9F8ZULrLOckJc0hhixA0q-sA-v_ldg8hp0Rtf_l9YVU8xfibbC_F8B23taEhJtxZOWP5Tmyy3WpHjSGOJdcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7496" target="_blank">📅 17:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7495">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=vyCtsU2mamHvsV3IXDEULRfxOWxZuwL44sGi3ViOsWQduSoxmJcA4jTPAinYbS-Bg8QDjMa_d1ds0PxxbT4MB12Ed3SNXN1ZDi-TvSLqCtzb57bgpAW1j3UB_-towKQMe3ZcdA6upNIeBH1zCqSupqXAtaMIBk1UcO5-l42TUnJzfOaWfsJRbgB_5nnToqlGxRFwHFbBn1wZ5rMoy2GOnSnEaTbAQACMtNqp7RBZcz783AOuPlzoyqi5gaOHXrtso3NGcKm-WhvUtJxstXoiqfgdfmHFaeB4gprVFuHLD2VcfIInoGK3jjmQUO4OgBvTCvmAb9FZc-1BqG5e59um7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=vyCtsU2mamHvsV3IXDEULRfxOWxZuwL44sGi3ViOsWQduSoxmJcA4jTPAinYbS-Bg8QDjMa_d1ds0PxxbT4MB12Ed3SNXN1ZDi-TvSLqCtzb57bgpAW1j3UB_-towKQMe3ZcdA6upNIeBH1zCqSupqXAtaMIBk1UcO5-l42TUnJzfOaWfsJRbgB_5nnToqlGxRFwHFbBn1wZ5rMoy2GOnSnEaTbAQACMtNqp7RBZcz783AOuPlzoyqi5gaOHXrtso3NGcKm-WhvUtJxstXoiqfgdfmHFaeB4gprVFuHLD2VcfIInoGK3jjmQUO4OgBvTCvmAb9FZc-1BqG5e59um7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7495" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7494">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-udgVayACFr51m56KJAX4oxUHTtrzV6uPoedEYVEyRxXut-VP9bFG5FNP0vKc7GuOcg3S1PEcGzRVVQIil2iIwQIJqc3zCsuUvb2fJZtDY78apIGo0UvGwZ9ulyRSElhTfdDc-94kNwb0RWv6KsR13TXPPAPHn9gADxi5ijsVvk4vrHefj2V1M73NdkoaL9KZm_Zsx9oi_0GZzWcEiYRKUREDXoZFSRA56v9QT6QSwlFPGd86D2wCv__NbKiukFonxVC3_8k9kZvWT3TTDu-lUqYV3mUKjMFxBhtGfFG5WTlfr9uLOjOcGtU1NLENj515Da0OmDTwG9-BFAriMIqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7494" target="_blank">📅 13:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7493">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNuGHCszybq6HgMqUgx5IK06kPyrnl2Bq2lOCeLiNU6t_qpqOsOj_KLBaRNqio5yl0VDR9qpnpaZgFbssQ3Ea32Pr-PKs_VCQRlKJsDdDS-9d4UXbm5RwVdkndLoKIbWUb8HwlFnFHUE_ZkY1k8nBfKR69lnMEG270H4wT2KWKPizKL8OmBghQ0BzE3WEbBMEuAhJbMaN8GcMI08VyKUw63NhpNuB8JdJXytaWy5K4SBFplGTW74OKCI6Du2wViTdgZuMafVcCQHxprp1qQl700Q8_MOQD6bRKhSl-hQqW41B-lM7IYTzIZmM-wfLaqEV77-cdOt5v_KdBTNqSMVhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7493" target="_blank">📅 12:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7492">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=rnsW1pISV7BRyn8MudaIW6xbYDjolRZlZ8_9_VGVr8KC-U5FCAfWNekAcs-BWb9gsgD3kjbf7atMv4iGRmZ-SkaDAdo3IZesi6BgcLhoeuVOa_pQmRn0RnBtCUU0qqpG3rd8-9PN9UduRBY3ri3irPJnIdKQu6dF0lU92jGHPkdFy3fq9iLXiNY0eRrdmEHbSXBZd9rn5ogiFrqJPA3-HvJl1sRhSpoyAPUC1X-jcn1lp2KhFrPNT6WpD6HSWubka9gXYUDA8Nr4o8MRmb0JToRChZrADOb5QgDHDBhqDCZgXc4hyH7hz_lf5jIAgaCSmOhe_WE-d_CzAJi24oZXTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=rnsW1pISV7BRyn8MudaIW6xbYDjolRZlZ8_9_VGVr8KC-U5FCAfWNekAcs-BWb9gsgD3kjbf7atMv4iGRmZ-SkaDAdo3IZesi6BgcLhoeuVOa_pQmRn0RnBtCUU0qqpG3rd8-9PN9UduRBY3ri3irPJnIdKQu6dF0lU92jGHPkdFy3fq9iLXiNY0eRrdmEHbSXBZd9rn5ogiFrqJPA3-HvJl1sRhSpoyAPUC1X-jcn1lp2KhFrPNT6WpD6HSWubka9gXYUDA8Nr4o8MRmb0JToRChZrADOb5QgDHDBhqDCZgXc4hyH7hz_lf5jIAgaCSmOhe_WE-d_CzAJi24oZXTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7492" target="_blank">📅 12:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7491">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohyElDXGymfz_I5uGzXWp1DIKoF_hNGrwU0PsKH_bUwy8cItmK4wcmv6Kfkw6YhRZuFrby_hY1wmIu0wwhmKMP63oqf8vyKYy_l01972hQ38YcyTZ4-6P6kOxlNRqu2szbsOrm2c8TtpriYsN2PwKSK2PO7RWPjx8miS65PCRW51wFaaFrAIcbBQm1BLhuhgDzwePtnTW6PNJVDq7DGeioD1pxTs2z_ymxFWn6Wk5q3d83ORIWLz65mM_lHEOBS8vxL1LqETI-R05zw7cwEpWDB8h45b1PkbuSuR3x8jD74I1T3Tf-0LfGnoo2XAqybQ-ouV2hxVTpVKji7YdLEQRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7491" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7490">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7490" target="_blank">📅 21:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7488">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAe0KFrsYbhPDrkD5zC-XWZxsr6NyZPW_CnBMeW1qcsbV4tfPuPr838BkUXIF6J8U4XYCcfisaFRd3nqXrOijs5Bl8e4fdnpMJBKV5FoPVrErruzbErvM08lOhjjTebw3C8fJ8FGisXqRXb9k_YRpemMg3eN4S9XUcV5AnwgXGq2JTKo8cFVz2g5VUqK65zQIs1GexFuQRCY1Hxm2teToKM7hgl8T8dx1WiisJMQJQSstNxXUFbumc4-9gwen5cU0AaHOerihoRU4F5XUtFDJEJIRsZY56JcxsqrwcAPJFK3Bq6Kb9wwqSGSZMbp1E29YVFsRLrVz4YNuuTn-RTz0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7488" target="_blank">📅 19:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7487">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWamXmcTzY6QVzlGocVbFGhsI-G_tsYUO_KDR9N9a7eZ6FWcOrTvECYxNe0wYoq1LQj-L52-b0my0XUvIdgdkiWpeVWbc4KIoV1NyXyN0JOGZ-hj8AaTkG94XWrH9YSz0bQwca-QYkKrd07FP98DQZni4gT4Yir8qeSWE6KbkGJzPOqhMZ5xRkZG1j27ZtpZEYQWXSOrQDbDJSlhtjoTWS5DIvA2f912SiQ9Zte3cO6b6-hh3DvcdWQ3i56klWifcUuNsN-Jb7gCdGbtSOlc6UIGrx96RLLaO415-qQ6GXCw8L-0pAoR8W2ZVK72Al4GOa4yHTYGgo55HcGUqie9ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7487" target="_blank">📅 17:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7485">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej28EoE7w7J_FRDNFXh61OXO_qVa0JgR48Rc7QKU-axaNlxxyPMsg8E3bSNM36y7q8L6_Ks7OxKouMGzzkoBfCtoxo7sm25Jd7p7yAP7PnCT6i0S3vZKRCNLjnnt-9KfZzHxa7PRaLesWmwEXqvSnXoigUsJrVZ3Y4KnbVtSmqPtqbaxV-Dz2bmhrV2PPTqzD7D0hsWlTLeIHuNyJmIECfO4jUHLQ8u_KnBIwCGR43jipjp1NUhQV6uPDIEAusBimZA9nRZyygu5p0f6GUYtKHAnPbWSZ4466zb34QibO5nA-qZHIErWoE4C8FrOCn3R6gruM-QbDhV_UL9f7Ao2lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7485" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
