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
<img src="https://cdn4.telesco.pe/file/tSSl_Z0Lx-9yWpSxbU4W3CW1FZ8nep-_C2sCvNUjRUppck7dFzkALkDMHPFt7twia05Pqw1SQ90qGVnKJhUfi28m8NKP-0bETY6_SSX0O2KS2ROsBEEnVE4UEdLxt6djuE2lMsGw2l534_7RiCwDv62h6y-B5Tj98wHC1SIVSAQVo8fRkOFeyWhYrGVwbDf2OiRGkvyb9jCBWJ8_iznPd23ymbPHolxFp8t4MTwPnIEKg6ufINymsVTRIHk1zO7LZNn02KKSJB5tP7AyIZmDNLEbYsXCNU3IBWWL1uazJQxvSkNmXC4aFWZXm-GIjHvY5xsk3oxowIuRkghlG0G-mQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.63K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 21:24:35</div>
<hr>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #100</div>
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
#ArchiveTell</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 675 · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjUp5a_4bZJTpLBmIhGUUk_UojawqM2Rm-a3qUO3w9xlaPBz3PJm7_lJCFPxjGA8RdH3RWTNsmMRW3du4VLFyVjWW2dROPBDhe9_V6G_dSC2_VdNHzcIdGX6qthc3OajYMI4c2NAOVpMLLWTbsABiZ4kKCuLPPvdeanq2klMTm9qnlJVXZfBJ0ioINXrG-t-qH6BLV4SzuO8vycyvdLPOKsyxal6g-WSlGCjrwAt2nKzgRraqwjaHHf4ZX64CuVQintF3kq3byuPNEpw_P4y6Y7ZBWGQSct3raMXm48-04WduYrhjXH0mqGR-_nQSMhTslcLhTpxy2vcjRl3YR7JDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 694 · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
100GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 32 / 64
💾
حجم تخصیص یافته: مخزن
⏰
مدت اعتبار: مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbqTPImMueLyCxTymN9YhWF03AT7MzYUUKIqvy7L7OHzJVFguqAbEETGaAhZwo5mNw9F2KWfecSUCeNZkZ8oSlbdPDUQ4jrQZPK_ywNSmSHpjpZ_AC2A6B29cDvVKop2KpCj-P54Jb38rQBTmDNckJxERJwg5xkmu87WLrdg55CGTL3eydUBoNbGs70DP9MCQ5NDFhbED8qLz74-ibGxxPRaFElC6CYZDd7bknqigztRpM1vZwZKsA8GMxwymbkM5DKpQ-3PQ8Gp_ziAs8HVTFQiLbVLZPJuf_E-UfgucoX4Bwhfx6MJNUate1ZiSOqFlryhNqWe9NkCELsijsLZKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZ1YdhqOPd08WL2ooZXs09wfNKWod0shur6oPS9d1JN1R0THFLOIrJXfGEnrB38HpI9Ub34dk8yLI7UnUUsr4z2Stnr9Z7ZdEIKxvAwrjZyW-IV2mHEXUnTJ9ZqvzM1R-P8Wo7yr4_ROepHNcjAP6apN1tfEEyeC1zLYJbaiqr-LAZlJBaNbNIx3L3MITLuZMwqEZAl3Diwr9GRgIrCziqsoUkZreG8Es12KYrjGu9in97Urm_N6Mkzr79Nt1_jCevQsAo10vKZiZbmh2_E2CL5guKbRlFQMCRcPlr-xxfMIiexVUlGXV3YhV54mf-KGtxF5rY3xbgiGJD9AKSXqGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5E5MttT82gEWfuWLBltRURoswNrn-6SID5VKyfBdNyRNAGZxTqVUBVeUodwPrgmceJ_96rPaYyV9oVGFjbQAwK_Maek6oXu_Kq9YCdYK7pTabaTPMkjs0c7jow32IIr1nHuoH3ggSS8qhNOefDMIfCAeMHpr_wbfMWIV7J3jk8gB6Zrv2_lBLhWMZVPQH1AvZvIXbB8ST3aFO24feu-4eQEeVfvaLPjealQO3fPYP4aqqkUV9B_cTl038rusaFhUVzio3ZABJ-BB8DexpQ0fzZDpAprHpFhAMotmkQw13k9WGA8SKgYWGX1CNJ0FtUUcuNOPIQNiYaVmWrem9oGZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmBfxILFbdHUResqZw3qVFT3kjf3RcTEazo-zsIicC035DABGw5L4Fn95SosqP79QewQd6bLLYS6La_V7uw4rEK1WdDs3Spp1YT5wh1lOlZBA1kQVdPu60jKeBBavYqYqEOWm6_hEyUf3nYtNEHq5IcQOxLM3P4WqonLK87yvpzB7UnT6TH0wL47cBdYZwIOpk3ZTcur8OFSCaVP4DEmXwBDLmaLdD5mZDaleB8lsLsnoErqa1MYwASSt_f-GXeuvGw7Fr_cvRcGgvoGmMz5MZ5F_eGR2c9AY3MYH-Kcc4_CLJbKlo8vRij96MbMIjVkOmyYIWcdvhGvy2VlimIV5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mo6u7WMjr3fxVA0wunLDUTFPFpg9zDQUtjBuqOq9F5baNX9SrfNamsRLGG5070GR5eh3XnSFB7N4DX6Qhz6MqYG0W7tzQn6UOWKfsFahtES5Mt-nABuiaeYvGM59DttDLHXVacgQnkVTIWB9YeRCIiG755tyMWZQzqbx0MXqZOch6OJB8grPVB8yCo7Iph7XvMy8phmD8db1HpL8qajmIChW9nee0H5-0OZPOaxU5npkAjJMHTLAZn6_u39k-i7iF3yeMZiDNOobtDafq_RCqZu_ZeAlz1DpljhPCH3jO_-WdDFJnfUJ_U1R_enNEt7rOdjDr-lO4ML9N7eQMp-ePw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnwKRE_N_PGBuDPMQGbXXhkOkzifoSdkS2WN54jJCzuet_Xy1ZPEUZ3Oqsa1DhGU78c6WX9A_Cjd04O1WjhLDGOc9WUDl4l1_AVR9CQgZPt7Iwe6w2FfjSoB9Xp2aKZndKKCtc4sBCZaHBaummTCvkFxmcJ2ejFoHotsXgFamTQDiQp18G9uPF59wCTEGwPapAc-5nJ2yEZ4GRnxgckFaUwCYaRe1cmtmqPe8aXpLauqwCmI9zHSdCB1pYRONjjLaADCe5sFJchJ99DKdxFc6d8PGIRIqxmXZY9WmEaNbbTmZXsv5cvrCq1cksXn2D7ehiwLNejbVSbpLVUrFT-bFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIU-p14hNTFmDcFZ8e5vKsMXt7oCoP4Z07MLNph5LgoHWv4jT63mEw59zvZTka3ICx8dNLtyxbaRl7RVpAM4jtUmK8fjrZ1ckXmSoxEdRjkczG6otHMiLCVd_-yTidg1812Lc3IXk_9LC_QUZZ_reipIkjtmMLAl-cHNbwPOfsGsbLKIuuaFpdp4mvSk9DIkdeWzKhmXu_xTuWUJM9ZNzz2CrGJS5LRZ6y6LrPNJ4mc6c3x7ACMmxUQSWUsM9VaLSMBaueVo5LmN8Ks_f4Wna1KSvchHjxzBJySyNmhHm8BdrA42WgoUmoySCFnNFdiVitclAS48C1N_Aab6532PUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=VcnjxlGE4Id09e0PXhEOGDznsQfejzo_mjYzFO6knTXjNw0uM-5M8NVQKL0E-Cbs4FDCUoDqrFagl9HpDXs4WgusHP29X5KQWp7fE-YTJUNqsG7UG_bLJaLAljnMotKWZfOktbK7yOCDVeVFFObOA9NDL-RV4uJ4Jt83SaPv2IEy7d_nYtI9DszMIJUQ5PFNcFxkTb3IaCjv7zzdpjwFk_fqPFQts1Q5Hwrxwd4SDw3KLOI_gdTUuU4Xv01ua4GCyE5FuqaYfULh8ZE_c4vedjeNeG9hWqjMczrnr-WvxE4uzXzHmLgoQd5G0IekDNENjBmsjf9KH_QstQmatj5IOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=VcnjxlGE4Id09e0PXhEOGDznsQfejzo_mjYzFO6knTXjNw0uM-5M8NVQKL0E-Cbs4FDCUoDqrFagl9HpDXs4WgusHP29X5KQWp7fE-YTJUNqsG7UG_bLJaLAljnMotKWZfOktbK7yOCDVeVFFObOA9NDL-RV4uJ4Jt83SaPv2IEy7d_nYtI9DszMIJUQ5PFNcFxkTb3IaCjv7zzdpjwFk_fqPFQts1Q5Hwrxwd4SDw3KLOI_gdTUuU4Xv01ua4GCyE5FuqaYfULh8ZE_c4vedjeNeG9hWqjMczrnr-WvxE4uzXzHmLgoQd5G0IekDNENjBmsjf9KH_QstQmatj5IOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlJhSI_bnXCEp5PkaYby9ldgWgwryoHhZJlbReYLgBd9X1k5I3--6NbnAz1a-pykBQka_Qo-XyZ4098ifFKYjwVFHfTZR1fU8Lo08CrjPzEY1N2BBZTs0ik9108vt-ujHeYSG0QZj1zbDMxHxw4Y2harvjGGRtOPTstaloUUkjUvqP9IXVlcUKRVuGKVRBzvdBAdhdo18Ju5QGXXam8R1T9BG81_16Vzg8oFoGUkyJl5F-1tngAbbe50xYj5WeLLevCrnL-Nf7_0ruiFpD2-nPWk7217zU5v-frcrkPdNtKr-NLvi67eS4orlEBzYB-Wdalz0vDCeCTzpI4afaM3ZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjgJXOpqmVRRMAdIUtpXteC7__pZ_PkezJ5uQA86CTZ6gU-rhFGasDvu_8S_2mRGUWjVlYyRBP9DMmIU9WXhpmEw6w5oH4ITSnnvoOPCbSAcqUCOF8uNmCMyHCiq5lZ834tfenkb98CJYvtp98-TcWC4O65WKtIm-UdBWwHSLHBenzcv1cxMFinn9ImAExFDl6YoxSThHSTpSuNtTxjAOJa4dMiQCPMpMTnu4vF7boNxEv5QGiGwSmkJUDMjchHqoxPYCqXvpOsqFgV5LOIgTAusZ8AKzmZogATEsGoGAck_wTktN1Q-1LmkEDry7XxIJ2hyvdZ1NxBk9MV92xrS6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=bTwHfZyqbG1V6p4H70eAY1onDVIo5_3JltuXovFDqa7rLO7ncNnN6aKEdO6ZVqt-kPIr4-qPE6gJ1k6yp85HmG7welWu9SDVsCuBWFTxofQbwTKW4EdgSoZeA_VLekaDjxwREiifd9XSU4ISJDBLSXxEoeX2E1GjF_05gyPtXW2E9kL8gvaGBHMrVLzH9hYYsxSHtKnLhYLmqIkfd2OkMDzZY-jrazgxbX3q1Tm4aWAAGcg8sUT_2boVGIM0eOgofK8sNPdB99V9F2z_wwNqjpW2JTpUxPVE-RHGv5masBJIcO5cUC8NzPKcr_0k6F1emtA38kCHpy9xwU2_BQYFsbCpi0av06jvf4hPcD1RjOvSllJGxfgf0pGNiqCFL6YZkzLuTUJgD2zvmZMj2BltnZRsw167Cxe71TkCeBbCXi6Xy7___Jcl1Tvvmtcpy44bMV1DCoon3l8--ngLTAgFwqDNjOdD6ARfNRcDrcfBy50vz-O5z4UBWSKc5YFtaGMfXd63Yz2QMKGydE97vyFHN7LqDQ87OZXPreoQCph3YbWLuMAWSYnBiHa6XLKioG_-WNIzj-fYna3TAuyiH-44UhwcjD84aLojAGIvby32hq1ViOvAsku7OYjMFYK7Y1dceL2bnSnKGK8sSz1VGqP5h5BDlCL7gFjelwXVd9E4AGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=bTwHfZyqbG1V6p4H70eAY1onDVIo5_3JltuXovFDqa7rLO7ncNnN6aKEdO6ZVqt-kPIr4-qPE6gJ1k6yp85HmG7welWu9SDVsCuBWFTxofQbwTKW4EdgSoZeA_VLekaDjxwREiifd9XSU4ISJDBLSXxEoeX2E1GjF_05gyPtXW2E9kL8gvaGBHMrVLzH9hYYsxSHtKnLhYLmqIkfd2OkMDzZY-jrazgxbX3q1Tm4aWAAGcg8sUT_2boVGIM0eOgofK8sNPdB99V9F2z_wwNqjpW2JTpUxPVE-RHGv5masBJIcO5cUC8NzPKcr_0k6F1emtA38kCHpy9xwU2_BQYFsbCpi0av06jvf4hPcD1RjOvSllJGxfgf0pGNiqCFL6YZkzLuTUJgD2zvmZMj2BltnZRsw167Cxe71TkCeBbCXi6Xy7___Jcl1Tvvmtcpy44bMV1DCoon3l8--ngLTAgFwqDNjOdD6ARfNRcDrcfBy50vz-O5z4UBWSKc5YFtaGMfXd63Yz2QMKGydE97vyFHN7LqDQ87OZXPreoQCph3YbWLuMAWSYnBiHa6XLKioG_-WNIzj-fYna3TAuyiH-44UhwcjD84aLojAGIvby32hq1ViOvAsku7OYjMFYK7Y1dceL2bnSnKGK8sSz1VGqP5h5BDlCL7gFjelwXVd9E4AGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=tH65ZAU7bQ7roYfF5l5iqN0M9xLQijR20dAIu1_CZ_Q1CrBedpOcLyAHNJ-6KowGmjnSmqGcJS_aLcbo64Br7B7XPQYzw9DZz8pAcyGMaRmI41HX9UlVpvSkPMRBMlsLlPTeYmsshtAyUUllenERqTRzwhv1NBhg44ENqKbiggn4FPth3N9xClvs3o5xCZKYjAaeWvFbzCDd8r8tFJswWNwWGcBvVuqztXBUScrdLIHWWme4SnshM3BUalXtUyvUmKDPSFyn7wuhKHaBFcGmWeiQMayp-wpGV4DqbLXgTkMCAmveO9aO_g2M5usS95JlPd3u453knUiD0BcPZb7uVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=tH65ZAU7bQ7roYfF5l5iqN0M9xLQijR20dAIu1_CZ_Q1CrBedpOcLyAHNJ-6KowGmjnSmqGcJS_aLcbo64Br7B7XPQYzw9DZz8pAcyGMaRmI41HX9UlVpvSkPMRBMlsLlPTeYmsshtAyUUllenERqTRzwhv1NBhg44ENqKbiggn4FPth3N9xClvs3o5xCZKYjAaeWvFbzCDd8r8tFJswWNwWGcBvVuqztXBUScrdLIHWWme4SnshM3BUalXtUyvUmKDPSFyn7wuhKHaBFcGmWeiQMayp-wpGV4DqbLXgTkMCAmveO9aO_g2M5usS95JlPd3u453knUiD0BcPZb7uVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_y7KVg0oAX4zB7pT79sA0Gdw3hLM2NdSYpmIDob_Hv3ZdByRyzzNyNNcSiCvnlhbj2Cec9Ao1ssUriK4wpZzPdbzOeL1Fhk1friNPZQBu9hFQ1wWqJBvJE2NeKTeNpLXIMbq1c-ZE10-k73CDVe7uGLZNCehnq3P4sq_TmAA1Ctxr_dKYYp7mzTxgePXmKSyUzGgfkccbXPD3fk_1rCXXfur4Z4eVNiouKizxj4LfPVau3Wz1JKvdbm9BZ0loKb9n8DFhcxpw2Ler5uo0-GbHo8qzRyPASk9J2TWveuzkvh3hufubHcifYMR4qEhrXLsSxjwBlOXF4df0-V9DqvnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdQTL8wo90SExEt3Tte3BxjCbt5iybeOj2yQP_QddbH7NU_uZfyb7xf_a8aGslfFNfEx7D-zkGKtXBh1A2EwRHeagy30gWC3zdtaYWgPnWj-MNKgP4kD_GShAptIlecG2R-wWGe2Qq8BDgzqIFYQ3-DYU2g0MfIestp7b3TkH8cCK4PRMTz7v-f7e6TAvxT8AhQLDkUfvN-rkI5DhH5bS9M7n0NcgzwhTJwKbu9dCfbrwrqdWWluuzc8MJjS0Vplh71H9h244XZXS5c-m9oynO9WIdGtr_Eu_67deUFj1uMJjhma_ANgm1WhOiUFuSQtehIkNUNzdbdAWKV_LLEhYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vgbtPSG-9RDb9pkZFxgP3AYsoebMfAQrhEGlP0nBaWDFNCVT8bSKaYeqaAjupZDru0G8M_ovAuTp_fFFmB0GRibhVrwl4EFdJdFx3_yKKpvyDZN6CnnhifrvJkiWJG02Cij3-nHZXvEpbHNPdsLeTXiwjKm7zh4u1tQxojq0dGRiJcybOn0Qo10qFTNotSsiXG1xlXhohHWijShwqxuUTAm2bsfWZy95YLxikkGGvGy4vgrTrhfhO8tL34gy1mNUWJ7bDH97qRF8F8NnLGnMyJjH27lxwfzmvcOJEg3jqKuDUigwR6zE5t66hSrEA7fxKCDHETmu2m3xKpg-bSTBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pYB1AxEV17iVVtlxSCQZA1Nod4GC81n2IMGXCehticCKzMA2QJspxaAg3caC_EYdbZf9Boo_bZ5TpS-_kX7XMbJqH--wLEH4FgtvC41vPZMYf7HMYkjS38Qa0q5LDTeYMGmGu8tLpt1-aafyKtNUXRE65BFR6Q7s1U31Oc1aJYYPJ_YDBbk_9bO3G7QiLd3k0_RAcK87yhclw9iAfRtOgAVQj0aqcn-EpVoizPfT0VhTux8gBKjYOCsaNnlw983QJf3wq4lbyvUKjcBxD4rId69z2wx4o3fAwC9d-DYVRnZS9T0QIpBtLfuWdBCjvLK3zvy_79XSNBtB2D26MfHzvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jqtPlCX4Z8i8IoWIDgRAKs6pLf5ZFN16iIQDp3xH-V_pvuNTINqj9XjY8N6_TLKd0qm2GwxR5tUw-3h3Xr5VwfaFKUK-eP0Fx19WbIS4Vzim6hKT4xKW8T4DTJm7vWSKN-_iBQCAOTmOtTR2hltEqHDpiSn1O9mHnaejzUibxJoMpeFmpnV9qZ_WS588DW_vuNoYnr00JwJ1gt48qpQWC_5h5WCV0cv_b5IMKaPJ4Ihwpue9wnC0GgOXi6KLFs_RhqGYdE7H7xzDI44fVuq0EV9CBTxPLmUTahgQ_usnVhCn_TwuTCNTuMystmjo1GgfYZziLe9lA6TzVuiDTBtp6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">7. به صفحه اصلی ورکری که ساختید برگردید و بزنید روی پیجی که ساختین تا باز بشه
این صفحه nginx که اومد یعنی اوکیه اگه ارور 1101 گرفتین یعنی اکانتتون بن شده باید یه اکانت جدید کلودفلیر بسازید
به اخر نوار ادرس یه admin اضافه کنید تا پنل باز بشه و پسورد رو وارد کنید و لینک سابی که میده رو کپی کنید و داخل ویتوری وارد کنید.
کانفیگایی که میده اگه پینگ نداد نیاز به ای پی تمیز کلود فلیر دارید.
مثلا این رو با پورت 443 وارد یکی از کانفیگا بکنید تا وصل بشه
188.114.97.6</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dw01GjsP_svTyZ7bwO0cYfSKq_AYji7K84an1Ln7CQfxIGa2dOt_nNiGyuXCIEEv62C7JR1aoMRx0Y3bEHhrm5dxqXGEXc-C73yfLqTpWn2YxXT8wZ-efzWycRgR3YTofiARyr7w-azkyw5t79nV8YDRLGk-WAuNIAzj5bmPak8ezjGwsqTyMVNMR4xRU9vn2r5Dd587LYHjf0-6UvbKPpWTuhisEsWg57aO0lRgleXK_g04F5exPjdGcjymcr--ef9q71nk898nfE4k4oAQ2Ejj8rf3Q94n1b8WlXXSM1ACodvWmfAC_KhybvfOT7T93GHnfN_U1w6iM8AoYR0Tfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saHYcLgUziRKRw5kme0952Ep6n5ZrtzToPHDRDWeJP8M_Xse6b1CyhjugG_v-rHSlSkjJjPDcxVgYsra3RthSwzJSnJN-Om6EyQjwtbRlUFIrCUopEaFk7Gmh3a9K3KTvMiy4mMVoFZ_T45O5ENKOq7u5_KR1lTcmqkQ-3ziBBBuph_zGbhQMYT1EGS2HVIPQrOqJYjvXnJ80RDuO8KPFnkhEmOp8XjMLpTPzXbt1hPebzZyAAYVMiMBH4ef16oRt5f7nRoLli5_wSJtk69adYkP5Blz94SmOclkSf5lsxznBpt7axr6qggcGqtr_eVDq-1jJQMf-x02aWiK0LSFlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9IH9_q2itHxlpVGaNelq4FnmENsgMZsRlPerjjaMS2VjTcrDxxUOKIj0prumjp72nX5k4e125yGwVNH8C9UBFzpRVpzvSMvBZMaiYtnIaU6xePgpxIfgQB2TLI6h7_EaOFmCh-IytqNwH3p36A6vhdBRrwbttbTCJmiy4tupbw2ZoJSRGzrigA43Wc8_cuyJmX0cskM8M2VWZDAJiELf2qUm7kEdRkVfhQUju2D_etvuUy2ygixL6GfCO3zZxzJguprG_i8EYY7JSbwZdP91DvrDreeXWy8P_xt0ltZAlWZcuBMAOwK2k5QxBa-BsW6hYR6K4l4l2fT4AGMpEQhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNfjFz_nkJoDsoBsBpT_-SHVbSotLlkCQgDZggCu1WLexuOaDtKdTYj69noASe_FYpbDTUY_tOIcMsOFQMzADQ1ydd97Nt5JU6rvVAcz-aLk5vbndmhOLTe4Bco-ovlFJeFMQHeRnlfbze4cJB9S5pzsnJXrR8D3XFMBXJ-sEw1Rq5YIJDZDJSzhoarsq6VI5yD4dgvNSyr1UST5pFeUa7CsJnF9Ts11CZBqC6WuCyVnP3nbQ85JlbgrTMFJiefGyyZ_kc3rRUbSgm8Zrk1gxmt7A4II64Y_j_WyL9cqAItTeSFjLBtRiOtVPIboCgu-ZTQmBWg6w0PbqXzZpAHQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkx5GofuFmocPEVrrGCUQ4kf69w9b-0FbbMWW1bKivejqAB9miLYPP-vxVyavlBfQhNGFKQDKkSMgv1-1F4xdbHV1GAq2pwueeHmG0Kt6BTjtWss47nDEg-ogOvtuhfi4Eu18azj7wGb9d7qdfjHcJalbl558JNV1Q8x3daStKPlmIthyuvgl4n99jDBGZzC_L-oLc94OxxjSDPSF3AEpY6Wm9agEwmA0jcT1SpQ13sYPAbZLJtsuACqC-qOjds7VQIzxOvHfD9yAC05N_Zaeeu-x--HtVoX6ek3dSWcKrUfDQZU1QAO321pRIl0Ok7xnaprXW4tyaE2BlsRPgvqeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibz7t1Rr2vM-5jXdkQVJgwZWrKHQ-UuVYlKhvs0yetNxCdI5JfMdOEekVPZjVXXRXfU80mhM2WyBypCGTrIdFOBbbKmDpU9anv9e5VW596Vf_lJFdxQPLBQalJxYd3w9ALdJ1MlS2XYdXjtVtSPCdarbBzkZ-ltJONRqimxWYz6m9ds1ofa-Qg5vNEcz1i0YNmqlR-uCm1DLDFKXdTrGW86cW2dCnWKSanNVbG34P0sfRdX3VZ_KsxKqYItQT9f2jtV2flS9LjyW9S5v62kYGV7zHUZzeGK0EelyG7Nn-DuAK8vLXiQuKX91GOnU4teHcMRYtnqZLMtFIoyhWcfVag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6FIJAbFnOxeFp49WcM2Zce4tg4LnHwg2nrbr8XQ7xfQ6X6du2MGW7hmfh5bdJshMvA-XSaYebo_HHbMRpeNir_5rT8Yg_CN9glmftMtEPpYu2uLqRmVjq-WwMtaTFuMPe1q6-ej0G_qML36hS7Al5CT-leUhgBafGITBHSeP2wZxijVlHIwDFs8WuZEsyfvm6M11xoH57NsOWNLuD4U2dDsGibSazml2Z-4Kyh1ZkBnTKlWKe8ZH8R955ZXcRXiIoi2_-BNSKWn8Y-onxpo6p34T0Vp5HgwHOkkqzdcBSq4CPlE2D-fSEkQEreWnB5Jo6TC_o3FsbTnHOXdWTio7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=byhvN80AXat9F-oeDihn8i7s6sREwH_GpZFkVkA8jf0dB6rtI8Y1zR2PQZECSFv9Jjz074viGqdJRHH4uVJztl3zDmkWhLvBP7KEVICAeNr0EdPNrObqKmGkWMqjMwD6RF2Z-z5GL8PqFHX0dYIYYO8TL5sgCScsQ6f39mmKdWDQ1hfvqP6cw0aIN5uRGcB6MGS5c-ptpxquuFCArwqWwQdOSq9q5LqV0qxf2IK9TWvywdqr-Z6ED87ym4IYEHotRMUKWxkL8bVOefDHdTLHYrSFbRVoeNvCqEmDdFNf85DbrYT9aM8jAyFP_rDZ3fo6U51I8ZLpbuaK3Jdfzj_bOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=byhvN80AXat9F-oeDihn8i7s6sREwH_GpZFkVkA8jf0dB6rtI8Y1zR2PQZECSFv9Jjz074viGqdJRHH4uVJztl3zDmkWhLvBP7KEVICAeNr0EdPNrObqKmGkWMqjMwD6RF2Z-z5GL8PqFHX0dYIYYO8TL5sgCScsQ6f39mmKdWDQ1hfvqP6cw0aIN5uRGcB6MGS5c-ptpxquuFCArwqWwQdOSq9q5LqV0qxf2IK9TWvywdqr-Z6ED87ym4IYEHotRMUKWxkL8bVOefDHdTLHYrSFbRVoeNvCqEmDdFNf85DbrYT9aM8jAyFP_rDZ3fo6U51I8ZLpbuaK3Jdfzj_bOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKBB96O42jHU173VxcOsyv2vjJWssG0xudOIKDF1Sjh2bIY3C6IHx8At1YU584JzPF_0loq6yFGFW5Npu3DzX2yrXKHEEZBtj_FqZ-vx2libS-KbKMwPC0XsJKKEB-5eBrN02K7yQ4nOjM5HvZanhBcyxU-iy_wgIZGCN5h82nSmpGrLRAL-eif3UXnngQG5XiGQG750YtYgSVD_qMYP2rjjNBcv0N9-U1l-yOpVpmGrMWq4dJ0YBskDtqWKmReYawNhClk0DZpjmitFoMYPXtbDHsPKHE2taYg9Vvm-wPj740VSQqtaZh9fsZijiknPf8OhafOuyWKDmJl1Ca6pCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFbUw5FfvVsh4YxGtD_n3uRAd8tD2qNkEY0SOL2xjojZLyLvegwNG3zi1PtXe4Yw67q7IdF25TGF3mBdXiuELzMW6IQtRi8NPaZ9l7zNZaUtJixMwcOI2_pp1XxB1wW8vugDF20zJREzVTOreOwX0d6Xju38Mk3i5JLsQHvUMTJYG7dTLdy0RFCDb19Ezh-7CiibkG93mqm1Ligo0VI8c277X650_lMDQUx4ErgFqjF0VJfh4Xk8u-EV_j_8lNpXLg640cjvODRzDjEJLyddTuZ8vXGPlpecOuvORmxwbpK2of6diXQLw4Xr5N8dO6tifdavSjP9c20Zvkx4-lKWcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5-xzFQkgUEqmNfzsBPvRZqbqZg6uDebcYPOxlXsr6XNzfqyDZ4qXk8pvkgcM0dQi21Ycc7PzMQLWnO7n_xAdd16qioUWDXLyvS_lOcAEQiVcAHv7SC-OZDjzc8TsZMfOsJMDDucr2Qdkt_949O4vTCC_K7mLEDMutSqXdHqc9KM73w-uK6zZY-N4RHCAsYmgLfPYfCCmRIVcPtrIStqq59Oi7Qbq263QwKcol5TY4L8_ZB2D2kNVg5i5vztO9JeZsA2ca6gzj9pkkj5rbq6tp5QkgXoJKgNfqpCvDnUUv-ZKi1OrwIhud77UxVYAOlT4KHOofc78XMv4e7kyCgNqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NV8rlDo9wosPJP11_LUqDPI_Jl-bb8J4IiG7aSD9DI2ooC205R7ymoHFVdJC34SRuV67ALt-cehAdzRHM2nyZi0tvM1UrQ53sThEffgrNLrwwobBiwwPstLj-lUflLyv4KtxJpUkVETLFMoyb--K7jK74ym-gR_ZMzCLEmcj3pAQL_xzgiiACrGtlXQ3MnCGKb-IRyIXRHHhXXTRDzjEMdxzY4Hszi21LFlod8tzgzpr8T9IQooIu9LuEDHZk2H5_KwxYQushFK48T3yk82m39ABEYmH8j8NZnCI-hT17XeoNqasV7kB7_bZStCZB50KBCkalAqFTt7n_lDRX5ia5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت بازسازی عکس‌های قدیمی بدون از دست دادن حس نوستالژیک
📸
Repair physical damage on this vintage photo: remove scratches, creases, stains, and tears. Restore faded colors, rebuild missing details naturally, and keep the original grain, lighting, softness, and period aesthetic. Do not modernize the photo, oversharpen it, change faces, or make it look AI-generated.
#ChatGPT
#Prompts
#AI
#PhotoEditing
#Gemini
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=n-GoghvMtVYaxJgWBFkLi_xFnvEJhrXUppOvO7DQbX2GtrBQk0eKl2r_X_BS9jUgWhBDmJWR_WLP7x4qY7ayFRvpjbH5XYECJPNkw2tTS5-_3OuWqy4yBofBryXgj2bOHJxia3tBhBWOmwxz7-CafUNtudwEH_sg6UgjDodvXXMUahQX3WV6mRorh81tu2iBhK3Ivsnh45Hb-lNjgscsWKN7kkQXv1eEOxXMue0JiHNnJCSQ1kOWAjyDkKVxH-l2xVIVOjcRhiWXBKXxKSnckyOXY_weuNacVmUgC9d7fM2llX5Zs2CFgS-jqIjhyivr8b5dHQUPS8nlwV2Enj13wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=n-GoghvMtVYaxJgWBFkLi_xFnvEJhrXUppOvO7DQbX2GtrBQk0eKl2r_X_BS9jUgWhBDmJWR_WLP7x4qY7ayFRvpjbH5XYECJPNkw2tTS5-_3OuWqy4yBofBryXgj2bOHJxia3tBhBWOmwxz7-CafUNtudwEH_sg6UgjDodvXXMUahQX3WV6mRorh81tu2iBhK3Ivsnh45Hb-lNjgscsWKN7kkQXv1eEOxXMue0JiHNnJCSQ1kOWAjyDkKVxH-l2xVIVOjcRhiWXBKXxKSnckyOXY_weuNacVmUgC9d7fM2llX5Zs2CFgS-jqIjhyivr8b5dHQUPS8nlwV2Enj13wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
ClaimCircle
با یک کلیک، خبرهای جعلی را شناسایی کنید
✨
قابلیت‌ها:
•
🔹
تشخیص خودکار متن، پست یا تصویر فقط با کشیدن دایره
•
⚡
تجزیه و تحلیل لحظه‌ای محتوا و نمایش نتیجه در همان صفحه
•
🛡️
حفظ حریم‌خصوصی: پردازش در مرورگر، بدون ارسال داده به سرورهای خارجی
•
📚
پشتیبانی از چندین منبع اعتبارسنجی برای نتایج دقیق
🔗
لینک:
https://chromewebstore.google.com/detail/claimcircle/ominadfbilailbklmclcmdbpmckckdad
#claimcircle
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToJizQ2PynRoM-e6qhCA-Ue-X6HbLCr06mx-l_oDFvhW_TOWR1VSHT7kYohx9fnyznDdVceXOjeuhp9AHqyvgsYfrLMxkE4X34equNptAMDfS_dUJscx8yUbPuxyPMiKH_1i6C2sUMwBD4ezbclU8-lxHmaPzuyq381unmvMefYQFg01a-TOVE1Pd5elsYvTvCXIj_hWylw5bK84NO902uUCP-i1m1X3Yv2py6TWtbyPLgFH-IAFeEO93VpJ3i4b4USZasbEBTNzYPUg-Cv3lrzPsTpANw0delFxo0-AOvWeAdmbXu2CqgAPwLmr_j0dI3RF_pBjC3BJV7cP5SUvew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
پخش FLAC با کیفیت lossless بدون محدودیت!
✨
قابلیت‌ها:
•
🔹
دسترسی به کاتالوگ گسترده موسیقی از تمام ژانرها
•
⚡
دانلود همزمان چندین ترک با سرعت بالا
•
🛠️
ذخیره فایل‌ها با وضوح اصلی بدون فشرده‌سازی مجدد
•
📦
پخش مستقیم بدون نیاز به سرویس‌های استریمینگ
🔗
لینک:
https://flac.music.hi.cn/
#Music
#Flac
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">📢
جدیدترین قابلیت‌های
ربات وگا
را معرفی می‌کنیم:
🔗
قابلیت AI Agnet در گروه
🔸️
ادمین باید از پنل استارت ربات در گروه به بخش تنظیمات برود و قابلیت را خاموش یا روشن کند
🔹️
با این قابلیت ربات طبق اتمسفر گپ صحبت میکند
🔮
قابلیت خودمونی بودن در گروه
🔸️
ادمین از پنل استارت ربات در گروه به بخش تنظیمات برود و قابلیت را خاموش یا روشن کند
🔹️
با این قابلیت ربات بی سانسور و صمیمی جواب می‌دهد
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
⚡️
Vega Bot
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6327" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
50GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 50 / 50
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6326" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StoUny400gCB9orob-DPBMiR5oiMORYUD7gOTYQNqq-2XucIWB2MgysAJ2IfpyTv2ZQ2pV45w6D9aBKatnjASx6mT6Vv8LSvYR6OAnv30BBGAW01Zk_QL-p3M_0iF1Sf8WjNUhriej56zBLxmL1_yzFrZDuQV317QQLmNWcFL7SVjCISh3U1uwR9ClV9Rb0psAxnDZlaQrPWFLor3tP7WhBA_CUSFnWC6j0WxaYtUzzAA0IzM5V-EJ9K75qbY9Gh1G0EeoZzbysTYCJXN4DpTaVXrEpU4Ha61Dg_4z1dzIhUdfHqQ5UjAbE1H57Gm4JPjFjzfW3GI9W_trXsgNw-Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
تولید انیمیشن کوتاه از متن + عکس فقط با یک کلیک!
🎬
✨
✨
قابلیت‌ها:
•
🔹
حفظ ثبات شخصیت در تمام صحنه‌ها
•
⚡
پیوند صحنه‌های طولانی بدون قطع
•
🛠️
دوبله چندزبانه برای مخاطبان بین‌المللی
•
📦
رابط کاربری ساده و سریع
🔗
https://aianimation.video
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6325" target="_blank">📅 17:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anLHeLeDpurvKmiMpyyPj_z0z7uXmdYBnzKrk91ZvL1b2b5gSfZEJ7wGDg_2M3iVmUpxVbXxfdGBqILyp-QfX3mwfOyjS9qPfsatZVnGha0FJJL0JYg8tiX4FW5vUCQWpz6IQs3cs0R9R_VFKDWMbI-umLgVwFMZhtungPat_CAcvNVOgugCiC7GHvhimzU9gJvF7hekAVAiCytOYSAGtTxQme_Acvd7y4EBLTLvSb9Pe127UldVgdnAIwAz0bI8cbwE_x2HZfJzezfsH3LmCG1FQNzQ8RvtaDn9vImfQgbwJa8D6WdTR8Xqiip8fqjlxLyeXIHud5CZZqMGTf0Hug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
تولید آهنگ فقط با توصیف متنی!
🎶
✨
✨
قابلیت‌ها:
•
🔹
نوشتن شعر، ملودی و تنظیم خودکار
•
⚡
ساخت موسیقی پس‌زمینه بدون حق کپی‌رایت
•
📦
خروجی با کیفیت حرفه‌ای
🔗
https://memotune.com
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6324" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaamJo9QoRJm6Ocod79p3nXTJoTWRsi2dPQRAGJta39OksEB_y_PZXzvhrwSEZIQZ6Kn-yoov73RiwPRoDp_O5VpSv21Au06QIbToDfrW1fvdGivLN41Dzja0WDOw3RB9SJ5hL6rI3jGfkZogln8COvBqqxwndL5x0NTH7l_E-eO0erYXhAnygh6yTzO9XG5s2NxyyGG7s9-qlaId3yO6t17rUUT_4s2rt9cuwiV3GZFdqGEYAL1MuEp8alpVPtDwrmCQh4t1Bo-hZHQkfpvNNzp5BPqcynQMwUdnqHKc2EvfLnUNjdTMOqPlVDxVhz6ks6K4XTHwtqqp4de1bD1Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ویرایش تصویر آنلاین با هوش مصنوعی، بدون واترمارک و بدون نیاز به دانش طراحی!
🎨
🖼️
✨
قابلیت‌ها:
•
🔹
انتقال سبک و رنگ‌آمیزی عکس‌های قدیمی
•
⚡
برش تصویر و حذف پس‌زمینه با یک کلیک
•
🛠️
افزایش کیفیت و ویرایش دسته‌ای سریع
•
📦
خروجی با کیفیت بالا در مرورگر
🔗
https://stylizeimage.com
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6323" target="_blank">📅 16:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=kdXV81rzgyMb3bDY6wHhMZ1m-yjMQaw-Z_FmD43qWKNUC4pzM7TpoZm6wd5KhtaPQCZw176hZ1_4q3sDiZH9tRNdgn4carYIfZ44faWlLrEjXLbKjQR6ytFQEQU_8vDLXV-u2MHv1oMbM5ccGpT2QX5ZjetXvzax1mtks1IKZucY5o6NXaZnW2lLUthJmwvY0m4E8bFrvWSvkzOVsDJ8MQv5YvsBOdxcQHnIov7ymNuYATI2os3ObSCnPmaZz4tK7bSAK5MM2kZ2obvQcAGW7Uxtfl91xKgry92_FgPdh6Oaox6vCuT38soV0tp3SvGtT_5fXcUpRYOmNyIr-tBZ6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=kdXV81rzgyMb3bDY6wHhMZ1m-yjMQaw-Z_FmD43qWKNUC4pzM7TpoZm6wd5KhtaPQCZw176hZ1_4q3sDiZH9tRNdgn4carYIfZ44faWlLrEjXLbKjQR6ytFQEQU_8vDLXV-u2MHv1oMbM5ccGpT2QX5ZjetXvzax1mtks1IKZucY5o6NXaZnW2lLUthJmwvY0m4E8bFrvWSvkzOVsDJ8MQv5YvsBOdxcQHnIov7ymNuYATI2os3ObSCnPmaZz4tK7bSAK5MM2kZ2obvQcAGW7Uxtfl91xKgry92_FgPdh6Oaox6vCuT38soV0tp3SvGtT_5fXcUpRYOmNyIr-tBZ6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
افزونه GlifAI، سبک هر تصویر را با یک کلیک کپی می‌کند!
🎨
🖱️
✨
قابلیت‌ها:
•
🔹
کلیک راست → “Glif it” → دریافت نسخه‌ای با سبک مشابه
•
⚡
بازتولید هوش مصنوعی سبک نقاشی، عکس یا صحنه فیلم
•
🛠️
حفظ جزئیات قابل تشخیص در خروجی
•
📦
کاملاً رایگان
🔗
https://chrome.google.com/webstore/detail/glif-style-hunter/abfbooehhdjcgmbmcpkcebcmpfnlingo
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6322" target="_blank">📅 15:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7RQHYhIs5x3-tsIAJerKcypEk6alsw9FrSmHXXUmgy4PwyA9gLWNTGs19_0HmR-fr7uciVKG0PyZVaDgICTv-J2A0HS9ubHt26j48iIDCUyZzeaF77q_ymdjQyOTk1YFVOkZ3SV6yO-zxbO13mNm2i1-g2VH5ubIKXaU72JSM81I9KxoIqax_3el-CXlt8RMVhNoymiVHb6tYHBAAPUScQwT4DOU1tgxC6kgrgkGbbraNLFn9DG_urnA5puOi3pBVvus4BQLw4k0TRowybGeNDDxnQxk8HPqkx2DkBkDsQuktKZTY8QofGVy5OvgjlrS5tIsmooM4pddHk59L8A2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bPdCz0njchjHCnDm-SGnFudIxgwqVWmTCXw_N63yAiSxcV1q3uxbDo4V6-LFOnVev5WOFhiXAj2R5CVoAci4Ws2CabzgBlx5m0VExgFIuo3ljXUcxw0nI986pC8JgJsqOumHvDtj7JOwnZkz8F9v1OAD92LAAimvZ6Qdm8-jfbifT_9t_hcRDWJBhQdRGEh_h5UHLI9RCuB6T7u6wmgIfFEY50k2OERQsMEX23TktGvYmCjQl9Ohb94hXBfqKUCKfGx4Zls_X5KrqChHmaslX-zPbEgav7Krvo0-5ZLJURM490s6RJmVUaE5jVaEfRCZ40jxgzKzHJi_20VI64IgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dYml8RZ2dmgqM28gYfbV2wGwpR9OtGargG7SkChoCj1GS8rqznG6K8HwoAHEYWq_Abelqm-1hf_HMMxv-lJjxOxhrHpY_a5t6KutepJVMbRk-3cGjSNDRNcd5wbBvS6r9NzPCOWFg4zNs4tKAE7zebxkPnsH0j0X7K-BvN_KC_IvzLFAj0ij_cpyUqK3SrG_zWDRLzBt7hIhxJyZP302PQDRxMbsAnt_k2F0BUTdCjhvxUNChDtbIlrr7W1b4KhY2eU08zb0B9kpXwWch-fZCbppOGPReAjf6plxpvYaQeClpFp5e7RMes10Hrey5fxfIfzFjWRppC3plO6jWQG9sw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6319" target="_blank">📅 13:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد
شرکت Anthropic به‌تازگی مدل جدید
Claude Fable 5
را معرفی کرده؛ اولین مدل عمومی از کلاس جدید
Mythos
که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:
• عملکرد بسیار قوی در برنامه‌نویسی، تحلیل، تحقیق و اتوماسیون
• توانایی مدیریت پروژه‌های چندمرحله‌ای و بلندمدت
• پشتیبانی از وظایف پیچیده مهندسی نرم‌افزار و مهاجرت کدهای بزرگ
• استفاده از مکانیزم‌های ایمنی ویژه برای حوزه‌های حساس مانند امنیت سایبری و زیست‌شناسی
📌
طبق اعلام Anthropic، مدل Fable 5 تا 22 ژوئن در برخی پلن‌های اشتراکی در دسترس است و پس از آن استفاده از آن نیازمند اعتبار مصرفی خواهد بود.
این مدل به‌عنوان قدرتمندترین مدل عمومی Anthropic معرفی شده و تمرکز ویژه‌ای روی وظایف طولانی، استدلال پیشرفته و توسعه نرم‌افزار دارد.
با لینک زیر ۵ دلار اعتبار
🎁
نیاز به شماره مجازی
⚠️
(ایران رو چک نکردم ببینم داره یا نه
😂
)
🔗
https://v0.app/ref/94OS6T
🔵
@ArchiveTell
| Bachelor
⚡️
#Anthropic
#ClaudeFable5
#AI
#ArtificialIntelligence
#ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6318" target="_blank">📅 13:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها رو یک جا در اختیار کاربر میده و دیگه لازم نیست درگیر دردسرهای مختلف بشید
🛠️
✨
✅
این بات به شبکه‌های ورزشی محدود نمیشه و حدود ۶۰ هزار شبکه فیلم،سریال،اخبار  و.. را نیز پشتیبانی می‌کنه
آیدی بات:
@Bear_Tvbot
🐻
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6317" target="_blank">📅 12:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYSkcU0MID5FssX8ZbHdMTPeqMcQIjVXB7tgdVlI5_8KiHmPdudYvNq4fUZ6mTLN-GPZqOKtcr9cPtvL1cTO0P8Z5z3MYashSRoAsD_86aQjkfqAWZxWbrHFj5lT6yLazdrx7-N72RP-j5kZxPkQO_znapI6_bOMNAnMsOkfv0C0qo0nDGqvixsymKkamvjEY_8SyXfOUt1QPtByIJj45EkkKdSmnLhmT19fwbqVKE75PoBB4EHb_sXh6OQuhMtNA5diQsei1yJAiTH-F6wcYXk9161bUHu023QFlK5LvHKzcLLtYgdW86lhKDMHRjPqfAh_q1u9dCAzh6UwpRoOew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مدل‌های پیشرفته‌ AI به‌صورت رایگان در Notion!
•
🔹
Claude Opus 4.8
•
⚡
Gemini 3.1 Pro
•
🛠️
GPT‑5.5
•
📦
DeepSeek V4
🔗
لینک:
https://app.notion.com/
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6316" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/shUpZNdj-oKEwE8DW9hCchYjuqKThYFXbIqmSU7j2iK46JocCOBp9uR1kcQDF_KYQOjZ_aEe_JGFYnZS7t1G6CcD2PBigw8l9w3ufa9wlZwXf9di1UsRZRwnEAC3GBH-OYZ2qi963Dfayh-s8P_632F5Tiw3r6lL4NMSYYD9cIldvgQaAswYuhMBt4A93ul_1u-F5vzgw6bqE81CkuXuL8D9aGoKoBFHf5g61B0rvY-vsYwJ8Jx1k_IwwSAkBvkcbrLZGTFAqEAI1yp6vYPSHWOr9HYRlDuUX7hyBSgRIfcjZvLI_ktuSZafUjcizta6QINp_gGuqypGLIG0CG217w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXoLs7vu0AvtkOKeKw9oiG1QxSkgAF66EdFghCxySRpXP_1ta8AXt7WbiWAEx1VWMJJBvID06BfaeXC_ouaebdfrqh7BerYmpNelgb066SnVkAVWW8_0912nwnfvPg3bcqL59WO_ReRir7iXwDLeTWo4QKz947QF2OV8AvpS94EYSeVKTovtYKJy8Mu_0lwY5UY5xfpDN1a6MDr6o7ygvKUip50XooDfWK60Gi-qmxbimvPMChBr4vTPaUHvD5hAxhJ1RoJmib2_GSX_CvlpwSU4fRPQyg4ch_M9ibaZOkPCWBJwoLXAMzhwa6RIAdkerjamlC2ad7HokHoXEiWikQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=kJXlkYMSD3-fvSdyYe0ANgz2i2JkOeQc5WWkRqhziLF1nwqLkQ2fpC1AmQ2iw7BUAxgdZAuT-QKLluhLxEGCzQ1j6h64XlPrCEzzMN6Wqt2g8YmyDy8RE729lD63pmkBURUBJCTfVAUu1B6qdcQhZg3Bq4PD9SWoPYelHoTgr_r7drwoIxhSSePmyJfMCyO47iUwJZAPCynAfnOT05eO5iD1LrpbDfKjAoHTsdOujCo75DTbSu5zWLL3lEAdnij8aqbofXv2lgkiaKzXBJVF1mu4kwOcuymGh-w2QOFffJ5lgs1eDGroo6kHoFKIHRh9ZCExvmVNtdAyw4SHcSkCag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=kJXlkYMSD3-fvSdyYe0ANgz2i2JkOeQc5WWkRqhziLF1nwqLkQ2fpC1AmQ2iw7BUAxgdZAuT-QKLluhLxEGCzQ1j6h64XlPrCEzzMN6Wqt2g8YmyDy8RE729lD63pmkBURUBJCTfVAUu1B6qdcQhZg3Bq4PD9SWoPYelHoTgr_r7drwoIxhSSePmyJfMCyO47iUwJZAPCynAfnOT05eO5iD1LrpbDfKjAoHTsdOujCo75DTbSu5zWLL3lEAdnij8aqbofXv2lgkiaKzXBJVF1mu4kwOcuymGh-w2QOFffJ5lgs1eDGroo6kHoFKIHRh9ZCExvmVNtdAyw4SHcSkCag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تلگرام به‌روزرسانی شد: پشتیبانی کامل از Markdown و امکانات جدید
✨
قابلیت‌ها:
•
📱
دسترسی در تمام ساعت‌های اندرویدی
•
📝
قالب‌بندی نامحدود برای ربات‌ها (حداکثر ۳۲۷۶۸ کاراکتر)
•
🤖
ربات‌های هوش مصنوعی می‌توانند درخواست‌های عضویت در گروه‌ها را پردازش کنند
•
📊
امکان افزودن لینک به گزینه‌های نظرسنجی
•
🌐
باز کردن سریع لینک‌ها در مرورگر پیش‌فرض
#Telegram
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6311" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3ztz9nnkvZtGCk8NvtJEi1iKgy25y5szGmjZz9kkx4jWUxQD-YbovmuoWtFyFwEGqTlxvUnPK0pK_R5_2pm7726iHDyFToeE7yKE8tIYKNuQEySJJz-TXI6oNrusBycgaREPLoZ8zj3Wr6hxPqPkelC_Qd0X9cy4y5zLWdLAffv8ZcmTV-OvFxA87Ck9RDIE81PZDb68TmPkOWQYu5gf-WcGYae__0DbuZNfv5uQn1ZP6Pr6GhNb1Lbux1XAyzCVXS_Ol92qH9HbXJQcEE4oB_v0m0d6x0x1FCYZWAV3YVefB7cYYBzx7s8xDeEtZi72IHdDirHuzi6RivfC1VrkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
MemeDepot
کتابخانه‌ای بزرگ از میم‌ها و گیف‌ها برای استفاده در شبکه‌های اجتماعی
✨
قابلیت‌ها:
•
🔹
جستجوی پیشرفته بر پایه دسته‌بندی و محبوبیت
•
⚡
فید و برچسب‌های خودکار برای میم‌های روز
•
🛠️
دانلود بدون واترمارک و ثبت‌نام
•
📦
به‌روزرسانی مداوم محتوا
🔗
لینک:
https://memedepot.com/
#Meme
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6310" target="_blank">📅 11:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔥
دامنه رایگان 1 ساله!
اگه دنبال یه دامنه رایگان هستی، از سایت زیر می‌تونی کاملاً رایگان برای 1 سال دامنه بگیری:
https://domain.stackryze.com/
✅
قابل اضافه کردن به Cloudflare
✅
امکان ست کردن نیم‌سرور دلخواه
✅
مناسب سایت، پنل و انواع پروژه‌ها
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6308" target="_blank">📅 02:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I45HRpNyItx4y-RVRnXBrpuJC79Ch8lBRbQfQm0XNtamihbmZFGeoiaQcW4OUDOF5YXbQWwcVPZ4Qj8Wr6DF53uSte72AeuPOC0RzBMW9sUl7fwCOzV0S6R624zdrrCwyek4_3OpV-UuLTVOokePeXucNskOd6YltOWu3MonsxyVDwymOzNfKntAoxVClIVXvcwZUAcYha6Bx8W_0M62gsBkQ93ATO2BNXzxTMEKRbBcWbFqYbGiFhnIOKWWrNSkO4s_iPx1ZKMgiWI4q0oBrzs_ez9uoxNqQFZv6qE8N1ZxD_XE2nhtiHfqVPFvhKy-TyloP45PYiPozT7cQNu4-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕵️‍♂️
CloakBrowser | مرورگر ضد شناسایی برای اتوماسیون
مرورگر
CloakBrowser
یک مرورگر مبتنی بر Chromium است که برای کاهش شناسایی ابزارهای اتوماسیون طراحی شده و تلاش می‌کند وب‌سایت‌ها آن را مانند یک کاربر عادی تشخیص دهند.
✨
ویژگی‌ها:
• مبتنی بر Chromium با تغییرات در سطح کد منبع
• سازگار با Playwright و Puppeteer
• قابلیت اجرا روی سیستم محلی، Docker و سرور
• مناسب برای تست، اسکرپینگ و اتوماسیون وب
• کاهش احتمال شناسایی توسط سیستم‌های ضدربات
⚠️
توجه:
هیچ ابزاری تضمین نمی‌کند که همیشه از تمام مکانیزم‌های ضدبات عبور کند. استفاده از چنین پروژه‌هایی باید مطابق قوانین، شرایط استفاده سرویس‌ها و ملاحظات اخلاقی انجام شود.
🔗
GitHub: CloakBrowser
#OpenSource
#Chromium
#Playwright
#Puppeteer
#Automation
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6307" target="_blank">📅 01:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):  Aistudio.google.com  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6306" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مرحله یک طهلیل من به واقعیت پیوست
😝</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6305" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uK8R2SkXPnpkmJxEKULu1V4xV_Q3z1D55yxQ_aTd1WeqJ3H0GdpTQuhrHx76B-34w3kY7ZbzWAZErrRPWqWOFN9vQZdR0vKNoNO_GkO2Ef5LynzjGRrihKdj09qNhJELtk1xBQn5UX7vXJluEKGWYTWywnUqMfQubItWD_eEetH054ZycMsM3z06xt7kBt3DOg_mc_0II5gQNu0WL9Lm1ON__Bgv6ITlqCUIgmHkPlPBoWRgDRutttddXIUVrLWPloCWbupbKhfmMCYKgcSdIl7vfisWiJZ1cXKyIh2Hn_qMIkOjmwrMae1ZDusynNd73GNNB7DKT0H8OC8vEIuZ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):
Aistudio.google.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6304" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6303" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">📢
جدیدترین قابلیت‌های
ربات وگا
را معرفی می‌کنیم:
📚
حل سوالات درسی در پیوی
🔸️
در بخش سرویس های هوشمند
🔹
امکان ارسال عکس سوال
🔹
جستجو در منابع آنلاین
📝
خلاصه خودکار موضوعات گروه
🔹
هر شب ساعت 21:30 ارسال شدن خلاصه مهم‌ترین مباحث در تمامی گروه ها
🌐
بهبود سیستم جستجوی وب
🔹
نتایج بسیار دقیق‌تر و معتبرتر
🔹
دسترسی به اطلاعات به‌روز تر
📰
آخرین اخبار هوشمند
🔹
هر ۸ ساعت بروزرسانی می‌شود
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
⚡️
Vega Bot
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6302" target="_blank">📅 22:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLUiKek6uGw4YRwpoaU6nVEVMKjpVyQnMmxKgbxr3tdaFRWY0dC9YzgDzLA6YFGx6QyseFfONFXysJZILHZophj8vV5HBYAeKInjQwctzgPLFRLUQY4KNrM_T0NT4zrEWbVAYH3UuRU1plaSEEBqlaqnvLSxdVGOOvMhkgZS-d1ufxaZxt1ydMZ3-jL__FdQ8xyx0FnPnV1-22cMHoDblBL4QX-ddBGrztFEXq5o9woOYDgf6Harjz1PGtjbAppAxtA2E52r5VdYvPuFAWr5ukYsivmQ0ZFeEvZ-WjdzU44hBuO2ereZZo-Iny0EEz0-MDq-Us1i-XaRcQJ46or-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
OpenAI برای برخی کاربران API Credits رایگان ارائه می‌کند
اگر از APIهای OpenAI استفاده می‌کنید، می‌توانید با فعال کردن اشتراک‌گذاری داده‌ها برای بهبود مدل‌ها، به سهمیه و اعتبار رایگان دسترسی پیدا کنید.
📌
مزایا:
• سهمیه روزانه برای GPT-5.5 و مدل‌های Mini
• اعتبار رایگان API برای حساب‌های واجد شرایط
• دسترسی مقرون‌به‌صرفه‌تر به مدل‌های هوش مصنوعی
⚠️
توجه:
با فعال‌سازی این گزینه، بخشی از داده‌های ارسالی شما ممکن است برای آموزش و بهبود مدل‌ها استفاده شود. برای پروژه‌های حساس یا حاوی اطلاعات محرمانه، قبل از فعال‌سازی شرایط را به‌دقت بررسی کنید.
مسیر فعال‌سازی:
OpenAI Platform → Data Controls → Sharing
#OpenAI
#API
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6299" target="_blank">📅 22:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/6298" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=Wa6NdIJ_DVhvXC1K5YXINxTo5vwv_bN3bCc42UAAcDY_cIeO8nKq5NcWiw6Yp9H6xm0Zt7ugNvQTzUeoDuA3YEJfxRV4Ysp3USm5Qaq50JprzqZOVi4RfpzAWdu7z81q4IzJ6TfiPIQxBWzMULCLxQtjwrAEcqEQYqT7F-_vCFO066TcU-ecTLbqqd-WU6JhNTDh0VJUi2fqQnaD3bEjXkyfeNMXKu6z4p5BP-OgfSn2rfiRl8sPoOjDh8g9luuX6DojVKeZEE2MdiAHih2PjXSZOq-CdhbAKQcbA7ztI9I5505YPVhHHCFDDY5yw9UtQWtwJl2QYSjuf9YjEUWPiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=Wa6NdIJ_DVhvXC1K5YXINxTo5vwv_bN3bCc42UAAcDY_cIeO8nKq5NcWiw6Yp9H6xm0Zt7ugNvQTzUeoDuA3YEJfxRV4Ysp3USm5Qaq50JprzqZOVi4RfpzAWdu7z81q4IzJ6TfiPIQxBWzMULCLxQtjwrAEcqEQYqT7F-_vCFO066TcU-ecTLbqqd-WU6JhNTDh0VJUi2fqQnaD3bEjXkyfeNMXKu6z4p5BP-OgfSn2rfiRl8sPoOjDh8g9luuX6DojVKeZEE2MdiAHih2PjXSZOq-CdhbAKQcbA7ztI9I5505YPVhHHCFDDY5yw9UtQWtwJl2QYSjuf9YjEUWPiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم ملی ۱۹۷۸ ایران، فقط یک تیم فوتبال نبود؛ نماد غرور، اتحاد و جسارت یک ملت بود نسلی که برای اولین‌بار نام ایران را در جام جهانی طنین‌انداز کرد و نشان داد که می‌توان در برابر بزرگان ایستاد.
از ملبورن تا آرژانتین، از صعود تاریخی تا تساوی مقابل اسکاتلند، این تیم برای همیشه در قلب تاریخ فوتبال ایران جاودانه شد
❤️
یادگاری از دورانی که فوتبال، فراتر از بازی بود، یک رؤیای ملی
✨
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6297" target="_blank">📅 20:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKbI1jEBggghLhfIWJr5jYs_KJEVUBx2q8KGQVTRKTsFDfsTsUonE9oJqsHN15zM_ZdQFRXUlJNe-W6iWyBZDhmcDyjcKeUsvBgSb8pT4TM5gtHMMRWbCon7HFVcI0-h9CBNIbN31xlXGKcUH9H54Og24yTVw5tFKq9gWDpbOQ1psgM8ULHD_xrVBxSIyzJLmveLgfMUDYN7Zv3DvX2Dn2n31lCv0pHdgl5C4kZRau5g-X10jflTLkDVejcItefAjeIoz2SPwN0wJVt3O5yek0f4jyLJK5haGWdZJeLsTFhXdhAtABZhJAYuvf_MCNilU9TsAybgK6ZI3XeK-QnC2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
RuView
با استفاده از سیگنال‌های وای فای، بدون دوربین یا حسگر، موقعیت و علائم حیاتی افراد را حتی پشت دیوارها تشخیص می‌دهد!
✨
قابلیت‌ها:
•
🔹
ردیابی ۱۷ نقطه از بدن انسان
•
⚡
خواندن تنفس (۶‑۳۰ نفس/دقیقه)
•
🛠️
اندازه‌گیری ضربان قلب از راه دور (۴۰‑۱۲۰ bpm)
•
📦
دیدن افراد تا ۵ متر پشت موانع و ردیابی همزمان چند نفر
🔗
لینک:
https://github.com/ruvnet/RuView
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6296" target="_blank">📅 19:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اگه میخواید به سرورتون وصل بشید ولی مشکل وی پی ان و این چیزا دارید و روی cmd و ترمینال و این چیزا وی پی ان سیستمتون کار نمیکنه میتونید از ssh آنلاین تو خود گوگل کروم استفاده کنید.
https://webssh.webhorizon.net/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6295" target="_blank">📅 19:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🌐
Javid Mask | ابزار افزایش حریم خصوصی برای کاربران استارلینک
اگر از استارلینک استفاده می‌کنید و به دنبال راهی برای مدیریت بهتر ترافیک شبکه، فیلتر کردن دامنه‌های ناخواسته و افزایش حریم خصوصی هستید، پروژه متن‌باز
Javid Mask
می‌تواند گزینه جالبی باشد.
✨
امکانات اصلی:
• محافظت از حریم خصوصی و کاهش نشت اطلاعات شبکه
• فیلتر کردن دامنه‌ها و وب‌سایت‌های ناخواسته
• راه‌اندازی ساده روی سیستم‌های لینوکسی
• پشتیبانی از Raspberry Pi (از جمله Raspberry Pi 5)
• دریافت به‌روزرسانی‌های جدید از طریق پروژه متن‌باز
📋
پیش‌نیازها:
• سیستم‌عامل Linux
• حداقل ۵۱۲ مگابایت رم
• حدود ۱۰۰ مگابایت فضای خالی
⚙️
راه‌اندازی:
1️⃣
سورس پروژه را دریافت کنید:
git clone https://github.com/rowdy-ff/javid-mask.git
cd javid-mask
2️⃣
فایل‌ها را بررسی و دستورات نصب موجود در پروژه را اجرا کنید.
3️⃣
پس از نصب، تنظیمات موردنیاز را اعمال کرده و دامنه‌های دلخواه خود را برای فیلتر یا مدیریت شبکه مشخص کنید.
💡
این پروژه بیشتر برای کاربران استارلینک در ایران طراحی شده و هدف آن بهبود کنترل شبکه و افزایش حریم خصوصی است.
⭐
متن‌باز و رایگان
🔗
GitHub: rowdy-ff/javid-mask
#Starlink
#Privacy
#Linux
#OpenSource
#ArchiveTell
⚠️
قبل از پیاده سازی و نصب، لطفا کد منبع رو بررسی کنید.
چنل ما هیچ تعهدی در قبال این پروژه ندارد.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6293" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YH-yGyWzTBaaFaYXBQwTLiwfFYQ89Ozq_nRJZklBqBavu4OHziakAiu5uIM1U8Goioiv51LWVWVIiHy3V_PGS33O0uTtF2TLHZdYXNYa9-cbxM_Gjp7RcMt1QrF6ty_DJH1Zr3xDC7IQ8GpGjK5tVzEyzlnXLEUYWYLTcXVJbZAYxyDxDPiC4fNAcCGUdzUtlbMWUtmerxjlqvwTgtUSbnA-Vc0XYA3EgbFRdMJ9mE0qXjJO7dKIMFqj3B8Cg869ZxH9IeEWVDNQzOT4TDnMRz0tR9Wkxgg5t3CLeBxR8nLWayl-NsfuMgnFj4DxLXKIBJi5Q-v9Y3Fp_6RNDgvkmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j4vtI1lUdr4GBg7ulIBjN_VXHiHuRi3uahObck-I1FKTTAj03lvstvn7265dMUd4l_Py0v6r3MF1hVAWioG3KvUMFBv5lTUP2VpuAjWikd9Wql8J4BK-dkf5I86t5O2EP-ip-yxQ5TrAyQvWibXskhi9PimZQnYqZHBeLd2Z8eGyfpO8bvFEBzeS-VEfqBcpOXK14X4FCtbAd1jANNwWRfZBGdauZV-R6XXL4nxXT4RMk1i3oWiimUJrxMhibwVuXNReG1Z6b_xFYy4LwWQuwqYXG6c5UlBpQN5zseliaw7hQ5bI4lal-I1hvYRQbbq3o8OTi_JFSgWeJN1nhywxQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slZztEYECU2FK9BxyxjQPBUKX3qpIbi06BwLdbt2nT44aXoqIccwaJNMld8vjI27jNQ2YblycRZXLTz6o7oXL7c4lCNpTA6CYT-2wV8BPZbQCCfwUJR-CMc5S0SzbscTf5G7uW01BD1cubCJKVR4joRIvzR0Q7q4JosWHn3a8mEZzl6FAMTqBWYlebuzebP-dAvz7TS1VtDkknMcBMt-VqQXXICHNzR8BU_lhHV21XS0mwUulhelxn3-FoogJpJMRVdj6oq_nWHtyy8WS2dKI3eADfp15iDPfgewd82juq-m0JgQq0W_f5JkpMBSlISGeEKpip-H9D-Rw1ENoKyGMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
شیائومی MiMo Code: مدل جدید هوش مصنوعی برای برنامه‌نویسان، با هدف پیشی گرفتن از Claude Code.
✨
قابلیت‌ها:
•
🔹
کار با پروژه‌های میلیون‌ها خط کد بدون محدودیت
•
⚡
پردازش مخازن بزرگ بدون از دست دادن داده‌ها
•
🛠️
آموزش مجدد مدل در حین کار روی پروژه
•
📦
تمام این‌ها به‌صورت رایگان و متن‌باز
🔗
لینک:
https://mimo.xiaomi.com/coder
#OpenSource
#Xiaomi
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6290" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54834411b8.mp4?token=argjy0wALuw671UOSJJGqBAK2SWFhetLyw7bez5EfKG9B3tjlYShFhJ9iB35s_Gs_Prsy9LFtR1OY2_h7d_-gF9x7cjrfbjMpiger8bWNeUMGPLDySi-7zhveCMQuNUhs2qXFwgNTSU4e5JsSy-rccDiIES4ARxDU-_zDDFBmZL8OxNNIzFZ-eGG5awQuz1eFE9BFNxwJbab0ob2Sbyr2gTtqaF_E75mum6jJpCo9Yr4D-PJitb22-tpz60Z218vjxliywu3m2aKC-OCC2J192922rNgoZF65Dm_BKpISXpUsN_q78mYMkrf8Vxl32L_E6jQaT0W-Cf2_oeEoQOXRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54834411b8.mp4?token=argjy0wALuw671UOSJJGqBAK2SWFhetLyw7bez5EfKG9B3tjlYShFhJ9iB35s_Gs_Prsy9LFtR1OY2_h7d_-gF9x7cjrfbjMpiger8bWNeUMGPLDySi-7zhveCMQuNUhs2qXFwgNTSU4e5JsSy-rccDiIES4ARxDU-_zDDFBmZL8OxNNIzFZ-eGG5awQuz1eFE9BFNxwJbab0ob2Sbyr2gTtqaF_E75mum6jJpCo9Yr4D-PJitb22-tpz60Z218vjxliywu3m2aKC-OCC2J192922rNgoZF65Dm_BKpISXpUsN_q78mYMkrf8Vxl32L_E6jQaT0W-Cf2_oeEoQOXRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
Every‑PDF
ویرایشگر رایگان PDF با پردازش محلی و بدون ارسال به فضای ابری
✨
قابلیت‌ها:
•
🔹
افزودن متن، امضا، تصویر و واترمارک
•
⚡
تقسیم، ادغام و تغییر ترتیب صفحات
•
🛠️
رمزگذاری
•
📦
کار با فایل‌های بزرگ به‌سرعت
🔗
لینک:
https://github.com/DDULDDUCK/every-pdf
#OpenSource
#PDF
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6289" target="_blank">📅 16:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">📊
خلاصه یک سال فعالیت گیت‌هاب در چند ثانیه!
توسعه‌دهنده‌ای با نام
PankajKumardev
ابزار جالبی به نام
GitStory
ساخته که فعالیت‌های سالانه کاربران GitHub را به شکل کارت‌های آماری و قابل اشتراک‌گذاری نمایش می‌دهد.
🔹
کافی است نام کاربری GitHub را وارد کنید.
🔹
سرویس اطلاعات عمومی پروفایل را جمع‌آوری می‌کند.
🔹
سپس آمارهایی مثل تعداد کامیت‌ها، ریپازیتوری‌ها، مشارکت‌ها و فعالیت‌های سالانه را در قالب کارت‌های گرافیکی نمایش می‌دهد.
﻿
💡
اگر توسعه‌دهنده هستید یا می‌خواهید نگاهی سریع به عملکرد یک سال گذشته خود در گیت‌هاب داشته باشید، GitStory ابزار جالبی برای بررسی و اشتراک‌گذاری دستاوردهایتان است.
https://github.com/pankajkumardev/gitstory-2025
#GitHub
#Developers
#OpenSource
#Tools
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6288" target="_blank">📅 14:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚀
دریافت ۲۵۰ دلار کریدیت رایگان برای API
اگر دنبال دسترسی رایگان به مدل‌های زیر هستید، می‌تونید با Agent Router API Key اختصاصی بگیرید
👇
🖋️
Claude Opus 4.6
🧠
Deepseek v4 pro
⚡
GLM 5.1
📌
مراحل فعال‌سازی:
1⃣
وارد سایت
Agent Router
شوید
2️⃣
اگر سایت به زبان چینی بود، از بالا سمت راست
🔝
زبان را به English تغییر دهید
🇺🇸
3️⃣
روی Sign up بزنید و با حساب GitHub وارد شوید
🐱
4️⃣
وارد بخش API KEYS شوید
🔑
5️⃣
یک API Key جدید بسازید
➕
6️⃣
طبق راهنمای این سایت، از کلید ساخته‌شده برای اتصال API استفاده کنید
⚙️
💡
با این API می‌توانید:
🤖
ربات تلگرام بسازید
🌐
وب‌سایت طراحی کنید
⚡
ابزارهای اتوماسیون ایجاد کنید
💻
پروژه‌های هوش مصنوعی توسعه دهید
🔥
فرصت عالی برای تست مدل‌ها بدون پرداخت هزینه
💰
﻿
@Archivetell
✨</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6287" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⚡️
سیم کارت رایگان همراه اول به خاطر جام جهانی (کد تخفیف + پست رایگان)
CUPSIM26
هر کد ملی تا ۳ تا میتونه بگیره (همه رو تو یک سبد بذارید)
لینک خرید
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6286" target="_blank">📅 11:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=BtRWUBoDBFlzUzyZunVgDdmntpkrHcxGv4eTl3iFQUjp0IPfigK6MjWLekutJXNaK2phHBH8EYseoQ0Ff143qTJ5mRPaKBC7Qzlxf73aaRKqkzY6f9awYbJDAXAqcbCqJqMokmZwHs9HKDdFS64UpBbunIJVWRIvkwO6D--ywA6UVH4wurnUqVk6BlpN35quzZIUlFknkjh5M6IyX7z2ZkkIbIPEzA3Ku6bZ00kSrmNc3URAm0PaNSgFsurHccDq9k2Kauo1cgnt6f-5L6JHz8dFyEgxWn2CKMilBxJL2nqXE1AsIOyrKzfgyFRV3Ojvo4LfafP5vWeqBwNjShdi-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=BtRWUBoDBFlzUzyZunVgDdmntpkrHcxGv4eTl3iFQUjp0IPfigK6MjWLekutJXNaK2phHBH8EYseoQ0Ff143qTJ5mRPaKBC7Qzlxf73aaRKqkzY6f9awYbJDAXAqcbCqJqMokmZwHs9HKDdFS64UpBbunIJVWRIvkwO6D--ywA6UVH4wurnUqVk6BlpN35quzZIUlFknkjh5M6IyX7z2ZkkIbIPEzA3Ku6bZ00kSrmNc3URAm0PaNSgFsurHccDq9k2Kauo1cgnt6f-5L6JHz8dFyEgxWn2CKMilBxJL2nqXE1AsIOyrKzfgyFRV3Ojvo4LfafP5vWeqBwNjShdi-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
OpenAI
تا ۵۰ هزار دلار اعتبار رایگان API میده!
🎉
•
🔹
۲۵۰ هزار توکن در روز برای GPT-5.5
•
⚡️
۲.۵ میلیون توکن در روز برای مینی‌مدل‌ها
•
🛠️
تا ۱۰ میلیون توکن در روز در سطوح ۳ تا ۵
•
💥
در عوض، داده‌های شما برای آموزش مدل‌ها استفاده خواهد شد.
📦
این ویژگی برای همه فعال نمی‌شود، اما ارزش امتحان کردن دارد — وارد OpenAI Platform شوید، Data Controls را باز کنید و به بخش Sharing بروید.
🔗
لینک:
https://platform.openai.com/
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6285" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5Byg2vf_TJONIWGDTmZudtgRlC0aAgCWgVsVPz-x97muwUCpcYySlvCEMqbrMimINZwnZedBCNCph12zpKUiq4YRf5SZl1xpbyp2l6uL-reW9mGZCd0GVMxqzBzHjRKGpKASitTMMsSo1EiTKjdW0XilRvxWP0CP_yIROTPpmuyfUvhWwc-C8tAUcX0sDCuAbmfByBV_F-nvDyi0WW64PLojFTZ33gXb5IwcqVc35QJfqUlCzRNN-iF0n4597SaiU0fitlZCJzSqdKT505w_KOYDHHT9JTF_ZLm_2C7JKkP7qrOK_DIFnko90i1DatkqdqkEgbcb8tVj9IwkCXiLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
BrowseryTools
مرورگر خود را به یک جعبه‌ابزار قدرتمند تبدیل کنید! 136 ابزار رایگان برای فایل، رسانه و هوش مصنوعی، همه در سمت کلاینت.
✨
قابلیت‌ها:
•
🔹
ویرایش تصویر و ویدئو بدون نصب
•
⚡
مبدل‌های فایل سریع و آنلاین
•
🛠️
ابزارهای توسعه‌دهنده با Next.js + TypeScript
•
📦
هوش مصنوعی محلی: رونویسی، ترجمه، حذف پس‌زمینه با Transformers.js
•
🌐
متن‌باز و قابل میزبانی مستقل
🔗
لینک:
https://github.com/aghyad97/browserytools
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6284" target="_blank">📅 10:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=HaMhSpiOClXYtr4f4tmDq_hHDYDKAfjvQO7zDVFbe9KEX7U8d3-60hUZRinLf43JWIMg6s_yoP23WAg-ERJThriEVMrK06wD709CV9jemUnDWB3enJsBOzyYoBUjdgIOjz8SkYRVT3U4eaYpN6FT4T7-_mo9_jByiO20TOAG-eH2aPeIvJI-ttew9Cs-yALQVjnfl8qUad0_XqbsU0mtsXcfuj-3706W-LCosCTE4VOz23ydHLOYgYgwvkU1FLc_0AwNo-wl8F9QEoT-O3bNxNSCiefAwhzDQe-J5tMn2xwlnZuBfUdtELbPfAh9YG3y8yFTFpstsS9mV7TZbkUSXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=HaMhSpiOClXYtr4f4tmDq_hHDYDKAfjvQO7zDVFbe9KEX7U8d3-60hUZRinLf43JWIMg6s_yoP23WAg-ERJThriEVMrK06wD709CV9jemUnDWB3enJsBOzyYoBUjdgIOjz8SkYRVT3U4eaYpN6FT4T7-_mo9_jByiO20TOAG-eH2aPeIvJI-ttew9Cs-yALQVjnfl8qUad0_XqbsU0mtsXcfuj-3706W-LCosCTE4VOz23ydHLOYgYgwvkU1FLc_0AwNo-wl8F9QEoT-O3bNxNSCiefAwhzDQe-J5tMn2xwlnZuBfUdtELbPfAh9YG3y8yFTFpstsS9mV7TZbkUSXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
افزونه ImageToPrompt تصویر شما را در چند ثانیه تحلیل می‌کنه و یک پرامپت آماده برای مدل‌های تولید تصویر می‌سازه.
✨
قابلیت‌ها:
•
🔹
تشخیص سبک، اشیاء، نورپردازی و ترکیب‌بندی
•
⚡
تولید پرامپت دقیق برای Stable Diffusion، DALL‑E و …
•
🛠️
بدون نیاز به ثبت‌نام یا حساب کاربری
🔗
لینک:
https://chromewebstore.google.com/detail/ImageToPrompt/pgabcjhpgdcgbflabemecpficpknnpfn
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6283" target="_blank">📅 09:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9CPgGaWL7TM9XQgNsmx-I9BQ-ciO_rV086LeVXVK06lJ5iJ_OFBh3tvTGjVMo8cjEuzKPCZKPuxdY22yv3PixzcqMeGFew7jVaUIBTtqaa2BbV8Q59sjO6ye1sZ_CHNHmcf8fJssfdrjyqX0854PMveiKztiz24A4kDcIBUv6VCruOMm2hypJv2tW-2HDO15x3Zoj2FUidkEPDognszAmry4pJuEymZLc2hX38hJqpOWxof3wW99ZBtBk5Tb6GuDIt4O7-pKkLwn5yA-97o5vyK0TO73XoWCnEhGDhpQcy4sV_ZPE_bmmhL_3L58nOdQW1mAUEAnuiGiSySePv6RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتقال فایل سریع و پایدار بین دستگاه‌ها با قابلیت ادامه‌دادن پس از قطع
✨
قابلیت‌ها:
•
🔹
انتقال همزمان بین چند دستگاه
•
⚡
ادامه‌دادن خودکار پس از قطع ارتباط
•
🛠️
سازگاری با شبکه‌های پیچیده و متغیر
•
📦
انتقال تطبیقی برای بهینه‌سازی سرعت
🔗
https://shrimpsend.com
دانلود فایل مخصوص ویندوز ، مک و اندروید :
https://github.com/shrimpsend/shrimpsend/releases
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6282" target="_blank">📅 08:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzCq5jmBQRIIM1mx_-fE_8pbViOUVMDeVbFk7EPX_OfVFFDY-A-1qb6RE-BWc7L0jYUcLU_xtIT4pECi_ya2AgI1ZW63i9-tCg6B0DSTpuMNTDBxoiDtWou8AaZf3T2-rUR5lQWmS7ttmHxByJfCuBrt0ysm0mr0vBJeRXYMmpZcsz8j70FbZn5iJ2lTqgbkE-zuHXoQssZFFj9y2uvVsfGjcl5AFqwzWW2-AsHd1y3dXoxFnjEwMKoClkgIBV68YSb9Us22B_V1szJn2nIkSt326G673g1zXpdXflCxEM3dBmugCu_BzmHYw18goiUAmaCKkqN4TXpwAvOCH7YlkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوتاه اما جالب
❕
به این صورت داخل duckduckgo میتونین qrcode بسازید
🔗
🎁
@Archivetell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6280" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6279" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚀
راه‌اندازی خودکار 3x-ui با WhiteDNS؛ از صفر تا تحویل کانفیگ در چند دقیقه  اگر حوصله نصب دستی 3x-ui، تنظیم کلادفلر، گرفتن SSL و ساخت کانفیگ‌های Reality و VLESS رو ندارید، WhiteDNS تقریباً همه این مراحل رو به‌صورت خودکار انجام می‌ده.
📋
پیش‌نیازها  قبل از…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6278" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=PB5UsrYGC3INQp1gYUrCNeV3oPoW9L_rUgM1SuZmnrwU_3yGdzDfLpRn5v7MxZsBajrfk7tePRLJzqYIsIxuYiKtuKSrc7fhRju0rKSkpxKgF9g9XvIHtMVb79dlce9of0vrmdkojMMEYzesBwqfY0rwQRMkoG9eBDnfrwzJD_RwmSBXOKuW9RAJ9gB87ruoiOGtgULlVKMb_QAFHuyJFKiWoejzwqEtp0_UDxm1UP8RICP9UNkTewyuqXwiqHy0Dazl9nmaYw6xpPBhSjM6W-buR3_sAPhzJlHugDnS1WsIfq9yxbJAhOp_FYzKI3Zv-tQNY7XRjbkGUsD0SKVrCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=PB5UsrYGC3INQp1gYUrCNeV3oPoW9L_rUgM1SuZmnrwU_3yGdzDfLpRn5v7MxZsBajrfk7tePRLJzqYIsIxuYiKtuKSrc7fhRju0rKSkpxKgF9g9XvIHtMVb79dlce9of0vrmdkojMMEYzesBwqfY0rwQRMkoG9eBDnfrwzJD_RwmSBXOKuW9RAJ9gB87ruoiOGtgULlVKMb_QAFHuyJFKiWoejzwqEtp0_UDxm1UP8RICP9UNkTewyuqXwiqHy0Dazl9nmaYw6xpPBhSjM6W-buR3_sAPhzJlHugDnS1WsIfq9yxbJAhOp_FYzKI3Zv-tQNY7XRjbkGUsD0SKVrCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6277" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=PMFDK1caxwFqkIWIYYjGS06rsqqsHdvJrw0V1_LM0saLAUDEAjsTfgYYEkOwLUsTwI_wjrVnDd7u7sqb_pwx1pgm-DckSQgPn5N8APholx18hrXK6HPCn5wZy5sCTftvx7up8UhdRvUva20rCq0eVC7zi45lM1voRPMXEdIpg5tWz780cmNOJqmB-jZ1dlrVDzEyMAkUP_2qJxJT4tkVwB47GZBupZXfXRI3MDDB9FYd68nFZ97v9y6lxcBIL9GlksyufSfVJqDO252JHz_aYJayixdB2M07nj3POF7c9Q9W6yOdOWLWC7aCfwZIRmblbdt1xrNBnMuFxcGm8Z5q7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=PMFDK1caxwFqkIWIYYjGS06rsqqsHdvJrw0V1_LM0saLAUDEAjsTfgYYEkOwLUsTwI_wjrVnDd7u7sqb_pwx1pgm-DckSQgPn5N8APholx18hrXK6HPCn5wZy5sCTftvx7up8UhdRvUva20rCq0eVC7zi45lM1voRPMXEdIpg5tWz780cmNOJqmB-jZ1dlrVDzEyMAkUP_2qJxJT4tkVwB47GZBupZXfXRI3MDDB9FYd68nFZ97v9y6lxcBIL9GlksyufSfVJqDO252JHz_aYJayixdB2M07nj3POF7c9Q9W6yOdOWLWC7aCfwZIRmblbdt1xrNBnMuFxcGm8Z5q7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6276" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=D9pdCZe07M7Hp1gbHYi2iMUqgbSewMblDB7ALoFuG5jMKc7Mtnlh30czCNPrjbeI4Hj5hnMT1GgEwd7Zaxtu48EfwNLDKvvYC1-i749EGUEb6nr8LOnY32vZVvD30SbWoSzlBnWaCuOIpxki-Y0m04NMuuuatjWCDT_a_VpDiDT6u3quDO-1WuaLBb-uVssTyTd1ok35fLPjA_PKBK_modI_kLXtyfVSFQBayF7vtIAgZAjSDdKlwwIjWjf5hMkDOYrwkQNFXWxbio9rl24P82FRZUVXfiowGSUZKP2tkwsu6vmWjv9HOxWXMwC2mkYtdx8oaU08q9GhGt31kTVpgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=D9pdCZe07M7Hp1gbHYi2iMUqgbSewMblDB7ALoFuG5jMKc7Mtnlh30czCNPrjbeI4Hj5hnMT1GgEwd7Zaxtu48EfwNLDKvvYC1-i749EGUEb6nr8LOnY32vZVvD30SbWoSzlBnWaCuOIpxki-Y0m04NMuuuatjWCDT_a_VpDiDT6u3quDO-1WuaLBb-uVssTyTd1ok35fLPjA_PKBK_modI_kLXtyfVSFQBayF7vtIAgZAjSDdKlwwIjWjf5hMkDOYrwkQNFXWxbio9rl24P82FRZUVXfiowGSUZKP2tkwsu6vmWjv9HOxWXMwC2mkYtdx8oaU08q9GhGt31kTVpgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6275" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ادم خودشو باید برای هر سناریو اماده کنه و باید تو پیشگیری خوشبین باشه. چون شاید همون ی روش هم جواب داد</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6273" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">همین الاناس که ترامپ میاد میگه:
دقایقی قبل قرار بود دستور حمله رو صادر کنم، ولی آنها گفتند ما مذاکره میکنیم و من برای این حسن نیت آنها ۲ هفته حمله را به تعویق انداختم.
ممنون از توجه شما
دانلد جی ترامپ
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6272" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">برق قطع بشه با کبوتر میخوای پیام بزاری تو تلگرام؟ 🫪</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6271" target="_blank">📅 00:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6270" target="_blank">📅 00:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6269" target="_blank">📅 00:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6268" target="_blank">📅 00:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">📝
جنجال جدید در دنیای آفیس‌های متن‌باز
پروژه
Euro-Office
نسخه 1.0 خودش رو به‌عنوان یک جایگزین اروپایی و متن‌باز برای Microsoft Office منتشر کرده، اما این ادعا با واکنش تند تیم
LibreOffice
روبه‌رو شده است
😬
🔹
بنیاد LibreOffice می‌گوید Euro-Office خودش را «اولین مجموعه آفیس متن‌باز اروپایی» معرفی کرده، در حالی که LibreOffice سال‌هاست چنین جایگاهی دارد.
🔹
همچنین توسعه‌دهندگان LibreOffice معتقدند تمرکز Euro-Office روی سازگاری کامل با فرمت‌های مایکروسافت، عملاً آن را به یک «هم‌پیمان غیرمستقیم مایکروسافت» تبدیل کرده است.
⚡️
به نظر می‌رسد رقابت بین پروژه‌های متن‌باز برای جذب کاربران و سازمان‌های اروپایی وارد مرحله جدیدی شده است.
#OpenSource
#LibreOffice
#MicrosoftOffice
#EuroOffice
🐧
📄
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6267" target="_blank">📅 21:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzthoKSYQh5cNW_07qm-a9D-MMmd8rsARf7bGqPb61XlrPNf8HL-FemQpZM7uMWzvqK_DDWP62z2m_PS90YWv19KCnLQgCRehCyXfKB68YPSs-tO7qFHIvYFK6rtpSu8fXCPIG0Y-n4e3QcvefW27NqlUjo4lMOaM31QnowNpfVjCR6TXYLOK51pSWnXpyV9gVhPMvls7JjMSf4wlhAPGOOtr7oZM0pWffXWGb5bI-yX5mSqH1vgwfvyEf_xBzb2PCdWxd3K3cvHCfuWu6nwMCoK2VDSlnlN8tgmkinNcaJkEulVVSm3UPjeVxEaUKPx_EQx101JwQS1xlIQz7Y7EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ZOOOP: همه ابزارهای خلاقیت هوش مصنوعی در یک پلتفرم!
🎨
🤖
✨
قابلیت‌ها:
•
🔹
تولید تصویر، ویدئو و صدا با یک کلیک
•
⚡
کلون حرکتی برای انیمیشن‌های دقیق
•
🛠️
قالب‌ها و مدل‌های محبوب پیش‌ساخته
•
📦
یکپارچه‌سازی ساده و سریع
🔗
لینک:
https://zooop.ai
#OpenSource
#AI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6266" target="_blank">📅 20:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNCeL251Wz9OQdDIuC-vJFqqR-JudxIuCROkcRFMCQ7pOX_Ab9AO9eHwA85Sv4qW3-aLhh6Sh_Yg0IuwMhiCXKItTe-bg0aCzF0zPQIYMYBb0mkjRBBHG7lZcQke5Ga1dFdv4mShqGqYB3MvyU0I_sAOtLXE_h_-HD9hkIo2AXlFK1DJwG3nfZzOjouMcn0Nn993up5omS0Kjhlmi0YXK39iRKKthgCxLYoqZGTwI2nLPyFgATsly8G4_AcSw3BV8KgdHKRXn5BH1MPtB-iMIwu4F07qXFIqKehqbAPkbBHcJTCoLzUCShY3iHXK6nXqCj3jPDVXDXAbv6MKHZfr6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕵🏻‍♂️
با این ابزار می‌تونید فقط با وارد کردن یک نام کاربری، حضور احتمالی اون رو در سایت‌ها و پلتفرم‌های مختلف بررسی کنید.
✨
قابلیت‌ها:
• جست‌وجوی خودکار در صدها سایت
• بررسی شبکه‌های اجتماعی، انجمن‌ها، پلتفرم‌های بازی و سرویس‌های دیگر
• نمایش تطابق‌های پیدا شده در یک فهرست
• اجرا مستقیم داخل مرورگر، بدون نصب برنامه
• امکانات پایه رایگان
🔗
لینک:
https://whatsmynameapp.net/
#AI
#OSINT
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6265" target="_blank">📅 19:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6263">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581e875845.mp4?token=PvQTF5dyY62oXAD752BglNqdJNCUa0Bh4yuDbtme-cJbC3gFHzj5rclxyzuxRJq5DTnR0whin-admRtuKmbYZ56BPeYWaJrwRosJTuabaexcT7EwcuJD0WbEOvoFIDS5dChz_njv3ZICbDdLHAeIk1FLrXJNx_JxEUAdEtsgrC0ywHe0DA-Y9L8DA-I2HtSuNSr2ezP4McNb9Tsin1gbj9ITlLyuh9Moc4e6Ltuqby5a3yiSbiWb8UaEp-wkgMujjTvW-Vogx5Ab452RJvQD2jye6Kx4TZXIZVq0-56gbD3msrW6XiIbOi_PHAo4YOPfem1rXHeeJ6kj9Lh9mgjIQSBBcoKy7X4eeWXRnXaZ4hgPhljykgGRzqrz35CjfgIL36Pt-Rai-yxdJTIRLnJHaIcqtDQZg_xK5tWuQQ4p61qCnb7SH6Dky8tFHnzvBHmM1qMOOHnNsLSVmupEpUbuVf2tQQ_g4wfM8yJNug9ZJtQim_0bEZJjzz9qU2gjb4j3wjoWONaikmtDmlsiY7IBuppfOVfQEKJji6fRsorBWe1YiRCufuzVFDY2OFwqGrb_zkgVu04cGX8gADf2iteO-qLwvrdn25NQDJ9SUjesf1h27mAzt8gC2i28XaonUPIymOCJ-QDNNRuZA208Q1ntCbvCMG1ckR4Lkdbi6Qqfbek" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581e875845.mp4?token=PvQTF5dyY62oXAD752BglNqdJNCUa0Bh4yuDbtme-cJbC3gFHzj5rclxyzuxRJq5DTnR0whin-admRtuKmbYZ56BPeYWaJrwRosJTuabaexcT7EwcuJD0WbEOvoFIDS5dChz_njv3ZICbDdLHAeIk1FLrXJNx_JxEUAdEtsgrC0ywHe0DA-Y9L8DA-I2HtSuNSr2ezP4McNb9Tsin1gbj9ITlLyuh9Moc4e6Ltuqby5a3yiSbiWb8UaEp-wkgMujjTvW-Vogx5Ab452RJvQD2jye6Kx4TZXIZVq0-56gbD3msrW6XiIbOi_PHAo4YOPfem1rXHeeJ6kj9Lh9mgjIQSBBcoKy7X4eeWXRnXaZ4hgPhljykgGRzqrz35CjfgIL36Pt-Rai-yxdJTIRLnJHaIcqtDQZg_xK5tWuQQ4p61qCnb7SH6Dky8tFHnzvBHmM1qMOOHnNsLSVmupEpUbuVf2tQQ_g4wfM8yJNug9ZJtQim_0bEZJjzz9qU2gjb4j3wjoWONaikmtDmlsiY7IBuppfOVfQEKJji6fRsorBWe1YiRCufuzVFDY2OFwqGrb_zkgVu04cGX8gADf2iteO-qLwvrdn25NQDJ9SUjesf1h27mAzt8gC2i28XaonUPIymOCJ-QDNNRuZA208Q1ntCbvCMG1ckR4Lkdbi6Qqfbek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تست رایگان Battlefield 6 در استیم شروع شد؛ تا ۱۵ ژوئن می‌توانید این شوتر را بدون پرداخت هزینه تجربه کنید.
✨
قابلیت‌ها:
•
🔹
دسترسی رایگان محدود تا ۱۵ ژوئن
•
⚡
شامل ۵ حالت بازی مختلف
•
🛠️
تجربه ۴ نقشه چندنفره
•
🗺️
بازگشت نقشه‌های کلاسیک مثل بازار قاهره از BF3 و جاده گولماد از BF4
🔗
لینک:
https://store.steampowered.com/app/3028330/Battlefield_REDSEC/
#Battlefield
#Gaming
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6263" target="_blank">📅 18:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سیستم جدیدی به
ربات
افزوده شد.
✨
از این پس، در بخش
سرویس‌های هوشمند >> آخرین اخبار
، امکان دریافت اخبار روز ایران و جهان فراهم شده است
📰
🌍
هر دو ساعت اخبار بروزرسانی خواهد شد
✅</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6262" target="_blank">📅 18:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🦀
Asterinas 0.18 منتشر شد
پروژه Asterinas یکی از جاه‌طلبانه‌ترین پروژه‌های متن‌باز دنیای سیستم‌عامل‌هاست؛ یک جایگزین مدرن برای لینوکس که تقریباً به‌طور کامل با Rust نوشته شده و روی امنیت حافظه، کارایی بالا و سازگاری با اکوسیستم لینوکس تمرکز دارد.
در نسخه 0.18 تمرکز ویژه‌ای روی اجرای Asterinas در محیط‌های کانتینری و مجازی‌سازی بوده و قابلیت‌هایی مانند Namespaces، cgroups و بهبودهای مختلف VirtIO به آن اضافه شده‌اند.
از دیگر تغییرات مهم:
🔹
درایور جدید NVMe
🔹
بازنویسی درایور فایل‌سیستم EXT2
🔹
پشتیبانی بهتر از نرم‌افزارهای لینوکسی
🔹
اجرای برنامه‌هایی مانند Firefox، QEMU و Codex
اگرچه Asterinas هنوز فاصله زیادی تا جایگزینی کامل لینوکس دارد، اما یکی از جدی‌ترین تلاش‌ها برای ساخت یک سیستم‌عامل مدرن، امن و سازگار با لینوکس بر پایه Rust محسوب می‌شود.
#Linux
#Rust
#OpenSource
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6261" target="_blank">📅 17:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کانفیگ ناب
🔥
trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6260" target="_blank">📅 16:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGkjawmh8jE1Y0pMxCCrrV4SRCF4eLtwFVkYcZEplcprtrUDBdU1pSLmzTIvdfv3bNMK9bpwjHb2d2B4gfaFQxV_oWqDDQnxpHchE1lPVamI0z5vXlTAGKoe5mKVGoWi-j0G4X9CrlY_oreB8_-OnkzxO2K0vclkKNJSQR1mbTK0Ms4toj0qXzeepopKcC33aZN7yhSWDUcEVm2FIIgQeN6V3EeH9TVE9gQpW-dajOb4cOa41CAyV2ppjTNVlpS5UIJ9KtL-3BKpe21rVNmYlwFOTFPJGClSvTOr5c1GYwPhVhZX_iECbsYJN6YfASxEB_vNZLZ9q1PXD4O7YElIBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
یک ویرایشگر ویدیوی رایگان که مستقیم داخل مرورگر اجرا می‌شود و فایل‌هایتان را روی کامپیوتر خودتان پردازش می‌کند؛ بدون آپلود در فضای ابری.
✨
قابلیت‌ها:
•
🔹
ویرایش چندمسیره ویدیو
•
📝
انیمیشن متن برای ساخت محتوای حرفه‌ای
•
🎧
افکت‌های صوتی کاربردی
•
🎨
تصحیح رنگ و بهبود تصویر
•
📦
خروجی با کیفیت 4K
•
🌐
اجرا در Chrome و Edge بدون نصب نرم‌افزار سنگین
🔗
لینک:
https://github.com/Augani/openreel-video
#VideoEditing
#Tools
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6259" target="_blank">📅 16:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=PUAspWafN3KxWvWeRahI_1FREBS4RnH_MpN0RgH6gYnPVy_R0DjPC1lvJVpzJho3rBYTwHKPbs2i4_rxQY24NBDk9ulNcBRrIZtM46H5DOBWk5RxM7zzCmOHqTN6hM710KkNl2cITYHMNhaoC-GPIhuHh4n3FKuiRLEVnCNJccCrDonz2hlViMTIWiFGG_rdl26H-XRptMYRoPYgkKqv8exLm3RMWg_1oGbw19yMm_Jxqmmx7S399AOcVq8vJgteA_C9cwMpsdruFkgrNgo5SbupdYk73euwJONG0flVPNqzNdaZnt5jC57JSAfjvbWboUfSEFp98eokoK_Miin9boKw58cH24BZSQ_kTheT9VwGg55SaI6fChSnY2H0jw2p7kY8rYMqZJRx68aJPQVfPeVbE_XavY9qUZ0CRGUK25kqWUqVuOJsUHzzv66nLA3FRxhUfY6Cu3sitgreJkzZix8XcSSTEhsTiivAX8ny6qg6QT9mQvpUtwZeiJH4VU2Y__Ow_CauKFWcZhPRMMrc0Uaan3CfDx1naoEkkYq_ivOaXEr8Ott0SnyLsEOdmw9SBJIu3z36vcZ7Yut0ZLzbcq28m61LxqL2rzUFECjFpoZmGgxo9a0XflTSgBd2Un7ga1DqukefqycfI2ehD2K6uL-FQUEWkr0iWNcypt5FvbY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=PUAspWafN3KxWvWeRahI_1FREBS4RnH_MpN0RgH6gYnPVy_R0DjPC1lvJVpzJho3rBYTwHKPbs2i4_rxQY24NBDk9ulNcBRrIZtM46H5DOBWk5RxM7zzCmOHqTN6hM710KkNl2cITYHMNhaoC-GPIhuHh4n3FKuiRLEVnCNJccCrDonz2hlViMTIWiFGG_rdl26H-XRptMYRoPYgkKqv8exLm3RMWg_1oGbw19yMm_Jxqmmx7S399AOcVq8vJgteA_C9cwMpsdruFkgrNgo5SbupdYk73euwJONG0flVPNqzNdaZnt5jC57JSAfjvbWboUfSEFp98eokoK_Miin9boKw58cH24BZSQ_kTheT9VwGg55SaI6fChSnY2H0jw2p7kY8rYMqZJRx68aJPQVfPeVbE_XavY9qUZ0CRGUK25kqWUqVuOJsUHzzv66nLA3FRxhUfY6Cu3sitgreJkzZix8XcSSTEhsTiivAX8ny6qg6QT9mQvpUtwZeiJH4VU2Y__Ow_CauKFWcZhPRMMrc0Uaan3CfDx1naoEkkYq_ivOaXEr8Ott0SnyLsEOdmw9SBJIu3z36vcZ7Yut0ZLzbcq28m61LxqL2rzUFECjFpoZmGgxo9a0XflTSgBd2Un7ga1DqukefqycfI2ehD2K6uL-FQUEWkr0iWNcypt5FvbY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
نسخه ۳.۲ مدل Ray از Luma منتشر شد؛ اما طبق تست‌های اولیه، هنوز با رقبایی مثل Seedance فاصله قابل‌توجهی دارد.
✨
نکات مهم:
•
🔹
پشتیبانی احتمالی از خروجی HDR با فرمت EXR 16-bit
•
⚡
تولید ویدیو تا ۱۰ ثانیه
•
🛠️
ساخت ویدیو بدون صدا
•
📦
ضعف در بافت‌ها، انسجام تصویر، دینامیک حرکت و درک پرامپت
🔗
لینک:
https://lumalabs.ai/ray3-2
#AI
#VideoGeneration
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6258" target="_blank">📅 15:29 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
