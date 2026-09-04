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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 12:42:35</div>
<hr>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvMZrDjuxd8OKafrUnSdE3FmiIG2khvq3cO4YUiDVSHMdSZVtpSKXKjcZw15V3BFlVlBMnKAj3aUxyoWe-IKjRBPkteW5xgAq8Ntm0nFsyY3HhljTUqhD4aX-BhRvvSkKOTQSl0Jxuc-mvo7qYmEpNsJ57G2MufRczS8GAThHwQd5QSjkapbAWdexVJ2ERznG7cFELQ8Og6jc-gChRMvRhm6N6WKwULIZcIbYyX9OqLKVoC_MshzZmr5m1YOfvApn3gSBJ6uCQVkx4r4Vh9N43EFPHd-fZGAX0lcajo3ED99xNFLDbc6cNEnKFoqQGMEe0__9v5hwmv5rUB-m0gu2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
کتابخانه پرامپت YouMind
بیش از ۳۰٬۰۰۰ پرامپت آماده برای هوش مصنوعی
100% رایگان و هر روز آپدیت می‌شه
⏱
📦
چی توش هست؟
🖼
پرامپت تصویر (+۳۲ هزار)
🎬
پرامپت ویدیو (+۹ هزار)
🌐
پرامپت طراحی صفحه وب
⚡️
بر اساس مدل‌های داغ:
GPT Image 2 · Nano Banana Pro · Seedance · Gemini · Grok Imagine
🗂
دسته‌بندی حرفه‌ای بر اساس سبک، کاربرد و موضوع (پرتره، انیمه، سینمایی، سفر، اکشن و...)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 398 · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 643 · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 775 · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7618">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGEMION | مرجع خدمات مجازی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrOSEeBjMf2WGOcSVIXM6XRWwfgsB9y7miPTx5Ex5ojFdz9eJquWdGyiwWMKw8_SyLtzxq--tDUM6oz79YSGeCVKeKDypTvQpVq8SceMRNRAlphHDgWGgPQhJwOljEEB27KFkprIiZ-oxanVgzpruMw4GS5DBhZ3x46vD5SdXucs32zq1gNAByx3REnzdm_rOHNy4oXscGdWmmgrCrnXxRwghAMpHMtLzi7maYEfCv03tw2bSlSOB_cmqoU94zweCSwZ4ltqwZ2q0bM78HuwTnCy68RvXqf-eTfjtTH5mNzdVSMDLsYZJN56e5Ag9XIUQXFtyrX7KauKbvdpiJAa7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی که تو دنیای دیجیتال لازم داری، جمیون کنارتــــه
😄
پـریمیــوم،اسـتـارز، ارز، گیــفت و خدمــات مجازی؛ هــمه با هــم در جمیون
⭐
🤖
☝️
@Gemion_bot</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/7618" target="_blank">📅 21:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7617">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/7617" target="_blank">📅 21:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqZGb8ybNlGTvmgAfVX221sL63l7co1Hkjs4OYIa8yuHe0ONrtMud8r4maRdQN2rcpxoXpVQG1oxW4snbY63jsJiFGLdc8w9Xi8eoQlR9dbFamAgECN8Z3FnYcqr-Vn8oydeI0YwRmUC70cszVa5cc8OuPG1E036LePFuTaAO8z-WY-EyDv6z3cYY-73yxGwcXAJx0ElRn1DOTwOtRwwsb_fPXQYhwdFJsi9etH7LwaNq54kTzQwHDy17yaL-hLC1UGV6O63yEcHaDDGB3P9boravbohG4NWK7uPopdpm1fpJLGxjEnss2_MZFUEPqst522s_F3xRFdwxlLa0NSJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7607">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7607" target="_blank">📅 22:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7606">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7606" target="_blank">📅 22:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYU6x0rLjfLC1MpW2NPGnrJwnt801H-tJ27WIxqcf1TruQXTMbfpkb8nwaLiqugN3KH8xGiTzjitvGBvCVnsCDFzqDLFWnIuTN-T_8c2n87S6zZgCjBlAlQfu_FmsfAnRzYEbjhuMvWrOcKI-YZLPSP7Q8iNGtuzbMcNvQtuet14QFptAv7a1RakX7EE0-WkUr9CutrIt08qnN4J9gty7H6dJVl9Ajvjt7IkRWgbYEubcTKy5v_lWBNSFfnI707o6sGR543oguBj1Z9J7M6N9e2B0Notkc_myzhPkA_2OttWT4Downdh4oMdg82NM3pYFvqzJRiIx-6Ldksxu4frcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0jesaDD-GdXVxpjIBTEG8rCf4Wqw-amPynkg0pyKa7g7SWbYjY3GWo-OCZ6Zc8-M5Q1X5SOY5IzyT4Z_Xo0ErqYTao06aL2RSCSxgVcDFtXbFApdsZZT9jY9e3AEI95dwmh4L6dx1b_5MCQzqbGZqozvNedgLeSiWQkNKV_XwUXZhtkvwPphgpjueICcTIXF9TqO9P7P2tW7h-J0r-r-Wa3lRzMEgCpPAQbUrP9Ztrz_6-kckv6FJ7hbJXue7qlSCSlD-cVALpFBYr1ACwMQKDE4ptNhMY1yu_QklbnG8ESPpFLR0MPPhzDR-ijxYDec8PlEVjJG07RSFnSrQnbFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzyQJz3G-UBWnU1h6tYs4704MCFN5iFADilQvI7pchwDCupwGInYO9zxdcWuBmbt8uj5WJ8o6XJPsBkBaOgtxRq0MdQG7n7hEtiZfVInhF1Ki44WAkKYCjn9XwHrDL83jkCmmXH__k6LNQlotNAWjUADICB78E4obTyl2uDcyQwlSRQ8n4DYdPdiCE8dE5ItGOrdYdWlksFq4mnFh0tOwAccedfktkHNLdf9_3QFWl8FjudLN9zF5ahh9fTQ7dyebG32A-6hniaOYNS_S-BnsyI5sHKR8h7QS2oGo3TmXezu1u_FGEKTu-xNBxK1wuTlomtU-ag-2kmNxsmN-oyMeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YASCZgy0hIF-XVH49oqTblxdLIBuDIUb8QwyFmSYsAGSj4AVs0gjnVjngjcp7iNCCSylY2HWrz_yHj7G6d0Joy0_KJ45rGtP7M6cu7lp3p0zS9Xg7epw3V0Sc-uJa9-xLE39SCsuqsAko2F-WaUA3ALndHBL02pIbUqGIerPWTn34W1ujzG7JilALYEPfkxFxGPA0WriaPuwAEtKzEorDm--UAD4XD6nSB4yxwsMs66Tg70L8Z-saNWyox3iDmP9vheA3eYhjgzU3qUUq1BJzZmAqcscX2pUMkZ3KST2h5QQIH5BaGqo_FU7UE2f9mt87VpEgyBT_FgeAbywI7DQ2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrlefogKcSWEEtUCK32gdVW43sx9-3uuFSzm3ieAn392Mf7BB_KcKwW59qSizTcujlODrJCx5XIwlB8xgVxhRPm7BlZkGK8sd5OWh8CSdcGNEQEKFUUXn-prFsD79YYesLiqsideSyYHUbFgNMlKy9NnnX5TNpLZQBk8lbeyHeLCcS5rn3kelE-R--0BeBgozgP8xdDyqmDkSzElsAA47jRbapuh8fhuzZisPg6XAfRcMBPFtWudSoRIcU-sMef0pS8YIXRiNC35KOFC18hifWx9c-9boda-cmjuKEeXHnPPOS9cVOo5ysRSjghRUl5puJnZ41KDNYNLul4cirexSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjs9huvidEwZejgWs8_DYQErKDR3yAzeblxF8ErdDc2c6yyZUtFQcYaeYNmCqJUvx_z8c2T5P4ZQOcutsCo80z5OanKyM9NRbthC5yxxKyPg6UZwZA1ATq4JCvS9K8czYLW_9btFb3aPd-l9SIfS_HGZNLolTzs3sCMjOdrm7ydRE__Z0RGNOdluDC0nRL5iVF_uJQS86o6BH8nWpZCO2ve-Xq7HDHQYrszMbIVelSv9710_j5QnWAihFU8MxxrAb4Bw9mWPVLSoOT7NrppQj1gNFaw6VTO_WCpquunWFIO-s4oVJIN644u1GqZ21L60_DFUQC3o5iOy88uBkEHPBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0b_AOK8qxHlQso_CJkbsDaOQYv4WZWAE4zDWeV88bmYQIr-AY0qxNJpHOXLgjeUcLETR59iASeDo0D7d1pxSKH2RkK2RIySbv7dYDxoQ4iRXf1ZfljoTTmZE16n07LRtUK0iKJ-tufPzWACRHILSx0zy0fDmZB3-XLycx1jmpUY2ZcyB-VkxnCODtEpfbTYBAS8C22wWLynsU_Rf-M4X9v4xfZL8k95War517eBj3Dw52gX0VmFuqQdoUfhv1apJ7aV9TKbByhmrqnGpMR7sp0pZEKljGkzoOvdAE565jfX8qZPXzqhq6X_f_9Ve7II-Lj9M4N1LWSnr4Ous0rdEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHse9vZyRy0vMaOldU7__ZJ5bPbwtCcRVy2Wj8PJbKBMYvC9w7_PuiFg_NLB5jCGkGDMVmYb0QZ0U-am7dus5gMRHyc5MlMMrXGmiFJXUCxzYK9cxykwtidjlkRco5H0zOAfRhUSGPuXZ7mF7AnAEAMPPHDPXNqRc8FoWnFnKwcqw3QeaZnR_IGXccG5LEdv2a1TTfzHF8I6sWc83GRJWtfLiomXaL871R2N4U3LJRuCrWxC0O4rOjQ8pphTfGAjR5fhiAAaC4Zlx_EMyIHKdw2wae-3Rva767JuMqJtUChN_YdVtU0FGv9PKDVwFzl_Lbp8VxXMq9POmlVGOBllMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZcY2hp13RvUQ9PxulK5rMp3Qqeb_ET88WyTMOeVnidG4DdLnw1NEJvuOoY-LxzZUid6MmHqfar49eBWiCO1frlQboiFdG26Xc4LU1rKZX1WOwfNpk5vnCZBlp6chndabBkXkLtPjIycFRxbgxXiTG0R-DtjUrSJ4WrKr5B7exr4WPtQoHf4eZDohRpLf0kQAfuP-Qs9Pgfhwh1fkAsVfzumaLBA--O-55bD8n6rOufDtjEzOlWBMG3qdCPrwXshO34TW7RrS8aukcZ_PsSKzcAsmEJoEImmal0dbhe2cUQ1nP3NPtO0JwE26SkTaNF6ADLsMh8WX0Usbq-AQ8YzZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbBuyY_-4BSBUxO1IuDTPCmTT--wCkFX1ClwqmS0amHKVDxEZca6Bddl-iwbQ64JyN9SBojm2b7_IkrOhilcI1j2-8RfRnCP11n73_MSIEjrgHy7DAfMjaZSSXBUlX1CQmBfxaO0zDwPx_7TAcfphzPR57qpAsC7XkAkiHKqT2kwqxvA98BWO2aWcwtCTFE2f1BEVmOpjCjx_ELIsO9l-fleX00LNY22x-hJUXi0-Vc5iyMiRd6UonF1LLIwrbYdw79uj5cx4yTSIIkDeLwwy2rrUCK3z3Q9LEjiaPoLu0pMOGz7dpdvjq891XQJGU9qEiCECpOb2DyYC79Z-zMr1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=tYr0GnOdghxjvHZLyxa4Z19OFdC8XpLMj9gyBBxOiRErE8Y0Simq6J5CRVITm8FN6j8Ww1fCqYmWqBRCu9Fth07zKfrjz91RZTaYGQ6NxX_93ijMm0gSVCkPO_xntAEiD_PImBE1mJK070kEVlr48TAjGzrTmMczVTSbonjSw_8GR4H-GN9IzVCnfjr60S7bulHf0Zh7n6e6X0IKCeh7390kJm7HvxKyAaSMwxX1EGmfoY2_lOC4bM9qe-Zsq4uLA7zh3ztJq3SMhruFxeLY4jw71e_lL3gDbo1G2H7pL6HsgQB0S08ktKK6G-hGti___4eXuEmfFCs19XurWkZ36w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=tYr0GnOdghxjvHZLyxa4Z19OFdC8XpLMj9gyBBxOiRErE8Y0Simq6J5CRVITm8FN6j8Ww1fCqYmWqBRCu9Fth07zKfrjz91RZTaYGQ6NxX_93ijMm0gSVCkPO_xntAEiD_PImBE1mJK070kEVlr48TAjGzrTmMczVTSbonjSw_8GR4H-GN9IzVCnfjr60S7bulHf0Zh7n6e6X0IKCeh7390kJm7HvxKyAaSMwxX1EGmfoY2_lOC4bM9qe-Zsq4uLA7zh3ztJq3SMhruFxeLY4jw71e_lL3gDbo1G2H7pL6HsgQB0S08ktKK6G-hGti___4eXuEmfFCs19XurWkZ36w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxTWQl01hMVIdYyXqk7CxjubsTTbYHEBcM7y0gA3eW1_YWgr0r_M7YfTyfaZw1Qobq8MR1c0bhyQ5SIKM9JQdLZ4vkwPWWdPujbmhaqSBHaOiyZT5oAMBJyELDm9g9bVM6h9UhmlgjTT8TUsJGCOu5yG3OlrXF9i3RxlutRnnbwIsXwq8M6Fo_oe91h_gqA-pD0EPAR3HQfsZG-BAwDvbJ9w8xbIbjJgJzcqT-nNEKFUiijdXIX2IV1-ucXNI1YHGzIcF-snNnIFXqIB1qesdg_y6xqlbBBwr39721IlG6--MjR5bdWlLkucQTmRdhLkRZXWLMXCHenSFTHArZfXrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=Q1Yoh73AABGEKB3GuzTtpOFICo2l9S9qLcFcHplRDS4CYF7dCxpt61VGAGJhgmpUjUzRGssqfLlvKGDxFImJSvTEgkZXdQYvNbICgdywcdclLjF_g5Hr_tFb85RQGL5nrYasJAZ0iCjFcFQXT1NDLJrOsG99PZWghTXJDgENbz66HfUOILCjTm9TWFUNaV0W6uTWjqIhMShcQ6GrQPozB6wGDCf_nK55-8Dn7qRDwNIU-uhK1XzJUIAKIuLiZjH82B8EhXH6aVRu-0GYjgn7rKPDw_Udsq6tEn0C88Dz1H9imra-SFrXsxhVPYwQyrBLXwmFJo_-PIJoa3K7diRf0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=Q1Yoh73AABGEKB3GuzTtpOFICo2l9S9qLcFcHplRDS4CYF7dCxpt61VGAGJhgmpUjUzRGssqfLlvKGDxFImJSvTEgkZXdQYvNbICgdywcdclLjF_g5Hr_tFb85RQGL5nrYasJAZ0iCjFcFQXT1NDLJrOsG99PZWghTXJDgENbz66HfUOILCjTm9TWFUNaV0W6uTWjqIhMShcQ6GrQPozB6wGDCf_nK55-8Dn7qRDwNIU-uhK1XzJUIAKIuLiZjH82B8EhXH6aVRu-0GYjgn7rKPDw_Udsq6tEn0C88Dz1H9imra-SFrXsxhVPYwQyrBLXwmFJo_-PIJoa3K7diRf0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5qW4TuhWH7_maWRzQV0Nia4lZ_iy3Q1df4KxM7ixVoCRCssF1gmizLKj_EiW-yVsQlFipt10RwplUgg-YeYk-DySa0T82ZytxYGS7cYbKUQd-7yYn67PiB5SlUSRGwF7s42bEvEheiCJZCmK6JdgBXMBwQ1gFA6wKBHPD5LhM2SZIZEwzHxRfwIAGSxC3Ad-OkmSQ5UWbr-JrIerIgdnt_c9D6KK1P3pGTKPsqZReBXpNoztGRG_BLwCUptaCO99xgSWDsB-dukkjZTA11kBLx1uLBxXJ-LHnc_YoOZb8kut6IskjaztFl73FH5n97vYbkZDMcHbfszqSLXxnM8gQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lATZa_xYesQtklfjMLKKJ7RHM0fBjaghM9yMF1FjkWkWNNddMBHy04rLmfD26cZVlpLAE-Yx_MEYadLaZUj4fhB4E9GH0XWasxtfu2PBiwOFnnEVXrC5wQQz81F85QYqlN3H8e0GF4McxrJdx4VjcVtyVniHvw4JCYw3l6JTv3ZCkwrQ4SyZnACphKg48BsK6J8jjnOP1ZCtgX2DT_4-clfiAgjk6ly1OY3VULr2OW0u2C5Pk3kajPyVPeqEflqPvsWSTAM2QX-E8-FRP0I9TJAXKNMtjX72uH3MjUfZkJ11eGkuoYPQ8gUq5pot-D-PFSoweyYXsse5-s4bGxe5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PhhvoLxY6ChQwffg4hpTpLyj9X4-N0tk-f8QzmJ0CYhAHEQlxzaHO32wyQiusbc14CkzSwqUyxlj_6WJFhMfmrSV_QQPVKptuEdwWmmQMqCzeOKbuoWF_95Sq6MpUbls-3-Bc3qLKbHIAEYMpMZmohGPbRbygEcVSpeYWqYLCZJanRWL2ExiMmFWe6IOXIVtjB1kDkmI4XV1WrjAinPap5dqwafndwCSEeOoQqK0-vHZAuUxKYmawlf2TPp_o7VsLlDbCdTx4QJxRvO5r46cqvEi3L1MEQrlg014UhywlP09UwDsyyY_WF433OIZY9OPhsVvnuGXHTImWEFn5_EBKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcEi2ejbhsNYLsQHVZHvpiRirWPUFXtcilh_IYx8-Hks4zSb2ooasroZ5VUXLCTf0tVwZAD4Oj_57uHhhYYl6tHNme6d_kUKAECyLWH_oJ-2d4PqxIoP7Xkkgk-8NGxWJTWRZlYEKLs8jP8LdeDyhIw-FX4C1JtDT2K3dz7Uxjt8OBj3l-PTNKUiQHd3NjwtMy-mHN2Nh44acfjGTU6JKHcJ3eiKsY2LfDNJ6-XznK9wDugk90RCXiIolMP0NnxgR0HaW2P2iVLNpQsXbu1M7sSZm5wL1wO0QSfVFnPZ7eEsNKX3PLBfefibKQnmbYiDoQ8FwgeqlE2Iy72eDlIzOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ePEQAJLmPLzQndDJWdQJ_mUPVnKX3ptjQAuLFDxBhTtc7f6DJtdkXJ1f7LfCNVCDL5mlfQZ6dIZOuUIHJSX_mfrRWBDFUFJFq1vLag8uYAXRMl2Gt1mxQg2PQ1TaHpk6EIJfJM6ZD4soXhVwmn7re2v6DwjtmuC_HfdIcJSpPYJgIy4uQh_LqpDQwqXWwqzb6yyroy8wERntet73Sp4TN67-GKkG2ZawIpLJAJ0NLDGRsCjkolkS0gs0XgwerVjarkDivR3j7kld8MXiH80V_ly9S7kXfWMPC35hF51_gH7u2g-xXq3-rFof7odjU3DPHI88RnmUTm46LNrI1zl_GA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHjq-DzjFM9YOE1vuFmE2SCrgAmWPWyAdt-9GprBZv8UNHWRDav2mOAXQUlkPKDxFmGqGBPP-FKXYe4KtMTK0jOfNtX05ygJiotWsKNNnSCYiREHT5C57Cypyc4CRhI0LpL5AodHiEc12U6qTZ12UIuxvS1FTbq_haluNwBdYWB3Z2D-XmrByePJgZ_CsDTN8g2RFNz2BoP5MufTN6YrfXBQvY-1tk0NyWKAkNKFVnK2GsAI1MFEPUteyk2tHOFY2jXSN2MI9bmf9xClQCup6SP3hHOdNSXSO2pngTnEVp0Ya_-6cBVMP4-0ZX9iC1oAL_nC-V_hhtQyGhFtcQJxng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZHnDTyhWs9bS-tTRoYS6ykyx7z55j-MU1jHCpKkzPnx47u4B0Yusfj-8R9rHCdg9hAyq9s5l43eTfJyolDV5EMyAVWVERO5zG0GVyUpyYigDrnv0WsRjykyny6p0p0iv8dbMSYJn-9aGXKQSrOcsn2wAxW0F6PIrhyucsxN3QY_8EVTMOwvRFl2_vOVt2WU93zjuVFSu-F3Aa49c8SU9ygr_cc-orDxXgeYVn5av6OPfcrC5UyopLAj0BWBoWpQ45xsR27jkhx8H8Okp8IiU3mILl8cdMBJOjMaeW2C_cyxLr0Tvt_vqiFSOs2qWZu_c14tTaBO3K31_NQOfT1f4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ud63ya2uHJUmgvG95zKtS4HLhN85pLOVTcdn2D6aYfvfYVngGQv07b5akTRyRB_92bYbS6_cP6Cct3CV1LuroVGgnCeqWr6ZB-vBLJ85bJWDzynmajEm5hr4ZMKZX7BhJjfCVzFLY-SohTtqPIEgG606Q5Xq6ydT93wkCT9vMgC18gmFpQNdnLtQcDnXjGZ1_Iln-dh05jjAv4zkcplezfuI-mFIsW17kNFeyqmj6c_UfDEhSpgDY91Inel_Xn9p5iqFItVeKKXRDQcpVz7HDVVAEji0v1B1H_LsfKfP2i3Ni4DTBvSwdPNLnEWnqvvLtMHY2GJoHkgg_1bCroeM-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCKsbBWh-EmZbzwXRAJ4YJyPyteMrDm8Z2ORmi3pbucQbuWBDdlgAYnGVBJX9WrxWfvnanksUP-oUzwBeLGSM7sz98Jh6SEhgfnEo2TZLHrTvZDNEWcurNxjhpkMeeAaiYULKnW_80pjmEaxx0bgJQEwEDBQ3WcggsJMYNni-W7zGfzd9OlnVFxxO1scC2CmEG8ZJiNqD6-yEjHcLLxG4H7SwMJhE8vG7wz3qTukrsytBOmr9Or_yClFJvL0YI8vcDEINIucflSD_VX7E3j_hyk04c1hDFJt8bYexYnxCVIEyZPDhFt78tls3wFty2PkwI0IjT05TnsB4SOuCeXv5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p22Lt5K7V85S2qU5Wvp-wdXtOzZcvBTEtmC5ZA2BvFIORDo_DVIzyAnNWaReov4mV_ncQYWgBHt2T8m-KQxrmXFlcRRAGBenXqKew-oQ7fiO7iGZoFOBBZLZO9YIUiMvDkSSZmjCGtfrQOuMs3HwBLfQC9lLN2RrBVxfd40n9w9DkqQ4a1hMrqOqnoZuoMrQWh7EvSjnLYgyt7lDpI8tmoobi-RzTHNv6uUy7AWiwxrJqF06uDTr_ojm2XN-fPH6D4X4jWunGfdyZZZIgfcB6lEh3o4xtVNjQgnDg0tlZ4WuNbOKE60UODuNERuVehrhwAxYEjiMTnDKufUvyWmRiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMdr9ZpggdJ8ZudThmOvZcO70ccobqBPF3dAD1HGJPQoNyWWNgSan30p4sl7LMmWjvFXdvCgpqREHEHcwc4-vfOG68ntRcPBu0guOAiY5UdiEIbyrjfZrU8k4ydrOAR03QNggZqPGUCo1TO_ekm8NKcCvvvGsInGHT0B0-C5dEhLvn7zFYAjUoLZOD54G64mg48Klno5zqu9fE9nxseGi8rSyWKeWEe1XnlYzJtU9tLDh3IwjaI4sjgCu4vKed-R6FgBumGLQ5M3sxcanWibPjFLWZHp_J33RNuurj5ehbhZ_LsPRRjaTRIQDwMRcqYvflMVeJ9p0V5GMu--tvxCHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwSyegrs7G0dvyxOCoBuNGKxlOWc6qZzcro_2toj0gDzh3cFNZbf-ZHDW6VK7MwQUuhDhh4_JrarueD6uQBgPQoLGVsxDgEzuTz5DOZBfxzLTfgSqw3GOtKUUdBNo-nxyQdl29ew8RFqUWUzd8R5w8-AcztFnMeoabRVtPFz94S6u5j7Xtf_DNPfYquF6cQRAS2ulLzPUDjX83SGD_C2jNey8fBjmZlPO6WXBoMK7mCtt0xiw_CF67fxAiuIlsvThCiMgJ2amPzzZAhhZ_KzPVnWVdpRJ0BR_ynOXb-fg6rKqDYXcmWejnx5T31ZvgRKNI9RPCE4FEl5R1d1pcijIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=SyY5KAI0lS71CccQkv6HGMm66KbFGeVbxi9RBcNIQ-Rp-tfEb3OBfftAGlD0edRp8DzsI9Y1N0kYl83hdDZ2UwBk9iVZ7kSSR2MDsiXjndtlYMBf2m1ezIuwKlvJk4jhjnoKBcNefaNb4JtTubIhV17Sv1EQBCiJRR9EvTrxAGiXjgQf7fHI2l2DXbszwlDdTUOcG8Wq-wg4qfktSlfk5c1ad2Qq8nMlvYSCKPjY7tRTCjpkmflbBNHno61l93F8I4-55XnJ3sxIkb01PgFi0WNKOv3zSRkAhxeS2ibRdnHtw8PA3rBcjH-MyZn5BPM3t6Ixw1msTVj4EFlaFa0kKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=SyY5KAI0lS71CccQkv6HGMm66KbFGeVbxi9RBcNIQ-Rp-tfEb3OBfftAGlD0edRp8DzsI9Y1N0kYl83hdDZ2UwBk9iVZ7kSSR2MDsiXjndtlYMBf2m1ezIuwKlvJk4jhjnoKBcNefaNb4JtTubIhV17Sv1EQBCiJRR9EvTrxAGiXjgQf7fHI2l2DXbszwlDdTUOcG8Wq-wg4qfktSlfk5c1ad2Qq8nMlvYSCKPjY7tRTCjpkmflbBNHno61l93F8I4-55XnJ3sxIkb01PgFi0WNKOv3zSRkAhxeS2ibRdnHtw8PA3rBcjH-MyZn5BPM3t6Ixw1msTVj4EFlaFa0kKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=OQblPbYGa80DhSgoY1Fm3wJ_EUG0fdFKCeM_CoF97e9LaSEYAAz8h98IT8GVsv3GSzE1ueJYqaO3c-5dDWpYevzWrG-JFwcanj-T0hEX0zYz4mBH4UhkQjcu1PMleN4OVD21xrHemrW3m4DjnmsjaHKQuAbkBZ8IQgO8aVOQQ8C0MbEwPUVf_3bq-I5cy--POSAOw6Z5NQDlw9h-1F39n6yOCR5UEMVGjp8H0eJ7PZC9Uh5NiTQ8hyb-qYHlopqruYx0Ok1l5TK9Fl1xbqh6xexNDHfp_3PJTERi_cI_N0JjGDoUV-uGkZq23yZIEtPP_iUykhqePMRuF59XhZ6fUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=OQblPbYGa80DhSgoY1Fm3wJ_EUG0fdFKCeM_CoF97e9LaSEYAAz8h98IT8GVsv3GSzE1ueJYqaO3c-5dDWpYevzWrG-JFwcanj-T0hEX0zYz4mBH4UhkQjcu1PMleN4OVD21xrHemrW3m4DjnmsjaHKQuAbkBZ8IQgO8aVOQQ8C0MbEwPUVf_3bq-I5cy--POSAOw6Z5NQDlw9h-1F39n6yOCR5UEMVGjp8H0eJ7PZC9Uh5NiTQ8hyb-qYHlopqruYx0Ok1l5TK9Fl1xbqh6xexNDHfp_3PJTERi_cI_N0JjGDoUV-uGkZq23yZIEtPP_iUykhqePMRuF59XhZ6fUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgmZxQj1JPsc-R0zDJjLIMWb9FrinfWQbFLWzrD-kKCmZrQ7-QqAVW4Ft7UR4BOMYEMb6UnllEkCFBIgumZ5WZ2ud4WwkdmDlQWmTVRUrnYFzosWy301RPLJ_rRgeQ7jK3-dP8T0ztk7yCt4OLjsBlTnPJfCT0DuFJFJRxQrI8ofOpsumOLVp3mCbFvVmUEKHkNGvUy2-bknv3qyjthkt4jAGT8DdkBAHmuh9oYaAXyLZ9Tyw_rbz-BQZ_HjCnfQXuxn3C6EQGD13pyJX2z0AAIaVqJ9Sg7HTWnBopk5prXN28fcs3CyRcBqbtz6Gmr_eobWTEYEj9mzQ4ebB4VKBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOMaLpUlGFx-qKf7qa7nUDMbFg_0TI__hq43wSQqeyvF0eGbqPOJMzWGXvAk-lCAelel-MesW0qrhKb9BQwapI3FAnSZALVRQdALdIkQYAINu9ovCpWJXvduLrgrB5oHQmBILRNQlUBQi7veJTGdL3_nle504-vZqR0oJ4zxa7SmlRkLbzjocz9m7FVU0HoPJPv6E0-QddR-UO0QXVrDov7RqPCFWSqXFuF3HEnYNI-nIUFmYDz-PXTkib9Ls8Dfj4Vp6RmFOQi9gois0wb0qln2hKroxA7J-BT5Trh7NsK_uG-1lLqT0yrFSVQH_yfHsbUyXr9FCybzHSr9GH8cUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_yittqwFNi3mhtXy4b_ltSH-nNodFqv5kpKJwCSml3Rp19VOTin4i8GFN9vTteH_3lNGaPTYJ1hRPU2waqAn7UhESb__HdoEuoZ2rdUqhOT9MvnhZO93DYqqGYA-_NkxcGx6mefNATOvo1NEbnyKABPUt6TLyjsMhRBO_IH-y8VNTIWAvGynWNP7Pr7LaM6H8IQPny7mOxxbCU3ddhLEuWfwMl1tM-eAbCbeFgdGTi1lLbkztAzwjcPzQH4mc7zw1XkVB69QzTFOqQ6xccNT5HOI3BuevmUo9MBZHKOuDT8pDfbDg6H2C8nvbD8sSv8tS91hbT-I3IASZ0f93I5Xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=FU9HZqDtfP85Kv8ABRnnEXRW3wuWKTnIEnFn2IDIqoCifjqbGIkRdG9gFL0Moy0C3vG3jjJqlhLqsEA-cd_pICC63Z5_IkVML6YNyFuHbUc2tTUmUu5Jfm6blscFFUrAGx8h9rgLNmvn7H--ODmSbyte5X8UtL3TaI5vkKyt8okckoR-ioISDvcXPzARQ43I5jc5qIh5469h5sJH1URI9r2A3OmmrTfe62hbY5A8fA1VJfiSwV0DxJJpI5y89GakcDktLSPkHu0irEO6bN53ProdOuc2_lCuOIzmE_rRl4ZjxKPgvpkw7kXsXFX1k2Kr3SkfhztmcPWJIGIcSKb8cAGQ1Jg_45ypazbR_mRumkPBZ-MwJeTgd8WvcbxeOBj4bJK3SDe45PnrZaVcxUf-9RIbx1XaYLv1fG3sGYCfKyXLTo1pAxxb3y0cyrVSJYeeBDmE6SD312XrFZbnMe93NAF9ZWRoALt1ve_MiPRmlnuzaKpMRq6_AQEcKaEBouM6W2Ja3C5wycHkGA7QjFMVkUGA1EjRqNTE7b9wBCzN5CeRyiNnttmJUxwXjyHwsYf9rwjpU5vtaF52is2vIG535KktXN4fo8PSfAsi9mh7tXuAyyupZhPzfv-Cng3OFwU_625BxYTIf772C88HBqc5IOXHdt2Rmk7Jp6rdDWuCL3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=FU9HZqDtfP85Kv8ABRnnEXRW3wuWKTnIEnFn2IDIqoCifjqbGIkRdG9gFL0Moy0C3vG3jjJqlhLqsEA-cd_pICC63Z5_IkVML6YNyFuHbUc2tTUmUu5Jfm6blscFFUrAGx8h9rgLNmvn7H--ODmSbyte5X8UtL3TaI5vkKyt8okckoR-ioISDvcXPzARQ43I5jc5qIh5469h5sJH1URI9r2A3OmmrTfe62hbY5A8fA1VJfiSwV0DxJJpI5y89GakcDktLSPkHu0irEO6bN53ProdOuc2_lCuOIzmE_rRl4ZjxKPgvpkw7kXsXFX1k2Kr3SkfhztmcPWJIGIcSKb8cAGQ1Jg_45ypazbR_mRumkPBZ-MwJeTgd8WvcbxeOBj4bJK3SDe45PnrZaVcxUf-9RIbx1XaYLv1fG3sGYCfKyXLTo1pAxxb3y0cyrVSJYeeBDmE6SD312XrFZbnMe93NAF9ZWRoALt1ve_MiPRmlnuzaKpMRq6_AQEcKaEBouM6W2Ja3C5wycHkGA7QjFMVkUGA1EjRqNTE7b9wBCzN5CeRyiNnttmJUxwXjyHwsYf9rwjpU5vtaF52is2vIG535KktXN4fo8PSfAsi9mh7tXuAyyupZhPzfv-Cng3OFwU_625BxYTIf772C88HBqc5IOXHdt2Rmk7Jp6rdDWuCL3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkDd9XwEHvU1rZOfTWt2DjCIODWYMqyw1-7IDP-S5W4zl1YnEneryjw7voThp-l4g7x_gSFAo59JL4L1L51wGzT5psGWvYlQXXfOvbe0cMC0WX_9klx2kHGQ-S_3ghaekvaQX2jFOvlRWMGIL7Dxr3moB1KZDLnR9S68wBkzZEfH-Or-eM3384TaWY7Bjf93OAuTswHlJRuomZwT0_odsKZNypVPq6ULkg7vjwMuZh3DwvpYV1UGCPK0b9WazfM9bo-lP7jL28nySdKmvd2NtcEe9tXhXjKj_ZeypaHDt_kZ_K5UWqnngWuU9RFBzNz8rQ2Xn9-UOxzu1YiqMzILEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyJpFnEw26DrhxIOYt8BPedaBrZlGBvOVU2oGXLz0SaTpcqsCOFjyKV77hmd3HN_1wD2fdD5VF5RXc9V8Wd9wiVPmgI1HgJlnaAxsQULfDWbSd1gZGLV_oAi304N-kdx1V8eS9Cjshs7ktJoBAVCUSHetFCS6Q7xpKMIO_A9jYXCFGiNNnIb1x4ZGPJ7VvwaetGwDKl0Qx44JH8_xXDETdmCP1iPS0rqScoPKtMjQEp9EKTi3UsRntF8OpI3N2WcfONuxIxYYlnbHlwKOBGX-eXKAVHdLzg1A40V0R33TgU23BBxUWt37O3nUmnj7u_9HAD_bE7GRV7M12lkh6RBEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haWO9HlRj_i1Xj9ZSlhlYWdWy8_SgSXEBXqxOBNnXVQQKFDsAsBXAQNaSXgHuzTLU3MjlzLW5gblZuA6FeFb3cX6rPajTXR4XJKdWXdACRl09hFS6HtvX7a23dMYlrWLuTThPkW__t0ezYFq6HL8_nklezV_P_o4aqpQBFmCP6aanK40YR5OwPeZrNaLPorglwgujCt58qIFbG-RpTgjL2XND3_pzvREwqujVfSkIlL_bWUs5zt7yall8H8B_uud10HTLRs43Et-1xwKzBxuGCxWP8j74B10aqPisSqtSnNDOupbcqXAeN36hY-L3BrC2YRU03zBU4nL49ZIOsEv2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eglvWEB2r8nNRBzWPLhbSFnNpDBa8Bv-s8kENXD4FQlDMuSc0dxxTNAVaKsyGV5g9JbUjnV3wh9k_XNSu_DSW3NJhRyRm0dHkNA_kBHuEJY3FGVH01c8Sg60eacFKZt0I7zhXNMMlUfVT-J4sO7khAK5ibUptNbIcWea1o_zGw6kSUCcX2mG67WST7M-69iJzRskYnghaZRah4RLBkszdNFCH6N-0vHmrGkWntziju8Te96CWSQHzMzhiR8iAyqUW3KSrcr5D1h4xFuwaY5428DhaRmcg7KPz9G0sYHySLSrmcV_YUoPyHAf1UL0x-VLdj4MANYlq0z59RI8h5u6HQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6ZO_Yb11dWMu6ymOUfKQtP4Wj3_i3JXL61Acxmz5rem254pF-RF2r3BcYzqZeYce-CDeM3ZdbSqt10C8bymi8t4jo2Fr1nq6Fs3_Ax4n4NnpCEjs6JDiWnxY95tIeo-Iip2z8To8t_oJae2d3IFOaCoBfh7XXvritRZL6nAT96_bUOmDDidgyQUDHE8eCQaxr_sdtFGcfwQBH-909uJaYrfP4-5cwAIEZFNyqMJ6Bc3IoyJ92Jyec9u-UcvNK7f1xP-X2BzNlzTkLDV9QSRD-4eN26V7v37NPexgMQMV1CAn1aBbT1daQlj6_-KAAkdituly-WTdhjr8d4tjer1SA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7534">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efaTxBz3NErpuprR1t3zY1l9hZHk0RMQw4iQSoLKL_BwhTXFAqkIo018hfTYHrYu3Cb5AhmiYGlc2B_4eV0k7OII2-qlIjJ9uEBcdwb06Y51iOzd_r7bhsuS6tpnqgsxJXLB5tdqyZchLgYpn_6XcNzucVbQrP-1Z9Q21raj--TekR8GTIGeNtnLyyAFX5JeQkgTZ7DZWHwDyN7J5WN_DXnFrkXCxf7rCORbeDt-whucyPDvTUAbamYNysbSFBC4R2V5MtIauNNo14VJdF_e4VoErlCzZR2ttR3x-jPZbkoacZ4qO2KVytXuU9RCwfWC5bN-hjMNLHAXLQdcd50YQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=f9pmts5hTbbXG9Ltu_cQhfUvEJRUieeSHRc661ccTuu3tn5KSKAdSrWK3s3x5-ZK9HGT5XlTpxbvsJxxKipUSPl1SdozdtShD-guVGamK3z8jKuUw2rsWWOGkK5fKO5zPLrdUVYDhFtwmfwKs2qhD_3vVr3vvXOmysYhfr0GvRrZs71vLzfbnHai0GN8Lq25nRUw10ms2T5Dfp39DBvDg4vVWSUu4VJplKstchy1HJqYS-XcnsFViEUhEq5lzTcjHwKLeKP_lfq3PfIfmPHzYux24skL5je4vJGYqS9OrC4p-2XkUaUNVQJrZ0y7sz8pt_pT0iRu2uJDLW1rrvsC-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=f9pmts5hTbbXG9Ltu_cQhfUvEJRUieeSHRc661ccTuu3tn5KSKAdSrWK3s3x5-ZK9HGT5XlTpxbvsJxxKipUSPl1SdozdtShD-guVGamK3z8jKuUw2rsWWOGkK5fKO5zPLrdUVYDhFtwmfwKs2qhD_3vVr3vvXOmysYhfr0GvRrZs71vLzfbnHai0GN8Lq25nRUw10ms2T5Dfp39DBvDg4vVWSUu4VJplKstchy1HJqYS-XcnsFViEUhEq5lzTcjHwKLeKP_lfq3PfIfmPHzYux24skL5je4vJGYqS9OrC4p-2XkUaUNVQJrZ0y7sz8pt_pT0iRu2uJDLW1rrvsC-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCKnWwT7NhfT9-7PkII12Ty_tD0Pfjdxv-1FaIqL3YFMvEjwDh06XELvKYJq2kcl4j7yUdVw6vd_D4W90lN9JeagNQK9A0dJBjyFrIVA8sl0MbN53az4fhSrVhXJjBO3SKh5JIds98Sq-3kU68ChRXxTu0OCD1cNFDdfXGqhTWB46j9BwxU40_k-myGLkR4-dfiIOG0SIVn1v1R2pgLrJ_QilB4_rUPtWPzaTOYtF8a3YxDAw4GIBBpTwtuZZdRhqp6soojw8ZWAiSpxITD1ddaZR8NMA5C9dqFUVntKnZRfwMu7B8KgCTthlnO05VPgXe1EvTLhHTRWz4grzGOMFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9NJ7V235Nq76HNdSSm3OrmcCeoVnDpnb45pOZQguduVm1xt4m8gcJTb7GxWaA9TmX-sUd0iv_6xnJE5JzTcG_UMAgTmj7AZZyrvLsLI_2GXsPHz7CIJua3amyASPegLOSj8-bvJkKjarXHiqBlI55oJvyKlf1IgOgv9WWA7gIEeBDA47CjoYXow8dLTiqaVsam7JsQZxS-5p95eF7H5qAYrVO9E7QRoDdFtI692oXQOASmRTQcOTXC7TE349B_9VIrmc_54NS8zgMr_dghYpo2V3b39kSwlpRh8x2AIwEur3cOae7RfB5FQoEXvflhj8vm8m1Fu4UMkuK7VkDgBYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miW3Fhnvemi6uG3YagURLqjMvqwJyiqXfkJVVIrK2SVF_rWCj7xqLrd4LHCV4kPstMQpQ1lqlsqUV09e0o6MlnF9HMFey3sAwjt8H1c-p-4IDQKj8WYTfJrdP6rA2-eS4pLcQE2jlwvhcOEMXTCecXmTqSkWsTxqRtm0lPllg9EIAHrfPdpXSa3NcxQL7setjwJvIgkfRmh6RIeNzJJeIC2A7DkovIihEjvq2Uc0NUqJ-MujPe7AHuHzop-kwYzVWKv2FY6vqYWlaenKTgTS6cU-mjm0Vl9BNHhI3TMeWtOAzbZGDzAWjjOC-cA6HD20DEtrukU0aowO1ZqB4H38lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AO-zA3yQzK6__TVHZL308ekZNeSFpTbqSnMWcBfswwY13LQFJ5sFcllUDRGZAwHWMJqShwvsv-46EvA3G1L2YluY1fMfzRxOBi03YVbOYNR8evOEmGF1QVjABNWFeEMYmiyACIdIGmzv2KNe7BxqVwQU9aLkQuO-VYL2tnqNG8Gbf5rc6-_aa10Lp-VGo3es4JZr1_8LMe3EATcT3rmWAmQSQHEcKJIPXu2QyhzqGA7xQZa5MPOaZI8-jXwrUFdIHC_67Y176z-Lnwdw3D36OfxYVWWkk3SDGPysLKMRIeG3VhcTudiu8V5KMEw0lk0UB6Mv-mTIPetTGP9Cu8m-5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7525" target="_blank">📅 20:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7524">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCDZATnABoZMUp7q8m3DND8P-xms3uwqNshWEvoMzGpeK6P1_K8rU54gKaWZYMafYgdio4UGfnjcbuIOKJIoSvncUasr9HTqyWmO_7Q31BiSeJxBYzaWEKmGLYPWUY9uffnju86bQyRtQZMiQzE5kiSrICz3lnW5jFxqmcvjxiFEu7rXv0WIre_eT2Ik0rejTEJ7PqbeEOGMEd2XkGURvedc_yS0dcKaHARGzR-p61qCQco1k24JuwievKMBwXbJzl3_brhq0dKiXgvj7exyYpYpICMOJDsyIvO3yG1hNdKg832zg7IjBqrdD9kODjYeOhm28S_6OL5g0A8AGaMBLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBNUFuGrRqrXOX6psdU5LxCF4rxw7qTkLLazPSSI_Mf_Dwnh-H2t_AIVp7N32Xz-EXUgDzvN2uaT4TrN7c01--JvsDaYVkJvCv26qnmcnZynSqzpYH-i3gxfR6jC9LNPKduA0ed53TeEu35bpzvlXfpmJbHWi6ndZuYGW8u_GTthvwz7m8jtLYjtDAXVef4RRS7YjwVmebyAEUar66-uTW7jkvU7BIfy9hC0CeCCsmiUl58pec7cxmPgRILLZpoai38LFHewiBJRGm7oe7BgWIfqWct01m1UH1SUY5liMx7gFLzUS_rtNiaN0y0zAgZUAOweePeS73bFCvvH8LG3mQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2MYyxYhrtjFdHdOJSx278ZdC1UDRo6stCv1BTdQWsDKGSp0lmIf7oawHUj98TARIPmB-6mYZfsyr9Z132ZGi46bntbPBP02_6icD2-FjSwkNR09QQNlKQ9sQaIrlGrgyJJ1pr6Qovo55TGvNe7BUFJS9BdA2mW_1Q4lHv0sa27WHNaLETI3jAGNmcFAN3BK_vmbIzquYFLxE2hF9nih-gjCuZmM_UrIZR3k4oyS9Up3C6TfY-2JehAVLLDHa6ks6r4_RDCEh_8R1mRtuBzoEQWsG17WGwjXjHIl0sW57qko9qXI6Pf6cUjIFZaAnV8MynQ-QQMBLT0Vtqkhs2toYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nibl9HZIDWLWYc5uPqSFZX8HpK-5t3CoSSY7gvPWUnL8D4-JlUUG7-SnGjHMkBXlz_hhIrAVHHYBXMG6XiKZpIzSB-rRbaoBqNGhYSkw3XxjhQhZ0Ftd1QxnUZ90Q1FPc1SrXWx1felVMBDMvPirtIxeI4KrNa_voGUbcs5gY82GtoWPeg5qc2Wj-7RuBkCFjzchQT-wA35HsPg82x9mq6QnS1fGeNEUVTwe7dRtnriauUOBtCuFgdyCGqD4W5PFzhD8RCgijJrivctpFjiscC_HJBZtnaemL53jXlUD3eaLVkoVpmYJ8csdFUmHFf8C_pBmmpZOKIqYoIntp9wBwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGD8jRD_VQr4q9R3FtMha25Ic_aXX9LWYaBESx-K3Fhn0bffRAJFQ-s2t0XXX40BG7wvaGAFLsJS_VXxPa6GIvrpWFnxQSHOrSw8DXtiV7rU5uXJ8-ENR7PeUaVhsK6TydZdeenpbp98SaVa81Fc48ZxP_0EyCrbjQA0Plw-2sNIN0Essmmitip3DIW-eMOwTlKrCynjhtGu19e8sC0CYRo0ZN_Efjsvk5oz5hjq2vEnzwymKuQM2iPMDrwRm8jCsGCM0EHPLZeHfgYlpsIXHfPGReAK3Z2w2biCe1QV0p2qbLlvFxF2_jkCqt3YAEtAQ_rW8FPAan461p5DC6k8VQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=Fk6Db-HbNLY3kmaGo61iRzseum9kkBdBcmXMWw0x23AlGv0OQkySpUwEO3cOs1Sgqf4UPIRfG8Z2XgFm2QPhXU5wqq_cQsRpHDjBCZ0u8TV5yP_wg4c5kAqYpukvrts8ceHBBvqFsi3YlLlCmuIEtoHGgxe52rlB2SrhThQpMk2ob1xsV8vavIDDA4TXQNgOIpf6bjZG24bag0RDexzsz8DY7e3OV8G5dN_F-UkJlDxei6mOjcnZjc1hgoeATT5dfjVgWaPsFZsm5ohtj9FZDktK0pSP3mclRlVOZLtwYbUlVMtUs7P87bplJc2-5Ug2GoQM6qVe979ysGUIcPR5w4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=Fk6Db-HbNLY3kmaGo61iRzseum9kkBdBcmXMWw0x23AlGv0OQkySpUwEO3cOs1Sgqf4UPIRfG8Z2XgFm2QPhXU5wqq_cQsRpHDjBCZ0u8TV5yP_wg4c5kAqYpukvrts8ceHBBvqFsi3YlLlCmuIEtoHGgxe52rlB2SrhThQpMk2ob1xsV8vavIDDA4TXQNgOIpf6bjZG24bag0RDexzsz8DY7e3OV8G5dN_F-UkJlDxei6mOjcnZjc1hgoeATT5dfjVgWaPsFZsm5ohtj9FZDktK0pSP3mclRlVOZLtwYbUlVMtUs7P87bplJc2-5Ug2GoQM6qVe979ysGUIcPR5w4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7509">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWxiajptXfVfNotFdn-BlhWec7oflQ6RUs8if5WM-B9JU4NVmGg-JtSANGr0R_KB_NIjRiwduq3y8VlfPEmMgpnNAu0pv-aN9hVQcQ2MQC5VPsm4sZIv7eio5dVCDv7SV7PFvX_FELUHc5Nz5xQqs6YT0qR0z9fJGdcOz5eQi8ja3JGWSI5o46_wZtzuJTIqjtHm6WmDUaBCdMd5i5bxUlf6iO13HWaRhzxjZymXZaiSMxCgzevRrCGqS55FepIAzLuWtvVJ27FAHcw-uDq5jl69J6S4sK_sRYda_JYfrwdYHDi5Rv76f_XQf8KMtr_1AJBP21TLAaP85McV8WzN0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7506">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMfO4nQyO0wWUeiGNK7wF7JYQ6Be4t9KF85WlFM3s7b4kwtwJQ4Uv-DGzO7DHqvQuFiv4rgK4Rp8VMDZ3m82CB8H7JjdeqiOb7W2L6k1kw0DUukC7N1dHXHBaZ1skW98MUjihByffgdvIiOTVQekI3jNFfu5EsOIdhW625lhNsfgmtmCxVjOzj2OhKapernkmV-50yzV-zWw0cHDVv51OTjAHDvxjZYh_HwQbsDzOZvQzLW__tmVGtBDll0NZ2g5a_fVNnAIkf5sR36Z6YSsdGNu3AHlqJykJwL3a7Ea2FmJ3w_JBK5sMs1ocUDqVIbj_joz6hYu2Vw0oBgfnKXxfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/us66MvfQnnaCE7fvCozsNK22H4Aw6E_unP8qM2c0vR7EqqneAuteH1a5plT-m-LBp7vz9B0ApkyraZXVJBSBQf8xjF0sHtE8FSIZl6wUULVNVALrKxWcuB71yVmckTF6F-ocSKnnKKeOYJ70JFJxtLKkmedhUWWrydSgf2ctYljWekGAYwWLgVkp-jSvcwBRbYHRar9XXgjOxMzdY2t1z_bD7JGEZBlKo-niBhIFtWFpKKOTCuZm0N9WdBEsAjM9nMoJgmdqncqGN-jjkKEum6O8fcnr9b273wWXlaCtgb1s1hOV1CiArZfzic5O0bMnAJ7jy3FSzKginSlHIa5BNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/ArchiveTell/7504" target="_blank">📅 13:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7503">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5PEMG-Xe4LbxfU-xNJfVUEoWqQyh4nXYdYxbuAzmQRBWkP9IMr4uTC1Hqy20A0vDgG0wjsRJOGBa30E0gVUnatkteKEDywV99mlpRxNANSgnkJhV-WgEogQf1BbjduIJ6QM7Gy4BOkhu1D5HZkZk36webo6vl7ekfXUO7y73rcF66j7jjBtwwqVW_SS2HhL8pLaMmts6Zyqsqax9uYN09iCNKLYra3VUxoS1_NeGWQmdzPGS2aDTZkFB4n7AknbZ9oMoDbsXhPxHxSE0V-IMxxNUFP8xS8nrV8UE0uX8mHC_erF2H11dHBIuFyA_ujxlnBVIApar2Zkq501Snf30A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7502" target="_blank">📅 10:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7500">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=lQqMjkcLls2SARYiH47P48ZMcw4A1cEmhfx1-sHjTHd9pqYeMsR3Z1m3FbseDb3HoGcj1zMDqTMUPnz2oIzRjFLlIddMXgWxYwCjj1qgMcUYtehaIj60nF66LbBSqVusDwJO2NyRjVm7CCnr3ykuHMRzdsERRyJzDb4iih9Qv2M-Pw7v2CehHJiSq1bwNDCaqWQf7HMqX85OA9teyO0guk4wzeIkM2aD0BavL3eNaoqtIbouNm1zrJcKCh6-lNcK34K1lcqJgUV4KSYiBcuKG8Dm4o--izkR7NFob63erp81MaxIyZRDk5yfVuAnZdzJVM0k5vlcS9C_1H05aizMxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=lQqMjkcLls2SARYiH47P48ZMcw4A1cEmhfx1-sHjTHd9pqYeMsR3Z1m3FbseDb3HoGcj1zMDqTMUPnz2oIzRjFLlIddMXgWxYwCjj1qgMcUYtehaIj60nF66LbBSqVusDwJO2NyRjVm7CCnr3ykuHMRzdsERRyJzDb4iih9Qv2M-Pw7v2CehHJiSq1bwNDCaqWQf7HMqX85OA9teyO0guk4wzeIkM2aD0BavL3eNaoqtIbouNm1zrJcKCh6-lNcK34K1lcqJgUV4KSYiBcuKG8Dm4o--izkR7NFob63erp81MaxIyZRDk5yfVuAnZdzJVM0k5vlcS9C_1H05aizMxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyI1vFcoyblBnHX-wDSoInloJs6HTTmwrKCIxJRL9NOGUu0ksotP5apTyjt95XTzDG5erbNXnXKgyrh4c2zncBZTtv13NfdZmht-_Z7nP_CYscKEBppo8EbbY2Fn4NZxv-OuVESZdyckpYzVorcISXVXfu_Ba4jLk17rfmT9p-jqjy6hJD5G0yOvyZkBZ5PL7ivKvmOXxhdi4Kq1FIAzwGcZvCRacCgBu_2qCz2noBFfMlk_X2T5Gz-dJFD2eAN0D9lGThOFLEOkuD7xcvFRHs8NHGyh5UZSIqXdhV1E4s6RxUqmqkZPwjPK7oDbkgLkQ2M1KXmrbnus1fz_f7caAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=P1-46Nt57h3V1HSaJ_PsZIC1cz1tfDk836XCtM2Ap_V1jtADoYlo_mKdJHVpZoGK8LFrWEOmCHevRqsB3wUJ8lyAkWgpJopzCGrC6Ba32Oc5merLTNkgQ9uUFx3hr95U3D5aGxAu6rYsCJIcKRc4hgovvmMaO8Ez-wHiyQP6Ltmg_fYv_fKazqqTpEu0wkxXkf-Ghd__xfLWp9dSnjiS6RZfrCujkVRjd4Z-RFXwofwATZMNuDQVueMYY5siiX6Ltswolki0KPFhHV0kN4a9qMveWW1U0q7kDQybxzdjcIxtiM4-32hhL6CQPNXyDdunUq_3wV6XZE07Zodn8vtqbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=P1-46Nt57h3V1HSaJ_PsZIC1cz1tfDk836XCtM2Ap_V1jtADoYlo_mKdJHVpZoGK8LFrWEOmCHevRqsB3wUJ8lyAkWgpJopzCGrC6Ba32Oc5merLTNkgQ9uUFx3hr95U3D5aGxAu6rYsCJIcKRc4hgovvmMaO8Ez-wHiyQP6Ltmg_fYv_fKazqqTpEu0wkxXkf-Ghd__xfLWp9dSnjiS6RZfrCujkVRjd4Z-RFXwofwATZMNuDQVueMYY5siiX6Ltswolki0KPFhHV0kN4a9qMveWW1U0q7kDQybxzdjcIxtiM4-32hhL6CQPNXyDdunUq_3wV6XZE07Zodn8vtqbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvewONXlWxa0X_FJ5tiDnPlCn5-Ct_HbyvBvxu7jFn4N6y0697NM8SbGenIp0DaBABD5mZaGDLTTQrFGhf-iafODGqHhDtVTOWqUOxzqy9nkiPEUz1T6CQpmDjdSptUDpjRIpY2GP1r-AlXG-rLY92YzTYC1zt7P2SuXl_koCyA-cYKriH8hiA6amArpBhcy4vFQpVuNKTi4J9IfoQ8zBYrGkKpUaq4ezlprYcMI9ePskMyxOO0v40Pg_AaAB9mu7HInq3EQZOfYqLdl9OicA2q13bKLlEMkniwkRznl5YzSW26bn-uWwdCxWAdDZZRcfe-YeKX1r_hsNijdbS8AiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGmnTy6hpNCI9rlm_8A9Kp7Ykzf8zdbdFNvTRRDftn4_TyLTXOzMs3uSPDPFhA5Tp3zoR55mQa1s8SdauLm-42Ckp4e2Vey2um1ufUS47UIHpap48VMTyisNMegTbUB4HjizfQOEtgksHVQfxzIx9sLpWsv3pknLVGifNs9kRu_8rdycNgWRGf_G9joZVLUEC4_QSxnklakNqgi-VlIwkceVEXGytUiTY0maTdu8FsSsexsJ0JFPjhtMITa9GEezIppKM4mOenV2aQU5wrNkWy5sqs20FC_Ka57Xr9xoj04MKAvGGBdyjlFfBta3ISEQIXt-wTHaZkoZxN6h6mrLiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=rjNXjVyWVvnZ7aKAE6wtcE2pZPkzS4StqHOq-87Y63_hLVJWPLj3lI0wi10BBjS8gzT7HXx0qUhXyGOwvEyS9sgu98UYWilcXLrnkXlcz7bD_dtOn7GvxvtbsYOGtkCJlPsUKLQ57BARMujf9djhsJPKsIcj48t4h2dfwBU-2I9rh8kjW457YgKprInys16scGoho2so9Pava96ILsGRN7D5cv-Qpz1WLar0DAsnWuhe_wcQ5-VK7WvF236dC9CkRWZh1Ixl9FR-8lBZSP7n74rXAb1Bj5WHBFxlUlLRHKWGq12Zqji3BZMdRrATUvKr5G8VES6keaup-mYy4rjtqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=rjNXjVyWVvnZ7aKAE6wtcE2pZPkzS4StqHOq-87Y63_hLVJWPLj3lI0wi10BBjS8gzT7HXx0qUhXyGOwvEyS9sgu98UYWilcXLrnkXlcz7bD_dtOn7GvxvtbsYOGtkCJlPsUKLQ57BARMujf9djhsJPKsIcj48t4h2dfwBU-2I9rh8kjW457YgKprInys16scGoho2so9Pava96ILsGRN7D5cv-Qpz1WLar0DAsnWuhe_wcQ5-VK7WvF236dC9CkRWZh1Ixl9FR-8lBZSP7n74rXAb1Bj5WHBFxlUlLRHKWGq12Zqji3BZMdRrATUvKr5G8VES6keaup-mYy4rjtqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
