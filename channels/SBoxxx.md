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
<img src="https://cdn4.telesco.pe/file/XqWDPdMND8zw31k3DSZFYPJB5lLdBEmtIMnTdx7g0Q_ThHot61hyKPIwIGz-xxPM481hz8RZqZc9tdmYvAegQUUCNWWMZI9QqwGZQ3zYtzOoSh05GySbPenjsfmzBq4cV1n7JL8X99K72M7kcgS6J74Oe7at9d1GVXlMPDmC_onSbfQJNeSN97fcU4tOCnfmbprBtHRhJ_VINpVWToRJLcLkSrUafEgobU4sHV8gkZki2_VZN0kDtr2-OnsBQozDZgt0dwKjHQ4LkBxFde_ZGo-0pE_JWYdpm7RKPwYpAauDPH6m8eDGqj_daXmSz7IJ1wzjiWKV0IZbf7wztYjfUg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 02:47:14</div>
<hr>

<div class="tg-post" id="msg-17733">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">به عنوان بخشی از بند عدم مداخله در امور داخلی ایران، رئیس‌جمهور ترامپ توافق شفاهی داده که دیگر بیانیه‌های حمایتی از «اعتراض‌کنندگان» ایرانی صادر نکند، دستگاه‌های ارتباطی ارسال نکند، یا به آن‌ها سلاح ندهد</div>
<div class="tg-footer">👁️ 881 · <a href="https://t.me/SBoxxx/17733" target="_blank">📅 01:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17732">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ایالات متحده آمریکا متعهد می‌شود که بلافاصله پس از امضای این تفاهم‌نامه تا زمان لغو تحریم‌ها، وزارت خزانه‌داری ایالات متحده معافیت‌های لازم را برای صادرات نفت خام ایران، محصولات نفتی و مشتقات آن و همه خدمات مرتبط شامل معاملات بانکی، بیمه، حمل‌ونقل و غیره صادر کند.
ایالات متحده آمریکا متعهد می‌شود که وجوه و دارایی‌های مسدود یا محدودشدهٔ جمهوری اسلامی ایران را بلافاصله پس از اجرای این تفاهم‌نامه به طور کامل در اختیار قرار دهد.
ایالات متحده آمریکا و جمهوری اسلامی ایران در طول مذاکرات بر رویه‌های مربوط به آزادسازی این وجوه توافق خواهند کرد. این وجوه، چه در حساب اصلی باقی بمانند یا منتقل شوند، باید به طور کامل قابل استفاده برای پرداخت به هر ذی‌نفع نهایی که بانک مرکزی جمهوری اسلامی ایران تعیین می‌کند، باشند. ایالات متحده آمریکا متعهد می‌شود همه مجوزها و اجازه‌های لازم را صادر کند.
ایالات متحده آمریکا و جمهوری اسلامی ایران توافق دارند که یک سازوکار اجرایی برای نظارت بر اجرای موفق این تفاهم‌نامه و رعایت آیندهٔ توافق نهایی ایجاد شود.
پس از امضای این تفاهم‌نامه و مشروط به آغاز اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ این تفاهم‌نامه و ادامهٔ اجرای این اقدامات، ایالات متحده آمریکا و جمهوری اسلامی ایران مذاکرات مربوط به توافق نهایی را صرفاً دربارهٔ سایر بندها آغاز خواهند کرد.
توافق نهایی توسط قطعنامهٔ الزام‌آور شورای امنیت سازمان ملل متحد تأیید خواهد شد.</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SBoxxx/17732" target="_blank">📅 01:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17731">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">متن توافقنامه به روایت فارین پالیسی:
تفاهم اسلام‌آباد بین ایالات متحده آمریکا و جمهوری اسلامی ایران
ایالات متحده آمریکا و جمهوری اسلامی ایران و متحدان‌شان در جنگ فعلی، با امضای این تفاهم‌نامه، خاتمهٔ فوری و دائمی عملیات نظامی در همه جبهه‌ها، از جمله لبنان، را اعلام می‌کنند و از این لحظه به بعد متعهد می‌شوند که هیچ جنگ یا عملیات نظامی علیه یکدیگر آغاز نکنند، از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند و تمامیت ارضی و حاکمیت لبنان را تضمین نمایند. توافق نهایی، خاتمهٔ دائمی جنگ در همه جبهه‌ها از جمله لبنان و سایر مفاد این بند را تأیید خواهد کرد.
ایالات متحده آمریکا و جمهوری اسلامی ایران متعهد می‌شوند که حاکمیت و تمامیت ارضی یکدیگر را محترم بشمارند و از دخالت در امور داخلی یکدیگر پرهیز کنند.
ایالات متحده آمریکا و جمهوری اسلامی ایران متعهد می‌شوند که ظرف حداکثر ۶۰ روز (قابل تمدید با توافق متقابل) مذاکره کرده و به توافق نهایی دست یابند.
بلافاصله پس از امضای این تفاهم‌نامه، ایالات متحده آمریکا شروع به برداشتن محاصرهٔ دریایی خود و هرگونه اختلال یا مانع علیه جمهوری اسلامی ایران خواهد کرد و محاصرهٔ دریایی را ظرف ۳۰ روز به طور کامل پایان خواهد داد. در این دوره، تردد کشتی‌ها متناسب با تعداد تردد پیش از جنگ که توسط جمهوری اسلامی ایران بازگردانده می‌شود، خواهد بود. ایالات متحده آمریکا همچنین متعهد می‌شود نیروهای خود را ظرف ۳۰ روز پس از توافق نهایی از نزدیکی جمهوری اسلامی ایران خارج کند.
پس از امضای این تفاهم‌نامه، جمهوری اسلامی ایران با به‌کارگیری بهترین تلاش‌های خود، تمهیدات لازم را برای عبور ایمن کشتی‌های تجاری بدون دریافت هیچ هزینه‌ای به مدت ۶۰ روز از خلیج فارس به دریای عمان و بالعکس فراهم خواهد کرد. تردد کشتی‌های تجاری فوراً آغاز می‌شود و با توجه به نیاز به رفع موانع فنی و نظامی و مین‌زدایی توسط جمهوری اسلامی ایران، ظرف ۳۰ روز به طور کامل برقرار خواهد شد. جمهوری اسلامی ایران با سلطان‌نشین عمان گفتگو خواهد کرد تا ادارهٔ آینده و خدمات دریایی در تنگهٔ هرمز را، با مشورت سایر کشورهای ساحلی خلیج فارس و در چارچوب حقوق بین‌الملل و حقوق حاکمیتی کشورهای ساحلی تنگهٔ هرمز، تعیین نماید.
ایالات متحده آمریکا متعهد می‌شود که همراه با شرکای منطقه‌ای، طرح قطعی و مورد توافق متقابل با حداقل ۳۰۰ میلیارد دلار برای بازسازی و توسعهٔ اقتصادی جمهوری اسلامی ایران تهیه کند. سازوکار اجرای این طرح به عنوان بخشی از توافق نهایی ظرف ۶۰ روز نهایی خواهد شد. همه مجوزها، معافیت‌ها و اجازه‌های لازم برای انجام معاملات مالی مرتبط توسط ایالات متحده آمریکا صادر خواهد شد.
ایالات متحده آمریکا متعهد می‌شود که همه انواع تحریم‌ها علیه جمهوری اسلامی ایران شامل قطعنامه‌های شورای امنیت سازمان ملل متحد، قطعنامه‌های هیئت مدیرهٔ آژانس بین‌المللی انرژی اتمی و همه تحریم‌های یک‌جانبهٔ آمریکا (اولیه و ثانویه) را طبق برنامهٔ زمانی مورد توافق، به عنوان بخشی از توافق نهایی لغو کند.
جمهوری اسلامی ایران و ایالات متحده آمریکا اهمیت حیاتی مسئلهٔ لغو تحریم‌های فوق را درک کرده و عزم خود را برای رسیدگی فوری به این موضوعات در مذاکرات به منظور دستیابی به توافق متقابل اعلام می‌دارند.
جمهوری اسلامی ایران مجدداً تأیید می‌کند که سلاح هسته‌ای تولید یا توسعه نخواهد داد.
ایالات متحده آمریکا و جمهوری اسلامی ایران توافق کرده‌اند که وضعیت مواد غنی‌شدهٔ ذخیره‌شده را طبق سازوکاری که به صورت متقابل توافق خواهد شد و مطابق با برنامهٔ زمانی ذکرشده در بند هفت، حل و فصل کنند؛ به‌گونه‌ای که حداقل روش، رقیق‌سازی در محل تحت نظارت آژانس بین‌المللی انرژی اتمی باشد. دو طرف همچنین توافق کرده‌اند که مسئلهٔ غنی‌سازی و سایر موضوعات مورد توافق مرتبط با نیازهای هسته‌ای جمهوری اسلامی ایران را بر اساس چارچوب رضایت‌بخشی که در توافق نهایی مورد توافق قرار می‌گیرد، مورد بحث قرار دهند. توافق نهایی مفاد این بند را تأیید خواهد کرد.
ایالات متحده آمریکا و جمهوری اسلامی ایران اهمیت حیاتی مسائل هسته‌ای فوق را درک کرده و قصد خود را برای رسیدگی فوری به این مسائل در مذاکرات ابراز می‌دارند.
تا زمان دستیابی به توافق نهایی، ایالات متحده آمریکا و جمهوری اسلامی ایران توافق دارند که وضعیت موجود را حفظ کنند. جمهوری اسلامی ایران وضعیت فعلی برنامهٔ هسته‌ای خود را حفظ خواهد کرد و ایالات متحده آمریکا هیچ تحریم جدیدی اعمال نخواهد کرد و نیروهای اضافی در منطقه مستقر نخواهد کرد.</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SBoxxx/17731" target="_blank">📅 01:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17730">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یاد فلیم اخراجی ها افتادم که امین حیایی آن پسره برادر کمند امیرسلیمانی را اسکل کرده بود!  یک تاس به او داده بود میگفت بریز اگر 1 تا 5 آمد بازنده ای و باید پول بدهی و اگر 6 آمد برنده ای. بعد امیرسلیمانی پرسید اگر برنده شدم چی؟!   امین حیایی گفت اگر برنده شدی…</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SBoxxx/17730" target="_blank">📅 01:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17729">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">من دقیقا نمیفهمم روی چه چیزی به جز پایان موقت ۶۰ روزه جنگ توافق شده؟!
لبنان؟! تنگه هرمز؟! موشکی؟! نیابتی؟!</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SBoxxx/17729" target="_blank">📅 01:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17728">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ: ما در مورد موشک‌های بالستیک و نیابتی‌های تروریستی صحبت خواهیم کرد.</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/SBoxxx/17728" target="_blank">📅 01:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17727">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">به نظر شما هم مجموع اعداد از ۱۰۰ درصد بیشتر می‌شود یا من اشتباه میکنم؟!</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SBoxxx/17727" target="_blank">📅 01:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17726">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zek2qv9ZRCeBG-Wv99YNvDBTmhO44UK7-bF-GMQkT3cvkFtgNjfgLCUv1_A6tCLiHkY5rrTTih79OuTTXDffHVo9kaAoGfdbYpb7TXRMmiBsHHzzSLeiPrXmkhUpS-cuP8FhuDYHodefyFWd9P4MB08y7VT03C0tMPUgfpyvpXEdIyhhBBaX44N8vNe8xPvVswgZ6KKIFnlvML6UFeFW-XpE4W3v0KRxAWM8aoK-fVtawSVez6DsMeSa4d-1hpODxiLwuad4xaIltHQhYHmiNjss-PSkh4MxvcTczN4Dubi1iSoBVxZ5SmyvSlMsChoI79r7BoNw0KLltBHpb1MEaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر شما هم مجموع اعداد از ۱۰۰ درصد بیشتر می‌شود یا من اشتباه میکنم؟!</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SBoxxx/17726" target="_blank">📅 01:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17725">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ولی انصافا اگر همه این مواردی که قالیباف می‌گوید در توافقنامه با آمریکا از سوی ترامپ امضا شده باشد امتیازات بزرگی برای جمهوری اسلامی ایران است.  بحدی این امتیازات زیاد است که آدم فکر می‌کند یا جمهوری اسلامی سلاح هسته ای دارد یا چند نسخه از فیلم های مستهجن…</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SBoxxx/17725" target="_blank">📅 01:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17724">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-poll">
<h4>📊 کدام طرف پیروز مذاکرات است؟!</h4>
<ul>
<li>✓ ایران</li>
<li>✓ آمریکا</li>
</ul>
</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/SBoxxx/17724" target="_blank">📅 01:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17723">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رئیس مجلس شورای اسلامی ایران، قالیباف:  تأکید می‌کنم که تنگه هرمز هرگز به وضعیت قبلی خود باز نخواهد گشت.  ایران حق دارد هزینه‌های عبور را تحمیل کند. تفاهم‌نامه پیش‌بینی می‌کند که ایران و عمان در مورد چگونگی توافق آتش‌بس گفتگو کنند.  ما دستورالعمل‌هایی از رهبر…</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/SBoxxx/17723" target="_blank">📅 01:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17722">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خون خواهی رهبر شهید یعنی آزادی قدس!</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/SBoxxx/17722" target="_blank">📅 01:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17721">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">قالیباف:   هر جا دشمن تعهدات خود را انجام ندهد، شمشیر ما آماده است و با منطق قدرت، آمریکایی‌ها را درک خواهیم کرد.  «من دیپلمات نیستم، اما بسیار خوب می‌دانم چگونه به آمریکا بفهمانم که چه کاری را باید انجام دهد.»</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/SBoxxx/17721" target="_blank">📅 01:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17720">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران، اسماعیل بقایی:
🔸️
همین حالا که با شما صحبت می‌کنم، متن یادداشت تفاهم اسلام‌آباد احتمالاً توسط رؤسای جمهور ایران و آمریکا امضا شده است.
🔹️
قرار بر این شده که یادداشت تفاهم به صورت دیجیتال امضا شود؛ وقتی یادداشت تفاهم توسط رؤسای جمهور دو کشور امضا شود، نقض آن هزینه بالاتری خواهد داشت.</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/SBoxxx/17720" target="_blank">📅 01:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17719">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">قالیباف:
هر جا دشمن تعهدات خود را انجام ندهد، شمشیر ما آماده است و با منطق قدرت، آمریکایی‌ها را درک خواهیم کرد.
«من دیپلمات نیستم، اما بسیار خوب می‌دانم چگونه به آمریکا بفهمانم که چه کاری را باید انجام دهد.»</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/SBoxxx/17719" target="_blank">📅 00:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17718">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رئیس مجلس شورای اسلامی ایران، قالیباف:
تأکید می‌کنم که تنگه هرمز هرگز به وضعیت قبلی خود باز نخواهد گشت.
ایران حق دارد هزینه‌های عبور را تحمیل کند. تفاهم‌نامه پیش‌بینی می‌کند که ایران و عمان در مورد چگونگی توافق آتش‌بس گفتگو کنند.
ما دستورالعمل‌هایی از رهبر انقلاب اسلامی داریم و وظیفه ما این است که در این مذاکرات برای اجرای این دستورالعمل‌ها تلاش کنیم.</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SBoxxx/17718" target="_blank">📅 00:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17717">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">قالیباف: ما آمریکا و اسرائیل را از نظر نظامی شکست دادیم، حتی با اینکه آنها از جمله قدرت‌های برتر جهان بودند   «ما اجازه ندادیم آنها به اهدافی که هنگام شروع جنگ اعلام کردند، دست یابند»</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/17717" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17716">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">قالیباف: ما آمریکا و اسرائیل را از نظر نظامی شکست دادیم، حتی با اینکه آنها از جمله قدرت‌های برتر جهان بودند
«ما اجازه ندادیم آنها به اهدافی که هنگام شروع جنگ اعلام کردند، دست یابند»</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/17716" target="_blank">📅 23:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17715">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdAPGwvlmakbnSZ5aDItAZf51YYA5JXOjwJ1NowfL1xGAjk6ipGELrHTkvX19fibj5JFE0h9JgF1-tz8DthyCn8u9-MWQbPiZHPzzuPeq7Ol9by-i3_m7VLAfpWhTiR5WdSnS2SNFq7LENulywGkd0SGVx6Xb04Vn7lczP8rthFFwcwzze6LUZTMohLayTFfE5j35Fc4sMSXxns5E6u2bxWpBf5s7BnFxrbbUrUrMr7OYgQRcAOQdnBYIAraI06IpeM1NA9sfgKHgCAlapaYSiYzaciqnx7gE9r9wUtR9FO7fZuOuZPvqD-RH3jBhukdxd_3T2rhRhVHmsQugqbpaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوزیشنی که 3 دقیقه پیش از انتشار صورتجلسه فومسی پیشنهاد شد.  بشدت هاوکیش موضع گیری کردند و آفتابه را روی کله زرد گرفتند.</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/17715" target="_blank">📅 23:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17714">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ می‌گوید احتمالاً نیروی دریایی ایالات متحده را برای «مدتی» در خلیج عمان نزدیک تنگه هرمز نگه خواهد داشت.</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SBoxxx/17714" target="_blank">📅 22:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17713">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ می‌گوید احتمالاً نیروی دریایی ایالات متحده را برای «مدتی» در خلیج عمان نزدیک تنگه هرمز نگه خواهد داشت.</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SBoxxx/17713" target="_blank">📅 22:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17712">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">— یک مقام کاخ سفید:
«ایران باید فعالیت‌های حزب‌الله را محدود کند و هر حمله‌ای از سوی این گروه با یک پاسخ مستقیم اسرائیلی روبرو خواهد شد».</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SBoxxx/17712" target="_blank">📅 22:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17711">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پوزیشنی که 3 دقیقه پیش از انتشار صورتجلسه فومسی پیشنهاد شد.  بشدت هاوکیش موضع گیری کردند و آفتابه را روی کله زرد گرفتند.</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/17711" target="_blank">📅 21:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17710">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYhaQ4X-4hCg7Q9YyzkgQVVBamBgDS2ZtUIjUU52t9rZLIHrPuoUjQUBilu6sZ_a4NOm0LBOBGC6obqWV8xy_J-CuYOnDsE4RAJh1S1N0DX7sFp0y0Iwetdn_SD4cotqjYfGrw4KOdqYJUb3aovgEwdOsvZqkMjDugqjtLOZdtSiyNJlI6-vyeCl7AK-x7zXCsD1njJKzIGAxdTyFEZ5EI25TmdvqsR6BIZBpPqVYMVbgoTLmbSb81PQEnMtj-5Fb38CLMdj42yuRF5s3caGCZqlhWnFwHulmuhrVNqY7fWYeTPuJqsbsQl61ggh19evN5VfcA0DAcm-8Vzp4N88jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوزیشنی که 3 دقیقه پیش از انتشار صورتجلسه فومسی پیشنهاد شد.
بشدت هاوکیش موضع گیری کردند و آفتابه را روی کله زرد گرفتند.</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/17710" target="_blank">📅 21:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17709">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وزارت امور خارجه ایران:
«لبنان سه بار در یادداشت تفاهم ذکر شده است و جنگ باید در همه جبهه‌ها، به ویژه در لبنان، پایان یابد.»
یادداشت تفاهم بر احترام به حاکمیت لبنان تأکید کرده است و حضور ارتش اسرائیل با این موضوع در تضاد است. اشغال مداوم جنوب لبنان توسط اسرائیل نقض یادداشت تفاهم است و ما اقدامات لازم را انجام خواهیم داد.»</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/17709" target="_blank">📅 21:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17708">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وزارت امور خارجه ایران:
در حال بررسی امضای تفاهم‌نامه از راه دور بین روسای جمهور دو کشور هستیم</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/17708" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17707">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yl3nMgKO0ekL0eSBQ0Ghu_zF34RuwnHzeJJTK8ttiqKn5mqZZoyEPdV76yungJ1qiTUsKqV0mOGkD7h-Q8k2yL3OFaYm-ExYVPto-T490bbaoG6uJgQuksUiEqJosXByIdR8etfGAlZY1nioav1TF9krss_BfirnITCco_RMbJeE5NNgGO4pMamiT0iMxvnc1vlsvb9b2FHTQdqQ-KBp9pdk5oek94jjfgqI-L38loZXS_ZjiKCZmx6LbAygUZqkg1ZjJIlKPF_azamAMX1Uqi_Uy4a9tSvGNq-ypIJb9h1UvodZCTW3c3PkkZtcmVAJ_o9nD72vsCYOGSRMYWhkJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خروج از دور باطل
✍🏻
مهدی خراتیان، مدیر اندیشکده احیای سیاست  ‌تغییر در ژئوپولتیک شیعه، عقیم‌سازی حزب‌الله، تضعیف بازدارندگی شبکه‌ای ایران و درنهایت تمهید برای دور بعدی حملات گسترده به خاک ایران، تصمیم قطعی اسراییل است.   نتانیاهو با محاسبه مهار کامل تهران…</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SBoxxx/17707" target="_blank">📅 21:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17706">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این مدل اجبار قهری برای عقد توافقنامه عملاً یک نوع Duress است و پیمانی که در چنین شرایطی امضاء بشود بعداً میتواند براحتی لغو بشود.</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SBoxxx/17706" target="_blank">📅 21:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17705">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏ترامپ:   دو روز گذشته به شدت دشوار بوده است، و ما به ایرانی‌ها اطلاع داده‌ایم که اگر به توافقی نرسیم، بمباران آن‌ها را برای شب دوم از سر خواهیم گرفت.</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SBoxxx/17705" target="_blank">📅 21:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17704">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ :
«اگر به نتیجه برسد، من اعتبارش را می‌گیرم. اگر به نتیجه نرسد، جی‌دی را مقصر می‌دانم.»
«بهتر است مراقب باشی، جی‌دی!»
«او هواپیمایش را برمی‌گرداند و از اینجا گم می‌شود.»</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/17704" target="_blank">📅 20:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17703">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مقام ارشد آمریکایی درباره متن  رسمی تفاهم‌نامه ایران   -ما شاهد توقف تلاش‌های ایران برای قطع تردد در تنگه هرمز پیش از  امضا هستیم  - ایران اعلام کرده است که ذخایر اورانیوم غنی‌شده خود را نابود خواهد کرد و نحوه انجام این کار  - اگر به توافق نهایی برسیم و اگر…</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SBoxxx/17703" target="_blank">📅 20:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17702">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مقام ارشد آمریکایی درباره متن
رسمی تفاهم‌نامه ایران
-ما شاهد توقف تلاش‌های ایران برای قطع تردد در تنگه هرمز پیش از
امضا هستیم
- ایران اعلام کرده است که ذخایر اورانیوم غنی‌شده خود را نابود خواهد کرد و نحوه انجام این کار
- اگر به توافق نهایی برسیم و اگر ایران رفتار کند، اجازه لغو تحریم‌ها را خواهیم داد
- ایران موافقت می‌کند که حداقل ذخایر اورانیوم غنی‌شده خود را از طریق رقیق‌سازی از بین ببرد
- توالی مراحل توافق‌شده موضوع مهمی در مذاکرات آینده با ایران خواهد بود
- پس از مسئله هسته‌ای، در مورد تأمین مالی نیروهای نیابتی بحث خواهیم کرد
- جلسه این آخر هفته در سوئیس برای بررسی چگونگی پیشرفت مذاکرات با ایران "حیاتی" خواهد بود
- ما کارهایی را برای ایجاد اعتماد انجام خواهیم داد و خواهیم دید که آیا می‌توانیم به توافق برسیم
- نتانیاهو درخواست نسخه‌ای از تفاهم‌نامه نکرده است
- اگر نتوانیم به توافق برسیم، ترامپ از استفاده از ابزارهای خود نمی‌ترسد
- تماس بسیار مداومی با اسرائیل داشته‌ایم
- تفاهم‌نامه امضا شده است اما هر یک از طرفین می‌توانند تا زمان حصول توافق الزام‌آور، از آن خارج بشوند</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SBoxxx/17702" target="_blank">📅 20:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17701">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خب خدا را شکر نشست خبری بی پدر تمام شد….
به همه توهین کرد، از سعودی و ایرانی تا اروپایی و افغان!</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/17701" target="_blank">📅 20:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17700">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ درباره حماس:
آنها وقتی به دنیا می آیند یک مسلسل در دستشان است.</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/17700" target="_blank">📅 20:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17699">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نقش پنهان امارات در جنگ شامل ده‌ها حمله به ایران   به گزارش وال استریت ژورنال، امارات متحده عربی ده‌ها حمله هوایی علیه ایران را از روزهای اولیه جنگ آغاز کرد و تا روز پس از اعلام آتش‌بس ادامه داد،  درگیری عمیق‌تری که تاکنون در کمپین هوایی تحت رهبری ایالات متحده…</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/17699" target="_blank">📅 20:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17698">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ فاش کرد که حملات و بمباران‌های ایالات متحده بیش از ۱ تریلیون دلار به ایران خسارت وارد کرده است.
«بازسازی آنها ۱۵ تا ۲۰ سال طول می‌کشد. بنابراین باید خودشان رفتار کنند. اگر رفتار خوبی نداشته باشند، دوباره ضربه می‌خورند.»
ترامپ همچنین تأیید کرد که ایالات متحده حتی یک دلار هم برای بازسازی به آنها نخواهد داد.</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SBoxxx/17698" target="_blank">📅 20:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17697">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ: ما در مورد موشک‌های بالستیک و نیابتی‌های تروریستی صحبت خواهیم کرد.</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/17697" target="_blank">📅 19:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17696">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ: ما در مورد موشک‌های بالستیک و نیابتی‌های تروریستی صحبت خواهیم کرد.</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/17696" target="_blank">📅 19:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17695">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏
ترامپ:
دو روز گذشته به شدت دشوار بوده است، و ما به ایرانی‌ها اطلاع داده‌ایم که اگر به توافقی نرسیم، بمباران آن‌ها را برای شب دوم از سر خواهیم گرفت.</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/17695" target="_blank">📅 19:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17694">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اینکه با جنگنده باستانی اف-۵ که بزور نسل ۳ است و همان زمانی که نو هم بود عملکرد خوبی نداشت بتوانی به پایگاه نیرومندترین ارتش جهان آسیب بزنی را فقط با هنر خلبان ایرانی می‌توان توجیه کرد.</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/17694" target="_blank">📅 19:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17693">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اگر ایلان ماسک یک تریلیون دلار از دارایی‌هایش را از دست بدهد، همچنان ثروتمندترین فرد جهان خواهد بود.
سبحان الله!</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/17693" target="_blank">📅 19:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17692">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ایالات متحده، ایران و میانجی‌ها در حال بحث درباره برگزاری امضای یادداشت تفاهم هستند که در حال حاضر برای جمعه برنامه‌ریزی شده است، و ممکن است همین چهارشنبه برگزار شود، طبق گفته یک دیپلمات از یکی از کشورهای میانجی و یک منبع دوم آشنا با مذاکرات - Axios|</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/17692" target="_blank">📅 18:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17691">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ایالات متحده، ایران و میانجی‌ها در حال بحث درباره برگزاری امضای یادداشت تفاهم هستند که در حال حاضر برای جمعه برنامه‌ریزی شده است، و ممکن است همین چهارشنبه برگزار شود، طبق گفته یک دیپلمات از یکی از کشورهای میانجی و یک منبع دوم آشنا با مذاکرات - Axios|</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/17691" target="_blank">📅 18:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17690">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aaa93f21f.mp4?token=mnLnu3Tgjsn18JoFVnBUIzwPbCbtypb4DXugeZB5rjwO7tC4gLFiwpP6wxSnUotLFb3iOm00slFnnoFlTrhN31RFDfxNCXMusw-du9LWL9jcFHJ47Mi20Iq3BidZJcbXEGQazQXErcwkGMRrqFN3CiNTgO6xQtZ4vos5xAs5JLQVbjBpTWVVDpdbACtHLNs50qKkAFQHc2fYv3oka8R8e9eB91qhepa7Aa323Wde6k_n7LJ16q4gTxKun573T7rQmfb0_g0VRH4TMZaKfQoCFzGK2Fy8EW1FYm9x9RBIQ42Rd_TNLfMeDXuTqfNvTibh2e5Oa63LgOSrkAsCjkSOMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aaa93f21f.mp4?token=mnLnu3Tgjsn18JoFVnBUIzwPbCbtypb4DXugeZB5rjwO7tC4gLFiwpP6wxSnUotLFb3iOm00slFnnoFlTrhN31RFDfxNCXMusw-du9LWL9jcFHJ47Mi20Iq3BidZJcbXEGQazQXErcwkGMRrqFN3CiNTgO6xQtZ4vos5xAs5JLQVbjBpTWVVDpdbACtHLNs50qKkAFQHc2fYv3oka8R8e9eB91qhepa7Aa323Wde6k_n7LJ16q4gTxKun573T7rQmfb0_g0VRH4TMZaKfQoCFzGK2Fy8EW1FYm9x9RBIQ42Rd_TNLfMeDXuTqfNvTibh2e5Oa63LgOSrkAsCjkSOMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">—  ترامپ درباره مودی نخست وزیر هند:  «او زیباترین مرد است. او مثل فرشته است. اما در واقع، او یک قاتل است.»</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/17690" target="_blank">📅 18:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17689">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUtDQrPDyOeI6gHX5x-wP8pYdug3TrlsFxjhx9sVPvWgP1QqFv__jV8yDL_xrSDBd0-s6dop88ek4YbfRU0TE1TDl0aJ8rPOzahBgNeUS6D-Bz7IafwMYCGcoOYFSfX7GN1fAWQB9QIRkRw5FhzK2jMpUVcO2BZpQ26CpHAyH-THN6xZxR7G26DYtsYpAd_Tb_pWkU8HZiy1pp_1q74cJmjJlaUGZknvc9ZAdKtlqM2XS0t_zmZ_5LHhDYshdpRwLbZZUWyTiMpjNj7QG6_jnbI6LSyUp1gTBqrEzJ7NVMMyrjifI94tNMMDxzC4TLDcJf_5KIDNXDQqFEJvX4ErjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">—  ترامپ درباره مودی نخست وزیر هند:  «او زیباترین مرد است. او مثل فرشته است. اما در واقع، او یک قاتل است.»</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/17689" target="_blank">📅 18:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17688">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">—  ترامپ درباره مودی نخست وزیر هند:
«او زیباترین مرد است. او مثل فرشته است. اما در واقع، او یک قاتل است.»</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/17688" target="_blank">📅 18:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17687">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">موجودی نفت به کمترین سطح بحرانی در بزرگترین مرکز ذخیره‌سازی ایالات متحده سقوط کرد.</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/17687" target="_blank">📅 18:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17686">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-gU1Uh9b-hhZBRHH0cXaUkS7QBXJ6ODHkU1u9pjlDYuWHaGe-Sdbu5pyugMYx8o5Sm9-v1JkpBwncrvsgIVfNJS4B0q1w9qhjAn2uLZaMSmN_P-5JL3qqGTraW_Tp5re76QKrafD5eFc8YTxcoJG5OX32xan5j2_JqmgWuN1k8jzIyYqMjbAGSihImNx1k-l5Lo3TcMDaypsJuh9ZzeOI91bs_HCMuaJBI9tujnAZxucezMoVEWCVxULewpFRhnYg9XwTlWjWxBXZ29_gSI65gErvcpOyGy2sFaxfJzmu0dlNRYeQrHrQdAmDmtPjK9OJmdgnoTjG3DalN9VTlmhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفوگرافی موسسه مطالعات جنگ از ابهامات و اختلاف روایات بندهای توافقنامه ایران و آمریکا</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/17686" target="_blank">📅 17:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17685">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔹
سفر هیات ایرانی به ژنو لغو شد</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/17685" target="_blank">📅 17:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17684">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">توصیه ام به شیربچه های دیپلماتمان این است که اصلا حضوری به ژنو نروند و به همان امضای الکترونیک بسنده کنند!  واقعا یک خودکار یا خودنویس حتی اگر از طلا هم باشد به احتمال لواط زوری با این ماموت کله زرد نمی ارزد  سبحان الله!</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/17684" target="_blank">📅 17:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17683">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ونس ترنس:   طرف پاکستانی از ما خواست که متن کامل یادداشت تفاهم را برای مدتی منتشر نکنیم.</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/17683" target="_blank">📅 16:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17682">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ونس ترنس:
طرف پاکستانی از ما خواست که متن کامل یادداشت تفاهم را برای مدتی منتشر نکنیم.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/17682" target="_blank">📅 16:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17681">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تشدید حملات اسراییل در جنوب لبنان و تصرف شهرک الحدثه!</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/17681" target="_blank">📅 16:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17680">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">عراقچی گل!</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/17680" target="_blank">📅 16:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17679">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حاج عباس حتی زبان بدنش هم کلاس درس است!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/17679" target="_blank">📅 16:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17678">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">توصیه ام به شیربچه های دیپلماتمان این است که اصلا حضوری به ژنو نروند و به همان امضای الکترونیک بسنده کنند!  واقعا یک خودکار یا خودنویس حتی اگر از طلا هم باشد به احتمال لواط زوری با این ماموت کله زرد نمی ارزد  سبحان الله!</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/17678" target="_blank">📅 16:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17677">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ می‌گوید در هتلی با رئیس‌جمهور مصر ملاقات کرده و آنها «عمیقا عاشق هم شده‌اند»</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17677" target="_blank">📅 16:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17676">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ می‌گوید در هتلی با رئیس‌جمهور مصر ملاقات کرده و آنها «عمیقا عاشق هم شده‌اند»</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/17676" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17675">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چرا قطر بقای خود را مدیون جمهوری اسلامی است؟  ترامپ در سفر اخیرش گفته بود:  ایران به دلیل وجود امیر قطر، خیلی خوش شانس است. امیر قطر در حال مبارزه برای دست یابی به توافق هسته ای با ایران و عدم حمله به این کشور است. ایران خوش شانس است که امیری در قطر دارد که…</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/17675" target="_blank">📅 15:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17674">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q59etAhqSndXd2AML29kxR-2x1DD923b_dWnSx29zTtuorxHHOpXOejX4jGthcisQJYw2w_kybBbacWMucDvqE8gf7KrM_Leqwi5u9a391Nz4KjBETtSHHRon-GsEkfNbTaSDjEtQlY-HonQo3NQIJx_gCREMLEnTHmFuqeCGsg8QF2CwHRP37Ug4QCkma0vSeLJ3dFqAUuyasn_nZuwBdEkiCV8H4VuZ4gkwg6kLzHM1BcBzTfvUVH33Lkvqv9qw4SvBRWheWswOa5RdBTH-C_R6laaK_Eyfeb_hO6yei4yQfBUt3hvL_lSERr5JcO9XbUuMujx5zyEAahcalKnBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی کانالهای ایرانی خبر داده اند که قطری ها برای راضی کردن ویتکاف و کوشنر جهت فشار بر ترامپ برای پرهیز از جنگ دوباره و امضای توافق، یک هتل نیمه کاره 5-ستاره در دوحه را به این دو نفر هدیه داده اند.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17674" target="_blank">📅 15:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17673">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ:   ایالات متحده صندوقی برای سرمایه‌گذاری در ایران ندارد  تفاهم‌نامه ایران نهایی نیست  اگر آنچه می‌بینم را پسندیدم، دوباره حمله خواهیم کرد</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/17673" target="_blank">📅 15:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17672">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ:
ایالات متحده صندوقی برای سرمایه‌گذاری در ایران ندارد
تفاهم‌نامه ایران نهایی نیست
اگر آنچه می‌بینم را پسندیدم، دوباره حمله خواهیم کرد</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/17672" target="_blank">📅 14:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17671">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔵
پاول دوروف ؛ مالک تلگرام
:
دولت بریتانیا می‌خواهد استفاده از شبکه‌های اجتماعی را برای کودکان زیر ۱۶ سال ممنوع کند.
اما ممنوع کردن شبکه‌های اجتماعی برای کودکان فقط آن‌ها را در معرض خطر بیشتری قرار می‌دهد.
آن‌ها مجبور خواهند شد از VPN استفاده کنند و به محتوای غیرقانونی بسیار بدتری دسترسی پیدا کنند.
ما قبلاً این را دیده‌ایم.
وقتی دولت روسیه تلگرام را ممنوع کرد، ۹۵٪ نوجوانان روسی همچنان از آن استفاده کردند. آن‌ها فقط به VPN منتقل شدند. همین‌طور در ایران</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/17671" target="_blank">📅 13:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17670">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ylhjw-puASJZEGdHlbng6QHxyr423DKTjI84TWSm1NteFpRQJrdEHXBmzlI6DIPgahfT2pj_0zwQNwm4am82E4AglxbwiI9qRjsHguB8mXnLSsLT5Nj_vOFrEr9qznBzUU6WunKPrOQFP4iTHfw3CNOhhR7IXUL5zMkzyf7i_u4QDXQEBwy07MsGzhJH5rqXBeRohve5GxH5z41McZ8Aa1DDNccVDndTLzbXRCCFOYQb6guRHiRNumznZkQOW2kZTCMVJm2Ob8CwtTvwweg9QDNv76rNbFUrhr74CgMo9REm2GAbHB2UPrGP4nYewzuqApOHcdU-meMuhzCfyThSkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای باری نظامی امارات در پایگاه نواتیم اسرائیل فرود آمد
در ۱۵ ژوئن ۲۰۲۶، یک هواپیمای باری ایلوشین Il-76TD متعلق به امارات از ابوظبی به پایگاه هوایی نواتیم اسرائیل پرواز کرد. این پرواز از حریم هوایی عربستان عبور کرد.
این رویداد، نشانه‌ای از همکاری نظامی رو به گسترش و عمیق‌تر امارات و اسرائیل در برابر تهدید موشکی و پهپادی ایران است. پایگاه نواتیم یکی از مراکز کلیدی نیروی هوایی اسرائیل است.
گزارش‌ها همچنین حاکی از استقرار سیستم
گنبد آهنین
اسرائیل و پرسنل نظامی آن در امارات پس از حملات ایران است. این پرواز احتمالاً برای انتقال تجهیزات، مهمات یا لوازم پشتیبانی دفاع موشکی انجام شده.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17670" target="_blank">📅 12:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17669">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نمودارهای برگرفته از سایت شرطبندی Polymarket نشان‌دهنده سقوط چشمگیر شانس‌های انتخاباتی بنیامین نتانیاهو در ماه‌های اخیر است.   خط زرد (احتمال نتانیاهو به عنوان نخست‌وزیر بعدی) از حدود ۵۰-۶۰٪ در فوریه با نوسانات اولیه به اوج می‌رسد، اما از اواخر مارس با شروع…</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/17669" target="_blank">📅 12:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17668">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_GCQA5lu4o12K4XfaIelElRgWpFrhVHymmSUIXcnu1mFNDglTV44OuT6oKr8-8uDIptFeDXrJ23EWck_x8foelN_fz9eu__MInfveQ6UyY7kbYjNIN-ZkaBl4mrk6OJUwvpUkCF8fX3zf06OaaVTueMIZ9OQpBXNBqym4xeCcwdaS8WSsVcyhLDPNsooJtzCJz8IN8A4lC4ACZoQ2q0tI3wFkO2MFqyt8jsU8UPVdeTEhquOgGD1eu0s-u3f2aLeQC711lm4rbMwDM4R4wbhQmZp0f9oORDIjtUePzUJ7grKd8rwtpBOHYlctnYIHcBldG8cmbSA_xFRf2lBgCtzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمودارهای برگرفته از سایت شرطبندی Polymarket نشان‌دهنده سقوط چشمگیر شانس‌های انتخاباتی بنیامین نتانیاهو در ماه‌های اخیر است.
خط زرد (احتمال نتانیاهو به عنوان نخست‌وزیر بعدی) از حدود ۵۰-۶۰٪ در فوریه با نوسانات اولیه به اوج می‌رسد، اما از اواخر مارس با شروع یا تشدید درگیری‌های مرتبط با جنگ ایران، به شدت افت کرده و به حدود ۲۵-۳۰٪ در ژوئن رسیده است.
این سقوط با منطقه زمانی خاکستری “جنگ ایران” همخوانی دارد که از اواخر فوریه تا ژوئن را پوشش می‌دهد.
در مقابل، خط آبی نفتالی بنت (حدود ۲۰-۴۰٪) نوسان داشته اما اخیراً پایدارتر است. خط سبز گادی ایزنکوت از نزدیک صفر شروع کرده، به تدریج افزایش یافته و در ژوئن به حدود ۳۵٪ رسیده و حتی از نتانیاهو پیشی گرفته است.
این روند نشان‌دهنده نارضایتی عمومی اسرائیلی‌ها از نتیجه جنگ ایران است؛ افکار عمومی معتقدند اهداف اصلی (مانند نابودی کامل برنامه هسته‌ای و نیابتی هایش) محقق نشده و این امر به ضرر نتانیاهو تمام شده است.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17668" target="_blank">📅 11:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17667">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بدون تصویب مجلس این توافق اعتبار ندارد  حسینعلی حاجی دلیگانی، نماینده مجلس:  طبق قانون اساسی هر توافق و عهدنامه بین‌المللی باید به تصویب مجلس برسد و بعد در شورای نگهبان تایید شود وگرنه وجه قانونی ندارد و باطل است.</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/17667" target="_blank">📅 11:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17666">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بدون تصویب مجلس این توافق اعتبار ندارد
حسینعلی حاجی دلیگانی، نماینده مجلس:
طبق قانون اساسی هر توافق و عهدنامه بین‌المللی باید به تصویب مجلس برسد و بعد در شورای نگهبان تایید شود وگرنه وجه قانونی ندارد و باطل است.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/17666" target="_blank">📅 11:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17665">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fvn6PSFeAIfGtDrMvuR4F9ye5_54iE8H_sRn6Xd-Vyl9xMetcgg-_b-CBUAJ_iMXVd-3dy89VMccvhP2jq4hgQbdZVa6mSDkqcX7vPS4orQNHlvID83q0SlwHPUlYCZ_h7jHicLxITueJolRRio1FCcVICJ7_AkFtnL5gi53vcKGU2xVsfiEVaxzKPHAkksCefFnGW9Tc0_L7yg2lHr55lQO7ClpgTR_D2tRhcfffk-Fp5mCQXedC5j0J3WCSpQBDrYPCwl3wFtFiiInhea4HSEC-LiiL0UNynokRDi1oraI3GBSh53E_YKNrSAV921N2jLhQqGE7cAxh7d-y8oX4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناتو در حال استقرار سامانه دفاع موشکی SAMP-T ایتالیایی در قونیه ترکیه
سامانه SAMP-T که به طور مشترک توسط فرانسه و ایتالیا توسعه یافته است، یک سامانه موشکی زمین به هوای متحرک است که قادر به رهگیری هواپیماهای جنگنده، پهپادها، موشک‌های کروز و برخی موشک‌های بالستیک است.
این استقرار در میان تنش‌های فزاینده منطقه‌ای پس از آغاز جنگ در خاورمیانه رخ می‌دهد، که نیروهای ناتو در ترکیه موشک‌های بالستیک ایرانی را در ۴ مورد جداگانه از فوریه رهگیری کرده‌اند.
یک آتشبار موشکی پاتریوت  اضافی نیز در پایگاه هوایی اینجیرلیک در جنوب ترکیه مستقر شده است.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17665" target="_blank">📅 10:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17664">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اسموتریچ:
«تا جمعه از جنوب لبنان عقب‌نشینی نخواهیم کرد - و بعد از جمعه هم عقب نشینی نخواهیم کرد.»</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17664" target="_blank">📅 10:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17663">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ونس ۱۴۰۵ = مرفاوی ۱۳۸۵
سبحان الله!</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17663" target="_blank">📅 10:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17662">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">طبق گزارش NBS؛ از روز یکشنبه که تفاهم‌نامه به‌صورت دیجیتال امضا شده، هر شب ایران چندین پهپاد پرتاب می‌کند.
یک مقام آمریکایی گفته این پهپادها توسط سپاه پاسداران پرتاب می‌شوند و نیروهای آمریکایی آن‌ها را قبل از اینکه تهدیدی برای کشتیرانی تجاری، ناوهای نظامی یا نیروهای منطقه ایجاد کنند، رهگیری و ساقط کرده‌اند.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/17662" target="_blank">📅 01:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17661">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">جی دی ونس:   تفاهم‌نامه ایران، شامل لبنان هم می‌شود</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/17661" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17660">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سفیر آمریکا در اسرائیل، مایک هاکابی، مجدداً تأکید می‌کند که حزب‌الله در توافق بین آمریکا و ایران گنجانده نشده است. این در حالی که تهران همچنان اصرار دارد که بر اساس شرایط این توافق، اسرائیل باید عملیات خود در لبنان را متوقف کند.  در پاسخ به ادعای حزب‌الله…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/17660" target="_blank">📅 01:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17659">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">برخی کانالهای ایرانی خبر داده اند که قطری ها برای راضی کردن ویتکاف و کوشنر جهت فشار بر ترامپ برای پرهیز از جنگ دوباره و امضای توافق، یک هتل نیمه کاره 5-ستاره در دوحه را به این دو نفر هدیه داده اند.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/17659" target="_blank">📅 00:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17658">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تیم فرانسه به روزی افتاده که بلوندشان شده امباپه!
سبحان الله!</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/17658" target="_blank">📅 00:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17657">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گزارش حملات پهپادی سپاه پاسداران به اربیل عراق   سبحان الله !</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/17657" target="_blank">📅 22:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17656">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حالا شما گرامیان گفته اید میزنیم اما به نظر من که اسرائیل را نمیزنیم.  دو مورد که مدنظر من است:  — همون همیشگی (حمله به اربیل)  و|یا  — سپردن کار به بچه های نقطه زن یمن  در صورت تحقق مورد دوم، منتظر اصابت موشک های بالستیک اصحاب یمین به در و دیوار خواهرمیانه…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/17656" target="_blank">📅 22:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17655">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">— سفیر ایالات متحده در اسرائیل مایک هاکابی:
«بدون اسرائیل، آمریکایی وجود نخواهد داشت.
وجود ما مدیون چیزی است که در این سرزمین رخ داد».</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/17655" target="_blank">📅 22:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17654">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ستاد کل نیروهای مسلح ایران اعلام کرد در صورتی که اسرائیل حملات خود به جنوب لبنان را متوقف نکند، باید منتظر پاسخ سختی از سوی نیروهای مسلح ایران باشد</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/17654" target="_blank">📅 22:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17653">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">این مسئله لبنان حل نشود کل توافق روی هوا خواهدرفت. مگر اینکه طبق حدس من اساساً از همان آوریل حزب الله را معامله کرده باشند.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/17653" target="_blank">📅 22:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17652">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKWRvsh66p3Z-Lg1CQ_9Xj1z9VaQup6ido7_ZPLx1E3UI-KGqnttXoVziUwhMZ2xpLRGWDimuSKG0Rmn29gBUfRXaX6bxrNkoijQzC_HCVG7Gd1Z_tYlppcgUEN1cECZqE_EosZTZh_G5buolSjap2VCiF_214V9VxBLCKxMYxGGKrfK-EE4qHxaoYYEhnyFJOS4r_3HwKZ4SUQHusqVamcCLau9W9mz2uS7hDMZHfsjgXfnR-IGdyD66TjxitCu5QekXBP1Z96cwLp0QLmaaq7JhRANiybc3grDfq3a97BoqwmaVKdzMWfQVoXT2RN38fyD9Yw1liAVR-Sd7_KTGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نبیه بری و قالیباف در یک تماس تلفنی:   اسرائیل باید ملزم به توقف تخریب روستاهای لبنان و عقب‌نشینی از سرزمین‌های اشغالی شود.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/17652" target="_blank">📅 20:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17651">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وال استریت ژورنال: ایالات متحده بلافاصله پس از امضای توافقنامه در این هفته تحریم‌های فروش نفت و سوخت ایران را لغو خواهد کرد</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17651" target="_blank">📅 20:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17650">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNBpcNGCi_ao6DGHkvYFdHWsYbM_N9WW7EWhdedxP0EmUr9Sc8XSdZZDZDKHpFl_JVuUEsOPupAV4_iS7jI0MoLuTkyFtohaaD6wInTonHURxZPl8aS32V5BiqxAtTDa4aMEObdJ8YsgOFmWoas8v0SOs_BeP9Z1ePGHdaNilzL34mdkKnsGpGdl7vtjuSmPcIEH85QC3-apWckhsH6x6gwYsOo2sIDrzlIZzbi--6TX8uOK7AdpRnKM9IioNk9y6gWVmw-muNTKBQITKZEELmzab1h3kSHQyEnFoanJ_U4arJKPFJOv44S_nUKRRxFN5cuw4-qrKqSUlYp9Dkq-3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  در محدوده مشخص شده می شود به دنبال موقعیتهای خرید باشیم.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17650" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17649">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8l7s3jqbhhCbit7Ed5pHe8V1w6NfTa5csIq1L74yj0Uzt40u3rkaJ_rl1yifg8W3NR7DG5ScxLFRVBwzh272xNFQTh2HcE3bUJxRB6y-d0U0nodFASYULjuZxHWvkXzLCKOrQcPvyRPE3F4TT6kaJHqP62h-y7wSBCPBDxYYOUvtGz3K3PFjnmU7-pr4EATNbTJky2c94uxPhc1aPm9WbLectxLzcpYNX3emn5thzB-450-u5m9bZbqjria0SKiirKKzYOsUeYredurfP4Jhsdaf4r02zw0IKtWX53JfkmirNKIJoEljEVFEi-_LxmRAxZZ6nkHqYdofpbBmq19aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL
— H2
در محدوده مشخص شده می شود به دنبال موقعیتهای خرید باشیم.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17649" target="_blank">📅 20:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17648">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJlkA00iSIriN2yTKvi7CZOVzYOO5-K6MJD3LChOM_Npc9-3ldsvP8-z2TidMukkR8eP4r6UTzAQXH4rgdr9DAVVaUAleC01m0gjefCkegmaSQlv0eMwgyy4UiS09JvrrNbbOaLif4w5tSve9EjH_PHt_jPLUTE3FQZYPVo7-Zu-VTITgMZrTMc4Cm9LPjxoWF2YqzAv3XeHOPLf0o-kKHJ85ObE4GGvRSciviiwCStKVnvI_jes6MgR0A-hD0tyEkaNojD4i4k27F2Z_sqTAru79a8_juPsVi5vbBwRgeX1UXsUmelOd0T1CEraxBry20sp-EkVooGUQTvm_W3voQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت جانفدایان</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17648" target="_blank">📅 20:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17647">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">برآوردهای اطلاعاتی آمریکا: ایران از این پس هر زمان که بخواهد قادر خواهد بود تنگه هرمز را مسدود کند. «این سلاحی قوی‌تر از هسته‌ای است» (سی‌ان‌ان)</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17647" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17646">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">العربیه به نقل از منبع آگاه دربارهٔ سند توافق:  سند توافق بر پایان فوری و دائمی جنگ در تمامی جبهه‌ها تأکید دارد.
🔸
سند توافق بر پایان فوری و دائمی جنگ در لبنان تأکید دارد.
🔸
ایالات متحده و ایران بر اساس این توافق متعهد می‌شوند که هیچ‌گونه «اقدام خصمانه‌ای» علیه یکدیگر انجام ندهند.
🔸
ایالات متحده و ایران طبق این توافق از دخالت در امور داخلی یکدیگر خودداری خواهند کرد.
🔸
سند تفاهم میان ایران و آمریکا تأیید می‌کند که مهلت مذاکرات با موافقت دو طرف قابل تمدید است.
🔸
آمریکا بر اساس سند تفاهم، بلافاصله پس از امضای توافق، محاصره دریایی ایران را لغو خواهد کرد.
🔸
آمریکا طبق این تفاهم متعهد می‌شود که ظرف ۳۰ روز پس از توافق نهایی، نیروهای خود را از مناطق پیرامون ایران خارج کند
🔸
ایران بر اساس این تفاهم، اقداماتی را برای تضمین ازسرگیری تردد کشتی‌های تجاری در تنگه هرمز انجام خواهد داد.
🔸
ایران بر اساس این توافق موظف است مین‌های دریایی موجود در تنگه هرمز را پاکسازی و برچیند.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17646" target="_blank">📅 20:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17645">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">چین می‌گوید مرحله بعدی مذاکرات آمریکا و ایران «سخت‌تر» خواهد بود
وزیرخارجه چین روز سه‌شنبه به همتای پاکستانی خود گفت که مرحله پیش‌رو از مذاکرات بین آمریکا و ایران انتظار می‌رود «سخت‌تر» باشد.
وزیر امور خارجه چین، وانگ یی در تماس تلفنی با اسحاق دار از پاکستان پیش از امضای برنامه‌ریزی شده یادداشت تفاهم آمریکا و ایران در روز جمعه، ، گفت که «قابل پیش‌بینی است که، در مقایسه با مرحله اول، مرحله دوم مذاکرات سخت‌تر خواهد بود.»
طبق بیانیه وزارت امور خارجه چین، وانگ همچنین گفت که شورای امنیت سازمان ملل «باید نقش بیشتری» در حمایت از مذاکرات ایفا کند.
«اجماع کنونی فاصله زیادی با مقصد نهایی دارد، بلکه یک نقطه شروع جدید است».
«دستیابی به صلح پایدار در خاورمیانه و منطقه خلیج فارس هنوز نیازمند تلاش‌های بی‌وقفه همه طرف‌ها است»، وانگ افزود و گفت که چین آماده همکاری با پاکستان در پیشبرد ابتکارات صلح است.
(خبرگزاری فرانسه)</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17645" target="_blank">📅 18:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17644">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F77UYLFuMAMYRti7o6DOmnm3Fc6CltwZxx-drQY8tqkTy6-Hs4PeW6t4yuQx-XJ6LShYRU20IFIvvbrxhAYwAa6s3b8x5N_IPcDiTMcDWIP_LtkraF5zZWp3lCrLOImP_lx4QmejT6lQ30dC7YDL5nBEmw4gfndUbtgGHYesSstius6DYJssBaf9w-EdFtXmVwbASy4-cKKe8ZrOUhMeGhvvcJovtip5tQ2zYWxZzhGRzlkEXX007tJ0y6p38jy4rpd7CFZ1S3JqVeaDgxz6dZpFUsl12mQu4D74s-k2WwtlD60NcWFAzH5Wn509zDFP1tmv-trgJNWfj4ZhFbMpeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نشست فدرال رزرو: چرا نخستین حضور کوین وارش از خودِ تصمیم نرخ بهره مهم‌تر است؟
نشست ژوئن فدرال رزرو بیش از آنکه به تصمیم نرخ بهره مربوط باشد، بر نخستین حضور کوین وارش به‌عنوان رئیس جدید متمرکز است؛ فردی که می‌تواند رویکردی متفاوت در سیاست‌گذاری و ارتباطات بانک مرکزی آمریکا ایجاد کند.
سرمایه‌گذاران به دنبال نشانه‌هایی از مسیر آینده سیاست پولی هستند و انتظار دارند اظهارات وارش درباره تورم، نرخ بهره و استقلال فدرال رزرو تأثیر بیشتری از خودِ تصمیم نرخ بهره بر بازارها داشته باشد.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/17644" target="_blank">📅 18:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17643">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ادامه ترورهای اسراییل ضد حزب الله در جنوب لبنان</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17643" target="_blank">📅 18:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17642">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سوگمندانه جامعه سرمایه گذاری جهانی خیلی به تهدیدات ما اهمیت نداد و فقط شرکت SpaceX ماسک ملعون پس از عرضه اولیه دیروز به ارزش بازار 2.2 هزار میلیارد دلار رسید!  دقت کنید 2200 میلیارد دلار!  ثروت خود ماسک نیز از 1000 میلیارد دلار فراتر رفت.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17642" target="_blank">📅 17:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17641">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ونس می‌گوید بازرسان هسته‌ای «قطعاً» بر اساس توافق ایالات متحده به ایران بازخواهند گشت
ونس در مصاحبه‌ای روز دوشنبه با شبکه خبری ان‌بی‌سی اعلام کرد که بازرسان هسته‌ای «قطعاً» اجازه بازگشت به ایران را در چارچوب توافقی با ایالات متحده خواهند داشت.
«در واقع، یکی از بخش‌های اصلی این توافق این است که (آژانس بین‌المللی انرژی اتمی) و ایالات متحده به ایران کمک خواهند کرد تا ذخایر غنی‌سازی شده را نابود کنند و این موضوع به‌طور بسیار شفاف در یادداشت تفاهم قبلاً توافق شده بین واشنگتن و تهران ذکر شده است»،
ونس همچنین اذعان کرد که یادداشت تفاهم مقدماتی مسائل دشوار، به‌ویژه برنامه هسته‌ای ایران را فعلاً حل‌نشده باقی می‌گذارد.
«یادداشت تفاهم حدود یک و نیم صفحه است، بنابراین سند بسیار کلی است»، ونس به سی‌ان‌ان گفت.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17641" target="_blank">📅 17:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17640">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ: کلمه به کلمه متن توافق را برایتان می‌خوانم
من نه تنها آن را منتشر خواهم کرد. احتمالاً یک کنفرانس مطبوعاتی خواهم داشت و کلمه به کلمه آن را برای شما خواهم خواند تا مطبوعات آن را به طور دقیق پوشش دهند زیرا این یک سند بسیار مهم است.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17640" target="_blank">📅 17:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17639">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وقتی میگوییم ابهام یعنی همین که الان ایران می‌گوید نه تنها باید آتش بس در لبنان برقرار بشود بلکه اسراییل باید از سرزمین های متصرفه عقب نشینی هم بکند اما در سوی مقابل اسراییل دنبال پیشروی بیشتر در خاک لبنان است و ترامپ هم می‌گوید جنگ در لبنان ربطی به توافق با ایران ندارد!</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17639" target="_blank">📅 15:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17638">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ: اگر اسرائیل به لبنان حمله کند، باز هم توافق می‌تواند دوام بیاورد</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17638" target="_blank">📅 14:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17637">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">— رئیس‌جمهور آمریکا ترامپ:   قطر و ایران مرز زمینی مشترک دارند و می‌توان از یکی به دیگری پیاده رفت.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/17637" target="_blank">📅 13:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17636">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">— رئیس‌جمهور آمریکا ترامپ:
قطر و ایران مرز زمینی مشترک دارند و می‌توان از یکی به دیگری پیاده رفت.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17636" target="_blank">📅 13:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17635">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffJQFenIZP-pM4GJEn-XX_IK8JLSVLj1k3iGOv9lwyZp0oN5b0ZTIxbsph36I4fKaR5mu9y5FiftseeiPB2Mmr0AyAOGb3wNwdTS_DZg36iPpLDG3bITOrIMOX3SuHTxMtbf0ergxjoVDcZST9c9RrCVwOSmnwCL8yV4Yvg3j3gStuC-CsaW2A-phQNAfyOJjP2-Ea7gJWaeLHLu3E3JufSijPhYFs2mHxlDEBR95sojtSKOwvrxBExJzxuQz4UrgkG4VP3KdIZy0KLzL-SyBE0PebAz4npb48aZefaE_hkuXMPbSSPWpwdVWWptPgwFKs4ibjMvg83TPfdEGTdjKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سطح اطمینان کاربران پیام‌رسان های داخلی از پایداری اتصال:</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17635" target="_blank">📅 13:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17634">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گویا گروه‌های مسلح تجزیه طلب کردی با حزب الله طاق زده شده اند.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17634" target="_blank">📅 13:32 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
