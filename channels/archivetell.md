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
<img src="https://cdn4.telesco.pe/file/ohEmD06bAw9YfcDzaId8UAQs5UMCuYoiLl2Eo-ap7kI2YgaH_r-fCyi790M3B-ap94PPHScAVf2RBDr6a_8nFUxw2TF_wCQswoOWRrxhl7ldJViM31179ITvafQAtjdrxFN0zhQIB-Nnd0F0ksHsfctLzR6i3QvBgEWiv-aChqntTbicc6HF11DZBgoJSNua8uH92k3IZYQZ0So_KpagngR3dTCoV2SexlbpAyHA-BYfHzWPFOpF1dWYXVYSFJ9MDpKL3YIlNYD8djS36O9mH3avjmnE8oHDG7wyr0ix1HI73g3iVVthjlUFO6dvvygvmrtkz68AjGCJdRKImtXf3A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 00:16:33</div>
<hr>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 326 · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 543 · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 721 · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=BEzFFtJ27bdr9Qx-erY_TfUbVcIEKp01O067tqzm27Ksds-DU5RC--KNioBRd8CgttqKx_mfE2tIW820foZUYyqIE1Ud0d0wfEBp8H7FMsrayWNmu8Ecz6W5HrqTKbs_iJltKZcC6ZQGVFbnd0uOHZANCahObSF1J11Nqk_Gg2u0xDvVvVq1n46Mz9ZwwoeJRDaPwFVwD6_e40it66ymjWexkYZBSYus5tEiGmS0SZdBqAutYyxBp-0z3_krjG3xVbi_pwa6UP0YXVXkcgzSMZV7sY2VxSqHFtMswz8EyxqtIOmcE7v4DOrkWQ5mA9wLlUdgn3bUDiVNksLiQ9vC36M7FUiEOKcg-2mLtccc8f-qIfA07rWMH87fUkyCBn7AZbRYObSATcn6lCR32x9Nh-6D9sUzAtpwuaZ9jqqFN6LVWtjdDQ_B5VOk5_FxQv7Y7-LArUAzTdn6x0L-tYAeAhCQRjMkB1LEG2zwqslVK0Oxxo4ZTFPkhYA5gagNkV4E96FXc-x8o-tCdCkBvHHV_NHL7nlza8Hx-JZBaC8cPvitstqrUd6E_kVidTgMybKOn0uH82xoELDrXrXOcdah_Xxjd9vrKbzsf96Lwhd2EWqtIkIfe9cecDFhzL8Hcxc2JSxrIQ0EjbrVmJ6WBXkDYXhbrreKDQGvliU-JrKH1bs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=BEzFFtJ27bdr9Qx-erY_TfUbVcIEKp01O067tqzm27Ksds-DU5RC--KNioBRd8CgttqKx_mfE2tIW820foZUYyqIE1Ud0d0wfEBp8H7FMsrayWNmu8Ecz6W5HrqTKbs_iJltKZcC6ZQGVFbnd0uOHZANCahObSF1J11Nqk_Gg2u0xDvVvVq1n46Mz9ZwwoeJRDaPwFVwD6_e40it66ymjWexkYZBSYus5tEiGmS0SZdBqAutYyxBp-0z3_krjG3xVbi_pwa6UP0YXVXkcgzSMZV7sY2VxSqHFtMswz8EyxqtIOmcE7v4DOrkWQ5mA9wLlUdgn3bUDiVNksLiQ9vC36M7FUiEOKcg-2mLtccc8f-qIfA07rWMH87fUkyCBn7AZbRYObSATcn6lCR32x9Nh-6D9sUzAtpwuaZ9jqqFN6LVWtjdDQ_B5VOk5_FxQv7Y7-LArUAzTdn6x0L-tYAeAhCQRjMkB1LEG2zwqslVK0Oxxo4ZTFPkhYA5gagNkV4E96FXc-x8o-tCdCkBvHHV_NHL7nlza8Hx-JZBaC8cPvitstqrUd6E_kVidTgMybKOn0uH82xoELDrXrXOcdah_Xxjd9vrKbzsf96Lwhd2EWqtIkIfe9cecDFhzL8Hcxc2JSxrIQ0EjbrVmJ6WBXkDYXhbrreKDQGvliU-JrKH1bs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 873 · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=ZvgAqaNWh6gw1QRG-K07JrSGbVbK39v9Trp6500kQ78CRp59cdb--cqkMEHOOhsS8q11gWzQ7CelMFUDpp5YnxnDHiOVRoQpSp_20xBr88XrWNZR4Ze9SPEP6VnQ6JfIjBPu4ZS_444yKJIxea85WaIK_kFKcKCJ6ZWYFrRWPy5GGTjFsEyKSbf6H0f2sZkihqu5oLBxxD_8vffWbHmfHeXCxrmKGE9vWJEqe495PuvGnGFlxnN8tCfEXlW8sdHcriXjjRphB9n5T5w4pWmnTp88GlEDcTaEwt8HQMymbqClhOnfESlVo3AisKR3prSxQd-A_hc111rPv5Mzc6fCzXAESOoVM4wh_OuDhQpgGPNtoH50rZqmIZrm28_LlzJ6eOJQ2pSy2QCBmPWYkVzvFwmEJeRBu5KO14aeWGYfRbI-faUliPywhThgwOBWlToIGW944HcJ_V5W4W-OyA4_h3yDDDJJu0S2cgwFtIHUZjQ-hQZI-ReNmG6-iLF9ISNHSbiR_MJUa1nmCdQlDromUqWnECCaj3GvUWQNuC9njj3QqOyquFemO0C-85GYPu2MbJ6Qr0Pmo90TD4XVPhPMn9hS4MOJLXv_WK3x_2OpmkeZtTNB9Z0NaA8Yux7ixZ2_ZlqZLBdZJPeSl5LGkRpc9mCCR0ceirWNuPLvyBpNLSI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=ZvgAqaNWh6gw1QRG-K07JrSGbVbK39v9Trp6500kQ78CRp59cdb--cqkMEHOOhsS8q11gWzQ7CelMFUDpp5YnxnDHiOVRoQpSp_20xBr88XrWNZR4Ze9SPEP6VnQ6JfIjBPu4ZS_444yKJIxea85WaIK_kFKcKCJ6ZWYFrRWPy5GGTjFsEyKSbf6H0f2sZkihqu5oLBxxD_8vffWbHmfHeXCxrmKGE9vWJEqe495PuvGnGFlxnN8tCfEXlW8sdHcriXjjRphB9n5T5w4pWmnTp88GlEDcTaEwt8HQMymbqClhOnfESlVo3AisKR3prSxQd-A_hc111rPv5Mzc6fCzXAESOoVM4wh_OuDhQpgGPNtoH50rZqmIZrm28_LlzJ6eOJQ2pSy2QCBmPWYkVzvFwmEJeRBu5KO14aeWGYfRbI-faUliPywhThgwOBWlToIGW944HcJ_V5W4W-OyA4_h3yDDDJJu0S2cgwFtIHUZjQ-hQZI-ReNmG6-iLF9ISNHSbiR_MJUa1nmCdQlDromUqWnECCaj3GvUWQNuC9njj3QqOyquFemO0C-85GYPu2MbJ6Qr0Pmo90TD4XVPhPMn9hS4MOJLXv_WK3x_2OpmkeZtTNB9Z0NaA8Yux7ixZ2_ZlqZLBdZJPeSl5LGkRpc9mCCR0ceirWNuPLvyBpNLSI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAaDgmo7VGXodF21R8p3eaPsNV45pvan1W0putjl4oXHQPVs9mDpaZUeX5ahKfSykGcnighxVygcFqYQTNx9PlKkmxE2uQQYdhOcnFEFJkjyWntfk7ChVEKX1Mi8ndCPkHbDApHUcxIgdiOGlSd9EZC-0dBBELB_v3EMt7g9rLVAhi3j1PLAgHTR1e7HjcPF9CTyt8zKagw8s8IOMaxT6qYUSOAT5PHVT1h7C7pYB_1SCbZfKoO0MO5HHSjNIqWDW5pmqozuB0UKLUaftT7GUwhDLgJcNvGtFyAmoKRlmrzPWIyGbZ_IngmoOiAZQoLCLqVQWSilsovOgo9HngdyAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=jGOwjXspA5uvhTRLSpfnjJXaYD6q2rSTZeTIc9C8uWtI_LghTbFpV_iWRYuaXLyiXDMZj7YA9nmJ7oq4bX_9T460CsbzbNW67o5ClxXszQEcOJAfKH5TJpFAjd9dfWw1P7x5fHACPjKctpgZkmsFOUzz709yLkpb3n0xXXHHhNVfbRglIV__V9dI1ipWevr27xHvx6i65Y-9WlwVfDYOhJEvu1dPmwtx6F1gamfVrK_1-OY41CPX4PwkCbF6KxppfQAgbIZzZdsu-iPfk6R1G078FVx7gZnzLrbEMsX4T6YKn2O7mA4AUiY-_W2B-56IklaPmHdNmOai8YeoaHqhUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=jGOwjXspA5uvhTRLSpfnjJXaYD6q2rSTZeTIc9C8uWtI_LghTbFpV_iWRYuaXLyiXDMZj7YA9nmJ7oq4bX_9T460CsbzbNW67o5ClxXszQEcOJAfKH5TJpFAjd9dfWw1P7x5fHACPjKctpgZkmsFOUzz709yLkpb3n0xXXHHhNVfbRglIV__V9dI1ipWevr27xHvx6i65Y-9WlwVfDYOhJEvu1dPmwtx6F1gamfVrK_1-OY41CPX4PwkCbF6KxppfQAgbIZzZdsu-iPfk6R1G078FVx7gZnzLrbEMsX4T6YKn2O7mA4AUiY-_W2B-56IklaPmHdNmOai8YeoaHqhUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZVNqWkrG1texyzFde0Ng27i8gE1xn_4kJnAsmaXD0uE9tlK1D2uzXTWsHjqNvqutn6bcS5QCKrBjuo8pjv4joMBFe6akJ2YKUJxE17XX7uuumgHPCtw9QY3pilb7ykvyVyf8e5VEGRgGYGvbS3j553F_VXzOyazenT6mdJNvnmO26ujXxIIT-nRD_ScrVhsNDj4Nart5MJDjgmHUArGu-Utjj5W044z6STY7Gve6xIt6shFgy17acD4nIFiojePoYF1bUHNb2egDsrS4zpImEWBdWPnHONWerRl__z6y60HNjBjRpuevfYTlYekPp5UBYOuhK-2MEp1mUZT3gbIlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=feSHLbuwdo3l31obOvH7Lp9gBSOVkxkVk44YJZfWsiRebyAOqhZurq3YdV0uP_SntD1d2cQjPYnrJKCQ48F8av-TkNbtbKDXjHx2MAArKOZgqjbx9CpaqEOUQiavi9PEHevnpVxuZ9K4qQS8CHWxTUnVxszADiH8w7VBnRz_SMXzoIc8hyChkZ6vO5UGE1ebp9bTtGJPEO351pOR9-6_mOU4VGtcD6WLjYJx5lQZbeMfaJh47BRJ7qlux06IXztWT6niBdfDhMdrbPYAVGdx7bsu0jGzJ4qLHFgZo4C162ZXMwSDKY0ve4nLpgaBtjBkyYw3WCJQcVlZxj-EUjjyyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=feSHLbuwdo3l31obOvH7Lp9gBSOVkxkVk44YJZfWsiRebyAOqhZurq3YdV0uP_SntD1d2cQjPYnrJKCQ48F8av-TkNbtbKDXjHx2MAArKOZgqjbx9CpaqEOUQiavi9PEHevnpVxuZ9K4qQS8CHWxTUnVxszADiH8w7VBnRz_SMXzoIc8hyChkZ6vO5UGE1ebp9bTtGJPEO351pOR9-6_mOU4VGtcD6WLjYJx5lQZbeMfaJh47BRJ7qlux06IXztWT6niBdfDhMdrbPYAVGdx7bsu0jGzJ4qLHFgZo4C162ZXMwSDKY0ve4nLpgaBtjBkyYw3WCJQcVlZxj-EUjjyyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLdC0l7x0w4ca00oZa2-qaFHyJQC-cJoZbDb2102d-N9VkkkENwV-mF-LJahhUnAYhRHgR2N75NSZPridUNXwufkV1J2QSq_7gvakLq8TANZ9iIXOQRDRHnV_1FvujF9SN9sf9OZsOEgStllQMWBuu-kc5rZQ-MdfVm1UQLZv8ySKz0pD9nvtSzVNotOmUfbZELv7zwVuv0_BVaaSjUO-vqf_7ZrP2aMFD28DGr9oNgh7-_AD4gyShTBAW8dn8dIyJP8C4ruWrsFeergonqlhBvpSt8yo5jrWHuQpPfuKGHWPZJgAGd4RNolXwR6Joi_3vOOZF5580_ldwH4urHSmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JefVfhcxDBzK5O0278mrGXAv9XycRkQkCS_9GXyKCL0VoVe6EgCIxj5LsA6TvT-4voNaM65Aib1p8U0zDcZJg6hzTH6-do6-lnf7L68Y9lJBlD2ONCd8JJ-dPnDHihVwUGrhumvLMxUxCqlgf4zDSd7qnX6KQfcszu8jxBKGi00VNlG03gbn9lXWwAkZ_lLxMSppxr-dgyVdIHuwt4eJ3M3Xp3zUkhsjTbwZPIi7Oojuyntntk7PtkyqtkJixyXw8Br2tsawSZ_tMAOSLvb-BK0I1QsZbBJmXhGymgHkLNZiHKU5ENHoOG-DLNv8Cyb3nkauOaygNUA56WQm4yRUZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Amg_QX94P2k5HvtpDely_S-CDxtNeCsuFW2GjW9HFet4TpdFwCkHu7uG3UVlSGFTAZqRsz031rLrRKCNJKJ3-JY5ls6i19P2xN069CgFQYw8IwYo1evp4IWoiypk0yHkHGQrLlbL1EIxQV7moryGBvkfxQ5oF9Daf7rlkfpo-gbDMffKDPTxPnNeO9GQBsiCmhNxnkQ6uzBI2yig4Nc6utZX8C-TI2cC1yts6uA-C8zBUmpavgjuc-5c5_P8nxy9zsjXWR-ghTDGJFTvty5RmTgb1qKJR4weoueVXlFVg_ppz3txEBvANITI0deSwQ-6lICz9xa4KYxME5glYE_z0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mS-rK0XIV__3FewBioU7BZmdfxfCdvt_h3p-ztw9Tzx_POhar7UzYkCHa-b38ZgG5Xa4Ay3Aw4xMwBaxw8zJvyXSickubW_fERVGDQLpA9yfcpBXN-WD_CDjXoAXXt_v0Jd_jWB0gY-H2doLCNszyExgqs7GD02ZjRBHz-JSGLrqK3IUuzRXx9ho1krm4nhA-_VBD3T5On8PGClxW1SGLJnYcXMNI4c9lgb6mpUUeOzErNphA72d8oVeYkTxN6-gYkpu509trdemkUAlYVBclRDT_5za-U1MTglCzkKVAadb76042neAaUpj9xLTuUjczGUJQX7ZhlrQb7KVTE6pKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2e1h_u0YubY_kJ4KObVm30y6jrwDPDEXIsswIkKO6NSzntm-L-iurXDTsM-0G-RmEdPNUVBxz176-_jiujXEAyFokOZQObmqATioXtRKJSq-SPIQmbKAtyrXv3prRgZ_S2-IDaoxMBhZk8_fvUwAmM4_EA0VB-ttSd9u5nKrNAZB_bqaC8JxKuzoOxKkDi6lbQRxcgEBErq0mkzRlT0bOqPMGh9yg8-pi_wN6xoB9FKJq23wruyfwFKyM_MG2PKxRL5bz54FbTP4lDAjJO4YgzrLvWzDDupQdGj1_J_3UEu7MrulmeUzHkbnDe0U1RQv6eG4BCUJW4hrhJzUlZcrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8TPFpEnvTxoriu8P6_9PV0RaeaGUbPxuYdJQ43GWVqzIX24OUv7EYQeOd4UivKS_WSZ8XFN8eOp1kzC9VmtpPmsE977mEzqjiixCsTmFKzBTP6-4mg_bQM1Kn-C1qOjgHW7q33Ax1IkAcUrmV3SnTP5rA0mRHrdEN3ag76L8QGZFnP1rNKcZ2njlrkqYdEod5wYngxly-KXh3N6oF-1lIpDb-UP2mxIBAFHWKn8IHgoNNq8TW_fnaSmZk3-KbZbuYfrNC9IHPvwqCK_XPwVzc763RbiV2yTVMmhFtK_ImA6LRQhhirI8VRwc_LMf3YgQL_HqVmsiufOqrNI1cSElA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=oJC7zb0z9DptsZmMq9-c8wEcedYG4kiXEAWmdeJfDidzQ4YtvFrQndr3hAiQW0hIV5N6tebvXs43H5nxhpKmYtruS17A6ts2_IdKaxnJVdmhOAHPX6dSqxq4iouwdy4dkDadWGMXXHMQzzWiJ21I67fGWKo01fqDCXOuw3aK29XUFl6R38aR2Tls9sF_aBthD4g8CwZPeIyExbxoqTOcYI0ia57wNL3ri_sNMrKLImQj6A3_v3FWofilFzBsJ0yy0E2HW3rG4cRsJUdhLmOt8j5NophZoKhJd66AcFc0k4w9Pxjqz0X-Ez_fBsBbZmcXjUyIsVtkf7SHRVNaoVwh7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=oJC7zb0z9DptsZmMq9-c8wEcedYG4kiXEAWmdeJfDidzQ4YtvFrQndr3hAiQW0hIV5N6tebvXs43H5nxhpKmYtruS17A6ts2_IdKaxnJVdmhOAHPX6dSqxq4iouwdy4dkDadWGMXXHMQzzWiJ21I67fGWKo01fqDCXOuw3aK29XUFl6R38aR2Tls9sF_aBthD4g8CwZPeIyExbxoqTOcYI0ia57wNL3ri_sNMrKLImQj6A3_v3FWofilFzBsJ0yy0E2HW3rG4cRsJUdhLmOt8j5NophZoKhJd66AcFc0k4w9Pxjqz0X-Ez_fBsBbZmcXjUyIsVtkf7SHRVNaoVwh7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vim4WTc7Nm66yE_u5tIs-_IulSJ6g1K1iXR6yxh2pLYNzzi_yE2YyXuIUUGXTY2oiLD_iuOTIOawGbfw_F_CrQa5apkdnUpmTR6OidMltpkhDa9pYw-fqv3TTXkt1M1xDVV6putekL3n1CGEIUe3-fAsiqM04lx5tMe1Yo7l6vO_fOrxp8Km5At_DppxfwcfTaT3PagAu7ZZh9cUofGpccxkUZOhOHTXo804t05mfTvGnCMyi_gg5YRtgqZYUznl3pGESxNqdM4ZXAwTjyox5WPOY78pTONjH2WuiXeGOSDVZxz23GtzCIrJ3hxzW1InOnpJupRc3TXfisSK3zUWFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iy3UGGaJ3wZyDbnGzRNIc2BWM8KZpsmucy2xx0AfQLCzfMXnycc9XdAEGldKQkNcWjX_HzepD601GKAEO_lQ9rl0LoNgHZ0vn71-p73VGOtMXzZlmWsaEA6-FfrirVLxbgd2QHDSHIDJ7ElR1e5V5mXNv4hAnaN3w82f3x9cVXVKUXsmCFZU4oIJES_FsZTqaaTwACU7Uo71vhIzXfm1PKDRWxDt1_7KwJytvEs2YZ1vKRmUx7VYOHMcIf6F6bo7k5e0GB_mMPB7NgZJDyOsa0Hgz6Yajg4t093z6H0-Inbnsdl2DQXUtCmM-mla_-ZYuggpSdeW4qZXxg40KGgRCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEwNkDpSbk_yeHTnzOse8kwbsmDEngap7_FF4Ka2nsBVEH065-DuQDsJR85HIsXkMHJJn0PhncSt-n35tKdluM_ZocLOu7KfkEPHum-zb-LiFZ5pCFKSKthdPkyPTr8Ui_telZLCV7GMRKjuL9UbGQAauHX2IlVCDSM5p3x5nCnNIhxQ1_EyGrHrBBRlq3tcP7FyVZ9eaI_HHJ3f5AtigTRAh242ymcoXFZWHBPW8TN9K1p8s85rYNoagiy-vG8NJD7RoH1Eicv6myBxXANq0namar7BsoXNJQa6U_-jgwUWr81M0diE7bPdKMU6eZwHUR6VxsWqzW_OZtjW6-UorQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB1BMDQrZNJoVRz5VMlUM6pI9kXVtotAfXmHFJLsj4aT7mQ1Vk9jeC5HNQMlDKLwqYGjYhJ0Rqgg6vvTfqVk2QjhrqJuUbyF5lY73mMtUwANGHGaAKKbVVLufwNQ3CxFEGYVqM315pTlIPmJgWbWzpGxluK4VVUexfEmG4g5h5aDT1OY98DxQ6foTP7A8Jk3YtlyDG4VJRDLkNd2c9JWUNtJor4N4RW6PBShuvAu80FgKm70h4zBS44A-EtkwrajMp2SNw7VOAJQKVwgeoyQyMK9WSEHd362aggRTS0maJXKB8Dp3ZxFHTel6ulRP632oQQkITKI9BRh9Potpr6heA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5yPgJY7CuZ_ZY0dmyve-QX7aKfrT6QK77R7YXsQdyLnuOXun3VVJCwUG2VkhGWdiPdc97TcI7VjQqx0Y4Yt_D_VmPjZI1csVJotYuIKPYBW_1f6H7nP7rLsY0Bv3gN1ki4ATVue5VQzeBRfiL3Htj31etWoWYDW0sPDQrcPffKzdd8QoR9bvFVA0tH_gBmac7e1rofqibBuJQALitphfenXe0SB5cPg3tX9ALOGYs-u7ZRigLLpSACXoh1yI74MM6HCNuq04IoMdcOHL3LPhX_-rN0aaNNT2-F2uxafUuK7nD4x7Kp197Ur-InPtSv7KE6YRfVTkNICzBV4mSo3_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTyerGS1keyGsWAEyOkvqrMMZ9koR0bTUCclTQOq18I1amOOAGHryphz52EmfnQDilWlFh913gLFOOIMdSsjcMJsHCxaInJF74IUz4-skDEPbifIoMsLjltn548GH7-u-9imy1UdT2Sxl-3-sK_AIHxRQDunlPUEHGiC2cxLe9X2F6hKj7e3M2DTtsm6lksYcR8JKrEoAvK-qVuleK0EdpLHnApsGtgpf_mfzRhc1_WPFG2Ok5AJyCb28pBhQRfUGy5tiXvgnVm0M29lnCG_5_hZB7LqLvpRUsjx-Ftfs3t2brhzzSzwOpL7zd6lEp3jcJuDWk5eQvvQxTPbACW72w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqaiZ1H5I-_UeNImJbS-_H6MKvp6G2btgLVtZ7SKfdGKQrKWBPvvXbVxBEBwN29QYlCbONGsTP6LpNlJa9XX9wvd1J9yj5HE0dyoSWfwc8lTgK245FNuCtBOCnItC0FMWYkBoE0ZwqmOaPpJ1mZl3TZr9DSTKJ6qtL97MPFPN-Qm1inRTmRCHhMihUZ670JYxvnEuG4OPPDuPNLzn-ybuigqTAHi97ssleNOl6Drg4oS476c6BE0fbPqjmEDSw7xipbS41HvuKIaJczOJtGJ7icwidKrJxFwX-w7-hVW1i5XiqVhywH8S3K81zNVx8OgHjNgMmmg7FtQAtFaSEJ8lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6XISLwhvhU0nDGfgxMUvm9IHK96yaYAzoQRuyGqoPdV3H2kfj_ClNu9XxAz9aKUWRMQVo50GViAgg7Yt8vX0M_kqpIIRJsij7MQ97GLO7qGAQ24m6iqRUZvxclRVk7lec8PN1SXx_u7kbEkxpjGOh-ksAH9ADWGXlZr92dlv3Mj8Epv1h5wFIT338zTnTSvlDnvxNmoyR4JtfnXWtfoUDKtPE5QdE1wF3c_owzbecxDt3DsapjaYRZfqRVI1Hj7W6nWBAuxrzKYnblRoo_ok7WIeJ5k79o7jnYinvoPFE7NlzQLj-TxIbKFsJ4MRvTYS9wm8ddlfOuLBWpzDHxdIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFCFy_lfJgo9X4t1EM7vUWbEf-Pa7V9zlOVYrSCJ6V4Bf416dCekF25Dkp8o4GcxqdewAHZOrwGJlcJnZwaPs6AHb53j-UQIbDuNg6TOLcyXCL_qqvbc7eiMpAamxIc3MnGLlQ8NfheEv2ZxwCsPKRqe0WTd95u9dVfIq3dBZAWFfjxXxLSR-Je68Dkdd64Sd7QpIhGqFKnkz-_ma4NzcVvGn3llnm72DbW_SCRTELQaS9RLvMps7agP7vnNbLdJNZrWfxf_OJ-jjdcPN_e_1aImbduhKwOi-x0IVRFOM5K3RhAYUU_ojFyczwERdZ9hixCYLlC1OV_Rby3FTY7jfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGpGGyKHfwRRWQHVPHxAPVL3GZiOWbZe9wsE7DYfVoErSugebrYfxYYTjGmi_8_hm5tJ4deiS-RS9OVEuVtPbVfh0o6diV1DQfOnzqfkgvzD4fvtWeuAGPXfEFpWo6rTkTiqNCvGFNhpK8vYJYW4PPbDxxs4bWvHBZlbmPt9zoTWNX5S_l_DyHmApm6BRhFt2LbBtrWZ1FfBj0sHzdj18uNtNvaCkfQkz_GpNJ5rkfrZY7IKyVMm1JD3dENsozW7c2r0bGmSM5Y3dtwOnIbORWg8A5Fg1LyHJ2_4KDCysFZlPrV4vHDUiEFC0rZdaCC2oQYXyX2GtKCTW_ZXc9iqSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfwOw8Za8t0PtIPsVDouVPtO802aJSriz_dwK1SC243v0i1ik572isitRXcfvx795PTZLocxcu4_s4jNABGj2iZW_UX2VwjmVfRhOYISpBRN4MyfxwuAfEwZyLjuFMxg-pIejIyQsDjrmNPx-Hc70HgDM9F9BWsrv4d6MlX8FJ-R2-Mm5pEYTQ6CTjQmJ-4Uu-FTDhmpPLNAgg1lGO5svjTXwT_kjeqn9rd0EojR2Ua0T6d363hMKUmZjacJQIs5kv1gpc76Dpgl2_D47chxtsYwzyn7sVfQxtD2_KtcT3eoroG4r3tB-DD-ARguG3BJFmDvcHXVuFJt6CuhhQTtYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6t1ugLOJfdniXdUdnNGlJgfU60B4twEK0122Omz-j7N3AjBy0A8tqb3Q8FlUo8TkXezr0-WF4ntHFvsylAAWG0ncDDprVFMKhExRyVNrbF-OIUTXIb0x2SwX5wIk3Kqu8le8fBH1rSo7luQOomnKEu7gVN9wNVUN-d1M4iddwE7vcEDKj7spvjLZpt1gVNCwPcMO4z-OBNxmKrBSwDLlEFG0KKMG59xNbt6rgYt6-GjHiwHobMU7XReBofKNHRfSU0RzkiAwTjIbofqRsyqWJeujL33kzFGDXDBiprqFVww4raDHXkwjSlRweCgVkpXrZCrPHCgD6IaSyj0_fWhig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4nlmY7OVVI6Q-MKuXd9SG1LTgBn2tv1_qdjJSRo01sRVfYoAiHhiEpCvMW8M3oYaSzhw8oXI1TDMkSjJazY96RrktdALsyy53GZ7TpFzdiAP-f7r3IWw5KPIdqA6FKNBRXWlPDHW2xAqvNza0hSt0fgPI9DXrHXO6vW2gS4MzAKLrr9yBQwc0S9TyGI9J0R-cSE7Z6I4do24R3iq9PpM_03JqKMaELfjyU9451QO38-TSaP9kmcE70Vv6l-erZvSUJ9qDvCHF5mhCW56V7ltDdyMVu1pt_KWeFhAfPNP9mlGJmy1wRFI9b4DBdYorrmqZ8EIrszQ7Af27VogjYI7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6GWqNaQ6qvtlbDiWhg5PigWD_IaCTGJunKpFFhghgYCDpTs3k49LDHJj4lHQmatWkx8v9UKAZS7F7w-SQA3tkzDS7V0BRHp9snPMdNncZ00gVkondSolAriLav4T9PsJqlHKuLun6nE1pDd1wiVpUd2LYpKFA0Y0NR9lKqdF84AigaPrO2L0tA1-NtSD1HEuz7TLffNVt5WCiiTnu5FNs1UPgxVO-qbinrCLz7ltUupg1JK616-ZJxx44nIM8W3ScukzFal-O9LwHDI6ZPBKLpUpHd2S_sAb6lanrqIv5ShJtKTJnEC9Gz2-_Whip_qUTt6R9o5Htmo0BGjAA3HZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSZmWJF9_amfv5bINaaa7OJBfSYiS-uKjIHPqJOzy02TFdig0f7MNXSc1WM9-a_yri25P18abvVid6y8pb6CLU3Hdpp7LtWRFOcfucOsYBW39tDmOtFKVHHxVVe1Xktc-mmagkhMDF8mca0UPCx8iSgP3VL2THFw9yJpYAzsZDqX-mrB70XeKSOyuM0vh4WfY9guME3AsSFkCIK-HZ9vNQA6_KsToDPbb3HxoSz4u8d8fZgMZA0YMGArXVZSj3LPHrx5lHm5gOk_pH5XQqQB6AvBw36_DNpi4BZ6f0T7e0tkGb7raakEBZChmNid-5hWwaNaAQSmQ5GI0JWcT_1Djw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foAnSrTJcwH3dgiGjsa9Q2r34C_JWIoOgeWkkh5Y7uN2w4RFtlKOTZbBGdqKQVMNNg-lPjAfVpyUpunufhO4GX7_mrMmd_tzuJ7NmK1vsEpN2w0am2gBJfh4ANUawnh1v0CHj1Q2w5asJbAVrivrXOQsuQoz8r7LSRR7CMJ5-SeyMpJOddb-P1Gy4fYDtn5WwrJyab9KaijKWRUE1JKlmIEVGdba8CRCmfVYnNEZUCntrPwt1jGYclxB5m4bLxLlkRcxwFADC8LgQi7BgDEocq1RdcA51nraPIgYAL8Bmr4ys_yIjqEtD7u2hBlWZQFf0RFQyzOhBiUwTaM3Qtip7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiYeGWcx3q3A4wWUprrwI5FBPTbtKZijV2Ag88bmmEjtbDUVa2pFGjJ3IFV91NUzzU0aGykdcDMbI23xaoiI0l4gA9OqylcUICaVOmGZwj_kttWk24EJxnCvjsEGi6JJCBdh5I3OGNGGPiff_Z3CnAMTgssoEpFtI0RB18D63Z4i6cPlGTvsOdsBfViilPJszWZ79TyT9Cfcw56ijhZkeg0jVjREAjfBit-UX4eqBh409v4BhayIxyGhBu7fplSQsDCUbkX3zFGd9nb47-8DETjgzd7mDUjnOK8TSEnTo8QVidNBbODFsYTs2SuojAzNu7NUn0NsnrGljyR9EdA7pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCLP8SpHs8eR-Vbr6wYyUCyTzKMyCVssjeQtx_sJe7AcQ8vyfxw6SYdfdKHmcRw1qQCiM2xGd5y5rREg1R3OuZbrLMsd4CFl6H5jZhBxdIeEHkFugrCXOWbFVlWbEYoEJZSRGJsW2kYfoG61C1PhbFYE9A0xEZ5q_I6zLrwZMRd-03GFEKiutczMZNnhYUAqNbgqLu8FNEsaDGIjMDKVIbLSoVGgFbR8W8V5C_7j6H3dJ7RaQbfGkP7Kb1IQ7awNicAxJWviO10NgdzPot3BAQ-xlwurPUumQJKViSbXIkUK1uElf24SJvRIdMrfCL9xxp4yW8NlvdVAswGrpkcN0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eruPQHHEDeyghDDZIWQcwJ_X75AnO69i4-lMoNt-UDErhYPTaxFCCRrLduSo5Wh5fw2KwmpNNoU8E-dMnLjef2rrBKBWmI1MSr0w8ju3XobtYIE5ZWHzYBe6v6ukdGOHg8i7rwzjIIduZxLKUzGOmjJhjmrIkgWIbDxMUq4M-xsWuAPTDYmUsflY5Lqp_GlY46eT_S6vFvq-4XpH6PMXUDaMwH_Jxvciz4LI6kbcceK_gX5JlBa1QKefkmtMw4Mp63pr9pZrdSQwu-n7OczChadn2WepChUMk2W8qxUG7qppV6sHgRIAsLy0xq4cao2FI4zm9-mOcozk5WSqlW_XeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=MlssfI-1mdYvZz2AdKn-Rzaxx0Q0_WWLoMbOukCNyGneem16My4PFNWe0vUl9bMxLpht4qwUgmtaDiEIKcgesPVS7ztR-IqQId8uRDfwv-d0b2-GZ1CCMhh35Vh6fWhuDtFmrJ5TKl3C1bI9VZatc0j_RE4tY00xHZOsjtraWbtU898G3n_gyt4KZWD3T5c0ttHLTAvKtdvJybpgVaC7AaTquRaFPGffkTWpJi2HU1DAGRpLZnDVZW0fOQ5X2fn7O1yioM9OU1jNCzSUuWDt3HnY8Hsn-m7pPJYLMy8kj54SZuTuUSNxYLLOaZPiENE3hx4GCgddGDmDR1Pay5iMJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=MlssfI-1mdYvZz2AdKn-Rzaxx0Q0_WWLoMbOukCNyGneem16My4PFNWe0vUl9bMxLpht4qwUgmtaDiEIKcgesPVS7ztR-IqQId8uRDfwv-d0b2-GZ1CCMhh35Vh6fWhuDtFmrJ5TKl3C1bI9VZatc0j_RE4tY00xHZOsjtraWbtU898G3n_gyt4KZWD3T5c0ttHLTAvKtdvJybpgVaC7AaTquRaFPGffkTWpJi2HU1DAGRpLZnDVZW0fOQ5X2fn7O1yioM9OU1jNCzSUuWDt3HnY8Hsn-m7pPJYLMy8kj54SZuTuUSNxYLLOaZPiENE3hx4GCgddGDmDR1Pay5iMJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFsKDTIgsfhDByV1XVMcb6o9I1Lv-KW1fHq9TGMO9VkEOBWj9d6ehTO18EIk70UvHR6gH8ijIHgtRCxuwDCNxJpEKs0zkxG9nLQNT0RotkRtYz2Z-Gf0lgb7-UJ_O1UqimN--nJItizCul3VsJkKuVtc3LrhS5j2tI6BZcLwdgr8J8Rm6mXE5fjXq69kK-u4F6-EowPuD38r9KdCCPeTW2nC02G0Q4JcQdHTk3t0mH7lhIq2cWGXK0IbMWVyrtfSTeAVEoiqIyKQ0n-XgdXUlbWJWaAeQGlgWdU9p3wtTxpjqHO8pkVQdVXRsJ_ECMT3XT0CrPV6DN8Ux9cE7X1MZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGU_kzV27DOTffUK1JtxkWQZv99FInZ9bkapEMQ4uXb4anbed1znCSppFgU7CxME8iDFj-IUjJRI2JY8S4m9nFTuxFFDPcIqFUZDf8RWa_qwKEGdggMqWuh1t6iF-m57gVRKTinxXFLQmjTungcsu5V_Kz2YKFMkivnCh3xbCNNvUpMnkYRajLr2HC8zRrqdfhlp41HLCnKAR_VOGFKBff9TDAIGOs0GrtchZ5myZ6B7j7YRPioQHph6zjZTpckSxU81hj-A7m6Xxq_zbm9kntEMf7qd0meycgsDvXAetEAAeXJjEiBmr8o42pbyezBLNgNJgWLNef0E7iCRzm2SMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=lQQRDJI4I91vLH_i2R-9PWA9cqxWOBSMVdRKCArEtUlL5ybKoMFFfk0ZAl-ynxD-Mp__oT1JZfFU9tyJxzsNRow6Pa9fM4OeTzf8iWP6jQNc0rpcfhxVtWINOT6hCkAnXgEVKEi_owRybwvxciaHzPtustIr0aaeX6glVdozBd188TTwYA1lHDMXCTGxy0EqZo3jQpZqS5uCOBtWCgTZBKd5oE5reB2BBPd19-jv5ooTJcCrvu3dkbrHdhllhCKRScJFCsbFqNI14CUNMba6iXF_G3WK8K2-KYGEMZ7HYhgpn_Lj2KMeX2WQn-ijerUxjbxpb5BFX-JqXwxtsXP2pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=lQQRDJI4I91vLH_i2R-9PWA9cqxWOBSMVdRKCArEtUlL5ybKoMFFfk0ZAl-ynxD-Mp__oT1JZfFU9tyJxzsNRow6Pa9fM4OeTzf8iWP6jQNc0rpcfhxVtWINOT6hCkAnXgEVKEi_owRybwvxciaHzPtustIr0aaeX6glVdozBd188TTwYA1lHDMXCTGxy0EqZo3jQpZqS5uCOBtWCgTZBKd5oE5reB2BBPd19-jv5ooTJcCrvu3dkbrHdhllhCKRScJFCsbFqNI14CUNMba6iXF_G3WK8K2-KYGEMZ7HYhgpn_Lj2KMeX2WQn-ijerUxjbxpb5BFX-JqXwxtsXP2pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=tj-A6DNADm4FyoqKAs-bOABjQ4oA_skXrCWet_Zib_gr6ACza0dZpqd41mIn4D7nRPX_V3eOtSdlepdMBty0qwyj3jWwydEm-K5UpX-hDvaJxZve9syyQ0ePh84edAQkI30nhLEoQpaclTMikL_rSAgVOnB2KxgFXNoTzvsI12E1LiMIs47TP6rgIm-dYR2ph5mHgG6eUwJBDTnckjJK5eaT0TR_tJkp8yib0WDHdjmhBQSiS052bMvjCF0YlB6d49myjz7SYxwtR-J5cObvlYQwKX9047Er5rmeW4wK34mLU3Fdk-0fO4Ql6euXW6hXIzTdgj1898ZxJcT5SlP7OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=tj-A6DNADm4FyoqKAs-bOABjQ4oA_skXrCWet_Zib_gr6ACza0dZpqd41mIn4D7nRPX_V3eOtSdlepdMBty0qwyj3jWwydEm-K5UpX-hDvaJxZve9syyQ0ePh84edAQkI30nhLEoQpaclTMikL_rSAgVOnB2KxgFXNoTzvsI12E1LiMIs47TP6rgIm-dYR2ph5mHgG6eUwJBDTnckjJK5eaT0TR_tJkp8yib0WDHdjmhBQSiS052bMvjCF0YlB6d49myjz7SYxwtR-J5cObvlYQwKX9047Er5rmeW4wK34mLU3Fdk-0fO4Ql6euXW6hXIzTdgj1898ZxJcT5SlP7OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=MGxHFIjPRN0bIjwKRnYPsSUkyfobp5AUheL1vmjpgYD7bS5JM7eqLVMQFKH7dx8aldl8zn1sbLkg732L1sHQE9AsyuRt7HpoyZAY6H9nQzduO451XJYBTBBb_g-5TF2gVDmqEtDFIzuKgX1nLdGmlyMij7-zRo6D56AoYCdNR9SdkHZu7wksLf1pWIWPG3picdUjAHrxF4fBDY10tpqspXg83-3dnL4wuGzp-DcLhNgtDMXOkTLVP9UfyPudI3qmXX7cGJxh0XozUTh_t02R9tJvQYPMeMZN39ZnrGQHuotCIIKbDJbZUR56jFTnxBWR-2jmfzaxgKLsREZIWjQwlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=MGxHFIjPRN0bIjwKRnYPsSUkyfobp5AUheL1vmjpgYD7bS5JM7eqLVMQFKH7dx8aldl8zn1sbLkg732L1sHQE9AsyuRt7HpoyZAY6H9nQzduO451XJYBTBBb_g-5TF2gVDmqEtDFIzuKgX1nLdGmlyMij7-zRo6D56AoYCdNR9SdkHZu7wksLf1pWIWPG3picdUjAHrxF4fBDY10tpqspXg83-3dnL4wuGzp-DcLhNgtDMXOkTLVP9UfyPudI3qmXX7cGJxh0XozUTh_t02R9tJvQYPMeMZN39ZnrGQHuotCIIKbDJbZUR56jFTnxBWR-2jmfzaxgKLsREZIWjQwlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gq05om13ZktP1Qt7PjVcZjG11Tm6nJbLpizhTKd6P9TVo1b0cmgMWOlc6L-yy2ROzV4vx6GlqCUEBLGUgBxkXzrc9_Ad3GGBMckVCn_x0CttSJSLnkP5LRUOcBc-2hgOi6iNh-iN22GiWHnqpY4wPnDShfmojgb2xBcdaNCs1rUZ89v9tiNzHJvXRCk4OWIxnGuNzoT3q9DVgsEfbMjkwv58eLCER5U8R-1ZHcS5lOZ07BpmQPy6LvujoY7M0QOzjQFbw5sSt-uhz7pg0DEICwrckLh0wDsqNB9Evq6NrBHL1XkGKv1l1bzhDjD8-GDcYMyYVCgOCMZ77vl-qgCuXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=tGkohFy08N_RZ6XefTb1G6tXaWV1TER8fhYkMAZE3Xwq235KCtxOj3KvWHTUdPbksVGrZvA_YV1fxIsBoKZIO1fea36uS5X6Hroz6OTlX_Ziiv6ub-AWoMELrSYMS9ZKt0Oam7QtIpxBy_C-hvdCxlV7Rv6VGH5yhnwxvTAIpcyCK1wrIjg68l-CkoXWQIJkPKn0JUtLcGN_-p-aoJWY9B1oBHnQOq0lW3k17D3PhuDPQs2PZcuSLDKpYJK11lhtLAMii2bdwMs8yC7CHxVIZbQjnq3WF3ApaVVLmm3TIPv6LlEkuQjf9oWb5FZOqwHIFhhFgaw5z93ooro---2bqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=tGkohFy08N_RZ6XefTb1G6tXaWV1TER8fhYkMAZE3Xwq235KCtxOj3KvWHTUdPbksVGrZvA_YV1fxIsBoKZIO1fea36uS5X6Hroz6OTlX_Ziiv6ub-AWoMELrSYMS9ZKt0Oam7QtIpxBy_C-hvdCxlV7Rv6VGH5yhnwxvTAIpcyCK1wrIjg68l-CkoXWQIJkPKn0JUtLcGN_-p-aoJWY9B1oBHnQOq0lW3k17D3PhuDPQs2PZcuSLDKpYJK11lhtLAMii2bdwMs8yC7CHxVIZbQjnq3WF3ApaVVLmm3TIPv6LlEkuQjf9oWb5FZOqwHIFhhFgaw5z93ooro---2bqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7622">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy8zjaj7PRbWxrD3oGD617QgJNJiWsz1YlPKCxl8f3g4JXnkxj0_TzVrqCBjn1Swu6qxYVNqP3EWXYElBMUGTg48EkbZ1T2WTAZtkXj13qzEf67E_ro8ciQV7Pg9FehmvNzL8jOr9iu75JhhmQFbRjv_Ukh1bxcHym_55fUbbBYEKWffZcRzmgvbnO0xYQuXlgPr_ALyep7qojwr1tt8WKsAjKbbsfaHH_iZh-165OThBCjT-kxy-vbAW7KemY8K24k-6Q1YkF2U9a_RxHEPRTW4aANjQ4h8xCub04VcnyjSHmaXujAaayIUdUALYB5Pbr-eCecpRtUWSplYWZxDWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSZAxWi5psWHWo4nh7dHWjga5M5a5ehhy3sWnDb0pkZKhUfjGTEadaXC3nulAqp5hA4knzO09zjzsaXP3lJ3gleUpJ9H2iysECMAnFNlKFH9y-osHXz_K9AbQXgXScFPshryV4oO4ZmjrTp4BD44WYhGy1fqdUXbvbC46c2H84N9hyC5oBLVqx5R91fryfv9xFeYWoyq3gn_sOtUlhh8QKLw_1Ux2x6sGrBU8-uc69QNrc1Ddmk0JP4TgHF8ziQQr8BzJj-W8T57zYGjmtIfQGoYVz9WQH8-Uo84Jd7N1-CXYQ0ATT0zOWPLmBclU84lrxT6FQPcpmZ9GRnFeXRi3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAjL7WQtosexCo0C22U--ikU-hRXQb5zvXjNiSSPi5e6VNo3buq7UrL_dZtOg7ZEvKRpcT_PB35hOSBN7qhfT4pEaWD_aUmbXPR0PgIfmP-2Ckn8FAYkglIGEvOrCrvzWhZJU8ZypssQvDVDS7qwRIQ-vwm-2eo89Z__wDaytvLxF1Rgp_z7Umybm9htTwXRACd20F3CtcIB7jypNxJ-y5veHpVpYvhJGuMUvVhCecUZgn-YpoCL01BfQNbYLmgUvRhA-3DsLKi05sVMVliYRA2Fdr4qNN8qAGd8nAfSMoJCcyQUf6-pSaDLaohZQ5geeLMEYBEikV1UcAeHw4RDlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxmkDPDRnVXZPGPwLmvBJqN5c7NuS8b2BUPb7rdmsM63mO3YNfU8B8NrkWKTUPHTZQYfAgRR5cHmdn4WVUPQspz8Xzg8xiz79FE_bMqIRF80740kwYZD5xkqzi5rm42ukeZVMuOu5EVNg1FkbvN8x8r1rAEIz3mnw1SIfW6CoSa2zvL0SFSrQD_qFe5lY-oP74pXrhZLnGHSIX3MlNRlds6ZucAElEpcxa09O3wLVs8umnrc7HYmJVFCq-B8ByQAVdegugJWuv3LPEfJYp-d77lDBDMp6CYaKQfIRy9sbomYGuVhhltMLDtDY4UZBKi3AI2hWlw-ZRgBAHpNM6DiXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONoPHLjPAMeVkwsnBlbI-oDgC_BiAPD0FjgRXldq8CJ_aIa1t3FyxC8K419F3jkxr_k896yJ9z_ZOIULjW_-NnLXMzwPiz4ICJs3-FQJbmodQJxsylA94f15krOmJfVlemqf9rhQNfKwg_FabTHTbfqocunvmAfjh3yccuyPfCEHSNVFZ9zn000vJ9Xl-QlIUV2MrEMDCQ8mxAnrlgXcJsI1fP8iGXLf7-XEfKaUBTu_plBMZnvVNxcUks6ab8oXT4yWu_f8D8VPYx8xNVQFFARd0BVY_Q63B1bxdoukA6OgIhINlmrw8RbMfyjKlFJD1BqO7uZxnAt5EazoQvCktw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8zVo57mI0daf-XUtO5cE1dwg9kcotXiUxfZaxUCWwpT2U6-4xMPViOVzuhz0PApdUAt61UCT88MLzoGWIwrTOu2A9opOqZCw1ZtWzGt7yTNqJoSvc543Z2ymMBaToOKfHJ7IVGZQ5_gmDqsrMsWsmNk4Ofrfp1ud1DQ8cg8UtsUcMT9mlx3dSmdx5sZh6uGXAZuEJiIBAdOoxuEBKOnRiIFOjgqwh0-2zIj7uxE4mk-LXe2KU_KMDaKhJvl9wfYilU28RpCPZRebY42X4IjzVCT6BCnBOGeNe035JRnGe8Mj0iNDnU2JyDj96MixNdkldhwGKyF5210dX6EDJOZDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRws7Y8Ms58CX2JncjWILYzBepDdBtJCaJhmceHx5SKPeCrAByE2Jo3S_k3WOu3ewolgrS4IGVAyRDiJwMxoRNyHu7gVRdR25S4w9YsN3JNi6mTGhwcX67RjIdos1K9WUBNXIO5JTMBQZkC37fp2xut4djqMGBHHgdSX79C5MSwKOssHk4HPce22mGASqaAzSCff0EIOF4g4jHflqzWxDdTLKL-JBKLn9gWTdkgHXT5DbGMc9wz7phChuZbfVBiRBr1WQq2m_KJjDDEbIqxalDBxx6e8Ia7vgdoa72gHDixfx-oozUB3W06Azn6IXXKCjd_wA3oRfcXtdr9tXUHjsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNMoTbYmoDPIiGqw2nostHhxc-cfYFQbVbrIDXgTUAPMn2VNw4lV5iLjpeOfv6r8NyYn5XaVVIjFKb3UW03av3e_ABzPhu3RM0QOtwgdIAmMGEWIXXTMFNaknGgvAeCgkFul3LpjIRoZv8Kcwj5ke0IncpD7Sz8wBADzPhCvnSdZY1WNzfptVVm3l9sXzO5gF-B6kIjraLQ8wAAqpdrnxdziaIjucruBBmUs3q4r6bsRYUv4_Q-vkl3J8YE3oy7xvZQKjvZIzVenRdTnkzkj2kTC8K912_a11lwSJxge-3PfmpZIIRSxjr4uV46SoQ_3l9mGGZALFzK9OX6srPs72Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1p6w7EJciJGUrXdZnmQievQJ3QzepcPawbZQ_1-D_Cv06uZKZgerKSU6viPhlvLaYSAZODR-i3nHSapsEsks968FZgAn7c6-OMcXbdk1D932FwRbC9n9yBcAkZMWwFSjNpZmRYkZXLiwGDCMqKHVguKH-JfcTthjp_1c5d3-daxA4hXMHZsAG_IUnmbcU4TXv01AvLXzmuCcT3dDIfHIGM5IQRzIvc3f5Ko-Y2SaQN-0tffP7v9eD1Xygt8wn4l5E_SDLQrl7EGaA-Z68hBXzG0iqffnPz5k19FdbQQXUTEGMk64QUEVNngWeVlPMVXEPy30KsMYcGdVxyJK2GX7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nucNurd5bft9S29e1eA33AZUPqp176uNDGhrv-87xMo09pXClZa69J33rfjo0PD2MNu9obYGVtFy69jIPo8eHEqtRisPgiSIJPk36Rwys9ow3s7C4OPwIk5_htOohkWw23fATHPBUhPK3Ty9AMEU6zaRhKrdLTTZxm6wdX6Zz010md8cAGSPMIhH7R26ePedQF2tQ1ToIua1ZydqTivRSPI89BF43JTtfx2-HRDKO78mdHgMFIDo68JjYO1_LLp58FNskOlEfMt91xDZc63VthDFRqO3TdKMHwqT2nAvjb789eGVNKZrnUaTsYr63HnkXs0_z1tbHUtwsOfY3Az4kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KY7ks0Or25ekgqS5OluSISz_OPgL-UwhahpC_tBrwCzbBhfTT2L7LBN3SdeY81qizLynNhnTOPq_B-5GOPBiPMtrZnWj5YrRXut7aI2xmtt-4PbC0hWU-4fdopZ0B0gdbKSCrd0x4MhIozSG3SHxypbFlZQBIm8RoZ4L_TBUQIB2tpW3Wmu5I8_WKxMIGY85lsOlM0oMPVI59zgucSJvuEdRpAOE8skqCeh54KoeqbaW-vXqCuLnNGpUIj7_rabBQZlUPhRluZ5JRdbBbrvLtnrQl2GbP7MZN5-rX6G7u5-6F5LLGKjUtOqHvPsCiXooM7v5f14HSkClaGeS1AUpSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2Kljjg5xHyz4y-kCTnrisF133Gnl04tt-SJqSxUbs3RZW2LOZEOZvfpDLn95CHeW_rWA5U4H-em5llvia2JyFxlDV8vVtQ1OB4qXAbFAIoYQiKol-4YAHR2TVTOQqpUwx4RXZFFODLkhIys7M4TglpuiIyqaqr8ESUvfcBAWKnXmIp950Nmsqx01lobu42kU_oDvu1KgjE9DeBAmJXMX2LBlsHozzAQtVBsfStg5LGylHecL8mVUL91cLOza3xsJ-fE7Wunlkl5EZNjncLhbVG9NJKyFsTSoHIwVTLhKxDaxah4lvS3QhmEJUVkH7LLN8zdBKg6-f8BttDN-w3UPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3jVuTOqXjJFVPdQmFGLC31DEv1_RXxQi5nO_qc1g41akHKhxBidlm7rqzz3glQ2Z7v0PQtuQfbNo1Qt9zCA1aSOJZllaUDOayW3WKkSZPLxCEdce_D9NQp-NUbVnMpjm6h40lG93K-uTPawCAjghVq3xUOfut1VinzPoEezOkqy5FoODU3yUMzYZA92r3g0pnqal1eN01rU6fuNQVIiW67QBIv17mcESG3csmYfV9urXMQ1a6jWiifqudXESWQHuiiCasNTafcmlTSRZzIGtW4CyvQYO56TMIfb8hSe4WAsiTT7F8WBLHt6gfF4jPnmwfvKxNKQAC4YwOunVbBRAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZtJhyt04TYVwmks3xGVUDuVvKcVXMJU9KZH8xHlEuo273mGhP6uptqEQsSCZ2UzwwGwCCE-x6Wzr5zgR_wGnZ48frqzMGbK9h-2wUquQrGqyqv_gOpvbutxvrZPNdJ_8UN0nTlqL2BqV4GbZtaoTX9Jgc_jtOyQl4NhJ6Jj4mz8jQ7-BLdYJ7F6Fv6j28g7OfcnpjUgblZvLRJKneyB_GsJrxyVkzi_OrFDjpb-mIuBw0T-mbEB54BuGe5Bp9vI8J3pRb1Dy4ZrhmmjhZWtH21lEoaXRx4UaCMzOVxNH2SzzOpxaG4fwMXA0PjkJZCsmLSIVJByNqcVDTtRluLvFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwKIWCBXer2Lz1LuU-wjmEh5YEQv5dphRw6yLfF3dUoynLhErDYxMXgK4V9dbsxjQ35466MJjXRSNSvL-06Y4HEHfPmZu5ofDZI3eWfzX0hminliCtkGsB8KgELmJkGTMx_-Y_H4asp4PeVX-F5Ak6hO1ZNbuvUZH3nmwd4T3N0D93W1r8ycZ70NNE-xIbywbnYGcnWM5SIso335T3ut6ZR6CyyMe64HLk_weAA1wn7O1qYULPdyzHRMsfnb7N48iKqRM8bZfFAYLZaGzjjWxEsrli_5eqjpNp2h6OBCVBRrXgNkHY_5kGCEW9qB6c--GcRSQvpmafaKLTG32_Fu5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEg4A1L_kQKtXIsZJwSGZtGO6U5-lTo65B7hXhltG4t54R8OVqKnomvCf3rzts9YSdI3dLh6hGqZJWfu3jBdvrlX9sTVDRz9IM7gdKd6Om07aW9DwWGeJ1nLCjQYK6PHXJVoqbNXMWVR6E7f6lK2ntEVwIAi_2WnzlIdxt5csV657IWot5L-ZWz71C7fLl9AOW54AW3c3gr-o9VW5GOgZD5zZCUcAcvUC_5Z4sk1g-e7DBJV4fAUdI8CCJLTX3WFaiAxJbcVXM5vn-Q9U1Sfe2NKUglYEcE5YdN4nTfhRIEccsKu7ci__jUqAZ6sS8aJxc_CfI_WR6G2Ii6jZVAnzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEj2YWSabe3Zwdldl5Gnr2t7s78gwoTEQBxiAO-Bz3TtjqaYrBuCSABnC5mwMNbDkp2KROxyp3yTdZz4Ui32_bNs3stZ2xiTHXFAN6cWHh4aRXv16zHToVle2H7acfdAvOTHDXb9EuLTkAgv2chGConSnEeRKXCkCCcnSqkBPsQrfdhbhpziFJC1-gJnBgT1HiYp1gfvYrfD9_RKAVTHr9W6Fjb5Y4LGhDq3crLs5Y-Tq648o02efH6bRyiFWQcPO7tV4PqvCSOmFvCsgHad_X_3LzN9cFmdvanGtaHlubheF5e7fxcHBttotz6wWdPKN4Mamw2Q0cSQdT_js96Nnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFwtZ7gdneyKFzdvzzwCH2WhoDt55D5tL4LLiJnzH5hUbc57AwzmtrZ9LI6W9ojkB7Kn9MuM7HJ1auurb-usbH57KRLkIS0GisGO0Cd7IObakQ1vAwdyFS-jL1g2qxOs9WMvt_znERsq2Ruvjhtz6sFsnjPHrEJlgJ5Nhoj9XNwOAQamutmbnsWbISMcjxf1AgO4W37ViFzo-H4IpOTPKe3vZsIBhgqFDhohnuxDpPonSBChmIAa-hTYmjywG9oJOuayAom3gaLjim93cLG2VRlZoy8-tgz3Rphh3MydeqIVUuLtg95liR3NQDLI9evPK48_ene4ZrFKvwE0NMVvzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=cMVzPP1JmoX7KbilhQIwITuLxolhXvw_3kDNI_R1k097Qi9IDfJKnLK2GEgDWHQ9XyGtTIVeUhkkjDWZdXQ_4ob87ICq0VTWduWxitAk5IH3TiKMzFbF8YnVAoLb79aYSnMMq7YAKeRqvkuaz_dMG08urQKr1y4wYbnzYp_0lpf1DmOxI6VpuCZr97G2bwHH3XqUwBL4h8rLHvP44ow-wkejglHwY4gelgc7lFKUqyJIyDVFOLOVo4SCdpL_lzUnTfHiDXgDMjnxldzA1q-5Wy17g3ppfqSF6au0f0z9Dzb6vJ6xXjGuTuM9Z7Znu0YwL00rFWwuRdjRgnZZXamX6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=cMVzPP1JmoX7KbilhQIwITuLxolhXvw_3kDNI_R1k097Qi9IDfJKnLK2GEgDWHQ9XyGtTIVeUhkkjDWZdXQ_4ob87ICq0VTWduWxitAk5IH3TiKMzFbF8YnVAoLb79aYSnMMq7YAKeRqvkuaz_dMG08urQKr1y4wYbnzYp_0lpf1DmOxI6VpuCZr97G2bwHH3XqUwBL4h8rLHvP44ow-wkejglHwY4gelgc7lFKUqyJIyDVFOLOVo4SCdpL_lzUnTfHiDXgDMjnxldzA1q-5Wy17g3ppfqSF6au0f0z9Dzb6vJ6xXjGuTuM9Z7Znu0YwL00rFWwuRdjRgnZZXamX6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3w_cuWkL_QVtJE64TgyeUlq-zOrgBUmolNLjPhF5kV-Nzc-8qIH_OS5r2IZuRO5uawTUWCvAbTNEIBw7VFrXrPJXZa1zEmencyYH7hjTL75aNOlcHspoFJeYmQceKViIbIsK9kRaavplc45U5_vajgsmfHzfIIuqCDVCmK6vDt6ofyG1B_a41pPvBhdfpBroHxs5kWoZIUhX9JIPR9aRBG0UyK5DyjNu4ooEvIg0tf0U5LmoRysAVGuztHsYX_u8-P-hVSG3LkVTlHQX_sWbndqGcik_ijUA8MaSaEBcUK9Pmy7VLvhuiEY2f3IlaY41cV3ka1azs06gRc5PqqPyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=TiKBKdlTGj1qwSRI-Dpt4BAfVWN-IB08MGlWnQEmcvhn3dNDr_-vWlMaJw-7d3ip73FxIT3_M5Jo-oXgZfdklpdP--ow22fb40Sl_bdx5w5zHebr3bdR4hJg3NfW-JBslLHsmVqilJsPHUttKHZW5xmWoxbf10SCEgIliJmlodWQXPrIryx9TnB8kXHgSPPnJ7JREXFfd-1Of7bvchz-HJmwVZacAe_enPpTWqxEgh7nduJoMmKB38H8ZzMyrY2Pl7qzLCI2Qb0htU-sABHdmJxfbx2XGe0oDVyfvZNE77vfFczbBUXJo8NbQ7JL6KPjGh-Qnorcs0Ho1uHOTyHOSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=TiKBKdlTGj1qwSRI-Dpt4BAfVWN-IB08MGlWnQEmcvhn3dNDr_-vWlMaJw-7d3ip73FxIT3_M5Jo-oXgZfdklpdP--ow22fb40Sl_bdx5w5zHebr3bdR4hJg3NfW-JBslLHsmVqilJsPHUttKHZW5xmWoxbf10SCEgIliJmlodWQXPrIryx9TnB8kXHgSPPnJ7JREXFfd-1Of7bvchz-HJmwVZacAe_enPpTWqxEgh7nduJoMmKB38H8ZzMyrY2Pl7qzLCI2Qb0htU-sABHdmJxfbx2XGe0oDVyfvZNE77vfFczbBUXJo8NbQ7JL6KPjGh-Qnorcs0Ho1uHOTyHOSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEAGjoHA9Ilv82rOX1xlnEQS21FZbr_pbPbrSPs2mLssoNKbmsi59fItMwTVHUYefXx5aiDRHbhIDy90OZEikUufxn_GFzzH21w9C8euqtEyjj3RoxkOje1R7r6axFTibET6PJxbkanVHuriC8YB9pwqi5RZOmiToOvl_Jok3uc-Y7bNvIB9Bv3IxHXGBL5qfZeskgy34Wx9VhveIbAwjjA9qJiGZmNMAHBzFkMLfzi9mjlrgSfKrDliFRAcb4ptQ7Zl1PNEbinFyenjlBfdG7WW9WtpJt2x5RCRDC0l23Kqm8ky4ktorsI8fzebte_tV1XEPMmECiwBNbzPl4Bu_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYqMO-WFfn9W1HZ0iOAcm21DTmk74LmN5jBdQW2502413SPFuDuQ146nyi695kNbMvtJ5GHtBNwWkkYERwgF1ePjpeVbaQrRiyD4CsVATXHterUKTAXnFGveREb-FJZp-X8VhN3CZNo8MpBEQtcRqc6qzJbbnIUmeZ8O2FlTLD_gqr8oZU_D-1tXKYS9kW1-o4Ys5swiT3QvisCE14IpLeMdYyhHzs56owwy9zSr8HFUQByzWh16XAx8V5VEhAiYAHftnUloxSj3edFTWKvf0t4oDricbqsp7vReTlSCaHaPkZX69Z3IdownIN5d9XMKXDB0s2VquwX2skq---M3jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eH_VUdF3OCe6e3xZjRqNJFsc6rkR9bCb0-vfOehN2wzqLqWBjd-0s0W08CthYaWkfPOyU8mtfpxTSr_sRavv6jR7qXR3QiuidJe1xkYSXaCDKatbefq0QyyszpnVZ2nVumvwvreiTZn50R7wf37jv86F-b_5-iR1o-7glYbVYYFksDAyF81ZVQWmKiHrpvHecmQ7zt9M4l5o9Wcn52BSjA0CVrb3I_iqMkHoDu1TiTXwgQIic0oV97kfjyT7JjP4GGxWJNxVF4YZ_EEuPi8oE015cVFVXwHt4QU5GysTKL7QZTyN9Ff0CMp29Kldac_dLHeDvyoGsPrz9tAUFGGSLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/unPYMS3CY4o8UbW1Iw34pCXWUIFb7dPAxschftQjvsk_QlHrXwgvlo0YA18siQbmSvlB8yliFif6pPpgel5jPse_rS7QOhzZ38Zkd-YJyk76z-iCb4InV5EK1Iw_Pz3yp7b18gYRsv4dOQpxr7gv6qAUs7IZ-7Ejt3Sm3IVr0olSA6DCMr-lPLWMYr65u2--ybNLbl7O74vtLnBxk-ja6WqGmUdOEOjT_bEoxBlfbUDmLa3MhiE-v_Dd9StCCFbkFuCeWceXQAtBgyM5tbBY1u1ft_W8F15MkE1Rji05GDSGu1yLEPoflUd1m1jp4Pc97P2UybV5Eqn1CG2TzCI0zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e0MffmhHJlo3-kmRT8QJC50nxqqTVSAMEaMJq8s6DkcEW1P_mIYEREq09V6lOGZsQfuBVc6KbW2BybwIMOXIKSqUjqodJwGEDy6HU01UAusFNv9NG4Z2rA8fHPJrR6TWhJsyaWNPBHOwgA-9CSAryW85tDJ3a596oyk6NJYO_uO4DBMjVVhpYL5zel33x-9kmT6CPsyXRl7itWR54pTh3AIUkzYMpS28QqZVNcrnTtqiUzdcY8B_tqM3ZYKPG_SzBo88E9bkwYXwm4dokr7Vu-K3tnrAYcwinqNWQIXtSCvWorHvc5Wlj8Nwolyyru3ceF2YBOjWnqGmfLOoBH5eoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cL3NSltuaIz9XVvHRL86pSpkrGqcuzUnAAcI6b42tcjfpsxSHQFFsQLkFBQx9oCjoe3zXVVeuwLLOVylLxL9QVxf3yZGaf_zWfWUlymoa6yNlkA05_Dr5QIC-QVM_0I62ItS-y27tHBAcNOJy1ViUGLnVQ7q2-ojRC1RHh__L5VZzUJ5A9u64tBTpWR0Obwfyt8Ve2n1ItaP92IBT8vlvGF6Vxdkw1zGXdNK0llDGs2lIg2MfvVkOgvYgexGH63miMhO1OyVgbNlC4QxZ7h9RoGG_Fwhc4Qg8gyk8Aaf3k3zxR-JPboSu9Csn_0V0OAT_yOYmnEb9TQ3qtIu_j9dMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKU742adYuQQD3ikud0HsMieJuAz_dgYq9QYe7zkEb_2x5mMfkVmFHLK9peFV8O5ef-VWORmg7LaDSuCUO7ArgytmdDvfdZFxokJYc-uaKD6rcjVd2OKQWt-OQWi1SYV1jroHZ6nN_0s0GqGdmjJ1l1hWlk1hzgWlp2orZ4yKR8LDB10FVcvAI2fpmpnCnkTQa0D6tIF3TU7dzT5FZKY-S4hTbn6kJ71GDLuEdQVjq2q2V-SDcAqyObwSyeVL9zVwyUpfDRUw4FYCpwSgHxT59jvbAH4mgEne1h8nSCh8T8HNWP8JtGaRO6ZPDAAxXWNWuscsolse342uBcshnRvWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSNhZhG1lSVa5FJ6g9AIabNdkXfsPpqdNe8BMxNmTDSs7C10rllF7CtbXDLsk3UWRBSmKM57Qt1xiZYvKcl9ByYi_-DGzHtYe3ZiZmdkMpA74PrpX2fBtnLTQTnBLk5VzwfMotvB3jfToUUZacJBHLWrgLGkWw0KMeqn3fhLBy05x67c3njIPDN__Hi-NZ4NLQ0d6dmSuaYVXSgy0CkVuo_hD7BK29lu2-TYCn5vCF6L_0BN0PbZLB5TBofRSBfL58IOKQssRgic28OKDIJcFm-UJg8iYRth9T169FAXKlNheioh2_SA6_Wj_2lfqJUQ8mdehDqngn6LsXdMBH-ErA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZ2banpIwqDzoZi9_OkUS-46LBmXsWYCOTwB896rV0kGOo9BUiep4H5SVRuV4x5HPCwUSyDsWykAfgvOvpBBDtXoR9JwmCe9iBA-JA5m6IAiFWR3skiWzoNPqAkC3HB78Qiu6ZCmpARSnF1z8UY5hwixHHTntaf7pVauDmsHhhdxexT0oNBwFLaJmEOTSP9ETwsjlkiQ3eABgQSHEnxj2E9n-rFaNoZJHxxWTc89VcDcpf0ub9lps-5jl9rqok4B6VRbA_WzvRZWP1bwFvld-7LvAQQkENIvLwAkPLhFHaAVt1aVKbyaMontARkLPIs6NXKxrVLPA0wazitoCo8mCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iw95X9WIX1-eEqvx4WATI8_frAS2HQHH3htrquTf7Lu0XB6t4L0KGbDpcaWt70CpblUSC5Pkwnklecz3fUxDmNCEjtx_xlWOIEPIerKXuHWqCP0BsDveWMjLjTaU5BFPPO1y7v16GiXn2mS71OvMVH40yvZWiwTH9vjYEyjInSqtLLZr2cTdxQWZ6L15HwuC-PiEef-UmUaBgCqjh3fGeBXEkquDQXku4yWPDT6SSQBdC_EfzpwkKii-GKZxDR-RPWn75kauRto282ok266SrKW6Y4RLqN-0RN3HI9XyriT911oBgmnyS107hEt7dz5xAGHOr-ONB5NQ7ERsAWLU1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMiRDLHAzvzF04Qdwck4VKSQta3JuYUVtVFj8AnR00wc4kW8pm6wNlceakXhtHfbhfwmNOQSbmyEMgGYmpjEE2zGh9UIUGN6zihH0zMcPsDY2KnuQA2aiCaDEKCLsxepxxNwOsu7Re5T4_ha7Fx5I1E8IFB4-HCuym8gcfwSX79PRYj-akQU1XaFMVxg6F7hQepYH8yNHXw6JOrUyS9iywLIKObUu3p7t-t_my1c5DEFvl5wpY5qhEpGV6wohMmRxpLDIZRM08RAai3L2dSdnzndteYsp5znFthIvMWFbyq05wwcL7nh4FDar7Av_qRQIJmaBu5pXZZhqrKxkbK92Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsaKm1VZz1nTPF-zKg0HsMLh9kMET7qxE7jFSUbx6K4DbT4SuWcTlhoTw90shZRIf7xwGQAEFsBb1HRE6_VhJD58bui1ENWK4fq62RJdt9AHFwKlatq0jMNtRY4TWuZjuJwFzAhXWJc2Vww8xiJKfCt45PjgkSirlcJ_g2uFG2_5_7HZLF_w5CEjYVrzbfXFdvcBax0k0eE2Cksq72TrzYq-2Kfl_N3Hw6Q04Lly2fhzJGFKcK7r9wScsI4XNU4-qpvToFteHZTE-_giQ4eQBgWIHu7UIms-JmnFJ7kc_u5PhAp73fKHxHNqJHl3vG6dsUicf-7YAXla93zau-eEmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
