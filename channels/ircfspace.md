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
<img src="https://cdn1.telesco.pe/file/ecP2-hkC20MWMg61TcqJ6R0DMYdlABlpKVxK0Akc2bK1Xxtl4zLj3wbss0dNAeZ6gcbRQnbxK1HsKz6QT0HcnvAufivGyOGe4LR6nU5Cf1rQdoO6qharfvXw6XWzjjsWPY-L5xvAWzHCZuAp2IDWJe8b863K5rYjBuDhepuRKzq5_lthUgw_6yMEzazoM3oOAALLMBGQSMWkBX1q3UV1yuTKJQ5AKGEMWsORewj1kFdE6X_Kl27CLArvk5vTjAbWXQqEHRvoeGw0gwM4aI1GHejqOa5zRPQ5Nlvw1YczsmnA_4VAbxDoMBlDVVJ7J7LEQEU_8KtHSxzOzzi3SOjhXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.2K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 20:16:10</div>
<hr>

<div class="tg-post" id="msg-2359">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">امروز هشتاد و یکمین روزیه که اینترنت ایران بصورت سراسری قطع شده، ولی پروپاگاندای حکومت بدون لگ داره کار می‌کنه.
امروز هشتاد و یکمین روزیه که جمهوری اسلامی داره
#روز_ارتباطات
رو با قطع اینترنت جشن می‌گیره!
🔍
ircf.space
@ircfspace</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/ircfspace/2359" target="_blank">📅 08:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2358">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wp0jMgpNfdoW84zSpMjEd3uIR9HvAfI1RScMxJVBGCSUK7W3eXFX7RuP0dQAukJC2jRiwm0ZwKMPW36qbcJHbBGjXg4fPyRaekZbozLN2U0b6G81pVpS6yKF3xicBLyxidMLsqdqKRYrLlWs2A9MuwNQbSobNiAorky-OR0kEodXMe1pBq-xiuFCr8rJM6PSRcC7mixTiHhcC9zcuzMUb4YuEsXgiGNYs6Ts1HrAesVBNIyAr7b9IT9gyhOxlLXq_Dkp3mAIWCiCShKbqqMA-EfctULH3oKALNN7xaNn6CLmTL8cUbND4WFMIVMlBxRV1hg4B58eHCBxF1NVhCmgsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در بروزرسانی جدید از اپ Network Checker برای اندروید، ویندوز و لینوکس، قابلیت اسکنر آیپی Akamai (جهت استفاده در اپ
#شیروخورشید
) اضافه شده.
👉
github.com/mirarr-app/network-checker/releases/latest
💡
t.me/PersianGithubMirror/5227
🔍
ircf.space
@ircfspace</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/ircfspace/2358" target="_blank">📅 08:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2357">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UDP6Yczb1C1tXXMVfSfTPAbjspgzM1mPEY2tiKgXNdX3StVnbjq-2eMpz5SawU4Fttyr6vIm7iyvFtO3n_oqAxDUo0UJKbK65k5mJKcfL5ScGbKbjvGWbgWG3aiYnGD76agQnFsfaiRa0ZsQzythkNqqERhq5dS3PPO071X0UyXB66cCPgB_OARSt2-Y8tWQ0ZD5UiXFL6PYSRK9xI-_ov4cL1qFvHaYNxZEd75dHTi05ucLao__XkB9_zKN7ojFLRs0D5x0E7ssA-Jxeo3zoTbqD5JyyCJnxRg3W0X7zN0RNLI46tPesmV3ugqJxmz0rxnkvQVjX8XEfIRH4yHGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ NexaTunnel یک کلاینت رایگان برای مدیریت تانل‌های StormDNS در iOS هست، که به شما اجازه میده کانفیگ‌های مختلف رو وارد و مدیریت کنین، وضعیت اتصال و ترافیک رو بصورت زنده ببینین، DNS Resolverها رو تست کنین و خیلی راحت بین پروفایل‌های مختلف سوییچ کنین.
این برنامه با رابط کاربری ساده طراحی شده تا بتونین وضعیت تانل، سرعت دانلود و آپلود، پینگ، IP عمومی و سلامت اتصال رو بطور لحظه‌ای بررسی کنین و مدیریت بهتری روی اتصال‌هاتون داشته باشین.
👉
apps.apple.com/us/app/nexatunnel/id6766783641
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/ircfspace/2357" target="_blank">📅 08:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2355">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">توصیه اکید من اینه که برای وصل شدن به اینترنت سعی نکنید از سرویسهای ایرانی (خصوصا سرویسهای متصل به نهادهای امنیتی) که شمارو قبلا احراز هویت هم کردن، سو استفاده کنید.
به هیچ وجه حتی برای امتحان کردن هم ارزش ریسک کردن نداره. و به هیچ وجه هم روشهای مربوطه رو معرفی یا پروموت نکنید! اگر کردید بهتره همین الان پاکش کنید. از سر دلسوزی میگم، بچه‌هایی که از چندسال پیش در ایکس فعال بودن میدونن دارم در مورد چی حرف میزنم.
©
aleskxyz
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2355" target="_blank">📅 20:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2354">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YOi-6jXYJpyOl0LIkggfnB0W668v9TEIKSWc_jqnOGtMfVqVvIIlI91KqcPGf2jBYBR23RmrziaiWVO_zUvN0Nrr4tZ5t6rOfsZT3so7ag9jG5v7Vox45XhiHcfrTTV-eXCUF2tsKx8lemoOSwAmvDmpAq2MEnAQ0g4QMb-1LXECTJq-oeyanSXpwaoq2MZETVVHlnAviy6Oj8laNR1Z8_tz56bmddRcToFByCbt6l4CLfE2pvSLCK9A0frXZS3yUeOj8zBjWZR60dvGNJwoBPuUnqjQdvUKAnEYEChkaLR1oV92R8BCHYS8juNYPwXZPO9vMkLvzbQ5mgSPfPhSkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما در انجمن تجارت الکترونیک تهران تجربه واقعی کسب‌وکارها در زمان اختلالات ارتباطی را مستند کردیم. از میان ۹۴۴ کسب‌وکاری که به نظرسنجی پاسخ دادند، بیش از ۸۰٪ اعلام کردند در زمان قطعی اینترنت، فروششان بیش از ۵۰٪ افت کرده است.
اما یک نکته مهم‌تر در داده‌ها وجود دارد: حدود ۳۳٪ کسب‌وکارها گفته‌اند در زمان بحران، «پیامک» مهم‌ترین ابزار ارتباط با مشتری برای ادامه فعالیت آنهاست. پیامک در زمان اختلال اینترنت، یکی از آخرین مسیرهای باقیمانده برای حفظ ارتباط، اطلاع‌رسانی، پشتیبانی و فروش است.
حالا تصور کنید پیامک هم قطع شود. بیش از نیمی از کسب‌وکارها گفته‌اند با قطعی پیامک، افت فروش جدی (بیش از ۳۰ درصد) خواهند داشت. پیامک بخشی از زیرساخت تداوم اقتصاد دیجیتال است؛ نه یک سرویس فرعی.
©
NimaQazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/ircfspace/2354" target="_blank">📅 20:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2353">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p0QUXenMje0oHDjPNNjN7PXsoyHurehwcKUbL8jozmQ8ussSKQvb1Vw8mYRzhK89zbtRmY9zmqOmXLw4TsjLbxBfpKxQlmTHiWEwjpXNJTHhzmQzuxZI1R8UU0AShnZuKoiH7Gt3OOMWToXILl0QLWd3UycIIzK1fL7jHVfbue9-2BCbbt5KixWSFHRa09CA6IkIhIg2fLFr65187lCjAVAPOgE-DdSztwhxAeT83StWk-NBB_EF9ESYdjXdfdtSV_R3EMW-g9GNGuGVOvB4xj4oWFcjSW2sxYFZ8D6K5JkalwhYgPN1wSlltW5vA-cHovNqusWu7jCdGj5eaNhbdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید به افتخار وزارت قطع‌ارتباطات ایستاده
شاشید
!
آیندگان در کتب درسی از تمامی دست‌اندرکاران فیلترینگ و وزارتخونه‌ای که اسمش ارتباطات بود اما ۸۰ روز متولی قطع‌ارتباطات شدن، بعنوان
#قصاب_اینترنت
یاد خواهند کرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/ircfspace/2353" target="_blank">📅 16:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2352">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ScsDpUM2dFpBP6hZs6NJdGtyAnQ2xy4W3oo63oq7AMFgXtQmDU0EYOLxf28xNbcYXHQllhSibgX4fYgk0iZaE0ArOvSGcc3B1T4psg570PQ07AAWqJkk2yf1GwHsFqf1sHCX7atvna6oSmx4cxDVNLUzm-7oz7_E3OJXxWv0sCdWUHYvc3YOueZt7a8axnCDFutunaGpiFedTRdXIAEkHWdqLEMILaIiHFOgfNs5gljBuiaw52Xm6L5-THBGQSfD0ut1hxZUDm9xdsgT3g7K0FosQZzeGnTT-HS8LhIR9M27SCtYmq_h23xChbgGRxir4HfucQ4GY84ynXli0RwcWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستار هاشمی از پایداری شبکه ملی اطلاعات در دوران جنگ تمجید کرد و گفت: شبکه ملی اطلاعات کارکردهای متفاوتی دارد. در شرایط جنگ شاهد پایداری شبکه داخلی کشور بودیم تا ارتباط بین مردم قطع نشود و خدمات مورد نیاز مردم ارائه شود.
وزیر ارتباطات افزود: در دولت چهاردهم نشان دادیم شبکه ملی اطلاعات ورای یک شعار در میدان عمل کار می‌کند. این اتفاق بی‌نظیر و شاید در دنیا کم‌نظیر است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/ircfspace/2352" target="_blank">📅 16:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2351">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OANUNt_jshjQ0aHN2fXTrrpNhdeq5GSZWSKg1NJKsZahlBEu_8QWOfWrbFUTLe4zz_uSt8QQYWuqRlyqTi7gEnN5QUnjBoG-N24-AApmJvNMyttuYY6oKRfDsT1F58ipIlo9L1wh3zW110-qrDTLyaGm2UWRQkaG8vMj2WkRZ5hA69X7uWGfGaw6C40eWw8ItJn4Z4P9ke2gF6tk-KHnMBzvhPLluo5q_8KQenylmTDlIY12bby7gH-1O8iJF8ZO1Fts2GBWg4_-ooG-jZ7jmPkPQp1KjtlXvBDJg_ve2p118qLAT3-iv9FgQCUpWuKYATxfu4l58RHpLJpszLvU8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ اندروید
#چشم_عقاب
نه فقط یه خبرخوان، بلکه یه راه آفلاین برای دسترسی آزاد به اطلاعاته، که بدون اینترنت، بدون VPN و حتی بدون داشتن مجوز اینترنت روی گوشی، خبرها و اطلاعات رو مستقیما از ماهواره روی دستگاه شما میاره.
کافیه کانالش رو روی فرکانس 10762/27500V ماهواره ترکمن‌عالم باز کنین و دوربین گوشی رو سمت کدهای QR که روی صفحه نمایش داده میشن بگیرید، تا اپ در چند ثانیه اطلاعات رو بخونه و روی گوشی ذخیره کنه.
اپ فقط به دوربین دسترسی داره تا QR Codeها رو اسکن کنه و هیچ عکس یا ویدئویی ذخیره یا ارسال نمی‌کنه. تمام محتواهایی که دریافت می‌کنین، قبل از پخش با امضای رمزنگاری‌شده Ed25519 تأیید میشن تا اپ فقط اطلاعات واقعی و معتبر رو قبول کنه.
👉
play.google.com/store/apps/details?id=com.filtershekanha.cheshmoghab
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/ircfspace/2351" target="_blank">📅 10:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2350">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">باورم نمیشه قطع اینترنت به ۸۰ روز رسیده!
وقتی حکومتی برای حفظ خودش حاضر میشه یک کشور رو وارد خاموشی دیجیتال کنه، یعنی مردم هیچ اولویتی براش ندارن؛ وگرنه امروز وضعیت اینترنت، اقتصاد، مهاجرت، ناامیدی و زندگی روزمره‌ی مردم این نبود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2350" target="_blank">📅 09:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2349">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CZllqUqptdKe67V3ByE6VWUdhs9J7co7RiO5IAgITdPkavFmIT57qccsZd6mJa-A5iBXyIACDBlG0ui76DeTwA0axZSGtdUXAJGmcUpiFzgAHObXQ2yEPqW_GepjJhzsBKfhzWghNqSEJCu2-x3XwmWZ5acHUhgBH97icHtSEz4V3ixzc0FZ7mCXQv-L0uE2TCUqc8Lb4DfTNo0PvDBss6ZQOchmg8ElT_OJIqJGlqGLVQUCLao5MokL7LUPU5Y5XuKv8u4elHqNmszOYEvpAi0pSSK0P20EVYKb5loziV7BeQhIQQOzMAL20CE0FeGxpMDqlhK2408p5I5iqFBheg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان بعد از ۷۹ روز قطع سراسری اینترنت در ایران، روز جهانی ارتباطات رو تبریک گفت!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2349" target="_blank">📅 21:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2348">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VgPW6gZg-f1Ic3Ff71mqBefps2RQg-9qnPFgZ4EF80dqyI82uwFAzq1YEu1s6E6guAoJN3EEPxKxpT3Ka3Q9B-tLEnOQkedkkNZA318VKuzrPxInP96-frdZcrJX_g-X-0ZMtRA-Okn2D4i0nSQs_9khn30Rr_nFY5Gxj1BVgpgjq5oAPMYkOcOsPOM5s7Wh_r7IFWuSONirNIgvocWO-Ct5s4vtAZmOwWhDLgsfW21pZS-a1hGNgxSFRKS1ykCfFcGWBT5DWqbHK0s0pKz4Ctb4wbdHc-s_dgjSf8opB_D_dPMJ49jjaZ_ZOZJPDvCZykt5J37D8_-xnk3ZkpXfTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیمکارت‌های بدون فیلتر، حفره‌ی جاسوسی برای مسئولان!
در رابطه با قطع سراسری اینترنت به بهانه امنیت و اعطای
#سیمکارت_سفید
، سیتنا در مطلبی نوشته: طبق منطق فنی، وقتی با سیمکارت سفید و بدون فیلترشکن به اینستاگرام، واتس‌اپ یا سایر پلتفرم‌های خارجی وصل می‌شوید، هیچ لایه واسطه‌ای برای مخفی‌سازی وجود ندارد. یعنی دقیقاً در همان لحظه‌ای که یک مقام مسئول درحال چک کردن دایرکت‌های خود است، اپلیکیشن‌ها لوکیشن دقیق او را با کمترین خطا رصد می‌کنند. اگر نفوذ و ردیابی، خط قرمز امنیت ملی است، پس چطور با دسترسی‌های ویژه، عملاً موقعیت مکانی لحظه‌به‌لحظه خود را تقدیم سرورهای خارجی می‌کنند؟
تناقض وقتی اوج می‌گیرد که می‌بینیم مردم عادی برای اتصال به همان شبکه‌ها، مجبورند از کانفیگ و پروکسی استفاده کنند. این ابزارها با وجود تمام دردسرهایشان، حداقل یک لایه پوششی ایجاد می‌کنند که لوکیشن واقعی کاربر را تغییر می‌دهد. اینجاست که بوی یک تجارت کثیف بلند می‌شود!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2348" target="_blank">📅 08:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2347">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اینترنت برای عده‌ای خاص، محدودیت و خفقان برای بقیه مردم
امروز هفتاد و نهمین روزیه که جمهوری اسلامی اینترنت رو به روی مردم خودش بسته، تا زیر سایه‌ی خاموشی دیجیتال، سرکوب، اعدام و پروپاگاندای خودش رو پیش ببره.
چندماه هست که هزاران کسب‌وکار اینترنتی لطمه دیدن یا نابود شدن، اقتصاد ضربه‌ی سنگینی خورده، تعدیل نیرو و تعطیلی‌ها بیشتر شده و مردم حتی برای ساده‌ترین ارتباطات روزمره هم با مشکل مواجهن. با اینحال هنوز هم بهانه‌ی امنیت رو تکرار می‌کنن!
این قطعی تکان‌دهنده معلوم نیست قراره چندروز یا چندماه دیگه ادامه پیدا کنه؛ اما همزمان جمهوری اسلامی با پروژه‌ی اینترنت‌پرو هم جیب خودش رو پر می‌کنه و هم به رفتارهای متناقضش ادامه میده؛ یعنی اینترنت آزاد برای عده‌ای خاص، محدودیت و خفقان برای بقیه مردم.
در این بین، عده‌ای در شبکه‌های اجتماعی تلاش می‌کنن با فضاسازی‌های ساختگی یا حتی ری‌اکشن‌های فیک، تصویری غیرواقعی و عادی از وضعیت کشور به دنیا نشون بدن؛ رفتاری که علاوه بر نبود بلوغ فکری و ناتوانی در درک عمق بحران و رنج واقعی مردم، برای خیلی‌ها نشانه‌ی هم‌پیالگی با ساختار سرکوب یا فعالیت‌های سازمان‌یافته‌ی سایبریه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2347" target="_blank">📅 08:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2346">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KX14q5itmHG-0qzXudgDqMZAdRM07oKuAVmF6lXhSb4jECRXa3U09vjrPnvKdpcyMJhIJVBivHAuPIJTx24lJFUd3ol3HGAFR5tTExSizlzFI_qHdGnRY8v9QqwQe8VbMp7Gh1t3M3I8F7Z8M8AJsWNBnQ7gpGn7uY8on2-S0UigJsQ1CtgZQIM6aL_9W18XbpmlAk1iyfeBZwWh7UmQ04cTBb3S1ggvHxDAuuWTP-zCZjL2e_kPDUGQn5a3wf5DmNOCMonR2COpNkfuKXhcI0cGTEpq3rkEB_pdMYjhXIsFSJ28sQA5DhwJUsQGB7CGOw-aTM16F-l6DJ9X1xp2gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱۶ از فیلترشکن
#MahsaNG
برای گوشی‌های اندروید در دسترس قرار گرفت.
در این آپدیت هسته‌های MasterDNS، GooseRelay و FlowDriver اضافه شدن، قابلیت CDN-Fronting سایفون تعبیه شده که میتونه شانس اتصال رو در برخی محدودیت‌های شدید شبکه افزایش بده، امکان وارد کردن دستی HTTP Type لحاظ شده، یه سری از مشکلات رفع شدن و اسکنر DNS حالا IPهارو بصورت تصادفی بررسی می‌کنه تا نتایج بهتری ارائه بده.
👉
github.com/GFW-knocker/MahsaNG/releases/latest
💡
t.me/PersianGithubMirror/5051
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2346" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2345">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اپ
#شیروخورشید
بعنوان یک فورک از اپ رسمی سایفون بصورت متن‌باز ارائه شده و توسط گیت‌هاب اکشنز بیلد میشه.
آپدیت جدید این برنامه تونسته دسترسی هزاران نفر به اینترنت رو در محدودیت‌های شدید فعلی فراهم کنه و همونطور که انتظار می‌رفت، افرادی سعی کردن برنامه رو به حاشیه ببرن و برای کاربران نگرانی ایجاد کنن.
علاوه بر متن‌باز بودن پروژه و امکان بررسی کامل سورس و روند بیلد، متخصصین حوزه امنیت و افراد فنی آشنا با ساختار این نوع ابزارها امکان تحلیل دقیق رفتار، ترافیک و عملکرد برنامه رو دارن؛ نه اینکه صرفاً بر اساس برداشت‌های سطحی، حدس و گمان یا خروجی‌های بدون اعتبار AI، درباره چنین پروژه‌هایی قضاوت بشه.
در رابطه با تفاوت این روش با MITM هم توضیحاتی از طرف توسعه‌دهنده برنامه منتشر شده که پیشنهاد میشه مطالعه کنین.
روش کار کلاینت شیر و خورشید کلا متفاوت هست و اصلا MitM انجام نمیده، که نیازی به سرتیفیکیت داشته باشه! دلیل اون روش این بوده که بیرون هسته سایفون میخواستن ترافیک رو در v2ray تغییر بدن، پس باید از سرتیفیکیت خودشون استفاده میکردن (که در صورت بی احتیاطی نا امن هم میتونست باشه). در شیر و خورشید تغییر تنظیمات SNI و ... که روی ترافیک ایجاد میشه در خود هسته سایفون اضافه شده. در واقع اگه کد رو بررسی کنین میبینید این قابلیت Domain Fronting چیزی هست که خود سایفون در نظر گرفته بود، ولی تنظیمات و قابلیت تغییر درستی رو برای فیلترنت امروز ایران در نظر نگرفته بودن، که الان در شیروخورشید اضافه شده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2345" target="_blank">📅 23:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2344">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UgPD0fjbiZi0mCnUQU2xcDHyGle8Ccf4yLi8T0ncta6VCWsNm5ugFxBUz_viIzGRg0v10cKEt7GSCPJrbeF2M6ERXRf5WaTpwUq5svDfiUQeyd00MeWsdI5pfcWpD6ri9iobJjQlRZkrxy6iB7QMSF86tcfgP8GU-ZD90AvIwq7JXII8b0CAGShCmjbV06bap4Gz9PIvK-zs7IckeAJPL7aQoTpli-6ASBHYkkb9hmllOArtRNXd1hxU4fbPjO18mmUiIGdBsjJiFkYxseMKNaizNliEWsBNsrktH8sWdgVnW9DqgPgBD5fWy9HhSPGcILvSincjeUG0lJlyBSBOaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتن هرچی که تهش Hub داشته فیلتر کردن؛ حتی گیت‌هاب.
قوه عاقله‌س دیگه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2344" target="_blank">📅 09:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2343">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ft9U4Gre8kdoGRSU8ABcnMMG_dCYIp6CJkoHMtQbyeRv6qaPTZWdO0ZdFtPZX_zpOxLglulRYJ_-BjWHJW0bdes6v42wK8QvZUehB8X7OffxsToAB_yqNqgImr1mkQBHac0ygXWDMVyutNcCa3rJf3ab9aJBlbN2PV-mvIJiEkU1HigAJM4CD--I1Z9d0HrE_Hk5awrdswsDb2MTdRLRCQFy3ZTC9Q5bwnXPh1Nt7zz6IRAaO029eaC5Py2i2htt-3JeaDrodHm4SnsQvQ9967LFtWdjM6GbZMq6Vu4J3LEES36Xsby5eDdPmgAZm9dkoZWY9LCXrqy8CM6V6_1xbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان TunnelForge یک کلاینت L2TP برای اندروید هست، که از امکاناتی مثل حالت VPN برای کل دستگاه، حالت پروکسی با پشتیبانی از پروتکل‌های HTTP و SOCKS5، مسیریابی، پشتیبانی از چندین پروفایل همراه با ذخیره‌سازی اطلاعات لاگین، بررسی وضعیت اتصال، امکان استفاده از DNS سفارشی و تنظیم مقدار MTU برخورداره.
👉
github.com/evokelektrique/tunnel-forge/releases/latest
💡
t.me/PersianGithubMirror/5008
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2343" target="_blank">📅 09:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2342">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n42P0J1lgSUlZWdBHDfHj3NwJscPDV4R3sCw1xAs2Ysx66VM7JJQyYSYfuhnOaLceCUHuIoX9lPbVHgYEYjMcW9piaoJ1cwMVShnEn3aI-eJNwcRgjF2fz2JrYC83_6WI1bqoFDrMfwq4aw-cjZbFa5AAJ4UprHLkGyZJYekJH97qFgTrQbmYbGv8GwgW6DsTby0mtmeCo6nmVjYQdetiuIEiACZ4cwWB5vso0ftbCccX-KL9JfOXhgdvJFiW5OxpbEr2FrTWcb02ROGKCC2I_1l1ijsTKt3D6uGOpcgRAp4xkktFzyWMvqMB6mM2MfRzBoLxG-MlP8JS-luVLo8lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آسیب‌پذیری جدید به اسم YellowKey در سیستم‌عامل ویندوز پیدا شده که توی بعضی شرایط میشه BitLocker ویندوز ۱۱ رو با یه فلش USB دور زد؛ البته فقط وقتی مهاجم به خود دستگاه دسترسی فیزیکی داشته باشه. برای کمتر شدن ریسک بهتره ویندوز و BIOS آپدیت باشن، سیستم کامل Shutdown بشه نه Sleep، و برای BitLocker رمز یا PIN قبل از بوت فعال بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2342" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2341">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J410iqwINVt1wM3wHwXzwalK_0eM1DNI6dJpyZNbTUpfYil1FWkSKifa32qke-JKuD-d7HY4Lqf4F7LU0kq-jQGOcokqBOauosT-YDCPhJ_90pGgACzfQTEQLs4oPFM2nsh-d2mrGrJHzCCSuRWUe-rsG0z3YMBofRk0fzhhWzDwPak-hHNLOXww-i6w5nVVGsAoiEZtFW06XLza_9x8W65dG8QY_Ed1lOzX2wGQoLB1479xlvwLV8eiZUwaeOVBKonee8jsZNNGEZxEBKTl2wtTbAJ-TdudX4ZhE4gr5l_8c-HwIv0btty9Za1fqGJ-6mh-R2aBDvQ1vUdJUdy-0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استارلینک مینی به ۲۰۰ دلار رسیده که فعلا اشتراکش هم رایگانه. کنترل اینترنت با اینترنت پرو و قیمت‌های کذایی یه توهم زودگذر هست!
©
imanraisii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/ircfspace/2341" target="_blank">📅 08:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2340">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lxjgI9xWPfeqYfRaq5y4RSbwjmVdAN-4mm9QVK7MFZuhP0SHjpBEQbVrfrM7kWTn-7hPaYSvQauh4c9KCdyDa2mAOF0HaR7qCH-J05uW435IpUTPL7mR6s2s8qmZBsoNP46-U4a9svOy54fUEgFObnPq3MhCPfOeWm6YLZvvptKGFTD43_unGU9BX-dk9BPIi2gwv3HeWwAJZEd-zYRj1CulfYM-XranRmQz75Tq3VMv4X-f2thVEU8dKO2ccpVKyRxrIu7ynhhzo3fpXq6bo6PBE_1hh7kqRAFQ8Vdt8uX9UxJ70KbGk7XRgdjVjgUb0UnodN8uUZNtVMvgd-D6Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در هفتاد و هشتمین روز از قطع سراسری اینترنت، از جدیدترین روش ترکیبی عبور از فیلترینگ با ذکر "لعنت بر جمهوری اسلامی" رونمایی شد.
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2340" target="_blank">📅 08:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2339">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/akDlnllqh3p1M44PeWSpifgaDRiZjFP3ZNOwL0RmYTxkyc4-WY_s07diTYUpv7TsxTa9vfGnxfn4tS6dxuesfl9n22RQA96a5xPXDrC1gBo7wSmE-HqssbAsYgiyl49euR-q7lOHJyI89BZBrc0bQ5GAN32Up2WEbqKpUXH4ma36nUabmvYklOYBpTBw1DFGqWjLXMvHjPpFAZV15SqiuDNzSHA7ryjiPkqI5bO7Z78TxXBRIYvgiP9-ziT6nzMS5OesPUlvJjpZuoLaSSZt-4Sa2j9xy96isfm37esU3np7-1OEEHZWRNSkuCJIzcQP103a0P-6NIwwERHNYtbWXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتگ از تبعیض بگو!
اینترنت غزه که قطع میشه، اتحادیه بین‌المللی مخابرات میاد محکومش می‌کنه، ولی وقتی که اینترنت ایران برای نزدیک ۳ ماه قطع میشه، سکوت مطلق! ۱۰ ساله در مورد ایران توییت نزده!
©
markpash
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2339" target="_blank">📅 08:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2338">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dYuuv0SgnLTJlcnlpKqd8dFYHeXv9Yr_tPgbyrmGEkbLAj86EXzA2gihntqdEjJYYUBi5fFgTBVAPLxL4kjmYJcpBt_JCa3XKemyFcedMTGV3NSRRywKYVA6UctuugR4XOY1hrUY5iaiHUG79sfVM0Ad3UcPTrBOsWfH3xNyieC8xhChZ7ex2yesyG0X13lHwFWLjec1PzBMx1ONlCWP3GqKXFr2eofgtlL0LAIntmnKRYkzOivEwf2TX8R0kbhJb0VL4jRJZQn8NBcxflyd5nTaTuD08l3RfmYLwLJmXd_gtznQEs3Pe_2yG7K7v29xUabE62vpZzppc97de_-MaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد حساب این الاغ [توی ایکس] بسته میشه، داد میزنه که آزادی بیان نیست...
©
AminSabeti
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2338" target="_blank">📅 08:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2337">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تقابل اینترنت و امنیت یه دروغ بزرگه. مردم نه‌تنها  دسترسی به اینترنت رو به امنیت کذایی شما ترجیح میدن، بلکه هر چیز دیگری که خلاف ترجیحات شما باشه رو هم به انتخاب و تصمیم شما ترجیح میدن. شما هیچوقت جسارت برگزاری همه‌پرسی در هیچ موضوعی رو ندارید.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2337" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2336">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ستاد فضای مجازی با مدیریت دکتر عارف در اولین روز کاری برای افزایش رفاه مردم و تحقق وعده‌های دولت وفاق ملی، گیت‌هابو فیلتر کرد.
©
pey_74
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2336" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2335">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kl67G3Lg-ljpV3pyl-qxTx3v6A16Pdwuml02qr6Po9PP2OrIKRMvshSVGq4n_UIyE4l-abOWEnyExDYyOB80HQnwSdNn1V60Gb8KwAFAQBRNz8LR5VRjTgIsfaX3K9GMiprqN1BRCZtOJQrx7kw7GkBOMxYBbnzvBqGGwLjaiAFYpZ8nuqme5x-B908THx0SmX-kW48yMwmX3-Tf_K0vHWMYcYlnr7DdkL1a_pYATk95LF3FN8vnWDpo5_AL2IU8Jvr6ydfNWfgt1UCC4C82THLR-TKojrZ-Enh-CEFQU0Gts2wwhGC66ZUcYYJgaDxTvvg5B3hYwzMN4jJrs3QqUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش
MITM
در آپدیت جدید از اپ اندروید
#شیروخورشید
گنجونده شده و می‌تونین بدون دردسر ازش استفاده کنین.
برای استفاده بعد از نصب یا بروزرسانی، باید وارد Options، سپس More Options و بخش Connection Protocol شده و CDN Fronting رو انتخاب کنین.
همینطور در قسمت CDN edge IPs اگر IPهای وایت‌لیست شده
Akamai
رو بذارید، سرعت اتصال بهتر میشه.
👉
github.com/shirokhorshid/shirokhorshid-android/releases/latest
💡
t.me/PersianGithubMirror/4954
©
PawnToPromotion, mahdavi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/ircfspace/2335" target="_blank">📅 16:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2334">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نحوه اتصال رایگان و نامحدود به اینترنت آزاد با متد ترکیبی MITM + Psiphon
👉
github.com/patterniha/MITM-DomainFronting
©
patterniha, MatinSenPaii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2334" target="_blank">📅 16:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2333">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">روز هفتاد و ششم از قطع اینترنت.
معاون دفتر پزشکیان گفته "درصورت برگزاری همه‌پرسی، مردم امنیت را به اینترنت ترجیح می‌دهند".
وقتی گفته میشه هدف از قطع سراسری اینترنت و خاموشی دیجیتال مسئله امنیت نیست، دقیقا مطرح شدن همین اراجیفه که به جای نظر مردم به افکار عمومی تحمیل میکنن.
زمان زیادی از کشتار دی‌ماه نگذشته. به جای این چیز خوریا، بهتره یه همه‌پرسی بذارن تا وضعیت مشروعیت جمهوری اسلامی دستشون بیاد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2333" target="_blank">📅 09:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2332">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pZHsATz9eFC6uU8xc4C8NXN0X1D9ZmbFrH8XAhXUOFzKCjdnLBpbiAxx4nExHT_Oo_BkfmQmaCKsrtgss7dCL98Qr6Xhs26LNKgTbVHQKhxq4lfQXSoeHKtf8sY-B8OkTGmpmUqv_LfAxWOMP9IsP0M4UdvGnolKAQFp3mgNGCmC0nETzp7xhfJPGm_8YhlLyosQMcPIwbxPu5paqS2JM1k6cRsp9tPeqgYx3n37euyrnCL_ywR7XAhn-fUS9l-cZAfXeLwhFUBNHyZYrlXbg0KlqoAMyH-WDgQjK1cQhZwnUwfOSDGD2TNwvhfmrjQIqptRv7gaMRgSF7nO2XAYWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون فرهنگی مجلس: امروز پیامرسان‌های داخلی گوی رقابت را از پیامرسان‌های خارجی گرفتند.
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2332" target="_blank">📅 19:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2331">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nvT49fyBXyDewz0A0eU88UzT0wgw3zYXia86NBDwcynFsmfghExTE14ONVsj0tImE5q0UYGLh6oiD4jZBOkDZ6bAeEYMj7rf7i5_dcn9mObUzDIwdjnHGLjcmXDaJLcjjiRzL9T6l7DWAUps_C8bF80hWtyY0GRbHyMg1mErOOrbtH2s0oz6hgg-CoOZJjXLTJAQVD45NCzFnLhTxQl31u8_UjV-gi4rBaxB0aM5xhLenQQ6owiugriX9SFkXqsm6HNWJ2f-D3GGkRUkLbh7yOrNNZ7NVZVRrrUP7oxPAxXZkRvtOhoUO0k6hGJ8-ZKS8AFq-8a8CFYJN296Tm15rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷۵ روز از قطع اینترنت گذشت؛ همزمان درآمد یک کانال فروش فیلترشکن از ۱ میلیون دلار گذشت!
©
mosi115
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2331" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2330">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rBj2HUK2qMImWsUSrxd38D32349PBMGQZd7WZHlkKM11XjyIiY3sFbPlbiFOAlWKM3UPFqQQ1sAKf-zW0Odt0q91KQofW3_rHFb_wE7gJ7AwjSZnFdglE5ERuLgxvOwLdnocCgp5bchI3lY9ABYoUB64KG0WNY9eQsD67om3LfS6um_ZeAS9n3pSgpwg_f92IIGqJPrFUwz4lf7VCxJkqjcIQThyS5tncvTRZv8qMjxA9p7ZskBe_De1L638bpalha342suaqW3znQstZ-Zx_ta9931DGFOAJXpg6LccWL8hUgL-CAuKuAO-XY-czWyS9BK3-yoJ6smyeKJvwsz0nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میاد مرحله‌ی جدیدی از
#اینترنت_طبقاتی
شروع شده؛ دیگه خجالت هم نمیکشن. قدم به قدم دسترسی برخی افراد و کسب و کارها وصل میشه، تا عموم مردم به عصر بدون اینترنت و بدون هوش مصنوعی برگردن.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2330" target="_blank">📅 19:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2329">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سی‌ان‌ان در گزارشی نوشته
#اینترنت_طبقاتی
در ایران خشم و نارضایتی عمومی رو شعله‌ور کرده و به نمادی از نابرابری ساختاری در جمهوری اسلامی تبدیل شده ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/ircfspace/2329" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2328">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">قوه قضائیه در یک کشور مردم سالار آنجایی که حقوق مردم با تصمیمات دولت یا نهادهای امنیتی نقض می‌شود واکنش نشان میدهد. در ایران رئیس این قوه نه تنها حق مردم در دسترسی به اینترنت و کسب و کار مردم برایش مهم نبوده، بلکه چندبار شاکی شده چرا اینترنت پرو را سختگیرانه نداده‌اید!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2328" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2327">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=TySLXyLrIXYWeWKtVTNUacxi84xdEaBnQhH8m_1CxOmwLw9dk7HkhqPGS1JuiAaexqo0IXK-UC99ADeYqBrcr6xwvPvxdvc0jz0JjMiCRuHSSWn9BjwpaFyucMdRNe1T75SP3_8NXGA-LJ4w5xV_eHtXztviYZRn5E8iyXpGTOwzF7C5nkKWQBiGraqJFl9P6ygHdlSTlJrI2gYDaxeTST-WbDybNqTiwncS-0GKbAg6OPO-jBCZk1duLrHeUPngXDqa57t6RDl1mFfgpU-rBCc-lrQVNoEMUkc6Z-cI7Bqb-g5lIpIrWm5xR82oyva0WwwxE9N-jUH_IQ857mlBSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=TySLXyLrIXYWeWKtVTNUacxi84xdEaBnQhH8m_1CxOmwLw9dk7HkhqPGS1JuiAaexqo0IXK-UC99ADeYqBrcr6xwvPvxdvc0jz0JjMiCRuHSSWn9BjwpaFyucMdRNe1T75SP3_8NXGA-LJ4w5xV_eHtXztviYZRn5E8iyXpGTOwzF7C5nkKWQBiGraqJFl9P6ygHdlSTlJrI2gYDaxeTST-WbDybNqTiwncS-0GKbAg6OPO-jBCZk1duLrHeUPngXDqa57t6RDl1mFfgpU-rBCc-lrQVNoEMUkc6Z-cI7Bqb-g5lIpIrWm5xR82oyva0WwwxE9N-jUH_IQ857mlBSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر هکر بودین و میخواستین بانکهای جمهوری اسلامی رو هک کنین، سرورتون رو کجا میذاشتین؟
علی کیافی‌فر، متخصص امنیت اطلاعات: در جنگ دوازده‌روزه، نوبیتکس، بانک پاسارگاد، بانک سپه و بانک مرکزی از داخل خود ایران هک شدند. مثلاً نوبیتکس توسط یک سرور زامبی واقع در یک مدرسه‌ی علمیه خواهران قم هک شد.
قطع اینترنت امنیت رو کمتر میکنه و نه بیشتر. سیستم‌ها نمی‌تونن آپدیت امنیتی بگیرن، سرتیفیکیت‌ها expire میشن، ابزارهای دفاعی (فایروال، آنتی‌ویروس) از کار می‌افتن و هکرها (داخلی یا خارجی) راحت‌تر کار می‌کنن، چون نظارت و لاگ‌گیری مختل میشه.
©
farhad_mottaghi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2327" target="_blank">📅 19:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2326">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NH3eEqnwvGIwAjrGZ1kBH-A9zrpSv9dcz2yKagDm5aa5HkF84VcUPIv5i0L6EEP-B7FcnIkzAHWk0FWWfHq8bIGCRX_QrjR9NV-heJfx8D9Soqx8faripGES3jX3LFJWhG1LxoIxXHobVsg4th8qvleOLPuxE1NVcKbzU9ar0rzWbqwikox0wET4fmOx6kdAQg1x2JzQQJrXwQQhmrxOJDgkhvTqn3pyym7_5EgfuKjWu-1_ch_1gCcMeRh3Fn9_HNAnQuGv6LlpPM03KuPurixOMJQHb5algOvmpHHwYtvODFJGiejvSh0cnQopICNPk7G_ArqzREI-GSbaCONNqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آگهی یک دفتر پیشخوان دولت برای فروش
#اینترنت_پرو
©
mamlekate
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2326" target="_blank">📅 19:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2324">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kqVZf_g69cbw3U01ZuvlNuex8nc9WWZRlZnM9cKsIbIRLzep_9p-ndzvJVQbSj8WFwFw3GENnq2m0JZBBJfJf-cjAmH1e8oeYaspOp-6k9biWIyPUr_CLWlRWDpAyDx02zTc31ErvsIUjFhub5UWBH42PZVTgzIUeQaLU0mfCbrVaEm4eRBybTHZtTj3FsWjCnDJr_mlPIfbXEded5ykm1U4q6PHluWNUa4r_VphV7Uasy2CcmBBjDpjbd602zSLMuOLJSbYxPe0y0Sj2-yhqfzEEsk11s4EhcrNsjTTXnVg70kfGzhO7yWBmHPvaWHMUWmeGtgTn5j_f1bBOaMFGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا دسترسی آزاد به اینترنت در متن سخنرانی‌های رییس‌جمهور و هیات دولت برقرار شده!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2324" target="_blank">📅 10:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2323">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تعداد کاربران اینترنت پرو کمتر از نیم‌میلیون نفر است!
تا امروز یک اپراتور با ارسال بیش از ۴ میلیون پیامک، برای بیش از ۴۵۰ هزار سیمکارت،
#اینترنت_پرو
فعال کرده و اپراتور دیگر با ارسال بیش از ۵۰۰ هزار پیامک، حدود ۴۰ هزار کاربر پرو فعال دارد.
©
aghplt
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2323" target="_blank">📅 08:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2322">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mh4P-45r4esYhl8o5q03aviyehCH6tYk1Dog26K33uus1yNS73OvdDkkq2tfPmMzmLLPTCGVR3-4FL1tE4kcdwJqQg9YwDxB-Eg4-T-LqHNie-u4sVh48Hx_UpS-3W2byBFaFE_eZmIdDIf9d_OUfHTwy-FnUKbMfae1BJjaB0pE2B7al0PUTKOC269L5rdJEbuxCRUWUwK7T-qUAz5Uhp5TRkjYUbjvVKxX1ilVOr-cJUmpdMoB_OCO2-_FplkxmjZe2FZPG-OsnxoEK6b5rjn_285IdfQh8--7yLub6DMUpL0h8c0jP3Hwkr8J_3c0HP2k83LUaocbcUnTE0RAxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن مهندسان نفت برای دریافت
#اینترنت_پرو
واجد شرایط شد.
۷۵ روزه اینترنت رو به بهانه امنیت به روی میلیون‌ها ایرانی بستن و هرکی که کار و زندگیش به اینترنت وابسته بود به خاک سیاه نشوندن، تا
#اینترنت_طبقاتی
رو اجرا کنن. مدیونین اگر فکر کنین کیسه دوختن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2322" target="_blank">📅 08:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2321">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بدتر از قطعی اینترنت فکر اینه که سالها درس خوندی، دکتر و مهندس و محقق و پژوهشگر شدی، بعد واسه کار علمی دسترسی به اینترنت بین‌الملل نداری؛ اونوقت حمید رسایی با حول و حوش دو کلاس سواد برات تصمیم میگیره تو اینترنت نداشته باشی، تازه خودشم تو ایکس وله!!!
©
NiHa_Mehr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2321" target="_blank">📅 08:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2320">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UUsbct1IuMyzfoqn-Op-Z5ApZ5OqFuacSqkTKT_IRFL-sjMKdTlH7WnAf8BneBq3lznA78hoossj2ksxtb2n8y7Qw4ohI76-3PU687fLudZ3SYJOibD9LSe6YFNi9ilhtnBFha2tJX-B-bXEsQiG4cqpd3kA6umv-ickOEu6BHq_fzM0Nb1O7b7E_iLHPWOE4TrQ-o2SwocLVszkmL7w5Xy3meU1QeujVty-fI0WgoJ2N7nW3PhIIWxR94TEN3mAyAIy49rnf3OmxsDgaOAmulKRm9K3e9oTYtYSszPvYQlWgCmqOrThxxX4pl47_oEn8eOJdcOuQr3loratZO3VtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس قوای سه‌گانه کشور در واقع ۴تان، که یکیشون به نام
#قوه_عاقله
نه توان قانون‌گذاری داره، نه زور اجرای قوانین رو، و نه در جایگاه قضاوته. مهم اینه که قوه عاقله قصه ما با
#اینترنت_طبقاتی
مخالفه و قراره نقش اپوزیسیون داخلی رو در این مضحکه بازی کنه!
©
nimaclick
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2320" target="_blank">📅 18:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2319">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hSelNLExqKKUq5IQ3JcuLifDNDxOXHFu1aUCe9CQmqg9JNKkAxWIBiHPA-Cmuw4Xd7fMQp6m_dqeNW9g3Vaz_xctMCUZXN_G8Gj6YTf2bVPFViVJnaJV-iJeXlKNrUYIh2tH3NRUnLipT318pg-QgRfuxSqFIlxQuFY34_OX_LY8_Cuv9TA2eRa3dfrvnF4SzBLfv1WsAqZvqQCk4H_UN_pBMPKB123kYd5xAfSgrpo9Q1E9-FopW04dGH5aXHeGoXk6qgFjK6Q9o64voUWtnaYG2vB8GsDyKLf5QxWAw22mzskzt8cjDy34enLL03FXwv7aZN57EkldK_4_tXH3YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای
#اینترنت_پرو
به اتحادیه صنف اغذیه‌فروشان و مواد غذایی باز شد و حالا با ارائه پروانه کسب و کارت ملی میتونن از
#اینترنت_طبقاتی
استفاده کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2319" target="_blank">📅 17:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2318">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SRYlFkXUU8E5c37fnH-RRt36mq8gRcF7V4KgicGmTW5xUO4vxpzOAMiJMXGZFiguwqiE_0bFxMaA-yKlzNPPVdmqu_R40WpWZXgxdN8uCVLfUJcZAFSL9EmYElKzzxwkVj8vUYh8KQaqM_P29Qk1OK21i_Iwjfr0ajz5Ewm2APWOHVMrNLQLC6KU5d17HCVAglC_Dx_S7NcMN5D7hi3GjZoudta6a-Cu86p6D0i4Q1DELfQYpkh_Ip-g4i-lrmfSchbjIuDtT8vbRwgzQOZG6A0xjGTRaDdXlclrmcBJTjs-NPz6uaBaY5vO3ebiwq3PYQpRrj8NJCaLE6si14_ZxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان TunnelX برای زمانی ساخته شده که کاربر نمیخواد تمام ترافیک در سیستم‌عامل ویندوز از VPN عبور کنه. با این برنامه میشه فقط برنامه‌هایی مثل مرورگر، تلگرام، ابزارهای توسعه یا برنامه‌های مشخص دیگه رو وارد تانل کرد و بقیه ترافیک سیستم رو روی اینترنت عادی نگه داشت.
👉
github.com/MaxiFan/TunnelX/releases/latest
💡
t.me/PersianGithubMirror/4816
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2318" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2316">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UQxpaaSFAHVpVUHcNxX3g3gQ5Fbk5VIMk18Jf3OPTDU0skh-wihbs2ibWTmOpIb1ngMS6qgQ0nRqzMXfZ6G9GAs3AdIHZUkM9fygQKfRz1eLyWmpxiqg5xLpoqYktyJkO6L3LCwFGRGdxsCJ1GkSPUWpsm_ryyE9Wt7RQk7yVxeHsigdOTMGwFtDbShp3D_alswvl5V3EDa55_4UP38M_MJ6gXgpTStooOse0pNQq9k5jKmXietrU9mwrQn-gG_eqQedtkbx9d9yHYg4OSGKuZ6QAQA-8C-z7OEJFZjcN67ui5jFphGj_ZzAglEhu1xgCv28hfvRDPATyMcXuY-x8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر اینترنت غزه، اوکراین یا هرجایی که حمایت از آن برای حامی‌نماهای حقوق بشر "ویترین اخلاقی" داشته باشد فقط ۷ روز قطع میشد، دنیا را روی سرشان خراب می‌کردند؛ اما اینترنت ایران ۷۴ روز است عملاً قطع شده و آب از آب تکان نخورده است.
فکر می‌کنید اتفاق خاصی افتاده؟ خیر.
ضریب دسترسی واقعی به اینترنت آزاد در ایران به گواه نت‌بلاکس به حدود ۲ درصد رسیده؛ میلیون‌ها انسان نه ۷ روز، بلکه ۷۴ روز عملاً در یک زندان دیجیتال گروگان گرفته شده‌اند و همزمان که جمهوری اسلامی در پشت پرده به سرکوب، بازداشت و اعدام مشغول است، آشغالی به نام "اینترنت پرو" را به‌عنوان راه‌حل به مردم می‌فروشد، که عقیم‌سازی عمدی دسترسی آزاد به اطلاعات و نقض آشکار حقوق انسانی و حریم خصوصی شهروندان است.
ظاهراً برای جهان مدعی آزادی، فقط آن دسته از رنج‌هایی دیده می‌شوند که موضع‌گیری برایش هزینه‌ای نداشته باشد، یا چشم‌های مردمانش رنگی باشد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2316" target="_blank">📅 10:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2315">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N2ClUx-TLGnkQ6EWdRyTlJWVN1MGF8LnQthauxelH9gYK4JI0U6k9j6MJ2RE-6Mdqk1h2H3qXlWCHf68o7PsUdQ9enQssdlspfOCa1TIIcZ1o7e9BHEiRTRquIAIQzxLtXywu17Zf8XguDvsNpiFxn8x6b0yEThf5_K6iPcrT08Ajmn7Tno3loHEp-jzlF7HPauyZnW2EdaB8aEGFOcgRKnELW0s5xEESitGg8pd2xcZDgNHJytGSrYk7ehRMclsq_SaKDny6yPUlrjIeb-BcH5-vv5jp_y3GwGBsD2ZP1YXsJ-bZ5XijC0thrDrQhj5gYB7hssLOwaszVX6nnqJ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در روز ۷۴م از قطع سراسری اینترنت هستیم.
وزیر قطع‌ارتباطات گفته "در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم".
نتیجه عملکرد و تلاش ۷۴ روز اخیر این فرد از خروجی عملکرد یه مترسک داخل مزرعه هم کمتر بوده و جالبه با اینکه از بی‌خاصیتی خودش آگاهه، حتی بصورت نمادین دست به استعفا نزده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2315" target="_blank">📅 08:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2314">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H0fvFMYhi2rcTfW_hLjLCZiMyAfdNOx_89JZAbNwAS9G1PQBQxdguACYU5kgNuy6YRWaaQh-50RdFTVe7cZfFKiXg7UGlkCSsyQp1-Ow3vGhgNrYpMu9z1jNOq4dHhjLCzSP9KOiv1FU_u-eQWhsoUU7wRODIYxWfq7dYg3bEVfV393v4BciJ1pChikGBNmXNKt1Y117BtT_ee1BArAA7TaO7-XfTciiHYF9b6W_tS2ZtiY8k9eboQZjwpjZIxTNihSWNSJjy3WvyZSSD7SNYiZTKcqUHhTAJo40T59yIkbGawVkGVWO6UVZkEYw1IZA2KvFbzBoIkHfz-f5laRyxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه روندی که نشان می‌دهد تصمیم‌گیری درباره اینترنت و سطح دسترسی کاربران عملاً از دولت خارج شده، وزیر بهداشت برای رفع محدودیت دسترسی به پایگاه علمی «پاب‌مد» مستقیماً به رئیس مرکز ملی فضای مجازی نامه نوشت؛ اقدامی که بار دیگر نقش کمرنگ وزارت ارتباطات در سیاست‌گذاری اینترنت را پررنگ کرده است. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2314" target="_blank">📅 08:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2312">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l1Pjo1NaIb60rbPhvihFO0gRvg-H-6CJ9Ea_cA7jZ7Y2itPfSJ6Brn8LNJK1Kt2DHlzQkBPmInpxRSEh4J1Gs4EWIRQBrajeA8RPXPLoT81_eotZoXHIaZdorGblMekteIjOct2yviQafsrSyoEPtS1VMBXTpf4wbuW7NcF8vS59fcGLZslDF5ou7xGMDDvZtFSJpYJ1YWxROiKJu6kCl-lR0xRQefk0kyVU9jN-LKXJCeYgDtu7mprueKlVH4BFtIroChJWz_OemSjL9jF3iutpN9ztehstR61sygEkr_otn5lRTOHrFKrS2gXT-ncxq3WIJ1KcjNKDHl65bHVnKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت AIO Downloader یه ابزار متن‌باز و کاربردی برای دانلود فایل و محتوا از سرویس‌هایی مثل یوتیوب، گیت‌هاب، اینستاگرام، ایکس، تلگرام، گوگل‌پلی، تیک‌تاک، پینترست، ساندکلود و ... هست، که فرایند دانلود رو از طریق GitHub Actions انجام میده.
این ابزار طوری طراحی شده که در شرایط محدودیت شدید اینترنت و وایت‌لیست فعلی بتونه بسیاری از فایل‌ها و لینک‌ها رو دریافت کنه، بدون اینکه نیاز باشه سیستم یا سرور شخصی برای دانلود داشته باشین.
با توجه به اینکه این پروژه به GitHub Actions متکیه، بهتره برای استفاده ازش از اکانت اصلی گیت‌هاب استفاده نکنین و ترجیحاً یک اکانت جداگانه بسازین.
👉
github.com/ProAlit/aio-downloader
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2312" target="_blank">📅 08:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2311">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A5dkZm-KxRmH8J3XMqvkZC1FVZQusiA-z070HWTAI-VV0AwOYlrc_4OqxPVKPC03yC7zOvYz1SwM9zVtMwjsTfcM0OMoSRVeBFVniEwA6XWJ5Irej9kUDd_ZNePy3cImeV0BEWWmpDUPU8HHj21E1kxyzySkCfwp4DfqKi32UHiqgKT6sJguHBm0WyiRvO7CS-yV_WmSUIaKaGtGoB6iHRgwXKWE8VlsOkKtmjFKl7u5NJ3tvtE73UVbDigDm_AHvPabHT8c7c4QGerLvBCF6iVmEsd01yowlDk2JyZwb6NsGM7hT-jyNJwM2m_912EQB75phOm2z0LippERGNYBpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پیامرسان_بومی
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2311" target="_blank">📅 21:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2310">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JD7cIHIjNL7q5ZkpNF6_fwf7qduWKo5XCIMfmWs6t1FV3xPEYq1A32UIye4r_hfJ29TlHqJ4c-1Q4KwdlrJrTvD9JPsVab2v7heBANMj9LKy-9H_3m1SRcbURyqdc_OD4w7O0TKj5_jAvpyiAfjlR2iZWg3TYi4uiV8Wof5jT0e0TNPo28OEzKXWiwZlSR2_r0ZqFnlolNRwGggar_erLiEK1PlNO2rqLfKolkp8Nqbt1ASd8N_EYYSLVVYz_3uTSXqimnRZahnysHM68YChASWTnqOn6p3qDPLrtVjG9P_JNwhm0lxY9UdBFgm9Ch9-WcQkrHb5GGo5iVdqiBs3mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه رودربایستی رو کنار گذاشتن و بدون ثبت‌نام و بدون احرازهویت، بابت پیوستن به پویش جان‌فدا ازت تقدیر میکنن
😁
کی به کیه؛ اگر آمارش به ۳۰۰ میلیون برسه هم تعجب نمی‌کنم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2310" target="_blank">📅 21:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2309">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تا الان توی هیچ پستی نگفتم که به پروژه‌هام دونیت کنین، چون حس خوبی به مطرح کردنش نداشتم؛ ولی شرایط همینطور پیش بره احتمالا سر چهارراه نشسته باشم
😂
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2309" target="_blank">📅 21:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2308">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قبل از شروع جنگ و قطعی اینترنت درخواست فیبر نوری دادم و حالا اومدن نصب و فعالش کردن.
با تشکر از شاتل بابت سرویس خوبشون؛ در واقع قبل از نصب اینترنت نداشتم، ولی الان با سرعت خیلی بیشتری اینترنت ندارم.
©
itsmralii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2308" target="_blank">📅 11:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2307">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YjDwc08EEmM6AehlbSlknZ91VvWJdQYBkZSuuiSaosVKKg6oXhIRsXsMNI1aRJlGVxtcntAHko5mm53mg1dIW_VSxN9nsFmfW6BnJ2sYiZLGSSrMA9wKkTf6339rMYsLNPf7ItNPIyvzo4Io8rXCHRGzDSneQDm-XJuh9S1jpQdcQX7NPqNJhKlsh22MgpgwooV82XSqsOrYPiHDY8SKBPsyzAEh30SoOKU0RyRfNc7K08EgIsPkzww3sU40FXR_lHGdSuthPXypFWtDz_QD64r5LQGdDaYveVxfTxcVv8lAmQUP9J24LYyYp4NwdQBBPUoc5xVLu8Giral8gKf09Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور از وزیر ارتباطات بابت هیچ و پوچ قدردانی میکنه، بعدش همون وزیر از رئیس‌جمهور قدردانی میکنه، بعدترش همین بدردنخورها دسته‌جمعی از مردم قدردانی میکنن؛ اما تهش می‌بینی ۷۳ روزه که اینترنت قطع هست!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2307" target="_blank">📅 08:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2306">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FnH2cBJ-pGKn4abmz5b1DNqUr4kCFvLMICBZ-Pdmvb0tEMUQp8mxr_MOWgRQHzy6nkPCTzeUHgcdxGE-ua4eIu1YUacdzvWVuOEb8S2ELFXk-n3pB_g91-y9BjNwGyTN_lls0zvwcYXj92ngUy0D0cpnKNT8tZ7-6RmLqDM-uEHR14YgtQ2AuJdl8EoS_JmSZ5H2plAWQN34bg1II2a4OLMavQF0G2fR4txL_bZ82JdA-JjTuMTcLnAzqXulIG-spV-V9rfWQZFRlfgHWyLGwHrldWdywS4Z0qEsiUSirnquv1VAbV1Y5wSsFm8vQBBHigKv-Wc2IZY6W7Ci5UsIwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteDNS یک کلاینت متن‌باز و رایگان برای اندرویده، که امکان اتصال از طریق DNS Tunnel رو با دو حالت Proxy و VPN فراهم می‌کنه. این برنامه با تکیه بر MasterDNS و StormDNS طراحی شده و میتونه بدون نیاز به تنظیمات پیچیده، ارتباط رو از طریق تانل DNS برقرار کنه.
👉
github.com/iampedii/WhiteDNS/releases/latest
💡
t.me/PersianGithubMirror/4637
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2306" target="_blank">📅 16:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2304">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cGp8eaKUyAceZsJTxS-_PjwEFgdV1p64RDVlfCpWckOYgD42_xSat8fbVxI4N-IEDrupZiDN-aXU4t7oLT4TeRicdGtKpcaAlAkwBCJxv8fvlHofW1IIlQlmqofzl2qYXLHyEaP0igpZV-2QKqC1Fx96QPCPCBlQrC4DzeQ2nG5vPObyG3OsJ0HqObht3UP7KZCrUfwKNPmgzXAS-HJPJm5K0W8pSXFGAbO8UXZTgIlXlwOkIcT8CbwsQhLgkjD-peXR8YVCPsFF4TGNhabO20rfcPr6pOOxGRygnZj5WY9oA5DXHT5qlw03jmqvDqdS322hDqtFR5Vpn04z_3nZYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز که نت‌بلاکس عدد روزهای قطع سراسری اینترنت در ایران رو اعلام می‌کنه، یه عده میگن "خب شمردن که کاری نداره، خودمونم بلدیم".
ولی مسئله فقط شمردن نیست؛ مسئله اینه که نباید این قضیه عادی‌سازی و فراموش بشه. اگر فکر می‌کنیم راه مؤثرتری برای اثرگذاری وجود داره، خوبه؛ ولی سوال اینجاست که چرا تماشا می‌کنیم؟
۷۲ روز گذشته و هیچ اقدام جدی‌ای برای کمک جهت اتصال آزاد به اینترنت انجام نشده، کسب‌وکارها نابود شدن، آدم‌ها شغلشون رو از دست دادن و سفره خیلی از خانواده‌ها کوچیک‌تر شده. مردم برای یک اتصال معمولی باید میلیون‌ها تومان از جیب خودشون هزینه کنن و در عین حال بخش بزرگی از نهادها و جوامع حقوق بشری نسبت به تداوم قطع اینترنت، سرکوب، دستگیری‌ها و اعدام‌ها سکوت رو ترجیح میدن.
در فضایی که همه‌چیز خیلی سریع به حاشیه میره، استمرار در اطلاع‌رسانی خودش یک کار مهمه و همین گزارش‌های روزانه امثال نت‌بلاکس حداقل باعث میشه موضوع قطع اینترنت در ایران کامل از توجه‌ها خارج نشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2304" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2303">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این هفت کابل اینترنت جهانی در خلیج فارس رو اگه قطع کنید خیلی خوبه، اونا هم مثل ما اینترنت نداشته باشن، بلکه دکان‌های حقوق حشری صداشون برای اونا دربیاد و یه نگاهی هم اینور بندازن و دل ما هم خنک بشه!
قطع کنید.
©
ehsan_369
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2303" target="_blank">📅 12:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2302">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CfqsKZrtZVbSz79pX04AmgQY6nvP7yGJ5ZGEPYiWiRabq1kobX0tSOSTy2niw7UQxNqPBEdQcVTRfCR9z1pi2_RfokF8Ho52w1R_VdwsiC3R6rpxjniv_K0xP6gtlNzdhuaK7lb-orV38Ql8pEzv_t86bRbhg81TOmXO6kp1GpJos5Zf-ej4RZ13dzgSp9W0ZtrGEiqFun8_lZhfxaZTmPqrnNSjGhY_lyef8MDIZjkdw2nuhUWfwPQvKk5REsMrm3EacmlZY_tN8GjxuHh_eTfLgbYy5-W5d32WSX0aX7I9qvlJZ0N99ZGZLsPZdIE_wSXiy28p7A2K1GV0L0qj7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم نوشته تنگه هرمز فقط مسیر نفت و کشتی نیست؛ بخش بزرگی از اینترنت و تبادلات مالی دنیا هم از کابل‌های زیردریا رد میشه، که از اونجا عبور می‌کنن. پیشنهاد داده ایران از این مسیر پول و کنترل بیشتری بگیره؛ یعنی برای عبور کابل‌ها مجوز و هزینه تعیین بشه، شرکت‌های بزرگی مثل متا و مایکروسافت مجبور بشن تحت قوانین ایران کار کنن و تعمیر کابل‌ها هم فقط دست شرکت‌های داخلی باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2302" target="_blank">📅 12:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2301">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/asKvBGhS98M_wcfhEPnx7Apw9er7gkaGCZZjl7DVTgSsIQEuhdieQZQfW9IR4VFsttdwm5qs_wYnYYm2i2Vxnzy4iN9VNQCvf633bPlZ1jy1meGm57JP6trdsLMdVcwLfHKMAxepWwqx6RIP38N0KsOxX6I4LJk-UZNw8ImxZD4StkPjsTjNfl7saV-uc9hJyo4u6ziL0TCXnbGgnmxtukXWaV4FnUblBiwiKqPewTmWn-gf08ntX0Ah-2VHgMXwrQgQmzbPWeC4MHAum4DtNu-CLXe7NfX9zGfgLPeBc5pngHOOVwb26vXTVA3qHTnuudO36q4hDa3vLAMRASBJWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران وارد هفتادودومین روز خود شده و هیچ نشانه‌ای از بازگشت گسترده اینترنت دیده نمی‌شود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2301" target="_blank">📅 12:07 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2300">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fYTyGlV1NIs0LXYbwixhTjDuifaIs-1ioK48PUozzV1SYZ4Ac_YlwEhuQw-qf2NUbLfyknEOmIwmwXC7sXgGwn4WKE_HParErKnz_rQYQ0dbIKpBVyBupTDoNKOgJgbZB6exLYUaJRh_qvY5jatQZYtc-lLkaYC1XDdzAiOiT7Ug2GzXDO8dKkiv4TQNCl-faBVkU8kb3PS77hhj7zE78Itn1gmWFXMj6AA2HasQWnkh1gV8eZVKdKVlnuYJIXFLxHRnY_P_ZHEluBcOtb5KgDfBVE3aBQexCHLRsczRuQuPgWY615TpgnOgd4TPdhxep5MypFYuqMlyrgmIIlzx-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۳ از اپ متن‌باز و رایگان TeleMirror برای "دریافت آخرین مطالب کانال‌های تلگرام در شرایط محدودیت شدید اینترنت" برای ویندوز، لینوکس و مک منتشر شد.
در این نسخه نمایش پست‌ها بهینه‌تر شده و مشکلات مربوط به کش تا حد زیادی برطرف شده، بخش تنظیمات به برنامه اضافه شده و امکان بازگشت به تنظیمات پیشفرض فراهم اومده. لیست کانال‌های پیشفرض افزایش پیدا کرده و علاوه بر نسخه Lite، یک حالت Normal اضافه شده که تلاش می‌کنه در صورت امکان تصاویر فیلترشده رو هم نمایش بده.
این برنامه فیلترشکن نیست و بر پایه دسترسی‌های فعلی وایت‌لیست اینترنت عمل می‌کنه، بنابراین ممکنه روی برخی از اینترنت‌ها قابل استفاده نباشه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4599
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2300" target="_blank">📅 18:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2299">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">افغانستان تست خدمات اینترنت 5G رو در کابل استارت زده، عراق تلگرام رو رفع فیلتر کرده؛ اما جمهوری اسلامی تا دقیقه ۹۰ درحال آزار و اذیت میلیون‌ها ایرانیه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2299" target="_blank">📅 17:52 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2298">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/acVRea90jW-5RS4udnTExAIexH76hOwnUluYXYlhzW-tSuB3nCCGgh9atb4CV7ZpQ2eZrdNACUvbhSrj0d1n6A4o2wWLE4t0nS65m6ozTleQrGCF2xXtvFuCpSJaHJhGA5WLyrkR-FKFA7HyzlTTsUrPs_-Q18xmcU3EOB_T_mPZw_6bbEnwAXNocTx9uYM9szxGVY0DsDuAiD3PsMf8AYGFGFidc3-7Or5HO-cbgYpPFRdZIweNfeIC-TQp-3TaQ08tpoaps4HUPgqDdNUGdhZOmRMuu7T6vduypOIs_jP-Kj1ChU-YMAcYPTlUZ3MaYkqZXY3yUN1qdad2Pgdizw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی خاک بر سرتون (پیامرسان‌های بومی) که با اینهمه حمایت و در میدانی بدون رقیبِ جدی هم عرضه ندارین کیفیت خدمات دهی، پشتیبانی و توان زیرساختیتون رو ارتقا بدین و بعداز اینهمه سال سابقه، آدم نمیتونه ۸ مگ فیلم ارسال کنه.
بعد از خودروسازی، باید شماها رو هم دومین فرزند لوس و بی‌خاصیت کسب و کارهای داخلی دونست!
©
kamran_falahati
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2298" target="_blank">📅 17:48 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2297">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">جمهوری اسلامی ۷۱ روز هست که اینترنت رو به روی مردم خودش بسته!
روح‌الله مومن‌نسب (تئوریسین بارداری با ۲ گیگ اینترنت) گفته شرایط اینترنت به هیچ وجه نباید به روال گذشته برگرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2297" target="_blank">📅 17:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2296">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DUV6A37Io31uUid5GnKXCW2c6tNgnCzdk4uAEhkufykkBVmB6GaolLN5A3E9XEvqJJ5fw75ovLdQ8y4BH0vWWzdWX_-RFM5UCmLj5tcsqsgxiMOmWV6gax9Ky3j_OIJu1YrG9Ydq_Zy4nXH2XuYial0gHpQxRx0qLTtjyFLM4kuhlAcZrVrcwjqxQxr71js55opH4yD48RhEXEuk1g1pCFYfRIAMYXzHkUTQO5L2U3i0jJ4ylT7KPCkKzVERTZ4__UP1BtxY7iakThu_ZOJpWD1mZnUAvPEK6h7dncYYrLReQlWz_dFMItIW36-33ohPv6f9TDzJwVPeQmut8VaUXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان Pigeon یه فورک از پروژه تله‌میرور برای macOS هست، که از طریق اون میشه بدون نیاز به فیلترشکن یا لاگین در حساب، به محتوای کانال‌های عمومی تلگرام دسترسی پیدا کرد.
👉
github.com/MaroMushii/Pigeon/releases/latest
💡
t.me/PersianGithubMirror/4500
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2296" target="_blank">📅 17:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2295">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G1SoTsAqbGNWPSRt9iVcS-abxL8M6sCDIEcdtHOnN_BIrenSYBRM1ALIUYqKKdZdb7iQYStjc_bXywg2_B3vNuGEh4G3TDj0UzpioTz97yXpKBpqrfqmCON7_g2S3XpOBw5zmSKIv1PWbXkxtOkxGI6VX-9ImyCoQxk8BYXBXh42bYa38Z24chD8ax26SreJ5Ke8B55jI5IrRw9v7R-jp0g9mcW4HZQHm7hTq7nzDa9d7AEl5iLJsDfeNEytgpfuDG2eBL5pu4IcSyk5wytyguUJ8bkm-mUXLFcGH-BLmLwlay-jxUucV8SP_iahszpNqLueEEVXMtY7K5lTsx8OxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Youtube Sandbox با استفاده از GitHub Actions بهمون اجازه میده که فقط با ارسال لینک یوتیوب توی کامیت‌مسیج، فایل ویدیوی موردنظرمون رو توی فولدر Downloads (داخل مخزن) ذخیره کنیم.
👉
github.com/iphoenixon/youtube-sandbox
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2295" target="_blank">📅 17:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2294">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZZ1o5_7z3IYpreqS8frxOI30qM-nrMzpEhP2dJGJzdqbe8PVL2u0O48sWE83ReJ3d7012wfij66SQy4Cn_TezODw3mGZGriuNWZ_6vqUoiibOsb6s96sKagUiVjVsjTbcLlv4iNvUQeaaA4EiS4WRCaDYUsnszYOIuZDOF1cB_mwOm04ovrVohRA99A1KMJklAB_lP1urG5w_8Zf_lrIQnsmCLNkx3YeQg7m89mYYP_KK-7Q2Q7xR2wq1PuSCoKCuGJa6zsT44fe_w2LSC7l_VHkKeaCVMiDJtxmivY-Tx3JibPs9NklfPuUpl_WdSFNFJ5yry2rkY79dS2s2nS-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه گوگل براتون باز میشه و در وایت‌لیست اینترنتتون قرار داره، می‌تونین خیلی راحت با نصب این کلاینت اپن‌سورس به گوگل درایو در اندروید دسترسی داشته باشین.
👉
github.com/aleskxyz/Round-Sync/releases/latest
💡
t.me/PersianGithubMirror/4489
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2294" target="_blank">📅 17:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2293">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/URSzOiIZLZ5wuNvyJRrPEWGFW0eorDnHll5uJJ_rF2snWDjoaambCOLQJns1yoP5dnTASdjyx7twte1eVfkHcMG6Cd_WlElBVp1BpxKMYqpTDGtiZwyl5z-d3b7l8CYcfWwwg3o0BwZtc_MzCnrzdsvdiYJMTquVdmtYkEAhrbyF3o2Kl3vhBZy-IdYK7elt55QGKKjsDEBiOSvmxWkdb2ASnnSU-E0lVxgNxN94ONw0gkq5yg_eKPT0ecqG--m0ptwhDp9YJD-h1iZ6WopbCEM8IUhAvYn8ChPLI4PLVhifXWghENbDyYh8OEKTxnlEhxLVZhHpqC2ANMKW80GiNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید کلاینت ZedSecure از طریق گوگل‌پلی در دسترس قرار گرفت.
در بروزرسانی جدید این‌برنامه پشتیبانی از پروتکل DNSTT اضافه شده، هسته ایکس‌ری رو بروزرسانی کردن، بخش تنظیمات تکمیل‌تر شده و یک‌سری از مشکلات برطرف شدن.
👉
play.google.com/store/apps/details?id=com.zedsecure.vpn
💡
t.me/PersianGithubMirror/4496
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2293" target="_blank">📅 17:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2292">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">۷۰ روز است که جمهوری اسلامی با قطع سراسری اینترنت، میلیون‌ها انسان را عملاً گروگان گرفته است.
این یک اختلال اینترنتی نیست؛ حمله‌ای مستقیم به زندگی مردم است. کسب‌وکارها نابود شده‌اند، معیشت خانواده‌ها آسیب دیده و ارتباط مردم با جهان قطع شده است.
در سایه همین خاموشی، بازداشت، سرکوب و اعدام ادامه دارد؛ بی‌آنکه صدای قربانیان شنیده شود.
اما بخش بزرگی از جامعه جهانی همچنان ترجیح می‌دهد چشمش را بر این فجایع ببندد؛ چون واکنش نشان دادن هزینه دارد و سکوت، ساده‌تر است.
For 70 days, the Islamic Republic has effectively held millions of people hostage through a nationwide internet shutdown.
This is not an internet disruption; it is a direct attack on people’s lives. Businesses have been destroyed, families’ livelihoods have been harmed, and people’s connection to the world has been cut off.
Under the cover of this blackout, arrests, repression, and executions continue while the voices of the victims go unheard.
Yet a large part of the international community still chooses to turn a blind eye to these atrocities, because taking a stand comes with a cost — and silence is easier.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2292" target="_blank">📅 16:29 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2291">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">قطع طولانی اینترنت تحقیر اکثریت بزرگی از افراد کشور، یک‌جا و باهم است. اما این بین، گروهی که شغلشان به‌هرشکل به اینترنت وابسته است، تحقیری عمیقتر و نفس‌گیرتر را تجربه می‌کنند. با آن‌ها طوری رفتار شده که گویا شغلشان "مهم" نيست. حرمت ندارند و می‌شود با زندگی‌، زحمات، اهداف، آینده و برنامه‌هایشان بازی کرد.
©
DevYara
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2291" target="_blank">📅 16:19 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2289">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بر اساس گزارش جاب‌ویژن با عنوان "تاثیر جنگ بر بازار کار"، محدودیت در دسترسی به ابزارهای اینترنتی موجب اختلال یا کاهش فعالیت در بخش قابل توجهی از گروه‌های شغلی وابسته به اینترنت شده و بیشترین کاهش فرصت‌های شغلی در گروه شغلی دیجیتال مارکتینگ و سئو (۸۳ درصد)، طراحی گرافیک (۸۲ درصد) و ترجمه و تولید محتوا (۷۹ درصد) ثبت شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2289" target="_blank">📅 12:07 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2288">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tLc7tN-5U-iGue-rPUqkeAJEhiShHzYHPHxy-vFIi5RJzrZgaMdKvm7ve9KRWiZW8FpumFA6XFppCPt7TNBf9EV3d5JJoaf7zvllzraqFERpT0RJ_G8TlnPCPCB33j9yuey5CpXCPK49H6Ed9-9wUXPU-dfYLt-wr3VGc_e7u0cgLEx2cRepG1Hvmg8TjFX4y1-0TpfEpztKD9qfXST9lQy3Do6UGTikxuzTRIrU2CrhrBobB03aGTQWi2ZnJJMjURHmEY_H2ZXKfP8qRlNVJjV2xKpZDvYkWWvBBgIiWqD8BLEqO7G5LAMHN6UKLaXinCXuSxtmVLGXZ-oK_ElPAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی شاکی است که چرا با وجود اینکه که پول داده، تیک آبی اکانتش حذف شده و ...
در همین حال میلیون‌ها ایرانی پول اینترنت دادند، اما بیش از دو ماه است که یک شبکه داخلی که فاصله زیادی با مفهوم اینترنت دارد بهشون تحویل داده میشه و از دسترسی به هزاران سایت و سرویس محروم شدند. سانسور اینه!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2288" target="_blank">📅 12:02 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2287">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وحید فرید، کارشناس اینترنت گفت: ما تجربه قطعی اینترنت را در دولت‌هایی داشتیم که به ظاهر حامی اینترنت بودند. خود پروژه شبکه ملی اطلاعات یک قدم به سمت ناامنی دیجیتال است. کسب‌وکاری که اینترنت می‌گیرد از نظر مردم رانتی است و روی حقوق مردم پا گذاشته. حاکمیت با قطع اینترنت به جامعه سیگنال ناامنی می‌دهد. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2287" target="_blank">📅 11:58 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2286">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سمیه توحیدلو، عضو انجمن جامعه‌شناسی ایران، قطع اینترنت را از منظر اجتماعی خطرناک توصیف کرد و گفت: در زمینه قطع اینترنت حاکمیت هزینه-فایده انجام نداده و متوجه نیست چه میزان خشم تولید می‌کند. آنچه در این وضعیت تشدید می‌شود، شکاف دیجیتال و محرومیت نسبی و شکاف حاکمیت-ملت است. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2286" target="_blank">📅 11:37 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2285">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XgiBUxnwbzwE3VxRgzI45rlVk_ud1jVBFdfzuZuPUgoDrVaFapPMf1YN0DJ_sl9LF4ei6ZW85Jp-dczX_CZ423ihq0qpSWCeNd-3Yn9-vks9ZN309CCHo2Sh2NJzNVMCKldog90gecVPsCQoM6bW_RfpCof3cw467cTGbf1UXo2iTEdEh3yjT9UU_6jx21-V91EokM-63x5VkruZNgVIiU7KrwW_j4r3am7EGJv0af4ZP9E0D0vIUlSZ2nFnAM48yTbEkWW0TSauUsLOrSicfmbeW5lULAi04-sDrVyrln6Am8vVwawjCcK6DmCuJZHhi7e_L0uEbo9hwmabtk107g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای شرایط فعلی اینترنت ایران که روش‌های عمومی دورزدن فیلترینگ عملاً کارایی ندارن و اسکمرها و کلاهبردارها زیاد شدن، مدتیه یه مارکت‌پلیس برای خرید و فروش کانفیگ راه‌اندازی شده تا خریدارها و فروشنده‌ها در یک بستر متمرکز و نسبتا شفاف با هم ارتباط بگیرن.
طبق توضیح تیم دیفیکس، خودشون فروشنده نیستن و تمرکزشون همچنان روی ارائه و توسعه سرویس رایگانه. این بخش صرفاً برای وصل کردن فروشنده‌ها و خریدارها از طریق این فیلترشکن و حذف واسطه‌ها ایجاد شده و فعلاً هم برای تراکنش‌های رمزارزی مرتبط با ایران کارمزدی دریافت نمیشه.
در این سیستم، مبلغ پرداختی نگه داشته میشه و برای مدتی بعد از تحویل آزاد میشه، کاربران میتونن به فروشنده‌ها امتیاز بدن و تجربشون رو ثبت کنن و کانفیگ‌ها هم بصورت رمزنگاری‌شده تحویل داده میشن. البته محدودیت‌ها خرید بصورت رمزارز رو دشوار کرده، اما افراد خارج از کشور میتونن برای خانواده یا آشنایانشون داخل ایران خرید انجام بدن و فایل کانفیگ رو براشون بفرستن.
👉
market.defyxvpn.com
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2285" target="_blank">📅 11:26 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2284">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=jGH_21QRQE_dy3pCWDy4JKRvrfnVCTYpOT4VcUWAspMpluII8dwOzInV85KXh8q3qrG2kXnax6gRXiRAg0gFJhNAe2x9_onq2KI3zKoqspFv3d4R6Ca1FQJ34IzsbEXtaGQBo4082V9EZY6fG4Q4fd7urIh77WLuh1zpV8cyxhRO4O46d7MyRNNv7848_exkJDwDCVqtLNXkoHMXpA5yukttrk_cbntX0-dc4zWnDYTu6J-SIsanxbDsqajYS0h_eJIeUwL6sClz58J4GKsyopdQamFv5s0BanUmRJ1c69ehjeCVLy5fFRsKrupTtH3rl3dAJP1Qa28BrWptZY_muA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=jGH_21QRQE_dy3pCWDy4JKRvrfnVCTYpOT4VcUWAspMpluII8dwOzInV85KXh8q3qrG2kXnax6gRXiRAg0gFJhNAe2x9_onq2KI3zKoqspFv3d4R6Ca1FQJ34IzsbEXtaGQBo4082V9EZY6fG4Q4fd7urIh77WLuh1zpV8cyxhRO4O46d7MyRNNv7848_exkJDwDCVqtLNXkoHMXpA5yukttrk_cbntX0-dc4zWnDYTu6J-SIsanxbDsqajYS0h_eJIeUwL6sClz58J4GKsyopdQamFv5s0BanUmRJ1c69ehjeCVLy5fFRsKrupTtH3rl3dAJP1Qa28BrWptZY_muA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبقه اشراف و طبقه رعایا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2284" target="_blank">📅 11:01 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2283">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وارد روز شصت‌ونهم شدیم. میلیون‌ها نفر رو با قطع سراسری اینترنت گروگان گرفتن و بازداشت‌ها و اعدام‌ها در سایه خاموشی دیجیتال ادامه داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2283" target="_blank">📅 08:16 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2282">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DptYTZ9fdk4jS0tFDQEMyeA0ixSqhGJDd75BwLV-IwRdTxXyFZRaMxz_vLeghXas4InvCvQAGmGDhXTRmLtunqG0mH02DlaMhXAG5NIaB4r8qxE1kib_ffH5nyasEcF5IyAHGz1saw3jPbOzQemJrw6XAurVcBYsFPpoZzR62lRh1DOYYdV4H4HbehpJEGZ_ncvkrs1teJl6075PwMnWhJSZbLNvOqXSdS0IYIDrB1x_uOf_nxVmgxoDZYrDWSKoDpqgEhMasDBAAaKXT_9o1exNoUPhWoxyqDgKQ_-Cm93YBBGDyUBHoJGGqq1aRa4KTVqSEoCSU8rQdXflGqOxig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از اپ theFeed امکان فراخوانی محتوای کانال‌های عمومی دلخواه فراهم شده و پشتیبانی از اندرویدهای قدیمی‌تر، حل مشکل رندر نکردن نظرسنجی‌ها و ...، بخشی از تغییرات جدید هستن.
👉
github.com/sartoopjj/thefeed/releases/latest
💡
t.me/PersianGithubMirror/4273
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2282" target="_blank">📅 18:20 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2281">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O8rgF4SQAt_F46cGObr0tF5c7rYdl_fVLxa_H77v4_P5Zsst_zvCN-4ZnESpICf3rD_oTHNFo1T3kiroHlRB4xjP2LRfA_H0vnGo5Q-gWsKg3irCpRn2fp_iJTbfb9Yj3iPATRg_IDiR8LMkgvIMQpGZZptu1fd4Kuhl8j-mUUhXRupgvFcUUEzhNbtTRp-CORqkWk8i4TB75sUMxchzVvavfMoirUwZD89JShCOMZMN_kKjsIAm5ypRZoyyMTovWkaXnbJwJyMG0Lpj_kNwyl_D8sKw4JiRQTGPGoi5ik_U3ul1WiihP6B_-OjeIWINbENvJI06gCcAg-SZ8XWPMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای آسیب پذیری اخیر کرنل (
Copy Fail
) فارغ از اینکه آسیب پذیر هستید یا نه، آپدیت کردید یا نه و کدوم لینوکس و چه ورژنی هستید، همین دوتا دستور رو واسه محکم کاری بزنید و تمام:
echo "install algif_aead /bin/false" > /etc/modprobe.d/disable-algif.conf
rmmod algif_aead 2>/dev/null
ریبوت لازم نداره، ضرری هم نداره؛ چون به صورت معمول شما به این ماژول کرنل نیازی ندارید.
©
tiosus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2281" target="_blank">📅 18:11 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2280">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">قطع اینترنت به بهانه امنیت ادعای مزخرفی است.
پشت پرده اینترنت پرو و سود حاصل از این رانت در جیب “ستاداجرایی فرمان امام” و “بنیاد تعاون سپاه” می‌رود.
حدود ۹۰٪ سهام همراه اول در اختیار شرکت مخابرات ایران است و مهم‌ترین سهام‌دار مخابرات هم “کنسرسیوم اعتماد مبین” است. این کنسرسیوم متشکل از “گروه توسعه اقتصادی تدبیر” وابسته به ستاد اجرایی فرمان امام و “شرکت سرمایه‌گذاری مهر اقتصاد ایرانیان” وابسته بنیاد تعاون سپاه است.
در واقع گردانندگان اصلی این مجموعه و به نوعی مخابرات و همراه اول دو نهاد ستاد اجرایی فرمان امام و بنیاد تعاون سپاه هستند.
©
yasharsoltani
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2280" target="_blank">📅 09:22 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2279">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">۶۸ روزه اینترنت بصورت سراسری قطع شده و در همین تاریکی دیجیتال، بازداشت‌ها و اعدام‌ها ادامه دارن.
قطع اینترنت فقط خاموش کردن ارتباط نیست؛ پنهان کردن حقیقته، اما خون با هیچی پاک نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2279" target="_blank">📅 08:21 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2278">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Shw7PMZrioT_YvBnkTdc61gvg79CFbl_75tTeeHbemMgPJD_EVsvKeieu5REC08ndLyqR-wfbNg0WU7XjOi2JmH-o2iBGEgdqil20L3831nT2NiOxr7HnHGjWYItN_BclScOk4MSTZifqsqubsIkVEwG-KEY5OsqrGyW-RzAqM1R06NRAqTvYSfaHbuFAh8aszKCOXzSs-qHmIOfaEL5-Em6ttEhmBUogq3n2yXev4mqzeAspG9XKea9_oUVgUr95CYSNjjzOKgsVLby42kZyqBOzlyFgplwJ6O1KtfKKmGipto2v5G6JBA8li3GA5QEucSVZm4KnJTQ6dKKbbLIRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۲ از اپ متن‌باز و رایگان TeleMirror برای دریافت آخرین مطالب کانال‌های تلگرام در شرایط محدودیت شدید اینترنت منتشر شد.
در این‌نسخه بیلد لینوکس و مک هم در کنار ویندوز اضافه شده، برنامه چندزبانه شده و یه سری از مشکلات برطرف شدن.
این برنامه فیلترشکن نیست و به وایت‌لیست فعلی اینترنت متکیه، بنابراین ممکنه روی یکسری از اینترنت‌ها کار نکنه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4295
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2278" target="_blank">📅 20:49 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2277">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C5Mhss-ufXcOPXd1hOQzxx6Ji_Km0RKG6AnE-riCBkCyPXkhDA1t6x1SIk-33vGImhlUuOG7obUvH9afQ41dJa0XScohAUve8J1ihmkgKiskt77lGnzG83_tHbZzP8C-syPG-XVTnxneyJNFtSwOfE9Hy1CDbmA3vWPJA8KQSi5E6Xepwjo4XWV7BqcUWt2y3xI6l-n2zdNeBj_2mxnMUhwMcHBIpqT4aXL7UZafTpZx2soDC34rO1OznjZJge2laXrdQChQA9ODoiZ1S40zXkb2h-ffmKT1RaG-0zbazIhj2cBmV4tP54HfPIXkD25529u9kcy2UnTj6AM4ks_Q0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک آسیب‌پذیری بسیار خطرناک در هسته لینوکس با نام Copy Fail (CVE-2026-31431) شناسایی شده، که به کاربر عادی (حتی بدون دسترسی sudo) اجازه میده تا کد مخرب رو مستقیماً در حافظه (RAM) فایل‌های سیستمی تزریق کنه، بدون اینکه تغییری روی دیسک ثبت بشه؛ به همین دلیل بسیاری از ابزارهای امنیتی قادر به شناسایی اون نیستن.
این حمله به سادگی و با پایداری بالا اجرا میشه، میتونه برای فرار از کانتینرها (Docker / Kubernetes) استفاده بشه و تقریباً تمام نسخه‌های لینوکس از سال ۲۰۱۷ به بعد (Kernel 4.14+) رو تحت تأثیر قرار میده.
اگرچه با توجه به وضعیت فعلی اینترنت در ایران بروزرسانی کار دشواری هست، اما توصیه میشه در سریعترین زمان ممکن سیستم خودتون بروزرسانی کرده و وصله‌های امنیتی هسته رو نصب کنین.
©
Bamdad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2277" target="_blank">📅 17:02 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2276">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gehMOzIwr-gue48Ah000Dgpg_CuPlHcc8NOHRtLvtftnf0XHKtq4ad_vvnCiV-UlvwMVjbZ5Wa3RZGXR5QzzGtGU3L6Qq6DA-j8xcqSLr61vez_SXdfkb8wC_6trqt4Ihc3A_j0zNQpQdgPg402u6DTswuBOYw-xThC7thsSNmGDt1VoVyNeGQGjCx7_7LoVB7IZTIRRojeyz5N8AvXSheWu5zHQfOCK9WNpQ4y123fyu8T1xkADqH8JGZR6DE9hLlQbf9FRBFwcIF1_3L-QMjf0IQVfoWW3OqPiNWXHmpq178KD1KP-HfrW6o70CxTlYXrJpH2ZVg2_I7yvNKqF2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل آموزش ساخت فیلترشکن شخصی به کمک گوگل و کلودفلر از طریق متد MHR-CFW منتشر شد. اخیرا یک کاربر فورک جدیدی از این پروژه رو به زبان GO بازنویسی کرده که مشکل سرعت پایین، لود نشدن برخی از ویدئوهای یوتیوب و همینطور یکسری از خطاهارو برطرف کرده.
👉
github.com/ThisIsDara/mhr-cfw-go
💡
t.me/ircfspace/2259
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2276" target="_blank">📅 16:49 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2275">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">توی خبرها دیدم که دستیار ویژه وزیر کشور گفته "محدودیت‌های اینترنت احتمالا تا ۴۵ روز دیگه رفع میشن"؛ بنابراین بنظر میرسه باید خودمون رو برای کابوس ۱۱۰ روز قطع اینترنت آماده کنیم!
😐
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2275" target="_blank">📅 16:42 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2274">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t3kgMyIHo_JAeVvQ9WhXnzl3OL3_fK8gJX5qCNskNdcYiSm0zUd4FrTeFSytcXexHxbLusfPd0yMT9HjlbfZ97Jo4vGInDmf6c79yDNHoIidXuqY670ANW6SL9sdFf9VXWWq_N7RjyB7xoI0mW14Z0L-riok_xcv4udwcZdWkZR_Uf4ZthICzZWJB8samKOubxOG_ki5nUyV8WIRIG_dWZaocpxtsEsJ1kviqh82A40jaCHPijLwqXDIfjU8Zk4AqlTpG83rB_nJ0aqGVuinfIF8z149yWdrCMVTk9_0vhk61gPPP6umBsBv46tO_eSCxYrxKv_WgF1yDCBERZMctA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز خبری در رابطه با قطع اینترنت سفید خبرنگاران توسط ایرانسل منتشر شد، که روابط عمومی این اپراتور گفته نقشی در این ماجرا نداشته و "هرگونه قطع احتمالی دسترسی متفاوت برخی کاربران به اینترنت، لازم است از نهادهای تصمیم‌گیر پیگیری شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2274" target="_blank">📅 16:38 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2273">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eCXlnII_hHiy5lAI6IskeObQMTVRgKmB_vspTwgu2wnZwufKDNToSbsKa02aWQaduFOt7q6CFQl0Z_90TdguUw4vpBUDbQW2YK7cXNcgo1h-osbb4_AlYAeIBLm28UYzhV8z3Wq1JFR8OC5oo1-itCfccRqAIqcK5yuKJCQi3Lk6F2XJxd43guGv5jBo4VHT8qubq0A3xYNwvv7G1nND0qDTJxc-e8VM_LUOEoiG0jkiD0FkqtyjYoI00Bej60oMrBIl0EwvwqvN7AkPNvgb0HnINxzsc6etw5SQsf6n7AoTUVO7NDaTX5KF-1mbIXR5AAUlVC09z0B6JcjV3gHxFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع اینترنت در ایران اکنون وارد روز ۶۷م شده است. اقدام به سانسور دیجیتال، پرده‌ای از سکوت بر افزایش گزارش‌ها از اعدام‌ها می‌افکند و قربانیان را از دیده‌شدن، پاسخ‌گویی و حق ابتدایی شنیده‌شدن محروم می‌کند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2273" target="_blank">📅 12:26 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2272">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">توسعه‌دهنده اپ SlipNet متاسفانه از توقف توسعه این اپ کاربردی خبر داده و در بخشی از توضیحاتش در مورد علت این تصمیم، نوشته که "توسعه ابزار آزاد، رایگان است اما بی‌هزینه نیست. متأسفانه در جامعه نرم‌افزاری ما، فرهنگ Donation هنوز جایگاه خود را پیدا نکرده است. از سوی دیگر، جنگیدن همزمان در دو جبهه (فیلترینگ از یک سو و خشم و کامنت‌های تند برخی کاربران در روزهای اختلال شبکه از سوی دیگر) توان ادامه مسیر را از من سلب کرد".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2272" target="_blank">📅 12:22 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2271">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کاربران میگن ابلاغیه‌های مشابهی رو از قوه قضائیه با موضوع "پرداخت وجه و تسویه اقساط"
دریافت کردن
، که توسط "نوآوران پرداخت مجازی ایرانیان"، یعنی نام تجاری دیجی‌پی (زیرمجموعه دیجی‌کالا) ارسال شده.
با توجه به اینکه ثبت اظهارنامه آنلاین از طریق سامانه عدل‌ایران امکان پذیره، احتمالا تعداد نفراتی که پیام‌های مشابهی گرفتن اندک نباشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2271" target="_blank">📅 22:24 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2269">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oG3Ej34zViSPnW91UsMaeetaDL3pfoouu81k74D23qsYzK24iUS8CXL4TH7r6x-jQXr2HNnRQ5PglwUoMOgYlO9EojxzRDKJoMtN3twVBaFVW9RRrK4vOkWYbY5WmQGsCYFC_CBKqaKi6jjD5FesBteliRbyTUUWyGdyP0NCm8NC8UZu4rzJpGrqCMqogAIVZzGab_6TaY6aNkTgJsjjh4mbFrY29L7oWWJZjWPyFSSMuDQU0BeYza9zv6kD8mYOpPyO-liOEL13TNBHkHOBqQ5OsBPeVJBmE07qAoMgIIy-gh1i_B57gL9OZJBjoZ8MP97BX_dJ7YcTGAkZ56gIbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبری که امروز در مورد "ثبت رکورد ژاپن در رابطه با سرعت اینترنت" در صفحات مختلف منتشر شده، مربوط به حدود ۹ ماه قبل هست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2269" target="_blank">📅 22:15 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2268">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jpsfkdt_e06hDdDOWQ7WcWoTmb5NCWNfKDyWOrO6dArkRz6n5bMUjxLOPb9H32bHqmSnXRgZSvrDevOzB-x29AvEJD-gECLQJF3qqu_E5ek6P6QUZPFVpCIyAVXyfQ3kOjXy-SRBAfWW8RB0KdoSmjSusiH1DSAhN9snNya-odf9bKoZ3zeTFoeZP5m0jsmc_pJQvmqSqLOSXTdvaD3etExwQ-GAol0bya5YzdExZow6D08EIo2Gu_ae0ounRJVKvunFCvHHvJyw93QKboGwiuBcP3YizlqnmGT6WyEenA7Qr8Bo12076CzqukIQ1ul1vcNm3x_AckUEdXKJtbUvPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیجی‌کالا خیلی اوقات در رابطه با خسارت‌هایی که بصورت مستقیم و غیرمستقیم به مشتریان و تامین‌کنندگان وارد میکنه پاسخگو نیست، اما در شرایط جنگی از طرف سرویس دیجی‌پی بخاطر ۲۰ روز تاخیر در پرداخت قسط اظهارنامه قضائی میفرسته؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2268" target="_blank">📅 21:57 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2267">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PSCsGRB2_MXvUpu6XpJM24p4IVXu7k3KIJrABTx0kwZaXuCNLkFZ68Sa4a8OkW4rJWQLsADNV41l13hd4nqYV57NmnNFKm6VSG1N_n7hawyP47zzg72XzG8NjZpCMDGgDJXfW1o50_EyMcWf4wFfPRjCG7zVjXXHILlr9K-zpdLlKEmy_cqC6wBU_dbBVCv8qDyUrMfu_pUtSwQxQmG_Bwhg5ZEALuK0hN6-Ox30pHAUfk_TOBbT1PompAZ3AEHDwXZ2F7jgvZBbNIeoqE0kHPRdY2ZAKvyHzRUqNG9Zt51FsJDsNooO2JHWpzvM5JpZ6PVf18kNFTouj86iaU7Ybg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ TeleMirror یه تلاش آزمایشی برای دریافت آخرین مطالب کانال تلگرام خودم و سایر کانال‌های موردنظر در شرایط محدودیت شدید اینترنته، که سعی می‌کنه با چند روش مختلف پست‌ها رو بگیره و نمایش بده.
این برنامه رایگان و متن‌بازه و فعلا می‌تونه برای دنبال کردن اخبار تلگرامی بدون نیاز به فیلترشکن، یه گزینه موقت و کاربردی واسه دسکتاپ باشه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4128
۱. این برنامه رو برای کانال خودم نوشتم که در لیست بصورت دیفالت وجود داره، ولی هرکی میتونه سایر کانال‌های موردنظرش رو وارد کنه
۲. برای اینکه ریت‌لیمیت نخورین پست‌هارو برای مدت کوتاهی کش میکنه، که با هربار مراجعه یک درخواست به سمت تلگرام ارسال نشه
۳. به وایت‌لیست فعلی اینترنت متکی هست و فیلترشکن نیست. ممکنه روی بعضی از اپراتورها جواب نده، یا خیلی زود از کار بندازنش
۴. برنامه دیتارو از کانال‌های پابلیک میگیره و به هیچ اطلاعات شخصی‌ای واسه تلگرام نیاز نداره
۵. در حال حاضر نسخه ویندوزش رو منتشر کردم، اما اگر بازخوردها مثبت باشه برای مک و لینوکس هم ارائه میشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2267" target="_blank">📅 19:53 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2266">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">در شصت و ششمین روز از قطع سراسری اینترنت هستیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2266" target="_blank">📅 08:59 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2265">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Um5Rbku3Dh85jvcI2SXVrKBsyN_gxW4BUyeG6044rNf8qzbTXpOIPdQ63uVJ3iZA2kESOckVaNqyjCREvy3XEoXaD1cRuYX4WzSoS-3WpAJFmTWC_CxIo-Qz40PMuQgKNi8r3-yBTC-Ndyixzm1EF1nxXCA88FF2V8lVNzKbsWvA2Z6oQ7544iLL5u-knL-8jrrqMUTzRCKExa4OUSjgJrD-ScuJV0l4GioIKhfMdEG0d5gVt9uvyPV_ijNDKrW3M8D_CyFDAY6FRAZirHT7PUIeqqsjO_GZyl5SKTehXIScLLfuzrzzmWSuoCqDwQIVu35i4r5Wanr63g9jZk0LgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی‌بی‌سی در گزارشی گفته که شبکه‌ای مخفی در حال قاچاق تجهیزات اینترنت ماهواره‌ای استارلینک به داخل ایرانه، تا کاربران بتونن محدودیت‌های شدید اینترنت رو دور بزنن.
در این گزارش اومده که افرادی در خارج از کشور این دستگاه‌ها رو تهیه کرده و بصورت پنهانی وارد ایران می‌کنن، تا دسترسی به اینترنت آزاد فراهم بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2265" target="_blank">📅 08:53 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2264">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انجمن فین‌تک در بیانیه خود استدلال کرد که رویکرد ایجاد اینترنت طبقاتی، گره‌ای از مشکلات زیرساختی باز نمی‌کند و در عوض، اعتماد عمومی و پیکره اقتصاد دیجیتال را با آسیبهای جبران‌ناپذیری مواجه خواهد ساخت.
این انجمن از نهادهای تصمیم‌گیر، به ویژه وزارت ارتباطات و شورای عالی فضای مجازی، خواسته که به جای تعریف طرح‌های تبعیض‌آمیز، بر بازگرداندن کیفیت به کل شبکه اینترنت کشور و صیانت از حقوق کاربران تمرکز کنند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2264" target="_blank">📅 08:51 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2263">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jvgeAzgomw7S4x8D0bBTVMZBVCOD8KdhEp9Cva2FGpw79HpSEjxI5W0zQt-mrW3M3Vo0I2pZSiLT_hZSzT0Q6Yb3BdhGb9t9H31Xbmd_agr7QllT-ZzEbFSTFTVfZWuMD953UquKpKlm6jCHqZFyUpL1681qmXYNroA0fVf9unR2mNgsdbcP6gnCIONMyQl8uCYzm8aQRDPWWGeGS_8pCM3HmOAgqQ120jlR0IRSY7BIBiOz_ZUo-Z8jrodUS2YU98Y9R97ZLviTUEwW-giJ_tJNe-2KXAsfKBD4qqsEJn4IWSwzvFQgjgCao6SfwZsDb87wasJWm6Snch3xgmNM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: داده‌ها نشان می‌دهند که قطع اینترنت در ایران وارد شصت‌وپنجمین روز خود شده؛ این در حالی است که نگرانی‌ها درباره وضعیت حقوق بشر در کشور رو به افزایش است.
از طرف دیگر دسترسی گزینشی و سطح‌بندی‌شده برای عده‌ای خاص برقرار است، اما عموم مردم همچنان از ارتباط با جهان خارج محروم هستند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2263" target="_blank">📅 11:13 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2262">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بلومبرگ در گزارشی نوشته که قطع طولانی‌مدت اینترنت در ایران دو پیامد اصلی داشته؛ از یک‌سو توازن قدرت رو به نفع نهادهای امنیتی و نظامی تغییر داده و نقش اونها رو در مدیریت امور کشور پررنگ‌تر کرده، و از سوی دیگه فشار قابل‌توجهی بر اقتصاد و زندگی روزمره مردم وارد کرده. در این شرایط، دسترسی محدود به اینترنت نه‌تنها ارتباطات و جریان اطلاعات رو مختل کرده، بلکه کسب‌وکارهای آنلاین، تجارت و خدمات وابسته به شبکه رو با رکود جدی مواجه کرده.
برآوردها در این گزارش نشون میده زیان اقتصادی این وضعیت فقط به تعطیلی مستقیم کسب‌وکارهای دیجیتال محدود نمیشه؛ اگرچه این بخش به‌تنهایی روزانه ده‌ها میلیون دلار خسارت ایجاد می‌کنه، اما با در نظر گرفتن اثرات گسترده‌تر مثل اختلال در زنجیره تأمین، پرداخت‌ها، تبلیغات و کاهش بهره‌وری، مجموع خسارت‌ها میتونه تا حدود ۸۰ میلیون دلار در روز برسه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2262" target="_blank">📅 08:37 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2261">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">روز شصت و چهارم از قطع سراسری اینترنت.
لعنت بر جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2261" target="_blank">📅 08:35 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2260">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کاربران شبکه‌های اجتماعی از جان باختن حسام علاءالدین، شهروند ۴۰ ساله که گفته می‌شود «به‌دلیل داشتن اینترنت ماهواره‌ای استارلینک» بازداشت شده بود، خبر می‌دهند.
بنا بر گزارش‌ها، او که پدر دو دختر بود در اثر شکنجه در بازداشت جان باخته و پیکر بی‌جانش را به خانواده‌اش تحویل داده‌اند.
©
indypersian
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/ircfspace/2260" target="_blank">📅 19:31 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2259">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نحوه ساخت فیلترشکن شخصی رایگان به کمک گوگل و کلودفلر، از طریق متد MHR-CFW ...
📽
youtu.be/L3lJZrAqqUQ
💡
github.com/denuitt1/mhr-cfw
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/ircfspace/2259" target="_blank">📅 19:22 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2258">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g8-XJMie5rXu_QgxzJ9O4BvoX-_fWtH9p-kVfRU1oSqkYrmbKBSWscWwhRVItUNF_7SKyl4sB976-1gtmwIKEpQhICFq1qMrCFtYNJQcnYzcwi6GGa62W5SZpE_TijKdXfNkbGzQNXcns394MFWimmP9CXtEnJizchkNnzc2gZKXY007YSJWHLXuYq2NKtKapvnanMbXZSrCOkxcODGlFU_hLbQDsx7wcsZhv9muk-88U42Uy5ATc9MB7Ha7-R8dpG1Yw-ol_J-KObZxAWdpCnW5_pvHy7nBOHAvqQ--2q7JYZAkC90_GgRvTgTxxzCF5Td8XgGhSdSJKoBxqP6q6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با روز شصت‌وسوم از قطع سراسری اینترنت در ایران، گزارش عملکرد سه‌ماهه اول سال ۲۰۲۶ شرکت Meta Platforms منتشر شد، که بر اساس اون تعداد کاربران فعال روزانه این شرکت به حدود ۳.۵۶ میلیارد نفر رسیده و نسبت به سه‌ماهه قبل حدود ۲۰ میلیون نفر کاهش نشون میده؛ هرچند این شاخص در مقایسه با مدت مشابه سال گذشته همچنان رشد داشته.
متا اعلام کرده این افت فصلی عمدتاً به دلیل اختلالات اینترنت در ایران و همچنین محدودیت دسترسی به واتس‌اپ در روسیه بوده. البته در پی انتشار این گزارش، سهام متا با واکنش منفی بازار مواجه شده و در معاملات حدود ۷ تا ۱۰ درصد کاهش یافته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2258" target="_blank">📅 19:13 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2257">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بعد از ۲ ماه قطع سراسری اینترنت و شدت‌گرفتن تعطیلی‌ها و تعدیل نیروها، پایه حقوق وزارت کار بنابر مصوبه شورای عالی کار ۱۶ میلیون و ۶۲۵ هزار تومن تعیین شد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2257" target="_blank">📅 17:39 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2256">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انجمن صنفی روزنامه‌نگاران در
موضع‌گیری
خودش نسبت به اینترنت طبقاتی و حق دسترسی به اینترنت آزاد حرف‌های درستی مطرح کرده، اما خبرنگاران جزو اولین اقشاری بودن که به اینترنت سفید (یکی از
سطوح
بالای اینترنت طبقاتی) دسترسی پیدا کردن!
واسه همین این بیانیه بیشتر شبیه یک موضع‌گیری تشریفاتی به نظر میرسه، تا یک مطالبه جدی و فراگیر. اگر رسانه‌ها واقعاً به این حق عمومی باور دارن، اولین قدم میتونه شفافیت و انتشار فهرست کامل خبرنگارانشون همراه با وضعیت دریافت یا عدم دریافت سیمکارت سفید باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2256" target="_blank">📅 17:33 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2255">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lUqLHU0kO2vz-IOi0djhYCHys9V4kRsu30p2EIeh3Q0DaXX-5Tqk60jFMZg-t6SDdmb-OwmHdVi6npPfJ8urkxwgmJtg4cWpC7YET2RhKl4tthKgZJs5Rd7wkxRj9FMGTkAI_6NdZfOsdudYqqMbbJw0aOTA2tqaQJYMTE7ElPaeh6dbrfMlBJPufbFAVZqt7YN3mbQXqU4nfkwWyPsDHEC-XgkPRjbhtyiLnvXz4IGjERcJBrwkUAZnac7vDg3P4j84mPBhI6FtsULzjP0omLhe28tz7LWfyaeSFPWgb66NB1nOXKg4ANMXIj5FPcRZcX0mZr3r_JowR9xm7H771Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن صنفی روزنامه‌نگاران استان تهران با صدور بیانیه‌ای تأکید کرد: دسترسی به اینترنت آزاد، باکیفیت و همگانی یک امر تشریفاتی و لوکس نیست، بلکه حق عمومی است و دولت‌ها موظف به تأمین آن برای همه شهروندان هستند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2255" target="_blank">📅 17:27 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2254">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ttxX1QlCaCpXx55wQsGGn_OE5YksA8oA2K2nfDYxuIJ08OurraE5g_vLuJg-FLZ-fFQB63U4-xr5hTHzSKmZMvRgdSNawJymnQeqGU3tixH5TtiKr1zFQf_QVmzws9g8t9OYomD878Yysyqeb97Xlybk0V27abAm31RGJxKznCwPgAyKEjH_jA8JGuGS_K6LLWwzLsqAAz0ya068-V0wFvTjJowpiAx_dRwPfhPvbgoDkweKXKyOZfNugBQfcvxxgRSTkouqe0--hXZY35slOMtvWUnkjTOPEkmzUeAZo-bPLUpIqRrKhfyUTFZmvNQ3SQurTghOImAGb_MQZ3nKJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایفون در بروزرسانی جدید اپ اندروید Conduit گزینه Personal Pairing رو اضافه کرده، که میشه یک لینک اختصاصی دریافت و با دوستان یا خانواده به اشتراک گذاشت.
این لینک رو باید در داخل اپ سایفون از طریق بخش Pairing URL وارد کرد، تا مستقیما به ایستگاه کاندوئیت کاربر موردنظر متصل بشه.
البته با توجه به قطع سراسری اینترنت، فعلا سایفون بصورت عادی برای کاربران ایرانی قابل استفاده نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2254" target="_blank">📅 17:15 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2253">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rYHskY_gP_yKSne2wSqOw5dTxtQMf6O4zcmc032cGfocJ11VbTKtLhJTSNkmS6tWero8-9dFs7tLtC6MTspW9lLUpHVM9Y4HD20mSZWAR5roIPlVur1jiuCRXlVsxafx5Pj2Thbptj2RBLKD9-xYdpC8pn3ZHUddppU0oWysjbhQJPbCtdQ4r3P5jD4WzAGp61no7CIh9l7P7jL82udb_OpMGVASpLj6V5p0QbI7bL55kI0FYI_qAW8MXBS0U7cguwxyFeNxE_5tMqWOu_Zt7QblpKsUZeXLBGIIkYCUQraJvbW0lM2fshTC9z8l5P6y5SsrNd7R-CgNzmzHxJ4vpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش تازه سازمان گزارشگران بدون مرز نشان می‌دهد ایران همچنان یکی از سرکوبگرترین کشورهای جهان برای روزنامه‌نگاران و رسانه‌هاست. جمهوری اسلامی در میان ۱۸۰ کشور، در رتبه ۱۷۷ قرار گرفته است.
©
dw_persian
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2253" target="_blank">📅 17:03 · 10 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
