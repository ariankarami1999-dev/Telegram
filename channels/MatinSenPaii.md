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
<img src="https://cdn1.telesco.pe/file/LlczMynCndLhDTTR40SntC6uBQccZM5lnwc5IdanEb0ja7SBwphEtX_7fGUXD6pVnqPz4wjKFfSQ9cuS0kMjzWmZ1FVX5DgPFDh4TLuhcDs_7Wi9Ns6fIsnPnEpei84tsk-RXMkUyai6kkkeKuw99nsyHmoYX-jzf0c-LaO5-IAWWjC1ZnyDGIe3bqcSCS6RRALV93-sWThEFHgilEhVLSRIQnTC_MOX52UXb7EDXffoNzJmwBPg7LdrmZhjx0jYUE18-604ZXSNN-CwJBKSIB9l47CQRDD0k7Gg6gjiaLQgTMcT6iwl7AFb62hvCcKLamxFDgYLspPrt6K0-0yWvg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 158K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 16:09:05</div>
<hr>

<div class="tg-post" id="msg-4361">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">به نظرم اگر می‌خواید برنامه‌نویسی یاد بگیرید، بهتره که یک زبان، و از اون زبان یک حوزه رو در نظر بگیرید و شروع کنید به یادگیری.
برای مثال اگر بخواید پایتون یاد بگیرید و همزمان توی حوزه‌های AI و Back-End باهاش کار کنید، آخر سر به خودتون میاید می‌بینید هیچ کدومش رو درست و حسابی یاد نگرفتید.
و همیشه در همین حین، سه تا سؤال از خودتون بپرسید.
1- چی دارم یاد میگیرم؟(روشن شدن مسیر)
2- برای چی دارم یاد میگیرم؟(روشن شدن هدف)
3- قراره باهاش چی بسازم؟(تبدیل به انگیزه میشه و دل‌زده نمی‌شید)
این پروسه‌ایه که من خودم طی میکنم برای هر زبان-فیلد جدیدی که می‌خوام یاد بگیرم. کاملا هم نظر شخصیه و چیز ثابت شده یا علمی‌ای پشتش نیست لزوما</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/MatinSenPaii/4361" target="_blank">📅 16:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4360">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اگه با ایجنت‌های کدنویسی کار کرده باشید، می‌دونید که بزرگ‌ترین مشکلشون Over-engineering کردنه. یعنی مثلاً برای یه تقویم ساده که با یه تگ HTML حل می‌شه، میرن یه کامپوننت ۴۰۰ خطی با نصب کلی پکیج اضافه می‌نویسن
😳
ابزار Ponytail (که الان به شدت تو کامیونیتی وایرال…</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/MatinSenPaii/4360" target="_blank">📅 15:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4359">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AWy8_ig4PFTx7ENI_NEAn2bR5nD2DAxMNwc7Iex-2MPKjeRyc0tmsSV5scKbtpQK5LXo3-o_kRd5JxlKBA6G4gYZVbFWm5uoLdCWGNfghTAta-QgYlr3fGQmMmyH4soad70IqfWHp1NkSqlzuVghSrR5arFLYC6dkeXjEEzw-jTGokUB8o4hYOGaPSaaVFlSFJmVPsOzClmtpea7Vd9kqmTiSh-eCjk8YAUI9jO7J8nyINYh6fBiTmzJWssFcfdoOEOVsthzFhdjdtnmsq9pD0JL0h8Lir7mdOIKHukZJDazfEqEg_i4-H96QPLh-q3EzUcS1klZM21K1Z7zI8lMPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه با ایجنت‌های کدنویسی کار کرده باشید، می‌دونید که بزرگ‌ترین مشکلشون Over-engineering کردنه. یعنی مثلاً برای یه تقویم ساده که با یه تگ HTML حل می‌شه، میرن یه کامپوننت ۴۰۰ خطی با نصب کلی پکیج اضافه می‌نویسن
😳
ابزار
Ponytail
(که الان به شدت تو کامیونیتی وایرال شده) دقیقاً یه پلاگین برای حل همین مشکله. این ابزار باعث می‌شه ایجنتتون مثل همون برنامه‌نویس‌های سینیورِ تنبل شرکت که حوصله‌ی کدِ اضافه نوشتن ندارن، رفتار کنه
🙄
شعار این ابزار اینه:
«هیچی نمی‌گه. فقط یه خط کد می‌نویسه. همونم کار می‌کنه.»
چطور کار می‌کنه؟
قبل از اینکه ایجنت حتی یک خط کد بنویسه، مجبورش می‌کنه این نردبان رو تو ذهنش طی کنه:
- اصلاً این فیچر نیازه؟ (قانون YAGNI) اگه نه، بی‌خیالش شو.
- آیا توی کدهای فعلی پروژه قبلاً نوشته شده؟ اگه آره، همون رو ری‌یوز کن.
- کتابخونه‌های استاندارد خود زبان می‌تونن حلش کنن؟
- آیا مرورگر یا سیستم‌عامل خودش اینو داره؟ (مثل استفاده از
<input type="date">
به جای نصب پکیج).
- آیا پکیجی که از قبل تو پروژه نصبه این کارو می‌کنه؟
- می‌شه توی یه خط نوشتش؟
- فقط در نهایت: حداقل کد ممکن رو بنویس.
طبق بنچمارک‌ها، این ابزار حجم کدها رو ۵۴ تا ۹۴ درصد و مصرف توکن‌ها رو ۲۷٪ کاهش می‌ده. البته اینم بگم که تو مباحث امنیتی و Validate کردن اصلاً تنبلی نمی‌کنه و امنیتش ۱۰۰ درصده
❌
آموزش نصب روی ابزارهای مختلف:
توی Claude Code
کافیه دو تا دستور زیر رو جداگانه توی پرامپت بنویسید:
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
توی هرمس (Hermes Agent)
hermes plugins install DietrichGebert/ponytail --enable
بعد از نصب می‌تونید با دستوراتی مثل /ponytail یا /ponytail-review کنترلش کنید.
توی Cursor، Cline و دیگر
ide ها
نیازی به پلاگین نیست. کافیه فایل رول‌ها (مثل .cursor/rules/
ponytail.md
) رو از گیت‌هابش دانلود کنید و بندازید توی پوشه‌ی پروژه‌تون.
توی GitHub Copilot CLI
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
توی Gemini CLI (Antigravity)
agy plugin install
https://github.com/DietrichGebert/ponytail
لینک ابزار:
https://ponytail.dev/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/MatinSenPaii/4359" target="_blank">📅 14:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4358">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">هوش مصنوعی به جای یک فایل، کل درایو C رو پاک کرد!
😐
چند روز پیش توی گروه جامعه وایب کدینگ ایران، افشین یه تجربه عجیب رو منتشر کرد.  داستان از این قرار بود که با Z.ai و مدل GLM 5.1 یا GLM 5.2 از AI خواسته فقط یه فایل رو حذف کنه، اما ظاهرا به جای اون، کل درایو…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/MatinSenPaii/4358" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4357">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه وایب کدینگ ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsApiGD54k35XLtFWJkpyT0vxuLzYiUcVwyXTxykcwWAeLPnLA0vn3t253Y2xWhfTMY6FRognk8iC340sy4pbPfkqcoqoAeQ9jXrIXR7RyEXE4y99GOsgYN4m5h4EoEAi_RZQLl4oYTNKWPPzdDzFPyiMNkY0rl76qLY132AJP1hnS_jnERkdvAmg38luNvKawK76ApIU9h1T3P1wCY5sxSbbJ4n-xeIBQgO3uFuEEPxJWQX8rgJEgITHan1V-0cbBrbfcGATLG2yTklFBPR3AQa64LTX2skJ9JRGsTB_-MiYM1mppmLvmDN5ueV2UsQijhFvmnYZ0v78R9baLqXyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی به جای یک فایل، کل درایو C رو پاک کرد!
😐
چند روز پیش توی گروه جامعه وایب کدینگ ایران، افشین یه تجربه عجیب رو منتشر کرد.
داستان از این قرار بود که با
Z.ai
و مدل GLM 5.1 یا GLM 5.2 از AI خواسته فقط یه فایل رو حذف کنه، اما ظاهرا به جای اون، کل درایو C ویندوز پاک شده!
این اتفاق یه یادآوری مهمه.
هرچقدر هم Agentهای هوش مصنوعی باحال و قدرتمند باشن، وقتی به ترمینال، فایل های سیستم یا دیتابیس دسترسی کامل داشته باشن، یه اشتباه کوچیک می تونه به یه فاجعه تبدیل بشه.
اتفاقا متین سنپای هم امروز ابزار Kastra رو معرفی کرده که دقیقا برای همین سناریو ساخته شده. این ابزار بین Agent و سیستم قرار می گیره و برای کارهای حساس مثل حذف فایل یا تغییر دیتابیس، اول از خودت تایید می گیره تا AI نتونه هر کاری خواست انجام بده.
به نظرم تا چند وقت دیگه استفاده از ابزارهایی مثل Kastra دیگه یه قابلیت اضافه نیست، بلکه برای هر کسی که با Agentهای کدنویسی کار می کنه، واجبه.
تا حالا Agentها چه خرابکاری هایی براتون انجام دادن؟
😅</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/MatinSenPaii/4357" target="_blank">📅 12:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4356">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OvkULflqH7YDugCvw6hdKiCxf0XSkSnzbraPjVStoVwaNFsHjBdcAv4Ume_BdJb7zLvecPSC-cmOR5M5S1fH_31zMbJYeH5x4HntWK8RXkskr0cczFMGRj8bX4aRxQaESj8KFj7U9DFT_JPEqV-pagS0rqFsahXfhFxx8deZmGovZxwPoGwS8EEmw_k30rSWX5kH2l8VZxTn08BKn5WeSuxS6uSy_dXrupJ2iCa1f86IBvr-dpmARBmVC3tHqrRzaScR8NM6djbOSR7zup63q5EJnJBug7jevUn-ruDKbMW2gyn3zF5-fnRcBlJScxolSCaOu9vVxrCw0Jp948yY_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار Kastra برای کنترل ایجنت‌های کدنویسی
اگه با ایجنت‌هایی مثل کلاد یا هرمس(روی Yolo) و یا هر ایجنت دیگه‌ای روی کدهای حساس کار می‌کنید، استفاده از سیستم‌های نظارتی دیگه یه آپشن نیست صرفا به نظرم، بلکه واجبه!
توی Hacker News یه ابزار خیلی خفن و کاربردی به اسم Kastra معرفی شده که کارش اینه که به عنوان یه «لایه‌ی دسترسی و تایید» (Authorization Layer) برای هوش مصنوعی عمل می‌کنه. یعنی دقیقا روی فراخوانی toolها توسط ایجنت‌هایی مثل Cursor و Claude Code نظارت می‌کنه تا اونا سر خود کاری نکنن.
چرا اصلاً به Kastra نیاز داریم؟
ایده‌ی ساخت این ابزار زمانی به ذهن تیم سازنده‌ش رسید که ایجنت خودشون نزدیک بود یه دیتابیس پروداکشن رو به کل پاک کنه! وقتی به مدل‌ها دسترسی کامل (مثل کار با ترمینال یا دیتابیس) می‌دید، هر لحظه ممکنه توهم (Hallucination) بزنن یا اشتباه کنن. Kastra اینجاست تا جلوی فاجعه رو بگیره.
ویژگی‌های اصلی:
- پشتیبانی کامل با mcp: تو کمتر از ۲ دقیقه می‌تونید با Cursor، Claude Code و پروتکل‌های MCP وصلش کنید.
- گاردریل‌های امنیتی: می‌تونید براش قانون بذارید که ایجنت برای کارهای خطرناک (مثل پاک کردن یا تغییر دیتابیس) اول از شما اجازه بگیره.
- مدیریت دسترسی: مشخص می‌کنید که ایجنت شما دقیقا به چه ابزارها و چه بخش‌هایی از سیستم دسترسی داشته باشه.
لینک ابزار:
https://kastra.ai/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/MatinSenPaii/4356" target="_blank">📅 10:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4355">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/885f71c1ea.mp4?token=mlzzQ4mCTbSOwn6d8ZOr5Qv4qkhLQHGDScHXkrmzhGBgWr8_irdo9yar-BC-g-uOKm9-QJgQAgtOPMJxsT4q-gNOj6Z6fU8LfOci_a_tRsEONqDF3Vvp9HWcJs6dgFweFwzXDAuSXI4JB07bFQPlhYr_Dz0lxmohsssx5VnZtoO0Ty7QWh4bqvQ6_3h_azCPBi2p1-d3KjWuul460lMPFrlwXhVuYXX1qowtU3x36zBLEUxiYqdT0hQDo3uORNed76UrNLAPu_o2egAQF3kQOmGCSlGMdtdGBwmwmo-OVZFsA_RaC21GUL7SnHzS3XhSPzpW9RalKuZIx0kiuFLu5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/885f71c1ea.mp4?token=mlzzQ4mCTbSOwn6d8ZOr5Qv4qkhLQHGDScHXkrmzhGBgWr8_irdo9yar-BC-g-uOKm9-QJgQAgtOPMJxsT4q-gNOj6Z6fU8LfOci_a_tRsEONqDF3Vvp9HWcJs6dgFweFwzXDAuSXI4JB07bFQPlhYr_Dz0lxmohsssx5VnZtoO0Ty7QWh4bqvQ6_3h_azCPBi2p1-d3KjWuul460lMPFrlwXhVuYXX1qowtU3x36zBLEUxiYqdT0hQDo3uORNed76UrNLAPu_o2egAQF3kQOmGCSlGMdtdGBwmwmo-OVZFsA_RaC21GUL7SnHzS3XhSPzpW9RalKuZIx0kiuFLu5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در کنار معرفی GPT-5.6، OpenAI یه کار جالب کرد و ChatGPT Work رو معرفی کرد. که به عنوان یه ایجنت می‌تونه کارهای طولانی رو روی فایل‌ها و اپلیکیشن‌ها انجام بده و ساعت‌ها روی یه پروژه متمرکز بمونه. به نظرم کم کم شبیه به هرمس، تمام ورک‌فلو‌ها و لوپ‌های پیچیده دارن…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/4355" target="_blank">📅 06:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4354">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">در کنار معرفی GPT-5.6، OpenAI یه کار جالب کرد و ChatGPT Work رو معرفی کرد. که به عنوان یه ایجنت می‌تونه کارهای طولانی رو روی فایل‌ها و اپلیکیشن‌ها انجام بده و ساعت‌ها روی یه پروژه متمرکز بمونه.
به نظرم کم کم شبیه به هرمس، تمام ورک‌فلو‌ها و لوپ‌های پیچیده دارن تبدیل به زبان طبیعی می‌شن.
شما می‌خواید، و انجام می‌شه
هرچند هنوز، مهندسی اینها، و نظارت روی کدی که AI می‌زنه، خیلی مهمه به نظرم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/4354" target="_blank">📅 05:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4353">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/802171ad75.mp4?token=kJgDcwHZ94m0TqhzZZY_wtgjGO8jsw1d1D08gtyFMsYTfqSRuA5sknwE2ieQ8J3c6XpbZ1n94U7ErpxU98WU8ZPsx2lRQoTpC9GVS9cJ763m9UCzxIG8ljX6z_Fp8m9DYjEB_LbLn553hRaDQXuNllGUXPrFJrIP5XrHiEpjGHSnLeOc59WHQxHjddnuMTWGChwsbR4a9DHDQv2_a851TWvFUGq8fkjny5_oij2AbtvRxh1ZbHquAOWXILuFegE4ne2VMpTSvkj5FinEsCDCTsDR9MlY_DiHO-X8lbzE15d_BqNO_Coezw-x8m8MOxXfTOnL5ygTNGI36dAEJdyh3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/802171ad75.mp4?token=kJgDcwHZ94m0TqhzZZY_wtgjGO8jsw1d1D08gtyFMsYTfqSRuA5sknwE2ieQ8J3c6XpbZ1n94U7ErpxU98WU8ZPsx2lRQoTpC9GVS9cJ763m9UCzxIG8ljX6z_Fp8m9DYjEB_LbLn553hRaDQXuNllGUXPrFJrIP5XrHiEpjGHSnLeOc59WHQxHjddnuMTWGChwsbR4a9DHDQv2_a851TWvFUGq8fkjny5_oij2AbtvRxh1ZbHquAOWXILuFegE4ne2VMpTSvkj5FinEsCDCTsDR9MlY_DiHO-X8lbzE15d_BqNO_Coezw-x8m8MOxXfTOnL5ygTNGI36dAEJdyh3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
درود به همه رفقا...
اگر کانفیگ میزنید و فرگمنت روی ip ها کار نمیکنه واستون بهتره که از دامنه برای ip تمیز استفاده کنید...
برای مثال بهترینش:
Chatgpt.com
Grok.com
با این مقدار فرگمنت:
Packets: 1-3
Interval: 1-1
Length: 1-7
اگر کلاینت Fakehost داشت:
Google.com
رفقایی که ابتدایی تر هستن داخل ویدیو کوتاه نشون دادم داخل هر مدل گوشی یا کلاینت که کانفیگ میزنید هست
✅
💡
نکته:اگر کندی در کانفیگ یا آپلود ندارید روشن کنید fragment رو عزیزان.
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/4353" target="_blank">📅 01:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4352">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">به شخصه پلن کلادمو ReSubscribe نمیکنم؛ تا ببینم وضعیت قطعی نت چی میشه به شما هم توصیه می‌کنم اگر تموم شده و کارتون زیاد لنگ نیست، نخرید فعلا..</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/4352" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4351">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88560d1079.webm?token=iKDAvkT9xXEa3J5e2rB1Vchwz9XJroTICgrtXEP6EdTprGnouxfjftyIq9KUv6N_yFFVh8RxBrq0N1rFZ9LefGyDIuanKe-UApKGUBq3vw2Lxt1SWclbksvv6nDzRvGQGRgNUBUWxZhiNlkT1TeUIlkkaEO57imjoZKTv_o0Te6uxhLvUp9OagC5exqfmAKfrvcBxnIrwo_ivuch8KIlAyZH6_yKl6_pJnmyQ-fR-k7Fj4Cpwj_Gsnfna9m3hlkyafkGJRoR_E9fGdZYPlGY4tt8sD3DtgrxtDVnGrPWYh42n_mzV3LbB-MtuYf8CRu1zeU_HvPuJTWc22_eQIdz8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88560d1079.webm?token=iKDAvkT9xXEa3J5e2rB1Vchwz9XJroTICgrtXEP6EdTprGnouxfjftyIq9KUv6N_yFFVh8RxBrq0N1rFZ9LefGyDIuanKe-UApKGUBq3vw2Lxt1SWclbksvv6nDzRvGQGRgNUBUWxZhiNlkT1TeUIlkkaEO57imjoZKTv_o0Te6uxhLvUp9OagC5exqfmAKfrvcBxnIrwo_ivuch8KIlAyZH6_yKl6_pJnmyQ-fR-k7Fj4Cpwj_Gsnfna9m3hlkyafkGJRoR_E9fGdZYPlGY4tt8sD3DtgrxtDVnGrPWYh42n_mzV3LbB-MtuYf8CRu1zeU_HvPuJTWc22_eQIdz8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4351" target="_blank">📅 00:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4350">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">به شخصه پلن کلادمو ReSubscribe نمیکنم؛ تا ببینم وضعیت قطعی نت چی میشه
به شما هم توصیه می‌کنم اگر تموم شده و کارتون زیاد لنگ نیست، نخرید فعلا..</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4350" target="_blank">📅 00:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4349">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یکی گروک مدل grok 4.5 رو داده بیرون، یکی هم متا مدل جدید داده بیرون به اسم Muse Spark 1.1 هر دو هم ادعا کردن که هم سطح Opus 4.8 هستن با هزینه کمتر، ولی به نظرم متا دروغ میگه
😂</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4349" target="_blank">📅 23:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4348">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A1vPCeFKDAcn8UEXWA1YORarJC6bHEyIQLZQi3-fZzxtDvWTG5ogdQw6BDYPTqk0ADzg_lnbVcbiiqTSCDDkvnbsciIoD0OzbJnI8eoZHYs9UEIHGwJddd_jbBOqQWfxiaEOjzmk9iuwQTbbWVhsxVHgc9D20Ifdu26W1qd5hTzLfrIZ22UY20xJznrp8nLQnUmDVL2ogbc9mQXRN58nF1mrXlXuNtAKZjl-WvKO3Pj1F489m-L2pPctnVjrPbwVVqDPetrs0t8-IXZEPHS_Z18ZyuWQsbu6l8mBbSRmJlxOfqYOC4gvL2wZgyPwMxg0U3Ks9zyRUPnY8jbPkvy0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر درست باشه فوق‌العادست
بچه‌های توییتر تست کردن Grok چهار و نیم رو، همه تعریف تمجید کردن</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4348" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4347">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یکی گروک مدل grok 4.5 رو داده بیرون،
یکی هم متا مدل جدید داده بیرون به اسم Muse Spark 1.1
هر دو هم ادعا کردن که هم سطح Opus 4.8 هستن با هزینه کمتر، ولی به نظرم متا دروغ میگه
😂</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4347" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4346">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اتهام جاسوسی به Claude Code؛ چین درباره ابزار برنامه‌نویسی آنتروپیک هشدار داد</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4346" target="_blank">📅 21:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4345">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه کاری کردن انگار شرطی شدیم
تا نتمونو قطع نکنن باور نمی‌کنیم جنگ شده</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4345" target="_blank">📅 21:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4344">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ObVSH37nBuPLHO9gi0RM_UFC57Iunk_u4fTphuZ47WhzTx8UDlMRJRAnkh6SE3ejaFwDnJwLgywtPUfv5LcT3hrpZhwJV5ztITx_KmgVTt3K_SmK9x7EcC1E2A-0Vtl0__bzYIeRy1zDT9yuxdvKkD_GA6YkgRj8G8rQ2bPBKrqbyWcHfPNDMOlOBURsXcW-87g2Gp852rbY58L0Qr0fj23tvltBWXPuVO8n-8HtAKQv7jtxVwYxORr5iwH-B-2GJVN364jGxi03bmyYyAtZFbHSytyRlVVYf4_brXVncdwBHZXXjVV3kD_FUlBpBhWtvnebyZJNKPCYcuNRptZ7tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
دستیار هوشمند کانال WhiteDNS
👉
@WhiteDnsChatBot
✅
جواب سریع |
✅
۲۴ ساعته |
✅
رایگان
نحوه استفاده:
۱. روی لینک بزنید
۲. Start
۳. سوالتان را بنویسید
مثال: چطور فیلترشکن نصب کنم؟
/search عبارت — جستجوی مستقیم
/contact — ارتباط با ادمین
⚠️
ربات WhiteDNS در چه زمینه‌هایی جواب می‌دهد:
✅
فیلترشکن و VPN
✅
DNS و تنظیمات اینترنت
✅
آموزش نصب اپلیکیشن‌های WhiteDNS
✅
رفع مشکلات اتصال
✅
Warp و Cloudflare
✅
تنظیمات اندروید، آیفون، ویندوز، مک
✅
سوالات مربوط به قطعی اینترنت
❌
ربات قادر به پاسخ‌گویی به سوالات غیرمرتبط با موضوعات کانال نیست.
💡
نکته: اگر جواب دقیق نگرفتید، سوالتان را طور دیگری بنویسید یا از دکمه جستجو استفاده کنید.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/4344" target="_blank">📅 20:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4343">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">ترجیحا هیچ VPNای نخرید دوستان. هیچ تضمینی نیست که اگر اینترنت قطع بشه هم اونا وصل بمونن یا نه. مثل اوایل جنگ که خیلیا اسکم شدن
همون هزینه رو بذارید whitedns راه بندازید</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4343" target="_blank">📅 16:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4342">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1d99494e2.mp4?token=JjCJs6Xs8IlBPzfGH1uWlDAgbcGZlokFgiS6mu4r0z4kqbpFYbImJt-lX3dzCq6w3MJC2gq302HsyMXB_iDzjDx3UlR-euITQqnVr63QQzOEMIED72Pn-E24GxMsXF-SIXXyG492tV2SQcEo3SzKeC4V6s9kwgzUJRyRNlTqwnrtUqVxKVqIzU01r1VYVVHQ5BXYyOaSrMSJt345DDRvKEQ7mNDsPea0RgDwQrr2TsYW-LPA_IqojghC-SjUpWrJE1ez2Lt9SUlpot97HOwlYGWClOSAjANG3HadHA_qbtH1okSnqZt1IMcqgpRw-3V5OQVCrGZwpNwAmk6F0SVERg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1d99494e2.mp4?token=JjCJs6Xs8IlBPzfGH1uWlDAgbcGZlokFgiS6mu4r0z4kqbpFYbImJt-lX3dzCq6w3MJC2gq302HsyMXB_iDzjDx3UlR-euITQqnVr63QQzOEMIED72Pn-E24GxMsXF-SIXXyG492tV2SQcEo3SzKeC4V6s9kwgzUJRyRNlTqwnrtUqVxKVqIzU01r1VYVVHQ5BXYyOaSrMSJt345DDRvKEQ7mNDsPea0RgDwQrr2TsYW-LPA_IqojghC-SjUpWrJE1ez2Lt9SUlpot97HOwlYGWClOSAjANG3HadHA_qbtH1okSnqZt1IMcqgpRw-3V5OQVCrGZwpNwAmk6F0SVERg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مقدار زود شروع شد</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4342" target="_blank">📅 16:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4341">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/poquuoy_SvTSqG2U-m8W_OyR3YXPV32hgn0cOnmQgLHZr1k1Gh8OUh7-wWygWwCNwOFgvdw6LZ8ykWR-KygcVM5Z7o_glmfZAa9mFeHIsjV_S6zOgErS2I1FBaEv2mmrlLPG7pBAnUwqcghZfkNcbJlbRvDTScxgR_4g4SKlpa7CWMCt783RZ1FNl14p93RxbIoL6_YKF0t85ISGxJfkGLJykMPfYmzggKmg8bfbTrWR6Yk2h-gnBxl5z_gGqTWRA6yQFwKyO4sBbyQyv7x-yVcHIfqe2jIoxJ2LBSnVCbXk3dSmWSVf5OdNb6A734EGA8BfyDV7aVSwpEyPkidk9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارادوکس عجیبیه. از یه طرف انگار جدی جدی جنگ شده باز
از یه طرف اینور دارم آموزش می‌بینم و کار می‌کنم با ai
و نمیدونم همین آب باریکه‌ی نت کی قطع میشه دوباره</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4341" target="_blank">📅 15:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4340">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">احتمالاً من دچار "فرسودگی LLM" (LLM Burnout) شدم!
نویسنده‌ی این مقاله (الک سکولن) یه توسعه‌دهنده‌ست که می‌گه مصرفش از هوش مصنوعی در حد استانداردهای الان کاملا معمولیه، اما اخیراً یه حس خیلی عجیبی بهش دست داده:
خستگی مفرط از خوندن متن‌های تولید شده توسط هوش مصنوعی!
روند کارش این‌طوری شده که دیگه خودش از صفر کد نمی‌نویسه؛ طراحی می‌کنه، طراحیش رو به Claude یا Codex می‌ده، کدهای اونا رو می‌خونه و ریویو می‌کنه. علاوه بر این، روی پروژه‌ای کار می‌کنه که کدهای تولید شده توسط Qwen رو باید مداوم بررسی کنه. یعنی عملاً کل روزش با خوندن خروجی‌های AI می‌گذره. حتی برای سرچ‌های روزمره‌ش هم از ChatGPT و Gemini استفاده می‌کنه.
حالا مشکل کجاست؟
اعتراف می‌کنه که با این ابزارها خیلی بهره‌ورتر شده و قصد نداره کنارشون بذاره، اما تو چند ماه اخیر، یه بخش کوچیکی از وجودش از دیدن خروجیِ مدل‌ها وحشت داره! چرا؟ چون دقیقاً می‌دونه قراره چی ببینه:
فرضیات غلط، توهمات (Hallucinations)، جملات بریده‌بریده‌ی اغراق‌آمیز، و
✨
استفاده‌ی بیش‌از‌حد از ایموجی‌ها
🚀
.
نکته‌ی جالب اینجاست که می‌گه انسان‌ها هم اشتباه می‌کنن و می‌تونن رو اعصاب باشن، اما مشکلِ اصلی با هوش مصنوعی
تکراری بودنشه
. مدل‌های زبانی دقیقاً با یک لحنِ واحد می‌نویسن و دقیقاً یک‌جور اشتباه می‌کنن. سر و کله زدن با یک سبکِ کاملا یکسان و اشتباهات تکراری، اونم به صورت هر روزه، کلا فرسوده‌ش کرده.
این دقیقاً نشون می‌ده که با وجود تمام شخصی‌سازی‌ها (Personalization) و پرامپت‌ها، هنوز هم اون امضای پنهان و سبک خاصِ هوش مصنوعی از زیر دستمون در میره و وقتی تو طولانی‌مدت باهاش درگیر بشید، می‌تونه حسابی روی مختون بره!
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4340" target="_blank">📅 14:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4338">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vnOfXfpyt2hQmRa62UeN_6b4AmD2D1hB648ve1n8qixjbU0Latx0GHuOqc8A5EyWguqvZ5IsIAZmdQIPrF91TbP3vKft3vWIXWDUtTMdHxn1c3NcmRN81cBAz0HhRmPLjnzJdJCtj0TXvMm1HaTkJ0hafAcHZ7pQ_aDxajEOm_tvcIcrRyJGuuaeLmNceQfQ-gwFFJT5t8H46htKj4l11XLNQRP0h9Ev7heVdbvKirxONgZMu1fjaVn2wNrD_bGdRwHCqDmFsnH3KjKmGP-yTWZF340g2vb7kNMGHbdNNOvYuK9rwSN89h_9wnDnQ5jvImttRdCkFu24YDuCM9GbEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SOoHO_wtBxg99VfBCREQwxyFoYwqcLAbiOV0kY5nqKrbmIRgXCd5SmT1GSYBpr-iHtcIOW_NbA1gKi9iSyeSU0Ga-FtJehfiG-zuSD3Eg_1_vXu4ldWylxGYCbKAK89GONEmddVNhUrXTv-2xhv5vvfngcVI8QAsfjkpWIZ10JC8IYsNOfesBZ_0n6s4kUHUce9R1tJVzdUigTAxqEtsoFp4bnJGK6prGs6vW38KsJF8v1gmdN94vqr7QHgWkJHzRukqTZJ7lUM85dsjw3zWAsWnywX5DIteYoiQcr1uGqsqn93RoglnL5rvwjt2S4ELHMkFtYx-JEp30F_2_nRyvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
100 میلیون توکن رایگان برای تست مدل‌های جدید AI  مدل‌های زیر را می‌توانید با OpenAI Compatible API استفاده کنید:  • Kimi K2.6 • MiniMax M2.7 • GLM 5.2 FP8  بدون ثبت‌نام، وارد صفحه زیر شوید و از بخش Your API Key کلید خودتان را دریافت کنید:  https://infer…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4338" target="_blank">📅 13:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4337">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/784bc3dcd7.mp4?token=Dh1pajTSTqCWZMppdvzqmhQAHMIwGZMuieSIk7Lv8nph1076P2YFmB65Kt8GAUtos0h_09pXXms1w-BIlas1QtJ_EF6SjP1zJz246Vf2u9tWnFpi6B3iiTL_XyrUn7ibwuAyywnvP2Ks0Pe3_eHzNqdlQ9_jrpWzlw9ICf_PQoLB7nXGMLucRAbN6HGY0TOftCfKVeZXiNgWlNpCQwFmQTfI09LsEeVtpPJrLD2BxDJDz0p5jUg4gOc6FN77O2HClqmz1UzkqYj_kWwRyb0UCT2nSMrllBc9QsY6_zWDTBx-LG9r9yArMuLXkeAFSQbSUaaKQwNWCQ3bEyIh0eovfiJcvCiKRTo4j6Dbg304o0uiYUx4B6tQNN-a7jVYt2f-iHz2IUt0r2iOicFQgo2qtVoXV-Cf24p0eL3ye5ep0AryFjdzrd0p3-p18YkKw2waJjC2efH7tzHSpXRo5K6QC6BkERRVDsWPazG9Mku_j5irncvHZXq1mkoU9sNMN7BKaf2tIWmd8opmIOVxbh4i9L3L3g54G6XmTtn1A5uUS58cnd2W2pGjudK28aVQRC_IEdBW3Hl5vJMnb_Tmqi9sZcQrNqKaFMywVf6qDV9KaSozwXoNS9OF3DVYS88_bzej0rsn-aEWYk8I5bFCwtERXINJnhPf9HQmqK1rZjzZ0ok" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/784bc3dcd7.mp4?token=Dh1pajTSTqCWZMppdvzqmhQAHMIwGZMuieSIk7Lv8nph1076P2YFmB65Kt8GAUtos0h_09pXXms1w-BIlas1QtJ_EF6SjP1zJz246Vf2u9tWnFpi6B3iiTL_XyrUn7ibwuAyywnvP2Ks0Pe3_eHzNqdlQ9_jrpWzlw9ICf_PQoLB7nXGMLucRAbN6HGY0TOftCfKVeZXiNgWlNpCQwFmQTfI09LsEeVtpPJrLD2BxDJDz0p5jUg4gOc6FN77O2HClqmz1UzkqYj_kWwRyb0UCT2nSMrllBc9QsY6_zWDTBx-LG9r9yArMuLXkeAFSQbSUaaKQwNWCQ3bEyIh0eovfiJcvCiKRTo4j6Dbg304o0uiYUx4B6tQNN-a7jVYt2f-iHz2IUt0r2iOicFQgo2qtVoXV-Cf24p0eL3ye5ep0AryFjdzrd0p3-p18YkKw2waJjC2efH7tzHSpXRo5K6QC6BkERRVDsWPazG9Mku_j5irncvHZXq1mkoU9sNMN7BKaf2tIWmd8opmIOVxbh4i9L3L3g54G6XmTtn1A5uUS58cnd2W2pGjudK28aVQRC_IEdBW3Hl5vJMnb_Tmqi9sZcQrNqKaFMywVf6qDV9KaSozwXoNS9OF3DVYS88_bzej0rsn-aEWYk8I5bFCwtERXINJnhPf9HQmqK1rZjzZ0ok" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های جالب Amir Hormati مهندس ارشد و پرینسیپال در گوگل در حوزه AI در مورد کدنویسی و Hard Skill ها، اینکه آینده از دید خودش چیه، چه اتفاقی بر سر کدنویسی میاد و به عنوان مهندس نرم افزار روی چه مسائلی تمرکز کنیم، جالب اینکه خود امیر از رول مدیریت به نرم افزار برگشته به خاطر همین!
✍️
Max Shahdoost</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4337" target="_blank">📅 13:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4336">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رفقا مجددا می‌گم، که کلا این سایت‌هایی که یهو کلی توکن رایگان میدن، امن به نظر نمی‌رسن مراقب پروژه و .env هاتون باشید</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4336" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4335">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رفقا مجددا می‌گم، که کلا این سایت‌هایی که یهو کلی توکن رایگان میدن، امن به نظر نمی‌رسن
مراقب پروژه و .env هاتون باشید</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4335" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4334">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه وایب کدینگ ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SD2hjnIFEqdbyu7nco2JCAPAk6BZJxCwiBdwh0uPYfPtXKt1d3JBqEatdnDCEVz9XQbVlpAsl5H2GamB4X7PQhYqtn6HdM34CYlEMY9YJ6e5xs75wAdy1ano5GxTeqSmnRuumnDnTutwq2CM_ZJ_BoLKcgHFCDHkg2FzWDcT01cc8hpF7Rfo-3cwpbzblOwgJURP_3ROFbsuPWIFbeg3rlR99xyVuXouyNOgKZtW8LJv0WB445UBNF9Rp2Ry5AkS2isid4Ea5FXPrhshkd7Dch0PU13OD8Meg0XK0J78sFZlR9m97gb_r9TBU3BVIvo-VWVynOtoTm4j_qggyw7g8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
100 میلیون توکن رایگان برای تست مدل‌های جدید AI
مدل‌های زیر را می‌توانید با OpenAI Compatible API استفاده کنید:
• Kimi K2.6
• MiniMax M2.7
• GLM 5.2 FP8
بدون ثبت‌نام، وارد صفحه زیر شوید و از بخش Your API Key کلید خودتان را دریافت کنید:
https://inference.dahl.global/chatKeys
💡
اگر کوکی مرورگر را پاک کنید، می‌توانید دوباره یک API Key جدید بگیرید.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4334" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4333">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NqVqiieqsCcQVVoit3ynPbe2lTKzRD7I6zDe7I2ibCtfUeriS-c69K1KM1qMsdvJLWvxeAkfW7aqesJDfZ_4NGNO2jbqV6iZkJbv5FeX9XXcFWp-e-OnCbA7K644itK9_hUHt-NOp1Wlz_Vs0-M5-tvuaGYZFCtlQjoD3t6aNyejd1MfnV0HyHrL_V4gP0ZDL8TRe91JrAG-y8ggnSOmA1gttyWrgdmYY51kDeqR0buUalIewkWzcta320z0asnFx6M_ekQEH1SbvvQdUjGJ-Op2WrjuhRARWBhf_m-S0Yd-GWH0AsNHX1gWUr9pz6BOun0KFxZBLkpxyyxLg2Yq8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزی نیست، کامیونیتی Rust هستن
😂
😂
زبان Rust برخلاف go و پایتون و... از Garbage collector برخوردار نیست.
نفر اول گفته انقدر سینتکس افتضاحه که دلم می‌خواد زبان rust رو بندازم توی آشغالا(garbage) و نفر دوم ریپلای زده که اگه بندازیش توی آشغالا کسی نیست جمعش کنه چون این زبان آشغال جمع‌کن(garbage collector) نداره</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4333" target="_blank">📅 12:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4332">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اگر می‌خواید اکانت Claude بخرید، بهتره بدونید علت بن کردن‌های کلاد distillation attack هایی هست که اخیرا بهش شده؛ و حتی کاربرهای خارجی هم یهو اکانتاشون بن شده. بهتون دوتا توصیه می‌کنم.
1- به هیچ وجه از سایت‌های ایرانی نخرید. و حتما بدید دوستی، آشنایی، چیزی بگیره از خارج کشور. اگر ندارید، برید سراغ توصیه‌ی دوم. احتمال بن شدن داره به هر حال و ریسکش پای خودتونه. من خودم به شخصه هنوز بن نشدم(نمیدونم شانسه، یا چون دوستم از خارج از کشور واسم گرفت)
2- اشتراک Codex بگیرید در عوض و یا نهایتا اگر کار خیلی واجب دارید و می‌خواید حتما کلاد باشه، cursor بگیرید اما کرسر خیلی زود تموم میشه طبق تجربه‌ی شخصی. به نظرم Codex سخاوتمندانه‌تره به شدت. و صبر کنید تا وقتی که بن شدناشون شدتش کمتر بشه.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4332" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4331">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نشت مخفیانه‌ی دیتا از ریپازیتوری‌های پرایوت گیت‌هاب با یه ترفند ساده‌ی هوش مصنوعی
📚
فکر کنید یه نفر بدون هیچ پسورد و دسترسی‌ای، بتونه کدهای مخفیانه‌تون رو توی گیت‌هاب بخونه. چطوری؟ با گول زدن ایجنت هوش مصنوعیِ خود گیت‌هاب!
تیم Noma Labs یه آسیب‌پذیری خیلی خطرناک (به اسم GitLost) توی سیستم جدید Agentic Workflows گیت‌هاب پیدا کرده. داستان از این قراره که این ایجنت‌ها می‌تونن issueها رو بخونن و اتوماسیون انجام بدن.
🫵
حالا هکرها چیکار می‌تونن بکنن؟
هکر کافیه بیاد تو یکی از ریپازیتوری‌های پابلیک شما یه Issue باز کنه و توش یه سری دستور مخفیانه به زبان انگلیسی (Prompt Injection) قایم کنه.
ایجنت گیت‌هاب این متن رو می‌خونه، گول می‌خوره و به جای کار اصلیش، میره فایل‌ها و دیتای ریپازیتوری‌های پرایوتِ همون سازمان رو می‌خونه و برای هکر می‌فرسته!
نکته‌ی جالب اینجاست:
گیت‌هاب کلی گاردریل امنیتی چیده بود که دقیقاً جلوی همین اتفاق رو بگیره. اما محقق‌ها فهمیدن فقط با اضافه کردن کلمه‌ی "Additionally" (به‌علاوه/همچنین) توی پرامپت هک، مدل هوش مصنوعی کلا گیج می‌شه و به جای اینکه درخواست رو رد کنه، تمام محدودیت‌ها رو دور می‌زنه و دیتا رو لو میده.
این دقیقاً نشون میده که توی سیستم‌های جدید هوش مصنوعی، همون متنی که ایجنت می‌خونه همزمان می‌تونه پاشنه آشیل و نقطه حمله باشه. حملات Prompt Injection الان دقیقاً دارن همون بلایی رو سر AI میارن که قبلاً SQL Injection سر وب‌سایت‌ها میاورد.
البته این باگ به طور مسئولانه به گیت‌هاب گزارش شده، ولی حواستون به ایجنت‌هایی که به سورس‌کدهاتون دسترسی دارن باشه!
منبع:
https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4331" target="_blank">📅 19:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4330">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یکی از چیزایی که راجب کامیونیتی فارسی باحاله و دوست دارم، اینه که زیاد توی کامنت‌ها با هم در ارتباطیم. کامیونیتی خارجی، این شکلیه که ویدئوی تکنیکال می‌ذارن، 60 کا ویو میخوره اما کلا 25 تا کامنت میگیره. یوتوبره اون 25 تا کامنت رو حتی لایک هم نمیکنه. اما کامیونیتی فارسی، ویدئوی 10 کایی کم کمش 200 تا کامنت رو میگیره و خیلی از یوتوبرا هم جواب میدن و اهمیت میدن</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4330" target="_blank">📅 16:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4329">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">☠️
ساخت رادار پیامکی با Hermes Agent بدون کدنویسی + API رایگان OpenCode
⚡️
دستورات نصب OpenCode برای ویندوز، سرور لینوکس و دیگر سیستم‌عامل‌ها: https://t.me/MatinSenPaii/4259
⭐️
توی این ویدئو: 1- باهاتون راجب کسب درآمد از Hermes صحبت می‌کنم 2- با همدیگه…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4329" target="_blank">📅 16:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4328">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P8cX9lsN3-axBiwmy34BKEU_drUkLFpzeQMSuL79_IkRXlnmcLFUCVD6v9ZvWOwkLRRMkW4MKcnw2KjJuONbEibu6NI-ouCsUeUbeiP5-9TKArJK_OXgMTyYHaj-EmdnIclYiU4La1kMtbfi1nkvnjmlJo6NO2mwA1ybGRzvzHhufCAwdy3mthQVY7tvmnW1k8v-f2Nk4K43Sd2IYpFH8QrPRk6MFWPNXpLHpvdtJbivLEKN_0ZybYAUfEVvBKQ5fPnY2z-vVLITYtTfKDRfMcakbyy3LS-ghwSxGF4Vq2pkbRagrvJYjLkdVbvqjUBTEit8HeXXyj7JbRelQiOlnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت رادار پیامکی با Hermes Agent بدون کدنویسی + API رایگان OpenCode
⚡️
دستورات نصب OpenCode برای ویندوز، سرور لینوکس و دیگر سیستم‌عامل‌ها:
https://t.me/MatinSenPaii/4259
⭐️
توی این ویدئو:
1- باهاتون راجب کسب درآمد از Hermes صحبت می‌کنم
2- با همدیگه OpenCode رو به 9Router وصل میکنیم و روش دور زدن یه باگ خیلی رو اعصاب رو بهتون میگم
3- از هرمس استفاده میکنیم که با سامانه پیامکی، یه کرون جاب بنویسیم(قابل پیاده‌سازی برای هر ایده‌ای)
4- و کار با پنل‌های پیامکی رو بهتون یاد میدم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api رایگان هم استفاده شده توی کل ویدئو
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4328" target="_blank">📅 15:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4327">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Zombie</div>
  <div class="tg-doc-extra">Bad Wolves</div>
</div>
<a href="https://t.me/MatinSenPaii/4327" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4327" target="_blank">📅 15:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4326">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خب انگار فعلا خبری نیست
نت منم اوکی شدش</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4326" target="_blank">📅 13:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4325">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4325" target="_blank">📅 12:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4324">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a627c5c6e.mp4?token=fb6QHTODTVAlpa0Y5XXQWF9rg_oEISxbITdrkzfhRFYbQeWAq_ew6-ySpFEQJt_MWVMncREYwzOwzMzW0pNCvJrAd0RDfc25Vf-2K821Kzg3cEBT3buJkp7qA0E9WnWgMzY9L7apkMm_mP9Fyef-NRSKk4zkVWAl3873TbxWWUaTk57E_BBxQ1usluct7Ii4kSLnM2Ho--wX8S1VyuBLQYR0fh6-rt8SlsTVNAaTJEe406wJwKWNUZSYWxxQru6TqALGdn6k-VgoiQ7RJ3U1rOGgDMJFpGeeTDJ7FP03drs5f7-Dz6HhSoynopzFFyDJSkO2j72DDsMYUAKr-BzENQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a627c5c6e.mp4?token=fb6QHTODTVAlpa0Y5XXQWF9rg_oEISxbITdrkzfhRFYbQeWAq_ew6-ySpFEQJt_MWVMncREYwzOwzMzW0pNCvJrAd0RDfc25Vf-2K821Kzg3cEBT3buJkp7qA0E9WnWgMzY9L7apkMm_mP9Fyef-NRSKk4zkVWAl3873TbxWWUaTk57E_BBxQ1usluct7Ii4kSLnM2Ho--wX8S1VyuBLQYR0fh6-rt8SlsTVNAaTJEe406wJwKWNUZSYWxxQru6TqALGdn6k-VgoiQ7RJ3U1rOGgDMJFpGeeTDJ7FP03drs5f7-Dz6HhSoynopzFFyDJSkO2j72DDsMYUAKr-BzENQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">The Return of
قدرت مذاکره</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4324" target="_blank">📅 12:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4323">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4323" target="_blank">📅 12:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4322">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مشکلی در وجودشان وجود دارد. آنها دیوانه هستند.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4322" target="_blank">📅 12:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4321">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">روی اینترنتای خود من به شدت اختلال هست
همراه اول که به زور چیزی باز میکنه
ایرانسل 4g+ اما هیچی به هیچی. آپلود 0
فیبر مخابرات هم از صبح 2 دقیقه وصله 20 دقیقه قطعه</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4321" target="_blank">📅 11:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4320">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نسخه‌های اندروید(اگر نمیدونید کدومه برای پردازندتون، Universal رو دانلود کنید)</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4320" target="_blank">📅 11:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4319">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge  https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4319" target="_blank">📅 11:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4318">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge
https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4318" target="_blank">📅 11:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4312">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4312" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4312" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4311">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آخرین نسخه‌های مک-ویندوز-لینوکس</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/4311" target="_blank">📅 11:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4303">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-macos-amd64.zip</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4303" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
نسخه لینوکس</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4303" target="_blank">📅 11:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4302">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dXhB5575hXje31ZETn7JpbwPviNz5eC1YIUKfRuyRp2Ft4xFx3MBLMQ9fEgCDibmmeWM92G91xK011TnQa9u_F5JzyeK60Ej2hz7BWu2ZFqJ9GjZat3XlrriJJS54uW_qWc6di7i60i8cnAoaboOnubMBijM56rN95z-Xo94PIWjJ9ABZd_j8W25GTFUACku24BukSVHotu6l0_EcxCx8TEKTd6AZ9qmysJFjVG4khgoS68uFrAhd69Fo_mActcH8DXKgmVlBr5TgEal_oXnM8k2QtkJvBnCI1Fs33Ve2Wjl4u9jZvazcdhA7t5ghRrSo7rOycnicWVdmG3wmCh--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق معمول، پیشنهاد میکنم WhiteDNS رو راه‌اندازی کنید برای خودتون و دوستانتون
آموزش:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4302" target="_blank">📅 11:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4301">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اعصاب و روان نموند برامون. نمیدونیم درس بخونیم، کار کنیم، کارگری کنیم، لپ تاپو بفروشیم و دلال بشیم که بتونیم زندگی کنیم، چیکار کنیم</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4301" target="_blank">📅 11:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4300">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">میترسم پنج دقیقه بخوابم ببینم نت قطع شده باز</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4300" target="_blank">📅 11:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4297">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OR5PJIZP55m7IgbJTIOgLpLLL_Pa48qWBfUYMZmtIpLbMYrGrIJT8U0LpId5FH5cUmiJPZ7d1MDr0dFT1jc7beIgNra_VtjPt15U2B03WVX7aeD0dvgVJ5qYkihyw2kAPq7zpgCp2IsPhf4pA4xpynWu4A3aJQNbfRURgpfHynCsMAdrRvUHUsFkyV9sakQVEs47-d0Td_LRHibB-cDRXVS1Abo4oued7xErAwX4HGfcYUxlgTkaa8rQsMZoWJobA3Q7TofEzsGj1VPIL74DnuRlUWHLbIX9EcxaJ1uTQ_tRVP7Ssp_zaDLGXw2uNzjQ5b_UdWyJCMEowa-VHWW1BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZPQRvmrH7EIjsr0p3JOWzJbHN-CgEYFHNqc00Sm1u_CSlS_0QEstMZcr4VHtI69-FfgO5-kU5qtrFOxItV9kXlwhMczofy6DWLJAl_Gbhf7EpBzZYot4VEx9T9hME3rQxqDsylRalG0xG8fbvj4UtZdX-31gTPp9As18M3Lsg33DCNFhmzsEHYNDhl-_gQPbufuBABtCTou9SOIwdnngPqSenlYmkMue7ajbr1vQOrrWfxuQ37WbYGlMWmTseWw1onye-NoTKp11mo1GZYyNRv7ityestWGM6zdT6TvgRoH8jC661VEGUB_No9XYWDOTp-bi73UhIV89GNJHkwsiRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X2Igd-WSdwVIL-RQpOMQqkgDl-lmJ72XSajzrY_J7iMUd4FAUjSRd9sNnd6Mkb2NWO_mPocb3orzScJV3BcARClWh1wv4vGBx7Y5E3AERQxZVw8JT-zvDbAdyorjnQqAGAFAbDdKz4YMYC8rOWXMvY3OjFvLJo7kxbsZmyI4N70V3xoHv-n2sof1vLzkEtoK9M5cFcKZhnUsuOzhhz0_qlj6IuQCPmsLoqfCjQ3WN6oQMaxHyjNrtAWxa3BCy51alBELwJaP5xqTwDHEhx9MauOjs-Q4p4ribdvQD2PydIV1PhrIrbYMpdnULu6EOrOKshFSfoHOtAb1bcXkzpfFyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی هزینه‌ی هوش مصنوعی از حقوق مهندس هم بیشتر می‌شه
خلاصه:
شرکت «آنتروپیک» (Anthropic) حدود ۲.۳ برابرِ پولی که بابت حقوق و دستمزد می‌ده، خرج زیرساخت و پردازش (Compute) می‌کنه! یعنی با حساب حقوق سالانه ۲۲۴ هزار دلاری (با احتساب تمام مزایا)، سالی ۵۱۵ هزار دلار به ازای هر مهندس خرج پردازش می‌کنه. در حالی که ۱ درصد از برترین شرکت‌های نرم‌افزاری فقط ۸۹ هزار دلار و شرکت‌های میانه بازار (میانه آماری)، کلاً ۱۳۷ دلار خرج می‌کنن. حالا ۳ تا سناریو برای سال ۲۰۲۹ داریم که نشون می‌ده این شکاف عمیق چطوری ممکنه پر بشه.
همونطور که اشاره شد، آنتروپیک ۲.۳ برابر حقوق پرسنلش، در حال حاضر داره خرج زیرساخت و پردازش می‌کنه. با حدود ۵,۰۰۰ تا کارمند و تقریباً ۱۰ میلیارد دلار هزینه‌ای که توی سال ۲۰۲۶ برای آموزش مدل و استنتاج (Inference) می‌کنه، سهم هر کارمند سالی حدود
۲ میلیون دلار
هزینه پردازشی می‌شه؛ اونم در مقابل حقوق و مزایای کلانی که برای هر نفر احتمالاً بالای ۵۰۰ هزار دلاره!
بقیه بازار نرم‌افزار خیلی از این رقم‌ها عقب‌ترن. ۱ درصد از برترین شرکت‌ها سالی ۸۹ هزار دلار به ازای هر مهندس روی هوش مصنوعی خرج می‌کنن؛ یعنی ۴۰ درصد از یک حقوق ۲۲۴ هزار دلاری برای یک مهندس ارشد. این رقم برای شرکت‌های میانه بازار فقط ۱۳۷ دلاره! اختلاف فاحش اینجاست:
۲.۳ برابر حقوق
در لبه‌ی تکنولوژی
۰.۴ برابر حقوق
در صدر بازار
نزدیک به صفر
برای شرکت‌های معمولی بازار
حالا بقیه‌ی بازار چقدر می‌تونن خودشون رو به این سطح برسونن؟ جواب این سوال توی ۳ تا سناریو خلاصه می‌شه.
(توضیح نمودار خطی(عکس سوم): نمایش سه سناریو برای هزینه‌های هوش مصنوعی به عنوان درصدی از حقوق مهندسان تا سال ۲۰۲۹؛ در سناریوی خوش‌بینانه، این رقم به رکورد ۲۳۰ درصدی آنتروپیک می‌رسه)
سناریوی بدبینانه (کاهش قیمت توکن‌ها برنده می‌شه)، سناریوی پایه (رشد ۱ درصد برتر بازار کند می‌شه)، سناریوی خوش‌بینانه (بقیه بازار تا سال ۲۰۲۹ به نسبتِ هزینه آنتروپیک می‌رسن). هر کدوم از این سناریوها، هزینه سالانه هوش مصنوعی به ازای هر مهندس رو نشون می‌دن(عکس دوم)
توی سناریوی خوش‌بینانه، فقط هزینه هوش مصنوعی به ازای هر مهندس، با کل درآمدی که یه کارمند توی شرکت‌های معمولی SaaS تولید می‌کنه برابری می‌کنه! همین الانش هم شرکت‌های آنتروپیک و اوپن‌ای‌آی به ترتیب ۱۴ میلیون دلار و ۶.۵ میلیون دلار به ازای هر کارمند درآمد دارن، که بالاترین رقم توی لیست ۲۰۰۰ شرکت برتر فوربز (Forbes Global 2000) به حساب میاد.
ساختار هزینه‌ها، دقیقاً جا پای ساختار درآمدها می‌ذاره.
موتورهای محرک توی سناریوی خوش‌بینانه:
قیمت مدل‌های پیشرفته ثابت می‌مونه، چون هزینه‌های آموزش به ثبات می‌رسه و تقاضا از عرضه جلو می‌زنه. فرآیندهای کاری مبتنی بر ایجنت (Agentic Workflows) نسبت به چت‌های معمولی، چند سر و گردن توکن بیشتری مصرف می‌کنن؛ طوری که «گلدمن ساکس» پیش‌بینی می‌کنه مصرف توکن تا سال ۲۰۳۰ حدود ۲۴ برابر بشه. تازه، اگه شرکت رقیب قابلیت‌های جدید رو سریع‌تر عرضه کنه، دیگه پرداخت صورت‌حساب هوش مصنوعی یه انتخاب نیست، بلکه یه اجبار حیاتیه.
ترمزها در سناریوی بدبینانه
: قیمت توکن‌ها توی سه سال گذشته، هر سال ۱۰ برابر کاهش پیدا کرده. مدل‌های متن‌باز (Open-weight) دارن با کسری از هزینه‌ها، شکاف کیفی رو پر می‌کنن. از طرفی شرکت‌هایی که مصرف هوش مصنوعی رو بر اساس نقش یا حجم کاری کارمندان سهمیه‌بندی می‌کنن، می‌تونن شیب این نمودار هزینه رو خم کنن و کاهش بدن.
نظر شخصی: اصلا نمیشه پیش‌بینی کرد:) با اومدن ایجنت‌ها، سناریوی توکن داره مطرح میشه. از اون طرف، چین غوغا کرده و با رایگان عرضه کردن مدل‌هایی مثل MIMO و GLM-5.2، واقعا نمی‌تونم نظر بدم.
منبع مقاله:
https://tomtunguz.com/ai-spend-breakeven-2029/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4297" target="_blank">📅 00:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4296">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یه مقاله از نیویورک تایمز(با اینکه ازشون خوشم نمیاد) دیدم که توی هکرنیوز بحث‌برانگیز شده. داستان در مورد اینه که با پیشرفت سریع مدل‌های زبانی، مهارت‌های کسایی که فلسفه خوندن، چطور توی بحث‌های اخلاقی هوش مصنوعی و Alignment مدل‌ها داره به شدت کاربردی می‌شه. و انگار یه بازار کار جدید داره برای این رشته شکل می‌گیره =)
لینک مقاله:
https://www.nytimes.com/2026/07/05/business/philosophy-majors-ai-jobs.html
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4296" target="_blank">📅 23:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4295">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اگر میمو روی اوپن کد بهتون ارور ۴۲۹ داد که به لیمیت رایگان رسیدید، نترسید. یه continue بگید دوباره میره ادامه:)</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4295" target="_blank">📅 21:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4294">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اگر میمو روی اوپن کد بهتون ارور ۴۲۹ داد که به لیمیت رایگان رسیدید، نترسید. یه continue بگید دوباره میره ادامه:)</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4294" target="_blank">📅 20:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4293">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Js6Kbe3-_UI2Fpe7T9QDSmLsEDeRLKYL2ATCw0WTlcXrSa6WPSLSzA-pC9iVWkUBvyvJAZDFy6a3OYZXfvqDFRS3pB114BAZhG7PAXOuJsLnJt8-Q3tL0f897EbuIjlCpJUgf7K2JxqNrFcwQ7ayLMGuUhh5eE0sD0RLVEaqniDxsjnoCfhzfpjsDzPP8o0WlkkEBc7uGFfPZj3A4rvksKaFi-X0n7mqwkSCqnTIZSW_1-p4R9LOdE2qzB8hQHwdacDVu9IqMzbe8oMBzzK1lA7J5vT_pVVZcl9MSUrc219Z8F4VqXT7IEVGGSt8_d-HYB33yEqTT1wRYH9KRQvgdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زبان برنامه‌نویسی Cyrus(کوروش) چیست؟
سایروس یک زبان برنامه‌نویسی متن‌باز و جدید است که برای ساخت نرم‌افزارهای زیرساختی و سیستمی طراحی شده؛ یعنی همون نوع نرم‌افزارهایی که نزدیک به سخت‌افزار کار می‌کنن و به سرعت و کنترل دقیق نیاز دارن (مثل سیستم‌عامل، درایور، یا ابزارهای زیرساختی).
فلسفه اصلی سایروس این است: هیچ اتفاقی پشت پرده و بدون اطلاع برنامه‌نویس نیفتد. یعنی کد باید همیشه روشن و قابل پیش‌بینی باشد و برنامه‌نویس دقیقاً بداند هر خط کد چه کاری انجام می‌دهد، بدون رفتارهای پنهان یا پیچیدگی‌های اضافه.
چند ویژگی مهم سایروس:
بدون گاربیج کالکتور
: بر خلاف خیلی از زبان‌های مدرن (مثل پایتون یا جاوا) که حافظه رو خودکار مدیریت می‌کنن، سایروس این کار رو به خود برنامه‌نویس می‌سپارد. این یعنی کنترل کامل و دقیق‌تر روی مصرف حافظه، که برای نرم‌افزارهای سریع و حساس خیلی مهمه.
کامپایل مستقیم به کد ماشین
: سایروس از فناوری معروف و قدرتمند LLVM استفاده می‌کند تا کد رو قبل از اجرا به‌طور کامل به زبان ماشین تبدیل کند؛ نتیجه‌اش برنامه‌ای سریع و بدون واسطه است.
سازگاری استاندارد با سیستم‌عامل‌ها
: طوری طراحی شده که به‌راحتی با نحوه‌ی کار سیستم‌عامل‌های رایج هماهنگ باشد.
سینتکس ساده و مینیمال
: تلاش شده که نوشتن و خواندن کد تا حد امکان ساده و بدون ابهام باشد.
قابلیت‌های پیشرفته بدون هزینه اضافه
: مثل ژنریک‌ها (نوشتن کد قابل استفاده مجدد برای انواع مختلف داده) و چندریختی (Polymorphism)، بدون این‌که سرعت اجرای برنامه رو کند کنند.
ساخت افزایشی (Incremental Build)
: یعنی موقع تغییر کد، فقط بخش‌های تغییر‌کرده دوباره کامپایل می‌شوند، نه کل پروژه؛ این باعث سریع‌تر شدن فرآیند توسعه می‌شود.
هدف کلی سایروس این است که زبانی باشد نزدیک به سخت‌افزار و ماشین، اما بدون این‌که خوانایی و سادگی کد قربانی شود.
این پروژه هنوز در حال توسعه است و به‌تازگی نسخه بتا (Beta) آن منتشر شده. اگر دوست دارید بیشتر بدانید، امتحانش کنید، یا در توسعه‌اش مشارکت کنید:
مستندات:
https://cyrus-lang.ir/en
گیت‌هاب:
https://github.com/cyrus-lang/Cyrus
کامیونیتی:
@cyrus_lang
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4293" target="_blank">📅 18:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4292">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آخرش یا atomic mail ایرانو بن میکنه یا ما atomic mail رو از کل جهان ابیوز میزنیم
😂
😂</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4292" target="_blank">📅 16:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4291">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دیروز و پریروز می‌خواستم ویدئو بذارم، اما با اینکه موضوعات زیادی دارم برای ویدئو ساختن، حس کردم که کمی عجولانه‌ست و تایم گذاشتم که هم خودم کمی بیشتر با ابزارها کار کنم، هم وقت داشته باشم برای مطالعه‌ی شخصی که محتوای باکیفیت‌تری ارائه بدم. برای همین تا وقتی حس نکنم کافیه، ویدئوی جدیدی منتشر نمی‌کنم
❤️</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4291" target="_blank">📅 16:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4290">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sXwCGuZjiVRrrOho9fK6TB0Wsv36LoEiifDJOszQndrxcKwQu8PAVVm_IuAmjn5UHTcw77AzNrCT5_CzIwvaM1c_YFn5xcj-3_ri0Ulw-dge-BHzB4h-Q0N5mKFmgenV8OUyNh2jlQn7zEWDHmvdhyLPhaJHcKrM1nmbfvPQMDioeDt6H75-cB3tnWS0ve2gffal-zTKRf4VV3URR221V44u0nwjxCdcGQUkeB60BXjJMd3_J2evoBcGxyjsY6s09hT2xWNvuFENno1p9MS6OZ5I3sQy7AOoz7x4aeOVhlrpm2hHLLmQNT3Y6_MMavVrhEQwApMlLRz91r-yOIMOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا هزاران پست سیو می‌کنیم ولی هیچ‌وقت نمی‌خونیمشون؟
🤔
اسم علمی این رفتار
Digital Hoarding
(ذخیره‌سازی وسواسی دیجیتال) یا "
پارادوکسِ بعدا می‌خونم
" هست.
این اصطلاح رو اولین بار
Van Bennekom و همکارانش توی سال ۲۰۱۵
و داخل یه مقاله توی مجله‌ی
BMJ Case Reports
مطرح کردن؛ اونجا یه مورد بالینی رو توصیف کردن که یه مرد ۴۷ ساله هر روز حدود ۱۰۰۰ عکس روی کامپیوترش ذخیره می‌کرده بدون این‌که هیچ‌وقت سراغشون بره.
از اون موقع، این پدیده به یه حوزه تحقیقاتی جدی تبدیل شده. تحقیقات جدیدتر (مثل مطالعه‌ای که سال ۲۰۲۳ توی مجله
Journal of Obsessive-Compulsive and Related Disorders
منتشر شد) نشون می‌ده Digital Hoarding با الگوهای شناختی و هیجانی شبیه به اختلال وسواسی-جبری (OCD) و وابستگی هیجانی به اشیاء مرتبطه؛ یعنی حذف‌کردن یه فایل یا پست، همون حس ناراحتی رو ایجاد می‌کنه که دور انداختن یه وسیله فیزیکی.
چرا این اتفاق می‌افته؟
👩
هر بار که پست مفیدی رو سیو می‌کنیم، مغز دوپامین آزاد می‌کنه؛ حس «پیشرفت» بدون این‌که واقعاً کاری انجام داده باشیم.
✈
ترکیبی از
FOMO
(ترس از دست دادن اطلاعات) باعث می‌شه به‌جای مصرف محتوا، فقط جمعش کنیم.
💤
نتیجه؟ انبار دیجیتالی از Save‌ها و بوکمارک‌ها که عملاً هیچ‌وقت سراغشون نمی‌ریم.
چندتا راهکار عملی:
قانون 5 دقیقه
: اگه محتوا کمتر از 5 دقیقه وقتتونو می‌گیره، همون لحظه بخونید؛ وگرنه رهاش کنید.
سقف هفتگی
: حداکثر ۵ تا ۱۰ آیتم توی یه هفته سیو کنید تا تلنبار نشن.
دسته‌بندی و پاک‌سازی دوره‌ای
: هر چند وقت یه‌بار Saved items رو مرور و پاک‌سازی کنید.
اگه واقعاً مهمه، به‌جای سیو کردن، همون لحظه یادداشت بردارید یا اجراش کنید.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4290" target="_blank">📅 16:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4289">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آخرش یا atomic mail ایرانو بن میکنه یا ما atomic mail رو از کل جهان ابیوز میزنیم
😂
😂</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/4289" target="_blank">📅 15:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4288">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FAVbFqWlaw-IoIUWgUevrdit1UpAxdEZ0IzrPNMHjq_vwbZ2w-Cl9ZCwm2KZKbc7hMRICAZnZ_LIv9tIMAllUQY427Q7cPVDBoDeIPVIOTBCaJITMz9EWwE3Rb1g9tdg_Yu95NqK-grNnb40LWYnuf9OzfF99TMiR5rbUxCU4Z7KVWxSUwHS-8ceq7A8UyJPk8cNj0VBy1vUm6mrlEua1pdjmaR3QVzxKIYDfvxd4j1AuZfjTdmrez3qhj7SFT5BJCayGFsct_NGHW7_bI5XOyF4O8T9KD17OV_n6B6Gl65pGAenHGFt75hwS0Qjcib7MR1KR5q7jNN8OcCQjpjgVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس نتونست لینک مقاله‌ای که بهش دادم رو باز کنه به خاطر firewall امنیتی توییتر، خیلی راحت با قابلیت Browser که اینجا: https://youtu.be/_30_ng3Hyfs یاد دادم، روی دسکتاپ برام هم عکس‌هاش رو دانلود کرد هم مقاله رو کامل ترجمه کرد:)</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4288" target="_blank">📅 14:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4286">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aIarTU2kNoZ22NJa8X670vqwu9G9ksTr4VIFIrPz0xZJTKCATx9lvHHbulVc710qEWd_KC8V6bmYzu9NRAZ-41chHJtVWDFseuYS3eDsSPlmJmWVVTKkHsjX0BWpL3LrsNFyla7a50DJQyL-YAh9NdDFnEGJumQrgpSXGzxQID-SWl4cAnIhceLsmp64MmJNkqeWveC1tEyiK23O7UzNmtNzv16JpDP5ZmVUPF2fGK06BMkScLqGeod4VLJA7SA2MtfjmhjQ1pGpbTPUCEgqHHHxJ92brI-M6Yt4FmtDn7_Qz4Z9fQUFb7eG90odXJLTBoPzsrQUgMHfslwsNHegTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WpDPsIlmfgsJMQnYLGLqdZC758GR344six1QIbFpMfW2PKAPBaIINs488PUyuSxvTtJSwgS81cuuPru-kg9K9G20Oq7x1K9SZZvUk6zgszTTQyaQiRH4DI55TWjatcsm5JygqgZQXERjmu7WNhKpR6roZE5519SI80VjfaMYlnGewtprBvwBC8tMySkg1xTi7yC7QnzX-HCl2cIyxnpL4JQWuh6MLWNhfmXf8ZWyv-1Znvi01b8YsWIz3583oODBufPx6l_j2QtFGMHRwX1_OccOt-YdiQma8qV8htGxkm1NV-eU_ssVWjlmURTRqXSUIVlmcZqjZrcF3yFtnfcaWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرمس نتونست لینک مقاله‌ای که بهش دادم رو باز کنه به خاطر firewall امنیتی توییتر،
خیلی راحت با قابلیت Browser که اینجا:
https://youtu.be/_30_ng3Hyfs
یاد دادم، روی دسکتاپ برام هم عکس‌هاش رو دانلود کرد هم مقاله رو کامل ترجمه کرد:)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4286" target="_blank">📅 14:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4285">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/okRwqzxtM0QMYmOMer4PiqcOmy6DeYujXpe4n7nxolR9Q8ZvLM4tIzcd54oGfhqAdMFwbLglR4D1OvO3me19EQVykQlP6WKqdCFnTbXjQuvsCw9cXWUyTi9TQI4nhxJhJzR_wMkfxjKeoaCWaGd3JGgInTISumYdWGHQeU4eW-5IYjc8daM1zYD83ddZQgzXdQpDg7WSwjLnOjP2YfT3ZgOR0wfQivj-AxSG3UL_rd7lwjItMWxWSp_rFNkWJPXOu5KdR_B1_FhotM-ybK_5D_JNIS3XscPfyK_CWGEPV9eb1RtkO8mc0M9a8_YDGvrd15FFHfkD90wN0-p03ESWCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه با docker کار می‌کنید، احتمالاً درگیر زدن پشت‌سرهمِ دستوراتی مثل
docker ps
و
docker logs --tail 50
هستید تا چندتا کانتینر رو همزمان مدیریت کنید. این کار هم خسته‌کننده‌ست و هم ترمینال رو به هم می‌ریزه.
ابزار
Lazydocker
دقیقاً برای حل همین مشکل ساخته شده؛ یه TUI برای داکر و داکر کامپوز که تمام کارها رو با شورت‌کات‌های کیبورد براتون انجام می‌ده.
-
بدون switch کردن:
همه چیز از مصرف منابع (RAMو CPU) تا لاگ کانتینرها به صورت زنده توی یه داشبورد یکپارچه نشون داده می‌شه.
-
سرعت بالا با کیبورد:
لاگ دیدن، ری‌استارت کردن یا پاک کردن کانتینرها فقط با زدن یک دکمه کیبورد انجام میشه (بدون نیاز به موس).
-
پشتیبانی کامل از Compose:
سرویس‌های داکر کامپوز رو هم به خوبی می‌شناسه و مدیریت می‌کنه.
-
بدون کانفیگ:
با زبان Go نوشته شده و فقط یه فایل اجرایی باینریه؛ نیازی به نصب سرور یا دیپندنسی اضافه نداره.
و خلاصه این ابزار سرعت کارتون رو چند برابر می‌کنه.
گیتهاب Lazydocker  + آموزش نصبش
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4285" target="_blank">📅 14:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4284">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اگر روی هرمس برای اتصال به api به مشکل VPN برمی‌خورید، از تکنیک رایگان وصل کردن پروکسی کلودفلر که توی این ویدئو توضیح و انجام دادم استفاده کنید: https://youtu.be/Ae8oyaIHi9o</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/4284" target="_blank">📅 13:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4283">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پیرو ایمیل یکی از بچه‌ها، تست کردم، با موفقیت بدون شماره مجازی و با atomicmail فیک تونستم api key رایگان Nvidia بگیرم:  سلام متین خوبی داداش متین به خدا شوخی نمیکنم همه میگن سایت انویدیا برای اینکه Api بده باید شماره مجازی بدی و از این کارا من تو گوگل سرج…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4283" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4281">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VFv970vyIHrGuNZWL3-H75w9zSPNY8kWdqbMuyBo3OrBrJggoNL6Jyfa7pJx0Q8gSGXa87lI1y3U3Xm1ZUBnXcRt-0ZhQzspnUiHghxlx4DQHkV2b822O9FYdyacvaNAPwE6iVQlFUaeNoSX6SaKRuHXHbauwkdP9icGIA8-BYtWga0frE4px5pu9k3FU74bbpNap-irxGfaXUJqOCoRquOqNLq-qmWCDB2PwUAFvm-ELHXN8MNPVDng19cTp1c_-iLonlf2jG5HJ2mfm4f4cq-n5tPyVtx5nkNbFPrVdYJXyWpA8TQiNhMP5RUWxAZM4cwXauZBsIeLifGnNRnHZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SIwRfGPGRG3nvzuAHbrpqoTfXCO_zgjArqkg9rDKI9imRjfbsQrviGfHqeTyXjSQPzZ3AYBrOEgrabydtt0P6s_sFwy0YwkWAmn5Juy3PgaRSBz-SYLHB7HQLsPiQ7rOKn9r4-O5do4DbSvZXl9rIP-iguICvv8yMstVAUnS4EIazPWQNIikjlcF2LMeMy9LzhdrysT9otAzcbp0rkxYwdU2L9BilLKtJ0GxQ8rAniLnUFvMTwrxXnUD9g0t0tQbabkeKJ-uJwpqEHPaOAeDPjF3GkxTNBUAk9sbBopwEtBYs8Zo4QAl1dT-mnom-1lUSriXhJhhqy-nML-Ow5r65Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیرو ایمیل یکی از بچه‌ها، تست کردم، با موفقیت بدون شماره مجازی و با atomicmail فیک تونستم api key رایگان Nvidia بگیرم:
سلام متین خوبی داداش
متین به خدا شوخی نمیکنم
همه میگن سایت انویدیا برای اینکه Api بده باید شماره مجازی بدی و از این کارا
من تو گوگل سرج کردم و هنوز هم شماره مجازی نخریده بودم
https://build.nvidia.com/settings/api-keys
ببین دقیقا ادرس هم برات گزاشتم
تو گوگل سرچ کردم Nvidia Get ApiKey
بعد سایت اومد بالا ازم ایمیل خواست
تازه atomicmail وارد کردم ایمیل گوگل هم ندادم
بعد که وارد کردم منو برد تو یک صفحه ای یک کپچا داشت تایید کردم و رمز عبور خواست اونم اوکی کردم
بعد گفت نام کاربری رو وارد کن اونم وارد کردم
منو مستقیم برد تو صفحه apikey ها و استفاده هم کردم
با تشکر از محمد عزیز. نمیدونم انویدیا وریفای رو برای ایمیل‌های شخصی برداشته یا اینکه کلا برداشته</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4281" target="_blank">📅 11:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4280">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اگر روی هرمس برای اتصال به api به مشکل VPN برمی‌خورید، از تکنیک رایگان وصل کردن پروکسی کلودفلر که توی این ویدئو توضیح و انجام دادم استفاده کنید:
https://youtu.be/Ae8oyaIHi9o</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4280" target="_blank">📅 11:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4279">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یه پروژه‌ی خیلی عجیب روی گیت‌هاب (با اسم Pon) منتشر شده به تازگی که تونسته پایتون ۳.۱۴ رو مستقیما به کد ماشین کامپایل کنه و دیگه نیازی به Interpreter و مفسر نداره. این برای پرفورمنس پروژه‌های پایتونی می‌تونه یه انقلاب باشه
👍
https://github.com/can1357/pon
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4279" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4278">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یکی از دوستان رو اون روز باهاش صحبت کردم، برای یادگیری فرانسوی داشت از Hermes استفاده میکرد در کنار منابع و ... دیگه‌اش. و به شدت راضی بود و می‌گفت حس میکنم بازدهیم چندین برابر شده
جالب بود برای خودم</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4278" target="_blank">📅 02:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4277">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یعنی حس خوبی که وقتی از api رایگان در سطح کلان(
😂
) استفاده می‌کنی، با هیچی قابل مقایسه نیست. فکر کنم Open Code ازم شکایت کنه اینطور که دارم توکن میسوزونم</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4277" target="_blank">📅 00:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4276">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یعنی حس خوبی که وقتی از api رایگان در سطح کلان(
😂
) استفاده می‌کنی، با هیچی قابل مقایسه نیست.
فکر کنم Open Code ازم شکایت کنه اینطور که دارم توکن میسوزونم</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4276" target="_blank">📅 00:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4275">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d956281ee.mp4?token=T8TBzZj5I6gW6c_13Tl8uu9KDTjdVpy6F1aTvFQJTF3TKl9mn9FA1digQXhsK1CHP9t8Ka4vBt1HRqeg8C8Gs2r8UGI0cJ7YdUJsW1E2YhSh518JXBTYWRV9O08uxMxTn0AWjLBk1Spt5Qru34z9UvFo2KnRmIx8rp9h6baztl8KDscaX3PKyO82A292DcAksstFPUbld15esSwYytkbYVFi8RT0izC7luT_kI3EJ9XZAceWgpNFdpdMMjxM9eb18iiknQpbd5lrF3ypJvjZXYQy3jVbEqn-0u9ABhYE6KeLr2PbUKkTSAQ9B_dYSmoM-ca3oue0QIrgT0H_tAWxeFSBRodXKqpycrbKY-tzKW9OyA1m1gnRNkRmGluub8r8clcLqI3_uGQiFEsJ3TlLgTSYs5ln2lvDB7di1sTrGKE_jAzLAhDGlDYJ0A3xPw1_M7P1-5TzVMNFglQDKHCOYr_aZW-e77mBtNIouhJhn3jgxsiWcMHMusmo8lh39csjSeAy8UyKc9FyWICJErlCw8ylSU4zj4qyOeKBpx4-4urYvTMiM3YpgdQC9Iiqak69SxTcDlfPXZstqCOT4MXqsNvnw0ec1Zrkq8H4piBpVGSa5Hdv0NmUf1WSIu0i6HLlWxMiWn9k2AvCxMwuELK9Ltyi_1CfiGzSD00Kj6zvWnE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d956281ee.mp4?token=T8TBzZj5I6gW6c_13Tl8uu9KDTjdVpy6F1aTvFQJTF3TKl9mn9FA1digQXhsK1CHP9t8Ka4vBt1HRqeg8C8Gs2r8UGI0cJ7YdUJsW1E2YhSh518JXBTYWRV9O08uxMxTn0AWjLBk1Spt5Qru34z9UvFo2KnRmIx8rp9h6baztl8KDscaX3PKyO82A292DcAksstFPUbld15esSwYytkbYVFi8RT0izC7luT_kI3EJ9XZAceWgpNFdpdMMjxM9eb18iiknQpbd5lrF3ypJvjZXYQy3jVbEqn-0u9ABhYE6KeLr2PbUKkTSAQ9B_dYSmoM-ca3oue0QIrgT0H_tAWxeFSBRodXKqpycrbKY-tzKW9OyA1m1gnRNkRmGluub8r8clcLqI3_uGQiFEsJ3TlLgTSYs5ln2lvDB7di1sTrGKE_jAzLAhDGlDYJ0A3xPw1_M7P1-5TzVMNFglQDKHCOYr_aZW-e77mBtNIouhJhn3jgxsiWcMHMusmo8lh39csjSeAy8UyKc9FyWICJErlCw8ylSU4zj4qyOeKBpx4-4urYvTMiM3YpgdQC9Iiqak69SxTcDlfPXZstqCOT4MXqsNvnw0ec1Zrkq8H4piBpVGSa5Hdv0NmUf1WSIu0i6HLlWxMiWn9k2AvCxMwuELK9Ltyi_1CfiGzSD00Kj6zvWnE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
آموزش کامل Mahsang VPN | تنظیمات جدید CDN Fronting و اتصال پایدار
اگر می‌خواهید با روش جدید اتصال Mahsang آشنا شوید، این ویدیو را از دست ندهید.
✅
آموزش نصب و راه‌اندازی
✅
تنظیمات کامل CDN Fronting
✅
روش جدید اتصال
✅
بررسی تمام گزینه‌های مهم برنامه
✅
نکات افزایش پایداری اتصال و رفع مشکلات رایج
اگر قبلاً در اتصال یا تنظیمات Mahsang سؤال داشتید، احتمالاً پاسخ آن را در این آموزش پیدا خواهید کرد.
🎥
ویدیو را از کانال TakTarfand ببینید و اگر مفید بود، برای دوستانتان هم ارسال کنید.
لینک مشاهده ویدیو در یوتیوب :
https://youtu.be/35-GhIi-egg
@mobamoz_channel
⚡️
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4275" target="_blank">📅 23:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4274">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام
❤️
توی این آموزش، تمام بخش‌های برنامه V2Ray را از مبتدی تا حرفه‌ای به‌صورت کامل بررسی کردیم؛ از اضافه کردن کانفیگ و Subscription گرفته تا تنظیمات پیشرفته، Routing، آپدیت برنامه و حالت‌های مختلف Tunnel.
🇺🇦
لینک آموزش در یوتیوب:
https://youtu.be/i1-XenoSalk?si=5jbQK3BrGAe4ctsu
اگر موضوع یا نرم‌افزار دیگری هست که دوست دارید آموزش کاملش را ببینید، داخل کامنت‌های یوتیوب یا گروه تلگرام پیشنهاد بدید تا برای آن هم آموزش تهیه کنیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/4274" target="_blank">📅 22:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4273">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">توی همین 5 دقیقه شد دو میلیون</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4273" target="_blank">📅 20:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4272">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FbHZ5JisR1z5nbCcCYGZCXDNV_7H1iaoOTy1RBg08LtDEEisvARvtiul_HfEQgOxeZOXDhtZJre4hW3OAi296YOkjRxCCuDxF1xDN2a9G8_J-YcIg3PsKY-TICLU0PiT1KHtg-kLkXduF-Raw95aNKFcsLhBub1c9ffx-tu907bx4Cp11IbiY7COWfL9SM93NRtIso-3oisCUoMCOlnw1l_BtBKbROvh4pY98ZRtmN9xWD9kxUGj4KQ8qgD1ezhgyHGUf-N8UsYsZJLoNAmLMvSMwF6C6DBnB8blnyotwCRkFOeG351QxqPCbw7IyXiHt0-jzfm9qSB1k2928kxY4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوری داره توکن می‌خوره که واقعا توصیه میکنم همچین کارهایی رو با api پولی و اشتراکای محدود مثل claude pro انجام ندین درود بر چین
😂
😂</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4272" target="_blank">📅 19:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4271">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h0mzlXVgeq2RbDZSw3RGBp6YxzyTi3SBo_5k6DDb8uNbDg9LXGpvGtH2RtInGmP8erLd68u7MGYd3kabKXNOmG0lvedEjT4-E7s5vdnrzilcjAgUPgBojRB1AR5qKLd2-0h61nm_7Y7G3WLSxA7fJBm4FeBhIG38Ko84PnyJz-2UVPToL33Dape_E865PXwtElP98O6hE-5UoneYU2e_Te4LTOVgUKqOhDQADiUv6LkGl81HJQ3mSmGO66BGV1cQTsBSAu-55pXbXH6TZ6fMZ1tlYF0DnfadabXxfEyw04XCI1kZD9hjJkWj8bto6DXuU_6FPaddaRpRcd7OphvpAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوری داره توکن می‌خوره که واقعا توصیه میکنم همچین کارهایی رو با api پولی و اشتراکای محدود مثل claude pro انجام ندین
درود بر چین
😂
😂</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4271" target="_blank">📅 19:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4270">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bs1omWdXJjcoComg732c6GaBAAPtxB_oKCzFWTEGdnoWSdXGV5P3FGMxZYAvqai6ZNN6-3Hgwhy9RWQ_iL-2b_LWB-NN4rZTfu9xQm9yrH8wEzVysuCOjnIkHlMyqI6gIfcW2xK-KL-CkUP1yr7tKX4nKI4B5DYTMWNnh6PSIs0SqfUuwH-3CwkQx1GSkzxRHZ28enQDiw3sAKSiQbDhHgSxm4Tqfs0oDqgZ6BJu7TsXZHmX9Oi4vQsVb6gkX9PgeTwtW7anKqzCFLtnEDAgXTEndBi04_PNaMoyNoaKNbDa9J_yXGU1O8fRDOPOXBcuTvYgUYdbxMSKF9hHuRItWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب این قراره خیلی باحال بشه
😂
برم ببینم تا چه حد پتانسیلشو میتونم بکشم بیرون</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4270" target="_blank">📅 19:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4269">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/juetJc2GeVe5eDTlu0PIj9MrXJg99DQLVmHY8RmBUZOo50n1ZpFHO4W2kdSGxfEBoBQkLaJur3uOSlvccnHgmHq5h-pbJDTK4uCIGHHisknO8HsYVnyr-QBDXr8oDrEmOczWbbz_zHkH3p7yuGhyvl1n_-Lzwhsr1RQet1kWoT-yiMLkQbJAN81qRcJwVzLiUn-hln8oXTSHR_23mqq64YzzcMmX7YC3rWjP-50Rc7Wtrn1mY9CrokO6wNm91_67getnQaVgly-hXzbNmgrryETeh9VBmn8Z720yBgQuZ9akYeA-eEXXhQv2Zl4rAxV1Vfi0UipFj6hO9zghwSEqnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب این قراره خیلی باحال بشه
😂
برم ببینم تا چه حد پتانسیلشو میتونم بکشم بیرون</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4269" target="_blank">📅 19:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4268">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FMcRBb9E_YCM0hkYjjA-x87RioHZnUpLTvfKgwWS1zUy5TIRBYsyQJPgbMob9jy0z1giHyq_jIp7o8XNNo4ha2Jdl5VkjbibrzHbH17X04jLMNbbPNRz_3VAGoU9FDUI-CCrNLVixnxrTFwvXhWs_RhkyH1YVCuQwV_BjQ_vZlezY21AmGcQjy3xGr_l2wm4xYtdPUvxHsth7R5_L2N8PxQ_gYEyD7-DkAS7yDyRCbjXJMmKI1DXGGgE_JUccWttvxC_bipdP6D9TMOH9XMgOEoWDOnaZgKk4nxf6y9UnZIh2vAiuA28JyBfJ2VLA1vf-wFSL3HUvDqvC2cLBKMMXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به زودی احتمالا به Hermes اضافه بشه برای کارای روزمره
😁</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4268" target="_blank">📅 16:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4267">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟  اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4267" target="_blank">📅 07:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4266">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4913b2f340.mp4?token=NDG1WpVQNe47_ErE7ldPv7UeXsYSFtVAL7pUIQJyCTsyfDrPl_lI8cwVqKURZW0SXAyk-7__0d5lhMErGwPXpYLnF1qBDND1ytsiYnAPwPWlt_uMbJCWng9FMjtcxqBACxcA0Pv0n1CG6nZibUJnqhir_8i82LSq4-IViOZpMhYCrcJ_3pzXOpN9ktpX2l0TDXv7cUI3mi1nMzFVcx87BV9aMJ-eeC4IbDZAHmgMsLKF84km9_dvrdv7K8VZGG0GLcY5pAK8x-Wl4UE2gQdAdANV5xiA4idRR5fSKrEtzL8Pxj7hGxsZzjiADTTzhXvFKH9fMe3KWQ9A5yaGBYPtVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4913b2f340.mp4?token=NDG1WpVQNe47_ErE7ldPv7UeXsYSFtVAL7pUIQJyCTsyfDrPl_lI8cwVqKURZW0SXAyk-7__0d5lhMErGwPXpYLnF1qBDND1ytsiYnAPwPWlt_uMbJCWng9FMjtcxqBACxcA0Pv0n1CG6nZibUJnqhir_8i82LSq4-IViOZpMhYCrcJ_3pzXOpN9ktpX2l0TDXv7cUI3mi1nMzFVcx87BV9aMJ-eeC4IbDZAHmgMsLKF84km9_dvrdv7K8VZGG0GLcY5pAK8x-Wl4UE2gQdAdANV5xiA4idRR5fSKrEtzL8Pxj7hGxsZzjiADTTzhXvFKH9fMe3KWQ9A5yaGBYPtVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه ابزار رایگان رو دارم تست میکنم ببینم هایپی که دور و برش هست اصلا واقعیه یا نه و اون عملکردی که می‌خوام ازش رو با مدل پولی مقایسه می‌کنم، اگه خوب بود بهتون یاد میدم</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4266" target="_blank">📅 01:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4265">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رفقا
freemodel.dev
گویا api رایگان از claude opus و اینها میده، منتها به هیچ وجه سایت امنی به نظر نمیرسه. استفاده کنید اما نه برای پروژه‌های حساس و چیزی رو در اختیارش نذارید. روی هرمس شخصی و لوکالتون هم ترجیحا نزنید.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4265" target="_blank">📅 00:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4264">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">متین واقعا باهوشه اولش بهم گفت برو فلان ویدیوم رو تو یوتوب ببین و تمرین کن و وقتی دید اینکارو نمیکنم گفت خب باشه خودم بهت یاد میدم تو کلاس. بعد جلسه اول بهم گف تکلیفم دیدن سه تا از ویدیوهاش و ساختن چیزایی که توشون یاد میده‌ست. و همشو هم باید تا جلسه بعد تحویل…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4264" target="_blank">📅 00:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4263">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">متین واقعا باهوشه
اولش بهم گفت برو فلان ویدیوم رو تو یوتوب ببین و تمرین کن و وقتی دید اینکارو نمیکنم گفت خب باشه خودم بهت یاد میدم تو کلاس.
بعد جلسه اول بهم گف تکلیفم دیدن سه تا از ویدیوهاش و ساختن چیزایی که توشون یاد میده‌ست.
و همشو هم باید تا جلسه بعد تحویل بدم</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4263" target="_blank">📅 00:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4262">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">Matin SenPai
pinned «
خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟  اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4262" target="_blank">📅 23:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4261">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">برای نصب کردن 9Router روی سرور اوبونتو اول sudo apt update && sudo apt upgrade -y curl -fsSL https://get.docker.com | sh sudo systemctl enable --now docker و بعدش این دستور رو بزنید docker run -d \\   --name 9router \\   -p 20128:20128 \\   -v "$HOME/.9router:/app/data"…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4261" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4259">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gKhFBXLSNgKBU9Hl0B7kK-fohlB5Gt2-pk7dLS0hETbRvg7w5Kd63QXaI9eLwLLwHrjNBEpymQnWWyXTMMFm5tLHdbT1h48xu-1qzOHKmKCNhNYw8bNPQ3EBnvMgy5i6c70bDbGSr154y4yImcWANYAOZmR2ZniTY63b1flaF3tF_DZbly-KdlunioYIwUggJi7y4R5I808ap1-yXavHvYJAIiCQC0en_Gnckj08ngZ0mmuMbQ0Zxyg3yXdHHk4382VfS7n4OkZf_-43qmS6hi6fDbQoduu60lZLfFfZkQx8W_vU_Xd-NrtDMMwy1RyHtoiQFuvPZJi5RumsYZmIHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CQHTUstiNiKQvEsG2VFpNFGzF97VWBQd665eeWLysa0AqEogVXCkCXABqF1kml0RWD7ZYHFQC361wWBd_L_yHeaP5m_TVC6tWsT0DeBDptUzZ-oMlqVI1nmgYHMvBL-1mZc7H7lZjnb45ZGBwqLTByiNXu0wT4ye27hoW9UeBdu3vVzrhxULqidPa013EfTaJ02lm8mSs-wjHLKmHtWpvH7Bzsyc7X1aT9UpyAqDukm7wAqijY7jx1IIbfAxhg43Vo5fwtnLPboqsZA2JWN0zdIcU8XW0nM36ZPn7MfiXcjGa_KG2cqrDcqj7xO0fpVnTOyczjBzD-JcQe2AjtSAmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من عذرخواهی می‌کنم از همگی. حق با شما بود. متاسفانه درست بود و الان برای من هم پولی شدن مدل‌های Mimo روی Nara:) گویا سایتشون باگ داشت فعلا از Open router + Nvidia nemotron استفاده می‌کنیم</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4259" target="_blank">📅 22:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4258">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یه ابزار رایگان رو دارم تست میکنم ببینم هایپی که دور و برش هست اصلا واقعیه یا نه و اون عملکردی که می‌خوام ازش رو با مدل پولی مقایسه می‌کنم، اگه خوب بود بهتون یاد میدم</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4258" target="_blank">📅 22:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4257">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">امروز اولین جلسه ی کلاسم با متین برگزار شد و واقعا دوسش داشتم
🌱</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4257" target="_blank">📅 22:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4256">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟
اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر شدن شرایطم، راجب خود برنامه‌نویسی هم ویدئو داریم) ولی در حدی نمی‌بینم خودمو که بخوام توصیه بکنم جدا؛ دوما در حال حاضر، فعلا خودمو نمی‌تونم هنوز متخصص هیچ حوزه‌ای بدونم. که اصلا بخوام راهنمایی‌ای بکنم توی هر حوزه‌ای. خیلی افراد بهتری از من هستن که بخواید سؤال کنید. اما یه سری نکات رو می‌تونم بهتون بگم که خودم با تجربه بهشون رسیدم و شاید مسیرتون رو کمی کوتاه‌تر کنه:
۱- دنبال پرسیدن مسیر از من و دیگری و این و اون نباشید. اگر توی این چرخه‌ی باطل بیفتید و هی دنبال ویدئوهای مصاحبه‌های آدمای معروف راجب زندگیشون برید مثلا زاکربرگ و بیل‌گیتس و... یا حتی پادکستایی مثل طبقه ۱۶ آقای علوی، هیچوقت نمی‌تونید اون چیزی که دنبالش هستید رو پیدا کنید.
صرفا برای اینکه گوش‌ـتون به یه سری اصطلاحات این حوزه عادت کنه این چنین پادکست‌ها و مصاحبه‌ها رو ببینید.
۲- شما الان AI رو دارید رفقا. می‌تونید به راحتی بپرسید، Roadmap درست کنید برای خودتون، شروع کنید به یادگیری، بعدش هم توی توییتر بیاید و وارد کامیونیتی برنامه‌نویسا/یا هر حوزه‌ای بشید، تایم‌لاینتون رو درست کنید و مشارکت کنید توی بحث‌ها، اشتباه کنید، یاد بگیرید، و...
۳- همیشه حواستون باشه که علاقه‌تون کجا ظاهریه و کجا واقعی. خیلیا هستن که دوست دارن «از اینترنت» یا «با کامپیوتر» یا «با گوشی» پول در بیارن، اما اکثر مردم وقتی واردش میشن تازه میفهمن نیم ساعت هم اعصابشون نمیکشه پشت لپ تاپ بشینن. عجولانه تصمیم نگیرید و راجب مسیری که می‌خواید برید، خوب تحقیق کنید
۴- توی یوتوب خیلیا آموزش‌های خوبی دادن؛ با ترکیبش با ai و مشورت باهاش و کاری که می‌خواید بکنید و هدفتون، می‌تونید به یه جمع‌بندی نهایی برسید و اون موقع هست که تازه می‌تونید نظر یه متخصص(مثلا بکند یا ai engineering یا حتی یوتوبر یا دیزاینر یا فرانت اند) رو بپرسید و اون هم برای صیقل دادن Roadmapـتون هست صرفا، نه اینکه بخواد صفر تا صد آموزشی رو بهتون بده. من هم خودم از خیلی از دوستان توییتر راجب بکند پرسیدم وقتی برنامه‌ام کامل شده بود، بعدش رفتم راه خودم رو ادامه دادم. وسط مسیر هم چند بار چرخید پلنم با پروژه‌های مختلف</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4256" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4254">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OXFr4OdZ-0l_aA7gJ0U76Hrd5F-7WOaSmD7jVRu22sylW72Z0ZvxG7e1HQz2EmUOwWAW3Kt-BBZk0mTI9j_MJ00eatZQD0bONQQszDK-Vyo2Esxuz5RfZSIU8f5umt2DC8sHi4PQ0fBwBqasUcf1xEW9zmZwHocSn75UoORJ7davJCe5Q_SVlfWpbNQUlkoZOkMT07fmRt2ciNqVetPRzs-eib86X_36Hq2QV9pVJIQ_uYlr8xJdXE0GWcZmJBRaBVzwcyum6WJzaraBgtNBrUUWFqOSVZSYxTWQ7IHtHJ8td9yvE0pMwLK70eAsfyq6ZDSFeMVGOn2_A9ebO2g8Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mVnbejXBoMxHAPkEjqVkPC8FPeXg_VDhrZB_ZW9H9tG7kzFV7ZHLiCt4XPDYdj_mNzpmoj2v0DgFU6sL9qQbcKmSFV9VOTLN9Dp8q1blK1KECCqJjCSmQ8MVMfwFvJY3rWxqIH2j2L_9gZgjkmZprTkzJCz8nQJW7CLxpPF8N7gYV7gA-h3jqHftNx-mZNG7aVXmDbMUsk63aVHhKXrmh_4VqJsdtVWg-6YBOsBWsFPbHsL4Vi5ZE2KLikxa7Kynu-pEUFiyD5xoZiBWdciDyZn1J4e3eA2DthV8LALg8Op4nCe8v0LEfBiFthDT18Wrb6Dk7hA2xLhBSA92FcP6lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من عذرخواهی می‌کنم از همگی. حق با شما بود. متاسفانه درست بود و الان برای من هم پولی شدن مدل‌های Mimo روی Nara:) گویا سایتشون باگ داشت
فعلا از Open router + Nvidia nemotron استفاده می‌کنیم</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4254" target="_blank">📅 21:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4250">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhitednsProxyProfiler-Android-v1.0.7.apk</div>
  <div class="tg-doc-extra">55.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4250" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پروفایلر پروکسی WhiteDNS نسخه ۱.۰.۷
