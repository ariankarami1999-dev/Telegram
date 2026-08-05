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
<img src="https://cdn4.telesco.pe/file/TFs_PvKVOICHK2FN1Dm7zloTe-sSCAAnirBHEfXmxDofv43Jgwftj6os2WKU3jRltSAq2YO97A965EXvS3XNl9G5CgHAivyZWS2kDSPIj8BCWwe-mqQAksy3Es_XMHFFSlWoNh9dy-Khjvhbmhlv1Rjg4lg0Wof-eRAq61ySKNSY7Cn_kYfS9FFOIKS5eGKidmTWiQswMf5SQVi7qseTdJWwfzp8jdUwvbN2A4XVCMDYbExc4LoDoDMLgxzQ4l-tKeAuOEKrsocYCxNc2gZFGD4hSgtWOnVONXnRj_KTVZChMSjtf3giUqNyoMdTkUIKHrY0ghDvfsvD0ehJexKExA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 445K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 21:31:18</div>
<hr>

<div class="tg-post" id="msg-20539">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">محسن کج بند : به عنوان یه سرباز از‌ همه ایرانیا تقاضا میکنم یکمی دیگه این شرایط رو تحمل کنن، چون ما داریم بعد از آمریکا؛ چین و روسیه به قدرت چهارم جهان تبدیل میشیم؛ این شرایط گذاره
@WarRoom</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/withyashar/20539" target="_blank">📅 21:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20538">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آکسیوس : دور جدید مذاکرات بین اسرائیل و لبنان که با میانجی‌گری ایالات متحده برگزار می‌شد، امروز ساعت 15:30 به وقت رم به پایان رسید. به دلیل تحولات میدانی، مذاکرات زودتر از موعد به پایان رسید، اما فردا صبح از سر گرفته خواهد شد.
بحث‌ها بر روی طیف وسیعی از مسائل سیاسی و نظامی متمرکز بود و بسیار سازنده بودند. تیم‌های فنی پیشرفت‌هایی در تعیین جزئیات کلیدی مربوط به اجرای چارچوب سه‌جانبه داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/20538" target="_blank">📅 20:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20537">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نبیل الحمر، مشاور رسانه‌ای پادشاه بحرین، مدعی شد پدافند هوایی این کشور در حال مقابله با حملات هوایی ایران است.
وی افزود که در ساعات گذشته چندین حمله هوایی ایران رهگیری و دفع شده است.
پیش‌تر نیز هم‌زمان با هشدار درباره احتمال حمله هوایی، آژیرهای خطر در بحرین به صدا درآمده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/20537" target="_blank">📅 19:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20536">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">منابع عربی از حملۀ موشکی به بحرین خبر می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/20536" target="_blank">📅 19:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20535">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نتانیاهو : ترامپ یکی از بزرگ‌ترین دوست‌های ماست،اما یه چیز رو روشن بگم، موجودیت اسرائیل قابل مذاکره نیست چه توافقی بشه چه نشه، هر کاری لازم باشه برای حفظ آینده‌مون انجام می‌دیم
@WarRoom</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/20535" target="_blank">📅 19:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20534">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گزارش‌ها از حادثه امنیتی برای
بالگرد ترامپ در آسمان واشنگتن
رسانه‌های عبری گزارش دادند بالگرد دونالد ترامپ، روز گذشته هنگام حضور او در بالگرد، در آسمان واشنگتن درگیر یک حادثه ایمنی شد.
گفته شده در این حادثه هیچ‌کس آسیب ندید.
سازمان هوانوردی آمریکا در حال بررسی ابعاد این رویداد است.
@WarRoom</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/20534" target="_blank">📅 19:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20533">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/20533" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20532">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ce2c280b.mp4?token=BF-wpa7dkNY9nbsY6t5ZZCTrDR2xGNyprstAPdDYe-kOrm7aEEWQT4wbagI0tncNo8_HYHiA79_VN56RfVjTec2NifFV1ctaOZodukSdsSqFNlXQJu-b75bzbImYlUp80a9yniK78JUE366XrKbRGwenlPkfmr6_FE0yub_WY1GDwmbOsV_l7tTiJAUvyM5a1k9BLuC0pqPqOpnosZb7MvvVLpnDmNdmuIUXhaXnoKkjU0FbqX81w9b3QqmuHRTNHlvdvhfG7esMMiv8omk6gUxfbZ4Wf0sDHkUsSm2P3u9ZeETZiTXA8Lel6ln_4GduMDni60B9mJ1lcjYhZrvNJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ce2c280b.mp4?token=BF-wpa7dkNY9nbsY6t5ZZCTrDR2xGNyprstAPdDYe-kOrm7aEEWQT4wbagI0tncNo8_HYHiA79_VN56RfVjTec2NifFV1ctaOZodukSdsSqFNlXQJu-b75bzbImYlUp80a9yniK78JUE366XrKbRGwenlPkfmr6_FE0yub_WY1GDwmbOsV_l7tTiJAUvyM5a1k9BLuC0pqPqOpnosZb7MvvVLpnDmNdmuIUXhaXnoKkjU0FbqX81w9b3QqmuHRTNHlvdvhfG7esMMiv8omk6gUxfbZ4Wf0sDHkUsSm2P3u9ZeETZiTXA8Lel6ln_4GduMDni60B9mJ1lcjYhZrvNJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل نتانیاهو در یک مراسم:
نیازهای سیاسی فوری این لحظه از من می‌خواهند که پیش از پایان این مراسم مهم ترک کنم.
ما در حال حاضر در میانه رویدادهای نظامی و سیاسی مهمی هستیم.
@WarRoom</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/20532" target="_blank">📅 18:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20531">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سخنگوی وزارت خارجه درباره احتمال سفر قالیباف یا عراقچی به پاکستان یا قطر در پایان این هفته: برنامه‌ای برای سفر به این کشورها نداریم
سخنگوی وزارت خارجه: مختصات جغرافیایی مسیر مد نظر ایران و عمان، مورد تفاهم قرار گرفته
چنانچه برخی طرف‌های ثالث در این زمینه کارشکنی نکنند، بیانیه مشترک دو کشور مشتمل بر ملاحظات و نکات عمده مورد توافق نیز در مرحله بررسی و تدوین نهایی است.
@WarRoom</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/20531" target="_blank">📅 18:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20530">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">داشتون مثل پلنگ اینجاست
🐅</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/20530" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20529">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اتاق جنگ با یاشار : رویترز تبر خورده خبر اشتباه زده
😂
https://ofac.treasury.gov/recent-actions/20260805  در این سند هیچ شرکت هواپیمایی ایرانی از فهرست تحریم خارج نشده است. آنچه حذف شده، همگی مربوط به شرکت هواپیمایی عراقی Fly Baghdad است که قبلاً به دلیل ارتباط…</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/20529" target="_blank">📅 18:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20527">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اتاق جنگ با یاشار : رویترز تبر خورده خبر اشتباه زده
😂
https://ofac.treasury.gov/recent-actions/20260805
در این سند
هیچ شرکت هواپیمایی ایرانی از فهرست تحریم خارج نشده است.
آنچه حذف شده، همگی مربوط به
شرکت هواپیمایی عراقی Fly Baghdad
است که قبلاً به دلیل ارتباط ادعایی با نیروی قدس سپاه تحریم شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/20527" target="_blank">📅 18:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20526">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">عراقچی روز جمعه به پاکستان سفر می کند.
@WarRoom</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/20526" target="_blank">📅 18:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20525">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وال استریت ژورنال: ایران همه چیز را به کنترل تنگه هرمز گره زده است.
رویکرد تند تهران، اقتصاد و روابطش با همسایگان را تهدید به نابودی می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/20525" target="_blank">📅 18:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20524">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رویترز : بر اساس جزئیاتی که روز چهارشنبه در وب‌سایت وزارت خزانه‌داری آمریکا منتشر شد، ایالات متحده تحریم‌های مرتبط با مقابله با تروریسم علیه دو فروند هواپیما و سه شرکت هواپیمایی مرتبط با سپاه پاسداران انقلاب اسلامی ایران را لغو کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/20524" target="_blank">📅 18:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20522">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کانال۱۴ : مقامات آمریکایی تأیید می‌کنند که در هرگونه توافق احتمالی با ایران، تضمین می‌شود که تهران کنترل تنگه هرمز را دیگر در اختیار نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/20522" target="_blank">📅 17:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20520">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رئیس تروریستی سپاه، احمد وحیدی:
«هیچ بحثی درباره اورانیوم غنی‌شده یا سلاح‌های هسته‌ای صورت نخواهد گرفت. تا زمانی که ایالات متحده آمریکا و اسرائیل سلاح‌های هسته‌ای در اختیار داشته باشند، ما به کار خود در این زمینه برای امنیت ملی خود ادامه خواهیم داد.
اگر آن‌ها سلاح‌های خود را کنار بگذارند، ما نیز این کار را خواهیم کرد
.»
@WarRoom
این رژیم قصد ندارد از اهداف هسته‌ای خود دست بکشد. آن‌ها در حال به دست آوردن زمان هستند. هیچ توافقی حاصل نخواهد شد.</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20520" target="_blank">📅 17:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20519">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ارتش اسرائیل: ما حملات متمرکز در جنوب لبنان را آغاز کرده‌ایم در پاسخ به نقض آتش‌بس توسط حزب‌الله.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20519" target="_blank">📅 16:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20518">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">برای اولین بار پس از حدود یک و نیم ماه، ارتش اسرائیل دستور تخلیه را در جنوب لبنان منتشر کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20518" target="_blank">📅 16:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20517">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یک مقام ارشد خلیج فارس به سی‌ان‌ان گفت که احتمال رسیدن ایالات متحده و ایران به یک توافق موقت در روز جمعه ۵۰ به ۵۰ است، هرچند تندروهای اصلی ایران هنوز آن را امضا نکرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20517" target="_blank">📅 16:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20516">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اصابت یک فروند پهپاد دریایی به یک کشتی و بروز آتش‌سوزی در آن
این کشتی هدف حمله یک شناور سطحی بدون سرنشین قرار گرفت که در پی آن آتش‌سوزی در عرشه کشتی رخ داد. نیروهای محلی تمامی خدمه را نجات دادند و آن‌ها در سلامت کامل هستند. غرق شدن این کشتی تأیید شده است
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20516" target="_blank">📅 15:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20515">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حسن روحانی: یک اقلیتی هستند که می‌گویند «اگر این جنگ تشدید و گسترش بیابد، امام زمان زودتر ظهور می‌کند! برای ظهور امام باید جنگ را تشدید کنیم»
رهبر پیشین هیچ‌وقت به دنبال جنگ نبودند
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20515" target="_blank">📅 15:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20514">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHpuuumOeRsDXp6srhwZnx9cMFNOnkHVfk1_feXayRGLU584R_Sn3jIQdWjMxG6Dpd9dAKUr9NNVQ0wl9zBM9zS9pucRJzw-9FU76HBB_6-bY-N7ydcyLrdEtLStqKgktAo25RmwSNrZx9msDReL-HmHu27thmLtmmpmD_G6tc9Xf6GQ3CVC-5ZD2Qexv12wam_6-U2_d9ZGveoC1dXbifAhkUOYW8NNO4S0PP4Swd8IK_KTZrr1ZShjOd71epGU3hkjpoR8poPmauopkxDZgDEhjsJ3CmHBqLJwAylhZaAjsdROfQ_S_TYqvYhNECD_fXZ3QOKYkUFq8L52sihmaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله هوایی اسرائیل به منطقه المنصوری در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20514" target="_blank">📅 14:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20513">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okenti8icJrjLwkp_ddEXpkWHNbUyWEiQ_N5iR-mHH_l_UtZa2nf7JD4oe4B-t0piiPGKYCrNetCPTz_V_JB0qaMfLziS-q6HzraL6nxTR84txLonkh9b9hOVLOFgFlew6XBXLx8WJP3rdTSpDiZaxdrX9wupGK63A2b4KUWavEIEnaqTSLUpc_vlxe1coZE2WjaRMa7FG7sIrtgrEGFKNK2YfSe-sK4Sdmtj8xPImn2G4engDIQAJY0DZNsMUPkVY-BjDSzMSx_7Udmkd3IQlHXzIBuTHuEwxhRWUp3o_oU0SKkZaNE6Nv6rStmTRY85umtGybJ-lWWtV74hQjqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش از فروپاشی اتحاد جماهیر شوروی، دریای خزر تنها میان ایران و شوروی مشترک بود و همین موضوع باعث شکل‌گیری این تصور شد که ایران از سهمی معادل ۵۰ درصد برخوردار است. اما پس از استقلال سه کشور آذربایجان، قزاقستان و ترکمنستان، رژیم حقوقی خزر تغییر کرد و در سال ۲۰۱۸ پنج کشور ساحلی «کنوانسیون رژیم حقوقی دریای خزر» را امضا کردند. این کنوانسیون سهم مشخصی برای هیچ‌یک از کشورها تعیین نکرد و تعیین مرزهای بستر و زیر بستر را به توافق‌های دوجانبه واگذار کرد. منتقدان معتقدند نتیجه عملی این روند و نحوه مرزبندی، سهم قابل بهره‌برداری ایران از بستر و منابع نفت و گاز خزر را به حدود ۱۱-۱۳ درصد کاهش داده و دسترسی ایران به بخش بزرگی از منابع انرژی این دریا را محدود کرده است. در مقابل، مقام‌های جمهوری اسلامی تأکید دارند که ایران سهم ۱۳ درصدی را نپذیرفته و مذاکرات برای تعیین مرزهای نهایی همچنان ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20513" target="_blank">📅 12:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20512">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6a7e2519.mp4?token=Nq7wBFOzYGwemfkVOIZh4odPUxSyfFl3XArRUMKlVOZYv4ZilFz1BruiZ6VCMJ5yDlQMCXfPC5xJNqFXRu81fQryXM20_EulxLv7T8Yw3bN7ms9DqMWJX6d9y14NqmU09VooMD7UPfxL0P4IDREln9r3hZQAUMZLqgwRVVtBUKpzPlSdHN17wU6f2kDSRkCQI5T38WjSNcfu2l6GG1fo2_yFCDo3JkSL-Jx0TVMaJkgRm4BTOrCe1POskljsT5Sa5So4rsg5gjByoSZU2u2B9jDU-TKH_xYaNjzvb2bQ8sL8zbbKRjtTJLvQqogeS9ulRqoMbSaMZ59aDRm49_zM_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6a7e2519.mp4?token=Nq7wBFOzYGwemfkVOIZh4odPUxSyfFl3XArRUMKlVOZYv4ZilFz1BruiZ6VCMJ5yDlQMCXfPC5xJNqFXRu81fQryXM20_EulxLv7T8Yw3bN7ms9DqMWJX6d9y14NqmU09VooMD7UPfxL0P4IDREln9r3hZQAUMZLqgwRVVtBUKpzPlSdHN17wU6f2kDSRkCQI5T38WjSNcfu2l6GG1fo2_yFCDo3JkSL-Jx0TVMaJkgRm4BTOrCe1POskljsT5Sa5So4rsg5gjByoSZU2u2B9jDU-TKH_xYaNjzvb2bQ8sL8zbbKRjtTJLvQqogeS9ulRqoMbSaMZ59aDRm49_zM_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : تحمل کنین تخت گاز داریم میریم ! داریم میریم سمت قاهره ! غر نزنید دایرکت ! تمام  این مسیر این شیشرو با هم حمل کردیم !
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20512" target="_blank">📅 09:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20510">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ecb47cbac.mp4?token=UbemSgIl42tRh9WnA1DNwy-nMABSS3z_GvdniT0YReGIxX3h6QiGiowy46yB7cupSkit1lcq4bswdbXMnq8MyfNGcHza30hzNy04cwVZspVuQwIql1eIuRWu74bn7IW16KoxsFqISsw3PJGgpNseOkolwzcwl2WEGpPoM5jULe9cIYmXtC37LIpl7dptdCJFc-4r_XtAOelXOVusVy834iVnE5BwztnNj1SS4Vh-NXdfdiVh_GfIFosbNYR-yuyb-CjN9uKATnUUm0Uf2qKWuDTssJubhh5SngMROzo1sKXyU6qtBkofonZ-ofGZ_c3tPgIiEVHj-B_WESAj2C7Ctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ecb47cbac.mp4?token=UbemSgIl42tRh9WnA1DNwy-nMABSS3z_GvdniT0YReGIxX3h6QiGiowy46yB7cupSkit1lcq4bswdbXMnq8MyfNGcHza30hzNy04cwVZspVuQwIql1eIuRWu74bn7IW16KoxsFqISsw3PJGgpNseOkolwzcwl2WEGpPoM5jULe9cIYmXtC37LIpl7dptdCJFc-4r_XtAOelXOVusVy834iVnE5BwztnNj1SS4Vh-NXdfdiVh_GfIFosbNYR-yuyb-CjN9uKATnUUm0Uf2qKWuDTssJubhh5SngMROzo1sKXyU6qtBkofonZ-ofGZ_c3tPgIiEVHj-B_WESAj2C7Ctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏خبرنگار: اکنون در قبال رژیم جمهوری اسلامی در چه مرحله‌ای قرار داریم؟
‏ ترامپ: «ظرف ۴۸ ساعت آینده خواهیم فهمید.»
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20510" target="_blank">📅 09:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20509">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏پیت هگست، وزیر جنگ آمریکا، در واکنش به گزارش فیک‌ CNN مبنی بر اینکه ذخایر موشک‌ها و مهمات آمریکا در جنگ با رژیم جمهوری اسلامی به شکل هشدارآمیزی کاهش یافته است، گفت: «شرم بر شما باد! سی‌ان ان گزارش شما حقیقت ندارد. خجالت بکشید. ما باید بسیار بیشتر از این از رسانه‌های جعلی متنفر باشیم.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20509" target="_blank">📅 09:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20508">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یک منبع ایرانی به المیادین:
توافق در مورد تنگه هرمز به تعویق خواهد افتاد تا زمانی که آمریکا به تهدید علیه ایران ادامه دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20508" target="_blank">📅 09:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20507">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">صندوق سرمایه‌گذاری عمومی عربستان سعودی (PIF) به همراه سرمایه‌گذارانی از جمله شرکت Affinity Partners متعلق به جرد کوشنر، خرید ۵۵ میلیارد دلاری شرکت Electronic Arts (EA) را تکمیل کرد و این شرکت را به یک شرکت خصوصی تبدیل نمود.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20507" target="_blank">📅 08:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20506">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">طبق نظرسنجی ها در اسرائیل و اطلاعات کانال 14 اسرائیل :
بنیامین نتانیاهو همچنان میتونه نخست وزیر اسرائیل بمونه بخاطر محبوبیت زیادش و رای بیشتر
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20506" target="_blank">📅 08:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20505">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c23a61982.mp4?token=QBA9sPDF5jmVT4e8YD3rMc8O2B7PQBFpiWRWcuC-XXQHaUz860ZMqmXBNM6bM1sje7TL6SpU85qKh6OTWwaKgVQuSACdVvxFZwkdJ_2zybHkXguykM4JYQLsVevc2W0UL735zohzkj7KrPCZfeYThoKQFt46USKJiTXWcAduKHpoE_YPKbYWljcaNyqgID14cGS13Fw8NljApdyqDzeH5dqVV_Aj6XuzT3vFimuZcJOwQyOl9UAkGBqLDy4CrAYglkb6yMv-0uMB1bsBJmmP0qGjkT2-rWeO681ZfyKADUWDKpNsSiGTxlO2bqXH9Oz7EJSqfs2DkaZfT32GSUh_ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c23a61982.mp4?token=QBA9sPDF5jmVT4e8YD3rMc8O2B7PQBFpiWRWcuC-XXQHaUz860ZMqmXBNM6bM1sje7TL6SpU85qKh6OTWwaKgVQuSACdVvxFZwkdJ_2zybHkXguykM4JYQLsVevc2W0UL735zohzkj7KrPCZfeYThoKQFt46USKJiTXWcAduKHpoE_YPKbYWljcaNyqgID14cGS13Fw8NljApdyqDzeH5dqVV_Aj6XuzT3vFimuZcJOwQyOl9UAkGBqLDy4CrAYglkb6yMv-0uMB1bsBJmmP0qGjkT2-rWeO681ZfyKADUWDKpNsSiGTxlO2bqXH9Oz7EJSqfs2DkaZfT32GSUh_ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : ما خیلی خیلی محکم میتونیم به ایران ضربه بزنیم ولی خب اینکارو نمیکنیم، صحبتای خوبی باهم کردیم ولی اونا نمیخوان قبول کنن. اونا به ما زنگ زدن و مودبانه گفتن: میتونیم مذاکره کنیم لطفا؟
ما به رسانه‌ها اعلام میکنیم که داریم مذاکره میکنیم ولی ایرانی‌ها میگن که اصلا صحبتی با آمریکا نکردیم. پس داشتیم چکارمیکردیم؟
تنگه هرمز به زودی باز میشه و اگه این اتفاق نیفته اونا ضربه محکمی میخورن چون ضربه‌ی اصلی ما هنوز مونده ولی امیدوارم کار به اونجا نکشه.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20505" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20504">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فردی مسلح دو روز پیش از حضور دونالد ترامپ در باشگاه گلف او در کالیفرنیا بازداشت شد.
پلیس اعلام کرد این مرد ۳۸ ساله که
ژنین جان تائله
نام دارد، در حال عکاسی و فیلم‌برداری از محوطه باشگاه بوده و ظاهراً فعالیت‌های امنیتی را زیر نظر داشته است. هنگام بازرسی، یک خشاب ۱۶ تیر و مهمات در جیب او و یک تپانچه پر در خودرواش کشف شد. با تفتیش منزلش نیز چندین سلاح، مهمات، جلیقه ضدگلوله، خشاب‌های پرظرفیت و دفترچه‌هایی با نوشته‌های «نگران‌کننده» به دست آمد. پرونده اکنون با همکاری FBI، سرویس مخفی آمریکا و کارگروه مشترک مبارزه با تروریسم در حال بررسی است
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20504" target="_blank">📅 06:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20503">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آکسیوس: آمریکا، ایران و عمان به توافقی موقت ۶۰ روزه برای بازگشایی تنگه هرمز نزدیک شده‌اند و واشنگتن قصد دارد آن را روز چهارشنبه اعلام کند.
بر اساس این توافق، کشتی‌های ورودی از مسیر شمالی در آب‌های ایران و کشتی‌های خروجی از مسیر جنوبی در آب‌های عمان با هماهنگی ایران عبور خواهند کرد و هیچ عوارضی دریافت نمی‌شود. همچنین مین‌های دریایی مسیر مرکزی طی ۳۰ روز پاکسازی شده و سپس این مسیر برای تردد دوطرفه بازگشایی خواهد شد. قطر، پاکستان و عربستان نیز در میانجی‌گری مشارکت داشته‌اند و کاخ سفید مستقیماً در مذاکرات حضور داشته است. عباس عراقچی با این چارچوب موافقت اولیه کرده بود و به گفته منابع آمریکایی و منطقه‌ای، مجتبی خامنه‌ای و شورای عالی امنیت ملی ایران نیز روز سه‌شنبه آن را تأیید کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20503" target="_blank">📅 06:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20502">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رسانه های عراقی طرفدار رژیم :
شنیده شدن صدای مهیب انفجار از سمت ایران در منطقه شلمچه در نزدیکی مرز آبادان
@WarRoom</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/20502" target="_blank">📅 23:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20501">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مارک لوین : دیکتاتور سعودی دوست نیست
@WarRoom</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/withyashar/20501" target="_blank">📅 22:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20500">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/049666fcb2.mp4?token=VENzFfhla2gWYvDWmxvrE2Q_IXhbwau97wSNgy2JLj5nMdokSzx6kbpxTp9Vt_o3ujQ2d67f_Om_Cp-4_lIhnGr27Mo9KOC2y1YhtrVz7T8Uy_42iyqgriy142jrj43wQUA2l_UKUvKdwZTrvo0rLmtBsvxHGAjrpGYZdb1el7e8Y-RANEltGSxTx3CzAPNfPF2dupAL7b9bBxac30mPTCcm2jEM5PKaReGZLLjGAHntFn99ZWyOVdD3En5GX4JMKAYoaSPKDs3PCL4UDEsNrO11UFqAa_SZpF8j5XZOh8l-TMxAtjubAlNCT2oQAUAX7-FXwUxVNlz1CAR9Kz2dPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/049666fcb2.mp4?token=VENzFfhla2gWYvDWmxvrE2Q_IXhbwau97wSNgy2JLj5nMdokSzx6kbpxTp9Vt_o3ujQ2d67f_Om_Cp-4_lIhnGr27Mo9KOC2y1YhtrVz7T8Uy_42iyqgriy142jrj43wQUA2l_UKUvKdwZTrvo0rLmtBsvxHGAjrpGYZdb1el7e8Y-RANEltGSxTx3CzAPNfPF2dupAL7b9bBxac30mPTCcm2jEM5PKaReGZLLjGAHntFn99ZWyOVdD3En5GX4JMKAYoaSPKDs3PCL4UDEsNrO11UFqAa_SZpF8j5XZOh8l-TMxAtjubAlNCT2oQAUAX7-FXwUxVNlz1CAR9Kz2dPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ عازم لس‌آنجلس و لاس‌وگاس شد
@WarRoom</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/20500" target="_blank">📅 22:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20499">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سنتکام اعلام کرد که از ابتدای ازسرگیری محاصره دریایی اعمال شده علیه ایران تاکنون 45 کشتی را ملزم به تغییر مسیر کرده و دو کشتی را با هدف‌گرفتن آنها ازکار انداخته و دو کشتی دیگر را مورد بازرسی قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/20499" target="_blank">📅 22:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20498">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/komOEd3NOXDSZ9csnfvbseyyQiDoO52npVP77pMXrw30SBWkGJRHKb4a5qM06_7-aIHlgIghWIJr6icf3NLi-Ut66LIjoQ4jsFWf6YS7qLfnhjD8FtxY6KDspSrQY_TzZC38mO8CJhIzLWISLkAwSn5kYNd76HyZ_KEVH3FhviTXwxM2scDTSsrs7MJWw2H8pzSoodd-GqlWtjv_xAGYjvooaji3wMagWhpJS4IjRdOZT8q7UC5sJZmUecCrSLgdz3f7Ffl_wdqAMmJEgAPK3BhAcqzYWTEhMulTICuH9QkxyQYW1_cETH00GhM2aDG0U896XIkOnPx7L8KpjhfyqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ۷۹.۳۵$ شد و به زیر ۸۰ اومد
@WarRoom</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/20498" target="_blank">📅 21:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20497">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وال استریت ژورنال: اگرچه واشنگتن تأکید دارد توافق ممکن است به‌زودی نهایی شود، اما ادامه حملات دریایی و اختلاف بر سر شرایط و هزینه‌های بازگشایی هرمز، همچنان مهم‌ترین موانع پیش روی مذاکرات هستند
@WarRoom</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/20497" target="_blank">📅 21:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20496">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نتانیاهو:
ترامپ و تیمش معتقدند می‌توانند حماس را وادار به خلع سلاح کنند و غزه را کاملاً غیرنظامی سازند. آن‌ها پیش‌نویس این طرح را برای ما فرستادند، اما ما با آن موافقت نکردیم. این پیش‌نویس، طرح ما نیست؛ ما اصلاحات و نظرات خود را برای آن ارسال کردیم. جالب اینکه این نظرات را پیش از آغاز جنجال و فضاسازی رسانه‌ای درباره این موضوع فرستاده بودیم. این موضع رسمی ماست و با درایت، قاطعیت و حفظ منافع خود، بر آن ایستاده‌ایم.
@WarRoom</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/20496" target="_blank">📅 21:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20495">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فاکس نیوز:یک مقام ارشد دولت آمریکا فاش کرد که لغو جنگ توسط پرزیدنت ترامپ در واقع بخاطر لو رفتن زمان جنگ در رسانه ها بوده و ترامپ این جنگ را فقط به عقب انداخته و مشاورانش به او گفته اند می تواند در این بین و برای آخرین بار به جمهوری اسلامی فرصت مذاکره و توافق دهد و در غیر این صورت در تاریخی که از قبل معلوم کرده و این دفعه امیدوار است لو نرود، حمله بسیار گسترده به ایران را انجام دهد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/20495" target="_blank">📅 20:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20494">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4509abf5f6.mp4?token=Iwf9XjhX-OBskCHQuhtFkq2c3x3vDd-HVPLZW-XTxdF-8BkZt6Jc4A-Ah4jL-jpKEu_9JZAj7pgFURh9COKTJJpQXuId7tg-EDJiFxaNq_9uJBwPZzxm-K4EYRDEV3v__bm_JhtO37LQe2YL9z5qJ2pc04cBI_kKZkajSOkCDOhuqQKOglFcEaRylsa_1EXPqekt3MwaOJ2UhFA1d3jhJ6thwAR9x7eCfGXk_UvZMzbI3zsP-3_GrgkJq1OuyJ1pO7b81bXHLvV47VtKZKUloO-11v8FyJlyFaloBBb11U6qT3KfAcI5MNYSWVaD-_Na-c-zHrclo4n16Qn5PCY_QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4509abf5f6.mp4?token=Iwf9XjhX-OBskCHQuhtFkq2c3x3vDd-HVPLZW-XTxdF-8BkZt6Jc4A-Ah4jL-jpKEu_9JZAj7pgFURh9COKTJJpQXuId7tg-EDJiFxaNq_9uJBwPZzxm-K4EYRDEV3v__bm_JhtO37LQe2YL9z5qJ2pc04cBI_kKZkajSOkCDOhuqQKOglFcEaRylsa_1EXPqekt3MwaOJ2UhFA1d3jhJ6thwAR9x7eCfGXk_UvZMzbI3zsP-3_GrgkJq1OuyJ1pO7b81bXHLvV47VtKZKUloO-11v8FyJlyFaloBBb11U6qT3KfAcI5MNYSWVaD-_Na-c-zHrclo4n16Qn5PCY_QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : جنگنده رادارگریز F-22 نیروی هوایی ایالات متحده در حال دریافت سوخت از یک KC-135 Stratotanker در آسمان خاورمیانه
@WarRoom
🚨
🚨
🚨
🚨
یاشار: اف۲۲ ها هم اومدن منطقه و آماده هستند</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20494" target="_blank">📅 20:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20493">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تلویزیون ایران: اگه ترامپ خودش بزاره ما توافق میکنیم ولی دخالت میکنه نمیزاره
مذاکرات بین دو کشور ساحلی در حال انجام است و هیچ ارتباطی با ایالات متحده ندارد، اما ترامپ با دخالت‌های مکررش، تلاش می‌کند این تصور را ایجاد کند که بر روند این مذاکرات تأثیر می‌گذارد.
ایران در تلاش است تا به صورت مستقل از تهدیدهای آمریکا، به پیشبرد برنامه‌های خود در مورد تنگه هرمز ادامه دهد و تأکید می‌کند که تأثیر ایالات متحده بر این مذاکرات تنها منفی بوده است، و تهران منافع و اولویت‌های خود را بر اساس زمان‌بندی یا خواسته‌های ترامپ تعیین نمی‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20493" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20492">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یک کشتی کانتینربر متعلق به هند در دریای سرخ به وسیله یک قایق انتحاری، نزدیک بندر حدیده یمن، منفجر شد و در حال غرق شدن است!
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20492" target="_blank">📅 19:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20491">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4zoDfmZOZCvLlQ5LarNdXMsQjV7t4Nw1LkevGkdmcQm3vIujPG-qP1d7b997gRL5ppcvMVMf1xQjrCj4I34XDoRHR1YNyJJ2s2R33a4WsmCZdH_j8dlA0LJKbLUOTS4j2NrTT9W3N6Lz_WPBw0-N_Cq8dphWfVN21H159bZxFAJcjzgpfx_PWrKepwuRBkKwlC4c59tFBbUnozDDvD9BJXuCIArqnAYK78ISGve0wBgrOk8y8AfYVAiMmWW3M2osyX43MQqNqPvVPZ5S5Tda0XZZTUH05ScGQxORijwuRHemVK-AJh0Rr4CrqF324GYvA4oZEhqzHdLRK5TmT3CeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود اهواز ….
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20491" target="_blank">📅 19:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20490">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ادعای ‌اینترنشنال :بر اساس اطلاعاتی که به دستمون رسیده، ملاقات پزشکیان و مجتبی خامنه‌ای که تو اردیبهشت انجام شده، زمان خیلی کوتاهی داشته.این دیدار داخل پناهگاه نبوده و تو یه محل امن، داخل ماشین انجام شده.
ادعا شده پزشکیان و مجتبی خامنه‌ای روی صندلی عقب ماشین نشسته بودن، اما صورت همدیگه رو نمی‌دیدن و گفت‌وگو به همین شکل انجام شده.
همین موضوع باعث ناراحتی پزشکیان شده و گفته: «اصلاً معلوم نیست اون شخص مجتبی بوده یا نه؛ با این کار منو تحقیر کردن.»
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20490" target="_blank">📅 19:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20489">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHQH4AauqkQY_bVeyejIAQlA5DflcY1a0ZzQ1iPS1XvLYNCASpm-N4QyIzKl57rrAIp_TejcUMHlfJWsLNY6ixtW-W_mAnSpIzWvRkWUbtmrdj9V7IOjGqFezfISA4CxsBuaa0KFsRHCYi0Mt9saET1bJi5n00ZTtc56-UZZvpdV8eLhcy9Z-4tzvfaSFh8a5ZoH3r_c6L4rD0e8RAw5Px0gnGS7hRZD2228aDrN5-Of7M_TEJR2In27AVJuIbWesV0lw3ppg3wavdsAts2Ly-k1t_T8KEnZfB6rb7DQYO2ddt95P0TrRTpdTDD8DW4iB8QQf1CafObz8rsyt9wAKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای توافق اهواز همکنون …
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20489" target="_blank">📅 18:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20488">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbHA0j8LKj4wTZHj8rkK2SLhwRmUkvonr7IQR25bkHGQr8dtXSjaZx9QDnTf2RhkqdyLfUtflt3cwW4bQ3RseKr5ERp3JyF19RqfEkV_qDtQWP7JSiaRsQCkg39eqHEVFqulvtYYngjuAsR_y2rKMm0bMcYs2Bxdc5e-JaN2HS7Jxk4ugYh7kEOObf__tPh-bKoJprQQSXOHhGz4GVUagcv4gf98XZBAk4PvUJ4XjeM4x6suSLKs7S-WDYOrK8dzSoMPk_Us1uuEdNLfjXSBGty7phRT7KZB7XcUsokIzNenhnXHoCr1CmEVtJpK2kouVkdCTbOkqUbdEbrjEaKjfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «توافق قریب‌الوقوع است» همزمان با از سرگیری مذاکرات ایران در روز دوشنبه درباره خلع سلاح هسته‌ای
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20488" target="_blank">📅 18:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20487">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmsG5lE41Yr9RVvPz3NMZCWFdNvuXsfH0YlzuyjtKn7Fcf5miht_Zbvj_8c-miibg1Xf5gex08d1MEBOXtHtIQ8_nBkWSsulJjhksVwFv2ab2Jo9bCbhLqKaYoMcqv9plhxVNJlX2rFs2aI1ng5E0VLtHjyweBxMI_1RGxSIu9q4ApfP4mAe046Zlfm8LnztS_ncMEAKYTmsIr9OJVIo_FOVVIdEmj0L-gCX1ImkT3i2NxfXPY4u_23-H0wgSdZiDCLBeviiYRNwxK61f4oEYdCUVF3-sVop4tYkgIN4NELS3gHQxccRzRPBZHdZq0KDH_tdgOkQrBj0C6qh-qyaYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام ياشار همين الان پادگان سپاه بانه انفجار شديد
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20487" target="_blank">📅 18:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20486">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa412933a5.mp4?token=pQuC1-23aXxdmMoKkq2w6i4OgrG7xXOYebKkznL4Yos5f4grncrYvpcYv6L401WdvQcFDKWDDahRegVwlkzykyBS-03QmxkVV0P-KxiTyl3h4_83-wSCYtOYtgh6mD4LDlTqVXinXzZh-oF4zdJIJtwz5dWHaDcO13cYHv29Emwt4YwX805WLvXrD197OK11v8JC14P9ryCOQCxmaEHIZThyCCV1YMZPBGT0S59F-Qg9O3WEDKUN3qlYcFoRb3pI8dsXod9M_YtrDnRhWrgqJ8QbMdiLQ2vFA5xhJWI25ZXrSahZyOmERwuCaw6wVOXgNIz2oOL9wlAi8ahdDIZ50Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa412933a5.mp4?token=pQuC1-23aXxdmMoKkq2w6i4OgrG7xXOYebKkznL4Yos5f4grncrYvpcYv6L401WdvQcFDKWDDahRegVwlkzykyBS-03QmxkVV0P-KxiTyl3h4_83-wSCYtOYtgh6mD4LDlTqVXinXzZh-oF4zdJIJtwz5dWHaDcO13cYHv29Emwt4YwX805WLvXrD197OK11v8JC14P9ryCOQCxmaEHIZThyCCV1YMZPBGT0S59F-Qg9O3WEDKUN3qlYcFoRb3pI8dsXod9M_YtrDnRhWrgqJ8QbMdiLQ2vFA5xhJWI25ZXrSahZyOmERwuCaw6wVOXgNIz2oOL9wlAi8ahdDIZ50Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران
: در مذاکرات برای بازگشایی تنگه هرمز پیشرفت حاصل شده است، اما هنوز توافق نهایی به دست نیامده است. ما امیدواریم که توافقی خیلی زود نهایی شود
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20486" target="_blank">📅 17:57 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20485">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ادعای رسانه‌های کشورهای حاشیه خلیج فارس:
به‌زودی بیانیه‌ای درباره بازگشایی تنگه هرمز منتشر خواهد شد
،
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20485" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20484">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSwXbsPd76IDkARJmEkf0hiYKz_uY6zHmXvv8wGyJbIQTXdgd3X7rpViPIhPBS1naJ0rYw0yXHZo716BZm6BWDRlfnO-o3HeMnMHzI2cJ5577Nesv4KO0QFD1pJO7-72U4N6eT2btR_QUKFhAfTfjZZ5sptCwrixwtvqXnxiy1VkDnNYvxxVV-78F7uRxxo56djbIs2fUKy1z78GGtNIbmB8jpzde51Hyd05Kznm0aR6iVGtz_uyChjTVJ-ippsV4nE8WGS3OxedBoj1nxDwFsEdr_xGZ4I1CMeJTGnaAsClCo-Q8UB51mXMT3vwiHqtcy85tQv3Sgvrl6Xx8aLLBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا، در مصاحبه با CNBC، گفت: ممکن است فردا با ایران برای بازگشایی تنگه هرمز به توافق برسیم.
کاهش نفت و افزایش اونس طلا بعد از این مصاحبه
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20484" target="_blank">📅 15:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20483">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">«تبریزی»سخنگوی اورژانس تهران : ۱۸ مصدوم در حادثه انفجار در شهرک شمس‌آباد
متاسفانه پایگاه اورژانس هم در نزدیکی محل حادثه به دلیل موج انفجار تخریب شده است، علت انفجار در دست بررسی است.
@WarRoom
یاشار : دقت کردی ؟ موج انفجار ! علت هم هنوز مشخص نیست!  فقط بی بی میدونه</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20483" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20482">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بلومبرگ : ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20482" target="_blank">📅 14:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20481">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یک مقام ارشد پاکستان به گاردین:
مذاکرات میان جمهوری اسلامی و امریکا،
به بن بست رسیده است!
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20481" target="_blank">📅 14:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20480">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قطر: متن اولیه برای یک توافق  آمریکا/ایران تدوین شده است
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20480" target="_blank">📅 14:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20479">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اتاق جنگ با یاشار :میگن کارخانه آلومینیوم کاران بوده بد نیست بدانید
آلومینیوم یکی از مواد پرکاربرد در ساخت پهپادها و موشک‌ها، از جمله پهپادهای شاهد-۱۳۶ و آرش، به شمار می‌رود. از آلیاژهای آلومینیوم در بخش‌هایی از سازه و قطعات داخلی استفاده می‌شود و هم‌زمان از کامپوزیت‌ها و فولاد نیز بهره می‌گیرند. این فلز همچنین در ساخت موشک‌های بالستیک، کروز و برخی موشک‌های سوخت جامد کاربرد گسترده‌ای دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20479" target="_blank">📅 14:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20478">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وزارت خارجه قطر: تا کنون هیچ توافقی حاصل نشده است و در حال حاضر، مهم‌ترین مسئله بازگشت به مسیر دیپلماتیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20478" target="_blank">📅 14:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20477">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b588c7cf3.mp4?token=bhCWDszoUxSovuqjJojdZoPgVIpAH0SsPfGlrOB3jzQA4UWe-CIs9jJOvcdQ3Mn5JjhSQZYx_Vj-H88nKN8iPnYd37CgmrOlGJqD2yEdqQzainsUmQZlo1t9OpZyo8tpJXV2IodmXe2NaEXKNOH7VJW2WlME_U6dp6N9K4AWo99g0YcK9I5E0BeyPr67B6QHWDQenqtwNdf0FZjWLOlZ_dNwxRRFztIM_Ba4rKsV3dbIhxRfGiDvkS-RJRuPSfMcgAZfC91LfQq9xgDqzvCk4sX3XZhp1fHYwIaIzQ9PIDSrbKsVqYwNatHHHOcJknk-aV5Ugie-gXADtpE8qVutV5sKWDQ-1qTbRoQNqXvlgNayjJmYtS1D9WuqeVY5wF3XC1pWwmXaw1Vx_zNcS6x9sv9xwbfsYzlZW1OKlQ8q8nNG26dfsp52CvTSgz4xZnlVLhmQM4Q2h-qvCY2EpfIYnVwO63EKMENrvJjwVLbJV_d23235dJ-cwKh1_fjw9b265QhAnAbudpEKbPe2RmaN_EoElgbvLtx1GgAGRkLdSpEJM86005krz4GAAZ5N7pDliXssG_NF9-1IT7Wy_aJsSgARnCazdVpR_QtN-fLodWattKp2BJ-bVwY-bS3dnz1RfnMUOpkIY2c2F8eubLUVppINmNjF-C5FPrHqbe984co" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b588c7cf3.mp4?token=bhCWDszoUxSovuqjJojdZoPgVIpAH0SsPfGlrOB3jzQA4UWe-CIs9jJOvcdQ3Mn5JjhSQZYx_Vj-H88nKN8iPnYd37CgmrOlGJqD2yEdqQzainsUmQZlo1t9OpZyo8tpJXV2IodmXe2NaEXKNOH7VJW2WlME_U6dp6N9K4AWo99g0YcK9I5E0BeyPr67B6QHWDQenqtwNdf0FZjWLOlZ_dNwxRRFztIM_Ba4rKsV3dbIhxRfGiDvkS-RJRuPSfMcgAZfC91LfQq9xgDqzvCk4sX3XZhp1fHYwIaIzQ9PIDSrbKsVqYwNatHHHOcJknk-aV5Ugie-gXADtpE8qVutV5sKWDQ-1qTbRoQNqXvlgNayjJmYtS1D9WuqeVY5wF3XC1pWwmXaw1Vx_zNcS6x9sv9xwbfsYzlZW1OKlQ8q8nNG26dfsp52CvTSgz4xZnlVLhmQM4Q2h-qvCY2EpfIYnVwO63EKMENrvJjwVLbJV_d23235dJ-cwKh1_fjw9b265QhAnAbudpEKbPe2RmaN_EoElgbvLtx1GgAGRkLdSpEJM86005krz4GAAZ5N7pDliXssG_NF9-1IT7Wy_aJsSgARnCazdVpR_QtN-fLodWattKp2BJ-bVwY-bS3dnz1RfnMUOpkIY2c2F8eubLUVppINmNjF-C5FPrHqbe984co" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمس آباد یک انفجار یک سمت و بک انفجار سمت دیگر !
حالا عرزشی چی میگی ؟ گاز و گوزه ؟!
🤣
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20477" target="_blank">📅 14:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20476">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0d135103.mp4?token=HqcLUlCS6kYJB6J7t6wM8x3uDwUEmYjqBYagauXtS0ZGxawxTt9oOhQz8Sa-tJli9JOkgZakmbJ8gt7Zurb6wSYXPZHuo4xatjWZwyq_DgkYUC25NYfZ9xsIUii6ilQ4wHfsqfHtSyOKlPOa3aXJMDdWrvQ6enr7zLnmcu4KUAd-UdgwscYDS2MkXRt1MOzlzb6vPegfX4_3zedWjuqFEX10sEIkBJsgBy2S4vwCYnKWtSk63cgDNoKATPqwin50q6TRKyAcIW4LGTdhrHZfBuCCPk-YV0c1vHJa_objJLjxXWm9DCDb_nKUDaBtsJH68_uyTCeB25d8keVybl0pnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0d135103.mp4?token=HqcLUlCS6kYJB6J7t6wM8x3uDwUEmYjqBYagauXtS0ZGxawxTt9oOhQz8Sa-tJli9JOkgZakmbJ8gt7Zurb6wSYXPZHuo4xatjWZwyq_DgkYUC25NYfZ9xsIUii6ilQ4wHfsqfHtSyOKlPOa3aXJMDdWrvQ6enr7zLnmcu4KUAd-UdgwscYDS2MkXRt1MOzlzb6vPegfX4_3zedWjuqFEX10sEIkBJsgBy2S4vwCYnKWtSk63cgDNoKATPqwin50q6TRKyAcIW4LGTdhrHZfBuCCPk-YV0c1vHJa_objJLjxXWm9DCDb_nKUDaBtsJH68_uyTCeB25d8keVybl0pnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار اسلامشهر هم اکنون
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20476" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20475">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSS_CZFpRsSFpa-4dwMNiWKevQfrEONpfkXAOQrzkGKbQ_Ses3j6O7C4oqZgGe5CpFFu8a9-7AQwgaAeDSzjstUs3smoauN9qsAogcBlppAXJVfuQKaHiNbGvKpy_GiPo2SPkVpbVBLyGJ8E_cDzjVdv5JywJEsYpYssxC4W5cu_misHN59HikL4ukDZhPVNLSTououk78xaTSevU54Lhhu_pa9TxgSqJQ4jRZ2UJdJdmXdbtiz5r22ZSD4pFKLsdpD59opqxnF-8Fb_Nj26mHOy5pYswT-R43FzhEFavlxEOn0VsKEG2AOApDt-5NYwTBr6jOfbQfkWptYD6qvSlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت مدیره شهرک صنعتی شمس آباد:
چند لحظه پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
اصلا حمله ای نشده مردم نگران نباشند
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20475" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20474">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گروه تروریستی حوثی‌های یمن اعلام کرده‌اند که یک حمله دقیق با استفاده از پهپاد علیه یک "هدف حساس" در فرودگاه نجران در عربستان سعودی انجام داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20474" target="_blank">📅 13:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20472">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d96f29aa.mp4?token=kXJWFlwwbV0eh5TL5jok7_LhTdzYpxRz4HRpp0zhE3XNTHEKfzs-gz_QUe4KRH6wEsORfDPYQpXMrBc-h69NGymQrrLxGxCfqWpI_GiuafBZj4nGxtBPVgNK0u1O99mb9AMI5xjD_ifgX-89w-A1_lzMy-2iUjQF6KNco4uTD909Gbvblel1_CC33n8Heqbu45HENqjfuFQQ0EIbjUXx0MpKLvH7wmWneQ5UofoVD0ghtUjxZ0RxfP7Diw_obVBavDbg6yXlKiO02W7NFm1Z44wF1X3dSRHDMnYxrRXlmrgPXjw79BfbdlmsHjsqAzsby4vlaOVkhVfg82ApGSpylw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d96f29aa.mp4?token=kXJWFlwwbV0eh5TL5jok7_LhTdzYpxRz4HRpp0zhE3XNTHEKfzs-gz_QUe4KRH6wEsORfDPYQpXMrBc-h69NGymQrrLxGxCfqWpI_GiuafBZj4nGxtBPVgNK0u1O99mb9AMI5xjD_ifgX-89w-A1_lzMy-2iUjQF6KNco4uTD909Gbvblel1_CC33n8Heqbu45HENqjfuFQQ0EIbjUXx0MpKLvH7wmWneQ5UofoVD0ghtUjxZ0RxfP7Diw_obVBavDbg6yXlKiO02W7NFm1Z44wF1X3dSRHDMnYxrRXlmrgPXjw79BfbdlmsHjsqAzsby4vlaOVkhVfg82ApGSpylw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشتی باری که امروز سپاه زد !
ایا این حملات جواب این حمله است ؟ یاشار : شک نکن!
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20472" target="_blank">📅 13:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20471">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsBWDvZUH-UAE36zwGZD4Dt4QSSMNb3EBXdTqgsW-rvPMi1SoVZYAF_TnPgYabZCCcrIYH80hfPF7cEyuysAxFcQtOJIkoDO09dlKHvPf7FFiByFZoiiTb9NsBDgPZYrm-avjPEeSI71Nz-D0Ns19v2FFnwVcAa33xi_U8LjKRLhsxrhzoi_g13Ww4D0HgsDvchjYLCZI3xiTd_Ks6id4bKWdySw_pe2atgmdIV3mPSr8C6nnhUCbExFCt7ikkSsRjnDSoLWifyeaQ37o9jTwjMaw6XKuRFwNl7rwl8afpZQq7333cCRThaaZqmPPLIHoa68RHE_e-swxTNqqE5bKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلاورجان اصفهان رو هم زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20471" target="_blank">📅 13:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20468">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/538f54d0f8.mp4?token=KXHYgpb79R2bJXYN0Ba91XDLcqlLhST6NQKvwQQT0BFTKYHVzpHBtykJYgOKQMm4eEqXMojT04-XO_s_PtbL8-QRJNglAN2Q95_JOZfirnayajAn5Eppm6h5oQnZ5KeJXHevF15FKdEyM-EdpTgWbZFjkd4tRjz5FjrpbSOHRwVqRqn2C-7FoBBxXr_2UbpJX4Z-2I7ssai_KEk8DYWHR680WsEIzuWveD_AHM_Q18YUxqT9WsDjlPX_S2rxAM4oglOGCeA-yOyHWN619ULNYVNiIra0oRgRNCBmXl1XAvKDrxMZU1edWlHWJ05aZijI7jMAS-MQixCZucguFgR_pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/538f54d0f8.mp4?token=KXHYgpb79R2bJXYN0Ba91XDLcqlLhST6NQKvwQQT0BFTKYHVzpHBtykJYgOKQMm4eEqXMojT04-XO_s_PtbL8-QRJNglAN2Q95_JOZfirnayajAn5Eppm6h5oQnZ5KeJXHevF15FKdEyM-EdpTgWbZFjkd4tRjz5FjrpbSOHRwVqRqn2C-7FoBBxXr_2UbpJX4Z-2I7ssai_KEk8DYWHR680WsEIzuWveD_AHM_Q18YUxqT9WsDjlPX_S2rxAM4oglOGCeA-yOyHWN619ULNYVNiIra0oRgRNCBmXl1XAvKDrxMZU1edWlHWJ05aZijI7jMAS-MQixCZucguFgR_pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون فرودگاه بین‌المللی رامون اسرائیل دیگه هیچ جایی نداره و از سوخترسان های آمریکایی در حد انفجار رسیده ، مذاکرات بسیار خوب پیشم میره
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20468" target="_blank">📅 13:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20467">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اصفهان صدای جنگنده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20467" target="_blank">📅 13:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20466">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfQkO5xH4ibE0JQokCWG_LjeAg2EGASCUWe6tLcpTOGoqnwDUcFO_PogmTMjLTBSSFti0Iim7j0-aNro1nqekxqHP9JL8ni041ew-2WokaJiMTBrR_8ZHyTlLjHsZYAzOaeMaR6myG_BMut51vTdEzHa-XpltnocOnlrCpEBCSJDW38wyMWUGgcvwCzyUBkuyYlBMdfT-ehp1xrDqvJnYNudbyL2v3q8FjIr67KY-MBBqTxV05tXYSi2uSMNYWITpH2khO1268ubMDpqs1-MsRJyTTqHAnDwT_nCIYMALxk0wQk4RRJBb4ZW6OVQjvFwufunS--5suPs5euyDcPfDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایی دیگر از دو انفجار
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20466" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20465">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c3af8280.mp4?token=d4HMQt2VRPOhf2hTHxo5gXXid7ve0GSvCgRiKbz1gFdj75Kh7gMao4Re65XZgpWsNtn23uP6O6YObghVg8cKERWGUhnUbch_g9LUs3kDDnFXNDL4cNF1steQwWS-D80agcYoBqa_yVBk1KzcsgLz0k7CdzFMuVf1x6MKzzs7OQiulTph8dW10sv4Gc7gEeGLp5W0z7zoEguiB-c8mYn4xpJdT7EWQUzlIKQgppzwf7w9c1sC2X_5tDJIoM3s3Sji1fmVQ5q2OjZdhSregT9w2QX_-aKs_zTadPJTnxEWB2e3N3kh_IeYuNqetD6_FuNLQo6K5OQtqGhwoA0119Rk6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c3af8280.mp4?token=d4HMQt2VRPOhf2hTHxo5gXXid7ve0GSvCgRiKbz1gFdj75Kh7gMao4Re65XZgpWsNtn23uP6O6YObghVg8cKERWGUhnUbch_g9LUs3kDDnFXNDL4cNF1steQwWS-D80agcYoBqa_yVBk1KzcsgLz0k7CdzFMuVf1x6MKzzs7OQiulTph8dW10sv4Gc7gEeGLp5W0z7zoEguiB-c8mYn4xpJdT7EWQUzlIKQgppzwf7w9c1sC2X_5tDJIoM3s3Sji1fmVQ5q2OjZdhSregT9w2QX_-aKs_zTadPJTnxEWB2e3N3kh_IeYuNqetD6_FuNLQo6K5OQtqGhwoA0119Rk6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش مردمی :
دوباره زدن
، صدای صوت موشک قشنگ شنیده میشد چند ثانیه قبل از انفجار و الان صدای جنگنده میاد
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20465" target="_blank">📅 13:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20464">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSCe3T0Cp8Xd5sjkNuZDmBhMVn-idNlw57W5HaCTke9BWQbqnF5c3ZjG6nHsIb7gs_LKJ84PPQiOfWpBUH3MPUA5Iy8EG0VnC2FvwzWDyYAII0TpJPw5BSySEBQb6DtpCfH7EiIln7bKwsEXm2mpvZhNIfn6VrTeBILUGC-aeioTZatAY-9wm2rJoQbrgfEXfGqs12FkJb3X902TwpkYPSttQ5GO63E9jnih9vKNHBh6FqFcMnP-xWc5Z9rsJ-UHTnZ_0mFk8o-XzkYkskIJIH_EMC31MX8E8qeqjdIJ3h61_Rk3QUcEDGAo1NVNQ9XcgqULzpYaLqPXVB5ONSeVIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرک صنعتی شمس اباد فشافویه توی خیابون گلشن ترکید گزارش های مردمی تایید نشده : مورد ۱ :دو کارخانه منفجر شده مورد ۲ : کلانتری فشافویه رو زدن @WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20464" target="_blank">📅 13:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20463">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20463" target="_blank">📅 13:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20462">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20462" target="_blank">📅 13:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20461">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گزارش های بومی : زدن بدم زدن ! خودش نترکیده زدن ! ‌ کارخانه پهپاد سازی هم بوده ، ۲ تا کلانتری و کارخونه هم قبلا زده بودن همینجا (حسن آباد فشافویه) @WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20461" target="_blank">📅 13:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20460">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7200405da8.mp4?token=lIv8fyv_x-1XQQ1O1OMUBdqlxkyzE3QSjIka-xMYHA5ChHg0-ToDpBROFjtSdJscZh7_4-jborp_nND_Tk1Xw0MTRC5g7sxfEDmDNZvvwsJ34pcBMWsxMj2ByiSrVM-4eCFkXBhNW9cJlb0PH2AD6Ffo2bNCyqz0XQYp8P9H8XuTnJ5Q8p8fs4_qt-iyf1oFUxrgdLkStfKDIkhzdk00gTDHpuZLJJKKMC2nqCkJwSe6fl-tO4YI1ItZDNhTXSoGuXTMmnRvxKWq91GoUF9vX2_nfvfv82Ryx0fDnk7Fu7eI2ffu8W5RLiudc73IMIlX0I24OMASNbllZlPzO8DsPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7200405da8.mp4?token=lIv8fyv_x-1XQQ1O1OMUBdqlxkyzE3QSjIka-xMYHA5ChHg0-ToDpBROFjtSdJscZh7_4-jborp_nND_Tk1Xw0MTRC5g7sxfEDmDNZvvwsJ34pcBMWsxMj2ByiSrVM-4eCFkXBhNW9cJlb0PH2AD6Ffo2bNCyqz0XQYp8P9H8XuTnJ5Q8p8fs4_qt-iyf1oFUxrgdLkStfKDIkhzdk00gTDHpuZLJJKKMC2nqCkJwSe6fl-tO4YI1ItZDNhTXSoGuXTMmnRvxKWq91GoUF9vX2_nfvfv82Ryx0fDnk7Fu7eI2ffu8W5RLiudc73IMIlX0I24OMASNbllZlPzO8DsPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش های بومی : زدن بدم زدن ! خودش نترکیده زدن ! ‌ کارخانه پهپاد سازی هم بوده ، ۲ تا کلانتری و کارخونه هم قبلا زده بودن همینجا (حسن آباد فشافویه)
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20460" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20459">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqMRfYzpaKIFk7q9DImQH4I342qUMuDHjHCft86ZU5vXWp0wnNhKqwNEPEqX0OloJuLfkx6wscK5rwiSZHIf3IV7GZozrkkLtaCNTp7duDRcKmmMsN-fOJab7BMbpPbk3Kma_TYdVASlraIA5MpZy15jtbHS2O9vi-WSmAl9xBqGy8eWO5LPMhtx6a60SZ2LDBo3wmUY2lbFluURGKkG5SqLiQxv7cCZL0xt56Jxmpy9xEGtn_-Y_lVppCIezZd-o-laMLcobXNsanIwl4z0fDOsJnBOx-y8JzwElVvDbTJSbGSuO1HQtM_7V_QbVDYWySBI6bM5KwH7PsiBqamK0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرک صنعتی شمس اباد فشافویه توی خیابون گلشن ترکید
گزارش های مردمی تایید نشده :
مورد ۱ :دو کارخانه منفجر شده
مورد ۲ : کلانتری فشافویه رو زدن
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20459" target="_blank">📅 13:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20458">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20458" target="_blank">📅 13:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20457">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رویترز: یک کشتی باری در نزدیکی تنگه هرمز مورد اصابت پرتابه‌هایی قرار گرفت و یکی از ملوانان مفقود و باقی کشتی تخلیه کردند
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20457" target="_blank">📅 12:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20456">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دور جدید مذاکرات بین لبنان و اسرائیل در رم آغاز شد.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20456" target="_blank">📅 12:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20455">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کانال ۱۴ اسرائیل: رویکرد سخت‌گیرانه احمد وحیدی(فرمانده کل سپاه) به سیاست رسمی جمهوری اسلامی  تبدیل شده  و سید مجتبی خامنه‌ای تصمیم‌گیری درباره پرونده آمریکا را به او واگذار کرده است.
مذاکره رسمی بین تهران و واشنگتن در جریان نیست و تماس‌ها فقط از طریق پیام و میانجی‌ها ادامه دارد
@WarRoom
اتاق جنگ با یاشار : دقیقا در پست ۴ ماه پیش اتاق جنگ «نشانه» 10May به این موضوع اشاره کردم</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20455" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20454">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">روزنامه روسی Izvestia : آمریکا می‌خواهد با سردر‌گم کردن تهران زمینه را برای یک حمله غافلگیرانه فراهم کند
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20454" target="_blank">📅 10:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20453">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMJZQWJGcBffRiWVFPMGhAS9ddD0lNn5zTatxQmgfZJokaIUuhr4I9YER9mYVcFd3X41f6FwYT9oIZkJqo6EwC9ARlwAsv5xd0ehXgIbdHcfN6ukcLCp19XVHZYXbMpanSivyXnIKyXNbgzzJTJFWVoHAv8wD-ALJMfMf5gV08MQxIyUz6ZvN34gOYut3pZpLn2-Iq0GYvmfZshoxJBYE16qa56Hnv2vIwsJ4Xn8Id1icu_hNFF1tQ6acs8vxl2ai5eli3CQEjvl_Br-NwZvsXy0ObqOJUcjFOEncQt7VHRPx_8Mx6EH0kBSWJ7KqYqVG0iNDmFA7u4aJ2_mMZF-zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غزه قبل و بعد از ۷ اکتبر ۲۰۲۳
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20453" target="_blank">📅 10:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20452">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تلگرام از اپ‌استور اپل ناپدید شده است، اما تا این لحظه اپل یا تلگرام دلیل رسمی و حذف اعلام نکرده‌اند.      اپل قبلاً در سال ۲۰۱۸ هم تلگرام را موقتاً از App Store حذف کرده بود و دلیل اعلامی آن «محتوای نامناسب» بود؛ بعد از رفع مشکل، برنامه برگشت. @WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20452" target="_blank">📅 06:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20451">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">صدایی مهیب در پایتخت یمن، صنعا، شنیده شد، و هنوز علت آن مشخص نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20451" target="_blank">📅 06:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20450">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تلگرام از اپ‌استور اپل ناپدید شده است
، اما تا این لحظه
اپل یا تلگرام دلیل رسمی و حذف اعلام نکرده‌اند
.
اپل قبلاً در سال ۲۰۱۸ هم تلگرام را موقتاً از App Store حذف کرده بود و دلیل اعلامی آن «محتوای نامناسب» بود؛ بعد از رفع مشکل، برنامه برگشت.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20450" target="_blank">📅 05:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20449">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgR1Dp2KfuWXPYgx9R6IbDMIJaHkhpX92GZcxVxSx_mQTZJ0eoQPquS_O_ah6zx-cJV4ZAwEHuf9Wig7BEEc37JL6Ju6hLH6lUNwEQVOuXDIxfvscntUJu42sfNVeQ0TPKlpybnSDIw0ZBr8mOT6H9tzx_P-Zimwqu73iwHfORLrlLy_f0yvdlUEDTmHHsB-Hd4t4ald3fYkw3Tga-8V3xWf9VT8CE2jl3UMXk7ZYj6B2CvpU4xXlrplwmUbKM4NaLaGG0yL7HrzjVpkG3Km6u0SZYV47jZtC_Kr_dX3RW68jYEnNeQHpYrqD0OZsmJizUn8AMtlbVUH8v8l4JIrlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مذاکرات دقیقه نودی به درخواست عربستان سعودی
@WarRoom
😁</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20449" target="_blank">📅 04:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20448">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl1ruorwSoH5eDAXsBfcGTfntUQVWXa1tE8Rhuj0I-6QOoWj--SVTGN85euLzrBmL4sukaDOdIeNiacXNXrM1arMkr40oRwP9qVMtR3DynLMIuPXfhB1ADEyUxUkOrYO3kx0eadfpa9F_3vV_SAbv3rRXkrz1-7NG6CUYrf-va6IvsbET-WCTYwTGMdGaIRLx1rN8pU72-9rXM2fa_wfqZQPW_V3j73GCxhZ7ZZfmWnIbo8mOwVnnqxHamzybrURHkvv1iuhTL-cJM_7Uo_7Np5zKNoQ2TZiAs1793w3Mr9wym3mUMdBnjjlA_Md2a8-H-Bdi3CmnyHCDEOsbQr-bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریایی بریتانیا : گزارشی از حادثه‌ای در ۲۰ مایل دریایی شمال شرقی الخصب، عمان دریافت کرده است.
یک کشتی باری در VHF 16 اعلام کرد که مورد اصابت یک موشک/پهپاد قرار گرفته است.
مقامات در حال بررسی هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20448" target="_blank">📅 03:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20447">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEHwXaG-F98KOuF82B-4MANYg4CPpx_TChBqkCn2kkdO16Xnzxkxfvkoi1PpA9g6hgiV_o9LFQazkZZbyKI40rWukSDmSs9zv2Qu6iwbfPQVZnR8OYUDFeM_QTKkp4xTSsyBzxznP-l2MP15rEyzHuQT5wFbdAYrFlQnD6vkYbtxdj3jI4QxgTJ_GxR-RWbEXGnx_ZF8EUkWCRKSX-8jHRyF6SRZeZIFOjt0yqJTdI5dI3yhgrTcXApXx3FmMLPI3ArCJlA6CzBaguz2oK42FefIfgcsQLpuqIrJ50AGf0HZw7aQNH_e0nicH5U0xr0D4qSMuSOkMAZrUXr-Uz1ykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفت هواپیمای ترابری نظامی C-17 گلوبمستر هم اکنون در مسیر آمدن به منطقه هستند!!!
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20447" target="_blank">📅 03:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20446">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کانال ۱۴ :مسیرهای دیپلماتیک ایران عملاً از کار افتاده‌اند.
به گفته درور بالازاده، تحلیلگر کانال ۱۴، مجتبی خامنه‌ای،  رسماً اعتماد خود را از تیم‌های مذاکره‌کننده ایرانی و آمریکایی سلب کرده است. دکترین تندروانه و بدون امتیاز احمد وحیدی، فرمانده سپاه، اکنون سیاست رسمی آنها است.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20446" target="_blank">📅 03:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20445">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">لاکهید U2؛ شبح خاموش آسمان‌ها به پرواز در آمد
🚨
🚨
🚨
🚨
هواپیمایی افسانه‌ای که در ارتفاعی پرواز می‌کند که بیشتر جنگنده‌ها حتی به آن نزدیک هم نمی‌شوند. خلبان آن به‌دلیل پرواز در ارتفاع بسیار بالا، باید لباس مخصوص فشار بالا شبیه لباس فضانوردان بپوشد تا در صورت افت…</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20445" target="_blank">📅 02:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20444">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSkgoDfE16AFMcHJxiVFKspt8Wgf19Ouh6V68BvKqJmciTrtFMoNyJO4fm5uDvFIQ7dbFnWryR3DZoYngQQT0pq5XOyjSpngswdYWspCLzAaQHja98Xf9EMrgRmeac8hAk8lWoO9E7nOipYpb8ncZ_hJJWim01XUcELIhgLsab415VrhpZ1M8Df2_xG6aqX7of4T7CpnmFYPYCfMjlVvGSycVpI3-vDih7RZcsuXC_TWM3flAV_BiIyvctV9PgODwxhuzCXl-6nEcGdRyWNwikQ4Z39bDQtdBDEC9ZRyf4_1uZnU0yGrELVYQLUpauQuEsK_KWbBKqDsCD8wODQY1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاکهید U2؛
شبح خاموش آسمان‌ها به پرواز در آمد
🚨
🚨
🚨
🚨
هواپیمایی افسانه‌ای که در ارتفاعی پرواز می‌کند که بیشتر جنگنده‌ها حتی به آن نزدیک هم نمی‌شوند. خلبان آن به‌دلیل پرواز در ارتفاع بسیار بالا، باید
لباس مخصوص فشار بالا شبیه لباس فضانوردان
بپوشد تا در صورت افت فشار کابین، جانش حفظ شود.
با دوربین‌ها و سامانه‌های شناسایی فوق‌پیشرفته، از صدها کیلومتر دورتر کوچک‌ترین تحرکات را زیر نظر می‌گیرد و ثبت می‌کند. با وجود گذشت بیش از هفت دهه از نخستین پروازش، یو-۲ هنوز هم یکی از ارزشمندترین چشم‌های اطلاعاتی آمریکا در مأموریت‌های فوق‌محرمانه به شمار می‌رود
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20444" target="_blank">📅 02:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20443">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خبرگزاری های رژیم : شنیده شدن صدای انفجار در کویت و صدای آن از بصره عراق هم شنیده شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20443" target="_blank">📅 02:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20442">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گزارش پرتاب موشک از ایران
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20442" target="_blank">📅 02:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20441">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNjXc_75cKh2GLBnK23oQ1gmidjflj3_rt3og25tC5hgGjZM0RTwCsjrySFxaaPhnrPU4kmk06j1pvJztYfGrgPSVrSMaQWSuZEGtSqyZwnJX7tQZROrEou65JRD-Hd0-EPBffAXjKdjo6GhB5lOX7pcns5OwgF08Xhzmmbp2nY9xl7iQimIw-pebk0_EeFYC4lSCpMLxy0ajhPwKP3XnjdUIiS4JD3Q2iIxvxPpnNCeZd1qNFXm7O7Guj6AwI5OeblGVNQHc4r2yLUH-PAINP0J194xJAsFyh8ZKLUBXZQX-O7EFhx9gx93zsEuVNjCVYLE-LtxKMA-msWoJpg4yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت یه کاربر خارجی : اگه نقشه ایران رو برعکس کنید؛ چهره ترامپ رو میبینید!
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20441" target="_blank">📅 02:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20440">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پاکستان ادعای ترامپ درباره آغاز مذاکرات با جمهوری اسلامی را رد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20440" target="_blank">📅 01:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20439">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9BWFVsBTeoqqeqDw5ViQ0VxzmNvSD2sZiwbVyTKA5OWfEtnoFdR60TjViUsNGVQbrs6ixvojvJUCbmZBAKeRZqxhcaTK3EYmB-TulfCcUYohUiNEncboaoXLNw_bZJZh7YGwDJ4-tSXHJ-Mo-GdCEsce14hEqopraUkEQCzY6SJJ8qznVtwhbpGL1z9BOlDFe-E--Yuezpy1bjeK1_r5dD2Ck2vS2j-iJLcGgMk9pznI-FR7bbUtb8JiqF1wNrIbZ4a1ZC3oKK-AnVNt62eEJ6qcr5tL_43_F5ieQyze0EwbHr4zkyXuz0YXPzZPUDj4VCNRIOhVhDgrKumQ_vs4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد امروز روزنامه اسرائیلی (یدیعوت آحارونوت) : «تو ما را دیوانه کردی.»
‏ ترامپ: «من حمله خواهم کرد.» من حمله نخواهم کرد. من حمله خواهم کرد. من حمله نخواهم کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20439" target="_blank">📅 01:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20438">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bowBkrRJ3HOMq0S0K5cXJAEYAGB7bQWIObW-f-mCA3yPn1ooUfXIduzl5uaWuFpBmHRpOQe74PRimhdSTqTEEtef4MJbIEh3GIXuZ67uhENqzBTbqUBHv1mZcTHCGqRK6h2-ml7VkCQd7hbckJjqE5uNF2ATNVg_dPACbk2UZs3x6dYokrQwx6fCde9zZ4SCilVim6PzDYUHpaWuKxPr6z0r3LI6gEOdXDrkF8QncEkon4aWooDdPPUR5twzjjj5X_GFi1EqUE2Q5EhGz4tSz5GTRSq12mt9dSvCy6DZpgQxIGVeAmj8o6Yn_Is9RCqiY_YheMKO2y1VATC-IYAECw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون
یک پهپاد سپا، مقر یک گروه کرد را در منطقه خبات، واقع در استان اربیل غربی عراق، مورد حمله قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20438" target="_blank">📅 01:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20437">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : دلایل به تعویق افتادن حمله از طرف ترامپ اگه شما مورد دیگه ای‌میدونید بنویسید ، حتما تا آخر ببینید و کامنت لیک ریشیر فراموش نشه ( کارهای اداری )⁩ https://www.instagram.com/reel/Dbl_dAtIsre/?igsh=andsNWUxa2tqaHZs</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20437" target="_blank">📅 01:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20436">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2-71K3XV5bhEljkWppQsXBXjdOQ9WQV6ayygjySBgmLaxcgWumwBuL09Uc4JN90dq_1xIvVYlbBR_DCl1Uj5OAtgjUHO5jvjyM0nsX9u_sjzGOHjNbEajMC-9bJEYAiG3mzYyz-EjCxDH6IFfApvhXAW6SbKpwkd1OZKmbW8JG0TCtj5Tp0GC3n2DldT-vWAyWqHxucmv98bt43F5tEDvnvMKmYgsGPIJc6oG8Scd9odJ-6ZFcbo-CeTDvLRTMkXjCJuce32m6v1E465s0AjZWUPxk8hvRY__SMAKUHqhnhfX6DPRyPLah8ovOgg6Sirwa2EO6KkQtFMmkuDcNNsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : دلایل به تعویق افتادن حمله از طرف ترامپ
اگه شما مورد دیگه ای‌میدونید بنویسید ، حتما تا آخر ببینید و کامنت لیک ریشیر فراموش نشه ( کارهای اداری )⁩
https://www.instagram.com/reel/Dbl_dAtIsre/?igsh=andsNWUxa2tqaHZs</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20436" target="_blank">📅 01:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20434">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20434" target="_blank">📅 00:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20433">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20433" target="_blank">📅 00:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20432">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a075dbac8e.mp4?token=aAFLI9w5XYIMDZoRK0fI5C7jGoOWk5E5jqA1TAqDU5AfXb4yBEaMQxURxKk-5tWJ9S15fCGmPKk8Lnr2S5QniCOA7ipzBfz0W35dSHmwUBASL1ZryUEeEMGArjHOX9cZstgSTkkcht7XAbsX9vsepovgFKDFFkA2nKEu1A02fSOqZ4SUl3hb3tsKqi4X0ELrt-X7b_uIjZu2Ty_oCMX6JYITswzZQbFHOjt_h5rmLAvq_flKHDlSPeNfy4cuqAwDKAOmARxjsxWeuOm2i8XKKXDVdkBKortKjH2rWVYdaGUCbyrCqTxxx1IElVKQQaoHZYeUdkooBokOXzl8yA7CbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a075dbac8e.mp4?token=aAFLI9w5XYIMDZoRK0fI5C7jGoOWk5E5jqA1TAqDU5AfXb4yBEaMQxURxKk-5tWJ9S15fCGmPKk8Lnr2S5QniCOA7ipzBfz0W35dSHmwUBASL1ZryUEeEMGArjHOX9cZstgSTkkcht7XAbsX9vsepovgFKDFFkA2nKEu1A02fSOqZ4SUl3hb3tsKqi4X0ELrt-X7b_uIjZu2Ty_oCMX6JYITswzZQbFHOjt_h5rmLAvq_flKHDlSPeNfy4cuqAwDKAOmARxjsxWeuOm2i8XKKXDVdkBKortKjH2rWVYdaGUCbyrCqTxxx1IElVKQQaoHZYeUdkooBokOXzl8yA7CbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون ‏عراقچی در عراق
😂
(مراسم اربعین)
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20432" target="_blank">📅 23:36 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
