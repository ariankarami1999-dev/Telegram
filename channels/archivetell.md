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
<img src="https://cdn4.telesco.pe/file/TfG8o_W9IfclDPleEO-4ejekbKIYpX8B00-ZtJIb58rp4nU1iSdo4VZtTcpklMmJ3G40I9MxtbM3VciKzcqkRDp_8SXH7YPi_OvDIDEfGhjHbx1SeEk-5m2pGINV9QkDbFSse6-knTSFaQjIrYut5GFusD-Tul-2oWabVzoe7Hy28l-APUx9NNEi0_ez-NGIFkxq2ST8Gm6Ohmaokl-Jxf-YkwD9aa_ULUVJZadh4qVUY5ZmwvVAyWfn4OeIg2cBv7KsmSqLiqdSil05pAvHLJ_AAvM5FHew-tqyy-48GCwjpQJ2XNk-Bl9znU8tP9GJ_Gy276nv3o9yYNg-OLgCPg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.64K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 01:19:55</div>
<hr>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">📰
خلاصه اخبار مهم سایبری و تکنولوژی هفته:
🚨
✨
🔹
آمریکا و توقیف AI:
دولت آمریکا برای اولین بار در تاریخ، انتشار یک مدل هوش مصنوعی (
Claude Fable 5
) را به دلیل خطرات امنیت ملی ممنوع کرد.
🔹
هک بانکی در ایران:
یک حمله سایبری سنگین، سیستم ۴ بانک ایرانی را فلج کرد.
🔹
شنود تلگرام:
پاول دورف اپراتور بزرگ هندی (Reliance) را به رهگیری ترافیک کاربران تلگرام متهم کرد.
🔹
خطای مرگبار هوش مصنوعی:
یک سیستم AI در برزیل با رد درخواست بستری اورژانسی، باعث مرگ یک بیمار شد.
🔹
فریب موتورهای جستجو:
محققان ثابت کردند موتورهای جستجوی پیشرفته AI به‌راحتی با یک کامنت هدفمند در ردیت (Reddit) فریب می‌خورند!
🔹
ابطال گواهی‌های SSL:
شرکت GlobalSign به دلیل تحریم‌ها، گواهی امنیتی هزاران سایت روسی را باطل کرد.
🔵
@ArchiveTell
| Bachelor
⚡️
#CyberNews
#AI
#Telegram
#Security</div>
<div class="tg-footer">👁️ 683 · <a href="https://t.me/archivetell/6489" target="_blank">📅 23:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6488">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚀
معرفی Prompts.chat؛ خفن‌ترین و جامع‌ترین کتابخانه پرامپت برای هوش مصنوعی!
🤖
✨
اگه می‌خواید از مدل‌های هوش مصنوعی (مثل ChatGPT، Claude، Gemini، Llama، Mistral و...) خروجی‌های تخصصی و بی‌نقص بگیرید، سایت
Prompts.chat
کامل‌ترین مرجع برای شماست!
🔥
چه چیزهایی تو این سایت پیدا می‌شه؟
1️⃣
قالب‌های آماده و کاربردی:
نیاز به نوشتن یه رزومه‌ی حرفه‌ای دارید؟ یا می‌خواید یه قرارداد پیچیده رو تحلیل کنید؟ پرامپتِ آمادش دقیقاً همینجاست.
2️⃣
پوشش تمام نیازها:
از ایده‌پردازی برای کسب‌وکار و تولید محتوای مارکتینگ گرفته تا خلاصه‌نویسی دروس و برنامه‌ریزی تمرینات ورزشی.
3️⃣
خروجی‌های سطح متخصص:
با استفاده از این پرامپت‌های مهندسی‌شده، هوش مصنوعی طوری جواب می‌ده که انگار یه متخصص حرفه‌ای اون متن رو نوشته!
🏆
اعتبار این مجموعه چقدره؟
این فقط یه لیست ساده نیست! این دیتاسِت
رتبه اول بیشترین لایک در Hugging Face
رو داره، بیش از ۴۰ بار در مقالات علمی معتبر بهش ارجاع (Citation) داده شده و حتی در رسانه‌های بزرگی مثل Forbes و دانشگاه‌های تراز اولی مثل هاروارد و کلمبیا هم ازش نام برده شده!
🔗
لینک ورود به مرجع پرامپت‌ها
🔵
@ArchiveTell
| Bachelor
⚡️
#Prompts
#AI
#ChatGPT
#Claude
#Gemini
#HuggingFace
#Tools
#Productivity</div>
<div class="tg-footer">👁️ 694 · <a href="https://t.me/archivetell/6488" target="_blank">📅 23:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚀
معرفی Upscayl؛ افزایش بی‌نظیر کیفیت تصاویر با قدرت هوش مصنوعی!
🖼
✨
اگه عکس‌های بی‌کیفیت، تار یا سایز کوچکی دارید و می‌خواید رزولوشن اون‌ها رو بدون افت کیفیت به شدت بالا ببرید،
Upscayl
دقیقاً همون ابزاریه که نیاز دارید! این نرم‌افزار کاملاً رایگان و متن‌باز (Open-Source) با استفاده از پیشرفته‌ترین مدل‌های هوش مصنوعی، معجزه می‌کنه.
🔥
ویژگی‌های کلیدی:
1️⃣
پردازش گروهی (Batch Processing):
می‌تونید یه پوشه پر از عکس رو بهش بدید تا همه رو با هم و به صورت خودکار باکیفیت کنه.
2️⃣
افزایش وضوح و شارپنس:
رفع تاری، نویز و پیکسلی بودن عکس‌ها به طبیعی‌ترین شکل ممکن.
3️⃣
مدل‌های سفارشی:
امکان اضافه کردن و استفاده از مدل‌های هوش مصنوعی دلخواه برای رسیدن به بهترین نتیجه ممکن.
4️⃣
پشتیبانی کامل:
سازگاری با سیستم‌عامل‌های ویندوز، لینوکس و مک‌اواس (macOS).
⚙️
نکات فنی:
* این برنامه با زبان قدرتمند TypeScript توسعه داده شده است.
* برای اجرای پردازش‌های این ابزار، سیستم شما به یک کارت گرافیک (GPU) سازگار با Vulkan 1.3 نیاز دارد.
🔗
لینک دریافت و گیت‌هاب پروژه:
🔵
@ArchiveTell
| Bachelor
⚡️
#Upscayl
#AI
#OpenSource
#ImageUpscaling
#Tools
#TypeScript
#Github</div>
<div class="tg-footer">👁️ 971 · <a href="https://t.me/archivetell/6487" target="_blank">📅 21:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آیپی تمیز بذارین اگه قطه
وصل میشه</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/archivetell/6486" target="_blank">📅 21:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFrGFWOJ3koDVqsGpljhk1yGMl7h18PZiWgzekFmuAx2J5CRYez1GDJPKZ1JewPwql97KNHRDcOwKIio9YAgn_aDUQZ-KMmIasUaeJDQhzgJquBmUXk0r6HYyU6XABMlWWGHrBvmy5job9VVOd3kuSHB-SdudEWztw5mrU_oAXraU4shN366Le4ofHAdZ5fzfqodn4L6PZmES77CY3TI-rho8ouXjk2yR5scUIGKvipoWLEQb8aWMC2G5lLB3xHuH2EZR8mbiXVoeEMvvRo5DKERP1sNW-jx8ionvCo9S3xv4KLl7v5QaXil7i4bjiDryjyWYFeFXsps7mWijSaCQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت What Is This Movie کمک می‌کند با توجه به صحنه‌ها، دیالوگ‌ها، جزئیات داستان یا نشانه‌های بصری دامنه جستجو را محدود کنید و سریع‌تر فیلمی را که نامش را به یاد نمی‌آورید پیدا کنید.
🌐
Site
#Movie
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/archivetell/6483" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTS46cPR4UyI8m6mShwmcnKJ7B7vpaWklTBQv6RPEwXK8Fbdrrv4zrZs3QuvVUQghrLMSKSlOgw-5_6VjjsupPFHIfAUPQfTziKnpmV9j9epC5S7ZK0KVPrzexpub6YQhbdVFCA2vUg_MDMnYLEyvl8myRIeGMHaaojuUvHRBhi8RGBZeSd8cgZeICeMuw8ktZEqH85BKFemFQ-2vLL6oPOad5WkRx7M2m2p0MfarJnNMn3acWllXkV7iVvErUqq84vbIPdmjPkkaBGIvLlBQ18vfj898EMinz6dWIq-bdqBhnJYxDdys3OO8zIdH9Y0q4t1PAFA18frsRkALU1qjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف رایگان واترمارک Gemini آنلاین و بدون نیاز به ثبت نام
🌐
Site
#Gemini
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/archivetell/6482" target="_blank">📅 17:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚀
معرفی Lift؛ هوش مصنوعی رایگان برای استخراج و پارس کردن فایل‌های PDF!
📄
✨
تیم Datalab به‌تازگی مدل هوش مصنوعی قدرتمندی به نام
Lift
رو منتشر کرده که می‌تونه داده‌ها و اطلاعات رو از فایل‌های PDF و تصاویر بخونه و در نهایت یک خروجی کاملاً ساختاریافته و تمیز با فرمت
JSON
بهتون تحویل بده.
🔥
ویژگی‌های کلیدی و برجسته:
1️⃣
دقت و کیفیت شگفت‌انگیز:
توسعه‌دهندگان این مدل ادعا می‌کنن که کیفیت خروجی Lift به‌شدت نزدیک به مدل قدرتمند Gemini Flash هست و از خیلی از مدل‌های متن‌باز (Open-Source) فعلی بهتر و دقیق‌تر عمل می‌کنه.
2️⃣
خروجی ساختاریافته (JSON):
این مدل دقیقاً خوراک برنامه‌نویس‌هاست! داده‌های خام، جداول و متن‌های به‌هم‌ریخته رو می‌گیره و یه دیتای مرتب و آماده‌ی استفاده تحویل می‌ده.
3️⃣
کاملاً رایگان و در دسترس:
این شبکه عصبی صددرصد رایگان و متن‌باز منتشر شده و می‌تونید بدون هیچ هزینه‌ای ازش تو پروژه‌هاتون استفاده کنید.
🔗
لینک‌های دسترسی و دانلود:
گیت‌هاب پروژه
مدل در هاگینگ‌فیس
🔵
@ArchiveTell
| Bachelor
⚡️
#Lift
#AI
#PDF
#JSON
#OpenSource
#DataExtraction
#DeveloperTools</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/6481" target="_blank">📅 16:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcwxwAus3AoD1ZcbNJInBM0TjQ7GPB_YufaItVQgiac5n1RC-aXj9pIax0CXIknl9n28YQSNIkAVnx49YebQjr16uIh-cpxLcQ8rk_4OhCzEVxMoU0Bv9SxCKz-GI9r_0kpCH1U4DaN1Go81Gr4UOfPdtJg45_Ldxl7rpy6r-VsV5OGQD0FVqZvUoZTS8J3_E9a7uMWdeNSRG8LldTVNydHigroP3QpbSds5pmyOvjwlhDtq_qd4xWJDaJi9Mjqt3RTMT0d9_VNxrLiPY3aV1GciO5VXswSIbvAYpBTjdqgD-8Nq_Rya90wMM3zE1c1W6B98tzqJESt1wwS8l6hnCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
مدل Gemini 3.5 Pro احتمالاً ۹ تیر (۳۰ ژوئن) منتشر می‌شود!
🚀
✨
🔹
شایعات داغ:
کاربران شبکه X پیش‌بینی می‌کنند که این مدل قدرتمند دقیقاً در آخرین روز از مهلت وعده داده‌شده توسط مدیرعامل گوگل (۳۰ ژوئن) منتشر شود.
🔹
سوتی عجیب گوگل:
در حین آماده‌سازی بک‌اند برای این آپدیت جدید، رابط کاربری تحت وب Gemini باگ داده و اشتباهاً پاپ‌آپ معرفی نسخه‌های قدیمی (2.0) رو برای کاربران نمایش داده!
🔹
نتیجه‌گیری:
این گاف فنی نشون داد که نسخه وب جمنای هنوز پر از کدهای قدیمی (Legacy) و باگ‌های پیش‌پاافتادست.
🔵
@ArchiveTell
| Bachelor
⚡️
#Gemini
#Google
#AI
#TechNews</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/archivetell/6480" target="_blank">📅 15:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚀
معرفی WinScript؛ ابزار قدرتمند و متن‌باز برای شخصی‌سازی و بهینه‌سازی ویندوز!
🛠
✨
اگه دنبال یه ابزار سبک، ساده و متن‌باز (Open-Source) برای شخصی‌سازی، سبک‌سازی و افزایش سرعت ویندوزتون هستید،
WinScript
رو از دست ندید. این برنامه به شما اجازه می‌ده اسکریپت‌های اختصاصی خودتون رو برای ویندوز بسازید و روی هر سیستمی که دوست دارید اجرا کنید!
نحوه کار:
خیلی سادست! تو رابط کاربری برنامه، تیک قابلیت‌هایی که می‌خواید حذف یا بهینه‌سازی بشن رو می‌زنید، یه اسکریپت آماده تحویل می‌گیرید و هر زمان که خواستید اون رو روی سیستم خودتون یا هر سیستم دیگه‌ای اجرا می‌کنید.
🔥
امکانات و ویژگی‌های کلیدی:
1️⃣
حذف برنامه‌های اضافی (Debloat):
پاک کردن اپلیکیشن‌های پیش‌فرض و مزاحم ویندوز مثل Copilot، Edge، OneDrive و سایر نرم‌افزارهای غیرضروری (Bloatware).
2️⃣
حفظ حریم خصوصی:
غیرفعال کردن کامل تله‌متری (ردیابی اطلاعات) ویندوز و برنامه‌های شخص ثالث، و مسدود کردن دسترسی و جمع‌آوری داده‌ها.
3️⃣
بهینه‌سازی فوق‌العاده:
تغییر وضعیت سرویس‌های پس‌زمینه به حالت دستی (Manual) برای آزادسازی منابع سیستم، تنظیم DNS و پاک‌سازی فایل‌های موقت (Temp).
4️⃣
نصب سریع نرم‌افزارها:
امکان نصب گروهی و یک‌کلیکه‌ی تمام برنامه‌های مورد نیازتون با استفاده از ابزار قدرتمند Chocolatey.
⚠️
نکات مهم پیش از اجرا:
* اسکریپت تولیدشده حتماً باید با دسترسی ادمین (Run as Administrator) اجرا بشه.
* چون این ابزار تنظیمات ریشه‌ای سیستم رو تغییر می‌ده، ممکنه آنتی‌ویروس (Windows Defender) بهش گیر بده که این یک هشدار اشتباه (False Positive) است. با توجه به متن‌باز بودن پروژه، خیالتون از بابت امنیت راحت باشه.
⚙️
سازگاری:
ویندوز ۱۰ و ویندوز ۱۱ (کاملاً رایگان - لایسنس GPL-3.0)
🔗
لینک دانلود / گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#WinScript
#Windows
#Windows11
#Optimization
#Debloat
#Privacy
#OpenSource</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/archivetell/6479" target="_blank">📅 12:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsSjzvj7fCgxWibz3cu0cSdhiGxzH3Lvv1A1mn5gd4QSQGihPsyPJ3peEWwYuyzc3y5BfbmCLKa7XWE-ge3pInjKwusuUrMbRiUJCvdq9Ey0wPuBhmiIoVUySLdbSz6Q_DMaG7CdhXNZOfQub5XGrQzfbV-WOBa4B9CNkfOlQAWsdChKeJdJMIxuIQ1m3j0bfo7nFErJIKHGsU0Mo5x0ujZzr2wYhqGQNxqb3KsocKYTpjhIoBPZGRmk6BaY17Tg1JS43Bf_sQMeOiD2duuZcxfyQBDRCx05aPV2-bbZK3PsvSt9D5Tt2bNTdPrbHrxj3FzE6G0NRJlCJm2Tt7avEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
با GeoSpy AI می‌توانید محل احتمالی ثبت یک عکس را از روی جزئیات تصویر پیدا کنید.
•
🔹
تحلیل جزئیات عکس و مقایسه با تصاویر آنلاین
•
📍
ارائه مکان‌های احتمالی همراه با مختصات
•
🎯
مرتب‌سازی نتایج بر اساس احتمال تطابق
•
🏞️
دقت بالاتر در مناظر طبیعی و معماری خاص
🔗
لینک:
Site
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/6478" target="_blank">📅 12:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8o_R3jogyF990u7hvY3uMXuOUdwAmm02XAm7WUbaf7Kx4-KhL3wBCLBdoxff_zPmhz6-AaJEm4UmxYZTrTPp2T06VmTeuEB-fBisaxfTXiCtsMbGbuz6sB2lw1CZzAwBH5U4v2QXd0uP_hsIdZuKJptWzHUGvJZ12S80rT5PhHNiSFPHFc4T4Pe3GlkgkfyPudUWc6ePnJDH14Pfp1TBepU3rJvUzwr3QXfLnurj1j0Gvs1YV0ikT6jcy01pTTktAVm8CJaVpNozji-kjPXUHZvbsQTchAPbD6WxGYSjBH2T9ikRMXKUFhDT_7MUsEJ07obt4moasFUYsnO61vS5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی کاملاً رایگان به مدل‌های هوش مصنوعی با Unlimited AI!
🤖
✨
اگه دنبال یه راه بی‌دردسر و مجانی برای استفاده از مدل‌های هوش مصنوعی هستید، سایت
Unlimited AI
دقیقاً همون چیزیه که نیاز دارید!
🔗
لینک‌های دسترسی سریع:
🌐
وب‌سایت اصلی:
🛠
اسکریپت واسط (Transfer API):
اگه برنامه‌نویس هستید و می‌خواید این سرویس رو به پروژه‌هاتون متصل کنید و ازش خروجی API بگیرید، این ریپازیتوری
گیت‌هاب
کارتون رو راه می‌اندازه
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#FreeAI
#API
#Tools
#Github</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/6477" target="_blank">📅 10:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6476">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=ouuvnu5K3GNIhmUlPtfX8-WHHBXUkmZKvjo_X5ee12x__--nahLPwuNzm7BTu_somHgvOA_WMPk8OcLXvP-7pRfV0xdlf506RgI1AWCKIbDDYPh4AdilYFZlgMhp1eOJgbdEA0L0Sj-FPKdi_T6_0Qci5UzijoLCgNzElTPKXC9zVwt_7o6bXqJ4ox2wuJJSHuMZPlm8WC-eDdG_w6KFqKWHGXFWztqSy2SZy1yHpGLl29fYgmok4YNdJUoIq9LkjnJhv-PUItXsAhCPLX4xFUuxrBBtObU3Jz4QJuWBn8NAnwE_yF4P5RDLTrl6BzYNt1vNrz202_bN_e2luQYyfg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=ouuvnu5K3GNIhmUlPtfX8-WHHBXUkmZKvjo_X5ee12x__--nahLPwuNzm7BTu_somHgvOA_WMPk8OcLXvP-7pRfV0xdlf506RgI1AWCKIbDDYPh4AdilYFZlgMhp1eOJgbdEA0L0Sj-FPKdi_T6_0Qci5UzijoLCgNzElTPKXC9zVwt_7o6bXqJ4ox2wuJJSHuMZPlm8WC-eDdG_w6KFqKWHGXFWztqSy2SZy1yHpGLl29fYgmok4YNdJUoIq9LkjnJhv-PUItXsAhCPLX4xFUuxrBBtObU3Jz4QJuWBn8NAnwE_yF4P5RDLTrl6BzYNt1vNrz202_bN_e2luQYyfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
گوشی‌تان را به کنسول رترو تبدیل کنید؛ صدها بازی کلاسیک مستقیم در مرورگر.
•
🕹
بازی‌های PS1، Game Boy، Sega و پلتفرم‌های نوستالژیک
•
⚡
بدون نصب، حساب کاربری یا اشتراک
•
📱
💻
قابل اجرا روی موبایل و کامپیوتر
•
🎮
پشتیبانی از گیم‌پد
•
🆓
رایگان و آماده اجرا
🔗
لینک:
Site
#Gaming
#Retro
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/6476" target="_blank">📅 09:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rI4jBiWzpPd0_ZynnU1cM4H9ZTpcIhlpEOmKSJrzLrtjEi-k7SfRntHkcIfHzjzLdNd2pAqBReBlWHJW5SrUzS9oRekQV5XSSudc7jR9jQAC0G2MPYsuwHyievDgcgPuACYHyfbcLEtNK-wbIC_GBPNE_NpGTeSZtXTZnu-PL2KDiHuyP4MCMAEQtk0a1NKLTchTS7HkAAbxvTwMf050mJhRWnQ8tL_4az0eAwvtnFTJ2H8sTBX5TMWlKUZv0S_fVks9XY8JTgj2f4bNM8owvxXf3a2sIFd3pupHbdGzRGrpysLg5O4Q_p8y1WrGNI0zWaEIHZ_H880TOEe9xyTPzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی رایگان به API مدل DeepSeek-V4-Flash تا ۲۸ ژوئن!
🤖
✨
یه فرصت بی‌نظیر! می‌تونید مدل جدید و فوق‌سریع DeepSeek رو تا ۲۸ ژوئن (۷ تیر) از طریق API کاملاً رایگان دریافت کنید و بدون پرداخت هیچ هزینه‌ای برای توکن‌ها، پروژه‌هاتون رو باهاش پیش ببرید.
🔥
چه کارهایی می‌تونه انجام بده؟
1️⃣
تولید کد و اتوماسیون:
ایده‌آل برای کدنویسی و سناریوهای عامل‌محور (Agentic).
2️⃣
تحلیل و تسک‌های فنی:
عملکرد عالی در تحلیل داده‌ها، تولید محتوای متنی و حل مسائل تکنیکال.
3️⃣
پروتوتایپینگ سریع:
تست سریع ایده‌ها و ساخت نمونه‌های اولیه بدون هیچ نگرانی بابت هزینه‌های API.
4️⃣
پروژه‌های خلاقانه:
خوراکِ آزمایش و پیاده‌سازی روی ربات‌ها، سرورهای بازی و سایر پروژه‌های خاص و غیرمعمول.
🔗
لینک دریافت رایگان
🔵
@ArchiveTell
| Bachelor
⚡️
#DeepSeek
#API
#AI
#Free
#DeveloperTools
#LLM</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/6475" target="_blank">📅 01:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6FNQ7bPEDhQAgwtpX6_geC_LkBQXmt5H_e0bvOdGMf-9Sa0B-m4NwVcChvPbM3ninZPzCWRk-btpfCG4eNuTx4__EHFcsl6QtrHFD9jH21O9h-4ACOdx_ZJWvIei3rPZHn1H-REt9jLXBY4k2zQVKB8bTM9_SHLUE8bJ0zjMRhCwrChZv46uYDCvt1aOpD5vmjzw3uWPGm58oEMWXCfDs3ryWHjsRGxqCLD6dfvR6TvH9TsWP3TrxVIv7WtLajO6qewG5dINoynZHH3jouYLyYLpaKoRDM1TTntT4ARBclNNf6f51uZGIATlmttZIdJeJ8eVeNxobQKIkghUnVpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دریافت یک ماه اشتراک پلاس رایگان پلتفرم HotGen AI!
🤩
✨
اگه به دنبال استفاده از قوی‌ترین مدل‌های تولید عکس و ویدیوی هوش مصنوعی هستید، الان می‌تونید اکانت پلاس پلتفرم
HotGen
رو به مدت یک ماه کاملاً رایگان دریافت کنید!
🔥
مدل‌های قدرتمندی که براتون باز می‌شن:
>
🔹
Seedance 2.0
>
🔹
Kling 3.0
>
🔹
Google Veo 3.1
>
🔹
WAN
🛠
مراحل دریافت (بدون نیاز به شماره و کارت بانکی):
1️⃣
وارد سایت
https://hotgen.ai
بشید.
2️⃣
خیلی راحت با اکانت گوگل ثبت‌نام کنید.
3️⃣
توی داشبورد کاربری‌تون، بخش
Tasks
رو باز کنید.
4️⃣
هر ۶ تسک ساده رو انجام بدید (ساخت یک عکس، ساخت یک ویدیو، اشتراک‌گذاری و غیره).
تمام! اشتراک پلاس شما به‌صورت خودکار فعال می‌شه.
✅
🎁
با این اشتراک چی می‌گیرید؟
به مدت ۳۰ روز، سقف محدودیت‌های تولید ویدیو و تصویر برای شما به‌شدت افزایش پیدا می‌کنه و می‌تونید از بهترین مدل‌های روز دنیا با بالاترین ظرفیت استفاده کنید.
(البته جمع کردن توکن به این راحتی نیست. زاییده شدم
😂
، الان تست کردم)
🔵
@ArchiveTell
| Bachelor
⚡️
#HotGen
#AI
#Free
#Kling
#GoogleVeo
#VideoGeneration</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/archivetell/6473" target="_blank">📅 00:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚀
معرفی Remnawave؛ پنل مدیریت پروکسی قدرتمند و مدرن مبتنی بر Xray-core!
🌊
✨
اگه دنبال یه ابزار حرفه‌ای برای مدیریت زیرساخت پروکسی می‌گردید،
Remnawave
با تمرکز روی سادگی و راحتی کاربر طراحی شده است. این پنل به شما اجازه می‌ده نودها، کاربران و اشتراک‌ها رو در یک رابط کاربری وب بسیار تمیز و به‌صورت یکپارچه مدیریت کنید.
تمام بخش‌های این پروژه (بک‌اند، فرانت‌اند و نود) کاملاً با TypeScript و با استفاده از فریم‌ورک‌های NestJS و React توسعه داده شده است.
🔥
ویژگی‌های کلیدی و پیشرفته:
1️⃣
معماری ماژولار و بهینه:
دیتابیس، پنل وب و صفحه اشتراک (Sub Page) کاملاً قابل تفکیک هستند. یکی از بهترین قابلیت‌ها اینه که حتی اگه پنل شما آفلاین بشه، نودها بدون مشکل به کارشون ادامه می‌دن!
2️⃣
مدیریت حرفه‌ای کاربران:
تعیین محدودیت ترافیک، فیلترها و قابلیت جذابِ محدود کردن اتصال به دستگاه‌های خاص از طریق شناسه سخت‌افزار (HWID).
3️⃣
مانیتورینگ و امنیت بالا:
مانیتورینگ لحظه‌ای ترافیک کاربران و نودها، پشتیبانی از ورود با اکانت تلگرام (OAuth)، احراز هویت دو مرحله‌ای (2FA) و هماهنگی کامل با Cloudflare Zero Trust.
4️⃣
امکانات ویژه:
تولید انواع فرمت اشتراک (مثل Mihomo و Sing-box)، پشتیبانی از وب‌هوک (Webhook) برای کاربران و نودها و ابزار داخلی برای اعتبارسنجی کانفیگ‌های Xray.
﻿
⚙️
حداقل سیستم مورد نیاز:
برای نصب این سیستم قدرتمند (از طریق داکر)، به
۲ گیگابایت رم
،
۲ هسته پردازنده
و
۲۰ گیگابایت فضای ذخیره‌سازی
نیاز دارید.
🔗
لینک‌های دسترسی سریع:
داکیومنت
گیت‌هاب
داکر هاب
کامیونیتی
🔵
@ArchiveTell
| Bachelor
⚡️
#Remnawave
#Xray
#Proxy
#VPN
#OpenSource
#TypeScript
#Tools</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/archivetell/6472" target="_blank">📅 00:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3ZKUNOk28bP9Yo1Z4t1DWfyZy18Jyy4zUl6bXEKL9KDHDEznQPeQdZmxJH6kFKoZAcAdKZF4E1sLtLQabsyA6INMEp0Jon5aoBBs6wW6kd_pjB3GfHNvDh4-XLKS1jRUybV-YM3NOq7HbikU2oFtPU66yWZER5mh2GUYJARUj7U1adAldTNPkI7Ps0PmSAw8dq8EeO58pmaPhe0360sOECcSRqtcgv3TMvkDtzQwSov0yJAiHM17GwbtgA5bzraJNNB0-Z20HiuRTP2_n_rJZq-YF08dF6xueJpoREKVu2hEvUWvoLWFUOY8k39-Ws4HQ3M6ajmKhHUjs-hKKIa7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
یک کتابخانه رایگان از پرامپت‌های Nano Banana برای ساخت تصویر با
AI Studio
منتشر شده است.
✨
قابلیت‌ها:
•
🔹
پوشش سناریوهای متنوع برای تولید تصویر
•
⚡
قابل استفاده رایگان در AI Studio
•
🗂️
دسته‌بندی منظم و جستجوی سریع
•
🔄
به‌روزرسانی مداوم با پرامپت‌های جدید
🔗
لینک:
Site
#AI
#Prompts
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/6471" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚀
معرفی Ladder؛ عبور از پی‌وال‌ها و خواندن رایگان مقالات پولی با یک کلیک!
🔓
✨
🔥
🔥
🔥
اگه برای خوندن مقالات، اخبار یا کتاب‌های معتبر تو سایت‌های خارجی با درخواست خرید اشتراک و صفحه‌های پرداخت (Paywall) مواجه می‌شید، ابزار
Ladder
این مشکل رو برای همیشه حل کرده! این سرویس با شبیه‌سازی رفتار بات‌های موتور جستجو، بهتون اجازه می‌ده محدودیت‌های هزاران سایت رو دور بزنید.
🔥
ویژگی‌های جذاب و کاربردی:
1️⃣
دسترسی نامحدود:
باز کردن مقالات پولی و ویژه در سایت‌های معتبر علمی و خبری مثل WSJ, NYT, Bloomberg, The Atlantic, Nature, Science, The Lancet و کلی سایت دیگه.
2️⃣
وب‌گردی بدون مزاحم:
حذف خودکار تمامی تبلیغات، بنرهای پاپ‌آپ، ترکرها (ردیاب‌ها) و اسکریپت‌های اضافی، تا یک تجربه مطالعه تمیز و راحت داشته باشید.
3️⃣
نصب و اجرای منعطف:
می‌تونید این ابزار رو روی سرور شخصی خودتون (Self-hosted) یا حتی به‌صورت لوکال روی سیستم (PC) نصب و اجرا کنید.
🔗
لینک دریافت ابزار
🔵
@ArchiveTell
| Bachelor
⚡️
#Ladder
#Paywall
#Bypass
#Articles
#Tools
#OpenSource</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6470" target="_blank">📅 19:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6btOjLkSAaClp00KRUN24BneyW2POwPpz2OLa2GlhozJyu4UKrnN5ruBnxKoeVXOSRoHOMgPQahE-euJHZZp3S6oDbpj8vRdiBUabftGewDxYLyPxmQXfWDccahIZEm9pPWvt-9rogEuKW6rYq5uVSbWp-naZAyV7lSd-yyPOO1mWGXZ9FQO5Q07mtS2tQr9Mav7jsJQ675ozSkf2auQXpUSALmUof-Qo1d-QWyarF5RYPBf-Neb7EUgxmEqjgKFVhYMR6EwtNxtQSd9MTJ2mfG4UffZflFlyg8TV2XdM69BY7S7mAxs2hKodlzC2oMh5lbsEpRW2wQEsbXaikF3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
بازی‌های کلاسیک کنسولی را مستقیم داخل مرورگر اجرا کنید؛ بدون نصب و دردسر.
✨
قابلیت‌ها:
•
🎮
شبیه‌سازی کنسول‌های Nintendo، Atari، Sega و دیگر پلتفرم‌های قدیمی
•
⚡
انتخاب بازی و اجرای سریع از داخل سایت
•
📦
امکان آپلود فایل ROM برای بازی‌های دلخواه
•
☁️
همگام‌سازی ذخیره‌ها با فضای ابری بین دستگاه‌ها
🔗
لینک:
Site
#Gaming
#RetroGames
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/archivetell/6469" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🎬
معرفی OpenMontage؛ استودیوی شخصی و هوشمند شما برای ساخت ویدیو!
🚀
✨
اگه تدوین ویدیو بلد نیستید اما ایده‌های جذابی تو سرتون دارید، ابزار جدید و متن‌باز
OpenMontage
دقیقاً برای شماست! این هوش مصنوعی خفن، فقط با خوندن توضیحات ساده‌ی شما، یک ویدیوی کامل و حرفه‌ای تحویلتون می‌ده.
🔥
ویژگی‌های جذاب و کاربردی:
1️⃣
صفر تا صد اتوماتیک:
از ایده و سناریونویسی گرفته تا پیدا کردن متریال (عکس، ویدیو، موزیک)، صداگذاری و تدوین نهایی رو خودش انجام می‌ده.
2️⃣
الهام‌گیری از یوتیوب:
فقط کافیه لینک یه ویدیوی یوتیوب رو بهش بدید تا سبک، ریتم و حال‌وهوای اون رو تحلیل کنه و یه ویدیوی جدید با همون فرمون براتون بسازه!
3️⃣
اتصال به ابزارهای مختلف:
این سیستم به ده‌ها هوش مصنوعی دیگه (برای تولید عکس، صدا و موسیقی استوک) وصل می‌شه تا باکیفیت‌ترین خروجی رو بهتون بده.
این ابزار کار رو برای تولیدکنندگان محتوا، معلم‌ها و هرکسی که می‌خواد بدون دردسر ویدیو بسازه، به‌شدت راحت کرده!
🔗
لینک ابزار (گیت‌هاب)
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenMontage
#Video
#AI
#ContentCreator
#Tools</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6468" target="_blank">📅 17:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MQEizfMqBaGDQplasWKs20XT5R9b8fhzZk1t60tdwE3WGjRwfBiDEJrbzOJAnHFO81lecwQ4BkUqXIizzwacRLyN42ZH1HfNMSXy4pW9xr1lWsf1y3Vu0OOTIh9TlnQ1aDTNUGpRtCAEU9sgPXIpxEVqIkQ8vJXAiw378qbM_WABtJDcmI0vFObrPXkcYyszPc5YaFB-eSa9NAxkDWOmYI-UykhOhTCTgcLNbujPXGJxSFunjF0v4NWlYhIWZBHPwFHkmJ6wrzS1YJDL4s65HvilSL_E1BbIJaLPpxmME2qGFiY6N6N_eUOfy4sV6546gaEz8rFiRS-FHOXqIAfFAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JGLZWboxaINqPH0rJMHpX59IL37t1jUPVKoE0oAEygPrHy9Wfr-iHD4f0nTu7UO5WXsA1JTUgyrwZ8Fj3gU_9g0Qv_uFrg3HVSQV3Xop57US9NHajj_EIlBrL3NtIRyT9DWUu_Fz_0CTmFmaDbcq9Z15iWjNYLU6JZ_iY4Yj1jNZnOGBPtS6ygXxjXYPwUywY-Sqp_bDy9S6c1CgBEc8xGcCIBGZXuEqkkKSmClULdN7mVIy3p8fZsCanzArwxSF8ntyrqSsCWlQ1tZSHTm9GWnAihwDEb0-shz5xJWifQ4NKHkCbIg41W8FUi91ehELWGFXmjFACIgPfAWm6439iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GqLrBtP6krc27Ccazj0OnolCNjVJ88yUn65Lfx4Bq8RV-v-JAsz2W2XMbpKVzdHP173FrOIxPsoj425lmj-MXpC5r-KP5QX5tVDeuz4FoeOKOB6sYKvIwdvAUKIrTEX4EHD77qHPGxh7j2fsezdODPhV13ZJ-W-hDYpk0oO-Ua7iiKZVg50UwNw_LmPLONnucQtqIIkZ2wSVpWHgoK1TwU-p5YJXyKSN4kOe2rhkpLhboieBXgJ-J5oaglxtYt-g3nxlEdRaBJt9iiPl2rouQwRXsGwW0xdHjY5GrMzCL-Ygve7oFN1zVQVCqPyrUiHqgHR6l73d_DBs5-q-IM2l-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kBHEfkSN0jTILqY0Srwstp729RpK03YsCeyb214g4EzIT1hk7PIbkLYv98Yh9aaBH0hTtBgZW8bDR226tjF-3uK7UMQrZfrE9K47le2oyf4JkXHH_4okGqB58oK9E0AP1_gP3CDzMALL0T55tLaj9s_DrSe65VEbLC38gPluIhVfDsyTwcDxJ6zHhZoy1z9lJyTU50pfnj5fFJr-z263wwa8AZ1OFK1o2ykiZutHgxG1nayqptBbuHl34Uzss47M6TGwm_N0y_JlNIIsHKZE4yxYqJJ0VwZn38Z8h-03cbuFlk9cz1jk55R2mew8ishVHCGP_Rhqn5MTQ2UCG7xTKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Splayer
پخش‌کننده موسیقی متن‌باز با قابلیت دانلود از یوتیوب و اتصال به اسپاتیفای
🎵
✨
قابلیت‌ها:
•
🔹
پخش فایل‌های محلی و مدیریت موسیقی‌ها
•
⚡
دانلود صوت و ویدئو از YouTube
•
🛠️
واردکردن پلی‌لیست‌های Spotify
•
🎧
متن همگام‌شده آهنگ‌ها، پادکست و کتاب صوتی
•
🎚️
اکولایزر پنج‌باند، ویژوالایزر و ویرایشگر صوتی
•
🎨
شخصی‌سازی تم و رابط کاربری
🔗
لینک:
GitHub
#OpenSource
#Music
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/6463" target="_blank">📅 16:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6462" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9ejJU7Y9t-YZTi8pP9U-xYFPhG-S4UKae9ik1l93dupwX1ucgOAbT-f9xWkvAoJhSwqpkPcMJFXMt4WXa5pBe-jWALN85idZ2SbW6eDVbb09HoS7xJ2odX0QND4HRCpPhqTaONsYdFh7M1oO7s9IKPUn11XWr-VVWFzxDdxsvBS_BAxQY-OzF5nHSgnv2oGLSdcZJ7qrlN1kEP_lF382MZd4hesFf3mOV1gzBeXnX0-udjtxzaXavF3-n34tsofwrqFybrXCNDf2SJg1ym6MvIN_3kiz-NTr6uVY3_yyMRdvSyZkiNAnXci68N0InN-4BqRGKGXRT22q-M6uoeaAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRshhmdJgsttPATcKQUkspPpO_G0yQlGy5kSutd6gIEfsK5Jt4yGAyHXL0m1DkdhJjP7adDcqzK0ZHoU5uS7FY6IiItuZ0lOdjO_aVqsH9txAPieg_rI-RmYdP0_GUIbrRyisIsmVh3ZBLiKE4WsqZk2Fd5SFQlVggRJ7v1YVcTS3lRgKYzO7dtyYoEWgopaxgkbDLCTzULvhor876pHLXV4ts4ouchNGN-_xrwKfhA2UMgaYTQr-SZvaLsOKYoCYsizL69e_w89da6OzAPQn3kZ6d7h50zEX5InT4Wpa2WZEBGYrIXKwvtObP4QB2jiH5NblzaNV8cIlUTi6YeW8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vXbSJGC-A-X49cD5d7EDY0zlqWwLiQLO7zPIC-jkMqLpH950lvB2H4fvs_ziv_tMMMWlng6ZTZpIWRK0SxxROryxqkFgT_vKtpl3fRPcXYs207UY9dqDlme3qHbJDpvvplyt8HF6zuAEXzOBmk4KPQrtgjrga5rA62i73GdxRRynEbz1F8e2eTJYaSBmkR0rDiN_cl9Aiygr29c4RluTSIwqo9fVP4S_N9i4IwyL_gacWlNWx-ruJj4W8hWicTsed4zpQDadCJKSbPsq6E1H7hzamp3IC-2iwk68mNd32iiw8WyViJa-itKLJhrBDsEOpDNgkvBzV36ykEh2u74zdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZIDZJVHirWZk-EXgf928pknSnEjWUymNVGpSI9b1liJ8fKBPrpJgk0vMAJUK6WW5R0Mo5mYpZhXVXHfpsUqJEQARpu4JemacArblD_Y43Zwd0uJgg4RBmHolY-otZ1VAyB63qqN2jysRt1I0FinE2Xzoc6sT540GEcj-R6gTWo5N5bndmBlTlCfxkb44aw67Zv8nx0trwXpaMXrSLkVsWUvv5uT9riaYVNb9w-Y2gpclZ8gGEbwaD3PbofmYeJRizveetwNUBFDJPPhSmHgaJEVduZHamd-pht_lNJVzxgNyVnI7iVZTd_7yg-y8IavyJhI2tcDJD-YXPNIbjpFVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ded905356.mp4?token=obcxUA-GOwNY9JClR04BGv_YRlalmPO2-4lwpTWlAfuYn733nM-Lv7c-Gww4p0LMG3ur-gbf5uWTk_hrl7v_SIQgqvsdBGFE1-QL0de5V9i7zfCaHFm03Z5wT5qrgXqitEYN29N6WhIbSYF7wOTPrY1vGKU0IsW5iSIhHLMSGyyydTQJywTg7dvigVSN5MWlCnVIaAXiaNNruR9fPj0anQhKBDCl_wIZnVWPhPoGhLPwndI6qJz2T9-2fkYULfmV1kEJWMUM04_6qUrX6PpK5AuuE2dt_WIcMb5QhMdIs4zF7KRdjCJnfu14czfgF0PWeaIpCiAFCbVDeZorOt_Jxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ded905356.mp4?token=obcxUA-GOwNY9JClR04BGv_YRlalmPO2-4lwpTWlAfuYn733nM-Lv7c-Gww4p0LMG3ur-gbf5uWTk_hrl7v_SIQgqvsdBGFE1-QL0de5V9i7zfCaHFm03Z5wT5qrgXqitEYN29N6WhIbSYF7wOTPrY1vGKU0IsW5iSIhHLMSGyyydTQJywTg7dvigVSN5MWlCnVIaAXiaNNruR9fPj0anQhKBDCl_wIZnVWPhPoGhLPwndI6qJz2T9-2fkYULfmV1kEJWMUM04_6qUrX6PpK5AuuE2dt_WIcMb5QhMdIs4zF7KRdjCJnfu14czfgF0PWeaIpCiAFCbVDeZorOt_Jxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6457" target="_blank">📅 12:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6456" target="_blank">📅 10:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYwV4rYJO4O8LCIkMat9ZOlyUhiCkc2C2DRUPgZ7Nkdu5WjH22vd0Y0YY6hjIieIb7VfXt_OhdY3f3AqeLGK6q4z58p5-hS0YTGf5iUuTElvmgcmS8Mg5XOMyqh9xTiPlpgfEKz4Bz4CK1acMz1qvQMPS53GAZE_Zgg8z_Elj9wLR9VkjyqQDbnr-vYoYhmyhVt2LuRw1MwYGGWSiBxNlLxLxRywZO1-lCCHu4fpvW_lWdwnxFl1HILfCBAO9giMLD_D5eqb6kEkPgUWuCtxpT2Wv82K3CQK9gqU9yaJHbtfzwonaxuihoRtSpjLRu7koP03CcxUL6R0m06vLj3EXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6455" target="_blank">📅 08:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6454" target="_blank">📅 02:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNZwqRZHxby2GNvhe7qX8d9e_m7o2PktKWkm04PbLc7XJmZpHQZblExhpc6vYJB30l646z7qX-OJGygVXOG4ey2pTtKJ4rMLWkD_ccCUye3PpJVNXxp3tiacCZgDWMAYVjXbqMGkIsgA2kvgLMclH6OCky4fp8yR9WiYTMDEdlk8JmeMMk6p-1jxi0auE0vxx-QcE12tO-Nvr8fTRzZRKyVugauvOXTx3feB8Ct9RM02M7BitLZSOB70rok2giv4Mrb3cBJKV0zhFJAWyNz7n9CX7CSh5-NlTD6T8zDdPz79u3hx1s0x5OLjGTfnPc3_B5MGqs45BE6KnCcRW1TTFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7yiMmqwjklo8LSF5ZCC8LHhr58lOtcbMPNlxme4Xa-SFfyOrPglS8FNySciX3yIx3QaLC_le2P8WDp6Loevyck4UQXqi-CHBVCIzSchAyJYX8cnzOxCet_DqOnjpA3c2n6m6qEb1yHSRGQetT6r1U0Pos4X7Juvhx1t919xuShWN-9Da6Ess1vZ3jYT0EOXRcPCo1IoWe2RAEMeBpOK5YDSC2_08qvcuA3NKXohYt4ig6ixzGcMUIRwZ423LuganjBb9VuyClcJfINL8pEsgtMUXR8Rxx5RO7Nb5fnSddLhEHIWYcdVfzN2aPp1yOUJfIGhCDic4z1WILua_dlaCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Product photography on a solid sky-blue background, soft studio lighting, no shadows.Product photography on a solid sky-blue background, soft studio lighting, no shadows.
Two thick, fluffy, plush terry towels are neatly folded and stacked one on top of the other, deep soft folds, thick looped pile texture. Top towel: white with thin blue stripes. Bottom towel: solid cream. [product from uploaded photo] rests nestled inside a deep fold of the white-striped towel, partially sunken into the fluffy fabric. [product from uploaded photo] lies diagonally inside a fold of the cream towel below.
Water droplets cover both products, fresh just-rinsed look. Top-down angle, empty blue space above for text. Photorealistic, high resolution, sharp focus, no text, no logos, no people.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6452" target="_blank">📅 02:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAQteVIhKXSIpmoe3bgiPK07sIOzHmMEN9JcjOz1RbpDCVR4H9QZvnNTaO9XUusayhEgVQGHAZ2xURa4JwgYRfj4RnTEaMhFnzwJTDt15714lctJJa5Aj7DcnRQmNocDmAdV5IIt-iwYy1XrriIR3UN0P5aaDwAlIiKGTi2OKbPkrQmpxgVBNEB_WUCPfhl9Zz_nXteN_pczlC4kKBurTKw-Y89dKnt96Wce0ItUOMuXfxG-K6VnfnlO4Um3xRce4W2qKNPO8S_fdZB-Sf08E05iJXXW_0MYGhm6v5TTCSkQ74jZV_zxE1QZ_xWGlDU2CSh_fGyhrjyZWrbgBk8yEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6451" target="_blank">📅 23:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6450" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6449">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTzjsOM7csQU4XaBelZ0COkjUFi_V3ftm36kMV-_Mqd12l_3XTXMJuvLL8I_RhfdrcIvLVIs5zOxXpNTa6UhdrU_mfKG1JT_8xVJ4iLtjt-5Ls2lODRWH1QoYtoKTA1kmFbq9R2OmwU6c4CVGxu39ZWt3QzWAiUibMhXXwIi2isHc3q2JwaH9ujmLVQ29oshd1d1d1cD2d0ppto1-uwWnjP0RSPLUUGoUVZEnqCp_MXoSxid6I7KQCjPdn6A8W68plbUL33wYkclQje96-TbXxQwr-KchyRRV5mwsFZH17Hi0TnTWTZevRtYU8b4oRYTlTzHv8o1B-v2X81oeaNc2HXtk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTzjsOM7csQU4XaBelZ0COkjUFi_V3ftm36kMV-_Mqd12l_3XTXMJuvLL8I_RhfdrcIvLVIs5zOxXpNTa6UhdrU_mfKG1JT_8xVJ4iLtjt-5Ls2lODRWH1QoYtoKTA1kmFbq9R2OmwU6c4CVGxu39ZWt3QzWAiUibMhXXwIi2isHc3q2JwaH9ujmLVQ29oshd1d1d1cD2d0ppto1-uwWnjP0RSPLUUGoUVZEnqCp_MXoSxid6I7KQCjPdn6A8W68plbUL33wYkclQje96-TbXxQwr-KchyRRV5mwsFZH17Hi0TnTWTZevRtYU8b4oRYTlTzHv8o1B-v2X81oeaNc2HXtk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6449" target="_blank">📅 19:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7JkM51QnNlvLVTxrE-uPz3nKfU9fOur_ZaSpmpd6aW4Sua0MUkbpuDn36j2BBprYTVwHg3f23_iJF8PfZpfp5JrfhboTWEi0dLSwZC8hMqim7VuOKoct89yWR36dbmxIqwEosO9kEvDyupaD-cBvyMpgyCOTeWH3OUuFCy3K-A-DFESyfTlywH97Veue_ToplBOYDbSj_B52GhfhNkfRe3r3SKj1sHOaMWko7Ap7N09Kc8GMO712u9owjAtFIQ7teM9rQxFLqJwRSybRRXckY3K8pzcAaug7L0ap-QfWztINptVGOZJuwPF6T4aP04KoDJu-B4RwX4GcueoryR-fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اگه حوصله داکیومنت خوندن ندارید و یا پروژه‌ای داکیومنت درست حسابی نداره، به جای این‌که سر خودتون رو درد بیارید، یه سر به سایت DeepWiki بزنید و با کمک هوش‌مصنوعی، جواب سوال‌های خودتون در مورد رپوهای گیت‌هاب رو پیدا کنید. اون خودش داکیومنت و کد بیس رو کامل مطالعه می‌کنه و کار شما خیلی راحت‌تر می‌شه.
🔗
deepwiki.com
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6448" target="_blank">📅 18:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_C6wC_1CA7bHMYHACQJ65Gr9sAnFnIGAD26_MEz0EcxLP5sdJq3iG6EPfrH-73qChJuKgF-WQ26g3c0PBwTbdiWCj81_zaricM401I8H05EmW1oBgVS-WSr1ByMiqaIrdQdERJFXE669ml5R1qBZ1V08W6VY2q-YpQVp-d4NjmmddUMwN-U8LhUncRzG2EeeSzEYAA_LXXppsDzIszxa3Kuf3JPGAZ3X8KMsp_nNJibEbPu3ZrpNntzZlHkA9b6GtDDNMV3UjV8MRCxwlK4-gXExuxtGRKbZzUAp0SNamvfthUAgSGCw2a3c-XWdcPuuE-JybrZWuyRNXiRb288yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت موزیک رایگان
🎧
https://freemusiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6447" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6446">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6446" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0w5q7Vly17ByngkHFkxC9SVHCIrr_oTlKTD_v8QqwKBkSJ5I-p28sYeXd6-l0ifKRmMxkV-LPbwnqSGb98KeEnMc0bxFfs4EHHypNT4oW1wct2Tx8lMeu8KowKDSPe83QfX7LF3XNhddDpgqgC90t2fCqq5oU5J5vPKw1VomZcX3N3fonRuJ6zY97B3RQHPHCZv8gbQvxGOuXMn99VmfM-JFTH8TNlZxAVniBmwi7_G0nm5j_0l9glwF5zNBr0Hkkz9kQMrSGn5AAntOLhDQV2a36gouRFn80clfpYKNNKtLzO3K46LQe8XA4He-WwjwEYnMt4QoDkWrMk8cjsRzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
۶۷ کلید ترکیبی پرکاربرد در لپ تاپ و کامپیوتر
⌨️
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6445" target="_blank">📅 01:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6444" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttnpGBFmrIa0nFGwnwfasrOx-mxwmrjgJPrqLDEll14kDnZ293vnB3T6jq_dDZjEd_iy377TinsXS3Wsp526_gIvNGk7oSC4Zwl75bu1U-NhyO-H7YVtCFHMRvn9Hs9sqUhvM-2pY7Fs3gv-fhaUmS4pGEztdd6k0m3vLEKwTgJ0AsRUhT82C-u6b2YujZCYEdgCCtBX88ydie7UbNoW5Od64A2fwnNyCl6lwjmJ_JAvEK1wc1iMmOPePoEyuccGWM3X9heXjfVLOs3Ex-XHOpSZewu93UDVkSMECnYigGwFINbuRG_cMX7bbcnXLeSp52KNusEoN9m51jjg4oiuvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6441" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6440" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C15StUe6D3ETcGJx09d0NbSKfo9JipQH9qfMmIeXJqonWpZ9ceDpAScdAySaNkLqUUqwdVxd9kZG7Wu38Fc27j9UuoLhemtJqc3FY7Kk1Ts03Av-hEoBcmWJ3sr_9DrKaQF3LZjAZfVRkR4VJTHH-tURmqoX-ykV0FyYjuqmo0RwePqYGRfKIdXHpuW-_7w5Z7Kr9poe0xCqqCwtyQG1ZosQk3EHqVyKU4zHkSkeVoidJ2Cw-rtWFmhyk9jt2Cekd9TRc8R-9CTjQvGEF_HNCFe8aWFG_QFNPlPP2pIV1fPayehn_NZ1xgyyI9hJ0_XzHEAJ1HJrG8cWvLzSMka2Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6438">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6438" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2LSs7cI8-NY1DM5YGRJ7rt1z1ypzKOk0sBFWIdPdb2aCJX8jbL_N5265z1n3x-tjBlOHZBwrad6Xtwe3RpeEa47NTZ5WUFrmbbIWDHUEFXyW3s3xGVF5BD04_dJrj7HBivfJfX823T9NuJ9QRXsKyt5LRRA1YgUe4LFTlr6Dkk5Cfb-ZWGW58cPqiu2ToglSLqLjbApYHdusiEieMWDiThkWZEPE2q1NLwHxWJ47sdSW-lYbEqIWJQFkUu_lLFLDxnweBpPIv_e0fesdCj3b8Wdp5rmo4SpoAzhrTA84G3FRSwZ9s8NATACTgmK3ZxBdL9gpF08i5sXeM-LmoYz5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6437" target="_blank">📅 15:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6436" target="_blank">📅 11:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2qJx7A9b6MNMEd_Jpyf8tlPKgG5YwG_1nhNV9zgQ-F6DTLhh0U49liD4n8L8nhFO5h2SHBQwKoJSsAUYPJin8gC4L16sv7PLpPo8r4NNjbto7FjlnTRFCWwqJct2DGsj2VMQ4sCGVa7wogQeiBZ7BE5SizLXF_H7ryzpfV5Ya3OMFKIxnERndvsPRFIhfXEoEIWJNvKwo1pqtjWornFZVvTVxP5xLVY6qfD8iI5yKpcBu0Br0eRholT2wwtWYzr1FIRERNky7czwBKFveh5NkS9Ak4ZYe54YEmJBEGxCacA1Ffbfuf7lq_VQn7n50KuQKxlo48UxeQKen_8FToj0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6435" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=D1oyCDp4MMuUoG0kbmFSSkFx54TSUzskxH3256pB0PUPJEXOKhUqHynPobSbZKYaYr5IX1FA3MCQPMRFDZmIYL-0kWXBhaf_hdtaVQiLD-5YS5Pci4Vv_CEiIJ2o4HARkU5TWueIT1pVFAFpcK0VlaPVBQqPwNmDERvwxiIHrUffCEYTwW6vUHkyxkZtwcAmUr8mtPlNjzwhSFjtnTRl2x68NG5VzKxYxFhX0VCQZsiXtIJwVwJF9EM3oC4Yt0Wf83_H1o6pXvPLDNndidN0LXSsYeyF2F-iHQA1iG88h9EEiZmnEqJtUeEib3oQRW5R3dWZO03K_jQkWc_rX_Mlqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=D1oyCDp4MMuUoG0kbmFSSkFx54TSUzskxH3256pB0PUPJEXOKhUqHynPobSbZKYaYr5IX1FA3MCQPMRFDZmIYL-0kWXBhaf_hdtaVQiLD-5YS5Pci4Vv_CEiIJ2o4HARkU5TWueIT1pVFAFpcK0VlaPVBQqPwNmDERvwxiIHrUffCEYTwW6vUHkyxkZtwcAmUr8mtPlNjzwhSFjtnTRl2x68NG5VzKxYxFhX0VCQZsiXtIJwVwJF9EM3oC4Yt0Wf83_H1o6pXvPLDNndidN0LXSsYeyF2F-iHQA1iG88h9EEiZmnEqJtUeEib3oQRW5R3dWZO03K_jQkWc_rX_Mlqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6434" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6429">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g58tH_nrORE5f52b5w0-FRqV_3ouLYZlB9DuuUjOFyCcoO3M25WnO8hDE86GJoGFCmF1OXz3utdxZK5DJ-bd3XJYcJVaIDVldLwvyXd5bdnO97fEo79oJK669HfRfcL23z8c2GBW4THBG-9QX0C9LJns3wmqeSXVgRqR96S6RkJbFa0q5qEjkZjtHaCgCfPTsPoeBCIoUepqS9r1V7jt8sJJ1YyqhRS7YhNBpHqoSCpT3kBGkEE2jfdIHF8Ysgj50CwcT_jCRQ-DRRvILne2_iJA-JIbsA4rT7M0TnKkBGlfeTaV5Klq5165gzQI8M54NWLgJXIZqIzEEJ-n8NVZ_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTY_K3zSgvbPHlw3ix3Pg_0HY27t586DkwVl7T6fvA-ydpogRi984nRoBhBv3pgUzX_D1BhKj2lau0C0__L1dfBD8lturzcNCkacf2xkb9aYNOCBUFT-hz-HNsfcedqk3z5Afu6GX4yJxuIg0byIju7HTtPSi7ypdeM2O6m6RdZSC_TK9oOky6XdHuUzuyEplMyGZHBeQKCxH_DmYT4HRqL8Lo_sq4X46iXjB_mvfJiCV-hrZTwgtngL_Tg0CNhcQj9ReyCUoLHBIzh8U2CsHE4ucDN8b1jaCXpH7bgyeg9VueJOlv8dtLqgfRhPke0xVGjZwiAWq-7qDWXbkrETnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mecw-SEo6AXNOMKwk78AzVJoxO289qeCpD_zUT3Rwxh4joolBeDrE7BXQ9slTmfHJ8w7DFufvCMfiiN9dwjJLTCO8yQLwMqJlePpOK-LsA9HUxsk3ISZd2fS4eLDNh-SepOL8q4WnlApTbsE_vv-cvAcMP2bw2Vl9433z-h026BMh010c0LNzJe4AsYd7F8-f0ztwjiKlgtKpERaWong93iNNAkgAkYqaAV_4oYzTmk7KSJoCZXkNANPATfQsNA9jxrC4ms5YJr4MVf9Da83JjsQPpOhBKyHVcIrrxE7seWXquYITB2I9WH0NR1QvowvG6dWXMhboBnu1GzS0e6PXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tdh3ZHz-3g_vBvNk6Ybyc78ETumkR_H4nQ7W8hIA-BQtRVGHnFyvEouR_KxXn6_M6QCSM9VgMp87dl6DXu6iW6qVITmDHQ63K2J64cQqD1lm-P4ZA7ICd-c9haxtnsnbJdJeARPVxAQSjB2mRB4Y85i4sQNsIoFIpMNIa51mHJBUsCNLUmiKN1joevc9kZLNrI2g0GSujQJtvEauakP_RaJ7ljlgMzTwH1RNiNbeXfv_BDi9PBUpxzDFutjcAKkQtI4zokXOdDZekp4qwuCPuP28yM0Gao8wMpQpcSnXSmQN8mRjCk6UomekKP5I9-mKYOhnMq9BuJ3MJPKrLFyZhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت api رایگان- GPT5.5
لینک 10 دلاری
ثبت نام بدون لینک، اعتبار نمیده و با صفر شروع میشه
وریفای کردن هم با تلگرام انجام بدین که تایید بشه براتون
با شماره مجازی نمیشه(چین)
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYDxDs-ZCBBOW-hP6jZsrfDiaTjZoAgibT_1Zu5OadmckLsnK6y_KY5w1ZuN2vHnU2MH1IH38Btgk4Eg4XYMSzuKd8Z8dwkYS5wGwZAzTAvc64mtREbmddY03Jw4dueokhYmI50xhr0q3WJNPQrQNq70sWUe2INGipFnQm9nWCxC_6fBVt7Uszx-h_dcsTOzBc7RotWXYplqZUyBxdXtvvHBiqVioKbwvPpCkxK6oLngsqCHLN2aKYyvsJupmHycJ_wXYCnrJebZ0o9eMwyqUsJGK7eQgMpxhiVZlmFs95PZ07hkC3mWPyCKIFhAttB73M_hK9_cDjmwVbjGaPIzgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WRWIMYpPh-NFJfyjyEkmii4E-jQSBaUi8YXsiTxd4S4Gxfhlb5u3b1LK31Jxjdo9e7DoRySTfG6KYG73lnbRJFqBoHXXGYroJSngXPhPVhPNjFYW8l9FdTs3lnK07rjGYZfLyef5peLC3rWJ0I3Ly1IpXiGuS02YnETTVYMy5l4BvqlqG0eGMlSmnjRg93M1DPLzZPClWDbcg_odG_jGgU97WLV4m8_rOgvnP5EakVfEVmfTWacWu00NIBYstXaLIdbjFVWD75ULV8QKukPJJABLVM0EJA4IjfGY5spyVylQtvxlnVbSSJt3Js26mu3bqiBtgpybUhtHzA7IJ6Yaew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XaUibAB_kFvp86rZTr0UPa-dO63-Oa46AQgzRv-kudWpQp1wRd1_DtQFjh6jxUtiBAnhD_o39JWITjzw_PJW4rs9QthOuhoL8FyEh29edDUdnlvSgqcxEjh-LQj1UFCU3ykkl_L559M85LnT8LpVyU9Gy2ilAJhdTW4aymTDmUkZ3X-H6TaY2VytHRaLboglvYNJrvRTOXPAkYkbQwds2QLDjobizyayMqbPqcX8NSBaOqHXpiPgU3KqaQRlQ5OMceImFsqRNrvHIF8eGSBzmRIrtZc9ejuG2gMjHTXQ6nu6VcFkJO6tm0mLQNb7-AtrOIkE0xAa6ruJ_bAqhdkxYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TqfrE4sssPCqAgEXylsAJElLNA7ECFOzgVwxt88c7zhTzJQlObTKXHgd7buv1PCVDTp6BkuGQhks6b-DlowaplU9rP5ehYwAPV5p3gtAKCAVrC10GCGYWh4tgKGXPMfFYhozgojebDsp6Cx0MUN4qwpTYpKtH0S7VnXgJYSX-9_6EusV9eHI7uYQ0oUYmfTMJcvwy0-TcvwLhzf4j65sh7bnsmGoVvTBt4FU06TdBEVSuaCpCBeoEt-LMCyG1zb9V-FAqMROU83nSULl2FLIpOEWXFsD-l5IINOoeidYBe9mJ_9AbBauATb7JX8s-PfiPxpcN06GWafNIWIrPY3oWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل جدید GLM 5.2 از چین معرفی شد  توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ii2Q9ulXWQeMXO3bF6VEUNPHmwWPZ8kNHXJpJVlEAYglNzHaFqF5_YaNljm6wBR74TIjeo59SBJQIM6whA1gQt4Pg6NCOmb203Iqsjy6gVMYjPhDxyeJgNQ9pXLgEKD3EH-Ll0A5N-X5XEVN-jZ94pjsIW9HPdL2-zNhlGUBdUstwiSFwhgHn1Ilm4BKMZUd8FPU5UcljAsC54pYTPlQaseGqu0PGD_IUn-RNOHvSpyFuKi3TCM1VgQOuqp06fTHfS6CeFdhevX7_LFv1oeCj6wYHVBuQ0FHQVyuVVPOjUOecvusMwgwwsjBvZOY02lzO9jmyICr-xC-RgcLFF9zow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l2vEx-CJTmCG3LwE2_LnnUbf6peSc15lIljnd5wWfJTR4G-XvKj8hDbFQhGhtlVL8mH3YKAjFMWy77c_DmfoDOWq2BLPqZda4MZjjMv1u5HhIKJlpblSBMOBBbwXUoztIl97tPK21dAUZUyR-IEuot6IFVzMCFd-w1_WpXvBRrAt33OTs3M3LqAXQxM3VyrqnyvrH9k-OnLA6m_EnVznY-3ZQgWtpX4cJp2murAfMbR_YjzWgk8aZq8Ilte0edYu2x7MQxC9BPe0NucagzhliC8EkMYZ2cZsRrMIY4WabEOsUfrwpYrMBPD2Hs1JeeYJwF5o8MELeVOOqgJs5EiIKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntx7s45Gac_s-ZXJZ7XZuY_xvGi8ZqpwWQKbFEauHL4XLE01eCRktuAm7Z-Y5OkrjzTDIJG7sn1838KDptQR2QagQD7dBw2shRnJZo1JB06RreGk5RbKNsEqNZnfAjt-WPIUnNgyT3wRgi_fcwsFl4LwpZcWTZ6nofc6oZRmcCz4w2sf0puzr1SDhfABMoBddy8ssT_2Wbk-XDtyC3HEfBTUL5ooWDY54AWUsVet8Ob_y8O8SJEIVWGqnoZN-CJM5vQSzg63RaSEUul2Ch0SmBAHM0p3VN1kU9yBNGfEWHIt3CZJN6rLHS1w-r6eK4M5zDkbjl2JWqns2d0VBtt73Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ho_gORUDM64KqVroLes3eSm1Nz-_-qtkADGYyFXoNYwh7neHH7Q_EwtAnRPYpXeSdtpCipvrpZ9o9hjvJWIDj9TIaJt8cla0xIQUUbDFxGGRb46ePsxKHpuz1UyQfGWcFVC0jIXBGUOrocvw3RE9IfJh-imTh5ZX4YVpG9xMaXXll2h_6j8FSK57z-jIP6MPYW0qi61P1eQhcVyUj7JQUqe9abH2WGd9CPozKY_aYrSZ5JyP9r5uGzaX_qptzyw5De2pV3anriZD2wyCR_oFh14cfJW5V0xg6BLZ7zumwGd3ks24Gwr-kqMrKwZej46GuYf7PXC9e8qg-gLRyAObxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VpZFmhBy2X_HqEeNfycqU2UIkhAAsxQ99TtpdRLNc0FwVVsSpGsOE1Vj9x5cixfOhl-vYVczb3WrFOtRVevWAPKn3PBJDiPMo0n0VTXUrWK-k3FQPMZM9kKnRZ4KhVwGeb42_oJVV4DrqyNB_PsX4aS_BKCQYzRnXsvSsNG16qW9cXN9mm4NmSTOoIUbQK1CVpdDfLBERZTHU919lSK36UrAGNm3MH1tRdg1mT2YhW87c2GbWdYvKiVkS4WdyphRo3wjmzB7qmNeE_T14N8I0gNi8cz2CNcXw7E4ZgSXkaEgil1p6jIa52hC3D78YjYzab_JjtMwOEr-l-8FasjTJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQT1GTx32YhkwWf6jXgPy3vvyVsIHL0VKX-y0K-mHOK9ln4ZCu65pvSczv94p1WO0PHv8H3XgXJmBOw2k0NheWPtesJ1pbRk3H1vJgZEjwiIojBDvSrcC15XEw5VvMFe6nvSe2pJEP6bGeyYv68Yvl4HWG7Kzc0g0RD7IllOz1gubJo32nkespjWmV6w10aGDI-HOVG3Q9BpA3Fd-bt-LQUW6wGFqvoxy2P5s0QZU9glXT523BWC9TXG5AwFc1u_Yebc52tY3KIrcCTffTa5zg6d4RmAxnYpfCI196u2U5OLEqdT1w0p53zJ5Je6g57EqaPF8OnhLZfHej7TxbiQbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=qRTHsGY_RlV-IDmDtSejk6FTgA0ord0zLfncbHPqZfULYq18B19ujb9PwKcRrl2QLfvWZNsE1RzcoRPTN5OID5MlTrnF0a_LFNlmZkppPeB_A35gHUxIYH_EnFg4Je6CPjyHnIcNVCEW617iFdbif9vpTdRuQgxKeofO6sydvwK-O42A6722juSRhgGRkyUfNOuYQ75M_IpKWgZN6gh9LGX4a7mSFN8AEHOFctIU9qOdKSgqQbiLIluYkj1JwJirW8DoJrY8TpDDk2xsO47oP4xzdwY511QpL1x20ajf7romh5xD2wnO8Qbe9FRAzcvqnc3QdSnOF2EkjMsXXgjbKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=qRTHsGY_RlV-IDmDtSejk6FTgA0ord0zLfncbHPqZfULYq18B19ujb9PwKcRrl2QLfvWZNsE1RzcoRPTN5OID5MlTrnF0a_LFNlmZkppPeB_A35gHUxIYH_EnFg4Je6CPjyHnIcNVCEW617iFdbif9vpTdRuQgxKeofO6sydvwK-O42A6722juSRhgGRkyUfNOuYQ75M_IpKWgZN6gh9LGX4a7mSFN8AEHOFctIU9qOdKSgqQbiLIluYkj1JwJirW8DoJrY8TpDDk2xsO47oP4xzdwY511QpL1x20ajf7romh5xD2wnO8Qbe9FRAzcvqnc3QdSnOF2EkjMsXXgjbKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPfjjTGCVWTbxUjLMSI7oSBz4IRRh7ajS6N8IZ1cZXTG3K00fG6TO16-Tj7J8fVAQH3pLXXMrCFdfipGp_1C7N-7zzyG82UbOWLGR-lGMkGB6UmMo8Vkll4GgHxBhood-7CVdJLY6ug-j_-Ws0cDW-iyrlZBeOiCjntYE1n9ZcLAj60CdQ9JSKGYq4vv6n-58pWR0X6OHyb6Ex1cV9lmHo1HvAL8W2ykszBycTP162tTFVkaTVxBptKKBpobEgs8XjAKszGB-vFe3O8N5btM7BHIKwBo20MoCSCDVvaA3AX2JY6SaZMLMKCxL3gjjK3QbDZPL8Alq6sGhSleSVWHPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=MMf46r6mOhXDEBy_yC4H7rEm8af0SfjJbtg3H6jyJTM8ivlLHlFxjQqzoy60N_sk1Ab4UNkOt5LtFfYgHa_aif-U87Cxi7b2x0inn6Ceamvge508QL09su6Wb5deLdfq7HsEX15iX2hEtYKFFsQxLte-n__SP0a6-UVT0jn-jcAqIic2AZUGG0zykWNKfVkrw5bSEKeBJgFb-m_7V1pQRO_mxQxzqLyfLHZQutcFygQqYhTdivv6eGwDb0qMKVk25bnPERhlVqyamO6JlkQDWxgiYSJ8RCWoaErejYYfGNQrjba1GoE5jWv764JMwA8qkl-xR0NPpGdKcpCbdE3iQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=MMf46r6mOhXDEBy_yC4H7rEm8af0SfjJbtg3H6jyJTM8ivlLHlFxjQqzoy60N_sk1Ab4UNkOt5LtFfYgHa_aif-U87Cxi7b2x0inn6Ceamvge508QL09su6Wb5deLdfq7HsEX15iX2hEtYKFFsQxLte-n__SP0a6-UVT0jn-jcAqIic2AZUGG0zykWNKfVkrw5bSEKeBJgFb-m_7V1pQRO_mxQxzqLyfLHZQutcFygQqYhTdivv6eGwDb0qMKVk25bnPERhlVqyamO6JlkQDWxgiYSJ8RCWoaErejYYfGNQrjba1GoE5jWv764JMwA8qkl-xR0NPpGdKcpCbdE3iQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIezyYr8rGAKdBqTeRrKHXasDr7SzrIMRSXz1ubOaDajgoNvfXHsUlGB-tJpYq-pMo4F-GzmAucsDKBVAzFPeFf2Ek4C7OnDIGVhKBF1iMyXSGStbI8rS36Jw-3GL7ruv9Rtj381gWo-GqU3TykeRG4CMUY81n6f28FK4kjU_cx5vMRFs_TQ8JAgl2HGBRu4TPMmVuiLFoQiEfYs_OG0hLx0slOq9a8-KOXGoxfSxo1LuohuT3J_aEdC5uGIENqdsLpwmGeDC4De37hckOe_BEOtAVQ-ryUr3cwQTn_CX1GyZ5FcMt2pm0bcNGEc7QhQnKJkClQd0Q3OWjh5S4TRog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LIVWSSt1x-AN1m0lNFvczufqwp-bff69RP7T1AJp4q8lMZygeuT05y1ZG42QhdHbZzikD9ZHRm0L7mhRPlCSGhnwBlWsQu-G47pVJDD2VrMWB7Nvn9pde7PXJsnlc0NS_PLiNztBv89DzAGINaZdYC26gCKYCcs3fMO1UamKuRzyysjcfZaB7XaktQSHMX0Uevrhi6jt0C1973g8ItVi5ryZZMyG-nPrtbYm5qkK1SlXIpQBL8aiUh7ItmPQDqnWxAxM62PrwjLb3KOxzKGxMznDin6MBEovfWqGxRt41Zl2h0Fzk9strGhi4z3BTFLswmUskfJ7sGTYItmQL1I2zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pv1L4xORbH2hVGSJgighCmat9ozo62WETLOE6uv2PTjQc0rsGxSr1ESrRmTWADKrn-DoU13d40ejrsQNK1JVqSbBoIsv-UhBEyZLOeapW1hK8rR7EBFFxUpziPukObYFkCdNc7XkRFazPJZqfSz07bykt_5yUwvJPNlXkfi-RYCUWDUxeWbWDx6WSSggSE35TBJ8FbHxJhqLJufzvZldO-5oFAaxC-7riZSZ1s0Agt1JUkS3fj2POyv4Ph_zMBu-gGCBuIOOuba9edUXFljV4VIJ8DS5mpOLFMvPyYYn1yZvKsKy-zO-XZIz7wb-X-eW2SCpfMPuWk45sS8QwGs4KQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjtMAxzRxiz6dTNPuFaZr__iucUZzcA3dy8F7aJ4TBFojpPJo4l6GZLF79OMl1z1d-5KYM3nWUY6q0tJrc-FD8Y62GnIbBy0q22zBmx9yYmHXQfnfjVM_p6VkjITBHG5LsqpMGE4TBHwKHn3KaxFcNuFzKcgwH8qm5qLROmln6ccsKYwT2TzMqZAnIu265cqqTG_gmVKvlv-tcujx_igY3ip4nIcwF3325lGTrQO5F-2JH0iFVkfJseayPzAFBMsGaxU0K82SYCjFlJRRUmJdMJU7fpK0RX_7oIl2ZlY8lrBvADljdgyg8WvjWywhM4U65-dYLVn8PKgaF8oCPe7ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikeSZ4GFiHD8Ma4PU6KbGlTbsPbfCLWXUO8gzmfv0LuV0gkYjqVR9B8YsTvWmlbzQi-BwjtOKFUPf_TOI5s-QqwBRRxtreRnNWFDELxtM7Yg8_rwg9gRHPdubAnIvSYLhJZYHY0ehj3uTaSz_T3SmhjDJNdm1Du35J1JWgxyfkO9ywp_2DpYSvznpF0GJgYq3LRU-B1jZfQpONuubNq59XwjNcwcURN10OQvsgG_p8tMQp7h4TrD3rjnWlXs_Jq-Fd0-Hx8KYAIxA_JOBbPu9Y-wqvk3ayGQi3V_TldCCwUbbbacVgeqsLFwnWdJy1utaSwn8g0lKPt9Pti4mcwjAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iz5VF6JGrqzvfLWnveuRvdIEnzi7UPnhrXRoUMlPpIxgOYf-P5Z9MNgR-GSoX2W-nHQ39kR-lLS7EBU5sTMTtBb3z_IeeDMXJaHVzdgSPNN8DBJtbHTmwobB30C5HUTsAdwlT5xgNdJA0ipn5d1Qi4N47EbiNcyKwOsEkLPIz2XIsFhZD_t44bD44uc-GhzzqYHZkq-jvTAsQm39KL0zYDMsIYzurOyEoWJJcD2qjWdIV0pWAJLLGuq1NSfCzuoDhL6rgF8V7sTPA83-LAgYZkTmXnLusBXaMG3dzFjm3XxzXUDW-uXJMRmGxMwBS3kxNnmSAGZnwlCk3z4_tP0ajQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0BXhTiIofxIMyg6g63wBbxn4etfFhouyRAXjjih8oNzf43BwUHt7dvAJDRjyF-DaOTigUZMOeScPvCiq291iLJx2pd8jhlDREQbqTj0bN1CeutQshVXMAc8X7rv9sYSu38WWSSzykIAanicdLGXF9rDNAgPLueseAIa8TPj6gXQh0xr7qQ5cAqIJvzFU7DLD8w5QeTWo35l4JdGVr-her9s_0oKF2U8OKvkXyS4p-C56mEg4Pv5C9Gub4faZbd29Yj_N5Pf_rrE7q5CyDEn_Ay8UbpxcKV5U7jr-6Ft7vTiv1rZwgzRPJaXqp9Ez7PZn90vI6o9z1_TTosrj7gc7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEqtnnWlaMVReRaHc35AmpMgtbApOm1oChLk2wYT5CpMC_dTWdOCCCOj7yyY3eVdATEWLl0LEO7BmaPMUWZYco0_GroN1-4hSfza8jYK6WVPE9kZAG0OVMrNTQlAjnYKwhuQ5Eo3vfboRHFRUwVaTA56gVsnXjIzWk6-4f9yz6XkcQO5d5bTlZSaVpf3jHH5eoCTJefN34-vvaURHVdkuCC4CdyeRbDpFVGiQRBClhHwAEspdVSq4JKZBlKrfHat6C3nAeIil3LOV8DPuYP1Q0Z_bH-94zpjUPxUdBuZ62S9x6L0_izDhMm-wJYthQ7tAqGZjkXEEr8HOo3I4NF74Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_Cdy6vTZsWeBfVtawr_gQHJQ-2K7nlRN_xyrOMdf3m_tQgocUH8ZWeoNMdeCHOwMw9ou_vREmbpiVL3Wi7_feZJkjPk5EfkAdZl_uYhlBEndUCQeH0-FJsgeydewp2BTDOrByMTcNELnnOT3mqQEmJI5_YXhTtX2UVmQLZwsA0td3ptd4VbEvr88nJ_iUYtfL-DCiKzY4Tmd4oLFsA_4k3N63EJT9Q4wJ_AUF8-gsVB5IIhf2lpbcljJzb4DP7BGGFYe_QqoGfWtBBSQPmHavXOlsrwAjOeWv4AabmHaMBD1cj-0v9hnhXKfS0FyuwF7CeqXKcfJXrpS4KQkx-E1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjGUFAz47sOIb8S-x7EWXtM7ojbeGszH-TieK2jqBG5DE19pzJbEV6T5OzKz06mFSJIN7-hLaO5AodOGEWXEHR_ECBKAgBrmqwg8rcwFwoq6bJAx17dZ6925tWRBO7NXVol7oJjIGV00wZurlfmwi_WXMKFE_jMmaIW5a2T1wEuDw1H2dMwT82ldvywy6zHccB1QIRW5_F0MSQSFRc2bL60-E3BrjVlPXvuUXBzGiPdH2LWngDBZ8yKvksZrTa0d6wO_eW2eQ-6qnoQKCk6wbzPKuICy0Ycg3VHzYIDPm2OHtcpsD5v1ogzruVXJVxpqL385YVPFDX6eff9v8wZqhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4l_W3BbD3n4WNHewvU-knZghuZkxqOguL_IJpWkfra7yHulFqgmjIUf1SPBioq5XG4yUIN61faCWO-VfDFhrOJdZWUf9UaXcPvesNmnEbuuZek333vw5sTFwkj6AuzEmUjaJWwuc8FMTYxoYMXnolxsaRbpGlDfWgw_3ZthMotHEjrLxe7putbG5FC4oEZ3C-DdIXaFAbQ8KCKMBmYITfBy5_teDlBSfjGreVveik5uLQ__iO6ROKNTdn08HidU7Q_6Z30O0TIljEDIJoev_5vTo2WJrjc9BmNzBzhLKdpKFFGlfAEIevZLgiekD2VgMjG1QcZWZAVwyY8JHfUNdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=ri05aK3CWt8CznS-_rgstrxXL8r8mvKz4sGWWKlN7Oi-9SUPLsy9uK33J1v_q5eaaStHmhNeoSqxIg0V1cKI3tTvkBI1XS4ZTW8PvKF6RVYrna6jSaXsHATdR1ESbwyQNkyicrJiY6ubLN44yLpy8VSu6gs-7iOQS4tDhtLgdZ9O704j5zQr7GxpFFf2pRq_E0vZBAbZl70AHku8cK3AhIu8X4ZI_wiFWuZ0rY-aOHGhpnKubzVZnLMbHo6GT1h8gnXMruyLgQLpykartPe6u6TcbMk1U-AKmKvAWTw-TnVX7ZmogWWP_znuYBIjmbkpYHTha5Oj3F0PbqPdtEPrMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=ri05aK3CWt8CznS-_rgstrxXL8r8mvKz4sGWWKlN7Oi-9SUPLsy9uK33J1v_q5eaaStHmhNeoSqxIg0V1cKI3tTvkBI1XS4ZTW8PvKF6RVYrna6jSaXsHATdR1ESbwyQNkyicrJiY6ubLN44yLpy8VSu6gs-7iOQS4tDhtLgdZ9O704j5zQr7GxpFFf2pRq_E0vZBAbZl70AHku8cK3AhIu8X4ZI_wiFWuZ0rY-aOHGhpnKubzVZnLMbHo6GT1h8gnXMruyLgQLpykartPe6u6TcbMk1U-AKmKvAWTw-TnVX7ZmogWWP_znuYBIjmbkpYHTha5Oj3F0PbqPdtEPrMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGH52LFWFGXBAaz4mke7tEWzH3I2vbdNtLrAWX-CKURJrDEI5cuyQ54eiYcGdKtP-6ReN6BBThxilHhH9APVgpmJrVHaokkZwAJzsdhGFiarygNccAgYmihvgdY-b3y1w2gBdJOZWepXOPQGLhiVERjOxr_axsMbeU-cjAKbljxb96BwPVjPRduZhGnPosmNbjJQ4oZ4eMurFWJcB0MMqxkg9Nvhd3BhLhDKgKhfyvXdNGWX1wHqe25_xHDCos7g2f_wfDRhnpw4U5rQ2RknxACsfGx3fNFWEkJL0GBeTHYwWls2cg3u_WDo1qOFMzFz1Bvw2-FVgQQcjNi94NFyJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
