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
<img src="https://cdn4.telesco.pe/file/uhDvF0Gd3UEBtEBFl4Yp7Sh3i_muUp38zvdlXLEKhGwsCO4Ia8JfvG34n7f23tFfktpfRgkygpIhV9EDe_JocDXI037w3kc47LmuKryf5dRDQh6pRb7vApZMvyt9YWo7sTaQ3B4Le138NoBtqwFFM04DJ0-y_wx8KK71UMidxZ38dfLtUAVygO2-GAfzrMxg-IJEWKMp4Bv-o03ShPmVM3v-U9REKx8EBRwDZJcHkXLRwoDflmxT852VRvjgKHrAONAnk_15mMLOvMtILUjhDlz8jxqEL_2-er1RINOdbdc8KpLlMrtAjQEgKg0kCvB4lUzADkKyMbtWlCgTZyXukQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.3M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 13:40:51</div>
<hr>

<div class="tg-post" id="msg-672545">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
حمله جنایتکارانه آمریکا به آب‌شیرین‌کن بونجی جاسک/ ۲۰ روستای ۱۰ هزار نفری بی‌آب شد  مدیرعامل شرکت آب و فاضلاب هرمزگان:
🔹
آمریکا در حمله تروریستی به آب‌شیرین‌کن بونجی در غرب جاسک، ایستگاه پمپاژ و ترانس برق آن را تخریب کرد. این تأسیسات روزانه ۳۱۵۰ مترمکعب آب…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/672545" target="_blank">📅 13:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672544">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
رویترز: کویت یکی از بدترین شب‌های خود را در حملات تلافی‌جویانه ایران سپری کرد  رویترز:
🔹
کویت یکی از بدترین شب‌های خود را از زمان آغاز درگیری‌ها در خاورمیانه، در جریان حملات تلافی‌جویانه ایران سپری کرده است.
🔹
در جریان این حملات، دومین نیروگاه تولید برق در…</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/akhbarefori/672544" target="_blank">📅 13:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672543">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ارتش اردن حمله به این کشور را تایید کرد
🔹
ارتش اردن از حمله پهپادی به این کشور خبر داد و اعلام کرد که چهار فروند پهپاد وارد حریم هوایی اردن شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/672543" target="_blank">📅 13:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672542">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mC6ZSwtECfEIgawxkg2FvDkbZVo3w0p9EjY0VTLrkj4563TKOWoX25XPh2TuXfoUQoo8Z24B0Hx3FnZBWkk54pRKOFaN2qW_ZKASHGXQzvdNFHRjCefHhGu_P2svfeqdWtS0LP3__17VNIGASMsSwqvGkxWLLLdcq7-Ac1UoRBO0fGiAivQ6C4NuNcaEBcScd8suUYG-KbOHvPTFr-ZOt5sk6rB-g1jKvDUFwjvkpQfej102pZYvyD4kdXkuCADZlzY10Mo3-TYNVphSToRluCPF4a30EDiXfPPfvZwW5_dsf-5wdZbtQy0QtOyp-iLedKPwdqSxFE9uuXF8xW8xIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طعنه نماینده کنگره آمریکا به ترامپ
🔹
توماس مسی، نماینده کنگره آمریکا در واکنش به ترامپ که گفته بود ایران، روسیه و چین در انتخابات ایالات متحده دخالت میکنند، نوشت: «چه زمانی شاهد سخنرانی [ترامپ] درباره‌ی دخالت‌های رژیم صهیونیستی در انتخابات آمریکا خواهیم بود؟»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/akhbarefori/672542" target="_blank">📅 13:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672541">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
برخی منابع خبری از شنیده شدن صدای انفجار در کویت و اردن خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/akhbarefori/672541" target="_blank">📅 13:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672540">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
امتحانات دانشگاه‌‌های ۳ استان جنوبی مجازی شد
وزارت علوم:
🔹
امتحانات دانشگاه‌های ۳ استان هرمزگان، بوشهر و نوار جنوبی سیستان‌وبلوچستان به‌صورت مجازی برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/akhbarefori/672540" target="_blank">📅 13:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672539">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
۲ آتش سوزی در کویت در اثر حملات ایران
🔹
سازمان آتش‌نشانی کویت اعلام کرد نیروهایش در حال مهار آتش‌سوزی دو نقطه در پی حملات ایران است.
🔹
یکی از آتش‌سوزی‌ها در یک تأسیسات نفتی رخ داد و در جریان عملیات مهار آتش، چند آتش‌نشان و یکی از کارکنان این تاسیسات مجروح…</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/672539" target="_blank">📅 13:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672538">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
حمله هوایی رژیم صهیونیستی به جنوب لبنان
🔹
منابع خبری لبنان از حمله جنگنده‌های رژیم صهیونیستی به منطقه النبطیه الفوقا در جنوب این کشور خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/672538" target="_blank">📅 13:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672537">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
برخی منابع خبری از شنیده شدن صدای انفجار در کویت و اردن خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/672537" target="_blank">📅 13:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672536">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hF9G99nnS94uRXLsjmJ2J6OZyRxC_V94dHlu2B_9ov9z8YWB5qFRN5VKj_J9OMt7aF-xgqiQQYKuTF8g1AD_ZkcXlDWok6bqkXPREjOlwLz_uOGZa9IalxFgGpWdbYC_8bhFYtRr1fIs_t7E-BBmf2tTliEFOJ4931Kz_t50igJIfXtqjqXgdGZ0Dcaa7_I7pJG45elLEU1sWhLfHUmeIAP5tKhqC7395hDfu6tR1qZa5FkcuyZ0-rIEG3KtXZC23bw2pA43Q2tv4UZRI_hi9NhSIcCkiBRw8OoDBtzqmLA-hiotGp0Laor5WRiH8ux15IrUl88o8kg06675qHD18g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام گروه سنی ایران بیشتر در بازار رمزارزها حضور دارند؟
🔹
آمارهای منتشر شده در گزارش دوسالانه نوبیتکس نشان می‌دهد که ۳۵ درصد جمعیت کاربران این صرافی در بازه سنی ۳۱ تا ۴۰ سال هستند.
🔹
آماری که نشان دهنده این است که حضور در بازارهای رمزارز عمدتا توسط افرادی انتخاب می‌شود که در دوره ثبات مالی و شغلی و اوج توان تصمیم‌گیری اقتصادی خود قرار دارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/672536" target="_blank">📅 13:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672535">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
حمله پهپادی به اربیل
🔹
انفجارهای شدیدی در استان اربیل شنیده شده و همزمان اعلام شده است که یک حمله با پهپاد، این منطقه را هدف قرار داده است.
🔹
هنوز هیچ مقام رسمی عراقی درباره ماهیت این حمله یا عاملان آن اظهار نظر نکرده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/672535" target="_blank">📅 13:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672534">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
یک پایگاه آمریکا در کویت، همچنان در آتش می‌سوزد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/672534" target="_blank">📅 13:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672533">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر خارجه عراق: الزیدی به دوحه و تهران سفر می‌کند.
🔹
کپلر: برای سومین روز متوالی هیچ نفتکشی تنگه هرمز را ترک نکرده است.
🔹
سپاه حضرت سیدالشهدا(ع) تهران از اجرای عملیات انهدام مهمات عمل‌نکرده در شهرستان پاکدشت خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/672533" target="_blank">📅 13:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672532">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
گوگل با هوش مصنوعی یکی از گل‌های خاطره‌انگیز پله را بازسازی کرد
🔹
هوش مصنوعی گوگل موفق شده تا یکی از خاطره‌انگیزترین گل‌های پله، اسطوره فوتبال برزیل که هیچ ویدیویی از آن وجود نداشت را فقط با توصیف افرادی که آن را دیده بودند بازسازی کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/672532" target="_blank">📅 13:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672531">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده جاسک: آمریکا‌یی‌ها زمینی بیایند با تابوت‌هایشان برمی‌گردند
عبدالکریم هاشمی، نماینده جاسک در مجلس در
#گفتگو
با خبرفوری:
🔹
زدن راه‌های ارتباطی بندرعباس، حمله زمینی نیست و دشمن می‌خواهد ارتباط بنادر و دریا را با مرکز قطع کنند. احتمال حمله زمینی را رد نمی‌کنم و اگر این‌ها پا به عرصه خاک ایران بگذارند، باید انشاالله تابوت‌ها را به آمریکا برگردانیم.
🔹
هر راهی که زده شود، راه‌های جایگزینی وجود دارد و انشاالله به مشکلی بر نمی‌خوریم و ترمیم خواهد شد. اصلا نیازی به خارج کردن مردم بندرعباس و اینگونه اقدامات وجود ندارد و راه‌های جایگزین برای خدمات، کمک و پشتیبانی وجود دارد.
@TV_Fori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/672531" target="_blank">📅 13:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672530">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
موج نام‌گذاری نوزادان به نام ستاره‌های جام ‌جهانی
🔹
صدها نوزاد تازه‌ متولدشده در «پرو»‌ به نام ستاره‌ نوظهوری مانند «ارلینگ هالند»، مهاجم نروژی، نام‌گذاری شده‌اند.
🔹
نام‌هایی الهام‌گرفته از اسطوره‌های فوتبال، مانند «لیونل مسی»، «نیمار» اهل برزیل و «کریستیانو رونالدو» اهل پرتغال، هر کدام حدود ۳۰ هزار مورد ثبت شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/672530" target="_blank">📅 13:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672529">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fj0jNGtZFprJJO3BlRNxRgDnNbnwTkzmxUFlNqUaXWHjIqhTCl72fLnfaOF0brzlqO0H8zz632IloaRHZjMQsCOYDJZ9BRnYpV7NsVhUqyFwQxErQUHcMk_aEM39siZdH757i67KJUiRZADAh77pGXJLAHoiEb2F0slgw9M-2Z_b4vL0a2lS6A4KFTtR5WOwkN1rRrktETNq-zScI4Eam40s1W_0qqb-4nzrY9rCvPjz5SXH0UVb-HU5o31kFFwHXcnI5TQpSR1OQibRCENL_DZcefGRejZGn8n2pcr9CTysv-xTXT_VbaV0_3zRA3DYjDacKTyAEJBaJECr9SgBRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چگونه ۳۴۰ نفر در دوره مدیریت پیشین کیش‌ایر در این ایرلاین استخدام شده‌اند؟
🔹
پس از انتشار گزارش‌ها و نامه‌های سازمان حسابرسی که از ابهاماتی در مدیریت قراردادها، کنترل هزینه‌های مشاوره‌ای، اخذ تضامین، رعایت ضوابط معاملاتی و انضباط پرداخت‌ها در دوره پیشین حکایت دارد، اکنون موضوع استخدام گسترده بستگان، آشنایان و معرفی‌شدگان مدیران و برخی مسئولان در بخش‌های مختلف شرکت نیز مطرح شده است.
🔹
بررسی اسناد موجود نشان می‌دهد که در دوره مدیریت پیشین کیش‌ایر، هم‌زمان با خروج یا منفک‌شدن حدود ۳۶۰ نفر از کارکنان، نزدیک به ۳۴۰ نیروی جدید به مجموعه اضافه شده‌اند؛ جابه‌جایی گسترده‌ای که به گفته برخی کارشناسان، نیازمند توضیح درباره منطق مدیریتی، فرآیند تصمیم‌گیری و معیارهای استخدام است.
🔹
اکنون مهم‌ترین پرسش این است که آیا جذب نیروی انسانی در آن دوره بر اساس نیاز واقعی شرکت و معیارهای حرفه‌ای انجام شده، یا روابط و معرفی‌های غیرسازمانی در تصمیم‌گیری‌ها نقش پررنگ‌تری داشته‌اند؟
مشروح خبر
👇
https://B2n.ir/fd6213
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/672529" target="_blank">📅 13:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672528">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
آغاز پیش‌فروش بلیت اتوبوس اربعین
🔹
بهای بلیت مسیر تهران به مهران برای اتوبوس‌های ۴۴، ۳۲ و ۲۵ تا ۲۷ نفره به ترتیب یک میلیون و ۲۵۰ هزار، یک میلیون و ۷۰۰ هزار و ۲ میلیون و ۲۰۰ هزار تومان است. نرخ بلیت تهران به شلمچه نیز به ترتیب یک میلیون و ۳۵۰ هزار، یک میلیون و ۸۵۰ هزار و ۲ میلیون و ۳۵۰ هزار تومان و برای مسیر تهران به خسروی به ترتیب یک میلیون و ۱۰۰ هزار، یک میلیون و ۵۵۰ هزار و یک میلیون و ۹۵۰ هزار تومان تعیین شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/672528" target="_blank">📅 12:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672520">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mjRrW3KgiJLt6rzKz_IjQzB8LiXxbw0tq7HjZeWzTMLEXx4D6R8rU1-S9kbIhszEvfRw-O2vgCRwFECfkvKLi6lSWPMeiz7Xe5P3Ha-IdeFqvZXSVvMNPc19ejt7ds9nPXydYI-mngdVlDfSw6Bo5EH-6AQGRNVxwXm30DxdUo3KpxOerYRGkXzwuo3fekDULXC0Qe31RzN5mhhb1x-lXx-6ufyUcFS42I-IUW66xhVDMzLhXSIpS6G5Eu-T2MGu3www70yRetR79QWqLBbtoyVSot6kIqJ9zr5TUhjbJJ_Bj5KX4gvD5BUSGlM8jLA8sP4LVfLoBlhSJGdfR2gRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4U6_tIB0V98zzaunOKdYRgJTuzYZHXcw0mNSj4m-wHoWi8IcftvDfOEdZBJYzY1PwJ2KwI9t27p_ZXqi3EP1I6SsQ2ojbUIp-0cT_eGSGl-5IdT3S5RkV4AXEYsHtsyta9PzYVlfuLLfMTiJoR_biwAliC_xOfbvsPM9Eyepv7Pk8TGWTEPyVz6WQG_xbs2H8ZzpYGi9R6iEfkAZCJaadWjbXSglZQUQ5rxN2JmRFDGa4Zp4cdVKqBU0QTzZTXspidYCcw2Ich0xKM_c0C24_zGrjJ4lB7_CH2Jm4CXL0CN3E7NgZnCGDmZTSumSn3S5vYhoixxTcokZRnWWQ_nGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kD1L-lb75V6qlOP2P-cpSjLSzGa9cFwYvk5Vp_GfTuNhVrQddMlRESUfvZwkrzm0Z6A78X7-5JO5wdVi3tRAQpbt2ZHHQZHxJXm-3wt_uYD2hqTN2JTuSMCpqaq_yJDZVn8oZQQXoEKa5u0jMJlxUA6gFS0n916r75Acs-tPqMyq2Uin3G7p1eSkmAwyde5bY6ay3XkXbDsx-q1KFww0qgMgFZkPR9s0soE6mdWBHodcSg5lfy4PI_GPDxmgxcLBaWEwFdx8UFCGJCqxwl5xqIjY1C0F9no30-tWagM8numJ6SIv2XTM69tUWO9NzIEUw3hp_gddhLtYJNz8hr2Bnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phZVUd5V9HGi3R3Qg4XLJoVTzakJVBovohpOyzoWuQqG2DPhBA5niUeImYrJJxIAQjI6vNWwhJoLP553GcG_coDL2ejnGVg7JjNp_tqq4LelJxfkmj8h7N3STfxf6PQCy-RY2jGPKIKtEbMWWWNtOXQU3mAsHrSoKSfbrp_qzAcRcgSQFDoAkVcWSm9Vs6IJoECHYdd4c7vvMV32lwouKJZh16u_uXIDskcXkAAJVVnlGPd3e6BnlIsRti0yjNjl7hhCmmVTyAaTi-w5Ev3NUSGhcM5U9L971EJg9XnsFVPk5oHEhvP0zwfuAc9c16tZuGkcPnW3SnhdTZ8-cwkPiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tBryRxvwHghYdIjHTTK2056VU1ZpCpO5f05A2bGV30VOZZzXIJOvgwNgoioRFphLRCpXEu54NCadGO0B0gxwy00Zu9tBO4oQkno2ad9r4-gLhF9KcpkjMQugYu-t-Af4BzwJQRCrgYfVh56vFExyd4IlLo70Hk84jgDk4gKZcobGWKLamJAUNAEKP2N-qsMv1vytq0_XhSzIxWIB16wJF0w4znc188o_AsU0Fn7QHZHKcrmjgD-D2QTxZOQrUXi_Vhnd6IQdkwZWLgVVdkJxcLoU20_MO5cvvcD-Y3AGRkGVWYGpWxjUrkcrrhEHyHStbW0tsl4k7v-x7I-gFq9GOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tiBfiReZYPRvmr3bvm_hPHOXsGShe4oXoyUxfUIrl757JJ7wWeY4aeNoS6GSvHzfbQH9AQxZ3GlV8JoML8LueSlHXr5yT89azS8TElJsVgOTu1-3zqwMRk4QpFsv6KevKospJQwdTBqQ_NrMpUSTell1klgg0xBh1xPa-msrNfJIoeOeLqDePdfATMvxRIEwguZkg8qnWjnOmAeQ8AJjH_FSsJYspYxLEH1DZLbj8HW1KieiJi4c8t1qojYGdB1cbUK-AeqsDe6Ol7OpM2qfK7aBxkW3hzqAbUOIBp3nZjQMXyLj9JQn6kTOZ3nmUg9TBIsQ1DBNz3OP5S_wDJl5iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q9pMiAbzv69hwHglLgkk1uC6uO9IFnoL31WYBMzADvBmkAMlhhYi-gsiiVOMCX_E0HY7uzXhvUwKhdkkaGandkr_HDo2WnUooc62GWgtvcmnZmlFTR-5GHa1fuFr6OE9k8meNHdW6HCgAtKFOVy_DLKIv7IBr6GQje401vl-lqh9rdfQjHTu5whjeAjMZMad297HZaNtqVvs3v_0-TH5c38IHu13omsAiOTn36HDGyNNI2rDu-b-qVY3uV4XB4DGlX8F88OaUI9EdooMG_EHsumLjZsp4VKF6hKyFMWmMqcuuCm-IB5c4wkVrFpbV95EWfkB3UAT6iRUjIhYtQ3zVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJTJX644fwwCfomfRM6UFjJ964nIA2tbKvSZsqH58FEjBlX0d-sIJftMG2_XR5RVSyl_qOerW7UhJv12UafpO-WQVy3ZTGz31169WBxsBtV8BUbDRr1ow5e9AR-KBp38L8srXC-dYT90O6eE2PDHGWDIIecUloJExOtCtJl9V_dYvDLoyETseBrVWua9ePvOSouj6PYLjcHnZlq9wFhYfJ6T69_uiR8LpEF9Do6V2OO2arzhHHcTOemHiLeQPdNSgrW-QSFDgFlIk2IIqclIaBooQtlKzHKyTiRKZ7R51jHbwSBWnMFkdlGkAn3th6BuTBK4r6Hy6g5A_Lbprm5YVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وضعیت پل محور بندرعباس به رودان بعد از حملات دشمن آمریکایی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/672520" target="_blank">📅 12:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672519">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
اتاق تهران؛ مشاور کسب‌وکارها در مدیریت نقدینگی و عبور از بحران
🔺
اتاق تهران با ارائه مشاوره تخصصی و رایگان در حوزه مدیریت مالی، به بنگاه‌های اقتصادی کمک می‌کند با مدیریت جریان نقدینگی و اولویت‌بندی هزینه‌ها، تاب‌آوری خود را در شرایط بحران و پسابحران افزایش دهند.
برگرفته از ویژه‌نامه آینده‌نگر «
نسخه سخت‌جانی بیشتر
»
👈🏻
کسب اطلاعات بیشتر: ۳-۸۸۷۱۴۴۷۲(۰۲۱) و
www.tccim.ir</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/672519" target="_blank">📅 12:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672518">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
تحلیلگر اسرائیلی: ذخایر موشکی ایران به قبل از جنگ نزدیک می‌شود
🔹
تحلیلگر برجسته نظامی و امنیتی کانال ۱۳ اسرائیل معتقد است جمهوری اسلامی ایران در زمینه احیای توانمندی‌های موشکی و پدافندی خود،‌ موفق عمل کرده است.
🔹
آلون بن دیوید با بیان اینکه بخشی از روند این تولید تا به امروز احیا شده، پیش‌بینی کرد که ذخایر موشکی ایران به میزان قبل از جنگ اخیر نزدیک می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/672518" target="_blank">📅 12:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672517">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df6dbe7790.mp4?token=MTdjaGjuIaRQfVcztzWGVGJpbiB5LkOjQeioE4QOAQ-YZl61yr80d5TbJ1ZYMqG5wXHiWVLTel7-MxWlX5Xldkp4obZtQYNB69ik5sTiFzvvybfiYr2jP8jBjUmG0llgDpkpDzTMECO1MEnw63e-9JREOv4uEOzbYvtA5FxRK2k8btgmJ8nIJwc3FGoNMHxnwzCuOxy6PV_19aZN4EmUBv18nvPcvDIG0_CMFGkxCJQ0p9dDPc0Ki-N7q-ud_aD7TiPkcQ05cNXKCoT3E5vS2UnHyZuIq72Rk7Gl1UBJWGXAUF3e4EsJWgrtaAMB2F_Wo0neIp9LhBJLJLxxE5tI9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df6dbe7790.mp4?token=MTdjaGjuIaRQfVcztzWGVGJpbiB5LkOjQeioE4QOAQ-YZl61yr80d5TbJ1ZYMqG5wXHiWVLTel7-MxWlX5Xldkp4obZtQYNB69ik5sTiFzvvybfiYr2jP8jBjUmG0llgDpkpDzTMECO1MEnw63e-9JREOv4uEOzbYvtA5FxRK2k8btgmJ8nIJwc3FGoNMHxnwzCuOxy6PV_19aZN4EmUBv18nvPcvDIG0_CMFGkxCJQ0p9dDPc0Ki-N7q-ud_aD7TiPkcQ05cNXKCoT3E5vS2UnHyZuIq72Rk7Gl1UBJWGXAUF3e4EsJWgrtaAMB2F_Wo0neIp9LhBJLJLxxE5tI9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسمت چیه؟ احمد نادری
🔹
کلاس چندمی؟ دوم راهنمایی
🔹
کار تون چیه؟ دفاع از خلیج فارس‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/672517" target="_blank">📅 12:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672516">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKj4wkMRsyU5r5EYbpso_p5YlGisnv07oFUvT09R0Z1I5roiS6c78nh4QaJKG82P8PgckXzoMF0l7Rqjf7ztsz8HoZbHAnL9mCfhYfaVrgBKp3rLtpQr86qO7rLtWsI4ZyN9xKZhnj1_ms7nSAQlj6jSukPlxlq4Qe6m37RBCd56HeaO7ve5X6Ej5n58ohq37U2m4sdb7ZYCzYzDi-zEboAdQpxKH7RVQvc5MZxoM9G9_Ry5vT6bYZJnkMnC2lqDRFq8duq-XsX7DIgTQ7izpc5P2SAg_t2JxOAg-godyx7cXx_UppPwFF7EE1OmFLSfJs8KDT-jiSJL224XOfOXAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۷ تیر ۱۴۰۵؛ ساعت ۱۲:۳۵
🔹
دلار امروز در بازار آزاد با جهش حدود ۵ هزار تومانی، معاملات هفته جدید را در سطح ۱۹۳ هزار و ۴۸۵ تومان آغاز کرد و همزمان، طلای ۱۸ عیار هم با رشد قیمت به ۱۸ میلیون و ۷۸۰ هزار تومان رسید./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/672516" target="_blank">📅 12:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672515">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWyHGCoJnWitJ7APmvi7yTGUrT3zAHM_3Ho164KvroA0E4FTeLqOqLeMXsr8IAdprLyUHspgl3lQpK6uEr9YIONAtfgqWyYi8-rzZsZX0qrWnojkw390qO3yRKRI30Zh204Lq_MPNOYSBFU5jA_9oyesVJoELKYwYVjPIs2rCF-W2V01owxaegBqTK1Vn1cRxXnSzXrEYLUgu7TT-8stxo1W4IsZReGEZvtJVB9iGMDWpkL1NNzp43tid3FVL0bnHVebfh64eLheRhDQ4vvEf92FnQw9Xs7FL4iFn4-0PhbQWi6NrUlHpvwBgb0FmqOI4WUPK7ZwmKV6LMzvr74_KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سدهای مهم کشور چقدر آب دارند؟
🔹
طبق جدیدترین آمار شرکت مدیریت منابع آب ایران تا ۲۴ تیر، سدهای مهم کشور ۶۲ درصد پر هستند.
🔹
ورودی آب سدها از ابتدای سال آبی ۷۶ درصد و حجم مخازن ۳۸ درصد بیشتر از سال گذشته شده است.
🔹
سدهای لار، دوستی، طرق، پانزده‌خرداد، بارزو و ساوه کمتر از ۱۰ درصد آب دارند.
🔹
سدهای نهند، آزادی و ایلام ۱۰۰ درصد پرشدگی دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/672515" target="_blank">📅 12:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672514">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRZWVTr0DYI5mzVYlsbAsFx6A3BefH-Bjw2W7B5vDdtHoLGqWmiV4kMSvfCEOtNQDpeMH6riQjTvKNvV4ZskXMDaF0PfO55RspVnU8Rr8h8IvIzvoBY2UWZk1dDGM8hWqmhLHq2whijrgHGkoyPqo6JGJLEVJH3XRZZQVMWy2WXN7Q5oWFlOUCMSNg-IShAJi8VNv4i41JzmUkIrF9RUyheZvHbGA1nrs6t3DsX9l-hPH8DMSewX60sL_1PBh4QJ7WwI_2_84bytI-Fs7hhvjxXALXYSrhcJ969BeRGZK0ClghsSCtrwZTAdy63NnWhtqUAc3qiJIsizbiLg15vCeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص کل بورس در پایان معاملات امروز با ریزش ۱۲۱ هزار واحدی به ۴ میلیون و ۷۷۳ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/672514" target="_blank">📅 12:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672513">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0935780bf5.mp4?token=G0vL1eUXvzMbFLbAtC94cE2PPDgsU4b-UuTIgtfRcSl63BAe2USWMvEG4b6NSkjKCHkFeaiCx44cRwFRpHR42Du2dZiCPB5GwgSiEIZLLTMqug2-D5NBOy6VOYCbLKSoJ_VDPkG2oGH7u_k-0vN5Q_cL4e3W_8tOJmyOXw2lS2g4ln5u-H41Qn1RbGtewmTiL1WIIxKCE7kOyIBxGmkmiecTOJlApYTaVLjFZVPHfeEAvzQkd74u1kpdfBpFFT1bkVbhIm_odMHImBHsxk1h1xZOekA2pokqyjWyBkH_5F3GAbxLJOrWW77a1EzJZKCta7Y0idzUMO2cpc_20VNfMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0935780bf5.mp4?token=G0vL1eUXvzMbFLbAtC94cE2PPDgsU4b-UuTIgtfRcSl63BAe2USWMvEG4b6NSkjKCHkFeaiCx44cRwFRpHR42Du2dZiCPB5GwgSiEIZLLTMqug2-D5NBOy6VOYCbLKSoJ_VDPkG2oGH7u_k-0vN5Q_cL4e3W_8tOJmyOXw2lS2g4ln5u-H41Qn1RbGtewmTiL1WIIxKCE7kOyIBxGmkmiecTOJlApYTaVLjFZVPHfeEAvzQkd74u1kpdfBpFFT1bkVbhIm_odMHImBHsxk1h1xZOekA2pokqyjWyBkH_5F3GAbxLJOrWW77a1EzJZKCta7Y0idzUMO2cpc_20VNfMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوستالژی موبایل؛ وقتی اریکسون با کیبورد و باتری غول‌پیکر پادشاه بود!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/672513" target="_blank">📅 12:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672512">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ورود سازمان بازرسی کل کشور و دادستانی کل کشور به موضوع اختلالات در شبکه بانکی
سخنگوی قوه قضاییه:
🔹
در جریان حملات سایبری اخیر که موجب اختلال در نظام بانکی کشور شد سازمان بازرسی کل کشور و دادستانی کل کشور موضوع را در دستور کار خود قرار دادند. مطالبه مردم در این زمینه، مطالبه‌ای کاملاً به‌حق است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/672512" target="_blank">📅 12:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672511">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_IMP9jAGV67O6Yk_ofMTbxDv9T1ZfRgA34_T2OAJ6UxPUZyTH4LnwSl51Wu6qSUQ3TP4iyF-s7MmHrxoqIx9a_yB48gX6oP_J_XWgzeVQrKS3mPm2vgu_8FuDhmU-yIfs5NKnAH3xXFX_zxldxrw2UQOuuX2nCeeaYUeeOraFp_v818kNxtI7Rkx0ZLE_Wqw7xkTPiosRadLXkYzi9PCRcnNdWkA0dB0Qh0FKOzOHwl0KxpvmLilbndX58C0sFF4j1PlaRew_mOO9QAIFX9HiCHkAW6SrX-NsYnmBy-AYIhQyMjnH-GVWHurFEhYK4H0KCmD3qpLWyNoEW2Ve6PhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خانوارهای شهری در سال ۱۴۰۳ به نسبت سال ۱۴۰۲، تقریبا ۲۰ میلیون تومان بیشتر می‌توانستند پس‌انداز کنند!
🔹
طبق گزارش مرکز آمار، در سال ۱۴۰۲ هر خانوار شهری سالانه بطور متوسط ۲۵۶ میلیون تومان درآمد داشته و ۲۰۶ میلیون تومان هزینه زندگیش بوده اما در سال ۱۴۰۳ این آمار، ۳۴۳ میلیون تومان مربوط به درآمد و ۲۶۹ میلیون تومان مربوط به هزینه‌های زندگی گزارش شده است./ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/672511" target="_blank">📅 12:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672503">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sG0XlMomey6oXJKBG1cLN5Oc2XxbITMISrakUXjhg-y8ycbB6SqYDRwe4QjRtlah6oxfDpwele7XpKYSSYREcQHf6jVIj7uqr3XY4mwnFgCT2HDmqsCDMOZKwuCQ3fz2GyGd74AJriBnaskzvCpabnCSB7nSd4ry9525-rP99lraWdaiWznpacBLnlPkpg-eZY2E643c3TYkoXkN5h7yJFqc4oRHbJYTQt4Ev4mruSRhgCfYqL43QU4bXNvEuYrwQav5fyEBjtt1YwtNf00WpL4d2QeFu8wXKz1l0k6DM6-38P9BMQEJorNOQms70Gwn05s27nXJQYoYnonQcdcCUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lf2-DPRg3Gat5jSgYTe8oqCs9t7tfJjpOYoE8wWzGIz7EAfdfONWSlo4aCwkV4v7uMPCr0ziuLjAa_ylm_hDHrKly-SozyjP2ddomGHbS5ExeUAlncSq1q51YK_i6qI6a9cOscK-3OVke0rODb-HjprkI94EYR1AkS85Rjn9RRNFv6Axp40X7LfGGokd1-VSo2re-t82F22TQFPFVOMcWG6ytogfOU6-xrMnXoyrQ1ujdliKw4wn8NXAbUtY9bsbbgb7un-Syp57je3rhHMKboXOp8yc3I5jjVicbTAzZkaPmzuze2WLpVKSz4FzfjI-URGNixMztl1gjVwBiLEKlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uNaRXi6HeY7VqcVVHIklJ4ZV9j92mGL7aL8qSu6DrEqomcBQS8_R9F4uRhE-jkG0fCWssEZYhoiRPtxTCJbV42sXnr5qRYZOyfLAx-FLwPXIn_lZ_kvbfXSwQr6oVdLx6oUrI0KUvoA6govFPEeZ1WAic-dsDa6DpxrMs_PX8OulpLQgzwd3I_EwUCnYwgWUpTL1vE1l6skxAWqbhjRcAwHs2VVxgQQhiXoU0MDW5F_Td4x2WAjsQL00UOdCvGtyzOMtpBMyWbpuzSQmKrUgBYsnh64KIjVbyzMfIP-kWBgzL8tJMd3mnGHtzeT1MOWomr49uhANMlf1j6nhxwusnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bvid42XnNkeJkTmyLhZVTBfeMP-ayry1qZ9c24UIu41T1HAV_d0dKIMd84pg8z_wniC1KszVQ_91zCw7JqlqdseOHwOf-RXeJP8CX2N_m38-UB5as7TbAJoGeD_P42Wtvz73jUHJTo-SDCdSbmlquBYh-ViPwrUmRaQDfRjo1z9fAWXWAAwIp0nVgjqwaFzNvBD9PKblgUdBngXuz-802HWakFPptsaNrzcRRbqfzeB8YGZzm-sTti5rGgWY6oRx-KdiMGPGEduGEdcOzPcZfe9WvfZMo7yxaCbo3ISHmGsGRUQOkGb0xoREuT3JRRLS-k94N3BjatGLIaW31aGftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CgXulAwc5Z16F9tMI_zP6hgFsVnbRh8h5nR-fRsnczQPySEqMWHfQ-aP_8oms5V1yKutaWdy8_YDBsaoyH7vLqo_h7GniEnzmR6ROgzlHCW7T0FtTIZxdf2IHcoRpwh4zcPSEFeRobbYNzhc7MCGPWZrcHHWTnxBbSFAHMJyjFZnM9fwmCgkvYdN-lXOfCcHhMIvhQkdqS-X_37Fsx_BebdENPfFTSO5Tbm3fMhhZN0TEHbSoWuGaO-ZssSz9oLNNiF9K0oLnML7UCb-Gy-pQ0fXkq1emVjvErkQFjWtHSLbPpUGCdxG0dhq3vN78AlCGIJTMOna9Ft8eRL311l79g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VAw0E6Et0KaJ9r7quVygt8nL3eEFggbcB4rRLbQ1-epLefWkIVJi0qKECKQwzFUAy316Y9O7fXMxzNBF1bIqmcDS2xEtXvFC9I0RG6xElbKRUb8Tqz7-JsN5iZisxwGpjKEJKaDjVws-1Ds8dCAQgFK63z4sY_trKC6pNV3aShS6iOX71GgyiRhJzdR2vciwUPrdc4tdcRV2JU54JzkK3SVClm5AaRu-Z1DHSVaEK_5hcr9e2o5LgTHuu3Pf600F6yC7-ZdDigYebdAXx5BQ3ghd2fN6-AskPVI6wUhcGFEVQDPH1qVfarKh0X1GxnJ8xfeaBEicZWFvECb-5_mi3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgC3FhryYXh3v4_SYUnv8ctA6_P9Mi66gmK_Cp7A0ywYVvF_wJbqiLxdtBMAjE8jU61m5g9Xcs3xjN95RC7Hs_U4_DtWQP9knUbMkxsuyhYgwmh3f2Z03EgeFn5pZ8t9MR8FhmW1eMyR5o-mZzKEltF-YY-9hCn9gYWXH6anBcEYA-d0i5lfd-JXEb8l-44IXziBaxLAeyvxi203wFuLiQaTh09f7dn8JzAAju_lTlw0fOMvOAMjrdXoVvU4g-BUh6zLKmItJmBxK5E67i5D2AWRZF9h8y0Q2lAb1A-kYnt7tUNwm0xPmH4jakfcWIgab0ZAMQ4QhgyoPNQuRWP0dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcEabckDRa49xbH9puuaiE6MKdPwPrnm0QFEt0eEGI8q-q3RgTSCQUMvuLM5Arg2VI8gugrDLOquvVdlm6efh1d8gcB8raiCH0x5dk44IirjYrjcZCxFKGNAYluv2IJPXW_E6sjJ7quuhTaveQOy5CFY8HXcML5X1KEz9E2F9Gi-r0fR8dCGxMFbet3Iecq5CWZwURXu-CjyZoYbXJzFmKSYthBOkGxdlnq17svxnZDvBSzsp-pLCQFotMNHbSP6xZl5KM35ixswymV7uuddj9WD2RspU27K-HQb6BI2WLxDL0HbGRNdvfWqqPF9bdSaLq-NiwGOAZtksIk_NPTMdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌱
کمپین «نه به پلاستیک»
🔹
تغییر، از یک انتخاب ساده شروع می‌شود…
🔹
در ادامه کمپین «نه به پلاستیک»، تعدادی ساک پارچه‌ای از طرف خبرفوری میان مردم توزیع شد؛ با این هدف که استفاده از کیسه‌های پلاستیکی کمتر و یک انتخاب پایدارتر، جایگزین آن شود.
🔹
هر ساک پارچه‌ای، یعنی یک قدم کمتر برای مصرف پلاستیک؛
و یک قدم بیشتر برای حفظ طبیعت
🌱
شما هم با کنار گذاشتن کیسه‌های پلاستیکی، به کمپین
#نه_به_پلاستیک
بپیوندید.
#نه_به_پلاستیک
🔸
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/672503" target="_blank">📅 12:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672502">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
اسکای‌نیوز: آمریکا دروغ گفت، آنها به مدرسه میناب حمله کردند
اسکای نیوز:
🔹
تحقیقات تازه و بررسی‌های مستقل نشان می‌دهد که برخلاف ادعاهای دونالد ترامپ، شواهد موجود مسئولیت ایالات متحده را در این حمله تقویت می‌کند.
🔹
به گفته هفت کارشناس مستقل و سه منبع نظامی، حمله با موشک‌های کروز تاماهاک و بر اساس اطلاعات هدف‌گیری قدیمی و خطاهای اطلاعاتی انجام شده است.
🔹
همچنین مدل سه‌ بعدی تهیه‌ شده با همکاری Forensic Architecture نشان می‌دهد مدرسه هدف‌قرارگرفته دست‌کم یک دهه از محوطه مرتبط با نیروی دریایی ایران به‌صورت فیزیکی جدا بوده و حملات نیز کاملاً دقیق و هدفمند اجرا شده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/672502" target="_blank">📅 12:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672501">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f470048b5.mp4?token=asslkmTk3SvKba0pvV9y8fB41eQCjSro7kf8tmc1vuzq6iVfey9vKraZm0LX75W4GD6sRRDKwhDcQqbsxy9EKO9-8zJ8wfVY_zksgdBYTNUnVD5mCE10pxQYLEymhQkJ8Hr19HspvoArJOPGEBUO-txEdTuIcojaR76MFs7x_iTsmu4Ckv8t6ve0PITORnrLV6p7G9qdY0HmM3HpSG9KB_AoEdh4KePi6a1EU0ZQK6V2k2AZKw1Y82Tj-QFIbs8DiA0oa0CohlceVbE4ad1X0_DH0Qd9yBUAfDe6yTIvALmJocTr6Hr3rJ0G7VjbLSz5klo6T9CKybvnx1__1HrPHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f470048b5.mp4?token=asslkmTk3SvKba0pvV9y8fB41eQCjSro7kf8tmc1vuzq6iVfey9vKraZm0LX75W4GD6sRRDKwhDcQqbsxy9EKO9-8zJ8wfVY_zksgdBYTNUnVD5mCE10pxQYLEymhQkJ8Hr19HspvoArJOPGEBUO-txEdTuIcojaR76MFs7x_iTsmu4Ckv8t6ve0PITORnrLV6p7G9qdY0HmM3HpSG9KB_AoEdh4KePi6a1EU0ZQK6V2k2AZKw1Y82Tj-QFIbs8DiA0oa0CohlceVbE4ad1X0_DH0Qd9yBUAfDe6yTIvALmJocTr6Hr3rJ0G7VjbLSz5klo6T9CKybvnx1__1HrPHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی قوه‌قضائیه: هنوز رأی پرونده‌های عباس عبدی و صادق زیباکلام صادر نشده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/672501" target="_blank">📅 12:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672500">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoyAJ-Qg5urryuRjSgILPvuaNWOCmN6eO2VGujINS6udnqjm0-X0ivOCfJetFIAhp1mOJUzax2o_FN0wX0tgj6CoyG29gQJCdhmEbUT0a6ICqa1rsdX7P4Xoi_pzx0Lh5A3PedE0wpvqyLR77vwUN4fSuLiPfaUmFUNemvgawXJH1yCXOTTY232n7maMYv4y-7DcPaKwiuKkDNjk76JHZi6rdl0_oDrpJA0PdWzwQ4MMPDDG1bcXLZJLz4QmfSSqXo8_Nz_2GdnbKbvteq0k16qOr28ymC6sZVwR44_lwoEixLn_Mpd-244uRJOCRH3XnzhRl_DWPJh9DTAcl_Q7Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی جنایت جدید آمریکا، آب شرب ۱۰ هزار نفر قطع شد
🔹
در پی حمله وحشیانه آمریکا به آب‌شیرین‌کن بونجی در غرب شهرستان جاسک، تأمین آب آشامیدنی ۲۰ روستا با جمعیتی حدود ۱۰ هزار نفر به‌طور کامل مختل شد.
🔹
این آب‌شیرین‌کن با ظرفیت تولید روزانه ۳۱۵۰ مترمکعب آب، به‌طور کامل از مدار بهره‌برداری خارج شد.
@amarfact</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/672500" target="_blank">📅 12:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672499">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6084cddc9.mp4?token=eJmdy-fLCwihoPerlKj4zJIImT9Mnx8YdU9GzEVJhIl8i7BGBGSesBhWj_W2Bg9OBaxYscmsv70OcQ3hE3sL5CsosEorGW6wvzlm7aWTjGbO1k3MLdyIoJGFQYdXZXsd5_yapB89-8DipFuimdwiP782rOKwEBp0pYgJhFrX6fgkBHx3puTpctPBPOYC4jNDmF0UKpWioCDCPjjkpxBZR8Gto9vDfeS86ltOrDI7LwuwcsNSaUWSWLJmmU3DRD3zDJt22DOb8cZK25kbsqa0ul-NEliNfbgfXWPQh2kKobl-noXgqckrGPsDuZ9baITsooXhQLrw29tS6CMEKuDCa4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6084cddc9.mp4?token=eJmdy-fLCwihoPerlKj4zJIImT9Mnx8YdU9GzEVJhIl8i7BGBGSesBhWj_W2Bg9OBaxYscmsv70OcQ3hE3sL5CsosEorGW6wvzlm7aWTjGbO1k3MLdyIoJGFQYdXZXsd5_yapB89-8DipFuimdwiP782rOKwEBp0pYgJhFrX6fgkBHx3puTpctPBPOYC4jNDmF0UKpWioCDCPjjkpxBZR8Gto9vDfeS86ltOrDI7LwuwcsNSaUWSWLJmmU3DRD3zDJt22DOb8cZK25kbsqa0ul-NEliNfbgfXWPQh2kKobl-noXgqckrGPsDuZ9baITsooXhQLrw29tS6CMEKuDCa4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهندسان ایرانی شاهکار کردند؛ مسیر جایگزین محور رودان ـ بندرعباس در کمترین زمان بازگشایی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/672499" target="_blank">📅 12:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672498">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
فعالیت مسیر ریلی بندرعباس که درپی حملهٔ ۲۶ تیر ارتش تروریستی آمریکا متوقف شده بود، برقرار شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/672498" target="_blank">📅 12:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672496">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ggtI16y3OrLwBUzkt1A0QLfvNBFCGQSZlBnWmkx4p0DqrkGg-c6N8JVn1A-PgBZ6tOa0zg7nqv_FTOCiopwvNy_jewUWx21OU4ykl_s9wdLQiXV0Mb_cXndptVxdhz16rtPGOkVMhmn5wlNu2UWNa2_z3L3EM08PG5etz3DlGKsYUe3yaGUu-K9ZiCkKKcLrLLdOuyplSABfvQvqU4B18KOfzIitjPeJDZKBeaV-6KOOkvV17ni5CzdwLUU8hNTl0phVp8MfNgLCa6i_uztWWYQ2HKAgJi_ayB6-NkhvOZERZYTD17jIfSZyZRlNjxeXts-9-GOf0HXHI3FPtBTsdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رقابت حساس و جذاب فرانسه و انگلیس برای کسب مقام سومی جام جهانی ۲۰۲۶
🇫🇷
فرانسه
⚔️
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏟
ورزشگاه میامی | ۰۰:۳۰
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/672496" target="_blank">📅 12:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672495">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhCADUpkBPfhehZequqv-VpeOqx7z4becMuf1JJluGRdlHhS_1C5OJaFUW6FvVAAFYNjFOLgRr0L6STOwTOyXphCR5Fq9zrrEtzqYUwHUSytYgNaO62F-xVdb1toyt6fzKSEI6bayz7WQI6BQuhhFo6SQuKNdUIplySxaS4-uuv56TxWbJ9VoNZ0empwam7btYuZZpZHtbTEYzjUCnyVZhM4w2bra4xgYYeJY9_r7jPLmhtHAgNwEnn4l9FD2iIwAQrjRKK2TJ-VByt0RuQlXDGSJ9VT7tKsAHlvic42DZvtU7QkfXaxhN8wIb1kLuHXTIQXzx19z-DTDzJ0Wt-X6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه آتش‌سوزی ناسا (NASA firemap) آتش‌سوزی بزرگی را در پایگاه هوایی موفق السلطی در اردن نشان می‌دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/672495" target="_blank">📅 12:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672494">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
آخرین وضعیت پرونده خاندان پهلوی و عوامل اینترنشنال   سخنگوه قوه قضاییه:
🔹
با اعلام جرم دادستانی کل کشور پرونده علیه رضا پهلوی و تعدادی مزدور دیگر تشکیل شده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/672494" target="_blank">📅 12:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672493">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c9cc90b41.mp4?token=gBP4MXURUgNtuS4Qgz8yNrgTErgAGtQDM0myejxpl37ZLzptfrXIUdr1yUDPgC10ml1FcnIM_yadqOy9ClUR0X2Mix8vPw_2QuLLv17lkCRiofE_oL5kaND3vSljhKP-cjqbkbYr2Rq8qtQWmQuiET61X-cL-b34Hwyf7EQip0MAIVQmELY_n2nzKzpl3ssyXFkEHW5YyZsd4cxU5_MvDMkoMGM88XrnMqG9rJk8IVRVymtxa7zbW7McVkz_Dr_m59vACxhxtbz0TLo2vqggFE3isyi9y6lxa9_8CwPbK3HA6sJk3eV4-Lho9_W7OvLK3IX0MEM-AFm6cUL78YOOww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c9cc90b41.mp4?token=gBP4MXURUgNtuS4Qgz8yNrgTErgAGtQDM0myejxpl37ZLzptfrXIUdr1yUDPgC10ml1FcnIM_yadqOy9ClUR0X2Mix8vPw_2QuLLv17lkCRiofE_oL5kaND3vSljhKP-cjqbkbYr2Rq8qtQWmQuiET61X-cL-b34Hwyf7EQip0MAIVQmELY_n2nzKzpl3ssyXFkEHW5YyZsd4cxU5_MvDMkoMGM88XrnMqG9rJk8IVRVymtxa7zbW7McVkz_Dr_m59vACxhxtbz0TLo2vqggFE3isyi9y6lxa9_8CwPbK3HA6sJk3eV4-Lho9_W7OvLK3IX0MEM-AFm6cUL78YOOww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا بعضی آدم‌ها موقع آهنگ گوش دادن تو ذهنشون سناریو می‌سازن؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/672493" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672492">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3HXoFkVpx6Gr38wsXog2Tk3ZX5Mx1RAGHGdDEWPdYOVtoOVrZHZq2vyDnVb3-qFNjt7aRmPrOBf0rgHEB2BNgeYMWer3vxe4o8YUuEWg8BaAxkLuHwMOAWtQmFbZpiZo3WD4rtbk3A7vIQttqO9gX3hAQWLTFQKd73jwVZdkagpbQX0QsmPjyGCD1J9BNGlbzXWA-kbZJGOFkPi7p6azObIFUCV-Hhg9cBX_Y-x5t2geOJIDeZpUnd-lJvSvKgUZV6bqOiNKd0NCec5LlvMcKeR27pJYEMYvnkYi6sGjbl7xOEPQ6otqxuHHvsPQwzubyW1Wx6pMNK6wX6O_TdGUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس عدلیه: با شکست طرح کریدور جنوبی، نقشه شوم دشمن آمریکایی در نطفه خفه شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/672492" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672491">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
عراق و آمریکا ۴۸ توافقنامه و یادداشت تفاهم اقتصادی امضا کردند
🔹
این توافقات شامل همکاری در بخش نفت و برق با شرکت‌های بزرگ بین‌المللی (مانند اکسون‌موبیل و شل)، راه‌اندازی خدمات استارلینک در عراق و احداث خط لوله انتقال نفت میان عراق و سوریه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/672491" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672490">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWNI2h5-DGpDbMNiqyyyGgakSgNpLuWDq4ZU6CZAsB_v--l6s3h-O88axyTcXqiXlua-f6jF1An3FerwKcWNbznXa1y2iSdWabMiU0Oe2OvCWRo_4IDpdMnencnRg-CMf6moZRyRQsRnt97vdFN8T3iuCgHoQVlkJjs9eRPKu-FD1j6W-a0nrxnjJOPWewjywI-LisxLW96LtbCyuctfRi4udjSnapZyQ8MLAna6XJPgO8VA3qo2BVpaOLpSBfd0CmfMYPM8Wj5LC-DL3zSJFSOd6tf3uB4vuA1pAzhUrDKliD75Nnohmqdn2VJ8rvJTe5nVjJHWMXECghubzqrJSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصاحبه تأمل‌برانگیز شبکه سعودی با رئیس رژیم صهیونیستی
🔹
اسحاق هرتزوگ، رئیس رژیم صهیونیستی، در مصاحبه با شبکه سعودی «العربیه» خواستار عادی‌سازی روابط با عربستان و سایر کشورهای عربی شد.
🔹
وی با تمجید از محمد بن سلمان ابراز تمایل به دیدار با او کرد و سوریه را هدف بعدی خواند؛ ادعاهایی که بدون کوچک‌ترین اشاره به حملات مستمر اسرائیل به منطقه مطرح شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/672490" target="_blank">📅 11:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672489">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d12c4ff35.mp4?token=Vurrh1_k47v3eJHTeV8oC6UtaYTiiF-Qgy4VNVRnfLJ0J07_vPuWd1MQd_WlDRScY9BIMF2SbTZpl8Jfi-Pzr3y0BjQmXFBn70x47sHzKGPfXde_eGotkM4MMV450qT-GW4uvkFDiCJb60hHbQ1Dmar8Ej5Imlj7-5_bYJ1Vl5LtarDtomfS4lNmzK8RKMqT9amqia9bfFIRCIz08F5HhjC_kSYtt62j9Yrk9IDsem_7f-fhXZ_fsPWdaR7ab7E8uIgNbeyYANlGcGVyO66q0K11qzqy3ARbi7FYhJQFLg35uPQ7Pus9FIpIfyhyEXp4Uk2Rdqhs0zdboTd2Kv44IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d12c4ff35.mp4?token=Vurrh1_k47v3eJHTeV8oC6UtaYTiiF-Qgy4VNVRnfLJ0J07_vPuWd1MQd_WlDRScY9BIMF2SbTZpl8Jfi-Pzr3y0BjQmXFBn70x47sHzKGPfXde_eGotkM4MMV450qT-GW4uvkFDiCJb60hHbQ1Dmar8Ej5Imlj7-5_bYJ1Vl5LtarDtomfS4lNmzK8RKMqT9amqia9bfFIRCIz08F5HhjC_kSYtt62j9Yrk9IDsem_7f-fhXZ_fsPWdaR7ab7E8uIgNbeyYANlGcGVyO66q0K11qzqy3ARbi7FYhJQFLg35uPQ7Pus9FIpIfyhyEXp4Uk2Rdqhs0zdboTd2Kv44IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حمله دشمن آمریکایی به دو پل در جاده بندرعباس–حاجی‌آباد
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/672489" target="_blank">📅 11:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672488">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
هشدارهای امنیتی آمریکا به اسرائیل رسید
🔹
پس از هشدار وزارت خارجه آمریکا درباره سفر آمریکایی‌ها به غرب آسیا، سفارت واشنگتن در تل‌آویو هم درباره احتمال «تنش‌های پیش‌بینی نشده»، هشدار امنیتی صادر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/672488" target="_blank">📅 11:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672487">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971fac3a64.mp4?token=HxhrfgANYqqaoV4EstmYuht3KEx3QfFVw4PdZkWASvzxEIGX55fnT2vD0GC1EZKSObZMuQgpVZpMjJCO2moHJHHXa3SMwpBTbuaxrB_tRVN943fY2KsiAqCj3_W9EFBeZVawjyv3EoZlVy1QcLEesrH9Jg0a1-XAhfvCX1MBgxCMr6mHS88iaGsM2-U0LQIpMmmeDt9wfbaGPFAGLn24NuI7eUViEJ2f91ejokv87dDHKa3uqF55zdZaCOtZEe61mw5WeD8qLtvJgMLk8Y4VMTcBZRpCGwCxA3reB_Jmf9fKoT1r8PV0SOyaP3Z5ZhO6KOMBOvy5tvVK2jCJK1e8sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971fac3a64.mp4?token=HxhrfgANYqqaoV4EstmYuht3KEx3QfFVw4PdZkWASvzxEIGX55fnT2vD0GC1EZKSObZMuQgpVZpMjJCO2moHJHHXa3SMwpBTbuaxrB_tRVN943fY2KsiAqCj3_W9EFBeZVawjyv3EoZlVy1QcLEesrH9Jg0a1-XAhfvCX1MBgxCMr6mHS88iaGsM2-U0LQIpMmmeDt9wfbaGPFAGLn24NuI7eUViEJ2f91ejokv87dDHKa3uqF55zdZaCOtZEe61mw5WeD8qLtvJgMLk8Y4VMTcBZRpCGwCxA3reB_Jmf9fKoT1r8PV0SOyaP3Z5ZhO6KOMBOvy5tvVK2jCJK1e8sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت پرونده خاندان پهلوی و عوامل اینترنشنال
سخنگوه قوه قضاییه:
🔹
با اعلام جرم دادستانی کل کشور پرونده علیه رضا پهلوی و تعدادی مزدور دیگر تشکیل شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/672487" target="_blank">📅 11:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672486">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c62b1093e.mp4?token=c2z6ykJ0PatR4WDXcpQks06o_AYhlo5e0T6AikrpKcuPtGLcV8yOrzYE5c9jBWURJSpYh4Z-5E64p3cCaapwXKKhWD7nBOwg8QQhEIIcvpqw4Z-TiUJGf9jiENHD95lwbj9zWvvanqzCrziCjLEq5TkLIoGIGxWj4yKZkoU6fHqRK1-OVnjZyYwwv8ucuS7EXV5M4VT8GHLoUDlwqVRZifLrxSWtuEJiOzk5z1XngeLsdlRE41vrguJvvhBLzNOfHJY4mz7QMX05HMFjo__-nW_CKva8KWog5rOyT1Xp2IknV_4T2-TaugIuI9V2Fx57ImsLAYa1ek1skaPbPl9A9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c62b1093e.mp4?token=c2z6ykJ0PatR4WDXcpQks06o_AYhlo5e0T6AikrpKcuPtGLcV8yOrzYE5c9jBWURJSpYh4Z-5E64p3cCaapwXKKhWD7nBOwg8QQhEIIcvpqw4Z-TiUJGf9jiENHD95lwbj9zWvvanqzCrziCjLEq5TkLIoGIGxWj4yKZkoU6fHqRK1-OVnjZyYwwv8ucuS7EXV5M4VT8GHLoUDlwqVRZifLrxSWtuEJiOzk5z1XngeLsdlRE41vrguJvvhBLzNOfHJY4mz7QMX05HMFjo__-nW_CKva8KWog5rOyT1Xp2IknV_4T2-TaugIuI9V2Fx57ImsLAYa1ek1skaPbPl9A9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بی دلیل نیست که بعضی‌ها اینقدر از پله برقی وحشت دارند
👠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/672486" target="_blank">📅 11:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672485">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cceeebfe.mp4?token=ErRpcPFxn5cji0Obd9gJWJwLut7EGrrhw_EfPwcgRldjQxUNcwldlgNAR0evTqfT28uB-9iTmbgjKJYvHU-EtZCvTc31Xxa_PccnZZdyyNeoKk4WkRJSXFwa96USMnQ2FwAdefEnLSOPAYGT-s5Ms7axlw6xlioUbEWyeCZduFJIGv5FC3XxjZF_uLSn3K3f3HiDFsSS73-xGnkG3W1DHhLoQKVShnZiOQOc0mKaRvjz-0Sx-oz6br8EPRsVLlFtLRisvDyCN3Y7kkwFRDqtEIpDHo-MLIxSPS19gYyDQ8FjdehMbRBVG5uyNQt5q7cRqNgPwSNd-lMBVCvEtzi8XbGTI2zMOxuOxQuRbFOSQvIntjjZChvx0UPyaQp6iKo-dEL6VeTNjw3O7wBcnDjaNtaTmLitwILeE6xvRwkTLdjQGzqsHt6acD2kgR_Wnwhw0c0bdXS1IeV4BOf2kpZmu00R_LsesVYNvsyuR7no7s-piENu4ZlML_KSwWB86FAC5AuaNLUeUhDOIBYIHW3Nhb_Bjw3T183I1ziXxzS5F2mk97q7CL8fABVxRuqQJXFNAIFSlLT5f_YcZQULl7bN2Mv0QJ6kK6pgmrW-oNcUlwrzogCrcsw2sXTirh2RbOL1PKNeHGL8IvSqtEItVcYB4SwogYBBolU86B2599-r3Os" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cceeebfe.mp4?token=ErRpcPFxn5cji0Obd9gJWJwLut7EGrrhw_EfPwcgRldjQxUNcwldlgNAR0evTqfT28uB-9iTmbgjKJYvHU-EtZCvTc31Xxa_PccnZZdyyNeoKk4WkRJSXFwa96USMnQ2FwAdefEnLSOPAYGT-s5Ms7axlw6xlioUbEWyeCZduFJIGv5FC3XxjZF_uLSn3K3f3HiDFsSS73-xGnkG3W1DHhLoQKVShnZiOQOc0mKaRvjz-0Sx-oz6br8EPRsVLlFtLRisvDyCN3Y7kkwFRDqtEIpDHo-MLIxSPS19gYyDQ8FjdehMbRBVG5uyNQt5q7cRqNgPwSNd-lMBVCvEtzi8XbGTI2zMOxuOxQuRbFOSQvIntjjZChvx0UPyaQp6iKo-dEL6VeTNjw3O7wBcnDjaNtaTmLitwILeE6xvRwkTLdjQGzqsHt6acD2kgR_Wnwhw0c0bdXS1IeV4BOf2kpZmu00R_LsesVYNvsyuR7no7s-piENu4ZlML_KSwWB86FAC5AuaNLUeUhDOIBYIHW3Nhb_Bjw3T183I1ziXxzS5F2mk97q7CL8fABVxRuqQJXFNAIFSlLT5f_YcZQULl7bN2Mv0QJ6kK6pgmrW-oNcUlwrzogCrcsw2sXTirh2RbOL1PKNeHGL8IvSqtEItVcYB4SwogYBBolU86B2599-r3Os" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش جنجالی CNN از ویرانی پایگاه‌های آمریکایی از حملات کوبنده و دقیق ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/672485" target="_blank">📅 11:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672484">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
حمله به زیرساخت‌های ایران  روایتی از محل حمله آمریکا به جاده بندرعباس رودان  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/672484" target="_blank">📅 11:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672483">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
کویت از وقوع آتش سوزی و آسیب به اجزای یک نیروگاه و دومین نیروگاه آب شیرین کن در نتیجه حمله ایران خبر داد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/672483" target="_blank">📅 11:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672482">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
انفجارها در بحرین ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/672482" target="_blank">📅 11:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672481">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee99573a72.mp4?token=BG2ZOb1Zq_pZEiWaOsf8SYWya4xfIC4JGSYCy1wCkBMGK8GKtQSp550ogpEEmtYSSyPBsFVwNjNM5w6l6e949Gt8C8VcqVSlPKAnpsDpXpkZozDyjN3wxtUuvkN4ObuJWT9BEoX9iFWQoAo1myc7jglfr9wI2Fp-9X8cDJRCLKf10xQndgO8BqhrGYVKqGj5ZDC1q_2WA2McI4W9vdjGxBd9bPTY9t8uk7QdRVKjzp9zG1p2E3E9gyaRhj9B-F08ap7jFdmR0GbUdd0yTNw5zMN_QGEIm9HbI26S3Je154kYbZrO42PN0lGlD_pR7smiB8WTZ-MrOV8DvM0yC6FLAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee99573a72.mp4?token=BG2ZOb1Zq_pZEiWaOsf8SYWya4xfIC4JGSYCy1wCkBMGK8GKtQSp550ogpEEmtYSSyPBsFVwNjNM5w6l6e949Gt8C8VcqVSlPKAnpsDpXpkZozDyjN3wxtUuvkN4ObuJWT9BEoX9iFWQoAo1myc7jglfr9wI2Fp-9X8cDJRCLKf10xQndgO8BqhrGYVKqGj5ZDC1q_2WA2McI4W9vdjGxBd9bPTY9t8uk7QdRVKjzp9zG1p2E3E9gyaRhj9B-F08ap7jFdmR0GbUdd0yTNw5zMN_QGEIm9HbI26S3Je154kYbZrO42PN0lGlD_pR7smiB8WTZ-MrOV8DvM0yC6FLAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جهانگیر: کلیه خسارت‌های وارده در جنگ‌های اخیر را مستندسازی کرده‌ایم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/672481" target="_blank">📅 11:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672480">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اطلاعیه شماره ۲۸
♦️
روابط عمومی سپاه پاسداران انقلاب اسلامی: اسکله پشتیبانی سوخت ناوگان آمریکا، محل تجمع پرنده‌های جنگی دشمن، مرکز داده‌های اطلاعاتی دشمن، یک مرکز سیگنالی و مخابراتی آمریکا درهم کوبیده شدند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/672480" target="_blank">📅 11:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672479">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
اخطار به نانوایی‌ها؛ نرخنامه حتماً در معرض دید مردم باشد
🔹
مردم هنگام پرداخت کارتی دقت کنند که تعداد نان ثبت‌شده در دستگاه، دقیقاً برابر با تعداد نان خریداری‌شده باشد.
🔹
سامانه ۱۳۵ تعزیرات و تلفن ۱۲۴ وزارت صمت آماده دریافت گزارش تخلفات مردمی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/672479" target="_blank">📅 11:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672477">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJ-Coh-o6FT1NAVA1ImsxMDjLzM2ofGjbYbBjgjTtCxWCX3ZLBj_hF8S-SVU1Kxg_xLzLNGq4S3G52ooQvtT376BVgYPcvAjrvygAt8jeoT7LG-Yxo16_315j7Sn1T4DvQd9loiTGdwOdZJSdYN9Ymea_5zsL523zLiJae1PQM6e8PVewiTWWsoldmSMjRGjlu3P1INtDttQXtroIXUEjpw4IQ4SzNJj8L3vP0sT-Mz8g1-9pLNfQ8FHhl8Ntprm68IXWgsG52ptF9npIf_ssYFU5N3TV_Bv62PjKvf5mDb1xD434oYpKrKVJ-bzYJurmlHQzPRn7FX3eIOKWzdlGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faf4c412ca.mp4?token=W6hGM5h8q1zjXQ_26g-UdlVZ6ZDTf_R2cSmQDWQGuyY9Bmo_IE8Q_r1_CkB9Wxt1mmvy5TC2C4Qm_hPh_I1LbZLE9uJIV91v4fOO4mBXIFBk1tFEzBykf3SJcszvmiURJKoJJ5fl4rY51ia0HG7BK4XhAGerdMniu2X6qHcV-y114_Gf3oNCR9pltLwaA7MIML9B--oHwrx9Hv8b9FN4tGqR9iKc1VW_BjzkpNrEy_lBnhCslwagaM1M1pMYZKocudk7JbM1Zbl_pOpMmMDEQLtQp2HxAcXT3iiI4nqtt3vJ2begteHuaJS8YBqk_jiZezptYhCmjGwDc0sZGtISFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faf4c412ca.mp4?token=W6hGM5h8q1zjXQ_26g-UdlVZ6ZDTf_R2cSmQDWQGuyY9Bmo_IE8Q_r1_CkB9Wxt1mmvy5TC2C4Qm_hPh_I1LbZLE9uJIV91v4fOO4mBXIFBk1tFEzBykf3SJcszvmiURJKoJJ5fl4rY51ia0HG7BK4XhAGerdMniu2X6qHcV-y114_Gf3oNCR9pltLwaA7MIML9B--oHwrx9Hv8b9FN4tGqR9iKc1VW_BjzkpNrEy_lBnhCslwagaM1M1pMYZKocudk7JbM1Zbl_pOpMmMDEQLtQp2HxAcXT3iiI4nqtt3vJ2begteHuaJS8YBqk_jiZezptYhCmjGwDc0sZGtISFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پهپادهای اوکراینی به بزرگ‌ترین مرکز خرده‌فروشی تجارت الکترونیک روسیه، در  مسکو حمله کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/672477" target="_blank">📅 11:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672476">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/X6f2jgFCraIAzrHuQLpBKarEXtemcK9-JND2tYKMuWmwYTgikEr1GLAjhRHLXAOZyPGrEUkZgfOTtUS_fBHPwuu1flVNFZIPnTv0RF79LZQcjv38AFjytdcJ_A3rZRVAAUYoPkXFaWOPwXqReWU5Uk20PRr0mafOqkoRfPbEpVD6hv5hDnq9NF1gx85ioStvdihIkwolaOBlgA3t2xrTKDgQ7Ysrj5WFoZe53kH0dsPdjqm_KLbhkMvxJDkdhSR6-QFlFMrXLLJz0_JYbx1SoMVWMBaCTL_GnLtSLiEUUmxJyFQkiRh0KlQdl_6GN5omHse16GwaIylbHXObMgIsaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با افزایش چشمگیر تمام شاخص‌های عملیاتی: ‌فغدیر از ۳۸۰۰ میلیارد سود دوره جاری ۳۲۰۰ میلیارد سود توزیع کرد
‌
🔹
احمد صادقیان مدیرعامل شرکت آهن و فولاد غدیر ایرانیان در مجمع عمومی عادی سالیانه این شرکت از ۸۱ درصد رشد سود عملیاتی و ۴۵ درصد رشد سود خالص در این شرکت خبر داد و افزود: در سال ۱۴۰۴ فغدیر رتبه اول فروش و رتبه دوم قیمت آهن اسفنجی در بورس کالا را کسب کرده است.
🔹
صادقیان افزود با ۳۶ درصد افزایش در تولید آهن اسفنجی و ۵۲ درصد افزایش در فروش آن، این شرکت در تمام شاخص‌های عملکردی و بهره‌وری رشدی چشمگیر را پشت سر گذاشته است، همچنین گندله‌سازی این شرکت علی رغم محدودیت‌ها و طی کردن مراحل راه‌اندازی حدود دو میلیون تن تولید داشته است.
🔹
به گفته مدیرعامل فغدیر حاشیه سود عملیاتی این شرکت در سال مالی گذشته ۲۰ درصد بوده است در حالی که بر اساس داده های کدال میانگین این شاخص در‌ شرکت‌های مشابه بورسی ۱۲/۸ درصد بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/672476" target="_blank">📅 11:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672475">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
انفجارهای مهیب کریات شمونه را لرزاند
🔹
منابع خبری رژیم صهیونیستی مدعی وقوع چندین انفجار در شهرک صهیونیست‌نشین «کریات شمونه» در شمال سرزمین‌های اشغالی شدند.
🔹
رسانه‌های رژیم صهیونیستی مدعی شدند که این انفجارها در پی شلیک موشک‌هایی از جنوب لبنان به سمت این منطقه رخ داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/672475" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672474">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
صدای چند انفجار در بحرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/672474" target="_blank">📅 11:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672473">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3e9f4994.mp4?token=oExv7ZJlTVR9AZe3gEbZLryICABsFEucWCyt63ggyCkrmXnp-vLYrhE8AfEmY3cdoO0dYLeYim2kSoSecSnO7K_Ynd6I-SAykj4O-zE8PlQE5B3PQklwikA2xSzf7tJgvzpH-4i1qkBxKt6ivWBAL3bX2T3PrraDWC0CN8iDEFJx8uVs1oVWjN-ccMMR8zaCdKC76A8tW5xv0dlKk1U1GPa6drwbFsIxWMaUAXDH7UN52pyPfgx7JgZcLDaocni_flEU4daqu94B30h3rmXiO_AeJu2RcbAh0J1YghdNQKJ6bj-phKtTWoK4_UsQtCfxbGChBGZp_IUjzTkh6cZ4sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3e9f4994.mp4?token=oExv7ZJlTVR9AZe3gEbZLryICABsFEucWCyt63ggyCkrmXnp-vLYrhE8AfEmY3cdoO0dYLeYim2kSoSecSnO7K_Ynd6I-SAykj4O-zE8PlQE5B3PQklwikA2xSzf7tJgvzpH-4i1qkBxKt6ivWBAL3bX2T3PrraDWC0CN8iDEFJx8uVs1oVWjN-ccMMR8zaCdKC76A8tW5xv0dlKk1U1GPa6drwbFsIxWMaUAXDH7UN52pyPfgx7JgZcLDaocni_flEU4daqu94B30h3rmXiO_AeJu2RcbAh0J1YghdNQKJ6bj-phKtTWoK4_UsQtCfxbGChBGZp_IUjzTkh6cZ4sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک پایگاه آمریکا در کویت، همچنان در آتش می‌سوزد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/672473" target="_blank">📅 11:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672472">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
فیاضی، نماینده مجلس: وزرای کار و آموزش و پرورش اولویت بیشتری برای استیضاح دارند
عبدالوحید فیاضی، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
در پاسخ به خبر منتشر شده در فضای مجازی مبنی بر استیضاح وزیر آموزش و پرورش، کمیسیون آموزش جلسه‌ای در این باره برگزار نکرده و من در جریان قطعی بودن آن نیستم، هرچند احتمال آن وجود دارد.
🔹
پیش از این، استیضاح وزیر نیرو در دستور کار مجلس بود و استیضاح وزرای صمت و جهاد کشاورزی نیز مطرح شده، اما به نظر می‌رسد در حال حاضر وزیران کار و آموزش و پرورش اولویت بیشتری برای استیضاح پیدا کرده‌اند.
@TV_Fori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/672472" target="_blank">📅 11:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672471">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_iT_WfrkfIkEcF2c5yfDHe5vqiKGWtOVLbB0zhJlnRrNhwPia9Ed9K95g7sHl1RYk78pGureX_GMTz58sWWsu0ZMPAwi18qFPa7W539vHXyLLdHOvcTPKq0OquastGETQ5rqYpgLc5aFdoEOdsw4kSBP3IZMct6BX6rndZ8-23i5xVrk-tbpokYVuxkqbsSRsPl-CllorG6YLPf0RvlAqzUDym7Nax217TBhHvhFmqxnKKc1rRfnl1qo3tgMtLhk6fpf8lCmZGgHBB9ytNe3MecUDsB65F9IDMFyqB2AhOtgqp0jc5Ia84e16UKWx5b9RbkNGPZgbGgQk5uLbxXag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس سابق مجلس آمریکا: به خاطر جنگ‌های ترامپ، کارگران آمریکایی  برای زنده‌ماندن تقلا می‌کنند!
نانسی پلوسی:
🔹
«دونالد ترامپ در ماه آوریل گفته بود که نمی‌تواند نیازهای مردم آمریکا را برآورده کند، زیرا «ما در حال جنگ هستیم.»
🔹
اکنون جمهوری‌خواهان با بودجه‌ای جدید که رویکرد «آمریکا در اولویت آخر» را بازتاب می‌دهد، همان خط را دنبال میکنند؛ بودجه‌ای که ۷۳ میلیارد دلار دیگر را صرف جنگ‌های بی‌پایان ترامپ می‌کند، آن هم در حالی که کارگران برای تأمین هزینه‌های زندگی دست‌وپا می‌زنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/672471" target="_blank">📅 11:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672470">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/672470" target="_blank">📅 11:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672469">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSl6UJC529s36wYAZ-NaBy6dUiPU3ryUA7QoTuSiiw9Cgx255Va_7wtoaEDDLuvlGKshhIgaMR8KAIDj9_KP7pSKZNaXN4sRq1T9fAN2etRvJV8hci7DGY0KyBjgcm_scU1OFZOAfP9bHBRzWPRRyD_geUJf2Rhz4kz9u7vkMN9pLeMqODSVb9qI_SOQyqyVGecX6QBMF4yRC05KO1w4EERURaEv-sEwPgDKQyvUpzBrMy6CKVtKpVvT4oXCK7jLvYZhB1riuwt2ERGBOkzli3Mzzi9APwOkiSOa-4EoAkEpWBpcRROY5t-JIt9nTYtqWH_8lmb9kZePtmQllQR6BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منع ستاره اسپانیایی از ورود به آمریکا به خاطر سفر به ایران
🔹
کاپدویلا اعلام کرد درخواست مجوز سفرش به آمریکا (ESTA) به دلیل سفرش به ایران در سال ۲۰۱۶ برای یک مسابقه رسمی رد شده و به همین دلیل نمی‌تواند همراه فرزندانش به تماشای فینال برود./ ایسنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/672469" target="_blank">📅 10:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672468">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
نسخهٔ جدید ایران برای دریافت هزینهٔ خدمات محیط‌زیستی در تنگهٔ هرمز
رئیس مرکز امور بین‌الملل سازمان حفاظت محیط‌زیست:
🔹
هزینهٔ این خدمات براساس نوع کشتی، ماهیت بار، سوابق شناور و سطح مخاطرات زیست‌محیطی آن تعیین می‌شود./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/672468" target="_blank">📅 10:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672467">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/672467" target="_blank">📅 10:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672466">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45cfabfdd6.mp4?token=MZC39RoLt7ZwYYpV3XYlTREAV1P8HC75pgoFB8AcDCd6LK0z9PVHvqPDH-kFp9Z7XlNGPRRQqBkK9piT3FsTQqnowSN6c1-HjE6a_C_UGu6vPKj_-zJZRrcd62xygckXdl4ewkoVTtLcxkNulfDpbw2DjSHNgG7upGsLtpztIZTrfyYvE01UtGUQC98rJlia5a5rJqIf6gC_jKOdWmSnYSqV1Vb080v0FGsaeoZi0JB7-n1LBBa370FqnEoyQ2Pu1gKri08j_Y-8cizRtMwg2QvGigKrdN1kKdJz73MAKlrqXOMvBaOdG2zyJ-iNcZdC_6aQcpa2l0g4wz2W_h1SMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45cfabfdd6.mp4?token=MZC39RoLt7ZwYYpV3XYlTREAV1P8HC75pgoFB8AcDCd6LK0z9PVHvqPDH-kFp9Z7XlNGPRRQqBkK9piT3FsTQqnowSN6c1-HjE6a_C_UGu6vPKj_-zJZRrcd62xygckXdl4ewkoVTtLcxkNulfDpbw2DjSHNgG7upGsLtpztIZTrfyYvE01UtGUQC98rJlia5a5rJqIf6gC_jKOdWmSnYSqV1Vb080v0FGsaeoZi0JB7-n1LBBa370FqnEoyQ2Pu1gKri08j_Y-8cizRtMwg2QvGigKrdN1kKdJz73MAKlrqXOMvBaOdG2zyJ-iNcZdC_6aQcpa2l0g4wz2W_h1SMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موسسهٔ تحلیلی در بخش نفت‌وگاز: تنها مسیر فعال در تنگهٔ هرمز مسیر ایران است
اچ‌اف‌آر:
🔹
به‌وضوح مشخص است که آمریکا نمی‌تواند کنترل تنگهٔ هرمز را به ایران واگذار کند زیرا در آن‌صورت ایران به قدرتمندترین بازیگر نفت جهان تبدیل خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/672466" target="_blank">📅 10:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672465">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرمانداری: احتمال شنیده شدن صدای انفجارهای کنترل‌شده در دزفول/مردم نگران نشوند.
🔹
ثبت‌نام آزمون کارشناسی به پزشکی از ۱۰ تا ۱۶ شهریور ۱۴۰۵ انجام و آزمون ۲۱ آبان برگزار خواهد شد.
🔹
شمار قربانیان زمین‌لرزه‌های ونزوئلا از ۵۰۰۰ نفر فراتر رفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/672465" target="_blank">📅 10:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672464">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
انهدام بمب‌های به‌جا مانده از جنگ ۴۰ روزه در مهران/ شهروندان نگران نباشند
🔹
شماری از بمب‌ها و پرتابه‌های عمل‌ نکرده به‌ جامانده از جنگ تحمیلی ۴۰ روزه در ادامه روند پاک‌سازی مناطق مرزی در شهرستان مهران منهدم می‌شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/672464" target="_blank">📅 10:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672462">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f98aacbd36.mp4?token=Gz3dwO7f_O4c4YmzusEYqxsuEap4gr1U9SEzgh16Pr2wG2q8MVuWd2AjmSt2vPCBFAd_q67daDCQcUJmatgf3zm3vx-JTZSVL-zhq3BKZbblP54Uhw5CIUQMZAYk-MJTEsbzek_lKCavIAjvfueynneZ2T4Db6sD0UrN8zpBP_7_LbPASvYnDAS9RTQKexaeii921dmKVHlfxdCu3c3xVKk4YIYuUAwEl3NZZGVu_ltAXuRjzhCGkXxyxmMQW_1Bk-xoWZ3bPzlhHrIHMpJ1GTm4SS_AkTUnj86tZSrWUA5xPMAzD3Uct4c85eVJaxmbq67B6bkJ6DnrUQ9d8bvXA3FkLq4oCIbIeyrVYiZWLdzfr8pq1PqdBrGbxw3vZ7ZtMGS0mkKJWGeL82FuUTK8rCJfFz9aOg9fWIfHgwpIaKOXPOaK_YdEfIx8dAOwyI557WbDlDZSxczCByAf54mpjzeZkcbvQcGLTavERbt_Ds4zeTUZDbjRbstSARE_obPrvl9nfgsAmHrvm6AmHfwdzfvgSpbD7AE1cdMpV9VgtZ3DOTOrCEY4WQizBsgJe30XywLJKq4jy5JlGDAvzN9DU0vGoEfEyYwTRXobl3IJeXJvOz_wHi4Nuyun2M5txck7tKpJD95xgXrXZqDY5Gc37f_Zmq8JAzWEn6Nr6H7wpV0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f98aacbd36.mp4?token=Gz3dwO7f_O4c4YmzusEYqxsuEap4gr1U9SEzgh16Pr2wG2q8MVuWd2AjmSt2vPCBFAd_q67daDCQcUJmatgf3zm3vx-JTZSVL-zhq3BKZbblP54Uhw5CIUQMZAYk-MJTEsbzek_lKCavIAjvfueynneZ2T4Db6sD0UrN8zpBP_7_LbPASvYnDAS9RTQKexaeii921dmKVHlfxdCu3c3xVKk4YIYuUAwEl3NZZGVu_ltAXuRjzhCGkXxyxmMQW_1Bk-xoWZ3bPzlhHrIHMpJ1GTm4SS_AkTUnj86tZSrWUA5xPMAzD3Uct4c85eVJaxmbq67B6bkJ6DnrUQ9d8bvXA3FkLq4oCIbIeyrVYiZWLdzfr8pq1PqdBrGbxw3vZ7ZtMGS0mkKJWGeL82FuUTK8rCJfFz9aOg9fWIfHgwpIaKOXPOaK_YdEfIx8dAOwyI557WbDlDZSxczCByAf54mpjzeZkcbvQcGLTavERbt_Ds4zeTUZDbjRbstSARE_obPrvl9nfgsAmHrvm6AmHfwdzfvgSpbD7AE1cdMpV9VgtZ3DOTOrCEY4WQizBsgJe30XywLJKq4jy5JlGDAvzN9DU0vGoEfEyYwTRXobl3IJeXJvOz_wHi4Nuyun2M5txck7tKpJD95xgXrXZqDY5Gc37f_Zmq8JAzWEn6Nr6H7wpV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت آسیب دیدگی تونل شهید میرزایی «گلوگاه»
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/672462" target="_blank">📅 10:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672461">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c22d4f988.mp4?token=pqhao5aCdM1VzTLWnGaO1xiVpyiUcoVbD1-jWDcPFKEzq60003aja8fh1s1E5ciaCwLLJ_k0k_UA-NTzs4ytJfWf4kc7xAQ0iQc1MgUDDSyPAQLo9ZIV5FdEHCdhUkm_iGLPt5WsP6LBg-VeefNJ6mfkxe0l3YWO6HyLxYaV1ijGnn4-GY1WumkM6YwTh8S7CPHGrFs4yeJonulLJyR21Jex0sWYpSzZaqRlmljpuExB-gOXbL3tlRh8m-aGT8AhgBPA-8nCYtsQ5oAd8wump5cA_6O2KPpv6UfAZcqprolEPJ5w6xznaFsKswBB1g_5qiqTKMJvCm3HSxdyLfIbqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c22d4f988.mp4?token=pqhao5aCdM1VzTLWnGaO1xiVpyiUcoVbD1-jWDcPFKEzq60003aja8fh1s1E5ciaCwLLJ_k0k_UA-NTzs4ytJfWf4kc7xAQ0iQc1MgUDDSyPAQLo9ZIV5FdEHCdhUkm_iGLPt5WsP6LBg-VeefNJ6mfkxe0l3YWO6HyLxYaV1ijGnn4-GY1WumkM6YwTh8S7CPHGrFs4yeJonulLJyR21Jex0sWYpSzZaqRlmljpuExB-gOXbL3tlRh8m-aGT8AhgBPA-8nCYtsQ5oAd8wump5cA_6O2KPpv6UfAZcqprolEPJ5w6xznaFsKswBB1g_5qiqTKMJvCm3HSxdyLfIbqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله روسیه به کشتی حامل محموله نظامی برای اوکراین در دریای سیاه
🔹
نیروهای روسی یک کشتی کانتینربر را در دریای سیاه که برای تحویل محموله‌های نظامی به ارتش اوکراین استفاده می‌شد، مورد هدف قرار دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/672461" target="_blank">📅 10:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672460">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daRZBoVMHPKvJ40bHLYoV1pSqBSRpXQci1Q110rXobLIwT1wpxIhPvqNZZVYbdLhmgAOnZldXu8cflz2ZPhx-kSYO1vgnswXO97rz9SAstxEoWCPK6BueI-35VzFwcEJ4aHjtWgdpJHryF5BFMfeIVsE31QAKjsXNlwzVlvLIVsEnRl9iEljaEPptgzPPJJrjLFIr9RJ1JDSa9QBMgVTaGWWaJH66zklIEYxMw1ryZ5Z41A5TKopHAIICkpPzE93HhwIAQDeHWy8k2NTtzEAoTqaMEWLN306MpsRF43oyQajyYmn5dgVLDlONLjIg3M1Oak7g3kUWLgxmr5putsb-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ اشتباه رایج در مسواک زدن
همین اشتباه‌های ساده، لبخندتان را از بین می‌برند!
🪥
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/672460" target="_blank">📅 10:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672459">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سناتور دموکرات خواستار استیضاح ترامپ شد.
🔹
دفترچه سوالات کنکور ارشد منتشر شد.
🔹
آمریکا کنسولگری خود در پیشاور پاکستان را تعطیل کرد.
🔹
تحلیلگر نظامی: دست برتر در تنگه هرمز با ایران است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/672459" target="_blank">📅 10:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672458">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEB0F2Mv74IrE2bbXJLX9KZEJa1dGtH0Ulev_A8jGKclLb3iV_AkAlFKiifQhDqJ8o_QX4yE2EgsNZgFQMD6fR06VG4qvLaku7YoYWOZlkfr2tDdkBxoTqPNgGmgEvIW8w21zIPot4vjHs4WRoIg2yQNXw_sNPch8MDDAylITpofqR2-yndRelCPGFCf_GCf-0Uii6dI1F6G6xiDP2GKyaBEuRyUn4f2n_hyiPSgdhczGiUTE0d4YzICNtUNmGfjcNtLBHPugYV42YGKKO8fBbAsR1MzAjEk65uvsBDZEP3aIC9Upk_2YsZFNF99ymdXmYGQBtzTT72n9JWUdSfXrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیژن مرتضوی، خواننده و آهنگساز ایرانی مقیم آمریکا با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/672458" target="_blank">📅 10:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672457">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTZdCae-ql7McKY8ls4XfgTN1_WY_NSQhcGPU-AFbrCjCvuCV5Dsj5q-azJ92xVupYKF5v-67aO5LM1dn1pyu1pnyb60CHUuYGMcEhvlCqjIqDd3ZHr8MP9R3MoOoaeZGk_nSAooYT6VeLoVThClxWvDp7u46GJkoLrqwgYJwKbiacLH2KjEhG1f3_8cCxOvghQ-7VARUu1TZ2T8fwx-DzA-XHi3ESp1BWLz-Lc9TE5bUXqEFHIQMmeD6wuROpdTrpJnahcyeAYarVZby3s5w7ks8e5eBpogHhM7gYB9NLPEvwQtzHg_PhwYtAGcWtHoCwkgGynlh_fEJs-gEYJNVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوگل در اقدامی هماهنگ با ارتش تروریستی آمریکا، تصاویر ماهواره‌ای مراکز حساس کویت را محو کرد!
🔹
گوگل تصاویر ماهواره‌ای با وضوح بالای نیروگاه برق الشعیبه، تأسیسات آب‌شیرین‌کن الشعیبه، چند پالایشگاه و مجتمع پتروشیمی و همچنین بندر الشعیبه در کویت را محو کرده است.
🔹
این تأسیسات در هفته‌های گذشته هدف حملات ایران قرار گرفته بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/672457" target="_blank">📅 10:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672456">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d419140269.mp4?token=SU65-liw0weIsDKu9I6BaLRMZRM3_LZq0VDtMFIe9ACaO9Hrjj5eC9tC5a6VnjhkSdXlQrcIi7RxrJNR2_JHwcFMdOkYd92toOhtFtwysX93dsHrdOK6VOarABoTceIENCIqz0yJn4y2jSE_HZL81vuAXbmF16Tmwe_BSlKtMYXSZ_mnylJ5a0kOrvZB-tndr9tWU3mjpYX_K18eNsijXsUD9SK5LVlBWJvD6sinKjW0ANtDD-pdb5bU1MaMTW_30mE0rTNjVpBbhNEGsqsiYOgfUHwhtroa6rOC_0gkyXVzrmCMEFfnZqItXWuacArKE4cktkWarnUI5MR9LTdEC7PElmLabLvfnPBncVnMazp6YrZu57N_4y2n_hH1xPDlX1d5HoxvuifTnqht5kiEggGYkEdgacxDMQJBWBKQV2UmhVoKFPnfjvcJX6vLQuzMB43BULcr4plr8jJhGrd_bZG56kfOuM0GmqtEkQI7xrRj0TDLTS-7p4v_T4Uj6I5HHbetxKin5k5Ht0GC0FFfao7ChaJlr9RdfZiEigsrtFfhKMDX5ZDW34cRV-Ur4ftaul0nns-6atZn3cU0RxTcLlSIQhzt0ZagStafhKX_yccM2i73utjIFeLbxNKox7hwgwzS13xVq9HIwQa0MkerZyQcT7cIv8XDnjqZe5aXKjs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d419140269.mp4?token=SU65-liw0weIsDKu9I6BaLRMZRM3_LZq0VDtMFIe9ACaO9Hrjj5eC9tC5a6VnjhkSdXlQrcIi7RxrJNR2_JHwcFMdOkYd92toOhtFtwysX93dsHrdOK6VOarABoTceIENCIqz0yJn4y2jSE_HZL81vuAXbmF16Tmwe_BSlKtMYXSZ_mnylJ5a0kOrvZB-tndr9tWU3mjpYX_K18eNsijXsUD9SK5LVlBWJvD6sinKjW0ANtDD-pdb5bU1MaMTW_30mE0rTNjVpBbhNEGsqsiYOgfUHwhtroa6rOC_0gkyXVzrmCMEFfnZqItXWuacArKE4cktkWarnUI5MR9LTdEC7PElmLabLvfnPBncVnMazp6YrZu57N_4y2n_hH1xPDlX1d5HoxvuifTnqht5kiEggGYkEdgacxDMQJBWBKQV2UmhVoKFPnfjvcJX6vLQuzMB43BULcr4plr8jJhGrd_bZG56kfOuM0GmqtEkQI7xrRj0TDLTS-7p4v_T4Uj6I5HHbetxKin5k5Ht0GC0FFfao7ChaJlr9RdfZiEigsrtFfhKMDX5ZDW34cRV-Ur4ftaul0nns-6atZn3cU0RxTcLlSIQhzt0ZagStafhKX_yccM2i73utjIFeLbxNKox7hwgwzS13xVq9HIwQa0MkerZyQcT7cIv8XDnjqZe5aXKjs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از پل‌های غرب استان هرمزگان که مورد حمله ارتش آمریکا قرار گرفت
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/672456" target="_blank">📅 10:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672455">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxQdGkrHF5uThoqEPyTlJ-Ov8Lr_hEG4zSjKvDGrjzgWDmFlNxmdAZJ0heJPJP3gDr9qKT3HImD2XV_QWghCSf_8HUKNqJpY8eWe_FPERMpXMWoQAX-lulFwpi3bwm1n0aKEpLqn618LQ8uO3i7tOKW3m9PrDBifQeeTz_taXrXYyALVpmmny7wIu9qfEy-wET54bbuGMC1IjXrC8wlQDM-4o92xXE4W2fCzlKJA7eR1gehcx6jYYE2RKujbeog8QGDF5hRKsW0rZT1hoWBZBNWuKC7_20bvW4v6_mMdHnhIMvzPZtcP8EEC0low2aP75jF0QGO36FUn06Mi4POxAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این‌بار پاستا رو به سبک انیمیشن باد برمی‌خیزد درست کن
🍝
مواد لازم:
🔹
اسپاگتی ۲۰۰گرم
🔹
گوجه‌فرنگی ۴عدد
🔹
سیر ۲حبه
🔹
روغن زیتون ۲قاشق غذاخوری
🔹
ریحان تازه
🔹
نمک و فلفل به مقدار لازم
🔹
پنیر پارمزان اختیاری
#آشپزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/672455" target="_blank">📅 10:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672454">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
سی‌بی‌اس: مقامات آمریکایی اعلام کردند که ایران در این هفته دست‌کم ۲ پایگاه در اردن را هدف قرار داده و چندین نفر از نیروهای نظامی آمریکا مجروح شده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/672454" target="_blank">📅 09:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672453">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ادعای کویت درباره حمله ایران به نیروگاه و تأسیسات آب شیرین‌کن
🔹
کویت مدعی شد در جریان حملات موشکی ایران، یک  نیروگاه و تأسیسات آب شیرین‌کُن این کشور به شدت آسیب دیده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/672453" target="_blank">📅 09:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672449">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bYH8ElMt-L4XzSFoBDxWUfaciyyL8_nNTyvoCQe21XkZ-F6_tlibE1haVMhB5Don8Axc7aY1RjdGuEBAwJ2DBaz-gXSNdGbVERKCSZYAEDI1eKKl0i1BaFZ1CsLl_IdtDXOhRNgjd2F-BS12IACdZ0Us84yQdxUCRuMLsD5o-HAdybIyordQnLVE9grbLR7PSszSYK_ysUo6RzRjEOtWBNGo0drynkg1uEwnCU6iI4O9XE1EadhB5y51gXxXFmtauAehb99s4pJl69k7yH6exqu1Rb9qG1DngrqfTY9nwCXEqJjylTcLig_D2PJkpzSu9FVz7-GjiGKQx-da8m3xvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pqe8wEzIfJDXmYuJjGzrf5PRZ4J5GzjwyYPuo9GctDoLH4L_6j55uM8uYUexpvpKScSLC1Zzf1-howf5rPljJO8kifEI9vt9n41Hi4VmGVQrHR1dZZ6N3hOM5r96SCJDtUS1WXE6e8GMHygfTbfI20R3z5GR0OPvrYbMKkJV9OBK0ksFKO8JwWe1K9kTcOi8IL6fScxpvxWb9JXkNZ7Gce_AbFSBYn3uszNvPBiy7BASw9B9E-46SQynO6oL-j_RPiQyD5tQh80NglqwcyFMmM51Y0Owag7XqYzHrrTG4FAsmeCLDW4IdLrohSOAt09fLbzYqJ6ST3oywQNAid5FBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iL_Eucv_U36snKhhaK-9UsN9c0xLV0NhyE61ffaP8da_7kH8TqTQLHNrUqE0rT9iUHM473HnVLheL4gdO3gvIp5ku8EXI5bRQY4O8gubd6XjT7AUl2UNeCqIPoZ6-iPNYhDupndjmGwOlP7c3yH58cnH1JOLW2L68ZdZ2mRjcC9nkdK6QuVBmq9LCwEhcWgiGr-hxbFDbqlwrb4zODzQYKeipSW8bPkbtwUZYIkeJftksghcuSUbMW6SmrqtmBe4wU7E0vjnDIeJBO7vwxhyR5gqwDthnQHV-9DUJx23VQA_vFoUlNAKRe6jWFnnM9P-r2BAJTqgWTckPu-QaoB_8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XR-azpkJQxqz_FEbridrWfNuQ6S95fdaacRDn9xjSHxAii36kW3XqIMkOzc_RGP30ZrK5_mtIZMgfMyE45qiDLsZOSnKIbhmvO9klZ8eNVG9FEvfsM5ly7F1MAYFnb4iaCq7r4XTOY12ArdTItyKksJb2wdIVhQTL7OYbniKMVjo6z2TqHOMi2bFvnh8bpsHnPXKQsVvmoTPs_P32IX13-UhmGlN10vNH4h5CCIiCCbZwX-XbNjQJmFZR6EKEKc9ApVp1gYYVtL4xUxnHxp_l6QDmgiQcecokwdBXitFXIt1q1SOjKcns_SgtbBmnCW7EhbLWaI6W1MQ4LOYL1x4Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حمله جنایتکارانه آمریکا به آب‌شیرین‌کن بونجی جاسک/ ۲۰ روستای ۱۰ هزار نفری بی‌آب شد  مدیرعامل شرکت آب و فاضلاب هرمزگان:
🔹
آمریکا در حمله تروریستی به آب‌شیرین‌کن بونجی در غرب جاسک، ایستگاه پمپاژ و ترانس برق آن را تخریب کرد. این تأسیسات روزانه ۳۱۵۰ مترمکعب آب…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/672449" target="_blank">📅 09:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672445">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2139743d15.mp4?token=RuJq0WJlElAvb5NLKqSZCYyVRZ8sDZss5VelnQ2xliUNnd9N2QqJHa-s_RQulzkqYW7vGdBa2ijKceN8hnUfO-92FpGaqA6dxn0yThxR8KPucwop1QJYdn6MKYpwL5hjijRW6Q7hHgcgzUT_ZyIPLuyRx_ue7_3-oRnYCwLt08Dymiz6dTIE17end7mxhuXs7SM2tkWfgd8rJqHsfjHjLY5vWVE1wFeweua6wNMjg21vAniVBrYgHEQbURqwo7EtdAhwWNBNeP-qJzYBc4DXkN666aeEpVeh0fTQqxxk8rIw4zHfN6LrF_3nFXfqJtk2it5TEZeufWBagJgyHdko6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2139743d15.mp4?token=RuJq0WJlElAvb5NLKqSZCYyVRZ8sDZss5VelnQ2xliUNnd9N2QqJHa-s_RQulzkqYW7vGdBa2ijKceN8hnUfO-92FpGaqA6dxn0yThxR8KPucwop1QJYdn6MKYpwL5hjijRW6Q7hHgcgzUT_ZyIPLuyRx_ue7_3-oRnYCwLt08Dymiz6dTIE17end7mxhuXs7SM2tkWfgd8rJqHsfjHjLY5vWVE1wFeweua6wNMjg21vAniVBrYgHEQbURqwo7EtdAhwWNBNeP-qJzYBc4DXkN666aeEpVeh0fTQqxxk8rIw4zHfN6LrF_3nFXfqJtk2it5TEZeufWBagJgyHdko6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تقابل تاریخی در فینال؛ مسی و یامال: از قاب سال ۲۰۰۷ تا رویارویی در جام جهانی ۲۰۲۶
🔹
سال ۲۰۰۷، خانواده لامین یامال در یک قرعه‌کشی خیریه یونیسف برنده شدند تا نوزاد ۵ ماهه‌شان برای یک تقویم خیریه با مسیِ ۲۰ ساله عکس بگیرد.
🔹
۱۹ سال بعد، آن نوزاد و مسی، حالا به…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/672445" target="_blank">📅 09:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672444">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
دود بسیار غلیظ از کویت به دلیل اصابت موشک‌های ایرانی
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/672444" target="_blank">📅 09:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672441">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b204f4e610.mp4?token=ufdBDeuF15nqp79nk8Km5hkb3guIcG2ia1qN1fimMqFDK10C9sLepC4PrUpHGAWd8gMeVOfgBC7bdNEyPnOJETQImeuMRZs2dDYXCZex3SUg82Nksm4NyFhEv8Hcfcja23rrKmCVCV3yNnRHcpb8gm_85nI86w9PYnMkR3tgZmIUDWmfX72e7rRbMvKlYIS0_8HeyIEMqIsNrPMd8MrKyZj70Qc6kQFKpfaSjcreQgAYxFAy_LX3ohkBcjohBJ_EMZw39CaIMiFmo_Gq5HWPYCLykrfWMr7EmpmClcWAL8JxRIk_1UN0W13PRkDHv1GJSFpqoEb1UvWdHWmLFDbU3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b204f4e610.mp4?token=ufdBDeuF15nqp79nk8Km5hkb3guIcG2ia1qN1fimMqFDK10C9sLepC4PrUpHGAWd8gMeVOfgBC7bdNEyPnOJETQImeuMRZs2dDYXCZex3SUg82Nksm4NyFhEv8Hcfcja23rrKmCVCV3yNnRHcpb8gm_85nI86w9PYnMkR3tgZmIUDWmfX72e7rRbMvKlYIS0_8HeyIEMqIsNrPMd8MrKyZj70Qc6kQFKpfaSjcreQgAYxFAy_LX3ohkBcjohBJ_EMZw39CaIMiFmo_Gq5HWPYCLykrfWMr7EmpmClcWAL8JxRIk_1UN0W13PRkDHv1GJSFpqoEb1UvWdHWmLFDbU3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دود بسیار غلیظ از کویت به دلیل اصابت موشک‌های ایرانی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/672441" target="_blank">📅 09:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672438">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/257aca5779.mp4?token=cj2bD-hW9fetgJrCuCRxqqU-RA6mhxjLeC0j-ZynGuDGnWgK01vqqAqq9gH6O-0J37L5K374RoqNQutmVD0aAzPsBpnhuGIEAWGoISjKOfQ-IXoB-bYdN79rTMWpthAzy2g3yzEb_t4oXUGjmDQ9XWNUsXntbzmLta6mOI0GtfTLH6_R2RshCYfxK2T3V5nbVF_agDau_3QTTD532-Dkelcfo5cSgvK3J7uZIWE7J2eK3oXHQ5K5GKkifFQZ-kYZGo-yHlk1QM39jekC16A6gCw1JXYZde3G0i5B_s5vtjhApq5NVhSA8PcrVL5I8vVst6yBnYl5SZhLgV8mcQB93g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/257aca5779.mp4?token=cj2bD-hW9fetgJrCuCRxqqU-RA6mhxjLeC0j-ZynGuDGnWgK01vqqAqq9gH6O-0J37L5K374RoqNQutmVD0aAzPsBpnhuGIEAWGoISjKOfQ-IXoB-bYdN79rTMWpthAzy2g3yzEb_t4oXUGjmDQ9XWNUsXntbzmLta6mOI0GtfTLH6_R2RshCYfxK2T3V5nbVF_agDau_3QTTD532-Dkelcfo5cSgvK3J7uZIWE7J2eK3oXHQ5K5GKkifFQZ-kYZGo-yHlk1QM39jekC16A6gCw1JXYZde3G0i5B_s5vtjhApq5NVhSA8PcrVL5I8vVst6yBnYl5SZhLgV8mcQB93g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو ادعایی سنتکام از برخی حملات متجاوزانه بامداد امروز خود به ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/672438" target="_blank">📅 09:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672436">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gM-A4p06iTZpmGNchPvRBsK7BCFOlVJ27CzpPf7YO4BZuPk7Xo190Xff4FEZK95QQ4aCjJZCYX5IfHLofMwGKASxcTbiEnBbZk1c4kR1Dh1YYWIWkDkWgd5LRtVPyl26jADe7K9yaSE9CWXs_b-b_7w8A8nf6cAPD8rAHWKepmRSuDiEEOTCr_PSOKGtj52WzNjSFW8gK8jrWxdk0Srpx8KZudwT7eEqVqxJKnf9w8s86ureu-lKYCt9CFZCxTv9YBYl1wDWcT43ESQsVvHlgaXzG6A4Lfx7mEAlR5lRLLTZmci1cKyJkYctvuyPnF73uSOwmQPZemD6TVro40WSyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعلیق فعالیت فرودگاه کویت
🔹
هواپیماها به دلیل تداوم حملات از ورود به حریم هوایی کویت اجتناب می کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/672436" target="_blank">📅 09:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672434">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان: جنایت جنگی دیگر آمریکا این بار در جاسک  تأسیسات برق و پمپ‌های آب‌شیرین‌کن اسکله روستای بونجی هدف حملات موشکی قرار گرفت
🔹
بر اثر حمله به این تاسیسات آب شرب چندین روستا در غرب شهرستان جاسک قطع شده است  #اخبار_هرمزگان…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/672434" target="_blank">📅 09:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672428">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98cab861f1.mp4?token=Xfa6ZK17wQ6q1WHBEINSp7VbVi_Swxc4dKNRAYoiwEQ825ody73S-bF780zbokUKLUtq2PS-Fp9Nltdw3mD6kOhxuwLmgG1Lt_7ccusq3VzUikWaXGCCU8Yj1NC5fthfqgN8YU-0t-95IRWbsdMFmf-zn5HjSe4fELjDBG2RN81C6QIgciIqH8wyuwiogY3zBCAoknr4zU5Ce0tJW7XbV5qnyQzVo4nSFqZBWFjr4FrEYgNLo0ECDgWahZzvk1OvQ11-aaytFeKTMs4pFOAaBx0BAJOY-yZlYfren5zfTp330xyIHYG17adXAQcvTNn57hz8_Jx635wJrv0HvZC6Mw9DtT7a0CKi2KxH87vm-3RBuyW_GQ_SUp2aYvRYmWL2yJweemAnQyGsNR8gESaYxF9bR-BAJRuUMybl3stHWZrwqhWR7axmoUdwmBF2pWVegXMEPeGh-6gTlqyqj_K32XPgMs3FKnumSrJfXj5NsKyf4b2nGODC58HpFM_Ua40wZFsAPQfaaBlEamGPG6_lQDSeuzfhb_6759qHNPSJ8i3QteMAQlzobRUs5dsjftYRvAwOa7-gRcOeFu8c2OEtqSYMkksWVgqM76oprtu7V_BXxUFGtmaIQpf9VOFYQAdiz0RCqfGSTcG_AIYcccv2cHOR9g-4g6pRsVswHmr1RWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98cab861f1.mp4?token=Xfa6ZK17wQ6q1WHBEINSp7VbVi_Swxc4dKNRAYoiwEQ825ody73S-bF780zbokUKLUtq2PS-Fp9Nltdw3mD6kOhxuwLmgG1Lt_7ccusq3VzUikWaXGCCU8Yj1NC5fthfqgN8YU-0t-95IRWbsdMFmf-zn5HjSe4fELjDBG2RN81C6QIgciIqH8wyuwiogY3zBCAoknr4zU5Ce0tJW7XbV5qnyQzVo4nSFqZBWFjr4FrEYgNLo0ECDgWahZzvk1OvQ11-aaytFeKTMs4pFOAaBx0BAJOY-yZlYfren5zfTp330xyIHYG17adXAQcvTNn57hz8_Jx635wJrv0HvZC6Mw9DtT7a0CKi2KxH87vm-3RBuyW_GQ_SUp2aYvRYmWL2yJweemAnQyGsNR8gESaYxF9bR-BAJRuUMybl3stHWZrwqhWR7axmoUdwmBF2pWVegXMEPeGh-6gTlqyqj_K32XPgMs3FKnumSrJfXj5NsKyf4b2nGODC58HpFM_Ua40wZFsAPQfaaBlEamGPG6_lQDSeuzfhb_6759qHNPSJ8i3QteMAQlzobRUs5dsjftYRvAwOa7-gRcOeFu8c2OEtqSYMkksWVgqM76oprtu7V_BXxUFGtmaIQpf9VOFYQAdiz0RCqfGSTcG_AIYcccv2cHOR9g-4g6pRsVswHmr1RWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل به طریقه گلاب ادامه دارد
🔹
فیلم دیده‌نشده‌ای از زیر قبه‌ی حرم مطهر حضرت عباس علیه‌السلام هنگام طواف و گلباران پیکر رهبر مسلمانان جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/672428" target="_blank">📅 08:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672425">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eo7LYL-DUC_eYX4JjLqdBx_cPNn86pstImCQ6eIMhdvVl2SHl-Ez4KJlwUewRZMNYU2F1IkXsiVAY0CSWbbnOY8wC_VtigtagFSS5XjXsr69ogyVCIP86t68Qucs4CFF5cuXqdKTmpjakqGBFDhnQSoU7NxSi8zsgRhAaFMBoROq1RtiI54el8X9ygtU9wvsGoebJ9zt0iZE_i2DdWWsJNJ8rdX8Ioesms7H2Ijm6JvONQ21hNqWeWSVZvWxVCzBYroKOSw_4Bl4SNY3kPX5Vz9XvLrw78EOB6ZJwt0lgqoEVxehjSG5etu6ixK4r8A-La_bcN8vGpwJ0pPh76vvpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W9PBaRhSeb8V3YyfivLdzROnBd6lVn3ptRcjw5DBsMojejJZm-2lq1Z8XD-t5UIss9ufuWP_zoEAZiyL67S4AExFM6XXtpv2asPlw7xzwxp0Vr5EkHqRa3Y4zHgm_LdqQouNP4Wo1VkHhxNYF12D4QxfHwe8A6psf8IWttygiQY1X0fuuLJnHO8fPtfUq9cZ9rLqvljF3tKIEEpBbpo4Uu4GvoOJ8fdmiC2UiOJBAzJUDGk1E9lJOi7LVufGmklBoqKXH0JNgxNxscA-DJ3VlVYDE815ewwT2X-NVaw-lVMH98cZtAbCHBEUpvQie_-eOv-VPOD75SI9ocpPwYGdtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویر ۳ تن از شهدای حمله آمریکا به پل بندر خمیر
🔹
این ۳ شهید اهل روستای نیمه‌کار بودند که درحال رفتن به منزل خویش روی پل به شهادت رسیدند.
🔹
در جریان این حملات ۸ نفر شهید و ۱۹ نفر مجروح شدند. #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/672425" target="_blank">📅 08:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672424">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اطلاعیه شماره ۲۸
♦️
روابط عمومی سپاه پاسداران انقلاب اسلامی: اسکله پشتیبانی سوخت ناوگان آمریکا، محل تجمع پرنده‌های جنگی دشمن، مرکز داده‌های اطلاعاتی دشمن، یک مرکز سیگنالی و مخابراتی آمریکا درهم کوبیده شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/672424" target="_blank">📅 08:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672423">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkQ6TaQ-Ya99Ovcr-j9jHWHDIRY6ipRp7rjjdkSGTgwcRO3Yghf6lV4FW5JkZorHzZERTOBRU4MRxlTYVzWkJvxinaO0fWMODBe-kHIq_AY_kw9E8fwLRJZlQ5z_jOzN5QFSnZu3khSgmWOaXjw6ScHMYClTAEazwIfvVRs-B-8hnLNS7zwcwyNLfp5AEler7Ca1BAf5wE5ITWlz4M1iWKEKmxY1r16Q4pzpRrZ9jQ5eoYxMyLQzMmCiwef6-iBoYvKkvnaFAPVKfhxW6qORBg54Lp47m6JYBSG5qmcI98kB8Ae6VOjmgWBOuMLLBhFt3bYxTorB3mLnRbSLR07ojQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی ۸ سایت هوش مصنوعی؛ ابزار هایی که کارتو راحت‌تر می‌کنند
⌨️
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/672423" target="_blank">📅 08:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672421">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
مهاجرانی، سخنگوی دولت: سهمیه مناطق جنگی برای داوطلبان کنکور ارشد استان‌های جنوبی در نظر گرفته شد./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/672421" target="_blank">📅 08:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672419">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJ8lcpMsasV0OZj7FKOfTUovlYzBXvod9pvTY8O7UgGZv9UcP2EGzkP0XEH9wh9aczjUJaolfp9dNwM9YdBMjlbRDpnCyQwfXLW1yZZIid5zNol8805YoEc6NHIX3S1je1KJTJjPzF5TD1DZDPxQ3ZCyPP72M-uMKAjT5E93fYE4TEETgJ2YfhSDzVYpEHvMBDjWLJe2mxjGJrbv8xLZlghj2c29bJaDrkttUQW6XAAJxyt-v62vFRIvyNG4bAyvO3xorqD2oHBkYjBW1-ytfZvO4zzj-WTRWICCs4othK5BiLHHarNFHcTve9Dmc5hKpqaojQnp-HWCv7T5ZpKpvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پوستر فیفا برای فینال جام جهانی ۲۰۲۶
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/672419" target="_blank">📅 08:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672415">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fANLbCzYD8oJKkd_c0fMH5RNw-6wDkrbSHGxqlbsXwCR5sQe4D0nNV4FVynLn8-T5Z4VuvDce3pcFH2_s7PUtGBsYB9YwD7pc9Jhq8Ny_EovsOmBnuGPWJcHHMHhq4I1gAokVUHm8HnDtaEl58eH3ojYg8dvh-_bvMv3VejYKiYUyOnRhaljhfBhULfLm9Tb38E5X8m2fLC2GeFDY5gzpU54SGtVbRuyHAnolmbSi9FMbL91Xh66k_0wbPl4kA3W2h2-GNx0c2Vwb74g3Ps0KfqLksmcdBtUPbi1hBh3lYaIb_4x8WEBI44gdevT6ljd9t4o5szv_u2lrCggHz4HgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EzgWd8fR87P6dxGGex1G2AfIwh28zRw7KfvjEB6N55uV5hBy_QmtKk9pNbZWfeaDvJHFqjIKYCOpw79qKYO4rUARfIZMpB2t0gfFiYNdQzAKOKx6bHIH48JcaBt4LyXTPXsB9GNa5kxYx5HdujQ-8cBvsTkCRqDX210HNTK95C2Nc4XWon3n0zjtJ9XOLEnAxXWwiBFok8S_6A5Y8CPIfGY4W4oBgsuC-akZqotvy5oQiaq2vxML3lr2qeXSgDQfs9bs11fsNRZspGT0vJ9mRFS2ZgdjjY7TbwH0B3vuod2jx1cWv9F6uj5tv1z2HIBzJqLwot4HLWrNFAsumzZWwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jnk_d4U-VBw8yBgabeNrp8tm_tVLbAfi-YLRnp7UX2UJHs-Jm5xYb60y3E-0E1SOEfxUaBbac_yT5SGekFOKc1TKPU8tpecks36k0-03JVNv_SUd6v5-nG3gwylUEwEoaRr_wznomurZdBY1V_m7SZoret64hs9hhJzgf7tGR6j37IrZ6xPTB0687fd06KuGx35vnPjkFBSMrz-ec5y5lm8lmROj4al6rMx42Lr4AX5BSLnTVV434ULZk3hHaWss06GjmU5ORMRu7FgTL7QAZ6rB7P8CfmvWlyKikI0R__1y39gQsSAndZ9BS9sWYFnZRXGgjgQZU5W7dl7wzjYg_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a69e676ae.mp4?token=URt1GuT0izhNq1iKrXlPAeCh1hLsWeGmeHFuSPhvT8YhXwIxwKfqmaWqcIvOMqIPBmfkYmMlyPu6v-xqwqVtS_-Zx8t7SKZh9sDUUEvsEibdjxhH1MdrcSAVnyNLvgakxIyhZg6Zo6Pg55RLIJfNnZGVppCS7FAsYCSWYYdi3_smXHo4Tf8s8EGat3oQVHQZORknNsVh_np299TnnNQRlTmnPChrR4GeKE5Qz4KOcTWfaqT613660SS7v8TV5EZ5xdpLzL4DGn8ORlFjDJMKgVbsNfLb67JSVwqZOSggxCWxm0Iy_qwVvi6aqf4lj_QB7Fa4ISceanu0poqNCdM-Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a69e676ae.mp4?token=URt1GuT0izhNq1iKrXlPAeCh1hLsWeGmeHFuSPhvT8YhXwIxwKfqmaWqcIvOMqIPBmfkYmMlyPu6v-xqwqVtS_-Zx8t7SKZh9sDUUEvsEibdjxhH1MdrcSAVnyNLvgakxIyhZg6Zo6Pg55RLIJfNnZGVppCS7FAsYCSWYYdi3_smXHo4Tf8s8EGat3oQVHQZORknNsVh_np299TnnNQRlTmnPChrR4GeKE5Qz4KOcTWfaqT613660SS7v8TV5EZ5xdpLzL4DGn8ORlFjDJMKgVbsNfLb67JSVwqZOSggxCWxm0Iy_qwVvi6aqf4lj_QB7Fa4ISceanu0poqNCdM-Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر دیگری از آتش در مقرهای احزاب کرد مخالف ایران در اربیل و سلیمانیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/672415" target="_blank">📅 08:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672414">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d5c6c882c.mp4?token=KRrYMUv0vgTKooA5mno08SzScqcqn1ihSBdWXfYzIEEMRsvTmJouqtBj1zCt39Df9x253xipVP8LdGFwtaWHdUYqOLGX97YOhg94fQTQSChAiOtqbYxkCiebIoK8ojngt5EkbHj-n1oxq1DmSAAvg6NTNHmfwJJvFDKOFq7nPBKnykegyD9DkcR5kYPPqwlT1vk6esP8TPxZO0tRVCLCgVstAybGcZWZQIwPgvHxtnSDJ6--NqI87tSz4kbS9HKu3eCIvdxUkBSeg98JrY7tFwVTxkO4Hr4qCAGM0jQ9_n7WpI-IQ_eAfZWlfaHQUNVk2G078LyHty2dOXsuTKI6-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d5c6c882c.mp4?token=KRrYMUv0vgTKooA5mno08SzScqcqn1ihSBdWXfYzIEEMRsvTmJouqtBj1zCt39Df9x253xipVP8LdGFwtaWHdUYqOLGX97YOhg94fQTQSChAiOtqbYxkCiebIoK8ojngt5EkbHj-n1oxq1DmSAAvg6NTNHmfwJJvFDKOFq7nPBKnykegyD9DkcR5kYPPqwlT1vk6esP8TPxZO0tRVCLCgVstAybGcZWZQIwPgvHxtnSDJ6--NqI87tSz4kbS9HKu3eCIvdxUkBSeg98JrY7tFwVTxkO4Hr4qCAGM0jQ9_n7WpI-IQ_eAfZWlfaHQUNVk2G078LyHty2dOXsuTKI6-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برنامه یک روزه فول بادی بدون نیاز به باشگاه و تجهیزات
💪🏻
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/672414" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672410">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b822dcfe2.mp4?token=ppPxUvAJlJe4HYdY5HGbBJIM31q0FbtBDxzdG9A7f0pkFN_vXrbLwqrJwxJsVSr7aCy7wZ5fPqiXFVXwhPVyjqy8iyDTEbBsbzfSuIJGpIQP7bNx86ecejZgKdlaEvL-Gc8zXq7FoDwAGk8MJg4NfJrq20ltsF7nPy7z6w06r4PtSZnPo3gKNFa9rOOr812VQ2x29R8mCyhY5J6F8rvAKJVVBovUha0zmHqsTWjdHvLweTlR0HrNUE55XH0dQcSnTVdKZEuzVqnL4c9Tx-o3xpUweDjAVhbwV6m7CihXdsYYjW4GrFS-xaQfXvRtEztYkFv77oQC3nUa7f7we6YivQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b822dcfe2.mp4?token=ppPxUvAJlJe4HYdY5HGbBJIM31q0FbtBDxzdG9A7f0pkFN_vXrbLwqrJwxJsVSr7aCy7wZ5fPqiXFVXwhPVyjqy8iyDTEbBsbzfSuIJGpIQP7bNx86ecejZgKdlaEvL-Gc8zXq7FoDwAGk8MJg4NfJrq20ltsF7nPy7z6w06r4PtSZnPo3gKNFa9rOOr812VQ2x29R8mCyhY5J6F8rvAKJVVBovUha0zmHqsTWjdHvLweTlR0HrNUE55XH0dQcSnTVdKZEuzVqnL4c9Tx-o3xpUweDjAVhbwV6m7CihXdsYYjW4GrFS-xaQfXvRtEztYkFv77oQC3nUa7f7we6YivQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پس از ادعای خوک زرد درمورد گرسنگی مردم ایران، یک ایرانی در خیابان‌های لس‌آنجلس با پخش رایگان پیتزا، پاسخ خود را نه با سخن، بلکه با عمل داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/672410" target="_blank">📅 07:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672409">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سران کشورهای عربی که به دشمن پایگاه داده‌اند، قاتل رهبر ما هستند و باید قصاص شوند
🔹
جنگنده‌های آمریکا و رژیم صهیونیستی برای ترور و به شهادت رساندن رهبر و دانشمندان و فرماندهان نظامی کشورمان از پایگاه‌های این دو در کشورهای عربی پرواز کرده بودند.
🔹
بنابراین سران این کشورهای عربی که پایگاه داده‌اند نیز در شهادت بزرگان ما شریک هستند و به عنوان قاتل باید قصاص شوند. پس چرا به قصرها و کاخ‌هایشان حمله نمی‌کنیم و آنها را به جهنم نمی‌فرستیم؟/ روزنامه کیهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/672409" target="_blank">📅 07:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672408">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTXGlnSxOtfom2XidjoaMWa1Tj96_sxNP1FZOxjt-Ls1izPKGSmN1nlOXyBtExObG0H-w2PZGwhhy4-CpxMdOV172cBhWe9CcTAU5T0xqExytNC_URIdjOkd4Ktf3Ed9mBbk8mh1dM3IbngfTH2mgDEXgAimFnXaBMoENGgi5gVqsobnBL8CVlZH8RIxIUCUjvBVkchkn7_eYExREX60xNERQP5-pCg8Rx9HHEkrXp970tCnXD6rw1sbbql8bxnqEOTUH3H9Auv-Gtz_SoCJUNVcMlLSwAllVmT0YPYE7htcSeJR229I6vHPjBNXtjDeYnYLKYeoiRemJrKxBoLclA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۲۷ تیر ماه
۳ صفر ‌۱۴۴۸
۱۸ جولای ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/672408" target="_blank">📅 07:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672407">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ex5yEYOdO6PE32UU3kFxaOTf7fX3CGgOEo5cuZhuzq6RpDnHapE98VE3CoOzd3OK8GGXHyoxzXLmhXBCz7p2uCylpzRL-NFxB0EPMppR4RFLCdZ7xttHM4YwhEQ5QE-luUK3lfNCGo2ggND_8g5Qz_v3MP3kZ9k5GRq9bdYNUckw2JtVLwBA7emnhVZZiEuJMEtKqHI9ZliOrUhm0YT3-A4rA735w1Q1Sm1l_WSA50qMk46T8Zlv3aFD0ejrHmT9jyydmBShjYyy4v35ZLVx4I0ilxa0cdmhQ3vsQ3ye0-IvTmoMJPnrWHLhJzVwsGhjT3k-HUVqK4PPhkAniPTr8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر منتشر شده در فضای مجازی از برخاستن ستون‌های دود در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/672407" target="_blank">📅 07:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672405">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d479df485.mp4?token=j_0W1YJKET2cZCZtxiYUF8Kx7HFPp5-5CsfJfexdIsynqbtmEsPSQEGYslFsgFWx_il9Lc8kStR4jcn2Q1NOGlEVACg9omY6DMuWVbaWHAAPKMZ1C2Miiw5lmyleYlTkbWZ4Q8XvWzeyEdIHsICq9wuRGI5k8czAG52voGNAjuPVs9rp1ZptyxptqHjQLknDKK7KErJ0WcPdBtLuPuWvKkiGdf5w_x_0BUlCEiuicCncqN6u7yVR85hKZ5mncYY109Vzzgt-xTGB58AglLt6GvORkUBCDqD402QpbecXetbZ1UFhbbGnmyVjlEGKu-x2RY_meyVO4ptVg7Jl6Cv6Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d479df485.mp4?token=j_0W1YJKET2cZCZtxiYUF8Kx7HFPp5-5CsfJfexdIsynqbtmEsPSQEGYslFsgFWx_il9Lc8kStR4jcn2Q1NOGlEVACg9omY6DMuWVbaWHAAPKMZ1C2Miiw5lmyleYlTkbWZ4Q8XvWzeyEdIHsICq9wuRGI5k8czAG52voGNAjuPVs9rp1ZptyxptqHjQLknDKK7KErJ0WcPdBtLuPuWvKkiGdf5w_x_0BUlCEiuicCncqN6u7yVR85hKZ5mncYY109Vzzgt-xTGB58AglLt6GvORkUBCDqD402QpbecXetbZ1UFhbbGnmyVjlEGKu-x2RY_meyVO4ptVg7Jl6Cv6Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش: مراکز و پایگاه آمریکا، و چند پل ارتباطی در بحرین هدف حملات پهپادی ارتش قرار گرفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/672405" target="_blank">📅 06:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672401">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان: جنایت جنگی دیگر آمریکا این بار در جاسک
تأسیسات برق و پمپ‌های آب‌شیرین‌کن اسکله روستای بونجی هدف حملات موشکی قرار گرفت
🔹
بر اثر حمله به این تاسیسات آب شرب چندین روستا در غرب شهرستان جاسک قطع شده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/672401" target="_blank">📅 06:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672399">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bce0a3dfc.mp4?token=MBZBWHwL06DoeG82MggT6flZPiaaAREXA6dDSzsBEyoUlzvIqb9d8hpygPIsRIX5e624DR8r6aZN5hw_k3ow-kytYwXp9ELEs3Ue1sSaX_Kmie-bU-OmG5VJaUfe9eZ5cKaPHtUOGAN8F89xL2FiBXpN4Du_PTpAm7kJakpnP7NP-sA7gpQxDaVsrD9pI0Q7lc1iAbSmtGaq6RoFEeCpiXJ2ewrjWgnvwPb3mPziNJbJkUpgxAoYiP5lrRNwgcGlVj-NH5hPm263hu3LN1OwzMkOnLfkBClvGlrnkbGEScgC8mrH5Y0roJkW_8QZa_PaEpftATh16orJNbxSQqqSTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bce0a3dfc.mp4?token=MBZBWHwL06DoeG82MggT6flZPiaaAREXA6dDSzsBEyoUlzvIqb9d8hpygPIsRIX5e624DR8r6aZN5hw_k3ow-kytYwXp9ELEs3Ue1sSaX_Kmie-bU-OmG5VJaUfe9eZ5cKaPHtUOGAN8F89xL2FiBXpN4Du_PTpAm7kJakpnP7NP-sA7gpQxDaVsrD9pI0Q7lc1iAbSmtGaq6RoFEeCpiXJ2ewrjWgnvwPb3mPziNJbJkUpgxAoYiP5lrRNwgcGlVj-NH5hPm263hu3LN1OwzMkOnLfkBClvGlrnkbGEScgC8mrH5Y0roJkW_8QZa_PaEpftATh16orJNbxSQqqSTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
پهپاد ایرانی در آسمان بی دفاع بحرین در جدیدترین موج حملات پیاپی ایران به پایگاه‌های آمریکایی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/672399" target="_blank">📅 05:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672398">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
کویت، بحرین و اردن به دلیل ناتوانی سامانه‌های آمریکایی در برابر ایران، در حال مذاکره برای جایگزینی پیمان‌های دفاعی با پاکستان به جای واشنگتن هستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/672398" target="_blank">📅 05:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672396">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
حمله موشکی ایران به پایگاه موفق سلطی در اردن
🔹
این پایگاه میزبان نیروها و هواپیماهای آمریکایی است. پایگاه در حال حاضر در آتش است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/672396" target="_blank">📅 05:40 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
