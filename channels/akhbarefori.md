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
<img src="https://cdn4.telesco.pe/file/jVsoh1bFgrvecqjwEdrPWzmID6ZMXtk-B6wJ07ZVGluEX97op3sPXLSYJMi4B-0rQQ-OmwR4c0xpbk0pQWB01n5x11hr5SJApwinok1u9t0drV-MmkF56BxkIyLgIKk7qBZrquGBpgdioFX5s8dV0tYJz-4Echm6OEG_BEglJiFKutnxc7vb4dzmwbZEeg9DQ9Zfw-MBoJtXcOlKJTVF_j6xfV_Yv8uh6lGzZCPvXR0JIRDPMBWR4yrgjHKIFubGXZiPxLGuyyKg7vsGJNl_zoL8tc3M8zXngS-qipWvm6XrpA5eKXsj1dPQWaMnTybSUQUrbdY8DKRmnKIbAdFUDw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.93M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 08:26:46</div>
<hr>

<div class="tg-post" id="msg-653574">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
حملات گسترده رژیم صهیونیستی به نوار غزه و کرانه باختری
🔹
ارتش رژیم صهیونیستی در ساعت گذشته حملات گسترده‌ای را علیه مکان‌های مختلف غزه انجام داد و به مناطق وسیعی از کرانه باختری یورش بُرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/akhbarefori/653574" target="_blank">📅 08:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653573">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdSMMBG00QWQ9us89ALOrNzYOTDZPFUlvBN-1iRz599RHS6jRgrg4SumhrW-anuG7LOjkssvCO0JiBTK5e-xONLrW0DJ5giiJLyB75_d4LMUF3oavGB8Mjn85wQRjnZ3lenChvDmsYtWcyjohrDDUx37W4uymNgn5q6O2UVihqlKoQH6KRmjFMALOhybC6d1HTZdXoj2QaXYibz0yYp_BAKcpcEfVAaB-m2Kx069AJ4cl-B29l2VQZ4u7IzQOC__r5XjwF3grcQZFtLUA1sMfDUQT5a6WlgBh4TqdY24tDU3ydnsmA11xTUXbN53LEpvJe8Tg-pTHAIx-_NzA_tVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع حادثه برای یک نفتکش نزدیک یمن
🔹
سازمان عملیات دریایی انگلیس امروز از دریافت گزارش‌هایی درباره حادثه امنیتی برای یک فروند نفتکش در آب‌های نزدیک جزیره «سقطری» خبر داد.
🔹
طبق اعلام سازمان عملیات دریایی انگلیس این حادثه در فاصله ۲۰۰ مایل دریایی غرب سقطری در یمن رخ داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/akhbarefori/653573" target="_blank">📅 08:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653572">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKBTeLuYcmlFstYJY9Zwp4uXFR8TDgWUJEVB2YlyyyMRVwaQI8ygc9TbCdCWGNlym_9AwiZQiUmjTWB9YR71MNDDBJybXNA4aGsj9RWb1JPUlMmL6wgONqv4UBK5thbYYo7IvSS3H3ZbbCdcn6LYOkVy3Jp-jNXlKacE7kHNG47SX3G0lW7q9XlnlaL5zyB9LfaZUep84C2LSKlrvr7SoPR8mpfXn6F5PJ18s7NuijlrBdkzoJ5WBk2kpGlGg_jGkOI1Sj950MDhe9HBGw_HyIyQoDrn-xZIuIMKYJGApZoc3RtCAsDwanp4ULXuR_HyJg94Z8V8AdblogSLYGFc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیاده‌خواهی آمریکا عامل سومین شکست متوالی کنفرانس بازنگری پیمان منع گسترش سلاح‌های هسته‌ای
🔹
کنفرانس بازنگری پیمان منع گسترش سلاح‌های هسته‌ای برای سومین بار پیاپی به دلیل کارشکنی‌های آمریکا و متحدانش نتوانست به سند نهایی دست یابد و در نتیجه، رئیس کنفرانس با اعلام عدم حصول اجماع، متنی را برای تصمیم‌گیری ارائه نکرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/akhbarefori/653572" target="_blank">📅 07:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653571">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادعای اکسیوس: برخی منابع نزدیک به مذاکرات همچنان بر این باورند که طی ۲۴ ساعت آینده فرصتی برای نوعی پیشرفت وجود دارد
🔹
دو مقام آمریکایی به اکسیوس گفتند که ترامپ روز جمعه صبح جلسه‌ای با تیم ارشد امنیت ملی خود درباره‌ی جنگ با ایران تشکیل داد./انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/akhbarefori/653571" target="_blank">📅 07:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653570">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
یک منبع ایرانی به الحدث: طرف ایرانی خواستار تضمین‌های روشن در مورد دارایی‌های مسدودشده و تحریم‌های نفتی است و این‌ها مسائل اساسی هستند
🔹
ما از تلاش دیپلماتیک کشورهای منطقه قدردانی می‌کنیم، اما توافق به ارادهٔ صادقانهٔ آمریکا نیاز دارد./انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/akhbarefori/653570" target="_blank">📅 07:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653569">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gayTU-rAp4doRNqdyl67cLk6yaQz6RPF4YnNiLPo_VWbA0FexrniQ7X0GOsHtGs9l9kmRVJP2l1GRtgTOyTPB0Qg_z3GZ9ZC4daYTRWo_Pp4ZH3XtQkHsUIosmLiQTGEoX_mlvz5frJnRrsA6pxKNscGS7vl9v6xrheYJX90yzE2HGLVYd92rN9b091JfKerqKlfT0p8RBRTKCGrBu4JYnNEVtK9EH26gD8eS3AvUgfyUI0f6AZkX_LmkgLWwvn42xCwEtrsWhmbPsIQsQFyXihXEomM3HqLln924u78pTHD6le08R6yimZt5hf4LbWQdJceVzd-hvqfdjNyqf9nCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۲ خرداد ماه
۶ ذی‌الحجه ‌۱۴۴۷
۲۳ می ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/akhbarefori/653569" target="_blank">📅 07:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653568">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8NexX61G3-M9e3Sd2OVdFQ6z7nDIX3Nz4LuyuwMg520CXyr0klviEYjXCFZ8sSU2YZ-24sgNX0Fmn29AvJyz_QWDfuvAZ_TDfl79ykhgC87BT9K7PWu1WbpKsc_G15t0aJ1XYE6EDAxCknMMGFUl_8qtSQnMkw74yEN8hqDe8D-3YgmnmOqHd2izylcn57CHIHuKRJQhi7aAvVK3oRWvx-DRyj6OMHMnBQeAQc3AEqps-ndL6c6yql2KRx5Ru-h00UTj5TfLIoOmPntvrgCSgyxIBY-9fuR4buirPvmie1rViDieArkcW64XYcsWcLQckAY2TdvhuFybbKF17_jUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توقف صادرات خودروی ژاپن به خاورمیانه در سایۀ بسته شدن تنگۀهرمز
🔹
طبق داده‌های دولتی ژاپن، صادرات خودروهای ژاپنی به خاورمیانه در ماه آوریل، به دلیل اختلال در مسیرهای کشتیرانی ناشی از جنگ علیه ایران تقریباً به صفر رسیده است.
🔹
براساس گزارش رویترز، این فروپاشی در تجارت، پیامد مستقیم جنگ آمریکا و رژیم‌صهیونیستی علیه ایران و متعاقب آن، مختل شدن کامل مسیرهای دریایی در تنگۀ حساس هرمز است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/akhbarefori/653568" target="_blank">📅 05:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653567">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXRt1Bc5l-T6iiSWjNos1ckQhUbllp8rzr8hRk0UxsfeE53LdsNE5AOEn_-9ofAqUHtvC6DVc9fDNtnoDzbXUdUZ7HKXL_voiJZhnlhDiQ12-_5gYxop_jTIkXIl41jcv1UhcW-_ueUCBqJtdqHZ8JB9FCrU6WonHxFmzu76k0B3i8TLdKt76jDEStQd2BXmo4dOhrkGQKXBBl2zNPbowceXaIYmKKPM9WM6bYgbJ8OXUTMYF7KheRJJdAYhbdWhDjTM5OponWRPP_qm_Kgwash138B18qa5-QL1TBeJwxiBa-A62XHU4ZQK_f62J1VvgQDEbEvGWGjB2YiLkDx1NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنفرانس بازنگری ان.پی.تی بدون نتیجه به کار خود پایان داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/akhbarefori/653567" target="_blank">📅 04:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653566">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
گفت‌وگوی وزرای خارجه ایران و عراق درمورد مذاکرات تهران - واشنگتن و ثبات منطقه
🔹
وزیر امور خارجه عراق خطاب به همتای ایرانی خود تاکید کرد: عراق چشم‌انتظار شنیدن خبر پایان جنگ و بازگشت ثبات به منطقه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/akhbarefori/653566" target="_blank">📅 03:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653565">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
نماینده ایران در سازمان ملل در نامه‌ای به دبیر کل و رئیس شورای امنیت، اتهامات آمریکا درباره حمله پهپادی به نیروگاه باراکه امارات را رد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/akhbarefori/653565" target="_blank">📅 03:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653564">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
محکومیت حمله اوکراین به خوابگاه دانشجویی در روسیه
🔹
پوتین، رئیس جمهور روسیه، حمله کی‌یف به خوابگاه دانشجویی در منطقه لوهانسک را محکوم کرد و به ارتش خود دستور داد تا گزینه‌هایی را برای تلافی علیه اوکراین آماده کنند.
🔹
به گفته او، در این حمله شش نفر کشته و ده‌ها جوان زخمی شدند و ۱۵ نفر دیگر نیز هنوز مفقود هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/akhbarefori/653564" target="_blank">📅 01:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653563">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49b200640b.mov?token=JjQdbxoIgSIeua8BYLgVDMR3CnachoUzct5tVJD0Gt-0BaW8GHN9RSgQlUyjHLsksA25rIf_tcD3oaNzVXoX49FGYpi44GlK4SkGTbWjSKvMXJ3f0cCSwZeDy9jwCAlpblHSwtip9iVjPcDi2JnCIbP3IZhcd4cvvZbPYbtQ1foF9H-ApxMvOhQV1hl4WRO-5rM2lFop04i_F_U6XRKUAcO5aTLa1h131EPuzo1w1zhlZBdKwLMjX829wJSWKyjw2RGdwYSCMEaFp734BRe95awK1bf3d_25hicTSeqllVM_mYvZduAqmSkVRcbSpurmT8UFL1Fdj4QrgWWZbvKA4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49b200640b.mov?token=JjQdbxoIgSIeua8BYLgVDMR3CnachoUzct5tVJD0Gt-0BaW8GHN9RSgQlUyjHLsksA25rIf_tcD3oaNzVXoX49FGYpi44GlK4SkGTbWjSKvMXJ3f0cCSwZeDy9jwCAlpblHSwtip9iVjPcDi2JnCIbP3IZhcd4cvvZbPYbtQ1foF9H-ApxMvOhQV1hl4WRO-5rM2lFop04i_F_U6XRKUAcO5aTLa1h131EPuzo1w1zhlZBdKwLMjX829wJSWKyjw2RGdwYSCMEaFp734BRe95awK1bf3d_25hicTSeqllVM_mYvZduAqmSkVRcbSpurmT8UFL1Fdj4QrgWWZbvKA4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار جالب امشب مردم در میدان تجریش خطاب به دشمن
🔹
رسیدی به هرمز، بزن رو ترمز
🔹
ما عاشق نبرد با یزیدیم اورانیوم به هیچکس نمیدیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/akhbarefori/653563" target="_blank">📅 01:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653562">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgdZqEf1dYfCMkAEpDZO3yyQtnBUbwgQIDQ2kAJbtK7SlYSOVurkULTiemkaplKkvR4X_EbTxjVcb0Qpsq3ImpBxSGADz0-TZ3D3ap_Ai3tJ5o4yPM4a2Z08gXCnkkxIYlZWuqeQf41PCYEuE5ZtwfBD4weLdNmjg4QJ3lBDeGOCxYicPCUVM7qyoz4uWa8D6u2YAiZm2tnm20VGNAc-Uww_OcZk4-O7dQgJ_XVAn5sxAjrVokyKAhHL0-Qv4q5gisTJ7-s7uciUwqBvx1X5iyUCKOfWWP--xp5xqiYfnvl9NN0345PlCGrsr8jApHi0FiZjsH3GXLKHsdMCwP4Fiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آملی‌لاریجانی: دشمن در صف‌آرایی مستقیم به زانو درآمده است
🔹
رئیس مجمع تشخیص مصلحت نظام: ایستادگی ملت شریف و نستوه ایران، دشمن را در صف‌آرایی مستقیم به زانو درآورده و او را به سنگر تحریم و محاصره کشانده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/akhbarefori/653562" target="_blank">📅 01:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653561">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
فریاد مردم در خیابان پیرامون مسئله هسته‌ای(۱):در مسئله هسته‌ای مذاکره‌ای نداریم!
🔹
امام شهید:مذاکره با آمریکا برای مسئله هسته‌ای بن بست محض است.(۱۴۰۴/۰۷/۰۱)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/653561" target="_blank">📅 00:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653560">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94cec408dd.mp4?token=Q9LlAGbJPIx5GIMF0QYwm0QfSPWmlsp3onCcM7kEvmO3UcgRvyBk4Ur_EnW_0HBlXGaWPcPLuoOSyuZslakSHZAbWLDOD14-L6VPIIgco35r0rE0ndaQ802sZso7dmK7KIJ6SjArz7kf5ETRA6yMSzk7u7SKTxWHAnMQVAjmPlNv_72buqKSZe9IOKn33JVYB8jMdqmzH7yQh5-R6j40HYHdByCWrxziKoP7CtIHtH_AOolqBI880-4teN4sb8keS1WBOhIDcHy-ERAC3AahljlLOdXRRNuPeXVLxLwbuWr8KUTDY4P5F08PGbpHyGb4PY8v_zfIR2mMGXTTLKN0BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94cec408dd.mp4?token=Q9LlAGbJPIx5GIMF0QYwm0QfSPWmlsp3onCcM7kEvmO3UcgRvyBk4Ur_EnW_0HBlXGaWPcPLuoOSyuZslakSHZAbWLDOD14-L6VPIIgco35r0rE0ndaQ802sZso7dmK7KIJ6SjArz7kf5ETRA6yMSzk7u7SKTxWHAnMQVAjmPlNv_72buqKSZe9IOKn33JVYB8jMdqmzH7yQh5-R6j40HYHdByCWrxziKoP7CtIHtH_AOolqBI880-4teN4sb8keS1WBOhIDcHy-ERAC3AahljlLOdXRRNuPeXVLxLwbuWr8KUTDY4P5F08PGbpHyGb4PY8v_zfIR2mMGXTTLKN0BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همکاری اعضای ناتو برای بازگشایی تنگه هرمز بلندپروازانه است
🔹
روبیو، وزیر خارجه آمریکا: «نه، این خیلی بلندپروازانه خواهد بود.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/akhbarefori/653560" target="_blank">📅 00:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653559">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af58dce728.mp4?token=pnA-n6gj7LkwpV__bH85JoWKVbdfbI0yKbxHz6nFyLvwl9-AEjDSfPR1HYH3OiR-DwuvAx2bE6mXHMRxruDdIUt6AgElRz_SPcgy-M5Scx8qQiCB3Z3aRYC8TQvg5xscXZigmZG_Jn1WO4E3E-9khnvgSqtADdkFhzSUNNj6rOGnof-HaYIzOTZHtoA7BeUu9tQFyaXDS1ERhyauYMKRu0qgcgaZsBheg_QSg7SrS_hPPMtgc16OOfkiHJpbbe8BvQ63RQesPufcf_vAW3w02gJC8tsopjvvIKtI1WXkJxaTMLxfApqmPa95XowWg6aQ44mhrwEh19Lx39SH5ees7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af58dce728.mp4?token=pnA-n6gj7LkwpV__bH85JoWKVbdfbI0yKbxHz6nFyLvwl9-AEjDSfPR1HYH3OiR-DwuvAx2bE6mXHMRxruDdIUt6AgElRz_SPcgy-M5Scx8qQiCB3Z3aRYC8TQvg5xscXZigmZG_Jn1WO4E3E-9khnvgSqtADdkFhzSUNNj6rOGnof-HaYIzOTZHtoA7BeUu9tQFyaXDS1ERhyauYMKRu0qgcgaZsBheg_QSg7SrS_hPPMtgc16OOfkiHJpbbe8BvQ63RQesPufcf_vAW3w02gJC8tsopjvvIKtI1WXkJxaTMLxfApqmPa95XowWg6aQ44mhrwEh19Lx39SH5ees7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: ما ایران را متوقف کرده‌ایم. آنها هرگز به سلاح هسته‌ای دست نخواهند یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/akhbarefori/653559" target="_blank">📅 00:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653558">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa4dbfae92.mp4?token=QyFFVQtGNrYKepWRHqMLtsv6ShAJ-Kr-oZrPHTWku6PLpbDO8cKPJDsyNlYbsfZBuil7WZOEK8axQjyGmATWd6lJNx8kC0ihffZhaPPw-WxotOA4rshVsBGP7l3sLaQNqffuF9wN7QPiSvW6BS2MfTp-hJmISOSGS0hR5cxUG9j0lQ6j3ImNPf5ty2jwV90LJD0ZwbLWOwYzdOu1AMXsOLPLJ4OyWRtQ9PdCbJm6VrzjVaByTVfPm5H0dad55FUZaTngnj2kH7D36oWtgejs36Eztp-VhenkbcsvtJxiTdBZw2IoI0KGgy_CNi5jv7fNSYng33TQFJDut_MpAcICGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa4dbfae92.mp4?token=QyFFVQtGNrYKepWRHqMLtsv6ShAJ-Kr-oZrPHTWku6PLpbDO8cKPJDsyNlYbsfZBuil7WZOEK8axQjyGmATWd6lJNx8kC0ihffZhaPPw-WxotOA4rshVsBGP7l3sLaQNqffuF9wN7QPiSvW6BS2MfTp-hJmISOSGS0hR5cxUG9j0lQ6j3ImNPf5ty2jwV90LJD0ZwbLWOwYzdOu1AMXsOLPLJ4OyWRtQ9PdCbJm6VrzjVaByTVfPm5H0dad55FUZaTngnj2kH7D36oWtgejs36Eztp-VhenkbcsvtJxiTdBZw2IoI0KGgy_CNi5jv7fNSYng33TQFJDut_MpAcICGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با وجود تهدید ایران به حمله اتمی توسط آمریکا، آیا چین و روسیه از تغییر دکترین هسته‌ای ایران حمایت خواهند کرد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653558" target="_blank">📅 00:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653557">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3956427383.mp4?token=soiqMQ_Gctz1R5OJkQx9TFdUqZbsm03ZMK3nH45A72G0ZSMCexux_bHvJfaQIN8eKp19dUeuywc2vJxKQAyKvTQfG7kAj5CRfbCtEyVDFZUFQaGCve9MQiX5JtPGNkKgJqX7edplaXQo0HsrkbaARxJVx5nneS9TfKrOMJs9AN9eObf_5Zl3goWq0zxwnyDdMpRBD_ylaoURLfXGgONRAeywbz-Ll0DXZ8h8EO3ff_sfTalmZhCRPFW9OeUT5V_sOwBuMNlV70DGkov7PymUBJI7Adato-H9wUARAPK_V28mNXXfRtyfeuDTGi1roAwJg607B09QwnpUDfz5GsHAew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3956427383.mp4?token=soiqMQ_Gctz1R5OJkQx9TFdUqZbsm03ZMK3nH45A72G0ZSMCexux_bHvJfaQIN8eKp19dUeuywc2vJxKQAyKvTQfG7kAj5CRfbCtEyVDFZUFQaGCve9MQiX5JtPGNkKgJqX7edplaXQo0HsrkbaARxJVx5nneS9TfKrOMJs9AN9eObf_5Zl3goWq0zxwnyDdMpRBD_ylaoURLfXGgONRAeywbz-Ll0DXZ8h8EO3ff_sfTalmZhCRPFW9OeUT5V_sOwBuMNlV70DGkov7PymUBJI7Adato-H9wUARAPK_V28mNXXfRtyfeuDTGi1roAwJg607B09QwnpUDfz5GsHAew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در بحبوحه «جنگ روایت‌ها» جواد آذری جهرمی خاطره شهید لاریجانی را دوباره زنده کرد؛ شهید تنها وزیر زن دولت را «جگردارترین عضو کابینه» می‌دانست. تأکیدی بر نقشی که زنان و خانواده‌ها در ایستادگی اجتماعی و به میدان آوردن مردان برای دفاع از کشور ایفا می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/653557" target="_blank">📅 23:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653556">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1Idi9sTWsf0yv8atgCUTQwMW6vBOYiNUACu5oQAgEqWMFq_clsrDrQ1m84am3mJWIKOc0B8OnWctXGVKwsay6rzTrHcqqfeW-d960qCoyBr7mtg3_SNux7jHrs48dJx23lAgsRVVZ3Cng1eNs8aoiJadwflkK9sVrDTx6k7QRFPFYpaHgKER15xoMEI58ZQYboz0h4Vy3jcWRIaXIfO0kY7P7GC9JTBSHrHlVOSuoJjsmyElxDkY5ep_mvjvEgMXPst3bpxAL1TW1-_TPHrEgHrJyN8Mia8uQTPGar5JBFSKcadZ0pGUbw6yHAft8ibAee2xAWZcZeY6U2IQ3_7Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفتگوی تلفنی وزیر امور خارجه با دبیر کل سازمان ملل متحد
🔹
در این گفتگوی تلفنی آخرین وضعیت منطقه‌ و روند تحولات مرتبط با دیپلماسی میان ایران و امریکا با میانجی گری پاکستان مورد گفتگو و تبادل نظر قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/akhbarefori/653556" target="_blank">📅 23:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653555">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
یک‌ منبع مطلع: گفتگوها بر سر موارد اختلافی همچنان ادامه دارد
🔹
یک منبع نزدیک به تیم مذاکره کننده
🔹
وی خاطرنشان کرد: میانجی پاکستانی همچنان در حال رد و بدل موضوعات است.
🔹
این منبع مطلع تاکید کرد: تمرکز در حال حاضر بر سر مساله «پایان جنگ» است و تا وقتی این موضوع نهایی نشود، هیچ مساله دیگری مذاکره نخواهد شد.
🔹
وی تاکید کرد: پیشرفتهایی نسبت به قبل در برخی موضوعات حاصل شده اما تا وقتی که درباره همه موضوعات مورد اختلاف جمع‌بندی نشود، توافقی رخ نخواهد داد.
🔹
این منبع مطلع تاکید کرد: متونی که برخی منابع غربی درباره جزییات تفاهم منتشر کرده‌اند دقیق نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/653555" target="_blank">📅 23:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653552">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLx3vt5ODfRRaH7XJ23l1YY5Arw7_1ZC4pl3pmDl0I7_xh0Kj30m428D9E0MdM6R64CLLTLpnNwVlhsPK3qMNCqityiaaRJGK6Kb7nnRaSb8eddkkHxNEKMmhIZ2icY-512FPn8wKi5IQRTsJmwnYNquMpF6xqy8ceU1Ad_qLQsx2EU8emB8wFy1edESMIhY9TqGEY37W9pFdOHrQHK6AEXkG75Nk_5v4AFCqw2_crDaW4NttrvN6OZLzLEXHVwdz3rvS6jmVfgzUTNYS8lXwXR4Mn3eSUhGI-oqwf8EXqesDZdwXJNU3J9q9mwr4Pp1kBJiAtXom7u-QMS8EoSUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LtzPkpI1etEhOjhYOA-MdYxnIOIwoFBKcoJ1AuL5t-By_KcxFLVd0HLet5YDyK1OmG42tAFY52kXRh6hbcGKvSepPVJA1YuKlBwrZXDAiIYlOEvyOTC_TRqRsCoz0bW2ZvXUTPUdVHp1UZ2sLCeDCxqi13CEN0GbgbjfmYxjjamiC-n77UMGS_7HTTENnBO4b59kH8ugQL1VvKWezfGYBimhq2XSvAV3gLHgoFRlMntDSaIIcHQ2zMYJ-YuwEZTcfCHqkbw8Aul-KeCK0nuQcEYvkIZCiF4Z_2MZss1DF9L7s85ASbhuAOE7qAthZdgaepugd4G4feq1TDLLMtGfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vsYBY74MZnYJMxeT8KKTn5-7pCtziILEnesJn1U7DMRJIH41HSiQtxSyyEyxuvqDEfbqGGnfgAnR1RJKMtReBTK0s-b73_0PxPpvi1XVqhguOBiq8xuoz11_0Td11k-hqG9bltgz5cHNtnoX-YGgxUgaJxngwQ71BCBrpsWK442xo71jV7COdTATxKlD7tS5MTSDHNb_yPBNx67VdfEzNELu8NEp4AgcFr_dNxqH5oI-zVmT6MTirxdAQm9XwhtzA-zveqNfxNFG4felTLeVQ61ooGPLg0M1-3Yo9J0X50sQmwNLXXNGHU3kZ4o1VZTtPcJWhnFT6i3Wox0O9RG4XQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کشف لاشه پهپاد متجاوز به حریم کشور در هرمزگان
🔹
لاشه پهپاد اوربیتر دشمن که توسط رزمندگان پدافند هوایی جنوب شرق کشور در شب‌های گذشته مورد اصابت قرار داده بودند، کشف شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/akhbarefori/653552" target="_blank">📅 23:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653551">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5280039e23.mp4?token=GOnEZ4BJ8YZpiAORAmgBGgnCHn9wop6vAYD55t8x0Y6XqIAY9AirSqe2cJFbPTC4S6YIh5IMeIBV4EaeM6y--AgycA4H0T4APaOut4ZlWIEcDzbz2Qm-_GHvFpmqEdedK3HbU7cwuJpQ6O8Egl9hYt9n0-IkoJ3x88JZQNXosx0QGN6ap7SHcKNEs1OFEL8i44Kx0MfA24webYCMwId308MvNCK2bZi5bjjs9MIu7xv_qNJo4odKFqoCGCKSDlvLUXsjZosGlfVnPcxSZVlPqCd9oLSF85ASoVPsOwalU9vtM1H4aVUHtqm8A8fXxDFo7IERysmI5KfWDB6P4rcQtoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5280039e23.mp4?token=GOnEZ4BJ8YZpiAORAmgBGgnCHn9wop6vAYD55t8x0Y6XqIAY9AirSqe2cJFbPTC4S6YIh5IMeIBV4EaeM6y--AgycA4H0T4APaOut4ZlWIEcDzbz2Qm-_GHvFpmqEdedK3HbU7cwuJpQ6O8Egl9hYt9n0-IkoJ3x88JZQNXosx0QGN6ap7SHcKNEs1OFEL8i44Kx0MfA24webYCMwId308MvNCK2bZi5bjjs9MIu7xv_qNJo4odKFqoCGCKSDlvLUXsjZosGlfVnPcxSZVlPqCd9oLSF85ASoVPsOwalU9vtM1H4aVUHtqm8A8fXxDFo7IERysmI5KfWDB6P4rcQtoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت صمت: بسته‌ی حمایتی ۷۰۰ هزار میلیارد تومانی برای ۱۲ هزار واحد تولیدی تصویب شده که پیگیر ارائه کامل آن هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/653551" target="_blank">📅 22:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653550">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1fkNilgiJjuZKaw2Hk7nMc6dyYiq8dSOJqHhzAuICBGr_b-KeS7UJh-MuketUYPkXtftIHv6XKz812ck0avQ_E7i8hYTL8dPi4xG45RBAsAf57qEjombg-HwUKdtY4f39tPK-6EP9MxGmfIOUQsls1G6UwSeqCtS5T1yafUUHlYCuT0B90NpEUEojTcb3TvNe9f_yWwh6cjVF8MZHU1urNC_h9H7Vn71F6Jt5PbMjIVwOLmuvKzUIjrRzHxa_kRCGNQg-u73fJ7L9nxDQuEM6uYKAHvZe7fAw2uN8i2QF0hZFg_xndqFpX2lgQV3rPc2R46yGCaj1MpoYCPv-NMUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک تحلیل عجیب؛ حمله به ایران در میانه جام جهانی؟/ گمانه‌زنی‌های هالیوودی، از حمله پهپادی به ورزشگاه ها تا گروگان گرفتن اعضای تیم ملی/ جام جهانی «خونین» می شود؟
🔹
گروهی معتقدند مساله جام جهانی آنقدر مهم است که بعید است ترامپ بخواهد آن را فدای جنگ با ایران کند و ترجیح می دهد، بدون مشکل آن را برگزار کند تا اینکه در میانه آن، حمله ای جدید را آغاز کند چرا که برگزاری بد جام جهانی هم اعتبار جهانی آمریکا را از بین خواهد برد و هم تصویری از عدم اقتدار و ضعف واشنگتن به دنیا ارسال خواهد کرد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3217004</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/653550" target="_blank">📅 22:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653549">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a8ac81235.mp4?token=owTNkLiZ_PqTFKxhCYy6HYq-DHIUnUSNhj-sDTluLdMHn_20sZVgOkbq2XBpjzceynL_Cf4qkO4_DuK-qXZml1Q-ANZbn3d-Xft61oqcDU8vej96YBSLmKHGEUa7yKD8HvLIpLmCe5eRBglew5rkgoD_sG5p8Le9D5SC7rXU5WOX6kXDG58StEiZVdYTSUCYG79mRcVf48VWhlPqeg5s9jRr8XO2rHwzsjCbBhktf_hEbwnENRtQZ8QqxmFDVlvxj9Sx1DDv5Ruj64H9zpaU6ox0veYWHnuKrgiYXYZ1ogvqLXAYEisZ1HIXTATzQCXh-MX44WrFVQcLR4NA8sGaSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a8ac81235.mp4?token=owTNkLiZ_PqTFKxhCYy6HYq-DHIUnUSNhj-sDTluLdMHn_20sZVgOkbq2XBpjzceynL_Cf4qkO4_DuK-qXZml1Q-ANZbn3d-Xft61oqcDU8vej96YBSLmKHGEUa7yKD8HvLIpLmCe5eRBglew5rkgoD_sG5p8Le9D5SC7rXU5WOX6kXDG58StEiZVdYTSUCYG79mRcVf48VWhlPqeg5s9jRr8XO2rHwzsjCbBhktf_hEbwnENRtQZ8QqxmFDVlvxj9Sx1DDv5Ruj64H9zpaU6ox0veYWHnuKrgiYXYZ1ogvqLXAYEisZ1HIXTATzQCXh-MX44WrFVQcLR4NA8sGaSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با "تیما"
توقف کسب و کارها ممنوع!
✅
تیما محصول جدید بانک ملت است که هدف آن تامین مالی یکپارچه زنجیره اقتصاد کشور برای رشد، توسعه و افزایش تاب آوری است.
بانک ملت، تجربه ای متمایز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/akhbarefori/653549" target="_blank">📅 22:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653548">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3l2WsB5ais_z_d9GpzMc2XOrG02uofeilz5OLDolQQEd4-O1OspOkd3wBtbULvGGAyd6z552fsAFbY4cq_K2u0mUlW2MHqV9fUHJaH-jH3cipt0ojxX3dz1DK49Jx43J3g2W2hdeeQlJtMjIOPrdJX8TLpirevOEXDhQ0bjimJTt7Nz7hsZNqD5EliNeQ2bRdp7CXLh82TAGTA4EWHTqVigKsIZEoJdYFmLUBfF7eSog-a2HL5coi-Fh61w_yyEsQc40adNyHDC5zQ0-EqoQjq1_RQy0lh7uJQSFg54Pp5XxMmwmHN2s9RMLr_JZOq2Eapd9f09oVAmVHzAHzBzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک تحلیل عجیب؛ حمله به ایران در میانه جام جهانی؟/ گمانه‌زنی‌های هالیوودی، از حمله پهپادی به ورزشگاه ها تا گروگان گرفتن اعضای تیم ملی/ جام جهانی «خونین» می شود؟
🔹
گروهی معتقدند مساله جام جهانی آنقدر مهم است که بعید است ترامپ بخواهد آن را فدای جنگ با ایران کند و ترجیح می دهد، بدون مشکل آن را برگزار کند تا اینکه در میانه آن، حمله ای جدید را آغاز کند چرا که برگزاری بد جام جهانی هم اعتبار جهانی آمریکا را از بین خواهد برد و هم تصویری از عدم اقتدار و ضعف واشنگتن به دنیا ارسال خواهد کرد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3217004</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/653548" target="_blank">📅 22:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653547">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eecdf190d7.mp4?token=I6oR4V162j6ayMitvRr1vQlVxPUTgUfdkrm1iGXzdD-MMAQRsDaeViBonVQTiu-lGPjb-SfI6Z1PaNi-o-D1CChYfw-EsSbxMC9F3rWNIt7XhblqLgNLxAey-T4ngAdghT65w5r28CDkdUqrut-r-TG1gg-SlHN3Uf4_DNZStHINktGddFV8AOxlZbH7dlx81VFISdf85bZbt_7Q72jXaC61n7rR9t506AuRfd9TuO2F0ZzUjTi8frbJEuCtAIHel3Tc_ZfBnQAewOiYaoP76opdINt8JMhzbyYRN1P_YixItste7ybH13XgfMW5vdKethiltjpudnud62DpIFItXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eecdf190d7.mp4?token=I6oR4V162j6ayMitvRr1vQlVxPUTgUfdkrm1iGXzdD-MMAQRsDaeViBonVQTiu-lGPjb-SfI6Z1PaNi-o-D1CChYfw-EsSbxMC9F3rWNIt7XhblqLgNLxAey-T4ngAdghT65w5r28CDkdUqrut-r-TG1gg-SlHN3Uf4_DNZStHINktGddFV8AOxlZbH7dlx81VFISdf85bZbt_7Q72jXaC61n7rR9t506AuRfd9TuO2F0ZzUjTi8frbJEuCtAIHel3Tc_ZfBnQAewOiYaoP76opdINt8JMhzbyYRN1P_YixItste7ybH13XgfMW5vdKethiltjpudnud62DpIFItXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توصیه مهم به افرادی که کارت اهدای عضو ندارند
دکتر امید قبادی، نائب رئیس انجمن اهدای عضو ایرانیان در گفتگو با
#الوفوری
:
🔹
حتی بدون کارت، تصمیم خود را امروز با خانواده در میان بگذارید.
🔹
آگاهی خانواده، در لحظات سخت نجات‌بخش بیماران نیازمند است.
🔹
به پویش «نبض ماندگار» بپیوندید:
عدد ۱۲۰ را به ۳۴۳۲ ارسال کنید
یا ثبت‌نام از طریق:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از دریافت کارت، تصویر آن را برای ما ارسال کنید
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/akhbarefori/653547" target="_blank">📅 22:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653546">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 54</div>
</div>
<a href="https://t.me/akhbarefori/653546" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه پنجاه‌وچهارم
رائفی‌پور:
🔹
0:06:00 رفتار آموزنده پیامبر با کودکان
🔹
0:13:15 مؤمنین با تذهیب نفس به کشف شهود عالم غیب می رسند
🔹
0:41:30 کلمات پوششی از فارسی به دیگر زبان‌ها منتقل شده است
🔹
1:15:45 منظور از سست بودن بیت عنکبوت در قرآن چیست؟
🔹
1:27:20 از سود دنیا بگذرید تا به سود بی حساب آخرت برسید
🔹
1:43:40 مؤمنین حقیقی در مقابله با مرگ
🔹
1:49:10 عکس‌العمل حضرت موسی در قبال رؤیت جلوه ای از خداوند
#دعای_ندبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/akhbarefori/653546" target="_blank">📅 22:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653545">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoNH1ASw4SOykYgBC9vssJsRKL3WEDSm4vnlgSdSh_2qacuYoAjDj0tHSV-nWrMS68PrE5244vD8wY1TB77jr-Azad9LZYY_AS4jf_KZ39ZDh48HqOirJ34vws1WXjGaN8C7aKDSfbtwSaucCI70wzn05GQ7ZwQx9KQuquaotpdu0GEd6A3Axv2lN0pREt_Hy2qqstuuLmqKtODsxTRMmkhwfnZNxG2d4su9AL56KsV48-hi4QvOth2jdYjmeYsIpzNJqhDb5lHnpvtMHzcn30cKxvpImaPkdKBoAOaczddFD3xcEJWJkzCUJcEpG5TXOGhduMRL2awsbGmbTZDQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فیگارو: در لبنان، ارتش اسرائیل در جنگی گرفتار شده که نه می‌تواند در آن پیروز شود و نه می‌تواند به آن پایان دهد
🔹
روزنامه فیگارو فرانسه نوشته است:
🔹
با ادامه درگیری‌ها در جنوب لبنان ارتش اسرائیل در نبردی فرسایشی با حزب‌الله گرفتار شده؛ جنگی که هزینه‌های امنیتی، نظامی و سیاسی آن هر روز بیشتر می‌شود، بدون آنکه چشم‌انداز روشنی برای پیروزی یا پایان آن وجود داشته باشد.
🔹
حملات پراکنده، تهدید دائمی مرزهای شمالی و ناتوانی در حذف کامل توان نظامی حزب‌الله، اسرائیل را در وضعیتی پیچیده قرار داده است. وضعیتی که برخی ناظران آن را یک باتلاق استراتژیک می‌دانند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/akhbarefori/653545" target="_blank">📅 22:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653544">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
آسوشیتدپرس: اسرائیل از تلاش‌های ترامپ برای امضای توافق با ایران خشمگین است
🔹
یک مقام که نخواست نامش فاش شود، گفت که دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه گذشته درباره وضعیت مذاکرات با ایران، یک تماس تلفنی «دراماتیک» داشته‌اند و اسرائیل از تلاش‌های ترامپ برای امضای توافق با ایران خشمگین است.
🔹
به گفته، کاخ سفید از اظهار نظر درباره محتوا یا لحن این تماس خودداری کرده است. ترامپ پس از این مکالمه به خبرنگاران گفت که نتانیاهو «هر کاری را که من از او بخواهم، انجام خواهد داد».
🔹
این اظهارات یکی از اولین نشانه‌های علنیِ وجود فاصله میان مواضع ترامپ و نتانیاهو از زمانی است که آنها تصمیم به جنگ با ایران گرفتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/akhbarefori/653544" target="_blank">📅 22:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653543">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای الشرق الاوسط: طرح امریکا برای انحلال «الحشد الشعبی» عراق
🔹
مقامات عراقی فاش کردند، آمریکا طرحی گام‌به‌گام را برای انحلال تدریجی سازمان «الحشد الشعبی» تدوین کرده است که با خلع سلاح سنگین این گروه آغاز می‌شود و با برکناری فرماندهان شبه‌نظامی ادامه می‌یابد و در نهایت به انتصاب افسران حرفه ای ارتش برای نظارت بر ساختار زیربنایی این سازمان ختم خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/akhbarefori/653543" target="_blank">📅 21:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653534">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFp3bYyDyGO-CThRXLQIp9IABBXl_5N8EEY1byU5z-_CEmnWUGgQER6V5tWZhogd_MWG_-bYeQIGJ76D7TJTMnpqBP98rEVAZCWQ8io5WC-MJc7xjANdq1Lgs-sMji4qF24HR7b_ITX0W1IkoLmLapK4pknfc8A5IvzDFwscdlKZ3XOwsDGmul1eHeZ1KP2ix3w0ps8tjl9_Eq5LDJtJQQFJOXokXR2v8BVeVXj3gmrpXidIrDqhyb5CwiLQeSwS-fgOtvJ0rZvKQZ5sO5-I7INBVFyKkWuloqxkEGjjqKJmhmFJgd4zGBKqdCavqpWzaXfq4CW5fURfXikHZbJckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/djjX5pqB7LQHVFL9in_K3-wQjoonBUA0aV5IpdZgbdRUAkF1lTTgdrf2DGEWCiTR75DeUXci9NwCoXdbEaGTIDWjxl-HBrUtZ9-42M7NBI-Umgsj0iWksFUHHEJVUinLV4PUeVihwfxyVImiSUo1PjNq6I5SA1gEhjsOMwcklSC02oABpg6ZuxvtX1o3rD6Fcu5yafQCj79BrTe8C_JikVwspgg3tEf3x8aOB6XW-yFGNY0MzvCuM8w9SZShHcCFHTtffpZbuX1HcQLLGvKmZv6ZrBBCyBaIyZ4BlCyzZSoyr-TDkhO6oKMfOuf2IKTBvgEnKIkqbBlhVdKYFZMoTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/feeu3e4hQ_fc4iUxugn1hedTJehd9HOU8RnRlF9yuiFx5vHnnwl0640zFsDUT3s9_5q8m7TpYaGPzM7UF5JFOdxzwGJDiqjimU7p4JxpyZGuqgvIewUC06ZjM1EvLDCvSfoO8JlljfGij7DY2PzVRFLsddss8_owYzSDoTE2CMOatRptjnkyZ9nbf8Is8FO-WFKWq0jBW0O_AcsWs8c0she6X2JW9fUUEMxwLLpOyVwZent5-1kHKIJ2pVgXBC0xgKprz3C1ZNcZZ1V1dtdJQAss8pV3OarefcFnsLmK8rPCs6wFDUYPqTL-7P-ht_epOxHdUyJFQG-7eFWionvJXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BU1piTHoEc4NHPsfvemgly1zy8VKW9Qxp5zANnofso8kvV-NSJ4QXG8dZvSWGIRfnIeA_svIuozkUsCYq59B3Uvw3PF3oAtAEJ-ATbR2ql67Tp7fH8d2iFJa5JklJ_I256rSec4AKpGYib6T8k9-SHw8MSpNdzeRKn6CCrbZWyQ9rt1cxa_jq9FLJs3PkWISVzrvfNb9esPMpY_r9JgkqzGjZKeQwr7AnnQ8QXFkuo63GqgcSRlct-B5U6nIdG8HBt0yr7ljK-qnC02u62bYwt5MPfT-hd9HWXantxARc1tDK5hB1JKcL-TdDeSpHlhG0nweXYFw6-No2or8-E04Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AbSu3V09fOYuWhNN8KT4COcAJjK97ttElyRJDxXNJ5H21JP9c5pTo7KVwxQ9EB_TatQCkgjP9Ls5hu04uBVQWsf4dGX28mOjeWe-CkV1J93fzweXPFVfFDSLRXr8UmvXU5LpXH66rMP0AnB8CUtVKrH8lMOiX68hkq6m15cSjFW5kko_0I30QwJJiwnRp7iFzU9WNPKxaBfNzD9FA37TlAnAXeofXjvVw15x70q9EDl1-Uib0PaXQlkXBdtAyDpcS-01f8eafyK1_P0edu3k55T0FpHWq95pP1eEYKm9Y_K3wlbg0xUvQjG-U2hd4v2TUSQ1A8khJDVLU3nZcyPPPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FP5AnC918X52dgPBrs0KLE29iQB6Lu8zedMpwE9ny5Ms9HR0kVMhQXbnRxPup03MVZhptbQ_65oPG0OEIAIIOpOeDyzJ98ZdV_5fhTvyS9sTcxX-oYUK3bKH8Rr4PijeBXxo8mRg-HsCuwa8hpzMYaLVODyLerx75LcFy5YpLz_oAc0p6fFzgxuajpQ38zey8GiO5vzF1OWGpF1pfxitaxMh46pODyh75GyWHodSJB36tN0eiAQtgz1ywjSEM620HCtKH3nuFN6WNHQoUMWa9ATi9Tx1GLzRk_y8hV24Nbj3fsdjMj083zawYAsJqyuSktdBAqiG_2dT68JdFDGwLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bdv2psFoLdCBEAdUxU0NrBQdfPFRbgG5OKNhCuBreP2r49EPl7T47l28pUcCGoOxkxWC8oCiQG2lC7xwo7oBSaCtPOSPu5vZsvy8gWbDnaPV6YDGUc29cXNW4Ba8K_JbGG9zybsZktev3VCXWVBo6KS6e_VnelWr5e5US18clSSli681vYdtjGyD_jXa3hcMMdIqoQ97FyM_0AHOMzS7L3AXdXsROCHfEN9gKz7t7BQau4SKwUTyOiE40ld8GJAKoQ5CLuvREwhByaBogAuBNPKZQYhbt5pSthobk2zv2orcyVOtOipcjjfMYuUqPSPqXc307ZSW85ZkNyMMmdgDgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HPZySejw-TrzJP9YW1sBlIcL8hd6fZkGSde0712LAzvm44CHo-dfJBOGnR3RB4xEUNymYMAVHGa52NL-5WUUipRs7uaPTaPMeKk63u5oXw-jTzCl7Z8c5YB1sXWesYZEo0PU6P5K3qPwl--P9P9ik_fs4mmxj4ewhL02Ilym_8TmtTddVd_uIpvhYvVYYHJMwkujPaGzx5vlKgVMAGGVEiHkt9jTm3fFYqMBRJnAKDxgmiolrzNYDuGTp9hw0zd6SQJeOosdvfeOvjCgoTQyhm1JS3sSvemGLp4JtL_Ljsv1zlAgbsgcJAr939agdFwJPHjJF76yf9VnOGdGOe40Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/or-cOsamEH7ZskAPwfaxzaEeUz4ZixdhiY2b0a7X77FBVdM-18Uho58FmOsJASe0G6vAF_EDiBvciDDVtZBUin0IE0-UBNaUiHBiD6A0j7gM3gheYCahPFczs6nKukD_QWLZG3qHXC9Kb-KwjaC5PkwaqutWzUQMsiW7S-UL4OLiTsTeu13lwnd3QPkmLCeCR7hdIQfxHxVrSR23ebDHb8tKdTvvSKJpVIvpDMWQ5V1N8eJPoQ0IVvMYOG0h3O-o0NjssNQmyIBCfpq5pdGqobqHvlsyxzxo2R72MvSKUvh4yWCfjfZo4s7I7fnJw3p8InvA-w5zSk7QWH25pVfXaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت قدم‌های خیر
💫
در مسیر
#همدلی
و حمایت از خانواده‌های ایرانی،
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با ذبح ۳ رأس گوسفند و توزیع گوشت قربانی میان خانواده‌های حائز صلاحیت، تلاش می‌کند سهمی هرچند کوچک در این مسیر خیر داشته باشد.
این خدمت، با حضور و اعتماد شما مردم ادامه پیدا کرده است
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/653534" target="_blank">📅 21:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653533">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
حادثه امنیتی در پایگاه نیروی هوایی آمریکا
🔹
یک حادثه امنیتی در پایگاه نیروی هوایی پنساکولا در ایالت فلوریدای آمریکا رخ داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/akhbarefori/653533" target="_blank">📅 21:24 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653532">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPgt_UY-PCIWl_41PE1OSf-fz4gIOg76_qw28UGCbjLeOL88ocvkyyCYjpy0ynhc6V2weIWIpqWgzXGpRrVe4KPFP-h0M53yC9E0GNLhsGnsz7LEfzLY84fXIymodDlR_vCuFv2S2kM1suqSQeC6FpGJiLn5oMvk-4hEc7uKCgkJFMp6Gj6-55J6zNGLnMLYRcRdkkGAJv7O5SfFnr3oQbWEWLOq3wv3H8Rl40Z2bkq3kuq82r17kYQM9QhmLggWk9m4kqJdwg6NAYk6k7NYr5v_-xq0N73A28RpcgNCkr9GVR3TuuryIFfwfurxDs0OuT_pHsQ3ebu45VCWgb9v2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه آمریکایی هیل: در صورت عدم توافق با ایران قیمت نفت احتمالاً هفته آینده جهش خواهد کرد
🔹
پاتریک دی‌هان، تحلیل‌گر بازار نفت در مؤسسه (GasBuddy) هشدار داد که در صورت عدم دسترسی به توافقی میان آمریکا و ایران برای بازگشایی تنگه هرمز، قیمت نفت در هفته آینده با جهش روبه‌رو خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/653532" target="_blank">📅 21:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653531">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd984e22eb.mp4?token=Smnvd1e7gH2O-nv7Kmws0j16PLev6QG5H6D2Bldy18qDC3ImRuqu70t1ql_aFnSF7yjql8ctqz4Y-l4B8V0-Va-2Q0f3QPfcdpx-3Y5fGvEaTO-faY0w47Zeh8vVCT0r8vR-sZQ61dnnwHKebv4dIdNilED6LF_YMkcGq9ewIshpFbuzoUTl9qblZ6gUUEuD1Utj3YDOTlO_XmrdHwInqb45knFhjxcQ8363Qubit6ts6jQ2p6qM1CnGeUo8Hn1XZYUra2qVv8sXbWqESccnRa1C4HvJLcMKyOQnuvGLzJ0sm1dFddW-FISF8zHMhujHaaHmi4oyFPPOfrxaQbWF9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd984e22eb.mp4?token=Smnvd1e7gH2O-nv7Kmws0j16PLev6QG5H6D2Bldy18qDC3ImRuqu70t1ql_aFnSF7yjql8ctqz4Y-l4B8V0-Va-2Q0f3QPfcdpx-3Y5fGvEaTO-faY0w47Zeh8vVCT0r8vR-sZQ61dnnwHKebv4dIdNilED6LF_YMkcGq9ewIshpFbuzoUTl9qblZ6gUUEuD1Utj3YDOTlO_XmrdHwInqb45knFhjxcQ8363Qubit6ts6jQ2p6qM1CnGeUo8Hn1XZYUra2qVv8sXbWqESccnRa1C4HvJLcMKyOQnuvGLzJ0sm1dFddW-FISF8zHMhujHaaHmi4oyFPPOfrxaQbWF9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در فرایند رضایت‌گیری برای اهدای عضو، کدام عضو خانواده دیرتر رضایت می‌دهد؟
دکتر امید قبادی، نائب‌رئیس انجمن اهدای عضو ایرانیان در گفتگو با
#الوفوری
:
🔹
وابستگی عاطفی میان اعضای خانواده، تصمیم‌گیری برای اهدای عضو را دشوار می‌کند.
🔹
در این ویدئو ببینید سخت‌ترین رضایت‌گیری در اهدای عضو مربوط به کدام عضو خانواده است.
🔹
به پویش «نبض ماندگار» بپیوندید:
عدد ۱۲۰ را به ۳۴۳۲ ارسال کنید
یا ثبت‌نام از طریق:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از دریافت کارت، تصویر آن را برای ما ارسال کنید
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/653531" target="_blank">📅 20:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653530">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7deada65a.mp4?token=VowMLFNAjVxhBWmY66-1lRZzP4O7Cj171FHQpiqtB3IKg-xncJqyN_pHAaN3_P0-B4cNiCop4vkb-14ZpA20gOoh3E9gmP59LOnOrHvDmddZmxwFqhG931XFbHSc_juTOLzJQP_s8ASVgs4WdrMfhNbZAIVQUWS0gwuwd9-Gf51QmfEyMSoO0MnLg8dRgPaxKBYNKMpHs55tk8B4Wln7gSE5-M6iJNCny2TDZcpXYg2ujybQA7kcC6rrhXU3P16hlhqvAd00PJRdd_ZmKMWQKntpq58yaah-qelLRjLn5rvxgxhpV09toBdymsqF1yAg1Yt8fpufTuS8IJGPBBdzjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7deada65a.mp4?token=VowMLFNAjVxhBWmY66-1lRZzP4O7Cj171FHQpiqtB3IKg-xncJqyN_pHAaN3_P0-B4cNiCop4vkb-14ZpA20gOoh3E9gmP59LOnOrHvDmddZmxwFqhG931XFbHSc_juTOLzJQP_s8ASVgs4WdrMfhNbZAIVQUWS0gwuwd9-Gf51QmfEyMSoO0MnLg8dRgPaxKBYNKMpHs55tk8B4Wln7gSE5-M6iJNCny2TDZcpXYg2ujybQA7kcC6rrhXU3P16hlhqvAd00PJRdd_ZmKMWQKntpq58yaah-qelLRjLn5rvxgxhpV09toBdymsqF1yAg1Yt8fpufTuS8IJGPBBdzjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران؛ پیشرو در اهدای عضو
دکتر امید قبادی، نائب‌رئیس انجمن اهدای عضو ایرانیان در گفتگو با
#الوفوری
:
🔹
ایران رتبه نخست اهدای عضو در آسیا و رتبه اول پیوند کبد در جهان را دارد.
🔹
سالانه حدود ۷۰۰ پیوند کبد در کشور انجام می‌شود.
🔹
ایران از معدود کشورهایی است که پیوند اعضا از بیماران مرگ مغزی در آن کاملاً رایگان انجام می‌شود.
🔹
مردم ایران در فرهنگ اهدای عضو، پیشرو و نوع‌دوست هستند.
🔹
به پویش «نبض ماندگار» بپیوندید:
عدد ۱۲۰ را به ۳۴۳۲ ارسال کنید
یا ثبت‌نام از طریق:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از دریافت کارت، تصویر آن را برای ما ارسال کنید
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/653530" target="_blank">📅 19:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653529">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef6033519.mp4?token=MxoJY6aRQmo-LKBbhg0g1y0Mz9t0HoL2UHmfG7dZ1GWYmOD42jzmnrlbtNh8NDifEq1P81iDpbmsxdg05vuXu1z3V-y6JqVWhxZutzdVP1ZpxN3pkRo_UVZy0PmyftZHaIK5pwaF4iX1MqWbdLiod87q2JOdF8Ldf-qrFmVh2cBznYvuwcqChXFIqV44h5yB2lRWGBaoezo3_PFFqOJv-hCfGmYfnuZlk7nFTWn1szqZauRgDwQYZGm66_NAPnkjvhEuZY0VWTobYbZI_nk7NIvSISg9wNZWfsizPmcUskUnxFtU3ilkY7IqUF_R-09APgCkLqdUodgmoTUeTDkVAQzek9nh_VigkhabfdvbqH1zlT_Jzs5Pf1O2bnSvjmUj5hmrhzygCPsKnjMa0Mzlb7JYRn4fDM8nanRK5wtGrn649jwXFFcXHptO7QaaqMFXxwur97KcERcGIZ0XPpMXHBuRWNYwQidHerq3Q2lKvQfhMvz85ND0fOKjod85eELYqHgkjaVoyzDaNFEt1jWW57QQQ-weB_ylGQKPxQikSoDiN6sZ7Sonr4WRVB4YQ39vkKnjEub2pmW48x_Lki1hVURo3By18dtcCTqitJAaRcolz6V_xGp7X8A3pItxTzOH-mYSIRVEOtc5CAk5VBkuhqOs19YJwCcq9zb49KFFxr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef6033519.mp4?token=MxoJY6aRQmo-LKBbhg0g1y0Mz9t0HoL2UHmfG7dZ1GWYmOD42jzmnrlbtNh8NDifEq1P81iDpbmsxdg05vuXu1z3V-y6JqVWhxZutzdVP1ZpxN3pkRo_UVZy0PmyftZHaIK5pwaF4iX1MqWbdLiod87q2JOdF8Ldf-qrFmVh2cBznYvuwcqChXFIqV44h5yB2lRWGBaoezo3_PFFqOJv-hCfGmYfnuZlk7nFTWn1szqZauRgDwQYZGm66_NAPnkjvhEuZY0VWTobYbZI_nk7NIvSISg9wNZWfsizPmcUskUnxFtU3ilkY7IqUF_R-09APgCkLqdUodgmoTUeTDkVAQzek9nh_VigkhabfdvbqH1zlT_Jzs5Pf1O2bnSvjmUj5hmrhzygCPsKnjMa0Mzlb7JYRn4fDM8nanRK5wtGrn649jwXFFcXHptO7QaaqMFXxwur97KcERcGIZ0XPpMXHBuRWNYwQidHerq3Q2lKvQfhMvz85ND0fOKjod85eELYqHgkjaVoyzDaNFEt1jWW57QQQ-weB_ylGQKPxQikSoDiN6sZ7Sonr4WRVB4YQ39vkKnjEub2pmW48x_Lki1hVURo3By18dtcCTqitJAaRcolz6V_xGp7X8A3pItxTzOH-mYSIRVEOtc5CAk5VBkuhqOs19YJwCcq9zb49KFFxr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس مسائل بین‌الملل: کشور عربستان به دلیل جنگ اخیر با کسری بودجه شدید مواجه شده است/ بخشی از قراردادهای مشاوره ساخت‌وساز توسعه در عربستان به خاطر جنگ متوقف شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/akhbarefori/653529" target="_blank">📅 19:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653528">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjDFHHK7c5i9NV5BmIk3QsL8NKgCkOxQcSC2-36uKjMcfvqjZA5seyPgouHaPtyi1rtUStuQ0gMZWi6twv4ypOXQuSzKpmDVIreQkhIvjxjPLtX04dEDEhjQmloXBLUonW3cLuhQE_9HwDktyCfPraHE3VS8qs_HDIVfYVZsrEerdhnAZrj4HBezze4EdXuDgVGZoCt3q-G0Z9pF76CngU0x4GxlC4wdr6TaljcjzCdsNeE75Yh6gPUlmD4YkJG-QIrcyg_HvsYfTdih0pLqg7ZXkp-Z-zXWWABK3Da_ZOxDqUiWT_Z8PuLCVwsIqEh1fQzGuEseQHJKEE6chGzGxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: شوک اقتصادیِ جنگ ایران، جهان را در «چهار موج» تحت تأثیر قرار خواهد داد
🔹
تأثیر این جنگ فقط به افزایش قیمت انرژی محدود نمی‌شود؛ بلکه به بخش‌های مختلف سرایت می‌کند و سال‌ها ادامه خواهد داشت.
🔹
موج اول همان چیزی است که همگان در حال حاضر می‌بینند: قیمت نفت خام بالا می‌رود، به دنبال آن قیمت گاز طبیعی مایع افزایش می‌یابد، هزینه‌های حمل‌ونقل بیشتر می‌شوند و رسانه‌ها از تورم انرژی خبر می‌دهند.
🔹
موج دوم، آسیب به خودِ نظام تجارت جهانی‌ست. تغییراتی که در زمان بحران به‌تدریج انباشته می‌شوند و بعد از پایان بحران هم حاضر نیستند به وضعیت قبلی بازگردند.
🔹
موج سوم، تأثیر پیچیده‌ اقتصادی بر کشورهای جنوب جهانی‌ست. این شوک‌ها از طریق کاهش واردات، سقوط ارزش پول ملی، سهمیه‌بندی کود شیمیایی و افزایش قیمت مواد خوراکی رخ می‌دهند.
🔹
موج چهارم، سیاسی‌ست. شوک‌های زنجیره‌ تأمین قراردادهای اجتماعی را هم فرسوده می‌کنند. کشورهایی هستند که همین حالا هم با ذخایر تحلیل‌رفته، فضای مالی محدود و مردمی مواجه‌اند که از زمان همه‌گیری کرونا شوک پشت شوک را تحمل کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/akhbarefori/653528" target="_blank">📅 19:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653527">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ملت‌ها صاحبان کشورهای خودند
🔹
رهبر شهید انقلاب: خلیج فارس، دریای عمان، اقیانوس هند، بقیه‌ی بخش‌های دنیا، تنگه‌های حساس دنیا، مال آمریکا نیست؛ این‌ها مال صاحبانش است.
🔹
این قرن، باید قرن بازگشت ملت‌ها به هویت خود، به انسانیت خود و شکستن طلسم سلطه‌گری و سلطه‌پذیری باشد.
🔹
به یاد شهید ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/653527" target="_blank">📅 18:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653526">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed2051f42c.mp4?token=Yt3ynA3AhSXbYSQ7VbaW1LhSMgjOltBPpXsM2iputVUW6lr-sWzNgoRHDYRQvifudFrndeDlBe0bOkRdqFnEdfuGgREhMINRm6IS1pO7znL3NrHT0R4lqEjN1sHY_7jrnhWeN2UHViAOwolLHkyPncLAuy7L7ssvthddHhgB0MbwHHYdeRhKbPMbcUdvWae-e11be-mGm1JOcaok5rpVW2tvbske6XnT2LrB-UgYHx2wOgh9wjDQKE3nsLkCRhkJ8e9qLWcKDKHEK5PuQGcKfz8FcZOO9gjqor7gJzq5uGW_h9gW013zUZdLUf39iLqklEs61DOnYtVED720YrYxlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed2051f42c.mp4?token=Yt3ynA3AhSXbYSQ7VbaW1LhSMgjOltBPpXsM2iputVUW6lr-sWzNgoRHDYRQvifudFrndeDlBe0bOkRdqFnEdfuGgREhMINRm6IS1pO7znL3NrHT0R4lqEjN1sHY_7jrnhWeN2UHViAOwolLHkyPncLAuy7L7ssvthddHhgB0MbwHHYdeRhKbPMbcUdvWae-e11be-mGm1JOcaok5rpVW2tvbske6XnT2LrB-UgYHx2wOgh9wjDQKE3nsLkCRhkJ8e9qLWcKDKHEK5PuQGcKfz8FcZOO9gjqor7gJzq5uGW_h9gW013zUZdLUf39iLqklEs61DOnYtVED720YrYxlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاخ سفید ویدیویی با عنوان «چهار شی ناشناس پرنده بر فراز آب‌های ایران» منتشر کرد
🔹
کاخ سفید اعلام کرد این تصاویر توسط حسگر مادون قرمز یک پلتفرم نظامی آمریکا در محدوده سنتکام، در چهارم شهریور ۱۴۰۱ ثبت شده‌
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/akhbarefori/653526" target="_blank">📅 18:44 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653525">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
سپاه: تیم دیپلماسی نیازمند پشتیبانی در تجمعات شبانه تا پیروزی نهایی است
🔹
روابط عمومی سپاه: مذاکره صحنه دیگری از کارزار میدان نبرد است که نیازمند استمرار حضور پرشور در خیابان و پشتیبانی از افسران عرصه دیپلماسی تا کسب پیروزی نهایی است.
🔹
امروز، به برکت مجاهدت پرشور ملت لبیک ‌و به فرمان مقام عظمای ولایت، قدرت نرم انقلاب چنان در تار و پود جامعه رسوخ کرده که هیچ تهدید نظامی یا روانی دشمن توان مقابله با آن را ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/akhbarefori/653525" target="_blank">📅 18:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653524">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0215cfaed2.mp4?token=DaSUsXaeWc8XDLq50kR-XeFn7ERMXeuU1n2bYyYM3Bu9idoBaIEjoH25CzuI2PkzBglQXZf8iktDcpby8LSi8IyGLSuimTjFbK9caVi2TyuqRabgz5OboLSy5GEBWfjWKIiCnxAhp_p2DqYItSUdXmh_iPJnxNVP_0da5kyPOzXtVyuELnWmU0xwARhmf3qzyy8XjJPRFkkoiG9PrCDH5oVuqytPnYnCsO4s21vBdZ0FHF8Wle-Di3BlEjpBkBsaa9LXDStuT2hUDB6-6q7LOAmITubbF6CpFJ_-xQdxVGYw_cCcKsY1qaJLI9yD73YCKTZL5RL-u6Mfzh_jBbMf7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0215cfaed2.mp4?token=DaSUsXaeWc8XDLq50kR-XeFn7ERMXeuU1n2bYyYM3Bu9idoBaIEjoH25CzuI2PkzBglQXZf8iktDcpby8LSi8IyGLSuimTjFbK9caVi2TyuqRabgz5OboLSy5GEBWfjWKIiCnxAhp_p2DqYItSUdXmh_iPJnxNVP_0da5kyPOzXtVyuELnWmU0xwARhmf3qzyy8XjJPRFkkoiG9PrCDH5oVuqytPnYnCsO4s21vBdZ0FHF8Wle-Di3BlEjpBkBsaa9LXDStuT2hUDB6-6q7LOAmITubbF6CpFJ_-xQdxVGYw_cCcKsY1qaJLI9yD73YCKTZL5RL-u6Mfzh_jBbMf7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا کارت اهدای عضو مهم است؟
دکتر امید قبادی، نائب‌رئیس انجمن اهدای عضو ایرانیان در گفتگو با
#الوفوری
:
🔹
۹۸ درصد خانواده افرادی که کارت اهدای عضو دارند، به اهدای عضو رضایت می‌دهند؛ این عدد بدون کارت، ۴۸ درصد است.
🔹
دلیل اصلی، اطلاع نداشتن خانواده از تصمیم فرد درباره اهدای عضو است.
🔹
کارت اهدای عضو، ثبت رسمی تصمیم انسان‌دوستانه فرد پیش از مرگ است.
🔹
برای پیوستن به پویش «نبض ماندگار»:
عدد ۱۲۰ را به ۳۴۳۲ ارسال کنید
یا از طریق لینک زیر ثبت‌نام کنید:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از دریافت کارت، تصویر آن را برای ما ارسال کنید
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/akhbarefori/653524" target="_blank">📅 18:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653522">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87dedaa288.mp4?token=CuuXRiC5XlQL_hrceO1y2ISH-jt7uWKrW6NorhqQAIPKxy9Wb5VnuVAQjGVDPeihcZHDgw3YWMtcwK9ePpnrDIy3sULmF6p6Z_-wFD0qNLxqc3tGLYZIgvm6Nf8RT9AgdKI6Qg26oUd8kVi9IGZM9QDx_O71jPfy6_1_IQereYBbDyR3Z4QtxVfIavblkBKqUVw1oMbtfe5N87IEJwoS54GsPrKRmBTsfHUqR67uLJkyZdTqqf-rhuncQjP0H98RIA-00xkfTYZgEtxEafiIQnzuFnkTh8n0PELFM3myqKR7_SXaKx4WROQAhGkrnMyd8eEaeF-p4jgViSooMgRTdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87dedaa288.mp4?token=CuuXRiC5XlQL_hrceO1y2ISH-jt7uWKrW6NorhqQAIPKxy9Wb5VnuVAQjGVDPeihcZHDgw3YWMtcwK9ePpnrDIy3sULmF6p6Z_-wFD0qNLxqc3tGLYZIgvm6Nf8RT9AgdKI6Qg26oUd8kVi9IGZM9QDx_O71jPfy6_1_IQereYBbDyR3Z4QtxVfIavblkBKqUVw1oMbtfe5N87IEJwoS54GsPrKRmBTsfHUqR67uLJkyZdTqqf-rhuncQjP0H98RIA-00xkfTYZgEtxEafiIQnzuFnkTh8n0PELFM3myqKR7_SXaKx4WROQAhGkrnMyd8eEaeF-p4jgViSooMgRTdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینترنت پرو بخشی از مشکلات صنف موبایل را کاهش داد
🔹
فرشید شمشیری عضو هیات رییسه کمیسیون تخصصی تلفن همراه و لوازم جانبی اتاق اصناف ایران، می‌گوید اینترنت پرو توانسته بخشی از مشکلات صنف موبایل را کاهش دهد و روند خدمات را تسهیل کند، اما چالش‌ها همچنان ادامه دارد.
🔹
او با اشاره به نقش اتاق اصناف در حمایت از کسب‌وکارها، مصرف‌کنندگان و هماهنگی با حاکمیت تأکید می‌کند محدودیت‌های اینترنتی، فعالیت شرکت‌های گارانتی، تعمیرگاه‌های موبایل و حتی واحدهای کوچک خدماتی را تحت تأثیر قرار داده است.
🔹
به گفته شمشیری، اختلال در ارائه خدمات باعث افزایش نارضایتی مشتریان و ثبت شکایت در نهادهای نظارتی، اتحادیه‌ها و سازمان حمایت شده و صنف موبایل برای پاسخگویی به نیاز مصرف‌کنندگان با فشار جدی مواجه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/akhbarefori/653522" target="_blank">📅 17:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653521">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf2997b98.mp4?token=NgDXvL4WYCPmU_ePzkztN-higJJ2xjjSAzrUnN_m_CHojnlRvt4npH76UyrESlCXbtgIMNWiey9ZFJDyfRrlGYbk3tf80AUMzztRwkxpmTLFkXVWnMz-16tKS_M-2KQ0k4Aq_ddqKlc_mQm-UBnuibRCfVr3Tfif3s9Fn1p8nRv-ylaYuMdOsiKuYnLXauE-03urNncgLaLzaan0ks4fsWGyUiOa6nkug1R216Ja4oXrogAtgRIwwHWJDDcpAMu1S0rfDa9AZfg6bTNQj0V1I_v89zMY_pSZTtxQwujY8VdtNwaIK8WGRboWMt7IBCkE09_459j4IOlkJ_LYXHR9HKJVxkWcJtWLyHrxp-5XQJbM3lNVBiM-YFCNetCHeqbUjyxtKPUtsW81aUwTHHr-t9Na33LTsgbdx4-xnJZ0E9ys7c1xlq4M8kirfwvrGV-XSAr1XynWhk6IcRE8CNKer1jwyDgM89jjayIjMZiI4qOCm4zEJ7RmsNV88FB80OyqsECM56QlxCG_Q_a6AvMMMqin2Fbsxl1YMZ0ZUNbJ4WZM80DQopADjGw1GFjX5fEFnSP7vED3eXQNQ8mRruEGKKu1W6EPsOAK9PrH2hgMKClkLn6IpkbZEs5q86pbqFwPjit-EMUyObfFilEO_AJj5082CtFZzVO3VrmHAzBas2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf2997b98.mp4?token=NgDXvL4WYCPmU_ePzkztN-higJJ2xjjSAzrUnN_m_CHojnlRvt4npH76UyrESlCXbtgIMNWiey9ZFJDyfRrlGYbk3tf80AUMzztRwkxpmTLFkXVWnMz-16tKS_M-2KQ0k4Aq_ddqKlc_mQm-UBnuibRCfVr3Tfif3s9Fn1p8nRv-ylaYuMdOsiKuYnLXauE-03urNncgLaLzaan0ks4fsWGyUiOa6nkug1R216Ja4oXrogAtgRIwwHWJDDcpAMu1S0rfDa9AZfg6bTNQj0V1I_v89zMY_pSZTtxQwujY8VdtNwaIK8WGRboWMt7IBCkE09_459j4IOlkJ_LYXHR9HKJVxkWcJtWLyHrxp-5XQJbM3lNVBiM-YFCNetCHeqbUjyxtKPUtsW81aUwTHHr-t9Na33LTsgbdx4-xnJZ0E9ys7c1xlq4M8kirfwvrGV-XSAr1XynWhk6IcRE8CNKer1jwyDgM89jjayIjMZiI4qOCm4zEJ7RmsNV88FB80OyqsECM56QlxCG_Q_a6AvMMMqin2Fbsxl1YMZ0ZUNbJ4WZM80DQopADjGw1GFjX5fEFnSP7vED3eXQNQ8mRruEGKKu1W6EPsOAK9PrH2hgMKClkLn6IpkbZEs5q86pbqFwPjit-EMUyObfFilEO_AJj5082CtFZzVO3VrmHAzBas2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم لگویی از روزهای جنگی تهران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/akhbarefori/653521" target="_blank">📅 17:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653519">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSo0NX7qBlvdztpLMhE0FH1eZaMdJMHSpv6mxEdctadudLqLj0m-yBXFAd4qvtHG3w52gFmsBzR0tbiHLiPQhzja1eVwwYhdTTJSRiUiawKAh3xkF8-_waelUsClzVRS_VrpgYUvR0u8F_B1aqeHgbNVYvRd6oFZ7y8X_AZE2dTddU7hklnWTwnVsGp7gxsfoeCo4XVGiPp2vsiO98cp7MbbD4NIrCbU0rRWoaZ8Gw5GDP2xaQPGmh-OBrcyKC8SWbbvGSMRj6-NW3d-3VhisDYzqNmEV_u-jCG2TLLs-9wkXwK2gQF5eoBXxxjWyzot3jYdmoKj_AVejZALMY5g1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba3f4a10bd.mp4?token=KrHnclCjkvz4n_2YuFLhXY-E98KN7V6rW5wp0vde2PZzEEOUfjsQnnocRYcfIaprTrc2WF6UP33VgyruZspH6LruekevOSYysMdWKBL7Q6wcUf2Usv4A0Z0_oIXu5lu_Mj-R2NX8bl-7jgvxSQsYBVbM9QPLPC00XtUL2IxGOKPMGJPsPxJuoNij_iONEIDj4xNxCeLEqXR8RV3NNUpQJjptbLfNqGMkwDCcl6XvOK1a5vYPjf013fiJpXJLNMHzsV7c8mvKvo5iZpYmANOMyvlNWGwSBeeHYKR1-fbVj_aj4ZTZS1goY0IgAChv0VdiWRs7sAAW-mb8KkBaEwkF2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba3f4a10bd.mp4?token=KrHnclCjkvz4n_2YuFLhXY-E98KN7V6rW5wp0vde2PZzEEOUfjsQnnocRYcfIaprTrc2WF6UP33VgyruZspH6LruekevOSYysMdWKBL7Q6wcUf2Usv4A0Z0_oIXu5lu_Mj-R2NX8bl-7jgvxSQsYBVbM9QPLPC00XtUL2IxGOKPMGJPsPxJuoNij_iONEIDj4xNxCeLEqXR8RV3NNUpQJjptbLfNqGMkwDCcl6XvOK1a5vYPjf013fiJpXJLNMHzsV7c8mvKvo5iZpYmANOMyvlNWGwSBeeHYKR1-fbVj_aj4ZTZS1goY0IgAChv0VdiWRs7sAAW-mb8KkBaEwkF2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام اعضای مجمع شهرداران آسیایی به شهدای میناب
🔹
شرکت‌کنندگان نشست تخصصی مجمع شهرداران آسیایی در سیزدهمین اجلاس جهانی شهری به احترام شهدای میناب یک دقیقه سکوت کردند.
🔹
همچنین دبیرکل مجمع شهرداران آسیایی در این مراسم عضویت افتخاری این سازمان را به نمایندهٔ شهرداری میناب اهدا کرد.
🔹
دبیرکل سازمان متروپلیس، دبیرکل بخش خاورمیانه و غرب آسیای سازمان شهرها و دولت‌های محلی متحد (UCLG-MEWA) از حاضرین این نشست بودند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/akhbarefori/653519" target="_blank">📅 17:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653518">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ادعای اکسیوس: واسطه‌ها در تلاش برای نهایی‌سازی یک تفاهم‌نامه هستند که شامل توافق برای پایان جنگ و اصولی برای ۳۰ روز مذاکره بر سر یک توافق گسترده‌تر است که به برنامه هسته‌ای ایران نیز بپردازد
🔹
پاکستان، قطر، عربستان سعودی، مصر و ترکیه همگی در میانجیگری مشارکت داشته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/akhbarefori/653518" target="_blank">📅 17:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653517">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2FXmBxIXgvzuRKyiibAehrlR0DsaZQm3F5tbxYPzbTDxDklqBM1yhOb_XdKUs8kessyp6AyQRzWbJllpc5FlFHmZ0Laa0jigBJXCmKlrDxjy5Hqny9B9uo7WXWq0Ny9ZxUv_QPGjtr2jjwA9rFLkjoIPanBARi0uZBCWViaEfOX1RX-VUeFR8WCl-FrnlTz8SzhiQ3fzroghQeIvL7otFVgimyMVjFmZH91G591DNCuqDB9Ghe_2jQutrzVJhAGHpx8MbAVyHe-Pt1hOYY2d5Uae0Dxcgvg9NWtJ6D7JM-fP9jThrBO5WzzGQ_txM3FFyA0k09nX97y0F4RGuSWAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یدیعوت آحارونت: ایران تنگه هرمز را به بیمه‌ای برابر حملات آمریکا و اسرائیل تبدیل کرده است
🔹
فشار تهران بر اهداف انرژی خلیج [فارس] و کشتیرانی جهانی، آمریکا و اسرائیل را مجبور به یک جنگ فرسایشی کرده که قیمت نفت را افزایش داده و تلاش‌ها برای بازگشایی این تنگه حیاتی را پیچیده کرده است.
🔹
ایران با استفاده از راهبرد «اجبار مثلثی» (یعنی آسیب رساندن به یک شخص ثالث آسیب‌پذیرتر که بر دشمن قوی‌تر نفوذ دارد)، به موفقیت دست یافته است.
🔹
در این پرونده، این طرف‌های ثالث عمدتاً کشورهای حاشیه خلیج فارس بودند که از نظر نظامی آسیب‌پذیر اما از نظر اقتصادی و استراتژیک برای آمریکا حیاتی هستند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/akhbarefori/653517" target="_blank">📅 17:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653516">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
تحریم‌های جدید اتحادیه اروپا علیه ایران
🔹
اتحادیه اروپا امروز در اقدامی ضدایرانی و با نادیده گرفتن حق مشروع آن در کنترل تردد دریایی ایمن از مسیر تنگه هرمز که بخشی از آن در آب‌های سرزمینی ایران ‌واقع شده، از گسترش چارچوب تحریمی این بلوک علیه ایران خبر داد.
🔹
این تحریم‌ها شامل افرادی و نهادهایی خواهد شد که به ادعای آنها در اقداماتی با هدف تهدید آزادی دریانوردی در غرب آسیا، به‌ویژه در تنگه هرمز نقش دارند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/653516" target="_blank">📅 17:28 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653515">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fe81b7298.mp4?token=XphVXLQAbn-rlC7RyqECHAFbS9guwS05-KMtYbsTtkcG5TdV2H70TQ64-LbhC-JP0-YDI5n49JKiFdMPBIhiziToYAxo2NhesrUU7SXbX_8MV1-gZC1a_jvrGCvj6yVF7DnrVYtSM_T7iVQAPomi_Xc4pfq7PgNjwXsT-BwClk-v5arCCK5VBajTXRfvf0bG151kd0Z6irWSFOFQckNDe3s-ZH8QltzGWqYzEfWBegigSsOFj1S5XkBJtOmxZGwverEx2st6_A8TGs5bwi5hwV3sUobx1kWlWfiS3gVn_Ab9Iw39ju7P4_ghPwDv796xDSrPgPVmWcAFEtxy9Zjx3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fe81b7298.mp4?token=XphVXLQAbn-rlC7RyqECHAFbS9guwS05-KMtYbsTtkcG5TdV2H70TQ64-LbhC-JP0-YDI5n49JKiFdMPBIhiziToYAxo2NhesrUU7SXbX_8MV1-gZC1a_jvrGCvj6yVF7DnrVYtSM_T7iVQAPomi_Xc4pfq7PgNjwXsT-BwClk-v5arCCK5VBajTXRfvf0bG151kd0Z6irWSFOFQckNDe3s-ZH8QltzGWqYzEfWBegigSsOFj1S5XkBJtOmxZGwverEx2st6_A8TGs5bwi5hwV3sUobx1kWlWfiS3gVn_Ab9Iw39ju7P4_ghPwDv796xDSrPgPVmWcAFEtxy9Zjx3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرمانده سپاه محمد رسول الله تهران بزرگ: نیروهای مسلح بیش از گذشته آماده‌اند
🔹
اگر احیاناً دشمن اشتباه کند نیروهای مسلح سخت‌تر از گذشته، دردناک‌تر از گذشته و سهمگین‌تر از گذشته پاسخ سخت و قاطع و پشیمان کننده و تمام کننده می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/653515" target="_blank">📅 16:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653514">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/akhbarefori/653514" target="_blank">📅 16:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653513">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGDn2bajNSOrj8sIeqojnk1_qn1Pzgp9YaQf_ZkaSdpeY4AeXu4JhOe2QdD7S_vv7tm1Lf4Whlo8FTfVCEv0YejIiiK79s26Kr5IG_p4MOIc26z7OAdyBrAvp_Ab7rAIbyLXFwBfM8h6trHzTQw04ZINr_LL_8DffGZzaIzpeqJSeRpuZhxiLBdtmM9qM9EvPCJzckCY28XTw8Q6n8ArRfSGXbDyHaWhp13fuPjPlrJx9iq8Q3mzy_Zh27cVEGe7a28EpkiCe6Z82R-XhY9TIgYGrHUaLZGGzTFO_858krOx0pRFNHDeD5V_SRpVCAEyb5dg7OazEAs1nnMLQ69EtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار نماینده ایران نسبت به آثار حقوق بشری محاصره دریایی
🔹
سفیر و نماینده دائم ایران در ژنو در نامه‌ای به کمیسر عالی حقوق بشر سازمان ملل نسبت به آثار حقوق بشری محاصره دریایی ایران هشدار داد.
🔹
علی بحرینی در این نامه با اشاره به پیامدهای این اقدامات غیرقانونی بر وضعیت حقوق بشر مردم ایران تأکید کرده است که این «محاصره دریایی یکجانبه»، که در چارچوب اقدامات قهری یکجانبه و در بستر فشارهای مستمر علیه ایران اعمال می‌شود، آثار حقوق بشری گسترده‌ای در پی داشته است و در صورت استمرار، حقوق بنیادین مردم ایران، از جمله حق توسعه، دسترسی به کالاها و خدمات اساسی، و همچنین حق بر سلامت و دسترسی به تجهیزات پزشکی را با تهدیدی جدی مواجه خواهد ساخت.
🔹
وی همچنین تأکید کرده است که این محاصره دریایی مغایر با اصول حقوق بین‌الملل و غیرقانونی بوده و به دلیل ایجاد آثار شدید بر غیرنظامیان، از جمله محرومیت از غذا و کالاهای ضروری، مصداق جنایت جنگی است.
🔹
در پایان این نامه، یادآوری شده است که وضعیت جاری در منطقه نتیجه تجاوز آشکار و غیرقانونی آمریکا و اسرائیل علیه جمهوری اسلامی است و آنها مسئول عواقب اقدامات ضدبشری خود هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/akhbarefori/653513" target="_blank">📅 16:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653512">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUuQAaTrAchSqqJwdSjRelqKDPI1WhqTiO9UbsX8YjS1r-cDGO4Kz0_s2JYiApE5Ha0SbL-80xNZuKWJSgYFh7kKRUZ1DKh1NrNa2BjYohWlnFTVSGxL3kLPdsgv_qlw-NkESPP1txqb88FTRAH1T1RV2f3BaHQdRT2j7rwJ-G2E53AqkPugvPmtP7JSpZevChAphrR6JBMWEOZNBYbh6ssUAVKUq5doF7zGjSYavCin9KUhJgeZIduTIbh40tfQjSKi8EknofsjJCdqyyDwq5VJhe396pFuYmvG4Wnp99YZ1dsxCiJ_S2HLje9SN4QtloNa7Cn0AzMPMgDphGaUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تسلیم در پوشش دیپلماسی؛ چرا پایان بازی ترامپ، «شکست پنهان» است؟ | خواسته‌های ایران، شروط یک کشور پیروز است
🔹
یک تحلیلگر آمریکایی استدلال می‌کند که دولت ترامپ عملا در جنگ با ایران شکست خورده و اکنون تلاش می‌کند بدون آنکه افکار عمومی آمریکا متوجه ابعاد این شکست شوند، از بحران خارج شود.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3216949</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/akhbarefori/653512" target="_blank">📅 16:29 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653511">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
شبکه ۱۲ اسرائیل اذعان کرد در پی حملات حزب الله، صدای چند انفجار در منطقه «الجلیل» شنیده شده است
🔹
این حملات، باعث آتش‌سوزی در این منطقه شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/akhbarefori/653511" target="_blank">📅 16:17 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653510">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyYMzCNTdLO50X22onnADi7Rzod68DMIcbURIUbMkGh-I1RET4AyLYMLLFb_BFoSbq0Uh30UnCFruxwAHI8QBTtuulP2Dx1E-4ZLrwFiIZy-PNlVpZbC9ObdwCaGLMUeB-ywdlbuh1on6DgoWAcqLrP4jS2YduEeEohGxiSbuAou_mH6AoNokkgLqDAc3h6mbh65ce5IM_vG5yybBvbXtIFqCYvYJ7r0D_WudA6oJOzbNuF-_Q9sBhwPVbwZoHot1ocbPKaMyZa3ZLHANv0MlQuIiF7TW5cD6WR9wcrSVucgP4re8PVc7P23sxkQfbqyhFEQQNfr7k5X4z8NV9gQrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر خارجه روسیه: آنچه اسرائیل انجام می‌دهد نه‌ تنها با قطعنامه‌های سازمان ملل، بلکه با توافق‌ های «شورای صلح» مورد حمایت ترامپ نیز در تضاد است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/akhbarefori/653510" target="_blank">📅 16:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653509">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sB8hJwqEH1AWnX3rCCsRo4xy3dT65DTX8mlavxz1fZWhawiJIWRL7RtfJteysdW-mHvk9Kq0GYVJVZJ2v3QqVtHBX9IlCfO-wytWMi7ZcZPtwb9nAd0gVij2m6RlQq7WqFhhQb-P4r7rk1zABUA0CAG1MJPQJcFzfzTfsnwexmo6xqQ6aC4YZrJXWwgu6Myr292ZdNxxTna7h0qHZZkPQPEhyXqe4Nj14EVKJJNnDL5vKOlAmA0k-3k6nevSWo9hjonYQvUQZ6bS8xk2GZtx7XSHCX1YyM838IdcywM30jMo_-SL6_TpnVE4xcMeXBnTNu_uB2rlhyh2lsZ4ppjeHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهکار جدید ایران برای بی‌اثر کردن محاصره آمریکا: استفاده از نفتکش‌های قدیمی برای ذخیره‌سازی شناور
🔹
تهران برای تداوم تولید نفت خود، به روش ذخیره‌سازی شناور روی آورده است و از نفتکش‌های قدیمی لنگرانداخته در خلیج فارس جهت ذخیره‌سازی نفت استفاده می‌کند.
🔹
در حال حاضر حدود ۳۹ نفتکش حامل نفت و محصولات پتروشیمی ایران در خلیج فارس مستقر هستند و تجمع بزرگی از این کشتی‌ها در نزدیک پایانه صادراتی جزیره خارگ دیده می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/akhbarefori/653509" target="_blank">📅 16:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653508">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szjKfNf84HH5ozVDt5eN1aDKV8xc05seur0V0j37FwZLhDylNl_vkx8Nt89hpB60m5hVTolckrnRHcBjQ5t6O_7RBbAB2iSgUrMFt4eGukaqheZmEKpsPTj7tuIYgQu5ufnL7WrxxpgDp_avYj-kG8GW4oTLp4JgxpYLSlbX-TlMoqzMTVnQpXKO2LMtGES53NQnUJvov_5EFZdUdWCwPeWaLYd7VZnK0O9URSE4vSLy5NZq18JPpb7bXFUxUplzMm_Hhoj4L8cEREzCQ1ooFpxzwyA-oLAdvCZb0IeyQJSTd0ef6B2GcbG-WO1YAIvCfbe6eqAoICzFncqcZB1GJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رمزگشایی شگفتانه‌های میدان علیه محاسبات آمریکا
🔹
کاخ سفید قانع شده بود که ایران در کمتر از سه روز با بمباران و ترور توان موشکی، دانش هسته‌ای و سلسه مراتب فرماندهی نظامی از بین خواهد رفت، اما باذن الله نشد آنچه گمان می‌کردند...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/akhbarefori/653508" target="_blank">📅 15:46 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653502">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gvje81mD3IEnUQK7kgNb4v46HegDU9YWvBVy9nQuWEvmoz6tmszrY5vi89zO7dmRNbeholYYMihn_OLND-N9Wawd00Atizl2FoflqGQPWzagdEf_ZoyqzUDJ75zw2dP_SVzFm9k39VnJSahsi4SI7dMbWoCub46pFbSl4JIBuemiGBNeToI_WsQeSxnDIEIYJYI_F3C7EKHZGXTjRjn8ow-NVEwC-k9WPhMoH81gjbYisuEKB8wJ9aqP6rov2LjkLxgnLKlGA_DhBXeC69E6gOQFshm8C9UxH3EGXzttxLBbxJmfigRBbA2r81b93mxPx-NZe3jVROdaoUUEi9h6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mulG0_P6S77jYrP_CiCJ043cwNVd82edSKrEXoe7T3et2ybzG0ladYOpQZo1jvL_QBR51TKsT-zXjhG2IosB-7k5dwhYqkuRkaQrBUtWG4vOc_O0QrnLavpUzBPo5K8dVSbPB5LuSR2x6xYFZ6wP8RbQze8yW4XIbeIXaRTA9q4cl0tM71KI3hONEgqUhycnZHrEiqxzUar8ZF0cVfMJGidlVth1Qj0jBkw0lumB_iuCiRsycHt75ZFKWf5gnWg6HyqLZxSZSKbQZ2wASXMP92Qumzz7Gk1YH6Cmi3P78WgLuuOEkaqk7qdaKWRBxD1BPA39mr6pj4EsXSTDv9dPfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/spziowZ9szC1YQxfJ-Ke9kwEmjH6YAirHccYc7WJKf0tpn5SNIj9ISat2wFZ7DX8XnmfIWOV8obvLVYVWunlnHjJ7L1hWFRVOwlu9J7fA-QfYYIl-LIfE8vopoTIijJtrBmwW6bBdKjJnjLYxMHp-PoJq5emddnWpRkHSN9_Di39vzEgPUUqNXvYAa6rVB4_VMpwgL_PTW0hbk_JpnY2JSJ0Kt2O07pktn7nWtSJzAyKK6oryTMlqsXC4ok6uzRz0jzBd31160DnYwxIrLlLXCm_IEyR48VSoqgya1gL-gUt-Dx0PqT5zVaJ7idhaamGf1S7zv9QoXSH7SLpjy0gDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qo_FDSNSj4keNkUSmmxXpYuGGKVVcjvw36fN76R24sd35AB6hPSTLPUVGsNLwqs50Vi0aXu6ySp0JCc3Ps1-Fjf28kwGdJ8eepL2YmArOEYO6wNprwK_8Qhi6VHp5v4YNiQmttjJf-P5gbRfq2Jsf2vDXKDxRqbWIx80oUMZN_uFrcUnoIXmLy5SHCzTVQJaNe7M2G1PTNBEWIaQVzqQh69lhcliAAq5mePEipn7_iPpOBEIk4ES4z1htbpGRVcJodf46J359UwdVpdTTyi5LaWNp1Qrz0RJFTGaNWK0mq2uwRnmcZGDf5Vpg_hyos7bpuMEnBJUwch688y2ZiZL6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/azo3jbN2255JUxxqN8nedfKskzc1YurgKtlpmKo46JJNKfDHnb64qnRE654flQQHdbT6zgeaDcrGuo0kFzVR1YRS2GWswKGz1ZzeUr1CE5VnWOAz2PeIedb_Lq_UsvoiETI2zPvhdbn4WhR0VU6eQHjTVZmceCAjY8MUtm-SPk1OSEMkUgJzO70w_ANXlS01SjvuNVITzhux9yNE9qN-MLqPIa00wUtkBPJ5lIrRMvuzEyvFGaJnHmM9fp4iD4f8NfHBmEaeEfLb7iGQtWq9VdGoWwY9RlylInqPDNwX1j0Y_IKJx4851uemO1jz9WAkmhT9GhQ3BME-czK6LtoeXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZnrR5_hxWhUItokH1NqRBysZvomly9ketlLJOdhxbzw63NSYaflFlIAGExJam6R0-50ZU8rXYVuUY3hq1w_BZgis274YCZGpFacOQSiY6D6a5pPe4d5PPx-Xw5vhSAitfdV0M9LIQKla91iKqOpgWZT3FR2Bo8r641aFKCyDZseC4yuoZ_r4eW0zkNs2t75UQS0soRBeyTXBY0bDaeccW-BHzQGmBW6AnT9lsz7CC7y2OxiNzCdEuybZl2BJcvUvfQrEJn_FHcUSUOQrqNdkAzh4vCj3_ZGf3UhGGbgDjoaAwJF2CJwCkA6haxzwpughPLdVtyrA3EYSX6nNMphkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رژیم مفید این روزها؛ روانتان را لاغر کنید!
🔹
برخی اخبار ذهن شما را مصرف می‌کنند. قبل از اینکه دیر شود این اسلایدها را ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/akhbarefori/653502" target="_blank">📅 15:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653501">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b118659c8.mp4?token=Vi1mqE31gBBdk8JfnO3o5Yq0SJrNdBOm0kc_rx0QmCHJBKeB4jxNsEJ5RDEBxcRGw1XPcfN7T3yq4F61KtA-v2GK3UYPRry68_cpPTxacw1oaofhyGkDrufVC5d7Et1dY6B8PFP8SNk5QCUaZkKoUC3455PNCAnehSChAojEy2t45CfkmD_bCVDGqFx2zD4zlmVjg8soec5pcIc9M-_vyW-L89Wu3vCKtYpfuk0utm1S7f8keCqQZlEFEOXlbXUkK9JzcoDjQHetFKYhtk8bKVyfaN0t5axs8h1dNjJfN5_KuUVctEQrVhe6Q6gBswzxJMNSPKsRogdfl9OIYqrGnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b118659c8.mp4?token=Vi1mqE31gBBdk8JfnO3o5Yq0SJrNdBOm0kc_rx0QmCHJBKeB4jxNsEJ5RDEBxcRGw1XPcfN7T3yq4F61KtA-v2GK3UYPRry68_cpPTxacw1oaofhyGkDrufVC5d7Et1dY6B8PFP8SNk5QCUaZkKoUC3455PNCAnehSChAojEy2t45CfkmD_bCVDGqFx2zD4zlmVjg8soec5pcIc9M-_vyW-L89Wu3vCKtYpfuk0utm1S7f8keCqQZlEFEOXlbXUkK9JzcoDjQHetFKYhtk8bKVyfaN0t5axs8h1dNjJfN5_KuUVctEQrVhe6Q6gBswzxJMNSPKsRogdfl9OIYqrGnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرشایمر: جنگ با ایران برای امارات، یک فاجعه خواهد بود
🔹
امارات در حالی در هفته‌های اخیر اقدامات ماجراجویانه‌ای را علیه ایران صورت داده که به اعتقاد نظریه‌پرداز مطرح آمریکایی جان مرشایمر، «ابوظبی توان مقابله با تهران را ندارد.»
🔹
جان مرشایمر در مصاحبه‌ای با اشاره به ناتوانی امارات در مقابله با ایران، تصریح کرده که ایران می‌تواند در صورت ورود جدی امارات به جنگ، زیرساخت‌های انرژی و همچنین تأسیسات نمک‌زدایی امارات را هدف قرار داده و نابود کند. ایران بارها بر روابط صلح‌آمیز خود با همسایگان تأکید کرده اما در عین حال گفته که هرگونه اقدام علیه امنیت این کشور از سوی کشورهای همسایه با پاسخ دندان‌شکن مواجه خواهد شد.
🔹
این استاد برجسته علوم سیاسی همچنین تأکید کرده که «وقتی آمریکا و اسرائیل با هم نتوانسته‌اند ایران را شکست دهند»، امارات هم نمی‌تواند با ایران مقابله کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/akhbarefori/653501" target="_blank">📅 15:29 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653500">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYYqLQVjes-cQlZmAj_viX7wTILR2_NCChRpgbg76kfjh9DMh6lo282qMXWxF87Gx5m7xsmHC7dMvS0q91D2gzpCUVAdBTWCSzfITATHMfp_n2cLdSToBpqh5Pm-Qp8FDSh1pc8hoOLSzz8cYQWMfgq1XV1HB6ceT1JPqHmLJv-I_rfj1blpUIdOhAubDfzJso2Y7oJMwDsWXKYrJKqxleslkyVMmpQjJG7ysFMEZIuBF-6AL4OHpI0k_gj6aPPL38c6MUPLDnNxO8gHdEBmVDsJpbF5ZCn71gJG8NxW7FfWeS4vvb3kaM1xlxH_V8_oaG2RutNcf5VyhyupvrFG1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراموشش می‌کنی، اما برمی‌گردد
🔹
هر بطری پلاستیکی که رها می‌کنیم، قرن‌ها بعد دوباره سرِ راهمان سبز می‌شود. امروز کمتر انتخاب کنیم تا فردا سبک‌تر نفس بکشد.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic…</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/akhbarefori/653500" target="_blank">📅 15:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653499">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: بروید نارمک و راحت احمدی‌نژاد را پیدا کنید
احمد آریایی‌نژاد، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
آن موقع (در دوران جنگ) شنیدم که آقای احمدی‌نژاد زخمی شده است. صحت و سقم آن را نمی‌دانم، اما بعید می‌دانم. احمدی‌نژاد نارمک است. می‌توانید نارمک بروید و راحت احمدی نژاد را پیدا کنید؛  آدمی نیست که پنهان شود.
🔹
بحث آقا معلوم بود که مجروح شده‌اند، اما مجروحیت ایشان به گونه‌ای نیست که نتواند کارهایشان را انجام بدهند. تعداد قابل توجهی از مسئولان می‌خواهند بفهمند حال آقا چگونه است که این لازمه ارتباط است. ارتباط گیری‌ها باعث می‌شود جای ایشان را پیدا کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653499" target="_blank">📅 14:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653497">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
بولتون: مذاکره با ایرانی‌ها هدر دادن اکسیژن است!
جان بولتون در گفتگو با بلومبرگ:
🔹
من فکر می‌کنم مذاکره با ایرانی‌ها هدر دادن اکسیژن است. فکر نمی‌کنم آنها هرگز به چیزی برسند که ما باید آن را رضایت‌بخش بدانیم.
🔹
اولین گزینه ترامپ پایان دادن به آتش‌بس است، که هیچ سودی جز سود برای ایران ندارد. آمریکا باید در صورت لزوم با قدرت نظامی، تنگه هرمز را باز کند تا اجازه دهید نفت از طرف عربی خلیج [فارس] خارج شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/653497" target="_blank">📅 14:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653496">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
ایران و آمریکا بر افزایش سقف خواسته‌هایشان درباره اورانیوم و تنگه هرمز اصرار دارند
🔹
یک منبع پاکستانی با خوش‌بینی درباره امکان دستیابی به توافق مرحله‌ای بین ایران و آمریکا اعلام کرد که دو کشور بر افزایش سقف خواسته‌هایشان درباره اورانیوم غنی شده و تنگه هرمز اصرار دارند.
🔹
این منبع پاکستانی تاکید کرد که کشورش همچنان به امکان دستیابی به توافق مرحله‌ای بین واشنگتن و تهران خوش‌بین است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/653496" target="_blank">📅 14:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653494">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سیاست‌های کلان کشور آرایش جنگی ندارد
صمصامی، عضو کمیسیون اقتصادی مجلس در
#گفتگو
با خبرفوری:
🔹
سیاست‌های اتخاذ شده توسط بانک‌ مرکزی و دولت متناسب با شرایط جنگی نیست. ظاهرا دولت متوجه نیست در شرایط جنگی هستیم.
🔹
این که بانک مرکزی اعلام می‌کند صادرکننده ۶۰ درصد ارزش را برگرداند و ۴۰ درصد را برنگرداند و یا دادن ۱۰۰۰ دلار به ازای هر کارت ملی آن هم در شرایط جنگی که کمبود منابع ارزی داریم، خلاف آرایش جنگی است. ارز در شرایط جنگی باید به اولویت‌های اصلی تخصیص داده شود چرا که منابع ارز کمیاب است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/653494" target="_blank">📅 13:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653493">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9a4f2cb19.mp4?token=qFPA8wfIMA5mfFHF-tc5_aNPZ0AKyxzdml8QzvudrC_rzaDyiSnOCsSfyXnYqQ0YgBTQQTK7GwCGED4CYxzhPjtcve0BMNJE__-qYD6gaVgSPU3iVVGy7Z5DvUIHpDILE-lxhluoOWjdN289u_FlmVgJ6iMKCmBBhc1yXyTlkMUD662IlGWH-5DS851MKI5w6-HoNcOc9KepbfRT6kukfob1VbdzrRvuzAPWoUEkM-3Qm19VYl5gqWduMpU28RQdb9o1zKaypIEgS-cc7LXkduG7UFjFGfBzjIi4MZgNbQLMALqKDTY1MNZtENmI8IZjFnL_ufoodj0DqF6xuPKIfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9a4f2cb19.mp4?token=qFPA8wfIMA5mfFHF-tc5_aNPZ0AKyxzdml8QzvudrC_rzaDyiSnOCsSfyXnYqQ0YgBTQQTK7GwCGED4CYxzhPjtcve0BMNJE__-qYD6gaVgSPU3iVVGy7Z5DvUIHpDILE-lxhluoOWjdN289u_FlmVgJ6iMKCmBBhc1yXyTlkMUD662IlGWH-5DS851MKI5w6-HoNcOc9KepbfRT6kukfob1VbdzrRvuzAPWoUEkM-3Qm19VYl5gqWduMpU28RQdb9o1zKaypIEgS-cc7LXkduG7UFjFGfBzjIi4MZgNbQLMALqKDTY1MNZtENmI8IZjFnL_ufoodj0DqF6xuPKIfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار وزیر نیرو درباره وضعیت آب تهران و استان مرکزی
🔹
تهران و استان مرکزی همچنان در وضعیت ضعیف آبی هستند.
🔹
وضعیت سدهای ساوه و کمال‌‌زاده مناسب نیست.
🔹
اولویت نخست، تأمین آب شرب مردم است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/653493" target="_blank">📅 13:44 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653492">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
کنگره آمریکا رأی‌گیری برای محدود کردن جنگ ترامپ در ایران را لغو کرد
آکسیوس:
🔹
رهبری جمهوری‌خواه مجلس نمایندگان آمریکا، رأی‌گیری درباره طرح محدود کردن حملات نظامی ترامپ، علیه ایران را به تعویق انداخت.
🔹
این تصمیم پس از آن گرفته شد که مشخص شد جمهوری‌خواهان رأی کافی برای شکست این طرح ندارند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653492" target="_blank">📅 13:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653491">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGvWx8DkupSMbGE2DKP37Qvugib9JWt2uNI8GEJXPUNWZUNxoUNY4_OefG2yMffM3tNYxcs7HOVFeCJI4MJ-I6-9RjMt4-xaFk4VkFV9_8dwg3PWf8NsCa2avoBUWuT66qI4Aycpm1UUlZbRtY003ifRnI2mPk-mdkF0OJKlp-g8QSFUAhKdpNQ-UWt-O9G1io1fFI-37pr39W2cthQSQ46YKb9i_xywgtth_-kaJw-M_FZKDhAl2n2JQvBhPseTiKVpBGqsjiuSEOHzjOBCnYlZimbv60IbIDd_B2QzutNHBClKYdUOM6AV05AqZtkCMvwj23B0ZnAZuqEOlDfxrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت خبرنگار لبنانی در حمله اسرائیل به دیرقانون النهر
🔹
خبرنگار لبنانی «احمد حریری» صبح امروز در پی حمله اسرائیل به شهرک دیرقانون النهر جان باخت, منابع محلی می‌گویند او هنگام انتقال مجروحان هدف قرار گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/653491" target="_blank">📅 13:28 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653490">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/816be2b81c.mp4?token=vTkczUoq5eDCsz5pXmduJ6_UzIrDcgCb3HSaitObq8qZycwWwjUnuDl5WR-v8EwdN-FYkzNorpUtih3YHDHeqLbDErxEDeerEBy0N8mkGyjxhx0CEdFJLRWalamtc21-rUrVewji2L9JZJG5zAnxOzbdUMSNVoKUzLsb6c0RMs9Ph2tc9SfwW7C3rzveLZTC9rfTFZzZeMClcGiz2c1FUS3VRiAANDar5MJACFVbH8kQ45H-tFpPbptl7RvAGrsSV20BHwTN5BrJJjJAclEjQuW08LgJzDhtUW_FSRPcsU43wbBV_jcp4McenapFcBHhsqkGs1N0uQD2sVLnupiZ2SOSgyWFB0qipuNz-zu6OwX4dKXDggvWttzG0l_5B4PSH6eyCElC2vlEXRyl1tBMed6InAx1p5uu9j_3QsL4rqarmsne_yK5i3g5c5bhvUB_6TEbT938VD7PpfBdTYMnL0F1DfJt79koYYo5cLCbQ-4trVFRIS764KEvZvyB8gVddAFgQQPtEtpY7-lpdWTZJFuS_ipS5dHNKOBp1RPMCl0oFjw1_Nw0qJDwiU_ahohK1amMGktzyo5Pp-6bibTt60CkHy9SJYlb-vaWiXev_FM9AHraFjDfLTWKuMuH-HvkmG3merS8TBLHKJXNYBCBZ6BFdQszwrsO_CqFk8v81j4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/816be2b81c.mp4?token=vTkczUoq5eDCsz5pXmduJ6_UzIrDcgCb3HSaitObq8qZycwWwjUnuDl5WR-v8EwdN-FYkzNorpUtih3YHDHeqLbDErxEDeerEBy0N8mkGyjxhx0CEdFJLRWalamtc21-rUrVewji2L9JZJG5zAnxOzbdUMSNVoKUzLsb6c0RMs9Ph2tc9SfwW7C3rzveLZTC9rfTFZzZeMClcGiz2c1FUS3VRiAANDar5MJACFVbH8kQ45H-tFpPbptl7RvAGrsSV20BHwTN5BrJJjJAclEjQuW08LgJzDhtUW_FSRPcsU43wbBV_jcp4McenapFcBHhsqkGs1N0uQD2sVLnupiZ2SOSgyWFB0qipuNz-zu6OwX4dKXDggvWttzG0l_5B4PSH6eyCElC2vlEXRyl1tBMed6InAx1p5uu9j_3QsL4rqarmsne_yK5i3g5c5bhvUB_6TEbT938VD7PpfBdTYMnL0F1DfJt79koYYo5cLCbQ-4trVFRIS764KEvZvyB8gVddAFgQQPtEtpY7-lpdWTZJFuS_ipS5dHNKOBp1RPMCl0oFjw1_Nw0qJDwiU_ahohK1amMGktzyo5Pp-6bibTt60CkHy9SJYlb-vaWiXev_FM9AHraFjDfLTWKuMuH-HvkmG3merS8TBLHKJXNYBCBZ6BFdQszwrsO_CqFk8v81j4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«سمفونی مرگ» در جنوب لبنان
🔹
ویدیویی جذاب از حزب الله که هنرنمایی رزمندگان در شکار موجودات صهیونیست را به تصویر می‌کشد.
🔹
این موش‌های شب‌زده را
🔹
ای گربه‌ها شکار کنید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/653490" target="_blank">📅 13:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653489">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVVFyMl38DxyPrjWtYgOOQ0WMv2SXFhAOPy3sUmuDCjQ52fX4Y-T2Rh75jrJmEPyWX0ffPuFZknqF3yeh2Ppg7NGpgoebCUalG8eGNanfD5YqN34FOXaeGd3UJpZWxQ4vYjsxQs1G-W13bZJ4PuQtaHKz6Zakgn6LIRN0VFWddwYQZ_8B8cfwtZg22lGghJgQ84Vq6Wb898CAIk7bMjJfPp2n7EzAneNHQD4VwkNbFcjtn8UJvI-D6ZJNKxYo4FpvskqQ6IvU1KqlN4alPBgeOkFuv3yeF3Pqip91KCAay2LDedSDU8LnERL3sCATj_V3mDexVBVEcxAH9D8Gztfyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله پهپادی اوکراین به خوابگاه دانش‌آموزان در لوهانسک با ۴ کشته
🔹
حمله پهپادی شبانه اوکراین به یک خوابگاه دانش آموزی در منطقه لوهانسک دست‌کم ۴ کشته و ۳۵ مجروح برجا گذاشت.
🔹
یانا لانتراتووا، کمیسر حقوق بشر روسیه، گفت که ۸۶ نوجوان ۱۴ تا ۱۸ ساله در کالج استاروبیلسک دانشگاه تربیت معلم لوهانسک در خواب بودند که پهپادهای اوکراینی به آنجا حمله کردند.
🔹
لانتراتووا در بیانیه‌ای گفت: «نیروهای مسلح اوکراین یک حمله هدفمند را علیه کودکان در خواب انجام دادند.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/653489" target="_blank">📅 12:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653488">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f35adc40e0.mp4?token=TIH5p--ClVD1XTnnwWMowfF-iWio16pWgT47OaZnxdh5Hq12ab_5XTGvNce_vt2cc9qBxNZ_aBOdxZnCaJenhD17ejsYX2AXygfMxaIpzlzuFatMPukuDdv_iueaERLPVKuk2YUaT_vbUnH0VvXlHu9TIvu7ASrgflADc2KOOxgiYmPYof-HcyhE2_7KbLEtzBWkXkWyUl6kN1luH7OVJv8peMu6Ki-OQCcPWSqvEF-WSMRqyURMCuwgSFoGP5upKMEGqpwQqdIEH0BIoKjGhC6KdQPeBSVxPWoicVT04P6jkVX-ayyQut_0dm1gdMSR8B7AMLzheYyoaXXoMExD3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f35adc40e0.mp4?token=TIH5p--ClVD1XTnnwWMowfF-iWio16pWgT47OaZnxdh5Hq12ab_5XTGvNce_vt2cc9qBxNZ_aBOdxZnCaJenhD17ejsYX2AXygfMxaIpzlzuFatMPukuDdv_iueaERLPVKuk2YUaT_vbUnH0VvXlHu9TIvu7ASrgflADc2KOOxgiYmPYof-HcyhE2_7KbLEtzBWkXkWyUl6kN1luH7OVJv8peMu6Ki-OQCcPWSqvEF-WSMRqyURMCuwgSFoGP5upKMEGqpwQqdIEH0BIoKjGhC6KdQPeBSVxPWoicVT04P6jkVX-ayyQut_0dm1gdMSR8B7AMLzheYyoaXXoMExD3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدالت یعنی قرار گرفتن به اندازه هر چیز در جای دقیق خودش ...
درس انوشیروان عادل به دنیای امروز
👇
https://youtube.com/@caffeinepodcast2025?si=ZkcqfzRb9diYDZJV
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/653488" target="_blank">📅 12:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653487">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/617f81fe39.mp4?token=EMYoHbsX23RMnnX7aACLnKbadXstZcksKupUrYwkEsXsPBFEjpsR279XonQqJawcG3f3Gzay1XMC1QpMrd5M1emORhcI7G092VdWdN1wcTk99MLA987AOpQjDstm009_Gc3Jb7rZKkDRAgE2Pfz4rW9S9tkHpePkCDeQ2Bqe0dH9flq5ZiScuZbpCy_jjHKaPGzSgC4aehH-DFRfuHFVlcHwAZWPFc5vWIleXVw9FlfYd0c8nEUZxEo_BCwoHxtxhFHzlAyS_Hdv5rtsy5Jtukw2X0-NWbZ0ivMRl1HQyZ-4Lfah_J5An-qiPK_lkf4TQeJ8bOfy0Thvm43rkxtwYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/617f81fe39.mp4?token=EMYoHbsX23RMnnX7aACLnKbadXstZcksKupUrYwkEsXsPBFEjpsR279XonQqJawcG3f3Gzay1XMC1QpMrd5M1emORhcI7G092VdWdN1wcTk99MLA987AOpQjDstm009_Gc3Jb7rZKkDRAgE2Pfz4rW9S9tkHpePkCDeQ2Bqe0dH9flq5ZiScuZbpCy_jjHKaPGzSgC4aehH-DFRfuHFVlcHwAZWPFc5vWIleXVw9FlfYd0c8nEUZxEo_BCwoHxtxhFHzlAyS_Hdv5rtsy5Jtukw2X0-NWbZ0ivMRl1HQyZ-4Lfah_J5An-qiPK_lkf4TQeJ8bOfy0Thvm43rkxtwYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موتور سواری فرمانده سپاه تهران بزرگ در رزمایش جانفدایان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/653487" target="_blank">📅 12:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653486">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1KO6irFkhY4s0mYthHMSpMc1NvxGznCmrdiTHX5W6Z4PYKdX9U3sLlqKnnxSjafXYhBvinvtsgvTcF5OwjQ9IQeg_DaMbKx9V_-XaeCAV22pfQhfO0BPtHAl3BSILt2ZM7a8XtZiS3RFRQsdahFEc6UyQI2LkQ83qdXWXlEu6T8TUZ8fmu44Z4UUXcRkaM2346XPVEdeVjYCfGzjIhT1LCdlSiRckYqooB5lkq_fuM-sBtI8zaB4x0vm4MgkLpL3ingwk7mAeDSHJxSfewYllno-WhEQLmneQk4kJp4UemkHYAsYGZpb6TtEW3lf91fTKaS-JLcrcgySxIWQnBfrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مذاکرات ایران و آمریکا؛ پیشرفت نسبی، اختلافات جدی
🔹
تبادل پیام بین واشنگتن و تهران در شرایطی ادامه دارد که همچنان دو طرف بر سر مسائل کلیدی با یکدیگر اختلاف نظر دارند. نشانه‌هایی از پیشرفت در مسیر مذاکرات در طول دو روز گذشته گزارش شده، اما همچنان اختلافاتی عمیق، مانع رسیدن به یک توافق نهایی شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/653486" target="_blank">📅 11:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653485">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpcKMuW42yRktVNEGuCEdgeXwMGZ4E4ANfSXEK_qz7K-5HoliwNgy1XWEBz2OTe2RHRK1fW6FgZLheQ3f1DWCZcRplKT0AIc4-ZQdgdQiRHfBr3hcn2RQT2CeIVl0_sF84i5KT130mWRagVNxhecqdtgTYS1TuPS1XA3Sq1D0ofVP4mKr0cbLFBWu3oPWb4olRZUoQt39UIr3FNbb6L4B6bbXli9iTn8mXApwdKQS5IUEuplTbagbPzmKbVG7Y_PDfIR4uUpDwRtdq1fIkV8S8NiEOp9u5M8qMkTWGRydlbJFl-IHRVMUAEKPq_Hdwt-jGndTO8LWfmKAXLOP8mcxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع حادثه برای یک نفتکش نزدیک یمن
🔹
سازمان عملیات دریایی انگلیس امروز از دریافت گزارش‌هایی درباره حادثه امنیتی برای یک فروند نفتکش در آب‌های نزدیک جزیره «سقطری» خبر داد.
🔹
این سازمان در بیانیه‌ای اعلام کرد که یک نفتکش در ۱۸۱ کیلومتری شمال سقطری، تأیید می‌کند که یک قایق کوچک حامل پنج نفر به آن نزدیک شده است.
🔹
در این بیانیه آمده است: «تیم امنیتی مسلح نفتکش با شلیک گلوله‌های هشدار دهنده، قایق را مجبور به تغییر مسیر کرد».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/653485" target="_blank">📅 11:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653484">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hb5kYR-HLHWY1zhGGB0f0oFv1rs4iiJXvNyhcQyuVub4lGGT2y6NMTcAhlq5FpuiM9I-KsmEaI8w3VJfHjr5J7YHKeHI_xrSXhF9ehuQ9HJnIqeBFhBZi9Yv7jzzIQcKDQn20paXqNzXJQrhRKP4TmPDmwXBU-SUWZyQtF-Wt9HhQQShMWe56DzkCvxdiu0MTP90ML1LtE0yasBc4fPYKM2N9_edrPRhDD73n1S0EjMfHCuBkrJGh0JFisPpZfhAgdcDeq9wLGQlPNYjHqDkoOjMWPOaRi4K0eMBs-v6hofx9gL6ceQCCgaazqHUwpw84aoR0fPYVkuJm6Dnen9lJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلاستیک؛ مهمان ناخوانده خانه‌های ما
🔹
پلاستیک سال‌هاست بی‌دعوت وارد زندگی ما شده است. وقت آن رسیده با انتخاب‌های آگاهانه، این مهمان ناخوانده را از خانه‌های خود بدرقه کنیم.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653484" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653483">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgGXBTj6AVNRnchwmGzRY1My6k8usqTrWypaEKVvcfax6d5yMrVH841W5uKu54gjnK1k46TQTpTfMKv3YyQiviozJNMM2WGEL3wamCOFztelOcWxbgJQF_JqSajoay2sb-OLDVC44fB1a9vRm1-WHcLSqcAlu7-r8h3BG8cp7zycWPtXfnM6ssMsyV6IK-Ji46n9j9Oh1jNOPheWEERELUdXBN9nXz_8vEBHE1SxQxPdjv7nZH6TIE4rBrHGCtydnUgiAf1c5YIzMcISF1Gcu9ki680aUsLz95WHDs7NslY75g2OsKDopQktDysvTSw4pPxCRW70EUF0ZKCUKmrNWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی: موشک‌ها را برای مذاکره با شیطان بفرستید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/653483" target="_blank">📅 10:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653482">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
چین و پاکستان یک ابتکار را برای پایان جنگ ارائه دادند
🔹
سخنگوی وزارت خارجه پاکستان: چین از تلاش‌های میانجیگری ما حمایت می‌کند و به طور مشترک یک ابتکار پنج ماده‌ای را با ما ارائه داده است.
🔹
نخست وزیر پاکستان فردا در سفر خود به چین، ابتکار عمل مشترک برای پایان دادن به جنگ را مورد بحث قرار خواهد داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653482" target="_blank">📅 10:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653481">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4OJgaBbjjF8xzPNCvQ0pAeFhn6i_GD4-sfIWgKw4WWvPqjaAI8Q7z6f2SWL8flaBk5mnLj8GqHT72iXSvTce1zxBTRFDmBYWZjFcGvS5tE39lWsV4DJUi5UD35cWAI_5dkNQyRTQGgxMNvLI4O7iWUxRqNob5NOOWk72AhcjCsxErNsF500GkPthb8_KRgAggmo41oskmyfN17Zn2nO0L16eDRTF7CLFPScPpEm__KYWpN76mdbgv-HSoG4sP9OupWAegBfJsSDwx0RkiHDVEAoFJaGPSzOm0G9s_ysWTLlT_EbVrZqyp0QN9JQb8ro1kBL-Kk-6WfAd48gE1xyew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نگرانی در اسرائیل از تکرار سناریوی اوکراین به دلیل پهپادهای حزب‌الله
🔹
تحلیلگر برجسته نظامی و امنیتی اسرائیلی با اشاره به استفاده حزب‌الله از پهپادها و تاکتیک‌های جنگ روانی، نوشت که این روش‌ها، اسرائیلی‌ها را در معرض تهدیدی شخصی قرار داده و نگرانی از وقوع حوادثی مشابه اوکراین علیه نظامیان صهیونیست وجود دارد.
🔹
آلون بن دیوید، تحلیلگر برجسته نظامی و امنیتی اسرائیل در روزنامه معاریو نوشت: اشتباه تاریخی تکرار می‌شود؛ منطقه امنیتی جدید در لبنان در حال تبدیل شدن به تله‌ای مرگبار است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/653481" target="_blank">📅 10:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653480">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rju5At4_GH2ePXtsJVxKgFyo5YXHMJw1iMcbxkFjoOI7KLm59ppB82qEXIib-q3dOeUwG23iW2nU8mH94k5Asxtsiiy9bHvbSHza8oD6_tHEq4nlFq6MW_FjFE1H7kgj-0TIyifhygKClafnEAJfe5YVLt2wCwnhrDHXLw-jp2O4xQaU6bUrKXD1f3Wca2anXKvJOyKZGUSDPXX6RTsso2OyPpRMk9OcPJe_K8vQX6OKZnUZ9zNhQZhx1S6koHEwLTDUdN1o9ToPaFVN0QSKPkAwVa_eytyOYU0PyLZUKOpz7dk8aIT3VzcPFMkEYxlhrG6fKunj93uPDxVZIA894A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا فروش مهمات به تایوان را به دلیل جنگ ایران تعلیق کرد
🔹
سرپرست نیروی دریایی آمریکا از تعلیق فروش ۱۴ میلیارد دلار سلاح و مهمات به تایوان به دلیل نیاز داخلی به آن در هرگونه جنگ احتمالی دوباره با ایران خبر داد.
🔹
هنگ کائو به سناتور میچ مک‌کانل (نماینده جمهوری‌خواه کنتاکی) گفت: «در حال حاضر ما یک وقفه [در ارسال تسلیحات] ایجاد کرده‌ایم تا مطمئن شویم مهمات مورد نیاز برای عملیات "خشم حماسی" (Epic Fury) را در اختیار داریم — که البته به مقدار فراوان داریم. ما فقط می‌خواهیم مطمئن شویم همه چیز را در دست داریم، اما پس از آن، فروش‌های نظامی خارجی در هر زمانی که دولت لازم بداند، از سر گرفته خواهد شد.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/akhbarefori/653480" target="_blank">📅 10:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653479">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pj1yJvru-zMdoA5gc6VycUVbd53bm8giTtMahhqTRSWQOvNTxQQlAqf-s92633jL8OXMyZ3UOLRRn7lXZfZO0kvBtk_cA0Ai8QTqYKy7CQrngopIU2DTbDP8L1zhkh4H0uA0s2ENN7aWeTjMD10vRdabpdish6ljNVR2Y3dO-OgWSDfh_dKu8F-fdT0UUreSI8uDBykZgAzNwtd1Oq1-1Y9Pp88KEV3qMwi7aEQPPmO4BJDe2PRAGRipaMlwG9_GdFPeaWGkngqmVqu2sxyLoHVUuNd7zejtybIft4hzW9jeWKbnWbMfEW39Z79rX3dOjoVoAJqAw5dng5yjLcvj-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کانادا و استونی در مأموریت تنگه هرمز شرکت می‌کنند
🔹
وزیران خارجه کانادا و استونی روز جمعه از مشارکت در مأموریت پشتیبانی ناتو برای آنچه که «تضمین آزادی ناوبری» در تنگه هرمز خوانده می‌شود، خبر دادند.
🔹
«آنیتا آناند» وزیر امور خارجه کانادا امروز (جمعه) گفت: «ما با ائتلاف به رهبری فرانسه و انگلیس در تنگه هرمز همکاری می‌کنیم».
🔹
همزمان، «مارگوس ساهکنا» وزیر امور خارجه استونی نیز مدعی شد: «تنگه هرمز باید بازگشایی و ناوبری دریایی ایمن شود، ما آماده‌ایم تا در هر ماموریتی مشارکت کنیم».
🔹
«ژان نوئل بارو» وزیر خارجه فرانسه نیز ادعا کرد: «استقرار نیروهای نظامی فرانسه در مدیترانه با هدف حفاظت از شهروندان و متحدان ما در کشورهای خلیج فارس است».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/akhbarefori/653479" target="_blank">📅 10:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653478">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vz3_wxefN91z9FUqYedDkrNsnXFYWykO9QUmnMsJ29DnISnVtEMamNOyblZ-hb5yO6O_dW7OaQ3hoVdnhjfw7WwcNn5ln_IQxJmlDwPH3_-a3Q9J9T2VhhrwZC8QoJa5UDtyt7FVZeMUPIt_OQPLg1tTFaHrGKmPn5rc3oFOxTbxxMjdLeeHnfqeucSXVRCf2-iK2KQjGHNuSRjqTHZfRfOMArVURj2FmVo-PromOiDQU2kPv8nr9YUuncyyw3913UiDdBX8QcKpR7zh4ZYzzPOx1uP9LkMlaf2WuI9MpWpO1jpLHJ5Gu3omo4E0V5ReJEMhhEAFoQ4-x5c8-nztvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یورش اشغالگران به کرانه باختری
🔹
منابع خبری از یورش‌های گسترده اشغالگران به کرانه باختری و استفاده از گاز اشک‌آور و بمب‌های صوتی خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/akhbarefori/653478" target="_blank">📅 10:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653477">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3KBDjCts3br5lb5QG7tXaLeVvKZeejmFoD-fXk1qtimOxlY08aOapHLNHOmXzR2BkQcWEb1YgJ3ZlmUCFPJliuoJhaK0hiaIG-9qc3LK98vXkjU8voTUsRDKngDSisdoTY9d95qp6qXv1Zj1G1RXUTyDLw4APT2A8wU5P_gWljtzfDJxgg75cdJt9HUYLCtOnhpsg17o0x9CSin3CaMinm7_z-Xqzfsowk5CF7_q7FBgBpJR0gKRnHidM_ppMKevdstiGJmJIJIz7p1DoA1XE74XN_V6IaBTNbcekd98F8MmmrLBUFE2EeaMdoKMIdRn2BF3LWaySVzM60YNfds5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجوز ناتو به آمریکا برای استفاده از پایگاه‌هایش در اروپا
🔹
دبیر کل ناتو اعلام کرد که آمریکا می‌تواند در عملیات‌های نظامی خود از پایگاه‌های این سازمان در اروپا استفاده کند.
🔹
مارک روته همچنین تاکید کرد، به عنوان یک اتحاد غربی-اروپایی، ما می‌توانیم به ایالات متحده آمریکا در تلاش‌هایش برای بازگرداندن آزادی دریانوردی در تنگه هرمز کمک کنیم.
🔹
روته افزود، چندین کشور اروپایی تمایل خود را برای مشارکت در تلاش‌ها برای بازگشایی تنگه هرمز و تضمین آزادی دریانوردی ابراز کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/653477" target="_blank">📅 10:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653476">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAFDPGtiidzQMTliND54rnEXA4w6CMqZQ9RabvDPWLjccfA3_V2OLs29rkf06_Qxc0wfYa3AXbf8Q_-qGhOUt5s7ygW2e39wY-3cWtjaXVv9chJN6ZGMm91T6ZyuENjZ0R-64QrqSpHMZ7DOaSrV6DY3xDtpyA9dVl6eEe4eE4pbI80dBIgZ7exX2DAFO9Lk_TRrtORNL7XUwPnG0mle-pHY1LC7KkMotBwEXDNfwOVLeMjHDR0QCsxqQ_mRhzpJLpA5bzVMjpoEOPjizsWfjyfRIXPv2_0olfGrduN_st_3hAe32ISW4u1tQUQLGt5TmXY9N5OQFLau8XhLagns3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران یک‌پنجم پهپادهای «ریپر» آمریکا را نابود کرد
🔹
وبگاه آمریکایی «بلومبرگ» گزارش داد که ایران از آغاز جنگ ۴۰ روزه موفق به نابودی بیش از ۲۴ فروند پهپاد آمریکایی از نوع «ام کیو-۹ ریپر» شده که خسارتی بی‌سابقه حدود یک میلیارد دلار برآورد می‌شود.
🔹
پهپادهای منهدم‌شده، حدود ۲۰ درصد از کل موجودی این نوع پرنده‌های بدون سرنشین وزارت جنگ آمریکا را تشکیل می‌دهند.
🔹
بر اساس گزارش‌های منتشر شده از کنگره آمریکا، واشنگتن مجموعاً حدود ۴۲ فروند هواگرد به ارزش تقریبی ۲.۶ میلیارد دلار(دو میلیارد و ششصد میلیون دلار) را از دست داده یا آسیب دیده است. این تعداد شامل جنگنده‌ها، هواپیماهای سوخت‌رسان، سکوهای شناسایی و همچنین هواپیماهای «ریپر» است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/653476" target="_blank">📅 09:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653474">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KFysky31xs9RrI61npi3gYDf4X3vYpaTZeiNzoYSzXVmc6GSGw36xuXPw-tjtw0bmZXQXpeqkcVNlDClshAqmmjJeiDiobroIYFCCYYLb86nUXp9rCKp0YJRGCk1mj5wVRP9aX7PiHHuw6-ZEmliuHLL3kvzG8geieRA8qF-1txQ6yW1TD94b9cxI8B_jcPqxzXrIJAIEg_GPgs58hgyZN3nqg63t6Q7ERQtjK57yQjbFfICorxJ2k5UaFl8b5ahuLslEjzcz7_W1nElbnip6Xfoznx3OYxQYC00S6m4SQan32PbzQ9Sp1nJHm64lN4Y3qFgvGGh35KC2gZPXQL53w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6tI_DUjmZMtV6oLNJP-ACe8Y4BygmpcIedXirXRKyuPzn1ijqHiT1S2jphG6ozAAty8HHsC2IIy2QyciOh6xbPHM0Iyz3Vk_vezLs2JdOKc9IdCvk8KbNtRvT55I4o0d1c1dFqf6rIzYCpbfuVkEUqBdsiDycHQMmgQS-a5l3ZHGk91BGzaYGY4al1HKHBKVxVdvQH0PB6KiV_O-ynVFWLYDMWKB0mY-DyhC7NtJDIAqBfJ0huCA6StxxK-UDycftSuzofFOAglN8F_4n5Bdc9K9MTBWfk--yT-5pWo0Xh5oYSKA3_YRTtWyyvIlxvXZW7p-xNi94KTUH2iSfkNUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جزئیات تازه‌ای از آسیب به پایگاه‌های نظامی رژیم صهیونیستی در حملات ایران
🔹
تصاویر ماهواره «Sentinel-۲» نشان داده است که پایگاه هوایی «رمات داوید» در دو نقطه مختلف آسیب دیده است.
🔹
تصاویر منتشرشده از تغییرات ناگهانی سطح زمین در نزدیکی ساختمانی در پایگاه «میشار» متعلق به یگان ۸۲۰۰ رژیم صهیونیستی در نزدیکی شهر صفد حکایت دارد.
🔹
تصاویر ماهواره‌ای خسارات واردشده به یک موضع دفاعی در داخل پایگاه هوایی «نواتیم» را نیز نشان می‌دهد.
🔹
تصاویر منتشرشده از سوی شرکت Soar از وقوع یک آتش‌سوزی گسترده در اردوگاه «شمشون» خبر می‌دهد.
🔹
نبود پوشش گیاهی متراکم در این منطقه، احتمال وقوع آتش‌سوزی طبیعی را رد می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653474" target="_blank">📅 09:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653473">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIJgx3YBwiBsFCoZPkx4X9qnvk_MibuNEVWneKMAPrkx-he4Vl6YPpvAOrBf_SPs0ViktWnIoSuR16140rIqYS9znmIkxAM9Xo-5KnWru99IqziMf2bP8utWT0P_9JDO_h_9SXAbFqnMBWVuQwix5wvg_RtmNtynjHzB59zL5e2yd2LDsoiIkSJwtah4TJ6wIkuYZE6IJN-g8HjhWVgVuHWQ2quG_TtXVC-w7bMhXw1nLCybKlWpd7IrCYoNKgyXrGhuLxVG3BVNtcrFWaRZ6LYkO3D2i0BToJoK_bVG025r7DkXnBB8Ej3Y5296vVK7nH4X_3DQkGDUL8q53tu9lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت چهار نیروی امدادرسان در حمله هوایی رژیم اشغالگر به منطقه حناویه در شهرستان شهر صور در جنوب لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653473" target="_blank">📅 08:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653472">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a2f35b9f.mp4?token=s6QG6U4LfsumI5nPfGzHVkimLn6P-NsVmjZUiciHohRQmb0bFm70DhmrZRJzOuqhwA7dAyF3D5QtlT3k8gzOeeqJh4hEiuNwFrjWw6qXLdrU6tQ3aLmYj8S4rZQxxfz4LA3n7_8Dl2UhiO0Trmzs9HtdLEJoiQa4Pk592DrtecrHO6xEck5SEhXrnPfRrfrcVMeiheAac_8HNeL0sEed6k2FboabuLcQfKkBfhH5YghFp5JCyYTO7nMUozNun5KJQcb1PDg9YHN6LOGbsDG0wg2OncF-YykOMQ5MgF1sSYuGChvjj3esccrzHIbBk50wx9E-flI_ZzrkN_Xdy_3WQhQ0Behz20YezSswBNi0cU4RT_pYbX-GnFhnIJzYNPFXEvxeEchM8sfz2TEBQvYWXdny5MdnQW3LHjXX2vK1azegjA2W2vMER1UulC9pOFAAn6FNVSl3hgU2bkwpZW8wg06F7Qrxbtrk3j7hpx7gj8f4rUiO5qA5dwsifqELlRQFwhekb6WJTt1cWp7NHMG-YEZ3OSIEqvp-xQ18mRXHF9W6THntamBNYwUX8p9D-gh4IoPquo-jZiFn3PQaDRHbidQdKyzGSpVX3NPjFn4dpsRqJQeIdQ0Rav-Q5mgT9TQpuZoqcwswPUFyPZhwugjxTn-07Y54zw_1wgtUqrMQOvs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a2f35b9f.mp4?token=s6QG6U4LfsumI5nPfGzHVkimLn6P-NsVmjZUiciHohRQmb0bFm70DhmrZRJzOuqhwA7dAyF3D5QtlT3k8gzOeeqJh4hEiuNwFrjWw6qXLdrU6tQ3aLmYj8S4rZQxxfz4LA3n7_8Dl2UhiO0Trmzs9HtdLEJoiQa4Pk592DrtecrHO6xEck5SEhXrnPfRrfrcVMeiheAac_8HNeL0sEed6k2FboabuLcQfKkBfhH5YghFp5JCyYTO7nMUozNun5KJQcb1PDg9YHN6LOGbsDG0wg2OncF-YykOMQ5MgF1sSYuGChvjj3esccrzHIbBk50wx9E-flI_ZzrkN_Xdy_3WQhQ0Behz20YezSswBNi0cU4RT_pYbX-GnFhnIJzYNPFXEvxeEchM8sfz2TEBQvYWXdny5MdnQW3LHjXX2vK1azegjA2W2vMER1UulC9pOFAAn6FNVSl3hgU2bkwpZW8wg06F7Qrxbtrk3j7hpx7gj8f4rUiO5qA5dwsifqELlRQFwhekb6WJTt1cWp7NHMG-YEZ3OSIEqvp-xQ18mRXHF9W6THntamBNYwUX8p9D-gh4IoPquo-jZiFn3PQaDRHbidQdKyzGSpVX3NPjFn4dpsRqJQeIdQ0Rav-Q5mgT9TQpuZoqcwswPUFyPZhwugjxTn-07Y54zw_1wgtUqrMQOvs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون پیشین رئیس موساد: ما به هیچ‌یک از اهدافی که داشتیم دست نیافتیم
🔹
ایگرا: حملهٔ آمریکا و اسرائیل ایرانی‌ها را به هم نزدیک کرد. اگر از من بپرسید که هدف و راهبرد این جنگ چه بود و ما چه به‌دست آوردیم، باید بگویم: آن اهداف اشتباه تعیین شدند و یا دست‌نیافتنی بودند و ما به آن اهداف دست نیافتیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/653472" target="_blank">📅 08:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653471">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
دستیار سابق اوباما: توافق پنج‌ ماده‌ای در حال شکل‌گیری، به شدت به نفع ایران است
دنیس راس دستیار سابق اوباما اعلام کرد:
🔹
در صورت صحت، توافق پنج‌ماده‌ای در حال شکل‌گیری میان آمریکا و ایران به شدت به نفع ایران است:
🔹
ایران آتش‌بس در تمام جبهه‌ها، تعهد به خودداری از حمله به زیرساخت‌ها، لغو تدریجی تحریم‌ها را به دست می‌آورد اما هیچ اشاره صریحی به برنامه هسته‌ای آن در توافق نشده است.  آنچه آمریکا به دست می‌آورد، باز بودن تنگه هرمز با مکانیسم نظارت مشترک است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/653471" target="_blank">📅 08:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653470">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/he_xJGQx15Lq40b3njbDpHTz75h8YHW4UXgDHPeTbcfxmq3kXR14T31k6J-MXzAuoVXJ_K8BCd0EkS2gOiPAkYzR_l73uZQTsdI40VPygY9NeIMUO3WlyGjTgxHkUVb6J0fet06C72ck68n3DRvIozplWpsdUaU3waCZBkRP3d5g1EbpX8MjbJRQ4hTmnZyDz9GAMaZvmFYtLqyB6LJQUGEmJwF4ZCdKocUCmZeDRZvr1wK-UoYpRcYfdb4pow1WYo7cf-WJqT4FceIccKG15M7FcauAiuHn_x14kIdbPpqIYB_2V4D_mXgOSBPyva33DwpLG7S0tB8Ttxyhy5qFng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۱ خرداد ماه
۵ ذی‌الحجه ۱۴۴۷
۲۲ می ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/653470" target="_blank">📅 07:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653469">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSwtoC5ro5OFgBuUEXhMEAEago0Xblx4XUzG2GFDmueprFJ9pGVGJc7DScvCaCank1SSI-L_gBDOQg7BxchAYgkBdlUMyVHiRL43h_y2Xo2FLNjvOc6DOwtzYcqtDjCU1m6zEOkfp-0w3qVxRA1YQLuoIjCYrLooL6OF0VDwp1yDWRLRXEQILcfwnc8uD0Re7M9QUjApnbeEjBG72qoH-36jChrsydW8KLJlzt4lAfwYs2m2Zdz6KHSblt5mXDoIvaqhfnmkzy1IC6klQMOQqwrm539_3tzLSjZFJ0eG29gh70dkld9fRr5gGWkgDGcgh75J4WD2rsvHwVFCOuXCXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهم‌ترین ابزار نفتی ترامپ، در جنگ با ایران آب رفت!
🔹
ترامپ پس از یک هفته باز هم گفت در مورد ایران عجله ندارم؛ اما آمار ذخایر نفت آمریکا از واقعیت دیگری خبر می‌دهد.
🔹
جدیدترین آمار مخازن نفتی آمریکا نشان می‌دهد که ذخایر تجاری و ذخایر راهبردی آمریکا، در هفتۀ گذشته، حدود ۱۸ میلیون بشکه کم شده که بزرگ‌ترین کاهش هفتگی در تاریخ این کشور محسوب می‌شود.
🔹
بیشتر از ۸۰ روز است، عرضۀ نفت عبوری از تنگۀ هرمز به‌خاطر حملۀ آمریکا و اسرائیل به ایران متوقف شده و ترامپ با همان ابزاری که با آن از بایدن انتقاد می‌کرد یعنی آزادسازی ذخایر راهبردی، تلاش می‌کند بازار نفت را کنترل کند اما هنوز نفت بالای ۱۰۷ دلار در هر بشکه معامله می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/653469" target="_blank">📅 06:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653468">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef66287df1.mp4?token=Hp_zkXklksrpSCGqEsSVVccjKE3EBIRPIItU44oF5gGdznUqyumLa-0-H_5H7d1azTsu1ITxelYgLn3hNADcRa3nKaRdP6szs70Stz2OadwiHi2gDYRP84OzJcCPuQFypn8LE59BirdnONi_HqbjSR0vEztWD4v2TtPZqLWI8-bR_Ed1FuJkVbIsVByRWhd5xqvEGUWYdgBIYJjE22Q7Ps5kL1xuJf-10iLokYc9cyE3CEEp2D2CHr72geQvfOr592uhwh4NxawXGlstyC1raztG1emI2aBjs1r31r-YDQ846aXU529_i3lKPvlAiLbGmMHKRpdgzNvs7YcJY0Jb7XkHWHioBUv-2mnLGvt1vpxuaie4AdclLv8LBKPFKcnCr1j4YBmkwy2MTewhLnBZ9ZQUv-SBrFWQB-zyzS8FJ0MDNyhkczbyVAO_SqGtKxW9PoqY-5xpvxBZND74Hg5lzAbdSRPeUHxIuzzNCfgu0LPAX1gJh_dTJipSsG8qtsx37T4vOloGPxaGh2A0PddIzGiNSb1AxlSnSypSntCDF_rH6qRD8Km722oH5qv2qzWxYUdvwKfB2OtRFxHobjBWd5-O6F-lGdA5v77_8mJIEY67XA0o6TvZqpqmTa5Q02P22Ai5odmocTU1h1tO0lKaQNXsLV6LIRDErgP3AHE-dDE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef66287df1.mp4?token=Hp_zkXklksrpSCGqEsSVVccjKE3EBIRPIItU44oF5gGdznUqyumLa-0-H_5H7d1azTsu1ITxelYgLn3hNADcRa3nKaRdP6szs70Stz2OadwiHi2gDYRP84OzJcCPuQFypn8LE59BirdnONi_HqbjSR0vEztWD4v2TtPZqLWI8-bR_Ed1FuJkVbIsVByRWhd5xqvEGUWYdgBIYJjE22Q7Ps5kL1xuJf-10iLokYc9cyE3CEEp2D2CHr72geQvfOr592uhwh4NxawXGlstyC1raztG1emI2aBjs1r31r-YDQ846aXU529_i3lKPvlAiLbGmMHKRpdgzNvs7YcJY0Jb7XkHWHioBUv-2mnLGvt1vpxuaie4AdclLv8LBKPFKcnCr1j4YBmkwy2MTewhLnBZ9ZQUv-SBrFWQB-zyzS8FJ0MDNyhkczbyVAO_SqGtKxW9PoqY-5xpvxBZND74Hg5lzAbdSRPeUHxIuzzNCfgu0LPAX1gJh_dTJipSsG8qtsx37T4vOloGPxaGh2A0PddIzGiNSb1AxlSnSypSntCDF_rH6qRD8Km722oH5qv2qzWxYUdvwKfB2OtRFxHobjBWd5-O6F-lGdA5v77_8mJIEY67XA0o6TvZqpqmTa5Q02P22Ai5odmocTU1h1tO0lKaQNXsLV6LIRDErgP3AHE-dDE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میلیاردها دلار در آتش؛ خسارات سنگین به نیروی هوایی آمریکا
🔹
تحلیل‌گر ارشد سیاست خارجی: سربازان آمریکایی کشته‌شده در کویت در سوله‌های بدون دفاع غافلگیر شدند.
🔹
صورت‌حساب تبعات این حملات و خسارات، اکنون مستقیماً روی میز ترامپ قرار گرفته و او برای انحراف افکار عمومی از شکست‌ها، به نمایش ساخت‌وساز در کاخ سفید روی آورده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/653468" target="_blank">📅 04:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653467">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
۱۶ عملیات موفق از سوی حزب‌الله علیه رژیم صهیونیستی
🔹
حزب‌الله لبنان در واکنش به ادامه نقض آتش‌بس، شانزده عملیات موفق علیه رژیم صهیونیستی انجام داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/653467" target="_blank">📅 03:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653466">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y04UrqdJvNV4-bRtyKOXsrA3_XJvqw8ziU2daCp-KMSAWbrXUj-CS4UBmKIytnm6TvVFsZhnvzANN1oI8zzIfUU4EifC-CpkkoFqwqPqeypDZiSi7ay-zrmOV7cOCFlxCGIWI5umeQB5eCQQeO4I6Qdet2FLcig6qPJiD8vocvsCDco5zrXPqrshfUlPc71prjbfNwLwYXqdhPcD9Zz1uDhoRoVrji9RZEhFOW0xdcSpZ1xVrnRxwdTwAAT4lpXFVmHFvLs_AHHp3BU0S4Tk3r2QKJNNWmSyGIeh51cgbJvEQKldsIcVGm93uMlIK4VtgzY8nWhDTSoPRA-Uc9ZCGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعویق رأی‌گیری درباره اختیارات جنگی ترامپ در مجلس نمایندگان
🔹
مجلس نمایندگان آمریکا روز پنجشنبه رأی‌گیری درباره قطعنامه موسوم به «اختیارات جنگی» را به تعویق انداخت.
🔹
این قطعنامه را اعضای دموکرات این مجلس با هدف محدود کردن اختیارات دونالد ترامپ در جنگ علیه ایران پیشنهاد داده‌اند.
🔹
نشریه هیل نوشته به نظر می‌رسد رهبران جمهوری‌خواه در این مجلس این رأی‌گیری را به دلیل به حد نصاب نرسیدن شمار نمایندگان حاضر خود عقب انداخته‌اند.
🔹
اگرچه اعضای جمهوری‌خواه در مجلس نمایندگان هفته گذشته توانسته بودند قطعنامه مشابهی را با اختلافی بسیار اندک رد کنند، اما روند تحولات در کنگره نشان از شکاف در بدنه حزب حاکم دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/653466" target="_blank">📅 02:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653465">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
هشدار بلومبرگ: احتمال رکود بزرگ در نتیجه بسته ماندن تنگه هرمز
🔹
بلومبرگ هشدار داد تداوم وضعیت تنگه هرمز تا ماه اوت (مردادماه)، خطر وقوع یک رکود اقتصادی ویرانگر در سطح جهان را به شدت افزایش می‌دهد؛ رکودی که ابعاد و قدرت تخریب آن می‌تواند با بحران مالی بزرگ سال ۲۰۰۸ میلادی برابری کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/653465" target="_blank">📅 02:17 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653464">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mne8BSFS9wUyGoW-Sk8sA01rieRYUhWJeeiHHqut8BiPIFGVdebwqr2pPXmyFYPCVyyysGTFRin1vaZaZzBIcqaYwGQkGhfEvAOQeWxnyh1MDVwno0VoKNeeeNB-nybsLheHafSQ0JCDddqYKEiAYmUacwS7kCvaB5TtvtEnMNbmWXw87EeHiFk-8TxNEwuyWIAmfBZrOiiLyoqWHIpi40nP1s1St3zYEHIZd-ucRk97wDbaE47sjetZh5UKchimBgctrVUY9-FlQrhbx3UvxT5mPrmRC4gUsmK9d5DnHofmAHTHJTn-6483jWyOrnUxWLu1uQIZMHYlLvnyQNR_ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصطفی نجفی، فعال رسانه‌ای در تحلیل فضای مذاکرات نوشت:
🔹
۱. مذاکرات پس از بن بست کامل و رفتن طرفین تا آستانه جنگ با اضافه شدن میانجیگران دیگر و ارائه ابتکارات جدید وارد مرحله تازه ای شده است.
🔹
۲. پیشرفتهایی حاصل شده اما اختلافات و شکافهای مهمی باقی مانده است.
🔹
۳. موضوع توافق کامل یا مرحله‌ای اورانیوم، مدت زمان تعلیق، زمان بندی رفع تحریم، دامنه کاهش تحریمها و نحوه مدیریت تنگه همچنان محل اختلاف جدی است.
🔹
۴. تاکنون هیچ متنی مورد توافق قرار نگرفته است
🔹
۵. همچنان احتمال وقوع درگیری بیشتر از توافق است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/653464" target="_blank">📅 01:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653463">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrA8gxyAJwg1ry176hPAf4Z6YaWrGAqCIIKneL0yMTLuh5hCC4-7eVFWAqIlCE-oqVtrcRZ3JXuo7ZEJ1ZdMCK1H_U9j1ILFRxz7REMwyHjTES386O87fgF5Oiv-AN5RwyYHLTEAQe4bLZa_Dp26uHJUXMhAjYI4nYtGr9T5Jnkq5tu9TB-wAvGrSShqE0ubSm4s1N-TmAbFsLjwSK0s-fiGiUzFHmEH2KXA3EnuoJl3AxUeJvJsvJrbk8Z-IMfOSBtQ6lKHMfLYrVfKIPY4v5SpeFW4xQKR6gRMuujLWmUcG-bP0_GCcrYzUgWw7GyS7JQlMNc8k2MEkhXwFlzCBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش فیگارو از تجارت مخفی اسرائیل در خلیج فارس
🔹
امارات ظاهراً دو فروند هواپیمای هشداردهنده پیشرفته از شرکتی اسرائیلی خریداری کرده
🔹
این هواپیما‌ها که مجهز به ایستگاه‌های شنود هستند، می‌توانند ارتباطات را در آب‌های سرزمینی خلیج فارس رهگیری کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/653463" target="_blank">📅 00:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653462">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
الجزیره: مذاکرات ادامه دارد/ به دو دلیل مذاکرات به ثمر نمی رسد/ افشاگری مهم واشنگتن پست درباره ارتش آمریکا/ ادعای اسوشیتدپرس درباره مرد اصلی مذاکرات
گزارش لحظه به لحظه از توافق احتمالی ایران و آمریکا را اینجا دنبال کنید
👇
khabarfoori.com/fa/tiny/news-3216870</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/653462" target="_blank">📅 00:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653461">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/368c47b54a.mp4?token=sbTFGiSZcGTJbe_f8_WlTwbMaSI-YJrl4d_n9n_gDJupIaO3DDZXt2kGARvS6OlLuAOfolEZ5gZPAs0QxEj4-v8Y6SjR2aq2PQT0Wo3FnaxmAbFG8_H102tfoPvhAAiK2UWq9yDFc6mSNhpxt7uLPe0qCDFXPw0l_3069M0m6WZLOeVdziLCeiT9h2KogLQU--7mPAL_klfUCYJ5IvxYK_9NhY7qHqiwoNqCHzAWhPz4OzG8q0lUGzDTaqu8TVivxF0kMOJ-UeCnFytlR9qK_nLBi7MjXh7RIgOtviVv59mm0D7EHbfUAS26uiPAnc_zxlegiaKSnsH5-k5jbdS-Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/368c47b54a.mp4?token=sbTFGiSZcGTJbe_f8_WlTwbMaSI-YJrl4d_n9n_gDJupIaO3DDZXt2kGARvS6OlLuAOfolEZ5gZPAs0QxEj4-v8Y6SjR2aq2PQT0Wo3FnaxmAbFG8_H102tfoPvhAAiK2UWq9yDFc6mSNhpxt7uLPe0qCDFXPw0l_3069M0m6WZLOeVdziLCeiT9h2KogLQU--7mPAL_klfUCYJ5IvxYK_9NhY7qHqiwoNqCHzAWhPz4OzG8q0lUGzDTaqu8TVivxF0kMOJ-UeCnFytlR9qK_nLBi7MjXh7RIgOtviVv59mm0D7EHbfUAS26uiPAnc_zxlegiaKSnsH5-k5jbdS-Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ارکستر سمفونیک تهران در نخستین اجرا در سال جدید در تالار وحدت، از فراسوی مرزها نواخت
🔹
این اجرا در آخرین پنجشنبه اردیبهشت میزبان علاقه‌مندان موسیقی کلاسیک جهان بود.
دراین‌باره بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3216851</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/653461" target="_blank">📅 00:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653460">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ci2jhWffkwNXjY1QsV_lrGM9UbKzjrKgb1qhS94xYZtUIUmnVZ2Tg8T8G5a36I-q7pXP7xCrMou1XSfQbk1BL6PIjXez4YSl3fcVhl-5XOl-0u7TfeLNb9Ng__2taa8gHZhZEvK3dKt0U96T9cvk1de1wkZiRLefJ-20O8YE6Em3gkg_e1mmz4XIHHtfpXo6bzcLEi1xxFCVJOgjvztsrxqZ7y44ZWLXPDZO-Xc7vHKxvvwXIa1-96wBKbtDtRUSj9fN2Q92q2YcsnI1LMWcAO3-Ymt6SfYXkExQS8-WRPgQYzIgCpRxOy60mi4a_scxdATQw3PvZyCMxzHQH6lF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: ایالات متحده ۵۰۰۰ نیروی اضافی به لهستان اعزام خواهد کرد
🔹
رئیس جمهور آمریکا: بر اساس انتخاب موفقیت‌آمیز رئیس‌جمهور فعلی لهستان، کارول ناوروسکی، که من افتخار داشتم از او حمایت کنم، و رابطه ما با او، خوشحالم اعلام کنم که ایالات متحده ۵۰۰۰ نیروی اضافی به لهستان اعزام خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/653460" target="_blank">📅 00:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653459">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
رویترز: هنوز هیچ توافقی حاصل نشده، اما اختلافات کمتر شده است
🔹
برنامه غنی‌سازی اورانیوم ایران و کنترل آن بر تنگه هرمز همچنان از نکات کلیدی مورد اختلاف است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/653459" target="_blank">📅 00:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653458">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔹
داغ‌ترین خبرهای امروز خبرفوری را از دست ندهید
🔹
🔹
ایران و آمریکا احتمالا بر روی این متن توافق می‌کنند + جزئیات پیش‌نویس ۹ ماده‌ای
👇
khabarfoori.com/fa/tiny/news-3216834
🔹
ابراز آمادگی احمدی‌نژاد برای مذاکره با ترامپ مقابل دوربین‌ها + ویدئو
👇
khabarfoori.com/fa/tiny/news-3216840
🔹
ماجرای دستور مهم رهبر انقلاب درباره اورانیوم ‌۶۰ درصدی چیست؟
👇
khabarfoori.com/fa/tiny/news-3216695
🔹
شوکِ ۱۰۰ درصدی به بازار لبنیات | صبحانه هم لاکچری شد!
👇
khabarfoori.com/fa/tiny/news-3216783
🔹
چگونه با وجود جنگ، تجارت جنسی در هتل‌های دبی رونق دارد؟
👇
khabarfoori.com/fa/tiny/news-3216745
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/653458" target="_blank">📅 00:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653457">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
العربیه خبر منتشره از قول این رسانه درمورد جزئیات پیش‌نویس توافق ایران و آمریکا را تکذیب کرد
🔹
این رسانه پیش از این مدعی شده بود که به پیش‌نویس نهایی توافق ایالات متحده و ایران با میانجی‌گری پاکستان دست یافته است
🔹
در خبر پیشین العربیه مدعی شده بود لغو تدریجی تحریم‌ها در مقابل پایبندی ایران به مفاد توافق، آغاز مذاکرات در مورد موضوعات حل نشده طی ۷ روز و تضمین آزادی دریانوردی بخشی از پیش‌نویس توافق است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/653457" target="_blank">📅 23:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653456">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213f1db8ef.mp4?token=jKflWQQPvvP4RLl2ehVIN1HmOQFklb0vIcdbYcRs9LtPkuz2b0a1FVWlbNbVSmq0_3BSAiKy0XS_qdQgBODwU5Tl1w7EHo6faOnp4XK-kwJnxcac3yKLPq3DV289ze_2KR7x01g53P6SopTf-9pd3M2KZH89Reqf2BJNYEnwn_adWZb-7dGVDl4_WXuqc1-m92Fy6tTiErRjV-RGtlQr9p7ReFccCW4X9qMbBUeBx9Bn0uOscI_GP_KhS2B4hkqncGYifn1qgHTd3cfNAOZKX7ffSgklWWDgwBnR_sf59NoCClWdZKPI2fTf85MC04wDpgXsAoCUYiNeC_WlZObzGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213f1db8ef.mp4?token=jKflWQQPvvP4RLl2ehVIN1HmOQFklb0vIcdbYcRs9LtPkuz2b0a1FVWlbNbVSmq0_3BSAiKy0XS_qdQgBODwU5Tl1w7EHo6faOnp4XK-kwJnxcac3yKLPq3DV289ze_2KR7x01g53P6SopTf-9pd3M2KZH89Reqf2BJNYEnwn_adWZb-7dGVDl4_WXuqc1-m92Fy6tTiErRjV-RGtlQr9p7ReFccCW4X9qMbBUeBx9Bn0uOscI_GP_KhS2B4hkqncGYifn1qgHTd3cfNAOZKX7ffSgklWWDgwBnR_sf59NoCClWdZKPI2fTf85MC04wDpgXsAoCUYiNeC_WlZObzGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخبر: اروپایی‌ها چپ و راست برای عبور از تنگه هرمز به ما پیام می‌دهند
🔹
تنگه هرمز سرزمین ماست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/653456" target="_blank">📅 23:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653455">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3db5c1fc5a.mp4?token=N1-uEWNLVe_QLCDg_smiAPnrzqG14Ov5g6lLrtv5psVCOwC6fA0NtcTn7epci_OzVj-GDgfdpMEz5uzrhEPdLsZn3XCBRXRFHPWMUFmvFIH3oa52H7PK_r5uWWdFZyOXr6pScYihOHy02EtOt2iHKsop1850y7T6LzTkYOHWvY2UBdLoCtryItrxNO7QSF-xZDzK4xhrcmtvekHR86QIMK73LRPPSwJ8PQfN8J0n0O2vh0AiOcENUGCiUHilchTBx6_rq7uE6WYkypkcmXXI_28n_JHEMZG-83agy8W371l5Fp8Kh07gaGO1Si6yBeoU26ME_p0GEmDIzo3uJoJaFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3db5c1fc5a.mp4?token=N1-uEWNLVe_QLCDg_smiAPnrzqG14Ov5g6lLrtv5psVCOwC6fA0NtcTn7epci_OzVj-GDgfdpMEz5uzrhEPdLsZn3XCBRXRFHPWMUFmvFIH3oa52H7PK_r5uWWdFZyOXr6pScYihOHy02EtOt2iHKsop1850y7T6LzTkYOHWvY2UBdLoCtryItrxNO7QSF-xZDzK4xhrcmtvekHR86QIMK73LRPPSwJ8PQfN8J0n0O2vh0AiOcENUGCiUHilchTBx6_rq7uE6WYkypkcmXXI_28n_JHEMZG-83agy8W371l5Fp8Kh07gaGO1Si6yBeoU26ME_p0GEmDIzo3uJoJaFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخبر: مردم تا خون بهای رهبری و‌ شهدای جنگ رمضان را نگیرند، دشمن را رها نمی کنند
🔹
مشاور و دستیار رهبر انقلاب: ویژگی‌های رهبر سوم انقلاب منحصر به فرد است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/653455" target="_blank">📅 23:38 · 31 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
