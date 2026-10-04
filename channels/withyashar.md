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
<img src="https://cdn4.telesco.pe/file/Kg-pu_jp8PBvsi_tH9Njg_fZz5twHDjx-u7TDZHdFZirIZgV_8ERtPLHTCCetmn4wc6ZbmDAsDKgyOkwxViX8nBxafOtYLkhbCCPqJ1L6HAqeXhghMI28aBf_UoobeasBVONuNfNVT6U_e8NoPEpudH9L1IL9VlVlEcFi14DXkssl8TYgB4bZgNu3-Gr0hOKJTFs_W89yqjHYvpKyh732Sab3cAZi8UJpvoebUTA6q4ZcVIxey0U8iY2oOyjQAvep1wi1KnjrzEIUUuyqDDYqxs4wc7XDqX8yHAvEQW5IwUAKoVOefhCAyAu3N--pxLYlmIPU2Sir6Zf8khu1WWJMg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 489K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 16:08:11</div>
<hr>

<div class="tg-post" id="msg-24885">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94d80c6a7.mp4?token=ETWwxkdmaguzx-RDMPtq5tRo2wkHHjYL4nJ6KW0788UOcBZXEBmyHzIJB8feRKDBiaiqfvpN1x7jc3UpBLdeZQQZQkV7lkgiqHOsmiy8yWh9-UOsg4Ot2ehP6-lfJ7ZomvPjnsbzZiGl_3w46q635hTSbOZlJ_2u1QgeZ6ZM3gQtJbUP7cDaM_H0x--ZZp7RKy-L7N9ZBYvXkYJbWaZLzZfkR26ptL2pX36jdep2lqQNUUmYX9nY6nq6Gim5RppRo7els7BST1rPlgj9VP5r17_k5-8D0stLe6CB3CTR3bWZmw519g6VHjj4JbublfHxmWZQeDGwapC3AABvKoFwSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94d80c6a7.mp4?token=ETWwxkdmaguzx-RDMPtq5tRo2wkHHjYL4nJ6KW0788UOcBZXEBmyHzIJB8feRKDBiaiqfvpN1x7jc3UpBLdeZQQZQkV7lkgiqHOsmiy8yWh9-UOsg4Ot2ehP6-lfJ7ZomvPjnsbzZiGl_3w46q635hTSbOZlJ_2u1QgeZ6ZM3gQtJbUP7cDaM_H0x--ZZp7RKy-L7N9ZBYvXkYJbWaZLzZfkR26ptL2pX36jdep2lqQNUUmYX9nY6nq6Gim5RppRo7els7BST1rPlgj9VP5r17_k5-8D0stLe6CB3CTR3bWZmw519g6VHjj4JbublfHxmWZQeDGwapC3AABvKoFwSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر خبرنگاران از
پرواز چندین بمب‌افکن راهبردی بی-۱ لنسر آمریکا
از پایگاه نیروی هوایی سلطنتی فیرفورد در بریتانیا منتشر شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/withyashar/24885" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24884">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سخنگوی وزارت خارجه: بحث خروج ایران از NPT بسیار جدی است و در محافل سیاسی کشور مطرح است
@WarRoom</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/24884" target="_blank">📅 14:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24883">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73c4bbc2f0.mp4?token=eTOXln5cp-dZ6D_2rH33uBzlOLS4QuMCqtEkZOS0TwVBhFEguq_Cqfvm2qlWOtr0-iRqL_bCdbTuKNZtxpIqUSCFoxELpRmWXANUzzJQha9Rq4kBQaWjaI9Jfhyh9z5ER03qw-eG5mcv53Ndt3NWnj1yBgdWExPHux210nojAM52opJZdfL9w1ImgeXsAYy9QMsqw8O2vunYWmiPgQe8oxvOa7Sj-TjvlIVgVigGLQLMyfnWI2f1uh6YfwNDTfv4HtWbUdqWF3mt7PVPfnKGCncBV_3Sh1mlv8CdtpAQ6ro1rADIKv5k1Sh3GIOoSiIQ8MnECL03QyUDsw0wyJHtRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73c4bbc2f0.mp4?token=eTOXln5cp-dZ6D_2rH33uBzlOLS4QuMCqtEkZOS0TwVBhFEguq_Cqfvm2qlWOtr0-iRqL_bCdbTuKNZtxpIqUSCFoxELpRmWXANUzzJQha9Rq4kBQaWjaI9Jfhyh9z5ER03qw-eG5mcv53Ndt3NWnj1yBgdWExPHux210nojAM52opJZdfL9w1ImgeXsAYy9QMsqw8O2vunYWmiPgQe8oxvOa7Sj-TjvlIVgVigGLQLMyfnWI2f1uh6YfwNDTfv4HtWbUdqWF3mt7PVPfnKGCncBV_3Sh1mlv8CdtpAQ6ro1rADIKv5k1Sh3GIOoSiIQ8MnECL03QyUDsw0wyJHtRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «درباره ایران تصمیمم را خواهم گرفت. ایران
تقریباً نابود شده است.
» وقتی از او پرسیدند آیا پس از نشست کمپ دیوید به تصمیم نهایی نزدیک‌تر شده است، گفت: «تنها مسئله این است که
یا راه آسان را انتخاب می‌کنیم یا راه سخت را.
»
@WarRoom</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/24883" target="_blank">📅 13:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24882">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خلبان هندی به نتانیاهو: "کمک خلبان عمانی برای نماز صندلیش را ترک کرد ، و من به احترام او، به عقب نگاه نکردم. بعد از چند دقیقه، ضربه‌ای شدید حس کردم گیج شدم و متوجه شدم اتفاقی برای هواپیما افتاده است."
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24882" target="_blank">📅 12:18 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24881">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دلار ۲۷۲،۰۰۰ تومان
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24881" target="_blank">📅 12:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24880">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رویترز: نیروهای مسلح یمن بامداد امروز یکشنبه اعلام کردند حملات گسترده‌ای را علیه مواضع حوثی‌ها در صنعا و صعده آغاز کرده‌اند. این حملات در ادامه تشدید درگیری میان نیروهای مورد حمایت عربستان و حوثی‌های مورد حمایت ایران انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24880" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24879">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkE897TkRt3Bj6Dd1jeX2dSrHkRNWWEaGC4DWgfsPspbQOcnsRWxKt6roBAcTYKf4uKlTVlVyxsstRm6729_PTvk6jPq8pnf70vnOlgd1vr7EHPwNAJU1M40fjrYXdsaQdT9MIuMrZEDZ7N0Ki2mAFxyvQsduC-dwhc49m1OsI-ng23MWuojcdxgUYARZgDhOlfnvaMjua94Huq9iVyra6D60K_jcyn9qZYJyUuOP8jT5Tlh9lbZOy_3OiRj5w4bbq3K95MmK5znoniANhAJEmgx9PLQL9jWJUA8DBiDQNFutPcZLakBPP6Jd3fxoFyb0cN48BiyEw3ngEyV6u1MQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:
یک نفتکش در داخل تنگه هرمز هدف یک پرتابه ناشناس قرار گرفته و موتورخانه آن آسیب دیده است.
خدمه در سلامت هستند و تاکنون هیچ آلودگی زیست‌محیطی گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24879" target="_blank">📅 11:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24878">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r11Pgrag_cqn3uZkDRsd34UOOAXdworrhyJLYmLkFXHXyHAhyUbVuv3pYpjm4E7wruGUVv7Z5fPVNUA5iEhOzad7yhZmhyVNdlD3DaYquzRlvSmbgQAbKJYt9XWJ2OTtDpu71aV_2c3NLLeh3CfXC9cENN60Qi_cncnni-McRB9LM8F0JnDlhTPe_BVApJf3mZLoNURlQhHQ2NLf0mE7raK6gZlu4sYTvGMoqhmnWthyfNoo6Cs_wAPe0sMXhUJIb-QYmhXWqWkXA_zu43RYwab9IE0WqvLilVmGdomn20jUMPykK9z4cnapTC4R5h6X7Xkh3HjU9L4EMF8y28Ei1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامگزاری جدید معابر در تهران
میدان نوبنیاد=شمخانی
بلوار دریا=تنگسیری
خیابان ارم=خرازی
یه بزرگراه جدید=موسوی
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24878" target="_blank">📅 11:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24877">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سپاه استان تهران: تا ساعت ۱۶ امروز عملیات انهدام مهمات عمل‌نکردهٔ دشمن در پاکدشت انجام می‌شود؛ احتمال شنیدن صدای انفجار ناشی از این عملیات وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24877" target="_blank">📅 10:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24876">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سی‌بی‌اس: برت مک‌گرک، مقام ارشد پیشین امنیت ملی آمریکا، گفت بنیامین نتانیاهو در دسامبر ۲۰۲۴ و هم‌زمان با مذاکرات آزادی گروگان‌های غزه، پیشنهاد حمله به تأسیسات هسته‌ای ایران را مطرح کرده بود. مک‌گرک گفت پس از انتخابات ۲۰۲۴، مقام‌های آمریکایی نگران بودند ایران به‌سرعت به سمت ساخت سلاح هسته‌ای حرکت کند و واشنگتن توافق کرده بود اگر چنین اقدامی شناسایی شود، آمریکا تأسیسات فردو را هدف قرار دهد. به گفته او، آمریکا هیچ مدرکی پیدا نکرد که ایران چنین تصمیمی گرفته باشد و به تهران هشدار داده بود وارد این مسیر نشود. مک‌گرک افزود نتانیاهو با وجود این، به‌وضوح در حال بررسی اقدام نظامی علیه ایران بود.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24876" target="_blank">📅 10:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24875">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مم باقر : دوران دیکته‌ کردن مطالبات یک‌طرفه  گذشته است و تا زمانی که هفت شرط ما بر اساس تفاهم نامه اسلام آباد، محقق نشود تنگه‌ هرمز باز نخواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24875" target="_blank">📅 09:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24874">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دایرکت پره که اصفهان صدای انفجار سنگینی اومده ، فعلا نمیشه تایید کرد</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24874" target="_blank">📅 09:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24873">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اصفهان رو گویا زدن
🚨
⚠️
🚨
⚠️
🚨
⚠️
🚨
ادکی صبر میکنیم خبر‌ درست بیاد</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24873" target="_blank">📅 09:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24872">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFeWIV-1fbvSNCSJTAj21-WyTjDgY-qO_xWJcM49vq0cux27NMWtQ-xqqeSmSYSVnx9aYnfF3N_Oe4rKriHWPJwsIDTsl8_MWGIcvnGXLcbifwXbvw_bjhxaB4syfyXzUYto5zXlXjebcyxop8cwZpr5MnlXqXXuhqfLYMxdgGk-oqwCwa9RAX7MmNQma94VQYXx0lJ62if8zGTPxYbG7UZDNUal3gKhZ_3kLYhiwSinUja0JhbwAB0RNGq55GiRPfXSn50WoL0B7dARAWyT_KvN2ph5SgOX5aJD1S5ivgnUwfhBdUSAmJSmkq7bEiszKIZsiCInQsll_pSgsqYJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز :
ناو هواپیمابر جورج اچ. دبلیو. بوش (سی‌وی‌ان-۷۷)
با حدود ۴۸۰۰ نفر خدمه وارد آب‌های نزدیک پوکت تایلند شده است. این ناو پس از چند ماه حضور در منطقه و پشتیبانی از عملیات آمریکا در خاورمیانه، برای استراحت و بازدید بندری وارد تایلند شده است و این توقف موقت است. ‌
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24872" target="_blank">📅 09:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24871">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بلومبرگ:
ایران خود را برای دور جدید و احتمالاً گسترده‌تر حملات آمریکا آماده می‌کند
و سپاه از پاسخ فوری و دردناک به هرگونه حمله آمریکا یا اسرائیل خبر داده است. در مقابل،
توان ایران برای کنترل تنگه هرمز و محدود کردن صادرات نفت در حال کاهش است.
ارزش ریال طی دو ماه ۲۵ درصد افت کرده و ایران در سپتامبر هیچ نفت خامی از طریق نفتکش‌ها صادر نکرده است. مقام‌های ایرانی انتظار دارند
پس از انتخابات ۳ نوامبر آمریکا، تنش‌ها افزایش یابد.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/24871" target="_blank">📅 03:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24870">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کان نیوز عبری : تا قبل از ۵ آبان، هر لحظه؛ جنگ قریب الوقوع است
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/24870" target="_blank">📅 02:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24869">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/24869" target="_blank">📅 02:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24868">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نیویورک‌تایمز: مقام‌های بریتانیا و آمریکا معتقدند افرادی که در ارتباط با حادثه پایگاه هوایی RAF فیرفورد بازداشت شدند، با عملیاتی مرتبط بوده‌اند که از سوی ایران حمایت می‌شده است. مقام‌ها میگویند سپاه پاسداران یا یکی دیگر از نهادهای نظامی ایران در این ماجرا نقش داشته؛ زیرا پایگاه فیرفورد در حملات بمب‌افکن‌های آمریکایی علیه ایران مورد استفاده قرار گرفته بود. پنج مرد بریتانیایی و یک فرد دوتابعیتی بریتانیایی-ایرانی بازداشت شدند. ایران هرگونه دخالت در این ماجرا را رد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/24868" target="_blank">📅 02:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24866">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یا موسی
😁
🙌🏾</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24866" target="_blank">📅 02:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24865">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تماس تصویری در واتساپ با بهره‌گیری از اینترنت ماهواره‌ای مستقیم استارلینک به گوشی؛ بدون نیاز به آنتن و دکل مخابراتی.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/24865" target="_blank">📅 01:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24864">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">برنامه منبر امشب ۴-۵ صبحه
😂
🙌🏾</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24864" target="_blank">📅 01:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24863">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eba7bd0a3f.mp4?token=LYAHjIKcrj4_XAVNsBaf1frYPTeE3QMmhvxTxq-4eQrQZW_Z9v82jhue5kD8P7V1AfED5YEKsurYN1eqgi7gj0zwBrIUGEvmDzRO4ynoVSUHierl4vu7PD0SdayIPW9BvWqZLU2hvElUB4a-pw8GjNXYczb5JkVTPHtvAfZ0LTg1oJ0xWTGaWgSRkeqHaucG6IGpP0Gy4-Q63TGO9lAOvLFAgEVSjyyct8xoRYo06T5n_iRUKxgtxX9S0HgavKCCzm5BjZGt5j6GRTscSX_Okq1TQwuoog_6TPKJE1W88q37swya6rZQDYc2ku0iko4OY3nok4LGZdsEag6wr3vHbpnKPMAGzTZwFaplVKIiJitb2E-L_QVWW2Cj0_qRX28OtuM80TzgibrwfORNDQ8bIQ9qchI2N259uocolrAF0faLmS-2YSYBGOjqFTfr0m5vuBi35VLYgWo1AzySOe4Z2vW-rE0T3VXD0hRsg2EUvhGneN48ndk0yke-PC7wnFY3--XyVw2r-UL_qIBMsbmJ1VMrV5PBqxXWlDsEO6YwWYCPWjY947EXVu6AsT11_JKFKFxiSQLRSMJhkF6rFj5WCjuMDeJ32Az-AfJEoLO12ZHH88UehTjhPFKfAAkufCfHh6f50PKSE1o9azMv5aZEh6GaxuQ8Iu3fF5pYlrAvOFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eba7bd0a3f.mp4?token=LYAHjIKcrj4_XAVNsBaf1frYPTeE3QMmhvxTxq-4eQrQZW_Z9v82jhue5kD8P7V1AfED5YEKsurYN1eqgi7gj0zwBrIUGEvmDzRO4ynoVSUHierl4vu7PD0SdayIPW9BvWqZLU2hvElUB4a-pw8GjNXYczb5JkVTPHtvAfZ0LTg1oJ0xWTGaWgSRkeqHaucG6IGpP0Gy4-Q63TGO9lAOvLFAgEVSjyyct8xoRYo06T5n_iRUKxgtxX9S0HgavKCCzm5BjZGt5j6GRTscSX_Okq1TQwuoog_6TPKJE1W88q37swya6rZQDYc2ku0iko4OY3nok4LGZdsEag6wr3vHbpnKPMAGzTZwFaplVKIiJitb2E-L_QVWW2Cj0_qRX28OtuM80TzgibrwfORNDQ8bIQ9qchI2N259uocolrAF0faLmS-2YSYBGOjqFTfr0m5vuBi35VLYgWo1AzySOe4Z2vW-rE0T3VXD0hRsg2EUvhGneN48ndk0yke-PC7wnFY3--XyVw2r-UL_qIBMsbmJ1VMrV5PBqxXWlDsEO6YwWYCPWjY947EXVu6AsT11_JKFKFxiSQLRSMJhkF6rFj5WCjuMDeJ32Az-AfJEoLO12ZHH88UehTjhPFKfAAkufCfHh6f50PKSE1o9azMv5aZEh6GaxuQ8Iu3fF5pYlrAvOFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: «ضمناً، همان‌طور که می‌دانید،
ایران عملاً از هرگونه برنامه‌ای برای ساخت سلاح هسته‌ای دست کشیده است.
»
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/24863" target="_blank">📅 01:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24862">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d5038c3fc.mp4?token=jxf379R90bA93myFNdxaCBqxK2QrSDxWQ3-Czso4y7Ox4I_auPV9USD9fZ6bCN7mkd_nfXm5qBJNLhc9qlOn7E4ZYFRy2cA0csv4vibYPpNHkEy15cTZQMESZcXbivVSgoeumtFZa6yxjR_0ZN6-D2YrTYMKIKHONzPzpoCitNbiOEaFB4c2VANNUcqbxcXy-NhTUUtCzMuN9XIdLPjBejdliQLeD6V_1xMpYhcSNyb-YY6cczBuPR9IZYugxpWsEheBQ9b9T1V_StV4i0IG-W17v8L4TEzgM-z9opWKWXMuBNLJ_DMohgMCRuzy3jMakreeYz96fCY3Rq9yM-u09g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d5038c3fc.mp4?token=jxf379R90bA93myFNdxaCBqxK2QrSDxWQ3-Czso4y7Ox4I_auPV9USD9fZ6bCN7mkd_nfXm5qBJNLhc9qlOn7E4ZYFRy2cA0csv4vibYPpNHkEy15cTZQMESZcXbivVSgoeumtFZa6yxjR_0ZN6-D2YrTYMKIKHONzPzpoCitNbiOEaFB4c2VANNUcqbxcXy-NhTUUtCzMuN9XIdLPjBejdliQLeD6V_1xMpYhcSNyb-YY6cczBuPR9IZYugxpWsEheBQ9b9T1V_StV4i0IG-W17v8L4TEzgM-z9opWKWXMuBNLJ_DMohgMCRuzy3jMakreeYz96fCY3Rq9yM-u09g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «درباره ایران تصمیمی دارم که خودم آن را خواهم گرفت.
یا راه آسان را در پیش می‌گیریم، یا راه سخت را.
»
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/24862" target="_blank">📅 01:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24861">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مقام ارشد آمریکایی به آکسیوس:
2 دیپلمات ایرانی امروز صبح از آمریکا اخراج شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/24861" target="_blank">📅 23:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24860">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6458715c79.mp4?token=bp2pK0F_boR4zDicRl88n3Rc-UC3M93vMVxnr0UFkavWIMQoBrTS6LVh-znH0Mx7VpFY1mgSwIEOySfNkQ38vqWdHjxEC5Y62xtaMgN_kQ7pPTA9vA7Gn9b7zkdsheYhUDEQKDQvLF-Dt6tgjRArMYrpFyDAG3VsLAAwuJH5uikBDMEpibznpSMc5nz0PaztcBR_5vYnZurpHDSJi8cSDUkpr9fWC2Z9cGv1lCjGEX5vC1gDFNzVD0WEh4a2fFX0UO9USi5pzmS3itOK4fl9vgwL_iDjTYSVnqUvjbz8YOAc0OgCTMyBAQmGDscdR4QIznmquwbhP5gIMDpDidSjVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6458715c79.mp4?token=bp2pK0F_boR4zDicRl88n3Rc-UC3M93vMVxnr0UFkavWIMQoBrTS6LVh-znH0Mx7VpFY1mgSwIEOySfNkQ38vqWdHjxEC5Y62xtaMgN_kQ7pPTA9vA7Gn9b7zkdsheYhUDEQKDQvLF-Dt6tgjRArMYrpFyDAG3VsLAAwuJH5uikBDMEpibznpSMc5nz0PaztcBR_5vYnZurpHDSJi8cSDUkpr9fWC2Z9cGv1lCjGEX5vC1gDFNzVD0WEh4a2fFX0UO9USi5pzmS3itOK4fl9vgwL_iDjTYSVnqUvjbz8YOAc0OgCTMyBAQmGDscdR4QIznmquwbhP5gIMDpDidSjVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/24860" target="_blank">📅 23:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24859">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دوستان عزیز من رفتم یه عرق خوری دیگه
🤣
🫱🏼‍🫲🏽
🙌🏾
سلامتی همگی‌، خبری نیست</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/24859" target="_blank">📅 23:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24858">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95f6e7c28a.mp4?token=jOwS41ZIFcIhLv7P3JKn_dLZYtzTftrVxwwDhgCNPK1t1QHcj-9XL-TSukNaGGD_WkKChP8mLRj3VLs3jjwc2yJt5iXdNIE6RxmGalvNc84vNvWo7AVhWjgYQhPLqtkK_RV24WewBnkDDkNZXwKk0oPcqE0PrHdUb_FMJWlFz1U4YqAhaKp3t0-Rcza2b_gIyyiJbFE2z4vzj9BKpzi3laut5HTfjvT-P1WoFI6eQ7Z_-XuFEGKJLjZT3WV7WZPo87wrlyEMY053edl4BGI5R2gEtkjgX_-lDzNhU5NxmBPvQPbH2RwbJ14eZZqCngLMX14v8H2hr2lokYnGLWpOYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95f6e7c28a.mp4?token=jOwS41ZIFcIhLv7P3JKn_dLZYtzTftrVxwwDhgCNPK1t1QHcj-9XL-TSukNaGGD_WkKChP8mLRj3VLs3jjwc2yJt5iXdNIE6RxmGalvNc84vNvWo7AVhWjgYQhPLqtkK_RV24WewBnkDDkNZXwKk0oPcqE0PrHdUb_FMJWlFz1U4YqAhaKp3t0-Rcza2b_gIyyiJbFE2z4vzj9BKpzi3laut5HTfjvT-P1WoFI6eQ7Z_-XuFEGKJLjZT3WV7WZPo87wrlyEMY053edl4BGI5R2gEtkjgX_-lDzNhU5NxmBPvQPbH2RwbJ14eZZqCngLMX14v8H2hr2lokYnGLWpOYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظۀ اصابت صاعقه به برج میلاد
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/24858" target="_blank">📅 22:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24857">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/24857" target="_blank">📅 22:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24856">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/24856" target="_blank">📅 22:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24855">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">واشنگتن‌پست: ارتش آمریکا در حال آماده‌سازی برای افزایش گسترده حضور نظامی در خاورمیانه است و ممکن است تا ماه نوامبر سه ناو هواپیمابر به همراه ناوهای اسکورت آنها وارد منطقه شوند. در صورت اجرای کامل این طرح، نزدیک به ۲۰ هزار buنیروی نظامی، تا ۱۵۰ جنگنده و چندین ناوشکن مجهز به موشک به منطقه اعزام خواهند شد. همزمان یک گروه آبی‌خاکی سه‌ناوه نیز از کالیفرنیا به سمت منطقه حرکت کرده است. مقام‌های آمریکایی می‌گویند هدف از این اقدام، افزایش گزینه‌های نظامی دولت ترامپ و فرماندهان آمریکایی در شرایط جنگ با ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/24855" target="_blank">📅 22:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24854">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نیویورک‌تایمز: مقام‌های بریتانیایی و آمریکایی معتقدند افرادی که در نزدیکی پایگاه هوایی RAF Fairford بازداشت شدند، با عملیاتی مرتبط بوده‌اند که مورد حمایت ایران بوده و احتمالاً به سپاه پاسداران یا یک مرکز فرماندهی نظامی جداگانه در تهران مرتبط است.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/24854" target="_blank">📅 22:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24853">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Remix Az Asemoon Dare Miad Ye Daste Hoori ~ Otaghe jang</div>
  <div class="tg-doc-extra">Yashar</div>
