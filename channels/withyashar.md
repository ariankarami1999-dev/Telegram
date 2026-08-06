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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 05:16:35</div>
<hr>

<div class="tg-post" id="msg-20546">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تگه دعوا شد
🚨
🚨
🚨
گزارش پرتاب موشک از‌ سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20546" target="_blank">📅 23:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20545">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">به گزارش رویترز، به نقل از ۵ منبع:
رژیم ایران به کشورهای خلیج فارس هشدار داده است که هرگونه حمله جدید آمریکا به خاک این کشور، منجر به انتقام‌جویی علیه زیرساخت‌های حیاتی انرژی در سراسر منطقه خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20545" target="_blank">📅 23:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20544">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رئیس تروریستی سپاه، احمد وحیدی: «هیچ بحثی درباره اورانیوم غنی‌شده یا سلاح‌های هسته‌ای صورت نخواهد گرفت. تا زمانی که ایالات متحده آمریکا و اسرائیل سلاح‌های هسته‌ای در اختیار داشته باشند، ما به کار خود در این زمینه برای امنیت ملی خود ادامه خواهیم داد. اگر آن‌ها…</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20544" target="_blank">📅 23:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20543">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20543" target="_blank">📅 22:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20542">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20542" target="_blank">📅 22:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20541">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پزشکیان: حوادث دی‌ماه پارسال قابل فراموشی نیست؛ کسانی‌که کشته‌شدگان را 30-40 هزار نفر اعلام می‌کنند، نامرد و وطن‌فروش هستن
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20541" target="_blank">📅 22:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20540">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نیروهای یمنی اعلام کردند که با استفاده از یک موشک بالستیک، یک تانکر نفتی به نام "دیزی" که متعلق به عربستان سعودی است، را در خلیج عدن مورد هدف قرار داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20540" target="_blank">📅 21:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20539">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">محسن کج بند : به عنوان یه سرباز از‌ همه ایرانیا تقاضا میکنم یکمی دیگه این شرایط رو تحمل کنن، چون ما داریم بعد از آمریکا؛ چین و روسیه به قدرت چهارم جهان تبدیل میشیم؛ این شرایط گذاره
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20539" target="_blank">📅 21:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20538">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آکسیوس : دور جدید مذاکرات بین اسرائیل و لبنان که با میانجی‌گری ایالات متحده برگزار می‌شد، امروز ساعت 15:30 به وقت رم به پایان رسید. به دلیل تحولات میدانی، مذاکرات زودتر از موعد به پایان رسید، اما فردا صبح از سر گرفته خواهد شد.
بحث‌ها بر روی طیف وسیعی از مسائل سیاسی و نظامی متمرکز بود و بسیار سازنده بودند. تیم‌های فنی پیشرفت‌هایی در تعیین جزئیات کلیدی مربوط به اجرای چارچوب سه‌جانبه داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20538" target="_blank">📅 20:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20537">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نبیل الحمر، مشاور رسانه‌ای پادشاه بحرین، مدعی شد پدافند هوایی این کشور در حال مقابله با حملات هوایی ایران است.
وی افزود که در ساعات گذشته چندین حمله هوایی ایران رهگیری و دفع شده است.
پیش‌تر نیز هم‌زمان با هشدار درباره احتمال حمله هوایی، آژیرهای خطر در بحرین به صدا درآمده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20537" target="_blank">📅 19:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20536">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">منابع عربی از حملۀ موشکی به بحرین خبر می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20536" target="_blank">📅 19:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20535">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نتانیاهو : ترامپ یکی از بزرگ‌ترین دوست‌های ماست،اما یه چیز رو روشن بگم، موجودیت اسرائیل قابل مذاکره نیست چه توافقی بشه چه نشه، هر کاری لازم باشه برای حفظ آینده‌مون انجام می‌دیم
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20535" target="_blank">📅 19:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20534">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گزارش‌ها از حادثه امنیتی برای
بالگرد ترامپ در آسمان واشنگتن
رسانه‌های عبری گزارش دادند بالگرد دونالد ترامپ، روز گذشته هنگام حضور او در بالگرد، در آسمان واشنگتن درگیر یک حادثه ایمنی شد.
گفته شده در این حادثه هیچ‌کس آسیب ندید.
سازمان هوانوردی آمریکا در حال بررسی ابعاد این رویداد است.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20534" target="_blank">📅 19:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20533">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20533" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20532">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20532" target="_blank">📅 18:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20531">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سخنگوی وزارت خارجه درباره احتمال سفر قالیباف یا عراقچی به پاکستان یا قطر در پایان این هفته: برنامه‌ای برای سفر به این کشورها نداریم
سخنگوی وزارت خارجه: مختصات جغرافیایی مسیر مد نظر ایران و عمان، مورد تفاهم قرار گرفته
چنانچه برخی طرف‌های ثالث در این زمینه کارشکنی نکنند، بیانیه مشترک دو کشور مشتمل بر ملاحظات و نکات عمده مورد توافق نیز در مرحله بررسی و تدوین نهایی است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20531" target="_blank">📅 18:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20530">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">داشتون مثل پلنگ اینجاست
🐅</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20530" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20529">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اتاق جنگ با یاشار : رویترز تبر خورده خبر اشتباه زده
😂
https://ofac.treasury.gov/recent-actions/20260805  در این سند هیچ شرکت هواپیمایی ایرانی از فهرست تحریم خارج نشده است. آنچه حذف شده، همگی مربوط به شرکت هواپیمایی عراقی Fly Baghdad است که قبلاً به دلیل ارتباط…</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20529" target="_blank">📅 18:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20527">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اتاق جنگ با یاشار : رویترز تبر خورده خبر اشتباه زده
😂
https://ofac.treasury.gov/recent-actions/20260805
در این سند
هیچ شرکت هواپیمایی ایرانی از فهرست تحریم خارج نشده است.
آنچه حذف شده، همگی مربوط به
شرکت هواپیمایی عراقی Fly Baghdad
است که قبلاً به دلیل ارتباط ادعایی با نیروی قدس سپاه تحریم شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20527" target="_blank">📅 18:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20526">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عراقچی روز جمعه به پاکستان سفر می کند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20526" target="_blank">📅 18:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20525">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وال استریت ژورنال: ایران همه چیز را به کنترل تنگه هرمز گره زده است.
رویکرد تند تهران، اقتصاد و روابطش با همسایگان را تهدید به نابودی می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20525" target="_blank">📅 18:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20524">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رویترز : بر اساس جزئیاتی که روز چهارشنبه در وب‌سایت وزارت خزانه‌داری آمریکا منتشر شد، ایالات متحده تحریم‌های مرتبط با مقابله با تروریسم علیه دو فروند هواپیما و سه شرکت هواپیمایی مرتبط با سپاه پاسداران انقلاب اسلامی ایران را لغو کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20524" target="_blank">📅 18:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20522">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کانال۱۴ : مقامات آمریکایی تأیید می‌کنند که در هرگونه توافق احتمالی با ایران، تضمین می‌شود که تهران کنترل تنگه هرمز را دیگر در اختیار نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20522" target="_blank">📅 17:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20520">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رئیس تروریستی سپاه، احمد وحیدی:
«هیچ بحثی درباره اورانیوم غنی‌شده یا سلاح‌های هسته‌ای صورت نخواهد گرفت. تا زمانی که ایالات متحده آمریکا و اسرائیل سلاح‌های هسته‌ای در اختیار داشته باشند، ما به کار خود در این زمینه برای امنیت ملی خود ادامه خواهیم داد.
اگر آن‌ها سلاح‌های خود را کنار بگذارند، ما نیز این کار را خواهیم کرد
.»
@WarRoom
این رژیم قصد ندارد از اهداف هسته‌ای خود دست بکشد. آن‌ها در حال به دست آوردن زمان هستند. هیچ توافقی حاصل نخواهد شد.</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20520" target="_blank">📅 17:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20519">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ارتش اسرائیل: ما حملات متمرکز در جنوب لبنان را آغاز کرده‌ایم در پاسخ به نقض آتش‌بس توسط حزب‌الله.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20519" target="_blank">📅 16:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20518">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">برای اولین بار پس از حدود یک و نیم ماه، ارتش اسرائیل دستور تخلیه را در جنوب لبنان منتشر کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20518" target="_blank">📅 16:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20517">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یک مقام ارشد خلیج فارس به سی‌ان‌ان گفت که احتمال رسیدن ایالات متحده و ایران به یک توافق موقت در روز جمعه ۵۰ به ۵۰ است، هرچند تندروهای اصلی ایران هنوز آن را امضا نکرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20517" target="_blank">📅 16:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20516">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اصابت یک فروند پهپاد دریایی به یک کشتی و بروز آتش‌سوزی در آن
این کشتی هدف حمله یک شناور سطحی بدون سرنشین قرار گرفت که در پی آن آتش‌سوزی در عرشه کشتی رخ داد. نیروهای محلی تمامی خدمه را نجات دادند و آن‌ها در سلامت کامل هستند. غرق شدن این کشتی تأیید شده است
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20516" target="_blank">📅 15:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20515">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حسن روحانی: یک اقلیتی هستند که می‌گویند «اگر این جنگ تشدید و گسترش بیابد، امام زمان زودتر ظهور می‌کند! برای ظهور امام باید جنگ را تشدید کنیم»
رهبر پیشین هیچ‌وقت به دنبال جنگ نبودند
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20515" target="_blank">📅 15:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20514">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHpuuumOeRsDXp6srhwZnx9cMFNOnkHVfk1_feXayRGLU584R_Sn3jIQdWjMxG6Dpd9dAKUr9NNVQ0wl9zBM9zS9pucRJzw-9FU76HBB_6-bY-N7ydcyLrdEtLStqKgktAo25RmwSNrZx9msDReL-HmHu27thmLtmmpmD_G6tc9Xf6GQ3CVC-5ZD2Qexv12wam_6-U2_d9ZGveoC1dXbifAhkUOYW8NNO4S0PP4Swd8IK_KTZrr1ZShjOd71epGU3hkjpoR8poPmauopkxDZgDEhjsJ3CmHBqLJwAylhZaAjsdROfQ_S_TYqvYhNECD_fXZ3QOKYkUFq8L52sihmaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله هوایی اسرائیل به منطقه المنصوری در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20514" target="_blank">📅 14:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20513">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okenti8icJrjLwkp_ddEXpkWHNbUyWEiQ_N5iR-mHH_l_UtZa2nf7JD4oe4B-t0piiPGKYCrNetCPTz_V_JB0qaMfLziS-q6HzraL6nxTR84txLonkh9b9hOVLOFgFlew6XBXLx8WJP3rdTSpDiZaxdrX9wupGK63A2b4KUWavEIEnaqTSLUpc_vlxe1coZE2WjaRMa7FG7sIrtgrEGFKNK2YfSe-sK4Sdmtj8xPImn2G4engDIQAJY0DZNsMUPkVY-BjDSzMSx_7Udmkd3IQlHXzIBuTHuEwxhRWUp3o_oU0SKkZaNE6Nv6rStmTRY85umtGybJ-lWWtV74hQjqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش از فروپاشی اتحاد جماهیر شوروی، دریای خزر تنها میان ایران و شوروی مشترک بود و همین موضوع باعث شکل‌گیری این تصور شد که ایران از سهمی معادل ۵۰ درصد برخوردار است. اما پس از استقلال سه کشور آذربایجان، قزاقستان و ترکمنستان، رژیم حقوقی خزر تغییر کرد و در سال ۲۰۱۸ پنج کشور ساحلی «کنوانسیون رژیم حقوقی دریای خزر» را امضا کردند. این کنوانسیون سهم مشخصی برای هیچ‌یک از کشورها تعیین نکرد و تعیین مرزهای بستر و زیر بستر را به توافق‌های دوجانبه واگذار کرد. منتقدان معتقدند نتیجه عملی این روند و نحوه مرزبندی، سهم قابل بهره‌برداری ایران از بستر و منابع نفت و گاز خزر را به حدود ۱۱-۱۳ درصد کاهش داده و دسترسی ایران به بخش بزرگی از منابع انرژی این دریا را محدود کرده است. در مقابل، مقام‌های جمهوری اسلامی تأکید دارند که ایران سهم ۱۳ درصدی را نپذیرفته و مذاکرات برای تعیین مرزهای نهایی همچنان ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20513" target="_blank">📅 12:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20512">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6a7e2519.mp4?token=Nq7wBFOzYGwemfkVOIZh4odPUxSyfFl3XArRUMKlVOZYv4ZilFz1BruiZ6VCMJ5yDlQMCXfPC5xJNqFXRu81fQryXM20_EulxLv7T8Yw3bN7ms9DqMWJX6d9y14NqmU09VooMD7UPfxL0P4IDREln9r3hZQAUMZLqgwRVVtBUKpzPlSdHN17wU6f2kDSRkCQI5T38WjSNcfu2l6GG1fo2_yFCDo3JkSL-Jx0TVMaJkgRm4BTOrCe1POskljsT5Sa5So4rsg5gjByoSZU2u2B9jDU-TKH_xYaNjzvb2bQ8sL8zbbKRjtTJLvQqogeS9ulRqoMbSaMZ59aDRm49_zM_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6a7e2519.mp4?token=Nq7wBFOzYGwemfkVOIZh4odPUxSyfFl3XArRUMKlVOZYv4ZilFz1BruiZ6VCMJ5yDlQMCXfPC5xJNqFXRu81fQryXM20_EulxLv7T8Yw3bN7ms9DqMWJX6d9y14NqmU09VooMD7UPfxL0P4IDREln9r3hZQAUMZLqgwRVVtBUKpzPlSdHN17wU6f2kDSRkCQI5T38WjSNcfu2l6GG1fo2_yFCDo3JkSL-Jx0TVMaJkgRm4BTOrCe1POskljsT5Sa5So4rsg5gjByoSZU2u2B9jDU-TKH_xYaNjzvb2bQ8sL8zbbKRjtTJLvQqogeS9ulRqoMbSaMZ59aDRm49_zM_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : تحمل کنین تخت گاز داریم میریم ! داریم میریم سمت قاهره ! غر نزنید دایرکت ! تمام  این مسیر این شیشرو با هم حمل کردیم !
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20512" target="_blank">📅 09:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20510">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20510" target="_blank">📅 09:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20509">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏پیت هگست، وزیر جنگ آمریکا، در واکنش به گزارش فیک‌ CNN مبنی بر اینکه ذخایر موشک‌ها و مهمات آمریکا در جنگ با رژیم جمهوری اسلامی به شکل هشدارآمیزی کاهش یافته است، گفت: «شرم بر شما باد! سی‌ان ان گزارش شما حقیقت ندارد. خجالت بکشید. ما باید بسیار بیشتر از این از رسانه‌های جعلی متنفر باشیم.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20509" target="_blank">📅 09:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20508">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یک منبع ایرانی به المیادین:
توافق در مورد تنگه هرمز به تعویق خواهد افتاد تا زمانی که آمریکا به تهدید علیه ایران ادامه دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20508" target="_blank">📅 09:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20507">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">صندوق سرمایه‌گذاری عمومی عربستان سعودی (PIF) به همراه سرمایه‌گذارانی از جمله شرکت Affinity Partners متعلق به جرد کوشنر، خرید ۵۵ میلیارد دلاری شرکت Electronic Arts (EA) را تکمیل کرد و این شرکت را به یک شرکت خصوصی تبدیل نمود.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20507" target="_blank">📅 08:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20506">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">طبق نظرسنجی ها در اسرائیل و اطلاعات کانال 14 اسرائیل :
بنیامین نتانیاهو همچنان میتونه نخست وزیر اسرائیل بمونه بخاطر محبوبیت زیادش و رای بیشتر
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20506" target="_blank">📅 08:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20505">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20505" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20504">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فردی مسلح دو روز پیش از حضور دونالد ترامپ در باشگاه گلف او در کالیفرنیا بازداشت شد.
پلیس اعلام کرد این مرد ۳۸ ساله که
ژنین جان تائله
نام دارد، در حال عکاسی و فیلم‌برداری از محوطه باشگاه بوده و ظاهراً فعالیت‌های امنیتی را زیر نظر داشته است. هنگام بازرسی، یک خشاب ۱۶ تیر و مهمات در جیب او و یک تپانچه پر در خودرواش کشف شد. با تفتیش منزلش نیز چندین سلاح، مهمات، جلیقه ضدگلوله، خشاب‌های پرظرفیت و دفترچه‌هایی با نوشته‌های «نگران‌کننده» به دست آمد. پرونده اکنون با همکاری FBI، سرویس مخفی آمریکا و کارگروه مشترک مبارزه با تروریسم در حال بررسی است
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20504" target="_blank">📅 06:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20503">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آکسیوس: آمریکا، ایران و عمان به توافقی موقت ۶۰ روزه برای بازگشایی تنگه هرمز نزدیک شده‌اند و واشنگتن قصد دارد آن را روز چهارشنبه اعلام کند.
بر اساس این توافق، کشتی‌های ورودی از مسیر شمالی در آب‌های ایران و کشتی‌های خروجی از مسیر جنوبی در آب‌های عمان با هماهنگی ایران عبور خواهند کرد و هیچ عوارضی دریافت نمی‌شود. همچنین مین‌های دریایی مسیر مرکزی طی ۳۰ روز پاکسازی شده و سپس این مسیر برای تردد دوطرفه بازگشایی خواهد شد. قطر، پاکستان و عربستان نیز در میانجی‌گری مشارکت داشته‌اند و کاخ سفید مستقیماً در مذاکرات حضور داشته است. عباس عراقچی با این چارچوب موافقت اولیه کرده بود و به گفته منابع آمریکایی و منطقه‌ای، مجتبی خامنه‌ای و شورای عالی امنیت ملی ایران نیز روز سه‌شنبه آن را تأیید کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/20503" target="_blank">📅 06:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20502">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رسانه های عراقی طرفدار رژیم :
شنیده شدن صدای مهیب انفجار از سمت ایران در منطقه شلمچه در نزدیکی مرز آبادان
@WarRoom</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/20502" target="_blank">📅 23:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20501">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مارک لوین : دیکتاتور سعودی دوست نیست
@WarRoom</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/withyashar/20501" target="_blank">📅 22:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20500">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/049666fcb2.mp4?token=TrLT6NuVMqmkgfTOU-iQSFaheHeg1T1nsM1-XbzoFuosZf3uT67PbCIP437MikJ6Od6DF6_j5bAJ1JVjXkwAHyNsH06R5f25sSg_VPMGbKVyivZAxRyVoHo9jDycUTpV9bwvUsRlfyg-n_th8McCZxwcWSGfwoMflvhIOUuNHsePF_DF4nL-1MPN1djPqZXUMPeiRxMINwLDtAykjNl1wngMt1w0FWxZDefsDEo3ZTBACistKKBGuPzPHb2gMahtVe-KkcMyEJjsWMwuIStxZQkhznNcrULSSAAOVLkQGmQkAGNAFW-KQ6rbBX81fpYYuYTogDvIzGNtmKiXxkFNbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/049666fcb2.mp4?token=TrLT6NuVMqmkgfTOU-iQSFaheHeg1T1nsM1-XbzoFuosZf3uT67PbCIP437MikJ6Od6DF6_j5bAJ1JVjXkwAHyNsH06R5f25sSg_VPMGbKVyivZAxRyVoHo9jDycUTpV9bwvUsRlfyg-n_th8McCZxwcWSGfwoMflvhIOUuNHsePF_DF4nL-1MPN1djPqZXUMPeiRxMINwLDtAykjNl1wngMt1w0FWxZDefsDEo3ZTBACistKKBGuPzPHb2gMahtVe-KkcMyEJjsWMwuIStxZQkhznNcrULSSAAOVLkQGmQkAGNAFW-KQ6rbBX81fpYYuYTogDvIzGNtmKiXxkFNbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ عازم لس‌آنجلس و لاس‌وگاس شد
@WarRoom</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/withyashar/20500" target="_blank">📅 22:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20499">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سنتکام اعلام کرد که از ابتدای ازسرگیری محاصره دریایی اعمال شده علیه ایران تاکنون 45 کشتی را ملزم به تغییر مسیر کرده و دو کشتی را با هدف‌گرفتن آنها ازکار انداخته و دو کشتی دیگر را مورد بازرسی قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/20499" target="_blank">📅 22:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20498">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ou4in2Fh0RynLXUGls6uufw7c-AZ7qlrg6Pu9Rf-Qokxt90dkdOY0MlRjQGkrmEsI0f14fWWSuR65BksziekwSoFwD_BXIb8e5H-IW98BqNl8sXLvhfYz9776TyFV9Z-H3gCBohpBdmlZeHU8O25WOcajoW723uPQTg8mbgJN_r_CnvzDlJEjfQENzMBKVfZu1BkV6ph4hzU8RUgMr1tGmUiWwlM_N2nGqf9M6UFcyfZtxpTYHAUry9z0rcdDojTolBsHELsxkoGMD-HiW4CCv_-UU_l-A4phzSUU0zOmB2Dgq8-8b8F4G-QmrwwCe1TDzT39-M5KEC7HoOFLN3gdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ۷۹.۳۵$ شد و به زیر ۸۰ اومد
@WarRoom</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/20498" target="_blank">📅 21:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20497">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وال استریت ژورنال: اگرچه واشنگتن تأکید دارد توافق ممکن است به‌زودی نهایی شود، اما ادامه حملات دریایی و اختلاف بر سر شرایط و هزینه‌های بازگشایی هرمز، همچنان مهم‌ترین موانع پیش روی مذاکرات هستند
@WarRoom</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/20497" target="_blank">📅 21:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20496">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نتانیاهو:
ترامپ و تیمش معتقدند می‌توانند حماس را وادار به خلع سلاح کنند و غزه را کاملاً غیرنظامی سازند. آن‌ها پیش‌نویس این طرح را برای ما فرستادند، اما ما با آن موافقت نکردیم. این پیش‌نویس، طرح ما نیست؛ ما اصلاحات و نظرات خود را برای آن ارسال کردیم. جالب اینکه این نظرات را پیش از آغاز جنجال و فضاسازی رسانه‌ای درباره این موضوع فرستاده بودیم. این موضع رسمی ماست و با درایت، قاطعیت و حفظ منافع خود، بر آن ایستاده‌ایم.
@WarRoom</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/withyashar/20496" target="_blank">📅 21:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20495">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فاکس نیوز:یک مقام ارشد دولت آمریکا فاش کرد که لغو جنگ توسط پرزیدنت ترامپ در واقع بخاطر لو رفتن زمان جنگ در رسانه ها بوده و ترامپ این جنگ را فقط به عقب انداخته و مشاورانش به او گفته اند می تواند در این بین و برای آخرین بار به جمهوری اسلامی فرصت مذاکره و توافق دهد و در غیر این صورت در تاریخی که از قبل معلوم کرده و این دفعه امیدوار است لو نرود، حمله بسیار گسترده به ایران را انجام دهد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/20495" target="_blank">📅 20:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20494">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4509abf5f6.mp4?token=ba5R50QJebB1QdXJY5AzaTTz7hKS6eO2jXJyNPc2UJWShoB06XE22BZNvNehdThLveh73Nh_dobPu7CwTk3Wy2FhjBKQwT1AY08YhWKNrLq_DO1qoC0t_Szhq-CyabEej-G31LuM_YsnDIox9boDng43mVJy0lpWu-56o4o1XmuzG9XXtQ4mfjchvTyTW5UdSWrjEKMVIkAYW0pLmFvyCAu7QPny4Xff3e-C7aIXVdY7sRNCQM4CLtcpbVFBzQf3ZDQtgm7c7eW75RCJkg3gihD9G2bu79aWaDQfTFPt6ZSCU0t8Hxw9HdZFAiVS455M7BmFW6r74DEfBGm9l-oTTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4509abf5f6.mp4?token=ba5R50QJebB1QdXJY5AzaTTz7hKS6eO2jXJyNPc2UJWShoB06XE22BZNvNehdThLveh73Nh_dobPu7CwTk3Wy2FhjBKQwT1AY08YhWKNrLq_DO1qoC0t_Szhq-CyabEej-G31LuM_YsnDIox9boDng43mVJy0lpWu-56o4o1XmuzG9XXtQ4mfjchvTyTW5UdSWrjEKMVIkAYW0pLmFvyCAu7QPny4Xff3e-C7aIXVdY7sRNCQM4CLtcpbVFBzQf3ZDQtgm7c7eW75RCJkg3gihD9G2bu79aWaDQfTFPt6ZSCU0t8Hxw9HdZFAiVS455M7BmFW6r74DEfBGm9l-oTTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : جنگنده رادارگریز F-22 نیروی هوایی ایالات متحده در حال دریافت سوخت از یک KC-135 Stratotanker در آسمان خاورمیانه
@WarRoom
🚨
🚨
🚨
🚨
یاشار: اف۲۲ ها هم اومدن منطقه و آماده هستند</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/20494" target="_blank">📅 20:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20493">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تلویزیون ایران: اگه ترامپ خودش بزاره ما توافق میکنیم ولی دخالت میکنه نمیزاره
مذاکرات بین دو کشور ساحلی در حال انجام است و هیچ ارتباطی با ایالات متحده ندارد، اما ترامپ با دخالت‌های مکررش، تلاش می‌کند این تصور را ایجاد کند که بر روند این مذاکرات تأثیر می‌گذارد.
ایران در تلاش است تا به صورت مستقل از تهدیدهای آمریکا، به پیشبرد برنامه‌های خود در مورد تنگه هرمز ادامه دهد و تأکید می‌کند که تأثیر ایالات متحده بر این مذاکرات تنها منفی بوده است، و تهران منافع و اولویت‌های خود را بر اساس زمان‌بندی یا خواسته‌های ترامپ تعیین نمی‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20493" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20492">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یک کشتی کانتینربر متعلق به هند در دریای سرخ به وسیله یک قایق انتحاری، نزدیک بندر حدیده یمن، منفجر شد و در حال غرق شدن است!
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20492" target="_blank">📅 19:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20491">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWfmUEuImWxolIv8fg1uVuPDmzMtqJHwK8R-hQFxdN_ycakhq79GdY1Rx_Npo5Mb54XhAoaNDJBtBznQIqAogeMOUKPhvNu-uiTW-pbnFSK6f7GfbjTnCSdeuDoR_JHmfHxK3td1udWf11rHcRcc9hSnvH3ZazOlQriPmGD30S00ejVoABmIrPebxhz0ebZCAG07pkMi7Buho-MtF5o8uZKxGd1KTcsEvgbnhyG5_a_cXzHpdeNnHoPChTV_hohB-2uuU3qIsXGLgEPM0hMpzw5-ch8n9BhLJ-_TLfHqyMq9gto3hyFUa0XZMAv9_z6QUH8L1ZT3JrXruXz6nFO__w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود اهواز ….
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20491" target="_blank">📅 19:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20490">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ادعای ‌اینترنشنال :بر اساس اطلاعاتی که به دستمون رسیده، ملاقات پزشکیان و مجتبی خامنه‌ای که تو اردیبهشت انجام شده، زمان خیلی کوتاهی داشته.این دیدار داخل پناهگاه نبوده و تو یه محل امن، داخل ماشین انجام شده.
ادعا شده پزشکیان و مجتبی خامنه‌ای روی صندلی عقب ماشین نشسته بودن، اما صورت همدیگه رو نمی‌دیدن و گفت‌وگو به همین شکل انجام شده.
همین موضوع باعث ناراحتی پزشکیان شده و گفته: «اصلاً معلوم نیست اون شخص مجتبی بوده یا نه؛ با این کار منو تحقیر کردن.»
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20490" target="_blank">📅 19:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20489">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4W57ZumP1DG5_BPn4KFwnZBmH9qNRwgfBj3FJxcbrJp7_6ffzK-uLzyATiAV-9QwCq86uXQe8Bqq9JnNxEReDtwPOHrGZ2f5W3uf2MLmXB6yYzPvDMguO3PhWIXqcior8RgEI1zSjXmGKy9LHu-vBG6zXBoG4hjjh845TK-Ig3edbI1IC36kqZ6dqeHb9yrH0ZRX2wi0X5_2utCwQL3VosW_VbQyLf_2fLHXBlbuwZyw6kv81BxOMy3uKR4v0QSgKxgRmbfbqC9wfYSSeQRDvwW1L_IayCyVlOWrVP7wYX3lTGIxGGrreXJaIr_iB3FWgBnORjScQZ3jxDug_Fv7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای توافق اهواز همکنون …
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20489" target="_blank">📅 18:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20488">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XncNj04q9IRfpXzSw_7SvslfOn67FwqxnAjroHHKRijOuzCalYwNLXy6GKb9bEJKq52Rr5pz8qS0kvvQ5We5y8gPbApS-3jLYWXSogAl_KUY7U8WHAhU-GDI7WWA_WxK_-D9vd_9nBpx1uuSjJXyhtMxA5xQnCFtxjPXCZXEeZzK8oybLEaijcTKVzVRvReAY65EC8e4Z1FsPYGH4XFOO_lmOoHPxWi31wUpB_r6vJf7K2rLnO8SUfWNziVgJV-a76-FRxo2Hq71I3uC3ACptsY3oWSn2gvOdjpBzrXE3_0PDL_mjt_DGqZXFn2v6lNkWkQLJCEm0jyQyqIumW5KDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «توافق قریب‌الوقوع است» همزمان با از سرگیری مذاکرات ایران در روز دوشنبه درباره خلع سلاح هسته‌ای
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20488" target="_blank">📅 18:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20487">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lm6i_qng-CZxeR0NEltaCTrvMQCd3BxTIacR2pjhGCAIXR1_z3YYUp4aFIh2k1F6ACHWtNH5x805Sd2ySZ9Ptyg_WCygFdm2EYmID14O4UeaZNfpnXRI1qWVw8JSexVC709yiTKQlVFK-4ELs-cnvpOLtHRooDdlpWC0fACFO1PChBJOqtbQFXwKvgh1HRQqcByYIh0JLJYl39NAEz8pHob6abwKXUWJDR-RPfDPyOFPCOyrWjpw-gg-XHh__dMEI5EMBGODQt-xoLQ5-mIFXJMHzyhEiuYiJhlVYZNCzVqQqFyCasGyLyZp4ii0mn5BdZZ-lH1DGZC0ePxhWowYDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام ياشار همين الان پادگان سپاه بانه انفجار شديد
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20487" target="_blank">📅 18:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20486">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa412933a5.mp4?token=UmIHZhMvUjbz67SNG4774Fn8LAa-UDeTNeAf0ikj1PDQv_yB3VzMXwj6GY6WYxV90woK337dQ5Oq-vkE4Itr8VMs56zEDM0VuF0l2ofo62QzKs77xUMovjjrGeNIyqkqh3J-PkeRO0EwhfNJ69b_Oz9WwraJCXzG74LGBkexr7T5Hk9WMRe6OmRXoafQOIp_95109P-oCU5r0ZoMiiiRw9d_0HBS1QmYqXs-0jO-myVYfhmQgO5I52sZrm9pqF3m4MC5JWQD_IGJZrrIb7pVSCbjgTb6dUZzA-On7Sll1DDWVlO65oNcVK0MZva0dHA3hZertRDIbDqvv8qRLkrOtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa412933a5.mp4?token=UmIHZhMvUjbz67SNG4774Fn8LAa-UDeTNeAf0ikj1PDQv_yB3VzMXwj6GY6WYxV90woK337dQ5Oq-vkE4Itr8VMs56zEDM0VuF0l2ofo62QzKs77xUMovjjrGeNIyqkqh3J-PkeRO0EwhfNJ69b_Oz9WwraJCXzG74LGBkexr7T5Hk9WMRe6OmRXoafQOIp_95109P-oCU5r0ZoMiiiRw9d_0HBS1QmYqXs-0jO-myVYfhmQgO5I52sZrm9pqF3m4MC5JWQD_IGJZrrIb7pVSCbjgTb6dUZzA-On7Sll1DDWVlO65oNcVK0MZva0dHA3hZertRDIbDqvv8qRLkrOtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران
: در مذاکرات برای بازگشایی تنگه هرمز پیشرفت حاصل شده است، اما هنوز توافق نهایی به دست نیامده است. ما امیدواریم که توافقی خیلی زود نهایی شود
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20486" target="_blank">📅 17:57 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20485">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ادعای رسانه‌های کشورهای حاشیه خلیج فارس:
به‌زودی بیانیه‌ای درباره بازگشایی تنگه هرمز منتشر خواهد شد
،
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20485" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20484">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Si9Ptt4jsD7dvrsYREcK4z4oGLO9qu60TWo5V5V6_duLAlTBrjxiZFWq7v8JkmeUFI0wpCMdieLeXsTiNcU8lQHqi6_aIFOK4iX1sd1KQrJ93EEzUuTN32-MvzLKk_7zYVHF1QtBQ0fpebUka-tqKU3CEn7fOfCON-OHu4xW9-NrLeInudJl09TgZmdEr9HJorGWL5Y6EXx2T-6ewxDhKwzH8SMTGHQ6CXAAdCwfTu8amBPBIvNaxxRFW3QIAnIOyWXcEKBcZ6o6cQTszxJ67_kJYG0P7KIp8wjDyh5XA5jukfrm1nkgsaZ7xgOeUGjGgcV0VHf78_ns3btma5wgLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا، در مصاحبه با CNBC، گفت: ممکن است فردا با ایران برای بازگشایی تنگه هرمز به توافق برسیم.
کاهش نفت و افزایش اونس طلا بعد از این مصاحبه
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20484" target="_blank">📅 15:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20483">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">«تبریزی»سخنگوی اورژانس تهران : ۱۸ مصدوم در حادثه انفجار در شهرک شمس‌آباد
متاسفانه پایگاه اورژانس هم در نزدیکی محل حادثه به دلیل موج انفجار تخریب شده است، علت انفجار در دست بررسی است.
@WarRoom
یاشار : دقت کردی ؟ موج انفجار ! علت هم هنوز مشخص نیست!  فقط بی بی میدونه</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20483" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20482">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بلومبرگ : ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20482" target="_blank">📅 14:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20481">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یک مقام ارشد پاکستان به گاردین:
مذاکرات میان جمهوری اسلامی و امریکا،
به بن بست رسیده است!
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20481" target="_blank">📅 14:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20480">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">قطر: متن اولیه برای یک توافق  آمریکا/ایران تدوین شده است
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20480" target="_blank">📅 14:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20479">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اتاق جنگ با یاشار :میگن کارخانه آلومینیوم کاران بوده بد نیست بدانید
آلومینیوم یکی از مواد پرکاربرد در ساخت پهپادها و موشک‌ها، از جمله پهپادهای شاهد-۱۳۶ و آرش، به شمار می‌رود. از آلیاژهای آلومینیوم در بخش‌هایی از سازه و قطعات داخلی استفاده می‌شود و هم‌زمان از کامپوزیت‌ها و فولاد نیز بهره می‌گیرند. این فلز همچنین در ساخت موشک‌های بالستیک، کروز و برخی موشک‌های سوخت جامد کاربرد گسترده‌ای دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20479" target="_blank">📅 14:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20478">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وزارت خارجه قطر: تا کنون هیچ توافقی حاصل نشده است و در حال حاضر، مهم‌ترین مسئله بازگشت به مسیر دیپلماتیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20478" target="_blank">📅 14:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20477">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b588c7cf3.mp4?token=tS_mifpP4RlkAw3uTTt6MMjCcKIcX7wtoYGUHpy1HQDseOuYMUav0cicjbl0f1hzIizeG1hze39EW-0ip5lzyc4vrKY1P8DYS0cb-iBA3DDYMZX4aMZCrZcK8mbqy2MlljdlFn5e85bZif_fSQL2M0UDY3McGAhm8awvDu2Jv3qvf6U62XmJrowO_IFYiJ0Nft-neZV38249NpWDc_it6Np0cXqzRWAlmEnRhOBA7q1AQTBcbn2yCSBEAVZppzEZ6KavaOd2HVXhtWJT-5Hu5mGoKTxAAc1D5e8bv44IF6WEjHf09-Y-HZ3DFtXfFkTeIlb3ueOBMB3mnHOwGuS0sQxx7vvDOOUKg52nP9ox0R9Kj_W8SPOSvBtbGWl9tj24q2mz5pJumS2ckew5ZVESNqMIfM76nHsORTQz8uKYRAZbw_LYcBSc88ZHKxaBx0pv7JKpLwVAbKDW6ViCP6chwpQ9X1D-wTbb5FqVXFSHlcGWpt3AhTCkB7uhDLYuyyC2QAc1ciC9Zh3c1OOkiHK4LOYExyj6E5aJeSetiT1jhydWtUgDzahBx77vVPfVr-8I6xL9pcq0SRG5KC9pCKYJ7QGXmVFwh4SHcqrxbymrRPIm0ioJJ4e8M0X7IwQZgvY8CKY_f6iIEvdAlPtCXQlerDe5I0zekhfH60nu2hxtpsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b588c7cf3.mp4?token=tS_mifpP4RlkAw3uTTt6MMjCcKIcX7wtoYGUHpy1HQDseOuYMUav0cicjbl0f1hzIizeG1hze39EW-0ip5lzyc4vrKY1P8DYS0cb-iBA3DDYMZX4aMZCrZcK8mbqy2MlljdlFn5e85bZif_fSQL2M0UDY3McGAhm8awvDu2Jv3qvf6U62XmJrowO_IFYiJ0Nft-neZV38249NpWDc_it6Np0cXqzRWAlmEnRhOBA7q1AQTBcbn2yCSBEAVZppzEZ6KavaOd2HVXhtWJT-5Hu5mGoKTxAAc1D5e8bv44IF6WEjHf09-Y-HZ3DFtXfFkTeIlb3ueOBMB3mnHOwGuS0sQxx7vvDOOUKg52nP9ox0R9Kj_W8SPOSvBtbGWl9tj24q2mz5pJumS2ckew5ZVESNqMIfM76nHsORTQz8uKYRAZbw_LYcBSc88ZHKxaBx0pv7JKpLwVAbKDW6ViCP6chwpQ9X1D-wTbb5FqVXFSHlcGWpt3AhTCkB7uhDLYuyyC2QAc1ciC9Zh3c1OOkiHK4LOYExyj6E5aJeSetiT1jhydWtUgDzahBx77vVPfVr-8I6xL9pcq0SRG5KC9pCKYJ7QGXmVFwh4SHcqrxbymrRPIm0ioJJ4e8M0X7IwQZgvY8CKY_f6iIEvdAlPtCXQlerDe5I0zekhfH60nu2hxtpsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمس آباد یک انفجار یک سمت و بک انفجار سمت دیگر !
حالا عرزشی چی میگی ؟ گاز و گوزه ؟!
🤣
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20477" target="_blank">📅 14:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20476">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0d135103.mp4?token=KXdS7Mo8WD0wShWHs4lj5_ljgEQEvzsjKidVvALAvsd5LuGM8yqslHbFZRx0lmNuuubo7fXH-RKexSR4G7xHV9c09BLoq4s5a-T9qBYywulbVd9QuZDEYcuKuUJ2ML2icD7p1gJOMhaUz4laOAdf_38coq-THoP37g2lD_SROYKwGy3goC9WT-XF4A-Y_ZQu98oCGWrxZSJTSL12GDeJbQ9qwyLapYY8pKfyDxfXU0QIFW-iVbhN50C-Khg9NgTCqgsx7MKkJZiVt6UxrZ9wGvLYqX11p2ZCFtXXqrd6bIc--SPv5ClNh-5P5D_OkbAvOYvEc2Xtnz5uXlzoL_ql6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0d135103.mp4?token=KXdS7Mo8WD0wShWHs4lj5_ljgEQEvzsjKidVvALAvsd5LuGM8yqslHbFZRx0lmNuuubo7fXH-RKexSR4G7xHV9c09BLoq4s5a-T9qBYywulbVd9QuZDEYcuKuUJ2ML2icD7p1gJOMhaUz4laOAdf_38coq-THoP37g2lD_SROYKwGy3goC9WT-XF4A-Y_ZQu98oCGWrxZSJTSL12GDeJbQ9qwyLapYY8pKfyDxfXU0QIFW-iVbhN50C-Khg9NgTCqgsx7MKkJZiVt6UxrZ9wGvLYqX11p2ZCFtXXqrd6bIc--SPv5ClNh-5P5D_OkbAvOYvEc2Xtnz5uXlzoL_ql6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار اسلامشهر هم اکنون
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20476" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20475">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTrlVtWDR7xmUBhf0pTlYhQ-GMB9IkT8bY3ri8poePNNhFP9Yibgf9_Zer7R-OoDh1AMg53mZjeWXMPTYSs2UMaaV9cXFjAuCOlMUl6n19IIVhRHgi8o0eT8mAOi-Bancq2pyBgNf6GgnAwL97-H5WfkL5KchDVE-w84zCEXe-VK-rKjZZyuMhAQu1HUKY0OwZRI4hrcQyrHwGMNpr28VwNSnDQQmzgkBwFBrvCGhUaBanYyjK6Sd2HTQ_Hnn8pWJZiyFMrddFWZYvaNBz1pJO3-Z3atFbRyVQlnenyDNevn-tXTJvbvwuuMiWILK-2WGWf9MNE2GogOP_d3cr2PsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت مدیره شهرک صنعتی شمس آباد:
چند لحظه پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
اصلا حمله ای نشده مردم نگران نباشند
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20475" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20474">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گروه تروریستی حوثی‌های یمن اعلام کرده‌اند که یک حمله دقیق با استفاده از پهپاد علیه یک "هدف حساس" در فرودگاه نجران در عربستان سعودی انجام داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20474" target="_blank">📅 13:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20472">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d96f29aa.mp4?token=e4n_ePMlltfAslJpFBwsxzQAzAtuQNxvITfclQwwDDO5u2Rx4pQ5X4hPUWwMigvn5qLnlGeEqvJprXgwOcFmdtAu1I-nzxgIaqzBaWljcXxcZ9fRKHjVIpq_LZ2Zy3FRscyyn7moH9Q4DeKys0dfsAH5hRkBKk6DAwJgmT4c4ACUytWuwImwgqyEjweLkN5Q9d_CcT9tsVt9cqPk-gP_yQ4uymPi3KNWzd-LVAimsZs3aTi8rQC-0V2I0x8kzO80D0um6emhFPB3RMw9wh-0mznOrk2QFpK-GGwu1rJ0Tnn28oxIHgDsGos0G2K4Sb2UwyeWLAADWaB2Jt0JXMDbRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d96f29aa.mp4?token=e4n_ePMlltfAslJpFBwsxzQAzAtuQNxvITfclQwwDDO5u2Rx4pQ5X4hPUWwMigvn5qLnlGeEqvJprXgwOcFmdtAu1I-nzxgIaqzBaWljcXxcZ9fRKHjVIpq_LZ2Zy3FRscyyn7moH9Q4DeKys0dfsAH5hRkBKk6DAwJgmT4c4ACUytWuwImwgqyEjweLkN5Q9d_CcT9tsVt9cqPk-gP_yQ4uymPi3KNWzd-LVAimsZs3aTi8rQC-0V2I0x8kzO80D0um6emhFPB3RMw9wh-0mznOrk2QFpK-GGwu1rJ0Tnn28oxIHgDsGos0G2K4Sb2UwyeWLAADWaB2Jt0JXMDbRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشتی باری که امروز سپاه زد !
ایا این حملات جواب این حمله است ؟ یاشار : شک نکن!
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20472" target="_blank">📅 13:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20471">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpGLEtvdjg6aqO3Hz6bd1YZ2NzlQ31Yqx5os_InRgfbHIPwIJJ8dckV-ykk8HLDsSgO9wTODtJSeKjbB3_DNmQd9byIumTM4FUONOCn1dRhluimWqgE5Vel899MgX5HAdSiFYQDFxVccCS8NqcHeDy8sCfNVQeULaD1IlVr3Li99u94bhGrys1JwzQIt8NCfBV76QUkY4OVrHmzfIqbDtQ9yOD6w4jiXQQZYXA-upfBaA3l7fib4bRUxTnC1NoinCL3OMLB3MrNe3QVIn3K33Rt2lzh1XZI13My_S8j6HTTpuy9bHiLCX_77mmHkW0F1bfemAEqebQk40Q7xrHjbFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلاورجان اصفهان رو هم زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20471" target="_blank">📅 13:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20468">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/538f54d0f8.mp4?token=Bu-mFG2AnGRQCKNZ6dyT5l5ctbdIlIPGwQxd6yATqmoxVrKjDdmiKfMLKDSJKdS6jPVa3Ba7zslc_J5kt4LDZHHZdc2X-j_grv8iF5m4iV1oUHipY_z0zGUaah8OXFp9MiWUwZfZHIt_Wd6l_9pKM8ZE-IPBQ2vc53iPSFjkAmJ9i0lpydm98NlA5XH-sjOLABYP8h8LYRuO6920vurrMwAchAc32JP_ySI5WFLie1qZjHVubUpyiM9MFAs-aUu9-bQNq4xBbFIPtlm9t05Is8yNp77M1mZdXpFCh7xGX0Nt7NAPfQNVLwIAAlO0HqmuMSaZlWkDdBk87fEjq_e7WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/538f54d0f8.mp4?token=Bu-mFG2AnGRQCKNZ6dyT5l5ctbdIlIPGwQxd6yATqmoxVrKjDdmiKfMLKDSJKdS6jPVa3Ba7zslc_J5kt4LDZHHZdc2X-j_grv8iF5m4iV1oUHipY_z0zGUaah8OXFp9MiWUwZfZHIt_Wd6l_9pKM8ZE-IPBQ2vc53iPSFjkAmJ9i0lpydm98NlA5XH-sjOLABYP8h8LYRuO6920vurrMwAchAc32JP_ySI5WFLie1qZjHVubUpyiM9MFAs-aUu9-bQNq4xBbFIPtlm9t05Is8yNp77M1mZdXpFCh7xGX0Nt7NAPfQNVLwIAAlO0HqmuMSaZlWkDdBk87fEjq_e7WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون فرودگاه بین‌المللی رامون اسرائیل دیگه هیچ جایی نداره و از سوخترسان های آمریکایی در حد انفجار رسیده ، مذاکرات بسیار خوب پیشم میره
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20468" target="_blank">📅 13:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20467">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اصفهان صدای جنگنده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20467" target="_blank">📅 13:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20466">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dO9mwWl8JyC8LzoTIO4FCE8aExdE8RK-LVNfDMPGVCTCKJ47no_wbOAIg5X08yVV45y28DwyzW-xDufZlRSbWMqokrfs1-wUAHXrHHwU63QiCLZusszoX92O8HSMXTulunxO3ZdDzlQiWNJ7-QCYIDVhyUA3e5n2OLaAP8pfxTd642clgCz35qKuDEp-peAQ_Lu3cBQ0qc5Ud3y9SWHFQXHyj98czEM8z58ciF9VUgQ6aXELeDbzDb-pvfKeJiwy-L2UiOpRv3xNvrW0bAXmOxl-oa475DqQTtiRqAU3pJ4foJZA14yerDHE8_z8_Jfm7aREvtJTLG7u9_wsiOXt-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایی دیگر از دو انفجار
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20466" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20465">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c3af8280.mp4?token=AR05-w0NMOu4cQ8pWLpB4TNVyMi7N4gGdJtn3eLvtdTZlKpDA7V14nexd0oeDJ5vIHSwVLYbqJGwdhlX-iGnitEAF5U6bdxQEVdLC6SdwASW_recsxpOppXcP_3lvH4VJa13UKUp8oTPeGoyrmy998Bfy_C3yBb6uotft1h4KTCJ3ExcErQxtgNGwt79bKRMCi8Uu8ZL4iZdcpMdGmN76mKWyEBERzfwfXC9CfrZUMFWG0119lJzbUXUVEgY03Yt16FrBH3DN9wGAzrgcjLLZH98f-NlezL6Gt13BLJ0D433HUMduHCRvuiGQUu-MyOaBfuKxQvsxxu7L01a7cuTRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c3af8280.mp4?token=AR05-w0NMOu4cQ8pWLpB4TNVyMi7N4gGdJtn3eLvtdTZlKpDA7V14nexd0oeDJ5vIHSwVLYbqJGwdhlX-iGnitEAF5U6bdxQEVdLC6SdwASW_recsxpOppXcP_3lvH4VJa13UKUp8oTPeGoyrmy998Bfy_C3yBb6uotft1h4KTCJ3ExcErQxtgNGwt79bKRMCi8Uu8ZL4iZdcpMdGmN76mKWyEBERzfwfXC9CfrZUMFWG0119lJzbUXUVEgY03Yt16FrBH3DN9wGAzrgcjLLZH98f-NlezL6Gt13BLJ0D433HUMduHCRvuiGQUu-MyOaBfuKxQvsxxu7L01a7cuTRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش مردمی :
دوباره زدن
، صدای صوت موشک قشنگ شنیده میشد چند ثانیه قبل از انفجار و الان صدای جنگنده میاد
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20465" target="_blank">📅 13:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20464">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNEWZHoIzbC-NC7OVRoxrQIPHpbbv0OETXDbjXW1b4AOQF-JC4-h8juNIWtYnDgE8K-VwqzAP9GJjTCKjYasMOf64FWaFGCDsIWc9SYJw0JS-5_mPRCd49y_1NkRr8Rg_MBAw_I5nblPDy61BJlVysVpD53XSC36FaO8fEpB2vHVcgvpjMkQcmy3sVjLBE7959U8G8siHKWhLryv8OcYLgPaWx6Ny6CCByCLLLBCN2f8kmcF646oWj4iWQC-cTNQptfWo5bdHcP_MMY8x_ZOZxbZgKYJy6hDhUkhnXw7ZuSx-FyR5dc-m46M5B8jTP-jZIazWe_sa1LFxFi-3Iu6rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرک صنعتی شمس اباد فشافویه توی خیابون گلشن ترکید گزارش های مردمی تایید نشده : مورد ۱ :دو کارخانه منفجر شده مورد ۲ : کلانتری فشافویه رو زدن @WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20464" target="_blank">📅 13:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20463">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20463" target="_blank">📅 13:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20462">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20462" target="_blank">📅 13:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20461">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گزارش های بومی : زدن بدم زدن ! خودش نترکیده زدن ! ‌ کارخانه پهپاد سازی هم بوده ، ۲ تا کلانتری و کارخونه هم قبلا زده بودن همینجا (حسن آباد فشافویه) @WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20461" target="_blank">📅 13:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20460">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7200405da8.mp4?token=XmN8W_RUE_dLO28FqnOG0jgg4AyH4sxDwFSyU242AJrPJe5glGcl8Rs0VtsIZFO8LxasJF1CMiNlW8v8XT2uslG2ZINUC91Ta-Gv5j8FkDdTDQIUDu8GDhGtCy0odCrZyauIexh2zsN322NoU7KLJE6KDTcnLRJxPTdERzf-kILO4MS4mHpYLrgA0h2ckwO2KQFUyDLZznu-YGcW7h3YtNCVnqxu2aEzYWxi7H0kq8Wh1K1vFPV43SmnlZODfpmgzJBAoFluDdlK2SJRmiaBw6u-MkCQzKQ242jREMZA2-4Jn6yXKSk4gmW7qSESQRgJsBzvEUnUuZrcIGC9gpZ6oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7200405da8.mp4?token=XmN8W_RUE_dLO28FqnOG0jgg4AyH4sxDwFSyU242AJrPJe5glGcl8Rs0VtsIZFO8LxasJF1CMiNlW8v8XT2uslG2ZINUC91Ta-Gv5j8FkDdTDQIUDu8GDhGtCy0odCrZyauIexh2zsN322NoU7KLJE6KDTcnLRJxPTdERzf-kILO4MS4mHpYLrgA0h2ckwO2KQFUyDLZznu-YGcW7h3YtNCVnqxu2aEzYWxi7H0kq8Wh1K1vFPV43SmnlZODfpmgzJBAoFluDdlK2SJRmiaBw6u-MkCQzKQ242jREMZA2-4Jn6yXKSk4gmW7qSESQRgJsBzvEUnUuZrcIGC9gpZ6oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش های بومی : زدن بدم زدن ! خودش نترکیده زدن ! ‌ کارخانه پهپاد سازی هم بوده ، ۲ تا کلانتری و کارخونه هم قبلا زده بودن همینجا (حسن آباد فشافویه)
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20460" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20459">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M30M2gruKFVjljASCPUHHhbSI5JczuL00CSWRwLChvFqc0pQJzcBkygrcs8dJsyaUHQuUSxR7G66iEIq60Z74xB54AY_qpkKbESsW0NaaM8JUzKsWAsaj9Y-no-GluXzSHfCoCsFIjE_2-fasQG_3BFzg_pW9aL3mr7ea6wb1kV4nh2LREf8_KMkRnOF-ozdnKdjef7Zh33EZ0DMPSSAUMxOjiMeg-UM-kUqZOteSQk0HhAIvNgos2zQTo9-eyuMYnEzTLIbVrV0ho6QC_cB0Q3Pr0ssRCCkZBTMPXY7IusCxmoUHZO8CU-Q6vNGkf4opVFz4vHBz_vEptuvdPN3Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرک صنعتی شمس اباد فشافویه توی خیابون گلشن ترکید
گزارش های مردمی تایید نشده :
مورد ۱ :دو کارخانه منفجر شده
مورد ۲ : کلانتری فشافویه رو زدن
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20459" target="_blank">📅 13:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20458">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20458" target="_blank">📅 13:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20457">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رویترز: یک کشتی باری در نزدیکی تنگه هرمز مورد اصابت پرتابه‌هایی قرار گرفت و یکی از ملوانان مفقود و باقی کشتی تخلیه کردند
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20457" target="_blank">📅 12:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20456">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دور جدید مذاکرات بین لبنان و اسرائیل در رم آغاز شد.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20456" target="_blank">📅 12:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20455">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کانال ۱۴ اسرائیل: رویکرد سخت‌گیرانه احمد وحیدی(فرمانده کل سپاه) به سیاست رسمی جمهوری اسلامی  تبدیل شده  و سید مجتبی خامنه‌ای تصمیم‌گیری درباره پرونده آمریکا را به او واگذار کرده است.
مذاکره رسمی بین تهران و واشنگتن در جریان نیست و تماس‌ها فقط از طریق پیام و میانجی‌ها ادامه دارد
@WarRoom
اتاق جنگ با یاشار : دقیقا در پست ۴ ماه پیش اتاق جنگ «نشانه» 10May به این موضوع اشاره کردم</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20455" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20454">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">روزنامه روسی Izvestia : آمریکا می‌خواهد با سردر‌گم کردن تهران زمینه را برای یک حمله غافلگیرانه فراهم کند
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20454" target="_blank">📅 10:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20453">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYMQ9aJQVsdoylXrm2gDy8IbrJW39xIqg-WRK5pu6JGOB5S_hpfiohxqtPf1NQ-a-w6R_YLkNgF1sVJVrPPQ5uNzCvZh5mHNxAmk32XtYjCA8oAaX6Sqyf98vo_9w2yvlJK0i8bBV5l3vPY74kJ9u0hvFZlypMVWGTsJMfg6MsjBuhVDqQ9WQ5zE2MknRJq-9VP9ARGEEuvGjvswy7h_RmlV2ESxMVl7qPyhR74eZoIFs8ACoRF-b_GJKjchm-oogtPp3FS5mxr0zjXAhrovN1bqCROh5RvWbgd_R97zzo1HFe9DsMj5ZI_-M0eu-ZBqhfQjUWMmh7jonVxid0Chjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غزه قبل و بعد از ۷ اکتبر ۲۰۲۳
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20453" target="_blank">📅 10:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20452">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تلگرام از اپ‌استور اپل ناپدید شده است، اما تا این لحظه اپل یا تلگرام دلیل رسمی و حذف اعلام نکرده‌اند.      اپل قبلاً در سال ۲۰۱۸ هم تلگرام را موقتاً از App Store حذف کرده بود و دلیل اعلامی آن «محتوای نامناسب» بود؛ بعد از رفع مشکل، برنامه برگشت. @WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20452" target="_blank">📅 06:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20451">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">صدایی مهیب در پایتخت یمن، صنعا، شنیده شد، و هنوز علت آن مشخص نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20451" target="_blank">📅 06:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20450">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تلگرام از اپ‌استور اپل ناپدید شده است
، اما تا این لحظه
اپل یا تلگرام دلیل رسمی و حذف اعلام نکرده‌اند
.
اپل قبلاً در سال ۲۰۱۸ هم تلگرام را موقتاً از App Store حذف کرده بود و دلیل اعلامی آن «محتوای نامناسب» بود؛ بعد از رفع مشکل، برنامه برگشت.
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20450" target="_blank">📅 05:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20449">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRoqH_ksVtYYLd6ghRwCufTFhc2GP2KwIAAZ9NGFNryTEWkVCkFXCyZWJ8wvSJbI0tBgvokmfKlxp8Y3aD9yY7ZwCDAEV2rInxjd4SWlqlNzO_vYbxBmRldu-u_0yvYudpi6nBQd7Ib41A9xxMht765GzaMHMWizI9vd5A0JGLEWjB3jDvDAV26Kmq4tb4qujUZ9mSH68gU4-fnXrFf4Tjw6j-4JIV-zQpEC-_356O91swMvh5DWf--buGSYxo-biQYS99KqoY9bO-4vyAp630zRYP-Uqk3S1bDVxKCmOrhqfK32tBrncv0OCLQdK954p4b9dS7CpNG3l_6uB7JWJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مذاکرات دقیقه نودی به درخواست عربستان سعودی
@WarRoom
😁</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20449" target="_blank">📅 04:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20448">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRxElY-h7bU6PExm9Np8Q4RXDYS609FuHji_6IMqamk-NvDcaJcQmi7ZqNGbU07Na1RJWJo_aRdpFBztceajsY8KL2KQpUWMB00in_6sHW6UbMx-I--eQWUk9XshKgt5Xs5_hnq5cBhWsfYJgpiQpDgMg_RBSz3U7OsNNIXTuXTerpwyd2Tj9KpSKiffCTI2V4u3eX1QNZyz37NAShnXKcv8u2h1LRewcwXij3Ai66-ckPNCZkcR02jfh85yeVMAWowg6WP5Gbolca_zs2pGJt8ogV6gvLxIJcEtSQAyeuQGkD-0AqWLb0w-mNIQuddGWGfzwWa68YD7B68AU7zUAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریایی بریتانیا : گزارشی از حادثه‌ای در ۲۰ مایل دریایی شمال شرقی الخصب، عمان دریافت کرده است.
یک کشتی باری در VHF 16 اعلام کرد که مورد اصابت یک موشک/پهپاد قرار گرفته است.
مقامات در حال بررسی هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20448" target="_blank">📅 03:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20447">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ou04cnV0Unpggngm7Ze3T30ULTD6fw75x-lvvfQIBR_hZ-Iucnai9eA8LbU6EBvS7hL4C4EZ1uCAUGHfw3ubgPOu79kI8UBr8f5xmEoUQFc38H5-3_XeQmWBs35atIj2ThIm3L-aiWfNqHwfNs1ALZiuMC8nVi-42ewrOvdDUjsXU_x43KCp3xUCZr3sEq5yo8GRoOtLDuwFwEzBprOxz_j4DnNFJSPiIIl0AjN1C31WQ3BIckyfOFYpq6ZKGVVsCWiLnMbmnKF8D-d3RUcxxQSQTNYdAdqpSDNxS70xBaBuhuXiflHu4Rpgk3UDw_2NP_ONdt-G2DbmEkT2mQXf5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفت هواپیمای ترابری نظامی C-17 گلوبمستر هم اکنون در مسیر آمدن به منطقه هستند!!!
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20447" target="_blank">📅 03:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20446">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کانال ۱۴ :مسیرهای دیپلماتیک ایران عملاً از کار افتاده‌اند.
به گفته درور بالازاده، تحلیلگر کانال ۱۴، مجتبی خامنه‌ای،  رسماً اعتماد خود را از تیم‌های مذاکره‌کننده ایرانی و آمریکایی سلب کرده است. دکترین تندروانه و بدون امتیاز احمد وحیدی، فرمانده سپاه، اکنون سیاست رسمی آنها است.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20446" target="_blank">📅 03:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20445">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">لاکهید U2؛ شبح خاموش آسمان‌ها به پرواز در آمد
🚨
🚨
🚨
🚨
هواپیمایی افسانه‌ای که در ارتفاعی پرواز می‌کند که بیشتر جنگنده‌ها حتی به آن نزدیک هم نمی‌شوند. خلبان آن به‌دلیل پرواز در ارتفاع بسیار بالا، باید لباس مخصوص فشار بالا شبیه لباس فضانوردان بپوشد تا در صورت افت…</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20445" target="_blank">📅 02:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20444">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0r1DquduISUuac8KwagYogVLGqqKa11BgOYDDm9oNr9WJTnh56e6kFbMzQn_aKofVnpqkCn24pXSc6RQFMKFrUblUxzsmGO6IjpGvc_9rt4xY8ZX9ZWoOsITWsHG_rUeH_fVsP6Z7GU8j8Bxwg3CjdhsjOMXsZZ8aHjnZUT5CvKlhK0aLLNoMx_2_8atCIMsLbDhrt-IziLdsuKUYbTSJuqv8sgvPJ6aIk065u9zjdW6WGclrDwswWuHBiTaCCuIdseca5z8SW4yb6NEkzJkCFWM-YgfWdQyodO-eqJgmu0fib5HOd2GQC5lF-Tmt5rVk8ZmzAc3ULmGlkZunZY8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خبرگزاری های رژیم : شنیده شدن صدای انفجار در کویت و صدای آن از بصره عراق هم شنیده شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20443" target="_blank">📅 02:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20442">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گزارش پرتاب موشک از ایران
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20442" target="_blank">📅 02:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20441">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tI9TS3Ru-E82HLf260iUzdItaVB5WB6qOcXzCcIKeflBO3N_AfMt1r1XEbQ-ogXHqq-Rp6r1WwycHewLKxnK-GTUz6sC98Exes5MC2bKBrGG6eRqnAwBBa_BCnvez4HrxaVUclazYmkNtDQ0ql8LZhPnAxts53tuSx48HmbRMCfZFEKINmClr4-LdS2y5D62VZA8wUX3mPgvBOHxYsGajVtvHodeWvT34AQRON8z1t63_RXDiivAYhRegREvz3mvqRChrHJrxSR-e_Uyy2hXlyS6va-LqmbF_onD9FZ3TfVVp_mNoK3kQm_t2HpOuBxwLEloDZe3t4rL-r0egyTPug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت یه کاربر خارجی : اگه نقشه ایران رو برعکس کنید؛ چهره ترامپ رو میبینید!
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20441" target="_blank">📅 02:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20440">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پاکستان ادعای ترامپ درباره آغاز مذاکرات با جمهوری اسلامی را رد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20440" target="_blank">📅 01:52 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
