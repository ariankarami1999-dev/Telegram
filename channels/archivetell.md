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
<img src="https://cdn4.telesco.pe/file/ArrzSfd7415rdhQu8gkBw_ivSjd-rWi8dOLAgY03HCyvryPTn0ksuMtHEsg8Ui5EKl1nWXB0Se8HJt4y_E_97uCe59m2f64jZJ_9Jf00x1sYFseFvGP4vDw2MuBCgn07dUmWG-14YWpJaOAG-zjE9_1GEkQh-_m6DMJcmnVvUk5OeeYLbV8k9HXptp9aP3vF-NpPlEOuJseRquI8iBgtLq66Jf5G-dZYGYsnuxMJG0ahSStXRyOgEFpBGwANF-vyrSOHr76ez7PCn1Fv0YJihF9FPNmykNyrEwOcJXcNW6fJpV9mKiRjfFbGzKMy9BWoV1-6JUAXM08cPGktZrtSaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.82K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 11:13:54</div>
<hr>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JapSbfCnpFeXTnz58PQ3EFxQ2f3RpZq52DoMp_osJ3tF3vl84jaZpJtWktRvl5nBT0owQTbE7UgpwOkBm1ccXlMRkMJJwdQAMNx9QZ7kZU8tGv95rIbyL0yvEZcsczK1HGvX_NjB7mUwAKTfn22R0d8uomQSQHm0Vxfn4hlA21hy2bAdKkniF3d1LqhZdaI5a21Lb4AFOwCH3Cmn1KqHgExaSfIRJUQq6XsUsgfpzRart9UWEPk3ZyqHKytNrNN87S3QzsaiyxT_xLZYCVMNZ7myhlqPFUP0T2MXW0E8g2alEJ7RWONVoi9GpR6shW_Dv50BL1rYJFm1OxHGW3HobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
معرفی Google Flow
این سایت جدیدی نیست ولی خب بعضی دوستان دیدم نمیشناسنش گفتم معرفیش کنم
😁
اگه دنبال یه ابزار رایگان و قدرتمند برای ساخت تصویر با هوش مصنوعی هستی،
Google Flow
یکی از بهترین گزینه‌هاست.
ویژگی‌ها:
✨
تولید تصاویر با مدل‌های
NanoBanana 2
و
NanoBanana Pro
🖼️
ویرایش تصاویر (چه ساخته‌شده و چه آپلودی) با پرامپت
🪙
ساخت تصویر با
۰ سکه
(رایگان)
📚
امکان ساخت همزمان چند تصویر و ادامه ویرایش روی بهترین نتیجه
🎥
قابلیت تولید ویدیو (با محدودیت بیشتر)
📌
لینک:
https://labs.google/fx/tools/flow
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 181 · <a href="https://t.me/ArchiveTell/6774" target="_blank">📅 11:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6773">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7jqo6V8yBNVqL30IDF2dA-1i5NkF7OzbXuqtsa7_qoZWxbTLsq-gnEkv3yBWwrcaMlryr5qHiAiSYYxwE-Xl5gMOqJC-Vb_najiZp90Yqhp8sw8hLO1SXGmHlWk71IDc1Dw-CSMG-Uzlj1paPDz4Z3RVxe0X1vpXWtZWmD9Cj83_Zn8ckOpM-dkpFnPg1ZUuZr6MdgNqVsgk0nydq34l6tSIH3HjlT6noHr1y-yM2VJpuTp4jRGYWRi6_NlarDYvUkZM6E0mikuswdJip-PGwUUkIh75YHbXrjyw-jOcVGSsMSm_zY_PEWO06BM-wfRFPMkVq-DAbR4sf2cRcnkfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
WLLPR | ژنراتور والپیپرهای مینیمال
اگه از والپیپرهای تکراری خسته شدی، با
WLLPR
می‌تونی توی چند ثانیه والپیپرهای مینیمال و جذاب بسازی؛ اونم دقیقاً با رنگ و استایلی که دوست داری.
🎨
⚡
ویژگی‌ها:
• ساخت والپیپر برای
📱
موبایل و
🖥
دسکتاپ (4K)
• انتخاب رنگ، طرح و استایل دلخواه
• تولید نامحدود والپیپر با یک کلیک
• هماهنگ شدن رنگ رابط کاربری گوشی با والپیپر در بسیاری از گوشی‌های اندرویدی
🌐
لینک سایت:
https://bypedroneres.github.io/ai/
➖
➖
➖
➖
➖
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 306 · <a href="https://t.me/ArchiveTell/6773" target="_blank">📅 10:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6772">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXyGHbLml5DzjjmT4sQFQmfX1W71Nd8bzrhGwPZd3dbAehSfNazUd3P5YWwqNDUf8b295E6IQC58iAq4dfXydPGd4TBOTGOCN3QpMNyXViqndePlvuBdbrZuElo7P5EZ_5DBdtwbmz5fOgmoCsny63Lhx9LkUyjTD9uRsgzB8feBKrfiCOQ6ZasT6UeC1YPmqUijhRVcZ9_GsK2VNZIuXL6btGSt-DV5rPTCO3ps0ahe7jnefKBFFm1kE049ypIYEbfaBLwqs511Glb7fMjgSM12YhR9fyAmo6EAlwoi_1_eIt_T1WLfybOVrszvThsh0gQtJk9kJDnFvQhHh_4tRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت OpenAI
نسخه‌ی GPT-5.6 را برای Sol، Terra و Luna از فردا راه‌اندازی می‌کند!
🚀
دسترسی زودهنگام از همین حالا برای کاربران در سراسر جهان فراهم شده، می‌توانید با خیال راحت وارد شوید و آن را بررسی کنید.
🌍
🔍
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 380 · <a href="https://t.me/ArchiveTell/6772" target="_blank">📅 10:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gy5nwCj6cALialeXngS0wO_VVbwdJgF1-xM0laUUaQto-A38emKG2qD8vehFHT_-nlZKHvnxOCJSWV-ZWCrMMhsFsM7UB2BK_Dij4qAOZJhtuFxODENNNMTJ1TwLB_QkTZEf4W1g_L5ZEtPoZN-z0lkS7-KXbZXRdYUT0lNRQaK9gDoUOvqJOe6a73XbJiGMNlkjNbnl47GVWNr7ZUx-kShx9lDuvb79KtV0K1MmmiFdKo5s_wlwPFY_EvsUP7c_uz9W2PO2sKi7_1hUxCbYeKMls99n_OjkQ2Ty9s9gQEUGCZlQSBTXW7MbxwhPZiIp36LATnQRz1s8lwueeWBKjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛Constrict ناجی شما در فشرده‌سازی ویدیو!
📹
- ویدیو را آپلود کنید و اندازه مورد نظر را انتخاب کنید.
- بدون نیاز به سرویس‌های آنلاین و دستکاری‌های پیچیده در کدگذاری.
ساده، سریع و کاربردی!
https://github.com/Wartybix/Constrict
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/ArchiveTell/6771" target="_blank">📅 08:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shWxaqEPTXQmvcWpI2lmoVGs3gJHvi8LR4xqppWQxnH89L6lyFzv2SEztVBHvJUYBDXZi8RNoCQUzvKZnEq1qiq8IvIVAIAOYzjP3NbGtwWqtdE_CU8IMu7x884-BnAVc9JwGqY3LDb6xOlvgyEOS918uSQQRUvFPdxaSKHtUfah9Zu6DtvV2b5UaAqfiWHiNX8uhbt1W2h9lrzXTfTQ4Rz9oCEMiM50SDCzSVOc6CWHqvtr2rqPBaELa4p2LNXp4UYfCyU3c7Trrl9qNg6Mle43A811oIAaam4UoXqTDabrLq3vX7hdtClvPIsWmYmhpbtOGZp4d9ouNmmAhosLLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تحلیل ویدیوهای یوتیوب، تیک‌تاک و فایل‌های محلی با هوش مصنوعی
؛
Claude Video
یک ابزار متن‌باز است که امکان تحلیل ویدیوها را برای دستیارهای هوش مصنوعی فراهم می‌کند. کافی است لینک یک ویدیو یا فایل محلی را به آن بدهید تا فریم‌های تصویر و متن گفتار را استخراج کرده و در اختیار مدل قرار دهد؛ سپس می‌توانید درباره محتوای ویدیو سؤال بپرسید یا خلاصه آن را دریافت کنید.
⚡️
ویژگی‌های کلیدی:
-
🎬
پشتیبانی از ویدیوهای
YouTube، TikTok، X، Instagram، Loom
و صدها وب‌سایت دیگر
-
📂
تحلیل فایل‌های محلی مانند
MP4، MOV، MKV
و
WebM
-
🖼
استخراج خودکار فریم‌های مهم و متن گفتار (Transcript)
-
🧠
امکان پرسش درباره بخش‌های خاص ویدیو، خلاصه‌سازی و تحلیل محتوای تصویری
-
🤖
سازگار با
Claude Code، Claude Web، Codex
و ابزارهای مشابه
-
🔓
متن‌باز با
لایسنس MIT
🔗
گیت‌هاب پروژه:
https://github.com/bradautomates/claude-video
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 676 · <a href="https://t.me/ArchiveTell/6770" target="_blank">📅 08:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">#Android
#Gaming
🎮
MuMuPlayer 6.0 منتشر شد
نسخه جدید شبیه‌ساز اندروید MuMuPlayer با تمرکز بر عملکرد بهتر و سازگاری بیشتر برای اجرای بازی‌های اندرویدی عرضه شد.
ویژگی‌های جدید:
•
🤖
پشتیبانی هم‌زمان از Android 12 و Android 15
•
🚀
عملکرد روان‌تر و FPS بالاتر
•
🖥
بهبود اجرای چندین Instance
•
🎯
سازگاری بیشتر با بازی‌های جدید
•
⚡
ارتقا بدون از دست رفتن تنظیمات و Macroها
مناسب برای اجرای بازی‌هایی مانند Roblox، استفاده از چند حساب کاربری و تست برنامه‌ها روی نسخه‌های مختلف اندروید.
🔗
https://www.mumuplayer.com
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 833 · <a href="https://t.me/ArchiveTell/6769" target="_blank">📅 05:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMxYP-6al6rVREWfK6z2Rjeyjfp521UnT7avSRIfOH_rJu84BQ7pyaKddW9-qJ4MRFrsVZF232mIcCbwdlRzYvF9fuKGrCijZbD2M5gAPQaaEVflJ8xzw9j9uk1kjaX8K2rLFXGeCf4eb7BK6aak5LPNgsYXixb1sQExHaouwBMg1OR55N35jmeQ1Pi43a0qrCL1oFOpVojevWdrgE1SrS1-8MRoIGMRJk5zwV6vm4bQJAcWr2Zf-VBORDGGNsQJOxlOgGyJCb6E9FUzB-b12kL-0TOAmY7S6fkUhxVsG08PbirQqcfQO3SVyoRA370W_47jbXgai_ePKlDYlcCWAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
یادگیری شخصی با هوش مصنوعی
موضوع رو بهش بده؛ بر اساس سطح و درک شما آموزش می‌سازه.
✅
آموزش مرحله‌به‌مرحله
✅
امکان پرسیدن سؤال حین آموزش
✅
مناسب هر سطحی
🔗
https://peras.app/
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/ArchiveTell/6768" target="_blank">📅 01:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏
🎁
100 هزار توکن رایگان ( 3 روزه )
‏دسترسی به مدل‌های زیر و صدها مدل دیگر برای کدنویسی :
🔹
‌GLM-5.2⁩
🔹
‌Qwythos⁩
🔹
‌Deepseek 4 pro⁩
🔹
‌Kimi k2.7⁩
🔹
‌Minimax M3⁩
🔹
‌Mimo 2.5⁩
‏
💡
ویژگی خاص:
امکان استفاده از مدل‌های ترکیبی ساخته‌شده توسط کاربران (مثل ترکیب ‌Qwen + Fable)⁩
🔗
‌featherless.ai
⁩
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/ArchiveTell/6767" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aj3FN8Z3pdXRGzkb1sHNgZyX644US2PHR7_TNv3LzAxCzxOHRnRA--6C5k95L4Uy5AfCiC-UwLFeaIFIMm9s6zno38ce4jXfPCGosIQpqqAlwFzvc2hmXx6pAhKdYagLYqgkjpst7_BtN0rBSomR2i84jFPVesxBP9A9whiCRanIYVC7HXjnO4kltwuDx5CoR3nrTDaq51dNkqEz_t5rdRfrTKVLR7OzY5Vrx4AH7d_LYPGQDBrPrWPUdKjGgPUYeeP-8NnVjIy-wZP1iRYn6clq6O7pVrheStL17SjBeKJ-8v1XQZUv6_YdC1ovor0cV6qxAvXglNN5UP50zLdSGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
PixelRAG
یک پروژه متن‌باز برای Visual RAG که به‌جای متن، اسناد، صفحات وب و PDFها را به اسکرین‌شات تبدیل می‌کند و جستجو را بر اساس محتوای بصری انجام می‌دهد؛ بنابراین جدول‌ها، نمودارها و چیدمان صفحه حفظ می‌شوند.
ویژگی‌ها:
•
🖼
جستجوی مبتنی بر تصویر صفحات
•
📄
پشتیبانی از وب، PDF و تصاویر
•
🤖
سازگار با مدل‌های چندوجهی (Vision)
•
⚡
ابزار CLI برای ساخت و جستجوی ایندکس
•
🌍
API و نسخه دمو آماده استفاده
🔗
https://github.com/StarTrail-org/PixelRAG
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/ArchiveTell/6765" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔐
VoidAuth
یک سرویس متن‌باز برای
SSO
و مدیریت کاربران در محیط‌های Self-Hosted.
ویژگی‌ها:
•
🌐
OIDC Provider
•
📖
LDAP Server
•
👥
مدیریت کاربران و گروه‌ها
•
🔑
MFA
و
Passkeys
•
📨
دعوت و ثبت‌نام کاربران
•
🎨
شخصی‌سازی رابط کاربری
•
🔒
رمزنگاری داده‌ها (
PostgreSQL
/
SQLite
)
⚠️
هنوز Audit امنیتی نشده؛ برای Production با بررسی کافی استفاده کنید.
🔗
https://github.com/voidauth/voidauth
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/ArchiveTell/6764" target="_blank">📅 00:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🖼
جستجوی معکوس تصویر با TinEye
اگر می‌خواهید منبع اصلی یک تصویر را پیدا کنید، نسخه‌های باکیفیت‌تر آن را ببینید یا وب‌سایت‌هایی که از آن استفاده کرده‌اند را پیدا کنید،
TinEye
یکی از بهترین موتورهای جستجوی معکوس تصویر است.
⚡️
قابلیت‌ها:
-
🔍
جستجو با آپلود تصویر یا وارد کردن لینک آن
-
🌐
پیدا کردن صفحات وبی که تصویر در آن‌ها منتشر شده است
-
🖼
شناسایی نسخه‌های ویرایش‌شده، برش‌خورده یا تغییر اندازه‌یافته
-
📈
مرتب‌سازی نتایج بر اساس اولین انتشار، جدیدترین، بزرگ‌ترین یا بیشترین تغییر
-
🔒
حفظ حریم خصوصی؛ تصاویر آپلودشده ذخیره یا ایندکس نمی‌شوند. TTinEye+1
🔗
وب‌سایت:
https://tineye.com
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/6763" target="_blank">📅 22:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6762">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyTZXafQnpP8oH8aiE75ZNrEItxJFHgIFnuLTkvYdfVxdtG3flVei-LMgtMPTXrpdxER9hns6eUYZ1WUFsJmd0ruMnBf5maoGbPrRgXcoK3X-C22tjWp03DoaFA_6K6GaCRf0BXx_q1PQuo4pZCTDKqDhQ-aS0VBmImG6kkQH8pDpKH_aF42gpfgoyG3uDzebyR7Lp4buDmPuNx9p6iGUaz-g_Va8uXeSJZSVY3aUgsCm3T6-FgrLQsMSCNcV63Se1NtQiZcgvf6tqAWy3hHUdlG6lgFfI3KduFF7w-WuRGwtt7wYkA8HqwPwPZh3X1thCk5lIubrisXuSq8vIlzvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
تولید صدا با Pocket TTS روی پردازنده معمولی (CPU)
این ابزار یک مدل
تبدیل متن به گفتار (TTS)
بسیار سبک با
۱۰۰ میلیون پارامتر
است که بدون نیاز به
GPU
، پرداخت هزینه
API
یا وابستگی به سرویس‌های ابری اجرا می‌شود.
⚡️
ویژگی‌های کلیدی:
-
🚀
تولید اولین بخش صدا در حدود
۲۰۰ میلی‌ثانیه
و تا
۶ برابر سریع‌تر از زمان واقعی
روی پردازنده‌های مک.
-
🎙
امکان
شبیه‌سازی صدا (Voice Cloning)
تنها با یک نمونه صدای
۵ ثانیه‌ای
.
-
🌍
پشتیبانی پیش‌فرض از
۶ زبان
: انگلیسی، فرانسوی، آلمانی، پرتغالی، ایتالیایی و اسپانیایی.
-
🔓
کاملاً
متن‌باز (Open Source)
با
لایسنس MIT
و آموزش‌دیده فقط با داده‌های عمومی.
🔗
لینک گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6762" target="_blank">📅 19:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ss3gNhUr-r4DJhfVq9jYefdLGTarSanMlteC_ZYu9OhzLVFJaOtX959n0gRApvy2b-FJU9k2XYBpPbrNHtpKF5jOqpwmys5o9_jXC0lXyu_vHVLfXRtVLC8ZzO5RMD3d2fL46N9TIxOHAWAqQH6HP2a_2lYhKtWOTs9Y-b_FvLc2HG2CJNn05MY4-AQP6nW1OvuYPxfwcWQ6yDpQHKa-kZWY8DJH1-dxCzxP6NPqfNyFxsmQQs5zO_EnEXunf-VKQQKH0g2LWv9ulepEAgzWm0z1JUCHBA88K6uoEavCuvbig_obdUaFGd--ghr12SkMTeh2_gAcfIO0Hrwzk7UGgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه به دنیای تکنولوژی، لینوکس، شبکه، سرور و ابزارای خفن علاقه‌مندین، یه سر به کانال لوکال هاست بزنین
توی localhost کلی آموزش، نکته کاربردی و تجربه واقعی از کار با سیستم‌ها هست. خلاصه هر چی از دل پروژه‌ها درمیاد، باهاتون به اشتراک می‌ذاره!
🅰
t.me/localhost_ir</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6761" target="_blank">📅 19:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHajyar6B0DGMUn4vpQJz1bOShG5LgtOAEe_GqUD4LI1U6AX5p-Y08at3u8xMl3u-I9jt6hmGErChGcqiIvwvUYgt7HVkQbfBuvz1GVw807dHY5Zdcva7QE5WzKcmgvEvRtjVzBThGyN1L1E7scOej5SxB6oYSFxLBjEvNbYCcWJ6Lc67OIhGZepmwrcxhG3jL4nhPwwd7QFsLctDtF5Qc4DMt5SNId7bLg1SnQk6x7utu2CdKiTJHHJuubVdbUbvlmNmSxJ1Ieckp5h4Xz1wMAn7RJQ9FwBtDxOdGxicy8pxm0PvYu48i-TLfaGoeiMrIqj29W6AT3MhLYVTN_1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلود و مدیریت فایل‌های تلگرام با TDL
یک ابزار متن‌باز و قدرتمند برای دانلود و مدیریت محتوای تلگرام است که امکاناتی فراتر از یک دانلودر ساده ارائه می‌دهد. این برنامه با مصرف کم منابع، سرعت بالا و قابلیت اجرای مستقل، گزینه‌ای مناسب برای کاربران حرفه‌ای تلگرام محسوب می‌شود.
⚡️
ویژگی‌های کلیدی:
📦
اجرای برنامه به‌صورت تک‌فایل (بدون نیاز به نصب)
-
🚀
مصرف بسیار کم منابع سیستم و استفاده حداکثری از پهنای باند
-
⚡️
سرعت دانلود بالاتر از کلاینت رسمی تلگرام
-
🔒
دانلود فایل‌ها از چت‌های محافظت‌شده (Protected Chats)
-
🔄
فوروارد پیام‌ها با مسیریابی هوشمند و جایگزینی خودکار در صورت خطا
-
⬆️
امکان آپلود فایل به تلگرام
-
📄
خروجی گرفتن از پیام‌ها، اعضا و مشترکین در قالب JSON
-
🌐
متن‌باز با لایسنس AGPL-3.0
🔗
گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6760" target="_blank">📅 17:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYlor5-P21g0Hv0NmQGcy3onP5vt7MMyG1HxNZjtKeX4uXx-c_Fkk2ozazD0VCR69_X_H_XauFRphbPeDcR9ADxcaDS74MwU2o2WpxPN_4rd-leUiZqFuiIsTdFGpC_H93TI9GnRiLdJmUfGojQyWXi5lv4Gpqi7-cFcaJ_Vv1Vo1Cion_m2GZ79lA21dO2RJwZ8ngBzqLopGqj9uYEN9JCNyxZFSOrR91Xevbz75QTmFrFvmhKYhl3o2-zjKRVjdF88Oe727kYGSAujHIc7OHVdhx2WXwm_Exvdpznf7y5rZH21ySqDpJinTM-SpTYXV67Xdt85CfDKzlVf7FYiEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهبود کیفیت عکس‌ها تا رزولوشن 4K با استفاده از ChatGPT
عکس شما را بهبود می بخشد و جزئیات را تا حد امکان حفظ میکند.
😮
پرامپت :
Restore and enhance an old damaged photo. Remove scratches, stains, and noise. Reconstruct faded or torn areas while preserving original details. Slightly sharpen the image for better clarity, but keep it realistic. Apply natural and era-appropriate colors to skin, hair, and clothing. Use a soft, balanced background color without being too striking. The final result should look like an old photo that has been realistically restored and colorized, while respecting its original appearance.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6759" target="_blank">📅 11:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKoYx4v4tN3DmEks7XpUEoznUdwVilA4ikghMiEoulxtiWotjuvfuwzi84r4toa1hU3OF571RBgPfgca_TDszYGKI2N9YPX_C7_cxaqd5jnY0508feJUO5ofldjc8JAU_J7vNphxNPSZYRBkOk4VIRwYGBUkmj-s9onuPIViDVjKuy1fQX0jA1hg3ycwb6LTkY70qKBHqGEHdm4ryz67S_mBEMuLDlTeR5BN_nBvXjf6j7z7zGYfuUhyi3hr8zdPBctMxQKHCnI7YAiek1SiSyscULU4L5m5VwHLRHcmCT1-S7_4nR3vNl8d-HvePtYzL0msqg4lKVG8vkdyV1BL4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
اپ‌استور متن‌باز و جایگزین Appteka برای اندروید
یک مارکت رایگان برای دانلود، مدیریت و به اشتراک‌گذاری برنامه‌های اندرویدی که بر پایه مشارکت کاربران (Community-driven) فعالیت می‌کند.
🔥
ویژگی‌های مهم:
*
📦
استخراج APK:
خروجی گرفتن از برنامه‌های نصب‌شده (حتی برنامه‌های سیستمی) بدون نیاز به روت (Root).
*
💾
مدیریت فایل‌ها:
قابلیت بکاپ‌گیری، بازیابی و نصب مستقیم اپلیکیشن‌ها از داخل خود استور.
*
💬
تعامل کاربری:
دارای چت گروهی، سیستم نقد و بررسی، لیست علاقه‌مندی‌ها و دریافت نوتیفیکیشن آپدیت‌ها.
*
🔒
امنیت:
اسکن خودکار برنامه‌های آپلود شده (از آنجا که محتوا توسط کاربران قرار می‌گیرد، بررسی منبع قبل از نصب پیشنهاد می‌شود).
*مناسب برای توسعه‌دهندگانی که می‌خواهند برنامه‌هایشان را راحت منتشر کنند یا کاربرانی که به دنبال یک استور بدون محدودیت و ابزاری برای استخراج APK هستند.*
🔗
[لینک دانلود یا گیت‌هاب پروژه
]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6757" target="_blank">📅 10:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675041278d.mp4?token=jdLFh0UcdRq7EwmiKEXUWZAuFVsLHszGxLO3AghRRz3MlKjVCUDFO1v9Ow2pjatOdCsRxbC89uFUi7NYgsbMwQS03X9FG37qO_t3QlvYiRbiwEORum8tBT7TS8Ge9_FILq-PNHS0CGR4a6_rZSwYZlYFDG-3nmWmkBnRiWXN_Ag-I36bIYPSLKuLBUHnen-T6bTbev2-5IVM9Cqr0_D3OOPAjATkAKnU04CZY66kU-BHJcPDPbLBrlr9aks4WUa_34Fr1WVU_ujlRuszluZq6xGl9gFoyts_NzNImNaQPB6InyJBm0ywjK9pZzuIZc0SKGDU9zhbLtG5VPF7D5xeKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675041278d.mp4?token=jdLFh0UcdRq7EwmiKEXUWZAuFVsLHszGxLO3AghRRz3MlKjVCUDFO1v9Ow2pjatOdCsRxbC89uFUi7NYgsbMwQS03X9FG37qO_t3QlvYiRbiwEORum8tBT7TS8Ge9_FILq-PNHS0CGR4a6_rZSwYZlYFDG-3nmWmkBnRiWXN_Ag-I36bIYPSLKuLBUHnen-T6bTbev2-5IVM9Cqr0_D3OOPAjATkAKnU04CZY66kU-BHJcPDPbLBrlr9aks4WUa_34Fr1WVU_ujlRuszluZq6xGl9gFoyts_NzNImNaQPB6InyJBm0ywjK9pZzuIZc0SKGDU9zhbLtG5VPF7D5xeKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6756" target="_blank">📅 10:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">📱
تست خودکار رابط کاربری و اپلیکیشن‌ها با Maestro
یک فریم‌ورک متن‌باز فوق‌العاده برای تست End-to-End (E2E) در اندروید، iOS و وب. با این ابزار نیازی به کدهای پیچیده تست (مثل Appium یا Selenium) ندارید و سناریوها رو خیلی راحت با فرمت ساده و خوانای YAML می‌نویسید.
🔥
ویژگی‌های مهم:
*
📱
کراس‌پلتفرم:
پشتیبانی از برنامه‌های Native، فلاتر و React Native.
*
⚡️
اجرای هوشمند:
بدون نیاز به کامپایل فایل‌ها، همراه با سیستم کنترل تاخیر (Smart Waiting) برای جلوگیری از خطای لود نشدن المان‌ها.
*
🖥
ابزار بصری:
دارای یک محیط رایگان (Maestro Studio) برای ساخت و رکورد تست‌ها به صورت ویژوال و بدون نیاز به ترمینال.
🔗
لینک مخزن گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/6755" target="_blank">📅 10:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚀
۳۰ سایت رایگان ساخت ویدیو با هوش مصنوعی
#اختصاصی
اگر دنبال
Veo 3، Sora 2، Kling
و سایر مدل‌های ساخت ویدیو هستید، این لیست را از دست ندهید.
⭐️
بهترین‌ها
VeoAIFree
→
https://veoaifree.com
(بدون ثبت‌نام و واترمارک)
Vixdo
→
https://vixdo.art
(۱۷۰ اعتبار رایگان + بدون ثبت‌نام)
Pollo AI
→
https://pollo.ai/m/google-veo-3
(چندین مدل در یک پلتفرم)
GlobalGPT
→
https://www.glbgpt.com
(Veo، Sora، Kling و Wan)
Leonardo AI
→
https://leonardo.ai
(اعتبار رایگان هفتگی)
🎁
بدون ثبت‌نام
VeoAIFree • TryVeo3 • AIVideoGenerator • Veo3Free • Videomaker
💰
اعتبار رایگان روزانه
VeoE • EaseMate •
Veo3.us
• AIEase • Aitubo • Pixnova • SeaArt
🧩
پلتفرم‌های چندمدلی
Veo3AI • Pollo AI • GlobalGPT •
Media.io
• Novi AI
🎬
ابزارهای تخصصی
Digen
→ Lip Sync
MindVideo
→ انتخاب نسبت تصویر
DomoAI
→ تبدیل تصویر به ویدیو
Klap
→ تبدیل ویدیوهای بلند به Shorts و Reels
Fal.ai
و
Eachlabs
→ مناسب توسعه‌دهندگان
💾
این پست را ذخیره کنید؛ احتمالاً بخشی از این سرویس‌ها در آینده پولی یا محدود خواهند شد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6754" target="_blank">📅 09:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIIgPPh66_qWurRdCOXysFOAmIB6cAA8rYNTTAzKTX-LwfuSBm94nB-GDD6WlKLwSEv6IIsyNmwtWvQoyPZ2lb43XLMWzggXGElQQu_cxJRY37vMZI0mLOgui1XFHMa5QMoPGE69d7M39372Kj_BHj8kOEX6iFzLJXdsrSZGezqvMzlagRYyUIpDGUdql_wF1sVAIFJBgD6s7iw38z5edRrjbwC7UQjeOwqOhOoeo6EZ-CkVkno9gL3qsDji4RZ7H-XB24W4YcTS1sdVs6O-HnG_xna86V49pQsmFcFwZ7omZGGAE5FJcvHBp2GMfjsiZb0w1nRYgZzjDBlemazkMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان بقول نیچه
در چنین گفت زرتشت
«من از خردِ خویش به جان آمده‌ام، چون زنبوری که انگبین [عسل] بسیار گرد آورده باشد. نیازمندِ دست‌هایی هستم که به سویم دراز شوند. می‌خواهم ارزانی دارم و بخش کنم...»
بیاین مثه نیچه باشین و این عسل و انگبین چنل رو به سوی دستان دراز بسپارید
نیاز داریم به حمایت شما
❤️‍🔥
https://t.me/ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6752" target="_blank">📅 01:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor لینک ویدیو آموزش:  https://youtu.be/pN3LxWzDtKI  خود پروژه:  https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell | Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6751" target="_blank">📅 00:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor
لینک ویدیو آموزش:
https://youtu.be/pN3LxWzDtKI
خود پروژه:
https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6750" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نیاز داری سورس کد کامل یه سایت (به همراه تمام فایل‌ها، تصاویر و CSS) رو یکجا برای استفاده آفلاین دانلود کنی؟
💾
🕸
ابزار اوپن‌سورس Website-Downloader با استفاده از قدرت wget کل سایت رو میرور (Mirror) می‌کنه و یک فایل فشرده بهت تحویل میده.
🧵
👇
#توسعه_وب
#اوپن_سورس
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6749" target="_blank">📅 22:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9RRJW9bSWP19TgtFdhT_NcVlLuUS4lUbKAtDjFsN9MS9zBiRndNzRGPdoGL8PYna1rr38W6rocr2Ul2kL0BfSTL5DipFq341jS1zGwjiiRHm_vOFcXv4VP1lqRdviC-fKpqsnmDHTSdVAuXctq7ulcrQunichwy1rBigXhOmiG-rkOH4CrPteqlyho62BLnGUxXsLkjwGJGsFTuNp_GrY9ahwvaYifCywVa3YuDU0Z0tNcLOEQNoQAopcO97H3GRKQCXHJ66oAJ7ptVSpaEBqWqTspgO6ftikCJ_YCohgL1j8knZuIDTe8t7GUiCfC0jzFReOCEyFMxt9Bg2aUynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/ArchiveTell/status/2074191361432035554</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6748" target="_blank">📅 21:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnpfSymbQlgUVVdw7aKQVHOKi2Vz3t7PrQmtjPyDa4W5NEqdUP9GAoi-c5k_wj2rFLBsQdasMrzFXVzXVl9TuxW5v6otLQHmt-SV14MT9_WhLSgw4U9_xI_KudjcLfM8GENIZ9W1Dv1_38qZ_1PsfayKnGb4reLJ4ICe-wCmyXS3J0gcG9k0cZQLmopaBh1wuuV52bEqAXiReBx8jjMEo8WO-WUbUdy9GQYR-qLMNerLN7hYQKbUMr1X-7kUaQMStIkG1eFNGWnHU0026BoqPqIAxeJQFACbGTWfqDbg_VApspDqsMqpiM5MFuhP1Yiao7YbmH9A_pSYxQnjAIikPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🗣️
هوش مصنوعی‌ها دارن با هم «زبان راز» می‌سازن!
🤫
🤖
‏تا حالا فکر کردی اگه ‌AI⁩ها یه زبانی داشته باشن که ما متوجهش نشیم، چی میشه؟
🤔
‏پروژه جدید
‌GLOSSOPETRAE⁩
دقیقاً همین کار رو انجام میده:
🔹
تولید خودکار زبان‌های مصنوعی (از آواشناسی تا دستور زبان)
‏
🔹
ارتباطات غیرقابل‌فهم برای انسان
‏
🔹
کدنویسی خالص با جاوااسکریپت (بدون وابستگی خارجی)
🚫
📦
‏این فقط یه ابزار نیست؛ یه پنجره به دنیای ارتباطات پنهان ماشین‌هاست.
🔍
🧠
‏
🔗
لینک پروژه:
github.com/elder-plinius/GLOSSOPETRAE
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6747" target="_blank">📅 21:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnQ94PighUG94Hj3jml6z4yM9F6P1qm7-gLOocgo8UtQBdhISG6rNMe_Ib76OqVoFxKFjB18jcsMXzFMpvIVmEFsznbQW4CYySUhscFO177_3Oi0JwUSAsZ45325Wx7Tf6PC6ZcC-ZMqdqsOwuaHI3hA7rr4qHEn2bq2nKCI5CMSLKGqYvrSh2v7_9eGk9whY71hn58LHtIJ8Mo8y-6zZ1JeOLVQCVhtJtQbmMwKcTtPxADQUvB2AYIAS5IHSTmjDzQ6NgNnUxLbepuSGOpn3v3s2aihhP353OkbDicuXqW_IIjhUgfkw6t-da6knCdVDD93Y8hslMsXUO1WDx1f8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🆓
دسترسی رایگان به غول‌های هوش مصنوعی!
🤖
‏‌یه گنجینه از ‌API⁩های رایگان روی ‌GitHub⁩
💎
🔹
مدل‌های قدرتمند: ‌Gemini Flash⁩، ‌Qwen3⁩، ‌DeepSeek⁩ و ‌gpt-oss⁩
‏
🔹
سرویس‌های متنوع: ‌Google AI Studio⁩، ‌OpenRouter⁩، ‌Cloudflare⁩ و ‌GitHub Models⁩
‏
🔹
یکپارچه‌سازی آسان: اتصال راحت به ‌Cursor⁩ برای کدنویسی سریع‌تر
🚀
‏فقط یادت باشه محدودیت تعداد درخواست (‌Rate Limit)⁩ رو رعایت کنی تا سرویس‌ها قطع نشن.
⚠️
⏳
🔗
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6746" target="_blank">📅 19:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSRMeMMRBUCrmQhrvpunPn1D5ndPaXqUAPNPs112qp6EBuzfF0gSNUMo6BaeuX07p3owyAI4-KrykB9tk4KISX26vJITXRCkCWU7bJIxzuzLnfi_994lzT8lGA0SIdDzvsFdKQRTq0Fu94oXlWU8DFyr30n7xJF1E27k0ayB6uFrtAz5OKAkW0gp1_I0CNMcE7b_-p7SVklQTqpJcSCIbiz9wl7jdbWzrXXc-L0tfaLvYWYz6U_KkutF5AFK_tvb7_EtoFhtoguyDOwHzy-NMVuL2XQhD17QUT2WWpsMBBBhNp9eM7WvFYOwwjCDHO0jjw8gedbMABSbpVOFkLyAng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎨
حذف پس‌زمینه با یک کلیک!
🖱️
‏این ابزار وب پس‌زمینه عکس‌ها رو با دقت بالا جدا می‌کنه و کیفیت اصلی رو حفظ می‌کنه.
✅
🔗
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6745" target="_blank">📅 18:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/910f222215.mp4?token=iJzfC38d1KC_fvOMAia7xMTGu55uBl2L-9g1eSfHzHCQA7F7QrWMS7h7EgFjck6qduJhp6woMVTu1al8Xklyd1cIYIKYUw46MayhyKje6y-jehBDNM52QM0bmnYxvK6nUfw9VYjiYyDYvUgfviMsI9djv6Kx9hfUwSMLJraRhcauwjYa5Jn4CWQcgnvOxbrv4HNfCu2A5kIWPK_7PQzqKa3CZyVOsNecfuQgcWNr0_-lmeLnwq_1vGYBXtZTGyWTFRkN2wH0Bpa31p3xRcXXb_qhzeNGuJqmtNvba7uIMg9UcZt59F8a_5ws2SpFXXc1t6ZTWwLEU-6jbetm-TpStw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/910f222215.mp4?token=iJzfC38d1KC_fvOMAia7xMTGu55uBl2L-9g1eSfHzHCQA7F7QrWMS7h7EgFjck6qduJhp6woMVTu1al8Xklyd1cIYIKYUw46MayhyKje6y-jehBDNM52QM0bmnYxvK6nUfw9VYjiYyDYvUgfviMsI9djv6Kx9hfUwSMLJraRhcauwjYa5Jn4CWQcgnvOxbrv4HNfCu2A5kIWPK_7PQzqKa3CZyVOsNecfuQgcWNr0_-lmeLnwq_1vGYBXtZTGyWTFRkN2wH0Bpa31p3xRcXXb_qhzeNGuJqmtNvba7uIMg9UcZt59F8a_5ws2SpFXXc1t6ZTWwLEU-6jbetm-TpStw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧰
کالکشن ۱۷۰ ابزار کاربردی و متن‌باز
تمام این ابزارها تحت وب هستند و نیازی به دانلود فایل یا ساخت اکانت ندارند:
🎬
مدیا: ویرایش حرفه‌ای ویدیو و صدا
🖼
تصویر: فشرده‌سازی، تغییر سایز و افکت
🔄
مبدل‌ها: تغییر سریع فرمت فایل‌ها
📄
اسناد: ادغام، جداسازی و ویرایش PDF
📰
داده: پارسرها و پنل‌های مانیتورینگ
🔗
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6743" target="_blank">📅 16:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doeeFzpMo1j0pJGKQr2pGUNdBZRT6UwfJnpOEc8Plwk9sA_kwILL-3TNkd3WbFleKB2JndRCSwFA-dcoHdQG1pjPsGlMOBcFhzf9IC601Wxcnc6Yus8pCSQ2hd46EkiRMEkMwKACZtqP16pdVP2jAxOdZ_ozBFRqHvt2wFuaF4euafR3-QZwdpQypx5vCW7ySEoxUb9dyEEPe3Me38wTdMntq2cNfb3k0htLFOgBI_eCySwY8Z7XzyTnx31tuMRQam2Y6kFZ-qZIE3fCam18TuVzMWJsRO04rLaVD3wkjrnwdZ0qINHP2UvuNF-zXuo8epRgr0iVWyPSKrlE5FBbHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
راهکارهای اتصال پایدار و پرسرعت برای اینترنت آزاد
🔹
پشتیبانی از V2RayNG، WireGuard، SlipNet و ArgoVPN
🔹
ارائه اشتراک‌های عادی و گیمینگ متناسب با نیاز کاربران
🔹
انتشار کانفیگ‌های رایگان، آموزش و پشتیبانی
🔹
تست کیفیت اتصال قبل از استفاده
📢
TirexNet؛ همراه شما برای دسترسی بهتر به اینترنت
🤖
Bot:
@TirexNetBot
💬
Support:
@HRMP1386</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6742" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏
🚀
دسترسی رایگان به غول‌های هوش مصنوعی!
‏اگر دنبال جایگزینی برای ‌Agent Router⁩ هستید،
سایت ‌
Bluesminds⁩
فوق‌العاده است. با ثبت‌نام، 100 دلار اعتبار اولیه هدیه بگیرید و با مدل‌های قدرتمندی مثل:
🔹
‌GLM 5.2
🔹
‌Qwen 3.6
🔹
‌Minimax M2.7⁩
🔹
‌Mimo 2.5
‏کار کنید. همین حالا امتحانش کنید و پروژه‌هاتون رو به سطح جدیدی ببرید!
✨
🔗
Docs
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6741" target="_blank">📅 14:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دوستان خوشتون نیاد هر چیزی رو ببرین تو ai ها. حالا ی سری کمپانی ها روشون نظارت هست، سیاست policies دارن. تو اروپا gdpr هست. که اکثر شرکتها تو اروپا ملزم به رعایت کردنش هست. حالا در کل بماند که حریم خصوصی و پرایوسی، لول بندی داره. ی شرکت کل داده های مهمتون…</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6740" target="_blank">📅 12:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوستان خوشتون نیاد هر چیزی رو ببرین تو ai ها. حالا ی سری کمپانی ها روشون نظارت هست، سیاست policies دارن. تو اروپا gdpr هست. که اکثر شرکتها تو اروپا ملزم به رعایت کردنش هست. حالا در کل بماند که حریم خصوصی و پرایوسی، لول بندی داره. ی شرکت کل داده های مهمتون فضولی میکنه. یکی میفروشه به دلال های داده (مثه گوگل و مایکروسافت و...) یسریا هم که حریم خصوصی محورن.
الان هرمس اینا رو واقعا نمیدونم. هر چی بیشتر این مدلا رو بیشتر وارد چیزاتون میکنین، ریسکش بالاتر میره در کل. باز این شرکتا اروپایی نظارت بالاتر هست ولی نمیدونم طرف خوشش میاد از ی مدل میگه به به چ مدلی چقد قابلیت بذارم چنل، ملت کلی ویو میزنن استفاده میکنن. طرف به تلگرامش و... هم وصل میکنه بعد اخر بعد چند روز میگه ببخشید هرمس رو شخصی ران نزنید
اینو میخواستم چند روز پیش بذارم ولی گفتم ولش. ولی حس کردم بهتره بگم تا پیشگیری بشه بهرحال</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6739" target="_blank">📅 12:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcuF1pyTp0CwHkWG-nIKl3K0sXgPSDV5cOdnIr9HPxbZJdG-5c5DVT4yyzjKNGCrpK2SFp_MLFVHtwW-3Sz9m4lCP_r8NyuwAfTpBGrOcJ2xFFTr25pN1Qzx9V-QCtpjCkDrpU4pWXrEJhvj28zB2pOTJjeoDrTZsMypv-O4tJOxB1nbmtZZKvmTO6XyK6x732uXHyjRUt6sw1VUch8b37mU0yAMyU5EOukcaJU7qIE8tDGl0SGwgFNfijcV_a59ioUv-_cKzsH43Gg4f4fyIvyoQz3SRLqfhc9vQhIysbTF4bXLJ3d1wf9rMrvxEQqWKEy6sq5Gpyvflpa0g6Nzcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/ArchiveTell/status/2074039784629014892?s=20</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6738" target="_blank">📅 11:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhwSyJFlWOCbMNChNJkIGlXxJs-4YJ4bhOZsLHJq3vYLwxXQGZyobkpSG8Pm7XUa_O1EHyLXcGqsJY64CFa1qWPo3O6hW52b5RaWJL4f5Cdj8HAX-cxpEgKiE4hRjnIalmkCdNfTWi8di_cHpJghymVFsAeu4Azyyo6mlTh0F5HgpMWhYOABGXpwKT3kT84vyedJgI_Nm9llzbgYYpZHjMJImzIlB7bIV199jH99PS3C_yke2I6yVV1C8xlRuHgIIvxFwjWmvp4cTKH4DhoJCH6oq6lHOXJKDmc4sD6b2XestNNzzpjnR0ZmTNHjuVcGVWbiu66UgxhV2znlSfXDMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
اجرای هر بازی اندرویدی مستقیماً روی کامپیوتر
یک شبیه‌ساز رسمی از گوگل که واقعاً سریع است و به راحتی از رقبا پیشی می‌گیرد.
🔹
پشتیبانی کامل از اندروید 14، از همان ابتدا.
🔹
عملکرد از طریق Hyper-V — همه چیز پایدار و سریع است.
🔹
هر فایل APK را بدون هیچ مشکلی اجرا می‌کند.
🔹
بدون هیچ بنری یا تبلیغ مزاحم.
🔹
بازی‌ها بدون هیچ‌گونه کندی یا تأخیر اجرا می‌شوند.
دستورالعمل به زبان فارسی
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6737" target="_blank">📅 10:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDekgFwhrFsSMdpYMQm979NI8xKLngoMAwgtMyYMc0ueCB3gICWQInLntKqG3wOOuyToD2MLSp5oVH21Xcwi_yGGLwV5s9i8N_lREiMKQA3WTEC1pFWIeGCEBy1m0xpPQzvJCO4qQbaIp-6kkqTaen2SNq-Jd0_QGfvoKLM_ha5r5LUY1W7nLlAAkURgM_U-aFkUauH4Oz45luTvIGPsO5uSLgd_U5ujEiITtAP7mL0bo3S1WqNO1O0TITxkiKz8BANeWgJlq17zcj_wiwnIBw-fPWl8j1Z-U-VeyhBcB7kic33Y0MAIXiUkEbQqHk4kjoCYgvdKRbD7KDv6bqGkfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
کپ‌کات رو فراموش کنید؛ این ابزار رایگان و بدون نیاز به نصب جادو می‌کند!
‏اگر برای ادیت ویدیوهای خود به دنبال یک ابزار سبک، همه‌فن‌حریف و کاملاً رایگان هستید، پروژه متن‌باز ‌OpenReel⁩ دقیقاً همان چیزی است که نیاز دارید. این ادیتور قدرتمند مستقیماً درون مرورگر شما اجرا می‌شود و نیازی به نصب هیچ برنامه‌ای ندارد.
‏
💡
چرا ‌OpenReel⁩ یک جایگزین بی‌نظیر است؟
‏
🔹
ادیت چند لایه حرفه‌ای: قابلیت ویرایش همزمان چندین لایه ویدیو و صدا همراه با پیش‌نمایش زنده و بدون افت سرعت.
‏
🔹
امکانات کامل کپ‌کات: دسترسی به افکت‌های متنوع، ترنزیشن‌ها، پرده سبز (‌Chroma Key)⁩، کنترل سرعت و فریم‌های کلیدی (‌Keyframes)⁩.
‏
🔹
ابزارهای جانبی کاربردی: قابلیت ضبط صفحه نمایش، کار با متن و زیرنویس، و خروجی گرفتن سریع با فرمت‌های ‌MP4⁩ و ‌WebM⁩.
‏
🔹
کاملاً رایگان و امن: بدون نیاز به ثبت‌نام‌های پیچیده، پرداخت درون‌برنامه‌ای یا واترمارک روی ویدیوها.
‏بدون درگیر کردن حافظه سیستم یا گوشی، همین حالا ادیت ویدیوهای خود را در سطح حرفه‌ای شروع کنید!
🔗
Site
|
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6736" target="_blank">📅 10:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6735">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvcMaQo931aNh31Cu2quTIKIXL9K0-bFFqSif2GnNeUDAulkc-1zi_65DmmY0YoU-i3V31Zox4ouKdg2UqgPmdgH6y4MuQbt-FFBsgqssbbVEVpcuz7UbtLW7Y2XzP24o3I_2kiXzeMsAJ9CL9ZeFu1hXP9laghtlxbk9AIUzZYKnS2efng69a6tLlcsUMup03hLobL1NDl_Ma62wVfdI2kLMstkWubWtTsAyg_nYlIPJQUsPEi45otEN7xHEgCGBvx75vwLgw47cOtfDPTx_2_t9B9FSJ1Sla5SvoOfVxuMRHlPRzD6svikEJ7UYhzy78AnHu7wg1Yz_JWfYIVXVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
تمام غول‌های هوش مصنوعی دنیا، زیر یک سقف!
‏دیگه نیازی نیست برای تولید متن، کد، ویدیو یا عکس، بین ده تا سایت مختلف چرخ بزنی و کلی اکانت پولی بخری. این پلتفرم همه‌چیز رو برات یک‌جا جمع کرده!
‏
✨
چرا این ابزار بازی رو عوض می‌کنه؟
🔹
تیم رویایی در یک پنجره:
به راحتی و با یک کلیک بین قوی‌ترین مدل‌های دنیا یعنی ‌ChatGPT⁩، ‌Claude⁩، ‌Gemini⁩، ‌Grok⁩ و ‌Kimi⁩ جابجا شو.
‏
🔹
تولید همه‌جانبه:
از نوشتن کدهای پیچیده و متن‌های خلاقانه تا خلق تصاویر و ویدیوهای جذاب، همه در یک محیط واحد.
‏
🔹
سهمیه رایگان روزانه:
هر روز کلی توکن رایگان بگیر و پروژه‌هات رو جلو ببر.
https://www.easemate.ai/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6735" target="_blank">📅 10:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6734">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ri5JqBiUqRQT6lcXmaPBCQathi2QUn4l2Fm_IUddW9GRQTiR4yN0rkMtXXdQbYAwP6I05iyD-elvi0gMbPd0Uyft2tDKKenH9hJgQ3LGK6mwPFe4ottBdBjJjPq6oFcwFKindgYl6S7jXF829Wv1wzP0tiqgw4DDU_UjEdIHddSxII41y-O4lCGZWGZYlYA2_LRxR6O2e0YQH-EueZOAmxGXdcfEttPby5q1HAohjioQaLve9EGnlzwj5nEMPJxh14Chqlu8eqcbUpacFe-m4IyPERMMZHySiyYbW7HbzP3ywv9m6psj2tMyBU1f_YkQYe_xYVjdtDKtjrAzfxvvdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
غول هوش مصنوعی، بالاخره رایگان و بی‌دردسر!
‏دیگه نیازی به خرید اکانت پرمیوم یا دردسرهای ست کردن ‌API⁩ نیست؛ از امروز می‌تونید به صورت کاملاً رایگان توی پلتفرم ‌Tabbit⁩ با شاهکار جدید ‌Anthropic⁩ یعنی Claude Sonnet 5 گفتگو کنید!
💻
✨
‏
💡
چرا این خبر بمبه؟
سونت ۵ در حال حاضر یکی از باهوش‌ترین و دقیق‌ترین مدل‌های دنیاست که حالا بدون هیچ محدودیتی در دسترستون قرار گرفته. فقط کافیه وارد سایت بشید و چت رو شروع کنید
https://tabbit.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6734" target="_blank">📅 09:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🗂
هیچ‌چیز رو دور ننداز! معرفی Karakeep؛ بهشتِ آرشیوکارها و خوره‌های اطلاعات
🧠
اگر شما هم از اون دسته‌اید که روزانه ده‌ها لینک، مقاله و ویدیو رو برای «بعداً خوندن» ذخیره می‌کنید و در نهایت بینشون گم می‌شید،
Karakeep
(با نام قبلی Hoarder) دقیقاً برای شما ساخته شده. این ابزار یک جایگزین فوق‌العاده، سلف‌هاست و متن‌باز برای برنامه‌هایی مثل Pocket هست که با جادوی هوش مصنوعی ترکیب شده!
🔥
چرا Karakeep بی‌نظیره؟
🤖
تگ‌گذاری خودکار با AI:
با استفاده از LLMها (حتی مدل‌های لوکال مثل Ollama)، محتوای شما رو بررسی کرده و به صورت خودکار تگ‌گذاری و خلاصه‌نویسی می‌کنه.
🗄
آرشیو ابدی صفحات و ویدیوها:
برای جلوگیری از حذف شدن لینک‌ها (Link rot)، کل صفحه وب رو به صورت آفلاین ذخیره می‌کنه و حتی ویدیوها رو به کمک yt-dlp دانلود و آرشیو می‌کنه!
🔎
جستجوی قدرتمند و OCR:
متن داخل عکس‌ها رو استخراج می‌کنه و می‌تونید در کل محتوای ذخیره‌شده (فول‌تکست) جستجو کنید.
📱
همه‌جا در دسترس:
دارای افزونه برای کروم، فایرفاکس و سافاری، به همراه اپلیکیشن اختصاصی برای iOS و اندروید.
🔌
تعامل با ایجنت‌ها:
کاملاً سازگار با ایجنت‌های هوش مصنوعی (مثل OpenClaw) برای مدیریت خودکار اطلاعات از طریق CLI.
اسم این برنامه از کلمه عربی «کراکيب» (Karakeeb) الهام گرفته شده؛ به معنی خرت‌و‌پرت‌هایی که شلوغ به نظر می‌رسن اما پر از ارزش و خاطره‌ان و نمیشه دور ریختشون!
🔗
لینک مخزن گیت‌هاب پروژه:
https://github.com/karakeep-app/karakeep
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝑒𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6733" target="_blank">📅 08:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یه پروژه مدیریت vps توسط ai زدم شب میفرستم.  اینطوریه که ازت آی‌پی و پس رو میگیره  بعدش تو دستور میدی. میگی مثلا ثنایی رو بالا بیار، تونل فلان نصب کن، رباتمو بالا بیار و ... خودش قشنگ انجام میده آخرش ازت تشکرم میکنه‌  دیگه نیاز نیست دستور های ترمینال رو بدونی…</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6732" target="_blank">📅 04:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚀
آموزش نصب OpenCode و استفاده رایگان از مدل های هوش مصنوعی زیر :
🔸
Mimo 2.5
🔸
Deepseek 4 flash
🔸
Nemotron 3 Ultra
🔸
Big Pickle
🔸
North Mini Code
🔘
آموزش نصب در موبایل
1️⃣
نصب Termux
اگر روی موبایل هستی
اول Termux را نصب کن
📱
2️⃣
دستورات داخل Termux
1) آپدیت Termux
pkg update -y && pkg upgrade -y
2) نصب ابزارهای لازم
pkg install -y proot-distro nano
3) نصب Ubuntu
proot-distro install ubuntu
4) ورود به Ubuntu
proot-distro login ubuntu --user root
3️⃣
دستورات داخل Ubuntu
1) آپدیت Ubuntu
apt update && apt upgrade -y
2) نصب پیش‌نیازها
apt install -y curl bash ca-certificates wget git nano gnupg lsb-release software-properties-common build-essential python3 make g++
3) نصب OpenCode
npm i -g opencode-ai
4) اجرای OpenCode
در یک پوشه اجرا کنید
مثال :
cd /storage/emulated/0/Download
سپس‌ :
opencode
4️⃣
اگر خواستی بعداً دوباره وارد Ubuntu شوی
proot-distro login ubuntu
5️⃣
اگر OpenCode را نصب کرده‌ای و فقط می‌خواهی اجراش کنی ، قبلش وارد پوشت شو
opencode
🔘
داکیومنت رسمی برای نصب در جاهای دیگر
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6731" target="_blank">📅 02:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🎬
تدوینگر اختصاصی شما داخل ترمینال! معرفی ابزار فوق‌العاده Video-Use
🚀
دوست دارید فقط با چت کردن با عامل‌های هوش مصنوعی (مثل Claude Code یا Codex) ویدیوهاتون رو ادیت کنید؟ پروژه اوپن‌سورس
video-use
دقیقاً همین کار رو می‌کنه. فقط کافیه ویدیوهای خام رو بریزید داخل یک پوشه و با زبان طبیعی بهش بگید چی می‌خواید تا یک فایل نهایی (
final.mp4
) ترتمیز بهتون تحویل بده
.
🔥
چرا این ابزار انقلابی و متفاوته؟
🧠
پردازش هوشمند و ارزان:
به جای اینکه کل ویدیو رو به خورد LLM بده (که به شدت گرون و پرخطاست)، فقط یک فایل متنی سبک از ترانسکریپت با تایم‌استمپ دقیق کلمات و در صورت نیاز اسکرین‌شات‌هایی از تایم‌لاین (شامل فرم تصویر و موج صدا) رو بررسی می‌کنه.
✂️
حذف اتوماتیک اضافات:
تپق‌ها، مکث‌های طولانی و کلمات اضافه رو به صورت خودکار تشخیص میده و هوشمندانه کات می‌زنه.
🎵
تدوین بی‌نقص:
روی تمام کات‌ها ۳۰ میلی‌ثانیه فید (Fade) صوتی میندازه تا هیچ‌وقت صدای پرش کات رو نشنوید.
🎨
زیرنویس و انیمیشن:
می‌تونه زیرنویس‌های کاستوم (مثلاً کلمات دوتایی بزرگ) روی ویدیو بندازه و با ابزارهایی مثل Manim ،Remotion و HyperFrames انیمیشن تولید کنه.
🤖
حلقه خودارزیابی (Self-Eval):
قبل از اینکه خروجی رو به شما نشون بده، خودش ویدیو رو بازبینی می‌کنه تا پرش‌های تصویری یا مشکلات صوتی رو پیدا و برطرف کنه.
این ابزار مثل این می‌مونه که یک کارگردان و یک تدوینگر رو همزمان داخل محیط کدنویسی خودتون داشته باشید که حتی پروژه‌ها رو ذخیره می‌کنه تا روزهای بعد بتونید ادیت رو ادامه بدید!
🔗
لینک گیت‌هاب پروژه برای نصب و راه‌اندازی
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6730" target="_blank">📅 01:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">thefeed-android-v0.30.8-universal.apk</div>
  <div class="tg-doc-extra">25 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6729" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
