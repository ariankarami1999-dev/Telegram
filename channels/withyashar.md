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
<img src="https://cdn4.telesco.pe/file/hgceMWAT122iPwAdIOtCRGVtVs7losBDqiqgP5xPJ8YosinKnAHbZEbbnwvSZX8_4YP8CksmxwuM9arcAYgHRYdyqxsgtpJrMK6YNf81evqxdCNsmhfj-e4uXZnqHc8UNIFqy7hsOQgaAFAK79xmNIwWGSRVCBYDzwJdwB7e7xL3HQDItrN3w_cmqqApcpJ1BqhrWbaQ81yG6R2TtikLvQXYxK1t98y_iYf6UZdqTNKsu6TSOUi_OT3KjC6cRABUlIGluyMgza3pbe3TUX_MZIAFYl2swIiHVetGRCXXbRl5Ne8J1RZMez7Ha9Ki19YQCgH4GzrifqCSQsXKTHA3fQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 488K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 05:04:34</div>
<hr>

<div class="tg-post" id="msg-25225">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پرتاب موشک از بندر لنگه
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/withyashar/25225" target="_blank">📅 01:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25223">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3JVYPTUSN_H_Bh9n23VlYkp5jsqhawBno4J-aV_xx1dRSaxOQRXojg8o4iSmzRhWoBICWktyJwZuBRkDd-DsdqSLchOHv1O9lEDHB7DcLi3AxR-Y0JPbP0aEnWDasW-igRU75Iqdj11MTa7eTxy-fIhl76Oll3zwXNZvsydy0xfZiMk2qSHnkBF7Q0eHkcqhM523fI9WrIyK1KRyPb2HVUEpHZPcTPX0S5gm3-ENNQaNcvydKZiBbauu5_D4fHzPJ9KZyV6Jclp05AAfUCUL8OlHTgZ-15sUga7X4tcCp1Tepx5l3wybc3t8AKe_hMUC_Xyx-9C3pNOzXkZxjN-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2a3b0dbfd.mp4?token=bnIboZLKyeOiYKzywskIqLrIvSxpAMkgwuizGP46AuZfkMUOdi81EawZ4K5Acor-jzyNMO9ym0hbCCOCJ1YCNOIUYWeGUpwop5BiYLBFIKjoHF5dU-Q3f7XEYeRQ9O7IQjZgN2nrFE1wBXsJF5VyqN25F9TAPK2s440YFDZiv0Oy7mJOO0RWc0ut9Y1Xm7s4LbCha6rgHIYgjtMWYH5o85yAoU97z-Zj-wOwqN_0s4ewNuUu3ESRvMuvKvge5HupB6bhamB06F_BCACBl9w8_opAq9SAtb0NMiDVxHFWPVwRg5amdp2xzam-qGXDlgNt-myDnwAF1B1PKdF9gIx5Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2a3b0dbfd.mp4?token=bnIboZLKyeOiYKzywskIqLrIvSxpAMkgwuizGP46AuZfkMUOdi81EawZ4K5Acor-jzyNMO9ym0hbCCOCJ1YCNOIUYWeGUpwop5BiYLBFIKjoHF5dU-Q3f7XEYeRQ9O7IQjZgN2nrFE1wBXsJF5VyqN25F9TAPK2s440YFDZiv0Oy7mJOO0RWc0ut9Y1Xm7s4LbCha6rgHIYgjtMWYH5o85yAoU97z-Zj-wOwqN_0s4ewNuUu3ESRvMuvKvge5HupB6bhamB06F_BCACBl9w8_opAq9SAtb0NMiDVxHFWPVwRg5amdp2xzam-qGXDlgNt-myDnwAF1B1PKdF9gIx5Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی جدید از نوع استتار تکاوران نیروی زمینی من را یاد شخصیت «گریفین» در فیلم شاهکار «مرد نامرئی ۱۹۳۳» انداخت. البته برای دوستان جدید شخصیت گریفین به صورت فقط یک «عینک» در انیمیشن «هتل ترانسیلوانیا» نیز حضور دارد.
😂
@WarRoom</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/25223" target="_blank">📅 01:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25222">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نیویورک‌تایمز گزارش داد پنتاگون پس از نشست محرمانه دونالد ترامپ و تیم امنیت ملی آمریکا در کمپ دیوید، گزینه‌های تازه‌ای برای ازسرگیری حملات گسترده به ایران تدوین می‌کند. یکی از سناریوهای مطرح‌شده،
انجام حملات طی یک دوره سه‌روزه
از حملات شدید علیه ایران است که موشک‌ها، پهپادها، زیرساخت‌های انرژی، مراکز فرماندهی سپاه پاسداران و تاسیسات نظامی را هدف قرار می‌دهد
@WarRoom</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/25222" target="_blank">📅 00:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25221">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">روزنامه جروزالم پست گزارش داد که هدف از ترور
علیرضا تنگسیری، فرمانده نیروی دریایی سپاه، جلوگیری از رسیدن او به فرماندهی کل سپاه پاسداران
بود. به نوشته این روزنامه، مقام‌های اسرائیلی او را فرمانده‌ای توانمند و خلاق می‌دانستند که در صورت رسیدن به رأس سپاه، می‌توانست تهدیدی جدی‌تر از احمد وحیدی باشد. این گزارش همچنین مدعی شد برد کوپر، فرمانده سنتکام، حدود ۱۹ مارس در تماسی محرمانه از رئیس ستاد ارتش اسرائیل خواسته بود تنگسیری را هدف قرار دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/25221" target="_blank">📅 00:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25220">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ادعای فارس
: نفتکش‌های متخلف روی مین‌های تنگۀ هرمز منفجر شدند
دقایقی پیش چند انفجار سنگین در معبر جنوبی تنگه هرمز رخ داد که ناشی از اصابت نفتکش‌های متخلف با مین‌های منتشره در منطقه از دریا می‌باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/25220" target="_blank">📅 23:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25219">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فارس: سرگرد مهدی جمشیدی، از کارکنان نیروی انتظامی، دقایقی پیش درپی تیراندازی افراد مسلح ناشناس در مرکز شهر فاریاب استان کرمان ،کشته شد.
@WarRoom</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/25219" target="_blank">📅 23:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25218">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خبرنگار المانیتور , جرد سزوبا: سناتور کریس مورفی، پس از دیدار جداگانه با
شیخ تمیم بن حمد آل‌ثانی، امیر قطر
و علی الثوادی، دیپلمات قطری و یکی از چهره‌های اصلی هماهنگ‌کننده میانجی‌گری میان آمریکا و ایران، گفت توافقی برای پایان دادن به جنگ با ایران
در آینده نزدیک بعید به نظر می‌رسد.
مورفی در سفر خود به قطر درباره تلاش‌های دیپلماتیک برای پایان جنگ با مقام‌های قطری گفت‌وگو کرد و تأکید کرد قطر همچنان نقش مهمی در میانجی‌گری میان واشنگتن و تهران دارد. این دیدارها در حالی انجام شد که مذاکرات آمریکا و ایران از طریق قطر بار دیگر با بن‌بست مواجه شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/25218" target="_blank">📅 23:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25217">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خبرنگار اکسیوس: فلش‌بک: در ژوئن ۲۰۲۵، پیش از عملیات «چکش نیمه‌شب»، کاخ سفید اعلام کرد ترامپ «ظرف دو هفته» تصمیم خواهد گرفت که آیا آمریکا وارد جنگ اسرائیل علیه ایران شود یا نه.اما زمانی که این اظهارات را مطرح می‌کرد، در واقع از قبل تصمیمش برای حمله به تأسیسات هسته‌ای ایران را گرفته بود.
در ۲۷ فوریه، کمتر از ۲۴ ساعت پیش از آغاز جنگ اسرائیل و آمریکا علیه ایران، ترامپ مدعی شد که هنوز درباره ورود به جنگ تصمیمی نگرفته است.
اما در واقع، ترامپ از قبل مجوز انجام حملات را صادر کرده بود
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/25217" target="_blank">📅 23:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25214">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30b8f646ae.mp4?token=ANGehQ6GwaxP30565ykTuzPOX97iE4nk_BXHVlTro2ZZqZcHAwYy0cwbZWJnhmshD8yA_SCWP_1p8t0vpj_vrKqM83uru3wYhLk3N36niMhYSuIvHIc5KmmxGl6ZS7Y3__B47VkGpG-e0HQ4K2WzEZVuXZlK8Zgm2XcWse1YSRiQw5AhvT3UWcDNfsnw_Nt_rljLxScnZRcH0UXrwFG6koBI5fBS_82M3BR8n-YZe6Q742seijXTb15_8GPn2hystD58hKxRZw4UPgjJKoOjEnOOokNwNHKu21ugt7Jy6zZJfX-7uABdwtZvkaVwWOT9ea72uZZabPiUj3IXsyZAxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30b8f646ae.mp4?token=ANGehQ6GwaxP30565ykTuzPOX97iE4nk_BXHVlTro2ZZqZcHAwYy0cwbZWJnhmshD8yA_SCWP_1p8t0vpj_vrKqM83uru3wYhLk3N36niMhYSuIvHIc5KmmxGl6ZS7Y3__B47VkGpG-e0HQ4K2WzEZVuXZlK8Zgm2XcWse1YSRiQw5AhvT3UWcDNfsnw_Nt_rljLxScnZRcH0UXrwFG6koBI5fBS_82M3BR8n-YZe6Q742seijXTb15_8GPn2hystD58hKxRZw4UPgjJKoOjEnOOokNwNHKu21ugt7Jy6zZJfX-7uABdwtZvkaVwWOT9ea72uZZabPiUj3IXsyZAxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه با پهپاد‌های موتور گازی‌ آبیش به منطقه ریزگری اربیل، کردستان عراق حمله کرد
@WarRoom</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/25214" target="_blank">📅 23:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25213">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پارلمان اروپا امروز، ۸ اکتبر، قطعنامه جدیدی درباره وضعیت حقوق بشر در ایران تصویب کرد. این قطعنامه با
۵۴۱ رأی موافق، ۱۱ رأی مخالف و ۲۵ رأی ممتنع
به تصویب رسید و در آن
خشونت علیه غیرنظامیان، افزایش اعدام‌ها، سرکوب معترضان، فعالان حقوق بشر و روزنامه‌نگاران و استفاده از اعترافات تحت شکنجه
محکوم شده است. پارلمان اروپا همچنین خواستار لغو احکام اعدام ترانه رحیمی و لیلا ابوالحسنی و لغو مجازات اعدام در ایران شد و سرکوب اقلیت‌های قومی و مذهبی و سرکوب فرامرزی جمهوری اسلامی را محکوم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/25213" target="_blank">📅 23:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25212">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaTGMGMTFSIDkUmuiLLsiawWXkQAe8Ih7L8e4UHZ2Sl_EujpiS7nI9_pI5URxO6zA4rZLiT9wFgVdN5epCoXZktvLXneaiHWyI2YEYAPQMauylR6Q2t7aYJk56PW_0kDWlPLk6t_ng1R3wJsLjjM7WXo0tzTO-Te36Qeam0koEVP9PheNAViZlFmRk0TCXF2ZlPlAV7AA6BvXz9ySUuSvMbnjgnvlHVyUuNzQ_KElNDN1ptSmAJQAWcruQAACjf30SfJIJVL_YsgvX-6KFMybDR54OMd_olpnsV46h-3vYG6KUW9KxgOzu4CndTOYwnMsbnzO-YA5cOoysn2avFByg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ در‌تروث : رسانه‌های جعلی تلاش می‌کنند این‌طور القا کنند که من از دشمن خواسته‌ام سن‌دیگو و لس‌آنجلس را بمباران کند، در حالی که منظورم این بود که
افزایش موقت قیمت بنزین، بهای کوچکی برای اطمینان از این است که ایران سلاح هسته‌ای نخواهد داشت.
تصور کنید اگر سن‌دیگو یا لس‌آنجلس بمباران شوند، چه بهای سنگینی باید پرداخت شود. من فقط مقایسه‌ای میان پرداخت مبلغی بیشتر برای مدت کوتاه بابت بنزین و
خطر بمباران شهرهای بزرگ آمریکا
انجام دادم. همه این را فهمیدند، حتی رسانه‌های جعلی، اما همچنان می‌گویند من خواسته‌ام دو شهری را که دوست دارم بمباران کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/25212" target="_blank">📅 22:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25211">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5ff0b265b.mp4?token=iUrtN1-cI8W15WxDr8yT5lDllthdNNZE8ezJe_D5pOxB9Kh0RKkCeenji1XOiU4ydYMTScir8UiNYf1a3FEdSv_ZRUiwquHf8ahgLnvn8xEGESsCpQ2iqc2ZWMccRI43wa6Ukr3DL1yHAyLMHUiHaZWI_Lmj4G2Um7dqkIbayMMLtJ3GP572CE_AUd3QDlvuQ4Ah16yEJwzGpHznQJwU-POqGTIs717uPSYEpkCAx5dxvcZzk0AFhXdKKGezIB8kxiEPxy3uyGhS_lwQLBLANjheiwBaCNK25umYmDply261NGbkcfHUzAcs50X0yq6W25a9rhSwuWxNcxrxEZbYnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5ff0b265b.mp4?token=iUrtN1-cI8W15WxDr8yT5lDllthdNNZE8ezJe_D5pOxB9Kh0RKkCeenji1XOiU4ydYMTScir8UiNYf1a3FEdSv_ZRUiwquHf8ahgLnvn8xEGESsCpQ2iqc2ZWMccRI43wa6Ukr3DL1yHAyLMHUiHaZWI_Lmj4G2Um7dqkIbayMMLtJ3GP572CE_AUd3QDlvuQ4Ah16yEJwzGpHznQJwU-POqGTIs717uPSYEpkCAx5dxvcZzk0AFhXdKKGezIB8kxiEPxy3uyGhS_lwQLBLANjheiwBaCNK25umYmDply261NGbkcfHUzAcs50X0yq6W25a9rhSwuWxNcxrxEZbYnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست، وزیر جنگ آمریکا: ما به‌دنبال
اداره و بازسازی ایران از طریق حضور نظامی
نیستیم و نمی‌خواهیم تعداد زیادی نیروی نظامی را در ایران مستقر کنیم یا کنترل مناطق این کشور را در دست بگیریم. هدف ما صرفاً این است که به آن رژیم اسلام‌گرای افراطی بگوییم: شما هرگز سلاح هسته‌ای نخواهید داشت. اینکه این مسئله به روش آسان حل شود یا به روش سخت، انتخاب با ایران است؛ اما در نهایت این رئیس‌جمهور است که تصمیم خواهد گرفت. و می‌توانم تضمین کنم اگر آن لحظه فرا برسد، اقدام ما سریع و قاطع خواهد بود. این رئیس‌جمهور اهل بازی کردن نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/25211" target="_blank">📅 22:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25210">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f244d9f33.mp4?token=aDpi997A2DSIy49GWY6R-upwRTt5znFS90JIPGpeP-AIQiPpH_wnGB6p2nJM9yVr-9qoZDMVZfoOTj3kmUNdFS1so07rj_C86SjjLlI_MJzzuWrrdfokMlWjrnkqBicxPtpbfnYkDStzzRAJnlBlLF8qssokajCP1VrgaezIY9rbe4DC7YYsTCncWEI5E46RVbzAl5RHMHkODzZbQ-6ZnFTFNpwsAS96VefV1_oIy78GhsRG87gZxWhkrvv6o9MfGP2Wlau5xPZo8tw8t3U-f3u2x0KZtnj1edyCEPPcEZ-VRuVySS1QlFWz-C4HLBlMnKxyx6adtBllc0crOwDBVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f244d9f33.mp4?token=aDpi997A2DSIy49GWY6R-upwRTt5znFS90JIPGpeP-AIQiPpH_wnGB6p2nJM9yVr-9qoZDMVZfoOTj3kmUNdFS1so07rj_C86SjjLlI_MJzzuWrrdfokMlWjrnkqBicxPtpbfnYkDStzzRAJnlBlLF8qssokajCP1VrgaezIY9rbe4DC7YYsTCncWEI5E46RVbzAl5RHMHkODzZbQ-6ZnFTFNpwsAS96VefV1_oIy78GhsRG87gZxWhkrvv6o9MfGP2Wlau5xPZo8tw8t3U-f3u2x0KZtnj1edyCEPPcEZ-VRuVySS1QlFWz-C4HLBlMnKxyx6adtBllc0crOwDBVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا، درباره ایران:
ترامپ رئیس‌جمهوری نیست که بازی دربیاورد. او رئیس‌جمهوری نیست که
اتلاف وقت بیش از حد را تحمل کند.
ترامپ صلح می‌خواهد، اما حاضر است برای رسیدن واقعی و تاریخی به صلح،
هر کاری که لازم باشد انجام دهد.
ایرانِ دارای بمب هسته‌ای، اتفاق بدی است؛ نه فقط برای ما، بلکه
برای تمام جهان.
@WarRoom</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/25210" target="_blank">📅 22:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25209">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ایلان ماسک نشان ملی علوم را دریافت کرد. @WarRoom</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/25209" target="_blank">📅 22:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25208">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05da9e1cfb.mp4?token=Wjibp6x6-9lsf1OEhgzqofO4r5Y5JB8QD_sUMVIKnNIy_Gv7UzucPzDrXLH7Cju2w1hI5aDv2AecUMGDHTDFUD2g6PMGBR00TUPfsIlluZLFlyFewOAFv7pcMWegfn51XAsT2Na4U3onLFRVKuJLsXIps7Y6tqCOY_7eJ3oe7lKgDf0ZsOKwctaFJ_HW7ta8uGge5PQ1YNRA-BimbE-4KPsH_VnXRp6Q0Y2c7iBki37jdyqp-X5t7s9nA56AKoITL-OgrvjqZYQT7EfNE-Pfsn7-16jBe58aKkdQ3KiGL_cIJDAmZdnlz2ApNKanZy0GhPlKLMppZgrTyvxbWHIFeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05da9e1cfb.mp4?token=Wjibp6x6-9lsf1OEhgzqofO4r5Y5JB8QD_sUMVIKnNIy_Gv7UzucPzDrXLH7Cju2w1hI5aDv2AecUMGDHTDFUD2g6PMGBR00TUPfsIlluZLFlyFewOAFv7pcMWegfn51XAsT2Na4U3onLFRVKuJLsXIps7Y6tqCOY_7eJ3oe7lKgDf0ZsOKwctaFJ_HW7ta8uGge5PQ1YNRA-BimbE-4KPsH_VnXRp6Q0Y2c7iBki37jdyqp-X5t7s9nA56AKoITL-OgrvjqZYQT7EfNE-Pfsn7-16jBe58aKkdQ3KiGL_cIJDAmZdnlz2ApNKanZy0GhPlKLMppZgrTyvxbWHIFeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک نشان ملی علوم را دریافت کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/25208" target="_blank">📅 22:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25207">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osrl4d5pm37-bxtCuRB3HJ-xtkIw8VYzetBY763BLo3Ws3i2uI2jP4a_YXxXWVGzA0DAUzm6TQtYz5eDnqXhrEf_LPnYBPi3NDO6nRME3rVAoHQ16E3xFvPBBK56RVJwohqNBchxGAXncJxFJnE90Gysl01S4uYdnr7QNkP84oKEyUOCw6772VGAlPkuzQRjo9gqGYau0mp3BtbEvauNNWl4R5KDiE06VZgTIIYfjG-YSUgPyOGdoyOLRtpBbuGFY7ZwFchR-mArpPlhUdo8VHVTXzA7nBZVEbbLIHQAOY0-wWicSReBJeHvE0YWU44Vr5-K6zuaPSywqUlZ_InF4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان و پوتین در حاشیه اجلاس سران کشورهای مستقل مشترک‌المنافع و اجلاس محیط‌زیستی دریای کاسپین در ترکمنستان دیدار و درباره
تقویت همکاری‌های اقتصادی و راهبردی در حوزه‌های انرژی، کشاورزی، حمل‌ونقل و تجارت
گفت‌وگو کردند. دو طرف بر تسریع اجرای پروژه‌های مشترک و گسترش همکاری‌های دوجانبه تأکید کردند.
خبرگزاری تاس: پوتین در این دیدار وضعیت خاورمیانه را
بحرانی و حاد
توصیف کرد و گفت روسیه آماده است برای مدیریت بحران و بازگشت ثبات به منطقه، در کنار ایران باشد و از تلاش‌های تهران برای پایان دادن به درگیری‌ها حمایت کند.
@WarRoom</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/25207" target="_blank">📅 21:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25206">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کانال ۱۴: مقام‌های سیاسی و امنیتی اسرائیل نشانه‌هایی جدی از احتمال ازسرگیری درگیری با ایران مشاهده کرده‌اند و به همین دلیل ارتش خود را برای شرایطی آماده می‌کند که ممکن است به سرعت به یک درگیری گسترده تبدیل شود
@WarRoom</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/25206" target="_blank">📅 21:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25205">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایلان ماسک
:
ایلان توماس ادیسونِ دوران معاصر ماست.
@WarRoom
یاشار : الان خرابش کرد یا تعریف کرد؟!</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/25205" target="_blank">📅 21:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25204">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/25204" target="_blank">📅 21:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25203">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fceaa00395.mp4?token=co8asWnvgQ_5JbwKl-sybLjyAo7kYGHdb9v20OHbBIPfMiF5WkfCNDEklq701y0gblIgK7B7o1R1yjfMLr5zLxq92DoFz_bIZlqcbIp5mWBoc9ztg_Xq0yo2-jIndlykwnVxxZWgrkQQOfq0UrM2xqsZY67jnshLwevHeAQzb5buwSSI8UlqCLAyYFLsTkMn7Wtuv7oc7h2-pLWS-gaSvqwFzOekeMj6hvX3maSCYYe-bK_1CKhQhPJ_RtaHRHyfuL9OAOdS64hUc4yuHPQwVfeEjlcKMm20pMpyq54ucxeoGKLAJrFvvImw9p3fhZXo3bbJJM8SmCy3-d6-uV0ic6CaV9aS7e8OxLlkM_h71Llh7HTYrB_bjVM1QrVWZbN3-Kf9xPY1GXmcSEu62S0ihNKTJVhw6JD7pXjm5hCaro-AtJqaLWQb2hxLaJ9E4ZBkzdzj-efQG-RTK74QgSDdn2oc_nnEXAwqzwMZ6e96jUz8rdWHIXILXfWziKuRyeN000O5PgqoxsjM0-0HIaca-mRFCEXgZSpjigAAyvQGhfPbhP45qbMj9F8LH_cWwgzrpMnoII25CxLfoSZhZe4JLSjLs9nSXBziycO8PNbJ3338eysON07RU2g8xjztGdsXO4-leXIf0ljo8klEanl4glteFwi5__COWQTMgHhkODg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fceaa00395.mp4?token=co8asWnvgQ_5JbwKl-sybLjyAo7kYGHdb9v20OHbBIPfMiF5WkfCNDEklq701y0gblIgK7B7o1R1yjfMLr5zLxq92DoFz_bIZlqcbIp5mWBoc9ztg_Xq0yo2-jIndlykwnVxxZWgrkQQOfq0UrM2xqsZY67jnshLwevHeAQzb5buwSSI8UlqCLAyYFLsTkMn7Wtuv7oc7h2-pLWS-gaSvqwFzOekeMj6hvX3maSCYYe-bK_1CKhQhPJ_RtaHRHyfuL9OAOdS64hUc4yuHPQwVfeEjlcKMm20pMpyq54ucxeoGKLAJrFvvImw9p3fhZXo3bbJJM8SmCy3-d6-uV0ic6CaV9aS7e8OxLlkM_h71Llh7HTYrB_bjVM1QrVWZbN3-Kf9xPY1GXmcSEu62S0ihNKTJVhw6JD7pXjm5hCaro-AtJqaLWQb2hxLaJ9E4ZBkzdzj-efQG-RTK74QgSDdn2oc_nnEXAwqzwMZ6e96jUz8rdWHIXILXfWziKuRyeN000O5PgqoxsjM0-0HIaca-mRFCEXgZSpjigAAyvQGhfPbhP45qbMj9F8LH_cWwgzrpMnoII25CxLfoSZhZe4JLSjLs9nSXBziycO8PNbJ3338eysON07RU2g8xjztGdsXO4-leXIf0ljo8klEanl4glteFwi5__COWQTMgHhkODg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : عموی من، دکتر جان ترامپ، از سوی دولت آمریکا مأمور شده بود گزارشی درباره نیکولا تسلا تهیه کند.
آنها می‌خواستند بدانند: آیا او واقعاً وجود داشته یا نه؟ آیا واقعاً یک نابغه بوده یا نه؟
عموی من، پس از مدت نسبتاً کوتاهی، به این نتیجه رسید که
تسلا واقعاً یک نابغه بزرگ بوده و از هر نظر کاملاً واقعی بوده است.
وگرنه مجبور بودید اسم شرکت خودروسازی را تغییر بدهید.
حالا اگر من آن گزارش را تهیه می‌کردم، ایلان، شاید می‌گفتم: «آن‌قدرها هم خوب نبود.»اما عموی من آدم متفاوتی نسبت به من است.
@WarRoom</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/25203" target="_blank">📅 21:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25202">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ece6af3331.mp4?token=msCTAtREI-cA3m1XA4Mtemfs-nnVq38neGStZiGN0RTom1JzSO9EfgxmM4ZUzsQUwpM-GZzuskCFbBCW8hZt4TZIseKTJdr4U0Tt93AC_1h_bP80wjHe3WAr-vZp-X89qOIHfMbCcJWnulX92CcRuR5VYLf9iuJPODVHP3PPRlYETwVkmZMGgsuxeTNCy34Jnpx_y1Ft3ZxD48fWcjl4vfBeVYKDvV1IdGg7yf-Cs0iibbwOk585VX6KNPW44wu4XUzKwmkkRR1QM703o1wz_Jfhr41oOQ17QFRrq6oLivdflspPZ2Ig_DVFRA8REWwCR8-Jy_zjy3Xn6LpiMar1GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ece6af3331.mp4?token=msCTAtREI-cA3m1XA4Mtemfs-nnVq38neGStZiGN0RTom1JzSO9EfgxmM4ZUzsQUwpM-GZzuskCFbBCW8hZt4TZIseKTJdr4U0Tt93AC_1h_bP80wjHe3WAr-vZp-X89qOIHfMbCcJWnulX92CcRuR5VYLf9iuJPODVHP3PPRlYETwVkmZMGgsuxeTNCy34Jnpx_y1Ft3ZxD48fWcjl4vfBeVYKDvV1IdGg7yf-Cs0iibbwOk585VX6KNPW44wu4XUzKwmkkRR1QM703o1wz_Jfhr41oOQ17QFRrq6oLivdflspPZ2Ig_DVFRA8REWwCR8-Jy_zjy3Xn6LpiMar1GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : می‌خواهم به شرکت اسپیس‌ایکس بابت بازگشت ایمن فضانوردان مأموریت شماره ۱۲ از ایستگاه فضایی بین‌المللی، که چند ساعت پیش اتفاق افتاد، تبریک بگویم.
تصور کنید اگر همه چیز به این خوبی پیش نمی‌رفت؟ آن لحظه خیلی خوشایند نخواهد بود. فکر می‌کنم شاید ایشان اینجا نبودند.شاید شما هم اینجا نبودید. اما همیشه برای ایلان ماسک همه چیز به خوبی پیش می‌رود، نه؟ ما به شما افتخار می‌کنیم، به شما خیلی افتخار می‌کنیم، شما یک گنجینه ملی هستید
@WarRoom</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/25202" target="_blank">📅 21:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25201">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اکسیوس: سرلشکر ایال زامیر، رئیس ستاد کل ارتش اسرائیل، روز سه‌شنبه به مقام‌های ارشد آمریکایی هشدار داد که
اگر جنگ با ایران طی سه هفته آینده از سر گرفته شود، اسرائیل ممکن است مجبور شود انتخابات ۲۷ اکتبر را به تعویق بیندازد.
زامیر همچنین هشدار داد که ایران ممکن است در پاسخ به حملات، اسرائیل را با موشک هدف قرار دهد. این هشدار پس از آن مطرح شد که مقام‌های آمریکایی او را در جریان آمادگی‌های نظامی برای ازسرگیری عملیات علیه ایران قرار دادند.
ترامپ پس از آن اعلام کرد که
آمریکا پیش از انتخابات میان‌دوره‌ای ۳ نوامبر به ایران حمله نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/25201" target="_blank">📅 21:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25200">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIRxyHtPtJu3GBjLKfQV6YvJ8xOU3TXFhP5Fvbv7Cp28VoOEbxI301l0RbGRu6NbaCQVGFgOjmd-0QsUR3Op41e-KJ9ohHegcri070wDFrGWPKdP9j1Y_ErlSntAeANdWp_tTUATIMMOpLmzMoykVMbl3gpZAQNrs1vLPY4xWxVkK5rWMyL4F6y6sCKHkQ3QTDilqUaf5aw6dOiGNgZ0gH2fpUaz9QO3f38LVWEqODwrFOwiQnbkuMW1zWCBvDH73CZpAHaeOw4jApi9JheW_UlzVEcIR2N-hYWlpANCLPb8toSys-KuG3RBSyV66TL6GyCoVzlQXE3W_P9D3ciBRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ما در حال انجام گفت‌وگوهای سازنده‌ای با جمهوری اسلامی ایران هستیم. می‌خواهم برای همه روشن کنم که، با وجود اینکه ایران هم از نظر اقتصادی و هم از نظر نظامی در وضعیت بسیار بدی قرار دارد، و با وجود اینکه محاصره همچنان با تمام قدرت و به‌طور کامل ادامه خواهد داشت، در حالی که نفت با رکوردی از تعداد بشکه‌ها از تنگه هرمز عبور می‌کند؛
تنها دیشب ۲۲ میلیون بشکه نفت عبور کرده است، بدون اینکه حتی یک بشکه از ایران آمده باشد یا به ایران رفته باشد!
ما پیش از انتخابات میان‌دوره‌ای آمریکا که در ۳ نوامبر برگزار خواهد شد، به هیچ‌وجه به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!
@WarRoom</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/25200" target="_blank">📅 20:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25199">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا: دفتر کنترل دارایی‌های خارجی آمریکا، ۱۲ کشتی و شرکت‌های مالک و اپراتور آنها را به‌دلیل انتقال نفت و محصولات پتروشیمی ایران تحریم کرد. به گفته خزانه‌داری، این کشتی‌ها
صدها میلیون دلار نفت و فرآورده‌های نفتی ایران را به بازارهای خارجی منتقل کرده‌اند
و درآمد حاصل از این صادرات به تأمین مالی برنامه‌های تسلیحاتی، نیروهای نیابتی و نهادهای امنیتی جمهوری اسلامی کمک می‌کند. کشتی‌های تحریم‌شده شامل هوت، اوشن کوی، نورث استار، فلیسیتا، آتیلا ۱، آتیلا ۲، نیبا، لوما، رمیز، دانو‌تا ۱، علا و گس فیت هستند. شرکت‌های هدف نیز شامل پوروس مریتایم ونچرز، اوشن کادوس شیپینگ، میسترال فلیت، وست مِرین، بهنگام تدبیر قشم، پاروس مریتایم، وانسا گس شیپینگ، گلدویو مریتایم سرویسز و ایتاکی مریتایم اند تریدینگ هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/25199" target="_blank">📅 20:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25198">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گزارش ویژه فاکس‌نیوز : گزارش‌ها حاکی از آن است که پنتاگون به «فرماندهی مرکزی ایالات متحده» (سنتکام) دستور تایید داده تا تدارکات لازم برای عملیات‌های رزمی گسترده و حملات علیه ایران را نهایی کند؛ گفته می‌شود که این برنامه‌ریزی‌ها پیش از انتخابات میان‌دوره‌ای…</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/25198" target="_blank">📅 19:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25197">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارش ویژه فاکس‌نیوز : گزارش‌ها حاکی از آن است که پنتاگون به «فرماندهی مرکزی ایالات متحده» (سنتکام) دستور تایید داده تا تدارکات لازم برای عملیات‌های رزمی گسترده و حملات علیه ایران را نهایی کند؛ گفته می‌شود که این برنامه‌ریزی‌ها پیش از انتخابات میان‌دوره‌ای در جریان است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/25197" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25196">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پلیس مبارزه با تروریسم بریتانیا : دو مرد لتونیایی است که در نزدیکی پایگاه هوایی سلطنتی مولزورث بازداشت شده‌اند. پلیس متروپولیتن ابتدا آنها را به ظن ورود غیرقانونی به یک مکان ممنوعه بازداشت کرد، سپس هر دو را طبق قانون امنیت ملی به دلیل ورود به یک مکان ممنوعه با هدفی مغایر با منافع بریتانیا دوباره دستگیر کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/25196" target="_blank">📅 19:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25195">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد!
از این به بعد در سراسر کشور، با خانمای بی‌حجاب برخورد و براشون جرم ثبت میشه.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25195" target="_blank">📅 19:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25194">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سنتکام: فرماندهی مرکزی آمریکا امروز در یک نشست مجازی با شرکای بین‌المللی حمل‌ونقل دریایی درباره وضعیت تنگه هرمز گفت
افزایش تلاش‌ها برای تضمین آزادی کشتیرانی و تردد امن کشتی‌های تجاری ضروری است.
دریادار برد کوپر، فرمانده سنتکام، از حمایت مستمر صنعت کشتیرانی و نهادهای دولتی آمریکا تشکر کرد و به خسارت‌ها و فداکاری‌های خدمه غیرنظامی در پی حملات ایران اشاره کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25194" target="_blank">📅 18:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25193">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6hnJzi0fq9Bsu6VaVdDxk2OZCdD5G1nxVDZ4vpz-gjviJn7sgDeUv7nFFoGBcQLIbA26b_eAWLINfrXsSSGMPDrYnLDCZJl7Ht8lN1vMMpt8uBjJkKc0Wab3bK6rPweL8OiucVA5GOg0ga3L7n46vaS9IFCuAITS5w-sKO0XygPZIbigmse_d8w6YCMgQ1W2mpQzJiIh-zGLDuioDZEVeEg7mFnV--ri2m1xVEn2qb-g1nJp7SjmLLrTuAlzr65BIPMAaJyHdmbNmSm1uYAWSdLUmqEqU1G1yH3Co0K7htiJ7tNXeUhL-qaPexkfCckhd7SWAx8aD5FgU_akOcrPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان نظارت دریایی بریتانیا (UKMTO) گزارش تأییدشده‌ای را از یک منبع معتبر دریافت کرد مبنی بر اینکه یک تانکر حامل نفت خام، در روز سه‌شنبه، هنگام عبور از تنگه هرمز، مورد اصابت یک پرتابه قرار گرفته است.
هنوز هیچ گزارشی مبنی بر وقوع تلفات انسانی منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/25193" target="_blank">📅 18:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25192">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/918015a856.mp4?token=DoYc3_WSlNFDWopqTOLTWGfEY00By0thoj97_RavG1v3iyZbkJZmWpYZEEcyteJWDldUjXU2h85AgwY95_IJzYio510W4t62BKRZjAK6ZwH9zXr0B_jMLjBvgrOWYUCknbgGE2LwtnaLZvdfNz6IfbI6QMZ94rxGXp4zhxn9fD40pwDS4FZdPcUcuOJGZvXDW935u-IMAtBVJQbIXep80cvJPMiDEQk-f_PZJZ3WklR2FSA0DYMm0MnwQRLGRcVd9E1AE2904ddvtufDAQLeYGSHQP2K9PUCSqFNPWu29lsoemFUeC7vARi5MbV5wWqlLOcb8L3ou5xq4EtrlPDOjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/918015a856.mp4?token=DoYc3_WSlNFDWopqTOLTWGfEY00By0thoj97_RavG1v3iyZbkJZmWpYZEEcyteJWDldUjXU2h85AgwY95_IJzYio510W4t62BKRZjAK6ZwH9zXr0B_jMLjBvgrOWYUCknbgGE2LwtnaLZvdfNz6IfbI6QMZ94rxGXp4zhxn9fD40pwDS4FZdPcUcuOJGZvXDW935u-IMAtBVJQbIXep80cvJPMiDEQk-f_PZJZ3WklR2FSA0DYMm0MnwQRLGRcVd9E1AE2904ddvtufDAQLeYGSHQP2K9PUCSqFNPWu29lsoemFUeC7vARi5MbV5wWqlLOcb8L3ou5xq4EtrlPDOjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره جمهوري اسلامي ایران:
می‌خواهید مشکلات را ببینید؟ بگذارید به لس‌آنجلس حمله کنند یا به جایی مانند سن‌دیگو. بگذارید به یکی از شهرهای بزرگ ما حمله کنند.
به این می‌گویند مشکل.
@WarRoom</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/25192" target="_blank">📅 18:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25191">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c4309370e.mp4?token=WPe9EWJq31TBcMOJtWcbn3Fhoe15aWsx7sEX9aJuHYqnbsjB02aB8b9BE9eb7PsEyAuRpsCwwx4Jbyf_6tRDN-js0pb_9TBioiu-T7z4-BSnMjHNXxuTlyETUPx5hiG9yzZYdFuwOb7cSNfrpCUfsajzeEBZ-QI55LHgHIjUoULLq_IZLIu0KRLk4vUPp0oRZjyvXNUY9lHSTT54dgqKwdnee1VlSsplmoxAgxhyJRPl3MaIn6oadYTbQRI72EQnUJF7J9AdnJ3Rm5qZByjjIjcvZqYfQqIzEv5iCydNZf9gsjoMnfmu9eybfTADNfKVvCq_jKAaJ8dAVR2fOuJU5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c4309370e.mp4?token=WPe9EWJq31TBcMOJtWcbn3Fhoe15aWsx7sEX9aJuHYqnbsjB02aB8b9BE9eb7PsEyAuRpsCwwx4Jbyf_6tRDN-js0pb_9TBioiu-T7z4-BSnMjHNXxuTlyETUPx5hiG9yzZYdFuwOb7cSNfrpCUfsajzeEBZ-QI55LHgHIjUoULLq_IZLIu0KRLk4vUPp0oRZjyvXNUY9lHSTT54dgqKwdnee1VlSsplmoxAgxhyJRPl3MaIn6oadYTbQRI72EQnUJF7J9AdnJ3Rm5qZByjjIjcvZqYfQqIzEv5iCydNZf9gsjoMnfmu9eybfTADNfKVvCq_jKAaJ8dAVR2fOuJU5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره جمهوري اسلامي ایران:
ما ایران را به شدت شکست داده‌ایم. دیگر تهدید سلاح هسته‌ای وجود ندارد.
آن‌ها در حال حاضر در یک آشفتگی کامل هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/25191" target="_blank">📅 18:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25190">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af618364fb.mp4?token=YI4zOvV56XUB5ZPD7gJvgBUDVkMaYbbOnTzvTwXMIoM6UkqJqBCaB8a4nLRd9TdwVXRkYri7cQIX5aBfMf9604CcNnFVBPfnJVMMyyJH7BEFXftbVjv2C7iq-Otz1S42S20_nLI9mRKPExwG8zQbO-hX-zDMyxuC7faFW4VPlgvbHyY5766m20R92iNOZ-zz59km0PZJN8tbM_NYhsjCjx_hPh-9xsIfYxkHlc_i9Fqb8eDB-HxK9fUnS7eg6Wxb1PjQBi2PJB1fyMWBstF5cszNySLkK7O-QyiD6vmqaCcT-MzMckdQrr3lfgtA4RzPX5ertq7mUTWqgkrHyaYmIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af618364fb.mp4?token=YI4zOvV56XUB5ZPD7gJvgBUDVkMaYbbOnTzvTwXMIoM6UkqJqBCaB8a4nLRd9TdwVXRkYri7cQIX5aBfMf9604CcNnFVBPfnJVMMyyJH7BEFXftbVjv2C7iq-Otz1S42S20_nLI9mRKPExwG8zQbO-hX-zDMyxuC7faFW4VPlgvbHyY5766m20R92iNOZ-zz59km0PZJN8tbM_NYhsjCjx_hPh-9xsIfYxkHlc_i9Fqb8eDB-HxK9fUnS7eg6Wxb1PjQBi2PJB1fyMWBstF5cszNySLkK7O-QyiD6vmqaCcT-MzMckdQrr3lfgtA4RzPX5ertq7mUTWqgkrHyaYmIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
پیروزی جمهوری‌خواهان در ماه نوامبر برای برنامه‌های شما چه معنایی دارد؟
پرزیدنت ترامپ:
خب، فکر می‌کنم این به معنای میراث است. فکر می‌کنم بسیار مهم است. داشتن یک پیروزی واقعاً تأییدی است.
@WarRoom</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/25190" target="_blank">📅 18:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25189">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رویترز: قیمت نفت برنت امروز بیش از ۴.۵ درصد افزایش یافت و به حدود
۱۰۴.۷۵ دلار
رسید؛ نفت WTI نیز به حدود ۹۲.۲۸ دلار رسید. تشدید حملات به کشتی‌ها، نگرانی درباره هرمز و درگیری عربستان و حوثی‌ها از عوامل اصلی افزایش قیمت‌ها هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/25189" target="_blank">📅 17:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25188">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e36deea25c.mp4?token=WahQbrJUTC7eK1VuAnjZZRDcqXkP9szkFqUxV6KSuebRY8x4MeeJvwXsz25Z16qY7BwjKApQ7Zx03mUitDjrwrW4G8rNQK4WN8WPSddHtsdrm2ZvdvI3EjZ2gqcLmeOLUPxHc1FsN0G1AUlKm6duqFI2c5Clzr_XJFMMFb-OOPdMdMygIv3Y8TtLpaXbea8d6HtIYz00m631ZTaIvDhKYcTXJnqZQ-OvUfdKmFu2cAti_hsoNeHvUvxQe82OobiobSvoVwW6_73qTzx5ApgQXIJJkSdoF3z2DBg4QsLlCVrfw4ST0at14kjWoKiwgNfNiA_iJbqGAa8GRneZ7lDzYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e36deea25c.mp4?token=WahQbrJUTC7eK1VuAnjZZRDcqXkP9szkFqUxV6KSuebRY8x4MeeJvwXsz25Z16qY7BwjKApQ7Zx03mUitDjrwrW4G8rNQK4WN8WPSddHtsdrm2ZvdvI3EjZ2gqcLmeOLUPxHc1FsN0G1AUlKm6duqFI2c5Clzr_XJFMMFb-OOPdMdMygIv3Y8TtLpaXbea8d6HtIYz00m631ZTaIvDhKYcTXJnqZQ-OvUfdKmFu2cAti_hsoNeHvUvxQe82OobiobSvoVwW6_73qTzx5ApgQXIJJkSdoF3z2DBg4QsLlCVrfw4ST0at14kjWoKiwgNfNiA_iJbqGAa8GRneZ7lDzYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو: حکومت ایران مجروحان اعتراضات را در بیمارستان‌ها می‌کشد
حکومت ایران وقتی معترضان زخمی می‌شوند، وارد بیمارستان‌ها می‌شود و آن‌ها را می‌کشد؛ گاهی حتی پزشکان و پرستارانی را که آن‌ها را درمان کرده‌اند نیز به قتل می‌رساند.
@WarRoom</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/25188" target="_blank">📅 17:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25187">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رویترز:
خطر حمله به نفتکش‌ها در اطراف تنگه هرمز افزایش یافته
و هفته گذشته بیشترین تعداد حملات از آغاز جنگ ثبت شد. ایران به کشورهای منطقه هشدار داده هرگونه تلاش برای ایجاد مسیرهای جدید صادرات نفت در اطراف هرمز را اقدامی خصمانه می‌داند و احتمال استفاده از موشک، پهپاد و قایق‌های نظامی برای جلوگیری از این مسیرها وجود دارد. در تازه‌ترین مورد، یک نفتکش شیمیایی در نزدیکی قطر هدف چند پرتابه قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/25187" target="_blank">📅 17:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25186">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/548fb32aef.mp4?token=aPSv8MEITAwkqPYT8-p7eKd2rCYe9T7as0zM4uUiju0L9yapwYiB4e6fHlot8yjriAkSlH4bl1kFcO2LottfUho8Ex-Yrf2I1tUuhdR0vqEF8PeUeQ1BnsY7-69v_lyHzAVK1CRp6jYZLHXy8_c2q9SjjfmKCUHftACdkRDPJM_p5ZcCrLzaw2u-AA3r_CbGMf6E2Gc8BH1n-Ikrgew0naa4yixoe3m-BWZb75cHnuev9oV8wrUseluaFzl6pqADha9ldullUIqqnoT_OsqSPfNeI-YSXB5B-LR2KJ2S6qSfSGlS3auv3tw5DnPfXzviHz4ggi1Y1gqb9FlLcl1e5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/548fb32aef.mp4?token=aPSv8MEITAwkqPYT8-p7eKd2rCYe9T7as0zM4uUiju0L9yapwYiB4e6fHlot8yjriAkSlH4bl1kFcO2LottfUho8Ex-Yrf2I1tUuhdR0vqEF8PeUeQ1BnsY7-69v_lyHzAVK1CRp6jYZLHXy8_c2q9SjjfmKCUHftACdkRDPJM_p5ZcCrLzaw2u-AA3r_CbGMf6E2Gc8BH1n-Ikrgew0naa4yixoe3m-BWZb75cHnuev9oV8wrUseluaFzl6pqADha9ldullUIqqnoT_OsqSPfNeI-YSXB5B-LR2KJ2S6qSfSGlS3auv3tw5DnPfXzviHz4ggi1Y1gqb9FlLcl1e5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا :
هیچ کاری علیه ایران وجود ندارد که بخواهیم یا لازم باشد انجام دهیم و نتوانیم آن را انجام دهیم
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25186" target="_blank">📅 16:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25185">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وزیر امور خارجه، چپقچی :
روند مذاکراتی همچنان ادامه دارد و از طریق میانجی‌ها پیام‌ها در حال رد و بدل شدن است.ما طرح خود را که تحت عنوان «طرح هفت‌روزه» ارائه کرده بودیم، مطرح کردیم و دیدگاه‌های طرف آمریکایی را نیز در مقابل آن شنیدیم. در حال حاضر مشغول بررسی دیدگاه‌های آمریکایی‌ها هستیم و فکر می‌کنم ظرف چند روز آینده پاسخ خود را ارائه خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25185" target="_blank">📅 15:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25184">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اتاق جنگ با یاشار : ناو هواپیمابر هسته‌ای روزولت قرار است برای نخستین‌بار طی حدود
چهار سال
وارد بندر
یوکوسوکا در ژاپن
شود. شورای شهر یوکوسوکا روز چهارشنبه از مقامات شهری و شهردار خواسته برای ورود یک ناو هسته ای آماده باشند، اما
نام ناو، تاریخ دقیق ورود و مدت توقف هنوز اعلام نشده است
. ژاپن قرار است فقط ۲۴ ساعت پیش از ورود، اطلاع رسمی دریافت کند.
ناو
USS Theodore Roosevelt (CVN-71)
و گروه رزمی آن در حال حاضر در اقیانوس آرام هستند و برای یک
استقرار طولانی‌مدت در خاورمیانه
به سمت غرب حرکت می‌کنند. بنابراین
روزولت گزینه اصلی برای این توقف  کوتاه ، یوکوسوکا محسوب می‌شود.
@WarRoom
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25184" target="_blank">📅 15:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25182">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">BTC 82,500$
🔻
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25182" target="_blank">📅 15:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25181">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دلار و تتر ۲۶۸،۰۰۰ تومان
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25181" target="_blank">📅 15:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25180">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مراسم خاکسپاری جاویدنام علیرضا رئیسی که همراه با علیرضا سپاهی حکمش اجرا شد @WarRoom
🖤</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25180" target="_blank">📅 15:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25179">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رویترز: هفتمین مظنون پرونده طرح ادعایی حمله به پایگاه هوایی فرفورد بریتانیا با پهپاد آزاد شده اما تحقیقات ضدتروریسم ادامه دارد. پلیس بریتانیا این پرونده را مرتبط با یک طرح احتمالی با حمایت ایران بررسی می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25179" target="_blank">📅 14:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25178">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نیویورک‌تایمز: اسرائیل به آلمان درباره افزایش خطر حملات احتمالی مرتبط با ایران علیه پایگاه‌های نظامی آمریکا، به‌ویژه
رامشتاین و اشپانگدالم
، هشدار داده است. ارزیابی‌های اطلاعاتی احتمال حمله با پهپاد را نیز مطرح کرده‌اند، اما تاکنون زمان یا هدف مشخصی برای حمله تعیین نشده است. هم‌زمان، تحقیقات درباره طرح ادعایی حمله به پایگاه آمریکایی فرفورد در بریتانیا ادامه دارد و مقام‌های بریتانیایی به احتمال دخالت ایران اشاره کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25178" target="_blank">📅 14:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25177">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae1a2241b4.mp4?token=O8zdCUyeMlBYcjSyuvrMf1p1DlCUBkbD6xTh3i_6595rBn8MI4XItj3q9pi1ZGW7H8TgzKtn84UcKrJ9rCfWF1Zj253XNMjQU6XhDkznLrMKzPLI2ZnBTSvLdIDFMnugoVuv1k21P-4EHuGVCNHDiTns0tiH7P3gDjizC3K4b4r6SOeAQBnkhTKLYZiaAYE4f4D7RvFzdJ5b3eE6klnv5zSyBoldm5vNPCMznirYf1pE0sU_jIJH23OhuInLCsFEge1tGJiT4kjBvl7J2hXD4RFHzGKyZwhRmo9C8UDcdXuXNm1Aj2C_WnuMKIUQLPdLrGU4xJKswrsboE_4WFLXli6t1j4LvRLkmu1ibJdYxgqPFzSFPSsOHbby4y2-OkcILBO1Bp0Ajy_vFqnAN_ypw531JKCVbKmw6WC4SPSobxAmwi-dg-Nx4Tjp-rQCSeRQQ8aGEeOax8IwSmOY4du00LgBSecMgdkL8yf7wk-N30lP7gIN-RKzD7-jJcqNw8t6_2GShdXkhnOA2T2nTG2QbeGcTiBtSIb3vyNwSiq2Su-syuhI_YRS1aUQm0Y374a_zubuail4M64_KpaB0xyoscuo5HlICO82YjAo3StTU5ulN-XFlfiKNYX-8dh-HqAAiZdtmJ4NAlqsga_d9ELeIQvEMDdoSjdwpgfjB608ppY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae1a2241b4.mp4?token=O8zdCUyeMlBYcjSyuvrMf1p1DlCUBkbD6xTh3i_6595rBn8MI4XItj3q9pi1ZGW7H8TgzKtn84UcKrJ9rCfWF1Zj253XNMjQU6XhDkznLrMKzPLI2ZnBTSvLdIDFMnugoVuv1k21P-4EHuGVCNHDiTns0tiH7P3gDjizC3K4b4r6SOeAQBnkhTKLYZiaAYE4f4D7RvFzdJ5b3eE6klnv5zSyBoldm5vNPCMznirYf1pE0sU_jIJH23OhuInLCsFEge1tGJiT4kjBvl7J2hXD4RFHzGKyZwhRmo9C8UDcdXuXNm1Aj2C_WnuMKIUQLPdLrGU4xJKswrsboE_4WFLXli6t1j4LvRLkmu1ibJdYxgqPFzSFPSsOHbby4y2-OkcILBO1Bp0Ajy_vFqnAN_ypw531JKCVbKmw6WC4SPSobxAmwi-dg-Nx4Tjp-rQCSeRQQ8aGEeOax8IwSmOY4du00LgBSecMgdkL8yf7wk-N30lP7gIN-RKzD7-jJcqNw8t6_2GShdXkhnOA2T2nTG2QbeGcTiBtSIb3vyNwSiq2Su-syuhI_YRS1aUQm0Y374a_zubuail4M64_KpaB0xyoscuo5HlICO82YjAo3StTU5ulN-XFlfiKNYX-8dh-HqAAiZdtmJ4NAlqsga_d9ELeIQvEMDdoSjdwpgfjB608ppY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم خاکسپاری جاویدنام علیرضا رئیسی که همراه با علیرضا سپاهی حکمش اجرا شد
@WarRoom
🖤</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25177" target="_blank">📅 14:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25176">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حمله مسلحانه به مینی‌بوس حامل کارکنان نزاجا در بلوچستان روابط عمومی لشکر ۸۸ زرهی نزاجا: ساعتی قبل مینی‌بوس حامل کارکنان لشکر مستقر در سواحل مکران که برای تعویض شیفت در مسیر بودند، در محدوده شهرستان نیکشهر مورد حمله مسلحانه قرار گرفت. متأسفانه در این درگیری…</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25176" target="_blank">📅 13:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25174">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9s9y0c1vU-LzUWJZD2J0RZxFEDw2qypnw9lcP92sNtYsuA8I_2XZHx0jUBtPyN_0lvgUlp2HemHpD2whBbHIULlfFmC8ePvARKuxdp4A513vJMXmDIYIprVAfk6uX4E1iP4ELGKLz95yLjDMBLKi1zXL6c2z8S1KQRSrO_zt2yau5wwP7-3-H2Pbzwkr4Lurd8ARKt1KcBIGHo_y0RoI1qIBdxTHzEQ7YQswyTxGsmTsEq3NmvCcrmNWDkPa0_rQGHh4Qb9hUbyzKaLOcW1MO6vt3gs__1d6mgjMBHFLT9BQG7jyzirWT8w5E0mXuJeGawyoUwI_Krh6R6NPp0jWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : دیروز ناو هواپیمابر آبراهام لینکلن آمریکا به سن‌دیگو خانه خود بازگشت و عرزشی ها آن را به تمسخر گرفتند، ولی نکته مهم و شکه کننده که دیدم در این ویدیو و آنها باید گریه کنند این است که نشانه‌های انهدام(کیل مارک) ثبت‌شده رویش حدود ۱۰۵ پهپاد و ۳۴ ناو جنگی را در این ویدیو نشان میدهد عملکرد قابل‌توجهی برای تنها یک گروه هوایی مستقر روی یک ناو هواپیمابر.هگست وزیر جنگ پیشتر گفته بود که ناو لینکلن و گروهش ۶۴ ناو جنگی ایران را نابود کردند (بیش از ۲/۳ام نیروی دریای ایران )
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25174" target="_blank">📅 13:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25170">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AbKDPHX7tbSF7K8nsIVp47HtZxu9zU3AaAhB3Sb5DlslEKmKLTpXYhdvZ0A-n-IOQn3wb7zIpF_WjwDWkvAGYC0DMmRI5kDd1lHWxzQ3JCa1rbTn33C7rcXVIIFiacUoIhESZIMT4szGtST0u57f3LbdgmcmD0LZru1awJiRaxt8G4AhU_4KGtR5DvCBmgzkHt4Hfjk2GszoOXP6U3T81R4vthIuGG310kLV2cDQhlT1MnSBhBmokJRBjgOdNajx8n6-KUJeUxz06vbvDLi_ZELkFT4LYLWSRCidU3UwEw6OnEhaihF6M9UKASP4IPU1Q8eqvpHW3bdM9R-kK3bO7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/imNUQ1kYGSA0SKBtVATgHJG1MTYlXGRgy_UNA9JiPH4dbZoiidPFLfCSNrTetNvY2buxMczWzNhXhYMrquN7BoRKIfFlb0YJ_UN57COZjDUX3hHAVJUMuViRMdru7KOQNqLXKhM0cyiFckO2UEjobOF4lbKieTcRilCS0U4ZFjcjBPKA2ipj03lgm0bS_XeF23nA-hd-we1wihlslohCYs0y5arMAKvETv2HcDImEUJSMrtNfmSNJkJCvN9Cl8W13jShfycekD--8LUh20o4JMRB7fV4QXbuEItvng6yABa-01fq4xKY0POotw4qvxUU_9IhKoXf3alrSgFmJH2pTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcbYYN0YLOV3BxexkzvqL_xovLHBoPMry0FJCCBT8Rn-sgiSLIFabUlJutH6WdNGdOYBA3SIXMfoFb-kBXxK6KP9s2PFuMlWLVI_DjyU-AmGS1t_K02hv71Cs-UTF-8pmTJZzMCkndinSvoWO30O1-mleb5WoXdmWZAmbMA1pnmCmUCYCNojlxpsveravIiaPAQybfHz0kTWP7LNHtNNL7wXP-o4SXDX005t_dKhWGWH-WuhixAcBlteEPujvnlGzHzwBjNNyIrxBo3UuOFNFZppfCW3QmoImjiAv860M3Jf8SI8TTEOBzElzr4vsgrkdg46AUWL4aAWGSqCB1MI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eFEvz01CSBoOnXjRAAFTdDit1wk9SSNxXKqwAhhQ9UtXeSETkwtRoFA_P6o1kVv4d7EEDXThTsLy7z9oDOXgdVVJW74KvG3LvEm7PMrKjzWhm1VWKqvjsbsRvq1uyEiC-GytP66Cxe1A8zXawoaGtyi0L89X0C7F_Iza7Yeaw6pmjDkxnlWslmye2AcyLijQeCritRmCor6V9KTYjqU_9VyZU22vlUnsobpGe2jFcmLNyZ-iJmL0OPbnQiAW8mFaytadGepU3hGEObhFRf5qRbeNr-Jyy4W_hWWmRgnB8s7CpT74gAWFSq-dIqpYwj_eh2kNScWKpowRGEtvo_84Wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک جنگنده
اف ۳۵ سی ناونشین آمریکا
از
اسکادران ۳۱۴
تفنگداران دریایی، با سه نشان انهدام زیردریایی در بدنه مشاهده شده است؛
زیردریایی‌هایی باید از کلاس غدیر ایران باشند.
همچنین روی این جنگنده نشان‌های انهدام
یک نفتکش، یک ناو جنگی، یک پهپاد شاهد، یک قبضه هویتزر، دو پرتابگر موشک و سه سامانه راداری
دیده می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25170" target="_blank">📅 13:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25169">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مرد خردمند ، مارک لوین : به نظرم سخنرانی
روبیو
حال‌وهوای سخنرانی یک نامزد ریاست‌جمهوری را داشت، هرچند این بدان معنا نیست که او در این باره تصمیم قطعی گرفته باشد. این سخنرانی تفاوت آشکاری با نوع اظهارات و سخنرانی‌های ونس دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/25169" target="_blank">📅 13:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25168">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMD65rc3c-XJKJpfuyXBYqQ2V9kMZmVl9WaOCMivhrX_BJN1dzrinJZTVyxg_qys4yryG_xitE8WHjndvqoWOOTFKjIBo7eWawbN7ezroNJeern_JZD8ejFI-I4IabwV1de_UUc-g282_iXETE9x5Xber7vlhjTlXdYA6uB-WYtSRE3Du9z5rYNB3YFCha33saUc3PblkRCgKXsxkLM8slsMa5IhpoI6aZq6Glc8XDdom7dWRxUFYT1rDrh_BlYYt0R5PlQ2WWCVu6BH7XJ8VBMqItPtMmHi8IWRWmFxiHwyiNxouAVoQStjz_pZ0kZsdYYt8LILIV-7aACWdG9EkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ مهر، «روز مهر از ماه مهر» و جشن مهرگان و پیروزی داریوش بزرگ بر گئومات مغ و آغاز شهریاری او فرخنده باد
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25168" target="_blank">📅 12:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25167">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حمله مسلحانه به مینی‌بوس حامل کارکنان نزاجا در بلوچستان
روابط عمومی لشکر ۸۸ زرهی نزاجا:
ساعتی قبل مینی‌بوس حامل کارکنان لشکر مستقر در سواحل مکران که برای تعویض شیفت در مسیر بودند، در محدوده شهرستان نیکشهر مورد حمله مسلحانه قرار گرفت.
متأسفانه در این درگیری یک نفر به نام «محمدرضا اوکاتی» به شهادت رسید و ۳ نفر مجروح شدند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25167" target="_blank">📅 12:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25166">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6614110b.mp4?token=dEkedDKL7r-alWHCSvC2tu1u4Ka0iEUHoSaXhnDtRpan0YvcRNqEamOASr6bmuWe8ZNCAslsy5OKvJRoZI81dUdQqM1cLJnvJk2Ba2cybQ3-eoFE74fRHKabHwzcFznTBur3Gvn811NReQqKlhtU3IhDXluxyx3vQOT-OBuqiITcxZHF8orghFUMt294HSi3v6wvoXC4SbIgUqwNRVRAIS6DumglSxYImbTkMAvirJIXDXIEcMTRHdzLLW3DhSBdDHe4we-iSUCs8ghblqGqk9l1_LqC-byXYfTse0p6lIQl1BpApjWFXxXjXi2wlcNg9nuj7FtIu-4dusSdmKwKBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6614110b.mp4?token=dEkedDKL7r-alWHCSvC2tu1u4Ka0iEUHoSaXhnDtRpan0YvcRNqEamOASr6bmuWe8ZNCAslsy5OKvJRoZI81dUdQqM1cLJnvJk2Ba2cybQ3-eoFE74fRHKabHwzcFznTBur3Gvn811NReQqKlhtU3IhDXluxyx3vQOT-OBuqiITcxZHF8orghFUMt294HSi3v6wvoXC4SbIgUqwNRVRAIS6DumglSxYImbTkMAvirJIXDXIEcMTRHdzLLW3DhSBdDHe4we-iSUCs8ghblqGqk9l1_LqC-byXYfTse0p6lIQl1BpApjWFXxXjXi2wlcNg9nuj7FtIu-4dusSdmKwKBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : زنم بهم گفت یه لطفی بکن، کلمه vegan رو درست تلفظ کن!
‏من میگفتم “وِیگن”! از کجا باید بدونم چطوری تلفظ میشه؟! من استیک دوس دارم!”
@WarRoom
😂</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25166" target="_blank">📅 12:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25165">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رویترز: ایران ماه گذشته ۲۰۰ میلیون دلار به حزب‌الله لبنان داد تا این گروه به خانواده‌های لبنانیِ آواره‌شده در جنگ با اسرائیل کمک مالی کند.حدود ۵۰ هزار خانواده که خانه‌هایشان تخریب شده یا امکان بازگشت ندارند، در اولویت قرار می‌گیرند و به هر خانواده در مرحله…</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25165" target="_blank">📅 11:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25164">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رویترز:
بیت‌کوین فقط امروز ۱.۳ درصد افت کرد و به حدود ۸۲٬۲۶۵ دلار رسید
و اتریوم نیز ۰.۸ درصد کاهش یافت. رشد دلار، بازده اوراق و قیمت نفت مهم‌ترین فشارهای کلان بر بازار رمزارزها هستند. حدود
۵۵۰ میلیون دلار معاملات اهرمی
در بازار کریپتو لیکویید شده که بخش عمده آن مربوط به معامله‌گرانی بوده که روی رشد قیمت شرط بسته بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25164" target="_blank">📅 11:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25163">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اکسیوس: پنتاگون برای احتمال ازسرگیری عملیات گسترده علیه ایران آماده می‌شود
منابع آمریکایی و اسرائیلی می‌گویند در صورت آغاز عملیات، حملات می‌تواند تأسیسات هسته‌ای، زیرساخت‌های انرژی و دیگر اهداف راهبردی ایران را دربر بگیرد. این موضوع پس از نشست چندساعته تیم امنیت ملی ترامپ در کمپ‌دیوید و تماس‌های اخیر او با نتانیاهو مطرح شده است. یک مقام پنتاگون به اکسیوس گفت:
«وظیفه این وزارتخانه، توسعه گزینه‌های نظامی و ارائه آنها به رئیس‌جمهور است.»
یک مقام کاخ سفید نیز گفت ترامپ در هر زمان همه گزینه‌ها را در اختیار دارد و آمریکا به‌دلیل کنترل تنگه هرمز و وضعیت اقتصادی ایران، در موقعیت قدرتمندی قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25163" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25162">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
پنتاگون به
فرماندهی مرکزی آمریکا(سنتکام)
دستور داده است آماده‌سازی‌ها برای احتمال
ازسرگیری عملیات‌های گسترده نظامی علیه ایران
را تکمیل کند.
بر اساس این گزارش، حملات ممکن است
پیش از انتخابات اسرائیل و آمریکا
آغاز شوند؛ با این حال،
دونالد ترامپ، رئیس‌جمهور آمریکا، هنوز تصمیم نهایی را اتخاذ نکرده
و
هیچ تاریخی نیز تعیین نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25162" target="_blank">📅 10:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25161">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شبکه NBC به نقل از یک مقام آمریکایی، یک مقام خاورمیانه‌ای و یک مقام ایرانی گزارش داد که
ایران و آمریکا در ماه جاری میلادی در نیویورک، از طریق میانجی‌ها درباره برنامه هسته‌ای ایران گفت‌وگو کرده‌اند.
واشنگتن می‌گوید هر توافقی باید موضوع هسته‌ای ایران را نیز شامل شود و ایران میگوید خط قرمز است و اصلا
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25161" target="_blank">📅 10:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25160">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تنش جدید اسرائیل و بریتانیا
اسرائیل در واکنش به تحریم‌های بریتانیا علیه شهرک‌های اسرائیلی در کرانه باختری، دستور تعطیلی
کنسولگری بریتانیا در شرق اورشلیم
را صادر کرد. گیدئون ساعر، وزیر خارجه اسرائیل، این اقدام را واکنشی به سیاست‌های «خصمانه» بریتانیا دانست. اد میلیبند، وزیر خارجه بریتانیا، گفت لندن حق اسرائیل برای بستن کنسولگری را به رسمیت نمی‌شناسد و بر سابقه نزدیک به ۲۰۰ ساله این نمایندگی تأکید کرد. امروز تابلوهای کنسولگری پایین آورده شد، اما یک تیم محدود بریتانیایی همچنان اجازه فعالیت در ساختمان را دارد.
سفارت بریتانیا در تل‌آویو همچنان فعال است.
@WarRoom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/25160" target="_blank">📅 10:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25159">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ: ایرانی‌ها آماده‌اند هر کاری را برای ما انجام دهند تا از آنچه در حال وقوع است جلوگیری کنند، با این حال، توافق با آنها واقعاً گزینه‌ای نیست که من ترجیح بدهم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/25159" target="_blank">📅 10:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25158">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gw3g3ikHgzr40jmhH3wsuj2H2bbru_fEpKeniusWhIczDWc_2UShI0Fdm5mLKYYXoAIerg1TXFCsXHNPOzhddvbz6wy63l3I2XnCiafyf-F4UackXL6V2qSzhsSyKhtQQzStHazNxuCUdrt8jHelxn1Bn0I8qIlZrgr_m17SmVIGz1i4n3s0iePw-kPbcxCpUQPojV2GPvECWuW6js5WZA33e0xZ2KEIoq-nfGR_vLZh3o-xhdp6OBjar7DhDjR18k5-z0iZCW8wzKAAHza9U_zrHWreqhdTjPA15C_Q8C-wLQvTVlBeZPAReRPKbNeYrd4CyUe_cwp9GSUUR4k4Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «انتقال نفت به سطح پیش از جنگ بازگشت!»
@WarRoom
حجم انتقال نفت خام از منطقه خلیج فارس :
قبل از مارس: جریان نفت در سطح میانگین و طبیعی خود (حدود ۲۴ تا ۲۵ میلیون بشکه در روز) قرار داشته است.
ماه مارس: با بسته شدن و انسداد تنگه هرمز در پی تنش‌ها و آغاز درگیری، حجم انتقال نفت افت چشمگیری پیدا کرده و به کمتر از ۱۰ میلیون بشکه در روز سقوط می‌کند.
ماه‌های بعد تا سپتامبر و اکتبر: جریان صادرات نفت به‌واسطه استفاده از خطوط لوله جایگزین زمینی، مسیرهای دوربرگردان و پشتیبانی ترانزیتی روندی صعودی به خود گرفته و مجدداً به سطح میانگین پیش از جنگ (تراز ۱۰۰ درصدی سال ۲۰۲۵) بازگشته است.
@WarRoom
یاشار: چنل های بی سواد همه اینو زدن قیمت نفت
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/25158" target="_blank">📅 10:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25157">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeQkT_Xudztc1ToZ0FIf_3tVPJtd0stWcLwQPa4Q8Vs9-1IMEiGYpuT0a0xvYLDGux7WqWfCJHmhPJnFD2beoxXVfQtM7Qt-y-YZAI9cX0Jg5WH6xfRGpovDGn0UUxJS049HXHgHl85IcW6VY29xadp_tIGZOOlPNVZtJtQovWLdui8-ToZEzqJkA-8P166dBdg53ic1J7MAjKEPms425jXhBE7KlkkG4BXoK9ODnJnj3KJc4QtnUwevWz9Zhbaw_2uvDsczGBdCOOJIY7vtqerc7h4j7yDzDxYaRcPDnV01l-McdfvfXv2TkDSSmnWub-MF-2Wy66GN0weP-EewmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس ۳۰ دقیقه‌ پیش صدای‌ انفجار‌ شدیدی‌ اومد … @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/25157" target="_blank">📅 10:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25156">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بندرعباس ۳۰ دقیقه‌ پیش صدای‌ انفجار‌ شدیدی‌ اومد …
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/25156" target="_blank">📅 10:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25155">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71094a656.mp4?token=ZzstzdwMLJMZD-aLqTIUYtmWGxgQsvvCO4y4PUmp7My7SSbEwz7IScC2xYl-15nO2zU7vq4RXvB6Pj_IjJBUCGY0nsZPu6KYlmkhquyD72Sih1_RT8lkRY8G4r2xRkHIChBvYqqaAz_ivPivVbH5xy73dHhYo7SR2z5MtpnKsqDin7xtRFVqF-PfJz-CrY7bEJQtzcF39ZS5qgdxmCmZqlDgOGpnykpVKRL7-MDJlMBSGGITNgAuaBjL1MsQQM3ba-A9youYQSGR-Nhb5YY84cWIVPkwbC4IDqKUekZv3wvWmWDafRdYeUgRDiey8nem8No2QNll4V-FLpJYqYfBmnLDQhv9Ka19ZhHzZnNa1hyynXIgu1Fe42e3fzpqfK1HjwjrTl6xF-iPsDsn9VwF2dMC-_bk8YZsr0S2tzBOxHz94a9hHH_OEhuVGgx5DtRh9sRH16DCv1krvQuZXEvxWNb5Kln5uC42KNl4cmyUCYqHdetnRmnfj6fN0yF-2bzsP6ufYMY6GwehSk5a6yS3Pu5Jxy8N6qM5t7nm8bs9fDzm1L2eVHs8Pf5bWM21nUBaFqtdFsPr_vc28JiohAP78FwM2ar-WRH-zyUgxRukrSSVpXiCrbuNnAQpGDPMmvHIKCEXdOXLOtRWrynsehrsb3IklMXmV_vCwepynL4Ca_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71094a656.mp4?token=ZzstzdwMLJMZD-aLqTIUYtmWGxgQsvvCO4y4PUmp7My7SSbEwz7IScC2xYl-15nO2zU7vq4RXvB6Pj_IjJBUCGY0nsZPu6KYlmkhquyD72Sih1_RT8lkRY8G4r2xRkHIChBvYqqaAz_ivPivVbH5xy73dHhYo7SR2z5MtpnKsqDin7xtRFVqF-PfJz-CrY7bEJQtzcF39ZS5qgdxmCmZqlDgOGpnykpVKRL7-MDJlMBSGGITNgAuaBjL1MsQQM3ba-A9youYQSGR-Nhb5YY84cWIVPkwbC4IDqKUekZv3wvWmWDafRdYeUgRDiey8nem8No2QNll4V-FLpJYqYfBmnLDQhv9Ka19ZhHzZnNa1hyynXIgu1Fe42e3fzpqfK1HjwjrTl6xF-iPsDsn9VwF2dMC-_bk8YZsr0S2tzBOxHz94a9hHH_OEhuVGgx5DtRh9sRH16DCv1krvQuZXEvxWNb5Kln5uC42KNl4cmyUCYqHdetnRmnfj6fN0yF-2bzsP6ufYMY6GwehSk5a6yS3Pu5Jxy8N6qM5t7nm8bs9fDzm1L2eVHs8Pf5bWM21nUBaFqtdFsPr_vc28JiohAP78FwM2ar-WRH-zyUgxRukrSSVpXiCrbuNnAQpGDPMmvHIKCEXdOXLOtRWrynsehrsb3IklMXmV_vCwepynL4Ca_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ ، درباره ایران:
«همان‌طور که قول داده بودم، اطمینان حاصل می‌کنم که ایران هرگز به سلاح هسته‌ای دست پیدا نکند. آنها این را می‌دانند.
ما به‌زودی از آنجا خارج خواهیم شد و خواهید دید که قیمت نفت مثل سنگ سقوط خواهد کرد و قیمت همه‌چیز نیز پایین خواهد آمد.
این عملیات بزرگی بود که روسای‌جمهور قبلی باید طی سال‌های گذشته انجام می‌دادند. باید انجام می‌شد، اما هیچ‌کس حاضر نبود مسئولیت آن را بر عهده بگیرد. ما چاره‌ای نداشتیم، چون نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/25155" target="_blank">📅 09:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25154">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c7d98ccb1.mp4?token=t4mZgYhHu81DvL6F1vWDq6gaNNFacp3wH4ozBzGXyu4Cx60l9A-TPKLbhHGNS1YabPx8VOp-yHxjgs5WTv4wMCr5eg_5b7FBovXFGMxS1vjEhuaUwTs79-kEiHKdcE601sBKh09zXLZo7yB-FwSSgmYC8A-azJnlqGhM6mGZqN4mtQFU2CQPoTeu07qGAIGCjr_KRPtCcRYg7JXQXD-bp4kzjsbqh5lhyMhiryrhnlnwfZfDOspqJlhl3Rwd2EGrjCP-kwJBQLitKK-O_4ds5eUq-eTKw5oC7J9cFwIJgBzDSrUeVr8czFKwES_ASSZiI_m9g2WVNFRVjEkPf0gkZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c7d98ccb1.mp4?token=t4mZgYhHu81DvL6F1vWDq6gaNNFacp3wH4ozBzGXyu4Cx60l9A-TPKLbhHGNS1YabPx8VOp-yHxjgs5WTv4wMCr5eg_5b7FBovXFGMxS1vjEhuaUwTs79-kEiHKdcE601sBKh09zXLZo7yB-FwSSgmYC8A-azJnlqGhM6mGZqN4mtQFU2CQPoTeu07qGAIGCjr_KRPtCcRYg7JXQXD-bp4kzjsbqh5lhyMhiryrhnlnwfZfDOspqJlhl3Rwd2EGrjCP-kwJBQLitKK-O_4ds5eUq-eTKw5oC7J9cFwIJgBzDSrUeVr8czFKwES_ASSZiI_m9g2WVNFRVjEkPf0gkZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : استیو ویتکاف در حال کار روی توافق با ایران است و عملکرد بسیار خوبی دارد
فکر می‌کنم این توافق واقعاً چیزی نیست که من بخواهم انجام دهم، اما آنها حاضرند هر چیزی به ما پیشنهاد دهند تا این درگیری متوقف شود.»
@WarRoom</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/25154" target="_blank">📅 09:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25153">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfd30d3c3.mp4?token=Xg9UFFxhVikRG_dfbzel4chLbI_w8nsG_0LRhcQY585iDTPSyK68oOALuLE1-Mh6BILczl4wjmXGtNf2I-pApNvY5-YAx3PkYE7aurL5PtW_IHI9ct5E7_7xwZ1ExMg5iao0UOM3Nq_fobR0BBOayR1uf3j2poLq_xLwSskjc752-u9QqEOBfkCGBtG7L0EABY0gjMwF_vm47fL0KlCNhMVlPcZ3Sz1d7iWHSQTb3e92shlx_vmlIIWxdfe164aNHegEo1f_Em6gK3Jac4TwsM-lNC3liRgrQk7rvGv_pD4HH89-efkDOPa0BVrHgG6O7mVQqqgSYi-t05z1THnQhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfd30d3c3.mp4?token=Xg9UFFxhVikRG_dfbzel4chLbI_w8nsG_0LRhcQY585iDTPSyK68oOALuLE1-Mh6BILczl4wjmXGtNf2I-pApNvY5-YAx3PkYE7aurL5PtW_IHI9ct5E7_7xwZ1ExMg5iao0UOM3Nq_fobR0BBOayR1uf3j2poLq_xLwSskjc752-u9QqEOBfkCGBtG7L0EABY0gjMwF_vm47fL0KlCNhMVlPcZ3Sz1d7iWHSQTb3e92shlx_vmlIIWxdfe164aNHegEo1f_Em6gK3Jac4TwsM-lNC3liRgrQk7rvGv_pD4HH89-efkDOPa0BVrHgG6O7mVQqqgSYi-t05z1THnQhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره ایران:
«می‌خواهید تروما و مشکلات را ببینید؟ بگذارید آنها در مسیر، یک موشک به سمت سن‌دیگو یا لس‌آنجلس شلیک کنند.
می‌خواهید صحنه‌ای وحشتناک ببینید؟ می‌خواهید مشکلات را ببینید؟ بگذارید سن‌دیگو یا لس‌آنجلس را هدف قرار دهند.
ما اجازه نخواهیم داد چنین اتفاقی بیفتد. ما از شهرهایمان و کشورمان محافظت می‌کنیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/25153" target="_blank">📅 09:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25152">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c79099a6.mp4?token=U8-_A1I5Dh_JoS3z-_9fFT5ZCRjmlnIDT8PcuWVUxUjZcr-pJzib_4vuliEWVBc3mwY_S8RqT1vD-gVSigfyafBaqOHfaOZUWW9VydAaEyaDBh-xE-lJCSzi2m2smihFeRaIIyVG72g9j6XU5sjr_MCV-e3ElAQ48s9QmME33zZ-xKk7fz8Rn9pp1hgJnuOInZj1iVWtHk0Yg9ZMsKPVYq7QgQYh9-fn-zvNzGVnfc8rD9xImXf4RKTu7ZbwA-J4L02J8-w1Jdjg3DYlrUjoVZlX2GIQNXQNYdKkHB5qMTSjJQfBGD7oXv0oWoV9RrR75IiTaKcPuR0s3ZjwJWZg7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c79099a6.mp4?token=U8-_A1I5Dh_JoS3z-_9fFT5ZCRjmlnIDT8PcuWVUxUjZcr-pJzib_4vuliEWVBc3mwY_S8RqT1vD-gVSigfyafBaqOHfaOZUWW9VydAaEyaDBh-xE-lJCSzi2m2smihFeRaIIyVG72g9j6XU5sjr_MCV-e3ElAQ48s9QmME33zZ-xKk7fz8Rn9pp1hgJnuOInZj1iVWtHk0Yg9ZMsKPVYq7QgQYh9-fn-zvNzGVnfc8rD9xImXf4RKTu7ZbwA-J4L02J8-w1Jdjg3DYlrUjoVZlX2GIQNXQNYdKkHB5qMTSjJQfBGD7oXv0oWoV9RrR75IiTaKcPuR0s3ZjwJWZg7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ‌ : در سه شب گذشته، ما بیش از هر مقطع دیگری در تاریخ تنگه هرمز، نفت بیشتری از این تنگه خارج کرده‌ایم.»
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25152" target="_blank">📅 09:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25151">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ef85cb34d.mp4?token=o-79UNlIsQ9V9Rst75e2cRUWMBd-XB1uxwIQkQBCThBBSer69XJt6Y1koAUu4tg9h5dflRlBfhzJE2Kv4zIxv0BSMGcRB_VCIp6yHkXJYUomPvDf3EpQGQg-io4vtReGgkunMnaVI2gOxggBwBFPMsEeOQ-aq5lDxpbnFIMQCvvVV5zAtY27EnYObm0wIpm2RT2nPYZJQWLcSR-l39eUipGHTdgN-4WEtbaQVpKCedR_o6sDq9JEsEqSlF3--skTRMi5lcc7MaFo9weHOh6lXL151xWGStROxu_aBKPWQOMKqZo9UZgnMpyHxqB9H645yqNdkZDkcPM53emLdnA8jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ef85cb34d.mp4?token=o-79UNlIsQ9V9Rst75e2cRUWMBd-XB1uxwIQkQBCThBBSer69XJt6Y1koAUu4tg9h5dflRlBfhzJE2Kv4zIxv0BSMGcRB_VCIp6yHkXJYUomPvDf3EpQGQg-io4vtReGgkunMnaVI2gOxggBwBFPMsEeOQ-aq5lDxpbnFIMQCvvVV5zAtY27EnYObm0wIpm2RT2nPYZJQWLcSR-l39eUipGHTdgN-4WEtbaQVpKCedR_o6sDq9JEsEqSlF3--skTRMi5lcc7MaFo9weHOh6lXL151xWGStROxu_aBKPWQOMKqZo9UZgnMpyHxqB9H645yqNdkZDkcPM53emLdnA8jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«جنگ خیلی زود به پایان می‌رسد. آنها کشوری شکست‌خورده هستند.
هنوز کمی روحیه و جسارت برایشان باقی مانده، اما زیاد نیست؛ اصلاً زیاد نیست.»
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25151" target="_blank">📅 09:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25150">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سخنگوی کاخ سفید : رئیس جمهور ترامپ از روند فروپاشی اجتناب‌ناپذیر ایران راضی است.
ترامپ اجازه نخواهد داد که رژیم ایران مانند آنچه با روسای جمهور سابق اتفاق افتاد، او را مچل کنند.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25150" target="_blank">📅 02:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25149">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا، روی ناو یو‌اس‌اس آبراهام لینکلن: ایران هیچ‌وقت نتوانسته راهی برای عبور از آبراهام لینکلن پیدا کند و طبیعتاً هم همین‌طور باید باشد. خیلی خوب بود که ناوگروه شما از ابتدای این مأموریت با نیروی دریایی ایران به یک توافق رسید؛ توافق شما…</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25149" target="_blank">📅 02:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25148">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14526f5af7.mp4?token=vZoKe7e5L4g9H2oDgOgfZ3z4V7HNVK0BX_DQI57EdMbV0pHnqUQgJT43sdqH9Fn2Gzb6JL6rdGHIijw8UDLtamTJN1fRo4lhCr7S7SVuf76qiTeF5OhjP5z0nzzBqBL5zeKYv9OGI1q9gPOYYxsyIg8iAS2hR2UMU7eecto3dY1LTD56OrbAX4NSw4ylwbIPNnHokdKzcYhwcaWU0fzDLA1Re5vQy_K5zPYvIAgEfiKX_A7T6SItChRvtiQXUmclbrE-ZtxS6XncEtQEntm_GaX96hYGHPYSyqncnTfCiZNuchjQ8pLBPqACyCSrxUNWzm9BWOYputo-H7zzcmlOdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14526f5af7.mp4?token=vZoKe7e5L4g9H2oDgOgfZ3z4V7HNVK0BX_DQI57EdMbV0pHnqUQgJT43sdqH9Fn2Gzb6JL6rdGHIijw8UDLtamTJN1fRo4lhCr7S7SVuf76qiTeF5OhjP5z0nzzBqBL5zeKYv9OGI1q9gPOYYxsyIg8iAS2hR2UMU7eecto3dY1LTD56OrbAX4NSw4ylwbIPNnHokdKzcYhwcaWU0fzDLA1Re5vQy_K5zPYvIAgEfiKX_A7T6SItChRvtiQXUmclbrE-ZtxS6XncEtQEntm_GaX96hYGHPYSyqncnTfCiZNuchjQ8pLBPqACyCSrxUNWzm9BWOYputo-H7zzcmlOdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا، روی ناو یو‌اس‌اس آبراهام لینکلن:
ایران هیچ‌وقت نتوانسته راهی برای عبور از
آبراهام لینکلن
پیدا کند و طبیعتاً هم همین‌طور باید باشد. خیلی خوب بود که ناوگروه شما از ابتدای این مأموریت با نیروی دریایی ایران به یک توافق رسید؛ توافق شما این است که
اقیانوس را با هم تقسیم می‌کنیم، اما نیروی دریایی ایران سهمش کف اقیانوس است و آبراهام لینکلن سطح اقیانوس را در اختیار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25148" target="_blank">📅 02:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25147">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBA6uHNNkFe0b8paetF2YPR0nHJn6sP-IDS5DSKz1I3Kd8qJio_mLFGW5Ixy4-2b5kpVdM1AJfZrs2Ae64aM4ZlBN4RFK2_oVTRDGirBieJv-leDx_1wXae-M4K9ABSqJIkIJY9m24fiv_Q29pK2h6FvWza0_W0oSYuA-WPIeNjtJm2gjzzu7z68BkCavnDZ8W2hNTDpdq9uKB--6U9P5dokxMQjsJ6529LKspGNV4U0Q_vEiOneYs1ELl38WXx4QvSnJHCl_3TMQDX4x_xPmaUeOdVOSQReoEvhsuVMf0Vq2DSQXkdEU9f_8vnbENwiXOC_szGfL1Nrx_N5aVDZ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقت‌یاب سنتکام :
ادعا:
امروز یکی از ژنرال‌های سپاه پاسداران در گزارش‌های رسانه‌ای مدعی شد که «تنگه هرمز بسته است» و ایران «کنترل کامل آن را در اختیار دارد». این ادعا
نادرست است
.
واقعیت:
در حال حاضر تردد از تنگه هرمز ادامه دارد و کشتی‌های تجاری حامل کالا و محموله‌های انرژی، از جمله
حدود ۲۰ میلیون بشکه نفت خام
، در حال عبور هستند.
ایالات متحده و شرکای منطقه‌ای آن کنترل آشکار تنگه را در اختیار دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/25147" target="_blank">📅 01:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25146">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آکسیوس به نقل از سه مقام ارشد آمریکایی:
عربستان سعودی و سوریه در حال بررسی
اعزام نیروهای ارتش سوریه به یمن برای مقابله با حوثی‌ها
هستند. چندین یگان سوری برای این مأموریت در نظر گرفته شده و شمار نیروها می‌تواند به
۱۰ تا ۲۰ هزار نفر
برسد. این موضوع در دیدار اخیر
احمد الشرع و محمد بن سلمان
در ریاض مطرح شده و هدف عربستان، تقویت نیروهای دولت یمن و فراهم کردن امکان عملیات زمینی علیه حوثی‌هاست. با این حال، هنوز تصمیم نهایی برای اعزام نیروهای سوری گرفته نشده و مذاکرات ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/25146" target="_blank">📅 01:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25145">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ در تروث: سه سال پیش در چنین روزی، یعنی ۷ اکتبر، جهان شاهد یکی از تاریک‌ترین و شرورانه‌ترین روزها در تاریخ اسرائیل بود. مردان، زنان و کودکان بی‌گناه به دست تروریست‌های حماس به قتل رسیدند، ربوده شدند و متحمل وحشت‌هایی غیرقابل‌تصور گشتند. امروز، ما یاد تمام جان‌های بی‌گناهی را که از دست رفتند گرامی می‌داریم، به بازماندگان و خانواده‌هایشان ادای احترام می‌کنیم و به یاد گروگان‌هایی هستیم که رنج‌هایی غیرقابل‌تصور را تاب آوردند. من بی‌وقفه جنگیدم تا گروگان‌ها را به خانه بازگردانم و آن‌ها را به عزیزانشان برسانم؛ و این کار را انجام دادم، چه برای آنان که زنده بودند و چه برای آنان که جان باخته بودند! ما هرگز ۷ اکتبر را فراموش نخواهیم کرد. ما هرگز قربانیان را فراموش نخواهیم کرد. و همواره در برابر نیروهای ترور و شرارت خواهیم ایستاد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25145" target="_blank">📅 01:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25144">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0adcb3b11.mp4?token=BjbkIQbSy2V0Ki-6wDgtTLFMrRB4l1M0uRCEMgImO2MJYGr7EGZx2Taow7eCdPL5O85n5E21JAPu6_cqyiM7zYTF0Bz2PzIPTfT6ynYHROLKd-F9Sh060aNO0J66VBlJtGKdI9xghzHTAZdw405uN3zAPWr6xVA9HhOlwr_Bi-dyDaHt63Wi-AC5QFuzPHmWZHSxRqxA4M42V5a3dV8jc_7BeS7ENIVhSiqoLIwkfvwW3MtT4HxKLCCkLzeUUdGn0ZnaYOAhii9ubEB-iaVqGxDPEj7vtZV-qPf7nRScRHMZE0IsbknSxKBuay3aEW-F63nGqx0tgWqULV4F2WbwuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0adcb3b11.mp4?token=BjbkIQbSy2V0Ki-6wDgtTLFMrRB4l1M0uRCEMgImO2MJYGr7EGZx2Taow7eCdPL5O85n5E21JAPu6_cqyiM7zYTF0Bz2PzIPTfT6ynYHROLKd-F9Sh060aNO0J66VBlJtGKdI9xghzHTAZdw405uN3zAPWr6xVA9HhOlwr_Bi-dyDaHt63Wi-AC5QFuzPHmWZHSxRqxA4M42V5a3dV8jc_7BeS7ENIVhSiqoLIwkfvwW3MtT4HxKLCCkLzeUUdGn0ZnaYOAhii9ubEB-iaVqGxDPEj7vtZV-qPf7nRScRHMZE0IsbknSxKBuay3aEW-F63nGqx0tgWqULV4F2WbwuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25144" target="_blank">📅 00:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25143">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران اعلام کرد که پاسخ ایران به پیشنهادات مطرح‌شده توسط آمریکا از طریق واسطه‌ها به طرف مقابل منتقل خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25143" target="_blank">📅 00:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25142">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران: مشاوره‌های ما با عمان با موفقیت انجام شد و بر سر هماهنگی‌های مربوط به مسیرهای امن به توافق رسیدیم.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25142" target="_blank">📅 00:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25141">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سخنگوی نیروهای ائتلاف: ما 82 هدف نظامی متعلق به شبه‌نظامیان حوثی را در استان‌های صعده، الحدیده، الجوف و مأرب منهدم کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25141" target="_blank">📅 00:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25140">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">به قول شاعر نایس پرفیوم
😼</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25140" target="_blank">📅 00:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25139">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3af54a6283.mp4?token=g4qqZLIf_6MEr6Sjb0C4fiukIUDCJLjKYe087JsBH1PrutCTCvzwG0e4ft8dkMRM1X_BSdWGlazxQydIVZatLGl_Dzw0dZBfML6p4s7rDZl279w64jLhD2J-joZwgyiUT6a5BRmnWvgI1x9tn0kdoQXmX20A5ELJXRHlgrlH5G7xlMQ9FWyG2-0nnJ3JteQ7UNK0mkeMCqjTwZBgR8OX9kozv-cgTrMbE0tTjvHGqPJZpKahXJEyHfp6_FB-4B0PplRHFTlLBlJ-vp6N_8C1d0qSMF4RwtS3Rl3g9ua5ZS1L1Nj1WtHu8moYa0ZsGjLg1oiLFtH8asEdPfT2hFNPtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3af54a6283.mp4?token=g4qqZLIf_6MEr6Sjb0C4fiukIUDCJLjKYe087JsBH1PrutCTCvzwG0e4ft8dkMRM1X_BSdWGlazxQydIVZatLGl_Dzw0dZBfML6p4s7rDZl279w64jLhD2J-joZwgyiUT6a5BRmnWvgI1x9tn0kdoQXmX20A5ELJXRHlgrlH5G7xlMQ9FWyG2-0nnJ3JteQ7UNK0mkeMCqjTwZBgR8OX9kozv-cgTrMbE0tTjvHGqPJZpKahXJEyHfp6_FB-4B0PplRHFTlLBlJ-vp6N_8C1d0qSMF4RwtS3Rl3g9ua5ZS1L1Nj1WtHu8moYa0ZsGjLg1oiLFtH8asEdPfT2hFNPtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/25139" target="_blank">📅 00:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25138">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25138" target="_blank">📅 00:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25137">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25137" target="_blank">📅 00:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25136">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df53d80fe4.mp4?token=Jr-sKl8HgJaHzFVQ-DDwQ1840XD9Jt0oGqCyQUKnP_9iT4dLBXNKqaz7A7A-8NcGXFWry8JbESAwgO4CnaziHKwt-OQ1zT-iZm9uZnK8Vn0AbbjKHl_wjwfLNBPGyoAVV2BMGG822T5yguwjr0ZdDW068XXn2CZ8E12qwccd5N_wnzA8pBOhA1fPut1fJAQ5yhLnlvDtX94nCPmePf2dDw7YdOvUHsRwKGEYHfBdq5c-WMzvu3aJJE1bi6c053Q3tw6Xezw6rqf7snUtWLNopTx8GOch0Rx6vIyX0A1erXtsOtoZXd8RNXbf1Gqp7j0V8g52sIl7Uoztb8y7WFJTyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df53d80fe4.mp4?token=Jr-sKl8HgJaHzFVQ-DDwQ1840XD9Jt0oGqCyQUKnP_9iT4dLBXNKqaz7A7A-8NcGXFWry8JbESAwgO4CnaziHKwt-OQ1zT-iZm9uZnK8Vn0AbbjKHl_wjwfLNBPGyoAVV2BMGG822T5yguwjr0ZdDW068XXn2CZ8E12qwccd5N_wnzA8pBOhA1fPut1fJAQ5yhLnlvDtX94nCPmePf2dDw7YdOvUHsRwKGEYHfBdq5c-WMzvu3aJJE1bi6c053Q3tw6Xezw6rqf7snUtWLNopTx8GOch0Rx6vIyX0A1erXtsOtoZXd8RNXbf1Gqp7j0V8g52sIl7Uoztb8y7WFJTyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلانتری گلشن تبدیل به گوهشن شده , درگیری ادامه داره
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25136" target="_blank">📅 00:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25135">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سیستان و بلوچستان درگیری های شدید گزارش میشه ، همه هم شکل و لباس هستند و حکومت درمونده شده ، نمیفهمه از ‌کجا و کی میخوره
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25135" target="_blank">📅 00:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25134">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سپاه خون دماغ شده دکمه پرتاب آبگرمکن از بندر عباس رو هی میزنه ، تنگه صدای ناله های شهید عججی میاد
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25134" target="_blank">📅 00:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25133">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25133" target="_blank">📅 00:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25132">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25132" target="_blank">📅 00:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25131">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خبرگزاری صدا‌وسیما : حمله مسلحانه به مقر انتظامی در گلشن  بنا بر اعلام منابع آگاه دقایقی قبل یکی از مقرهای انتظامی در شهرستان گلشن سیستان و بلوچستان مورد حمله مسلحانه قرار گرفت. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25131" target="_blank">📅 23:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25130">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-lGUKeaDIKCbhpGcVlFBlCAfApzP1M7H8CMQQyW23TSHqu_p-DB8IC_o3sH5IQ-s2MZ8zPSFJfMkUQ0Po5U_wlsUvg98Jh9s_abaGvl3IX7TdTZVEAFFwJHJo8eD_AWC0Thj3fC1zlBs3SasncOQCG1sXde2Y_v4h1mAawkqF7ux3mhB_oYJ9392LR0diWn1Ohxbu1Q89Wm0OxdIO95sikw_PJ1HHLnhPIz_k3LHpdv0xxzR78TIWM2WV6MKbZaepq584ay4irqCKAEe_ozDsDlEozcKFlYrRcFJXuQa5FQBBOnzjRTERjLGs-j1pzPNd6G8GmM-sOeFmnh9TzAig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی مبنی بر وقوع یک حادثه در فاصله ۵۱ مایل دریایی شمال «مدینة الشمال» در قطر دریافت کرده است.یک نفتکش گزارش داده است که هدف اصابت چندین پرتابه قرار گرفته است.
گزارش‌هایی از تلفات انسانی منتشر شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25130" target="_blank">📅 23:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25129">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v312lVwcSVOS-RaMviO07VR-D4VZnMkY_wJukMVVa5-HBCa3QF3oMrNHPPCZdD1ckwJKXEuasr2OK1oi19XoeP0Lf0vltlYepCLur-W0KBAq-fx-7gzfMVpA9gE5m4TAuodbtr8W850XmRo796tJVAN0O5bA8m9LkUnsjhCL4dKUpRh31xvclVzTVFNNRXoojNzykNEmrHyR8kZe-ugJK9QAgJ2Di9hIOZg08qqKtlF-4c2vUsDGbXv8vxiHbl30ZTxB2hgb6U-7t10XCMw3iZtec7clBFlwWIyWhaMSb6lsDPW6Tg9OPoBhLajBY5m3mH5VuBf17zmSRz47LPf4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون نظام وظیفه: اگه لازم باشه برا جذب سربازای ۶۰ ساله هم فراخوان میدیم
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25129" target="_blank">📅 23:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25128">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25128" target="_blank">📅 23:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25127">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کانال 15 عبری: ایران در روزهای اخیر شلیک به سمت کشتی‌ها در تنگه هرمز را از سر گرفته است. ارزیابی این است که حمله‌ای از سوی آمریکا انجام خواهد شد و بنابراین ممکن است آنها بخواهند ابتدا حمله کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25127" target="_blank">📅 23:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25126">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c43a91ec.mp4?token=kjhF2s0PIcVyAO5pr-QnCcM6nAJI8RKG7FTTZhQ9fBld3GPt5OOyzah-sLLt69r-rBrqLULEU8FCa2vMTrnmeHt6iUDZx-8Avm8-M7-9t3Rw8gofKGyuIZAoU6M-BodjWnOyXbYa1q0T0VbIQROvY4yGCvnNBqv21vrf0ZJ_lANmOvNcxm1v1zQj1tCjsPZKdxohtstY8BcViIgntOx2ETKQKvWrv-kiEke_eAqDaBoRCp2Wlw8lWmvvqJS87XCcrCJFNP64lJJfKN0BzrBF5YAA0VdsbrRAzLvZIui7cnk5v8SMg94PZRDge2gIDAKe9imelY0fh8BBdN1Ih6CnOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c43a91ec.mp4?token=kjhF2s0PIcVyAO5pr-QnCcM6nAJI8RKG7FTTZhQ9fBld3GPt5OOyzah-sLLt69r-rBrqLULEU8FCa2vMTrnmeHt6iUDZx-8Avm8-M7-9t3Rw8gofKGyuIZAoU6M-BodjWnOyXbYa1q0T0VbIQROvY4yGCvnNBqv21vrf0ZJ_lANmOvNcxm1v1zQj1tCjsPZKdxohtstY8BcViIgntOx2ETKQKvWrv-kiEke_eAqDaBoRCp2Wlw8lWmvvqJS87XCcrCJFNP64lJJfKN0BzrBF5YAA0VdsbrRAzLvZIui7cnk5v8SMg94PZRDge2gIDAKe9imelY0fh8BBdN1Ih6CnOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره ایران:
فکر می‌کنم داریم خیلی خوب پیش می‌ریم. داریم ایران رو خیلی بد می‌زنیم.
اون‌ها هیچ‌وقت سلاح هسته‌ای نخواهند داشت، و این خیلی مهمه.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25126" target="_blank">📅 22:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25125">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHsHKyBrCflhoqbXfhvyGH6_80EPahv0hzXYL8eTVThOuos8ZZ_rqpoUdaR_ctsjMGUgi4qAzoYN5byQgESXdXfOYo5r8zSOZGqz_zjs0n2Ml-bdxhHYApo4Xx8EIXiYEZP-ymO5ESzaGQ0inyCsfq3342god81y5JQO-pq9UYt4HRZuvec00d_3WAJE462NqGKN7lIC35fZXOA1NgYlGGB-1Yxai717rW4M7TBTnUR3ebAElKz-WpnBDybkXoAlgbclhB6vjYi5usfMx-GdfaUf--vFPrYxi7VarrtocHi3qJuKGnpRzydY25cF-mVWbGx4TmIGmcT5uGOQygChPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
این هفته، گروهبان ارشد تفنگداران دریایی آمریکا از نزدیک شاهد نحوه تجهیز نیروهای مستقر در خاورمیانه به
قابلیت‌های پیشرفته پهپادی
توسط سنتکام بود.
تفنگداران دریایی به
کارلوس ای. رویز
، گروهبان ارشد تفنگداران دریایی، درباره استفاده تاریخی سنتکام از
سامانه‌های پهپادی تهاجمی یک‌طرفه کم‌هزینه
(نمونه آمریکایی شاهد) توضیح دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25125" target="_blank">📅 22:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25124">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دو منبع دیپلماتیک منطقه‌ای به i24 نیوز: احتمال دارد تهران یک حمله پیش‌دستانه را آغاز کند، به دلیل نگرانی از یک حمله آمریکایی
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25124" target="_blank">📅 22:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25123">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آتلانتیک:
احتمال دارد که ترامپ قبل از انتخابات میان‌دوره‌ای، دستور حمله دیگری به ایران را صادر کند
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25123" target="_blank">📅 22:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25122">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فاکس نیوز : خنثی شدن طرح تیراندازی در «مال آو آمریکا»
مقام‌های فدرال آمریکا اعلام کردند یک
طرح تیراندازی جمعی با الهام از داعش
که قرار بود مرکز خرید «مال آو آمریکا» در مینه‌سوتا را هدف قرار دهد، پیش از اجرا خنثی شد.
شیخدون عبداللهی محمد، ۱۸ ساله
، به گفته دادستان‌ها با داعش بیعت کرده و ابتدا قصد سفر به خارج از آمریکا برای پیوستن به این گروه را داشته است. بر اساس اسناد دادگاه، او قصد داشت در یک رویداد در
۲۴ اکتبر
تیراندازی کند و هدفش کشتن
۳۰ تا ۶۰ نفر
بود. اف‌بی‌آی پس از آن او را بازداشت کرد که طبق اسناد، وی از یک مأمور مخفی(آندر کاور)
یک قبضه AK-47 و ۲۰۰ گلوله
خریداری کرده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25122" target="_blank">📅 21:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25121">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خبرگزاری صدا‌وسیما : حمله مسلحانه به مقر انتظامی در گلشن
بنا بر اعلام منابع آگاه دقایقی قبل یکی از مقرهای انتظامی در شهرستان گلشن سیستان و بلوچستان مورد حمله مسلحانه قرار گرفت.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25121" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25120">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ درباره اینکه چرا شایسته دریافت جایزه نوبل صلح است:
من شاید جلوی
نابودی کامل جهان
را گرفته باشم، چون ایران هرگز سلاح هسته‌ای نخواهد داشت. اوباما این جایزه را گرفت، در حالی که هیچ کاری انجام نداد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25120" target="_blank">📅 21:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25119">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27b83a25ca.mp4?token=f3cVh5GaFXrLFukrRpxHcjwJwrQ5qHdBfE5n_YTdYs8-OMMwaU4EsD31-uLbMYreQwkA1pA1Yb_P9NUolkbVeLlSJoMbjWSw7iWGsOGjnGsJNgt-Y9c0LcGIroEckA3TetYnF6OEM_EXVeAcRVuyRBDT60Hi6QrBfGLY4MSeQRZI_Fme2Q5VAQTguji12-2mAh4_Z366fAYvqyzcO8AloPpi3nvoMHY5r7Z41GVAmdhe0VNDdiuOFUkielF-pKJYbO_emrxV7ELHg715Uy19lb0Z1XiQmXLwAmP6Zf9xgqv50H5qhQTgM4ygD7mFMEmgGYkzZNcWAzmfJI6x7fzsYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27b83a25ca.mp4?token=f3cVh5GaFXrLFukrRpxHcjwJwrQ5qHdBfE5n_YTdYs8-OMMwaU4EsD31-uLbMYreQwkA1pA1Yb_P9NUolkbVeLlSJoMbjWSw7iWGsOGjnGsJNgt-Y9c0LcGIroEckA3TetYnF6OEM_EXVeAcRVuyRBDT60Hi6QrBfGLY4MSeQRZI_Fme2Q5VAQTguji12-2mAh4_Z366fAYvqyzcO8AloPpi3nvoMHY5r7Z41GVAmdhe0VNDdiuOFUkielF-pKJYbO_emrxV7ELHg715Uy19lb0Z1XiQmXLwAmP6Zf9xgqv50H5qhQTgM4ygD7mFMEmgGYkzZNcWAzmfJI6x7fzsYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار فاکس نیوز: آیا طاعون در روسیه یک سلاح بیولوژیکی است؟
ترامپ: ما اینطور فکر نمی‌کنیم. به‌زودی متوجه خواهیم شد، اما فکر نمی‌کنیم که اینطور باشد
روس‌ها می‌گویند که این موضوع کاملاً تحت کنترل است
پیتر دوسی از فاکس نیوز: آیا همین حال و هوایی را که در آغاز کووید از چین داشتید، اکنون از روسیه در مورد طاعون هم حس می‌کنید؟
ترامپ: خب، چین زیاد چیزی نگفت و روسیه هم زیاد چیزی نمی‌گوید، اما آن‌ها می‌گویند که کنترل آن را به شدت در دست دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25119" target="_blank">📅 21:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25118">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/333de74250.mp4?token=V8UibPatoZFYtL4iG17cSHPV-hhcGJofiK3JYt7IbFR0Qg3wM4-dX6a3pvTN9RE4FpU3RKqSvLW1gwVPY1uMIkGTBqqmYSdULICvE5lGK8Tx0kwapuu-EQVTT9sqKWfTSBPtxgiGrnE1xOM-4fCtR4Q2uoPwvydnI_4824uJ6xksWDNgmfxquYxJ4kuDlhsb3Mv_MqKs9bv-QvieF09rVic7OdQ7no3Egd1J19rZ2csPCIky9BmAyM9E1KPOwmPHHbE8P660tN0kRKqsMLT1PfBlBn1LKTnBGRujRKyRwuj3oyCutaxfCiaqgwjoG8W75g3KJETJ7vtjrcf6jp1L-k8jii15wOtZcj9PMf1-iglrTcMKzboeXKsIl3k6ytdn87t05AbMPh5sc1MeQgpEBUtgKK955PFIUZE0p7GipoqD-MFSz5MRHhzBlAslhIUrvaqL66fwdKlhSsyG-fMAHGIHTAi1XyG_2VF1GY57AxVFTk_doI8yKanpcy8inBLATlezyDx-b1SxyRdo1ysbtu6E4GvbfzyqifXfcWFgZnO-f6iPlxRJx62sMlsfqdiur5OOjWlWZ0yi3cWuilpMlf1xDoHeF7ryxPfL_dRMko4xG_kzK2MQehI6zBgZouXZQ-pVopRS0aSHGcSI9K9l-mxQw2kmxrrLZbo7F-0mH_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/333de74250.mp4?token=V8UibPatoZFYtL4iG17cSHPV-hhcGJofiK3JYt7IbFR0Qg3wM4-dX6a3pvTN9RE4FpU3RKqSvLW1gwVPY1uMIkGTBqqmYSdULICvE5lGK8Tx0kwapuu-EQVTT9sqKWfTSBPtxgiGrnE1xOM-4fCtR4Q2uoPwvydnI_4824uJ6xksWDNgmfxquYxJ4kuDlhsb3Mv_MqKs9bv-QvieF09rVic7OdQ7no3Egd1J19rZ2csPCIky9BmAyM9E1KPOwmPHHbE8P660tN0kRKqsMLT1PfBlBn1LKTnBGRujRKyRwuj3oyCutaxfCiaqgwjoG8W75g3KJETJ7vtjrcf6jp1L-k8jii15wOtZcj9PMf1-iglrTcMKzboeXKsIl3k6ytdn87t05AbMPh5sc1MeQgpEBUtgKK955PFIUZE0p7GipoqD-MFSz5MRHhzBlAslhIUrvaqL66fwdKlhSsyG-fMAHGIHTAi1XyG_2VF1GY57AxVFTk_doI8yKanpcy8inBLATlezyDx-b1SxyRdo1ysbtu6E4GvbfzyqifXfcWFgZnO-f6iPlxRJx62sMlsfqdiur5OOjWlWZ0yi3cWuilpMlf1xDoHeF7ryxPfL_dRMko4xG_kzK2MQehI6zBgZouXZQ-pVopRS0aSHGcSI9K9l-mxQw2kmxrrLZbo7F-0mH_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل: حماس همچنان از بیمارستان‌ها برای فعالیت‌های تروریستی سوءاستفاده می‌کند:دو عضو حماس که از
بیمارستان کمال عدوان
در شمال نوار غزه خارج شده بودند، بامداد چهارشنبه شناسایی و کشته شدند. به گفته ارتش اسرائیل، یکی از آنها در حال
کارگذاری بمب‌هایی بود که از داخل بیمارستان به منطقه خط زرد منتقل شده بود
. فرد دوم،
محمد طموس
، تک‌تیرانداز شاخه نظامی حماس بود که هم‌زمان به‌عنوان
کارمند امداد و نجات
فعالیت می‌کرد. ارتش اسرائیل مدعی است حماس در هفته‌های اخیر از بیمارستان کمال عدوان برای فعالیت‌های نظامی و بازسازی توانمندی‌های خود استفاده کرده و این اقدامات را
نقض توافق آتش‌بس
می‌داند. تصاویر عملیات نیز توسط ارتش اسرائیل منتشر شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25118" target="_blank">📅 20:49 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