</div>
<a href="https://t.me/withyashar/24853" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
@withyashar
📱
https://instagram.com/yashar</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/24853" target="_blank">📅 21:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24852">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏اکونومیست: نشانه‌های نظامی از احتمال آغاز حملات در ۷۲ ساعت آینده حکایت دارد
‏اکونومیست با اشاره به داده‌های ردیابی پروازها از تجمع کم‌سابقه هواپیماهای سوخت‌رسان در پایگاه العدید و اعزام هواپیماها و یگان‌های جستجو و نجات رزمی به شرق منطقه خبر داده است. بر اساس این گزارش، هواپیماهای شنود و جنگ الکترونیک آمریکا نیز فعالیت گسترده‌ای در منطقه دارند. تحلیلگران نظامی مورد استناد این گزارش، این آرایش نیروها را نشانه آمادگی برای آغاز احتمالی حملات در آینده نزدیک ارزیابی کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/24852" target="_blank">📅 20:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24851">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نیویورک‌تایمز: مذاکرات آمریکا و روسیه برای پایان جنگ اوکراین شامل یک معامله چندمیلیارددلاری مانند رشوه برای خرید دارایی‌های نفتی لوک‌اویل شده است؛ معامله‌ای که می‌تواند به نفع دو گروه تجاری خاورمیانه‌ای مرتبط با خانواده جرد کوشنر و استیو ویتکاف باشد. این توافق به تأیید آمریکا و کرملین نیاز دارد و پوتین در دیدار با ویتکاف و کوشنر آن را مطرح کرده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/24851" target="_blank">📅 20:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24850">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e4d2ebd7d.mp4?token=uFwvqZ8BtQunrhWmj3Wtahg5APqVeNcRyaXJE-WObn0xceA9QoHaEUJ6p4V4j-bx6KT4BJqZqN9ZVpp7Mihj4zeae2cJ4tDCWVFaBOX2vGG-ioOoWnc86WkB5RBvKr3BJE3NGrEu-yxquYTZaNleHrkfUPE6aREsOdf6A39dzxZH6NhhiByidr5UW0yelVC6N6Y-L365F5CCXA8XriT-oAym6TXweo5_xrozYj1NSBP-1c73VTYAwbweK-QT76qM_RtVNBa3ZSZ2wBpdxNZBULAUk9T3kLaxX_cOksl9IgSmyc1iXeugiCXkrmYQztDIoA5tCuazxQoxC0IgQ19rXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e4d2ebd7d.mp4?token=uFwvqZ8BtQunrhWmj3Wtahg5APqVeNcRyaXJE-WObn0xceA9QoHaEUJ6p4V4j-bx6KT4BJqZqN9ZVpp7Mihj4zeae2cJ4tDCWVFaBOX2vGG-ioOoWnc86WkB5RBvKr3BJE3NGrEu-yxquYTZaNleHrkfUPE6aREsOdf6A39dzxZH6NhhiByidr5UW0yelVC6N6Y-L365F5CCXA8XriT-oAym6TXweo5_xrozYj1NSBP-1c73VTYAwbweK-QT76qM_RtVNBa3ZSZ2wBpdxNZBULAUk9T3kLaxX_cOksl9IgSmyc1iXeugiCXkrmYQztDIoA5tCuazxQoxC0IgQ19rXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/24850" target="_blank">📅 20:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24848">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وزیر جنگ آمریکا: حجم نفت که امروز از تنگه هرمز عبور می‌کند، بیشتر از حجم آن قبل از آغاز درگیری‌ها است
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/24848" target="_blank">📅 19:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24847">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نفتکش «اور وینست» هنگام ورود به تنگه هرمز، ظاهراً تحت اسکورت نیروی دریایی آمریکا بوده و نفتکش «آتیناگوراس» با پرچم یونانی نیز در حال خروج از عمان بوده و با ترانسپندر خاموش (AIS) وارد خلیج فارس شده است که گویا هر دو مورد هدف قرار گرفته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/24847" target="_blank">📅 18:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24846">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/24846" target="_blank">📅 18:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24845">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزارت خارجه آمریکا: نمی‌خواهیم درباره احتمال دست داشتن تهران در حادثه هواپیمای فلای‌دبی، پیش از پایان تحقیقات اظهارنظر کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/24845" target="_blank">📅 18:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24844">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تلگراف:
خاورمیانه در آستانه دور جدید درگیری نظامی گسترده است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/24844" target="_blank">📅 18:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24843">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آکسیوس درباره وزیر خزانه‌داری آمریکا: ما در جنگ خود با ایران به سیاست "دیوار آهنی" و تحریم‌ها و محاصره روی آورده‌ایم، سیاستی که واشنگتن قبلاً هرگز آن را اجرا نکرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/24843" target="_blank">📅 17:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24842">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ادعای الجزیره:
سوریه و ایران در حال نزدیک شدن به یکدیگر هستند!
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/24842" target="_blank">📅 17:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24841">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این دوستم تهیه کننده آخرین فیلم «رمبو» یعنی «آخرین خون» هست یه فیلم هالیودی از انقلاب بعد میسازیم اتاق جنگم توش باشه
😂
🙌🏾</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/24841" target="_blank">📅 17:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24840">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3bf49b39.mp4?token=AvFOgelvbtNJ_wa3aebKeTrRbLKlQojIslg3JRYkXlba-wsg9ghuPnxYT7e-zJKgHTgZ7d5MfDBn6kDBYTLzXiWfYCFFISDMNi6wpU1j0Fg7cGMOcTxfPIwh4SiZKSbKkrhl3d3xbSivrJjaKSt5nC7JY9jmdEqzr-h_R7Qps6iiL5l1KoRSOZE-vbONzSiH5M86TNYXpUPZCfupsUIefQb3lGNHl_ouP56q0w9yhdaXHZ6QGmKsXs3jbzNKbBSThPS_ohR0lh6Gf5Ua9-eL2u1HkmbmC835hQT8KmiAORCUXHb8eIAKESC3Crp4S85iLI03VQtDKb5-11Fu9UlV_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3bf49b39.mp4?token=AvFOgelvbtNJ_wa3aebKeTrRbLKlQojIslg3JRYkXlba-wsg9ghuPnxYT7e-zJKgHTgZ7d5MfDBn6kDBYTLzXiWfYCFFISDMNi6wpU1j0Fg7cGMOcTxfPIwh4SiZKSbKkrhl3d3xbSivrJjaKSt5nC7JY9jmdEqzr-h_R7Qps6iiL5l1KoRSOZE-vbONzSiH5M86TNYXpUPZCfupsUIefQb3lGNHl_ouP56q0w9yhdaXHZ6QGmKsXs3jbzNKbBSThPS_ohR0lh6Gf5Ua9-eL2u1HkmbmC835hQT8KmiAORCUXHb8eIAKESC3Crp4S85iLI03VQtDKb5-11Fu9UlV_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/24840" target="_blank">📅 17:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24839">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سلامتی همگی‌مخصوصا بهترین آرزو برای کنکوری ها
🥂
اگه خراب کردین هم که سال دیگه دانشگاه های بین‌المللی باز‌ میشه
😁
🫱🏼‍🫲🏽</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/24839" target="_blank">📅 17:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24838">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqOhGHXDwUf-oU8Q8UnhnhA04fU8fbkpf_ivFEkBXUb_7VVccOF_MSAJL_Sf1Cz5qtazhiBrY85FDMv4GoPFvD7QuBcYo6Irm27eWY61okSwGXh6Ua8j-sfV9NOtH9y6jGlFb2kjgM-lS-MSe5H4m2KHtFIAnKqZ1QgOaJG5lp7_-Ihnwe0MOK4qmNPy6yxZ56ji_ccquhB_H9MS4a9ToWrXt0RjeBQPV3eRP_8zvWL_Z3byOGA2g1XCpiAUy0BEOqxn41UqeychO8yeP6634Tuwijsp4Q42pbz9CypGu0fW2QLRFKWip8frcHk-W98JIPOfFayiEWxxi5mLBvgM8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : رژیم یه پهپاد زد سیریک ولی آمریکایی نیست @WarRoom
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/24838" target="_blank">📅 15:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24837">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دلار ۲۷۱،۰۰۰
یورو ۳۰۵،۰۰۰
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/24837" target="_blank">📅 15:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24836">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دیدبان اتاق جنگ : رژیم یه پهپاد زد سیریک ولی آمریکایی نیست
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/24836" target="_blank">📅 15:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24835">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2207daf642.mp4?token=Ys9oyfMoJ4F3VUOxT3QlyeT9MtKJPm1Ks5g8JOlaD_u4L9ZrCG1xt5TNpqWoxEPFlRnldzr0-mvg7RO4FAor8V1CU_2RLwyp8o8plB6_6PlBaEuYMDIO_Jxv3VP_nZQ-OBsP6bT9jRLMDDb85DafDSrd_8shNdOL0URp4jTg5oh1U7YUEDJB2dkyixAKVJeSj-dhD75HfocwSdhxeVX1Yst1yqCtu-dYmQ63q_O-W76EWCiBWNGK4Cjz4BZfKcilLyeLIFDZ5pkqu0vRyFgLwYJACfb4U2Wg8hQ-UFmhtplzb_xCBUj3VZ2mrA-pVHbuIZbWaJSWSlPouVainxwCglLUFHYqMXXHA0WB1JoJWow55BilIrUBzK65lePqWWqQ9PuSM7Epx22ra7aqCrRyysgu22T8KDhIvIiNM64Tf3ius6DH0WTNCat7aL75-L2UKplHucAhGNPXHsf9FVJn-fnU7Or-qnkyGhumuHf4Cc_rqInX9odoXKUQAbeyjsYxqh4u88F-MtQqkYlZUqreAXTFuf04obuWxxQHyzJMd_mNktH46IKqmScBz1083o9sETVCKCAIca2_eME7CkbTW6g_6SDRHAlq6k6ggPdWcflOn9WKEwoucP_r4MxmdP7mrk3QPjmM6QzLdXcje4PbG0LPDf20TTNy0kv7dqmRcRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2207daf642.mp4?token=Ys9oyfMoJ4F3VUOxT3QlyeT9MtKJPm1Ks5g8JOlaD_u4L9ZrCG1xt5TNpqWoxEPFlRnldzr0-mvg7RO4FAor8V1CU_2RLwyp8o8plB6_6PlBaEuYMDIO_Jxv3VP_nZQ-OBsP6bT9jRLMDDb85DafDSrd_8shNdOL0URp4jTg5oh1U7YUEDJB2dkyixAKVJeSj-dhD75HfocwSdhxeVX1Yst1yqCtu-dYmQ63q_O-W76EWCiBWNGK4Cjz4BZfKcilLyeLIFDZ5pkqu0vRyFgLwYJACfb4U2Wg8hQ-UFmhtplzb_xCBUj3VZ2mrA-pVHbuIZbWaJSWSlPouVainxwCglLUFHYqMXXHA0WB1JoJWow55BilIrUBzK65lePqWWqQ9PuSM7Epx22ra7aqCrRyysgu22T8KDhIvIiNM64Tf3ius6DH0WTNCat7aL75-L2UKplHucAhGNPXHsf9FVJn-fnU7Or-qnkyGhumuHf4Cc_rqInX9odoXKUQAbeyjsYxqh4u88F-MtQqkYlZUqreAXTFuf04obuWxxQHyzJMd_mNktH46IKqmScBz1083o9sETVCKCAIca2_eME7CkbTW6g_6SDRHAlq6k6ggPdWcflOn9WKEwoucP_r4MxmdP7mrk3QPjmM6QzLdXcje4PbG0LPDf20TTNy0kv7dqmRcRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا، اسکات بسنت: «ما از این درگیری با ایران عبور خواهیم کرد. فکر می‌کنم عرضه نفت بیشتر خواهد شد و قیمت نفت
به‌مراتب پایین‌تر خواهد آمد
. افزایش دستمزدها نیز ادامه خواهد داشت، چون ما شاهد
رونق دوباره بخش تولید و صنایع کارخانه‌ای
در آمریکا هستیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/24835" target="_blank">📅 15:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24834">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وال‌استریت ژورنال : نفت برنت در پایان معاملات هفته حدود ۱۰۲.۲۵ دلار و وست‌تگزاس اینترمدیت حدود ۹۱.۱۱ دلار در هر بشکه بسته شد. بازار همچنان تحت تأثیر حملات نفتکش‌ها، احتمال تشدید جنگ ایران و آمریکا و تصمیم گروه هفت برای آزادسازی ذخایر قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/24834" target="_blank">📅 15:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24833">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رویترز: ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» که در منطقه هرمز مستقر است، در وضعیت آماده‌باش قرار گرفته. رویترز در گزارشی از داخل ناو نوشت خدمه در جریان هشدارهای اضطراری خود را برای عملیات احتمالی آماده می‌کنند؛ این ناو حدود ۵ هزار نیرو دارد و مأموریت آن در منطقه زمان پایان مشخصی ندارد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/24833" target="_blank">📅 15:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24832">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دیگه عادی شده آژیر نداره
😂</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/24832" target="_blank">📅 15:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24831">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارش صدای انفجار قشم احتمالا از تنگه @WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/24831" target="_blank">📅 15:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24830">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارش صدای انفجار قشم احتمالا از تنگه
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/24830" target="_blank">📅 14:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24829">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">الجزیره: حمله هوایی هدفمند اسرائیل به یک آپارتمان مسکونی در غرب شهر غزه. @WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/24829" target="_blank">📅 13:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24828">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d07a84855.mp4?token=F0g9P5s-XIe4AMf9soh4c1b7ZnXr-tst-vUtyQ3AGPXs7uVIOD5Rs6WpHAxCW0fY-4PMp9wV_oDvPNlzYuqVs_Q8YZC8OgakKPyNU6LGR8xAYGXxxo3wuE5xyAQUjYgn1WsJhOAxk_YR1tGLrRHvQXlZW2gWMU9u3sYTMOyPt6Vjg0nljHqnc8S9SlrnKbXBoovp1sNtaVchC1dLEAJNCN3n4dJIMSLAOjYzpqmPoB1wXpvl1iqF0nwfqHDIDU0sOgBW4GpYz2aFOQyC0qvGQ7azezXYinrPsX432COoXNLvxm5TEYL3qxyLuPx7wmSngIMqDzjPIe4x7K2rKsLD46DyAsSMGVAviZ6wJ4QlS3Hze6PiK5NcZ-6r6KWkd4TVgmjK4peV1ZL2KPohenvp-2lCE1ui8JJyq_hAHhA714LXuqTss2iN7q0nv_rkFjAbssZwbaJg2R6QDDs1raJA7EiZus4XR6w2gJZ_WtnrEQBogTSPOj-6ZJNdhjp-jKXyZRMyXe7Qfj9jlqtzenCRk6dSl6sPgevMCtpqtdTfrMDnaGo1FwHGZ2AI_1LQvq5MtmW7tZRx4sUjIfq2oUWimRpfROztB1aykkDgtZ0avRKNZgRPNDNL_ds4WHfuvyKFKX4GV379VFcpxWAcRPO-BC2gAkZYWVl_ZJuIY1S3mgo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d07a84855.mp4?token=F0g9P5s-XIe4AMf9soh4c1b7ZnXr-tst-vUtyQ3AGPXs7uVIOD5Rs6WpHAxCW0fY-4PMp9wV_oDvPNlzYuqVs_Q8YZC8OgakKPyNU6LGR8xAYGXxxo3wuE5xyAQUjYgn1WsJhOAxk_YR1tGLrRHvQXlZW2gWMU9u3sYTMOyPt6Vjg0nljHqnc8S9SlrnKbXBoovp1sNtaVchC1dLEAJNCN3n4dJIMSLAOjYzpqmPoB1wXpvl1iqF0nwfqHDIDU0sOgBW4GpYz2aFOQyC0qvGQ7azezXYinrPsX432COoXNLvxm5TEYL3qxyLuPx7wmSngIMqDzjPIe4x7K2rKsLD46DyAsSMGVAviZ6wJ4QlS3Hze6PiK5NcZ-6r6KWkd4TVgmjK4peV1ZL2KPohenvp-2lCE1ui8JJyq_hAHhA714LXuqTss2iN7q0nv_rkFjAbssZwbaJg2R6QDDs1raJA7EiZus4XR6w2gJZ_WtnrEQBogTSPOj-6ZJNdhjp-jKXyZRMyXe7Qfj9jlqtzenCRk6dSl6sPgevMCtpqtdTfrMDnaGo1FwHGZ2AI_1LQvq5MtmW7tZRx4sUjIfq2oUWimRpfROztB1aykkDgtZ0avRKNZgRPNDNL_ds4WHfuvyKFKX4GV379VFcpxWAcRPO-BC2gAkZYWVl_ZJuIY1S3mgo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو به دیلی میل : «ائتلاف اسلام‌گراها و چپ‌گراها در حال مطرح کردن این اتهامات هستند؛ در حالی که این دو گروه اساساً باید مخالف یکدیگر باشند. چون اسلام‌گراها چه کار می‌کنند؟
همجنس‌گرایان را به دار می‌آویزند و زنان را از حقوقشان محروم می‌کنند.
آنها مردم خودشان را در غزه، لبنان و ایران می‌کشند و مخالفانشان را اعدام می‌کنند. اینها در نقطه مقابل دموکراسی‌ها قرار دارند.»
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/24828" target="_blank">📅 13:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24827">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دلار ۲۶۸،۰۰۰ تومان ( رکورد تاریخی )
@WarRoom
🚀</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/24827" target="_blank">📅 12:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24826">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تا آخرین لحظه حیات
از آن چیزی‌که تا به حال‌بودم تغییر نخواهم کرد! و اگر تا به اینجا با حمایت شما رسیده ایم  , مسلما به فروپاشی این رژیم هم خواهیم رسید.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/24826" target="_blank">📅 12:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24825">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خبرگزاری صداوسیما:
دقایقی پیش در مقابل ساختمان دادگستری شهرستان مهاباد تیراندازی رخ داد.
این حادثه پس از مشاجره لفظی میان چند زن و با ورود مردی مسلح به سلاح کمری و شلیک گلوله اتفاق افتاد. مرد مسلح به سمت زنان نزدیک شده و تیراندازی کرده است. تاکنون جزئیاتی درباره
تعداد مصدومان یا تلفات احتمالی، وضعیت افراد حاضر، هویت تیرانداز و انگیزه او
منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/24825" target="_blank">📅 12:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24824">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rds5fMsdmv_FfaA4aV-eP6K1dFSocdi2Kux7Xqo9r0xZ4xms5qg4nWfZybguzAe0XzhDfmpTCtDyiWmcKaTLoypNO19yABmhTcI_GL6nKEYabSOy069PgnV0vv9yW5FbXdD95ZEhS84AP_niNNZ6n7q6eoigs0jbEMwGOzALoZrM6Tu388D_ifMbmV3YsOcZMmEgrpTvkjyFItrlxJKSMzqPBudwPQqc2ORnVZGXOS7WfShg5eiP5jygX-r2gXalegq3u6tD5epEdfQzVM2VCK1QUw3yDktujLjuBvpl16VftCeZVbgwtwTJKIMSInuGSkJH5EST9jKSP3gTLfB9AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نابودی پارک جنگلی چیتگر در سه دهه
این پارک در دهه چهل و در دوره پهلوی ساخته شده بود و ۶۰ سال قدمت دارد
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/24824" target="_blank">📅 11:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24823">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خبرنگار کانال ۱۲ : گزارشها حاکی از این است که کمک‌خلبان، شهروند عمان، با یک تبر سوار هواپیما شده بود. @WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/24823" target="_blank">📅 10:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24822">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آکسیوس به نقل از سه مقام آمریکایی: مقام‌های ارشد دولت آمریکا در کمپ دیوید برای بررسی اقدامات بعدی درباره ایران و انصارالله تشکیل جلسه دادند. یک مقام آمریکایی گفت در این نشست «تصمیماتی گرفته شد یا دست‌کم موضوعات به‌طور جدی مورد بحث قرار گرفتند». جی‌دی ونس ریاست…</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/24822" target="_blank">📅 10:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24821">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfEZ-B_8ZVsbPkEdcfff9Y_uLT9dq-phSSItIXnwWE78iXPJCvSy2_EFIR_MLLYTzgcfSg9ln0CSW8RDcxJrrGbuaepfx408ilkszE1ZLFaFUsQQoFb60GqAm7J9dmf2HeX3uYTjqksvvi0k4T7ybdWOmTmW4mKvXSO5KtPZFnf6v7byASb5v48WcybzM-aeJ1GZ3SD7NmfK-J_mgN-YDdNvbgXVJ4yGADfa3CCMBnHsu98lQ9R7vsBZd02u4mDszj6_1wN7hmIR8dhdAHaWr7sIrqYVZkKAjkEQ_10uyVGgdiw7ZEx408y462PTc78Dvir1wS-UAa7mEYSTdKWAag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه افغان نیروی قدس سپاه پاسداران از کشته‌شدن یکی از نیروهای تیپ فاطمیون خبر داد. او در اثر انفجار بمب کنار جاده‌ای که در زاهدان، استان سیستان و بلوچستان، در جنوب‌شرق ایران کار گذاشته شده بود به هلاکت رسید؛ این حمله احتمالاً توسط گروه‌های بلوچ انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/24821" target="_blank">📅 09:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24820">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80f878b1ca.mp4?token=nV9qPCT0zKNIjCpzLY2-ErRle81Lj4gqFGP3UhwUutnAbosMnwYYHLwB9DcOW4lw5yeGPuDmlmiswyAHrA3dGxubrk8x0ByYOFEgiMNRKa8B6dbXtTPWhRMA9Yprf2HGbQXoyNs6bGdxaA55PZtIm7Ibwtv8a-YsioFYdd6Bgch-lsa2xsVqs-tId0rlkaRu-xm1kxZs0PHHk3fznJuOO01tsEUvcWUzzzeh8kI8ybKdUPq27KHq9FEl5LwRyPNU9gvUKYZHNzuTrb6qikFqzvOZlSnxyDHnt6v7B8JcfDUZW5xjlHfuckTCHLgZPhIqke2JsZUxCPF7cMRgBF8NVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80f878b1ca.mp4?token=nV9qPCT0zKNIjCpzLY2-ErRle81Lj4gqFGP3UhwUutnAbosMnwYYHLwB9DcOW4lw5yeGPuDmlmiswyAHrA3dGxubrk8x0ByYOFEgiMNRKa8B6dbXtTPWhRMA9Yprf2HGbQXoyNs6bGdxaA55PZtIm7Ibwtv8a-YsioFYdd6Bgch-lsa2xsVqs-tId0rlkaRu-xm1kxZs0PHHk3fznJuOO01tsEUvcWUzzzeh8kI8ybKdUPq27KHq9FEl5LwRyPNU9gvUKYZHNzuTrb6qikFqzvOZlSnxyDHnt6v7B8JcfDUZW5xjlHfuckTCHLgZPhIqke2JsZUxCPF7cMRgBF8NVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «من گروهی از مردم را دیدم که اسمشان «همجنس‌گرایان برای فلسطین» است. یک روز آنها را بفرستیم تا بروند مذاکره کنند. دیگر هیچ‌وقت آنها را نخواهید دید. آنها کارهایی انجام می‌دهند که باورکردنی نیست.»
@WarRoom
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/24820" target="_blank">📅 09:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24819">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzE5Bq9A2QG3Qw7_FhY-nTmbKjIUPzton9HoNbW84Kr7voU6LHp06ngONcRCI3eya4sr8QFXuWo0ukFkmNggLKw_SufAbw2yETh802P-Ia2x4IjOYzco8BmkI7Slqv70XghB42gPJVoCxaYxs0Bat39bPfEJj8h6rybdac7EWESND1vIO_iZMTwsz_eIh2DbXw0Btbtsf3zECXcQjOtVrm3ORbbhFyxjPY-R1WkvMOy4v4lqbwZFNvE_gBH24MdCodxaC4ElxQHAjZW05-AbDM_Idr-9D1QHr7lsvHxih9wbFVq_CccQVnWPs5T9L96FOv121MXcYBTkhfFgHS-bEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی اعلام کرد حکم
سیاوش جمشیدی
که در جریان اعتراضات دی ماه ۱۴۰۴ بازداشت شده بود به اتهام استفاده از اسلحه در‌اعتراضات شهرکرد ، بامداد امروز ۱۱ مهر اجرا شد.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/24819" target="_blank">📅 09:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24818">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آکسیوس به نقل از سه مقام آمریکایی: مقام‌های ارشد دولت آمریکا در
کمپ دیوید
برای بررسی اقدامات بعدی درباره
ایران و انصارالله
تشکیل جلسه دادند. یک مقام آمریکایی گفت در این نشست «تصمیماتی گرفته شد یا دست‌کم موضوعات به‌طور جدی مورد بحث قرار گرفتند».
جی‌دی ونس
ریاست جلسه را بر عهده داشت و
مارکو روبیو، پیت هگست، ژنرال دن کین، جان رتکلیف و استیو ویتکاف
نیز حضور داشتند.
آخرین بار که چنین نشست مشاوره‌ای برگزار شد، ژوئن ۲۰۲۵ و پیش از آغاز جنگ ۱۲روزه اسرائیل بود.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/24818" target="_blank">📅 09:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24817">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پدافند غرب تهران بدجور زد !
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/24817" target="_blank">📅 04:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24816">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شنیده شدن صدای تیراندازی یا پدافند از شهریار و اندیشه کرج
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/24816" target="_blank">📅 04:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24815">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/24815" target="_blank">📅 04:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24814">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f241181503.mp4?token=Glxuey0c5aUGnNTsfxbkfXnoECK6ClCCxlmhgUyqrXqWKLXce-_HkJ7rdph0I9iPhslEeTOG4h0US28c3mthxyW0DuFXApKAURYHD4Wpz4ImCH122lGVUJ1x27D5lZaxyRpnNAyGN0dqnTDE2kZae8f73LbuECiSUJjTGyatSVokLAz1xPZ8nAOBJXQm4ztpf10kyX5YQajgbEo9JWi6lek5AVc8SrCemAedVWXLAv1zL5pcZVnGqJspKJq_f3teaUlDeS8KacYo2kna95eHIt7P3rRG-6k0e5qaoyDpeh-xW9RuAPDcc_s8JImGOClbSO9hr_NORV-e5yvK7vv-7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f241181503.mp4?token=Glxuey0c5aUGnNTsfxbkfXnoECK6ClCCxlmhgUyqrXqWKLXce-_HkJ7rdph0I9iPhslEeTOG4h0US28c3mthxyW0DuFXApKAURYHD4Wpz4ImCH122lGVUJ1x27D5lZaxyRpnNAyGN0dqnTDE2kZae8f73LbuECiSUJjTGyatSVokLAz1xPZ8nAOBJXQm4ztpf10kyX5YQajgbEo9JWi6lek5AVc8SrCemAedVWXLAv1zL5pcZVnGqJspKJq_f3teaUlDeS8KacYo2kna95eHIt7P3rRG-6k0e5qaoyDpeh-xW9RuAPDcc_s8JImGOClbSO9hr_NORV-e5yvK7vv-7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «یکی از بدبختی‌هایی که داریم ، کسی نیست که با باهاش مذاکره کنیم. هیچ‌کس نمی‌خواهد رئیس‌جمهور باشه ، جدی‌ میگم : «الان با چه کسی در ایران صحبت کنم؟» تق‌تق! کسی خانه نیست.»
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/24814" target="_blank">📅 03:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24813">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8addbc83.mp4?token=i78x1Cnm54Ag3nNDvpmU3V0UA9Pc7IE60w8CGfIXcb3aEZKViJWWyBU5sR0T0LSjb-0izaUVG2NY1C6ll2btJ-gtpxzDJ45bgmNwqSGIjDUf6v6ux8a6HbDQqv4dOAb97EQZzQiwdqBBqNpOECZB9IJzHwJvX9g5pXaLv5k7jOZOAsgMDKcUEc1zX1qGnbghLV04MQPjfz5SAMsDVLRzHNTQa3OOEAAXONOG_RTHNHFbB6orJsFleEN9A2rFLqMD9NtkQ3wI-fz0l7p1gZckrQAm7uQ2LO1JE7HntiGS-sCaRGawFEQDOe2BfIzorcRgQDkT3anqUEqDivraUVic1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8addbc83.mp4?token=i78x1Cnm54Ag3nNDvpmU3V0UA9Pc7IE60w8CGfIXcb3aEZKViJWWyBU5sR0T0LSjb-0izaUVG2NY1C6ll2btJ-gtpxzDJ45bgmNwqSGIjDUf6v6ux8a6HbDQqv4dOAb97EQZzQiwdqBBqNpOECZB9IJzHwJvX9g5pXaLv5k7jOZOAsgMDKcUEc1zX1qGnbghLV04MQPjfz5SAMsDVLRzHNTQa3OOEAAXONOG_RTHNHFbB6orJsFleEN9A2rFLqMD9NtkQ3wI-fz0l7p1gZckrQAm7uQ2LO1JE7HntiGS-sCaRGawFEQDOe2BfIzorcRgQDkT3anqUEqDivraUVic1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «ایران برای ریاست‌جمهوری شورا برگزار کرد، اما هیچ‌کس در آن شرکت نکرد. همه می‌گفتند: «ما نمی خواهیم»
@WarRoom
یاشار : فکر میکنم منظورش به همون خبر استعفای پزشکیانه و بعد کسی حاضر نشده کاندید بشه. برای همین با استعفاش موافقت نشد.</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/24813" target="_blank">📅 03:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24812">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f8e97b36.mp4?token=kwbSSV1RJd4wrEt-aHPUP33z9S2_gk6zGpaLVzNiaOzMOS-n1bv_wxep5XGscpuE6-GzF5GrEMQOCe9BML4KXZuYH85T2pgwvckBiGlSGETD3wnFO8C4Mou9PHIrYjO2tPrnJq7SbjfYV5sa0CRKImzoDDtJ0MDKWNwlKnuKOqsTrSwRZkxthDRQUEN4C05E3pJZWOQHwwAJJE-EeDQawcTl-AVbXf1TGXptmr4TLv5JQAXnfG-s0jbbXTQfLUmUhdPmR6Z_5uwqOUOjwxAZLM1uPPOAM9X8ke1Gym5ZEN1vDi6IOdASlpako7_ea1Q4ZoVdib_6_TuOvVcrmWviTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f8e97b36.mp4?token=kwbSSV1RJd4wrEt-aHPUP33z9S2_gk6zGpaLVzNiaOzMOS-n1bv_wxep5XGscpuE6-GzF5GrEMQOCe9BML4KXZuYH85T2pgwvckBiGlSGETD3wnFO8C4Mou9PHIrYjO2tPrnJq7SbjfYV5sa0CRKImzoDDtJ0MDKWNwlKnuKOqsTrSwRZkxthDRQUEN4C05E3pJZWOQHwwAJJE-EeDQawcTl-AVbXf1TGXptmr4TLv5JQAXnfG-s0jbbXTQfLUmUhdPmR6Z_5uwqOUOjwxAZLM1uPPOAM9X8ke1Gym5ZEN1vDi6IOdASlpako7_ea1Q4ZoVdib_6_TuOvVcrmWviTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «اگر دروغ بگویم، به من پینوکیو می‌گویند. من دروغ نمی‌گویم.»
@WarRoom
یاشار : خیلی خوبه این بشر
😂</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/24812" target="_blank">📅 03:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24811">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f2bfed07.mp4?token=BnmyqNmXkjyoK5qHrHA1D9-YoTReHb5GK7GH6mhcZVx_DgyT2IzYsTQb7NbXwXhQweIlktY3Qinua-lNq1HNM9ZL-ETh0Tbtt-nrHqdxn98kTBxI9G6t8Ycr8zmNrVctn4Eb__cvIjuLNSTpQYF40JPXbf0SoX9wOn1-J4jENYtIGfZqiztWn1cpZ8loYdUXugHeZ40UkyLCewiZ8aG5r7KrjtaCyo5Ax5r61l8Y2l9jh0K_ctbb9K8bx67DKMabAA1Zjxyx7crOvbKwl7u-xNHBws3o_1YQWS2TSfuttTFixxm3E2_nssCFzILc18kMNG8mAL4Q_X2BvUF5ps2UIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f2bfed07.mp4?token=BnmyqNmXkjyoK5qHrHA1D9-YoTReHb5GK7GH6mhcZVx_DgyT2IzYsTQb7NbXwXhQweIlktY3Qinua-lNq1HNM9ZL-ETh0Tbtt-nrHqdxn98kTBxI9G6t8Ycr8zmNrVctn4Eb__cvIjuLNSTpQYF40JPXbf0SoX9wOn1-J4jENYtIGfZqiztWn1cpZ8loYdUXugHeZ40UkyLCewiZ8aG5r7KrjtaCyo5Ax5r61l8Y2l9jh0K_ctbb9K8bx67DKMabAA1Zjxyx7crOvbKwl7u-xNHBws3o_1YQWS2TSfuttTFixxm3E2_nssCFzILc18kMNG8mAL4Q_X2BvUF5ps2UIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «احمق! همه‌شان فکر می‌کنند کلمه Dumb حرف B ندارد.» (ترامپ با بازی زبانی به تلفظ واژه Dumb اشاره می‌کند؛ حرف B در نوشتار وجود دارد، اما در تلفظ خوانده نمی‌شود.)
@WarRoom
یاشار: همون‌جور که می‌بینی ترامپ هم اونور دنیا با این احمق‌ها درگیره. واقعاً احمق زیاده.</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/24811" target="_blank">📅 03:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24810">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2bX5ZU_fuYpD18YjNCXxAkB7O5j6-cjwTc1WyUaYhQ6AqWOQC1RymdHyBk7Im6RzCGHJbGirDSluWcTFw0Q70ACvDv8bi9N4UXrVKfQpYBJXphJLkKRWa4obNsRpdKyNdalOZXO7QId7QQ1JGq48xo3xpEMpJUAJP0khF96iPW_ZJGOKQu7cUMu7uGvkhuT3s8Y5K1V1BibOqT3C5Ryrw36Rgolmcw-l55mRzq6w1qU8Qad5O4z0rs72iApdGJBFHhsWjiXjRaojjMV-jZpi2A_VgbfXqPiAoZw9FO9wtAaYx4yZE4HEPVNnAesT89mJZqUOOw3Sovj2Ystn18W8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش حامل نفت خام در حدود ۴ مایل دریایی شرق عمان، هدف اصابت یک پرتابه ناشناس قرار گرفت.
تمام خدمه در سلامت هستند
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/24810" target="_blank">📅 03:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24809">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24809" target="_blank">📅 03:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24808">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24808" target="_blank">📅 03:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24807">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الجزیره: حمله هوایی هدفمند اسرائیل به یک آپارتمان مسکونی در غرب شهر غزه.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/24807" target="_blank">📅 02:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24806">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/24806" target="_blank">📅 02:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24805">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/24805" target="_blank">📅 01:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24804">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/24804" target="_blank">📅 01:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24803" target="_blank">📅 01:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24802">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/24802" target="_blank">📅 01:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24801">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کره شمالی موشک بالستیک پرتاب کرد. پدافند ژاپن در حال رصد تحرکات است.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24801" target="_blank">📅 01:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24800">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9IOhG8rIsUWeUCL5aA84RoQHHpo4UXv_QOVz2mgjM1IMVisS4zhsrAtFdLC24cPletIyi8OsAxvWQAXcs-U6SlI9Q6iAiGWo2UM9p6EQfTn00g1_pDZo13LymhZo4BIVqlhGOfZdLOLBblnuMEryXLTB5n7pILgR1xw9ER5cW6xBgWj3xxJEAc26Ho5KARoRIKuZWma6YeNS8Z_Vo92avqHoTREYliymEld8inNo2i5CwC8o540XKzjFEaS3RybxpEP_qjfZjxUZqz6B11zqokrZwd1Wk__iaHYqH-FFPTZMumfaCt55KLszqnoh6TwdoRB4ZPYjPAzzviTs3A2zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع العربیه: کمک‌خلبان عمانی مرتبط با حادثه پرواز فلای‌دبی «همام الهمامی» نام دارد. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/24800" target="_blank">📅 01:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">منابع العربیه
: کمک‌خلبان عمانی مرتبط با حادثه پرواز فلای‌دبی «همام الهمامی» نام دارد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/24799" target="_blank">📅 01:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24798">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نظر مارک بر اینه تو این ۲۴ ساعت آینده میزنه انگار</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/24798" target="_blank">📅 01:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دلار داره موشکی‌میره بالا
🚀</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/24797" target="_blank">📅 01:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24796">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">چنتا کانفیگ فروش دایرکت دادن برای تبلیغات
😂
😂
میگین به جایی ‌وصلن ؟</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/24796" target="_blank">📅 01:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24795">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">چنتا کانفیگ فروش دایرکت دادن برای تبلیغات
😂
😂
میگین به جایی ‌وصلن ؟</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/24795" target="_blank">📅 00:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24794">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وال‌استریت ژورنال:
کمک‌خلبان عمانی پرواز FZ1073 فلای‌دبی که متهم است به خلبان هواپیما چاقو زده و باعث سقوط شدید هواپیما شده،
قبلاً در عمان از پرواز کردن منع شده بود
؛ دلیل این تصمیم، نگرانی‌ها درباره گرایش او به دیدگاه‌های افراطی عنوان شده است. با وجود این ممنوعیت، او بعداً توسط فلای‌دبی استخدام شد و در مسیر حساس
امارات به اسرائیل
پرواز می‌کرد. هنوز مشخص نیست عمان این نگرانی‌ها را با کشورهای دیگر یا شرکت‌های هواپیمایی در میان گذاشته بود یا نه.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/24794" target="_blank">📅 00:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24793">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خبرنگار: گام بعدی شما در قبال ایران چیست؟ ترامپ: خب، اگر به شما بگویم، یک خبر بزرگ خواهید داشت، درست است؟ اما خودتان خواهید دید؛ همه‌چیز خیلی خوب پیش می‌رود. ایران وضعیت خوبی ندارد. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/24793" target="_blank">📅 23:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24792">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4ee0bbd03.mp4?token=ih9tHMMUNUsp1MfjwfJAq705eXo0ApuwoLtrATm4BVJ-zaue6TDtuFcuPJSj2U7OrT7QcYkH3AYg57HGrdH8P1qQY1viTBmbjNNRnJv4g77xa6CpdQGZMvd30a6-bKmZ8CfG3F46EH8I6ToPWEdxY-6TlORhvo09CJYj0_V7BPx2pIMfvy_Rfy6k4mXrFXhIUdRBsMi2DbdwVbX0BavilwDjcF7Hp4E4kT2ec-gw45gOnqrE7KPSv11AvyYqT-yK_bnOZHg5EmbJLb-C-gfhB6mha-tR0wxwZQ9D-oGjioMxNk_Mb6EqCUPqHTHjpAub4TfIuwCiMQ-0Yl21OHE1sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4ee0bbd03.mp4?token=ih9tHMMUNUsp1MfjwfJAq705eXo0ApuwoLtrATm4BVJ-zaue6TDtuFcuPJSj2U7OrT7QcYkH3AYg57HGrdH8P1qQY1viTBmbjNNRnJv4g77xa6CpdQGZMvd30a6-bKmZ8CfG3F46EH8I6ToPWEdxY-6TlORhvo09CJYj0_V7BPx2pIMfvy_Rfy6k4mXrFXhIUdRBsMi2DbdwVbX0BavilwDjcF7Hp4E4kT2ec-gw45gOnqrE7KPSv11AvyYqT-yK_bnOZHg5EmbJLb-C-gfhB6mha-tR0wxwZQ9D-oGjioMxNk_Mb6EqCUPqHTHjpAub4TfIuwCiMQ-0Yl21OHE1sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
گام بعدی شما در قبال ایران چیست؟
ترامپ:
خب، اگر به شما بگویم، یک خبر بزرگ خواهید داشت، درست است؟ اما خودتان خواهید دید؛
همه‌چیز خیلی خوب پیش می‌رود. ایران وضعیت خوبی ندارد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/24792" target="_blank">📅 23:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24791">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پلیس ضدتروریسم بریتانیا :‌
امروز
دو شهروند ایرانی،
سلام احمدیان ۳۶ ساله و رحمان صالحی ۳۴ ساله
، به اتهام آماده‌سازی برای انجام یک عملیات تروریستی علیه جامعه یهودیان در منچستر متهم شدند. این دو نفر
۲۹ شهریور
در منچستر بازداشت شده بودند. پلیس می‌گوید آنها با یک
طرف امنیتی ثالث خارج از بریتانیا که احتمال می‌رود در ایران باشد
در ارتباط بوده‌اند و تحقیقات درباره این پرونده ادامه دارد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/24791" target="_blank">📅 23:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24790">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">جروزالم پست: ایهود باراک، نخست‌وزیر پیشین اسرائیل، مدعی شد نتانیاهو ممکن است برای به‌تعویق انداختن انتخابات، زمینه یک جنگ جدید را فراهم کند. باراک گفت اگر شرایط سیاسی برای نتانیاهو نامساعد باشد، آغاز یک درگیری تازه می‌تواند برگزاری انتخابات را به تأخیر بیندازد.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/24790" target="_blank">📅 23:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزارت خارجه آمریکا: در بیانیه‌ای مشترک به مناسبت سالگرد اجرای تحریم‌های «مکانیسم ماشه»، آمریکا و چند کشور دیگر بار دیگر بر تعهد خود برای اجرای محدودیت‌های سازمان ملل که از طریق این سازوکار علیه ایران بازگردانده شده‌اند، تأکید کردند.
این کشورها همچنین از ایران خواستند به تعهدات خود در زمینه منع اشاعه پایبند باشد، با آژانس بین‌المللی انرژی اتمی همکاری کامل داشته باشد و نگرانی‌های بین‌المللی درباره برنامه‌های هسته‌ای و موشک‌های بالستیک خود را برطرف کند.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/24789" target="_blank">📅 23:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24788" target="_blank">📅 23:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/24787" target="_blank">📅 22:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24786">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/24786" target="_blank">📅 22:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24785">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گویا معین هم اعلام کرد بر میگرده بزودی @WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/24785" target="_blank">📅 22:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24784">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وزارت خارجه بریتانیا: آمریکا، انگلیس، فرانسه و آلمان در بیانیه‌ای مشترک اعلام میکنند که متعهد به جلوگیری از تأمین هرگونه مواد، تجهیزات و فناوری برای ایران هستند که بتواند در فعالیت‌های هسته‌ای مورد استفاده قرار گیرد. این چهار کشور همچنین بر ضرورت همکاری کامل ایران با آژانس بین‌المللی انرژی اتمی و اجرای تعهدات پادمانی تأکید کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/24784" target="_blank">📅 22:36 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
