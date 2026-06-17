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
<img src="https://cdn4.telesco.pe/file/t_JGijPVxfoAic9UHVfeniCbkNjhuumzMhPmE6MZlNq-oMSvyaDOmQ2J12JlMXbCCRGlt4kvg2zVExm-5S5IHuS9bECXYXnP9wYT4cGFMsLpfj36KYMOCiPtontSKq8pmHc78wImwtFMY-JzzfW10gCB4NOm4SUmIEB95Zl9hWiUfU0SX9dJJwo6ehn8iAeN3FJU9zyTJWn05wq57Zb21VJpLFGF87pbS5DglFKgFestckVkC1KfcCkhyoSCNzKvD_a6NOz4eFgWQtvb6mfLIlJPWNiIOMx5L9BHBvRPRjdQDnSnTNWx2qEHnOliQZC2HPSS4x-0hs1l4ewDT9e2wQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 967K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 23:05:04</div>
<hr>

<div class="tg-post" id="msg-128776">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
🔟
ایالات متحده آمریکا متعهد می‌شود بلافاصله با امضای این یادداشت تفاهم و تا زمان خاتمه تحریم‌ها، اسقاطیه‌های وزارت خزانه‌داری را برای صادرات نفت خام ایران، محصولات پتروشیمی و مشتقات آنها، و تمامی خدمات مرتبط شامل تراکنش‌های بانکی، بیمه‌ها، حمل و نقل و غیره صادر کند.
🔴
1️⃣
1️⃣
ایالات متحده آمریکا متعهد می‌شود تا وجوه و دارایی‌های محدود یا مسدود شده جمهوری اسلامی ایران را با اجرای این یادداشت تفاهم به طور کامل برای استفاده در دسترس قرار دهد. ایالات متحده آمریکا و جمهوری اسلامی ایران در مورد روال مربوط به آزادسازی این وجوه در طول مذاکرات، به صورت دوجانبه توافق می‌کنند. این وجوه، چه در حساب اصلی نگهداری شوند و چه منتقل شوند، برای پرداخت به هر ذینفع نهایی که توسط بانک مرکزی جمهوری اسلامی ایران تعیین می‌شود، باید به طور کامل قابل استفاده شوند. ایالات متحده آمریکا متعهد می‌شود که تمامی تاییدیه ها و مجوزهای لازم را در این رابطه صادر کند.
🔴
2️⃣
1️⃣
جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت می‌کنند تا یک سازوکار اجرایی برای نظارت بر اجرای موفق این یادداشت تفاهم و پایبندی آتی به توافق نهایی تشکیل شود.
🔴
3️⃣
1️⃣
پس از امضای این یادداشت تفاهم و منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ این یادداشت تفاهم و تداوم اجرای این اقدامات، جمهوری اسلامی ایران و ایالات متحده آمریکا مذاکرات درخصوص توافق نهایی را منحصرا در مورد بقیه بندها آغاز خواهند کرد.
🔴
4️⃣
1️⃣
توافق نهایی با یک قطعنامه الزام‌آور شورای امنیت سازمان ملل متحد تایید خواهد شد.
(امضاء) از طرف دولت جمهوری اسلامی ایران
تاریخ
(امضاء) از طرف دولت ایالات متحده آمریکا
تاریخ
( امضاء) در حضور میانجی
از طرف دولت جمهوری اسلامی پاکستان
تاریخ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8 · <a href="https://t.me/alonews/128776" target="_blank">📅 23:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128775">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فوری / جمهوری اسلامی ایران و ایالات متحده آمریکا، به طور مشترک و با حسن نیت، در تاریخ ۲۸ خرداد ۱۴۰۵ نسبت به موارد زیر توافق کردند:
🔴
1️⃣
جمهوری اسلامی ایران و ایالات متحده آمریکا و متحدین آنها در جنگ حاضر، با امضای این یادداشت تفاهم خاتمه فوری و دائمی عملیات‌های نظامی را در تمامی جبهه‌ها، از جمله در لبنان، اعلام کرده و تعهد می‌کنند از این پس هیچ جنگ یا هیچ عملیات نظامی علیه یکدیگر آغاز نکنند و از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند و تمامیت ارضی و حاکمیت لبنان را تضمین کنند. توافق نهایی خاتمه دائمی جنگ در تمامی جبهه‌ها، از جمله در لبنان، و بقیه مفاد این بند را تایید خواهد کرد.
🔴
2️⃣
جمهوری اسلامی ایران و ایالات متحده آمریکا متعهد می‌شوند که به حاکمیت و تمامیت ارضی یکدیگر احترام بگذارند و از مداخله در امور داخلی یکدیگر خودداری کنند.
🔴
3️⃣
جمهوری اسلامی ایران و ایالات متحده آمریکا به انجام مذاکرات و حصول به یک توافق نهایی در مدت حداکثر ۶۰ روز، قابل تمدید با رضایت طرفین، متعهد می‌شوند.
🔴
4️⃣
بلافاصله با امضای این یادداشت تفاهم، ایالات متحده آمریکا شروع به رفع محاصره دریایی خود و هرگونه مزاحمت یا ممانعت علیه جمهوری اسلامی ایران می‌کند، و ظرف ۳۰ روز به محاصره دریایی به طور کامل خاتمه خواهد داد. در طول این مدت، تردد کشتی‌ها متناسب با تعداد ترافیک قبل از جنگ که از سوی جمهوری اسلامی ایران برقرار می‌شود، خواهد بود. ایالات متحده آمریکا همچنین متعهد می‌شود تا ظرف ۳۰ روز پس از توافق نهایی، نیروهای نظامی خود را از حوزه پیرامونی جمهوری اسلامی ایران خارج کند.
🔴
5 با امضای این یادداشت تفاهم، جمهوری اسلامی ایران ترتیباتی را با حداکثر تلاش خود برای عبور ایمن کشتی‌های تجاری، بدون هزینه فقط برای ۶۰ روز، از خلیج فارس به دریای عمان و بالعکس، اتخاذ خواهد کرد. تردد کشتی‌های تجاری بلافاصله آغاز، و با توجه به ضرورت رفع موانع فنی و نظامی و مین‌زدایی توسط جمهوری اسلامی ایران، ظرف ۳۰ روز برقرار خواهد شد. جمهوری اسلامی ایران با سلطنت عمان برای تعیین اداره آینده و خدمات دریایی در تنگه هرمز، مطابق با حقوق بین الملل قابل اجرا و حقوق حاکمیتی کشورهای ساحلی تنگه هرمز، گفتگو خواهند کرد و با دیگر کشورهای ساحلی خلیج فارس نیز تبادل نظر می‌کنند.
🔴
6️⃣
ایالات متحده آمریکا متعهد می‌شود، با شرکای منطقه‌ای خود، برای بازسازی و توسعه اقتصادی جمهوری اسلامی ایران یک برنامه قطعی مورد توافق طرفین را با تامین حداقل ۳۰۰ میلیارد دلار ایجاد کند. سازوکار
اجرایی‌سازی این برنامه، به عنوان بخشی از توافق نهایی ظرف ۶۰ روز نهایی خواهد شد. تمامی تائیدیه‌ها، اسقاطیه‌ها و مجوزهای مورد نیاز برای تراکنش‌های مالی مربوطه توسط ایالات متحده آمریکا ارائه خواهد شد.
🔴
7️⃣
ایالات متحده آمریکا متعهد می‌شود به تمامی انواع تحریم‌ها علیه جمهوری اسلامی ایران، از جمله قطعنامه‌های شورای امنیت سازمان ملل متحد، قطعنامه‌های شورای حکام آژانس بین‌المللی انرژی اتمی، و تمامی تحریم‌های یکجانبه آمریکا، اعم از اولیه و ثانویه، برابر یک برنامه زمانی مورد توافق به عنوان بخشی از توافق نهایی، خاتمه دهد. جمهوری اسلامی ایران و ایالات متحده آمریکا به اهمیت اساسی موضوع خاتمه تحریم‌ها که در بالا ذکر شده است اذعان دارند و قصد خود را برای رسیدگی فوری به این موضوعات در مذاکرات، به منظور دستیابی به توافق متقابل در مورد آنها اظهار می‌کنند.
🔴
8️⃣
جمهوری اسلامی ایران مجدداً تایید می‌کند که سلاح هسته‌ای تولید یا ابتیاع نخواهد کرد. جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت کرده‌اند که وضعیت مواد غنی‌شده ذخیره شده را از طریق یک سازوکار مورد توافق طرفین و مطابق با برنامه زمانی مندرج در بند ۷، حداقل به شیوه رقیق‌سازی در محل، تحت نظارت آژانس بین‌المللی انرژی اتمی، حل و فصل کنند. دو طرف همچنین موافقت می‌کنند تا در مورد موضوع غنی‌سازی، و دیگر موضوعات مورد توافق دو طرف مرتبط با نیازهای هسته‌ای جمهوری اسلامی ایران، بر اساس یک چارچوب رضایت‌بخش که در توافق نهایی مورد موافقت قرار خواهد گرفت، بحث کنند. توافق نهایی مفاد این بند را تایید خواهد کرد. جمهوری اسلامی ایران و ایالات متحده آمریکا به اهمیت اساسی موضوعات هسته‌ای ذکرشده در بالا اذعان دارند و قصد خود را برای رسیدگی فوری به این موضوعات در مذاکرات، به منظور دستیابی به توافق متقابل در مورد آنها اظهار می‌کنند.
🔴
9️⃣
جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت می‌کنند که تا زمان توافق نهایی وضعیت موجود را حفظ کنند؛ جمهوری اسلامی ایران وضع موجود را در برنامه هسته‌ای خود حفظ خواهد کرد، و ایالات متحده آمریکا هیچ تحریم‌های جدیدی علیه ایران وضع نخواهد کرد و نیروهای نظامی بیشتری را در منطقه مستقر نخواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/128775" target="_blank">📅 23:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128774">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Or4fwGU4BpkQJ0VdcG2WlopukN2haJHXmIIuHurwmeKgyEAB3HmdO-O1FgtyErqwos6OMPR0BunQ5Bl3JTjy-TBtSZAFRGMxz2qifNI8Wbeqabb3ZJsacYlenZvrbpPV7oM4rwA6QDKLSqEmnA8XQntw4uw2LMRPu7A-COX2Y6TTv4M6hQA5MkMkDOJKI3ymF22VqizQ62EjvbE3okeUCWN3oVzEDJR6517YBDjAtLZRzCbD2bPXs2yOSwxcYMb8VPhLxioDx-IABYktcbqPB9EDKoxe4OuHjLr04SQTR_SJppe9aYY1zypPbBDQ_GAmPcXoDtYWRuoDBq4UzcHb_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدا سیما : انتشار متن تفاهم‌نامه ایران و آمریکا تا دقایقی دیگر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/128774" target="_blank">📅 22:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128773">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تعهد ما این است که در مدت مشخصی، ترافیک دریایی را تنگهٔ هرمز به حالت عادی برگردانیم
🔴
برای تدوین سازوکار مدیریت تنگهٔ هرمز و خدمات دریایی، ایران و عمان همکاری خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/128773" target="_blank">📅 22:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128772">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
وزیر خارجه ایتالیا پس از تماس با عراقچی: توافق ایران و آمریکا گامی مهم برای ثبات منطقه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/128772" target="_blank">📅 22:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128771">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
مدیرعامل سایپا: ما قرار نیست ماشینامونو گرون کنیم بیاید از خودمون بخرید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/128771" target="_blank">📅 22:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128770">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0daa17143.mp4?token=v9xoDVaJXHWtwnqvHL4f4Sz3TMesmQYqOdvqmuzeoNwGZzh-DF1fcOfj1uh4raizgkdcc2ZdmYeIzpDbXCqqMZeUXPY-L8UbkNSOUpnhOwDLmL5nT767vsPFXpqT3a26yS24FcgBiCXuTsfTatU-FRfmve9Xbfsk2S7GSUwqiapOJvgkgQjDH_sNlLmawwxp2rXXWXWwPmKo6SOwwWFi1cbZ9mynYixI7WpD5TULTKxMVJteeR18bT1DlwRfA4ZO_3wKLJKG7xPtIrh2K1YofONAQ4kbzADMnlnvosvXqvlSxecaTCTXroV0gZpuFLGM4F5XfD1VKBSvWwLVuf4KtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0daa17143.mp4?token=v9xoDVaJXHWtwnqvHL4f4Sz3TMesmQYqOdvqmuzeoNwGZzh-DF1fcOfj1uh4raizgkdcc2ZdmYeIzpDbXCqqMZeUXPY-L8UbkNSOUpnhOwDLmL5nT767vsPFXpqT3a26yS24FcgBiCXuTsfTatU-FRfmve9Xbfsk2S7GSUwqiapOJvgkgQjDH_sNlLmawwxp2rXXWXWwPmKo6SOwwWFi1cbZ9mynYixI7WpD5TULTKxMVJteeR18bT1DlwRfA4ZO_3wKLJKG7xPtIrh2K1YofONAQ4kbzADMnlnvosvXqvlSxecaTCTXroV0gZpuFLGM4F5XfD1VKBSvWwLVuf4KtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ با هواپیما به سمت کاخ ورسای رفت، تا مکرون شام بخوره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128770" target="_blank">📅 22:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128769">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KK-_8XTHxi_AFkiy3Mmcl1y9q8Gat4K70UKpI7nAIxGVI7WOquoGs_HruHisf33qMcbfmY8AOv4JPp8MSA0OxZE4WbSojiyYKThcfxULdtHX4R6wsVPgf0uvDA2T-mZkVwDe0iOqG335L_sp9QsUJI_DlXQLJ7gTA9uIJw3RoLlKCcOkFH21svcAOYbs1C4hOBwHwiNcRqPH_t3qEW-dphCBZNAqGYZnqF5Tol0zX14nReC10OyoPmEHoUkuXALasx8yk7ETUx0euUUnQ1-s_CV7OjkWFxqjVCFTFYWaJkdIg4_Z-_hndw2c6cPuGgFha-ouwxv5qImyNewRAinnaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور لیندسی گراهام: به نظر من امضای این تفاهم‌نامه به نفع ایالات متحده خواهد بود، زیرا تنگه هرمز شروع به بازگشایی می‌کند و درگیری‌ها با ایران متوقف می‌شود.
🔴
اینکه آیا آمریکا می‌تواند با ایران بر سر برنامه هسته‌ای و سایر مسائل به توافقی قابل قبول و قابل راستی‌آزمایی برسد یا نه، هنوز مشخص نیست، اما من تلاش برای رسیدن به چنین توافقی را کم‌هزینه می‌بینم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128769" target="_blank">📅 21:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128768">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
وزارت خارجه ایران : ادامه اشغال جنوب لبنان توسط اسرائیل، یادداشت تفاهم را نقض می‌کند و ما اقدامات لازم را انجام خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/128768" target="_blank">📅 21:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128767">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
منبع آگاه به فارس: پیشنهاد امضای الکترونیکی تفاهم‌نامه ایران و آمریکا پیش از سفر به ژنو مطرح شده است
🔴
تا این لحظه جمهوری اسلامی موافقت خود را با این پیشنهاد اعلام نکرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/128767" target="_blank">📅 21:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128766">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
معاون وزارت ارتباطات : با اشاره به تجربه قطع اینترنت در جریان جنگ اخیر کشور به سطحی از بلوغ رسیده که حتی در شرایط بحرانی و التهاب شدید نیز میتواند بدون قطع اینترنت مدیریت شود و دیگر شاهد قطع اینترنت نخواهیم بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128766" target="_blank">📅 21:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128765">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
الجزیره به نقل از مقام کاخ سفید: ایالات متحده متعهد است که بلافاصله پس از امضای یادداشت تفاهم، معافیت‌هایی برای صادرات نفت ایران صادر کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128765" target="_blank">📅 21:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128764">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوری / بقایی: احتمال امضای تفاهمنامه توسط روسای جمهور ایران و آمریکا مطرح است
🔴
برنامه‌های ایران برای نشست ژنو تغییری نکرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/128764" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128763">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
آکسیوس: طبق توافق تأیید شده، ایالات متحده و جمهوری اسلامی ایران بر موارد زیر توافق دارند:
🔴
آتش‌بس فوری و دائمی در تمام صحنه‌ها، از جمله لبنان، با تعهد به عدم انجام اقدامات نظامی یا تهدیدات بیشتر.
🔴
احترام متقابل به حاکمیت و عدم دخالت در امور داخلی.
🔴
مذاکره برای توافق نهایی ظرف ۶۰ روز (قابل تمدید با رضایت متقابل).
🔴
رفع تدریجی محاصره دریایی آمریکا ظرف ۳۰ روز و عقب‌نشینی نیروها از اطراف ایران پس از توافق نهایی.
🔴
بازسازی و حفاظت از مسیرهای حمل‌ونقل تجاری در منطقه خلیج فارس–خلیج عمان، با پاکسازی موانع و مین‌ها.
🔴
مشورت ایران با عمان و کشورهای منطقه درباره حاکمیت آینده و ترتیبات دریایی در تنگه هرمز.
🔴
تدوین طرح مشترک بازسازی اقتصادی برای ایران (حداقل ۳۰۰ میلیارد دلار).
🔴
رفع کامل تمامی تحریم‌ها (سازمان ملل، مرتبط با آژانس بین‌المللی انرژی اتمی، تحریم‌های اولیه و ثانویه آمریکا) طبق جدول زمانی توافق شده.
🔴
ایران تأکید می‌کند که سلاح هسته‌ای توسعه نخواهد داد؛ مسائل مربوط به مواد غنی‌شده و غنی‌سازی تحت نظارت آژانس بین‌المللی انرژی اتمی مدیریت خواهد شد.
🔴
حفظ وضعیت موجود تا توافق نهایی: عدم اعمال تحریم‌های جدید یا تشدید نظامی.
🔴
صدور مجوزهای آمریکا برای صادرات نفت ایران و خدمات مالی مرتبط.
🔴
آزادسازی و دسترسی کامل به دارایی‌های ایران، طبق رویه‌های توافق شده مشترک.
🔴
ایجاد مکانیزمی برای نظارت بر اجرای توافق.
🔴
توافق نهایی در چارچوب مراحل آتش‌بس مذاکره و سپس توسط شورای امنیت سازمان ملل تصویب خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128763" target="_blank">📅 21:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128762">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
یک مقام کاخ سفید: نشست سوئیس برای مرحله بعدی بسیار مهم خواهد بود زیرا سند کنونی نیت‌های طرفین را منعکس می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128762" target="_blank">📅 21:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128761">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
کاخ سفید: توافق نهایی از طریق یک قطعنامه الزام‌آور از سوی شورای امنیت سازمان ملل تصویب خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128761" target="_blank">📅 21:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128760">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری / وزارت امور خارجه : در حال حاضر در حال بررسی ایده امضای یادداشت تفاهم از راه دور توسط روسای جمهور ایران و ایالات متحده هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/128760" target="_blank">📅 20:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128759">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
یک مقام کاخ سفید: به همان اندازه که ایران به مسائل هسته‌ای پایبند باشد، تحریم‌ها علیه آن کاهش خواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/128759" target="_blank">📅 20:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128758">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mm_z8W0f_6N_4YLU9ExbjGAcfM2MR_PVhf4WGMt0jK2qmrYwN18P64d_9RYvlKBYWdzgsy20WJrZVaJmei7SU8CR91GUpCH7sPw6OhjglDHn4yhFrYyz0HBuwN1Qljj6oP_NLG21da4WGJPcuTr1KgvT4QHF7kRSuE_srPfDPxK2b_3wjB7QEQ9CfjZ7x8x4UOFi022FeP3kKxXqrDBrD8l4IP4xly5LH0HdP6dz_GDhj_9Q65C5YDo-7GI_IQworSs3gwjUiXlag80LGi3XjubWgqqdzzFmrW5oDSpO73Ty_CosxzPY3VG89YnwTqvq94Ywyza6rCN47vA5MiPmlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان تجارت دریایی بریتانیا گزارش می‌دهد که یک کشتی در ۱۰۵ مایل دریایی شمال شرق عدن، یمن، امروز زودتر مورد حمله قرار گرفت پس از اینکه دو قایق کوچک حامل افراد مسلح تا فاصله چهار متری نزدیک شدند و آتش گشودند.
🔴
تیم امنیتی کشتی پاسخ آتش داد، که باعث شد مهاجمان حمله را متوقف کرده و از منطقه عقب‌نشینی کنند. خدمه در امان هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/128758" target="_blank">📅 20:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128757">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری / تسنیم :گزارش شده قایق‌های تندرو و کوچک ناشناس، یک کشتی عبوری را در فاصله ۱۰۵ مایل دریایی شمال شرق عدن هدف قرار دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/128757" target="_blank">📅 20:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128756">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f24117a830.mp4?token=fr3s8bXAOeDqMRt6tvctC5BhDNzF4D33DXOIESDOvhhjkPupIy2Rq4wR3BUfu7EIWkhAMwuZ_fu8_cAunDJRBgVyBwyQdhjTKj1oGmoeVobRKPndwCNHM8KmqWYIQq0wctRB2VVWVXqn_8lC4uVatkrM6HJAePQNybo2DrCJpxbuXjNQdMWQ77ZSrJh7lbaLh_cIM4k54TLK1bH6HYn-r-t324Y_dAdgci74fKI60W3loeLHkHXZhC2OTTSDLeXWZ865KNOAlrx4fTvOYqvMTv0u_uLuoZUDgU0rV7E1g0ELgvzWJS8QqH4q4Z5nt16242s-JaxPN2llvvoxKwvC7X-eO85QHkz42kou-fGmtRwuAvCedH4m8LnWX1ql4Jcu7maAKqRpxM9ri2t1aj-tXM8jLp2n30EpaB7PyIf_akYvk5UHIeJ4ES2jXRZwDAwZ_7rlwX14dwJ_kIl9Q4GWoJWW7RtSb5UZuoCQn_tR2J1ZSwdfZBDUyt60SqZdPkJc5G91JiUDSrkr2BFz1Uh1ccIKntPAYo-GUhCK895Ob8d9Dk0zOeG6AITGeR_YAB_69rV5ijMdMb8lisLE50JKDtGdeKEg1HQM88mhonI0b9xZyX87vFJdm0RrmV4xE7TqAsHlKeKfhnsHFt4yRPuO9GhXBN9N6QWiRpuvuIQmfy4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f24117a830.mp4?token=fr3s8bXAOeDqMRt6tvctC5BhDNzF4D33DXOIESDOvhhjkPupIy2Rq4wR3BUfu7EIWkhAMwuZ_fu8_cAunDJRBgVyBwyQdhjTKj1oGmoeVobRKPndwCNHM8KmqWYIQq0wctRB2VVWVXqn_8lC4uVatkrM6HJAePQNybo2DrCJpxbuXjNQdMWQ77ZSrJh7lbaLh_cIM4k54TLK1bH6HYn-r-t324Y_dAdgci74fKI60W3loeLHkHXZhC2OTTSDLeXWZ865KNOAlrx4fTvOYqvMTv0u_uLuoZUDgU0rV7E1g0ELgvzWJS8QqH4q4Z5nt16242s-JaxPN2llvvoxKwvC7X-eO85QHkz42kou-fGmtRwuAvCedH4m8LnWX1ql4Jcu7maAKqRpxM9ri2t1aj-tXM8jLp2n30EpaB7PyIf_akYvk5UHIeJ4ES2jXRZwDAwZ_7rlwX14dwJ_kIl9Q4GWoJWW7RtSb5UZuoCQn_tR2J1ZSwdfZBDUyt60SqZdPkJc5G91JiUDSrkr2BFz1Uh1ccIKntPAYo-GUhCK895Ob8d9Dk0zOeG6AITGeR_YAB_69rV5ijMdMb8lisLE50JKDtGdeKEg1HQM88mhonI0b9xZyX87vFJdm0RrmV4xE7TqAsHlKeKfhnsHFt4yRPuO9GhXBN9N6QWiRpuvuIQmfy4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا بخشی از این موضوع این است که معاون رئیس‌جمهور را می‌فرستید؟ اگر جواب داد، عالی است؛ شما به خاطر فرستادن او نابغه به نظر می‌رسید. و اگر جواب نداد، تقصیر معاون رئیس‌جمهور است.
🔴
ترامپ: این ایده را دوست دارم، حتماً. به این ترتیب، اگر جواب داد، من اعتبارش را می‌گیرم. اگر جواب نداد، تقصیر JD است. بهتر است مراقب باشی، JD. او هواپیمایش را برمی‌گرداند و از اینجا فرار می‌کند.
🔴
بله، این ایده را دوست دارم. فکر می‌کنم ایده خوبی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/128756" target="_blank">📅 20:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128755">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee1220f65.mp4?token=O94S9aOxrsEsbiUAc4tj2xXRUYIxFtlPFVkZn6PRpyXhKkDJ9rqPhn-Nys_MeqOixFI6ISykyFOtmUWgSMBpdC9ZQ2zgqIaYR7E-mwV4xY41LXoba3_7Ns5GF0fpqoSVFnf6ETQ3IyKQptDE9qM_YyZEYiaVtEUVPRhsC2QDl5IfqKlw95EJ1z9PLItjoiyrYn459W89FHcLdTiapuTffh7wNjjMrIe18DHcVnBlwg1Gc2hjfQHtF48uRf_aDTvCWTgoeG0BFk0P8N3msZ_IaZ9P_YeECXOEE-B_ITRYbofMaP5afeI1S8b_fDgQO51GS9Urn49mfJzD_DkI8QS2BirdT7VnHSZh_LYGSZKeefd78snBIe-Q_PmdzW5bdcIXnndxzR-SCRlEHzS04iLTh1sXmP9DOvne0XO-VM8lbkypoiVLCC51hrZ5tpUT4oEdQDdkuPlS-YVXn2Id-cQZYIHke89yELa0LNZnMrdg2aYunF21Ha1TdPv4cbaGvAjbeY_fEtnksJYV0aZJcR8kCwRG2w7Nxxc_FYMvyK5xs6LkWVKbm4ZWq5uxo3fOvY7j6ZxP7e0QLjhUbfrYoM8LWxGweHp9okc63j8gdrgFKAuFUzn0pVfaNtFNvO9T2tLpI77xHhFMvtkJrcNghx5GEqxXrPbgigQy_BBHdIAUUW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee1220f65.mp4?token=O94S9aOxrsEsbiUAc4tj2xXRUYIxFtlPFVkZn6PRpyXhKkDJ9rqPhn-Nys_MeqOixFI6ISykyFOtmUWgSMBpdC9ZQ2zgqIaYR7E-mwV4xY41LXoba3_7Ns5GF0fpqoSVFnf6ETQ3IyKQptDE9qM_YyZEYiaVtEUVPRhsC2QDl5IfqKlw95EJ1z9PLItjoiyrYn459W89FHcLdTiapuTffh7wNjjMrIe18DHcVnBlwg1Gc2hjfQHtF48uRf_aDTvCWTgoeG0BFk0P8N3msZ_IaZ9P_YeECXOEE-B_ITRYbofMaP5afeI1S8b_fDgQO51GS9Urn49mfJzD_DkI8QS2BirdT7VnHSZh_LYGSZKeefd78snBIe-Q_PmdzW5bdcIXnndxzR-SCRlEHzS04iLTh1sXmP9DOvne0XO-VM8lbkypoiVLCC51hrZ5tpUT4oEdQDdkuPlS-YVXn2Id-cQZYIHke89yELa0LNZnMrdg2aYunF21Ha1TdPv4cbaGvAjbeY_fEtnksJYV0aZJcR8kCwRG2w7Nxxc_FYMvyK5xs6LkWVKbm4ZWq5uxo3fOvY7j6ZxP7e0QLjhUbfrYoM8LWxGweHp9okc63j8gdrgFKAuFUzn0pVfaNtFNvO9T2tLpI77xHhFMvtkJrcNghx5GEqxXrPbgigQy_BBHdIAUUW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر دووسی از فاکس: برای مراسم امضای توافق صلح ایران می مانید؟
🔴
ترامپ: شاید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/128755" target="_blank">📅 20:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128754">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ: رئیس جمهور چین به دنبال کمک به حل و فصل اوضاع مربوط به ایران بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/128754" target="_blank">📅 20:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128753">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها باید تعدادی موشک داشته باشند، چون دیگران هم دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/128753" target="_blank">📅 20:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128752">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ترامپ: به محض اینکه ایران اقدامی انجام دهد، تحریم‌ها اعمال خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/128752" target="_blank">📅 20:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128751">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6589ab41.mp4?token=aSpK1nLgXoMLsPJqqeskY9XkccTulMB0q9JFo5Q_82jgYU6gmWFoiI2Y-RKUxhL28xmU4tbF0_XGTdDFRwNHc41nVCMkVxPjATemTpUoFtGVueFW9cBYe9r0bQISRyL7Gj93SOyLEZCyQrpQno3lB9Ja3KWecZ2Td7O9PFrHr--Xc9dJoSY4nDUKJw70xg6OoILZ9Y2hWfAYolOsSAObH5EM3n87irnA23x0MPDwEpzOkYglQxk8oT7QkABIn2CVsNzqJxNn2LiXczEkwqj7Eu2OVXcqB-UCJNyUiT3DZE2VrUvOVsRdA4PeYgi5eC1DPL1_XtO18rXjbBU3PyPz0mRldA9gS45f2MK1_IGZz3ARW3LlAPNpjfDKtBIM8TY4s2FZV9q59aG95H2WnU4dOZK20cgeSvJBvJ58m3Xk7SUZOIDYyWuiMBe-BvotBEbXo63ziqZN3kLX06c0O63b_dM1tTwrKKkETds5QiV9jUinO4sMs3_oqxentyGHNfg7YfbrNvFO-oHB8QY1x3iE0jHiS9qZbEB4NVt55q4OwQcJbUpsjhLuQorftfjG49xdmkXH9UrwH0RoxMojj7AQsFHinGJaNUH5xAk-TroEeptFVEK9eBZW3ilOEGVx919jyuh9u2IdnFZ0oFf3xOMgTVND31qVnt1X1acMCppopxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6589ab41.mp4?token=aSpK1nLgXoMLsPJqqeskY9XkccTulMB0q9JFo5Q_82jgYU6gmWFoiI2Y-RKUxhL28xmU4tbF0_XGTdDFRwNHc41nVCMkVxPjATemTpUoFtGVueFW9cBYe9r0bQISRyL7Gj93SOyLEZCyQrpQno3lB9Ja3KWecZ2Td7O9PFrHr--Xc9dJoSY4nDUKJw70xg6OoILZ9Y2hWfAYolOsSAObH5EM3n87irnA23x0MPDwEpzOkYglQxk8oT7QkABIn2CVsNzqJxNn2LiXczEkwqj7Eu2OVXcqB-UCJNyUiT3DZE2VrUvOVsRdA4PeYgi5eC1DPL1_XtO18rXjbBU3PyPz0mRldA9gS45f2MK1_IGZz3ARW3LlAPNpjfDKtBIM8TY4s2FZV9q59aG95H2WnU4dOZK20cgeSvJBvJ58m3Xk7SUZOIDYyWuiMBe-BvotBEbXo63ziqZN3kLX06c0O63b_dM1tTwrKKkETds5QiV9jUinO4sMs3_oqxentyGHNfg7YfbrNvFO-oHB8QY1x3iE0jHiS9qZbEB4NVt55q4OwQcJbUpsjhLuQorftfjG49xdmkXH9UrwH0RoxMojj7AQsFHinGJaNUH5xAk-TroEeptFVEK9eBZW3ilOEGVx919jyuh9u2IdnFZ0oFf3xOMgTVND31qVnt1X1acMCppopxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره افغانستان: ممکن است تمام تجهیزات را پس بگیرم... افغانستان دارد به ما چاپلوسی می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/128751" target="_blank">📅 20:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128750">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74479be1f.mp4?token=W-6vfFR_Iyr0BzpdJcScMExJfbEEYr_TNRtTvVe-gc3jNfIzmzRB0awJRH4dsOpEYoX51tdfyKcI_XI3L9ByI0_1rwjuuqR4me61phW7UO91rEyXBcJWiKLg1Qxhy8GCP_R8Ywy9wnbyuSQsuoRBPU9zFe_-MUz5v-GjtmYy0KLbo2QX8vcynOqK5St-FbOJEcPL2HtcvIlsO1n6VIpXFpRY4sVPt-_IIA8XNOP58oGXxBiUBTCUxdhRnNiJ7nPDIDHsZEwte5OuoeIWSTf2v-uRt7yKJ1cj-O9fos9vluM713R8azvgqLJ2-fV0YdINEsdbcVtoIM8kp2ahnC6X0QtU33Z9jfCi1qoAEiF2fMeRn1w2EJfWg5-Sc8KdmRmqkwKrx_mNEDudbf0CiCbeXykF2WWaA03a6m9a3dSjfm5Z7uW3sSwpMB1u287GgIbVKuHYOeAc2Yvg_qrQUss6nDpKyQLdrfaoFCx7FpxB2PqeG_Sdo5VixZ3OlK8Ymcv0kO6fYUrBwnb8kdKELrlkIgttlba_Vyk4Kr0tYxrP-NV4VweJtvOaK4rQ5GtliEZ-MvLr2gBB1ehz94cbmCnlW057FIDXxGNP74xO8i1VE1lB93ypetYvFrFmEAE_Y1oyd-KSO-XTgshT5N_cnTTW-1jFhghRZUI_UNMx3Afa7KM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74479be1f.mp4?token=W-6vfFR_Iyr0BzpdJcScMExJfbEEYr_TNRtTvVe-gc3jNfIzmzRB0awJRH4dsOpEYoX51tdfyKcI_XI3L9ByI0_1rwjuuqR4me61phW7UO91rEyXBcJWiKLg1Qxhy8GCP_R8Ywy9wnbyuSQsuoRBPU9zFe_-MUz5v-GjtmYy0KLbo2QX8vcynOqK5St-FbOJEcPL2HtcvIlsO1n6VIpXFpRY4sVPt-_IIA8XNOP58oGXxBiUBTCUxdhRnNiJ7nPDIDHsZEwte5OuoeIWSTf2v-uRt7yKJ1cj-O9fos9vluM713R8azvgqLJ2-fV0YdINEsdbcVtoIM8kp2ahnC6X0QtU33Z9jfCi1qoAEiF2fMeRn1w2EJfWg5-Sc8KdmRmqkwKrx_mNEDudbf0CiCbeXykF2WWaA03a6m9a3dSjfm5Z7uW3sSwpMB1u287GgIbVKuHYOeAc2Yvg_qrQUss6nDpKyQLdrfaoFCx7FpxB2PqeG_Sdo5VixZ3OlK8Ymcv0kO6fYUrBwnb8kdKELrlkIgttlba_Vyk4Kr0tYxrP-NV4VweJtvOaK4rQ5GtliEZ-MvLr2gBB1ehz94cbmCnlW057FIDXxGNP74xO8i1VE1lB93ypetYvFrFmEAE_Y1oyd-KSO-XTgshT5N_cnTTW-1jFhghRZUI_UNMx3Afa7KM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: به آنها می‌گویم: شما احتمالاً سومین ذخایر بزرگ نفت در جهان را دارید، به چه دلیل به سلاح هسته‌ای نیاز دارید؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128750" target="_blank">📅 20:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128749">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ درباره ایران: آیا اجازه می‌دهید ۹۱ میلیون نفر از گرسنگی بمیرند؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/128749" target="_blank">📅 20:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128748">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
گزارشگر:  چرا اکنون برای شما قابل قبول است که آنها بخشی از توان موشکی خود را حفظ کنند؟
🔴
ترامپ: آنها چه چیزی را حفظ می‌کنند؟ آنها اکنون کمتر از سایر کشورها دارند.
🔴
ما احتمالاً ۸۴-۸۵٪ از موشک‌هایشان را از کار انداختیم؛ بقیه زیر زمین هستند؛ حتی نمی‌توانند آنها را بیرون بیاورند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/128748" target="_blank">📅 20:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128747">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0760bad7.mp4?token=ZSzXmGUzXMFJOs-RGpUntrh9ed00kH9CS-MPi0AKJzm8LAD94ZdUwjCGtGkpf8we5c3Lcm04qMD8bfaRlELIXuye_AQNe-S3ijdE4art32z57jvgn8EhXwU_CqiDqrHfAC2MPGcE4s3i2dRYSVxwiMr0eJdwgSN7HHg5BfxND1kGr0gmggAKTy87Bk_QwbD8le7sAItF3G0VJYdqvaXVPjqzHjFbVQa9L_cWL1-SrwJtzMO6Lh4IJBHPDAbn0gCsf2kCykI2EIMA3y9GHEP_VPsCScfmcBosZxo2W_Ry8pafOGW06nT-E6N0mLMtl21vyEULlxzlSjLH-gh8cmWApxbwi0vrzMPVlvvHoO52dvBOLaYoL6RZjhFiPR9p_sl_iaewEteTQ-8Cd-tVP00S1Q3RsssoDRahLOTQRo0YxewAUFsWX7XmTp6SZCK3sLQGwKEG7Xc_c0FOinhzWzqfVGt0oCM2xyMAlu5rFLTsvo-3z5MM0XXzCIjKZkVea9mWixxRox-zm87768OUJ5bVvnJEw0N0Z3FVX25VpcI8Mv0wAT9T95IJEBdi7u7tQDheoTV4bYCDX95WtULE0AQfOXAWmBnu7QeJTYBo5bYQpgJ4zUEC8qFFC9lNADCFhkwwD_xqco7GbKQmobgz9zb5a0m6ReU5czL8i38pOpqvRHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0760bad7.mp4?token=ZSzXmGUzXMFJOs-RGpUntrh9ed00kH9CS-MPi0AKJzm8LAD94ZdUwjCGtGkpf8we5c3Lcm04qMD8bfaRlELIXuye_AQNe-S3ijdE4art32z57jvgn8EhXwU_CqiDqrHfAC2MPGcE4s3i2dRYSVxwiMr0eJdwgSN7HHg5BfxND1kGr0gmggAKTy87Bk_QwbD8le7sAItF3G0VJYdqvaXVPjqzHjFbVQa9L_cWL1-SrwJtzMO6Lh4IJBHPDAbn0gCsf2kCykI2EIMA3y9GHEP_VPsCScfmcBosZxo2W_Ry8pafOGW06nT-E6N0mLMtl21vyEULlxzlSjLH-gh8cmWApxbwi0vrzMPVlvvHoO52dvBOLaYoL6RZjhFiPR9p_sl_iaewEteTQ-8Cd-tVP00S1Q3RsssoDRahLOTQRo0YxewAUFsWX7XmTp6SZCK3sLQGwKEG7Xc_c0FOinhzWzqfVGt0oCM2xyMAlu5rFLTsvo-3z5MM0XXzCIjKZkVea9mWixxRox-zm87768OUJ5bVvnJEw0N0Z3FVX25VpcI8Mv0wAT9T95IJEBdi7u7tQDheoTV4bYCDX95WtULE0AQfOXAWmBnu7QeJTYBo5bYQpgJ4zUEC8qFFC9lNADCFhkwwD_xqco7GbKQmobgz9zb5a0m6ReU5czL8i38pOpqvRHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: اگر آنها پرچم سفید تسلیم را بالا ببرند و بگویند، «سپاس خداوند را، دونالد ترامپ بزرگ‌ترین رئیس‌جمهور تاریخ است؛ ما کاملاً تسلیم می‌شویم؛ کاملاً دست می‌کشیم؛ این جنگ تمام شده است؛ ما شکست خورده‌ایم»، نیویورک تایمز و سی‌ان‌ان و چند رسانه دیگر خواهند گفت، «ایران پیروزی بزرگی کسب کرده است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/128747" target="_blank">📅 20:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128746">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ : ما یه میلیارد دلار بمب روی ایران ریختیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/128746" target="_blank">📅 20:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128745">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ: حادثه مربوط به حمله به مدرسه میناب در ایران هنوز در دست بررسی است و اشتباهات در جنگ اتفاق می‌افتد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/128745" target="_blank">📅 20:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128744">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fca7846a9d.mp4?token=nZN30oqSiFXm0cJIrDoNv4Wj8FL7zPaIErIqLY_TSSSd4q9FAVgts8lS21L1z5VB30wp56B4piJ4kelVy50hpXxIEubuLBx9Leai9-7lOiC9ucK7bAbDhx9FsCtuhPbn4kLOZZgNGOHBz_HEoDP2JdDl5uI_B_3kwEvodKbxF6MQCCjH_XzWmeyywTQYZuVFRxkaaSwQzLZNFZP1oNJ0MEPgVb9OQXZxlHrilefmcdx-V1ClHMP0YHCzWIaUpCpdjf7w6LVMm9Q08wBZxxkB9WN38Qdk99nAEPHw-jhGNxhozrI7XZx5GHNmKrNyZuuFGbH1axYFomNeHuLN6WANcX7mS49psv4WzdZZKKvWxDTXldXdZyDPAXytjRaOiZERFBzrMMQLe8UkbtaqJtM0keGqQVw9_-tPHYwvd8yLgF6iMckm0qYCvbnTXLKEW_ugqx677QheMQfvOsLIqLQO7-2xEMeCgvgaomLokeSa-rAEkEpY5kN5upa8dxxY2VBMkvGFDlUKzK1vm48umC_3_sA_kL3_V2bNrdR5AUvlCp0ZFxOix8nE0kMTp1UdMqxiYrNx-ZljJGzIk-Pq-i9ubDKT8AM4VmaZkcOKBQwvQH09gtaA_Y7aDFrlmiPnnPJ-3UU_uUu4RC0iE7kl12agGqn6JRtO6RmrTwBzc4KZymQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fca7846a9d.mp4?token=nZN30oqSiFXm0cJIrDoNv4Wj8FL7zPaIErIqLY_TSSSd4q9FAVgts8lS21L1z5VB30wp56B4piJ4kelVy50hpXxIEubuLBx9Leai9-7lOiC9ucK7bAbDhx9FsCtuhPbn4kLOZZgNGOHBz_HEoDP2JdDl5uI_B_3kwEvodKbxF6MQCCjH_XzWmeyywTQYZuVFRxkaaSwQzLZNFZP1oNJ0MEPgVb9OQXZxlHrilefmcdx-V1ClHMP0YHCzWIaUpCpdjf7w6LVMm9Q08wBZxxkB9WN38Qdk99nAEPHw-jhGNxhozrI7XZx5GHNmKrNyZuuFGbH1axYFomNeHuLN6WANcX7mS49psv4WzdZZKKvWxDTXldXdZyDPAXytjRaOiZERFBzrMMQLe8UkbtaqJtM0keGqQVw9_-tPHYwvd8yLgF6iMckm0qYCvbnTXLKEW_ugqx677QheMQfvOsLIqLQO7-2xEMeCgvgaomLokeSa-rAEkEpY5kN5upa8dxxY2VBMkvGFDlUKzK1vm48umC_3_sA_kL3_V2bNrdR5AUvlCp0ZFxOix8nE0kMTp1UdMqxiYrNx-ZljJGzIk-Pq-i9ubDKT8AM4VmaZkcOKBQwvQH09gtaA_Y7aDFrlmiPnnPJ-3UU_uUu4RC0iE7kl12agGqn6JRtO6RmrTwBzc4KZymQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر دوسی از فاکس نیوز: مرد خردمندی یک بار در ژانویه ۲۰۲۰ گفت: «ایران هرگز در جنگی پیروز نشده، اما هرگز در مذاکره‌ای شکست نخورده است.»
🔴
پرزيدنت ترامپ: کی این رو گفته؟
🔴
پیتر دوسی از فاکس نیوز: دونالد ترامپ.
🔴
پرزيدنت ترامپ: آها، فکر می‌کردم می‌خواهی همین را بگویی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/128744" target="_blank">📅 20:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128743">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0926f88f33.mp4?token=qpYWq5B0HPaEXderQPsZITyv7mn3cxCSuEWGzQrZ1sCpXLcMjsfqS4D_XLuk_19qrgSx4SUQGSF8Q3yZJFYBkQKqDYNlDELQzXANWdElKHTjBZBGqEqSTjNoQDeclRLNXJPUcuMarwIKTtdRgRr-hfGTnEkw2DBDKCmkD-c91slPvrolCHyqyl42ka501wVhD3LOHBwBtWI1orpqOmTrtZp23IrN2l-l9HzLNyUpIoKfl6dFhJYWOxl1dj-qCUimCnSKnqOaAtmNt9nLjtkLokSNUuUgHmjqodhF-Icp0JwfdwP9Ir7kpa-Tk__7kI-z0btSILM6T58bFcADe7A2ObcdBq1P9Xx2TmqbKAZIRqjeAcial3gSKb5EhUb35QG4Z9FFDn3UDYdoPBZLTSKHXentJtpG2J4-ZylFB9jm4h_X7d8q5GlqzO8RsAhu7h7hac-vQD_7p17tftaNCotbNMToPHR8CE1NM0f5ZkwSC7-f0BlfeZHiWCQ2ufaB7GJeqtVeaE44fDrj29dW3WQvSVactaCeVrG8p5lRhcIkunTUlCFkrg2dessm4tmLoMG3II0u9RTfdzrmrcGkgoHz38-fTwMw0Yt03lH_Ewbq0PEa8elDlJck6B8R2-KFztdhIP7TkaLPsC-gVQ-hVXDJuWylknEuPus015f1sJi2e9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0926f88f33.mp4?token=qpYWq5B0HPaEXderQPsZITyv7mn3cxCSuEWGzQrZ1sCpXLcMjsfqS4D_XLuk_19qrgSx4SUQGSF8Q3yZJFYBkQKqDYNlDELQzXANWdElKHTjBZBGqEqSTjNoQDeclRLNXJPUcuMarwIKTtdRgRr-hfGTnEkw2DBDKCmkD-c91slPvrolCHyqyl42ka501wVhD3LOHBwBtWI1orpqOmTrtZp23IrN2l-l9HzLNyUpIoKfl6dFhJYWOxl1dj-qCUimCnSKnqOaAtmNt9nLjtkLokSNUuUgHmjqodhF-Icp0JwfdwP9Ir7kpa-Tk__7kI-z0btSILM6T58bFcADe7A2ObcdBq1P9Xx2TmqbKAZIRqjeAcial3gSKb5EhUb35QG4Z9FFDn3UDYdoPBZLTSKHXentJtpG2J4-ZylFB9jm4h_X7d8q5GlqzO8RsAhu7h7hac-vQD_7p17tftaNCotbNMToPHR8CE1NM0f5ZkwSC7-f0BlfeZHiWCQ2ufaB7GJeqtVeaE44fDrj29dW3WQvSVactaCeVrG8p5lRhcIkunTUlCFkrg2dessm4tmLoMG3II0u9RTfdzrmrcGkgoHz38-fTwMw0Yt03lH_Ewbq0PEa8elDlJck6B8R2-KFztdhIP7TkaLPsC-gVQ-hVXDJuWylknEuPus015f1sJi2e9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره خنثی بودن متحدان جمهوری اسلامی ایران: می‌خواهم از چین، رئیس‌جمهور شی، تشکر کنم، با او بودم و او خنثی ماند، کاملاً خنثی، و من از آن قدردانی می‌کنم.
🔴
و می‌خواهم از ولادیمیر پوتین تشکر کنم، او بسیار خنثی بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/128743" target="_blank">📅 20:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128742">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ: حمله اخیر اسرائیل به بیروت خشونت‌آمیز و غیرضروری بود
🔴
محاصره دریایی ایران از بمباران مؤثرتر بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/128742" target="_blank">📅 20:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128741">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ: ما کارت‌هایی برای بازی داریم و ایران باید رفتار بهتری داشته باشد. درگیری بین اسرائیل و حزب‌الله باید پایان یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/128741" target="_blank">📅 20:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128740">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوری / ترامپ: اگر ایران درست رفتار کند، می‌تواند در بخش نفت سرمایه‌گذاری کند و ما هیچ پولی به آن پرداخت نخواهیم کرد.
🔴
ایران به صندوق ۳۰۰ میلیارد دلاری دسترسی نخواهد داشت مگر اینکه رفتار مناسبی داشته باشد.
🔴
آمریکا مقدار زیادی از پول ایران را توقیف کرده و در مقطعی مجبور به بازگرداندن آن خواهد شد.
🔴
این توافق به کشتی‌ها اجازه می‌دهد تا از تنگه هرمز عبور و مرور کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/128740" target="_blank">📅 20:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128739">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eea5008dc2.mp4?token=aFgSj_H3YuCaaEm-H2mGkkpWjXSWXwJLs5VFjhxeJsOqnEEOnSUc3aLR1wd7KmlcCdikxwx5nPY4lpVmGiN0_4Cw5qcynru75nhfsmoXpxfz-xc6AL0ABzneIi7YwAAOJ-r2a5g2nRYn_5tLu9SM1IDY1El5zrZzq9GpgOdWw0yTyVvg_9Q1LAyFdsFoKMZtOxSSlDk5ZkXSWApQ8V6yL8DSoodYgRRVMfU_F3TfeIvpurIX-08-MGRggNYfBn9x5jdkWq7vH_DNtpLLoyF4uZZI3I6qSEx0pKTrdFhAXULSB92cJD79xngsFuoR7G6C1FfxOdpP4dJqnG55jAYGkGRCQrmPx0QC9_DM-EHvJG6gMF8bvMIDkG6jQtq-OWc-muXYXYT6Suprt93OWXgo1neblmCxOFZmtzRK-hBc9HvdtAGMEizp9-aCVxip7deUy56Oeq2wizmr_uVUUq49M-3SvntPu2h_YWCjSsp6voz4mpoozpp1NP9ceN6jVpsmGpEspauleKtcL57vcBZsHdZd0XT2BXxwYoMVhXOte9rI_Xl7UP7lnZcedQQYEiHu64BOdsPXdvVmzgv3GfrrlDuKng695o8oOyujRNnSSsvEgawAYMf5PbjZUX5tmHDvSzOLbQbSEs7vLQYNK4iaArYyk2m3r-q7dIcfviFiDf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eea5008dc2.mp4?token=aFgSj_H3YuCaaEm-H2mGkkpWjXSWXwJLs5VFjhxeJsOqnEEOnSUc3aLR1wd7KmlcCdikxwx5nPY4lpVmGiN0_4Cw5qcynru75nhfsmoXpxfz-xc6AL0ABzneIi7YwAAOJ-r2a5g2nRYn_5tLu9SM1IDY1El5zrZzq9GpgOdWw0yTyVvg_9Q1LAyFdsFoKMZtOxSSlDk5ZkXSWApQ8V6yL8DSoodYgRRVMfU_F3TfeIvpurIX-08-MGRggNYfBn9x5jdkWq7vH_DNtpLLoyF4uZZI3I6qSEx0pKTrdFhAXULSB92cJD79xngsFuoR7G6C1FfxOdpP4dJqnG55jAYGkGRCQrmPx0QC9_DM-EHvJG6gMF8bvMIDkG6jQtq-OWc-muXYXYT6Suprt93OWXgo1neblmCxOFZmtzRK-hBc9HvdtAGMEizp9-aCVxip7deUy56Oeq2wizmr_uVUUq49M-3SvntPu2h_YWCjSsp6voz4mpoozpp1NP9ceN6jVpsmGpEspauleKtcL57vcBZsHdZd0XT2BXxwYoMVhXOte9rI_Xl7UP7lnZcedQQYEiHu64BOdsPXdvVmzgv3GfrrlDuKng695o8oOyujRNnSSsvEgawAYMf5PbjZUX5tmHDvSzOLbQbSEs7vLQYNK4iaArYyk2m3r-q7dIcfviFiDf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره محمد بن سلمان:
من چندین بار با ولیعهد عربستان سعودی صحبت کردم — آنها خیلی خوشحال هستند که هنوز... شما هم باید آنها را خوشحال نگه دارید، می‌دانید؟
🔴
ما از فرودگاه‌های آنها استفاده می‌کنیم، نه اینکه اگر نمی‌خواستیم، آنها بتوانند ما را متوقف کنند.
🔴
رفتم آن کوچولو را بگیرم. اما خطا کردم. از خطا کردن متنفرم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/128739" target="_blank">📅 20:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128738">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a52031f13.mp4?token=UEgs2z21Od3fURX8di_OYMXXs2jnWvKLCD_J9x-7SAL63LPrU_mVN125RMETYdDYrEG7DohUIGMK4QtPpOlumYQI4DvhByB3_1pzofjSI4dArE-NUHbkTsEP3AVOKmkiSiqsSj6gUvedZAj3xjRE-9EkeneE7-XcfYsTQDhZoIW8S1slB4u4I8naykNJ-yWKhDnsN8Na5z3PK0F6gXhTRLxSNMeUu7eeLO7UL-CqGuB6ShOjxMmRQKMMUwSH6m8K6YNUL9rBbQrZxanwsJHlhTiwK11VbmF5hCDb0egekuvt8X3svaF1vtMhx_5qRnQn1pYzzfI93AoSfQ4JV_8jVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a52031f13.mp4?token=UEgs2z21Od3fURX8di_OYMXXs2jnWvKLCD_J9x-7SAL63LPrU_mVN125RMETYdDYrEG7DohUIGMK4QtPpOlumYQI4DvhByB3_1pzofjSI4dArE-NUHbkTsEP3AVOKmkiSiqsSj6gUvedZAj3xjRE-9EkeneE7-XcfYsTQDhZoIW8S1slB4u4I8naykNJ-yWKhDnsN8Na5z3PK0F6gXhTRLxSNMeUu7eeLO7UL-CqGuB6ShOjxMmRQKMMUwSH6m8K6YNUL9rBbQrZxanwsJHlhTiwK11VbmF5hCDb0egekuvt8X3svaF1vtMhx_5qRnQn1pYzzfI93AoSfQ4JV_8jVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره مکزیک: مکزیک کنترل کشور خود را از دست داده است. کارتل‌ها مکزیک را اداره می‌کنند؛ این ناراحت‌کننده است.
🔴
رئیس‌جمهور زنی بسیار خوب است، اما زنی بسیار ترسو است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/128738" target="_blank">📅 20:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128737">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de5ef35f0d.mp4?token=EAddveU3WsDCA-ajBBahkbbpdQzcm-5-UAwp4XcyKVXWdUiZVEzAE9N-ON8Mrk0KCZQ535Sa8kbEu9DoD-tW68VqzcuDBkPEs9P-HUz6Y1iqlmiNMn4kXTm7snXdux4ieXF-H5_JXfvRbJI1jI137PDVXpKfm0dxzRctkru08_NmCn_m7-xlN-ejXLgyA4spwbZrekoqVkUWL0g5TONkeZVsmlnyMmoo5X7IZaZ6ZLFgETMHKpv_hM9hFZF371O0DYdkDDqEY6ivnVD9SSwx_HBPp87DUed3touVgcWMJTuMrdVUHVrF9ZgyX9o0LqnjkYVQZHkC61hvlUCIjTbTy6DtQvUcliyF7Yly7lizMvFblqzJgSTj7_0h4TW8SaL02W72YejQ6LONoDDjO46_OKc-u56kbwIaihK5Bs-BQGzRA7XbJBCoATCP-dqjY_29ZzTXA3VH8eZRidBfr8hhZu3gi4z-DsbSzkbG3X9SjN9O2jQUGs4u5MA5uvIO_MIyKBJeQPT3xS0uELIh_20WqWF3sTlU0vKsGFwSD0x3mzW7pQJXTfZ6JFzMpF1FfMh-lpLcD7TM6-WsIfQSE7pfbz1sjnGqK3HCrmK9Vz7A-fuU6V1rEeIGUyOA0-8y9JDoIqnRSuQcutAiuALCBF2adHfY9hvnapWBJ9gWyhsdJ7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de5ef35f0d.mp4?token=EAddveU3WsDCA-ajBBahkbbpdQzcm-5-UAwp4XcyKVXWdUiZVEzAE9N-ON8Mrk0KCZQ535Sa8kbEu9DoD-tW68VqzcuDBkPEs9P-HUz6Y1iqlmiNMn4kXTm7snXdux4ieXF-H5_JXfvRbJI1jI137PDVXpKfm0dxzRctkru08_NmCn_m7-xlN-ejXLgyA4spwbZrekoqVkUWL0g5TONkeZVsmlnyMmoo5X7IZaZ6ZLFgETMHKpv_hM9hFZF371O0DYdkDDqEY6ivnVD9SSwx_HBPp87DUed3touVgcWMJTuMrdVUHVrF9ZgyX9o0LqnjkYVQZHkC61hvlUCIjTbTy6DtQvUcliyF7Yly7lizMvFblqzJgSTj7_0h4TW8SaL02W72YejQ6LONoDDjO46_OKc-u56kbwIaihK5Bs-BQGzRA7XbJBCoATCP-dqjY_29ZzTXA3VH8eZRidBfr8hhZu3gi4z-DsbSzkbG3X9SjN9O2jQUGs4u5MA5uvIO_MIyKBJeQPT3xS0uELIh_20WqWF3sTlU0vKsGFwSD0x3mzW7pQJXTfZ6JFzMpF1FfMh-lpLcD7TM6-WsIfQSE7pfbz1sjnGqK3HCrmK9Vz7A-fuU6V1rEeIGUyOA0-8y9JDoIqnRSuQcutAiuALCBF2adHfY9hvnapWBJ9gWyhsdJ7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره روسیه-اوکراین: هر دو تعداد زیادی سرباز از دست می‌دهند، روسیه بیشتر از دست می‌دهد، چون آن‌ها تهاجمی هستند و وقتی در جنگ تهاجمی هستید، بیشتر از دست می‌دهید، خیلی ساده است.
🔴
من فکر می‌کنم هر دو (زلنسکی و پوتین) می‌خواهند کاری انجام دهند، فقط نمی‌دانند چگونه آن را انجام دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/128737" target="_blank">📅 20:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128736">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ترامپ: اروپا با مشکلات زیادی روبرو است؛ در حوزه‌های انرژی و مهاجرت وضعیت خوبی ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/128736" target="_blank">📅 20:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128735">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ: به نتانیاهو گفتم که از طریق این توافق، چیزی را که بیش از همه می‌خواست، برایش محقق کردم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/128735" target="_blank">📅 20:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128734">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ترامپ درباره سوریه: من مسئولیت زیادی در قبال آقایی در سوریه داشتم که اکنون رئیس‌جمهور آنجاست؛ او کار فوق‌العاده‌ای انجام داده است. او این کشور را در یک سال و نیم جمع و جور کرده، تقریباً مثل کشور ما، یک سال و نیم، اندازه‌ای تقریباً مشابه.
🔴
آنها گفتند، «لطفاً آنها را آنجا نگذار؛ او مردی بسیار خشن است، القاعده.»
🔴
من گفتم، «خب، من یک چیز می‌دانم، یک پیشاهنگ کارساز نخواهد بود.»
🔴
و او در واقع کار بسیار خوبی انجام داده است؛ او دوست دارد وارد شود. می‌دانید، حزب‌الله دشمن اوست، و او وارد می‌شود، اما هر بار که می‌شنود کسی هست، ساختمان‌ها را خراب نمی‌کند — فقط با دقت می‌رود و او را می‌گیرد، اما نمی‌دانم مردم این را می‌خواهند یا نه.
🔴
شاید نخواهند، شاید لبنان نخواهد — ما باید کمی توسط لبنان هدایت شویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/128734" target="_blank">📅 20:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128733">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19e4e6a48.mp4?token=G8a-TnONC1t1SXCMuRLDedeiSlFBXWKTW-8Se5MWxlMPU6uQSS2H2_YrM-Stq7T2SoUino6EWAbK_Kyah6oqoqAih42CjL_XrATcHR025jX-u29Om_ysaCaPNqPn7WQ8YTfT8WwEPJgel5e0Cty-ZqxfrkqYOwla9_EpNgVTUDBU9Tt626dPlidaIKt0HIIh2j0w-uaw2NdzAwB25pvvkw2fnDFR7EO_b9cP4tEw9KAuGsuR-KM3ja4ToT-UA26vK7k09ojxqUcm9LMX5K9sxkS5JsbqiWjMZyiiqoHmP0mHncPCpaPjXBYdEqwE8EkcQj97sndZHb5bjHOJF8B95I2W7qcx8VBv-b74cNrhO8G7otKuW56pZO-OJeMPeL5xGZ1HYX15Z8iv9HM3HpeviojIqr-k8MkxQBkjveoy8YnPduAdv9LOV-J7oXiM7uNXXnybdBJtnOOCSRI5EnkMQeQIkxF9mXPdPJNdwSA2OXcqQp6sR4RHBiLBBhWbcJWsyw5b3GGcrt4SRuaonLp1wijIx-sQXFK3QBpN98Vu48BExtcxjLVjza1QAvTBRTShiIZMwVwyNqRc5yYpPRPRhcYs6NyQkSdugrGPM44inDbC0g_9ihfSpEdMpgB0fRgjY_uyByafd-MNeSQ-YRCrhTsslGX-qR_Cx_UsFjziSAI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19e4e6a48.mp4?token=G8a-TnONC1t1SXCMuRLDedeiSlFBXWKTW-8Se5MWxlMPU6uQSS2H2_YrM-Stq7T2SoUino6EWAbK_Kyah6oqoqAih42CjL_XrATcHR025jX-u29Om_ysaCaPNqPn7WQ8YTfT8WwEPJgel5e0Cty-ZqxfrkqYOwla9_EpNgVTUDBU9Tt626dPlidaIKt0HIIh2j0w-uaw2NdzAwB25pvvkw2fnDFR7EO_b9cP4tEw9KAuGsuR-KM3ja4ToT-UA26vK7k09ojxqUcm9LMX5K9sxkS5JsbqiWjMZyiiqoHmP0mHncPCpaPjXBYdEqwE8EkcQj97sndZHb5bjHOJF8B95I2W7qcx8VBv-b74cNrhO8G7otKuW56pZO-OJeMPeL5xGZ1HYX15Z8iv9HM3HpeviojIqr-k8MkxQBkjveoy8YnPduAdv9LOV-J7oXiM7uNXXnybdBJtnOOCSRI5EnkMQeQIkxF9mXPdPJNdwSA2OXcqQp6sR4RHBiLBBhWbcJWsyw5b3GGcrt4SRuaonLp1wijIx-sQXFK3QBpN98Vu48BExtcxjLVjza1QAvTBRTShiIZMwVwyNqRc5yYpPRPRhcYs6NyQkSdugrGPM44inDbC0g_9ihfSpEdMpgB0fRgjY_uyByafd-MNeSQ-YRCrhTsslGX-qR_Cx_UsFjziSAI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره حماس: وقتی به دنیا آمدند، با یک تفنگ ماشینی در دستشان بیرون آمدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/128733" target="_blank">📅 20:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128732">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ: امیدوارم توافق‌نامه ابراهیم را گسترش دهم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/128732" target="_blank">📅 20:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128731">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ: ایران حزب‌الله را دارد و این مسئله باید به نحوی حل شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/128731" target="_blank">📅 20:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128730">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/397b3f7778.mp4?token=lXuaT_IG94_q-1tutiKC7cYtxEpDxtc20odiDKsNEmEDy44za8t1rL6L7-RMQpuzr7Xk1RzzXXCYkkOr6fy_Irok4Z0ypHeQOHVNAKWuSnE3VDEnGzxDLjbKMbPMWI1UEUS6Jy6lfRggzUszsG1kcGhj9CaNfe5FJpyz2ouoVE6iBhQQuKWXzXf40GUVQ2YVUwYBZbNkFGwKI1cAZa7anly7epHrToD9V1lynpJPto5d-n-jaEIP4pcaOSQu9QEalhN8beco071RkwvKgTHldjQv--v4DJm6CkO57gQTXeXemu67dNff8twythdc3D6ZGxqOf4HdKZLumI7IWWEw4AsF4PJdzvBkTD-gyjLbP8zlUK-KE145796550QMK4jsPHNiY1POPGfbtDI3usTJyAIg_V9MpYQ3PgvMeLVi2k9FCMhHThbxVj2PPgOoBeXnhPmHF507ajG3oW1FmJvL59DCJq8pG8yGt4sSFUpkpJSKZqCAkaqQnomSktBhhdkac_sYraYO5x9scMdB_ztg8Fiwp6BJIiuBqhB6VsUzv849n_WcOq-35_KHQkOqFQY-EMwcGToBSzdt4Lj2c079DA4IBTU2d5RLdPzCicIYg1bN95ujxvvyFsRC2fNWTNdS346U3PeSLgFkS4YuxcLhaS90VMUic9c7POErAIwmgfU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/397b3f7778.mp4?token=lXuaT_IG94_q-1tutiKC7cYtxEpDxtc20odiDKsNEmEDy44za8t1rL6L7-RMQpuzr7Xk1RzzXXCYkkOr6fy_Irok4Z0ypHeQOHVNAKWuSnE3VDEnGzxDLjbKMbPMWI1UEUS6Jy6lfRggzUszsG1kcGhj9CaNfe5FJpyz2ouoVE6iBhQQuKWXzXf40GUVQ2YVUwYBZbNkFGwKI1cAZa7anly7epHrToD9V1lynpJPto5d-n-jaEIP4pcaOSQu9QEalhN8beco071RkwvKgTHldjQv--v4DJm6CkO57gQTXeXemu67dNff8twythdc3D6ZGxqOf4HdKZLumI7IWWEw4AsF4PJdzvBkTD-gyjLbP8zlUK-KE145796550QMK4jsPHNiY1POPGfbtDI3usTJyAIg_V9MpYQ3PgvMeLVi2k9FCMhHThbxVj2PPgOoBeXnhPmHF507ajG3oW1FmJvL59DCJq8pG8yGt4sSFUpkpJSKZqCAkaqQnomSktBhhdkac_sYraYO5x9scMdB_ztg8Fiwp6BJIiuBqhB6VsUzv849n_WcOq-35_KHQkOqFQY-EMwcGToBSzdt4Lj2c079DA4IBTU2d5RLdPzCicIYg1bN95ujxvvyFsRC2fNWTNdS346U3PeSLgFkS4YuxcLhaS90VMUic9c7POErAIwmgfU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: مردم می‌خواهند من پل‌ها را بمباران کنم.
🔴
من قبلاً این کار را کردم، چون می‌دانید، آنها به یکی از وعده‌هایشان عمل نکردند و من بزرگ‌ترین پل آنها را بمباران کردم، معادل پل جورج واشنگتن در ایران.
🔴
اما ما آن پل را بمباران کردیم، شما دیدید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/128730" target="_blank">📅 20:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128729">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17a88534a.mp4?token=c971YnBoqJ8HkfNCEpmsDbEwT1jhA54cdbUj7f0ECMWbHZxu9rK6vUcZiZmhqzsZl_xfvpAQI5HEIyXL8Gw0L7kbUbFed9SOz6viXp5jYuBeB_M9PfWQdFMmdaLNPVSdoBvqzX50WYDbc55MMAmNjWhD9XjR_X6j7xl9f71u6AGm59gRMTpcPqI6h7dB4n1EVxwGfuK37WnLcWoRckF9VU99iNWQNGr_hVYyIzzyit3bHhcpIXa3cE1mdSLqOHNuu7tLvje0kTNmAi6v1Oh_L48ofJ79QFjv7JIFmykxfo3l6PtC4pkdtwHPdavBDO_6VyTM9hr66hf0-dwZnu958TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17a88534a.mp4?token=c971YnBoqJ8HkfNCEpmsDbEwT1jhA54cdbUj7f0ECMWbHZxu9rK6vUcZiZmhqzsZl_xfvpAQI5HEIyXL8Gw0L7kbUbFed9SOz6viXp5jYuBeB_M9PfWQdFMmdaLNPVSdoBvqzX50WYDbc55MMAmNjWhD9XjR_X6j7xl9f71u6AGm59gRMTpcPqI6h7dB4n1EVxwGfuK37WnLcWoRckF9VU99iNWQNGr_hVYyIzzyit3bHhcpIXa3cE1mdSLqOHNuu7tLvje0kTNmAi6v1Oh_L48ofJ79QFjv7JIFmykxfo3l6PtC4pkdtwHPdavBDO_6VyTM9hr66hf0-dwZnu958TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره توافق ایران: توافق اوباما راهی به سوی سلاح هسته‌ای بود.
🔴
توافق ترامپ دیواری برای سلاح هسته‌ای است که سلاح هسته‌ای نمی‌تواند از آن عبور کند. هیچ‌کس نمی‌تواند از آن عبور کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/128729" target="_blank">📅 20:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128728">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1993599568.mp4?token=RKym9jqS9cGHv4zmc92menSMsRLh5B3hlUxisaA90LL7KJk8WJFbGGJDQtmzoSPz7-843hCj_yEL9o8R8Q9epHgcOGanrlUxt89lvaBE0rD-VI4wjhGHA1mx5gdpQff4otTpUtIozDCk5RjNZM9FIeFQv_nABAl1-VKNQQ2j87OhDk43f4wM7L24RMBemhuI7M7CRk5K2OWnKFy2YtU37JT9y1Q-c1iNQD2Qw3xizbzuQzvDBVQYCviNAQZ_Ysuz1Xk52qdp8H2qW-Q7OBGGKb6h_6upfeVnyzco9SbB8mNUoVfOJ0c0HOb0lmLRESoGd5dbEu7MrB1rdJldwdLtiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1993599568.mp4?token=RKym9jqS9cGHv4zmc92menSMsRLh5B3hlUxisaA90LL7KJk8WJFbGGJDQtmzoSPz7-843hCj_yEL9o8R8Q9epHgcOGanrlUxt89lvaBE0rD-VI4wjhGHA1mx5gdpQff4otTpUtIozDCk5RjNZM9FIeFQv_nABAl1-VKNQQ2j87OhDk43f4wM7L24RMBemhuI7M7CRk5K2OWnKFy2YtU37JT9y1Q-c1iNQD2Qw3xizbzuQzvDBVQYCviNAQZ_Ysuz1Xk52qdp8H2qW-Q7OBGGKb6h_6upfeVnyzco9SbB8mNUoVfOJ0c0HOb0lmLRESoGd5dbEu7MrB1rdJldwdLtiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره محمد بن زاید امارات:
محمد در امارات یک جنگجوی شگفت‌انگیز است. هفته گذشته بمب می‌انداخت، من گفتم، «چه کسی لعنتی این همه بمب می‌اندازد»، آن امارات بود.
🔴
او یک مبارز خوب است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/128728" target="_blank">📅 20:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128727">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ترامپ: خب، آنها به سرمایه‌گذاری نیاز دارند، چون ما حدود یک و نیم تریلیون، شاید دو تریلیون دلار خسارت وارد کردیم.
🔴
پس کسی باید به آنها کمک کند — خب، هیچ تضمینی برای کمک به آنها وجود ندارد، و ممکن است همسایگانشان کمی به آنها کمک کنند، نمی‌دانم، اما این مقدار زیادی پول است.
🔴
تقریباً هیچ‌کس چنین پولی ندارد — این همان نوع خسارتی است که وارد شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/128727" target="_blank">📅 20:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128726">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ: اگر ایران به توافق پایبند نباشد، احتمالاً بمباران آن را از سر می‌گیریم تا زمانی که به آن پایبند بماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/128726" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128725">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ: از شرکایمان در پاکستان و قطر تشکر می‌کنم؛ آنها تلاش‌های فوق‌العاده‌ای انجام داده‌اند
🔴
امیدوارم این توافق صلح آغاز یک توافق گسترده‌تر باشد که خاورمیانه را نیز شامل شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/128725" target="_blank">📅 20:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128724">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128e52341e.mp4?token=iaVn5k7ZcaX3dmx3Ealb6RYClpcw7g41HSDRM1wIkwo3a-hiEYyW_XL67YbePh51GXnFWEeugeW1uQnGVGfevWGqfl2qBOsyJeKWFgb9VX0Dd0kAMiRVy0J6AH2oWT6bhvQrbT8FkYsu_CE11LTq0-0WB_YOhNcTB46THB_VpY83WloSjRLBlysnopkORdhC201E5M_VGbZPB-G_PEgYeb9xgmwtPyl2rd9GeKTiN7Cl-E6z6nZvqmwzp-NJAWhkCiPc36bJBdzlweqbnDCNhutv1wtsLABC6z9vakVzG8La7Ob4OCXfu2jVF3Ccgn3v5zKqHSiFXVsjTSSf4uUILIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128e52341e.mp4?token=iaVn5k7ZcaX3dmx3Ealb6RYClpcw7g41HSDRM1wIkwo3a-hiEYyW_XL67YbePh51GXnFWEeugeW1uQnGVGfevWGqfl2qBOsyJeKWFgb9VX0Dd0kAMiRVy0J6AH2oWT6bhvQrbT8FkYsu_CE11LTq0-0WB_YOhNcTB46THB_VpY83WloSjRLBlysnopkORdhC201E5M_VGbZPB-G_PEgYeb9xgmwtPyl2rd9GeKTiN7Cl-E6z6nZvqmwzp-NJAWhkCiPc36bJBdzlweqbnDCNhutv1wtsLABC6z9vakVzG8La7Ob4OCXfu2jVF3Ccgn3v5zKqHSiFXVsjTSSf4uUILIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: آنها از یک نظر فرهنگی ابتدایی دارند، اما این فرهنگ ابتدایی نابغه است، آنها مردم بسیار باهوش و مذاکره‌کنندگان بسیار خوبی هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/128724" target="_blank">📅 20:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128723">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ: ما موظف نیستیم چیزی به ایران بدهیم، اما ممکن است برخی بخواهند آنجا سرمایه‌گذاری کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/128723" target="_blank">📅 20:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128722">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ: جلوگیری از دستیابی ایران به سلاح هسته‌ای، در کنار باز کردن تنگه هرمز، مهمترین نکته برای من است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/128722" target="_blank">📅 20:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128721">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ: این دستاورد بدون فشار فوق‌العاده‌ای که ما طی یک سال و نیم گذشته بر ایران اعمال کرده‌ایم، امکان‌پذیر نبود
🔴
ما با کشورهای خلیج فارس برای رسیدگی به مسائل غیرهسته‌ای مانند موشک‌های بالستیک همکاری خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/128721" target="_blank">📅 19:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128720">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84cd4ae6c5.mp4?token=Yf1YXkPapGxVPXOQjndRpJJcIffAPXLBnHtyXUZjmCj-egQi5bTt8KFzXdwmd-X7PYM7yf5N7KHwqEMupCEGBD2je8Ribav_A_bnjzbkNeoSxXaNYYrPLCHRQU9XHg3Ap3vNBOx0VtAlFvfxxdh0PH_DbHcJiW0sMK2Za-ysi2j9-d815Vdfgrg-hPsrv8vQ2NdNwcla_HCT60p4jkozKTaw8fFzelNzCCeMPuRZRi8lOPWhHgX1AZ9jfOrAbo2FaXjxtPZai2XZfVGJK5q1xeiko1eQFLqh3Pjru51dCd6-_GGhlvm0QqFJ1zcW0tLTri9s9WdVxwwFOrrHTdKe-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84cd4ae6c5.mp4?token=Yf1YXkPapGxVPXOQjndRpJJcIffAPXLBnHtyXUZjmCj-egQi5bTt8KFzXdwmd-X7PYM7yf5N7KHwqEMupCEGBD2je8Ribav_A_bnjzbkNeoSxXaNYYrPLCHRQU9XHg3Ap3vNBOx0VtAlFvfxxdh0PH_DbHcJiW0sMK2Za-ysi2j9-d815Vdfgrg-hPsrv8vQ2NdNwcla_HCT60p4jkozKTaw8fFzelNzCCeMPuRZRi8lOPWhHgX1AZ9jfOrAbo2FaXjxtPZai2XZfVGJK5q1xeiko1eQFLqh3Pjru51dCd6-_GGhlvm0QqFJ1zcW0tLTri9s9WdVxwwFOrrHTdKe-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / ترامپ: ما یک نسخه از توافق ایران را به اسرائیل ارسال کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/128720" target="_blank">📅 19:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128719">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66a1ea2a6a.mp4?token=r_BpRUb-bRzYvQ5J5-aSe15WE7M5CyFOJhBYpbdQvyFbtAVCGLTNU2H9Bjl7LUjWqBCdPz47wnFc4nBj-iYDYj8oS6fMJmoUlp4IezkUdVFZ--Xa8yLTxwou--50azuqKXW9o9SeYXM9brzKuQ3vCLA-R5yd1Exej8mS5VN_jeQya7N5GtQSy01XTgyO55qSrPEZ7O80K2zMfQePJA5aEAGzlwByISsn29llTlJzqbPwL66WN7Xh4Sbj7biW9E2QSwEAWEDu2BFXNclX6eOUPfNOK5Z9txGb6hxcprdUJsXLUaxiPMp6IkyVcWN5Yr0-0bqkl3yN7E_D__za2oXTmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66a1ea2a6a.mp4?token=r_BpRUb-bRzYvQ5J5-aSe15WE7M5CyFOJhBYpbdQvyFbtAVCGLTNU2H9Bjl7LUjWqBCdPz47wnFc4nBj-iYDYj8oS6fMJmoUlp4IezkUdVFZ--Xa8yLTxwou--50azuqKXW9o9SeYXM9brzKuQ3vCLA-R5yd1Exej8mS5VN_jeQya7N5GtQSy01XTgyO55qSrPEZ7O80K2zMfQePJA5aEAGzlwByISsn29llTlJzqbPwL66WN7Xh4Sbj7biW9E2QSwEAWEDu2BFXNclX6eOUPfNOK5Z9txGb6hxcprdUJsXLUaxiPMp6IkyVcWN5Yr0-0bqkl3yN7E_D__za2oXTmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره نتانیاهو و اسرائیل:
ما شریک بزرگ هستیم و او شریک بسیار کوچک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/128719" target="_blank">📅 19:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128718">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ درباره نتانیاهو: نتانیاهو به کشور آمد و از باراک حسین اوباما، رئیس‌جمهور، التماس کرد که برجام را انجام ندهد.
🔴
او گفت این می‌تواند پایان اسرائیل باشد، و اگر من نبودم، همینطور می‌شد.
🔴
و اوباما به او گوش نداد.
🔴
بیبی واقعاً به کنگره رفت و از آنها التماس کرد، اما به جایی نرسید. و آنها این توافق وحشتناک را داشتند که برای اسرائیل فاجعه‌بار بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/128718" target="_blank">📅 19:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128717">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ: هیچ پولی در ایران سرمایه‌گذاری نخواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/128717" target="_blank">📅 19:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128716">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ترامپ: ایران با ما همکاری می‌کند تا اورانیوم دفن شده در اعماق زمین را تحویل دهد و زمان در این موضوع نقشی ندارد.
🔴
فکر می‌کنم اسرائیلی‌ها می‌توانستند در مورد حزب‌الله بهتر عمل کنند
🔴
نمی‌گویم اسرائیلی‌ها نباید از خودشان دفاع کنند، اما نیازی به تخریب ساختمان‌ها در بیروت نیست
🔴
از بابت لبنان خیلی متاسفم
🔴
مذاکرات فنی در مورد ذخایر هسته‌ای ایران فوراً آغاز خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/128716" target="_blank">📅 19:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128715">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
فوری / ترامپ: توافق با ایران فردا یا پس‌فردا امضا خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/128715" target="_blank">📅 19:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128714">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ درباره ترور سردار سلیمانی :
این یک همکاری مشترک بود، همانطور که در کسب‌وکار املاک و مستغلات می‌گوییم. این یک همکاری مشترک بین اسرائیل و ما بود.
🔴
ما یک ماه آن را بررسی کردیم. تقریباً یک ماه قبل می‌دانستیم که او در کدام هواپیما خواهد بود.
🔴
او فقط با خطوط هوایی تجاری، آن‌های بزرگ و پرجمعیت سفر می‌کرد، چون می‌دانست که ما او را سرنگون نخواهیم کرد. آن‌ها بسیار باهوش هستند.
🔴
اما ما می‌دانستیم که او در آن هواپیما خواهد بود، او را دنبال کردیم و سپس اسرائیل به من اطلاع داد که آن‌ها این کار را انجام نخواهند داد. و من باید تصمیم می‌گرفتم.
🔴
و به ژنرال گفتم، «خب، اگر اسرائیل این کار را نمی‌کند، ما همه آماده‌ایم. آیا انجامش می‌دهیم؟ آیا دوست داری انجامش دهی یا نه؟» گفتم، «البته، اگر می‌خواهی انجامش دهی، ما می‌توانیم انجامش دهیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/128714" target="_blank">📅 19:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128713">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ترامپ : نتانیاهو گاهی اوقات کمی از کوره در می‌رود، اما من با او همکاری بسیار خوبی دارم
🔴
ما به احتمال زیاد توافق را امضا خواهیم کرد و ایران خواهان آن است؛ آنها به طور مناسب عمل کرده و موافقت کرده اند که سلاح هسته ای تولید نکنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/128713" target="_blank">📅 19:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128712">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ترامپ: من نمی‌خواستم "هربرت هوور بزرگ" فقید (سی و یکمین رئیس‌جمهور ایالات متحده آمریکا) باشم.
🔴
من آن را نمی‌خواستم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/128712" target="_blank">📅 19:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128711">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ترامپ: ما در مورد لبنان کمی با نتانیاهو اختلاف نظر داریم، و او می‌توانست تحمل بیشتری داشته باشد و هر بار که یکی از اعضای حزب‌الله وارد ساختمانی می‌شود، آن را تخریب نکند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/128711" target="_blank">📅 19:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128710">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a0d76d44.mp4?token=MjdV1mjRGBv2nn3H0JFc-gBVFr4quyqxBV1JQWffAL_0wgefhbbgRVWzODeVgjnIWSuLpCMkZknxiQNSMCuk4lLEKD2q4qWLQxqkzU2fVML96xk5-1RJDsf3emzTsnw_KJ4MGxnhOzJ7o6EDohdlFVTL0I1ZsU31yYy_I92ldaHf6A1G9aXG1R4ttoxojqRunJ5PEFy8OIWT11TE4_UHinCvRSg0gLm81HbtogsH9FwYFdWQMe92mkmfi5nvCNZlkN5RrdAhXwu0FXrh42RzyhSDca5SiabY2MMBznrSJd6at0TL-3OpZCCd7cQw9veHlVFuhzCyFFO2JGUIzLFGfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a0d76d44.mp4?token=MjdV1mjRGBv2nn3H0JFc-gBVFr4quyqxBV1JQWffAL_0wgefhbbgRVWzODeVgjnIWSuLpCMkZknxiQNSMCuk4lLEKD2q4qWLQxqkzU2fVML96xk5-1RJDsf3emzTsnw_KJ4MGxnhOzJ7o6EDohdlFVTL0I1ZsU31yYy_I92ldaHf6A1G9aXG1R4ttoxojqRunJ5PEFy8OIWT11TE4_UHinCvRSg0gLm81HbtogsH9FwYFdWQMe92mkmfi5nvCNZlkN5RrdAhXwu0FXrh42RzyhSDca5SiabY2MMBznrSJd6at0TL-3OpZCCd7cQw9veHlVFuhzCyFFO2JGUIzLFGfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
اسکات، آیا بازار سهام از تو باهوش‌تر است؟
🔴
وزیر خزانه‌داری بسنت:
خیر، قربان.
🔴
ترامپ:
این یک جمله وحشتناک است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/128710" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128709">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ترامپ: توافق با ایران خوب است و این چیزی است که در متن یادداشت تفاهم خواهید دید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/128709" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128708">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: اگر من دخالت نمی‌کردم، ایران خاورمیانه و اسرائیل را نابود می‌کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/128708" target="_blank">📅 19:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128707">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ درباره ایران: بازار سهام بسیار درخشان است. و هر بار که چیزی شگفت‌انگیز می‌گفتیم، مثل «ما قرار است توافق کنیم»، بازار بالا می‌رفت.
🔴
و هر بار، هر بار که چیزی منفی می‌گفتیم، مثل «ببینید، ما قادر نخواهیم بود توافق کنیم»، بازار پایین می‌آمد — خیلی زیاد، خیلی، خیلی زیاد.
🔴
این به شما چیزی می‌گوید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/128707" target="_blank">📅 19:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128706">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ: من با نتانیاهو در مورد لبنان اختلاف نظر داشتم و به او گفتم که مودبانه رفتار کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/128706" target="_blank">📅 19:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128705">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ: من توافق کردم چون نمی‌خواستم شاهد یک فاجعه اقتصادی باشم.
🔴
دو روز گذشته به شدت دشوار بوده است، و ما به ایرانی‌ها اطلاع داده‌ایم که اگر به توافقی نرسیم، بمباران آن‌ها را برای شب دوم از سر خواهیم گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/128705" target="_blank">📅 19:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128704">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ: من توافق کردم چون نمی‌خواستم شاهد یک فاجعه اقتصادی باشم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/128704" target="_blank">📅 19:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128703">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ: فکر می‌کنم رهبران ایران رفتار بسیار متفاوتی خواهند داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/128703" target="_blank">📅 19:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128702">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ: دو روز گذشته فرصتی بود تا درباره جزئیات توافق با نزدیک‌ترین دوستانمان صحبت کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/128702" target="_blank">📅 19:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128701">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ: اگر به جنگ ادامه می‌دادیم، تنگه هرمز هرگز باز نمی‌شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/128701" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128700">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ترامپ: من در اجلاس گروه هفت جزئیات توافق ایران را با رهبران این کشورها مورد بحث قرار دادم و آنها از اینکه به توافق رسیدیم بسیار خوشحال هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/128700" target="_blank">📅 19:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128699">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ: توافق با ایران هر آنچه را که می‌خواستیم، از جلوگیری از دستیابی این کشور به سلاح هسته‌ای گرفته تا باز کردن تنگه هرمز، محقق کرد
🔴
قیمت نفت پس از توافق با ایران به سطوح بی‌سابقه‌ای کاهش یافته است
🔴
اگر ما این توافق را انجام نداده بودیم، تنگه هرمز باز نمی‌شد و بمب‌ها همچنان بی‌وقفه می‌افتادند.
🔴
دو روز گذشته بسیار سخت بوده است و ما به ایرانی‌ها اطلاع داده‌ایم که اگر به توافق نرسیم، برای دومین شب به بمباران آنها باز خواهیم گشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/128699" target="_blank">📅 19:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128698">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
آکسیوس: حتی اگر زمان امضا تغییر کند، نشست هیئت‌های آمریکا و ایران به ریاست جی‌دی ونس، معاون رئیس‌جمهور آمریکا، و محمدباقر قالیباف، رئیس مجلس ایران، طبق برنامه روز جمعه در سوئیس برگزار خواهد شد.
🔴
انتظار می‌رود دو طرف درباره آغاز مذاکرات پیرامون برنامه هسته‌ای ایران گفت‌وگو کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/128698" target="_blank">📅 19:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128697">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrUMG92ClyTSLncQ6VDk0xEYerhsycR2zOSJJWSNUx2TMlPN2Vp-IsgmNHDgVQvrAA2-gyPg7DRQhy5IhCMzPu1hfWBfFwrODU5n7uzRppAP7EKDhMEC4cz1aKt8YpW5TWn-CJYbllXaUqQpikZCdJZrS5MXkRtqXxcG4Ja0jJwB2KAy7_cf4Gz95lxbatvBEwelne1t4eut-7tY1zQFyhsP5SxclwI9-kEcpP9gYpVvOSrCj5hrsB59wiACBt3GzIKQTxMbXoeycKZuYa24I58owXveBzELminuEcp1R5Y2TQt4htPTrwYyW1oClmO7rTHtdwTdUGuKgZJ3DVkedA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش وال‌استریت‌ژورنال، دونالد ترامپ که برای شرکت در اجلاس امسال در سواحل جنوبی دریاچه ژنو حضور یافته، چهره‌ای به مراتب آرام‌تر و ملایم‌تر از سال‌های گذشته از خود نشان داده است.
🔴
این تغییر رویکرد در رفتار رئیس‌جمهور آمریکا، توجه تحلیل‌گران را در این نشست بین‌المللی به خود جلب کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/128697" target="_blank">📅 19:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128696">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ایتامار بن گویر تصمیم گرفته بستگان اسرائیلی‌های کشته‌شده را به عنوان ناظران رسمی زندان منصوب کند، اقدامی که با هدف تشدید شرایط بازداشت اسیران فلسطینی انجام می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128696" target="_blank">📅 19:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128695">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
رویترز: تهران به حزب‌الله وعده داده که با آغاز ورود منابع مالی در پی این توافق، حمایت مالی بیشتری از این گروه خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/128695" target="_blank">📅 19:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128694">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UloXT2rvyY5vaE2ymNQkr_-SZbvtg8u2DMaXF-lDlq9wPLSrzXjTu4eWVnWZplTmV4QJxJCQM9WlO-t3fXMmScpYJJRVavWasO5rKNGinqiDT8IBmER09xBarl4KXE9lxJhxvuRIqpz4Tc8-AVWC6VwAWlSSNmdAdKBCYi294AChESLzCSg5--FZVsXNa8oZE1tDAnGFIR6vUuEThRU_W7NF3suwUOmfyq4bvooVhsmGr8GyG1hc5WoTy8o_9DYNu_ghSGZLUL0qmj3CtUH5uqx6J93TOh5SasCiYvXx3WA2-kjxxv93OOoG94nwiVEWNcMtjzX-mLZyO-BO15I5gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال دارایی‌های مسدود شده ایران را اعلام کرد:
🔴
چین: ۲۰-۵۰ میلیارد دلار (بزرگ‌ترین)
🔴
قطر: ۲۰-۵۰ میلیارد (شامل ۶ میلیارد بشردوستانه)
🔴
عراق: ۱۵ میلیارد (برق و گاز)
🔴
هند و کره جنوبی: هرکدام ۷ میلیارد
🔴
ژاپن: ~۳ میلیارد
🔴
آمریکا: ۲ میلیارد
🔴
لوکزامبورگ و عمان: مبالغ کمتر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128694" target="_blank">📅 19:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128693">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
آمریکا در حال بررسی صدور مجوز تولید موشک برای اروپا و اوکراین است
🔴
دونالد ترامپ، رئیس‌جمهور ایالات متحده، قصد دارد از شرکت‌های دفاعی آمریکایی بخواهد که موشک‌ها را تحت لیسانس در اروپا و اوکراین تولید کنند تا کمبودهای حیاتی در پدافند هوایی را جبران نمایند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/128693" target="_blank">📅 19:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128692">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
عارف، معاون اول رئیس‌جمهور: مدیریت تنگه هرمز در دست ماست و برای خدماتی که به کشتی‌ها برای تأمین عبورشان ارائه می‌دهیم، مبالغی دریافت خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128692" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128691">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a57b5fc0a8.mp4?token=SbB8w_XwrhXIancpK9leh3CAQd4AQDya8SkE5y012Axq4IosWk6ornfMc4Z-P1iOUzRbnFL5EeIP2RUfzBtmPiuqNYMc6T_v2xVxZ2zuH69ydyt69-LtHRmGbNzxu-9_vIJ5sVDb6qLOkfgwOe3t3OuvXFdiGhO2UxJ4ycSzLeCzq8gk3U4Fmr6b6hVnGxGWk6k_D8wF1yr0g8Caxq-C3GJ81TuTdqAzm4iyZxbnI1TkgwYrnBAG3HXHmpm30fK9W69ciUl58yiN4d7-NHpokNLrvAKITmV5TLS5aikj-j3ydyf2Pf5hdHlD29tR55GsalYCZON9Wvug1Mn8hjy92Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a57b5fc0a8.mp4?token=SbB8w_XwrhXIancpK9leh3CAQd4AQDya8SkE5y012Axq4IosWk6ornfMc4Z-P1iOUzRbnFL5EeIP2RUfzBtmPiuqNYMc6T_v2xVxZ2zuH69ydyt69-LtHRmGbNzxu-9_vIJ5sVDb6qLOkfgwOe3t3OuvXFdiGhO2UxJ4ycSzLeCzq8gk3U4Fmr6b6hVnGxGWk6k_D8wF1yr0g8Caxq-C3GJ81TuTdqAzm4iyZxbnI1TkgwYrnBAG3HXHmpm30fK9W69ciUl58yiN4d7-NHpokNLrvAKITmV5TLS5aikj-j3ydyf2Pf5hdHlD29tR55GsalYCZON9Wvug1Mn8hjy92Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مکرون درباره ترامپ: من همیشه به رئیس‌جمهور ترامپ اعتماد داشتم چون ما همیشه بسیار صریح صحبت می‌کردیم.
🔴
وقتی اختلاف نظر داشتیم، آن را بیان می‌کردیم، و وقتی او به چیزی متعهد می‌شود، به آن تعهدات پایبند بوده است.
🔴
و امروز، آمریکا و ترامپ به چیزی متعهد شدند، و این بسیار مهم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128691" target="_blank">📅 19:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128690">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeKmxB8xAuOsG4DOrigcXREoiLP5lpRxf5In2Jj45zhsv3kRXcLStvQDD_5YW834XpFcVgaPAmCMo5XkOb3GnxQqOTMtTacuFeh7NOMZgd-MTNVx3I-5gnidyBe9CHDaSi-W3k9Xh4c7y_5qpV0QQxf8OG9guDsIW8MvfrTqXXsU9ziMlsI0FhJg8YEqcTuGeM4usJcXMHnHbUAbhREPrmiKi3paIBDPhVWIPh9ckCYUrCBqymPDDJjmem8q3Wa3e7arpLIjWPhTPFJvcepfutjfMlu9uTPZMQCzM2tOIdK5PQxfIc4YwYtAy5MnoxdVZ0eYYLgwvHsbYaolpXzxBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: ایالات متحده، ایران و میانجی‌ها در حال بحث در مورد تسریع امضای تفاهم‌نامه هستند که در حال حاضر برای جمعه برنامه‌ریزی شده است، و شاید حتی امروز آن را "به صورت الکترونیکی" امضا کنند.
🔴
جلسه مذاکره‌کنندگان همچنان برای جمعه در سوئیس برنامه‌ریزی شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/128690" target="_blank">📅 19:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128689">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
سفارت ایتالیا در تهران روز جمعه بازگشایی می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/128689" target="_blank">📅 18:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128688">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
رئیس‌جمهور فرانسه امانوئل ماکرون:
من فکر می‌کنم توافق ایران ترامپ معامله خوبی است.
🔴
البته که همه چیز را فوراً حل نمی‌کند.
🔴
اما اگر به مبارزه ادامه می‌دادیم، چه معنایی داشت؟ این به معنای بسته ماندن تنگه بود.
🔴
ماکرون درباره لبنان: حزب‌الله باید در لبنان سلاح‌های خود را زمین بگذارد. از سوی دیگر، اسرائیل نیز باید این کار را انجام دهد.
🔴
نباید هیچ جنگی رخ دهد. آنچه باید اتفاق بیفتد، صلح است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128688" target="_blank">📅 18:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128687">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
مقام ایرانی به تسنیم : سفر تیم مذاکره کننده به سوئیس لغو نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/128687" target="_blank">📅 18:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128686">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c6252578.mp4?token=ujyW-DxoMfuYgLrV_JB3a7ogcBnH1bTdVLsTPRrqH0VnohPnCMMA6coeEt5rguvIHHE1eGcszM7oMHY4dr_ei1zrvhtvkmRXpBPNPqL9DrZ22iAr9bBPpn35q-rYGQ40nwzcnRO_6xYznKfUvIL-rYPP0LNo2Oe5-gnSLFugNR7vjIuSNfRl3yroFVP18U_3R97MBfGiMduc4JsyEse-YBPZZo_uOrhc-jCOu0igxdco2HVuhpYMYX1safcCFfG_0MiEjj7SZXsqpxfbF8_08iPtA3KReOEn3mifbQMJme5edCFB4GkP71bj6K6Gdemw-53FVFTEP4aecoIjsxIt3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c6252578.mp4?token=ujyW-DxoMfuYgLrV_JB3a7ogcBnH1bTdVLsTPRrqH0VnohPnCMMA6coeEt5rguvIHHE1eGcszM7oMHY4dr_ei1zrvhtvkmRXpBPNPqL9DrZ22iAr9bBPpn35q-rYGQ40nwzcnRO_6xYznKfUvIL-rYPP0LNo2Oe5-gnSLFugNR7vjIuSNfRl3yroFVP18U_3R97MBfGiMduc4JsyEse-YBPZZo_uOrhc-jCOu0igxdco2HVuhpYMYX1safcCFfG_0MiEjj7SZXsqpxfbF8_08iPtA3KReOEn3mifbQMJme5edCFB4GkP71bj6K6Gdemw-53FVFTEP4aecoIjsxIt3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره پرونده اپستین: بدون مدرک نمی‌توان کسی را تحت پیگرد قرار داد
جی‌دی ونس در واکنش به پرونده‌های مرتبط با جفری اپستین گفت:
🔴
«صرف اینکه فکر کنیم اتفاقی اشتباه رخ داده، برای محاکمه افراد کافی نیست.»
او تاکید کرد:
🔴
«تنها زمانی می‌توان افراد را تحت پیگرد قانونی قرار داد که مدارک کافی برای اثبات تخلف آنها وجود داشته باشد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128686" target="_blank">📅 18:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128685">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
مکرون: ترامپ، مانند همهٔ ما، موافق بود که از سوی روسیه هیچ تمایل جدی‌ای برای برگزاری گفت‌وگوهای صلح یا مذاکرات وجود نداشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128685" target="_blank">📅 18:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128684">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ترامپ: من وارد توافق‌هایی شده‌ام که ۱۰۰ درصد قطعی بودند، اما عملی نشدند؛ وارد توافق‌هایی هم شده‌ام که هیچ شانسی برای انجام‌شان وجود نداشت، اما اتفاق افتادند؛ فکر می‌کنم توافق [با ایران] انجام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/128684" target="_blank">📅 18:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128683">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f35d9ebf38.mp4?token=NxIGyaAAP8Fw7Mz36xdTJBSPHk_ufERUWwndI5GmZWlc3NFaztcZLXWr3HvkyOtNsROZpCO15H8zdZcts7TcALbRtmEVL4bfh-nkJ_54JGTqlAkvtEDJ94wYOaiJQl5b3p62-8x4vyJbJqraD6okN9uiVtd-EBK2wa2AssGl-pzcWxtsDrvvnCypw0vx3oX5sN7PFJ2uAZC7dTS2KFePjnwcR7jEK8idZV_qZRPb8Qzy0iShVWyr_lBn_IQWM2Wj5H5eZYiAIbhQjTatZLPG0a0V6RlRTZ8sJhBo6FcKoYdXSI2OTGFjmr_00TXEUgdlhotk8f3UkC1HfhwOtKqq8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f35d9ebf38.mp4?token=NxIGyaAAP8Fw7Mz36xdTJBSPHk_ufERUWwndI5GmZWlc3NFaztcZLXWr3HvkyOtNsROZpCO15H8zdZcts7TcALbRtmEVL4bfh-nkJ_54JGTqlAkvtEDJ94wYOaiJQl5b3p62-8x4vyJbJqraD6okN9uiVtd-EBK2wa2AssGl-pzcWxtsDrvvnCypw0vx3oX5sN7PFJ2uAZC7dTS2KFePjnwcR7jEK8idZV_qZRPb8Qzy0iShVWyr_lBn_IQWM2Wj5H5eZYiAIbhQjTatZLPG0a0V6RlRTZ8sJhBo6FcKoYdXSI2OTGFjmr_00TXEUgdlhotk8f3UkC1HfhwOtKqq8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اروپایی‌ها به ابن نتیجه رسیده‌اند که حق با من است
🔴
خبرنگار: ما در این اجلاس شاهد برخورد بسیار گرم رهبران اروپایی با شما بودیم. آیا فکر می‌کنید آن‌ها دارند با جهان‌بینی شما همسو می‌شوند؟
🔴
ترامپ: خب، فکر می‌کنم آن‌ها به این نتیجه رسیده‌اند که حق با من بود. راستش را بخواهید، من معمولاً همیشه درست می‌گویم. فکر می‌کنم آن‌ها معتقدند حق با من بود و الان حس خوبی دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/128683" target="_blank">📅 18:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128682">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ترامپ: من معتقدم ایرانی‌ها یادداشت تفاهم را اجرا خواهند کرد
🔴
ترامپ : ایران سلاح هسته‌ای نخواهد داشت و تنگه هرمز فوراً باز خواهد شد.
🔴
شاخص‌های بازار سهام به لطف توافق با ایران در حال افزایش هستند، در حالی که قیمت نفت در حال کاهش است.
🔴
ما ایرانی بدون سلاح هسته‌ای خواهیم داشت.
🔴
ایران ۴۷ سال از جهان سوءاستفاده کرده است و توافق فعلی من دیواری است که مانع از دستیابی ایران به سلاح هسته‌ای می‌شود.
🔴
در حال بررسی تحریم‌های جدید علیه روسیه هستم.
🔴
توافق با ایران انجام خواهد شد و آنها می‌خواهند به زندگی عادی برگردند.
🔴
من مانع از دستیابی ایران به سلاح هسته‌ای شدم و تفاهم‌نامه با آنها بلندمدت است؛ من معتقدم که به قرارداد تبدیل خواهد شد.
🔴
اگر ایران یادداشت تفاهم را تکمیل نکند، دوباره به نقطه شروع برمی‌گردیم.
🔴
ما به ایران رفتیم و آنها را در هفته اول از نظر نظامی شکست دادیم و من می‌خواهم اسرائیل حس قضاوت خوبی داشته باشد.
🔴
من معتقدم ایرانی‌ها یادداشت تفاهم را اجرا خواهند کرد و اگر این کار را نکنند، ما بمباران را از سر خواهیم گرفت.
🔴
می‌خواهم اسرائیل بتواند از خودش دفاع کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/128682" target="_blank">📅 18:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128681">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: اسرائیل مجاز است از خود دفاع کند اما من می‌خواهم اسرائیل با تدبیر عمل کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128681" target="_blank">📅 18:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128680">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_E4rQAUDbTTIGzLwDWfrmxXLfIc9eOVM2riP5BPmIJ6Xn3DpkYlyv0XvD9SS_CUpu_c9qKw-kyFMakIqpIhhxIvmqPaGNf1AJFiGgZTLSVsK6l5Or8l9zGZzJk28X3xgKGgY9K7xGh6nYMiXVFID_V-4R-V2l4D4F3piGeJAGYOwv9lIJXoq0B5c9eXPuksbyjnEXGmtLFU6YqaHGLYdhjf12uNR49To8UUFsRqtckF--UMIJ5zi1_BE-fY_lkQXWAUA3qgsmEMVPMYweqfFwA8M-GcV9tkN-SrKYGIV2O1-QMIcblY15MADGoP7KOr0u-pYnIpRCW85GcdYZDw2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
من در عرض ۴۵ دقیقه از فرانسه یک کنفرانس خبری برگزار خواهم کرد. سپس به ورسای برای صرف شام با رهبران فرانسوی و دیگر رهبران اروپایی خواهم رفت و بعد از آن امشب به خانه بازمی‌گردم!
🔴
این سفر یک موفقیت بزرگ بود، اما عمدتاً چیزی که همه می‌خواستند درباره‌اش صحبت کنند این است که ایران سلاح هسته‌ای نخواهد داشت و تنگه هرمز فوراً باز خواهد شد!
🔴
شاخص‌های عظیمی در همه بخش‌ها برای اقتصاد ایالات متحده وجود دارد، به طوری که امروز بیشتر از همیشه افراد مشغول به کار هستند.
🔴
بیش از ۱۹.۱ تریلیون دلار در آمریکا سرمایه‌گذاری شده است، با تمام کارخانه‌ها و سایر موارد، اما نکته مهم این است که شاخص‌های اخیر بازار سهام به دلیل توافق افزایش یافته‌اند و به همین ترتیب، قیمت نفت به سرعت در حال کاهش است! رئیس‌جمهور دونالد ج. ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128680" target="_blank">📅 17:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128679">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_QDs6Qsw5pk31OLPK7QtcIUXPzicfmXvYqvfSfp4dUkov37pK5nSYwlV8rDqnhpNurIM3JMHWQveOScEEMvoc2OwysPr1DI1VFXKGCUIr6M-sUM_LVptEz_mQbpXQLn49YjEjFaVrpImKdL-96mPnPJTsx92JkRI23oZcbjWVm2XraITsb8ZlMQUi6NO_I1Y8iHcRRTomU3OL7A0PbrU6zzPZDLpjhqszeW8Qp_ruLnIvdVgt-GpwVmdRVdZabdiBMUfAJNA-P7fAtZZSAeiZgbZVtnYmky5L5UnacPhmV7TYK8i39AgIYD5D9qOim_IIs61QvRgtzmiQt62fSbPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت سوئیس:
بیش از ۲۰۰۰ سرباز امنیت محل امضای توافق ایران و آمریکا را تأمین خواهند کرد و منطقه پرواز ممنوع برای تضمین امنیت اعمال خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128679" target="_blank">📅 17:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128678">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
جی‌دی ونس: برخی افراد فقط می‌خواهند بمباران ادامه یابد، صرف نظر از اینکه آیا برای آمریکایی‌ها دستاوردی دارد یا خیر.
🔴
ترامپ سعی در ایجاد بدبختی برای مردم ایران ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128678" target="_blank">📅 17:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128677">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c64bf468.mp4?token=oqTUepKxxUbeULAYA56UfUXghfD62veBHExIMR8GBT6ogPF_0qn3msqpUo_v1QcZd3Mcz0bbTX-lXX5yvf_L6EywKCU5d_mJ_kKKGImde5BMnqMhafMtzFyp5IDb0MJpmkDBRcp0mHbbE7V1kzVmCYETJT7rrmiAa0QMkHVK5p9Y6go_Ij8UnjuMOuqKC634GBsBynQ_Lqn22hOpAgbPbo7ib0z9N1ik0euUCTSazU7bTEVCRwCQ_r4RHi4itEXj8q36hXzpVHABbcRVwvs3euvHqlLq_EoM3lCgzh4NOIsNRVw1DGch0_TxEYNIpONVVHasiqi6LBDpbJCw075bYY2dIpeZIgd_dHnSH27q9XTjULzXTI9u0L-XnKiMdozN_k8lLgYr0ml2vnVoo8KZ0TZKOAzTbPE7-vSW1UXN7UcS1dOflePpJsABEVBWUQ3AYl_o2lx5wjxV3IWzO_H7OiOZon8S0PhPiuDdTxMzFe9qcOHPRSPEwllh2xsw5KMKJ5WGrb0ZByHesRvaXr713CfLLHkt6-yBXazlzd0VKRzNNtvswsouFc48zHhVONPwAMN8m5qHC2-ViHQKcJ6ExV5sHiL4elSwuX3ZMkfrKskIpBUvoj-DfG6DQBBrqM26hoCNQbTF8_2SYEAnBcSiltQO15YgwEqUuVkUgpbxhBU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c64bf468.mp4?token=oqTUepKxxUbeULAYA56UfUXghfD62veBHExIMR8GBT6ogPF_0qn3msqpUo_v1QcZd3Mcz0bbTX-lXX5yvf_L6EywKCU5d_mJ_kKKGImde5BMnqMhafMtzFyp5IDb0MJpmkDBRcp0mHbbE7V1kzVmCYETJT7rrmiAa0QMkHVK5p9Y6go_Ij8UnjuMOuqKC634GBsBynQ_Lqn22hOpAgbPbo7ib0z9N1ik0euUCTSazU7bTEVCRwCQ_r4RHi4itEXj8q36hXzpVHABbcRVwvs3euvHqlLq_EoM3lCgzh4NOIsNRVw1DGch0_TxEYNIpONVVHasiqi6LBDpbJCw075bYY2dIpeZIgd_dHnSH27q9XTjULzXTI9u0L-XnKiMdozN_k8lLgYr0ml2vnVoo8KZ0TZKOAzTbPE7-vSW1UXN7UcS1dOflePpJsABEVBWUQ3AYl_o2lx5wjxV3IWzO_H7OiOZon8S0PhPiuDdTxMzFe9qcOHPRSPEwllh2xsw5KMKJ5WGrb0ZByHesRvaXr713CfLLHkt6-yBXazlzd0VKRzNNtvswsouFc48zHhVONPwAMN8m5qHC2-ViHQKcJ6ExV5sHiL4elSwuX3ZMkfrKskIpBUvoj-DfG6DQBBrqM26hoCNQbTF8_2SYEAnBcSiltQO15YgwEqUuVkUgpbxhBU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک روحانی: من شاااشیدم وسط ایران مذاکرات و دوقطبی‌ای که میگید، مذاکره اوج بیشرفیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/128677" target="_blank">📅 17:06 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
