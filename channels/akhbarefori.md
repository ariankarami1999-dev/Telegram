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
<img src="https://cdn4.telesco.pe/file/D_LKKWV7a9LL7VQdBcI-CRi0Xpl6zVcC4pni9CbKcYhlQtc3IGbh0uYZuUcKvASv-GwqjZvsD0GYeBiWPmu8bunj-a-AMZykpLbSbb3kzsM6KIylkTwVZ2lVt84gyC5setlLn3IJLqhFbad0PhyjHQcRlqjjhXvq4RCnEYVRPv7UInQ6MWHmqklUtalB0wnvX70FVI9_-QTcLCsRcihMpf-lt72bV8_6YjOWb9_CtTSMEVL6mw8-LbN-8FnXzoM9eUCi8KkfSvE2OVM1nEjRmlEwCrgt-KrDkKhrS6VLViS4fklY5Cy2GL-sPRy75Lj6MX8cAU3EV_hxFWLsflyk3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.27M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 20:24:41</div>
<hr>

<div class="tg-post" id="msg-666533">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
تعویق برگزاری امتحانات نهایی پایه یازدهم به دلیل تسهیل در تردد زائران مشهد
🔹
به دلیل تسهیل در بازگشت زائرانی که به مشهد مقدس مراجعه کرده‌اند، امتحان نهایی پایه یازدهم که برای روز شنبه برنامه‌ریزی شده بود، به تعویق افتاد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/akhbarefori/666533" target="_blank">📅 20:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666532">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
توصیه کارشناسان فوریت‌های پزشکی
🔹
اگر در مراسم پیاده‌روی وداع با رهبر شهید شرکت می‌کنید، حتماً یک بسته پودر ORS (او آر اس) همراه داشته باشید. پودر را در یک بطری آب حل کنید و در طول مسیر، آن را به‌صورت جرعه‌جرعه بنوشید.
🔹
نوشیدن محلول ORS به جبران آب و املاح از دست‌رفته بدن در اثر گرما و تعریق کمک می‌کند و می‌تواند از بروز کم‌آبی و خستگی ناشی از گرما پیشگیری کند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/666532" target="_blank">📅 20:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666530">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vwglro26Nn3eGq8wZevggNV60WqSxVUrMzKOuGoU7kcy4RVjxmLNR9igvi7kFfRjMSPbyVoHXxUhAly3tqJu10I5YZPYkeHoJ74WcYQO9LvffLG_mOjUk_I0E2o6sNn2kUx1C6gZttRsjilAuN4SPQkR16siN0yHWBuDrx9o6XChXbdfkc9NTjNnmFRde88m3ALYyKSn-nf2sddFGxspIXR563YcD3dNLOFIkoFFQwe2DPsLX0F17Xs9hZTpaju9CCsF_bOkvJkr3Mn9ahzfPTutoUn5Qrevn3x2N7LWVdRtXZqNvwHhJgcb2LPYNgFUP4pn7iGKIYy2TsTPVImxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G88AsN8dEmsUIOloCt1JEp8fNAhkbO6FGIygrqFsCubAUHMtHbFaI3RtWFTSla9ZGJDLqWp0cIRO8TPawVeZzuF1cjS7SwReV1y8wmkq6yn7m46CACLz9V3PdWrA_QXraaaOA72hRC5bMq54HR8ocUU_j-sdfxKR6DDwkNHTjWD-aAHKS4Uajm3iqlSrvuIj3cEhW9yzOHnmKqjXHqjfKdd3VK9rtvsZ-cgoYHl4SfEx3SyiYKSiCZsf-dlESf3uI23OpFha_ut9_5WD7T6hWqvR_A5e90K6g4i-WGp2pobVfKW0_O8481dyrxLMW74zDQWJoCllVyJsfs_JIPnNuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
برگزاری نشست قرارگاه مرکزی حمل‌ونقل جاده‌ای وداع و تشییع رهبر شهید انقلاب با حضور وزیر راه و شهرسازی
🔹
نشست قرارگاه مرکزی حمل‌ونقل جاده‌ای وداع و تشییع پیکر رهبر شهید انقلاب اسلامی به ریاست وزیر راه و شهرسازی و با هدف برنامه‌ریزی برقراری سفرها در حوزه حمل‌ونقل عمومی و جابه‌جایی عزاداران شرکت‌کننده در مراسم تشییع به میزبانی سازمان راهداری و حمل‌ونقل جاده‌ای برگزار شد.
🔹
وزیر راه و شهرسازی از انجام هماهنگی‌های لازم در خصوص تأمین سوخت تنخواه ناوگان اتوبوسی خبر داد و بر ضرورت برنامه‌ریزی دقیق برای تأمین ناوگان حمل‌ونقل عمومی جاده‌ای در سفرهای بازگشت تأکید کرد.
🔹
در ادامه این نشست، رئیس سازمان راهداری و حمل‌ونقل جاده‌ای به ارائه گزارشی از روند سفرهای هموطنان به شهرهای تهران و قم طی روزهای اخیر و بررسی ظرفیت ناوگان حمل‌ونقل عمومی جاده‌ای برای استمرار سفرها و بازگشت از مشهد مقدس پرداخت.
🔹
معاون وزیر کشور و دبیر ستاد ملی مراسم وداع و تشییع قائد شهید امت، معاون حمل‌ونقل وزیر راه و شهرسازی، معاون نظارت و بازرسی امور تولیدی سازمان بازرسی کل کشور، رئیس سازمان هواپیمایی کشور، مدیرعامل شرکت فرودگاه‌ها، مدیرعامل فرودگاه امام خمینی(ره) و اعضای هیأت عامل و معاونین سازمان راهداری و حمل‌ونقل جاده‌ای در این نشست حضور داشتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/akhbarefori/666530" target="_blank">📅 20:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666529">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
خونخواهی، میراث کهن ایران؛ مسئولیتی بر دوش مسئولان
🔹
طلب تقاص خونی که به جور ریخته شد صرفا مطالبه‌ای ملی نیست؛ بلکه ریشه در فرهنگ تاریخی این ملت دارد.
🔹
سیاوش در فرهنگ ایرانی با مظلومیت خود به نماد جاودان عدالت بدل می‌شود و کیخسرو با برپایی داد، نه تنها خون پدر را پاس می‌دارد، بلکه نظم اخلاقی جهان را از نو استوار می‌کند.
🔹
ملتی که سیاوش را در حافظه خود زنده نگه داشته است، ظلم را با سکوت همراهی نمی‌کند و نمی‌گذارد گذر زمان، حق را به فراموشی بسپارد.
🔹
مسئولان این نظام به عنوان وارثان مکتب رهبر شهید و وکیلان این مردم در قدرت وظیفه دارند این مطالبه تاریخی و ملی را پیگیری کنند
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/akhbarefori/666529" target="_blank">📅 20:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666528">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_FaLJ9l34sZmX9DNyta3O9CiOJpmmfzrzlSxWzOG5vCJNf-w2LL_--V0m4mdmWvab6troTuErQck6mgHGUKA7cFZX1tIRaLNDZVGVx1jsy8Srydmd_Q9LeCDTsemetXC8yUIGtxu_TmvJ6AtJZgBmMgzkBLMBawxUe-yFvvA0a139FQcXI6UwNHYn-Ce9avZtGhRiKR1BaFxwLlK8vIEAzcXiLRWshpoUsDgU6JZ9iq4J8lzXgvEN1wVU96z1BWttZWqDHZlrel7nLTaNMg3s_OV9oOcELIZIjPCitpGt1AM3EZSmO8dYYSJaiw_L0RwP9rbp7c9hFBpIT4mOP8mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهان در نبودت دگر زیبایی خاصی ندارد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/akhbarefori/666528" target="_blank">📅 20:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666527">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
رئیس‌جمهور: وحدت و انسجام را در عمل نشان دهیم نه در حرف
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/akhbarefori/666527" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666526">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e948877e53.mp4?token=ZGJ-I-RyGq-ku0zCTDMwn-mX7cvwiiOQ8AeNjc4gp7utrLzB3vRRMbDTVnbher93J8FAsmX0oIGyUBerHk7p0RDdwuLvNf_de8n3I9Iox0gOzWjcOtdeD9QWAFnknjZh2PzY6zsfnhqPwM1my3hlBmuh5ewuwd1XgbA4WK7qktf7qnk1JZYlVucnfqZSJ_i_e6K1sn4DsHeNzOe0pw1irRVnAdX6NXwPL4vIJAtEa0y6OZU0RZ1fyNEUIFV1YDER78Uu5BNqHQy3IrArx9GmUESLHZfdBswA5oFJfBxAyc8LHCrdm9jPs2dbLuGAaujMJBR5qtIA3pTqQuq2moMoXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e948877e53.mp4?token=ZGJ-I-RyGq-ku0zCTDMwn-mX7cvwiiOQ8AeNjc4gp7utrLzB3vRRMbDTVnbher93J8FAsmX0oIGyUBerHk7p0RDdwuLvNf_de8n3I9Iox0gOzWjcOtdeD9QWAFnknjZh2PzY6zsfnhqPwM1my3hlBmuh5ewuwd1XgbA4WK7qktf7qnk1JZYlVucnfqZSJ_i_e6K1sn4DsHeNzOe0pw1irRVnAdX6NXwPL4vIJAtEa0y6OZU0RZ1fyNEUIFV1YDER78Uu5BNqHQy3IrArx9GmUESLHZfdBswA5oFJfBxAyc8LHCrdm9jPs2dbLuGAaujMJBR5qtIA3pTqQuq2moMoXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ازدحام جمعیت در مترو شهید بهشتی برای رسیدن به مصلی
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/akhbarefori/666526" target="_blank">📅 20:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666525">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
نحوه فعالیت بانک های کشور در روزهای  یکشنبه و دوشنبه، ۱۴ و ۱۵ تیرماه ۱۴۰۵
شورای هماهنگی بانک‌ها:
🔹
حسب تصمیم هیئت دولت مبنی بر تعطیلی روز یکشنبه، واحدهای فنی و پشتیبان ستادی و شعب منتخب بانک های عضو شورای هماهنگی بانک ها در روز یکشنبه ۱۴ تیرماه ۱۴۰۵ در تمام کشور به صورت کشیک از ساعت ۸ الی ۱۲ فعالیت خواهند داشت.
🔹
اسامی شعب منتخب در وبسایت اطلاع رسانی بانک ها منتشر خواهد شد.
🔹
تمامی واحدهای ستادی و شعب بانک ها در کل کشور در روز دوشنبه ۱۵ تیرماه ۱۴۰۵ تعطیل می باشند.
🔹
نحوه فعالیت بانک ها در روزهای سه شنبه و پنجشنبه در استان های قم و خراسان رضوی بنا به تشخیص و اعلام استانداری های متبوع است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/akhbarefori/666525" target="_blank">📅 20:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666524">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنیرو آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdsXUyE7ZzJcKxDP1uBvlZMJeV1foYRVguo6mOWALRR77jp_nSgzoZBnr9xxVJuT0KHroEEzqY2Z9QituORO5D9ywmyaNMMLLSgPBpDfWW9amwIR6cMHAN7hRzYaZs5htnq-nrP7pLcH16_VKSSbYys_SxdA4W_4qTvXSEdxixGHL7PB64D82g3jze2d61pTtFHXUkDn87kGTkv6VgQnEf9WZGz5dchbUK-Q8p9auhgm31JiVX6Nc-U55-aX1DqrPY0JE4tYz8KemmZS5_tvJpS9gEt44F6ZUcMvyzhIy0eDHcGoS0O2e5QkB1oRbit37Ug3P7D1O_jT2pcrRVQjCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسئول ستاد وزارت نیرو در امور اربعین و مناسبت‌های مذهبی:
⚡️
💧
توسعه فنی و زیرساختی صنعت آب و برق، با رهنمودهای رهبر شهیدمان ممکن شد / تامین موفق آب و برق  مورد نیاز آئین وداع با رهبر شهید انقلاب
🔹
مسئول ستاد وزارت نیرو در امور اربعین و مناسبت‌های مذهبی و‌ معاون پارلمانی صدا و سیما گفت: نگاه حضرت آقا همواره بر مصرف صحیح و به‌اندازه آب و برق بوده است.
🔸
احمد حیدری در حاشیه مراسم تشییع پیکر مطهر رهبر شهید، ضمن عرض تسلیت به مناسبت مراسم بدرقه و تشییع پیکر مبارک امام شهید و خانواده بزرگ ایشان، تاکید کرد: مسئولیت تأمین آب و برق مراسم در ستادهای کشوری به وزارت نیرو واگذار شد. این مسئولیت در شهرهای تهران، قم و مشهد دنبال می‌شود. در شهر تهران، در دو مقطع شامل روزهای جمعه، شنبه و یکشنبه برای مراسم وداع، و همچنین روز دوشنبه در مسیر تشییع از خیابان دماوند تا خیابان لشکری، برنامه‌ریزی‌های لازم انجام شده است. حداقل جمعیت ۱۴ تا ۱۵ میلیون نفر و حداکثر تا ۳۰ میلیون نفر برای حضور در این مراسم پیش‌بینی شده است.
🌐
[
مشروح خبر
]
#باید_برخاست
#عزیز_ایران
#صنعت_آب
#صنعت_برق
@niroonline</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/akhbarefori/666524" target="_blank">📅 20:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666523">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c500e8796d.mp4?token=p_2ZThcX73pEqzle1cDb2NlP3hD2Q26N1z51U20dI4VrU7vDmA2WveG0M1MEGo7wYDYbXbGlNTO5Gb8ulCqjk-Xn3xtGQ3jaXsrdo1FrOGHexUVTzTIsXNBY9yd0WLwCtOzwLU4NoVM1M21LFX7HGk6vX77evNEi9T9PzYHlYgKfCTXp6FuDdbB0uDhpST2jpgoTr5VBlsGd4ndh8bDKJm9YhFa4nxC98omI6bEfzFBj_OrkCWRoVnjqHajCwIullS3XrzZ_E0gWMYxChqb-BRLI7HLXglM1heA0EoYMGzTFdNtyfQ5tomCACwkEFabLyS7RUXa_LMflgm1_Sf4HlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c500e8796d.mp4?token=p_2ZThcX73pEqzle1cDb2NlP3hD2Q26N1z51U20dI4VrU7vDmA2WveG0M1MEGo7wYDYbXbGlNTO5Gb8ulCqjk-Xn3xtGQ3jaXsrdo1FrOGHexUVTzTIsXNBY9yd0WLwCtOzwLU4NoVM1M21LFX7HGk6vX77evNEi9T9PzYHlYgKfCTXp6FuDdbB0uDhpST2jpgoTr5VBlsGd4ndh8bDKJm9YhFa4nxC98omI6bEfzFBj_OrkCWRoVnjqHajCwIullS3XrzZ_E0gWMYxChqb-BRLI7HLXglM1heA0EoYMGzTFdNtyfQ5tomCACwkEFabLyS7RUXa_LMflgm1_Sf4HlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار مرگ بر آمریکا و اسرائیل مردم در مترو تهران
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/akhbarefori/666523" target="_blank">📅 20:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666521">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NpXlgE_vLleSVszpj107nnKpS789RQRDiPZspvo09o8NqFLoQxUE9Sy2YTZ1dqAcf-KjSt48ZwExypMWH3DOn4IGSFc2_Y1US2HCtICIYevW0EhdMSsG3CmJGBBTNZDENma9PlYptaVuNwkuBtouDdXOFA44UW9TtF0SH8vQy-N8RLT8F3ylyrk5447f_zhVLJGtquaU2wwKgZn_fmklgAiUkxDC52q5qhB04JhYh67y2g-8XgC14nhKOGmPXZ1IY8RIDhqE6S3V_R6llk9DhgnBbX3bzgd5McTtd_vKzNouM69AuG8UUa5CmNltphDHvmQpoacCTtvL-1Tu-PJbaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fSMNclHKCRvc0b5KG3GF3pOLrn3YTh3-Kz-9T5XhNhHOAW-mbEt53KvYlXN0I8Om60sETVvSCFy-fDNA7YuG_qzcTKIpSMLw_Cqyriis5961lO6H5-mEspk-6kGYKc3b_k9WDY8XPbK4z1wPIaQpA-B2cD6RmYnCpmxNEJmevyhSIlddMdutXbC5S4NB9I8JQjNxPYMrhE7jW4_I-_PlzCPetyN_dafaB-G4WTqPv6jcpVzPW509mXsNsYiukjSL76L-bnZZjy9y3Uapvt4BKP71rK0K1KHzrdmNUwL-f_Gnovq--sdLbaCli_-r1bB2FEyyG_pbzgIMP0n9oWOQ1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خون دلی که لعل شد؛ روایت رهبر شهید انقلاب از مجاهدات ایشان
🔹
«خون دلی که لعل شد» فقط یک کتاب خاطرات نیست؛ روایت دست‌ اول رهبر انقلاب از سال‌های مبارزه، زندان و تبعید است. نویسنده با نثری روان و بی‌پیرایه، از کودکی تا روزهای سخت مبارزه را با جزئیاتی کمتر شنیده‌ شده روایت می‌کند؛ روایتی صمیمی که خواننده را تا آخرین صفحه همراه خود نگه می‌دارد.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/akhbarefori/666521" target="_blank">📅 20:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666520">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
اسرائیل در پی چراغ سبز شورای صلح ترامپ برای جنگ علیه غزه
🔹
شبکه‌ای عبری گزارش داد که ارزیابی‌های رایج در این رژیم حاکی از جنگ مجدد علیه نوار غزه ظرف دو تا سه ماه آینده است و این امر منوط به چراغ سبز شورای به اصطلاح صلح ترامپ است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/akhbarefori/666520" target="_blank">📅 19:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666519">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5608cabb7.mp4?token=Fgt-CkGkTHfryXOoHIC2_W_rikqVrT_iAOO4RpdPjelD0XJH9zFfSkOB14479M_2KF8JK4zb9WyMG2qQHW1fVCGq0bQggYobTDk-BHhssccsm7vJBnPDZU3LZOSzZKcpnw_01J8Du0SjXIsMdS7a5IE5FUara4KiUIIZI4Gd_lB8R0Y-AK-LOUDsXS4t84ySIiV1SrXyNdW9cqmRiTSVzFrCS7JnNJAatnShJLAJKjgGMVo7OqlvlGUZ8-pRBEQslPCMqpnwOTGd19HhFcIYUShwD4yz9G8D7awnrsl0gIfxPDJvclmhUmSwL2P3YWD53MlPuXNgengdc2JrvvB3fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5608cabb7.mp4?token=Fgt-CkGkTHfryXOoHIC2_W_rikqVrT_iAOO4RpdPjelD0XJH9zFfSkOB14479M_2KF8JK4zb9WyMG2qQHW1fVCGq0bQggYobTDk-BHhssccsm7vJBnPDZU3LZOSzZKcpnw_01J8Du0SjXIsMdS7a5IE5FUara4KiUIIZI4Gd_lB8R0Y-AK-LOUDsXS4t84ySIiV1SrXyNdW9cqmRiTSVzFrCS7JnNJAatnShJLAJKjgGMVo7OqlvlGUZ8-pRBEQslPCMqpnwOTGd19HhFcIYUShwD4yz9G8D7awnrsl0gIfxPDJvclmhUmSwL2P3YWD53MlPuXNgengdc2JrvvB3fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: من با رهبری شهید وداع نکردم و نخواهم کرد
🔹
رهبری شهید برای من همیشه زنده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/akhbarefori/666519" target="_blank">📅 19:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666512">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Du5AqvF7-f7zcofVSdA2p3kpTVh7vya4LA50HGCME-xe70XjsnNl_X1TogyundQky-P2RF1tbeqRxw7vojh82xq7pFwiV_FjvR7yWY9eHvFm5379HXsKieHHrZzbpAWc3bhADidinGvbgk5RbcRIHlETD3MCDgS_ikCkFjTnasxj19M-uEoz2UV6_mHrAiaLtQODPpexGNWDEO8lxMNon7QCA_kO-JZU9uUUNDNIDrOQXy2MmOUVTRVTEbJuvVzcW9ehD6vu8AZW2IKxPsahE_uJOaO04OirIjwYf9kLTYmmEWH1QLtLaFRxSG3glxT_hzmMuMSKMwgPuMNUbmEClg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uOlpnPcjRTfW3gBpVtM061XPA58vojrRiUvQbiiRUWIofzNFPweXdg5oV83OI7FtoIlNpBd5F8kF6KBu8e9gN2WBYuWzLOkB-smD_SIamrCDKEnRNpSDtXXR7zVOfR4fw9YLjge17PyIrKlQk7FIosT_SZfwlTSIyJds-MGy64aR12DQK9DZcUfQopHSMHBNaWlZ7WDTaBB9gIo_t1AOmQmAj8_34s67drDs8_JrhQ1lP-LktnEpOX5wEMEGuWYwVNxzSlnVuOGAAVCtN8L-MVGtijFXQTS24ZoecdpEmcGFaxROI0goYc6wDYujkN_6YhXJzBdyYXDisgKXBg-esw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XbFsO7quRS2dEoo7_KIXz7mUpnPUT94TEKCHNmeOp4wiJT6uVdrzp_Me-FCZE0mnwyhaN1o7Q-m7zeqzcdX2Q0lalpRkJvXa7V0mWCWvBAqagdk6Uhymdszkb5EFCBCtXEJCU0hnG2N0BNehkTmhQ_om1YLINlKK8wTn7O1GRxRHH6e71diAAM7qGLjJLZV7lZZTDVlGcw5DCw1UTE2WNGhC4YzwTRF2KqFq9oUQBx6PG3zbTTeOoKtew3joiCXoi4MC9FlbqEsbh-QyaqVpbjFq5_UWCOaMnGh7OJy7vol4_OCIVqQy0yJeAkuuirrI-Kpk7BdELu9MYJbcZeNL2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GRWjgGWZ9kCH70Rcoc0lYREAjYc7dQwJVOzalY5alVZqoyfF5B5AlfkZXTNzu8rH_odVzPtcncJgYlQVVVjD_v5WeYnLul69PbQypTlynhgWu-YaAqV707hdhUeJXJPslkK1xHo9dW45cno6nIkNaa1xtBbj3BKU3XzoB7xCotsc2BlU8GblSzWq-2wViZDy4qHfos42Y7it2rCeLZhIGmgIaQ_t0_QtKu9FVMl47YQSZt6hvoRHmTip5yJZcv_aPzxYglyQb3mS4Q5VgQzyKGVJJ_eYEndVy9YwQI98GGfJsFMNjlE-yv_JAWWpe4VPYCNvNEsqXje1mLSevkX-mA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cac4c39e7.mp4?token=NE5IYmHHuhinZRpL_m9xMOw0P3YkXJl0JQsY6IJ-nPKVHWEjeuGValVe1s4lpVo1HrQhPodw4o-voMUY4Ye8Dmm0I1WqeNXNFdW7FnW5CoJcRq5dXVDhHRILTG14AbKC3qWZ3JjrAkKP450d57af-oAAAHC2IAId9MRG0neeMY84QAgnzmcEYfr8E217L7Qd0Egr1QZtPIY2N5oP88YmcbniU1nIjgwbHl0I0vmAxmpJkSxfRdnQ3tWAy9au-6bZIusRhFXb2ZwJ6N5q11vmCfXlUfn9D9uQvHf9gA5BIZI91KrqwgYgEnz7PY4lWTJMjmTcNqt83bklbAMPUHHGAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cac4c39e7.mp4?token=NE5IYmHHuhinZRpL_m9xMOw0P3YkXJl0JQsY6IJ-nPKVHWEjeuGValVe1s4lpVo1HrQhPodw4o-voMUY4Ye8Dmm0I1WqeNXNFdW7FnW5CoJcRq5dXVDhHRILTG14AbKC3qWZ3JjrAkKP450d57af-oAAAHC2IAId9MRG0neeMY84QAgnzmcEYfr8E217L7Qd0Egr1QZtPIY2N5oP88YmcbniU1nIjgwbHl0I0vmAxmpJkSxfRdnQ3tWAy9au-6bZIusRhFXb2ZwJ6N5q11vmCfXlUfn9D9uQvHf9gA5BIZI91KrqwgYgEnz7PY4lWTJMjmTcNqt83bklbAMPUHHGAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای مردم عزادار در آخرین وداع با رهبر شهید انقلاب
🔹
عکاس خبرفوری: سمانه صالحی
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/akhbarefori/666512" target="_blank">📅 19:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666511">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
اردوغان: جهان پس از توافق ایران-آمریکا نفس راحتی کشید
🔹
رئیس جمهور ترکیه امروز شنبه در سخنانی اعلام کرد: هر راه حلی که از سوی کشورهای منطقه اتخاذ نشود، پایدار نخواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/akhbarefori/666511" target="_blank">📅 19:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666510">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aW34zeaLBP_Eiiijko85p-LOmQbLF2K3G66zMWYsX3vSAk2X9Q6r5GxR2flC7rsIzuOkoQasmn4fctDxl9XHmQB0Vg1EGM_Bt4vuqoLkggytQUB6mVnTYALdAJBEXX4QpFBX9S1w_he-cgmJL2jFwlB-oRHoKruVA0MjlToCsdqJMzedsZEiiwepeGAaUMkkj282KEAqCuHADRU7lqxXTVevBpltenfUP8CJ0smliISkjkOhZAN-MjP7IN2p4oSrOTAm7vhbBHj1GNtWFLf_6U837Ulufoxj5Pxwfta7SXUwTqZwBQZBArA0zd6po1ngghE98luiXilFQawHa38ByQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال رسانه‌ای روس: میزان محبوبیت یک انسان در آخرین سفرش آشکار می‌شود
🔹
میلیون‌ها نفر آیت‌الله علی خامنه‌ای را در آخرین سفرش تنها نگذاشتند و مردم جمهوری اسلامی ایران در کنار میهن و رهبر خود ایستادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/666510" target="_blank">📅 19:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666508">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0145dd6a7b.mp4?token=BRISsvmYGOiz84Jknut6bhLuFiLD-o7mexPjz_0I-YNSWWotjPxbyM_vQyxM0D3OhYNr-AcQdvSep5KJCBNhxSKrGi2fMeOqpD4j7vAqqk7z0T6UTN2fnyfUcSUn2oDI-q3_fwk5rF116XOiZ7i8XCf-Tum-fqCrFM1J6R_TP7ukDw_0pBz_ER7kKS819T-xCi6tWvmNASal66mavJF8HNER7_xJ8ayLQwPTML8IoBmit-O41csFgOgcf-NDbv83tpfp8WBA49QzxsDSnBcG2P-6vY_7Lt-6sdo6F0leo0PbW2bU5do6GbHFZE7hb7PEAYyYXPxOHIAWZOM2KhmlnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0145dd6a7b.mp4?token=BRISsvmYGOiz84Jknut6bhLuFiLD-o7mexPjz_0I-YNSWWotjPxbyM_vQyxM0D3OhYNr-AcQdvSep5KJCBNhxSKrGi2fMeOqpD4j7vAqqk7z0T6UTN2fnyfUcSUn2oDI-q3_fwk5rF116XOiZ7i8XCf-Tum-fqCrFM1J6R_TP7ukDw_0pBz_ER7kKS819T-xCi6tWvmNASal66mavJF8HNER7_xJ8ayLQwPTML8IoBmit-O41csFgOgcf-NDbv83tpfp8WBA49QzxsDSnBcG2P-6vY_7Lt-6sdo6F0leo0PbW2bU5do6GbHFZE7hb7PEAYyYXPxOHIAWZOM2KhmlnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: من با رهبری شهید وداع نکردم و نخواهم کرد
🔹
رهبری شهید برای من همیشه زنده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/666508" target="_blank">📅 19:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666507">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c315ef6a62.mp4?token=SRajLSA77hhxHe701oqCJVacT38Xmzf9uzXRekTgqIzZWKvBNxz5b5e3NBVA4bbCVWr7vm1ud3OKXbHBfozKd-b70gdAibOhufAJqt_E36ioD6-3lzui9kuY1rb1DKb05QQfcz5b798dgn687U5BaQ7a6k12ywdlA_lAmrCJuVEkfsOs5yZPuMOTwUKTKDJkBc-KyyxlUdSFftSd1aKEW1ONbgp3dQd9_98sZCAGTAWa8jWFRhD2L9Q4DkvF-ejjPBweAx1PLBIsaa5oKlFZYI-Xs7ogeX8iW7YNvVb3N_H2kMw9Le1sMmsvup7dXIokCVAbvllSg-WDuthrhD_fcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c315ef6a62.mp4?token=SRajLSA77hhxHe701oqCJVacT38Xmzf9uzXRekTgqIzZWKvBNxz5b5e3NBVA4bbCVWr7vm1ud3OKXbHBfozKd-b70gdAibOhufAJqt_E36ioD6-3lzui9kuY1rb1DKb05QQfcz5b798dgn687U5BaQ7a6k12ywdlA_lAmrCJuVEkfsOs5yZPuMOTwUKTKDJkBc-KyyxlUdSFftSd1aKEW1ONbgp3dQd9_98sZCAGTAWa8jWFRhD2L9Q4DkvF-ejjPBweAx1PLBIsaa5oKlFZYI-Xs7ogeX8iW7YNvVb3N_H2kMw9Le1sMmsvup7dXIokCVAbvllSg-WDuthrhD_fcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حیرت عکاس سرشناس آمریکایی گتی ایمیج از حضور حماسی مردم در مراسم وداع با رهبر انقلاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/666507" target="_blank">📅 19:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666506">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5700bf5c0e.mp4?token=vAvDgM204aBBJIGXrlCnytEs2Yq9ibr8qouc5LPyfVQKXLAVc-psopk0KWlotbRVJs-1tKTsxSeqRUSx6K0jfNrCrNEGBQWX_O24OJfK1vFq-vIedEH-kXZFJEHJrSRbID5qqTC-6PIbc_iUQO2RCdavr_TOzdPDtRPlKSJPjss7BjYM4w7BdXpjxgwR5KA4CM1m4VAgUFEEAgvyiKEP_UOPzQUap-WrHmytu_019OuyXJYqmlT_sXZFPOQf6l8Tr-lwGh0jir_ak2nPO8doLCzeA4gPYTjhIIfOlvgYozEhghWCECDjIb8crlbuz2wIHBrpazibAEK8aiTqcYT1_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5700bf5c0e.mp4?token=vAvDgM204aBBJIGXrlCnytEs2Yq9ibr8qouc5LPyfVQKXLAVc-psopk0KWlotbRVJs-1tKTsxSeqRUSx6K0jfNrCrNEGBQWX_O24OJfK1vFq-vIedEH-kXZFJEHJrSRbID5qqTC-6PIbc_iUQO2RCdavr_TOzdPDtRPlKSJPjss7BjYM4w7BdXpjxgwR5KA4CM1m4VAgUFEEAgvyiKEP_UOPzQUap-WrHmytu_019OuyXJYqmlT_sXZFPOQf6l8Tr-lwGh0jir_ak2nPO8doLCzeA4gPYTjhIIfOlvgYozEhghWCECDjIb8crlbuz2wIHBrpazibAEK8aiTqcYT1_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: رژیم صهیونیستی به همه کشورهای منطقه حمله کرده است، آن‌ها عامل بی‌ثباتی منطقه‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666506" target="_blank">📅 19:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666505">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
پناهیان: ما حاضریم تمام منافع ملی خودمون رو در راه انتقام امام شهیدمان بدهیم؛ ولی انتقام را بگیریم
🔹
ما همه هستی‌مان را می‌دهیم اما انتقام آقامون رو می‌گیریم
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666505" target="_blank">📅 19:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666504">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b194b778db.mov?token=aqbNdJAhrDmkm_a8YiodfVhk5q1wqoue_Td2d_oP7YAkVaVA8zvyKuyYu0rjqbTp83UWmN10PJrqYKFdPunoPhmRFr6BFvXJEUx20oK9WBR48O8myZsVUn_8h6tCA7tdlKYPqkk7nafZd1iviIL2I_QthWKopg_-0wSVOFMvF1ge33F9OGdOJeiPDCfZeNQEUGMaTGVKT80kX6H0HoOnd7Bq0JSvZZh2w6Z7iAz8jxo86L5DWazPA0zj7SkmReDLfblDDfrywJyxTUY4RpLXcGO4IJE5Lq9o21MVH4Mhj4gHIS0MTS6TI7LETmWVL84BBLDjF9TVHY_5e3cKxI_DHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b194b778db.mov?token=aqbNdJAhrDmkm_a8YiodfVhk5q1wqoue_Td2d_oP7YAkVaVA8zvyKuyYu0rjqbTp83UWmN10PJrqYKFdPunoPhmRFr6BFvXJEUx20oK9WBR48O8myZsVUn_8h6tCA7tdlKYPqkk7nafZd1iviIL2I_QthWKopg_-0wSVOFMvF1ge33F9OGdOJeiPDCfZeNQEUGMaTGVKT80kX6H0HoOnd7Bq0JSvZZh2w6Z7iAz8jxo86L5DWazPA0zj7SkmReDLfblDDfrywJyxTUY4RpLXcGO4IJE5Lq9o21MVH4Mhj4gHIS0MTS6TI7LETmWVL84BBLDjF9TVHY_5e3cKxI_DHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استقبال مردم از مراسم وداع توقف مترو در ایستگاه مصلی را لغو کرد
🔹
به‌دلیل افزایش ازدحام جمعیت، از ساعاتی پیش قطارهای مترو در ایستگاه مصلی توقف نمی‌کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666504" target="_blank">📅 19:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666503">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1df790d290.mp4?token=bBVyNvj3JDXLegXL7e3InDUwF_suh1SnwB67AIHn5v33j8UudokfC2z8oM5sdUu-_3z4lIf3hzlPvbyZmRTJFvjLM0pwFTmY8Wb58ynQ1pshFdT_hvk6AeGnLIc0OfQn9NrwCQ3-sq1RIMaVWjkqRjuVRysFMbBNcfjiiKX94Rl6mHmX3631TEAEdOwbV297I8A69l9psowVj-3JmBSkyt5KErZu0UK6sAPgsYRDKEo6gQNRbMk8XuH83LkN8t2-Ez8hzIc_rSz6QALMCxYnKdaDON1qrk-u9rahHKkaaBK3glQ5TAtHxheeCFF7FkFqKfv16Fcdej-vVVTmVNEkMYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1df790d290.mp4?token=bBVyNvj3JDXLegXL7e3InDUwF_suh1SnwB67AIHn5v33j8UudokfC2z8oM5sdUu-_3z4lIf3hzlPvbyZmRTJFvjLM0pwFTmY8Wb58ynQ1pshFdT_hvk6AeGnLIc0OfQn9NrwCQ3-sq1RIMaVWjkqRjuVRysFMbBNcfjiiKX94Rl6mHmX3631TEAEdOwbV297I8A69l9psowVj-3JmBSkyt5KErZu0UK6sAPgsYRDKEo6gQNRbMk8XuH83LkN8t2-Ez8hzIc_rSz6QALMCxYnKdaDON1qrk-u9rahHKkaaBK3glQ5TAtHxheeCFF7FkFqKfv16Fcdej-vVVTmVNEkMYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: برای چی باید با هم اختلاف کنیم، برای چی باید بر سر جزئی باید زاویه درست کنیم
🔹
این علمای بزرگ‌اند که وقتی یک زاویه درست می‌کنند، در پایین مردم عادی به جان هم می‌افتند و مسلمانان مسلمانان را می‌کشند و دشمن از این موضوع سواستفاده می‌کند و ما را در مقابل همدیگر قرار می‌دهد. دشمن آدم‌های آگاه و توانمند را به شهادت می‌رساند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666503" target="_blank">📅 19:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666502">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-YVsHtHSXxZmw65QU3AvZu8tBUhdnc2ufSlCVC1rtiWB2nNfnRZ6fHlFSQy7-xg4WjkacoLs7gGzR8C1XvlXvho9iaMopXUzfj8jREkJY9loj8zP7GPaXs7jo_Aj8gW6YJe8Fueyefy9Cqs0CcTAs5a284CQzClNj0e5FPkr8HG64c2KArjN5njgSiHevzbKKvLr7vHxM8K1npSqvWBD-P914Sh6LFC-Wmf170Eyc-k52PB4omotikV2eVY4DosHzgCA4byil7iXaz9O3ND6gMK57BPcY34EeCr0wEh0EqCMF0KL0vPqaWA2muzNVqYKvxYBsLyUd0B8mGYO47mcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان نتوانست حضور گسترده مردم در مراسم وداع با آقای شهید ایران را کتمان کند و اعلام کرد که جمعیت عظیمی برای تشییع و گرامیداشت حضرت آیت‌الله خامنه‌ای در مصلی تهران گرد هم آمده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666502" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666501">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
گریه بی‌امان دخترکی که با ویلچر خودش را به وداع رهبر شهید رساند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/666501" target="_blank">📅 19:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666500">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfaf30c6.mp4?token=MKY9W1rD-0W5qRGVcQzuhD0ViT2EYzcmnahdiv-wL3oFRIMqqkQf6XOx7u81SPymy-GNafsbrcCfY49kFtQwlyD6MwuxgKla59QZj8xyJo_Sa6LJe3oxNjrU9pGuglKyW17ZfI4lmfpjaIBD2vBE2s-RPrk5AFxDSziAIGCq4rK9eTIBy1lOdRSQ5UkUSaE0UOsT1Z_Pcou_kgpE9VhK_bnPaWUFKpPfrit2-ZpbIKzxAuvwvWaFdz4mFzYxIOYeJhJjt5k8dKAlhrLRcl2Ar5uB1iKK8oewCwJ-3lt5bLGjchhJVW7b7361Sa8lhhT9nirLxwEFqj6y7wD37_OgTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfaf30c6.mp4?token=MKY9W1rD-0W5qRGVcQzuhD0ViT2EYzcmnahdiv-wL3oFRIMqqkQf6XOx7u81SPymy-GNafsbrcCfY49kFtQwlyD6MwuxgKla59QZj8xyJo_Sa6LJe3oxNjrU9pGuglKyW17ZfI4lmfpjaIBD2vBE2s-RPrk5AFxDSziAIGCq4rK9eTIBy1lOdRSQ5UkUSaE0UOsT1Z_Pcou_kgpE9VhK_bnPaWUFKpPfrit2-ZpbIKzxAuvwvWaFdz4mFzYxIOYeJhJjt5k8dKAlhrLRcl2Ar5uB1iKK8oewCwJ-3lt5bLGjchhJVW7b7361Sa8lhhT9nirLxwEFqj6y7wD37_OgTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رجزخوانی متفاوت یک جوان در مراسم وداع: از امروز موشک‌های ما با بغض این مردم پر می‌شوند نه با سوخت جامد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/666500" target="_blank">📅 19:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666499">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKwby9bP_4dsWj1z13vTKvoWUBWFWguYkzZNuT6b2Coz1iMW6Ynfp1M2AZDTDBHsuN7F6K5IeuYN3s5eBVeC92EQJ5BcFCwJLWlATjrkaQ6F1tf3nZW6bdQrXswZl-CuSxnEAEVi9V0xhruesEMEubUqLs89rWwszJY4bluZ36lnhwIKXponUbR1PTiRbvTf3S-xu2CkQ8z7MeAfMr8ERkG3xtan__EHYi-zmHw4FoNOXsxF5Et1JRoioffte8YwcDrZxFRhDG4mEQThLQD-_R3gg7vw4EvxNcixCwsEhqNwbDg3TIGb3KMxpDdVTfuTNw3ShpcTkEtR6hHWz3mdmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ولایتی: خون رهبر شهید باعث بعثت همۀ آزادی‌خواهان جهان شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/666499" target="_blank">📅 19:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666498">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
واشنگتن‌پست: مراسم بدرقه، نمایشی از مقاومت جمهوری اسلامی ایران است
🔹
رسانه آمریکایی روز شنبه با اشاره به حضور گسترده مردم ایران در مراسم بدرقه پیکر رهبر شهید انقلاب اسلامی نوشت که جمعیت حاضر در این برنامه، «نشانه‌ای غیررسمی» از حمایت مردم ایران از حکومتشان است.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/666498" target="_blank">📅 19:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666497">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ملاحظات ویژه ایران برای چین در هزینه‌های تنگه هرمز
سفیر جمهوری اسلامی ایران در چین:
🔹
تهران با توجه به تحولات امنیت ملی پس از جنگ اخیر، برای کشورهای دوست از جمله چین، در تعیین هزینه‌های خدمات تنگه هرمز ملاحظات ویژه‌ای در نظر خواهد گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666497" target="_blank">📅 19:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666496">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVzn5PPLvTFHjWCO1WvGFywXMkimokELWpyyPvSOf6fy1AOy1aRKW_4UhBPU8AzGe3V46Z7Qr_OBe9sZs-9e1y2hcvDkCtsaDZD_SzNO5nqYH6JXzkjJOxx5aACLW8s_Llz_KSe6BJdWje1S7IGpXWnWui9HCiLBYE2NLiwnJMY7fkwHqj5RurSk3R3YRS8pB07TH0jCfYgYbNbDN9aG0jNoXQnQGq3u1WiRhhwP_XMFPdqNLSCe45LTcQCC4xNP0XICMyulQLsZFsgXGsNSlFAWPwAOIcZJVIUXAmYnJnk7KMYvirxY1hGjR3POvmEYXq76Uu171RpFwr-mFqkm-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666496" target="_blank">📅 19:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666493">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mbksYADpSpQe15jxd_IH_iCbLrHZ300ceo__kpKIL5dQQZju-Cg_rUzt2BuGu6YBQ-ld7Udqc8QeGTeW2atmgUQorJTlCtzHbWGxuBdcyt6WcsRI3R4u9OSuPD9Agnc2kssOPO6bZhRDCBXWgvjDn5Onkhw-743cG309wwMvqUnMu_aIyNvAKbNPfENb_kWp3YGWl6zIs0utOfSi2BPV54T7aiPXh7Flde67-m3W9I-q5k_lDyimY9eMeS0Tdf6yhWI-kFHv3gHLhcgb35T6GnmZZNpbIiHgErZDPxaKTuDEbpfd7k_XRs46CCqe2mUM8PNp0Mygh3yVMknPfrfnUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gfLRnyOStcJAEuvhRIds045MOue4sxfN1-NS4rklG7NnuCI9ixYdfr611nVYh0hAgicsAh2qBThwQ6ZT_LALg0QurNtIu6oNPWvWYLUNThXFQeANAJnmxQx3Um0KgmrcV-qF0YfEddJ0z1rczDCBpwpVNx4HXF1N4HrfTpQ7kUyX6xs695Oi5ptUqPhgzT-4YSvblbVRY2bsp1MBQVaXpkx7HLB6LefCYDz_kNPnLGn7wSRSFGpoVwHAu1jRWOzTtN5FzKKef0rbqsWBcgQnRgFNSCm4FkpjXWLFp_qXwiLeuJOzBzPMKtLKG3d7ATBdFMQY__d3UNPIgO9bMlRrVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fiWYQNoJoh8iAa5BUAUNw89KWenwGx7cXFhgAs7oCkkL96w1eY8ttrzCKGNqNqO4ns9hvOjba9LEGyvYnnYI1sL6xbxpbjAQAWlfIx7KV0h_uzYDzuQjnnKme7hOgWZsL7Iiu70sHrTk9a_-wfWFquy1Khz7ck0CyRY2zExLIVDhyllOpwJ4EZaz1l00Dcq2qBWFF9dlKyOFS1eETbIZssnXWaOx1-m9h_JadzDK_WqXj4mtrLt1jlpdPnFSEh3LgCJzpcH5p2Q5oFBOtptuHgBiSakmDan3U2cFAzehjyUQeYAduKiZUo00UyxfW-IYDGZ5CshObeJcqppm4VNzrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حرکت مشترک سه پلتفرم نمایش خانگی همزمان با مراسم تشییع رهبر شهید انقلاب
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/666493" target="_blank">📅 19:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666492">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ry9ENv6F1eB9dBiI1Tvhm4vlObdyaOSULG6ETvLacJcmeP1NzwRfksqshv-kpA-stUaWt0eHjHZUKs5grkwdlEUNegRe-L5plvzdAUlodkH4WeZlexTpE8Zn7b0EMw45NmwJ3YS-g2G-e4OZWDdT6x8r4tYOTenOgVMT9WjGZLyMa3oqjBo8QXpm3q0nUYmosjG_t4hVaJcDDRiAVs0VIP0hEED5RWFtTUV2tIZkwotsjWHSrtZP7KetoLvfJ5dLS7FnfQ2P2CCiSANGItw9qVzb6ahxWzUOYOkru-TkpQ2FlJe6Oj4PwBvNry_8TokKuM3d5X_c1JrtDLxgiKQnkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میرمهنا؛ نماد مقاومت در خلیج فارس، الهام‌بخش امروز
🔹
میرمهنا؛ دریادلِ شکست‌ناپذیر خلیج فارس. زمانی که قدرت‌های اروپایی برای تسلط بر آب‌های جنوب ایران رقابت می‌کردند، او با ناوگانش در برابر آنان ایستاد. با بیرون راندن هلندی‌ها از جزیره خارک، یکی از بزرگ‌ترین…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/666492" target="_blank">📅 19:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666491">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d664908bc4.mp4?token=o1Y7z2ZHWFEo-kq0xJK4Z41Zkp1zEqrUbHZrilVWxUYdwlGhl48i9irEenKSkKUT4VvYnQYgrXkblyQoE-9015u88rfwQIB8LaVuE1OQNvGwT5Rv6WBvuh9wgiz8tQD7lrPPc1hg6VomDssmazgaftd7AavB9AsfwDdoZvNtjCI5L_cgJMk0WI_tlRyCn9dSnitAueQe5FwbAhgKWYGmKaPPcPbnb2og6xwfpJw9JPK-8yVx-kmLvKy8urdJjDQIb4ds58wkqXOMjBEjYYC82I5nQDD7gQ4POEPNz4ScQBGHc6MpOa_ri5974RjQvrHShrAovMFHHY5A5NdCak8rpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d664908bc4.mp4?token=o1Y7z2ZHWFEo-kq0xJK4Z41Zkp1zEqrUbHZrilVWxUYdwlGhl48i9irEenKSkKUT4VvYnQYgrXkblyQoE-9015u88rfwQIB8LaVuE1OQNvGwT5Rv6WBvuh9wgiz8tQD7lrPPc1hg6VomDssmazgaftd7AavB9AsfwDdoZvNtjCI5L_cgJMk0WI_tlRyCn9dSnitAueQe5FwbAhgKWYGmKaPPcPbnb2og6xwfpJw9JPK-8yVx-kmLvKy8urdJjDQIb4ds58wkqXOMjBEjYYC82I5nQDD7gQ4POEPNz4ScQBGHc6MpOa_ri5974RjQvrHShrAovMFHHY5A5NdCak8rpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احمد نجفی، بازیگر: کدام رهبر یا مسئولی در جهان، مثل رهبر شهید ما با علاقه و دقت با اهل سینما و هنر تعامل داشتند؟/ هدف ایشان ترویج فرهنگ و هنر در جامعه ایران بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/666491" target="_blank">📅 19:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666490">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
حمله بالگردهای رژیم صهیونیستی به جنوب لبنان
شبکه المنار:
🔹
بالگردهای ارتش رژیم صهیونیستی در اقدامی تجاوزکارانه، مناطق مسکونی شهرک «مجدل زون» در جنوب لبنان را هدف تیراندازی قرار دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/666490" target="_blank">📅 18:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666489">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
تهران؛ کانون وداع با رهبر شهید
الجزیره:
🔹
تهران به مرکز وداع با آیت‌الله خامنه‌ای تبدیل شده و جمعیت بسیاری در خیابان‌ها و مصلای امام خمینی (ره) حضور یافته‌اند.
🔹
این رسانه همزمانی این مراسم با دهه اول محرم و روز استقلال آمریکا را نمادی از تداوم رویکرد مقابله‌جویانه ایران در منطقه توصیف کرد.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/666489" target="_blank">📅 18:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666488">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ایران یکشنبه تعطیل شد
🔹
هیئت دولت پس از درخواستهای متعدد از استانهای مختلف کشور برای فراهم شدن امکان حضور مردم در مراسم وداع و تشییع قائد عظیم الشان انقلاب اسلامی و با هدف تسهیل و امکان حضور گسترده اقشار مختلف مردم در آیینهای سوگواری، روز یکشنبه ۱۴ تیرماه…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666488" target="_blank">📅 18:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666487">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-A9SLbrT3M1BZPFM6HsEw9-NxgSy_6c0_zWD_6bCriqlQcMRlDpqFw8Wg2B-VpPq0N0c989Qpk_ThsNV2FUhKq8aC4gF0Cfr-jBSkNVXRxaCnaCmO3p_fL5UezfaoCn0oI9NUX4R3eDuI5DjTSd6t_IWMYfr9OafdArDCTWXGAWzNfx9T5N7kKuhpmMLlo05x3dPR_zioKqWkb5PRGi2vrHwMHxJBI3ozK-36lnJf3OC7ZG_2uZO2xFxV9u1DZtFQXPbkLYf7DwxxtjmMQn_a5501Znecn7tR5L-L5IXPLQTdua8AqvGJYMcYY9uN36zQBsYgx7eBcXhrsyltWswQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/666487" target="_blank">📅 18:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666486">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqV1hwhtpxDH0KY_Tsnkt6iFW0wlgEAWE5y42ALugAPd7ug9dUFGo4jZFhvif5yuymbL3bn97QqSZGfvDocBgC_OPJZkNE2wIIunGbb1fvm9RuPKdVG-5HKiLEgBwqsJsWWu16yV29AS4k4HuMDEh9SGdffXfBb8Zfiszmd6l8ACcQ9nHsABXD65yA7KTmfHJHvKID96GEib3CSDXJ2kuTAd4xDqbQcASXCd2zJ-bDLql2_T0ApmQhl1B9y5k6l7GI4kq_T0peiWfN2PTDgrl8rfrxUZxyRiZip9XbiCeonyYMzN_0QNpOYLyf9od2HKp7G2N9S3lJmegeXcAXyE1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر خبرگزاری فرانسه از مراسم وداع با رهبر شهید در مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/666486" target="_blank">📅 18:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666485">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
شمار شهدای لبنان به ۴۳۰۳ نفر افزایش یافت
وزارت بهداشت لبنان:
🔹
شمار شهدای تجاوز رژیم صهیونیستی به لبنان از دوم مارس (۱۱ اسفند) تاکنون به ۴۳۰۳ نفر و تعداد زخمی‌ها نیز به ۱۲۲۰۲ نفر رسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/666485" target="_blank">📅 18:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666484">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15bb4eea1.mp4?token=taxlt6Y1wtiZRAt0igRHaYOXqMoWzA3pDCdL5t21E6Wkg2q_fPcC_10Zd3ygajZeD3DvTTNx9D91UNA-WpjV8UmByxnUxmQb7bQKZb3Nv4pRASzFn6TFKQy_I3KynLyZsm1gvcHAQBUpNR4Gv00-WYaderiO3fQUfiRXJiCMImfL_HQlKhJG4C9ZLkY0BfsDPpoFA0_oJ7H01Q0JZyLGpadgDlu0verF-O9remR_a-07g8UXT6aKbgTKLIAqM2DSMRRQ2rEuLDH-twO1zf78DVf8hSQvghidTFJt0sxC-kO4_-gTtIwKozv9CYOLsyQUI7zZmMgHXwsReyyxc8TT3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15bb4eea1.mp4?token=taxlt6Y1wtiZRAt0igRHaYOXqMoWzA3pDCdL5t21E6Wkg2q_fPcC_10Zd3ygajZeD3DvTTNx9D91UNA-WpjV8UmByxnUxmQb7bQKZb3Nv4pRASzFn6TFKQy_I3KynLyZsm1gvcHAQBUpNR4Gv00-WYaderiO3fQUfiRXJiCMImfL_HQlKhJG4C9ZLkY0BfsDPpoFA0_oJ7H01Q0JZyLGpadgDlu0verF-O9remR_a-07g8UXT6aKbgTKLIAqM2DSMRRQ2rEuLDH-twO1zf78DVf8hSQvghidTFJt0sxC-kO4_-gTtIwKozv9CYOLsyQUI7zZmMgHXwsReyyxc8TT3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دکتر حسن ابوالقاسمی: زندگی رهبر شهید به قدری بدون تشریفات بود که می‌توانستید تمام وسایل خانه ایشان را با یک وانت جا‌به‌جا کنید/ رهبر شهید اجازه کوچک‌ترین فعالیت اقتصادی را به فرزندان خود ندادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/666484" target="_blank">📅 18:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666483">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
مشارکت ۳۰ میلیون نفر در مراسم تشییع رهبر شهید ایران
نشریه بین‌المللی کرَدِل:
🔹
پیش‌بینی می‌شود طی شش روز برگزاری مراسم بزرگداشت و تشییع پیکر رهبر شهید ایران در دو کشور ایران و عراق، دست‌کم ۳۰ میلیون نفر در این مراسم شرکت کنند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666483" target="_blank">📅 18:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666482">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUl0-RMfxFtqkwfurUwSgDJSxQA3cqnxV9azdnwq80_mb8YUMJzXcD6_qcFU7CMvEbLEgFI6_Z93LDosImUYLWlMiH5QeLLxkDjMLqtHI6oRS93ZdgUkrh_ycMyd4_E2iZq5HjpKIHpocA-kHUdIpzIP7Kr_DprNUA3aeHJ09daeQwo4sVd1sAHHnsHOYpHyM1NMRUyMxHIPH5PSbdOt9SQitKGQto2POFHJG-RhXh8wnR2hsdNwiHfo5txVBiUWROqRoS8xF1FOxRunFTWrgifPcHNhhNInwXABK043xQAExLu_o0cd_Zm7u8JEopjKS3-4hR4HfGHNq1WC2QLO_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط بالگرد نیروی دریایی آمریکا در شمال اقیانوس هند
🔹
یک فروند بالگرد MH-60S Seahawk متعلق به ناو هواپیمابر «جورج اچ. دبلیو. بوش» در شمال اقیانوس هند سقوط کرد؛ از چهار خدمه این بالگرد، وضعیت سه نفر مشخص و یک نفر همچنان مفقود است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666482" target="_blank">📅 18:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666481">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCxEI0PR3HTF4Ot8-u2twVyIgJNggFtHQXWOJFUE8USsDZey-4Wx8-KJRfulDyZusgh_jCqLUgbPPHqc0zzslQLouKE5mHwq3S61cL63ufiCiod-e3lwbulyo39u80JNbOUE8gWH-iJh51W-KMhgUEsb4OVWacQ0MX7IEsLLWaoprUUqpQXKlLUq8pe8TEkseK0a4krC6dpa6NpQDKUuJyO9p00B9hTCRxydQSNXgB2X7vdBNZWJmxIgwRlR3BQt11cofGbHKKrvTY-YtRdwczPielaewl_G9Xf51kieqG8ZxlicLnQ70Q2vkEc6n36DbNqMdUk3zK_Sox4WY6_XGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرچم خونخواهی امام شهید توسط عشیره عطاشنه استان خوزستان در مصلای امام خمینی به اهتزاز درآمد
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666481" target="_blank">📅 18:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666480">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56a0f3176.mp4?token=QPLJ4X2-YIoqMX-Dic7oHy6lPZyIApVG5w5r8vsSEV3xYtvarWvoKjbsJrnxgVGGWcbm5qpFm-MZf-mvoLB5XagCKdjqRaJz7LzwnUXy4_0-jvn2kxHtaZbqp6igZAaYyKiug_8ctyUJEQopRa9dAhEovU6xiHBUKMxkN0Htp0OoqUI5b1WGxxDdJEIfBp2qmnN4kaGm6YYa5XkTIE9vY_yGLEWgpvCvPtjUmUx3edq3u7JT92-WhVNPljBScqaYayuUOIPqlkzvnz7jmkwhCUc61apKchltwY2clDOIiEB03IQLFRQAQKCunVLxbQRiwCSXebBXB9rZ_3r08TWJXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56a0f3176.mp4?token=QPLJ4X2-YIoqMX-Dic7oHy6lPZyIApVG5w5r8vsSEV3xYtvarWvoKjbsJrnxgVGGWcbm5qpFm-MZf-mvoLB5XagCKdjqRaJz7LzwnUXy4_0-jvn2kxHtaZbqp6igZAaYyKiug_8ctyUJEQopRa9dAhEovU6xiHBUKMxkN0Htp0OoqUI5b1WGxxDdJEIfBp2qmnN4kaGm6YYa5XkTIE9vY_yGLEWgpvCvPtjUmUx3edq3u7JT92-WhVNPljBScqaYayuUOIPqlkzvnz7jmkwhCUc61apKchltwY2clDOIiEB03IQLFRQAQKCunVLxbQRiwCSXebBXB9rZ_3r08TWJXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احمد نجفی، بازیگر سینما: سکوت در مقابل شهادت رهبر انقلاب مایۀ ننگ است/ همۀ ما مدیون رهبر شهید انقلاب هستیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666480" target="_blank">📅 18:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666479">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
تشییع زمینی پیکر رهبر شهید؛ پایان مراسم وداع در ساعت ۲۰ یکشنبه
فرمانده سپاه تهران با تأکید بر اینکه مراسم تشییع پیکر رهبر شهید به‌صورت زمینی برگزار خواهد شد:
🔹
مراسم وداع تا ساعت ۲۰ روز یکشنبه ۱۴ تیر ادامه دارد و پس از آن پیکرها برای تدارکات مراسم تشییع منتقل می‌شوند.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/666479" target="_blank">📅 18:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666478">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
جزئیات مراسم تشییع رهبر شهید در قم
🔹
طبق اعلام کمیته برگزاری، مراسم تشییع پیکر رهبر شهید روز سه‌شنبه ۱۶ تیر، از ساعت ۵ صبح با اقامه نماز در مسجد مقدس جمکران آغاز می‌شود؛ سپس پیکر مطهر از مسیر بلوار پیامبر اعظم(ص) به سمت حرم حضرت معصومه(س) تشییع خواهد شد.
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666478" target="_blank">📅 18:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666476">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f42a2a3e.mp4?token=v6OpjekV5E6srNF3RvqnPwGK4q9x3P0gH3QE-O_elbZ-MNxl83FJ9pTYcATsp8T_ykpFxllIVOBgQDUJaZLFlAELNt_WruLl9nIeOfoyMYYbDUfZCMhoVPvU6jBFaj6CIC45DaZ6neLMrHLuEhJq6ByUD3qE_mSLkXVYxaADX8TSO5G4GoGsO2Yc_mldGS3jNHRqEp_yTVl_zcN0FvfKQOOdvZgSr7ir1U9Cr4DQm541QzlefqkLSxPO0CbrYO7iPyS3WSt323NAlIb-o95DsptHK4BQmZ2fK7Tc0kUPh06Cjxv303sNCv29R_uhHQ4-yaKWezOu0Yqphzx2KkCq2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f42a2a3e.mp4?token=v6OpjekV5E6srNF3RvqnPwGK4q9x3P0gH3QE-O_elbZ-MNxl83FJ9pTYcATsp8T_ykpFxllIVOBgQDUJaZLFlAELNt_WruLl9nIeOfoyMYYbDUfZCMhoVPvU6jBFaj6CIC45DaZ6neLMrHLuEhJq6ByUD3qE_mSLkXVYxaADX8TSO5G4GoGsO2Yc_mldGS3jNHRqEp_yTVl_zcN0FvfKQOOdvZgSr7ir1U9Cr4DQm541QzlefqkLSxPO0CbrYO7iPyS3WSt323NAlIb-o95DsptHK4BQmZ2fK7Tc0kUPh06Cjxv303sNCv29R_uhHQ4-yaKWezOu0Yqphzx2KkCq2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن محمدی‌پناه، مداح نماهنگ «باید برخاست»: مردم در تشییع فریاد می‌زنند که باید برای خون‌خواهی و انتقام رهبر شهید برخاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/666476" target="_blank">📅 18:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666470">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5wqaaImoYNyO9JCeqLK_914ZwqcbDj-NGJVxHYXLGrC1LTG38yZuW1oj5XRxfsQ6pmAioFCGFk3lQJ94Ruk-AHMnfnvc58YFZ7GrfxzM9cp8mCRhHzznzKrEIpzHxl5koHCV6hh38gaGU-ws03NkgWTQBj-5v7Zq32A20WTqOSr4S58LhSEI_jm5KsJuAy2lhSqPqDQNOYsB2_XIt1mJT-6lrBuFx-YmPuOI8aDoGVlkEIP9OiHRO5SUz89YfOLFerqwyaj957cNRjnmVNinZ3aFDFJ8IRVFWBh7EFEwf4GCvQwBl1qMmpYCNFVnpdyKpzoSCsR15_h30lfPr97Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oPTA_7m68Vz4DDc8c7to6VBnQLmi65uEiohDzEex4nFLUkRv1DxDL6FJDrnuHIvqX6RVXeE9I7XuADFKv-SsUcl6yhTewdNmg72H2XaA6bMvcSLN8Vnip_dLlrW9aMnqi2yM1ckrgtlj9SoIV9i66ZaXkjjKVjqmDRYSsBMnOBvPFglGOlqEqhlPfzrpFUeIcAw0oHjXTOEPr5118gutv2vFbApPdVSkLc3Z5VU9nVvuiKcSxRLfEU-BSXJK1s6T7wenPqDw7-lODoJvGgPvn209jDdVWjZex4CuJaygmX09JMK7hkdZnPfqp10WAhGc1K6KP8fFlhZWzDLS_tuqsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PqoOVaUZBQwW1SmNH1UFbQgOf8Qi5K-GUs40roftxBw-GspMYZfDiWUDv2iowIeZW03UZUcR55mS1CY-YuGFMqSrfoWENtIUIbxBrCh-keE4Na204GWLW-MQWZ35pf5ax5gUPwurJCX96hWyPEv78gPxUD9tX0z-0Q6THilSiw-EQTP0ZEV7zbN4tLOMfrE7DnwwNz1SBUF7dcWfU-VM6l9dakNYvRGBdYcxATDf2Entn7BaOa0ztzOxYz_rvNVfM9MdsdQEY60THAyfkSW6FQX2ffTYPj2rZqfe3L1cg5uN2telQ_JDyOgtUCYrRLRWAvUJGQEK-YY7-oargjmKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cQzxZTXjLMVmJJD6sgqFQPuf0Pf54ZL42AMhh_80TrnLwr-ljFOu1hCOJ__6XZkqKGPSCJg-ung1-BEhU_itqTwPxIUOo3RBNGunxom11CNrZ4MjqAOnU-uy1rRcNnSkwbBDQJ3TFxfaqcnZwDJLeHm5NwhoAX5inlg0Rv0hKuTrDrKQPf9qaxceHo1PktTNgNDm0_vJXhqDBHFzvkU_iAtnxXhsUzjGX-ZI9_xysnlTmOoL01O81GprWVD3neaOMe3dnxwu2jAWWGNwiQSpseBcYWcPjn5KLYEngbVeizTwJjj4IsrjKwP21MxpyuNRAwl4L2hJh2-3KEEQ2WaxCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RQqrwSm34bcg1PBs6p1hrujwEuH1OhQQ_gJuEXjLPCGQorbgKSHhutQMUaj6VBAGhUN8l3kGOLIvF1P9lZVOLyT3O0eIyVsrdWwmUkd-8n6Efh9mZA0miqBSWfh6D3IUqVGsAMWL-Xz3ie66DEjA28WfL0x5FBxueAwitIp5RkoICd99f0ruNHA6p5ES-jmocp8CwcnxdtUTfsFe4CdqK56AabKMTXWNbtIfjoGkIJvDtGdOOP3xiKLMHL1Dfs5ml-bzsr_UPyCsdM-VQ84S2JMFZxy420yJCRMcnqmDeOFb6z3CYp9rmsZtBVkeiNV_Wj9Clk-gCkHzqfI7moKepQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DFb501NoJzy088qDPI0f-LLzp8wT11e1lMuwEW-jH0Y-GK6aal-iAH_BwIHvGO9sxcoM_0BkWjqM2Yqajt-sCF4ZBYo_-dGeLCIzbZcduZ--8UURPQE-iHZtePD72G4axBlKGTiEvVprVcTlXAeGPkYeWzLE7sS6jhcjNn2KnF7yi6K8uTk1Ck0RYKhyLAfKForv4t7QEL4JrfVYq5NYxAVMn2gJrKAEo-xEUyH3Ey7evoCOhvN3jz7fODGLkA5QA7F5RFaHCgr36PaUivI4Q4onRsIg3pG7VsIIcGJOZd3dZY-vw67NsESeCeluNVLH2R2GjH8WF-WSky-Rk8aL6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از مراسم وداع با رهبر شهید در مصلای تهران
🔹
عکاس: زینب سادات اسماعیلی طبا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/666470" target="_blank">📅 18:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666469">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvaedDSaNQnlO-MoRLc2LhzeIerOcbiQVJUazVu63vC6uDIZYFxONdPL4lYv2d9WMQmmxLfqQW3unqZivePFpk2ftRE8cKjK8sEwWfLZxwku2PwZDURVYoicZtD48kHCRR_inGBE_Ftmnbh5L0fFG2e8DOXL50tqbrXA6p0FSyaraakUDFAusnebkrDKqQQaFOSgXtnWAoKraXH5cbTuB9oWyVIX7v5enkIWNCJVD2Q6IM3kOsQHMllHgGOtjltwXrMQuQ_hKP65bCtfLygvOqINFuiPH6NE-jvQLODwicTut62NfTvqokNOuV5-6As0sLDDStPvXcXZmE91Q4o71Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کوچک‌ترین وداع‌کننده با رهبر شهید انقلاب؛ نوزاد ۴۴ روزه‌ در مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666469" target="_blank">📅 18:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666468">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CveiMGm7P7ZTNvwSKZ8_qxIyP874zBDAWCxLHJYOnSmZjExnWFv8rjvnr88l9yRlGTzsNLahtcSRsWLDQiVJIcqE8CzjRqjjQJpPoqOjluWqAJzcN44wlZFVdk_VeVDmZhu0ZCNgAWQ77P61E-O-_f0kYBj51gCm3VAfn8YglqYCFpYr3rrjsAMQV5JvZyM_100bNXK4uvNAJj-8-aDBXxdvEuaVeYLL2o0dWLfB-0N8_HprTH_1IZ2X3p48GLLttGT96PLv70vrwEcWQ6k5u0n4Ytp0YcLvk4JrmjXBo6ju0Dqh6aam6_stglIKZutI_5q9Gjngxm2aF6CWhhtuGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی ستاد تشییع رهبر شهید ایران: دولت عراق برای هماهنگی مراسم تشییع ستاد ویژه تشکیل داده و گفته شده به خاطر محبوبیت گسترده، کشورهای مختلف خواستار میزبانی مراسم بودند، اما به دلیل محدودیت زمانی امکان‌پذیر نشد و در چند کشور هم مراسم عزاداری برگزار شده است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666468" target="_blank">📅 18:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666467">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مقام ارشد چین: به توسعه و تقویت روابط با ایران ادامه خواهیم داد‌.
🔹
اوکراین ادعا کرد بیش از ۴۰ درصد از ظرفیت پالایش نفت روسیه را غیرفعال کرده است
🔹
قطعی گسترده برق در کوبا ناشی از تحریم های ظالمانه آمریکا ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666467" target="_blank">📅 18:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666466">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
صحبت دنیامالی وزیر ورزش و امور جوانان در آیین وداع با قائد امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666466" target="_blank">📅 17:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666462">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eeBNw99jewJjXZJ7KMR4ha7-2HJMW7DsiybJWv3UJl-p5LsQNrkKu6U8el65ThzKCtkHqyCDKrtRoupPoP8_6w4DO8wbvN4V6zwA-sdqGc5ulTSgiIv-xOfx-BY7RXH32M748iUP9oc4EDE43qO2N-lTgB_rW3DZa5aDy9lWoqh5Hq1NYCbwXGrKWVTWap-CZ3AL3wYDXWBS4YeHHFM8E6q2_myqr41CcJKnE-UBSlxD4KILa_6LwQURFxa1z1VXML-iKLsJHQNX6QXs7MpP9bxFnqvZgZNvcr_ynWZQ1gR-54JcY15Ocl-DxqmQZOxhQackBDzuLvNfzsFCj1TD6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2HCx_bgKq1Tria4ganE8XMRr-dCEg8vASkjFycmAwuWq7xXEJlTxCqyaog2nmverJqAoFBbmuca8ft4sOy5YCvC3QtaBHF4K1Y_sfvJCCKYISCfWQYK6ZrFpLmr4nW09cbcpXmGCdGP3Ml6_5NGVg6mXbYtJNbyNA3M80sm0mzDH4WRj4HG-8R3WQ9GoPRz0T6jbNKZpplWX0IAAxsAFY18ome_W9HOFQUp4i63MRyk0iitCuY84hOHlyJM91XK1iEtEB-KB1J-oO0m-scYni3ToXWPlPaopsj-WjdfqR2ZxMInM6dYEJYmdyEzMEOlv5aj4VeOKzCm4vaTSRvetg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WPkY5_ncx8ck61icnx1uW2ujeB7KQdEGBOrdytLncnqnKhXiN8W85pj96sLqOqPTd6pIPZN2-bkDSzsqyhrzOFcPkpxh9LldEPFCwP2HjqwS60O7DUd7LEeerJ38_d1Cp9YykJVrPOIc7KcuuUcbn5Fc3FvU6vYSv1RwWc3isEPxW0zvuiAGE_CIwbb8baizFP6CcZjFF3rFpFkWffJxH5hGny9TkhFNzTApgm6_utWsY0ypbb3wCHjJe3ocLjt2A5-a9N4PviKJBN8ePhJTx3ujqWnFb-MfH_YJJUN0EAucBr7O4iEQkwDkvpYx9ZllJ4q-urZvh9eWhWfMU2OW5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hJc9LmXJp1wf31R0wBb4RQI2AQefNzKWnoU1EiOxPq50faQVi8r5ZmDMrCaqgquhkkgOIxnZGqlrapoi-t9T6JEaC61k62h_ywcBbvIsEnPRRimEkEnJTU7IBh664ciJe_7u9g8owQiTK_ENE4ILUjey2Gw-YvI3ZDODAWAtoS26wo-slAghlfmc3nb-ho36wv9sNHTzqrGaR5dO2MPE0CMGJJ_Q1eAAzFKmDfs998K12tCK3NrNMlSVecMiieiQIR9PRq_znxMAPKuYRFRih_NTDYMFHME-jwnCdxmwgxbyYPXfaxffIQ4b-M-0KwMNHiWq2_8OmARNLWxojd4WOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور گسترده مردم در آیین باشکوه وداع با رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666462" target="_blank">📅 17:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666458">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ شهادت نامه</div>
  <div class="tg-doc-extra">حاج مهدی سلحشور قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/666458" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پک ویژه مداحی هیئت قرار ویژه تشییع رهبر شهیدمان
