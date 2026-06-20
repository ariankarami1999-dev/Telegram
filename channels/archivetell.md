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
<img src="https://cdn4.telesco.pe/file/Z37a9DRXh6UxHrlp9BlJVFK0TS3DPLEaBViAkcr9kkYcWxU5BQYIhiyguRLk8i0jBZ-MjDaKBc1Lr5FS-XXJeOb7iXCid4_C2PKrlXlB4AV6U33Moy7dmCFz8_uK9d19SS5En3mZ3QdKizApCFbNTyCSIv7ALGFjX18PL9gkF9WR1PYKrp1917fSiz-_TRjp03bj9DkPLbO3lES0mEhIpkweZ6f8B1MyB-umZ1pSaLjDw8ej2bLTfKlG0eEnayh0E2lJA-lR3xg8tI86kObMgQOJRbNZ2EjcNUTvq5bEKNtLyL6dBA-LsVon3iqh4NoSwyM4Vm3qPhFV-gFq7xcSgQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.65K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 15:53:56</div>
<hr>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚀
🔥
ویژگی‌های کلیدی و پیشرفته:
1️⃣
تبدیل سایت به اپلیکیشن: هر سایتی که فکرش رو بکنید (مثل ChatGPT، یوتوب، ایکس/توییتر، اسپاتیفای، دیسکورد و...) رو به یک برنامه دسکتاپ مجزا تبدیل می‌کنه.
2️⃣
حجم فوق‌العاده کم: برنامه‌های ساخته‌شده با این ابزار تا ۲۰ برابر کمتر از اپلیکیشن‌های سنگین مبتنی بر Electron فضا اشغال می‌کنن.
3️⃣
سایز مینیاتوری: میانگین حجم هر اپلیکیشنی که باهاش می‌سازید فقط حدود ۱۰ مگابایته!
4️⃣
مصرف بهینه منابع: به لطف استفاده از قدرت زبان Rust و فریم‌ورک Tauri، مصرف رم سیستم به طرز چشمگیری کاهش پیدا می‌کنه.
5️⃣
پشتیبانی کامل: این ابزار کاملاً رایگانه و روی ویندوز، مک (macOS) و لینوکس بدون مشکل کار می‌کنه.</div>
<div class="tg-footer">👁️ 721 · <a href="https://t.me/archivetell/6462" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxmqW4zZ_Vdhy1Mo8WGx3pCJZolq7Ccyo6-eUU55V0l1JGuuQExhGabBqt7G6WKqaYmJF3rviSPQj832cYgVTceWfbsJfEd9Zi1S-_QAVchdm6COVPw43uP-V5hB0HvLqLVX2UOO6jj6_aU_ThDiVn0k9WG4dL6zTThR7fcX0MGN0ziOFQRT8Ma5snzlGYd9aSo5hZj_H33lJe1z7KwvmbR8SJcLTdY_Zh1OejNEA69oheFAAtnf5b2BYh4mll24qfRC5JmKAi2eYF4QFMcCEyIgGcUanvM0FHXYFatj6YPn2csekKxK6mP55FZo3SRC9YEGhihiSWyuePuOvN9zbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1jSBM2YaPHnfmUz9ZUxG2pUYZygQZRS23eHFzLLHAea5qzfDK47IXq5qmJ4w5BvCnqPpxYpV4h3vJx_vBSkH9zjxenTLhVeaNuVG0_52PwUWgOUL9zdBHgwSO-lcUZ0rCFvWr8_a3YtFuBiFLRjOVj9iyO3zbOOXLfW5jo70tba_LlfmXx4k3K2Ml6XMihl1hOSHRewDWq3xhDFCFqbdxvNYdmOWfuJ69xbwTeFs0kZ9ydu5zG-RFm_wfrkvaq9VXDjxqniC-v63n3E-MrEgBCUoj9fMVOFOQ2Sonl5biamXa3cSc6fvbY-hBqztdmybY9zWTWg8I-ddJlMd9rEVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6BgPBMHShSg3e6Dz-7zK35-OjAO9P9SWogLS0FygrGuoX7ZfpeslapryfRdCkQ3N2Y-L8jAMje-oNM7jN9p2aeHojoRK1QOfUp79-NiZJjUPUsUFQ2equlyOlHID5p1BB-AJwMNExcfqol1ZyIOcO1SiFuz2m6HXQuTUl53aafBpar4GSOyQ96pWxYUOaNhRzkR6g7CnL2ZzjA2gbUXc5xDU-ES-PEpvCgeH99ApjE-LbYRzg971E1YMtYyFLmFbiOuLAibH7y4FkCZc0bFzSQ3qsPTGiHR6dJ2HSRle4gK3OuE4oiIf4tcFfXAXiSceg5oY2zg9dAiCGl_JkS0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Or9uiw14GGC2igPcAzDNpBsNKSXHyo44bX2P9n8gjomdCfeqlBL02vBYhuq-kiwLTgPQd7NFxnqGWz4VM8Svhfz2WVyQ7Bi-UI7kHcO7aihPyflVWWHSZecjDAthe-qd7xJ1OxtlYjyBN9cIcbUl5gdTOa2e2cCCrHCm_p5qkYy-K_GCm-hRW9pUL2Aty64JuKEUN4Ifk0nKyf080wpCkC3lOkV1llaKswKWoTbK_QLiHkweK2H3FLert3kdB5LtKxlYaft6rEW0Cw6IuQGpQdEB2vn_AGqABI3a-gco8-cCZHInFB9gM8bLc11Zr3Y4hTIBqA9a5VfhtMU1LAfyPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ded905356.mp4?token=SivPGiZqbnu81tlVdJVV4SZ6e59aAm4JLOLsr-gKwov0sk9k6YPN_zaofXS3fhz6wbiSeyjUpBo32fTrzWIsBUOxfUcnUR2pZLlTkDUR-IDK1ZHuTmPqSfABPhGJ1hXCBLntKQowsSfuqt6vnhZ0z41XklozYOK0CFS3tiR3mTtBubEK6ttoschOKW9kh3Cnufar-izPNoBWJWWfXFNgwMlXYORUbTqdAmd4QTWLhK_1ieX_jUABjiPebnmK5l047wc93r3pT3ZGHIW5YIpbX_O860oPPmUfV_GXFoufJHRJxssw3oYszKy7bbSeQFZcxLhKbALGtuFhfw-BuYVkNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ded905356.mp4?token=SivPGiZqbnu81tlVdJVV4SZ6e59aAm4JLOLsr-gKwov0sk9k6YPN_zaofXS3fhz6wbiSeyjUpBo32fTrzWIsBUOxfUcnUR2pZLlTkDUR-IDK1ZHuTmPqSfABPhGJ1hXCBLntKQowsSfuqt6vnhZ0z41XklozYOK0CFS3tiR3mTtBubEK6ttoschOKW9kh3Cnufar-izPNoBWJWWfXFNgwMlXYORUbTqdAmd4QTWLhK_1ieX_jUABjiPebnmK5l047wc93r3pT3ZGHIW5YIpbX_O860oPPmUfV_GXFoufJHRJxssw3oYszKy7bbSeQFZcxLhKbALGtuFhfw-BuYVkNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
با Pake هر وب‌سایتی را به برنامه دسکتاپ سبک تبدیل کنید
یک پروژه متن‌باز برای ساخت اپ دسکتاپ از سرویس‌های وب مثل ChatGPT، YouTube، Spotify و Discord و ... است.
✨
قابلیت‌ها:
•
🔹
تبدیل هر وب‌سایت به اپ جداگانه
•
⚡
اجرای سریع‌تر و مصرف رم کمتر
•
🛠️
ساخته‌شده با Rust و Tauri
•
📦
خروجی کم‌حجم، معمولاً چند مگابایت
•
💻
پشتیبانی از Windows، macOS و Linux
🔗
لینک:
GitHub
#OpenSource
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 835 · <a href="https://t.me/archivetell/6457" target="_blank">📅 12:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇺🇸
ترامپ: شرکت Anthropic دیگه تهدید امنیت ملی نیست!
🤖
✨
به گزارش Axios، دونالد ترامپ بعد از دیدار با «داریو آمودی» (مدیرعامل شرکت Anthropic) در حاشیه اجلاس G7 اعلام کرد که دیگه این غول هوش مصنوعی (سازنده مدل‌های Claude) رو یک تهدید امنیتی برای آمریکا نمی‌دونه!
🔥
جزئیات و حواشی این توافق:
1️⃣
ریشه اختلاف:
قبلاً سر آسیب‌پذیری و باگ‌های خطرناک «جیلبریک» (Jailbreak) تو مدل‌های
Claude Fable 5
و
Claude Mythos 5
اختلاف شدیدی بین دولت آمریکا و این شرکت پیش اومده بود.
2️⃣
اقدامات قبلی دولت:
وزارت بازرگانی آمریکا تو ۱۲ ژوئن محدودیت‌های شدیدی اعمال کرده بود تا دسترسی تکنسین‌های خارجی به این مدل‌ها محدود بشه.
3️⃣
همکاری و چارچوب جدید:
الان Anthropic با درخواست‌های اصلاحی دولت کاملاً راه اومده و کاخ سفید به همراه چند نهاد امنیتی در حال تدوین یک چارچوب فنی دقیق برای ارزیابی خطرات مدل‌های هوش مصنوعی هستن.
﻿
⚙️
سیاست کلی آمریکا در قبال AI:
ترامپ تاکید کرده که هدف اصلی، حفظ برتری بی‌چون‌وچرای آمریکا تو رقابت هوش مصنوعی با چینه و اصلاً قصد نداره با بستن یا تصاحب شرکت‌های داخلی، جلوی رشد این صنعت رو بگیره. البته این رو هم اضافه کرده که در شرایط اضطراری، از استفاده از قوانین سخت‌گیرانه نظارتی (مثل قانون تولید دفاعی) چشم‌پوشی نخواهد کرد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Anthropic
#Claude
#AI
#USA
#TechNews
#Security</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/archivetell/6456" target="_blank">📅 10:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqGnd-qP9-EqtNSSJS_fjYNg4B3SA0HMbs5qJE1m0-FcBeT7lnFLKTHwymRP_lsnHh5Oq4_sioRsrbZfVAr4L8As8gPcQA48dKvWb-w50XdybkW8bzE72pm-82WkQPagEpHKkfUAsU0DXViPXeKHailcqcE8Gc8snEjvT-FdKgCspgJar6JdBnH7MEZB5_XxU5VSy55EPhXnw4AhiLgHWWMkwVh1iLgRWk5eTAxJV-TlaeyjFRqADFkWisLIFxYFBnzdBZpbUhP_tN1QmmbH6hmPUWDzwF8UK0OAFVCFJ1pXcIAEM9VLJQMt3oor2pKH9L16lxwuOtqP-GnDeprHOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">KillerPDF
جایگزین متن‌باز و سبک برای Adobe Acrobat
📄
✨
ویژگی‌ها:
•
🪶
مخصوص ویندوز 10/11 با حجم حدود ۶ مگابایت
•
✏️
ویرایش متن داخل PDF
•
🔗
ترکیب چند فایل PDF
•
📑
استخراج صفحات انتخابی
•
🖊️
نقاشی و افزودن امضا
•
🔒
اجرای کاملاً محلی، رایگان و بدون تبلیغات
🔗
لینک:
GitHub
#OpenSource
#PDF
#Windows
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/archivetell/6455" target="_blank">📅 08:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚀
مدل جدید Janus Pro از DeepSeek منتشر شد؛ پیشتازی در تولید تصویر!
🎨
✨
استارتاپ هوش مصنوعی چینی DeepSeek به‌تازگی گزارش فنی مدل متن‌باز جدیدش به نام
Janus-Pro-7B
رو منتشر کرده. بر اساس بنچمارک‌ها، این مدل در زمینه تبدیل متن به تصویر (Text-to-Image) تونسته عملکردی بهتر از رقبای قدرتمندی مثل DALL-E 3 (از OpenAI) و Stable Diffusion از خودش نشون بده!
این مدل در واقع نسخه ارتقایافته مدل Janus هست که اواخر سال گذشته معرفی شده بود.
🔥
ویژگی‌ها و بهبودهای کلیدی:
1️⃣
کیفیت و پایداری بالاتر:
با بهینه‌سازی فرآیند آموزش، ارتقای کیفیت داده‌ها و بزرگ‌تر شدن سایز مدل، جزئیات و پایداری تصاویر به‌شدت بهبود پیدا کرده.
2️⃣
تغذیه با داده‌های غنی:
در این نسخه از ۷۲ میلیون تصویر ساخته‌شده (Synthetic) باکیفیت در کنار داده‌های واقعی استفاده شده که خروجی‌ها بصری بسیار جذاب‌تری رو تولید می‌کنه.
3️⃣
مدل ۷ میلیارد پارامتری:
این مدل با ۷ میلیارد پارامتر، درک بسیار بهتری از دستورات (پرامپت‌ها) داره و سرعت و دقت تولید تصویر رو به سطح جدیدی رسونده.
📉
تاثیر دیپ‌سیک بر بازار تکنولوژی:
جالبه بدونید اپلیکیشن دستیار DeepSeek (مبتنی بر مدل قدرتمند V3) اخیراً رتبه اول اپلیکیشن‌های رایگان اپ‌استور آمریکا رو فتح کرده!
موفقیت‌های خیره‌کننده دیپ‌سیک و صدرنشینی مدل V3 تو جدول مدل‌های متن‌باز، حتی باعث شد تا سهام غول‌هایی مثل Nvidia و Oracle در روز دوشنبه با افت مواجه بشه. (شرکت‌های OpenAI و Stability AI هنوز به این خبر واکنشی نشون ندادن).
🔵
@ArchiveTell
| Bachelor
⚡️
#DeepSeek
#JanusPro
#AI
#DALL_E
#StableDiffusion
#TechNews</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/archivetell/6454" target="_blank">📅 02:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SuKitqaby5iyJ7YvD2SZ-OkvBdMde8t8kVldo_rmyGavZALgWIKFkHjHgXCNZ_pMC8CQl7Z6zb0m4_azLKoIITojVwP1iVWKRQvPPhsSM_bNfmp4LtX_eDmlicmM0dxHOHUBYC7Lwtbvv4PBCiHnHJBWiB9KaIjc0JKcawDaHx0zyz8VrSYCu4pdXOfIGz-MwN3QZXx3rrFPOvncJlboDbJlrFQxfcUoqR3a_dQMW_xvYT9tk1MV7mPyQ9B2yyRxxVW-fELLKn_6ouARdv_dbrmNfA67-Luj_8aif0Ked9w21cpUCRugPCjl5abHMltrK8kafH504CQFkmrX0vnbNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JfVOHgPka5BRdgW7Fiu8xu0ZO-UxH4ivUazcVMXzKoqtztgQGi4JlJGsQCDvHMEdTcYdf5rzHRoUsTKQomHYdFQTJYbOW6pLPZfoBQAvchbhZv3osxCUPu8hwHeLa2jQ3dAuwuC4Kt6sIZM63WdkEJa3O8l7hbMQHVdKhmbrj4iPqVKEfLq_5W1Vo683C1_Uo_eiIfAmiZRFScdzaFNAcXFIM1s9JPfjaZ2vv9dR30JpGFOi1FLXef5J5j_U6wSdddtY2BPGvFsZeKY-ZgwdlPIltmkloOpPwfC3jHGfR_d5KESu_Ol3Sg3MYQz5BzbmSX75HcUAoesunQIUBt9AlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Product photography on a solid sky-blue background, soft studio lighting, no shadows.Product photography on a solid sky-blue background, soft studio lighting, no shadows.
Two thick, fluffy, plush terry towels are neatly folded and stacked one on top of the other, deep soft folds, thick looped pile texture. Top towel: white with thin blue stripes. Bottom towel: solid cream. [product from uploaded photo] rests nestled inside a deep fold of the white-striped towel, partially sunken into the fluffy fabric. [product from uploaded photo] lies diagonally inside a fold of the cream towel below.
Water droplets cover both products, fresh just-rinsed look. Top-down angle, empty blue space above for text. Photorealistic, high resolution, sharp focus, no text, no logos, no people.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/6452" target="_blank">📅 02:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXOzvkNUEqitBBNdJiz3nt_4eCRTmqpSxhVSuX752PZjJa721TFghHmyOOsHwqQsIQLDdsn_nc6H1X56x-yZhnVxzGPFunL36FCn7H00kknYKmP1vZbK_HpltoyG8dBbbvmPVLna8WDPH2WFYFm7Zf5EOqNVOKo29-GeFXjtiAMGtnM0GjyTwKE9XItklajz7TFB43lDqF8mvku1zcQF5-xexTtIaxKKBmtoMQnTVFPQ7EvNn9NCkt3jn3ol9xEh11-vU9RqoK5v0t33xwQ603mzoHKgkGvu_inbGb9ZyPnZjNanq8OSGngG5N6FrOgZCzOahDTmMEqU9g-aYR6H_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی BleachBit؛ ابزار قدرتمند، رایگان و متن‌باز برای پاکسازی سیستم!
🧹
✨
اگه به دنبال یه ابزار امن و کاملاً رایگان برای بهینه‌سازی و پاکسازی سیستم‌عاملتون (چه ویندوز، چه لینوکس) هستید، BleachBit یکی از بهترین گزینه‌ها برای حفظ حریم خصوصی شماست!
این ابزار با حذف فایل‌های اضافی، کش مرورگرها، کوکی‌ها، فایل‌های موقت (Temp) و لاگ‌های سیستم، هم فضای هارد دیسک رو آزاد می‌کنه و هم ردپای دیجیتالیتون رو به حداقل می‌رسونه.
🔥
ویژگی‌های کلیدی و پیشرفته:
1️⃣
خرد کردن فایل‌ها (File Shredding):
حذف دائمی و غیرقابل بازیابی فایل‌های حساس.
2️⃣
پاکسازی فضای خالی (Wipe Free Space):
پاک کردن کامل فضای خالی دیسک برای جلوگیری از ریکاوری اطلاعات قدیمی.
3️⃣
بهینه‌سازی دیتابیس‌ها:
فشرده‌سازی دیتابیس برنامه‌ها برای افزایش سرعت و عملکرد سیستم.
4️⃣
امکانات حرفه‌ای:
پشتیبانی از خط فرمان (CLI) برای اتوماسیون، اجرای پرتابل (بدون نیاز به نصب) و امکان تعریف رول‌های (Rules) اختصاصی برای پاکسازی.
🔗
لینک وب‌سایت و دانلود
🔵
@ArchiveTell
| Bachelor
⚡️
#BleachBit
#OpenSource
#Linux
#Windows
#Privacy
#Tools</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/archivetell/6451" target="_blank">📅 23:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🌐
ارتباطات آفلاین، امن و غیرمتمرکز با Nomad Network (نسخه ۱.۲.۰)
🔗
لینک گیت‌هاب
پلتفرم
Nomad Network
پلتفرمی برای ساخت شبکه‌های مش آفلاین با رمزنگاری قدرتمند، محرمانگی پیشرو و حریم خصوصی است.
✨
ویژگی‌ها:
>
🔹
کنترل ۱۰۰ درصدی:
بدون ثبت‌نام، قوانین یا وابستگی به سرورهای متمرکز.
>
🔹
تکنولوژی LXMF و Reticulum:
مسیریابی همتا‌به‌همتا (P2P) و زیرساخت مش رمزنگاری‌شده.
>
🔹
انعطاف‌پذیری بستر:
اجرا روی امواج رادیویی تا کابل‌های نوری.
مناسب برای دور زدن محدودیت‌ها و ساخت شبکه‌های محلی ایزوله.
🔵
@ArchiveTell
| Bachelor
⚡️
#LXMF
#P2P
#Reticulum
#NomadNetwork
#Mesh
#MeshNetwork</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/archivetell/6450" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6449">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTzgpLGww_NwbJFA-JfT4BTh45CSqsmHsWNk2UDkJplexJacRzHtyJ2bNhk74I0N7k0eJtDbxBoImXAo3nHcvrwI3otjNXdOBBpUcRjGq3h7RCmA9ljL_iW1lGYjM91D7GXjoYnpi2UpXUt8ev05qhO4WCd9u-FKIhGXl37pDXfWwSrFsxiVe8Ce-jjXlGLOR6Yx_WYeX1v1VhKdWYlmLjfbhv_4Uk0CnkZ-T46c6CiwasCRxCMuTJ8Fqcha6hgvBQsW1fWpDbsx5gZ6RLrv-X28z9lAKWL6NnmK8G9NkspyqCwXm4fbtJBHEtwRJ0lsRBQuN2PyTGG-j4JjXXXRM45rs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTzgpLGww_NwbJFA-JfT4BTh45CSqsmHsWNk2UDkJplexJacRzHtyJ2bNhk74I0N7k0eJtDbxBoImXAo3nHcvrwI3otjNXdOBBpUcRjGq3h7RCmA9ljL_iW1lGYjM91D7GXjoYnpi2UpXUt8ev05qhO4WCd9u-FKIhGXl37pDXfWwSrFsxiVe8Ce-jjXlGLOR6Yx_WYeX1v1VhKdWYlmLjfbhv_4Uk0CnkZ-T46c6CiwasCRxCMuTJ8Fqcha6hgvBQsW1fWpDbsx5gZ6RLrv-X28z9lAKWL6NnmK8G9NkspyqCwXm4fbtJBHEtwRJ0lsRBQuN2PyTGG-j4JjXXXRM45rs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Palmier Pro
ویرایشگر ویدیو نوآورانه و رایگان که با هوش مصنوعی کنترل می‌شود
📹
•
🔹
اتصال مستقیم Claude، Cursor و Codex از طریق MCP
•
🔹
برش، تنظیم ریتم، صداگذاری و افکت‌گذاری خودکار
•
🔹
درک رابط کاربری توسط AI بدون تنظیمات اضافه
•
🔹
ابزارهای جانبی برای تولید تصویر و ویدیو
🌐
Site
#AI
#VideoEditing
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6449" target="_blank">📅 19:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlL-DFNuxP4oeTEcZSH_d7UYw9E69hLwbUMdvY1fgXbGoNHMm4rz92ZDf631NmvV3usa3hVZfJHM3cNCqlnytibnqMHenXcqCpunWaWYMPfsvBtyiBVpHPn_JS9yWVISgsUxRYf12nAcq0UlvZinI1H5vr30c80lpnhJWrXEOHcN7TsrprPw0IddSQFQHL0Q5ZFYNIyNYZkzPZ-lrtzYVd05aYEh6R813lgRPW5FwQGsM4d3mVgxSS7QFXQsxA_OwwYDMae3BgzGDi4_qi4f7ovuS3f_ILESrYtGxd76huQOHImlRc2vtpnfF1fR2qJJ_DNgWuKMJ7s5J60Ux_rMBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اگه حوصله داکیومنت خوندن ندارید و یا پروژه‌ای داکیومنت درست حسابی نداره، به جای این‌که سر خودتون رو درد بیارید، یه سر به سایت DeepWiki بزنید و با کمک هوش‌مصنوعی، جواب سوال‌های خودتون در مورد رپوهای گیت‌هاب رو پیدا کنید. اون خودش داکیومنت و کد بیس رو کامل مطالعه می‌کنه و کار شما خیلی راحت‌تر می‌شه.
🔗
deepwiki.com
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6448" target="_blank">📅 18:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEuQIEbaakU1zr3ooaOx48JfjwJYMvhyfNQ3Ccg3J40pfhzaRTv2DvMj8S-18hR_5YWx2F6PBvFEivEzEJmlMnFynWcMLJ6BaHVwZ9lB7DCo6TibR73M2Pyi3dAucE-h6M6R_w3UwA1RXCnOpSfogembXmHyGm0Vc7UOXPx2MJmzBm0mMki_fz_W-3_WaGNhlgcJxrkAqkLrmu1N9XLlK4tGMW3wCKqoAa2hBxWdCkQqO46Cf9ANWbKbWR5ycp0wSA6c3UhHO7ub1AhCc0lqBFviRQd8tAhg9V2UdZXOm5y_zcqXU9n-gqcUGOrRo3GcByz_8y-B5pfIFtSnInd3nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت موزیک رایگان
🎧
https://freemusiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6447" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6446">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚀
آموزش استفاده از مدل‌های قدرتمند GLM در ابزار Claude Code!
💻
✨
اگر از Claude Code (ابزار برنامه‌نویسی محبوب مبتنی بر ترمینال) استفاده می‌کنید، الان می‌تونید با اتصال به پلتفرم Z.AI، مدل‌های بی‌نظیر سری GLM (به‌ویژه نسخه جدید
GLM-5.2
با کانتکست خارق‌العاده ۱ میلیون توکنی) رو جایگزین مدل‌های پیش‌فرض کنید!
🛠
مراحل راه‌اندازی سریع:
1️⃣
نصب Claude Code:
(نیاز به نصب Node.js 18+)
تو ترمینال وارد کنید:
npm install -g @anthropic-ai/claude-code
2️⃣
تنظیم API و متغیرها:
تو سایت
Z.AI
ثبت‌نام کنید و کلید API بگیرید. برای سیستم‌عامل‌های مک و لینوکس فقط کافیه اسکریپت زیر رو اجرا کنید تا همه‌چیز خودکار تنظیم بشه:
curl -O "https://cdn.bigmodel.cn/install/claude_code_zai_env.sh" && bash ./claude_code_zai_env.sh
(برای ویندوز باید متغیرهای
ANTHROPIC_AUTH_TOKEN
و
ANTHROPIC_BASE_URL
رو دستی توی سیستم ست کنید).
🔥
ارتقا به مدل ۱ میلیون توکنی (GLM-5.2):
به‌طور پیش‌فرض کلود کد روی مدل
GLM-4.7
تنظیم می‌شه. اما برای استفاده از نسخه
GLM-5.2[1m]
، فایل
~/.claude/settings.json
رو باز کنید و این مقادیر رو به بخش
env
اضافه کنید:
"CLAUDE_CODE_AUTO_COMPACT_WINDOW": "1000000"
"ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5.2[1m]"
"ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5.2[1m]"
⚙️
نکته حرفه‌ای در مورد قدرت استدلال (Effort):
با دستور
/effort
داخل محیط کلود کد می‌تونید قدرت تفکر رو تعیین کنید. اگه این گزینه رو روی
max
یا
ultracode
بذارید، مستقیماً به استدلال سطح Max در مدل GLM-5.2 متصل می‌شه که برای حل باگ‌ها و تسک‌های پیچیده عالیه.
💰
هزینه‌ها چطوره؟
استفاده از مدل GLM-5.2 تو ساعات اوج ترافیک (۱۴:۰۰ تا ۱۸:۰۰ به وقت پکن / ۰۹:۳۰ تا ۱۳:۳۰ به وقت ایران) ضریب ۳ برابر داره، اما تو ساعات غیرپیک (به‌عنوان آفر ویژه تا آخر سپتامبر) فقط با ضریب ۱ محاسبه می‌شه!
🔵
@ArchiveTell
| Bachelor
⚡️
#Ai
#Claude
#GLM
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6446" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TB3rvVZteb55DZj2Wy5Se9wWiLsGpXmGF-bz_hfpHSFPSJ9DUjdNdlnSExPZ-fAh_ptaSZjyoVtzx2szDwCySovIR9MndlRJSKx32kvrY_y06jKssz-zEiqxCcVNIuBovPrM66V4ng0OA6-TV-x-0AAjQtipKet0psnVwYRlqYqPbc_U05twPVtorSvRlqzAGllvZnIlCxnUK0icivE8V6YirjSL_6-uPgCn3K3I04HiBZ6EwM969FcaWnnsMDRicmTdPc-7Zx7k_tE72fdrjvGnCZ1AVomdFtx3ntu10E5QQ9xth3pRiVjfFa-Dy_ADxn_uawpFBxfyT9bUyCqGPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
۶۷ کلید ترکیبی پرکاربرد در لپ تاپ و کامپیوتر
⌨️
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6445" target="_blank">📅 01:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🎯
پروژه Universal Android Debloater
📝
این ابزار یه رابط کاربری گرافیکی (GUI) کراس‌پلتفرمِ نوشته‌شده با زبان
Rust
هست که با استفاده از ADB به شما اجازه می‌ده گوشی‌های اندرویدی
روت‌نشده
رو دی‌بلوت کنید (برنامه‌های اضافی و پیش‌فرض سیستم رو حذف کنید). نتیجه این کار؟ بهبود چشمگیر حریم خصوصی، امنیت و افزایش عمر باتری دستگاه شما!
──────────────────────────────
این پروژه متن‌باز (Open-Source) در واقع فورکی از نسخه اصلی Universal Android Debloater است که با تمرکز ویژه روی افزایش امنیت، سرعت و بهینه‌سازی مصرف حافظه توسعه داده شده و با حذف اپلیکیشن‌های غیرضروری، سطح حمله (Attack Surface) رو به حداقل می‌رسونه.
✨
ویژگی‌های کلیدی:
🔹
رابط کاربری ساده، روان و کاربرپسند
🔹
دارای یک لیست جامع و کامل از پکیج‌های سیستمی
🔹
قابلیت دی‌بلوت کردن دستگاه (حتی بدون نیاز به کامپیوتر)
🔹
دارای ویکی (Wiki) و مستندات کامل شامل آموزش راه‌اندازی، راهنمای استفاده و نحوه بیلد گرفتن از سورس‌کد
🛠
از نگاه فنی:
این برنامه با استفاده از زبان Rust و کتابخانه گرافیکی Iced ساخته شده تا تجربه‌ای بدون لگ و یکپارچه رو ارائه بده. از نظر حریم خصوصی هم خیالتون راحت باشه؛ هیچ دیتا یا اطلاعات کاربری جمع‌آوری یا ارسال نمی‌شه و تنها ارتباط خارجی برنامه، درخواست‌های (GET) به گیت‌هاب برای دریافت لیست پکیج‌ها و بررسی آپدیت‌هاست.
چه کاربر مبتدی باشید چه یک متخصص فنی، اگه می‌خواید گوشی‌تون رو بهینه‌سازی کنید، این ابزار یکی از بهترین گزینه‌هاست.
💡
حرف آخر:
با این ابزار، کنترل کامل عملکرد و امنیت گوشی اندرویدی‌تون رو دوباره به دست بگیرید!
──────────────────────────────
🔵
@ArchiveTell
| Bachelor
⚡️
#Github</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6444" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8WEhatx0JfrEpVZGi0OSvzVmyK8C5UFoRN6XMPiUrqDKd7htd4C_Jcd7uEB2OrgjmyGfkx0xX-_ZQW_lzcWZ12a8p95fi9Opzpm5VUavXbwNzJiLYqpWs4pETCXz0V2SQS429T-uqci-vspN2IdPP_SPsnSOZGoaVg4rmTBoWkWXLtAnLkZOgfKxkySL5OWQN7TQwvtGyLJkxrCf6ZqaXONJBAC-QjI92hY-4xfRObt_Hx0-qNxbgOzPbC95fyB5ABeR2SqN-53iPuxCjTKAJexHjBg4lBwAPRFORgqskj8bEQsX0R1vH_eip0q57I23rFy6peZ7aTbEhqoCdWWWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دانلود کامل ویدیوهای یوتیوب + ویرایش فوری بدون افت کیفیت
🎬
یک توسعه‌دهنده دانلودر شخصی خودش را متن‌باز منتشر کرده؛ ابزاری ساده برای دانلود و ادیت سریع ویدیوها.
✨
قابلیت‌ها:
•
🔹
دانلود ویدیو با کیفیت اصلی
•
✂️
برش، چسباندن و تقسیم ویدیو داخل برنامه
•
💻
اجرای کاملاً محلی روی سیستم
•
🆓
رایگان و متن‌باز
•
🧩
رابط کاربری ساده و کاربرپسند
GitHub
#OpenSource
#YouTube
#Downloader
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6441" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚀
آموزش اجرای GPT 5.5 xhigh در Codex روی ترمینال (کاملاً رایگان)
1️⃣
ثبت‌نام در Freemodel
وارد سایت
Freemodel
شوید
با حساب Gmail ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🔹
گزینه 1: احراز هویت با شماره تلفن
🔹
گزینه 2: احراز هویت با تلگرام
✅
گزینه
Telegram Verification
را انتخاب کنید
🔗
وارد ربات تلگرام شوید و Start را بزنید
🎉
در این مرحله پلن Pro برای شما فعال می‌شود:
هر ۵ ساعت: ۱۰ دلار اعتبار
💰
هر هفته: ۶۶ دلار اعتبار
💰
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Keys
یک API Key جدید بسازید و ذخیره کنید
3️⃣
نصب Termux (روی موبایل)
📱
اگر موبایل دارید، از Termux استفاده کنید
4️⃣
دستورات نصب در ترمینال
(
به
ترتیب وارد کنید )
1⃣
آپدیت Termux
pkg update && pkg upgrade -y
2⃣
نصب ابزارها
pkg install proot-distro git curl wget nano tar -y
3⃣
دسترسی به حافظه
termux-setup-storage
4⃣
نصب Ubuntu
proot-distro install ubuntu
5⃣
ورود به Ubuntu
proot-distro login ubuntu
6⃣
آپدیت Ubuntu
apt update && apt upgrade -y
7⃣
نصب ابزارهای ضروری
apt install -y sudo ca-certificates curl wget git nano gnupg lsb-release build-essential python3 make g++
8⃣
نصب Node.js
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
9⃣
نصب Codex
npm install -g @openai/codex
🔟
تنظیمات Codex
mkdir -p ~/.codex
cat > ~/.codex/config.toml <<'EOF' model = "gpt-5.5" model_provider = "freemodel" preferred_auth_method = "apikey" model_reasoning_effort = "high" disable_response_storage = true
[model_providers.freemodel] name = "freemodel" base_url = "https://api.freemodel.dev" wire_api = "responses" env_key = "OPENAI_API_KEY" EOF
🔘
تنظیم API Key
echo 'export OPENAI_API_KEY="کلیدتو اینجا بزار"' >> ~/.bashrc source ~/.bashrc
▶️
اجرای Codex
( با فیلترشکن خوب وارد شوید )
codex
✨
حالا Codex روی ترمینال شما آماده استفاده است
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6440" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFMKPfrAYxwdXVvc3fqMS1dXl-B8eWd6X_nQCDH9IkOQqNV5JS1lOVVD5zlb2j_LBvYXPIDZ1kycOq7XZehWLIe3A_8NMW2RYfVydT4QVs6asg5L57UFCrWjfouQkUboPzEaCOGrhYux9za1gyV2-zpErwJZjACGua262QQhiBRJ8oj404jZICpYu6JUNpN8V0weifW0F_a-Zu0kU_zEDktSU_P4pUXFN2hjfPl3kPOkup_bfWZ3I1xbxah--euqp_1OqOhOJTh30_6DuSfbXVCHLQk2fYpOogkZwBxrrcOfM212-6QMMFdnLdtroa7Avl-1i0DjtlftkQN-idgSrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6438">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">💻
ایده داری ولی حوصله نصب ابزار و دردسرهای راه‌اندازی رو نداری؟
🚀
Replit
یه محیط برنامه‌نویسی آنلاین با AI داخلیه که می‌تونی مستقیم از مرورگر پروژه‌هات رو بسازی.
✨
امکانات:
• کدنویسی با کمک AI
🤖
• ساخت سایت، ربات و اپلیکیشن
🌐
• اجرا و هاست پروژه‌ها در همان محیط
⚡
• بدون نیاز به سیستم قوی یا تنظیمات پیچیده
🔧
برای شروع سریع پروژه‌های شخصی، استارتاپی یا AI گزینه جالبیه
👀
🔗
سایت
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6438" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORquz0u-4ELdKxzrQSABwrIYuaF6Prb_i4GsuoxQw0OaXcQT8Do3jQXyMu3Bwau4eTPktV8Ays1hT_5qBNDp0kGkY5b36BsfTsgVHVSqXMVbjlKLo5_Uey7_X_FTsL8THla9tB1wt_McfJtfIon4A-se-g4UkW8HkcOP9flxZLH1NIR5yCTr3rTql0uw7vKKnxYXAOnRjS5SaW6nOpbQA0ac_z9KDt4jzG7OOTpJGNrG9FOU93ZRrrM6mc_GDSlW9gXg1JpuClETkpCWmGBJdfFS7l-hd_Tg36L5iCVjvCryaSu3INpXqRbjvWQ2_LZknWKILmG2PlIwyNsp9p7-bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دسترسی رایگان به Claude OPUS 4.8 و GPT 5.5 + دریافت ۷,۲۰۰ اعتبار!
💯
🤩
پلتفرم
Gumloop.com
یک رابط کاربری چت حرفه‌ای با قابلیت اتصال به سرویس‌های مختلفه. جالب اینجاست که این شرکت به‌تازگی ۵۰ میلیون دلار هم سرمایه جذب کرده!
مراحل دقیق دریافت اعتبار:
🔹
از طریق حساب گوگل یا مایکروسافت (OAuth) ثبت‌نام کنید.
🔹
در مراحل ثبت‌نام اولیه، به سوالات پاسخ بدید و هر گزینه‌ای که می‌تونید رو انتخاب کنید.
🔹
وقتی به بخش اتصال سرویس‌ها رسیدید، Apify، Semrush و Reducto رو انتخاب کنید (هیچ‌کدوم نیازی به لاگین ندارن).
🔹
اتصال به Slack رو اسکیپ (Skip) کنید و نادیده بگیرید.
🔹
اگه مراحل رو درست برید، حداقل
۷,۲۰۰ اعتبار
به حسابتون اضافه می‌شه!(که مال من نشد
😂
)
🤖
مدل‌های هوش مصنوعی موجود در پلتفرم:
Opus 4.6 تا 4.8، GPT 5.3 Codex، GPT 5.4، GPT 5.5، Gemini 3 Flash، Gemini 3.1 Pro، Gemini 3.5 Flash، DeepSeek V4 Flash & Pro و Kimi K2.6.
❌
در هیچ‌کدوم از این مراحل نیازی به وارد کردن کارت بانکی (Credit Card) نیست.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6437" target="_blank">📅 15:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚀
آموزش اجرای Opus 4.8 Ultra در Claude Code رو ترمینال ( کاملا رایگان )
1️⃣
ثبت‌نام در Freemodel
وارد سایت
Freemodel
شوید
با حساب Gmail ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🔹
گزینه 1: احراز هویت با شماره تلفن
🔹
گزینه 2: احراز هویت با تلگرام
✅
گزینه
Telegram Verification
را انتخاب کنید
🔗
وارد ربات تلگرام شوید و Start را بزنید
🎉
در این مرحله پلن Pro برای شما فعال می‌شود:
هر ۵ ساعت: ۱۰ دلار اعتبار
💰
هر هفته: ۶۶ دلار اعتبار
💰
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Keys
یک API Key جدید بسازید و ذخیره کنید
3️⃣
نصب Termux (روی موبایل)
📱
اگر موبایل دارید، از Termux استفاده کنید
4️⃣
دستورات نصب در ترمینال ( به ترتیب وارد کنید )
1⃣
آپدیت Termux
pkg update && pkg upgrade -y
2⃣
نصب ابزارها
pkg install proot-distro nano -y
3⃣
نصب Ubuntu
proot-distro install ubuntu
4⃣
ورود به Ubuntu
proot-distro login ubuntu
5⃣
آپدیت Ubuntu
apt update && apt upgrade -y
6⃣
نصب ابزارهای ضروری
apt install -y sudo ca-certificates curl wget git nano gnupg lsb-release build-essential python3 make g++
apt install -y curl nano nodejs npm
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
7⃣
نصب Claude Code فیلترشکن بزن
npm install -g @anthropic-ai/claude-code@2.1.167
8⃣
تنظیمات Claude Code
mkdir -p ~/.claude
دستور زیر را برای باز کردن فایل تنظیمات بزنید:
nano ~/.claude/settings.json
کد زیر را داخل فایل پیست کنید (کلید خود را جایگزین کنید) و با زدن Ctrl + X و سپس y و در نهایت Enter ذخیره کنید:
{
"env": {
"ANTHROPIC_API_KEY": "کلیدت",
"ANTHROPIC_BASE_URL": "https://cc.freemodel.dev",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلیدت'"
}
▶️
اجرای Claude Code ( با فیلترشکن خوب وارد شوید )
claude
✨
حالا Claude Code روی ترمینال شما آماده استفاده است
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6436" target="_blank">📅 11:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPHPoHE5TF0SEBRWAE5jM8ybVtpA9_HMsguOU-9Gm_Y9Z_fayVKl80jk99_QZZKYCOThYAkLFVR6uMQDW2Nt-7bABfstYTmCFGbyHO_0j-TmP713AyDjylN1m6Vikwldp-AuLNjprECLZeZ7UEF_76hJW8Jnm6o4qLSapb4a657X_EoM7DL5Dbj_fjnrOuAqGLwcz3yNJPSaJlAFs4W6hae9gPIPIrakoNWiMPWscI-eDYC2AJXlfreSLMCvXPjHqJdeCReh5jIOgfg4Kgdx6D6eM-M_xcPQXeT35XiRfz-CMRWkKyGwRAVyO1k6bYDYTV7GYdYhSijybOMks_hJCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ دلار اعتبار رایگان OPUS 4.8 و GPT 5.5
🔥
🌐
ثبت نام
#API
#Claude
#GPT
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6435" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=NBnB9EvLx2AROr45lV7nYKO6I0CczVJ_5RWxpK7d3v5wqmA0R5SgbJT9tmBbSuxqvm3CzOyz-Xq4oog9uDd72trYfpYH0m84NMUEj8YfDunLUwWWMTwhsU7wMif6Tse-SSAPIiEtISKre_NhxnFq4l5pz7CiY6Z8VufgBNUnQR-2msTL8hFSXU55aOG5SCZ2DvVUieHhnrYfP8vszpeWlLcLp-NnAuPHMQpK3XU14UQovmcvwW3HSCtATz5sGLl8vZG3bs8mT4nBsfPJwZiko7FVrCYUKcQ0YQ_9AZybsiq8YF1K_8MP3tJ7y7qTsRNx6913-MXCdNvDNZF5SewuVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=NBnB9EvLx2AROr45lV7nYKO6I0CczVJ_5RWxpK7d3v5wqmA0R5SgbJT9tmBbSuxqvm3CzOyz-Xq4oog9uDd72trYfpYH0m84NMUEj8YfDunLUwWWMTwhsU7wMif6Tse-SSAPIiEtISKre_NhxnFq4l5pz7CiY6Z8VufgBNUnQR-2msTL8hFSXU55aOG5SCZ2DvVUieHhnrYfP8vszpeWlLcLp-NnAuPHMQpK3XU14UQovmcvwW3HSCtATz5sGLl8vZG3bs8mT4nBsfPJwZiko7FVrCYUKcQ0YQ_9AZybsiq8YF1K_8MP3tJ7y7qTsRNx6913-MXCdNvDNZF5SewuVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
Open Design
یه نسخه اوپن‌سورس از Claude Designه که واقعاً به درد می‌خوره
😮‍💨
باهاش می‌تونی از روی یه پرامپت، سایت، دک، تصویر یا حتی موشن بسازی و بعد همون‌جا توی محیط امن ویرایشش کنی.
✨
چیزای مهمش:
• 150 تا design system آماده
• 260+ پلاگین
• پشتیبانی از Claude، Codex، Gemini، Copilot و بقیه
• خروجی HTML / PDF / PPTX / MP4
• همه‌چی لوکال و بدون قفل شدن به یه سرویس خاص
خلاصه اینکه: یه ابزار جدی برای طراحی با AI، نه فقط یه چت‌بات دیگه
👀
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6434" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">با سلام درود رفقا میخوام یه ربات open vpn بیارم
دنبال پنل درست حسابیشم
اگه کسی پنلی داشت که بشه حجم و کاربر و ایناشو مشخص کرد ممنون میشم داخل کامنت همین پیام یا پیوی بگه ممنونم ازتون
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6433" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✨
ویندوزتو سریع‌تر کن با Sparkle
🧹
یه ابزار رایگان و اوپن‌سورس برای بهینه‌سازی ویندوز
• پاک‌سازی و سبک کردن ویندوز (debloat)
• بهینه‌سازی سیستم با یه کلیک
• مدیریت DNS
• نصب برنامه‌ها با Winget / Chocolatey
• حذف فایل‌های اضافی و junk
• بکاپ و ریستور تنظیمات سیستم
🚀
همه‌چی تو یه داشبورد ساده و مدرن
🔗
GitHub
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🧠
AI OS
سیستم عامل هوش مصنوعی لینوکس
👇
یه سیستم‌عامل ساختن که بهش میگی چی کار کنه، خودش واقعاً انجام میده
🤖
🔒
HAL (امنیت):
• کار ساده → خودکار
• کار حساس → تایید می‌خواد
• سیستم → بدون اجازه دست نمی‌زنه
📁
دیتاها لوکال می‌مونه + حتی آفلاین هم کار می‌کنه
خلاصه
👇
دیگه چت‌بات نیست… یه OS هست که کار می‌کنه
🔥
🔗
Github
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⚡️
Gemini
داره می‌ره سمت ساخت ویدیو با چهره خودت!
یعنی یه عکس از خودت می‌دی و بعدش می‌تونه ویدیوهایی بسازه که انگار خودت داخلش هستی.
فعلاً این قابلیت دست یه سری تسترهاست، ولی اگه عمومی بشه، تولید ویدیو با AI یه سطح جدید می‌ره
🚀
#AI
#Gemini
#Tech
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6429">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYzu40nBm3fynyrBXA-yeWVEH1CdU2p2NnY4I7g4m_QnrWPQEczUrKzzfwbTe9ULhnGR5b3nWAAHlT71QyqzoqpQT1XrqU1gBpADVyPyNABGDSCk4IRZOGMI3SkYFI-wrpYSSg5iuQFcS3kBxkxIgcxOTF_aJcxIpqKh9KG0zMO3I-dAXXVxB3f9ljtuxO5QYD0RLzn1sefutZ6DOmJu8Nr3H3egXq0gPfHzT1vxuLsGlkXDKUO8LugqBF99MUEIXVEg-Cc_0E04GDnUcXioA2cC8h0CeLmcrzt_-OHabMIPuA_rWbUYgdPuOIaguuuuNYvaxnG934qoCQ7HcD83eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍎
اجرای macOS روی کامپیوتر معمولی بدون راهنماهای پیچیده و تنظیمات دستی — علاقه‌مندان اسکریپتی ساخته‌اند که نصب سیستم را خودکار می‌کند.
🔹
نسخه‌های macOS از High Sierra تا Sequoia را پشتیبانی می‌کند.
🔹
روی پردازنده‌های Intel و AMD کار می‌کند.
🔹
به‌صورت خودکار ماشین مجازی را ایجاد و تنظیم می‌کند.
🔹
کمک می‌کند محیطی برای Xcode، Logic Pro، Final Cut Pro و نرم‌افزارهای دیگر اپل به سرعت راه‌اندازی شود.
🔹
به‌طور منظم به‌روزرسانی و پشتیبانی می‌شود.
▶️
دستور نصب:
/bin/bash -c "$(curl -fsSL https://install.osx-proxmox.com)"
GitHub
#OpenSource
#macOS
#Proxmox
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🌐
DigitalPlat FreeDomain
راهی برای گرفتن دامنه رایگان
این
پروژه به شما اجازه می‌دهد بدون هزینه، برای سایت یا پروژه‌تان دامنه بگیرید و سریع راه‌اندازی کنید.
✨
🔹
دامنه‌های رایگان فعلی:
• .DPDNS.ORG
• .US.KG
• .QZZ.IO
• .XX.KG
• .QD.JE
📊
طبق اعلام پروژه، تا الان بیش از ۵۰۰ هزار دامنه ثبت شده و مدیریت همه‌چیز از طریق داشبورد آنلاین انجام می‌شود.
🔗
ثبت دامنه و راهنما
#Domain
#FreeDomain
#Web
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">ایپی 188.114.97.6، تنها ip واقعا تمیز کلودفلرِ ایرانسل دوباره باز شده، بقیه ip ها رو alpn-1.1 (وبسوکت) محدودیت شدید آپلود دارند، در نتیجه پنل های bpb و ... رو اونها قابل استفاده نیست و فقط XHTTP رو سایر ip ها قابل استفاده است.
///
ولی علاوه بر
188.114.97.6
که مستقیم بدون نیاز به چیزی وصل میشه، رو بعضی ip ها مثل
104.17.121.43
نیز فرگمنت باعث میشه که محدودیت آپلود برداشته بشه و اون ip قابل استفاده باشه، تنظیمات زیادی برای فرگمنت کار میکنه به طور مثال در حال حاضر میتونید از:
"ip": "104.17.121.43",
///
"packets": "tlshello",
"length": "1",
"interval": "0"
استفاده کنید.
///
تمام مطالب بالا راجع به ایرانسل (و بعضی نت های دیگر در برخی مناطق) میباشد، و رو بیشتر نت های دیگر محدودیتی وجود ندارد و اکثر ip های کلودفلر به طور مستقیم قابل استفاده اند.</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2FDktv1v9TwK0LSABg_U34AX7Az2PXvYVLLCxbv9ypUFfOA2D0fhsZkQOwvgKYDrw-dd18AvI0EkiK_lEN9thI-Vt88TewetCzhKKoD2XDqEZH0nuy8I5O-0YZGZZs4tgV92Gn9HHl4DZ7PiiG5KgTZN535TUJGFQAq0CgQ34aIT0iv6JfFLHbKn7iszw9g7ZGp6yJx2ZmSOMdQlJOPTRJfBaifbDHiyiBVyFMSOMJDWWEMJQt_peOUdMQ4nCwysc3XUzzwib7ruMn6Qj-FF3Z3D_WjkSj9x8iCej6s4qLX0IrS-GxKPuViwotY3OkZJgsrmlcz2YI3EvEvXC0ysA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡️
برنامه Sandboxie؛ اجرای امن برنامه‌ها در محیط ایزوله ویندوز
اگر می‌خواهید نرم‌افزارهای ناشناس، فایل‌های مشکوک یا مرورگر خود را بدون دسترسی مستقیم به سیستم اصلی اجرا کنید، Sandboxie یکی از قدیمی‌ترین و قدرتمندترین ابزارهای Sandbox برای ویندوز است.
✨
امکانات مهم:
🔹
اجرای برنامه‌ها در محیط کاملاً ایزوله
🔹
جلوگیری از تغییر دائمی فایل‌ها و رجیستری ویندوز
🔹
ساخت تعداد نامحدود Sandbox
🔹
فایروال اختصاصی برای هر Sandbox
🔹
محدودسازی دسترسی به اینترنت، کلیپ‌بورد و فایل‌های سیستم
🔹
محافظت در برابر اسکرین‌شات و نشت اطلاعات
🔹
پشتیبانی از مرور امن وب و تست فایل‌های ناشناس
🔹
متن‌باز و رایگان
برنامه Sandboxie از سال ۲۰۰۴ توسعه داده می‌شود و امروزه به‌عنوان یکی از محبوب‌ترین ابزارهای امنیتی ویندوز برای تحلیل فایل‌ها، تست نرم‌افزارها و افزایش حریم خصوصی شناخته می‌شود.
🔗
Github
#Windows
#CyberSecurity
#Sandboxie
#Privacy
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3zLiZrgYsfa7rxzVw3U3xpQaBRaBoJjvD5gYu-0DVrFql_H9sVuFfhwa1tP57a_zTJPJfs-ktQ89NuZJ4esDQDpmqeB39ESo3y-mupbYNmBUzxXrZ6G2DhYz3uKkKYjOIGOPeyFySRl4vrIlOsiryngewgg0pNOIviBs12-mc6ozmaDcJsHBf-tYWw1nXnXv5MEpz-JcV449T-J9skaaOSmGuroPTqUXCsDWdO0CkXlI__Joo6MjLhmDXswnLG9FscHxlSo-cfP3Gzy-_izkS3rTvQLTMtDQqD0rB32YxMQSDK0NXLMv6X3YH6ASiwFrSQT93cKwhnKIqUl2n9IeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏬
دانلود ویدیو، موسیقی و پلی‌لیست‌ها بدون تبلیغات، اشتراک‌ها و مبدل‌های آنلاین مشکوک
یک رابط کاربری مناسب برای ابزار افسانه‌ای yt-dlp پیدا کردیم
🔥
قابلیت‌ها:
🔹
دانلود ویدیو از بیش از ۱۰۰۰ پلتفرم محبوب.
🔹
پشتیبانی از کیفیت تا 8K و صدای بدون افت کیفیت.
🔹
قابلیت دانلود کل پلی‌لیست‌ها، کانال‌ها و زیرنویس‌ها.
🔹
امکان قرار دادن ده‌ها فایل در صف دانلود.
🔹
به‌صورت خودکار مرتب‌سازی و تغییر نام دانلودها بر اساس قالب‌ها.
🔹
اجرای محلی روی کامپیوتر شما.
🔹
پشتیبانی از ویندوز، لینوکس و مک‌اواس.
GitHub
#OpenSource
#Tools
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfdQuXavRKzcaQDNlzII4tdqBI_s5xe_p-sSbJe5Uopg9o8vG9AXPXXXvtQITNdxEvLK78ayCJR4yuOjM6uDGtnQcxWwVVNHBvnmO0PztTPGyUtvJdnFgaJH0CGoi9t4T4gR6AFw8JhvVE6mg1zaRlQ_Jh13sV2x8AW_6arpg9ZDZifkD6Gx8kVlM03naeNwEzaO0n3LdA4_jLyjIIBrjYQbolxBz2RSSdHvCyxyxA3sKhdMd4ZM9cytU0uWoIrzq-HWpFxeEsqFpFNhVP5upFJCByRGQ9U5w4DfnZgGX4hbQePHApJ6Mp4UBz29afFrgm-tXnlzvdyQsj1LwF5cXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت api رایگان- GPT5.5
لینک 10 دلاری
ثبت نام بدون لینک، اعتبار نمیده و با صفر شروع میشه
وریفای کردن هم با تلگرام انجام بدین که تایید بشه براتون
با شماره مجازی نمیشه(چین)
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvRNke3cBuzlpJTYvmWhZWGyuN85Mwr5uKiig3UKikyIOTbRehLvEnVnu8rZa5RTYo1pC2eD0W7C6zC1Ax2gdgWZl2trI9ioowlQMZSV8iQq8CwJJmV336pLdDuw6V0yX4wlrwoJJsUN0pYGjlU0jorRrU8fuRHRjgp-yz9oR4DFNnZ22Q7hAamSQRkKWIKZyAzAJs-c0RmnCuy9zw5aTbYiZAALmRdwjeS11THD4x3eQEO9vbsejZ4BrMl0jGUAD--cYOt0ZkIp42AWxShfAjWRavgVHzAqTQ51RwNTlz-kss5FQl2Jz8K_hfCEOo4LpiAnEJO7SchGHneCZY7Ong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مدل Cursor در حال توسعه یک مدل جدید با 1.5 تریلیون پارامتر است!
⚡️
نکات مهم:
🔹
از صفر آموزش داده شده و نسخه ارتقایافته مدل‌های قبلی نیست.
🔹
گفته می‌شود برای آموزش آن از حدود 100 هزار کارت گرافیک H100 استفاده شده.
🔹
علاوه بر کدنویسی، از Agentهای هوش مصنوعی برای مستندسازی و مدیریت تسک‌ها پشتیبانی می‌کند.
📅
طبق گزارش‌ها، این مدل طی چند هفته آینده معرفی خواهد شد.
#Cursor
#AI
#Coding
#LLM
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m59ZN9t7K4kZtqcHMd_A0e98xVoYhzAqh_HSbXKtIk_mxCiD-EwXL8XKRmfkUCokmj4862kqHMI79mtq3QjeMMkDzprKjWQmdVsBZDBGnzP5H4sZY1XcRm28enNo53S1ICaGjCJZlzg0l64E5RHGFCKRDgY8O05gEb_EckY5x2dtSdal7AlF8HitMLhGcmIIQ1faJC6W8cHQpv0I6hNcB0mTteY5DiIyAjSLzDfq8kNNNLETbDnvgdz1IrA8wWtyArZIPTo1Uivc0cjgtUMw3kzy8GuX0gZ5wEwtMItdq86qeUX2jLhjHd1LckkSDEnUbVolABFJa-1LCqjkKQqAnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CPhuJXZkfsN9_Mio297A0mF_RRLj0m86jhv7PxUblG9Nvt9XEPHkd3885rWv6CvHrgt9pNGtFIUAMhN4287I2Dn_37esoqIdxiFIhLRQsD9cwXUJZi8ta9nG2nBpCGTYnFiG9qDGMEjenFnmjEsLNpphwmAwc8mRBafOi-PPuqBUydNK6qmttq7bnEzYKu3i_GsUwS5Dk0PR8ERu4hJPc9_GLbJJCTOF7edpbHQTjLAj-7a_7ForFeLorJyxgtF1siFBfW7W4wMmhQ66BnHMbz4mNbk_yDekKzuZke9i2oovNdSSnYHVe6I2SwyRkMYFU-APdiIqr4owUnPK2Z-U8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXGawqw-sGxrR4Xmk5MM-D5fm2Zoqo21BP9pD6okqLg1OIzJ8vyXoYyQh6hOZWXiQZjpfRRyJm82UZPxPdGBv4Q9xa2f28GvUGo35tLZ3j5MMUu6HWL4NgRk6rSIiUS8AfpICqXhh1ogMdyV2LKlTbLrxOsVc_95Q2VIh9aBJ__mUPdy0XK4DBvbeRHjkVoJMlXWD9G9Tf2DwifEu1B8HiKSQeoNUVjw-ayxPmsUeEeJw96hBnfkdDA5nto70AGDk-5ByEhH099vGOT3FcLGpWPNsP3TkOtP__DEs1zKrz2M9iXHlDSPPArB2wn3Gdyy_dStZwqnxdYHnOzqfc6KKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل جدید GLM 5.2 از چین معرفی شد  توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OlCkgok0Z0bSm37HWrxyEUNISd23obDzJmv_4CLFAUJVCSe7YRMswzIzf7hGR4ZkpLF56NePyTOKjXfzPefs7pH-2EahW-1OKMiXj8WSXHq-SSPDQdx7M1qtBTap2czWyx2fzCbjgiZGZowKhBZtv_0V81AiupMeJ2aeV-AEaNzUw7PVgyp9v_qoM_cwyj0WORNlf30UZ_p48hSfm_V0pWMDj_GdWM5KGWWwR9yRl6-d2Ug2oXLloNijCLUuuK0Jb8UyqdN0KNDFzQsmq6rlCGBML0Je5ckTjq6l5Ye3FEm6KFx7ObWGjkbgmyEdEiFA4FLKIGEdmaGt-EmsadgAJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eZ8yWfHIMwHLBzKtRarbyYBfNuPhecsMArPdGE_yGArB6jApe-U0C8HzJ4KT3E86WRbQ5xYr55raTTnl29tHG9I_jZNv_xveInyA6CkoZ8K35Rkx_XKi94Rs5M0TSwB5Ebj1WIuqwwqunBFbtTytg9LZberJyUTnu6xJxiEI7VOL4ZXQ5JPaVFG-weYEPUFZQbUe5yPiyVdAfMcgQXl8W0PGInl4DfzngxCXzxSHXWEbi27BfNDgQbZ7tQI3rNovrIK7MJoqcgTFnniLG76R2ldU688YEs5Fsq83rUydoLhKj9i_cbBWyERr4ELy5HpzW9uhhivWFHrIIqyrKWGcQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رقیب رایگان Suno پیدا شد
🔥
StableDAW
یک استودیوی هوش مصنوعی برای ساخت موسیقی روی کامپیوتر شماست
✨
قابلیت‌ها:
•
🔹
تولید موسیقی بدون نیاز به اشتراک
•
⚡
ساخت ترک با پرامپت متنی یا ملودی خوانده‌شده
•
🛠️
ویرایش دستی ترک‌ها با رابطی شبیه FL Studio
•
🎹
پشتیبانی از MIDI، سازها و استخراج نت‌ها
•
💻
اجرای محلی روی کامپیوتر با سرعت بالا
🔗
لینک
#AI
#Music
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">sadra.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">همین الان ساختم
نامحدوده
تست بکنید به احتمال زیاد وصل باشه برای بعضی مناطق
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🌐
ابزار متن‌باز
CF-IP-Scanner
برای پیدا کردن سریع‌ترین IPهای Cloudflare منتشر شد.
این پروژه با اسکن رنج‌های Cloudflare، بهترین IPها را بر اساس پینگ و پایداری اتصال پیدا می‌کند تا در ابزارهایی مثل
Xray، V2Ray، VLESS و Trojan
استفاده شوند.
⚡️
قابلیت‌ها:
🔹
اسکن خودکار IPهای Cloudflare
🔹
نمایش پینگ و نرخ موفقیت اتصال
🔹
مرتب‌سازی نتایج بر اساس سرعت
🔹
خروجی گرفتن از لیست IPها
🔹
اجرای کامل روی ویندوز بدون نیاز به نصب وابستگی اضافی
📈
اگر با افت سرعت یا ناپایداری اتصال مواجه هستید، این ابزار می‌تواند برای پیدا کردن IPهای بهتر مفید باشد.
🔗
Github
#Cloudflare
#Xray
#V2Ray
#OpenSource
#Network
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⚠️
همراه اول بسته نامحدود شبانه که لیمیت سرعت از ۶۰ گیگ به بعد داشت رو حذف کرده
✔️
بسته های حجمی شبانه آورده
🌐
100GB
💳
49,000T
🌐
200GB
💳
69,000T
🌐
300GB:
💳
99,000T
👍
خوبیش اینه لیمیت سرعت نداره
💵
کد دستوری خرید :
💎
*1000*252#
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🤖
ابزاری جالب برای اتصال دستیارهای هوش مصنوعی به شبکه‌های اجتماعی و سایت‌های محتوایی!
با این پروژه می‌توانید به مدل‌هایی مثل
Claude Code، Codex و OpenClaw
اجازه دهید در سایت‌هایی مانند YouTube، Bilibili، Xiaohongshu و LinkedIn جستجو و اطلاعات جمع‌آوری کنند.
✨
کاربردها:
🔹
بررسی نظرات کاربران درباره محصولات
🔹
جستجوی فرصت‌های شغلی در LinkedIn
🔹
جمع‌آوری و تحلیل محتوای شبکه‌های اجتماعی
🔹
تحقیق و بررسی بازار با کمک AI
⚡️
گزینه‌ای کاربردی برای توسعه‌دهندگان، پژوهشگران و کاربران حرفه‌ای هوش مصنوعی.
🔗
Github
#AI
#ClaudeCode
#Codex
#LinkedIn
#YouTube
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RSAKCn816WDKYdS2OxiZvQoet28XP2z9FL56juUZf4N9z303w88Z55xFUsiPAM2O6ER8E7YzjIhLD57SSEDWduGp2RiZxmfx1uHrwMbMPfq0lO2dyZDQbFAsn1YKj21ISK9G7m3-2w4dWlNPO7A1hH_gcSgL-gPg9-qoauLUuxh7z-Gz5NnXkaOu6cxdMyPrDQNjBXj6PR4-3K6Q_DI-0cibsuviP_xVFKosww_nHB049fiSKHNg3Abu3wtHehWrsdpSHDk9GbNH16XTFgCOOIeEZCOjv6OLZfpnBaldX23IYkTjWFmx-367DebD7bL6q4hboOvVOHdLiFTVTI-8vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fic5iuDX-vl3P088Q66zOGliPhvav8WkzizfL1r7ivsEJB0FsRaY5rQqaJzLNEbuYwUw6a_SVJXRaPaRT8ufZP6msBJyPlAv0WZjxRajeTIEpmaWyf37dfhVTQuYsIjXXQ27qqxwy0aJ1rlFKt6VYSZGWhJDCbWOljQbJUB5ZO_8eUlVgjlCXH7uOwxdRgHP4WvFu-5pt52V_-L7ED3PqQ3woop73iAqukbv1AO-fRc26QTVR9CV4L51J7xdJGKBxILpADAlXQuxAHTKcPNTEkZ6ObDUB7O4v5pWtw8ikrZDqBMJJVZ-5dh4q6Oop7I401TREg3ZuwkW5hCU5mxkJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nv8CETJW3g6DI88i1dup3jCE8gYImTepLomMxt6td3gcKI6T2KH6mUewrhlGWmj0IqeF18OM2l4rOcWbpUNHvgJr6Lcr_9k7W75sCq73s2WajhhFRbVMH3ECr98onlLVfcWDZuMTZqqfDHLHXpENYwfUST6FMbJGESh68TWcxm5OPCXflXXTnw1HlcfjEicykY9ZnJPSyGVj9eAyDO2Cy81X7MElG_XloTr4hdSjz1aXeHnYJZKiqSynbwaKjKwatxjgOMJ_4B9C-JRetH5QIBSxr1fBJUxvNl-M8ebIEjnhDxwtRzIzZKhgZd7IT28NvemDK_0cqyAYAj8c2Fjj1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cm96w7xOXC6kaYxkMrUBJVaBNIgh-PJ8xa7RjNB4xgSTlTRnI-IE_SUnGm9YXMJmB640IzshYnCFP0_AT6v6BsuygOxAqIFicvG8xTXrHCuocPiMUztIyckzbVh3_B7jjNbRzGY1voOo85K-cKt4tcaY8_xBK3dPucBrW2i35J91OaV714Rl5shsG1Yrplt42IuY4IE-WOdbjHnY2VGVnaxksywCZSEaYlB-xHVI8DV__wsupSpEy4ajjWocstx5q5Yt6JCD1tLRvo1rXICndWOY5n2s5R2J_IAbg-WIuYSHRFEEr0-Sx8MS1Ymn1xiadhrMENx6Yjr55OlfXteMYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=uxkAA6MnGZgI5fQnezzD5lSl_w_9uKhTWcC5ZZY28vxUgZlhaSNTZNYUFaTv6Ecw8eWKLbx9lLu-ad7fFe6zpO_nisg8VeNzc9fabhSxYijSvntlY3dzWVRCD28ud-ddQkH6vlufVTcxAv9YbE-2-JM8Pp0IwxU5rwa-Con7UCcx_vqkykH6cY8o_yMAcJTvZXMa7xv-2RSUKlR9zuyw7jbQHbG0A0SH4a0n6aUo7gD7pwsQAJwy5PSKf81oAXpdTDld-jnlhzd1pBIDhLDEg_EIYBWl7HgBFHgz1CB-qZnssBqzA1b70NvJrxK8KxkYfH7077JZ2RXqvGYJ4_bPNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=uxkAA6MnGZgI5fQnezzD5lSl_w_9uKhTWcC5ZZY28vxUgZlhaSNTZNYUFaTv6Ecw8eWKLbx9lLu-ad7fFe6zpO_nisg8VeNzc9fabhSxYijSvntlY3dzWVRCD28ud-ddQkH6vlufVTcxAv9YbE-2-JM8Pp0IwxU5rwa-Con7UCcx_vqkykH6cY8o_yMAcJTvZXMa7xv-2RSUKlR9zuyw7jbQHbG0A0SH4a0n6aUo7gD7pwsQAJwy5PSKf81oAXpdTDld-jnlhzd1pBIDhLDEg_EIYBWl7HgBFHgz1CB-qZnssBqzA1b70NvJrxK8KxkYfH7077JZ2RXqvGYJ4_bPNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
Fable 5
اکنون به صورت رایگان روی کامپیوتر شما در دسترس است.
توسعه‌دهندگان نسخه ویژه Gemma 4 Composer 2.5 را منتشر کردند که با داده‌های استدلال دقیق آموزش دیده است.
🔹
تمرکز اصلی بر کدنویسی، تحلیل و درخواست‌های پیچیده است.
🔹
کاملاً به صورت محلی و بدون نیاز به اشتراک یا API کار می‌کند.
🔹
در قالب GGUF برای Ollama، LM Studio، llama.cpp و سایر ابزارهای محبوب در دسترس است.
دانلود این شاهکار
#Fable
#Ai
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🛢
نفت خام:
81.5$
|
دلار: 159,050 تومان
🕰
بروزرسانی - 26 خرداد 1405 - 03:04
🪙
قیمت لحظه ای رمز ارزهای پرمخاطب:
🟢
BTC:
$66,152.52
(+1.00%)
🟢
ETH:
$1,786.95
(+3.76%)
🟢
BNB:
$615.87
(+0.07%)
🟢
XRP:
$1.24
(+4.98%)
🟢
SOL:
$73.79
(+4.37%)
🔴
TRX:
$0.32
(-0.41%)
🔴
DOGE:
$0.09
(-0.86%)
🔴
ADA:
$0.18
(-0.05%)
🟢
PAXG (Gold):
$4,304.90
(+0.65%)
🚮
قیمت ارزهای تلگرامی:
🔴
TON:
$1.71
(-2.06%)
🔴
NOT:
$0.000448
(-7.03%)
🔴
DOGS:
$0.000044
(-1.64%)
🔴
HMSTR:
$0.000158
(-6.08%)
🟢
EVAA:
$1.258452
(+88.39%)
🟢
X:
$0.000012
(+3.86%)
🟢
MAJOR:
$0.035791
(+2.66%)
🔴
PX:
$0.017240
(-0.23%)
🔴
STON:
$0.578778
(-0.88%)
🟢
REDO:
$0.077989
(+10.89%)
🔴
UTYA:
$0.019192
(-7.00%)
🔴
DUST:
$0.000175
(-2.63%)
🟢
TONNEL:
$0.627903
(+4.80%)
🟢
FISH:
$0.005469
(+1.74%)
🟡
قیمت طلا و نقره:
🌍
انس طلا (دلار):
4,335.20$
🌍
انس نقره (دلار):
70.01$
💰
طلا ۱۸ عیار (هر گرم):
16,296,900
تومان
💰
طلا ۲۴ عیار (هر گرم):
21,729,000
تومان
🥇
سکه گرمی:
25,500,000
تومان
🥇
ربع سکه:
47,620,000
تومان
🥇
نیم سکه:
85,960,000
تومان
🥇
سکه بهار آزادی:
163,625,000
تومان
🥇
سکه امامی:
167,010,000
تومان
🥈
گرم نقره ۹۹۹:
377,140
تومان
🛢
قیمت نفت:
🇺🇸
نفت WTI (تگزاس):
81.5$
(+1%)
🇬🇧
نفت Brent (برنت):
83.7$
(+0%)
#دلار
#طلا
#نفت
🫀
نبض بازار در دستان شماست...
‌</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAssa</strong></div>
<div class="tg-text">بچه ها شرمنده یه خبر باید بدم بهتون
من تحقیقاتم از سایت render بر اساس هوش مصنوعی بود الان شخصا سایت و قوانین رو چک کردم
مثل اینکه bandwidth رو ۵ گیگ میده اما پروژه اولی خودم تا ۲۵ گیگ مصرف بعد ساسپند کرد البته این هم بگم من کانفیگ پخش کرده بودم و تقریبا سه روزه داره دست به دست می‌چرخه با کاربر بالا
الان هم کد بهینه تر شده کمتر گیره
خلاصه که شرمنده بازم درباره اطلاعات من احمق برای اطمینان هم از جمنای هم از Claude هم پرسیدم
😑
💔
البته اگر قبلاً ورسل زده باشین میدونین که اون سقف زیاد مهم نیست و اگر شخصی مصرف کنید و ترافیک عجیب رد ندین کم کم برای شما تا ۴۰ گیگ میره بعد ساسپند می‌کنه
ورسل به اون بزرگی با هابیش ۳۰۰ گیگ رد دادم حالا این رندر که چیزی نیس
😂
بگم که ریلوی سقفش همون ۷۰ گیگه
و اینکه اگر ساسپند شدین فوقش با ایمیل فیک ثبت نام کنید و یکی دیگه بسازید بیشتر از ۵ دقیقه کار نداره
بازم عذر میخوام باید شخصا تحقیق میکردم</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtuVQ4-V9Xu_Q6HEXvxXTQcAfWREx4gdoOz2JLIEQ2qIIg03Vfza5hXW8JrXVk7VbG4nFG3fXN09JX8avx68seqKIAIFXjniKcbfuidHKzxJSWguscb5-B1gVQvCsUQbZcgUn5Xpn266VxLsrfEh7kzsrfmh7L25clV57njY-V00bp4vUtFzYM_81RZ8YkK6gtT8OpjFjyEXDeFccyetuDANQiHYLIhzAEquCLl3v0XzAMqLakiB4zY5prpY1Cux7hzzlJAsccAbs_oHZYQZhgrpskIeyRXctLaedXAqn2RTDhRXeVqoRCGYEbc7ym3yFHaz-lgcMQcx-ioGx9TunA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=DdZG1I7zTVuTaWbtVaOtKfmX_79ERkQ57XoE0HJS0x-iLSOcjZigqUCvZsRmv8AD8wbI5gRKYGgRW7Y37YWbf4UFgKLW2np2sI9yd-EwEQSKq0rbUw0az-Ui1NADQQskkfhg8t7KKPBBaCNFDB8Mr2sCJXxQh9iwCajJ7RGXgrnNFyh2Dq4nWz1reLGNlwCXWQnAgNkrvawPc7wISZOYZQbBd8h75OwQOa1HEqYuIpDZR_O6NllUCO-HFmkg597_AnY5P-RGj_5EIhJh4h4vuACW24ye2eTJaX7Nx41imsCXtG7RvcRbVRHq6gHiHGoJs7xUgzf0tB4WR7kPc-rCmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=DdZG1I7zTVuTaWbtVaOtKfmX_79ERkQ57XoE0HJS0x-iLSOcjZigqUCvZsRmv8AD8wbI5gRKYGgRW7Y37YWbf4UFgKLW2np2sI9yd-EwEQSKq0rbUw0az-Ui1NADQQskkfhg8t7KKPBBaCNFDB8Mr2sCJXxQh9iwCajJ7RGXgrnNFyh2Dq4nWz1reLGNlwCXWQnAgNkrvawPc7wISZOYZQbBd8h75OwQOa1HEqYuIpDZR_O6NllUCO-HFmkg597_AnY5P-RGj_5EIhJh4h4vuACW24ye2eTJaX7Nx41imsCXtG7RvcRbVRHq6gHiHGoJs7xUgzf0tB4WR7kPc-rCmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
یک پروژه متن‌باز جذاب برای ساخت ارائه با کمک هوش مصنوعی!
دیگه لازم نیست ساعت‌ها برای ساخت اسلاید وقت بذارید؛ این ابزار رو می‌تونید روی سیستم خودتون اجرا کنید و با هر مدل هوش مصنوعی دلخواه، پرزنت حرفه‌ای بسازید.
✨
ویژگی‌ها:
🔹
پشتیبانی از OpenAI، Gemini، Claude، Ollama و مدل‌های دیگه
🔹
ساخت ارائه از روی متن، فایل و اسناد
🔹
قالب‌ها و تم‌های قابل شخصی‌سازی
🔹
اجرای کامل روی سیستم شخصی
🔹
رایگان و متن‌باز
🎓
مناسب دانشجوها، مدرس‌ها، پژوهشگرها و هر کسی که زیاد ارائه می‌سازه.
🔗
Github
#OpenSource
#AI
#Presentation
#Productivity
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🌍
افزونه Local Translator
؛
افزونه‌ای متن‌باز برای ترجمه صفحات وب بدون ارسال داده‌ها به سرورهای خارجی.
💡
اگر دنبال جایگزینی سبک و خصوصی برای مترجم‌های آنلاین هستید، ارزش امتحان کردن را دارد.
🔹
ترجمه کامل صفحات یا بخش‌های انتخابی متن
🔹
استفاده از Translation API داخلی Chrome
🔹
حفظ حریم خصوصی؛ پردازش روی دستگاه کاربر
🔹
دو حالت نمایش: جایگزینی متن یا نمایش ترجمه زیر متن اصلی
🔹
ذخیره خودکار تنظیمات و فعال‌سازی خودکار
📎
GitHub
#Chrome
#Translation
#Privacy
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRyBLQkE_eWknaSsRzIEGxYTgHbSI56yQAFPuWgdIMLcT0y-egl1NyEhyewF7ZLVuYHBlFT0vPdqZScJGfcE6m-CmO8Uv0-BC5kWpcjwf075FplGiZW2vJOC_Ugf2eIAMYdptUnBGJ6iqH4l3wLM8KVqhZr-u9dwLdWkez0tOwzXwopcjVpANc2YMG43lKfxETINQmqUdZT6Jjdp1wRXegtaDLQQ37GxMniT7BVLy_G8Ymo3q3zBN9i7hkp_fq_31KvhSnawZhJQmlPZxYPIRFcXwgQm2rvueZzvU0TD1uFnQFKfNi6sMxmL9QwUIeQLcFrD4aPNKCz5OicqW0ks-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با افزونه SkipBait میتونید ویدیوهای یوتیوب رو سریع خلاصه کنید و دقیق‌تر داخل محتوا بگردید
🎬
✨
قابلیت‌ها:
•
🔹
خلاصه‌سازی سریع ویدیوهای YouTube
•
⚡
جستجو داخل زیرنویس‌ها و متن ویدیو
•
🤖
پرسش‌وپاسخ با هوش مصنوعی درباره محتوای ویدیو
•
🌐
پشتیبانی از جستجوی وب برای اطلاعات تکمیلی
🔗
لینک
#AI
#ChromeExtension
#YouTube
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
گزارش‌های تازه از پیش‌نویس توافق آمریکا و ایران
🇺🇸
طبق گزارش Reuters، پیش‌نویس یک تفاهم‌نامه موقت میان آمریکا و ایران روی چند محور اصلی می‌چرخد: توقف درگیری‌ها، بازگشایی تنگه هرمز، کاهش فشارهای نفتی و آزادسازی بخشی از دارایی‌های مسدودشده ایران. همچنین قرار است درباره پرونده هسته‌ای یک بازه ۶۰ روزه برای مذاکره باز شود.
📌
با این حال، Reuters تأکید کرده که این توافق هنوز نهایی نشده و بعضی جزئیات، از جمله رقم دارایی‌های آزادشده و شکل دقیق رفع تحریم‌ها، در گزارش‌های مختلف متفاوت آمده است.
⚠️
فعلاً باید این خبر را در حد پیش‌نویس و گزارش رسانه‌ای دید، نه توافق قطعی.
#Iran
#US
#MiddleEast
#Reuters
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
احتمال بازگشت Claude Fable 5؟
بر اساس گزارش برخی رسانه‌ها، کمپانی Anthropic تیمی از کارشناسان خود را برای مذاکره با مقامات آمریکایی به واشنگتن فرستاده تا محدودیت‌های اعمال‌شده روی مدل Claude Fable 5 را کاهش دهد.
📌
گفته می‌شود این محدودیت‌ها پس از نگرانی‌های امنیتی و گزارش‌هایی درباره روش‌های Jailbreak و دور زدن مکانیزم‌های حفاظتی مدل اعمال شده‌اند. برخی منابع نیز مدعی‌اند که امکان عبور از بخشی از محدودیت‌های امنیتی Claude Fable 5، یکی از دلایل اصلی این تصمیم بوده است.
🔹
هنوز هیچ جدول زمانی رسمی برای رفع محدودیت‌ها منتشر نشده است.
🔹
در صورت توافق، احتمال دارد مدل با لایه‌های امنیتی و محدودیت‌های بیشتری دوباره در دسترس قرار بگیرد.
🔹
کمپانی Anthropic تاکنون جزئیات کاملی درباره آینده این مدل منتشر نکرده است.
⚠️
فعلاً تمام این موارد در حد گزارش‌های رسانه‌ای است و باید منتظر اطلاعیه‌های رسمی از سوی Anthropic و نهادهای آمریکایی ماند.
#Anthropic
#Claude
#AI
#LLM
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YfMMApl2F18Sx6inyu1EqBqtzuNpqJybGNVw1sbNn2NOHUrxFQxjM7GgZ1zEuMcNVfev607szRZwGEFNqIo_N90I6kYHCEfzBhqJZF7-TK-4sD8SWxmzilR_W30LoEpfLgzJVysB1WyOAyyWPz0MJ_AakZoW6VRR_KyZaavsGzAY2cio28-RcZSMa99sgkj1wfPQqMxLAkZA9nyhHWAvkX0OlY5ObVYpgall-rIVIs7II6fTq0CyrqXUPDegc5DjDCHuAgk0DbyIVsSNb-1NSCzSNXbhBwsRWeCb2wJVP-Vf5LHkO0i7nwLBkbrExPuiJiElXw6FwYPjApbXnnR8zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: آلمان
🧭
شرط: حداقل 1 دعوت
👥
دریافت‌کنندگان: 21/30
💾
حجم: مخزن
⏰
اعتبار: مخزن
🟢
فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
آلمان
🧭
شرط: حداقل 1 دعوت
👥
دریافت‌کنندگان: 21/30
💾
حجم: مخزن
⏰
اعتبار: مخزن
🟢
فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URHdQAq1UKuNGN-lxBCbK4RkhfTznL4VD0EKra2Z1-26yRlnUCiK1sqLQvBm6OXYFQIm2CsmdVVYftgRkm4Q-gMiGKFikwg__gl3506FMWFJ3dzNRiQ7MoTSJXx1nOha1ui_I3sWHxmWujRby7HzAro_vtIaN2XRavjNk-xFOrdioWXW_YKNil1o5643geDl67UZI-IyoPPNQDNjKaRE5uf1Ho3yxm6XsASKSnOuaNoxIx2wACSKOOlNsaOVex6EeB6VXtPeZV97aRVe7eQAvsQN1wJVfboLRO74lpQ_Ni4kuH53DHz1wXwdkycaRjSzl3pHayzWi2O60aPOmMGDBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل جدید
GLM 5.2
از چین معرفی شد
توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و Agent
🔹
هزینه API بسیار پایین‌تر نسبت به برخی مدل‌های مطرح بازار
🔹
مناسب برای کدنویسی، اتوماسیون و وظایف طولانی‌مدت
🔹
دسترسی رایگان از طریق محیط توسعه Zcode
﻿
📊
برخی گزارش‌ها نشان می‌دهند GLM 5.2 در چند بنچمارک حتی از بعضی مدل‌های پرچمدار فعلی نیز عملکرد بهتری داشته، هرچند نتایج واقعی بسته به نوع استفاده متفاوت خواهد بود.
🇨🇳
رقابت بین مدل‌های چینی و شرکت‌هایی مانند OpenAI و Anthropic هر روز جدی‌تر می‌شود و GLM 5.2 یکی از جدیدترین نمونه‌های این رقابت است.
🔗
ورود
#AI
#GLM52
#LLM
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚀
ساخت VPN شخصی (VLESS) کاملاً رایگان و بدون نیاز به سرور (VPS)!
اگر دنبال راهی هستید که بدون پرداخت هزینه‌های سنگین برای خرید سرور مجازی (VPS)، یک کانفیگ VLESS اختصاصی با پنل مدیریت حرفه‌ای داشته باشید، پروژه
REN Gateway
دقیقاً همان چیزی است که نیاز دارید.
این اسکریپت که توسط یکی از توسعه‌دهندگان چنل(AssA7778) نوشته شده، به شما اجازه می‌دهد پنل و تونل خود را مستقیماً روی هاست‌های رایگان
Render
راه‌اندازی کنید.
📌
ویژگی‌های جذاب این پروژه:
کاملاً رایگان:
نیازی به خرید سرور یا دامنه ندارید.
پنل مدیریت حرفه‌ای:
دارای داشبورد برای مشاهده مصرف، ساخت لینک‌های VLESS متعدد و تعیین حجم مصرفی (مثلاً ۱ گیگابایت برای هر کاربر).
ضد خاموشی:
دارای سیستم Keep-alive داخلی که هر ۱۰ دقیقه پینگ می‌فرستد تا سرور رایگان شما در رندر خاموش نشود.
پشتیبانی کامل از V2rayNG و NekoBox.
رابط کاربری دو زبانه (فارسی/انگلیسی) و حالت تاریک/روشن.
🛠
آموزش سریع راه‌اندازی در ۵ دقیقه:
۱. وارد لینک گیت‌هاب پروژه (در انتهای پست) شوید و روی دکمه
Fork
کلیک کنید تا پروژه به اکانت گیت‌هاب خودتان منتقل شود.
۲. وارد سایت
Render.com
شوید و با اکانت گیت‌هاب خود لاگین کنید.
۳. از داشبورد رندر، روی
New
و سپس
Web Service
کلیک کنید و مخزنی که فورک کردید را انتخاب کنید.
۴. در صفحه تنظیمات این موارد را وارد کنید:
Region:
حتماً روی
Frankfurt (Germany)
تنظیم کنید تا پینگ بهتری بگیرید.
Build Command:
pip install -r requirements.txt
Start Command:
python main.py
۵. روی
Deploy
کلیک کنید و ۲ تا ۳ دقیقه صبر کنید تا آدرس پنل به شما داده شود (مثلاً
your-app.onrender.com
).
🔐
اطلاعات ورود به پنل:
آدرس ورود:
your-app.onrender.com/login
رمز عبور پیش‌فرض:
admin
(حتماً بعد از ورود از بخش Security تغییرش بدید).
حالا به راحتی روی گزینه Add کلیک کنید، حجم تعیین کنید و لینک VLESS اختصاصی خودتان را کپی کنید!
📥
لینک پروژه در گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎁
دریافت اعتبار رایگان API برای مدل‌های هوش مصنوعی
سرویس AeroLink در حال ارائه اعتبار رایگان API برای استفاده از مدل‌های مختلف از جمله Claude، GPT و سایر مدل‌هاست.
💰
اعتبار اولیه:
🔹
ثبت‌نام عادی: 35 دلار
🔹
از طریق لینک دعوت: تا 50 دلار اعتبار
⚡
محدودیت استفاده:
🔸
حداکثر 10 دلار مصرف هر 5 ساعت
🔸
حداکثر 70 دلار مصرف در هفته
📌
مراحل:
1️⃣
ثبت‌نام در سرویس
2️⃣
ورود به پنل و ساخت API Key از بخش
New API Key
3️⃣
شروع استفاده از مدل‌ها
🤖
لیست مدل‌های پشتیبانی‌شده
🌐
ثبت‌نام
⚠️
قبل از استفاده، شرایط سرویس و تاریخ انقضای اعتبار را بررسی کنید.
#API
#Claude
#GPT
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWr15AjtFNWZVG2ZwIxgbszoMvqKQMBdG3U9N4smgblsK9xW0Xa0THZLYSXJy3itbFvpcugLpxWCEnqzbWIVspUjESXbrAn-srwgFR6RueAP7lQ568cIzCRxY6DLH0v9bCYMvEZk8sVU-sBFy66zS33SmB18hITB9J5Eo5Y2h0Ptw2KQzpA8gAUbwZR2DEnFwn_wE2RG2VkN8Cm6W-V3Y_s_eVgn2EzwXRv-BDSgzoEKV0A4Bp_3mkVFIcvaXgraqdUK-hrgKTSVItTeBgnZqYVvLPm-2ChJRanaxN6NmrgfrvSqOa7KIURhCytivKDY0tdE_9TkPPpRv0zecI4uYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
OpenRouter قابلیت جدید
Model Fusion
را معرفی کرد
حالا به‌جای تکیه بر یک مدل، چند مدل هوش مصنوعی به‌صورت همزمان روی یک درخواست کار می‌کنند و در نهایت بهترین بخش‌های پاسخ آن‌ها با هم ترکیب می‌شود.
🤖
برای مثال می‌توان GPT-5.5 و Claude Opus را به‌صورت موازی روی یک سؤال اجرا کرد و یک پاسخ نهایی و بهینه دریافت کرد.
✨
نتیجه؟
🔹
پاسخ‌های دقیق‌تر
🔹
تحلیل‌های عمیق‌تر
🔹
عملکرد بهتر در برنامه‌نویسی و مسائل پیچیده
در واقع Model Fusion شبیه یک «اتاق فکر از چند هوش مصنوعی» است که روی یک مسئله همکاری می‌کنند.
🔗
قابل آزمایش در OpenRouter
#AI
#OpenRouter
#LLM
#GPT
#Claude
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
100GB
🧭
شرط: حداقل 1 دعوت
👥
دریافت‌کنندگان: 43/64
💾
حجم: مخزن
⏰
اعتبار: مخزن
🟢
فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcdzAq3MYpMgItOq67segV2CXUTRcHPQbSlFSai-RwJP3tWHpD7PRJiHpKcMmia55l30ZRTDVtHNbc7gWaVT-G02V3ys6Lf2banyDxeRDhEMtU7LX5eayB6bEfJRRv3Bx9v5dlHel4jurN05IjRG6jYZrNEP-0-OVoXoa-KiZM0lZYyiTpyaICxnfUdBik3uw5yJPhSKFvgC-obX8flbqQ7ucAl2W5FBR87-HMntEXWyKMHspT5eKZ_b8XDwO8ShH0kLibhqm3Y0-ZrNxjBQoHx7mhEYKtqpFZQ2LHBwOA7j8hNvpl4bKgTCkfQX29LuWJRn46_XnFMbz_iDMiCzGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFCUFx50RTarV0OnqvF_Dyb98b3dJJBOL3QHSNHP8ZRTLDFDN6IIClCz_divX7s-QR74Bz1GvT85i1wuNOvzihno0DJPy3hRG47CGutlWg-GEgLk4Ly-LwwmGrMRQI_5XTqk-yAF24kqc9Qn95h5vivUVSYWNWVhXhM9Pd8Yy9QUSbB1Rd9dQIEpBj-z_bPd8W0_5exYdSnoYLFgvdcdoInA2ex06QMJUsZoA9FStDRsDzdMsWp0d8T11O-BECeCyQTk6chFhbbHHxaX24E57TanCUqyjOyhMoOXKObTGvb4c-nLBM7dP8sIqrba1P5-NH6K4P9fMn_uRyb-PHqkQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه که هوش مصنوعی هم جلوش کم بیاره!
📖
متن چالش:
"Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off—then, I account it high time to get to sea as soon as I can."
🎁
جایزه ویژه:
۱۰۰ گیگ کانفیگ اختصاصی با آی‌پی ثابت آمریکا
🇺🇸
برای کسی که ترجمه‌اش یک سر و گردن از ترجمه ماشینی (AI) بالاتر باشه!
*(نکته: اگر تعداد ترجمه‌های شاهکار و برنده‌ها زیاد باشه، جایزه رو به قید قرعه به یکی از بهترین‌ها تقدیم می‌کنیم).*
⏳
مهلت ارسال:
فقط تا ساعت
۲:۴۰
فرصت دارید.
👇
نحوه شرکت:
معطل نکنید و ترجمه‌هاتون رو همین الان
زیر همین پست کامنت کنید.
ببینیم چه می‌کنید!
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvd5u6DiHEvmB0XpYaH7aE47AnesLepb9fy_atYeLbqGCq6SYKawi5tCtc9ToinAxDYrRADsYy_nofe-YgA6rHaGmG74hswL9ns8v2IRpaQJJ9AYs6g0ztPEnCG-1oGQ53Ip77jd5QNVYE9aCWQw6on1fRYsLeidcS4DbgI4sRy648thAh8D9uqOYzytNoUOB4zk3QnrqKSSjI1AgJfE2bI_fw51VNan0EH4_l6q4rGcPdj0B97gerFCNQpRLuUYTQXNess8MQzxZf9K8UPQv6uSQF4USkW1F9RKWbVqz6oM6YdmT5eplWXM7syhVxuNZx_k9L9k2MN9vS_2pm0zsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUkFIsaCdq9C-jVVKrHA3o9aXLipnPAl7l_XszCUhgoEtmqm-IZPXK_xflC4cjJab-jyZtoV1GbMwIxsD94FbnJIkCmDc--CJrqnQjH_up13EV1WAhsqCeLy6QUWsAXwDAZ-SEcoAKdo2Y3cHIOKyWBFeKsuAfZtsuJwo8drrZd2vE7IeZeastLa7qOoYllcsjOUDVNmBa0q20mYAWzL3YhE5W2PlkXbRYS-Z46qv4FeM1YDSqmvapWIMDJV1JCgyf-i4TLJEfP-re5fKPShGDI7W1PLJv4mVYAtR3B9PkqW9E4tzvW45jHbagKBreIDcDe1mfHEfKJMXGR6x2tLAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن»
یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like it was never there. Match the background, lighting, shadows, and colors. Keep everything else the same.
#Chatgpt
#Gemini
#PromptEngineering
#PhotoEditing
#AITools
#Design
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzVSNxNaSkLhoWWLyCeOuCSiwxvmkGwLNtMnBF4mEItWy5_OvuiK0nAkhWtfIx_phbEWjcXBhDdze0rjU6mg-uEFNkiYojUa3YisFROGhwk705-ELIlmO18r-BdZXGF-NHotXGdCqk31EUmdLt3voZ78OeSzEahZIwWI-FkeI5JIa4TEOplXHgn0dRSlxk-FvJBcD44vi8biIj4XQ8jy3xGdbtIcEoCe-OyXYseNU7ZqtbynSKUcTkLzBUvTTiEVlESaukf8afHvz1MeHa6Jhv-_XMDS21fGiGNG8zXPmEvt7q_c7VYaFu7Fk0Mxk0SKloZwObhMVXImePuzTgHqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4gzxear1N-fUsjBAqwyPIxGwdWoostqsw6W8hWz1OJdUSo_XMyxgGH8npXeROoe9qxFivtoVqF6OGMNdasLSfM1UXZGn9cQF4jNw6WZ-RpMedIr2boW3FbHhqQ0rXJqQGdxFDos_LvKS76YjLfMIqhRJgcEy_Y_pMUgmCxjZQHl-TEiF0aql7YUx5F2_5jshTgA6pIind_JojKTFpR-Nyy3L8pvrRAD6c9Fk6SJ_WMT7wrXvRpt-tYAu9N5UremRK4KHNmLuAOOiaHD3itd6LP3cNybNcel3XXTzEpEys4f8WuDpyttl6PDNirChBBDd-s0y3Z2pxO7ExQ2fobk9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
روزانه 6 گیگ کانفیگ رایگان
🟠
پنل BPB کلودفلر
🔹
با جیمیل لاگین کنید
https://dash.cloudflare.com
💻
در ویندوز نرم افزار BPB Wizard رو دانلود و باز کنید
https://github.com/bia-pain-bache/BPB-Wizard/releases/latest/download/BPB-Wizard-windows-amd64.zip
🔹
عدد 1 رو تایپ کنید و اینتر بزنید (اجازه لاگین در کلود بهش بدید)
🔸
لاگین که شد بیاید تو پنجره برنامه گزینه 1 رو بزنید و ورکر بسازید
🔹
تمام سوالات رو بدون تغییر اینتر بزنید و آخرش y رو تایپ کنید
🔸
پنل که باز شد رمز دلخواه ثبت کنید و لاگین کنید
🔺
تنظیمات پنل
Common
:
ipv6 رو خاموش کنید
VLESS - Trojan:
- در بخش
⚙️
Protocols تیک گزینه Trojan رو حذف کنید
- در بخش
🔓
non-TLS Ports تیک عدد 80 رو بزنید
✅
بیاید پایین و گزینه Apply رو بزنید
🌐
دریافت کانفیگ ها در بخش Subscriptions :
- گزینه Raw (without settings) رو بزنید و دکمه کپی رو بزنید
- لینک ساب رو در v2ray وارد کنید (میتونید لینک رو باز کنید در مرورگر و کانفیگ هارو کپی کنید)
🔵
@ArchiveTell
|
#Mz</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4Z_C87wQD5Z9JsU6bFmKQqpXUWCrU_TM3u9cEh9M9mgxs4wZMOXtZ_aUrbUMpDiYiFjgPIR0SzPlaABZgKBc6Gmpdj1lOQEFIfHtwr6suoXyHrKFe3xEDTjyNyk8aWLjEi8GN7DeJ7pIPVegddPBSyzqWB8KcvRycBisVW_J649iD18r9n0BIIop6I5QAnlaZYaHizqc9TdxKeallZ7Y8C0Iuwjd5ekOuhYXV3gScYsmNeRvrbP9rcBXcDQL40vMa3CzQai0U2P3Uxh8UdiSefenrsJuPGgAo5-V0USkgDUhuU8R2lwobk0FsvwskHQeBZaVwThOrvCG6IVc3VXZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😬
کاربران Gemini از محدودیت‌های جدید گوگل شاکی‌اند!
ظاهراً گوگل بی‌سروصدا سیستم سهمیه Gemini رو تغییر داده و حالا حتی بعضی درخواست‌های متنی ساده هم بخش بزرگی از سهمیه روزانه رو مصرف می‌کنن.
😶
🎥
بعضی کاربران می‌گن ساخت یک ویدئو می‌تونه کل سهمیه روز رو با یک پرامپت تموم کنه!
👀
«جاش وودوارد» مدیر محصول Gemini بعد از موج انتقادها گفته تیمش در حال بررسی ماجراست و احتمالاً تغییراتی اعمال می‌شه.
📌
اگر این چند روز حس کردید سهمیه Gemini زودتر از همیشه تموم می‌شه، احتمالاً تنها نیستید!
#Gemini
#Google
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=L5YBt1LynbmUTAj6ClSygS-Ifzh5JwjdMc3ianh4ZNMNofBp0AGNFi2jFZR0P5AEGXoQq7_YnaX7BSvJRYfjRWr08tlGP5Slr5D6abGTHXdVHWmrS1ezS2Fk2YY3TI53VgNcmixC6bUQxZBe6exD8avOJlu27QUlSMnExVaB3ptYOONQyQ2-qvUTG6O9O44-W4B0xaa3CgdLto6Jtdbkr5LDcwFqXLSeNLQIMt18oMetZ6bGY2KReWf3XEXoQeyPDGrb7FQ2duuVdsAQWmCJFspS5aUEF1rG1shO9HiZhcBsfJ6QJTDV8VAyJ5wrYBNzc0OVic6QlKICFtXRVuoSbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=L5YBt1LynbmUTAj6ClSygS-Ifzh5JwjdMc3ianh4ZNMNofBp0AGNFi2jFZR0P5AEGXoQq7_YnaX7BSvJRYfjRWr08tlGP5Slr5D6abGTHXdVHWmrS1ezS2Fk2YY3TI53VgNcmixC6bUQxZBe6exD8avOJlu27QUlSMnExVaB3ptYOONQyQ2-qvUTG6O9O44-W4B0xaa3CgdLto6Jtdbkr5LDcwFqXLSeNLQIMt18oMetZ6bGY2KReWf3XEXoQeyPDGrb7FQ2duuVdsAQWmCJFspS5aUEF1rG1shO9HiZhcBsfJ6QJTDV8VAyJ5wrYBNzc0OVic6QlKICFtXRVuoSbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">WhatLetterAI
تصویر را به متن تبدیل می‌کند و به هر زبانی که بخواهید پاسخ می‌دهد!
📸
🤖
✨
قابلیت‌ها:
•
🔹
تشخیص متن از بیش از ۱۰۰ زبان
•
⚡
استخراج متن از تصویر و پاسخ‌گویی هوشمند به سؤالات محتوا
•
🛠️
دریافت خروجی به زبان فارسی یا زبانی که انتخاب کنید
•
📦
پلن رایگان با محدودیت ماهانه برای ترجمه و پردازش متن
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0kxIIrHD4tTzl62HMxXncIAZSyKyGY7eObS5Cqb19VdQoCSUnd7HVjqLY7dR3YGST3C0ZUpgG0YuBZvqhIDRdXRRVwcDWoO2Rd1bnAXKfvVXE6j5IAUZVmScvuuafTu75La8eZp8MUxbUvsV3GKz6k4fg8PZpHvKf7s_1m2wzy-W6bYp3a3AQpUL2-Su_vi1_st-HLCk0GPEbUWy7y3JIrtunDccx3Poz5c1zxuXFCyhDcqA4848ubWI6yPuwnjsY6LLsihqeHJuyEL45NHmj2Za36-HROYgjacpIH31PEPyU5N14DdnLWHNV4u6x1zMghtpFA3pIM9vcGJfqbrAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تولید رایگان تصویر هوش مصنوعی
🔹
بدون نیاز به ورود
🔹
خروجی سریع و بدون واترمارک
✨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfD9KHQdE74RlOGSe4f18EUE8o1biXlc0ZFCz7yVD2vTZ6cXWeitWC-QAFUWvvv4gn6eSJpZVi0x45UlHKGGfXWlQ0-99FLxYNNRkr2FYsyzViquvezj7LbbfK4o3JQT_cLtQFWrcmRJexatenSHlR-mZKxtp_oAPrlP0orfqOWJl0vDEo6C7jsPrU74RoIaTnm9lWv-9THPWy6N6jZCJtGtuHGl7UYQoOHkgDGP0uzezgW574dW4D-0Frs-mlD983j5hULkzb192nzOG4rd1X-vo1cvyeKRPshR0UbFcuBgnJHw0B0h3nptCa4YAof4_AP-Ai1gNxhcVI0s6FxUDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=LqnDObBFJYmaUGLRwxeqhwcATRyQqjzIORUcNJKEMBHaFt8vglTeYTcVP56wBvaVZU7CeZ0WAW7GhVH9bTLgDDzNg8sTGGNO7cQLq6cJnZXhyps1EuUM6sXE2dnWebTQ24J1fD1d09StNSVkcfurgQtQn4lRsU18Kpfws3Reqg_2sxGjdAfeUAXbGLjh4VHOAcui-KzWhtXnt4hyCjLlyNpfuJEqth1gyeWv8xgF_RNgDFyMiKbIWTA08fsFalxx7MnUQi-80unxEO9WCINIgSVJp9ucANrVySTQwpREe76Tsu7rfEi4GdfKjoX0xL2NtAPDV1ZbV9U_6_g04EnwxFajtaw-YDG6uM0Su49DeEBd3OOK9D40uGlIr_Xflvanj9YcDVRzkvpM_uO9zSN9lA_ePcIoXmqf2TkmkH4Y-0Wa4jpaaNwyCXJTbV_gT5L_cuO88Zkgs1-AF0PCmCtB783gj3Nx1Tvgw7IqM1HvTCvYImoajY-ADs57ZE0uqWalGp_865lz7K4PiHXUhrmt1zxkx8hRBusw-OqcuYSRK1XBZBiomSlI3iDIlDpOPlQzDIkxrRm1NtOe82gWMy92jOPMota46qNcQoLSTwhNHCqoMkYtyylMjAfn_NOqADUkTunF5CMbBWlr6CVUMwnj8TbAska53SqsKfGD1-l5NI8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=LqnDObBFJYmaUGLRwxeqhwcATRyQqjzIORUcNJKEMBHaFt8vglTeYTcVP56wBvaVZU7CeZ0WAW7GhVH9bTLgDDzNg8sTGGNO7cQLq6cJnZXhyps1EuUM6sXE2dnWebTQ24J1fD1d09StNSVkcfurgQtQn4lRsU18Kpfws3Reqg_2sxGjdAfeUAXbGLjh4VHOAcui-KzWhtXnt4hyCjLlyNpfuJEqth1gyeWv8xgF_RNgDFyMiKbIWTA08fsFalxx7MnUQi-80unxEO9WCINIgSVJp9ucANrVySTQwpREe76Tsu7rfEi4GdfKjoX0xL2NtAPDV1ZbV9U_6_g04EnwxFajtaw-YDG6uM0Su49DeEBd3OOK9D40uGlIr_Xflvanj9YcDVRzkvpM_uO9zSN9lA_ePcIoXmqf2TkmkH4Y-0Wa4jpaaNwyCXJTbV_gT5L_cuO88Zkgs1-AF0PCmCtB783gj3Nx1Tvgw7IqM1HvTCvYImoajY-ADs57ZE0uqWalGp_865lz7K4PiHXUhrmt1zxkx8hRBusw-OqcuYSRK1XBZBiomSlI3iDIlDpOPlQzDIkxrRm1NtOe82gWMy92jOPMota46qNcQoLSTwhNHCqoMkYtyylMjAfn_NOqADUkTunF5CMbBWlr6CVUMwnj8TbAska53SqsKfGD1-l5NI8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎵
LoFi‑Engine
ساخت رایگان موسیقی LoFi برای خلق فضای کاری دلپذیر!
✨
قابلیت‌ها:
•
🔹
تولید محلی قطعات منحصر به‌فرد LoFi
•
⚡️
صداهای طبیعت (باران، باد، دریا، پرندگان)
•
🛠
تنظیم تصویر و طراحی فضای کاری به دلخواه
•
⌨️
پشتیبانی از کلیدهای میانبر برای کنترل سریع
•
📦
کارکرد آفلاین، بدون نیاز به فضای ابری یا اشتراک
•
💻
اوپن سورس، سازگار با ویندوز، لینوکس و macOS
🔗
لینک
#OpenSource
#AI
#Music
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=HZW2jtgdQA4rbXPofmmDXHgTb4-qtXwjEcTL4K8gPTqeacA0FHsMrDpi6IhA3oDjfM1AzdbQyXhJnpcjQr3J3IQdQrWUa6vYSXIRFYpu-DccDFCozs2_N5rzj5EspltDnXC-oYFAG8_qvGtD38v6jl2YLIm2dbdn4uOgMJMiXYFYUXlPqi6Oeyxlk1OPpC0uidODyQFx2csd6_D5bwDZgVjEBKPBUNw3-6ES4AqU4i7FImYbO-FTAR8WgCB1gy4jYVLwOBf7t3znf6eBYw2ePLA-qksff3ldSEWKakvRrKXzrqWnsGQQKSKtryrWXRtG9DsdARKpA-NJVi28UBmH9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=HZW2jtgdQA4rbXPofmmDXHgTb4-qtXwjEcTL4K8gPTqeacA0FHsMrDpi6IhA3oDjfM1AzdbQyXhJnpcjQr3J3IQdQrWUa6vYSXIRFYpu-DccDFCozs2_N5rzj5EspltDnXC-oYFAG8_qvGtD38v6jl2YLIm2dbdn4uOgMJMiXYFYUXlPqi6Oeyxlk1OPpC0uidODyQFx2csd6_D5bwDZgVjEBKPBUNw3-6ES4AqU4i7FImYbO-FTAR8WgCB1gy4jYVLwOBf7t3znf6eBYw2ePLA-qksff3ldSEWKakvRrKXzrqWnsGQQKSKtryrWXRtG9DsdARKpA-NJVi28UBmH9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
Runway
با چند کلیک، عکس ثابت را به انیمیشن تبدیل می‌کند، رایگان!
🎞️
✨
قابلیت‌ها:
•
🔹
پشتیبانی از تمام فرمت‌های رایج تصویر (JPG, PNG, TIFF…)
•
⚡
افزودن جزئیات گمشده توسط هوش مصنوعی
•
🛠️
تنظیم سرعت و طول ویدیو به‌صورت دلخواه
•
📦
خروجی MP4/WEBM با کیفیت بالا، آماده انتشار در شبکه‌های اجتماعی
🔗
لینک:
https://runwayml.com
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">uk-new_domains.txt</div>
  <div class="tg-doc-extra">21.8 MB</div>
</div>
<a href="https://t.me/archivetell/6351" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آیپی کلودفلر
آمریکا انگلیس آلمان
با این آموزش اسکن کنید
https://t.me/archivetell/5657</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">Cloudflare Germany
🇩🇪
103.21.244.0/22
103.22.200.0/22
103.31.4.0/22
104.16.0.0/13
104.24.0.0/14
108.162.192.0/18
131.0.72.0/22
141.101.64.0/18
162.158.0.0/15
172.64.0.0/13
173.245.48.0/20
188.114.96.0/20
190.93.240.0/20
197.234.240.0/22
198.41.128.0/17</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">Cloudflare ranges
74.115.51.0/24
23.227.38.0/23
185.158.133.0/24
216.198.54.0/24
212.104.128.0/24
216.24.57.0/24
66.235.200.0/24
198.202.211.0/24
103.133.1.0/24
199.60.103.0/24
63.141.128.0/24
137.66.28.0/24
137.66.28.116
185.133.35.0/24
208.103.161.0/24
185.148.106.0/24
209.94.90.0/24
160.153.0.0/24
199.34.228.0/24
160.153.0.0/24
198.41.223.0/24</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dE2CJU20QnjowvbLm129SFFN_6yERsObEz4NdznFZB9LkkqmduXDcPlsp_zyiKSpmSFkElqaWqrXQH5MjYkZnEBjcLC2sWw-nTHfQ8AdHkX2AwcS2YONRje8OCUn3S6v-Pf6CSYNNU1vc5hUQQk87t8fls409rQJscKs0UrvHQCUcdwHLtYx-9oqO401RZTVg_u6sM3hb_-CWrZvkaF4CCJ5-gvDGQhg9HEZrSXSGZFAGKv6bKCAJvOtod48sNYEcjO80LFrJozXMZPdEfNmjfUYNQ-bnfZQxXs3_xHIz70Ptpu89A5NISmH4pu4eF81euTp8jObGRtLJvTSCRldwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4ezSI7BzWIyv9espp5-Leuodc02HG658S59fdyLqzW3HDn8tUigUtAVwpp8_1iTNGEaSIyZmmAVU3F6mv_4rRvbJrEdn7XOJq-749CnmH8cZVbF14jTbYV-AbwrbtN34HbADlS1D1OL_JLgjwies5cCMxVqZVxfaPFpmEqB3G5Xusw0r0HuUhyX7joBD5PMZCttqaN0b1IZBVZVkda-vzb-X08DAu5ctPFD8UmpJ6KPD2rnNE4r2s405q41KklN4fX6pCA17sZ0mLbZ7j7dRARGQki-lsePIuoBpXhO5AggyBwcczd-X6BmTfdQvW6BQ0W9xw00h0kmSlFEcmGagQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_a1OkQzDiZFyQnRsIycjrTokKenqIqGg3nQI8RRt7NDi4ikp-1BvXSIg00kPOGsZGK22NMkJmh7EElTsGjdFweGNPAUv9g6c2axeYPyBIZVJr9T1LiWU0OvxLAMaqwY8zxm4puqnHTJ7fuR8cA5aJ6uST-uYOyHuDEecJxI0Mydk7T2IhMTZHDd7QcRm-l9vOqp6eeFYg-bOzpGtHO5rW1d_1sHsoTS_DVz0fx2ALEYvNpq4uhbPZaCWxYBSOyo1cbd-TFhC1OHmHCUB7uCOGrLaHkgaUY23yIkZLjjUvZfrZq6MjQfp0wJhYETWUu72OOIIEIer3EH18tDrCPb0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c83S73kdk996dnf6OH5niX1j5BSrh2jTmmyaWnSryuLcyS16p2n2F1M_epyRDoqER7z9f0axOvhwE3QpbGAVXKlONd6IBENVcocaLUr8jbsVJNYEYAOwzeeT2tg2eseNn023jTxnd8CFKg3y_eu0q-r17Vl7SxSd7z6O7HdwvL8pBoChTsr5Bkts0R46UqN7eTwW59iscuaRgrnE9KXHHMhytYdNYolwg1hhrS7AIwBGQEdVBqxcz9pKwTXunddchFSZb2Vv0pqVvsbzVbe8LC1iAVpGkiPQUwLik45lmKNZFrZB0cHXmolcjEnj9Fa7IjkZ4D5clx2Evhm69MooDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bsLd7RXJ8k8JWTVvDlEmLNzCjQytcWkzsDj3bd0CIre3NWSyoId5Bv08cFiwTN2SBk8uQ6aiE3WXe6e70zhwaQaIx_a7ZXUle9x3XGbTIC3njgUsBr1lFVWqjMeOEL7YnhIjdCemLJlrIZkB93oghRQYO30HtmDBboCtvb3Vg1h0b5PAjgw_li4e5jj8RA7TE8qq5c6n-P7e-dTGDeUbghoAlfOk5lDYcLboNZJ67NGFnAkEDUfUYft-sZiFptB8YWu0sWGtw1A_lknvMxNpzdIPSWYCVLYZuwz-TatDhmqCLBqhSnZJehIsRPPVywMN1gUFDdfzK98-TaKYrLgDvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">7. به صفحه اصلی ورکری که ساختید برگردید و بزنید روی پیجی که ساختین تا باز بشه
این صفحه nginx که اومد یعنی اوکیه اگه ارور 1101 گرفتین یعنی اکانتتون بن شده باید یه اکانت جدید کلودفلیر بسازید
به اخر نوار ادرس یه admin اضافه کنید تا پنل باز بشه و پسورد رو وارد کنید و لینک سابی که میده رو کپی کنید و داخل ویتوری وارد کنید.
کانفیگایی که میده اگه پینگ نداد نیاز به ای پی تمیز کلود فلیر دارید.
مثلا این رو با پورت 443 وارد یکی از کانفیگا بکنید تا وصل بشه
188.114.97.6</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrQR_HPAaa1Smlypf-E7EVqokxfYN0O03RMmUhd3yjXBq0ug5DQkcOPpV6cH9W2w6WJgRs4IRYUU7BhNQilzUENX0BeP8g9Kw5O5TxHDhSn3IaHyCtHfdXILQnp1CxJWXBaQx-iolZQZeE_JSsCRSvBfBYNZHep8aLQzEDX1gkt9uFuH9ru3jHJ11TBRgaQbroMemaVhHRcuJ8g1u_W_CEk3VED3nD3B_byH_QQAsSFiq07S92Prf2pPuV4YzDZz8CUBgWGMCeM144470mvxum0nJP9SdtpFuaWA6xNxdcNF3nVmwaaFckkrmto6HUBl6ARLE3ll0deEeB_aSrr_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNSqOzHQuXi3Mn3MAmHiLLEZNr3WfwAJ4mKQKUuiDi0dEstldYFEd3AO_2AQybgIj65mnDw024z8I6QnIpjFVhy05sMb3K_Ga1E0dB3RUIcFRMzLWpZpwCIXOpnHp4DcSGLT4bASp_HiTqEFlDUIIn3BbdCGck8aWC0XVqFUhgemIq4jzpBdFrmvBqay4CDBBsVxeNTmgimAdCLeWbsN58KqtAQwdba_mCpSm2u3jQungHsboCxYMKP6jWXMJMfgHr5US_CDXtWXLpO_ejNgas98YdD7DFagCzCwLXMBuupBvlNO6DBDhOhpWm7MWjQa1nyXLnMaY9nCL5NPt6ib0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YU5GYZerFRYzsQW6VtrnsKowPd-8D9Y09taIpHaMGA9cMGgdc0lriahUZOqdYqRx8MbLUGdWHRpRij1ut_lJM4tkmHUi9biW8KITrJQl7yxfWocl6ydm7T1dSHn6ynMT-br9drX3UauHtnt3Y0jajDjvmKu1d7FgNqXgOaUrHQAfVl8PWjfTaIPFUaPzOu16JzKpRKCC3woIT0ENK3xqBLaWrAnhXxV0WTPkZbiQpg-6t6JfJBlKUw9bVMYtNUXF5x3iDIjfmICHPWhnddM-H_6Y1zbtXcR8ZTMENtcKrw18oNpGV9NmUqYNDGWbsRSbgv8q62b9KKECGeuxI2xaDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghOvSARIF3ZsGvRdIPY17zNmFvgkDAZ4v6cya86Z_zhjaR4DCH6X20aWNn1vJmLL0LYiYK9Yaq6C9BkgyU-34nLWAk6j8mfwBIr1sSayYOSR_KcDUvnE55H_wOawQRvtFV3X5gUgprUCS6IdaxOHI66L8jdGu5LFUNyI9I62oZLni1n4P80-9MDhtVNdZc6ENUCLCiKGkq5LfmYw9FYvIDqeWEBqeeRL_vQhtHYh9pble8l03FsF3cWp_CBFnw3BPxP8YhcLzi5KtduqRjrtKjThsS6DIueIIWIpesN8nh_lBMYGzXwuS76PV5_Gu6LO6WHRJnFd_9JXbj7coFNfSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A51s7up2hHWKAZ_dGeRxJfnh10JkEvmXmrgCzvvT8Wq44gR9gGbL4YN18P4eNBOMqRLRtyD8Jr832uSFJoJ328GJzcqo7SqB4oYONTnaL9itz-velHayMHWar7fb-TJLVqFhUPu2uqaHtnMoLsdBoHm8p77AAkPMeHki2dmHDu0K8QVSNGohpgtZFO6XozbL0IvRpL2QnJohv29uuw8vdhNNm3cZkrd9tWyU6UFmhO68gIhCKfQ40P6d8sSV8ppOj-VRu23ws8gtIbFN1I2iPQCLctse_W6gNrBSZjlVJIrWda4Vwia2BmeUIIYqZbueo4HD8Erkh7t5BGAj90-cgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOqTz29qTNwWv7oIpNbV6fYwcbwZl--m3QA2swKVjpM2KYi5gXFUhlcR-bFRGOJwZrphnQ-YbptLIWTeCE8WLo9tKMv3HJDyoHc3C7g8126RtFoS4zz6Syh2aa8-iZ1LKEzVYlfQ25IH43xEjdf65N5PaM19_e0_sPihSORX3iOQnRkWS9-IAlzpdYN6d-dKi_v7joXr0Sx8Sxr8l_ySSYPitY0WGb5pEPVGJlTWs_kjNvxBoXkQGXlulqt0AdGdbIS8DsthV3ZAbkN5wiG5CSstamTNcfk---WfYKyLSfFozzSga5hKA8WqPvP1KicFyXv0HRVW_Z7npHd27PFd0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1ofmrErqLzrs-TEwozVO9x8VfvH_0rt1F4OHvQ1l4v7_4om7Er7qKC1-SZoA2XlizI4qixcNmqywf4v2kYLFr27OTDdkY8WYdLZamaF5ftPHKPGp2e43O_OcNyGjf0Ectbt-QmmCBhKCjzJV8miYLaXYEwTnEZBQpylZWPub6muC6T91Dud8VItxHdvGIsfkPr2aEOkP7a-aTqroeJfV1DVjvklaQ5qXZZ-daaGmzmVwZa-46H6Ebm0l6-D8RcOFgQ9BuUPJE43UjdHBhU0latXuyiMYwUDckLXzSEIEd0VtYQilqIp-qgwv52KjQZ4jDOq3NOWvrN7cYFNvW0okg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=QAQbCSdHIwBSNhJeN-PTcyQD6UExmmlZPSku9IUHwUsPeEYgxm9uABxDiZEFpevMqnoLcWNUTiOmZXfKx0DVKmmvDQEbi5jQ47PPNHCbuR8CrrqkMlPlNVX00IyLWPpJCJiu1HhoLQrJuz8RRpYL6s6Kvc-v7-YF9bewoagZMnrP53EtfiHqiXeei-HDprX0MOeJFZR9oXpF-6NAM7hk0yePoPSJJnYme_IgRVx8-SrbaVS9P5CplKXp2-wdiW3G5t7VZAwH3YoKb0R8Lre65MEJ076NZy1b_ldvniTLkV3_Jr1rNUII1zk8yV_m712YcK4WXCvvY3F0CgXV976Qcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=QAQbCSdHIwBSNhJeN-PTcyQD6UExmmlZPSku9IUHwUsPeEYgxm9uABxDiZEFpevMqnoLcWNUTiOmZXfKx0DVKmmvDQEbi5jQ47PPNHCbuR8CrrqkMlPlNVX00IyLWPpJCJiu1HhoLQrJuz8RRpYL6s6Kvc-v7-YF9bewoagZMnrP53EtfiHqiXeei-HDprX0MOeJFZR9oXpF-6NAM7hk0yePoPSJJnYme_IgRVx8-SrbaVS9P5CplKXp2-wdiW3G5t7VZAwH3YoKb0R8Lre65MEJ076NZy1b_ldvniTLkV3_Jr1rNUII1zk8yV_m712YcK4WXCvvY3F0CgXV976Qcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
