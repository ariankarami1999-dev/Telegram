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
<img src="https://cdn4.telesco.pe/file/OqkIfdE7UyyexyzDUvqd6gaCTPcDr6J_TTdSpaj9I7CPLVNoFpYvRJZvIav4OvTDonO9T69zL_vndEPzJGTJVF3isCOcKJuDWWAM1LylOLiJx-sd6TGpZ4UuCq2Ks5Oeznn5pgMhHSNct3tAEq5arE0_dk5afJKboRxsAIzRfX_qgnG9cC6moldalgZqEuzFLsl2XjYrHUyJpM67pnFOm_fn90MO-7YMyx8LwoPAoDzDijumUqsgRX5ISkV0wiMoMdFyRYfW1JjEq-SQshmvQbLHZq2oCjr21Hy5bLFcbi59IaMtmNN0sSOiiRSrA8HK63iClERNJsEs_ItsplrmOw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 330K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 23:05:04</div>
<hr>

<div class="tg-post" id="msg-15189">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">۹. جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت می‌کنند که تا زمان توافق نهایی وضعیت موجود را حفظ کنند؛ جمهوری اسلامی ایران وضع موجود را در برنامه هسته‌ای خود حفظ خواهد کرد، و ایالات متحده آمریکا هیچ تحریم‌های جدیدی علیه ایران وضع نخواهد کرد و نیروهای نظامی بیشتری را در منطقه مستقر نخواهد کرد.
@withyashar
۱۰. ایالات متحده آمریکا متعهد می‌شود بلافاصله با امضای این یادداشت تفاهم و تا زمان خاتمه تحریم‌ها، اسقاطیه‌های وزارت خزانه‌داری را برای صادرات نفت خام ایران، محصولات پتروشیمی و مشتقات آنها، و تمامی خدمات مرتبط شامل تراکنش‌های بانکی، بیمه‌ها، حمل و نقل و غیره صادر کند.
۱۱. ایالات متحده آمریکا متعهد می‌شود تا وجوه و دارایی‌های محدود یا مسدود شده جمهوری اسلامی ایران را با اجرای این یادداشت تفاهم به طور کامل برای استفاده در دسترس قرار دهد. ایالات متحده آمریکا و جمهوری اسلامی ایران در مورد روال مربوط به آزادسازی این وجوه در طول مذاکرات، به صورت دوجانبه توافق می‌کنند. این وجوه، چه در حساب اصلی نگهداری شوند و چه منتقل شوند، برای پرداخت به هر ذینفع نهایی که توسط بانک مرکزی جمهوری اسلامی ایران تعیین می‌شود، باید به طور کامل قابل استفاده شوند. ایالات متحده آمریکا متعهد می‌شود که تمامی تاییدیه ها و مجوزهای لازم را در این رابطه صادر کند.
@withyashar
۱۲. جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت می‌کنند تا یک سازوکار اجرایی برای نظارت بر اجرای موفق این یادداشت تفاهم و پایبندی آتی به توافق نهایی تشکیل شود.
۱۳. پس از امضای این یادداشت تفاهم و منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ این یادداشت تفاهم و تداوم اجرای این اقدامات، جمهوری اسلامی ایران و ایالات متحده آمریکا مذاکرات درخصوص توافق نهایی را منحصرا در مورد بقیه بندها آغاز خواهند کرد.
۱۴. توافق نهایی با یک قطعنامه الزام‌آور شورای امنیت سازمان ملل متحد تایید خواهد شد.
(امضاء) از طرف دولت جمهوری اسلامی ایران
تاریخ
(امضاء) از طرف دولت ایالات متحده آمریکا
تاریخ
( امضاء) در حضور میانجی
از طرف دولت جمهوری اسلامی پاکستان
تاریخ
@withyashar</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/withyashar/15189" target="_blank">📅 22:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15188">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یادداشت تفاهم اسلام‌آباد بین جمهوری اسلامی ایران و ایالات متحده آمریکا
به گزارش تسنیم، متن تفاهم‌نامه ایران و آمریکا به شرح ذیل است:
جمهوری اسلامی ایران و ایالات متحده آمریکا، به طور مشترک و با حسن نیت، در تاریخ ۲۸ خرداد ۱۴۰۵ نسبت به موارد زیر توافق کردند:
@withyashar
۱. جمهوری اسلامی ایران و ایالات متحده آمریکا و متحدین آنها در جنگ حاضر، با امضای این یادداشت تفاهم خاتمه فوری و دائمی عملیات‌های نظامی را در تمامی جبهه‌ها، از جمله در لبنان، اعلام کرده و تعهد می‌کنند از این پس هیچ جنگ یا هیچ عملیات نظامی علیه یکدیگر آغاز نکنند و از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند و تمامیت ارضی و حاکمیت لبنان را تضمین کنند. توافق نهایی خاتمه دائمی جنگ در تمامی جبهه‌ها، از جمله در لبنان، و بقیه مفاد این بند را تایید خواهد کرد.
۲. جمهوری اسلامی ایران و ایالات متحده آمریکا متعهد می‌شوند که به حاکمیت و تمامیت ارضی یکدیگر احترام بگذارند و از مداخله در امور داخلی یکدیگر خودداری کنند.
@withyashar
۳. جمهوری اسلامی ایران و ایالات متحده آمریکا به انجام مذاکرات و حصول به یک توافق نهایی در مدت حداکثر ۶۰ روز، قابل تمدید با رضایت طرفین، متعهد می‌شوند.
۴. بلافاصله با امضای این یادداشت تفاهم، ایالات متحده آمریکا شروع به رفع محاصره دریایی خود و هرگونه مزاحمت یا ممانعت علیه جمهوری اسلامی ایران می‌کند، و ظرف ۳۰ روز به محاصره دریایی به طور کامل خاتمه خواهد داد. در طول این مدت، تردد کشتی‌ها متناسب با تعداد ترافیک قبل از جنگ که از سوی جمهوری اسلامی ایران برقرار می‌شود، خواهد بود. ایالات متحده آمریکا همچنین متعهد می‌شود تا ظرف ۳۰ روز پس از توافق نهایی، نیروهای نظامی خود را از حوزه پیرامونی جمهوری اسلامی ایران خارج کند.
۵. با امضای این یادداشت تفاهم، جمهوری اسلامی ایران ترتیباتی را با حداکثر تلاش خود برای عبور ایمن کشتی‌های تجاری، بدون هزینه فقط برای ۶۰ روز، از خلیج فارس به دریای عمان و بالعکس، اتخاذ خواهد کرد. تردد کشتی‌های تجاری بلافاصله آغاز، و با توجه به ضرورت رفع موانع فنی و نظامی و مین‌زدایی توسط جمهوری اسلامی ایران، ظرف ۳۰ روز برقرار خواهد شد. جمهوری اسلامی ایران با سلطنت عمان برای تعیین اداره آینده و خدمات دریایی در تنگه هرمز، مطابق با حقوق بین الملل قابل اجرا و حقوق حاکمیتی کشورهای ساحلی تنگه هرمز، گفتگو خواهند کرد و با دیگر کشورهای ساحلی خلیج فارس نیز تبادل نظر می‌کنند.
@withyashar
۶. ایالات متحده آمریکا متعهد می‌شود، با شرکای منطقه‌ای خود، برای بازسازی و توسعه اقتصادی جمهوری اسلامی ایران یک برنامه قطعی مورد توافق طرفین را با تامین حداقل ۳۰۰ میلیارد دلار ایجاد کند. سازوکار اجرایی‌سازی این برنامه، به عنوان بخشی از توافق نهایی ظرف ۶۰ روز نهایی خواهد شد. تمامی تائیدیه‌ها، اسقاطیه‌ها و مجوزهای مورد نیاز برای تراکنش‌های مالی مربوطه توسط ایالات متحده آمریکا ارائه خواهد شد.
۷. ایالات متحده آمریکا متعهد می‌شود به تمامی انواع تحریم‌ها علیه جمهوری اسلامی ایران، از جمله قطعنامه‌های شورای امنیت سازمان ملل متحد، قطعنامه‌های شورای حکام آژانس بین‌المللی انرژی اتمی، و تمامی تحریم‌های یکجانبه آمریکا، اعم از اولیه و ثانویه، برابر یک برنامه زمانی مورد توافق به عنوان بخشی از توافق نهایی، خاتمه دهد. جمهوری اسلامی ایران و ایالات متحده آمریکا به اهمیت اساسی موضوع خاتمه تحریم‌ها که در بالا ذکر شده است اذعان دارند و قصد خود را برای رسیدگی فوری به این موضوعات در مذاکرات، به منظور دستیابی به توافق متقابل در مورد آنها اظهار می‌کنند.
۸. جمهوری اسلامی ایران مجدداً تایید می‌کند که سلاح هسته‌ای تولید یا ابتیاع نخواهد کرد. جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت کرده‌اند که وضعیت مواد غنی‌شده ذخیره شده را از طریق یک سازوکار مورد توافق طرفین و مطابق با برنامه زمانی مندرج در بند ۷، حداقل به شیوه رقیق‌سازی در محل، تحت نظارت آژانس بین‌المللی انرژی اتمی، حل و فصل کنند. دو طرف همچنین موافقت می‌کنند تا در مورد موضوع غنی‌سازی، و دیگر موضوعات مورد توافق دو طرف مرتبط با نیازهای هسته‌ای جمهوری اسلامی ایران، بر اساس یک چارچوب رضایت‌بخش که در توافق نهایی مورد موافقت قرار خواهد گرفت، بحث کنند. توافق نهایی مفاد این بند را تایید خواهد کرد. جمهوری اسلامی ایران و ایالات متحده آمریکا به اهمیت اساسی موضوعات هسته‌ای ذکرشده در بالا اذعان دارند و قصد خود را برای رسیدگی فوری به این موضوعات در مذاکرات، به منظور دستیابی به توافق متقابل در مورد آنها اظهار می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/withyashar/15188" target="_blank">📅 22:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15187">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">طبق برخی گزارش ها نیروهای ارتش جولانی در سوریه برای ورود به لبنان و مبارزه با حزب اللّه آماده میشوند
🚨
@withyashar</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/withyashar/15187" target="_blank">📅 22:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15186">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">شبکه خبر: انتشار متن تفاهم نامه ایران و آمریکا تا دقایقی دیگر
@withyashar</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/withyashar/15186" target="_blank">📅 22:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15185">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شبکه i24News اسرائیل:
متن رسمی یادداشت تفاهم ایران و آمریکا منتشر شده و طبق این توافق، همه درگیری‌ها از جمله در لبنان باید فورا متوقف بشه.
همچنین یک برنامه اقتصادی 300 میلیارد دلاری برای جمهوری اسلامی در نظر گرفته شده.
بر اساس گزارش، ذخایر اورانیوم با غنای بالای ایران داخل کشور و تحت نظارت آژانس رقیق خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/withyashar/15185" target="_blank">📅 22:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15184">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/withyashar/15184" target="_blank">📅 22:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15183">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3f8b7f61.mp4?token=Kqium351hovlMo_IV89cLmtz6DpU5Ljw_3Yx3yAj6YAHqlVV2hYR7tsXg6JCuQ2PeFPNci6G32sHI5LdSQWm-UWZ4c5MUN25jWZA2tQCLo7DwDLn-vfAFLAHV1tioEx6k3FiBBW3WlxwiLrPMbqk_IqB1aIcgYPJ00obr4PBeDwdW8S-OzaTylOhKbTbj5Wn3aQAwl7CeNj7-TVdA74s_ub5qdFmSLZ8wLE3Qe5OWLw_TTYLt9FxMh8VvAMCdii_ivXRPZpgkOwOUqpUwm8Fdf3TZmxw4BcjfiCw2b7Bgy5nBw4UUdOvs4OoQ3MjWzU59AUv38rbgCRlkKBlFTPSCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3f8b7f61.mp4?token=Kqium351hovlMo_IV89cLmtz6DpU5Ljw_3Yx3yAj6YAHqlVV2hYR7tsXg6JCuQ2PeFPNci6G32sHI5LdSQWm-UWZ4c5MUN25jWZA2tQCLo7DwDLn-vfAFLAHV1tioEx6k3FiBBW3WlxwiLrPMbqk_IqB1aIcgYPJ00obr4PBeDwdW8S-OzaTylOhKbTbj5Wn3aQAwl7CeNj7-TVdA74s_ub5qdFmSLZ8wLE3Qe5OWLw_TTYLt9FxMh8VvAMCdii_ivXRPZpgkOwOUqpUwm8Fdf3TZmxw4BcjfiCw2b7Bgy5nBw4UUdOvs4OoQ3MjWzU59AUv38rbgCRlkKBlFTPSCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با هواپیما به سمت کاخ ورسای رفت، تا مکرون و رهبران کشوران اروپایی شام بخوره
@withyashar</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/withyashar/15183" target="_blank">📅 22:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15182">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAxxSZMWoBwP7TrKOQFdtBj4HabKEqIX1BzLfiJLB6baN8dPD7rtiRpARtXMR1SAQzyc2DfE9CDlZ4qEQGhSmRNlAx1APCnXXvvrEdmD9cu0VYdoQQ1q6ADsyuaQgaqT6_98CluFWVq6tPx33TR6306XFAuLnnN4HX4exh1m1eYvu88RCFQ9rAdwl4tSKydaC59bnTE2j780nWUlnU_Feroos4MNBs2-1xhWCPEyVQ2-EV2to_RbM9G-S3RTKwHwEKBsDOEHAZKza04e-nh58IK_AeamehJDjw_DCfzVhrm5keV3ogfzjiEP2Wxsl-qkJt4E-bemdTLPUGSTYSwTPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور لیندسی گراهام: به نظر من امضای این تفاهم‌نامه به نفع آمریکا خواهد بود، چون تنگه هرمز شروع به بازگشایی میکنه و درگیری‌ها با ایران متوقف میشه.
اینکه آیا آمریکا میتونه با ایران بر سر برنامه هسته‌ای و سایر مسائل به توافقی قابل قبول و قابل راستی‌آزمایی برسه یا نه، هنوز مشخص نیست، اما من تلاش برای رسیدن به چنین توافقی رو کم‌هزینه می‌بینم.
@withyashar</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/withyashar/15182" target="_blank">📅 22:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15181">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وزارت امور خارجه ایران: ادامه اشغال جنوب لبنان توسط اسرائیل، نقض تفاهم‌نامه است و ما اقدامات لازم را انجام خواهیم داد
ایالات متحده متعهد شده است که تمام تحریم‌ها از جمله تحریم‌های شورای امنیت سازمان ملل را در یک جدول زمانی که در طول مذاکرات مورد بحث قرار خواهد گرفت، لغو کند
@withyashar</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/withyashar/15181" target="_blank">📅 21:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15180">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
کانالی که ترور هنیه و نصرالله رو دقیق پیشبینی کرده بود، دلار ۱۶۰ تومنی رو هم دو ماه پیش اعلام کرده بود از تاریخ و نحوه حمله ایران به اسرائیل پرده برداشت!!!
🚨
نمیدونم به کجا وصله ولی از همه چی خبر داره بیا خودت ببین
👇
👇
🔴
LINK - CHANNEL
🔴</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/withyashar/15180" target="_blank">📅 21:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15179">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">الجزیره به نقل از وزارت امور خارجه ایران: در حال حاضر در حال بررسی ایده امضای تفاهم‌نامه از راه دور توسط رؤسای جمهور ایران و ایالات متحده هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/15179" target="_blank">📅 21:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15178">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">معاون وزیر ارتباطات: اینترنت دیگر در شرایط بحران قطع نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/15178" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15177">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یک مقام کاخ سفید: نشست سوئیس برای مرحله بعدی بسیار مهم خواهد بود زیرا سند کنونی نیت‌های طرفین را منعکس می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/15177" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15176">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خبرنگار: آیا اکنون می‌توانید بگویید که آیا کسی را در دولت خود به خاطر حمله به مدرسه‌ای که در اولین روز جنگ بیش از ۱۰۰ کودک را کشت، مسئول می‌دانید؟
پرزیدنت ترامپ:
این سوال عجیبی است که در این تاریخ پرسیده می‌شود، چون شما درباره زمانی صحبت می‌کنید که مدت زیادی گذشته است، اما کسی این کار را عمداً انجام نداد.
فکر می‌کنم باید درباره آن‌ها بگویید، چه می‌شود درباره هزاران سربازی که وقتی در ماشین خود را باز کردند منفجر شدند؟ چه می‌شود درباره هزاران نفری که توسط ایران کشته شدند؟
اشتباهات رخ می‌دهد، جنگ زشت است، می‌دانم که تحت بررسی است. از پیت هگستث این سوال را می‌پرسم زیرا آن‌ها آن را تحت بررسی دارند.
﻿
@withyashar</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/15176" target="_blank">📅 20:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15175">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_C_y44HU1hpq5MpB-GynrosDUgRxiUw4BvH_WhX7MOhTVpsKc4Mfz3xAytJrX1UBvjL7AJVAsx_lF6QvglOsXwzC5oRaBYqJg3UfuRMbSbnynoYniAygLwbWnA_5TUJHAjwdKFLKmlBZVkxjIhrPIJKS94ZbgPlDqwhElwAV3u4-8s9br731bJ_FobWHBd_OPrCPgArNokQE-00YebLR574vL05wb6Eag-ogqPfkqWPDN--bt-8wHySAhkBNFeKlW5f9JaNSgOykUVRSoawiqV912VMbL-bpoFyIwzVTVOAY9_zwvF177hVhQgylgv0XEIaJ2U86QxQgHOF05faMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌ها از وقوع حادثه دریایی در نزدیکی سواحل یمن
گزارش‌های امنیتی از وقوع یک حادثه دریایی جدید در آب‌های نزدیک به یمن خبر می‌دهد.
گزارش شده قایق‌های تندرو و کوچک ناشناس، یک کشتی عبوری را در فاصله ۱۰۵ مایل دریایی شمال شرق عدن هدف قرار دادند.
@withyashar</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/15175" target="_blank">📅 20:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15174">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer"><a href="https://t.me/withyashar/15174" target="_blank">📅 20:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15173">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ : به آنها می‌گویم: شما احتمالاً سومین ذخایر بزرگ نفت در جهان را دارید، به چه دلیل به سلاح هسته‌ای نیاز دارید؟
@withyashar</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/15173" target="_blank">📅 20:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15172">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ: ایرانی‌ها باید تعدادی موشک داشته باشند، چون دیگران هم دارند
ما روی یک تلاش موازی با کشورهای حوزه‌ی خلیج فارس کار خواهیم کرد تا به مسائل غیرهسته‌ای، مانند موشک‌های بالستیک متعارف که درباره‌شان صحبت خواهیم کرد، و حمایت‌ها بپردازیم.
کسی می‌گفت: شما نباید حتی یک موشک هم به آن‌ها بدهید برخی از این آدم‌ها را دوست دارم، اما فکر نمی‌کنم زیاد باهوش باشند.
می‌گفتند: جناب، شما نباید اجازه دهید آن‌ها هیچ موشکی داشته باشند. من گفتم: «خب، پس من باید چه کار کنم؟ آیا باید اجازه دهم عربستان سعودی موشک داشته باشد، اما آن‌ها نداشته باشند؟» گفتند: «بله جناب.»
اما نمی‌شود، کارها این‌طور پیش نمی‌رود، می‌دانید؟ این‌گونه کارساز نیست و موشک‌ها مشکل اصلی نیستند. موشک‌ها فقط به یک نقطهٔ کوچک آسیب می‌زنند، اما کرهٔ زمین را نابود نمی‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/withyashar/15172" target="_blank">📅 20:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15171">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ : رهبرهای جدید ایران آدم‌های باهوشین، خیلی هم باهوشن؛
به اندازه قبلی‌ها تندرو و افراطی نیستن، فکر می‌کنم واقعاً کشورشون رو دوست دارن و آدم‌های خوبی هستن.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/15171" target="_blank">📅 20:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15170">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ: خب، آنها به سرمایه‌گذاری نیاز دارند، چون ما حدود یک و نیم تریلیون، شاید دو تریلیون دلار خسارت وارد کردیم.
پس کسی باید به آنها کمک کند خب، هیچ تضمینی برای کمک به آنها وجود ندارد، و ممکن است همسایگانشان کمی به آنها کمک کنند، نمی‌دانم، اما این مقدار زیادی پول است.
تقریباً هیچ‌کس چنین پولی ندارد این همان نوع خسارتی است که وارد شده است
@withyashar</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/15170" target="_blank">📅 20:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15169">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ: ما موظف نیستیم چیزی به ایران بدهیم، اما ممکن است برخی بخواهند آنجا سرمایه‌گذاری کنند.
آنها از یک نظر فرهنگی ابتدایی دارند، اما این فرهنگ ابتدایی نابغه است، آنها مردم بسیار باهوش و مذاکره‌کنندگان بسیار خوبی هستند
@withyashar</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/15169" target="_blank">📅 20:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15168">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0786cbbc7f.mp4?token=uivEic-0hOhts1KcykzgZ-qcTgahenF5KqcqZGKjAIIdqYfFQI47fQw1xGf1opHwEkoazsCE9Mjqil_u46wjfXRelmU1bICETz4L6d8SWRjwfiPI7F3UGDRhUvPMOeQSHB2GIQUDlxouNjDJe0xrCLsuVfb5A2GQi9nbsdp-BozlYCDfd2z6aHHRsIOz4t1VGWClABVJhkbVpBw4lGcMPCqF1H4WEKhEWr3k5e-fn2Yg7XUF4OUQiFA42153hYicwb8QbKEYs0uheO7AIDFi1LExze7W__Ks6aiI5dY25OiHIBL6uQwKMg3wRo58yAUn_YOIliCLM2k3AM93dIVVHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0786cbbc7f.mp4?token=uivEic-0hOhts1KcykzgZ-qcTgahenF5KqcqZGKjAIIdqYfFQI47fQw1xGf1opHwEkoazsCE9Mjqil_u46wjfXRelmU1bICETz4L6d8SWRjwfiPI7F3UGDRhUvPMOeQSHB2GIQUDlxouNjDJe0xrCLsuVfb5A2GQi9nbsdp-BozlYCDfd2z6aHHRsIOz4t1VGWClABVJhkbVpBw4lGcMPCqF1H4WEKhEWr3k5e-fn2Yg7XUF4OUQiFA42153hYicwb8QbKEYs0uheO7AIDFi1LExze7W__Ks6aiI5dY25OiHIBL6uQwKMg3wRo58yAUn_YOIliCLM2k3AM93dIVVHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما یک نسخه از توافق ایران را به اسرائیل ارسال کردیم
@withyashar</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/15168" target="_blank">📅 20:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15167">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ: من با نتانیاهو در مورد لبنان اختلاف نظر داشتم و به او گفتم که مودبانه رفتار کند
نتانیاهو گاهی اوقات کمی از کوره در می‌رود، اما من با او همکاری بسیار خوبی دارم
ما به احتمال زیاد توافق را امضا خواهیم کرد و ایران خواهان آن است؛ آنها به طور مناسب عمل کرده و موافقت کرده اند که سلاح هسته ای تولید نکنند
@withyashar</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/15167" target="_blank">📅 20:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15166">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ: من توافق کردم چون نمی‌خواستم شاهد یک فاجعه اقتصادی باشم.
دو روز گذشته به شدت دشوار بوده است، و ما به ایرانی‌ها اطلاع داده‌ایم که اگر به توافقی نرسیم، بمباران آن‌ها را برای شب دوم از سر خواهیم گرفت
@withyashar</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/withyashar/15166" target="_blank">📅 19:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15165">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSBvnwI7OlPnpdybsWrooPzfqhpggcJS-K_iG1knxFkBczumJmT6sinCZA8IecYVr5VjdLFBufUcfE0pAImXumLj-MfISPPL9Fzla04xuBBhNcvcWO3oO202fUt8o3XjtLyxg4df3thOZLcr4_qCvuMbf2k_NeaGRF6pK3S_bZX01JWy5YOhaybnSH0wi3BqbOAguB0qyNodwXtf1gH1Dfvb4s2I8oX6U-QQogplkbd-09bCGGTmSR9IePqV9Qye0J3KnZEBvkIIQyLsZNHAbLSo2JDGIgQ7T9dcnia74WiACzroPrkZ40Q0hAvvRc1lFVPlCgjoIUAf-5CrnlFppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال استریت ژورنال دارایی‌های مسدود شده ایران را اعلام کرد:
چین: ۲۰-۵۰ میلیارد دلار (بزرگ‌ترین)
قطر: ۲۰-۵۰ میلیارد (شامل ۶ میلیارد بشردوستانه)
عراق: ۱۵ میلیارد (برق و گاز)
هند و کره جنوبی: هرکدام ۷ میلیارد
ژاپن: ~۳ میلیارد
آمریکا: ۲ میلیارد
لوکزامبورگ و عمان: مبالغ کمتر
@withyashar</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/15165" target="_blank">📅 19:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15164">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آکسیوس: حتی اگر زمان امضا تغییر کنه، نشست هیئت‌های آمریکا و ایران به ریاست جی‌دی ونس و محمدباقر قالیباف طبق برنامه روز جمعه در سوئیس برگزار خواهد شد.
انتظار میره دو طرف درباره آغاز مذاکرات پیرامون برنامه هسته‌ای ایران گفت‌وگو کنند.
@withyashar</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/15164" target="_blank">📅 19:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15163">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آکسیوس
: دیدار هیئت مذاکره کننده ایرانی و آمریکایی در روز جمعه در سوئیس برای امضای یادداشت تفاهم نامه به احتمال زیاد برگزار نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/15163" target="_blank">📅 18:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15162">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یک منبع نزدیک به تیم مذاکره کننده به تسنیم گفت:
سفر تیم مذاکره کننده به سوئیس در روز جمعه لغو نشده است اما جزییات ترتیبات مربوط به امضای تفاهم نامه همچنان در حال رایزنی است و هنوز هیچ جزییاتی در این باره(چگونگی امضای تفاهم) نهایی نشده است.
@withyashar
اگه تسنیم میگه پس یه خبرهایی هست داره لغو میشه
🤣</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/withyashar/15162" target="_blank">📅 18:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15161">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رئیس جمهور فرانسه، مکرون پیرزن باز:
من فکر می‌کنم توافق ترامپ با ایران توافق خوبی است.
البته که همه چیز را فوراً حل نمی‌کند، نه.
اما اگر ما به جنگیدن ادامه می‌دادیم، این به چه معناست؟ این به معنای بسته ماندن تنگه هرمز بود.
@withyashar</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/15161" target="_blank">📅 18:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15160">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ: من وارد توافق‌هایی شده‌ام که ۱۰۰ درصد قطعی بودند، اما عملی نشدند؛ وارد توافق‌هایی هم شده‌ام که هیچ شانسی برای انجام‌شان وجود نداشت، اما اتفاق افتادند؛ فکر می‌کنم توافق [با ایران] انجام خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/15160" target="_blank">📅 18:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15159">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Parandeh (IG @yashar)</div>
  <div class="tg-doc-extra">Martik (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/15159" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/15159" target="_blank">📅 18:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15158">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ: اگر ایران یادداشت تفاهم را تکمیل نکند، دوباره به نقطه شروع برمی‌گردیم
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/15158" target="_blank">📅 18:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15157">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اخبار اولیه‌ای و تأیید نشده‌ مبنی بر لغو امضای جمهوری اسلامی برای یادداشت تفاهم در روز جمعه، به دلیل حملات به لبنان.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/15157" target="_blank">📅 18:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15156">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph6sMi6Wa5Zx4YmVHJjkXV0H8SkvmAvhqJsgFxo3Rx5wVSKY3_RD6K_utSIVdmCjzbqPNL2ohmgeztFz2R3OE3clFFMEpJcq0EUCrubf2f8PuVDveV-56Pneypz9601Y9oMimsvGbZLScO_Za8t2Vyad2d09sdMiKEmRz86Z7umem5ehug8s8DxgugB6MWJsqy2N6wwP61BKoigY1UwYxn0kwl5YlCuKPfsbP0uU_myOtVKjl3xz5FCwSH1r-4mG5yw7RBQ0MGY9JR9LcQ292u00QFb3i9FoE0pBjegvoYbaTJC8FQHoMwMhan8pC1yRXFIbw1Rj2_ijchQvFBTFOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : من در عرض ۴۵ دقیقه از فرانسه یک کنفرانس خبری برگزار خواهم کرد. سپس به ورسای برای صرف شام با رهبران فرانسوی و دیگر رهبران اروپایی خواهم رفت و بعد از آن امشب به خانه بازمی‌گردم!
این سفر یک موفقیت بزرگ بود، اما عمدتاً چیزی که همه می‌خواستند درباره‌اش صحبت کنند این است که ایران سلاح هسته‌ای نخواهد داشت و تنگه هرمز فوراً باز خواهد شد!
شاخص‌های عظیمی در همه بخش‌ها برای اقتصاد ایالات متحده وجود دارد، به طوری که امروز بیشتر از همیشه افراد مشغول به کار هستند.
بیش از ۱۹.۱ تریلیون دلار در آمریکا سرمایه‌گذاری شده است، با تمام کارخانه‌ها و سایر موارد، اما نکته مهم این است که شاخص‌های اخیر بازار سهام به دلیل توافق افزایش یافته‌اند و به همین ترتیب، قیمت نفت به سرعت در حال کاهش است!
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/15156" target="_blank">📅 17:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15155">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">️جی‌دی ونس: برخی افراد فقط می‌خواهند بمباران ادامه یابد، صرف نظر از اینکه آیا برای آمریکایی‌ها دستاوردی دارد یا خیر.
ترامپ سعی در ایجاد بدبختی برای مردم ایران ندارد
@withyashar</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/withyashar/15155" target="_blank">📅 17:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15154">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اسرائیل پرچم خود را در منطقه‌ای از سوریه برافراشت
منابع خبری در سوریه از نفوذ نظامیان ارتش اسرائیل به روستای «القحطانیه» در استان قنیطره خبر دادند و پرچم خود را برفراشتند
@withyashar</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/15154" target="_blank">📅 17:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15153">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کانال ۱۳ اسرائیل: آمریکا جزئیات توافق با ایران را از اسرائیل مخفی نگه داشته، زیرا نگران است که تل‌آویو محتوای آن را فاش کند و کارزاری رسانه‌ای علیه آن به راه بیندازد
@withyashar</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/15153" target="_blank">📅 17:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15152">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پاکستان خواستار تعویق انتشار متن تفاهم‌نامه شد
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، در گفت‌وگو با CBS اعلام کرد که طرف پاکستانی درخواست کرده است متن کامل یادداشت تفاهم (MOU) فعلاً منتشر نشود.
وی بدون ارائه جزئیات بیشتر گفت که به درخواست پاکستان، متن این سند به‌طور موقت محرمانه باقی خواهد ماند.
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/15152" target="_blank">📅 17:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15151">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سوئیس: امضای یادداشت تفاهم ایران و آمریکا با حضور نمایندگان ۴ کشور ایالات متحده، ایران، قطر و پاکستان برگزار خواهد شد.
بیش‌از ۲۰۰۰ سرباز امنیت محل امضا را تأمین خواهند کرد و برای تضمین امنیت، منطقه پرواز ممنوع اعمال خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/15151" target="_blank">📅 16:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15150">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تسنیم: اختلال خدمات بانکی ادامه دارد , تجهیزات شبکه فرسوده هستند
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/15150" target="_blank">📅 16:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15149">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ایران امروز یک تفاهم‌نامه با شرکت سهامی خاص هلی‌کوپترهای روسی برای ۲۰ هلی‌کوپتر سری mi-8/17 امضا کرد (۴ تا از آن‌ها قبلاً قرارداد بسته شده است) که باید تا مارس ۲۰۲۷ تحویل داده شوند تا برای مقاصد اطفاء حریق، انتقال پزشکی و نجات استفاده شوند
@withyashar</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/15149" target="_blank">📅 16:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15148">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fff486d39a.mp4?token=IvIlFEG6AseEpBHGoOJ0fjOvo5wigaxQwV2DQQTx5JvEyyA-zcmvLEl6fS8ol8kx0nqTFZ-Yu4wbzpgziSiF1uxZZ1JPMZUD2BKnmai8Qo0vkxZMX-tYS1C3XvqLZXMXRNpbNluI53_67Ny1MHz0J48kLixIzSALcBbpdsFZrVaej4vD38hYrqCnWI__TILI1dh07a8oV-ZvzxvRKF7BtGjCxCIJ7lS1dbu1rqUqzGFBjvnkrmB8GJ_eM1XCmXTsOO4s5Yb7W7Dfk93awwff0EzfHELbGNAiVz786IO694I5Vu7lUwumHSaFLNgEvRLpl9g358zgi0lPepDuq9BHPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fff486d39a.mp4?token=IvIlFEG6AseEpBHGoOJ0fjOvo5wigaxQwV2DQQTx5JvEyyA-zcmvLEl6fS8ol8kx0nqTFZ-Yu4wbzpgziSiF1uxZZ1JPMZUD2BKnmai8Qo0vkxZMX-tYS1C3XvqLZXMXRNpbNluI53_67Ny1MHz0J48kLixIzSALcBbpdsFZrVaej4vD38hYrqCnWI__TILI1dh07a8oV-ZvzxvRKF7BtGjCxCIJ7lS1dbu1rqUqzGFBjvnkrmB8GJ_eM1XCmXTsOO4s5Yb7W7Dfk93awwff0EzfHELbGNAiVz786IO694I5Vu7lUwumHSaFLNgEvRLpl9g358zgi0lPepDuq9BHPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: دلیل پایین ماندن قیمت نفت این است که هر شب کشتی‌هایی را از بین می‌بردیم که حتی شما از آن‌ها خبر نداشتید.
دو روز پیش، سه روز پیش، یک ماه پیش، ۲۲ کشتی را از بین بردیم. به طور متوسط هر شب بین ۱۵ تا ۲۵ کشتی را از بین می‌بردیم. هیچ‌کس این را نمی‌دانست.
نیروی دریایی ما کار بزرگی انجام داد. هیچ‌کس نمی‌دانست چه اتفاقی می‌افتد. به همین دلیل نفت به ۳۰۰ دلار در هر بشکه نرسید؛ بلکه به ۱۲۵ تا ۱۵۰ دلار رسید.
حالا قیمت آن ۷۲، ۷۳ دلار است. شنیده‌ام که الان حتی کمتر از این است
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/15148" target="_blank">📅 14:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15147">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ: با احمد الشرع، رهبر سوریه، درباره مقابله با حزب‌الله گفت‌وگو کردم.
@withyashar</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/15147" target="_blank">📅 14:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15146">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b10b0e16f.mp4?token=HtAowuMxu2kSFNyJMCjHIojtxZa_13TN6VhRbjJvod-cHYN4R1r_ZM6yUvWZYIPHUsL12VNku3hWPNIRDZNa6McBZNpeYlLJZcoT-3lv5LVXLVMfm9cliDVNwYE3LOqvo_WBz2ebrfiE40kqSW3zuKWMjNdgnPBkvbdmjLl5kL09Tus7gQparTlnEmmBzg9G1TYsayFDOD-8N0GuDoJIdZBazC7xXdsr3E7rK5o-HaiBr4Ig_eTFB_PUbokUzWwab7yRnJO8mBYJl4Kf3xnd2ZRlv-4DgOLZqreHh7kLz6ElCZIOJFvCS2lPC748CvxJb4iP8uaWD3KyBnvnd_W0dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b10b0e16f.mp4?token=HtAowuMxu2kSFNyJMCjHIojtxZa_13TN6VhRbjJvod-cHYN4R1r_ZM6yUvWZYIPHUsL12VNku3hWPNIRDZNa6McBZNpeYlLJZcoT-3lv5LVXLVMfm9cliDVNwYE3LOqvo_WBz2ebrfiE40kqSW3zuKWMjNdgnPBkvbdmjLl5kL09Tus7gQparTlnEmmBzg9G1TYsayFDOD-8N0GuDoJIdZBazC7xXdsr3E7rK5o-HaiBr4Ig_eTFB_PUbokUzWwab7yRnJO8mBYJl4Kf3xnd2ZRlv-4DgOLZqreHh7kLz6ElCZIOJFvCS2lPC748CvxJb4iP8uaWD3KyBnvnd_W0dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ‌ در‌کنار ژنرال السیسی (واقعی): فراموش نکنید، هیچ‌کس هرگز به اندازه من با ایران سخت‌گیر نبوده است.
این کار باید توسط کلینتون و باراک حسین اوباما انجام می‌شد. این کار باید توسط بایدن، بوش و بسیاری از افراد دیگر انجام می‌شد.
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/15146" target="_blank">📅 14:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15145">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ: قابلیت پرداخت فقط یک حقه دیگر است. آنها کلمه «قابلیت پرداخت» را ساختند
@withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/15145" target="_blank">📅 14:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15144">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ: یادداشت با ایران نهایی نیست. اگر از توافق خوشمان نیاید، دوباره به بمباران بازمی‌گردیم @withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/15144" target="_blank">📅 14:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15143">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ: یادداشت با ایران نهایی نیست. اگر از توافق خوشمان نیاید، دوباره به بمباران بازمی‌گردیم
@withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/15143" target="_blank">📅 14:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15142">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iT5ZtwLy9qfwUOkdwEM53a8I-BtzAXLYDc75jwPauErju-2mCW1GXjZL6Wn2g83kOQ9GjE4BTToMy7GFavsKHvGSdvGwU_UmNTqSZzutnPMFK8ovyflkVGorABjYkINLaVi8XashJk7i_-3Q1lkUcQruymo7NSpO7sUQjkhgBe5dsmXhMOOJMpoM8uoHgwLaDCy0D5k_7o3FHQZxTCISrgpdoRY3BnBLViNKWWvfPmbG44Upd8BlpsX4zcoRjakLb6XQ96-P2wNZ9P52BLToD5WMFJpHcZyjXS-mFzcm3Uh8Y9mvkEWn2h5zBUs7AlrlSnnvdTgpLHylO7p6WthKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندرو تیت که ۱۰۷ بار لیکویید شده، دوباره در صرافی هایپرلیکویید با اهرم ۴۰ و حجم حدوداً ۴ میلیون دلار، روی بیت‌کوین پوزیشن لانگ (خرید) باز کرده و باز هم بخشی از سرمایه‌اش (۱.۳۵ میلیون دلار) لیکویید شد.
اگه قیمت به 64,626 هزار دلار برسه کامل لیکویید می‌شه.
نرخ فعلی بیت‌کوین: 64,800$
@withyashar</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/15142" target="_blank">📅 14:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15141">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d627cfcdc.mp4?token=VQZZJbE-T4dCo7xLRREddp-ke-McUskqFayXR0fI_EOIttFliRtHOQme0iJRfVN6CF4bOqj8TAix_I0x3bGkiQRUtVRfxllvLBKuhXdesxoV3T0LovQMEfpJF_pOpNgl7o7v3wxJ5ubBr4cfl5qGq23YBrFohA3pWNiqAWuQuD4KYK3O5S8AkcvD70hRb_Pp_Cmg85VX_xkuoiZlcv9OwBq_7GAzzivbOTl5yrqb5gtR8ZKvpIp09BD3J96rXyIuWOORP25qQr05I3yiP04rYO9R1GRWny5dmxUW4HhE5vIHF9Fx3D35LXO5QZfICBtsatb6hLDXGdEfB93NbBT9Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d627cfcdc.mp4?token=VQZZJbE-T4dCo7xLRREddp-ke-McUskqFayXR0fI_EOIttFliRtHOQme0iJRfVN6CF4bOqj8TAix_I0x3bGkiQRUtVRfxllvLBKuhXdesxoV3T0LovQMEfpJF_pOpNgl7o7v3wxJ5ubBr4cfl5qGq23YBrFohA3pWNiqAWuQuD4KYK3O5S8AkcvD70hRb_Pp_Cmg85VX_xkuoiZlcv9OwBq_7GAzzivbOTl5yrqb5gtR8ZKvpIp09BD3J96rXyIuWOORP25qQr05I3yiP04rYO9R1GRWny5dmxUW4HhE5vIHF9Fx3D35LXO5QZfICBtsatb6hLDXGdEfB93NbBT9Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‎بخشی از سخنرانی قالیباف که تو رسانه‌ها وایرال شده
دیگه ساختار مدیریتی کشور از فردمحوری خارج شده و گروهی تصمیم میگیریم.
@withyashar</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/15141" target="_blank">📅 14:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15140">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وزیر دفاع اسرائیل کاتز: تمام روستاهای نزدیک به مرز لبنان به صورت سیستماتیک ویران می‌شوند.
@withyashar</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/15140" target="_blank">📅 14:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15139">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فاکس نیوز: ترامپ به زودی درباره توافق ایران کنفرانس خبری برگزار می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/15139" target="_blank">📅 14:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15138">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تسنیم: متن توافقنامه به صورت کامل در روز جمعه و پس از امضا منتشر خواهد شد
یک منبع نزدیک به تیم مذاکره‌کننده   گفت: تفاهمنامه همانطور که پیشتر اعلام شده ۱۴ بند است و موضوعات مربوط به ۱۴ بند نیز بارها در رسانه‌ها مطرح شده، اما جزییاتی که در بلومبرگ‌ درباره هر بندی آمده است در موارد قابل توجهی ناقص است.
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/15138" target="_blank">📅 12:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15137">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRnw-DTlwwU2oABOhyOYtb5MyWtEb6sytpNukUzyHYNGJpk9MgyB5_COaR7DQHmm-6kS1P9g47rljxxVMxc3QtIhdE6zxktNKswkZ6Xk4YO4tpl8Xx9oz2aj7I_YiBigdIH0sSFmRRcv1tSV5GyHlMHmip_KlGz89BzfCeL3OIfijWEQBfgPWXlQwhgaL1p0tt-5jyqQvwdpqlAGQ-zqI3_7laZufBivP9mc3H2LNYOgYpo_HFFfv3CaXZ5ABNNoKu8rGHiYIC9XJQuNKtRRUp3v_CXtD58ymB4PrVWmtViHssyPGHYdAD-Dl1Uxhfxh-eix0VYI68U6T1Axnie6AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودرو پورشه سردار آزمون در کرمان توقیف شد
به گزارش تابناک به نقل از ایسنا، سرهنگ اکبر نجفی ۲۶ در تشریح این خبر گفت: خودروی مذکور که به دلیل تخلفات قانونی و برابر با احکام صادره در لیست توقیفی‌های مصادره اموال سردار آزمون قرار داشت، توسط گشت‌های محسوس و نامحسوس یگان امداد شناسایی و پس از طی مراحل قانونی، به پارکینگ منتقل شد.
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/15137" target="_blank">📅 12:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15136">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">صدای انفجار‌ سیریک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/15136" target="_blank">📅 12:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15135">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بلومبرگ به نقل از یک منبع آگاه اعلام کرد: واشنگتن شروع به توزیع محتوای تفاهم با ایران به کشورهای متحد در اجلاس گروه ۷ در فرانسه کرده است
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/15135" target="_blank">📅 12:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15134">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرگزاری فرانسه: یک گزارش حقوقی دولت آمریکا نشان می‌دهد ارتش این کشور از ابزار هوش مصنوعی گروک متعلق به شرکت اسپیس ایکس تحت مالکیت ایلان ماسک، میلیاردر حوزه فناوری در جنگ علیه ایران استفاده کرده است
@withyashar</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/15134" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15133">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پمپئو وزیر خارجه سابق به فاکس  می‌گوید اگر برداشت ایران از موضع آمریکا درست باشد و تصمیم‌گیران اصلی (سپاه و رهبری) واقعاً تغییر رفتار بدهند، می‌توان به عادی‌سازی و حتی ورود سرمایه‌گذاری فکر کرد، اما احتمال چنین تغییری را بسیار پایین می‌داند. او تأکید می‌کند نباید هیچ پولی—چه مستقیم، چه از طریق واسطه یا حتی
آزادسازی دارایی‌ها—به ایران داده شود، چون به‌جای رفاه مردم، صرف تقویت برنامه موشکی، سپاه و خرید تسلیحات از روسیه و چین می‌شود. در عین حال می‌گوید اگر واقعاً تغییر واقعی رخ دهد، از آن استقبال خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/15133" target="_blank">📅 10:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15132">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBaBrDKqSM8YqLI1OnybSv9Ml3C20RhMDQI9b0QWE0aR3UhJO_rp0Hlx5cGyyrICB1Ebtw0LeOv5Ssen_o9HV2DSOPlOuN3MPETaApOIKayoQWcbqbtZFOhTknUUf2YkyllHoUKWoXRHWFBzaWSUZ1A3sXrI3-IQi2XP6DcrfQ1AvPDykv2eUb49OB4_X2uxFk_HX4D3yenyV5XzM0wngi579yVT63eMiba_QG2UEz5veIyZldQv1yltcJFqzgGWqaKIFZjd7f-yIjxvDgiYye2SWqqcyUWr790LSsJ3xhRpU1rv79FNmO3WxhCNi8YOafpTVpUZBVNeQldSzc_RqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«ایرباس موقت ایر فورس وان که توسط قطر اهدا شده، رنگ‌آمیزی شده و در نیویورک آماده است — درست همزمان با تعهد سرمایه‌گذاری ۱ میلیارد دلاری قطر که دیروز اعلام شد، بعد از آنچه برخی آن را تسلیم کامل آمریکا در برابر خواسته‌های قطر و ایران می‌دانند.»
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/15132" target="_blank">📅 10:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15131">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یديعوت احرونوت ادعا کرده بالای ۵۰درصد از پول‌های بلوکه شده ایران دست چین و عراقه
رقمش هم کم نیست؛ حداقل ۳۵میلیارد دلاره!
@withyashar</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/15131" target="_blank">📅 10:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15130">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خبرنگار اسرائیلی : این یک اشتباه تاریخی است.
پرداخت میلیاردها دلار به بزرگترین حامی دولتی تروریسم در جهان، فقط باعث تأمین مالی راکت‌های بیشتر، پهپاد‌های بیشتر و حملات بیشتری علیه اسرائیل و غرب خواهد شد. این سیاست «آمریکا در اولویت اول» نیست.
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/15130" target="_blank">📅 10:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15129">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c657925428.mp4?token=aat-EtukME0Nvj-M47dc7OZ3yUmjmm3WNZVTvGydl89MAXTiP0d01Vcyf1YgWQPqfxnsTGAzW69UlifVkyQw_MuUtKXnQDSJ5kXJBHR0ONZQk9L9C7L4lM8D0V8naFibrEtd9aC_031lWbC9poMzT7xg5SneHYhY4cW5cCnME5FL2eVl3tIkmJlGqePTEC1ikrfPBC9Ip-GR8Tu1Vs7ZAgiipLsA0VlYnhsFbmK-Dh-tk9wv4yonUcsFXvooYtWmxIPpzcPqsb6xjiuh4YPJXEymOGBbbQKPMVapZmxG29OMKRhqaHqZDLQ_Q2Oowy9YuS9TbCgWFfeU_TgHCnU8xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c657925428.mp4?token=aat-EtukME0Nvj-M47dc7OZ3yUmjmm3WNZVTvGydl89MAXTiP0d01Vcyf1YgWQPqfxnsTGAzW69UlifVkyQw_MuUtKXnQDSJ5kXJBHR0ONZQk9L9C7L4lM8D0V8naFibrEtd9aC_031lWbC9poMzT7xg5SneHYhY4cW5cCnME5FL2eVl3tIkmJlGqePTEC1ikrfPBC9Ip-GR8Tu1Vs7ZAgiipLsA0VlYnhsFbmK-Dh-tk9wv4yonUcsFXvooYtWmxIPpzcPqsb6xjiuh4YPJXEymOGBbbQKPMVapZmxG29OMKRhqaHqZDLQ_Q2Oowy9YuS9TbCgWFfeU_TgHCnU8xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک پنس، معاون سابق ترامپ: «به نظر من بهتر است به نیروهای مسلح ایالات متحده اجازه دهیم کار را تمام کنند، تنگه را باز کنند و قابلیت‌های تهاجمی ایرانیان را از بین ببریم و به مردم ایران فرصتی واقعی برای آزادی بدهیم.»
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/15129" target="_blank">📅 10:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15128">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">چند ساعت پیش، دونالد ترامپ با استناد به قانون تولید دفاعی (یک قانون از سال ۱۹۵۰ در دوران جنگ سرد)، دستور داد تا تولید مهمات، موشک‌ها و تجهیزات دفاعی آمریکا سریع‌تر شود. این فرمان در ۱۱ ژوئن به وزیر دفاع پیته هگست ارسال شد و مشکلات سیستمی در صنعت مهمات را هدف گرفت: ظرفیت تولید محدود، زنجیره‌های تأمین ضعیف، وابستگی‌های طولانی‌مدت و گلوگاه‌های تولید.
هدف اصلی: تسریع تولید مهمات حیاتی، موشک‌ها و تجهیزات دفاعی برای دفاع ملی آمریکا.
نحوه اجرا: قانون به ترامپ اجازه می‌دهد با شرکت‌های خصوصی توافق‌های داوطلبه ایجاد کند، تولید را اولویت‌دار کند و زنجیره‌های تأمین را تقویت نماید.
توافق مهم: شرکت لاکهید مارتین اعلام کرد با دولت آمریکا برای چهار برابر کردن تولید مهمات حیاتی به توافق رسیده است.
دلیل اقدام: کاهش ذخایر تسلیحاتی آمریکا پس از جنگ با ایران و استفاده از مهمات در ایران و ونزوئلا، که باعث افزایش سفارشات مهمات شد.
@withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/15128" target="_blank">📅 09:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15127">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdyhZgQADxwlQ0cib-NmlhtLz5KwklZ5eGyVA5k_-RiNTUwJN-XRvPR82uMOXtKJJwRMkY58kmXGDRgGyjic7g5G4Uq30_1oASE6Eso7fzxmLkPMFHE-ul-NXNXYr-3mMBN72GWjFIljfpAOy5F5ean6CAsa9VFqtPvGpt9d_t-bCNn66ML99F94eoHG0pldYcMly1dhaMQwuAJpT9c8JCPGyvIzjT9jscprT84u57pUmRxMU0K-CgIbYLMlblETvPwZWC_6szUVYtaehQnZeOWxtIskA30EFafCXK7FO93nAXfhJlo5SUdg7PAS5YpSOp7LBDPKgvILivECha7C8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">️ارتش اسرائیل اعلام کرد یک انبار تسلیحات جدید حزب‌الله حاوی ۵ تن مواد منفجره و ده‌ها پهپاد انتحاری را کشف کرده است
@withyashar</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/15127" target="_blank">📅 09:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15126">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer"><a href="https://t.me/withyashar/15126" target="_blank">📅 09:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15125">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تنکر ترکرز: ۳.۸ میلیون بشکه نفت خام ایران از محاصره آمریکا عبور کرد   تارنمای تنکر ترکز بامداد چهارشنبه گزارش داد، دو ابرنفتکش ایران که مجموعا حامل ۳.۸ میلیون بشکه نفت خام هستند، از محاصره آمریکا عبور کردند @withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/15125" target="_blank">📅 09:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15124">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خبرنگار العربیه: جنگنده‌های اسرائیلی دو بار به شهرک‌های «انصاریه» و «المنصوره» در جنوب لبنان حمله کردند.
@withyashar</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/15124" target="_blank">📅 09:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15123">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بلومبرگ: به گفته مقامات آمریکایی، معافیت فروش نفت ایران فقط شامل محموله‌های نفتی می‌شود که قبلاً بارگیری شده است و شامل مجوز گسترده‌تر برای از سرگیری فروش نفت ایران نمی‌شود @withyashar</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/15123" target="_blank">📅 08:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15122">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer"><a href="https://t.me/withyashar/15122" target="_blank">📅 08:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15121">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل، با بازنشر گزارشی از شبکه 14 اسرائیل درباره کشتار دی‌ماه، در ایکس نوشت:
«قربانیان سرکوب در ایران و خانواده‌های آن‌ها شایسته حقیقت، شفافیت و پاسخگویی هستند. جامعه بین‌المللی نباید در برابر این وضعیت بی‌تفاوت بماند.»
او گفت: «تاریخ حکومت ایران با رنج مردم خود نوشته شده است؛ اتاق‌های شکنجه، گورهای دسته‌جمعی، ناپدیدسازی اجباری و خانواده‌هایی که بدون پاسخ رها شده‌اند.»
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/15121" target="_blank">📅 08:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15120">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">منابع عربی: اسرائیل حومۀ شهرک نبطیه‌الفوقا در جنوب لبنان را هدف حملات قرار داد
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/15120" target="_blank">📅 08:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15119">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وبسایت خبری سمافور: مارکو روبیو، وزیر خارجه دولت ترامپ با انعقاد یادداشت تفاهم نامه با ایران مخالفت کرده و هیچ اظهار نظری درباره رسیدن به توافق با ایران نمی‌کند.
وزیر خارجه آمریکا امیدی به رسیدن به توافق هسته‌ای در مذاکرات با ایران پس از امضای یادداشت تفاهم نامه ندارد و تاکنون درباره امضای یادداشت تفاهم نامه با ایران کاملاً سکوت کرده است
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/15119" target="_blank">📅 08:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15118">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsbWCh9Htmms4qPFPX1E89XQIfm9k3tvHY2QeQxYY9spqaBz50y-HCjKotg3X3PpFPsWApPqHA4VYuxSxmD58TGjoYm6XTKEQEbz4nYj16GORNFlMoxoF84f-OjnmI2cf3B0w7AolMYABVwTTKpJnAclOdDyFj-gMcN0lwkSE4oq7ki5InXt02Uu_SqUGhDmDeowp6qbvheocevdwSd7tuZHYW-GR1pZHdIXlBLj12vFpY6IW9XxvM3QlRERhTranzG6l0Gee8ocxMTSVKFXcno8wqHr7yz9j18vgyAt_Un8KeNmWSus0lNvcqxem3dGcHR7tvlZMVWXElyvoWTxrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: به گفته مقامات آمریکایی، معافیت فروش نفت ایران فقط شامل محموله‌های نفتی می‌شود که قبلاً بارگیری شده است و شامل مجوز گسترده‌تر برای از سرگیری فروش نفت ایران نمی‌شود
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/15118" target="_blank">📅 08:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15117">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lx7G5aTyqm2QPrwGxICNtG3gZIU5cGwOZ_vT11zS9OVe0z8IZaE_tB7W46Y1RWsNfJ7JVlLROguYUTzW9x3MCHW_vJkeumQ0SDfJWh_0OilD6f9vyQFGHfz-FusujdnGMXoXKlad1405PHXih_UUhvhaDDsJWXeZR06BuC28RdY0_D9KZUxSLmnjlszM66dj4JDC0575Nk4C4QikaN4wXRWDjlGnxy9Px8D6YmLsr7IlcgQ99PvvzvfmLZ0jNQd_CW7gMJBiloQ4Qmp0g22AYDYJs_IomylThyCnB9zHfKeUScfyHd7Uq_uyIxt8WdJOVXzTnNB0TLKFkYVPmqoypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید:
«نه سلاح هسته‌ای، نه لغو کامل تحریم‌ها, نه پول»
@withyashar</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/15117" target="_blank">📅 08:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15116">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
اگه میخوای بدونی قیمت دلار طلا خودرو .... درسال جدید چقدر میشه این چنل تمام پیشبینی ها همراه تاریخ وقوع رو گفته
🕯
@link
🕯
🕯
@link
🕯
🕯
@link
🕯</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/15116" target="_blank">📅 02:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15115">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESsks1WmWECGYyrXkoyFrxHdGoHNMn1dE-NCMdnzmcBuU2RdBJhtJKQvOCUmqblrR0W6PB3RGpphQ6bvZafVkUaj-8QVe2xkbiDc6ETivRN1PuFZdsCcr62naoiu9umYj9lf3QlC6zqhpkqCXW4qMKC_kccQU-wszoLb8dR_yPagu33M_7UNcWK9n3gHQh6hO9yqKWCGjSP63ODBrhzRjm3yA7NotYW5UcomXs7D4fXX6e4ancEhqTO_PhMT9XJagPD7o99vVDL8ag881FUzeQwoT7jJJRoUHhivqEuPreWq01F3nom3N-XKsW2ey0fRR0jlutTt_EhkfkQq-P9QlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین  الان ، چه خبره خلیج فارس
@withyashar</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/15115" target="_blank">📅 02:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15114">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سنا با محدودکردن اختیارات جنگی ترامپ در قبال ایران مخالفت کرد.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/15114" target="_blank">📅 02:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15113">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95de30e10e.mp4?token=R6pNZI8HoHEc1ti_ga6SecZjNTjgB1MQasDLLhy18KJh1LJtz_sereBeHHYjFMihwv1k5PahxzIz_J4i_-p_7laHqQ4m9AdlpBkNyu-rUdNRl6GdTMXFsEzDtDlRPsKMAzE3M7o0bkS1gZfMk2mWB2gD4kNTHy-s5pwIVQspA8NQLb4K7nrmB9k7O-34_4HwMQajDNvql90Er5u3Hck9SaVFiiP4-8j_jqfhnJp82VIN8rIVF2RR3kPMs9afT3RrTgQNAiU5JacoAMHWP81VKv3lbtyt09GBbAQTS5F6hUVraGnI92qG9IFdI-0bT1k1bspaJZ7nK_NylRRNVeV1hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95de30e10e.mp4?token=R6pNZI8HoHEc1ti_ga6SecZjNTjgB1MQasDLLhy18KJh1LJtz_sereBeHHYjFMihwv1k5PahxzIz_J4i_-p_7laHqQ4m9AdlpBkNyu-rUdNRl6GdTMXFsEzDtDlRPsKMAzE3M7o0bkS1gZfMk2mWB2gD4kNTHy-s5pwIVQspA8NQLb4K7nrmB9k7O-34_4HwMQajDNvql90Er5u3Hck9SaVFiiP4-8j_jqfhnJp82VIN8rIVF2RR3kPMs9afT3RrTgQNAiU5JacoAMHWP81VKv3lbtyt09GBbAQTS5F6hUVraGnI92qG9IFdI-0bT1k1bspaJZ7nK_NylRRNVeV1hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس : اگه دونالد ترامپ حتی به عنوان رهبر معظم انقلاب در ایران هم انتخاب می‌شد، دموکرات‌ها باز هم می‌گفتن آمریکا شکست خورده
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/15113" target="_blank">📅 00:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15112">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23735193e5.mp4?token=IaqAVYGhCO8zULZsVqAd8r8Rppu9JJN3WRv5ykQ2-r2JSb37JWxN-2iQpT4LxdiT4yEvA0tx7Vr15bXn8pg4sCMTDR_VmXI5G76Lxc_k5smzmMax7bIqlj2obC_-rhQ6eLZ4NKKyH4UMoIarILzZKyrlt--qx2y-bQoseDtmXDaZIUQ84Bf9_f0wy6Qow0cIY8Ts1Mit64XrbJSdBbfC8tJXDDwTdCGH5OzY0zTY0GRu6DsO10eykvslcFLlT059_r56wOXLjBZl2q9Q38RqF6MHecupEeyz_smoSrdwm5nCNWonHRuVXAXGNbS5ilPp_WR913D9Pk-h5ss2n4oDNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23735193e5.mp4?token=IaqAVYGhCO8zULZsVqAd8r8Rppu9JJN3WRv5ykQ2-r2JSb37JWxN-2iQpT4LxdiT4yEvA0tx7Vr15bXn8pg4sCMTDR_VmXI5G76Lxc_k5smzmMax7bIqlj2obC_-rhQ6eLZ4NKKyH4UMoIarILzZKyrlt--qx2y-bQoseDtmXDaZIUQ84Bf9_f0wy6Qow0cIY8Ts1Mit64XrbJSdBbfC8tJXDDwTdCGH5OzY0zTY0GRu6DsO10eykvslcFLlT059_r56wOXLjBZl2q9Q38RqF6MHecupEeyz_smoSrdwm5nCNWonHRuVXAXGNbS5ilPp_WR913D9Pk-h5ss2n4oDNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور جی دی ونس:
پرزیدنت ترامپ هرگز نگفت که هدفش نصب رضا پهلوی برای تبدیل شدن به رهبر جدید ایران است.
آنچه گفته این است که اگر مردم ایران بخواهند قیام کنند ، عالی است. این کار اوناست این بین آنها و دولتشان است.
چیزی که ما می خواهیم توقف برنامه هسته ای آنهاست.‌‌
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/15112" target="_blank">📅 00:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15111">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f65655673.mp4?token=DZl7X72wMWRtLmeBgGuSag1D5daFqzBuysswJCtjg-ebc6HDyj4FHZ_-gaIg5d-FCMKxfGtfXJKVENN18J1icqmr7JygcqIV12yvCM_uyiHctDKyodoEgaN93C95dzULGaSMG5LuJF3phtvge6qYGEr94O-ZqEAfxVM-cibLr2mSz7U7aDNA6obRClmnXn3CapUu3DsKI5pJlIpQnXrqV3zRxD1F0Q6ljM8mXBTUTVgC8yMsZGdS9kcqgQEgPzjUwAFE6XuJEFIWl1bEtimo20umr0oUCpT42hzctXNzwQj9N9WcE2YIcSY8RzRxmIthf8kskGwl28dbmXI9t8r0bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f65655673.mp4?token=DZl7X72wMWRtLmeBgGuSag1D5daFqzBuysswJCtjg-ebc6HDyj4FHZ_-gaIg5d-FCMKxfGtfXJKVENN18J1icqmr7JygcqIV12yvCM_uyiHctDKyodoEgaN93C95dzULGaSMG5LuJF3phtvge6qYGEr94O-ZqEAfxVM-cibLr2mSz7U7aDNA6obRClmnXn3CapUu3DsKI5pJlIpQnXrqV3zRxD1F0Q6ljM8mXBTUTVgC8yMsZGdS9kcqgQEgPzjUwAFE6XuJEFIWl1bEtimo20umr0oUCpT42hzctXNzwQj9N9WcE2YIcSY8RzRxmIthf8kskGwl28dbmXI9t8r0bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور در به در دنبال  دکتر خوش چشم هستم که او را به صنعت فوتبال وارد کنم
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/15111" target="_blank">📅 00:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15110">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">همکنون
انفجار های مهیب در جنوب لبنان،
گزارش های محلی از شلیک گسترده تانک های اسرائیلی و درگیری شدید با نیرو های حزب الله در تلاش برای پیشروی در جنوب لبنان.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/15110" target="_blank">📅 00:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15109">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اورشلیم پست: ماهواره‌های اسرائیلی در طول حدود ۴۰ روز اجرای عملیات «غرش شیران» بیش از ۵۰ هزار بار از ایران تصویربرداری کردند
میانگین هر روز بیش از هزار تصویربرداری
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/15109" target="_blank">📅 00:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15108">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">جی‌دی ونس: برخی خواهان اعزام صدها هزار نیروی آمریکایی به ایران هستند
ترامپ جورج بوش نیست؛ در باتلاق ایران گرفتار نمی‌شویم
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/15108" target="_blank">📅 00:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15107">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">واکنش آمیت سیگال خبرنگار کانال 12 اسرائیل به توافق ترامپ:
ممکنه دشمنی با آمریکا خطرناک باشه، اما دوستی با آمریکا مرگباره!
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/15107" target="_blank">📅 00:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15105">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کانال ۱۳ اسرائیل: ترامپ مانع اجرای یک عملیات نظامی‌برنامه‌ریزی‌شده اسرائیل در غزه شد
این طرح در بالاترین سطوح سیاسی و امنیتی اسرائیل بررسی شده بود، اما پس از ارائه جزئیات به آمریکا، واشنگتن با آن مخالفت کرده و خواستار عدم اجرای آن در شرایط فعلی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/15105" target="_blank">📅 23:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15103">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">با این جماعت چه کنم
😞</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/15103" target="_blank">📅 23:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15102">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArtin</strong></div>
<div class="tg-text">اسکل عقده ای یه پیام رو جواب نمیدی
عقده ای هستی زیاددد</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/15102" target="_blank">📅 23:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15101">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شاهزاده رضا پهلوی به نیوزنیشن: مردم ایران اکنون میگویند چرا بمباران متوقف شد؟ ایالات متحده باید بمباران ایران را ادامه میداد
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/15101" target="_blank">📅 23:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15100">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گزارش حملات پهپادی سپاه پاسداران به اربیل عراق
🚨
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/15100" target="_blank">📅 22:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15099">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">به گزارش ان‌بی‌سی نیوز، کارشناسان ارشد صنعت نفت هشدار می‌دهند که علیرغم فضای مثبت ناشی از توافق میان ایالات متحده و ایران برای پایان دادن به جنگ چندماهه در خاورمیانه، بازگشت بازارهای نفت به حالت عادی و از سرگیری تردد در تنگه هرمز فرآیندی زمان‌بر است و احتمالاً چندین هفته به طول خواهد انجامید.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/15099" target="_blank">📅 22:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15098">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwQRFi-SPCZsVkuf4sEbPPC9wx8l5Ml5Ex8DH2ISzV6tJ63HA46RX9MtBQKsd2pCFw2XToviJA8pJUlMIUrrBOn4pnnJH1B7lDp82cAYWLOUam5u-xiJEGAeuZ5iTknNw8SutizwEu3t0tX0VP3dwPrGvL9tuc83UIGPLu0XrkhkYNNJjzUrNgD6TIfoSrOu67By_HUN1U3xoT5lOWn3Ou0BFqhIZaPLxNWZTiFDzg08pl1YFSU2mwMh3kb0XugQ1v10fGnB5_ibvgXeP8Ls5D1A6xdwjsRhXyRxR1_tL6G5NJc7KYIfX23gJ5TBHyLLMBKddvYUBR0rNgIiftzQBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پایگاه موشکی دیگر در شامل شش ورودی زیرزمینی، در حال ساخت است. یکی از دلایل احداث ورودی‌های بیشتر، قرارگیری این پایگاه در ناحیه‌ای استراتژیک از ایران می‌باشد
بخشی از فرایند ساخت پایگاه مذکور، پس از جنگ 12 روزه صورت گرفته است، هم‌چنین برخی از سازه‌های روزمینی این پایگاه در دو جنگ اخیر هدف قرار گرفته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/15098" target="_blank">📅 22:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15097">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b21de6065.mp4?token=YxkvQNRb9tai3mw-ETFv25tVHRIDcph7YvCLbk9ry8LkSIVYT2jcww6AqRxdCZSilefxgWpfIyl3AfoNCUAsh7nlSfJLU-68m7eQVeZDQcjulXqXyvrvSzfInLsLrjZEoryY-7ZI4KZPltT7uLU_vxk0XjZFAc3U6pnMUfj6n7duANAI-Cj2gHM6XDYwBpPQTtG5m3u0qB1SwGw-EWk0OXgG9-L82NQ7WoQUyv835QbruzsemZwPB0HgdTb2Z3bRfYDa6ihhzyflGJ2QPMladwoVMhHdO5Ss-KkJaEFfRfXdIekwhqhSLppTQwr7aNgOjhn-rgIStfCADCm7U4hOww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b21de6065.mp4?token=YxkvQNRb9tai3mw-ETFv25tVHRIDcph7YvCLbk9ry8LkSIVYT2jcww6AqRxdCZSilefxgWpfIyl3AfoNCUAsh7nlSfJLU-68m7eQVeZDQcjulXqXyvrvSzfInLsLrjZEoryY-7ZI4KZPltT7uLU_vxk0XjZFAc3U6pnMUfj6n7duANAI-Cj2gHM6XDYwBpPQTtG5m3u0qB1SwGw-EWk0OXgG9-L82NQ7WoQUyv835QbruzsemZwPB0HgdTb2Z3bRfYDa6ihhzyflGJ2QPMladwoVMhHdO5Ss-KkJaEFfRfXdIekwhqhSLppTQwr7aNgOjhn-rgIStfCADCm7U4hOww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدئو احمدی‌نژاد بعد از توافق
@withyashar</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/15097" target="_blank">📅 22:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15096">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68844ebd5c.mp4?token=GVuqIC2Utpy03P7Gu18UsYXu3yNsDUr06RBLP7ncOvWGo1KYEYkYB9kYmt3GlmtD81-O0X0ZLO9CvOOQC7RxluTl-W6Atdu1Thb2ZXERd_TtyuF66-Bi3B3sn6Y5GN3gqfZ9SKTEdbsNdEhIzlwByOr9jYm3xig0L1LI7PdfbSA2986DsmP2oyQGNPJHTneBnq5mr2Cwz1J8PQmxBOITEwDrlRXI0fF-mxoL-rFbxudAvREG5ODO9lyBhGeIYKieoGSUhxZrNALqdAUYHaFp3UfkgyE8UGeA4PkF8ZzsfEQjO899QCPK6HcznuAn8dF5IWOngCA5V5riEaAqNX8llg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68844ebd5c.mp4?token=GVuqIC2Utpy03P7Gu18UsYXu3yNsDUr06RBLP7ncOvWGo1KYEYkYB9kYmt3GlmtD81-O0X0ZLO9CvOOQC7RxluTl-W6Atdu1Thb2ZXERd_TtyuF66-Bi3B3sn6Y5GN3gqfZ9SKTEdbsNdEhIzlwByOr9jYm3xig0L1LI7PdfbSA2986DsmP2oyQGNPJHTneBnq5mr2Cwz1J8PQmxBOITEwDrlRXI0fF-mxoL-rFbxudAvREG5ODO9lyBhGeIYKieoGSUhxZrNALqdAUYHaFp3UfkgyE8UGeA4PkF8ZzsfEQjO899QCPK6HcznuAn8dF5IWOngCA5V5riEaAqNX8llg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد اینهمه شب تو خیابون رفتن، آخرش بهت میگن اقلیتی تندرو
🤣
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/15096" target="_blank">📅 22:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15095">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا:
اسرائیل تو دو روز گذشته پس از اعلام پایان جنگ توسط رئیس ترامپ، 84 بار آتش بس تو جنوب لبنان رو نقض کرده و همچنان به جنایات و کشتار مردم لبنان ادامه میده.
هشدار میدیدم اگر اسرائیل به شرارت‌هاش ادامه بده، باید منتظر پاسخ سخت نیروهای مسلح جمهوری اسلامی ایران باشه.
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/15095" target="_blank">📅 22:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15094">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی: در صورت بدعهدی آمریکا، پاسخ  ایران، نظامی و کوبنده خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/15094" target="_blank">📅 22:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15093">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/15093" target="_blank">📅 22:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15092">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">12 بند توافق ایران و امریکا به گفته باراک راوید خبرنگار ‌آکسیوس :
-ایران، ایالات متحده و متحدانشان خصومت‌ها را متوقف خواهند کرد، از جمله در لبنان. ایران تعهد خود را به عدم توسعه یا دستیابی به سلاح‌های هسته‌ای مجدداً تأکید می‌کند.
-ایالات متحده و ایران متعهد می‌شوند مسئله دفع ذخایر اورانیوم غنی‌شده ایران را حل کنند.
-ایالات متحده و ایران درباره غنی‌سازی اورانیوم و نیازهای انرژی هسته‌ای غیرنظامی ایران گفتگو خواهند کرد.
-ایران وضعیت موجود برنامه هسته‌ای خود را در طول مدت مذاکرات حفظ خواهد کرد.
-ایالات متحده محاصره دریایی را برمی‌دارد، از تحمیل تحریم‌های جدید خودداری می‌کند و در طول مذاکرات حضور نظامی خود در منطقه را افزایش نخواهد داد.
-ایران ترتیبات لازم را برای تضمین عبور ایمن کشتی‌های تجاری از تنگه هرمز، بدون هزینه، به مدت ۶۰ روز فراهم خواهد کرد.
-ایالات متحده متعهد می‌شود دارایی‌های منجمد شده ایران را پس از اجرای تفاهم‌نامه در دسترس قرار دهد.
-اگر توافق نهایی حاصل شود، ایالات متحده نیروهای خود را ظرف ۳۰ روز خارج کرده و تمام تحریم‌ها علیه ایران را لغو خواهد کرد.
-هر توافق نهایی شامل برنامه‌ای برای ایجاد صندوق ۳۰۰ میلیارد دلاری برای بازسازی ایران خواهد بود. ایالات متحده به ایران معافیت‌های موقتی تحریمی برای اجازه فروش نفت در دوره مذاکرات اعطا خواهد کرد.
-مذاکرات بین ایران و عمان با مشارکت کشورهای خلیج فارس برگزار خواهد شد تا ترتیبات مربوط به حمل و نقل و خدمات دریایی تعیین شود.
@withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/15092" target="_blank">📅 21:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15091">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نفتالی بنت(نامزد نخست وزیری اسرائیل) در پخش زنده خطاب به جمهوری اسلامی: باور دارم به زودی یه دولت جدید در اسرائیل میاد و امیدوارم من رهبری اون دولت رو به دست بگیرم. از همینجا به رژیم ایران میگم؛ من قراره بدترین کابوس شما باشم، تاوقتی مردم ایران رو از دست شما…</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/15091" target="_blank">📅 21:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15090">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شبکه خبر: تمام کسایی که توی بیت رهبری بودن کشته شدن جز مجتبی خامنه‌ای @withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/15090" target="_blank">📅 21:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15089">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شبکه خبر: تمام کسایی که توی بیت رهبری بودن کشته شدن جز مجتبی خامنه‌ای
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/15089" target="_blank">📅 21:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15088">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b67afa5b.mp4?token=bp2KBEE_jso-flzjOi-tGIAFbSPLaRgQkZi0WpCt6GwCU2GiQfqcEPTl0DVK-ismMJ6f-Fc3BS5rUGCZUVZ_tUSCXv4YOaWnqpk8kijmYbHKQWp-ZjJpvc6taymNrUSUxKQ0aQxXhf8nTmmkGePU5t-ZtDKOijGDNENXNBSaK-pCwTMJ6aRBVM5HhiaUPcIjk3zj3rEz_vAjClLudiZmmrIWMI-I8gnvMR-dSnOFAIzNjxxT2F6O6fX7fkiaPaR8uP65jU_TZESJGl4PgHhfJn2uTwnCU93iq0x1VEsp2zj5ZqFvt9bUgMJvQ3bC4AZYOzSl2C6i0w9ZF7-ZndeqDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b67afa5b.mp4?token=bp2KBEE_jso-flzjOi-tGIAFbSPLaRgQkZi0WpCt6GwCU2GiQfqcEPTl0DVK-ismMJ6f-Fc3BS5rUGCZUVZ_tUSCXv4YOaWnqpk8kijmYbHKQWp-ZjJpvc6taymNrUSUxKQ0aQxXhf8nTmmkGePU5t-ZtDKOijGDNENXNBSaK-pCwTMJ6aRBVM5HhiaUPcIjk3zj3rEz_vAjClLudiZmmrIWMI-I8gnvMR-dSnOFAIzNjxxT2F6O6fX7fkiaPaR8uP65jU_TZESJGl4PgHhfJn2uTwnCU93iq0x1VEsp2zj5ZqFvt9bUgMJvQ3bC4AZYOzSl2C6i0w9ZF7-ZndeqDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت(نامزد نخست وزیری اسرائیل) در پخش زنده خطاب به جمهوری اسلامی:
باور دارم به زودی یه دولت جدید در اسرائیل میاد و امیدوارم من رهبری اون دولت رو به دست بگیرم.
از همینجا به رژیم ایران میگم؛ من قراره بدترین کابوس شما باشم، تاوقتی مردم ایران رو از دست شما آزاد نکنم دست بردار نیستم.
@withyashar</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/15088" target="_blank">📅 21:45 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