💔
🥀
تو زنده ای ..
برای قلب های مرده ی ما کاری بکن
ما دوستت داشتیم..
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi
@gharar_madahi</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666458" target="_blank">📅 17:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666453">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuBkyeDUgKotpxSDP74rbTAuvXTIfjvkSm3HYaSaDPmFQe3e5wyDmBU8aJVJlAxlFSFUdTAI4gSN41K04pCI24ZWB5m2cc8rNgCvcnrMcZhNPsf1YvzpaOBeo5Tue0cJfqwXWMlci5KmkG3ileRHTKiTiM0NM5tDAn0MkTCF7u57rGNY3Fd88hinTLYfgv6osxLyK5PIaTATmvapblRyZFSTUQQ6w_xvKCFdOUt1dp4o0Bg9nQocmOOq-Ag5pHiF77fBBZW7ESeRkbfs0INRnz5TqYXZmbHsupyrZGFcEM-uFnPZ2_WvizJFQpM2FQKOp7ObQvykLHMEGcwWOuJtIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قاب ماندگار؛ نزدیک‌ترین عکس از پیکر مطهر رهبر شهید انقلاب اسلامی حضرت آیت‌الله العظمی شهید سیدعلی خامنه‌ای در مصلی امام خمینی تهران
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666453" target="_blank">📅 17:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666452">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72d04a82d0.mp4?token=BpBJidIya6fIVTL1lgJd-Vw7MDKhfv0arzC8LIsrT1udihW0xIE6gG7Tf38iUnZAkLfnh_UODA6A4z8X4LYdwLizZ2ecDBRVJmrZri1NanLe_sGSAD245wCM_KuVJ0aHAuH4f48GC-uVnk_odL9bGlxL_pOP_RQ8P7g67jTUHU1CndXlpuL6sY4o2kNQigVuQYBWStu1nNtqOtABo-hGUlqq6UhQC5wj-yljJNpailco_jHwoa1wU3mBsJNCxqYKFJIF1Q2elIGxkF457Vug0yP3aGzt8Qj84bQb0oAlVsLoeW3EdhSRWGm23a-LjDlcM6hsBo9SsD_-Vw5KoMCO3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72d04a82d0.mp4?token=BpBJidIya6fIVTL1lgJd-Vw7MDKhfv0arzC8LIsrT1udihW0xIE6gG7Tf38iUnZAkLfnh_UODA6A4z8X4LYdwLizZ2ecDBRVJmrZri1NanLe_sGSAD245wCM_KuVJ0aHAuH4f48GC-uVnk_odL9bGlxL_pOP_RQ8P7g67jTUHU1CndXlpuL6sY4o2kNQigVuQYBWStu1nNtqOtABo-hGUlqq6UhQC5wj-yljJNpailco_jHwoa1wU3mBsJNCxqYKFJIF1Q2elIGxkF457Vug0yP3aGzt8Qj84bQb0oAlVsLoeW3EdhSRWGm23a-LjDlcM6hsBo9SsD_-Vw5KoMCO3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اردوغان: دولت فعلی اسرائیل نباید فرصت غرق کردن منطقه در بوی باروت و خون را پیدا کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/666452" target="_blank">📅 17:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666451">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromورزش فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ec099076.mp4?token=B8vwUjp0hwHJRTCUVvWY-w06xqEOJMArzPklVC9Wr6cxTvyJPY0NLsGrUo8KZ7v3ZY_AflEt0JM1t_Ksjx9n425MSiQjAUjCKz56Sb4Ik0onRcKm1-W5ZGE0q5qRt5DFzxY077NmeZMJd8UZ0ThLIIDuK3YjwQK8IsZ-FVM4p7ScKKsO5ceAOjqz6_Eb6Imc3oGyoej4kwPke7z0_hczHOvtSFEUoBpj70JVpzCAqcMpOXzWdOmfSNKQUh3kC6pjJUoyloaftUFkc2NFFe96efbrJFXC_VVCLPukcsm1xjRoAylH5xZGIv4L36Q-9weVUqMoSGEGOAuhxk2jlnBAGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ec099076.mp4?token=B8vwUjp0hwHJRTCUVvWY-w06xqEOJMArzPklVC9Wr6cxTvyJPY0NLsGrUo8KZ7v3ZY_AflEt0JM1t_Ksjx9n425MSiQjAUjCKz56Sb4Ik0onRcKm1-W5ZGE0q5qRt5DFzxY077NmeZMJd8UZ0ThLIIDuK3YjwQK8IsZ-FVM4p7ScKKsO5ceAOjqz6_Eb6Imc3oGyoej4kwPke7z0_hczHOvtSFEUoBpj70JVpzCAqcMpOXzWdOmfSNKQUh3kC6pjJUoyloaftUFkc2NFFe96efbrJFXC_VVCLPukcsm1xjRoAylH5xZGIv4L36Q-9weVUqMoSGEGOAuhxk2jlnBAGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت های مهدی تاج رئیس فدراسیون فوتبال در مراسم وداع با رهبر شهید انقلاب
@fori_sport</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/666451" target="_blank">📅 17:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666450">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b15bad4f.mp4?token=FgZlLTE0aJIvTdVbTAXd2Y1ZSOrIihAi6Hc_AG_GrUJt5yOg4Az4aZezC8uWiEC-Kdyx4yFPoxsbiMpI253G6Ia5-JFcHfK1mDFokRXC7sGrVsu7BGFQTil-_qZnVQm-7_2sopdar1RynbBepwiRUdo4wQKlKnLButLekLfFNMNHQk_q-WY9aipiRof1lqjQrpXcqt34m8beHy77NesKxAvvUlHhVKbPnlW2rJDiLIxJl5-0bcKiqlyB7lIz3FLTnKJCNBcAeiuPiQbpL0DRZkIUZnSoNCSJ6bO49ZPz0A9Rf25Dte0phMKqafnR8qPDrXQswJAuGGMyYua5pfeyVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b15bad4f.mp4?token=FgZlLTE0aJIvTdVbTAXd2Y1ZSOrIihAi6Hc_AG_GrUJt5yOg4Az4aZezC8uWiEC-Kdyx4yFPoxsbiMpI253G6Ia5-JFcHfK1mDFokRXC7sGrVsu7BGFQTil-_qZnVQm-7_2sopdar1RynbBepwiRUdo4wQKlKnLButLekLfFNMNHQk_q-WY9aipiRof1lqjQrpXcqt34m8beHy77NesKxAvvUlHhVKbPnlW2rJDiLIxJl5-0bcKiqlyB7lIz3FLTnKJCNBcAeiuPiQbpL0DRZkIUZnSoNCSJ6bO49ZPz0A9Rf25Dte0phMKqafnR8qPDrXQswJAuGGMyYua5pfeyVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوای لبیک یا اباعبدالله در میان انبوهی از پرچم‌های سرخ
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/666450" target="_blank">📅 17:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666449">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USnCGFeLsNKgnDCyWXyaA1oljF-fJOAFv2Ej04LxOJLeMdZCq0I-nsKTtZdHjd9QTGS5xCX1JpMv4iFSIV1du1HmEOIA6aRDVotFodDab-JbZpMaGYFCXSVp21wT4kIFumjV1o81dHkMG4eM0ai5Q-UH1gqKq4f910seBF4QSbkMxIA1_nle5nILdggfcA2lQPBIgkNZyu1XHCXMWzvtxHbNmS23pm8kG5yoxv9B5C16Uv535RaDRV-z6YFycFcy1qkNiey472FZGm5ep9lEFauL1iiybLqpegxq4EoJg1EI7iMRYe7aGRIsWnlWo-KckMr9GjTKBruYm0xA0Dkl3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش از نوسازی نیروی هوایی ایران؛ سوخو-۳۵ در آستانه ورود
🔹
طبق گزارش نشریه «میلیتاری واچ»، تولید بخشی از جنگنده‌های سوخو-۳۵ سفارش ایران در روسیه تکمیل شده و روند آماده‌سازی برای تحویل احتمالی از سال ۲۰۲۶ در حال انجام است؛ موضوعی که از آن به‌عنوان آغاز نوسازی جدی نیروی هوایی ایران یاد می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666449" target="_blank">📅 17:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666448">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: بانک‌ها اقساط و جریمه‌های بی‌دلیل را باید به مردم برگردانند
جعفر قادری، عضو کمیسیون اقتصادی مجلس در
#گفتگو
با خبرفوری:
🔹
از مدیرعامل بانک‌هایی که دچار اختلال شدند،  توضیحاتی خواسته‌ایم و جلساتی هم می‌گذاریم تا تعیین تکلیف کنیم و مشکلات حل شود و تذکر دهیم تا فکری کنند.
🔹
مسائل و موضوعاتی که مردم در ارتباط با پرداخت قسط و اعمال جریمه ناشی از اختلال بانک‌ها داشته‌اند را صحبت کردیم تا بانک‌ها جبران کنند و مشکلی در بازپرداخت‌شان پیش نیاید و مردم حق دارند و نباید تاوان مشکلات پیش آمده را بدهند.
🔹
قاعدتا بانک‌ها باید جریمه‌ پرداختی که بابت اختلال سیستم‌های خودشان، بی‌دلیل از مردم گرفتند را پس دهند و ضررهایی که متوجه مردم شده را به شکلی جبران کنند.
‌
🔹
این اتفاقات، پدیده قابل دفاعی نیست و اگر تمهیدات لازم به موقع اندیشیده و اصلاح می‌شد، این اتفاقات نمی‌افتاد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/666448" target="_blank">📅 17:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666447">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfPaJeBFyEN43-Y0C5gC9oS5fTekk-IICinIKmL_CwwVQdkcP182x0BvqzCtY_ATQOD5OqLFQ7GJW2XdPPObwxn8_cVcapwZn4uCtbeh5F1sOUYvzRfS9QfRiF7TZb-NE7yj_cffxKgzmIRdjaIRwmw5h_JmlhzAbGI9YSaHk8itedzUW6b8wowOtinJgzatR1bw2Z2eDvSSbrXzDbyhS66atoWVBE8hPP8gP9I0iMjzYwKnykDdJg7RJeH9_jUc6y7-x5LRzhEaPTaAzLP6cFyZOjFjvNXHymFZSc_q4zuAoRPBiMdyNwnexArpOIne0qVFF9hDSjUpWRDyVsiupA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر مچ‌بند سرخ، یک عهد است
🔹
عهدی برای فراموش نکردن خون شهیدان و ایستادگی در برابر ظلم.
🔹
در مراسم تشییع، با مچ‌بندهای سرخ کنار هم خواهیم ایستاد. #مچ‌بند_سرخ
🔹
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666447" target="_blank">📅 17:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666446">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyyNvI4DpGXHTnNgxayD--VF01MgL17VCFMpVx0vDSWCUb6ImMNLgkufvc_VVHiFUsibDsUBrSJTohC0OLfFloUD832s4n6ZDryKAM6XYJ1mp1BkETN9WDbZyPiklahbuu0rxkAHDq_RSdZxZTZ25knX14Oj9QIQjX8VL3wn990vy2jvi-lZeYo605SIVGs8M0Mxg5H1OihGYktM5iTxD0K-bA0sShXBFJ6Ik7PVOXQ1oRHdCqkrLEPAMzdE31frojrunTLpkXoo30L8XDnFajnSwi_MW0nM0ansVK0q61DypIHMv-fDaCuHYHegzlaRW70pV-BVQe5CV1rCi8HGTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قاب به‌یاد ماندنی از مراسم ودای آقای شهید ایران در مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666446" target="_blank">📅 17:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666444">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
الحدث: دور جدیدی از مذاکرات بین آمریکا و ایران در پاکستان، در تاریخ ۱۱ جولای شنبه هفته بعد برگزار خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666444" target="_blank">📅 17:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666443">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5te4cDGG-kH_vwmq_axM5RNcM-3ef7CDnSRlEdXIhqVvS_Am5hq-JBoFNHCt0stri8jhBScTvsemh3DClaY5LflVdMJSHornv9DXIOrXKbqTxTxHDGrbwvHuilJMKX2WKY0VVU9yb8UKtkEBe0T5dou9lC-pgZ9T7flECIHrY85oiGRmFbhnNmXsV-HypDee5hr1PDwfcqNILFscvaLdGscdfCGSvnLSAHB01eQcSz6xjW9iC0PCULep9rTzeS7TJsRT_GeY5my2twMPGqbLHWUFisc3sOz6RH4HclFhBPwIYuhHJzR7cFKhXQGrld9kq1dQwQyI5jGIOHVdPIhYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لغو سفر وزیر صهیونیست به نیویورک از ترس بازداشت
هاآرتص:
🔹
وزیر امنیت داخلی اسرائیل، سفر برنامه‌ریزی‌شدهٔ خود به نیویورک برای شرکت در اجلاس رؤسای پلیس سازمان ملل را پس از اعلام برگزاری اعتراضات و درخواست گروه‌های حقوق بشری برای تحقیق و بازداشت او لغو کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666443" target="_blank">📅 17:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666442">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77cb53eb67.mp4?token=YW_BC9yTGgHE9Id4pxB85zj1AIJQ2l6KV8PUbmxMYmg1QneTI0RPJkFbrsZg6XG02HlB6sQruCxXFxG0tt3XpEXkBnac9HTH0nsoogMLzzqnA9sk2d965Nn6AWG5oDh-hWaQrzGE7n_WEN1d30g3Vw_5tznOF-ZvZd2_CeVbimSFJsSVFbMbDdgyIi1gAyLJN2Uk4NPfp28O4eVOApPXv8Xgn5bC_EWcVznpWGzh5ozFhyPrsxSKyjvMmWzfGJLpR3fgiJlZr2pZuPD28zYm5mGcpSFYYdsoBL4ScJ_glc91eXdQy0e8PnOw0aHuYQwiXXCxbI6voUSZhq71JNiBqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77cb53eb67.mp4?token=YW_BC9yTGgHE9Id4pxB85zj1AIJQ2l6KV8PUbmxMYmg1QneTI0RPJkFbrsZg6XG02HlB6sQruCxXFxG0tt3XpEXkBnac9HTH0nsoogMLzzqnA9sk2d965Nn6AWG5oDh-hWaQrzGE7n_WEN1d30g3Vw_5tznOF-ZvZd2_CeVbimSFJsSVFbMbDdgyIi1gAyLJN2Uk4NPfp28O4eVOApPXv8Xgn5bC_EWcVznpWGzh5ozFhyPrsxSKyjvMmWzfGJLpR3fgiJlZr2pZuPD28zYm5mGcpSFYYdsoBL4ScJ_glc91eXdQy0e8PnOw0aHuYQwiXXCxbI6voUSZhq71JNiBqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقام خون رهبر شهیدمان چه شد؟
🔹
پلاکارد حمل شده توسط جمعی از مردم که در حال حرکت به سوی مصلای امام خمینی هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666442" target="_blank">📅 17:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666441">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
دودَمۀ میثم مطیعی برای خون‌خواهی رهبر شهید: انتقامی مانده است
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666441" target="_blank">📅 17:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666440">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT5pefCEvvyulAZPqQThF4IpVqpGj8TJQOhSMjkZrISQMsZSAI0pncwjFSJZCGiYu1iqAVU3IZIX8WcG5IhxSAZBiidPDgisxygkrRHe32TEKvjDQQ6nhCCnbXL7I69fIklgQBlOOjibZrgx9OPoLgWq7YrHYnJcYrhJKiNXpUOKbs8Npwp-UOZG9xrHhDZtC2ER0GjrkBMu0ido41j-y-CeR8lznTAqwPwPsn5CMzeYboT0vpNYeZHHwxc57lEKCQra9EiY2cv_e46FAHWrruGRFnoVg_Aq2ToyUlSNnVGQuP28u3mBtWodpmanewpQ5A2i01QM417L6GUhNAwBvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله جدید رژیم صهیونیستی به غزه
🔹
منابع فلسطینی از حمله جدید رژیم صهیونیستی به غزه و شهید و زخمی شدن شماری بر اثر آن خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666440" target="_blank">📅 17:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666439">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5954bb030e.mp4?token=OBvLtfHKwCNDyJ_3zr8ptPso3ctAJNC2ItD-Rh9oCHcem45-UKXY_LGPL61cxGIMInPWvVpK4qDMynqAKc4QAr-n1YpVAD3f5v4EwOVR24RiFwmZf7xb6iEBeeRxQHHzvT6HxYSqVAJ9gMmQpy9LIZHGiANA3x_GZiC1mt0jI9LOZ7gc6zz_wBPh9GIsOY8WjMADmuEt0gBTPlq4K87YLPtnFgqq_QK1qXD1Cd49qgVIOMlpWf4OdnnAPwZphjBt3D-nnoYIUEIa1F5um6cJi3wTHNgkFmR-LzJoCkGvGtooLGj4zMSF9I601QICxzHa6EzhMlW0MJBeVSNWFgB35w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5954bb030e.mp4?token=OBvLtfHKwCNDyJ_3zr8ptPso3ctAJNC2ItD-Rh9oCHcem45-UKXY_LGPL61cxGIMInPWvVpK4qDMynqAKc4QAr-n1YpVAD3f5v4EwOVR24RiFwmZf7xb6iEBeeRxQHHzvT6HxYSqVAJ9gMmQpy9LIZHGiANA3x_GZiC1mt0jI9LOZ7gc6zz_wBPh9GIsOY8WjMADmuEt0gBTPlq4K87YLPtnFgqq_QK1qXD1Cd49qgVIOMlpWf4OdnnAPwZphjBt3D-nnoYIUEIa1F5um6cJi3wTHNgkFmR-LzJoCkGvGtooLGj4zMSF9I601QICxzHa6EzhMlW0MJBeVSNWFgB35w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار حسن‌زاده: قطعا تشییع پیکر رهبر شهید به‌طور زمینی انجام خواهد شد
🔹
مراسم وداع با پیکر رهبر شهید انقلاب تا ساعت ۲۰ روز یکشنبه ۱۴ تیر پیش‌بینی شده است.
🔹
از ساعت ۲۱ امشب تا نماز صبح ویژه برنامۀ وداع در مصلی برگزار می‌شود
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666439" target="_blank">📅 17:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666438">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwSjG-NM2Dkhc1dPWgij4g-LKd0hl_rlcw2XHb5YcxMaq3JWPIK1imI7FkvlflmfsCrW3rmO1WZHLgK-pgsOVPApZ0cfcE6030P3r0NvAwK30P_PH4OpLvRXyxEzzFeJhXeKLgwr3fbIeBYQGb0cCzGUcTmHK0w9wnX8xypP5zf4EaUW0wYtyyEqPj-jGgrneZdnRnjDAyodSS3SdUcrYMaLxPEcji4rLIgSifV7SQ2fPxsRwi-NUL4jF_DfN8fPsUhW0wWzDUTO-U_x1POu2jQbyC0iH2jLaysd__D5FL7SjHP--pmVtyrId3vNjmEakYrLu3yBp887hLt9ozLJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه جمهوری اسلامی ایران به مناسبت وداع با رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666438" target="_blank">📅 16:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666437">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGl34owTrIALePKlWVjZLkeEx7Ay3dVFKbgbbklx7oyBbv_j7cnRRtSZHZTbJaSX40mveqpIL-zLkR2ZWeFrsk6Zj6v2X7SEXKe4FK7wc5g5z4G3rOckPt5U0paATWIC0C2kFDds1aUutzeVAPsFyTfQguimxH-Nqcrex-ACSiC9ISRBZjwG2maG_tkthO50l4LR7XOh4hIXGagDpnhH1wSVo7H46eQYU9hxEGw2w-vval3Ueo-8_eb32thxih4MK0PhjjwILuN5FmIfmB2_f17JUgnemYLEGtn5l5UUWr7JGf-AGRN3K14Yt2FgHGawiqf7CJJd8zkc7-7RJ8JKZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه بریتانیایی گاردین، با تیرِ
«
جمعیت انبوه در آغاز مراسم شش‌روزه تشییع رهبر پیشین ایران
»، نوشت: «
پیش‌بینی می‌شود تا ۳۰ میلیون نفر در مراسم تشییع شرکت کنند.
»
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666437" target="_blank">📅 16:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666436">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87f90c0973.mp4?token=vW-ik5vkPTMqNQFb2B8RXCGtOhVx2HghpMjBDTT45iU5HoTpY2XzDwu0dSpQCX71FM7h5N4RItpPcBzWd-RlJyaddDkqSM_ZJeGsyv7yyOYdHi-5sX2MzI7QlQzkdFRoAqHzQrOLw4i3CJ2fw-ukQo8Vg6a3wEdxTvzqDUa2Fa9PA6pRr991RDFjr9qKEERj5Ggns2FEeDbo2_S4ir8AY-rCO4gAho0Ro6kLyfC_QyJoa7r69hUhq9FGjDkUoOfAwJCZrtkSRTXw9iT6sIVLsV3gUy1JYtP9bwbhEBxgaeY1AXcSyVs9QOUQyMVnxWzgu1-5tWXvDgNazDD20v-KMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87f90c0973.mp4?token=vW-ik5vkPTMqNQFb2B8RXCGtOhVx2HghpMjBDTT45iU5HoTpY2XzDwu0dSpQCX71FM7h5N4RItpPcBzWd-RlJyaddDkqSM_ZJeGsyv7yyOYdHi-5sX2MzI7QlQzkdFRoAqHzQrOLw4i3CJ2fw-ukQo8Vg6a3wEdxTvzqDUa2Fa9PA6pRr991RDFjr9qKEERj5Ggns2FEeDbo2_S4ir8AY-rCO4gAho0Ro6kLyfC_QyJoa7r69hUhq9FGjDkUoOfAwJCZrtkSRTXw9iT6sIVLsV3gUy1JYtP9bwbhEBxgaeY1AXcSyVs9QOUQyMVnxWzgu1-5tWXvDgNazDD20v-KMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت اعداد از مراسم تشییع رهبر شهید
#بدرقه_یار
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666436" target="_blank">📅 16:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666435">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGUTw_OHvjESNBvLkI8k6lJ-jnAsrPexHN6PIcB_K4em5yqD8Ozf21b5q7HeKom4dwQunh0g5v4SjOLSJL8Xzh3QenoIoe5el16b0aV-ISg0eZ1k6DM3FL4-MFDzJ0VJWPgIVojrOKs_cwLymnVy7GZhyx19kSJ3ywFgsP4PaO8Nt-s4ACFYlSZirSK-wPXgA-9hhSW6kAan0WTNWRwYFwqCULsajXmvxUvJhtNL7V_5iddTNaCYPWN-pJWKBwj6vwB0dRfQRQC1twS8J4LOseosxOy_kLwkWLkORs8APwGOMUd81nWKQHdSEM6elURgbRkgwQVsUC1kNvXnkVH0Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناو هواپیمابر فرانسه به پایگاه خود بازمی‌گردد
🔹
رئیس‌جمهور فرانسه اعلام کرد: در پی تحولات «مثبت» در مناسبات میان ایران و ایالات متحده آمریکا، ناو هواپیمابر «شارل دوگل» از منطقه خاورمیانه خارج و به محل استقرار اصلی خود باز خواهد گشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666435" target="_blank">📅 16:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666434">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ای رهبر شهیدم؛ عهد می‌بندم که راهت را ادامه می‌دهم
مصاحبه خبرفوری با زائرانی که از راه دور خود را به مراسم رسانده‌اند:
🔹
ای رهبر شهیدم؛ راهت را ادامه می‌دهیم؛ ما برای تشییع نیامدیم، برای انتقام آمدیم؛ عهد می‌بندیم که اسرائیل را نابود کنیم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666434" target="_blank">📅 16:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666433">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bQ0a3zaYawWNHtvvpG2fLcMo_edvGjoq0zIOkUoTHH8nJkDkTfEoEP8rpmvXuw7_sf8iA6BEM3ETbtah5ySjcL3bVZdyH-1TkxCBBJlPLbF9j4jonbpNWvdGZhDhTPhFDBkq8evHn4P8azSW5ZTUhkNcDRNiZcE7wenHlR7AgrNEbGtCRVIvVfODk6fCeC9lBUoK3q0A5R00AfqrKzQC_Zi20sAQWn04JlkrW5Sk9CLEFSTQu5QQ5FCMAp3xS4T3I8aAiE_q-7i46KNKpcsmZWOjKx7-zufF95BZJfVvRje_45mJCJuuBe9JiyDLsLPYz2SSoOFE6I_zw24pekZsWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چهره ممتاز حکمرانان تاریخ ایران
🔹
این کرسی سابقه جلوس کسی را دارا  است که بعد از بیش از ۶۰ سال مجاهدت در راه خدا و گذشتن از انواع لذائذ و راحتیها، به گوهری تابناک و چهره‌ای ممتاز نه فقط در عصر حاضر بلکه در طول تاریخ حکمرانان این کشور بدل شده است. ۲۱/اسفند/۱۴۰۴
🔹
مراسم وداع در مصلای امام خمینی(ره):
شنبه ۱۳ تیر ماه و یک شنبه ۱۴ تیرماه
🔹
مراسم تشییع تهران:
از ساعت ۶ صبح دوشنبه ۱۵ تیرماه
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666433" target="_blank">📅 16:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666432">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rblu02G90-0PMVt-K4S-5dYOVIMFX3XwugvL4O3yIVAk7KGCetF8kXf3ca6jrZ9gPI5D-qs7aK09AENG5GOtFpiiMVQgdk2MrBG6jy6-mXphXqAXyF7Wp0G_EJupSn4wMxpAUcpT4f0MRsxfdBjrmnDkChcBlcQ8whz4GMCSbx0FCWzI-8linur0TaHT_0wHj5ivO_KNUiiU52j19So2NFZjo9k7mhJTPzCPvNMBf13TYKJMqdxwAXMyG1T_E3NvmqLWGu1rYK4hg7YMkSrKY7nNLS91We29KtX0ngNzXavGqOy8joxTPpSdpjexV4aim-2kIoYojhQ22-p3-lWilw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ با ایران برای آمریکا گران تمام شد
مرکز مطالعات راهبردی و بین‌المللی آمریکا:
🔹
هزینه عملیات نظامی علیه ایران بین ۳۴ تا ۴۲ میلیارد دلار بوده که از برآوردهای اولیه بیشتر است.
🔹
در صورت عدم تأمین این هزینه‌ها، ممکن است آمریکا با کمبود بودجه عملیاتی مواجه شود و در بودجه‌های ۲۰۲۶ و ۲۰۲۷ نیز رقمی برای این جنگ در نظر گرفته نشده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666432" target="_blank">📅 16:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666431">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
اگر در مراسم وداع و تشییع وسیله‌ای پیدا کردید، این کار را انجام دهید
شرکت پست:
🔹
افرادی که در مراسم وداع و تشییع رهبر شهید وسیله‌ای پیدا می‌کنند آن را به صندوق پست یا دفاتر پستی تحویل دهند تا به صاحبش بازگردانده شود. همچنین افراد می‌توانند با سامانه «پست‌یافته» اقلام گمشده خود را پیگیری کنند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666431" target="_blank">📅 16:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666426">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
زارعی: جنایت دشمن نسبت به رهبر شهید باید در صحنه بین‌المللی پاسخ داده شود
سعدالله زارعی، کارشناس سیاسی:
🔹
باید در ادبیات جهانی جا بیندازیم که شهادت یک شخصیت عظیم‌الشأن مذهبی توسط یک دولت و قبول مسئولیتش یک جرم عادی نیست و این یک جنایت بی‌نظیر است.
🔹
باید سازوکار عملی ایجاد کنیم تا این جنایت در صحنه بین‌المللی پاسخ داده شود و ابتکارات عملی برای اقدام در کنار ادبیات‌سازی دنبال شود تا برای اجرای حکم قصاص بستری فراهم کند.
🔹
شهادت آیت‌الله خامنه‌ای یک اتفاق نادر در هزار سال گذشته است، زیرا هیچ‌گاه یک مرجع تقلید در جایگاه برجسته خود توسط یک دولت خارجی به شهادت نرسیده بود و این موضوع باعث شد مردم ایران با نگاهی جدید و فراتر از یک رویداد عادی به این اتفاق بنگرند.
🔹
اگر دشمن می‌دانست شهادت این مرجع چه تأثیر شگفتی به نفع ایران ایجاد می‌کند دست به این کار نمی‌زد و مردم این اتفاق را به عنوان یک واقعه عظیم تاریخی تلقی می‌کنند.
#خونخواهی
‏⁧
#هزینه_خواهید_داد
⁩
‏⁦
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666426" target="_blank">📅 16:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666425">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6262b313bb.mp4?token=IM_kbAsq-s7wvWn1Ct5YlJnMc-wYBAEnvMbf1kYDi2qQemtIuX587SrPhGFwPSN63pyhLk5U-fT1JvCax4jkjmCwlc1Sp3USVSfBpz9wYWDhy0qDY3v1vGLpr-ONTpvWThsXb9kdiUo2qafSUD1jtfZ5HSBp72bj1lwLFVKwXAUCifL5Q7Wl6Y2kLuijD5Q70kBgyhqCPqTxiQHGFl7oxohFoOe7Xncbk3CbBiN-5HB7U356Pt6Gt1SJDvJNBcy1klpSn7R9_Euxw3SChJD_ozHASNJZQ7QhKz0ds4YhJajRyvAzE0CGG1JVRjtcNvQ79GV3HwhA00r7BrQw2U4Pd4pEzKMIMysRR52gW_xJVxnaoiMDrwLnssYLPcHTFZdCoi1sentXTN-HIcEKyFtL_SsjB-P2g1anaOUGQ6tX2sTGUgzuagoSTbQ8AkEhWLPS5k46SMO75MS8UeIDKjKKcieg1bhTPtklX2Sh3UbL_A2zfWrYhvA4qT3mYxXLdm2Oj9sb4_AXAvlI7etmdfh0N4yGbLdb7XFTI09swKV4km7xkJV4XdpQX1DmS-GHwBILgVO6H_RapN5sFS1bpJbqAETkIYGsXoCfqywWhzOt7bxIaY78OJSuIrHoph-n4syyATZfDdwYF9EFITxI4LWMytD2G5oRKyiQtHLy8uHJ-mY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6262b313bb.mp4?token=IM_kbAsq-s7wvWn1Ct5YlJnMc-wYBAEnvMbf1kYDi2qQemtIuX587SrPhGFwPSN63pyhLk5U-fT1JvCax4jkjmCwlc1Sp3USVSfBpz9wYWDhy0qDY3v1vGLpr-ONTpvWThsXb9kdiUo2qafSUD1jtfZ5HSBp72bj1lwLFVKwXAUCifL5Q7Wl6Y2kLuijD5Q70kBgyhqCPqTxiQHGFl7oxohFoOe7Xncbk3CbBiN-5HB7U356Pt6Gt1SJDvJNBcy1klpSn7R9_Euxw3SChJD_ozHASNJZQ7QhKz0ds4YhJajRyvAzE0CGG1JVRjtcNvQ79GV3HwhA00r7BrQw2U4Pd4pEzKMIMysRR52gW_xJVxnaoiMDrwLnssYLPcHTFZdCoi1sentXTN-HIcEKyFtL_SsjB-P2g1anaOUGQ6tX2sTGUgzuagoSTbQ8AkEhWLPS5k46SMO75MS8UeIDKjKKcieg1bhTPtklX2Sh3UbL_A2zfWrYhvA4qT3mYxXLdm2Oj9sb4_AXAvlI7etmdfh0N4yGbLdb7XFTI09swKV4km7xkJV4XdpQX1DmS-GHwBILgVO6H_RapN5sFS1bpJbqAETkIYGsXoCfqywWhzOt7bxIaY78OJSuIrHoph-n4syyATZfDdwYF9EFITxI4LWMytD2G5oRKyiQtHLy8uHJ-mY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افتخار می‌کنم ایرانی‌ام؛ این حضور، رمز پیروزی و وحدت ماست
مصاحبه خبرفوری با زائر لرستانی که از راه دور خود را به مراسم رسانده:
🔹
رهبر ما هم مظلوم بود و هم مقتدر. ما راهش را با افتخار ادامه می‌دهیم و فرزندانمان را برای ایستادگی تربیت می‌کنیم. آقا، امیدواریم از ما راضی باشی و در قیامت شفاعت‌مان کنی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666425" target="_blank">📅 16:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666424">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
آیت‌الله جوادی آملی بر پیکر رهبر شهید نماز می‌خواند  کمیته اطلاع‌رسانی ستاد تشییع رهبر شهید انقلاب در قم:
🔹
مراسم نماز بر پیکر مطهر رهبر شهید انقلاب در شهر قم، توسط آیت‌الله جوادی ‌آملی اقامه خواهد شد. #بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/666424" target="_blank">📅 16:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666419">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KeexwYNv4orSnvR7HQq-PlND-_ZnnFLD4fu1qREyJcRrc53rBSeUHf8OLR2X2P7sXpKtqvdKC5o4kYsT331hDzKdjABLMMoWeVEX_EWOu-mJ9FkX-o_si1u-g1JUwhTnFAzn8eAfsYpj2mvnJalicOlnplTfubuSTJLkwSIVZPZ0fVMQa7ZTuDmXvibMXgT8rEJfaQbt3fKDGxZCxpofKGOaeJ7s02PMXOcG2tV4z1h7e78-lsEWrd-FSS-L89AnRJf0LlAYpNXD57k90ISq8zPqNoRfaAFBYZo2jy9eRbouZa1NwpB16LDskbigyH_96iAli1XEX1OeMHzadIBMJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FfOcwtaEUbLwkvXq7MT_RGWtgqCmqLREz8WcxY0jZfHlfcZVrg9H3k6TyRuIsA0U12iOnxwR-NKrrZkeh0PVFdqqWNj8BI9q_s-516sAhQMhi2DoGsbyLAKwDbdv9ayfKhBtcsxUFzDnKAT1SqwuHAF5sCc-XYB5PWWRTbV9iFYGikc-x56Uc7FjIFPo0u5oZkOHDhKKMi64uBI9MY_oRUCoPHgIgJ_2EuCyd_DabqYMOg1BLVRxJLFHV3at8Aohd5ubMa-dZ2KG2Fsy5B7pi_V6LY5D7SVvUm3bZ7Mgp0CatWVpULtgbmtGK2uIxMEo19MnVUJgB7qN5qBAlPpSDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_0UOgFFiPHPkKQqfC0q2C6xuNrQUrobNOKwvrcIt9tOyGNMY0LxoCWFb-HVF--jXlDLifIMRFqfc3wU2dnmrsSAhzJWf0jupeVlwWEiNp0AAxjZW5T0REav5P25JBlb5gYOIiiYi27XnxLU-aGYwwD0Y-sdWvkXH0ZGPmR-Gvk8ej5vEZkRXK2xyj7baROcja6am7-pTGtmrqrnQ5blLAIJy6ePwHRatau7Y-DDfMzA05e8JGzTrQwwFJBsDaVvGWTjwW2a2BV0yIbEU1RNmYWgkv4KGOobj1J2K7x2cXfnzeHYUgm8PKzecU0hmLighRtgggJ64LkDntUNWKdfNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xey4azBOdOTeVHZqghL_oLWLElUWrj8GY3gx_wnlg9VjcNhhTvCnLVcty2Jjgy5y-squDcSmuYrXGa8ORTHVNQ-rPrT6iLXPC-YoXIqVhw4MkPCvYNgoAHh6derjuDX9KCOBUl4powBkSydo4QEiOdkFabPrILV3W2cibI1_xRcIbPFnhtqXR8ss8YUTt1zhhXFfrw5raVbRz29-4YPwsE7kcDk1N21LIiCw2MTPnPH4IZBovVaL2aiV218CjjNGTF4PUnCljzZDv_rCoZ7rqasdme6o2mYPvsZZHSsqlliQvNkzKPTkzSYOD0c7FQGXT2xU8AzFMHfXSDJkx-3nxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/asgOGpZls0R86KlsfO93lBkpeaC-bDzFi2tQwiW3kFiK4JH9oV4avB3C6T2kEggC44u7EdhWrOntrEG4MjWVBcC95Ij9SqMXQW3EBn6X5yxTIb7D-NowSBp3brDex95rjKSSDW7oZAgoF6uxHL9zlyrbqfTyJC0veGCae_KVBbd1RtLYe_w2Ydz7Bo2y24RBzHojCCPPLgT_8txoaEpnCaUo8zfkoHz7aidjBnRsscQSGA7Cmdmwixsbq2WeErEk7UrCI8CXfkcrynAI8_SS5kSto-Lu6MbO_wSyrmW49Y8Mas1meCjhn_W9ELYLU696Pos9aiy4gJ7XOkL5-1aWMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیدار نمایندگان حزب الله لبنان  با سید عباس عراقچی وزیر امور خارجه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/666419" target="_blank">📅 16:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666418">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c4a85bf45.mp4?token=E7gebDEil8GVQ1IFIBY0nsVE4ObyjJQuFO8FU1B1rc-jwhO7cykt1kaFBdpnMPP744gFQDUGnkBiURGea6rL55PPLRMgN4dNQNMCwsLUHENv4ec74LrnQfhPoVeICtPW9AcbfUsvdAP4wfPQvFXg_NZ-vTMX_TU_fm8iPfA5CdX6uNtTM2h7zyrz4gbTym1YY6i7VakAexdKdrrO0v-GKBu2IYNd4sVR8hnLl9wrA1qjY-pn-mEvCNT-mZg0rZsRRwlonY1ixJljcnItDYe83Mt3lJRqq1IM2geVHDs9yqMUvNKBHS_Txvc1pfVYOxZSzawXbpRK99JPez_whu5UxZbhxTbryyoA9zEPPk0xmb1jho61MJFV0fVIev2xzk5swYfvbAGiipnaVL4yfr7bXoBemXoMYzQjMG7SwpMYb2o_-P6LuSgdAn8mo4I7eqPB_7Cei4yxBds-N7ZaimdiBmAcU-7XZwFmhDhFlNM0Lze5nWMprzmsULPOndvpuZamIGARzCOQjDOk7rat_R_q2B_vKyh_QZuXWdvwvdrJrVgoq-zKtfbsGR2oaMsMD_-hO0_YBGvFJLu5ZlfNHViYGCXob0j-bZ6tV5iEdMqjT1WoYWA9pD_J8-mNeqoyafii5-Fdyn0QKJrkRIPGxqtbU_rSWVUoEUAB7LLzYPuePVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c4a85bf45.mp4?token=E7gebDEil8GVQ1IFIBY0nsVE4ObyjJQuFO8FU1B1rc-jwhO7cykt1kaFBdpnMPP744gFQDUGnkBiURGea6rL55PPLRMgN4dNQNMCwsLUHENv4ec74LrnQfhPoVeICtPW9AcbfUsvdAP4wfPQvFXg_NZ-vTMX_TU_fm8iPfA5CdX6uNtTM2h7zyrz4gbTym1YY6i7VakAexdKdrrO0v-GKBu2IYNd4sVR8hnLl9wrA1qjY-pn-mEvCNT-mZg0rZsRRwlonY1ixJljcnItDYe83Mt3lJRqq1IM2geVHDs9yqMUvNKBHS_Txvc1pfVYOxZSzawXbpRK99JPez_whu5UxZbhxTbryyoA9zEPPk0xmb1jho61MJFV0fVIev2xzk5swYfvbAGiipnaVL4yfr7bXoBemXoMYzQjMG7SwpMYb2o_-P6LuSgdAn8mo4I7eqPB_7Cei4yxBds-N7ZaimdiBmAcU-7XZwFmhDhFlNM0Lze5nWMprzmsULPOndvpuZamIGARzCOQjDOk7rat_R_q2B_vKyh_QZuXWdvwvdrJrVgoq-zKtfbsGR2oaMsMD_-hO0_YBGvFJLu5ZlfNHViYGCXob0j-bZ6tV5iEdMqjT1WoYWA9pD_J8-mNeqoyafii5-Fdyn0QKJrkRIPGxqtbU_rSWVUoEUAB7LLzYPuePVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصاحبه خبرنگار خبرفوری با شرکت کننده چینی در مراسم وداع با رهبر شهید انقلاب: آنچه رسانه‌های غرب از ایران نشان می‌دهند با واقعیت فاصله دارد. ایران مردمی مهربان و خون‌گرم دارد و من برای درک این حقیقت از نزدیک اینجا هستم. ایران کشوری امن و صلح‌طلب است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666418" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666417">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqI_2-Kw33M95eV1FKiavemZ8PmO654HvHBvjp71tGdHdPhnpe84qmSfLiT3LBL7-rXPDLL9CAKZa5Ab803gEiL3wMAxPapRNXOaZGvUwNwokMObqdfqkc94Aa-JLeJpCunRvpAvWRZSiOD_xyLEgR6buR82L5nowzj9nJWlrA8xahjbAaZcFsG8Jz0akWjTFTbgxY7prtxHQoO-wQ57o01hcsCUstQHLZVce3U8URejh_DA9IHmewEtRpu2CCGHDr3vt__ZwxGS3wjbF8inTVqbYfti0iQD3kAe-2Oejrklb7N4rg1f1A13EHkVjYgnqgnGvsMlLeua5aQmdK9rTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای روزنامه ترکیه: آنکارا نگذاشت کردها قربانی درگیری ایران، آمریکا و اسرائیل شوند!
روزنامه صباح ترکیه:
🔹
آنکارا از طریق ابتکار ترکیه عاری از تروریسم، آنچه را که به عنوان یک فرآیند مبارزه با تروریسم داخلی آغاز شده بود، به یک استراتژی ثبات منطقه‌ای گسترده‌تر تبدیل کرد.
🔹
فراتر از مبارزه با تروریسم، به تقویت وحدت ارضی سوریه، کاهش خطر تشدید تنش‌های منطقه‌ای گسترده‌تر و جلوگیری از تبدیل شدن مردم کرد به قربانیان درگیری ایران-اسرائیل-آمریکا کمک کرد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/666417" target="_blank">📅 16:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666416">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/890723cd8e.mp4?token=dNWZUTjvRMOd5itmYngi9Oth1a8tBDutJc4QLOrL4anTBZpddqgsAdPKgoFTPZ0QKQZmVvZQisDmiaJXDrr1yed0bZh3-9Qh7Uri56h1e_PNyMT0LtqCRIwD2QRh4twQ_8v96WhlvdVNOtjT8A4lsQHorewI1yzRuomXv9jpVOfBf0i46dQ_yfCMalh7PiQcZrHI4IPaVyto-3FOCebTFxip66Y93L6wytjwTyF89auuTrkVzV46LvXG8ShuvI4ewyMJ53nYWuM9Q_XCkbyOMuv9KlsdWXPpx6JbhKdI_yVW53XR8ONwQ3jWZWwm-V2gDiUu_QI9SoXLuJS3xLuXuqGOg-GiCyw824BqTMy1lZGnVXRwECcl0Z4HWFajOk1lc-YAx7FX-zOaOAour8PvhW_Z1119mbyxRdvqfOttocW1puuZdPLmouZZElkMC-465Gmenw5l63E1Oa-L_OlnoY3nV9YqrjrA3nh3tfhFPtNEWMSKzLC4r7i6CwGvFkH7RXF9kOQTw1zGfDe-a1QKBrUy-UUz4pec2mVRPvxChAvlsexBrpXf88PgPnA676yybQaEnoxKYG1BjIIkyglK9mmJXemGI3lVn03U7cJPvXd7Gn4Jea0Ai2_dQWKCrEG0JPenHlF9wqInJwhFzebGko_Em8Tfaqbacg4peUMUA2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/890723cd8e.mp4?token=dNWZUTjvRMOd5itmYngi9Oth1a8tBDutJc4QLOrL4anTBZpddqgsAdPKgoFTPZ0QKQZmVvZQisDmiaJXDrr1yed0bZh3-9Qh7Uri56h1e_PNyMT0LtqCRIwD2QRh4twQ_8v96WhlvdVNOtjT8A4lsQHorewI1yzRuomXv9jpVOfBf0i46dQ_yfCMalh7PiQcZrHI4IPaVyto-3FOCebTFxip66Y93L6wytjwTyF89auuTrkVzV46LvXG8ShuvI4ewyMJ53nYWuM9Q_XCkbyOMuv9KlsdWXPpx6JbhKdI_yVW53XR8ONwQ3jWZWwm-V2gDiUu_QI9SoXLuJS3xLuXuqGOg-GiCyw824BqTMy1lZGnVXRwECcl0Z4HWFajOk1lc-YAx7FX-zOaOAour8PvhW_Z1119mbyxRdvqfOttocW1puuZdPLmouZZElkMC-465Gmenw5l63E1Oa-L_OlnoY3nV9YqrjrA3nh3tfhFPtNEWMSKzLC4r7i6CwGvFkH7RXF9kOQTw1zGfDe-a1QKBrUy-UUz4pec2mVRPvxChAvlsexBrpXf88PgPnA676yybQaEnoxKYG1BjIIkyglK9mmJXemGI3lVn03U7cJPvXd7Gn4Jea0Ai2_dQWKCrEG0JPenHlF9wqInJwhFzebGko_Em8Tfaqbacg4peUMUA2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقام؛ خواسته مردم در کلام مداحان
#خونخواهی
‏⁧
#هزینه_خواهید_داد
⁩
‏⁦
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666416" target="_blank">📅 16:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666415">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asD44U3eF5gDRhBnA_a0lMU1yMccIL1H0HLztUqJYYgdGQ3JqSm9RHHeEVF9sRBjlr3Ev5rizmGuax81fTHG036yhloRIqJX7yCRGFYfEo0i93tgg8JDIUx4TpksK3cO35AeYqc6caF4g4X6zBl0vU4GJpkQvxKZbJD4FxHFlBFhDY4mDhMyXFOUvCC-eUqSjzCG1U4S503B61GHBG8C63o6V3fXgDAGELpdzfEGiyxW5fiOvktK2r4mw-aodz05QNu8P4zjQ3haXaSM-0TjorSRvyzL7yfsPfZJJXGlsWg-c-9ffGgzDHuNnCjnpY8KvD4M3UWgpqezx8v1zgbFnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعداد فالوورهای شگفتی جام‌جهانی ۲۰۲۶ سر به فلک کشید!
🔹
وزینیا، دروازه‌بان کیپ‌ورد بعد از درخشش مقابل اسپانیا (۷ سیو و کلین‌شیت)، از ۵۰ هزار به ۱.۶ میلیون دنبال‌کننده در اینستاگرام رسید. #جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666415" target="_blank">📅 16:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666414">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رئیس اتحادیه لوازم یدکی: تمامی ارز مورد نیاز ایران‌خودرو پیش از جنگ تأمین شده بود
احمد حسینی، رئیس اتحادیه لوازم یدکی در
#گفتگو
با خبرفوری:
🔹
هفته گذشته ایران‌خودرو افزایش قیمت داشت؛ تمامی تخصیص ارز ایران‌خودرو از قبل انجام شده و ورقه‌های تولید بدنه را قبل از جنگ دریافت کرده است، اگر استدلال ایران‌خودرو برای افزایش قیمت، افزایش قیمت لوازم یدکی باشد، مورد قبول نیست.
🔹
جنگ از حالت قبل خارج شده و از تب و تاب روانی کمبود لوازم یدکی کاسته شد، ولی کالاها تا از گمرک ترخیص شوند و واردات مواد اولیه صورت بگیرد و وارد چرخه عرضه شود، زمان می‌برد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/666414" target="_blank">📅 16:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666406">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3SqLvM3OhJYQ0lWObj2xAsncSVYcJeJcf5qSwB4j3vJMdk758j6VmXBSNACYFRKeDLZ1Hkar-fSr8jBVmkjWmY--ds-7A6-QNn40S0FeKCxGCYp_Twc71frRFCfr4F82ys_hmCSFFhMBJdP4-ah12ufFSeXasErA4x5qGrbrXrLcfn5nIkxI-Sgj_Qqgvaxl8E97UqULM4vUGiju7_Vu4Zg1Ca2X3BXBMZxOl30g7asd9SDcVK5dLVO_qTqlUvLCUAvT9alRilB6p2soGS8PWPyV1zTx_5X8dGgMDmqwp2ioE3322lbYU_zFgHZlkmmZxagieeESEtxYHIrkNk8Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C1v9ZE2ULMK_aJEaKmj6yACi5AvzdxOvysWWx8axKDgZWM0hMaj_r_tQyRZ-fX8eIIJmANmxCKlKqduQiHr0V1-rT_O1mmD6IHDk3nYc5J5d03FjxmbLiu5ib7_I4yP6vzQ4T2ywI91PkcpYOBz1RYCUd2xqeOAYtbYo2cCB4uyjs-55XO6ivmJXmuS9e5ozc2lwtrMYRFDptMgO3okTIKMvYWYpSSe5HDChUJPisH9Hqo4K2WOBMKT3j20UEwYj7X6fYsiMoDhP15v3RCrptj0aR2qw6yrh2pDEwMknM16uRcDd8DSXjgAMv_WlM_F_qs71wCjD0Y-kDrP5Khy3Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsdOq5TmiBZbirDt8Qpay40pAHqe_Ykj98QHIvDggHnk0Nu3CC5JswX9n6KI9jCQS_qEQF-YlA6-J9sYk_NLKdbnx3iHpKq578c1VoXQASimZEJ9P48Za84O8jW9ZhbTwlBlBEFpCcYRZGrJYDcMJ2HNvuBaQ20m0MWhuJGUrpwztTcvzDC-NM9N7eb5iFsjB9JiQ29qWq3CtfG1otLM7SAHqipXHIXlflRO5TXQks-ZGv4gH3s9BIvXVloS9Y6gBBRq-LCGK4bqJfhUWsroWqSszyRWtdYv58enj7GQDxfNo6112QI8EhjuMaQ3kXGFUS_p0TiBu7xWgzDfrrlKzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kXuAwfCWmd5gXz8c8GF5tLc35URqjG-Idm_m7nmrPefFTOQ0oD6cYZo0kOjDBR1--B_Gv9VIy1ZhxtI2ZdJr3kfFxkNIJLXO085nBAmGygtwUO3AcatEjPomNAw05xTe8najm6CJiEjH2Bfi2_psetYpnBPGsx5E5TrHofNCzFwrjAh4LuNajcFMSKf8wqFdwa0mKC-Z_c6XUjEV1qh1vnzGeVXi0AimfRCyXGN-Qe0ElSUC4ufC800FDRE5E9jtK1QeTozK-8jtGRct4HaNCw4xTUYmUWErj4VddQejBeLKuETTH5cKpSL7v_ZZmgTuEP2Sw4V30aj1t1-R4eAVnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7AIKqSBbSatxaYLOSvglBE9o6h_9MazLFvtaGfE6mJRfH_TER8fvBdKDSBzdrKQQQkotZboJSZ46tXYAH2DGjm2sSYrwmRP4bF5668iRaftXD05ZxBksYEWV0m-Y5ndbka4rqVglCct6DEVHqy_fWuN2wt3EJByRgPD6hKOlxSp69THuD19hz5qvTdMcPL6E5aYRVJYmUQIgh4NttLoryKlb-oFhrT8gSxX-OcS1pS0cbVmByAJqVlFGM7Geya-WntYBO2tm3XgRv-oYCyqxW-0leA0bAyrFa0WiyyVBOmZsbQYX64jeUAo2lt_ZigFJD7RnKyjZYkEoWc_9EzqGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oUp1xntGnYef-8m_KqogQpHT4ytn0l9Yxo9DjzVxKID8WmkGqLVT0yWMQYgGo4LRN7cbyVUNP5hDPt_LFCkV63WKcgL6BFalpLaWRKolmTAmiI38P0HvLf8bbnfkSr-ia0xH20DKQlPO56ud9rYTKl5SbZMU1wdt1-l_edW51Dr7b-mLBTTSMmL5l0DKas3VpsM-rRbhzprk93u6ntSQ1EixTBD4sJD9k9qHsd4OQRW3h8ImYLxiBcRGgGgRLDIU_PUt7rG6fFyvTBe2EbWUZdJvg3rt5zDyudvAjskVvrcIOSN8ge_GBYFZuEfrLNf8Uo4htHuouj_0T8ptZZw61A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t7emOltZSotD_CQ1cmdjE4OjOugalPOH4jn0_6LvjC8m2V0PvayWjxcR_bf8omg2UYHWMVecdYS_dA0TRMpnF19JMBkkGAK5QHY4Z_QYBzP6PQc599r4VS5qp4tBjP18C8_uXMUBk0aOGj043uvQIkViPBOWkoGOX0eSbC1HIUWUx1QS7CZeCgQCyCcLoytied7We-EIiNRaBru0bF3tUMvIp4_54Nine92w2qTYcQ0MQYIeSzlMFRWkfYJBRCuzGhNIv0lcMEMJfBwiVHB9BFrJhvinbaEM82HgihCQRFN-_F58k31B5id0nueGVeZ4sMTkuOGNj65KgrTXAAirjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jHyjuf9gsqj07AN6WpH-tN9UurIocM7w2vqSA6E1-iXSlz4CTM7XIwF0TdLSBb8C9grjmXtEnCHIdKkp1Eb9ihjTt3xWCmsmQL-dbPEkpzPotzJbKUWbX3CM4h7KQPPciym9NusKQNJxodhABNhRNRaqB13TQE2c5EFivjdhv6-ZAegpI1Z_QkYK2gx-u5a5TuzpUCv_YGvzc7q9mVlnMI4AwayivOs74xXvcNN3v_NevfqTDGCQok-wN5vb7IMr82kCq411_nHXwK3kOPwPLmuCOtDQoelZ_gWK8HQegptpDIxZJKDZ80VzUzondY-5L7z4FHzjYqa7nLTziafUXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چه چیز‌هایی از پول به کودکان‌مون در هر مرحله سنی یاد بدیم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/666406" target="_blank">📅 16:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666405">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c24226f40.mp4?token=uA231JPqUbcGlUcZOX-z9gA-clv1443IQv2VHKBz0ahXbRUEqKbu-OkZ8Z6C0O6frir-7XodwwnfvbSye0z46R292me9xdktrBTHUJe_5ocKUediogWi-9kVezVoop439uwa9k0nsvuEi0iwb-W1YMxbPRU_-lDY4P7znmBtzPWIDW0q_VaM-Udfa8xX-M0zxJIHJXdnvAmlrxtg6JKzraxoz0Z0aHMyJp-zUUpy9yepMf2BVA-yFHvYHoEl347lNr4WL5xddnmNx1nDLpW1mMF6B81ZDfvA9zdBvSsCeS02rNi_35rpdOGmp0jvcFOzj7JWi0ULZCWpUifO56aojAR13ZMu40ZcuiBKNGkJypHf0K2tjSHuipTg1L9242mNj9fbNI7ZsnGYZesyOGGORhup4BASJwVZHZKoUd1lDOmIYu7-MSkcyo5ul3tyMbLmR8YgWY9gfuDxuddbV77TBA0FAOoF_BOUelw0wHUKW-oXIV91Fp1ZxXeEnUuKj5DjA1iLSbudDwGIMTwHf2skR94yHBew4D70OB2Zx-8am0Iw1nNIgFCcotFIjUCtgCoTbIEeWnaOqdlXAsIZGWUQNpsR1cVBwjEHtUfclJwjklTpOtvd5tbQxcZk0K6WZP3iMZa6QqYvbK-xTtn6dFV07JrQS5R4_Z8aMk2V3e2xGEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c24226f40.mp4?token=uA231JPqUbcGlUcZOX-z9gA-clv1443IQv2VHKBz0ahXbRUEqKbu-OkZ8Z6C0O6frir-7XodwwnfvbSye0z46R292me9xdktrBTHUJe_5ocKUediogWi-9kVezVoop439uwa9k0nsvuEi0iwb-W1YMxbPRU_-lDY4P7znmBtzPWIDW0q_VaM-Udfa8xX-M0zxJIHJXdnvAmlrxtg6JKzraxoz0Z0aHMyJp-zUUpy9yepMf2BVA-yFHvYHoEl347lNr4WL5xddnmNx1nDLpW1mMF6B81ZDfvA9zdBvSsCeS02rNi_35rpdOGmp0jvcFOzj7JWi0ULZCWpUifO56aojAR13ZMu40ZcuiBKNGkJypHf0K2tjSHuipTg1L9242mNj9fbNI7ZsnGYZesyOGGORhup4BASJwVZHZKoUd1lDOmIYu7-MSkcyo5ul3tyMbLmR8YgWY9gfuDxuddbV77TBA0FAOoF_BOUelw0wHUKW-oXIV91Fp1ZxXeEnUuKj5DjA1iLSbudDwGIMTwHf2skR94yHBew4D70OB2Zx-8am0Iw1nNIgFCcotFIjUCtgCoTbIEeWnaOqdlXAsIZGWUQNpsR1cVBwjEHtUfclJwjklTpOtvd5tbQxcZk0K6WZP3iMZa6QqYvbK-xTtn6dFV07JrQS5R4_Z8aMk2V3e2xGEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یک مهمان خارجی از مراسم تشییع رهبر
🔹
بخدا قسم تاکنون چنین امنیتی را به این شکل ندیدم و مردم ایران واقعا با غریبه‌ها مهمان‌نوازند!
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666405" target="_blank">📅 16:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666404">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خبرفوری
pinned «
♦️
ایران یکشنبه تعطیل شد
🔹
هیئت دولت پس از درخواستهای متعدد از استانهای مختلف کشور برای فراهم شدن امکان حضور مردم در مراسم وداع و تشییع قائد عظیم الشان انقلاب اسلامی و با هدف تسهیل و امکان حضور گسترده اقشار مختلف مردم در آیینهای سوگواری، روز یکشنبه ۱۴ تیرماه…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/666404" target="_blank">📅 16:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666402">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
ایران یکشنبه تعطیل شد
🔹
هیئت دولت پس از درخواستهای متعدد از استانهای مختلف کشور برای فراهم شدن امکان حضور مردم در مراسم وداع و تشییع قائد عظیم الشان انقلاب اسلامی و با هدف تسهیل و امکان حضور گسترده اقشار مختلف مردم در آیینهای سوگواری، روز یکشنبه ۱۴ تیرماه را به عنوان تعطیلی رسمی در سراسر کشور اعلام نمود.
🔹
این تصمیم پس از درخواست‌های متعدد از استانهای مختلف کشور برای فراهم شدن امکان حضور مردم در مراسم وداع و تشییع پیکر مطهر رهبر فقید انقلاب اسلامی اتخاذ گردید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/666402" target="_blank">📅 16:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666401">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EomuwoiFl28sGNncjHpqiv5FwC7zpF5AG1OTmcJVRnjkXPwJELp3H_PMVhAbGfQ4FKH9t-7lWp_2PKESbzUCWtJIfUzVPn2LoBh--nsa-sj9owQlYleqeU16m68n8hrsSagAYHamR4-ZKjWt4uvCNzNXGoVodJW6nFfxetG5q9m-TSZ_6J_nAQJ94z5P88Sl79ubCg5yszMY6KpzuZ2oZcHIel0j2c30N3aLnfCIxbYa1bdTUd0CuBFrsSMur1VMLnpX1SFJ1FmS1gLnycD3cVIkYgZMg4tSXiaUXTZYQgto8oeGcon4LgdCfBm6KjqzB-YhLmK9yoAIas-aAxMWrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خون‌خواهی؛ آرمان مشترک میلیون‌ها آزادی‌خواه / جهان برای تروریست‌ها ناامن می‌شود: درسی که ایران به تاریخ خواهد داد / سرنوشت ترامپ و نتانیاهو چه خواهد شد؟
🔹
همزمان با آغاز مراسم وداع با پیکر مطهر رهبر شهید انقلاب، میلیونها عزادار در سرتاسر کشورمان فریاد خون‌خواهی سرمی‌دهند.
نظر شما چیست؟ گزارش خبرفوری را اینجا بخوانید و کامنت بگذارید
👇
khabarfoori.com/fa/tiny/news-3227630</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666401" target="_blank">📅 16:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666400">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
نماز بر پیکر رهبر شهید توسط کدام یکی از مراجع تقلید اقامه خواهد شد؟
🔹
نماز در تهران توسط آیت‌الله سبحانی
🔹
نماز در قم توسط آیت‌الله مکارم شیرازی
🔹
نماز در مشهد توسط آیت‌الله نوری همدانی #بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/666400" target="_blank">📅 16:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666399">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
بانک مرکزی فقط ۲۰ درصد تقاضای بانک‌ها را تامین کرد
🔹
بانک مرکزی برای دومین هفته متوالی، تنها ۷۰ هزار میلیارد تومان از ۳۶۰ هزار میلیارد تومان تقاضای نقدینگی بانک‌ها را تأمین کرد.
🔹
اقدامی که نشان می‌دهد سیاست‌گذار پولی همچنان از تزریق منابع با نرخ‌های ۲۳ تا ۲۴ درصدی بازار بین‌بانکی خودداری می‌کند.
🔹
این در حالی است که نرخ سود اوراق دولتی به حدود ۳۹ درصد رسیده و شکاف میان نرخ‌های رسمی و واقعیت بازار همچنان پابرجاست./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/666399" target="_blank">📅 16:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666398">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
عبدالمجید الحوثی، از رهبران جنبش انصارالله یمن: هنگام عزیمت هیئت، فرودگاه در محاصره بود و جنگنده‌های سعودی و اسرائیلی بر فراز آن پرواز می‌کردند تا مانع فرود یا پرواز هواپیمای ایرانی شوند
🔹
یمن در برابر آمریکا و اسرائیل تسلیم نخواهد شد و «شهادت» را مایه عزت و پیروزی می‌داند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/666398" target="_blank">📅 16:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666397">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ze_nwxl5l_QT8KIANn5JqG-2k-OtwDvMm57J2eu1AJSV2tPgPjdD6uFi2PhPq_3lnog7IgvgDAg-125Vqo5LX4ua7rnpmEnFNU6bpHp3vBMbKDevDvajVZbOg5AwLeJJ_vaAzBwMpYiFZTeBKrtUW6vEqG1t6fzVQXsv2L6HxvMdxM7Su15quFaBqfLiSSAW-6x6lCxElTuLchm5kmKvSTJyyayVlOt6AWX5BWKyJRDu24eDAtQ6ene23D5dVodcDpcXcTCnq09fdUScybMP_p4-rhyTi0R4JwAOxs-sE4IHAEgtUeznZkpEe4THaUoelaNoHH_JynPLge26oGx01g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: ملت بزرگ ایران با قلب‌هایی مالامال از اندوه و اراده‌هایی آکنده از امید، ثابت خواهند کرد پرچمی که قائد شهید برای برافراشته ماندنش مجاهدت کرد بر زمین نخواهد ماند.
وَنُريدُ أَنْ نَمُنَّ عَلَى الَّذينَ اسْتُضْعِفُوا فِي الْأَرْضِ وَ نَجْعَلَهُمْ أَئِمَّةً وَنَجْعَلَهُمُ الْوَارثِينَ.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/666397" target="_blank">📅 16:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666396">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e7a4ba999.mp4?token=nFPo8Z3yat8ldvIAmUr9L2PG4XA1OSpyxReNtNDj90YoC8NE39biRVBTq-5uIz90tsWyafEM36Qj1JNQfzabADJLoSrLhl1mW9pFzYhqBOI7csPMoiZbWadXXc97dcv1MJcPNEcysTIO_p_wtDaauSfYiRpZFo7WeyxChy07Dj1fn9eOHe54JZbhy_tbwIVFkUJXc5qsqHMyjA57ZUWm7UWoErHQKIX7C11h3luYA_tLga8oSh6HLENLpPtzZx6zUTwAbULYsA3ykmgTaEBQsPZ4WmlOMaAXKH_VQMBPDAl6mZ-JWzF5tFeCF8ISdTbJbB7VW3wupz1JsE4lIKXU5rN5or-ZSNyIUFeFKqktZgsQhxOFkNe64mqrLykoJWxTkEZDfyLNNRZEQoZ04eTtqcrinYnaXktNAZGC4esB5HrTEvHFtwN8b0uoyKc7isdBGBaOF49U6r3ODXzlQJytwPf--Hnfk6EeRvRiFQiqd36vuKDuRNufy___pT8eYrwyNoxQR5RIHiMbs0wHsUu88vhsmygLh5bTTTnKbfkjviV1i2zUOom2Ww73OmG5DoUc-gk5tLUTYa8asihUf27NUBRv5_qdke-cQUjPhEB36hhnDAHFFLerfHW8HBZQlxEQcHOtmTiAL9nIb1XMdu7vzniQDZ9eEWWTBxycwig2QKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e7a4ba999.mp4?token=nFPo8Z3yat8ldvIAmUr9L2PG4XA1OSpyxReNtNDj90YoC8NE39biRVBTq-5uIz90tsWyafEM36Qj1JNQfzabADJLoSrLhl1mW9pFzYhqBOI7csPMoiZbWadXXc97dcv1MJcPNEcysTIO_p_wtDaauSfYiRpZFo7WeyxChy07Dj1fn9eOHe54JZbhy_tbwIVFkUJXc5qsqHMyjA57ZUWm7UWoErHQKIX7C11h3luYA_tLga8oSh6HLENLpPtzZx6zUTwAbULYsA3ykmgTaEBQsPZ4WmlOMaAXKH_VQMBPDAl6mZ-JWzF5tFeCF8ISdTbJbB7VW3wupz1JsE4lIKXU5rN5or-ZSNyIUFeFKqktZgsQhxOFkNe64mqrLykoJWxTkEZDfyLNNRZEQoZ04eTtqcrinYnaXktNAZGC4esB5HrTEvHFtwN8b0uoyKc7isdBGBaOF49U6r3ODXzlQJytwPf--Hnfk6EeRvRiFQiqd36vuKDuRNufy___pT8eYrwyNoxQR5RIHiMbs0wHsUu88vhsmygLh5bTTTnKbfkjviV1i2zUOom2Ww73OmG5DoUc-gk5tLUTYa8asihUf27NUBRv5_qdke-cQUjPhEB36hhnDAHFFLerfHW8HBZQlxEQcHOtmTiAL9nIb1XMdu7vzniQDZ9eEWWTBxycwig2QKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزا عزا است امروز
خامنه ای رهبر
پیش خداست امروز
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666396" target="_blank">📅 15:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666395">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82fbe4e3be.mp4?token=KksjzQlk1TU51T4n0MxEpZ64_5EqrT9uNBJMVl6fpXW-k1lGaiAtD4cUV7QaEaxjrXsS4_9LqHKABLZ0uavdDqNZh1M3UikreqrtNzjcgZWOKc2_WGqsNJhDrTkE2kB2bz5ni-BsXVCVogz_XivTcJxEI5MvIKjnTzT81p737sd4zBzFhpkqkoOlcMNRETripZLksi9qocPW5Bzas3JMEXwpC41-4iB6xcmir33C76RgNcanuDUbTOPceBamMSbUCuShsTOK-z9hNa1BEXd8HbNWhFHlRmLg7m8Q1U5oGk-TlUaUK5cK3hVCGVWmJdCrbNDE_ZGRp8u6WRfTntw8uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82fbe4e3be.mp4?token=KksjzQlk1TU51T4n0MxEpZ64_5EqrT9uNBJMVl6fpXW-k1lGaiAtD4cUV7QaEaxjrXsS4_9LqHKABLZ0uavdDqNZh1M3UikreqrtNzjcgZWOKc2_WGqsNJhDrTkE2kB2bz5ni-BsXVCVogz_XivTcJxEI5MvIKjnTzT81p737sd4zBzFhpkqkoOlcMNRETripZLksi9qocPW5Bzas3JMEXwpC41-4iB6xcmir33C76RgNcanuDUbTOPceBamMSbUCuShsTOK-z9hNa1BEXd8HbNWhFHlRmLg7m8Q1U5oGk-TlUaUK5cK3hVCGVWmJdCrbNDE_ZGRp8u6WRfTntw8uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز همای برای رهبر شهید خواند
🔹
نماهنگ «عشق دل‌افروز» با صدای «پرواز همای» در روزهای وداع و تشییع رهبر شهید منتشر شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666395" target="_blank">📅 15:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666394">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67b25c7636.mp4?token=SGVvxzmxnpRdqNlKVYPqH6JU1MjP5SouKQoyuinGuYZ-rbLaLqBxA_u-aqIl6IxxAzPFxHWPnaNljY3CY4cUyiKRk3zNfGyzn8Q1E9YWL-4w5Qi1TCiWUemZmYyLv_B33aud27Z_N04Keb-3mIgg9_dCzxTeGADjjVw1N0YsFCWLPVYrO98iyKxyTBNe72pEdvcokoyV9dpKaUjwiSEookwRtGWG7zgqdIQ2CfZUhLINZGKCDQwM3je4Dl87ukA4l3QqbDxytKBFQ8PQfvAAEMAoL-qMHi-EZMZrviQG4pbn_C9G7hAuBxBBk-WtK6mAKrCDB9iTu1F0m7Mjf08DoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67b25c7636.mp4?token=SGVvxzmxnpRdqNlKVYPqH6JU1MjP5SouKQoyuinGuYZ-rbLaLqBxA_u-aqIl6IxxAzPFxHWPnaNljY3CY4cUyiKRk3zNfGyzn8Q1E9YWL-4w5Qi1TCiWUemZmYyLv_B33aud27Z_N04Keb-3mIgg9_dCzxTeGADjjVw1N0YsFCWLPVYrO98iyKxyTBNe72pEdvcokoyV9dpKaUjwiSEookwRtGWG7zgqdIQ2CfZUhLINZGKCDQwM3je4Dl87ukA4l3QqbDxytKBFQ8PQfvAAEMAoL-qMHi-EZMZrviQG4pbn_C9G7hAuBxBBk-WtK6mAKrCDB9iTu1F0m7Mjf08DoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاعر عراقی: به کوری چشم بدخواهان، سراسر عراق با تمام وسعت و عظمتش به تو درود می‌فرستد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/666394" target="_blank">📅 15:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666393">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7ddc6fdf.mp4?token=alV7K_g_vnwg2qsIayh_Q4IsNIrn7htt_ilc-D8DWlKltinH4fzXLStZnLxDybpLD_sRy1CvVpibzzEAWOM12yokLhS-kMgn12ARpYKm0l8TeZPNJRQ03GtuI1Mhnic7cbPXLFYTrEk-ogCryvpKQfgLU-WLRwhCKSS6M4Ru2GocoORsD1WJbMPP3s40_sXMTRktAW-uaxTvUJ-FbEbhu55CJW3TBLT328EtWuuBd79-DMvhU3MxUyt3Vqf20DWY6vtiGtsQvFIMdjOzykOMGCqhGEysMJQTlnJhIbDSopSHUnXs6_HVo-GcSq21Or3WGP1QGAMcsuSMXKzfGq-4_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7ddc6fdf.mp4?token=alV7K_g_vnwg2qsIayh_Q4IsNIrn7htt_ilc-D8DWlKltinH4fzXLStZnLxDybpLD_sRy1CvVpibzzEAWOM12yokLhS-kMgn12ARpYKm0l8TeZPNJRQ03GtuI1Mhnic7cbPXLFYTrEk-ogCryvpKQfgLU-WLRwhCKSS6M4Ru2GocoORsD1WJbMPP3s40_sXMTRktAW-uaxTvUJ-FbEbhu55CJW3TBLT328EtWuuBd79-DMvhU3MxUyt3Vqf20DWY6vtiGtsQvFIMdjOzykOMGCqhGEysMJQTlnJhIbDSopSHUnXs6_HVo-GcSq21Or3WGP1QGAMcsuSMXKzfGq-4_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جکسون هینکل، چهره رسانه‌ای و اینفلوئنسر آمریکایی در حال توزیع شربت نذری در مصلی تهران
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666393" target="_blank">📅 15:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666391">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqZewV9lgPo5epJ0ahO28V6RT8eLyHAIbMLKFSZOeZOCmVfOtM0j0IAg1GQ6vLIiusdUdUoC8_TnToBLloor9u_-oIXSZv1Pd9VgMuBzZ0iAqhEbcA2DSCEM4f9RXo-yHxqcC6x9bXI72xiwMY7stU2CgHtM00tyMCBHzSUH2zAQxzO3VWxDlfheuOH5hsSv0oPJ--ux794keP8JsMOVu-RDq4ugPHYPB_2lqlhnFU-nNq7sUrz8Mmm_p2dQE45buOxvjEXId7ckH-Z2JxOOnt2K81Es9KSP6tpHtgGBsFMkGOqMtD8lX0PT4LoTFZHlBJaexOF_W0TImxpi-6rrMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کره‌جنوبی برای فتح هوش مصنوعی، هزار میلیارد دلار روی میز گذاشت
🔹
کره‌جنوبی از بزرگ‌ترین برنامه سرمایه‌گذاری تاریخ خود برای تبدیل شدن به قدرت اول هوش مصنوعی رونمایی کرد. بر اساس این طرح، نزدیک به یک تریلیون دلار در توسعه صنعت نیمه‌هادی، رباتیک و دیتاسنترها سرمایه‌گذاری خواهد شد.
🔹
در این پروژه، سامسونگ و SK Hynix بیش از ۵۱۳ میلیارد دلار سرمایه‌گذاری می‌کنند و چهار کارخانه جدید تولید تراشه حافظه در کره‌جنوبی می‌سازند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666391" target="_blank">📅 15:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666390">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUHMBYR3VazgKRGH5Bs6RnikgR-hl0EBywLxjxtMOM6mtXNJHNHXsKeBYnDawZOPWtTnZpvp_NWz_LoKF_B8r6sP555PeVKXBgtU4iGs1B76nKJYWdABlghXh6e0AZvwx3heSuZUuiP-i2ePZSZ8d-8Ifci45JgnA7tKfvUipyuszX_LjK74RzRr-4-70B-wxm24IqoTdwFX9_VAyFzpdFxneqfZxe_ersMzdQuHO_7Ydtoe9AJu5RePpn4tN7pA1D8N8Hd-PW7nBJnm3arUALJy7JEJSJJE8RcrV_qAtkmmOKPdIOhc2eriCUG_r1ENJKtglf7A4Et9XFBauumMmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بنر دیده شده در ورودی مصلی؛ انتقام خون امام شهیدمان چه شد؟
#خونخواهی
‏⁧
#هزینه_خواهید_داد
⁩
‏⁦
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666390" target="_blank">📅 15:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666388">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b5f9c0d3.mp4?token=fVE84Do0fYLnugl9pdWp9A6qQE1x1YCrMyoDNByU2WoE9e2UJQDLhVpz-dbrMc9SxycfElg2ecpt5iH7G3viHXT7aWoPNKUxOp_JXPR1bunmwUIYHbRT9hXj1tL8k2KzaL0g97Nz8jJl2rMa77kuQR9QGDukRvjv4WsQOyTDalypaMG28C4yXZ_UGPCb6zvecVOedZBRghhQTy9HAySc6EgZzkNedGPrghKVpxb8TC0N1TUjldBUnut3iGcJ6OMcIWMR7z8Hur554yr1EexaFyaom3-pB18YTo4PPNs4eqgdfW41V5-A6-00fv6ZVkdw1mTU1i7wTLCgAy1fogGhCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b5f9c0d3.mp4?token=fVE84Do0fYLnugl9pdWp9A6qQE1x1YCrMyoDNByU2WoE9e2UJQDLhVpz-dbrMc9SxycfElg2ecpt5iH7G3viHXT7aWoPNKUxOp_JXPR1bunmwUIYHbRT9hXj1tL8k2KzaL0g97Nz8jJl2rMa77kuQR9QGDukRvjv4WsQOyTDalypaMG28C4yXZ_UGPCb6zvecVOedZBRghhQTy9HAySc6EgZzkNedGPrghKVpxb8TC0N1TUjldBUnut3iGcJ6OMcIWMR7z8Hur554yr1EexaFyaom3-pB18YTo4PPNs4eqgdfW41V5-A6-00fv6ZVkdw1mTU1i7wTLCgAy1fogGhCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باران دل‌نوشته‌ها در سوگ رهبر شهید
#بدرقه_یار
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/666388" target="_blank">📅 15:36 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
