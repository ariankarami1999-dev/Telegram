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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 01:51:16</div>
<hr>

<div class="tg-post" id="msg-7618">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGEMION | مرجع خدمات مجازی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrOSEeBjMf2WGOcSVIXM6XRWwfgsB9y7miPTx5Ex5ojFdz9eJquWdGyiwWMKw8_SyLtzxq--tDUM6oz79YSGeCVKeKDypTvQpVq8SceMRNRAlphHDgWGgPQhJwOljEEB27KFkprIiZ-oxanVgzpruMw4GS5DBhZ3x46vD5SdXucs32zq1gNAByx3REnzdm_rOHNy4oXscGdWmmgrCrnXxRwghAMpHMtLzi7maYEfCv03tw2bSlSOB_cmqoU94zweCSwZ4ltqwZ2q0bM78HuwTnCy68RvXqf-eTfjtTH5mNzdVSMDLsYZJN56e5Ag9XIUQXFtyrX7KauKbvdpiJAa7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی که تو دنیای دیجیتال لازم داری، جمیون کنارتــــه
😄
پـریمیــوم،اسـتـارز، ارز، گیــفت و خدمــات مجازی؛ هــمه با هــم در جمیون
⭐
🤖
☝️
@Gemion_bot</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/ArchiveTell/7618" target="_blank">📅 21:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7617">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 778 · <a href="https://t.me/ArchiveTell/7617" target="_blank">📅 21:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7616">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اکثر شبکه های عصبی جهان علی الخصوص chatgpt از کار افتادند و فعلا دلیل اون مشخص نیست
❕
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/ArchiveTell/7616" target="_blank">📅 20:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqZGb8ybNlGTvmgAfVX221sL63l7co1Hkjs4OYIa8yuHe0ONrtMud8r4maRdQN2rcpxoXpVQG1oxW4snbY63jsJiFGLdc8w9Xi8eoQlR9dbFamAgECN8Z3FnYcqr-Vn8oydeI0YwRmUC70cszVa5cc8OuPG1E036LePFuTaAO8z-WY-EyDv6z3cYY-73yxGwcXAJx0ElRn1DOTwOtRwwsb_fPXQYhwdFJsi9etH7LwaNq54kTzQwHDy17yaL-hLC1UGV6O63yEcHaDDGB3P9boravbohG4NWK7uPopdpm1fpJLGxjEnss2_MZFUEPqst522s_F3xRFdwxlLa0NSJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7607">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7607" target="_blank">📅 22:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7606">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7606" target="_blank">📅 22:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReSK4GXMbnY15-bGKOYfUPnaxSKCBHZXoypw0T1H5l5aB-KkYm2ATkmodLmpfd9Ktw0UAW-KUGSUXIvd3P1BmQCW4lwwNaWBly_lsjtEr8g2csUS12OPEnFYpp5RCwY-6_5T7BGXD36Di1QPVSZnrIw9HnAoYY7eeS2jeuPMCCxn3j4Ih42-ij4s8xUiaKqjQ5mMQNSvZbPxgVQnGjA-RzTSmtl49AWdQ7tiFiscFTiZm4BLTClL-FD2Db4Wa10ThV6HEGolMsn1QvczM2m2DdLx_CUK5P6ngY8tPJ9SH_MnwI-xy7HIDNY6mBa8dZJq3CbbBtN8F0sMqbcQTrNIqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYU6x0rLjfLC1MpW2NPGnrJwnt801H-tJ27WIxqcf1TruQXTMbfpkb8nwaLiqugN3KH8xGiTzjitvGBvCVnsCDFzqDLFWnIuTN-T_8c2n87S6zZgCjBlAlQfu_FmsfAnRzYEbjhuMvWrOcKI-YZLPSP7Q8iNGtuzbMcNvQtuet14QFptAv7a1RakX7EE0-WkUr9CutrIt08qnN4J9gty7H6dJVl9Ajvjt7IkRWgbYEubcTKy5v_lWBNSFfnI707o6sGR543oguBj1Z9J7M6N9e2B0Notkc_myzhPkA_2OttWT4Downdh4oMdg82NM3pYFvqzJRiIx-6Ldksxu4frcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0jesaDD-GdXVxpjIBTEG8rCf4Wqw-amPynkg0pyKa7g7SWbYjY3GWo-OCZ6Zc8-M5Q1X5SOY5IzyT4Z_Xo0ErqYTao06aL2RSCSxgVcDFtXbFApdsZZT9jY9e3AEI95dwmh4L6dx1b_5MCQzqbGZqozvNedgLeSiWQkNKV_XwUXZhtkvwPphgpjueICcTIXF9TqO9P7P2tW7h-J0r-r-Wa3lRzMEgCpPAQbUrP9Ztrz_6-kckv6FJ7hbJXue7qlSCSlD-cVALpFBYr1ACwMQKDE4ptNhMY1yu_QklbnG8ESPpFLR0MPPhzDR-ijxYDec8PlEVjJG07RSFnSrQnbFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBko2_DyU8ETb2f_A5q7SyasEmQ0e71SxZ3P7i3B8ssvtbet4PpIp9dOe5eu_s9s8dUUe1O6Dz1ztz3qV6hhG-oT390l_ieHP3OEbqhGE2RdDOG8R71IZw8B0G8Qqq-R8HoYfIg8fCHtff7tVAsyi85qaOzrA985pz5FJuwAMzwJWFjlmPOrpnH82TGGQUOmET0yp_23ctNgytLFjfGEcEUoX7blPeSF9xV_ZTi4xUfiEWGwhp2HT8fhgXvN1p7THxW-tdfrmoeH3R0-Ey6irIWNHTra_GHrLwlrzzt8BJdH7h-zOyPxckLQdQFmwj9qKU_2B4H_AuW0DOitTR2OXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leZqcQzs6HRjfn2JVF8yaJHSnKwI0kS3QJQ1Udfk_hgmHMJx_r0x5lqLJ1hrl1RdwjILj2tShZ3w5b-sXQ7YsXjLY5bl1goOCw-H5bxv3sPNLGVjpDf8yoyqbsOkIJ0Oa0DElmzCv6xxMO4v7fq708LBG7HfjLtrJDR6UqXIvMaD3iCoBnkXstKYcfC41-sN63l5hns_YbZfGFSO4NuZfKuXguiJLGk5zt4pEdZX0zvQwJ4UofYi4kEKpxZNG_dKoCJmFJUmTR19zXHGdDFknZmWG8tZo9ELo5TCshc4zmb4cdlWlPv7P2goZbkCy-QAeqCX9wbs9KiAfvGGHKKEaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7YbgMOCdd0DmvqUPfr2mFgKwwNKyXVCXkONjycRoExDa62BUD_bgM5MCk2PwJMNfoJnMvRa3r3wbTOoa-7He-RfQT98HlStsk21wLSxDWQzEgSxDAN8xANOwBD4catHRC_HZ-NAVzEKecGXvpnMXLI6cCQC2YWpM5D3pnXfsXaa00vScYfCefmUPR5hgjtzyvC4KFudy38jDyz9lWMe0MIdhFV94e_rMG9pVo9V8FkWyo9oCOrw5hWfYb6nJwf2JvZJVmjB8L4ODBgnipIYcwgN8v15rVLQSZP7ZLRQ9uWJUOHGALLSDKXZWHR3a4oUO3oPADrgOOA3UkWPBGb1kQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hi48eHyrfH9QY0s21WPkQQXYTHbpo26firNdF5u7PVivCRO4lInYyXngZVItJG28okEC36SpANvj-my4UhAcLu6F8phh8374RaAU6WOR0TjBppB1WaTyeSklQ0zveTPwSWy8SLO98cufhjYV1gKAXJA-KpIRcKIA5qdJybBySoUxxQ5b32YqoJDxCwQleSclT39HAILbg0v0L97ZpO4R4LFJtn1AG-3ZXZ3NB1IpW_Kf1NeckJYhZajMNDLCMboco1unhNDrT-FdYseegrJQ4K2IRg8x53QXmk4pT7jaP1saQP2cmFm98abgLHZPSoA8WsobcoFfRB0jDHChti8TmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCyXkFX_wCEGK5QK1ePn8IWjPmqfxkJlLV2nStKyalSAag4Y-_3ejlErlaYoljTO4kvtUzV-4QzA5AmjOPmgvBr7Dmp67wayVcEQcmVoNZQ3tQ3GPu5HQnV3hgTbQdjY1VXBz-0wcYqx6sbVB5SvmWTVr-5nZnhtJMmrJNXn7PDwpy0I1oFQlcLjorcSGTnSaUFO_TSLahgl39BQ8Z0G75X7FjjECkcG5sSoxepDShc7Lgy9sLEln5njBqxZVOOb0IaH6MUoL95xitQZgg53InCDoIViDlXDoVxsqZ_7l2wNP41z4u9ut2yna9w5KnE8Jh_8-hpCc_RE94F5kv2b5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFUoMHcNnAPv_o3K_nFb0WUsmOhv2HaNYtD6KH6WHzNOgxLEQY_F0nnYFIDH_lYWjG1l2nOf2uUTNF2Lft_jcDGuVzvYxSJ6zgZ6TJ-cE4QZcF7IEqIPPDLZ3i8oQ43it-koJo8Bw_xGAGaSEz0_NsaQUj_VuGyOdWkHDZYVvooW1jHNq8PNF7y7vykauoOduNYhciMDtztkw93TdTBBGgaIpzFyjbaSIkc3yKkoDg5Z-ArHHPqYOaMYIyOxAAXhewg58wSJgfetc44sXqu1U6jQzhCe24efeYDoUnGcadi9kzhI7Sg0QbhvzIe8hQKkWZ9XojzS2R582nxzY7f5Xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6HsRjLj6okGhwJiSvj-PutkZND1zHGWRFC5-AbtV5eZ1dbXzD1wqVcgZIe1o_TmVDAB1pNfxwT5aUvqGGUe7X6yGU6EKJLIOp1ltSUA22vx3i5xxteHaPep2GSwEt3dFh2e5-UYoz-yljVuC0W0YRFNeXJd9r4kKNo6LtR4CyqhXV7NG1iXvnnwncC1GG2C_bYuqOJVEr_gH5A8zuOluyEiqkeRuM_DvBJFfpL1ubh_KyX7OKKp0VJoke4OtaXeEZtgCUteRyD1IwsgTZWGI1uqlnW7NJWUGYZPfM0edREeW_-lJwSLKSbs6fIVnZPqvpScFjLcSF9VzcVrXA-uKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=XOfj5PtCkzF8cq59wBuouQXFUm3y3Jamwo_US01voKq8Vn7bZ8ccBHXggC-pEQELp7qqevuSPI2pJob8UsXMh-WSq23OGN1cvAGh4jTzqfXBD9ddyyTgNYJfHOB9UDa4YrwEnhsWFN0bUV7Wg7jF-nxj6p4euooVp29HYob_nVU613oepiQYT1SERIIUPk1JCVuzlSLxd5EiYPOq4J0PUOKwsAQfXSgFct5uj0VXrNiB3UftqRVZ0n_5gsKt29k5kSpRZMwQlqIJsYZXN3b35tfyHi4lgRmZUarpTPFe4DYyJh8R4hQuI9BgWhMRPFrDo_C6PfkdWW7_bB0QIgMapg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=XOfj5PtCkzF8cq59wBuouQXFUm3y3Jamwo_US01voKq8Vn7bZ8ccBHXggC-pEQELp7qqevuSPI2pJob8UsXMh-WSq23OGN1cvAGh4jTzqfXBD9ddyyTgNYJfHOB9UDa4YrwEnhsWFN0bUV7Wg7jF-nxj6p4euooVp29HYob_nVU613oepiQYT1SERIIUPk1JCVuzlSLxd5EiYPOq4J0PUOKwsAQfXSgFct5uj0VXrNiB3UftqRVZ0n_5gsKt29k5kSpRZMwQlqIJsYZXN3b35tfyHi4lgRmZUarpTPFe4DYyJh8R4hQuI9BgWhMRPFrDo_C6PfkdWW7_bB0QIgMapg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-KfzHh9R6w7SldUjFiFjBI2Cr9bMUDiDdbfv5AEcEnQeC_RH99T06bno52Dp9djmE-UU4QQcrTgJck48-R356xuIAYoqrIx7xyIPLrB9jMbZCKMl_TysqL2qwXegAskpV6JDLgbMMzhYwjWOlzBGqBK0TiZWtdTf-xO92ai39v0DBIrnUg1ViDcbaywkJd9CAzo-q0WW2ohZ1mfbLHfN5q1MK0-3IuanUPHIY6QA2fzTMhBkH6wVjPfMIPHKTHQ525DO2IHl8ctjrciMcLf51V8UtqQK6dZd6iJZKTfYiASOrNkM_g_gLMrD7AST99I5f76bEBMDHRByZQ_zie0gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=OAy0cQ18cAzEHr7aC2P26-6Na6gp-Gocos2-oO9K1WJr-3v8jBtvPPg9hQFRMLCSs-5I1IORL9IZHs2DsA8Df2Q7-NJppkQa_mf7_gJ4hMhbbMPkXoPHywQqJToZ5D52TC_MNkbTe3FkLl9LOtKSkJ_MQmmsHPU0iWDaEipVBSlNL4p8sMKgyKiOoStTg8B0F4qTCn5RjLhi90r67-32_qNU5J6Bw2HPcbG0otOzu5YH3lhZZvwgbVV2Y6MS7DfbMltKPIQhLACLWzspF6g9YhtdZD1hXUOqcsBxtsDq9HgJ61kSvSOyJJxFixS2ISc648bXWQw9MNHeQ5fWqDfxLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=OAy0cQ18cAzEHr7aC2P26-6Na6gp-Gocos2-oO9K1WJr-3v8jBtvPPg9hQFRMLCSs-5I1IORL9IZHs2DsA8Df2Q7-NJppkQa_mf7_gJ4hMhbbMPkXoPHywQqJToZ5D52TC_MNkbTe3FkLl9LOtKSkJ_MQmmsHPU0iWDaEipVBSlNL4p8sMKgyKiOoStTg8B0F4qTCn5RjLhi90r67-32_qNU5J6Bw2HPcbG0otOzu5YH3lhZZvwgbVV2Y6MS7DfbMltKPIQhLACLWzspF6g9YhtdZD1hXUOqcsBxtsDq9HgJ61kSvSOyJJxFixS2ISc648bXWQw9MNHeQ5fWqDfxLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gccVkpt7cirIZydeJnW30mk7pYpxpAEj5zaltW4PVQM4MvommHNUj270q16OhBG5gQEIBaM1kWkQS4dXgPmdGzwbvGG2Gs-QO8MbWp1dAEUz3sS2QfblZsTcdzJvA1fPN9dRCjiHfyzCSPBUl_va3cMTJyY6ibcgBrukNLZrRaqpgmYtvwq_PhDbyS9IADxBZsW5TehSCltdS66BRSVUl_6k_6ggIXuVRSkh_-o2XUinRzSbzhQhGoMtAC8h_YXjm-QOiZzp5btcSub87fVt9NiDtLfhoQXNfURb9Xhp3dGR1zblSuLq_SdqkThYTDsSp1LDw27spWv2lGj7ntGoeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hXPyPQ_bGszwecb_TZRIApbELYJlD7l2JxRVHSDOOdyCuSwvAg42DXOG3GAyfvREd0uAZubf6JnDhW3n94akpRdmuDwahdRc-KpYs8WWkP0PyiWL3rwLUyaIWAhn46Q8_E4rVQrri3JAn0y_myGBg52h4yDaRAE7s82Ch0mJWzR8qTD2ndg3RKuTMPcWM7JHSVWIWNW376kuizIzajM4v09M1rJ36OfWdWKqlJ0AXJWcVxf6vTRehOpfBqNwHdHDU2MkgTaB3FnUIvTXm8vg6l37yTAFbb3I9jkNeP-pE0EczJevE7My9qHu4ee4EoXiFi3T6cbseC2yET2bVdXdDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PhhvoLxY6ChQwffg4hpTpLyj9X4-N0tk-f8QzmJ0CYhAHEQlxzaHO32wyQiusbc14CkzSwqUyxlj_6WJFhMfmrSV_QQPVKptuEdwWmmQMqCzeOKbuoWF_95Sq6MpUbls-3-Bc3qLKbHIAEYMpMZmohGPbRbygEcVSpeYWqYLCZJanRWL2ExiMmFWe6IOXIVtjB1kDkmI4XV1WrjAinPap5dqwafndwCSEeOoQqK0-vHZAuUxKYmawlf2TPp_o7VsLlDbCdTx4QJxRvO5r46cqvEi3L1MEQrlg014UhywlP09UwDsyyY_WF433OIZY9OPhsVvnuGXHTImWEFn5_EBKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcEi2ejbhsNYLsQHVZHvpiRirWPUFXtcilh_IYx8-Hks4zSb2ooasroZ5VUXLCTf0tVwZAD4Oj_57uHhhYYl6tHNme6d_kUKAECyLWH_oJ-2d4PqxIoP7Xkkgk-8NGxWJTWRZlYEKLs8jP8LdeDyhIw-FX4C1JtDT2K3dz7Uxjt8OBj3l-PTNKUiQHd3NjwtMy-mHN2Nh44acfjGTU6JKHcJ3eiKsY2LfDNJ6-XznK9wDugk90RCXiIolMP0NnxgR0HaW2P2iVLNpQsXbu1M7sSZm5wL1wO0QSfVFnPZ7eEsNKX3PLBfefibKQnmbYiDoQ8FwgeqlE2Iy72eDlIzOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IAgEqgF_sTCSsPRfR078cmmKJXYT4bJkSbRk32SSTG1XZrE8KTD0jZO-KHZ7tV3S8Dl096E28RqghoAz5WpenazMu15P5Jlp3RqpdmvRFXJ8ECXU-LtB8c4pKOD8IBsn_2kMJjChdcPC8AVtRQhiuVXtp2og1UmV2ozU_03zYG0tfqH1g53WFXHI28WwZAFZqrn0TlIsdimJDzgJwM7-Yh8oBXhpF4IzR3Kd9qdsQJQEV6txsJkAanrQ9fiooq2_h4TPtBGcgiQLjF7nYk0MN40ryNZDEY0sEY_s_SO5ze5EDAY96FvsR56yVxSQF3Emh4evmEp8gd0d6riBZEAwtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tx3oIkNy1SijYdOFufK2sDrYLa2qSozlGlC06fC5dH0sB5sAjERUC3DG80HreV061oevLSEc0QXhSgtpfgBCN7NhYIOln0GZ8wOtb_4uuEAhsOEnM-E0Gzx_x0ywgDt6is_JkuGHnnPkJZrCCBNVXzC0nFL0tzVBPGcxXkOTZPlf1V4x5MPGrtGWBckCrVBQ-q9JgQBrhIhpYICIvzlkOKCr2k_Wp3ebHNGFI00_B3lQQZPNTr2K1OaErvl-jp-2RdLe-iw1AT1AhWvenBmzVWaPZGagMHawDrMaAEhrkDBizuQQMFIlAzCV-WEvi7umUu7zkmVzQMx8ZJ_fkbxQQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z01IhJ4vKugcyp1t7b-528XYe7gnNdahEQl1mgpOiEJHyG-IzpsexQZeBMk44kRNP62YwB_w2Tb8yBfelqwosprpOYbpGRrYMcetQ90Eae4mwsTZ21h5QUr5VOr1M2rInWbwy3xzBRn40upF5x5zsdmIeyORHxlVNZuyb9eNEVKYBDRffOzB3-y9uyHFF8U-1dUH34FAds5WvtTdd0fPFW315lh4tQY8TR2ADJ2qA8Qe_GTWn8vaNn3DL_DlaKeJKO7OiUI05rDoXorEK0fw9VC8leZPnJ8OYhjK6OOB2bBg0lMVJsmyvyefG_jee71ex0K5MFggdlEgPm8e8KthJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_VK0_--FSpUG1ri_tmDc4qj2dQZfjDLhUB2BoIywza7qc7k0olFr0IhzKRs8uqES5qXICCpZbvvXNT2ySnLjdt4CmWMJKOxq1siKLxHTVq-yFmmvkAwyk8nb8Ly_6qDcinFVyer9V899SRGrJN_bJBfWsEys8IB41dKPWOmIYbITXnnwW3qb9SCBc860fhuF2FoyvCH7Ek-xFpx4nJIz64LJdvSIoIwz6TnioVYbeR8blZobKHD2ZoaNLWaDeZ_0iaB4uBkbjifCeK2rFwgTx0fj8oB9lFXPc2YhARl4ZQpJrytfLlLDNAghiKl5FMNK_UHxMI4_qYGfswjSIq2VA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbWmKdLyOtfioOq0Ar47QwVSqxvUoAWZXB_Kczm3P25J9DnaGWEw4_LsKz83T8Jbs7c7VwEUiCA7OMZ3co9IEOuHI2Itkj_n-YlHhhuHOW9je_sy_PgneC_KSKiYa4tVz_Uzc1rG-sxaXXdaUBDV9-r0zMcpvbWqLnue3kDoo-YwcoA8LHmKx48B3kSzyDrLuDPZuHkpKOKFuosQ4Q5K3yIIijoAufgJwnlJPqu7fwLAhie3oqnwfEmfmH9Z1QMnxeeAGdBeAKC-vYvrl4kY0E0ZT1NVf2iBye8Y3pKL5fQXrW6Jt7ase0ouWYbzKMZEfWa2nIBzbRE_rBAepx7n-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=DsCq1DW_vzlnEYEkZwfh8MOuiv5Xd6Cw7qut1pQArM9vRZb9EtaJW-9h-1Br-etQ4X1HucXm5gr2rPP3WglblvV4vNogl43Ad2EO8N9aIQoyAzuS-YZU5CFVZiC_HtAOJ02erQpWidTm-9mWFSfECXkaGHQgGcciq9XlZWPevOMctb3EuER2c54xMxgVAoQ6tLnfABOJ8ZKw-uFoEYDJFm7Mo-KdD9R1OBJlD_tO_JZC0Kx8GRysqZshDUulVyQE2xU0GZ2UspCGcG8hVK0Zh4T-ddzXQv5XfSksL2Uzsba423d3W5uHMJYVG8pp143pW4uQv8skupbbs2OH5y5jTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=DsCq1DW_vzlnEYEkZwfh8MOuiv5Xd6Cw7qut1pQArM9vRZb9EtaJW-9h-1Br-etQ4X1HucXm5gr2rPP3WglblvV4vNogl43Ad2EO8N9aIQoyAzuS-YZU5CFVZiC_HtAOJ02erQpWidTm-9mWFSfECXkaGHQgGcciq9XlZWPevOMctb3EuER2c54xMxgVAoQ6tLnfABOJ8ZKw-uFoEYDJFm7Mo-KdD9R1OBJlD_tO_JZC0Kx8GRysqZshDUulVyQE2xU0GZ2UspCGcG8hVK0Zh4T-ddzXQv5XfSksL2Uzsba423d3W5uHMJYVG8pp143pW4uQv8skupbbs2OH5y5jTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9TeuVq2zDBLui_o5DtWJCVvSslz8vPnIeTIkUmnhzwfZE0ORnzXtrm0mUAttQeWWztlccZEc-hh-KQQk7C4EhrLZufyfKdYjTEl_b8M0Qy-EsjiyxYh9YPDZ2HsAWXXMvpspDqs6xFERPwIYZV3V6KgvHAP1iARmHMXmW9zTEVQ4yGKT3T7QNa23jXETV7TpVBmfSaC7p5Xt3SvHJ4wBwDuZjdmB8oZA0qktI6XB2bBHVkKZ3S9tf0pCETAJdwMLG9yKvzM9o88u5HBKF-eJYkZWhto-cFetuE7os2GHCRwudHZQ7PCz72hJgQSUwmu4JtAb-KKD4mCxICvqH-gRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=FhHT9D3pDWntTA5SUUeo85uhhTRHiZkFP4olAje2HRfX1Z579ZjCnI9WH5lm8zmk_MyKgHJNfZnUX10m3ssFbTrfhnVWBD9Ow_GZA6TeHVWMBzUkbYyk9TaxWgZJu2bhseloILw95klHBre9wXXbkr1AAVSRjkpKjCWplMIVeR0IFkVPKaH3O0pZUXhP33otCO0_L6esgmCW03tZTOl4YHZzN6TKOK34Ct17F--VadnRJUMqAqRoOpiHmqYKTw1zGwi8poc7Tlk7wdQiNt7LCyg6o7-f0PzQZ4L7Qs8fhI0QrkxtY3aZyTQa9NNRU2vKQlOCG8sXOus6cW7R4PV9QwfhN9yxbVbeZ4Hhu7ai5QEOc4TZH2odJO8nTWvgv-yeoKnIek_J5c2PauDKtSvi5TePOetjjrHMLW6IwtNZKVoVA4NgyeGgY2sOoqXGURqZ0AgswjLm8Qml4ga-SzlI7V3MJn1kgWNnFIxrrge55KCDCFSxHisSdkvQ0QBIov9Hl50dlfsdBn3WbFz_5wifudkbT6ircJLf08-HU9vt-fcMzFRD9lULlvb0GB48Mo4aAPms6uer7qUFm0cTxFdwM9UsQ343MEdhTw5ZgTSBbZAZzhDgvODMXkid9S0dBFVxlxOynu3dLhNeiq8Bfwqu3_LQ34jJcLQduaGEuVvQPSo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=FhHT9D3pDWntTA5SUUeo85uhhTRHiZkFP4olAje2HRfX1Z579ZjCnI9WH5lm8zmk_MyKgHJNfZnUX10m3ssFbTrfhnVWBD9Ow_GZA6TeHVWMBzUkbYyk9TaxWgZJu2bhseloILw95klHBre9wXXbkr1AAVSRjkpKjCWplMIVeR0IFkVPKaH3O0pZUXhP33otCO0_L6esgmCW03tZTOl4YHZzN6TKOK34Ct17F--VadnRJUMqAqRoOpiHmqYKTw1zGwi8poc7Tlk7wdQiNt7LCyg6o7-f0PzQZ4L7Qs8fhI0QrkxtY3aZyTQa9NNRU2vKQlOCG8sXOus6cW7R4PV9QwfhN9yxbVbeZ4Hhu7ai5QEOc4TZH2odJO8nTWvgv-yeoKnIek_J5c2PauDKtSvi5TePOetjjrHMLW6IwtNZKVoVA4NgyeGgY2sOoqXGURqZ0AgswjLm8Qml4ga-SzlI7V3MJn1kgWNnFIxrrge55KCDCFSxHisSdkvQ0QBIov9Hl50dlfsdBn3WbFz_5wifudkbT6ircJLf08-HU9vt-fcMzFRD9lULlvb0GB48Mo4aAPms6uer7qUFm0cTxFdwM9UsQ343MEdhTw5ZgTSBbZAZzhDgvODMXkid9S0dBFVxlxOynu3dLhNeiq8Bfwqu3_LQ34jJcLQduaGEuVvQPSo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pek7l4kM9opCp7jv4uaTxANc633xrSmH0VtuI4h0E2Eod-VXMuRsIXUmJvQmhT-LykecBMIBbAW-8uLuDWHrl8yBiwkZMAq7TQ8vSvWwGoRwviTHS3GcI2mHknbSvjKpiJrBCT44oziDB2zkUTaPeaEY56iCUs9PrPgXJCmAFqi-BM5npbKJWSjBiTThOTeU6hvjnz0usYp1bwMUKnmb6SilZozwzjEySLaf_5kLZFXz4WghwrGuwn6w7P50U7v3-QPdYg1MkFEIc5adkUbDPGi0WFvr696RxVEgivbVKeeUyqi7YHhJmqDJ4PVhQ-x_doFGooeuOE9K9ICDie0ZOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMpyMtyirzk4yM0nTrPmKfMLb83l6g52NjJSRhMzj8Wru8iKFRpKTU-QUbGrLD5WSnUWkqGJG8fqHHg8cd-YV5_Q_1UljbTcj_mDeV68hYczY0G8tT3G2OcHIhLlEMA-2E1aYB2LZ8q-i69PdSWF0icLD4aR-JmWLdg8mEJLvAk7TjnRNs8-qMe68T6loEJMbMQfvUo7zuLjJNEDwZD9_sv2HwXpq0X0ww-S8qhhTmcJBmRGP5Dv6mTmPv5Zrenh3fCrzyGcEuq78bQ23OlMG_fJpMSzPj-_yIaDj0NBVFcR7lHnqkeC19YMSO8VhCgcK5wrfsdwWaJJ6Iv9ofz38A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmSlrwh92J3h5hU3eaOprnLw7KXxDZn8chlom6veyx_qYfZexQOIz8-uaF4bb3axeu_31HSUKHPhmCvm17OWiGJELO4avgjWCRrppFzfaZcxOaY59VI1ht0eCI81I3MS_PmKAKwc3Iw2QwM63y34CoxDYHXlddyUYZzJnI8yfaBTCtx4ldDJN8bJWh7YIZI59EcM4aA3HEHV7jdhHEIrKqhtreWvqA-NQ-fTyncoTzo8jeANaOFAgEfM3BPhSSA1cK4aStEdvyleUg9zsVrwHaClL38dZwSXvmb6BE6DW3Z2MitmoU91_ChXLqej1iTDD9v-byj3DJSkkronfYMZjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7537" target="_blank">📅 15:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7536">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhfOc-rcKnyEvYDSBbbsgkJaj9taDX2pgVoVdgwGIr3vkSD4nogZCVQawBywGcC2ncmzNULBbWYPjAqe4nRMVKAWlmCxnPy-wtJHZMuNQ970FYYxLQu-En7t6sijUpL_2sdl7mMITIImEcdWFgnM70Yd-Uomh64Ghwf9Y5DhEO47hs19hZpbp-J5RFwyF7iDeQAmT-q8Ei0hv1ITGac_q9eUdI25TNgXXjIi5vXFyOuczCmPJHY8X45PFbHkyiY_k6fqnRrNKZHuj_Qo0PT7L6R8VGnCmlko7IpHeUpkFI-lBjTYErjl0D6qPU3StZ48gQAa75PmB9hFztSKi71oHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=vMI2t3hYPbjvDKGj4F5ywuOqCGoX8K-DguVAKPYOchBuYhR8PZAv-T8UU9q5udEmi6j9NmDdV_OVK8FU4l8ve9sBpz_Un4Kg9fTUIKDYmWZusbJfoo2wgcL1dCjCgObvVzFUgsmEEaQIl97rGqaNznX5K9JoC90YJPtCkuW0vo5Z5WaI66K4oVMJ4upSeKeUeL8pctneuS56dF2o6AXFh8KncStvIHx0eZH1byLZsomKEEW5_70uKtc2GS1vrN4QPnueJwtyCXilaTxQmtxLWK2y7-meXTjOKv9Npq_W3i8s7Sx7CUZgjO21m5842n87Yk8Z-mUB3otI7UMiVw-DuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=vMI2t3hYPbjvDKGj4F5ywuOqCGoX8K-DguVAKPYOchBuYhR8PZAv-T8UU9q5udEmi6j9NmDdV_OVK8FU4l8ve9sBpz_Un4Kg9fTUIKDYmWZusbJfoo2wgcL1dCjCgObvVzFUgsmEEaQIl97rGqaNznX5K9JoC90YJPtCkuW0vo5Z5WaI66K4oVMJ4upSeKeUeL8pctneuS56dF2o6AXFh8KncStvIHx0eZH1byLZsomKEEW5_70uKtc2GS1vrN4QPnueJwtyCXilaTxQmtxLWK2y7-meXTjOKv9Npq_W3i8s7Sx7CUZgjO21m5842n87Yk8Z-mUB3otI7UMiVw-DuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljnF-fTa8A2OwQ5L_6pGC5oC8QHsrGs9NRih7-hqh1OEwhvT60Ls63vrqloHTo-TtvLwh7Tr-iFl6arKY1qJYMfxeJEM-hyoGZ9sPiA6yhxpYCGXleYw49x9F8JQe87GcY5e5-CZA_lHdTszHmxasxlJP_Z8wkeMHFFTs_wp0z6BeMm1T-Lpw3uKkaUqZOtD76dG-AWUtW1DJMBNkAy0whqY8h2rcE-WyGZevSVMgC7Jxf4g6E3nsHbYJ9GkpBbTR1MtAjjSrlT1eTLrVZbXrSXakInwWEntQPqGx3vgQR42ODCHih0vQLHBgX-7hbuswwTK3fRUgmziXrXsYZQoVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgWHhfvwsJOaHa_Qm4uaCOccgg64RhDCnhNTEw9XZLYhY4gakFGqVsNd8Yf5TzVFo9tb9yl48PFYyrRQ54-fGq14da1QCgDKei94RNTQFpUkAj2kQRdhenG_Q0cK8075f4LEyKP_Lh_ljW3LW5rUect5JDj675acrGgK7luLSAu2nLyhPZmtrKIV7pnv1AaShhi0Fu-5enaq-E9qhRStAW0B26kGowg7FR-xR4pobHkvSchHXlQVjHoCYty1nviScecWlkwhWqZToFtfilcD-XRx_1ji0E7BOJ4qY66ulWUxxu39mogKOuYzfxu3osmv9d6umzquzm4xIieESe0pog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxAr609Zw4zr6yZukmLV8hkFCCF1jHYeQIH2M_mEsnamMeacP0RyYimdpjkKhnpohsXh2ra6SI1JiSFhuQ-Clkl3Hbc_wjjYGyqi8J5juXTOsF_2jLUJGFfBQDhOS65D9RH1mA4LJQzk_T86V6fxx9A9rnUsOTHG6ONHwwNJe7wQzfuY44f41oG-mRo56mQOy2Of8K-4Hg0lA2r3neQmoN0Z0O0UwsVS7l5MFl7N3kaGKRJCZF_RPgbWu-hoKAD3pjdw92jh3x8xjxAas_DAOmyabsRoJaI5A-4uZ2fLlquASxTZcqTPwATUNx-bIge0vIxRvttHyzGKqfCL0j8NNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7522">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKFPTCxGLKRuBu1JP2gW4mdfMNwfA-05dCAY5egKXKbZ6Wx7MQvrkkIPIqmX7qMVu-I1X56_uupqib0wT_40HNGkT2-JxrjfiXGNO1yix4NqpRpdXbY7UtqEBE73-wxcQqq7N4BjK8UCVDv1wSIbNJJ3oUo_Vofc-QK6Bp0GHIgVUBaZPaTUXR1JRx-vNCK8DVuwL0mB45oXNCRtLLWJRQbPktGDDo0ZigtrYFsx_5qasrZPYAzwKj_IlykWHUR_LIRsNYIjIxYi8ZY3gMnZ0mPcVN__23avzgBTe9UjhGsEsU2tcrUSD0bLTeHTuUHvx4_4Csa3eOk9x5r-iqgIFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNIwqXxqRYUp_ZL9aVneKHY8xqoxkt2-XxFuXXrP_RZ56GYj1xDXq6JLzO1YYWpctyyq2_BexaU_3ytEOP1_SmeAlaEOOTX85U4XQ7W5nT-rMWgaNcCZIre5iPlrp5ELylBdDc3qKorc1lKxjjcD81OAKQ7qEzuHjWTvCFi2ZuNuUpSkPCeWliM2jHaWvtI2eyOMM7GJa_0gxjJJChk1z4eaRQxEJkhgI6syFfwPwbRmyQIjE9uOjyTAXN_5cWeTuR0Ob3Fc8unD0kkRscGtS9jZC8Te2Vowiw0HWhXa8LBWxopjj1V1sQazIwMdfawVeODefJYGJntQf0Se4YBmzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNIqeEsZhUkj6CkcTL1is4CD3VN0pKFb8QO-2J09T63i4oPz70iSUOh1Wd7CNJtK9Pk320Z-hEeGztnI_5zsgC2Sb3vAMGI04Yc4bNvcpN5DHD9VEc2nji4wkL6vUk7pKEBnXJ1nO0xoHcbbCyl7c428NHaEwQ7dpCTD2ZSmupKA8YyxcslimWJS6nsTqHV1Tw0rXPx58eP1gOkVDjbCEWJ8Yi_BRC4ROCrp7KILMCimwCuNnjGjxv6Dl1_vo12u4VUxhtir3dJVR9PHtwnCZWBhb_N2uRr9zgSI24Py9PF5psMctxlI0pDAEYENwFlyM4DVYq67oE3kCS1_VE6lrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVwrWip4axzO6_D25KhD0lz3Qwh0B7Ub7akwTzBvfSmNPbkYU4yGza4amMsAykOr_DYazrOmxrPB2UzH_tKq3mE32kmHGZTO_aetERfiTFJS4PwcdD_BjIidacHWR51D56HwAfkWjgurcI6nJVSoKQUvAnqdWl2GOPnc8zlbAt7ttacoo9itgxHFn5ae_CFx9520Z2ldGwCGn4R8L5-MAiyoEHNwFB7-2cl2Ade3GK2jpc92UOoltKKryW90MiZ8vr7jV8XZ43c97h35qtV1Ov07cLAyiI3DB3n3sYgGH4q-c6H9JO-ylfV6HdDyjboIiDbOrUzvsvnEUquyDAQf7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=aMAsVRr1kZevBYrdxbOEPAplaQOQIJWvMHEkxHTMDfAD99SMX8jFkNbTCjytz3eR5Jh1S7Ryac914lpqYjSgSmbo6c9irQ9SG69nz7K8Tu-eb2xnIWvVEgRXFM2lOlC_AZMGtHEsfgszwzVdollc6GvqaqCxFkPVI-vu0dt7Lin2D3OOjiQ5layKUTT3aTkB-V32tYibEp7amxyNsjOoe2L8WSjqEjJuH4Z3rhP02EXAwbUF0JOuCyBxTzB5kU3ID_vumYdqf52seMFuVr-_zvJrNFn6yEZhnziqyga_RiKSS0W7AS-X0Qy5rkexdOhCwFyHUFoiqUSGZgLj5b5vD4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=aMAsVRr1kZevBYrdxbOEPAplaQOQIJWvMHEkxHTMDfAD99SMX8jFkNbTCjytz3eR5Jh1S7Ryac914lpqYjSgSmbo6c9irQ9SG69nz7K8Tu-eb2xnIWvVEgRXFM2lOlC_AZMGtHEsfgszwzVdollc6GvqaqCxFkPVI-vu0dt7Lin2D3OOjiQ5layKUTT3aTkB-V32tYibEp7amxyNsjOoe2L8WSjqEjJuH4Z3rhP02EXAwbUF0JOuCyBxTzB5kU3ID_vumYdqf52seMFuVr-_zvJrNFn6yEZhnziqyga_RiKSS0W7AS-X0Qy5rkexdOhCwFyHUFoiqUSGZgLj5b5vD4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7512" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7511">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7509" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7508">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnHxbiCUkzqPeGHb_X6tBNrYvf3pRHLluKAM2sZC5aJjnbVnh2Ed73JmHC-iJDNOL6Wlbo2vR2-byDTRB24yBEQj1ZO-GK7XGd1GJTx35EUQhaaZiBxBAvyCHRd4t7h77E9nJRVilBQeSx3YTaE-zwh1Ngp8EWv7kj-6VHx4EmLu5vaL7VcxISGdwSpx6MG-PTCc3Z8w69EupB54muVv0aL0cTdVm04Bh0BGxaHyEA6wDF-4L5hFQTG0l2Lm6MlZt0UQ_xplFtfmW_Zf0bpGG666OAxTOEWF2zZf-a4xN2Xz8igLOUANZqS4jUzUnARDk2pGiQRQB-H2L4ReuKzxBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7506" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7505">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Caf4V4Gv-R0zRcaNnEaPEKz09eSOGcV8ebrqLZq4ayfnPjn7KhNMftFx9VfA0T4It_neL1tdX6-eQ3O-ZGMP8Htr-VdLhXvnrkqeTcWOLtT1BLJ6fRk3MpNf0a4rrqs-FzWTagARUwcjBVmLPTyrXpyGXFGRxZb73gwDlBM6ZFRdJ5tZBGwTn0HGdIGz6hhyay5fDEoUS6EZyB2TBzjLgkdpdXgqEq9NMEnb0ZLQiH8WeHVXDRcPErA-pH1mfq653nkCPsEPaOymVFZFmiLP7NTdDYoRUJzhbFaYF7Yw4aR7H2xZU8NcSk1Pf1YNTbMBBRgOIXmkBoRWKQ-Ki7MvRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_BtG60WztIx5xhkUJKYShBgFB19J97D4Up82lBRDFSjcXtg_gG9Bk-OYpU2lHyII2mYYvW7H17-W2k28M03evvOM09CBmECb_TpYS-oIKYJeTe6bJVJ91BCQWQ0EKmotGW_Kp-01VMp2yAsVU-5hAHa7XtPfHAG7Qd-6AHdFjLMPwOgrucIzYDwrHjeMrkyxW64XrxJEgAwBkL_ahIbj6fvnIXg3XicWzGxqhJlJysLKRlrNPJ74qEETHSUebmZZFFwHhRQaNgJX6yfpr3v0G4KT6Qj8Yk_pgXcjDd4awjAhictkButSlVC50lY1kxMnrIOD_m2PvCGKA9byD7j5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7503" target="_blank">📅 11:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7502">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sO-EXi5alqoWoEXMJQfB_hUJUaeBD8-4AqAX9xSJleh0wqJhr2xw1yXzLAPxAPyJfs7z3bN_Oq4LgDLNjo6r5lcrGork-akKLL3x2LdRSX7v4ioRQBZjAn7k3Fo7wkV96bhoqh396o7P1ahNq1SwW28i1ZOJ4gVhOa3AHVwsXxHvHzhOrYeqnUlzQwuI6_Shn0ExmrH8UdVHQV9pFcaTMn7lFG79WtEmvcyEeGw8klDswaSmv1LTpk3jAevuTB9kLyOjulJKMlXgkDo64iBpgYDowOrrEU8p4lEUYas9vhfqtDfqPwkgnlaS2M46zWRg-Y655nH2wIoxkl6uJzPYpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=JlGbjawJTcrSX9QS9brHr95wXK84o631DPHJv6OCbWjeioPyioDkITNCSv29lBlc1N-2d3mk9uCY3QMqHJtTXehtxnJX7S4rMOBjsjBOgDJ-3jmdHIIy3RWORK59ZpcKi164AofKLkVPVlhto7xFJatY-BIIHU9m6LKbHgti481iahujANEnqi8cdIP8qvp7BBPA-WhV36LzSUuVAOxgisZdD4OElZ3ktAh7kEsUF59M0Cf2qDU3MokZiaIE6I5lX7XCiohfwSmdAzyYnZzDDSkC5Prsp3kraE_zhQLCFMln8PXZrA4-10NaT9ESP_GobSSBnRUhqddKEkFM0gmzgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=JlGbjawJTcrSX9QS9brHr95wXK84o631DPHJv6OCbWjeioPyioDkITNCSv29lBlc1N-2d3mk9uCY3QMqHJtTXehtxnJX7S4rMOBjsjBOgDJ-3jmdHIIy3RWORK59ZpcKi164AofKLkVPVlhto7xFJatY-BIIHU9m6LKbHgti481iahujANEnqi8cdIP8qvp7BBPA-WhV36LzSUuVAOxgisZdD4OElZ3ktAh7kEsUF59M0Cf2qDU3MokZiaIE6I5lX7XCiohfwSmdAzyYnZzDDSkC5Prsp3kraE_zhQLCFMln8PXZrA4-10NaT9ESP_GobSSBnRUhqddKEkFM0gmzgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E41nB4R5qcsz3fZckajvisCfhM5slDXhVyMJsqzS5fDydUl_n2cScxEcqCME2lk8KFpHh9kX7wRNlewSTTLvqM8YzcUxzQKnK91nvxrzpTUwlxmBqjIBYzNVI2_mm9Uir95TQwu6J69QrMUDOJPhQdtaLsmmDOfUCw7U-mUGHHg02P_AjrYsyzPy-0WOJzIJRQrIzku6i7KYowlYCilpsynvc47RNQ0yNw1VcUN-DSkhP4tRye6CorScvKiFtzSb6VSDGPCR4M4j6B4QtMUbKoVCCUf9j3zI6fOfDLtIUkwhYBzh4Mp5yxoM4RR3lltQkmv_fRuDBz8mZS8Xx4trxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=XxXqSiVIwVNm39HdxJrAmGJIQxpITNAkrGX7GIDioNta21kJYvyGoferT6vCmfSQQTp_moU2tPU-35OgDoDK9-HnqOUZHZiY3H-uRWkxj01yUmHuld0Cl25BJrXGHZyKFDLgnVBKQyvgjSxVK8AQ2tf4RbnReDO9U1EXe_-9Mt3uKBxhDeQoxpVwMtU3UPVsNTnVMyPt0WmUNil744ifI5JasCvxOME3vnISDkwJ7ahAsbG3yo28OnxvkESj2PMFKX1uQD2H4vVXfGFzO5rll_BUVJ_xGsDH7qtpPVKs9NTVG2nWWrJWeEyd6Z3beduZtXu1mWck_n-3U_bSKJ24OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=XxXqSiVIwVNm39HdxJrAmGJIQxpITNAkrGX7GIDioNta21kJYvyGoferT6vCmfSQQTp_moU2tPU-35OgDoDK9-HnqOUZHZiY3H-uRWkxj01yUmHuld0Cl25BJrXGHZyKFDLgnVBKQyvgjSxVK8AQ2tf4RbnReDO9U1EXe_-9Mt3uKBxhDeQoxpVwMtU3UPVsNTnVMyPt0WmUNil744ifI5JasCvxOME3vnISDkwJ7ahAsbG3yo28OnxvkESj2PMFKX1uQD2H4vVXfGFzO5rll_BUVJ_xGsDH7qtpPVKs9NTVG2nWWrJWeEyd6Z3beduZtXu1mWck_n-3U_bSKJ24OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSMd-bTzEapqmyJO4FWYeK7kFVtvxKKMwWtoWvVmcbDY53eanGW6l_i6Z5Oc2afeokl8X8d_FYHrdibQm4J2be8Vz_b4SySRgK_l0PXRYtz47_rp7H0UeGiQOiy-AIrpPyB9pCdPtkgDpreb45s_GNbV1b83kynmSVbgT8mCVSWsJtlyLflWJfuUDOGBQggOx3Exq283gnYFO5-mDGqBZOQI7fEUs8noB-UECWyTSIGV7Qa51AhfKdcOB98UBr5WaWDSe3jd8mZ8RTUdySmV1zEFVuPdfkHTEk3LfDUmKAAAL-_j0S4sQ1eZaPtxaNrKbB5nGQhgBsoqEFVimoPgsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=GBLHHbLZZNWsroUzEk0moJT5_ZQtHUVAxIp2Tq3wIE31gDWU91Z-pQP8f-zC01UHELUHGS7fG7ExGjhrfrlpb9VIG7uArFXr7vNitPnYDxm91vNmKHwaS-nilh8E6SZkUqbDoygh4KszuzukCnzlXiYoI1q2xASUW5Kk6uYjX0OnmfQawgd-s2GRhnockwtbfQU1aE_SE0wpmYNfkQ6AjMgXbqg8ziWjXn1Yyvq8rPdH17kcDf7HXjcW1A8cLPZSm8jalfZU2ufGGk8RQWdWjNABwdF-HU_J7XTqmGgizBS3if_YMwb-WpixCL7eyD5xsOCcSq-kDqMJb-lQ6IPAhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=GBLHHbLZZNWsroUzEk0moJT5_ZQtHUVAxIp2Tq3wIE31gDWU91Z-pQP8f-zC01UHELUHGS7fG7ExGjhrfrlpb9VIG7uArFXr7vNitPnYDxm91vNmKHwaS-nilh8E6SZkUqbDoygh4KszuzukCnzlXiYoI1q2xASUW5Kk6uYjX0OnmfQawgd-s2GRhnockwtbfQU1aE_SE0wpmYNfkQ6AjMgXbqg8ziWjXn1Yyvq8rPdH17kcDf7HXjcW1A8cLPZSm8jalfZU2ufGGk8RQWdWjNABwdF-HU_J7XTqmGgizBS3if_YMwb-WpixCL7eyD5xsOCcSq-kDqMJb-lQ6IPAhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTsoUDqqPLJVSZcwtq-jAZ7QBJAAzykHAaO1-VH9x0tUk0mC6IJSeEYhA6oXNJkUguf1RqpEdMsQFbOPU6j687UiGA1iGEDANQp3k43tKhwURwJLdfqWsIBIb6rKMBouvGpzG0QvZ1HL8u5MNTdIUpQfdPi6SqmZ_i_6_J-4VkAofvh3T-qhw0ZnjdcRoBHcr1XN-v5hyDORmt6gW6bw1kalQ-lmJuv5uVMlROlcOIy3zs3iS51uOXEsnRJ1nGwGFBFOGJgr8fDdFcVlOHKoHtl8eJQTQgNqjxf_hhwuvoTDaOCJm50r8Tfk33hLbOcLikDq4R24sZVec4hxkrkDzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5-xuCd2UYwLEbUD6vxZh5uY9qYJM9gc__OYHJ9dZoJYp-ULJoGP_vDB4_5zXxlCdC_VFjV7hKzk3-19oMPmiBmczDWgAKqb54IhycHt8qfbo6q7i4eZnN-dE4ORGsrrlt-JNAx8Gl7TNeSU6PSHPxrNtlterst5JJYj9hT3FeMYZ2yYRUvgQhZcLhFxAAp6pE5Uu7KA4IJ4miH2-wnl0OrPRTHqb1dBhUSSSr95kx-Zme8sSG7c1Cq1W9rRcUHIHU7_IDZ3_N7YNkqHtjVUJK4Eam9QMomEOjs91WgAtCvFKTwOXw5AM8TeJSqSg2pboz1xxucba78_6iJqUhZK1Q.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