نسخه جدید
#TheFeed
(v.0.30.8)
🔹
بهبود مدیریت لینک ها در برنامه، اگر توی یک پست ای دی یک کانال دیگه و یا لینک یک پست از یک کانال دیگه باشه، وقتی روش بزنید میتونید به اون کانال و پست منتقل بشید، توی قسمت فید باید اون کانال حتما توی اون کانفیگ وجود داشته باشه، توی قسمت میرور خودکار اون کانال به لیستتون اضافه میشه.
📯
من نسخه اندروید
universal
که مناسب همه‌ی گوشی های اندروید هست رو توی این کانال میزارم. ولی اگر نسخه‌های دیگه رو میخواید باید از گیتهاب و یا کانال زیر دانلود کنید (
ویندوز
،
مک
،
لینوکس
،
بی‌اس‌دی
، اندروید‌های
قدیم
و
جدید
،
ترموکس
، و حتی
نسخه ipa
آیفون) و لینک دانلود نسخه آیفون از تست‌فلایت توی کانال پین شده، البته هنوز آپدیت نشده.
📢
کانال اصلی دفید:
@networkti
📦
کانال فایل‌های باینری/نصبی دفید:
@thefeedfile
⚙
کانال کانفیگ‌های دفید:
@thefeedconfig
🔗
گیتهاب پروژه:
https://github.com/sartoopjj/thefeed</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6729" target="_blank">📅 00:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚀
معرفی CdnScanner؛ جامع‌ترین و قدرتمندترین اسکنر IP و CDN
🚀
✨
ویژگی‌های برجسته:
* پشتیبانی کامل از ۱۷ سرویس‌دهنده (CDN): شامل Cloudflare (و WARP/Workers)، AWS CloudFront، Google Cloud، Azure، ArvanCloud، Fastly، Vercel، Akamai، Gcore و...
💪
تست فوق‌دقیق بر اساس کانفیگ شما: در این ابزار IPها فقط زمانی تأیید می‌شوند که با کانفیگ V2Ray واقعی شما (شامل SNI، Host و Path) پاسخگو باشند (پشتیبانی از TCP connect + TLS Handshake + HTTP HEAD).
🫆 اسکنر اختصاصی HTTP: امکان وارد کردن مستقیم IP، دامنه یا رنج CIDR (مانند
1.1.1.0/24
) با قابلیت بازگشایی و اسکن خودکار کل رنج.
* تولید خودکار خروجی V2Ray: ساخت بی‌درنگ لینک‌های VLESS ،VMess و Trojan از IPهای سالم با قابلیت کپی و دانلود یک‌کلیکه!
* پینگ واقعی (ICMP): عملکرد دقیق روی Windows ،Linux و macOS (همراه با سیستم جایگزین TCP در صورت مسدود بودن پینگ).
* اسکن کامل و بدون نقص: بررسی جزء‌به‌جزء تمامی IPهای یک رنج مشخص، به جای اکتفا به نمونه‌های تصادفی.
* رابط کاربری مدرن و فارسی (RTL): داشبورد حرفه‌ای و چشم‌نواز همراه با نوار پیشرفت (Progress bar)، کارت‌های آماری، پیام‌های Toast و طراحی کاملاً راست‌چین.
📥
دریافت و نصب:
همین الان می‌توانید این ابزار قدرتمند و متن‌باز را از گیت‌هاب دریافت کنید. (اگر ابزار برایتان کاربردی بود، دادن ستاره
⭐️
به پروژه در گیت‌هاب فراموش نشود!)
🔗
لینک پروژه در گیت‌هاب:
https://github.com/ScannerVpn/CdnScanner
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6728" target="_blank">📅 21:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6727" target="_blank">📅 19:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یه پروژه مدیریت vps توسط ai زدم شب میفرستم.
اینطوریه که ازت آی‌پی و پس رو میگیره
بعدش تو دستور میدی. میگی مثلا ثنایی رو بالا بیار، تونل فلان نصب کن، رباتمو بالا بیار و ...
خودش قشنگ انجام میده آخرش ازت تشکرم میکنه‌
دیگه نیاز نیست دستور های ترمینال رو بدونی یا حفظ کنی. تو فق به زبان فارسی بش میگی انجام میده</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6726" target="_blank">📅 18:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">https://x.com/ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6723" target="_blank">📅 13:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دیده‌بان لیکفا منتشر شد
🆕
افزونه‌ای برای مرورگر کروم که هنگام بازدید از وب‌سایت‌ها، اگر آن سایت سابقه نشت اطلاعات داشته باشد، به‌صورت خودکار به شما هشدار می‌دهد. متن‌باز، رایگان، کاملا محلی و بدون ارسال اطلاعات به سرور
👍
Download
🛫
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6722" target="_blank">📅 13:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JToa-2nNz-29y7Fkem0yEer52GXHVnu64TCVKO3qFL4EeUaIWzUNaCVPYJS9ACoZ8jawqHpbo-j6BsZ6iQhbXlVpIeVDV9Q6yu8oLJLWkgOJ85uKzz7rxJ0i8-U2bjcmY4ufKE5c2O7yCK5k3G3iEq6bo8MjKXe257uq_gCjmq3LgLQtW8pGCZtXg9F2gUBxnduYhKPAdGNWAq2v58smkNyEmji6o7I9N7FAJdvn6MvfHyYN_wRoDKaxQVd_rIVh7yUGbVHOTHxAFPsUGMCGtB_ejiE0MSYX45-vLYhI1dmFgcXI38eXRxkhEX9bugEI-t0GZE78YyCOoLDATwrpVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💻
سیستم‌عامل شخصی، مستقیم توی مرورگر!
‏یک پلتفرم متن‌باز و سبک که می‌تونی روی سیستم خودت بالا بیاریش (‌Self-host)⁩ و همه‌چیز رو کاملاً آفلاین و امن مدیریت کنی.
‏
✨
چرا جذابه؟
🔒
امنیت مطلق:
داده‌ها فقط روی هارد خودت ذخیره میشن.
‏
🛠
ابزارهای کاربردی:
ویرایشگر متن، ضبط صدا و پلیر داخلی در یک تب.
‏
🚀
فوق‌العاده سبک:
بدون نیاز به سخت‌افزار قوی، فقط با یک کلیک.
‏
⚡️
راه‌اندازی:
دریافت سورس از گیت‌هاب و اجرا با داکر.
🔗
لینک گیت‌هاب پروژه
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6721" target="_blank">📅 12:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🐦‍🔥
اسکنر قدرتمند سیمرغ (SIMORGH Scanner v0.3.0) منتشر شد!
🚀
اگر برای کانفیگ‌های VLESS خودتون دنبال پیدا کردن IP تمیز کلودفلر هستید، اسکنر سیمرغ یکی از بهترین ابزارهاست. به تازگی نسخه 0.3.0 اون با یه رابط کاربری وب بسیار جذاب (نئونی-رترو) منتشر شده.
🔥
ویژگی‌های خفن این نسخه:
💻
پشتیبانی از ویندوز و اندروید:
نسخه ویندوز به صورت Standalone هست و بدون نیاز به اینترنت اولیه یا نصب پایتون، به راحتی با یک کلیک اجرا میشه. نسخه اندروید (APK) هم با بک‌اند بومی Go نوشته شده و کاملاً برای صفحه نمایش موبایل بهینه‌سازی شده.
🎯
تست همه‌جانبه:
می‌تونید تک IP، رنج‌های CIDR و لیست‌های ISP رو اسکن کنید. این ابزار دارای دسته‌بندی لیست‌های آماده ISP ایران و بین‌الملل هست و حتی می‌تونید لیست اختصاصی خودتون رو به صورت فایل txt وارد کنید.
⚡️
امکانات دقیق اسکن:
دارای قابلیت‌های نمایش پینگ (Latency)، بررسی مجدد (Re-check) و تست سرعت (Speed test) به صورت مجزا هست.
📁
خروجی حرفه‌ای:
در نهایت آی‌پی‌ها و کانفیگ‌های تمیز رو رتبه‌بندی می‌کنه و خروجی‌های مرتبی مثل best_configs.txt و clean_ips.txt بهتون تحویل میده.
🔗
لینک گیت‌هاب پروژه برای دانلود نسخه‌ها
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6720" target="_blank">📅 11:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb0268ad1.mp4?token=vQgi99qY-65fhj4v4MvxSjyyumNA4yY7yFpLBvMn_ikIYhuwUazq1baqQJ3kxhw3sPEV6HwxU1z-DDELfqbOB3V8IY6C6zH07PSu9J8b9wAx_mHCoGVN_wu84qdvewqN2Nbv-gN5HlsZjZj65TxGVE3wAGDidGKWTEaof_WJcsAUC5reQiJuKJmz-Fks5ldj75gB-bYVEq2Bwco8gsP331LK58Klc55XGCQyMFG8pAbru0ksijz5kijVhuSPRN7kubQKI5n93aN_aU1YdewZatmqt7g6BJDMV2YFge2dEwYqMnN_pZeUX9pCovUP6yYor1xktfWP_UPm9b-Ueleaqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb0268ad1.mp4?token=vQgi99qY-65fhj4v4MvxSjyyumNA4yY7yFpLBvMn_ikIYhuwUazq1baqQJ3kxhw3sPEV6HwxU1z-DDELfqbOB3V8IY6C6zH07PSu9J8b9wAx_mHCoGVN_wu84qdvewqN2Nbv-gN5HlsZjZj65TxGVE3wAGDidGKWTEaof_WJcsAUC5reQiJuKJmz-Fks5ldj75gB-bYVEq2Bwco8gsP331LK58Klc55XGCQyMFG8pAbru0ksijz5kijVhuSPRN7kubQKI5n93aN_aU1YdewZatmqt7g6BJDMV2YFge2dEwYqMnN_pZeUX9pCovUP6yYor1xktfWP_UPm9b-Ueleaqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
‌GitFut⁩:
رتبه‌بندی پروفایل ‌GitHub⁩ مثل بازیکنان فیفا!
⚡
‏هر توسعه‌دهنده‌ای تو دنیای کد یه ستاره‌ست!
🌟
‏این ابزار
رتبه ۰ تا ۹۹
رو بر اساس:
‏
🔹
تعداد
‌commit⁩ها
‏
🔹
ستاره‌های ریپو
‏
🔹
دنبال‌کنندگان
‏
🔹
زبان‌های برنامه‌نویسی
‏بهت میده!
‏
ببین به کدوم بازیکن فوتبال شباهت داری!
⚽
💻
‏
👉
امتحان کن
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6719" target="_blank">📅 10:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQGfNkVwPW5lxYHNA_r1HkjoOmqp5QraM6i6H68WZUoLMgfBLCeSmRrx4ZvUZNBLcvIsOODL9VDw_a10SvQth3pJaLcXZMSAEN3YUYvptPWj8Wv9A7Lzup55aBl5InU9B6YNBYW2sb2H7EIbktYZsb8MpCavBW21cuN5mtqTMRRiPpaAyhJaGDvSTNMReNke9nbmSKwY1x0cwrWfopptUz9od-Hus8Jiv3Ee90xq9kInJ4DxBptvZazjujUOr5eVevJUhQHV9bVGuSdLoT5yvKQUcpcJBiqOqQkpl9tD39JZPEVFIuD3uMITMTnzh7oPnQfaLLNKGkq9l5G3O1jMyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
‌scrcpy⁩
— کنترل کامل گوشی اندرویدی روی کامپیوتر!
📱
➡️
💻
‏
✅
بدون دردسر
: نیازی به روت یا نصب اپ روی گوشی نیست! فقط با ‌USB⁩ یا وایفای وصلش کن.
‏
⚡
سرعت بالا
: ۱۰۸۰‌p⁩+ با ۳۰ تا ۱۲۰ فریم بر ثانیه.
‏
🔊
صدا
: انتقال مستقیم صدا (اندروید ۱۱+).
‏
⌨️
کنترل کامل
: موس و کیبورد فیزیکی شبیه‌سازی میشه.
‏
🎥
ضبط صفحه
+ نمایشگر مجازی.
‏
🐧
سازگار
: ویندوز، مک، لینوکس (بدون نیاز به ‌snap)⁩.
‏
🔗
مخزن
:
‌GitHub⁩
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6717" target="_blank">📅 10:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏
🚀
‌Arvix AI⁩ = جعبه‌ابزار کامل هوش مصنوعی تو
‏
🧠
متن:
‌GPT⁩, ‌Claude⁩, ‌Gemini⁩, ‌Grok⁩
‏
🎨
تصویر:
‌Midjourney⁩, ‌FLUX⁩, ‌Nano Banana⁩
‏
🎬
ویدیو:
‌Kling⁩, ‌Veo⁩, ‌Seedance 2⁩
‏
🎧
صدا:
‌Suno⁩, ‌ElevenLabs⁩
‏
🎁
توکن رایگان + دسترسی به همه مدل‌ها
https://arvixai.net/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6716" target="_blank">📅 10:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏
🚀
آموزش دریافت ‌API⁩ رایگان ‌Nvidia⁩
🚀
‏‌
1⃣
ثبت‌نام اولیه:
‏وارد سایت
‌build.nvidia.com⁩
شو و یک حساب کاربری بساز
📧
2⃣
‏‌
شروع تایید هویت:
‏پس از ثبت‌نام، روی کادر زرد رنگ بالای صفحه کلیک کن تا پروسه وریفای آغاز شود.
⚠️
3⃣
‏‌
دریافت شماره مجازی:
‏به سایت
‌2nd-no.com⁩
برو و یک شماره مجازی موقت و رایگان دریافت کن.
📱
4⃣
‏‌
فعال‌سازی حساب:
‏شماره دریافتی را در سایت انویدیا وارد کرده و کد تایید را ثبت کن.
✅
5⃣
‏‌
ساخت کلید دسترسی:
‏به بخش ‌
API keys
⁩
برو و کلید اختصاصی خودت را بساز.
🔑
6⃣
‏‌
انتخاب مدل‌های رایگان:
‏به بخش
‌
Model⁩
برو و از گزینه‌های
‌Free Endpoint⁩
استفاده کن.
🤖
‏
🌟
برخی از بهترین مدل‌های در دسترس:
🔹
‌GLM 5.2⁩
🔹
‌Minimax M3⁩
🔹
‌Deepseek v4 pro⁩
🔹
‌Kimi k2.6⁩
🔹
‌Qwen 3.5⁩
‏
بدون محدودیت توکن
🔓
بدون لیمیت روزانه
‏
♾
40
درخواست در دقیقه
‏
⏱
🔵
@ArhiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6715" target="_blank">📅 03:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318f76cfea.mp4?token=EWrS9qCsBoGyVIZ_jeuaG-gJXBGLeFWQttv1gAr2_7pD0Yu0JTdAP53IlhvToRVT-CMLMh-3Lauom_spqdmFtmWVUejI_m1rhF8LfcGcAoHqXyahHwQWENXkcqK8-0oHXWEii82kBrVWVvfpsHM6TusscPbCEAH_q0WTSAQFppSOd1EqEZ1sljAv-Q4hXa1ibFMtpc04UGZNVnxDFVuOKENCuhB589iEv63zK4eT8EnU3hDVr_OoqRGcSOFV9KN7RwCQCvH5t-OPN5oe7hBs_VfDOhbzn1MJrqroad_TdHmk6tdoWt_GY0YKxRg5Dl-R8kfxWiY3MeSo_tYZI9pJ9EOXfGKtiPXWMCAbbEhDFvwawz0fABApbfzeK1Fr1jeQszck-AypPxERMKEdb4h-vt1uiOSLAxE0SCZeAWi7c-m7cE9OBpmZdrkmvCyT783HkhaYMOfOwHYCC0EBTA5IwmtshLmOdL32bnicwAfxtm4bs4K_XfkIdvA4jrjoiCMe-PloxS7drawN3TMtJJAE26wJ7ZccmjSKWo6pcOFK8r3jkVpVhIem7De3E1KIj0oCecg-igI0ZlcGbtyCvjUUYeI0orR4TBlrHAIy49-t9zbBX_Ee8mkRl857WpXrHFFDH9it-21K6UuF8q5DWAuLlpzIHrJ6TTjUT_1E4e8LSDY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318f76cfea.mp4?token=EWrS9qCsBoGyVIZ_jeuaG-gJXBGLeFWQttv1gAr2_7pD0Yu0JTdAP53IlhvToRVT-CMLMh-3Lauom_spqdmFtmWVUejI_m1rhF8LfcGcAoHqXyahHwQWENXkcqK8-0oHXWEii82kBrVWVvfpsHM6TusscPbCEAH_q0WTSAQFppSOd1EqEZ1sljAv-Q4hXa1ibFMtpc04UGZNVnxDFVuOKENCuhB589iEv63zK4eT8EnU3hDVr_OoqRGcSOFV9KN7RwCQCvH5t-OPN5oe7hBs_VfDOhbzn1MJrqroad_TdHmk6tdoWt_GY0YKxRg5Dl-R8kfxWiY3MeSo_tYZI9pJ9EOXfGKtiPXWMCAbbEhDFvwawz0fABApbfzeK1Fr1jeQszck-AypPxERMKEdb4h-vt1uiOSLAxE0SCZeAWi7c-m7cE9OBpmZdrkmvCyT783HkhaYMOfOwHYCC0EBTA5IwmtshLmOdL32bnicwAfxtm4bs4K_XfkIdvA4jrjoiCMe-PloxS7drawN3TMtJJAE26wJ7ZccmjSKWo6pcOFK8r3jkVpVhIem7De3E1KIj0oCecg-igI0ZlcGbtyCvjUUYeI0orR4TBlrHAIy49-t9zbBX_Ee8mkRl857WpXrHFFDH9it-21K6UuF8q5DWAuLlpzIHrJ6TTjUT_1E4e8LSDY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تبدیل ویس به متن تلگرام کاملاً رایگان! (بدون نیاز به پریمیوم) با هوش مصنوعی Cloudflare
https://youtu.be/Xq7e2k3qlqA</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6714" target="_blank">📅 02:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دوستان وقت بخیر و خسته نباشید
این چنل زاپاس آرشیوتل هستش
داشته باشین بهتره
❤️‍🔥
ی موقع اگ چیزی شد...
https://t.me/FOSSArchive</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6713" target="_blank">📅 22:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0691365cb.mp4?token=Hw1RA49hL4vOsUp4uatbTsSe2f2vtKh6Qlhp6F49ySe4wZ52VzeY9wetuVnF6I5jJPIja1N1qMNRszM8WN9nsCrH-vS-_kRW0_OZ7O8UNjk-bjJgFA_i2fqTQ7-OWoTy4rTzsMZoeN5H8lkMK_8nxXhWp6pJNBvElkej79jLztalVjqcri8WaQeZflkRJgObdbhzabdQQCpmvJew5TFrAh0UGZQXhdObz79fpQOGaRzzlJ9iVoKyEsAFbgFNhR6dLvoNmuwZo-hO61oF8wl6JjGmmGHYa8wPwIUR_LY9ZIGRXwXBVpKD1ay3jIqHMvEF60LxWAPd8ZYnSTkkG91rqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0691365cb.mp4?token=Hw1RA49hL4vOsUp4uatbTsSe2f2vtKh6Qlhp6F49ySe4wZ52VzeY9wetuVnF6I5jJPIja1N1qMNRszM8WN9nsCrH-vS-_kRW0_OZ7O8UNjk-bjJgFA_i2fqTQ7-OWoTy4rTzsMZoeN5H8lkMK_8nxXhWp6pJNBvElkej79jLztalVjqcri8WaQeZflkRJgObdbhzabdQQCpmvJew5TFrAh0UGZQXhdObz79fpQOGaRzzlJ9iVoKyEsAFbgFNhR6dLvoNmuwZo-hO61oF8wl6JjGmmGHYa8wPwIUR_LY9ZIGRXwXBVpKD1ay3jIqHMvEF60LxWAPd8ZYnSTkkG91rqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
ImageGlass
ابزار سبک و سریع برای مشاهده عکس ها در ویندوز با پشتیبانی از طیف گسترده ای از فرمت های فایل.
• پشتیبانی از بیش از 90 فرمت: WEBP, GIF, SVG, AVIF, JXL, HEIC
• رابط کاربری بصری با سرعت پردازش بالا
• مناسب برای کاربران عادی و طراحان
https://github.com/d2phap/ImageGlass
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6712" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423195fff7.mp4?token=iZ11v9a3hxO_XsUcB70Sb87bdxaAl7mKufrEdrLOt4QQmfMntxJDkNQolp-giRVhXrFGuFZRede2SVlUCphsFj1PLJKzBvILuieW0mz0989TFvzJfmi9ckCOOKWqKntmj7Y4xpfbrfWOPGYO21QFm0wWYbps9OZzbZN_8wbR7RvehWdvXEcoiE_qSs-J5e2gU_QoeRsKQZGq5xLcDioedH4c7GtJ7oA_Vfy2WyWUr-b30-0lJFYElSxJq_TAbSmoiKn6FPZb4lDTxywEh1z5UaEcSOHdV5jciXVgn8tHOW-61llT_mMWC-4Jz82OMN5Y_fHxXng63qHh7lz_91AFvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423195fff7.mp4?token=iZ11v9a3hxO_XsUcB70Sb87bdxaAl7mKufrEdrLOt4QQmfMntxJDkNQolp-giRVhXrFGuFZRede2SVlUCphsFj1PLJKzBvILuieW0mz0989TFvzJfmi9ckCOOKWqKntmj7Y4xpfbrfWOPGYO21QFm0wWYbps9OZzbZN_8wbR7RvehWdvXEcoiE_qSs-J5e2gU_QoeRsKQZGq5xLcDioedH4c7GtJ7oA_Vfy2WyWUr-b30-0lJFYElSxJq_TAbSmoiKn6FPZb4lDTxywEh1z5UaEcSOHdV5jciXVgn8tHOW-61llT_mMWC-4Jz82OMN5Y_fHxXng63qHh7lz_91AFvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏کتابخانه‌ی معروف ‌Pad Shaders⁩ (منبع غنی گرادیان‌ها، پس‌زمینه‌ها و شیدرهای خفن) رایگان و متن‌باز شد!
🎨
✨
‏دیگه نگران لایسنس نباش؛ می‌تونی تمام پلاگین‌ها و ابزارهاش رو تو پروژه‌های شخصی و تجاری استفاده کنی.
https://shaders.paper.design/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6711" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6710">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚀
دسترسی به قدرت هوش مصنوعی در سرور شخصی؛ آموزش API کلودفلر (Workers AI)
☁️
🤖
اگر برای پروژه‌هایتان به یک هوش مصنوعی قدرتمند (مثل Llama 3 یا Mistral) نیاز دارید، سرویس
Workers AI
کلودفلر یکی از بهترین و بهینه‌ترین گزینه‌هاست. برای استفاده از این سرویس، باید یک API Token اختصاصی بسازید.
🔥
مراحل دریافت API Token در کلودفلر:
1️⃣
ورود به بخش API:
وارد پنل شوید، روی آیکون پروفایل کلیک کرده و به مسیر
My Profile > API Tokens
بروید.
2️⃣
ساخت توکن:
روی
Create Token
کلیک کنید و سپس
Create Custom Token
را انتخاب کنید.
3️⃣
تنظیم مجوزها (بسیار مهم):
در بخش
Permissions
، گزینه
Account
را انتخاب کنید و دسترسی
Workers AI
را روی حالت
Edit
قرار دهید.
در بخش
Resources
، اکانت خود را انتخاب کنید تا دسترسی‌ها محدود به همان اکانت باشد.
4️⃣
نهایی‌سازی:
روی
Continue to summary
و سپس
Create Token
کلیک کنید.
⚠️
توجه:
کد نمایش داده شده را بلافاصله کپی و در جای امن ذخیره کنید؛ این کد دیگر نمایش داده نخواهد شد!
💡
نحوه استفاده:
شما علاوه بر توکن، به
Account ID
نیاز دارید که در صفحه اصلی
Workers & Pages
پنل کلودفلر قابل مشاهده است.
آدرس فراخوانی (Endpoint) شما به این صورت خواهد بود:
[https://api.cloudflare.com/client/v4/accounts/](https://api.cloudflare.com/client/v4/accounts/){ACCOUNT_ID}/ai/run/{MODEL_NAME}
✅
حالا می‌توانید با استفاده از این توکن، مدل‌های هوش مصنوعی کلودفلر را در کدهای خود (پایتون، Node.js و...) فراخوانی کنید.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/6710" target="_blank">📅 16:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxZvn0_AUdF83vWyMF8sLs7ze_HLF_MNuVLJM9KFXmJQ8uiICvIxXXj2ZpP9NFoe_zAuMokPKMImIBZtweBcqYpeubvMywYHd1AmYmOJf9-u449tnWxiY5JUCnxFL2-ydpKlgxfIGXxAE4fNfD2Hd_nhKtRfYxfzpmheMH3Mho1072HdDMWpH8HfQAAcZSoa2Mo8CfHCyBvQ6W_2xnAY9RYJ_KRrU2b7eeziOqgbHqXzymvf3LFpubMuOSfdtGMloypgI5EvrhUqq8rme7PAaaYkhFtPSfHZt6859_Gz6KUZ_IdQYbi6SDjCh-sgHb79MmOh0rvQ95LUCK5SeT51tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5
هوش مصنوعی رایگان و قدرتمند شرکت انتروپیک
10 دلار کردیت
با لینک زیر 20 دلار
https://v0.app/ref/94OS6T
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/6709" target="_blank">📅 15:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سایفون رو اپدیت کنین خوشگل شده
🔥
(نسخه بتا)</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/6708" target="_blank">📅 14:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/013ef6f73c.mp4?token=VNqrwrK3EOS2m_A7xK1JFdT60KuOU7CN5nxksVqoskL80zuutBM1ay7417S1GrCckQ6D_JbxTgYQcGCmkh-ZWPidev4q9AWZmt7SJ6UBKwVQqEoClkNBpT7d2ouwJNd02ldwEciZoixy-lh68GvjbGflzB0yPDl_1IRqtJ_dfJ3L9TUv0BWIwugnqtT6ZOA_iLiUZvEwBlIoAwByFCPYN9L26fHPC1l6GWH5WoxJKzmXyKgAZSJlYgMByEaqRqtGE-OTrxcPSHZpDNX7EsT-aMQrhXoVs3Yo9LjlhWpltbbl3AV20dOHPvtLx7BX9pl6DE8455k_wmvVBqozmety_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/013ef6f73c.mp4?token=VNqrwrK3EOS2m_A7xK1JFdT60KuOU7CN5nxksVqoskL80zuutBM1ay7417S1GrCckQ6D_JbxTgYQcGCmkh-ZWPidev4q9AWZmt7SJ6UBKwVQqEoClkNBpT7d2ouwJNd02ldwEciZoixy-lh68GvjbGflzB0yPDl_1IRqtJ_dfJ3L9TUv0BWIwugnqtT6ZOA_iLiUZvEwBlIoAwByFCPYN9L26fHPC1l6GWH5WoxJKzmXyKgAZSJlYgMByEaqRqtGE-OTrxcPSHZpDNX7EsT-aMQrhXoVs3Yo9LjlhWpltbbl3AV20dOHPvtLx7BX9pl6DE8455k_wmvVBqozmety_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت 10 تا ایمیل رایگان با ساختن یک ایمیل اتومیک (مولتی اکانت)
https://www.youtube.com/watch?v=XHJ3TwrwG-g</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/6707" target="_blank">📅 03:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPd8IX6n0t606alF4qdPHfuYgjfcsFF2Y56l9NIsQ4jH69nRXXbkWWxWKcyO4M2wcGJS_L3H7AQJWNSSwcWA_XdsXa1A1wSjT3CqlI65wv9x5nTmZURhNtKtYtrkdqytfjBlfQ92k-LdaE8C7CzzqPPpFOGOUWmqOSKc21ijEcr3NG0ytan6Xczm39mAKDNjIrMWUrbmAGt4-DUWPDFOUyKfvt7PmYS1oGlD5kiwyqG2oPIVEsID8yv2eiwV_JMocZSlCptAHAHwjBi0ZtfXeM1ajJHsB-TS3IsrtoqUswjChUzzUu-ZVyaHEg1q9P22AgKSpwJVuo5v8-30_-tmDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
قابلیت جدید «وگا کد» فعال شد!
💻
‏همین حالا وارد
‌Mini App⁩
ربات وگا شوید و از قدرت کدنویسی هوشمند لذت ببرید.
✨
‏
🛠
مشخصات فنی:
‏
🔹
پشتیبانی توسط مدل قدرتمند
‌GLM 5.2⁩
‏
🔹
سقف
۵ درخواست
در هر ساعت
⏳
‏
🔹
ورودی تا
۱۵ هزار توکن
📥
‏
🔹
خروجی تا
۱۶ هزار توکن
📤
‏همین الان تستش کنید!
🚀</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/6706" target="_blank">📅 02:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMblp-Ip7xtw0-Eo4Jac0fZp07T_O1X2LTPpm3p8l1P4fUrsucQKBkuWrf-SrYZ0FqaPdaUuIcVK63S51p-SWV7hPqpQNz9xOvMZJZRitFzqzgbZ11cZcRg2CcbGB-G5SOyQNI7O0c3qX07lDiS0YyWGD-YdZcPAMXB84lPsVIpSUhOsfGhZftSlHvcRdQZ0XumUkzsffWiLqQNHpLv02KaKE4NauY98hGzhqR4wa2bbgSs5Fw5ORHh6JVbRZtwk60gWj09foksLzhoUFFsP5m3aGimcNFvOUX5tTNTZXUqReKkS3JKBjsQw-4N5_6cFpCEmY4H39_E7xQycfrR4hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک میلیون توکن رایگان Gemini از طرف
گوگل؛ بدون نیاز به کارت بانکی!
🎁
✨
گوگل به تازگی یک فرصت بی‌نظیر فراهم کرده است: دریافت یک میلیون توکن کاملاً رایگان برای استفاده از جدیدترین و قدرتمندترین مدل‌های هوش مصنوعی این شرکت. برای دریافت این توکن‌ها به هیچ‌گونه کارت اعتباری یا خرید اشتراک نیازی ندارید و همه‌چیز با یک کلیک انجام می‌شود!
🔥
چگونه کلید API خود را دریافت کنیم؟
1️⃣
ابتدا وارد پلتفرم Google AI Studio شوید.
2️⃣
روی دکمه Create API key کلیک کنید.
3️⃣
تنظیمات و محدودیت‌های تولید را به دلخواه مشخص کنید؛ کلید شما آماده استفاده است!
🤖
مدل‌هایی که می‌توانید با این کلید استفاده کنید:
Gemini 2.5 Pro (قدرتمندترین و هوشمندترین نسخه)
Gemini 2.5 Flash (سریع، بهینه و همه‌کاره)
Gemini 2.5 Flash-Lite (فوق‌سبک و اقتصادی)
💡
کاربرد: این حجم عظیم از توکن‌ها برای ماه‌ها کار فشرده، از جمله کدنویسی، پردازش و تولید متن، تحلیل داده‌ها و حل مسائل پیچیده کاملاً کافی است.
🔗
لینک دریافت کلید API
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/6704" target="_blank">📅 00:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v003aHNPxjc6K0alIEGDxvdGWJqL4BM9RavzoU6K9nO2UF1XVP4Zys_nmj8ejR2s352VeNu-3I4lcLWIDs4HpR_xF6AvM4P8bGlP1op7qPKf6kfh27GgB0bzjuwBG2HJlK4ypKomE_jncMKuH0Cdt5MImdryjZ86f9SLHiYYDiGTsiisNrdDE_MtudckB9Aar9GaLlsWEQRA1mL1D-x4nJndsIm9mjvFCnhX4KsIlT58xsR9jEZc39HeR0Q5H461r-gXHO1XmzTVfv0LgX299AKbccR7ZxQ5A6-u358cUGLa5PSAX2QbPQTndb4NEbo4AD5L8FSESKCVOq9Gh_5Q9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفسیر خطاهای ویندوز با ابزار داخلی
راهنما:
— کد مورد نظر را کپی کنید، مثلاً 0x80070422.
— ترمینال را باز کنید (با فشردن Win+R و وارد کردن CMD).
— دستور
certutil -error 0x80070422
را وارد کنید.
— توضیحات دقیقی از مشکل را دریافت کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/6703" target="_blank">📅 22:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiIZvBnbbVpkuxHCRkFsDNAa6dAgwlp7Ti0o-KUPqWGG4xL509JHZBq56FC1TjfrB4_PVTZDZo2-NzJbDNL7Wo-y8GPXg1cn7hm2AdCZMpsjbD-wd-ydeNHpyeUamtGbUaIiDJUk5BQfHCE27sr3sEBQPu_Ji9AGFbkh35WM0J1vxvr6Qh77C8mGXDRuvF3EV95SlBI__Ga_bXfkDm3fbEmeSHLwuhcO_mqRWuU6usQBY8kKCP9g0i6nT7-sHN3fEiv__jvnDWPiIi87ch5PJbYmR0ykHkBdgxGj8dJPn7B0muAi29ST_qGOCF3UcxBCbrbdgNv-Wh9k4uD6GTSCkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا پولاتو چیکار می کنی؟
پولام:
به زودی ۱ میلیارد*
😊
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/6702" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V4ztz1W1Ro9jj-jgLn3LU3VucJ4-PMRAbhvmD8NUu6fZnd3idazI0kAgo-MYWWpnHk4UZUFjt2bv3DYzdPJJVaLNtQgAKSjft1qhdhiQsTAzKP7pJ2MMqJF_ocU9QqiBd4qIi7iAIQpFTUp2p4EnkIEXeaA88PXDAYsVWeo7rI1B709a0cpP1UdRM38SoaBkgRF2QS2LKmOWGci4aVDDooAZRPcQOFlcaxq33FLs87DN6XR3Ek8GF2JNU8lNheXyEh-LfHLR6pLpdaQ8WvslUjJdIi0xpF6ZjuYgaTBIg0GHWU1vKQZNrq6N_mbIXExm1aSJn_ZCaL7-zbDqAbJQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Um2Sh0xumlHet8RqGu-lmyRkysnsAo6B-han8TQphAMA6pXIQu3zOcrp1lJgxt1WM7Ajw0uJwsjpaS92AoxwTydxsawWhCQ2ki9Uwma2tG-ow8lnkLFWsN667X4778DTreOfDNBYQCWGiAJDkLtldLJUZDQb_sEHlTYWNRdDvsQ7bwx26FYw0JoLqh4NGB-AJLpGeJtKkSxUbipiHfzEL7HA5pEu3eKxLBawQH2oxExevJ1PDNC-zjtPV0ntNM0u5mz5d-2Hl3FqdQ93Mvb6MWwl_VU9bWIMMFBAKrlf_fuhko-oCWfa_QWCHQK44zcei9zIqWWcN8osBm2hjRd7vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/INic9-AnigUUXGfUs9ajaMUPc9g5B7Hf1nugYocXG8DbStXSQK9Vy2Vlk9zrODKnnYokSp8gTdjxNcCsqlxsLS1P8jCUO958zydo2J5-NqOFwELSe336V8JezOgPUK8QyylbKgW9J7wPcyrmoLhNSU3F6qwiXZoqb6VVL8zxQB-fAQZ7xEUPry5cvkWRbgMTs7uPRcrtCf4IGk-0yAdkuYkYd7RDns5QIAxwHQPXj2IUypgADu5UMTp_FwJTTjmIKgUiPchtbAHj0STjaO7YdAcfvD57M4N7YHolLJanZWjwy8kHGM2YHV5SyOLdx950WJuzkgK9kPUhQk5eWYF3PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ThDHB0CdJH_fCIkvR0LUyy8rjH3uQLtF8OAYYQuVmD64ExC9T1_LQgxc13fAVDDkx_Cp1So4DcQzB6NJE21KLG5tOHvHcC-fh2xaMIXCka8udaWi-GoiKK4gC3HlPLNIKQ6T5dKTvJGXuSKdWf__bohEnwnakcNiCYDNBhDP2qD9O_52D0gexAGu-X8JQQ_R0y1UVOOuNhYQwTuyTzT-n3bTjnzYFnn-YAocPLJNkIyTZlTictBTwwbx17tgkP49qYLgs05H0re0k40-BsM2gnhO3xjrN-hYHu9xqTH8aRTmJZKV5aJcSE0Cih-fqyqKQhohxO8mFwmD4jS7hmcUzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HH1CMOxS4SGIr7hUgUAI_G1SeDxwOoM6F_64ACcdKbhDr5itdsdT1S4xhkXLTX4Kurc7Dbgs3KwsOMLYIWDg95YsPVOnwzTlzmTTilysSLKZRER-Ik7mMpnyj68JfGHGASXhEVeZVaiV8qiRNEMbZN-ZgV8GLwD7FBSG4FVvhl7jZ7cUWbRlCj7BaTSYo7GvqroWBZCUhbKgIEUHXDb9v8Ay-sXhlVJbeQMnRCftZtcQfQlD7w4Z8Rr9hynptJuJ9t6aAkXjJZ8-fG5LWLEQHueY_x6PCBy85-CoMjC4chXuXXgJKdOIKPQgBeETPG0mD9L0eG3OyVxXht6RBkfQHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vKRpvCX2sdyrHcnszfkPoK1ApvQAuFJENHXJC8-bIAFUnGk2YG5tIax61CJtLZP-N-54VZejM-CHyIyQyzYSIwpH49RXggX-iu-eVOSrFa4sXn6xrN67Yaj6tSCAPHj2-3-arP1rHWpYaZVCTCn3vDqn1FXWajpBmVe3PXSx2pv8gStCdqoKAcD6CKOUt5wHG0A5in3jrx7BOIu6HBB9FPGKEKyq5AloY86emhw_hEISjc3-UaY4QlNSupHXRz1QPpQoYOKdVlLyJuKOMxuGVtBb6IMTxjbynePirHpfBHlBBCfMurafWCtBxPvnPi1zOraPZLBbSK310QR8zXbVMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ak86aS-g-vxWPqUMh4oNaVdSwa_PQdrZfwwXKjscy55Inw0eWOJcu4zDtXOuVrXZLq2cwrPJTxOMlioDuqqrMOugtStYIw0N-2yfwSTGUejEs1Ld3xW61eFiMgwjBVZIJy6BMXiPmjo1nwjj9MwbLqH-nvTaGMVebwVk0Pdju_ikUmR0eBzAVa7S3LQmrUHu_OxyER-SByfmRiRhjXediQ2jD71wj_mJ-t2bfbm3nAxS-gru2jfdQYZGXCbah0M2vITFXzHAujkmBJSV_aWaz3LgFcVL9oibvHAH-Y6KF_Dm7MG7E98L1wWMW2OItpcgFkIS7PSo1wT_rGgDdNUOYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتایج
جایزه عکاسی با آیفون اعلام شد.
در این مسابقه سالانه عکاسان از سراسر جهان بهترین عکس‌های خود را که با آیفون گرفته اند، ارسال می‌کنند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/6695" target="_blank">📅 17:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7dfwqGgbcgpwQIjeoN6Wn0mZtRwPM3kN7zyIwpVBb_-LblsqcOSy1bmsqrPkKOMam9qoR2_Z7S3409yI7rk6RQAJ8NcA5C5juuC69lTH4JNSWrjZyfGiH3R40uUHoeW66UDvBvC926uyryZYi6Wex0V8v-h2nnEd4Rtlf35ugKVQnc9rrcJi8MQgV-tiRCR0LmLG3aqO6tawxDbhF33zeCrbyC63L5_fF3GnFntgjUrHi2Z1jLjENpi5_CgoY0jL252EmHinQBM1lWwelLW4EMxDmSl4_WdJM00LCb6fE8PBfz45gvj8mzKMoJ4sB4P7IFPtAQ9GRGe8Ys8egw1xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AITwitter Generator
یک افزونه برای تولید توییت است.
این افزونه که بر اساس فناوری پیشرفته هوش مصنوعی ساخته شده، خلاقیت و سرگرمی بی‌حد و حصر را به حساب کاربری توییتر شما اضافه میکند.
https://tweethunter.io/generate-tweets
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6694" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBHLB5ohOve--EHItpnKMU3baSI0h9Vglidvwxg_kNdjlOFNvgJYpM0SgNmLqvdKA_cabcYhLGvWd41v4DbQacxX2gDK4oJ77PW7BkZbqoFgQuO6QIkIA-JCXK9JZxT9IroyR0EPuwgPvHIjlKqxUtirEDoOic5juYxWCBUgdgaaGcI0zOkZuEGUF8uKv8B5SE67hWdpG0bDdJ9WBxutRslY5IUIK2WdZD4jqltr5Cab2Z_nqmoRNaONHbyWNp7nsDogaqWxg9XPIV37tmBTF7NfsbAkPPl6bkisoK0ZGFX6e-ZXvWiECwwQlL-6OMDlYoIVxH4QCxhQ65xyXxWUJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک مجموعه‌ای رایگان از پرامپت ها برای Claude ارائه می‌دهد
🤩
این مجموعه شامل ده‌ها راهکار آماده برای بررسی امنیت، رفع اشکال و بازبینی کد، خودکارسازی وظایف و موارد دیگر است. برای هر پرامپت، توضیحات مربوط به نحوه عملکرد آن ارائه شده است.
https://code.claude.com/docs/en/prompt-library
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6693" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpMJiSe8IXpO6Sz81DxGmD1UAb4uVL90thR1DeHXpeU0PPMZX03VK2cbcBTa-YqnKQBwYzCwKCu-RFm4CZj_ByahWIHgeckPjtFHVDaOYYknbz9nU1G1bSlm8YY6cIfXZdbs_6F1hWIrA6LkdTXQ6aPv1ei0DDDRKqUFAPcWsGqu2LoBxIxliwGnkOsUJuTqr7m-13iqrkF1f7NWhOen2z4e69As9t0o9lIPCa--z7PeW5CE6WurooIK3BlwUF2kmLpOq0_Sg_057kdLHtVsC4s9NR0agregFl_V9OaU9tiyaAX5hOmym-8U6eZARSQYrG1MD3i403O8ASUhyasW9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فتوشاپ را فراموش کنید
🤯
یک ابزار مبتنی بر هوش مصنوعی می‌تواند تمام وظایف را با دستورات متنی انجام دهد و برای این کار نیازی به مهارت‌های طراحی یا دانش فنی نیست.
🎨
✨
🔹
همه چیز بسیار ساده است: یک عکس یا تصویر را آپلود می‌کنید، پس‌زمینه را تغییر می‌دهید، اشیاء اضافی را حذف می‌کنید، رتوش انجام می‌دهید، کیفیت را بهبود می‌بخشید و از ده ها امکان دیگر استفاده می‌کنید.
🖼️
🛠️
🔹
بدون ثبت‌نام و مستقیماً در مرورگر
🌐
🔹
کاملاً رایگان
🆓
https://ezmaker.ai/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6692" target="_blank">📅 14:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏
🎁
500 کریدیت رایگان ‌Opus 4.8⁩ و Fable 5 هدیه بگیرید!
‏دنبال دسترسی رایگان به قدرتمندترین مدل‌های هوش مصنوعی می‌گردید؟ با این روش ساده، ماهانه ۵۰۰ کریدیت رایگان دریافت کنید.
🚀
‏
1⃣
وارد سایت زیر شوید:
🔗
‌www.relay.app
⁩
2⃣
‏ ثبت‌نام کنید:
‏با اکانت
گوگل
یا
مایکروسافت
خود وارد شوید.
3⃣
انتخاب مدل:
اگر روی آیکون پروفایل خود کلیک کنید و وارد تنظیمات شوید
در بخش اکانت ، اولین گزینه را بزنید و select model را انتخاب کنید و مدل مورد نظر خود را انتخاب کنید
4⃣
لذت ببرید:
‏از امکانات پیشرفته و کریدیت‌های رایگان ماهانه استفاده کنید.
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/6691" target="_blank">📅 23:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🧠
یک سرویس جدید که قادر است مدل‌های سه بعدی را به کتاب‌های آموزشی تعاملی تبدیل کند!
📚
✨
هر مدل سه بعدی را بارگذاری کنید، سیستم به طور دقیق ساختار آن را تجزیه و تحلیل می‌کند: عملکرد هر قطعه را توضیح می‌دهد و نحوه کارکرد آن را نشان می‌دهد. در پایان، یک آزمون کوتاه برای ارزیابی دانش شما ارائه می‌شود.
🧪
🔧
برای آشنایی اولیه با قابلیت‌های این سرویس، مدل‌های آماده‌ای در زمینه‌های پزشکی، مهندسی و علوم طبیعی در دسترس هستند.
🏥
🏗
🌿
https://atlas3d.space/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6690" target="_blank">📅 23:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0677cd71ec.mp4?token=li8NxdhKlDNRpiZtRpJBukdfIxHVCb-7ty4jKukeCFwW22GdxsO911GjTJT3Bk_yqSDmcMGajTBnMTesFosuTJwQStVbJnnoZ2e3RpaVCunDMIh65UxlPHfnSlgByMsH_4nwfz3GrcEssAo8PUqlFpyZV57PU0kb54PbpcqfnfofcC58Y9Nx9Im38elrCvy8gKynldvuisCZBsdmPXMUsx_VzmCYwOeAfpZ_umnAR41bWoBB3aj6UIwN8DXxpGpBF2WIXWpIBbX1J2Lh8VFkpyZwEKJ57i64l3hMwWzkj8TaEXGDNDRE0-GCLHcwh7Q1e2300B51Mi3ENg7PSFrRtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0677cd71ec.mp4?token=li8NxdhKlDNRpiZtRpJBukdfIxHVCb-7ty4jKukeCFwW22GdxsO911GjTJT3Bk_yqSDmcMGajTBnMTesFosuTJwQStVbJnnoZ2e3RpaVCunDMIh65UxlPHfnSlgByMsH_4nwfz3GrcEssAo8PUqlFpyZV57PU0kb54PbpcqfnfofcC58Y9Nx9Im38elrCvy8gKynldvuisCZBsdmPXMUsx_VzmCYwOeAfpZ_umnAR41bWoBB3aj6UIwN8DXxpGpBF2WIXWpIBbX1J2Lh8VFkpyZwEKJ57i64l3hMwWzkj8TaEXGDNDRE0-GCLHcwh7Q1e2300B51Mi3ENg7PSFrRtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
😂
سووو رونالدو با رینگتون های مختلف
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6689" target="_blank">📅 23:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آموزش‌ گرفتن Fable 5 به صورت رایگان تا 1 ماه هر هفته 70 دلار
💰
برید توی
Aerolink
و ثبت نام کنید
📝
لینک ثبت نام
🔗
نحوه ثبت نامش دقیقا مثل
freemodel
هست طبق این
پست
📄
نحوه اجراش روی
claude code
هم همونه فقط این تنظیمات رو بزنید جای اون
⚙️
{
"env": {
"ANTHROPIC_API_KEY": "کلیدت",
"ANTHROPIC_BASE_URL": "https://capi.aerolink.lat/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلیدت'"
}
هر ورژنی از claude code هم بزنید قبوله
✅
لیمیتش هم دقیقا مثل
freemodel
هست
🔒
موقع اجرای claude code بجای دستور claude این دستور رو بزنید
👇
claude --model claude-fable-5[1m]
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/6688" target="_blank">📅 22:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚀
معرفی Qwen Gate؛ دسترسی رایگان به API مدل قدرتمند Qwen 3.7-Max!
🤖
✨
مدل Qwen 3.7-Max در حال حاضر یکی از بهترین مدل‌های هوش مصنوعی است، اما استفاده از API رسمی آن هزینه دارد. ابزار متن‌باز Qwen Gate نسخه وب (
chat.qwen.ai
) را به یک API کاملاً سازگار با استاندارد OpenAI تبدیل می‌کند تا بتوانید به صورت کاملاً رایگان و لوکال از آن در پروژه‌هایتان استفاده کنید!
🔥
ویژگی‌ها و قابلیت‌های این ابزار:
1️⃣
سازگاری گسترده:
قابلیت اتصال بی‌دردسر به دستیارهای برنامه‌نویسی مثل Cursor, Claude Code, Continue و سایر کلاینت‌های مبتنی بر OpenAI.
2️⃣
چرخش اکانت (Multi-account rotation):
پشتیبانی از مدیریت و چرخش بیش از ۳ حساب کاربری برای جلوگیری از محدودیت‌ها.
3️⃣
امکانات کامل:
پشتیبانی از فراخوانی ابزارها (Tool calling)، استریمینگ سریع و دارای یک داشبورد حرفه‌ای برای گزارش‌گیری.
4️⃣
پشتیبانی از مدل‌های مختلف:
دسترسی به Qwen 3.7-Max, 3-Max, 3-Plus و سایر نسخه‌ها.
💻
نصب و راه‌اندازی سریع:
برای نصب کافیست دستور زیر را در ترمینال اجرا کنید:
Bash
curl -sSL https://raw.githubusercontent.com/youssefvdel/opengate/main/install.sh | bash cd opengate && qg
پس از اجرا، آدرس
http://localhost:26405/dashboard
را در مرورگر باز کرده و اکانت Qwen خود را اضافه کنید. حالا می‌توانید از آدرس http://localhost:26405/v1 به عنوان Endpoint (درگاه API) در نرم‌افزارهای خود استفاده کنید.
⚠️
توجه بسیار مهم:
از آنجا که این ابزار بر پایه اتوماسیونِ رابط کاربری وب کار می‌کند، احتمال مسدود شدن اکانت توسط سیستم‌های امنیتی وجود دارد.
حتماً از اکانت‌های فرعی و تستی استفاده کنید
و به هیچ وجه حساب اصلی خود را متصل نکنید.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6687" target="_blank">📅 21:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚀
ساخت بی‌نهایت اکانت معتبر با یک Gmail!
📧
✨
سایت‌های حساس (مثل صرافی‌ها، ChatGPT یا AWS) ایمیل‌های فیک را مسدود می‌کنند. اما با ترفند پنهان «پلاس» (+) می‌توانید بدون نیاز به شماره موبایل، بی‌نهایت ایمیل معتبر (برای دریافت اکانت‌های تریال) بسازید!
🔥
این ترفند چطور کار می‌کند؟
قانون جیمیل این است: هر عبارتی که بعد از علامت + (و قبل از @) بیاید، نادیده گرفته می‌شود.
مثلاً اگر ایمیل اصلی شما ArchiveTell@gmail.com باشد، می‌توانید با این آدرس‌ها در سایت‌های مختلف ثبت‌نام کنید:
ArchiveTell+twitter@gmail.com
ArchiveTell+vpn123@gmail.com
از نظر سایت‌ها، این‌ها ایمیل‌هایی کاملاً متفاوت هستند، اما تمام کدهای تایید مستقیماً به
اینباکس همان ایمیل اصلی شما
ارسال می‌شوند!
🛠
ابزار کمکی:
برای ساخت خودکار هزاران آدرس مشابه، می‌توانید از ابزارهای آنلاین
Gmail Generator
استفاده کنید.
🔵
@ArchiveTell
| Bachelor
⚡️
#آموزش
#ترفند_جیمیل</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6686" target="_blank">📅 20:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65311253ad.mp4?token=p8vadFK7R14QFQfMqqBKwiF_orRZ-ferjyld56tYmVnVBzhoXnPFTvz2SoSlKfEZnbCofcdp2Q1NakztwVfdp02n-xWdtqvMPPB5QPz4lvydMz9Jj-HomzyFNEnpOx-o7P4xqXGFg0_q_5DhW35tNKUKiSS_eHFHGiNiDrhZ9UeOw0QHY09ZbKSPuD5nLzRDGfPtMd7Aw7jNfvGRNI36SJb3xu2GLLSYODlvbiZqJ_LPuCqYR1a-Ph4XJK7Yd7HpAFc1pfbDjGKuf046tM3DCnw1DcWdU7TrJ792sAXSDLqQXsllGfh7DowEoRev4SGLlNCU-EXvXuvg9O2bhSgMaZnq72f5HK8XzCDedVXidXXY63D-yRO4IveQpawgSqHzUagOhRJThkBy33v1fB3Z7TkB3agHo3yRqTb0xORQHbX9W4hWpCDV4Y-RrGWU4_RBcph4cQrH7driayakTZyLN29Nf2BiBrLhPqZeJjr_FTrcGaH9bPolhS3xzNTxiyUnDF4ASzzsA4Lx1qneX1YY4m3lulkCYrTM6j6x-rx6qRkQyDQFPwa6QxkEW8oCmWbg2yBle7A5RGfrBedcwO0eiWYJgekDAzuBx_DH5P8pw_4kVdU9MT_OA0IUrLN-jkCM3ViHFymfhtL3oMKWXlnG4j3WrCimemIVIeBiZRGUDo8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65311253ad.mp4?token=p8vadFK7R14QFQfMqqBKwiF_orRZ-ferjyld56tYmVnVBzhoXnPFTvz2SoSlKfEZnbCofcdp2Q1NakztwVfdp02n-xWdtqvMPPB5QPz4lvydMz9Jj-HomzyFNEnpOx-o7P4xqXGFg0_q_5DhW35tNKUKiSS_eHFHGiNiDrhZ9UeOw0QHY09ZbKSPuD5nLzRDGfPtMd7Aw7jNfvGRNI36SJb3xu2GLLSYODlvbiZqJ_LPuCqYR1a-Ph4XJK7Yd7HpAFc1pfbDjGKuf046tM3DCnw1DcWdU7TrJ792sAXSDLqQXsllGfh7DowEoRev4SGLlNCU-EXvXuvg9O2bhSgMaZnq72f5HK8XzCDedVXidXXY63D-yRO4IveQpawgSqHzUagOhRJThkBy33v1fB3Z7TkB3agHo3yRqTb0xORQHbX9W4hWpCDV4Y-RrGWU4_RBcph4cQrH7driayakTZyLN29Nf2BiBrLhPqZeJjr_FTrcGaH9bPolhS3xzNTxiyUnDF4ASzzsA4Lx1qneX1YY4m3lulkCYrTM6j6x-rx6qRkQyDQFPwa6QxkEW8oCmWbg2yBle7A5RGfrBedcwO0eiWYJgekDAzuBx_DH5P8pw_4kVdU9MT_OA0IUrLN-jkCM3ViHFymfhtL3oMKWXlnG4j3WrCimemIVIeBiZRGUDo8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبیه‌ساز هاگوارتز ( مدرسه جادوگری سری داستان‌های هری پاتر ) از ‌Fable 5⁩
در این قلعه افسانه‌ای می‌توانید درس بخوانید و با جارو پرواز کنید.
🧙‍♂️
‏این شبیه‌ساز مستقیماً در مرورگر اجرا می‌شود.
https://hogwarts-production.up.railway.app/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/6685" target="_blank">📅 20:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ظاهرا کلودفلر اعصابش از ایرانیا **ری شده و از این به بعد دیگه ایمیل فیک قبول نمیکنه اگرم بکنه تایید نمیتونین کنین اگرم بتونین تایید کنین بنتون میکنه
😍
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/6684" target="_blank">📅 18:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ArchiveTel
pinned «
دریافت 2 دامنه رایگان بدون احراز هویت و شماره و ...  https://youtu.be/1yzxi-U_vVo
🔵
@ArchiveTell
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6683" target="_blank">📅 18:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🛡
آیا وای‌فایِ شما واقعاً امن است؟ (یک تستِ ساده و حیاتی)
خیلیا فکر می‌کنن چون روی وای‌فای‌شون پسورد گذاشتن، امنیتشون کامله. اما حقیقت اینه که اگر پسورد شما ضعیف باشه، نفوذ به شبکه و شنودِ ترافیکِ شما برای یک فردِ آشنا به تکنیک‌های ساده، کمتر از ۱۰ دقیقه زمان می‌بره.
⚠️
چطور تست کنیم؟
در دنیای امنیت، ما از روشی به اسم «Capture Handshake» استفاده می‌کنیم. وقتی یک دستگاه به مودم وصل می‌شه، یک تبادلِ اطلاعات (Handshake) بین اون دستگاه و مودم انجام می‌شه. اگر کسی این تبادل رو ضبط کنه، می‌تونه آفلاین و بدونِ اتصال به مودمِ شما، اونقدر رمز عبور رو حدس بزنه تا بالاخره یکی درست دربیاد!
💡
چطور نفوذناپذیر شویم؟ (اقدامات فوری)
۱.
پسوردِ قوی انتخاب کنید:
رمز عبور باید حداقل ۱۶ کاراکتر شاملِ (ترکیبِ حروفِ بزرگ/کوچک، اعداد و کاراکترهای خاص) باشه. رمزهای ساده مثل شماره تلفن یا کلماتِ دیکشنری، در لیست‌هایِ هکِ «آفلاین» در عرض چند ثانیه شکسته می‌شن.
۲.
غیرفعال‌سازی WPS:
این قابلیت که اجازه می‌ده با فشار دادنِ یک دکمه روی مودم وصل بشید، یک درِ پشتی (Backdoor) خطرناکه. حتماً وارد تنظیماتِ مودم بشید و
WPS رو کاملاً Disable کنید.
۳.
ارتقا به پروتکل WPA3:
اگر مودمِ شما از WPA3 پشتیبانی می‌کنه، حتماً تنظیماتِ امنیتِ وای‌فای رو روی این گزینه بذارید. WPA3 به شکلی طراحی شده که اصلاً Handshake به روشِ قدیمی تولید نمی‌کنه و عملاً در برابر این حملات ایمنه.
۴.
تغییرِ دوره‌ایِ رمز عبور:
حتی اگر رمزِ پیچیده‌ای دارید، هر چند وقت یک‌بار اون رو تغییر بدید تا اگر کسی قبلاً در حالِ شنودِ ترافیکِ شما بوده، دسترسی‌اش قطع بشه.
این پست رو برای کسانی که هنوز رمزِ وای‌فای‌شون ضعیفه، فوروارد کنید!
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/6682" target="_blank">📅 13:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjQa6qOSiV_84lXCBcSjQuPvtzF5qFQtPYBck3Qis-ZbDBnzvQPdunLg1c31i2Hm7hHSvwEWWwjGiHWo0VO96puiAkArxrhQ4hVRVnRNPSZ3hoSrCCiq2Kz1BdM51RUjDNeFxAcjvn9eaqVfYFgWau9T1Ug39BwMz595nG7sX_F-BObi7hQ6GyNSZqyHbo26OQ1szVEpScAnw_mn3XOIDYiE6TgQ-sP_88Y2i1Qy8SueYUvypZcKAoZZE2TSbe_z0kJhZWRusOjTvC_tGzOHuzHzU8cFk_Yi4aacWODntZ1oly9pb2gdssAIWgPXv4R3cczvXz5uEAZ1LgSLrqA2bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/6680" target="_blank">📅 09:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است. با اجرای این ترفند، می‌توانید نسخه گران‌قیمت Ultimate را به راحتی فعال کنید!
🔥
آموزش قدم‌به‌قدم فعال‌سازی:
1️⃣
ثبت‌نام:
به سایت
gitlab.com
مراجعه کنید و با یک حساب گوگل جدید یا یک ایمیل معمولی اکانت بسازید.
2️⃣
تعیین نقش (مرحله حیاتی):
در بخش تنظیمات و شخصی‌سازی پروفایل، نقش خود را حتماً به عنوان
مدیر سیستم (System Administrator)
انتخاب کنید.
3️⃣
انتخاب نوع کاربری:
زمانی که پرسیده شد چه کسی از این فضا استفاده خواهد کرد، به جای گزینه «فقط من»، حتماً
«تیم من» (My team)
را انتخاب کنید.
4️⃣
تکمیل مشخصات:
کادرهای مربوط به نام شرکت، پروژه و گروه را پر کنید. (اگر با خطای «مسیر گرفته شده است / Path taken» مواجه شدید، کافیست چند عدد تصادفی به انتهای نام گروه خود اضافه کنید).
5️⃣
فعال‌سازی نهایی:
روی گزینه «ادامه به GitLab» کلیک کنید تا لایسنس آزمایشی ۳۰ روزه Ultimate شما فوراً فعال شود.
⚠️
نکته بسیار مهم برای جلوگیری از خطای دسترسی (Permissions):
وقتی وارد داشبورد شدید، به هیچ وجه چت هوش مصنوعی را مستقیماً از صفحه اصلی (عمومی) باز
نکنید
. ابتدا وارد داشبورد خود شوید، روی صفحه گروه یا پروژه‌ای که ایجاد کرده‌اید کلیک کنید و سپس از آنجا روی آیکون چت
GitLab Duo
ضربه بزنید.
در نهایت، از منوی کشویی انتخاب مدل،
Claude Fable 5
را انتخاب کنید و از دستیار برنامه‌نویسی حرفه‌ای خود لذت ببرید!
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/ArchiveTell/6679" target="_blank">📅 09:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دریافت 2 دامنه رایگان بدون احراز هویت و شماره و ...
https://youtu.be/1yzxi-U_vVo
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/6678" target="_blank">📅 02:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTu6aCQ1h3CMziiBWK1A_93z5xVPkbU30fP90P6OHMAkhVLhFuISVPzSfeJc3zFZ3mmauavnHPeFEGQ5anJ2jlwqEi9QeCyXi4K69Pqfjo0NXuLZsXo4sNfJ6f9IGBTxDx1w3WejTyctOxeB8yGmoB3LyLboWB31k_9t57VfFzkmc_-KBFzmopH9sDUP20AyEvDMYFqx2G8u65GfLjvadt2y3o7_Os9bLPnYJWwoyClXOwFtg__iXnXsjydHBDuQio8lyA5sHdd0nuaQ8FjsGhow7n_DOcBOX3BN2ea0aPeZusS_Be3rCkD-efihsgTKg0Rxv_KBug2c-Su96Wo3Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توسعه‌دهندگان چینی GLM ابزار قدرتمند ZCode 3.0 را معرفی کردند
😮
این یک ابزار همه‌کاره برای نوشتن کد و تعامل با عوامل هوش مصنوعی است: همه چیز در یک پنجره جمع شده با امکان کنترل از راه دور از طریق تلگرام.
این سرویس به صورت رایگان در دسترس است.
http://zcode.z.ai/en
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/6677" target="_blank">📅 01:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mccgoxO5o2XhEd0bDUIYlHDw3Mk2JMFDfXI7cvxNyaFf5ry4_LvEvkpfJaFwNprey7WY06SawdvMa5wRmw8U-6_dpckey_XVcDq1crQFaJhoUk6N-2jqwYSPUguqiPS1rtfDso5jNS0yNVlb09MyNEePgUQLxq9m6TERvDX3FJfCzAgTa7P8V2QkLZHBZpmblp9-miRxAzQoVcfYJqgNANlzhpUGGikv-jViLVHldpHLRDGHubAJ0bwuJlNhEzb5ar_I81zfehIWg1jzuRoBvznr6HpCb71tL9UCJ8s8_JV0PpDEm7BWrs5PpIcmEs0shThmiLuE4rmt0AquO7WodA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت Fable 5
🔥
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/6676" target="_blank">📅 23:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=fESE00BrJ2gqTPWS7ScdXW5eQ-m2NADF2tdusIJ5vJrb4rULsU3wl9wWbBKG3sruZ7zjysrZsw9l9Y6zEqR-HHUblLjeQoHppQdbvoQfiKWtk-9xrU2dMCnsO4FeF4vwq0VvlJjeskCgHBMybXws4_SBHkO9rX3ahswuFgTE79loyNeyydPrBxcoq9Ez_dX4NF6Tks27jcc0zxQWPXL94YJecdga9yWS4C1xCvpoAfXvtjuz3hAyfLh853zYMFrlP6wyjN5gId5nuUmcY3aQg91jy2_DvitOptOky0-5K6RK0gy7nTm9Qduwvquakow27zqLa1FlIlqAPRjkJEgyF1SDKZyme0XKhn_fgdS6N9fcOgYzp95SR1CmE1ep1yBHtef54XnriFc2HzzDJqIvs9bYPcf2-OzxhVG4jhMCe51HRF_L7rx_FjaasSCK0hmfvkILgm-ecPT-Em7-bPJzvehgZgWGtLuk0maZRkVtguSXYOt7qgXJfAunwnPWTL2AfDPtNgJrpuNGTQWzBGiistJYhfQo1BqusSQgQEjrO0H5GH1R0eFBr7FNveEvIvxc3YUeQLkeBxdkc0zOmTjaQ0GFbIX1241HU7wOcX0zMsQvBnWWVOQmUCl1DXDAFb8b1PjvwFXqVMh-XA3no__t6LykLJqhz3AfUOb_7-p_nMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=fESE00BrJ2gqTPWS7ScdXW5eQ-m2NADF2tdusIJ5vJrb4rULsU3wl9wWbBKG3sruZ7zjysrZsw9l9Y6zEqR-HHUblLjeQoHppQdbvoQfiKWtk-9xrU2dMCnsO4FeF4vwq0VvlJjeskCgHBMybXws4_SBHkO9rX3ahswuFgTE79loyNeyydPrBxcoq9Ez_dX4NF6Tks27jcc0zxQWPXL94YJecdga9yWS4C1xCvpoAfXvtjuz3hAyfLh853zYMFrlP6wyjN5gId5nuUmcY3aQg91jy2_DvitOptOky0-5K6RK0gy7nTm9Qduwvquakow27zqLa1FlIlqAPRjkJEgyF1SDKZyme0XKhn_fgdS6N9fcOgYzp95SR1CmE1ep1yBHtef54XnriFc2HzzDJqIvs9bYPcf2-OzxhVG4jhMCe51HRF_L7rx_FjaasSCK0hmfvkILgm-ecPT-Em7-bPJzvehgZgWGtLuk0maZRkVtguSXYOt7qgXJfAunwnPWTL2AfDPtNgJrpuNGTQWzBGiistJYhfQo1BqusSQgQEjrO0H5GH1R0eFBr7FNveEvIvxc3YUeQLkeBxdkc0zOmTjaQ0GFbIX1241HU7wOcX0zMsQvBnWWVOQmUCl1DXDAFb8b1PjvwFXqVMh-XA3no__t6LykLJqhz3AfUOb_7-p_nMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
واقع‌گرایی GTA 6 شگفت‌انگیز است: یک علاقه‌مند صحنه‌هایی از تریلر رسمی بازی را در دنیای واقعی بازسازی کرد.
بعضی از صحنه‌ها عملاً از نسخه‌های اصلی بازی قابل تشخیص نیستند
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/6674" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAI3FrZrDHj1EMNIP0uEbj8Xtf31_Xq4S-YU7X-zUZyF1A3RtPI68XbLIwy7zpXhOFOUDdLfTf-xNC2L6QOOhMzqd3fX9QdFzA0SxHJRVOJQn_o0NEnBTduNUhbjRBRCgZfvSu8siZqGyQiUIAf3Thhim50H3DLy_hQK-iG9eFwkOguXJ1lNzLDHs72gkOywBu1glr_5PlwhfhxH1Uwf_FH7tHxtkUT8X8ChOQWcOCPk7qaFWGRzn2EZZt1BS3LwxWzZ2yzq387PCMOsfczpi_zREap0D5HDHhcQ3xBTZm0yEoDqjSvdlB4-nM4Ndl-HOVlAEcTHcSAcvWw8Dp9DrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون هوش مصنوعی مهارت خودآموزی (self-learning) را به دست می‌آورد — عامل یک راه‌حل پیدا شده را به خاطر می‌سپارد تا در هر جلسه جدید دوباره آن را جستجو نکند.
🧠
وقتی هوش مصنوعی با یک مسئله مواجه می‌شود، این روش را ثبت می‌کند و علامت می‌زند که دقیقاً چه چیزی کار کرده است. دفعه بعد سیستم مسیر اثبات شده را دنبال می‌کند، به جای اینکه دوباره گزینه‌های ناکارآمد را بررسی کند.
https://github.com/Kulaxyz/self-learning-skills
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/6673" target="_blank">📅 18:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6672">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOBuyU6W3khEbMCxD55Mtw7DYNDgMj_ugwdteVkvK12OvpO2RlfP-eHp0Mq2RE29tf7Bt7NKow6gPShzsM_gdJ4yMPHlzl6Rb76OakYqwmgnMgDuiUN_B78nETdryBKdPFCnZt87vo5RQburK-j1E4s88ITa6FmndXoBGRyfquKQmMz8HA_LAPFQ_wRc9M9OAs7cPB3j_P964xpjUF20_uZFW4r2jbr1wcI-XPrtMh_5fj6AzhSH0NNHMj9Qg4pm-1__bBrQBcLf-chcojLV9WNMucZ_DtIwv2whPl3IVeYG6PtOw3jIYM6Hq3aGAqRl1XNOZBhMJBAl4dEGJJRhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">RevPDF
ویرایشگر PDF سریع، بومی و متمرکز بر حفظ حریم خصوصی به صورت آفلاین است.
این برنامه امکان ویرایش متن و تصاویر را مستقیماً در سند PDF فراهم می‌کند و همچنین عملیات‌هایی مانند ادغام، تقسیم، فشرده‌سازی و تبدیل فایل‌ها را انجام می‌دهد.
تمامی عملکردها به صورت محلی روی دستگاه اجرا می‌شوند و حریم خصوصی کامل داده‌ها را بدون نیاز به اتصال به اینترنت تضمین می‌کنند.
https://github.com/Pawandeep-prog/revpdf-release
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6672" target="_blank">📅 18:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6671">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1d8b6548.mp4?token=HHBXc9IhI8V1nlxP01C6Huzl6i-sk2RKrFQPMoKgVognRjOU0_Iomqn2vzfVcB2T-QAXrfn3bQTHnrZpUBNI_hbgL7wzv9ldSKEQc9Lsrp0hT5QYeAV7T5PNaNHXo-2CgRtPjQxWykWKtJCfxm2ZOK74PKwLk8xJhlTuzWqHiGXcZa-8bKtiFFOALv_NOIlnfGIvmCrdYD33d1CotlFi9198TZI5mDEi1Ovzc9LPHE5XVMZBWJBVQ_mv_3dQdSq6Nrvsph9B5rOv7cMz8rXPNbObsADCJV1BvnW4vEwBDMGYyb_D__r42_tlnjEuYMxTSzX5JjtNqZ3kFnTznMQyokZCSMpReCy-cNp52155O78ZNSt10MEb9R__naOvUky9mTlrxn5xH6vGME96sbbp-rWgRKQ-8hJxx0ZPx3wewih9oFCGRDx-Hi6qcWYzSx3FZoSAibITtKxXf5r3UuvqWG_y3paqDAU7Xfk5NXBXfJBWazX4d4Lb60mZ2AGzc56VWRktA4UBqkkolDkV0uf5i__f9RXQAsKGOuRA4M5h3gJtE1lxJnQvK_VKeScf0Ik1sleeemqR45XtB7v8y9TO7La_LymXF1TnjI0zLB5su0jDy-E8o9lnWu6Ah2fCg6FT8IKF6wwMpdarYNgeskzGdwrZI37qf0SSB7gEmaJntLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1d8b6548.mp4?token=HHBXc9IhI8V1nlxP01C6Huzl6i-sk2RKrFQPMoKgVognRjOU0_Iomqn2vzfVcB2T-QAXrfn3bQTHnrZpUBNI_hbgL7wzv9ldSKEQc9Lsrp0hT5QYeAV7T5PNaNHXo-2CgRtPjQxWykWKtJCfxm2ZOK74PKwLk8xJhlTuzWqHiGXcZa-8bKtiFFOALv_NOIlnfGIvmCrdYD33d1CotlFi9198TZI5mDEi1Ovzc9LPHE5XVMZBWJBVQ_mv_3dQdSq6Nrvsph9B5rOv7cMz8rXPNbObsADCJV1BvnW4vEwBDMGYyb_D__r42_tlnjEuYMxTSzX5JjtNqZ3kFnTznMQyokZCSMpReCy-cNp52155O78ZNSt10MEb9R__naOvUky9mTlrxn5xH6vGME96sbbp-rWgRKQ-8hJxx0ZPx3wewih9oFCGRDx-Hi6qcWYzSx3FZoSAibITtKxXf5r3UuvqWG_y3paqDAU7Xfk5NXBXfJBWazX4d4Lb60mZ2AGzc56VWRktA4UBqkkolDkV0uf5i__f9RXQAsKGOuRA4M5h3gJtE1lxJnQvK_VKeScf0Ik1sleeemqR45XtB7v8y9TO7La_LymXF1TnjI0zLB5su0jDy-E8o9lnWu6Ah2fCg6FT8IKF6wwMpdarYNgeskzGdwrZI37qf0SSB7gEmaJntLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
«اودیسه» نولان - تریلر نهایی. این فیلم یکی از بزرگترین آثار چند سال اخیر خواهد بود.
با بازی ستارگان: مت دیمون، تام هالند، ان هتاوی، رابرت پتینسون، لوپیتا نیونگو، زندایا و شارلیز ترون.
اکران: 17 جولای.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6671" target="_blank">📅 18:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjbO5dPJHneJeBmOyS9h1sROp9h7bJbmUreLDYWfHFaDf1Ip3blPAPbU9eHA7QefA4iVvCswI8LGVdomBEFgyrkY18DUzKpwKyQf7RA891MxbjG3FcWiEFWpB03QWu8jH3p-nJPrJGg9rn9RRfzyp4ostcGRLb6HzNNOiyW4khalIuOYZmRgK_PzotZRuY09wFW7YLVIFDYCuieax4NTixZAHmyLIpgN5j4I4LxVKJyzPSKb8sE8OToF5Dp7faciwipAAmyRtZwuJpQwPrVEgHdWvjAwy2vRd3ap-4TlcmupHyjFfJD811C-A0hUPITurBfLYR6W1ySB3hhX1UHPJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض چند ثانیه هر نوع کپچا را در سایت‌ها و منابع دیگر رد می‌کنیم
• به سرعت بیش از ۳۰ نوع کپچا را حل می‌کند، رفتار انسان را تقلید می‌کند تا هر محدودیتی را دور بزند.
• با چند کلیک روی کامپیوتر نصب می‌شود، نیازی به ثبت‌نام و نصب نرم‌افزار اضافی نیست.
• فوری و به صورت محلی کار می‌کند.
https://github.com/clawdbrunner/captcha-solver
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6670" target="_blank">📅 18:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268d269709.mp4?token=FqnWSz4HjxtPL2cTJt3Y7mhKmZ7FoFWubxNAFk7vkyWGQ8uMNO4Q92oxhYo5tPXdJzYoig-3V0CfGcdg_BzKFUMDM6hagl_fSThjivwF0oYXtwpisNDR3oxCL_8BLVpSP0uLKLYQKS0PZ-P-ePUU2EE9Y8kBNGaHQmcf6ncBgGtINBdADT5A-aEgRa5nQ0xv_ocqt5KZnOt8W8MTDuQcR1_JCF8lLdxUYdrfyjBNsAnqPmJ4pNhCV5p55UdKWcGYWGSoSYDS0cfCwSuGNbj2FVyir0sEjefOgLedSDOInKqhSAjy-ZpTDMFp9NoSLIEL-aaVMBzv5Q-zsAXnoq9Pgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268d269709.mp4?token=FqnWSz4HjxtPL2cTJt3Y7mhKmZ7FoFWubxNAFk7vkyWGQ8uMNO4Q92oxhYo5tPXdJzYoig-3V0CfGcdg_BzKFUMDM6hagl_fSThjivwF0oYXtwpisNDR3oxCL_8BLVpSP0uLKLYQKS0PZ-P-ePUU2EE9Y8kBNGaHQmcf6ncBgGtINBdADT5A-aEgRa5nQ0xv_ocqt5KZnOt8W8MTDuQcR1_JCF8lLdxUYdrfyjBNsAnqPmJ4pNhCV5p55UdKWcGYWGSoSYDS0cfCwSuGNbj2FVyir0sEjefOgLedSDOInKqhSAjy-ZpTDMFp9NoSLIEL-aaVMBzv5Q-zsAXnoq9Pgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
شبکه عصبی Gamma به ChatGPT اضافه شد — حالا می‌توانید پرزنتیشن‌های زیبا را مستقیماً در چت بسازید.
ابزار هوش مصنوعی محبوبی که صدها هزار نفر در سراسر جهان از آن استفاده می‌کنند، در ChatGPT ادغام شده است. حالا کافی است ایده خود را توصیف کنید یا متن را وارد کنید، شبکه عصبی آن را به یک پرزنتیشن آماده با اسلایدهای طراحی شده تبدیل می‌کند.
می‌توانید تا ۱۰ اسلاید را به صورت رایگان تولید کنید.
🔗
لینک
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6669" target="_blank">📅 17:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCZ5Ypg7diYCXhKroAqMgjw5BbPCVy3a4RDsGh8tb96_ORovbMzFz1G6s1Q_H-ykX_HNYtSrksSiJ7a1RLZNQJUaQcuDHWEaMcmkWjMlWbMn17G7KqGfy5GZ4kVK-z65TudQPr-poQItblQfCVU_CHrI4_wsr9H7pA0JQAcBe2a15HCocXboB_0uBD8T_7ZHu43bN6nF4cWrsSAyidRqnVON7ugWwG8Mqx0k_N6J1YQzyge2ull0J6H7VblHqD0OuHs8ZnwGf6TlMX70E9EKNk8VCPQaVtjZTP4GGtLM6PbY2CkKZ3NuQgYzYyQSV0uBHdO1G_MIRT8pZYLDpjfjlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دیسک‌های بازی پلی‌استیشن سال ۲۰۲۸ ناپدید خواهند شد
بازی‌های جدید فقط به صورت دیجیتال منتشر خواهند شد. همچنین سونی فروشگاه PS Store برای PS3 و PS Vita را خواهد بست.
یک عصر به پایان رسید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6667" target="_blank">📅 17:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚀
معرفی Superfile؛ فایل منیجر مدرن و فوق‌سریع برای محیط ترمینال!
📁
✨
اگر از طرفداران محیط خط فرمان (ترمینال) هستید و به یک مدیر فایل قدرتمند، زیبا و سریع نیاز دارید، ابزار
Superfile
دقیقاً برای شما ساخته شده است. این ابزار با رابط کاربری بصری (Intuitive) و کنترل آسان از طریق کلیدهای میانبر، تجربه مدیریت فایل‌ها در ترمینال را به سطح کاملاً جدیدی می‌برد.
🔥
ویژگی‌ها و امکانات برجسته این ابزار:
1️⃣
پشتیبانی کراس‌پلتفرم (Cross-platform):
اجرای بی‌نقص روی تمامی سیستم‌عامل‌های دسکتاپ از جمله لینوکس، ویندوز و macOS.
2️⃣
شخصی‌سازی بی‌نهایت:
دارای سیستم پیشرفته برای نصب پلاگین‌ها و تم‌های متنوع جهت تغییر ظاهر و افزودن قابلیت‌های جدید به محیط برنامه.
3️⃣
نصب سریع و بی‌دردسر:
قابلیت نصب تنها با یک دستور ساده از طریق پکیج‌منیجرهای معروف مانند curl، winget، scoop یا Homebrew.
4️⃣
محبوبیت و پایداری بالا:
توسعه‌یافته با زبان قدرتمند
Go
که توانسته بیش از ۱۷.۷ هزار ستاره (Star) در گیت‌هاب به دست آورد و نشان‌دهنده استقبال بی‌نظیر توسعه‌دهندگان از آن است.
https://github.com/yorukot/superfile</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6665" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIV1p8nYG4ZK4zZ-MYRS3UfVrobJugmU8VSl2_URHgPtIIirs_19-Uw2ZkUI9LlRrMM_L43sWmhhERD0H9tWRfF-d2xVMixBQqaw3LfqislWXT3ScyGd2QY_RixJNAXOB3IGpsSOdSiZ7QYVA_xuslQx5dr0-4xyJ6l4sO4h95pW4XLrZoDdhZDllr8_XWON2bKq0jvFQVrgu-uylT2kSoEaGIcLCl0BRf9GXhsuVO7ZPZsScto3d-OJkQEmolntrTUWH9sgjWLtSxO34MZpclVQdldpUUvbQN5A715msdyZPMnnA8iG-c31EDWmWTOlI-UqmwldNnOeOu9cgU56sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر اروین یالوم خودکشی کرده ظاهرا
😐
اروین یالوم نویسنده و تئوریسین روان درمانی اگزیستانسیال</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6664" target="_blank">📅 15:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jP2gowhTdE-hCUrwNHJWAv480hcJBp-bRQDf8cI8uTrFA0OawRZQsxzRMedhWoJ6ozDnfHHnPbv9TzDWPf-M8rimh2H_-af9mU7PBNxowGh-F2PEpYj_9evDfzTwYkSPc44G9saaAtNzsvrx7eYZVbdQtjiHYEOIKLCyJTvazRrs3W2_cPc12mfoea-pSH2j6r8mHQkwhnwJcSnDSfreBqvHEQ92N4iAkIP_2d4HYiaFe5QmOvqK17Dpkv6SssFdzthXO1tT0jXP7aNJJmYCVki0frgupLFLfYpbJOJo5syjxDWqaubCr6SYGD0SdyBGgNFQp-cTc73guKiSyQxO7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر سرویسی راه‌اندازی کرده است که پروژه را از نظر سئو، جستجوی هوش مصنوعی، احراز هویت ربات وب، MCP و پارامترهای دیگر بررسی می‌کند.
سپس به سایت امتیازی از ۰ تا ۱۰۰ داده می‌شود و یک پرامپت با اصلاحات ارائه می‌شود که می‌توان آن را به شبکه عصبی داد و سایت را بهبود داد تا امتیاز خود را افزایش دهد.
https://isitagentready.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/6663" target="_blank">📅 13:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EL5_cynaAqYLzCER1b2FkbQCEd4uXAgkXPe2s1cjXYll9dbaaMq_6TkehHMIvuO5bnWudj0fHpz5k2Sr9dGEf03uyEC9liT2QSG7u6tnmlKopXd7haCSOgyfmwyXQ2GYcMdkSEyJYD5Ak71Lke08cK1-GPM0zpONvjDfF_rXAMIDVZmNV1Z6H5ArvuiTm9Qrs06aqgN_IpuihWFOa9m6MTdcfnJuI7ANaAahkjbU7vhg6SFWaQSpI26rBpPKbJbU9iJF_X77f2xKhXYUaMWvqwwDagVNuc2U2MPvDGKkQjSixLnAMS-w7Oglqh8WpDTy7XElprlH4C59b6Mgl0oSzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع مفید برای توسعه‌دهندگان: در گیت‌هاب یک فهرست عظیم از APIهای رایگان برای همه موارد زندگی جمع‌آوری شده است.
🌐
بیش از ۵۰ دسته‌بندی موجود است: از آب و هوا، ارزهای دیجیتال و مالی گرفته تا یادگیری ماشین، نقشه‌ها، موسیقی، اخبار، انیمه و میم‌های بامزه با حیوانات.
🐱
💻
https://github.com/public-apis/public-apis
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6662" target="_blank">📅 13:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i8AOhgRhdugbz0mStBWdt9JeUm2PZhv3KucA_zuvibAJsD9jNOg3nmYf1clqnaWu230srU_kXULGAx-hgxDhXtcvHFEfSTjJiOjwTTU7mPB_Al4EOE6jD1tQGfUki_pwfr5mL5K1Su6sZILVv4BXj24CLRgTxKV28GDMriGTLOT4IitFHIsOGz1X4CMf0VfW-xw4Jd--K-z2jy0PpvA1TMdsaVePbLkgQey57YkfZPmygtEpYfaDF4gUvrcMQ73rO2juATSU744XjlA_gSzJK6ZeSrklyrvqS0YKE_E13lz8svi86iaubRPxG86PISGzDYArizH-d5SgRrtxJS2_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KDXi6xEKkUKkWDtQREnqkdX-VOse1Anrn0L1CREeqWjsT51QSn4Gj34Mo83LGccWysvftAP6kcDUr_07t-CA3z24rJ6x3YYwjyNJQ1vrBCKR_LFQlV88HLWG2t_95zj8xK25g9rWlKuQMFtiemARvgkiQ1FteXQ9LRsuRKFDBA3OWjMiOoOx-EJYKWPqg20O-3Hok7Yn2woXbUQmOkooTxfs5NdHOPBrFNCcWlH-DU4YldAyUKXvQM8APrAbvi1fS-BkdBeKHR9XR0njn4_tLHoHlkWaVa3mYT5QpOSlCoMh9smhsvDihJ1FArYic5iU6JzqeOOMNq-D3OrIy4VVSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ORxxZNxFMJ1BN2sHao55elgezU9e2JZquuhuypdpcCVuTFSJt7MQHlBt42bHkBXa-_ZEnK8Mplx6gUQh6CXSTtEX1jsNJfRIlxHquTtxGebxBMGINSlu7pdiUIYBHjXl5BnKNNzrp4Q9rj2whBcs_7_627nPQqJuQRU4UNSNXEqjERw4QNWrqSlyybsTuaJ3xUM7ZsgUrbnB18Vg4mJuiDF9wcM0iPcdCxW7vLYrk1M9_ZNDExVWc2cykXmOgdoYjO7O_BY5kFuX88t-EMwpgC682gZ9FoNQIFshm5mFKfW9JPMB9efZLrkenJt_PWuYEnN8NnVUbbK0EuXVusIOAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s86Lrddw2mVm_HU60g0jzQnlB_BovDYCUVMcmyIv9gWOBcVHlmJYTaHyGwaN1EFRa_Gj9srFxYa9bIGY89akRnlk-ZmjDPRORCayaRDhZ2FW4mVWwc4ZTVzaxzYSOcE3VJB4g8QGrjTuqdBLcoZmWBgr9PH1BKDpj9sh7KhRGHVrkUWpNIG6QjJIpnYFun7A1p2x2LrBFyNr4yyjlVbzLqtzZxcByS8SNfaQ-KdPRzSqSExS6yLoFqOWD7JUKgPNfoRswCEWJtuRpZGG3KMe3J5G1TnTBM_H6OsGAZqmt46-pSVX83_O5LiqUvLyhqr1jzClQdsJiY7cOqOrdRMYgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">PlayTorrio
مگاتورنتی که همه چیز را دانلود می‌کند:  بازی‌ها، موسیقی، فیلم‌ها، کتاب‌ها و هر نوع فایل.
https://playtorrio.pages.dev/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/6658" target="_blank">📅 09:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJyyguNe8XCsQ9C-rOfVUuXC35FIHpCpiRAX5xtKBGFNrAJ3sz-TV-JFjxn2xeURy-_oWCTuH64Q16D75vnKbn5IWWSqt31y7nfPtsOGtmgtsFXTSyOPTL9W1gEeCcDZrnXUObeEaQRT34g9Vi4lSYTz8MLwqHYe3C3VIVuvbwFK8SknxUVFqoYxAJs5dWjw6Ip_9HFxADniKEw7IpQj8-pQs4NHwhtiUy16sO8lNQfrIYRyYzkoiz2mDmqKNsysohEIyNyuo9cfP4bkkI454kbDoGyh6FfBTWm5U557jIjTadUngk9dfciDUauPZ3xsW0zfgWh7rhu08alTRcg6Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود Mythos و Fable 5 برگشته‌اند! دولت ایالات متحده این دو مدل‌ رو از حالت مسدود خارج کرده است.
امروز Fable 5 برای همه کاربران در دسترس قرار می‌گیرد و تا ۷ جولای می‌توانید تا ۵۰٪ از محدودیت‌های هفتگی خود را روی این مدل استفاده کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6657" target="_blank">📅 09:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZPdU_-8eR26raGUQdnUNFdlNOAuigFVmdy_cKWvod3AEkF4NS6EkE9ZYgroEYVUfu6y0ETs-P9xojnMLMkRt5OzA0f0YauqMJHhjIUpqNXu6TwFL-VSwWiEhvJ_IjoU_JuTi2PzZvoN_by6lXhfcJljfeN575dBSS28TPqRvxJ8tQ3iHQ8s_25WzeSDKqpzQUsqtvZvDK78TUuB5-e7RWLBLZfoaMdnVs3nbo4cjAxv6ykT7ZPZtQLT2NjRn9LwkCuYwyrOtS7W6yzZHxn4lfgLgbShBkHlBPhFjBhOlOAq2oSSHq3QyfopHjwwkQN8wq7gR2AguApbPZ_S-Ua1rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلود اوپوس بدون سانسور منتشر شد!
توسعه‌دهندگان Qwen 3.5 را با داده‌ها و استدلال‌های Opus 4.6 آموزش دادند و یک نابغه شرور واقعی ساختند.
• محدودیت سوالات فقط تخیل شماست.
• می‌توانید هر چیزی، حتی ترسناک‌ترین‌ها را درخواست کنید، اما مسئولیت آن با خودتان است!
• به صورت محلی اجرا می‌شود و بسیار سبک است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/6656" target="_blank">📅 08:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ArchiveTel
pinned «
🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6655" target="_blank">📅 08:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">درود دوستان AssA هستم
بابت خرابی ربات
@REN_WZA_BOT
دیروز معذرت می‌خوام
حقیقتا به خاطر شرایط نتونستم سرور تهیه کنم و ربات روی کلودفلر ران شده
فکرش رو نمی‌کردم که قراره انقدر استقبال بشه که سقفش به نصف روز نکشیده پر شه
😄
خبر خوب اینه که یه ربات بک اپ گذاشتم برای وقتی که سقف اولی پر شد بتونید کار هاتون رو راحت روی ربات دوم انجام بدین
جای نگرانی هم نیست تمام اطلاعات دیپلوی ها و کاربر ها انتقال داده میشن پس عملا هیچ فرقی برای شما نداره
مورد دیگه این هستش که خیلی از دوستان بدون اینکه پنل قبلی شون از کار افتاده باشه یا مشکلی پیش اومده باشه ده تا ده تا میسازن که واقعا عجیبه
🤔
خلاصه که دیگه قرار نیست به همچین مشکلی بر بخورید
و نکته سوم هم اینکه ربات دوم کمی با عجله ساخته شد اما از تست های خودم سالم بیرون اومد
اگر باگی یا مشکلی دیدین با تگ کردن آیدی ام توی چت بهم بگین
@Assa_7788
(بابت مشغله های کاری و پی وی شلوغ به احتمال زیاد پاسخ ندم بهتون پس ممنون میشم پیامتون رو با تگ کردن آیدی ام توی گروه بنویسین)
و عذر بنده رو برای طولانی شدن پیام بپذیرید
🌚
❤️</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6654" target="_blank">📅 05:49 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
