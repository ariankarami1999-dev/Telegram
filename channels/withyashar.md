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
<img src="https://cdn4.telesco.pe/file/gXWM3fLObt5ePspFHClWkm199pIFyqwpoEsKqzrwaFXf3MUYw296b5NzIWAMwn9J4jNfFMy1INi3BR6eoi1eIRH3pWkUv_9-aGlO6LKEpZs3zMxOqa5XVp55DUXjcTkJA-sdqeje4ND2kisKzfC159xz8Ge0NKDEdDB-yGYWAtp8b8sRk1Dac4ffPSZGYQIj2hpfgPMeGiWUgB_5_oE922dLFhzgR5DgTtMXrMeK0OdkHg43IlWbL5jdXcs66Ml4TFEBVnOXqbKQsrbdxYswoqwKHBaLG7yFRr1NuztLyoUt-edrBXatV_yqNliiVcslkJZa4n_5ZQLtuyRU9EPcyQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 450K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 19:06:53</div>
<hr>

<div class="tg-post" id="msg-22684">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkI8BAQV1lz4TU59VNwivc-agJteHvjJoB4skegn5TW22195GF-mYk7PjT8QupNS2a3Lx60s9lK3ox-so6x6vKl2Z08Rt9G9zdEUXnhZ04Jbid7Lb8f1xOJxbciCl65nVV4Y_TEPCyQHABinIG6RjzVd4JRX8FeyYtSP4KjP8SuemD8kt4fk_vLST0qMd_VhAoEjcHzGOV6rKP0qxnIdr1WJ95D4Zgp7RswKqOOKk7_jIgxrSJHkYnLVPMdmO4inIZi3BBGvDXJe1zoBuLusGyfVbHDQaCLwPOUqGblGIGu4B_2Td91MKjzaQ4a_FCXBS23JCVznIPFdUmT1Wf4FjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : شهپادی که سپاه چندین سال به دنبالش بود و یک بار ۴ سال پیش اقدام به سرقت کرد ولی ناموفق ماند، توسط دیدبان اتاق جنگ شکار شد.
این یک شناور سطحیِ بدون‌سرنشین از نوع «Saildrone Explorer» است که شرکت آمریکایی سیل‌درون آن را طراحی و تولید کرده است. این شناور حدود ۷ متر طول دارد و با استفاده از یک بالِ سختِ بادبانی حرکت می‌کند؛ انرژی دوربین‌ها، حسگرها، سامانه ناوبری و ارتباطات ماهواره‌ای آن نیز از پنل‌های خورشیدی روی عرشه تأمین می‌شود. سیلدرون اکسپلورر برای مأموریت‌های طولانی‌مدت طراحی شده و می‌تواند ماه‌ها بدون خدمه در دریا باقی بماند. این شناور به دوربین، رادار، حسگرهای هواشناسی و اقیانوس‌شناسی، تجهیزات پایش سطح و زیر سطح آب و سامانه کنترل از راه دور مجهز است و داده‌ها و تصاویر را از طریق ارتباطات ماهواره‌ای به مرکز فرماندهی ارسال می‌کند. ناوگان پنجم آمریکا از سال ۲۰۲۲ استفاده از این شناورها را در خلیج فارس آغاز کرد؛ مأموریت اعلامی آن‌ها افزایش آگاهی دریایی، پایش تردد شناورها، جمع‌آوری اطلاعات محیطی و شناسایی فعالیت‌های دریایی در منطقه است. این شناور پیش‌تر نیز در خلیج فارس خبرساز شده بود؛ آمریکا اعلام کرد در
۲۹ اوت ۲۰۲۲، شناور پشتیبانی «شهید بازیار» متعلق به نیروی دریایی سپاه به یک فروند Saildrone Explorer متصل شد و آن را یدک کشید. طبق روایت آمریکا، پس از نزدیک‌شدن شناور و بالگردهای آمریکایی و چند ساعت پیگیری، طناب یدک‌کشی جدا شد و شناور بدون‌سرنشین رها شد؛ حادثه بدون درگیری نظامی پایان یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/withyashar/22684" target="_blank">📅 19:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22683">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دیدبان اتاق جنگ وسط تنگه هرمز شکار کرده
🤣
خبر تا دقایقی دیگر ….
🚨
🚨</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/withyashar/22683" target="_blank">📅 18:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22682">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آکسیوس گزارش داده بسیاری از جمهوری‌خواهان و دستیاران کاخ سفید، با وجود تردید فزاینده درباره تصمیم‌های سیاسی ترامپ، عملاً از تلاش برای تغییر نظر او دست کشیده‌اند و ترجیح می‌دهند از خواسته‌هایش پیروی کنند. یک مشاور قدیمی گفته است: «چرا زحمت بکشیم؟ رئیس اوست.» با نزدیک شدن به انتخابات میان‌دوره‌ای، نگرانی جمهوری‌خواهان از رویارویی با ترامپ بیشتر شده است؛ یک اهداکننده جمهوری‌خواه این وضعیت را چنین خلاصه کرده: «هرچه بخواهد، به دست می‌آورد.» در همین حال، نزدیکان ترامپ معتقدند نباید منتظر کاهش نفوذ او بود و هشدار داده‌اند که
حتی پس از پایان دوره ریاست‌جمهوری‌اش، ترامپ همچنان یک شخصیت سیاسی غالب باقی خواهد ماند
@WarRoom</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/withyashar/22682" target="_blank">📅 18:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22681">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نتانیاهو: در آستانه سال نو یهودی «روش هشانا» در ارتفاعات جبل‌الشیخ هستیم. پایینِ سرِ ما دمشق قرار دارد، اینجا لبنان است و آنجا بلندی‌های جولان. ما بر تمام این منطقه، از جبل‌الشیخ تا رود یرموک و از اینجا تا دریای مدیترانه، کنترل داریم؛ این سطح از کنترل کامل، بی‌سابقه است. این یکی از دستاوردهای بزرگ ماست. هنوز کارهایی باقی مانده است؛
مأموریت اصلی، شکست دادن جمهوری اسلامی در ایران است و ما به آن بسیار نزدیک شده‌ایم
. ما می‌دانیم که در نهایت تمام محور سقوط خواهد کرد. ما برای انجام این کار متعهد هستیم و آن را انجام خواهیم داد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/22681" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22680">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رویترز گزارش داد نفتکش سوخت‌رسان «Hercules Star» با پرچم جبل‌الطارق، در فاصله حدود ۱۷ مایل دریایی شمال‌غربی بندر میناء صقر در رأس‌الخیمه هدف یک پرتابه قرار گرفت و دچار آتش‌سوزی شد. آتش‌سوزی مهار شد و نفتکش سپس به لنگرگاه دبی بازگشت؛ خدمه این کشتی سالم گزارش شدند.
همچنین گزارش شده است که نفتکش «MKD Vyom» در آب‌های نزدیک عمان هدف قرار گرفت و
یک خدمه آن کشته شد
.
@WarRoom
یاشار : در خبر رویترز «یک کشته» مربوط به MKD Vyom است و نه هرکولس استار،  در تمام رسانه ها به اشتباه منعکس شده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/22680" target="_blank">📅 16:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22679">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ارم‌نیوز ‌امارات گزارش داده است که آمریکا در حال بررسی طرحی برای استقرار تفنگداران دریایی در برخی جزایر خالی از سکنه ایران در اطراف تنگه هرمز است. بر اساس این گزارش، در صورت اجرای طرح، جنگنده‌های F-35B مستقر روی ناو تریپولی وظیفه پشتیبانی هوایی از نیروهای آمریکایی را بر عهده خواهند داشت.
هدف احتمالی این طرح، ایجاد نقاط دیده‌بانی و پایگاه‌های لجستیکی برای نظارت بر تنگه هرمز و حفاظت از کشتی‌های تجاری عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/22679" target="_blank">📅 16:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22678">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqhIkbU8Rj8MPym_FLwt3Wx8eL0Cbz60UwC40noaSUT6P6BJA7hyV92aFOJMVzSp4DJLkb2TRgev36LWEj3j9riMDiaaIfx40k5C3PDosXtsCnaG5p5LgR5RWN_RypvYgCTbloqJ_gCCb28YP-x2Li12vOwuf2pEXas-kU7ctj5b1-FL7tIPzmFYP3v9s0XfSSZDakDsqe2vhJEtIJc7XhAYcAZUWE9cPBzToA-_u8pwmOVLDMSazNAWUaXGP3ovo6g1Y0IglQ8LVPIdXYNM8Z3Dxjmjn8jrC076tXPuV0-xZjf5nBDYqsH0dkPO8BXN-eS-IKNg0wdV5ov1r39cMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه ایران، ۱۱
شهریور ۱۳۸۲
@Warroom</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/22678" target="_blank">📅 16:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22677">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvFlZCkJJ7TxKL32Y3NMFMPZArniYDIQdu_67N723_EcmUpjc43LpJ9R2KcKrmRySCVfob5uPPuNQ9Pj1KY_vbUHt2aebSew-KDVhDaz3TiQVIFqXHIAKiUSCFCCJQL5-Ag2kjb5-oRn_hf9wZUjNhsiSfd6QYS_AYKrGvIhU1UP98hsJa27BRZCpce23em-JMjtq14wFObU3eMsoioI60mPhr5AhrO90JE4XRw_F8Zj9YMJuyOj1DvFQHgXN_XE_tuYyz096tuQRlj7DTQAYeztMaDRPKNRAlWZw8qW_jb7kCEJZBPOYFzc6rCFBiKDybnHakTSJTw-P-afYczJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو رعدنیاهو دیشب در آسمان تهران کلی بچه ها رو ترسوند
😁
@WarRoon</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/22677" target="_blank">📅 15:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22676">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e9f7b7cff.mp4?token=LrnwmJXvinObvwroBcha4JSFTU_jSWBPm8BEZ5J_XPZab5zcORlrq4QJdFYmtl6uwzpNpbwMzhFxGSV4pOrRg5M27uyrV_QTX5uYPLgZR1DwwzgRNUMq4yBYI1FRt0wS30bIeiwJNYeYN4nAiNCC76KkiLXwGtcag8uI1TbJgsxyLNbVwm_c6MoYEjWvDw-D01gDupHc3C9L0igH3Uq4-uykR1j9Eu5v0wiTdvTeBbwUtivHVDM2maNr1FzCC4WhxDLGyMjMW6Q56X-DILhxgQY_6oLFoFMxdmIfBemkRMvOS91pVGuQ4Xt11AiMNwaG7z68IAp2XGK0LNnIb4Gn6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e9f7b7cff.mp4?token=LrnwmJXvinObvwroBcha4JSFTU_jSWBPm8BEZ5J_XPZab5zcORlrq4QJdFYmtl6uwzpNpbwMzhFxGSV4pOrRg5M27uyrV_QTX5uYPLgZR1DwwzgRNUMq4yBYI1FRt0wS30bIeiwJNYeYN4nAiNCC76KkiLXwGtcag8uI1TbJgsxyLNbVwm_c6MoYEjWvDw-D01gDupHc3C9L0igH3Uq4-uykR1j9Eu5v0wiTdvTeBbwUtivHVDM2maNr1FzCC4WhxDLGyMjMW6Q56X-DILhxgQY_6oLFoFMxdmIfBemkRMvOS91pVGuQ4Xt11AiMNwaG7z68IAp2XGK0LNnIb4Gn6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در فیلم جدیدی که کانال چهارده از حملات دیشب به اردن منتشر کرده، در ثانیه اول واضح است که پدافند آمریکایی پر قدرت عمل کرده و «موشک قدر» جمهوری اسلامی را منهدم می‌کند و ذراتی که پخش می‌شود حاصل این مهار است و موشک خوشه‌ای در کار نبوده.
@WarRoom</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/22676" target="_blank">📅 15:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22675">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6GjzhNzchxKpvIT0E4EzFMTLoT2zJMY9JAD9asdmctwFHQ4ww-S6Z2nx6P2SISWuNmiUNQwXgQMNY7vX-hKDDwN49k9l8nALwKrJiQ-2JFZQDD-U3OVukbMCqAJJBWpNR5LIkSqfKE_L96wn4Ix3RkMi2y24p1bBxONIXUxiASH3seUGVw6gWsynZ5H4dOXvTROw3laeKLcu_ft9wl_p7JAMrIgw01ia140pOW-3q50nAXGifm2mWZsRmaPgxnr1ov9MUYykx5obRn6MZEf5KhyvpAPAVAck_2QYBlxR_O1TMfFtBprKj-Z01xdoPFPlbIqBuCJgTu_e3h7UpmdoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طالبان به ترامپ : ۷ میلیارد دلار سلاح‌ها آمریکایی بجا مانده اکنون متعلق به افغانستان هستند و ما آن‌ها را پس نخواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/22675" target="_blank">📅 15:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22674">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یک مقام آمریکایی:
تمام نیروهای آمریکایی در خاورمیانه در حالت آماده‌باش کامل قرار دارند، پس از حمله شب گذشته ایران ,
ما همه منتظر دستورات رئیس‌جمهور هستیم.
@WarRoom</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/22674" target="_blank">📅 15:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22673">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سی‌ان‌ان: تصاویر ماهواره‌ای از افزایش چشمگیر ساخت‌وساز در سایت به‌شدت مخفی «کوه کلنگ گزلا» در نزدیکی نطنز خبر می‌دهد؛ محلی که ممکن است به تأسیسات غنی‌سازی اورانیوم یا یک مرکز امن هسته‌ای تبدیل شده باشد @WarRoom</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/22673" target="_blank">📅 15:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22672">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سخنگوی سپاه: ناو هواپیمابر آمریکا را در فاصله ۵۰۰ کیلومتری هدف قرار دادیم
@WarRoom</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/22672" target="_blank">📅 15:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22671">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شروط جدید جمهوری اسلامی برای توقف جنگ اعلام شد
سخنگوی سپاه: اگر دشمن خواهان پایان این وضعیت است، باید:
۱- ضمن توقف کامل جنگ،
۲- از تهدید مجدد دست بکشد،
۳- ارتش رژیم صهیونیستی از لبنان عقب‌نشینی کند،
۴- محاصرهٔ یمن پایان یابد،
۵- ۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود
۶- و از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.
@WarRoom</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/22671" target="_blank">📅 15:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22670">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">۱۰ دقیقه پیش چندین گزارش داشتم از‌صدای انفجار‌ از تنگه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/22670" target="_blank">📅 14:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22669">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حداد عادل بود نه لاریجانی
😁</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/22669" target="_blank">📅 14:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22668">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHBjBAwDx8boJPhFMl7LUhURzKFWJCVOlEGGHuzcEy69RGTgIVPYyDQT0HVT_0mVjy5xXracOTkDpy6YC2F5Hvzko2WcoyvlcDFI1tUoSXDxwC7T9lg_sz9PayLlJQju1UmtH15KsKysSX7X8IOFGwX-fMqyP53kNmLuQdAx8VCVRtSUEM3AZOBvh18b7hB_HCvO_nRvljmdy4YizINu0i9QzsJpHQJfHDTo_6d1xf070s0BcU38qHVIprk2I7iBXOoxhSyP26YNQLrXjcrtO2_9q1nd0aFMWwbHr1963InfivklDaEraNGMHx5ofTVVf0Kx8PPZ1Yl4NnyyT4RPQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریای بریتانیا UKMTO: گزارشی از وقوع یک حادثه در ۲۸ مایلی دریایی جنوب‌شرقی الفاو عراق در فاصله‌ای نزدیک از آب‌های کویت دریافت کرده است. ناخدای یک نفتکش اعلام کرده که شناور با یک پرتابه ناشناس مورد اصابت قرار گرفته است. خدمه در سلامت هستند
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22668" target="_blank">📅 14:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22667">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kib2VnWMlEemvm3xhBfTqjs2W9eMavS5k2qjhps7hfsMYN_kaASdumsJgM2Hp6etaRFCPL8BEYGrwKArbtiaV6YvOhNJBmSH5gTBAU-d4oFsft_XcVeGBxyanp1h_OxCQN6WxfVl_0RQlgv11qiKSZNfhXtIx8q5-wlueWzIr-OPhrXvcRWFa7UiE7xZVIKLGFbPPz9ku1oJzCm53qt3TWLnPrG4l9A1jtFSug8xCdn3AdHp7MA0bS02myHBAKt8dZ0rDcleJtPenwuouxf45alS-EpMGoLCw_ynAWM-ghUt-FLfOB00dWDU9PjatoTzCN57rwUyPWXmbB3KLgALHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: تصاویر ماهواره‌ای از افزایش چشمگیر ساخت‌وساز در سایت به‌شدت مخفی «کوه کلنگ گزلا» در نزدیکی نطنز خبر می‌دهد؛ محلی که ممکن است به تأسیسات غنی‌سازی اورانیوم یا یک مرکز امن هسته‌ای تبدیل شده باشد
@WarRoom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/22667" target="_blank">📅 14:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22666">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">العربیه : نیروهای مسلح یمن رسماً اعلام کردند که طی عملیات اخیر خود، تعدادی از سرکردگان شبه‌نظامیان حوثی، از جمله طراحان اصلی حمله به تنگه استراتژیک «باب‌المندب» را کشته و شماری دیگر را به اسارت درآورده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/22666" target="_blank">📅 14:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22665">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کانال ۱۴ اسرائیل در یک افشاگری ، مدعی شده قالیباف در یک جلسه غیرعلنی گفته تحریم‌های آمریکا اثرگذار بوده و خسارات ناشی از جنگ تقریباً جبران‌ناپذیر است و گفته «جمهوری اسلامی در آستانه فروپاشی است». بر اساس این ادعا، قالیباف همچمین اضافه کرده: «همه ما میلیاردها دلار دزدیده‌ایم، اما دیگر نمی‌توانیم مردم را برای مدت زیادی کنترل کنیم.» او همچنین از رویکرد تندروانه احمد وحیدی، فرمانده سپاه، انتقاد کرده و گفته «پافشاری و رویکرد او، ایران را به خطر انداخته».
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22665" target="_blank">📅 13:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22663">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حقیقت یاب سنتکام : هیچ ناو جنگی نیروی دریایی آمریکا مورد اصابت قرار نگرفته است؛ تمام حملات تلاش‌شده از سوی سپاه شکست خورده‌اند. در همین حال، نیروهای آمریکایی تنها در هفته گذشته با موفقیت
۱۰ نفتکش ایرانی
را منهدم کرده‌اند. این شناورها بخشی از یک شبکه چندمیلیارددلاری موسوم به «ناوگان سایه» بودند که برای تأمین مالی سپاه پاسداران فعالیت می‌کرد و ایران قادر به دفاع از آنها نیست
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22663" target="_blank">📅 13:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22662">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یک مقام آمریکایی به الجزیره:
پاسخ ایران در برابر پدافند هوایی و موشکی یکپارچه ناکارآمد بود.
موشک‌های شلیک شده توسط ایران به سمت اردن منجر به تلفات جانی در میان نیروهای آمریکایی نشد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22662" target="_blank">📅 13:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22661">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دلار ۲۳۲،۱۰۰ تومان (سقف تاریخی)
بازار آزاد ۲۳۶-۲۳۸ هزار تومان
تتر ۲۳۱،۰۰۰ تومان(سقف تاریخی)
نفت برنت ۱۰۰.۴۰$
انس جهانی طلا ۴،۳۹۸$
۱ ظهر تهران
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22661" target="_blank">📅 13:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22660">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رویترز گزارش داده بنیامین نتانیاهو در آستانه مهلت ثبت فهرست‌های انتخاباتی، برای متحدکردن احزاب راست‌گرا تلاش می‌کند. انتخابات پارلمانی اسرائیل قرار است ۲۷ اکتبر (۵آبان)برگزار شود @WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22660" target="_blank">📅 12:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22659">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رویترز گزارش داده بنیامین نتانیاهو در آستانه مهلت ثبت فهرست‌های انتخاباتی، برای متحدکردن احزاب راست‌گرا تلاش می‌کند. انتخابات پارلمانی اسرائیل قرار است ۲۷ اکتبر (۵آبان)برگزار شود
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22659" target="_blank">📅 12:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22658">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcnXAHRayAHAn8vMg-2RXyPYpSx9LR6WTuivnJAPIeBkseJKoWAl_O2VSyKDiUeafrUs3Eoe3kC9vpANcD6M9tdopTY6fU1boWpcunEgmiXUVYYs957rouA0RlcoyTXm-hkdf8T6vQvCdAud-FYuf7gsjMXMUTHupu_nqt_hjRS44UYc80frFAlA-ToNkSZdpG65s3yJB3TQo3CNCG6jtkKK3gw8rZwxc09QX7eklDcCCf3wg2sI3v6MC4knMGjCIZHl_Vg4L3nXiBoi6TdaogIWRiEhXhnlqMthtQnrzthsoxQXyIjC3cV7kU6JgK1Z8uZHqYGVxc2wGqasM3hCvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریایی بریتانیا (UKMTO) با تاخیر گزارشهایی از چندین مورد کشتی تجاری در شمال خلیج فارس و خلیج عمان دریافت کرده است.
گزارش‌ها حاکی از آن است که این کشتی‌ها به عنوان بخشی از فعالیت‌های نظامی دیشب در منطقه، هدف آتش‌سوزی قرار گرفته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22658" target="_blank">📅 12:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22657">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رویترز گزارش داده هزینه بیمه و ریسک جنگ برای نفتکش‌هایی که از هرمز عبور می‌کنند به‌شدت افزایش یافته و هزینه بیمه جنگی در برخی موارد به حدود ۶ درصد ارزش محموله رسیده است؛ موضوعی که باعث شده برخی شرکت‌ها از عبور از این مسیر صرف‌نظر کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22657" target="_blank">📅 12:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22656">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آسوشیتدپرس گزارش داده ایران در حال شکل‌دهی به شبکه‌ای تازه از گروه‌های نیابتی، به‌ویژه حوثی‌های یمن و گروه‌های مسلح عراقی، برای افزایش فشار بر متحدان آمریکا در خلیج فارس است. بر اساس این گزارش، نشانه‌هایی از هماهنگی میان حوثی‌ها و گروه‌های عراقی دیده شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22656" target="_blank">📅 11:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22655">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دلار ۲۳۰،۱۰۰ تومان (نرخ تاریخی)
بازار آزاد ۲۳۵-۲۳۷ هزار تومان
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22655" target="_blank">📅 11:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22654">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe589f1aee.mp4?token=jBTci9U3CKMuJMaOCXT24M4Ue3bhQwFrAnMuDsNHpjUV5SMno4QCVNXFDJdPIzQwsTGLkbrRubvSN6ZXOowA2LXypaxXg7tlTS-i4TCeu8XNYhSpyQGfmUcbypVNp5O6RXJOiNxKorqS3HRyCzuKkSoiIfqE6QAzSxWyLCuJ3TSJ1dwkUqsWwxe6nsgaSF_-Q3YNsKb8XCfpYkfYpc1J7oT7fH-voCZOmVekubZyC8irgtSw-tY_L8rJAy43KLRZlOqrPr6FSuuVyUNhN8jbQbqrKRSfcYZ19WHyvlr19JPfuac1966yVRnGEfjJZC7CBn9_St1Vx6vQ0KyGyPSAUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe589f1aee.mp4?token=jBTci9U3CKMuJMaOCXT24M4Ue3bhQwFrAnMuDsNHpjUV5SMno4QCVNXFDJdPIzQwsTGLkbrRubvSN6ZXOowA2LXypaxXg7tlTS-i4TCeu8XNYhSpyQGfmUcbypVNp5O6RXJOiNxKorqS3HRyCzuKkSoiIfqE6QAzSxWyLCuJ3TSJ1dwkUqsWwxe6nsgaSF_-Q3YNsKb8XCfpYkfYpc1J7oT7fH-voCZOmVekubZyC8irgtSw-tY_L8rJAy43KLRZlOqrPr6FSuuVyUNhN8jbQbqrKRSfcYZ19WHyvlr19JPfuac1966yVRnGEfjJZC7CBn9_St1Vx6vQ0KyGyPSAUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقال تانک از نجف آباد اصفهان به جنوب
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22654" target="_blank">📅 11:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22653">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">قیمت نفت با رسیدن به ۱۰۰ دلار در بالاترین سطح از اردیبهشت امسال قرار گرفت
وقایع شب گذشته در تنگه هرمز کافی بود تا سقف هفته‌های اخیر نفت شکسته شود.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22653" target="_blank">📅 11:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22652">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/847f998c3f.mp4?token=Mjti-r586keYWRn75cPGfNhfx9LrvUE11ExCM7p-A-uJNDaEPYNmerfdffkU3enBcd65RR2mhZAiSoA-B5G1zIUgRlO42gvCbfDiQ9w_xwX-AMPnw_spRMxfqt4m84eNTXqzw7b-o4bJZZCtVNTMm3udydCCr0aMpMqhDmDjPQxP1zjel4PkPQnsjz9h6w6HId-DRznd5SO7XQoZTdaz22qPDy9sz0LnAosoLOzzIXJK9RJHfC_shBXOKbu0Fym92k53UGx4x-nOQWs5cvlQZFUR6BsZF_vgosJCMm22JTVOocD8fTxZcFrzvOGFwQFhogYUCvaUKRvvC_sO1E-13Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/847f998c3f.mp4?token=Mjti-r586keYWRn75cPGfNhfx9LrvUE11ExCM7p-A-uJNDaEPYNmerfdffkU3enBcd65RR2mhZAiSoA-B5G1zIUgRlO42gvCbfDiQ9w_xwX-AMPnw_spRMxfqt4m84eNTXqzw7b-o4bJZZCtVNTMm3udydCCr0aMpMqhDmDjPQxP1zjel4PkPQnsjz9h6w6HId-DRznd5SO7XQoZTdaz22qPDy9sz0LnAosoLOzzIXJK9RJHfC_shBXOKbu0Fym92k53UGx4x-nOQWs5cvlQZFUR6BsZF_vgosJCMm22JTVOocD8fTxZcFrzvOGFwQFhogYUCvaUKRvvC_sO1E-13Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : نفتکش «M/T Riesco» پنجمین نفتکش ایرانی که امروز هدف حمله آمریکا قرار گرفت پس از حمله در دریای مکران (عمان) غرق شد.چهار نفتکش دیگر بر اثر اصابت موشک به موتورخانه‌هایشان از کار افتادند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/22652" target="_blank">📅 05:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22651">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مقام آمریکایی ‌به رویترز گفت: «وضعیت تمامی نیروهای آمریکایی مستقر در اردن مشخص است و آنها سالم هستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22651" target="_blank">📅 04:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22650">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گزارشهای بسیار از صدای انفجار در کنگان ، انگار از طرف بندر دیر بوده
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/22650" target="_blank">📅 04:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22647">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">https://www.instagram.com/s/aGlnaGxpZ2h0OjE4MDk0NzgyMzU1OTg1NTY1?story_media_id=3824690341744932317&stkn=MWF3bWE3bnlhMWkwcw==</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22647" target="_blank">📅 03:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22646">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22646" target="_blank">📅 03:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22645">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22645" target="_blank">📅 03:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22639">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ارتش اردن : ایران در جریان حمله به پایگاه هوایی موفق السلطی، ۲۰ موشک شلیک کرده و پدافند هوایی این کشور ۱۸ موشک را رهگیری و منهدم کرده است، در حالی که دو موشک باقی‌مانده از «مراکز جمعیتی» دور افتاده‌اند.
هیچ تلفاتی در نتیجه این حمله گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22639" target="_blank">📅 03:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22638">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpzKpZuY9w8h2tJoFLFVUbzxInL3fA2loj_HkU7Lyy005Y4UemhGgT3YG7wkccRSzMIu7QHJZnujHmWhtPk6nrRyEXeduLOZ0bURapKaE2I8UcY3R_2oYmDdhVhqrxuX-VlyUhaSpbPZryYQCre-Gax938z0-CmH6SCiESp2mz12e9GUk8Agpc3exII08CgSRF-v9S4Cz_dfy1mMUlM6D_6QFqEdd9hARKlIlvOWH9_qPqbuVbKnNkxaaT5saEi-R7iNWErczCRDFRwFneMM0_vNaHIbpbwU6nalBT7T6vPsH5E9fDV1SI1dEXBuiFhF6r4lJTLNLUXI97g_3T1o5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران اعلام کرد در واکنش به اقدامات آمریکا علیه نفتکش‌ها و شناورهای ایرانی، نیروی هوافضای سپاه با موشک‌های بالستیک به دو ناوشکن آمریکایی
DDG119 - USS Delbert D. Black و
DDG53 - USS John Paul Jones
حمله کرده است. سپاه مدعی شده این دو ناوشکن که به موشک‌های کروز و سامانه پدافندی Aegis مجهز هستند، در این حمله آسیب قابل‌توجهی دیده‌اند. همچنین تأکید کرده به اقدامات آمریکا پاسخ خواهد داد و نسبت به «خطای محاسباتی» هشدار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22638" target="_blank">📅 02:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22637">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">«تانکر دریا» در لنگرگاه خارگ در آتش میسوزد @WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22637" target="_blank">📅 02:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22636">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22636" target="_blank">📅 02:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22635">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ویدیو حملات به اردن توسط سپاه
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22635" target="_blank">📅 02:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22634">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22634" target="_blank">📅 02:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22632">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پرتاب موشک جدید از‌ تبریز
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22632" target="_blank">📅 02:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22631">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بیانیه شماره ۱۳ سپاه: آشیانه تعمیر و نگهداری، آماده سازی و محل استقرار جنگنده های F-35 ،F-16 ،F-15 و شلتر جنگنده ها مورد هدف قرارگرفت
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22631" target="_blank">📅 02:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22630">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/541f997a69.mp4?token=Tx6THX9xBkCC9N7Ehk091XApc6gt6x6Xffne1J1eNNKS7ggqQt7TXogpbhwPZGSdixdrhuQy57gwY_QzNOrKHkYs-Y-LX-t-4ddT_bMUKT8NssyjK0K3hB46-KPREjOyIFm1A61ZM4KW33iwljb7bxCdchlMDARD7qDLGdkjRoEELiLayFclhUbANzj1c-XQO7CtJ4c0qWXfKCMC-nqEhSHeIYFwp0j6s5cRxaYoOsCXW1-57UuuODCKAeQ-UPDEvWkjKdcI35HGPgPaybBdM_0JOVEyW9oI-16nRUFyCe0e8Bi89diCRIEL3ZYvrc_vvTkTCkI9wLQ2AMUVZ-pnKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/541f997a69.mp4?token=Tx6THX9xBkCC9N7Ehk091XApc6gt6x6Xffne1J1eNNKS7ggqQt7TXogpbhwPZGSdixdrhuQy57gwY_QzNOrKHkYs-Y-LX-t-4ddT_bMUKT8NssyjK0K3hB46-KPREjOyIFm1A61ZM4KW33iwljb7bxCdchlMDARD7qDLGdkjRoEELiLayFclhUbANzj1c-XQO7CtJ4c0qWXfKCMC-nqEhSHeIYFwp0j6s5cRxaYoOsCXW1-57UuuODCKAeQ-UPDEvWkjKdcI35HGPgPaybBdM_0JOVEyW9oI-16nRUFyCe0e8Bi89diCRIEL3ZYvrc_vvTkTCkI9wLQ2AMUVZ-pnKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه، درباره ایران:
ایران همچنان به تلاش برای حمله به کشتی‌های نیروی دریایی ایالات متحده ادامه می‌دهد و هر بار که این کار را انجام می‌دهند یا سعی در انجام آن دارند، نفتکش‌ها را از دست می‌دهند.
امروز دوباره شاهد این موضوع خواهید بود.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22630" target="_blank">📅 02:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22629">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">شبی پر خرج برای رژیم جمهوری اسلامی
سنتکام : ایران از این نفتکش ها به عنوان بخشی از یک شبکه مخفی چند میلیارد دلاری برای تامین مالی سپاه پاسداران و عوامل ایرانی در منطقه استفاده می کند.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22629" target="_blank">📅 02:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22628">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سنتکام : ۵ کشتی زدیم  نیروهای سنتکام در ۸ سپتامبر، پس از آنکه سپاه پاسداران انقلاب اسلامی طی دو روز گذشته دو بار یک کشتی جنگی نیروی دریایی ایالات متحده را با موشک‌های بالستیک هدف قرار داد، پنج کشتی نفتکش ایرانی را منهدم کردند. کشتی جنگی ایالات متحده با موفقیت…</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22628" target="_blank">📅 02:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22627">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22627" target="_blank">📅 01:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22626">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سنتکام : ۵ کشتی زدیم  نیروهای سنتکام در ۸ سپتامبر، پس از آنکه سپاه پاسداران انقلاب اسلامی طی دو روز گذشته دو بار یک کشتی جنگی نیروی دریایی ایالات متحده را با موشک‌های بالستیک هدف قرار داد، پنج کشتی نفتکش ایرانی را منهدم کردند. کشتی جنگی ایالات متحده با موفقیت…</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22626" target="_blank">📅 01:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22625">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اتاق جنگ با یاشار : تمام اطلاعات و تحلیل ها و نام کشتی ها درست خبر رسانی ، پیشبینی و تحلیل شد و با اختلاف چندین ساعته امشب به اطلاع شما رسید !
🙌🏾
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22625" target="_blank">📅 01:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22624">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سنتکام : ۵ کشتی زدیم
نیروهای سنتکام در ۸ سپتامبر، پس از آنکه سپاه پاسداران انقلاب اسلامی طی دو روز گذشته دو بار یک کشتی جنگی نیروی دریایی ایالات متحده را با موشک‌های بالستیک هدف قرار داد، پنج کشتی نفتکش ایرانی را منهدم کردند. کشتی جنگی ایالات متحده با موفقیت از حملات ایران جان سالم به در برد و به گشت‌زنی در آب‌های منطقه‌ای ادامه داد. هیچ پرسنل آمریکایی آسیبی ندید.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22624" target="_blank">📅 01:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22623">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/withyashar/22623" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اخطار خلبان جنگنده آمریکای به کشتی HORIZON برای تخلیه موتور خانه در ۱ دقیقه
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22623" target="_blank">📅 01:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22622">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0NvqLkWbRUo8s6vC0RiIB-5B2UubPOXvcGJCUt-btKY6LDQzC8Hj2Ib9XmvbQF7rtpPXKwnMsJZR5mBzBUJVVhg6BUAzsUNXzI0I7Dgjp11P1NJazFxRYWz_EVP5O8OvLTLA6gZ1NlSnf8ohpLgQLLsYgQNtMG9l8cXdnma9WcJpt7_YcMQoMRdfKyDp-dRmYbwSukFXzHYhvCh74-hEhbfYeWQZ9725SgyndgsWQFmwS2Jf0kZZCeDCcFa9JSaAT4XIRR29Py1vDmyfKIWFKx7H3RB08ulABZkisrrKUunxs6QaC_bm7qA3tpQkpT_h_3ScSCD1yYtCCNF083q4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی دیگری‌که امشب هدف قرار‌گرفته احتمالا
HORIZON
است که با نام هرمز هم شناخته میشود با کال ساین 9hek9 که به نظر میرسد مربوت به امپراتوری Hektor  همان حسین پسر شمخانی باشد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22622" target="_blank">📅 01:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22619">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تنها خدای واقعی زمان است</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22619" target="_blank">📅 01:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22618">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bxk_KYlPUH2Px4b7Cgte59NyOgUm0kOM6YCR8zr_f_HLjq7ifpNDyqsxcFsUZs62koj2Bdcfc8HglUE1SsJqFgTUz8IRJluNnBPCJYY-RxyGrFsnplWczDL7jXypH80It3w4Tz2UVTVldqli9fg56JQr0g0cJwM4QAu0vN47-fWA-OHAxaqCobv552v9C4-gdSzrln93iI-_uOa6sV2BLBc5BhNmXRboyN5CdALrLR7R5j6wjwi9zrTC3wvdh0M7htJ87OMGloBMnJOq5vOieH_iNglwJYMjQXWk7TE-XVMSu1ah9SMQR5pwpfNw1wN7RaMq-Rxrcgb2fegb8LOxiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بروجرد پرتاب موشک ناموفق بود و ترکید !!!
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22618" target="_blank">📅 01:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22617">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff90ac3f79.mp4?token=Xp5U3J9b64q6OK12sKC_m14PCMn5K_0qaiytiTugxzb2WKzWwbn1erOLKlV2pGTpxleamKiHP0Nv-3EoVpqkMeDn7B9mvgBnOMew2ONjJOl_YPKHbp68mxql0-i0LUxZXp2bgtLEXfLKARX6jEuyOKVrjdF6Ytk4RvErjTV8zqflSV0fa0FuO7cSIZEb1Lo2J22yQcbpxfmqVxJdExbTuyIGIkDdwbcvb77hnbknk6zrs1OxUE9EooGkE1t5rTxB8E90_Jrcm91NZK5hNE9QvnzOm_6GB7jhuBy4Zx_dIQivWkvBixVyhaj8yf7rviJ9YQtMtFi6CKlXx7qemfPgAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff90ac3f79.mp4?token=Xp5U3J9b64q6OK12sKC_m14PCMn5K_0qaiytiTugxzb2WKzWwbn1erOLKlV2pGTpxleamKiHP0Nv-3EoVpqkMeDn7B9mvgBnOMew2ONjJOl_YPKHbp68mxql0-i0LUxZXp2bgtLEXfLKARX6jEuyOKVrjdF6Ytk4RvErjTV8zqflSV0fa0FuO7cSIZEb1Lo2J22yQcbpxfmqVxJdExbTuyIGIkDdwbcvb77hnbknk6zrs1OxUE9EooGkE1t5rTxB8E90_Jrcm91NZK5hNE9QvnzOm_6GB7jhuBy4Zx_dIQivWkvBixVyhaj8yf7rviJ9YQtMtFi6CKlXx7qemfPgAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیرجه موشکهای خوشه ای بر روی اردن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22617" target="_blank">📅 01:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22616">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سپاه به اردن موشک خوشه ای زد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22616" target="_blank">📅 01:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22615">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7a6210ca1.mp4?token=nnLIpJvFiyCVGRCZ6-XzO0J8F5A3X-5Zj6uaVRn90vrhyzXV3xCvA6jhhYxnK1JfCblFrE9lg-_jd-XN6wzvOFXTsSvt3d3_3IIuBKI-z9I-SvPM7WK0MoG3irebChvbLPmqn3ln7wgPAvf34HzgrkHzINDLKUTSve1mg-MnG1cCWe7ddwrddlgHsfl8VDfhXV9sjreVgorlc9ZPwmXhkGbPT9N-KaNGePHNU21QkBcVBJo_vSFK4-1Q5BxkWaf4auXMUofRWh-Sh4ekgYGvaiY5wo1hrfvpgrgJEOn4CTwev2jEbnjywszPnI0au-Q5uwY8YkhzDhP8eU7SRRx7yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7a6210ca1.mp4?token=nnLIpJvFiyCVGRCZ6-XzO0J8F5A3X-5Zj6uaVRn90vrhyzXV3xCvA6jhhYxnK1JfCblFrE9lg-_jd-XN6wzvOFXTsSvt3d3_3IIuBKI-z9I-SvPM7WK0MoG3irebChvbLPmqn3ln7wgPAvf34HzgrkHzINDLKUTSve1mg-MnG1cCWe7ddwrddlgHsfl8VDfhXV9sjreVgorlc9ZPwmXhkGbPT9N-KaNGePHNU21QkBcVBJo_vSFK4-1Q5BxkWaf4auXMUofRWh-Sh4ekgYGvaiY5wo1hrfvpgrgJEOn4CTwev2jEbnjywszPnI0au-Q5uwY8YkhzDhP8eU7SRRx7yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحدید سپاه : مرتبط با آمریکا، در منطقه تنگه هرمز و خلیج فارس شما در معرض هدف قرار دارید دستور میدهیم که خدمه و مهمانان خود را تخلیه کنند اگر تمایل دارید [در اینجا بمانید]، مسئولیت حفظ امنیت خود و خدمه‌تان بر عهده خود شماست.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22615" target="_blank">📅 01:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22614">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d364bd4e.mp4?token=Zuc3bMYHuk8g-zA3WG_09Umx8MTwHyFRFLsUAOhdSlDsApCyu8xNn656TqOwQ610YICbGkrLt7aXOIOGUX3mhnVGaoz8K23Ml6rjJoziW2qfjFn8fxBE5cNiH0tYYGb23aviAg9iN1xO1vhT22kMn2Mp85KFKjcyloLFgRImUQUAyeoEkkg7y3w_nF1xnjZDM0NLPdLNjgLCjKhtlpcrSqp2Lb9zc2dQPUH184RuwxJKMqeY-Gb3uWhHdE3TTfsoq7NUrd0wHOBtWbaksHiDOQzUzkmgzA7mPL2A_AWYVEmv9aWvxhU1JfHeEoGKN55fdyj-LFgKcz8CgEtWzeeYqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d364bd4e.mp4?token=Zuc3bMYHuk8g-zA3WG_09Umx8MTwHyFRFLsUAOhdSlDsApCyu8xNn656TqOwQ610YICbGkrLt7aXOIOGUX3mhnVGaoz8K23Ml6rjJoziW2qfjFn8fxBE5cNiH0tYYGb23aviAg9iN1xO1vhT22kMn2Mp85KFKjcyloLFgRImUQUAyeoEkkg7y3w_nF1xnjZDM0NLPdLNjgLCjKhtlpcrSqp2Lb9zc2dQPUH184RuwxJKMqeY-Gb3uWhHdE3TTfsoq7NUrd0wHOBtWbaksHiDOQzUzkmgzA7mPL2A_AWYVEmv9aWvxhU1JfHeEoGKN55fdyj-LFgKcz8CgEtWzeeYqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ قم حرم زیارت بود که موشک پرتاب شد
😂
✌🏼
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22614" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22613">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21c8f0d7d.mp4?token=ipcqjvFnTjZZDuNxfJ4dhfWf5YAXBusN-P70BRGf0Re4VaUSHy8ZWaOKCh-W3pOGkdz3XgfNgYxV3ZFBH9gjl-I63Huu1JQb5dAfGjoS1Yx8RPBlJdKsSU94QvYt5V5j7SqtcT6HGwFKQGS2eXlr2bwQAXJ0AHxHcxCccPRIQQEUYudzTr4AK1iuS_sgBW4FrvHFS4gYZOY_P8EdEsQ6vqX_lBDS119iKoB6wbG7U-J2UnVlh1cfYtzltJr2XEFebN-ruEtx3yUdyaNlV0WDARQVm2yDF_fPsZaelkeMY3hmMPNl_expBTFwn8gSxy8fkt6sy-ANJE89ulMZUChXhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21c8f0d7d.mp4?token=ipcqjvFnTjZZDuNxfJ4dhfWf5YAXBusN-P70BRGf0Re4VaUSHy8ZWaOKCh-W3pOGkdz3XgfNgYxV3ZFBH9gjl-I63Huu1JQb5dAfGjoS1Yx8RPBlJdKsSU94QvYt5V5j7SqtcT6HGwFKQGS2eXlr2bwQAXJ0AHxHcxCccPRIQQEUYudzTr4AK1iuS_sgBW4FrvHFS4gYZOY_P8EdEsQ6vqX_lBDS119iKoB6wbG7U-J2UnVlh1cfYtzltJr2XEFebN-ruEtx3yUdyaNlV0WDARQVm2yDF_fPsZaelkeMY3hmMPNl_expBTFwn8gSxy8fkt6sy-ANJE89ulMZUChXhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب یک دسته موشک از‌خمین
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22613" target="_blank">📅 01:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22612">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a496403d.mp4?token=Zk6K3hdO7BWfWe59t1BRd8AN5giUJ9i1wJySBzU7Zlnj61dUhBmlRpqz4ZehCQM_sr-5OaHZ2G3MiFUWtI16I-6cVDdlCrvLOnQAysk6dirnDFiWAkQJQIBy5pSEG8i5grSBnGHqydpGCegT0cUVnZfHsM3t1doRgT4BPVWijyBRMTeAxa11YegS2js6ZyWIjUQKTkVdaRHNjfW7iJU1g1e5OeZbbFFXBgsMJegZpat8uyed3FZNVhVFbb3AyuRHWGv1mcp9S3afpMgX9srKMDI828Ly5rwjYTCMJYLmfP7Yg4l8WPun_0LomR4HqikDGEZYezlyLP6UYH7Z5BF9Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a496403d.mp4?token=Zk6K3hdO7BWfWe59t1BRd8AN5giUJ9i1wJySBzU7Zlnj61dUhBmlRpqz4ZehCQM_sr-5OaHZ2G3MiFUWtI16I-6cVDdlCrvLOnQAysk6dirnDFiWAkQJQIBy5pSEG8i5grSBnGHqydpGCegT0cUVnZfHsM3t1doRgT4BPVWijyBRMTeAxa11YegS2js6ZyWIjUQKTkVdaRHNjfW7iJU1g1e5OeZbbFFXBgsMJegZpat8uyed3FZNVhVFbb3AyuRHWGv1mcp9S3afpMgX9srKMDI828Ly5rwjYTCMJYLmfP7Yg4l8WPun_0LomR4HqikDGEZYezlyLP6UYH7Z5BF9Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از تبریز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22612" target="_blank">📅 01:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22611">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bbb709c43.mp4?token=jZQq0-Q98EJxwDyK8Al0YhWvujuFMG2RWeCF4D-Hus3mbR3llhCA7SpF8xTGVp-_Ty3HfEAXeZWbOPd1gMLh_1ekfnQwYxpa2UAfT2OwsveHmsZbbQ4uuZnUcUHMTFyXuIOuIEk3CBHkAHd9r9GrZ_FlNAnvxJLbp-sEFk-Uox7a6TofkNNL3i000Gi7VJwGEKKOTlRYLxBjxD7r94Pja9zf9SQA03y3RRjnhpMfW12vqvaTTqYj1ys9DrAU73cAOaAC5Kg1NQJrmFoz3xAUyGrcmCpEftj06_VM02ox1Aitin2Zk5JYFO0umlhaOikBumKeOT8xoeQidrpLn15c-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bbb709c43.mp4?token=jZQq0-Q98EJxwDyK8Al0YhWvujuFMG2RWeCF4D-Hus3mbR3llhCA7SpF8xTGVp-_Ty3HfEAXeZWbOPd1gMLh_1ekfnQwYxpa2UAfT2OwsveHmsZbbQ4uuZnUcUHMTFyXuIOuIEk3CBHkAHd9r9GrZ_FlNAnvxJLbp-sEFk-Uox7a6TofkNNL3i000Gi7VJwGEKKOTlRYLxBjxD7r94Pja9zf9SQA03y3RRjnhpMfW12vqvaTTqYj1ys9DrAU73cAOaAC5Kg1NQJrmFoz3xAUyGrcmCpEftj06_VM02ox1Aitin2Zk5JYFO0umlhaOikBumKeOT8xoeQidrpLn15c-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون پرتاب دو موشک از اصفهان
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22611" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22610">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گزارش پرتاب موشک از کرمانشاه @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22610" target="_blank">📅 00:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22609">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارشها حاکی‌است چهار نفتکش ایران توسط جنگنده های F18 هدف گرفته شده اند.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22609" target="_blank">📅 00:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22608">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مقام آمریکایی به وال استریت ژورنال: ایران دوشنبه، برای دومین بار، حمله‌ای را علیه کشتی‌های متعلق به نیروی دریایی آمریکا انجام داد @WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22608" target="_blank">📅 00:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22607">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22607" target="_blank">📅 00:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22606">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/withyashar/22606" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اخطار اولیه  نیروی هوایی آمریکا و تاکیید به هدف قرار دادن موتور خانه و و دادن ۱۰ دقیقه زمان به خدمه برای ترک  محدوده موتورخانه
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22606" target="_blank">📅 00:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22605">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گزارش حمله موشکی آمریکا به سومین نفتکش ایران در سواحل شهرستان جاسک
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22605" target="_blank">📅 00:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22604">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تحلیل ساده
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22604" target="_blank">📅 00:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22603">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دلار ۲۲۹،۲۰۰ تومان (سقف تاریخی)
تتر ۲۲۹،۲۰۰ تومان (سقف تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22603" target="_blank">📅 23:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22602">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گزارش پرتاب موشک از کرمانشاه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/22602" target="_blank">📅 23:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22601">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اتاق جنگ با یاشار : آمریکا نمایشگاه هوایی زده رو تنگه حدود ۱۰ سوخترسان ، پی۸ ، پهپاد و…. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22601" target="_blank">📅 23:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22600">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خبرنگار صداوسیما:
ارتش آمریکا به نفتکش دوم در نزدیکی آب‌های جاسک حمله کرد.خدمه هر دو نفتکش با قایق نجات در حال انتقال به سمت ساحل جاسک هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22600" target="_blank">📅 23:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22599">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پس برم زیر سماور رو روشن کنم
🤣</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22599" target="_blank">📅 23:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22598">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رویترز: امشب در سراسر خاورمیانه آماده باش جنگی است
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/22598" target="_blank">📅 23:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22597">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مقام آمریکایی به وال استریت ژورنال: ایران دوشنبه، برای دومین بار، حمله‌ای را علیه کشتی‌های متعلق به نیروی دریایی آمریکا انجام داد
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22597" target="_blank">📅 23:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22596">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سپاه : به تمامی خدمه نفتکش ها در محدود اسکله های کویت و بحرین که میزبان آمریکایی ها و شریکشان هستند اخطار می دهیم شناور خود را چه در لنگر گاه و چه در اسکله ها سریعا ترک نمایند چرا که مورد هدف  قرار خواهند گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22596" target="_blank">📅 23:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22595">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کامنت برای ترامپ
https://www.instagram.com/reel/DdCe4x2B6Qc/?comment_id=18626069959030735</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22595" target="_blank">📅 23:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22594">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سپاه پاسداران اعلام کرد حملات موشکی جمهوری اسلامی علیه پایگاه‌های آمریکا در خاورمیانه به‌زودی آغاز خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22594" target="_blank">📅 23:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22593">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مقام آمریکایی به فاکس‌نیوز : نفت‌کش‌های ایرانی را در نزدیکی خارک و جاسک هدف قرار دادیم.
این بخشی از تلاش گسترده‌تر برای اعمال فشار اقتصادی بر ایران است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22593" target="_blank">📅 23:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22592">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رسانه های رژیم : دو تانکر نفتکش در خارگ و یک نفتکش ایران در جاسک هدف حمله آمریکا قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22592" target="_blank">📅 23:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22591">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22591" target="_blank">📅 23:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22590">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گزارش های زیاد از صدای ۲ انفجار در جاسک  @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22590" target="_blank">📅 23:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22589">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رسانه های رژیم تازه تایید کردن</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22589" target="_blank">📅 23:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22588">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">منابع محلی خارگ اعلام کردند که این حمله خوشبختانه هیچ‌گونه خسارت جانی به‌ همراه نداشته و کارکنان نفتکش در حال تخلیه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22588" target="_blank">📅 23:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22587">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏I24NEWS :  نیروهای آمریکایی در تنگه هرمز به نفتکش‌های ایرانی حمله کردند @WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22587" target="_blank">📅 22:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22586">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">صدای انفجار جدید از جاسک (ممکنه جاسک پرتاب دفاعی رژیم باشه)
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22586" target="_blank">📅 22:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22585">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گزارش انفجار مهیب در تنگه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22585" target="_blank">📅 22:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22584">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏I24NEWS :  نیروهای آمریکایی در تنگه هرمز به نفتکش‌های ایرانی حمله کردند
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22584" target="_blank">📅 22:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22583">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22583" target="_blank">📅 22:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22582">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX-Bb8kOsA8QQnAfoazcE2fe89kIdrQocUO3BhXSv3slFdK_K_GlQlIZPFi0Q0v664PGlbR9dUldJ1hBafuwJGpcw5VXflgvLK4Yn9FPjceFCkKN1FxpulauRW5cP9IfPgsg5DyWVXZcIEwU5flYY9tKfnamRh3E-c-xprroREFrYqc7KaOc_EmtidluBqI7gfgJ__o8z6CHsivf5ccyf33Pv0VA7x-Lo8K5MVAFuKIRv3E2iyR1qqT_xmh_BNfSCKQomYBFvfXH47wDvAsiBbTR9JRhFRDROd80KVZvVXNANU3rTp9PegqNFeVR8zYzZW70ofWn0wxPbwS89iID2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تانکر دریا» در لنگرگاه خارگ در آتش میسوزد @WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22582" target="_blank">📅 22:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22581">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22581" target="_blank">📅 22:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22580">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22580" target="_blank">📅 22:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22579">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAUhG_VXyZaeWaZOJHkxxIpuKJ682cEuOLyMSHLLpdzJR15KuCxslNiGAVmQEzvLRaAxR7FKUoQXOG-uGJ69-n03-fEnOJIdfAWX4iQBaS54rulcJtSDVFhu3IOxhQnW-QNbOK9lJ39rFcIlSvRmQAMRiKObzszh5VKlhhYWzssK_P3RH5u9SiVVWe5k8NlCbLR2AAAKytwzG2kiYhXwTeF8ExwYHwunO2Whc_3jVwzouZU9EQ73BkHvVXvkj9vUIFpt0ZrUfaOdBTcrhgFlpEVHjMSmsfdvaPOQjsApdu-C_25IQ_RotqCdetTJgbeQaEJIA5JO-P5yMPPMdtN_FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تانکر دریا» در لنگرگاه خارگ در آتش میسوزد
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22579" target="_blank">📅 22:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22578">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22578" target="_blank">📅 22:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22577">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">😾</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22577" target="_blank">📅 22:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22576">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">صدای انفجار ها در محدوده لنگرگاه جزیره ( محل نفتکش ها ) بوده و خارگ در ارامش کامل است تا این  لحظه @WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22576" target="_blank">📅 22:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22575">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سخنگوی سنتکام :
یک فروند زیردریایی بدون سرنشین ما روز گذشته طی یک ماموریت نقشه‌برداری از آب‌های سرزمینی دچار نقص فنی شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22575" target="_blank">📅 22:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22574">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گزارش های زیاد تایید نشده ، خارگ آمریکا داره ۲ تا نفتکش رو میزنه  @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22574" target="_blank">📅 22:06 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
