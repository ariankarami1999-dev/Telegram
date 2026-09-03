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
<img src="https://cdn4.telesco.pe/file/goqBWJ5aXGEqpV7xMWvOtpkFShVtC39CSdbGNR2k-lGg3iBICa_534wX8xUzChvwEHLchPhAZ0DhQ6IdmlkSl3z_tShsrgFKaQLGVyym2uclq4NxNBdwZSvGjd6UShf5RGBXXO6UlNsJjVtchxB3n2nEGU2iOcQphVOWRTC6M979suUM8HhyEw4KzhgSLVDfNngPvhUC0ieK6CjKrgwCMLHXrvD7DIZpFMtCU93eGnY5MPjvciHsuM-p6p-9pp3U2hCSwowt8v4Xe5h3sblqRF8lzEx7I8_SJEFPhXYYBzcd15uBbl9DZwOK51M5MRqHidZEKp4TdE8RSinKGQ34PQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 20:53:28</div>
<hr>

<div class="tg-post" id="msg-7616">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اکثر شبکه های عصبی جهان اللخصوص chatgpt از کار افتادند و فعلا دلیل اون مشخص نیست
❕
@ArchiveTell</div>
<div class="tg-footer">👁️ 452 · <a href="https://t.me/ArchiveTell/7616" target="_blank">📅 20:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqZGb8ybNlGTvmgAfVX221sL63l7co1Hkjs4OYIa8yuHe0ONrtMud8r4maRdQN2rcpxoXpVQG1oxW4snbY63jsJiFGLdc8w9Xi8eoQlR9dbFamAgECN8Z3FnYcqr-Vn8oydeI0YwRmUC70cszVa5cc8OuPG1E036LePFuTaAO8z-WY-EyDv6z3cYY-73yxGwcXAJx0ElRn1DOTwOtRwwsb_fPXQYhwdFJsi9etH7LwaNq54kTzQwHDy17yaL-hLC1UGV6O63yEcHaDDGB3P9boravbohG4NWK7uPopdpm1fpJLGxjEnss2_MZFUEPqst522s_F3xRFdwxlLa0NSJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 687 · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7Q1O4wHCam1No3dBd9TNMPgHk8vxYP5iI4vIw5QAM_DvCokfqVUMqc-UYV-E1AK9XfkiaTYbynJCVt5YsD33npmkhQZk_l8rnbXtcFdmA2dGR80du6uXfIQfjFJKQUcWDkA0yP9x4zz2iQFfss6Hj4mUQaS6kbnjfRp827aHYW3mMkoxnM2fATFm4rq6SImbnsWAlGzA7GxKedpCYLQYi-Ywk9GacWCtVoBLyL2hT-gVxJNkRPT_35INosi6ctP3cI3J8n0NtCsalN327d1quMX6RjnhmRlCHXDBXIRzGlKW2xw8XPbYevOxz5eTu2-Y1Kvp54DU2IZY3ikRrM_9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
خبر خوب برای برنامه‌نویس‌ها و علاقه‌مندان به AI!
مدل‌های قدرتمند GLM 5.3 Flash و DeepSeek V4 Flash الان به‌صورت کاملاً رایگان
🎁
داخل IDE چندعامله‌ی Verdent در دسترس هستن — بدون نیاز به کلید API جداگانه یا اشتراک مدل!
❌
🛠
روش استفاده:
1️⃣
برو به سایت
Verdent.ai
2️⃣
نسخه IDE رو دانلود کن
3️⃣
وارد شو و از GLM 5.3 Flash یا DeepSeek V4 Flash به رایگان استفاده کن
⚠️
نکته مهم:
این دسترسی رایگان دائمی نیست! محدودیت مصرف ۵ ساعته و هفتگی داره پس قبل از شروع یه پروژه‌ی طولانی، حتماً سقف باقی‌مونده رو چک کن
📊
⏳
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 800 · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 947 · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7607">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7607" target="_blank">📅 22:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7606">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7606" target="_blank">📅 22:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYU6x0rLjfLC1MpW2NPGnrJwnt801H-tJ27WIxqcf1TruQXTMbfpkb8nwaLiqugN3KH8xGiTzjitvGBvCVnsCDFzqDLFWnIuTN-T_8c2n87S6zZgCjBlAlQfu_FmsfAnRzYEbjhuMvWrOcKI-YZLPSP7Q8iNGtuzbMcNvQtuet14QFptAv7a1RakX7EE0-WkUr9CutrIt08qnN4J9gty7H6dJVl9Ajvjt7IkRWgbYEubcTKy5v_lWBNSFfnI707o6sGR543oguBj1Z9J7M6N9e2B0Notkc_myzhPkA_2OttWT4Downdh4oMdg82NM3pYFvqzJRiIx-6Ldksxu4frcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBOif0M9BOc3xvMRCxKzas0eLr2hsNg4ZbWdDow3ayZyZk8HT4c1M4Z3t1dOPwYps3IVSDBXfY5YEq8F9l0Of6GRuzBoSl-bEU1Sq4_ri4BATrV0SOHuGgc-S4ILdzYNY1gocOZ2pzOgt6d8xKjX8AdL1dA2xmLAi80etsaP-qsdG8Wj92bda0dH__sPKpWChbcoaz4F0vgS2WrrFdPgVU5nqQ2TFjGIdzosW-VnKsK5R1uXBnW9hi6mvPQEWoOlVMI1c39l6wE_HpNCOdmFDjJGYRmVaKuaAfKlYLjfSdB85Bcx848fADXq7pwp_rrJydwBABzwpBrxnw8QebW8EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBth4GbVb_40oJ9W0bzyhJOY6Y7c7WOlTqvEGehB1-cHwpjeg-L3-XRIJn5p7ylotF1XZd5GbMGpfmLY7rUYv7Pe887tNMGbICPIHX3oNcP1K5-iVNsuMwsWkeZOtWNDH4yThP7yKibUTtZ0kSBIF-5xm95bNSN7NnFJqsoAbApr4AJJSf_k9kgAMu01WY6K7zF_YyckmyLw4J_LsNidHRK6ysIr28DzM8NbFOEqvuTICX1m-JpWQN5iEgtIBkwnsbpHcyVF2pQ0zuo7wPOIAubpa-iqOKW9dSdrXeJYdvNWyxpYoxFoGveOe2WR0oeeWuNTMkaLAoJk9ZGzfykZIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZT3TSyYju0WoHua0oPsriH_S1sStqu5UJ_gKxrZSl6ap1-W-5dbVs_vicWl8VgfH7w3qJa1t5GAgIdloUgpnGjRXcyburXlpWxGFHYNCOnc9Lmq41msrXDyTpI12eUKdDcOLW76P_yj8P2Egpv3bMoAjFacqLSM45QDv-cmI9ziquZ74As4EnmReptgKWZfYhHjoZxnMBjRqP4OyLoELDO-0PgScpw39oBOhHThsZlVKwX_qY6ZIGwre3boULZeO0eKj4SeU5XNTiva6RmYIwe2IIbgOLbh2ljBHm7ZPVcD_vChlHJ8wXV16MiZUnuiOrp7OYyAGT-x5WoSDKnQfSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSMuTQnhYSIa3Aj6Hmrzm4l7kFnDm_zYgTo9BXqv8PtjlxBKc9L8MPDN754mGWNixsZjyiWIQngKaNlYGwPuOEdS-PAdKdZPuAQNQbRLCkpavocG4ix9nIYTU9FDYiNERJnRKzO1acV-MzItjdyExSV_4L7MVOwYkJigTxmhOiJc9wScZ3L0TDVSP8WvwttnQXt6uCovYvPT_L6FvjtCdmqTo5aSHHmeFqeHhVBJ90-cVUvNHeaPkKF44zcyzcoc-uThIz9Ybp5Co-23leH6ttiOHvt6tRklDvJfF5kiHosu-Ck2LCQIUSdc9oDNl6zThEeKYbj1MFkHqXkjLHK51Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFBBzMdJpwePTu_eoYCmdjI6-DiSXbgjQz0IiRuZDvMJloLairuYr2HL80nd1NfjhEnSgr-5Qx9ycye8tBuV5Gx_GmNTBj-haX_RxCLeAii5y43tWO_2We3dBPtLd9BZ3kIaZOsPmQ_zniFgP3YxrOtSaAS9hN6iYp3AM3m1Cf88gCmSB5R4_DpmaeUM1L_wQ76O2rxTdy0K58yvZhi2yFgPNyxZkJj6OrQvwHxueKbX70OGwhW7cWPjpsFksOr7sAbh31iN9LFDVNcaUzQ2VCNolC4mnVcXtLhsBjzjbJXXucqHUT3nNy0e--ZDBbddYznqdqGVYbD0CxTu0kZ4mQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Su_gipzbb3htHJ_aLikGQUvWpQt9fpGbiMI4bWtYxohd8R1h0OBHbCtzNgrfG6pIhEBoPllBdsXi8MjBTI73UFxxzDL2f79mdWvDBNCi7OG303HJ6Esp78iEEm2gTXERxO_ug94mCONK0FsCrGwsVV7MmDHY-YomLNFTBZA7q7Dzr4j4W6640rZf2D0gcCn_cLYWxwYQlWupydLDPmj0Ui5l1mWX9LiGhmWlTSXGvLMBDCYzxPpWSkUZ6QBvT6Sn6FvAgZmKS6j7yFDLTb8BrDvc2SS5EFglklShomzoiPF9_XCOSXnfeCiSs9TEmnb_i_DUykdfZn_aGnC6EBYQPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUQjFwnz7mXyqMihGA3cqTvesoik7JnIV13wD4n701CfiYf-Vx23NrdXG0AC5NTEJj3ak6wKu4HP8N3rR0rUz-1GQnMP5nyqAu_Vr0FIC-nv8RIZ8ssXWbwK1L_beQ73FkykRD3Zgdbcuu8rrBgisUqd9FEw4CFJhcCWajcVJ0w6dgic4WHkeRzaM32awpQ6fj68fygQbX22RbuETfMuYcxX0r8argeewF7BcfZYbDVyzWQMi5LAcOZmXrTFEO-eDww0T7a_3ptap_DAORtzTIVTv-Vk8nlNPSoUARtCHGVvBMLAinm78YrBjbIQz5FfrQFxaFvyVyyB8GAJGcYNzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFxXrIGJc7KK6cXnIp7N99I7fztSG7ceHzEypGkItS-FdqzJqf1Z6OpYR4OqkdjZz-_r-0zr8PLQX_tvPekJx9JP4-RpAjMoIXJ19O2KpJgVZYAQWcTwpd1jnclDybZY8IIsfNAA-ssFZTRslQztzQIeF7HayeBej06StppunTXDo8WFG2fIIRmlItaGsCEQ4cZUFOGBw3sqUfNWUsgd8Fbhgwv9Jqk7JMktJyOHKoxv5wKk2mFIrM8UJXYo2Qwh7Rl_QuL6fUWJf6INJCY9okglEeBKlucwNR-POxrQIuf2H4PJtPVF2xTRRzbeJSJiF7LATx40-QF7hs3Se6mRbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQY204dT-OwkA5Df8y0m-udNKYK5DVT5XGCU-xhU2E-r2wYgfxEzpDaSQj8uI5Zx4-umWmZ7DIehoqDFAH2ljqoEuSpOJAqWBh25UHk_RoBGUai42jpwR5Q9b1--talFx_pBVQ0kxKAUKUslppzuQ5B3Qq15e-XLxpgSzNznomppL5bvNF4wAw1eru2MnjpugWZ87x1Me0mXttI-mrn1AdrpymsUpJ0bBW81784VYcXH8DZNREm96mY7vlPKWaByCzzOmUC5K-ZGa0IeLwny0NfjtHDOTWEPj_lWUQsY2NxjWMkDCx7gpKNLvh7DbdLVCVlxd1htBOeTg4zsECMRoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=GlNEvhZrzc_u1Y-DxlMCxdZGoUOeU2fxxIbfpWy3RfqQWydzrwegYjcx-9svBwLTPrAYd93CQAWpH8FE8oxv6dDm8t5vQjzhrmC3ZRrph05qNJrpdiyL3DhyhwTrH91WdMyPXrPYESd_j5_5yI2VSixYNJat7BhEDU5bTcwHaXDNFF7EaVjQCGIm_X1K-WQlpgink3CRmlr8vHe8XVwC6xO-E44mQYk9oZsXiGHNebmYW2m5m_Iz4tky7L6XSj3u8xjdtoYBsRxD--crxQ6UdBvHoZ1sqvZrQEoW5dSbdBbXmRuBLB3e5X5fT9zGmK-w1m3Tse8z_7FjJJOzQKvAQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=GlNEvhZrzc_u1Y-DxlMCxdZGoUOeU2fxxIbfpWy3RfqQWydzrwegYjcx-9svBwLTPrAYd93CQAWpH8FE8oxv6dDm8t5vQjzhrmC3ZRrph05qNJrpdiyL3DhyhwTrH91WdMyPXrPYESd_j5_5yI2VSixYNJat7BhEDU5bTcwHaXDNFF7EaVjQCGIm_X1K-WQlpgink3CRmlr8vHe8XVwC6xO-E44mQYk9oZsXiGHNebmYW2m5m_Iz4tky7L6XSj3u8xjdtoYBsRxD--crxQ6UdBvHoZ1sqvZrQEoW5dSbdBbXmRuBLB3e5X5fT9zGmK-w1m3Tse8z_7FjJJOzQKvAQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpQ2BlXe2y0C9e333VDxij_BVK48ixmj6LOOXieVvgc6PGl_iE6JQ3Jl9LL0_8pYz1m0fmZQ32A8ROLc-Yw-sWcvPHe0BIGJL9Stgd_DWNCyz8KWGqfw5Jd5MJ7yrgm9CFDm1hdGosdo5n78YbQl9plU-bIoXwi2kQCWdi2u9gGiAeKcbWSpS4rr8R2QNQjaEWNX4UtOkrCobpS27WPO50jloZ6c7S27_ampxFsHGSLyNxlrBg2EclDjnVrZLq-XBusgzp4nwMcacV6v8I_XR3-G3U23PCc_h4uSBDahhHJg3VtKNXbUBBLU4Sktg2mtR3iVzo4MkedjoOA8n3RQpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=ALkWjr6c9itkTvFYrxQqgWp2JTDOWb2nGs7VUnSAjTkiKBXBVtwiNEceUlkNXbazudEE2QaW9fYP-T5ld2TRc2D_9WsUuzbv3b4jqPz980PuYt6j6ZZpgjA4NFFUk_972WI7DGN5Dk9eVMMSFH_QmQr6odt7VClT68-fT05YndylXq6fpr9gubfGz23nfAHzmD1VVp67hcXomy2MFbIxsgZHN2grySciKZg9h7ZeC00PRqy3RdL6I5SqFiOOGJLn9h-C5G9YEsXsDOua6Bl9PFFQi3ScAcU8Fnh8miASD5PI37oRFTSxYmr7kL8AuX4eSxD5Ns1eDunsa6zDkxfdzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=ALkWjr6c9itkTvFYrxQqgWp2JTDOWb2nGs7VUnSAjTkiKBXBVtwiNEceUlkNXbazudEE2QaW9fYP-T5ld2TRc2D_9WsUuzbv3b4jqPz980PuYt6j6ZZpgjA4NFFUk_972WI7DGN5Dk9eVMMSFH_QmQr6odt7VClT68-fT05YndylXq6fpr9gubfGz23nfAHzmD1VVp67hcXomy2MFbIxsgZHN2grySciKZg9h7ZeC00PRqy3RdL6I5SqFiOOGJLn9h-C5G9YEsXsDOua6Bl9PFFQi3ScAcU8Fnh8miASD5PI37oRFTSxYmr7kL8AuX4eSxD5Ns1eDunsa6zDkxfdzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJR3cmcKw1c1RqbNJSroObeD_jx2gGD7kxRHNCMsnZAh6ehDeAPA68wdnIHEXW3ZxH_4vhKl4iraWiFUK_ym8vXLwm8k3rK5Z7rNQ7e62BRQPK5KeV_zWcouDubNQWpZ7XjqzTyTVNzmSPEMCvNlAo2SF9H6qWLF7JZS99AnAnhbcUJneXRiqQDmWXtGALP3Ax2PuqsAUq2O2APwAglhBvN3P4T5S1R4kN9aHJUSeWHQEo_T-DWh85u0EiPwlNpA1fSmkn0D_HFGNfdRZ5QXbywNBVpDhJIGzWpFdoEXvygJE3wFrATSCmIcWClbDS2PUX0f3Rwi8tZsn5xkew737w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fiqkd_6sHFqScB9sCnI3tfhxgYPPcORxTulfo5WJm1NuXU19vH0pS99ooK2Xha24hnhbPwC2zC2g-2vuEc0uA_rm64E3SaE9k73aWodUi7Fw94XOqU4NvkmTb0FXHFwjEE_TbmBqazfldRCe-lY5IQkx5rPj7HSDS-ziisou-ndvkMAvBNpht9a7_E6iOJh0xJg3v5HWTVw_btNwykkt9_yLyM9BQrzxs80oQ8bChWWj0BxP6mhmFLjASk8oeavAdKVPHfADL1sVuJVMrMeZq1MO5yrJSPFdnLf-s62EJ7_6_7AxbkFsAQze66IoBTLucWkCII1rOm7k-Vmsk6OXJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M_RimEEx0TE8uEnjzEOQvpyR5lzLPj848ptKDb6Li9XEunC26QO9AvrF3SOZDTakiUb1sERzUHEUPNZamOvcEFqd-RL4XO75a_EKHAykVrY55cPWC3RgR4lbvTdx28tMzJSPTkqnX0HT_BnjQruDn40jTDBd8uCwxpnzSUGo4hFSyNu9xpLXvjfFNcKVLoWCWHLEfB1zUh2VvCoIsygPBbgF5RW7Usl_5CcFQT_iMbV8Wsz9fLjB4ajMkQUCUZnRKVZCcGNTeoh0WprHBoVDy2KEcODqJZIgNjwMJohylmtG3N-8D7T0cHBcgOjR4-kKOAUGmip3Eyc-9cmB2eRXoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PhhvoLxY6ChQwffg4hpTpLyj9X4-N0tk-f8QzmJ0CYhAHEQlxzaHO32wyQiusbc14CkzSwqUyxlj_6WJFhMfmrSV_QQPVKptuEdwWmmQMqCzeOKbuoWF_95Sq6MpUbls-3-Bc3qLKbHIAEYMpMZmohGPbRbygEcVSpeYWqYLCZJanRWL2ExiMmFWe6IOXIVtjB1kDkmI4XV1WrjAinPap5dqwafndwCSEeOoQqK0-vHZAuUxKYmawlf2TPp_o7VsLlDbCdTx4QJxRvO5r46cqvEi3L1MEQrlg014UhywlP09UwDsyyY_WF433OIZY9OPhsVvnuGXHTImWEFn5_EBKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcEi2ejbhsNYLsQHVZHvpiRirWPUFXtcilh_IYx8-Hks4zSb2ooasroZ5VUXLCTf0tVwZAD4Oj_57uHhhYYl6tHNme6d_kUKAECyLWH_oJ-2d4PqxIoP7Xkkgk-8NGxWJTWRZlYEKLs8jP8LdeDyhIw-FX4C1JtDT2K3dz7Uxjt8OBj3l-PTNKUiQHd3NjwtMy-mHN2Nh44acfjGTU6JKHcJ3eiKsY2LfDNJ6-XznK9wDugk90RCXiIolMP0NnxgR0HaW2P2iVLNpQsXbu1M7sSZm5wL1wO0QSfVFnPZ7eEsNKX3PLBfefibKQnmbYiDoQ8FwgeqlE2Iy72eDlIzOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Si9McP1xoTTFj0_UaJzqHz7NaVQLExGicP8q0XLKKN_G_K-4G3dNIqSINaq1sdDco9xN0vabuG_7PTY-KpcOvgFmFUuG0GSPmlSKGgUApWbfMFn8LQj33lHp_an4W1h9QxCyqTSQftkuRjARlc3NWafIj2wnRf05mx3GCPpILom25xhBE-fPPOH5ZA9fivcagK81aykAQjmyF87sKZ1nUu85iFAvZ-axQH6Mdjgg6LRSrKymxaEwX7Fj_arjuiLqZBFicirwWlCI1ERXiq3Go_RYDWHppzQ_rnXbXigaI4U7w5C7aZZ227lGBZDT4hRg35yWhavYPOqXma7Q5ssULQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzkZ-vW_GDQasWBQ8B2otzDZeSK0-6Kwwgli0bX4ZGH96OiZmotFUGpL-Azth1WqK3LJBxfOlw7rT_D92fXMZbToDLvEyDA9Hia1QpCQy7p8b2z-IrLO-pTVVUHMcSUbOOj-KZBOhIMQpD0dH0zZF5SXd5oDeIH0Lgrf72-RXAsg0YMLOr49vNUd8ww97cpKRwCxJGn3uYAAqvMtA6z7JVbIYpSB2WPzHXg6eNwvyMGumR3Ne-nGq6rX1cpgiZkN9wGJ95H_32G39wD5KLi0uw17PyAAEPB4AR2AH6AIIHg-2gmA2kxVh434OMLkJBagVOVETSE2dqZONFLiXd_XVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChL90nRIIuKTbZXz2GQtQlFmyc5kUTnh5FC1wDGiDcgAIdCN_zflwLmiCscEkuswuVhzZ4PC4vKytfCNVxW1Pg7SOG_kfoaNt_j7QG7Xz4VMLZt6KaFOi2wZUJ190EMyv8A39NSnhhAwKpDw8LqoA2acg5wDNUKX-_4RQ_7RQfinbomBmfz9RDokKhAO3emgzlqahj1kW03JhkT8ZqKk2FStowx-D4Z2_jNQ33wlxcmsGsNlVy6-VB5dc_xcQSJIdSRglvVgQ8IXWUpHZOv6InCbw7VOj9Y6REnYvHcXDm5rQSQG3QHHJ-8yKmwV1GHtkM7wQ2d2Smv5m-6I2ovPgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ee30ckr0ZsQC9JUYbZg3P7oZl-2kWTgFrJdU3xH9GTOMgvlUYLvY8urzsbG2Re328giVKYqi5CtQnlP92vKSeY8HcXQJ_n2ckghiMFDLUIS6ZTWhAa2VHd31iLEeqh5f1EAHwN4eBvsXEXDT78VlXGsEz4nRlA6CKg4GpTD-niigqKdc8LOPD9h-Z77KM3mnBzwRa26OKpENgft-nzmTqxPVEs5mlFSI5CzxaTDbii7vY9luFerfT2eprQ8m1xfKSTKrjWdvhA_uxY3bb23mQNkkN8ny4W4mGIc4gYnYfNs5dhTyJJ_fDLiXWLhjVA9CqbG5fJpEHZVdvjGl_A6Uwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7BZLeKIORhGonxfoPC95_D4-wm4NT6gKzc0Hkydx1ZYiWXzFJLoVh3ZgeBpRjCKdmWheyOgr1wcJgdit2cJlytFzdRrJ9BpuK3E1M7usjV6AiSkusWK3toOe2Yos73Y8eEewRPFBrQlid8b1-fNWiLKbyiZGBuxIWZSV6BNsndzMdfQEFqQ8Ci-GS6dqipklgRSEscRFZAyVDiXDjWs31nuB7cJLoxa2LD52QhUDAsx1vlWd78VXW6JchSTZSHIFZISLbmyN6rzEhCvUF_3PpZxllSfcwZpuhcWAL_KS9EVPo69wAq6Su9WZGm61OsH9NQiDvIwQysN12uVe01P0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZF8qLhj7nidg4zJhJ7uOwwS0GUA0NRqlsM0K8MDy5JDCbJ2Z4LKA0AgmxBcaAUhVRvD78EcIaIopewhMA_yfqaEvkLHdHSQ-cPasG1GmCt1aRzZNWHRWnGCmDeTZbfF142OIWsa9AQtDyUVaysXJB5b7anmmrhF9IAlifCffqOY-leuIZw0ekzC7yvy2Tk6bswaupguztgmKzhx1juKL_dweTNIJq6A0dkRGANVJo-jdhrjM388w0cVEGXDuXCYzM9eXRKyv29-2XnV11eQkJawBQiWYk0R86ieZD0rGEhrDFOzrEcvPKl8DNaIJECmx6aT0zm72_gk_g7Hf8F8VLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-lq-iifQKCzmq29tJp1fKLqaS8SLNI2Gtpw1PTzwsDI7OMMjzdhAoz5vnOa66LnOKDpqGWTCTjaifLQaLmyS3lYO1hcn3AoC1wSXJ_CWLuvaOeWcCb_F6gtyykNE9tOdfJHBaxVQbgFeOlbl06IrCbTaq4WHdkAQKJ2gOFgSMbbeqocDysMeB2XbPBj7m6_duA0An-h8hcDOQYRPwTbaVSPal_hMNjhvpbQY1lLlA76l5U3__4Dme6k-dqYIeihXmnq9o-iQYaJIPxE-HSQZ9J-Ar_uCA7JaOQjm6MLJV0cndTlmnfWGX2TKqZM6IMQyQYlIzatLNfEXzvKmxfEpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iul78tR2nUr6SHWcFgRk4IyqZGNiYc7z18AMHNv_I0Ah3hH4xz0ws0T-IU1Uo_itm9WJ5caGcvnmQFg97CWkguW1HZdjMSEmvgajSd44oTa48-ZUORMPIs5v6Nm4vFqfU6t6pDh3noQbBSbmRc6wdowERFm9fk1CaC6l9dL66S1oIwuImVy1Kj0At_wUyApkx3f7XO0e4Rur9wTK7C4tAjf317goriCrRPP2t8SwSH6c9mzOoEBhpFyIjLHBCdDS4uADELkllLuMILbiR5H5RzaVfSvCyBExnVH90vy67UlKEZbivOhcbPIQgUPpjJwPoPEX4v0YuSL9_MqvL-yHdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=Y_a_w7RHRwzBO9IhKK4Wk4L7EUqPdSj6W8m5U3goztb1b61scNZrdymx25miTBwRVRZATO7PIc0kuX9hzXYTiCCyGwd9bI98yQK6mobdcv5ZTNJDSNjAGh3gxBWzQ_qTPTvY-B7YfH8ZhyuiQOv-IfPHDJ9X5dGHw4G3m4S6AJLnoO7yKNDjwy1YlWSQmeZx2DMv2dQnyoC3E9aLiFrFLC0FYCc220AfVWwqDPzNY7LifsP6LqwgMRQcNjBO-yzoWS_pSwK1UJ93F5-5tgoEOWYPUCSQ4bZ34QpsurcCWiAJGgpxlbE21ZTOYbVLcJuAKIdAdnr2eVcGiowPF8zAXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=Y_a_w7RHRwzBO9IhKK4Wk4L7EUqPdSj6W8m5U3goztb1b61scNZrdymx25miTBwRVRZATO7PIc0kuX9hzXYTiCCyGwd9bI98yQK6mobdcv5ZTNJDSNjAGh3gxBWzQ_qTPTvY-B7YfH8ZhyuiQOv-IfPHDJ9X5dGHw4G3m4S6AJLnoO7yKNDjwy1YlWSQmeZx2DMv2dQnyoC3E9aLiFrFLC0FYCc220AfVWwqDPzNY7LifsP6LqwgMRQcNjBO-yzoWS_pSwK1UJ93F5-5tgoEOWYPUCSQ4bZ34QpsurcCWiAJGgpxlbE21ZTOYbVLcJuAKIdAdnr2eVcGiowPF8zAXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=d_McIAS6-ZUWkNAFVo_k1gz4g112bwt5K_fjyNcaZ6Ebxfa5hULlOz1XtS9Uo4dlsq-maBwDzyE-wc7r0YU3u1NujIM__up8LMLY0r4-As5KWqxIw83BPIPArcfvY4WXAYIQZqbtyRKlLUkgOXfpxfXLsGOAgZ9zITvKlsB2YLYAaMIuHlZ-kUmPM9xYJ9CzMdX53-oYLFtyTlDkiZ4nQ_J5JfCmAs-Au6efuZ-2Pu3KdD0NhYPJvqxA-oe_VN13YrcW7JS0d6zkwMuumpPVrYuOgX1LjzqFTopmQB__lydJFY8Ro0ePbxfEFGOrxfzWD_2PTCgJnNo330jET1bSzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=d_McIAS6-ZUWkNAFVo_k1gz4g112bwt5K_fjyNcaZ6Ebxfa5hULlOz1XtS9Uo4dlsq-maBwDzyE-wc7r0YU3u1NujIM__up8LMLY0r4-As5KWqxIw83BPIPArcfvY4WXAYIQZqbtyRKlLUkgOXfpxfXLsGOAgZ9zITvKlsB2YLYAaMIuHlZ-kUmPM9xYJ9CzMdX53-oYLFtyTlDkiZ4nQ_J5JfCmAs-Au6efuZ-2Pu3KdD0NhYPJvqxA-oe_VN13YrcW7JS0d6zkwMuumpPVrYuOgX1LjzqFTopmQB__lydJFY8Ro0ePbxfEFGOrxfzWD_2PTCgJnNo330jET1bSzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLEWRzZ80XYGUMuOWq9afWLlkgaxkITGrpIHYmxN7Ij4ld4Mn_Alx9Dcr6SiPoQafQpuVmHyAWdZKOkAdosWey4ero3ZkOuLDESwEu1vuk7xN99mP1b7H2K4aw4xseO2t5HqJGPOQUNHiS-SVGzK33LvzhFMG9-NRTnGUFflNu60V4_D71VzxQrVzICgKJxDqqxQ69ahLpbofO2IrDPM9SCnMxud6K0qVdHkOEkof4ULUOce6t_o_puhOHzEnxhleR1gwT2u-4GhOirvNuXJ1o1ZDLWAXcvormhZrbgcWDWGI8WEphu5l5m9AcKmeso6ykdabJGHgOMtwIbVsw3dtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqfFJdXkwt5UZO8XKCaYfznSakEJrFe4ZKkmtewU2mKtctu8PnO-5K5W7AuDaxECjaiZ4W3Uxo6EiI7ReeNE-aKaIuCtBSZ-i0REHwYu9X0co9VQKfaHbM3TPn21snvlqTxSPNDCyvKoltPxGp8Cwc4kVUcd-JSDSs-puS0wdW9OKqExYjKlzH5aKuJn2Dnj5z5bVMtF2LoCGLbV5j7lRaV420fwFvqC7n5mCIyVb1P9tlrQZTLz4XE6TbqF9rpPQN6Cl3qEE31Fw4y0wQa4YQaoXabm24wnJ3-XuiXRc5PZSbw_be90CJSoDKnGNLi43l3LPsbn3ks_ddtx0t3c2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=XXLKeIv02ZBOtGQ8-puHd2p99OtFDzai4UlXIYB1Yeuoo0nbJjf5HKd7OIillP_MssK_Z9cC6yDwkbLHCUTt3cGaT-WQFAE3uJuMfffmAl7TqeF84dPOXuhEe18HWadeoJta0cbkYU9Qooj3XqPwdbDjOgDN8G7QI5DN_IcDMAQJAm9oTQo6fy40aDo8oYWZqZgFHzy9C8rjl_ms73xrNKr_9dUFEq-L44bcx1PACCiRg7XlvBkvU4FORthceoTNhbKuYNMtfuIFAfc-RV_snSF4tSbmiGTOWyDfLN71Tof-RW9uvRjqiaal8hY7rPwYuUUwXm3Ya48O2jMwC5tOdlYGzyW69xU-I3-eVO2FZGfs1XEvjg-gHEOeHgEFd3CBKBorYe6hmjLULODUx0T0a2zfjwUqCfqwZ_P5pGALGKHYBNz-iCNxbOJiQOl1eu7qum5-cuOY0qRCbOZ3N4nUIQMGYtDjHaesagua3EO_QHaTKmb-pqc3EkzvprMUVATPkjsouLSVVGlWuh4LNgOwxgk9nBfPyzHVTqcWx5TAz7UPk_oy13q9PfNiIVZEYvy1WsuCp5sJoDEVHW-vXmHiAylOgR9C4zXEiMaXA83WALy7kr7XNUDlr6n2aSl07O1OiQ37OtXy96eWv1TZsJ-0LL2hFmwRDgrro8wz0tJV3-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=XXLKeIv02ZBOtGQ8-puHd2p99OtFDzai4UlXIYB1Yeuoo0nbJjf5HKd7OIillP_MssK_Z9cC6yDwkbLHCUTt3cGaT-WQFAE3uJuMfffmAl7TqeF84dPOXuhEe18HWadeoJta0cbkYU9Qooj3XqPwdbDjOgDN8G7QI5DN_IcDMAQJAm9oTQo6fy40aDo8oYWZqZgFHzy9C8rjl_ms73xrNKr_9dUFEq-L44bcx1PACCiRg7XlvBkvU4FORthceoTNhbKuYNMtfuIFAfc-RV_snSF4tSbmiGTOWyDfLN71Tof-RW9uvRjqiaal8hY7rPwYuUUwXm3Ya48O2jMwC5tOdlYGzyW69xU-I3-eVO2FZGfs1XEvjg-gHEOeHgEFd3CBKBorYe6hmjLULODUx0T0a2zfjwUqCfqwZ_P5pGALGKHYBNz-iCNxbOJiQOl1eu7qum5-cuOY0qRCbOZ3N4nUIQMGYtDjHaesagua3EO_QHaTKmb-pqc3EkzvprMUVATPkjsouLSVVGlWuh4LNgOwxgk9nBfPyzHVTqcWx5TAz7UPk_oy13q9PfNiIVZEYvy1WsuCp5sJoDEVHW-vXmHiAylOgR9C4zXEiMaXA83WALy7kr7XNUDlr6n2aSl07O1OiQ37OtXy96eWv1TZsJ-0LL2hFmwRDgrro8wz0tJV3-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUpr7vqwD-UbzELxFUuRg-SIpwYUEl7SRexTObNm3OV-RfMtMxWofNvY3zyCxUsYQPWvo0ox1tDBdYp1uqB2tQeLxGwH2fTF-sGHj9P5eFxu013Adys-E5K02_08-p5a4xmtt64p7goL0_uhbX-wpUXVbuw-1nIkPTkRjCR4rLcSD3zNzfuPsVrLlUX4FaZoDeznu68Sckt1eD53mZTYv1u2kCWf_YEStl_EmiIvOm4iZhRFOhITq1NAaTQZzOi_JXEi3-4LKZPq3jfm0A1gLH7FRYKyYjTIx4JvVO1FSt1rVCcXHpLaiHZ7L0h4t0SFIwki4BjTz5vcDc6GvaTKQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnFEymVuGMfgcu6-TJc32hzDa8QZ1w-BsNukJRQ8mXhiN34dnb3cR05nQo3bNsCX-JMYCAT-l0O4Z9bEQEglNyV2An83JcWl4gIeIO3zBmN8HAaglpIQY1Au4vAYftznB1MUXYryuL1GxrhcZCvKkkbAXhZgCGeu1qFw_-lZXoTNZbJMJ5AIBw2gyGCNTQKoZSoXZxi6lgvMWMtZpgvEl8h95lGP4QDnHkVffmiYYnY95EdijG2At0opFc8VDjXp8r4LFDUrnXNE8FhtkvRz4YXvvqzbDueCWMi0WPtk3UufHLt_a6nwpjBRxQi4BMhAG93GY2GX6bsSxPfKktUR0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukkx2lKp5KrsWkt1w-G92T6OJYb_ylFh6qIy_fvJGYt5AVd-7R_Cxy23TSug5jgZX4feRzBgjpkWbRBmaFAsnCGU-q4MPCmhvG4MmS9yIh5AOvkTc-AJgyqpMn69YMf3O4KOhdxSPfZqbrwCImGaQPxJb3vYdPTc-BazKHUp6qFJ9VVlwt0dlo7yUbf_XqOA_AAC2h5OPEKpOvqc4M9OK2GrrODrHoiGvTNaTuCmNUGhZ6i3LyXgQdnymlbbdGLrgutMfUCuR8qYFudqYFgrQnGoONb3tTKMvVzFBclhq4gOvkzwkZD_yQ9l_V42pMpN7LnXAjTCa92ukXGRRJJf6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7537" target="_blank">📅 15:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7536">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_jc1wYCUcWmPoaqYpgJK9zIPaJUdcb2wMfGUR5TD0iLDvWFiT9Tuds6sx3VJAVmWvtzKyMOdvULrBY8xtOTBDEHlflelMlBy9BVswMUwBKrrTqi8K8SJQajvbUURg9fTCTwgZGNGbkf42XtJ2Gg1XTad3KLdt-41j5u_E4cgqBk-RX9HJSZ03rvPpn5dX3uItjU52hOIVewkRXqgBh0RUfQe0DDtTBXVWwanthxhat0Sso_Gz5Up9vx1WPWFYFxF-lW-UB4uH5_7mHLwN6fYWVjM4l1UzH_4vVxaMKAJVStuFnGAhgVBFvIFJekKl23sKkWWpDgw-WpwdkuttAAug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dbe-PrIXEbabvqfgNbq5_JirZSDBvL7BAbo6q8ovkdkYIJqmHz2JPXE_FqJt_Kg4t_uitD5m0dh5aXFz0wWA79yYI4qlQGfC2GydsIxXJoqyma4CVswrFxqyWvrq-FgZkvDIBAxqiu9YjlNlJwufst1og7hXW_-Tz3yhH7-Szxp8yMN8p64H9Gk_Kbexo3rnQtoTJoI3e7PCu_jhozbPyC4c1KPP7jKJeRC2tQ0TIkeFceAnw3FtKnUeVX0Pyei80lDRA6fzsmCFwHSPuCdKthkRJ8f5IBO8o-s2BDnjZDbaTPH6pYf5OcwUjIrqY_NS2r6DA9mh3DZaIA98q_qIPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7534">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0GbrKAF6BTXUAEnAFSgwHKlSXQ8OHlsewJlnsmU9PWzHPngcoY8gLqZoDmEYVVKK0Ay-aCpGVt9wZDVc3jKZSPGDuxzE1APZVBsTqWL88rBWl1Pb375HgVErH97XQKje2qFr5TSHvPgdbf71naKTqD8sVNlxO3SKXFxYMMjCaTA8DtxDL98FdDHCfZ8TpU9rvxCB0o8hufKl4jYL-GSrIJWupbFd10WNJpORxz2TZHwjixXqq9jxQvB4UWsXR69AfZtDipi9gHNYEJ4NoQ8_Ggb8C-jkxA56sYKBwedE7bL4DXkVUft09FO7q_4kqhIZXhKbqTo5yvunw4w7XTVyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=AseSqMVOd0TIA2sLDDrwE5NIzipW3xe_cQKCWZEDzyfGbS2ZucEDoetp8Rzcp9Pv0mHjdY9Dgy4GS5c6r-7Mp3mRbi1e3p6rS1ugsIBX3EhFi3G6dMKQ0BOgS_c8zo-60YvIYWgrHnjeftPJHSxBUrEakYqJgK8puBDxck8Bim3IKDLKimhqZeUa4wxB-V2kDMIQJQ5sRMKtWPHQapVqPox3Q0rGpHUtP54rLdBXe7rYdlS5RPIDrL-EB66dLvdTZHVparsuGw6EzqJlRYM_PUcnRXzub7Nm_5TAyqELVgfrexdNs6Jtw-ivyNGteyLX-Eb7xMrjqCXKdUDeAfBpcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=AseSqMVOd0TIA2sLDDrwE5NIzipW3xe_cQKCWZEDzyfGbS2ZucEDoetp8Rzcp9Pv0mHjdY9Dgy4GS5c6r-7Mp3mRbi1e3p6rS1ugsIBX3EhFi3G6dMKQ0BOgS_c8zo-60YvIYWgrHnjeftPJHSxBUrEakYqJgK8puBDxck8Bim3IKDLKimhqZeUa4wxB-V2kDMIQJQ5sRMKtWPHQapVqPox3Q0rGpHUtP54rLdBXe7rYdlS5RPIDrL-EB66dLvdTZHVparsuGw6EzqJlRYM_PUcnRXzub7Nm_5TAyqELVgfrexdNs6Jtw-ivyNGteyLX-Eb7xMrjqCXKdUDeAfBpcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOZ0HbapIXiFsaVenbEnU2RUbT9scfrUXvZFpR3OhAOCbWMBoTdKKRAOO2ksd2kDJJwU_eG3bmjrv8F3OI-KsXBqp2B2Jk_o13zTLrxiy6VjcXbmWbyBgsyyadw3-ZRyHCoZqAFYX7PxefXRmZotR87oBIh0APwDICvGN_9n-KeaHcAlo2fUd4qwQAscE6izazLgL8bOOTyik0OumatVhkL7Fjyu7UzLXKka-ntSv0AEdeprMeQ2CESeTV-_PkarRA2rHgelSquB-cHhj7SWj6poa08RpdRz8gYTJkTwKX-SuVxe8uA0M0_pwhN9t8ZuQ6Wtwy7MDiCtBgFDpVUOQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVDnebn4rJbYK2qJLFA3bxZ3nOwdgFw6YjE5cvnNEDcDrjl4m8xJcxFooNWjEJLyrm-ceHfiDGqK4NtcR9KQeEmbaa3PNJCZ2YZyj22z1DaoHIa_Cc4oC0c60IzgnECWtqnjudNHVQ5EG-mBAaBix6pZLFq9QlppZ69LEhZyvFgqjy7cbuB37Fga_DYlU20yk91OR40VCCQI2EThA2WyUQpxliDtnTnHcpcOUGzazCC8Qs4NDqVW4R24hnHW487hdxAgVjaK1VrIB92iLk-DFxs-OFRNsW4bgfI9rltTHpeTxVhgthGZ2_14l_jO94H1IDOVT4WTfzqhLe569dYKpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgWHhfvwsJOaHa_Qm4uaCOccgg64RhDCnhNTEw9XZLYhY4gakFGqVsNd8Yf5TzVFo9tb9yl48PFYyrRQ54-fGq14da1QCgDKei94RNTQFpUkAj2kQRdhenG_Q0cK8075f4LEyKP_Lh_ljW3LW5rUect5JDj675acrGgK7luLSAu2nLyhPZmtrKIV7pnv1AaShhi0Fu-5enaq-E9qhRStAW0B26kGowg7FR-xR4pobHkvSchHXlQVjHoCYty1nviScecWlkwhWqZToFtfilcD-XRx_1ji0E7BOJ4qY66ulWUxxu39mogKOuYzfxu3osmv9d6umzquzm4xIieESe0pog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7525" target="_blank">📅 20:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7524">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNls7vx7RYDq3x6U3pUf6eaLBE10diFMWwi1pPQ6xYNDkN8F7xbRV6Sy-P0ndonV2esR-RwAgpFXjJd7SvT9zTELs-7QFH9G-srRGJWbNdp-HeqpCCgAXYOb1rpWU3OrbJDoCyqP3D5ikrDuWetIKAuKuDH9riiw9EPWE5DzUh7mTRMunKMy-IrX6EKqfoELNZcVlroWL42GiOkj9kfjAaL9NRk6SjQPnugajM24ghfgD0MJxFBx6EdCNaEA2XPwnmxLbr048_HsvCHHaSQUHVBD5Q01cWOHy6sd_gHpabSiA0KLHKcGz52w_io9pUGfhp5NZ52FuCWsXCN3PvEPqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZbl6MV_FGA8kCW_dIkqehJbht-6Jx3-HEsUC6IVam114H9GyDigSdHq124H5NXbAu5_3XqfwmlxnsvLFr788o_YAm6IkeefPTqRgrAnWXm4bO-mA2UF-2w0yN23u3fXTsfFwEghP8slkjdSeYoQtz2WRDJBCEeMDJuyI_Q-3qIoeCFFtVQXja0J2KHdCq-8GEcYhGpaTXEPoPmqknMSlsK8vf1XOhl-im7XxAFdGz449KnSLp5sIyLhlrxK_KFqWkAgzJ0PxNM3Z1jSG2-svFV5ZPEY8QxMc2u65oSjXw4dykRMEFVsn9zJfdT1c7oYs5fsD8m4DlgxIdXLlXnbMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyQbado5KqchdTUxKrK8w--didnO7B565TFlXTMcm1A7JXe_NfkOC6UNYYTNtnInXnlae8fSD2hkAkcsCe1wv7Ep5l0okQIHJtgm2JHj3K5h0DK9HCX690gtuMa7c8IbA1JY1cP_PXBoIm06Ey6gvrXHi6HFc299q3KPwKr9qjGpoCbPUX7B5lepDLN_Z7bRMRwIPl4bmiakuxBE7A5UNkyjAJSpnmOeaAKZelQt3hP55IwnFjON0jQX2-0-0WyNH5VbTjCYaC1CuxYtztfUalqy5Rt-O11bIVwrfDrt11obHDMUiMmYndSptewwFCZuZ-o9a8IHzvqDT2MQWEWVVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdIxMFuadf8M5T-z7UFU7sGFes5YUaE0nlrA3OMVphSHZgpzbU25a_f9JsBubj5Y4jvIJBpmu7HC913Tkc4AUBghAQ3iQQFlz1vpMeduPUTjPxPupghJcuWKFhmKyUxLdNTzQZJmOxo-hU_NcqzpPK0ueZcrg1zCKfpuevXjAG23TGj-uYSeF0XXY-Z85MXNXU6mTIeEzZBpMrBTfm7D6yNWrsC9NOTi7ijNCI6wnsyNdkH7x-D2KTCYGE3XiAniyZ54Cvmaw8b2-mGZ1ZHk_lWydx7EK3OimVExMmPAi_jeb38igoJZudnfnPQ03yU7KpMSYZkKDQ8mosPEue9QXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E39v6hIK2x1OrEO_AsTYRXSH1MO5k3_nGaYSAu2FZ91M0q2kQbOoTiFJL3MUl6wnUUXsFczDHKpNQelsZUB7heb3lD677Yi2iUzg8JSoRmxcJvYxc8TYSmS8ivFWKvaHKktPE3RIrVRIOCDv-OXkq1MryQsT0K5nX5dJVsFFf-LGn4rsLY98wfzO_RuTgCwOsi9utUntCYF8RDpIFzShRPhnEEb3TwWCCJkRJwnRofqz1qemBdGb_iZpjdE5-iXjK31FEid1rqlekMlBZuilXv4aL9MjBeq0NErcyvtYZQPx3koenjWuPAF2gN70QPJB8Oudj-j0G3rfyQlBIiMshA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=ibe2WwSGYxoqjfpX4G9fHO6cCfC21ba3dkmk6bpkpjgbj50rNhJ0EQKHJVjgZ3FWTWz-urTgRWF96-UJQJEhoau_fW6hidBdIJKrV-JvSF-T72Hc2THb8wh8b1UCNnuXfm1XrvYq98ftm6KyR2HKIjrrLdxOpvCNmJxy9EaeS6XmJGjT23Osiwm9y5LhgOBQfZZyvnGm1cha-GpML0F9S2sYitIOWKPI0gjYjVRHGd0f4eGkotqNdOx8r5N54x1DeuAuQz7hPt9cFkQvrROAA9xabxQ_EHx5QiS2nIZha9vP86mbdnVbwLRdRtYsbDDZ5wgXNax-KbFPn2Gpc5LwA4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=ibe2WwSGYxoqjfpX4G9fHO6cCfC21ba3dkmk6bpkpjgbj50rNhJ0EQKHJVjgZ3FWTWz-urTgRWF96-UJQJEhoau_fW6hidBdIJKrV-JvSF-T72Hc2THb8wh8b1UCNnuXfm1XrvYq98ftm6KyR2HKIjrrLdxOpvCNmJxy9EaeS6XmJGjT23Osiwm9y5LhgOBQfZZyvnGm1cha-GpML0F9S2sYitIOWKPI0gjYjVRHGd0f4eGkotqNdOx8r5N54x1DeuAuQz7hPt9cFkQvrROAA9xabxQ_EHx5QiS2nIZha9vP86mbdnVbwLRdRtYsbDDZ5wgXNax-KbFPn2Gpc5LwA4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_QVV0rUYiVpszcwyWEHXgWvLLD3xGN8I3bfo7Q5-LZj9px4GQ3Rm1YawD1ZGTC9jowHLQXNK9OB9WUiy9f5HsO7UJTRieHslENNsCPYMftFGUYTXNMj-WzCIM2_Orlnmr0eCiWybzThI69YvBwx8L9fIcSxvjIsC3h-B14bNk5gKdt8LBKjCznrtxS1DXlghxM44-LgAMlOoMOGZniLAUEKx53olcMM6BkerFqQiska7biJC4NqrdcaRFPDqJh-MksosqQxZh_kXho__LtQ8Mr0SP-Ga27JiaTCQk952ywz1CsuJ80MCzNFnApPltH4dFRPcru--2nOw1pb7D0-Bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyOraIOnRGRF7upfERsdUHuTxB72tYPmEy9SIjUoRInKA1zRRTIYqbA3BlCBbkyxP10PP4riUSc1ob5tJyhbdbSSwzNlru3Zqy8DXGaHPcfBBjff9A3P49slaHS3EdIlMvxRLqJVhexQQ6xef_L23mded-lf1s0MoYa9c2DD0M_dHkL7q5L5RUuTrna5sOroiY6ZEun4W-NVLnDD0oL4_5kp_NHZDsguSD6Vp-zac4XhGBOam7Uj5R9XSBO1eqHmIZuvVj8aMLce-L86iov5-jK24Lyp4UwMv8nK4ETviKidmPZRT3ToIpcW8ZgMw3CKuKzEA_9bNUHw4X-7aw-i2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIbVPp-LawuPKBk2g9SS2UkcwRc0wVC7-TwP1kwpqs-OeyMuajuW0Yn8lk0F0VC6z8dbz2CddkdZ_WI0GDOSMNV_BJXLcbifYWwDgkZ2iZVN3o9m5npDp4rWuzUQogUkIlqu8n4GRvvbWz9rpHgihWrNRdnUwFxybrQggPaq7EvZ0fkgK3oD9zE_bWDlgbXRLrkni_brEV16LSb5mRUjjblpsGnAm5jJTgFKleFazsCYLXbOiG38n11YMkpsvJwYA6DTT2h_Q008HoWeWCGKMdwKfgjebfl1rbmp0_Qe4EtOFMfYnR5oJ414CQ3CbWYZn6h5SNGg8f7_JDQ4xP2AlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQ_CsDMslyt6BKgsyI52UI_QrYvbY8AcUnGiOj5xYqPG3lPT3O6ZjJvO96XV2-gcgqk21MJXG0I_MIKVeU07nXs_vOxyDuqmdjC-8o74harXw-ERqltcDYyaMjbkF-gld1QKFYSTCLHk7Sviv70Uzctlx6Yop73zX-aOBoeSEP54kMrwJlu4v4RhmmAt9PbA_25FgZW2-_jz8_DIvFLAfB-8S3OZ_RiZ3jHkGEkW3TPh97ObTz9Y0cQljLw5wWOrvUqC6hUDvpwFvJ_5--8_jAlubLGPECQ3dDY_QOd0iuzWvAnA5zq6S_kf7_y-Ru5NzOiPJ7I4RRwqMcBHvT1cbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=hM8c5BWRKY-JxgIpDzR5w9qzOgbVSGGlmtGaMrF_QfgJYZrz9zLcb-_5aUwxp4Xo_kF7o7ek91TFlgdi6yJ-gOUpwfwkG2f2sacbCq2mKrN67KFM-9WDcYlCihUS7loCWEHHKPY4Amt0X2xk_0Q_d0DTQcffKPPbYv2VoQF6R9wDk566ZZn8Q0tPDYrdZb19XdBvLz5r_Ft83H99wvf7BblIk8ANSGmWBe-C6ziaiTK1q014rkWLTM27o9NZxpi7UapchMQK-S05EAz45i7SpMJoxR0mEONDdz0K_oR05i083rWAl8kXam9Oh_vA7SY1P-GCL7E7npM_3iJo9cu9MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=hM8c5BWRKY-JxgIpDzR5w9qzOgbVSGGlmtGaMrF_QfgJYZrz9zLcb-_5aUwxp4Xo_kF7o7ek91TFlgdi6yJ-gOUpwfwkG2f2sacbCq2mKrN67KFM-9WDcYlCihUS7loCWEHHKPY4Amt0X2xk_0Q_d0DTQcffKPPbYv2VoQF6R9wDk566ZZn8Q0tPDYrdZb19XdBvLz5r_Ft83H99wvf7BblIk8ANSGmWBe-C6ziaiTK1q014rkWLTM27o9NZxpi7UapchMQK-S05EAz45i7SpMJoxR0mEONDdz0K_oR05i083rWAl8kXam9Oh_vA7SY1P-GCL7E7npM_3iJo9cu9MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7500" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7499">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHF2mhe2Kex5CgTMgZibPjHYIMvUrU6yqlnyLtbXZx9Ko_d61VT_bvASlC3loJBMQFxBMABRkUM6oZKh3JDwvcXS-uyyt1PFAJJvVEk16fMF_abziCrc6M6gt2BG2FxVw9YyScnmsVXd7ff8rdU2IMOgPROxcEzvpxKP-9-E3Dyr-krBZWXsBAmk4VGwTyuvALwYnr7Bg7TlO9KF76QnBaoIN-OS2Zt0DoiiNtUY-vJVsyUM1bhX80m735rsFJBw-_RZcULu6BDr2hziPhigpJz1j9q_fubAuX2AJNoEtilAMNxE6GQTqrnSDs6ZMdP9h0ShV9GdN_kstNKEpIrChw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=X28O_ZTOkOTPQkSZfjZzan6cK55ATKl5AUGLbycSb7UZaoClus3Nx1DEnhOwRyKLGkiwBZZmSkilhTOjeOIL-wlEaS_RzwBlnzVAehz_CeK-n5sfiWPh4UeZECBAjo6mJUAdrFxrv2ZUbRfT_5GgYakhQyztq6sEKIxIdk5UpkTdlscvB3reeRbS7XdR52ZuK_zl_sETfHVZiKPOfgrtICGcpjyVwvdtkD76KpWprkV-muV1Rhnw2E8nfNDOX0EPHFbxHLMaZXK3ilY4dNeGBSS2AUboJfxz-SIrNm4GZamSUA0iMMa36GipOyyEYV3r1Kun0Rk30dtA0agxQ7EpuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=X28O_ZTOkOTPQkSZfjZzan6cK55ATKl5AUGLbycSb7UZaoClus3Nx1DEnhOwRyKLGkiwBZZmSkilhTOjeOIL-wlEaS_RzwBlnzVAehz_CeK-n5sfiWPh4UeZECBAjo6mJUAdrFxrv2ZUbRfT_5GgYakhQyztq6sEKIxIdk5UpkTdlscvB3reeRbS7XdR52ZuK_zl_sETfHVZiKPOfgrtICGcpjyVwvdtkD76KpWprkV-muV1Rhnw2E8nfNDOX0EPHFbxHLMaZXK3ilY4dNeGBSS2AUboJfxz-SIrNm4GZamSUA0iMMa36GipOyyEYV3r1Kun0Rk30dtA0agxQ7EpuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7498" target="_blank">📅 22:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7497">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCiGdIt1hBgsmrGeeihZcNXi9SB6q47iI6R-k0s7jWOSyi5-DmYH1BAOVYforvg_7VwzPmKIYxMlDPIaR78uSHor0okCuNkNKIzMOJ2D4OgdYP_EHlaD0FstARamXwSp_QA9etzW-nuaw5Fim8UDJDo8BB0CBjL-w6BjuJWiA7IZ85wtU0_n1hScV0PzSK9GkFePUuvEA65RkJk1Y0Twi1qgvluBmUobnonFwHjHv21fr2F6TzU6JE5dwzwyZ3tD0jL2k9EAYWK_m0M5XS0gpqEhG2MIbRVZG8TRJbmlLu8jYrJuriywAP9lvfi9ytrd_eyYSJP8uZAdLE0iuxPyEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNgLaV3RGhL9zmktM42lQy_AL_fkHcCijM5wXmVZALtToMSiaRkW13PNScnKsn-H0NGUTovmIuEdZsSnxKNkpSbNeLtLmB8ugHCmDdpAV71z7lfP-wJW-5_b0pVlg6EN4M6CDQ7IW3ZCci7ZcTZ8EdbyK5SP9RtzGK-GioUMAXIrXcuFTMnKaajrS0yKCCweya4lHIdrpGsd7Qltou4a0QntvJ6_KgsU9xhJE9mIoriG_A_HxmooQcBOrzGYakJ9XtvT3FK3VWhZJ_If4a5Nsy8X85MzdvivomBr6FCLOCy448MA4ptQ4dKETv-QIclOGf1RSEc2PB_77SQzvwREJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=I9sLMo9jVjKwjxpWEeMOsJX0IIHfnejHOw4bT_LbwkMW4nSnafv-RS7xkdkWbXsNwT2ph6vytirsm3HMXV6JsSHpencHG4VdAAhe_1EIJ8Z8gKun82tmtlhfREGgGdTib8lMk2WyudTnMlsn8S2-lbDzbP31n9FT1XSv37zBYlkhtB6Rpo8B56LhEyBwuRerfAgGgi5v1I436AnxMqP-7BclV_XY1Al8Z8NkX6zMh1pknxKcEt3LPQuYVqufLFC8Cv-J4KIwSRo66SxyS2e5Ix5v9_awG6XuJysQy3oSh137zfKfMFJYh2zbVis87zYK3DrOKBuuqAbxnSlGwF5aJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=I9sLMo9jVjKwjxpWEeMOsJX0IIHfnejHOw4bT_LbwkMW4nSnafv-RS7xkdkWbXsNwT2ph6vytirsm3HMXV6JsSHpencHG4VdAAhe_1EIJ8Z8gKun82tmtlhfREGgGdTib8lMk2WyudTnMlsn8S2-lbDzbP31n9FT1XSv37zBYlkhtB6Rpo8B56LhEyBwuRerfAgGgi5v1I436AnxMqP-7BclV_XY1Al8Z8NkX6zMh1pknxKcEt3LPQuYVqufLFC8Cv-J4KIwSRo66SxyS2e5Ix5v9_awG6XuJysQy3oSh137zfKfMFJYh2zbVis87zYK3DrOKBuuqAbxnSlGwF5aJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7495" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7494">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZokQ4bqsChZxUQzR--CNefWkrvmIaZRabvAj2U5RZ6YbSQUDGcLCC4VoCiMLe6O0YxkWv7cYFT-9sR_LBWhOllqnDI6fDdAbN1YdSjDGClGqnXQIs3EldBv1OO5-jyPG4h1oiRRr9dIS34S4L0mLyjXtQ84HZ49EvS9AsA62evX2plC-nZXHTthRn3Inq7Ns9URasYV8JAA93n1J3W5vhTTs4LD_YJ4yOm2oRH1NOin8QvvdsRC2OE6WUmXXvIwUh_Ne3958m7JKsOPhbgxrOvn7kf-j0iVGElcR9eupy1rdquwUAmYj97jonY3jGnN8NoJN6gJ_3DpEbG3x52EKJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWl8GHdcTriRa4Snmj30KfCaUuEjs6zz5FjqXZjeOimaHHnlzCH9c0MQrGI4J3ev2m7O8-5VDXdGyzARrsKLlqZk-FzVWFRbjjolXVcOzQTRvMgxL8jVWQdPyc05aeQySDNJHdXGEwvvtXdZRO410u1VbI_7eoabCtv6ZuuH3AB_ztNdiHWUtyLcmw68mERywPi87QZPXPYNfiDucPkosY-xBtHBidUOVtrSxdXLBXOxks5FfnNMSg_q-e5PwBSEACTDlsIMb7qFnOvdWh3Gslia1r6uiA7SeyNtptwwO11xDKEoXFLzm6wYXTgJNpCsySRQMJ-r13nFoh12WKcE-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=c4VyGrZHxUU2JOfPxndNF2oDinSmtPXJ8LdHkN-5yc2C3MWNZzrXXN70XNulMFGD0BhJ5_MswDkeJ0FObi-W2Jo9l4Ro2KTvcx718oE7tdO8akc8Jj7uNRoJ2QX0RmRnUUTIZb3tgFxB38Qwq3YLGWx142XF6U1UTKW5aDf4FHxOpta2CLUZ1EuG8obs8ge_q0zv1R6qXugsAfBmZOB1NfOPOKBdSx9SKyFWVQnUpsLDyNrPnaMICpbtrNLR81RbKugBBrzaOg0kg3zdhoCdI57ZjZRKot3qn5YQozdaQY2ApMoEHeh1isj8f9kyXZ3ww6AhKsxGAk6XLdh1YsHOZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=c4VyGrZHxUU2JOfPxndNF2oDinSmtPXJ8LdHkN-5yc2C3MWNZzrXXN70XNulMFGD0BhJ5_MswDkeJ0FObi-W2Jo9l4Ro2KTvcx718oE7tdO8akc8Jj7uNRoJ2QX0RmRnUUTIZb3tgFxB38Qwq3YLGWx142XF6U1UTKW5aDf4FHxOpta2CLUZ1EuG8obs8ge_q0zv1R6qXugsAfBmZOB1NfOPOKBdSx9SKyFWVQnUpsLDyNrPnaMICpbtrNLR81RbKugBBrzaOg0kg3zdhoCdI57ZjZRKot3qn5YQozdaQY2ApMoEHeh1isj8f9kyXZ3ww6AhKsxGAk6XLdh1YsHOZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSviWnpqu-FdCdmAHNnJuBF6BYYhgkPeZQbM7fnVtYlcCBO5mZOiEN_Pf8oBJdJbYyabNKu38IaPp_ME8nKfZWS5x8XG2o8Tw0Y6tx-0QVQCkOYjmnwo3YIdCD_mIvp0krx1mDt2iA-Ksh78NstlwBWgk--ZuQRWm2oIb6KkEZPBZ_59RM4BaM8YZeq6DYcwAiltMZ-pfx-02E5nAPCtdkzNipoMdmvccSqLCu6CO0HClr32i3Q4Qylwuz-IL0_GOntcEBcxMg_VA01KyqKzDzPf6QYIEp9V7rAKiMgI5RMMgtmq4dih1UJwWVrYkf6HqUDuA_Rw7fk_x1-M0wKPKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7491" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
