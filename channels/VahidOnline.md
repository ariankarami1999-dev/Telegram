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
<img src="https://cdn1.telesco.pe/file/L-ONBxCTRyobFDLFoC6q-rKxjaxKEJWd1qQPrSrDPf6Z7L7elDrqR8VOZFFEIML2WacOMqwlgstjrDLoXyj_MJcbhU2urfub0HgF8grqwgz8wpbYxv8YrtPjndcB8zrUhaYpkaGgj64nTaScF1UuCAUEwnsNbuvS0PTaG3W5ANLGLzt16fEWaCPajERxCSBY3zyk1PGicYS8CQQx-KGscH7X7iCrZr9e7N8dk4pcRvkjV6JzPLWjiZ42FDH2Fv0BV--IBiivNl4BC_zEi_4msag_8RO3FPVTBZ_TJzpS1TKA9e-gsslzKZE-Fz_D6Rpayjz-kf6ataKGV2Cnx2VNxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.33M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 17:08:24</div>
<hr>

<div class="tg-post" id="msg-75939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSnXCbUu0GyBDnR56gYBzPbeNK77seVPCv2044CLqG3cfcv16WqWJCRD2R13pcb_1fWvKMcSK2gHG2gqVkkOiYgFJqDdkgr7TzD25BCGcSGuPvZXWY4NB535kyCC0o9AwghYqjVbMEGkW0xyYZ2k_ECTifYY4prTULWJAq_7rnrb7TLJnXh2Kn_HDFI3JHNGjw26VCru4yyQOJ8ifocMiKYL7CurVBPizyy_0vOkn_mudWk2Rx4E3zk-Y3HT6VMaBtlZ4Dxgg6BwQN7Ad3vaQtaiYFcoYnAvKqw8Qfk_AIIg8izJyN6Bomaksb9J2K0nKe5s9T2xa_D1cl89weXgCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نعیم قاسم، دبیرکل حزب‌الله لبنان: مذاکرات مستقیم لبنان با اسرائیل نمایشی مضحک و توهین‌آمیز است
♦️
نعیم قاسم، دبیرکل حزب‌الله لبنان، توافق دولت لبنان با اسرائیل که با میانجی‌گری آمریکا تدوین شده است را «تسلیم و شکست تمام‌عیار» توصیف کرد و گفت حزب‌الله تنها به توقف کامل حملات، آتش‌بس و خروج اسرائیل از خاک لبنان متعهد است.
او همچنین خلع سلاح حزب‌الله را به معنای از بین رفتن قدرت لبنان دانست و تاکید کرد این موضوع برای حزب‌الله قابل پذیرش نیست.
پس از توافق آتش‌بس میان اسرائیل و حزب‌الله لبنان، آمریکا برای حل‌وفصل اختلافات مرزی و مسائل امنیتی میان دو طرف نقش میانجی را بر عهده گرفته است. در همین حال، موضوع خلع سلاح حزب‌الله و نحوه اجرای آتش‌بس همچنان از مهم‌ترین محورهای اختلاف میان دولت لبنان، حزب‌الله و اسرائیل به شمار می‌رود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/VahidOnline/75939" target="_blank">📅 16:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NNG6cWU70R2p2RGikqaZvFWoFYyOhbbhqfn-BUAs2cfPSoXbkcMjrlGKzhXpzI52p0dU0Xgm9cTYFrMBPJUUfUCMElxiv-3kJ6ZHDBPVF_x7OtLl1syJYLPnFR498ffcDno5WZxyx_luN3KoRw7ChjnkQCbosiKmSVl7655WTKfgj__2f0UyVlshXyJhNWa_RikprNoyL5tCE6-7n8gchAslXF2HmXF-JtD0iEcGQwuk5Wq-TuExgjZbEjT2pfWB__OzFY-5jAuoVuNVrGn3wEo-02L1bF8SxnyfFIha_o0yTei50spWQ0o0epaU89z9MuA3mh1SJDhRqZ25_VHuJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران روز پنجشنبه ۱۴ خردادماه و ساعاتی پس از انتشار ویدیوها و تصاویری از برخورد پهپاد سپاه به فرودگاه بین‌المللی کویت، به نقل از یک منبع نظامی، آن‌ها را «تصویرسازی دروغین دشمن» خواند.
این منبع نظامی به تسنیم گفت:‌«پرتاب پهپادهای هوافضای سپاه به سوی اهداف آمریکایی در کویت، در نیمه شب و اصابت هم در نیمه شب (و در تاریکی هوا) صورت گرفته است درحالی که در فیلم و عکسهای ادعایی که از پهپاد در فرودگاه منتشر شده، هوا کاملاً روشن و مربوط به روز است.»
سپاه پاسداران پیش از انتشار تصاویر برخورد پهپاد با پایانه مسافربری شماره ۱ فرودگاه کویت ادعا کرده بود که موشک‌های سامانه ضدهوایی آمریکا به این محل برخورد کرده بودند.
این منبع نظامی که نامش فاش نشده به تسنیم گفت:‌ «فاصله «هدف» پهپادهای هوافضای سپاه تا فرودگاه کویت بیش از ۴۰ کیلومتر است و این نیز نشان می‌دهد که اصابت به فرودگاه کویت ارتباطی به پهپادهای ایران ندارد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/VahidOnline/75938" target="_blank">📅 16:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75937">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/deQ3uGLInXjoGnHndg1u4wgYv4Oy6k5fbSIIRZlhnGSZbhIRXtB4_PA0NucRa6kuVK026V34FpLG-2sYNacPqOMXhmX0D1_Q8VQ01sppcjCk8pxdIvya9gcYU_F_AN9esw6fdHC4S8_ThRR7UQlASeZTjpeDMN2MJdAJ-5lwKUo_NAqWC3ZjQTrmzYh4Z448xZbiFQTwI64Lu4jtxJkFuyENXSHGokex8V8A8BfrOy2a2GpRRgaHWamt6FCEMCU_jOX3gEhvfc9T5PqteL6F4ipSHok_Izbl6c6IBGjNwKzC8JWX6NIKrMJLFzEzVnzFnTTdQFkgZkiPVuz7SM_gRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام مکتوب و منسوب به مجتبی خامنه‌ای، سومین رهبر جمهوری اسلامی، در مراسم سالگرد مرگ روح‌الله خمینی در تهران، خوانده شد.
در این پیام که محمدجواد حاج‌علی‌اکبری، امام جمعه تهران، روز پنجشنبه ۱۴خرداد خواند، رهبر جمهوری اسلامی‌ آمریکا و اسرائیل را به «جنگ ترکیبی» با ایران متهم کرد و گفت این جنگ «بر دو نقطه متمرکز است؛ یکی تاب‌آوری مردم و دیگری ایجاد اخلال در دستگاه محاسباتی مسئولان کشور».
مجتبی خامنه‌ای همچنین هرگونه اقدامی که به‌گفتهٔ او «موجب بدبینی و سرخوردگی» شود را «کمک به دشمن» خواند و خواستار «حفظ وحدت و انسجام و اعتماد متقابل» مردم و مسئولان نظام شد.
مجتبی خامنه‌ای هفتهٔ گذشته نیز به تمام کسانی که آن‌ها را «جان‌فدایانی که دل‌شان برای اسلام و انقلاب یا استقلال و سربلندی ایران می‌تپد» نامیده، هشدار داده بود که «اختلافات غیرموجه و حتی موجه را به تنازع و تفرقه تبدیل نکنند».
در بخش دیگری از این پیام، اسرائیل «پادگانی متعلق به نظام سلطه» توصیف شده و تاکید شده است این کشور از هر اقدامی برای جلوگیری از پیشرفت ایران کوتاهی نمی‌کند.
این پیام همچنین اعلام کرده است: «دشمن خبیث در مصاف با فرزندان دلاور شما در نیروهای مسلح دچار شکست شده است» و افزوده است دشمن پس از آنچه «تحقیری پرمعنا و عمیق» خوانده شده، تمرکز خود را بر تضعیف تاب‌آوری مردم و ایجاد خطا در دستگاه محاسباتی مسئولان قرار داده است.
در پایان، در این پیام از همگان خواسته شده است با ایستادگی، روشن‌بینی، حفظ وحدت و انسجام و همصدایی نکردن با دشمن، «نقشه شوم» او را خنثی کنند.
از زمان اعلام نام مجتبی خامنه‌ای، به عنوان سومین رهبر جمهوری اسلامی، تصویر یا صدایی از او منتشر نشده و رسانه‌های ایران فقط پیام‌های کتبی از او منتشر می‌کنند.
مراسم سالگرد مرگ روح‌الله خمینی که هر سال ۱۴ خرداد با سخنرانی رهبر جمهوری اسلامی و با حضور پرشمار مقامات و فرماندهان ارشد نظامی برگزار می‌شد، امسال به‌صورت خیلی محدود و بدون حضور مقامات نظام برگزار شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/VahidOnline/75937" target="_blank">📅 16:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TovUDbG5NGCljVEeiyEbt5fvrenHdHOEzuY5KdWtfGjeDad7GFEQcNWSO-4Rdveq8w-xDaQSKOna0uYBNxeyfK0dnjfTp8URxwfRcn4R-4U0iMA9BnYeJqV2RhSnWgdVtEgdvWxOaX00tu2DPBGTNfr_9wEm7KnjdKZiZ2CopNQXfczPOcQ4IgcuAMO6svrOQjn00cg2LEUnDUmP1v7sO4EZZq3OzD3XzEWA1yyDdIvs9DcSVvdePZy4FynG68263FCPRBt3V35B_3ItAAiW1Jbfen58MBITRcBNsNfiW2fxsDzahJExaLLwAY726MI05O_BxahaZ-9eSgJaOKWjdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ، رئیس جمهوری آمریکای روز پنجشنبه ۱۴ خردادماه از تصویب قطعنامه «پایان جنگ ترامپ با ایران» به‌شدت انتقاد کرد.
رئیس جمهوری آمریکا در این پیام نوشت:‌ «دیروز، در یک رای‌گیری بی‌معنی، مجلس نمایندگان، چهار جمهوریخواه بد و تمام دموکرات‌ها، درست در میانه مذاکرات نهایی من برای پایان دادن به جنگ با جمهوری اسلامی ایران، به محدود کردن اختیارات جنگی من رای دادند. چه کسی چنین کار غیرمیهن‌پرستانه‌ای انجام می‌دهد؟ آنها می‌دانند مذاکرات در چه مرحله‌ای است.»
ترامپ با انتقاد تند از نمایندگان حامی این طرح نوشت: «دموکرات‌ها از سندرم اختلال روانی [بیماری مخالفت] ترامپ تغذیه می‌شوند. آنها ترجیح می‌دهند کشورمان شکست بخورد تا اینکه به من یک پیروزی دیگر، از پیروزی‌های بسیار، بدهند. چهار نماینده جمهوریخواه، داستان آن‌ها کاملا متفاوت است. آن‌ها خودنما هستند! آن‌ها باید از خودشان خجالت بکشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/VahidOnline/75936" target="_blank">📅 16:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b2qa6yutjdtAVd4444DLCR1aaES1-HrrnzRDWR-fetuzMBXLKW17Cy0rh5cBgz2nrlfqBUUc4EMibDqJtBqZurzCOIOnPMQ4evMxapn0flP23zhoOF3OkB73nwGIxjFehOa7YJjUiHqDnqvGTmqYbiSRjP_lksMQoko99tuq9KXoxPkpX5YpSizx7cTxyX9vw6FsMn8oaZd6vHBdkYMEG7xoj6xKl8EU4ZNa12ieUDYgVpUMFUJsATNHh7EfsklL-XYvdpzTOmjw2mgUEfPfDc4ryY0VVw4PVkKJlIWO92VNgL1AL0y3vkdWVjNIAo3KTOi6piYerQMqsmWJiwjbDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی، نویسنده، تصویرگر و فیلمساز ایرانی-فرانسوی و خالق کتاب مصور «پرسپولیس»، در ۵۶ سالگی درگذشت.
به گزارش خبرگزاری فرانسه، نزدیکان ساتراپی اعلام کردند او «کمی بیش از یک سال پس از درگذشت ماتیاس ریپا، همسرش و عشق زندگی‌اش، از غم درگذشت.»
ساتراپی سال گذشته نشان لژیون دونور دولت فرانسه را در اعتراض به ریاکاری دولت فرانسه در قبال مردم ایران و جمهوری اسلامی رد کرد.
مرجان ساتراپی با انتشار «پرسپولیس»، کتابی مصور درباره زندگی خود در ایران و مهاجرت، به شهرت جهانی رسید. این اثر با استقبال گسترده مخاطبان روبه‌رو شد و به یکی از آثار شاخص ادبیات مصور معاصر تبدیل شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/VahidOnline/75935" target="_blank">📅 16:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75934">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K4Ad6sB8xSBbx4WDn6TBG5u5XhPfrQt29jPvkftgX5Vuar8m01kw00fEm2QzRpDnNciWrdP0fme0Z8JirbOxwXkLLTXxPx3PzbvoJN-v5dvM16u6AEXwMdJaQyBeMUgf7GPE3o0NM6VftWf09PLOhPxvOAqqTp4cWuZFH6JAb0bo9uBG8n7zhw9P_TgtKmoSe05bnZDAURiJDmlyse8qc6MJ4QhujB8jcDZKsZJAzCU-udVK0vNOWLwnDKDPxrfw6gBk2N7qw-i_R3u2wDZfTaENchy0RRFaFuUJBdLRUB7QRD2aqRWyQ9aWEtyJb6FYoyGh6XHvaZ0ksWpLU1rZXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هه‌نگاو و سازمان کوییرهای ایرانی سیمرغ با انتشار اطلاعیه‌هایی خبر کشته‌شدن مهشید فلاحی، زن ترنس، در سنندج را تکذیب کردند.
این سازمان‌ها ضمن عذرخواهی درباره انتشار این خبر نادرست، با وجود راستی‌آزمایی‌های قبلی، گفتند اسناد جدید نشان می‌دهد این شهروند زنده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/VahidOnline/75934" target="_blank">📅 16:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75933">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZK3bb9TP4dfiHzVOMZ3bl-G1MAcbO4d63CbCylKr3n7plb2oR0RmQ9r6S1cYQBghBI9fq1KUuKC9oyzAgJUBEhVjyTympHF_12eEJt6rw5xdy-naeBrbj5kqQonsVVwEQk-ouVVzp2HpCXf3rzwfdk2pmIlEAon8Nr51SQjJ-5BOz-BBAANuWgY-VDdNJrH9Ze_wHdmTZHT6q7EtE9OgyXxEJUUkrBEedwRoylzJAf2HQ92l32WUD6U2Iz2A4P8uP1MYsPwO_h13V4kU8RCTarlnYOHDN1L-TR2GA9ibXpfF1VKxw1VVbxufWsHPaPSaV5bnHMYmuLihhyDzaiCtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحدث گزارش داد آمریکا و جمهوری اسلامی به توافقی چهار مرحله‌ای نزدیک شده‌اند که با کاهش تنش‌ها آغاز می‌شود و به پرونده هسته‌ای و ترتیبات امنیتی منطقه ختم خواهد شد و انتقال از هر مرحله به مرحله بعدی، پس از «اجرای تعهدات» انجام می‌شود.
طبق این گزارش، مرحله نخست توافق شامل توقف عملیات نظامی مستقیم و پرهیز از هرگونه تشدید تنش یا گشودن جبهه‌های جدید در منطقه است. مرحله دوم نیز بر امنیت کشتیرانی، بازگشایی تنگه هرمز و ترتیبات امنیتی ویژه گذرگاه‌های دریایی و خطوط انرژی متمرکز است.
به نوشته الحدث، مرحله سوم این توافق شامل اعتمادسازی اقتصادی، کاهش محدود برخی تحریم‌های جمهوری اسلامی، آزادسازی بخشی از اموال مسدودشده ایران و ارائه تسهیلات مرتبط با صادرات نفت است.
بر اساس این گزارش، مرحله چهارم توافق پیچیده‌ترین مرحله به شمار می‌رود و ممکن است ماه‌ها طول بکشد. این مرحله شامل بررسی برنامه هسته‌ای ایران، سطح غنی‌سازی اورانیوم و سازوکارهای نظارتی و ترتیبات امنیتی منطقه‌ای است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/75933" target="_blank">📅 02:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75932">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/huHdFD3cViR196V8SxHOQ2JAyKqyZwHwqSI7v1CVtCyldSxYbATLmUMBngQj0wsJ0uJiEBBqj6QtaRjgEXcCYc-pzV2TrIq66G6X5CHU2vkuOdpITAE4ZkSQWmOzScvxZs1qkW48Z6yfsxzss_-ODFXRDBvT1LPtFKqvumLZBTZ4qdfgpiY3XvUeO6CBiQwUZdAs3082QKMZs5HcazpfshcSjijzDaQFMCv0X9NG_5Fca57YFxb9x9M-LHfcVJAiXQMrIoOp6wRYrncV7lCNpmzgK04_3ITEszH44s6mGC3_GOw6FEmTQFSgqRZoeDMoYBajREWPpNk7Gsnf0C2Hag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا اعلام کرد اسرائیل و لبنان بر سر اجرای یک آتش‌بس به توافق رسیده‌اند.
بر اساس بیانیه منتشر شده، اجرای این توافق «منوط به توقف کامل» حملات حزب‌الله و همچنین تحقق چند شرط دیگر است.
این توافق پس از آن اعلام شد که حملات اسرائیل به جنوب لبنان در روز چهارشنبه دست کم ۹ کشته بر جای گذاشت و حزب‌الله نیز راکت هایی را به سوی شمال اسرائیل شلیک کرد.
در بیانیه چهارشنبه شب وزارت خارجه آمریکا آمده است: «همه طرف‌ها بار دیگر تاکید کردند که آینده روابط میان اسرائیل و لبنان باید توسط دو دولت مستقل و حاکم تعیین شود. آنها هرگونه تلاش از سوی دولت‌ها یا بازیگران غیردولتی برای گروگان گرفتن آینده لبنان را رد کردند.»
حزب‌الله تاکنون به صورت رسمی درباره این توافق اظهار نظر نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/75932" target="_blank">📅 02:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75931">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a5b9c36ab1.mp4?token=s39QKn9eTOxmJd0nov2a63SS8ixThmC9rbK5llg2pN4McfKBNAP6jKuyWH5FsbZKPRSTOe3EcE9k1Jq0bmQyrf7LMLYavpFftosdX_UzofX14PN5bZGBM7i1U4lL2joePAg169m0uarElmzWIV0fvoOxiSaa6T9RgPZYuVhBbP-ZQj8bKaDrMcsSbA5-1SjkV-Rn57e4UPddg6fhqBFiHMLf2ADU3BHIcPYnuowbJ64LDohbI69eR4EH2ImOsK6Kwn3hCk_G-ufvAbTqaY5b2oNSVXRwWGQ-py2Ij3pK61IPaLuPVDw25sd6BFH-bxx4e18prc2mYfJ0g4PtFOIhEA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a5b9c36ab1.mp4?token=s39QKn9eTOxmJd0nov2a63SS8ixThmC9rbK5llg2pN4McfKBNAP6jKuyWH5FsbZKPRSTOe3EcE9k1Jq0bmQyrf7LMLYavpFftosdX_UzofX14PN5bZGBM7i1U4lL2joePAg169m0uarElmzWIV0fvoOxiSaa6T9RgPZYuVhBbP-ZQj8bKaDrMcsSbA5-1SjkV-Rn57e4UPddg6fhqBFiHMLf2ADU3BHIcPYnuowbJ64LDohbI69eR4EH2ImOsK6Kwn3hCk_G-ufvAbTqaY5b2oNSVXRwWGQ-py2Ij3pK61IPaLuPVDw25sd6BFH-bxx4e18prc2mYfJ0g4PtFOIhEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه اصابت پهپاد انتحاری شاهد 136 به ترمینال فرودگاه کویت از دید دوربین مدار بسته.
mohsenreyhani01
سازمان هواپیمایی کشوری کویت با انتشار ویدیویی گزارش کرده که «نخستین تصاویر» حمله پهپادی به فرودگاه بین‌المللی این کشور که از طریق دوربین‌های مداربسته بیرون و داخل فرودگاه ثبت شده را علنی می‌کند.
در این تصاویر که از چند زاویه بیرون و داخل فرودگاه دیده می‌شود یک پرتابه مشابه پهپادهای انتحاری به سقف ترمینال فرودگاه برخورد و موجب انفجاری بزرگ می‌شود.
در ویدیویی دیگر، وزارت کشور کویت با انتشار ویدیویی اعلام کرد که شیخ فهد یوسف سعود الصباح، معاون اول نخست‌وزیر و وزیر کشور نیز ضمن بازدید از ساختمان ترمینال ۱ فرودگاه بین‌المللی کویت، این حمله را «تجاوز فجیع ایران» خواند.
کویت اعلام کرده در جریان این حمله یک نفر کشته و بیش از ۶۰ نفر مجروح شدند. فرد کشته شده تبعه هندی بوده و وزارت خارجه هند گفته چند شهروند دیگر این کشور نیز در این حمله زخمی شده‌اند.
سپاه پاسداران که شب گذشته از حملات موشکی و پهپادی خود به پایگاه‌های آمریکایی در کویت و بحرین خبر داده بود، روز چهارشنبه گفت «هیچ شلیکی به سوی فرودگاه کویت» انجام نداده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/75931" target="_blank">📅 01:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75930">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aajgSTr9c8X_RhccJ2yH3XRFwKuMsw7HvIjyJRWFRFQzneMS6ojwRcUI3m7GTrH1_7M7nSuw08ualRvx2i31Z1tKNN4uuD_PjpBNQD0nNSbppWyUZpKEiHHE1yiOYm9C-uMu0f7SDxQ3P1bGNjgOffMAFoOh7iLJxJFCzti7bx_NTWbSmbKXcTzjGiUM8RUQDKf654cuSiTCnK0cyXB-_6sr7KtOWQiy1UmuJVOKiF88LGpm9nGq67QFQb3-84wjUHxp4h-0h3WW8TWqwZRyaultg2O1DhVQ_1wvLrA_LEagw19VmaROZMRu9WweMtyP21tB1RC9xltCMVHLTeaEjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس نمایندگان آمریکا روز چهارشنبه از قطعنامه‌ای به رهبری دموکرات‌ها حمایت کرد که هدف آن متوقف کردن جنگ با حکومت ایران تا زمان صدور مجوز از سوی کنگره است.
به گزارش رویترز این قطعنامه با ۲۱۵ رای موافق در برابر ۲۰۸ رای مخالف تصویب شد و چهار نماینده جمهوری‌خواه نیز به دموکرات‌ها پیوستند.
این رای‌گیری تازه‌ترین شکست سیاسی دونالد ترامپ در کنگره به شمار می‌رود؛ با وجود آنکه جمهوری‌خواهان در هر دو مجلس اکثریت شکننده‌ای دارند.
بنا به این گزارش، این اقدام عمدتا جنبه نمادین دارد، زیرا برای اجرایی شدن باید در سنا نیز تصویب شود و همچنین برای عبور از وتوی احتمالی دونالد ترامپ به حمایت دو سوم اعضای هر دو مجلس نیاز دارد.
با این حال، این رای‌گیری نشان‌دهنده افزایش نگرانی در کنگره درباره جنگ با حکومت ایران است.
سه قطعنامه مشابه پیشین در مجلس نمایندگان شکست خورده بودند، اما با اختلاف آرای کمتر از دفعات قبل.
همچنین سنا ماه گذشته یک قطعنامه مشابه را در یک رای‌گیری رویه‌ای به پیش برد؛ اتفاقی که پس از هفت تلاش ناموفق قبلی رخ داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/75930" target="_blank">📅 01:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aENbctYEv9zwPJBPKBmf4tdNZ7PdBXgthW7ViqcpR4gnGk7M__xVC4Qu-QoGAu82Akbbph3jC7fgObNVSlPAC12NcqoM1DrLvGOeZJ-JYdCqF34Afc2n3c4iHlp-fOHSUZsKOdYQ5Ea2M5iVLo6eo4lhgjArzO9JQgti0gFxS4mHxtvsHoinure5uIAsa98EkVba-Qs2-SgpxNVnaa35Pv3C_u2NIHGYEBPz_6hi-tpko0E67ZR4_1v8hBEMn-NaqtIJiAwRKjaKchpbNBm_k0ijgmmqT8lWpxrSj9Cu9RWasWkVi7LMoqpgOiKHcIIhFR6RHJsIzKToNkyCPv_cHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ترامپ: می‌توانیم همه را نابود کنیم، اما ترجیح می‌دهم به توافق مکتوبی برسیم
دونالد ترامپ، رییس‌جمهوری آمریکا چهارشنبه ۱۳ خرداد در کاخ سفید درباره حمله جمهوری اسلامی به کویت و شکستن آتش‌بس گفت: «ما سه‌شنبه شب حسابی به آن‌ها (جمهوری اسلامی) ضربه زدیم، و در واقع دیشب هم همین‌طور. و وقتی موضوع را برای من توضیح دادند، گفتم بسیار خب، پس همین کار را می‌کنیم، اما ما هم کمی داشتیم شدید به آن‌ها ضربه می‌زدیم.
ترامپ گفت: «بنابراین برای بعضی چیزها دلیلی وجود دارد، و معمولا دلیلی هست که گاهی منطقی به نظر می‌رسد. و خب، آن‌ها کاری انجام دادند که خیلی… مسئلهٔ بزرگی نبود. ما خیلی سریع جلویش را گرفتیم، همان‌طور که با بزرگ‌ترین ارتش جهان این کار را می‌کنیم. اما بعضی‌ها ممکن است بگویند که آن‌ها تا حدی تحریک شده بودند، چون ما به دلیلی دیگر اقدام قاطعی انجام داده بودیم. بنابراین آن‌ها در حال تلافی بودند.»
او در ادامه گفت: «خود مذاکرات بسیار خوب پیش می‌رود. بسیار خوب. اگر اتفاق بیفتد؛ ممکن است اتفاق بیفتد، ممکن هم هست نیفتد، چه کسی می‌داند. اما اگر اتفاق بیفتد، ممکن است همین آخر هفته رخ دهد. تقریبا اوضاع به همین شکل است.
آنجا بخش متفاوتی از جهان است، می‌دانید. من می‌گویم در آن بخش از جهان، آتش‌بس یعنی این‌که به شکلی ملایم‌تر به تیراندازی ادامه بدهید.»
ترامپ افزود: «تحت هیچ‌ شرایطی نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند، هر اتفاقی ممکن است بیفتد وقتی با ایران طرف هستید، اما وقتی با کشورهای دیگر هم طرف هستید، این یک بخش بسیار بی‌ثبات از جهان است، احتمالا بی‌ثبات‌ترین بخش جهان.
رییس‌جمهوری آمریکا تاکید کرد:
«ما از سه تیم رهبری عبور کرده‌ایم. این یک وضعیت نظامی است، و واقعا هیچ ارتشی مثل ارتش ما وجود ندارد. ما می‌توانیم دو، سه هفته دیگر ادامه بدهیم و همه را کاملا نابود کنیم. ترجیح می‌دهم این کار را نکنم. انجامش خیلی آسان است. آن‌ها آماده‌اند که این کار را انجام دهند. می‌خواهند انجام دهند.»
ترامپ گفت: «اما اگر بتوانیم چیزی را مکتوب به دست بیاوریم که همان نتیجه را بدون کشتن همه به‌دست بدهد، من آن را ترجیح می‌دهم. فکر می‌کنم بیشتر افراد من هم همین را می‌خواهند. بعضی‌ها نه، اما بیشترشان بله. یعنی ما بالاترین بازار سهام تاریخ را داریم، با وجود یک درگیری نظامی یا جنگ. بعضی‌ها اسمش را جنگ می‌گذارند، بعضی‌ها درگیری نظامی. برای ما چیز بزرگی نیست.»
🔻
ترامپ: اورانیوم غنی‌شده زیر کوه دفن شده و می‌خواهیم آن را خارج کنیم
دونالد ترامپ، رییس‌جمهوری آمریکا چهارشنبه ۳ خرداد درباره خروج اورانیوم غنی‌شده از ایران گفت جمهوری اسلامی در مقاطع مختلف با این موضوع موافقت کرده، اما چند بار نیز نظر خود را تغییر داده است و این مسئله بیش از حد بزرگ‌نمایی شده است.
او گفت: آن‌ها [با خروج اورانیوم غنی‌شده از ایران] موافقت کردند و بعد گاهی هم مخالفت کردند. این یکی از چیزهایی است که درباره‌اش صحبت کردیم. خیلی هم بیش از حد بزرگ‌نمایی شده است. من خودم آن را بیش از حد بزرگ‌نمایی کردم.
ترامپ با اشاره به گزارش آژانس بین‌المللی انرژی اتمی گفت این مواد «نابود شده» و زیر کوهی دفن شده‌اند که تقریبا فروریخته است.
او افزود بیرون آوردن این مواد بسیار دشوار است، اما تاکید کرد: «من می‌خواهم آن را به دست بیاوریم.» به گفته او، آمریکا و احتمالا چین تنها کشورهایی هستند که تجهیزات لازم برای چنین عملیاتی را دارند.
رییس‌جمهوری آمریکا همچنین گفت سه سایت مورد نظر به طور دائمی زیر نظر هستند و در صورت هرگونه تحرک، آمریکا از آن مطلع خواهد شد.
او افزود: «اگر کسی به آنجا برود، دقیقا می‌بینیم چه اتفاقی می‌افتد و کمی هم بیشتر آن را منفجر می‌کنیم.»
رییس‌جمهوری آمریکا درباره مین‌روبی در تنگه هرمز گفت ایالات متحده از مین‌روب‌های زیرآبی استفاده کرده و مین‌ها را پاکسازی کرده است.
او افزود: «تنگه هرمز بلافاصله پس از امضا باز خواهد شد.»
🔻
ترامپ: ایران یک مشکل بزرگ جهانی بود و اگر مهار نمی‌شد، می‌توانست خاورمیانه را نابود کند
دونالد ترامپ، رییس‌جمهوری آمریکا درباره گفت‌وگو با حزب‌الله گفت آمریکا برای نخستین بار با این گروه صحبت کرده و سه‌شنبه توافق شده که شلیک انجام نشود.
او افزود اسرائیل نیز قرار نیست شلیک کند و تاکید کرد موضوع‌های مرتبط با تنگه هرمز، برنامه هسته‌ای و لبنان باید از یکدیگر جدا بررسی شوند.
ترامپ گفت بنیامین نتانیاهو، نخست‌وزیر اسرائیل، برای او «شریک بسیار خوبی» بوده است.
او همچنین با اشاره به نقش آمریکا در تحولات منطقه گفت بدون کمک واشینگتن، اسرائیل قادر به انجام عملیات اخیر نبود.
ترامپ افزود ایران «یک مشکل بزرگ جهانی» بوده و اگر مهار نمی‌شد، می‌توانست خاورمیانه را نابود کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/75929" target="_blank">📅 23:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75928">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoFhpc5ooGcpIvgJJYwppst6aG15Xnwt48O_yvvaT2lp9sGgW6uluCwUS2EJaCUNLy519ncKYajDItCij1fB3SLrP1HXyHhkPeQJLJq9bTQJlro3tLz5m1YyHB64JbdO2OWklfDR3KiRzb-U5NTNTl-oD7YIOm9HxtqrS0fjOy5sfQsU1Z6t3WqV_VQjxxk16ah5Cduu-WjnT1O2ax63T6xWza4GXVRiWofo67w-S7FPolD38Kahu3jt4YHchPmdlf7WbIO4yDOaWlJlYGfVZjJbB-7qU0Yh9BOGls799iyWy7uRyuI-xO9FmgmszUd2fldLA0Deo8XgwpLD_R-nTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقجی، وزیر خارجه جمهوری اسلامی، روز چهارشنبه تهدید کرد که حمله احتمالی اسرائیل به بیروت، پایتخت لبنان، باعث «ازسرگیری کامل جنگ» ایران با آمریکا و اسرائیل خواهد شد.
او در گفت‌وگو با شبکه المیادین، نزدیک به حزب‌الله لبنان، همچنین ادعا کرد که بعد از تهدید اسرائیل برای حمله به ضاجیه، حومه جنوبی بیروت و مقر اصلی حزب‌الله، نیروهای نظامی ایران در «وضعیت آماده‌باش کامل» قرار گرفتند.
عباس عراقچی در گفت‌وگوی روز چهارشنبه خود همجنین اعلام کرد که ارتباط با دولت آمریکا «قطع» نشده است، اما افزود که «هیچ پیشرفت ملموسی در روند مذاکرات حاصل نشده است».
ساعتی پیش مارکو روبیو، وزیر خارجه آمریکا، اعلام کرد که ایران هنوز تصمیم نهایی خود برای پایان دادن به جنگ را اعلام نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/75928" target="_blank">📅 23:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75927">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ljny-MyYMQxiXptJha8LoCEM1CDro58PZkHGQA72dFcAfjJyHP1KAfZqeFbVaYxF5XdWZf2OI6eLrbgxV75pgmGIfmbIF5JMUrep2JDcWQU9Y20xmJHZ4rLzT4OiBRQtvNeMzTNeruv6VkV0cxi1f0XQDNNBbxjU3oJ3QRzKjNwEeYUVnzUr26P42oinKP14bsbiFjygcjDGPnHQlA90UGo6t3XxBHqfR9w3FEjt_RgTLiPsBe4iV7co6WjXFhtNLjdUA7L8PfF3t8w9vgAqTMjQ3F0S9gH5faA-PrrJ8YvtGU7Anges83acAsiVqHaT5rZlFzdfDqxuyiPbHxB55A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام
ادعای جمهوری اسلامی
درباره شلیک به یک ناوشکن آمریکایی رو دروغ خوند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/75927" target="_blank">📅 23:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75926">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/993ece4c51.mp4?token=rqxCU1MwaOY7-oHrZfNyKh0Lajk7rEZcKr7JGU-uMgNAkl8LicL8zIq1PRnndqMq7fATZMWLIFP1jRWJMb8eompHo5kJMZXG-CWDZD0ywXMGJhda4CLP8nHP8RHIVpMo-CzbJk0yPOdkMF0_6JRXnVaEBldk1Ks5jgbNeEsA4FdFOii1w29u-p8hnHv9wd-Ma22ov9GkAJpTKFPQnanh7Md19juEKBlimHqoHgx7XVSVxUI_zzooL2L0lp2Y-G4xNWkL6dI8jDjUO28psoZam6ov433OT37Qsh7991tMpbMpzHgsItjPNaZ8gvBAFa5EFDZgq570-kQ33Gk5LBJArg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/993ece4c51.mp4?token=rqxCU1MwaOY7-oHrZfNyKh0Lajk7rEZcKr7JGU-uMgNAkl8LicL8zIq1PRnndqMq7fATZMWLIFP1jRWJMb8eompHo5kJMZXG-CWDZD0ywXMGJhda4CLP8nHP8RHIVpMo-CzbJk0yPOdkMF0_6JRXnVaEBldk1Ks5jgbNeEsA4FdFOii1w29u-p8hnHv9wd-Ma22ov9GkAJpTKFPQnanh7Md19juEKBlimHqoHgx7XVSVxUI_zzooL2L0lp2Y-G4xNWkL6dI8jDjUO28psoZam6ov433OT37Qsh7991tMpbMpzHgsItjPNaZ8gvBAFa5EFDZgq570-kQ33Gk5LBJArg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شلیک موشک‌های ارتش به ناوچه آمریکا در دریای عمان
شامگاه چهارشنبه، خبرگزاری فارس نزدیک به سپاه پاسداران به نقل از نیروی دریایی ارتش جمهوری اسلامی از هدف قرار دادن «مرکز فرماندهی و کنترل ارتش آمریکا» خبر داد.
فارس نوشت: «ساعاتی قبل و درپی نقض مقررات تنگه هرمز و شرارت علیه شناورهای تجاری ایرانی از سوی ارتش آمریکا، نیروی دریایی ارتش جمهوری اسلامی، به‌محض کشف و شناسایی، «مرکز فرماندهی و کنترل» این شرارت، مستقر در یک فروند ناوشکن آمریکایی را هدف قرار داد.»
در رسانه‌های جمهوری اسلامی ویدیوی کوتاهی از لحظه شلیک موشک‌های ارتش به اهداف مورد نظر در دریای عمان منتشر شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/75926" target="_blank">📅 23:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75924">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RM6nQJDIyLmH3WsPqg1DDwu3PdIsVMuMcApqcxsNNI2gcMhZlZpgkNfQ_Ip6pTnlPIzhakIk3gN4EBheHZ9K9Orh7sjtdg_XunPn275JvMztuHLqiMEHrPVewUJL5A_MkkMV47yhs0RZY-4q1LQ84kT9oHR51-9qmgrmbD0S1hU14KO-DonpRzvmUzzZK3bNIT6RrjjKt77NYvx85TNOWkhaN7UyFXc9kdgFOigH0AEApNBqWxGeeEKa8KqX8mwMhznFpA2ff0xVFyy_NgCk2mvGOvKvgLnjEQHym_BKNYeBtD5vHL0Qendd14sJsmhWt_7FiCOAZcyYbK0J5pn8Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LeiYqfnLgDf0TOgjGRSTIsRsX7UQbaJOeUajx1C8jQzsw8-uFP6Cwbd4QlQEFmOPuLxWaubht167kcQh-fKv3O_RlrsAI8xumWZ_oEJ3M6FriHJfay6ozTAkffZbTSSSYxLt6AdE5tA-QL7CJTJMOXaAKbOWY-brLWAZkikNjRU-juZ937Z5W3GvO97gZA8F4xpMSB9MJ0jGQt8JFwHQJN1IqWDMzG5QExsVyA3UamNia0Mq9QQBNkl5x_Y_jgeUuXSzUYBin83AAOgE1iYa_o88LcaUlQyYMsOl75TOdOg9_hLNa4pqv_FoWNpTaoR9_XSJO4yrI0tUoI_In0dBkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده اعلام کرد ادعای جمهوری اسلامی مبنی بر اینکه به ترمینال مسافری فرودگاه بین‌المللی کویت حمله نکرده و خسارت ناشی از یک موشک رهگیر آمریکایی بوده، «کاملا نادرست» است.
سنتکام اعلام کرد جمهوری اسلامی با پهپاد به این فرودگاه غیرنظامی حمله کرده و این اقدام را «عامدانه، محاسبه‌شده و بی‌دلیل» توصیف کرد.
@
VahidOOnLine
پیش‌تر:
حسین محبی، سخنگوی سپاه پاسداران، گفته است که تخریب ترمینال فرودگاه بین‌المللی کویت «ناشی از خطای سامانه‌های پاترویت آمریکایی بوده است.»
به گزارش رسانه‌های داخلی ایران آقای محبی اضافه کرده است که سپاه «هیچ شلیکی» به سمت این فرودگاه نداشته است.
او مدعی شد که بنا به تحقیقات سپاه: « تخریب ترمینال مسافربری فرودگاه کویت ناشی از خطای سامانه‌های پاتریوت آمریکایی بوده است، که پس از شکست در رهگیری موشک‌های ایرانی بر این ترمینال فرود آمده‌اند.»
در نتیجه فرود آمدن یک موشک در فرودگاه بین‌المللی کویت، دست‌کم یک نفر کشته و چند نفر زخمی شدند. فرد کشته شده تبعه هندی بوده و وزارت خارجه هند گفته چند شهروند دیگر هند نیز در این حمله زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/75924" target="_blank">📅 22:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75913">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s-oYu9BHxT-MAB8fiFi0P09w5im8AIhr1R37fe7PdWda3zknWrr6qY4rkr-HVVskl5hp8QS2fYrpdcP9RJSF4KgG3pSvoAq6Yz3q0_kZhQq3Rs5EJMVW8q2VRbjpCz5gTOmp3N0QCf5KPbuWANcc1zXLll9CeZrpsWwhMeBXWneMnjNXjVTaqSFDmRcBc8XZHgPlpMaYDuUVBKv_BTjUxkOQpLhGHzoMr0Sp77yqX6S1MpVpcRcm0sxF9cWS7eR7p5jOL3Vtgaj3M02HL423ExNjRNHcElR29eo9fMZGzk_-AtXdIToanQvL2MzChz-SIdD9Pqob7nUMv15DACg7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l-AvOnKnv9ZNrWXJRRDJlnqj_kP7H78t5jUJI7C5rlN-6gZTMAtsch7OYIhD8yF50yF-bZW7dXidhzgob-qH-q1FWIYUHf6g-SMV-deKWSsFhNqhKps2O44aZ057UHZ_1bpxOXtX-lWbznacooPapLThuzN7IAb_sPj13VoFxun6XNuPEKBYmS9Iw2_RDUHx0iYlobla56FncRAG8akjQMFhw5-323gxCBRYUYSnhC-nBKY9NgaKVSDQzWsAyZPhn8kKqh3KAlmmq2f1ME6x5ok8jlEeZfo3iqWh2By5dxonPmYAbek663AHNLO866u6ImPNrZ8ycxXfai8SOeSWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oHTUwuttLVa66n05jcrY-1vZ5zZBJGMRHhon7Y2rtoH_IjYgt8WZU-ojaSCJ1PS-x5Qa3NVzz6H-drPsa3gM9u5EXQPTspho7GaNuHmRnEI1eDmbJha3c6Xb4uh1y4alyPaVgLjEdxEaFzWj3MD8_FVnGy-5YYhBVXr05bknBzpef77E1HwBPY9YKVbmU3PrIY_Ujj-wO6m1JSWpD-TBpn9BSUelR4eMgGfCFgnSaI-Y_DXL1-vUfjRB0Z9rSsgdu4l4O8adA64-A5eilCHtSc9aQUxtLWKy9CvxUbWwFZ6PQestGBW7xtSeQXLnMjJjlKo5lgm3eS-fGh9AjzcQEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/USvhMF5qzhcnNJKN4mNR04njzYq0e0lcgz1mwn6GXzEouOTq2E50lx70QERSS1PZIIT87QOafWbRK62BbMZBdflLnit-ml-6u6lrcy3CJyP7kIMJN9kw7AtozQk6uoj4JkEPBEfDFL-aEib9BWANHxewQx3bSWoDzdtFoUOxVAX3bNL4JVSl0AhEtW5QMlc8Rkq01fxSp7KU2E9aKH2THtWuK4WX_q-N_iwwXW1orcvAgcLPto9rBQkbRbI4jCLHRvUO99Yc7QIZLIe1eKcNJ-zte1eZ-rEcHZD7xScr2UE2_QcQl1evQVVndY_9ok8fPMVjTogHwl559_wyv2QCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ry2TxtO5PlL-DJwaG-qbGa6diz5loAZIKBhDj4jhstIxylJ8VGewokFjkkb7dE0_FxaOzaavv57s2QnazyaL--kRKUte7M1zmUbtjhgLk9pL2lhloObdZW5xw8uNOJKime4tMC4lsRla1nonNAGNxcswNqDKCj9vJjJCSE97RJapAKsyMRM4-2i0lNh02NvCQlm_wzT5HeADOvrnBv0wI4i5yfg7nFCDlWmMi064kC6QKSww24Uv6pulNluDbl5q1uJkf-lgnxojaQIbCQO46OLBhQOvj4OgUuhJugh_c66Mrb5QJr5gw6J8wZcRtTjq5vUdEbURT_QNzVg1e3WyEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WplrWY43XDiYtOifEFq5rHePn6makOwBx-uh2yFSXExXYO3tjE66Ig7_dXM9pliuj1-p-soPB-7Diw9or_fYik8VoBv8-Mba7RyuT5WV2tArinE4PErOlTC0az_UtzALdhy_xfKCedASd86Op3YGoOCeFSqWt0GgxRiIP7b9Gw_F948Sjxdq9JnPe0PnvbfgyeBUS56AEGv8zeDK27pEIjmXdE5Ytn0de7-Wg-Q9T3lr2epK_M3RjSl15l8L_WLP7vwxxDWGjfbbfKRHzzJvxa_F15LENgA889daxcmTZ3XS6sr4BUAXGskgYXQ7PRiTVorRLg1nVIDCjsdPQnRaiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VdDj1UhvQIQ1HAcudgcEgkxEtTjClEk3BNwJQjCAMOiTYlFji8iLGt_MhjwMNRwJfyEKBKrR8jEMbiFLDZ7yOxROjh1MClyZVM_9aNHVtV0gZ-JGXHbNYBV7BgJagA9tZydOq6JMiPtA2quKg80mA8NElw85zl1IYQU3xPwXsSo6B_gSX4nBNmxJJ5Qq-3lPxWlPTCskA40yU4M80XayxtcCWN9RMmnJbvuIfeWKexMTkATlYe_-rjguKdwUbjyV3Kyif1R9Y2oDZIXTqg0mGC0oQypAtwg11DvbbFoDdcyOZkJ6EJeANqyLbalermo25zGi3_iF3WvIV5bJ8F-eYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DaBoANJ2kPiz3jtY8oJnxNaQGTbtbRveFmCRiYgz805X4EwCG_HYdelOXaIrzVTjRqfIS1lsVlxOOTk89uCJfUXOcUqDWCksO7wmxZ44fUYVtiDmxb10_iY_sGsncA7jW6d5NuxYUkbDW1RUVQkLBz298a6Tx4Sgd2dKz3CMu6kgAdQWGzXacvS7iEb5yvWvgaLmKeB5QUMbLQ6JX64EuDlY6kzHzdM9iPw6PA6PEPLl0nomu8TbOO09LtH3zaXeN8iobpaKyBr-lzq-YmWLXKGMmrzfyADeujqNJUSZN47oOe-YjNOjTdDXntyMPLP9acsSx92LT_fEvpFUNUqyVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M93QDeeqwT4s8tcM9oUlSsLiBkmVCKLfOJy0w4aZFBtbeWcxYiWJHVqk1ROKUFI8ogdSOxLm6AYAB5bewYEJJJYgfj4yVy9dwU-BBt5EF5j8rGeGKD5VGSDkS0wvX_2ouQLeSfOUaj54Eby53L0aicbvuQhYl152n_ELXheCik7UKHzBgy-vNCk6uo-4V3jefPWI9XlRiyYJuzPRzsg5b2chyGnFtccs2etiBT7de8OW-ZymSYZ_fYmTzaqSkS24CAArungkbkJaUhBS0-h1fqJ_A9jQ2oWnbDW9faQdDcjM03KBUcWhf2VXpNbCIpdSbcncMZa4QX04c23AU1iZ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WCoqf_Ps1cnmN1nZQ042UrVEpMIgSPGOxy-y3Y7erwZKRqqsm_WSSinr1MmDo4p3viW4IbMynPkOeQJOtubZ7W0OxMkCPAuOp2X9EnsQeGgreyrLzfcqaC6i-fwAFKI1_d_hEN28rR240kvXUQ5Az62GrTzLWShzGS3loCW7nUNrhNyWDW_Q6uHCfcCUCTmjdZuXvWQR-rzMOklT1_iMmE0wMYNXMhwbgKoEr0XSIs7OxS_vhlSalxHoPdEI-1JHf6B-by_4aG2VER5B4mmxF7O4EQVk24PyF6IPPvlSr9l_ZZBYZT69IJIpdDgn5UfflGfocjbLhiRqgJdoWPcTtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت دادگستری آمریکا روز چهارشنبه اعلام کرد مدیرعامل یک شرکت فناوری در کالیفرنیا به اتهام تأمین تجهیزات آمریکایی برای نهادهای هسته‌ای و نظامی ایران بازداشت شد.
بر اساس بیانیه این وزارتخانه، جمشید قُمی، ۶۳ ساله، شهروند دو تابعیتی ایران و آمریکا و ساکن نیوپورت کوست در ایالت کالیفرنیا، به «تبانی برای نقض قانون اختیارات اقتصادی در شرایط اضطراری بین‌المللی» متهم شده است.
او متهم است که «تجهیزات پیشرفته شبکه، امنیتی و رمزنگاری ساخت آمریکا را برای مشتریان ایرانی، از جمله نهادهای هسته‌ای و نظامی حکومت ایران تهیه کرده است.»
وزارت دادگستری آمریکا همچنین اعلام کرد که جمشید قمی از «شرکت‌های پوششی» در امارات متحده عربی برای پنهان کردن محموله‌های تجهیزات شبکه و رایانه‌ای که مقصد نهایی آنها ایران بود، استفاده می‌کرد و این شرکت‌های واسطه برای مخفی نگه داشتن مقصد واقعی کالاها و دور زدن تحریم‌های ایالات متحده به کار گرفته شده بودند.
جان آیزنبرگ، معاون دادستان کل آمریکا در امور امنیت ملی، در این بیانیه گفت: «طبق آنچه در کیفرخواست آمده، قمی با تأمین فناوری آمریکایی برای سازمان انرژی اتمی ایران و سایر نهادهای تحریم‌شده مرتبط با برنامه هسته‌ای ایران، به ثروت دست یافته است.»
او افزود: «بخش امنیت ملی وزارت دادگستری افرادی را که برای پیشبرد اهداف هسته‌ای ایران قوانین ما را نقض می‌کنند، پاسخگو خواهد کرد.»
به گفته وزارت دادگستری ایالات متحده، متهم بیش از ۱۵ میلیون دلار از ایران به حساب‌های بانکی خود در آمریکا و یک حساب امانی منتقل کرده و به‌دروغ این پول را به سازمان مالیات آمریکا به‌عنوان ارث خارجی اعلام کرده است.
بر اساس این اتهامات، اظهارنامه‌های مالیاتی فدرال او تقریباً هیچ درآمدی را نشان نمی‌داد و بالاترین درآمدی که در هر سال گزارش کرده بود تنها ۲۰٬۶۸۴ دلار بوده است.
وزارت دادگستری آمریکا همچنین مدعی است که او از درآمد حاصل از «طرح دور زدن تحریم‌ها» برای تأمین هزینه ساخت یک عمارت چند میلیون دلاری در اورنج کانتی کالیفرنیا استفاده کرده است.
@
VahidHeadline
دادستانی علاوه بر درخواست مجازات حبس، به دنبال مصادره اموال وی از جمله عمارت گران‌قیمت اوست.
بازپرسان معتقدند او به مدت بیش از یک دهه از طریق شرکت خود در تهران به نام «فراز پرداز رایانه»، بیش از ۲۵۰ تن تجهیزات کنترل‌شده تکنولوژی را به‌صورت مخفیانه خریداری کرده است.
او متهم است که با استفاده از حساب‌های شخصی در eBay و PayPal و از طریق شرکت‌های صوری در امارات کالاها را تهیه و به ایران ارسال می‌کرد.
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/75913" target="_blank">📅 22:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75911">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tEmJQUQzWNsMCIQ5xJDrVcrJp5zBRwd83WRJFXKzj2L7_oL45Z1bbKlKYl_VmhaUVELlUTAOIfPtADNqCKQSS9KkF8Gx3x4xT7NYTNtiLCyp_RbokV8vHQ__Sx9Eh8EP2gTrHQsBS_iDUsWvB4-O_9L227uw3MD0EFURzvNYKf1rzJtzcG7o9sQrKXK17Ua6E7QYvK8SaXvCSHSRN2_mCBrB8DwFIV070j3WghOrk-jS7P7_by0fSj6votu0juJYh9ld0426rqdE77W9LwFuZ2bdUA-XQQJzi_dRQ4Y7Mbb2mQg3dK4wBfp5Xvd6oyvdIEFEBPxTOIjcZ2tmObAi0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/un-CIqqvp1OXtoiWsu2oAmJMaGD2qHrya1qaU5vFCyfCz-jLyoFDXw2Kj7leleJplV8GwR2xQVnIsiXAMJ3Z9QTLuhFbtds2PPiK1_IgtorG22f2EuZA2TMk1BuZ3ph66kgsWptu7R3c1miF6veTZxNwXZwLJuIenJbF74bnzRPE-KFVzuxHFb0rRlfcrgW9gdh0FznqvFsfVAp2gxxCxil76SN1ZRZJkkuyo1NJLaZSdhAtLuEyOtehsuHELIqE0MWtab_3tEom0D5V4EV0yM9YZuLofzBYuFDk0W8mqcbFe2HWOe9GvAQ3P7AlQn6AoT5xmyP8DkSkCjHeJ98vAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سی‌ان‌بی‌سی، ترجمه ماشین:
▪️
نتانیاهو از پاسخ به سوالی در مورد اینکه ترامپ در تماس تلفنی این هفته به او فحاشی رکیک کرده و رئیس جمهور آمریکا گفته است اگر او نبود، نتانیاهو الان زندانی بود، طفره رفت.
نتانیاهو در پاسخ به سوالی در مورد اینکه ترامپ ظاهراً او را «دیوانه» خطاب کرده است، گفت: «وارد جزئیات نمی‌شوم.»
[ولی ترامپ در
مصاحبه با NBC
گزارش آکسیوس رو تایید کرد که بهش گفت دیوانه]
▪️
نتانیاهو می‌گوید او و ترامپ «اختلافات تاکتیکی» دارند اما «در مورد مسائل اصلی اتفاق نظر دارند»
نتانیاهو هرگونه اشاره‌ای به اختلاف با ترامپ را کم‌اهمیت جلوه داد و گفت اگرچه آنها گاهی اوقات «اختلافات تاکتیکی» دارند، اما «در مورد مسائل اصلی اتفاق نظر دارند».
او گفت که این موارد شامل جلوگیری از دستیابی ایران به سلاح هسته‌ای و تهدید اسرائیل با آن می‌شود.
او گفت: «گاهی اوقات، مثل بهترین خانواده‌ها، این اختلافات تاکتیکی را داریم. اما ما همیشه راهی برای حل آنها پیدا می‌کنیم و این کار را به عنوان دوستان خوب انجام می‌دهیم.»
او گفت: «ما می‌توانیم صبح اختلاف نظر داشته باشیم» و تا بعد از ظهر به زمینه مشترک برسیم.
▪️
نتانیاهو در پاسخ به این سوال که آیا واقعاً آتش‌بس با ایران برقرار شده است، گفت: «فکر می‌کنم یک بازی تاکتیکی در حال انجام است.»
نتانیاهو گفت: «و ایران مطمئناً می‌داند [ترامپ] چه گفته است، اینکه در صورت لزوم، بازگشت کامل به اقدام نظامی وجود خواهد داشت. این تصمیم رئیس جمهور است، اسرائیل آماده است، و نیروهای آمریکایی نیز آماده هستند.»
او گفت: «فکر می‌کنم ایران باید این را در نظر بگیرد. فکر می‌کنم آنها دارند این را در نظر می‌گیرند که دارند با آتش بازی می‌کنند، این واضح است.»
▪️
نتانیاهو از اقدام تلافی‌جویانه ترامپ در محاصره بنادر ایران در تنگه هرمز تمجید کرد و آن را «بسیار مؤثر» خواند.
او گفت: «محاصره معکوس، یک حرکت هوشمندانه بوده است.»
▪️
نتانیاهو گفت که «هر دو روز یک بار» با ترامپ صحبت می‌کند.
او گفت که دو رهبر «اهداف مشترکی دارند... ما می‌خواهیم به آنها دست یابیم.»
اما در پاسخ به این سوال که از توافق آتش‌بس احتمالی چه انتظاری دارد، نتانیاهو اذعان کرد که «این یک سوال بی‌پاسخ است که جنگ چگونه باید پایان یابد.»
▪️
نتانیاهو گفت نهادهایی که به نفت ارسالی از طریق تنگه هرمز متکی هستند، در حال حاضر «در حال توسعه مسیرهای جایگزین» هستند که کمبود عرضه انرژی ناشی از بسته شدن مؤثر این آبراه کلیدی در طول جنگ را جبران خواهد کرد.
▪️
نتانیاهو انتظار دارد که تغییر رژیم در ایران رخ دهد زیرا رهبری فعلی «به شدت» تضعیف شده است - اما پیش‌بینی نکرد که این اتفاق چه زمانی رخ خواهد داد.
نتانیاهو گفت: «شما نمی‌توانید دقیقاً پیش‌بینی کنید که چنین رژیمی چه زمانی سقوط می‌کند. شما در بسیاری از موارد آن را پیش‌بینی نکردید: نه در رومانی، و نه در سقوط دیوار برلین، و هیچ‌کس آن را پیش‌بینی نکرد، اما این اتفاق افتاد. چرا؟ چون ترک‌ها از زیر در حال گسترش بودند.»
او گفت: «در واقع، شما همین الان در ایران شکاف‌های عظیمی دارید و نمی‌توانید پیش‌بینی کنید که چه زمانی این اتفاق خواهد افتاد.»
«اما من دیروز در یک نشست عمومی اینجا گفتم... ببینید، من معتقدم که در نهایت این شکاف‌ها گسترش پیدا می‌کنند و رژیم سقوط خواهد کرد و ما تمام تلاشمان را خواهیم کرد.»
نتانیاهو گفت: «من فکر می‌کنم که ما باید به مردم ایران کمک کنیم تا این رژیم را سرنگون کنند، و این تغییر نکرده است، اما دقیقاً در لحظه‌ای که ما انتخاب می‌کنیم، این اتفاق نخواهد افتاد.»
او گفت: «فکر می‌کنم آنها به شدت تضعیف شده‌اند.»
nbcnews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/75911" target="_blank">📅 19:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75910">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GjFybxQSwCyzekvS3I4bDa4jtRD_bNW5DBIYmeJQNzWPkR1jALxmdYMVdov3nHas7jNN40JmK0hNMtEYM-Np8PeWVra7W-Xatua2zUn-o6nRx8chr0iJrzQ9JP0Nd-prWf53HmxbwpfPmsP0aPDpkND13asl_osT8ZRWVAK7ja2JjZoBaPwqGk9rMwtHsDU-N0tp-KSbZegue1-AK6PzQYdTl-_eam5zQ8g1nSMkmpDjMAd6CoJ5bi1sVpGG1x0ddZbVIr3nI9D59bz93v-b_xDOaHqmP1PA_yVY8_Q46HwOY3WJ8Rk9gOJH7TLJBdXh-J-legcH61N4Zd7OYe35Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا، روز چهارشنبه گفت که سرنوشت ذخایر اورانیوم ۶۰ درصدی ایران در مرکز مذاکرات با واشینگتن قرار دارد و تهران هنوز با یک توافق صلح موافقت نکرده است.
روبیو در جلسه کمیته روابط خارجی مجلس نمایندگان آمریکا گفت: «فکر می‌کنم اکنون در برخی از اسنادی که میان دو طرف رد و بدل شده، این موضوع به‌طور واضح مورد توجه قرار گرفته است، اما تا صبح امروز هنوز تأیید نهایی از سوی نظام تصمیم‌گیری آن‌ها را دریافت نکرده‌ایم.»
روبیو در مجلس نمایندگان آمریکا بار دیگر بر اظهارات پیشین خود مبنی بر پایان جنگ با ایران تأکید کرد و گفت: «ما دیگر حملات مستمر در داخل ایران برای تضعیف توان نظامی آن کشور انجام نمی‌دهیم، زیرا عملیات "خشم حماسی" به پایان رسیده است.»
روبیو با تأکید بر اینکه آمریکا به اهداف خود دست یافته، افزود: «ما پیروزی را این‌گونه تعریف می‌کنیم: نابودی زیرساخت‌های صنایع دفاعی ایران، کاهش قابل توجه تعداد پرتابگرهای موشکی که در اختیار دارند و کاهش چشمگیر ذخایر پهپادی آن‌ها.»
او ادامه داد: «ما به همه این اهداف دست یافتیم. علاوه بر آن، آنچه از نیروی هوایی ایران باقی مانده بود را نابود کردیم و کل نیروی دریایی متعارف آن را از بین بردیم.»
با این حال قانونگذاران حزب دموکرات در این نشست موضع آقای روبیو درباره پیروزی آمریکا را به چالش کشیدند.
از سوی دیگر ایران بامداد چهارشنبه کویت را هدف حملات پهپادی و موشکی قرار داد که به گفته مقام‌های کویتی باعث کشته شدن یک نفر و زخمی شدن دست‌کم ۶۳ تن دیگر شد.
@
VahidHeadline
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/75910" target="_blank">📅 17:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75909">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پیام‌های دریافتی ساعت ۱۳:۴۵
سلام وحید همین الان بندرو زدن فکر کنم فرودگاه یا پایگاه هوایی بود صداش زیاد بود جوری که تا شهر نمایشو لرزوند
بندرعباس سمت اسلکه صدای انفجار یا بمب
وحید جان بندرعباس صدا انفجار خیلی بلند 13:45
بندرعباس رو زدن خیلی بد بود این دفعه صداش از همیشه بیشتر بود خونه لرزید
سلام ساعت 13:46 بندرعباس صدای انفجار اومد.
غرب بندرعباس
بندرعباس صدای چندین انفجار سنگین همین الان شنیده شد
همین الان بندر رو زد
سلام ، ۱۳:۴۵ صدای ی انفجار با لرزش شدید بندرعباس
سلام 13:46 صدای انفجار بندرعباس
وحید بندرو فکر کنم زدن صدا انفجار اومد
سلام همین الان قشم صدای انفجار شدید اومد
هرمزگان صدا اومد
بعدش این خبر منتشر شد:
"معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان گفت: صدا‌های شنیده شده در شهر بندرعباس ناشی از انفجار‌های کنترل‌شده مهمات دشمن است."
(گزارش درست اینه که: صدا شنیدم.
از روی شنیدن صدا نمیشه گفت "زدند"، "حمله شده" و...)
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/75909" target="_blank">📅 17:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75908">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ir1-0EVPwT6KfsVcZ0hOhhTPIvcfIUypZNRZkmLQKRQjFofsTBQnVmD985IhRViY4ApC8i4RyZjBzRrRlJ1k-8-8SsEjdVvsPCdEvV2_0RQOarkN9IsQwehf23S1LcK9JOxSSJDDF7tWMorlnxwEBXmHfszlkCzvNxBnjWKlNpZCjcc_p_KiHat1gdn_dtM02AXp-ewRCPL_Ll9F4ixaU59hDxD3zO7zcRVEjHo9TmBwol9uFZugOLSWJrdoKFgehIFLPNbbjW_9tcsy1xCNHbeAhq4bt1grIhZ9gVA_nWZnQ5EKHcsUsycSLTdnpqwzdQ3Gi9aJd3HSCSsGE5QWDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاظم جلالی، سفیر جمهوری اسلامی در روسیه با اشاره به سفرهای علی لاریجانی دبیر سابق شورای عالی امنیت ملی به مسکو گفت: سفرهای او، به جز دو مورد که خبری کردیم، بقیه محرمانه بود. یعنی هم ما و هم طرف روس، سفرها را رسانه‌ای نکردیم. فقط دو سفر اعلام شد.
جلالی به خبرآنلاین گفت، لاریجانی سفرهای محرمانه زیادی به روسیه داشت و در یک سال‌و‌نیم اخبر، هفت بار به روسیه سفر کرد. جلالی بدون اشاره به دلیل این سفرها و موضوعات مورد مذاکره گفت: «در یکی از این سفرها، طرف روس با من تماس گرفت و ابراز علاقه کرد که سفر رسانه‌ای شود و آقای لاریجانی هم مخالفتی نکردند و خبر آن منتشر شد. اما سفر آخری که در ۱۰ بهمن‌ماه ۱۴۰۴ صورت گرفت، به شکل دیگری رسانه‌ای شد.»
جلالی افزود: «ما دیدیم وقتی هواپیمای ایشان حرکت کرد، سه یا چهار هزار نفر در فلایت‌رادار آن را تماشا می‌کنند. زمانی که هواپیما در مسکو نشست، این رقم به ۳۴ هزار نفر رسیده بود. برای فلایت‌رادار، این عدد بسیار بالایی است. بعد هم یک‌سری شایعات شکل گرفته بود. در ماشینی که ایشان سوار شدند، به ایشان گفتم که این سفر را باید رسانه‌ای کنیم. پرسیدند چرا؟ گفتم با توجه به حوادث ۱۸ و ۱۹ دی، الآن عده‌ای از ضدانقلاب‌ها تلاش می‌کنند این خبر را به شکل دیگری جلوه دهند. برخی نوشته بودند که رهبر نظام به روسیه رفته یا برخی گفتند که پول‌ها را به روسیه برده‌اند و این خبرهای عجیب زیاد شده بود.»
جلالی در ادامه گفت: در ۱۰ بهمن، زمانی که علی لاریجانی با پوتین ملاقات داشت، در پایان جلسه من گفتم اگر اجازه دهید ما یک خبر کوتاه، با هماهنگی، منتشر کنیم. به این ترتیب همان دو سفر رسانه‌ای شد.
سفیر جمهوری اسلامی در روسیه همچنین گفت: پس از کشته شدن علی لاریجانی، پوتین متن پیام تسلیت خود را آماده کرده بود اما گفتیم منتشر نکند تا اول رسانه‌های داخلی خبر مرگ را اعلام کنند. [چون فعلا به مردم کشور خودمون دروغ گفتیم و ضایع میشه!]
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/75908" target="_blank">📅 17:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75907">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQ2QwON7evbFHKhcE16K-o0B5ItLMxwmw4K91btsJp9WYFpmeJ6pS22tieNoVBcgCwirWIrXUuN2EInTrTsp4QLUn-Tk8DUhITRQgDFFN4z7uGnmzKkoB6XxuuGc8fQIWrU6C9ETr-KYC5siJfesbixVh_vulcQmIq_OH7DbAMpLi5XoH5mKXktM0HpUBMwOY_SKuCX4_jrKkCHRwlhh2T0qkxOIC11I8qRm8fKRaP1XyvA5_RKVZjLYUvnxfGqeoXqP5rZbDA-HrmUeKgL8_OR6NNu12WJ-D26MKbEzbc-YRXZQ_6TVmkTfkrZSEP1iTjJIwRAoItdW4HPLKjUfSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در گفت‌وگو با پادکست «پاد فورس وان» متعلق به نیویورک‌پست گفت که جمهوری اسلامی موافقت کرده که سلاح هسته‌ای نداشته باشد، اما همزمان یادآور شد که تهران همچنان می‌تواند «نظر خود را تغییر دهد.»
او در این مصاحبه که روز چهارشنبه منتشر شد، گفت: «ما باید کاری در قبال ایران انجام می‌دادیم، زیرا صرف‌نظر از اینکه وضعیت ما [از نظر اقتصادی] چقدر خوب است، نمی‌توانیم اجازه دهیم آن‌ها سلاح هسته‌ای داشته باشند.» پرزیدنت ترامپ اما اضافه کرد که «آن‌ها از قبل موافقت کرده‌اند که سلاح هسته‌ای نداشته باشند.»
وقتی در این گفت‌وگو از پرزیدنت ترامپ سؤال شد که آیا رژیم ایران با این شرط موافقت کرده یا خیر، او تصریح کرد که «بله، آن‌ها با این موضوع موافقت کرده‌اند.»
او اضافه کرد: «منظورم این است که آن‌ها اکنون می‌توانند نظر خود را تغییر دهند، اما این یکی از چیزهایی بود که باید با آن موافقت می‌کردند و موافقت کردند، این موضوع اصلی و بزرگ بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/75907" target="_blank">📅 17:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75906">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcTjlJSSvzkmEVCRDxBFWU4xcR0mTAAiA5x1uJ_3wxqSTLwkQ54Rohj-AQwRnjBKP5j6xChO5TxW_U-pXjthgHl8Vh_6qHVOYZTUnPtUh3mZrB1fdpgekQ2Jjyo69vUSmKl80JJL1BIEKI9aORKp5VSu9AHVf92rtW0jo0G4x8Eitr-hr9fNrUEhMgym9hq4gz4uKhQ7pEg6DGVw41-R8czHCQYy04vcSaPNV6IZf892R7EuxbF2oX7vHSk-pxNoAxXu4gjWuxcUrzG8t8vts20wR-cIQfkxUCJiXnT2MlQHrKGNmKmHQOkO2lYCDg5p7Hw5Hgt2XDs5D4RJg76DCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجۀ ایالات متحده می‌گوید این کشور مصمم است مانع از تلاش ایران برای «جا زدن» افراد مرتبط با سپاه پاسداران در کاروان تیم ملی فوتبال برای شرکت در جام جهانی شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/75906" target="_blank">📅 17:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75897">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T-RE8KuFr8CcE8yPmotQJq_60rNEYhObNCv5JX_OtaI60vVrMISMeaERx-bWVesXkl0BYpII4WLX-s8IRerbfE2o8L8jxV2nNpywDo0CVMh91voyOWgvHvClyZ5awoonjQMi5DDe7rFCfVrgqqPOd2uHbd-XvDeXPRbmQJ-3z7YzRYK9xVdtRTxD3rpRIqXSMTB7GpCXYr5XsvJbWzkyrGQ-M1RHbyfUg_lqY9yePK288n2LSlCTbCqvXlYYo5aRww-70UPa5XLNpsLYazIWXeW6cKUA9Q7HvlM9kAApeADFaR0MQYqQKH7rR5_F4ohZ9UUcPO1pw7FfM5499qrZqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BTSq0n4abKiTItr7U7ur0GdTEJn4XKWJq2Ck-qDFbP6o3R0c7hcWXNzvQt3ahNZOGZFh6DUMPH0oo08zlnYW5BwqZTh1mLRHpvGFCpwr-LyCCPbR2CRlI1JJk9VaT01X6FLkNzgMfp4v3Enk7Batgi5T87ex5ZO54dhPp-n33koL49D2jxtqUgmaYrm37lU5sFId34BBML9fq9R9yOolOezPDEIbVJaXjgkcBciW0VGlm9_0fW-wPOrEkDt-tweobRN8PHN1YbtZywKKCKdMy0-K2m1zbG3XDoRVAJG3-3rzkGPRbGy_YmT2gKibNmdJCpA_V0fAD7Of2KvN59oe8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Dm4a7EFimEHRkRZ4jRj-kSdsuUB6eGrjfEJAx8G8ACqz6hQ1iE5oZEOWHyRWMGf7QJeQwJYc9YD9t0FJougqpa7GGZFFZGQSnhLvkc0i9-Zir4HZqj4jBOKLkqONyph62l1c8t_eRBs9FOITeMjjjz1miH2e2VuRa5LG-9-3MdFPh6OGfurNGDRWMBHMy9KXVGyb8Q_xUl8a9i-LcAbRXdOp5F8OLkZBLZkR_QxSkSuXgv5sRR9B1xyMA40Ty4u9TX-1hBJ7_i8aoJvjSE-d5T0JW43Z4XL2Gf3yvwYqDkaQeKi9P8eSxZmWJI7kshoL1BXe3MMBjt0h4DuU_YJLOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/icWMcuVpgEWer1w7HXrvofZqG0ImMvbCt0imNEXut8qPkgKr69SRrSwfojhHXbB3q8UzhxZp_hCV1A2AEjoYL7akEUlYSm-5jDKJHkaiiGe7RuACQwF8ZsZTvvvJIfUdvi6_MJzBLBjdTtk94e7BnrmEmEyb7Adv0d0VhPfOqNgOJxV0RE0ijsIq_rDczoLtnz_GZZiWLeYNYjElnI4jv5QIEpovJMOq8x9K-emlYV3-8rosfs1M5lC3fpzuU8PhilwB_p_cD8OJvZGOdhtBjBtRiMMzna5jbM7zkPmLjchTPXbxhyRQ34UlZFvVmkRf-agFGMKLLWSY-yvzHzCfhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i-ZxSJQRIOwfWpPRaYCpnNbxxEpcQPZGKBH0S174svhQL6EpgAm98VtjY5MV31vrZ7eV26vHKdDQwXzusIn_vwTkvtPqj6C51lk12v5YN_CyDZPEHESk2F09qpfWfFdYLbh3scZ8SXRHU_Njit3H6hyEhkyO-3sUMGmha7G59tBWXuadNQFd33xrh3uwuJWF_AJyRCByOgAUB6yW6_w3ITsHXeigENTswdq_yEapOMI5gCFgJimUK5cTxI97HkqGDyFyRveEb09c_-FEnz4i7U7Rh7Bj_ZrvPSZbT4ZyK35Db7vxqVx8S6Eyd-e97cUJFqtWRYawYj2ESqDkdh1lQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I5MlyVjXHhXb4lBg9XzJVx39GYs_3pjbqsElrzjMLwNJwbGjFwIlnGCbI6xH7yZDpHqxgZLPhSsfXGEbPqJVsKOQ8hfXcpz1eE1g8sdPk56rGM_aG_zQngHC3ZpJxkdngJq2YxdlcyAAmDBlDDNAOrcfa1Ou5WPOTD7Ue3NyPYXu8Q0HZu7xqSuaVS6y0bVtr7_iR_IyyKED8l_FYC5nVzMff6u4yhyDImcC4izDA7UJ9uaHNVd5fxGmd0WNsLvoq_6w78nirdFrwfMZjJBKniI8_0M8hwAWV7d4HbwII2yDV0SHtj7NDmA4nDT-Z6p3dxvGcYkGsdShfWzQWYb7kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DhOtnLfkcpxA4F8FzxQZdi8Bt_xCtfdlEmuZt_Hr3AOo6Nny_iVk8m8yo-KflDqjotb56TfQbOEfF4tXo0yRdif_4fSkZIOHYJUtqrJAWNA0mCsK476Qes8IWKymQqK6SUA-mfIPhuow6bne5OIICapcYHsw3c9WM0J8zlkdIBp0VkWBZPkff_cC67D7URNQ7VcKARZjgAjb7RiKK0XxvGjCi9f8IaE0AtxLleb6mUlUMQ66eAHPpyxaZWG6PYAbOWHYOtUGElH51QdljcZl_sCL32ayCnhdH8VDHZNCccsfW_jO8vQ6Ct85I95bNVpZEm5A-sJsbygufnppPcKG7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jReEeUis9ZZv4zpchW-vq17YVkRt-uWP1_AAdOJ_V0ERQxkUx-qx7h2qElysbw9TKqG9kPAUBkTnHKi86pIL90NQFkDp1A1NRqpndNikuwaiq4lGa1vHmMckpK9b5Vi88dXO7MZxQVIbdB9W8EmFDorfnw7gAE2wPGCOoH9OqvZuuslZs-kf6kQ0qamubKrm0U_ryt4PxnlEAzsTwwc7Dj_J2O1v1IB7d9W28a4ReDsGYaJUroYC8om_cjeNE-_5SkNgQTUhoiPTW4_K88as60ZedNJ2i29UzZAZA6R8kOrFaQ7mBSt2lkHXzgUlFebJDKYuRXoB86pFI4XLJA7eMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1acb519b46.mp4?token=Uxw8E-wYsFj_vFWUS4NJUp7kxHpHSxXYHo-8unsy1seFsTY7A8UrCeUpYPPzvHWSn87pcLNEUgKWS4WkWsUZbsESDxV0XhCBmnphOJwtXgJApnUP6tOoxmXbFRdVSoLGosHjRecdGF3WXsO1m6n4C0S4J82833AuR6KJHr2UkXZV_G-4OVt5GJy9LQTWRprK1EYmWmtmOjF31byYXhS_otQK-fZHmDjwB4fQCKc6_bcEKO4fCrkuzVgQChP0aeHHaxpAeaoEu1mANpoIIoo29v8N7DyhOpXwEKNPWuuTv4uHKEkmQ3TPf_LGsy07ZlRdzKtuXGbkv5S4ZGlTlYckVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1acb519b46.mp4?token=Uxw8E-wYsFj_vFWUS4NJUp7kxHpHSxXYHo-8unsy1seFsTY7A8UrCeUpYPPzvHWSn87pcLNEUgKWS4WkWsUZbsESDxV0XhCBmnphOJwtXgJApnUP6tOoxmXbFRdVSoLGosHjRecdGF3WXsO1m6n4C0S4J82833AuR6KJHr2UkXZV_G-4OVt5GJy9LQTWRprK1EYmWmtmOjF31byYXhS_otQK-fZHmDjwB4fQCKc6_bcEKO4fCrkuzVgQChP0aeHHaxpAeaoEu1mANpoIIoo29v8N7DyhOpXwEKNPWuuTv4uHKEkmQ3TPf_LGsy07ZlRdzKtuXGbkv5S4ZGlTlYckVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت خارجه کویت روز چهارشنبه ۱۳ خرداد اعلام کرد در حملهٔ پهپادی ایران به «تأسیسات غیرنظامی» این کشور، از جمله فرودگاه بین‌المللی کویت و برخی نمایندگی‌های دیپلماتیک، یک نفر کشته شده است.
وزارت بهداشت این کشور نیز اعلام کرد در این حمله دست‌کم ۶۳ نفر زخمی شده‌اند.
وزارت خارجه کویت در بیانیه‌ای که ساعاتی پس از گزارش‌های اولیه از حمله منتشر شد، مشخص نکرد که کدام نمایندگی‌های دیپلماتیک در این حمله آسیب دیده‌اند.
ساعتی بعد وزارت دفاع این کشور اعلام کرد که روز چهارشنبه ۳۰ موشک بالستیک و پهپاد را که ایران شلیک کرده بود، شناسایی کرده است.
سعود عبدالعزیز العطوان، سخنگوی این وزارتخانه، گفت: «از بامداد امروز، نیروهای مسلح ۱۳ موشک بالستیک متخاصم را در حریم هوایی کویت شناسایی و با آنها درگیر شدند. این موشک‌ها بر فراز چندین منطقه مسکونی رهگیری شدند که در نتیجه آن، بخشی از بقایای آنها سقوط کرد.»
او خبر داد نیروهای مسلح کویت ۱۷ پهپاد متخاصم را شناسایی و با آنها مقابله کردند و افزود: «این تجاوز شنیع ایران، تأسیسات غیرنظامی و حیاتی را هدف قرار داده بود.»
وزارت امور خارجه هند اعلام کرد که یکی از شهروندان این کشور در فرودگاه کویت کشته شده است و این حمله را محکوم کرد.
این وزارتخانه در بیانیه‌ای اعلام کرد: «ما بار دیگر از همه طرف‌ها می‌خواهیم که به چنین حملاتی علیه اهداف غیرنظامی پایان دهند.»
پیش‌تر، خبرگزاری دولتی کویت گزارش داده بود که حمله بامداد چهارشنبه به فرودگاه بین‌المللی این کشور چندین زخمی بر جا گذاشت، فعالیت فرودگاه را به حالت تعلیق درآورد و برخی پروازها به فرودگاه‌های دیگر هدایت شدند.
اداره کل هوانوردی غیرنظامی کویت هم اعلام کرد ساختمان ترمینال شماره یک فرودگاه در این حمله «به شدت آسیب دیده است».
شرکت هواپیمایی کویت نیز اعلام کرد پروازهای روز چهارشنبه خود را تغییر زمان‌بندی خواهد داد. با این حال، اداره هوانوردی غیرنظامی این کشور ساعاتی بعد خبر داد که پس از ارزیابی خسارت‌ها و اجرای تدابیر ایمنی، پروازهای شرکت هواپیمایی کویت از ترمینال شماره چهار از سر گرفته شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/75897" target="_blank">📅 17:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75896">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THoMtmVdgj8i3iwj0Pp4oo3k67qyEbcv7tKtlPuVdaqbexUv80z-wvPNLULmmHz2gWtSZH8g-x8hFgx92e6jFxaTgdTpyvbzSVgXwX8cAQLrd234HicZ8h7jJ50STtTie5QUNnldsT_aaPeMQsHJKQp_Ujz22_BiJDkjGF2W5FyJMCYWRR62EEFGYPX1lV1Rn7_z6JdITKuVabWM8-OJtWGBBJkOPIKrRT3hRdXDBLJ17yspFNC199-O05CjqQRIXz8sBW91574SyqfIUP8gv6RWCcmjxi6Dk-bofGDGtm9OQvxH-jB0tfkCXxWUerrYuPbMeaSDuhS8Q5FcXWg9LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان وابسته به دستگاه قضایی جمهوری اسلامی، از اجرای حکم اعدام فتح‌الله آوری، به اتهام قتل محمدجواد بخشیان، از نیروهای انتظامی در جریان اعتراضات دی ماه ۱۴۰۴ در همدان خبر داد.
خبرگزاری میزان مدعی است که در زمان دستگیری، «آلت قتاله (چاقو)، هودی مشکی و همچنین همان کتانی سفیدرنگی که در تصاویر دوربین‌های مداربسته محل حادثه مشاهده شده بود»، کشف شده است.
خبرگزاری میزان مدعی شد که آقای «آوری» دارای سوابقی چون «آدم‌ربایی»، «ضرب و جرح عمدی»، «تهدید با چاقو» و «شرکت در سرقت مقرون به آزار» بوده است.
اما خبرگزاری مهر در ۲۹ دی ماه ۱۴۰۴ و زمانی که خبر از دستگیری وی در غرب تهران داد،‌ او را «دارای سوابق کیفری و امنیتی» معرفی کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/75896" target="_blank">📅 16:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75894">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZP20OMo_FFs38l45_kOeZXymr2-gn8OCvM_Vx9KodXKdyrlwB4JA8sb2sNJsZWE2P-04FYS4KgGrVO7vT4FGxxcq7REah7sepPTXJQXEds7DTt6W8WJvHdXFZ0X0bPxqOS3DYwcsb7gwbDPhNvQIPFNKBscz3E-VZmyI7_CPoExtX4OJ535mBUoHaugcXhUgW6Qu5trB1did-szBH_nsgOTutMNSjX0oCid9DJNs8ClmI1y0_dac9ADth60Ks4kb5j7a9yQ6fv538L700-w8FlpjSHnsuM6TjX3DgXyUZ5DA-gFas7MqEv6_WGdwbZhnFbtM966aw5LarZgbO8sy6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZP20OMo_FFs38l45_kOeZXymr2-gn8OCvM_Vx9KodXKdyrlwB4JA8sb2sNJsZWE2P-04FYS4KgGrVO7vT4FGxxcq7REah7sepPTXJQXEds7DTt6W8WJvHdXFZ0X0bPxqOS3DYwcsb7gwbDPhNvQIPFNKBscz3E-VZmyI7_CPoExtX4OJ535mBUoHaugcXhUgW6Qu5trB1did-szBH_nsgOTutMNSjX0oCid9DJNs8ClmI1y0_dac9ADth60Ks4kb5j7a9yQ6fv538L700-w8FlpjSHnsuM6TjX3DgXyUZ5DA-gFas7MqEv6_WGdwbZhnFbtM966aw5LarZgbO8sy6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">.</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75894" target="_blank">📅 16:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75892">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e49979671.mp4?token=Ll7dVgdfArQyD6q29vJoWUFUUuURwV8tH-ZHYT_gh_Wc3caBn19KZKaFTg_l-OxgPvDScrG2gEnJvrForzxStSfxJT9tY6SjiCpOhFzIBu1Q4CPCtuuGo4A0FddRraFaALA8E_X_55v_eneg28fE85WCFXxlUdkTyo34qRuoau-hG87nMHaf43xl4Z8F5AeBbUa0LMRSQSCbbGkoaaGhCNZ_AS1PUdkGe-4wEjRYCIYmYRwBaP-gVHKIEpZMk825I7n_izc-RV34VdHSW4Tw9xDlKoqVk9yp9L5K6IsD4kAAsYUAK6qu-MMWgqg2Q-tk6wZbw2nlfJXl3Twnf_IQrg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e49979671.mp4?token=Ll7dVgdfArQyD6q29vJoWUFUUuURwV8tH-ZHYT_gh_Wc3caBn19KZKaFTg_l-OxgPvDScrG2gEnJvrForzxStSfxJT9tY6SjiCpOhFzIBu1Q4CPCtuuGo4A0FddRraFaALA8E_X_55v_eneg28fE85WCFXxlUdkTyo34qRuoau-hG87nMHaf43xl4Z8F5AeBbUa0LMRSQSCbbGkoaaGhCNZ_AS1PUdkGe-4wEjRYCIYmYRwBaP-gVHKIEpZMk825I7n_izc-RV34VdHSW4Tw9xDlKoqVk9yp9L5K6IsD4kAAsYUAK6qu-MMWgqg2Q-tk6wZbw2nlfJXl3Twnf_IQrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"انفجار خودرو در جایگاه سوخت‌گیری تهرانپارس"
خبرگزاری فارس و تسنیم با انتشار ویدیوهای بالا نوشتند:
سخنگوی سازمان آتش‌نشانی:
در ساعت ۶:۱۴ صبح امروز، وقوع یک مورد انفجار در جایگاه سوخت گاز واقع در بزرگراه یاسینی، مسیر غرب به شرق، بعد از سه‌راه تهرانپارس (نرسیده به پل ۱۲ فروردین) به سامانه ۱۲۵ اعلام شد. بلافاصله نیروهای دو ایستگاه آتش‌نشانی به محل حادثه اعزام شدند.
در بررسی‌های اولیه مشخص شد که یک دستگاه خودروی نیسان یخچال‌دار در حال سوخت‌گیری در این جایگاه بوده که به دلایل نامشخص و در حال بررسی، دچار انفجار شده است.
خوشبختانه این انفجار منجر به آتش‌سوزی نشده بود، اما شدت آن باعث وارد آمدن خسارات قابل‌توجهی به بدنه خودروی نیسان و بخش‌هایی از سقف و دیواره‌های جایگاه سوخت شده است.
در این حادثه دو نفر شامل راننده خودروی نیسان (حدوداً ۶۰ ساله) و یکی از متصدیان جایگاه (حدوداً ۴۰ ساله) دچار مصدومیت شدند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/75892" target="_blank">📅 08:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75891">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پیام‌های دریافتی:
شرق تهران
تهران نو صدای انفجار شنیده شد
وحید جان ۵:۵۸ صدای تک انفجار شمال شرق تهران، سنگین بود. مثل بمب بود
سمت شرق تهران یه تک صدا اومد ۵:۵۷ وحید جان
ساعت 5:56 تهران شرق یه صدایی مثل انفجار شنیدم دقیق نمیدونم
سلام، ساعت ۵:۵۷
شرق تهرانیم و انگار صدای انفجار از جنوب غربی بود
تهرانپارس صدای انفجار اومد ساعت۶صبح
منم صدای انفجار ساعت ۶ شرق تهران بیدارم کرد ولی چون ادامه نداشت فکر کردم اشتباه کردم تا پیام بقیه رو دیدم
سلام، ساکن شرق تهرانم، تهرانپارس- با صدای انفجار ساعت حدود ۵:۵۶ بیدار شدم اول فکر کردم توهم زدم، الان که پیغام‌های شما رو خوندم گویا بقیه هم شنیدن.
الان حدود ۵ دقیقه ممتد صدای آژیر میاد حالا آمبولانس یا آتش نشانی نمیدونم.
سلام، پردیس چهارشنبه ۱۳ خرداد ۶ صبح صدای مثل بمب اومد
وحید جان من تو نارمک صدای انفجار شنیدم ولی نزدیک نبود  ۵:۵۸
شرق تهران یه صدای خیلی بلند اومد ۵:۵۷
سلام تهرانپارس فلکه اول ساعت ۶ یک صداى انفجار بلند اومد و از  ساعت ۶:۱۹  تا ۶:۲۲ صداى آژیر ماشین هاى امبولانس و اتش نشانى میاد
آپدیت:
دلیل احتمالی انفجار در پست بعدی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/75891" target="_blank">📅 06:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75890">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OT-JsxBpYF8dIFYkcL6xwZB-ATTyneaa2h6aZoHaE92yckCGd6bwyx1nYJO5rsBua5LYGIkMpkC5DaEXmz1yVOmTqa-FZC-8ZV0jwItA3oxMKiKbg8nyBymYihkSGBUwcJ3pMA1Habc5X3VCTb8rwNI1yACd5C9DLjrsTao2D46tgThCeuuz_k8GGzGW5liR7zBt4RVZTdjoGD9_YJLZQdLO4zcUA4xyLjQJTwhCqEANy9d75A_qtfuMgNH9do0QsgwLCrH60LbnJt_71Vw-iAiDRobuIWZpRbHGJ6VnRpsADfVx5l46Tmd2klJ32ZHJA9gr7a1xgTYtcMAHV8ayuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌پست می‌نویسد، بر اساس گزارشی جدید، یک خلبان جنگنده «اف-۱۵ئی استرایک ایگل» نیروی هوایی آمریکا در جریان جنگ ایران در کمتر از یک ماه دو بار در کویت (آتش خودی) و ایران سرنگون شد، اما هر دو بار زنده ماند.
هویت این خلبان هرگز به‌طور علنی اعلام نشده است. مقام‌های کنونی و سابق نظامی به نشریه «های ساید ساب‌استک» گفتند که او یکی از دشوارترین پنج هفته‌های دوران خدمت یک خلبان نیروی هوایی آمریکا را از زمان جنگ ویتنام پشت سر گذاشته است.
به نوشته نیویورک‌پست، بدبیاری او از دوم مارس آغاز شد؛ زمانی که در یک حادثه آتش خودی در کویت، نیروهای دفاعی این کشور به اشتباه به سوی سه فروند جنگنده اف-۱۵ئی آمریکایی شلیک کردند.
در این حادثه، هر شش خدمه این سه جنگنده مجبور شدند با استفاده از صندلی پران از هواپیما خارج شوند و با چتر در خاک کویت فرود آیند. همه آن‌ها سالم نجات پیدا کردند.
با وجود این حادثه، به گفته پیت هگست، وزیر جنگ آمریکا، خلبانان تنها چهار هفته بعد دوباره به ماموریت بازگشتند و در عملیات بمباران اهدافی در تهران شرکت کردند؛ اقدامی که او آن را نشانه شجاعت و فداکاری این نیروها دانست.
نیویورک‌پست می‌نویسد، اما چند روز پس از آن ماموریت، بدشانسی بار دیگر به سراغ یکی از این خلبانان آمد. یک جنگنده اف-۱۵ئی بر فراز ایران هدف قرار گرفت و دو سرنشین آن در خاک ایران سقوط کردند.
این خلبان در سوم آوریل به‌سرعت نجات داده شد، اما افسر سامانه‌های تسلیحاتی همراه او زخمی شده بود و پس از آنکه ایران برای دستگیری او جایزه تعیین کرد، ناچار شد مخفی شود. او روز بعد در عملیاتی نجات پیدا کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/75890" target="_blank">📅 04:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75889">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N5AgRgyRo2FLmohPzOzol4od-I7REpgENdEG5zO1Fq5DnkZGRXmvZQwQ-dPv4jeQNoZonvYcycBVxZhjE5vGq_z3EvC4MC5q5XiD4105zk5Fj_8vH6bLKkxtmrXixDJ3iijFuZqLuAcnGQ5ZtH7mYNl_SwyNV6SNrLXWn_0VqP4Hu7wKeqS90a76fNKuYis66dhzLU3T3YtNbF8vczDGr9E8sxYNumqTiWh4agqbOk7hXkHjR8oKINCUOP8MN4TfGiKRkLcfPCYbEMgp545nZyg37FmsOYwHKiRLqwRoK2U4gha6H7zR9mfjy9hhlZtkiConuqcaNxIpCVpDsHNBRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی آمریکا در شبکه‌های اجتماعی اعلام کرد که سپاه پاسداران مدعی شده که در حملات امروز با موشک و پهپاد به مقر ناوگان پنجم آمریکا در بحرین و یک پایگاه هوایی آمریکا در منطقه ضربه زده است.
سنتکام گفت این ادعا نادرست است و تمام حملات جمهوری اسلامی به نیروهای آمریکایی شکست خورد.
@
VahidHeadline
آپدیت:‌
سنتکام توییت دیگری هم منتشر کرد:
ستاد فرماندهی مرکزی آمریکا (سنتکام) دقایقی پیش اعلام کرد که «موج دیگری» از حملات پهپادی جمهوری اسلامی که نیروهای آمریکایی در کویت را هدف گرفته بود، ناکام ماند و پهپادها به اهدافی که داشتند برخورد نکردند.
سنتکام افزود پدافند هوایی ستاد فرماندهی مرکزی ایالات متحده «با موفقیت چندین پهپاد را سرنگون کرد. سنتکام گفت هیچ یک از پرسنل و یا تجهیزات آمریکا آسیبی ندیده است.
@
VahidHeadline
(مثل دو روز گذشته در این ساعت، ده‌ها پیام دیگر از تهران دریافت کردم درباره صدای عجیب پرواز هواپیما که منجر به بیدار شدن خیلی‌ها شد.)
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/75889" target="_blank">📅 04:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75888">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XCfkPY9TVrpttN9vuiXsK8cylrP9CFHEw68EhioNoWkt_WgnwAZjISJ-bcq4KX0BBIx7zy-l_JN3qsXil2oCAmbK296O5trgQwH3Kh1JvwINWMqoBQ_2E9qjDUAbyVGAFJ8MEbeIzEbp74ZG6-UHPBgE8iWKW2jqwojzXvwZobZELlBTflwYVJZh6hvm-Swywq4F6SAexr-mTc_Gk0gxr7zaCsyfXHFic_BMmD08ND4gA562RxGDTyVD-g2AssTRNww3qaXxxKGQ30RhyVXL_Gz3c0TvioWnLUNhZXdxs_Spz0-4ldHuKO4O92PCZVWeSLuHzo2w57JPCXpv8ldR6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام از حمله به جزیره قشم پس از دفع حملات موشکی جمهوری اسلامی خبر داد
ترجمه ماشین:
نیروهای آمریکا و شرکایش در برابر رفتار تهاجمی ایران دفاع کردند
تامپا، فلوریدا — نیروهای آمریکا در تاریخ ۲ ژوئن با موفقیت چندین موشک بالستیک و پهپاد ایرانی را منهدم کردند و در پاسخ به تلاش‌های ایران برای حمله در سراسر خاورمیانه، حملات دفاع از خود را در جزیره قشم انجام دادند.
ایران چندین موشک بالستیک به سوی همسایگان منطقه‌ای شلیک کرد؛ با این حال، هیچ‌کدام به اهداف مورد نظر خود اصابت نکردند.
دو موشک ایرانی که به سوی کویت شلیک شده بودند، پیش از رسیدن به هدف سقوط کردند یا در مسیر متلاشی شدند و سه موشکی که به سوی بحرین شلیک شده بودند، بلافاصله توسط نیروهای پدافند هوایی آمریکا و بحرین رهگیری شدند.
لحظاتی پیش از آن، نیروهای فرماندهی مرکزی آمریکا، سنتکام، سه پهپاد تهاجمی یک‌طرفه را که ایران به سوی دریانوردان غیرنظامی در حال عبور قانونی از آب‌های منطقه‌ای شلیک کرده بود، سرنگون کردند.
نیروهای آمریکایی همچنین حملات دفاع از خود را علیه یک ایستگاه کنترل زمینی نظامی ایران در جزیره قشم انجام دادند.
هیچ‌یک از نیروهای آمریکایی آسیبی ندیدند. نیروهای سنتکام در جریان آتش‌بس جاری، همچنان هوشیار و آماده دفاع در برابر تجاوز بی‌دلیل ایران هستند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/75888" target="_blank">📅 03:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75887">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vnAvioFcTpYaO92TR8x--4yw_5FnH4LrRPFjh18h8X3y8MRzJR_ERdVVuBjorct7Nx9D2PV9klbrdcbuiynR6F6NSTWudOTCtlFEZNc5CBzienCD8h_23NPEs69fp01jO4s2ulyMeqfn34gRIrWC0CcO_3PDT1OacCFDDBiZfvU4s44q1Db1KXQ33z2dxQ3FnkWJyi6B9Xq1OtY10bXfX1ylRMLoXthQJpUMfNq9ROjT4nvbOKZzhNBECLNfBIsbgqyRL1ZRXDS0Cif-B3QczdZGCixXV9WydBYKlitKbsVw9LQdIs3q0lLUJsShuYJviFq0RvilxUOB1QfgHeU7og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعتی پس از مخابره گزارش‌های متعدد از حملات موشکی به نقاطی در کویت و بحرین، سپاه پاسداران با انتشار اطلاعیه‌ای رسما از حمله به پایگاه ناوگان پنجم نیروی دریایی آمریکا خبر داد.
@
VahidHeadline
بیانیه سپاه به نقل از منابع جمهوری اسلامی
"بسم الله القاصم الجبارین
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ
در اواخر شب گذشته ارتش متجاوز آمریکا یک نفتکش ایرانی را در حوالی تنگه هرمز مورد اصابت پرتابه هوایی قرار داد که این نفتکش از محل موتورخانه دچار خسارت گردید.
در پاسخ به این تجاوز و نقض مقررات تنگه هرمز شناور متعلق به دشمن آمریکایی صهیونی به نام پانایا مورد هدف موشک های نیروی دریایی سپاه قرار گرفت.
دشمن آمریکایی در تجاوزی مجدد یک دکل مخابراتی سپاه در جنوب جزیره قشم را هدف پرتابه های هوایی خود قرار داد در پاسخ به این تجاوز پایگاه هوایی و بالگردی آنان مستقر در یکی از کشورهای منطقه و همچنین مرکز ناوگان پنجم دریایی آمریکا مورد تهاجم موشکی و پهپادی نیروی هوافضای سپاه قرار گرفتند.
پیش از این اخطار داده بودیم که در صورت تجاوز پاسخ متفاوت و سنگین تر خواهد بود و همینطور اقدام کردیم. این پاسخ ها باید عبرت شده باشد.
تکرار می کنیم برهم زدن امنیت تنگه هرمز تاوان سختی برای ارتش متجاوز آمریکا خواهد داشت.
و ما النصر الا من عندالله العزیز الحکیم"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/75887" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75886">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uRpUmGrkimAzCQbUjk430oqC16sgL0Ne0hWnsjotUCSuQ-4uGA64o0nodeD40PJmQ56LGSVJpvJwroB2BnK82TUNZGspJPQPzM__gs0qS6O7BRBU7qMRx2NcGSWZ5RyG3Oe7NNmWAfnV1FevPFFbA-_cF2HemkIq7g7Ki6Kph-F5zL7Wc5kOqH9QzfkvAmzeEPKsKbxSbAOsAFOjQJqE6YRK0u_zJ6AOaDJ_7WzrRCSoFHmdxYNPz9MA6ytqpC4jX0csrpTG64CpXQUJLx_m7DMhzX7Fn21FkScerjw9qLO6nvU8VJ83IUKX-Uj0oNEoUfTD_LWrUQjHDVX2faYfyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
عکس بالا: بندر کنگان دو تا موشک شلیک شد سمت کشور های عربی 2.19
ساعت ۲:۲۰ از جم بوشهر موشک زدن
درود همین الان از جم دو عدد موشک شلیک شد به سمت خلیج فارس
از جم ساعت ۲:۲۱
دو تا موشک پرتاب شد
از جم بوشهر هم دو تا زدن
همين الان
شلیک موشک از شهرک موشکی شهید چمران جم هم اکنون
ساعت ۲:۲۳ دقیقه صبح دو موشک همزمان
آپدیت: پرتاب سوم
سومی هم پرتاب شد
یکی دیگه هم همین الان شلیک شد
۲:۲۴ از جم یکی دیگه پرتاب شد
🔄
آپدیت:
وزارت کشور بحرین دقایقی قبل از به صدا در آمدن «آژیر خطر» خبر داد و از ساکنان این کشور خواست به نزدیکترین مکان امن بروند. این هشدار پس از آن است که کویت نیز اعلام کرد مشغول مقابله با حملات هوایی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/75886" target="_blank">📅 02:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75885">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vHMP5xQQSCmadSpY1CJta3dK6RRBAvqtO8mD0K-dRSJzTWetL48TCW8HE0c0atT1LCmpxl0XkUORpgzVLZTggaBAQZsXY4D7o-o75JAMMnZn3SnzZrJcUT41eG8poYGisOVHsw2xa8QS0y8MstiVFRaYFYrd7l6pdQJOFEL4Dgd-0k-xMI4Zw6KtbIOSn4hYUdGwexKNyPDWP4ONF3J2xoPV6wEvf7BSqc-4aJoq3TbIsHPaHPWlXr6R7gQyqLWcdnRrnmiqGr5FZRahTXpT5DyXvhR-xDb5XKnwFesG7okxASLBmjLAG0HI139DHgZzGvI_CAT9l2MD6zbMAqE3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
۲:۰۷ همین چند ثانیه پیش صدای پرتاب موشک از توی خود شهر داراب شنیده شد.
الان دوباره صدای پرتاب موشک اومد
وحید سلام
یکی دیگه هم الان زدن از داراب
۲ دقیقه پیش
۲ تای قبلی هم یکیش تو هوا ترکید
آپدیت: عکس بالا
و پیامی دیگر از کویت: دوباره صدای آژیر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/75885" target="_blank">📅 02:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75884">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r39ta-kiJeUIwilJtvns4WGwRtyMzAvyQFAZaNYh8EYW5mDakgtqtMwlG7m1RrbT3VNip1dUr1KSsolRRvep6mOxJ1VR3aQKiypg4INUmuSsvr5RYRL0QMKEWlPdAtGozcBkwZFN43LYVj3VHEKhv8KmuN_N7iwFqoWs9ZsskpRCdT7q42BjTXpBeZPMGy_WXXOnQsKI7Jg0H31_Hky3hgmjBUCkdkRwYrN5GbAGbBWPrN6Kt_NKcTEmoD4RfwLvChnWE8sqA_xP80LX10aNAMANWmwIOl3b7md4TZN1jTgC2by90LjpCJ5iO-iBkUw_nLPoi1GlGPFd3w8puNFmiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از داراب در استان فارس پیام‌هایی درباره شلیک موشک دریافت می‌کنم. هم‌زمان اسکرین‌شات‌هایی هم از کویت دریافت می‌کنم که میگن هشدار اعلام شده.
چهارشنبه ۱۳ خرداد
Vahid
ارتش کویت
اعلام کرد
سامانه‌های دفاعی این کشور در حال مقابله با حملات موشکی و پهپادی خصمانه هستند.
VahidOOnLine
ستاد کل نیروهای مسلح کویت با انتشار بیانیه‌ای فوری اعلام کرد که سیستم‌های پدافند هوایی این کشور، بامداد چهارشنبه، ۱۳ خردادماه، مشغول مقابله با حملات موشکی و پهپادهای متخاصم در آسمان کویت هستند. ارتش کویت در این اطلاعیه تاکید کرد که صدای انفجارهای شنیده‌شده در مناطق مختلف، ناشی از عملیات موفقیت‌آمیز سامانه‌های دفاع جوی در رهگیری و انهدام این «اهداف متخاصم» است. مقامات نظامی کویت از تمامی شهروندان و ساکنان این کشور خواسته‌اند تا آرامش خود را حفظ کرده و به طور کامل به دستورالعمل‌های امنیتی و ایمنی صادر شده از سوی مراجع مربوطه پایبند باشند.
@
VahidOOnLine
پیام‌های دریافتی که پیش از اخبار بالا نقل کرده بودم:
سلام همین الان ساعت ۱:۲۳ دقیقه دوتا موشک از داراب استان فارس پرتاب شد
یکیش حین رفتن ترکید
همین الان داراب صدای انفجار شدید اومد و شیشه ها لرزید
کل همسایه ها ریختن تو کوچه ببینن چه خبره
وحيد همين الان اژير كويت فعال شد دوباره
٦ تا انفجار خيلي سنگين تا الان
توي اين ٣ ماه اينقد صداش سنگين نبود
سلام آژیر در کویت
۵ انفجار بزرگ در کویت نسبت به روزهای قبل بیشتره
آپدیت:
ما بین فسا و داراب هستیم
یه صدای انفجار وحشتناک اومد ولی نفهمیدیم چیشده
من داراب هستم
ما عروسی بودیم تقریبا ساعت ۱.۴۰ دقیقه بود که یه صدای انفجار اومد و سقف سالن لرزید
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/75884" target="_blank">📅 01:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75883">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پیام دریافتی تایید نشده:
صدای  انفجار روستای نخل گل قشم
سلام وحید جان
قشم صدای پایان جنگ در همه جبهه ها از جمله لبنان میاد
خبرگزاری مهر هم نوشته:
"بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/75883" target="_blank">📅 01:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75882">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f311feab7d.mp4?token=fAKthU-XaEh6ZpZuEwFWP274wUoBL7kbTwy6qJGK2UnTSICdhqBUsYRMgiNc22-iz3jy6JnQnPEz15_Ax9cN7abtNAZ0sKbssIfY6GDvABNdjAGvKmhi5_v0v1V9QWuUMJ-Mw69dkpM1XJ3tSPwMnUvoKsG5BK0KXvPSySEw2YYwU6kzbp0CttwlE_HHmh8CQ5dNd83Z6NrmhXD5KR5LraaI2A4UEolNH4jaWJHsCGFYl9pnICYdtFjtdr-zUzLzisC_s7Q4LjAidb-9fbkm7J5xExSyoGEh-jX1pzHlsyNj3HNrNmbZMgY8cs5xE1Dz6OUBZUCZyNBdegC_2b7i0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f311feab7d.mp4?token=fAKthU-XaEh6ZpZuEwFWP274wUoBL7kbTwy6qJGK2UnTSICdhqBUsYRMgiNc22-iz3jy6JnQnPEz15_Ax9cN7abtNAZ0sKbssIfY6GDvABNdjAGvKmhi5_v0v1V9QWuUMJ-Mw69dkpM1XJ3tSPwMnUvoKsG5BK0KXvPSySEw2YYwU6kzbp0CttwlE_HHmh8CQ5dNd83Z6NrmhXD5KR5LraaI2A4UEolNH4jaWJHsCGFYl9pnICYdtFjtdr-zUzLzisC_s7Q4LjAidb-9fbkm7J5xExSyoGEh-jX1pzHlsyNj3HNrNmbZMgY8cs5xE1Dz6OUBZUCZyNBdegC_2b7i0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به یک کشتی دیگر شلیک کرد.
بیانه سنتکام، ترجمه ماشین:
تامپا، فلوریدا — نیروهای آمریکا [امروز] ۲ ژوئن یک نفتکش بدون بار را که قصد داشت به سوی یکی از بنادر ایران در خلیج [فارس] حرکت کند، از کار انداختند.
فرماندهی مرکزی آمریکا، سنتکام، تدابیر محاصره را علیه نفتکش M/T Lexie با پرچم بوتسوانا اجرا کرد؛ این کشتی هنگام عبور از آب‌های بین‌المللی به سوی جزیره خارک در حرکت بود. خدمه کشتی هشدارهای مکرر را نادیده گرفتند و طی یک دوره ۲۴ ساعته چندین بار از اجرای دستورهای نیروهای آمریکایی سر باز زدند.
در نهایت، یک هواپیمای آمریکایی با شلیک یک موشک هل‌فایر به موتورخانه کشتی، آن را از کار انداخت و مانع رسیدن نفتکش به ایران شد.
سنتکام از ۱۳ آوریل اجرای محاصره همه رفت‌وآمدهای دریایی به بنادر ایران و خروج از آن‌ها را آغاز کرده است. با ادامه آتش‌بس با ایران، نیروهای آمریکا تاکنون شش کشتی تجاری را از کار انداخته و مسیر ۱۲۲ کشتی را تغییر داده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/75882" target="_blank">📅 00:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75881">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eQBKdQt6qIkt4BET4eA4r-Z6z0ISjcP7CAMdEhVSBspAO9rFy8wS6XiE8gpClhaQ-37HSSBMOwvT9l73IBtY43--liLFOCL2bLchbJo3GY7t6aQw0qQAeYWFRMrgI6RnJLhlCLMww0prC9rvvgrO7nnwdw3rd-YVA62ywSWZHnQ7JzofdRBKv0L779qSAfVjGYwOcZqhuQzsL4TH1A0Lem6v7P21X3yyp2fmtShLuYppO8h1ZaDgMEbB6zH77feqimqvGf0Ham9s5Ur29gE-F7uyGt1NcCBCINFQ0j-1-Zef1wdp6S7WS21-VU11ZiKDS-QmygALYsYCsps6DB7GIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: گزارش‌ها درباره توقف مذاکرات درست نیست
ترجمه ماشین:
گزارش‌های رسانه‌های اخبار جعلی مبنی بر اینکه جمهوری اسلامی ایران و ایالات متحده آمریکا چند روز پیش گفت‌وگو را متوقف کرده‌اند، نادرست و خطاست.
گفت‌وگوهای میان ما به‌طور مداوم ادامه داشته است؛ از جمله چهار روز پیش، سه روز پیش، دو روز پیش، یک روز پیش، و امروز.
اینکه این گفت‌وگوها به کجا می‌رسند، هیچ‌کس نمی‌داند؛ اما همان‌طور که به ایران گفتم: «وقت آن رسیده است، به هر شکل ممکن، توافقی انجام دهید. شما ۴۷ سال است که مشغول این کار بوده‌اید و دیگر نمی‌توان اجازه داد این وضعیت ادامه پیدا کند!»
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/75881" target="_blank">📅 20:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75880">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QkXcLNXXrRE5G1pjS9YQGArBbTJxMMqMduUGkuS7B1Ci8zAb86uZ3dzXiOTaBtJ5P7TuoNwYFo_yrfJGzMumbMOb1pgQT-At9kbT32M9wurPkdQpvT2t0LfnW0fls8ZBDEYIGVPSF_gv9gsldMmI2OEhdYyWIIQaWiSgsywuH-0TM4MfefnXPiwULVp4W-SnmTzMlD_ex-0RQZEqqf4YMVTskp-gz5zLVX0eh2xqAMh0vVKG2X-5Z7kjEz-lk2d7_fi4jWzdTZjfgeQKYwF3Q-HIlAsYQpun-Q9GcDJKpL_81PIn9jBxwfr-edxzNp76k8TnSzPeWrDhY_8WDKO6Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا در جلسه کمیته روابط خارجی سنا گفت که نشانه‌هایی وجود دارد مجتبی خامنه‌ای رهبر جدید جمهوری اسلامی در سطحی به شکل فزاینده‌ای در حال مشارکت در روند مذاکرات است، «اگرچه تمام ارتباطات او به صورت مکتوب و از طریق واسطه‌ها بوده است.»
آقای روبیو افزود: با توجه به اتفاقاتی که برای رهبران متعدد در آن سیستم رخ داده است، تصور می‌کنم که حضور بسیار علنی احتمالاً چیزی نیست که در داخل برای آن‌ها توصیه شود.
او همچنین در پاسخ به سناتور دموکرات کریس مورفی، کاهش تحریم‌ها در ازای بازگشایی تنگه هرمز را رد کرد و گفت که هرگونه کاهش تحریم‌ها باید پس از امتیازات عمده در مسئله هسته‌ای و اورانیوم غنی‌شده صورت گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/75880" target="_blank">📅 19:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75878">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/avLSAIRpjzdi0VpcHUTmU9farafOs3mp3XAduWq5ChyzkGVvAVNy_41qR0IF0vmELaGt6AbiCZLYFuE-QPB4983XqRv3mZ-gNChxTxjKq7Gxx-3QpgmWYWxuzothp5lh2LAftjPQ4ok3nnUk4a-Tb1-RRgEX-DHV6_y33Gy2eNWhGjyyuQfeCzSOehP-FTAZv2BCBBumxpVPlWuA2OmzvDJbHiJ5LCSJyOLOCm22uop5DuyoAFs25ZP1F5F-u4RgNYugNNKVI6hxE9yANDjzTGmYMxbdkmmq21eXkJvkoaGHB23avvohjIKgv-mVCz8s3XIM8iZtGJgqxs1A5WuBfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JHsYvGgMGNCbIlk6EDdiYnmCkzzosdM4jbZ9Xq4YS8aVGrVPxi2qLxoH2vOnoio_DW9p2oNYGFrbuPTVTh202MzNd78RbsEAWu--mwTfkqMVb87J50wFASArumaZGFzcA56W8aGa9SjhYuJjo03YDNmyO6LczZRKWcCk4m8shjZw0EIa5GSoQe2qtqQ0xqqo0NiS-KDQZBHd0oRVFElTkuFwezJ_EW3aXax-LnMn0BRSH0JFSJkGKJvLDl5mhvYR8fjeBI4PYIRBjYTEshosNmprO1FrvmndqEIfkEjWkCVgj0VudC5jTQcQ9OKMVO8jAO6Wf_lFTqbOOY7YiWVKEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکو روبیو در جلسه کمیته روابط خارجی سنا گفت: «چیزی به نام نیروی دریایی جمهوری اسلامی وجود ندارد. آنچه باقی مانده تعدادی قایق کوچک است که روی آن‌ها مسلسل نصب شده و نیروی دریایی واقعی در کف اقیانوس قرار دارد.»
او افزود: جمهوری اسلامی همچنان تعداد زیادی پهپاد در اختیار دارد. توان بازدارندگی متعارف تهران به‌طور قابل توجهی تضعیف شده است.
@
VahidOOnLine
وزیر امور خارجه ایالات متحده در جلسه استماع سنا تاکید کرد که شرط اول آمریکا برای مذاکره با جمهوری اسلامی، بازگشایی کامل و بدون قید و شرط تنگه هرمز است.
او در ادامه تاکید کرد که منظور از بازگشایی، بازگشت شرایط به پیش از جنگ و عبور و مرور آزاد تمام کشتی‌ها از این آبراه راهبردی، بدون محدودیت و مانند سایر آبراه‌های جهان است.
@
VahidOOnLine
او گفت باز کردن تنگه هرمز شرط اول آمریکاست اما صرف این کار باعث برداشته شدن تحریم‌ها نخواهد شد و رفع تحریم منوط به شرایطی خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/75878" target="_blank">📅 19:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75877">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDi7Z4JbEsA27sU_VEhp-PHmXFJ1E76cvkazfryBC-RWnkLNQfAb-SKWO5_rD0jGTrqBS2ZPP288E0A96iBJJC1sM1kjsTuR8JhXQuSBNfGq1XRhk18WNMXY4nBbk_XzE_YvGJi_PVRe4K6AAk7TMhGi-6Ia_kG8T4_zKU1L3fnN-etbtoWgglltgQojZRtUl_mOkPNk5gartCJxXAQwY6AYqnklv52CXvqYNmT2EEYDjtQFgccApWcb552HNQYlW_Dr5NRq-_LXmTlIPqmAz25LK29yWV5ZrcxfPZjXH91ddNpHdyKg8rzw_wocY8pIJQhVYAiAHUf3CV80mR77aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسراییل، در مراسم تودیع دیوید بارنئا، رییس موساد، گفت جمهوری اسلامی تاکنون به دلیل توطئه‌هایش علیه اسراییل بهای سنگینی پرداخته و سرانجام این حکومت سقوط است.
بر اساس گزارش دفتر نخست‌وزیر اسراییل که روز سه‌شنبه ۱۲ خرداد ۱۴۰۵ در شبکه ایکس منتشر شد، نتانیاهو در این مراسم گفت: «هر کسی که بدخواهی علیه اسراییل در سر می‌پروراند، بداند که توطئه‌هایش شکست خواهد خورد و بهایی که خواهد پرداخت بسیار سنگین خواهد بود. بهایی که جمهوری اسلامی تا همین‌جا پرداخته است، بسیار سنگین است. پایه‌های رژیم وحشت در ایران ترک خورده و دیگر به آنچه بود باز نخواهد گشت. من به شما می‌گویم سرانجامش سقوط است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/75877" target="_blank">📅 18:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75876">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fuvm7qASTxl9pzQMapPUGWQbgR_ykk1jNE5LXxgo3JnzO2nnzIYC2Pi-UuN-Pp9i2WJJEf-5ZLVKLKFO9yeu5Ay0N54HhOk4XESfX41kLL2FAho65RiF2hkIghm21TrfLXGMm_Gt2YkM6k5P1zErqHv_rQlz-nOGy-ejQ4LU6hiTKctgTAZIz0NJBnh7cgB4mNXsHOFbPxkV1Js5RDoZedbF_iX9pqwTFuh8mqtBlUwjlUkZ15yj2XIVZfB6Xv8hXqV1L1xFsUgsnRpi85avQCwsC1XXbxVjw46KUNtAuT3MrlSetKjngtmawkd3sFlqURKHlDdsPY6R8lohN0fzbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا در جلسه کمیته روابط خارجی سنا گفت که جمهوری اسلامی در حال دستیابی به سلاح هسته‌ای بود و اگر عملیات خشم حماسی صورت نمی‌گرفت دیر می‌شد.
آقای روبیو با یادآوری این که توانایی نظامی جمهوری اسلامی به شدت تضعیف شده، افزود که جمهوری اسلامی ایران برای اولین بار در تاریخ، بسیاری از شرایط مدنظر آمریکا برای رسیدن به توافق را پذیرفته است.
به گفته او شکاف در ساختار قدرت سیاسی جمهوری اسلامی و زمان طولانی رسیدن پیام‌ها مذاکرات را طولانی کرده است. اما طبعا اگر مذاکرات به هدف دلخواه آمریکا نرسد، ایالات متحده گزینه‌های دیگری را درپیش خواهد گرفت.
@
VahidHeadline
پیش‌تر ‌خبرگزاری فارس، وابسته به سپاه، به نقل از یک منبع آگاه نوشت که تبادل پیام بین جمهوری اسلامی و آمریکا برای آنچه دست‌یابی به یادداشت تفاهم اولیه بین تهران و واشینگتن خوانده می‌شود، دست‌کم چند روز است که متوقف شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/75876" target="_blank">📅 18:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75871">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ERqxgj7206Be7Oqu3M-pS6KDoBk7siCG9ubERB4q3xZI7aGUJGIIcOlzc-GT9kcPGJM-cXDfpUHMBhEoDA_3k1LPbfr1T9tF4KfZQPys59HliDqfCY-I97ZmwbNdzRYD8PzTMDHckiJXM-mzXH3W69hoHJusWX83vvbLm5r8A1KjpNpBRjyEUoxu6a5K8GbezRvFtlp2OI4wQRozviORpQ60PRlouC5rVUuKNx4ZN1_dQH8eKj_yLLMJ0aalf8oeJIGdpMRugcdQ3Ez0rwIFaVk08guPo0TFVKJbVZfmxUbDys0j_F3QqA9gHEXeqLAAAXtaeSXyF_0rWXC1_GlE-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/92446ed5db.mp4?token=sd-eS1UYIn46lSADpQPzNA2hdueEzWIM3pGCRgksaxiPfA3TSQ8DulUy5CG8Owzl6X5N5zLgXbo4uAInffRiV0iRSaSp3dMg13x3Y49emmt69hXwzOXWOZATgnXq7I2McQ71OcinobKXuwfr46kZCfzmDQCCcXxHoeAHH12uEUeHfPDTB6w2Bh8CLhuDgw4jAhO9wZN_zy_TSnE6Cwi97U1xZ_9NOvWps8RhDPIU1inUXz_--bAHwVQmSOKSUJl7k_s5yQxcuQz2EE-NnrRE6y8x3Y0ryqN8xcq5ml_5yeTjH1xbZkX0E1KBNO9lPnMIczmyPuh8dJYCo9LHGzgxzA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/92446ed5db.mp4?token=sd-eS1UYIn46lSADpQPzNA2hdueEzWIM3pGCRgksaxiPfA3TSQ8DulUy5CG8Owzl6X5N5zLgXbo4uAInffRiV0iRSaSp3dMg13x3Y49emmt69hXwzOXWOZATgnXq7I2McQ71OcinobKXuwfr46kZCfzmDQCCcXxHoeAHH12uEUeHfPDTB6w2Bh8CLhuDgw4jAhO9wZN_zy_TSnE6Cwi97U1xZ_9NOvWps8RhDPIU1inUXz_--bAHwVQmSOKSUJl7k_s5yQxcuQz2EE-NnrRE6y8x3Y0ryqN8xcq5ml_5yeTjH1xbZkX0E1KBNO9lPnMIczmyPuh8dJYCo9LHGzgxzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هما میرافشار، شاعر و ترانه‌سرای نامدار ایرانی، در ۸۹ سالگی در لس‌آنجلس درگذشت.
مرتضی برجسته اشراقی، با نام هنری مرتضی، سه‌شنبه ۱۲ خرداد، در اینستاگرام نوشت که خانم افشار هفته گذشته چشم از جهان فروبست، اما خانوادهٔ او با تأخیر این خبر را منتشر کردند.
این شاعر و ترانه‌سرا، که بر اساس گزارش‌ها، سال‌ها با بیماری آلزایمر دست‌و‌پنجه نرم می‌کرد، از پُرکارترین و محبوب‌ترین ترانه‌سرایان قبل و بعد از انقلاب ۱۳۵۷ بود.
هما افشار با بسیاری از خوانندگان برجسته ایرانی از جمله حمیرا، هایده، مهستی، ستار، ابی، داریوش، معین و عارف همکاری داشت.
او در سال ۱۳۱۵ در تهران متولد شد و در جوانی با علی میرافشار، پسرعموی حمیرا، ازدواج کرد. این پیوند، دوستی نزدیکی بین هما و حمیرا ایجاد کرد که به گفته خود او، جرقهٔ تولید بسیاری از ترانه‌ها و همکاری‌های این دو با هم شد.
@
VahidHeadline
هما میرافشار، روزنامه‌نگار، شاعر و ترانه‌سرای تصنیف‌های عاشقانه موسیقی دستگاهی و آثار به یادماندنی پاپ، در ۸۹ سالگی درگذشت؛ چهره‌های نامدار موسیقی و علاقه‌مندانش در شبکه‌های اجتماعی از مقام هنری او تجلیل کردند.
او در سه مجموعه شعری بیش از هزار سروده دارد که افزون بر ۲۵۰ شعرش در زمره ماندگارترین ترانه‌های ایرانی است و بی‌دلیل نیست که در جامعه موسیقی به «زن هزار ترانه» و یا «ملکه ترانه‌سرایی ایران» معروف شد. از همین روست که ایرج جنتی عطایی، ترانه‌سرای برجسته معاصر، هما میرافشار را پیشکسوت خود می‌‌داند که «پیش از ترانه نو و در کنار آن شهره بود.»
هما پیشگام سرودن اشعاری بود که یک زن برای معشوق می‌خواند و یا حرف‌های عاشقانه‌ یک مرد برای دلبرش، چرا که تصنیف‌سرایان آن دوران به جنسیت ترانه‌ها کمتر می‌پرداختند. او سال‌ها پیش در برنامه «یک‌ حرف و دو حرف» رادیو بی‌بی‌سی به زنده‌یاد محمود خوشنام، پژوهشگر موسیقی، در این باره گفت: «منیر طاها، سیمین بهبهانی یا لعبت والا که کار می‌کردند، من ندیدم که ترانه‌هایشان بوی زنانه بدهد مگر این که از زبان مرد بیرون آمده باشد. اگر خواننده آنها مرد بوده به ناچار باید چیزی را می‌نوشتند که یک مرد به یک زن بگوید.»
«یادم می‌آید که یکی از من پرسید که شما این حالت را چگونه می‌نویسید و من در پاسخ گفتم اگر بخواهم از زبان مرد شعر بگویم، مشتاق شنیدن همان‌هایی هستم که دوست دارم از او بشنوم. آن حرف‌ها را می‌گذاردم در کلام و اکبر گلپا می‌خواند، یا می‌دادم به محمودی خوانساری می‎‌خواند اما گاه طوری می‌نوشتم که مرد یا زن هر کدام بخوانند فرقی نکند.»
....
در ابتدای دهه پنجاه بود که اشعار هما میرافشار و ملودی‌های زیبای محمد حیدری در صدر جدول بهترین‌ ترانه‌ها قرار گرفت و نام هما درخشید؛ مثل ترانه «دیوونتم» با اجرای حمیرا: «بذار بگم دیوونه‏‌تم...آره دیوونه‏‌تم من...نشکن منو به سنگ غم... چراغ خونه‌تم من...» یا ترانه «دلم می‌خواد» با اجرای هایده: «دلم می‏‌خواد که روزی صدهزار بار... بهت بگم دوست دارم عزیزم...» و یا ترانه «میکده» با صدای اکبر گلپایگانی: «هوس میکده داره دل دیوونه‏‌ی من، نمی‌‏دونه بی‏‌تو ایام بهارو چه کنه...»
...
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/75871" target="_blank">📅 18:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75870">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NCY1ZRYr83l3fHOoz68xJRktNzU4kGNUKa1NM-gFo2gO36h7gkv5D82vsqbW6Ib5YR7ZZTrB9OVJ1joHoqA_3yDbZ0Cq3NJSYNayyaj-VsvwKNdXS3NHr2HUq2hESsHiqFxFD0C_Bdkef0NRypaUCQDXVg3d4L6Zs6Q0981uErV-WuHTXs2skosSMzFCpHA0euiqjQp8IEtADPBSnnpr4cwIiQiYq_rik44xa2ZgolDhmLX4PRXM4IeadewSpww_biCqlVq42kJh7OlQatfv8qymXYVmAjnaegJBGXvcwn5CSI3zHP5R8aHZ_FDtFdZBeD5dmtuQDzNymNb6Ri0xrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/75870" target="_blank">📅 17:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75869">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAILd_HCfbqW8yeCZKldumpds7vqKsfmgwhx7BZRXITM1RThsbwjhWbQcdiqO5_ftL1bJiPF3i8seUbTojFdoJU0Ls2DBm6rQZ103aQqInPxvxwUkUHE67AD4jr6NrsF0vU_cbVB5l_wzTJfjK6SIUOLxfRrUdRk1g6BLYcgeOO8500tTxvDyR03lq8Ek1rieAXNo3i7zrvzX7P-XblnF6vJJlHnfsDps5cHQIR31A1vAAbI55Bwsu-fB7dheRIpRYQOMayF7ylEs4LbL2xiilkEwUNxrYXIqMBfG4XwxtuNGcCzbSpCGkxu4_py938i_Ai3K_2X7OAUnx2S95ZflQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام شهرداری تهران می‌گوید که برگزاری «مراسم بدرقه» و تشییع جنازهٔ علی خامنه‌ای، رهبر کشته‌شدهٔ جمهوری اسلامی، در شهرهای قم، مشهد و تهران «قطعی شده است».
به گزارش رسانه‌های ایران، محمدامین توکلی‌زاده معاون اجتماعی شهرداری تهران روز سه‌شنبه ۱۲ خرداد گفت که این نهاد «در حال تدارک برای حضور جمعیتی بیش از ۱۵ تا ۲۰ میلیون نفر در تهران هستیم».
او به زمان دقیق برگزاری این مراسم اشاره نکرد ولی گفت که احتمالا در پایان ذی‌الحجه و اوایل محرم برگزار شود.
این زمان تقریبا مصادف با اواخر خرداد و اوایل تیرماه است.
علی خامنه‌ای از ۹ اسفند پارسال که در حملات مشترک آمریکا و اسرائیل کشته شد، هنوز دفن نشده است.
معاون اجتماعی شهرداری تهران در ادامه گفت که «مراسم بدرقه» سه روز در نظر گرفته شده و در تهران قرار است ۲۴ ساعت طول بکشد.
به گفته توکلی‌زاده، محل دفن خامنه‌ای «طبق وصیت ایشان و توصیه‌های نزدیکان‌شان» در حرم امام هشتم شیعیان تعیین شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75869" target="_blank">📅 17:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75868">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5BTCQ8b-yMdEQAlAczQhVP3bIvdT762l23FA88w5jxDHvVEE4th8ElWDfwRazWS4212Qvwo8c2Dy6R01U3zQj11JFKY33n6e63xRIoo2sBEf29m_mWf5rFNsljYFtGZfCuVgzBeH4T0KXS9DQkRlOBcMaQYVF8PdScxzR1czZFKKtEx4jogQeDvyXmSHpy6HApr6xz03N4Q20SFzjVBRn2fvRPTM_mKQnCNPP298Jt8gJKMrFQDBwkUhVWFmekhoLectYfu5Um74r3COGm2b5GMHvjPpu8J83GecF1JF1f2WGoOygHMFuJXiY-sNCdiNLMGEyLnCxoSyDtuxCDvEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از چند روز تاخیر، بانک مرکزی و مرکز آمار ایران به‌طور همزمان گزارش‌های تورمی اردیبهشت‌ماه را منتشر کردند؛ گزارش‌هایی که با وجود تفاوت در ارقام، از تداوم روند صعودی قیمت‌ها و افزایش فشار معیشتی بر خانوارها حکایت دارد.
مرکز آمار ایران تورم ماهانه خانوارهای کشور را ۸.۸ درصد، تورم نقطه‌به‌نقطه را ۸۳.۹ درصد و تورم سالانه را ۵۷.۷ درصد اعلام کرد.
همزمان بانک مرکزی با تمرکز بر مناطق شهری، تورم ماهانه را ۸.۵ درصد، تورم نقطه‌ای را ۷۷.۲ درصد و تورم سالانه را ۵۳.۹ درصد برآورد کرد.
بر اساس گزارش بانک مرکزی، شاخص کالاها در اردیبهشت‌ماه نسبت به ماه قبل ۱۰ درصد و نسبت به مدت مشابه سال گذشته ۱۱۳.۸ درصد افزایش یافته است؛ آماری که از رشد شدید هزینه خرید اقلام روزمره حکایت دارد.
اختلاف ارقام منتشر شده از سوی دو نهاد آماری به تفاوت در جامعه آماری، سال پایه، شیوه نمونه‌گیری و وزن‌دهی کالاها و خدمات بازمی‌گردد. مرکز آمار کل خانوارهای شهری و روستایی را مبنا قرار می‌دهد، در حالی که بانک مرکزی تنها مناطق شهری را بررسی می‌کند.
مقایسه آمارها با ماه‌های گذشته نیز از شتاب گرفتن روند تورمی خبر می‌دهد. تورم نقطه‌به‌نقطه که در فروردین‌ماه ۷۳.۵ درصد اعلام شده بود، در اردیبهشت به ۸۳.۹ درصد رسید؛ افزایشی بیش از ۱۰ واحد درصدی تنها در یک ماه.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/75868" target="_blank">📅 17:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75867">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/695f2e3957.mp4?token=X0VTviEw10y0QtM9VKLiiQB7aLIT-0S48OIemIC8QrW8HtOSytJ5fasqdmx1O_KfI7isy4GRAdiphVKljgDE9WXCZ58kiS5WZ1pNJKk251NCEd2JMD1rBqmFM6I3fM9zaXnkkjIG537ES5tp10Y0sLpHxXxhWiz0Oiw4zyuIaRK6zBIC3iJPHBizrbJtyMj7Zwt27OILgtodHLvpzljpwpR5borp5mD_eHOt-XaB1K8e3A4_k68kGAAZpm_K-AETg5bY3p_9Gw5LNF0VyqnqRG9Vrm9xJrAqMeFQ2APU9TfXQexIAHm3Dy0p-yt0qQGUCRibRN2FoqG5XHmdOeJsGg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/695f2e3957.mp4?token=X0VTviEw10y0QtM9VKLiiQB7aLIT-0S48OIemIC8QrW8HtOSytJ5fasqdmx1O_KfI7isy4GRAdiphVKljgDE9WXCZ58kiS5WZ1pNJKk251NCEd2JMD1rBqmFM6I3fM9zaXnkkjIG537ES5tp10Y0sLpHxXxhWiz0Oiw4zyuIaRK6zBIC3iJPHBizrbJtyMj7Zwt27OILgtodHLvpzljpwpR5borp5mD_eHOt-XaB1K8e3A4_k68kGAAZpm_K-AETg5bY3p_9Gw5LNF0VyqnqRG9Vrm9xJrAqMeFQ2APU9TfXQexIAHm3Dy0p-yt0qQGUCRibRN2FoqG5XHmdOeJsGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدها دانش‌آموز روز سه‌شنبه ۱۲ خرداد با تجمع مقابل وزارت آموزش و پرورش در تهران، به تغییر قوانین کنکور، افزایش تأثیر معدل و پیامدهای جنگ بر آمادگی برای آزمون سراسری اعتراض کردند.
در ویدئوهای منتشرشده در شبکه‌های اجتماعی، شعارهایی از جمله «دانش‌آموز بیداره، از تبعیض بیزاره»، «دانش‌آموز می‌میرد، ذلت نمی‌پذیرد»، «وعده زیاد شنیدیم، عدالت و ندیدیم» و «فشار روانی کافیه، زندگی‌مونو پس بدین» شنیده می‌شود.
سیاست‌های مرتبط با کنکور از جمله افزایش تأثیر معدل و تغییر در شیوه برگزاری و زمان‌بندی آزمون‌ها، در کنار شرایط ناشی از جنگ، در ماه‌های اخیر با تغییرات و ابهام‌هایی همراه بوده که به گفته داوطلبان، موجب سردرگمی و دشواری در برنامه‌ریزی برای امتحانات نهایی و کنکور شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/75867" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75866">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kjfy3TF9cbe0u02PUOvPgWYqgpvREG95mGFPcKuEVYU2ZLj9yD9H28cIYcOWBSZ6TNuDlXe1Nw6VGClP8VhxIO5gaBgmqfJGuQP1v507t5IH98YRjKOnwlsMP5MpU6V8YaGA9FxYh0tgi7qIGY6LX9s5RGRSko7SHFCIkEDuoiQ39RWqxeXlplmWDmGjDH_EcjxJbyLBNNT2aixhHHakQ8CFCLrUhCpBdiz-2tcnV6FfSLcgO_OK8HNfueBeFldFCmOydkxDDtcZ2b1KFEWfME57KTHAmL0qs-eLBt2yfOVXw2Brm8wuzXAL6AWsrrHQSXQzFX9tWJhEQy_GSWs2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ برای سومین بار این متن رو علیه بعضی از رسانه‌ها پست کرد.
ترجمه ماشین:
اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در کف دریا آرام گرفته، و نیروی هوایی‌اش دیگر در میان ما نیست؛ و اگر تمام ارتشش از تهران بیرون بیاید، سلاح‌ها را زمین بیندازد و دست‌ها را بالا ببرد، در حالی که هرکدام فریاد می‌زنند «تسلیمم، تسلیمم» و دیوانه‌وار پرچم سفیدِ نمادین را تکان می‌دهند؛ و اگر همه رهبران باقی‌مانده‌اش تمام «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم ایالات متحده باشکوه آمریکا بپذیرند، نیویورک تایمزِ رو به افول، چاینا استریت ژورنال — یعنی وال‌استریت ژورنال! — سی‌ان‌انِ فاسد و حالا بی‌اهمیت، و همه اعضای دیگر رسانه‌های اخبار جعلی، تیتر خواهند زد که ایران یک پیروزی استادانه و درخشان بر ایالات متحده آمریکا به دست آورد؛ اصلا هم رقابت نزدیکی نبود. دموکرات‌های احمق و رسانه‌ها کاملا راهشان را گم کرده‌اند. آن‌ها کاملا دیوانه شده‌اند!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/75866" target="_blank">📅 05:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75865">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">باز هم صدای غیرمعمول پرواز یک هواپیما خیلی‌ها رو در تهران از خواب بیدار کرد.
پیام‌های دریافتی:
صدای هواپیما سعادت آباد
سلام، تهران صدای توافق میاد فکر کنم
صدای جنگنده یا هواپیما ۰۴:۰۹ غرب تهران
دوباره همین الان دقیقا ساعت ۴:۱۰ صدای شدید تر جنگنده غرب تهران
سلام تهران صدای جنگنده میاد چخبره؟؟!
مطمئن نیستم ولی غرب تهران فکر کنم صدای هواپیما یا جنگنده اومد
تهران سمت  سعادت اباد صدای جنگنده میاد
خیلی پایین بود صداش
همین الان تهران صدای کلی جنگنده اومد ک رد شدن
خیلی بلند بودن
صدای جنگنده غرب تهران
ساعت۴:۱۰صبح صدای جنگنده سمت شمال غرب میاد
تهران جنت اباد 4 09 صدا جنگنده اومد
4 و ده دقیقه صبح بالا سر شهرک نفت پونک جنگنده اومد آنتن قطع شد و وصل شد
همین الان غرب تهران حدود ۲ دقیقه صدای جنگنده اومد
دقیقن ده ثانیه پیش ساعت ۴:۱۰ ‌صبح یک‌هواپیمای از همونایی که موقع جنگ از بالا سر خونمون رد می شد
تهران حدود ساعت ۴ یه هواپیما مسافربری رد شد صداشم زیاد بود
هیچ وقت از این مسیر رد نمیشه!
توی فلایت رادارم نیست
شهرک‌ غرب ۴:۱۰
صدای جنگنده او‌مد
سلام وحید جان . ساعت حدودا ۴ و ۵ تا ۴ و ۱۰ دقیقه صبح شمال غرب تهران صدای مهیب جنگنده اومد. کاملا مشخص بود تو ارتفاع پایین داره پرواز میکنه . البته نه پدافند عمل کرد نه بعدش انفجاری شد. احتمالا برای نیرو هوایی ایران بوده
امروز سه شنبه دوازده خرداد ساعت ۴و۱۳دقیقه صبح صدای هواپیمای باری یا مسافری اومد چون چراغهای کابین و چشمک زن روشن بودن، مسیرش رو دنبال کردم مهرآباد ننشست تا جنوب تهران ادامه مسیر داد، صداش عین هواپیمایی بود که دیروز دوشنبه ساعت ۹و۱۵دقیقه صبح ، بسیار طولانی و ممتد حرکت می کرد به سمت  شمال ،چون از  کوه های البرز رد شد
صدای جنگنده نبود غرب تهران
یه هواپیمای خیلی بزرگ بود که اونقد پایین پرواز میکرد احساس کردم الانه که بخوره به ساختمون روبرویی خیلی بزرگ بود هواپیماش و خیلی پایین
پنجره باز بود دم پنجره خوابیده بودم صداش شبیه جنگنده نبود مابین جنگنده و پهپاد بود
همچین قیرقاژ داد رفتم رو هوا
سمت پونک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/75865" target="_blank">📅 04:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75864">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پیام‌های دریافتی درباره قطع شدن موقت خطوط تلفن همراه در بعضی از شهرهای استان‌های فارس، بوشهر و هرمزگان و...
از حدد ساعت ۲
▪️
شیراز کلا قطع شده انگار
نه میشه زنگ زد نه میشه کاری کرد
▪️
کل تلفن های همراه توی شیراز قطع شده
تمام اینترنت ها قطع شده
مشخص نیست چرا اینجوری شده
نه ایرانسل نه همراه اول نه رایتل آنتن نداره
▪️
وحید از حدود ساعت ۲:۱۰ تا همین الان انتن گوشی ها و اینترنت خانگی و هر چیز مخابراتی توی شیراز پرید
همین الان [۲:۳۰] همراه اول وصل شد با سرعت کم. ایرانسل وصل نیست
▪️
شیراز خط گوشی بیشتر از ۲۰ دقیقه رفت
از ساعتای ۲:۱۰ دقیقه تا ۲:۳۰
ایرانسل هنوز نیومده
آپدیت:
ایرانسل هم وصل شد
ولی همگی 3G  هستن
سلام وحید جان بندرخمیر هم از ساعت 2 همه چیز قطع شده الان به زور وصل شدم بهتون اطلاع بدم
اصفهان هم دقایقی خط همه رفت
تو شیراز یک دفعه همه انتن ها پرید. حتی نت مودم خونه مون هم کاملا قطع شد
الان بعد از حدود نیم ساعت دوباره انتن ها اومد
وحید فکر کردم فقط واسه من اینطوریه نت خونگی مبینت ما هم قطع شده خوزستان سربندر
از شهرستان های فارس نیم ساعت همه انتن ها رفت و اینترنت مخابرات هم کار نمیکرد الان اینترنت مخابرات اومد و انتن همراه اول هم با سرعت کم اومد ایرانسل قطعه
نت و انتن و... کامل توی بندر ماهشهر پریده
اهواز هم همینطور
سلام بندرگناوه چند دقیقه کلا همه چی قطع نه زنگ نه حتی شبکه داخلی همه چی بسته شد
بندر ساعت ۲ بامداد تقریبا آنتن ها رفت
و بعد برگشت خط 3g شده اما اینترنت کار نمیکنه
الان فقط اینترنت فیبر وصل شده
دقیقا راس ساعت ۲ کل دیتا سنتر شیراز قطع شد
تلفن همراه کاملا بدون آنتن
تقریبا ۳۰ دقیقه شد که وصل شد
همین الان حدود نیم ساعت در نورآباد ممسنی همه چی پریددد نت و آنتن و خط و همه چی
😐
شیراز از ساعت 2 تا 2:30 انتن همه اپراتور ها قطع شد
بندرعباس هم همینطور، قطع شد وحید جان تا الان
اینترنت و انتن های تلفن همراه تو قشم کلا قطع شد یهو
تقریبا ۱۰ دقیقه قطع شد
هم انتن هم اینترنت همراه
بوشهر اینترنت مخابرات و ایرانسل هی ده دقیقه ده دقیقه قطع میشه
خیلیاهم کلا قطع شدن از اشناهام
شیراز بعد از نیم ساعت وصل شد
کل سرویس های ایرانسل و همراه اول و شاتل حتی اینترنت مخابرات قطع بود
خط  ایرانسل هم برگشت
وحید سلام و خسته نباشی، اینترنت و خطا برای ده دقیقه کامل قطع شدن هم بوشهر هم بندرعباس، بوشهر وصل شده و نت همراه ضعیفه منتهی بندرعباس اینترنت ایرانسل قطع شده
وحید اصلا همه‌ی استان فارس همین شد
من فسا هستم منم قطع شدم
دقیقا از ۲:۰۲ تا ۲:۳۶ قطع شدم
وحید بوشهر هم کلا قطع شد الان وصل شده و خیلی ضعیفه یه نیم ساعتی کلا آنتن نبود
میناب هم یه ۲۰ ۲۵ دقیقه ای کلا انتن نبود
بندرعباس: ایرانسل کلا قطعه، همراه هم قطع و وصله
سلام اقا وحید داخل بندر دیلم استان بوشهر ما از ساعت ۱:۴۵ دقیقه هیچی انتن نداشتیم چه ایرانسل چه همراه الان درست شد تازه نت رو h هست
با تمام سیم‌کارت‌ها ما الان وصل شدیم
مرودشتم کامل قطع شده بود همه چی الان وصل شد
سلام وجید جان
ما برازجان هستیم
برای ما هم نت ایرانسل، همراه اول و رایتل و مخابرات کلا قطع شد
الان که برگشتن 3G هستن
سلام از جنوب استان فارس پیام میدم اینترنت خانگی و همراه و همچنین آنتن از ساعت ۲ تا حدود ۳۰ دقیقه کاملا قطع بود
بوانات برا یه نیم ساعتی انتن پرید
سلام توی یزد هم آنتن همراه اول کلا قطع شد، فکر کردم باگ گوشی خودمه، اما الان که گزارشات رو دیدم ظاهرا چیز دیگه ای بوده
درود وقت بخیر شیراز حدود ۲:۱۰ دقیقه کل خط ها انتن و اینترنتشون پرید و بعد از حدود نیم ساعت با سرعت بسیار کمی وصل شد
تشکر وحید جان
سلام وحید خط بستک و کل غرب استان هرمزگان بعد ۲۰ دقیقه وصل شد
سلام وحید جان بندرعباس الان 45 دقیقس که همه چی قطعه آنتن ایرانسل اومده ولی روشن نمیشه همه چی پریده فقط فیبر نوری وصله فعلا
سلام وحید جان :استان بوشهر :کنگان از ساعت ۲:۲۳نت ایرانسل و مخابرات پریده و هنوز وصل نشده خدا میدونه چیکار میکنن.
شهرستان
قیر و کارزین
هم ایرانسل هم همراه وصل شد اما مودم مخابرات از ساعت ۲ قطع
درود. از لاهیجان پیام میدم. اینجا هم امروز اینترنت مخابرات دو بار برای چند دقیقه رفت و بعدش با سرعت خیلی کمی وصل شد.
اصفهان هم حدود ساعت دو انتن قطع شد‌ ولی چند دقیقه بعد برگشت
سلام داخل اهواز کل آنتن ها قطع شد و سریعا به حالت قبل برگشت
مجدد همه چیز پرید توی بندر ماهشهر باز الان وصل شد
وسط بازی بودم پرید بیرون انتن رفت فکر کردم خودم اینجوری ام  از ساعت دو
الان وصل شدم دیدم بچه ها هم نیستن هیچ کدوم نوراباد ممسنی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/75864" target="_blank">📅 02:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75863">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pmHjwUlhhwKjXkO8z3VEyFhkDae7ZJkarE0-7YWgkvPqAKZekfWp3E36wOyKFER9z_HTAxILefbb3K4SVlv76k2RySpHjeOb-0-D6D7fF8V_Za7D7g7-YXRfSIAe4CtsJsPhhd7B6k8QqkeBMVx34PgDnJs3l5i9GqjzOXlHkJFIr-VllS9JS1GllvUp2_A7hnwZ1jUHhNNJZgiPN_OBDc18_e819dWYfPY1X1eWEKizu0KnJj4Nbfug7BhgwTJzmbYdyrIz62-qFNuTia5RUscMK8llVCD3emduqvQ6c-_5agibwVXls5_rqf2sotVuMur0GsYXKUDBJtmC-DkVXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در گفتگوی تلفنی با شبکه خبری «ای‌بی‌سی نیوز» اعلام کرد که به نظر او، توافق با تهران برای تمدید آتش‌بس و بازگشایی تنگه هرمز «طی هفته آینده» حاصل خواهد شد.
ترامپ روز دوشنبه در گفتگو با جاناتان کارل، خبرنگار ارشد این شبکه در واشنگتن، با ابراز خوش‌بینی گفت: «اوضاع خوب به نظر می‌رسد.»
رئیس‌جمهوری آمریکا با اشاره به تنش‌های اخیر افزود: «امروز مشکل کوچکی پیش آمد، اما همان‌طور که احتمالا پیش‌تر متوجه شدید، من خیلی سریع آن را برطرف کردم.»
او توضیح داد که این مشکل ناشی از ناراحتی و عصبانیت مقام‌های ایران از حملات اسرائیل به لبنان بوده است؛ ترامپ در تشریح نحوه حل این بحران گفت: «من با حزب‌الله صحبت کردم و گفتم تیراندازی نکنید؛ با بنیامین نتانیاهو، نخست‌وزیر اسرائیل هم صحبت کردم و گفتم تیراندازی نکنید، و هر دو طرف شلیک به یکدیگر را متوقف کردند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/75863" target="_blank">📅 01:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75862">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B0sJxTJQLnToeBuS5w7QWGsH8aKyIlPAEKfLMy4kgMfDsj5Vd83wwse00fcsyUHwmL0zPymU5NB2kulFoMYDyxlYjDbfRMGPwGGEFJpHAD805XWo6irnliJbtc5_fHSgJavKTq2pcAIbsL5_cqHkbj3tGdoPAGZuRAZw6fdTCqELlCzGz1Xa5FJK9-3DQ5I7jz9O2sfNqqG_6C_vTGbJ6Q6Z4kMqFq4JmQfkwCZ5HwEOv4FWtlt-p-_XHkbCUOXasXKGImeAFVfXqKfzVW_LgfAzIqy1_tudclKTNzwwH62O-hFKVnoicA80I_24BaZL-Hi85HUeXSfUzJhr9iGOFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
امروز با بی‌بی نتانیاهو گفت‌وگویی داشتم و از او خواستم وارد یک حمله بزرگ به بیروتِ لبنان نشود. او نیروهایش را برگرداند. ممنون بی‌بی!
همچنین با نمایندگان رهبران حزب‌الله گفت‌وگو کردم و آن‌ها پذیرفتند که تیراندازی به اسرائیل و سربازانش را متوقف کنند. به همین ترتیب، اسرائیل هم پذیرفت که تیراندازی به آن‌ها را متوقف کند.
ببینیم این وضعیت چقدر دوام می‌آورد — امیدوارم تا ابد ادامه داشته باشد!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
خیلی شبیه به
پست چند ساعت پیش
ش به نظر می‌رسه. به نظر می‌رسه همون رو بازنویسی کرده ولی قبلی رو حذف نکرده.
نظر چت‌ جی‌پی‌تی:
در اصلِ پیام، تفاوت محتواییِ بنیادی ندارد:
هر دو می‌گویند ترامپ با نتانیاهو صحبت کرده، نیروهای اسرائیلی از رفتن به بیروت منصرف شده‌اند، و از طریق نمایندگان/واسطه‌ها با حزب‌الله هم درباره توقف درگیری صحبت شده است. گزارش‌های خبری هم نسخه اول را با همین مضمون منتشر کرده‌اند.
اما متن دوم از چند جهت مهم بازنویسی و تنظیم‌شده‌تر است:
۱. ترامپ نقش خودش را پررنگ‌تر کرده
در متن اول می‌گوید:
تماس بسیار سازنده‌ای با نتانیاهو داشتم و نیروها به بیروت نمی‌روند...
اما در متن دوم می‌گوید:
از نتانیاهو خواستم وارد یک یورش بزرگ به بیروت نشود. او نیروهایش را برگرداند. ممنون بی‌بی!
یعنی متن دوم بیشتر این برداشت را القا می‌کند که ترامپ شخصا جلوی حمله بزرگ به بیروت را گرفته و نتانیاهو به درخواست او عمل کرده است.
۲. عبارت «حمله/یورش بزرگ به بیروت» اضافه شده
در متن اول فقط می‌گوید:
نیروها به بیروت نمی‌روند.
در متن دوم می‌گوید:
وارد یک major raid of Beirut, Lebanon نشود.
این مهم است، چون متن دوم وضعیت را جدی‌تر و عملیاتی‌تر تصویر می‌کند: نه فقط «نرفتن نیروها»، بلکه جلوگیری از یک عملیات بزرگ در بیروت.
۳. تماس با حزب‌الله با احتیاط بیشتری بیان شده
متن اول می‌گوید:
I had a very good call with Hezbollah
یعنی ظاهرا «تماس خیلی خوبی با حزب‌الله داشتم».
اما متن دوم می‌گوید:
I also had a conversation with Representatives of the Leaders of Hezbollah
یعنی «با نمایندگان رهبران حزب‌الله صحبت کردم».
این تغییر احتمالا برای این است که مستقیم نگویند ترامپ با خود حزب‌الله «تماس خیلی خوب» داشته؛ متن دوم آن را رسمی‌تر و غیرمستقیم‌تر می‌کند.
۴. تعهد حزب‌الله محدودتر و دقیق‌تر بیان شده
در متن اول:
all shooting will stop — Israel will not attack them, and they will not attack Israel
یعنی «همه تیراندازی‌ها متوقف می‌شود؛ اسرائیل به آنها حمله نمی‌کند و آنها به اسرائیل حمله نمی‌کنند.»
در متن دوم:
they agreed to stop shooting at Israel, and its soldiers. Likewise, Israel agreed to stop shooting at them.
اینجا حزب‌الله مشخصا متعهد می‌شود به اسرائیل و سربازانش شلیک نکند و اسرائیل هم به آنها شلیک نکند.
تفاوت ظریف این است که متن اول از «attack» استفاده می‌کند که گسترده‌تر است؛ متن دوم بیشتر روی «shooting» تمرکز دارد که ممکن است محدودتر از «حمله» باشد.
۵. متن دوم تردید و شکنندگی توافق را اضافه می‌کند
متن اول قاطعانه تمام می‌شود. اما متن دوم اضافه می‌کند:
Let’s see how long that lasts — Hopefully it will be for ETERNITY!
یعنی: «ببینیم چقدر دوام می‌آورد؛ امیدوارم برای همیشه باشد.»
این جمله نشان می‌دهد ترامپ خودش هم دوام توافق را قطعی نمی‌داند و بیشتر حالت آرزویی/نمایشی به آن می‌دهد.
جمع‌بندی کوتاه
متن اول بیشتر شبیه اعلام رسمی یک توافق فوری است.
متن دوم بیشتر شبیه بازنویسی سیاسی‌تر و شخصی‌تر همان پیام است؛ در آن ترامپ نقش خودش را برجسته‌تر کرده، تماس با حزب‌الله را غیرمستقیم‌تر توصیف کرده، عبارت «یورش بزرگ به بیروت» را اضافه کرده، و در پایان هم درباره دوام توافق تردید نشان داده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/75862" target="_blank">📅 01:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75861">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dosl9dpxMYfg1_qdZX2d5hbO9ZKrkAfcq-qXtyrMeiL0etaTaTW03G_QAerS5CGCrDU_-ch6glffDYs3fco6Vnm5AlC84VLOcUc8Y_nlXJ509hUIT9aif6BZEKykv5pfvxvgwDoGO3eOZfYhhNCqy0sF3y5rf6CtEjF7lw_V9nEHSRoz9eMADHapVy3euG59BnZfvJaDigIDKmW1Ke_Uq_r6q3RpAWOiqaBhbpzwdXZPPDR5z-f1Omb_8I0v7WlQJm79HwYnnmDPcHbgk3zUKo2VLcAeI_M6OIikHHRGAqL9_-F2wFABSvOq_igvigmtjfzknlN67KNDFFnFIyrRFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری جمهوری اسلامی، ایرنا، روز دوشنبه ۱۱ خرداد از کشته‌شدن دو سپاهی در قم خبر داد.
این خبرگزاری ادعا کرد که این دو بر اثر «انفجار پرتابه‌های باقی‌مانده از جنگ اخیر» کشته شده‌اند.
طبق این گزارش، سپاه این دو نفر را حسین رمضانیان فردویی و محمد اویسی معرفی و محل کشته شدن آن‌ها را منطقه فردو، در استان قم اعلام کرد.
با این آمار تعداد تلفات سپاه در دوره آتش‌بس جاری میان جمهوری اسلامی با آمریکا و اسرائیل، و در خارج از درگیری‌های اخیر، دستکم به ۱۶ نفر افزایش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/75861" target="_blank">📅 23:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75859">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d24e12abc.mp4?token=S_QyS680Os1QL5l2EBi-doQ-vCfOJDeJr7jn2B6ebCOz63nKNxNCno7DtZxDaUxAO_5mlfJvPz9MRa1uju8idY2wFkT5iChkPHRBbFLakilqS5r4Jg00SsKd2X2NYFdA581Ytk7ZVbRcqB6WYKnM4A3emo0Fd4x_rbbYCDcT1S8vBwbI7D89EqI3hIYRAsoMqmUaxh1KkYE3il0K6x-GCtQfwu7hhbtjsXpnat8ny4__jSLlvyVRR6ASDbaE1S7CP9SLRpongkwXlIk7sCvvdTk_EsJoIdvHG5Ac4Rgj_PlSG4KujQnKIJ9gonwYMvYONQnQkzCPQW0FsjCMZVDvIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d24e12abc.mp4?token=S_QyS680Os1QL5l2EBi-doQ-vCfOJDeJr7jn2B6ebCOz63nKNxNCno7DtZxDaUxAO_5mlfJvPz9MRa1uju8idY2wFkT5iChkPHRBbFLakilqS5r4Jg00SsKd2X2NYFdA581Ytk7ZVbRcqB6WYKnM4A3emo0Fd4x_rbbYCDcT1S8vBwbI7D89EqI3hIYRAsoMqmUaxh1KkYE3il0K6x-GCtQfwu7hhbtjsXpnat8ny4__jSLlvyVRR6ASDbaE1S7CP9SLRpongkwXlIk7sCvvdTk_EsJoIdvHG5Ac4Rgj_PlSG4KujQnKIJ9gonwYMvYONQnQkzCPQW0FsjCMZVDvIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روابط عمومی سپاه اعلام کرد که در پی حمله ارتش آمریکا به کشتی ایرانی «لیان استار» در محدوده دریای عمان، نیروی دریایی سپاه طی یک عملیات مقابله به مثل، کشتی «ام‌اس‌سی. ساریسکا» با مالکیت «دشمن آمریکایی-اسرائیلی» را با موشک کروز مورد هدف قرار داد
IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/75859" target="_blank">📅 23:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75858">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lGYHYbZAyeVxNbxxDLhqd16OqgXnEVq-4HMgVoLcclDqRokaZcqszp4jXYBE6dSTG2BLZQet5nlGioNhJ2ZNwR2VuNPRcq0-b9uyQFtHEID8SdW8A9hh_ZUDZEdlwVsW3NnSw0ausHNpKfSUjr3x2SeHUb1OT7a6BWf7MHhscv0wSAm-i6aLUVxTYL6S-lrxCLgbpg3S0o6rOAePRUJrJKjv81Lm-cRkXaJR04Z_1zp0rehvZSymecPD05RXFOqG9Pkw6XnRp7IDvO1hq14NNmCSOT6KCsunPgt0q18_R3VWv_s_ekwWBocmkRKsfwgFKLdMJGGxVm4ntQIThA15Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام دونالد ترامپ مبنی بر موافقت بنیامین نتانیاهو با توقف گسیل نظامیان به بیروت، در شامگاه دوشنبه ۱۱ خرداد ماه، با واکنش منفی چند چهره شاخص سیاسی در اسرائیل مواجه شد.
ایتامار بن‌گویر، وزیر امنیت ملی اسرائیل، با انتقاد از این تصمیم گفت: «زمان آن رسیده که به ترامپ نه بگوییم.»
همزمان نفتالی بنت، نخست‌وزیر پیشین اسرائیل، نیز در پیامی دولت این کشور را به ناتوانی در حفظ امنیت متهم کرد. او با اشاره به حوادث امنیتی در اورشلیم، بیت‌شمش، لبنان و غزه نوشت: «مکان‌ها متفاوت هستند، اما داستان یکی است؛ دولتی که کنترل بر حاکمیت اسرائیل را از دست داده است.»
بنت همچنین گفت: «هرج‌ومرج در همه‌جا دیده می‌شود و ما امنیت را به شهروندان اسرائیل بازخواهیم گرداند.»
یائیر لاپید، رهبر مخالفان دولت اسرائیل، نیز با انتقاد از نتانیاهو، تصمیم او را «اعلام تبدیل اسرائیل به یک دولت تحت‌الحمایه کامل» توصیف کرد.
@
VahidOOnLine
دفتر نخست‌وزیر اسرائیل در بیانیه‌ای به نقل از نتانیاهو اعلام کرد: «امشب با رئیس‌جمهوری ترامپ صحبت کردم و به او گفتم اگر حزب‌الله حمله به شهرها و شهروندان ما را متوقف نکند، اسرائیل اهداف تروریستی را در بیروت هدف قرار خواهد داد.»
نتانیاهو افزود: «موضع ما در این زمینه تغییری نکرده است.»
او همچنین تاکید کرد ارتش اسرائیل به عملیات خود در جنوب لبنان طبق برنامه ادامه خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/75858" target="_blank">📅 23:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75857">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XvUPu744hYWrylzOualMifiUdcNYZ3cOlnA5EHdGey4L89GqgzZy9WNgScPQER-fv8dSg8o1I1nLLgqe8q1q5o5EAzA4bIU_wrjegGPm7GqN6kVifESzvt_1ZU9EWS1gKiv_qOMt9LXQrZVPDwQcNB4JSYke6t1ptjFtQx6j2i83cy7Zzrzv1IHnvC5v226cUNAP-B75YIwEoY282f09Dcib6jMUST871if50WkSP1E-U29HgB-i09NQcNKyrixaKfZi-Oc3ZG0kvPj1jfoYu_rxJkbsRlz2SC12mWpt29sz6_hMfPf2mCZbgLtwVv_pS0rTh1v_7dTlSAgrrpRPCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی: ادامه حملات به لبنان و غزه، باب‌المندب را به تنگه هرمز تبدیل خواهد کرد
اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران، شامگاه دوشنبه ۱۱ خرداد ماه در پیامی که رسانه‌های دولتی ایران منتشر کرده‌اند، نوشت جنگ اسرائیل در لبنان و غزه «در سایه حمایت‌های وقیحانه آمریکا، عزم محور مقاومت را برای توسعه پشتیبانی‌ها از هر دو جبهه، اقدام برای فعال‌سازی سایر جبهه‌ها و همسان‌سازی وضعیت ترافیکی تنگه باب‌المندب با تنگه هرمز رقم خواهد زد.»
فرمانده نیروی قدس سپاه همچنین هشدار داد که ادامه عملیات اسرائیل در جنوب لبنان و غزه، این کشور را با واکنش‌های گسترده‌تری از سوی حزب‌الله و گروه‌های فلسطینی روبه‌رو خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/75857" target="_blank">📅 23:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75856">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V1U40a85M5lQOxtHRsLdc0e6l-NvUNfwJeKN4CIJjWJtj72UKiVGyLx0P5X-8P15o3YiInvMLaK3DuL6MkpI8XSegq2Tz286Y1yZljuID7ldNBJ8ed9OS4jc42wER01aWxo_zbzJOSXvqFOB3pz35OmrQ0WgJbQiN0yvSfhXtSzucbK98Ywh0YRbBuK_YUXQTOBcc5rQlymvqUz6NEGO7ClCrTguVDP7LZlLFWBWFnQffXoRFA-rQVbrt7Y_xaJ37YSPfGQtnm1ISXNL8ZmY49wQ0qbK2tycZ1b7tgDoqJdPsyL4JApmse-piW4VtMAAz6v3nINzLTCfOJF6YLyZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: مذاکرات با جمهوری اسلامی ایران با سرعتی بالا ادامه دارد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
این دفعه گفت "جمهوری اسلامی ایران"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/75856" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75855">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ApXPVszLre2HD66ljsg6sXex4wPjWx7CBl2ejeNDaJRUP0y-G_J0gny9J35aQ7ylcTHPPPEpqSbwomhMTxF_pGEKZbqLsKZs1BObDjqCpdBJs4D78al0NtDnd4NxzqAOmH3UgbeqQgLlCaOA4JsA31ZueGJRhb3IF_j7m8_o_7pyqMMudUz1vrRUHJ1iwBga_VZfHTdm7fNeKEDIIDo1Y1LWApagqpbi7PXFkGa0b1khM7udYuzGa36lzhDAfFhq-HPRSBnu3Xwr18z0VuHiaY5uPBqiwulm6pVq1xSlybutqpr2qeyAgPY8bL21sbR-Mi0yb8Ilm-LKerNwoPrZgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اسرائیل و حزب‌الله پذیرفتند حمله‌ها متوقف شود
ترجمه ماشین:
من تماس بسیار سازنده‌ای با نخست‌وزیر اسرائیل، بی‌بی نتانیاهو، داشتم و هیچ نیرویی به بیروت اعزام نخواهد شد؛ و هر نیرویی هم که در مسیر بوده، همین حالا بازگردانده شده است.
همچنین، از طریق نمایندگان بلندپایه، تماس بسیار خوبی با حزب‌الله داشتم و آن‌ها پذیرفتند که همه تیراندازی‌ها متوقف شود — اینکه اسرائیل به آن‌ها حمله نکند و آن‌ها هم به اسرائیل حمله نکنند.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/75855" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75854">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xs0UXl-TwwgDxpNIBRcbhCCMoua3XKrJCTN3o5-RHkW-eb5avJeXMLdmH5gSrT93R3BCoJIe8cZQ-Xl7pC92BpIT3iuYyDQ19EQIrui_8462S8J3NhXz5L_PRXI4g2r7GqywnCGdDoxa6DbeIY8O24O97PToNLWTQ0qBOjZGVWlKsua43eR9BcfdV2Jnu8Q5nLluhIbF09RIvrpNCIImNjNd3CMoJd8tMiFuq7GSghLXRsNpbEysj9hGByYz7FeVxFoox933z_dvpW9ee7658WILBRNMtmk_oEqA1xaW_371pKtTPTJ_JT0ULWhL4EpLiPK7XvH4euI6tEL6xT8j7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: محاصره را حفظ می‌کنیم
توییت‌های خبرنگار NBC، ترجمه ماشین:
تازه: رئیس‌جمهور ترامپ به من گفت که درباره گزارش‌ها مبنی بر تعلیق مذاکرات ایران با آمریکا، چیزی از ایران نشنیده است؛ اما اگر درست باشد، اشکالی ندارد:
«فکر می‌کنم اگر حقیقت را بخواهید، زیادی حرف زده‌ایم. به نظرم سکوت کردن خیلی خوب خواهد بود، و این می‌تواند برای مدتی طولانی باشد.»
او ادامه داد: «این به آن معنا نیست که قرار است برویم و همه‌جا آنجا بمب بریزیم. فقط سکوت می‌کنیم. محاصره را حفظ می‌کنیم. محاصره یک تکه فولاد است.»
آیا می‌تواند آن‌ها را آن‌قدر منتظر بگذارد تا کوتاه بیایند؟
«فکر می‌کنم تا هر وقت که بخواهند می‌توانم صبر کنم. آن‌ها دارند ثروت هنگفتی از دست می‌دهند...»
همچنین وقتی از نویسنده کتاب «هنر معامله» درباره گزارش‌های تعلیق مذاکرات پرسیدم به نظر می‌رسید با اکراه نوعی احترام برای مذاکره‌کنندگان ایرانی قائل است:
«این حرف مناسبی است، چون آن‌ها مذاکره‌کنندگان بهتری هستند تا جنگجو.»
GarrettHaake
الان هم:
ترامپ و نتانیاهو دارند تلفنی صحبت میکنند.
J74wabx
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/75854" target="_blank">📅 20:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75853">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PPLv1LbLzgZTtEmbvlcsqKMEj0K4wkKTYCCBoVnbzQlGiOq_g8vnkhiJLjQT4f4tsA1KC04na6dG4RYo8bHQgNoyHUIxlWJnAedCn2U1JHO95ibgqTcTVrUfF169mJEO6oBAHhmenzqISpN273fYLL6F0yDo31bq_4l5FZlJSmRVi2hl3N6LBk7rb2BT2L0ELpL6D2YdVSlLxyRgJro2thp38oIRTMC7cq8xM9wTzbdXQ6xODzTAtwVX9iRFAvezRMQQgYF6AgSCmQCeY7ACKC_V3WLWq0dlFW8Z9wh3bb_x8B74kRuQ0vT-JKaOvCPQQ4z6X-bXfSWTB_cphWK1eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با صدور هشدار تخلیه از سوی ارتش اسراییل برای ساکنان حومه جنوبی بیروت، فرمانده قرارگاه مرکزی خاتم‌الانبیا به ساکنان مناطق شمالی اسراییل هشدار داد که در صورت عملی شدن تهدیدهای اسراییل علیه لبنان، برای جلوگیری از آسیب، این مناطق را ترک کنند.
علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، اعلام کرد بنیامین نتانیاهو «در ادامه شرارت‌های خود در منطقه»، ضاحیه و بیروت را به بمباران تهدید کرده و برای ساکنان این مناطق هشدار تخلیه صادر کرده است.
او افزود: «با توجه به نقض مکرر آتش‌بس توسط اسراییل، در صورت عملی شدن این تهدید، به ساکنان بخش‌های شمالی و شهرک‌های نظامی در سرزمین‌های اشغالی هشدار می‌دهیم اگر نمی‌خواهند آسیب ببینند منطقه را ترک کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/75853" target="_blank">📅 19:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75852">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89a4fe09bd.mp4?token=DRxBsv8ZC3sTbtGzWyrsLVYsqBiCw1VGOocysw7QmrU86ICE71BB3SOG3PCjhSiGxPvm6LwBPPiplCAsJepUARIbAqLHES33Clc21ZvYqJRPbioq2bci_9fHgvcj1e0JXCoz99DGAGx5fcNqitcKBMzAj7tIbQSL-_ewgGr4A-Rspnl8pAunly6lfAwn3bJcMOqo95sIaoILG8bj-E-cAC4OW7Pn2uhKd1Xo8zqnKdbhEAvlI1GjcwfWScDTjGS52il06nZ_lyMFJFRx3WrnPQYwgtCYp1W5lumeRHKf_SZ--fS-h1LW5NgDX_M9UOIHQDymvTieU4qbrz7ZFE-WPg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89a4fe09bd.mp4?token=DRxBsv8ZC3sTbtGzWyrsLVYsqBiCw1VGOocysw7QmrU86ICE71BB3SOG3PCjhSiGxPvm6LwBPPiplCAsJepUARIbAqLHES33Clc21ZvYqJRPbioq2bci_9fHgvcj1e0JXCoz99DGAGx5fcNqitcKBMzAj7tIbQSL-_ewgGr4A-Rspnl8pAunly6lfAwn3bJcMOqo95sIaoILG8bj-E-cAC4OW7Pn2uhKd1Xo8zqnKdbhEAvlI1GjcwfWScDTjGS52il06nZ_lyMFJFRx3WrnPQYwgtCYp1W5lumeRHKf_SZ--fS-h1LW5NgDX_M9UOIHQDymvTieU4qbrz7ZFE-WPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«حمید سلیمیان» در حال نواختن تنبک
#حمید_سلیمیان
، متأهل و پدر یک پسر چهارماهه شامگاه ۱۸ دی‌ماه ۱۴۰۴ در جریان اعتراضات در زرین‌شهر اصفهان با شلیک مستقیم گلوله جنگی جان خود را از دست داد.
حمید سلیمیان راننده یکی از شرکت‌های فولاد بود و به گفته نزدیکانش به موسیقی علاقه فراوانی داشت او  تنبک و سنتور می‌نواخت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/75852" target="_blank">📅 19:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75843">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KzHEbPbAsNaDYuwAg4uzI9epxEmb4qhf_Uh4sLAanHKsORFWruCIq8Sgnl4b73RtEAYUkjzaYskqZiay4Ugf41_H6_6K1FZgN-E1ZbgugF11POGrNAKj75NRIT0tuBi1u2NIYvLtvdGGiltWP31jH5L1W9WzOFSdWknq2oXJvtgaAJ-xHyeEIZGAOXn9aXP2vFQxOWt8sobb2Y8hgDgDRj3qjjaM6hGwdtb7W1EHkdepaY6FWdvSDBmNBVFNqYCX5F_xcvXRbhnj8oGek27Gf3XGA5-_RqYdGf6QMOZgQ8AFvVNzJO48dyspBdIsRH-ZtSCCHr97BwseJbPkIr0rIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QXA0KEAalnX0oe4DF8nb-38NjiJqoDJd0s0NLz31TLdCk0vWWxktljXB3JEgiGlqckGqcgCm7-Rw9PnbJO-gU8tHCm5KSZk73EFIpiHB1ni5yOIsdxb--rSSyrKjD2--JxPvITK4u_zPB06iqWbb4Hbp3cwM5wRPmhxHxFWYBm07MlTE-OH-PJ5Sw-24IAYk_cTfh7EvE1wVeZIoT0MkGNPBRWn3pkPvzdweEQjGuRAAbBJTx1BGlKP45e1cwD_StVtgmP40gWzRkrTeqN0ohb8Xw4X4MRtpKYgseZuNeXd-EcapBp8l5FnDHJz5q8zwbIQlEcMn4dzbVe0Pl_0tIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r1fHCUgfnhUHR4kYNiE9G812yDb9dcEP7d7usXcZaRmRhYDoIQ8jj6l0gZ9GI_7bjlEPYTljvVzzia8jIKReahqywC4iAcvzuTnv7yiYP8QrOjo9VkIhjLRfk7M5aR0hCOL58WkbzZAyH1kKgua9lIRSYFo2w8bXI-GgHJ7EcejwGSL6tupzFJ_ylC_Jl9tDS_vT69KFQ2Aiiie21j-z2GY2x3DvheP9nmSjrAQvzBAsL5QmGF0fhuyhG8sxhMjzx2X7Z0yDWcsWK5fBHNpWdkDwYipHei-A-Ew8MZyAHdBITbHjqzmu9vBLNoonxp_CghGvtWCK8m8dqMBVJ_WEGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NT9GKDPLLmfoyFrhZojLbZRvL59GjzuNZavSQpWjFYpeUld9lMZn5eXspa80q05LmIv-EaO4YmZRaT2RojQ0Igep_DgqNZXuuJ81kr--yjUDurW87V_ekEeNSxAgIduzcUsWOJajTdGM38Z2L3-g4m2fVYaYqs4H3ybqVRlodbijPwkzu5ZTOYNShYuYbu44myeb9N-AFJ2-pQdXTuXL18q8sM7BwOU3jrdeiK5_Fc_9gwakadFeaV0_3vr24XyWqR_2IPcnGN_8t3l9q_86TUewCBQTk1ZTY-_4QrHwuIe54hkNthTyqJXgeWcg1XGaN5CTJQxMGKBrwJan_vS4Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uFmtRCItwqbRW41Hmpcjjddvea7iRkUYaKoqYQKp09nincCreS2XwyPf67fcxNrHFfrjufe6ma2a5kMMzN2dibrlhkHUaayRNKclE9rE0i9EHv_K7ou4Cy_ds9Z-famdw3bYSZZL0vix93owm4qb7kjPrjVw1cBMIDGQb4VPc83nkZYBklcdn2GCUJ-DNesyWf2ghz8wBQ0RKKMbMBKpT2wGKtzPIUfMbZYtRb0_8Zu9WSazUxCHSvD_VGV7pnNUqqoRQcN25xSYU-m4v1w_5M0freGjtwfWQwE8bHAqTcOyABDH2mWrKZlROR3TtzKxUuSb8ybbdKvXQbPUehrG5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qyy-TEXoVePXT7OsylY_AjfEfvfwObdkj-1vxSVHn1YHQ5Z1QpTjXVylHRQWzffGskE5W0RBLIUO1od2VyWnsnZ48yAISqdqLnb2Z8oJx_bEnNOuCqofnn-z0kvM7uJw-CoM1InQSLqlIM31MeFf613N09Akbn4mECCHNsGhyoyEgQp60Cd-P5_SQTd0NHZT8wLZuz4xLKMdBdHrIATAxM_08eJ3xsNOhBEx-7T4PEGYuwWiKaZZ5TulU3pRjsmZzDac4pNyKESwecqj1Qal1DFaVQwhZT66sOi5WDxRwhwfTDFR7PNHbZWJcXzks1r4Yn_6KCQkYmi-Rsx7GG-96w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EUNNNFLOEwQTHz7JdnvQWwurVOjw3hmPMJrtGJIqCdeq_cJdko3tyXpnqXDdqq7FiHdkEs5okh6tPmNudl8AF-l14MmpkHupdvVx2KL5YihWC9Wg91oJxjfVz6YYuq_wzh2sp9FKoAe6j3cRrUD071169CKaVmUwQvK-A-jOU61A7_gfEuR0O3K-iVlarpBpfyCfVjcRBSpLt5DW4SVZhZg4op1YJFKKnghGsCyvhgXiO0WrSMugNd5caixVn3QnQhvGpK7uGNFyyr8etWrJygcYZ9BsrCog65wFU0ANQ0pFfYsrfFLQ8hfbCVogdx_8b1UVsr9SIJDGWXfLNyQdqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YtR0gQQ_hrfCifFsjkOysWif4XX9Ikjkk7FN-daLbkNdGk--iN8VgSMaMiJHvWQCKDmR6XY4vk_MDXDEx8G1Nt_nIyXRp3Vnw5YtezXgJxKcRV4ELfAuuMrKWQsuoOzX7OoisI-hiuN1N9P9zahaKaFBSu_dblLEm-1JmvkGdPx_eQBbCWkQ1IDiL1OcPMnt9D4e4_sYaIa32ckfgNIluKqqEKDmL1g_hjQyd6xP2oY2521YvbalszQPvTQn_ONJtiD8ixmvzo1KrbndZONiCj-PmDRxXAtinTamk6eTfF9eRbazeR8ZhptrbhJkTlsdnKSwMQwQOMB-pkVZOxQsOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CIDJGqs0xL1DsUQsc6i6YtXJLIPrjeRgqeqayb70St2WR6xtvQhxHouZ98DMQd1A5M2RlArWcaSXOqZkiRJ9oj8W5_l1GNB651d7GE2417tFV_crSIWPhVctgeRQdJAr44Wfv0nyRc6QssAnbolPoVWxptTaZHWwo-5agsuv5g66uHrc7ZgLTjP3ARWmFZS-ekvofR_KQgUsaVrTiWe5qNYGCXUfOAazqfDVoquypYGFVknUXREtuj6Df99M5SAikMC0QJaCnJqf0GK2MDQGOPRJWQ3j9rnyGy2KAjDtZVHCxq83W1NPaDr7tnR6W45nPZMwQuyfLViHZc5OfeofEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هم‌زمان با تشدید حملات نظامی اسراییل به لبنان، مقام‌های جمهوری اسلامی بار دیگر تاکید کردند که هرگونه آتش‌بس میان ایران و آمریکا باید شامل همه جبهه‌های درگیری، به‌ویژه لبنان، باشد و هشدار دادند ادامه حملات به این کشور می‌تواند پیامدهایی در پی داشته باشد.
بنیامین نتانیاهو، نخست‌وزیر اسراییل، روز دوشنبه ۱۱ خرداد ۱۴۰۵، اعلام کرد که به ارتش این کشور دستور داده است اهداف متعلق به حزب‌الله در ضاحیه، حومه جنوبی بیروت، را هدف قرار دهد. او در یک پیام ویدیویی گفت: «هیچ وضعیتی وجود نخواهد داشت که حزب‌الله شهرها و شهروندان ما را هدف قرار دهد اما مقرهای تروریستی آن در ضاحیه بیروت از حمله مصون بماند.»
دفتر نخست‌وزیر اسراییل در بیانیه‌ای اعلام کرد نتانیاهو و یسراییل کاتس، وزیر دفاع این کشور، در پی آنچه «نقض مکرر آتش‌بس از سوی حزب‌الله» و «حملات علیه شهرها و شهروندان اسراییل» خوانده شده، به ارتش دستور حمله به «اهداف تروریستی» در حومه جنوبی بیروت را داده‌اند.
نتانیاهو همچنین گفت عملیات زمینی ارتش اسراییل در لبنان در حال گسترش است. اسراییل در جنوب لبنان منطقه‌ای امنیتی ایجاد کرده و می‌گوید هدف از آن جلوگیری از حملات حزب‌الله به مناطق شمالی این کشور است.
در واکنش به این تحولات، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، در شبکه ایکس نوشت: «آتش‌بس میان ایران و آمریکا، بدون هیچ ابهامی، آتش‌بسی در تمام جبهه‌ها، از جمله لبنان، است.» او افزود نقض آتش‌بس در هر جبهه‌ای «به معنای نقض آتش‌بس در تمامی جبهه‌ها» خواهد بود.
عراقچی همچنین آمریکا و اسراییل را مسوول پیامدهای هرگونه نقض این آتش‌بس دانست. جمهوری اسلامی پیش از این نیز بارها اعلام کرده بود که آتش‌بس میان ایران و آمریکا باید سایر جبهه‌های درگیری، به‌ویژه لبنان، را نیز در بر بگیرد.
ابوالفضل شکارچی، سخنگوی نیروهای مسلح جمهوری اسلامی، نیز به اسراییل هشدار داد که «تداوم جنایات در لبنان برای نیروهای مسلح ایران قابل تحمل نخواهد بود.»
هم‌زمان، محمدباقر قالیباف، رییس مجلس شورای اسلامی و رییس هیات مذاکره‌کننده ایران با آمریکا، با اشاره به آنچه «محاصره دریایی و تشدید جنایات جنگی در لبنان» خواند، این اقدامات را «شواهد آشکار عدم پایبندی آمریکا به آتش‌بس» توصیف کرد.
قالیباف در پیامی به زبان انگلیسی در شبکه ایکس، بدون اشاره به جزییات بیشتر، نوشت: «هر انتخابی بهایی دارد و زمان پرداخت آن فرا می‌رسد. همه‌چیز در نهایت سر جای خود قرار خواهد گرفت.»
این اظهارات در حالی مطرح می‌شود که عملیات نظامی اسراییل علیه حزب‌الله، از گروه‌های مورد حمایت جمهوری اسلامی در منطقه، شدت گرفته است. با وجود تاکید مکرر تهران بر ضرورت گنجاندن لبنان در هر توافق آتش‌بس میان ایران و آمریکا، این مطالبه تاکنون محقق نشده است.
اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی، نیز روز دوشنبه در نشست خبری هفتگی خود گفت: «ما تاکید کردیم و کماکان تاکید داریم بر این نکته که آتش‌بس در لبنان بخش لاینفک هرگونه آتش‌بس و هرگونه توافق نهایی برای خاتمه جنگ است.»
او همچنین حملات اسراییل به لبنان را از عوامل ایجاد تاخیر در روند دیپلماتیک برای پایان دادن به جنگ میان ایران و آمریکا دانست و بار دیگر بر ضرورت برقراری آتش‌بس در لبنان به عنوان بخشی جدایی‌ناپذیر از هر توافق نهایی تاکید کرد.
@
VahidHeadline
تازه‌تر:
خبرگزاری تسنیم، وابسته به سپاه پاسداران، گزارش داد که جمهوری اسلامی در واکنش به ادامه حملات اسراییل به لبنان و آنچه «نقض آتش‌بس در همه جبهه‌ها» خوانده شده، روند گفت‌وگوها و تبادل پیام با آمریکا از طریق میانجی‌ها را متوقف خواهد کرد.
تسنیم همچنین مدعی شده است که ایران و گروه‌های هم‌پیمان آن در «جبهه مقاومت» در حال بررسی اقداماتی از جمله انسداد تنگه هرمز و فعال‌سازی سایر جبهه‌ها از جمله تنگه باب‌المندب هستند. این گزارش می‌گوید این اقدامات با هدف واکنش به حملات اسراییل و حامیان آن در دستور کار قرار گرفته است.
@
VahidHeadline
ارتش اسرائیل در بیانیه‌ای به ساکنان منطقه ضاحیه در جنوب بیروت هشدار داد و از آن‌ها خواست برای حفظ جان خود این منطقه را تخلیه کنند.
در این بیانیه آمده است اگر حزب‌الله به شلیک راکت به سوی شهرها و شهرک‌های اسرائیل ادامه دهد، ارتش اسرائیل اهدافی را در ضاحیه جنوبی هدف قرار خواهد داد.
در ادامه تاکید شده است دولت اسرائیل با مردم لبنان در حال جنگ نیست، بلکه با سازمان تروریستی حزب‌الله می‌جنگد.
@
VahidOOnLine
در پی اعلام خبرگزاری تسنیم مبنی بر توقف «گفتگوها و تبادل متون از طریق میانجی» میان تهران و واشنگتن، بهای جهانی نفت بیش از ۵ درصد افزایش یافت و به بالاترین سطح خود در هفته‌های اخیر رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/75843" target="_blank">📅 19:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75842">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGo4KuSumPRD-ZxYRkEJPEBSgFL1ZRLQ1iaMbquREqh8RGwjUEOJ5yM0KXWdnbQAkq62PZtFIcBDU6AUyjE9RAAffXFNH-NwaOSYjY9O6wI7z_zrJnDtKrwQhsTRt6zZwHqBekU-IPBERpPTJg2dUsRLTcPsKT9QmFraF8_NzLZa0M65pWMMYcmfGd0QqIyKfkyNxIiJWflGU390eVeHTJEVa_k3vA4ieMx2JA4IhwCmiXW-qA6Fw3zARV7_RmTrFYA4BzaN20Awhul59zFrlAHe30FPDE_1Y7ouEWlVuuA2Qr87WCb4G8sS2nEQm_k0mvzY5gOFwpLL1celSnjnGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران از کشته شدن یک دانشجوی زن در دانشکده دندانپزشکی قزوین به ضرب گلوله خبر داده‌اند.
میزان، خبرگزاری قوه قضائیه، از قول دادستان قزوین نوشت: «بررسی‌های اولیه نشان می‌دهد این دو دانشجو که در آستانه فارغ‌التحصیلی قرار داشتند، در مرحله متارکه از یک رابطه عاطفی بوده و پیش از این نیز اختلافات خانوادگی شدیدی با یکدیگر داشتند. صبح امروز، مرد جوان با یک قبضه سلاح کلت جنگی وارد محوطه درمانگاه شده و چهار گلوله به ناحیه سینه دانشجوی دختر شلیک کرده است. شدت جراحات وارده به‌حدی بوده که متأسفانه وی در همان محل جان خود را از دست می‌دهد.
در اطلاعیه دانشگاه علوم پزشکی قزوین در این باره آمده است: «انگیزه این واقعه، مسایل شخصی و خانوادگی بوده و ارتباطی با فرآیندهای اداری یا محیط آموزشی دانشکده ندارد.»
به گفته حمیدرضا قافله باشی، رئیس دانشگاه علوم پزشکی قزوین، «این تیراندازی به دلیل خصومت‌ خانوادگی اتفاق افتاده و دو دانشجو که زن و شوهر بودند در اثر شلیک جان خود را از دست داده‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/75842" target="_blank">📅 19:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75841">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پیام‌های دریافتی از تهران درباره صدای پرواز یک جنگنده یا هواپیمایی دیگر مربوط به جمهوری اسلامی:
سلام تهران صدای جنگنده اومد همین الان
غرب تهران وحشتناک صدا جنگنده میاد ۹:۱۵
صدای جنگنده داره میاد غرب تهرانم ساعت ۹.۱۴
سلام وحید همین الان تهران صدای جنگنده میومد نزدیک ۲ دقیقه
شمال شرق تهران صدای جنگنده
سلام تهران صدا جنگنده شدید
الان از بالا سر ما صدای جنگنده اومد
رد شد رفت
همین الان منطقه گیشا صدای جنگنده میاد
همین الان ساعت ۹:۱۵ دقیقه صدای جنگنده سمت غرب تهران اومد(فکر میکنم جنگنده ارتش بوده باشه)
سلام وحید از سمت لویزان تهران موشک بلند شد
وحید الان ساعت ۹:۱۵ صدا جت منطقه ۲ تهران
تهران-فرمانيه
ساعت 9;16 صداي جنگنده مياد
وحید تهران ساعت ۹:۱۷ صدا جت میاد زیاد
هروی
الو سلام تهران سمت شهرک غرب صدای نمیدونم هواپیما بود جنگنده بود چی بود خیلی نزدیک بود
الان ساعت ۹:۱۷ دقیقه در قیطریه صدای جنگنده اومد
شرق تهران صدای جنگنده شنیده شد الان
سلام تهران صدا جنگنده شدید
احتمالا جنگنده های خودشونه
ساعت۹:۱۷
سلام دوشنبه تهران ساعت ۹:۱۵ صدا جنگنده من شنیدم سمت هروی
صدای جنگنده تهران ۹:۱۷
صدای جنگنده منطقه ۳
خیلی پایین بود
تهران صدای جنگنده اومد
سلام ساعت ۹:۱۵ سمت دروس تهران صدای جنگنده اومد
صدای جنگنده شمال تهران ساعت ۹:۱۵ رقیقه
سلام ساعت ۰۹۱۵ دوشنبه صدای پرواز چند جنگنده شمال تهران
منطقه ۳ صدای جنگنده انقدر زیاد و وحشتناک بود که از خواب بیدار شدم
سلام  پاسدارانیم صدای جنگنده اومد چند دقیقه پیش
صدای جنگده نارمک
سلام وحید. صدایی که ۹:۱۵ اومد شبیه جنگنده بود ولی از پنجره نگاه کردم شبیه هواپیمای مسافربری بود فقط نمیدونم چرا از ارتفاع کم حرکت میکرد
سلام آقا وحید من خونم گیشاسصدای جنگنده نبود هواپیما بود من بالای خونه رفتم دیدم ولی هواپیما بزرگ بود ی مقدار دیگه باری بود یا سواری نمیدونم ولی از بالای گیشا رد شد
من از روستای اطراف شهریارهستم یه هواپیمای مسافربری بزرگ تو ارتفاع پایین از بالا سرمون رد شد به وضوح دیدمش صداش زیاد بود
سلام وقت بخیر نیاورانم صدای جنگنده اومد وحشتناک بود
وحید من شهرک محلاتیم
بین ۹:۱۵ تا ۹:۲۰ صدای جنگنده میومد
(با ارتفاع پایین)
سلام وحید جان صدای وحشتناک جنگنده ۳ ۴ دقیقه پیش خونرو لرزوند
-هواپیمای کارگو سپاه از تهران بلند شد
.
-صدای جنگنده برای این بود؟
-ممکنه برای اسکورتش بوده باشه
J74wabx
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/75841" target="_blank">📅 09:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75840">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پیام‌های دریافتی از
#بندرعباس
درباره شنیده شدن صدای سه انفجار:
بندرعباس ساعت ۹:۰۷ سه تا انفجار
الان بندرعباس ساعت 9:7 دقیقه 3انفجار قوی
یک صداهایی شبیه برخورد جسم سنگین (بمب یا هرچی) به زمین داره میاد از دوردست.
بندرعباس ساعت ۹:۰۹ صبح دوشنبه
سه تا صدای  انفجار اومد بندرعباس
ساعت ۹ و هشت دقیقه
دوشنبه، ۱۱ خرداد ۹:۰۷ صبح. بندرعباس.
صدای ۳ تا انفجار از نزدیکی پایگاه هوایی شنیده شد.
آپدیت:
خبرگزاری تسنیم وابسته به سپاه مدعی شده که مربوط به مهمات خنثی نشده بوده. البته دو روز پیش‌تر از این هم اعلام کرده بودند که طی ۷۲ ساعت آینده قراره از این صداها شنیده بشه در بندرعباس.
پیام‌های دریافتی از
#اصفهان
درباره شنیده شدن دو صدای انفجار از دور:
پیام ساعت ۹:۱۷: اصفهان صدای انفجار میاد، دو بار پشت سر هم
اصفهان همین الان صدای انفجار اومد سمت ناحیه ۶
الان اصفهان یه صدایی مثل صدای انفجار اومد
سلام وحید، اصفهان ساعت ۹:۱۸ ۲تا صدا مثل انفجار و کمی لرزش حس کردم فاصلش خیلی دور بود، بین ساعت ۸ تا ۹ هم یک صدای مشابه اومد فکر کردم توهم زدم
اصفهان صدا انفجار نزدیکای جی شیر(مطمئن نیستم)
سلام. اصفهان حدود ساعت ۹:۱۵ صدای ۲ تا انفجار به فاصله چند ثانیه.
نمی دونم چیزی زدن یا دارند مهمات خنثی می کنند. البته تقریبا هر روز صبح یه صدا میاد که به خنثی سازی میخوره.
امروز ۲ تا پشت سر هم بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/75840" target="_blank">📅 09:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75839">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nDTEH2RVxmevlXIpt0EkvPcjaHuS9LxhMxoJL3Lw7YWiSZcU2zo09Xc_2tBhjH-XC-yLIYUokhFASht-pqZSgMv1p1zprwOWSoHVSzwLtG3_lW3DVOBU5S8XIecXgZ4NzP3wUWzqCJiC3sSUYH8zhBnompKCTtbghhvi3NFSrGYtCnyrNoxXj7Q_47saNCU-WKWB6DA3ljuEN11XEJke6rD3XEizKBMmj2JORvXuEaQDuVIMpTmrNifB5shT_A3iC3PD9o20A5dHsKzuiUeEQfnhDeVhonztSY7kvgsz0t2t0baXQMtWh7fjEDeB9gknTO3cJpf-ukyINKkxxvqW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران واقعاً می‌خواهد به توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌های کودن و بعضی جمهوری‌خواهانِ ظاهراً غیرمیهن‌دوست نمی‌فهمند وقتی سیاسی‌کارها مدام و با شدتی بی‌سابقه غر می‌زنند که باید سریع‌تر حرکت کنم، یا کندتر، یا جنگ کنم، یا جنگ نکنم، یا هر چیز دیگری، کار درست و مذاکره برای من خیلی سخت‌تر می‌شود؟
فقط بنشینید و آرام باشید؛ در پایان همه‌چیز خوب پیش خواهد رفت — همیشه همین‌طور است!
رئیس‌جمهور، دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/75839" target="_blank">📅 08:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75838">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پیام‌های دریافتی:
امیدیه خوزستان صدای انفجار شنیده میشه
از امیدیه خوزستان پیام میدم
طرفای ساعت ۸:۱۳ دقیقه صدای ترکیدن اومد
ساعت ۸:۳۱ دوباره زدن
همین چند دقیقه پیش صدای انفجار واضح ای اومد
امیدیه هستم و صدای دوتا انفجار شدید ساعت 8:33 اومدش.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/75838" target="_blank">📅 08:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75836">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی اعلام کرد که دو نفر دیگر از معترضان دی‌ماه ۱۴۰۴ را به اتهام «آتش‌زدن مسجد [گیشا]»، «لیدری کودتا»، «تخریب اموال عمومی» و «مسدودسازی خیابان‌ها» اعدام کرده است.
نام این دو معترض که بامداد دوشنبه یازدهم خرداد اعدام شدند، مهرداد محمدی‌نیا و اشکان مالکی اعلام شده است.
میزان نوشته این دو «از عوامل اصلی آتش‌زدن مسجد جعفری در محله کوی نصر تهران [بودند] که اقدام به تخریب و آتش‌زدن مسجد، تخریب اموال عمومی، درگیری با مأموران حافظان امنیت، انسداد خیابان‌ها و ممانعت از عبور و مرور مردم کرده بودند.»
دستگاه قضایی جمهوری اسلامی در ماه‌های اخیر به شکل تقریباً روزانه اقدام به اجرای احکام اعدام معترضان و یا افرادی می‌کند که آن‌ها را به همکاری با آمریکا و اسرائیل متهم می‌کند. برخی نهادهای حقوق‌بشری می‌گویند جمهوری اسلامی از اعدام برای ایجاد فضای ترس و به‌عنوان عامل سرکوب استفاده می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/75836" target="_blank">📅 08:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75834">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FNHV_CUcXD0i8TkMEXElrJQXDkPzYU6nnVD5io90t8fpEs_5dVzM2NaNGBbcH3wtemTQ-TT03zZBCJFDKPDd2IZXBiULwUU4p6ts7QFNZT2bAsNHnWsCWjgKu7wlvfMSWwV7pEKX-_1T2oKfmkEVqZZOuFzAPcp3-VfvEDxm631zUBEyS9VhClHdNvb5Oh8DbZyB9ahC9m7ehHb1X-cVE2Nu7kLJWprBKVj1ks82PAHANyuIe9TDqLb0nFNTEow7mT4vU6XFtce6qoZWHRF-WIW1E76wvo9vMR0dEQOjiJTZi05Tr5tC8vZ-JPiB0mFQq04DK_qQswDdErCtFoyw1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sy_OzNz9RuERGUk49mRjyDN6-FXexnaKhWk2BnDWi7F7Pk7h8XuiansARjjSp_dcb2d3bWTDfoWt4f0WbdikUjXauQBCY3sNSqIzFZhDXUNCTBoKbonYHh4Xt94pDUipLtW5Xg8Yh_smPueTnYoWc3-skBlKzqLi4xy4NSKmcZ6G7xGKEgmODklwuMeNR7avCU4q3d_PuroOuxmsf953O963a-JgtBWMHrqWFaz90jijGdYS6aPSWKt61go34KLEKP6fvIBMfzxLwcbU7uHwevQHPntNbnCTXqJLdtbFQHkD95N6htXRPdrh_RMMllaicMPdOP4q5sMJ3o6nsAizaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیانیه سپاه: ساعتی پیش آمریکا به دکل مخابراتی سیریک حمله کرده بود پاسخ دادیم
من اون موقع فقط از یک نفر دو پیام داشتم:
ساعت 4:00 چهار انفجار در شهرستان سیریک
پایگاه سپاه سرخور زدن
ساعت 4:26 دوباره یکی زد
هرمزگان شهرستان سیریک
و الان کسی تصویر دوم بالا رو فرستاد و نوشت:
"حدود ساعت چهار صبح، آمریکا با چند موشک به اینجا حمله کرد.
پایگاه  نیروی دریایی سپاه  شهرستان سیریک ، حوالی روستای گروک"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/75834" target="_blank">📅 07:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75833">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a89b39dc76.mp4?token=Rs2_lEqI0XmonT4WRxI0q9qI63L86cp4Nk_kdnkkN1C4gmQvd6zeDm2LYcUEzEUn5PWoirDgTopuOJR6M5evpqBvBtoRdJW1Q9CmWDLaMgzzb2WUNRBCIZzvVm_gWLOL_FzyqShcaXCS8zt2YO-QpuBjKqqM1AzRmxCmNfg-IHDQa6EX18511aKpAGh30p0MduKJxlvjgoFKTbLdkdqjFm0sK5Q1Xh9e9uGH3jKZoY6_8FYyq3gHivgZ7nPGB5mi5tawP-D-fFWQgpXpLRFKXxpvTLrsgor6ZTX73T7wgUfdzaX0q5V8oRiERJAehLLrApdxpDt0cQnFhTlXUtcQig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a89b39dc76.mp4?token=Rs2_lEqI0XmonT4WRxI0q9qI63L86cp4Nk_kdnkkN1C4gmQvd6zeDm2LYcUEzEUn5PWoirDgTopuOJR6M5evpqBvBtoRdJW1Q9CmWDLaMgzzb2WUNRBCIZzvVm_gWLOL_FzyqShcaXCS8zt2YO-QpuBjKqqM1AzRmxCmNfg-IHDQa6EX18511aKpAGh30p0MduKJxlvjgoFKTbLdkdqjFm0sK5Q1Xh9e9uGH3jKZoY6_8FYyq3gHivgZ7nPGB5mi5tawP-D-fFWQgpXpLRFKXxpvTLrsgor6ZTX73T7wgUfdzaX0q5V8oRiERJAehLLrApdxpDt0cQnFhTlXUtcQig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'شلیک موشک از
#امیدیه
در خوزستان'
ویدیوی دریافتی دیگر از همان موشک،
دوشنبه ۱۱ خرداد ساعت ۶:۳۰
Vahid
ستاد کل
ارتش کویت
دقایقی پیش اعلام کرد سامانه‌های پدافند هوایی این کشور در حال مقابله با حملات موشکی و پهپادی دشمن هستند.
به گزارش خبرگزاری رویترز، جزییات بیشتری درباره این حمله پهپادی منتشر نشده است.
ارتش کویت در بیانیه خود تاکید کرد که صداهای احتمالی انفجار ناشی از رهگیری اهداف مهاجم از سوی سامانه‌های پدافندی است و از شهروندان خواست دستورالعمل‌های ایمنی را رعایت کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/75833" target="_blank">📅 07:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75832">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PsNhLMLJHMVHEEi7ATdlQ5dZeOpgjSzyhmY9l7xuLHSmO9jRugPxYs-0w9H3BiTkTU01eYFAZTaFPu0A-zQ6RS26XQ4OxY81898OWJQ1XpYCots77sTc9I6uA0KL9R3I7wfmGcFxrh0hYO0fcgVRtbJgHUYvH3ITht2DbfkdZDz3a9eTowOCOD61YyEXd6No5ZTVvKM2FmiJA3sAROYe0WaL1JecE-griOiAz_dNnwdGXv0aYROREUDOYmcYReMJcQmi9vY60Ep335TeI-8rJXsM92wJZim-LCO3tGHZ1L0jwyF-Jb2hqbXGGosSCyt6r_npYQCwCTM3o8B6lhPoaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام درباره حملات شنبه و یکشنبه
(از جمله حمله ساعاتی پیش به سیریک هرمزگان که با توجه به
پستی پایین‌تر
گویا حدود ساعت ۴ صبح دوشنبه به وقت ایران انجام شده. در آمریکا هنوز یکشنبه است.)
ترجمه ماشین:
"آمریکا در واکنش به تجاوز ایران، از خود دفاع کرد و تهدیدها را از کار انداخت
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده آمریکا، سنتکام، این آخر هفته حملات دفاعی علیه سایت‌های راداری ایران و مراکز فرماندهی و کنترل پهپادها در گروک ایران و جزیره قشم انجام داد.
این حملات حساب‌شده و عامدانه، روزهای شنبه و یکشنبه و در پاسخ به اقدامات تهاجمی ایران انجام شد؛ اقداماتی که شامل سرنگونی یک پهپاد MQ-1 آمریکا بود که بر فراز آب‌های بین‌المللی فعالیت می‌کرد. جنگنده‌های آمریکایی به‌سرعت واکنش نشان دادند و پدافند هوایی ایران، یک ایستگاه کنترل زمینی، و دو پهپاد تهاجمی یک‌طرفه را که تهدیدی آشکار برای کشتی‌های در حال عبور از آب‌های منطقه‌ای محسوب می‌شدند، منهدم کردند.
هیچ‌یک از نیروهای نظامی آمریکا آسیب ندیدند. سنتکام در جریان آتش‌بس جاری، در واکنش به تجاوز بی‌دلیل ایران، به حفاظت از دارایی‌ها و منافع ایالات متحده ادامه خواهد داد."
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/75832" target="_blank">📅 06:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75828">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UBBrP6gZn1hPDj9Vw5NVmBT1qmQZQbmjSO-Sul7BkhUgay4grZO-5PRxYr-rsa8AbhyKENdF7lE4NscSZugBdRjxzNZQqS_b8aJycITcyqumYINjQsJMI73s5MhVmVR0iKm0a96ScAS1muS-WKjIIYkyRhiKlRkJQpURrVmU47LQhOgrPerGAyEav9WnnNMPwPKf2P7GtvCBeWI8DFTFjjzNFaxu4_PpwcIfCSRwsSyjZosxJ9dufxXbtmDZbC6L1u27o50WaWZug5GJkYLjShi61FBXIfkm0zVKu91M7RDDHi-4SGHtpfFsKwXND7ruGm3J1a0pWHnbJdo0VoSeQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OfvfqSg4mky3Oz3YLmcapgB9KrwTlK6Qa04scmbJ4MDxkF1KfaLfZlAZ8sqN48mqNWF_wivEs1UfbM7N5zzIqchYYv8f-pjWpFHIMAI4mvWpuewntWDCgNoxMkAUdSQgYEEGUDivbZewxuC75zd17yGpbCI1m-wHSiMsNB1K5wQT0QkFuFByTpj6JvHpYJx4_1e3oh38TRXKA4ug0NzC7yNqLI5FgpI1WjHp6ihkw6vs8ZnxWk3HiEiB7_BhTywckidMiGkaJtCViII8CKs4Nr3m2GTn3-qewPnSNYmCCGzx8Sjjpj8sVPRk3G3EYFGzUBUsmWW5VsJDxVtc_bW1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oJBV6_ezyyAxu1bvX_FNPXEBKTu6bVMmnCL4Ab8n2GnPkQY1gsbq3-RskqFbtTZjyaTIW-3EMKfsiNYY1ENaLEPudnYiGifl514fVcrKch6qqVhXwWqEgF5OWE2mzW5gMKZyPszg1hjYhURlTEnEi4g8br9NOoAArmjqM-XLZpfPt_kq6nzCcfPKoKFiUVhObCyqwK5dAPeBC9FYo891XBSSqSZm1Oktb4jrUxgmfkXlgIF0FrrjPsPMtsC6v5_gaPTrkKl_HQYfr_IGuAx_LuhC05y8K40mGEErqPzmziLlHkHyRXi3fSp5QgU3hEed4fWi4HMvufxpQ1VuJoFATQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1affc9bf27.mp4?token=TS6342YK8z-Y0oKSKbFp2zRdNHp05Bk73O_g5A7ubFbDYAoo9GgVyJrXfqUlaZd7zwe0EvROm01hiD24J_p310jsNFdPgWOUW7M-IOtTA89AbXhw36S305T76udMS_1Svfy-hgqQdwQjwb-evOxzwEOTN_NJAVtArUkwymRyltfMkYhn0XTY-j9B-a9bR8yerIkkBlCVSfAEDUOhrPTG4LsH4FQpogfvJIYazJ0qWorK7fCVxj3QJNtP8_DG9inWLy8DPrNRZAX2hNjK77lZXv-A-beJ8f7iVDgWU8ZqZcSnI3AntTO7mif_xauTl0zXMIuexAXgNJjPB94ReCE9og" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1affc9bf27.mp4?token=TS6342YK8z-Y0oKSKbFp2zRdNHp05Bk73O_g5A7ubFbDYAoo9GgVyJrXfqUlaZd7zwe0EvROm01hiD24J_p310jsNFdPgWOUW7M-IOtTA89AbXhw36S305T76udMS_1Svfy-hgqQdwQjwb-evOxzwEOTN_NJAVtArUkwymRyltfMkYhn0XTY-j9B-a9bR8yerIkkBlCVSfAEDUOhrPTG4LsH4FQpogfvJIYazJ0qWorK7fCVxj3QJNtP8_DG9inWLy8DPrNRZAX2hNjK77lZXv-A-beJ8f7iVDgWU8ZqZcSnI3AntTO7mif_xauTl0zXMIuexAXgNJjPB94ReCE9og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'شلیک موشک از
#امیدیه
در خوزستان'
تصاویر دریافتی، دوشنبه ۱۱ خرداد ساعت ۶:۳۰ به وقت
#ایران
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75828" target="_blank">📅 06:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75827">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nyvdjarWolyCF3hKXANBF3VpRg8bATPh74B_fnXZcOISY_22UO7mVskNN-lGIMmPRB8in_ME-DF9_jMSHEDSzlstTuPxeY5wqZpTmEdKkITz4JE17hcgEAYIzJVp2oQzJi8C7fpV8fFM3doXMNaRN4U3HIOkUCj4qo6gFykXppDdAtnsTCBCSEIUFbzGKM4kDNLiQ79TuEtxCGPJ9obZ0j1RtXF5hJKAp_oMMQO0qKsKIMrHs9D_lP0GHsEQHhYdA0Ptep_3Kw_OsZhrm7Cbci4wM7GtyOpdk-0jK-ryJj27V8-oszDG-U31E8HV3DZ1z5UJJQUBC4CiwNFhVJN3Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک به کویت
دوباره همز‌مان پیام‌هایی درباره شلیک موشک از امیدیه خوزستان و اعلام هشدار در کویت دریافت کردم.
دوشنبه ۱۱ خرداد
ساعت ۶ به وقت کویت که میشه ساعت ۶:۳۰ به وقت ایران
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/75827" target="_blank">📅 06:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75826">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NzjWZkBx6Dadpw-yaJy6EGcOgdxigbpjbcoMKFrAMHOk1BkFed8kYSHxPRYPUbaMrA7Cc0DePBRDENnsaQAln1XKzsZ7Xa3XZ6EvMveU96_pOAC7VJc4v8gs6-IHT5HNoASUV4f3MozRx0uwxvpKmM_Bf5jQV263caYSwl-DyCf62jsTjuEvTXIY-VbqtSU-gOZjzRLN6DXZ0XhTPWFEYj9dI1dvWiAvLJDNeH6TxTCG5m0YUEhB9sDJtwahfgEUb1AF2qxlIKIKe83T5WrXRNGtuSl3erxVjqjfVkX1ajSUMaTndndu6d_pkUwXGEBfP7Mr4fSPFPCyHx_jqzoYyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
رسانه اخبار جعلی سی‌ان‌ان امروز طبق معمول گفت که توافق هسته‌ای ایرانِ من درباره مسائل هسته‌ای صحبت نمی‌کند؛ در حالی که در واقع، بسیار روشن تصریح می‌کند که ایران سلاح هسته‌ای نخواهد داشت.
سپس با جزئیات بسیار محکم و مفصل، به جنبه‌های مختلف دیگر موضوع هسته‌ای می‌پردازد.
در واقع، بیشترِ این توافق درباره همین موضوع است.
سی‌ان‌ان و بسیاری دیگر در رسانه‌های اخبار جعلی، فاجعه‌ای با رتبه‌های پایین هستند.
حتی با مالکیت جدید هم بعید است اوضاعشان هرگز بهتر شود!!!
رئیس‌جمهور، دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/75826" target="_blank">📅 03:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75825">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O3QqdfRrjaRT2MB0Qd3aIvy92_9o6oCb8AL_7XBZjpdUSCxanb5U5IFbuocitL1x37mCV8YgLTiwzqnOW_HRJSc6AvEwN_4B0Eqa0rRlj3jLZxUuyoTV3QMDM3XZa_Fo07JxFKPIJG8CeTcmFxD1xAGlShYug-GkiYDjHi1H30mPERX4X_ih3_Xr1UBI3kcktddxUvGAEBFQ8MTcK1lshSNe4mzcT3-DHJT1McnyfNxPoqb3DsxMo6xRMincybqe949GqeT-pk2TfGPu_aqNOvQRoQEFwAmd2QrBgFaGeXLLvoDCt2JgDapNsPfcAFFgeknE0dfVWcv1SQMQXFL48w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس نیوز هم به درخواست استعفای پزشکیان پرداخته:
FoxNews
چند مقام دولتی با تکذیب شایعه استعفای مسعود پزشکیان، آن را «خبر کذب با هدف ایجاد ناامیدی» خواندند.
فاطمه مهاجرانی، سخنگوی دولت، الیاس حضرتی و علی احمدنیا که از اعضای شورای اطلاع رسانی دولت مسعود پزشکیان هستند در پست‌های جداگانه به ادامه کار رئیس جمهوری و تلاش او برای «حل مسائل کشور» اشاره کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/75825" target="_blank">📅 00:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75824">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DQ5o53sbbXAesTNRlc7IpexdXkbhQGqGLKRItovuzi54I7g9MVFGb4mzrS1v91o4h9S3M9S4MA9j39fa7PGyJde83mHJ9e1vekVdiJSvaFW-I4-5BpRMp7dTC0ByFosV2aUxOOThKdLQH7Gj_nLyolEmwipxfmu7NVk__j94Zr1vlGPfzVx0-wGEYwIvkNnDjLlhKdvzELl_ZUEnTU8_aU0-BY-Pjrt9L-p6EHY00QcvLtQtOj8_eGa8vFTMWbG5HF8uxoE7npbMLLb_4RpRfgVyrdYV6gWXO9TQGU8JtrvVQRnrqkx4YCarqG4iGSluBRiMs7pA06UR_Ktw0pI7ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های جمهوری اسلامی وقوع دو انفجار را که تقریبا هم‌زمان در تهران و کرمانشاه و در ساعات پایانی یکشنبه گزارش شد به نشت گاز نسبت دادند.
سایت تسنیم، نزدیک به سپاه پاسداران اعلام کرد که در ساعات پایانی روز یکشنبه، «انفجار گاز» در محله باغ ابریشم کرمانشاه باعث مصدومیت ۲ نفر شد.
این سایت‌ همچنین [با انتشار عکس بالا] مدعی شد که انفجار در یک واحد مسکونی در «فاز یک اندیشه» در استان تهران ناشی از «نشت گاز» بوده است.
خبرگزاری ایسنا به نقل از سخنگوی اورژانس استان تهران می‌گوید این انفجار تاکنون ۶ مصدوم بر جای گذاشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/75824" target="_blank">📅 23:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75823">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c3fc33b86.mp4?token=lxz0NNmM0W3IA-flyVTD-2tjG2zKt61avwhszlDKxMm3yK2juuNYlpBBcO5P31R26k84nBBDw0UFeDmg6vW_z1Vo0KdixDK5VRXTCy3HHcAEWl9O1OpAtJxAo0MgpI4khFIH3vBaVxFIarp52tY4mQmMWH5-Py2wu9_AJlUbrUoxM9uCOF19R6Vhezia_VWOHFHZF0AsLAXj1yOsgbdVwBOLUzNfq_MFOpfG4HsMey4mZwUMrvcSALH3dCw_t9h1MOmRu1NQr-ExVP6mn8xHAh78EPrvitDt1xTbFEgKBrNFm70ZKUesJbyIP48RpUfbNJ2GN4WW9_bGUxFjLCMx3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c3fc33b86.mp4?token=lxz0NNmM0W3IA-flyVTD-2tjG2zKt61avwhszlDKxMm3yK2juuNYlpBBcO5P31R26k84nBBDw0UFeDmg6vW_z1Vo0KdixDK5VRXTCy3HHcAEWl9O1OpAtJxAo0MgpI4khFIH3vBaVxFIarp52tY4mQmMWH5-Py2wu9_AJlUbrUoxM9uCOF19R6Vhezia_VWOHFHZF0AsLAXj1yOsgbdVwBOLUzNfq_MFOpfG4HsMey4mZwUMrvcSALH3dCw_t9h1MOmRu1NQr-ExVP6mn8xHAh78EPrvitDt1xTbFEgKBrNFm70ZKUesJbyIP48RpUfbNJ2GN4WW9_bGUxFjLCMx3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران انقلاب اسلامی، در واکنش به گزارش شبکه ایران اینترنشنال درباره استعفای مسعود پزشکیان، رییس دولت، این خبر را تکذیب کرد و آن را «شایعه‌سازی» خواند.
شبکه ایران اینترنشنال، ساعاتی پیش در گزارشی اعلام کرد مسعود پزشکیان در نامه‌ای رسمی به دفتر مجتبی خامنه‌ای، رهبر جمهوری اسلامی، خواستار کناره‌گیری از سمت خود شده است. این رسانه همچنین نوشت در این نامه به وجود اختلافات ساختاری در اداره کشور و نقش نهادهای نظامی در تصمیم‌گیری‌های کلان اشاره شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/75823" target="_blank">📅 21:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75822">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SnmFNKkOS8_uFA_RgIZrUVQIaGT7Dqe4BPowBZvGp9L5B2us-JhclYVbz16cGgDND6ZG2umDcwQN6LamXSih_aYwGtT46575AQKbIvhE59pBC0sXNBpJzHtq-XBND59vIgsi9a6ACj9Kv8CaKuTkV5N5eUMXs79kkdV7Dx5rUZTMgQMLyByd_pfQM5CrMPbSziH-mTapwDjQhHI8S_dlZ_bH6S9dMifFHZToeVP_QCQ1Pvj-gwzAj6nkAbsQWHfYnoXrRje8KhP8SMMQf29HKiI20fm4EAJ6MAlQshDE85QGer2uW_nbHEd4iJl8eKHru59PGTouS-eIwpR0oa1uHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/75822" target="_blank">📅 20:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75821">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnlZ7ltLnJbji9IKyabLiYNKITSkuGff6I50qeL8RvtyDDghOc-AmEnJjVfYwVaBj5-_2cMExtbh0L8jgH-pgxUSUDKc_YHeGvRJomWznWvMgByGiehVgRdgLNJsV3JRKwfrJjQzKDDTlh8_jOds-wtA1R47sPq78KKvPpHcFnEupOGUOIkThc2Ssc_qEBx6VxPK43w6a5PQ_KamU03p2fJK2HUW-Rrx76UNCHJ5E2qCyVIg-qqdpf1YXxOZtt6GnUEjDpdFvBzT_OUWmMkrdjsP6CYvLtYmixyYy3sTjRA4YG-2fIataycaAmH0btfU0OK0ZxD3qRn6_hy5gW-acQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پیاهو، مردی که تصویر معترض نشسته مقابل نیروهای پلیس یگان ویژه در مقابل پاساژ علاالدین در آغاز اعتراضات دی ماه سال گذشته را منتشر کرد،
به گفته وکیلش
به ۱۰ سال زندان محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/75821" target="_blank">📅 19:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75820">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6220710705.mp4?token=jIYW7kiX8QpHcwkjM6-wJqbX6nkOW42np_gUuef4SI4g2jwA0Cene6c0aJvp6VP7HLiRxq2j68ghVnWbFZyFiXf9BOZMDoXFp1ZjLjtDp4SSNnHg-I5Qtd1p7WkwiSqyho5RARjoSAx9Eb-XWCcgfhGco0noQ1hZlWV3d_-n3YaqX9vxuKLANud4PRoF1_GZ4uFZgdt60p1o3mat-SixlksZIbHv4pg2_5q9gD85x0jY1AHu8uz5sMTjQFVGz9xi4vnOE_3MqJM17gJuimAHodud2mERBDaD5g1nBxRdrl9F-ltLWJnTPki_b6vTJi-DctBQgGIMAG5ZAQWXNGoxRA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6220710705.mp4?token=jIYW7kiX8QpHcwkjM6-wJqbX6nkOW42np_gUuef4SI4g2jwA0Cene6c0aJvp6VP7HLiRxq2j68ghVnWbFZyFiXf9BOZMDoXFp1ZjLjtDp4SSNnHg-I5Qtd1p7WkwiSqyho5RARjoSAx9Eb-XWCcgfhGco0noQ1hZlWV3d_-n3YaqX9vxuKLANud4PRoF1_GZ4uFZgdt60p1o3mat-SixlksZIbHv4pg2_5q9gD85x0jY1AHu8uz5sMTjQFVGz9xi4vnOE_3MqJM17gJuimAHodud2mERBDaD5g1nBxRdrl9F-ltLWJnTPki_b6vTJi-DctBQgGIMAG5ZAQWXNGoxRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، در گفت‌وگو با فاکس‌نیوز درباره ایران اعلام کرد: لایه اول و دوم حکومت آن‌ها از بین رفته و اکنون با لایه سوم روبه‌رو هستیم. شاید آن‌ها دیده‌اند برای بقیه چه اتفاقی افتاد و می‌بینند ترامپ آماده انجام چه اقداماتی است.
بسنت افزود: اگر ترامپ با این توافق موافقت کند، همین حالا به رهبران جمهوری اسلامی می‌گویم که او این توافق را هم از نظر نظامی و هم از نظر اقتصادی اجرا خواهد کرد. آزادی کشتیرانی در خلیج فارس از طریق تنگه هرمز باید به وضعیت پیشین بازگردد.
او درباره اینکه آیا ترامپ «کار را تمام خواهد کرد» گفت: اگر «تمام کردن کار» یعنی اطمینان از باز بودن تنگه هرمز، در اختیار گرفتن اورانیوم با غنای بالا و نداشتن سلاح هسته‌ای از سوی جمهوری اسلامی، پس کار تمام شده است.
بسنت تاکید کرد: چه از طریق مداخله نظامی، چه محاصره یا فشار اقتصادی، این نخستین بار در ۴۷ سال گذشته است که ایرانی‌ها درباره نداشتن سلاح هسته‌ای گفت‌وگو می‌کنند. این موضوع پیش‌تر ممنوعه بود و اکنون برای نخستین بار روی میز مذاکره قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/75820" target="_blank">📅 19:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75819">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفرهمند عليپور Farahmand Alipour</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=AMmcux8ZvCP1OsOBGXhElc5yfGTFyOTRmogmzywdv1ZkfD_fzkxbmL4McxlSuUkVDAcwNehOavPCXppQ2bFWHWJWiyJNjYSZYEU4xYP111YNhks2NnSnCeVe6WvE_WtUrw_W5EQMYA2pZk8Q8o0UPSCtdA_Ujmqjckf1GQuG1rjv2Ls6M1_UTBRwhebNgUnkKuIAjkydNV5r4Fv7DRjuegDu2eC1WfsWpsKutsR7memDrppOE6U6gxAtmBfNTfW_axCNzI-MTXJYZsCIvQ7DSzmq_3cM7wzhwwM7XUyAFxkPh8Hv5e8QYk6NlHkXuOpdKQvn5UAawC90piVBiMnyQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=AMmcux8ZvCP1OsOBGXhElc5yfGTFyOTRmogmzywdv1ZkfD_fzkxbmL4McxlSuUkVDAcwNehOavPCXppQ2bFWHWJWiyJNjYSZYEU4xYP111YNhks2NnSnCeVe6WvE_WtUrw_W5EQMYA2pZk8Q8o0UPSCtdA_Ujmqjckf1GQuG1rjv2Ls6M1_UTBRwhebNgUnkKuIAjkydNV5r4Fv7DRjuegDu2eC1WfsWpsKutsR7memDrppOE6U6gxAtmBfNTfW_axCNzI-MTXJYZsCIvQ7DSzmq_3cM7wzhwwM7XUyAFxkPh8Hv5e8QYk6NlHkXuOpdKQvn5UAawC90piVBiMnyQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴
در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته
«دو گزینه بیشتر نیست»
یا جنگ و خونریزی یا مذاکره مستقیم
«برای از بین بردن غنی‌سازی و موشکی»
این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات آمریکا و جمهوری اسلامی همچنان همون چیزهایی بودند که باعث یک جنگ شد، و این مصاحبه یک ماه پیش از آن بود که دست به قتل‌عام مردم در خیابان‌ها بزنید!
الان هم محور مذاکرات کاملا مشخصه!
همون چیزهایی است که جنگ ۱۲ روزه رو رقم زد. همون چیزهایی است که در آبان ماه عراقچی در تلویزیون گفت.
خون تک‌تک ایرانیان از جمله کودکان میناب پای شماست! شما طرف مذاکره بودید، شما انتخاب کننده و تصمیم گیر بودید.
و شما بین اورانیوم و موشک، و یا جان مردم، زیرساخت‌های کشور، فولاد و پتروشیمی و…
اورانیوم و موشک و دشمنی با اسرائیل و آمریکا رو انتخاب کردید! هنوز هم طرف مذاکره و تصمیم‌گیر شما هستید! و‌ جنگ ‌از سر گرفته بشه باز تصمیم و انتخاب شماست و مقصر شما هستید!
نمی‌توانید پشت کودکان میناب قایم بشید و از کشتار دیماه فرار کنید!
هر خون و ‌هر ویرانی ، همه پای شماست.</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/75819" target="_blank">📅 19:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75818">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ogxP17P9lGoh4Z2yhxZ7Ss4abDS_hC8y8FDsfbi30EpFROrQNjFveChgDVWnPh4b-UQPP7G-DmrxKjEP_tTaFCV6wtHOipZdIS8zcWuuFCYf220EesUMs4FYXbW-392BnOzM-wi5Ze0vJrxBy86hjOlnY_PP8akG1-BpSd9nDGImIh3P9MYDJ7IsiSbfOcs-BT_hOTpPw2lYCgYjPTTwekexQRZ7omsVXvXR7ZINzBku9IHnIwHtJ3S6tcSF-GGUh6AXgNPuv4nrr3qwT3IsZKJnG0_dKK4m2HzADGE4RPcBEAaxqAHNFLaLBxjeZj9WL3uJJI9eWD8n4kmg3_GHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسن و حسین امیری، دو برادر دوقلوی ۲۰ ساله محبوس در زندان قزلحصار کرج، از سوی شعبه ۲۶ دادگاه انقلاب تهران به ریاست قاضی ایمان افشاری به اعدام محکوم شدند.
بر اساس اطلاعات دریافتی هرانا، مبنای صدور این رای اتهام «جاسوسی برای اسراییل» عنوان شده است.
یک منبع مطلع در گفت‌وگو با هرانا اعلام کرد در کیفرخواست صادرشده علیه حسن و حسین امیری، مشاهده تصاویری از ساختمان‌های آسیب‌دیده به عنوان مستند اتهام «جاسوسی به نفع اسراییل» مورد استناد قرار گرفته است.
این منبع همچنین گفت: «حسن و حسین امیری به دستور بازپرس پرونده به صورت جداگانه در زندان قزلحصار نگهداری می‌شوند و از حق ملاقات با یکدیگر محروم هستند. این دو زندانی در حال حاضر در سوییت ۳۵ این زندان محبوس هستند.»
بر اساس این گزارش، این دو برادر پیشتر در یکی از ایست‌های بازرسی و پس از بررسی تلفن همراهشان بازداشت شدند.آن‌ها پس از بازداشت، به مدت دو ماه در وضعیت بلاتکلیف در زندان قزلحصار کرج نگهداری شدند.
👈
حسن و حسین امیری از دو سالگی در مراکز بهزیستی پرورش یافته‌اند و خانواده‌ای برای پیگیری وضعیت قضایی و حقوقی خود ندارند. به گفته آشنایان این دو جوان، نبود حامی خانوادگی بر نگرانی‌ها درباره روند رسیدگی به پرونده آنان افزوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/75818" target="_blank">📅 18:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75817">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nag3LSDdVSly8OAduhc6f83JbDXi7rxzUOjd3BvBFXQpJzMbt0rMdwkIA6ZxwVuRWkL9n43BmhuFdj13neEchpkXGKU5RSE-jhCvXYp6IUexSj_pI_dC02_LPYee5hFLXIVssVUt-lljnUOLf1fGmHlNX3GhdY5iEWCYlQJGoxCq_Fj4ev-v2RD0y929-irN5Cl5fACRMiE5QdndI1YwbkpRB_jF4p0SjAIxxI0R9gZaWc8YctaPTdabwlvIlq7LsGKMk120DcXU_agBf1BpWIk3Pq4tsig6GBSSzckuacd2rpwabirSQS2FN9SX92aH9q77rYVhO7uFGs5jVWYA4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: ایران چندین ورودی تأسیسات موشکی زیرزمینی خود را بازگشایی کرده است
شبکه خبری سی‌ان‌ان روز یکشنبه ۱۰ خرداد با استناد به تصاویر ماهواره‌ای اعلام کرد ایران توانسته از زمان توقف جنگ شماری از زرادخانه‌های موشکی مدفون خود بر اثر حملات هوایی آمریکا و اسرائیل را از زیر خاک بیرون بیاورد.
حملات آمریکا و اسرائیل با تخریب جاده‌ها و مسدود کردن ورودی تونل‌ها، دسترسی ایران به پایگاه‌های موشکی زیرزمینی را محدود کرده بود.
سی‌ان‌ان ادعا کرده است که ایران تاکنون ۵۰ مورد از ۶۹ ورودی تونلی را که در ۱۸ تأسیسات موشکی زیرزمینی توسط آمریکا و اسرائیل هدف قرار گرفته بودند، بازگشایی کرده است، از جمله در پایگاه‌هایی در خارج از اصفهان و در اطراف خمین.
بر اساس گزارش این شبکه خبری، ایران همچنین بخش‌های دیگری از این پایگاه‌ها را نیز ترمیم کرده است؛ از جمله جاده‌هایی که آمریکا و اسرائیل برای جلوگیری از تردد پرتابگرهای موشکی بمباران کرده بودند. تصاویر ماهواره‌ای نشان می‌دهند که تقریباً تمامی گودال‌های ناشی از بمباران اکنون پر شده‌اند و در دو پایگاه، این جاده‌ها حتی دوباره آسفالت شده‌اند.
ایران شبکه پایگاه‌های زیرزمینی خود را در عمق خاک و در مواردی زیر کوه‌ها ساخته است تا در برابر حملات هوایی مصون باشند، به همین دلیل آمریکا و اسرائیل بسیاری از ورودی‌های این تأسیسات را بمباران کردند؛ اقدامی که در کنار تلاش برای شناسایی و نابود کردن پرتابگرهای موشکی، باعث شد توان ایران برای شلیک موشک به‌طور قابل توجهی محدود شود.
این حملات خسارت سنگینی به پایگاه‌ها وارد کرد؛ به‌گونه‌ای که بیشتر ورودی‌های تونل‌ها زیر حجم عظیمی از آوار مدفون شدند و جاده‌های منتهی به این سایت‌ها نیز به‌شدت تخریب شدند.
سی‌ان‌ان می‌گوید باز کردن ورودی تأسیسات موشکی زیرزمینی می‌تواند به ایران این قابلیت را دهد که در صورت وقوع دور جدیدی از درگیری‌ها، موشک‌های بالستیک بیشتری نسبت به اواخر جنگ ۴۰ روزه به سمت اسرائیل و کشورهای دیگر شلیک کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/75817" target="_blank">📅 18:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75816">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/im-Eclq1664K-c9QV3df4PUctzSndh-jabOS-YqmOEHLPCThiKlE6jFvbXkk8YF0TxGvtvLtTmuiKRfD_ckR4p8vx_bygkCqr745HtqBPDXw8VcmWeyY08zlP3hnjH1tsjixrXCJMUucDvj0CEgnaago6nmXzVXn7JvzVB0WXAMgo0OQGh6CAXa7dN7tLL7omJzXfei2f71K0TSCP1w8bhYjNGqmqTQCdUY41qYgMIIIBl_Bvf_Cp6ZDaMTZI5egn8YuxJpYEtzxDBfZR7EE0Ax5VzqkMMP8IdsnIvqy2dXswYhBqaEUw8D_Is4hhCKQdY9g5UqrqkAg6eqQQsSgVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس مصوبه جدید شورای شهر تهران، هزینه خدمات مرتبط با خاکسپاری در بهشت‌زهرا به‌طور میانگین حدود ۴۰ درصد افزایش یافته و در برخی موارد رشد تعرفه‌ها به ۵۰ درصد رسیده است.
روزنامه دنیای اقتصاد گزارش داد نرخ خدماتی از جمله حمل متوفی، تغسیل، تکفین، تدفین و برگزاری مراسم افزایش یافته است. بر اساس این مصوبه، هزینه انتقال هر متوفی از سطح شهر تهران تا شعاع ۱۰ کیلومتری ۵۰ درصد افزایش داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/75816" target="_blank">📅 15:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75815">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0driHRYW0A7v2IwzCuDTq24ANWg_O-EnbrUGDlulNeHdMEMcaSXrSYwtRNJiBOG8-omIRIRGLUsqu8b8iukOZ-nxLFRS1_SZzRj2e507B9WLaqbNNbvelgwE-RJzsKpTOKROh-Zy6P-_DwPQXYiuPe9zzvKpBJewJfSz6QzczMC448nRhMsp_ROFS2YC_fkClttzIXPUP__x3oBY9SECZxXcS5lzKn6k5S_pGre7XfzPjQz3UdLJxRWUxaAhNEChmMlFPQI47f0raSJPe3IRQmSO9pL8jHBEtEL_hZ5FuuCUNeKL_hsvq4iS6VMbdSuyII96Qg0Pk3WVs2MzdgeLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت هرانا گزارش داد زهرا شهباز طبری، زندانی سیاسی محبوس در زندان لاکان رشت، پس از نقض حکم پیشین در دیوان عالی کشور، بار دیگر از سوی شعبه دوم دادگاه انقلاب رشت به ریاست محمدعلی درویش‌گفتار، به اتهام «بغی از طریق عضویت و فعالیت در سازمان مجاهدین خلق» به اعدام محکوم شد.
این زندانی سیاسی ۶۸ ساله، در فروردین ۱۴۰۴ در منزل شخصی خود در رشت بازداشت شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/75815" target="_blank">📅 15:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75814">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PG5XzFVp7lZqqsKjH9ftTDAOhLg8gPCr1lxXn9DHMbMbU8R1NV-qL-XQUhVARcdh0fmUeyupHAUQl6nbiTBCgKUo67jHkAYR_41wLkKljWQ6PkmEVyjPGqY5lKnYaRCs0jUU7Lrjamib88qJ7q42hbIu9NyV9fN74JtDV8ZOwLqrJQhPyDyuvedpcVp_ieyQKhx23X5EzB28qq0-89rVQKCbfBh608II8oRXIi5i3hFG13q_I15Vjk4vR9jmQNozXUWHdKfvfz8KKXEIc-iJVLvWhJWCAaKJaUglKoYSaqm-PNP239jyl-6k3oNXTVkzHtqoljy6Gcsn_Mjs-P-FJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران روز یک‌شنبه اعلام کرد‌ «طی شبانه‌روز گذشته ۲۸ فروند کشتی اعم از نفتکش، کانتینربَر و سایر کشتی‌های تجاری پس از کسب مجوز با هماهنگی و تأمین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.»
ساعتی پیشتر روزنامه اسرائیلی «اسرائیل هیوم» نوشته بود که ده‌ها نفتکش حامل نفت و گاز طبیعی مایع در هفتهٔ گذشته با اجازه آمریکا و پرداخت عوارض به ایران از تنگهٔ هرمز عبور کرده‌اند.
این در حالی است که دولت آمریکا بارها اعلام کرده است با پرداخت عوارض به ایران برای عبور از تنگه هرمز مخالف است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/75814" target="_blank">📅 15:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75812">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OkLwa3vloKAvmizpkwhKX3VTjIWGfTAC1vNLvjz3-wr0WHQzZFJ3XTd_zdWznFkw1Yj8k7UGzC0eL-2RnTs98lDjyomlo9r1zCqDlwqTm-AjalNQN5NnSPolRY9m4H0jZcTGBBEOUpToEmrimEsMixBZnQDlWTWGAKdiYlyOSMaiqB8iKWHZTk3CQiRrrij-ODYTYQ7KJLaDNhT5jtwZCl1TJeqpRptLs3K7fxML29BCuu7g8T_mH0T7W_EN9twRHumKyGt8SkRsCglAjnT_9Xbiir1HXfVb-rPbhZvLqHK7jVoV1DnQ0C_mKlsBFM6f-t2b0NDxukFcFDpU1E1IYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9b60ac63f.mp4?token=glDa4LN3Q1Oeckse6CuKWwY1RkKOkI9y7Afd5HEtFfyLZTbal7_tCejxhA7qkMNkAuoR6K2MIXCRJy-771mhXS1o-Yph1P3E4N1ADvvZIPrr7cYyNp64zePSr3nKgRzQ55OxY_UIIlROaBbFGe0DVkkV_LwUAlikh67Rj7DaO9DJBrFuNN_RQmmKWZLkLjCqaio1ylC62REcjGCNY4k3aPDncEb2h2mi7QwuNfRWj0GJ3qqMPLkwcyqfisHHno8rmojMuVr6tPe565I2z7hJZZYbYk5FOQXaX1PTqcF7fD802L-J0KUGYXmvZ3NVt5_TzEAoettaFryRzCarN_jUPA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9b60ac63f.mp4?token=glDa4LN3Q1Oeckse6CuKWwY1RkKOkI9y7Afd5HEtFfyLZTbal7_tCejxhA7qkMNkAuoR6K2MIXCRJy-771mhXS1o-Yph1P3E4N1ADvvZIPrr7cYyNp64zePSr3nKgRzQ55OxY_UIIlROaBbFGe0DVkkV_LwUAlikh67Rj7DaO9DJBrFuNN_RQmmKWZLkLjCqaio1ylC62REcjGCNY4k3aPDncEb2h2mi7QwuNfRWj0GJ3qqMPLkwcyqfisHHno8rmojMuVr6tPe565I2z7hJZZYbYk5FOQXaX1PTqcF7fD802L-J0KUGYXmvZ3NVt5_TzEAoettaFryRzCarN_jUPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جلسه مجازی صحن مجلس شورای اسلامی به ریاست محمدباقر قالیباف و مشارکت آنلاین ۱۸۷ نماینده و حضور ۱۴ نماینده برگزار شد.
در این جلسه که اولین جلسه از سومین سال مجلس دوازدهم بود، اعضای جدید هیئت رئیسه مجلس سوگند یاد کردند.
جلسه روز یک‌شنبه، دهم خردادماه، همچون جلسات معدود گذشته در مکانی مخفی برگزار شد.
محمدباقر قالیباف در همین جلسه تأکید کرد که «تا اطمینان پیدا نکنیم که حقوق ملت ایران را گرفته‌ایم، هیچ توافقی تأیید نمی‌شود».
قالیباف که از او به عنوان رئیس هیئت مذاکره‌کننده ایران نیز یاد می‌شود در این جلسه بیانیه‌ای را قرائت کرد و در آن ادعا کرد که «در حال عقب نشاندن دشمن در یک جنگ تاریخ‌ساز هستیم».
@
VahidHeadline
محمدباقر قالیباف، رییس مجلس شورای اسلامی گفت: «سومین سال مجلس دوازدهم را در حالی آغاز می‌کنیم که یاد و خاطره رهبر شهید با ماست و هنوز فقدان رهبر و پدر امت را باور نمی‌کنیم.»
او ادامه داد: «رهبرمان به ما آموخت مقابل زورگویی و تهدید، ذره‌ای سر خم نکنیم و با مشت‌های گره کرده مقابل خصم تا آخرین قطره خون مبارزه کنیم.»
قالیباف اضافه کرد: «دیدن جای خالی رهبری برایمان جانکاه است، ولی دلگرم به مدیریت و رهبری جدید هستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/75812" target="_blank">📅 15:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75810">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g8L7zapDWtr8N0X2eN-xTGZCBalYrPxt7oPCMzhhwEv0V_LgkfEfp__VUWFChilL9FWUry0qr_7WKvo8NGUUPinw9THsngstqNCLBBHeszgZFBSWLYa--J5zIdMDKheYpCZfx-FynoiGDI04AOglUzDHCzx8nqpDFAJ9cs4ubKFRuBfkc3XgIuwsJw45YUHBQcN31Dt_f4hwlRMnkD-SHJrKwPftP1YYk2-G9CYKLXRdzQBn3_L6-dwZMTkX571Y35-HSz7QeECEFUinY9SDWY3um77n7wVbqGsHWszr2LH4cTOpRbpXbvWXnOCLhHdRbW5t8Sy5cBA5FX65eJMnnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8e2c9e72d6.mp4?token=V9qcn7L2Osjhp1Gjdnp1UZWyDP1n-VeG4LuZSwyoD9whfroQcfo4AEfVCyDnQ9EztMpnB4kUtiG07Zi2zEo6r5sFG9aCridHpbRPf3Ht9ae0w5MdftGGba_jpO12_1HI8QBjAvK0jzm-8dkeYoEnX3WJuswca8J9n8FH7eii0cctwAxbDGV0ntNF5s1Xz5YDxVKQ4AzIJ5Km6QzfgktHkRyluFlGVXxNv5rnk_TDurbceuVbMAQho_DBirya960uLZaaWbQOYAhELNr5RZ7ZlBzQuo1I9Vh00qH1tAmoOpcDcjNX16OsJoxngDAZ3aXQrMeX2g1YN2OEZ28oVyPMiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8e2c9e72d6.mp4?token=V9qcn7L2Osjhp1Gjdnp1UZWyDP1n-VeG4LuZSwyoD9whfroQcfo4AEfVCyDnQ9EztMpnB4kUtiG07Zi2zEo6r5sFG9aCridHpbRPf3Ht9ae0w5MdftGGba_jpO12_1HI8QBjAvK0jzm-8dkeYoEnX3WJuswca8J9n8FH7eii0cctwAxbDGV0ntNF5s1Xz5YDxVKQ4AzIJ5Km6QzfgktHkRyluFlGVXxNv5rnk_TDurbceuVbMAQho_DBirya960uLZaaWbQOYAhELNr5RZ7ZlBzQuo1I9Vh00qH1tAmoOpcDcjNX16OsJoxngDAZ3aXQrMeX2g1YN2OEZ28oVyPMiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی انتظامی تهران کافه‌ای در خیابان ولیعصر را که در آن برنامه‌های موسیقی اجرا می‌شد، به بهانه آن چه «فعالیت‌های مروج فرقه‌های انحرافی» خواند، پلمب کرد.
مرکز اطلاع‌رسانی پلیس جمهوری اسلامی در اطلاعیه‌ای نوشت: «این کافه با برگزاری برنامه‌هایی با ظاهر موسیقی غربی، بستری برای حرکات نابهنجار، و آنچه که ماموران توصیف کرده‌اند "تحرکات شیطانی" فراهم آورده بود.»
نیروی انتظامی جمهوری اسلامی نام این کافه را ذکر نکرد اما ادعا کرد که «مشتریان این کافه، شامل دختران و پسران جوان، در وضعیتی غیرطبیعی و با حرکاتی عجیب و غریب، که از آن به عنوان “شیطانی” یاد شده، مشاهده گردیدند.»
پیشتر نیز بسیاری از کافه‌ها و اماکن کسب و کار به اتهام‌های مشابه پلمب شده‌ بودند اما جمهوری اسلامی سرکوب‌ شهروندان را از زمان اعتراضات دی‌ماه گذشته تاکنون شدت بیشتری داده است.
موج تازه اعدام‌ها، صدور احکام سنگین و بازداشت‌ها نگرانی فعالان و نهادهای حقوق بشری را برانگیخته است.
@
VahidHeadline
ویدیوی بالا رو هم به عنوان "تحرکات شیطانی" در اون کافه منتشر کردند!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/75810" target="_blank">📅 15:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75809">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PFgjokR3O-b2gLWRnPTaHqT6UfRRSjpYmsHfhvT9ZcwX6Gpdish2n4-IGQMWyv-Fy2SGn8oQ7rW3JfHvSyPteTJszbzF4Gfs2ZeY2THhCa5K_67luFziqDE1VMmnORJZorS6idSrXL2riv0GZNdyAQ9qf5OmTs8ar9FIyT8t5XW-zDKADGOfIfHI0sjX7DaulbXKcAH_qI_AYgrPIw_KA7kTqW95Hc9VsvfRONR59E_Vpbn66HfpTy1EFBwwo9-075QOKDyyWJlUkzOo8UHIhd18nI70Vmbk_4xbS3pfqpq40qzdEbMwQUi4KT7XdHSY1QcwUHtgJltmNV9wYmfGOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس، ترجمه ماشین:
رئیس‌جمهور ترامپ در جلسه‌ای که روز جمعه در اتاق وضعیت برگزار شد، خواستار چند اصلاح در توافقی شد که فرستادگانش با همتایان ایرانی خود به آن رسیده بودند؛ این را یک مقام ارشد دولت و منبع دومی که در جریان موضوع قرار گرفته بود، گفته‌اند.
...
مقام‌های ایرانی به رسانه‌های دولتی گفتند که آن‌ها نیز متن نهایی را تأیید نکرده‌اند؛ هرچند دو مقام آمریکایی پیش‌تر در طول هفته مدعی شده بودند که تهران آماده امضاست و همه چیز به تصمیم ترامپ بستگی دارد.
به گفته این دو منبع، ترامپ از تیم خود خواست تغییراتی در پیش‌نویس مربوط به بندهای برنامه هسته‌ای ایران ایجاد کنند.
در شکل فعلی، این تفاهم‌نامه شامل تعهد ایران به دنبال نکردن سلاح هسته‌ای است، اما امتیاز مشخص دیگری فراتر از آن در آن نیامده است.
در این متن آمده است که یک بازه ۶۰ روزه برای مذاکره درباره تعهدات هسته‌ای ایران و کاهش تحریم‌ها از سوی آمریکا وجود خواهد داشت؛ نخستین موضوعات در دستور کار نیز چگونگی تعیین تکلیف ذخایر اورانیوم غنی‌شده ایران و محدود کردن غنی‌سازی بیشتر خواهد بود.
ترامپ می‌خواهد تلاش کند این بخش را اصلاح کند.
یک مقام ارشد دولت گفت: «موضوع، جزئیات بیشتر درباره این است که آمریکا چگونه مواد را دریافت می‌کند و زمان‌بندی آن چگونه خواهد بود»؛ منظور او اورانیوم غنی‌شده بود.
منبع دوم گفت ترامپ همچنین می‌خواهد برخی از عبارت‌ها درباره بازگشایی تنگه هرمز را اصلاح کند.
این مقام آمریکایی گفت به ترامپ گفته شده است حدود سه روز طول می‌کشد تا ایرانی‌ها با پاسخ برگردند. این مقام ارشد دولت گفت: «آن‌ها عملا در غارها هستند و از ایمیل استفاده نمی‌کنند.»
این مقام ارشد دولت گفت: «توافقی در کار خواهد بود. اینکه چقدر قریب‌الوقوع است، باید دید. ما حاضریم صبر کنیم تا رئیس‌جمهور آنچه را خواسته به دست بیاورد. ممکن است یک هفته طول بکشد. ممکن است کمتر باشد. ممکن است بیشتر باشد. امیدواریم در آغاز هفته چیزی داشته باشیم.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/75809" target="_blank">📅 05:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75808">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boS_orG-A_rbpxRGYEiSFgn0i46YGM-uhu7PMjh900HPFddq4wD4nl0c6brMym7dvTonkPo73d0klwtux1ZDFLxgsiRqxgK2CnViejoZboY4PwrGJyXyGZWs1E3pwauK8ywbDevafrbco08fKIVJUEeHXknKq5AdwjN-9jh3XNGiMqo0jfRO67LGMELNRnkZVGSOR7zF2u9WVryZZBCNRhhZ60Ur69DjdoN2ue5AarkM6DYihl9NO0H_b6Slu78xa7U17Bcj4ooWb9l3N3hMyekeCqa3wVpVjyUV7TAKFBnn7Mua23YfPJOCwDEJebYhd3NpucVkHlwvdQ34D3epFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط‌عمومی سپاه بامداد یکشنبه، ۱۰ خردادماه، اعلام کرد یک پهپاد «ام‌کیو۱» (MQ1) ارتش آمریکا را منهدم کرده است.
خبرگزاری فارس نوشت: «این پهپاد با ورود به آب‌های سرزمینی ایران قصد انجام عملیات خصمانه داشت که بلافاصله در رصد و هدف موشک‌های پدافند سپاه قرار گرفت و سرنگون شد».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/75808" target="_blank">📅 04:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75807">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rC4h5t1J71IfuPs_Swy_4WuZURkPomKR8DIazDgi3bVY9O9quiDwcTA62PrchtLRwXg_bKiWUpnIOID6BwgJQac-XDwO22nmW7eiBL0DgqQXfw7-GbnfEOHGx0G4vfXVg3sZVBjfvyon8oIO3HurnWI9LJj_7Bg5RUGo-XBPuM2yUnBDhOq0H2uWpROqIrv6qMf9r5YDIMDC5rlkLm5t0UUH3uM-ObzHboajsGmuDfghezjToqvEymCRNzEWMvHfUqut9qAYFv0Sv76cVFUA2CsGk5nRROHJed0xgPq7mqoTOlTHQTY7B0vjwm2sBsk9YwMCD_sjfFxE0zEpqo_N3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی ارتش آمریکا، سنتکام، اعلام کرد نیروهای این کشور یک کشتی تجاری با پرچم گامبیا را که به گفته واشینگتن در نقض محاصره دریایی به سمت یکی از بنادر ایران در حرکت بود، در خلیج عمان هدف قرار داده و از ادامه مسیر آن جلوگیری کرده‌اند.
سنتکام روز شنبه نهم خرداد در بیانیه‌ای گفت نیروهای آمریکایی روز هشتم خرداد کشتی «لیان استار» را هنگام حرکت در آب‌های بین‌المللی به سوی یکی از بنادر ایران شناسایی کردند و بیش از ۲۰ بار به خدمه آن هشدار دادند.
به گفته این نهاد نظامی، پس از آنکه خدمه کشتی به هشدارها توجه نکردند، یک هواپیمای آمریکایی با شلیک موشک هلفایر به اتاق موتور کشتی، آن را از کار انداخت.
سنتکام افزود این کشتی دیگر به سمت ایران در حرکت نیست.
در این بیانیه آمده است که از زمان اجرای محاصره دریایی علیه ایران، نیروهای آمریکایی پنج کشتی تجاری را از کار انداخته و ۱۱۶ کشتی دیگر را وادار به تغییر مسیر کرده‌اند.
سنتکام جزئیات بیشتری درباره محموله کشتی یا مقصد دقیق آن در ایران ارائه نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/75807" target="_blank">📅 21:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75806">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSTWsmn6VkjshP_raLbGgx12ARUP1nSxY7CjaA2uwmhnFFoONrn3FxWE04GPCGqGZiS8EvaAivFy676FEETF8eBhUWKX3ONKrIKB5tGvAQfZuILkHBzc1kE_wjbY8AyzEI_dmLL4aWGKv_u3QugOchpj6BYTwHCW9KAAX_qEpxkd-dLp1Li4f4gBpO4krLxgy4qODrRpxWCVmzgJ9SpD-JH10Oa9f0Ckbxs3B4xJ51VymZrUPBIuRPaUVAmETdkit-pG2V7mxk5VV8dKKxtZiKhCNWiRNkNd40bz3N2ateCIg5fjusahXao8dYn9RIHn2xlxSq9kCSebACiV2J6bKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی در گزارشی درباره تفاهم احتمالی بین تهران و واشینگتن با عنوان «جزئیات غیررسمی»، اعلام کرد آمریکا متعهد شده در طول ۶۰ روز امکان دسترسی جمهوری اسلامی به ۱۲ میلیارد دلار از دارایی‌ها را به‌گونه‌ای فراهم کند که این منابع قابلیت انتقال و هزینه‌کرد در بانک‌های مقصد را بدون محدودیت داشته باشد.
این گزارش افزود که بر اساس این تفاهم، جمهوری اسلامی مرجع انحصاری تشخیص ماهیت شناورهای عبوری است و هر شناوری که محموله آن تهدیدآمیز شناخته شود یا بهره‌بردار نهایی آن در «خصومت» با جمهوری اسلامی باشد، به عنوان کشتی تجاری شناخته نشده و اجازه عبور از مسیرهای تعریف‌شده را ندارد.
صدا و سیما تاکید کرد که این رونوشت هنوز در حکم یک تفاهم غیررسمی است چون مسیر آن همچنان در چرخه بررسی، مذاکره و بازبینی قرار دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/75806" target="_blank">📅 21:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75805">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIombIB-hTtsftbzj8-rfzOh3UB0hePQmwWnKVgPviP9b0lnBfnSWa1QStYG1OHx-f2r15V5WGQQoEnR1mRVqRWhRDNgSA58MlNXfeOjWGs4eCc82N7rFWPjf7RQK2sCWnf6wxOR2bpVa9-4CN1eTrrkNmogQ3j6i4CInot6akVms69jRZAXHZSqNiOx3I2W33D52N6JfZMTZS8LJG9f9yDK5g1sAHkuZjnQHF7n3LUHjY6SmKeAVobL5Zj5xZRRzadzVvx7dyWOjhA2hYx6Hz6zlnRmwIVRNh-B4-igZnCgoqXfzXZzqUhND0Jb_fLBbMragFhJmIVB0NMj98F-jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش نیویورک‌پست، در پی حمله موشکی جمهوری اسلامی به یک پایگاه هوایی در کویت، چند نفر از نیروهای نظامی و پیمانکاران آمریکایی مجروح شدند. این حمله در حالی رخ می‌دهد که دونالد ترامپ، رئیس‌جمهوری آمریکا، در حال ارزیابی پذیرش آخرین پیشنهاد صلح تهران یا بازگشت به شرایط جنگی است.
یک منبع مطلع روز شنبه نهم خرداد، اعلام کرد که در پی رهگیری یک موشک «فاتح-۱۱۰» توسط پدافند هوایی کویت طی ۲۴ ساعت گذشته، قطعات و ترکش‌های ناشی از انهدام موشک بر فراز پایگاه هوایی «علی السالم» فرود آمده و منجر به جراحت سطحی چند آمریکایی شده است. این حادثه همچنین خسارت شدیدی به دو پهپاد «ام‌کیو-۹ ریپر» (MQ-9 Reaper) به ارزش تقریبی ۳۰ میلیون دلار وارد کرده است.
این حمله در شرایطی صورت گرفته که دونالد ترامپ روز جمعه با تیم امنیتی خود تشکیل جلسه داد و اعلام کرد که قصد دارد تصمیم نهایی را درباره توافق با ایران اتخاذ کند؛ توافقی که شامل تمدید ۶۰ روزه آتش‌بس، بازگشایی تنگه هرمز و آغاز مذاکرات بیشتر درباره مواد هسته‌ای ایران در ازای لغو محاصره دریایی آمریکا می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/75805" target="_blank">📅 21:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75804">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YNygapKjOksVOt6XoCOG0bOzMQhiDV7w4fE3-VcYJVpYW5P5_w_tIEoDOQKOrLD_iuWs7y7g8_illonfGgU7TYLUk1zCs7vvyvgx2iinbqYBYB9D3Yj3yjAZLMoY7YAi7QLG-GTW4ruKAWc1yHkjOfgBsVsIV3mPpOTNuaumXOzQRod5tq7Tr_LooS5kOuRHIa-4zh9YzvJDUCa6jHgh9G1HDmsX-uVbH6wkR7ixuKW--tueIiwl059PHs4LBK8QnyRMM2QsYvOdAkodzaDhBoLiECrRkU6H4KBU34PKpEPyTlwnGHW4LEohJmVQvqDA3ukDuzmH0TNhsWToFvtlkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا در بیانیه‌ای اعلام کرد که هرگونه اقدام شناورهای نظامی جهت مداخله در مدیریت تنگه هرمز یا ایجاد اختلال در تردد، مورد هدف نیروهای مسلح جمهوری اسلامی قرار خواهد گرفت.
در این بیانیه آمده: «هرگونه تخلف از این ضوابط، امنیت تردد آن‌ها را با مخاطره جدی مواجه خواهد کرد.»
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد کلیه کشتی‌ها، شناورهای تجاری و نفتکش‌ها صرفا ملزم به تردد از مسیرهای تعیین‌شده و اخذ مجوز از نیروی دریایی سپاه پاسداران هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/75804" target="_blank">📅 19:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75803">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83c715fa8b.mp4?token=OqxB0rdi3p7oGBbrpgxzn_hEi7PkSl-q9QcleQgdziQ_0JWZtnH1hJ7-ft1YMmt4qPJr3swwnbRDrId1k8wBdyA5TENUX-0Y0p7QEj9i8GTYtUhDqpqVjvF2ifX05sxKsvLSDIfB3t_H9JedLcLc6S1Di3Th0dv-0nZ4pIsrmYfL9LnCskRHFMDIBSYnoRaM2H43ZES0KQ0jFOhtjgb5HZJhNqzpXBP35jRncpo6eGh6ArqgGD2lVY9t1_vQlfifbUvq2UYsMhksBj0oufnIwwpUHuk4LqrZnkCgoltRUu8a2jqnIud9FOQYTYjVU6K_cLkgfW5QMahqMrvqGZnCgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83c715fa8b.mp4?token=OqxB0rdi3p7oGBbrpgxzn_hEi7PkSl-q9QcleQgdziQ_0JWZtnH1hJ7-ft1YMmt4qPJr3swwnbRDrId1k8wBdyA5TENUX-0Y0p7QEj9i8GTYtUhDqpqVjvF2ifX05sxKsvLSDIfB3t_H9JedLcLc6S1Di3Th0dv-0nZ4pIsrmYfL9LnCskRHFMDIBSYnoRaM2H43ZES0KQ0jFOhtjgb5HZJhNqzpXBP35jRncpo6eGh6ArqgGD2lVY9t1_vQlfifbUvq2UYsMhksBj0oufnIwwpUHuk4LqrZnkCgoltRUu8a2jqnIud9FOQYTYjVU6K_cLkgfW5QMahqMrvqGZnCgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا، روز شنبه نهم خرداد گفت ایالات متحده در صورتی که مذاکرات با ایران به توافق منجر نشود، آماده ازسرگیری حملات علیه جمهوری اسلامی است.
هگست در جمع خبرنگاران گفت: «در حال حاضر تمرکز ما بر حفظ آمادگی و آماده بودن برای بازگشت به عملیات است، اگر لازم باشد.»
او افزود دونالد ترامپ «صبور» است و به دنبال دستیابی به «توافقی خوب» است که تضمین کند ایران هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
اظهارات وزیر دفاع آمریکا در حالی مطرح می‌شود که مذاکره‌کنندگان تهران و واشینگتن در تلاش‌اند اختلافات باقی‌مانده بر سر برنامه هسته‌ای ایران را برطرف کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/75803" target="_blank">📅 18:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75802">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dcIgqFGlMMB7fuqfbHCGuVeDjaJrHWKx2zRswJD4VJd-RgRg6cd9-zOFeqXQ45xTXmjbirchI0vfMSzhktKflH1Mx5zRoJIEy0OBEEUFk5Jc9a9F4Ahc7jgwiHnYk36SGBU-BkWyZRDXDvHa1d4prFmHQ2Jb_fCuvXGzmvJUHjgpPb2PdkdN8r-BBK-Ix1xp-Fa7uPflRV2wkkhC1sBx7uLsVqkll6BZofW257-LEFykZ7JRElg1lwtdKkpXmWO4HhHswvWGadBJYDqZWY-ltINUtGcd0vS-OVu3BDRtYTUTKu2DbN9_vlZPpfbJpiynsdW5b14IFL5Btx2ez52KGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی نیلی، وکیل دادگستری، اعلام کرد شعبه اول دادگاه انقلاب شیراز بنیامین نقدی را با اتهام «افساد فی‌الارض» به اعدام محکوم کرده است.
نیلی در گفت‌وگو با امتداد گفت که بنیامین نقدی شامگاه ۱۳ دی‌ماه در شیراز به دلیل شعله‌ور کردن یک کپسول آتش‌نشانی به سمت ماموران نیروی انتظامی بازداشت شد.
به گفته این وکیل دادگستری، در ابتدا اتهام «شروع به قتل» به موکلش تفهیم شد، اما پس از آن اتهام وی به «محاربه» تغییر یافت.
او افزود پس از پایان تحقیقات مقدماتی، کیفرخواست بنیامین نقدی با اتهام‌های «محاربه»، «عضویت در گروه‌های برهم‌زننده امنیت کشور»، «اجتماع و تبانی به قصد ارتکاب جرم علیه امنیت کشور» و «فعالیت تبلیغی علیه نظام» صادر شد. به گفته نیلی، در خصوص اتهام‌های «ایراد صدمه جسمانی به ماموران» و «حمل سلاح سرد» قرار منع تعقیب صادر شده بود.
نیلی همچنین گفت قضات شعبه اول دادگاه انقلاب شیراز در جریان رسیدگی، مجموعه اتهام‌های مطرح‌شده را مصداق «افساد فی‌الارض» تشخیص داده و بر همین اساس حکم اعدام برای بنیامین نقدی صادر کرده‌اند.
وکیل بنیامین نقدی با اشاره به قصد خود و همکارانش برای اعتراض به این رای گفت که در مهلت قانونی درخواست فرجام‌خواهی خواهند کرد. او ابراز امیدواری کرد که با توجه به این که به گفته وی در جریان رخداد مورد اشاره هیچ فردی آسیب ندیده است و اقدامات موکلش مصداق افساد فی‌الارض نیست، حکم صادره در دیوان عالی کشور نقض شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/75802" target="_blank">📅 18:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75801">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Akbarpour🔥نیما</strong></div>
<div class="tg-text">اینترنت در ایران آزاد و عادی نشده. بیشتر مسیرهای خارجی یا بسته‌اند یا نیمه‌بازند. فقط بعضی مقاصد و مسیرهای خاص اجازه عبور دارند. همین باعث شده فیلترشکن‌های معمولی خوب کار نکنند.
در این میون بعضی از افرادی که دامنه‌ها و مسیرهای سفیدشده دارند، دسترسی می‌فروشند. نتیجه‌اش هم شده اینترنت نابرابر، رانتی و پر از راه‌حل‌های موقت.
انگاری که درِ ساختمون رو کمی باز گذاشته باشن که هوا بیاد، اما اجازه ندن کسی ازش رد بشه.
برای همینه که گوشی‌تون ممکنه نشون بده که اینترنت دارید، حتی شاید اولش سایت یا اپ مورد نظر رو باز کنه یا بهش واکنش نشون بده، اما در عمل از اینترنت خبری نیست.</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/75801" target="_blank">📅 18:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75800">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h-IOVvtn67jfwDm4XJZ6gji-qMUg2wEPtbWg08SXNu5ad_RvpaiZoRvMTkw-2wvhdfSYRExyH_qzArAoFg244pGu-MW1wFjnImFMMjW5XaXu0mn1spHL36dpROkfJZfj-Q3m6GT9D2NsjGefGOFq5UGucE6nkd_Jz-6idZjeDBCekeBl1wqQZGVPY5UQVKc3gGLfs07TS779uHYkYo0oUB_k2yxkJKd2DWPGzGR446KTJ7xZgal0pd9UNvpzY1ophxpYyDJ9IJiIeCQtKYWLxbVaGwpoCXrfuARmqGHz0lR7V_5TJQ6o_QdCTBJ_nCaIBYvcxxn3dI8TnHHj9tXCcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ان‌بی‌سی به نقل از سه منبع آگاه گزارش داد جنگنده اف-۱۵ای آمریکا که ماه گذشته در ایران سرنگون شد، احتمالا با یک موشک دوش‌پرتاب ساخت چین هدف قرار گرفته است.
به گفته یکی از این منابع و یک مقام آمریکایی آگاه، چین همچنین ممکن است در روزهای نخست درگیری، یک رادار هشداردهنده دوربرد را در اختیار ایران قرار داده باشد که این رادار توانایی شناسایی هواپیماهای رادارگریز را دارد.
ان‌بی‌سی نوشت مقام‌های آمریکایی همچنان در حال بررسی سرنگونی جنگنده اف-۱۵ای هستند و هنوز روشن نیست تجهیزات نظامی احتمالی چه زمانی به تهران تحویل داده شده است.
کاخ سفید به ان‌بی‌سی گفت شی جین‌پینگ به ترامپ اطمینان داده پکن تجهیزات نظامی به ایران نمی‌دهد. سخنگوی سفارت چین در واشینگتن نیز گفت پکن صادرات نظامی را «با احتیاط و مسئولیت‌پذیری» کنترل می‌کند و با «تهمت بی‌اساس» مخالف است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 445K · <a href="https://t.me/VahidOnline/75800" target="_blank">📅 07:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75799">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nlzf3_o_72dqey_OunP8ZYeRNDLH8c4y3GX0gX1egsnameIOoeeIzL_CHF-DR77KZmPV_-R0JGcsHjtgDv85cUsbFvCflU-WY3bJEIOnvfrCqZUYCo1agcyXTx6jRjQaYWiRmZLiRBT0TfEQq-7vtvFi0AYguyTTW5aiFkjzbMOkCpBuFw3Ue443Lv1-x-qF-PpzWvXOD51xi9y9W-ZNa0CvridI-qFUIc7ZsrL3KTQnTG3p979lihkgYSkYBn7KFlvQU9spBvg5dOn2nPRpFlS7vmA4V8qf29PuUco9OAQ6ZlM1ch7KEirGa6c3_Lr5p6gg7GNVdgkUk8Q7Ovc1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">'به جای پول نقد قطر موافقت کرده ۶ میلیارد دلار  اعتبار در اختیار تهران قرار بگیرد تا کالاها و محصولات اساسی را از قطر خریداری کند'
یک منبع آگاه از روند مذاکرات به ایران‌اینترنشنال گفت سفر قالیباف به قطر به شکستی دیپلماتیک منجر شد و با وجود درخواست تهران برای آزادسازی فوری و بی‌قید و شرط ۱۲ میلیارد دلار به صورت نقدی همزمان با امضای یک یادداشت تفاهم اولیه با آمریکا، مقام‌های قطری این درخواست را رد کردند.
به گفته این منبع، مقام‌های قطری تنها با آزادسازی نیمی از این مبلغ تحت محدودیت‌های سخت‌گیرانه موافقت کردند.
بر اساس گفته‌های یک منبع نزدیک به یک مقام قطری حاضر در این گفت‌وگوها، دوحه از انتقال مستقیم یا نقدی این منابع به ایران خودداری کرده است. در عوض، این پول تنها به صورت اعتبار در اختیار تهران قرار می‌گیرد تا کالاها و محصولات اساسی را مستقیما از قطر خریداری کند.
این محدودیت در شرایطی اعمال شده که آمریکا به شدت با اعطای دسترسی مستقیم و بدون محدودیت جمهوری اسلامی به دارایی‌های نقدی مخالفت کرده است.
آمریکا ابراز نگرانی کرده است که تزریق مستقیم پول نقد می‌تواند برای تهران فضای تنفسی اقتصادی حیاتی ایجاد کند و به آن اجازه دهد حقوق‌های معوقه بخش عمومی را پرداخت کرده و در دوره‌ای از تنش شدید منطقه‌ای، تجهیزات نظامی را از کشورهای دیگر تامین کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 432K · <a href="https://t.me/VahidOnline/75799" target="_blank">📅 03:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75798">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/139e7f5cd8.mp4?token=PtrK1XyjpmFyrlML-Pwb9CXGYi2m9OflSun4as7C8QAyAlgxRal8DZvCzXVdnbewl7j8eB9kAN0LB1l92sex4w7GMrIN5yXWMTEJP32x806_a8Au2c907zknbONbJQQ1yWX7X1uN_R_PXBgQslq51QnbLyXYV8fKxgp5SnJMtQF-uO895l_900HMnnvvAOUXBQOPvhox8GuUJwXlhoc3MQqvjz3Z2ryIKnKGZPXcfcL305gGvpcbofeXsvhAZC8hfa6CqNJbX7r7Tr3dbVv2bXkXQztCxa-Fh2WsTnD96fM7SPGBqNg6965jQqgAprzuUH1QPrDm9JW5UYDd1Q-eIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/139e7f5cd8.mp4?token=PtrK1XyjpmFyrlML-Pwb9CXGYi2m9OflSun4as7C8QAyAlgxRal8DZvCzXVdnbewl7j8eB9kAN0LB1l92sex4w7GMrIN5yXWMTEJP32x806_a8Au2c907zknbONbJQQ1yWX7X1uN_R_PXBgQslq51QnbLyXYV8fKxgp5SnJMtQF-uO895l_900HMnnvvAOUXBQOPvhox8GuUJwXlhoc3MQqvjz3Z2ryIKnKGZPXcfcL305gGvpcbofeXsvhAZC8hfa6CqNJbX7r7Tr3dbVv2bXkXQztCxa-Fh2WsTnD96fM7SPGBqNg6965jQqgAprzuUH1QPrDm9JW5UYDd1Q-eIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، بامداد شنبه ۹ خرداد با انتشار تصاویری مدعی شد بقایای یک پهپاد متعلق به آمریکا و اسرائیل که در حوالی قشم هدف قرار گرفته، کشف شده است.
تسنیم بیان کرد این پهپاد با واکنش پدافند هوایی ارتش هدف قرار گرفت و منهدم شد.
پیش از این خبرگزاری مهر به نقل از منابع محلی گزارش داد یک ریزپرنده در حوالی قشم از سوی پدافند هوایی هدف قرار گرفته و منهدم شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 417K · <a href="https://t.me/VahidOnline/75798" target="_blank">📅 02:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75797">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V0oVyaLVcB52Y77GkoIbr1LGvAqH4-lJKvnRfm6sKpa2i6PeJMs1wMUvPk6vNLK52LZPgWsc6hXenb3R8OayhPWe4FHOgahYtNt9UMOcADKrUV8-mN41FDL4kMCYoKrD86pv41E1pXyZSbjZuAEOH9lXn3mhAI2wgwzFWuKnRpvFsF4gXunw2TJ_P1X0AXKuPrg4NyfHuPFwvI-bknj73La2jm8xTaCj9TUaXLMESWZ0rmtrahvshJx7ott1JvrivzSjgnkT1tPuu-Q4tLdmduQqif_p2V9Kswr-grbdIvP8AokPEBTCM_N7_wA0sftu0e81KOiCpNDiCAcx32aUzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نیویورک‌پست، یکی از آخرین موارد اختلاف بر سر راه توافق احتمالی میان واشینگتن و تهران، چگونگی آزادسازی مرحله‌ای دارایی‌های ایران است که در قطر نگهداری می‌شود و برای اهداف بشردوستانه در نظر گرفته شده است.
بر اساس این گزارش، منابع مالی مورد بحث مستقیما در اختیار حکومت ایران قرار نخواهد گرفت، بلکه برای خرید مواد غذایی و تجهیزات پزشکی استفاده می‌شود و سپس این اقلام به ایران ارسال خواهد شد.
نیویورک‌پست به نقل از یک مقام دولت آمریکا نوشت پرداخت تدریجی این منابع به اجرای تعهدات از سوی ایران، از جمله بازگشایی تنگه هرمز و پاکسازی مین‌ها در تنگه هرمز، وابسته خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/75797" target="_blank">📅 01:42 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
