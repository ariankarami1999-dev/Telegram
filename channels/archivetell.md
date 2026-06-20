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
<img src="https://cdn4.telesco.pe/file/JwrmCitxYlfG27FkdPHE1LcuQ4_hMLryhFdp3lzxW0icrN4M7lGelSdS6ahHH8RVwl1B9JFQt_kG8Ou9orALZZmVN4KMI7enba7l0CIKOkLTDgCbpaan1SaCDUmPR5y9TDCWdz_l7DWA0s0RGAuBHs1EE7ydmoZH1FdkdD73n_-nuzuFAJiMv1i7xwIpGR47tugqhyuxQF-p2WeAqy4RtBzaSccSYrYrflLlDQQyzdRNvbGt0w2gNotPbH_ykVmjxymz5sYDnLBzXaRlWJjOMNXQ3DyyBZ2RutZc5HJiic9C4IwoAUk_TvJZ03IiWwYGRn-v7-m884TZGB9hRJSXRA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.65K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 11:47:27</div>
<hr>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 818 · <a href="https://t.me/archivetell/6456" target="_blank">📅 10:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 979 · <a href="https://t.me/archivetell/6455" target="_blank">📅 08:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/archivetell/6454" target="_blank">📅 02:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/archivetell/6452" target="_blank">📅 02:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/archivetell/6451" target="_blank">📅 23:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/archivetell/6450" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6449">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/6449" target="_blank">📅 19:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlL-DFNuxP4oeTEcZSH_d7UYw9E69hLwbUMdvY1fgXbGoNHMm4rz92ZDf631NmvV3usa3hVZfJHM3cNCqlnytibnqMHenXcqCpunWaWYMPfsvBtyiBVpHPn_JS9yWVISgsUxRYf12nAcq0UlvZinI1H5vr30c80lpnhJWrXEOHcN7TsrprPw0IddSQFQHL0Q5ZFYNIyNYZkzPZ-lrtzYVd05aYEh6R813lgRPW5FwQGsM4d3mVgxSS7QFXQsxA_OwwYDMae3BgzGDi4_qi4f7ovuS3f_ILESrYtGxd76huQOHImlRc2vtpnfF1fR2qJJ_DNgWuKMJ7s5J60Ux_rMBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اگه حوصله داکیومنت خوندن ندارید و یا پروژه‌ای داکیومنت درست حسابی نداره، به جای این‌که سر خودتون رو درد بیارید، یه سر به سایت DeepWiki بزنید و با کمک هوش‌مصنوعی، جواب سوال‌های خودتون در مورد رپوهای گیت‌هاب رو پیدا کنید. اون خودش داکیومنت و کد بیس رو کامل مطالعه می‌کنه و کار شما خیلی راحت‌تر می‌شه.
🔗
deepwiki.com
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6448" target="_blank">📅 18:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEuQIEbaakU1zr3ooaOx48JfjwJYMvhyfNQ3Ccg3J40pfhzaRTv2DvMj8S-18hR_5YWx2F6PBvFEivEzEJmlMnFynWcMLJ6BaHVwZ9lB7DCo6TibR73M2Pyi3dAucE-h6M6R_w3UwA1RXCnOpSfogembXmHyGm0Vc7UOXPx2MJmzBm0mMki_fz_W-3_WaGNhlgcJxrkAqkLrmu1N9XLlK4tGMW3wCKqoAa2hBxWdCkQqO46Cf9ANWbKbWR5ycp0wSA6c3UhHO7ub1AhCc0lqBFviRQd8tAhg9V2UdZXOm5y_zcqXU9n-gqcUGOrRo3GcByz_8y-B5pfIFtSnInd3nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت موزیک رایگان
🎧
https://freemusiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/6447" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6446">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6446" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TB3rvVZteb55DZj2Wy5Se9wWiLsGpXmGF-bz_hfpHSFPSJ9DUjdNdlnSExPZ-fAh_ptaSZjyoVtzx2szDwCySovIR9MndlRJSKx32kvrY_y06jKssz-zEiqxCcVNIuBovPrM66V4ng0OA6-TV-x-0AAjQtipKet0psnVwYRlqYqPbc_U05twPVtorSvRlqzAGllvZnIlCxnUK0icivE8V6YirjSL_6-uPgCn3K3I04HiBZ6EwM969FcaWnnsMDRicmTdPc-7Zx7k_tE72fdrjvGnCZ1AVomdFtx3ntu10E5QQ9xth3pRiVjfFa-Dy_ADxn_uawpFBxfyT9bUyCqGPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
۶۷ کلید ترکیبی پرکاربرد در لپ تاپ و کامپیوتر
⌨️
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6445" target="_blank">📅 01:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6444" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6441" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6440" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFMKPfrAYxwdXVvc3fqMS1dXl-B8eWd6X_nQCDH9IkOQqNV5JS1lOVVD5zlb2j_LBvYXPIDZ1kycOq7XZehWLIe3A_8NMW2RYfVydT4QVs6asg5L57UFCrWjfouQkUboPzEaCOGrhYux9za1gyV2-zpErwJZjACGua262QQhiBRJ8oj404jZICpYu6JUNpN8V0weifW0F_a-Zu0kU_zEDktSU_P4pUXFN2hjfPl3kPOkup_bfWZ3I1xbxah--euqp_1OqOhOJTh30_6DuSfbXVCHLQk2fYpOogkZwBxrrcOfM212-6QMMFdnLdtroa7Avl-1i0DjtlftkQN-idgSrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6438">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6438" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-WC6w9qnMCvEu8kp4WeYD_HvRlw9Iwbs1KJyvq-AysodwHQxXsxBtRr77X6-6xqqFu5B7QSILI615-Lqjj857WRw48SGrT27jVbHfxw6JFvDg2d1Ivp28QV5HzyKSwSzzP_VrHaGOsOpzZ7qd7izdLoakIvaQsSDQ-TarTYe_5Kqeo669VBXWXmPDBVDOv6AOXa7KiuPueg5ScoGiCkbxR_L4c4CXo5tqBfCD7n6TqjbCZdtXM66TUfivhuwi1qMgXhZH3SBlfSLqIwhb2x9Tf5AWYMzp6uTtBGnaLkvWCwqcWe_PDRblLvJ4dm4B7BnLL70_pjjzl4sGcwc6E2fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6437" target="_blank">📅 15:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6436" target="_blank">📅 11:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6435" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6434" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">با سلام درود رفقا میخوام یه ربات open vpn بیارم
دنبال پنل درست حسابیشم
اگه کسی پنلی داشت که بشه حجم و کاربر و ایناشو مشخص کرد ممنون میشم داخل کامنت همین پیام یا پیوی بگه ممنونم ازتون
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6433" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6429">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qo89o-cJJBoP2MBoVWdTHOY9s9P6KKdtKwGvTI9_hIbw006PjWqDJa-_2QkueTQRTz-4qQFBNjoKjbgzeeYmKmOAcyuqqIiuCf1_sblBbjnbAjGZ-0_OWijYXsyDoncQ_ozYwl4p-sKVbmkhmUwG5iVG73fSMB4c_p81Tg3PApVC-gnuNfzo2x2Um_uVIKuJAlFH0x50rXGpqZFWESZtTPn6SlaLDLbRK4lnDJlJP0QngXSbDoSC6Cxz2gpvj-eEMIWKmgJPVhCrdv924Lxizf4xw23t156kdSjMimaD1GOXghILYQQB3f9oE3EJEDJEBWURbEJEztFI9r3hwpEnFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IchWyzJMUB0M4q0kCvEGZ-ztTIdqFhhvoc8a5vaoFgMPuELPMvHWQKoQVDcFJkTHjGqYFPPP45ZfVzRvUxK-TR1Jw7H7sP9fEKJ-2sDwVx7Q3W3fXZwBCZWoGJXttHLj22Gzp3GaGqPAgCG3RaYIAyOW82ecR1-7OqkL875GbR_QCn352yBJXvtTqQAgPiYZXA1S8k4e7Oyjqk2oiy6bmsW55_7DYUi55tmuLmZyDrDg8d6eXx6-Q3fhW322_4d3mD7Yc8x_3JK0E52o2X8qpkjPR2weQzCR-dR5tDRaYl3aPiqbAgQaaiiBk_w88nDT6sPjGGmmFEosiHbkuIv76Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFDaXTO-W5-utXrTN_zQuLXT83vK0c_jPizZEb9vh5xjchmLne-g_XrhGoMFb0kxMRistha_bH5vQj1XvglSeCiLGnF7lzPjevhQMrIzKNXtnaM9bRnRoXPEs5EHDRVpeMJ7ug9NhDXtUWQQ77J9OhAk-6DzFHrzQd65os-BmO9XpSS4t-xLysEY6J-G75uDnlaHBbqkO0lSy7UOuGW4ART4seqRWhLzJdd0j4AT6z9SeJ9iOSPE7pbfGlk4mSY-aRpZIAITGCVvlO4BSZ6MzPTmhaWfHLaYUFkNZT28YIfTCEiEPaJSf14aG-LQJjJEYGuHa9U-3EcY7ciKesz8fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ds1lFJxPx55apwxZ5bkPIWMvRtA7K7_cz10DFpjA14bn68ry12XWGDHnS0OKKGtsUofguCyCBEwvcKKKSX9h86HeVMYoQH5TMCDw3V1ZGkUbrdD3bO4gXjUoTi5q4DzO6VMV2UAdl68Y_rI5KpakpOxScjbxRJhLIHs1CCX4aim25rTtAZaxY5l-rOSKnxbrURSGfqJ_bZB0Xn0a94LvPJ6C6_0w01_E-PsUYs4bvdoktNfZmhfVcgwXl9nbiI4C4mmpLybtGvILT3WnPJC4F9-UPvvxmIv3-0tmQC5v6LA6A3HcKzoPQkuYL7OwZ4Wd5_tLAjMFdHLV58Dn5h0hsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت api رایگان- GPT5.5
لینک 10 دلاری
ثبت نام بدون لینک، اعتبار نمیده و با صفر شروع میشه
وریفای کردن هم با تلگرام انجام بدین که تایید بشه براتون
با شماره مجازی نمیشه(چین)
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pa-K79iCvr-koDIMRHlHDUCYH0MPEwIbnImeOCOJmYhwZUq65F-pdFg2bn8e8KwHFUyB5vef__8qHKLKTFdygUhOApsJ_zZAHHbOptQJj95kCv48BS08FC_fJ5mYLH7126CZyZO4SXbop3c8TASKLt6Y_T65cZXfEC68VG1FN3klE0vCRUduKK-W-4-n6_KfMmtUhC4swPMMMqovDwcniH7uLW_sAolNDVZUJUqEH9YDCa8ofHEHpoOPs3WwXqvdrLJqPgUhGsNDrcpQ12uWS-WFJdilKGBAz9H1cJRjhPNiOFFnf4Cy7tPA6rNPl0jrYS6qh-XGKv1x4F6HpDE-Ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bh_ZcpUj_zm-s6PQeEHQIDJwSfJXy49otidN4zo7vsXVQup7yQ1qrmuxLiKYiu_IC_Z7n0FavY9O2aczJ-486MUp0o3eO0A94p3-zC3ok4P8JLLq0VESfGB3kh7ZW1JiD1KyVRoxMczdCkNSuHZoaitl5Vc6pSQp20pTugh711-XsGk2V57eMn_BHtJ3_5DDSGY_zw886gBSMrw_OQjcrpN86y5QLyzp97u0FSnrv8qOpe7IulaBa4vXye56N6-iLmJfK1YwFvH78jLXOQ7qMZI552emmgFFn6p9bEeG3DH7yRAvQP6Mibeva5gOPtc4FEPxsDG41dxlLzujDDDP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKcgj44qtEBsZF5rJ4a7vCbLFhO_KnhwsLVxzSs_JwjcOsuogfKMclJZ_KKGkn-2NuoYIvSK22DJ1DSwftdcaw1maf6oRodRXMiLML3MVYYTsTMc59nlO8uOukJ17UImJjeNqIRIWPV0dHwMLIaKPYty2Vw_mYWO2A8r78KZzEQO0hiCXJKOmUC73lMtwfcEIA2f_v-w7cPFV1F6lFxf20_zJPEaFBg_zaiX2CgjowoXizVEhGe6-PCQR5hvb1hoZLGjS7LSu7e17fdj32sdRTEkO89rI1JTRCn_lrB9C4Yq3jyUYxWcVIoFP6Ecw3kJNZqr8JJFzcq3IBjtGUGDmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dle9UyAW0fw-CtUgf4AmudmsRf7ati5EhDRXVwX84Cvi9Ej1W4E2b8r8aovRbJvgkxwaIsTjnOvcU7GGGZQEsRKUyfib_kSY8JsIeI9g6j0Uj1BBAH3ZxaO2q3GFzqbBAP__EdyDLiAlKceb5LIMwIqcaxUbY8pk0bcKUeh3XhwGZuJiZVfnsKPosyoilbHRVn7jRloaPvbTtVSLhtDQ5MOae3rbw-RojKIbY3gI_vh6QJI48gvX-K8zihHZDra0xd72ansyxAhGhORT0prd-p2OrrfP6Q8WvKpCFxoo_UPLeg2qaYsS8pydfcSKLxUbAHgjlMgoQ7IHKBzeiskqHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل جدید GLM 5.2 از چین معرفی شد  توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و…</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XWXgWhIO1zcKk-Q8r8qaxlLa4Dnq4jfGE_5PfpxnP0qJnJQckeutWFXKTQm5JR7zdqGEIV0OcmIjHJnb-gZCYyH8UB4BWhXCe9KebyWpIO-GJb7gmP_DobrDWOOvj08wdHAgLKE5VQvPj-wW5oKadpMgaUo6PB3Ou9v-WLPnoOAO15LwJIrJPDtjFw0lkNNyRm_0sQ73K3Epqg7H0XMxP7UdEkZlhhMs1K6sWoZ9w6SqEg2kXQRdbRrRJoL09HcspaHw_3dhUarjI1G4Iruq5yww2VhoCq2iaE-zbNEi3_w1ikG3FCP5AGlXng56aKSHXnUqq181mvTMtHn3x_8AaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGk4so9dYzVC84xsF4-h8R1d8sTJZm6JtWBT-eYHCIClTuJWDIrnadzP49y7NJZn7ob3NBRE876ERHA0f6N6cwTnfGmag19mm5qNbvZxc0I9WawnOMiD6M8LBAsVAmuUtw21FnbiLB8iN1tXWv1waPh3mDsObfZIR2h9KZEK7HRdehLZuE3tqdSyM7bTZB53MNQ52OkO0EuV8fCWmxml-dBCsVAu8-rnUjub0dOuKN37nx57bIA4xJzdiPSOYXevQs0LwhVyBsfHRy9mvtOOJ9OiOBx3u_IGkwT1D0hbE37HScpNduMSoU1F0I0sMX8oRLCoZJt_3J9C6UyS76SA3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ih4p-bmuRNTVDfISDNCxrUHnh7SKiBSPBKeUzr-siN0O9bvLmj5MDH_7qeYk24NnAWJTa3hSpm1bd4lPSI8YXCxtF0dCIJebAFK_cAh4Tlt6zalamMTDnFAHYLldPcJCz7Q1PCi0v5JO22ih9XsWa08yXw56oHmmZ-HTPb_Mw3wcyyVvhiDW3xeXkEM1WhIZufLELPCgNLeHAgfgcWTUV1zu5NgIKyZYhBF7W6C3Z0uo-hk_1aJF8xiCMkadsVzdlTmqPfNbl8MeO65RxYXKTkT54BDrSlTVlv3L_OSac8IAUNu6rTrwltGsCtlt0ooHN2PKpuBJyy1Cb9ujWLoxyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P48bgDKNQLE1qxcIszcwQO_zpMu3dEHBQ-Tru08KftUP0MV0HebQlWcuZqo16YonsM8R8twQMQxMpyveDSuOj-8wUV4WvAQiDASq2MS_-ZM-IlZ6ZaapWoujO6VcT6xhRdTfLyUQoweXRuQpA04b66Cv4JAVpm8RqUgQgdKlO-txhHlEKX6amrZPIRNgcyTSwac5pD2b18tLxy0rXLihCn78qaSWC5pGn-SwbTYtRLxOnHHbOsfQ-0zJQXi8UNrXWoQ18vcCSeVsPjGloJdWM8jq9ilgZRPrGOzbgG4A0euFJUTzDeVJDgfhWO4qfjkZ3sIW9YasfF0RSkKJlRmfEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CMEIzWzpWIZU6TM1kUO_ohPH6rGI_hL8ZZBq8L8T58lj2j-h0OFHXngFDSIIeTn8rEYYSPihy8lAZH1b4MHYxX8puvMDW5dy__YlJ4voxosAGuCWJDSKUsvbp29g7chxX8JYMVJKKn0yveM18NpicOF2cLN97JhmHtk-ok66bEbpWqA3_GDErSUo4Sth5u9iwXyZznzyxbyertplHqG1FqLsh9FLZlHX0VOB7SYOb3CPNt06ESbl-8_15malbR3pH_xTV6q8QceDw3uxYc8Id9PMi8yHNrfzxUsrUpYJ4EEG-0DEXaL8xtbn0qnTsy-EkNwXrXAUNMw4O8Od4RE7Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tIyez9BkJa0WeFyCn8gCFsAaaviajollutmnVPXKT3Z4GoVbNENQb9KSxm4oB9UT-A-Kb1FXZpS2YycyIGn-tjU1JdekjKO2HxRtqWLnppZ7dXOpdE7bXu8lUXF7yHactAmVpQtB5q3-by3I130ZDWP5KXJAnkBXy-Hn9cqXolH-8WOfE1tCSM3_hIZuR00Q3RPFjvLWzSGfAOPvmVJHMCb42iUpP7oWHHnSa-h7EG0cDhTTtAAwdNgKJqP9yCT6Owt4rQ8HAMxR32feIRiAx-WfK6zWbwdwXwXqF3B6M2RyIcmDyMnkLe7rSDcDBAJAe14H-n119P2hMepvmbbyNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=otPYkfoRjoldqQ_AFCA52GFzaQ9KtRVzxVIJ64jMM013XnXrsYKSHaqHQh870yokhpV-TwUvBiiJITkWDZBijrATRL8IJZCy8C-0pfrIWQywdbN5RlOnJMqplC5SHH-HJRhydyoth4lw40hi1mdLM_6AYPKdyeXInFL4mrwF-XR_dskSseFIWJOQNi_WqQjAixaiMhS9i8NxJhpI1NLHlbvetbB9XRvNx8YU9kKCxMckkgKSMshHO6xD2uBGz-FQvP_dP7VBKPX1BHQgOe01DDtlzKpKFEk3EXYEkNw6Hm2zW6ksV6gdlA3qCjznkk_dXlBL198QL6q3D1-WvNEhUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=otPYkfoRjoldqQ_AFCA52GFzaQ9KtRVzxVIJ64jMM013XnXrsYKSHaqHQh870yokhpV-TwUvBiiJITkWDZBijrATRL8IJZCy8C-0pfrIWQywdbN5RlOnJMqplC5SHH-HJRhydyoth4lw40hi1mdLM_6AYPKdyeXInFL4mrwF-XR_dskSseFIWJOQNi_WqQjAixaiMhS9i8NxJhpI1NLHlbvetbB9XRvNx8YU9kKCxMckkgKSMshHO6xD2uBGz-FQvP_dP7VBKPX1BHQgOe01DDtlzKpKFEk3EXYEkNw6Hm2zW6ksV6gdlA3qCjznkk_dXlBL198QL6q3D1-WvNEhUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMhqt33Yx6T-92WJew7i4_LpqpjEtrUpEEc0YP29g4147-OdbAPt3qOrQOok1eVmw2V5c9GeWzLNB6M8DUix8lL7Rdu1bMeRRazi0FsxJ814M-W-ux_BfLuCjDtx6qkQKFE3MzBxfumgtjxectnH54aQKodHaCuZn0sNciRB6MH_HY5gbMmt7YvzVpFopttTuGCPAIc4z9IW63DJcVyq5OKRiMT4ALtuFpn48KQjIznzZYN_hafFgnnQNZAxqsjW9lIYi4wbSN1myZEvMkcgnX-tayV5QGjSP2yMbkfmY4j0w_A303JXGgyBnuRv-_mjDo9hOR3KwNj05i6Kbq9I0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=G7QSu44oprR-zttTk0umLFb23aDC5CG0sboVA8tly-Vxu5Vrr_RDJZuqkWnPoIuewQVhJGND-Mcw8u8zgBNLgRqs_zXjQ0qK4K7htC3-7zDoorh0hYenYchp6peIYul7J1d3Vtrs7Aq8WTon1-W2qzbTG355I7EarliFDZWMCRsEZIhC4Fn-38JPRNnXgbr4Ndi-WKjYRH0CviY7S3yrYU3hukttOYH-F3N6Nr37FsLlPKfFDVVoFHy6WYVIk0NWXWUIJM0TgcpmHM_tz4v4pnSuN73hf2ECJKnHvTc_F4jroy3cztEqYwuh1hox6XrXtylKlXGINVczkNy5ng-gUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=G7QSu44oprR-zttTk0umLFb23aDC5CG0sboVA8tly-Vxu5Vrr_RDJZuqkWnPoIuewQVhJGND-Mcw8u8zgBNLgRqs_zXjQ0qK4K7htC3-7zDoorh0hYenYchp6peIYul7J1d3Vtrs7Aq8WTon1-W2qzbTG355I7EarliFDZWMCRsEZIhC4Fn-38JPRNnXgbr4Ndi-WKjYRH0CviY7S3yrYU3hukttOYH-F3N6Nr37FsLlPKfFDVVoFHy6WYVIk0NWXWUIJM0TgcpmHM_tz4v4pnSuN73hf2ECJKnHvTc_F4jroy3cztEqYwuh1hox6XrXtylKlXGINVczkNy5ng-gUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6KY7DGb94KfudeW6zJBWn7QGDUJwhF32b3pzuAQ71nqfNmqwHbtFKKw4fhNJ3x0RWPL64Xnc-2DJu-1eSr4PTfXHIRPsprGrm9-P7HWcXDd91AlG1oAbjDZ6aQnzB10y3cIFZNDMP1z8dAagk4pK8wXrabNywG05A_m1GNQpWQTQg0pmgRaYMS5IjTHyEUoCrUdk5RXDWcbYSpKOkuOm5rhnPnx9nvzF57toNdihi9kIzegnP0Vup_jCn8rT7zjGePwZnAf1DoxGLT9yaqxRlkCDznjbRSrIKcKPGlj1lzsn6mEgT2rAeFwIW-cYqpe1SUjv0_zzoJdZP6Ty5lVgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lxT_a144-Te8fGVlXbn5xfHyUx7StVmRITC74hv_iTd5Oa73hB-iVwkzi6EYMMAXKCSy1kR79tV63qJPoCg6HmYb7_FX6BjroIUE5HwnEkWFykXPVFFzW89t4bLA_mIp8qytzX1XOsH3FxlJkOzbBYneUDxVC3ID9H7gtnaKb8HCdxoZEartkHbvvKodTXwDiMJY_1qakyKGyc_RBotDPCNAXaERSlU3eO_i1-wOu2ctrd5F6NYK1bkME29FPr79n7pDFr1LqOqvOfTCGQPLTczJrsA9XZX8KISbBR_bLXIxJE0rNYgKjA_dHIUut5-SJ6GYIvP6GrrZ56PTT5_1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMayUT2NJVT4FcyjCSFa1NU2RsyqcUl09fnjHn_Z_qg63IEcV6Iy50IqfNtYdban50uXOuFRxAQ9UegdxPZsT2cIvhF_08oOxykC70pMrkQI_rir9GK_zvIORK9YquLB6r1aWe9GbE0qiUeEdKPL7wipAwo5P_z6_QcIfAr3MyMwY4aifO55MfRB1_Oh6tMNqIe_X24hfXzbc1O5xDbf-uxv6kCtIEivBJlLLK5jJRGN-BvJC1PGcUEIFwPicQv9dQecF0IXzxuYKc1O6bf38fbNhiyYxjnB-7BF5Mx3_3dQqYFsvl__gjBkGItHG-Atycp-BvUzwqcHmjiHBe7qVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBudEhUiCh7zDTyNfmNTUYPwhuqGaK7igNjOKfmNicj0MfFGAeQUQmqkhqiOLfECCp_4w3GMwZ1DbjzOiKsZmKZkjaKb6NYMGrbdCoJVH8NcDubHQA_dhErMk0hqzDtdrm3_eemQSmpf6D0msZgzfdtjYluQnD5vHl5F9fYB7I6vEBirR0mfQuBjVJPQ6WmrrgCsZXiOLnO235FkDMDQdiJ_UP0AKaDvBoKQ941Mm2ckucKI4Avnw3JxKSNUopS5yU3bCKS6xY-tSdIWHGm8Z-9U7HcrpDrzyCeNRnx2LGSOWp3v6D00NjnZtajlPl4vxHkDunE-MRcGQmpJWMCTbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrbC8bJQv-S9QhIMRQMzKN-HJfRG_N_uUkj-qfoVLKnQU5DdxFxLcJmgOYcRtiTDfcXRiT-_BOPLIw-l5r745DXo18Cl2B7Wsx2ep_Y8ejt_g7CNzOIWRkTygEGhbc3sT0wndMP9oJiNYs6jzsyw_G3hZQHF22m0NrtvN9gkBETvRV3P-vhorreVGR3-MQZ3QR5KxTh2fG_KXQC9enxLLjPUyXtFndKIG12XHyJT818qbl8sqoC1txGlrdffLySDEBuy5xFf2sJBTgZEIcFxkPtAhI6DrDsgqK8qrzwmoPJtTPzNiPi4vr5HKyCU9dmoNyYzXbAHi46oz2-NyQOocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juVQMvKwjbD7Fj9R0fO7R1Mtr_PE0cU7IqzzOnJkAi4kApnApT9R6O0Hk5GgWnb5U5rdeysrjGOH4QOSz-E2O8VBM108LdaMkIGYA5eihPTz_siOtDLP-1HY8jffDkzsowElYbvhmGsuibTzz426hOyChNu77PIg_pK2F5Jnw2zyvmDKcpRA-1LPsnTmfGd1viFgDXTkPgQ4NtbAanLxwwLTGhN198B1duTD5S4WGnhBW9ZfKZuZRaMcAvNzXPcfiNGxTcARkY2oZ7JHZtQ-U9J_95pJuZi-LT6JQp1_dPIGmGdkPS2hllPp6FqP-0cMnftdDXb4E8YpCERKbaIv5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJTXyAXpokAdl5_rc5g9aQegwGwaPgCjtcRHq4VdnN9QNoxXe-Pl7Su2VLaIrU94Rgg3kf0dsnBRBE8VrOw-gnchebPQmWW7SSjjsvFwuZeQCxNN0j1MQWtdCprWvx9rrL3fFbYCyYkSpcq3ahK1QkTL5X9piBBoGsNnVLhPMYb_BV4NjbRZUP92OpSnHdJo_D4IQbye7SgTVgVPtYyWDfkokJDoUyKi2uQeGmhcpyvOwcWLuwvBT2MQAdjDwTsOdNusC3csGtTF6aXlKLBZ0nh59NU7fTusQYfMjEPPBH4qHHIrLJzGJNVNKYzfnaH7T2hLJJ0Z39RSCpDqvMFmug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axgwuvV3C0xl99XGHbPpMw2kL0RP5gMvQSDUi8skk5wuWcMYa6NZRgwbS3AoCtn77ioxWqEn5ZKNnUbBRFcfDKRUvdhdWp_CD2aIIqBHjF5ZOJ9PfFAB6Ln_thPKs1xrN2hbZ-HmXf7Fjv3YIYDwWJgod0aVNQI4weOTEW6w564Q1q7P7_mZGIEFn-hHvgVQKjICCEN8iUeM2Q9JW-1-CBz1ii8cuOBBmfm4JiWbxPeDXTvjIxHFDjTOAhnrbY85_L7v0ttYukVePt5EvRuQQcVGR9XcT-dA8npiGSq8kjzsg47CC8sj7xhG2_t6LUsdr1-MRuON09zaJtDtptJsvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIA40i3dNqhiXKdi8p7MlxcgRxYnafA4Xzgua1ycRteV-gAgmFtKnXWZ9WiFYdy-l0-WhL6-usXTGgl9eSSRz-920q9Ce32ogl6if3Ju9i_CNZHz_xCJzA4RC9XPa3GnuoAE1ITP69bVseh_KE8cI80sAHaZB9G4UctYdQOvyDMAULd3WErCXwgNSl7p2JWypWfLmOiX2JZz94hWmW1cPqbb8ITe3rpBpiehE7JgNUBJQT-b7SWEhuDPv83fkxwNPR1_VfAB94yg-_5kiQo9ZEkT5UwnsrZ-eBP_mPhsrD_0grdmt4eKCsU_VWhnkn-EaUpYpA9mUWDJLmkbLivbng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oz030ZTV4GXogUtKYZ7NniuMZy9ufaIovZq5ELB9NkKDSbac91AfXZmsNtA83rul2poHhdNbd4Bv0dEvtWgm6qAXKknQDbcoLSSTL90Yy46KcCWFdPDxak4y7wcVXk8qqNzyA8e8Y999Y6ubg_HLp9Igl-kLqlLuN3oc26bScfrZkWqBiEUhchOuGrQpKvxSL3M40v8xfe4OE_0rAJNOXabnOj4AG64sga8q6D5L1rmn9psK1rUljuI5H1_rnMICbNNM-ztrGglnx2SwUhhopWAd4q4RK0G49AcUz5w22EvsahVXpuR1Er40VN5GZLRbOp2VP_vEjvxHK0p1Qel6Zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oil1IdbuURXLVC_d8K2e0Ybuq9o8zoytx0Omu7jiSejy4ZcD4WKCNrd3k3U5uoaUQj8f65Bbq-SwjSVv_OO28Svm-BlyZ0S10fuHZWrRc-jjgRGQ-hi4LsfKFOh86QEOFgpCh_abRJChuCOOb0t5KmPVW9jLs9dWA6kOq-i-CwE_yPLqB3hgzYJW4joZ5qWVJZamkeDGsHwQc_c9KCj96DmGF0eIkQAEvVUQJekAlEIYgB1Y7X6SK2WovI3UoS4KjRG4sHxedpROnZgXAA8ULGRGsCUckif3X_BgPB-6ilA6UihqUd9dXoS_jtQAk4D8H3ECiUVvQTtXX978WfqZeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=sIqQxWTzrVaXRALyh3nG5v11yiYKDp61UcT9nAj2YAW18ucyTeYNxY62OlKZ744mg4LR9Ilz2SMI6WW6E6p16TcQwJoAeKzXoyX6xRs99qTZXKpTiZ7WU8O6npjnSw8f7Cw_YceSrRXbVEAfVdlsHcXkTLw4qOdUrztkS2ijd2LRLwJWH1i70SwUWkEmT6KCfJFprT417B0-BINptiM69PbNSSN3tAYybMYoVuiRPn7EIsNB1O1aOnQO9xr89GD5_G4oBgSDX54u5KMomc0iUqh4-OsTTMY4qWZEXJUuBLjQQt9qUYRWJGZhafHAe6x14yUOTXjdce-JDjIsGLjZKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=sIqQxWTzrVaXRALyh3nG5v11yiYKDp61UcT9nAj2YAW18ucyTeYNxY62OlKZ744mg4LR9Ilz2SMI6WW6E6p16TcQwJoAeKzXoyX6xRs99qTZXKpTiZ7WU8O6npjnSw8f7Cw_YceSrRXbVEAfVdlsHcXkTLw4qOdUrztkS2ijd2LRLwJWH1i70SwUWkEmT6KCfJFprT417B0-BINptiM69PbNSSN3tAYybMYoVuiRPn7EIsNB1O1aOnQO9xr89GD5_G4oBgSDX54u5KMomc0iUqh4-OsTTMY4qWZEXJUuBLjQQt9qUYRWJGZhafHAe6x14yUOTXjdce-JDjIsGLjZKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGWPO3bP2mVZ0tLwRHOlzsSVYVxDEoWj1gVtG3IkUiPa7CkzxzJHHAd4gqqAgxK4HmZl2NkTax2HVs9vYCiILAWcsZfPuUWdNUSJGsRvljTlUxGD36LsbIKYms1_URHtzNTJ_lZdAgT5aEsN4I2STyJkS7YGEIlNpZW8TamIbSvYKhZs_kxSWCi59aoAasn2i44yZ_jBmZZhrjBms9sdwfBq9ZkuhqKhCuxhVV9g7NKeHj5QF1_Tk-adotngyZtPzhlz0ez3uNwba01h8b5Zz86t4YR_qrfykM0tgiwbgMZQiMPVCnSq7ZOihVzJCIQI9biYu2mJokPtSdoy0zroxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-B-VPfhB-0M664TAKdQg5u85D5HHdAp581dvESrLuIGfjrCXtVAM-OBgy8ST6VOVMK8J_g93JsgTq-GuCRTCEODOdqSBUHTfnf2ma9Q_LQJYsxMsapAzHmnO0nZQbpZjPUJc5GI7odDHcViuShkYsCWzA-01QWk_-Y_85PhQmaTlI15NKywI9BYGPpIfUQLRMZLUsfFGKlhEJ4MWygG64wK3oNJMOPpWkF1MutKRaIjNb-d1T81Dq30jIN9DdyGK0rNvg86NO8pHO0eV1wsdGa4l5HAO-tX862kdiZzoFNQdnQMRuPB4L99A0SN6YPxEF8CIWoYtlRtWQdNeOHFFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=rGWP0_loSwYcKWdRfw2RJ2aqVYNvsrlKwlt83QdhETT5wrK2D-vVrHpAVS1JjzdJGxrfNxtU5JKIi0HmimmBitQCM4y9sUtiNRz1u9kcZmDyJTA4BzarQkpCRP12hCxvCqWVsetHXfSmKwqf1cRIZAY1Q2n0O2WdvMJLsMdeoZP7QEJeqPecLS8slU7juGw8nYy89scbkWz9Vg4oyXuxu30czlf3eDbiUwamH8M0PDKTrreR8jLcet9Qo0oIN2G_aIlA8U2KpEZn6bNyKBVW8pfXp5tDxXhVBBuL6bor6Ka13L9uIUkMuCU2HAT1_O2UfjQXFqAacPuvw-hA9XKlkFhn521WGkADWrflCXEq59IW0igAI6-csqSRoaM0-ls2tmrSOZEzE_koFsDjzotRWK9PugKIT0oSnzLoXHfPQjU902M51q8a2Jm7Wq1C-wSeL2fmbNiT4JNvelSBAVV9OqbyIwd_FBhFzv3Gj8yYptM6xFl1lX2QuOc2Y0P0RZ8mmMGBVQpb0ypRW2mmlRfHO1SWRKqW_AINyOXZh4f2Lbnt1t-AgUxW_GABXM2dhuQNycOLJq125W2BKyFh1vzcjUUSvhARZe5yjfIomAG13haYgs85jgVmn1mww8PGXHG_fOymdFyjM_dRFL8yHg1vPns5ddcCN-HA-6cFHNBu_F0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=rGWP0_loSwYcKWdRfw2RJ2aqVYNvsrlKwlt83QdhETT5wrK2D-vVrHpAVS1JjzdJGxrfNxtU5JKIi0HmimmBitQCM4y9sUtiNRz1u9kcZmDyJTA4BzarQkpCRP12hCxvCqWVsetHXfSmKwqf1cRIZAY1Q2n0O2WdvMJLsMdeoZP7QEJeqPecLS8slU7juGw8nYy89scbkWz9Vg4oyXuxu30czlf3eDbiUwamH8M0PDKTrreR8jLcet9Qo0oIN2G_aIlA8U2KpEZn6bNyKBVW8pfXp5tDxXhVBBuL6bor6Ka13L9uIUkMuCU2HAT1_O2UfjQXFqAacPuvw-hA9XKlkFhn521WGkADWrflCXEq59IW0igAI6-csqSRoaM0-ls2tmrSOZEzE_koFsDjzotRWK9PugKIT0oSnzLoXHfPQjU902M51q8a2Jm7Wq1C-wSeL2fmbNiT4JNvelSBAVV9OqbyIwd_FBhFzv3Gj8yYptM6xFl1lX2QuOc2Y0P0RZ8mmMGBVQpb0ypRW2mmlRfHO1SWRKqW_AINyOXZh4f2Lbnt1t-AgUxW_GABXM2dhuQNycOLJq125W2BKyFh1vzcjUUSvhARZe5yjfIomAG13haYgs85jgVmn1mww8PGXHG_fOymdFyjM_dRFL8yHg1vPns5ddcCN-HA-6cFHNBu_F0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=DLyck7S5aXHEOESWbfGAxKSoaJKdtqeid1bp-L2Q2XNKdodvOD6g5jGfX8PyO3CIwOuPyEC771ecAn4zO6dF1lDYzmAZ7FGDXdejllnGpqBAGJ8G3wocfBrNeSRpCLzvpb1HpyuCngHAZPjpFFhO6pdIZsXYim6i4fB5EJMj-ZbkHr880ij2rqKl-DrE8d3WuvvahDlsTul48JPcN4gnVNTqqIJUlhmv5e36yeEULdVMoSQeZqs_K9fIkxeUmGtie0pJHe20ZUVhl36w8t2MlMBY0cwkfbm5o4YjQsLozJ-5Ub8VSUkgBLXay9L254WwYLjkARE6Cy_LCkBQhlYW_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=DLyck7S5aXHEOESWbfGAxKSoaJKdtqeid1bp-L2Q2XNKdodvOD6g5jGfX8PyO3CIwOuPyEC771ecAn4zO6dF1lDYzmAZ7FGDXdejllnGpqBAGJ8G3wocfBrNeSRpCLzvpb1HpyuCngHAZPjpFFhO6pdIZsXYim6i4fB5EJMj-ZbkHr880ij2rqKl-DrE8d3WuvvahDlsTul48JPcN4gnVNTqqIJUlhmv5e36yeEULdVMoSQeZqs_K9fIkxeUmGtie0pJHe20ZUVhl36w8t2MlMBY0cwkfbm5o4YjQsLozJ-5Ub8VSUkgBLXay9L254WwYLjkARE6Cy_LCkBQhlYW_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSYuiWIA0suj7hFDNj2Uvc5awPYByLL3O-AZ6VB7Ky3WNQ6AKi0l_25ep4Asy-eMNYsNTk688rEsfL-mScWt4abyJTVWTkFfmqKP1XN_KDN2vEVS8JB6PkJPK9vGO2vZG_5WW-1Tn6w3_eYJOhDqqpTQvqy0OWA0tdp0op30e7YTicm3tnPb4-RXB46oFTzIXvHB4eQFM_lNcPy04F3UMWb9O7VxCJJM1vSzKwQReOFRtKTQde2Sa_xn9X1adsEVlUKmvgtK-slq_X_gh3YEyMkLSzTimbssEWXYlTW6uXiX6SnjweuOFYBzUhrnGNED1J7e7UggDFp6Qj1ijqUw3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lV2QqdOcpkJ_wvhc82VVMr4okDWsO8h3Ch82HXyGo5LgEvXT1_VPpxZ27rzsafw6utB_0ukTvL8BIZgm1mFXZ38gHnKKec5Fut7wUnCSqQGMI-nwU7mIXNJk9Ir2rFd0R3fsgvO_pz4-RWPI-zWHULdcbNHcaIepzg_maKEtKkr_FjXZv_5a4g9aGwTUTBljGx8_e0wIgh83SiPFUWDZ517tKIM_ezq1woPbB_hRL3CuF2Qgthe3m-Y8QP1XlgFMlK4uZ7xZGnekga6aoEGZLz8co5a1XYCr3aU0qSe4ykQWilHZ7KSosPJz8Bj4bPsb6FKotz72qcinWH5x8KfRTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AJj_uUef3AjPTm4IdLKSVsuRLulQ6DmKRWVhu-_oUjR6lcVlM1hKcoK5RPVu50h2fDOnIkZSn6mgiDHXwSAN9ui0eU_KKWTZVKKnSGGyZAYma_0VuMMevN-bXHjasbAbEA9FYrvBpXpk4sXv3cX7hmiRw0W70iWYS2YQsiYuoR03SGmNeMjzSxRC-t8bP77qjdr8IjCuQ5gewBLcPIJ3X-Vbja4ldXgcCFUz4i5WzjOh8jX8n14naGyKJUJXyFdDRIi1WMvcCe75RGEQ9jEsVEgPhGTeVxs6agdvgp-K4hhET4QP01u8jeeGZ97jiR7OfZsfCeIyRwBvzgUFAfN8eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QOPuRpD-FQ0ibRdS3QKom5ZBgf5AGbLrurnPkuN9j1VmaZo_S6V-_aPNtCUZZmS-mYoBSMKyi6TjNAdq9D2pPMAgFeNlEGwXW5MC6ILmV7x2R1gEy6UsqHkLjhaJ1hFBvCEV_CmVj5WW9Or7P9otafbA70kGF3GAwRdk_kteNjDGD4czkbp8GTTAS4rRra4mI3ifWPZyR9h85AfstP1VjbDrzWLU5lgW-pvxl5321car5DDddhXECmcYQEmGdlFXJWXLsweuctyhU-gUeCO-6rFHWmMvZKZvT71DNp7miXtf5QkIUamfzxFHrBFM40iSzH4s6r9wJZiA4Se3DPzq_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qFRTllKP1AacvOIfMyyFHVYxo9LQbKdXdLXdMA5hWM7QzrPRXIj94mwvmh8EbAwj-FhrYL6uJYUKR8963qkP6x3krAeXvly1qYVwuiH4zJo7pf6TlCZ-ZzMT3lZaX6pMEOXd8Icw_4yPa1lZaw3TpdMIXdWjpPQselxscfHirukt7VX5fo0NkdjAXcigFXbtlpC0aSkLG7NiPfy0CP7ktQS5qhbjpvo_orPcSO9Kyc2AgaPhYocdXWnKZNghw_K70rzn-a5Akg9QLoca1AqVEeLLMqhEmLhLb1mDFvqM_oO6FVnzBisRwr-0QaTImZt6bMU2v82kEqKOPKDv6gOZmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpjyqPsgoS1JlVeO7uQv0qg4V8qUKj7yJ41Qetot4SWawikx-WDVK4N8xBOi1G7zt7Tu3KRFFdJ8ZOzFl-i2qz830gumT89xHGOj8M5L8fTVQ262-B0O_keIu63_akQ06M6Z9BtrLYhOsmF8qnc98lndgiJloTr8fKAmXKIkT977p5lS_U7PfgGZ8qhkoRck8OX-eJzcEOClZXtUPHKZTRCXHFi-9h_Xh3rJOAixfQDTacxi_X74rtKRCMM4nimIBCbgUw_Bac83uI7KnRE3MjJxjiNrt_D8x1FFJTDBsC9eFLXMVEP4rMP7BTWaMO4ccWuEhbi5bCdtDoFwAIGw1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_xj7xgjShX9DUi-n3iDy7M3D9DD39qIbcqR1Me-ueXokTzBn9beIQFbsdG-0jarv57WUaOY3P2Dox293Ja-qGnK0Y8KQb56fy8mEwKvZTav2Spp9i1liwKhYWDehaB7AKOn5nkhkrDwyrY9ufFOKTMKEiYSfEduP6oKrhHmBRQzCnCPj_fdp8AWA8W5gO8J0VkqqQ0WkKLLJvF3APfmaE6v0L0MjwMplP5OFrRytxEeqds0n-M0Ikh3ayO5_Qn8NELWMT0Yq-QbFAl5Kv7Zr4QfmqieB_Gt61q79EoPPur56Zcb2zzP_rRoH0fcw0hKY0saaQ9z0C4MN4xY2I84Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rquggt1MpXwzuIkNyTh3BmoYDca7XE9sM5cW0hiAIzO2CmiE6Bss_lUPa1tSIEVe4VPSFwXeONjP97G2bIHY1yPjwkgkIdn_kkdNcfvEGU0-8bT_aDA7GzUB37Ram3k-drA5cZ03_7ehmzBFQzp04Z9VglQwfFcLHI1jremnNBFohYBvpv8Koju3HhtLj69HH_d4YRon8ImCXMf1ZTltB87Y2kAf9bpdrcvwb-eqfItx82iJ4kztrO_AyiV0UzMt1Ug2UnIRkoh9DEz9OQCiEuUjILgq7q_a19ZcTvLxNy3YWkF7gwEMxFqdXufbz3iUVk47LdyU-q4OsUVY5nEQTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfKG3nqagg9rZsbMQdmYHZTU92HIpbXjZrjjqbttCECvDYFNZH6BBHCgnzl41KJFttOISf-1vEcFg51KZU9XSvpk2q_KoNh_D3ufIZcEvlkvs2RYE3wQa-r1QG8Ro5ne38R-LE9bZqUpWS-LOm3gwG6wSV_5Xoyyz8B8G6XaET53tdu9YdtSz-v3pBqmEGc5Xqi4S8nwGf5O0ukE9P_rkOePs0tRV9yOswq19ga_w7eObNGT23rxcv2Ij7Okf1C8fF-sHMXxG1tQgioHV8ZkoV5IufeO901DzglwEQ8mlrnwe0WJS0ETeoxmR05jgc1w9FMYuN3RzOlJVD1aFproxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMETrsIgFcuKHJAVAhHCJY9VmV5kg6yxf0uu8uItL0cYIavMQc42lD32tQ0nCagkVKZZsK_sFSyqfgiuedWPFgOKsJwW_50DL2BlXHrqzxyyWE1Nsrdi2tVAgdDWtaBFvodkA5fsRMOoe1dBFTbQG3MbziDZScoBPxRONIhtKqGBq_XukKYW9d75S1xl0bOgxR6stQRv38quSFo4XXFWcj81coIWR8yGq-I-pDtWHWFIVh5ZbDnKv5xAX_g9OqaEmM4ar31LSPVjRp1T2-sorrNgLAoqVFbweqqtNRVRTzxkm-VCT_Ex1qduWICYOXeSn3B0-ZKqaM--hUl_tBAezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZojWStZM-SNUtfsBU08I0BgSU1u5P3StYAjKZKpmTgUkalMDmyjKxkWHZwUKSc6fpdrfkza7QuCa9yUejGkxAIONcQz-MUApVey0RSPEqPkbySIZhyVDYno8BqBj5M1RdrZaFc4IFWA_C1QTQH5_UXAiRY-LTpj9znoBaPtXKkgv7x2gcOv6QyH5ENtHT0LMSJ4dWD3x7VKjiKg2np_72moXVGMPimfVwG1bRCh53xtAKfBjJF_dGy_FQP_18YqcZB6zx6f9n91V7Gj3pVOppsmFL9laJGEER1NlY4NPp2n-kq4kx3PA3GpxRMP4rQVZhXB7pKfVaT5MIrpmj5pWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbOR8JZTzCwW6vmimKKgyisjHe1bNX-5HnL_5ltJ3htlJYCWqiQjQQWzTdW0VwuLjE9uHTUg4z3UJatg-DZJXudbRUNfnZVUQypksJeSuZD5qHgtNQ2yeSuTlhMNQ7tG0wZiwyakGXfswS875UMA57f9nOEhPg1mhdhidBlK2NK1llK1Xo0xsXPTa9XjmAFYqlzMWcVGBAK21ZYYOffKk8D5rzKR4NYwmKCCPO2D3Pp7_C-kA0DugHw7YGr9JA820e_zhu4zssw8uxa9dD2jlAifWdUqC2tgTe3XzIJQ7zbAQV5nIZ13m7MJDLpf0pK0YT2YeYmUFtf2mqStfJnzzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=LMpS-kmwuP2Ji1o2JtK9AZzyH_25bgOZ-jC8eiVhrXalasVt8t24uj9xtxl4S_UemdFk5Wj3__sfq-VxVG8K6WArMwolx-g3bDdJT6O4EQle7sYimYxWg32J607_y4a998QhE_ZonVjUCM2JjqvMQalnLt0g2s046aB085_NTlY430UxZjo_qsHg7800tR0lm93tB-32iiF4OMTaqRlpga9DD1CNSdZzI_pdakhyZ8X9apTYzmKBA1Ehz5ayFofMuwM10ocrLVOs6yuLuQFszHbl_Cjw3WaKfktXAGmht9SJyEscDPnhGHXfllk01z8Nwo-CdadtJ8akfmm4_5B1xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=LMpS-kmwuP2Ji1o2JtK9AZzyH_25bgOZ-jC8eiVhrXalasVt8t24uj9xtxl4S_UemdFk5Wj3__sfq-VxVG8K6WArMwolx-g3bDdJT6O4EQle7sYimYxWg32J607_y4a998QhE_ZonVjUCM2JjqvMQalnLt0g2s046aB085_NTlY430UxZjo_qsHg7800tR0lm93tB-32iiF4OMTaqRlpga9DD1CNSdZzI_pdakhyZ8X9apTYzmKBA1Ehz5ayFofMuwM10ocrLVOs6yuLuQFszHbl_Cjw3WaKfktXAGmht9SJyEscDPnhGHXfllk01z8Nwo-CdadtJ8akfmm4_5B1xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s47OxfAntBlItQDkLFI7xaG2sofxb7g9EbkhPihAxMLdEqnX592kIoFw2bPwgbG0G-_X3WHBiGgfVIGNYi7_ifnGLtQtJs-ScDzYSuZSQMrC4ZGJhhXKfSKU6vYcgCBNFEhDL6KIWI7_uK3Z8h8ZKjui986zBb4GCu7HTHf8wnqofbMHGBzC7PC8z0jrweKqMNRc9IBUB-CXdBQtugg_s4kFUCAZzRqB6j6nFulf6xZQOhAsCOLEtn8xYa-R88QRgotzIskcraetUhHVEU8MvExwb3hID94MbT3MYGsvpzNptX-ONB2-2xJxXwWWlWQ_fpwhSAhhvUefwxnhinvPHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEKRXVwtmtrq9L8CH8z_bKnQfkwWeZ9SwAgSmSwP88JrJO_1XbUlinEc10pxRr6xWo8tXAGmv2p3RgUZVq2Qcjp4dVUvfdtXU5ThOTGd0r1aOQOeUE5drDL84Z_k1dK0UZFBntr-dP1Iwqodx_qkLeQ-5FWAhZ8f3V2x6vGC089MNRosW5u-_efxI3xop0z0OWQcTMa6_HPBEBL8w6_c8hH4aQuDcY21Wmd5KlL7H4tSqLz6cJKfDfb1I0iqZ_n3SwYNwdZJUqmO3Q0Y_WKF8Px7mVenkUdAJjN7-0Bl_kVbnKeAp8RhWYJ8sGPpzvLRjYw4GqKahPMsjG8QRFGxFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
-
لینک سایت در مرحله اول
-
لینک سایت در مرحله دوم
#GPT5
#AI
#API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
