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
<img src="https://cdn4.telesco.pe/file/R4cG55bvEK71P-oQekMq-zdWofyGSkDZdo3LGi83uw7ajDCbh0GkWCAP5t5SR4yNwVL9dv59w3epXLOpwvXDAjiI3f-n7wKC05_a7LN76KmKeiAbH4bALT2GIIXcE5HLfSEeuIbOY2cAEtrTjq4u0E-701v7Yi1fqv9ENin8LJVmsdQKROFf4q9pJAYZ_8TD4yBAZbzv13wD7kqQGIXiafRcCDtMy1NoxuTFOpfM_5bV-m0yaAkLVMCGC8k7C7QRCLvT4WOxmjdPo6xYnpgrMs-S59s1Qu-5C8gFjF06TJqNi8fZJTpYGe-HLSmTbPo7lIwX2oADQg44VW-VFJnJcA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.7K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 14:16:28</div>
<hr>

<div class="tg-post" id="msg-132368">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
فعلا تلاش‌ها برای بازگشت سردار آزمون به تیم ملی جواب نداده.
🔴
سردار حاضره پست عذرخواهی رو منتشر کنه. قلعه‌نویی هم گفته هر طور شده سردار با هر تبصره‌ای که هست به تیم اضافه بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 934 · <a href="https://t.me/SorkhTimes/132368" target="_blank">📅 13:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132367">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🎙
‼️
پیمان حدادی:
‼️
🔴
برای بازی با ملوان به دادگاه CAS شکایت کردیم، سپاهان و گل‌گهر هم قرار بود شکایت کنند. امیدواریم سه امتیاز این بازی را بگیریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/SorkhTimes/132367" target="_blank">📅 12:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132366">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎙
پیمان حدادی:
🔴
ما هم می‌گوییم استقلال نباید معرفی شود؛ در حالی که نماینده پلی‌آف در آسیا نداریم؛ بعد از جام جهانی در کنار لیگ حتی می‌شود جام حذفی هم برگزار کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/SorkhTimes/132366" target="_blank">📅 12:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132365">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🎙
پیمان حدادی مدیرعامل باشگاه پرسپولیس:
🔴
با چند بازیکن وارد مذاکره شده ایم اما هنوز از آیین نامه نقل و انتقالات برای فصل آینده خبری نداریم. نمی‌دانیم بازیکن خارجی می‌توانیم جدی کنیم یا خیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/SorkhTimes/132365" target="_blank">📅 12:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132364">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrH-zCseqXYvPsZoNYfJ3OVT0eimwa04jsgfa6_PV_Qd1A5m3KQiCOYkpKAHSw-hWWOK6FB3E9x2Yls7gWU9YVLK2zZ2QlwifCJlnv0dVi8SbJqBAJIQnH8f3UxCINQ9jgAsYmel0b9S63fu9rh5oPx4DoOrNowV8AmzfCyhI_EoZcJhnhSHmnmjblwngKJerjpZA8hM8vOkNr9w-Y_ftH3gIWsWq0c_SAyNfbddtpwkX9lt0CR6MzcPqnQn_rREOIUkJRQLRVjYfS1MnGc4Hmr4ONTgXKvNwSGHCSaWRubMQESaC1L8Jz5AntqSe7Ot8Z10FpCUlxY5XxJwTltfOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#روز_شمار_جام‌جهانی2026
⚽️
14 روز تا شروع بزرگ‌ترین و هیجان‌ انگیزترین رقابت فوتبال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/SorkhTimes/132364" target="_blank">📅 11:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132363">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">#فوری_مهم
🚨
🚨
گویا سپاه امروز پایگاه آمریکا در کویت مورد هدف قرار داده بخاطر حملات دیشب آمریکا به بندر عباس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/SorkhTimes/132363" target="_blank">📅 11:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132362">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❗️
نت بلاکس: به نظر روند بازگشایی اینترنت ایران متوقف شده و در حال اعمال محدودیت‌های بیشتر برای جلوگیری از دانلود و استفاده از VPNها هستند!
🔸
کماکان هیچ اخباری مبنی بر اتصال کامل اینترنت دیتاسنترها وجود ندارد که مشخصاً برای جلوگیری از گسترش تانل‌ها و VPNها…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SorkhTimes/132362" target="_blank">📅 11:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132361">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔰
سرویس VIP
🔰
5 گیگ 300T 10 گیگ 600T 20 گیگ 1T 25 گیگ 1.2T 40 گیگ 1.6T
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال و مدت زمان نامحدود  جهت خرید از پیوی =>  @Winstn_Churchill</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/SorkhTimes/132361" target="_blank">📅 11:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132360">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔰
سرویس VIP
🔰
5 گیگ 300T
10 گیگ 600T
20 گیگ 1T
25 گیگ 1.2T
40 گیگ 1.6T
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال و مدت زمان نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SorkhTimes/132360" target="_blank">📅 11:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132359">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❗️
خبرآنلاین: سردار آزمون حتی با دستور رئیس‌جمهور هم دیگه نمیتونه به جام‌جهانی بره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SorkhTimes/132359" target="_blank">📅 09:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132358">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⭕
تلاش بیهوده برای رفتن به آسیا یعنی حماقت اون هم زمانی که حقمون نیست که به آسیا رفتن فکر کنیم
✅
باید بپذیریم که اگه شرایط جدول برعکس بود و ما صدر جدول بودیم و لیگ نیمه به اتمام می‌رسید حق خودمون میدونستم که به عنوان سهمیه ایران برای لیگ نخبگان معرفی شویم
✅
نه به cas فکر کنیم نه به تلاش بی ثمر. Cas تا بخواهد به پرونده رسیدگی کند سه فصل لیگ نخبگان سپری شده.
✅
برای فصل بعد برنامه ریزی کنید. تیم را بسازید‌ ریشه ای و بدون بازیکن سالاری...
✅
پس بکوبیم و دوباره بسازیم.
فرصت ها را از دست ندهید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SorkhTimes/132358" target="_blank">📅 09:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132357">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzaN84p1mV9_UrCLZ4KHhHdcXBmMbO-pSxNRQF8WiGQdZkzGXI-rrjZFvGpLWdlh6TQ-dlZw_y3NjgXbrJZ50YtdZO4OE54KIyyL6v3ZqWgAD1PHpqHbhEfQiyfRCGTUKMCEYZ7QGQGi3KBiwdod26OfR2_2uob-_1zDc_rT7o_CDSHKztY0a-CfiWrdU8LWh5VPF-UQc0203jmYg1W1vjsRdlhEXs4THJvrLhOLGUC2osGBUfjeg2uYCSrad8M4cAUEW8mLFAY-f5DYnQoRUE05BwC83BXz6UoRZH6441BmlKxULn5FqmpjMx4vXtbu2kCl_GALEbZZw5LYNWEwAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوسمار برنامه ویژه‌ای واسه پایین آوردن میانگین سنی تیم داره و باید با اکثر بازیکنای بالای ۳۰ سال خداحافظی کنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/132357" target="_blank">📅 09:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132356">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
تسنیم: ساعاتی پیش یک نفتکش آمریکایی با خاموش کردن سیستم راداری خود قصد عبور از تنگه هرمز را داشت که با اقدام سریع و قاطع نیروی دریایی سپاه و شلیک به سمت آن، مجبور به توقف و بازگشت شد.
🚫
در مقابل، ارتش تروریستی آمریکا به زمین سوخته‌ای در اطراف بندرعباس شلیک کرده‌اند که صدای انفجارها مربوط به این ماجرا بوده است؛ این شلیک هیچ خسارت جانی یا مالی به همراه نداشته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SorkhTimes/132356" target="_blank">📅 09:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132355">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPJSaQOZ-k9uML6bAM0LJNO2eNe-DHEE6DFJiFOmEXda9j-JW4gCJf3GSXOF7C8BbuYtyIa7XUg5nTzfgp7zWXx7IIor7HiOqgsKFqZXOjKXPXfFBp85wbtIouL1vTRzeECeJRqbnxKPYJDca-eBXvRaUC6Q0hUjB2gyNMMnbRMEpl3Cz323RHosyVCcIXyjWr36DFrimJTmbiUKl9hJkTaYkupgBmXTt82q9FJJyusRb7zpHx5tG8Dn91c_fA_Hbm_VO9Q-dB4aI9DFqOHXzP0gkfjqHvgwo6BsWeTLzrcRlK4c6SvFdk_F7pPHsG_PowvW5Iw6v-dvv76Axjw6sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SorkhTimes/132355" target="_blank">📅 01:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132354">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
رضا درویش:
صحبتی برای حضور در هیأت مدیره پرسپولیس با من نشده است.
🔺
در ورزش بهتر است هر فرد پس از چند سال فعالیت، مدتی استراحت کند. همان‌طور که یک پزشک پس از انجام جراحی‌های متعدد نیاز به استراحت دارد.
🔺
فعلا ترجیح می‌دهم دور از فضای اجرایی باشم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/132354" target="_blank">📅 01:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132352">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
گوگل پلی رفع فیلتر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/132352" target="_blank">📅 00:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132351">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
خرید بزرگ پرسپولیس از اصفهان میاد./مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/132351" target="_blank">📅 00:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132350">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❗️
نت بلاکس: به نظر روند بازگشایی اینترنت ایران متوقف شده و در حال اعمال محدودیت‌های بیشتر برای جلوگیری از دانلود و استفاده از VPNها هستند!
🔸
کماکان هیچ اخباری مبنی بر اتصال کامل اینترنت دیتاسنترها وجود ندارد که مشخصاً برای جلوگیری از گسترش تانل‌ها و VPNها…</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SorkhTimes/132350" target="_blank">📅 00:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132349">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔰
سرویس VIP
🔰
5 گیگ 300T
10 گیگ 600T
20 گیگ 1T
25 گیگ 1.2T
40 گیگ 1.6T
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال و مدت زمان نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/132349" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132348">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
ترامپ
🔴
کنترل پول اونا دست ماعه و وقتی اونا کار درستی انجام بدن و چیزی که میخوایمو بهمون بدن ما هم پولشونو بهشون میدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/132348" target="_blank">📅 22:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132347">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
نت بلاکس: به نظر روند بازگشایی اینترنت ایران متوقف شده و در حال اعمال محدودیت‌های بیشتر برای جلوگیری از دانلود و استفاده از VPNها هستند!
🔸
کماکان هیچ اخباری مبنی بر اتصال کامل اینترنت دیتاسنترها وجود ندارد که مشخصاً برای جلوگیری از گسترش تانل‌ها و VPNها…</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/132347" target="_blank">📅 22:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132346">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
بودجه سپاهان برای فصل آینده مشخص شد
⏺
باشگاه سپاهان بودجه 500 میلیارد تومانی برای فصل آینده خواهد داشت و به هیچ عنوان تصمیم ندارد از این سقف بالاتر برود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/132346" target="_blank">📅 22:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132345">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
🚨
حمله وزیر ارتباطات به مخالفان اتصال اینترنت:
❌
واقعا شرم اور است بعضیا نمیخوان اینترنت وصل بشه، اینها فکر میکنن اینترنت تو دوتا پیام‌رسان خلاصه میشه اما اینطور نیست
❌
من و دکتر پزشکیان با قدرت جلو میریم تا بهترین اینترنت رو در اختیار مردم که حقشون هست بزاریم…</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/132345" target="_blank">📅 22:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132344">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
🔴
ترامپ:
✅
به درخواست نخست وزیر و فرمانده ارتش پاکستان، به ایران فرصت کوتاهی خواهیم داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/132344" target="_blank">📅 22:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132343">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
بودجه سپاهان برای فصل آینده مشخص شد
⏺
باشگاه سپاهان بودجه 500 میلیارد تومانی برای فصل آینده خواهد داشت و به هیچ عنوان تصمیم ندارد از این سقف بالاتر برود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/132343" target="_blank">📅 21:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132342">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
الان به نظر میاد خودشون دنبال توافقن. فکر نمی‌کنم حق انتخاب زیادی داشته باشن  اینترنتشون تازه دوباره وصل شده، اقتصادشون هم داغونه، تورم هم خیلی بالاست!  شاید مجبور بشیم برگردیم و کار رو یک‌سره کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/132342" target="_blank">📅 21:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132340">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
بودجه سپاهان برای فصل آینده مشخص شد
⏺
باشگاه سپاهان بودجه 500 میلیارد تومانی برای فصل آینده خواهد داشت و به هیچ عنوان تصمیم ندارد از این سقف بالاتر برود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SorkhTimes/132340" target="_blank">📅 21:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132338">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
❌
مرتضی کرمانی مقدم:اعلام قهرمان؟ اگر دست من بود می‌گفتم همه تیم‌ها به لیگ پایین‌تر سقوط کنند. مگر کیفیت مسابقات امسال بالا بود که حالا منتظر ادامه آن باشیم؟ به معنای واقعی کلمه هیچ تیمی مدعی قهرمانی نیست و از این به بعد حتی اگر مسابقات برگزار شود بعید است کیفیت آن تغییری کرده باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SorkhTimes/132338" target="_blank">📅 21:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132337">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmN6LHNuGWW4KBqOBqLHnzANicMufstBcQ9rbozUCOubkwde85OgcvB3kQEwVC2HlZqqnQV0QGXvuNOazBpIs137t0Hiewmf0XQTbfwCA2i0hK7rVKNQBUhuTORvsK36N1PqmlxgNDXXd1JO4ksYqdRbYswh0111M0gxRcuvgowp-xReo4Y-ZMx8DEDjBjIIZYJQOmJn1w47tjmfguAjfMdJrtoULtJrc5FeqYVXvRPa6by7wCm8_PAfsUIOr1ztCppP_VEUOrCiIDeKf3ObRHqiDiTD7SGVc3BoVeVrEvSAch04fc3cA-8-3FHoGUIHilmOTmu7Q6t8YkwWqFLSnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
فینال لیگ‌کنفرانس اروپا
[
کریستال‌پالاس
⚽️
-
⚽️
رایووایکانو
]
⏰
امشب ساعت ۲۲:۳۰
🔗
این دیدار هیجان‌انگیز رو در سایت اسپورت نود با بالاترین ضرایب پیش‌‌بینی کنید.
🎁
بونوس ویژه ثبت‌نام برای کاربران جدید، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SorkhTimes/132337" target="_blank">📅 21:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132336">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
باکیچ و تجربه متفاوت در پرسپولیس
◽️
سایت‌ها و رسانه‌های فوتبالی مرتبط با کشورهای حوزه بالکان در مطالب منتشرشده درباره باکیچ، روی سابقه بین‌المللی این بازیکن تأکید کرده‌اند؛ هافبکی که سابقه بازی در لیگ‌های پرتغال، ایتالیا و یونان را در کارنامه دارد و سال‌ها در فوتبال اروپا حضور داشته است.
◽️
رسانه‌های این منطقه همچنین حضور باکیچ در پرسپولیس را اتفاقی قابل‌توجه برای فوتبال مونته‌نگرو توصیف کرده‌اند و معتقدند بازی در یکی از پرهوادارترین تیم‌های آسیا می‌تواند تجربه متفاوتی برای این بازیکن باشد.
‼️
نظر شما درباره باکیچ چیست؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SorkhTimes/132336" target="_blank">📅 21:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132335">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
اوسمار کراش زده رو آریا و لیموچی و حزباوی و باشگاه در تلاشه برای جذب شون راهی پیدا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SorkhTimes/132335" target="_blank">📅 21:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132333">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
#فوری | ترامپ:
🔻
ایران می‌خواهد توافقی منعقد کند و ما با آن توافق می‌کنیم یا به ماموریت پایان می‌دهیم
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/132333" target="_blank">📅 20:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132331">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b15265d538.mp4?token=Dxn_3qGeGF07tvtbjQeY0meHzm8mZTGx9lMjp1C1zS-YWelTurx-TC7JHBEVBAx8L1gmlJJ4mEilMznruOlzrV0Ydju3zH05ZjYkf3h3mQm95M3c_D4SPOLZpf3Dx0rxCbe9VK1WRlSpmMRhoXKjYgvQoSJagjdq50rpwRGpXzVa_qMc1-jLfNRcit1nkYctgvMEVBrOJzByDcz-p2vZic2e6bM845MpFngDGZ-N_SH1N0GMu_xoaz6tpjERNuID_Moi_rRwfP2iJfmKVIrG6jEfWY3VYP_YWsz1sX0IwASgqZC6CiaJrp1Y1s2b9ZrTA7Qn1YdxrEWF-c_l9bD3mg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b15265d538.mp4?token=Dxn_3qGeGF07tvtbjQeY0meHzm8mZTGx9lMjp1C1zS-YWelTurx-TC7JHBEVBAx8L1gmlJJ4mEilMznruOlzrV0Ydju3zH05ZjYkf3h3mQm95M3c_D4SPOLZpf3Dx0rxCbe9VK1WRlSpmMRhoXKjYgvQoSJagjdq50rpwRGpXzVa_qMc1-jLfNRcit1nkYctgvMEVBrOJzByDcz-p2vZic2e6bM845MpFngDGZ-N_SH1N0GMu_xoaz6tpjERNuID_Moi_rRwfP2iJfmKVIrG6jEfWY3VYP_YWsz1sX0IwASgqZC6CiaJrp1Y1s2b9ZrTA7Qn1YdxrEWF-c_l9bD3mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوری
| ترامپ:
🔻
ایران می‌خواهد توافقی منعقد کند و ما با آن توافق می‌کنیم یا به ماموریت پایان می‌دهیم
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/132331" target="_blank">📅 20:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132329">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🔴
🇭🇺
❌
قرارداد دنیل گرا بزودی با پرسپولیس فسخ خواهد شد.  این تصمیم توسط اوسمار به هیئت مدیره باشگاه پرسپولیس گفته شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SorkhTimes/132329" target="_blank">📅 19:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132328">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QMAfT7prt85PhQo-_5C7i4G-urUW6-Ig7wekM0S_qFYp3xBGjQXVd2XChW2MqyY5k7dioMHl7vdgHkTPjtREAcvUu3Y-otrLlwJS7eWpdJcUBIwTyhjdgTaRZXBWxLgacZmH-RjQgQwnzXIp1Rq0U1jXTaitRdPL4YB9MDOX6HZc9K0WXlqeZZ6aeqoVRIzao_sWeCPPcBDEPsP-0TyVNJEH4_Mm3llynuZa8PTEBrDtZmMlnOAAac4JxHKZiYJgFPrV-Dyn5pJ2EQF4P7Ymh6OY9SWXxzwNZb7bKrhWcD2TUiEnGUwGJmEDlIy3xlSfSRpr8UJKWfuNz1TT8ony6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇭🇺
❌
قرارداد دنیل گرا بزودی با پرسپولیس فسخ خواهد شد.
این تصمیم توسط اوسمار به هیئت مدیره باشگاه پرسپولیس گفته شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/132328" target="_blank">📅 19:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132327">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
حدادی : تا پایان فصل خلیلی سرپرست تیمه/با اوسمار در ارتباطم و گفته برمیگردم/اوسمار لیست خروج نداده/برای برگزاری لیگ جلسه گذاشتیم که بعضیا گفتن پول غذا نداریم و لیگ رو کنسل کنید/در نیم فصل دوم اوسمار نتایج خوبی نگرفت ولی دلیلش حواشی درون تیمی بود و فنی نبود…</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SorkhTimes/132327" target="_blank">📅 18:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132326">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
سپاهان به بازیکناش اعلام کرده فصل آینده با کمبود بودجه روبه‌روئه و احتمال فروش چند ستاره این تیم بالاست؛
🔴
پرسپولیس و استقلال هم می‌خوان از این فرصت استفاده کنن و برای جذب بازیکنای کلیدی سپاهان وارد عمل بشن...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/132326" target="_blank">📅 18:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132325">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
‼️
واعظی، مدیر رسانه‌ای استقلال: تیم ششم جدول نباید دنبال رفتن به لیگ نخبگان باشد. آن‌ها حتی در جام حذفی هم نیستند. ما حتی شانس قهرمانی در جام حذفی هم داریم. پرسپولیس فقط فرافکنی می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SorkhTimes/132325" target="_blank">📅 18:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132324">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🎙
🔴
پیمان حدادی، مدیرعامل پرسپولیس درباره اتفاقات چند ماه اخیر حول باشگاه:
۱۲باشگاه به صورت کتبی گفتند بازی‌ها برگزار نشود!
بازی‌ها باید کامل برگزار شود و در همین اردیبهشت هم می‌توانستند برگزار کنند.
امیدوارم نمایندگان ایران براساس جدول پایانی و پس از ۳۰هفته، معرفی شوند
در پرونده بیرانوند علاوه بر منافع ملی باید منافع هواداران پرسپولیس هم در نظر گرفته شود،برای بازی با ملوان به دادگاه CAS شکایت کردیم.
به هیچ بازیکنی اجازه ندادیم که سر تمرین نیاید پرداختی‌های پرسپولیس نسبت به بقیه تیم‌ها بیشتر است.
نمی‌دانیم آیین نامه نقل و انتقالات برای فصل بعد چگونه است، برخی می‌گویند می‌توانید بازیکن خارجی بگیرید برخی می‌گویند نمی‌توانید یا ممکن است دوباره سقف قرارداد تعیین کنند.
کمیته اجرایی AFC پانزدهم اردیبهشت جلسه دارد و ممکن است سهمیه فوتبال ایران ۱+۲ شود
درحال حاضر محسن خلیلی با حفظ سمت، وظایف پیروانی را انجام می‌دهد، نام وحید امیری و کمال کامیابی‌نیا برای سرپرستی تیم مطرح نشده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/132324" target="_blank">📅 17:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132322">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
‼️
واعظی، مدیر رسانه‌ای استقلال: تیم ششم جدول نباید دنبال رفتن به لیگ نخبگان باشد. آن‌ها حتی در جام حذفی هم نیستند. ما حتی شانس قهرمانی در جام حذفی هم داریم. پرسپولیس فقط فرافکنی می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/132322" target="_blank">📅 16:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132320">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
‼️
واعظی، مدیر رسانه‌ای استقلال: تیم ششم جدول نباید دنبال رفتن به لیگ نخبگان باشد. آن‌ها حتی در جام حذفی هم نیستند. ما حتی شانس قهرمانی در جام حذفی هم داریم. پرسپولیس فقط فرافکنی می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SorkhTimes/132320" target="_blank">📅 15:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132319">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
‼️
واعظی، مدیر رسانه‌ای استقلال: طبق قانون، صدرنشین باید به لیگ نخبگان برود. حتی اگر ما هم نرویم، پرسپولیس که رده ششم جدول است، کجای کار است که اعتراض می‌کند؟ تراکتور، گل‌گهر، سپاهان و چادرملو حق اعتراض دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/132319" target="_blank">📅 15:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132318">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
پیشنهاد رسمی باشگاه پرسپولیس به رئیس سازمان لیگ: حالا که‌مجوز حرفه‌ای باشگاه سپاهان صادر نشه استقلال و تراکتور رو به لیگ نخبگان آسیا بفرستید و ما رو هم به سطح دو لیگ قهرمانان آسیا.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/132318" target="_blank">📅 15:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132317">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز
🔴
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس هنوز باشگاه وارد نقل و انتقالات نشده و منتظر اوسمار هستند!
♦️
لیموچی و هر اسمی که به گوشتون خورده در حال حاضر هیچکدوم شون صحت ندارن و تا این لحظه باشگاه هیچ مذاکره ای با گزینه ای نداشته به بازار گرمی ها توجهی نکنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/132317" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132316">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
🔴
شنیدم اقای کشوری فرد گفته هیچ باشگاهی جز پرسپولیس و مدیرعاملش اعتراضی نسبت به عدم برگزاری لیگ نداره…!حالا که یک فرد دلسوز داخل باشگاه هست که برای احقاق حق باشگاه میجنگه و پاپس نمیکشه اقایان بی تابی میکنن و تاب سربلندی پرسپولیس رو ندارن.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/132316" target="_blank">📅 15:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132315">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
🔴
شنیدم اقای کشوری فرد گفته هیچ باشگاهی جز پرسپولیس و مدیرعاملش اعتراضی نسبت به عدم برگزاری لیگ نداره…!حالا که یک فرد دلسوز داخل باشگاه هست که برای احقاق حق باشگاه میجنگه و پاپس نمیکشه اقایان بی تابی میکنن و تاب سربلندی پرسپولیس رو ندارن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/132315" target="_blank">📅 15:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132314">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
وزیر ارتباطات: اهتمام رئیس‌جمهور به بازگشایی اینترنت و احیای ثبات ارتباطی، نشانه‌ای روشن از عقلانیت و ایستادن در کنار مردم است. ملت ایران شایسته ارتباط آزاد، آینده‌ای روشن و اقتصادی پویا است .
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/132314" target="_blank">📅 15:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132313">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
محمد حسین صادقی: در پرسپولیس بدشانس بودم
🔺
وقتی بازیکنی به پرسپولیس می‌آید، طبیعتاً نیاز به زمان دارد تا خودش را با تیم هماهنگ کند و به ترکیب اصلی برسد. واقعیت این است که در چند برهه زمانی از این فصل، آماده قرار گرفتن در ترکیب ثابت بودم، ولی مصدوم شدم. …</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SorkhTimes/132313" target="_blank">📅 14:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132312">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
وزیر ارتباطات: اهتمام رئیس‌جمهور به بازگشایی اینترنت و احیای ثبات ارتباطی، نشانه‌ای روشن از عقلانیت و ایستادن در کنار مردم است. ملت ایران شایسته ارتباط آزاد، آینده‌ای روشن و اقتصادی پویا است .
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/132312" target="_blank">📅 14:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132310">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
حالا که مسئولان باشگاه پرسپولیس خواستار برقراری #عدالت برای دادن سهمیه آسیایی شدند زمان این رسیده ما هواداران سنگ تمام را برای باشگاه عزیزمان بگذاریم
◽️
در تصویری که منتشر کردیم خواستار رسیدن سهمیه آسیایی به باشگاه عزیزمان پرسپولیس شده‌ایم و کمپینی به راه…</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SorkhTimes/132310" target="_blank">📅 14:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132309">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0ISr4cDgMz4tkDFpcQxuQkxIUzO0OTrHb41VfkduNnMLDduHROE0fEweh2jE7C923gfaeeEm7ap4f6OO9N2RqJgXr23YPQOHY2mUEnPXexD4DNFAvebadHvB_37x7wZLImuh9Y8EyhjpeHDJdJt03pAbUW75OMMCRl1Wwryl-vMlDqzggPO0Qfgv7sCDu77YYp3_0bfYcA0FUIe_mH5Cc2ht-TUGHWBbDWRNe87bOU-M1QxTGLN-uBD2_5rstoXxacj9pQSmjVfz3DeEWktRorrEKQh-Pu13QHR3GSH2pSOolZqg1RGzeL0xDuH05Zzfq8asQfmwVgEZW9Qjicdqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حالا که مسئولان باشگاه پرسپولیس خواستار برقراری
#عدالت
برای دادن سهمیه آسیایی شدند زمان این رسیده ما هواداران سنگ تمام را برای باشگاه عزیزمان بگذاریم
◽️
در تصویری که منتشر کردیم خواستار رسیدن سهمیه آسیایی به باشگاه عزیزمان پرسپولیس شده‌ایم و کمپینی به راه انداختیم
◽️
از تمامی دوستانی که در این حوزه فعالیت دارند از کانال یک‌نفره تا کانال و پیج میلیون نفری خواستار نشر دادن این کمپین و تصویر بالا هستیم
#پرسپولیس_آسیایی
#سهمیه_آسیایی_حق_پرسپولیس_است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SorkhTimes/132309" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132308">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCwJujpcn0iiGVjVRV1lvJpwnc6QRvFrEJ0PW2xy9FGajol1A-CPAoKk56MA7bzmANFjZhIxb5NCnP9GGiCEqngQxI7QVIldj_E5b7CEr9xM9odpROZ0TYXY6fUqsWUbi1N2um3PlxhhInQax_XaAYo7f6UJ4TWr3kx9eqn3BWqkFRao7hbTF50zIorvaHztepO7dr-7taglwwx4kEeLfG--DRY6d2M-PSHTgnk946F7cLXMd7xpv5PgDhus5SNbmRT5yBazxCK51Cbajak8x1upKaiAkk7LXPZt2ow6BgpGNNr25ntdUnmAjNFXljvUCNFYToGiarmw4VwsEEJVSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
بونوس خوش‌آمدگویی
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران جدید، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SorkhTimes/132308" target="_blank">📅 14:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132307">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
درخواست پرسپولیس از CAS
2 امتیاز استقلال و تراکتور را کم کنید
❌
پرسپولیسی‌ها سال گذشته پس از اینکه کمیته انضباطی فدراسیون فوتبال، باشگاه ملوان را در دیدار با استقلال و تراکتور به دلیل استفاده از یک بازیکن غیر مجاز (سینا خادم پور) بازنده اعلام کرده بود، از ملوان شکایت کردند و خواستار اجرای همین قانون برای خود شدند اما این شکایت در کمیته انضباطی و استیناف رد شد.
❌
باشگاه پرسپولیس اکنون و در شرایطی که قرار است نمایندگان ایران در آسیا براساس جایگاه‌شان در جدول مشخص شود، از دادگاه CAS درخواست کرده تا زمان رسیدگی به این پرونده و اعلام رای نهایی، به دلیل شرایط خاص موجود دستور توقف رای کمیته انضباطی صادر و فعلا تا مشخص شدن تکلیف پرونده پرسپولیس، 2 امتیاز داده شده به استقلال و تراکتور کسر شود.
❌
شنیده ها حاکی از آن است که دادگاه CAS نیز در این باره از فدراسیون فوتبال استعلام گرفته تا بعد از آن درباره درخواست پرسپولیس تصمیم بگیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SorkhTimes/132307" target="_blank">📅 14:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132306">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3yhx8TpqR8lOzWOcqwdqHmYTENf7tMgbpTzQd1OtuiOkpz1dFP1JdHV9GRnaQJcyqH1Z1r5cODxwZc4JrPs6LG1pltD9PoPyUfCQBXf-V34UxWURI5fPFtuGuzj7Uxrk5EwYx7nOGKvjghn5ha0Pf72lckBKxTj9-LCTa815wFYh7JTmHjTd-nIKgNHSGWjNi0juMWSHLoF4qaAc5OrbSpamXshqwZbAHeN0u5c10Z3jTf4zLvqL5GCPA2MV2K2b-daGwKN5Vogt3YQbkgbP0S11BGZ_uUoHXzDTHiEnlZu-L6_4nF7lkc4VXr8IYGx2pCv2SIQR4GnhWbYs7nj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🟢
یک فروشنده در تیخوانا مکزیک، برچسبی با تصویر تیم ملی فوتبال ایران را نشان می‌دهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SorkhTimes/132306" target="_blank">📅 13:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132304">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
وزیر ارتباطات: اهتمام رئیس‌جمهور به بازگشایی اینترنت و احیای ثبات ارتباطی، نشانه‌ای روشن از عقلانیت و ایستادن در کنار مردم است.
ملت ایران شایسته ارتباط آزاد، آینده‌ای روشن و اقتصادی پویا است .
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SorkhTimes/132304" target="_blank">📅 13:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132303">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
سردار آزمون به زودی با انتشار یک پیام عذرخواهی به تیم ملی بازخواهد گشت.  #خبرنگار_فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/132303" target="_blank">📅 12:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132302">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
ایسنا: مهدی لیموچی در آستانه پیوستن به پرسپولیس قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/132302" target="_blank">📅 12:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132301">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
طبق برخی خبرهای ضدونقیض؛ تندورهای حکومت فشار زیادی آوردن تا مجددا اینترنت بسته بشه و هر لحظه امکان داره این اتفاق بیفته. اگه کاری مهمی دارید سریعتر انجام بدید. چون هیچی قابل پیش بینی نیست.
✅
هنوزم بسیاری از آی پی ها فیلتره و اینترنت اختلال زیادی داره.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/132301" target="_blank">📅 12:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132300">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
باشگاه با یک بازیکن از سپاهان به توافق نهایی رسیده و این بازیکن داره فشار میاره که با این تیم فسخ کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/132300" target="_blank">📅 12:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132299">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
علت کندی شبکه اتصال زیاد است به مرور پایدار میشه
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/132299" target="_blank">📅 11:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132298">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
مهدی هاشم نژاد وینگر ۲۴ساله تراکتور:فکر می‌کنم خط خوردن من ترور شخصیتی بود. دوستانم در تیم ملی گفتند که خط خوردن من برای آن‌ها باورکردنی نیست.بعد از مصدومیت قلی زاده همه فکر می کردند فیکس باشم اما دعوت هم نشدم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/132298" target="_blank">📅 11:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132297">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
مدیران باشگاه پرسپولیس در روزهای گذشته با ایجنت پوریا شهرآبادی ، مهاجم جوان گلگهر جلساتی برگذار کردند و خواهان شرایط جذب این بازیکن شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SorkhTimes/132297" target="_blank">📅 11:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132296">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
شهاب زاهدی که به تازگی بازیکن آزاد شده؛ تمایل دارد به پرسپولیس بازگردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SorkhTimes/132296" target="_blank">📅 11:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132295">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
✅
مهدی لیموچی در آستانه پیوستن به پرسپولیس قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SorkhTimes/132295" target="_blank">📅 11:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132294">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
نماینده محمد امین حزباوی امروز پیشنهاد مالی‌ مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SorkhTimes/132294" target="_blank">📅 11:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132293">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🟡
فسخ لیموچی با سپاهان؟
▫️
به احتمال فراوان مهدی لیموچی به دلیل عدم گرفتن دستمزد خود در سپاهان با این تیم فسخ خواهد کرد و مقصد احتمالی وی پرسپولیس خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SorkhTimes/132293" target="_blank">📅 11:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132292">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUloY3JXyLqWsHwITOmOd6PuUSbnN69mYv1Im3fa_hUhE6w73Y0mT8TXLtOKw8y84dD4SFwkkWz5pZMubrFgUsPMfa51PIgylNQ6WqsVuvMlnXH1auMo8-BWGtNkEMoesVfytqIHBtPWX6suCrz4QdM4jn7FOX5mcTBZmQ4_kF1MDJCy81fbUC7qSoKWfEgeoWeqmhXfiawmmwhIW4BBERq5HlrxQHg-8H1p_1kKeIJuJfV4dgbkkj4UjhlRWD38_ag1E0KR7s8l6WdRYoE0a9yB9-DR2EyptkSAv7qV_O-6ONb-p3hu1iFv9kv6txCPPitSfjXzYjQSOTgx3_h9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهاب زاهدی که به تازگی بازیکن آزاد شده؛ تمایل دارد به پرسپولیس بازگردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/132292" target="_blank">📅 09:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132291">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷
🇮🇷
جهانبخش نزدیک به یک‌ماه است که مصدوم است!
⚪️
مصدومیت علیرضا جهانبخش فعلا مرتفع نشده و این بازیکن فعلا امکان همراهی تیم ملی را ندارد. این در حالی است که 23 روز از مصدومیت جهانبخش سپری شده اما این بازیکن همچنان شرایط تمرین ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SorkhTimes/132291" target="_blank">📅 09:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132289">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnqMl3ERlSAN7OGg4aFX8EUadBIYccyHOh51utLmyv_O1A6SGAubmuUXuamJywbqVcAAS30QJ0BlXcsnVprCPY0RdfzD6HHQBcK0e-RGQuupsHoYheK9rsnrw3MCzMmUwFiq3dGVjW4Q22W5O-eHMFLZ3qP4VJ15rgeJ_K9GsG4JGCHRjaIZqUu3GmoTsnG1rALRDPkSGOylIM7Z9diFefRB5Gz9232oW8TLUV6ylx7zQCrd5Q8DUw7L9g1K74pyZsDEhgFn-Bp0na1ak6fmiR-PFflSgv5tWQh-VkJumnIaMn4xdwyG2k0yNNR_omQ778LBGu22bjxevnsQdDmqLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت فعال شد!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد سایت وینکوبت شوید:
👇
🟣
ywincob.com
🟣
ywincob.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/132289" target="_blank">📅 01:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132288">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‼️
کارشناس صدا و سیما : وصل شدن اینترنت متوقف میشه و دستور رییس جمهور اجرا نمیشه چون خلاف دیوان عالیه.
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/132288" target="_blank">📅 01:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132286">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b15265d538.mp4?token=erbsOq1oiH_XkB3WvF7ZlJLdbR0B52J7j79N-CpSdKbCzbtWVNUO_ib_U0dqoU3tw5QcAfQGSwgkjFShkUQPjgDKKpjSy6yRgAm9vVsd_iGefrMwpB0iySBpTGUACJ0oQ7Sqx8GWQh0YP3E0EtphLLCIR5V_u3kCXSEUCQThMolo2PfbothviGCOIt5K51P1llcHE37V6GvIlnfyu0--3fl7zmsNkE-nmy7O5cmPXR7MfksQU2tJJRY5sQ7XbWILg6plkVlBaBg4N_zuRlaTXNZwuCQHfbBau9gmwF7PQ8i9QQk7a1lPIq3Neh32X4fxoUShzf0s6A_LlKGSqod8ew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b15265d538.mp4?token=erbsOq1oiH_XkB3WvF7ZlJLdbR0B52J7j79N-CpSdKbCzbtWVNUO_ib_U0dqoU3tw5QcAfQGSwgkjFShkUQPjgDKKpjSy6yRgAm9vVsd_iGefrMwpB0iySBpTGUACJ0oQ7Sqx8GWQh0YP3E0EtphLLCIR5V_u3kCXSEUCQThMolo2PfbothviGCOIt5K51P1llcHE37V6GvIlnfyu0--3fl7zmsNkE-nmy7O5cmPXR7MfksQU2tJJRY5sQ7XbWILg6plkVlBaBg4N_zuRlaTXNZwuCQHfbBau9gmwF7PQ8i9QQk7a1lPIq3Neh32X4fxoUShzf0s6A_LlKGSqod8ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوری
| نورالدین الدغیر خبرنگار الجزیره در تهران:
🔻
همه چیز انجام شده، چیزی باقی نمانده جز امضای توافق
‼️
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/132286" target="_blank">📅 01:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132285">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVbodx38nTAVJJsThE0zWqDBM79I11bjU1wwSwq9ffWrowS--4qL8MXKNSvQx1_6MJpvibLSmxXZ5LGoT4b46kj_fAjzqNxLr2h8k7wQ6lUVzXZ-sJezLAgEpbEz4P4RJwMJF4vMG1DdQc4wsClHbQ1o1sKCTh-VPEnpHeIEVEZZwNQwZGX6Fpb-aQzvVFUPqxJYaBsI8KQuBQQBBlGtPha47p7eyBa3ibzfc8CbjM4WEdKjvhzq1OaicfG-TSgNpvNmWTip4oScGt1aaQMO_emlkAITAYEH17OdAk3gtewSJKsfOaRa4vYlp-masNu7_4XaBf5Gf_1MNRZt_21mLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🔺
فیفا اوکی داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SorkhTimes/132285" target="_blank">📅 00:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132284">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔹
سهراب بختیاری زاده فصل آینده نیز سرمربی کیسه میماند
😍
✍️
خبرگزاری ایران ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SorkhTimes/132284" target="_blank">📅 00:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132283">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
با معرفی نمایندگان ایران در آسیا؛ پرسپولیس شکایتش‌ را به فیفا می‌برد
🔴
به دنبال معرفی نمایندگان ایران در فصل بعدی رقابت‌های آسیایی، باشگاه پرسپولیس اعتراض خود را در این خصوص با ثبت شکایتی به فیفا خواهد برد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/132283" target="_blank">📅 00:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132281">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❗️
سرعت اینترنت در زمان قطعی بیشتر از وصل بودنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/132281" target="_blank">📅 23:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132279">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🟥
فروش سیگار
به صورت نخی ممنوع شد تا
جوونا دیگه راحت به سیگار دسترسی نداشته باشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/132279" target="_blank">📅 23:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132278">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❗️
اینترنت سراسر کشور وصل شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SorkhTimes/132278" target="_blank">📅 23:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132277">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
شایعات
🔴
مدیران باشگاه پرسپولیس با درخواست ویژه اوسمار با مهدی هاشم نژاد ستاره تراکتور وارد مذاکره شدند
‼️
قرارداد این بازیکن با تراکتور به پایان رسیده و هم اکنون بازیکن آزاد است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/132277" target="_blank">📅 23:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132276">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
نت بلاکس: اینترنت ایران کامل برگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SorkhTimes/132276" target="_blank">📅 23:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132275">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🟥
تیم ملی ایران برای هر بازی جام جهانی فقط چند ساعت ویزای ساعتی آمریکا را دریافت می‌کند و بلافاصله پس از مسابقه به مکزیک بازمی‌گردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SorkhTimes/132275" target="_blank">📅 23:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132274">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
یک بخش از صحبت مهدی تاج اشتباهه.
🔴
اونجایی که میگه اگر‌ کمپ تمرینی تیم ملی به مکزیک بره، مشکل ویزا حل خواهد شد!
🔴
ربطی نداره!
🔴
شما کمپ تمرینی رو به موزامبیک هم ببری، برای برگزاری سه مسابقه باید وارد خاک امریکا بشی و در نهایت به ویزای این کشور نیاز داری.…</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SorkhTimes/132274" target="_blank">📅 23:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132273">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‼️
الان چیو دقیقا وصل کردید؟! مردم ۹۹ درصدشون قطع هستن…!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SorkhTimes/132273" target="_blank">📅 23:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132272">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
ارزش امیرحسین محمودی ستاره ملی پوش پرسپولیس به 500 هزار دلار رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SorkhTimes/132272" target="_blank">📅 22:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132271">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
به روزرسانی جدید :  اتصال مردم به اینترنت بین الملل به ۸۶ درصد سطح عادی رسید و در حال افزایشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SorkhTimes/132271" target="_blank">📅 22:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132270">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نت بلاکس: اینترنت ایران کامل برگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SorkhTimes/132270" target="_blank">📅 21:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132269">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paZN5zfcpTE7Rvsd-QdxwKPmjLzObUNyc0DPiPAikmee_apw14NahT5tGsiUvYF90yaUQNbUtJCw6Ea4Yw4iQ0vLFCJiPn-FO9n-mwDPRzl4DvVgDZjoNgk8qGK-LbeRLaJGCH5a4CRFP2Qv0y0QeMtoAyNXwCDEaYu9eXmUBf_8dYhsMdxb4VLlE2FDpg6bIcWYvq1cTH0mlPx8CwMutoqDCrD5ACtbUk2fv-axIFBo76Fzs4J5YQ6idYA6fvYQmL5ly0mkR5b0smXz87CQhitQWWxk6KSIZvCuzSqIFW9-tJacIuPKvkL085aWmtRzDOSgPJO0jHSM7UpH-P8wVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نت بلاکس: اینترنت ایران کامل برگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/132269" target="_blank">📅 21:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132268">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRlVGSHjRio9aoqLigDYRZtcZJJI-Lm8N7-Lhhqwwny1wxYFcvzs_rtRHzR9gqBJCrEdLFnQg-lLfXpmFLvhdpy1w9K9Q2CpBmocOVf02Kfjfp_WYvY-2hTCS4XY5VSobjtc-yfxRizbkoO6K8JcYUo25uB14Jk_V-4UES_6AWMTbSxUzzBy_NQUCRfIHXMcW2lusx42nYPzor1N2bl5x0JyUx7R0MqbQZ5SUjwFfKDbA_J4gbjzvRx1t64NHWPmzpi9vKq0pwY5dLbAk1hWhc9O-ym_AxjWvXOZH4w4rG8BjYOBD-uVuZwwd62MS2yMEmIZ1f0rM1vzSARRX-rn9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی سریع و مستقیم به وینکوبت
🟢
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی انجام می‌شود:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🟢
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/132268" target="_blank">📅 21:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132267">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✅
💢
🇮🇷
🤝
🇺🇸
📰
الجزیره به نقل از یک منبع آگاه: میانجیگری قطر به توافق آمریکا و ایران بر سر دارایی‌های مسدودشده تهران منجر شد!
🚫
به لطف توافق بر سر این موضوع که برای ایرانیان از اهمیت بالایی برخوردار بود، احتمال قوی وجود دارد که توافق میان آمریکا و ایران فردا اعلام…</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SorkhTimes/132267" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132266">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
وزارت ارتباطات:
🖍
اینترنت گوشی های همراه هم تا ساعاتی دیگه وصل میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/SorkhTimes/132266" target="_blank">📅 20:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132265">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‼️
‼️
وضعیت اتصال اینترنت بین‌الملل کشور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SorkhTimes/132265" target="_blank">📅 19:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132264">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8VA9oTbArCEEWWeO3DGWWMISC5ysbr4DYwoSK8zoPtGmugzGVfZFR74slllB3TMVZ55sTOBWLllRD98smpLU6p9gBWT0c5rsE5t-1jce4sSkv2oqJzkyknOCGcbxflIgBMGwWttk8qmMT7Yda4jfAWhKgFl6j4UH7fMoTNExVIXFUD-9VW6G1KpzuvtKPU8mo8fmmF5Plxrx54vik2IDNDUf1n6ZnFTiYPDHzMBs9sHIyJasWL2vsRLivoR41gMAa8lvcQHQ5ge6w2dHwrDeHfSd6VNhgot5AvsUBpDoe3J2U2EarV4rQY7cuIBciuNDGUtxL8GRP0nLgdcK89DOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‼️
وضعیت اتصال اینترنت بین‌الملل کشور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SorkhTimes/132264" target="_blank">📅 19:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132263">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔽
وزارت قطع ارتباطات:اینترنت همراه، امروز (سه‌شنبه ۵ خرداد) وصل می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SorkhTimes/132263" target="_blank">📅 19:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132262">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
تسنیم : یحیی گل‌محمدی به جز باشگاهای عراقی یه پیشنهاد مالی خوب هم از تراکتور داره و ممکنه بره تبریز!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/SorkhTimes/132262" target="_blank">📅 19:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132261">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSoKfFxq70pJuoEkpBooK7rrdWBRBR1Fh-m6_HfO2uN-GQGKgFKs1Ti3Ic8r05uUKfCwig4a2TyccFJogzQbJNR_mbwaWnO0ZRBRRSKR_M_Cay5TViyupePFq2JBbkHLlo8_SW7I4-2PrxOdi3t2KRBuFHp2AfzDO0gdKslu7diL0yMg_cII_2ovWlwPCZExWComBEbsrC24o6l-kZpInxdLhThL2q5ZZsN8FIwSIQ3Iaf-9xY61GFHJHM1sTC27UwNGPoKCiMzalbFRWUCobMqlyElsDTgyQypDfbKk1UuqmcSd8Hvc5wnL54P5hPP5i_PcetSaEcWiot1onqiC7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شایعات
🔴
مدیران باشگاه پرسپولیس با درخواست ویژه اوسمار با مهدی هاشم نژاد ستاره تراکتور وارد مذاکره شدند
‼️
قرارداد این بازیکن با تراکتور به پایان رسیده و هم اکنون بازیکن آزاد است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SorkhTimes/132261" target="_blank">📅 17:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132258">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
پس از ۸۸ روز قطعی و ثبت رکورد تاریخی ۲۰۹۳ ساعت انزوای دیجیتال، نت‌بلاکس لحظاتی پیش تایید کرد که اتصال اینترنت در ایران در حال بازگشت است.  وضعیت فعلی در یک نگاه:
🔹
اینترنت خانگی و ADSL: اکثر شرکت‌ها وصل هستند.
🔹
اینترنت TD-LTE: ایرانسل و مبین‌نت وصل شدند.…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/SorkhTimes/132258" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132257">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
تیم فوتبال دهوک عراق به یحیی گل محمدی پیشنهاد داده اما یحیی میخواد تو ایران مربیگری کنه!/فارس
🚮
امپرور جان لطفا هر گورستونی میری طرف های خیابون شیخ بهایی آفتابی نشو…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SorkhTimes/132257" target="_blank">📅 17:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132256">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
دوستان از برخط به online شدنتون مبارک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SorkhTimes/132256" target="_blank">📅 17:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132255">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
دوستان از برخط به online شدنتون مبارک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SorkhTimes/132255" target="_blank">📅 16:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132254">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
خوشحالیم که دوباره آنلاین شدید
❤️
🔴
خوش برگشتید؛  امیدواریم تا شب دیتاسنتر ها هم متصل شوند تا کسایی که وایفای خانگی هم ندارند به اینترنت متصل شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SorkhTimes/132254" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132253">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
نت بلاکس:
🔻
نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/SorkhTimes/132253" target="_blank">📅 16:39 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
