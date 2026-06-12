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
<img src="https://cdn4.telesco.pe/file/QtJj4gA4RFpnucMxrw2sYGix7DgdUfZPkgyatjoxIMexLBCafxxHFCP6ewiYKyLIjbf0iEbJR-4lU6WmBWP9iM1ZgShfMdc0sT6coH_zZfcQt20ASAKdppOyCzLlO1gxzSn5dnzitNBIHim7BakKHEDX-m3XmrITCLNR9keYAfyIzB6SuQuTGXu924sOgf4YBjXQXMGu9FFmdlPE_8q78x8EBeAHP7LaWxAtrepZ4UZ_byy197x_gZi4tNtPo4q9PQti-0y5RFoozpOfEfluA3-ame-6FPO0CtlbnFV14edw4Kolbt1LNpRvx5ugI_mbiH-ZbwmkJsPWkcUcq87PNw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 982K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 14:17:28</div>
<hr>

<div class="tg-post" id="msg-127368">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوری/سخنگوی وزارت خارجه: متن توافق پایان درگیری ایران و آمریکا تقریباً نهایی شده و منتظر تأیید نهایی نهادهای تصمیم‌گیر است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/alonews/127368" target="_blank">📅 14:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127367">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فوری/سخنگوی وزارت خارجه:
متن توافق پایان درگیری ایران و آمریکا تقریباً نهایی شده و منتظر تأیید نهایی نهادهای تصمیم‌گیر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/127367" target="_blank">📅 14:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127366">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
فرودگاه هامبورگ در پی یک حادثه امنیتی تخلیه شد
🔴
شبکه ان‌دی‌آر به‌نقل از پلیس هامبورگ اعلام کرد که فرودگاه این شهر در پی یک حادثه امنیتی به‌طور کامل تخلیه و تمام پروازهای آن متوقف شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/127366" target="_blank">📅 14:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127365">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
خبرگزاری دولت: هدف اصلی امضای تفاهم‌نامه، پایان جنگ در تمامی جبهه‌ها در منطقه است. در این تفاهم‌نامه پایان جنگ علیه ایران به اضافه تمامی جبهه‌های دیگر منطقه به شمول لبنان مورد اشاره قرار گرفته‌است.
🔴
نام کشور لبنان به عنوان بخشی از توافق پایان جنگ در صورت امضای متن فعلی تفاهم‌نامه مورد اشاره قرار گرفته‌است و
آمریکا تعهد می‌دهد که رژیم اسرائیل را وادار به پایان جنگ در لبنان، کند
.
🔴
عبارت تمدید آتش‌بس در متن فعلی ذکر نشده‌است و اشاره به چنین عبارتی در برخی گزارش‌های رسانه‌ای نادرست است؛ متن تفاهم‌نامه خواهان پایان قاطع جنگ در تمام جبهه‌ها می‌شود.
🔴
تهران تضمین‌های روشنی برای آزادی دارایی‌های مسدود شده بر اساس ساز و کارهای مشخص و مورد نظر تهران دریافت کرده‌ است و در صورت تصمیم تهران به امضای تفاهم‌نامه پایان جنگ، بخشی از دارایی‌های مسدود شده بلافاصله و بقیه به تدریج در طول مذاکرات، آزاد خواهند شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/127365" target="_blank">📅 14:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127364">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d242dab561.mp4?token=JGKdn5b7yDy57MCt4hz2TAmRzj23h1aROemnkSm6c7FZ7Ma8AZ09nEes0muSv3aXZPx2tuhMLLThvaGO29hCLrbyPt-oTlMsJ7sIeX0w04quIAjANzuhnlE6cUvFPxtimCHztQgCEMnoQU2uFWJkyq-BCeZSO_4iATaJCVMj8NoT9b-KVIHLCRiMTEv2DnkraeoVQyOsiSjGxD2cOaFH4Z6i3TZxwZBiOltm_1m56PNngmBABHgnAINHhfQdodednOuwyc0J51fT3B-ckp3gIJyqcyIqvjEaN3Y7jaJ1PjS56lb5tEnsULB7uiMyEjb-liJGE1cbW6D3O8UaC48JUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d242dab561.mp4?token=JGKdn5b7yDy57MCt4hz2TAmRzj23h1aROemnkSm6c7FZ7Ma8AZ09nEes0muSv3aXZPx2tuhMLLThvaGO29hCLrbyPt-oTlMsJ7sIeX0w04quIAjANzuhnlE6cUvFPxtimCHztQgCEMnoQU2uFWJkyq-BCeZSO_4iATaJCVMj8NoT9b-KVIHLCRiMTEv2DnkraeoVQyOsiSjGxD2cOaFH4Z6i3TZxwZBiOltm_1m56PNngmBABHgnAINHhfQdodednOuwyc0J51fT3B-ckp3gIJyqcyIqvjEaN3Y7jaJ1PjS56lb5tEnsULB7uiMyEjb-liJGE1cbW6D3O8UaC48JUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ملت وقتی به تحلیل‌های خوش چشم اعتماد کردن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/127364" target="_blank">📅 13:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127363">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
خبرگزاری دولت: متن نهایی تفاهم‌نامه تا زمان پذیرش قطعی آن توسط دو طرف منتشر نخواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/127363" target="_blank">📅 13:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127362">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
خبرگزاری دولت: به گفته سخنگوی وزارت امور خارجه جمهوری اسلامی ایران، کلیات و متن تفاهم‌نامه پایان جنگ میان ایران و آمریکا تقریباً نهایی شده‌است و در انتظار تصمیم نهایی نهادهای تصمیم‌گیری در ایران است
🔴
تهران در طول دوران تبادل پیام‌ها، برای اطمینان از اجرای برخی مفاد تفاهم‌نامه تضمین‌های معتبری از برخی طرف‌های ثالث برای اجرای تعهدات پیش‌بینی شده دریافت کرده‌است
🔴
بر خلاف برخی ادعاها که از سوی برخی جریان‌ها و فعالان سیاسی در طول قریب به یک ماه گذشته مطرح شده‌است، متن تفاهم‌نامه پایان جنگ میان ایران و آمریکا با دقت و وسواس بسیار تهیه شده‌است تا جای هیچگونه تفسیر به رأی و فرار از تعهدی برای طرف مقابل وجود نداشته‌باشد.
🔴
تا زمان پذیرش کامل متن توسط جمهوری اسلامی ایران، تمامی متن‌های منتشر شده در رسانه‌ها، صرفا گمانه‌زنی‌های رسانه‌ای هستند و متن نهایی تلقی نمی‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/127362" target="_blank">📅 13:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127361">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/127361" target="_blank">📅 13:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127360">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
پزشکیان: ملت ایران با وجود همهٔ فشارها و تهدیدها، از استقلال، عزت و تمامیت ارضی کشور دفاع خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/127360" target="_blank">📅 13:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127359">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
تسنیم به نقل از منابع آگاه: فشار نظامی و دیپلماتیک آمریکا برای تغییر در متن ۱۴ ماده‌ای پاسخ نداده و آمریکا از طریق واسطه قطری اعلام کرده است که نیازی به اصلاحیه‌های اخیر آمریکا نیست.
🔴
این متن همچنان نیازمند بررسی و نهایی شدن در نهادهای ذیربط در ایران است و تا آن زمان سایر گمانه زنی‌ها و خبرها، معتبر نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/127359" target="_blank">📅 13:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127358">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
اسرائیل هیوم: ایران موافقت کرده است اورانیوم غنی‌شده خود را تحویل دهد.
🔴
از غنی‌سازی بلندمدت صرف‌نظر کندو  آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.
🔴
ایران باید متعهد شود که به دنبال دستیابی به سلاح هسته‌ای نباشد. تنگه هرمز بدون محدودیت باز خواهد شد. هر دو طرف متعهد می‌شوند که اقدامات نظامی بیشتری علیه یکدیگر انجام ندهند.
🔴
پرونده لبنان همچنان شکافی بین آمریکا و ایران باقی مانده است. انتظار می‌رود یادداشت تفاهم روز یکشنبه در ژنو امضا شود، در حالی که ترامپ برای اجلاس جی۷ در فرانسه حضور دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/127358" target="_blank">📅 13:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127357">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
کلش ریپورت: مصر و ترکیه در حال برگزاری یک تمرین هوایی مشترک در چندین پایگاه هوایی مصر هستند.
🔴
این تمرین شامل مراحل نظری (یکپارچه‌سازی مفاهیم رزمی، تبادل تخصص‌های آموزشی) و پروازهای عملیاتی متمرکز بر مأموریت‌های عملیاتی مشترک است.
🔴
هیچ نوع هواپیما یا تعداد آن‌ها به صورت عمومی اعلام نشده است
🔴
این تمرین پس از مانور دریایی مشترک «دریای دوستی» در سپتامبر ۲۰۲۵ برگزار می‌شود، که اولین تمرین‌های دریایی مصر و ترکیه در ۱۳ سال گذشته بود.
🔴
دو سال پیش، برگزاری یک تمرین هوایی مشترک بین این دو کشور غیرقابل تصور بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/127357" target="_blank">📅 13:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127355">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
فارس: آمریکا عقب‌نشینی کرده، ایران بررسی را آغاز کرده و هنوز هیچ توافقی حاصل نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/127355" target="_blank">📅 13:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127354">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
بلومبرگ به نقل از یک مقام گروه هفت: توافق بین واشنگتن و تهران به احتمال زیاد یک یادداشت تفاهم خواهد بود، نه یک توافق نهایی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/127354" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127353">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
بلومبرگ به نقل از منابع: توافق بین تهران و واشنگتن ممکن است یکشنبه آینده در ژنو امضا شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/127353" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127352">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a72e0fc3c.mp4?token=lKatXpEwNURKls4j4gWoSMdvwO0P1NPPGSrNPA96bfGGJmxPJ4KsR48zzLIyVObbbPZydJgZGbHcPR2fLCd9Gv_dYyESssNoZj8tnipesNQmak0GhMhKvRekUgLm6bzWyiN5q9SF0feAUWyQnZISSzqceSHFVRQamBZDwTtr6tTClUQs-5boIbxSeWgSiC6tv18mCwksM1VfOb1OaHvHTs1gi3tNwIuKKy2hmwWWxOHzBMUqGKSWAYExaflyDeba9MYPAWL3XIoWo59E7_vut7BX9dY_wkP--bh1-gXT8H1IH4b8y_gProKrf3HLHJUo-BUigotmQwFJYkH6q271oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a72e0fc3c.mp4?token=lKatXpEwNURKls4j4gWoSMdvwO0P1NPPGSrNPA96bfGGJmxPJ4KsR48zzLIyVObbbPZydJgZGbHcPR2fLCd9Gv_dYyESssNoZj8tnipesNQmak0GhMhKvRekUgLm6bzWyiN5q9SF0feAUWyQnZISSzqceSHFVRQamBZDwTtr6tTClUQs-5boIbxSeWgSiC6tv18mCwksM1VfOb1OaHvHTs1gi3tNwIuKKy2hmwWWxOHzBMUqGKSWAYExaflyDeba9MYPAWL3XIoWo59E7_vut7BX9dY_wkP--bh1-gXT8H1IH4b8y_gProKrf3HLHJUo-BUigotmQwFJYkH6q271oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی هوایی اسرائیل داره به روستای تبنین تو جنوب لُبنان حملهِ می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/127352" target="_blank">📅 12:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127351">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
مقامات گروه ۷: تفاهم‌نامه آمریکا و ایران ممکن است همین یکشنبه در ژنو امضا شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/127351" target="_blank">📅 12:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127350">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceca5f8bc2.mp4?token=a5TlP1OoWLXNgZDI01dyhFAGsfLlcAoQ3Dxo20N6AK8WYcQUjOYHIAIvErikXN4FH2K46iylm7bu_wmi5VaR0GVaJRZ8J9mLzdyafJLdKlmgifY_gQXAqcKNNoq4_9K0aP3kWGmZCQEWy33HiCRdP8_oeQb029ddMyKTafnj3zQeulDHIVZIEWX_WWBJLdPsyksO7b9oF0as4Po41BuGLdRziaC4lT6409g2vrcF-bjYrPC6tS1RXMNXrbBvfDvbasCEAFkN9n7tPE_PDpffvnO4zwlhVFjmWG9goLn3FtvJHZpX2aQmNF75KlGi_QLjtHYiWpGp0cVbAWXoJytEoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceca5f8bc2.mp4?token=a5TlP1OoWLXNgZDI01dyhFAGsfLlcAoQ3Dxo20N6AK8WYcQUjOYHIAIvErikXN4FH2K46iylm7bu_wmi5VaR0GVaJRZ8J9mLzdyafJLdKlmgifY_gQXAqcKNNoq4_9K0aP3kWGmZCQEWy33HiCRdP8_oeQb029ddMyKTafnj3zQeulDHIVZIEWX_WWBJLdPsyksO7b9oF0as4Po41BuGLdRziaC4lT6409g2vrcF-bjYrPC6tS1RXMNXrbBvfDvbasCEAFkN9n7tPE_PDpffvnO4zwlhVFjmWG9goLn3FtvJHZpX2aQmNF75KlGi_QLjtHYiWpGp0cVbAWXoJytEoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست به مناسبت توافق ۴۴تا پرس سینه زد و فیلمشو منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/127350" target="_blank">📅 12:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127349">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
خبرنگار العربیه: یک تیم حقوقی پاکستانی در مراسم امضای توافق ایران و آمریکا در یک کشور اروپایی حضور خواهد داشت.
🔴
ایران درخواست کرده است که امضای توافق با آمریکا در یک کشور اروپایی انجام شود تا به آن جنبه بین‌المللی بدهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/127349" target="_blank">📅 12:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127348">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
مقام آمریکایی به Reuters : دو تا پهپاد ایرانی دیشب خواستن به کشتی‌های تجاری تو تنگه هرمز حملهِ کنن، ولی رهگیری کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/127348" target="_blank">📅 12:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127347">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
رسانه عبری i24: از جزئیات توافقی که تاکنون اعلام شده کاملاً مشخص است که ایران تضمین‌هایی از آمریکایی دریافت خواهد کرد مبنی بر این‌که اسرائیل تا پایان دوران ترامپ هیچ‌گونه فعالیتی در خاک ایران انجام ندهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/127347" target="_blank">📅 12:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127346">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: مذاکرات نهایی ایران و آمریکا بر مسائل اقتصادی و هسته‌ای متمرکز خواهد بود و شامل بحث‌هایی درباره برنامه موشک‌های بالستیک ایران نخواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/127346" target="_blank">📅 12:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127345">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
عضو کمیسیون عمران: بیش از ۷۰ درصد درآمد خانوار صرف اجاره خانه می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/127345" target="_blank">📅 12:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127344">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f73bf5f98.mp4?token=NYnz8TZqEoIVD94pGQiIrdGTe8vmbktUyE-oObcd6T7aCJMxu9UHgVJvUakYvp34WW_sIielbWWw_7w5SZlRIeKQ9pG63C4GN-vIqlw4abeRTqmL5YS7WIifIrU2qTe8M7W7Z_Q6v0c4GmSfHcFiPdrR7a00D2FoVvPdbXOaMF6zQcLaWbD2xkh98eWMx3a_GSwc6VpiANB62Dtc5y3wp_AIMAOll-mjGqgIu3lCoXBi9dP3AsmnmnmYlBRK0rHUNfHMnV9rppO2bmTgRLY9eKOogGYk-i-duxzx-UV4_g2Pf4wo5rDe_OSk6YuQSjsZ2WBgV7uzMK8RMT_qLBaMtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f73bf5f98.mp4?token=NYnz8TZqEoIVD94pGQiIrdGTe8vmbktUyE-oObcd6T7aCJMxu9UHgVJvUakYvp34WW_sIielbWWw_7w5SZlRIeKQ9pG63C4GN-vIqlw4abeRTqmL5YS7WIifIrU2qTe8M7W7Z_Q6v0c4GmSfHcFiPdrR7a00D2FoVvPdbXOaMF6zQcLaWbD2xkh98eWMx3a_GSwc6VpiANB62Dtc5y3wp_AIMAOll-mjGqgIu3lCoXBi9dP3AsmnmnmYlBRK0rHUNfHMnV9rppO2bmTgRLY9eKOogGYk-i-duxzx-UV4_g2Pf4wo5rDe_OSk6YuQSjsZ2WBgV7uzMK8RMT_qLBaMtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری صدا سیما: هک تصویر انفجار اتمی در تلویزیون، سیگنال آمریکا بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/127344" target="_blank">📅 12:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127343">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
مراد ویسی: با توافق احتمالی، دست ترامپ هم به خون جوانان کشته شده دی ماه آغشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/127343" target="_blank">📅 12:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127342">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2UimXL6VVz2lUflquN0DHzcF2aOMo86b1xL_eAVW6l4SL9k2YBShxXT-2L-7B9idAMz0yyfYpvPTyxr7ra9e7MrGPt71ADjwr8g4J8QY6EyxCi80UxTu1K-04i92OJZh4iiQaF96BAkrCId5BiA5ZLdV1ANJm5DUJlne703N08LluIRCShlN414KUik0wy_KwOw9wqaHFNbjotmja81D9pEOupSFK-1fd7W1QFVyVvpAhZf-gOYhaD1Q9ZaLrhGMAOUaBjhSMYvOFnZOG4zp0ru76I7J6bu4IGRC2B-t66aD0or2Ptxxq_VeOAe1CFjdGcTSipPF_uyg_cVZttNCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبی:هنوز ویزاها نیامده است
امیدوارم اینفانتینو به وعده‌هایش عمل کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/127342" target="_blank">📅 12:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127341">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3dQTKeNr4kqR-hE79fFx0rGYEQB4zqg2Xbh0GKR6aUekxSvKpz9BjYguFyv4hHS9FrRGhOAXysjrktDz9s5Lt9Hx8q1Qev0TBs8suTQbO9_s8kfE9YpMMDowl9g6Rix_dB3AGfPoruI6QvBum9JDA7h3WyOs1PUks7MPK6Yf7K_1PmpudSToROa7V12uVhgd5zCEB6jlxn4QI-TRvLnZflXBaxC8fqRpFwpgxaQw093SsO4qUTysUC4LWjVkQ_ueyfqnUmisPSBVEqvagm3iXmrvG1kCVGROdsP34fyFW-mXQ-vR2GL4tv8VNclR1wfJcQKb7Adzct4OPL2iwhkgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کلش ریپورت: به نظر می‌رسد ایران به رادار هشدار اولیه AR-327 در جبل الدخان، بلندترین نقطه بحرین با ارتفاع ۱۳۴ متر، حمله کرده است.
🔴
این سایت میزبان یک رادار مراقبت هوایی سه‌بعدی برد بلند ساخت شرکت بریتانیایی BAE Systems با برد حدود ۴۷۰ کیلومتر است که در یک رادوم ثابت قرار دارد و مسیرهای دریایی خلیج فارس و مسیرهای هوایی منتهی به تنگه هرمز را تحت نظر دارد.
🔴
ستون‌های دود در تصاویر منتشرشده توسط ایران، توسط تحلیلگران OSINT به‌طور مستقیم به محوطه راداری در مختصات حدود ‎26.0375°N, 50.5420°E‎ مکان‌یابی شده‌اند.
🔴
این رادار یکی از گره‌های شبکه منطقه‌ای هشدار اولیه و دفاع موشکی مرتبط با ایالات متحده است که به عملیات ناوگان پنجم (Fifth Fleet) متصل می‌باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/127341" target="_blank">📅 12:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127340">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wv20CWZC0OoDGB1Ih_aLUns8FNycgb2NiedQroI1m_1rPm5HAeHSJBvbkfkpjQF_gN9TAB-Z6J-tDXU42AMz5Do7zshanklgrh8-Uw_qYhR6p7CmmAeyY18rPDqUjbgMB4mg9BEEu3CfgFcHNCbLZ91L73b3-6rh2zUmtOCBGNnJzJqWNwNiMu_6hsYNAiTEqXdiMyFNk7v5fT4ZE1kDhGwMUAxdx5uSGIkJ5tbpsQjTOZ1-6TKjWOV7Vxz5Ar1htSgCIyyQoGU0Uwivlp28WEEMbLzr9TYABCNR3jm_LGXk_Hm41cx_AJ-n9hDyHHir677gmnKLH7feV5utjy7bLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت آمریکا در ساعات گذشته ۳.۲ درصد کاهش یافت و به پایین‌ترین حد خود در ۵۶ روز گذشته یعنی ۸۲ دلار رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/127340" target="_blank">📅 12:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127338">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
تصویری وایرال شده از تجمعات شبانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/127338" target="_blank">📅 12:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127337">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
حاییم رامون، وزیر پیشین اسرائیل:
توافق میان واشنگتن و تهران توافقی بد است و به اسرائیل آسیب می‌زند؛ همچنین این توافق پیامدهایی برای سرنوشت سیاسی نتانیاهو نیز دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/127337" target="_blank">📅 12:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127336">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBSMawcaTjf4JzyJ8UQbhCV9omxQAnY-EgTDPotgeZTeMPfAFz5WNI6QAgiWbHCSABrHuCFnCU9dcqxxpkLugZoOmnCT7EpxwAZrHVo9G1KxHXcx-96G6PEzXbJguYGTaJX_WkR9tlPZgHsjUvNQM2D2aR90_OqggT0kJaWdx_tRyJKU9xvGk6W_NiGISIM8ofY-WZXfqa4Je9ZiUdzF7C_gtSgaWhEi-LcJOXArO1KsIOEdqj4XRlKdeVWG9QfTvqoFTsUtD-g_WI0zKyIHGbMQSIqndjjxWS023BDo2_WK4lhDUX_AieYf6ENWz08iugI4rmKoGkOgVSh7gb__Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای روسی بیش از نیمی از کنستانتینوکا در منطقه دونتسک را پس از عقب‌نشینی بی‌صدا نیروهای اوکراینی از حومه جنوب غربی، تصرف کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/127336" target="_blank">📅 11:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127335">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYAjA6ESLwdhGwt58rEdPP4jWdeHQzOwmdjsZvDRpp2n7t-4RhdihEOF6htbbtNODWFFzVrR-7vLLtLqgmhPK1KEqrFlYNwkz79GQWTXzkEfAzeKVHF6FSnhJ2-DPesDFWDnSiGYXjmHv6MO-0H57-kr8X-Osrhizx-CjeFrs8zeTS-P5hL4qFhFaaRrJXRHCfrg3_oFEEyqAriMH3Itp7fPUMzVZitdTX21Rl4Uz6sAaq_nCY1HSfzfQ75-MxmMVf1YAwZJRXrAGHOtagKx1hh7VzLVJFRfkYURQO_yXIp4hytfmxVO8_IG2de8ajlQRQgEQpw-coyM7sUlAir9Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/127335" target="_blank">📅 11:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127333">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
مهر: جزئیات جدید از پیش نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا توسط منبع نزدیک به تیم مذاکره کننده ایرانی منتشر شد.
🔴
جزییات این پیش‌نویس به شرح ذیل است:
۱-
توقف دائمی و فوری جنگ در همه جبهه ها از جمله لبنان
۲-
تعهد آمریکا به عدم مداخله در امور داخلی ایران و احترام به حاکمیت جمهوری اسلامی ایران.
۳-
رفع کامل محاصره دریایی ظرف ۳۰ روز
۴-
تعهد آمریکا به خروج نیروهایش از پیرامون ایران
۵-
بازگشایی تنگه هرمز ظرف ۳۰ روز با ترتیبات ایرانی
۶-
تعلیق تحریم های فروش نفت، محصولات پتروشیمی و مشتقات و دسترسی کامل ایران به منابع مالی آن.
۷-
لزوم ارائه طرح های بازسازی ایران حداقل به مبلغ ۳۰۰ میلیارد دلار توسط آمریکا و متحدانش
۸-
۶۰ روز مذاکره برای رسیدن به توافق نهایی مبتنی بر موضوعات هسته ای و لغو کامل تحریم های اولیه، ثانویه، آمریکا و قطعنامه های شورای امنیت سازمان ملل و شورای حکام آژانس بین المللی انرژی اتمی
۹-
تکرار تعهد ایران در پیمان ان پی تی مبنی بر عدم تولید سلاح هسته ای
۱۰-
در دوره مذاکرات آمریکا متعهد شده به نیروهای خود در منطقه اضافه نمی کند و تحریم جدیدی هم وضع نخواهد کرد.
۱۱-
آزادسازی ۲۴ میلیارد دلار پول های بلوکه شده ایران در دوره ۶۰ روزه مذاکرات نهایی. نیمی از این مبلغ قبل از شروع مذاکرات باید در دسترس ایران قرار گیرد.
۱۲-
تشکیل سازوکار نظارتی برای اجرایی کردن توافق.
۱۳-
توافق نامه نهایی توسط قطعنامه شورای امنیت سازمان ملل به تایید می رسد.
۱۴-
مذاکره نهایی قبل از آزادسازی نیمی از پول های بلوکه شده ایران، تعلیق تحریم های نفتی ایران و رفع محاصره دریایی آغاز نمی شود و توافق نهایی صرفا در موضوع سرنوشت مواد غنی شده و غنی سازی، رفع تحریم ها، برنامه بازسازی اقتصاد ایران انجام می شود و بحث درباره برنامه موشکی ایران و حمایت از گروه های مقاومت به صورت قطعی از دستور کار خارج شده است.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/127333" target="_blank">📅 11:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127332">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
نیوزویک به نقل از یک منبع آگاه گفت ترامپ به نتانیاهو هشدار داده که در روتد توافق دخالت نکند و الا با اسرائیل برخورد خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/127332" target="_blank">📅 11:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127331">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
یدیعوت آحارونوت:
نتانیاهو، گفته است که به ترامپ تأکید کرده که درک می‌کند او در پی دستیابی به توافقی با ایران است،
اما اسرائیل نباید قربانی این توافق شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/127331" target="_blank">📅 11:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127330">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snmcZ7fg0Xf5KS33IEkDLKqS_oFkql_AIudsR3g9xkHWlnMDaBoZxW2ToO-zKjh6Hi-tnaD52Wh8a0c62QH5gjhs2uHmpPPGOqmyxpzhDs-RqLUYoujrxf7Vr9J-P6S1Sp3fE2KDGK507s6OpVb7NBhNBvwlktmorTWRyKTEMQIK0ryfSVeNWUqmaQ8PYfpL9i-DUP8ORrpz4sym_Mm0N8v6mDiBob-nmMCHW-EFcRXXmwJlYEshTQYB5YMcDTSkYrFfMFui5cXLlZNLtbaJgBUASjYXPs0Ff2_sOnt3fmuk_Ks7E_0_hYLTMEhYd2M9kkYsgtJniAtCzYEuTYxbEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا قالیباف هم به ژنو خواهد رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/127330" target="_blank">📅 11:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127329">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
الاخبار: ایران پاسخ نهایی را از ایالات متحده دریافت کرده که مبنی بر گنجاندن لبنان در تفاهم‌نامه‌های آتش‌بس است
🔴
تفاهم‌نامه پیشنهادی شامل توقف کامل عملیات نظامی، تعیین جدول زمانی برای خروج اشغالگران از خاک لبنان، توقف عملیات تخریب و آزادی زندانیان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/127329" target="_blank">📅 11:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127327">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6ghQi0B_-WYdcr1PrMwlmdeR_yWQeOFRUg3tmcb2mGMWGTgddM456G99dd1jk32qiYbxFxkPph3G-2pJIfroKWl2tPHmKiySmLtfdLp9sNBk_RrNczqXiQo6AYFZKK6q5iErdI4I87eItW9e2Q1UGzePtxcs7kMlHsNrVPomcdB4kZ7MtuZvxfmUj3uVPuGPVGc5FEAiEGg8JPUQ0qDQxf4FUkE1X8jhWw7XMbBqFUTUTJO8yv1cK3R_cKue2y_H-CXbXuJQYfeMLXl8rBnp2Iv_HIXbUmBCA75_nSP4qudTPJGAFWJJUeMa5drkIp80ERZ1a19NRx-iiUujGdHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fozkoj5HCbV9lqwJrpa25ItbGKBcD5HS_b1awD4RXuWThVosslymCrDcZt88Ik5R3oPIpj44lLUn3EYDkZDXojQ-YWTSIaVPl1uVIVkl0boLvCi0zyJ1VIuT-uVno7LN1VrWEQBGy_ob5667IclGQy8eQbivwShH48eit5vU1OoQL8FDL47mc7-gDlviiiHtkWcrof1X1Sm7KbmKTl_ARmGeO03E_7geBQ80pAvbTFmqAnL4stq6waOZIg5kxFQ9m68ilJlMidfEacNQ0-Asj3Y4TD9B-uRjBJt_THEqj5v2L7fmEDTNulncnLG1DFiGhpmJkoOOuh9GWOu_ginJxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصویری از کابین دو نسخه متفاوت از بالگرد شینوک
🔴
نسخه قدیمی‌تر سی که در دهه ۱۹۷۰ ساخته شد و در ایران نیز خدمت کرد
و کابین آخرین نسخه تولیدی که هم اکنون نیز در حال تولید است نسخه اف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/127327" target="_blank">📅 11:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127326">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
آکسیوس: هواپیمای آمریکایی حامل تجهیزات جی دی ونس برای امضای توافق احتمالی با ایران دیروز به اروپا پرواز کرد‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/127326" target="_blank">📅 11:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127325">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
اکسیوس :  توافق ایران و آمریکا در ژنو سوئیس امضا خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127325" target="_blank">📅 11:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127324">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
پولتیکو به نقل از مقامات آمریکایی: پس از آنکه رئیس جمهور آمریکا صبح پنج‌شنبه ایران را تهدید به حمله مجدد کرد، امیر قطر، رئیس امارات و مارشال عاصم منیر فرمانده ارتش پاکستان  با ترامپ تماس گرفتند
🔴
آن‌ها به او اطمینان دادند که یک توافق اولیه که راه را برای مذاکرات جزئی‌تر هموار می‌کند، در واقع در دسترس است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127324" target="_blank">📅 11:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127323">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
خبرنگار الجزیره:  تاکنون، هیچ تصمیم نهایی در تهران در مورد تفاهم‌نامه با ایالات متحده گرفته نشده است. هرگونه توافقی باید از لایه‌های مختلف فرآیند تصمیم‌گیری کشور عبور کند.
🔴
برداشت من این است که بیشتر مراحلی که تصویب را تسهیل می‌کنند، پشت سر گذاشته شده است، اما در سطح تصمیم‌گیری نهایی همچنان با مشکلاتی مواجه است. اکنون شبی طولانی از جلسات در جریان است و نتیجه آن هنوز نامشخص است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127323" target="_blank">📅 11:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127322">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
منابع آگاه مدعی‌اند لبنان نیز در توافق ایران و آمریکا گنجانده شده و پایان جنگ شامل توقف کامل عملیات، خروج اسرائیل و آزادی اسیران لبنانی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127322" target="_blank">📅 10:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127321">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
الجزیره: بازارهای سهام پس از اعلام دونالد ترامپ، رئیس جمهور آمریکا، مبنی بر لغو حملات برنامه‌ریزی شده علیه ایران و قریب‌الوقوع بودن توافق صلح با تهران، افزایش یافته‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127321" target="_blank">📅 10:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127320">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4cQc8DLCsGTuNwk3Vq5RFF9NPWwFsfOEFH-NAa_0C4J5Wil2ZDrsVJ6tKuDeWzkr4VjLF6wFhLIgf9fJEpN_aoff7_F1QGVu23ynuQZAsH3co7tpKlJfVIT0IiHtHbb68rablEqIrNuEa_MVdyu8QdvVGZJ7d_o7XiJUQQf1Hp9I4FUpIrje_YAWCxDDKitiTCjC7HWtVemsmrm5LF3QU_d8O8GtTMklDzyCzZI-hAqvJZt7V1LOGe5hMTTc9hLPw0twF4KX3nwWSfL_TD3jBFbyau-zhQEsWkeD61ayp0aR4PqPiZRr5mDaEo4DarDgUwxlWWMfpERg1TPSkhJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جروزالم پست: رهبران جنوب آسیا و خلیج فارس برای جلوگیری از حمله ترامپ به ایران با هم رقابت کردند و به او توافقی ارائه دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/127320" target="_blank">📅 10:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127319">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYleyv84kTZxwojKK8ZWosKqRsFypDBS_c1T5L2DACcelyUIsHPxn8FudtZ2ggNg1Vvq8Vy83nElcSlN_QLJIjhBHbygz4mENobjVKH_dBV6SoPCi1qpCc8-t5PhQNe5NxfzlKnY4PCaV6klviW4wmUKGr8QLPTuWzGn3nPiobRa41qwcHnzw2pzsP0Z5OUO5vHTi04cJSykbGJcMbXVLsj5rpK73MKrRIcTHscKsPud45DLfl2X0Y_SsGbP3E2CxCeHE-LVqQkKzIXr0gG6wYuWu0EHJCw8eAN2t0TkBhJcvCnRPvxLq77B62Fn-CllMWeptk69_RJ-u_63spAS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: امیدها برای صلح بین ایران و ایالات متحده افزایش یافت پس از آنکه رئیس جمهور ترامپ گفت که به محض این آخر هفته می تواند توافق نامه امضا شود ، حتی اگر تهران گفت که تصمیم نهایی در مورد پیمان اتخاذ نکرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/127319" target="_blank">📅 10:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127318">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9d9b52544.mp4?token=ZQe-6MpCJRwdA5O-rqyWiwU0gJgOm3DQAO5Dr-V_VWEN6kFH2ZRuP0_GxueFs7c2vEXl4LQLmIDNOY-p5H8inJsaKygscTf5Qoe4iT9EjffVQ4Q1VA1BJ5ajZ6XhCU2jOU9Z_2B_jjAnWzo_rX-dNPvDj7BHsPtNIaf1s57RPXBsCKZSPsN4u4KJQ7q7H1I3fYF5ARAfqOKXD-YVpn-nHk_cb3HxyQVzcRFadGbCwsgS1xfT_0w8Aqw5yKbATKFrT4EPGL55P6UIQEBzPvBGThG4GOaKToLcPncYWqdM-U5r7Aj6MveC5NWt1WztFAg-qajiGAV1Zx536NJ0HRiCcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9d9b52544.mp4?token=ZQe-6MpCJRwdA5O-rqyWiwU0gJgOm3DQAO5Dr-V_VWEN6kFH2ZRuP0_GxueFs7c2vEXl4LQLmIDNOY-p5H8inJsaKygscTf5Qoe4iT9EjffVQ4Q1VA1BJ5ajZ6XhCU2jOU9Z_2B_jjAnWzo_rX-dNPvDj7BHsPtNIaf1s57RPXBsCKZSPsN4u4KJQ7q7H1I3fYF5ARAfqOKXD-YVpn-nHk_cb3HxyQVzcRFadGbCwsgS1xfT_0w8Aqw5yKbATKFrT4EPGL55P6UIQEBzPvBGThG4GOaKToLcPncYWqdM-U5r7Aj6MveC5NWt1WztFAg-qajiGAV1Zx536NJ0HRiCcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گروهی از دختران که با حجاب کامل در حال قدم زدن بودند توسط افراد طالبان با ماشین زیر گرفته شدند!!!
🔴
در افغانستان زنان دیگه اجازه نفس کشیدن هم ندارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127318" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127317">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVEmsWqKccQGfzOVRsCdNiwNEjDLcfQg2tswYmOX25nsIV0cycuQ7R3D0Gn1pW-vE-LNZE5avcDVuPmfdqzaRL7uMpIFWzIK2TVY_xuf_7JIZYvGrXufqQAMIIqhv7csWK8xRbxSlvHUIDyFKFV4UJmwoHECLXTQ9M3w_6uIWn8e6QUk2QZossnBMGIYs9re_nOEyNGAhWhHIhVb6XIUbkaOsX_ImncBMqhPf9hYzDqdHCQiorO28Q2Omk0M9MkyQH8D0s0IrBjrTZYeTZMq7JGFKSxR6DnJJVlTcne_oPPUbQephjH6NWvU-zhGH4dUvzd1eJmiTgN7jdMfqnNvVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکونومیست: آشفتگی‌ای که دونالد ترامپ با شروع جنگ با ایران ایجاد کرد، می‌تواند بیش از آنچه بازارها انتظار دارند، طول بکشد. جهان باید برای قیمت‌های بالاتر انرژی آماده شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/127317" target="_blank">📅 10:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127316">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
یدیعوت آحارانوت به نقل از منابع: نتانیاهو گفت به ترامپ اطمینان داده که تمایل او برای توافق با ایران را درک می‌کند، اما اسرائیل نباید قربانی شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/127316" target="_blank">📅 10:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127315">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وال‌استریت ژورنال به نقل از مقام‌های آمریکایی: واشنگتن در روزهای اخیر عمداً از حمله به زیرساخت‌های ایران خودداری کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127315" target="_blank">📅 10:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127314">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
جی‌دی ونس، معاون اول رئیس‌جمهور آمریکا در مصاحبه‌ای با شبکه CBS گفت که بنیامین نتانیاهو «قطعاً در چیزی اشتباه کرده است»، که جدیدترین نشانه از فاصله گرفتن آمریکا از اسرائیل به امید حل و فصل جنگ است
🔴
ونس همچنین اذعان کرد که نتانیاهو «به شدت منافع کشورش را دنبال می‌کند - گاهی این به معنای هم‌نظر بودن ماست و گاهی به معنای نبود آن است»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/127314" target="_blank">📅 10:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127313">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
آکسیوس: موضوع دارایی‌های بلوکه‌شده ممکن است در قالب یک توافق محرمانه جانبی حل‌وفصل شده باشد؛ هرچند یک مقام آمریکایی اخیراً این احتمال را رد کرده است.
🔴
به گفته یک مقام آمریکایی و یک منبع از کشورهای میانجی، آمریکا، ایران و قطر در روزهای اخیر درباره سازوکاری گفت‌وگو کرده‌اند که بر اساس آن ایران بتواند برای خرید کالاهای بشردوستانه به بخشی از دارایی‌های مسدودشده خود در قطر دسترسی پیدا کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127313" target="_blank">📅 10:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127312">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5ryeq1oMpITe1OApp-FB8t6SE2D4LMPhK_zG4JdhyWFZpIUZJoaAsL4z0N7_rFxO0ORWH74lcP7uEO7yurfuk0XShco2xAUZQoiZBbU34dc3w85sV_aUroEAmZRKO2fPPNCUsHlTqy5AnVAummoXtEst4tYQadN1Xg5Q7GWLTHvOAYpIfywy-BNAmVOjzhGhM_hK5KsPj2kW4dWpuFkXnRyO3L6vKgZd8Vq5mss1JRKxcqT9M_u7BzyIZ1GVdkDR0VzXJWJLoup3sLzHmLSdy7i3c4zD6V27D3whIrLFVBVL_MgKmEiFBmruXetHGmBm-QcDHKcdmUQVgIYKSAkjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قدیمی ترین کتاب فارسی چاپ شده در لیدن، در سال ۱۶۳۹ که درباره دستور زبان فارسی است
🔴
لَیدن (به هلندی: Leiden) شهری دانشگاهی در استان هلند جنوبی و در نزدیکی لاهه در کشور هلند است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/127312" target="_blank">📅 09:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127311">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
رایزنی پادشاه بحرین و ترامپ درباره تحولات ایران و آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127311" target="_blank">📅 09:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127310">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
واشنگتن پست: جنگ ایران رشد اقتصادی جهان را به ضعیف‌ترین سطح خود از زمان کرونا خواهد رساند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127310" target="_blank">📅 09:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127309">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbepVtHBPl9x8R_dRc9RvYMx6y7Xf2Z4y2vmI8VTYXzr0U8J0rVsYpKZKOMaurYfG91oDmx7L6KKydoLnhkpoCKBz1-siyD2ELCCM7Bat5SCJcBu6NuyP0QtYykk3hyEP16khgsOinDQTfP_O-DTseFeC9hLR4LvxDUUpC148DCZvrCFJ7EB4QrNepJJbrT-QrP4GH9tmy0A5n7rVl0SG_VNq6tum6lsqodUUxjhu6lQM_bQ4eekBrM_w8lUq8iVVPkg1d65sAnHm0yGQpeWXlbVTzc0aHwQ8ONH0VE_qkA8OdpdL5l10PatftFx0XweuGQuxE0oGKKSgJKfvYvANw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس از بریدن سر یک انگلیسی توسط یک مهاجر سودانی در شهر بل‌فاست ایرلند شمالی و همچنین خبر تجاوز ۴مهاجر افغان به یک نوجوان بریتانیایی، شورش‌های گسترده‌ای علیه مهاجران مسلمان در بریتانیا رخ داده و ده‌های خانه و خودروی مهاجران توسط معترضین به آتش کشیده شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127309" target="_blank">📅 09:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127308">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: آمریکایی‌‌ها درحال القا هستند که جمهوری اسلامی تحت فشار به توافق رضایت داده است، در حالی که ما به هیچ عنوان از خطوط قرمز خود کوتاه نخواهیم آمد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127308" target="_blank">📅 09:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127307">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZorfLxeov3pZewynxWs_z3CVL9HyiROgyUSk9vGhTb7PXjl5Bx4g33qRBq1NwK74rl1f3_c2oJyfvEHnFFFqG1yUrRFgaYphDDMwbXPXpVvu5rxO1DiI_4Sh6X2tgHHaIdnwPo-ZkVbsaKUxlio_Bv3e0WNTpDYZ13EhzCqzbSMsTAp17MU31KtQD6W0-wYGwsNAL_JCGsLuHataqmNvodLnoYoB93L5uN6O6-UOvGMLUP3LLiq0ZJpDjKuK34AyHUu4ZEFiKlzERetoH83SQ2Tr-xPzxhPdRPzAjdmPmYiZFTbKHTFgjWNQA4PpmMf79yiOnmlRltQGApUOJcw7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت آمریکا به 85 دلار رسید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/127307" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127306">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
الجزیره به نقل از اکسیوس مفاد تفاهم‌نامه تهران و واشنگتن را اعلام کرد:
بازگشایی تنگه هرمز بدون وضع عوارض عبور در ازای رفع محاصره دریایی
🔴
کاهش تحریم‌های ایران مشروط به پایبندی به تعهدات
🔴
تمدید آتش‌بس به مدت ۶۰ روز (شامل لبنان)
🔴
چارچوبی برای مدیریت ذخایر اورانیوم غنی‌شده ایران
🔴
برگزاری مذاکرات هسته‌ای در دوره آتش‌بس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127306" target="_blank">📅 09:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127305">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سخنگوی فرماندهی مرکزی ایالات متحده در منطقه موسوم به سنتکام در گفت وگو با شبکه سی بی اس نیوز مدعی شد که در حال بررسی گزارش‌هایی مبنی بر حمله هوایی آمریکا به یک تاسیسات آب در جنوب ایران در روز چهارشنبه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127305" target="_blank">📅 09:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127304">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وزارت دفاع روسیه: دیشب ۲۳۱ پهپاد اوکراینی بر فراز چندین استان منهدم شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127304" target="_blank">📅 09:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127303">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DR3vPh_qTMNUIdmAjaYLp5FyAfoNlQdhYd6kFe185IcX8LLRm81W5maYJn2zZSE-HmOReCNyVGlq8MrO7Cu6Y_jLv6oYO1khppQQFwLUf_zhUkmVLIBNijSwdOrJfW3wj3gpNffUsDiaNeQjo76vnwcNoXzeDIHuT_rViGQClzyGfE5SRA2raazevZ_idZEDyZa8cU7R0VuXS6-gl63JSjD_VtSDom-57UWB5ZRL2d5A49LPgdo1acWStDyTC2CmQsIYqM-SVvpCpOzd3wxsOIiRj5y2jf2yGsd8OJJgINefsAYbZQcv99IB1VmChDU6beUmeLafTUGV1i9j_S7qUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دادگاهی در سئول «یون سوک یول»، رئیس‌جمهور پیشین کره جنوبی، را به اتهام ارسال پهپاد به کره شمالی و تلاش برای ایجاد بهانه‌ای جهت اعلام حکومت نظامی، به ۳۰ سال زندان محکوم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127303" target="_blank">📅 09:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127302">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbbvcNgHAUw6QzUWWLrTga9iY8iDuZ1FhQjqmYRX_H-SQZswhAhlgVn7ocpzaLfTHOiHoUYu2Wl7JIwejlHrC_UUx4G_Enh9GeZUyyrGzf31lppMqeyjGDskJRDZPTr1gTbl07BXZLSOo0fBZnnFDrTvu7n1d58kuU1rDB3rJoQ2hX2TTNYjKng8WUylpHOB7INUjRqfpshqQAWiiyy-1WJ6axP95qgQwLRhGJJ51guztLflduikGmvK3Z3Kj_RqoHRIjt-djPjEPtQ-HzMNd-_hIGGlzO_UHMEUpTa1TwoQOOAi_icL8G060pj_RHCzpkiEFWoRjizaB5BjKLGYrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیشب ۱.۱۵ تریلیون دلار به بازار سهام ایالات متحده اضافه شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127302" target="_blank">📅 09:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127301">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgcePGRlk-cUCH0Arm-_H79uB0v167d_ffrXJv2-60QP8SJRYrhXBeB1pPm9fKHH1lRieKQJzorrxZ9Vhhg5LFYsiyZCcTugSu2e4iW0QNQy6_JxnGF2DpogL4aKAi0Yg40TAopjA9TLFgFxwy2v-RLndDJT6-s-gT5wow6Twuu4dwpakxJdalP1-zd12SNucTo1K31lo37rvIYU0fDxnCRMsLkVC7S41VJd09OGo52gnCOb2M-85-xmavVhaPYHKLw4DIRBULFCjCdmgPcT2c2phuoNpdqfVLzfYV4reJPIC0j_y2cSLh5rxGSj7_eL5yc_-snpjsnCOtv0jLdwbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی:
احتمال فریب از سوی ترامپ بالاست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/127301" target="_blank">📅 09:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127300">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b3ef8e07c.mp4?token=lXQleDmYFhX_rzApDzWq-dKbP0m98R9O4b7UtzX9yWylMdVyRUYOQmotxfAa6HJbugkaBwd8yaioHlWmhD72r74XzZb2Nz5mNEBOdaUDtYxUA8FXYhvEkLG0l_dFVgZSJ2YPR24yMlfRlYpyw7yf6-80bA_YB-fMwvc6zUiHNz-DwpB59Dzxg_EnIdNi6YIDIZvOmtChFCL8Xf7efRknFS_u0gay2izj7tqzxrhNMoG-wnjIWXr-9Mn1ZHy9pQFoxD21zsw7T1lJ4BPCtsmedpXHLq6GayYIu4QQGSShWa_tYNb7UioKpZKNeFwXaEp8Vtwcwl6bBnfMmILF4r_hdTrar_jB27YPDbu6nSTzwNA89YkosWYVus-DFjbONZ-UtgSqFQZEkyQwX1_hOWLTxIjNAMQdRJKDZtzeZvJ6JWpzyordBWf9mBKFSqjGL_JZJRBB3ML3DL4anVtmhQT-0sZQ6bwH0vcyUCzPcsRZMMDAMgk2vXiNY3wdaCAVp_QlK0wDgGMT8Ym8spQBBiZALzqJXzotx24Rzt_TjotWxKd18NeXAGcrmXrORS7h3o7tat24O8m5GRIwV9JoogWrc78uM9VDUNlM1sxNI9ErN26zph-oTeTpGab3SXCq7ViEZAKF0NNVaipcce4bpC6DQyrNiLgZQdaoL8sxV6xz6qY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b3ef8e07c.mp4?token=lXQleDmYFhX_rzApDzWq-dKbP0m98R9O4b7UtzX9yWylMdVyRUYOQmotxfAa6HJbugkaBwd8yaioHlWmhD72r74XzZb2Nz5mNEBOdaUDtYxUA8FXYhvEkLG0l_dFVgZSJ2YPR24yMlfRlYpyw7yf6-80bA_YB-fMwvc6zUiHNz-DwpB59Dzxg_EnIdNi6YIDIZvOmtChFCL8Xf7efRknFS_u0gay2izj7tqzxrhNMoG-wnjIWXr-9Mn1ZHy9pQFoxD21zsw7T1lJ4BPCtsmedpXHLq6GayYIu4QQGSShWa_tYNb7UioKpZKNeFwXaEp8Vtwcwl6bBnfMmILF4r_hdTrar_jB27YPDbu6nSTzwNA89YkosWYVus-DFjbONZ-UtgSqFQZEkyQwX1_hOWLTxIjNAMQdRJKDZtzeZvJ6JWpzyordBWf9mBKFSqjGL_JZJRBB3ML3DL4anVtmhQT-0sZQ6bwH0vcyUCzPcsRZMMDAMgk2vXiNY3wdaCAVp_QlK0wDgGMT8Ym8spQBBiZALzqJXzotx24Rzt_TjotWxKd18NeXAGcrmXrORS7h3o7tat24O8m5GRIwV9JoogWrc78uM9VDUNlM1sxNI9ErN26zph-oTeTpGab3SXCq7ViEZAKF0NNVaipcce4bpC6DQyrNiLgZQdaoL8sxV6xz6qY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا سیما: با صراحت میگویم بخش عمده ای از شروط ده‌گانه در توافق وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127300" target="_blank">📅 09:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127299">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8390c84022.mp4?token=WxOl28tD6OlhAap0xiHV_8aKmUTs3byVBXcZgRdwitZ2Whl0QuC0erVQLVXne04ViUHwExlJ1747GmOGxrMRcjNz3xGE3FtlcPhGm2gV4JIS--Wn95IttmDwU29crYyZmp3m6CuCB9DYKrU1RIKcd7Phw5Rs9tUjiWxRtT37V6Q4UtYuwTyHwwfNbnCEQLBP5WP06bnrHrJxFsFDVeymczj1zbrMCAPtymN6K3BNBXYLYcF-DFW4FR14dxvr8WA-c1XIm5ar45_TR-avfawU4jijyj9P-kOKC5dpznzqJ6LlsMrhZOkJkkU1kKx0o2ZeQ3vDlgF5oIttqivBcCmQ1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8390c84022.mp4?token=WxOl28tD6OlhAap0xiHV_8aKmUTs3byVBXcZgRdwitZ2Whl0QuC0erVQLVXne04ViUHwExlJ1747GmOGxrMRcjNz3xGE3FtlcPhGm2gV4JIS--Wn95IttmDwU29crYyZmp3m6CuCB9DYKrU1RIKcd7Phw5Rs9tUjiWxRtT37V6Q4UtYuwTyHwwfNbnCEQLBP5WP06bnrHrJxFsFDVeymczj1zbrMCAPtymN6K3BNBXYLYcF-DFW4FR14dxvr8WA-c1XIm5ar45_TR-avfawU4jijyj9P-kOKC5dpznzqJ6LlsMrhZOkJkkU1kKx0o2ZeQ3vDlgF5oIttqivBcCmQ1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه CNN با انتشار ویدیویی از اظهارات دونالد ترامپ، نشان داده که او از زمان آغاز جنگ با ایران، دست‌کم ۳۹ بار ادعای «نزدیک شدن به توافق» را مطرح کرده است. این در حالی است که با وجود این تکرارها، هنوز توافق نهایی امضا نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127299" target="_blank">📅 09:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127298">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
نیویورک تایمز: واشنگتن در حال برنامه‌ریزی برای کاهش تعداد هواپیماها و ناوهای جنگی اختصاص‌ یافته به عملیات‌ ناتو در اروپا است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127298" target="_blank">📅 09:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127297">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
حملات هوایی اسرائیل به اطراف شهرک بلاط در شهرستان مرجعیون در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127297" target="_blank">📅 08:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127296">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: اعلام تاریخ برای امضای تفاهم، گمانه‌زنی رسانه‌ای است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127296" target="_blank">📅 08:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127294">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3iqiNz8Ci048iFjtjxS_gHwtLFz0jusnuJDhXb_OwyZKaeX1AgcT2v__ixZjtMKP85M1ZAw7mQBNaohSkaoXjJhTz8J_8MA6ipGklCsz2WTKcZVbvwBithaLS83GxtHu-znTuAimz-TmoZGn2FpUNM9BIkZt7-JKkHDgyD_NhK5v0dnggIET9xyiNtCEZ8EvXdZhVVvWXdWuyRkpJLL2otdwgJ9BBsqFMKdmvXrBvuR0-YZ5mqgQYrguSoUO_4p2M5pfkSN1SAvH0iWK8NntF0OqD4D3cjlBJ15agZA9ayp4oouVW8NsYcm-OnNz42ONfuqb2ZO_u2wy5M5ANXUPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YwE5EG32ACnnYAe0yo2mMyeMp-yC-cvM9dIYqBOREUjM-muLypcbirU31q2xKqwZQ5JjrtKbYrKA5-sNJ3kNnHgdwLWo90avCXIXJzKJgB_SaEuLNNTjTmso3KBMm-uDZFyWC5Y0LR8O9I-TkWEWPsqDSfBwwZi8McueY-AC_GPROMKSWyS0B4JhfDDtNLrgAkUTMZ5V6ctnAkfHvs9nCgLUI7ph6bQyCQvddvNazqkFN-vKh_hRvVcjM9sorSMXo9L8RNuSCL5E4gjgo3fxcjtyrA8JuqUjWM0rx4XWaOs4NPrH5iuub91YD19dwtXLBetdbY7Gr1soV_SLiDOyzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گروه هکری حنظله اعلام کرد که در واکنش به «حملات آمریکا به غیرنظامیان و زیرساخت‌های آبی ایران»، تأسیسات آب ایالت کالیفرنیا را هک کرده است!
🔴
حنظله اعلام کرد که باوجود دسترسی به سامانه‌های مرتبط، از ایجاد اختلال در آب‌رسانی شهرهای آمریکا خودداری کرده و این اقدام تنها «هشداری» به واشنگتن بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127294" target="_blank">📅 08:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127293">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Do4sqEnffpbhLof8dRYVaIiwHfaZa7qIl8DuLRJfz7dJf11UtFL1KdFD4r_J8jf3F05uQ3XGE3yrP_E5ui_JHXgVmQM45mvZslM4jQRKS1EQ8y2YgKAPWZxuZLJtLboGis-YAYgh-XP-ZVhNTrXhzWnx0IO7wMVF7Ig-k96ocK1f6Zlvhpb_1FV_J1Po1m9EMcBYssYbPsOtNmjeMVsByl4dOuwE-lNWv-guDUFLVKBpAs7B0Q-QL7Swd3lTD3tVdSAnPPdyenRX_qWa5J3jzVeAvnLO87My4kSYbbqiT3sDiAsNeFrNFi-Bea_Xx5GZK2iW0V8n6djvlKOm8QohYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایلان ماسک پس از عرضه اولیه سهام اسپیس ایکس، به اولین تریلیونر جهان تبدیل شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127293" target="_blank">📅 08:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127292">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
تلویزیون سوریه: گروهی از نظامیان اسرائیلی به همراه هشت خودرو نظامی وارد روستای صیدا در حومه قنیطره شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127292" target="_blank">📅 08:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127291">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
شبکه فاکس نیوز به نقل از یک مقام ارشد پنتاگون (وزارت جنگ آمریکا) ادعا کرد: در پی تلاش ایران برای هدف قرار دادن کشتی‌های عبوری از تنگه هرمز، نیروهای آمریکایی دو پهپاد ایرانی را سرنگون کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127291" target="_blank">📅 08:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127290">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAx7AOC9EpVz7N4QimGV3ZSJsQeZGoUZ6G6-Y1dpDsXEBlZZWOQsbuxfC2wVZztOgcqVTwiAVGZhrYvHlR5Tki_1tBNdZLUDH2mwLTlEa_mkSmEa6G5l_1RZdddrDl7MVCdZ7G33I-I1_Qfg12QI_Fsc8k_AjZ_VuatJwzyJ6BX4SoLFSaer2x-jp8xoSMucb3eCIPrlu_brfgmJ-356YRkjWW2bU-P2exD3PC7AKH7oEvvSZphzPuNjwzfUPibHgtu6a51t6PeX0JZmdvsdPIq-eRnrxQZo-9qMfHFi14fIy_1__-JaZf9IuGR3wY6hOSJ5V5A6m7exz01yEK5bPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ریچارد ویتز، کارشناس امنیت بین‌الملل در کالج دفاعی ناتو، در گفتگو با الجزیره گفت: توافق احتمالی واشنگتن-تهران احتمالاً به صورت «فازبندی شده» پیش می‌رود؛ فاز اول شامل بازگشایی سریع تنگه هرمز و فازهای بعدی به مسائلی مانند پرونده هسته‌ای اختصاص دارد.
🔴
وی هشدار داد خطر بن‌بست در جزئیات فازهای بعدی وجود دارد که می‌تواند دستاوردهای اولیه را معکوس کند.
🔴
ویتز تأکید کرد بازگشایی تنگه هرمز برای خود ایران (برای صادرات نفت)، متحدان آمریکا در خلیج فارس و اقتصاد جهانی حیاتی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127290" target="_blank">📅 08:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127289">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
اکسیوس، به نقل از یک مقام آمریکایی: ترامپ با گزینه‌ای موافقت کرده است که بر اساس آن ایران سطح اورانیوم غنی‌شده خود را تحت نظارت سازمان ملل کاهش می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127289" target="_blank">📅 08:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127288">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
اکسیوس: این توافق که با میانجیگری مشترک قطر و پاکستان حاصل شده، در صورت امضای نهایی طرفین «توافق اسلام‌آباد» نام خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127288" target="_blank">📅 08:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127287">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
آکسیوس: چهار فروند هواپیمای ترابری نیروی هوایی آمریکا روز پنجشنبه به اروپا اعزام شدند تا تجهیزات لازم برای سفر احتمالی معاون رئیس‌جمهور آمریکا، جی‌دی ونس، به مراسم امضای توافق در ژنو را منتقل کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127287" target="_blank">📅 08:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127286">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ: امروز جنگ با ایران را به پایان رساندیم و آنها موافقت کردند که هرگز سلاح هسته‌ای نداشته باشند، چیزی که ما بر آن تأکید داشتیم. این هدف اصلی بود. این ۹۵٪ از موضوع بود و آنها این کار را به قدرتمندترین شکل ممکن انجام دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/127286" target="_blank">📅 08:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127285">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1487e4114f.mp4?token=DRu5Oxy-0RDn_W3sfndVS3dYM6n7cnwH-N5bBtZ-I3g1QX4ZVhJN0dykPR-vrzO26mSgy5ykprWUjIEeqN5vI71kPQdfzNCsS5GhZL5igfJjI0mocPzzhSwJD_jV-ngftZKTbPYXR6phGjuXHd5V4KZXop4IQjxd0sJucngAPmlBSzt1jyw7AZ6-BLkjT8MynBcsR08lZnDlD7AXgS0OZ77MdtEG3JEbTUcM1GVlA6DKO-XySf58d-A8RcIQl1NaBQz22OVc-7fHOZLyvYrrN55aXyHe-Hr78GBQFxFYzRcKHTPk8x8CLdK97CN_OChwm_mSemHZkhR6M6ms8Mym-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1487e4114f.mp4?token=DRu5Oxy-0RDn_W3sfndVS3dYM6n7cnwH-N5bBtZ-I3g1QX4ZVhJN0dykPR-vrzO26mSgy5ykprWUjIEeqN5vI71kPQdfzNCsS5GhZL5igfJjI0mocPzzhSwJD_jV-ngftZKTbPYXR6phGjuXHd5V4KZXop4IQjxd0sJucngAPmlBSzt1jyw7AZ6-BLkjT8MynBcsR08lZnDlD7AXgS0OZ77MdtEG3JEbTUcM1GVlA6DKO-XySf58d-A8RcIQl1NaBQz22OVc-7fHOZLyvYrrN55aXyHe-Hr78GBQFxFYzRcKHTPk8x8CLdK97CN_OChwm_mSemHZkhR6M6ms8Mym-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما: پخش تصویر انفجار اتمی اشتباه در تدوین بود؛ هک نشده بودیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/127285" target="_blank">📅 08:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127284">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
یک فروند جنگنده اف-۳۵ آمریکایی بر فراز امارات متحده عربی اعلام وضعیت اضطراری کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/alonews/127284" target="_blank">📅 01:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127283">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
پیگیری خبرنگار فارس در بندرعباس از منابع محلی نشان می‌دهد دقایقی قبل نیروهای ایران اجازه عبور یک نفتکش متخلف که بدون هماهنگی وارد محدوده تنگه شده بود را ندادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/alonews/127283" target="_blank">📅 01:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127282">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
صداوسیما: دو انفجار در بندرعباس شنیده شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/alonews/127282" target="_blank">📅 01:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127281">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKgeDm25op9ms1lBnHFYMFwODnc8ouPO_mIwZH27NYcWcdAElh8Jy_WTPXw4DQb-VNB-kEngSFlQdg39sCNjUmR5RLVX0V5UBSPPCakCuuxMtaYwZ2gJOjHQJ3avA899F3S6U3kDNbHNYcNwDQ8CJkyfEVDLtiR1X5LOBjKqxGBnbTYpVHZfIU3EZRMBhmjubuMA-8JXYchJc_Sq_b4hSL9dmyvL9pnEa6ombB6v_r3g5gMosyvZ8OWyUFSio1dZNgw3lkOenUkqXx9eQ9NhCa0bli1hPJ7199JJJbX8OIGb2L4Rcc5YgCECmVvYwdV29V5-eoHrV3344YtMt8vsWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند جنگنده اف-۳۵ آمریکایی بر فراز امارات متحده عربی اعلام وضعیت اضطراری کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/alonews/127281" target="_blank">📅 01:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127280">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
تسنیم: تاکنون هیچ برخورد موشکی یا درگیری در سیریک ثبت نشده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/alonews/127280" target="_blank">📅 01:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127279">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
خبرگزاری معتبر تسنیم :
تا این لحظه، متن تفاهم‌نامه هنوز به تأیید نهایی نهادهای مربوطه تو ایران نرسیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/alonews/127279" target="_blank">📅 01:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127278">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
صداوسیما: برخی منابع آگاه صدای انفجار را مرتبط با مدیریت و بسته نگه داشتن تنگه هرمز می‌دانند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/alonews/127278" target="_blank">📅 01:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127277">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
صدای انفجار در سیریک
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/alonews/127277" target="_blank">📅 00:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127276">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
امواج مدیا به نقل از منبع آگاه سیاسی در تهران:
🔴
متن توافق شامگاه چهارشنبه آماده و نهایی شد
🔴
دوحه با ایران و آمریکا در تماس بوده تا زمینه دستیابی به توافق را فراهم کند
روند اجرای تفاهم در صورت تایید نهایی، آغاز خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/alonews/127276" target="_blank">📅 00:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127275">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
صدای انفجار در سیریک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/alonews/127275" target="_blank">📅 00:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127274">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6mFzkEThsy0lrjJ6_e2CaLf3LsIUw4NQF-4GEIPb7eiCC2sBqduxFLELWl1RoOnTiVgm2iAAn329HD2oVNWgM8FzkhcOQScid2_rm16bP44H3InEbhN3xgImrPQROTz0SzzHHp30wUkzkqaxvuZUohLFibM0rbdkxRe7xhtx_E2vOjMu5oy7LtSeHs9tRxl3QbM2qgvOe9lylSdmy7hldO1eJvLnZKQgoJUR8aI3YEcxcc5OmESfFcuc-qNkB9LYBT_646pBoQ7gj5Uo6y3QTiIdwU4joAdUidXVLgQvjAi55gXF9E0_BTQp-VDcSTkdyxLkaSk0OTxaa5m45fiHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مکزیک فاتح افتتاحیه شد
مکزیک 2 _ آفریقای جنوبی 0
@AloSport</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/alonews/127274" target="_blank">📅 00:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127273">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
اکسیوس، به نقل از یک منبع: نتانیاهو هیچ اطلاع قبلی نداشت و وقتی ترامپ بیانیه اولیه خود را در مورد توافق با ایران منتشر کرد، غافلگیر شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/127273" target="_blank">📅 00:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127272">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VimB8cl-ELGvz57V7sWU2Nb5DZEgZQbv4TPPUQZVVDquHEK2QpWa6g2dVUBEo4Q3fzHZMLEOckP1uzNGFm-XW5up0vorztL94eRRqOcyWbOCldc8mLTsnitr3upKvMQWJaF3-cmVRNU92H_81Em1NRb5cFereg-6cdyr364P73yfENIQ8QWHOFOmGel4kJProwA2jEKlGo09oduEpiYXVL1lz_2Vlj5Z0qbHmaiAyzrHDRGKwqQG4FmlM88c9ThHTUxnNWX-BUd3JYR8zFxanZ_subuRBmCIvDQn7oeXRxING1cHwsUG8jX9-2h0hv2C5CLUm98ruVQQSbxgfpYhHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش چشم دیشب تو شبکه افق گفته بود فکر نکنم توافق بشه و یکی دو هفته جنگ رو داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/alonews/127272" target="_blank">📅 00:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127271">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
خبرنگار: آیا رژیم ایران عوض شده؟
🔴
ترامپ: بله، نه یک بار بلکه دو بار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/127271" target="_blank">📅 00:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127270">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
واشنگتن پست: توافق قطعی شده و بزودی در ژنو یا رم امضا خواهد شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/127270" target="_blank">📅 00:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127269">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
واشنگتن پست: توافق قطعی شده و بزودی در ژنو یا رم امضا خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/alonews/127269" target="_blank">📅 00:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127268">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
العربیه: آمریکا دسترسی به دارایی‌های مسدودشده ایران را تسهیل خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/alonews/127268" target="_blank">📅 00:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127267">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الان یعنی با قاتل  حضرت سید علی خامنه‌ای
💔
، قاتل خانواده‌ی رهبر جدیدمون
💔
قاتل سردار سلیمانی
💔
، قاتل سید مقاومت حسن نصرالله
💔
، قاتل شهید فقید اسماعیل هنیه
💔
، قاتل دانشمندمون محسن فخری‌زاده
💔
، قاتل سردار حسین سلامی
💔
، قاتل سردار محمد باقری غلامعلی رشید
💔
، قاتل سردار…</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/127267" target="_blank">📅 00:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127266">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ :  ما این جنگ رو از نظر نظامی خیلی زود بردیم، تنها چیزی که نبردیم، رسانه‌های فیک‌نیوزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/127266" target="_blank">📅 00:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127265">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
بقایی: تا الان ایران به جمع‌بندی نهایی درباره توافق نرسیده است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/127265" target="_blank">📅 23:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127264">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ : تنگه بازه؛ ولی این تنگه‌ها از چند ماه پیش هم باز بودن، فقط شما خبر نداشتید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/127264" target="_blank">📅 23:57 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
