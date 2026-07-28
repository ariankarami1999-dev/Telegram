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
<img src="https://cdn4.telesco.pe/file/XE2AfZ8KAxP7vqgjTayhmFRWqLjdWD9nRNgRLwBLTBoIedyZgpvCkusoZrXF4kqInZCHa7QRI_a6nmWpwxWN8HcPti74WFRmr4BWnNzWlRsADHruuJB0DyMcpxGEukTzdODVErV88f6f9bmmeRpEJ76qru0EmsEtdyus7Ferz6LIufagy7M-wFIrAyaC7dgcP0tRM41Sauv-dTxp51XnR9v89-NxH_Bqw3Vm2lut0YY1jWYfhwjclvaCzEIU-av2UXv2WEZd8udyMSIRKR74OvNp08K6iir7DEHo9mWFWXhcQwDcDl6TbxZFtYcGTnVdPVP0I_OJQEZhFEAvvwh1Rw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 428K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 16:18:26</div>
<hr>

<div class="tg-post" id="msg-19873">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رویترز به نقل از یک منبع خلیج فارس:
عمان حمایت کشورهای خلیج فارس را برای طرحی که به تهران اجازه می‌دهد داوطلبانه برای استفاده از تنگه هرمز هزینه دریافت کند، جلب کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/withyashar/19873" target="_blank">📅 15:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19872">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رسانه‌های عبری: دفاتر نتانیاهو و زلنسکی در حال هماهنگی برای دیداری سه جانبه در واشنگتن هستند؛ با وجود سردی روابط، دو طرف ، ولی در موضوع ایران منافع مشترکی دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/withyashar/19872" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19871">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec75b87ae.mp4?token=RSQhnfHBnYtWKak5QPXDlH_KGVycDR3iaUCCjvoURJK9z987w6dlR-s3OJ_IoGwvhm41kwQKHj_uJ0TTi9CgMKzyZfeoVao-SZW1aZHJluMqhTHGt40cdOoLFmyBVGMYDIuuNeBDmw-USczzOd-Z-UJWhyxyMvJcfUjOIygQAgvlWKsJFwGatiSZrxtMdQfUoGCCujdsSN-hbJyA7_F9xfYcPe2ibDja35eruGnrnebtueE94C1gCeCwSTg1GNHuipfhkqjEfUyzicC2K_vmGtOuYjKzElTabVkPA0qh9OJidwMHHRjZoG0EnSQFiCzIr8FTe6gxInGvtAlvZjOALIqfARdmWJdUz_5xVmouEJiL4FRr2sY_dooMLIn2yH9cYdBr4H-LAGcdaBBQg69bNR0sLwbC7_10WlnaXHWjJF6PouBuLcIjQVoqSYjgdcVXjcDX_Rkfl5QrCOBkvpxCFKDQo1NrZNonT9yS-mtnAv-LAsaARqF2yMyOJK54o69wtns6q0CIZ1pY-jDkH5U7o79NdS_v99h19PGCZa-wgwtrd3_OIHyvp4iR5Ymy_q6u6iPBVJ6PlWWxQM-P5V4umDOi4wzzYrjp1ndSwTGEkrJrgFrmdH2h6p6JK3rVcBm3wE7yuq5cUplupsiSFbdeHto-JQwjBh8SP5szQ-1rWTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec75b87ae.mp4?token=RSQhnfHBnYtWKak5QPXDlH_KGVycDR3iaUCCjvoURJK9z987w6dlR-s3OJ_IoGwvhm41kwQKHj_uJ0TTi9CgMKzyZfeoVao-SZW1aZHJluMqhTHGt40cdOoLFmyBVGMYDIuuNeBDmw-USczzOd-Z-UJWhyxyMvJcfUjOIygQAgvlWKsJFwGatiSZrxtMdQfUoGCCujdsSN-hbJyA7_F9xfYcPe2ibDja35eruGnrnebtueE94C1gCeCwSTg1GNHuipfhkqjEfUyzicC2K_vmGtOuYjKzElTabVkPA0qh9OJidwMHHRjZoG0EnSQFiCzIr8FTe6gxInGvtAlvZjOALIqfARdmWJdUz_5xVmouEJiL4FRr2sY_dooMLIn2yH9cYdBr4H-LAGcdaBBQg69bNR0sLwbC7_10WlnaXHWjJF6PouBuLcIjQVoqSYjgdcVXjcDX_Rkfl5QrCOBkvpxCFKDQo1NrZNonT9yS-mtnAv-LAsaARqF2yMyOJK54o69wtns6q0CIZ1pY-jDkH5U7o79NdS_v99h19PGCZa-wgwtrd3_OIHyvp4iR5Ymy_q6u6iPBVJ6PlWWxQM-P5V4umDOi4wzzYrjp1ndSwTGEkrJrgFrmdH2h6p6JK3rVcBm3wE7yuq5cUplupsiSFbdeHto-JQwjBh8SP5szQ-1rWTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فروریختن یک مرکز خرید در ژاپن در پی وقوع زلزله ۷/۱ ریشتری
به گزارش "ان اچ کی"، شمار زیادی زیر آوار گرفتار شده و شماری مصدوم شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/withyashar/19871" target="_blank">📅 15:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19870">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آمیت سگال:در اقدامی که از دونالد ترامپ کمتر دیده می‌شود، دیدار او با بنیامین نتانیاهو دور از حضور دوربین‌ها برگزار خواهد شد؛ موضوعی که پیام‌های زیادی در خود دارد
@WarRoom</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/withyashar/19870" target="_blank">📅 15:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19869">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏شالوم بن حنان، از مقامات ارشد پیشین سازمان امنیت داخلی اسرائیل (شاباک)، گفت در طول سال‌ها صدها هزار حساب کاربری رباتی که بیشتر آن‌ها وابسته به رژیم جمهوری اسلامی بودند، شناسایی و مسدود شده‌اند. به گفته او، این شبکه‌ها با هدف مداخله در انتخابات اسرائیل، تأثیرگذاری بر افکار عمومی و ایجاد هرج‌ومرج فعالیت می‌کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/19869" target="_blank">📅 15:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19867">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزیر جنگ اسرائیل:ما قویاً خواهان حمله به تأسیسات انرژی ایران هستیم، اما ایالات متحده در حال حاضر اجازه این کار را نمی‌دهد
۷۰ درصد غزه را نابود کردیم و الگوی آن را به جنوب لبنان منتقل کردیم.
ایالات متحده در موضوع ایران ملاحظات و منافعی دارد که با منافع اسرائیل متفاوت و فراتر از آن است.
@WarRoom</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/19867" target="_blank">📅 13:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19866">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کانال ۱۲ اسرائیل , وزیر دفاع کاتز فاش کرد: جنگنده‌های آمریکایی از اسرائیل برای انجام حملات به ایران به پرواز درمی‌آیند‌ و ایرانی‌ها از این موضوع آگاه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/19866" target="_blank">📅 13:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19865">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مهاجرانی: هواپیمای تازه‌خریداری‌شده در فرودگاه بوشهر بر اثر اصابت موشک منهدم شد؛ تنها بخشی از دم هواپیما باقی مانده است
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/19865" target="_blank">📅 12:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19864">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سی‌ان‌ان‌ به نقل از مقام کاخ سفید: ترامپ در کاخ سفید با زلنسکی و نتانیاهو به طور جداگانه و پشت سر هم دیدار می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/19864" target="_blank">📅 11:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19863">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حقیقت یاب اتاق جنگ :گزارش رسانه های غیررسمی در اینستاگرام و تلگرام نادرست است مبنی بر اجرای حکم ۳ نفر . دیشب مردم اصفهان درگیر شدند تیر اندازی شد و جلادان فقط توانستند دو نفر از عزیزان را اعدام کنند و یک نفر اعدام نشد. @WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19863" target="_blank">📅 11:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19862">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مدیرکل مدیریت بحران استانداری اصفهان:صداهای شبیه به انفجار در برخی مناطق جنوب و غرب اصفهان، بهارستان و حومه ارتفاعات صفه و شهر ابریشم شنیده خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19862" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19861">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سخنگوی دولت: سهمیه بنزین ۳ هزار تومنی از ۱۰۰ لیتر به ۵۰ لیتر کاهش پیدا کرده
اما هنوز هیچ تصمیمی به صورت جمع‌بندی شده برای قیمت بنزین در جایگاه نگرفتیم
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19861" target="_blank">📅 11:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19860">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏زلنسکی و نتانیاهو همزمان به کاخ سفید رسیدند
‏ولودیمیر زلنسکی، رئیس‌جمهوری اوکراین، و نتانیاهو، نخست‌وزیر اسرائیل، همزمان وارد کاخ سفید شدند تا در دیدارهایی جداگانه با پرزیدنت ترامپ گفت‌وگو کنند.
‏همزمانی حضور این دو رهبر در کاخ سفید، گمانه‌زنی‌ها درباره احتمال دیداری محرمانه میان آن‌ها برای جنگ همه‌جانبه با رژیم جمهوری اسلامی را افزایش داده است.
‏این دیدارها در شرایطی انجام می‌شود که پرونده‌های امنیتی مهمی از جمله جنگ اوکراین و تهدیدهای مرتبط با رژیم جمهوری اسلامی در دستور کار واشنگتن قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19860" target="_blank">📅 10:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19859">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حقیقت یاب اتاق جنگ :گزارش رسانه های غیررسمی در اینستاگرام و تلگرام نادرست است مبنی بر اجرای حکم ۳ نفر . دیشب مردم اصفهان درگیر شدند تیر اندازی شد و جلادان فقط توانستند دو نفر از عزیزان را اعدام کنند و یک نفر اعدام نشد. @WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19859" target="_blank">📅 10:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19858">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حکم ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی در اصفهان انجام شد و جاویدنام شدند  @WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19858" target="_blank">📅 09:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19857">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">جلسۀ شورای هماهنگی مجلس با حضور قالیباف
سخنگوی هیئت‌رئیسۀ مجلس: صبح امروز جلسۀ شورای هماهنگی مجلس با حضور قالیباف، اعضای هیئت‌رئیسه و رؤسای کمیسیون‌های تخصصی تشکیل شد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19857" target="_blank">📅 09:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19856">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxHqv1fLLMlSDzTBtnVUicd9BclYBsxfhu0fD1oLN944Wj4qp4GpH2MyAJlMLSNlu6jIunKDPYsgJvMz0Gp4UxPx4ca1_WdCm31wQ3EOuRjC30ccxxscELhZHl3wASgx6FefudS4PYKCqz_1mgyOc4x8ZKSasdFpIHI9cyGq4JN5Zn3i-o_du5U7S5ekYy1ShvVEwb8j3YhpCceD6mazs2ZuUEtF5q6ddOVjnRj1CCCsBT9CD-T-KhVo_z-GmHuOm-32a7kNVcQ7XeAnSjAuTue5KjsBH4iA3RPuYfKnr34Hu4HUkonNqxHlbof_7xwaMqwRbqLuIKGmk1qHpQ_x9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویرک پست : ملانیا و بارون ترامپ در ویدئویی نگران‌کننده که ترور آنها را تشویق می‌کند
یک ویدئوی جدید از ایران، حامیان رژیم اسلامی را به ترور همسر رئیس جمهور ترامپ تشویق می‌کند.
این ویدئو با عنوان «چگونه ملانیا ترامپ را بکشیم» تصاویری از بانوی اول را در کاروان موتوری و در برخی مکان‌های اطراف شهر نیویورک نشان می‌دهد و حتی نام برخی از فروشگاه‌های طراحان مد که او از آنها خرید می‌کند را نیز ذکر می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19856" target="_blank">📅 09:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19855">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">روزنامه لبنانی "النذاع الوتان"، که با مخالفان حزب‌الله همسو است، امروز به نقل از منابع خود گزارش داد که ایالات متحده پیامی قاطع و جدی به لبنان ارسال کرده است. این پیام حاکی از آن است که هزینه دخالت حزب‌الله به نفع ایران و انجام حملات علیه اسرائیل ( در صورتی که ایالات متحده یک عملیات گسترده علیه تهران آغاز کند ) بسیار سنگین خواهد بود. منابعی که در این روزنامه ذکر شده‌اند، گفتند که این پیام به این معناست که هر راکت یا پهپادی که به سمت اسرائیل شلیک شود، در واقع دروازه‌های جهنم را برای حزب‌الله و لبنان باز خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19855" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19854">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گزارش انفجار در اردن
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19854" target="_blank">📅 08:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19853">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGy9WO7dgLpSBFCr4dO8DAA6IgEepdspATCX0UxK0KM2uWkoy65IxFkrkfGZekFWftwxgn1rPzMblgw3OZ_D7UEG_vgnXfSKOzI9m7FsB36CEyujelQKW0bWO2sm-YDuYQkootlqbwBtgQleDa8Yp-bN7xQGhwGja1xms4_APk6PhRlKnAwcw0XLtjC_DQpm6l3QTqOT2Bqen9K2PNQ2gYFHYGi60XO-apEMBWCuThv0kEHCXVC2QVU2pja-y3mSb9UjrN16B_L3dyJqz6LTojiaGxoZKRFDzF17XrIUk-vcr-2iD4yDWIWshtBK4EH0DQerTj6trmJTzIK1sBCZVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار نفت سعودی شده و همکنون 89 دلار است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19853" target="_blank">📅 08:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19852">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhZU6SI0MXdvGyqEi6U_kz1THaUye0Ma6ShrshmdVFj2Ykml0BINdCpT1TBxdlL5OgvX8h2fT8MRb2wxtiG1AJ1-Nmrcew76C4d8-xLwzSUzLyNfa-2guWt3FMEF7NrxQcreomE_Szu2GbwvmFjcRTTWcJc6hXUyykcpQVh2Y0xVuM_3ihoKGLkk8SqLjGCf2CRo3Hlb4p67lqn7_9NBjiaIbjYhPX4xCwDKD_aepC3BAMNrYcIxnbfjN9WonP3cJ39KZegPsxE2FpT_-V8GVsVT8AGIZa5d-fM1y15EGd6LaeaT3UIY2p0QHXinlIB5H8uZuIbCgczztfx3LMSHMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو و همسرش با «اطلاعات محرمانه‌ای» درباره ایران و تأسیسات هسته‌ای کوه کلنگ وارد واشنگتن دی‌سی شدند
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19852" target="_blank">📅 08:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19851">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">به گزارش وال استریت ژورنال، رئیس جمهور ترامپ پس از آنکه بیش از یک سال به مشاورانش گفته بود که کیف در حال شکست در جنگ است، به طور فزاینده‌ای نسبت به چشم‌انداز اوکراین در جنگ علیه روسیه خوش‌بین شده است.
ترامپ «برندگان را دوست دارد» و اکنون به طور فزاینده‌ای زلنسکی را یکی از آنها می‌داند. انتظار می‌رود این دو رهبر روز سه‌شنبه در جریان سفر زلنسکی به واشنگتن برای مراسم تشییع جنازه سناتور لیندسی گراهام در کاخ سفید دیدار کنند.
او تحت تأثیر صنعت پهپاد اوکراین، به ویژه توانایی آن در مقابله با پهپادهایی مشابه پهپادهایی که ایالات متحده در جریان درگیری با ایران با آنها مواجه شده است، قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19851" target="_blank">📅 08:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19850">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حکم ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی در اصفهان انجام شد و جاویدنام شدند
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19850" target="_blank">📅 08:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19849">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شنیده شدن صدای انفجار در اربیل در شمال عراق
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19849" target="_blank">📅 00:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19847">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9da687f9ab.mp4?token=DKsneSUQvmg6iQyV4mo5au7c4aY-4CxD9l3CxP9OyrOdPk8U3RkE2koz15JWtr7nPXMLyLsW32k9v9qxbQwY0ua8L6v2gfhOjShE9JmzZujNOTJkX2aaIXl4qiMWurrmQHtRnAgvLu5FS4sG5vxMCsaVXpGIW5L1WMxo9p072s2U1oJVEpRkofwuy8EeKuk6huNmpz8R6ixuyQaAfIoFhZQ3wb6SFvWO9kB1uNopXi728R4Qmm6GQcy3qPD51CFxjK6hEGQz5F8DyUAiZc5NWsS1sSnH8oeAmTNNe4NiK_gyIK-AnbHXWiPHSP3xcMld42O3QQ70JgmsPBUbnRjyLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9da687f9ab.mp4?token=DKsneSUQvmg6iQyV4mo5au7c4aY-4CxD9l3CxP9OyrOdPk8U3RkE2koz15JWtr7nPXMLyLsW32k9v9qxbQwY0ua8L6v2gfhOjShE9JmzZujNOTJkX2aaIXl4qiMWurrmQHtRnAgvLu5FS4sG5vxMCsaVXpGIW5L1WMxo9p072s2U1oJVEpRkofwuy8EeKuk6huNmpz8R6ixuyQaAfIoFhZQ3wb6SFvWO9kB1uNopXi728R4Qmm6GQcy3qPD51CFxjK6hEGQz5F8DyUAiZc5NWsS1sSnH8oeAmTNNe4NiK_gyIK-AnbHXWiPHSP3xcMld42O3QQ70JgmsPBUbnRjyLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست وزیر قطر: پول‌هایی که به حماس پرداخت می‌شد، شفاف بود و با مجوز دولت بنت انجام می‌شد.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19847" target="_blank">📅 23:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19846">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3e86fee4.mp4?token=i3ym5G07bBWWvHxr4p3p-Tp4E0AX7G1Z1lXHHenhpLECpaXLm-DSt4BGS5QUoBlew1nSvpUcYkft4EBrat0dS8239kCRfddmaIE6o244sqZk71bI_fhHnqhrjqcPQhM35_6l_Dl9qo6-uuIUz-BFRSssb6ykJ3lLPi4VoBg67DT6y8BND7036SatOmObnJtvTROJ_9NTr_Md_j1uZ7PmrF1aDp4Xp-1VhTMqpV62gG-GUIPIMftEOlYGdm5wRkg96LrIOZbZLUCMvUCxRul8ZjyevySnfJke1WYe_juIVC3l92F4XLj9Pwfp-szJbannEr5kJV4IciaHiP5zUNqeT5k_7oe7aUCl1hTwMKXrM06mM3Sp4fVfflEz5Bj79w4DEZyvcBrJn2WqrgOHK1tVbrewPzkuDyA1GIrmr5Vw-QDjxx7wtGTY2Q-Fugn0rEDu5hgX1m_T3q7tOFkO39cxjfrQksTpcVLjwETeneIid-Uzftbc91jOJa0KOMJKdh-zuVMTRBvp26BPbhmejj2EXf81cyBsZHDpYKyYsvROlF1wLYM--8RsqyCCr8YVcl525h5td4Re6y05I9lscmfa5uZt0GQT-1zNCPwGHpFaRZW5MIz9D8e0yqL0EbNi8Apd5NUKVALsr0F65nD7OiJqWwsw7dBbd9p3EHm1S0eynBU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3e86fee4.mp4?token=i3ym5G07bBWWvHxr4p3p-Tp4E0AX7G1Z1lXHHenhpLECpaXLm-DSt4BGS5QUoBlew1nSvpUcYkft4EBrat0dS8239kCRfddmaIE6o244sqZk71bI_fhHnqhrjqcPQhM35_6l_Dl9qo6-uuIUz-BFRSssb6ykJ3lLPi4VoBg67DT6y8BND7036SatOmObnJtvTROJ_9NTr_Md_j1uZ7PmrF1aDp4Xp-1VhTMqpV62gG-GUIPIMftEOlYGdm5wRkg96LrIOZbZLUCMvUCxRul8ZjyevySnfJke1WYe_juIVC3l92F4XLj9Pwfp-szJbannEr5kJV4IciaHiP5zUNqeT5k_7oe7aUCl1hTwMKXrM06mM3Sp4fVfflEz5Bj79w4DEZyvcBrJn2WqrgOHK1tVbrewPzkuDyA1GIrmr5Vw-QDjxx7wtGTY2Q-Fugn0rEDu5hgX1m_T3q7tOFkO39cxjfrQksTpcVLjwETeneIid-Uzftbc91jOJa0KOMJKdh-zuVMTRBvp26BPbhmejj2EXf81cyBsZHDpYKyYsvROlF1wLYM--8RsqyCCr8YVcl525h5td4Re6y05I9lscmfa5uZt0GQT-1zNCPwGHpFaRZW5MIz9D8e0yqL0EbNi8Apd5NUKVALsr0F65nD7OiJqWwsw7dBbd9p3EHm1S0eynBU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زامبی لند
🤣
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/19846" target="_blank">📅 23:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19845">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c6fd33f33.mp4?token=vXSVhJ7YmAyqAzygOtfmcVFpns8XqjTZULTta1adJyNt0oKBDVTrmVmPp9T0JiGBzvPOr6nf3dF_gh0dU-LRCulhGUW_PCqnH_gAw7mT09aS7PvKGl1_8UPuWdkByV8NEm3u8Hlm_BUDLpqRBXBHTzJL4N-e44s1mSRg4tZIiX6IikukEPHwTBcJmv8b7qvJamzlXkFfY4bhpsQprmqulHU9ViZW0KnmzhRVdkrrXfS2KC0P8eZ7eilVzIA9m1s3iQDHpBaJxdlPyOwcBweJpj8hcGRmZLxKQl_56KqB7PLKc6AVtDyAnKeW_K5iAsVoPtvBGV7fP0_FOBYXqbb4Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c6fd33f33.mp4?token=vXSVhJ7YmAyqAzygOtfmcVFpns8XqjTZULTta1adJyNt0oKBDVTrmVmPp9T0JiGBzvPOr6nf3dF_gh0dU-LRCulhGUW_PCqnH_gAw7mT09aS7PvKGl1_8UPuWdkByV8NEm3u8Hlm_BUDLpqRBXBHTzJL4N-e44s1mSRg4tZIiX6IikukEPHwTBcJmv8b7qvJamzlXkFfY4bhpsQprmqulHU9ViZW0KnmzhRVdkrrXfS2KC0P8eZ7eilVzIA9m1s3iQDHpBaJxdlPyOwcBweJpj8hcGRmZLxKQl_56KqB7PLKc6AVtDyAnKeW_K5iAsVoPtvBGV7fP0_FOBYXqbb4Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
برای مدتی قیمت سوخت پایین آمد. سپس آنها رفتار مناسبی نداشتند و من مجبور شدم برگردم.
حالا آنها دوباره رفتار مناسبی دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19845" target="_blank">📅 23:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19844">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8c208632.mp4?token=Tyxz4QUBdLTBzj1kkC2vrKkCONNKK5nbyq1X9Uh9KXLjMn67a5UwFUSOSINYlg0jcuIf7a06TwV2UEJRxfwyL2zoCDo1WmZ9vFtAyNthIK88wLowBrGviqBqIBwKA5z2sIX_NkGX42csvaFrhxxXHf9AqG1f0CywSxyny_-InRR6dnjPke0ceYCSQGr97iK8IdpHSEzULbZ-dEZOCUFsqr7xgxvxVxjL7BL8hYSAZ1ywWB1zficsspF_6KiLgqDJUdKZvzjxBMkDo2xSu668hj0kIGN2GoXUgSWWaAZvN8aBDxtzr4al6Nw99QQD689CM_BuLxFMpTs4u3BHyvn6uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8c208632.mp4?token=Tyxz4QUBdLTBzj1kkC2vrKkCONNKK5nbyq1X9Uh9KXLjMn67a5UwFUSOSINYlg0jcuIf7a06TwV2UEJRxfwyL2zoCDo1WmZ9vFtAyNthIK88wLowBrGviqBqIBwKA5z2sIX_NkGX42csvaFrhxxXHf9AqG1f0CywSxyny_-InRR6dnjPke0ceYCSQGr97iK8IdpHSEzULbZ-dEZOCUFsqr7xgxvxVxjL7BL8hYSAZ1ywWB1zficsspF_6KiLgqDJUdKZvzjxBMkDo2xSu668hj0kIGN2GoXUgSWWaAZvN8aBDxtzr4al6Nw99QQD689CM_BuLxFMpTs4u3BHyvn6uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
مذاکرات دوستانه‌ای در جریان است.
ایران می‌گوید: «لطفا، لطفا، محاصره نکنید.»
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19844" target="_blank">📅 23:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19843">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b4de1bcc9.mp4?token=Jm9FB5bPXCkRjdOamfAYfxN5VW11HuDzGmF37FUJHQFNVgMxsH6TpEvXKTsCCgFuXKVFMvC2cvRnZfqMANIelmVZFKyO_kmHoD4GUVOoDJuWrvft38qMKzRbrfqX5LYDAtGKCM8DZqF0qN2oWCKHbSxqtnre5dJoISwwvQl4BfDdRoVcKmgJ8Pw52HHxFtS5MZXcwo9tQOFiiO4HGn59QvvdhSB-RBAjZEVjP8KtW4gBewnVnBHR2kRcTatuJ_63atZgT5vsce1OKZNx8PVLcLgt_r7pu4nsCjlHDNNZNorNpAYLw217BndoyaPzrmwfK2Z3UND_AY2dz_C60LBHbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b4de1bcc9.mp4?token=Jm9FB5bPXCkRjdOamfAYfxN5VW11HuDzGmF37FUJHQFNVgMxsH6TpEvXKTsCCgFuXKVFMvC2cvRnZfqMANIelmVZFKyO_kmHoD4GUVOoDJuWrvft38qMKzRbrfqX5LYDAtGKCM8DZqF0qN2oWCKHbSxqtnre5dJoISwwvQl4BfDdRoVcKmgJ8Pw52HHxFtS5MZXcwo9tQOFiiO4HGn59QvvdhSB-RBAjZEVjP8KtW4gBewnVnBHR2kRcTatuJ_63atZgT5vsce1OKZNx8PVLcLgt_r7pu4nsCjlHDNNZNorNpAYLw217BndoyaPzrmwfK2Z3UND_AY2dz_C60LBHbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
شما نمی‌توانید به آنها رشوه بدهید. شما باید آنها را شکست دهید.
و ما داریم آنها را به شدت شکست می‌دهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19843" target="_blank">📅 23:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19842">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a198bcb3de.mp4?token=gaLwmM2nBtv-7wYpnWNVTmVpazRVnD90ap42Gi2cq4MeIWKU-sAGFEKX_Fnfb1hJ8i7zY4q8v0HXyUEfuWQEe5zzg6u91za5mKW9_liheN76OrT18Y1kofQSW-AXJ2Z9SfYkVg4t-nL4YxVHTO992dAF_luSON6C6I1YMEOZj07gaccwcgE9viXNgtHtHR9KSEj1vXreLGOyVBnV18VCz_1anO6H_iW8yPehqBJVM0LNPZUwo7J-zgBFSD2YSjYwYNw1BEAaLaLMBK24Y0HuZfb6bRqpknnissM2ynmk37MkBVqAoYwvdcL8AJKnsozWYf6bbetuhBaYSp5psVUJGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a198bcb3de.mp4?token=gaLwmM2nBtv-7wYpnWNVTmVpazRVnD90ap42Gi2cq4MeIWKU-sAGFEKX_Fnfb1hJ8i7zY4q8v0HXyUEfuWQEe5zzg6u91za5mKW9_liheN76OrT18Y1kofQSW-AXJ2Z9SfYkVg4t-nL4YxVHTO992dAF_luSON6C6I1YMEOZj07gaccwcgE9viXNgtHtHR9KSEj1vXreLGOyVBnV18VCz_1anO6H_iW8yPehqBJVM0LNPZUwo7J-zgBFSD2YSjYwYNw1BEAaLaLMBK24Y0HuZfb6bRqpknnissM2ynmk37MkBVqAoYwvdcL8AJKnsozWYf6bbetuhBaYSp5psVUJGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : همون اتفاقی که توی ونزوئلا افتاد، داره توی ایران هم می‌افته
فقط مردم متوجهش نمی‌شن
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19842" target="_blank">📅 23:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19841">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/506238d711.mp4?token=r9C8IdG6gnBEMu0GitMoDozRUqI_iY8jXlygSSnykXgefqCbO18aJB2j89T1zeWOLNPmbsG7oRlqkYi--VeRoe-V8oedRkF6kdQWru4ZA4sp3kpp-R3uty-ll3ffAJB-KujendG2rcSjAh8d8S2vbodkyQLw5kYlYZnXch-EEg2vP_shsYRxPtwLcYUNTTL-arnqRVXOx5HAPYfWeS3E7q83s9DjuMrUIk1ee3U6Hi5zNaTSIq4ccmajo_-xmD7L7_3Kl1jWrtYMEtQyEm8Mq3zv7YvdEL20V4-3jxCzr_AUCi_SEqYBlupZayROaDqGYswVrrH8tBWSS3ZhBZ4dCjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/506238d711.mp4?token=r9C8IdG6gnBEMu0GitMoDozRUqI_iY8jXlygSSnykXgefqCbO18aJB2j89T1zeWOLNPmbsG7oRlqkYi--VeRoe-V8oedRkF6kdQWru4ZA4sp3kpp-R3uty-ll3ffAJB-KujendG2rcSjAh8d8S2vbodkyQLw5kYlYZnXch-EEg2vP_shsYRxPtwLcYUNTTL-arnqRVXOx5HAPYfWeS3E7q83s9DjuMrUIk1ee3U6Hi5zNaTSIq4ccmajo_-xmD7L7_3Kl1jWrtYMEtQyEm8Mq3zv7YvdEL20V4-3jxCzr_AUCi_SEqYBlupZayROaDqGYswVrrH8tBWSS3ZhBZ4dCjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به كشاورز زمين داد، چريك شد
به زن هويت داد، آنارشيست شد
به كارگر سهام داد، كمونيست شد
به هنرمند اعتبار داد، توده اى شد
به مسلمان حرمت داد، تروريست شد
به دانشجو بورسيه داد، ماركسيست شد
به اقليت حقوق برابر داد، جدايى طلب شد
@WarRoom
نسل ۵۷</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19841" target="_blank">📅 22:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19840">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipEEDKkqBCN4Ra8ItQdhCGfejJTItAN971W8WMmIycsoCq8C0Kflwct0epZz3s3X2RZb894ku2dHXqrIHzLvYYg_7KY-78YUogOk5TSEs1A44VpAigfJfMMrFLCCv_JX2okaz70weY0eJg9axcE-ua5IuDDItoe0v1fWD5EuZJcB9SFfLtHvJxe8vw9oxhR-OzCCWKlUK1zQ37_YeuEQ7yePdW21Z3dUWkED_QV1AihwN6PPRQP4wJU0IayUEF0c08-gMVDSkQamQD4eN9YiVRGDwELJ72ru9cMPCbM_ktrzkI1KOh29hfRLfYD5bexVftiSNR19IbVuEW5okXqWcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏عمو لیندزی بخاطر ما تا مونیخ اومد، حالا وقتشه ما بخاطرش تا واشنگتن بریم.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19840" target="_blank">📅 22:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19839">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db3a98b01b.mp4?token=rVBw_LKJfkDFqJhchYgdUlriGrMJ6zJlfOVgFMLVrr4pqf0Amk9iQyjnEBY4r4gXs2KZ0S_XbLOitxQDHrpkqEAWXLUCMvupIZWBeM0f2GiDjgNT7_qqt4SlY9XVmR-i5DummZQmeaZltllWZbe0FMcoW8HlKS0Y2i1Ao5mwTT6dFc1wsxaoO7soZtwv2G753qNFxOO3AmrmG-fc0wMcdqK_2vpsn4fKs2ZyYluz-_tboK7A4TXHFGXtap0bWs-Ozn2NoKVhW1wFlEomBhKD8_GZK0pHY_bgVUyCX6Ze0yU1TLL1CPAyhf7GMenRci6EqLB3hEVWMqzot5uA_n5LR4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db3a98b01b.mp4?token=rVBw_LKJfkDFqJhchYgdUlriGrMJ6zJlfOVgFMLVrr4pqf0Amk9iQyjnEBY4r4gXs2KZ0S_XbLOitxQDHrpkqEAWXLUCMvupIZWBeM0f2GiDjgNT7_qqt4SlY9XVmR-i5DummZQmeaZltllWZbe0FMcoW8HlKS0Y2i1Ao5mwTT6dFc1wsxaoO7soZtwv2G753qNFxOO3AmrmG-fc0wMcdqK_2vpsn4fKs2ZyYluz-_tboK7A4TXHFGXtap0bWs-Ozn2NoKVhW1wFlEomBhKD8_GZK0pHY_bgVUyCX6Ze0yU1TLL1CPAyhf7GMenRci6EqLB3hEVWMqzot5uA_n5LR4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏در برنامه دیشب مارک لوین پیشنهاد داده شد که یک دولت قانونی در تبعید با رهبری شاهزاده رضا پهلوی تشکیل داده بشه. مارک لوین این رو یک ایده فوق‌العاده خواند.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19839" target="_blank">📅 21:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19838">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کانال ۱۵ عبری: نتانیاهو در دیدار خود با ترامپ، تحت فشار زیادی قرار خواهد گرفت در مورد مسائل مختلف، از جمله سوریه، غزه و لبنان. این دیدار بسیار مهم است و امیدواریم که مقدمه‌ای برای یک عملیات مشترک بین اسرائیل و آمریکا علیه ایران باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19838" target="_blank">📅 21:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19837">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خبرنگار: آیا نتانیاهو از شما می‌خواهد که با ایران به توافق برسید، یا از شما می‌خواهد که به حملات خود ادامه دهید؟
ترامپ: عملکرد بیبی عالی بود. ما در کنار هم عالی هستیم ، نمیخوام بگم ولی ایران اکنون ۸ درصد او چیزی هست که چهار ماه پیش بوده
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19837" target="_blank">📅 20:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19836">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ: از پوتین درباره ارائه کردن تصاویر ماهواره‌ای روسیه به ایران، سؤال خواهم کرد. با اسرائیل در مورد ایران مواضع بسیار نزدیکی داریم. ذخایر مهمات زیادی داریم و مایلم که مهمات بیشتری فراهم شود.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19836" target="_blank">📅 20:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19835">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یاشار : نگران نباشید یک سری مدارک رو و آلبوم رو حتما موساد دیر حاضر کرده  تکمیل کنه میپره
😁
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19835" target="_blank">📅 20:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19834">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خبرنگار: آیا شما و نتانیاهو در مورد ایران با هم موافق هستید؟
ترامپ: یک اختلاف جزئی وجود دارد، اما ما بسیار به هم نزدیک هستیم، بله.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19834" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19833">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ: من زمان زیادی را با ایران سپری می‌کنم و فرصتی وجود دارد که اتفاقات خوبی رخ دهد.
ایران در طول چهارده روز گذشته، ضربه بزرگی دریافت کرده است.
آنها به ما با لحنی بسیار مؤدبانه درخواست کردند: "لطفاً دست از این کارها بردارید. بیایید ملاقات کنیم."
احتمال رسیدن به توافق وجود دارد.
اگر اقداماتی که ما انجام دادیم، صورت نگرفته بود، آن‌ها اکنون آمادگی مذاکره با ما را نداشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19833" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19832">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خبرنگار: آیا از وزیر دفاع، پیتر هیگز، به خاطر توصیه‌هایی که در ابتدای جنگ با ایران به شما ارائه کرد و نتایجی که در پی آن حاصل شد، احساس خشم یا ناامیدی کردید؟
ترامپ: نه، ایشان وظیفه‌اش را به بهترین نحو انجام داد. ما ارتش ایران را نابود کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19832" target="_blank">📅 20:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19831">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wm57G2puJ4T3gVWarWLF3_nh0FTydVzUH1Q6nR3FS0VMbKOfKuPHpmkHUXcVC4KBOdSTRnM1EBKUXfPME9_8_PbenLXN4b0z0fb3SbGrokhf1p8T5kgaTHR5D74PuaO2hE0tdEVzc_JXbdL660M4mopMiPSVPmNKmjTW9P6U5_7Yjj_naExcbjSRPTxbvWn6WJ0giFa8dYulqBiKbOB2TYaCrd3vjqqk8-xIN7xDFCw1toe4pgw5L2_PfP3a3PqBWhgSUoJ78JHfc8GkeasXp-fAL3iGlI6HVLr-vjWmlbIh0wlq9l_MAM_NMT6EbHQoOslV6qgOKs74clUtFax4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند پهپاد MQ-4C آمریکا پس از فعالیت در خلیج فارس، نزدیکی ایران، در آسمان عربستان سیگنال اضطراری ۷۶۰۰ ( از کار افتادن ارتباط رادیویی ) صادر کرد و به مقر خود برمیگردد ، همچنین ادامه پل هوایی ترابری سنگین نظامی آمریکا را شاهد هستیم  @WarRoom
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19831" target="_blank">📅 20:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19830">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نیویورک تایمز : ترامپ در حال بررسی سه گزینه اصلی در مورد ایران است: تشدید اقدامات نظامی، تشدید تحریم‌های اقتصادی، یا اعلام پیروزی و عقب‌نشینی نیروها.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19830" target="_blank">📅 19:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19829">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رسانه‌ها از حمله هوایی اسرائیل به شهرک طیر ابلعروب در جنوب لبنان خبر دادند. جنگنده‌ها ۶ نوبت این منطقه را بمباران کردند. @WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19829" target="_blank">📅 19:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19828">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBwuV1QBj1ro-e2JsFA7MCQqjMjO78XBb_jrrKgw_a0zEN-OghNK8S4W8QrUF0c3jCLyEaBW1hrYVxk_ptClX-cxBhG0S8WTDHI6kaReDF-QzLvFTTRRS1y9HOzglcYE4UE-cpq4IUj3gC0KFBUUPcdXNwPvmiMDLVKDBCDJLummjnay6GHrDv6ZJUj1fLmhOHSS3n44KwiTVbPtJOKhEkmxZxJ2VsWsorlw7KSxPW_O8ceKgnAqMhBkeZWZZJBBAvnYPQ6CpYb26nBgJRV0KB52HuLFojaciD58oEUfqlAau0CUACv1Z6ILXzo0VyY4Aknpimui1kFf7SCgVy7-xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک ملوان آمریکایی در حال گشت‌زنی در دریای عرب توسط ناو هواپیمابر یو اس اس فرانک ای. پترسن جونیور (DDG 121) است که از محاصره دریایی ایران توسط آمریکا حمایت می‌کند. سنتکام ۱۷ کشتی تجاری را تغییر مسیر داده، ۲ کشتی را از کار انداخته و ۲ کشتی دیگر را توقیف کرده است تا از رعایت این تحریم‌ها اطمینان حاصل کند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19828" target="_blank">📅 19:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19827">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هم اکنون
تیراندازی نزدیک کنسولگری آمریکا در تورنتوی کانادا
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/19827" target="_blank">📅 19:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19826">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تامیز اسرائیل : بنیامین نتانیاهو در دیدار پیش‌رو با دونالد ترامپ در کاخ سفید قصد دارد اطلاعاتی جدید و حساسی درباره روند بازسازی برنامه‌های نظامی و هسته‌ای ایران ارائه کند. به گفته منابع اسرائیلی، این اطلاعات شامل ارزیابی‌هایی است که نشان می‌دهد ایران تلاش‌های خود را برای بازیابی توان نظامی و پیشبرد برنامه هسته‌ای افزایش داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/19826" target="_blank">📅 19:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19825">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خبرنگار:علت پذیرش درخواست میانجی‌ها برای توقف آتش توسط شما چی بود؟
ترامپ:چیزی برای از دست دادن یا به دست آوردن نبود ‏
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19825" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19824">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbRJ9o9D-e0rQM1rkqAWywRO1RQ3c-o_P2Mo8xBb5U4XYTjIwyMJ3VQl0amlfnGN42Ytpu3AK4RNIg3XXL26ExJvAGpQN0qT8Uw6Rq2ORXKN5O3GhBoP5uDTPcyFtod-O0uhwQOgsRiIc3C0PTx4uV-h0YsedRGmqdj_zXKwkT6FTl5R-lzOBszlZ21jIkPmc-DLjTIuNrmRZNtdqy42VpHEuiL2Mfb4ZnGcApcXB0gcEB5vPLSON91FwMyuPmR18WDjfPlXLpsiqqHveeXutJbPc0oo3Au3q7M85s6MXog8qzjPyg2Uyw7195_M2okxQVcSbIT_VRg9Ab43QED_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها از حمله هوایی اسرائیل به شهرک طیر ابلعروب در جنوب لبنان خبر دادند.
جنگنده‌ها ۶ نوبت این منطقه را بمباران کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19824" target="_blank">📅 18:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19823">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل گفت: به درخواست واسطه‌ها پاسخ دادم تا فرصتی برای مذاکره با ايران فراهم شود.
"من زمان زیادی را برای مذاکرات اختصاص نخواهم داد."
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19823" target="_blank">📅 18:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19822">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل گفت: ما در حال انجام مذاکرات عمیقی با ايران هستیم و اگر این مذاکرات موفقیت‌آمیز نباشند، به یک عملیات نظامی گسترده باز خواهیم گشت.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19822" target="_blank">📅 18:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19821">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کاظم دست کج : در اسلام‌آباد طرف آمریکایی ۲ درخواست افراطی داشت و اصرار داشت که مسیر جنوبی تنگۀ هرمز فعال باشد و گفت اگر آن‌ها را نپذیرید مذاکرات شکست می‌خورد و ما برمی‌گردیم؛ ما درخواست‌ها را رد کردیم و گفتیم برگردید.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19821" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19819">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ie5gv8i-R24iemnKsrCMHG2mGl_dMJwAS3GmVHtgWYiXLQEv9lvnP5_RzVRldOGM1rEyjC2wlUZikijcU8uGEY7Fj3qwWoQx81jqiUN5bm9hdu8ggXxjiIOdEMkepDsnogfY2S_Dyemx80Uf60yQYDcbp_-RALbIK0dwP95WdGc2kR0sVu87GEDuVkULm03RjNKEpj5TfNZtYu168vDSJL9LGIyCRA4slWkbhyZbXyvdRj5bSiYTvPGOfGxUxuZOW2qcxcG4okkzuGm3CUqHoPeJ3zCSjQNKAbnO2AZ9i9l9tz6rzs2JhAN-0f9wXX0KQmoalkLUZkI2o1UyW9xi-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند پهپاد MQ-4C آمریکا پس از فعالیت در خلیج فارس، نزدیکی ایران، در آسمان عربستان سیگنال اضطراری ۷۶۰۰ ( از کار افتادن ارتباط رادیویی ) صادر کرد و به مقر خود برمیگردد ، همچنین ادامه پل هوایی ترابری سنگین نظامی آمریکا را شاهد هستیم
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19819" target="_blank">📅 17:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19818">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وزارت امور خارجه عربستان : ما پهپادهایی که قصد هدف قرار دادن تاسیسات نفتی در مناطق شرقی و ریاض را داشتند از بین بردیم همچنین این حملات را که توسط شبه‌نظامیان تحت کنترل ایران در عراق انجام شده است محکوم می‌کنیم و تأکید می‌کنیم که پادشاهی عربستان سعودی مصمم است جلوی متجاوزان را بگیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19818" target="_blank">📅 16:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19817">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">همشهری: سران قوا با بنزین ۱۰ هزار تومانی برای سهمیه سوم موافقت کرده اند.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19817" target="_blank">📅 15:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19816">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">جی دی ونس در انتقاد از اسرائیل برای جلوگیری از مذاکرات:
من قطعاً فکر میکنم شاهد یک کارزار بسیار پنهان و با بودجه بسیار بالا بودیم که تلاش میکنه مذاکرات رو منحرف کنه و مانع رسیدن به توافق بشه.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19816" target="_blank">📅 15:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19815">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbef676e41.mp4?token=QVPXHk_vVu4z9_gJNQTm8CarWhOwkQak_ylPqtmWYVQwWS7IVZu23_wQQ64tP7InhqphYEBFzPabR8_Btq6eH-SouWUWUCAKwEdJy8A_oZA7xLNb3GAQfx5dcJyz_QFvJVaeeOUpLSSCYuDRpC2dU5vKVQ9Is0H9RVUxHkhiTyrBWNSdGbW1w-v0WSnX-T4lbOf3n7H_zcQc2fkgDgsLDhTjchQP6ygQgr73ESTche9rq05ah6Taw7YIlLGjejZowdB3Nx-toTO1nKZG1u7wI_VfWf42NkVypgofaguoURc2wxx3FYBx5quLZJJmMDENDYn__TSe-gLrF90nScRYsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbef676e41.mp4?token=QVPXHk_vVu4z9_gJNQTm8CarWhOwkQak_ylPqtmWYVQwWS7IVZu23_wQQ64tP7InhqphYEBFzPabR8_Btq6eH-SouWUWUCAKwEdJy8A_oZA7xLNb3GAQfx5dcJyz_QFvJVaeeOUpLSSCYuDRpC2dU5vKVQ9Is0H9RVUxHkhiTyrBWNSdGbW1w-v0WSnX-T4lbOf3n7H_zcQc2fkgDgsLDhTjchQP6ygQgr73ESTche9rq05ah6Taw7YIlLGjejZowdB3Nx-toTO1nKZG1u7wI_VfWf42NkVypgofaguoURc2wxx3FYBx5quLZJJmMDENDYn__TSe-gLrF90nScRYsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: من با رئیس جمهور ترامپ در مورد مسائل مختلف گفتگو خواهم کرد، و در صدر این مسائل، ايران قرار دارد.هدف از سفر من به واشنگتن، تضمین امنیت، قدرت و آینده اسرائیل و همچنین گسترش دامنه صلح در منطقه است.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19815" target="_blank">📅 15:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19814">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rongZTMh7IEjnSLPUMWxNr6KEHEg6IMp5tcLws5f-FgCwZxlTIXowgiOiRDGPH5x7dwYIXIOO7ijSik5BcJgY_UVms_xnw7Sr3WNB_PbItev90x2kSDrEF6qADZJve8eQxBBe6lwjfNqSA-fuNa3JKLn4GngxBOVsVyjDxRiuc31XRxe03SNQInpvvS3RXR0l6cezsHgBxl_VfhRRGnaeqY0YYpL-F6Qt2ciOaYB8i4RGVwTFPb8-wet99qkWW4omxMejMDBbwlb-pk8c7Jk9EQVxQ5AHK9Z29sVPwMdQtOwm6D94qT3IE75qK5WK7sNFMO01Z6ggdFrf6yJQ9-ZIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون کرج سمت فرودگاه پیام
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19814" target="_blank">📅 14:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19813">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">صداوسیما: تلاش آتش نشانی برای نجات ۳ نفر که در طبقه سوم ساختمان مجاور هتل استقلال محبوس شده اند @WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19813" target="_blank">📅 14:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19812">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUeY12sKCbN8ZVbRHERubEmnLNjtQDq6Uzz33kPD7ka8j2UrYlvQU05UN3A3j2mL8VD-wLHfd_M3GwgWpSGyEwQ6-5bBAiGgGPOudHS1VpHW0LK7bK5q4aU_or2h9ZnY8FMOuB2UOG4pBaN8fJMD_9uRynsKQzcpjDKxGKZnwnA3vHTwlJkWPnpIKPirc3Ty4mH-auTzJGfvMoFibvB6cDEsrJs27BlmNkcuUWEqlnm0Oy6iPv0qsPz-RFVTHWowaFZaAs7lXroUcGSmwJ0WiEYSGiMkFx7nFXExfjRQ6_NyXKHxwoh1Djx7_ZRKhaHRfq9B2E6i9wYeVfAk1Ts-yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دهه هفتاد میلادی، در زمانی که در منطقه کسی نمیدانست سوخترستان حتی چیست. عکس بسیار زیبا از سوختگیری دو فروند بویینگ 747 شاهنشاهی بر فراز دماوند.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19812" target="_blank">📅 14:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19811">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">هواپیمای استاد بزرگ شطرنج بی بی نتانیاهو  تیک آف کرد و پرید ! تا کور شود رسانه هایی که خبر تاخییر رو کنسلی انتشار میدهند @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19811" target="_blank">📅 14:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19810">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f9ca588d.mp4?token=NTIrPHaV_Fgjudw54gylfi6iK_6L_Nu1KW2QihPen6w5PpZhyqAEhIKES5eWlh6nTmxtekZgQ59CJ7_aWz548DciII3DDgtdrzZR_B9TMBg6PIiE4tCA2BJ68xJLhlAJ9SOlO5Jsr9snDrxMpubwnXWie_rAO5INBVqONdfJRA2l-wCRy7F24b5__LEuPgpOwVkKzPyASdpA7ydQ7J_EfXjP4dKlvPAGTOR4pOrGU6d-2iy0tbB9SKA5iBIy_t6eXamCn3Bxl75sbL5CTGxIOJePVeuL9_aRafkr4zDGTrPlvMDBhSHJ5N0Ydwt4MJaEAyyfg_tojkKMFLz13az-vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f9ca588d.mp4?token=NTIrPHaV_Fgjudw54gylfi6iK_6L_Nu1KW2QihPen6w5PpZhyqAEhIKES5eWlh6nTmxtekZgQ59CJ7_aWz548DciII3DDgtdrzZR_B9TMBg6PIiE4tCA2BJ68xJLhlAJ9SOlO5Jsr9snDrxMpubwnXWie_rAO5INBVqONdfJRA2l-wCRy7F24b5__LEuPgpOwVkKzPyASdpA7ydQ7J_EfXjP4dKlvPAGTOR4pOrGU6d-2iy0tbB9SKA5iBIy_t6eXamCn3Bxl75sbL5CTGxIOJePVeuL9_aRafkr4zDGTrPlvMDBhSHJ5N0Ydwt4MJaEAyyfg_tojkKMFLz13az-vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار : نگران نباشید یک سری مدارک رو و آلبوم رو حتما موساد دیر حاضر کرده  تکمیل کنه میپره
😁
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19810" target="_blank">📅 13:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19809">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKRoMfBGDVV2_lfhKKxt5GM0sanOgA-6upqVCXTLJTs5pEcjwE5rWcMAzzyVL8D5YM6MKwX5V9mMOJ5_SC2wU_gFAIj6l462NOV3jRsUWyoa7kS6yGuPGawdn8m7KuSkgIVj-V8EgncLmAv6zIi9KUzthNcYwTVpuFHn8VhEiWkb98B5GIP1N1ZsCsXrSO6DCUXrs5S3cYJ1wZlkYXPsyWhpO4eT_P2Qs2-kTU8S5HvCny5dvwaFQfFuNIwF2ZZc8oUMWEq5gm_D8-4YU2-imT3uiqMXGlYy7UyQcKVr4iGWZcxW-qh4vhdSBhW3HWItFxyP6VNQGD0wkuoHIPQOnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای استاد بزرگ شطرنج بی بی نتانیاهو  تیک آف کرد و پرید ! تا کور شود رسانه هایی که خبر تاخییر رو کنسلی انتشار میدهند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19809" target="_blank">📅 13:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19808">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19808" target="_blank">📅 13:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19807">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ایتامار بن گویر، وزیر امنیت ملی اسرائیل گفت: «باید کارهای بیشتری انجام شود. من امیدوارم که دونالد ترامپ، رئیس جمهور آمریکا، متقاعد شود که ساده‌لوحی خود را متوقف کند. او یک تاجر است و در مورد مسئله ایران بسیار ساده‌لوح است. هیچ دیپلماسی با این افراد وجود ندارد، هیچ چیزی برای صحبت با آنها وجود ندارد. باید با ایرانی‌ها از طریق دوربین صحبت کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19807" target="_blank">📅 13:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19806">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دفتر نخست‌وزیر اسراییل از به تعویق افتادن پرواز ۱۱ صبح وی به واشنگتن خبر داد، اما بدون ارائه توضیحی درباره علت این تصمیم، زمان جدیدی برای انجام این سفر اعلام نکرد @WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19806" target="_blank">📅 13:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19805">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دفتر نخست‌وزیر اسراییل از به تعویق افتادن پرواز ۱۱ صبح وی به واشنگتن خبر داد، اما بدون ارائه توضیحی درباره علت این تصمیم، زمان جدیدی برای انجام این سفر اعلام نکرد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19805" target="_blank">📅 13:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19804">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRRknybaHQbL1nY2pDddxUhoBn5K0ND2hBkPZzjTIwHB99xSd4Lb8g4EfTjnBKY0MWZY8xwIyZ1CNm9DDTnrMt7_ev-J1PjTY6RrL-vTndpbMZ-jW14qI8RdmO-mYx8c3-f-7hvEsl0XbmKhCEUaBzxmf0TtfW7gxF9E7ZCAyp0rINrnUgxpYoDaEVewyV1Cmk1Wfoq5NNpTlxydNWVduUl9Dc8srDsSolectoUwBVDvXLvFByW4QlR5_tpFRdkkQIb2E-tE5kfMoov7AzrKrC2sB3Dg0jdz1CJv1_V8Uit6r1SnOkpED8-k6ruRcMlb1o81ZxnxP_xhBnsUaBIgLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه اطلاعات ۴ مرداد ۱۳۵۶. دقیقا سال پنجاه و شش هم همین موقع ها، هتل هیلتون آتش گرفته بود.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19804" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19803">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">صداوسیما: تلاش آتش نشانی برای نجات ۳ نفر که در طبقه سوم ساختمان مجاور هتل استقلال محبوس شده اند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19803" target="_blank">📅 13:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19802">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db435b3a7.mp4?token=iudrdp0egxPkOLfa0KuBMjM0gpBoG_TbGmV3XzMszQ07jrt6lHnMe2z-L5dTDt_W_ABvV6MMbUWBmNcQmCb_QPf3n7I7_mmL5CuPdEUdfdFghQudg6BOetyFc82Bzun38L1bGuXF9NrwGfSbNACDkNFFweAT011tPcm6g_WujBqVq6B17zFt_BuK4C8W4skUiY_0DVmSB_rp_ImbEF-KrsbT1mrceXNbjoaC617GN_DH9PO3DxR5fVNIJgpdx-rGG_odW7aO4AyeVOE7WbiUNKP9szUaxEhRADXDvitihMHX3zXkgR47pO5L5z5_0FkMURAoGJiBSgcemE62N9ObGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db435b3a7.mp4?token=iudrdp0egxPkOLfa0KuBMjM0gpBoG_TbGmV3XzMszQ07jrt6lHnMe2z-L5dTDt_W_ABvV6MMbUWBmNcQmCb_QPf3n7I7_mmL5CuPdEUdfdFghQudg6BOetyFc82Bzun38L1bGuXF9NrwGfSbNACDkNFFweAT011tPcm6g_WujBqVq6B17zFt_BuK4C8W4skUiY_0DVmSB_rp_ImbEF-KrsbT1mrceXNbjoaC617GN_DH9PO3DxR5fVNIJgpdx-rGG_odW7aO4AyeVOE7WbiUNKP9szUaxEhRADXDvitihMHX3zXkgR47pO5L5z5_0FkMURAoGJiBSgcemE62N9ObGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هتل در حال تخلیه است
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19802" target="_blank">📅 13:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19801">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtdrY8APU4_5MT550uFn3djL3-uUzcNFuruJRRk0SI1Tx8-nul_UWppP5oSbzK2tGCN3tvaiSqPbEyEAmrb48R8RJD5DmORaZKRIHTSYI29ma5-kJ8Gta3YMdhtg1rTWjRlLXVTCAIkFjX0qeGRcL3t40q68MQcJy4C3bIaLUi6nJ_fw3zRKSvKI5liARbqJGr5f1KAcFuBT9a7KA1g9AXCZTTyKEOu4isox5qeZZJe5sSCCx_3UprhWNOAdBxm8TxW4Dk4-5oxadkiHoy6ILPlN3ufSN_46KoYk-gpMVg8uxYg2Zf5QwRDdIw6IQtkPCWEjmeU9DPcFP5vEpwacZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش سوزی ساختمان هتل هیلتون
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19801" target="_blank">📅 12:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19800">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">جمهوری اسلامی  : تنگه بسته است
سخنگوی وزارت امور خارجه ایران گفت تهران به واشنگتن اجازه نخواهد داد شرایط پایان جنگ را دیکته کند و هشدار داد که تنگه هرمز همچنان بسته است. او همچنین اوکراین را به دلیل حمله ادعایی به یک کشتی ایرانی تهدید به تلافی کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19800" target="_blank">📅 12:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19799">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b0896ed8.mp4?token=OxoiwLfL4dju1BBZKRxtFt_Tci89nmhFue_aPkg0NiE-s3Z0iqToQxdMMAoXJv-O-XA1aHiY1rOxONawEU6lgBOjQ8jHlWsAP_S7Ir1svcqttoyGuS7BmIR-f0FeeRTWKl1SDoxjAGDWIRKORIHRPqcF-QjkQiZz4L8UhQUHAreDl8eqfAeD0kRiMmdv_DPG34HFrJ855FhHQLy2evpWpkeFX3XXYONhm2Afm06pogrDfwA8mQta32nkO3FGsfFbkVLYsSEyo9o-rbw_A52os9EcYNcleG7GETNA1PkKXgOLgejOdB-bTWuOK28g0SsYWF7nY00g8VORMLP4XRbbIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b0896ed8.mp4?token=OxoiwLfL4dju1BBZKRxtFt_Tci89nmhFue_aPkg0NiE-s3Z0iqToQxdMMAoXJv-O-XA1aHiY1rOxONawEU6lgBOjQ8jHlWsAP_S7Ir1svcqttoyGuS7BmIR-f0FeeRTWKl1SDoxjAGDWIRKORIHRPqcF-QjkQiZz4L8UhQUHAreDl8eqfAeD0kRiMmdv_DPG34HFrJ855FhHQLy2evpWpkeFX3XXYONhm2Afm06pogrDfwA8mQta32nkO3FGsfFbkVLYsSEyo9o-rbw_A52os9EcYNcleG7GETNA1PkKXgOLgejOdB-bTWuOK28g0SsYWF7nY00g8VORMLP4XRbbIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در
۲۰ و ۲۱ بهمن ۱۳۵۷
در پادگان‌هایی مانند
دوشان‌تپه، عشرت‌آباد، حشمتیه، لویزان و مراکز دیگر
مردم برای تصرف اسلحه وارد پادگان‌ها شدند و تعدادی افسر، درجه‌دار و سرباز را کشتند !
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19799" target="_blank">📅 12:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19798">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دیدار نتانیاهو و زلنسکی با ترامپ
گزارش ها از سفر قریب‌الوقوع و ناگهانی زلنسکی، رئیس جمهور اوکراین به آمریکا همزمان با سفر نتانیاهو به آمریکا
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19798" target="_blank">📅 12:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19797">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سخنگوی وزارت خارجه: درخواست مذاکره کردن اصلا با ژن ما همخوانی ندارد بقایی:ادعای درخواست مذاکره از سمت ایران، صرفا یک خبرسازی است. البته ما درب دیپلماسی را نبسته‌ایم، اما در حال حاضر هیچ مذاکره‌ای با آمریکا در جریان نیست. @WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19797" target="_blank">📅 11:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19796">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سخنگوی وزارت خارجه: درخواست مذاکره کردن اصلا با ژن ما همخوانی ندارد
بقایی:ادعای درخواست مذاکره از سمت ایران، صرفا یک خبرسازی است. البته ما درب دیپلماسی را نبسته‌ایم، اما در حال حاضر هیچ مذاکره‌ای با آمریکا در جریان نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19796" target="_blank">📅 11:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19795">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtuU_YbkvctRFb9b2C9QNOhFsT5kRjb-X_xChHfMv2EjqPoINp4jh4ELBkRWPCoCkzA-48kcntv1d1Z1SjkXLpkPGUfrMGAkq7b6tJcc1uZ5WQRuTE6O55IzEYM9U23ysUQcg6Pypm7fQY7ZmD9DDdsAXw9bUgG82kG0ToGNwbB15b2HaFIMYyOsEhCdZ3o4A1N2WIFUgA6-OFLiIQ_rTbJmLcX4i6VWy4X2-nyW8VnOqotkwC-_zAJAdN8CtxeZIYUvuOUGK2qf7f9CiubSq2nhDDcMWZSo7P9G911ibLHOVchcam2pkMtGieV_rOu3Ex-QT74C7BZDcTquX56p1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از «نیما مرادی» که در حمله اوکراین به کشتی ایرانی کشته شد. کشتی آنا از بندر آستاراخان عازم بندر انزلی بود.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19795" target="_blank">📅 11:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19794">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پوتین: شناورهای تندروی ایران در درگیری با آمریکا عملکردی موثر داشتند
رئیس‌جمهور روسیه در دیدار با فرماندهان و نظامیان ناوگان دریایی این کشور اعلام کرد که ایران در جریان درگیری نظامی با آمریکا با موفقیت از به‌اصطلاح «ناوگان پشه‌ای» (شناورهای کوچک و تندرو) استفاده کرده و این نیروها عملکردی کاملاً مؤثر از خود نشان داده‌اند
، توسعه چنین نیروهایی برای ناوگان دریایی روسیه نیز ضروری است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19794" target="_blank">📅 11:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19793">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هواپیماهای تهاجمی A-10 Warthog برای عملیات احتمالی علیه ایران در خاورمیانه اعزام شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19793" target="_blank">📅 10:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19792">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccbe6758e6.mp4?token=umIwtPRPaawqz7F8c-tExORHe8UJ4htbMNSoX7eQKd8I-0NqWyOPNJHMxdXjxnj0a6U6CIFwWkPhw1QEtdQ8qZsVM19BrqQvheCrog4hyaXqvHGlWebqIDlae5Yi2S-c034vvZB66ecEACRILqpmQiRPlDk0Z2uHyliDNqbogiTec4aDxqz94wkzrWA24uXOcJ9Bo7FU5vaiqHPREQNMk6PnJRamyV2CHvcq_dqvwvqz1zYlGKxQURNUnRYIq76B8AU9d93ITuwTfnk3WlDEC7zowTbVgbYOLv0eUBtsw5tNin2gDKgn6JkCHDBaVa0mt6eyzagFUd_sbA6toaWJNS9KRJLBpV-qqEw7MtGmeiAr9nTys96d7Rik8gR8omUUCOeMNnOBE21OtnfuEAvzg3LmXbCYFx6nYs9ljY28TDYJkkgtc6TQzZEXeH8MUQRL1tZtkPVZOf8qhzm_nh3lpZaIkcNpu8lo4JKKTfxevWY60hy9b-9N1Xb3hFmQhyeXPQWYs00pq_NwJE12D0BqO0pvyOlvPSMC4JRnMIHEUOnexvJYEXNdvsw69D_EtIKDIIfA2EeM9F_3pIyWAjDXlwD5ipifmPJ3YvcauAwPiALPGWB14E0caqQ6-99luz1CCNwX_hQXvZd09KaUNdAUKq6TZQAibjUpkDgL8sMQ-sI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccbe6758e6.mp4?token=umIwtPRPaawqz7F8c-tExORHe8UJ4htbMNSoX7eQKd8I-0NqWyOPNJHMxdXjxnj0a6U6CIFwWkPhw1QEtdQ8qZsVM19BrqQvheCrog4hyaXqvHGlWebqIDlae5Yi2S-c034vvZB66ecEACRILqpmQiRPlDk0Z2uHyliDNqbogiTec4aDxqz94wkzrWA24uXOcJ9Bo7FU5vaiqHPREQNMk6PnJRamyV2CHvcq_dqvwvqz1zYlGKxQURNUnRYIq76B8AU9d93ITuwTfnk3WlDEC7zowTbVgbYOLv0eUBtsw5tNin2gDKgn6JkCHDBaVa0mt6eyzagFUd_sbA6toaWJNS9KRJLBpV-qqEw7MtGmeiAr9nTys96d7Rik8gR8omUUCOeMNnOBE21OtnfuEAvzg3LmXbCYFx6nYs9ljY28TDYJkkgtc6TQzZEXeH8MUQRL1tZtkPVZOf8qhzm_nh3lpZaIkcNpu8lo4JKKTfxevWY60hy9b-9N1Xb3hFmQhyeXPQWYs00pq_NwJE12D0BqO0pvyOlvPSMC4JRnMIHEUOnexvJYEXNdvsw69D_EtIKDIIfA2EeM9F_3pIyWAjDXlwD5ipifmPJ3YvcauAwPiALPGWB14E0caqQ6-99luz1CCNwX_hQXvZd09KaUNdAUKq6TZQAibjUpkDgL8sMQ-sI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتهای زیبای ریچارد نیکسون در مورد شاه و اتفاقات آن روز.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19792" target="_blank">📅 10:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19791">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f90eed59a.mp4?token=Q_V--63D4vv1Wm58a7zRypeiJDncgmzLvARR68x11xEv6B36aC4ZvioJtOCAlo45yI6MpgPBVmMnaAhXkCfgSRRFy2-LBoCLEUpR27Dq6m7BqVElF9ngRBkmYCMbu2V_QINUBMcBOEeEg1Jd0IkT9N0_HRKeSZNkznwgozgh8mLJjupoxtFoJnxzSk6NHx7Ma3jnJ5zLH1J_91XwDYejrP97UXAMAuTJgbz9MVZJvYwZoHhPa5PMIeghPouAqpA5fnVZhe_k1gSsGi9PmNH_TGD9Hys4zMTDRVMy5pK58oAl71H-6AaFRq1VBCINhOST4BwUPx4mWlEwv6ORBhwpfhYGi6yi_mvZO1ZYPsfq6HRLH4s3Dt2lzhttn0VmaJXmEMHWhcWaSA5mTrt_VJrbbcjvcadZZD8trysP0rIFOPtqith8vd1EGk-4LdPX_TjN_3k6e-Z13xlERfIzfrGon0Dg484ygJgbNfEzscLS4fzmKB6Qb2chJ5qFwB8w-WG47Jrs6wHiE6HWtKRLFmhdpEe6FxVscKeYvdtmNKO_VVZGjynyvpB5sZ8zdkxzsDirNni-EbkuUZOrIPbD1sMMuHbee8D8DyQ-XF_BwP5E_2X6X_1er3ZcmQQepgDDiTSO8H5m3ShiVkB8mrGZGgInWUVq0B4bpsOmb4xc-3hlUxM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f90eed59a.mp4?token=Q_V--63D4vv1Wm58a7zRypeiJDncgmzLvARR68x11xEv6B36aC4ZvioJtOCAlo45yI6MpgPBVmMnaAhXkCfgSRRFy2-LBoCLEUpR27Dq6m7BqVElF9ngRBkmYCMbu2V_QINUBMcBOEeEg1Jd0IkT9N0_HRKeSZNkznwgozgh8mLJjupoxtFoJnxzSk6NHx7Ma3jnJ5zLH1J_91XwDYejrP97UXAMAuTJgbz9MVZJvYwZoHhPa5PMIeghPouAqpA5fnVZhe_k1gSsGi9PmNH_TGD9Hys4zMTDRVMy5pK58oAl71H-6AaFRq1VBCINhOST4BwUPx4mWlEwv6ORBhwpfhYGi6yi_mvZO1ZYPsfq6HRLH4s3Dt2lzhttn0VmaJXmEMHWhcWaSA5mTrt_VJrbbcjvcadZZD8trysP0rIFOPtqith8vd1EGk-4LdPX_TjN_3k6e-Z13xlERfIzfrGon0Dg484ygJgbNfEzscLS4fzmKB6Qb2chJ5qFwB8w-WG47Jrs6wHiE6HWtKRLFmhdpEe6FxVscKeYvdtmNKO_VVZGjynyvpB5sZ8zdkxzsDirNni-EbkuUZOrIPbD1sMMuHbee8D8DyQ-XF_BwP5E_2X6X_1er3ZcmQQepgDDiTSO8H5m3ShiVkB8mrGZGgInWUVq0B4bpsOmb4xc-3hlUxM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو دیده نشده از مراسم محمدرضا شاه
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19791" target="_blank">📅 10:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19790">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏ساعت ۲۵ ایران ‏ساعت ۹:۱۷ صبح روزِ ۵ مرداد سال ۱۳۵۹ بود كه اين خبر به دنيا مخابره شد: «پادشاه ايران درگذشت.» ‏انورسادات با لباس نظامى آمد،  ‏مستقيم به اتاق شاه رفت. ‏دستش را روى قلب شاه گذاشت،  ‏به انگليسی گفت: ‏«تو ساعت ٩:١٧ دقيقه مردى، ايران در ساعت ۲۵»…</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19790" target="_blank">📅 10:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19789">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">صداوسیما: در ساعات اولیه بامداد امروز، ۶ فروند کشتی متخلف با خاموش نمودن موقعیت‌یاب خود قصد عبور از مسیر جنوب تنگه هرمز را داشتند که یکی از آنها دچار حادثه شده و بقیه تحت مدیریت ایران به خلیج فارس برگردانده شدند
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19789" target="_blank">📅 10:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19788">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خبرنگار الجزیره: نیروهاى ارتش اسرائیل، به همراه بولدوزرهاى نظامی، وارد شهر عرابه، واقع در نزدیکی جنین، در کرانه باختری شدند
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19788" target="_blank">📅 09:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19787">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پنتاگن : از زمان شروع درگیری‌ها در ۹ اسفند، ۱۸ نظامی ایالات متحده کشته و ۶۲۴ تن زخمی شده‌اند
سی‌ان‌ان ‌: بر اساس اعلام پنتاگون، بیش از ۱۴۰ نظامی آمریکایی جدید به مجروحان جنگ علیه ایران، اضافه شدند
نام چهار سرباز آمریکایی کشته‌ شده در حملات ایران که از پایگاه داده‌های پنتاگون حذف شده بود نیز بازگردانده شد
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19787" target="_blank">📅 09:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19786">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏
ساعت ۲۵ ایران
‏ساعت ۹:۱۷ صبح روزِ ۵ مرداد سال ۱۳۵۹ بود كه اين خبر به دنيا مخابره شد: «پادشاه ايران درگذشت.»
‏انورسادات با لباس نظامى آمد،
‏مستقيم به اتاق شاه رفت.
‏دستش را روى قلب شاه گذاشت،
‏به انگليسی گفت:
‏«تو ساعت ٩:١٧ دقيقه مردى، ايران در ساعت ۲۵»
اما ‏آن روز كسی نفهميد معنی ساعت ۲۵ چيست؟
‏او در يک مصاحبه با خبرنگاران خارجى و داخلى ‏گفت: جهان عزادار شد.
‏امروز مردى از ميان ما رفت كه خواهان صلح بود، ‏بعد از او خاورميانه رنگ آرامش و آسايش به خود نخواهد ديد.
‏او فقط پادشاه ايران نبود.
‏پدرِ بزرگى براى منطقه خاورميانه بود و ‏روزهاى سختی را پشت سر گذاشت،
‏او براى دفاع از كشورش در مقابل دنيا ايستاد ، ‏او امروز صبح مُرد اما ايران در ساعت ۲۵ از حركت ايستاد.
‏اين خبر به ايران رسيد، روزنامه كيهان و اطلاعات با خط درشت نوشتند: «شاه مُرد.»‏
‏فرانسوى‌ها ضرب‌المثلى دارند كه حركت روز و شب ۲۴ ساعت است و ساعت ۲۵، ‏ساعت مرگ است.
‏به واقع ساعتِ مرگ محمد رضا شاه پهلوی ساعت ۲۵ ایران بود.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19786" target="_blank">📅 09:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19785">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گزارش صدای انفجار‌بندر عباس ، ممکنه خنثی سازی باشه
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19785" target="_blank">📅 09:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19784">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19784" target="_blank">📅 02:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19783">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پیغام های زیاد گزارش انفجار در‌ اهواز
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19783" target="_blank">📅 02:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19782">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab6daf7646.mp4?token=BQK_dHIKYr4tRK_ZxeBRfYq6s9aClxbc3PqpWy83ony7ihzr-v_JADmRKl1SA-qtPXKeLzB8w2BwFdDSrG8TK-Xo-7fs2Uacw-4gT6PbaDqBnZuSPJzCttslfpLWn-y3EMrykqRUzI3WyQY2Q6usSVVpi-CN4v4avDJc_A5Ho4wR95jaygJzqNSWATPgXTdqFEy3fLGcpOId0VbULhLgFy2G3dc9tm-gNiOPy-xEGXp8lpSW5G1tUs2qFi5n6-KfMpfIDUqY9sZ2zD91Gokn-ohcxFzQnM270_yNs0rZx71L60BJLDUwWLd8JUlHDFxn57RURcgCvhPAEsLWlr0tqTWL1Sxn9gyCFNQ9mxdyRwBfDJiNPorkCZ6k-5BKOEZL86kU0h0ceqveFLSDxSUBNmRyv4KzH1eZ_8WoqFGumkkY-axABcB85mH14q6h6hduaW0quY4KnmvisadpEWmVEygBsQnNdP08eUZiptnHmg-oFGMYA5cwnIL0cZqb6MoBPgXcR2nCrSesOSrVdXo4QR0Pyy0-emlx3UZvjnuJgYZlJMV4w09ENr9ug_8Ng3EaPPZTWvvs7r5DFEYpklTJsl3C3ZOFRCcxysvDsZK6bBWuyeFt8eMjlWR4GtuIrCLjtovJzABYm0KMrvPGhcS6cUsVQy5tCEimuLcgvtFBz1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab6daf7646.mp4?token=BQK_dHIKYr4tRK_ZxeBRfYq6s9aClxbc3PqpWy83ony7ihzr-v_JADmRKl1SA-qtPXKeLzB8w2BwFdDSrG8TK-Xo-7fs2Uacw-4gT6PbaDqBnZuSPJzCttslfpLWn-y3EMrykqRUzI3WyQY2Q6usSVVpi-CN4v4avDJc_A5Ho4wR95jaygJzqNSWATPgXTdqFEy3fLGcpOId0VbULhLgFy2G3dc9tm-gNiOPy-xEGXp8lpSW5G1tUs2qFi5n6-KfMpfIDUqY9sZ2zD91Gokn-ohcxFzQnM270_yNs0rZx71L60BJLDUwWLd8JUlHDFxn57RURcgCvhPAEsLWlr0tqTWL1Sxn9gyCFNQ9mxdyRwBfDJiNPorkCZ6k-5BKOEZL86kU0h0ceqveFLSDxSUBNmRyv4KzH1eZ_8WoqFGumkkY-axABcB85mH14q6h6hduaW0quY4KnmvisadpEWmVEygBsQnNdP08eUZiptnHmg-oFGMYA5cwnIL0cZqb6MoBPgXcR2nCrSesOSrVdXo4QR0Pyy0-emlx3UZvjnuJgYZlJMV4w09ENr9ug_8Ng3EaPPZTWvvs7r5DFEYpklTJsl3C3ZOFRCcxysvDsZK6bBWuyeFt8eMjlWR4GtuIrCLjtovJzABYm0KMrvPGhcS6cUsVQy5tCEimuLcgvtFBz1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز : در ۲۹ دسامبر ۲۰۲۵، خودروی آنتونی جاشوا در نیجریه با یک کامیون تصادف کرد. در این سانحه، سینا غمی، مربی آمادگی جسمانی و دوست نزدیک او، جان باخت. جاشوا پس از ۲۰۸ روز دوری از رینگ، با آهنگ «نقاب» از سیاوش قمیشی به یاد دوست از دست‌رفته‌اش بازگشت و در یک کامبک احساسی دوباره وارد رینگ شد.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19782" target="_blank">📅 01:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19781">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLAmtup4VyfQUkYg5X4mHj-QRaXmEuFSV7GqzY6VkK7qrr2BxR8mMJQD3QXawTohZ6KHboR2_MF4dZubOT-OdknqM2BoV37TqJPXSEEI1A4R9KwD68gDuNoex6rh0epMVLM0Mm1Cz7PdxD8y6_iNliWmT0tCoBuEq_AkLpv77335P-ZzJZ2TatIwul6gMuFmiXmYUFTZl5hqR_tK2oXAsOcJ0JTXrXpHvpWZsG0Fy4eNNH-xZeEjk-B7WxC5rZxMhETINsYynY3EHEIkbkpmwKWS4pQRcJ9MLG4Pse2VWPP6kXI9dHQCa05gvPz0rAA8wMW7E8B1oodcDLm6KYgDLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشاگری یک سایت خبری روسی مبنی بر کنترل مافیای لوازم آرایشی توسط حسن روحانی
رسانه‌های روسی در چند ساعت گذشته با انتشار خبری جنجالی از یکی از بزرگ‌ترین پرونده های قاچاق سازمان‌یافته آرایشی-بهداشتی در غرب آسیا پرده برداشتند.  طبق ادعای این سایت، حلقه اصلی این مافیا حسن روحانی؛ دیپلمات‌ سفارت فرانسه و فردی به نام مهدی‌زاده بوده‌ است.   طبق گفته این سایت اخیرا و در طول جنگ ایران و آمریکا دو کشتی محصولات قاچاق آرایشی تولید کره جنوبی، متعلق به وی توسط دستگاه های امنیتی ایران کشف شده است. این در حالی است که چند کشتی تجاری نیز در سال گذشته توسط دستگاه های امنیتی جمهوری اسلامی کشف شده که با دخالت سفارت کره جنوبی و پیگیری وزیرخارجه کره، این موضوع رها شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19781" target="_blank">📅 01:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19780">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رسانه های نظامی اوکراینی ادعا کردند: در صورت پاسخ نظامی ایران به اوکراین،ارتش اوکراین حملات پهپادی دور برد به شهر های ایران انجام خواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19780" target="_blank">📅 01:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19779">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19779" target="_blank">📅 00:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19778">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">جولانی: حزب‌الله به مدت 14 سال، رژیم سرکوبگر سابق را در جنگ وحشیانه‌اش علیه مردم سوریه همراهی کرد و باعث آوارگی و کشته شدن تعداد زیادی از افراد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19778" target="_blank">📅 00:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19777">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پوتین : شرق اوکراین برای ماست و غرب آن برای لهستان، مجارستان و رومانی است و به زودی به آن ها برگردانده خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19777" target="_blank">📅 00:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19776">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فاکس نیوز:حمله گسترده به ایران هر لحظه ممکن است رخ دهد
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19776" target="_blank">📅 00:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19775">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVT2GTGpdYfHKN8AFeAgaNwYEsskHFrkhMBYoarXZo4iv2XsPlCfYOqp-SGixUBU-aYSbln5zQkHEgIXDmADjdk9oRrH2fDyweMsHdYCp205p28Dhwmdi9ogZaWkiRcT2B9AZjlaShd5c0vlve0FyYdoyHdV-qu130KkeIb2_kRzPtb4gGbqKCO5Lq0WHRbvJNSPw0MZtD5EeKd8tEJ9Jc9DZp2tmTG695VXE9bMGTUF2QD7MV_Ua4DUpt-1tDeHECG12SAdnFDWlYkvy0KvObCFZw2zRAsTK8v5CJITfPnqifsjqQXl3_Hf64rPpembqkudCWZS83xufWBfQSyZzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : نگهبان جهان
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19775" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19774">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCc4-77N4LJcqY1LPDBwpJmrdRg7JDDdR0HmizHaBjgjQsxbOgFGmfKSDqo0Ca7DWp9HkuKmywxukPwyU-WJfcI8oCiODnEH75RNIFyP88_76IgAe8f5ZFF-mPRN0dPryvQ4ocU8LaAsvJS8R5p-ilik1WoOZzxwZjgVuRFt9Rn2SU__PW6B6MGpwnsF0sSfmX1ah91NJhpGVpXl0YXsGJBvjDT-5yCzx566TV2QWSJdFznzazHUAYn_d_kQ0IGYI2q4QTHNf7oJ3kiTR2eT2bfnJDlNef5_LPscx_2ikqYog5TOz6m_IkI8CvsxlaEnElpAii6ujT5bvb9BhORtGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : خداحافظ موتورخانه
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19774" target="_blank">📅 00:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19773">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fp_9euVsMH3phZ8TjOHWVGSXVXHPTfhjSei7mb7rmfXnshjuONh4Umygdf1c-fz4ahlVVhK0OToXYrSaoF2gfP1G_-Q6i-8oh5FKSQdM48zhmRhFaJUz22rvNXI20E3zzR8OyWZjwYioxb11KiuNJOrf4K_WCtYj028bohOcdCgXnvpw_MmeYHTrUXCGaCL5prcSXvH6uNYm9F4btRlpRouquTibDBzTUQ_gVVihLOrkDcczEcnxd_fyie-F3MAYcDke3sPPBSXscFTf54aQF4hYTZ92JaKQbzSYHOYHhIfXa-ktFw2s7d1ORdE6LlgMlxC0H7ytPO_ycPAsy6ox5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : فرشتگان نگهبان جهان
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19773" target="_blank">📅 00:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19772">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9e1f8494c.mp4?token=lYmHU3y2d-H4NO7eoDC0LzKaI3lQV9D0SO3Y3OGf_nzisOD09ZmPWny6JnosQVwps_SIr_rOIKv2TmprCjzepn3rM5eYzbqoMoH8RSC0sEw0L9Dcaox3BR8Psf-eE92MEB1bRvFPGdgdsytlMaum0khCkjyOmryrUpVowkXYiMo5sZpy59Vf8toj6MFM0UdfI-xLRwtqSkluWvIK8ZJhcvf_8WDRZKPf6saNedQO6GdOo2NN_QG5skD2tUcHGmY90Q7ZTxcUa6qIMBH37gchXjaHEghKiBaWTO4w5uk4Xnv9EJ7Pcbl59axRz5zUmyetxa2D4oUI_dvbynLxr6dZZi0cc3MP1zec4_AOJLWHMSal7XG54gmrGrIOv94QfosnuSGOvRTGiRLmd0Osg32Sr7v_l4ANQ0OHDYxgPTrBNhhCP6cUpnqYlEf7Z_X-6giEtC-79HTr2d32FQHK0HEytIzuXSPvqCWI6T0yFLrxoJ0EIm6omchAfuQcE4awApfagXvplgD6Ww1tmoxr1IhcHJaeuL6c_e9zbLFsfYXSaaBDmrX-ntXsQRGzRT7qFSiAwJI7hLXJa9m14kinUfCRQiNcQt1s5fHP_sUFaWWzcd9aGshmjeTrlGFmHmG5UrrjtVKD8QaU7pbuQx5sbiHiusENoboZMOY3bsEqAhNm9uo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9e1f8494c.mp4?token=lYmHU3y2d-H4NO7eoDC0LzKaI3lQV9D0SO3Y3OGf_nzisOD09ZmPWny6JnosQVwps_SIr_rOIKv2TmprCjzepn3rM5eYzbqoMoH8RSC0sEw0L9Dcaox3BR8Psf-eE92MEB1bRvFPGdgdsytlMaum0khCkjyOmryrUpVowkXYiMo5sZpy59Vf8toj6MFM0UdfI-xLRwtqSkluWvIK8ZJhcvf_8WDRZKPf6saNedQO6GdOo2NN_QG5skD2tUcHGmY90Q7ZTxcUa6qIMBH37gchXjaHEghKiBaWTO4w5uk4Xnv9EJ7Pcbl59axRz5zUmyetxa2D4oUI_dvbynLxr6dZZi0cc3MP1zec4_AOJLWHMSal7XG54gmrGrIOv94QfosnuSGOvRTGiRLmd0Osg32Sr7v_l4ANQ0OHDYxgPTrBNhhCP6cUpnqYlEf7Z_X-6giEtC-79HTr2d32FQHK0HEytIzuXSPvqCWI6T0yFLrxoJ0EIm6omchAfuQcE4awApfagXvplgD6Ww1tmoxr1IhcHJaeuL6c_e9zbLFsfYXSaaBDmrX-ntXsQRGzRT7qFSiAwJI7hLXJa9m14kinUfCRQiNcQt1s5fHP_sUFaWWzcd9aGshmjeTrlGFmHmG5UrrjtVKD8QaU7pbuQx5sbiHiusENoboZMOY3bsEqAhNm9uo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در بخش دیگری از‌مستند او قصد داشته در اوایل ماه مارس به فلوریدا سفر کند تا از دونالد ترامپ، رئیس جمهور آمریکا، بخواهد در بمباران حزب الله لبنان به اسرائیل بپیوندد.با این حال، بنیامین نتانیاهو، نخست وزیر اسرائیل، قبل از این سفر، توصیه کرد که درگیری گسترش نیابد و گفت که اسرائیل باید بر ایران متمرکز بماند و هشدار داد که حمله به حزب الله می‌تواند باعث یک جنگ منطقه‌ای گسترده‌تر شود.
نتانیاهو در این تماس تلفنی به گراهام گفت: «ما در حال حاضر بر ایران تمرکز داریم.» گراهام موافقت کرد و پاسخ داد: «این واقعاً توصیه خوبی است.»
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19772" target="_blank">📅 23:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19771">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de7526ff5.mp4?token=DmfvgQ152XFo92z4axbw0TKXh1tbX0PrIcpQbF8rnd4EK0qK4PgTiOq0AZfOHj9wIJ161Hmykbj5qJ0tspD1KN2Qlo6KhT-eZzJOVYPLRua7zD-qIb6J55ufNnp-yLUBu-nSZW34e7k4apUwDvDaaac_zlakAdOTtuKuPP8nQEVFqoOZ3BAjNpWIw4D4eAUICcAY_vKU8xkkGFwuQllnqZ6SITCA8rmXNQg7h7KaB4wF-rldUhc0lvia97l8rPNkZFDQKaxU7BcRo012y-cdduIhqCeeLxp0k8tyXk72zba8RTg4hDQujlWRAlVP2h8jK6BpgMx2nnBsZiHp3_anyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de7526ff5.mp4?token=DmfvgQ152XFo92z4axbw0TKXh1tbX0PrIcpQbF8rnd4EK0qK4PgTiOq0AZfOHj9wIJ161Hmykbj5qJ0tspD1KN2Qlo6KhT-eZzJOVYPLRua7zD-qIb6J55ufNnp-yLUBu-nSZW34e7k4apUwDvDaaac_zlakAdOTtuKuPP8nQEVFqoOZ3BAjNpWIw4D4eAUICcAY_vKU8xkkGFwuQllnqZ6SITCA8rmXNQg7h7KaB4wF-rldUhc0lvia97l8rPNkZFDQKaxU7BcRo012y-cdduIhqCeeLxp0k8tyXk72zba8RTg4hDQujlWRAlVP2h8jK6BpgMx2nnBsZiHp3_anyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر مستند منتشر نشده نشان می‌دهد که سناتور فقید لیندسی گراهام در اوایل ماه مارس پیش‌بینی کرده بود که دولت ایران ظرف «سه تا چهار هفته» کنترل شهرها را از دست خواهد داد و مشارکت بیشتر اعراب «حرکتی تقریباً برگشت‌ناپذیر» ایجاد خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19771" target="_blank">📅 23:54 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
