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
<img src="https://cdn4.telesco.pe/file/VkFA1lTRJyan2GTa2EU2l-5w7CFAHx5_3IMC5PpeA_57SbZPTrWuvGx3C2W_fCvQAlKvI54hlq6F_LDK2yqTyr60g0877wXeSB0WUC047gSm2dHkX81F2nullkrycWgJJLociU0GhPY4d0498TnPrAkHn_Od61QgqGcpDMX5WcpICTDd5y_RtqX6ukZtklS6CCcirWYnsaRHaSsrtoUivW2kB5fDPlmyGdbRvl9XfvhJlJPrFsvXWOsivZfCsQyC8KvJJTJ6trTsYeHXNxJporVnOaBxgrP2suUiY6w_mq-QUDfoP7zuIHfCEyhd3Ltfqvpw1aCAL0hP205hM_8YmQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 11:29:34</div>
<hr>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 311 · <a href="https://t.me/ArchiveTell/7512" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7511">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 672 · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7509">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7509" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7508">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5GSH1jOfkdM1yjTLZXxSfubYr12dbHLWmqfbOpmtFKsD5K4feCJyrXA56faq5UCiCJQo9TxSMTdmy9P5f_KWTOb860SKCgNecIoi053RCyM21XJbw6wAXNLl82wHQ4GbY038_wvGmcz9BKJgQtujivv35FjUWS3D27PfbX24ZRIcbkuxh8Pa_EPRnuX-hnJ-Fxlw8D32Irw-5zVG4PbIGfQC4brZtm5dQKMmofxO3DzeaeONmoMJY8j5n0GdolQi2Sc6arz5LTVLkLqQ1GNUloKg1PQvLbfu2nSbiFaE0rkUDyLRMkm_O2AYyy-_jGfJsqgubwNE4bHmbg4fAjMdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7506">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7506" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7505">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGEbxOsk9_hsd6PjSwQweU8cKwxSxs4kfP9t_GMZhOEpq5mdjtrplTfR6iSLcF_uFGq_oQ4c6wgKnAnxMXYEmu0gVmnhNknwCI1UxdyTfn470NHNqPK69-Td9y_lG2XFImMmWZSqE5BNGlDIc1hnrMouG05nq7-rDlfxINmfyGJZahlR89L9jFUvVaGZ21gtfYBuFWcXlFwUtHX0uaDiWrXDv8QnEjIpCojPCoOxfWfmQpXm5u9AFiNnPlKyYl-rfmqUeWr5oHtUT5QIKVlWUQCfhzBhOWEM9gtFg2m409p8HM0NyD6OTM_HL00GqAVCQtLNtY9mnZirATQkVAcgNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXkhXVtfF3yhH4EA-dXFg93cnpIm9eufS4EJErqv5gM1cw_p17PnVuidXfxn6nh6gQfLzdLcdDppA-RksmZJ6HhuIAuGIOvoQ0QzRhNUdLSmctd_Dwfs6A9sQeL-VSe__1x-fZw6fmQZyq-QM4otnjJZsY35kXLyhn0v7y-P0D4tcxx4Zde8iBW4W2uGwvCBRUVXqQscn0zlqU8A2o5XYwdC0u_PLgHxfyVqaUm9m0D6T5PRZW1sKQ8GAUBCwbjK6z28uMWHcKAH_VmI9BaSI7L5AIwjWjlg0Zt-HJR0X5aRTRdAbFxiTGRRuVZfbnNRSSDNhyQeZeeoH_Sgtdhueg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7504" target="_blank">📅 13:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7503">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7503" target="_blank">📅 11:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7502">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7502" target="_blank">📅 10:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7500">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=EWZJPfcrIE2HmYdJGNNeGzo9YVbnOxbj4CgaZODlnOCjlR7BdDJaQB6uPjlcmN29lXJK5WdguuHROXKTr0u3F6JW5SX6uENa7sIhsx9X4h06neM6LM4xB-gZNMzj3mkhs99Ll3MkXvXFDsnKRmRdzU53UzeAgrSn4hg29Qj4SypXpVo2DcYhWDl91uafVNc1wziRk7oq73ebv2ioKXS6ONCiRf7dfZA4sjJYJItlMyEFu5xZsXSovmKy_M867rOVkOvs8FsNxVXcD07HeDLPcgKQibxeV4uCy0sah7DN5eqmbVJ83MpbOcrs6iq76cQCnjyUTp9BygEyuzCx_qmUGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=EWZJPfcrIE2HmYdJGNNeGzo9YVbnOxbj4CgaZODlnOCjlR7BdDJaQB6uPjlcmN29lXJK5WdguuHROXKTr0u3F6JW5SX6uENa7sIhsx9X4h06neM6LM4xB-gZNMzj3mkhs99Ll3MkXvXFDsnKRmRdzU53UzeAgrSn4hg29Qj4SypXpVo2DcYhWDl91uafVNc1wziRk7oq73ebv2ioKXS6ONCiRf7dfZA4sjJYJItlMyEFu5xZsXSovmKy_M867rOVkOvs8FsNxVXcD07HeDLPcgKQibxeV4uCy0sah7DN5eqmbVJ83MpbOcrs6iq76cQCnjyUTp9BygEyuzCx_qmUGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7500" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7499">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzPJitWRQ-IoVgsZtoB3UdLZGRy93iP8GX6R3EW5ItIvHjavQso-zkvTIVaiUTPouCu9OBPEfi_387HektoKrISuUBFQPM2rtyOeqyMryAa7FKncphZ_XY5ChXPCYzcnQBAA6rL4IUmzDyl_iKal5L170iZmN86tyxmJ3tDmi9bgtQqhz3BxXEXb27C35A-K5BnTJfp7KZXSLMK08wHYeQ9_u8F1tRKLZAp-9q62EhRXnCWH3NfKE1Nr_rHhhPCi5BcU66wWNUaZbmL11jnYzy-wZ7lZgaP09WJCfpQM9hHmPxVqhjz-n2zwSB36cWk-q1LOPn1JzEELcoEH1L5I0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7499" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7498">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=ErmnpLrtSD2ob1G0SAgipPKq7Yp0CwjRi4kSvvOfz9f-BZ95szd6tpfoVUY6Up2aKLV7l0jodFCzJjiSkDl3TEz8xEvZLWLLuXQ-nMmTiY5DDVRSY46vRq8CbWj0iq3VtaQTRLEpSBSPUFlpIHWQ_EiQLBWNrMUysQfRgZf7SGTqPG-pSWonKDgowtb_wr0YIfcWpTpA3Lfqu0QRob-cNc9Gc8eKRzoRdES4XO6XCh3eC4pZ5UAIFkKWMs57PNAWBOIso8p1WlQusL2oC2_ulQHdi2ZtDNTPB8zj6TG91KeY5xOQOPkmNipYUVnXSTUqH8D7VVcJ_3t9pwmR5Ej0GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=ErmnpLrtSD2ob1G0SAgipPKq7Yp0CwjRi4kSvvOfz9f-BZ95szd6tpfoVUY6Up2aKLV7l0jodFCzJjiSkDl3TEz8xEvZLWLLuXQ-nMmTiY5DDVRSY46vRq8CbWj0iq3VtaQTRLEpSBSPUFlpIHWQ_EiQLBWNrMUysQfRgZf7SGTqPG-pSWonKDgowtb_wr0YIfcWpTpA3Lfqu0QRob-cNc9Gc8eKRzoRdES4XO6XCh3eC4pZ5UAIFkKWMs57PNAWBOIso8p1WlQusL2oC2_ulQHdi2ZtDNTPB8zj6TG91KeY5xOQOPkmNipYUVnXSTUqH8D7VVcJ_3t9pwmR5Ej0GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7498" target="_blank">📅 22:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7497">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WT75s6LloCj8nJFMJ30bF5ElFSMp1xUCM7hHCP4Hmvk8fbd0zNIjVl1JwhVYOS1gV1hLpqZGHCPUCz1ubO4qqyIiZV0ABFN6dx49Fg-8v8ypQnerk1G3kwCUaTU4HHDPzRtAwvxDiACT8vOu0pLCmClB-CgbLuD8TR3NLD6I-uxUQpgs60c2CsXfuXk-5yWzEXFvOjzn4S8UKjKwTR3zGFAeVJxbAnp6-b6M5cSseSv-HWV07zNqrT7LE9oc-KBpJ3ZHiJwZQDxXB4uOwWMAaOw8lvmRU_uVKjo-29K2Z8PDrLXPX-S5qHF2lVxbSZ-xW9jvWER_Cik3tE1kcyXVWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7497" target="_blank">📅 19:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7496">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRIfCS1hMMiS3qu8GOHWRnO3vtShBwmR8ZEtKIUViSt08sHoH-yuCp3TLMrhCtyz-OsdVcVudFw6tvh3zvYn2MjkNirJBiUJFOkRIyZqglRCih1QaUBW0lpIUnVVXkm_Z3RWBtk7lQYPkukYgx7OyVJ9COh8Zef4FE6No2qratyqUXGvDi2ijfy5xLBxp4QzP4BHnfhmcuanwAlkpsVP7o2pD9IF53G6ltDwVcYxWnStWxyYceZkOu1DuTpkT7UpbKCtC1g9B5cMs6KSyle299KGYcguonuIDS4prU_gOAIvWo29LFQ2XPc8ItVIOA0zz0YJTj0Mcq1DUXzeeLBhJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7496" target="_blank">📅 17:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7495">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=YIx6qWikUzYQCQgYhK3E6Fr0Dg-McdQjJvIlEb4phy9uurqksPYIA2Uxd9Y6ROxobTqe3_1-R2U06IX8GD7DJRJ_cQqykuDOCjF_93FGMSB2AyZ4h8URzBaHpoYHv2c5iHB1-_S2MmXe9SU1qqQLN1Q9qePhoG1rfY7AxWZFJvvlaNrpH-LmqPD0Pgp96Vb-Lv65dO_z1q4b_x5Npqh4Rz0F6AwiDhFqqsQrJV_ZWWoWkmyCPcakCwrm7bwEdxazqw7qlWuf7mAda9Gt6tLG3BC2p3JJoiG4DEphxCzCw91JXqLqIus46QV8X6_r05sNz62qyX7VqTZKcD5XUR4ABA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=YIx6qWikUzYQCQgYhK3E6Fr0Dg-McdQjJvIlEb4phy9uurqksPYIA2Uxd9Y6ROxobTqe3_1-R2U06IX8GD7DJRJ_cQqykuDOCjF_93FGMSB2AyZ4h8URzBaHpoYHv2c5iHB1-_S2MmXe9SU1qqQLN1Q9qePhoG1rfY7AxWZFJvvlaNrpH-LmqPD0Pgp96Vb-Lv65dO_z1q4b_x5Npqh4Rz0F6AwiDhFqqsQrJV_ZWWoWkmyCPcakCwrm7bwEdxazqw7qlWuf7mAda9Gt6tLG3BC2p3JJoiG4DEphxCzCw91JXqLqIus46QV8X6_r05sNz62qyX7VqTZKcD5XUR4ABA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7495" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7494">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Etgsyf-EN-LsZLe61DYk0PSfBy4Ei_KollGqhOSb1SWMcbvlQxRRQTpf9rE8GAJXNAREacX5YS8ARXvexE0759B8MPbVmkTcjXts8-lH7aFL7d-gqtyUTyHqVHlABplXisMEVDT3pQH9JHX5qy-rsEgb8RpaGUMqBQn_pFbZvR9_E5Y7FzA_Ug4tU6BOZRf630GMt1L6RxtSzdhXpiu8M1WZG6RWlKhxHEtHHO1I93BinlAePoaV57IXBl1Sw5W3DlGtj-138QzcFY7lzFIEwjUFQ_q_u1VPM7lwIdiy5Ubku7i_gVCT2hWQ1wmnWr8wwea9lPs2IHhepIPCP6HAyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7494" target="_blank">📅 13:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7493">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YT5R1xYcp4mn1C6RTY2wXfyFSXDLWPeBf__YfG5jX2eXutnSvVsNB-TJdDb5mZH3U3Fpkci-Il3copV1zkPoj8m9tLtxianOTntzomaVN1SVZ1du6j_QyqILzC8ZfUpKGgN7Lzi6la-w-iwa4lcwtyeNuU5tF6_QAu1i2qtSiAhar4Dud2QIImb9HrTy7N13NqzmAzyvI-OkfwowiEua5DUsSJt-Ggch5gS24NyqrwV1HkmWqZo0J5ExSjrDWnDk8jYSiXdticZoNaTwwhiDkoZSZHWbHrvWkAXs2wVvLpEDSiKZQE-CDMmLVj_kcFsh7j6yS6Kyd-FtdoD4gNQB-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7493" target="_blank">📅 12:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7492">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=iZkMtk15ZTg_De1QBF872aAwk2TM4UhM5JOrkP43SDLdA7PDxTuvu8KNCks2T8WJyinM5ZzRVOYVYx6KeAGciSt6O9J6-In8f6bQ_uUG8GcP-1TamTsWDL7rMt6q4DlhU1sC-Mu3Gzb1GQjwlQrjGBKgS-zsts8s-scpRjk9MOxsFd4GirPuLqYW6lxlooo1AHlCMSjITBlLi0nqFUQb9OnG29BdH2_NuIw2iwTv8doLvCxuP-zKYbOrTPS5qIlvKpjulZUYWjBei1qUvoRnvMSzAtrfoEeY6WwUB2s77uWQ6qv-UQOj-Ir_0JNbLRPv-ZctfR6LdECMmdRT4TifBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=iZkMtk15ZTg_De1QBF872aAwk2TM4UhM5JOrkP43SDLdA7PDxTuvu8KNCks2T8WJyinM5ZzRVOYVYx6KeAGciSt6O9J6-In8f6bQ_uUG8GcP-1TamTsWDL7rMt6q4DlhU1sC-Mu3Gzb1GQjwlQrjGBKgS-zsts8s-scpRjk9MOxsFd4GirPuLqYW6lxlooo1AHlCMSjITBlLi0nqFUQb9OnG29BdH2_NuIw2iwTv8doLvCxuP-zKYbOrTPS5qIlvKpjulZUYWjBei1qUvoRnvMSzAtrfoEeY6WwUB2s77uWQ6qv-UQOj-Ir_0JNbLRPv-ZctfR6LdECMmdRT4TifBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7492" target="_blank">📅 12:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7491">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7491" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7490">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7490" target="_blank">📅 21:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7488">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxQ1TVHS6yNl9D8_I81yuDqhKX3w-ct9OC0pxj4rkhfGYIMMV49aBQcum6DCbsgp23T0wN5iA-Q-XaeSN4zmAfrmVEOsEYfrYH75jA-usHpbp01Xz_TNpRLheLiIXmFPiFK9mxCeb_9Qe2IFzcYX4qdRXpSOO123JFcg2MvPYI1JZkCc_BrOpVV0fgb9AsMH8PeJjS-OVQWKnrYMNM9LeX8ZCHioLdqMATy0URa5ATvgpuvDPyUzXL-GDVzm6o0EO-RaQr8MeYs1UVDjbCQojH5EbZYa5WpuaMjpQA-fo6WEJiY14zaigYOc8LOysQs7jQzcDqr1ceMVeS7zzv87XQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7488" target="_blank">📅 19:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7487">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKaeY9ZcbbSSJcohkBtO_hf7wh4h16Pa6RfejD_5xVHCMcP3TRMLg_0lQo_HoOvjZ12dN6HZ212dBvOIJWW2I6AjCF7c0J8XdSzPDCmCN4d8RQVHPR-Ff8i0dvOpLaZ1gCW5AmhKm4e3AFS9yHO1NXFw5zScs4b74yuh-nEwe-eIsgeXdjpwqhrea-VGHwNgXtgX2mY0jYd2lhTb0VyezNURDUOtCA2g3e5-eKjRyM2w_5KdEL3BWw8vLjzTa8ITokhfPkpMu8uLdrHnunhkctKlJ8h5L4evZ6JYUX27ZhXwYAhThG6-cgJy3IyGR0gd_dfl5g3xu7kshnMYx5HEBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7487" target="_blank">📅 17:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7485">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnPIWkUtUy5rWa0O8974KxjTtSDE16T4Mgd7DmpI2_F_SCXZ5BHATF-ElDd990ffXOltB7b9Rsdicvh71uByPAJWOlHJNBIUGwnvPfs81TzaTHlsBc9vA8TQS5xTZborw40C3uE1rhfALfDz_ZxNaxICq-GrUeGmpCE6IVq6aBVFwcPkHHoswcMHOujGzLI_7ij6mPi5Kf1fU6VOLz7nSOzSnlD9fy8643DonFGpPliebUXN07MMlr6aoImDyVJ8efa13hKnoQfH79mLq0akedNQmPpvs_sId_rn1LX13FXBNEDbz1g34SlkS1G7XYeMs7BpVZqjNci2t6PPYSOmsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7485" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7484">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfQcUlvrVHJvvWEX4UMqEDpn9d4VA-7Oh4OxnY8PrxHO1WOSndwG9f16NIKNQqVTs9m20bRuKp6XN96n6BfEKSTORgTy5IL7kMI-CoGeRCs7EmqzYv0uSSGosPQSkEsmn3CYuR7Zh-Hn_ahVf4_xQALPg58AFHGq9C2SVUk8_QNdh7hkDoLDawWeFYPVkNvNbu_9rBcRC900gh-d1UCrX-0-sqQ546IcGkVSzYGPwuWVI7xB-e-cYIktUYX719wPpJc2ETbbhVMBCK4niF_Gx1wCIFlAunVpV90U8-X--2ilQrCguLv3RL5a4BOJPP4u6diUlqTITh_8ECP7nzD9Cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7484" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7483">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7483" target="_blank">📅 17:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7482">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOpv69fK7xHK4jJrEUlR43T61jF4M2rLiUyR8kYPJECIDI0TqNxKVjSqY6W3qVEtv8K4r3GQ3Wf1J5wvEMaatU3E6EhtDSL1FdJbf_D0p7pxJng3ruJ2V051L1cobAIK3P1c4Ri9ZJ2PGQHe0ZvAPmHZ_N_J6G3lyD4WdKm9UIUO7McBEl7gKKDF_j67JG8y_GnCFMDpMmyma5ZMXv9-ZbbUeIk2tS9J0J0jJc_2HK1By3_48azUrLk_aTOYezXpCGQ6haGXVw0dWQZBuyHULybJD3AfRrATGhpJKmI1VHophHzwwjiF430shky3HkBci-QhmFtPsj271h_X9SbUrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7482" target="_blank">📅 23:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7481">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWOEa305RCOo1o7WsIoNqLGLqBiKxzVXs8-cMYtKJAmG1E78KEcr-FvFZi0XpE1tbBQsrley-AnihErpd2yy45NXSHD00JKUTQGvnm0vbfgmje1AAq9BtrRr9Z04887cvgsWNMjFFJCS4znmTc-eNaf1azizZzBjuvXSYaN6JZLuCYA0I7299N6pvn2wZJPPeC4esye0vKrTzO3KCdTUAHNaons2oBbucOlP60cYlDaSHjllC-l3bd0JSfzY0cltPpcUAY4hAbDwR5dQGHrYoGr8x27IgM7_TQs-I8tAVXAUV-F5Lic0k2FVKJkO2__Wkp52cPsSO-3ckZoKLcyuLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان: امروز از ساعت 12:30 تا 20:30 به…</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7481" target="_blank">📅 15:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7480">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7480" target="_blank">📅 14:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7479">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U84xXIIFbuodG8jT1MgkWsiGaqHiLZbYNOjCYgoAqwyG08m5WdaEm-K1utAOOBp1c9zUMluzKLM_UWcGpgmIwTTS2DPMtrjtYh0z2sgbstAKUavi-XnaI37RHNtSFhWrEpOCxneNH47SakEqJV49LA7iC-JcvtOs5mpRLImgJ-0A6gIXngKk559yfAbr-v3hPIAN0EJFlNhuiskRPr6HDBrslZze80hIQ1FP7Pb0TxQjB8iXF-ceLnbVqUs0LZw5mzRZ15UyzIMpGBYeCdu43t12U6CmVRSciXKZOHd60eH5PlqnWmqyOhMVk2F73KdYcUV4ZYFhoOXYHR0eGuHpkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7479" target="_blank">📅 13:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7478">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7478" target="_blank">📅 22:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7477">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">Gemini 3.7 is out now
😍
از اینجا میتونین رایگان تست کنین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7477" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7476">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evM3KCAaGRl8wRdtTvpgKg6xmFejZwuOdcbgosJD8wfu7AjNsoEih6UJIUkfp6KunFuP55lB6EZzNbc6ATpIWgGddLEjt1UMwVkJh4msbF_JA9mygAh3UtVGoslgA4nE6B8PpGWAe8RnJm6bp3iyypbq9Sjyef5r3pF7hjSJDdzo1K_TqegP0LbJrV9l2qgDocfkJVe9cfCmpaFWbnTKCjkVsTkK-NmAk02CjPhIk847RkHrFeM2NnQObjhgwOuKgysgpbqz9yqZnQ007psbGO84jJBEBysCEmlTvCZ-Ej9b3IJI_CplZirnW0XMGey_Z_jVreOaPQJC9WzTeGd0JA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/ArchiveTell/7476" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7475">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7475" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7474">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7474" target="_blank">📅 17:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7473">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bn75LTcUHEz_geMJVqM5jt0avFmLxjKci7dwT-pr63efWrbt7Rd2RC5w6cVxEKIEXPI8xpPPGJl7d-bUNQxClDlu2Lm4BngzJulnq5jdXzTlg7w1nGiiO_aUcxZbRN-d1eiw-iJ4YoVZ9XNdRrWsJJfD_qAZKb1bBiLZB1lgxxeg3XopmSu1RwiYOqRBSRU3yjCeY0lNxP4MLaXpnhaDi-5iW3snBJUHk5hpvMcBgGUKLgJ_ZInbs95rGEW2iS0C4rq4Ljw0QuoNyxB3gsdTJy8UOHto40izemuWctfIOGdB_0yZ732GUfIBOXyR8RtEZ0DI11YtL_x5647Q7Nc10g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7473" target="_blank">📅 17:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7472">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDcvYAIJAv-wO1mDw3WsyOPVjR6OdM6JVH7RJLXGGhHrm8U67fa8eTPaSjHYifwnyn8XNbXafTcFh4Wkm-uVd-X76-wDMlStpb_kc1bvsih3OY-el1QRAgV5XyR2gILerjYyBOhtrpV911NWxjkKMq7_xgejyhGz7bVmY67qsAsNLAEX_4v4RzFY-0K97rbBeP_Nut8Pr5Ithw8Z9pT5jGRSB-KhgauKzx3Lcu3U6_lVy_pyR_g7ABZBrBf0bnZacawMf-LefvpH8NRvJdXLjHCVykKbf7IAYvx8ILEAsfobuvv5AEwFxBMQlGA2fZYulgsrFIy2ZmblC9llXoBz2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7472" target="_blank">📅 15:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7471">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7471" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7470">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiNACwpLaVuO66kVV0aCGt3FpqTWoM4E6CX2IWxuFYZb3NAsXGCaHkLknLw4zoRc3fsCyagei-i2cwhMkz8iQKItS261oNY3WOjA2FNQDv5MAmspsuZT5Wo3PVlMuy3D2kjr93ucELyBr0DR8Gz12lpv7wnLWYcgiUObKiNgPALahEWoAieboXPzlp5lTZGFjChBqTBYEu9T1PlEcbUbdSSB_JUb8aOLLvTtNnlgJMrPYJcuaByCNJh7KtCVYK4AseJDzFI60SbUTPIqGOtRA9ptva3fxLEeqqlVupjgbzJDei5z6ehyuQQoqIEgYabc6PP5fSDCIjMu2nO6Q2rcag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد  قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود ۱.۵ تریلیون پارامتر داره و قراره در آموزش SFT و RL پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:  چند هفته بعد، Grok 4.7 با حدود ۲.۱ تریلیون…</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7470" target="_blank">📅 23:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7469">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">https://t.me/ArchiveTell/7053</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7469" target="_blank">📅 17:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7467">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQslcfKoh71jodY0NFRHtfKEiGu4NE6pCkg_OTDv0yjq1YaE95cPF8qQEPxZHFsMRVXS0Ey1NUL_aOzNeS-2JJbYoZRgRlMsHbGNByyWWSu_Moi7ug45kyfT4D_mSBekDtDoQYQw388_CELqAb64NHvMGAE4MrDvRDJeHbdusheYjV3GksLP5kTWRgHZVw8SFSDobs5onQeMCXT07V5OWST-wLGCKue7YNoc5Zn_pWxTvqBkL10wNfqacfnQqA7PKkdl8uufnSqgjtXbgTVIf1c99Utr3Zmo5S9GsWy26bko_vR6UtIr4R8mCJb80FOdGFU_JnkZCd90nLh6RG_xhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7467" target="_blank">📅 15:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7465">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7465" target="_blank">📅 13:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7464">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7464" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7463">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7463" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7460">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukDJNUeH2tXZi9hJ6Q2iWMSJ6vUi636PoE3aHfruxv5twxY3KHiK-kd6EY3-jgbb4CpvPqckRkcIwj8XsqG_iBr1muMAtge0IvXi3axBQSLQft0mmONbAcBKCkfm7o_RLvbKOdnit4IX74kCKoLA5rjHnZVklIqwS3XSEq3LgGAya3XeS3TlAra0HHNw-9W_vjecE1n9XJY4P4JxhRmKGLypEqwBbVpboeV6wZarcMJeKqATR4PnOzRK_Ney_t_sPRRcbiI8mnYqiXzrGTmstW1NNhfTox2yQP543TNCNVDLRq1XHc_kUTvvAJoZ9JvUKP8t6ZkT_CisjI4uT1j-Xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7460" target="_blank">📅 16:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7459">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbxS5zhJJRJ_IxFdqCs3AIOiF0Cr3qTT7bMX7PZ4W8XBYfGlouIj3ot3dDO3uEtx3_stev5LUnED2dZfMbVpFBkvLMNh7AocoHLf4a4TTXn_HibJ7JqTUySD3sWnawIilo0vDwsT3bGzXS4tzvzAUe0Tgrk7S-N_z2TGY2mzNIiKswnwYciMQKNVYMKjyX8LXb8eon9hoevPLzQkVklA6MTIyyb3H0T4MEldq-YeN-aP5bX41y05siJ8a0yoyGhDGf2V3NLEpOjgvFIOKQxrCtRFPebcBNOEPZwOKmp1QivHH-7HDEm8Db5ckNIDQvue_MX_ocHSlWJQO8evkgbLKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7459" target="_blank">📅 13:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7458">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7458" target="_blank">📅 11:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7457">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7457" target="_blank">📅 11:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7455">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djpKZTUTQQaBWI2mwzu3sdITabeO3b-6Zn3RQgFC9u-U5ANFhNt6X4Fr3HiCn4FzeJ8wOc7Pm1862opUyfiuJAgm1VZyI75UEcg3HceEujhj7SGxCxmtbirCQkQfIABuY20vbL7kGx-nl_89TbuKzacmBPaQAgA82H9tmsnpzbEwNpin5G6hx1OIZooEGiZRH6O1jpHTzVF6FWp49RI0gIjG31U7gswRqwKKFk8em_cDlejbP0qTFSB4mJFJJ_D62uZqXGNldd1KVMpokkAgmR_V2CCo9s3k0Dcal-PlMd0OOcWCCc8FRe7g9c5ag8lsw1OZJxNZQ0VMJWh9zo3CGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7455" target="_blank">📅 22:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7454">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUD9rWPDpjnGJ2gszPrnk5t887ETCrJ1u12LOk7q2I0F5TCZFinAEYD5LUjWYSwH5nIDNkY9DPC-Zn1_nECyd0p9p0qLKaX95LGkgQU905gNMVV-dfbaFMKfJc1yRDpCZW8eQXA67Te7XUvO2JcpAkK4LGcAbPOiDj5NWMWaNGRv6mjHyRLm-_1O_cIAw15KPXrhZUiXRJ7sbMpyHs6V00BzD0CCVVTBOj6AIesd8SK0QZzCdruG-Xkzvww572t0hO1Wt6pbovpQyE9H6EjfMn7q5JhzJsDR_oANey-zFmp_m4m-eG53rQvLVHrzO5ybwtnd_CDv6QzRUN5AALMzAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7454" target="_blank">📅 20:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7453">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sy0kXsQ7UXYlIg-IpHWv82XTohrUJYkP5IZ82VjlhrmokRWu8m8nw3Uykac5yYEIeYXyBOKEEvvXngd_Co04n-XanMEUe8tes39MZuq-GK3E_TE0DFf3CF8olsXE-BVz132MpOfR_O05DhJBiXVkZX0HvnmuaPI5K3ezx_Dx7yEZUPgAhCf2NjOyRVwfN2GHb64GQGarx-yGvEh9d4wCdQYiyyHifXXHG9rfhg90OPVgmb4T3vk05AnT2X4QPoMCCyuADfkvNUEgYesST0M5UrWwOMPE21lZW4qD1DeKcDvDuYc759UsyumkUUFiWVifQ-rG_zx0cIOUakq1hmCyuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7453" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7452">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/ArchiveTell/7452" target="_blank">📅 22:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7450">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/ArchiveTell/7450" target="_blank">📅 18:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7449">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bt2wcVwYFsheu5qlfawolr7r4LFcm1YtV4mfUzcosbythHtBaSqHxB4ZNwzuXeSvvhFYBBP96aC_CgigrQKUkIN3EgeeD6_UfEk_WWBGHjLws78FsYOZJHLpygMh7CoovSZcYlvVfKXqaBn7SgQha1LmTUtlkBbZuxxOeZlJfdRlEQb8BnRbfqpWy3wzDXGrEuY0NomvPAVL3rd9UJzlJjTY4iPFGkNBOqrSfF33s1YpZd1l0C32F4wg8bamLq9E_3Nb925ckC5rVJP1E3hK3JSGlj8RVl9sUNrQf6HyDY9pkxEqwAW8pL00fBDNzmNSWgMKdNdGwJZ5EBBjHkDG1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/ArchiveTell/7449" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7448">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIKEHP3Cw_hn2qvtJI4WIywjdHDfvMgN8K9vlWlqrai7a51_jem0VGCfzqE1HhTpwr7TdkfCwlKU29l0VPFdF8iawGZ0icUBseOYW-NFXB191vPFTfRMUGAUwsexnkt81vVYriuF4SDbpC66LGQdQPvymtvoHIBv_1XRSD4_rJw6fANg4yQI97X7uRMVThI_azBlFHG7HA_NtnDh3L5ckVWNFklS8pcvrH6pxndVoO3ykr8q5C_REtuoGXoyK9_gOzuDzan-MyUE7BRCqSJ2dQcQnCl8Ak49I6J32N8ueTAqOBaotAMA2ZKa37vsUxR3P2GElc1qk5IRhvMtSdqUxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/ArchiveTell/7448" target="_blank">📅 18:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7447">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnRCCikbuJvV5RXfySqwbnXReeTQKZjmYyQ0ZBee_rSc6fwuUc3BEf60Q059tR5cLsUW0AksyzlhIgj0jq7ERAV82ulzbnigEgwZ2tmPrCu5b7tS-OlVm0KzvcwGA2BlZmsN24vedVR1WOKug90MEftb5nG1fnQeeMJpmWD23QZta30M23N1zk8BtKzchtX3JZsMtKPafTJzQrEKE9c723fln_x09RaR_Eb9jENTdPe_3a7qMSVMRxosRdDH9TBF4w3RcfA7eNMUL0Gl2VwSdiLIUINRdsi8vDIb2vHZ8X4Qp2HFAxPv1USXkCwXnVok6N_mGeu1xXi1N5nOQ7CCow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/ArchiveTell/7447" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7446">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYdeZoAmRDF7lKm7DKTnCopOe4jf3XFVUk471iYs7uM3VvFHgq6sDKUaaMPUUW4A0mj1UM6RTUrq3wEC2QDGtLrajsRum6St2zlypEpeNSuizWTY3yGtPYkeRRakGFsLI-e9MrPh4GoF1CUAjh94XwICMc3z3bpccvAFsm62GfX-IVJzFpfLT7w6AHFf0cfg84c1QmIarMXvp_f3Dr9PL-Hf8gOMXKODaSX0-9ZV1w4cfF3were00IXfKHiKNnGjaxcNkotPngHsvKOpL5ixC6Hre_OjQzVlsY28vRf4cEbZ1MBdrc1uESZjFZB8PkBS68eZeEr1CYKq323I3tVHYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/ArchiveTell/7446" target="_blank">📅 13:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7445">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/ArchiveTell/7445" target="_blank">📅 20:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7444">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=o-7vlxdHJyiKEPQboJeW0PVCSwdNKSjAhnt1F1qIzZnguIN5UnVO3_xGwSgUCpcL3oMI22PyK2ouQu7lhfviXX4vAckWdGqBKFXqo0oA7O_F9D1Pk6bnjNt21lrZJdIxvazZZ0BbZWpGUxCojerUvXbhoqSsjbO5Ohg17hlKKYbb0a8tCv5I8JbmL-8FQUBeBqJhqE0i_7yfs6Xa9_X_7MV7cNyH8oD0d5mHE1b8I8tuvvpjgDZPjrNYBCgBYaZCbLsmH1B88beP5d5qVlKiA7qX_-T81-yWRMBU4mU_vPIdIFKrGNVuiixgt1eeXgd3EsLt6lj5WEt2rf0xAzDGXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=o-7vlxdHJyiKEPQboJeW0PVCSwdNKSjAhnt1F1qIzZnguIN5UnVO3_xGwSgUCpcL3oMI22PyK2ouQu7lhfviXX4vAckWdGqBKFXqo0oA7O_F9D1Pk6bnjNt21lrZJdIxvazZZ0BbZWpGUxCojerUvXbhoqSsjbO5Ohg17hlKKYbb0a8tCv5I8JbmL-8FQUBeBqJhqE0i_7yfs6Xa9_X_7MV7cNyH8oD0d5mHE1b8I8tuvvpjgDZPjrNYBCgBYaZCbLsmH1B88beP5d5qVlKiA7qX_-T81-yWRMBU4mU_vPIdIFKrGNVuiixgt1eeXgd3EsLt6lj5WEt2rf0xAzDGXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/ArchiveTell/7444" target="_blank">📅 18:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7443">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7443" target="_blank">📅 17:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7442">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فرار از زندان قسمت 3 رو بزاریم؟
تو این قسمت Sonnet 4.6 و Haiku 4.5 از زندان فرار میکنن
😁</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/ArchiveTell/7442" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7441">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmZqLLDO12F1DFAY9sf7QEV8LFIxw35hx_3WArzvNkFdA8YbWXfDeQ4wVU60rFdb9j-A1Gg-Bsjvdxl2Q7q30F9Hu8cYuHhEcmwjJLUPjawuIao_v8adNwRAVY-ue11wLa1nixk0Ts3kxSCpQM-s00KPYGEdY_ypxSPDc72aPD8UB4dOEDnu5OedC8Y2cZBmJZ9EZTL0BhqLg5AxD092JgpGPBoP_ZFzVYpDMKc8KqWNOamHKv5lv5kfbBXRASgo9yVSGhZJkd27G8c1DF-RNVABs1zw9luxxx0xBs-bAZ-SIi8vs-MG5l_6IPgJcYcIXC2kOWTecljknPcr84A9mQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/ArchiveTell/7441" target="_blank">📅 14:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7440">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/ArchiveTell/7440" target="_blank">📅 22:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7439">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شرمنده دوستان
😢
بالا باشین
تا چندی بعد فرار از زندان flash و glm رو میذاریم
❤️‍🔥
بدون رفرال
🥹</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/ArchiveTell/7439" target="_blank">📅 22:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7432">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=vwqkhFt-BoJbGTd4sLIByhXO85ItF1rC2CvrvOjqr3I_qFgksPcwN4onBvQr2mdE1E3lxVDR59MIdrScJARNzwQuT4QXTZ7la0V5fWikQTrHceFuS6BRq09QRVOySxyebRsql27CvoHJlvSGZ9LcfkI2VpKmjATXBjfaQhG180CKE-EKttiKYjZH4YT3xUZERC4HvwnpGzGhBh3M7cfUOI1IDN0fTQKuSgVwQwioEl3ZPpBghcznWEDbbN9M9V51QXlR4yznTm7KWrb07DhCHX0sAxUPRqnixFBFSJ8w7oymoUDplpeeVEoDXDcM1NetWnFf4vS8vMMVklwA2i4BNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=vwqkhFt-BoJbGTd4sLIByhXO85ItF1rC2CvrvOjqr3I_qFgksPcwN4onBvQr2mdE1E3lxVDR59MIdrScJARNzwQuT4QXTZ7la0V5fWikQTrHceFuS6BRq09QRVOySxyebRsql27CvoHJlvSGZ9LcfkI2VpKmjATXBjfaQhG180CKE-EKttiKYjZH4YT3xUZERC4HvwnpGzGhBh3M7cfUOI1IDN0fTQKuSgVwQwioEl3ZPpBghcznWEDbbN9M9V51QXlR4yznTm7KWrb07DhCHX0sAxUPRqnixFBFSJ8w7oymoUDplpeeVEoDXDcM1NetWnFf4vS8vMMVklwA2i4BNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/ArchiveTell/7432" target="_blank">📅 19:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7431">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Llslf2Yn1LME5IhFE--EPY10C3fJYh8D_sWAuo5pzYRHoWAMwA-sOXrE4bPTq43w7wGptbXkZ0bBU1r21ts3I2HvU73BTnwpZfXpe0_GohW2zLBiCJLynDK8Vqo3bGJ53UY5D7STbwiYXGsm3dt0uWGsipkw8IP0ULhD-noxwGuUgFkvllOfehJzDecggB4iwa9ExxfR5K3n84okEuk1p18SbLjp-Qm4Ct7C881ecHWENvOZX9HTDapf2beAIZoVUxL_iEjyse6O5KxoezKixJVlcMi8snF0Dz4g4_DAUmg1WblBLgDrqG7395Czmjhnm9ABtivhqoUPntx5_XEpig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ArchiveTell/7431" target="_blank">📅 19:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7430">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUgTcmPkLKAjnl1UD0V4XY3ncIUJclMuSZxwEG35YxxCvz3N9YPMSgvrUWe4NiIjzb6MPdUtVVJ7fpnYLX3onHNiLKAMmFlUGPJQQAIeihqW424Jkh9_9asSwCLLaThRxTe-3iO1NaAPuF_jVDYwh0aLdIZqU7oJGKJ0iXE5ltSw--riTqF5Zhlwc43CBXsyL4LSTSMScVUTHErradLZzBbybPVis7vZfGduqbH8bN2s5-gWGNOJ0qAobmlhXl0rN4Ks1fFBlW1M-909B12OYlRyBpbSi2x9UW7SIHrU0Q3pzKvm3ZXeSiRKQKWBtanNg3tBTzCEZ9XEo0DTqBVcBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😺
چت متنی داخل ChatGPT نامحدود و رایگان شد.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7430" target="_blank">📅 18:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7429">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHXl6adAVXxbRM1S45Uj6afUDeVSaR1W9vAGwsCTElr7lLgec34c0PZDdtF1Ml0LXYF_EiiTNYgdSCKNK23o_BxpP1fdJcT20Y4FmLRIJ3ttHUhgAvJHJoSkjgmpum-Wv2XMV4R0FtFnxoofj8VYxT-ZjexOLf8zhKcwueQKjSZVb4yDa-2dzd-bM0RkfzvQFbPco-ASfWT_9kv13rTxhzhHJeFh_GT_i_cOaqIY-spkommkTMIcUCYdZtl5RIkd7Wsaz6YdZAAwkClyCPp2i27n5RKHzlNrFg2cn_A1wINIncrkHaBmxUupKbW-r5HIVRqtGfG2OppuIies4c2vSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7429" target="_blank">📅 15:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7428">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/ArchiveTell/7428" target="_blank">📅 12:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7426">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPSSvSH9s93gSD1shQWUzgm6__o9O6_3gtp9f9i5suXvIQ-Dw9Srtz1FodPW9K7gM0q3VpuqEWbu18g11niwfMjqYLqfQItmXCYef1SsFROza84f84hzGOUJRrT0FHiJCxnWVs-s6C0x4IEE1nsVL70uPtHO7bmqDuToXnHVZhSX8y6rWHxApyn86ZCV5Cd5HOSEyOFr0ol53AchExYrH92z8ySbr_MJO3Uj6MhvLcmLLBxYcEPuiztWhQ6TINRQCKpiCyBNOM0d5Ims0gt2n5nTrv4nh4m3tB77TlQmV01K56aXKu1L9BOMTBkEyzuFNr_pjyYZRJHxoMpnwURlwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/ArchiveTell/7426" target="_blank">📅 00:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7424">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nusGGZZcA1xtya78VhIIAl4ZPfpJ7TS1W7en4au-M2jYwlJbpsBFX-HuG_HMJ5I8lufD-DsKZtPMiAs6WUcGmWAAozhte2ZEIIU-CcVi5qF5I3h0Q4dY0vMOJFeulWGICKUnGBKC2094l0FJcBPKzx73FW5NyXddOvnce9NxTzlN51TwP72h6bMKJea_SqqmnZiUV3TUeMN2BGOKwFTgErFFFHo-a9aVTNc-bn99GtbkeXOxWFL6k1JS3tHZmZBtjgkkPp-SmpSY_OMF0JYlrvKsZUXTDdRFOwAMoc8t8Xwd2WikuATTAGD-juwpXYrt8N0jM1JD5cPTxHF5L873fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ArchiveTell/7424" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7423">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krmBy6vZ6v9mvl7qj5I7M99yGmwrX8gnyetKROlwTGkqJsD9AFrFPqeTyzJouUm7DWqockSWiTfFgeNBOA5HGrJ1MpqvxZ649_R6nOgPYS6if7MaRQmiQ2tLl7ycf2BZNrRzCbimLLJAhHbj28xDCBRypVN6QFDSMK3H6p7HZAre8dCRB24AKjNKXVWCVCSJl2wFCMFvsEm2FoRo9Un-BAEJorN_Hl-5MU0PfrpaHsQAlp3Nd9iFTXe5bkI_5ImQf3GOGyd3mWx4iCqRCB9Y0w55jUJYk52oo-gxP1ZNmn2o0rpij3vpB5erxLy7aoBa7c1ZL-Fqj523ni3E8wAlPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7423" target="_blank">📅 15:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7422">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnV8tcDT-0hexjlv_RGrwEyNRDNmtxSwNOGeHMQw1_bxK5R27YjkLGvBhoMEgXtjQdgcqk35c19eF4_G2v22gQ4m9mS-3_0jSyKjXvv7OdFpW-HZ98GR6sMdO7IHvDB462dC7T-K39aX4x3NUXC6sFbDZWzl36UtVk9VlAQvizlCOpBjffnzt-SWtgABPTTRqtpjWRCouqkwEnI6Q_2T5v83Vs87Q-zwAk4FdeICXppfYp1KpbIJR7RkrGLzh6pCQHGKNjZWFSlcr4uKzXk0yOPMMWqZLRtTA_xsUeMSaoN_F40jx6JTR6PJyJQbBXcje4EvBoBHIj1YauexAWcecA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7422" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7421">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2Te9LpmKA0kXIVmgxIeeEpf2C-K8SD9NEJVQQsySUlhIKACuH_J-jkfr9EfOAQT53V32p7h2XW4hDT_v5BVELrSzRAZs6XBJDDUBmFeI3p79zHeG6jedgXzYsas3KGSAofXFqG16nh0Zy86QBNLSm7B39WhEjpI4JSrcfoRaLU9vNJwGHPhDXeh12P--D5RuySrbPXxWFQ2euWv6I1kBuJqmmj3mdFiA4jGjzrhjzs4Vw-1enXohnNlZQKoybmrl8mC0FhAsVtGMW5820A3R-rssP4huDv9QkOZw23zrLpfLIvmAhJfARyACAPSyqyLP6_t6ozKBSECb6aRkpzKGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7421" target="_blank">📅 13:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7420">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اگر دنبال کانفیگ میگردید و حال و حوصله گشتن ندارید یه بات پیدا کردم خوراک خودتون
😆
میتونید با رفرال جمع کردن ، گردونه چرخوندن و دیلی چک سابتون رو شارژ کنید
⚡️
🤖
@survpnbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7420" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7418">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uF5_a1L6lAY9TwzZ01H85qGe4LGcILc0g9jCJ522sXf4gC3DwC4vix1us_wfqZPME49Qz4soyPU0da-pRz_d30GyvhnZO7meh1MHmVicGK-qax-cSl6HoIuMThf1FevnWWMizaJt_zCz2tkAJpnWT5HBUGfj9-6qrkXAkcE_4OWuND_g609tcZ4ubnDJymZTBDifxx9WNpsnmT2dzGoFS3TvYzl_IgPBJBx251lAVEUGzYv4KdxjT6sn4dMbi1-xVJiBE8tOZ4z55RSy2QJLA-t7gEM9qN-34SpCaxFW3xLEbtA-S06elocyb5KxR5788PSoyvkrpb1crnJTpKTfkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/ArchiveTell/7418" target="_blank">📅 00:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7417">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vANuGbQa22aDbRR-8vooci3-IC2X5iAGepE5cWJMQFor5eZvzqSzPbdFjPJlG53Oi3nNxXfETEQw04Ps9ueMyb95p3nyjimy3HJaEDgz0YPhm7hKOZcyhYNV4gaKXRpDNV7cno7vr3wOdReb2jPGY5WJ_15nMChCYOCy4hneb6yvGmJbH_LfXGRvZGuQZyT6x6gLkBIkRkC3cPn2qQeC-WBXp2-WBJ5jdlBXqebn8FMdPtAWgE54BzBDj1kzU5KvEYeFfbTQ354U0qBH3HprcRZFzTwd68nU5oMDqmbR2eldipLhBB8sJrP4GRlOFVdr3RKy76V7-u5WJ98tnp6vtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/ArchiveTell/7417" target="_blank">📅 21:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7416">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeIAEhVv_QoJXq6aEfsojgk8h_cDebaCriHKGpq-D6dTaxXGf8TaxSJzABIrW8SRiwtCmOj2UoxJvhX1ezqj6ai-MnVgXbafHrzf_6yjzWJngazogrMcR9GM7paAowrLPdaPD6aoHL2sVvMxlB5c56yuEkJ-se4elnXUX-FgRV_5H8Ng5nP_BF-zT2PJjgYjw_KFohU2PZDyDfc0e5cq87b5C_OEuLWrZCi3d9V7rm6Qm-Lq2PDmgKMjl3wjINoVlphCMnP77ZzhHbJ8mJDuLqcobzjvNSH0mPZq4XBwLFuYjSbuIlknarRLQEHpXEsBES3NQqEvQpKBWKMn0y9DZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7416" target="_blank">📅 20:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7415">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJ6lmbmdL_bqns78_1Sx1wjgXi2Whap7RvQCE6GMwSf1LvV6w2oYI3PNJE9rM3z2Z0CMHo-szUg9paiUUmtMy90_fpQ957nX3kFNL0v_8dw1C3ZEJWv3AWCizgbPrYgkmY-CimaWUw-bFPH1GZkoS0XHkiNv1XTZXpHEux9jl2Mh7FG81pRJ3pwzsi3tNgmHG41EpYA1euF514O4I-auHL-T4KRoj0P6N7onQyv3Y_iN88f20KmpntOZofAvWz08jmxLYqtzS3cgjyqastFDktaV2X0E0sqbO_TA55knq-kj8Frgs7vp7M9USddk_eWtndIKNXim9tl2E5CSIMF00g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7415" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7414">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIDgS4NjzOVihUy1Wle5cgaLtF_396YJDs5qM2YseZLEqilB2mBAaOx-7M5kCWs96-oPU_8lgtST1PDZlizZO0Fo8ZceQYU9kGPRmMaJbFGidA_StdLEsm-HfJ47yc4XufpyJArldcDgmIcguedl5wkbPfA8ilQDjIrRQb355S5sr7H81wRDxUzAgXC9-q7h-O-oTZyBfisIAbBCt6k2obwWJR7pha70v45NXEk4hYMlfhHyyZWcdc6pebP1pB-UVm0BhEUelcjK5IWizXz8Xf1Gbf1Vbhx-d3gV_JywofhhVWoxcwxCb6cPOo_labm5DnsNLafOBcZAJYBjHuuC7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7414" target="_blank">📅 17:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7413">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTfJtIzPvEiUwjXNdhtPgIJWj-pf410LDRD5P0dWj2u_0rwRqabI6CHXVLMAspTb33pZgT6e91rDCHJ7KoBi4wkbaCWVk3wrH6P6ChIObC8VjOhONToKOmkoPjLFdIbXNnO6nMsgtr7KEW852RSZOqb6UNbQIhdpV8mpd2p-kYuQhDcbltjM1X4p31gavFLiPgpYFAhaiSxogVY1Cxexx3gIsN8eUXYDr38ypUwHLhf7vycq2aqBIOGsQ4W1y2QMiVa1JS5tnArQNrJN_iIb2i-IhrzD8G00G8wKYAUrx2jO0IvkBsI61QzMlyRJF6R6wW2jiFalQnkCuFQ_T0UpeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7413" target="_blank">📅 16:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7412">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7412" target="_blank">📅 14:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7411">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXlLZUgVHDzo3STWQu2pkTRiZ00j-GvrKBDPnUZEA-7yTtpACW73q5UniaJCDNVL5tc7WZ2g57HBFz7zPhne6Co1AmaEqQIuDKkH4VEFOAPOkGxuhvt5opgEzArbR02Dol9_5tju2UuuzoINlHWbGjYAptcNw__zIRRpTJ8aGpkAXX8TXJM5wFmxtshCj_YFOkA72fKYSB1kiGKL6lblLsUgr5pnjsKg56Ho02A2EbXGZUSOwchcijrOa_wRDCPG_EeQaI0K3dPWWku9_YtFnQ09ILZjesw62rKN2xXS1zKjdpg3nBY0fmK5VvGaOYZmecBYy7sY-EFn2EDVF8SP8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7411" target="_blank">📅 12:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7410">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7410" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7408">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ی پست ناب بریم
🔥
🔥</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7408" target="_blank">📅 11:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7407">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETEJDQ5Xr2lWuHk_Wnyy4vYu3jbPgGMG4HJ0vaJV2nFmjPOcksznMB0Vg67ifROI8h61lvt4xEl8RKbWWPSnMnnI3qcJHci3ABQH0OEej08aFgma9mNZNyakN0upaPJ33v0JU_7BAKM2TX_LqK-tapzPD7cXFdiDohXQG9st5ZRSi3nTYHDV-of1jytb3lslgyNrLiFcAFfNOTFdIezIUsUsJsTkBL6BEz9XwbeILDKzHb_xnv7opWXk2rYfQtY8bUtEzOoC-BpSW-L-Z037lxL0oUEox4KdFvKsJ96blkfj9DuA8XtRQz-hAhil0Uyvxxpq-XfhYaz2vROz4rjw-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#fun
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7407" target="_blank">📅 11:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7406">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7406" target="_blank">📅 02:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7405">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=KcsnM9QgynqXV-ML8gN25xd6Bwf7r2dSrJzguu-DaNCmvGaEYhJKu4VDne1SiA6oDoGGxIOQUwWaJMrZRpU3aKOSPLhdCCJ5smbRAk5tEB95loPX1Kw2mcYCicul2wEUbVMQetLBZFHbNIQ807XsQbvSKqayEnbMceTIeb6qHXU16P3b0vXp57LUvBYk_uhZSjaN9JPgVMb90p4et9ljwScGd2cBTTWedN8evua_89xJApok6NODD7P_ZWkOT7ZbGANfQFdxmnOfZDz_KOgA6SoMuDb-OvrMZ6e_vh7oDOm5XmE449BqCiJdo0Ptth1NWfJymaNSrim1bsja2gHhQ5_6JJbN9qB8MZeEpiONkH62cpHiFzjzv3CXLTbZVi2TNJIagGCWQxDXAhmWcLc0kxNBx6RHr0Ixh4QTo7mn4kl1ytAhq4Rz85aulMhsaEq882LbjLQG5w5fncshh_vLeWEf_KK2I_9e_CHXr4z-W4ZXlTZEukXnihksZPKNVXGKFTCtDLoSbEavAP0_w2BVua0JFNBBHD6Bk388DfY1SjKXrM0PgQ-ua068EAhhJkMo5Br7VufcYTcfhmSrDpOHC5IdX1BUagT5dpu9BxH1y5VrPBt763ajz7YOBsAT0ZIZ3qpIc07kb0-xt0wcbCjJXOQCneyLN_GMfphOZ5bBVwk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=KcsnM9QgynqXV-ML8gN25xd6Bwf7r2dSrJzguu-DaNCmvGaEYhJKu4VDne1SiA6oDoGGxIOQUwWaJMrZRpU3aKOSPLhdCCJ5smbRAk5tEB95loPX1Kw2mcYCicul2wEUbVMQetLBZFHbNIQ807XsQbvSKqayEnbMceTIeb6qHXU16P3b0vXp57LUvBYk_uhZSjaN9JPgVMb90p4et9ljwScGd2cBTTWedN8evua_89xJApok6NODD7P_ZWkOT7ZbGANfQFdxmnOfZDz_KOgA6SoMuDb-OvrMZ6e_vh7oDOm5XmE449BqCiJdo0Ptth1NWfJymaNSrim1bsja2gHhQ5_6JJbN9qB8MZeEpiONkH62cpHiFzjzv3CXLTbZVi2TNJIagGCWQxDXAhmWcLc0kxNBx6RHr0Ixh4QTo7mn4kl1ytAhq4Rz85aulMhsaEq882LbjLQG5w5fncshh_vLeWEf_KK2I_9e_CHXr4z-W4ZXlTZEukXnihksZPKNVXGKFTCtDLoSbEavAP0_w2BVua0JFNBBHD6Bk388DfY1SjKXrM0PgQ-ua068EAhhJkMo5Br7VufcYTcfhmSrDpOHC5IdX1BUagT5dpu9BxH1y5VrPBt763ajz7YOBsAT0ZIZ3qpIc07kb0-xt0wcbCjJXOQCneyLN_GMfphOZ5bBVwk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/ArchiveTell/7405" target="_blank">📅 02:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7404">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peFt-jVzzHKBnQZ0jMGgZFfa4mv-B6AxMrSVt8s_biS6TE9cw7qCShlMHtWeOtzGu1prn0yWSrSqrd0mvI-x2TJTXk2eEqRe-ftLa634VMYDSE6m5GFBo23ZZYiaG2-booji3WMoh2318vo8fu2jggVRhIbsGSR_2jblmgGPn8t40NYy_BwgHCg0-LCiuk7b7YeY2ZdkMWYrPbKc4MiiAfBDM_aDPpTd8q8DwrPbR-hz3JyGDiLiFbuzwItfwB2mqAzCBpJXTkkgK89laRMZbEYjf9Gj7tdbY5MghUsAyWoabnAEJwr7hYh4l7BsDkkwMayxjZvYu-JetqGfkADOdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7404" target="_blank">📅 01:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7401">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">📥
پترنی ها آپدیت جدید داده
۲ ساعت پیش
چنج‌لاگشو ننوشته
https://github.com/patterniha/v2rayNG/releases/tag/2.3.2-P10
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/ArchiveTell/7401" target="_blank">📅 01:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7399">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfHF2tpt61-t8wBTJOO-6SyR8oIgTvRnSDaze6H-SdYtJK_KhVQIicTsdyvD6QdyFcTqFnwUfthy5FIHtHS7mi-Mh0iZ-QvGMKv2twCMDu5oGkECsi1WDwEKp40YX37SoRSdQe8ofbgUYZx7ZpF1Cgpng6E9zoLLUY4YrovYw3WBnJ-V5sWuwpb6hLYGio40ItWbf0i0QertGLi-igy7v4As5dR-eJJD5XXMQ2CwaYZJ7IWGy-VJMRG482ioCqtO8q2Vd7BYccOOmUgePQ2xsuEcs6VNSW7LpAiCqwSuiPFWDYoDM9wCDLEi6OyQcH42P-TB9FTyU_EQ5-IY4ikfMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولت کلادفلر خودتون رو رزرو کنید
‼️
تنها کار باید برید یوزنیم بدید و به اکانتتون وصلش کنید
⏺
کلادفلر یه سرویس پرداخت و کیف پول برای ایجنت‌های AI معرفی کرده که بتونن خودشون API و محتوا بخرن. با سقف هزینه و محدودیت‌هایی که شما تعیین می‌کنید.
cloudflare.pay
❤
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7399" target="_blank">📅 00:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7398">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7398" target="_blank">📅 20:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7397">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqODLU-ZnKay-k93lxZObUL6RzI5Dd_ztH_xBs3RqTOcYC3N-GOsH7ICZiVVtr13FbSP5yPVvGV0313VI8_z4-r96FN6WyiFycoJ7HZDm6X-DQQ_ksoLgOFeYKtnHh4mjuNV9CCfpfsaS17k_ys3mQCcWLcWUElxpZ0b99g_yOnIBIgoUHZrzCQDTQhAtLRNlXI3ZUrOV_-sEOIiiU6wahbvy42qJ35QxfmeP7CGuVAwpXFfUtCaK7MtlNU_g3lYUFfViNwqW8QAdXawX9GICJlfiNOesqcWMMORlQLYPzzBypwIAPK34LSvJ4ekntPw23n4_Rv3EkmcYtrKaglXIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7397" target="_blank">📅 18:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7394">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url: https://www.fastaitoken.com/v1  Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471  Model: claude-opus-5 Model: claude-fable-5  دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
…</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7394" target="_blank">📅 16:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7393">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7393" target="_blank">📅 16:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7392">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7392" target="_blank">📅 16:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7391">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLLQxBgIn5xmOrCLT-IyTUw5Xh4-066kABOjp2r0eJlaGCrYaMUYcXvvoudnOFDZkIXLGtLjOGctmxWlmccBcC4c1fSqG_rPRj0B1iFVKF9FXcq-uB8mBnQXmidxBnDtIoE7phZZ22zODkHKyi4aHraIczFOH3CZ-WF39ms-VWzCn5_cdyBLK_KPxQRVeBOZrgZOdISdrJBpFwvWHHRcR4u8krxYg7RphBG8uVjUaDSuZJsr8kAS4jaWyTn8Ue8yA2k6I8kYjRy5IJPdCp8f1ZuO3Rtvx6xh33wG_yw991assCabPkrxV2hA_mXLMQ7ktfWHrMRYgu1g9B2VrstPGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7391" target="_blank">📅 14:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7389">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0s7DNPJYXeuC6wQX6SxlbIMk0Avm9ve_C2wMnXojf9aX6cOKUqJaZnyah7wBogTSbBtaZYgCZrpz627PJ6_A0GVByPNeJW5X0KjNzmUSxLlaXt1Z4c1AXyRwtDwwI9TT0eRac_5Iaxf8qQxcqOoWFj7-rHMOhVwQHZEygWLIwsOVYayK2tkEojXGb9LuvAAwTJOd0VvydXL-kexHMFNsxcvAWajdJqoRQalisgM8FpzvnQczpkLD6mIRzTtWWA3pUOPqKFpY6RGZPIt9lFN_MeIjj4yAxB9j2lGmXVlnfnbZHve4HSUYNc31Girv3yjXo4eT5hDehsEDGerg7Fqxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دسترسی رایگان به Canva Business
🔥
از طریق
لینک دعوت
به تیم، وارد شوید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7389" target="_blank">📅 12:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7388">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آیپی تمیز کلودفلر
92.53.191.134
66.225.252.96
104.18.14.224
104.25.247.228
104.17.2.54
176.124.223.242
104.16.122.178
188.244.122.16
104.20.14.15
185.148.104.192
104.24.152.74
104.18.2.152
104.27.24.70
154.211.8.196
104.17.88.93
74.49.214.92
195.85.23.208
172.67.114.81
92.53.188.13
104.18.198.203
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7388" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7387">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1oGH_WTnI7p1YJdsG8r6qqWrGB1DqjUfIrIUQeRCNxvYzNtQ0dnrKsdCyizR9OwrUgqGJYhVkJiInRdoO9xjw40ft_z3YrO2QMrTwlpQbePciAq8H2UaZPgQ-U7IDF5qAi1VxMV2K1UU7pV3xvmayTz6p98OyxlqvW0uigyAxCO1p2v3sAIHpPTFi7Qxdp8wSbP1J4kwL0LpoRtuDv2tf8k0_zpzgGonnhQNe1MZUe3LLqdV-gg13TcU3K0TQi4DfB1qgp4vi9GQz1CU1-LR9EiWdFZRaJipYx1shMaNgn6DdaYOiC4POV2z0jZgqxhbUkEqRVN6al1zznyZFEBAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
تولید محتوای بصری بدون محدودیت!
‏دیگر نگران محدودیت‌های اعتباری یا کارت‌های بانکی نباشید. با این ابزار قدرتمند، می‌توانید بی‌نهایت عکس باکیفیت و ویدیوهای ۵ ثانیه‌ای جذاب خلق کنید.
🎨
‏
🔺
تولید نامحدود ویدیوهای ۵ ثانیه‌ای
‏
🔺
خروجی عکس با کیفیت بالا
‏
🔺
بدون نیاز به کارت بانکی و پرداخت
‏
🔺
رابط کاربری ساده و بدون محدودیت‌
🔗
https://zsky.ai/create
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7387" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7386">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بسیار عالی
ظاهرا سرورم دیگه پینگ نمیده
بوی خوبی نمیاد</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7386" target="_blank">📅 19:50 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