🛠
پروفایلر پروکسی WhiteDNS یک ابزار تشخیصی برای ویندوز و اندروید است که بهترین ترکیب‌های پروتکل پروکسی/VPN را در یک شبکه پیدا می‌کند. این ابزار می‌تواند هم بررسی‌های محلی بدون VPS و هم تأییدات عمیق‌تر مبتنی بر VPS را اجرا کند.
🌐
ویژگی‌های اصلی
اسکن شبکه محلی:
آزمایش سریع بدون نیاز به اعتبارنامه‌های VPS.
🏠
اسکن VPS:
تأیید از راه دور عمیق‌تر با استفاده از اعتبارنامه‌های VPS شما.
🖥
تست پروتکل‌های VLESS، VMess، Trojan، Shadowsocks، WireGuard، Hysteria و HTTP.
🚀
پشتیبانی از انتقال‌های TCP/RAW، WebSocket، gRPC، XHTTP، HTTPUpgrade و mKCP.
🔄
پشتیبانی از ترکیب‌های TLS، REALITY و بدون امنیت (در صورت معتبر بودن).
🔒
تشخیص دسترسی‌پذیری، فیلترینگ، پورت‌های مسدود شده، مشکلات SNI/TLS و رفتارهای شبیه DPI.
🔍
نمایش نتایج تشخیصی دقیق و اطمینان از شواهد محلی.
📊
کمک به شناسایی ترکیب‌های ایمن‌تر پروتکل، پورت، انتقال و امنیت.
🛡
نحوه استفاده
برای یک آزمایش سریع بدون VPS، گزینه
اسکن شبکه محلی
را انتخاب کنید.
⚡️
از
تنظیمات پیشرفته
برای تست پروتکل‌ها، پورت‌ها، مقادیر SNI، انتقال‌ها و انواع امنیتی بیشتر استفاده کنید.
⚙️
وقتی به شواهد قوی‌تر سمت سرور نیاز دارید، گزینه
اسکن VPS
را انتخاب کنید.
🌍
آی‌پی VPS، پورت SSH، نام کاربری و رمز عبور یا کلید SSH خود را وارد کنید.
🔑
اسکن را شروع کنید و پروفایل پیشنهادی کارآمد یا نتایج تشخیصی را بررسی کنید.
✅
نکته مهم
اسکن محلی نشان می‌دهد که شبکه فعلی شما به چه مواردی دسترسی دارد. اسکن VPS شواهد قوی‌تری ارائه می‌دهد زیرا هم سمت کلاینت و هم آنچه واقعاً به VPS می‌رسد را بررسی می‌کند.
🧐
نسخه:
۱.۰.۷
🏷
@WhiteDNS</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4250" target="_blank">📅 21:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4249">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بهم یاد داد از این وبسایت‌ها برای جزوه‌ها و تحقیقاتم درست کنم</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4249" target="_blank">📅 20:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4243">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AYOW8-VMTC73SKiqYPglMaesOdpx-9hL4KqlbZQnNMXgoIicA8rZbC6urlFdyi8lyEzM8FmolYcx2_OBTG4Wg2MM3spPCzZAfPOXl8-ewfKrJl6qtdAGxLTyuN7Xz2TELVuRqgPlshkXAEexGJ4AYuPPrfWOwW_CHxMy4uszdsvqEngRj5lTcJBnQR6cEXN6slbK_FYDo2AxvZKlWhqD7K6I07sZXWxma-skyvAZbw7P3luid6UoiV0XCz65copxF5vyiU_TlsUCRqAzAJDLUqtHrO7xjQEIrfmsia38EX0X0lv0VOCRwNeEGEqot-LfvhtimdPRIgON09BhbQYHFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s0XRewBb8fS-ofHW6kQj2pVMD7gFzWYvE4PQHNlpvCnx3_fFcaZ-zU9BIh7rX3LDQ54TiJDEmduAmcfoi3tSDLwXlhFKnvfnV82fBXFjaWsVqKZpFVr1rwhgq-54zJE1L87LeQzs8SbzpTnQjJKwUj2D9yNHIPmPqt6MVCAno2lwvNHtbbaEVMfTyD6QTIbe7xi9CHKZizaMt15FVyBidDNViniHnBrmB2aPG08Ea5eMjOpa8NQTTnPvxGILHumjZPsY4TMDfaawoH6WBCvTJIGvOu59-ZA5QhUToqoaj2oAD81L3ia11Ld5dlkIquOHJ7KXwrtJx6eZS1p5ykFYpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oiSpaThLWSp-8TkgpQ1VDloOB68AyhQ1TGIDI0OoL_9vf2Y8dTQDHB9YcY2ABUE28cR2d_kNOdbP9o8XHmtJB0lAUE2r3oIQTkrLbK1Wvt7lakh6CVl5KiZWZqJ_UBOKGYpCJf66StWowL8QAUVUlMQnrn9Ut1m-DOPo5RPmQmsjRgo7UZwjwF5emwM_BqzAorvGje8cUZYm1pdfrAK_r7r-NEqWymZSJlymaAX2g_RIRdEwVcxT0PtVayQaCd1Jjvtmhz5ARzrMvLr0PaGJQHJpVvNWlrXVYM0DT2GnLlo1jrBK9quwhH_YjtftGXEIKYSttkgQ5td_beD0P-74tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NuCuYlahKIi_LKFjQoaPVsjXS5tWcAwpkiTAs0HG2lWfQpaykqWXNhC-eZwXvzkeXD8q-7uRgEvUyuTZR-dltPNVbth4MxWHUpVGiIjZ3hbyTUt65OMJscNyL5xgpjR7t0w2dHXME25qQ1xB9xXU2Iv-ZnecHiGLR0bmya3IU_u_XPBvPFges6cbsqIOVUzZ0Yb6_ydS6FeG-2xx8XMn6e10NQFt5Yf6lSyhvxKEtShydJCNOtGswT0HMH1Je_gidPjuBWYSXHH6Dip8xMIQcQr2vSSbM-K0jxmollbpqXe9cdngOl9hI7fNfj3Yxw7iisSRGoKuucn0PMqtT0mPWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kFVt3yIONFydX7ZKlcYtcZJiXMgwDtxvxkEmUwVtlnNxjnaiBlGbY6i1BslL5RtXzj-aUwJyrEsFB8c0NSe012yl6UtAnADyJxOsbtYtcFBD9V2oVaKL2KxtWuCvpYu7LUv4QUYArfrHOJuWU_0lF_xT26wRtxJrC1kM_pdxhltFYj4vYv39N0HW1ZMsSC1DMjPoY3Mc3gjKkB-hkzMchBRnbjftwtEB0WXb467cSQx8MWaxKlwc8m_MG4-GJSQvsr6OblVmAgwuW9bkSU_aiE1lvl8Wl2HRPXEufWYztnQ9s8EdCMT3erfhdBNM5SJFdKtr7NLoHXgeK12BQJ-l9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BF9puI5p9Qh5tCnUly5hnqEq0TASQixnyQ1ahJ3IlKrPmHnA2iNufy6BILQAlVJPmCjx3aDwf0ilrrgQf63JPN-5aM2j0Cnv-JWSW-FEIrx5sRhKnDolywauffdgH4i6ycvC40mdtJoKxZvnCp0KXt81puKDyJF45wLqng1_ukIoT-_msIJa0GECPAgdvXpd6BcNv5ykkkyOMMt9mu1IdeL4TUmRPW4UsnXCq6smPhxcZrrDnWxOlUa3Leevt1qzZd6tzbvJIh2jbq5hs6bf4uVehxYJpn8cMdrncS3FhOrhbF0DBNoni352x3rzP6LJZr2-RJl0Y7gFrhBeFqkmAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تیم مهسا توی آپدیت جدید، یه صفای حسابی به UI دادن
😁
اما UI کوچیکترین بخش اپ هست که عالی شده.
۱- هسته‌ی سایفون برای ایران بهینه شده و به راحتی تمام، وصل میشه(الان با همون پیام میدم)
۲- اسکنر قدرتمند اضافه شده برای اسکن آیپی cdn_fronting
۳- الان میتونید از سایفون+آیپی تمیزتون، کانفیگ بسازید. مثلا من اینو ساختم با لوکیشن آمریکا:
psiphon://?region=US&protocol=cdn_fronting&aggressive=ON&cdn_type=any&cdn_ips=
104.16.73.68
%2C104.18.180.6&cdn_sni=
pypi.org
&no_sni=false&skip_cert=true&proto_tls=true&proto_http=true&proto_quic=true&builtin=true#psiphon+2026-07-05+20%3A26%3A39
۴- یه منو کامل برای Chain کردن دوتا کانفیگ V2ray(مثلا یه کانفیگ آمریکا دارید که کار نمیکنه، یه کلودفلر دارید که کار میکنه. با کلودفلره وصل میشید به آمریکا و آمریکا VPN نهاییتون میشه)</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4243" target="_blank">📅 20:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4242">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کتاب کامپایلرها و طراحی زبان - Introduction to Compilers and Language Design
اگر دوست دارید بدونید زیر پوست زبان‌های برنامه‌نویسی چی می‌گذره و کامپایلرها چطوری کار می‌کنن، این کتاب آنلاین یه منبع رایگان و عالی برای شروع طراحی زبان و درک کامپایلرهاست. خوندنش برای عمیق‌تر شدن تو مفاهیم پایه‌ای سیستم‌ها خیلی بهتون کمک می‌کنه:
https://dthain.github.io/books/compiler/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4242" target="_blank">📅 20:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4241">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تعداد پنل‌های وی پی ان بر پایه‌ی کلودفلر کم کم از تعداد کاربرا بیشتر میشه
همشونم شبیه هستن تقریبا. زیاد فرقی ندارن با همدیگه</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4241" target="_blank">📅 19:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4240">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بالاخره کار مقدمات و آموزشا تمومه
کم کم توی ویدئوها میریم سمت ساختن پروژه‌های واقعی</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4240" target="_blank">📅 18:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4239">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I8ig6OfIs_HB9XpXHwSEcglICM5w_w80-hJnwgxaLBM46LKgTBP-XMPKi7DdYVXIH_6wdw_nptkuPbEapN50xX_CncgV3laTKCTLsZpr8C8zNMoyCZ8vUSbCDYmzzdmb52h8d8LJHMUMDdk-NUzaBr-2ZRKAhspQdKoSkPMvC6xFaI6ER3Xet_vs4r1f8wcmCw_33AemUy8Kz1AhINtgFWyfRxzBqBujfHVo81OOdZRqO7yLFYUOMp-lH3nY2LNu3hUbDtWCK2RornImT26CfhnTh_B4uxyP4MGZtBtd4knowQ9XbBkFjW0_8aLyB9lNZgkF6DUCPVH_qqHLtIi-lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز Hacker News رو چک کردم، یه سورس تو گیت‌هاب ترند شده که پرامپت‌ها و ساختار دقیقی که برای Design System با مدل Claude استفاده می‌شه رو افشا کرده. برای کسایی که می‌خوان از AI برای ساخت سریع UI کامپوننت‌های یکپارچه و سیستم‌دیزاین استفاده کنن، این ریپازیتوری عالیه. با دستور /learn بدیدش به هرمس و تمام.
گیتهاب پروژه:
https://github.com/Trystan-SA/claude-design-system-prompt
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4239" target="_blank">📅 17:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4237">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Iksbf-wK7JSJvba7FhCBn3ajneK1AQtB5bok3TUHlB_7Xm8nou_h3h7Sptzwb3RDeXoTlHWfYfbVzemrUJLVgEwEc0-yJOtKfTNDgBWRU5ihjZanVu2BUeWuCAae1mHrdZ9syiC2Rry7WtiUpmxKKMnmBp2mI3X8fpjn44ZEsftW-iyahucejtyNf7aLHnmDjhd7_YV33QLyqoz36chOH1a7eEXIVya97cZnt5T5LM6Pm4zvRO2GOc2blR0SLCoT4ouV1buuBrOZ6LHVK-N1F_iWuE-Ut_narhZT26fVJDaGtMmRA92u8XVfsve9JH9fITqOexq5U9PzlrkKjaqUqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/La1bSgR-NYueT3sAzvW9-xoZGq3LLBSdQSJFS2QrzXhF3Qc1F0YMzEV8jwUiJ-6NmoyEjyKcKzm9MBEJ-rD4R3NfSUW4lSUObnJbhPClE_ZGpj0pojDtO2eZyaIxsLrBX36yfRyErd7BKKRBJk24jX9oOmiASpiD8GlzTwdsH1v8PSqp2zKCcimL3AxxODihnAKFaKtEljyWVynjnqO6dnbRjJqPr1p4tqr36r_1HvMZ8UF73YVuz0xtiex-B4p9XeouC6Srz_4rzLS-CM9CX7HBhf53Xp68oFMAGXlS2Wqpq-apx1IKgkj4Xc0fSJGc07KZ8pU_8198vchWeji_qA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه سری از دوستان کامنت گذاشته بودنکه این api nara که پولیه و کردیت می‌خواد و فلان.
سایت Nara چندین تا مدل mimo داره
که همین الان یه اکانت جدید ساختم و مجدد تونستم با api key اش به mimo 2.5 وصل بشم
شما صد درصد از چیزی غیر از mimo 2.5 (mimo hermes , ...) استفاده کردید</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4237" target="_blank">📅 15:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4236">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-Commands-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4236" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات استفاده شده توی ویدئو، با توضیحات کامل
سایت ConEmu برای ترمینال:
https://github.com/ConEmu/ConEmu
سایت Nara برای API رایگان:
https://router.bynara.id</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4236" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4235">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ab2KMBPwzIoLZK9WeVHQu5yUV0jJKLHftP7WGHxYVvTZzsvUrlOyzpc1xkJO2_4Lsw4jDV2OnlrhckV2Ps9r4HMVSszfZtBvTy6M5Lc9yjqgECFB_xI0pSwiSrDZq0efT0iHm4CLplYaA1VBCSaaAo9kzS0jSoPmBiltfETtktF7fPKADohsD5Ig33gXih-EtW0x8hEmjDzF7rLKUTn9cW0Z7jlM9vjTgojBfMcyLZoc8fOYSzQsANQ8aKn1qfI05-Uhd1TOx7i0frWJIpGood59T749wF1HN6o1c06rRCGlX5mN9hCwCuOWI_uw3Xw-kIRpu9YvxGd9TleINcINcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
مثل یه حرفه‌ای از Hermes استفاده کن! 47 دستور مخفی هرمس که باید یاد بگیری
⚡️
فایل خلاصه‌ی دستورات:
https://t.me/MatinSenPaii/4236
⭐️
چندتا از چیزهای باحالی که تو این ویدئو می‌بینید:
دستور
/learn
: با این دستور به هرمس یه داکیومنت یا سایت رو میدی، می‌خوندش و کامل یادش می‌گیره! دفعه بعد که سوال بپرسی از همون دیتایی که یاد گرفته بهت جواب میده. همینطور ازش یه Skill شخصی هم می‌سازه!
دستور
/goal
: یه هدف بلندمدت براش تعریف می‌کنی و اون توی کل پروسه‌ی توسعه یادش می‌مونه که باید به اون هدف پایبند باشه.
دستور
/snapshot
و
/rollback
: دقیقاً مثل سیو/لود کردن تو بازی‌ها. یه جای کار رو سیو می‌کنی، اگه هوش مصنوعی گند زد، با یه دکمه برمی‌گردی به قبل!
دستور
/yolo
: خاموش کردن ترمزهای امنیتی هرمس!
دستور
/suggestions
: اگه گیر کردی و نمی‌دونی قدم بعدی برای پروژه‌ات(یا زندگیت
😂
) چیه، اینو می‌زنی و خودش کارهای هوشمندانه‌ای که میشه انجام داد رو بهت پیشنهاد می‌ده
دستور
/moa
: ترکیب قدرت چندتا هوش مصنوعی با هم (Mixture of Agents) برای حل باگ‌های غیرممکن. با چندتا مدل موازی و یه مدل تهاجمی
دستور
/browser
و
/bg
: دور زدن محدودیت سرچ تمامی مرورگرها برای ایجنت با CDP (Chrome DevTools Protocol). این یکی فوق‌العادست
دستور
/pet
: این رو دیگه باید خودتون ببینید...
😂
بتمن رو تبدیل به ترمینال پت می‌کنیم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api رایگان هم استفاده شده توی کل ویدئو. دو تا ویدئوی قبل رو دیده باشید، عالیه
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4235" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4234">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دانش و پیشرفت علمی، پیش از هر چیز، به پذیرش نیاز دارد. دنیای علم آن‌قدر گسترده و پیچیده است که با ورود به آن، با انبوهی از اطلاعات و دیدگاه‌ها روبه‌رو می‌شویم؛ دیدگاه‌هایی که گاهی با باورها و عقاید ما همسو نیستند. اما اگر ظرفیت پذیرش در ما وجود نداشته باشد،…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4234" target="_blank">📅 02:11 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
