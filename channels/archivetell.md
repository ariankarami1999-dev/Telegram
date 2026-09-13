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
<img src="https://cdn4.telesco.pe/file/X5R2wXrDD6cEciyNvySHLGByUgdAcPnvRTvqVFHpC9TppDK-ovFygsLCk2_ZjOaVnF_8zvwJ5biOP6CiQYAqQYATDVIMpb8rVb-yIOmI1mB-kUpS3L6lIobuJ9wCY910dy8R9YmPVCUIJIMRafpYV74qMKPf8EbK4VHJ1Wznnx3PXpyqKTJTcbcNum4CQ3l376LrAWvQq2UAnV88-A_7Crh6ak6hKoZFWwBQlltOQz5eGHp-UGesrOhAZSGHEzxAnCbc0QVzCPOXRThMykzhr17ZOailTdDMs5PB_xU9XmFIXaRSPG1TV7zgq6pAxudPwVXume7JeSKz53x5QBoh6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 16:28:12</div>
<hr>

<div class="tg-post" id="msg-7738">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=QxdAAO4W1G5hqkbhEcHYYSAbKksuIfV6RvfFhSAVwlhQsamp7j9CL_FzSsQnQywHavWGIpFNUfuZlG8cNNqvW8Nl-DCcE1xCIpdZAuv8snYA_msXZFFHbyCWLzKGpR5zA5V0Xp8heA248d3M-NyhgBZ2fg2K9EHy_AEbLviQLib0tAAXS6J1LUvYdAWO9FAxv1XC5ofHCP6vWDa5o60qlzRC453xuPaA-UvMG5ouzJf8IG3syJ04Gke37yZeW6buIwTVYvwk9pvtrsj7slm8cnyKqMOieDmAjULsIYZx7a_fIBeMZmqKZAncdIorTlnXr80q_OaDA3DUuu-5SpriqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=QxdAAO4W1G5hqkbhEcHYYSAbKksuIfV6RvfFhSAVwlhQsamp7j9CL_FzSsQnQywHavWGIpFNUfuZlG8cNNqvW8Nl-DCcE1xCIpdZAuv8snYA_msXZFFHbyCWLzKGpR5zA5V0Xp8heA248d3M-NyhgBZ2fg2K9EHy_AEbLviQLib0tAAXS6J1LUvYdAWO9FAxv1XC5ofHCP6vWDa5o60qlzRC453xuPaA-UvMG5ouzJf8IG3syJ04Gke37yZeW6buIwTVYvwk9pvtrsj7slm8cnyKqMOieDmAjULsIYZx7a_fIBeMZmqKZAncdIorTlnXr80q_OaDA3DUuu-5SpriqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🎬
ساخت موشن‌گرافیک حرفه‌ای با یه پرامپت!
‏این ابزار هوش مصنوعی کل فرآیند ساخت تیزر تبلیغاتی، از استوری‌بورد تا تدوین صدا و انیمیشن رو خودش انجام میده و خروجی رو با بیت موزیک سینک می‌کنه. خوراک بچه‌هاییه‌ که سریع میخوان خروجی باکیفیت بگیرن.
🔥
‏
⚡️
دسترسی به منابع غنی:
۱۵۷ مدل سناریو، ۲۱۴ استایل بصری و کلی الگوریتم انیمیشن آماده
‏
⚡️
شروع سریع:
کلی تمپلیت آماده‌به‌کار داره که کار رو برای پروژه‌های فوری جلو میندازه
‏
⚡️
عملکرد هوشمند:
کافیه ایده‌تون رو متنی بدید تا در لحظه ویدیو تحویل بده
😎
برای دانلود ابزار تولید ویدیو
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 294 · <a href="https://t.me/ArchiveTell/7738" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7737">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">1.7B token MINIMAX
url:
api.minimax.io/v1
key:
sk-cp-k8fnOYl1xeWGiSNy7qWxNP3Gu-nkuMKLaAFl7ZoCnGiqA2sabKF30eMTQNurXcyGtgGdbM168WEvBhyTOo2WQaE9RoXzVPAyyG3CYwZuybXzDILyBEBc5nk
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 704 · <a href="https://t.me/ArchiveTell/7737" target="_blank">📅 14:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7736">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zn0rgzjXGTSr-XogC0HBnXYqpNKlzVcw4z_hNhiRSbdvj-4Nu2bZy4OTUTqHP4rbk9vuhnZRPSPssvrkjagwJQMSn9eNW_asB_wokN736peg_AcKQhEXT8E3UsOreFw3aK053lWTbVVf1mzRNRQxDzjNSVRxjoN_9Th7_BVkUH9f2NZUIepyd4JIOHEXlu2a7R0_C7FruEf2w5B0zDa7zg-yWbqKkcQAmxbxkd0JdvvqzB1ycWdTttDf2slZ_tyHT6jSkSCDtxY-0KyTWpE4XeiPiPMdBQgnE-7T4WZDyVNvuJUAtpCLrRDk1GKdB5LqFx3cWymuK-09zYVXv7S9ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
مرجع خفن اسکیل‌های ‌Claude Code⁩ و ‌Codex⁩!
‏سایت ‌SkillsMP⁩ یه کاتالوگ تر و تمیز با بیش از ۳۳ هزار اسکیل آماده‌ست که تو کار با هوش مصنوعی کلی جلوتون میندازه.
🤖
‏•
دسته‌بندی جامع:
از برنامه‌نویسی و ماشین‌لرنینگ تا امنیت و کار با ‌API⁩
🔍
‏•
دسترسی سریع:
لینک مستقیم به گیت‌هاب برای هر اسکیل
📂
‏•
کیفیت‌سنجی:
دارای ایندیکاتورهای کیفیت برای انتخاب بهترین ابزارها
⚡️
‏خوراک بچه‌های وایبکودره که بخوان پرقدرت‌تر پروژه‌ها رو ببرن جلو.
🚀
🔗
skillsmp.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 722 · <a href="https://t.me/ArchiveTell/7736" target="_blank">📅 14:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7735">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🛡
دیگه ایمیل و پسورد اصلیت رو به هیچ سایتی نده!
حتماً براتون پیش اومده که برای ثبت‌نام در یک سایت مجبور شدید ایمیلتون رو بدید، اما بعد از یه مدت صندوق ایمیلتون پر از پیام‌های تبلیغاتی مزاحم شده یا اون سایت هک شده و رمزهاتون لو رفته!
ابزار جالب
AliasVault
دقیقاً برای حل همین مشکل ساخته شده:
💎
این ابزار براتون چیکار می‌کنه؟
⚡️
ساخت بی‌نهایت ایمیل دائمی:
برخلاف ایمیل‌های موقت که بعد از ۱۰ دقیقه می‌پرن، این ایمیل‌ها
کاملاً دائمی و همیشگی
هستن و برای هر اکانت می‌تونید هر تعداد ایمیل دلخواه که خواستید بسازید!
⚡️
دریافت کد ثبت‌نام داخل خود برنامه:
نیازی نیست برید یه ایمیل دیگه باز کنید؛ ایمیل‌های تایید و کدهای ورود مستقیماً داخل همین برنامه براتون میاد!
⚡️
مچ‌گیری از سایت‌های متخلف:
اگر یه سایت ایمیل شما رو به تبلیغاتچی‌ها بفروشه، دقیقاً می‌فهمید کار کی بوده چون برای هر جا یک ایمیل اختصاصی ساختید.
⚡️
نصب روی گوشی و کامپیوتر:
هم اپلیکیشن برای موبایل داره و هم افزونه برای مرورگر، و خودش پسوردها رو سر جای درست پر می‌کنه.
💬
چرا این ابزار فوق‌العاده‌ست؟
•
ایمیل‌ها هرگز منقضی نمی‌شن:
هر زمان در آینده بخواید وارد سایت بشید یا رمزتون رو بازیابی کنید، پیام‌ها باز هم به همین ایمیل دائمی میاد.
•
سقف تعداد ندارید:
برای ۱۰۰ تا سایت هم می‌تونید ۱۰۰ تا ایمیل مستعار و رمز مجزا بسازید.
•
کاملاً رایگان و امن:
بدون هیچ هزینه‌ای، امنیت و آرامش صندوق ایمیلتون رو تضمین می‌کنه.
🌐
ورود به وب‌سایت AliasVault
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 962 · <a href="https://t.me/ArchiveTell/7735" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7734">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eM3bjlVQD6n5b834KoMHofwwWo4bDl7BcZjxz6frkwJp4bya_7TySLMHlIszmPcThYwBssPG1cnDnahUUiZd8VsbPq1pgyyZAQk3bovhgC65-lk5MgzpHT95ey1Zz3HgkSFYL43ChoQTZ09sX4zLOYmyrvZ4FHMh0xR_iMbcdb7VrbG4s84lOOKoaN7YK3hAsZS3aVEIqcVZ13VzJs0Ljk75vO6dsHKVZq_K8NrNmE799pqToj6XMJUhIkeKJWPu2a1zepGkyJCESSC4NB2_am-cVUlBQCWiellO6aK7L8QryZwv8NJ-remszFR6DZ3ktGhl1iK4MhPx6Fhisv3KLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک سایت، ده‌ها مدل و ابزار با اعتبار رایگان روزانه
🎁
💬
Multi AI Chat
GPT، Claude، Gemini، DeepSeek، Grok، Qwen ، Llama
همه در یک چت، با امکان مقایسه جواب‌ها
🎨
تولید و ادیت عکس
تولید تصویر از متن (Flux، Stable Diffusion، Ideogram…)
حذف/تغییر پس‌زمینه، حذف اشیاء و متن از عکس
Face Swap، Upscaler، تبدیل اسکچ به تصویر
ویرایش عکس با دستور متنی + تولید تصویر سه‌بعدی
🎬
ویدیو
تولید ویدیو از متن و از عکس
Face Swap روی ویدیو
خلاصه‌سازی، زیرنویس و ترجمه ویدیوهای یوتیوب
🎵
صوت و موسیقی
ساخت آهنگ (Suno، MusicGen…)، Text-to-Speech با صداهای طبیعی
شبیه‌سازی صدا (Voice Clone)، تبدیل ویس به متن، حذف نویز
✍️
نوشتن و تولید محتوا
تولید محتوا، بازنویسی، خلاصه‌سازی، ترجمه، گرامر
تحقیق کلمه کلیدی و تشخیص محتوای AI
🌐
لینک سایت :
app.1min.ai
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 985 · <a href="https://t.me/ArchiveTell/7734" target="_blank">📅 12:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7733">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎁
دریافت 20,000,000 توکن رایگان
claude-fable-5 | claude-sonnet-5 |
deepseek-v4-pro | muse-spark-1.2
✅
وارد ربات زیر بشید و api key رو دریافت کنید
@kiro86bot
💡
سازگار با همه سرویس‌های OpenAI-Compatible
🌐
base url:
https://api.xpiki.com/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/ArchiveTell/7733" target="_blank">📅 11:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7732">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🆓
هوش مصنوعی رایگان  — بدون ثبت‌نام
Kimi K2.6 | GPT 5 mini | DeepSeek V3.2
📌
امکانات:
⚡️
چت هوش مصنوعی نامحدود
⚡️
تولید متن و محتوا
⚡️
بدون ایمیل، بدون رمز عبور، بدون کارت بانکی
📌
نحوه استفاده:
🔗
وارد
این سایت
بشید مدل موردنظر را انتخاب کنید و شروع کنید.
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7732" target="_blank">📅 23:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7731">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKUqeExmmsHO7NKWvDhrkn9aptlNqf0BzIDNp_FeI_JjTW620-M8VTdtg_KL1Xc8V1rS3M-jYRK2sVbJTKmLEZi5PxqdAtVlkpiqdDYsUA6gyEN3r4-QtSzBfjJuCLhxuklZzPvvd3tDlshQnGDV9skp6Rl1qHkABQKzcy06_90KFrCZUlo_CCJSdsMn2qAhcli30fB_WW6Ca2imckzPFGo77RjlGonhcmgn_Zg7_x8WAm7CfM0eeQO5FOkGPvXbkrbWq-FdPWJxERMNOwu1SctgpUeHS0foejmoBCnCwHdAsc5D7tJqbCeXmEfyi-LnJ-cZaSfM1Ei-Yn7XujL2UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
۵۰۰ مگابایت پروکسی رزیدنتیال رایگان (
proxyma1.io
)
یک سرویس پروکسی رزیدنتیال که با ثبت‌نام از طریق تلگرام ۵۰۰ مگابایت ترافیک رایگان می‌دهد و API هم دارد.
📌
نحوه دریافت:
1️⃣
وارد سایت
proxyma1.io
شوید و ثبت‌نام کنید
2️⃣
پس از ثبت‌نام، یک پیام برای استارت ربات تلگرام نمایش داده می‌شود که داخل آن یک کد هدیه قرار دارد
3️⃣
ربات را استارت بزنید و کد را برای ربات ارسال کنید
4️⃣
۵۰۰ مگابایت به حسابتان اضافه می‌شود
🚀
📌
ویژگی‌ها:
☑️
پروکسی رزیدنتیال (Residential)
☑️
۵۰۰ مگابایت ترافیک رایگان
☑️
پشتیبانی از API
☑️
ثبت‌نام آسان با تلگرام
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7731" target="_blank">📅 23:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7730">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksdZ2-sNSE2U6mdOGPgVb3WKpAkdHf0jedEAjtQESy8PEYArNsihBJflKwUDZooWQMLcZojcz47_M5Xhl0BfDXHq6IKGM0ZayExb7yjbHh9i29oZV5xRX0KizTCrH1QYUW8qT2KYvmsQSavaiLPT35_g9RMbF-vmeRE6e9iQdF9Iwz3YBAtnJeu-W5sbOOLXe_hzX5Eh9qz3cDUCpD7nARyhg4hoRVk_6NYjPO9OZ2OroqOYhym0xJ2_jqjrb8jVRMobQznPbPlJ4kc_HWAHWse4Q59q2P14LiiTIQ9byfE6M9AM6YyGhY09WQF4g5j4Kw3LpuE6TnhbGEC63FBevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
۵۰۰۰ اعتبار رایگان برای مدل‌های برتر هوش مصنوعی
پلتفرم جدید در شروع کار ۵۰۰۰ اعتبار به شما هدیه می‌دهد تا با قدرتمندترین شبکه‌های عصبی کار کنید: تولید متن، عکس و ویدیو در یک جا.
📌
امکانات در دسترس:
☑️
چت چندمدلی
☑️
تولید تصویر
☑️
تولید ویدیو
☑️
موجودی اولیه: ۵۰۰۰ اعتبار رایگان
🪙
📌
روش دریافت:
1️⃣
ورود به
getunikey.ai
2️⃣
ثبت‌نام یک حساب کاربری جدید
3️⃣
ایجاد کلید API در تنظیمات پنل
4️⃣
استفاده در رابط چت یا ابزار های واسط
base url:
https://getunikey.ai/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/7730" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7729">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔍
Hidden File Hunter — شکارچی فایل‌های مخفی ویندوز
دنبال فایل‌های مخفی و سیستمی توی ویندوز می‌گردی ولی پیدا کردنشون واقعاً دردسره؟ این ابزار دقیقاً برای همین ساخته شده
👇
؛ Hidden File Hunter یک برنامهٔ دسکتاپ ویندوزیه که تمام فایل‌های مخفی و سیستمی درایوهات رو پیدا می‌کنه و توی یه جدول مرتب و قابل مرور نشونت میده.
✨
امکانات:
✔️
پیدا کردن تمام فایل‌های مخفی و سیستمی در همهٔ درایوها
✔️
نمایش نتایج در یک جدول مرتب و خوانا
✔️
خروجی گرفتن از فهرست کامل مسیرها در قالب فایل TXT
✔️
کپی کردن خود فایل‌ها با حفظ ساختار پوشه‌ها در مقصد دلخواهت
✔️
فقط می‌خونه و کپی می‌کنه — هیچ فایلی رو تغییر نمیده، حذف نمی‌کنه و بهش دست نمی‌زنه
✔️
ساخته‌شده با Python و PySide6
✔️
تم تیره و روشن
✔️
رابط دوزبانهٔ فارسی و انگلیسی
یه ابزار ساده، سریع و امن برای وقتی که می‌خوای بدونی توی سیستمت چه چیزهایی از چشم‌ها پنهان مونده.
🔗
لینک گیت‌هاب:
github
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/7729" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7727">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚀
اپلیکیشن Bifrost (بایفراست)؛ پل ارتباطی فوق‌سبک تلگرام بر بستر ورکر کلادفلر منتشر شد.
بایفراست یک بریج لوکال (Local SOCKS5) مدرن و بهینه برای اندروید است که ترافیک تلگرام رسمی را از طریق پروتکل TWP به ورکر رایگان کلادفلر متصل می‌کند؛ با پینگ پایین، بدون قطعی و با سرعت دانلود فوق‌العاده بالا.
🔒
بدون نیاز به VPN، بدون روت و با مصرف باتری نزدیک به صفر:
این پروژه کاملاً متن‌باز (Open-Source) است و برخلاف فیلترشکن‌ها از VpnService استفاده نمی‌کند (هیچ علامت کلیدی بالای صفحه نمایش داده نمی‌شود و اینترنت سایر برنامه‌ها کاملاً دست‌نخورده و بدون تغییر باقی می‌ماند). مصرف پردازنده در زمان عدم استفاده دقیقاً ۰.۰٪ است و امنیت و رمزنگاری پیش‌فرض تلگرام (MTProto) نیز کاملاً حفظ می‌شود.
📥
دانلود و نصب برنامه (از گیت‌هاب):
https://github.com/Qorvhex/Bifrost/releases
⚡️
کانفیگ تستی برای شروع (بعد از نصب، کپی کنید و داخل برنامه Paste کنید):
twp://telp.qorvhe-x.workers.dev?clean_ip=1music.cc#Bifrost-Test
🛠
سورس‌کد اسکریپت ورکر (TWP):
https://github.com/Qorvhex/TWP
📁
لینک پروژه و سورس‌کد در گیت‌هاب:
https://github.com/Qorvhex/Bifrost
لطفاً تستش کنید و سرعت و عملکردش رو بهم بگید!
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7727" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7726">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🖥
مرورگر ضد ردیابی Private Browser Pro؛ هویت جعلی و دور زدن بن شدن اکانت‌ها!
​بچه‌ها اگه نیاز دارید روی یک سایت چند اکانت مجزا بسازید بدون اینکه سیستم‌های امنیتی بفهمن همه‌شون مال یک نفره، یا می‌خواید ردپای دیجیتالی‌تون رو کامل مخفی کنید، این مرورگر اوپن‌سورس ویندوزی دقیقاً همون چیزیه که دنبالشید. این ابزار بر پایه نسخه فوق‌امن Ungoogled Chromium و Electron ساخته شده و از زبان فارسی هم پشتیبانی می‌کنه.
​
🎭
جعل مشخصات سیستم (فینگرپرینت):
شبیه‌سازی کارت‌های گرافیک قدرتمند (مثل RTX 4090، سری RX 7900 و تراشه‌های اپل)، اضافه کردن نویز به Canvas و AudioContext و هماهنگ‌سازی هدرها برای عبور آسان از سد کپچاهای Cloudflare Turnstile، hCaptcha و reCAPTCHA
​
📁
مدیریت و تفکیک کامل پروفایل‌ها:
امکان ساخت محیط‌های دائمی (Persistent) برای ذخیره دیتای هر اکانت در پوشه جداگانه، یا حالت موقت و یک‌بارمصرف (Ephemeral) که با بستن پنجره کل ردپا پاک میشه + دکمه پاک‌سازی آنی
​
✅
پروکسی پیشرفته و ضد نشت اطلاعات:
پشتیبانی از پروکسی‌های SOCKS5 و HTTP (با یوزرنیم و پسورد)، حل آدرس‌ها از داخل پروکسی جهت جلوگیری از DNS Leak و غیرفعال‌سازی WebRTC برای مخفی ماندن کامل IP واقعی
​
✨
محیط کاربری تمیز و دو زبانه:
کرومیوم دست‌نخورده بدون واترمارک‌های تستی، تم دارک با کلیدهای میانبر سریع و پشتیبانی کامل از منوی فارسی و انگلیسی
​
💡
بهترین سناریوی استفاده:
ایده‌آل برای مدیریت چند اکانت در شبکه‌های اجتماعی و پلتفرم‌های حساس، تست وب، ریسرچ‌های OSINT و حفظ حریم خصوصی بدون نیاز به خرید اشتراک‌های گران‌قیمت مرورگرهای ضد ردیابی.
​
🔗
گیت‌هاب
​
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7726" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7725">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">📥
تبدیل فایل‌های تلگرام به لینک مستقیم نیم‌بها با ربات Leecher!
بچه‌ها اگه کندی دانلود از تلگرام یا قطعی فیلترشکن موقع دریافت فایل‌های حجیم کلافتون کرده، یا می‌خواید تورنت و ویدیوهای یوتیوب رو مستقیم به فایل تلگرامی تبدیل کنید، این ربات لیچر ایرانی حسابی به کارتون میاد.
🇮🇷
لینک مستقیم با ترافیک نیم‌بها:
تبدیل آنی فایل‌های تلگرام به لینک دانلود پرسرعت تحت وب (سازگار با دانلود منیجرها) با محاسبه مصرف اینترنت به‌صورت نیم‌بها
🌐
دانلودر همه‌کاره (لینک به فایل):
پشتیبانی از دانلود مستقیم لینک‌های یوتیوب، اینستاگرام، وب‌سایت‌ها و حتی فایل‌های تورنت و تحویل فایل داخل چت
☁️
اتصال ابری به گوگل درایو:
امکان لینک کردن اکانت شخصی Google Drive برای ذخیره و آپلود مستقیم فایل‌ها در فضای ابری بدون مصرف حجم گوشی
🎁
شارژ رایگان روزانه:
۱ گیگابایت حجم رایگان در هر ۲۴ ساعت بدون نیاز به پرداخت هزینه یا خرید اشتراک
💡
نکته کاربردی:
لینک‌های ایجادشده بین ۶ تا ۸ ساعت معتبر هستند؛ کافیه فایل رو به ربات بفرستید، لینک مستقیم سرور ایران رو داخل IDM کپی کنید و با حداکثر پهنای باند خط‌تون دانلود کنید.
🔗
استارت ربات
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7725" target="_blank">📅 20:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7723">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMbnrVecEs_h5rwWFFotpCn6I0VKUhwo6t8QZeVjg07MHDvT8LeyRV6cmmhGcXdZD5ABs-WH_UBva1qUMWKc9utzNVLNNUHfBmd3udcF55yTQOSLhdwv_j6Zli5V4Hq1Szxs-OoCVKfG6_bzsK1DQxiynRkVz96CH_65A2HrLZynJ5q1SLU3ebGUBglcp2sWx313qP_6xDs1Uc6UjRSRk2z_z1EqphdtX5rrl9rRISo0DYNy1lOUaFdVnG1kpRw5o5v7e9JPoL-CNQK2RPKQKNzzjC6MdS5pxzNnsjfPBefhyuAY2p_wHzGwzXz4dCBxtRmxZwFI9B2ee4Tnv02IoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید (1.8.0) برنامه MSN-GUARD منتشر شد :
💢
BOOM
💢
تغییرات :
1- اضافه شدن متد اختصاصی SHARD برای اولین بار
-_-_-_-_-_-_-_-
2- دسترس‌پذیری کامل و پشتیبانی 100% از صفحه‌خوان TalkBack برای عزیزان نابینا و کم‌بینا برای اولین بار
-_-_-_-_-_-_-_-
3- آپدیت هسته
-_-_-_-_-_-_-_-
4- اضافه کردن قابلیت Backup و Restore و Reset Factory از تنظیمات برنامه
-_-_-_-_-_-_-_-
5- برطرف شدن مشکل دکمه Reconnect در نوتیفیکیشن
-_-_-_-_-_-_-_-
6- اضافه شدن Theme کاملا روشن برای استفاده زیر آفتاب
-_-_-_-_-_-_-_-
7- برطرف شدن باگ اتصال خودکار پس از قطعی اینترنت و چند باگ دیگر
-_-_-_-_-_-_-_-
6 روش دسترسی به اینترنت آزاد:
1: متد Masque
2- متد Wireguard
3- متد Warp On Warp
4- متد Psiphon (اختصاصی و اولین)
💯
5- متد Tor (اختصاصی و اولین)
💯
6- متد SHARD (اختصاصی و اولین)
💯
💻
ریپازیتوری گیت‌هاب (متن‌باز):
https://github.com/mbm110/MSN-GUARD
📌
لینک مستقیم دانلود :
برای گوشی های 64 بیت
برای گوشی های  32 بیت
برای تمامی گوشی ها
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7723" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7722">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✉️
؛ Turbo Mail ایمیل موقت، سریع و بدون دردسر
اگه برای ثبت‌نام یا دریافت کد تأیید به یه ایمیل موقت نیاز دارید، Turbo Mail یه گزینه ساده و سریع برای شماست.
⚡️
ساخت فوری ایمیل موقت
👌
بدون نیاز به لاگین و ثبت‌نام
⏳
اعتبار ۲۴ ساعته
🔒
مناسب برای دریافت ایمیل و کدهای تأیید
🚀
ساده، سریع و بدون مراحل اضافی
کافیه وارد سایت بشید، ایمیل موقتتون رو بسازید و استفاده کنید.
🔗
https://mail.turbocenter.shop
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/7722" target="_blank">📅 18:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7721">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎧
دستیار هوشمند و همه‌کاره موزیک‌بازها؛ دانلود با کیفیت FLAC با ربات MelodyAddict!
بچه‌ها اگه عشق موسیقی هستید و از دانلود تک‌به‌تک آهنگ‌ها، افت کیفیت یا پیدا نکردن موزیک پس‌زمینه کلیپ‌ها کلافه شدید، این ربات فوق‌العاده با پشتیبانی کامل از زبان فارسی دقیقاً خوراکتونه. همه‌چیز از شزم اختصاصی گرفته تا رصد خودکار پلی‌لیست‌ها رو براتون یکجا جمع کرده.
🔄
سینک خودکار پلی‌لیست‌ها:
زیر نظر گرفتن لایک‌ها و پلی‌لیست‌های Spotify، SoundCloud، YouTube Music و Apple Music و ارسال خودکار ترک‌های جدید با امکان زمان‌بندی ارسال (۳ ساعته، روزانه یا هفتگی با دستور /digest)
🔍
شناسایی جادویی آهنگ:
پیدا کردن نام و فایل موزیک فقط با فرستادن یک وویس کوتاه، زمزمه، فایل ویدیویی یا لینک ریلز اینستاگرام، تیک‌تاک، یوتیوب و توییتر
💎
کیفیت استودیویی FLAC و Lossless:
قابلیت تنظیم کیفیت پیش‌فرض خروجی برای گوش دادن به بالاترین بیت‌ریت ممکن، با سرعت عالی و کاملاً بدون تبلیغات
📂
مدیریت پلی‌لیست‌های ابری:
امکان دسته‌بندی، ساخت و اشتراک‌گذاری مستقیم پلی‌لیست‌های شخصی داخل تلگرام
💡
نحوه استفاده:
ربات رو استارت کنید، زبون رو روی فارسی بذارید و برای شروع کافیه وویس یک آهنگ یا لینک پلی‌لیست موردعلاقتون از اسپاتیفای یا ساندکلاد رو براش بفرستید تا بقیه کارها رو خودش اتوماتیک انجام بده.
🔗
استارت ربات هوشمند
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7721" target="_blank">📅 16:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7720">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jVgYfmWz1XO6pnwy_fTqzTBlaG8USKOmT43JUX7aWSa5RFKz32kiZb3LhdaBq4lB85aQc7rb5NuDZN5e67ECGfV8RZIBMou5XRgB68eFNaGvc_DD4gScrGTvgAoOdBAA5iduLydt1SXJ0ab1hgFYxrctRi0BlNKiYI-SWgLpyVU2OmzcjMnG6x_Jfn-_VgGzmIH_5jCHaF9mgRDNyVM61hmkLNa8nSaFozfBRa9oX5V3aidn9JxfrGOwCkMZ-6KINFD9Tx0iaZOnJ0h7S25DpGxNTeqUsmQ4Id_AvKxYE_uUB82MSYSWHty8nfUPHaTA9wI2XkRZMc5bEBkwCYW7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید ArasClient منتشر شد!
نسخه جدید با اضافه شدن بخش Free منتشر شد و از این به بعد این بخش به‌صورت مرتب آپدیت میشه.
📱
؛ ArasClient یک کلاینت سبک و کاربردی برای مدیریت و استفاده از کانفیگ‌هاست که تمرکزش روی سرعت، سادگی و اتصال راحت‌تره.
🆕
اضافه شدن بخش Free
⚡️
آپدیت منظم کانفیگ‌ها
📊
تست و مرتب‌سازی هوشمند سرورها
🔄
انتخاب سریع‌تر سرورهای مناسب
📦
پشتیبانی از نسخه‌های مختلف اندروید
🔗
دانلود نسخه جدید:
https://github.com/ArasTey/ArasClient/releases/download/v1.6.8/ArasClient_1.6.8_arm64-v8a.apk
🔗
سورس پروژه:
https://github.com/ArasTey/ArasClient
💬
نظر، انتقاد یا پیشنهادتون رو کامنت کنید.
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7720" target="_blank">📅 15:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7718">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPwMUSduTem8GwbITsVuboRhVWArR1Z8L0yFOs9RtwBF8WK3FDaBd6AJt4F9XVI-VhtY8m3UukSmhsKJDgMUJmUj8LB5c3CaiPd58Knv3fSpauWSeqoD6ne7ClQhBabnAn20DtwOANF3c9G70KGk-rAB4-k3EXqpIlqb97iC_bya1ExSVWWoj13UfSheuqkOxiWfm3ZIt5QupQS738yfagppbOXLQqITyZB_uGzhH-gAx0Xih7_NthEiG86SYj4HQ6seCk4BAl0H-87M2mgq5NgX8S1oP4XVbb6D3ZfAs8yzOVK2XheRCNA_socaXrSNUDuE5Uz25PJ3ucOVIIPZvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
اگر می‌خوای شبکه‌های کامپیوتری رو از پایه تا سطح حرفه‌ای یاد بگیری، نت‌داد دقیقاً برای تو ساخته شده.
از مفاهیم بنیادی مثل آدرس‌دهی IP، سوییچینگ، مسیریابی و امنیت گرفته تا شبکه‌های مدرن، همه چیز با پروژه‌های عملی و مثال‌های کاربردی آموزش داده می‌شه.
✔️
۱۰۰٪ پروژه‌محور
✔️
۵۳ درس تخصصی
✔️
۱۴ بخش آموزشی
شروع یادگیری از اینجا:
🔗
https://netdad.vercel.app
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7718" target="_blank">📅 15:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7717">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vt1iSXMuEvdVOQlMgTMeuUHyUtfsghRMZ9ZJhKbT1D9dz-b71TSHQUiNh6DvYSmsr_5J1-17gRIsagjNrwpU90ubVK1BPYHbgEeh5YGlv9SIPquPAfGb_1OrMjs4tQV_2skHMQBpDP8HSpODHy9d_C871STzb8tKzKw8pw93AHwkiajRrAo8llf6Hko5WqWSVjfg3Au6JVHo34WSp5BwKOx2TkA5B_k-LNvz7TkqIlCnOhLUYiXmWM4lw-atNd9W3uxBuSb4HYJaYA4MF3cnDajsGSB8mipyfIy3K-jrmXJExwjqju6nWtwL0c4aFu-8-Qn9aC-U19qZRZWnriWS9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
100 میلیون توکن GLM-5.3-Flash با ثبت نام در AutoClaw + ZAI
از تاریخ 14 تا 16 سپتامبر (دوشنبه تا چهارشنبه) 600 میلیون توکن GLM-5.3 و DeepSeek 4.1 بدون نیاز به کارت و همچنین یک کد تخفیف ارائه خواهد شد.
این پیشنهاد در
اینجا
قابل دسترسی است (در حال حاضر شامل ۱۰۰ میلیون توکن می‌شود)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7717" target="_blank">📅 14:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7716">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/She3BJPQqOXkXAsWNwdhAzgf5TJpbF9AUcdkEIdFXM2w1Y5EWUaczF9e47q9nYmM-HcwH0XgKLVY1SOdPmOZic1NsJtQeXnKQUZr-yZ9jilustnT-2PIfYA07lScapqqzou_O18-R3uavlFdPsQs7Aw0zMIEWmKvIWqFY6QlrbzKN-ZSPxv9Xx1m_R0_nUrYD99Ygoh2ZPhmcKy4WfIchPF74XnUPII_FbtgCuNUvb_ZA7R9znRz1DLLN0_ZvRIMuTCrXvDYG4wu2vDT_8I3TXDjEjXXbeZDHhmRSo6EEWAx0LtiKBNVPXygGymg73gJcl51ryjCvX0TtIR0dyGAew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥁
کیبورد لپ‌تاپت رو به یه درامز حرفه‌ای تبدیل کن
پروژه خفن KeyBeat یه استودیوی درامز تحت وب هست که بدون نیاز به هیچ نصبی، مرورگرت رو به یه ساز واقعی تبدیل می‌کنه
🔥
یه پروژه اوپن‌سورس عالی برای برنامه‌نویس‌ها، آهنگسازها و عشقِ موزیکا
🔗
لینک سورس کد و اجرای مستقیم:
https://github.com/faithsaly5-stack/Keybeat
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7716" target="_blank">📅 12:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7715">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iu7mXPt57J7-xG3PjztY9yQV7aAtdY21x2Eq5cHucSoOoVjE1gyDZXfrRUGANQCGHSj0SuwITtFjmabGBwbN2ROpnqYQRVEcWZI7sFw-K3rHrgN9pyslSl-kKN8_X4BaeDttFqfRsrRHuZlHpKcUiLjpmziH0ltfJSUZvtMK6NHNMdJDFBWhzcnMLSToImEUr3SGUE4yvTlIByVPTDDOSRp14wz6aktnnHyO3PrThLIj5RWwbSlS2SbCE-420Y84DBiBK85IPbS5_SFkSq8Z-IGKYWbQolOZnYV_nmlw-X3nyPRRVX_husD8rik-gOec5MVtf8yA6siU0vW-wXJEGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
دریافت آیپی رزیندنتال رایگان
💎
با گوگلتون سایت زیر بشید و روی claim offer کلیک کنید.
بعدش برید بخش proxy generator و پرش کنید و بزنین براتون 300 مگ آیپی رزیدنتال میده
🆓
http://rainproxy.io
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7715" target="_blank">📅 10:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7712">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enRyIC1qiHwHh7CBTHUtxztDLg6v172DAO1CPhSlyXWR6URrOjUbImIvgHoo6mnMkpsKf2XnFnNNyT3Sbq-_SmNKRWrn5YvZ92Ki5M_ntRnrGpfmICgwn5kb7kqGotY-CmNhMKjx53cbfG7taKL3aLVaejSteZRVfPOfSSdWMuDy0dik7dKiAoGJAdSbsgOtzi1nVjf57LZLwuFB8T2pF8BJwvLmsqV4koBQc84KTjNfM4kjbisGz_bpwKaGo3ouGOoCqVJUX4ZeIT-p01J7uzL0I3o1zJSFk_-6j0wZTs6P_BhgTJQbw4c15zz6Ac8YlDkPXsBS56sgXaBxlFpMAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
15 دلار اعتبار رایگان برای دسترسی به بهترین مدل‌های هوش مصنوعی
استفاده از مرورگر به شما 15 دلار اعتبار می‌دهد تا مدل‌هایی مانند موارد زیر را امتحان کنید:
• GPT-6 Astra
• DeepSeek V4.1 Flash
• GPT-5.6 Luna
• Claude Opus 5
• Grok 4.5
برای دریافت:
🔗
browser-use.com
با استفاده از حساب گوگل خود ثبت نام کنید و شروع به استفاده کنید.
برای دریافت اعتبار بیشتر، از چندین حساب استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7712" target="_blank">📅 21:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7711">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🧰
جعبه‌ابزار همه‌کاره و فوق‌سریع تلگرام؛ معرفی آپدیت بزرگ بات Amir Tools!
بچه‌ها اگه کلافه شدید از اینکه برای هر کار کوچیک (هوش مصنوعی، استعلام قیمت ارز، دانلود یوتیوب و تبدیل فایل) یک ربات جداگانه استارت کنید، این بات همه‌کاره دقیقاً خوراکتونه. در آپدیت جدیدش کلی ابزار مدرن با رابط شیشه‌ای اضافه شده تا از ده‌ها بات متفرقه بی‌نیاز بشید.
🧠
هوش مصنوعی با حافظه اختصاصی:
مکالمه پیوسته بدون فراموشی کانتکست چت، سوئیچ خودکار روی مدل‌های پشتیبان و امکان ریست سشن
📥
فایل به لینک مستقیم و دانلودر یوتیوب:
تبدیل آنی انواع فایل، ویدیو، آهنگ و ویس به لینک مستقیم پرسرعت + دانلود مدیا از یوتیوب با بالاترین کیفیت
📈
نرخ لحظه‌ای و چارت زنده بازار:
استعلام آنی قیمت دلار، تتر و ارزهای دیجیتال (BTC, ETH, TON و...) همراه با نمودار اختصاصی و باکس High & Low
🤫
پیام ناشناس امن و دوطرفه:
ساخت لینک اختصاصی با آیدی تصادفی برای دریافت متن، ویس و عکس ناشناس با قابلیت پاسخ‌گویی مستقیم
🎁
سیستم قرعه‌کشی خودکار کانال:
ساخت مسابقات و چالش‌های گروهی با دکمه شیشه‌ای و قرعه‌کشی کاملاً خودکار و عادلانه بین اعضا
🛠
میکروابزارهای روزمره:
ساخت بارکد تصویری (QR Code)، پسوردساز غیرقابل‌نفوذ، مبدل ارز به تومان، هواشناسی و مینی‌گیم‌های کوئیز
💡
نحوه استفاده:
وارد ربات بشید، دکمه شیشه‌ای منو رو لمس کنید و بدون نیاز به رجیستر یا مراحل طولانی، به تمامی ابزارها به‌صورت یکپارچه و رایگان دسترسی پیدا کنید.
🔗
استارت ربات هوشمند
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7711" target="_blank">📅 20:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7710">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است.…</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7710" target="_blank">📅 19:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7708">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل: ① به https://arena.ai/ مراجعه کنید. ② حالت Direct Mode را انتخاب کنید. ③ در لیست مدل‌ها، GPT-Image-2.5 Sunburst را پیدا کنید. ④ به مدت 72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود.
✈️
…</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7708" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7707">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با هر رفرال شما 100 دلار و شخص دریافت کننده…</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7707" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7706">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeI-GHT7SdnRPld9nkDJmX_neluE7hUE-NOMv1Q4FF-FqoMi52h0Cw3KcL0X1ZZYctrFsrEZ5c40qfdTnLYDSGWClA_hemnMWag9gRCgPr8tSmLY0pXe6pm0vehVvMz_TK2ABYHPhRQbx_sx12OuAWutaADQa0wtZg_9NyB0VxEK04ZpmUCEe-osgQ8NjttiFnGo2NV8l8WgB6i_OF9XVWC3yQ3Ay-29AfbZoq341o5ZSc8n8LLsl-HHNWxQIWHktPXRacZOHOeWMDDyQICmo9PrNuyasZHDzP9mRMnXMpcVDx7yb3gN2QWbsUEZgfZudxvxUmoMCKWoYAfaDQz-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل:
① به
https://arena.ai/
مراجعه کنید.
② حالت
Direct Mode
را انتخاب کنید.
③ در لیست مدل‌ها،
GPT-Image-2.5 Sunburst
را پیدا کنید.
④ به مدت
72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود
.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ma2cA8gzbHIz_u--fI0JC5nNQUegQAdi5Kd5zZPFQkcetvhMoYnluTWXa6LwOvRkGjsZB-7P5Wc3t0sUSMXsbe_o6n8xalAcoW13-QtMi6mNYDplzc-vRnK4SfJfoYuyndQEAcKfAhhWnnTWVaPPB0ktN8rXMAZI96pxbuOdZdmsTx2ITo0IebXNtT3-AJOhMzzh5F2iYsFN7yJ8NyXf75V0-CUqfA5vQxJhdu8n3fj_Jc0uqPwTe1ijn3Rr9l7JakLH-3NDozm8Ery-ftBui72hwbkHqDGmr6-6eHLSoJ1mI90DerBd9mjs9VrUOZ-psdoK9jUOaQoZ89mJyGce6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4.1 Flash به صورت رایگان
💥
🆓
این نسخه ۲ روز پیش منتشر شده است. دارای ۱ میلیون توکن متن، قابلیت‌های بصری پیشرفته و کیفیت مناسب برای استفاده در سیستم‌های هوشمند است.
🚀
🔺
رایگان به صورت روزانه
🔺
پنجره متن با ظرفیت ۱ میلیون توکن
🔺
سهم استفاده روزانه هر روز ریست می‌شود.
هنوز مشخص نیست که این سرویس چه مدت به صورت رایگان باقی خواهد ماند.
‼️
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzVesJjOn6zQYd-exEpOIGTWldgJfowzwI3EA7p07VYqYx_1Px6H3RZDZvt-69jMikglVhAb_hZXxpMsybHnuol_WjdFg_sSbTme9m3CgutA5DzM6y9AGVUX84vxYvFGd4Huu8ANPK7hL3uvvVIBUxDQZ6ua2R-x_f12ub9CvvMu57RVKI5tQItPhKxh-gGVZLeYAQB9wDqwnKAoLcKgO0NZzEIfzp26-06jlrHPgmCA60SwHdJZ2HyEcc5aWd3wJ5xzEEv3ChXd_LhsPg-iw6qaFTI5cwAN8Lxyr24eMwJxKP8pX3BqpXrHYeU6oEV9Wi1RQigI8lonISjcm4Xn2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
با این سایت میتونید 5 دلار اعتبار رایگان برای بهترین مدل ها دریافت کنید همچنین این سایت 3 مدل کاملا رایگان بهتون میده
💵
😎
Kimi K3 | Deepseek 4 Flash | Mimo 2.5
✅
📌
Base URL: https://tokenharbor.ai/v1  با جیمیل…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUGy5irWEJtIlHexUcUhKdVts655-KKsTtlbglt_8AwGrjGi67YGIh9hSMI63mTM1YFTriwfu2CfTbAJzsN3iNe56CKq14xuwXCRgP0Vu4z3NKurpjd8ecQFncDwR9pPDjXIDe2DO88VKNuMwE-LstUzJDIBE9Zpdc8GK6A21A0qfshmq2k3zumgOriRm3ut8f83IME5_o8MCrlWJTkTSkNIlF_-i8pLRBgvg_yHJL-VnGfvUpqWTi0N1lELC0U6_GMYV4wHRTFIKy5Wi2ny1YwB9gEXpu0V-Az4HuGX1vc70RhN_XWbTIUTBWpBhY-YfpMNYc0GxQa95SsBjSEqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqSDzrKUEFzI4QDgaXsY5krrVOeSTqDhGHt5KlF1l3IqSPnWBB0pvdmw9n8kdBv4eE14pOIfaY6iCm7VtMCdVBIQtuRjWsN1EnRBZ2v80_6nQTxxx8h8PesaRS53dIN73HhmmfKpgct2OFVYJveGSgYGIFdLpUAnsCD2zyCEyEUikCWcZCCuc4fFkysCE4iW7VJu_KUQhKsh2mWyJgxOAcFVtjNU4RpGeTb8Z_h0sk9ItRJwlfBI2n7EgHijbndfjoelO46AHWhWgnctEJ_LNe5ZWbyrNbtNwhbiQsrcZVtWj0QVTeRdQXfKo-V6z-TnOU2-xDXg-WQrKkj6CZxrOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">150 میلیون توکن رایگان برای مدل های زیر
💥
🆓
GLM 5.3 Flash | Qwen 3.8 Flash | Mimo 2.5 | GLM 5.3 | Hy 3 | Qwen3.8 27b
✅
وارد سایت زیر بشید با جیمیل ثبت نام کنید سپس از طریق منو 50 میلیون توکن امروز هم دریافت کنید
✅
‼️
نکته :
از مدل های با پسوند Free استفاده کنید و احتمالا این دسترسی شامل محدودیت تعداد ریکوئست در دقیقه باشه ، همچنین ممکن هست هر لحظه اشتراک رایگان بپره
📌
Base URL :
https://kiraai.vn/api/v1
🔗
لینک ثبت نام
🔗
لینک گرفتن کلید
🔗
لینک دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🧠
پروژه OXYGPT — یه ربات تلگرامی که هوش مصنوعی رو حسابی جدی گرفته!
بچه‌ها این صرفاً یه ربات چت نیست، یه اکوسیستم کامل AI روی تلگرامه: چند مدل هوش مصنوعی، مربی‌های حرفه‌ای تریدینگ، sandbox واقعی لینوکس، اخبار فارکس زنده و داشبورد مدیریتی. خوراک کسایی که می‌خوان یه بات production-grade بسازن نه یه دمو دو ساعته
🔥
↔
مسیریابی چند-مدلی AI
: استخر کلید Gemini + سرویس‌های سازگار با OpenAI، round-robin می‌چرخن و روی خطای 429/503 خودشون فالبک می‌زنن
🪟
پنجره‌های مکالمه مجزا
: هر کاربر تا ۵ چت جدا با تاریخچه و state خودش می‌تونه باز نگه‌داره
🧙‍♂️
مربی‌های تریدینگ (Persona)
: چهار شخصیت آماده (ICT، Quarterly Theory، Matrix/369، Price Action) با یه دستور سریع صدا زده می‌شن
📓
ژورنال معاملات
: ثبت و پیگیری ترید‌ها با قالب‌های اختصاصی، مستقیم داخل تلگرام
📰
اخبار فارکس زنده
: رویدادهای پرتأثیر Forex Factory رو با تحلیل کوتاه AI نشون میده
🖥️
قابلیت Sandbox واقعی لینوکس (E2B)
: مدل می‌تونه کد اجرا کنه، پکیج نصب کنه، ریپو کلون کنه و فایل بفرسته/بگیره
🔑
قابلیت BYOK
: کلید API خودتو وصل کن، از محدودیت پیام و quota عمومی بی‌نیاز شو
👁
مانیتورینگ کانال با AI
: کانال‌های تلگرام رو زیر نظر می‌گیره و پست‌های مهم رو تحلیل و تحویل میده
💡
دیپلوی با یه دستور روی Docker/Railway انجام میشه، و هر ۵ ساعت یه بک‌آپ خودکار از کل دیتابیس‌ها زیپ و برات تو تلگرام ارسال میشه — دیگه نگران از دست رفتن دیتا نباش.
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdzFlOXwZQrlGIfBE-zYHxVf-3-ENF7RqkJcwvEiv_e6nQrQbkKGyd9faV3gMcrcM6qqxgPhKbWQoq_p5EsO2618dsODVbleKipRoGasE-jQnnh1y4GI9H4lQaLN8OJ0TH0_AnXepolkcKi-CMTvl2qnkPlRL-xV1CIsOjIhmRG1atlLFUM3nxNv9QpjYDhlc0xEZ2z604Boe3Prej0xJwUcer2m3lOlGBaiUPf5wG7ACdV1WRQ2fIbQINaGNCZqYYtWhS7QH-GtJiGorhBZvteF9lGNF5sXle5AZf4j-IQ4Vs5iecE6iScxyjjorz4FkEL3rLhbjbk25B8Ki5HgAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e13K5Ag_3m6yAzafIH_jgApXcrJGIlK3jNUQZ6pCf3tjAYOJgkRFPdDB6OzO5QsfP79PRLRyGdRLOe42euflMP_tg6hQ8v0oizTHXRuxdy9inQm4y3faCvqIGDwkcAGkNLOsR-ER2GDpsBZJEFKZA4GQhuNCmNnu98zUBRDO_GikQZU8rTUAua5QOF5JVjJGZzFjNcq1NAYww1wHWwVWHjFypUkrjAa5eGf4eHBsXe0oDPIhIkvJ1Pct-cI6eVgA59vuVtjbNKr_FJSBZFiad135mkgGzmzRxDzDROJFV26FQUYwYdkJWjO5K_EfqVJRkOYFvno4toLP-CfGVr927g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزانه 1 میلیون توکن رایگان برای مدل‌های زیر
💥
🆓
Gemini 3.8 flash | Muse Spark 1.3 |GLM 5.3 Flash | Deepseek V4 Flash | Deepseek V4 Pro | GPT 5.6 Luna | Gemini 3.1 pro
✅
وارد سایت زیر بشید و ثبت نام کنید و یک کلید دریافت کنید
✅
‼️
نکته :
با هر آیپی ۱ بار میشه ثبت نام کرد اگه میخواید چند اکانت بسازید هربار آیپی هارو تعویض کنید
📌
Base URL :
https://apinex.bond/v1
🔗
لینک سایت
🔗
گرفتن کلید
🔗
دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiGu0s2Ej9z7_WmXR8e-Y958DlWxr8fArzwwTjrwfQmT-zw5RC2v30owPZbH1lbeuaHwg8woeAyMaAbWCZm9ZM9tJG8XHGDyTANgslYOUrBYaqUrk6AbhtaQBL_f9jn_F9zCU9VbaRmtJ3ZS5uaX86Oe6wa_r044lkJsJXYUkpvu8TCjYeV7Zo3_Aj_XwemJ5VSbrJQjheTwSTf8L9G-cOQkL0Ks8E-W7rUziaGfacjOp3L0sjIp4BdJ5g3wzETjg6rq8YDFDzBz-ylkEih6TeQ-f1jR2Ne4niNPodsPyluKqkaXQiid41cEHqn2VkOUn8sRRemT2ADnSj89EI3ZvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 میلیون توکن رایگان 1 ساله
💥
🆓
Fable 5 | Opus 5 | GPT 5.6 Sol | Grok 4.6 | GLM 5.3 | Qwen 3.8 max | Kimi K3 | Deepseek V4 Pro 0813
✅
برید داخل
این سایت
ثبت نام کنید
حالا برید داخل
این بخش
پلن سالانه رو انتخاب کنید و این کد تخفیف رو بزنید :
DEVWEEK
بعد اینکه تخفیف اعمال شد تایید کنید و تمام ، یک api بگیرید و استفاده کنید
✅
📌
Base URL :
https://codecraftapi.com/v1
اکثر مدل های جهان رو داره میتونید از Playground چک کنید ، چون سایت شلوغی هست طول میکشه تا ریکوئست ها جواب بدن
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnQGGkztRo5dzKyHAdBt-WKixFnXOTQiNmdwwrVP3xK96ptJo7t3Pj1QzrYyJSEggcaw8VL5VAMVaSTCi2syCxsFyIkfIPIcj_t-yGTuMs9IckNQdsQhgsxC5NzqJVBJL9g6XxLQtUfKvyLyLk1J9WpobQHHXmZdOqcf5p9EIQOUjumCNMXKJm02GJFMJ1P6GkrTAaeHfH_JdyNDSX1_unkimvhtqnBMIXxWv_qBqoA4HC3kZKkvZb8_h5JFL6AnyaSOzzBQEerBl3MUMAszMBPqVNW389iBev5jDzWyRKag5zxW4WDG_S8vSaDH2eD7pLFNYR5onVq6dDoT2whuKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
تغییر ریجن گوگل در ۳۰ ثانیه
⏱️
با فیلتر شکن کشور مقصد یکم برین تو گوگل بچرخین،
بعد به لینک زیر بروید، ریجن را انتخاب کنید، دلیل تغییر را بنویسید و ارسال کنید.
https://policies.google.com/country-association-form
حداکثر تا ۲ ساعت ریجن به جایی که میخواهید عوض می‌شود و ایمیلش میاد
✅
بعدش میتونین به راحتی از antigravity و سرویس های دیگه گوگل استفاده کنین.
از توجهتان ممنونم
🙏
✈️
@ArchiveTell
|
#method</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">📌
Model :
gpt-6-astra
📌
Base URL :
https://api.eirouter.ai/openai/v1
sk-e76d452dff7eccef0a1b6bde4f8262c7f628f4f2991676cf3188d0cb68023b3f
sk-778bbaffd07397311260074542e405ab11833bf458e0250363ac1afd7db02297
sk-b028d3f23d96d0b0fc96a24985164437fcaf272276caf33548a664a0df424dc1
sk-1f153c31ccd2448b30c2f56287d5dc8fcc8ddafa579d12a797450321d86e9d29
sk-3334618935b09f67a70938d3379971e3ad350fec1154008d3abbaa07565c00b3
sk-242582ef9fc5e53351eb2fd67178b83033a450a61d048cf66be6aacf98a9e2bc
sk-db726cb7cc5b14160f9d8900455fcd34fd56cbb94f3afac65494a5161eee35b6
sk-7e85fc089be2d58f76c236c8ae1efc6062f68a459bdc9f87bcbe896c2d7307e2
sk-cca857a86f2c62b5d704f2234ed5632f8ef4dfbfcc0da509fe0e021516a0406d
sk-3c3eb497a104328775de0ddb333c7c8d596c20a89e25bbe7e204318f35e2b050
موجودی هر کلید هست 5 دلار ولی نکته اینجاست توی سایت قیمت هر یک میلیون توکن این مدل هست 1 دلار
😁
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=JYmy36IMjvdJE51TiEah0NkeDjwyU_9wkoCElke7qxTS0jVWaIDYKhrzZFLmfLKN-qAjiqPxMyCtOkrsNt9q3JZa0IGtdKvyqHY8r-IEiOiN5-_ChqePJ0DbEE2dzd_lCWUPHJw0R7TiNRf81d0BWpS10dbDUCHpjbLauDCfUKTF7dbTeS2Bhx2N_nhAoFljRQN-rFRBRTRjxGjbYcOIKcbw6fhLQ5Ou2_u-Cf3r0OHKHDK-bpqjIAV6EnvK5QF4jgpuQR3PEopNHEJRfmWqV7tWQb8vhcfXP4Ba4-k9Fw0vgz-6JIA63vLBvxUyXKoySzDb4IhRPhDk8udmVu6F-q-hRARbrFQ2zHbKUH7BdA1JuFTt4jWELyoBEMRpgVN3H0EHNAkfCcQV-1Nzco6Vcu6xt02K3DJHnvTVCxDvEIRC53xjAd_bH2GbaGWj-IcUs5ShNwBGD9FaU2xmOj0M9yK1XDOmjvR0LzD1Yg00Cn0hr8gCO8ueH1_X1zkxZhyQOwhhpKRD8JIahrWXFNQqR5atgH-NyWPbjkpBrOo8TaYdHDyBj3KTXANHi5T40jhFp38isN93Y3qClr62W3k4vPchqD5HnO1OG4wU73kNmzdsSJc68eR59b9kgAqgt4LbdeJy3QUq3rRgEOmXBHLtzzPNgWn4BF__YOAHcaLljSY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=JYmy36IMjvdJE51TiEah0NkeDjwyU_9wkoCElke7qxTS0jVWaIDYKhrzZFLmfLKN-qAjiqPxMyCtOkrsNt9q3JZa0IGtdKvyqHY8r-IEiOiN5-_ChqePJ0DbEE2dzd_lCWUPHJw0R7TiNRf81d0BWpS10dbDUCHpjbLauDCfUKTF7dbTeS2Bhx2N_nhAoFljRQN-rFRBRTRjxGjbYcOIKcbw6fhLQ5Ou2_u-Cf3r0OHKHDK-bpqjIAV6EnvK5QF4jgpuQR3PEopNHEJRfmWqV7tWQb8vhcfXP4Ba4-k9Fw0vgz-6JIA63vLBvxUyXKoySzDb4IhRPhDk8udmVu6F-q-hRARbrFQ2zHbKUH7BdA1JuFTt4jWELyoBEMRpgVN3H0EHNAkfCcQV-1Nzco6Vcu6xt02K3DJHnvTVCxDvEIRC53xjAd_bH2GbaGWj-IcUs5ShNwBGD9FaU2xmOj0M9yK1XDOmjvR0LzD1Yg00Cn0hr8gCO8ueH1_X1zkxZhyQOwhhpKRD8JIahrWXFNQqR5atgH-NyWPbjkpBrOo8TaYdHDyBj3KTXANHi5T40jhFp38isN93Y3qClr62W3k4vPchqD5HnO1OG4wU73kNmzdsSJc68eR59b9kgAqgt4LbdeJy3QUq3rRgEOmXBHLtzzPNgWn4BF__YOAHcaLljSY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده:
جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch:
کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی خودش اونو به آرت نهایی تبدیل کنه
🎯
ادیت موضعی دقیق:
امکان هایلایت و تغییر دادن فقط یک نقطه خاص از عکس، بدون دست‌خوردن بقیه جزئیات تصویر
💡
نکته دسترسی:
تعدادی تمپلیت آماده هم برای تسریع کار اضافه شده و این مدل در حال حاضر به‌صورت عمومی داره برای تمام کاربران فعال میشه؛ حتماً حسابتون رو چک کنید.
🔗
ورود و تست در وب‌سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⭐️
۶ پلتفرم برای تست رایگان GPT-6 Astra
دسترسی مستقیم و استفاده از API مدل‌های پرچمدار و سنگینی مثل GPT-6 Astra معمولاً هزینه بالایی داره و اگه حواستون نباشه خیلی سریع اعتبارتون رو صفر می‌کنه!
💸
با این حال، یه سری پلتفرم کاربردی وجود دارند که اعتبار (Credit) اولیه یا سهمیه تست رایگان می‌دن تا بدون نیاز به پرداخت، بتونید قدرت این مدل رو توی چت، کدنویسی، پردازش تصویر یا ساخت ایجنت بسنجید:
1⃣
پلتفرم Vercel AI Gateway
یکی از مطمئن‌ترین گزینه‌ها به‌خصوص برای دولوپرها. این سرویس هر ۳۰ روز حدود
۵ دلار کردیت AI رایگان
به کاربرانی که حساب فعال دارند میده. محیط Playground، پشتیبانی از ایجنت‌ها و سازگاری کامل با فرمت OpenAI API داره و برای ادغام با پروژه‌های شخصی عالیه.
2⃣
پلتفرم Brainbase
اگر دنبال کدنویسی پیشرفته، تحلیل ریپوزیتوری و ایجنت‌های خودکار هستید، اینجا فوق‌العاده‌ست. بعد از ثبت‌نام اولیه،
۲۵ دلار کردیت رایگان بدون نیاز به کارت اعتباری
دریافت می‌کنید تا بتونید تسک‌های سنگین برنامه‌نویسی و اتوماسیون رو با مدل پیش ببرید.
3⃣
ابزار Roboflow Playground
بهترین جا برای محک زدن قابلیت‌های بینایی ماشین و پردازش تصویر (Vision). توی این محیط می‌تونید اسکرین‌شات‌ها، نمودارها و تصاویر پیچیده رو بدون نیاز به کلید API آپلود کنید و دقت تحلیل مدل رو با بقیه ابزارها مقایسه کنید.
4⃣
سرویس CometAPI
اگه مدل رو برای اتصال به ربات تلگرام، افزونه یا اپلیکیشن خودتون می‌خواید، این سرویس کار رو راحت کرده. بعد از ثبت‌نام کردیت رایگان میده و چون ساختارش دقیقاً مشابه API استاندارد اوپن‌ای‌آی هست، بدون تغییرات عجیب غریب توی زیرساخت کارتون راه می‌افته.
5⃣
پلتفرم Imaginode
یک فضای همه‌فن‌حریف با محیط تعاملی Canvas، چت، API و ادغام با پروتکل‌های MCP. بدون کارت بانکی کردیت اولیه میده و هر پیام با این مدل حدود ۱۲ کردیت مصرف می‌کنه؛ بنابراین برای ساخت سناریوهای متصل‌کننده متن، تصویر و اتوماسیون حسابی جوابه.
6⃣
سایت Vibany
ساده‌ترین و دم‌دستی‌ترین راه برای تست تفریحی و سریع. در بدو ورود حدود ۳۰۰ کردیت رایگان می‌گیرید و هر بار اجرای مدل حدود ۱۰۰ کردیت کم می‌کنه. یعنی حداقل ۳ الی ۴ تا پرامپت عمیق و جدی می‌تونید بهش بدید تا خروجی رو با مدل‌های قبلی مقایسه کنید.
✈️
@ArchiveTell
|
#AI
#API</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🧠
شیائومی وارد میدان ایجنت‌ها شد؛ معرفی دستیار همه‌کاره MiMo Desktop!
بچه‌ها شیائومی رسماً وارد قلمرو ایجنت‌های سیستمی شده و یه دستیار دسکتاپی معرفی کرده که مثل ترکیب Codex و قابلیت‌های کنترل کامپیوتر Claude عمل می‌کنه؛ این ابزار خوراک خودکارسازی کارهای روزمره شماست.
🖥
کنترل کامل دسکتاپ و وب:
اجرای خودکار تسک‌ها، کلیک، تایپ، کار با فایل‌ها، پر کردن فرم‌ها و امکان ضبط و اجرای مجدد فعالیت‌ها (Record & Replay)
⚡️
پیش‌نمایش تعاملی و ادیت موضعی:
رندر زنده سایت‌ها، گیم‌ها و داشبوردها با قابلیت هایلایت کردن یک بخش و بازنویسیِ انحصاری همان قسمت
🧠
دسترسی رایگان به مدل‌های نسل بعد:
بهره‌مندی تسترها از دو مدل معرفی‌نشده و پرچم‌دار MiMo-X-Pro-Preview و MiMo-X-Flash-Preview
💾
کشینگ فوق‌سریع تا ۹۹٪:
فناوری بهینه‌سازی توکن برای تغییرات مداوم پروژه‌ها جهت جلوگیری از هزینه‌های اضافی
💡
نحوه ثبت‌نام در نسخه بتا:
ظرفیت بتا کاملاً محدوده و اولویت با کاربران فعال اکوسیستم MiMo Open Platform خواهد بود؛ فرم درخواست رو پر کنید تا لینک دسترسی و مدل‌های جدید زودتر براتون فعال بشه.
🔗
فرم ثبت‌نام در نسخه بتا
🔗
صفحه رسمی معرفی
🔗
صفحه رسمی قابلیت ها
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=QnpUTz9jOu3ompgh7aL8-IQtB_HhX9ZcWzUGrHqQAIgxFhbmxa0zItUXK4LFa-9cOHtv0hnz7cDHmM0qdA-1VHiONVytEe3rzCVuLjQpUvx0GbMu8bzxti2xP0S-9rXnrxPxIPGrg6uk3mt5wjVxjN0Ankvfc7xxs9a9Hu0RipvLkh_pVw3m5TvUfJF5iUrFKCdvNRVfoY18im5kd_p7yjw2pgirVDPaj2d_jQ5jwAFNxrGcSf9K5DUmwEETWCRdnOoirHwIerXYRYsfNZgyiHhDap7dNFxny993oWv4wSA-jrJUHun0zTNzDw4WJeiLOH-sLUVt5xLUQbbjS27HsL0g3KCyFWXgJ9i_s8Ftzolg8cqQ1b2FqpMiQCamg2BnW5_iwqnfpX0yHTKp3rRIl_tiu53iiyWsV4nVPpfzHCdHyXBI6vhPGsLyUe2WgqNcxajhuORJIYzbj7yfv4sNMwDXERRxZh6GWBR4szkjTIKVCjhkrOhBljDOMnegSdwaY4t1AtauLwp3CkfN7_z21mjLMDRTU1b-FD-BPqU-mMUt2D7SBngT_QQ4KwCqLeozagIdwV7dWQqIk2dZPpTZpni9vZw6J-w-UBq7GwV7vOti9i-d_RjZJ_PPFrAHzcXx0Eny7A2iSuFlkecGulFLDpd7BopB-YY4BLp6HScdems" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=QnpUTz9jOu3ompgh7aL8-IQtB_HhX9ZcWzUGrHqQAIgxFhbmxa0zItUXK4LFa-9cOHtv0hnz7cDHmM0qdA-1VHiONVytEe3rzCVuLjQpUvx0GbMu8bzxti2xP0S-9rXnrxPxIPGrg6uk3mt5wjVxjN0Ankvfc7xxs9a9Hu0RipvLkh_pVw3m5TvUfJF5iUrFKCdvNRVfoY18im5kd_p7yjw2pgirVDPaj2d_jQ5jwAFNxrGcSf9K5DUmwEETWCRdnOoirHwIerXYRYsfNZgyiHhDap7dNFxny993oWv4wSA-jrJUHun0zTNzDw4WJeiLOH-sLUVt5xLUQbbjS27HsL0g3KCyFWXgJ9i_s8Ftzolg8cqQ1b2FqpMiQCamg2BnW5_iwqnfpX0yHTKp3rRIl_tiu53iiyWsV4nVPpfzHCdHyXBI6vhPGsLyUe2WgqNcxajhuORJIYzbj7yfv4sNMwDXERRxZh6GWBR4szkjTIKVCjhkrOhBljDOMnegSdwaY4t1AtauLwp3CkfN7_z21mjLMDRTU1b-FD-BPqU-mMUt2D7SBngT_QQ4KwCqLeozagIdwV7dWQqIk2dZPpTZpni9vZw6J-w-UBq7GwV7vOti9i-d_RjZJ_PPFrAHzcXx0Eny7A2iSuFlkecGulFLDpd7BopB-YY4BLp6HScdems" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آرشیو ۱۵۰ پرامپت آماده برای خلق ویدیوهای سینمایی با AI!
بچه‌ها اگه با هوش مصنوعی ویدیو می‌سازید ولی خروجی‌ها تخت و مصنوعی میشن، این کالکشن خفن خوراکتونه. یه دیتابیس آماده از ۱۵۰ پرامپت تست‌شده که دقیقاً دستور زبان کارگردانی و سینمایی رو به مدل تزریق می‌کنه.
🎥
کنترل دقیق نور و دوربین:
پرامپت‌های تخصصی برای مدیریت لنز، زوایای حرکت دوربین، نورپردازی و دکوپاژ
🎞
همراه با نمونه ویدیویی:
هر دستور شامل پیش‌نمایش رندر واقعی است تا قبل از خرج توکن، خروجی کار رو ببینید
🎭
تنوع ژانر و اتمسفر:
پوشش کامل انواع سبک‌ها، سناریوها، اکت کاراکترها و فضاسازی‌های سینمایی
💡
نکته استفاده:
تمام پرامپت‌ها آماده Copy/Paste هستند؛ فقط کافیه کپی‌شون کنید داخل ابزارهایی مثل Runway ،Kling یا Luma و المان‌ها یا کاراکتر مدنظرتون رو با کلمات کلیدی دلخواه جایگزین کنید.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oep-NK08y9f2vkezpCZKTKrMtd1IIJ9m0bgb-Use5ypivXhM9sctestBDkermxSlTwlyWiJDaazdcgjmDRND1oK4CMAHwIQ_8LdP3Msz59x9oTpCUX6SQ9K6f6T3lQnnGFDCrAxrM8fR3NcPxJ50ZrO7q6ScsoEqwTJlB-qPDtGSj2juPEgMSC0LL_WwkdMWh_z0kivSwOhwS9c0-az2hS0mBI7giqeMXxT-YTIPRSb8UljDEvUPi1cYHpbVer4lh_9ZqX17kSEq6WLLTJ2-QEfI-cLX-HTOtj2w7Zud-DUlYVhEWWSJgnJRuGqEyrT-5Qk9m8DYpaoWSUluXI71oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مایکروسافت آفیس رسماً مرخص شد؛ معرفی غول اوپن‌سورس GenOffice!
بچه‌ها اگه از خرید لایسنس آفیس یا برنامه‌های سنگین خسته شدید، این پروژه جدید خوراکتونه. یک جایگزین کاملاً رایگان و متن‌باز برای مایکروسافت آفیس که ایجنت‌های هوش مصنوعی رو مستقیماً آورده داخل اسناد، جداول و ارائه‌هاتون.
📝
پکیج کامل و همه‌کاره:
مدیریت بی‌دردسر داکیومنت‌ها، شیت‌های آماری، ساخت اسلاید و کار با PDF بدون نیاز به ابزارهای متفرقه
🤖
ایجنت‌های تحلیل‌گر:
اتصال مستقیم به مدل‌های قدرتمندی مثل DeepSeek ،Claude و Kimi برای تحلیل داده، نگارش متن و تولید محتوا
💻
آزاد و مولتی‌پلتفرم:
پشتیبانی رسمی و نیتیو از مک، ویندوز و لینوکس بدون نیاز به پرداخت حتی یک ریال
💡
نکته جالب توسعه:
جالبه بدونید نسخه اولیه این پروژه رو فقط یک مهندس، توی مدت یک هفته و با سوزوندن ۱۰ هزار دلار توکن هوش مصنوعی جمع کرده! ریپو تازه پابلیک شده و سرعت استقبال ازش وحشتناک بالاست.
🔗
گیت‌هاب GenOffice
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=vmCb5V61EED1sKMD35FZD76cE9HhrGyvV52cXPMq3fDmJupgXmFj1UpdVQ_SABEjOqnOmf9phnkol4l2f_Qx1WiYRbQUSdhh8ISvlBvLFrcynImJKpHkEocT3Z-6vRbT1TNMbMK9-w9VFvgD6TeoFjpb5Gq0LvCdPki3jJXqZK6UWU1u707vxs5PloMwHwvCZGi259VakenWzUHmfOddSkykaXJEwmjasemxZaFOkRtVz2hm4o9UqCWxV4Kjya_g144Z5JzwdjYPOSMOURKw-6839c22pp44Cg1LAc9mlIrXEiNe3P7B6MB-SUUsEjRI3OpKH0WXM_wgPVQNKV6lmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=vmCb5V61EED1sKMD35FZD76cE9HhrGyvV52cXPMq3fDmJupgXmFj1UpdVQ_SABEjOqnOmf9phnkol4l2f_Qx1WiYRbQUSdhh8ISvlBvLFrcynImJKpHkEocT3Z-6vRbT1TNMbMK9-w9VFvgD6TeoFjpb5Gq0LvCdPki3jJXqZK6UWU1u707vxs5PloMwHwvCZGi259VakenWzUHmfOddSkykaXJEwmjasemxZaFOkRtVz2hm4o9UqCWxV4Kjya_g144Z5JzwdjYPOSMOURKw-6839c22pp44Cg1LAc9mlIrXEiNe3P7B6MB-SUUsEjRI3OpKH0WXM_wgPVQNKV6lmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت خفن: تبدیل هوش مصنوعی Astra به یک بات بازی‌ساز حرفه‌ای!
🎮
🔥
داستان از این قراره که یه دولوپر، Astra رو طوری شخصی‌سازی کرده که عملاً تبدیل شده به یه ماشین بازی‌سازی. اصلاً هم شوخی یا بازی‌های دوبعدی و پیکسلی دم‌دستی نیست؛ کیفیت کار در حدیه که باورتون نمیشه کل این دموی سه‌بعدی خفن فقط توی
یک ساعت
جمع شده!
👀
⏱
سازوکارش چطوریه؟
🛠
همه‌چیز با یه اسکیل (Skill) جلو میره:
* اول Astra باهاتون گپ می‌زنه و از بین ایده‌هاتون، کانسپت اون بازی رویایی که تو ذهنتونه رو درمیاره.
* بعد طبق همون پلن، توی ده‌ها دور آزمون و خطا پروژه رو قدم‌به‌قدم کدنویسی می‌کنه و می‌سازه.
پرامپت استفاده‌شده برای ساخت این دمو:
📝
Prompt (high effort): /dream-loop Build me a graphics demo: isometric camera, voxel-ish art style with realistic shading and reflective wet floors, a character in an interesting scene. Fantasy setting (think Elden Ring, Diablo). Three.js in browser, >60fps. Don't download assets. Time limit of 1 hour. Controls: click to move the character, camera lazy-follows; drag to rotate camera; scroll to zoom in/out. No gameplay for now. World should feel alive: motion, animations, subtle environmental behaviors. Area around player should look expansive, but only allow movement in a limited space. No need to confirm the art with me or ask questions, just go!
🔗
دموی بازی توی مرورگر
🔗
خود اسکیل Astra
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZy0NihTEZS4Ei7nTN69qD_q7_QbgGhq0XEk2krOLnLqpGPVgmYyhJai9MlKLVgsO5yxpNna_2MWIExuUPOgEM-UsjTiQP3jx0DQiVSocxM4i2JJtrsaS97_UmUxe3WZHZP_rObjcipndfQc-gA-W23bqFABAus5VbGn3mQ5HysO5T_ZmDKiaZcHWMy0oxip-0vmNQRkf2i2_I9BmPdE7AasGeQkUwTh4Z3ArpNSj-yjkOtC1LFBxWcp54bdCQi_ckP3yc1qhn7c9oqO1wIFVoWBmhTwwyuCGT9xbYnnMpYhYIjpetWzmud7dIE3pAkfI00rrEy34deREoLn1BoFdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
باز کردن بی‌دردسر فایل‌های آفیس روی اندروید با OpenDocument!
بچه‌ها اگه فایل‌های متنی یا اداری دارید و دوست ندارید برای باز کردنشون تو سرورهای ابری آپلود بشن، این اپ خوراکتونه. تمام اسناد OpenOffice و LibreOffice رو کاملاً آفلاین، سریع و بدون نیاز به اکانت باز می‌کنه.
📁
پشتیبانی کامل از فرمت‌ها:
خواندن بی‌نقص ODT ،ODS ،ODP در کنار فایل‌های رایج DOCX ،XLSX ،PPTX و حتی PDF
🔒
حریم خصوصی واقعی:
پردازش کاملاً لوکال، بدون اتصال به اینترنت، بدون ترکرهای تبلیغاتی و بدون نیاز به ثبت‌نام
⚡️
سبک، امن و باسابقه:
یکی از قدیمی‌ترین و پایدارترین پروژه‌های متن‌باز اندروید (فعال از سال ۲۰۱۰)
💡
نکته کاربردی:
بهترین گزینه برای کسایی که با فایل‌های کاری و اسناد حساس سر و کار دارند؛ با خیال راحت می‌تونید حتی در حالت Airplane Mode به تمام داکیومنت‌هاتون دسترسی داشته باشید.
🔗
گیت‌هاب پروژه
🔗
وب‌سایت رسمی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=VRGW70p6p-DrWQLApPAAXVz3UyQ6gww_XohhVUrPFFTVZq69uGj6iQVbnOCfNGM700A_JVcop8tbB4fkl4t9OLobOOAUl9wHgUCbLDSx-eKP5GtQLPusK6pGqev5nPy8smW_TnuyhmgPt7B1WHcgwLqerYKknF-lLTJFPlpV4kkvoAipphdzktOJMwHJsVHHzp1jm7d7xjyaT0aqEyxMeH4ewJggEt5OTMj3p_jFU_1RpWh_o4RJKkUJr-GVUc0Qz71mrb8NXjOkabQ_cKVSNzBMdVFzosSFyzvXWxTbHFyRC2kRWEveZzY6SfVudtE2fDBlMCM4W2BVfKEUbNd_PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=VRGW70p6p-DrWQLApPAAXVz3UyQ6gww_XohhVUrPFFTVZq69uGj6iQVbnOCfNGM700A_JVcop8tbB4fkl4t9OLobOOAUl9wHgUCbLDSx-eKP5GtQLPusK6pGqev5nPy8smW_TnuyhmgPt7B1WHcgwLqerYKknF-lLTJFPlpV4kkvoAipphdzktOJMwHJsVHHzp1jm7d7xjyaT0aqEyxMeH4ewJggEt5OTMj3p_jFU_1RpWh_o4RJKkUJr-GVUc0Qz71mrb8NXjOkabQ_cKVSNzBMdVFzosSFyzvXWxTbHFyRC2kRWEveZzY6SfVudtE2fDBlMCM4W2BVfKEUbNd_PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📍
با GeoSpy لوکیشن دقیق هر عکسی رو دربیار!
بچه‌ها اگه دنبال لوکیشن یه عکس رندومید یا اهل چالش‌های OSINT و ژئوگسرید، این هوش مصنوعی خوراکتونه. حتی اگه متادیتا (EXIF) پاک شده باشه، از روی خط‌کشی خیابون، گیاهان، معماری و تیر چراغ‌برق مختصات رو براتون پیدا می‌کنه.
🌎
جست‌وجوی جهانی (Global):
پیدا کردن چند تا از محتمل‌ترین کشورهای دنیا حتی از روی اسکرین‌شات یا عکس کراپ‌شده
🏙
مود شهری (City Search):
اگه شهر مشخص باشه، با عکس‌های خیابانی مچ می‌کنه و آدرس دقیق پلاک و خیابون رو میده
📸
تحلیل چند زاویه‌ای:
امکان آپلود تا ۴ عکس از یک لوکیشن برای بالا بردن نجومیِ دقتِ حدس
💡
نکته طلایی:
کیفیت عکس اصلاً مهم نیست؛ این ابزار حتی فرم شاخه درختا یا مدل آسفالت رو می‌فهمه! موقع ثبت‌نام اولیه هم یه سهمیه سرچ رایگان بهتون میده تا تستش کنید.
🔗
وب‌سایت ابزار
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkRfaoEsAjl8vegAVWaxiPRC6l79AA0Iu7sFNLXBaB2Z6V5sQ5JAxj7ZPTWRolwKlUdaKTAQPyyiOuwiTq1GWLE71UYuFwwByGErdu8njGJ-xRYsEiW9ZoIv_FI6o6g7u4aW0LEeZdQq5e0KhT9mfov9bBF2vOer6jwDdw4PH5nIZDHHZ3YV-sIwKC-fUcrXLn6i2CpwOYS5gqUbOlr9XuHoraJlBl0ru9zY759ujrSiXQlsNc5hePEb8hUiKI4Mw86MsmCMZLX7KemjMkcblF5pBviEMyPaMMctHcW_in7_KIobng0F4LHsLTbi0Lco52n0gw1Tni5B9ax9JFzlOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕸
با SpiderFoot ردپای دیجیتال هر چیزی رو توی اینترنت بیرون بکش!
بچه‌ها اگه تو حوزه امنیت، تست نفوذ یا اوسیانت (OSINT) کار می‌کنید، این ابزار دقیقاً خوراکتونه. اسپایدرفوت یه ابزار متن‌باز و بی‌رحمه که کل سطح وب رو شخم می‌زنه تا تمام ردپاهای دیجیتال و آسیب‌پذیری‌های یک هدف رو دربیاره.
🎯
تارگت‌های همه‌جانبه:
جست‌وجو بر اساس شماره تلفن، ایمیل، آیدی توییتر و تلگرام، نام، IP و دامنه‌ها
🤖
اسکن تمام‌خودکار:
جمع‌آوری آنی داده‌ها از بیش از ۱۰۰ منبع اطلاعاتی بدون نیاز به سرچ دستی
📊
نقشه ارتباطات بصری:
تحلیل داده‌ها و نمایش گراف‌های دیداری از اطلاعات لو رفته و پیوندهای مخفی
💡
نکته و اجرای سریع:
راحت‌ترین راه اجرا با داکره؛ کافیه دستور docker run -p 5001:5001 spiderfoot رو بزنید و پنل تحت وب رو باز کنید. (یادتون نره، فقط تست امنیتی قانونی و اهداف آموزشی!)
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOFBlGx3nC7QP7oguACFmb8lnGy3DU2myUhubInPpCb523RC240BCCUUri_cWnLYxMushmebJaTAbQSyJYwLIB_xDOMFk2wsSjgwm_Xe8pokqPP90TlLYzHguNdeDFbFzuO87EhhQIE5ey5U4j59NHZ-0yCKk2ZossyBf2gkjn3uHIcspAewghqN4nEwkKecSKen382r5sGYVK1YAE4LpqXYd7Af8uKcH1gGLrNnQaG-X1P-thMeZaWw-tKBpavVkifS9Qya-zjeqJ1N8KoqU_XW5E_qKtA4-Z4XSGRc1W0DDmBT_i1g07mZmeHDK39nbNsYPQVPqN9g7gW-BuPbUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توکن‌های نامحدود برای Claude Code با شاهکار مهندسان اسپاتیفای!
🚀
🧠
پلتفرم
Portal
مثل یک مدیر هوشمند عمل می‌کنه و با واگذاری وظایف ساده به مدل‌های ارزان‌تر، تا ۹۰٪ در مصرف منابع و توکن‌های هوش مصنوعی شما صرفه‌جویی می‌کنه!
🔥
🔺
تندخوانی با Gemini (bulk-reader):
فایل‌های حجیم و چند هزار خطی توسط Gemini 2.5 Flash آنالیز شده و فقط یه خلاصه مفید به Claude تحویل داده میشه.
🔺
کدنویس روتین (code-writer):
تولید کدهای استاندارد، تست‌ها و تنظیمات خسته‌کننده به مدل‌های کم‌هزینه سپرده میشه.
🔺
تمرکز روی کارهای حیاتی:
با این روش، Claude فقط درگیر کارهای پیچیده و استدلالی (مثل رفع باگ و طراحی معماری) میشه.
💡
در
نتیجه:
یک ترکیب هوشمندانه از چند مدل AI که باعث میشه هزینه‌های شما ۹۰ درصد کاهش پیدا کنه و خیالتون از بابت محدودیت توکن‌ها راحت باشه!
🔗
لینک دسترسی و پروژه
✈️
@ArchiveTell
|
#TOOLS
#AI</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwVaoolp5DC2NWKCINdFMCpqiiEmGqhP0smQrmBW2D5khNcOeCOCAi2qWezyXhQT3jsfO9B609BHCKuywG8TvZu5Z2TqH3vWmfHbWr_ZB-KvyhT8GfdfUvrITIFBR89tJNsmIiLr9FKpVTLTzQU_AJpE8LY9jIG6ZGHZLS2kX1pW3evnnkEsYV0SZbM22OV5X19OITzMvPn0SaVU2kEOYTjSbGziQ2HfAGi2UjubC1_fyEEB_3IMCFAGAHlWNbXmMji4Pj5GvO0fgMhbxP7yuHqgttHQL90US5vB8GVWktUK2cdfdkzXIes2r7jOEPPTlApzP5n4fFpgmiuWZEM7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XyKqBmJ-OTgS4UcV2yPtGu-ae7jeSTn_3gEcykN6U2BoOWqZYEhHga9xaLEtTXJo3UMtzBW4clQzZfR2w-EDMvY_HCUOJUBGvFkwfth1TCwV66Dkclb_7Vnbma_iRbDydZtcFPC1DzNsoB3_Azez1TSjuBIrP4WVpAQQ5B8sKNwLt4kDI3RU-81mCTGFmzYBrgM200NYNnoxO9m1YBUalwwnJNX3GnxABQ7LkNdGF0mQZ9_-4FXu2PtiSN2FVxVfpdfk_vCetW9W1axLAPj_hyOfZi4NkMBpyFvzV9OmmdcFK3_oGnFPPe_lCuOMyIsBHCNEYoZH3SESm0xnJihKGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cQPNWIW0XuWIqbwhgtFTC3RbPcCXnR9-lkX8utwINJMvVRcDuY-bNiIa-nHxvOdbSqEbnGvmenPgxEY0OBX4AgrpNIb8DTbYVCBW3CIhZngoMOor2GCeoc8SUjY4tL1-lfo0oYeGmy01HKzlLD8OKvk2avGJ-UC0YkgmoS8O3TwqFiVuVmSELSeCNY6e9DwnDwSWn6omEviovspEdIPXth5yiKQ1ibpYyPTM2b7wjBQd2QXWyVD3tUv8w1cG-K7oWbcGpzuDKPhcgvCp8wxYIPHtkscOWoK2_w0Q-JvbOPidk_hseGUgY6btUXJFcI_XiLZ0DJecljBRzX0927YKLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📌
مدل GPT-6 Astra بازم یه حرکت دیگه ثبت کرد؛
بازی Portal رو تو 23 ساعت و 43 دقیقه تموم کرد!
مدل به طور خودکار شخصیت رو کنترل می‌کرد به طوریکه هوش مصنوعی یه تصمیم می‌گرفت، بازی متوقف می‌شد. GPT-6 Astra با استفاده از تصاویر، موقعیت شخصیت و زاویه دید دوربین، تصمیم می‌گرفت که چه اقدامی انجام بده. بعضی وقتا هم تصمیم گیری هاش تا چند دقیقه هم طول می‌کشید، اما در هر صورت تونست بازی رو به پایان برسونه.
🔥
این کارو آقای "cozyblaze" با کمک اشتراک ۲۰۰ دلاری Codex Pro انجام داد.
🔗
سورس پروژه
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6n1Fq08zJDMbTum0iJa2i-WhL0KOSldSr4dljyDROmiRcqJq3hprXzuVh7tlBLm7va5rHkgk3H_mflnwqMvd79gE8pvuCSxAe6pdH9YHKGMrXk_CneaeSNJbFdnmV_03wynM5COSuf1gpD3Tyn3q8G-1VtMfuiy-Q1DrQpGIdNJUTTs9a3tkzHpdn34HgMhHGbQBgLXkSTIyK6XilAuVlFJJjEd6M85RqWhiMGMMC3rmwPXArr6CJNO_vMZszhjkfIMqySzLR2kk_azabJ8fdwO8rE-MR2C0nwcq3wWUGXiFbgpLSlVyU1umKz3IhTZzEowmMpL_qZ3R3CDVTb1pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعبه‌ابزار همه‌کاره برای برنامه‌نویس‌ها با DevToys
💼
اگه خسته شدید از بس برای کارهای روزمره (مثل تبدیل JSON به YAML، تست RegEx یا دکود کردن JWT) مجبور شدید سایت‌های مختلف رو باز کنید،
DevToys
دقیقاً چاقوی سوئیسی شماست!
👍
🔧
بیش از ۳۰ ابزار کاربردی:
انواع کانورترها، انکودر/دکودرها (JWT، Base64، QR)، فرمترهای کد، هش‌ساز و فشرده‌ساز عکس.
📄
تشخیص هوشمند کلیپ‌بورد:
به محض کپی کردن متن، خودش می‌فهمه چیه و ابزار مناسبش رو پیشنهاد میده!
🛡
کاملاً آفلاین و امن:
تمام کارها روی سیستم خودتون انجام میشه و دیتای حساسی سمت سایت‌های ناشناس نمیره.
➕
پشتیبانی از اکستنشن:
میتونید ابزارهای دلخواهتون رو هم بهش اضافه کنید.
📌
لینک مخزن گیت‌هاب پروژه
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=bXs6KZSSxM7TbXERZQRyElRIBP_ZKeQO_EixBYgpBCJpKbGRdy0d1qQjvsOd0ikx9n3ByeDVLkK7Gb6UhmPLv9shexvxUbKZ5i6TL-0jeAmjTun64I3ZbZ0sEPxjUQE1WrBQ4xoIKU2BXqDmLhGJlKnSgJJY0lXw5c396actw7gUdK6-YLhGhgAg00KjMkKLAznhiGU1qVckkAztvbgB5VpWshOONp02VhG50JbYK0sqFyiU7oD-VWQjWBxnK1aQyP7_ElCpYo1F8vmN_TmFFLUJmHGuRs1i9ru7lLA66zB82EHV5yFIVZZMLIoiwDmvOY5x8u8Us4eeqXNXpT9g8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=bXs6KZSSxM7TbXERZQRyElRIBP_ZKeQO_EixBYgpBCJpKbGRdy0d1qQjvsOd0ikx9n3ByeDVLkK7Gb6UhmPLv9shexvxUbKZ5i6TL-0jeAmjTun64I3ZbZ0sEPxjUQE1WrBQ4xoIKU2BXqDmLhGJlKnSgJJY0lXw5c396actw7gUdK6-YLhGhgAg00KjMkKLAznhiGU1qVckkAztvbgB5VpWshOONp02VhG50JbYK0sqFyiU7oD-VWQjWBxnK1aQyP7_ElCpYo1F8vmN_TmFFLUJmHGuRs1i9ru7lLA66zB82EHV5yFIVZZMLIoiwDmvOY5x8u8Us4eeqXNXpT9g8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم 7 برنده خوش شانسمون
🎉
:
1.
@reza1629
2.
@mhti9
3.
@KIING_ZOG
4.
@Gogogrugo
5.
ＮＯＢＯＤＹ
( 6641463426 )
6.
@an_Y008
7.
@AshenOne2077
برای دریافت جایزه به دایرکت مراجعه کنید
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🥇
رکوردشکنی دوباره از GPT 6 Astra
خبر رسیده که GPT-6 Astra تونسته تمام ۴۸ مرحله بازی «I'm Not A Robot» سایت
Neal.fun
رو بدون غلط رد کنه ، خیلیا جوری جو دادن که انگار آخرالزمان امنیت سایبری رسیده!
😂
طبق معمول، ته این هایپ‌های رسانه‌ای خبری نیست. کپچاهای تصویری سال‌هاست که عملاً مرخص هستن و حتی مدل‌های پارسال هم با یه پردازش تصویر ساده دورشون می‌زدن.
سیستم‌های امنیتی واقعی وب الان با تحلیل رفتار موس، کوکی‌ها و الگوی کلیک کار می‌کنن، نه با ۴ تا عکس چراغ راهنمایی و خط‌کشی خیابون
😁
تست کن ببین رباتی یا نه ؟!
🧐
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPFtLdoyeK7Im3873EbG7yO1frUaVxVUkdGs4OQKMJceCfa0JdFm8xqyB-fTmoCsNtgCTMV47j4Y5VElRS-EiK1rjWUIygbKyCCgpWtxP_sZcF68zfF0xyuSLG2rBh9PO6D4NTM3yfsfcDYwi5Kc746lHo5ZXPwbD8skIxuKS1_LZJ7WKzktZAy2reL_xxOR3KQq_eLCHmr9m3Q_ZD_JROIpNh99HZyidtDKx9OO1MHiWar5nwb4ZD5SV7xT10JPEFG25t94W7HxD5vcoDvuuXcUcdkRDbyX7_etPpjZ6aZlhAevT933GYoHw-VyAaX3oiP-oJe63ENLjjaspSVZIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جداسازی صدای خواننده از موزیک با هوش مصنوعی؛ تمیز و بدون دردسر!
🎤
🎧
بچه‌ها اگه دنبال ساختن نسخه کارائوکه هستید یا می‌خواید صدای خواننده رو برای ریمیکس بردارید، ابزار آنلاین
AI Vocal Remover
دقیقاً همون چیزیه که لازم دارید! با استفاده از مدل‌های صوتی AI، وکال و ساز رو در چند ثانیه مثل آب خوردن از هم سوا می‌کنه.
✅
🔺
پشتیبانی از انواع فرمت‌ها:
هم فایل صوتی (MP3، WAV، FLAC، M4A و...) و هم فایل‌های ویدیویی (MP4، WebM) رو به راحتی قبول می‌کنه.
🔺
بدون نیاز به ثبت‌نام و کاملاً رایگان:
پردازش تماماً در کلاود انجام میشه، قبل دانلود می‌تونید آنلاین پیش‌نمایش رو گوش بدید و تا یک ساعت خروجی MP3 یا WAV بگیرید.
🔺
کیفیت و دقت بالا:
تفکیک دقیق لایه‌های صدا بدون نویز و افت کیفیت محسوس سازها.
💡
نکته:
برای آهنگسازها، تدوین‌گرهای ویدیو و یوتیوبرها برای برداشتن کپی‌رایت یا ساخت بیت‌های بی‌کلام، این ابزار سریع‌ترین میانبر بدون نصب نرم‌افزارهای سنگینه!
🔗
آدرس ابزار
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXHESbS9F_SeNtHuXXHE6mMaRS2EGtqh3AE8SSgeKg545CsmHQIMUJElt_pb1VpNTJJl4ePCs1ebSnfCWLXH_3qEb931YDzbQwOYAGStYzRMz9h5wWFVGJF-XQkV3S85XOYvdjmv-znmqpHjzmnvp4MBULYwLMGzwuUsVP852Qshzapwn3n8vWwe6u27X3Q8Z9FPMduPsLAKC8P8XlKqqemcpRSUhxVpqwgRQKQ--MHJlQKctKHuhXT4VWgB9d-GnnmKgFuev7zeVxwRxlfpqUUI0BAQ9S09sV2w6MbrUpZlndqaA--5rhmjkb5nUqbiFRIXnHyINhD_fXNJg2-XfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل گوشی اندرویدی به یک کامپیوتر دسکتاپ کامل با Android DEX!
🖥
📱
اگه از قابلیت محدود سامسونگ دکس خسته شدید یا گوشیتون اصلاً DeX نداره، این ابزار خوراکتونه! نرم‌افزار
Android DEX
با ترکیب جادویی ADB و موتور قدرتمند scrcpy، گوشی اندرویدی شما رو به یک سیستم‌عامل دسکتاپ واقعی با پنجره‌های شناور و کنترل کامل تبدیل می‌کنه.
🚀
🔺
تجربه دسکتاپ چندپنجره‌ای:
اجرای اپلیکیشن‌های اندروید در پنجره‌های تغییر سایزپذیر روی ویندوز، مک و لینوکس با اتصال باسیم یا بی‌سیم (Wi-Fi).
🔺
خوراک گیمرهای موبایل:
کی‌مپینگ حرفه‌ای کیبورد و ماوس، شبیه‌ساز جوی‌استیک WASD، قفل دید ۳۶۰ درجه شوتر (FPS Mouse Lock) و حتی شبیه‌سازی ژیروسکوپ!
🔺
دور زدن شناسایی امولاتور (No Ban):
چون بازی‌ها مستقیماً روی سخت‌افزار واقعی گوشی اجرا میشن، آنتی‌چیت بازی‌ها شما رو شبیه‌ساز تشخیص نمیده و بن نمی‌شید.
🔺
امکانات یکپارچه سیستم:
مدیریت اعلان‌ها، پخش صدا، انتقال فایل با درگ‌اند‌دراپ، رکورد صفحه و تعریف پروفایل‌های اختصاصی برای هر بازی.
💡
نحوه راه‌اندازی:
فقط کافیه گزینه USB Debugging (یا Wireless Debugging) رو توی Developer Options گوشیتون روشن کنید و برنامه رو اجرا کنید؛ بدون نیاز به روت!
🔗
گیت‌هاب پروژه
🔗
سایت پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqEoXWkQWe63wsr34bugXXDP1SLMKv5rAs2EiqSu7GcSMZDbW4E00wX-n8vEuNCFvGtwTynAbkN0zpeI_thC1rP-zgnGu_5WhJL-F1M77jjPrUctzX8EZtW_EQsHqizXsebqw6nfs0EygvyP_PN5kBks3f8lwKAMKExt5iKrn75TenuursGGoql2CytC5-rxNmg_cJlSgsPignSxuuZa9Z4Z-R5hzrEQR4wKQuS44M6oU-dTI5vAgRikg3hcxpxpzkXTFy1YbF7mqX7LbL5jEIZXuzTHxOyn76Q_DDZeev_a3hnkaAprTs-1kzLtlb3W2wqZJgust29MHKSap-XwnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معدن مقالات و دیتای آکادمیک اروپا؛ گنجینه‌ای که کمتر کسی می‌شناسه!
🎓
بچه‌ها اگه دنبال مقاله‌های خاص، دیتاست‌های خفن یا پژوهش‌های پروژه‌های اروپایی هستید که جای دیگه پیدا نمیشن، پلتفرم
OpenAIRE Explore
دقیقاً خوراکتونه! یه پایگاه عظیم با بیش از ۱۳۰ میلیون دیتای علمی دسته‌بندی‌شده و رایگان.
✨
🆓
🔺
آرشیو عظیم ۱۳۰ میلیونی:
دسترسی مستقیم به مقالات اوپن‌اکسس، دیتاست‌ها و حتی سورس‌کدهای پژوهشی پروژه‌های اروپایی.
🔺
بدون لاگین و کاملاً رایگان:
بدون دردسر ثبت‌نام، پی‌وال یا محدودیت دانلود، مستقیم به منابع معتبر دسترسی دارید.
🔺
ردیابی شبکه‌ای پژوهش‌ها:
می‌تونید خروجی‌های مختلف یک پروژه (مثلاً مقاله + دیتای خام + کد نرم‌افزاری) رو به‌صورت متصل به هم پیدا کنید.
💡
نکته طلایی:
برای پژوهشگرها، متخصصان هوش مصنوعی که دنبال دیتاست‌های تمیز و رسمی اروپا هستن، یا کسایی که دارن روی مقالات بین‌رشته‌ای کار می‌کنن، این ابزار مثل یک میانبر تمام‌عیار عمل می‌کنه!
🔗
وب‌سایت رسمی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdamDcRRwO9FRcbrk6HCuY6DPk6pi-BFu5kbwEITGgMMEqmYwU4T4Bm4yFJUqJmjHsPukJSl_3S89BpiOnvx85XSSj5Y_-rbgzUbKF_xndW0L7tLS6wfx4q6uG9JelLPs20DCRwurNGtiU58jKFdHvPSJVorpb6gw6g1uws7N8hcLC0hufqnGUxJvrsQGm0fhPk0xa9dNC7ZGXQmDQovJLC5Tl83pnjuCMeMyngk5195MO2oM8V_iV58rGI16phEi_XIdd00D7yLq_L_SQnycH9Y-EO1ZJ5l83eRVUDAkFeHpnkhUcNRybbDagSBy13qoK-et2ffthE-OsimZUHTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیبورد «شریک جرم»؛ قبل از ارسال پیام حواست به جریمه و حَبسش باشه!
🚨
بچه‌ها براتون یه پروژه به شدت سمی و دارک آوردم! این کیبورد اندرویدی اسمش «Соучастник» (هم‌دست / شریک جرم) هست و کارش اینه که موقع تایپ، متنتون رو آنالیز می‌کنه و آنلاین بهتون می‌گه ممکنه بابت این پیام چقدر جریمه بشید یا چند سال برید آب‌خنک بخورید!
😁
🔺
کاملاً لوکال و آفلاین:
نیازی به اینترنت نداره و داده‌ها از گوشی خارج نمیشن؛ با llama.cpp مدل جمع‌وجور Qwen3.5-0.8B رو آفلاین روی گوشی اجرا می‌کنه.
🔺
سیستم دوسطحی سریع:
اول با یه دیکشنری سریع کلمات حساس رو بررسی می‌کنه و بعد مدل هوش مصنوعی جرم یا تخلف بودن متن رو می‌سنجه.
🔺
پروژه کاملاً اوپن‌سورس:
کد و نحوه کارکردش روی گیت‌هاب قرار گرفته و برای گیک‌هایی که می‌خوان اجرای مدل سبک LLM داخل اپلیکیشن‌های اندرویدی رو یاد بگیرن عالیه.
💡
نکته:
هرچند قوانینش بر اساس مواد قانونی روسیه تنظیم شده، ولی معماری استفاده از مدل‌های فوق‌سبک لوکال برای پردازش آنی متن موقع تایپ، ایده به شدت خفن و قابل شخصی‌سازیه!
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5RlN0BWPZLkeGw-pohe7u1lix4IV5sff9KzEqeeKJTuloTURRsP6KrCHkuOPny4HGHWNAj_079mBAX4Uzr-hFmcZsOxwwlAUhyHgryXpe38-Ha1CRnPOmpg5ciV32KHfoY9ZorUNJ2u2964kTvYJirHHyQNO8iZB9hjzoHCidbMUkLQbBJWum3Nhzni4GsVe_mrOM-ahts8Jbkenc98G2M59xwKVTx0qnDcXVGnhdfzLaqwB-8lkXx-6alf7wGq8Z_LTloU60uu8oU34uGvxRUXoct5epkbCs_wPwbGmPi4WwpFBdPnvoFhtHrT3f0xXC3XOnxvbdXljf-DFoHpgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طراحی و ساخت اپلیکیشن با M3E Canvas
🛠
📱
پلتفرم
M3E Canvas
یه پلتفرم اوپن‌سورس و جدیده که بهتون اجازه می‌ده با درگ‌اند‌دراپ و کمک هوش مصنوعی، برای اندروید و وب رابط کاربری بسازید.
🔺
طراحی سریع:
المان‌های آماده رو می‌چینید، رنگ و فونت رو شخصی‌سازی می‌کنید و همونجا تو مرورگر تست می‌گیرید.
🔺
تولید پرامپت جادویی:
جذاب‌ترین ویژگیش اینه که در نهایت از طراحی شما، یه پرامپت دقیق می‌سازه که می‌تونید مستقیم بدید به ابزارهایی مثل Claude Code یا Codex تا براتون تمیز و بی‌نقص کدنویسیش کنن!
📌
لینک دانلود / گیت‌هاب پروژه
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه
ArchiveTel
رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد
این ربات
رو استارت کنید
2️⃣
در چنل ربات جوین بشید
3️⃣
با آیپی خوب ترجیحا آمریکا وارد دکمه بشید تا سایت باز بشه و دکمه وریفای رو بزنید
‼️
نکته :
در هر گوشی فقط 1 بار میشه اگه میخواید با یک گوشی تعداد بیشتری بزنید باید هربار کلون های تلگرام رو نصب کنید  ، هر 5 رفرال برابر با 1 اکانت هست ، تمامی کریدیت های جمع شده تبدیل به اکانت میشه و قرعه کشی میشه و لینک فعال‌سازی به شما داده میشه
‼️
شرایط : حتما باید در چنل آرشیوتل عضو باشید
تاریخ برگزاری ، فردا دوشنبه ساعت 20
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfEThayMm0a9mRa3LqQAl4H-JddxGn-tDteAq4ugw7Z-PDrfhBGx2ALqgZOxXgAtGuoRn03YplWsZGd3wTwQkXMoTMySaV1IA86daMNLIZLNdZ7LeporvrPAIgd9WCA19Eb8FyHNFY3Yx3efcbVo2WKursifO-UOIqKaWidWitQxMFcSYrk3Lge7mOxvUbvlHzEiUxtt0nGqClXc3k_yGXINN2aNKMb8VRvwjjmR48k0U_p1KzirCueI-fO0RKdxdH3RRhAiPYihaCj5WEKiLdw3b5mUj_va07HEyq5PyGiCelgooYnec2HduSWzpVM0qe8z4AflzSx2FsDl3cnFOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API هوش مصنوعی ها
💥
🆓
DeepSeek-V4-Flash-Vision-Exp | DeepSeek-V4-Flash-0731 | Qwen3.8-Flash-Next
✅
این سایت ثبت نامش کمی آزاردهنده هست بخاطر UI بدی که داره ، باید با گیتهاب لاگین کنید بعدش میره تو داشبورد و به ایمیلتون کد میفرسته و اون کد رو توی مراحل وریفای وارد کنید ( شماره تلفن لازم نیست ) حالا بگردید عقب و از سایت API دریافت کنید
✅
هر روز این سایت 1 PTS بهتون میده که معادل 10 دلار هست و خیلی زیاده برای این مدل ها
🚀
محدودیت هم هست 20 درخواست در دقیقه
‼️
📌
Base URL :
https://developer.amd.com.cn/radeon/api/v1
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwa38GE97tXS6SenCbghsIYSAEX8pdzep_VFXDeE-gh00lH25v6_4Sp7rbyHxv2qHlQJCBUOoeAjqMzOkpvfKuSShN1tfUGfgWt-7h62xG_A_rCzQxu8nYaRBxlnOe-d49XLC82nnK55o9RPQ2iUofG68xrzOtReW86cfJ7RO-K2RT-NwxAZOA8ca6LTjKmx34wQlQ1cECnBmP0DLGarPJ_FFfsaCxj8-oZVPzJpWzfIOi8VjFFxHl0ob3k-qliveRloDlEiapOZmZHuSbWeC377h6KT9XjZ8cqW3TPM3qsv2_8WrMvE9jFr-Rx4DVHNfcu7OuZjl0mnL71Hq77LRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به هوش منصوعی های محبوب
💥
🆓
Opus 5 | GLM 5.3 Flash | Deepseek V4 Flash | GLM 5.3 Flash
✅
4 میلیون توکن میده که میتونید استفاده کنید از API هر روز هم ۱ میلیون توکن میده برای opus 5 ( حد مصرف روزانه هر مدل ۱ میلیون توکن هست )
📌
Base URL :
https://helyxai.space/v1
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkpMuku55U4h_pmFEjvJd0FQTA_i2ApPh0RQ2HNdSzBRfgotD5wLPDY1rGi7OZQf82R1gwoJxxG10BU04ppCYp_2LRZibwKMK2N4Gxu6SxGFuoKbupKgcOKolKOsl6zRScvbmCWS-qwVdJ8dpr1vT6z05BsB85U-08_IoX5ExwewVwwjZ7KnXafILziodCPmg0kQEC6FlLnkagORgwM189PljLpVn04mSFinCuFFdeTaIGGuXYWM-oDLYNFfwJuQMSY-DnVSsDxfswh-UVpNUAeSTPxdSz-2vI8qPy79T9QgtNAJERSY365LpbX5etC5sl9sMtvjAoTGvclyNHu-1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏
اینم لیست مزایایی که داره:
‏• جمنای: ۱ سال رایگان
‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه
‏• جت‌برینز: ۵ سال استفاده از تمام ‌IDE⁩ها
‏• گیت‌هاب: پکیج کامل توسعه‌دهندگان
‏• آفیس ۳۶۵: نسخه کامل ورد، اکسل، پاورپوینت و تیمز
‏• فیگما: نسخه حرفه‌ای مادام‌العمر
‏• نوشن: اکانت پرمیوم مادام‌العمر
‏
برای دیدن آموزش کلیک کن
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8cFlR66iWeaoAdLNcZg-nb9Lu9IylAzfo_6L1cf5yVl3rPrH8Cgd0fCR8EuYd0oT-uIA77cmVKbG7_rT6mUnXB7nPK87Z3khkSuCO7idW3Af-BUqvVA-N0s7iFNahLBTasqDVX2CsCRw4cAC9QojE7oqQIfBOyRL_vl7_tYuKUI86soyIG3kUfdkQ2LzkP7FzFXIIATVJSlMBQV0f3L5koGyEJ7BID91s_OeQ3yUuxDLIcU-VR-RfKuMwEnVLMvUmFMkf5dU0QJVd7XkbXcBp77XKyQ6i7cEZRGB-acrksKhrE2VRwAAgrIpqrjoligJHziwtq-zaWkdq-Dsbx50g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
داستان GPT-6 چیه؟ انقلاب هوش مصنوعی یا فقط شوآف تبلیغاتی؟
🤔
این روزها همه جا پر شده از اخبار رکوردشکنی GPT-6 Astra و نمره عجیب ۹۹.۹٪ در بنچمارک ARC-AGI-3.
طبق بررسی‌هایی که کردم، این نتیجه تو شرایط کاملاً ایزوله و خاص ثبت شده و توسط منابع مستقل تایید نشده.
قیمت‌گذاریش هم به شدت نجومیه؛ هر یک میلیون توکن ورودی ۱۰ دلار، و خروجی ۵۰ دلارِ ناقابل
😁
(مقایسه کنین با جمینای ۳.۸ که ۳.۷۵ دلاره)
در ازای این هزینه سرسام‌آور، وقتی در کل حساب کنید، برتری خاصی نسبت به رقبای خودش مثل Fable 5 نداره.
یکی از معدود بنچمارک‌هایی که هنوز اشباع نشده و به نظرم بهترین معیار برای ارزیابی مدل‌هاست، بنچمارک Humanity's Last Exam عه
تو این تست، عسترا نمره ۵۷٪ رو ثبت کرده؛ در حالی که Fable 5 با قیمتی مشابه و حتی پایین تر، نمره‌ش نزدیک به ۵۸٪ عه
🔥
با دیدن همین آمار میشه گفت OpenAI با این Gimmick های تبلیغاتی، رسماً داره به شعور کاربراش توهین می‌کنه
😐
من حتی کاربرشم نیستم ولی باز به شعورم توهین شد
#طهلیل_ai
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4o194_JRmESrdCZuZRaC4Hu5lrnwG7KRwQ6161oyRXZRGQUYHLhnuocKOX2grzh5H_yyYzGDqrbbELzzt3d9cS3bXVDnvnv9j7hmlOHxVhb23Y84NCsBCQiRy-fvU0LGwQfBVcvJMYpxrfY3j-RFLNIS1b9UTA6qGfbGU3YcOurcfFWsLX1OtCMkZKSHqVop2D5IOx6vDagcZT_hQfQhiopTx8lxf6rQ6_Eb0GgCTnMIzKenEJwdi5xD6P13R_z-iyZEfNFpvYab0W4S-Szyx7SfLm9AJj_9J7_ZFONffD9dY3tAf6PFStymlM5APMxUbPCkcvAnqZ0sIZqeFM7rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Free 2k$ model GPT
💵
📌
Base URL:
https://vip.9aws.net/v1
📌
API KEY: sk-g926rIr0SG7pfoD4WextkZwRRAgFOwYZDsG5hnDr8mL2ZH9d
📌
Models:
gpt-5.5
gpt-5.6-sol
gpt-6-astra
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBlPbO4Zblt9zQR3AkCAo_0LEG56fGdGz7Wi31NfwAHQHHsJzJ-NUziPv3KAklU6MscbWB9yWpuqi7Gbk4H1qvQ9eZ5ywugqKtegnWr92XQyd2TbRWiaHb8O6g1BwHGB5t531vlMeH3hmc8gqt_Y1Svebadlm7trZA3zKVJKaCfO-qGSr_PEl8owrnbUmrb4PPV2aiLE6qMlMBKXPTyJbG_YQacQ4No1ON1OHbosR9P9SRjF6IAczoV-CFM_dEsTKV9wAX91fS6ESrHei4kvrRpuFrf4DVYbawHFs0MSqU91wYj4I7cldCP-n6TWTV9Fr0Sk-UPSC1iM-BJ5fgNGBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی آزمایشی رایگان به مدل‌های پیشرفته هوش مصنوعی
💥
🆓
Opus 5 | GPT 6 Astra
✅
سایت ClickUp فقط یک ابزار مدیریت پروژه نیست؛ ClickUp Brain حالا امکان استفاده از مدل‌های مختلف هوش مصنوعی را در محیط کاری ClickUp فراهم می‌کند. طبق مستندات رسمی، مدل‌های OpenAI، Claude و Gemini در Brain قابل انتخاب هستند و می‌توان بین مدل‌ها حتی در یک گفت‌وگو جابه‌جا شد.
🚀
🎁
سهمیه رایگان
در پلن Free Forever، نسخه آزمایشی Brain شامل ۲۵ استفاده برای هر Workspace تا ۱۰ نفر است. در Workspace های بیش از ۱۰ نفر، این مقدار ۵۰ استفاده است.
✨
⚠️
این سهمیه ریست نمی‌شود و پس از مصرف، برای استفاده گسترده‌تر باید پلن/افزونه پولی تهیه شود.
🤖
حالت Agent هم دارد؟ بله!
دارای دو نوع Agent است:
• Super Agents برای انجام کارهای چندمرحله‌ای، تحقیق، کار با اطلاعات
Workspace و اجرای workflow ها
• Autopilot Agents برای انجام خودکار اقدامات بر اساس trigger و شرایط مشخص
💡
علاوه بر چت معمولی، Brain می‌تواند روی فایل‌ها و اطلاعات Workspace کار کند، جست‌وجو و تحقیق انجام دهد و حتی Task، Doc، گزارش، اسلاید و موارد دیگر ایجاد کند.
🔗
لینک وب سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhJlwLLKC1mg8z1niSkEJKFC__FnKmyJmNePy5lf0VPe6aJhCTbGbzUi3YG30CS7mNPLCi1vDzRaJPFrYSD-pb6BA8fP9YUJJIHL97nvCcQ8HY5BNMZGX9AX8L7_dD9kPjhekqQmT4WZ38KIPwrJVj4MwC0mg7VgGdiqj3pmppiPNiIv1SWSiREm55TYjImQyZNYRAg4p8I8jL65-oQLOXJRl1AhyJXJHbCGnRvOvh1XUpaYUAYpsRZp-cEtoNfwFdHtLPmo_22XlXjF0a5eS3HDcZYJC7pMeu3u8nRW0P4RO8NZhBRs6l1pSsCLJGcDtsRv2mxNl0vMOGXRy6tJsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های هوش منصوعی
🚀
🆓
Opus 5 | Grok 4.6 | Deepseek V4 Flash
✅
برید تو سایت زیر ثبت نام کنید و موقع گرفتن api باید گروه Free رو انتخاب کنید از این گروه این سه مدل بالا رو تست کردم جواب دادن ، بقیه چیزای خوبش کار نکردن این مدل ها رایگان هستن و کریدیت نمی‌خوان
✅
📌
Base URL :
https://kiosapi.com/v1
اینم کلید خودمه اگه دوست داشتید میتونید تست کنید ریت لیمیتش رو نمیدونم
📌
Keys :
sk-ZoCd9hc91if9INutCoTC6zA0wJ2pbrd9a75GQJTyj5V4gIup
🔗
https://kiosapi.com
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbhN8N0ownmPJOMstCvkiKTBAYNvoIeZ8bgERdKUh5cMtrIJaN50rRHk6Qbu1HT8kpIG-111G68nxs9WcnCHKUZuYnpLJwA5pDYZFevMgla2xHCwCWenA4Ew4nzh0RjIGMwSxvdL2oSerd_e_IskObaVMVYR5JhcQz_5HAPDcP1FvyN5r9hVeUdUVwV0UbzMvyQiBefypRoAdSSrmzn5gzPNH8KP1xmTQSleZ1uvdJeQMwWBYrWJTY_n0hY4gZC_t3dQCFW12zs7ij4JR0v-1NwfvywOCalgQ2Or2Tl1eDLGwQCfPv-H4rG57BOUnR5WhNIjYY2tNEVlG-bHf-C85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5000
دلار
😎
📌
Base URL :
https://vip.9aws.net/v1
📌
Keys : sk-faNuu4uK9WqIYAiXjdmYxeX6PI1Z5wNLzCsIXKbKVQ67W1rG
📌
Model ID : claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVHjrQcaG-yXNVOnQuWuc8NhMkfzgHTgS2BOLSsVX2SELsJwtwO4cJxTWPoSLxDt5SZm6osTBqXtxf8rvIi5YcZYy66OpZyeFk1Bv335TZ4nFfr7-dzY-a7_mhCeDGbBTRPZOo00l0QXIiKY0xvQ2CAdFcJCqgJWNkfFIUa4BRp9o2E35FbeF6FxEcatFLExn4ilOPp0yv28t8d1EyFgzYVx6JWdZg5HNYeRacUorH01985VYe7FL7zTlw_V-HFopKOebXfiDGG6sLaTLftNDqrbkgvyxANwd9iZs2_jnBxhty9K-y5jcFBr5KQRXz3PyOB2djb2mFm5A1lBk0lQHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ساخت وبسایت ۱۰۰٪ رایگان، فقط با یک کلیک!
​سایت شخصی یا پورتفولیو می‌خوای اما حوصله خرید هاست و دردسر کانفیگ رو نداری؟ این پلتفرم اوپن‌سورس رو دقیقاً برای همین ساختم.
​
🔥
چرا ZeroWeb؟
​
💰
بدون هزینه هاست: کاملاً رایگان و مادام‌العمر روی سرورهای کلودفلر.
​
🤖
مدیریت با تلگرام: پیام‌های فرم تماس سایت مستقیم میاد تو تلگرامت و همونجا جواب میدی میاد تو سایت.
​
⚡️
نصب با یک کلیک: فقط روی deploy.bat دابل‌کلیک کن، تو ۱ دقیقه سایتت بالاست.
​کدها و آموزش کاملش رو تو گیت‌هاب گذاشتم. همین الان دانلود کن و سایتت رو بساز
👇
​
🔗
https://github.com/faithsaly5-stack/ZeroWeb
​
⭐️
خوشتون اومد استار بدین
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXG-4EkMifYZC2ElfUU0XOMGWZgBj7fuMfQkFSfPpHHwsL68uZjyBgZC8TQJzq45vqne3KkMGzlEBRlGEs0Q3Fjj630Q_7zohvfpz_FSQkOxn3P0zC0970cMUARP7aMuIx4_ieR_O0LS4UmCIJrSYUPOHX10cL70Pa94NwU18CkZHVEm__tgZJMYWqXS71UjFnhT5ZLl0iDrNiJMCYmoRwsB6QnfMue2f4d2jaWYAznzNG157RASaq6O7aqzrfvvBRhtECezdjhXft9sg0wfr4o15phr-Z2xkYBXg4MI3sek4wZ3uynp6bxaOv-blAIK6jHwEAXivl9oLiMsUNt4lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت z.ai کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه: ۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan: هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید…</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePL3NhVk8_UztZdJpRKviC3GeqV6OvYNoZe_icUyZnO2jmYLVZsE3uPhN8OPfWvEL_Z9bMMGhisFMaqIyzBulpMUp_PbrbwOWGHATwkLktJlERCF15yCZafHPX8dumhN-PCATfRR73UgWlx_TJ1sROi782VzPDIsQXWYqR85PmCu0ny3_DWmGueZwJPxxDtlTjFC4O91iHHm2usI2epefimWs4KrqHnnLe6TGWyyQ8JVu_qkQLbahEAO9ier34dgLdbQGcOBdfUnpGdojp5PbVHF-nDHtoNqreCaPJz15IT5OzXjBmfTHsFgik7K2OeZPo1iYyg2ruoBoH6u9OIJDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1,000 دلار
😎
💵
📌
Keys :
sk-ByTi6xCfB7Pt1N8Hp9z7VdsRwGIMM5pdnh4CsorUfflysvbq
📌
Base URL :
https://tabitoken.com/v1
📌
Model ID :
claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auTHd-pBrxJV9DMN2e18nwfquvBdLi9uu2Z7Ok9M8i1_qCq06yNPWKiZ2CCL2RoDvWg_Gl_CSYLkILHIreC3lvAiPFD3uYgLQTH0HZdWsJqpjnz3irvyADIZs2hICXvo7qFYoNC6jU_naJgxvkA2edW_tQ830tuAUw6NQP0EWOFZc_txURT6L8zlxl6ViB0rLbXFQrEVG0DlG0cC6ts5OtwU6RWQr7vo7yoqOr5wtKgMEV54x17cxSl7su_Qfme4K7EWOPnsf2WIlxt2YJiVpspK0JGIF13-Qe9-O9levOLjWIK4mfIhgVLCkBkJeErr-RRfK0XDQA-BspqnoGZyxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfDsAs7gocHr0hvNSyRrSXi7ds1ohPAOnge3mb2cIN0AgsHdjHUKON-k2Rr48Zt697FBxzG1_luVNMbJ-KPllkkLZr8rWuwX9yAahCcjzlZMufFW7g-FQmgbhvFZfliTR87F7vl8401LxXlCd7FiFLnsL7WuOHBljchvH5QSFNvDMToge460C5w_eDAlcJrat6A3Xugc_cfrowy7-Uvgw3fOCUqa7K8Yq6jWMg00oegVrq1RUQDgIk5R7MfcC59QfnVmpVyIhgGnK9vKhfY__6pxZN0v7KPS70ZU1GVxLKM704fZs1xEvW2AORb9l9WTXFppKlGk8isowJZ6cuafig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت هم به دلایل نامعلومی میاد API مدل های Fable 5.1 و GPT 6 Astra رو میده ایشالا که خیره
📌
Base URL :
https://api.experientiallabs.ai/v1
ماهانه 5 دلار میده و همچنین فکرکنم Fable و Astra کلا رایگانه
تست کردم اوکی بود
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ER3dWgzpRDf9UZMMhsseA2zzYEZ7NATquheUhcX66MqLlQN_yCZqVoLpYANe5k1JjqBaRdDQPuQFeutMyjznWLEI4GoHRNi14Hzh9orIRJy6pm0BjWcN_Ui_vODaBfW7tpfzaE91na5i5I7zSX4mB0TWzLI036YS458xSztVLih06jprJqFno4PDHjJWD5fCZG1d_r1x4y8hnMrGQw1JUAoJ4u6wxzXr7XSUCBvTJti-c_qCXRNQIAzl6C5mYmMJRyrzNmXPL1gNbVwi7gBgjZpTB7K4YYqmvPx7BDppATxw5AVjk28F7afgzg0LYrCHhrbiiVOMpzjQljOa0iQJWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=D13B6JkZV6cXihO5wEnSJ7ap_xXrGRLELGmES7Mtu-P0AjgB84y-GpiV_bv4zKiF709xhnfjQRoiQrd9EV8i-GfEiboLWyu-BcVXCzBzFPwf9QfPdUuufpjmTQdJ-4woNU-nuwklc75UP_QGqAv2L0VzciZGIKPSw_Ms8JFUgrKnwXYdFd-Ep0eF7dUu2rabMFZS3YodiTob9DDubtx5_SvR893qnJfyfNU4EqkCXJ5JZSk-iQ4oA3tJq4GQMp3ZXrPydD8q0tcyPhFvbX3uL8lnpvwM8NTS1FXhQQXKhsOJE2bQmDtxFKQT1v__A3ZUl19KDYCVm9lk9EdwVxwqfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=D13B6JkZV6cXihO5wEnSJ7ap_xXrGRLELGmES7Mtu-P0AjgB84y-GpiV_bv4zKiF709xhnfjQRoiQrd9EV8i-GfEiboLWyu-BcVXCzBzFPwf9QfPdUuufpjmTQdJ-4woNU-nuwklc75UP_QGqAv2L0VzciZGIKPSw_Ms8JFUgrKnwXYdFd-Ep0eF7dUu2rabMFZS3YodiTob9DDubtx5_SvR893qnJfyfNU4EqkCXJ5JZSk-iQ4oA3tJq4GQMp3ZXrPydD8q0tcyPhFvbX3uL8lnpvwM8NTS1FXhQQXKhsOJE2bQmDtxFKQT1v__A3ZUl19KDYCVm9lk9EdwVxwqfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هوش مصنوعی حالا می‌تونه با YouTube کار کنه!
یک قابلیت جدید به نام youtube-skills به ایجنت‌های هوش مصنوعی اجازه می‌ده فراتر از باز کردن ساده‌ی ویدیوها، مستقیماً با محتوای YouTube کار کنن.
🤖
🚀
قابلیت‌های اصلی:
🔺
استخراج ترنسکریپت کامل ویدیو همراه با تایم‌کدهای دقیق
🔺
جست‌وجوی ویدیو بر اساس موضوع و پیمایش کانال‌ها
🔺
دسترسی به ویدیوهای جدید و محتوای پلی‌لیست‌ها
🔺
دانلود زیرنویس‌ها
🔺
پردازش گسترده‌ی محتوا؛ از جمع‌آوری ترنسکریپت‌های یک کانال یا پلی‌لیست گرفته تا تحلیل چندین ویدیو
🔺
امکان انجام تحقیقات عمیق با بررسی هم‌زمان چند ویدیو درباره یک موضوع
📊
یعنی ایجنت می‌تونه ویدیوهای مختلف رو جمع‌آوری کنه، متن اون‌ها رو استخراج کنه و برای تحقیق و تحلیل از محتوای YouTube استفاده کنه.
⚡️
مناسب برای ساخت AI Agent، تحقیق، جمع‌آوری اطلاعات و تحلیل خودکار محتوای YouTube.
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qO62sGU1UcCrT_dHw_s7sQKxpDPU1GagaNgSNL_zEL6l714JMJQTJsd2vqmeKLtLK6gq01tJz9AjcH0Sub5wVs9duy7Vn8IvEXNxnoNTsXCIzTRYIAMSa5OOvxNmWF7IiZm1npdVnnC-bOD-EgcveVNNOIOia-_qtwQLbBvFAedj6Y_VsQrIXMoeX8fPJ-zbObT9C9qSfoUINHqlLrmAxK9xcLHwHixrc-YEHy1W1eu5gWzvTbvz9g1rALgtePyGPxe_cw_tZIvMO6ev5rZFy2edaYVb8GSOTBoOZxZeeIJoxVUw96MpgMjWm7Qu5xJ601kFz2U-UvTWSKX_bl8rCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">200 دلار برای دسترسی به مدل‌های هوش مصنوعی محبوب
💥
🆓
Kimi K3 | Deepseek V4 Pro | Deepseek V4 Flash | Sonnet 4.6 | Haiku 4.5 | GPT OSS 120B
✅
کافیه با جیمیل ثبت نام کنید و یک کلید API دریافت کنید تا 100 دلار دریافت کنید
✅
📌
Base URL :
https://api.you.com/v1
📌
Example Model ID :
kimi-k3
حالا برید بخش تکمیل پروفایل و یک ایمیل با دامنه ناشناخته وارد کنید
مثلا تمپ میل
سپس 100 دلار اضافه دریافت کنید
😎
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🎯
چالشی بزرگ برای وایب کدر ها به همراه جایزه
اون لحظه‌ای که به یه دایره چرخان خیره شدی و منتظر جواب هوش مصنوعی موندی؟ Commons میگه این وضعیت روزانه
۳۰ میلیون ساعت
از وقت آدم‌ها رو می‌بلعه و حالا با پول جدی می‌خواد حلش کنه.
😎
💵
🎮
چالش چیه؟
به‌جای یه پروژه‌ی کلی «چیزی با AI بساز»، این‌بار هدف مشخصه: زمان انتظار برای پاسخ هوش مصنوعی رو به یه تجربه‌ی سرگرم‌کننده تبدیل کن. یه بازی کوچیک، یه تجسم تعاملی، یا هر ایده‌ی تازه‌ای که به ذهنت می‌رسه.
🚀
⚖️
داوری روی زیبایی کد نیست؛ روی کیفیت خود تجربه‌ی انتظار، اصالت ایده، ارتباطش با AI، قابلیت استفاده‌ی دوباره و کیفیت اجرا تمرکز داره.
💰
جوایز:
🥇
نفر اول → 20000$
🥈
نفر دوم → 8000$
🥉
نفر سوم → 4000$
🏅
رتبه‌های ۴ تا ۱۹ → هرکدوم 500$
🔐
+ 20000$ جدا برای بخش ویژه
📌
مراحل شرکت:
ثبت‌نام تو
commonsmade.com
← بخش Hackathons ← Join the hackathon ← ساخت پروژه تو بخش Code ← وقتی آماده شد Publish کن و تو Hackathons ارسالش کن
✅
🗓
مهلت: ۱۷ سپتامبر | کاملا رایگان
اگه مدت‌هاست دنبال بهونه‌ای برای یه پروژه‌ی وایب کدینگ بودی، این هم خلاصه‌ی مشخص داره، هم جای خالی تو نمونه‌کارت رو پر می‌کنه، هم یه جایزه‌ی جدیه
✨
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzkYbTfIGVQkIe9KXf_2C-WNJKZK1sklvPes7IYR_9OU0x79aXpIz4ImMjGcUC82bn9EYhh-afHSCg85RTS6Ttk8jBrt_GbS28zBy8_rbjGK91v4KKQY6wuUx3iCqnfa9Xs-t0M9cG4YJjNqrRTC_zVzXUFsNo9poCJsPWCqSa7eXpsPJhIDPWs3hPVRpsEKxX1JbsXAc5c6LM9QkEAi4QEZOwmylZR-PH7iJaxSUhBCP_XSCHAWEmAAvnyOuL5hd6-3U7jrDTHlN121z2RyPeeUCHoHkkY7Sy8iOwoxNMZbJbm4hk0xjb6mYgTjwqE7GM_Lx5FWYZgxh1AbA00cag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت
z.ai
کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه:
۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan:
هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید عادی
: یک‌بار ۱۰۰ میلیون توکن رایگان موقع ثبت‌نام (تا پایان کمپین باید مصرف بشه ، با اکانت جدید ثبت نام کنید )
⚠️
توکن‌های رایگان فقط داخل خود اپ ZCode کار می‌کنن، نه از طریق API.
🔗
لینک سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=ahEl8G3im9GT13YfPduOZIcPtM6HKOQc8dwL4aF8zvpfi2CXH3qXE8iDHWmo2He16wEKEFTYTu7AZq7cJ2z0ugngVtwAO1wKn3_OiWXUDkHX-7iO3fzIwT6MdNs3fpSemn-z2Qsa1iGMz-XvhFLiwddFP2CRUBKQK00nVFFStSLzhlWJVN17uZM9ADIsrUBT98xIFX2VCwESKK6a5yWLHV6-AwxJbyBcdOdo4f1EXYyJQvq8GwRjdmIF-neeYPLIoMXcadCdmGLt0uCNto3qmegFrZ8CTIpjrqgIqSEXM4RqiZItg1jmtIMCvCAMBxi30kpEafAIm9JkNUZmcPeMJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=ahEl8G3im9GT13YfPduOZIcPtM6HKOQc8dwL4aF8zvpfi2CXH3qXE8iDHWmo2He16wEKEFTYTu7AZq7cJ2z0ugngVtwAO1wKn3_OiWXUDkHX-7iO3fzIwT6MdNs3fpSemn-z2Qsa1iGMz-XvhFLiwddFP2CRUBKQK00nVFFStSLzhlWJVN17uZM9ADIsrUBT98xIFX2VCwESKK6a5yWLHV6-AwxJbyBcdOdo4f1EXYyJQvq8GwRjdmIF-neeYPLIoMXcadCdmGLt0uCNto3qmegFrZ8CTIpjrqgIqSEXM4RqiZItg1jmtIMCvCAMBxi30kpEafAIm9JkNUZmcPeMJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌍
Pythia — رادار زنده جهان برای هوش مصنوعی
ابزاری متن‌باز که وضعیت لحظه‌ای کل دنیا رو جمع می‌کنه و بهت میگه احتمالاً چه اتفاقی قراره بیفته
🛰
🔺
بیش از ۴۰ منبع خبری و اطلاعاتی رو هم‌زمان رصد می‌کنه (اخبار، درگیری، بلایای طبیعی، هشدار آب‌وهوا و...)
🔺
پیش‌بینی از فردا تا یک سال آینده
🔺
کاملاً رایگان، روی سیستم خودت اجرا میشه — بدون اینترنت، بدون سرویس ابری
🔗
لینک گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=DW6EsPH13LQ-Zk8rmuZUru-HjXJ9ARJcIxJ44ExLBgYZ1W9aznwX3MltXF5GaRQ5iwxFU0cFSDcBeZ3Tn2zPVE4VKiajNHVtnQTH3z6BySEVuIy5uqZUnAEmybSXxQLfkgFeefXsHNYLcbYsAYUIpPYRPrkVIxqb-julGHCX6tBk4_y3vYQb917chuy05PLqZG47CAI6fuWk8vhtkBwfIK_6NDFXP94PA2IdJS7j1Zp0-uGoy-nglz-mktVEdKzHWfWg-Lt93ePe5g97iyrCJwPVbEv7OCOL5UgB84ASLYKOpXBULbTKMpWAmqBVXXZqP6GdeuFOTtOiaWOVQz1dzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=DW6EsPH13LQ-Zk8rmuZUru-HjXJ9ARJcIxJ44ExLBgYZ1W9aznwX3MltXF5GaRQ5iwxFU0cFSDcBeZ3Tn2zPVE4VKiajNHVtnQTH3z6BySEVuIy5uqZUnAEmybSXxQLfkgFeefXsHNYLcbYsAYUIpPYRPrkVIxqb-julGHCX6tBk4_y3vYQb917chuy05PLqZG47CAI6fuWk8vhtkBwfIK_6NDFXP94PA2IdJS7j1Zp0-uGoy-nglz-mktVEdKzHWfWg-Lt93ePe5g97iyrCJwPVbEv7OCOL5UgB84ASLYKOpXBULbTKMpWAmqBVXXZqP6GdeuFOTtOiaWOVQz1dzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
شرکت Anthropic ابزار رسمی بررسی محتوای Claude رو منتشر کرده
راهی برای فهمیدن اینکه یه فایل با Claude ساخته یا ویرایش شده — مستقیم تو مرورگر، بدون آپلود
🔒
📎
دنبال یه نشونه امضاشده (C2PA Content Credential) می‌گرده که Claude موقع تولید عکس، ویدیو یا صدا داخلش می‌ذاره.
🖼
فرمت‌ها: عکس، ویدیو و صدا (تا ۱۰۰ مگابایت)
⚠️
محدودیت‌ها:
🔺
فقط نشونه Claude رو تشخیص میده، نه هوش‌مصنوعی‌های دیگه
🔺
نتیجه «پیدا نشد» یعنی نامشخص، نه «قطعاً انسانی» — این نشونه با ادیت یا اسکرین‌شات پاک میشه
🔺
هیچ اطلاعاتی درباره سازنده فایل نشون نمیده
🔗
لینک ابزار
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=LWx6RHI3Q_IS0a98V6xf2EqSb_n3usTknULROELVrbKV0qBkI4xh3cm3sTbFLzjLRrocJcCwI9XKOqyT2gGeEGILpXY9nX03rTHhahIKEVIw_446o68WwCAV30UnCc22b_00Guxr62v8Zua8MlEr_7vk7v9jgxnSqBvwXE0gZPgAeZNS8iQ2SeCWPprv_UvELSuJuz3fXsMQyWuGv4Z444mChcs0z73GQhQQY6ADreb9MuZbYXBJOLL3W0hEmawN7j2l9WE4KGq4OjoZkIkIpYpLfmhH1KL8XWzNfoLaNCnZiFexat9T-sFcG3lQWc00ivgwnSRCwauKTcJVArfv-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=LWx6RHI3Q_IS0a98V6xf2EqSb_n3usTknULROELVrbKV0qBkI4xh3cm3sTbFLzjLRrocJcCwI9XKOqyT2gGeEGILpXY9nX03rTHhahIKEVIw_446o68WwCAV30UnCc22b_00Guxr62v8Zua8MlEr_7vk7v9jgxnSqBvwXE0gZPgAeZNS8iQ2SeCWPprv_UvELSuJuz3fXsMQyWuGv4Z444mChcs0z73GQhQQY6ADreb9MuZbYXBJOLL3W0hEmawN7j2l9WE4KGq4OjoZkIkIpYpLfmhH1KL8XWzNfoLaNCnZiFexat9T-sFcG3lQWc00ivgwnSRCwauKTcJVArfv-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت Dola مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5Oqab-6cOqSpIRkQzbZdhh5NlySa4f69c0LDj-SVyDnnSRIPHQ15qomnQeMl1t7xOscWa9ibnzAFnaxgGIdqQkPpcuDPCU_LWeW9JAFDYwo4xW9SjrHdtO_uyFSnUCVyGMWVUIMa-RbYLVSMKwU7t9o49T_0pegnevnGQ_HTN1PoHqZNF2SKLREw9fLlNZ8CqQyNcPHIptlPzgHZyPfRuu6zGKTff5cgtNns4EEHy_YUAPS1dndRZSOkjggx61fdB_uhwxIJiU_RIyB8aqFBmZ1-O3PTAzshGq3UwsTqsUZq19k0Dfb_6_oXSVtKQecLrfJ0pcX_nfQWaXHmecQeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن API رایگان GLM-5.3 از طریق TokenRouter
💥
🆓
بدون کارت اعتباری، مستقیم قابل اتصال به اپ، چت‌بات، اسکریپت یا هر ابزار هوش مصنوعی دیگه‌ای
🤖
📌
راه‌اندازی:
1️⃣
ثبت‌نام یا ورود به حساب TokenRouter
2️⃣
ساخت API Key
3️⃣
تنظیم Base URL:
https://api.tokenrouter.com/v1
4️⃣
انتخاب مدل:
z-ai/glm-5.3-free
⚠️
نکته :
به دلیل رایگان بودن ، مدل کمی کند هست و باید در ساعات خلوت استفاده کنید ، محدودیت و ریت لیمیتی اعلام نشده ، این پیشنهاد به مدت محدود در دسترس هست
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=tiyCsrrRfIg4fOpSsDFWW0j2o5txYozGEf-4RF36XNU4ykahu1FwAJb_RAAL8kS_DPiMu6JJkR9GnVGw_eIXhG1DUfJgEsN_5LbiEEQlb2leSNoN7PteQFY-oOTuxt1S_c4SVKzX-lmiUcH2RbPh_GPtKdcVEAUeHm37IMyXbNvn_BJ8peUvSSPcdR_litA7StbR9NwWXj9903jMmyuE97ith1dx-VWZ9zNStSN6fCanMGiXdiyCce4pEdiWcIAbj-H_LZE3bim63-zNWqjch73hzSglmQrqZsKXPX7FCmy_GyUWhQXxUN1eYxdpsSyaAAt6U99-dZsUBWHe8P1XIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=tiyCsrrRfIg4fOpSsDFWW0j2o5txYozGEf-4RF36XNU4ykahu1FwAJb_RAAL8kS_DPiMu6JJkR9GnVGw_eIXhG1DUfJgEsN_5LbiEEQlb2leSNoN7PteQFY-oOTuxt1S_c4SVKzX-lmiUcH2RbPh_GPtKdcVEAUeHm37IMyXbNvn_BJ8peUvSSPcdR_litA7StbR9NwWXj9903jMmyuE97ith1dx-VWZ9zNStSN6fCanMGiXdiyCce4pEdiWcIAbj-H_LZE3bim63-zNWqjch73hzSglmQrqZsKXPX7FCmy_GyUWhQXxUN1eYxdpsSyaAAt6U99-dZsUBWHe8P1XIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثر های شگفت انگیزی که تا الان توسط GPT 6 Astra خلق شدن
🚀
✨
🔗
منبع اول
🔗
منبع دوم
🔗
منبع سوم
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7622">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBwo9q9mJzcY07qN-rMCHnNfjbsVtQ03ieYU6HpzwGOMp7arIhOARSJXO_qQZ4cEo8oUPvUS6KG90xH8_QwQ2onNETifgjxZaMerddRyzTB7g-HRRr43sgF2j_ZN-cgsJVind5W4ATfZjr3qDqyTZjFtNq0nDe9MrBqeJQz6nrXB5G2LSwRch-n1gy640XWCZpjtnpa4QmKbxWgK1UnAUzrXfiM45VbgiKB9fXes-jHrMBFjqS3AwLhJ3CmWh2kR2oL2V7XiC3AKg0ChktCODdRjovlbpcbAURkBsKY5PovaVo_a9jsuD88nq5lloc3nQ2dNN2LvxfrqrrPf10NcNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ek2Q6Nv0osDuaJ211SdeiYSKYoLfev7rhKNszZXFS6_jzUeQn_PKSKkZrMrzGFdzw4_yHJ8wMTsbVH5lg2jMSHBZ9t33R9_6hT6NrrzTaWrNHWLVFMnyhcbGwRSTem_UdrElZYPA9yTHQWVH_doYp4Ml0UzWXXvJke3n8jBf7mq67TUTHJlsg9W1CXy6InQQDC_eceTWsIHVf69N3eqmxr_aMZ7DD3FoekKm_aHoJpFSDFkEdW95GT8PkvQy7cXiBUc6MT7r7eiK6nRw2YCippGShDCW7f3wZAP2pDBHRqKaWVp1L75QWy-m3mqNKI6Dah5F1Zg8qOReaZolOepa_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAarksHhMjPj8KFNAAetXsPrOJXB61VXRlJUcYTJV8PRE59xCUTGlaMqgVe8klll8x-ZFwYi2bt5SxhOzR7__QjBCSBZ5k_g1w96dg5-S_cgtL3wDjA2bb9pzlWxZ1Pg1AK7uA6Eebfg2AbRyE5KDkoY3oOXvkCecoJP-Gapn9ieCIy6DD_vaUOU1TIpAcNVXVEvAX9A_YSegS2CdJfzLnEPQNGgoomniAzAgNCJK2ER4-jFXhFZY4Wh_Bi4XWBHFY5NwKMty_GrFeRy42pCTpCX3so4rqc-DTlYRlKMtcZEsI_dgfAIaUSg5KIOI-0i1hvD1rqhKpufD6_gxZOy0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1rIjMMmYaqAIeseZSCwn2DOvc9CujuY9hrWc_7k6LH9vovEaG4o9L4DWI3V1Gdnf6QIOVFiOlsFtCYd038krv8td55qLlQv27_ejZSBtxo4nVJGDn-fGM3BDQhg9-J8NrxeKaSF7Ro8IaCFHIbI42TvO4SrnVO-Y6bAIccI8dD945LFVMHp5uvgtNZC-lQsZsPAuAbgfw3trutttlp8TSixf94CnpwJ4qmDNSUDG242EOJwMTwOI7C5Hk8v-tjroGGGx5oKP3PvNUhGOI5VmL9iP9X1iiYXl98nn1eNy_QmHaXDXv7To16cx7vrqNg_BBhEc-vsn5gODv4-C1imVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
