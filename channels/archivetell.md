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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 22:41:20</div>
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
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 735 · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
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
کاربران دریافت کننده: 36 / 64
💾
حجم تخصیص یافته: مخزن
⏰
مدت اعتبار: مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbqTPImMueLyCxTymN9YhWF03AT7MzYUUKIqvy7L7OHzJVFguqAbEETGaAhZwo5mNw9F2KWfecSUCeNZkZ8oSlbdPDUQ4jrQZPK_ywNSmSHpjpZ_AC2A6B29cDvVKop2KpCj-P54Jb38rQBTmDNckJxERJwg5xkmu87WLrdg55CGTL3eydUBoNbGs70DP9MCQ5NDFhbED8qLz74-ibGxxPRaFElC6CYZDd7bknqigztRpM1vZwZKsA8GMxwymbkM5DKpQ-3PQ8Gp_ziAs8HVTFQiLbVLZPJuf_E-UfgucoX4Bwhfx6MJNUate1ZiSOqFlryhNqWe9NkCELsijsLZKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5E5MttT82gEWfuWLBltRURoswNrn-6SID5VKyfBdNyRNAGZxTqVUBVeUodwPrgmceJ_96rPaYyV9oVGFjbQAwK_Maek6oXu_Kq9YCdYK7pTabaTPMkjs0c7jow32IIr1nHuoH3ggSS8qhNOefDMIfCAeMHpr_wbfMWIV7J3jk8gB6Zrv2_lBLhWMZVPQH1AvZvIXbB8ST3aFO24feu-4eQEeVfvaLPjealQO3fPYP4aqqkUV9B_cTl038rusaFhUVzio3ZABJ-BB8DexpQ0fzZDpAprHpFhAMotmkQw13k9WGA8SKgYWGX1CNJ0FtUUcuNOPIQNiYaVmWrem9oGZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdQTL8wo90SExEt3Tte3BxjCbt5iybeOj2yQP_QddbH7NU_uZfyb7xf_a8aGslfFNfEx7D-zkGKtXBh1A2EwRHeagy30gWC3zdtaYWgPnWj-MNKgP4kD_GShAptIlecG2R-wWGe2Qq8BDgzqIFYQ3-DYU2g0MfIestp7b3TkH8cCK4PRMTz7v-f7e6TAvxT8AhQLDkUfvN-rkI5DhH5bS9M7n0NcgzwhTJwKbu9dCfbrwrqdWWluuzc8MJjS0Vplh71H9h244XZXS5c-m9oynO9WIdGtr_Eu_67deUFj1uMJjhma_ANgm1WhOiUFuSQtehIkNUNzdbdAWKV_LLEhYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dw01GjsP_svTyZ7bwO0cYfSKq_AYji7K84an1Ln7CQfxIGa2dOt_nNiGyuXCIEEv62C7JR1aoMRx0Y3bEHhrm5dxqXGEXc-C73yfLqTpWn2YxXT8wZ-efzWycRgR3YTofiARyr7w-azkyw5t79nV8YDRLGk-WAuNIAzj5bmPak8ezjGwsqTyMVNMR4xRU9vn2r5Dd587LYHjf0-6UvbKPpWTuhisEsWg57aO0lRgleXK_g04F5exPjdGcjymcr--ef9q71nk898nfE4k4oAQ2Ejj8rf3Q94n1b8WlXXSM1ACodvWmfAC_KhybvfOT7T93GHnfN_U1w6iM8AoYR0Tfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6FIJAbFnOxeFp49WcM2Zce4tg4LnHwg2nrbr8XQ7xfQ6X6du2MGW7hmfh5bdJshMvA-XSaYebo_HHbMRpeNir_5rT8Yg_CN9glmftMtEPpYu2uLqRmVjq-WwMtaTFuMPe1q6-ej0G_qML36hS7Al5CT-leUhgBafGITBHSeP2wZxijVlHIwDFs8WuZEsyfvm6M11xoH57NsOWNLuD4U2dDsGibSazml2Z-4Kyh1ZkBnTKlWKe8ZH8R955ZXcRXiIoi2_-BNSKWn8Y-onxpo6p34T0Vp5HgwHOkkqzdcBSq4CPlE2D-fSEkQEreWnB5Jo6TC_o3FsbTnHOXdWTio7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKBB96O42jHU173VxcOsyv2vjJWssG0xudOIKDF1Sjh2bIY3C6IHx8At1YU584JzPF_0loq6yFGFW5Npu3DzX2yrXKHEEZBtj_FqZ-vx2libS-KbKMwPC0XsJKKEB-5eBrN02K7yQ4nOjM5HvZanhBcyxU-iy_wgIZGCN5h82nSmpGrLRAL-eif3UXnngQG5XiGQG750YtYgSVD_qMYP2rjjNBcv0N9-U1l-yOpVpmGrMWq4dJ0YBskDtqWKmReYawNhClk0DZpjmitFoMYPXtbDHsPKHE2taYg9Vvm-wPj740VSQqtaZh9fsZijiknPf8OhafOuyWKDmJl1Ca6pCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6327" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6326" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6325" target="_blank">📅 17:54 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6324" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6323" target="_blank">📅 16:08 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoqDJOzHlQB770FjGAGcRoc78gM-ysH568xphqvnFS1hjyWCkwI0Wp1wDdFPFaQBdKe4IrpC70vK7lm8bSNdZoV_ZdQbqkFPhMDB3WN9wXCzkM-szbzE0WRSr_kogS3fdUxzYz1jCCqO1kGNEGCjEJWlvSnfwwhGGJWwnGrnhDv0DnGQTA1_AS0912xZGQVqJDyBXk1UOvApGPLEWjOvcZjqvwERjk4HMz3I3a1rn22zIj43pfpdiupGJzdcfQykoHBBNSLbX0i055tsqScDB6jK6eYKxjzgh4JTHV_LLe3K6uu2CPAVxruyttcPfM-9DN59VgO7wFm43ptUpC9ZHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4PydhkLTOBQ__rO9KYBxq-9OjMM4MZqxgV7QigFt7Y35YPDK92LE4WHv4ANddS1UXUGOJtSgP3R9vxyGGBsJ18-ZMjTJAmBeI4k9k-viIsgCO_ttCUqFEgCEccbP7urw1TkOj6rjFzW6T2DsliIgX4GIQir3Kdg40NQvwg8MzcyMC0qDZ_nfVoWyaZGEtlzKxExjOmVtuU48P4AHw-G4p_XNF0ixxqxlnbBBufolB5yw9w7D9Wm_CRgr-JgBxhH2l5xulBby7oVIBBcXiJvBTWMrYw8bsq5PHM6wHMQQS3Hvx-eJYZCN3Mh8zYVFGnvw9qBTg9-7etHx7LTfh8_6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IsWQ7lRsnqzZuwPcIFvZKVJ7P6e6Tkemje5OUmMYzH6gHcvyiKKe3w4p1izvcPTXjumS2Y_i-bUKqUxHVrKSkfw7W6MStKGP10E4NdAf5dtt36zF63Ak4X8bQ6ybPv67ty0CmZEV8D2RfxpE7x1u603YK2ECKflVm2RxphZWPVFZB-URJP-7OACiczDJyQWNPFXb_yRYmKoMlTxHDbIZW4O059au_WYsNHFl7GrKkW3GJtbsQG87uX2RY_d--Vwj-UYDEdEHcgIUFwKavHP6zey5CGMXT0fhDTvX5EWubXuyAnkAhEx-Gjp6mHeryekfd74cdb7EWscISM8OB63vbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=iEe49SCE3w6dIPxapE5zn9NBeJLGNWfh93F2S2_bGXJMcc6PskCHvw_ZaUH1sY4pGA6GRUnZm3lW2bHbnVZwoEYNSal82IcASzeZucGzaJjw5AZqUKvE9htQ_6aP6i3iX7Na3K9jUc0pzPs5yws5rNN9GHw2Qch_seW2PW8NKxtxa6aL-UuRNLFAsjOccDOSOVJEOMzSuu1M_5t7rsq7wnk6lVkIQ8LYTF8lB4_JrT84EiBencG-HVIEFpDS2xfmsn1aBEkMHWUM3Fh2kkF9IfWVK9hqM9j5cgtnwc1LIWP1Q-oqvzopOvJQpuy1J7wFgHgj2WP-aA6pWjCauBzyZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=iEe49SCE3w6dIPxapE5zn9NBeJLGNWfh93F2S2_bGXJMcc6PskCHvw_ZaUH1sY4pGA6GRUnZm3lW2bHbnVZwoEYNSal82IcASzeZucGzaJjw5AZqUKvE9htQ_6aP6i3iX7Na3K9jUc0pzPs5yws5rNN9GHw2Qch_seW2PW8NKxtxa6aL-UuRNLFAsjOccDOSOVJEOMzSuu1M_5t7rsq7wnk6lVkIQ8LYTF8lB4_JrT84EiBencG-HVIEFpDS2xfmsn1aBEkMHWUM3Fh2kkF9IfWVK9hqM9j5cgtnwc1LIWP1Q-oqvzopOvJQpuy1J7wFgHgj2WP-aA6pWjCauBzyZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3MHKgFHl3cBW69sN-YuZNnlOznhoM7i1GN5S41QLo1p3slvICTLRRuuHmpcFGvPLa5xfuIf_LfH8u3eQkzwV9JYcGMorcOvGdlHFnkEEEsijPBIFupze2gnMEOsSMJSALINUqIUAtyt5QzCB0SjFvJAu8ozQiihzXyvm2nXPIAVMcBhdtTUseTpxhX6fvW6lECL7_9vDv_tGxWuEZheEq64D0vCDJYss3mBqEC8vsYMjBbCFQt3eQsruHf5STROmB5Q5TA92f5jksr2ov02Odj4Ikb4rrZ3s-85wN4OkW2das-0wmaxyLh9BRYr3am6b8TVzKZsBOuZQajybQWUjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiKsJgEjTLsU15xynJC3Y3x_d17zRitY2SnR8kItlsRccrXLZ5Zh8VI-SxWK4ZrWN9aG9tJPnkANEaeqSTGLrF05ohAiAIRIoLSxBk-JRIpq4s6Zul2_T2ujua0ue5ZCGoKHt7F65Y60FbF8Kpkeq64P1rZIxfPpTse7WNAZ2_L8UjLHqx0qhWnPPC4DgcoFGCeoC70TUJF5SMF9br5Ob4wEKgJWhYQqgSqqlFmWlcNtD_9Hhqjm47qhBrrIDFAX5jIlp6C6TYjPs4nMO8Ydoo9sUVKbHcOE98xwsVZZ_qD-Wfbd3snYLdQGGOoFcZh1zTTDzu3drRIoGXts92mcxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSK7FRocUCmrYkluFhUnLMZ_wtrFb7LdnUTYone106Uo4--A-g1nx5TDJDns57AlELEc0X0P0TQFrZwcgp1KRNSc_o1fljZwKTd3_-slw41zljDFWayugVBRYwtoGxA0z8XIRunsJJs9EI3reK-LXUDbqWAB1RNXR5WOJ0oXwjOdmEKOcgfigcJi_zAn8XUe5Z1c164l3IyxY7MU_ZaFalRlDZd9cQy6RPThoGiOAkCcCKqwgZvUFHVzo2JBxoyGDF7JvrX9tNnRowUSSASh7zuSCLwQJP4l-k5Hakaweh-EFoZmR9lMDkQuT7pDTQDednYkTX51XqBim_JueqJN5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6303" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHWP55QeXENhBxChT60k5e6FRSBtsWN102ymOnf-Bw0PxJrBhtgWDmXfgqH-FHvq2NfxeGLtsymMDU4t-Q7NoDHWDVRJz77qVKoeboPEDChpKFOh5neoiO9oSf7y3EXAYnt1DC0rQ-36WWWe42wP5WSlFC-F5pGM-pHZas3J_0IkjOrxsdWlP2vRyqZfeLXLXFtgLIzKgotaOIn20_-KUEt5TMxznJonvp76rk9BQ1trIp6ObFxKCCFPSHMzDeThESSNVERb-DTF4ZBY01dkeqaAHnzRImC_cyAQrRtX99gIhXVL8RxcKjzIS2uMHQZ-QDXUK17xTJKDTd2IkMy4Bg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=MCUrkTM1qW6208H_SqUlxOr-H714S4ROoMhv6jFZQjy93YMxO6BUIF1BFkNDF9ufixpv22vBDdvXFkA-eFS97TqWXDqggG_cFkz0Y6ert9MjdS0I6JZhwtS4SvAvGh0_hj7EUu4IboEU3-XcMLQzvTOK-jStR4Z23ZLmXOc36p6YGONYSwMFRRZQY6lOvmAewGLMJv1Pi9nrQSVckgj_J6m3V6tMhkPy6msrtLkYmkAFqW3cFUItac0xM-WZFujDhNMjvJ05jUgFAOv5whyl4dxbWKjoZS-FN8V_Wt-RwHRHmLBGhDUbU23x0DaAoJsOMmUafBKgBKXYr-ZWOCXT1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=MCUrkTM1qW6208H_SqUlxOr-H714S4ROoMhv6jFZQjy93YMxO6BUIF1BFkNDF9ufixpv22vBDdvXFkA-eFS97TqWXDqggG_cFkz0Y6ert9MjdS0I6JZhwtS4SvAvGh0_hj7EUu4IboEU3-XcMLQzvTOK-jStR4Z23ZLmXOc36p6YGONYSwMFRRZQY6lOvmAewGLMJv1Pi9nrQSVckgj_J6m3V6tMhkPy6msrtLkYmkAFqW3cFUItac0xM-WZFujDhNMjvJ05jUgFAOv5whyl4dxbWKjoZS-FN8V_Wt-RwHRHmLBGhDUbU23x0DaAoJsOMmUafBKgBKXYr-ZWOCXT1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlUVds8ViuZiiHEC_sZ4K4sEiW2dHWrBKeBBREL1Ggk4jAspMYc-thOxFx3rABZON3JdtTVMSt3q1KqrXbKu3z9aJOpvd-Vk5OoDv2vfxne8JtZF0WL3TNYxnfnzhM5opwPrkU0EAgrTCKEr61rkls_8t7WLTmU3gOQwqvoiL2fcv1f0QoTXBsFt8zqmSwRzudRrXJg-Bpl9ZcU9ipG1xpNXeCGX_MuSYHSEkpLsJKoLtrocLeOXV-LRbxeoFP9I36ZrtFdhS02JS-ObddS9DpYmZB5ZvTTgddx5zGKbhgbY5wDiqY071ml3A4bmmP72zl0igNXKEtf6s9d5rg_17w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6295" target="_blank">📅 19:31 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6293" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hiXFzDoD_E9Srk3rPmWxQHkG9NunkpgA9CnYY8CnQraPstJ2mlD3UZ7sadzFDJz7GUd_to5q2IQqZ5WE2LEAWbz5qo3L9_Wno9FvF2-_-ElnfTPWQvoC11TMY_07YNk9vun9DjmTaA9XDicwkSkBDxnmFax6kYqERhElzRS-OSrxDXlpaVg0GDc_fRx71e3wSfbaJV1I1lmDcPWeYK281ZViWGi1QkpnPbrRTdxEeDBrEc90mvin0QUFcKuZoun4nLs2rS5PZyKHz3WLuTf4kYwjtK0KrZwtq1KFbNwz0UHXX-6_kSEMFzxr1ln6RXcrl3UGpFHZvgW1FAZDiW4Aiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGIq7HWKnBYEbVfXVIrFi956ioZUU7Zrto_D4u1tAsqeGJN69EV151YkMi8bJTkNtz6q3GsVpdgUTTF5um2nmoUyEDN4J_pUMI0ZFZB0SrHxRGiGwhjOp8cq8FXe6kfNkTptF8PBN3GQZY2EFLvyhskmW68l7s9JRHArlpCJv_IZ9aUjjK6xr3xk1mKSwD_78s3eGMlmI6Kso7Wr_AWGYiGN3-09hsgP8YFpj8cYrQOLBd3ISvBF6ltAz0jJr-aUow9HPukAnQ4So61cn8itMeuInK3l0Vem_49U81DHLzygt4cnaihZOsEsbMkqlq81Ma_p3TvXYDjfOjXd8I4vkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_M13PcLMHy8tnCJ00nftIhiFHU_Oksb6NXZ-wV_J2G4CQXCtueA1rTdjVEoAal5sBQhsriJFkrpQAoVzxkGSliOo713IaeJCtmlS29ln0-whgGC0dp6T6P3UeWN5qAfKTeV2mmoGNerQk8QLi8e37gQx_4iAu-qFlJZqxgGeTm6G5Ij96ntsSabghDWbd9vVoYi2INF1D_Ite9eQJqVmh2sD0SS2fRr8jcrq8x6UvPwcZIrO9n49tjkT3KUQYmsm-fFL4vbJFua06h6DpBkMg2Rls6n9tpEVkDmIyCymsyxo0D7hxBmoe1k8GGE4KQyeawlMR7zxyY2Ps7jScqOMQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/54834411b8.mp4?token=crIH3jFSxKckmWiB5d-jryaX0NPvl2CZCZJiwwn5bme9KhQcCJFvEz4fS6Avyb8jPrP41yCo1JUB9mWC_Ca1-ZLKgmIQCk3lbDcfVQvSiT0H3eLqFtKN2aKeualFb4GFQYnBOQmbYa2pCMBdUVfGv97LY2gHaYpPfoxYtiL1hxxE-nmNrPSxqQV_TYfx15M9B6qnRRP_Q-Q79CMPgknha1AnBzgjvYX2lpJPV40ayXou2fu8b4Cbm3zDw8exOGT5f5EzgL1TwClVc7_me7QILpDMQF3lQW0oOEdFZJhyneyE50LGMB7oXjvMqzVsD4ZrLPNN9GB-ySL5HkIQiYIVqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54834411b8.mp4?token=crIH3jFSxKckmWiB5d-jryaX0NPvl2CZCZJiwwn5bme9KhQcCJFvEz4fS6Avyb8jPrP41yCo1JUB9mWC_Ca1-ZLKgmIQCk3lbDcfVQvSiT0H3eLqFtKN2aKeualFb4GFQYnBOQmbYa2pCMBdUVfGv97LY2gHaYpPfoxYtiL1hxxE-nmNrPSxqQV_TYfx15M9B6qnRRP_Q-Q79CMPgknha1AnBzgjvYX2lpJPV40ayXou2fu8b4Cbm3zDw8exOGT5f5EzgL1TwClVc7_me7QILpDMQF3lQW0oOEdFZJhyneyE50LGMB7oXjvMqzVsD4ZrLPNN9GB-ySL5HkIQiYIVqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6287" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6286" target="_blank">📅 11:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=BqpnEEPpXd26LB0MeEcT3zKeF_8Cc4hgzTgBnntm06ICmKvTXl_1jF9ysMtDqwcgI9ueRfoU21C32dUky_9zt-88JzX74uFqvXEUepToK1cqDQ9Gc3fIN8aXhpePXeDvLFaPqu37k_Uh3kFAjxoprqPglm3UGMXLwb4QNU5l0UVILmT3NsGnPVcmgi5uL8PuVtqdGgPYAZi3_snSrlGu649Gr-xqMKlvWUZljT2AYtlfsqsNXlI6wOc1EoYwf_PHkTIAlml9T1pxnR7ghiyJplGmRl1w9ovxC_XXrOpwZwlhqullg3iumpzFw41AMhzBs_K0E1wjedaTn5VE9lfEfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=BqpnEEPpXd26LB0MeEcT3zKeF_8Cc4hgzTgBnntm06ICmKvTXl_1jF9ysMtDqwcgI9ueRfoU21C32dUky_9zt-88JzX74uFqvXEUepToK1cqDQ9Gc3fIN8aXhpePXeDvLFaPqu37k_Uh3kFAjxoprqPglm3UGMXLwb4QNU5l0UVILmT3NsGnPVcmgi5uL8PuVtqdGgPYAZi3_snSrlGu649Gr-xqMKlvWUZljT2AYtlfsqsNXlI6wOc1EoYwf_PHkTIAlml9T1pxnR7ghiyJplGmRl1w9ovxC_XXrOpwZwlhqullg3iumpzFw41AMhzBs_K0E1wjedaTn5VE9lfEfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXuSuWhV8aQtSNf9a5dtPp9lhjTzbH6WrFsldUSN_8-3x2ZwZSBhD8laKy4iKfISyz3d9wXmu4MJlyw6K2SXvZWmOKu7OOgxj-PPGOg8w71XG7o-wYSOj84kdMaP1JUgCZCfrt1gnCOKZsufZGUYQSlT_qwgrJCjN_-NNKHREngRmo_ML-PAWgmDtH2f64v2jLpZmxZAvHcrh6caDCTMj29V6SV29Qr3LuVIY8bp3PJMF7L4Bm-nWvNHOQA_Kxl738mAQuBf49Ji5JNehzUu7om0SRvORvgA2UiaJ3QKeIBj2dSjrzksnvM82aFPPhxFIhxScHYGChUe2oB76eADXQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=IwyGu2RAMjNGKjGjXuhHVq59wB8QMV1ioNln49Q8qsjxJ9b__BQE-ibwlRBbipPQJRKKlxJxx9Y8e639mqpykyG_0w6WQs90UbCsLKonBG_1tv9gWz2RIFQ_J9ri55ALPX5avoDUyHLMwnNu3QY1K7tz1iXlHRJEgqUHUyFXh8J7e8qHUEz4P-ZA9G3txkuCdMr1VameO6z9XkDL5nYBwr0FzYysZ73RiOokjRAKv-mTrwIYfrVKXVb6BrvfMm1hUdPvBonccpneHpcitsK5Pnmpllaeu09z-fOPc9vEKCNtvG-3bz_bT4Kbu7VzKYfOPnTn_koPqBURD5BGTikYqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=IwyGu2RAMjNGKjGjXuhHVq59wB8QMV1ioNln49Q8qsjxJ9b__BQE-ibwlRBbipPQJRKKlxJxx9Y8e639mqpykyG_0w6WQs90UbCsLKonBG_1tv9gWz2RIFQ_J9ri55ALPX5avoDUyHLMwnNu3QY1K7tz1iXlHRJEgqUHUyFXh8J7e8qHUEz4P-ZA9G3txkuCdMr1VameO6z9XkDL5nYBwr0FzYysZ73RiOokjRAKv-mTrwIYfrVKXVb6BrvfMm1hUdPvBonccpneHpcitsK5Pnmpllaeu09z-fOPc9vEKCNtvG-3bz_bT4Kbu7VzKYfOPnTn_koPqBURD5BGTikYqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrbC4a1pGTZ3E6PQv1rpPcGiIXvZd9C83nLKnQDVrrO07iQOdtF0uEucpnFkkcwTBviuqkW5em2JYJhWucKKxH3y54kA3vre3bwwKXPjBodC9FynoSwk3TNIn7fkM1MjthIxkS6uTtt2gNWYWwksQ0FhqOd7NzjVBho64n9Cd2gEMPhWRnNIAn-H2WKBmGtGWdFlOds04CaegWnZmcmzsDdU2xNh4iZUTPlJmT-nIlD3XcPVKj69b4AEuo6vSpT4mRXBS1aarLujrmq3zx5wPTbgViuGYZwnD1HMfjJ1ZVWqd7Kg0-8iYIQiAoHb6Js1pN-5_aSmpTJ2xYqfCmFXvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OO182w5Oi3vITnZWCckAv54QXBOfR1_NJDt17PolCF71PFhdMkMdNOcHga5eAq8NbTVUQ64HY_AEKmfpSLQP6mZi-Yf_g4VqGoUWIbKHLGVICFzeLis85-MzoLVrCbQMy_6jHzjcgf5XXLaV2qc6W0ZQqG4jakwCqZ2EF7I9evZp6Mm6tMtKnuWq5g71jha83xW8wHp66sEvkq3Tzd5hico_GsdAOkDUHGJoiJRmDGo-QDbDaoexZPV9fYHNSkfYBNioXf3U7EqqsZaVxckUZNrw_0ZpsE3AOlngMikK_R_xQHgQRrQc_Ef1mfV_S0_cHj0_1FwGEM3GtK_HbPRvDw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=sWFZVDpX_5EEEEd6eNvoCwHxE_hxJc-PwAe5rMItBcJ31818phBFBmiaxH2c3h_MWuc2J4J5yONOvbjE1sDZgA79rzdgvb6JQ-coV6vBmi_Df7EFkWG_VwqiPmDZqrCTnNcVwCGlfWsGCL0WQwd2MYCJk1r3Z2xOP4x3w5y1Loneg5PyW09-UYfBmhkr1G-4LhZc0S3PVj0c7WkMnuYifkB14pjD72aklOUlEMRdsrV3TxwGG87ORoyTSQgGz6RBaY6CN3SfKAVPq0rOQt0xS4sSctSC_5Oezcwbuxs8hkck0mw4HEL2wQMOIErbeN9E0kkdWh-4z-wmKCoG297xAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=sWFZVDpX_5EEEEd6eNvoCwHxE_hxJc-PwAe5rMItBcJ31818phBFBmiaxH2c3h_MWuc2J4J5yONOvbjE1sDZgA79rzdgvb6JQ-coV6vBmi_Df7EFkWG_VwqiPmDZqrCTnNcVwCGlfWsGCL0WQwd2MYCJk1r3Z2xOP4x3w5y1Loneg5PyW09-UYfBmhkr1G-4LhZc0S3PVj0c7WkMnuYifkB14pjD72aklOUlEMRdsrV3TxwGG87ORoyTSQgGz6RBaY6CN3SfKAVPq0rOQt0xS4sSctSC_5Oezcwbuxs8hkck0mw4HEL2wQMOIErbeN9E0kkdWh-4z-wmKCoG297xAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6277" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=P1XjDjQ7LdKfv-vLqe77VCFknT01YqLd5QlHqBK-JUdUC9RJZLn1IdmZ20_TNDXHVuUolsK2LuKouKP8foS660Jrt26oQk5EiANU2CDut6Quzuq2G3fHPMDZwK4pGKtHkrO6orakNggRQ0kp7Xk0AEiLb40FgbxzLgi6TzzXAbW5ZcFONnLr-xyqSrHtigu9VvhkteKIzVU-EJ6QuJZft3HrgEINPuKeXdWiYwTG48tBBeyWd4icL9WqSkVOPkC392FKk2Nm7Uzs-7dvGpL_SGvZoEboIbFyx-0H3kz4agY_U2lUkyGkJ9MZ_jLMA_3f9LtI0wU2pFrtZLlTFGeXGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=P1XjDjQ7LdKfv-vLqe77VCFknT01YqLd5QlHqBK-JUdUC9RJZLn1IdmZ20_TNDXHVuUolsK2LuKouKP8foS660Jrt26oQk5EiANU2CDut6Quzuq2G3fHPMDZwK4pGKtHkrO6orakNggRQ0kp7Xk0AEiLb40FgbxzLgi6TzzXAbW5ZcFONnLr-xyqSrHtigu9VvhkteKIzVU-EJ6QuJZft3HrgEINPuKeXdWiYwTG48tBBeyWd4icL9WqSkVOPkC392FKk2Nm7Uzs-7dvGpL_SGvZoEboIbFyx-0H3kz4agY_U2lUkyGkJ9MZ_jLMA_3f9LtI0wU2pFrtZLlTFGeXGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6276" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=iBfO0qBRI2XYdRvZvGH8p8RAzVMLQ1Z1pGLci90pUcHc5WCcN4quDFhhFiXaqPNd1vWTGFl3ojMSuoQZ6x3gieLnzh1XxwoJXO1eZqNYVZHeSf3cuN4ZJSQwQp6p8pRUEnLySo1WHv4FktLR6_jEc8tybBYDNWjgxwfHHNzOHaIm4jn71N28OjRbl21ts35wnoHHXR9PY27aIGsGowj3JtFHsPil6LN7uRe4VBaK7r7obOmm0U8w_GKXebXfhUCkey3zjUDFvBRM-TMLxWjZQM5CQ_fuiISnItRkCdEpsaaNoVUoyU7Su5hcWLy4VfKYBOyHOoAWWffsrJ1od7jCtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=iBfO0qBRI2XYdRvZvGH8p8RAzVMLQ1Z1pGLci90pUcHc5WCcN4quDFhhFiXaqPNd1vWTGFl3ojMSuoQZ6x3gieLnzh1XxwoJXO1eZqNYVZHeSf3cuN4ZJSQwQp6p8pRUEnLySo1WHv4FktLR6_jEc8tybBYDNWjgxwfHHNzOHaIm4jn71N28OjRbl21ts35wnoHHXR9PY27aIGsGowj3JtFHsPil6LN7uRe4VBaK7r7obOmm0U8w_GKXebXfhUCkey3zjUDFvBRM-TMLxWjZQM5CQ_fuiISnItRkCdEpsaaNoVUoyU7Su5hcWLy4VfKYBOyHOoAWWffsrJ1od7jCtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6275" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ادم خودشو باید برای هر سناریو اماده کنه و باید تو پیشگیری خوشبین باشه. چون شاید همون ی روش هم جواب داد</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6273" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6268" target="_blank">📅 00:30 · 21 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eS84CI3Kd7xMTVlWOcH5Gxq3zvUASHSdsIg-g-6FGYoQbVAMKTte85mGEjk5dMeIvLIkqnrAc1sJno1iZ4qKACMTmi_wNOrtVhELaM_7DPB9MfeQp05JNa0DZhtwlflDx4oOCFzVJ9Ns-xm8Og8q9Gj5_kP2Vd1vtPJCB50CEON-G5TfCcFCcmYBp82XG7EpEIDZpIXpxU0UD_eJ7dZM1pvn_lSp23oSBWW9JEOEMSPwrS33ztkGadofQp0F58110IEvdBqO-jrOllEtJGw3EC6n-CTDZufDYIpt4A5zckn8gR5SziruhmD_BcaQJ7Oci3qIxQZ0yk8VPTNhaWBUlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6266" target="_blank">📅 20:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1_RMJpsO2N4igZ9BO7aBfSZTflyOTmu9p5cgybC9G9wenk8WJL8N72gtQ5WXZy9cD9ogOZN7BzAT2lRWZPjahmlnQygqzzhhpXKkrR6GB8-ypiR8er_ZpVVySQiFPMWfiUXtFpAS2qUe_mdR2XXtCGbusELHB1-z8SgkZnGL4XyHq54ZNfPkCnlhczBSANa76e1EYlrEbWKfUSXfm_yS42PP1YFp0pig_HDqIyTC-Bzijg8xHURbfUhDAV4bTGsEa_PTE_IRCTcivoJCHd3M_wAa0sCaGrlZ3qskpUwmUz4RtQR7JGarqz2el-VFO7Cc3dfNqGgmqA_or418SlIsw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/581e875845.mp4?token=vVLcQHUcoJOFoDhHyXZqtPyW-Qt9L_pPE3cHcBtSK8RKWqoPmpAr3ZYgodIRRk9IRdDA2qoocuPBVIsxRfJfWeYCLdQrVTeTiUW9vthgspg6WfO0RAfTGzUEaBqh5Zz9UWV2QcPnsBWuvDH3HqN_Gk5eP1MrMDQjtkHqOg164nFQt1lPtZXHG6aBW8GEYhRMQvU6NkjcdTeH6diianUdHTz0IP3LbEKQpLEIgTYMJpymdfW6QXNq25ITlEf_X2sk2GVJKPFHxgreBxrYmsRPBBlaaxSOdE4wiCkIKbgRtwmt4KgN9KDDSi4AIAr6gJMU0KdioW0dDLxY22r_GomMYIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581e875845.mp4?token=vVLcQHUcoJOFoDhHyXZqtPyW-Qt9L_pPE3cHcBtSK8RKWqoPmpAr3ZYgodIRRk9IRdDA2qoocuPBVIsxRfJfWeYCLdQrVTeTiUW9vthgspg6WfO0RAfTGzUEaBqh5Zz9UWV2QcPnsBWuvDH3HqN_Gk5eP1MrMDQjtkHqOg164nFQt1lPtZXHG6aBW8GEYhRMQvU6NkjcdTeH6diianUdHTz0IP3LbEKQpLEIgTYMJpymdfW6QXNq25ITlEf_X2sk2GVJKPFHxgreBxrYmsRPBBlaaxSOdE4wiCkIKbgRtwmt4KgN9KDDSi4AIAr6gJMU0KdioW0dDLxY22r_GomMYIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6262" target="_blank">📅 18:05 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6261" target="_blank">📅 17:29 · 20 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTLBgYamfFvvQgZb1g1hQsfUf4vGL2jEE64ss84x_PAKc1FwPwpQHQHpx8rY9VTi8Y6T-P8AlKM6NZGa7CbfMUiL5Il_8ALqh4kBM3zgaFn30d_ITw0_43xb_DcYvTwK2baToP1AKmv0OaQV0TNvKEVsxNmHvqLthydybRXrnN9pEu_jvajITDgfBbVBgxy5fBQzK-lxkUZ6kZ4-u0_vHwtkaXSZVlWRWBKAASFBO0FIroQNupDi6VSK2zLl6MvlR_nlirfahMjWvFtt69_-B_DNghpDL0sdB4R19ZgEHBhh7p3992BRUv0_-UEgTZ_JwaLNuVbpQKB9nv2Qyx2ovw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=ellBTYSq1X_tiGUaEJZm2A8twqhr8hSnpQ8DEIc1Kb-22GojyIiY-z4rePRjBY_WvhjELHbtXgC6TlEIpPSQup0n4VB0gOX47mFlNeDhsHX8OXXn6jjKp6vO-sPnbdemhPeL-CapXbOoTJWumUCxEdjQPUYrZNBi3beRubyft-vpe59B1xjLke6pJLDtmy-dAtb01cSh_ZBJzu8AHJF1rcQg4L44NH0nYyafk0HR5B8K4UN2GmFAVgqcrWuo4AuA9oCZ7kk3YLo5nL6IIaDqDP4ks97Feylmu1-nZlfZnux85NTDdlSc7LACTVGe4H8twDC2p11FbsIfWQkIaS69OLPWB4oud8M4WfbpTg3GkPjVValLEQsTnVDB-0O6zTsvLTEHJ-rk48mgFC5jGSzhnsrVIONjsEpVhxpGJhmM7x66f1jsU4fdz76bjw7cSsm4JekFb4Wu89TLj7vh6eMaef4wHj-y1JZtU36B53FrTf2w67UazvTcbWUgIrBDp3ZDAVqSJvF4QMwi-Y51ZLae8Sfvc-Oh5WtuUzwfORCHCNuoMPD5SMaODQZvk_8GNlu_cdG3Dt52zyPz5yE3oyBNm2cC8Lli1YzR37dXtyZze3luK5XPxPU7D4dykA_weN4MvcvqBphf33p0rSqjBnWwZ2KKvqEhI0d__8tcAktK-ic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=ellBTYSq1X_tiGUaEJZm2A8twqhr8hSnpQ8DEIc1Kb-22GojyIiY-z4rePRjBY_WvhjELHbtXgC6TlEIpPSQup0n4VB0gOX47mFlNeDhsHX8OXXn6jjKp6vO-sPnbdemhPeL-CapXbOoTJWumUCxEdjQPUYrZNBi3beRubyft-vpe59B1xjLke6pJLDtmy-dAtb01cSh_ZBJzu8AHJF1rcQg4L44NH0nYyafk0HR5B8K4UN2GmFAVgqcrWuo4AuA9oCZ7kk3YLo5nL6IIaDqDP4ks97Feylmu1-nZlfZnux85NTDdlSc7LACTVGe4H8twDC2p11FbsIfWQkIaS69OLPWB4oud8M4WfbpTg3GkPjVValLEQsTnVDB-0O6zTsvLTEHJ-rk48mgFC5jGSzhnsrVIONjsEpVhxpGJhmM7x66f1jsU4fdz76bjw7cSsm4JekFb4Wu89TLj7vh6eMaef4wHj-y1JZtU36B53FrTf2w67UazvTcbWUgIrBDp3ZDAVqSJvF4QMwi-Y51ZLae8Sfvc-Oh5WtuUzwfORCHCNuoMPD5SMaODQZvk_8GNlu_cdG3Dt52zyPz5yE3oyBNm2cC8Lli1YzR37dXtyZze3luK5XPxPU7D4dykA_weN4MvcvqBphf33p0rSqjBnWwZ2KKvqEhI0d__8tcAktK-ic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
