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
<img src="https://cdn4.telesco.pe/file/VAwxHeuMcfOYwO5FawhPWJ7MBR-AUhXN4O5UtwjA4BcyjoEbeLCa9Sy0bI8x88eMDohopdK0jYLx1eHL0Svnh2qTO7-lw-M8hzwHWLDnfO9Iz8Kh4VfAV3xjzufosKEcP7qD7gzdwiL6ZmfL5efg2q-z6SE4JsUYXA6-U7CBfBZJhlVuBUkeZFiuAEs9gYGuDvUHahJZMgx0s0a8vEnobYfsjbtQaP5q1aoa3J0hItAY4muLglAf9TiwUJIzqZsMyu50jxVs7gf_yMwsl98Qlcj5oiiC654AoVA0Itvhh0fLPxJoXuXur1AjnfBOiqAuvoacfu_Cwx0IPRGsffzAdA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 17:45:14</div>
<hr>

<div class="tg-post" id="msg-461566">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‌ هلاکت ۴ نفر از تروریست‌های وطن‌فروش در سراوان
🔹
قرارگاه قدس نیروی زمینی سپاه: درپی انهدام یک تیم تروریستی حرفه‌ای که قصد اجرای عملیات ترور در سراوان را داشت، ۴ نفر از این تروریست‌ها به‌هلاکت رسیدند.
🔹
همچنین تعدادی سلاح و مقادیری مهمات و مواد انفجاری از…</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/farsna/461566" target="_blank">📅 17:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461565">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCfrvmdZgku0nerZd5jVEicEhrWB1H7Yjgb9RyLZdgjHwtPbpzJeQlmEOi7slwWE0qstDWXepeSLqDzFXJ-gFKQtK6NwGMZy0h11ZprAggOp1dRaVdTWXcXWkmtvgRxC07q2uHXlh8DGBrzWW6Xv3FhLKgoJNZeEmcdNxoU8usZe9av8vam79xdY8mhm23iHAjm3HnvCDqVlyVIMgoweWFHZbE6rQLuPZH62ZUz0mRRFt2wKcDTkNZwxV75VUaQZME5CgHvjBhSy6DJvJgXq8JXkyJ4x07QjTqwbsAt1R_1uCqVKXqSXJlxPbYkjbeyNg1vQf9Tx6O6M2c-VCvUFGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندر دیر آمادۀ ورود نخستین محموله خودرو از قطر
🔹
رئیس اداره بندر و دریانوردی دیر: بسترهای لازم برای ورود نخستین محموله خودرو از قطر فراهم شده و خودروها پس از ورود، تشریفات ترخیص قطعی یا ترانزیت را طی خواهند کرد.
🔹
همزمان، صادرات بندر دیر به بندر الرویس قطر پس از وقفه‌ای چندماهه دوباره به‌صورت منظم و روزانه از سر گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/461565" target="_blank">📅 16:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461564">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🖼
سخنگوی سپاه: پیروزی‌های انصارالله در ساحل غربی، روایتی از یک پیروزی الهی و ثمرهٔ سال‌ها ایستادگی در سخت‌ترین میدان‌هاست.  @Farsna</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/461564" target="_blank">📅 16:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461563">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">شایعه توقف پروازها به عراق رد شد
🔹
سازمان هواپیمایی:  تمامی پروازهای کشور به مقاصد نجف و بغداد مطابق برنامه در حال انجام است.
🔸
پیشتر شایعاتی مبنی بر توقف پروازهای ایران به فرودگاه‌های عراق منتشر شده بود که سازمان هواپیمایی می‌گوید فرودگاه بصره، یک فرودگاه نظامی است و به دلایل مسائل داخلی عراق بسته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/461563" target="_blank">📅 16:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461562">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpdXG2Egyy1W2YTWpw5bI_h_fAvdqqvvLkefjcz84j6OHJAbjxk_0mj8BEbBSZIRYPM3q3hPLCCYjzmUmBv9DWemSiG6v9I5FpqfZxO1Yx7l_4Qi73cyi_wWRUWaHXprb81P6qc3FFO9102ysIvxP74q0fIrpd6la_uj5XlxUP_83ScXdEb2ysmhuaGlMn_ES9NjunnrY6aAJyLLcXeYma4-0ItLVdkLemeiYyA75yKOvJfuyFsujAsDcAvt3hiie2LlsID3VlLgJ4OFJz-BbTERzrGWWDNUkui2ASKNrr7HLn37MbTOTZgB4lL1QB2u5snHcruegQxrdn5dDYIAyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متکی: ترامپ تنها ۵۳ روز فرصت دارد؛ نباید با صحبت در مورد گفت‌وگو و مذاکره به او پاس گل بدهیم
🔹
منوچهر متکی در صفحۀ خود در فارس تعاملی نوشت: هم‌اکنون در حساس‌ترین بازۀ زمانی جنگ ترکیبی آمریکا و رژیم صهیونیستی علیه کشورمان قرار داریم.
🔹
ترامپ در شرایطی که با استیصال در جنگ نظامی، نگرانی از شکسته‌شدن محاصرۀ دریایی و ناامیدی از کارآمدی تحریم‌های اقتصادی روبه‌روست، تنها ۵۳ روز فرصت دارد تا فضای سیاسی آمریکا و نظرسنجی‌های مربوط به انتخابات کنگره را به نفع جمهوری‌خواهان تغییر دهد.
🔹
ترامپ با تلاش برای پایین‌نگه‌داشتن قیمت نفت و القای درجریان‌بودن مذاکره با ایران، درحال مدیریت افکار عمومی و نخبگان آمریکایی برای پیروزی در انتخابات کنگره در ۱۲ آبان است.
🔹
پیروزی متجاوزان در انتخابات آمریکا می‌تواند به معنای ورود به جنگی تمام‌عیار دیگر علیه کشورمان باشد، اگرچه نتیجه‌ای بهتر از دو جنگ قبلی نصیبشان نخواهد شد.
از آقایان قالیباف و عراقچی درخواست می‌کنم:
🔸
در ۵۳ روز پیشِ‌رو، به‌هیچ‌وجه از تعبیر «مذاکره» در سخنرانی‌ها و مصاحبه‌های خود استفاده نکنند.
🔸
هیچ گفت‌وگو و ملاقاتی با واسطه‌های رسمی (پاکستان ، قطر ،عمان) یا واسطه‌های غیررسمی دربارۀ جنگ و انتقال پیام به دولت آمریکا انجام نشود.
🔸
برگزاری نشست با کشورهای جنوبی خلیج‌فارس، به‌ویژه دربارۀ نظم منطقه‌ای، به پس از این بازۀ زمانی موکول شود؛ چراکه نتیجۀ جنگ، نظم آیندۀ منطقه را مشخص خواهد کرد.
🔹
ترامپ با اعلام منتفی‌شدن تفاهم‌نامه‌ای که خود امضا کرده بود، بهانۀ لازم را برای چنین تصمیمی فراهم کرده است. مراقب باشیم برخی به ترامپ پاس گل ندهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/461562" target="_blank">📅 16:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461560">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hupfm0BEykoAPyOLHWv_Wa1_2M-0TBnawA6aHqHfkmYibY-zTw6ypiIybzGg33WfWURUylOSZVuSMBgm759mXm1mCQuvL5xUN7SuBSoAsZPXMGDgpw-SBgbpWlUF0kswGLH3g4xPLOAMYXzTZpnCLG2kBgxaUQOYOAHsKD69PLXN-4uytV-Zj102Xy8vOqWegYlW-4MJkEwUUNSIW56X2jU7hxV6lMmljK8izyGlqNPB8cE1OZN1yFNa6vza2mAF_l9OxmPmD56Y6sjju8nJu34Dfx6KUs8un-GLbqsZ8SHRLi6BCU5y9eVFqZ7x4Zh5NMXXhw8KJuUecBnKLtcYNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hh4OOZJoBqBvq4RdRdtPPyhVS1dx1p5Yn-eqvrusNFV94G3OU3Qxhgt7pM-69zGAZqP6ZBPXiFsOLu9YPkFvoX5ugDdgKrYL7zsOBAFcw4q432MhDsn-oRVr6p5c96bcjcgin-oXhkLTXtYkIstlzPqTMfAWqM7udaKvoxR-glw5_zogOi-bMb7GobWeq1pqQePDy9XUNdv-giSnIJoGHqgbcybB_2AGKeN6TaV5tiHP6NNpk1iJnJyZ3K3Qb7voglI4GsK9HhhGhCSnRkjW6nerytdU7JwUlpviny9V_zVh5HQw6PvIYvHVmjypiywrxawREFn3bvvaJPpYKvUeaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گفت‌وگوی سرپایی عراقچی با همتای چینی در حاشیهٔ نشست بریکس در هند  @Farsna</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/461560" target="_blank">📅 16:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461559">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jj8DpQKMAf55PjJXZMBSBu3dlW2eizbzGO6eKesZPEicINHFGnDvlECDWwQ6BNPViJ0LilROH-K9ykwC0WOKuf8bcRYp1IwEMktkXHXSMTpXN2twaxzVERG8FJn0aYEGZonszvfDmanHeJRQue5TUTgswlUxRQDidvK9xn31QxXoFqQn9JNbY0C2MZaceNIKBFTcx8crogMkVr2KcZ3GyZDw0oqnno9eC960j4rGeZ_-t83AodQhFxa_fqjkxXJc89p7Zjj1Go30a2susevVXpuioH7paVn6MmfNBLzf4VWeNlBYC6gaF8A0ecighOPpbBk0cFJ4fYJoOwKI_jMQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترافیک سنگین ایستایی در جاده‌های شمال
🔹
پلیس راه استان مازندران: درحال حاضر ترافیک در محورهای هراز، کندوان، سوادکوه و بزرگراه‌های استان در مسیر رفت و برگشت به‌صورت پرحجم گزارش شده است.
🔹
در خروجی شهر مرزن‌آباد محور کندوان ترافیک ۷ کیلومتری ایستایی رخ داده و از حوالی ساعت ۲۰ تا ۲۱ مسیر شمال به جنوب محور کندوان محدودیت یک‌طرفه اجرا خواهد شد.
🔹
ساعت ۱۶ مسیر جنوب به شمال در آزادراه منطقه یک البرز به مازندران و پل‌زنگوله انسداد انجام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/461559" target="_blank">📅 16:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461558">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/El53ks8LEPcw4MhOpkQvHy6d8W2EjM37lA48eSzRLl82CCb-b2lNQgVFQ3G8RnVS8onqojIqx_3yKPs2ZbDZOMXkr0iHK1WCf3BAF8BAMQ4ugT2AzA2Q7EPGuTigLFYY1GyfihS3ugi_iPMYKn4s23Ur_liPfnWtaX2Jc1m_CDFCZdiJhONKTBRhD74JMSSKBqibKyClfoEMuaYe4FNdVJyd64llasw2cgHWEkMhFtKru978o0XctKVVD9CmsjOiocjviLRmdp39IjGp4Lw0p33MFl-NXoCOe0ovDFpckKdzWaelxtWghMPWpHYik8lOU9FGBseMdHuLa5Zdavnm7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهم هزار پروژه‌ای همراه اول از بزرگ‌ترین افتتاح ارتباطی کشور
🔹
۷ هزار و ۹۴۷ پروژه ارتباطی در سراسر کشور با حضور رئیس‌جمهوری افتتاح شد که یک‌هزار و ۵۰ پروژه آن به همراه اول اختصاص داشت. این پروژه‌ها با هدف گسترش پوشش، افزایش سرعت و ظرفیت و تقویت پایداری شبکه اجرا شده‌اند.
🔹
راه‌اندازی ۸۳ سایت جدید ارتباطی و توسعه شبکه 5G و ظرفیت LTE در ۲۲ استان، به معنای تماس‌های پایدارتر، اینترنت سریع‌تر و دسترسی مطمئن‌تر مردم به آموزش مجازی، خدمات بانکی، سلامت دیجیتال، کسب‌وکارهای اینترنتی و دیگر خدمات آنلاین است.
🔹
افزایش ظرفیت شبکه، توسعه زیرساخت‌های انتقال و توزیع محتوا و ایجاد شبکه مدیریت بحران تهران نیز تاب‌آوری ارتباطات را در زمان افزایش مصرف یا وقوع بحران تقویت می‌کند.
🔹
همراه اول با اجرای این پروژه‌ها، توسعه ارتباطات پایدار را در نقاط مختلف کشور دنبال می‌کند، ارتباطی که امروز نقشی اساسی در زندگی روزمره، اشتغال، آموزش، اقتصاد و امنیت مردم دارد.
@mcinews</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/461558" target="_blank">📅 16:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461556">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IcAM2vBJ-l--xq7opzkSrOs9bRs2RC9ocoLFYPtNwW_11mYqFxsAvAmBPPGfpiHYSg5wNuI3c7ulKb0mu8I2L7dNP95W3RrBEP8_GbeCwWtU0lyjxG9lrNfp-Ucd5ON3aEKasUWlcK7kajNZpmXnifzD92JCWoqYhjJShlJupxPBzu09bDS83VwOxWTgLd4HNtlk1TdIwmK671hTXbvShmWJQDBJmsqtiwTQ-qJJVAbS2RDOv5VkJ_TIF3TzjGKGq99AaZqHHxxc-uniZ9IPwofxO8D0EFDe_fnmzibK0mm8JrcI2RYdfMDRX-SuyFD3_vWUIVj2CFfT1AaPvHL9Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iG_Plgbm53MJzfb1Xh2m4MNLWRYISQu6bUJQD4CoVYn-LscUwSLocsvV_C7DDTcCq1yCql_0OXOpK_37wGGjXcIgXykViDZelgNYR5WuWH52mQ4bbG51M3Uu0oqhAcPNkeGdd6rQ3FGQ2asuwBE3n_AFGKGcnhx-7uwHhQq3EZx_dJLVKsMfNriMjO4HszhSzz6EomK8VHbPwcDAK0xJGMA_DHJig436FklHEdYvcFHuaTQmLk5ON_UJitcS9j7SgIp3ZrQPQKjn1Ji5t9u6j0Lnt8FdHGANz353gIx5RTpCz7838zeTsLbXTa_0_xrtLCBFGr1AZ97bx246cAEdag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
نصب تجهیزات فرآیندی و سازه ۱۱۰تنی در ارتفاع ۷۰متری؛
🔰
پیشرفت فاز۳ تغلیظ مس سونگون به ۷۰درصد رسید
🔻
پروژه فاز۳ تغلیظ مجتمع مس سونگون با پیشرفت ۷۰درصدی، وارد مرحله مهمی از عملیات نصب تجهیزات و سازه‌های فرآیندی شده است؛ در این مرحله، مکانیزم‌های فلوتاسیون نصب شده و سازه ۱۱۰تنی پل گالری و بریج شماره۴ نیز در ارتفاع ۷۰متری با موفقیت جانمایی شده است.
🔹
عملیات نصب تجهیزات فرآیندی پروژه فاز۳ تغلیظ مس سونگون در حال پیشرفت است و تاکنون مکانیزم‌های مربوط به ۹ دستگاه تانک ۱۶۰ مترمکعبی Cleaner & Scavenger نصب شده است. براساس برنامه تأمین تجهیزات، ۲۰ دستگاه مکانیزم مربوط به تانک‌های رافر با ظرفیت ۳۰۰ مترمکعب و پنج دستگاه مکانیزم تانک‌های Recleaner با ظرفیت ۵۰ مترمکعب نیز در ادامه وارد مرحله نصب خواهند شد.
ادامه خبر در مس‌پرس:
https://mespress.ir/x6Tn
@mespress_ir</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/461556" target="_blank">📅 16:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461555">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/farsna/461555" target="_blank">📅 16:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461552">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WnOQ023jacLmquLBTDsObC6PgTrwqocIsApuKMNwG-nsMGi6iDUSEVUavm-Byc260177WT28DZnSwuuaChSY0k-IJQE9wXZcK4-IqjEcsibRrX5KNtzCCryZgGwi99etFgo-CZL6sKEP9OXubXWFLH79rlo3RYE5_h5etmcvFegq48cap0Ru8X2oshxobcoOawD2K0qvwDmf_iJ9UCO0eNd7Le_jUo91HecHX2tZ8MATApHYwZdxvfP3Di8Fxv4aVE9wTwGk5oWW_CyQSq72Cmi71fY5xldJzqZKgukK0dsgOhKejUHEbuwDfFUmvVtXnTpzR-7e0HzjNMX59gUzeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fj9LrGibFq0Mk1K8cKQm9WYNpoHEgTUg9nsZEDnvAqLg9-bWvv8K18Uze6yGs8euVHYoPav32ifdXDG-1fxXjOoRgFG-7yTl21h__KlJypYUj6NPQtc-OPNVHFroLl2MJDCBjaY0sb3jhymjdAodWsVOZylHyln2TeAtx0MgiL3_NAYKdITffOnDoEX61uD2KjtVcvEA2oSO3VEpnB3mG9ZQD7Dd8P4ooop4ThQ0wrteiwBVB51Ll-yxI2BUWpKmN2OQcYzU2gbNpO8fffZ9yXU6KLtFZPknFvMjr_-y0P4LuqqJrmeqQjrtbWWijHZ2dN5h_8oCNWYyLmIB3T2Cvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lyP1tFMt9w67ZSyrtHNQmHUP_87ddIjzhz80zezMU8Y_9PQHofLEdQxuq9yyuX6wyQZ7Jqbu8u4HkPMv6MgD_jrP0yZihEgeadUuw-V3QH2s_SZNBhRIEKbabTsHfQUzTnpLv-DcBCg0RbD9PNToy1XHBXqdlGGdlc25EmL5wK4wUfYjHBsVVfF50VuDe-ryPpOefp3O61d8CcoWWU_tGTsXj-BvYDfvBIOj2raXLjZmpB7AmYAVkuZRHbEBggnYfImCSxdwJnt7EwPxuc7uehaIvDgdYvnaEHRwKMuegyEIfbBJGJ0LQz6DGe6vENOJ0jAQ-kbUMvD4ueeSH4hkuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پزشکیان با خالد بن محمد بن زاید آل نهیان، ولیعهد امارات دیدار کرد.  @Farsna</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/461552" target="_blank">📅 16:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461551">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpqE-7akiv5V4Vt7lT6mXAVdl1KaSQilY5mdOoRmmTsadutz409nIKI23idfe5CTP9JjerCJhnsiXlKIYcq3bCQp1pVVnQzSThvTkmR2lhhizOw3ZmkRd1B-zfWz2WM84Wpg9f3wpiE9aI_R2J9U98aSKaB1KRsf4IvukLW7lfpLgoG_GL3xKzhVC_e9m3Kv0uEKYmOcfy6cW8LsXuPtFOBc1Vafb36MSBEM0bvtVVFyGvTbPrUD79GmZCxH3azPClo1LM7fIO5CJfkrnmXGDk37Adn3o3Iyd2KoqQCM0cIGyiDmNQUjtpU-b8K3007hgD2_W8Nq70cGjiZSloJREg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت اطلاعاتی آمریکا از عربستان در یمن
🔹
شبکۀ ای‌بی‌سی نیوز گزارش داد، دولت ترامپ در حال ارائۀ حمایت‌های قابل‌توجه اطلاعاتی و کمک در زمینۀ شناسایی و تعیین اهداف نظامی به عربستان سعودی است؛ اما فعلاً برنامه‌ای برای انجام حملات مستقیم علیه نیروهای انصارالله…</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/461551" target="_blank">📅 15:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461550">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38b2b245b.mp4?token=UocOr_GonLcZ4L7rWe-Kr_BvPTaF3KAyzHHrw-IAgZbi7nR_UEa7ZlfP_qb5lywRHH_cQD_K4dg0LbfN1G2KmhMvZ4JAtoXqv_gVS9MnK4t6aY9wtRPDKPMLgDCPLnsFYTnhOliHLDnj5ww_pKkUrCQPvJtIFDpH2T15BqW33S6ESUr11uExLcJlVpZ_L-dwSYxP1K5Spw_gEfOp60kQucmceLPZT8H5Z3xqrcLbm8GUPW1S-fC7F58BgpDto9lw3q-T1e56HK89YMuji5X1Zq7PtjUpcV07OQ-k4CZDIM-l5O4HbmLFQ6xAaSBDuj2xuy3ZEUAZT7KZCZqnEIn9dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38b2b245b.mp4?token=UocOr_GonLcZ4L7rWe-Kr_BvPTaF3KAyzHHrw-IAgZbi7nR_UEa7ZlfP_qb5lywRHH_cQD_K4dg0LbfN1G2KmhMvZ4JAtoXqv_gVS9MnK4t6aY9wtRPDKPMLgDCPLnsFYTnhOliHLDnj5ww_pKkUrCQPvJtIFDpH2T15BqW33S6ESUr11uExLcJlVpZ_L-dwSYxP1K5Spw_gEfOp60kQucmceLPZT8H5Z3xqrcLbm8GUPW1S-fC7F58BgpDto9lw3q-T1e56HK89YMuji5X1Zq7PtjUpcV07OQ-k4CZDIM-l5O4HbmLFQ6xAaSBDuj2xuy3ZEUAZT7KZCZqnEIn9dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرمربی و بازیکن خارجی که به استقلال نیامدند اما پول را می‌گیرند تاجرنیا: با کاریله و استراندبرگ تفاهم می‌کنیم  سرپرست مدیرعاملی استقلال:
🎙
کاریله از ما شکایت کرده. درخواست مالی او از ما زیاد نیست. می‌خواهیم با نصف مبلغی که می‌خواهد توافق کنیم. با استراندبرگ،…</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/461550" target="_blank">📅 15:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461549">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6db67df5f5.mp4?token=CrApSV1xgjgx5W0ZJesbRvdY_uubARUe0X28AxXkOiUGDVglifDibNi4WwxfyiV2BWfSfveDYCPFlYREYfBodisCYCopNOTOQD6hRdJ6PVHJwAKXnanMcpuxJhY-rsfk2SPzWX2maXt4azF4EgiDnMLn4cR6cFmXnEBe29Ln2xWLnlNVSO3yEJgVS0KpfiPQ_47LsV13KpDXGk2UOWnGKA2kQlQpYx4-cmbos2z6c6hcgIHPbFXrBJ3SlC6oJSGOaoY1K9Gn3viVcmc5_mCkg846tPnNj-KVv0ogIjvgqAZDrpFVIv-mi2dM4ufCGYZB5RPXPigetQWNAU3QYWpK_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6db67df5f5.mp4?token=CrApSV1xgjgx5W0ZJesbRvdY_uubARUe0X28AxXkOiUGDVglifDibNi4WwxfyiV2BWfSfveDYCPFlYREYfBodisCYCopNOTOQD6hRdJ6PVHJwAKXnanMcpuxJhY-rsfk2SPzWX2maXt4azF4EgiDnMLn4cR6cFmXnEBe29Ln2xWLnlNVSO3yEJgVS0KpfiPQ_47LsV13KpDXGk2UOWnGKA2kQlQpYx4-cmbos2z6c6hcgIHPbFXrBJ3SlC6oJSGOaoY1K9Gn3viVcmc5_mCkg846tPnNj-KVv0ogIjvgqAZDrpFVIv-mi2dM4ufCGYZB5RPXPigetQWNAU3QYWpK_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: در قضیهٔ تراستی‌ها و رفع تعهدات ارزیِ آن‌ها، پیگیری‌ها باید منظم و مستمر باشد
🔹
به‌هیچ‌وجه قابل‌قبول نیست که یک تراستی در ماه نخست ۱۰۰ میلیون یورو عدم رفع تعهد ارزی داشته باشد و عدم رفع تعهدات همین تراستی در ماه بعد ۱۵۰ میلیون یورو شود. از سوی دیگر،…</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/461549" target="_blank">📅 15:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461548">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3-d-uEZOnL1FTz95kLlzhJauRVcf24b8RrLWEDyIO-4DPmq5MuLDzbftV9k6WGeFpEYq5eaWoATX1XvAOPNKySsS5a2L5TpOK6TDJKU6OB69iTkzKYxhB4pxGWt_MrLrBlnOwnwTGuw8US-3EkG3oSkSvjR5Bv395uUu95axBtNqtUYB9uXbni17VMEIhg0Z4hfm-SE2rSPBQ7sHnt0sHzoFBAEc93mVzs0Nc0auYyG7V-9z-c0bMBwC-yTVPgkK0zQsF289o_1yBW6yIU_Vos1XbyNJdvpzkyyDgrMLMQz1rRXk6-AGUkHtUZHuSlUkFHCFbB3cnBsGgOQ-dnYDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکایت بنیاد آیت‌الله رئیسی از ادعاهای کذب یک بلاگر اقتصادی
🔹
بنیاد شهید آیت‌الله رئیسی از یک بلاگر اقتصادی به‌دلیل طرح ادعاهای کذب دربارهٔ رئیس‌جمهور شهید شکایت کرد.
🔹
این بلاگر مدعی شده بود در دولت شهید رئیسی از او خواسته شده مباحث اقتصادی را به رئیس‌جمهور…</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/461548" target="_blank">📅 15:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461545">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ic2N0EY1lTLk3XmORRCFfYvzEFNTU7dKLU0sSpuxFunUilKQHyt1itQVdA7TExURlOfHY5boKYQEDqU8kP9zbkTejXkM2axu77vPRCw4XgbxflIFhkiOZw6G_Bxzd1ojBuTk-GxjRsqPP6-1ADuYMCDEPZyQsAMnx2yE-5hKXaRZ-Efxtl2v1pDDdHuwVZiqUYVt7xZBQHOG5LElUp_gcq7z8fPQ2v6bYaClAJGWRvcQbBnzAPTaHVNmca78QgM0PNmY2QBQyXc_aT7qUwSdWVQFOC_7HZUwSpGySFksxv8sUArs-ma255RY3FZn4Fj0f6UFcATC33Tz19anDKStSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qdde5ZSa-KKkTqtjU5Fnufdr0rUYTHodv-veE6vHNZlZbwkjLGfQq6taw5IGKyky3im3wnaBcnKWrggp9boa2vyThGkVN0hILJb-QPNZ8rlZOGjAQadSQZrKYtIFujSEJuUHHoE0fyoAbuuIYKKLV6qO5sD5QtH9ND1PvmNNT2L5utms-jiaIiGhJkUn2jnALSxkQalYZY5q8p0x1jvDngEM_T7EoIG5-KokJIkfE-tHqNhwvSicN51V-sD6z_eKy3ELV_E7JyOjh88DIqVHHdYAqAqNT5Y8Si6pLMiWZ61UJkskU7B5Y3gWlVX-m42_XD6CTzPQc-uCle4NFn46jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h57LwVLFaEn0uMFOKUv9nAAycnWWdGtzGlvo0jAQLP3MI0ac1zOvwv_ZpNJVN7xlP2W748c6LkJK4CwGPNUJ-qq4f2_xVDQpVjgSxw-Azj4W861-n8-0g3tFLVOrQUb6WYydyBnYpfBzuQ0nSNBDkwuDzggfDgslitBrevn8we_Ewq6U_s_SUcvNXPI4I5rbF-RRL8HoleMgZwMY5GVKw3qCBYrqN_NUfJS3mHPVnrm_ZDpwAOfqeDmA3b0cmcxP2rEuct5eDTa9h5GA_DIr3O9_g0sTVDYXBSz7rr94HOibpQGndOi2m5uYiSABaiBig2aqKmBvm-qi8UE8kYIpUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گفت‌وگوی سرپایی عراقچی با همتای چینی در حاشیهٔ نشست بریکس در هند
@Farsna</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/461545" target="_blank">📅 15:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461544">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اجتماعی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-DPjZFGQTSpy6ddeyYr7yo621UXw3nFZ5VYxxrcI2dR15PKZUTPOM0UafORb7_zxPo0lcjyCQdOt26nMUdOM97VqtUbzCosZIerkDNFiCl1TCfOhix212U5AUvlv1VlfZXMA1BmnzggWFnLKeijcTjVJA4-FiehDn6qSF9abhuqDco2g1dDmEtGj-iL1a4pKaMIgsUSv-LbN9rqAM-k3C79VsNjJ_9wpqfaEAvrpna84HokHN42OEMlykicQg2KODYYVcKlCJVcU_rMkBl1D80hKWVgRfRuJLGCg2j255HMLlUx9JvH__0qjCmZDoWVGEQ4DY5EItCp7yg2NPVe4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال سیلاب، صاعقه و وزش باد شدید در ۸ استان کشور
🔹
سازمان مدیریت بحران از احتمال رگبار شدید، صاعقه، سیلاب و وزش باد شدید در آذربایجان‌شرقی، زنجان، قزوین، تهران، البرز، مازندران، گیلان و اردبیل در روزهای شنبه و یکشنبه خبر داد.
🔹
از تردد و توقف در حاشیهٔ رودخانه‌ها و مسیل‌ها خودداری کنید.
@Farssocial
-
Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/461544" target="_blank">📅 15:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461543">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fad3da36c.mp4?token=eAg8QFomTHlEapFr1wPJG152uH3cyYR6_yvCmkg2Fjt9fxFTEei6EMjxWb9gBnr0vfyRJe4pn-wPR31TL79nJRH1nzS4_KNb_WZ9fliiXozuIMKWIs0NpkNPUCUy6hnacOUJqZkZgNpwiceEeB2RlerxVPPRmVu-SGGmKOlpNvVFGU0eu4oSLzslX6DPXgTf9kuAXyGwv_ypYxUyTFoqtrDdJpD1i_ejEwOvOers-JSeptXm3OR_mqCXV9nGnyaHdbA2niTmF0Lt8iQL0vfDS6yWo_P2MUChvV1j_3aVA8BGiXYgBCTwxTwr4hSUrCj9oBRBZKhv-T2rBqvwalVukA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fad3da36c.mp4?token=eAg8QFomTHlEapFr1wPJG152uH3cyYR6_yvCmkg2Fjt9fxFTEei6EMjxWb9gBnr0vfyRJe4pn-wPR31TL79nJRH1nzS4_KNb_WZ9fliiXozuIMKWIs0NpkNPUCUy6hnacOUJqZkZgNpwiceEeB2RlerxVPPRmVu-SGGmKOlpNvVFGU0eu4oSLzslX6DPXgTf9kuAXyGwv_ypYxUyTFoqtrDdJpD1i_ejEwOvOers-JSeptXm3OR_mqCXV9nGnyaHdbA2niTmF0Lt8iQL0vfDS6yWo_P2MUChvV1j_3aVA8BGiXYgBCTwxTwr4hSUrCj9oBRBZKhv-T2rBqvwalVukA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارت‌های بازرگانی همچنان دست‌به‌دست می‌شوند
🔹
مشاهدات نشان می‌دهد یکی‌از فضاهایی که کارت‌های بازرگانی برای اجاره عرضه می‌شوند، آگهی‌های سکوهای رسمی فضای مجازی است.
🔸
این درحالی‌ست که به‌گفتهٔ دادستان تهران اجاره و خریدوفروش کارت‌های بازرگانی جرم است.
@Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/461543" target="_blank">📅 15:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461542">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf92b2ceaf.mp4?token=Reup1-tBUo3A5Mz2K4IgHD_0DyKplMZ1RKfFl3Mg91P85cYQPUj1OKPEsLx41x3ZQa8RRFGsRsYXA8414xuAbhc8dU5cUbAO1PrDA2bExpRaE3dR61IDjuBXRTbbD93x5i7fPEUQSIIQVinffIUcCpm7TTHT1YWJ026bHB-0UlEanVRQnAPf5ZBcmamV7Dq4zZLAxifXHH1hSxC4rGf3s1V-BrnuB29pPx174jzhXHqVPrKySXu1ui3UfirnkPJMr6ZO209UEkuGfnzU1DuasvH7dJK2r_N_HxZmv48aCJlZI2vEpMGg32oxEqrPxk60f6MYhw4OCkngfiZ4lbsXxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf92b2ceaf.mp4?token=Reup1-tBUo3A5Mz2K4IgHD_0DyKplMZ1RKfFl3Mg91P85cYQPUj1OKPEsLx41x3ZQa8RRFGsRsYXA8414xuAbhc8dU5cUbAO1PrDA2bExpRaE3dR61IDjuBXRTbbD93x5i7fPEUQSIIQVinffIUcCpm7TTHT1YWJ026bHB-0UlEanVRQnAPf5ZBcmamV7Dq4zZLAxifXHH1hSxC4rGf3s1V-BrnuB29pPx174jzhXHqVPrKySXu1ui3UfirnkPJMr6ZO209UEkuGfnzU1DuasvH7dJK2r_N_HxZmv48aCJlZI2vEpMGg32oxEqrPxk60f6MYhw4OCkngfiZ4lbsXxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جای نفت در جهان هرروز خالی‌تر می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/461542" target="_blank">📅 15:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461541">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d6e9ca6f.mp4?token=kZdry_XkfgljI5PlbE1NlK6UL2Fp7K0B4Lbga3nTwio2a0-uV9Sy6aveU8xcb0U5q6lXaUzh9cC8ls3OxPPdxjrWsxjefKrY9QYVADcQYUPu-ht1zswqdYMNIy-j54VHZmMNTeUletbjDKSsV0Es_9gtWi8wXsmufLvfAogb0zYiPKra25lyo56BLO7RiMDpcEx8yp_nFM06xxoLKiXKDSZcbZaYZEiX488MmFeETBVxls6vg-Ur0hG5MR1HYVvnR3S3lF-R5-y6cwv2hNTd-fXCvZr0vC3M1FNUHAtcKeLMTgS8GhFjIDYThTeulDBBgA7R990Nmqdyws2ywrMYHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d6e9ca6f.mp4?token=kZdry_XkfgljI5PlbE1NlK6UL2Fp7K0B4Lbga3nTwio2a0-uV9Sy6aveU8xcb0U5q6lXaUzh9cC8ls3OxPPdxjrWsxjefKrY9QYVADcQYUPu-ht1zswqdYMNIy-j54VHZmMNTeUletbjDKSsV0Es_9gtWi8wXsmufLvfAogb0zYiPKra25lyo56BLO7RiMDpcEx8yp_nFM06xxoLKiXKDSZcbZaYZEiX488MmFeETBVxls6vg-Ur0hG5MR1HYVvnR3S3lF-R5-y6cwv2hNTd-fXCvZr0vC3M1FNUHAtcKeLMTgS8GhFjIDYThTeulDBBgA7R990Nmqdyws2ywrMYHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه از صحنهٔ جنایات دشمن در لامرد بازدید کرد
@Farsna</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/461541" target="_blank">📅 14:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461534">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tzdq1X6x834RR4JfqdinnWoVVy_fRhKlhwnR9yxpsqD-ymCpydi2LpduD1ebWqQ28ehigGoKsko61IjYjHbMXxeGy4vcLiGE8u6yXTQhGlh-tHOpJgQlO3Mm_r5KnNhubzlXnxn5jk70VlQva0tMXmi4vIpE2Ku_v9ddnaMFL_VTo1pHni5k_wJ_jAx3Oh1SlzlD6qOeO2gnHqx-GuE9LusqF_g4EuMEwJlhj-wAY-bZV-3vOfa8D6gEQiaXLpnUCsPB5QcDl59bmJgX_uDtYgXrUll_3oSFS3uTamJ_VeAeMpXgxz2K8ntHr8bk1TOlPWCaU_CNSo3HUiogyvnhcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGwmLdcSrzzdsz8TikT6ZnL36ms3yG4EDKtK6e9wjamKpf_-tNAa3AaT88alhECoAX1r03kvA5mrx70FsFnycvSWzekzQBDGbCaj_h5xEIsE8aXYpH-jRuky9zSN4I5qVvwBOLPHkEIRTnOC99bp7Lc1CrfJDAF6teUx9-SIQvqwWg2JnO8DwSLu57ZXk1MdF1ITverLcDO9RPRjxrzu6mCJwao645xv4iWGfPnQe_Dr8_g1Q5uljHHAwbupPpm7kogIa_CGGdbpnF3QZdmwInL2KA8BHGYAdeCW-wSwZiqYY4Wlv7yutoaCE_mjeeFOQF-QuG1SnkhKUiku6AipVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNjLyHdpSn27Z-1ytav_t88xMIxKFTF3qW-Z7ZSACvZj9_ku3f7vF9y2-JXRd2QaF48-5YnKW0ETXBkPrT6dDaAIaUGmLst8TvZT_NyS5dNfOlz0UCpDNK9ZBNcW_mVqvv43kryZ4n5jmBpoLq3K1m-dPDdMoDgcgTWZa1yhIiZpLJrJ8G49TQolU111e8J76eI-LH-6BVgOhdUU2Mx_1YSzN0Km22ytQlSm5yqIZCUv9T7FuLRD97Mu_shG7Emy-I7pQvdFukKLT_bTkEJijVVFRDmuTeSQkfxdTrwLtihyvXXPLoeh_Cj0h7bSk1ME62djo_nRyVIJTA0Zg3fiMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pJnhjzZrFvi-VqvF_fvRdhoERb3StJ35KEqYNHG40gSzWAADfNuHZGUONgcFBYuJ6WAXmjNVpytwwMIw1l8DV_L_QZ5_rU1y4aFWeAc2IeUx151nHqmoBW_Zg05-_kun-Zv-7dJTLDPuHtMr6qDLB2Dw61u5VOnJk8LYLJvwAWx7_CvyYtxJrPGrFxy3VMdtnwRuFFq2_SticzydMRGQhntlcckeSlV8JIPngYa1c9Xync3UjWj-BuO_VZyspBvmDN0WRRIWCIdPyIGTbI9-fEDdqOEDAY3xdrK1WIBsZHHq4-tDS0LYqxaQhmfX95TrYu8pRnFBekdJapFmnqAf0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKBBgjuxQx6qMmGkC0ZwEEm-fwwPwithvXAwNPCIg0bj7b_Lj-hthR8fMS71EMnLmfkGC9-NkZnI9ibhN7o4bcjUVV8oOv_4_jB_ZHx9tB_aHqbjmuQ7l0MsgsWxjf5ScphGJ3eUQ4z0prWdz8vweS-7dEfw_Y1ptaNMOf2TIK-A-yEi-I3AMdpMiLAondGfFvdsUcwp-l-0ZdsJHskbCxHnVdg909seGgTktxSNuGjjZFvk63HSzuOB0TZtLJFT3Xv3nRd1SaNmcomsmOhs1yEk5SmXIaAL2IRaaz5-89bLoegLhQgoYZQ9Hd0qW0l_R81YhAwii2GRIUDAaYa76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ithonNdV5B4atU8iyoaYQKVgn5PI9OsQ0b2dCeQawDeDWz4YsMe__13mIpO-NYylf6Q6Ef3fQbZ0hVDKoMStRuGqeV-XxpWWxWTQzaoNZ2LAzBkqBUWMXrBJK0eu4a5VJqLdxjdcXLy3Ht9agHOzdOS9uwP36dNA5mxDPLNe1b_IYImqU1Z3r4ouOY754gIQo1_Dcfaa2jnqFJxfDXuWAVYy6lKG-DuO6S0S4GnVyL1L6rU2vCNOSMwQYMSSaTU4FZmQ7qCxEsDacGa3EGq6pIaeELIaHbfglTHIWtBFSOHXbwhZmyyp8j9SEDktUqSwlaPqr_faBuGdDfZqjkpUYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A5yojMtn_huFUAIUqESMzsvUrsPFQVYfnu18pF4Nn5JUn4DYLWMY8btTq_4KrJP72xhVITYOVjCux2tc_xdhxhw68OU6berPZmY0TkTnLwJRkaKHk_kooRj0muKhL63i2t_sKZTvcpvvVqoaZr7uslg_PDwZiOgm7HivggVEi9BsZ67f94wJOJeKdhcc8pR_0ZSffBWRoEEX38Gbxfm3TeKBFdNbnL-59cP0NbjBnexNsI6ExBITRKi0hIboZhYMFpzlQVzVkwZBtgD94ru24ivwsGLKG6ms2NtWzP0c-qj7J8rmZbytdF_ZwiBmQ8136rBDZ9XJanXeEfnwlYTNrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نهمین جشنوارۀ انگور ارومیه
عکاس:
محمدمهدی فتحی
@Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/461534" target="_blank">📅 14:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461533">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a405ba0f.mp4?token=fuiRDikLcgh0EzJ7J30xhGjVDccLXcAdhlCnVB82BVM-8o-2DYU533tVfuyrkdW2QwJ1OeFkSoRNfTjRoWb5veoGCSVLXB5H08j9x7xto_M56MrKXR37ZE0MgpZW7Yd4LnunfhE4Wd19-Vs-rtP_WpzU2rYEr9KDi_p2JjUGBvlfzR67MYQQ8Yx5_X1eEy5O_L5IS3npqScSNoLmPydkkTJvaW_9Ijju60Kla3Z80IU3aIxFTErbpfgH2kyq37F_TDTt1piFBjj99ikoVMBi5ZYmjagzQ3r8ia7MJEhImUs8cjONZkqKoPKu1BdaB2WJg-wGg4_WxATNnt0BgLODhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a405ba0f.mp4?token=fuiRDikLcgh0EzJ7J30xhGjVDccLXcAdhlCnVB82BVM-8o-2DYU533tVfuyrkdW2QwJ1OeFkSoRNfTjRoWb5veoGCSVLXB5H08j9x7xto_M56MrKXR37ZE0MgpZW7Yd4LnunfhE4Wd19-Vs-rtP_WpzU2rYEr9KDi_p2JjUGBvlfzR67MYQQ8Yx5_X1eEy5O_L5IS3npqScSNoLmPydkkTJvaW_9Ijju60Kla3Z80IU3aIxFTErbpfgH2kyq37F_TDTt1piFBjj99ikoVMBi5ZYmjagzQ3r8ia7MJEhImUs8cjONZkqKoPKu1BdaB2WJg-wGg4_WxATNnt0BgLODhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسته‌شدن موقت مرزهای شلمچه و چذابه توسط کشور عراق
🔹
معاون استاندار خوزستان: بر اساس اعلام مقامات کشور عراق، از بامداد امروز مرزهای شلمچه و چذابه تا اطلاع ثانوی بسته شده‌اند و هیچ‌گونه تردد کالا و مسافر از این مرزها انجام نمی‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/461533" target="_blank">📅 14:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461532">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttucBcaIb6ULuEmmQlCcb5D3PCQBsDLsj08Bu99RyQlaLx9ma4f-INPOZYD1Gv9ExHNrNbh_C_OmrW0oFowXwMuBRJjCpcjgkYF3WDSCwtP8nq-WqJK7PmOweqwaVT1gDa8AKmgTCWITJSxe-NQ2fVrWt1dOrUJngwFZhRfOGPEoR-fAVfLjGtDq-92i0hRxJjUZlT7SEhqVqKeqJryKNU8GEo79vzx2Pu39nPnRslBkmOB4plJm_qEgOE-ZNAYJEbF5pcJMyypoe80BqZEA7rPAWHInK4ATdHIre1Nb4S-UUcah5ucRZXc9ZIwzHETEO0EQAaGZhK8nFLxqsorlqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پزشکیان با رئیس‌جمهور هند دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/461532" target="_blank">📅 14:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461531">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d6858133e.mp4?token=RAOrO_ouLuR8Ni5mE5FsDIqa1VR-JYiQfnKNxrrj_MiCCpxbQIge2bFleuoMEoTOgo6UrrvOpD2RgMAqt_IeVcrhDnrJDVsnMdoaVPJGIGt76s3Hm9a5_8OE8qmASTdsMtzMeakFPVudG75c1J_jKAh1AvqP42l1mWyvVpAiXhak0g6CT3Pke3HzHU8n_vP-XySj0Q9GFLVh3Nua3End-pvsQp7KUsNIe4elS8dho6-eC4R5v8WbT2LF9azN_H_3LbDKVdCPeP-GqvVguFO10srTr3JfHiZmiRA68Q0Og-eum6Pfc5iiBq0dQ3gD9SKx3K_vGJTPNli8OM0B1VmaLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d6858133e.mp4?token=RAOrO_ouLuR8Ni5mE5FsDIqa1VR-JYiQfnKNxrrj_MiCCpxbQIge2bFleuoMEoTOgo6UrrvOpD2RgMAqt_IeVcrhDnrJDVsnMdoaVPJGIGt76s3Hm9a5_8OE8qmASTdsMtzMeakFPVudG75c1J_jKAh1AvqP42l1mWyvVpAiXhak0g6CT3Pke3HzHU8n_vP-XySj0Q9GFLVh3Nua3End-pvsQp7KUsNIe4elS8dho6-eC4R5v8WbT2LF9azN_H_3LbDKVdCPeP-GqvVguFO10srTr3JfHiZmiRA68Q0Og-eum6Pfc5iiBq0dQ3gD9SKx3K_vGJTPNli8OM0B1VmaLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۲۰ مگاوات انرژی تجدید‌پذیر برق‌آبی به شبکهٔ برق تزریق شد
@Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/461531" target="_blank">📅 14:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461530">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff42263766.mp4?token=f97cSSyDhAq2QQwVG6ZAFV15risQZyhL_lvufLG91p91GTbtu6ImydmCJZKBrksdRJV4Tjnixgt9rur8FcIO0iB_rpvb0qi4fvl2aXVjHuXrITcjjycKsPzAXVzsUEABxehFz5KA_Wk99Itv8SMHmMoZ_QzmP70NzzWjFjyTP7UMLfDAQFvDkitrIjW20PFJiY6tcK7ifxK1O0dZfo897pj-oT576VlYG0MWdP0WmZ-zNQikqVaScOxnH-75J2xTOP8-FQrxep0U4TU4XISbOH8TKJw9_kurz495X8EP459UkM75tIjiyhX3fr_bGxEmRqxg75-L-hDyTv_6hyMkbxNlF63FoJYhhOC5zhVpqsdCSJqgsM4y-q7z4IwRx3JEa6Wy6JregrVS3qcDA1yFcGJcDt72WTZkwGNzpz_4LIEDRr_rqOoh3RnAsf91BmluCo2nt6Xu6Wie7PGkkuFYqx5hoiHyBWBLXTVO5qAL-OHwu9Y13CHbNPdfHbGJ7tMp_lLtER_MCirzEQ22AN6YMI5PUkr_GGYcq_Y6ESVY_XVicPBmVBubgek4zZqO55rhiBRCStdPL7cOa24t8OihH4s3zXHskINryKIaTu7pngexbG3T8ydtNnq1aoDeX8RYR8v8zYrchHBqOl-eMXnzUPG6QclHkSTLfpjZiVM7Bhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff42263766.mp4?token=f97cSSyDhAq2QQwVG6ZAFV15risQZyhL_lvufLG91p91GTbtu6ImydmCJZKBrksdRJV4Tjnixgt9rur8FcIO0iB_rpvb0qi4fvl2aXVjHuXrITcjjycKsPzAXVzsUEABxehFz5KA_Wk99Itv8SMHmMoZ_QzmP70NzzWjFjyTP7UMLfDAQFvDkitrIjW20PFJiY6tcK7ifxK1O0dZfo897pj-oT576VlYG0MWdP0WmZ-zNQikqVaScOxnH-75J2xTOP8-FQrxep0U4TU4XISbOH8TKJw9_kurz495X8EP459UkM75tIjiyhX3fr_bGxEmRqxg75-L-hDyTv_6hyMkbxNlF63FoJYhhOC5zhVpqsdCSJqgsM4y-q7z4IwRx3JEa6Wy6JregrVS3qcDA1yFcGJcDt72WTZkwGNzpz_4LIEDRr_rqOoh3RnAsf91BmluCo2nt6Xu6Wie7PGkkuFYqx5hoiHyBWBLXTVO5qAL-OHwu9Y13CHbNPdfHbGJ7tMp_lLtER_MCirzEQ22AN6YMI5PUkr_GGYcq_Y6ESVY_XVicPBmVBubgek4zZqO55rhiBRCStdPL7cOa24t8OihH4s3zXHskINryKIaTu7pngexbG3T8ydtNnq1aoDeX8RYR8v8zYrchHBqOl-eMXnzUPG6QclHkSTLfpjZiVM7Bhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: چندجانبه‌گرایی زمانی معنا دارد که همه در برابر قانون برابر باشند
🔹
حکمرانی جهانی زمانی مشروعیت خواهد داشت که صدای کشورهای درحال توسعه شنیده شود.
🔹
ما به‌دنبال جهانی هستیم که در آن قدرت جای قانون را نگیرد، تحریم جای همکاری را نگیرد، جنگ جای گفت‌وگو…</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/461530" target="_blank">📅 14:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461527">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ae4DXayOGAePEDRhfOCXd4GbS-vhH6eiXYdx_Rg_xV49PSY_NeLuMWVbrD0DiUTi_o69zkptCFeGbHnRnz4wsud-5vhTUKAsTBvuHb60tIFEdB-3NpfLGvdIgvKwF5E7Qn1yBXtWBxVdlLVk2liyOHpo647wumFip6fBRbbuqvQ_A_TVOGId6r6idYH9zh0OFnp239AK6K4fSEcQ41wh6qQj43S2vLZnPf9eI062Cw3xZ6ygZ2dTWN34lsUd8ysEcrb3VSZWjfMyU0GwAksrkZCJBiyhHUdLXZjL_qLheLRG7sXYLrrU7iezMrAQNnAJfy5DZECYX5f2m9-EbEiaOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brlQfW-nsGg9lm1Q5EPRnhlxfGaejMM9d9v0QMNv7arfkUwES_4S2fSL4M7oYFEMaiJNDdb--E4G2RBMEhANiU_nuWWn-YJGmBT79gFr0YnDN6f66Po3eA13I7NXBfdbV9p031z2V_BEg75ChG7CQMmvyJ18Tenc756882zlDMfO4xtFXy_3OdXSCh2iWjg_8aLmHTL3uE3K6DzJO3VRyTJMlVekdq9Uy6Jrn5NSh89q6Fgs4P3om1k-a0etz6g4bzkW-iIMC3WQvaLmc98uZudI5an3G2sJL7hJYuQY5jjyP1wPE2HV69UB8PxcnQM2OlSNWNJMGFTnMEdDt-qeZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">25 سال بعد از یازده سپتامبر؛ مردم دنیا درباره آن چه می‌گویند؟
🔹
در پی انتشار پستی از سوی پیت هگزث، وزیر جنگ آمریکا، که در آن مسلمانان و گروه‌های اسلام‌گرا مسئول حملات ۱۱ سپتامبر معرفی شده‌اند، شماری از کاربران با انتقاد از این روایت، تاکید کردند که این حادثه در چارچوب یک عملیات «پرچم دروغین» برای تحریک افکار عمومی آمریکا و جهان علیه کشورهای اسلامی و فراهم کردن زمینه جنگ‌های بعدی صورت گرفته است.
🔹
بخش دیگری از واکنش‌ها نیز به سابقه سیاست‌های آمریکا در قبال گروه‌های تروریستی اختصاص داشت. کاربران با اشاره به تاریخچه شکل‌گیری و گسترش القاعده و داعش، واشنگتن را به حمایت یا بهره‌برداری از گروه‌های مسلح برای پیشبرد اهداف خود در منطقه متهم کردند و مدعی شدند که آمریکا از تهدید گروه‌های تروریستی برای توجیه مداخلات نظامی خود در کشورهای اسلامی استفاده کرده است.
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/461527" target="_blank">📅 14:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461526">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7108374e6a.mp4?token=aEZYNxAhBYE4w9Ul6Y3Z9NEy2uS9NtwQNxibQ-NliXOFhG5vk_2faw2YWLXP39_X2sWSMUVEaWSb0OU-t58o-PYyKs68q95B4Jsn5X_qKOY25Ib0BGUK77vc_0F9GJE9CdaZLHURyHmNa8U5NVRa79uS0b4jY_qjk3hp6Am0DugAkumZA-Mo52EzW1Crbcz3HpbrLBF7sX9jIZCSzeJH9apoDMvn27WgOdlzn7P-dz6vjRzYNpUGTFqX4uV1s1bQJZSzLIAn7Qscfrne2uW_N4NxqFAC0J4RT6leGRn5GoqZNSWNBhOGVUnTpvSTsssVMx0KxPgwIPZvg8JEJ8T8ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7108374e6a.mp4?token=aEZYNxAhBYE4w9Ul6Y3Z9NEy2uS9NtwQNxibQ-NliXOFhG5vk_2faw2YWLXP39_X2sWSMUVEaWSb0OU-t58o-PYyKs68q95B4Jsn5X_qKOY25Ib0BGUK77vc_0F9GJE9CdaZLHURyHmNa8U5NVRa79uS0b4jY_qjk3hp6Am0DugAkumZA-Mo52EzW1Crbcz3HpbrLBF7sX9jIZCSzeJH9apoDMvn27WgOdlzn7P-dz6vjRzYNpUGTFqX4uV1s1bQJZSzLIAn7Qscfrne2uW_N4NxqFAC0J4RT6leGRn5GoqZNSWNBhOGVUnTpvSTsssVMx0KxPgwIPZvg8JEJ8T8ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: تاسیسات هسته‌ای صلح‌آمیز باید از حمله و تهدید مصون بمانند
🔹
مقابلۀ عملیاتی با تحریم‌های یک‌جانبه و ضدبشری اولویت اعضای بریکس است. بریکس باید صدای عدالت باشد.
🔹
اعضای بریکس موظف به ایستادگی در برابر عادی‌سازی حمله به زیرساخت‌های غیرنظامی و تأسیسات…</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/461526" target="_blank">📅 14:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461525">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bleGXamophasIwzTeCoxp4IXDHZSdGv_pHjUafrSWxqV_q2Qq8o39Fosatoph3VwokrPBMXBhUxtFGDhQ4oM8X5Ae95c_jw7uCwC04-1WJijHLe2RNzfNzXep1QICcZcMUiT4k1P8EZ6YzXOWVHEXmVvVlYlyRDrneR6NBrZQWaRfLA5CQZ27ALnfu1vynLvuTTQBzN_GBrSgCzjKN4WndfATl3IXiCDQGxdOjc0pb51vH_sT5bNh45ySIBE9eIfIiWqSGt6onLP8zYY-TuO26n3D-g8MipK91T-akd0JMerIL6OTkXkK7EVDHMRYg0FV6Dc61gmRz8kGIc9BSY2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانشگاه‌ها می‌توانند تا ۲۵ درصد آموزش مجازی داشته باشند
🔹
معاون آموزشی وزیر علوم: برنامهٔ وزارت علوم برای نیمسال اول سال تحصیلی ۱۴۰۵-۱۴۰۶، برگزاری حضوری کلاس‌های دانشگاه‌هاست.
🔹
دانشگاه‌ها براساس آیین‌نامهٔ جدید می‌توانند تا ۲۵ درصد آموزش خود را به‌صورت مجازی برگزار کنند و آموزش ترکیبی نیز در دستور کار قرار گرفته است.
🔹
وزارت علوم برای اجرای تدریجی این شیوه، کلاس‌های نمونه‌ای را در برخی دانشگاه‌ها آماده کرده است.
عکس: اصغر خمسه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/461525" target="_blank">📅 13:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461524">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d0c57f91.mp4?token=E_NIJO93lG9yimD_HwtHCT4R-J2XBGg71ESLFHk-1jkatyjrbbGgsqY3eDerkNYuLvweEEv4Uw8cp7_GOn8y065IpaDAu3u7sHYJMhrs6r49rHWz2DQf4NZ1kL5WoqnPlYdaBtrouHstiiuuTUeBUUb5LF1DxEK08MQUpWxxj4GROp7W-zMXfZ8nhEcHjfgdGeqsenFiU6haOC0kLU5pYG0Kea3q4tWTLRtK550JWpsNGd1VTmV7EEn0219dP_Fi91IlJw4IDY9dZbb_rL3Fsfx2OYeXdXXpDsfJwAg6TeQrK0JpT74hqp0sijQV1nTHzC1PD41KDQD4-sO_dge64Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d0c57f91.mp4?token=E_NIJO93lG9yimD_HwtHCT4R-J2XBGg71ESLFHk-1jkatyjrbbGgsqY3eDerkNYuLvweEEv4Uw8cp7_GOn8y065IpaDAu3u7sHYJMhrs6r49rHWz2DQf4NZ1kL5WoqnPlYdaBtrouHstiiuuTUeBUUb5LF1DxEK08MQUpWxxj4GROp7W-zMXfZ8nhEcHjfgdGeqsenFiU6haOC0kLU5pYG0Kea3q4tWTLRtK550JWpsNGd1VTmV7EEn0219dP_Fi91IlJw4IDY9dZbb_rL3Fsfx2OYeXdXXpDsfJwAg6TeQrK0JpT74hqp0sijQV1nTHzC1PD41KDQD4-sO_dge64Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پزشکیان در حاشیهٔ نشست بریکس در هند با نخست‌وزیر مالزی و رئیس‌جمهور اتیوپی دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/461524" target="_blank">📅 13:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461523">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szMxxNuTxrjWhBjTEhbm84SiHPF-_-aKKYyqn4mu_fUvCnhp7wFnpnjXlJU6JgtIMJmARZdKnhT0HZ4pFXyHlr3DnYDpiBAqiOJAGG8FfGaKpmuz1mce57pPEPYEGW906IEsC0jnU3EqbfhRhdnqIJpI5K8vc2-qDRKjw-ULYLTSyK7Mzfy48kkItf7CW7-TSeWHtS46HxLI3jnMc72TVkt6IMTvCWQjm0PoA1UmuZiK3XMNTN5WdhszYaxHHhBjRwGLfOD8v7t24mIqGvDUStn2aBrQT4gukRoUw4lVG8XHKk7-ow2XNoiIG0mVXp97KMCWQaM9IGJ5F_ZOot_yjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ: پوتین مایل به دستیابی به یک توافق است و اگر زلنسکی هم خواهان توافق باشد، خیلی عالی خواهد شد؛ مانع اصلی ۲ نفر هستند که از یکدیگر متنفرند.  @Farsna</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/461523" target="_blank">📅 13:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461522">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c7826bdb.mp4?token=EA6i7BRrnyTJcHzZnBGpgVwp2tB1Obo8kckr2HwytXmXJjaOvaq8O5lhbv7ectiG7sHKj-aXprJZyfu6LbfJZPU6etUjCtSfuQRTqFEyBTBPdOVnYLy8pEmpdXkCyF-W7AcambScbgyfJul-AEUyzbjjZc1tM2Me0-O5id6GwTBAEuRLbM5gBIAwuJv9P0F20ADzhBLdzkTBy2-CryQP0TKdAugqAMTfypxbEmyBzrRbhdWvbrZrxTx2cI0VxMkYkocd2QVNS5Ig6GrLPP_Cd9t6qtERQtcxTMO3o76nXGOFRe7cJeEEVDV4-kQ47INe2qfdxOXcpE628o38kLbZHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c7826bdb.mp4?token=EA6i7BRrnyTJcHzZnBGpgVwp2tB1Obo8kckr2HwytXmXJjaOvaq8O5lhbv7ectiG7sHKj-aXprJZyfu6LbfJZPU6etUjCtSfuQRTqFEyBTBPdOVnYLy8pEmpdXkCyF-W7AcambScbgyfJul-AEUyzbjjZc1tM2Me0-O5id6GwTBAEuRLbM5gBIAwuJv9P0F20ADzhBLdzkTBy2-CryQP0TKdAugqAMTfypxbEmyBzrRbhdWvbrZrxTx2cI0VxMkYkocd2QVNS5Ig6GrLPP_Cd9t6qtERQtcxTMO3o76nXGOFRe7cJeEEVDV4-kQ47INe2qfdxOXcpE628o38kLbZHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از به‌غنیمت‌گرفتن تجهیزات نظامی مزدوران سعودی پس‌از فرار در یمن
@Farsna</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/461522" target="_blank">📅 13:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461521">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">عملیات پاکسازی یک خانه تیمی در سراوان
🔹
بامداد امروز عملیات حافظان امنیت در شهرستان سراوان برای پاکسازی یک مقر عوامل ضدامنیتی آغاز شده و همچنان ادامه دارد.
🔹
یک منبع به فارس گفت: از حوالی ساعت ۴ بامداد امروز یک عملیات منسجم علیه یک خانهٔ تیمی در شهرستان سراوان…</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/461521" target="_blank">📅 13:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461518">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86aa112bb8.mp4?token=FlXgT3fe5o5ROp7YbhaeV6H4AQsM1m69CL7k1ZesZu7Kj7uOgd9NqU5ebZjRL1DKK--GsAy6LBwRQJpzRJ4v34pRL5bs8JvH2f9FYShc3APSq7B3cKo4z5ShsOFDjbStpsA1t2uv1XEgg6ZcGxpYJdrhx0psiyEsiT55-4lfSUk73QxC2A5uWWI5dAgpVHhIF96aUgVDrvUPDZBuF1h0c3M0uNO1bBXPAG_ykTUQvSjtvtSfzJcn38reyByp3SE6EKtXBRFFZhudkpypDIDdqG9JEE9Sg1KihXQXj2zAY4ChGczeOaMdIQWVePZ-AM3He648oUXfbKIwRc7eE3T0gy0kCGO1k5ZvOi_4-eZIWTQxkSHjgIxZsG9Nha64rOUFgLerMj-SdT3r5n8KRrnNVcdCyuNQgUXXogaOvGC4Ww-rDL13XvSVqhlGU3livAmmEcqkg3nNR2aVxm25f2tNnbEvs4ocZKiznOBgISnWMk-l3gEfxeEhQAGDTnxA6eBnVVIYosIaB06TzoKQM1Rq5OJUg6PKWnlFxBEqqx02ECWtH0Av3IGz8Vjnsen5JeestdRI9OWdWKotR0sOhh2Tk2_sxefKD_gPkcmf_ScNc93XWKzf_Haj0tKldH7386YVqy52fgWKF7hPcZ-xiLJIsj_Fv9qqg-_Sn5ZzNjtlKAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86aa112bb8.mp4?token=FlXgT3fe5o5ROp7YbhaeV6H4AQsM1m69CL7k1ZesZu7Kj7uOgd9NqU5ebZjRL1DKK--GsAy6LBwRQJpzRJ4v34pRL5bs8JvH2f9FYShc3APSq7B3cKo4z5ShsOFDjbStpsA1t2uv1XEgg6ZcGxpYJdrhx0psiyEsiT55-4lfSUk73QxC2A5uWWI5dAgpVHhIF96aUgVDrvUPDZBuF1h0c3M0uNO1bBXPAG_ykTUQvSjtvtSfzJcn38reyByp3SE6EKtXBRFFZhudkpypDIDdqG9JEE9Sg1KihXQXj2zAY4ChGczeOaMdIQWVePZ-AM3He648oUXfbKIwRc7eE3T0gy0kCGO1k5ZvOi_4-eZIWTQxkSHjgIxZsG9Nha64rOUFgLerMj-SdT3r5n8KRrnNVcdCyuNQgUXXogaOvGC4Ww-rDL13XvSVqhlGU3livAmmEcqkg3nNR2aVxm25f2tNnbEvs4ocZKiznOBgISnWMk-l3gEfxeEhQAGDTnxA6eBnVVIYosIaB06TzoKQM1Rq5OJUg6PKWnlFxBEqqx02ECWtH0Av3IGz8Vjnsen5JeestdRI9OWdWKotR0sOhh2Tk2_sxefKD_gPkcmf_ScNc93XWKzf_Haj0tKldH7386YVqy52fgWKF7hPcZ-xiLJIsj_Fv9qqg-_Sn5ZzNjtlKAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمانده‌کل ارتش: وحدت و هماهنگی موجود میان ارتش و سپاه کلید فتح قله‌های امنیت و اقتدار است
🔹
سپاه پاسداران در طول بیش از ۴ دهه همواره یکی از ستون‌های اصلی قدرت ملی، امنیت و بازدارندگی جمهوری اسلامی ایران بوده و امروز نیز با اتکا به ایمان، تجربه و توانمندی‌های…</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/461518" target="_blank">📅 13:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461517">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQz8meuBfZeFn1mAjUkdrxh8DPCDMFPoNaRvxRQgikrEAnDBaJ3qcxACGiGgbDcJ4PIRyajJRT3_8fNE0R-yR7xcBZEJnKuMzsE6ldYUhZMRYKWwL6Q34_gS1MEmSp034NMqb_Zt77Yn6Vzf-MMA57TQVVTC0qnGQk08VjIaTRWM01naPVbUF_0qgrdnmam5T4jIvzZVV69JKNxMchLxkba94SOFd7sNm42XOdbristoCgO_aj7TLkEPX0L1lBtltwf9LGAWZMyM8Veqh_sWIYiuX7MJ-HRKRX6rj8zdXFmT-2zlEvrV615roaWvWG9zD1oonimsEGNT0zH6zc-ojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده‌کل سپاه: ترامپ برای دستاوردسازی به دروغ و فریب‌کاری متوسل شده
🔹
آمریکایی ها به سد مستحکم ایمان و غیرت ایرانیان برخورد کرده اند و استیصال و درماندگی در رفتار و تصمیمات کاخ سفید موج می‌زند.
🔹
ترامپ برای دستاوردسازی به دروغ و فریب‌کاری متوسل شده است.…</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/461517" target="_blank">📅 13:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461516">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWm-XzhE-YhyU6hjpDM3wmqyiDStUOFy0wbL3zJKMklbY0CoS_6-VX1VRuVIpMu5pip9ClCWf6wPGH-lscdYaz5Kdyn_sBzlK31VGkZGOczLhhODZLPRE5RoQcfw1klQveFUrVmWg-GAErdC5UczbkOaszr161YHj334k8Y0NzwyrDkFarpCrySltRTVLBiHYPNuZDXMKFipPaA6K9OUgc_-yfvssFjm6q_jYu2-aqiKO7AGHcPA2qBGA9Tb7VJT8vllPeIs_YgMJvL4id6k0uR2nkDSIAGMg7MmaYFmwlwTKZvhUn41pCugepTfLTz_a_laAQiknGy2HZaPyxLN0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست مشترک فرماندهان ارتش و سپاه
🔹
سرلشکر وحیدی، فرمانده کل سپاه در نشست مشترک با سرلشکر حاتمی، فرمانده کل ارتش برای بررسی آخرین وضعیت میادین نبرد بیان کرد: توان نظامی ارتش فراتر از تصور دشمن است، در این جنگ آنها برآوردهای غلط خود از توان ارتش ما را به عینه…</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/461516" target="_blank">📅 13:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461515">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsplmAlroy7VxlwDq0dQryF5ev-IEpls-zGEN1tFbbclfVCZLU-d_pLEg1sVopTENMB39v2l44-vbuqyh2PskNrwEj16ynfU9K2-2UdQKOpWQZIUtFk7ZmdtLeOi1E-3R25sL8MAsctiAQuZUuKiKg_xI2VHtWkNyuKILPNEnI-EWNRa2VEtjRmFJlTWyIgXj8s76ALTimC6ZDIKL-S1384UPpq8rWtH-GeZ1Zh4YUMaPbJA_1rt1xcPiHHsucKcJY3xmBsZmO_yrqKwEoKIT4mu_UPb-6PCj2F73gcugH1kxFPa8YfKP03HfpfaWzKXfkO4qlrLJzsjaDq82f64wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست مشترک فرماندهان ارتش و سپاه
🔹
سرلشکر وحیدی، فرمانده کل سپاه در نشست مشترک با سرلشکر حاتمی، فرمانده کل ارتش برای بررسی آخرین وضعیت میادین نبرد بیان کرد: توان نظامی ارتش فراتر از تصور دشمن است، در این جنگ آنها برآوردهای غلط خود از توان ارتش ما را به عینه مشاهده کردند و واقعیت‌های نظامی ایران در میدان رونمایی می‌شوند. ارتش صهیونیستی بدون پشتیبانی آمریکایی ها در زمانی بسیار کوتاه فرو می پاشد.
🔹
فرمانده کل ارتش: وحدت و هماهنگی موجود میان ارتش و سپاه، ستون استوار امنیت ملی و کلید فتح قله‌های امنیت و اقتدار است.
🔹
وحدت ناگسستنی ارتش و سپاه همان گونه که رهبران انقلاب اسلامی انتظار داشته و دارند، سپر آهنینی است که از کشورمان در برابر فتنه‌ها، ترفندها و توطئه‌های دشمنان، محافظت کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/461515" target="_blank">📅 13:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461514">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmsyAErB97ReMsnwMiCeijGjXTVQBponeVxz7ceMWmmrdR3R3xdgBg54_otInb5N25A0zr_DvOVla1xNIuEX7008MGFR_Z7V5nmPamO744MftKUyTK0gdgl3kqMlyiBf5B9IRc1T_1u4KTk3boinD3toqZMFLbg4Gcl9BEW-hd4WZdSK8PD2myQRbYegpFiNczOFSPztoSazhICCWrzBzqnt4FF_Se62NXjZqG_XROwJqshpXXrXNmDHuIQP2KtQbs3E0tgHhDot0SPrseuO6xt9sr3PGrHOqEenvalRfFt-PCdVtSvcbs5bYsKri1E2wYRUfTYJPtJyhI1SoU2-Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردزنی بورس در آغاز هفتهٔ جدید
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۵۵ هزار واحدی به ۷ میلیون و ۲۷۸ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/461514" target="_blank">📅 12:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461513">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مرز خسروی باز است
🔹
گمرک خسروی: مرز خسروی باز است و فعالیت‌های تجاری و صادراتی در این مرز بدون مشکل ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/461513" target="_blank">📅 12:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461512">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGSr_Uwz5wS5x9t9l4RLycR31_lDfvRGkoMltb9MRX2NvxVEq0JWQxT3nv1Q5nmNFzGTKn_EYcmCGr165BPtfLqN8o5AlvXsbRkpWKf9UOXTtJOVV04UnrbJJzRkogKyxL0x3-l0kmczSbrGA-Wm_vIAFv1I4q350dR3ReYw88k_DXfxOJ8WwREmLgKLS1ixr786NlYabhRX0f6pffqEx4tg3FV5jN4kgcv3bOIXXPaoP6_-oFqIts_ERcCBlCm2sCuVBr3q76kHL1nuoDCYSFKztsE4LJ_HMZiHy6rxiidb16E2InVzjMx14gTvAdRynwb7Bj-qxCaQ7Aono62WhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
درحالی‌که مدیر سازمان فوتبال استقلال دیشب گفته بود که اعضای این تیم امروز ساعت ۱۴ تهران را به‌مقصد بصره ترک می‌کنند، فرودگاه بین‌المللی این شهر تمام پروازهای با مبدأ و به‌مقصد ایران را تا اطلاع ثانوی تعلیق کرد.  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/461512" target="_blank">📅 12:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461511">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOiKTbJhYK7pmCOOPSoYml4W-EGTY5wAZllReotuabMjOA5PT5ejPUUKCeCu0B5l8IThlVTwk9C0_je1mhOZk94APVrqTkYowI3H5l_axr_yOt5fG3Svp_ctY-fRdWdFuJsKVpnaolPdNborBRTiNy2OG1_I_WaC0acEWZ45bJA_DCwbhsBOthQJTjumD1rT1ujM-Nh5gjeV71axjf58JZLTj-y4IaPWU46qpsouCdOIap0JvsrlWxrXvEDKB2GK6awcFHy45JtsmmNMIs8flOnj4zhUxgvIuuinGwKwVdkbsLLegtep0NZLcdPvIOTQPnjAT-jnA0RRNy_iwR7NkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درآمد پتروشیمی خراسان ۳ برابر شد؛ ثبت رکورد ۱۲۷ هزار میلیارد ریالی در ۵ ماه نخست سال جاری
به گزارش روابط عمومی پتروشیمی خراسان، مهندس عیسی نوروزی‌پور، مدیرعامل شرکت پتروشیمی خراسان، با اعلام این خبر اظهار کرد: درآمدهای عملیاتی شرکت در پنج ماه نخست سال جاری با رشد ۲۰۹ درصدی نسبت به مدت مشابه سال گذشته، به بیش از ۱۲۷ هزار میلیارد ریال رسید.
وی افزود: از مجموع درآمدهای کسب‌شده، ۵۳ درصد مربوط به فروش صادراتی محصولات می باشد
همچنین نوروزی‌پور ادامه داد: پتروشیمی خراسان در همین مدت با *ثبت ۵ درصد افزایش تولید و تحقق ۹۸ درصدی بودجه تولید،* موفق به تولید  بیش از ۴۰۵ هزار  تن انواع محصولات اوره، آمونیاک و ملامین شده است.
مدیرعامل پتروشیمی خراسان خاطرنشان کرد: رشد قابل توجه درآمدهای عملیاتی در کنار افزایش تولید و تحقق بخش عمده برنامه بودجه‌ای، بیانگر تداوم روند رو به رشد عملکرد تولیدی و اقتصادی شرکت در سال جاری است که مرهون زحمات همکاران و متخصصین مجتمع میباشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/461511" target="_blank">📅 12:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461510">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7FmQLYMGRP08Gothc_FbnPGSI35enqVQ3iB-GHxvHDUGbNJ5oXMj9laoIADx81d21UQQ9MBD834v_MpRamZLmFWOLXYA76txX6fuatekVp_yqiXENBt5jolmUVsTMwkoAvY1zOWl6Kud4dzgD6zpEFqmSy0h4dFsvxUUOEKur0VGvERp8Ph8JE0d_t5Lh3msxv446ka23M_GwEz-_i6IuVysVmmC8FfNjla6G3JcMFp7DZmXrnhbmx7XSz_-BwafQdUKTKOp6NKSXz5dEMRPRd_ggsmMHIT4Cv00UlP7I3-Pae2IMRXpqu53NnTjQinOXZPm2auqcgJ8_qJEd0UvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
بانک رفاه کارگران پل ارتباطی مستحکمی میان جامعه کارگری و کارفرمایی است
🔹️
سرپرست سازمان تأمین اجتماعی گفت: بانک رفاه کارگران، بازویی توانمند و پل ارتباطی مستحکمی میان جامعه کارفرمایی و کارگری است.
🔹️
دکتر محمدی با بیان این مطلب در نشست سراسری مدیران صف و ستاد بانک رفاه کارگران، بر ضرورت بهره‌گیری حداکثری از ابزارهای نوین بانکی تاکید کرد و گفت: استفاده از این ابزارها برای مدیریت تعهدات مالی و تسهیل در پرداخت به‌موقع مستمری‌ها، با جدیت تمام در سازمان تأمین اجتماعی دنبال می‌شود.
🔹️
وی خاطرنشان کرد: سال پرکاری پیش رو داریم و باید با تلاش دوچندان و مدیریت جهادی پای کار باشیم.
🔗
متن کامل خبر...
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/461510" target="_blank">📅 12:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461509">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/461509" target="_blank">📅 12:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461508">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64aea342e2.mp4?token=lG92-mk-_dZ-6TBUyn8T-h0EKaolNFi3vVNi6W4FgPdwNQN-2vPW4E-jNrIDsnih-wBzWYUy_M3IJcx2QabQAzQKtHqAzaf_izZgPh1l-WCQzsOJbvbGANz_KsQkgyj9pCmlTqx5MqRS380unEXXNFupa-lnA1A5uq-40dPgbIw-k96_kc2DcNMReSmCs7cTe4ZQm0YpBqrsv_grcOpB3m_i6k-j0lajLKmX-iXEMD81256_3DTGzQPAT9mlYk5pZDGDii2ELgx6OCOslBrJKRrYHn1TefgejUU0WYD7RC6CkYxzSzYODiYlYUMSsQNhfA1j0wO-Wo6lNBlsWS00SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64aea342e2.mp4?token=lG92-mk-_dZ-6TBUyn8T-h0EKaolNFi3vVNi6W4FgPdwNQN-2vPW4E-jNrIDsnih-wBzWYUy_M3IJcx2QabQAzQKtHqAzaf_izZgPh1l-WCQzsOJbvbGANz_KsQkgyj9pCmlTqx5MqRS380unEXXNFupa-lnA1A5uq-40dPgbIw-k96_kc2DcNMReSmCs7cTe4ZQm0YpBqrsv_grcOpB3m_i6k-j0lajLKmX-iXEMD81256_3DTGzQPAT9mlYk5pZDGDii2ELgx6OCOslBrJKRrYHn1TefgejUU0WYD7RC6CkYxzSzYODiYlYUMSsQNhfA1j0wO-Wo6lNBlsWS00SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ موشکی کره‌شمالی به رزمایش ترامپ و شرکا
🔹
ستاد مشترک ارتش کره‌جنوبی اعلام کرد که پرتاب چندین موشک بالستیک از منطقهٔ «وونسان» کره‌شمالی را ساعت ۵:۲۰ صبح رصد کرده و در حال تحلیل مشخصات دقیق آن‌ها با طرف آمریکایی است.
🔹
این پرتاب‌ها یک روز پس‌از پایان رزمایش‌های نظامی مشترک کره‌جنوبی، ژاپن و آمریکا صورت گرفت. کره‌شمالی بارها در جریان یا پس‌از رزمایش‌های واشنگتن و متحدانش، دست به آزمایش‌های موشکی زده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/461508" target="_blank">📅 12:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461507">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMArBAq7LQfmsgZrt9YE9SDmoBzeCOfgpWSQFZ9mQy_rvCEJLFKH243BhQM44BmTaWierpeNzUisWNrtKuajfzzkzpSIMr1akxglLluIbtv32rXm61RmwYqRjv7Mb-gH6R1_RxgpHLZXyjQSz0o84eLtKLz2mrjUs0RToRl0gfNLHzJW4HTx39KSnLvlSUKuoQ8WhTvSEW3UvPDzZ8iz7NUcHcMsTTvs5fzwTSKrRglPbpQLPeWn97Fe7w48l2D5XzpfwwSks4xXz-WM28uGNVNS2Y1bdbya-gJQPvZDfuUl-YwXpSjIltpPImsRsdrMTyC0vXr_bOtkzaz_q6byXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلندقامتان ایران راهی فینال آسیا شدند
🏐
تیم ملی والیبال کشورمان در مرحلهٔ نیمه‌نهایی مسابقات قهرمانی آسیا با نتیجهٔ ۳ بر یک مقابل استرالیا به پیروزی رسید و راهی فینال این مسابقات شد.
🏐
ایران برای کسب عنوانی قهرمانی با برندهٔ دیدار ژاپن و کرهٔ جنوبی روبه‌رو خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/461507" target="_blank">📅 12:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461506">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cfb2ceb1b.mp4?token=e_MPyM53YjZO2dxo1nI_SPVbaIOyIfXt3h6IwhqCNE9UWISsqLieAYzeKvCgLZRPk9reJcLL3vdHJjISgHqRTdtUFN0T9f8OAg-cdJchPi-EL7Cai7uIdyVwyU9zEL3-7m3WtBVKJckO0OHKlTxJDeE161rb44GrVwX0gobA4odw1eYQi13aZMVyn9JUojZ0UzwPYZ8QgSGHbKKJOlfylH5mjbJSKPNRwKXI3xd6cx86jP7d4roCY_mFt_EqrCcG_0ElNpKNYI9J1HCBoBMQ6vyU_TFU1jg9OSR-M0Jz5od8lHXZPPIJt2QVakp3v4c8ZOkkfiNXy1tzKPW04BtbWgMLKjXYdnBLYA_d_pzR9WPtXxe5Gu5VYcl7tZ71sCu22bH_YNBy0llcp4yLTXuKCugCUfnPxeMTJ-UyfEUCUdkUhpj9fjVb3AhMBVx-TLs4FM7muRybW4eSGYEbxVfab4YMMj_WFqyxAKMiZ7sYUtP7R-m7ilwp6RFWuDMI8zXDOhfiHVA_9a_RKmPbYqFFTpbopbPHyy71kOnzEe2N9YpPTAbNvhZljsYlW99a5WIAVH9IWPAGLTLDtIFrFWwHvWpPX9Z3zQn_olvq93WahkdgeZ6EznYOssXSaulidZpqAgp392iQoC_UmULClgP9QAqUOU9BMV3_8ZpsEE3jxSU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cfb2ceb1b.mp4?token=e_MPyM53YjZO2dxo1nI_SPVbaIOyIfXt3h6IwhqCNE9UWISsqLieAYzeKvCgLZRPk9reJcLL3vdHJjISgHqRTdtUFN0T9f8OAg-cdJchPi-EL7Cai7uIdyVwyU9zEL3-7m3WtBVKJckO0OHKlTxJDeE161rb44GrVwX0gobA4odw1eYQi13aZMVyn9JUojZ0UzwPYZ8QgSGHbKKJOlfylH5mjbJSKPNRwKXI3xd6cx86jP7d4roCY_mFt_EqrCcG_0ElNpKNYI9J1HCBoBMQ6vyU_TFU1jg9OSR-M0Jz5od8lHXZPPIJt2QVakp3v4c8ZOkkfiNXy1tzKPW04BtbWgMLKjXYdnBLYA_d_pzR9WPtXxe5Gu5VYcl7tZ71sCu22bH_YNBy0llcp4yLTXuKCugCUfnPxeMTJ-UyfEUCUdkUhpj9fjVb3AhMBVx-TLs4FM7muRybW4eSGYEbxVfab4YMMj_WFqyxAKMiZ7sYUtP7R-m7ilwp6RFWuDMI8zXDOhfiHVA_9a_RKmPbYqFFTpbopbPHyy71kOnzEe2N9YpPTAbNvhZljsYlW99a5WIAVH9IWPAGLTLDtIFrFWwHvWpPX9Z3zQn_olvq93WahkdgeZ6EznYOssXSaulidZpqAgp392iQoC_UmULClgP9QAqUOU9BMV3_8ZpsEE3jxSU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پزشکیان با رئیس‌جمهور هند دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/461506" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461505">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmy7DEYil9SFClMd7WIDwK3-Wg5W0wRFADQBhXnbZmNqMBdJFgegogzuQF6AU6o_xbvh7rHUvdGuqC0tLuDinR9BRYnNOaXGnbpx6ljxEp81l_XrncJXmQ_02PC4uUYTT2d0qSBGhtEyKunikvy05rkwa1eWUzBtjamwer3J4-G8OW-AJ_1HV9bR_bfdORBgGJ20znUHIASD2u0s0vQrbh_Yh1jD0HBvP9zL220_e1PwDDCg2KnIDcKENd4Hm9kPCVnpPIQD5colak1wRs-11AjMnWCeVYce-LrXm6wQh1VS2jR11e6crq3OGUHU4Ts4nWh3KmkhcxH_s1pLXLWwsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد ۱۲۳ مگاواتی آسیب‌دیده از جنگ به مدار بازگشت
مدیرعامل شرکت تعمیرات نیروگاهی ایران: واحد گازی ۱۲۳ مگاواتی G15 نیروگاه مبین انرژی در منطقهٔ پارس جنوبی که در جنگ تحمیلی دوم دچار آسیب‌های شدید شده بود، به‌چرخهٔ تولید بازگشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/461505" target="_blank">📅 11:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461504">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HO3Swn83cFir_t9u6CmJZmqveWEZ38t3IhpYO2OCFMI0h-RK8pchO4tdH9FSt50mNdFhPyyUGoJytXSiSvgxe5N14VFBj10NRUNMDPsZbaxuEPJjfcq8awguJORKwSuM3e8bVBD1NONxmc7mbAqvTkR5Yb5j3eu-FwYZy_y7vkV7NpbJk4C-Axc_zPFIpAIM_1PO80Lnhood9QreITjkEJgPs8ape_J1GYJcqPw-YR9SqF7vF1F4yvMb-E3epr8MIyZPRML2ctjvlpCT3ASxWcZkxBpBWTJxXrdkG3bbvqs2yl655H7eVuMUQ1TEYX7Js9Im2SHfi6J1OPR2qGFoUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پزشکیان در حاشیهٔ نشست بریکس در هند با نخست‌وزیر مالزی و رئیس‌جمهور اتیوپی دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/461504" target="_blank">📅 11:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461503">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghAilx2lO4QsmrHHcypiMCj0gEBNjpetD_0LVbMDuDPXik3kmoR5R2qUlUKhnSyqcZrhXQPEO4vri3MJ8NsHv4gi5Q_sT48JTixW2StAg--pEvlZhcXTY83LOrXGeCmvOAr_tl_SgXszRe9Uv9xL_opneDSHZ9P-UTUHxi7iDSAv_yOhYounyhL6em1LsX_EJ91DiQHbFEXuYWI8GxN0GIQg411Igqp9BkRD2LI6M4Mj-FXOLU3y_wvRMFRGHb_2Msqjp8W_IVbHJfvG4T_KWH-niqCgkNHZcIm9gMTfyrCJ408WZMIEH6SKr-kFTAzuWqJzYkCfso4xrBW2lkrMUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رگبار و رعدوبرق در راه شمال و جنوب کشور
🔹
هواشناسی: درپی فعالیت سامانهٔ بارشی در بخش‌هایی از شمال‌غرب، سواحل دریای خزر و دامنه‌های البرز، امروز و فردا در این مناطق رگبار باران، رعدوبرق و وزش باد شدید موقت پیش‌بینی می‌شود.
🔹
همچنین در ۵ روز آینده، جنوب کرمان، جنوب سیستان‌وبلوچستان و ارتفاعات هرمزگان با رگبار، رعدوبرق و وزش باد شدید موقت مواجه خواهند بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/461503" target="_blank">📅 11:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461502">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فدراسیون فوتبال ۲۰۰۰ دلار جریمه شد
🔹
کنفدراسیون فوتبال آسیا، فدراسیون فوتبال ایران را به‌دلیل تأخیر در درخواست مجوز دیدار دوستانهٔ پرسپولیس مقابل آلانیا اسپور ترکیه، ۱۰۰۰ دلار جریمه کرد.
🔹
فدراسیون همچنین به‌دلیل ارسال دیرهنگام درخواست مجوز بازی دوستانهٔ تیم امید ایران مقابل کایسری‌اسپور ترکیه، ۱۰۰۰ دلار دیگر جریمه شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461502" target="_blank">📅 11:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461500">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTsZosIjsA5xmuYTBgi4VINChbKd46GEtk7K6rEtu9ZuWy2BQdvsk7L5rsGfnaBeLklbRIP6CL0vmIGVkVOWLyZg3zLQZxvEBxO7uRNYJB62BeX9Pmk2ItwvVeH5_ezuc5uxnRi95zjp0245uyIResHajPAbueQg28_GG4ildUIIRzSWfFRrnFXj9O7q6LJJ18f5SzH1X6n1MxcvQYWexx-i6F7zQhUMtFO_9Ncs-LIjTjfbi4Eej_eFCHy2CUdHNTPIrjNV0_X9nsii-ZfIb0uFHP_0tMhROtvyp5B9DB7vWDSpJYYs3YpQEBfuOOgEtJntXc9c2B7MO17Bg9FMxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ سردار سیدمجید موسوی به زوج جوانی که حلقهٔ ازدواجشان را به رزمندگان هوافضای سپاه هدیه کردند
🔹
فرمانده نیروی هوافضای سپاه در پاسخ به زوج جوانی که حلقهٔ ازدواجشان را به رزمندگان این نیرو هدیه کردند، نوشت: برای بنده و هم‌رزمانم در نیروی هوافضا جای بسی افتخار است که جان‌فدای ملت بزرگ و عزت‌مندی هستیم که همچون شما گرامیان را در دل خود جا داده است.
🔹
هدیهٔ شما برکت و مایهٔ ریزش لطف الهی در بدنهٔ سازمان ما و ان‌شاءالله موجب خیر در زندگی مؤمنانه و انقلابی شما شود. ممنون لطف شما هستم.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/461500" target="_blank">📅 10:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461499">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkc5nXjOakdzRzM3Q9PCJvncoQffu88WxGYg1Bn2X1JUIi8tEyhIHpxUAKQIjIPQJUBoxwwUfWiaKkxTU93Q7sY52tNLzTfrfP95Rl7c7ZTAASxNkdTChcFnC64v8oEXhitT69tMsK-tMsVJyTe9ynSBRKZ1JSAN9QcCCLq6jrq031hyFjX_oor49r7FVa9KA7eRCu1iiUV_zfX_ztX6umj_iSoTF85kwvWC7ebQEhxxEXNsenV_d_mXY9LCxDWhftssb2eGOxEMsgSdYo_igAPnuM-GhdUiPj0S4FTGZyEGPjceYjRPShBG7TvtskEj_orFtS2dcLa7Xq_h08LHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکایت بنیاد آیت‌الله رئیسی از ادعاهای کذب یک بلاگر اقتصادی
🔹
بنیاد شهید آیت‌الله رئیسی از یک بلاگر اقتصادی به‌دلیل طرح ادعاهای کذب دربارهٔ رئیس‌جمهور شهید شکایت کرد.
🔹
این بلاگر مدعی شده بود در دولت شهید رئیسی از او خواسته شده مباحث اقتصادی را به رئیس‌جمهور آموزش دهد و این مطالب نیز در قالب انیمیشن‌های کوتاه، کمتر از ۳ دقیقه، تولید شود؛ چراکه به‎گفتهٔ او «ذهن شهید رئیسی فرّار است».
🔸
گفتنی‌ است میانگین رشد اقتصادی ایران در ۳ سال پایانی دولت دوازدهم منفی ۲.۰۵ درصد بود، اما رشد اقتصادی کشور در سال‌های ۱۴۰۰، ۱۴۰۱ و ۱۴۰۲ به‌ترتیب به ۵.۶، ۵ و نزدیک به ۶ درصد رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/461499" target="_blank">📅 10:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461498">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bdf7fbf08.mp4?token=i5-k6Gbdow4aP7wSbOLnsvjv2-y52oIdXsHXmY2FIO_A8YLzXhQ9CNS_2GZVcWMV6h-ez_fx0GrkpfAB8bC5Zw4vRgti111pSQrk8lt5sZA61UHXawMkp9BqOUFtkK3MFdXWtj0NiPLDLi0HIjhx5v8dj6tLpsAF30w82TwVCk1GVSyICUm19POuA2ArQbe953LgsHxA0NVxdShnZ6m12keThj6dY-PerIeDAUXieVOIFL8Hl1C58qGmZt7EF-upRzRjeuq9917UXBGSJq4iK1UPfykowImo3DM2pqtjLm7zLCP5UgsPoU8vuHyzHMFe-cn73x1TV0DmVAnNdgWgrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bdf7fbf08.mp4?token=i5-k6Gbdow4aP7wSbOLnsvjv2-y52oIdXsHXmY2FIO_A8YLzXhQ9CNS_2GZVcWMV6h-ez_fx0GrkpfAB8bC5Zw4vRgti111pSQrk8lt5sZA61UHXawMkp9BqOUFtkK3MFdXWtj0NiPLDLi0HIjhx5v8dj6tLpsAF30w82TwVCk1GVSyICUm19POuA2ArQbe953LgsHxA0NVxdShnZ6m12keThj6dY-PerIeDAUXieVOIFL8Hl1C58qGmZt7EF-upRzRjeuq9917UXBGSJq4iK1UPfykowImo3DM2pqtjLm7zLCP5UgsPoU8vuHyzHMFe-cn73x1TV0DmVAnNdgWgrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«دانِ خوابالو» روی «جویِ خواب‌آلود» را سفید کرد
🔹
پس‌از انتشار تصاویر جدید از ترامپ در حال چرت‌زدن در یک دیدار رسمی، منتقدان با اشاره به لقب «جویِ خواب‌آلود» که او در اشاره به بایدن به‌کار می‌برد، خودش را «دانِ خوابالو» نامیدند.
🔹
انصاری، عضو دموکرات مجلس…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/461498" target="_blank">📅 10:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461496">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cute8aj7UHyEIIeOJ5sZ6h19iKek7wMDw-7TIaRF3oof8uS7hTKV_ZmQp4dfsJNJi6cUDwB6Hl1UOb5UIw-I14lUATKCWcDJh3u_Lc-FIK3Z0pnq3DMzSbz5NsNfMKFVF8Y4AEWjJ0J33O_ADbPxoyf7kSXNo1jh2805QL9gNSPTnKXwikXMtJnrha4pa42JkiJDS6JM-odTn4hHeb3cwDyPYMjpYPLj13ivSg6qpphy5WJBGchsH1T12FhRWmxd66R5JIxScBm-D2HxsBpkxB6kltf6FIuuSihT5BfNF_zkvUBRp2GRbYd2BupHpwcyJbvCReqxNS0URp2lvjbejw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2xO-cnBxWSriglBh9W0XQp65SC9NoVDL5euDbSIlWtHuJyG-SxcEv6iGjfTaFvfxozibZv-g309E-70BheCiU-bE_WgkK95h9LfzZoJfBUo0e7V6HpWpqUagLDh4r9LfpCI4ekY228_cMaAuwqbqiTiK44nO0NdAIZ1X2SFmPvJxaZxSTCWXMhhLq6Ks_QyOCDM4CfFjyZ74Fn55WpfI8lWC7DUtBEAWqasQ0fRzkKjfXPhshIp2MpuNxC4iamKdq-uMqUG8CiTZ92EGOITzhjgKDmOtyNdO2o6DoGbwr7kSfV9_ZJf7jfVOuW3OXUfN_4LBA8pRDj17yD4hwDc3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پزشکیان: آمریکا چون نمی‌تواند با قُلدری مردم ایران را وادار به تسلیم کند می‌خواهد کاری کند که مردم به‌خاطر نبود معیشت و امکانات تسلیم شوند اما مردم ایران تسلیم نخواهند شد
🔹
اگر این‌ها مرد جنگ هستند با نظامیان بجنگند؛ با نان و معیشت و زیرساخت مردم چکار دارند؟…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/461496" target="_blank">📅 09:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461495">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/461495" target="_blank">📅 09:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461494">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Htw4lvDkTDPunljnz8-zXNqi9MYnDtQNrhHjpz3L9glbNCWvmdXPiXvqrPu4AE6ZcBROCEJ1SbxBaH0bkY0LA2Z10-OwtpNZ0h-dxUbT_9s5YJnj24QHWVmrGkxCRCyisESWR8jdwtJjyTjSRPmqzLGqj3SpdX4iYJkwxxqHCs0ZPWAPN65R8yGEn5GkIaJM7GPtFlCFSTd3_pIhkOVTnxMsV--ed5FbOkf4cUaoXIoXuvFWWz8xt0sv7e_OXBER5nQzhnSbBVRAF9IRmSMyuox2P_zvCFW6QMqGHG047PPivq51oiWAkKO-Rfpl7B79rxsNE1UOn-hsfVjQb7S-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/461494" target="_blank">📅 09:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461493">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdrp4gK-RYb1r-s1QNVvNFaw56X24OW3gVhhAKnj9FBozrhm3bCxBJYYInJPVYZlphC7NHOHde8cSgboPBvdazzRbR19PJX88EH_nNWspuYw6Qe26LPS7O--IF0AMbsR_PUgeDh0_dz6FQiF25Z024WySKoD8U4bZRxumQoT0WuHbWXj5nAUrAMj6YQDdgaCpK_FW3PsSFD6Ku_AugYUYACeCRDv8933TTty1KggVi-QGcXraN8Z4A3-8s3eJ4G20TYtiSJNFJDTKvEbq5QQOIWEr0N8lOzv-CH9Rt9fdGPFWCSEKpn5mPEyvjVafmNU0NQDQ7OzoR5YOUsMazs-Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ‌های جدید حوالهٔ ارز در مرکز مبادله اعلام شد
🔹
دلار: ۱۶۳،۴۱۳ تومان
🔹
یورو: ۱۸۹،۶۰۱ تومان
🔹
درهم: ۴۴،۴۹۶ تومان
🔹
یوآن: ۲۴،۳۶۴ تومان
🔹
روبل: ۱،۹۳۹ تومان
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461493" target="_blank">📅 09:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461492">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فرماندار مهران: مرز مهران باز است و تردد در بخش‌های مسافری و تجاری در جریان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/461492" target="_blank">📅 09:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461491">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بسته‌شدن موقت مرزهای شلمچه و چذابه توسط کشور عراق
🔹
معاون استاندار خوزستان: بر اساس اعلام مقامات کشور عراق، از بامداد امروز مرزهای شلمچه و چذابه تا اطلاع ثانوی بسته شده‌اند و هیچ‌گونه تردد کالا و مسافر از این مرزها انجام نمی‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/461491" target="_blank">📅 09:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461490">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zvcugz3jTnSiiAnENvx9DlQqr5nCH4fkQo6cOWsFcy20tyyDYc65f89nThBQxQDGKeNYFf6Xov9gKuH_-Sfsp1hJSzlBVWbLj5gLqj4mv4AcVD39BV1aUlV6TH8MaeOqH3kX0CHL07UyT-o4X_bEUBaDUQJ4FAbB4Q-mdcu1DUH7eLxOfu5HOzFeewsr9_1xj3_oPHEfk7jAglD_jHXdZ2dt6I7h2DdUAMmzZYMG0C6CW18IxQQ55VLQnpVAbpTsEoFY4MdcPV82KNlM-MtQOxZEf__Gki08QNKyxfGRPt6zMON68m23q_Isg0BpRbXefgWfrbop-QrHByUVPQTBvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: ۵۴۰۰ کیلومتر را آزاد و ۹ هواگرد سعودی را سرنگون کردیم
🔹
ستاد نیروهای مسلح یمن در بیانیه‌ای دستاوردهای خود را نبردهای روزهای گذشته با مزدوران سعودی را اعلام کرد.
🔹
۱. بیرون راندن نیروهای سعودی از ۶ منطقه در استان‌های تعز و الحدیده، با مساحتی کلی معادل…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/461490" target="_blank">📅 08:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461489">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عملیات پاکسازی یک خانه تیمی در سراوان
🔹
بامداد امروز عملیات حافظان امنیت در شهرستان سراوان برای پاکسازی یک مقر عوامل ضدامنیتی آغاز شده و همچنان ادامه دارد.
🔹
یک منبع به فارس گفت: از حوالی ساعت ۴ بامداد امروز یک عملیات منسجم علیه یک خانهٔ تیمی در شهرستان سراوان آغاز شده است.
🔹
گزارش‌های اولیه از زخمی‌شدن و هلاکت تعدادی از اعضای این مقر در جریان این درگیری حکایت دارد. در حال حاضر تلاش برای دستگیری عوامل و پاکسازی نهایی این مقر در سراوان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/461489" target="_blank">📅 08:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461488">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بسته‌شدن موقت مرزهای شلمچه و چذابه توسط کشور عراق
🔹
معاون استاندار خوزستان: بر اساس اعلام مقامات کشور عراق، از بامداد امروز مرزهای شلمچه و چذابه تا اطلاع ثانوی بسته شده‌اند و هیچ‌گونه تردد کالا و مسافر از این مرزها انجام نمی‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/461488" target="_blank">📅 07:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461487">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ضربۀ ایران به زنجیرۀ پشتیبانی هوایی آمریکا
🔹
ضربات اولیۀ ایران به پایگاه‌های نزدیک به خاک خود طی جنگ تحمیلی ۴۰ روزه مثل قطر، کویت و شرق عربستان که فاصله کمتر از ۶۰۰ تا ۷۰۰ کیلومتر از مرزهای ایران داشتند، این پایگاه‌ها را به‌شدت آسیب‌پذیر کرده بود.
🔹
اما کاهش چشمگیر توان رزمی این پایگاه‌ها، فرماندهی آمریکا را به چاره‌ای اساسی کشاند: عقب‌نشینی تاکتیکی به عمق بیابان. بدین‌ترتیب، مهم‌ترین تجهیزات هوایی و پدافندی به دو پایگاه دوردست الخرج در عربستان و الازرق در اردن منتقل شدند.
🔹
با انتقال دارایی‌ها به این دو پایگاه، یک واقعیت تازه شکل گرفت: تراکم بی‌سابقۀ سامانه‌های پدافندی و لایه‌های متعدد دفاع هوایی در اطراف الخرج و الازرق، آسمان منطقه را به یکی از امن‌ترین حریم‌های هوایی تبدیل کرد.
🔹
شبکۀ هوایی جدید، ترکیبی از پرنده‌های بدون سرنشین مانند MQ-9 و MQ-4 و همچنین پرنده‌های شناسایی رژیم صهیونیستی و از سوی دیگر، هواپیماهای سرنشین‌دار از انواع E-11، E-3 و E-2D بود.
🔹
اما در میانۀ این بن‌بست تاکتیکی، یک تغییر رویکرد همه‌چیز را دگرگون کرد. به‌جای تمرکز بر انهدام مستقیم سکوهای پرتاب، تیم‌های اطلاعاتی و عملیات ایران تصمیم گرفتند شبکۀ پشتیبانی و زنجیرۀ سوخت‌رسانی پایگاه‌های دوردست را هدف قرار دهند.
🔹
منطق این تصمیم ساده اما هوشمندانه بود: با وجود مسافت طولانی، جنگنده‌ها و آواکس‌های مستقر در الخرج و الازرق برای ادامۀ مأموریت‌های خود به سوخت‌رسانی هوایی وابسته بودند.
🔹
عملیات ترکیبی آغاز شد. در این بازۀ زمانی محدود، چندین پهپاد و موشک، هم‌زمان با یکدیگر، نقاط مختلف این زنجیره را هدف گرفتند.
🔹
نتیجه فراتر از پیش‌بینی‌های اولیه بود. هفت فروند سوخت‌رسان نظامی آسیب جدی دیدند که از میان آن‌ها، دو فروند به‌طور کامل منهدم شدند و لاشۀ آن‌ها در بیابان به‌جای ماند.
🔹
دست‌کم یک سامانۀ پدافندی تاد که از گران‌قیمت‌ترین و حساس‌ترین تجهیزات ضدموشکی به شمار می‌رود، به‌کلی از کار افتاد و منهدم شد. یک فروند آواکس دیگر نیز در جریان همان موج هدف قرار گرفت و سقوط کرد.
🔹
مرکز تعمیر و کنترل سوخت‌رسان‌ها که نقش حیاتی در تداوم عملیات هوایی ایفا می‌کرد، به‌شدت آسیب دید و عملاً از مدار خارج شد. حتی ساختمان‌های اسکان نیروهای آمریکایی نیز در این حملات تخریب شدند یا دچار خسارت قابل توجهی شدند که نشان از دقت بالا و شناخت کامل از موقعیت‌های حساس داشت.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/461487" target="_blank">📅 07:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461486">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هوای پایتخت «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۷۷، و در وضعیت قابل‌قبول قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/461486" target="_blank">📅 07:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461485">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd8cc0bb73.mp4?token=T-1_oXp2gJ2n4MtmGftr3FXCO6Viws1oev7G_Xnw9mP5wkmALr0xRXYXoeAAxQRkobRQF7fwpEUK4xadr1j0GjnPNYxjSN07fg9X2p6wPQE5Cf6KNH-OaG3nOFFLHzISXUeAQ1_FLsFMZNRI7aQwKEQ9hTJ_7FoDtiEXeF6MFFgutHREDFehrj9vpr3iB_sqzJociI2wrhU4l7CdrLGlnG0nSQGzBuCIgPzIcr4Vk1EUn1jFvnZw5J1d2t83ux2ohReThNL5tiKqWOA31EHubnraweHDVH-l-x5bcc3xqu8bxA5YxrWR5dmAE2DCMI7OU_gb7Vkt3ORWdDdU9ZJ_SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd8cc0bb73.mp4?token=T-1_oXp2gJ2n4MtmGftr3FXCO6Viws1oev7G_Xnw9mP5wkmALr0xRXYXoeAAxQRkobRQF7fwpEUK4xadr1j0GjnPNYxjSN07fg9X2p6wPQE5Cf6KNH-OaG3nOFFLHzISXUeAQ1_FLsFMZNRI7aQwKEQ9hTJ_7FoDtiEXeF6MFFgutHREDFehrj9vpr3iB_sqzJociI2wrhU4l7CdrLGlnG0nSQGzBuCIgPzIcr4Vk1EUn1jFvnZw5J1d2t83ux2ohReThNL5tiKqWOA31EHubnraweHDVH-l-x5bcc3xqu8bxA5YxrWR5dmAE2DCMI7OU_gb7Vkt3ORWdDdU9ZJ_SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراض رباتی!
🔹
حدود ۳۰ ربات در مقابل ساختمان وزارت امور دیجیتال لهستان در ورشو تجمع کردند و خواستار نظارت و قانون‌گذاری بیشتر در حوزۀ هوش مصنوعی شدند.
🔹
این تجمع با شعارهایی در حمایت از تدوین قوانین برای هوش مصنوعی برگزار شد و نگرانی دربارۀ پیامدهای گسترش فناوری‌های خودکار و تأثیر آنها بر بازار کار را برجسته کرد.
🔸
حضور ربات‌ها در این اعتراض، اقدامی نمادین برای جلب توجه افکار عمومی به بحث تنظیم‌گری هوش مصنوعی بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/461485" target="_blank">📅 06:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461484">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwvvQXl6TRZH07-ExXUMEwJyba-PAKhJRJ1sgRtw-ST8U6DH4ZRHlQ3Ka-1QHPd0ojiPpCohO2uolIpAJW_xCewX5IOcqyEtkHAQujGmAzb5ULWHaa_bU9_48YK6-r3gpsSCn-b6uM67KWuE1U_bsLGNRfi1kS3CZ4v2FedBBiFCnecptgAk8mZNmRoeAFvRz5XhTgyEY4TcwCvfzP3Bf6KvPHVbh479O7c_KlDmFgQE_9oIPC7JYhuxunQOh_UcIfgUsH-oa0Xa4qYGRGITBKeSxYp-FFdj108CIgwa-1fifF3It_FRXl5RWAoNkPGURytGaoMArMK3vIvWWa6JWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آژانس انرژی اتمی: کرۀشمالی یک مجتمع غنی‌سازی جدید راه‌اندازی کرده است
🔹
آژانس بین‌المللی انرژی اتمی اعلام کرد، کرۀشمالی یک تأسیسات جدید غنی‌سازی اورانیوم در مجتمع هسته‌ای یونگ‌بیون ساخته است که می‌تواند ظرفیت استقرار حداکثر ۲۸ آبشار سانتریفیوژ را داشته باشد.
🔹
آژانس تأکید کرد که برای رصد فعالیت‌های هسته‌ای کرۀشمالی از تصاویر ماهواره‌ای و اطلاعات منابع باز استفاده کرده است، چرا که این نهاد از سال ۲۰۰۹ هیچ بازرس مستقیمی در کرۀشمالی نداشته است.
🔹
کرۀشمالی بارها اعلام کرده که جایگاه این کشور به‌عنوان یک دولت دارندۀ سلاح هسته‌ای «برگشت‌ناپذیر» است و آژانس حق دخالت در امور داخلی یک کشور هسته‌ای خارج از پیمان NPT را ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/461484" target="_blank">📅 05:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461483">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBINGIHpCtsbPRoM0vdhY6Hqu6X-TpVSYjD_c6oqHzMR9faWnof90D98nOy8b4EJNtTgOONRdJ0Aa1SWGJQ15WercaO5-hQioRWkqVoB7m-bl3bEMMg5RkW-kKVg45FGN8PShysZw_3RuOcDzIwhAB6ROtNArkN6s6AqqnqpcCtozzPP_TxCZoJ_pQcvx-R0b1J5Bu4v-y0vtk2n3i1V-BZvK5wouR1-aCTAZ8TCaMro9-JR0LIcR2GezcI7dR-AwmsnKR2o4Z5ceNT6Yc_fB26XvmCrwc_abXIb2540RM90myN6K3vhkokSw3TU0RmbAuaWmyqK7-Mp-qNTxyolXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چت‌جی‌پی‌تی برای یک پروندۀ قتل شاهد ساخت
🔹
یک وکیل مدافع در نیومکزیکو برای تهیۀ لایحۀ تجدیدنظر از چت‌جی‌پی‌تی استفاده کرد، اما بخشی از اطلاعات تولیدشده شامل شهادت پلیس و شاهدانی بود که هرگز وجود نداشتند.
🔹
دادگاه عالی نیومکزیکو این وکیل را به‌دلیل ارائۀ اطلاعات جعلی، ۵ هزار دلار جریمه و به بی‌احترامی به دادگاه محکوم کرد.
🔹
وکیل گفته بود تصور می‌کرد چت‌جی‌پی‌تی یک خلاصۀ «ضدخطا» از پرونده ارائه می‌کند و از توانایی هوش مصنوعی برای ساختن اطلاعات نادرست اطلاع کافی نداشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/461483" target="_blank">📅 04:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461482">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c24f8e1f79.mp4?token=qkBOjduJO6kvlHYOWXwkSOIa1OU5fqL6hIWfIrrECnzgBGknDNSHyy3vkzkD56FGUKgtpMIrsYi6aeFx8O9LxEJeFrpBS1oo7OUGiAbEazXF8hgdRWEKaBdHnsY7Zblcc8p-_LlSp4FExn6_Oz34FIin9uxhimqAbAluXDvz1kpXmBCJbUmOcBtNLlBuRkqjmBOLASE-V6GsBazMPhXWgwzX3bQipK03JDWhX2DzUcYuc8qpwPHWwx6pdFJa_3b8JJ1NuE46E25QckDac1TNtupfhyLLm7VTUjIbvLPk9BHNncwYSIlF0NAT726VOpowJn4fudWCN1Ya8UTYWQFnDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c24f8e1f79.mp4?token=qkBOjduJO6kvlHYOWXwkSOIa1OU5fqL6hIWfIrrECnzgBGknDNSHyy3vkzkD56FGUKgtpMIrsYi6aeFx8O9LxEJeFrpBS1oo7OUGiAbEazXF8hgdRWEKaBdHnsY7Zblcc8p-_LlSp4FExn6_Oz34FIin9uxhimqAbAluXDvz1kpXmBCJbUmOcBtNLlBuRkqjmBOLASE-V6GsBazMPhXWgwzX3bQipK03JDWhX2DzUcYuc8qpwPHWwx6pdFJa_3b8JJ1NuE46E25QckDac1TNtupfhyLLm7VTUjIbvLPk9BHNncwYSIlF0NAT726VOpowJn4fudWCN1Ya8UTYWQFnDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از حملات پهپادی دقیق روسیه به نیروها و تجهیزات اوکراینی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/461482" target="_blank">📅 03:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461481">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97bf68b8d3.mp4?token=ZwWDJHrBQj53pHDsez8vTeuJ4tyszSvkuTsSf8zwChMUQLptCbEuKR_OBoxaEHLOUsBcckMcX0OFLsAdW6lFnv6DYt3_g3WH_Ah8E5le8ePzV5It0cXaOtVY-GYHat7gwMpzKUa6nfK30B07xUYagS9kLXMSbZ3K7IaWLdn3BReK3UfkEkyrMEdTygDgl_OUe28yH6ZPCdXpSO5vaB4V9ns-O6PNYtoxeUMzosLZysurxbLvDE4-aMD-TGiAm22k_-UXxccxf0uO1WEoZuXhV8P2Z1TXkEaN1KCrTyjvvLYcMEpXucxHcOn5gkIHUkz_8YO9r88DsO90k8wYRM9tFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97bf68b8d3.mp4?token=ZwWDJHrBQj53pHDsez8vTeuJ4tyszSvkuTsSf8zwChMUQLptCbEuKR_OBoxaEHLOUsBcckMcX0OFLsAdW6lFnv6DYt3_g3WH_Ah8E5le8ePzV5It0cXaOtVY-GYHat7gwMpzKUa6nfK30B07xUYagS9kLXMSbZ3K7IaWLdn3BReK3UfkEkyrMEdTygDgl_OUe28yH6ZPCdXpSO5vaB4V9ns-O6PNYtoxeUMzosLZysurxbLvDE4-aMD-TGiAm22k_-UXxccxf0uO1WEoZuXhV8P2Z1TXkEaN1KCrTyjvvLYcMEpXucxHcOn5gkIHUkz_8YO9r88DsO90k8wYRM9tFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
می‌خواهی کارهایت درست شود؟
🎙
آیت‌الله مجتهدی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/461481" target="_blank">📅 03:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461480">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌ ینبع عربستان متروکه شد
🔹
بارگیری نفت از پایانۀ ینبع عربستان واقع در دریای سرخ صفر شد.
🔹
خط لولۀ ینبع یکی از خطوط دورزن تنگۀ هرمز است که مهم‌ترین سهم در عبور نفت حین جنگ ایران و آمریکا را برعهده داشت.
🔸
روز گذشته انصارالله یمن به خط لولۀ تغذیۀ پایانۀ ینبع…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/461480" target="_blank">📅 02:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461474">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sW-Pih1aRMHSlttaYn-NJjgilLE3CVckE082EeWYvp4RSMW6u65QHPMAg104_GHdnYrKXP_Dq_VIgcawX7ryeXq1hyq9guWlEzanHnI_4eF5s-C72iFlwl5hZhC0MmNhNkrbbHPNo6-hAy8xJ0GUYPgzKjck7EYeDjzuJQGDZv1XvN9a_-h9D4qVCnk2aPMPb3fnzQyorDVvUml1Wwodf81hNik6MyUBel9Zv3iVzgFqxZjduziLEGYTa2Y8n9yJtxn8zWpO_iuWh_NSfm1LZP8GlqiTb_ngc9NfoOkNg_br4nCqCXk-H2HFPilDfy51waI5FA8IGqDp88STy8mNUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m17RUL0yR9S4JE3TJZPQtcKUiROH9YAihv3Hf3BJlZmhqKT3U_H3U7BpMRorJ84c7r-3NF78pb65txhd0fvSl7XEi_Cn1qACRYfWIkM2SchC9XlwS4d0RlmrZJjFfF-wVaoymUyL4IS6JSCg8o1mqEOsNvisDXS2D1ogsW-oI3XIAnYk8b2qZ7NdJFKh6oWx8qloCx18rgSbIJcA5BP7b7Udz5O9T6fNpn8zyEVWpIb1EBIYzHRs2Av2jKyGZjsCIU-U2w-GnFgmEXlBwrRCRqbyNSQkJvIsGs-kOzq7V4lApQijnYb5TcTRwuUTKpghmEkEPHf9ulb3PCu8Xwf7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vx6oKBX2t7uL66nxUaAtpu2YnCm4f8vK3Y00ZA3GPU38kRW8TWKstxvfaEs6_iXCAb-Po8LFK8DwQxUl8E1kMB-7nvDqjwwQ0GpX_VLAUmAatFO6FsLarrVkqpqLYSIJktzRFNZ6MHiSNXY5z0pl-TQev2vx_Xj8Qyyrv4WuQOwnbmFw5DLR8Lms56ezyq6ySivMGY8ppajzRzamJvYEaOCz2R5pcYvIoHjkk-tmDaBo21Q7Geb3Cu-9byhe8-LBqXdLm9ZnpPc4eV2Yg7lD0D6j-U96hw4lAnARmE12iGyh1EtnFtvrOf1rk5Tw7v_ohJVxSEyuWPunvIjDZv6Yww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/grcHF5bszEqK3W3Pqf5AyxcoM4KuZn_ufaUMtQhj-h2YsytW8ubzhfEz8-pYEfcfnZtShZFQH4AnfGr8fvcjQQiWDWW4Iu-AXA5WdjVK7ZmusQuYiP9Qm_nu0pyKCcEo42Od7nTsWZa0QTz4KFnNhT90ALoefT9RFBqdmpl1GdTGFQS9QpULARdtwCMTk-mkZjimrdyWaKNXzt8487t_o4LOAvzi1l8UvytvdomO2DlxG4PLG4GEdgRNBc9Dyzt3hQR-eNgfdFjloY4Gos2QlMxSTnBwQDm2CR3xPkUu32YrDTzNLWzoAYe2mSCppWLs8pb91iEfT1WZlt35S042cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lVn_6HZ6gwgFHmAOukOCeLE1PNhkXA2sg5XPVvVu8YUEmMM5DnMtq8U-JVTqi-9GXTUcgpTZEqxeaf3UnI1U60mpX9dr0muH5jq1Je4ZYUvaN5wcJE50bt6HdGb5Zc0bNGuN1Sk1jF2M9LAUzBkbV5W_4HXBcjmE8FJ0ZC4dKEyO4rCzm65gkQVA_iPckt4_Z4wD2gqkszCP1OGk-3vCcy1V7LOtn1BG1MOSkFy6cS8KGPwYSIU7Jh5qltDKQFkSEwY_v1I3NUsaoZfUsqHd7aT_cl3gefhPXtWrYnUxHMstRGmJMIoyAp68OLE-AtogLRK_NB3JoCPfuFNu9Q12JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RUKO2K4I5ZEGHjv7YN2pcX9YY0Ec_3jjg1VeWbwCUUhh2MKdLdsXQ9SyORKZCwn0Fewh3vbZBUmY67hn6EvNf5BmudqMQpdKXEqEHRJTKwcOZgn2dsonEVo8R9NibrS7mOOX9ZEHrRlB3Ft7cJaciRI-KRj44tJTCi5HK-itvlEuwYNHCzPO0BlrhZygFFszbZFVU6koAP5BFcfpoSBKBvKfZtDopJAFcztKvLd96g9T2olo8DJdTBhVCWRtMJLdJ8FVIEFl5hPqQeNMV243tp06auhX3k5SSDJO0n3ZQHtdVIBpaU1Nw1LCNeSHQbh-8uqHUqWe2T0ncwSVRrsWCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
میدان‌داری مردم تهران در میدان انقلاب اسلامی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/461474" target="_blank">📅 02:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461473">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdtxmQeHUbcl3cKEay7FSTf0noQW39NCbOnsgLQQ_n3SC764SvwJsFpYCJ0nzZAoDf4kgGGTvREu5ozd30f9Zc8dQlkj9ifw55rR6EFfb9gCAUzf1kOf5GbbhzBbXCUHNM_ZftMTTaezbtcp6Gsf6kAOp5Rr_WYMP_v1xRnvWcd3R86uKuE3pXm8H832RT2vkvmTmBWrXICtnSwHzrou71cgqdtXf2M8v4CTEQGgvG67K4Bs7neY-s6Ve0YLw5n0nyrnRsd1lDgV--SrGWDlyXVDqUzV7mz9MjJuU01y2YFynHSuO18FIeL0yUrRtk28k2yZSjnhrCAlSsTZE4qpOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت اطلاعاتی آمریکا از عربستان در یمن
🔹
شبکۀ ای‌بی‌سی نیوز گزارش داد، دولت ترامپ در حال ارائۀ حمایت‌های قابل‌توجه اطلاعاتی و کمک در زمینۀ شناسایی و تعیین اهداف نظامی به عربستان سعودی است؛ اما فعلاً برنامه‌ای برای انجام حملات مستقیم علیه نیروهای انصارالله در یمن ندارد.
🔹
دو مقام آمریکایی در گفت‌وگو با این شبکه اعلام کردند که رویکرد دولت ترامپ ممکن است تغییر کند؛ به‌ویژه اگر تهدید علیه خطوط کشتیرانی در دریای سرخ به شکل قابل‌توجهی افزایش یابد.
🔹
به گفتۀ یکی از این مقام‌ها، محمد بن‌سلمان روز پنجشنبه دوبار با ترامپ گفت‌وگو کرده و در این تماس‌ها خواستار مداخلۀ نظامی مستقیم آمریکا شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/461473" target="_blank">📅 01:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461468">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHntnY9PaDwX_i7kciVK7CWOG3KPacSGkpInGrTM1XTlQoSEgY9YCWEFgPERcENcmpcWmoWjBc7QYvT-9ZGaziRdoIYjxSw9jw0VBODwCP-OSq8c_qcISXP8faGS5MSaEPwmvFpJprE78Rvo5ANurbPv5-DJFfe7JJZkxaWWszrQrlXulA8CNHvfv6FN_3rk7rgCxuMXeQ6NEs2nZA4TElHUjz2eZ1rOnMm08JMwYNjubXwEExQd09m_gZ-vTWnIzabcGyIoceCmVyi9uect3BnwAXSGHnnw1psaNhh0mqUkQZxhS0tPY8feDtFTzkvx1A8UdPnyv93yHfba02YyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ce1J8U5EtHKdne4Cd9uD-jbDw2fmL7pUfUcU1kz1myIynHbeYXKX6U4hldkq8vKjof567cFwdSUwTF5NAJA_ubKf0lhU6xja8P074kfHPTIgFyGMBH-iGwekXqdxyQDJeY1F6S47qlO7zJjRK3taWls9fk4-q_CRxEBhTnIpLNLQ46Oeq3GVVYcUSngtnKc3CwMKQJ2FXSd2lDtV8fShAe61Sfri11lAbUTc-mRtuKL3CfHdEihLUezuLQytO9x53Bjk79Gibz6QHN4z6f_FYUT1WyXMLzS_MU3Q40l9wBhDv3fE_WXMuAfL39kv6grbL6_NtleKz3exOgGk2MLW0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vj94lLT6QWEcBNgJG-gI_d37tZ7zt0Vcbex5DdpnpA7E8-hDBYpQOUdg5Mx_jggSwyBPOSRWjTCnmAxU13oAX7ZHTwNKqEnUgkFDXvL6ymd58Lx95pl5le37dJX-gHo_Z12JEa317C-PpiZdrP72ZSKnjAXG7xgLk9tQKQedTJjsZpnDf_fahjhf1aoNSzTFJUnLImJDm2rD9abwG7pigs8xeDgJ1FShUatgXh4L9FAxlcXNOv4xgEfz12Vxt62-s0YzAU7Hx0Z6vGoQILuKnSYDfZEebl4OcvdBBZFA8PzvqhYSpYybHoKyQXsM3ONHUxjNYX94BDCMi4OD0r3sZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v0lNBt12HKIe6la3qViwHrIBqKft1zzP55czzY2bwITfdB7bKpDGopSvUF8wW62PPNslgQMawcnl5WhOCaIhGcuynUOF1Ew2CQ3B4oSj8HkYV60m5M7-HgwOdBUl9WYT2yDn_NEDrfGUxBQykIvKj7I7cGuUIq4TxyY0DF59z1YvRbOvgIHj5mF4sACw3SOc3BQv-sc28MVSlZWmkI4q5DYRqOZJnaYj0MxajZZCzgLvImLIKxehVDunvmPXV2p2L0w8K2NJc9I-QqjGXoHR_DApUZLYahly0gTKSoLeGSzpxkvS8wU7JpPmEEU1IwJ6V_DyScyNPcQanslAXxPShg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QneU9sgO2ZBxdbYeKVofqFB-oS9ZwG8FF5fpA7I-QbBj97VHmdUSLNDh_1rikg58bkILKxMqAbweEPPMn21BStL5dqYIQhni1AsCkrfBIzyMIqcf5_lQGGlzGvdQtgZjB7Q8NaUaCd9l-uOa4by9q9C9Fz2cYAinbuGCsY8ykK19qc3h6qe-HQk7dZi5ySnLegNl2_-Y11Wz-rlOcgy0BiUasNih6NjagbZMPraOPlU0m60ciGX6mdsuWNknWpo_sfDc0pQ2rp1OZ4w0oBUAHTgvXRJrCbaH2ZEfuz0psiis1fsOY_tx3iSN0_eB7PWT7K0-o1fnPRK392k-GGRTFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۲۱ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/461468" target="_blank">📅 01:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461458">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c7VgoCkUQkyymGrHEEWI289XPqNGAMPm1i6sqxsE5z7On0gyS8ZuSLWHb-XSYr_rrsDqYLbulTJTE5mC8uk3FJEdmhx8oiUQr-mSlYXndx8JRGmS3-T7-OMRbK5zNIguW_XZ2SeiDatf_EtzNgS2ogwyIBabd2y_CrCRmvPx4XLXDswFxDutkAYQZnWhcDLF5ET5-lfgXvU0wCGLDhbEF9H-0LPu6VkloNeK8kS1tclN8fFdvDxIHF-KP13EAR4ip0XEaj0yXz3F853qQf5hx9SgQ8a6VSVsM5Qsigut0INxFNhhV_YUUBxJ07jc_riAbnYEgcdN6k3ftH-Vq-OgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lKekRnBcQwXmsRynLqp9NjYheBW5bZ4AFNYrab60QMtyLBWwQiLi2awOzEnUTEAfFBOD6azl2RnPDWVnQVeY7kErBydLkGa_Lg0W7B7ek1DNKXXdBAxu8IHfuW1QcL3XiFxe6VGQHiS5r4ATpNyIdROu1ATg1absRUaxP0tx9dayE1R67_DfkL9Qbxf_ZL1DbzhauVbscbiFIuUFi3KyjzuFGsjCAe2xT5YRJtY1DURUTUuNsaLyTreWuYZp88t4P4Um3MFzqV37XUVoJA3Y-DuUClB2rd_rqiKIh2_wifkh_UG5TVYX0TV5_hGq61uGVICEoravddAvavKgxtx57g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_J588d5udLy1XiaizfvNyEWwwqeXZZgZGdhn2-0miY1TnV4UVa0_L44GkyQTMRZ9WlXw1VuzTtVhmX7I0XPH0JfbC0soRCjg-0UWIxh6tdxbWsIkddSmY_SyJSGRnw7L1Hig0YUQ-dl0q_pl8ocsDy6cUhbLUQ70HSC72CIKSSyqTdaYecUP55v5c_t6EyI4llzqDEaQToxcDsJF7hJiIQQ-G7JRBz-HR16NBIjFhEcmX4YVLfMBIwQpHHEdhOzoAD4G1gBV7phjad88xRhf-NfBq0KSmLjL7GyQkvTaEO7lrjqrAzuAd2cBhggGUwyQcOqyHM6eUry88iKpa4mjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keKFRdbaa3eb46p7NgPX5S9mk-0D2pUYMDMGeHbKc-aCjxsGqG-L_GgOwZRNipRv3ytjBB3g0bvP-muHL99YZDSb_vYBUJ9XcGWQVWLy03cSajBFPLh-UVxNJXUbcZ_C6QT_kT-PQRBdSnKg8IqmP79K9FuZpqaQTXs83qhe27hJE6EuoOYMzvFhBwj7ykDMIt5uApgTjiuFIXJMygoRXyB1bldupFDrMZSUwz1xuBzvj3QvC2O-_0jwPP1YsEWgnvihtyzYrZjwY8kHjgwLPeg4-y-ggytFO3wxkfz7R2EspIgca3xTpxStUjiy4nJhwy08PAs2a072QJxh7rF4wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NeAySWeSH0vddlkVRp-DWT5MiS17XbzRTvMMf9yx8gDjfAchd0CRFoC-Hg5rWadVDecqWKE0sqt086OrV_V6j2AMG2nobl7IqynZql0ktdrM0o-h8_A09_IW3yHP3WiXWUIZL7ui3Mq2iEYBRd8gqz4jMzrU-Yox22cJjOVeMhEYTP9Cmd-rEw4-8uu7snIy7y5l72h9cOIp4m4_XUeEWLN-9xrkF8BF1dqkHY516tz2NEXiNIlWh8M_-ZoOvFiP-eVwun8Jes7zV0F_lsA9CQfx5I7gT4CPDobyFc4paUZ58JMZx2qoTYJdReGK_uW3dzL9eyd6TbqsXz_5nNW65g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGME0P7RfzztRyMQddHTMfSUz0YRmSQZ8vNLzcnc9vw_BhqrEZTP76ducW8DwvT8YPo6psNgx93YjY_F_Jq8J81wUfwrVqUvkWcPr9_c80Y9CAbZilBHx77OnGptI93_2QUKPk0hf2lb9BddJeb05QV-bmnE_cKQjzLb7rju1QWUDV22T_c5uw6OKRFZSI2EHmXBD6lvwrPykt6ItPMW5z07SnCVv7xw-NiXJf7Sc31wnG9NF2nD51tPmWO-6R7EnTbLCp-bew-JKzaWSaOZtaVQhcqXMiLBnRSDmF4UZjmD-iH6rHjiXr53heAWuQ5LWJpgfVC3QPUJaVCVd3QXzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DClk8yjt1hHxsoCQCpEIF9XiOndZB6WBaabNAU1b_XIgH7eFlWJNWDLFviKb2ArW7MpzHCauMRgEmxYCgocVZT-lo_6Vog7QcevjYAuQp1YAaubxPQhAqXKVQXbVvAP5yQS0PTww4O3_vfIUZWKuSerqgXm2-KmxEY7vNtx1OZcE3nV-2f192AkcQk9FhjaYpYJEahaxdf8lPzwYisPvVM_IPR044BSlaDBL1cnSpQKKIh0xHUbr0LM6HWXNAx3zD3JzwEyM4tMdZQ_pljg0_9Qfy4OrhZks5OvrqZYdIiqMun-ZEoryb63y6-IOvZIEp9dUQ78QyBBI1Ht1vKxUJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UO125AEdGryQnC7Fb_LVVyhw45f3MnHJSHyF3gxGfjj23mwLRL41-4KE0mqE2jeNAzCjpxxPIlaPBj7Zre56ktrhB6RhsBnDxlxR4X1vRqmi9H-X0daItu4GiqXMiSUR4YjVYuL5gNyeacGPskKcLXQNpkey7BsoSy9i07dy6bMl-g3ZPVdT71bIQVBGIX4v7sJfCrRaH7CVxkwks3yhIDWKHCiLOX31kE12IBtG34yw7fxW0ZCrWH1RWtxMu0M0AiDWLPwnYwRZOseSfFwWhVhhp3SzGkSdT5A3c_qsb7tauhzK6PMoHm-D6LK5U24mcG1utsxpQhxKe11TCv2clQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDLGq5izISk7wUkaqgVnEf0d6mkZ1xO369ZFMf4_AZUqYvc26tLfUKXL7xPSATxeWNw9xO3fo7C2-RYrWPuBSB13WoF2EUkErEWgD6oGy8uRqhRKULYS85jY2f6xqsOetZSPvAQwfBwHPpD1CcH1cpFt7jjogxa2m9opXISk39kQysX_t_42m_5F4S1YhFm_eyqxA7XRSRrvsUzHsj6fT2SwRG2rzS3IrIrRISII_-dAS80zDf3yh4faLFYqxQ5er8q900P7jdU7M3ageAZuElGw26lZbBCXm6Cb5K2kI0HAvyretTKvxMd9WZ26JQxdN4AhTmXZLoqiyyl6GgITew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MRVEFsjDcAd-XF3Gb19dzT4DNjLIv_nubJn5gPfsy2yA11pod33bHcSyB7S0BisXxceinUAoDK4XdfKcie8k4hvBqd8GvAB8fcMEUfVTgRIlYWYuPNJQKP6vdvQMLuzBjRZgdObYLcvA3rHMvZb503r9otIukcd8-3Q4n2wVfoZC-Ig6b6L2z3im4c8zdS4YQT4Mx1fDe8_Hw9zZVhD14hOS3R4CrrvZavGu3ksfqqVHLB5pJmdM3cUkWYWXtP5ldeQDVnP-8u8pR-NymxnrgRly2p8OmXctHEMQlqFJR7xO2KbreBGscCZ7oLm8PJoz5ILvmtOsVPj14ujpKFULUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/461458" target="_blank">📅 01:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461457">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhfeY1WHycbWTXAL_aval-f3LKsiIgUGv61BqHjr5Wqj7YG38qRDwpBGxYj3aJisx5TeJ6T7FwVtB7BLQtfOCZihDS-Q5wbPlck6MnYvie2rCPB0O5AqLb475jU1PVkzJ4JHcaRzBMcey5qkF-jc5YqFsuCdgRJD4RFLdrAugZWy_RHuFYejZTLkx7BavIGrK_0XleC2xROJ5Re3D_4jzZQHLGE6XNB6xELWpSjkeYOaXC6KFpDBY3gOh27AVCK9JHOB69p8dSeFohpBmXoWrdVq2R--rdX-Rg35n19WtCA42VgZnjR8y9-g-Sk3ATb0JwOjDsAO7Rz2zsMZlnBLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: آمریکا به‌عنوان مربی و پرورش‌دهندۀ اصلی تروریسم در جهان، فاقد هرگونه صلاحیت برای تعیین معیار دربارۀ تعریف تروریسم است
🔹
سخنگوی وزارت خارجه دربارۀ ادعاهای وزیر جنگ آمریکا راجع به تروریسم و اتهام‌زنی به ایران در این خصوص نوشت: روایت وزیر جنگ آمریکا در سالگرد ۱۱ سپتامبر دربارۀ تروریسم دچار تناقض بنیادین است.
🔹
نمی‌توان جنگ‌افروزی کرد، مرتکب ترورهای وحشیانه شد، به غیرنظامیان حمله کرد و همزمان مدعی مبارزه با تروریسم و تعیین‌کننده تعریف آن بود.
🔹
عاملان ۱۱ سپتامبر ایرانی نبودند؛ بلکه همان کسانی بودند که آمریکا خود آنها را در دهه‌های پیشین سازماندهی کرده و پرورانده بود. پس از ۱۱ سپتامبر نیز آنچه در افغانستان و عراق به نام «جنگ علیه تروریسم» انجام دادید، حاصلی جز کشتار خیل عظیمی از غیرنظامیان بیگناه و ویرانی گسترده در افغانستان و عراق نداشت.
🔹
با این اوصاف، استفاده از سالگرد ۱۱ سپتامبر برای توجیه جنگ تجاوزکارانه علیه ایران، جنگی که با ترور بزدلانه مقامات یک کشور و هدف قرار دادن غیرنظامیان، از جمله زنان و کودکان، همراه بود، تلاشی شرورانه برای مشروعیت‌بخشی به تجاوزی غیرقانونی با استفاده از زبان مبارزه با تروریسم است.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/461457" target="_blank">📅 01:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461456">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">منابع عربی از وقوع انفجار در عربستان سعودی خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/461456" target="_blank">📅 01:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461455">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">منابع عربی از وقوع انفجار در عربستان سعودی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/461455" target="_blank">📅 00:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461454">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lf4c3kPbHH3iI2qJe4ducLOdWqs3D8DSM_rXE_0ZF66SYoBaTvL_BfIY8LWRziop194Fph-qpxBEr9-zlfJsHWTmUHL7oCZuZfVJ1KGXKD_h3-HXaNuY7GoNOuNJmmcs9FsQQzJbkPgGqfM9T9yP_67S_7nSoxRvbJlYlbAxqTchS3rkZyIVNeUzQihmnLoFGcgsDWw1z0dGg4Yu_kXCxeAeytXgl_77jzUiHmeU05O4bO7fKaiAZ8u055frAA9AiAq4g7QB8BgwbW6BgQyqFSOmz47nClOPsduFOUV37_jMOPrKdPvCPrmg_zQeCZol4z85sVCgRyqOG2OmTMCWDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداداد عزیزی مشکلی برای همراهی تیمش در لیگ نخبگان آسیا ندارد
🔹
پس از فحاشی‌های خداداد عزیزی علیه امید عالیشاه در پایان بازی تراکتور و گل‌گهر، او با حکم کمیتۀ انضباطی فدراسیون فوتبال چهار ماه از حضور در ورزشگاه‌های کشور محروم و ۲ میلیارد تومان جریمه شد.
🔹
با این حال از آنجایی که حکم عزیزی شامل مسابقات داخلی می‌شود، وی می‌تواند در لیگ نخبگان آسیا شاگردان جواد نکونام را همراهی کند.
🔹
برهمین اساس، عزیزی امروز همراه کاروان تراکتور راهی دبی می‌شود و در بازی با شباب الاهلی در هفتۀ نخست لیگ نخبگان روی نیمکت تیمش حضور خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/461454" target="_blank">📅 00:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461453">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‌ عربستان حمله به خط لوله نفتی خود را تأیید کرد
🔹
وزارت انرژی عربستان خبر داد خط لوله نفتی شرق به غرب این کشور در ریاض و مدینه، روز پنجشنبه، هدف حمله قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/461453" target="_blank">📅 00:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461452">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aV3-TZduaK25oxQipXHCISxpZ6_-nv41tKtm_8XkIXcFGz0KzDPDf2wWduesanX0CAMyYndrWNiYc_v5pWlhLC9l_FoNfUl4SMMGx0vcDGGhNrqyMoJfdlvRIhsy4yQiVFU01w-9Ip5-VqFTNSMjI6EVZHBsEn3-_-8EYjaEuokBN_3YSg5eSeJS_jDoFVAqELvX-0I_myXj_W1PsejY8FdxlCE5z-lbkGzmRM8sHobK_orSv3I0VTcWIv2l-2R8AoYi4qDoO5bCvWlx7FCPr4OvwPekYQoSV9FujQxcc-MuzHLEFwrk62Xqchute5gw2S8gR0dYCQ9WLolaMtLc4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت وزیر سابق نیرو از قدرت مدیریت شهید رئیسی
🔹
علی‌اکبر محرابیان: اخلاص، تواضع، بردباری و مردم‌داری از ویژگی‌های برجستهٔ شهید رئیسی بود، اما نمی‌توان از هوش اقتصادی، حافظه و قدرت مدیریت ایشان نیز به‌سادگی گذشت.
🔹
در جلسات، شهید رئیسی نام پروژه‌ها، اعداد و درصد پیشرفت آن‌ها را به خاطر می‌سپرد و روند اجرای طرح‌ها را تا رسیدن به نتیجه پیگیری می‌کرد.
🔹
یادم هست یک بار در جلسه هیئت دولت، من درباره پیشرفت یک نیروگاه در جنوب کشور توضیح می‌دادم. ایشان وسط صحبت من گفتند: «آقای محرابیان، جلسه قبل گفتی ۴۷ درصد پیشرفت داشت. الان چقدر شده؟»
🔹
من نگاه کردم و دیدم واقعاً ایشان درست به خاطر دارند، گفتم: «الان ۵۳ درصد است.» گفتند: «پس در طول این مدت ۶ درصد پیشرفت داشته‌ایم. برنامه‌ات برای ماه آینده چیست؟ اگر همین روند ادامه پیدا کند، به موقع می‌رسیم؟»
🔹
شهید رئیسی معتقد بود مسئول باید نگران باشد و برای حل مشکلات تلاش کند، اما نباید اجازه دهد این نگرانی به مردم منتقل شود؛ چون اگر مسئول مضطرب باشد، مردم چه کنند؟
🔹
در سفر شهید رئیسی به خوزستان، پروژهٔ آبرسانی غدیر که اجرای آن ۵ سال زمان می‌برد، با پشتیبانی و پیگیری شهید رئیسی به طرحی یک‌ساله تبدیل شد و در نهایت با تأکید او برای کاهش زمان اجرا، این پروژه در ۱۰ ماه به سرانجام رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/461452" target="_blank">📅 23:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461451">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">سرپرست وزارت نیروی دریایی آمریکا: ایران پایگاه ما در بحرین را کاملاً ویران و نابود کرد
🔹
عالی‌ترین مقام غیرنظامی نیروی دریایی آمریکا تأیید کرده است که یکی از پایگاه‌های کلیدی نیروی دریایی ایالات متحده در خاورمیانه طی درگیری‌های اخیر در جنگ ایران متحمل خسارات سنگینی شده است.
🔹
هانگ کائو (Hung Cao)، سرپرست وزارت نیروی دریایی آمریکا، در ۹ سپتامبر به نشریه «اپک تایمز» گفت: «آن‌ها بحرین را کاملاً ویران و نابود کردند.»
🔸
منظور او پایگاه پشتیبانی نیروی دریایی در بحرین بود که مقر فرماندهی مرکزی نیروهای دریایی آمریکا و ناوگان پنجم ایالات متحده به شمار می‌رود.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/461451" target="_blank">📅 23:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461450">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afb66bf6c.mp4?token=UQbgf9rCWwVDH4jDz7zevlooGOiqALRcW78RxzmrG3ItoqzEzHjrpaKNGU66cEWH-MkZG9mkMMFqdSlkHHe86-hiLACOYx2olYBYiesBaccofSVVlex0BZ_XpvkGbc1bid1ZI9jU9Y676ep2T3sk_BE5BoBgzNjnAxMA4FuhPvK-lIbuVmBJHl_ALqHHIHXUc0CxKFN4y6tFJnKWSaFsbQHmBwKU5sZd2JHRBPlWpRHuhGYovmeGqRgYw2kMoqsSf0JQZeFupV10uLVM6vXrPky31n33vtV-y5L7zROncEun0QyDcvMVn58RVKgL0C1iIAUeU3D4XDfq0sX_2dCSfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afb66bf6c.mp4?token=UQbgf9rCWwVDH4jDz7zevlooGOiqALRcW78RxzmrG3ItoqzEzHjrpaKNGU66cEWH-MkZG9mkMMFqdSlkHHe86-hiLACOYx2olYBYiesBaccofSVVlex0BZ_XpvkGbc1bid1ZI9jU9Y676ep2T3sk_BE5BoBgzNjnAxMA4FuhPvK-lIbuVmBJHl_ALqHHIHXUc0CxKFN4y6tFJnKWSaFsbQHmBwKU5sZd2JHRBPlWpRHuhGYovmeGqRgYw2kMoqsSf0JQZeFupV10uLVM6vXrPky31n33vtV-y5L7zROncEun0QyDcvMVn58RVKgL0C1iIAUeU3D4XDfq0sX_2dCSfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ سخنگوی وزارت خارجه به انتقادها از برگزاری نشست ایران با کشورهای حاشیهٔ خلیج‌فارس
🔹
بقایی: اینکه دیپلماسی با پشتوانهٔ میدان موفق شده کشورها را به این نتیجه برساند که راه‌حل امنیت منطقه این است که به‌دور از حضور بیگانگان با هم صحبت کنیم، دستاورد کمی…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/461450" target="_blank">📅 23:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461449">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2547a60937.mp4?token=IdlbtY-zrSC6Rief9jHASyg_cDpKeHN5Qiw3yWQW9sn83tc2aRUbTcWZyupMNXAoQsdZPO_Ly2BffPckt2BbERB3NM9W2Nf9nZLg9GKjkCH0PXRy-IH2mMcOnMz5SC6JLohpEduZoufZqtmnX5tP9h3pWNwGNpRUWvzqqveGswRz_HaaGXmWNBHNxC-N23nhx6ct-GjpZa9t_dzAHNHK3FcjCeqw4TsSzDNBC_EPst8hYd4mFedZE6Kl5gHq7j6iXai01Yuhfj2Vpa8-sw-KX3u83xtw0KcgdYRrGLeBFDHgzQTyz2PCL8w0YFaqqbO3QeDA3McKYPM6yKnA_HkKHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2547a60937.mp4?token=IdlbtY-zrSC6Rief9jHASyg_cDpKeHN5Qiw3yWQW9sn83tc2aRUbTcWZyupMNXAoQsdZPO_Ly2BffPckt2BbERB3NM9W2Nf9nZLg9GKjkCH0PXRy-IH2mMcOnMz5SC6JLohpEduZoufZqtmnX5tP9h3pWNwGNpRUWvzqqveGswRz_HaaGXmWNBHNxC-N23nhx6ct-GjpZa9t_dzAHNHK3FcjCeqw4TsSzDNBC_EPst8hYd4mFedZE6Kl5gHq7j6iXai01Yuhfj2Vpa8-sw-KX3u83xtw0KcgdYRrGLeBFDHgzQTyz2PCL8w0YFaqqbO3QeDA3McKYPM6yKnA_HkKHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: عربستان، ژاپن و اردن تبعات رای‌ مثبت خود به قطعنامهٔ ضدایرانی آژانس را خواهند دید و ما آن‌ها را پاسخگو خواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/461449" target="_blank">📅 23:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461448">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fubw0j-fMllq8hRVeogMT9XPWZgDYvXp7CJGp34ab3fgvOXjfN2aHHO3F16YkoAjIsb5W7s1AWyJ8hAAvbQOR1uv-8DO_BBuBvf_rP7a44Sj6CZqXRR3ixP5ZimGlgWgTZAW0HJYZ8Ccj6pqo8Tr75iwHIyyV9v35lmeu6E2tEZuTzbZ5zWbP_kZRyMCSgfv0XGuAlgAD6NIv_B-94sbQFYxLpnlKKa3yzZKWkBHb2pfnUQ-GSab6URk7LvybynOgrmKEvdm73owY0YHqJSiQOsB4Gtvike1W-Bqhksvxt2mT69KMG5Z42FwrQmbllgM3oLAgtJffZ2Szba3StSalg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۴ خبر امیدوارکننده از ایران در یک قاب
🔹
از کاهش ناترازی برق و توسعه راه‌ها تا بازگشت کارخانه‌ها به تولید، رشد کشاورزی، توسعه خدمات درمانی و موفقیت‌های فرهنگی؛ مجموعه‌ای از خبرهای ۱۱ شهریور نشان می‌دهد بخشی از ظرفیت‌های کشور در مسیر فعال‌شدن و توسعه قرار گرفته است.
۲۰ هزار مگاوات از ناترازی برق کم شد
🔸
وزارت نیرو از کاهش ۲۰ هزار مگاواتی شکاف تولید و مصرف برق خبر داد و هم‌زمان طرح هوشمند «مهتاب» برای هوشمندسازی شبکه برق با استفاده از فناوری‌های نوین و هوش مصنوعی کلید خورد.
۹ کیلومتر دیگر از آزادراه حرم تا حرم افتتاح شد
🔸
۹ کیلومتر از آزادراه حرم تا حرم در محدوده آرادان ـ لاسجرد به بهره‌برداری رسید؛ پروژه‌ای برای افزایش ایمنی و تسهیل تردد در یکی از محورهای مهم زیارتی و ترانزیتی کشور.
نخستین صندوق ارزی بورس در راه است
🔸
پذیره‌نویسی نخستین صندوق ارزی بازار سرمایه از هفته آینده آغاز می‌شود؛ ابزاری برای سرمایه‌گذاری با بازدهی ارزی و حفظ ارزش دارایی‌ها.
تولید برنج ۱۶ درصد افزایش یافت
🔸
تولید برنج کشور با افزایش سطح زیرکشت، بارندگی مناسب و اجرای برنامه‌های فنی به حدود ۲ تا ۲.۲ میلیون تن رسید؛ بیش از ۹۰ درصد محصول نیز برداشت شده است.
کارخانه لبنیات خلخال پس از ۱۰ سال فعال شد
🔸
کارخانه شیر پاستوریزه و لبنیات خلخال پس از یک دهه تعطیلی با سرمایه‌گذاری بخش خصوصی به چرخه تولید بازگشت.
۱۰۴ کیلومتر راه روستایی در جنوب کرمان افتتاح شد
🔸
راهداری جنوب کرمان طی پنج ماه، ۱۰۴ کیلومتر راه روستایی را به بهره‌برداری رساند و عملیات احداث و بازگشایی ۲۵۰ کیلومتر دیگر را با اعتبار ۱۳۵۰ میلیارد تومان دنبال می‌کند.
۶ هزار نفر به خدمات آزمایشگاهی نزدیک‌تر شدند
🔸
با راه‌اندازی واحد آزمایشگاهی سراب قامیش سنندج، حدود ۶ هزار نفر از ساکنان ۱۹ روستای منطقه به خدمات تشخیصی نزدیک محل سکونت دسترسی پیدا کردند.
۲۵۰۰ واحد مسکن ملی وارد بازار اراک می‌شود
🔸
قرار است ۲۵۰۰ واحد مسکن ملی تا مهرماه در اراک تحویل شود؛ اقدامی که به گفته رئیس اتحادیه مشاوران املاک استان مرکزی می‌تواند از فشار تقاضا در بازار اجاره بکاهد.
جایزه بزرگ جشنواره کازان به سینمای ایران رسید
🔸
فیلم «سرزمین فرشته‌ها» ساخته بابک خواجه‌پاشا در بیست‌ودومین جشنواره بین‌المللی فیلم اسلامی کازان روسیه، جایزه بزرگ جشنواره را کسب کرد.
۷ واکسن از ۱۱ واکسن اجباری در داخل تولید می‌شود
🔸
رئیس مؤسسه تحقیقات واکسن و سرم‌سازی رازی اعلام کرد ۷ نمونه از ۱۱ واکسن سبد واکسیناسیون اجباری کشور در داخل تولید می‌شود.
۱۴.۴ کیلومتر از محور شاهرود
-
طرود بهسازی شد
🔸
۱۴.۴ کیلومتر از محور شاهرود-طرود با اعتبار ۴۴۵ میلیارد تومان به بهره‌برداری رسید؛ پروژه‌ای با هدف افزایش ایمنی و کاهش تصادفات.
دستگاه پیشرفته قلب در دزفول به‌کار گرفته شد
🔸
دانشگاه علوم پزشکی دزفول دستگاه «روتابلاتور» را با سرمایه‌گذاری ۱۶۰ میلیارد ریال در بیمارستان بزرگ دزفول راه‌اندازی کرد تا درمان‌های پیشرفته قلبی در شمال خوزستان و مناطق اطراف در دسترس باشد.
توقف کامیون‌ها در مرز جلفا ۷۵ درصد کم شد
🔸
با بازطراحی فرآیند تردد ناوگان سنگین در مرز جلفا، تعداد کامیون‌های متوقف در تیرپارک از ۱۵۰۰ دستگاه به ۴۰۰ دستگاه کاهش یافت.
رتبه نخست داوران به آهنگساز ایرانی رسید
🔸
پویا سرایی، آهنگساز و پژوهشگر موسیقی کلاسیک ایرانی، در نهمین مسابقه بین‌المللی آهنگسازی کارلوسان ویتاله در ایتالیا، رتبه نخست هیئت داوران را به دست آورد.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/461448" target="_blank">📅 22:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461447">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a550834d17.mp4?token=Ul-HpNb1kJ7-V97ZjPpbVjAlDRtJvw2xdDrPmuccgSpReGsMvMsYboAuQBhjn7VsnkW7vsi8CG8p8bykcgnR4sPhaRAQ-fkUjS5hKXxbgR7ZyqzaOy0QPCllb0mxSWhF9RlhrC1PR817jk22qrnV8QU_BbwZKZodiMUfKmsdADHr-amYWRKOw33h0KqMUmQgCi0cV-GkFKkhbQom_y0XGSdFGUACWKoZFihtVdc-ARJ63UX9HF2byHzV4eeV9g5sj9qEsk2WuH_oY-V-Q8Dgjrj10r_Zuiuds4wwanzewQcr2MKD4HI2y0DraIjXU1YJCDbmm2qXDlioIDuicAwptg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a550834d17.mp4?token=Ul-HpNb1kJ7-V97ZjPpbVjAlDRtJvw2xdDrPmuccgSpReGsMvMsYboAuQBhjn7VsnkW7vsi8CG8p8bykcgnR4sPhaRAQ-fkUjS5hKXxbgR7ZyqzaOy0QPCllb0mxSWhF9RlhrC1PR817jk22qrnV8QU_BbwZKZodiMUfKmsdADHr-amYWRKOw33h0KqMUmQgCi0cV-GkFKkhbQom_y0XGSdFGUACWKoZFihtVdc-ARJ63UX9HF2byHzV4eeV9g5sj9qEsk2WuH_oY-V-Q8Dgjrj10r_Zuiuds4wwanzewQcr2MKD4HI2y0DraIjXU1YJCDbmm2qXDlioIDuicAwptg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: منشا حمله جنایتکارانه آمریکا به لامرد، خاک یکی از کشورهای جنوبی حاشیه خلیج فارس بوده است.  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/461447" target="_blank">📅 22:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461446">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2baea5ba.mp4?token=KW1vvOCV9ev1N1uocM04PtX62Zkwh8iX0p546yrlvP4z6s-fArpPOr9O_jagydaomV-L0LpvN-RYy8wbSuTZ1hHq-xEWbBhROI4Cx9EFqRz8OlNThnYdVRHNgBH9J4fsD_pd0uiXBcH3MR8Cs6rngUYXegdav86f6wXwHQPjqX8wl5WEVrDkGJve9Uda-8SnOCbTw-xbdo8o4B4ACVCxaB9wmhfvL4vFpmXg73PJo-C3PEqHy2fynjAa7CbnQgGy3G7JO5CIPXdywxYFn_RYyh763pdJgIh9Ed188vQn1QWpME-TO-sHwPs-LS-bT7TpfQ96Ipik8DZl3XNUaDOvhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2baea5ba.mp4?token=KW1vvOCV9ev1N1uocM04PtX62Zkwh8iX0p546yrlvP4z6s-fArpPOr9O_jagydaomV-L0LpvN-RYy8wbSuTZ1hHq-xEWbBhROI4Cx9EFqRz8OlNThnYdVRHNgBH9J4fsD_pd0uiXBcH3MR8Cs6rngUYXegdav86f6wXwHQPjqX8wl5WEVrDkGJve9Uda-8SnOCbTw-xbdo8o4B4ACVCxaB9wmhfvL4vFpmXg73PJo-C3PEqHy2fynjAa7CbnQgGy3G7JO5CIPXdywxYFn_RYyh763pdJgIh9Ed188vQn1QWpME-TO-sHwPs-LS-bT7TpfQ96Ipik8DZl3XNUaDOvhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا در ۳۰ ثانیه ۷۲۰ هزار ترکش بر سر مردم لامرد ریخت!  @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/461446" target="_blank">📅 22:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461445">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: ما در وضعیت
«
نه‌ جنگ، نه‌ صلح
»
نیستیم؛ ما در وضعیت جنگ هستیم
🔹
تحریم و محاصرهٔ دریایی به منزلهٔ جنگ است و هر آن‌چه که ما در این وضعیت انجام می‌دهیم نامش دفاع است.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/461445" target="_blank">📅 22:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461443">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مدیرعامل بورس تهران:بازگشایی نمادهای سهام عدالت درحال پیگیری است
🔹
سازمان بورس پیگیر برگزاری مجامع سهام عدالت استانی است. در صورت تأیید نهایی دولت و شورای‌عالی بورس، زمینه برای بازگشایی نماد این شرکت‌ها فراهم خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/461443" target="_blank">📅 22:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461442">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آتش‌سوزی گسترده در مسیر خط لولۀ نفت عربستان
🔹
داده‌های ماهواره‌ای ستونی متراکم از دود سیاه بر فراز جنوب مدینه در عربستان سعودی را نشان می‌دهد و گزارش‌های منتشرشده با استناد به داده‌های ماهواره‌ای، از وقوع آتش‌سوزی گسترده در یکی از تأسیسات مرتبط با خط لولۀ…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/461442" target="_blank">📅 22:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461441">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f182f209a1.mp4?token=uFKNUetrH9Sw3oICGnMjzlsWqRCAyBzHQ4IblbWja2f5ZwreP9mYrdiwLVg5WMMqthtdD4ZwAWflxY9XJMwuUavFfBczkYVqo1TpKjQhGIUsMtCqa__bhZF3N9I4Ad1o_UhG-PVIgOKVM93pQTT8a0mNthI7HBbHWNw5KfLVxaoxNmKjE0N7q6XtDZIGy6xODdTZ8UPq1IvDw4_3MhfeB00ypWJ07RrmT_UAPWXOyGSdVnloptnYyLuf2IYJDnW2-FqH-vaiTYek2nbLGAVBoyvxmOcUeFO7dIxRTITVyAXsdz6xLO2yVX15PXe7U74F_RWmVOUVrdegP97XWpFkQ58Ct20CDDyJcwSIVC8S_32P3l3u-XSdwRK7OsTUFY2xMtalS5k3IRRgZIxSECY-VI8yMIW3yA_YMRp8M6cyiSyAMHkQBSowqDDYI8guD9CXWxpj1cdAiXMPrtjOxVPUr_1heN7FImmxF730a5f_C-OGrNI0if9fiKE2gucybMP1LvVOmtA5zbLUh1G2NW5AoxU7I2dT74DryueyGI2XGCjE-MHBq2kSdAGdb7mW96m2bV-9CTLVxS79SO-C-YlPsHZO9R2I03PPJTTKTu4Z2G_2Vzhzv4NYf2jY6WCfAfSOhHXMlxq-f6mcr1-ZY2yLw7BUG43BOQP3dlahsumzjl0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f182f209a1.mp4?token=uFKNUetrH9Sw3oICGnMjzlsWqRCAyBzHQ4IblbWja2f5ZwreP9mYrdiwLVg5WMMqthtdD4ZwAWflxY9XJMwuUavFfBczkYVqo1TpKjQhGIUsMtCqa__bhZF3N9I4Ad1o_UhG-PVIgOKVM93pQTT8a0mNthI7HBbHWNw5KfLVxaoxNmKjE0N7q6XtDZIGy6xODdTZ8UPq1IvDw4_3MhfeB00ypWJ07RrmT_UAPWXOyGSdVnloptnYyLuf2IYJDnW2-FqH-vaiTYek2nbLGAVBoyvxmOcUeFO7dIxRTITVyAXsdz6xLO2yVX15PXe7U74F_RWmVOUVrdegP97XWpFkQ58Ct20CDDyJcwSIVC8S_32P3l3u-XSdwRK7OsTUFY2xMtalS5k3IRRgZIxSECY-VI8yMIW3yA_YMRp8M6cyiSyAMHkQBSowqDDYI8guD9CXWxpj1cdAiXMPrtjOxVPUr_1heN7FImmxF730a5f_C-OGrNI0if9fiKE2gucybMP1LvVOmtA5zbLUh1G2NW5AoxU7I2dT74DryueyGI2XGCjE-MHBq2kSdAGdb7mW96m2bV-9CTLVxS79SO-C-YlPsHZO9R2I03PPJTTKTu4Z2G_2Vzhzv4NYf2jY6WCfAfSOhHXMlxq-f6mcr1-ZY2yLw7BUG43BOQP3dlahsumzjl0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۶.۵ ماه است خیابان‌ها قاب حضور ملت است
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/461441" target="_blank">📅 22:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461440">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
آموزش‌وپرورش اعلام می‌کند مدارس دولتی حق دریافت وجه اجباری ندارند، اما در عمل چنین نیست. به‌دلیل افزایش شهریه مدارس غیردولتی، تقاضا برای مدارس دولتی زیاد شده و برخی مدارس از این شرایط سوءاستفاده می‌کنند. با وجود نامه
آموزش‌وپرورش منطقه ۵
، مدرسه از ثبت‌نام پسرم به بهانه نبود ظرفیت خودداری کرد اما بعد از پیگیری‌های فراوان و پرداخت ۱۰ میلیون تومان، ناگهان ظرفیت ایجاد شد! آیا این عدالت است؟
🔹
اغلب
فروشگاه‌های موتورسیکلت در خیابان ۱۷ شهریور تهران
بخشی از پیاده‌روی مقابل مغازه‌شان را هم جزو مغازه حساب می‌کنند و با قرار دادن موتورسیکلت‌ها، عبور و مرور مردم را واقعاً دشوار کرده‌اند. مسئول رسیدگی به این وضعیت کیست و مردم باید به کجا شکایت کنند؟ بعضی‌ها می‌گویند این مغازه‌ها بابت
استفاده از پیاده‌رو
به
شهرداری
پول می‌دهند؛ آیا چنین چیزی صحت دارد؟ خواهشمندم پیگیری کنید.
🔹
بنده یکی از داوطلبان
آزمون استخدامی فراگیر ۱۳
هستم که تیرماه ۱۴۰۴ در این آزمون شرکت کردم و برای دستگاه اجرایی اداره کار پذیرفته شدم. با وجود گذشت بیش از یک سال و طی‌شدن تمام مراحل شامل آزمون کتبی، مصاحبه تخصصی و گزینش هنوز
نتیجه نهایی و زمان به‌کارگیری پذیرفته‌شدگان مشخص نشده
است. با وجود پیگیری‌های مکرر از هسته گزینش کشور، سازمان امور استخدامی و منابع انسانی واحد استانی، نتیجه‌ای حاصل نشده است. این روند فرسایشی، داوطلبان و خانواده‌هایشان را با مشکلات جدی مواجه کرده و ممکن است باعث انصراف بسیاری از پذیرفته‌شدگان شود. لطفاً درخواست ما را به گوش مقامات تصمیم‌گیرنده برسانید.
🔹
لطفاً صدای مردم
خمینی‌شهر و درچه اصفهان
را به مسئولان برسانید. جاده منتهی به کارخانه رب آیدا و روستای جلال‌آباد وضعیت بسیار نامناسبی دارد و خرابی آن به خودروها آسیب می‌زند. تاکسی‌ها نیز به‌دلیل شرایط نامناسب جاده در این مسیر تردد نمی‌کنند. این مسیر نیاز فوری به
آسفالت
و مرمت دارد. مسئولان کارخانه می‌گویند مالیات و عوارض شهرداری پرداخت می‌کنند و جاده مربوط به آن‌ها نیست.
🔹
من با هزار بدبختی و به‌صورت قسطی یک پژو ۲۰۶ مدل ۸۲ خریده‌ام و تازه این ماه قرار است آخرین قسطم را پرداخت کنم. حالا با این
طرح جدید اسقاط خودروهای بالای ۲۰ سال
، واقعاً نمی‌دانم باید چه کار کنم. اگر قرار باشد این خودرو را اسقاط کنم، از کجا پول بیاورم و خودروی دیگری بخرم؟ آیا مسئولان شرایط اقتصادی قشر ضعیف و کارگر را در نظر گرفته‌اند؟ کسی که با سختی و قسط و قرض توانسته یک خودروی قدیمی بخرد، چطور می‌تواند یک‌باره آن را کنار بگذارد و خودروی جدید تهیه کند؟ مگر مسئولان از درآمد و توان مالی مردم بی‌خبرند؟
🔹
لطفا مسئولین درمورد
بازنشستگان کشوری
چاره‌ای بیندیشند. با این
حقوق پایین
و قیمت‌های سربه فلک کشیده چکار کنیم؟ پول درمان پرداخت کنیم یا پول خورد وخوراک و مسکن؟
🔹
چرا به مردم می‌گویید خاموشی برنامه‌ریزی‌شده نداریم و بعد قطعی‌ها را با عنوان‌هایی مثل خرابی یا مشکل انشعاب توجیه می‌کنید؟ اگر محدودیت یا کمبود برق وجود دارد، صادقانه به مردم اعلام کنید. این تناقض‌ها بیش از هر چیز اعتماد عمومی به مسئولان را از بین می‌برد.
🔹
برای ما احراز هویت انجام شده و حتی به دفتر خدمات دولت نیز مراجعه کرده‌ایم، اما کالابرگ همسرم که برای زیارت اربعین به عراق رفته بود، هنوز واریز نشده است. کالابرگ من واریز شده اما برای همسرم با وجود انجام احراز هویت، اعتباری شارژ نشده است. احتمالاً افراد دیگری نیز با این مشکل مواجه هستند. خواهشمندیم مسئولان وزارت تعاون این موضوع را بررسی و علت
عدم واریز کالابرگ
برخی زائران اربعین را پیگیری کنند.
🔹
در
آزادراه حرم تا حرم
، دو بار از ما عوارض گرفتند اما متأسفانه
وضعیت آسفالت
در خیلی از قسمت‌های مسیر بسیار خراب و نامناسب بود. حتی بخش‌هایی که عوارضی پرداخت نکردیم، آسفالت بهتری داشت. وقتی از مردم عوارض دریافت می‌شود انتظار می‌رود حداقل وضعیت جاده مناسب باشد.
🔹
دیشب به داروخانه رفتم و برای بچه‌ام دو مکمل و یک کپسول خریدم. فردی که بیرون داروخانه نشسته بود با دیدن پاکت داروهای من گفت همین‌ها را از
ترب
بخر؛
نصف قیمت داروخانه
است. باور نکردم اما وقتی بررسی کردم دیدم واقعاً قیمت‌ها تفاوت زیادی دارد. واقعاً ماجرا چیست؟ اگر این فروش‌ها غیرمجاز یا کلاهبرداری است، چرا نظارت و برخورد نمی‌شود؟ و اگر محصولات با همان کیفیت و اصالت عرضه می‌شوند، چرا باید در داروخانه‌ها با این اختلاف قیمت به فروش برسند؟
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/461440" target="_blank">📅 22:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461439">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65f3678981.mp4?token=GbESNv23_-NoYC9oOm9mRHHGvEQ3lWVvWaDn99h0TXbtbnMGKlPlktJp-x0OcuvYC7rZ94znOkWKayuOaRbVUlfmeTjP_gBS1505Zkmdc0NUZzkx572aUoHasTMyGRiqWOXw7i0LXtm_vyoqXsXSPemC_652AjkMjwjUsCiCdDS4sXFC6ru15xTE2wsrdN4H5aCpwyOE0r73r0lfE7ynlB91ZOJ5dUaLBP2i6dbcjNXcVsybOyUNFfgIAIYmH3j08yux5zrQ3Q491cvd19QyEIsoCRYMtW1QjdOCuKv5GRrbUGEo7dRFWr3t1MQdHnCuc0dBhHqi81bm4H4AOlFS57en4xrQmyywCcvO2oTkLd5UsXLuiVHQ6wiatU1-6RZ5v2bubxw9djjFl0xtLixw0K7PLDEPmmSaSmNrlovmV02yPaaOJTDq2s_aaBettFoVoVN5_NrTGSf06v7DW97dDkQyTknxXEIj_bFwneehWd2OK4e7h65zVO1CpKesak9JuZcabB5nzJYpXseNxF23PWX1kwgaxXBDpVbwoVGDv9-YngVuV4gp8BinZ7cuyUYSRw6SGY6Rke48d7hVEzLpsbbnCL0hIoBWsaTwkx97WIjpNfFCDZveOwEDoYVxIu4b01565zmp5w3pZ-8Mm-D3NoILjNLuRonlKzs25THp_ZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65f3678981.mp4?token=GbESNv23_-NoYC9oOm9mRHHGvEQ3lWVvWaDn99h0TXbtbnMGKlPlktJp-x0OcuvYC7rZ94znOkWKayuOaRbVUlfmeTjP_gBS1505Zkmdc0NUZzkx572aUoHasTMyGRiqWOXw7i0LXtm_vyoqXsXSPemC_652AjkMjwjUsCiCdDS4sXFC6ru15xTE2wsrdN4H5aCpwyOE0r73r0lfE7ynlB91ZOJ5dUaLBP2i6dbcjNXcVsybOyUNFfgIAIYmH3j08yux5zrQ3Q491cvd19QyEIsoCRYMtW1QjdOCuKv5GRrbUGEo7dRFWr3t1MQdHnCuc0dBhHqi81bm4H4AOlFS57en4xrQmyywCcvO2oTkLd5UsXLuiVHQ6wiatU1-6RZ5v2bubxw9djjFl0xtLixw0K7PLDEPmmSaSmNrlovmV02yPaaOJTDq2s_aaBettFoVoVN5_NrTGSf06v7DW97dDkQyTknxXEIj_bFwneehWd2OK4e7h65zVO1CpKesak9JuZcabB5nzJYpXseNxF23PWX1kwgaxXBDpVbwoVGDv9-YngVuV4gp8BinZ7cuyUYSRw6SGY6Rke48d7hVEzLpsbbnCL0hIoBWsaTwkx97WIjpNfFCDZveOwEDoYVxIu4b01565zmp5w3pZ-8Mm-D3NoILjNLuRonlKzs25THp_ZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌اللهی که منبرش سنگر مبارزه بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/461439" target="_blank">📅 21:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461438">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7928214bf2.mp4?token=Bg93T9NdSkN6_g8d8rlOM8XRypZVuzY9sCSo9dNbzAG90nGnvUs92-I1U1Jxr7buv1CTGTFB2PICGrp0SGCw289YTjl_3T478xMU9rycPT1K_vM6AUGaIzGODO8ejrS9C4ODs_YofFCnhVfGY1-Byb5Xcc19yEGzQ5wVV1SRnxob6HWhz5pmfRXQQy35rgB6X8wC8qMzvMgEg-mUOBtCtga1oKrrWOEIcjIS2ByKN_LyYDjzSQj-4TQfpq8yumq8_rIm4gObJ3Tin108zVZVtgq3n6aBRfp-muy7P6BqUTRqx-2a-F44GYZ4-lsAcEX9BCZlwkA42_r6Ja0T2fP4YzEqYTk-CNBJnxKEwntyTgKQhoxhHhcmFRdCUS9jj4OH-4ainuAzsglwlcISOnmgPinTRcEWTwnB7sXIEv0BvY9t--YCnZz61I2aRB3svAZvSms2rUKXlkOv3b_jX8A0aickzcXwbdCoLec9EBj3ImCYdKcxbuTWjs4VTCfhhqLnNxOHSNKxcbmdRDBPLHPIvJXq1M15TPjgo6Xw4BsWRZzuJWiLUliNi_7my4OQFe_pZpjqpTMV_47UgpddLavZNyveDpYRh2tXSD0ZNXVsrRcIoax-aneIWQ60YzzjobPyndP9t5TG5yUDlEzNqDt_O-z01BDLBLqA-2F8KsD3pKo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7928214bf2.mp4?token=Bg93T9NdSkN6_g8d8rlOM8XRypZVuzY9sCSo9dNbzAG90nGnvUs92-I1U1Jxr7buv1CTGTFB2PICGrp0SGCw289YTjl_3T478xMU9rycPT1K_vM6AUGaIzGODO8ejrS9C4ODs_YofFCnhVfGY1-Byb5Xcc19yEGzQ5wVV1SRnxob6HWhz5pmfRXQQy35rgB6X8wC8qMzvMgEg-mUOBtCtga1oKrrWOEIcjIS2ByKN_LyYDjzSQj-4TQfpq8yumq8_rIm4gObJ3Tin108zVZVtgq3n6aBRfp-muy7P6BqUTRqx-2a-F44GYZ4-lsAcEX9BCZlwkA42_r6Ja0T2fP4YzEqYTk-CNBJnxKEwntyTgKQhoxhHhcmFRdCUS9jj4OH-4ainuAzsglwlcISOnmgPinTRcEWTwnB7sXIEv0BvY9t--YCnZz61I2aRB3svAZvSms2rUKXlkOv3b_jX8A0aickzcXwbdCoLec9EBj3ImCYdKcxbuTWjs4VTCfhhqLnNxOHSNKxcbmdRDBPLHPIvJXq1M15TPjgo6Xw4BsWRZzuJWiLUliNi_7my4OQFe_pZpjqpTMV_47UgpddLavZNyveDpYRh2tXSD0ZNXVsrRcIoax-aneIWQ60YzzjobPyndP9t5TG5yUDlEzNqDt_O-z01BDLBLqA-2F8KsD3pKo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین وحدت در شب ۱۹۵ تجمع مردم مراغه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/461438" target="_blank">📅 21:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461437">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یمن: ۵۴۰۰ کیلومتر را آزاد و ۹ هواگرد سعودی را سرنگون کردیم
🔹
ستاد نیروهای مسلح یمن در بیانیه‌ای دستاوردهای خود را نبردهای روزهای گذشته با مزدوران سعودی را اعلام کرد.
🔹
۱. بیرون راندن نیروهای سعودی از ۶ منطقه در استان‌های تعز و الحدیده، با مساحتی کلی معادل…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/461437" target="_blank">📅 21:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461436">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f433103ae3.mp4?token=PlBb1SwnoB5cLMbBYrJfVb-AO9Cp31nIn_rDMvJLOjjsQDjpL9CSNobHAj6UMN4BB9HK740LTtkeZfWyTpLa94ilznixS89BinksQJNVuONitzp305z_X38wXgcSeKjXpbvRrBmEWKYz3oEdMPToZV_fGiF94CyX9b6kmolXIovpzHWxPC8dqHiTNsa70Ppg2H_XHHSMViw-2RIGCI-xZw_Owc5hmj0nSIiTrY4kxLODl9nvk0DTbv3_RwAOZKPNCg1G3PUqAJfWcskVrJhRCNqIVWrWIiSwSL8FZ7y5k0JTl8oIiwsjs-ORcPpZ7qn0w1V6OyvZiLwcP4_7EHtErK6JdVz73ArFmFqul0zQNX87f3-hKCsimkmX8LnN-TWGcnym5FYYrWAweHg-93wDAI0lX2XjAeJrTtGaCt_lLZQBJnt3v7U1onimYr1PH4dPUfCT4cenYxFgUMkgvRi6hfZ9vu6Bsyv0IgBuzNkyBOzcR0GHrn6pN2rC4dRw2iK0GqPC46xi4WBYq33bSCKFXqjq4-EniJCIG0N2vO-PzQ73nfMOa930Knd-DMENzpvhkG17a43uRQm9jZ5o3tH3GsdnuCcojnSKADvtXpkJYCPbMSUjIVQfdRgK9h6AjI3fQsoG_ILK6XdazEpctr_trSu7hTRZOJrGAAEzaTj1tTY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f433103ae3.mp4?token=PlBb1SwnoB5cLMbBYrJfVb-AO9Cp31nIn_rDMvJLOjjsQDjpL9CSNobHAj6UMN4BB9HK740LTtkeZfWyTpLa94ilznixS89BinksQJNVuONitzp305z_X38wXgcSeKjXpbvRrBmEWKYz3oEdMPToZV_fGiF94CyX9b6kmolXIovpzHWxPC8dqHiTNsa70Ppg2H_XHHSMViw-2RIGCI-xZw_Owc5hmj0nSIiTrY4kxLODl9nvk0DTbv3_RwAOZKPNCg1G3PUqAJfWcskVrJhRCNqIVWrWIiSwSL8FZ7y5k0JTl8oIiwsjs-ORcPpZ7qn0w1V6OyvZiLwcP4_7EHtErK6JdVz73ArFmFqul0zQNX87f3-hKCsimkmX8LnN-TWGcnym5FYYrWAweHg-93wDAI0lX2XjAeJrTtGaCt_lLZQBJnt3v7U1onimYr1PH4dPUfCT4cenYxFgUMkgvRi6hfZ9vu6Bsyv0IgBuzNkyBOzcR0GHrn6pN2rC4dRw2iK0GqPC46xi4WBYq33bSCKFXqjq4-EniJCIG0N2vO-PzQ73nfMOa930Knd-DMENzpvhkG17a43uRQm9jZ5o3tH3GsdnuCcojnSKADvtXpkJYCPbMSUjIVQfdRgK9h6AjI3fQsoG_ILK6XdazEpctr_trSu7hTRZOJrGAAEzaTj1tTY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
توکلی زاده، معاون امور اجتماعی و فرهنگی شهرداری تهران:
«بشکند آن قلمی که ننویسد مردم ایران هرشب در خیابان ایستادند» /
🔹
کجای دنیا مردم هرشب برای خون‌خواهی، دفاع از نیروهای مسلح و دعوت مسئولان به وحدت به خیابان می‌آیند؟
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/461436" target="_blank">📅 21:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461435">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFexTgm_vg3FmLK1z8iuSYAf17EaUNfC5dvL-4IARqWGk9-kg7RuEfoB1h7le6AK5sOp_yo0juEDzUqy8oegjyAR9YmM5efC3z80QxsgcAi_ONiGhRnq0l9f_vxNxIihA_6-ZN9SdNOIMYAU7nMpeDztv51aA4b7a4IDU1tHhYC4Zfnm3lQXUovoFmAAyWNpH6mf3aVE_jV0dju5a37DM09sYawoceuB5yFZ29NmrSD_hvHbkmGuPE3eQR96iN6nP370ReLcYE24FJGHXQHfSpzDJYUr82N8s3Mq44P6MWE40pPXxmpKoXs7n8YumFfRZqhEEn31RxA26a1vaVxb3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقش مدیریت
#تحول_گرا
در خلق ارزش پایدار؛ چگونه
#بيمه_البرز
هم‌زمان صدرنشین بازار و پشتیبان تولید ملی شد؟
شرکت بیمه البرز با اتخاذ رویکردی تحول‌گرا و ارائه بیمه زندگی و سرمایه‌گذاری پروژه‌محو‌ر، ضمن کسب
#جایگاه_نخست
صنعت بیمه با ثبت ۱۵.۵ همت حق‌بیمه تولیدی (رشد ۴۰۹ درصدی) و سهم ۲۴ درصدی بازار، طی سه ماه ۱.۵ همت از پس‌اندازهای خرد مردمی را به بخش‌های مولد صنعتی تزریق کرد.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5096</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/461435" target="_blank">📅 21:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461434">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461434" target="_blank">📅 21:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461433">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_yj6OTHCp-agMMm714xRTXiMorY8fNVtXu770l9_GwTRe5vkg59_eN7WuynxZg9TEf0dQEYQPkBmLvDREemOMjUqsMMnGNvKzX0oSabJsBp_Y52Z3Sz9-Q73vtl5llJuM_I_LZwV0-hn0hBgI23qW9gC82PSBsPEFP-HJx5l0wya0J_q7wseb2vMpFMz6tIcbbZ5Ls-gd0kbovMBgfKvkRewaCMsiBPS1vzHDjGZpQXcSKMA7zDXg9xqzDLfrtVpTcgmnO7fpwOSI2aQZmqcsn3fef3LxOinWwhhBUlij9PB6MBUHGkG43ZFYY1CVlKProl0D9ykq-03JiJVSae3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بسیج: آمریکا دنبال ایجاد اختلاف در کشور است
🔹
آمریکا دنبال این است که بین جریان‌های داخل کشور اختلاف ایجاد کند و ما با حفظ انسجام نباید اجازه دهیم آن‌ها در این کار موفق شوند.
🔹
اسرائیلی‌ها منتظر فروپاشی خود در ۸۰ سالگی تأسیس رژیم صهیونی هستند و ان‌شاءالله زودتر از زمانی که رهبر شهید انقلاب فرمودند، رژیم از بین خواهد رفت.
🔹
ما با حفظ انسجام و وحدت داخلی باید با مسائلی مثل حجاب و سایر موضوعات فرهنگی مواجه شویم و اجازه ندهیم این مسائل انسجام داخلی را به هم بزند.
🔹
باید عرصه را برای حضور همه مردم با سلایق و رنگ‌های مختلف در بسیج فراهم کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/461433" target="_blank">📅 21:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461432">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8de15aa0aa.mp4?token=RQni9SEWgjTRDPmzHFu21EI-HB75_9m6qguIidrWEKqS935xb5Ga5G5F9_pj28IqABYqBmSgLVR0-3YOR7_D5QWeJQL3Um7H3BsFsoq2DBpl5jhPe-1hmOJFjMFfU64iTjUVArK74XgFotI165uo6bQYyZgSADM-X1JKXTKWaLVCPsJRvmVH09ANYPL7QnpejDrGbPXse16M-Tzz7KPiN0onCdnyXzLuVJr86yGbBZZ83BEOmXqVi_1B6JaYksKFP7Ddi0Q_S5IGgA83Fdv7zmF4euGzMJvfgAKpuBeMZoaLcqLv6CaAxUGvXT7SL1w12FKtnxILqA6QwtpvtezUkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8de15aa0aa.mp4?token=RQni9SEWgjTRDPmzHFu21EI-HB75_9m6qguIidrWEKqS935xb5Ga5G5F9_pj28IqABYqBmSgLVR0-3YOR7_D5QWeJQL3Um7H3BsFsoq2DBpl5jhPe-1hmOJFjMFfU64iTjUVArK74XgFotI165uo6bQYyZgSADM-X1JKXTKWaLVCPsJRvmVH09ANYPL7QnpejDrGbPXse16M-Tzz7KPiN0onCdnyXzLuVJr86yGbBZZ83BEOmXqVi_1B6JaYksKFP7Ddi0Q_S5IGgA83Fdv7zmF4euGzMJvfgAKpuBeMZoaLcqLv6CaAxUGvXT7SL1w12FKtnxILqA6QwtpvtezUkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
‌ بدون تعارف با خانوادهٔ شهیدی که طراح تونل‌های شهرهای موشکی بود
🔸
همسر شهید مصطفی عارف: تا قبل از شهادت همسرم نمی‌دانستم او کجا کار می‌کند. فقط یک‌بار به من گفت بعدها می‌فهمی که ما چکار می‌کنیم.
🔸
فرزند شهید: پدرم یک قهرمان بود. خیلی دوست دارم پدرم را یک‌بار…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/461432" target="_blank">📅 21:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461431">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c433d1a34.mp4?token=MU2H6hScRSHiP1Apxjvs_Pe1TXw44l5VVoYDTCbmrcMARUn4RqXAMYTzZ5lc3LoHARL4uvJMnG77KZnvNU91u9nGwYh0NfQ5gZaklakTjMgjVxDnGpX9zAeWfyybDTuVH6-vETQRBmdnosHoJgUvytCX-FFZMAXXV1T0RpbVahAffCgQOn8k7JfcVEDBHlKW5uqvy6K2ve3nZQNzqsFe2thHEiQHQxHddztNuUrOjg7EQt1t780T2Rv2a-YJRSdFk3marc5Q_8XdmFiJKgvftqeN1lS_OFFv66A7HQVdgxhZ5UhGAc0kKrYlkFWBgnVybOrTvM7tTQdunVlG4f4DMhzRgbkUtVh9SySqgZ_xjaTEtnM0mtEpFlQ3MT4ciDF6vj9C9mVFNqJNtzHyy59DnSUBEt6F2QHY32vSTKUu7ZLv4yU32g9Fe4bHukPP_i533XXWQXXP-XQl3eO4IWlBufyibVIcv3KWHk_Q2gzrOKusedkA3B9jhWPsSmOpSDS8eN5KdSgERhCP8z0t1OmM16zif5nWUgjGuatqLDPCiq_FMV-HzpCzr-NSpJrdLi2AmP2wpQBHdaSm8MF2CvmX5kgvg5VF8J1QQDcWLSV1FJ4DyR72ka3LcSi6gvTGJ_o-e7RfndPX-AdC6edHq5k73UCdjxjTXEvYrkhqtq64iQ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c433d1a34.mp4?token=MU2H6hScRSHiP1Apxjvs_Pe1TXw44l5VVoYDTCbmrcMARUn4RqXAMYTzZ5lc3LoHARL4uvJMnG77KZnvNU91u9nGwYh0NfQ5gZaklakTjMgjVxDnGpX9zAeWfyybDTuVH6-vETQRBmdnosHoJgUvytCX-FFZMAXXV1T0RpbVahAffCgQOn8k7JfcVEDBHlKW5uqvy6K2ve3nZQNzqsFe2thHEiQHQxHddztNuUrOjg7EQt1t780T2Rv2a-YJRSdFk3marc5Q_8XdmFiJKgvftqeN1lS_OFFv66A7HQVdgxhZ5UhGAc0kKrYlkFWBgnVybOrTvM7tTQdunVlG4f4DMhzRgbkUtVh9SySqgZ_xjaTEtnM0mtEpFlQ3MT4ciDF6vj9C9mVFNqJNtzHyy59DnSUBEt6F2QHY32vSTKUu7ZLv4yU32g9Fe4bHukPP_i533XXWQXXP-XQl3eO4IWlBufyibVIcv3KWHk_Q2gzrOKusedkA3B9jhWPsSmOpSDS8eN5KdSgERhCP8z0t1OmM16zif5nWUgjGuatqLDPCiq_FMV-HzpCzr-NSpJrdLi2AmP2wpQBHdaSm8MF2CvmX5kgvg5VF8J1QQDcWLSV1FJ4DyR72ka3LcSi6gvTGJ_o-e7RfndPX-AdC6edHq5k73UCdjxjTXEvYrkhqtq64iQ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
‌
بدون تعارف با خانوادهٔ شهیدی که طراح تونل‌های شهرهای موشکی بود
🔸
همسر شهید مصطفی عارف: تا قبل از شهادت همسرم نمی‌دانستم او کجا کار می‌کند. فقط یک‌بار به من گفت بعدها می‌فهمی که ما چکار می‌کنیم.
🔸
فرزند شهید: پدرم یک قهرمان بود. خیلی دوست دارم پدرم را یک‌بار دیگر ببینم.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/461431" target="_blank">📅 21:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461429">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حملۀ تارتار به سازمان لیگ: دستی از غیب تصمیم به لغو گرفت
⚽️
سرمربی پرسپولیس پس از لغو بازی با خیبر: از این تصمیم غافلگیر و شوکه شدیم، چون مدیریت باشگاه و بنده هیچ درخواستی مبنی‌بر لغو مسابقه ارائه نداده بودیم و این تصمیم به صورت یک‌جانبه و بدون هماهنگی گرفته…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/461429" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
