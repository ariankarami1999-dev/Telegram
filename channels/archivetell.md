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
<img src="https://cdn4.telesco.pe/file/qWs6pjhsVJdijZsrv_rWX29v_ecs7GJixGnPvnN3YOcWG6tC5cc62XMRjGeYFDxldU8xt3J_8td49RQn_aJf0y60gwlkcO22vPRGDumOfq7Gtj54EuL9dnYPA9CKwOrewW_jM-XAPDL6ILZipM32LjshESbAk-jVWaqqsqVfqwP7i_rW3rmBs6DIoBCWiQUyUz6BqEUyy6d3nhzbRWOzrBS_VCvZeMFdH5fqAmGo_UEnCMocpXjo7ycfgKFLWbNWxBtXkc5exSj4smh9ypw_D_B_rUuaiy8FYcTV8ljh3jaYj3nyIx5nke1sDVT4QvgzXZouLa_le3lZZHnBd06akA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 05:41:16</div>
<hr>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fagPndPSGvC6-nAx43jA3_g0uLhsJSTIIlkBFRudAafktrIeJSWUmEdXWvbYu9pz17pJ2j9E6P8cntEkukzDeq1uJ9GM-z9QcC_vvlv8w_h0C2tj--NUS6GT2ZXOxlMc5z-u-lpsVO70fT8IyG3mUgRfFxOnMzNxDzQ1Nkq9qwwZVb_15_zqg9W5ytmz18jMlirJ7a9N79rMW4swtMR1w8gMwo2dGVyXr-0kP4lixVcFFl5m70xsDE9zyFjNVA9RD3J9YMv0uBKdfws4vVfYFc-WSkv0CIBpD4ysnIcUzij6rPToIoqI0jP2BJC3x7t1qjy53TGmuw-wVH_cEhLp9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7517" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7514">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdMBFrrsBjMbHOEw_whXmk6G7q91oI4foJhXpUOQOx5ob6My-d_EYk5hI39L2JvdsCEl9EIVVJ92-4eDhvuhRokb53Ew9XPJlwXzAS_jxvYPDWnFq5KpSrw4t0ECsvB9OlVH6tC2RSfFnMeubxGlepRAV9U3qy1uJjzPAu_4NMeT5TG5W4LgqH2VCLurs-Jx6EDS8hzMYJ1fploP2zUQ36fup-RNsAC5Vgz2jQhvyxngCTmPQSkuxCNz08X0UhtsyxQ3QJY51cbwaExvOGnzXvKl8EprbBjbCcjRdxOLloYmZig5PFzMRRXUTb8QNmeqXy6eMHwJzjSXngB34nIqEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-hGUyVr_I2ArcwQgnL1RuKPDiiiEr4W585XYu2Cs49LYuh5AEJsPvfUbW_bb7SRfNj45VfnlZknXzXY850DQvfJ5syNhcMyHvYRyYYcycv9qPuSx1xCl4w2rrKTPq-UeJPUF-40LWaAPEHEcR9R_9LfG4pYZg2G1SuA-bvJhbJyoWr2LK3VCkd9tpttyRxMuy2tswyXroiXpfN7Y4Vu_De8JZOV3-cimHTvt0R9WFx80G79qjXwX3n5Gw3GYvSmp6thFNe5OlHspnCMAeiJnF2VneXqo6EliF-OIbmu7A4zqxn9v52CqWBFEcC598CRjIz1Zs2PQi1-6fmJPRojOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=fzq5B2XW6YftYx6P_p6p2s61kvlOWrAGP0pK4PCv01jmkPdzyG44wZm15bm8aa-U3gXjWnW-ZZ87yBr-BS40r7UV29jWgmT0qV8cGGG1i6oqGfWEPjh5qifTqqnUyXWlIUBlS9319X6z71sLZPXfiqIRWXOuzcN7JJZw6uHazO8ZqDFanGpQ0-iq14RHFOsDv64cwzCEJ98jokQ-jw1pxRFXcBNpboR-8SIywCp6fYP2gy2zxUr0NAaesHJlUWlYS15iS3a76ggwp7s2rb5RmTTRM5sK3k0lrq3dpl346GGw_VhrcUqfvUio24LdU9M8DWT3oduBSZ_SEtvCGDE-noWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=fzq5B2XW6YftYx6P_p6p2s61kvlOWrAGP0pK4PCv01jmkPdzyG44wZm15bm8aa-U3gXjWnW-ZZ87yBr-BS40r7UV29jWgmT0qV8cGGG1i6oqGfWEPjh5qifTqqnUyXWlIUBlS9319X6z71sLZPXfiqIRWXOuzcN7JJZw6uHazO8ZqDFanGpQ0-iq14RHFOsDv64cwzCEJ98jokQ-jw1pxRFXcBNpboR-8SIywCp6fYP2gy2zxUr0NAaesHJlUWlYS15iS3a76ggwp7s2rb5RmTTRM5sK3k0lrq3dpl346GGw_VhrcUqfvUio24LdU9M8DWT3oduBSZ_SEtvCGDE-noWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7512" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7511">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7509">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7509" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7508">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiEomFhTbIkR_-CQ6Uj2SWp4rJoPe0wCbW9HMh1KjvvfaTqMfA7EAVKpd6sWH6To8VMw6S0WdV1Pzhkes9j-JnfxIXuhkpWaW-rrQy2UkBKxH_6BKYtCPzoammQxVnJ77uDA9q5OV4xYOXVQQzk4E3PZP22BlpoNLElzTT_HHOjTygYwMjnaeAvFJdlGmU9VvKc_mIEJsUDEw1Cuk_E3wDCFkeZkJxGQNfsX_buVk4FKcHd7dyEkI8yPUrqFA-V5PaJnNlT6QmvoDg_ODAzWDgqxwNjA_ESCK9YAvK5YA6dODmF70Y9tfMOSWbdwl8N3alRbDYLnwwFvlcLBrR2unA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7506">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7506" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7505">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYMbxbTNQVyqO8c46US-XgfQ3u6s0rZI8sqQcbvwVBVHWs-TdpS5euOlv6cuhaK5zDW0-U388U07NXMrtYy-T8MYn0EgdleONlxNHBpvKJ6sfFRh30wsJmBnu4G2Lowh4RZY2oZsyjJV3YxiOYD_i1bguWQ5hO8yPi8SKAoqEFW8Xuum46IbQyX7K5y22hE4aHJhSOgl7UdhwWgwILR0IvYPdfj19hTdTwC1CZcLlOKM5t_aTBbsTNnu3he7x6A3sqYo9_Nalyj0fT0V3Dw7RFTOgk3fhXnotzxAlyZIpiYp7UJmtxMcGHGoDrXdVkFAc6HSSAETHX5CpdouAu8PeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrpQkEfICJUZ_skvNni8BOVH8I29vKcSQ2AilFndy_cUmqcWGePjM1CgZfyDibvrBmHZSM3pxw_MoVG8X47o6QPn3xnOsYAGNTud510Swtdlk7K10qDZNl6KI1EpGcPwgAQtjo6t47sNaIltCicuVQUBXUuEd08sn0EIgrqAGXmCMdx2ybezHzNPExcjbAXcNRe9Om_AQgli5XLUKQry0TFCSIYv_CQVD5MwrbJnqDV8Yqy_VwLAxQArc7WspPrIEAnfOq_9d2lFaZAS5in1UT6wHl7UnfTZCVKV1i4cqSrJejE90sqCEAi_KlR9J4D8Nn36sZxVD_G4zM8Cv6SYKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7504" target="_blank">📅 13:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7503">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7503" target="_blank">📅 11:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7502">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sa7TgEElH9erpdQ_uEfBdsRlZUz3FJJzzQU7VQWPNHW_-m1VXUZAHdlWaCvPphVFduRmvmTrI5WGqmbYcwlpYAUaNDkKZd63uWTirz1o_2ZjaKFIhnx1ID9khSO1zDDAK-E0CDsuFAXGzYdoi-JWBr-m97H9U4Dh2pTJDWNOJlfNEY9ArrUshthFxR_kf5ILK70_L4nV53T3RUQ959b4ArI6ntRdBLdG72iGetN9y7WvojT2JPZVVmqgbdFjcI6Db-gDJKvCppOgehXuLWSGAKxLn2l4Wma5dBBTZTbu4TuClzBqwCzm8Upmd_fqFEbCLCbUI8wbZ7nmOdKzhnUiOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7502" target="_blank">📅 10:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7500">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=qWwkvfxexk-XoHR1wVFM4kZUR4PU_v93G84ZY7Sjtaj3bVf0TB6Y4Iznficq2BNCZyjDezv9BDV4R9-fVXEKTkPxPOMoa0yXXEy-v4mXGzd0EaV_BvTBVsdyFzAL3qVKw-qJpskooLEhf7mZ7nusRz7_GeOPgw_xvS9_6yNoCni_mtcwMeM5g0x2Utxlq1-K2DrTbJUv45ijTZRq7gVD7CrEfThCDf3v7VnmyfBjUK9jH9P6VKDcPmWY0LK3tkbU_CiyA9ro-usJ9O1MypzBBVUkfWR0vCWJmpDWj5D11vRIDcTfTOBETEdNUF7R-eAx-uZ3X11Q1gMzXA4ItdYbuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=qWwkvfxexk-XoHR1wVFM4kZUR4PU_v93G84ZY7Sjtaj3bVf0TB6Y4Iznficq2BNCZyjDezv9BDV4R9-fVXEKTkPxPOMoa0yXXEy-v4mXGzd0EaV_BvTBVsdyFzAL3qVKw-qJpskooLEhf7mZ7nusRz7_GeOPgw_xvS9_6yNoCni_mtcwMeM5g0x2Utxlq1-K2DrTbJUv45ijTZRq7gVD7CrEfThCDf3v7VnmyfBjUK9jH9P6VKDcPmWY0LK3tkbU_CiyA9ro-usJ9O1MypzBBVUkfWR0vCWJmpDWj5D11vRIDcTfTOBETEdNUF7R-eAx-uZ3X11Q1gMzXA4ItdYbuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7500" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7499">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYnNEsRK-sJia-PnA9ciitftqUKjsNm8oUIM7Ek_AYMJSaQjSwaGria3PKl24yRyTwImscVXOtQ4lzNEsApfVo-eYnLZh0KIYvMVi7-y-Up1NMtJgVS6eNiXpmTTrnpzluIfo44mMkgUlRDd0O7-39civI2xiIEwj9Gb1LvnnpX2rXyhq9J4rqHjVVic52LYuE0YaqYHveNF_CFOvOG29Qv3nu39bSgbwX3OYydxNevbzUp3O13YEpD3pC48C7KVlFVwm1cIG1fPCol0OAeLuBcJMx8vH917pbKLo3IPCr1yO2BHgotVBWWmzkhmxcvh_SlDpX3xCCZbe21sPZjXMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7499" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7498">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=t96UFFEt22CNdPRfj2asvEtR4TnYo_RHEoJjzsAwARyMWoCQLTw3aMHOzaOdqqu5AHF_aZiYiBpHZQI6YbNzHMfQIFwqP3szId89ZPAEk3yKMF8v42HaIE4O-tMWSVbEpVhCfsu_WDdPYcAVOhJBGO6jx1yKg_0WlLb23PERau3KJ4MeXxilRieHSSrSyGCj_8mflY8FvTh082W7ABcgyeQOLlzRC-CU6PG_A6T6QJ98yrZNGIvTeiLBVGD0ypDCpa0KdmHuiQB0Rw-tIggUwNZEZdE1jf5o_GGlFkgvGojDglrAGtQpyk5bn3ZkxsNmTyMnxgLy-O6krYDXGqlzTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=t96UFFEt22CNdPRfj2asvEtR4TnYo_RHEoJjzsAwARyMWoCQLTw3aMHOzaOdqqu5AHF_aZiYiBpHZQI6YbNzHMfQIFwqP3szId89ZPAEk3yKMF8v42HaIE4O-tMWSVbEpVhCfsu_WDdPYcAVOhJBGO6jx1yKg_0WlLb23PERau3KJ4MeXxilRieHSSrSyGCj_8mflY8FvTh082W7ABcgyeQOLlzRC-CU6PG_A6T6QJ98yrZNGIvTeiLBVGD0ypDCpa0KdmHuiQB0Rw-tIggUwNZEZdE1jf5o_GGlFkgvGojDglrAGtQpyk5bn3ZkxsNmTyMnxgLy-O6krYDXGqlzTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7498" target="_blank">📅 22:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7497">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DyCaBHoQfUPrGvPTtmf25Yyef5ilf128XDW-YcJxLNC9fW50VTYjkY22v09a-dzV_lX-jD_MnxFgws_k8gBv0gnANDCJHnu1qwZIvsH6-wiG3fk4Yq8jQjV0xeXApgDHNHm--OjcvBSlGh0uzajvctFwOXsM_gddKPsQc_MyKooN2yyeIlwE2BeFwJRr9ewmYW-LXvooQEBZkYN6fx4BhWxqgwy57csm4QaKjTzGGp7PjtyGeGs4eOAQ20BgbGOB2DNrIv0ryZ6p5AXN3sjWdt6G1ko6nKPmuNF734zeS6QjwTDetoBBFWyVyPLOtoykgunupIhsvY6yYXV2z63mSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7497" target="_blank">📅 19:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7496">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIUItIy3U5XtNFk3sIsmf0gwo-9Zd8E8cfJ3z5soXegEzpMlEdqwkdjf8lpIzaYwbWGFU2o4_KQGcQEamTp9PxHCpcEhRzJ6ajaWkBcscQxTB5rsD6_iAV0RaMSGtPOeKf9nQ3hHebsym5Onc5FFIvsZrkiPcrbfBly2RNy_DUgPX1YZZE_n7CfY1wstkgHS-bk1byY4GWOVXjndy0BXj8J4-X_GGYbgZPi16H-rlFryqRZF3woe2SYYRENjDKXIOE7Ii_JiaVxMrMQNAUTQfOlpRMbvJAZdh4bvFUgYLJh9gMy3W4RZE_IfHMHqgL0j_hzimnJ15--1hPl9pCMRBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7496" target="_blank">📅 17:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7495">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=Lj2tCGffRpUodBxrvSwfzL4YoTNhe_4rADyaKU9hi-wri8_eyiqv8dqcehTTcJu-2sSDH7G4bSJfgFx8kJT2B6ckXBte7WndElWNZGsHSFzQIe4I58U3uBhIlmGejQ9_3vTRxm65mmX6tIuFsyoDskIPer9aHSILsRyLQ1SUxxtkcoi69kFsCtWIPHW5t0UrjDK9bo_D9tpeWZeB83glIXoxPZX5C_xWvoTZnGukWibbSF8wd0FgHn8yUFeYAudlIrkOMvtnSANzkpMSGUYUA2gf7C42vcBx3LQXHPU24gc7SlDVGZMxAcDdDQQTMNRG_F6Uk3fajQCsUWwhKJmi3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=Lj2tCGffRpUodBxrvSwfzL4YoTNhe_4rADyaKU9hi-wri8_eyiqv8dqcehTTcJu-2sSDH7G4bSJfgFx8kJT2B6ckXBte7WndElWNZGsHSFzQIe4I58U3uBhIlmGejQ9_3vTRxm65mmX6tIuFsyoDskIPer9aHSILsRyLQ1SUxxtkcoi69kFsCtWIPHW5t0UrjDK9bo_D9tpeWZeB83glIXoxPZX5C_xWvoTZnGukWibbSF8wd0FgHn8yUFeYAudlIrkOMvtnSANzkpMSGUYUA2gf7C42vcBx3LQXHPU24gc7SlDVGZMxAcDdDQQTMNRG_F6Uk3fajQCsUWwhKJmi3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7495" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7494">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzANNqZJI-NF4IxSuUMM5N3POw77KO-FAfApgjB_HQ_Tc7Hld3QSo6lyc-pouF_sIJH-l4I3uoya4lwOnTVImN6UBuCcA1qRYylEguzWmozfVkyAYd0s060uKOmmLy20yUWfUQxe0nluSK254Ipb7unI0M1RqzmngMtqYgJ7m6xr0j-uHnlcYpHhF4YY2A3gkdeJa1GuUlWQBbi2MoFC6XBuWSpnmNzuNBQ3XpNxs8F_qcaUb2eM4grpJCCaugnQvHnWJ1MG610DCNY_HZtzH9KSSFBJI8k9NX4ypMULkrlb60FdGIFJo-wtvGnSLX3wLEK5R534z0p8G3Zv6sDNUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7494" target="_blank">📅 13:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7493">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TI3dZbCTz37PVssH3sO5Qb1ZdtkVboN4Lps_xTBv_XrmXjPdVpYOLOjeK-8wJHqEOzlyJ6RrS6hkynj10MtPnoR4HMgHg8ToEGmRJaAe0XpTaVtZmAtfWOLWuKXldWuNJ26VYIgvrJ3wxNOlE2RP2ktMDJZoarEXVOCv4jkCiK0jsGGCQG9mzxrB6X3qQmojdLctTcU6W6iEPHx5CmkkjaC8oUlsMTtft4503n2eg_74dyR2xq6rPmCYWriZTeqVMQFTIG6H7mTQ42V54AFijX_kmu_SlmE4KkQVtXo9juSTU1_mBeiWgqh22wZk-2Po28pkX5kCKmqt_QqNriGBbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7493" target="_blank">📅 12:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7492">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=nRzMqSCLm_C7q0qeMZOZwHL6JKNZu9CKBoNXz-NNV8HEbRuh-8Z2tpizkJYeDtguvOn_ov3hD5yi7gEq4T4P9dN6TeXf6XXAia5wGN9HzgRs5_ZQGJNL3y6WBIWI3kLwHuzdVN95Ype-Jgl0c1LoFLSggD2bI40n0PVKUcb7WK5I-4Xtd8whfgwZDQskntQpqoh9cw41U9VRkp4vCWfycBf9czy3gDcgUKyWfz3YlZ3_VYSOJKkZ1zp6BHF2P94ThXjbHM4ThGApQaksHVa-3AVxkW5xKeaOCM0eaRZRwY7ZibGdZR3Wz1hdJeagPuWR70mZKJ4EwmQuLVJj_HBxOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=nRzMqSCLm_C7q0qeMZOZwHL6JKNZu9CKBoNXz-NNV8HEbRuh-8Z2tpizkJYeDtguvOn_ov3hD5yi7gEq4T4P9dN6TeXf6XXAia5wGN9HzgRs5_ZQGJNL3y6WBIWI3kLwHuzdVN95Ype-Jgl0c1LoFLSggD2bI40n0PVKUcb7WK5I-4Xtd8whfgwZDQskntQpqoh9cw41U9VRkp4vCWfycBf9czy3gDcgUKyWfz3YlZ3_VYSOJKkZ1zp6BHF2P94ThXjbHM4ThGApQaksHVa-3AVxkW5xKeaOCM0eaRZRwY7ZibGdZR3Wz1hdJeagPuWR70mZKJ4EwmQuLVJj_HBxOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7492" target="_blank">📅 12:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7491">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c18VWV2t8y8c0VtYDHA68uiPdjtXaatCpkx5rIP-5sk4oOeXVfaKM02koMgtSY3rHA7ybUKAhfP3faMLoG-xL530xQ69faj4uZKDdAVFI5vxgqyBRdRFzP7_W7dmEW3j_8boKKMHASz6qvZrh2RUlBj9jAyqeTGBRM3L9IAl_WZMJ-yqBUl-hyFEFXkYDVfNtclIzcXlEPcEc-C0clSECEK8qQCmdMwQVLHNTYfGXIjkxREj1LEwK5CpwPH83LD4EkdEcDaRt0hciu9laot_R8z4X1TlPiQd9hynN7rkqOoUrxPwqI0KcrW6d5bUmsQktRjKQ5JbGSYDBS6UJsc4-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7491" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7490">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7490" target="_blank">📅 21:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7488">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iA7st2WQe7DCOAtZ9tEtmoIuDAzpD0DPaStEp7Zj6JP62Cv35bK7EPuRRXOyAv8RFYMfYpk_0CSJTly_ML8QRMtE1uon4w9LuZaVs5eN_dnx--sDnmMc6ZeRnpXbli1LFPQzwYjX-dUHaJXGo9a2lnlw-hB6ycLi3OoDeVKMD3ZFywhOE1sfkcH3_oUCzoDzwPHTRCDg49EdXTCgFP0NOsYRIv76ZT1n-FMjMPRgB7xQPR4lJX8Bi4U-njgzzgUlh9CIdZkmBxLQlaLTmPhMpyf-9uR2PJE1iNnxxoBu5fQC-Y7iEaI4vGLDFnPzB6tLJ8bL0x2S2E3ouMh7PmlhLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7488" target="_blank">📅 19:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7487">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZ6UP6HLITek4I1rNwD0oNqiPvE3VIP67Az34xH5GPa4sF3uzaGEJDzJaIB2Ki_JipLBX3vN54r6I0lR-YCyPozdk_4Z92_tuEBr11Dpalpg03RmRpyyoQjDajriGeztE6kcZMSZecjTvsQ8hOdQuiejI8dZr2K_bfcIBtikuZdhr116AqzVsujCyIISfMRDdF_dNlZGwJfpNVFs6X9y6hN3bF0MGc0I3PR-30oXpIjfHR9gNf5LtlDCiDooTIq_zcRBEhDd0O-g5EwcgXtk_YlrN4hb63xTudJGB7JmSXBzAxzJZqG5sfYzPDfePdNSB39RhEBLt985boB8GWQFZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7487" target="_blank">📅 17:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7485">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEyhqb9TTrzJ6OniXjd-wU8CUqjF7Mr_zAROe65PfjeYp7Jm0wgB2pWDxJ-DXY5nB1WlDNSx6GWGogtGQSiUFWwV7gsqBEu8-4YhMfHdClrG3qewM4ilCwAEVkqf8amkVTCmTJdtmVazbGC0QSW3GmwPLMDJZ7jOMGoIRgaXaXTN0AFsNPEcHlC4EQdSTs-NfNgGj1PNbf05UM4K8VgucM90FCKYVKvT3BQtZLogi4HvAQk5aU82duEhWaY_52Yn22f--qYew8FMNGlco3X-VIHkAZSgOSMI-wUZlrpp3EK-cdBs2IdxnTgU39FxYg2BjyhZy2YOzcuW9jNI-bHK_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7485" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7484">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGFm7kkVKQrqpPxkrBpxB1LCDrOMqdZGVxTo-5Bl_w-InCg3KXOwo4udfWgqk22uHN9gNXj3qhts-U8_V5R10OCkdLg7ILbS7fI7qwY4Us0myMa4OmBb_D44xva2b3gJthtxqGd3wDyNYbVm4GtBlvTYLPNkoA5hVw62GwDyaPDnA2DfUEyo2KjnWSlVYFzadXsCX9XG0LCrrLHWmIHrTsozEMfpH52NDJy69_vdisdusFZd_dTkh4brZGUDUso7GcLIhFo8b2zyrDQuU9f2qM-xGy6XRWU7FEp8R5zBWBnd9LUgfq-XHW2KpkzkoX8s8pt-Zfnt4Xp2zcLaXYhwuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7484" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7483">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7483" target="_blank">📅 17:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7482">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmrXIn6ti_4qYLdLJizK0XJMVFf4Hf3otbvJqzivjbxD8f2ZgAwcIzRmFV456RXVqk1T41LhmS3i-Y4Hq7OOwRK4OtSMyoXnLNXtKCgxgqm2iUKCVUp3QNDgOkMxQmvcx8jENg1zJ1cVZCS_mAroCaO_srug4XXi00ziprUlCnboUeqMdhwAPyQyug0m6wrqYSKj0fXQ4bnpAHXK6HpBzID7lAbVzOAld3oYJsGUGzARxZeZLrBlUlysGIcgSS2auE_n93MplnE1ctOUkD-yayOGYpo3pJgZ0j0cN5WGde1ToRJ70mOLLjx4n3vIuIB9mT5ajqsAa3WU-tHt7DWruA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/ArchiveTell/7482" target="_blank">📅 23:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7481">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUzPf4D1Bb3t3WnQbjFBQfhZllhUbn9Wd5JPb213YtvP_uLr1PTwq4gWOz0bkGsXP0VSb03gDPzWquYoxSAevyBzrQ0XvTrLGpnhvmYZca3uiSi7PIQAR58fnWzrsMyP7FE84VtfoIzsacrPyKyevnR6ASdOJ9XNyMH3_8p1k62eWUO4wqXX2ADtE5fTZMa4ub1FqV4Z_FTmWZLtNNaXlellyimDlF8iycXs3dSAgW10t4MPVBRgtOV1cCqw9tTd5i4PpNUcnezmy3FO8v9FfZHnioPMnjF67Cf1mpZlUFNwKC0sJjYC8F_RtMrEtBK1-EsG_cnKG_A99G6f8JK5UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان: امروز از ساعت 12:30 تا 20:30 به…</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7481" target="_blank">📅 15:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7480">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7480" target="_blank">📅 14:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7479">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OT9AMSNVNf036FfJ2t7kqLl4pMhKAPxvr20H5PmUClPsntSO8cxR82hxdZsXOQ7mjU--mx4XcvM-q5iMWhcIgKJe-yvw3wPwOqW2rpWJCARLxWWrEw7d5z0Zvo5ojgrXTMpcTIx-Hovxc4FQV6pfFj3KHmr-p2oBFrRBV6aJjleqSOlWHwIba6J9uToI8q6_qbsoqNAZw1-ddEZaa0TVf92Q27vKt3bSPjFAHn2I878_OCdOKbpDcber_06YDqfA1kHVVHcVHIl5SBkIpY0Zju4QLkpM4VoUXvjka3-eW_lEK0Brz3Y2Q910axDKNb5YMp75ziw3QbNkBT3z9o46Iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7479" target="_blank">📅 13:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7478">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7478" target="_blank">📅 22:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7477">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">Gemini 3.7 is out now
😍
از اینجا میتونین رایگان تست کنین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7477" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7476">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEPN8m-Bbh6ScuSE7xEZD2snFBSv2o_rvxmw3pfCSpu5J4Kil-HMoleRd3DTEFbsLO90o8cyQFX4BMdqVbBb952bpETiQsRepIz6SI_xuYutiTt1mEmDrc2pAeTv6ovNlvlcbc9-nUx1RpOSSGE6bchVrjwW-NQNS0xJIpw1nHWJjT7eAEJ1OzJovPk2JJRLT_LHHD6EttCohoDatEqncvrAkAlEAaz83RDOiiJJCrROyO8HbfpJ3emnRVH1qGlKkIaoYYa5t27oaf6ujQ28LapORv7lx1y2_PM4Zc8ifZWT_ZBeG33I8HQaDJxJ29GgLlte6QkMu-OvLSZVM1iQXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/ArchiveTell/7476" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7475">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7475" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7474">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7474" target="_blank">📅 17:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7473">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTdNqrkl--P_u39OgPWUWlkFDKnEFunR9QdwoXl5hdH-hkO6kYG1oF4GiP-HemXpz0EOBZKRc9BJNrI3-91zv5184dtwcHtBb2KyhieD-KSJBcf_ZoomphqMr5KwL1JXAUHN03Pjw73TpD71pjeQyYwvPJWP10iTgsOUJIjv_1J7R8KjOcKqR8cSX1cBHobH8B2PkhD3w9ey2BerIuzUM9uLX1t9GnahvJkESl4MezQUlFyzvLQKHr2Hwr8-zmB3RptoJLXSDsgENEXFdnCqL2Ve5QSI0zP7rAQCW7YluLfb8TaGFK3CK8gJaPLmS9p5tvCgyF0q6o9dxYANP5Fuhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7473" target="_blank">📅 17:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7472">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCC0P2WVvScHtERgUXD4918AdLTLxmOswEw3iuM_9wu7Ens0bsfSO0_VHjNAbNuo458902W9w5x8z1lvoxCRj8VQ-WFoJ1GJmRFUCXm6Tw_1hSfgnESjPtMuciIfXjNQYXS40S2oBCPyNt1nipJvu1RmrXFexSO0hZhOVuU0Hcs_s0dgoz4l9fo7pbPVghhRTvCSXZHzddgmo4u5AaIS0aUzADRiwCTOzin5e9A7TorZ4EDYiGao1aS-OnUNjS1HOE1rNzlnUdL3Wqpm1_eMr6xieBHFlZhEWEi0mnbwzYem6KBNPMJoXeOqJbYMwU5Ey0f3wSnr9gkJ7nhxgpXM-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7472" target="_blank">📅 15:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7471">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c16P1hmmalqDhOdyeJIW07EUriR6XwNtIvyjdTLU9b4g0fAokEzKzKtLT92fGlrrut7ogF5SoildnWVHng6KJhHo4AkYpCFWS_KuwPpUxdGNzy0vZpd_LcwEO8goDTotEbD_J2ItvWWnekfg62no0Ykiu9VdDb82r13bo59N5eWh55O-Dyq0p3kxaPx5Qi4MkygMr5-2LBxanH8827RdOWS-YKJjxHqXNiezMPflAFMe_Mdl8POm4mkst1-NcvmBsrqpJukW5sASkiePEqY_xAUiwUte37OK1MipzERCQRRzFR_3SFfhTT8oaoqQlsIrkiHy868LKLIUx9hn5roIrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7471" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7470">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpfDnJhJURhOhHqji7FdonUfzqgkygcfr_hP9IDMNT1m4XcVehqDLZLnmkiGI1HLYYvWHeP7y74xZcU9Bp8JXRWIs9Uzfy8LTbDHAaFMjuLIFfSTsDZlIBgCKh-nxmyRUpEcc-LPG50OtNCg0p3G2cojCuXjptQ0Wwfdw1zWL_QT2fSsGiBTKaV8GuwWz684AII7hYjrJTIPfTX_uXBvUgTfjkZSCmqFEVJXOECQT3LnpyAFBqaZ5MoeTNJpYqxXZ_iCx6MD0uetz17GhuSFar8QHneAMMEoNVopN2Ke9OWq2671a4oy9djCyE7LdG3XlolQeLSn37lH_H17J1EPpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد  قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود ۱.۵ تریلیون پارامتر داره و قراره در آموزش SFT و RL پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:  چند هفته بعد، Grok 4.7 با حدود ۲.۱ تریلیون…</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7470" target="_blank">📅 23:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7469">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">https://t.me/ArchiveTell/7053</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7469" target="_blank">📅 17:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7467">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHnLlJYElRjayEfUZ6xpVo5CuOqvRmuMaIdyDQ1--sR4iam2-OGJSkdKD_BUMeBWrGZPN0WMzKCl2qBE6XP4SJ2XsjDwTi-EBI5eL6YN_tw_RXS8DxriplxlG2wuKQATiTuUSnsi1kktfFG1TbmLImeAlaycMzeUOTKI31p7q69g8ESk5yZD100wh-YYwIVEwe0Fu0SChI76eKGsKQ_L7K2ilOoZ0usLlTb8cvXtZvHNQ7uAqirTsYh4xTbJ9RdGrpdOw2rG42YY7aYJFdNPlt89Hpck3n2R5aGtLLwD8A4GjcdoZ1MS9HsFetzjAGBa1MQnzKEt0UDWC8ccczPPRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7467" target="_blank">📅 15:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7465">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7465" target="_blank">📅 13:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7464">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwJ4mgoVnTgS0BfRZWR1Mv7XJ2Cg0AwOgTvsQDzLX8UlLqJIGtItvmEFO2h6iK4dZbUsIqrxCjeMpgw4AgPNkgW-azimXSwSQHGwSaZUnqRRsK6-lxnEeXvDkpCAp79mChPfhzUeSj8jw5v6w-FW7VM5Zk41nZvsiXActtMhW_3iNZ5iNt9NNodAXGPGdMoci_x3ruPbl-gaLRncRChgAJ1RhZ2AeQsxByfYr5E_yPlJ4erP3lN1at347Olo8pdNJGLYxszIen9qhppXqvtJGaWIraVA4SgAPa4nJM3pid0jHZuc7qf547D5czD1myjz_3k4ZC6rpVPiAcbUi47EaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7464" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7463">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7463" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7460">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgJkzwsq1P6428NaGVZHmzOQhyBiixnukZVjXdCHX6m5sQG7foz07PIqwkdby74pFXM5gwYryg0m-YzKgfdHFBBkgqS-jzzlWsrbdAKqeGlxv_A2m1yttHckIr1witkvm4Yq7P-r-AIizpHgzHeHwpOIFsEQO3IXPqBd4KGEwgD4E_O7e4ZkXbNYEwoTMn-PU5Ms5sf_VZJAMOtKzx1UxDmxi9lODPbJqUtM2fHPIjt78FMpO4-Z8CCePlYcmR6X723S_NMt2P6zhcAsha4U1cK997XI5HrHfC-7pzmsE2L4ETVRYotKI0ArEPC2H1b1YQ3UOhahhp1SsuNogyg_Ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7460" target="_blank">📅 16:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7459">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVwdYh1k1iIv5jyffzSXksFPVFKFDwA4jojllP_-mkP8r0Y5ZENOxd9eiWUtToFJGNhK36F7oS1attdgOY8nZ0J2KjTDt98u5eQKYkV5HhM4oe9gl1H3vhidDcT-xxEkxHkdfNYBeC2kfpg7aaTwd87AGnOixf36-3RNUOo9Leb7NtwyfewkjUjeivzge4e1AIVcRDfbkLStwTpzewBvvXhOUj3BU9MRtx-oQoK3cFqVaIHQsMnEJCbRZbmRBehPWUp4Md8HQtd4_3rUPReENcDDMmvm8aeZSoWDrxeH61L-q-tREpEbBDIkD1qcl73tVwjR-yBD4sBeRERHeYjPyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7459" target="_blank">📅 13:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7458">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7458" target="_blank">📅 11:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7457">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHrAV93R80DO-KszUZePHf74QWSrXxeRiuSlMc0V1AH66J0ZNBjlhhTTbrxdqZ6EsmpVyNw2nMeADdGoAO7k8OlWq4Tp9o9e2LGzuYSvpxJ3BpUYEnNoppU0HlJwMjQKVCKvaw5EullHMfUDNuwt_30Kz9z8wqlrg7Bb4sTL4_oFySX7_L8D2Tekl4N0aS3kYc5Ovexvka7cEv_Z63tzwQ6n_tKdaaG3MvQ0-M6QjV47Qf3uNfckj1zHBrXyXERbkA1JOTYfxMxJ0v_sLGtvYMnCSZpFFzclg5hMaH-u3NuX7--RMCCrobT65GMWKci1q5sPITgeMklYI3RdqtcT5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">40 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
✨
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدیمی لازم نیست )
داشته باشید و از طریق این
لینک
وارد شید
✔
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
40 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7457" target="_blank">📅 11:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7455">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oag8Di6Eg3o3bn34RIw4GjUTyL2wlyhKRkQ_Xp_RW6GKPNLLTOMwgetW5EMJhinL4s8JXJBLuwmCmW2d-mrUENS00acwtOzZoHKBg4GSgO419Nfxzsbht2R1bspa4pq3qi5n9Cd3sAESBsuvQT8O3NYNelSrJAKIDaDXoRuMlbSW55nfJ1midaNfyhuewLhneYylfOtRkt1Z6lfuaX9yi2nyUPdY7cKN5jC4ZNtU34q9mCRF94mQ_RoI6WRR5caZuMPmzS6uVe8RjTZbpXyNDB8wRTXK_N_XN06cN0gAMHP_L-kKjkYpmQQfrfmInf_0IWm-rXw2BmdmPONbXhDx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع بزرگ یافتن سایت های API رایگان
💥
🆓
💵
با پوینت های این سایت میتونید کلید های API خریداری کنید و یا کلید API خودتون رو به فروش بزارید ، همچنین میتونید Redeem Code برای انواع سایت ها خریداری کنید و کریدیت دریافت کنید
🔍
همچنین این سایت منبع بزرگی برای یافتن سایت های API رایگان هست
🎁
موقع ورود مقداری پوینت دریافت میکنید همچنين هر روز میتونید از بخش Daily check-in ده تا پوینت دریافت کنید
⚠️
🚨
نکته:
حتما با فیلترشکن وارد شید
🔗
لینک ثبت نام
🔗
بخش خرید و فروش کلید
🔗
بخش خرید Redeem Code
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/ArchiveTell/7455" target="_blank">📅 22:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7454">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITwoAoaQAct8_LCzZWOoKHPB_zsGXAWfRzSCtCIjZ7Ta0OvV8ArGOQEoQhmTZz5yS8QKdkdjlVz_MIiaN-lQ2bpN7c9r8idB8GtsHCWqMnlm8XlQmob1mh-tO9CaRpeoTE31ASeHDYysVObMIQkFauLXcGmawlw3ICfSW8QrCTgtXryoa4ryDIbZkbXT5aulX_b7hgUfEsbxJVu5wPGEJp6vIpd3J1mx1NNCh5hRPiigLs21GsUnexSwlYkSHjlPMWsq1I0JsfZPaCSf1uBAHJxtcJofrBRtcot_oc6BhPT1DxSFDSbxm87rMdW3DqpdW9PwdOnzbW6-iRkr875JVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های هوش منصوعی قدرتمند
🚀
🆓
Opus 4.8 | GPT 5.6 sol
✅
وارد
این سایت
بشید و ثبت نام کنید
سپس به
این بخش
برید روی Upgrade کلیک کنید و پلن Enterprise رو انتخاب کنید و روی Start Trial بزنید تمام حالا به
این بخش
برید و در صفحه چت یه چیزی بنویسید و Let's Go رو بزنید
✅
پیشنهاد میشه که اپیکیشن Postman IDE رو دانلود کنید
‼️
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7454" target="_blank">📅 20:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7453">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdyOGUYWpyQycKXhlJlYv3NqUhgB59HgNPKkl0MhIWDStGaUqyXFItqkN5Zk0yrEKN131pKNzZ84i17h706zNiPyb0jLc60udzdWY7Wjwwwf5HNDDkyh0505JQlZcgIzGq5EUc90dJNdkwqxU5XFBDjMzcruVGroteI_U9S1s_K9LeNVvXALNBkG389KuVnqvzMR6pWQ0Cro4RIQmU6MiW0k5wrzqyi18qTLbnHy3JYLl90ZvgymDNvYGlugC90gU973Rf0berMoPhj1X7kzGzGZ751uH4vhIAl_C3ycYFQy6RgDsk3leCPG8OJirX60NGDLGv5GuP9yeyON4v425A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدیه ویژه برای شما
🎁
3 میلیون کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
dxai-sk-5feecf996d141afae9e16f8bc072d49a692312d7452a4043fd055c37aba2c8a9
🔺
Base URL:
https://airdropdxns.my.id/v1
🔺
Model ID:
grok-4.5
|
qwen3.8-max
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7453" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7452">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">جزوه ساز پرومکس
❤️‍🔥
از این بعد لازم نیس سر کلاس چیزی بنویسی، فق کافیه فایل صوتی کلاسو بدی اینجا و  با کیفیت ترین جزوه ممکن رو تحویل بگیری!
📝
https://github.com/faithsaly5-stack/Study-Note-Maker
تست کنین نظرتونو بگین
❤️
⚡️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/ArchiveTell/7452" target="_blank">📅 22:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7450">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پایان دورانِ عذاب‌آور جزوه‌نویسی دستی!
✍️
یه متد خفن طراحی کردم که می‌تونه ساعت‌ها ویس و فایل صوتی رو به یه جزوه‌ی تمیز، مرتب و آماده‌ی خوندن (Study Note) تبدیل کنه.
✍️
فرض کن ۲۰ تا فایل صوتی داری (مثلاً ۱۲ ساعت ویسِ کلاس یا ویدیوی یوتیوب) که نه وقت می‌کنی همه‌شو گوش بدی، نه می‌تونی کلمه‌به‌کلمه بنویسی. با این روش،
بدون اینکه حتی یک نکته از قلم بیفته
، کل اون ۱۲ ساعت تبدیل میشه به یه جزوه‌ی شسته‌رفته!
🤩
فرقی نمی‌کنه دانشجو باشی و درگیر حجم سنگین درس‌های ارشد، یا دانش‌آموزی که وقت سرخاروندن نداره؛ این ترفند کلاً سیستم درس خوندنت رو عوض می‌کنه. کافیه صدای استاد رو سر کلاس ضبط کنی، بقیه‌ش با این متد!
🎙
دارم یکم دیگه روش کار می‌کنم که حسابی کامل بشه. اگه پایه‌اید و می‌خواید امشب تو کانال بذارمش، پست رو لایک کنید تا انرژی بگیرم.
☺️
✈️
ArchiveTell | S</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/ArchiveTell/7450" target="_blank">📅 18:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7449">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxDYid80akmCPNm3uqZjEpeVmh75RuSglKAb-sQgmC23YdjWevYAksR4IMcqkAz7fujBkGBnjFlZ_Dz52s-izdWFAPe_kOU1e3yiVjNG0XoCSICrw8aw4VeTMi5dywKnGcEY07v8JfIKHrddu1XvRmNhYdDy1kx7BXgnMGsfsYfEzbmeDns6_Ek4JyNb2x6uFbu4DoRfwb0bsQJiWFWnRk7sgcqu-THCX962rt0EzTRliCl2QeIEcsf54cmWvSxDvS9o7vo7hqguhrBejdHPx8jaKex4fNODmerYyGkZf5ugZtdTuh61SVU1R9RNM46TGqnCKy6zVYKnwQZ5956nmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://tabitoken.com/v1
قابل استفاده در
Vega Agent
✅
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
120 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/ArchiveTell/7449" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7448">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dK4MxRSB9LhlehkEy9i3nerMsrpJv75CprbMF9BahVEbdgOaVmCPAAXQhOLslMnlrpJGM9k0k1ecwKZAZHfkenbpUFOAWwth3unF5U_OWSi_kSOcD_9bB_p1vQr1yhr_tPo-DX14Coe4ZTHMpIoAIFFuOrycxGP4NjTyc8_xedNf8YHXIB-p6waA1oNmMON2EITvbEJuRndpWJKgSTDwTa8c8OLaJvrzrq7mfW-lkmr6eGBvr4x021T9IgxqwgrIJJtuS0dCREJySwnsRheVz5K713HEkumOzPu7ET8GfC-nl63a317OeGqVzLWFncHUE1lQ7dJp9YvAhfLq9HAZIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20
دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
GPT 5.6 sol | Mimo 2.5 pro | GLM 5.2 | Gemini 3.5 flash | Deepseek V4 Falsh | MiniMax M3
✅
برای فعال‌سازی فقط کافیه یک Gmail یا outlook داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://fapi.leileihog.top/v1
قابل استفاده در
Vega Agent
✅
🎁
با هر رفرال شما
10 دلار
و شخص دریافت کننده
20 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/ArchiveTell/7448" target="_blank">📅 18:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7447">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oU7IgU68GIj_mg_ZXCvaYWo6gQnyawjz_X5HSfdKcTjrZhmZMz2KnVtYPhl2Tp71Jy58BwNMpCnIJsQMF8nOfSmxFEugyB53GHr-D6Ty9_M-Hmx0tk7ChsWC2EzURih_D1jwulmmwtWpb8CV6iD-bx2UTG6L5feCGzpFE-WSy9z8MITEmMbTQVeeDHEgJdwAbFhymgE76KbLvOiLtC5T_VdOvSVikOyc_IsIol9sz1oL9ud8ILDVhz5MWvTnWzPYWMrImZraEWqeXfvd8a0g0BfjwotxXBuNYknCu8i7R0A07-ymEI7Kw8ewoGqUPl1ICKVQfunqfgvyxLs7pz7KqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10 هزار کریدیت برای دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
GPT 5.6 sol | Opus 4.8 | Deepseek V4 Flash | Kimi k3 | GLM 5.2 | Sonnet 5 | Grok 4.3 | MiniMax M3 | Gpt image 2 | Seedance 2.0 fast
✅
قابل استفاده در
Vega Agent
✅
Base URL:
https://www.getunikey.ai/v1
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/ArchiveTell/7447" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7446">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXD4W8boNEpZt2Xu9j0qQGiRwpO7EutXpG4jI0cuDq3-VjnKQVqHb-G9fJGOtS01ZqPnzJWHs0J2ldwLh_ElPhmVQvZGx0YIA4e-Cm3SL6QB0hRlOLMvzeYf8k_-Kq5IOHnRYteFYXdn3_bSOOTaqh1QY6_Yo51Yz7XNkHk2DXm5GA2DebXbmFOKo1PZyNjy5-HNNQqDGH0I6n-WilttwVpahw78DbSvYf6xTdV36VjgAewTH1E7gd5YiQ71pziz-kc_ROlSVnJItiDm23NHdiyCWNUl2oyp4nGvaowe4cVUOqlBs1taM8mvSOZRp9JjRS-TCB7IKO_Lb_RjxVk46A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان نامحدود به برترین مدل ها برای چت کردن
⚡️
🆓
با این سایت میتونید به 35 مدل هوش مصنوعی به صورت رایگان دسترسی پیدا کنید از جمله :
🚀
GPT 5.6 Terra pro | Grok 4.5 | Deepseek 4 pro | MiniMax M3 | Gemini 3.6
✅
🚨
توجه برخی مدل ها مانند GPT 5.6 از کریدیت شما کم میکنند ، این سایت هر ماه 3057 کریدیت به شما میدهد
💵
😎
🔗
لینک ثبت نام
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/ArchiveTell/7446" target="_blank">📅 13:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7445">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">💥
🍌
نانو بنانا پرو نابود شد!
کمپانی xAI مدل Imagine Image 2.0 را معرفی کرد که با قابلیت‌های خیره‌کننده، اینترنت را منفجر کرده است:
🚀
🎯
پیروی دقیق از پرامپت بدون افت کیفیت
✂️
ویرایش دقیق و حذف پس‌زمینه پیچیده با حفظ شفافیت
🔗
پشتیبانی از ۵ رفرنس به صورت همزمان
✍️
رندر بی‌نقص متن روی تصاویر
📈
آپدیت و اسکیل عالی تصاویر
این مدل قدرتمند هم‌اکنون در Grok در دسترس است!
🔥
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/ArchiveTell/7445" target="_blank">📅 20:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7444">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=rt34o9-PgksKlnc3uWYTnX8jHnN6mslJP0yBXRpBmt_iBtO7NFiBkejkD0rpJuoizfwBdggHVUgwTiiDLx4rizCU_ZqHUVlKB-bnWdldMo_Mef_eA9cV8XBd5mZRclWx4pVF-vqHm9rLwJb5zyP4xtsYit6c_6_Aj9MJKAxxazDn79txbSu47G_PWWLAp6s5gUu6UG5rr8WQoLmKtVO6EWyLvgck5SPXzaCgvp5t5bLI0ceuJe50j7P1HK05t1PqZumTlvf9tqBrpjmOB7W8WjC-hkhyv6dEfkIkkOAXQ95sqNOVaQBwXR-jHn884pmhnBGprKM1C9b8-auTOafiBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=rt34o9-PgksKlnc3uWYTnX8jHnN6mslJP0yBXRpBmt_iBtO7NFiBkejkD0rpJuoizfwBdggHVUgwTiiDLx4rizCU_ZqHUVlKB-bnWdldMo_Mef_eA9cV8XBd5mZRclWx4pVF-vqHm9rLwJb5zyP4xtsYit6c_6_Aj9MJKAxxazDn79txbSu47G_PWWLAp6s5gUu6UG5rr8WQoLmKtVO6EWyLvgck5SPXzaCgvp5t5bLI0ceuJe50j7P1HK05t1PqZumTlvf9tqBrpjmOB7W8WjC-hkhyv6dEfkIkkOAXQ95sqNOVaQBwXR-jHn884pmhnBGprKM1C9b8-auTOafiBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهندسی معکوس پروژه‌های گیت‌هاب با GitReverse
◀
☁️
بچه‌ها اگه یه پروژه خفن تو گیت‌هاب دیدید و خواستید دقیقاً همون رو با هوش مصنوعی (مثل Cursor یا Claude) از صفر کدنویسی کنید،
gitreverse
خوراکتونه!
🔺
چیکار می‌کنه؟
لینک پروژه رو بهش می‌دید، اونم کل فایل‌ها و ساختارش رو آنالیز می‌کنه و یه «پرامپت» جامع بهتون می‌ده. حالا کافیه این پرامپت رو به AI بدید تا کل پروژه رو براتون دوباره خلق کنه!
🔺
ویژگی‌ها:
پشتیبانی از مدل‌های مثل Grok-3، Gemini-2.5-Pro و GPT-5.4.
🐱
دانلود سورس‌کد از گیت‌هاب
🌐
سایت رسمی (نسخه آماده استفاده)
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/ArchiveTell/7444" target="_blank">📅 18:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7443">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فرار از زندان برای مدل های Sonnet 4.6 و Haiku 4.5
⚡️
💥
📣
🚨
حتما با اکانت فیک تست کنید
برای دریافت کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/ArchiveTell/7443" target="_blank">📅 17:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7442">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فرار از زندان قسمت 3 رو بزاریم؟
تو این قسمت Sonnet 4.6 و Haiku 4.5 از زندان فرار میکنن
😁</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/ArchiveTell/7442" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7441">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4GFRpxAnBHF6v4EJR6HSEA0e2MyX_bWE_plnFUX5saU-V2mhf2icvv2_vJAfADbreI38zfZForEKQTIPvnckqeTeYn7it6uowLK0-h0Qki9wP_URDuDMhKGWHEAzfcgXHEbcnePq_mgSMIjOgzaoXlzKjHuazj7UWlniOJq2mqYinhcY52S1mrk4JDpM3StraDxNJFBKLIi1PgW4Ft08p8nzNxC_xKTPAac3s7k_D2JWEFTWUD7OPmyHmh0y3EZA6ti1YD_Vci6RjYma5Y7N0Vlw-wuOKuRlT5AtLIhKQCQukMtZ1kUh7TeFHGwYD1lkptmxs1czsNZ_Q9PQD8Amw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
با این سایت میتونید 5 دلار اعتبار رایگان برای بهترین مدل ها دریافت کنید همچنین این سایت 3 مدل کاملا رایگان بهتون میده
💵
😎
Kimi K3 | Deepseek 4 Flash | Mimo 2.5
✅
Base URL:
https://tokenharbor.ai/v1
قابل استفاده در
Vega Agent
✅
با جیمیل وارد شید سپس لینک ارسال شده به جیمیل رو باز کنید و 5 دلار رو دریافت کنید همچنین تیک Free models enabled رو بزنید
✅
🔗
لینک ثبت‌نام
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/ArchiveTell/7441" target="_blank">📅 14:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7440">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فرار از زندان برای مدل های Gemini 3.5 و GLM 5.2
⚡️
💥
📣
🚨
حتما با اکانت فیک تست کنید
برای دریافت کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/ArchiveTell/7440" target="_blank">📅 22:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7439">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شرمنده دوستان
😢
بالا باشین
تا چندی بعد فرار از زندان flash و glm رو میذاریم
❤️‍🔥
بدون رفرال
🥹</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/ArchiveTell/7439" target="_blank">📅 22:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7432">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=cyuNaxTPB8kZ0m9qmfbnngYMgu2_Dhzz0kVUTneZgN_upnJk0yZm0U2UiwL6CSh1UPW9tfc5N6qDrwcx2c6AaBO0Ik3gpe5P2799QiuqNu86sbI0wCkApPHuqs7AmlG9p-afV5HjuxGPn6oPV_TZr2Wh-dnE9xVNmhLaKjDTA60uqCn6mcaTaTQJ8r3Dm7-QisP9npHLq7pixYvRZFBsdn7EzwtSXjqafpDBzftJ0UB5dDr5iTreNrbpQDh5yeBJDaJEG6XITpKpaz4tcjvhaNYqrUubPh-XjdWAZBETX69yUC1ggYTVOPZCL8J9lZzPzLcD2H2ZzpqDVYisXBflRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=cyuNaxTPB8kZ0m9qmfbnngYMgu2_Dhzz0kVUTneZgN_upnJk0yZm0U2UiwL6CSh1UPW9tfc5N6qDrwcx2c6AaBO0Ik3gpe5P2799QiuqNu86sbI0wCkApPHuqs7AmlG9p-afV5HjuxGPn6oPV_TZr2Wh-dnE9xVNmhLaKjDTA60uqCn6mcaTaTQJ8r3Dm7-QisP9npHLq7pixYvRZFBsdn7EzwtSXjqafpDBzftJ0UB5dDr5iTreNrbpQDh5yeBJDaJEG6XITpKpaz4tcjvhaNYqrUubPh-XjdWAZBETX69yUC1ggYTVOPZCL8J9lZzPzLcD2H2ZzpqDVYisXBflRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمدید فرصت ساخت ویدیوی رایگان با Gemini
♊️
🆓
بچه‌ها گوگل مهلت استفاده از ابزار خفن ویدیوساز Gemini Omni رو تمدید کرد!
جزئیات:
حالا تا
۱۱ آگوست ۲۰۲۶
فرصت دارید که
۱۰ تا ویدیو
رو کاملاً رایگان بسازید (قبلاً تا ۴ آگوست بود).
❓
چطوری؟
تو اپلیکیشن یا نسخه وب جمینای، برید تو منوی ابزارها (Tools) و گزینه «Create video» رو انتخاب کنید.
جا نمونید، برید تستش کنید ببینید چطوره!
😳
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/ArchiveTell/7432" target="_blank">📅 19:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7431">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-6yyl7exBS53yRVS9wnzgYi6wBMSRZKXbbWNLFr1ANLJR8PNcboL7Iv050HhgOZN3SCALRakJRKEM1S_6vrqAeFBZwwsc4ptDK8V0e8XxkhoUyWQXeL04ZI41Sc21tAxZpCRsY03SLakSX8pefim93vQZ4fMhYpdSWmmRtCyYNcXIhySD0clBYIDW3oJtbydjVMgDTzKBLamuKxZ-8dekopTV6p6QtJwGZY7aXYkQibeGGmKfmQBnePOTKQbpty5Soc-KYaM_3Zxoj6cLomAsbLw7tcYIujd8eI7snntwYlhrbkcOU6y-BsVYR1Qu50_IAXqsvRSus7tRkkidw-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن خفن و متن‌باز بدنسازی با openGym
💪
💪
اگه از اشتراک‌های پولی و تبلیغات اپ‌های ورزشی خسته شدید،
openGym
یه جایگزین رایگان و کاملاً شخصیه که دیتای شما رو تو سرورهای غریبه ذخیره نمی‌کنه!
📌
چرا باید نصبش کنید؟
💠
دیتابیس کامل:
بیش از ۱۳۰۰ حرکت ورزشی با انیمیشن آموزشی.
🗺️
نقشه عضلانی:
روی تصویر بدن نشون می‌ده این هفته کدوم عضلات رو بیشتر درگیر کردید.
✴️
پیشرفت هوشمند:
خودش حساب می‌کنه جلسه بعد باید چه وزنه‌ای بزنید.
👾
بدون نیاز به پسورد:
ورود امن با اثر انگشت یا چهره (Passkey).
📜
انتقال دیتا:
می‌تونید تاریخچه تمریناتتون رو از برنامه‌های Strong ،Hevy یا FitNotes بیارید اینجا.
✅
صفحه همیشه روشن:
موقع تمرین صفحه گوشی خاموش نمی‌شه تا راحت رکوردها رو ثبت کنید.
💡
نصب:
می‌تونید فایل APK رو دانلود و کاملاً
آفلاین
روی اندروید نصب کنید، یا با Docker روی سرور خودتون بالا بیارید تا بین همه دستگاه‌هاتون سینک بشه.
☁️
دانلود APK و آموزش نصب از گیت‌هاب
🌐
نسخه دموی آنلاین (برای تست محیط برنامه)
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/ArchiveTell/7431" target="_blank">📅 19:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7430">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdrvwqvCyCEfibJhfkkhX_DeRUaL7MescMPL40ExWeGe6BJyZsAh0clGM7VRz5q_biCAgmwn55HY4glh3WQpQjepDaAbk3IhnlekVJxZZRppqJvS6YPhcuwdGV_FJlqHK-8DM2-TyA8Q1ja_0g9jDQXpX3X4Tl9wvVDRGQVzc1HNWIwTfBS-jzZV-pLrvWVW6QRuRDtgzuN4SdQ9jJnW4Ha9slBGx-7yj4utbijH169DKTTfsC4hpYcX5stgcpt0dqY7lLjOdsQyWM12fK0rTIYJejQMP-OjQI4BFblHQvHvEvBku651jwNFRiHF1L740IbhqA8Qu_a3pBovHywtyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😺
چت متنی داخل ChatGPT نامحدود و رایگان شد.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7430" target="_blank">📅 18:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7429">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzWN-mTWrixRDAe_tZrDzLxBL7_wjCuH9HpRzgiLNCZ7_dCf_vMnyzb2Ckxvsgel67qacxP7lKaocpUCn7IMW2IKf03TH69_ZPs478nlsP80uDa0UxxP_I0AVXeu4_4hMd8R2F2k2xt3qxwlX2KVxuOp02P9RTseP8d8j9MYsNVJCNdWp6fbRvDBekIAlyJUskcTgOZbv6RhGjt4OzLDHD95ZgSYcEkMkSpwuNRN71Nw5KL8Y19N1GqTkmuRIrQLmGy4wNew7jw1qqGjIsHyL_OssoFcjYi-Hr67_7fPv8pU3Eh_g_aiOgZgp6_Nm0pn9YbEnYFjViPzXSqTyvQAxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
🆓
دسترسی رایگان 14 روزه به GPT 5.6 sol و Claude Sonnet 5
​سایت و ادیتور Zed اشتراک ۱۴ روزه Pro خودش رو به همراه ۲۰ دلار اعتبار رایگان ارائه میده که به ۱۶ مدل برتر هوش مصنوعی مخصوص کدنویسی دسترسی دارین.
💵
😎
​
📌
مراحل دریافت:
1️⃣
وارد این
سایت
بشید و پلن پرو رو پیدا کنید و تیک Free trial رو بزنید
2️⃣
استارت رو بزنید و با اکانت گیتهاب ( قدمت حداقل 30 روز ) لاگین کنید
3️⃣
از داشبورد برنامه Zed رو دانلود کنید ( برای اندروید در دسترس نیست ) و تمام!
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/ArchiveTell/7429" target="_blank">📅 15:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7428">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=A0KKKNDYN4NDxKobDxCf5TFiuYijgO8kjLeH6e2LvTHF70Jp4ugvGRvgu3FnNVzQuse95Ko8nzripkElkGqJt_BpU8n4ycR-QAhmdYAN50diLusEoCeFXLSrNIEK00wVgkirKn1NF17ojEtBp1FPb-RrSSKPITY58UavlVFNHoxkPY2Q0ELMefzBzhnscoTRvpwpBXUsIQqTUe0053FGdVYf4vYj5YQ_C83T_JhBiS-_e3Q2Uixprdrml_76lyId8VyywPEB8qg7Co7U1APn1GknTprrjUa2m5jODr0HWPh7KWHwgc3PK6cxUpmEkHhz8w2KDX1QcY99MXY_RJBR4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=A0KKKNDYN4NDxKobDxCf5TFiuYijgO8kjLeH6e2LvTHF70Jp4ugvGRvgu3FnNVzQuse95Ko8nzripkElkGqJt_BpU8n4ycR-QAhmdYAN50diLusEoCeFXLSrNIEK00wVgkirKn1NF17ojEtBp1FPb-RrSSKPITY58UavlVFNHoxkPY2Q0ELMefzBzhnscoTRvpwpBXUsIQqTUe0053FGdVYf4vYj5YQ_C83T_JhBiS-_e3Q2Uixprdrml_76lyId8VyywPEB8qg7Co7U1APn1GknTprrjUa2m5jODr0HWPh7KWHwgc3PK6cxUpmEkHhz8w2KDX1QcY99MXY_RJBR4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چت‌جی‌پی‌تی رسماً تبدیل به فتوشاپ شد!
🖌️
⚡
ادوبی یه پلاگین جدید منتشر کرده که ۷۵ تا از ابزارهای حرفه‌ای خودش مثل Photoshop، Premiere، Lightroom، Illustrator، Acrobat و InDesign رو مستقیم میاره داخل ChatGPT.
😺
🔥
کافیه توی تنظیمات چت‌جی‌پی‌تی پلاگین Adobe رو فعال کنید و با نوشتن Adobe@ توی چت، از تمام این ابزارها استفاده کنید.
✅
این قابلیت از امروز برای تمام کاربران در سراسر جهان فعال شده!
🌐
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/ArchiveTell/7428" target="_blank">📅 12:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7426">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX-afkBHvS0clHESDPbMwlmyOQwDdeJEnQwX-rlaVgZGucGzbAVgL8uBVuIm1Sf9UEiPVOdsHf-graJZq46FlRnOHK-Wefr5sxhvXkUpR9BD-7OfCjFb5cVxoCkAECCDJngDIUfjMf6Xa1D3onItuy4LVOTUH63mgZtL3r6QgmLd15O1JE8P5ezK_ehk1DWxzoZQn0AVp_7F5-FFd79u4ND-vIq6_P7YK0sEyhMMXOcrJUy3s5dhxrmwrDiIuwnEZ93IQovOA5pK8r5QgclQSpXXJjXtBdbBsnD2ShznODgjNGQeIQv4LQbbFDGgxHo6HIeSlUXk9-lw1YEaVOAEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک ساز خفن گوگل
🆓
🎵
🩵
با این سایت میتونین با یه پرامپت موزیک و موزیک ویدئو های خفن بسازین و منتشر کنین.
با لینک زیر ثبت نام کنید و ۵۰۰ کردیت رایگان دریافت کنین:
🔗
FlowMusic
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7426" target="_blank">📅 00:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7424">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRwJ845LZNoWlC0YgZn9dE8c2VSuUlCrxMgZHAQ3uleVziZdxwgPyNhdWlFbFg-_YEOcnZ-lMAkjPR91f3zH8iKmy3-VtnuDoPeVmzNzzlO0nryVen2HTwpNHgQV8ZzI4lvwMeESHj4TCdIsllF8iJ_D-InR0Zxy-oS6AUwHIhiSx1748gvy4GX0dLUTp6UBUm_MOk_MPVYkFRIiMTd6j2MSUUljFBgBO7EOTL4v40D8EVeUoSqhm4SMJo6fGpD4zcdEu_XEElb9rX8y6j8n6zFMytcN3s6AouMcJVLOfqr4p26hsLIM3SGvhiFL93m1iW6n2cmuD1zZO-EbemHGAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1500 کریدیت برای دسترسی رایگان به برترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.5 | Sonnet 5 | Gemini 3.5 | Haiku 4.5 | Gemini 3.1 flash lite | Nano banana pro | Nano banana 2 | Nano banana 2 lite | Gemini Omni flash
✅
1500 کریدیت برابر با 15 دلار برای 7 روز
💵
🗓
برای دیدن آموزش کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/ArchiveTell/7424" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7423">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uv8RmRmAqm9p_aN-axBrHNy_3xFxCO_bC6NDxJ-Th7qecdBoCoo5ko160RgAp7TuTLD2i_Ycok_K8waj_KD-3Yi_e9AmGscJ3YXLf1GcbEVBbFBzH8B0thHnhPRz8tnJjBQnN2x0Lmy0naJhMzcxacsab3pRz3qJCmZocYUfxc5yrPuVnRQaP9dmiCjMlcNF9lnsoEsfMTbj5xbb1FWDVUssaJMKsHA3H8oblXaZm_QhDwPzH4GMSOX-RkG_x7BRyN72qNXb0iUBgRx951lyd3wP4NRP5GVQoWSaNzjfgD33eL2r-sjJpJ0b3FFO7Q5UmwLeQbKvBZfTkoWhXtpGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به Kimi K3 و Qwen 3.8 Max
❤️‍🔥
🆓
بدون نیاز به کارت اعتباری کافیه وارد
app.clusy.io
بشید، با ایمیل ثبت‌نام کنید و توی پروژه جدید مدل مورد نظرتون رو انتخاب و استفاده کنید.
😎
⭕️
فقط ۲ روز از این فرصت باقی مونده! به دلیل ترافیک بالا ممکن هست سرعت سایت کمی کند باشه
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7423" target="_blank">📅 15:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7422">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrACiANG8DFFkDBARlExMsNmpm7LuWEIOPR1U_qmbUmJHSjmkNpNLEAwir62FRdw6E1C_NTdVb2Ah9F2RuLxAtZPgl7k-fQ8bLapqL0U731FbsTvP1mmGCKpNghoQBH6PI3EnKn7QJlyQpL6thPgSL13YbezVqPnd-1AdfPue7rpcfWyZ0UTM_41iTbWAsnxaCjvkOCCdzGQILR_3mt5SyIuNUlb99bdWhQZJmQnrh5IjTzAvbOwyyf7DvFCR0Pr-iqPNtvwXiVQeNLUoqdChoK6nIT7Q5q7Q0Bjh3NCaOz3oUSxhFwqsjVLPZUvwV5RHnn7fis2Q9K-k9piHJCs5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان:
امروز از ساعت 12:30 تا 20:30 به وقت ایران
⭕️
🛠️
مراحل راه‌اندازی سریع:
1️⃣
وارد
سایت
شده و با اکانت Google ورود کنید.
2️⃣
به بخش Account رفته و اکانت خودتون رو از طریق تلگرام فعال (Verify) کنید.
3️⃣
به بخش API Keys برید، یک کلید جدید بسازید و اون رو کپی کنید.
4️⃣
برنامه OpenCode (یا محیط دلخواهتون) رو باز کرده و اطلاعات زیر رو تنظیم کنید:
🔺
Base URL:
https://api.aigate.shop/v1
🔺
Model:
muse-spark-1.2
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/ArchiveTell/7422" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7421">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5U59ktzqB8nWkmedBPCGhqmDDpflZ5MtcvfJwfC96VtAOY8NfUidXdMu1XAqf6dutCzQQZHlcrHUgR3oPgvI6upOpgFk6HMj25caIvnguf0hX8yG7FEv_yEmO6fxZqfy0U-L5SXoaBOYBQtFwwR4_4sC_t5fFUTIM8CFjpgdRMWl6LZTpafe3MiaYTYDMeNPnOq3pwxQ8AqcG1tBrt5fZ-0_LWq-Bj-NwbeZgGJXdDNjRfaB_uJfGnfKBokG3XUSGEX5jDNKKVla493vgp5teLFyZkXDg1q2eoea7Blu_1WFGcPFYLJIK5skcOVJIAuWncqUIzYCm84CRHwR9olVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ‌سیک V4 Flash
به‌صورت
نامحدود
و
رایگان
تا
پایان
سال
6️⃣
2️⃣
0️⃣
2️⃣
به آدرس
cnb.cool
مراجعه کنید
➡️
هر
ریپازیتوری
که خواستین را باز کنید
➡️
عبارت
@codebuddy
را تایپ کنید
➡️
حالت
Work for me
را فعال کنید
➡️
تسک
مورد نظر را وارد کرده و اجرا کنید
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7421" target="_blank">📅 13:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7420">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اگر دنبال کانفیگ میگردید و حال و حوصله گشتن ندارید یه بات پیدا کردم خوراک خودتون
😆
میتونید با رفرال جمع کردن ، گردونه چرخوندن و دیلی چک سابتون رو شارژ کنید
⚡️
🤖
@survpnbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7420" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7418">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVQkDX7CuubPClwQErySLr8WGkk7t1EMDxZkxN2XVbj_Puv6CpXdzhZ0-jz37Ed0Z_HcB70zQkxwPg6MAOJSMNYKbjTkzARfz0cSXySKTW4DEc-ZcLPxbTOAZaQJ1w9dkotPYu_3W3iRdwaJQZ3ZRQ_k7en0WsyTGRpauTilSpKKghf16GrOJWSaevDy2v4Ey-ia1XvPNt9c60SxDaqQzTKxEKs0EvJJHQLITPES4I9sUzVCkXFSgWgJIz-CmwuKkDUwM2zCO38_d0uYmaC4s6FSMgolDw-elHJ0wSgcbrp9ra-s4493xOCZ5VVWu9Re564SkWxyxS0xrnydKXptYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کامنت یه کاربر زیر پست تلگرام در ایکس:
من آدرس مخفیگاه پاول دروف رو می‌خوام
😕
💯
اکانت رسمی تلگرام:
مخفیگاه رو که نمی‌دونم ولی من رو می‌تونی تو خونه پیش مامانت پیدا کنی!
🙈
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/ArchiveTell/7418" target="_blank">📅 00:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7417">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpxbdeOja4LAA13kHthvzfYeuLg5HzQ3XE5dGqT6hENXc4HHIaJkNQrawxH9_OgU9S8uB1QK8s56IbMdYPO0ojFfl004zRTmqLe16mWYPhK83YBFwxR_qvJzYg3D3I3m9-9NCJLb51tRxDOgsmj5tn1N4uVQ_xnUye5c5CKAlUDMYrJPYUSqXbDmp19SD7NfMBT-9G0P9Yf09CkuiOPKSX8RKh7bhYnYCenZXqOZ9EeCQFOTkaTXsEgF5ZCq52l7x--rf388COnxUZAhz0N9ODk1Ld5JpZRcfXmpWaPth0JCleEEi8cKAOc_2_Uc7G84Jw6j11ij9-zHBwHSllob7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف فوری واترمارک تصاویر و ویدیوهای Gemini
🚀
🔥
دیگه نگران علامت روی عکس و ویدیوهای جمینای نباش؛ با این ابزار رایگان خیلی راحت حذفش کن
❌
😎
✨
ویژگی‌های کلیدی :
1️⃣
100% لوکال و حفظ کامل حریم خصوصی (بدون ارسال به سرور)
📶
💯
2️⃣
پشتیبانی از عکس و ویدیو با کیفیت های 720p و 1080p
🎞
3️⃣
کاملاً رایگان، سریع و بدون نیاز به نصب
🆓
⛓
لینک سایت
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/ArchiveTell/7417" target="_blank">📅 21:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7416">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCm1cZx_S86uiIeDJzEG7k0Zq86VRvpBtD32uZ5Vueabpnu-1kum3HxO6YFvo2aZ_sTOO4TXXksaobdgCwResgxC8KTOLgbGMA98hjRG3rLYI6GbE7bC-5jUBFVgD6gig-DafERYKD10VR39tQYZfo279-1hih-3MzwbN0Uj1GpxxeSt3rVruV-X6bMF3NO55zyvuOsx5hz1f02kfCDMITztRGKNEcyg8r9fRJDrjhzVsMMNxahaz7bItqSb0y_SLAJcsujvLFlaSpoyRXcRIZ7hUKKA9QgGw95qzMGY0nRdNz42UuckcR-9WXrm7eKlZHN8fmyzOc9kG9blnLEv5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت
Dola
مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت روزانه و رایگان
🔺
کیفیت و قدرت بالا در خلق ویدیو
🔺
استفاده آسان و آنلاین
🔗
لینک سایت
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7416" target="_blank">📅 20:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7415">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsesf49IxhWKM6yggJuykUzfmorpnPyNeFnWQdZ6kOteKarjElIsXR4mfmTL8nvevnNuzb9QfRwh_abH-eWQuBY_z_xAfJS7HkMAXIhma7PXHotfIuxDEKmGRn_xc4pVwXbpTJsguOOpIktFvnU2nnripoG0uoALQfIVJ6y8RSPAChMebPIpbkonxwO9ycvGYpQl5rKzBL3q5q2zp8OQDXEilesXS_EoWyRXb4gSX3MEXNLPtfbZD33NRprliYqKF1URZ13lWLWMzAR5Oaq5_xa60n84bwwRGXmn5yOc0jpbCqEWEarX-EmhhlqLVsrGoiULFcUz3RFqGQ12CAO2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
گنجینه API‌ های رایگان هوش مصنوعی
🆓
یک مرجع کامل برای پیدا کردن API‌ های رایگان مدل‌های زبانی (LLM) بدون جستجوی طولانی
🔍
✨
🗂️
1️⃣
freellm.net
بیش از 424 مدل رایگان از +30 ارائه‌دهنده با اطلاعات کامل شامل محدودیت‌ها
📉
📊
2️⃣
freellm.sh
لیستی ساده و سریع از سرویس‌های رایگان با نمایش وضعیت و محدودیت هر API
⚡️
🚀
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7415" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7414">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URyRiCjA1o467o6RFy1BbBrrLxEDUU7V_xZnRczCX_LJE2O_wkTgOWwz8Bh6xIqE0_Hq-85skBqbVUKsY8Fqt7PC99ePcYCP_9YjuQjnVgwkFochNQmDJ4CkawDijX3otKqRxmoHYZ9GOh4_hbuaaotAt_ApAM8o3BSAHYbqhZPL7b-XRgBMXJ14hh3SEAfVORBFImyiOtN-9bGhhM-Q_wngK7JyFshjIiqlCCxBS6_Innaq1sD-2PWTFj9pE6wGH38Tl5XGoYuUgu3hClCo0gRSYlYHO3iCUj6WwYcRcGJYujy_vc8oC1Vai0r94e5FS5EBB_AOBbowkqhhHx_gMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمینای اسپارک (Gemini Spark)؛ دستیار هوشمند و همیشه‌فعال گوگل
♊️
🔍
بچه‌ها گوگل با «جمینای اسپارک» رسماً داره هوش مصنوعی رو از یه چت‌بات ساده به یه «ایجنت عمل‌گرا» تبدیل می‌کنه! این دستیار کارهای روزمره و گردش‌های کاری شما رو به صورت خودکار پیش می‌بره.
✨
قابلیت‌های خفن اسپارک:
📄
اجرای ساختاریافته:
اهداف شما رو در قالب وظیفه (Task)، زمان‌بندی (Schedule) و مهارت (Skill) دسته‌بندی و اجرا می‌کنه (پشتیبانی از اجرای همزمان ۱۵ وظیفه).
🌐
وب‌گردی خودکار:
می‌تونه کنترل کروم رو به دست بگیره و پروسه‌هایی مثل جستجو تو سایت‌ها یا رزرو رو کاملاً خودش انجام بده!
😨
مدیریت ورک‌اسپیس:
خوندن و ویرایش فایل‌های Docs و Sheets، زمان‌بندی تقویم و مدیریت کامل ایمیل‌ها.
💻
کنترل مک از گوشی:
اگه اپلیکیشن جمینای روی مک نصب باشه، می‌تونید از راه دور (با گوشی) فایل‌های سیستمتون رو بررسی کنید.
🤒
شرایط و محدودیت‌های نسخه بتا:
❤️
فقط برای مشترکین پولی (Google AI Pro و Ultra) با اکانت شخصی (بالای ۱۸ سال) فعاله.
🔛
ویژگی Keep Activity اکانت باید روشن باشه.
❗️
فعلاً از زبان فارسی پشتیبانی نمی‌کنه و تو بعضی مناطق (مثل اروپا و بریتانیا) در دسترس نیست.
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7414" target="_blank">📅 17:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7413">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S306BuNnRPEdFeZywIl7HeyVN_SnlbSMMXv7TaS_tsLm-CRNxVUITjZstSw2s3JM4D5bOzVgkQHcwCwrsHPBBWe7b-KAQi8kOaO0NEQU59hwGEfrSsnUbsVbArlCFkvXR_61lE6TykVcX-H2bDJK13zgwyPuiaTlBvVcDPbn3rc-oyqyYVMCVcaxcCFya4BIE289RyQFPpvq9pv3v1MHjsWTBNfsARVblSSHOd8eGKKIIqRaTcCQZAcsk6rPqsGCU3YebofOqsQFJ7jVB57lQUk4ye5dLieoRifLMv_p_GyRuNOSudeCk7QgbYmKfmUPt-pkCsy81xAVMEsf05rk4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌اندازی سرور اسپیدتست شخصی با OpenSpeedTest
🚀
🌐
〰️
بچه‌ها اگه سرور/VPS دارید، ادمین شبکه هستید، یا کلاً می‌خواد سرعت واقعی کانفیگ‌ها و سرورهای خودتون رو بدون وابستگی به سایت‌های عمومی تست کنید، ابزار
OpenSpeedTest
دقیقاً همون چیزیه که دنبالشید!
🚀
این پروژه یه ابزار متن‌باز و بی‌نهایت سبکه (حجم اسکریپتش کمتر از ۸ کیلوبایته!) که با جاوا اسکریپت خالص و HTML5 نوشته شده و بدون نیاز به هیچ دیتابیس یا فریم‌ورک سنگینی، سرعت آپلود، دانلود و پینگ رو اندازه می‌گیره.
📶
👩‍💻
👩‍💻
✨
چرا این ابزار خیلی خفنه؟
🔺
اجرا روی همه دستگاه‌ها
✅
🔺
نصب بی‌دردسر
✅
🔺
تست فشار (Stress Test)
🔤
🔺
بدون ردگیری
🔞
💡
کاربردش کجاست؟
برای تست سرعت واقعی ارتباط بین دو تا سرور، عیب‌یابی کندی شبکه وای‌فای خونه (LAN)، یا تست کردن افت سرعت موقع استفاده از تانل‌ها و پروکسی‌ها.
📌
👩‍💻
لینک مخزن گیت‌هاب و آموزش نصب
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7413" target="_blank">📅 16:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7412">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔥
یه
پلاگین
به اسم
oh-my-hermes
برای
Hermes Agent
معرفی شده
🏥
این
پلاگین
سعی کرده چند
قابلیت
مختلف رو توی یک جا جمع کنه تا نیاز به نصب چندین
پلاگین
جداگانه
کمتر
بشه
✅
😍
از جمله امکاناتش می‌شه به اینا اشاره کرد:
✔️
هماهنگی کدنویسی و مهارت‌های codemode
✔️
سیستم مصاحبه هدف و پرامپتینگ برای برنامه‌ریزی و مهندسی حلقه (ulw-plan، ulw-goal و Loop Engineering)
✔️
معماری حافظه پیشرفته (شامل Dreaming، Pruning و مدیریت کانتکست)
✔️
سیستم حافظه لایه‌ای (بلندمدت و لایه‌های L0 تا L3)
✔️
متخصص‌های دامنه‌ای و قابلیت‌های تحقیقاتی
⚡️
تنظیمات آماده‌ای هم برای استفاده
سبک و سنگین
داره که می‌شه فیچرها رو
روشن
و
خاموش
کرد
GitHub
🐙
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7412" target="_blank">📅 14:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7411">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPiiWvOE9RhHuiVlQsoh-fpkEBAmz6H6lw1AZ-50MeCmNLhFm5jWork4frTNksmt9ROQsOI02XMFdoKa2sUphuj5CPLZPYhgpMB6q1qAvK902GevEp7Avw_ktLlBQA8uBaRsylHpbWPKx2PcOZPBES9icDUXV3U6sHdpphVavI39XIvz7EHU_4kd1foTkO5ASv4oNs1vtSm4NJmHtX3uvVzdfUZrNpk1rikcqpIlirQFiSoQ8GBinctr55SSvJLKE3V7AVZLsDRWufUVufMbgM1vHoSjSwSfD4BrCmnBKF0X2aKNkaATcpSKNREt-lUBVqDdZ9ZgKA386ivfTW50kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱ میلیارد توکن رایگان  تا ۱۲ آگوست
🚀
🆓
پلتفرم
InferX
یک کمپین محدود راه‌اندازی کرده و تا
۱۲ آگوست
امکان استفاده
رایگان
از برخی
مدل‌های هوش مصنوعی
را فراهم کرده است
💥
از جمله مدل‌های این طرح:
😐
DeepSeek V4 Flash
😐
Gemma 4 31B IT FP8
😐
Qwen 3.6 35B A3B FP8
و چند مدل دیگر
😍
طبق پنل سرویس، برخی از این مدل‌ها با هزینه
صفر دلار ($0)
برای ورودی و خروجی قابل استفاده هستند و می‌توانید آن‌ها را از طریق
API
سازگار با
OpenAI
در ابزارهایی مانند
OpenWebUI
،
OpenCode
،
KiloCode
،
Dify
،
Hermes Agent
و سایر پروژه‌ها به کار بگیرید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7411" target="_blank">📅 12:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7410">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptkq-lEgClf404FZ9BQxNr3LvEajTCPLqj7jT_tAGkZe576HSRNwH9O_JyOyAqRe-Cg3nXAiUczbqJGOya7cIHVcN8lNxj3yrevgpEbt0-p1A70daEaYL98RW7UoHXMt1TPcXRXAh9ACaKqHQHR9rVBkqOwxJURoWCPtVFYgOXC8wOusdeJ7NQf1HQjvRNHLdFXpGolGQzhX8tA8XaKP7qbfD4-fR3lqmaxnRYq2tXxFEwyrVBCd40hlV1DZ1_nNAhLeEIAIu8aunEMgCTpaGlOTMw8n57RYdnLtjqgCCFKeEUWm7i_QNnMesjMqSaNQwo8J0AR2zLllEF-IhjNUSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی CloudSSH؛ ترمینال قدرتمند Web SSH بر بستر کلادفلر
🎶
📱
پروژه متن‌باز
CloudSSH
یه ابزار Serverless و فوق‌العاده برای اتصال و مدیریت مستقیم سرورها از طریق مرورگره. این پروژه با استفاده از TCP Sockets در Cloudflare Workers، یه تجربه کم‌تاخیر و سریع از اتصال SSH رو ارائه می‌ده!
✨
خلاصه‌ای از ویژگی‌های جذاب:
🔒
کاملاً مستقل و امن:
پیاده‌سازی خالص SSH 2.0 با TypeScript (بدون نیاز به کتابخونه واسط) همراه با رمزنگاری اطلاعاتِ اتصال در مرورگر.
👆
رابط کاربری حرفه‌ای:
ترمینال سریع بر پایه (xterm.js + WebGL) با پشتیبانی از تب‌های همزمان (Multi-tab) و تم‌های متنوع.
📁
مدیریت فایل (SFTP):
رابط گرافیکی کامل برای آپلود، دانلود و مدیریت فایل‌ها با کشیدن و رها کردن (Drag & Drop).
☁️
همگام‌سازی ابری:
پشتیبانی از ورود با اکانت گیت‌هاب (OAuth) برای ذخیره امن کانفیگ سرورها.
🤷‍♂️
دستیار هوش مصنوعی:
پشتیبانی از API مدل‌های OpenAI برای کمک به تحلیل لاگ‌ها و اجرای دستورات لینوکسی (مثل Docker و systemctl).
🐙
لینک مخزن پروژه در گیت‌هاب
🌐
نسخه دموی آنلاین
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7410" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7408">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ی پست ناب بریم
🔥
🔥</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7408" target="_blank">📅 11:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7407">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETEJDQ5Xr2lWuHk_Wnyy4vYu3jbPgGMG4HJ0vaJV2nFmjPOcksznMB0Vg67ifROI8h61lvt4xEl8RKbWWPSnMnnI3qcJHci3ABQH0OEej08aFgma9mNZNyakN0upaPJ33v0JU_7BAKM2TX_LqK-tapzPD7cXFdiDohXQG9st5ZRSi3nTYHDV-of1jytb3lslgyNrLiFcAFfNOTFdIezIUsUsJsTkBL6BEz9XwbeILDKzHb_xnv7opWXk2rYfQtY8bUtEzOoC-BpSW-L-Z037lxL0oUEox4KdFvKsJ96blkfj9DuA8XtRQz-hAhil0Uyvxxpq-XfhYaz2vROz4rjw-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#fun
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7407" target="_blank">📅 11:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7406">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7406" target="_blank">📅 02:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7405">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=aoTbUnoBW8k7LrNxM8GYHAjA8dNefN40TIIqbHED2wK1PGytRQsuMwKp0v-2TwK9FCLsNwRjXEyXdvkhen9ii5IHasNCr6nKsTgUKGcTvp6fi4jSZyTHNO22BPoZrrIbIPyeYUq3T1GMC_Yq_6gOu9s5Md6IZz07f4GhJnxn7bK-GUSjnxc7Li5FXROlUMhv0PPJrvLroqQtHpEwtdYygALndfNMCtSMtsMktrRB2yQ1ihbxAkQkafiS_WSsMxUGZHuFf8wg8O9nnabGrhg8GSr6NhzzBKlFxxEZpY9RuGsoNjQtJOOF1WPp0ZK2QfGnJ3cAQcORW08Cptp2c1PoCxzaZIyycNyfP7rcVm8rcJVo_D5GxB6BTA5JN1g-u0H_eKHRMd7y_gburTc_B5Gklz3Yxr68l9lsy8EAtU6_jQTimFTBNaNtxpS_hxLnK3Zjb7NnDNp0XGwN0i08tqGl0Rh2sKf3wQt8b7z_e3dbaqN7wfZ_8P1yAAa7CRW_vPruwqfneNWL9XT2F8QsPbVrjuaJYm2VAfo1NCfiKSkcMK_dKsDq4V9JOk7pCZCCE2hNzWHFszpkuuVtD_x5X3372TQ8X-Pc6jhK2-CiqekVvzAAGpH79scWrwe1dXM2nbT24PAUiiDOZV8G2umGh-nAJEfwcw35u-jVMAzJVZJim8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=aoTbUnoBW8k7LrNxM8GYHAjA8dNefN40TIIqbHED2wK1PGytRQsuMwKp0v-2TwK9FCLsNwRjXEyXdvkhen9ii5IHasNCr6nKsTgUKGcTvp6fi4jSZyTHNO22BPoZrrIbIPyeYUq3T1GMC_Yq_6gOu9s5Md6IZz07f4GhJnxn7bK-GUSjnxc7Li5FXROlUMhv0PPJrvLroqQtHpEwtdYygALndfNMCtSMtsMktrRB2yQ1ihbxAkQkafiS_WSsMxUGZHuFf8wg8O9nnabGrhg8GSr6NhzzBKlFxxEZpY9RuGsoNjQtJOOF1WPp0ZK2QfGnJ3cAQcORW08Cptp2c1PoCxzaZIyycNyfP7rcVm8rcJVo_D5GxB6BTA5JN1g-u0H_eKHRMd7y_gburTc_B5Gklz3Yxr68l9lsy8EAtU6_jQTimFTBNaNtxpS_hxLnK3Zjb7NnDNp0XGwN0i08tqGl0Rh2sKf3wQt8b7z_e3dbaqN7wfZ_8P1yAAa7CRW_vPruwqfneNWL9XT2F8QsPbVrjuaJYm2VAfo1NCfiKSkcMK_dKsDq4V9JOk7pCZCCE2hNzWHFszpkuuVtD_x5X3372TQ8X-Pc6jhK2-CiqekVvzAAGpH79scWrwe1dXM2nbT24PAUiiDOZV8G2umGh-nAJEfwcw35u-jVMAzJVZJim8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/ArchiveTell/7405" target="_blank">📅 02:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7404">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBesJxYYmnnWJMZ0HCv3yd3IQhRAid0itAd94ISvN-MDdt1Z73imn39uneAUXWjJev_jaxpcDHtN33_fJnDDmrpg7hzq7wK_eyxoP1sNafykrh8xz11vRE9-GD022zcnh9UHt8D0De5xNUjFzWVynLQ_bXCMeKhySrstgXHodWLoX5h_Yin3ODj_Z2Rsb0ul51tAxKbImZKfPLIP1v-pBQyDn1ChNXzP9Jb-0vbxFERuoAaVpg2E6JgralV8RQB4_zboKOcz1y_Q54fzJju0K0c31jcCAMdoZbAOHcytHTzrXyfyMRb01QU1gm4TFeXNN8sVsizl4j7_y8il-Qq76A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎁
500 دلار اعتبار رایگان API برای شما!
‏همین حالا کلید اختصاصی را دریافت کنید و از مدل‌های Opus 5 و Opus 4.8 لذت ببرید:
🚀
Api keys:
sk-2UddB27hnFA1z2LKWKnq6BQaffBLe86FU0htxAHm0Q9n5vjW
Base url:
https://agentrouter.org
Model:
claude-opus-5
|
claude-opus-4-8
✨
کلاینت های مجاز :
🔺
‌Claude Code⁩ | ‌VS Code⁩ | ‌OpenCode⁩ | ‌Hermes⁩ Agent | Qwen Code | Kilo Code | Cline | Roo Code | Open Claw
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7404" target="_blank">📅 01:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7401">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">📥
پترنی ها آپدیت جدید داده
۲ ساعت پیش
چنج‌لاگشو ننوشته
https://github.com/patterniha/v2rayNG/releases/tag/2.3.2-P10
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/ArchiveTell/7401" target="_blank">📅 01:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7399">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3p0BZri3mEpyOndc1ETCftIqOm8inisU9EWuBTYneP9ghumtyAjzNxpnyQYVDRpGIwD-BC3010CgDeMhFLP6-E1TuBvSVNbjXCjDGZ-ZX4_VxAnv4GkP5zf11FXCM4Ak2rK4lkNC_BBEKDeYRszr0GWoUVcc-BEq8uJZQGzFbVrgSGxRxy6tfE6v9SVr5BqQvP_9YtoSt_ysDG7mDbQus-hWLmWLzF5Qih_ouX9i3sVzuFqrgFHN_Kc4pO2cwV0De5HFiptUcvgaLWNhK4XADDNoy3-965RaVoyWsBpypiVNsv7s_eVKzBVwuvJHWLECqphXr8MsuwrgR8kwV2TRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولت کلادفلر خودتون رو رزرو کنید
‼️
تنها کار باید برید یوزنیم بدید و به اکانتتون وصلش کنید
⏺
کلادفلر یه سرویس پرداخت و کیف پول برای ایجنت‌های AI معرفی کرده که بتونن خودشون API و محتوا بخرن. با سقف هزینه و محدودیت‌هایی که شما تعیین می‌کنید.
cloudflare.pay
❤
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7399" target="_blank">📅 00:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7398">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آموزش تبدیل کردن صفحه چت سایت Qwen به API
🚀
اگر در موبایل هستید از
Kiwi Browser
استفاده کنید
‼️
✨
آموزش اجرا :
وارد سایت
chat.qwen.ai
بشید و یک حساب بسازید
در سیستم کلید F12 رو بزنید تا Developer mode واستون باز بشه
در اندروید از سه نقطه بالا سمت راست از منو گزینه Developer tools رو بزنید
وارد تب Application بشید و گزینه Local Storage رو پیدا کنید حالا کنار این گزینه یه مثلث هست بزنید روش و سایت qwen رو انتخاب کنید
یک جدول باز میشه و آخراش یه متغیر هست به نام Token اون فیلد روبروش کپی کنید یا توی کنسول این دستور رو بزنید خودکار کپی میشه
copy(localStorage.getItem('token'))
اینی که کپی کردید در اصل api keys هست ، ممکنه بعد چند روز منقضی بشه و دوباره باید بگیرید ، تمام حالا میتونید توی هر جایی که دوست دارید استفاده کنید
Base url:
https://qwen.aikit.club/v1
Model
:
qwen3.8-max
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7398" target="_blank">📅 20:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7397">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBEvAuQBqbbAhrGFZxhFTGTinwU88kq9vmpQa0JgR6kOGveiaqA5FM7Sws39jQ9O3smtBFuIPgCrX39shYTDvHvUmfIHs8bZwKmIiqW1Ca2SIIrXlpmRs-Ioyaxxj_07uV9KQPW4db_S6-ukEL8o_mKe7kC7QRTiI6dL0i8R3Ksjm0H2uE52WYi7eXrx0o_1BK2_QqhqtaZRLGQyOHWFPnyqckDIRNwQEYVfouWYlWzDf5A1V8_31uy0gws_M4h7hBFtx6vs0qFDl6GfjsHktkohK7HFGmmlw7UfSFutfl8pxZN6m4YxAWzLY6dQYUaEjVybFpAPBZRrYc9U4TWGig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩
‏وارد سایت ‌
Cline⁩
بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند
این سایت
‏حالا توی ترمینال، ‌Cline CLI⁩ رو نصب کنید:
‌npm i -g cline⁩
‏با دستور ‌
cline⁩
اجرا و لاگین کنید و لذت ببرید!
💻
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7397" target="_blank">📅 18:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7394">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url: https://www.fastaitoken.com/v1  Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471  Model: claude-opus-5 Model: claude-fable-5  دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
…</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7394" target="_blank">📅 16:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7393">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url:
https://www.fastaitoken.com/v1
Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471
Model: claude-opus-5
Model: claude-fable-5
دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7393" target="_blank">📅 16:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7392">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro
همچنین دارای چند مدل رایگان
:
GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3
به
این سایت
برید یک حساب بسازید و با تلگرام وریفای کنید و لذت ببرید
✨
قابل استفاده در
Vega Agent
✅
📍
Base url:
https://anymodel.org/v1
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7392" target="_blank">📅 16:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7391">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_lxOIji1uyM-O2eOs3NoAEAVjfvz4XDkGib92qW11bE58bOSq56oHhNLBeNHYEw3F3n8nMZavBOyTtE2ihZBP4AYOLA353ZxVCYpVymLv2n0SYirY952Eg2wXqulwiUgYLFaTFIr_bqRgz5oD-BOwtxrgHlZY1UQbANnpJQeCClwIjUMW1YdiSL1CRyjkKlFSqIUgrNi18QBRM22vO2iVbzY5bJerxw-vqTfX-NtlIVZT-ER1pfe43vVInwDtIbjmBYLRMZAJaSYTdEVdLMclGjiKghPNJO_mXqW6K6I9Lfnq1Ce1E6qadk_QFc8_J6umza3VsFjO9ibrVPaPdegA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏100 کریدیت روزانه برای حرفه‌ای‌ترین مدل‌های ساخت عکس و ویدیو!
🎨
🎥
‏بدون دردسر و کاملاً رایگان؛ فقط کافیه وارد سایت بشی و با کلیک روی پروفایل بالا سمت راست، اکانت خودت رو بسازی و از قابلیت‌های بی‌نظیرش استفاده کنی.
📧
✨
🔗
‌
https://www.creen.ai
⁩
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7391" target="_blank">📅 14:40 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
