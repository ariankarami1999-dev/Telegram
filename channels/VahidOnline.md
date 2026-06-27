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
<img src="https://cdn1.telesco.pe/file/sNQ-Aljp-gfT6SLFp9FYPIp1aprCtnhv1swJT_QWv1Xu99NJjh5OeHIdB7mOnnWHxsVz40p6B01M7tObXohVemefqCfQLVlqlVGNl_bhwogmoh_EzOyhMIRkZXAIkPLkO0cp4V0X6C4fcMktUDRABseAy1a65WLk4ydJqKKQJ4i8cMQUQ7JKBr0piM249hO8BhlgdhdhLBMXd_PzMMt8Tqkr_mrxqxpYFY6dAfMEwcHv7iBbh5sgqWaDeQXgLJAgmQJXU5ltAz1Im12Xdhle1-S8B9-9EwCKXTng6YKB_4V25xG3mQs8IA7T4b-InFixOIsPu06z6cFS-Eh2gcSlew.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.35M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 19:16:34</div>
<hr>

<div class="tg-post" id="msg-76710">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUxJ5NSONGkVCfCwvJ3XEndA_hOMqc4ZJd_u2cITANvfksKO5rtShdhR3m1QvxMHEZDw3VrpcYfgE_RktPjeQzKrMHtiqei_45CkcAEAl8apTb8u9Gu_UlzQaiKiDhLemv6B2m-yFrdVGIlisbBR39ApBHt_tMFZfTLjqxnkFGUJ-Qy0xUMZj8UiI88Qta_iDVdRr7HdeKs42Za2DPBO4NR5-dhGblDHCi224KYm4MXee2xAV4Qks-ds2SZ-BNF5AJ8AAbEhFMR6bCLp67mW7qJemDHtn5dzl-VMOapjl7Fm6qNf_lg0p_jpOmQzUZQrF7WmGNJWrBJFryItQin0Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رسانه‌های ایران ارائه خدمات بعضی از بانک‌ها از صبح امروز (شنبه، ۶ تیر ۱۴۰۵) دوباره مختل شده است؛ خبرگزاری ایسنا به بانک‌های ملی و صادرات در این زمینه اشاره کرده است.
شرکت خدمات انفورماتیک این اختلال را مرتبط با حمله سایبری دانسته است. در اطلاعیه این شرکت آمده است:
بررسی‌های فنی نشان می‌دهد این اختلال در امتداد آثار حمله سایبری پیشین بر زیرساخت‌های فنی و سامانه‌های متمرکز بانکی پدید آمده است.
هفته گذشته اعلام شد تمامی اختلال‌های پیش آمده در بانک‌های تجارت، ملی و صادرات برطرف شده است.
اختلال هفته پیش باعث شده بود که در بعضی موارد، حتی انجام عملیات خرید با کارت‌های بانکی هم امکان‌پذیر نباشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/VahidOnline/76710" target="_blank">📅 17:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76709">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDmykcD3JBBz-QRuAWOFF6OFIUIKf7aeR0DdQfOsb35FIw5gulA_p2ECkJeWCDi4eLTzPUzhUDlC1W3cMDLr08XxTfm4NbFBfypgDQ1j2Z2KXxdwnaYO6w9dzkQINdi17wz0ywd5ItLb3sAkSxgkKSNi7NNzIRhOhR_udXx4VEgHzsLXVtce1Nf4RMr-LKHbOU8MPjqfMoSpxP0uWBoBGTN2k5AyU7gGTuIyB0FDSJAqajMlq2ws-3LeI6pviVclokL8eTMGYnhy6Y2H2MtfsWzI7Y9t4tczn7Crr7b92zQHIJwJBZQe-SnUJkhbwNfnhFLfPHp3NpeGIvBz30PAQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهنام گلخنی، پدر احمد گلخنی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴، روز چهارشنبه ۴ تیرماه در باغباد‌ران از توابع استان اصفهان بازداشت شده و با وجود وعده آزادی، همچنان در بازداشت به سر می‌برد.
کمیته پیگیری خبر داد آقای گلخنی پس از آن بازداشت شد که
در استوری اینستاگرام خود از مردم دعوت کرده بود تا ظهر عاشورا بر سر مزار جان‌باختگان اعتراضات حضور پیدا کنند.
بنابر این خبر قرار بود او روز شنبه ۶ تیرماه آزاد شود، اما با گذشت این موعد، همچنان در بازداشت است و اطلاعی از وضعیت پرونده یا اتهام‌های احتمالی او منتشر نشده است.
احمدرضا (احمد) گلخنی، شهروند ۳۷ تا ۳۹ ساله اهل باغبادران، در جریان اعتراضات دی‌ماه ۱۴۰۴ جان باخت. او مقابل کلانتری باغبادران هدف شلیک مستقیم قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/VahidOnline/76709" target="_blank">📅 17:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76708">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckQCCVMuwng-XF388QmIlHM4inBnt411SFdYMzri1ER01QaU1UXunKGIq5QthfJ7UnURWaBj0HEeFj8IzxOGEqiKWZw0O-NfXgy2r8zzEcU6P-CJv-uboWI_WmamgPQlYfRMpQeQxwAdLVRD0TD7CSb1LUvEsSL8WNmrPxc1RDmRiyBNNATGw2jiM-mRAmhroemPuREvSH5x4PiBp-AFv9-NgBx_GQ2vRba4L_0iFZTQYzbSM7Dol2bKcC3uB48E6-umft5tfhmM84iBf5tev9akoNkPH0JQMssu3WVmmmp9EHKVpe0kPpkhNZTyyaTykyz0zX0EKbZ3ZD9UTQDoAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل شرکت شهر فرودگاهی امام خمینی از برقراری دوباره پروازهای میان ایران و امارات تا پایان هفته جاری خبر داد و گفت: ایرلاین‌های داخلی مقدمات راه‌اندازی مجدد مسیر دوبی را فراهم کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/VahidOnline/76708" target="_blank">📅 17:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76707">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U_vcM0ijmYGEH4sonxiHbnXruk54ZBt7LC5LSKygAw2rolBW_AZpzVTVAZydT5bnYOL_e6MSh8eOd7TT6I6DFgCMVIaKFryncyZHfJzZbV4FsmOz2MD_rwJGA7RJrrFrDHY1fYmAgQOLZhoLdLA6MJ2y-xfkGq54QFeEeK9AMvsBz-PeB8yxQ2vPn1bI7PradQkN5zoM3EYA7b4E8PTZR-qGwNbixlANXFDLDONzVzxYbz4GTOZYDNJ__IKQczQ3Vl1rE-4eiif2d_eMrEZSLtxRNtQ6OLduaugbQdFlwnHhPnM0SI6Hprupu5ii4QGrmc_-7klxkvf6Qbsk5TpQQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه بحرین در بیانیه‌ای اعلام کرد جمهوری اسلامی بامداد شنبه با چند پهپاد به خاک این کشور حمله کرده است. این وزارتخانه با محکوم کردن این حمله، آن را نقض حاکمیت بحرین و تعهدات جمهوری اسلامی بر اساس تفاهم‌نامه اسلام‌آباد با آمریکا دانست.
در این بیانیه آمده است حمله پهپادی، نقض آشکار حاکمیت بحرین، تهدیدی علیه امنیت شهروندان و ساکنان این کشور و مغایر با قوانین و عرف‌های بین‌المللی است. وزارت خارجه بحرین همچنین اعلام کرد ادامه حملات جمهوری اسلامی، هم‌زمان با تلاش‌های منطقه‌ای و بین‌المللی برای کاهش تنش، روند صلح را تضعیف می‌کند و نشان‌دهنده رویکردی برای بی‌ثبات کردن منطقه است.
وزارت خارجه بحرین با اشاره به تفاهم‌نامه اسلام‌آباد افزود جمهوری اسلامی متعهد به توقف دائمی عملیات نظامی و احترام به حاکمیت کشورهای منطقه شده بود، اما حمله اخیر به گفته این وزارتخانه، نشان می‌دهد تهران به تعهدات خود و جامعه بین‌المللی پایبند نبوده است.
بحرین همچنین با تاکید بر حق خود برای دفاع از حاکمیت، امنیت و ثباتش، از شورای امنیت سازمان ملل خواست مسئولیت خود را در اجرای قطعنامه ۲۸۱۷ و پاسخگو کردن عامل این حمله بر عهده بگیرد.
@
VahidOOnLine
یک مقام آمریکایی که نخواست نامش فاش شود، به وال‌استریت ژورنال گفت حمله بامداد شنبه، ششم تیرماه ایران به بحرین شامل دو پهپاد انتحاری (یک‌طرفه) بوده است.
این مقام مسئول اظهار داشت که یکی از پهپادها توسط یک سامانه پدافند هوایی زمین‌پایه سرنگون شد و پهپاد دیگر بدون ایجاد هیچ‌گونه خسارت یا تلفاتی، در محوطه یک فرودگاه دورافتاده فرود آمد.
همچنین گزارش شده است که یک پهپاد انتحاری به نفتکشی حامل دو میلیون بشکه نفت خام اصابت کرده و نیروهای آمریکایی دو پهپاد دیگر را که کشتی‌های تجاری را هدف قرار داده بودند، سرنگون کرده‌اند.
@
VahidOOnLine
پس از اعلام دولت بحرین مبنی بر حمله پهپادی جمهوری اسلامی ایران به خاک این کشور در روز شنبه ششم تیرماه، کشورهای حوزه خلیج فارس این اقدام را به شدت محکوم کردند.
این حمله ساعاتی پس از آن رخ داد که سپاه پاسداران از هدف قرار دادن مواضع نظامی آمریکا در پاسخ به حملات سنتکام در بندر سیریک خبر داده بود.
وزارت امور خارجه امارات با صدور بیانیه‌ای، این حملات را «نقض فاحش» حاکمیت بحرین و تهدیدی برای امنیت منطقه توصیف کرد.
وزارت امور خارجه قطر نیز ضمن محکومیت این اقدام، بر لزوم پرهیز از پیامدهای این حملات «غیرموجه» و تداوم مسیر دیپلماسی برای حفظ دستاوردهای یادداشت تفاهم اخیر تأکید کرد.
در همین حال، وزارت امور خارجه کویت این تجاوزات را تضعیف‌کننده خطرناک تلاش‌ها برای صلح دانست و بر همبستگی کامل خود با بحرین تأکید کرد. جاسم محمد البدیوی، دبیرکل شورای همکاری خلیج فارس (GCC) نیز این حملات «خائنانه» را که به گفته وی زیرساخت‌های غیرنظامی را هدف قرار داده، به شدت محکوم کرد. این تنش‌ها در حالی اوج گرفته که از دو شب پیش و با حمله سپاه به یک کشتی باری سنگاپوری، فضای امنیتی در تنگه هرمز به‌شدت بحرانی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/VahidOnline/76707" target="_blank">📅 17:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76706">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FmrR0Zoog4nWrWebI8KpRp5y9yBis5WMHh7lJPbU2QRmH_rGLkKJoEZ0t7jCu0jjhBNM2CqetaL9kJN3e0pnupyTglzyYy4cqRuNXSxYBQS7A-LBxOmh90eT1Y25WJtyrLxxP6nZg-W6gijGprTloT5tgjIVGq8vYC1b-JEySudSd59I6UiaZp-X6g6QRJ4KsByz17ETV6wBZYVsq8_qh1k_atGXi7CPTm4ZIkzDZV8_NJDZJD3oyuWIuntQBiJzKEYNZGebA77m-meeJArWzPMLFlZpXhE6Igk5dfeaV5s2vN_PhWIdw4vvx3FoQbkWgINQDlr2cdswwuAFgDeJzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ می‌گوید بررسی‌های داخلی وزارت دفاع آمریکا نشان می‌دهد مجموعه‌ای از نقص‌ها در سامانه‌های اطلاعاتی و هدف‌گیری ارتش این کشور ممکن است در حملهٔ موشکی به مدرسه میناب نقش داشته باشد.
بر اساس گزارش بلومبرگ که روز جمعه ششم تیر منتشر شد، یک تحلیلگر اطلاعاتی متوجه شده بود ساختمانی که در پایگاه دادهٔ ارتش آمریکا به‌عنوان یک تأسیسات نظامی ثبت شده بود، در واقع به دبستان تبدیل شده است.
به‌نوشتهٔ بلومبرگ، منابع آگاه گفته‌اند این ارزیابی در سال ۲۰۱۹ در یک سامانهٔ دیجیتال ثبت شد، اما آن سامانه به پایگاه دادهٔ رسمی هدف‌گیری ارتش متصل نبود.
مقام‌های رسمی آمریکا تا کنون جزئیات این گزارش را تأیید یا رد نکرده‌اند.
بلومبرگ می‌نویسد تحقیقات پنتاگون همچنین بر ضعف‌های دیرینهٔ سامانه‌های اطلاعاتی ارتش آمریکا از جمله استفاده از پایگاه‌های دادهٔ قدیمی و نبودِ ارتباط کامل میان سامانه‌های مختلف متمرکز است. این گزارش می‌افزاید هنوز مشخص نیست فرماندهی مرکزی ارتش آمریکا، سنتکام، پیش از حمله از فرایند تکمیلی بازبینی اهداف استفاده کرده است یا نه.
وزارت دفاع آمریکا اعلام کرده است تحقیقات دربارهٔ این حمله همچنان ادامه دارد و جزئیات تازه‌ای ارائه نکرده است. دونالد ترامپ نیز گفته است ممکن است هرگز مشخص نشود چه کسی مقصر بوده و خود او هنوز مدرکی ندیده که قانعش کند آمریکا مقصر بوده است.
ایران می‌گوید در حملهٔ هوایی به مدرسهٔ میناب که ۹ اسفند پارسال در نخستین روز حملات آمریکا و اسرائیل به ایران صورت گرفت، دست‌کم ۱۷۵ نفر از جمله ۱۶۸ دانش‌آموز کشته شدند. شورای تشکل‌های صنفی فرهنگیان تأیید کرده که در این حمله بیش از ۱۰۸ دانش‌آموز کشته شده‌اند و گفته است معلمان هم در میان قربانیان این حمله بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/VahidOnline/76706" target="_blank">📅 17:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76705">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MrqnM4sXaqNY5vH3xTmjhZ92CX1Drb0Xjym7tMbBuB_WUvVHMUE4qbPvNQ1AUIBQ6-eUe3S4ASMA-f8_spOAXwLUXcyTfjy0E_QqEHO7wSGuLq4jyNGKwRHc2_Dj6SPB65v7_aCgcoOSSXneo9e0oOxfYXW95neJxiRur2U5bPgZ_pMw4_pM3ps0ef6iBkS70OvJ8ZlKtOr-mx9Tjy9DwQuP0ZnRuIt7uDzQJPEmwCfLm2lA0hWszBF8WevUEewr6eWrkima7VCatYet7oXRgC2ouhTcy1vA7GUo6G896nWN3U96bFsMIi7OAFaeRECX-iNhag1vikXfCbklWjZ48w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"یاسین محمودی، نوجوان ۱۶ ساله و اهل رفسنجان در استان کرمان، در جریان اعتراضات مردمی این شهر با شلیک مستقیم نیروهای حکومتی جان خود را از دست داده است.
بنابر اطلاع ایران‌وایر، یاسین محمودی روز جمعه ۱۹ دی‌ماه ۱۴۰۴ در خیابان طالقانی، ابتدای سه‌راه امیرکبیر رفسنجان، هدف شلیک مستقیم نیروهای حکومتی قرار گرفت.
گلوله به ناحیه شکم این نوجوان اصابت کرد و او بر اثر شدت جراحات جان باخت."
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/VahidOnline/76705" target="_blank">📅 17:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76704">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r7XgV-Xfl_MduIaIeTAtc_aLdQZ0SzJobSKLcuF_UYhfz-xh_CR01SzFO78VoDsdTpq2SUHyjiG-1okfjieUIVwSFLPo1ZDmi9PDMhO6dYLClXi-y-_whFmtebnKRijpMPB-VLWJ0oQcPUiaqSS77Vzu2IShzw5mHo8QG_618-Iuh8FKqLuRQjoBsro8X78aHSecsjbMh7Zxn0NCVEtX7mnbNKV6SllFwvfTzvf5PbBzZS9rA2WJ4dkxOUGlMzce-kweWKwa7qTGYY1D5rjj-8Jim4UTAqmgxxVnIJwuXWfWRePNx98NfVYn3RoSL4lMU_KVnd5v2xwYA9lpiOXDOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسابقه فوتبال ایران و مصر با نتیجه مساوی یک یک به پایان رسید.
بلژیک با پیروزی ۵ به یک بر نیوزیلند و مصر هم با ۵ امتیاز و به‌دلیل تفاضل گل کمتر، به عنوان تیم‌های اول و دوم به مرحله حذفی صعود کردند.
به این ترتیب صعود ایران به نتیجه بازی‌های غنا با کرواسی، ازبکستان با کنگو و الجزایر با اتریش گره خورده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/76704" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76703">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=fQ-PDZAvaBX6BQWlk-lg6fovRSaxEJEilUPbnfGnG2eFcTuJS1stFICiJrtgMQvLy11I9dgH6hz_BHYLgd8hgNJrd1_NvEaj02GiZAG21JPJ42N_hP_E1Aw42lSVWrUXpc9NSGzccbfWG43wiCqaOK8qRP9majMCVUhXY05lEaGq9uOhB5SYy5U-OnWHYmCU4TqN-uGlqlsvMKuxhV4na87brSUmIqbNprmrrs5H9LhCZVws1pLCEUkcEzwOKzUj1rWuKbZzPCbxva_5VhP7FHiXHxE8JlPy7FU846PvlSOK054Dei4vD0hrW_qGb62m5iBidRKDO8U2wVJqAnsC8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=fQ-PDZAvaBX6BQWlk-lg6fovRSaxEJEilUPbnfGnG2eFcTuJS1stFICiJrtgMQvLy11I9dgH6hz_BHYLgd8hgNJrd1_NvEaj02GiZAG21JPJ42N_hP_E1Aw42lSVWrUXpc9NSGzccbfWG43wiCqaOK8qRP9majMCVUhXY05lEaGq9uOhB5SYy5U-OnWHYmCU4TqN-uGlqlsvMKuxhV4na87brSUmIqbNprmrrs5H9LhCZVws1pLCEUkcEzwOKzUj1rWuKbZzPCbxva_5VhP7FHiXHxE8JlPy7FU846PvlSOK054Dei4vD0hrW_qGb62m5iBidRKDO8U2wVJqAnsC8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم  ترجمه ماشین: حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری  تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی…</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76703" target="_blank">📅 06:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76702">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DR0Hjp0i50Q-1wr4d1JiAPrxRopA2Ixp4gngzEq7ZhegflO80wE9YNgAheNwC7nXOFbb8qMsPhinFOvZfPhDdiWXTjZCPNLRxrvO3-vkRTIvuKi0CGcEyKnUndQ63o95v4QzjIv6MHhrtLmSi_gr1LMn3x9_K_twum_51lsseBg5a_Olv1jhFPWs65_vRzXnGwqxLGG5UVqcIAgqcI-uAAkNMclmtuxYXX7pkbYllXNTod4euIXVxay3ESwg0PzdKXVKMbaRqAcyr7RBjoZ_HpoqbKXsBwdDKkdypHKRaml5rxBlHaOKOJu5VnXTBa5_AIbNW_KQrs63oqulfAwvSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌سپاه پاسداران اعلام کرد که نیروی دریایی این نهاد در واکنش به حملات آمریکا به سواحل ایران، مواضع ارتش آمریکا در منطقه را هدف قرار داده است.
در بیانیه روابط عمومی سپاه آمده است که آمریکا پس از حمله به یک کشتی تجاری در تنگه هرمز، به بهانه عبور این کشتی از مسیری که ایران آن را «غیرمجاز» می‌داند، حملاتی هوایی به سواحل ایران انجام داده است.
سپاه این حملات را نقض آتش‌بس و تعهدات آمریکا خواند و مدعی شد در پاسخ، «نقاط استقرار ارتش آمریکا در منطقه» هدف قرار گرفته‌اند. جزئیاتی درباره محل این اهداف، نوع حمله یا خسارات احتمالی منتشر نشده است.
در این بیانیه همچنین گفته شده است که بر اساس بند پنجم تفاهم‌نامه اسلام‌آباد، کنترل عبور و مرور در تنگه هرمز بر عهده ایران است.
سپاه هشدار داد که در صورت تکرار حملات آمریکا، پاسخ ایران گسترده‌تر خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76702" target="_blank">📅 03:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76701">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z0baDs_PGvHxoUqO3Mn75mGyVtCdk6Fl3baeNgPkr0yYaA8lsHRCuxcbwC64pWU1A6wrmHlG4vSeD0vf0GvVfdvd3BmJVtHiAQ2Yd6dJr0WmB1kt5gL8fvrLgWVoTgIljWiA06vm_oFtwQFcX1obJO-hgNwN0ydKcqM5nq56A2CRBIP-CJCfUAD5HSYzT7w3mWh31f6VjcqS5vehSaYjmqnLL1Elvvh3XKP5KsW699VvzcJkXankZhyV1aW3ucP3L_L6NKLfQAEyD6UztqDUo-kJwgLF5JcBAoYftXdF6uNAQT2F3nzShJGMXMIwHPmWCO800mMZXTnHO-NPRGeLAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
رسانه‌های داخلی در ایران از درگیری مسلحانه میان نیروهای حکومتی و گروه‌های مخالف مسلح در «ایست بازرسی بانه - سقز» خبر دادند. گزارش‌های اولیه آنها حاکی از آن است که دو نفر از نیروهای حکومتی کشته‌ شده‌اند. همچنین گزارش شده است که پنج نفر دیگر نیز مجروح شده‌اند. جزئیات بیشتری منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76701" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76700">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hwxO1XK9wPN-psG4lEDK58G_F-OrmVHaj8njYVusmcaWqyjLEmzaF-eRj5NW-qpvo8qxQychrjM7baGZqYXmS2LL4h-7y1a3mbwEYnQ74fN_ZO_fnFayHWjrreiwJpTxl2JMxpR0agq4ima1nCjLHiz3h_Kn1I4IwS_av0b_pHDF9W3MuqPUcxxat6sgEkmMZbRnzE3rBFeKy2NQr9YlZaUeoyn3LTtTkfGFz15lDVci_m4PYvj7zd37ghuBsXaCnhjsNbsUgpuOyaygz91DGZdSXa-qnVqhDbhFE1S3aJBTjasF_CkzqpcRXLagWjil8SsXEChSn2APveEITQPIbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم
ترجمه ماشین:
حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آن‌که ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک‌طرفه به کشتی M/V Ever Lovely حمله کرد،
انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند.
این کشتی باری با پرچم سنگاپور، هنگام حمله ایران، در امتداد ساحل عمان در حال خروج از تنگه هرمز بود.
این تجاوز بی‌دلیل نیروهای ایرانی علیه کشتیرانی تجاری، آشکارا آتش‌بس را نقض کرد. افزون بر این، رفتار خطرناک ایران آزادی کشتیرانی را تضعیف کرد؛ آن هم در حالی که جریان تجارت به‌طور فزاینده‌ای از این کریدور حیاتی تجارت بین‌المللی عبور می‌کند.
نیروهای CENTCOM همچنان هماهنگی و پشتیبانی برای عبور امن کشتی‌های تجاری از این تنگه را فراهم می‌کنند. ارتش آمریکا همچنان حاضر و هوشیار است تا اطمینان حاصل کند که همه جنبه‌های توافق با ایران رعایت و اجرا می‌شود و کاملاً به قوت خود باقی است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76700" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76699">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SWMCAPbwQUmQUlNQPlomtF-7oeU1NoZC7iLNwmESaTSIRZobueYEzkFhYhIAZYZtf6b0r20jmbICcA9u9TJdRMgJaaep3Rpq58ThqLUn_ZH18EonLDTbDB6DK1zLvA6mUyuJCkDovNoBmVTvYkhQyrakeBu_prS3L5tap12g95q6lzrnxpI3RXctrZeptWGaBEwbvQL1arVf33CQhjcfJXgbuhWoYf7vElHYos7VJlaH47jLyn3woIDIbT1Rc67U46wm4dCwMt7lTIvKpMtPw-9i4b9NaTZts5aYjUzvdIuke8n_8VEMH667jXLNrPDwcO8qgbJhcALM3m-_hHw_ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:
دقایقی قبل ؛ شنیده شدن صدای انفجار در طاهرویه سیریک
منشأ صدا هنوز مشخص نمی‌باشد.
اطلاعات تکمیلی متعاقبا اعلام می‌گردد.
من ساعت ۲۳:۳۰ این پیام‌ها رو دریافت کرده بودم:
اسکله طاهرو رو زد  ۳ ،۴ بار
زده بطرف تنگه
سیریک گروگ سه تا صدای انفجار
آپدیت:
تکمیلی| به گزارش خبرنگار صداوسیما در سیریک:
ساعت ۲۳ و پانزده دقیقه امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.
یک منبع آگاه نظامی علت این انفجارها را اصابت پرتابه به محدوده اسکله طاهرویی سیریک بیان کرد.
این منبع آگاه نظامی گفت: حدود ۵ ساعت پیش چند شلیک اخطار از شهرستان سیریک به شناورهای متخلف‌ در تنگه هرمز پرتاب شد.
همچنین شنیده ها از شلیک دو موشک اخطار ساعاتی پیش از حوالی کرپان به سمت تنگه هرمز حکایت دارد.
و
خبرنگار آکسیوس به نقل از یک مقام آمریکایی، جمعه‌شب، پنجم تیرماه، گزارش داد: «ارتش ایالات متحده حملاتی را در منطقه تنگه هرمز انجام داده است». پیش از این، صداوسیما از شنیده‌شدن سه انفجار در طاهرویه سیریک خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76699" target="_blank">📅 23:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76698">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83b030969e.mp4?token=eYP_tEYlef5B6bKmWYpsINoiBQxHIaeanis2vpWmPnf1oMgeYe6MDWjfySTYKhRuqqJn8hD2LYlXWEQXHfXc17V1s_vlcdqstP1oAV-dSW9UJ-H3gjkjNk4BGunQ3U-vCwoOBmgBZD6aVYjQ7_Q-IxfGLKdHDXIi2BiZ40VN8G_LdyVovc8UEWgWX7iDgHEyF3mtDiGxdu5mIWxEyAGmSKVeqHLRKfaHaPPj-2my8dlgQPVQJjyoA_g8s72ePoshj9nZHD7zOWXRHAAhZTI4mE-4YfaXB1JlkE3vkB-JWEuC2n3N1FwOgKa93QcANP5FoGEYWxozrPSF8x-N97U1OGIHi5Jf22_qfKG-8t4e7xLc6-7p7e3bUvcMZMpDS8YKla6E-DrgWuUJ0ZtkOI1zaMQMkS5eNvm8k7gYddLc_SELYzZehb9PfPzx3PD8qmUOFFDb1msSL2-TDFNtNFCr12wgDVS4e3bcQ0fLYuzMuQV4epWLh00aHhoqDZOc8V2kl4A3Wnkz3zCqE8p-WizQ94xzr8grbbYNpxVFvu7ofiWRnXqG_dyd0N0SOVUhJpmVKGN9J9bvkGxwHCwC7SFfczISB8F8KqOUTxlsKdH4p5nvBhbAJxufs3LWy9zQsEHs0_4MPRR5VsgIRAOugFs8j6IurBNaZAjIj7EsvDhqDXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83b030969e.mp4?token=eYP_tEYlef5B6bKmWYpsINoiBQxHIaeanis2vpWmPnf1oMgeYe6MDWjfySTYKhRuqqJn8hD2LYlXWEQXHfXc17V1s_vlcdqstP1oAV-dSW9UJ-H3gjkjNk4BGunQ3U-vCwoOBmgBZD6aVYjQ7_Q-IxfGLKdHDXIi2BiZ40VN8G_LdyVovc8UEWgWX7iDgHEyF3mtDiGxdu5mIWxEyAGmSKVeqHLRKfaHaPPj-2my8dlgQPVQJjyoA_g8s72ePoshj9nZHD7zOWXRHAAhZTI4mE-4YfaXB1JlkE3vkB-JWEuC2n3N1FwOgKa93QcANP5FoGEYWxozrPSF8x-N97U1OGIHi5Jf22_qfKG-8t4e7xLc6-7p7e3bUvcMZMpDS8YKla6E-DrgWuUJ0ZtkOI1zaMQMkS5eNvm8k7gYddLc_SELYzZehb9PfPzx3PD8qmUOFFDb1msSL2-TDFNtNFCr12wgDVS4e3bcQ0fLYuzMuQV4epWLh00aHhoqDZOc8V2kl4A3Wnkz3zCqE8p-WizQ94xzr8grbbYNpxVFvu7ofiWRnXqG_dyd0N0SOVUhJpmVKGN9J9bvkGxwHCwC7SFfczISB8F8KqOUTxlsKdH4p5nvBhbAJxufs3LWy9zQsEHs0_4MPRR5VsgIRAOugFs8j6IurBNaZAjIj7EsvDhqDXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش مرتبط با ایران در سخنرانی ترامپ به تشخیص ماشین
متن  زیرنویس:
https://telegra.ph/trump-06-26-4
بعضی از جملات:
ایران هرگز سلاح هسته‌ای نخواهد داشت. نمی‌گذاریم چنین اتفاقی بیفتد.
و به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، ایران امروز نه نیروی دریایی دارد، نه نیروی هوایی، نه توان پدافند هوایی، نه رادار، و عملا نه تولیدی. ظرفیت پهپادی‌شان ۸۲ درصد کاهش یافته است. ظرفیت موشکی‌شان ۸۰ درصد کاهش یافته است. پرتابگرهای موشکی‌شان ۹۰ درصد کاهش یافته است. رهبری‌شان یک بار کشته شده، و رهبری‌شان برای بار دوم هم کشته شده.
و دیگر هیچ‌کس نمی‌خواهد رهبر ایران شود. گفتند: «چه کسی می‌خواهد رئیس‌جمهور شود؟» بعد همه گفتند: «نه، ممنون.»
این کار باید در دوره ۴۷ ساله‌ای انجام می‌شد که آن‌ها با ترور حکومت کردند. و همین کار را کردند. با ترور حکومت کردند. وقتی مرد یا زن جوانی را می‌بینید که بدون پا یا بدون دست راه می‌رود، یا چهره‌ای که از بین رفته، این به خاطر بمب کنار جاده‌ای بود که ساخته شد؛ ساخته ژنرال سلیمانی، که من در دوره اولم او را کشتم. و آن یک کشتن بزرگ بود.
هنوز می‌توانند شلیک کنند؛ می‌دانید، دیروز یک پهپاد را به سوی یک کشتی بزرگ که وارد تنگه هرمز می‌شد شلیک کردند. چهار تا شلیک کردند. ما سه تای آن‌ها را ساقط کردیم. یکی از آن‌ها؛ فکر کنم؛ ما از دستش ندادیم. کسی آمدنش را ندید و به کشتی خورد و مقداری خسارت زد. اما نمی‌توانند چنین کارهایی بکنند.
و فراموش نکنید وقتی باراک حسین اوباما JCPOA را انجام داد. ببینید، اگر به آن نگاه کنید، باراک حسین اوباما؛ اسمش را شنیده‌اید؟ او فاجعه بود. فاجعه بود. او ۱.۷ میلیارد دلار پول نقد به آن‌ها داد. ۱.۷ میلیارد دلار پول نقد و ده‌ها میلیارد دلار. آن را به ایران داد. فکر می‌کرد می‌تواند دوستی آن‌ها را بخرد. و دقیقا برعکس شد. آن‌ها از پول استفاده کردند و موشک ساختند و هر چیز دیگری.
و من برجام را لغو کردم؛ توافقی که... همان توافق هسته‌ای ایران بود؛ فاجعه بود. ضمنا مدت‌ها پیش منقضی شده بود، اما من مدت‌ها قبل از انقضایش لغوش کردم. اگر این کار را نمی‌کردم، ایران سلاح هسته‌ای داشت. اگر ۱۰ ماه پیش بمب‌افکن‌های B-2 را نفرستاده بودم، آن‌ها سلاح هسته‌ای داشتند. ما آن تأسیسات هسته‌ای را نابود کردیم. بسیار مهم بود.
و آن وقت دیگر اسرائیلی نداشتید. اسرائیل نابود شده بود. می‌دانم در این اتاق طرفداران خوب اسرائیل زیاد دارید. و اسرائیل نابود شده بود و احتمالا خاورمیانه هم نابود شده بود. و ما... آن‌ها می‌توانستند ضربه‌ای بزنند. ما خیلی سریع نابودشان می‌کردیم، اما آن‌ها می‌توانستند به ما هم ضربه‌ای بزنند.
بازار سهام از زمان انتخابات ۷۳ رکورد تاریخی ثبت کرده است. و امروز شمار بیشتری از آمریکایی‌ها نسبت به هر زمان دیگری در تاریخ کشورمان مشغول کارند. این خیلی خوب است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76698" target="_blank">📅 23:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76696">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tAKg3DYmClkoRR8UzAj7CdlJdvb5bYLEvBFUCpI2MqCgJPdBnXkyb7rLrmRsu6xs_43vG9TzxguxX6yG3BF_l0m-t5kgNg_kxsMs2Jj5ojHw5Hfm8jdTsGy9JzHfQ2JstCCNAq9K3Koy4EylUg1N6TCK1aMPk6HlHbmBy5a7NfQEZkZcnzKoC-SLhKXs35C8x5YxHcEubxlvkMHWHNiijKe7vJqicneWl9HXdEGYbQ4qY0YPgUF7hjjCNAcFw-wDsQRJz7wd3aIcSkVcCnYGc9Rf00Ck_FYf6rzGFr3YnCJrCL93MuQsQUD3M6PRB5H-uCHjBzoQQjhOgd-5CPWMsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iYPRTKzMJeIi3aiNXbI1YRSI1FRvlHOktIKbeu5WcvE1E2aPdVg72x2iZ8RYJ0FOSEiYhm9OzOxQOY00cfoRgY5OXz84Zn-J5iQwSOaXE7ZG64q7iIA7YZ7tEq7Z5tCEGlEj41DV41KnewNm6zk4w1kahMK_AkrXaPyW9jgKHK0msZHNTqUH_mWm4P8tVscQQi_0Npg4Mf8yTIaSj7FBjGf8I7_2522Zou5InkasCEZeELwDNGTRsxXKiTWml9LhmTQ3fs-NVrhL_MHnZYhYXoVz654k-kumUR9YTS-YtlcV2om9cxI8LjcGtKLUM1kGSLegzwas4MEdRhFmljUkRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، پس از امضای توافق اسرائیل و لبنان در واشینگتن در بیانیه‌ای اعلام کرد: «این توافق دستاورد بزرگی برای اسرائیل است و مذاکرات طولانی در واشنگتن به نتیجه رسیده است. مهم‌ترین نکته این است که اسرائیل در منطقه امنیتی باقی می‌ماند و تا زمانی که حزب‌الله خلع سلاح نشود این وضعیت ادامه خواهد داشت.»
او افزود: «این توافق ضربه بزرگی به جمهوری اسلامی است و تهران تلاش می‌کند اسرائیل را به عقب‌نشینی وادار کند اما اسرائیل، لبنان و آمریکا تاکید کرده‌اند که جمهوری اسلامی و حزب‌الله در این روند نقشی ندارند.»
نتانیاهو تاکید کرد: «اسرائیل در منطقه امنیتی باقی خواهد ماند و اجازه ورود حزب‌الله یا غیرنظامیان به این گروه داده نخواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76696" target="_blank">📅 22:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76695">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=kpArwTsQzr8OBU-ES1F7MjLwbhNOBJERP9-ZOtmXf0xUVoS6e0NvL8xwqc1W97J3wdnjkf2SCY0byEsgiCTI1H6MRuQCocAzKt66AUhCh_Ior99fxES0uwbevxEQ6uUBfEebBpqVeo4o49VyAJIhV9XFyVaBmTXWJzHY0v-HCxQpFtMCy1NXxQSUniDawKIh6_QUZYKKjeqfAUGmSLV5CE5ut_hfpjP_NSU9i6LTRbcuK5qq7INTXKE2DOff-YX7gS_doCTUVbN5Vf-_LEWlNQ13OD0HN5Y6ZCpkSJOOcamNZl-tytc0dJrUET8icjo_lA4lOC2usZ6ZThNVZbtfwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=kpArwTsQzr8OBU-ES1F7MjLwbhNOBJERP9-ZOtmXf0xUVoS6e0NvL8xwqc1W97J3wdnjkf2SCY0byEsgiCTI1H6MRuQCocAzKt66AUhCh_Ior99fxES0uwbevxEQ6uUBfEebBpqVeo4o49VyAJIhV9XFyVaBmTXWJzHY0v-HCxQpFtMCy1NXxQSUniDawKIh6_QUZYKKjeqfAUGmSLV5CE5ut_hfpjP_NSU9i6LTRbcuK5qq7INTXKE2DOff-YX7gS_doCTUVbN5Vf-_LEWlNQ13OD0HN5Y6ZCpkSJOOcamNZl-tytc0dJrUET8icjo_lA4lOC2usZ6ZThNVZbtfwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم.
ویدیوی بالا درباره ایران نیست.:
ترجمه ماشین: همان‌طور که دیدید، کمونیست‌هایی که اخیراً در شهر نیویورک انتخاب شدند، سوسیال‌دموکرات نیستند. آن‌ها می‌خواهند شیوه سنتی زندگی آمریکایی را کاملاً نابود کنند.
فروختن کمونیسم خیلی آسان است. همه‌چیز را نابود می‌کند، اما فروختنش خیلی آسان است. صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. می‌گفتم اجاره رایگان است؛ خانم‌ها و آقایان، از این به بعد لازم نیست هیچ اجاره‌ای بدهید. از این به بعد هر کسی خانه می‌خواهد، نگران نباشد؛ فقط خانه‌ای را که می‌خواهد انتخاب کند. همه غذای رایگان می‌گیرند؛ از این لحظه به بعد همه‌چیز رایگان است. همه به من رأی می‌دادند.
مشکل اینجاست که بعد از دو یا سه سال، کشور به منطقه‌ای فاجعه‌زده تبدیل می‌شود. کشور شکست می‌خورد. همیشه همین‌طور می‌شود. فروختنش خیلی آسان است. آن سال اول، آدم فوق‌العاده محبوبی هستید. همین حالا هم این اتفاق در نیویورک و کالیفرنیا دارد می‌افتد.
اما بعد شروع می‌کنید به زندگی در فلاکت. در فلاکت زندگی خواهید کرد. غذایی وجود نخواهد داشت. مسکنی وجود نخواهد داشت. ارتشی وجود نخواهد داشت. قانون و نظمی وجود نخواهد داشت. هیچ‌چیزی وجود نخواهد داشت. از هر نظر به ساکن جهان سوم تبدیل می‌شوید و همه رنج خواهند کشید یا خواهند مرد. رنج می‌کشید یا می‌میرید. این همان چیزی است که اتفاق می‌افتد. هزاران سال است که این اتفاق با نام‌های مختلف افتاده است.
به شما می‌گویم، من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. خیلی آسان بود. لازم نبود کار کنید؛ می‌توانستید در خانه بمانید. مشکل این است که چند سال می‌گذرد و کل آنجا فرو می‌پاشد. همیشه همین‌طور می‌شود؛ همیشه همین‌طور بوده است.
اما متأسفم که بگویم ترور کسانی که با آن‌ها مخالف‌اند، عنصر بسیار مهمی در ایدئولوژی آن‌هاست. ترور برای آن‌ها مسئله بزرگی است. آن‌ها حیوان‌اند. حیوان‌اند.
در خیلی از موارد باهوش نیستند، اما در بعضی موارد هستند. جذب پیرو برایشان آسان است، چون وعده‌هایی می‌دهند که خودشان می‌دانند نمی‌توانند عملی کنند. و دموکرات‌ها هم مقابله نمی‌کنند. برای همین احمق‌اند. مقابله نمی‌کنند. می‌ترسند. من شومر [احتمالاً اشاره به چاک شومر] را می‌بینم؛ از جنگیدن می‌ترسد. آدم‌هایی را می‌بینم که نسبتاً معمولی‌اند و آدم‌هایی که ما با آن‌ها مخالفیم؛ آن‌ها از جنگیدن می‌ترسند.
دموکرات‌ها چرخش عظیمی به چپ داشته‌اند. من به بعضی از کسانی که آن شب در نیویورک انتخاب شدند نگاه کردم. این‌ها از خیلی جهات آدم‌های احمقی‌اند؛ از بعضی جهات از نظر فکری احتمالاً نسبتاً باهوش‌اند، اما آدم‌هایی هستند که می‌خواهند کشور ما را نابود کنند. آن‌ها از کشور ما متنفرند. از مردم ما متنفرند. از حزب دموکرات متنفرند.
حزب دموکرات در دردسر بزرگی است، چون این ماجرا با نیویورک متوقف نمی‌شود. این مسیر، انتخاب شدن را بیش از حد آسان می‌کند. همه‌چیز، به نوعی، برای انتخاب شدن بیش از حد آسان است. بسیار خطرناک است، اما به‌زودی چیزی برایتان باقی نمی‌ماند. مشکل همین است.
از خیلی جهات، آن‌ها اجازه می‌دهند این افراد راه خودشان را بروند و هر کاری می‌خواهند بکنند. می‌گویند نمی‌خواهیم ریسک کنیم و حرف بدی بزنیم، چون می‌ترسیم اگر این کار را بکنیم شغل‌مان را از دست بدهیم. می‌ترسند انتخابات خودشان را ببازند، حتی اگر فقط به گفتن چیزی درباره این نسل تازه آدم‌های بیمار فکر کنند.
آن‌ها آن‌قدر باهوش یا سرسخت نیستند که با طاعونی که در جریان است بجنگند. این دارد درست جلوی چشم شما اتفاق می‌افتد. اگر همان‌طور که با جمهوری‌خواهان می‌جنگند، یا همان‌طور که با من می‌جنگند، با آن‌ها می‌جنگیدند، پیروز می‌شدند. آن‌ها ما را شکست ندادند، اما در برابر کمونیست‌ها پیروز می‌شدند؛ ولی شجاعت این کار را ندارند.
پس خودشان دارند کمونیست می‌شوند و به یک حزب کمونیست تبدیل می‌شوند. این‌ها سوسیال‌دموکرات نیستند. این‌ها کمونیست‌های سرسخت و بی‌خدا هستند. کمونیست‌های بی‌خدا هستند. همه کمونیست‌ها بی‌خدا هستند. به خدا باور ندارند.
به نظر من، این جدی‌ترین تهدید علیه کشور ما از زمان تأسیس آن، حدود ۲۵۰ سال پیش، است. این تهدید بزرگی برای کشور ماست.
درباره ایران هم:
ترامپ در کنفرانس سیاست‌گذاری ۲۰۲۶ ائتلاف ایمان و آزادی، گفت: نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. نمی‌توانیم بگذاریم این اتفاق بیفتد.
آن‌ها دارند از شدت نیاز برای رسیدن به توافق التماس می‌کنند. آن‌ها خیلی چیزها به ما می‌دهند. این باید در طول ۴۷ سالی که با ترور حکومت کرده‌اند انجام می‌شد.
رسانه‌های جعلی می‌گویند آن‌ها امروز خیلی قوی‌تر از چهار ماه پیش است اما آن‌ها اکنون خیلی چیزها به ما می‌دهند.
@
VahidOOnLine
📡
@VahidOnlin</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/76695" target="_blank">📅 22:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76694">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=ffMf1h7wUpLlAcij9hQugzfHwaEVGndlg7hfO5kt8aCuJc0oqgW135m_JyXm8a40_7r7sX6GVCY1nGv7b_7RuKXNYgAuhwULYs7zes8BWtOpFrQLC9FDduafvealVKY-ny1YhmgcFPFMVr8ITAIoQ_K3Ec3HIwyOIiwHRfeMrFNZc8s7FKakuaXbtXMwajSwwKGWyQ31gLuv_90oyEJFVbD5L219UaIxIV2tvZ35rLO1D_c_VPlcVAEBBFRtHb3i0X9J4hxyE2_kdVOPYdRYzQlTN-8JV4NTaFiN6__nifmFDJ6YFsbYwm6UztHHz_Orr7jXUcajnVow8-F428hl0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=ffMf1h7wUpLlAcij9hQugzfHwaEVGndlg7hfO5kt8aCuJc0oqgW135m_JyXm8a40_7r7sX6GVCY1nGv7b_7RuKXNYgAuhwULYs7zes8BWtOpFrQLC9FDduafvealVKY-ny1YhmgcFPFMVr8ITAIoQ_K3Ec3HIwyOIiwHRfeMrFNZc8s7FKakuaXbtXMwajSwwKGWyQ31gLuv_90oyEJFVbD5L219UaIxIV2tvZ35rLO1D_c_VPlcVAEBBFRtHb3i0X9J4hxyE2_kdVOPYdRYzQlTN-8JV4NTaFiN6__nifmFDJ6YFsbYwm6UztHHz_Orr7jXUcajnVow8-F428hl0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره‌کنندگان ایالات متحده، اسرائیل و لبنان پس از پنجمین دور از گفتگوهای دیپلماتیک، روز جمعه پنجم تیرماه، یک چارچوب سه‌جانبه را امضا کردند.
این مذاکرات شامل بررسی پیشنهادی با حمایت آمریکا بود که بر اساس آن، نیروهای اسرائیلی بخشی از قلمرو تحت اشغال خود را به ارتش لبنان واگذار کنند.
پیش از آغاز این دور از گفتگوها، لبنان خواهان خروج کامل نیروهای اسرائیلی از خاک این کشور بود؛ در حالی که برای اسرائیل، شرط اصلی هرگونه عقب‌نشینی، خلع سلاح کامل حزب‌الله و دریافت تضمین برای بازنگشتن نظامی این گروه به مناطق مرزی است.
روبیو در مراسم امضای این توافق‌نامه گفت: «این آغازِ آغاز است. کارهای زیادی در پیش داریم. امروز اولین قدم است و گاهی اوقات، اولین قدم سخت‌ترین قدم است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/76694" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76692">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=FBsEE9s7-8tpDSNwWkKRpJ54O7ukFBCVKUDGIzznh9fkqfUj6PATa8OW-x4tLHwkbRlQ5Sn4q7xGJUOm526YEW8Ymcwu4ynbWhmFr_waavJhjUaO7EFRpSQ3gNzBrwYs2VbSXIatsbjn6VAMy2V9j0XGTPIok20Eyx2MMgbmujbUlhiwK_6pmOdKlazGZ-aXXvx2o4hteCtEz3MoZqcEx_ZLa3JaXxZop7FT07WOf-2TnRHah92tAK8qYClb1qQcM-XYaPLFfb_4RehFkQmxDLL1qZX916Tq4JoxgeI9I0kxD8TpemrXIJQ19__U8SyWrztzlzEsw9Gdjc80PkPcvw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=FBsEE9s7-8tpDSNwWkKRpJ54O7ukFBCVKUDGIzznh9fkqfUj6PATa8OW-x4tLHwkbRlQ5Sn4q7xGJUOm526YEW8Ymcwu4ynbWhmFr_waavJhjUaO7EFRpSQ3gNzBrwYs2VbSXIatsbjn6VAMy2V9j0XGTPIok20Eyx2MMgbmujbUlhiwK_6pmOdKlazGZ-aXXvx2o4hteCtEz3MoZqcEx_ZLa3JaXxZop7FT07WOf-2TnRHah92tAK8qYClb1qQcM-XYaPLFfb_4RehFkQmxDLL1qZX916Tq4JoxgeI9I0kxD8TpemrXIJQ19__U8SyWrztzlzEsw9Gdjc80PkPcvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که امدادگران در ونزوئلا همچنان در جستجوی بازماندگان زلزله‌های ویرانگر شامگاه چهارشنبه در میان ساختمان‌های فروریخته هستند، تازه‌ترین گزارش‌ها، حاکی از کشته شدن بیش از ۵۸۰ نفر و زخمی شدن حدود سه هزار نفر بر اثر این حادثه است.
بیم آن می‌رود که شمار قربانیان بسیار بیشتر باشد. بسیاری بی‌خانمان شده‌اند یا به دلیل آسیب‌دیدگی و ناامن بودن ساختمان‌ها، از بازگشت به خانه‌های خود هراس دارند.
در کاراکاس، پایتخت ونزوئلا، و شهر ساحلی نزدیک آن، صدای افرادی که از زیر آوار ساختمان‌های فروریخته درخواست کمک می‌کردند، شنیده می‌شد.
پیش از این مقامات ونزوئلا گفته بودند که حدود ۳۰ پس‌لرزه هم پس از دو زلزله شدید روز چهارشنبه ثبت شده است.
در پی وقوع این زلزله سازمان زمین‌شناسی آمریکا هشدار داده بود که تعداد قربانیان این حادثه ممکن است به هزاران نفر برسد.
@
VahidHeadline
هم‌زمانی این زلزله با بازی برزیل و اسکاتلند در جام جهانی خیلی‌ها رو یاد فاجعه ۰۰:۳۰ بامداد پنج‌شنبه ۳۱ خرداد ۶۹ در استان گیلان انداخت که همزمان با بازی همون دو تیم در جام‌جهانی ۹۰ ایتالیا اتفاق افتاده بود.
زمین‌‌لرزه‌ای که حدود ۴۰ هزار نفر رو کشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/76692" target="_blank">📅 19:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76691">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8qihro49aoK1z5CB0KzsFUDsexOqAbgeHDuG57g0l8Gep9Vw2TDW91vaEaugSPYi2iUCeV6pW2SL9ixMpXU7omTEb4Om6UD4fBKQ__fVROcQ_u2O5eyEczbYuPtd1zvcfHIf-NMNp36zM3IGoKzTvc_WOQS8S-L_qSf8M2EMIwGhAV46Z5BGQm3cAd6jSbMTpXLXJ--yZuIWsyM87Y5HzuU0otkR8HKjrM5eWqhpohOUV1pgmzLoCL8tsfBo26RWJnjNrryyaIZAQm-dDsIyNuUwWbx3kZX2kCdi-vB8-CmsrK3yJeS5m9nPQgI2Ylm5iXvWKqWQaX9FNpAx6G2YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی گزارش داد که روز جمعه، پنجم تیرماه، سپاه پاسداران سه نفت‌کش خارجی را که قصد داشتند از مسیری «غیرمجاز» از تنگه هرمز عبور کنند، بازگرداند. این نفت‌کش‌ها تلاش داشتند از «کریدور جنوبی» استفاده کنند؛ مسیری که اخیرا عمان و سازمان بین‌المللی دریانوردی (IMO) به عنوان یکی از دو مسیر موقت برای تردد در این آبراه پیشنهاد داده‌اند.
جمهوری اسلامی با رد این توافق، مسیر پیشنهادی جدید را «غیرقانونی، غیرقابل‌قبول و بسیار خطرناک» خوانده و تاکید کرده است که تنها مسیر قانونی برای عبور از تنگه هرمز، همان مسیری است که پیش‌تر توسط تهران تعیین شده و از نزدیکی سواحل ایران می‌گذرد.
داده‌های ردیابی «مارین‌ترافیک» نیز نشان می‌دهد که سه نفت‌کش پس از حرکت در مسیر جنوبی تغییر جهت داده و بازگشته‌اند و سه کشتی دیگر نیز مسیر خود را به سمت شمال و آب‌های تحت نظارت ایران تغییر داده‌اند.
این در حالی است که به گزارش «لویدز لیست»، بسیاری از کشتی‌ها در هفته جاری از مسیر پیشنهادی عمان استفاده می‌کردند. این اقدامات همزمان با تنش‌های اخیر پیرامون مدیریت این آبراه راهبردی صورت می‌گیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/76691" target="_blank">📅 19:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76690">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QhIB_yHg41cYSQ9Xfa9XCFJFq5iPPkqJ5jy43Ax95FIiJ5iEPdT4KaoiiKi4sCumkHMfPzfU3ddxkuPYvKkZWzKzYHc_M0-uuex7aKcLOcrVwoBSLNfd_JCKUPlt_wjSkuF0d-u1OGVetGJtD4-VKNOg1PuAmru637t9Xu_u0ob3E0gTElo0RqJUGoh_eZql1Rp8yRzmEJLZodubDojHyadvKsFFPxVNmuJSpmcRVr3ra97rmU7ndsDJvSHpZPw0Oj0OZUmFgnzuaAsemhmdriT59SJ_cPoc07k0cc5lBD2PUnCeOYww3pnEz881pNAugiwX7p-FlJNtAElUWSHrmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
جمهوری اسلامی ایران دست‌کم چهار پهپاد حمله یک‌طرفه را به سوی کشتی‌هایی که در حال عبور از تنگه هرمز بودند شلیک کرد.
یکی از این پهپادها به‌طور مستقیم به عرشه بالایی یک کشتی بزرگ و بسیار گران‌قیمت حمل بار برخورد کرد. خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این نقض احمقانه توافق آتش‌بس ماست.
رئیس‌جمهور  دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/76690" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76689">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKsQ9KD0rZMlk9JVfVQPqbkxCdgJCalkMA1_bPrCz1uSrW96LZmsoHk8mEiUP493EV6j8b5NteFN79AseyOzp75l00vLDfDsyJom7heGyTPwmxiRLwJpFDn1nLrJ_I5rWl8vTuRLmXS4WDdiqz44R_tcerSfioWqgPsdv0fhKMatB8xZqHmBMF8Rs0ubpL4UkogD_z4T-aMuHv7WPZJxBMLCsmSfocJsQCG7hEPkE6Oq5Lm-7bECTnnWfzzJSD1kDqRGL1li_MBHGGIbzKPPiOQ9njI6jDEQ_K0zRWZxHZTYh0HZxr6GK_iesJidlTlSBZX3YG_w9_Xb3Eklh8e0KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرس تی‌وی، شبکه انگلیسی‌زبان صداوسیمای جمهوری اسلامی، روز جمعه خبر داد که میان ایران و ایالات متحده یک «کانال ارتباطی» در تنگه هرمز ایجاد شده تا از وقوع حوادثی که می‌تواند به تشدید تنش‌های نظامی منجر شود، جلوگیری کند.
این گزارش یک روز پس از آن است که جی‌دی ونس، معاون رئیس‌جمهور آمریکا، گفت واشینگتن و تهران قرار است این کانال ارتباطی را راه‌اندازی کنند و این اقدام را «دستاوردی مهم» خواند.
او در گفت‌وگو با وب‌سایت «آنهرد» گفت که ایران موافقت کرده تا یکی از نیروهای سپاه پاسداران را به دوحه، پایتخت قطر، بفرستد تا به گفته او «در کنار یکی از نمایندگان فرماندهی مرکزی ارتش آمریکا، سنتکام، مستقر شود» و از این طریق بخش زیادی از اختلافات حل و فصل شود..
شبکه پرس‌تی‌وی به نقل از یک منبع آگاه گفته است: «بر اساس بیانیه نهایی منتشرشده از سوی دو میانجی پس از مذاکرات هفته گذشته در زوریخ، این کانال ارتباطی با هدف جلوگیری از بروز حوادث در این آبراه راهبردی که ممکن است به درگیری نظامی منجر شود، و نیز برای اجرای مفاد ماده پنجم تفاهم‌نامه اسلام‌آباد ایجاد شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/76689" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76687">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HdRojgGXvoMXznSIItjbdAWYCk-82wc_MUdG97IFVz_831NCScKWuTJ5tG-g5kGO6gJdqoKTX8Sj6q2oR6P3BxzTutlafHj8pYv5sr3cSH1p0NgnyxnnU0goyVxdL5lheWNMKa3gysJO2dyRnT2WMtwuh6omn6xHRBlo_bno1dtb8W7MqSDR8EnauEIsD98T5DcpFc3hGqIdW4Q_kgUxmVfs40X84s3zmR7VrisZlziEhLv4YxTU01NrYK9G0TzzUW6Lh7IHYn8qeOadEy1rp7efMyRX3Ap8M6zzzFzjux4Sb8wdV76bbH1DM65A2-rHvgFLjNwLb1Aire8wBqmJYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b3pv-4EHwJa4UufgHle0SKZhANBXcgeCPM4R1NBmIetn1c3zZYM9hixhvs_QiAgNnOeb5BdCniMlyBsewzP2859HyiJudz9VVSFFUHAB1GUWSRN0n5ZqbbI67cbtKotnsSrFoClz4xZZtd04ob5nv5ocWkj06OZgYtmB7U5y5rJwKkzpWoKEALZ5te7PrROBJD8lMAg8ghtus9mZM5-39JIfMfczYOyaZZ2G5CUtWnxa5M4H9KCGy9GlIerW5jminHu92h8u37b8m86lteCbmvCJhCk3XewjXNIoA1cjNkClpXlGhB_6fWTCvBlbFUH3Dmg6zspbZQsGL-ERHt1wDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، می‌گوید عبور ایمن کشتی‌ها از تنگه هرمز بدون هماهنگی با حکومت ایران «قابل تضمین نیست» و هشدار داد که در صورت انجام نشدن این هماهنگی، ممکن است مسیرهای تعیین‌شده برای تردد کشتی‌ها به حالت تعلیق درآید.
این اظهارات یک روز پس از آن بیان می‌شود که سپاه پاسداران اعلام کرد عبور امن کشتی‌ها از تنگه هرمز تنها از مسیرهای مورد تأیید ایران امکان‌پذیر است و هر مسیر دیگری که بدون هماهنگی با تهران اعلام شود، از نظر جمهوری اسلامی «قابل قبول نیست» و یک «ریسک امنیتی» به شمار می‌آید.
عمان روز چهارشنبه اعلام کرده بود که با هماهنگی سازمان بین‌المللی دریانوردی، یک مسیر موقت برای تردد کشتی‌ها در تنگه هرمز تعیین شده و از کشتی‌ها خواسته بود تا اطلاع ثانوی از این مسیر استفاده کنند.
@
VahidHeadline
قرارگاه مرکزی خاتم‌الانبیاء، ستاد فرماندهی جنگ جمهوری اسلامی، روز جمعه پنجم تیرماه با انتشار بیانیه‌ای درباره پرواز هواپیماهای اسرائیلی در آسمان کشورهای همسایه ایران هشدار داد.
دربیانیه قرارگاه خاتم آمده است: «حضور و تحرک هواپیماهای نظامی اسرائیل در آسمان برخی کشورهای همسایه در مسیر ایران را اقدامی خطرناک و تهدیدی علیه جمهوری اسلامی می‌دانیم.»
قرارگاه خانم الانبیاء در این بیانیه با هشدار به دولت ایالات متحده نوشته است: «اگر آمریکا نتواند اسرائیل را مهار و کنترل کند، جمهوری اسلامی هیچ تهدیدی علیه خود را تحمل نخواهد کرد و پاسخ به این اقدامات را حق خود می‌داند.»
این بیانیه در حالی منتشر شده که طی روزهای اخیر تنش‌ میان جمهوری اسلامی ایران و اسرائیل بار دیگر به‌ویژه بر سر ادامه «اقدامات نظامی اسرائیل» افزایش یافته است و تهران اسرائیل را به نقض مکرر مفاد تفاهم‌نامه پایان جنگ متهم می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/VahidOnline/76687" target="_blank">📅 19:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76682">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B-01rOy8rXWIxjyVevwdtCWy_FzoECXl9G5bb08Bxs-z3HnsUDGpNTauEmiXXSio_ShlOWdoUVSxATIrtYtQBtWDUiDWx4k1ZVfuTSRK4Oj89M7PxO39M8GasP-XcWNFUTYmDqw3PUKuvg4eNk4EHJu6y2i43c0Fd0oDosSTaLW1Jxy731ggoH8Co4LZF6yk2T4rlzlidHiM7jwH86BoEeiTfRwiA-K_RnN_deXhqOxiSig-PqS7JAgb5MIkeeYxVegbmJhui_zMEqBwgW3NuEp2rUfOkjxOp-vmCtKxEg31YIuT-46FjlJgiv417jLD5bBc8vp3zC3N8reJqkiq5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vUmL5Pq75h8orb0AGe9dBoPr4_E69fkifiZnsLtLHut44ZQNUMDQ8PP6alhZ2HHY0e-JqjdlkE2N8MJw994VIsyN-REheVFp_n_gRxtDn-DXzRpuXp_ES2F94zETtD0y-ldP9zKFazrTb4Kve42UfQaTy2G_12tW57v5QkCz7rDcF099zNK9iYXPJEtfPBLYuCeaUsJhz9zfWXRjTEoq-Nfz_3T_rdKicNNNOyOZEArb2ZaX5CcSvqP7FhkC8-BkWUsgOf8Med0gdU0X7g_OfPpg8oWgygNVscFjQFgvL0qsNNCq_FoiBhPyavkYwmD2thSyTpuJ8wzem3ctmdUMcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QlNCAiRZjCDl5t1t5ZdaR0XJsNHZcrWFXufAeqfrHx8y0ok45uIk-PNCvgn5n5fou_nvr1tSx7LEBpIF3K5YcO5j0lncwqL6U-EQaoEuyFoCGo-amcfgfDx6cC_L6iT4XtJ6bmBaKF17dnEnRewSYR-3sjr7fEUvg11IL6_aE0PSUEAzQxP4Up5lt1evvuIs37BcTI9rPb637aK7b_SWzx6NlQ5DeymPkVOCrk-uS_98lIGZWOI77wY5Mtdv0UeaftKPxV-iRgNnOtJqq7MtqcHCuDdCrd8g4AQ7lS0fnbM7ybwDw7m5a4sENXxTd3kkti90iuAf6HkITT2vCppIIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PlAGvGAhpG8tAiwmMFsmO9y034oXTljkCRh9E2RWCmVE2B6dqWAGxnKQsT9gscrpphWvwfjrlmdgvGdlNY3KTiRgzdVROMMdQ7_5cCffVzTWZ9kdfWbw2uXQIb_1c-4gfQFdofrzmQScD7J7xWSSSSn-icg_KYqAeUOWdMxjBPxbtFv3GgqR4K29sF-qxJO2v2Le5i6OmCAdz24OcnZUGhLiLT77c37ELSrOcoT1j7p3EzIkfeYzgp3DoMb5w6IaMv-4ALL0HBHr9bpe5V3GQUsuM-qWRtfivNwm2I-GjmR9JcvXIBuQYDMUTtFPRA7Vo_quUpo0lKWl5dmiKbHyRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hAcF5_ZXkAktDcBFoiliRDWV6SamBTGyyX7kq5OtU4gFEVj8xZj9WuS9jOqGy7lMje31vnsLUTCQrnpDU9clyzc2h3QBWkIz67Rf-_DOg0SpYABkDRkD5XpY1O1W4Oj87eO8-d0OhI7pXApfoXAtI_70fef09k7R3x_FE4fJHqly2CEq5MNjcTSJjlsLeQczhPi61kKTrSf4BcKULd41tq2Rgz-x618cBJexclHN9bR69gCwKD9FrImyhHn7nsUyDRqw9eAkq90sbVdK1nQf31rpe5dMN_zq7CLDREJ6XWbPRWAkD-_0S130AZTsYu3JRf4hdIDmoDWJvdL6FQbTSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نعیم قاسم، رهبر حزب‌الله لبنان،در سخنرانی تلویزیونی خود در مراسم عاشورا گفت: «اسرائیل هیچ گزینه‌ای جز عقب‌نشینی کامل از هر وجب از خاک لبنان ما ندارد... اسرائیل باید بدون هیچ شرطی خارج شود.»
در حالی که مقام‌های لبنانی و اسرائیلی در واشنگتن مذاکرات مستقیم برگزار می‌کنند، آقای قاسم گفت گروه او «هیچ عادی‌سازی روابط، هیچ پایان دادن به وضعیت خصومت، هیچ دستاوردی برای اسرائیل و هیچ حضور جزئی در خاک لبنان را نمی‌پذیرد... اسرائیل باید با خواری و شکست خارج شود و این اتفاق خواهد افتاد.»
حزب‌الله لبنان مورد حمایت جمهوری اسلامی ایران است و تهران می گوید در تفاهم اخیر با آمریکا و مذاکرات جاری با این کشور، منافع این گروه را در نظر می‌گیرد.
به مناسبت عاشورا شیعیان لبنان تجمعی در شهر بیروت برگزار کردند و عکس‌هایی از رهبران جمهوری اسلامی ایران هم در این مراسم حمل شد.
@
VahidHeadline
یسرائیل کاتز، وزیر دفاع اسرائیل، در پیامی در شبکه اجتماعی ایکس، در واکنش به تهدیدهای اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران، نوشت: «اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.»
کاتز خطاب به قاآنی گفت: «به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحک تهدید به او می‌آید.»
کاتز افزود: «نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان. هیچ‌چیز ما را متوقف نخواهد کرد. نیروهای ما آماده‌اند تا کار را به پایان برسانند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/76682" target="_blank">📅 19:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76680">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gG7SSnnp3SM0dFo0EEXwBjiDhjZFv7FunKFaJM4zrVfzCpbnby2h6ISUOaqPVOF-8Il3L0iCbjRCUQVAUpc83wPVPVa0WOnHtulBIbihykZxNFAST3QjFcjse8X2pC0o7oK95WeH4bRUG01MAKADaGrjwYV320cr4pO936Lpi8fATeuQttFRj0bopJjA6k-AiAZa-RnqgPZ2MSPYycQ1GYdpb9h-CqILjgn91Vk59QHurII3QkOAvXDE7roGKqWgsRh9Da7DN_GRzSFv3vAtx3GwRIhkACkWJS63IhOAelUePOteZHm9QGFhFo16TxnP84lmPyNI8tulVlVSsVM-9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iagWkgq-kFR35jA2nExmngugIqOBSIeS9O6US5T4HQ1l8TCIjwwgn5h3gSBK13Ljzh-1h0nQNdC9Y2tqdKKS9-hSLTsiK-qoAlmAXxsoL3dVUCNLdTJnbEypJ1Zix52juh29LnGoNhaHU3J4nQ-cRUbOl2gtxuU9k78Mc801dtFz5l71ssunJquo6jYipC1xnld5WTPvMhOs6RaBsBdrh7eMJ4fOfcxR1Qy1VFpyrrkbSCNWN4IVDyCABFAmoOT6RwB7tBDS3GAkynkoItrUStqbYqEi41UauuqGqIjyObOYxCuniGg6VIkHdTnJYgvOSe2IfWBkQVhI-iN1UG2vBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در نشست وزیران خارجه شورای همکاری خلیج فارس با حضور مارکو روبیو، وزیر خارجه آمریکا، در بحرین، کشورهای عربی حاشیه خلیج فارس بار دیگر بر لزوم مهار تهدیدهای منتسب به جمهوری اسلامی تأکید کردند. در بیانیه پایانی این نشست آمده است که تحقق صلح و ثبات پایدار در منطقه بدون رسیدگی به موضوع برنامه موشک‌های بالستیک، پهپادها و حمایت تهران از گروه‌های نیابتی ممکن نیست.
@
VahidHeadline
وزارت خارجهٔ جمهوری اسلامی ایران با انتقاد از بیانیهٔ اخیر کشورهای عضو شورای همکاری خلیج فارس، آن را «مداخله‌جویانه، غیرمسئولانه و تحریک‌آمیز» خواند و نسبت به آن‌چه «ادامهٔ رفتارهای ستیزه‌جویانه و مداخله‌جویانه در منطقه» نامید، هشدار داد.
در بیانیه‌ وزارت خارجه که روز جمعه پنجم تیرماه منتشر شد، به کشورهای حاشیهٔ خلیج فارس توصیه شده که از همراهی با آمریکا در «تهدیدانگاری» برنامهٔ هسته‌ای ایران خودداری کنند.
این بیانیه همچنین بار دیگر مواضع پیشین مسئولان جمهوری اسلامی دربارهٔ قرار گرفتن تنگه هرمز «در محدودهٔ آب‌های سرزمینی» ایران و عمان را تکرار کرده و می‌گوید همین موضوع «مبنای عمل در رابطه با مدیریت کشتیرانی در این تنگه خواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/VahidOnline/76680" target="_blank">📅 19:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76679">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0UOa_dmKJ5U5MwPqftTaK31uc4CQU4Wtzdz6DuSweOamxmlJSLeYkLZvCEl-foxz-elzBYKXTdF6tiEiXkrmZiLlX8NYcrImMjvZA--HQ2uCPeAlCIhLTd8ff3bMQLxVlFAlVICo_D5yv4j7hW7vQXYpcj-KcprfevsqXoTHmzJzPMRHlKOMwmdCN7PIrJrSX1SJgZXQhJxt5CnRpiEfEZkjLmrDb8nk93Gq_X_KvQ4riPc_gSu81XSyJslVkA7w3KNGd7XgcP66IhsY8UbnJoLC7Qym4-QmMSXC3wOO86twHCeLDazALtSpObrPnaDjo78Hfx0qbm_HjUZ6BLyVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، گفته است که پس از جنگ خاورمیانه، برای اطمینان از اینکه ایران به سلاح هسته‌ای دست پیدا نکند، به یک نظام راستی‌آزمایی «بسیار قوی» نیاز است.
آقای گروسی در جمع خبرنگاران در ژاپن گفت: «فکر می‌کنم هدف این تفاهم اخیر [بین میان آمریکا و ایران] این است که اطمینان حاصل شود ایران به سمت توسعه سلاح هسته‌ای نخواهد رفت. دولت ایران هم به‌صراحت اعلام کرده که چنین قصدی ندارد.»
مدیرکل آژانس گفت «اما البته صرفِ اعلام نیت کافی نیست. ما باید هرچه زودتر که از نظر عملی امکان‌پذیر باشد، یک نظام راستی‌آزمایی بسیار قوی برقرار کنیم.»
ایران گفته است که توافق درباره نحوه بازرسی‌ها و حضور مجدد بازرسان آژانس در تاسیساتی که مورد حمله نظامی قرار گرفتند بخشی از مذاکرات جاری و توافق احتمالی نهایی با آمریکا خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/VahidOnline/76679" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76678">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8oGMk1Pms3MFQdjnPqUaM3uFTcKycwO-WK6z26P9Xj8wzAZ4onLbqjOBjr9MtoMU4yy-HlTZanL1WURTBwCQjj1jH8p61deWOGv6LqxwN7JiK_Bh9CqLg-5phpZZzrBY-mguGqnuhzrjkj6itIlM7n1aknQK03hbwGD4zaRhxgMVX4hKSL75S7Mqz5zwWhpmzQeYBQvWiyyp5OPMwhnACJfEAS5nDB9Hz4wgxIFJo5pdDLeEApLTfGCE-FyVqGd26iyPLq9XaovhGAXQzfSfv3aQHu_iEfDqHYFyNzPBwBHHEZma8ovSMOrcJrj4KcUeh7uUSrn2mMx_FjeaYA2vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر کانادا روز پنج‌شنبه گفت کشورش باید سفارتخانه‌های خود در ایران و ونزوئلا را بازگشایی کند.
به گفته مارک کارنی، فقدان حضور دیپلماتیک، توانایی اتاوا را برای کمک به کانادایی‌های خارج از کشور و واکنش به بحران‌های بشردوستانه، به‌رغم اختلافات عمیق با حکومت‌های ایران و ونزوئلا، را مختل می‌کند.
او در توضیح بیشتر گفت: «تعامل به معنای تأیید نیست. داشتن سفارت، داشتن خدمات کنسولی در یک کشور، به این معنی نیست که ما سیاست‌های آن کشور را تأیید می‌کنیم.»
او در عین حال گفت هنوز در این زمینه تصمیمی گرفته نشده، اما تأکید کرد که این شرایط «باید تغییر کند و حرکت به سمت این تصمیم، کاری است که باید انجام دهیم.»
روابط دیپلماتیک ایران و کانادا از سال ۲۰۱۲ میلادی قطع شده و سفارتخانه‌های دو کشور تعطیل هستند. استیون هارپر، نخست وزیر وقت کانادا در آن زمان جمهوری اسلامی را «مهم‌ترین تهدید برای صلح جهانی» خوانده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/VahidOnline/76678" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76677">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=U1j3woCntwx3Jcba3IZf1BC6nT__6nqHDk_1Pt-SNRCEEd0L8E4n3l4S5nd3acKC5jJX_eZpnk_e1GHxKl9Fj31pLfapyccBc8EXeyoBoBpRcGnCBE1dCnriv7g7RHslBimDDU0nN98zg8UERZMdwP9zyto1NLQ-KVXrbToG8w57SFats5ar2EP-THe4TcKYgqBFPbRLDUqFYp_d8zzHtyJ7fLmeD8qMtGk5JyTVLyg3Buzuqyh18QVsP9oLm-x8MaCV_nY5KOZK-jeWkq5O_EFbyYU4qmt9fJqVgE1HiOAoccDbXsyo8MsF2Jz1FDVputLcdmyUidyI_DOe4n-S_g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=U1j3woCntwx3Jcba3IZf1BC6nT__6nqHDk_1Pt-SNRCEEd0L8E4n3l4S5nd3acKC5jJX_eZpnk_e1GHxKl9Fj31pLfapyccBc8EXeyoBoBpRcGnCBE1dCnriv7g7RHslBimDDU0nN98zg8UERZMdwP9zyto1NLQ-KVXrbToG8w57SFats5ar2EP-THe4TcKYgqBFPbRLDUqFYp_d8zzHtyJ7fLmeD8qMtGk5JyTVLyg3Buzuqyh18QVsP9oLm-x8MaCV_nY5KOZK-jeWkq5O_EFbyYU4qmt9fJqVgE1HiOAoccDbXsyo8MsF2Jz1FDVputLcdmyUidyI_DOe4n-S_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودداری ساکنان آبدانان به عنوان یکی از محروم‌ترین مناطق ایران، از بردن این کیسه‌ها به منازل نمادِ «شرافت» و «شورش گرسنگانِ آزادی و نه تهی‌دستان» نام برده شده است.</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/76677" target="_blank">📅 18:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76673">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kimP1OX3i2dS0oh5kljm53dJE5RZK9prIN6GVarNOqnnsx9M51Z1f66FazLtzI1MZnKnALkNlylh2taDtJK3MZf-nAsgMxoQSa1F5U6krJ5Z_iiMi4XTd9MN6S4OheiuLkepsUSbcqA_dSCcCbfQUEQXymK0PgSwCy6JGxiRemI5sS6kKALTdkAgf689f20z3tOWdCf2worDzNU20CnPHG3bZOZYVjQFyVv2CAfXaYoDDwIZVGvuXWUQNzWbz5WSjFz9a80x4MEFfWSdb-SueRVJYW-0sNqf1NF3LNE0guQv-8kGXvyw6CIltxcDtVFbqtTx7L1pKs83sksXUUVl6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kdxEX9TGhu5zFYC-BjbWq0xJkeh6iemdro-qL2tlqX_yUf8OUaJyqJ-Mr8JzDHXUSBDkoTKiADOzllgIKrPN2lFvVWf4ltkgnHee7AGaJcDBlrZG64LRKSm7W6D-YpZBCDZII2d8zrcHIMIQcqQTkz6phz_FR1DMyPfCjmcta3KW61aRj8KE0zLEcoAsQyHCGw5KvGlavGv97y2qicZHOrPCV7I0txDI8_pbsUfRtjM23oG-xZv_OtL0MVtZm6pFTTOyhtvafzfmPjR1LisuhnWvA9cQLsuKWbJfYODSXkw30axVUfkx-lxXDH2zBPT1mR_-BIhiqNr2UeXGLgAFYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B-N5FJlbkA2twz8Pt7HiNJYJksGGSedDMoI6OTwO7V1_vwKQH3aKq5dSSbVJKH-n1uSLaUgOpSrkv4bF2whlU2XhcOv5fIbU1nrAdirviOzaHDCVaSAPI8ikWsElP2aeZujlbAXtGOoErgQkscr9W9PK7ev2YEOtc8tTsn6wS79J6aGZYx_dxOCFAqzU3S8dhNQcOVh0KGsVD4Y3Ex1jCoJ2x4yH4aI0StuNq23ToBT9U6hTZ_drqJP8VD4SCk_C1SpNk-PbAnQh0e7OCRwlEnzYCxCA1339jC4LtsqKK0D_QzaHsjHfizMT7UcPt3dmRFLqVWo81ymnxjkGwPbsbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RFLYuFC5VRtaLJFv1L_E5viCE68K6nFmaOOyd_MDCMTkHPBtgTaegXGPu_wP-F-E82HWKNHiAjskUW6X74RBxa7_HRV9HC4dfBqID-WsIcU42kgZXJOR3cgqNXkf6PZINyJWTMFLE3IjHvRUH4uOfWeac24vonDeUeCJcb8Mo1ISO0l9mSq3hoCrMYdk9TGMZg0DYgoa-esDKi7IY5fUgWl5bh3SF35QCSDjWzU6RMpt2gy6h09uUYuBQRG529jXxCbcEO5sHTPXiRGpX01tRYe8BzRrL7-yifvFWnJ5QK9wtPsKSxF_nKh38gSqMvIkJBGm_4eAB-SEbQkYLLgt8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی:
خود امارات الان مسیج زد که اشتباه سیستمی بوده
هشدار دبی اشتباه بوده
دبی ساعت ۵:۱۸ به مدت ۲ دقیقه آژیر زدن ولی گویا تست بوده
اره فکنم دستشون خورده
احتمالا تست پدافند بوده
الرت دبی اشتباه بوده الان مسیج اومد برامون
وحید جان دبی گفت آژیر قبلی رو نادیده بگیرید
🤣
دستشون اشتباه خورده بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/76673" target="_blank">📅 17:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76671">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KdA1hc7W90n2QE7stkCQGVEmAoNdGLjSdP8gaW9xbSkzZWkhfYvLuYpitKLvkDsbNDHIaJfcrd2P-k4aWjMjZhGXtvYUg8V5atZM6Yq3jS6HV2Qnsy5U6uD7VVyf_Nf4sZZLcmxmdXDL7S19L-c6u04B3TWr1R8REn8sCo2CJsHgCEo7chr-u393JaAfJE4eb34sWOJyxbc8Chm9iceN59WqAJ8j8-P_tOXBDMB3JGcLWq379wsDoEdR4GZ_tHF1BJPOsGkOLp3KCH0LMbsXWWbUWBScQBPu7G2IgiYKVJPKW4xTY1w1prVVKuh9ZTfw1-v2usdDV7bAmhK0m6Nl4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mvpxDbPvH1xI0giVX44_fUINHUkBOy7-NoYZkCqH73oja-Row_9Co5xIAVOsncY4Qps8sMxsfSHZpwGoVjimtwwVObCq2G0fuecaWJHhK7O4s6QW2_881_NoCAF9QUBWCRbi5u-QyK7nSXo0K2LTikhtsAOFIguWfkiDMPwlNdLf_pS5Zx6P9eDY1uanCQ4QjE9NDJ9GeVgqLC17NTUOEHWiPETZIUb4sLlrrmZCoPvyOiUnuy61IE7kJb6HkfWz-u2CX9PDw5uTAYjOpasdqmISTnnEaeym6muA6H-xSj11ehzBreIktHkdHviduJb8OvQKJeVNDMRVzv5olL6EGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی الان:
سلام وحید جان
الان دبی برای ما آلارم موشک اومد
سلام اقا وحید
همین الان باز اژیر زدن
نمیدونم کجای دبی رو زدند
وحید جان همبن الان دبی آلرت موشک دادن
ما امارات هستیم
هشدار حمله موشکی بهمون دادن
الان امارات دبی دوباره صدا آژیر اومد
🫠
البته خیلی کوتاه بود، و سریع گفتن اکیه
وحید جان همین الان توی دبی برای همه آلارم حمله موشکی اومد
منطقه جمیرا ۲، کایت بیچ ۲ بار صدای انفجار شدید از آسمون اومد
احتمالا رهگیری بوده
📡
@VahidOnline
آپدیت در پست بعدی</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76671" target="_blank">📅 16:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76670">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=KgQaj5e6PvmyM19jWq4-E0neP16mE-lCfNEV2XSM91fpwAP3713bSa3CnZejqcdofVc2HPTCO7iPRcIOwsBql84ix9A7QqGcim7g20Udg9S2qD03LzDNw-PhleDqJl6o8ou5P12iWB2CGQe-HgxkKWq4RiCv5jcf286SNVnRoeDR4bkNYCrlnd3SKiJtmRGGigVAGjcbiw0sr7bkVuk4m3y0GvFWkdcIw81ZbHIHcKnA-kkbGzbh_ixwnIxIrezWVX0JS4MN3SjMOrniDZ3RDj-fkTSwvbWaARecrzkDmCosE57iLsMwOHu83999hPMo5e6LmOO_B-8_xvznKrkHzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=KgQaj5e6PvmyM19jWq4-E0neP16mE-lCfNEV2XSM91fpwAP3713bSa3CnZejqcdofVc2HPTCO7iPRcIOwsBql84ix9A7QqGcim7g20Udg9S2qD03LzDNw-PhleDqJl6o8ou5P12iWB2CGQe-HgxkKWq4RiCv5jcf286SNVnRoeDR4bkNYCrlnd3SKiJtmRGGigVAGjcbiw0sr7bkVuk4m3y0GvFWkdcIw81ZbHIHcKnA-kkbGzbh_ixwnIxIrezWVX0JS4MN3SjMOrniDZ3RDj-fkTSwvbWaARecrzkDmCosE57iLsMwOHu83999hPMo5e6LmOO_B-8_xvznKrkHzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روز پیش از دیدار تیم‌های فوتبال ایران و مصر در مرحله گروهی جام جهانی ۲۰۲۶، فیفا روز پنجشنبه چهارم تیرماه اعلام کرد تماشاگران می‌توانند پرچم‌های رنگین‌کمان را به ورزشگاه محل برگزاری این مسابقه در سیاتل وارد کنند.
پیش‌تر، فدراسیون فوتبال ایران از فیفا خواسته بود از برگزاری هرگونه مراسم یا فعالیت تبلیغاتی مرتبط با گرایش جنسی و هویت جنسیتی در دیدار ایران و مصر جلوگیری کند. این درخواست پس از آن مطرح شد که کمیته محلی برگزاری جام جهانی در سیاتل این مسابقه را «بازی افتخار» (Pride Match) نام‌گذاری کرد چون هم‌زمان با «هفته افتخار» (Pride Week) برگزار می‌شود.
ایران و مصر پس از قرعه‌کشی با این عنوان مخالفت کرده بودند. همجنس‌گرایی در هر دو کشور جرم‌انگاری شده و قوانین کیفری برای آن وجود دارد.
فیفا در بیانیه‌ای اعلام کرد جام جهانی رویدادی فراگیر است و پرچم‌های رنگین‌کمان و دیگر نمادهای مرتبط با گرایش جنسی و هویت جنسیتی، به‌عنوان نمادهای حقوق بشر، اجازه ورود به ورزشگاه‌ها را دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76670" target="_blank">📅 06:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76669">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e3e8CKAvWSo4hXY8WVQwMeyzPqUtQZaSwCR0U5iLoTMbu1Nt9dYCa93Kno86SLEU_4Ajvgu7oTcIiM-Hyoz10PIxFLtHcO_iuTUkwnENTC47XhYC43Ot8qwTm-_G2f56AbUw14ZE9gzvW-kpv9R2XRxTbQlWEMfehJgoJdBjOLzppx3fT1DGNdfW2VlRjE4LDQ8Ri3Bt-Zjii13mgMnmgsONaIopnMLQqIk4cw9yxrXeEtzPKUire_q08nhl7m9jjb_lYzRLOYB6EIWtwJDttty7b77j3x7HwgPn30D63x1SoNJ9Uxj_3bEXDrUa3koSPQq8Jow57mpwSosEKw6jyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: یک مقام آمریکایی به CNN گفت یک کشتی باری در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛
اتفاقی که باعث شد سازمان بین‌المللی دریانوردی عملیات تخلیه خود را در تنگه و اطراف آن موقتاً متوقف کند.
ترجمه ماشین: یک مقام آمریکایی به CNN گفت یک کشتی باری روز پنج‌شنبه در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛ حمله‌ای که باعث توقف عملیات تخلیه هزاران دریانورد از کشتی‌هایی شد که از زمان آغاز جنگ در خلیج فارس گیر افتاده‌اند.
این مقام آمریکایی جزئیات بیشتری درباره این حمله ارائه نکرد. ایران مسئولیت آن را بر عهده نگرفته است.
سازمان عملیات تجارت دریایی بریتانیا روز پنج‌شنبه اعلام کرد که یک کشتی باری از سمت راست خود با یک پرتابه ناشناس مورد اصابت قرار گرفته و پل فرماندهی آن آسیب دیده است. بر اساس این اطلاعیه، ناخدای کشتی گزارش داده که هیچ تلفات جانی و هیچ پیامد زیست‌محیطی در پی نداشته است. مقام‌ها در حال بررسی هستند و به کشتی‌ها توصیه شده با احتیاط عبور کنند و هرگونه فعالیت مشکوک را گزارش دهند.
‏CNN برای دریافت نظر با کاخ سفید تماس گرفته است.
توقف عملیات تخلیه چند روز پس از آن صورت می‌گیرد که سازمان بین‌المللی دریانوردی (IMO) اعلام کرد توافقی میان ایالات متحده و ایران راه را برای تخلیه بیش از ۱۱ هزار دریانورد گرفتار در منطقه خلیج فارس باز کرده است.
آرسنیو دومینگز، دبیرکل IMO، در بیانیه‌ای گفت: «پس از آغاز طرح تخلیه IMO، که طی آن چندین کشتی تاکنون با موفقیت تخلیه شده‌اند، تصمیم گرفته‌ام اجرای آن را موقتاً متوقف کنم تا دوباره اطمینان حاصل شود که تضمین‌های ایمنی لازم همچنان برای کشتی‌های موجود در فهرست تخلیه ما و همه کشتی‌های حاضر در منطقه برقرار است.»
او گفت از حمله‌ای در روز پنج‌شنبه در دریای عمان به یک کشتی که از تنگه هرمز عبور کرده بود مطلع شده است و افزود که آن کشتی تحت چارچوب تخلیه IMO فعالیت نمی‌کرده است.
دومینگز گفت: «من همیشه تأکید کرده‌ام که ایمنی دریانوردان در اولویت مطلق است. بنابراین، برای تضمین رویکردی هماهنگ و ایمنی دریانوردی، طرح تخلیه تا زمان روشن شدن بیشتر موضوع متوقف خواهد شد.»
دومینگز یادآور شد که پنج‌شنبه «روز دریانورد» است و گفت این لحظه ضرورت اطمینان از ادامه تلاش‌ها برای تخلیه «هزاران دریانورد گرفتار در خلیج فارس» را برجسته می‌کند؛ بدون آنکه آن‌ها در معرض خطر تبدیل شدن به «قربانیان جانبی این درگیری ژئوپلیتیک» قرار بگیرند.
سازمان مدیریت راه‌های دریایی خلیج فارس ایران روز پنج‌شنبه اعلام کرد کشتی‌هایی که خارج از مسیرهای تعیین‌شده آن حرکت کنند، تضمینی برای عبور ایمن نخواهند داشت و مشمول بیمه یا مسئولیت‌های مرتبط نیز نخواهند شد. این سازمان در پستی در X افزود: «پیامدهای حرکت در مسیرهای غیرمجاز بر عهده مالک، بهره‌بردار و فرمانده کشتی خواهد بود.»
این تحول در حالی رخ داد که مارکو روبیو، وزیر خارجه آمریکا، در منطقه خلیج فارس حضور دارد تا توافق با ایران را به سه کشوری عرضه کند که احتمالاً از بزرگ‌ترین بدبینان آن خواهند بود.
هفته گذشته، ایالات متحده متن رسمی یادداشت تفاهمی را که در آخر هفته با ایران به دست آمده بود منتشر کرد.
یک مقام ارشد دولت آمریکا متن سند ۱۴ ماده‌ای را خواند؛ سندی که مفاد مربوط به بازگشایی تنگه هرمز، کاهش برخی محدودیت‌های مالی علیه ایران و انتظارات برای رسیدگی به برنامه هسته‌ای ایران در مذاکرات فنی آینده را تشریح می‌کند.
قیمت نفت آمریکا پس از جهشی که در پی تعطیلی تنگه هرمز به دلیل درگیری‌ها رخ داد، به پایین‌ترین سطح خود از آغاز جنگ ایران رسیده است.
cnn
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/76669" target="_blank">📅 03:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76667">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=qHs2T4MQ4a8xHBhX__E3Aai_VDpXn1mpDJmlRFzI5HB_U76qxyKLsoZADIuEcKjLTFJLzIaAYi7bfkI-4Fu2L7ylW0WKXk1FxH-XusuXpiBgAcJF0Mg4D-WhNwv9NwxtyP3G716XxYruljtDjblY-g53AIH0xbTuz0hyMlUqYc0iQYYyWyuwMgoFaxiSZHD9c1piXTr4N_befqODQXiqeUm43VXBW_0zFdcKAnKHdPoKowSbCPlCx1sacG_yGu70-w1CuZNlFnUH7x4UJv6KyshWPtoH28HKcy6T5N0kKdOQqGF5W9jGTAfIJJggg9QpaAA1S0oNfB-5lVS0_Uo7ww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=qHs2T4MQ4a8xHBhX__E3Aai_VDpXn1mpDJmlRFzI5HB_U76qxyKLsoZADIuEcKjLTFJLzIaAYi7bfkI-4Fu2L7ylW0WKXk1FxH-XusuXpiBgAcJF0Mg4D-WhNwv9NwxtyP3G716XxYruljtDjblY-g53AIH0xbTuz0hyMlUqYc0iQYYyWyuwMgoFaxiSZHD9c1piXTr4N_befqODQXiqeUm43VXBW_0zFdcKAnKHdPoKowSbCPlCx1sacG_yGu70-w1CuZNlFnUH7x4UJv6KyshWPtoH28HKcy6T5N0kKdOQqGF5W9jGTAfIJJggg9QpaAA1S0oNfB-5lVS0_Uo7ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل کاتس، وزیر دفاع اسرائیل، در مراسم فارغ‌التحصیلی افسران رزمی در پیامی هشدارآمیز به تهران گفت: «اگر ایران به دلیل فعالیت‌های اسرائیل در لبنان یا به هر دلیل دیگری به اسرائیل حمله کند، با تمام قدرت به آن ضربه خواهیم زد؛ به‌گونه‌ای که برتری قدرت ما را به‌روشنی نشان دهد.»
همزمان، بنیامین نتانیاهو نخست‌وزیر اسرائیل، تأکید کرد، حضور نظامی اسرائیل در مناطق امنیتی جنوب لبنان، سوریه و نوار غزه ادامه خواهد یافت و زمان‌بندی مشخصی برای پایان آن در نظر گرفته نشده است.
این در حالی است که جمهوری اسلامی ایران در جریان مذاکرات اخیر  بر ضرورت جلوگیری از گسترش درگیری‌های اسرائیل در لبنان و خروج نیروهای این کشور از خاک لبنان تأکید کرده است.
همچنین برخی مقام‌های لبنانی و جریان‌های سیاسی منتقد حزب‌الله، تهران را به دخالت در امور داخلی لبنان و تأثیرگذاری بر تصمیم‌های سیاسی و امنیتی این کشور متهم می‌کنند.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روزپنجشنبه چهارم تیرماه  در مراسم فارغ‌التحصیلی افسران نظامی در جنوب این کشور تأکید کرد که نیروهای اسرائیلی «تا هر زمان که لازم باشد» در منطقه امنیتی جنوب لبنان باقی خواهند ماند و قصدی برای عقب‌نشینی ندارند.
او همچنین با اشاره به فشارهای بین‌المللی، از جمله توقف ارسال مهمات در جریان جنگ، گفت اسرائیل در صورت لزوم «حتی با حداقل امکانات» به جنگ ادامه خواهد داد.
نتانیاهو در ادامه با اشاره به ایران گفت: «با توافق یا بدون توافق، تا زمانی که نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76667" target="_blank">📅 22:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76666">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtMwVRgf-SKgl6UOfSH0D3FwrgePV9xO_TmiC6W_UMVhrxvAFiFF2NYMShL1t-sl8ehdrWVgr4F5X2jX-nnw_W7lDQqdi-Gbh5qnXdcP7OS6EKLDcgPZHb3QoeE5ym7nkWdbJuuE1MY-VeKTUCj2YVZ6k61j-QJeMiY-vrb3A5En6eM8P5xliethcsM39OihkEgCE5raZWOzNi4ySz5Vk30jbWoOxNd_EDNpA6roq4ZloGi0SqI1F2uutR_wtb560Xv8UkXweAITJY1It1ZkBNK0WenhY_An9a6ifdWbpu1R1JQ0Xue9lR66BYLSS7E9vcTRjsLaeYl8Ig9Zz9jcDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی خبرهای منتشر شده در برخی رسانه‌ها و شبکه‌های اجتماعی در خصوص ممنوعیت شعار دادن علیه آمریکا و آتش‌زدن پرچم این کشور پس از امضای تفاهم‌نامه را «جعلی» خواند.
میزان نوشت که ریشه این خبر در «سرویس دشمن و در راستای عملیات روانی دشمن» است و تاکید کرده که انجام چنین کاری جرم‌ نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76666" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76665">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j7vcE9OGsGx8HeS483NQIehPGujE4cJyq5O_7TysNHAruj7vbgXRgo5hHrKdie1HaMjQe6SCYowEcEaWQNxps4VlfEM8YFRMQVXMGRvU0OwuSofg3IVVMunbPXgguflXbl1VLSYeieib8lJLxT46IJ_2qrXpyJG4nguIt0OXr01oGNlJJceM7nP44feG6wNPykbFJbz1tScJ03v4OzqegQCk264Yx5cB95iIphIz-VWMcsfL4NPwjKkD2CHXlxXPVxtZsYHnaLA0uvzCIkwodnjusvEZVLa1Ym2nRddQMT2turyOyDl6x2saTX_IkkZBshoiic9WFhY9g_axWz6qpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، گفت یکی از مهم‌ترین دستاوردهای مذاکرات سوئیس، توافق اولیه برای ایجاد یک کانال ارتباطی مستقیم نظامی میان آمریکا و جمهوری اسلامی با هدف جلوگیری از تشدید تنش‌های آینده بوده است.
او افزود: «یکی از چیزهایی که می‌خواستیم از این مذاکرات به دست بیاوریم، ایجاد یک کانال ارتباطی در طرف ایرانی برای کاهش تنش بود.»
ونس گفت طرف ایرانی با این پیشنهاد موافقت کرده و گفته است: «بسیار خب، ما یک نفر از سپاه پاسداران را به دوحه می‌فرستیم تا کنار یک نفر از سنتکام مستقر شود و از این طریق بسیاری از اختلاف‌ها را حل‌وفصل کنیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76665" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76664">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O05f10guNXkrFpUuL0wmnwC3qg2aCRqO3hS33hXqAT1sFEzDqhLyT4ClCkqO-C3dD9x2nfffoBnD2gZxG27kvlT6ZZ4eTYTXeWT0c6LnqAqG6SkSI0hl9qgMuGeDWPYB-oqz8UGx6QJ2X-z3aE02lXlORXCc8IlGH2kfM5S6PghKcxiNvxTWqLgoqUuAjPGzHuo_sWRa_OiswV3hz6pzGeEeqHoS0XqHLVF_iJRFWg_xB28V_PV9xIdDb4GLeuakUJiQ--Uj3DmXcJlIGoUFIb1G6xfFI9Ght2M1r8T4O0DrzEZUuIXL643nrapoSCFpfyaHkDQJ8qL6dVJFAe3evg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد ایران، روز پنج‌شنبه گفت اظهارنظر مقام‌های ارشد ایالات متحده مبنی بر اینکه ایران دارایی‌های آزادشده خود را برای خرید محصولات کشاورزی آمریکایی هزینه خواهد کرد، «ادعای دروغ» است.
او در شبکه ایکس خطاب به مقام‌های آمریکایی نوشت: «تنها محصولی که ما برداشت می‌کنیم، همان چیزی است که شما سال‌ها پیش کاشته‌اید: دهه‌ها بی‌اعتمادی!»
این در حالی است که بعد از اظهارنظر دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره این که ایران با بخش عمده دارایی‌های آزاد شده خود محصولات آمریکایی خواهد خرید، اسکات بسنت، وزیر خزانه‌داری آمریکا نیز روز چهارشنبه تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای «خرید مواد غذایی و دارویی از آمریکا» استفاده خواهد شد.
پیش‌تر عبدالناصر همتی،‌ رئیس‌کل بانک مرکزی ایران، نیز گفته بود که براساس یادداشت‌های امضا شده بین دو کشور هیچ الزامی برای خرید نهاده‌های کشاورزی از آمریکا وجود ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/76664" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76663">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">(
⚠️
۲۰ دقیقه، ۳۰ مگابایت، با زیرنویس فارسی)
مارکو روبیو، وزیر خارجه آمریکا، پس از نشست وزیران خارجه کشورهای عربی حوزه خلیج فارس در بحرین گفت هیچ‌یک از این کشورها از دریافت عوارض برای عبور کشتی‌ها از تنگه هرمز حمایت نمی‌کنند.
او افزود کشورهای عربی خواستار اطلاع از همه مراحل مذاکرات با ایران هستند و آمریکا نیز مایل است آنها در روند مذاکرات مشارکت داشته باشند.
روبیو تأکید کرد تهدید یا مسدود کردن تنگه هرمز از سوی ایران «مشکل‌ساز» خواهد بود و گفت: «هیچ کشوری در جهان از پرداخت پول برای عبور از تنگه‌ها حمایت نمی‌کند.»
عمان نیز روز پنج‌شنبه تأکید کرد که هیچ‌گونه عوارض ترانزیتی در تنگه هرمز اعمال نخواهد شد.
این اظهارات در حالی بیان شده که مقام‌های جمهوری اسلامی بارها گفته‌اند در حال مذاکره با عمان برای اعمال یک سازوکار نظارتی و دریافت عوارض برای عبور از تنگه هرمز هستند.
@
VahidHeadline
ویدیوی بالا درباره بخش‌های مرتبط با ایرانه و گزارش چت‌جی‌پی‌تی ازش:
https://telegra.ph/Rubio-06-25-4
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/76663" target="_blank">📅 18:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76662">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvyCZfKbWwy4SgPsLUv850Xc2MzHLHIhy1uq3mvK64pPrfyHl_fx6lD3WM9difZd0b1ZNWNg3LEYgish2xuxbo3ZiQjUPnyHrGqEu9U4ycXIoGsfaYXoYBeE95zMVeKi301PkKOy-4a8sXItNRuQS2WJ-5mm3Zzd7RPrHlOcZh8oMA_SL-qVJazPiszlG5glFvIoApe8Mg2VnY14Fs2Kbw5QUrl9GkUVn24IcXeas1FrCUgvozV76d3EISNinNykUsc3PwCoaBniImLZwu-ANSZuaTDBSJu2CN03ehRKzbOQE38oH2WsNY7zYrTxdcegXV_XWtSPIGX3rn4-NULNug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
بنیاد عبدالرحمن برومند دست‌کم ۸۰۶ مورد اعدام را از آغاز سال ۲۰۲۶ در ایران مستند کرده است.
‏
🔸
روند اجرای اعدام‌ها در ایران حتی پس از برقراری آتش‌بس میان ایران، ایالات متحده و اسرائیل شتاب گرفته است. به طوری تعداد اعدام‌های ثبت شده از دستکم ۷۴ مورد در ماه گذشته به ۱۰۳ مورد، تنها در ۲۳ روز نخست ماه جاری رسیده است.
‏
🔸
بسیاری از افرادی که اعدام شدند، در پی دادرسی‌هایی نامشروع، شتاب‌زده و فاقد شفافیت به اعدام محکوم شده بودند. متهمان به‌طور معمول از حقوق دادرسی عادلانه، از جمله حق برخورداری از محاکمه منصفانه و دسترسی به وکیل منتخب خود، محروم بودند و بسیاری از آنان به‌صورت مخفیانه و بدون اطلاع‌رسانی به خانواده‌هایشان اعدام شدند.
‏⁧
#نه_به_اعدام
⁩
@IranRights</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/76662" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76661">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سپیده قلیان:
تا نت خوبه براتون بگم که اوضاع زندان سپیدار اهواز از دی‌ماه ۱۴۰۴ تا امروز برای معترضین خیلی بدتر از چیزیه که خودم تجربه کردم.
در دی‌ماه تا امروز، بازداشتی‌ها رو توی نمازخونهٔ زندان نگهداری می‌کردن/ می‌کنن. هیچ حقی برای ملاقات، هواخوری، وسایل گرمایشی یا سرمایشی نداشتن، و حتی دسترسی به توالت بیشتر از سه بار در طول روز نداشتن. گزارش بچه‌ها نشون می‌ده که خیلی‌هاشون آثار ضرب و جرح شدید داشتن. حتی نحوهٔ جلب‌شون هم عجیب بوده؛ مثلاً یکی از بازداشتی‌ها رو بعد از دستگیری با موتور بردن زندان و تحویل دادن.
همون‌طور که می‌دونید، زندان اهواز کانون اصلاح و تربیت برای دخترای زیر ۱۸ سال نداره، برای همین کودکان هم کنار بزرگسالان نگهداری می‌شن. زندانی‌ها آب آشامیدنی کافی و غذای مناسب نداشتن.
الان هم بازداشتی‌های جدید در زندان سپیدار در شرایط مشابهی هستن. این جداسازی که سازمان زندان‌ها از دی‌ماه انجام داده، اصلاً تفکیک جرائم نیست؛ فقط شکلی از کنترل بیشتر و آزار و شکنجهٔ سیستماتیک است. زندانی‌های سیاسی رو به بدترین شکل از بقیه جدا کردن، توی جایی بدون نور طبیعی، بدون آب خوردن کافی، بدون دسترسی ۲۴ ساعته به توالت و حمام. حتی نداشتن این امکانات پایه رو به عنوان بخشی از شکنجه اعمال می‌کنن.
#زندان_سپیدار_اهواز
sepideqoliyan
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76661" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76660">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P8jiBGB9tjs0oqOzleymX5gj2JnKpy5lszhANuYq-8JYorYwg0LTzuGZfekkLFzYtjMZ_pN4Mxud6hg0EPH_4xHVWkkAQ4Taihv38X2kDRUOI_VFFLtOpE_DGLTZEcySJh69nsTfWJQ3Gj7sRGNv1zAQe7W45orcMv2P3yS6JVboaFL_6aCFUHznlbvm4OqMsE-pC1WMKuBXBQQ-QhRMQSft1gRbd0YjC6hUce-NKfVNzLT9vC0RCy_PrCb7dIzGqS6_AItBEwbZdmFPiMRoCr1uVsNCAVfsEWpzv3vuuE1cawqH8SUzQPn0oYqMlophe3SsqmMp4jgp90veAh04Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد.
ترامپ، پس از تغییر نتیجه رای‌گیری در سنای آمریکا درباره قطعنامه اختیارات جنگی ایران، از چند سناتور جمهوری‌خواه قدردانی کرد.
پست ترامپ، ترجمه ماشین:
وای! سنا همین حالا رأی خود درباره ایران را از ۵۰ به ۴۸ علیه، به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر موضع دادند.
از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه تشکر می‌کنم.
این رأی به ایران هشدار می‌دهد!
رئیس‌جمهور DJT
realDonaldTrump
سنای آمریکا با ۵۰ رای مخالف، ۴۷ رای موافق و یک رای ممتنع، با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد. این قطعنامه از سوی تیم کین، سناتور دموکرات، ارائه شده بود.
با شکست این رای‌گیری رویه‌ای، بررسی «قطعنامه اختیارات جنگی ایران» عملا متوقف شد.
جمهوری‌خواهان و دونالد ترامپ استدلال کرده بودند تصویب این قطعنامه می‌تواند اهرم فشار آمریکا در مذاکرات جاری با جمهوری اسلامی را تضعیف کند.
رند پال، سناتور جمهوری‌خواه آمریکا، اعلام کرد در رای‌گیری درباره قطعنامه اختیارات جنگی مربوط به ایران، رای «ممتنع» خواهد داد.
او گفت به نظر می‌رسد درگیری‌ها پایان یافته و دونالد ترامپ از او خواسته است تاثیر این رای بر روند مذاکرات را در نظر بگیرد.
رند پال افزود: «رای ممتنع من راهی است برای اینکه به رییس‌جمهوری فضای بیشتر و اهرم قوی‌تری برای مذاکره به منظور دستیابی به صلحی پایدار بدهم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76660" target="_blank">📅 07:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76659">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2898920f34.mp4?token=pkyNxO9ERyaJriF4BpDM9SQGD8OKWQGoa6bHWg2tydn7J53HI5zLHfj8IZXxP4o0ng9ZWGGN4KPfAdfRUwa6_xzCT2A16TuR4uL2ZhfSAzHJJCRnnMaYSf7O-e5lmR9pLesbw4yorBWqct3dLA6EKwwSCcQdb4rJ-kB3GhHqJ0y1vjF_uGINQHw86ilLoL8UZL2M1RUYWUzLKtSAGNx1cHZmlsrHBiKFGmuWJttetUeE4cKULmu_HMd8yVViOyMgTQKgEuHx1rbXK-NdpOs-64Ic_ljR1PCBN-XklxvSOawI-qoeVIqnNLrWYTZQUK_1Dn8R6ojOKzKqGc1rTROPfg7dcfOCH2iiHgiivWgph1Bhm-KAz_aPgVlc1_KwSBGpFqCWD3PfWQNODaEaN0xEB6r67IfUq56A3BA16D6i_9ygNjXnO1FlAAuShBf19kHIIP46eGFwpI3J_L-OBKnZyhzJ4zAjQj6UC_VKLWudQ8dH_hVmfkwUpCnZynUgb4o9FjD9LuCiJdpRpe-tWGRZnyi5MdPB_6Nah0IucdXcoB_ecqHU9yyhyRtyx_q4r4Zy0ocEu1QspKz3qJm_ztWNtRN6zB8Zk73qPXJ9TDE5lkLtOi7rKs5FT-odV53m1xX3DT0iwccRplKFhVNGjNjOPOpGF89TktxqB4VB1fKsMNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2898920f34.mp4?token=pkyNxO9ERyaJriF4BpDM9SQGD8OKWQGoa6bHWg2tydn7J53HI5zLHfj8IZXxP4o0ng9ZWGGN4KPfAdfRUwa6_xzCT2A16TuR4uL2ZhfSAzHJJCRnnMaYSf7O-e5lmR9pLesbw4yorBWqct3dLA6EKwwSCcQdb4rJ-kB3GhHqJ0y1vjF_uGINQHw86ilLoL8UZL2M1RUYWUzLKtSAGNx1cHZmlsrHBiKFGmuWJttetUeE4cKULmu_HMd8yVViOyMgTQKgEuHx1rbXK-NdpOs-64Ic_ljR1PCBN-XklxvSOawI-qoeVIqnNLrWYTZQUK_1Dn8R6ojOKzKqGc1rTROPfg7dcfOCH2iiHgiivWgph1Bhm-KAz_aPgVlc1_KwSBGpFqCWD3PfWQNODaEaN0xEB6r67IfUq56A3BA16D6i_9ygNjXnO1FlAAuShBf19kHIIP46eGFwpI3J_L-OBKnZyhzJ4zAjQj6UC_VKLWudQ8dH_hVmfkwUpCnZynUgb4o9FjD9LuCiJdpRpe-tWGRZnyi5MdPB_6Nah0IucdXcoB_ecqHU9yyhyRtyx_q4r4Zy0ocEu1QspKz3qJm_ztWNtRN6zB8Zk73qPXJ9TDE5lkLtOi7rKs5FT-odV53m1xX3DT0iwccRplKFhVNGjNjOPOpGF89TktxqB4VB1fKsMNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری ترامپ و دبیر کل ناتو
در بازه‌های زمانی مختلف از این جلسه ۴۵ دقیقه‌ای، در مجموع حدود ۵ دقیقه درباره مسائل مرتبط با ایران حرف زده شده، به تشخیص ماشین البته:
مارک روته، دبیر کل ناتو:
اول از همه، درباره ایران. واقعاً می‌خواهم روشن کنم کاری که شما درباره ایران انجام می‌دهید چقدر مهم است.
این، پیش از هر چیز، درباره توان هسته‌ای است؛ توانی که ایران عملاً در آستانه دستیابی به آن بود. و این می‌توانست تهدیدی برای منطقه باشد. می‌توانست تهدیدی برای کل جهان باشد. این کشوری است که هرج‌ومرج صادر می‌کند. تروریسم صادر می‌کند. و آن‌ها خیلی نزدیک بودند به اینکه به توان هسته‌ای دست پیدا کنند.
هفته گذشته در گروه هفت دیدید که همه رهبران گروه هفت از این واقعیت استقبال کردند که این توان هسته‌ای تضعیف شده است. این فوق‌العاده مهم است.
و فقط می‌خواهم این را روشن کنم، چون گاهی می‌پرسند اصلاً همه این ماجرای ایران برای چه بود؟ این درباره امنیت و ایمنی است. این یعنی رهبر جهان آزاد مسئولیتی را فراتر از سواحل ایالات متحده، برای بقیه جهان، بر عهده می‌گیرد. و این همان کاری است که شما انجام دادید.
می‌دانم بحث‌هایی بوده درباره اینکه آیا متحدان اروپایی‌تان به اندازه کافی کنار شما بودند یا نه. فقط می‌خواهم یک چیز بگویم؛ می‌دانم شما چنین فکری دارید، و ناراحتی شما را از این موضوع می‌دانم.
اما وقتی به اعداد نگاه می‌کنید، چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های اروپا برخاستند؛ در شش هفته‌ای که این جنگ جریان داشت، تا زمانی که آتش‌بس در میانه آوریل برقرار شد. بخارست، فرودگاه رومانی، مجبور شد به روی پروازهای تجاری بسته شود، چون باید مطمئن می‌شدند که شما بتوانید هواپیماهای سوخت‌رسان را در هوا نگه دارید.
پس این ماجرا بزرگ بود. می‌دانم موارد پراکنده‌ای بوده که واقعاً از آن‌ها ناامید شده‌اید. اما به‌طور کلی، متحدان اروپایی شما در کنار شما بوده‌اند. واقعاً می‌خواهم این نکته را بگویم: چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های هوایی اروپا برخاستند.
خبرنگار:
پیام شما به دوست بزرگتان، اردوغان، و مردم ترکیه چیست؟
ترامپ:
من او [اردوغان] را دوست دارم؛ او دوست من است. او وارد جنگ نشد. او یکی از گزینه‌های اصلی برای ورود به جنگ با ایران بود. شاید هم در طرف ایران، چون همان‌طور که می‌دانید طرفدار جدی اسرائیل نیست. و من از او خواستم وارد نشود؛ او هم وارد نشد.
2:11
خبرنگار:
می‌توانم یک سؤال دیگر بپرسم؟ آیا گزارش مربوط به حمله به مدرسه میناب را دیده‌اید، آقا؟ می‌توانید به ما بگویید؟
ترامپ:
نه، آن را ندیده‌ام.
خبرنگار:
چرا نه؟
ترامپ:
خب، باید صبر کنم تا کامل شود. نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند. یعنی می‌توانید حرفم را بشنوید، اما نمی‌دانم اصلاً بتوانند— آن‌ها خواهند گفت یکی از موشک‌های ما بوده.
پیت، نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند؛ از نظر اینکه تقصیر چه کسی بود. چون موشک‌ها از همه طرف در هوا بودند. ببینید، شما انتظار نداشتید— و آنچه رخ داد وحشتناک است. اما موشک‌ها از همه طرف در هوا بودند.
و کسی گفته این موشک ما بوده؟ خب، شاید موشک ما نبوده باشد. اما من چیزی ندیده‌ام که مرا به این نتیجه برساند. موشک‌های زیادی هم از سوی طرف‌های دیگر شلیک می‌شد. پیت، نظر تو چیست؟
پیت:
خب، آقای رئیس‌جمهور، ما این تحقیق را بسیار جدی گرفته‌ایم. و وقتی زمان مناسب برسد، هر نتیجه‌ای که به دست آمده باشد، همان زمان برای اعلامش خواهد بود.
ترامپ:
منظورم این است، اگر به پاسخ درست برسید، فکر نمی‌کنم کار ما بوده باشد. فکر نمی‌کنم ما بوده باشیم. موشک‌های زیادی به سوی آن‌ها شلیک می‌شد.
خبرنگار:
آیا جلوی توافق نهایی ایران را می‌گیرید، اگر شامل هر نوع هزینه‌ای برای کشتیرانی باشد یا [نامفهوم]؟
ترامپ:
بله، برای من غیرقابل قبول خواهد بود. چون تنگه‌های متعددی داریم و اگر برای آن‌ها چنین کاری بکنید، باید برای دیگران هم بکنید. تنگه‌های دیگری هم هست؛ آنجا هم اجازه چنین چیزی را نمی‌دهم. بله، این قواعد بازی را عوض می‌کند.
خبرنگار:
آقای رئیس‌جمهور، فکر می‌کنم رأی کنگره برای پایان دادن به جنگ با ایران، حتی به شکل غیرالزام‌آور، تا حدی بر مذاکرات با ایران اثر می‌گذارد.
ترامپ:
ما در مذاکراتمان با ایران عالی پیش می‌رویم. درست وسط یکی از مسائل کلیدی، که در هر صورت به آن خواهیم رسید، خبر فوری داریم: سنا رأی داده که دوست دارد ترامپ جنگ را متوقف کند. ایران این را می‌بیند و می‌گوید: «این دیگر چیست؟»
حالا، می‌دانید که این بی‌معنی است، درست است؟ اما تعدادشان برای من کمتر بود. چهار سناتور جمهوری‌خواه داشتیم و همه دموکرات‌ها.
دموکرات‌ها می‌خواهند جنگ را ببازند، چون احمق‌اند. برای همین به آن‌ها «داموکرات» می‌گوییم. آن‌ها کودن‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76659" target="_blank">📅 01:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76658">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gc-5YclKj42T9UWVc8Ss-7nryC8faVhru6_ZiyEJt56vUhEGzGz9XrPKCXC9i0COliNGv67c6oyZq5Mm0mhJ2rW-91JkPYlTflUMfE1Gl-l5aedegSbsGJUeNikYYH-0kksMduXTDFjLt3I1pZz6ornVVJqoZ8JdS2isfGQXLUilUtOJSf3Fy76PiT2_jtPAyUNRDfDvDjUb9RdLpQX-0ZP3RhA8zIrWOWa60y6m0p4bWMZvHmih_4GMgPsnil1edatCE2OOYzD-ApFEFTEWIqvkRK2Zigrtqz_mohtu5Q_8CQ8OPw7SqYfk0eKnr9IOuxr6z7SeOUF-A4LiadG5Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رویترز دولت دونالد ترامپ، رئیس‌جمهور آمریکا، قصد دارد طرح فروش ده‌ها موتور جت به ارزش صدها میلیون دلار به ترکیه را پیش ببرد.
چهار منبع آگاه به رویترز گفتند که این کار با وجود مخالفت‌ کنگره صورت می‌گیرد. خرید این موتورهای جت تحولی مهم برای آنکارا پیش از نشست ناتو در ماه آینده است.
این موتورها که تولید جنرال الکتریک هستند، نیروی محرکه قاآن، اولین هواپیمای جنگنده ترکیه، را تأمین خواهند کرد.
ترکیه به عنوان عضو ناتو این پروژه بزرگ را در سال ۲۰۱۶ برای خودکفایی دفاعی بیشتر آغاز کرد.
یکی از این منابع گفته است که این قرارداد بیش از ۷۰۰ میلیون دلار ارزش خواهد داشت و قرار است ظرف چند روز آینده نهایی شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76658" target="_blank">📅 22:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76657">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89b252a095.mp4?token=dxtl91Bs8x0p1uuZrIFWbEzhQp_jPNwzwxua2AVXbIUPxcuy76BvKi0Ycm1U-2-ORuU8zHfFUhEYhjZg_Hta5GTWpw2iCK1LgGYk8jMKFi7crV4BRrijzSuk1ItzNSC0RlmnD1DGjMxLc5wuEzP_LneVIA61sMAV3ujyVgGqSA7enyXxGsndx0y2DoMTxuWBNsG2uNHKa5j-2rHuv-IFiCiFSnhmrBb_AB2osDpeRNm3OjjkFo4_Ez3pTaysIOA6ZdBotvANc4TqX5aOcllyaWFqeXJ9cOwiGlm-azrZkEYjke2HF-SPLQaXKvX2LRG27aAXZ96LJwrbB0Dy8v_MhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89b252a095.mp4?token=dxtl91Bs8x0p1uuZrIFWbEzhQp_jPNwzwxua2AVXbIUPxcuy76BvKi0Ycm1U-2-ORuU8zHfFUhEYhjZg_Hta5GTWpw2iCK1LgGYk8jMKFi7crV4BRrijzSuk1ItzNSC0RlmnD1DGjMxLc5wuEzP_LneVIA61sMAV3ujyVgGqSA7enyXxGsndx0y2DoMTxuWBNsG2uNHKa5j-2rHuv-IFiCiFSnhmrBb_AB2osDpeRNm3OjjkFo4_Ez3pTaysIOA6ZdBotvANc4TqX5aOcllyaWFqeXJ9cOwiGlm-azrZkEYjke2HF-SPLQaXKvX2LRG27aAXZ96LJwrbB0Dy8v_MhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا:
«هر زمان که وارد یک مذاکره می‌شوید، با یک روند بده‌بستان و امتیازگیری متقابل روبه‌رو هستید. این یک اقدام موقتی است؛ فقط برای ۶۰ روز در نظر گرفته شده است.
در نتیجه آن، ما انتظار داریم آن‌ها به تعهداتی که در سوئیس پذیرفته‌اند عمل کنند. اگر به آن تعهدات پایبند نباشند، رئیس‌جمهور گزینه‌های زیادی در اختیار دارد.»
USABehFarsi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76657" target="_blank">📅 22:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76656">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=pJB9Wz_zWwOlM3faB-Tk4nRGNgrYvbPQiy8Z1XxHxPX27NcKorWNiaqZkkOwKCGVTmogquZzg2W4_Azm7DDftmCpdoZjOb3GeBizPVu-XYVoz9QgvO_0nGSul3jZDD2Bmb1MO12zZq539s3xVCeLxmWVtVlDPnzCz3xkoCTpczod-u_jrBOw0NJt-dznXO0NXoU7o22IBMp1Slao8K5XA48CIbVLkgmRtWD9cMwRTTPMiZ-I3hUkYzsPHVZDJoiTQQiPIIrRD1YOxx3DDX8b0NFgjKU1FFPGoLCpYHXjgdCk6G_arIoV92jqn5tGbBY30nM1FlPiqK1WkkqFg3SVGw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=pJB9Wz_zWwOlM3faB-Tk4nRGNgrYvbPQiy8Z1XxHxPX27NcKorWNiaqZkkOwKCGVTmogquZzg2W4_Azm7DDftmCpdoZjOb3GeBizPVu-XYVoz9QgvO_0nGSul3jZDD2Bmb1MO12zZq539s3xVCeLxmWVtVlDPnzCz3xkoCTpczod-u_jrBOw0NJt-dznXO0NXoU7o22IBMp1Slao8K5XA48CIbVLkgmRtWD9cMwRTTPMiZ-I3hUkYzsPHVZDJoiTQQiPIIrRD1YOxx3DDX8b0NFgjKU1FFPGoLCpYHXjgdCk6G_arIoV92jqn5tGbBY30nM1FlPiqK1WkkqFg3SVGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه آزادی ملیکا ملک‌محمدی
این نویسنده و دستیار کارگردان تئاتر نیمه‌شب ۲۵ دی ١۴٠۴ در پی اعتراضات مردمی، با یورش خشونت‌بار ماموران امنیتی به منزلش در تهران بازداشت شده بود.
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76656" target="_blank">📅 21:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76655">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=EPIPdjHNeVpsElkyIsKByEyQkWW8yIySQMR3UKNBUQKIFQ5D7QN07oXryucXj5z71Moze7yTYsdbkEx9Gv_WM9xI-qWSnc_SthZJy1-LS9gQs-wV10AIkuu2Qiza_9QL07nKXkY1_BeIsFvPsoVOYXNvzWsWmxJHrLGKndqCmNUWTP8HfXZuRMCin74WdOMUhwnEFFjPo7L8IOU7WwdMhO-rxcCEvmJNRBU-aQkEAWOnx_78ejWM6uvW63cOmRO56scWEOIATQRfU6ZKoMT_v37Ujq2BXaKtVzUqFq6gyxIDcIdG_qFWuUuyN_sPWO5tTlg_l6OrL46zXHtdxeyS7g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=EPIPdjHNeVpsElkyIsKByEyQkWW8yIySQMR3UKNBUQKIFQ5D7QN07oXryucXj5z71Moze7yTYsdbkEx9Gv_WM9xI-qWSnc_SthZJy1-LS9gQs-wV10AIkuu2Qiza_9QL07nKXkY1_BeIsFvPsoVOYXNvzWsWmxJHrLGKndqCmNUWTP8HfXZuRMCin74WdOMUhwnEFFjPo7L8IOU7WwdMhO-rxcCEvmJNRBU-aQkEAWOnx_78ejWM6uvW63cOmRO56scWEOIATQRfU6ZKoMT_v37Ujq2BXaKtVzUqFq6gyxIDcIdG_qFWuUuyN_sPWO5tTlg_l6OrL46zXHtdxeyS7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه درباره روند مذاکرات با ایران اعلام کرد که تهران امتیازهای زیادی می‌دهد.
او گفت: «ایران در حال دادن امتیازات بسیار زیادی است و ما با اختلاف زیادی در حال پیروزی هستیم.»
او بدون بیان جزئیات بیشتر خطاب به خبرنگاران گفت خواهیم دید چه اتفاقی می‌افتد.
دونالد ترامپ ساعتی پیش از این اظهارات در گفت‌وگو با شبکه خبری فاکس نیوز گفته بود بازرسان آمریکایی هم با بازرسان آژانس بین‌المللی انرژی اتمی از تاسیسات هسته‌ای ایران بازدید خواهند کرد.
او در واکنش به اظهارات مقام‌های ایران در رد اجازه بازرسی به آژانس گفت: «آنها توافق می‌کنند، آن را کتبی می‌کنند، سپس می‌روند و می‌گویند که این درست نیست.»
رئیس جمهور آمریکا بار دیگر تاکید کرد که جمهوری اسلامی با بازدید بازرسان آژانس موافقت کرده است.
مقام‌های جمهوری اسلامی از زمان حمله آمریکا و اسرائیل به تاسیسات هسته‌ای فردو، نطنز و اصفهان مانع از بازرسی آژانس از این تاسیسات شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76655" target="_blank">📅 21:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76653">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=i0UL2gLnbidSb0UjWiEUKtYm052-ex3LPA6Xe5vhpSmoNJFVJLnXSnntqJ6hVDmSsvtfx6atD8rJUjmTWznzixl2XvG1POlOV_D_fMZtUNhIwwaYJoU4f4x0g4MSCIFuNd1DIn88XiUmwS0M5z0vPlspLxjJm10okBC5k-mTmRZpztUTT6wp4s9CG2gajHAOIlS-8d5Z3UiFW_DmrBNdrTWzwMdxEq9D3_y5DbppeEjr2_VmOrq7zxSEuNcbFELO5GzdxZzSvfPugN9qKDSoeKlTbU17YGX4KRxx9Uyv_qT-uMsFXL479PNL8cv-lQwkSB2dcEB_Q-60wh86yywbvg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=i0UL2gLnbidSb0UjWiEUKtYm052-ex3LPA6Xe5vhpSmoNJFVJLnXSnntqJ6hVDmSsvtfx6atD8rJUjmTWznzixl2XvG1POlOV_D_fMZtUNhIwwaYJoU4f4x0g4MSCIFuNd1DIn88XiUmwS0M5z0vPlspLxjJm10okBC5k-mTmRZpztUTT6wp4s9CG2gajHAOIlS-8d5Z3UiFW_DmrBNdrTWzwMdxEq9D3_y5DbppeEjr2_VmOrq7zxSEuNcbFELO5GzdxZzSvfPugN9qKDSoeKlTbU17YGX4KRxx9Uyv_qT-uMsFXL479PNL8cv-lQwkSB2dcEB_Q-60wh86yywbvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به  پزشکیان دوباره بیل دادند، اگه شهباز شریف جلوش رو نمی‌گرفت فکر کنم تمام اسلام‌آباد رو درخت می‌کاشت.
NR2OH
مسعود پزشکیان، رئیس‌جمهوری اسلامی ایران، در جریان سفر خود به اسلام‌آباد به همراه شهباز شریف، نخست‌وزیر پاکستان، در مراسم نمادین کاشت نهال دوستی ایران و پاکستان شرکت کرد.
ویدیوی منتشرشده از این مراسم نشان می‌دهد پزشکیان پس از قرار دادن نهال در محل کاشت، همچنان به بیل زدن و ریختن خاک اطراف آن ادامه می‌دهد؛ در حالی که شهباز شریف چندین بار با اشاره دست تلاش می‌کند پایان مراسم را اعلام کند.
در این میان، لبخندهای شهباز شریف و ادامه بیل زدن پزشکیان توجه کاربران شبکه‌های اجتماعی را جلب کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76653" target="_blank">📅 16:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76652">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtpQDtX5Funab08WmGAN7KYrYaS_OaeaIkPLzdNmZuS1yNtcAX0JP9UdCs9sqIxHMquD7AXL3nrBqWYXJVn-TqwyiVcFapHUnSwh4m6mwXAHk-EmnRSv4eda7-LW3Cc3_DXQRWK5LM59VrZMUxnC10Zaxmq8pyv3UbGj-a2oKOnfNKZ5bNWYHf8n7CAKcwUdjCce5pfVUixq-QDo4trpDrq-xZKgqwgmmRmlnwQ6Z3BUzkyc_8GZWzTheWtbcKAxWtgWaiCLbur7HOWgLuUKZHUbom_O5qMu7uidhrb8aOet7WUoLBewdgq6j8Y1s2H6iGRuA46pSV6N0FPu-CXJBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده روز چهارشنبه گفت واشینگتن بر نحوه مصرف دارایی‌های آزاد شده ایران نظارت خواهد کرد و به همین منظور دفتری در دوحه، پایتخت قطر، برای نظارت بر این وجوه تشکیل خواهد شد.
اسکات بسنت در گفت‌وگویی با شبکه خبری سی‌ان‌بی‌سی، تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای خرید مواد غذایی و دارویی از آمریکا استفاده خواهد شد، حتی اگر ایران گفته باشد که نحوه مصرف این منابع را خودش تعیین خواهد کرد.
او بدون ارائه جزئیات درباره سازوکار نظارت بر مصرف این منابع گفت این وجوه توسط وزارت خزانه‌داری آمریکا در خاورمیانه نظارت خواهد شد.
مفام‌های جمهوری اسلامی در روزهای اخیر با رد اظهارات مسئولان آمریکایی گفته‌اند نحوه استفاده از منابع آزاد شده در اختیار تهران است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/76652" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76651">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaZJ2SKieGPLokW96LUVxhjT2LY0iO8sQHqLxF3E2uXxUDICyWZMDdFfLzXV_OCmSpdFihyL9vg7ihwfdh0tw-17M5HFQgIWPY4zKbw2AW1jZBJKvb45VbVFu13-I_r5_nP--HQGv02UqVkBjalcnCpFaXvx2eK9RKYVHahYR1Og6RghJbRBDgbPlqmjDbXYenm7oQcYX8nIK7KLbcH_P2Ljb96WfU-vEae7GShcnKOqrVPW_EHwQcOsGCaPN6exMeVWqgMUAbgZmr-XeQ9nF_EEFRRFE0eZSE3pYrEAoSYoHsX2KDZxleQci-M1kxm4VJlqdqHdFOQd4WZ-fwAi1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی اعلام کرد که دسترسی به تاسیسات مورد حمله واقع شده و مواد هسته‌ای صرفا در چارچوب توافق نهایی با آمریکا ممکن خواهد بود.
کاظم غریب‌آبادی روز چهارشنبه در شبکه اجتماعی ایکس با اعلام این که در سوییس هیچ نشستی با رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی «علیرغم درخواست او»، برگزار نشد، نوشت: «هیچ برنامه‌ای نیز برای دسترسی به تاسیساتِ مورد حمله واقع شده و مواد هسته‌ای وجود ندارد.»
او افزود: «این مباحث صرفا در چارچوب توافق نهایی و در نتیجه اقدام عملی طرف مقابل در خاتمه تمامی تحریم‌ها و... بررسی و تعیین تکلیف خواهند شد.»
پیشتر گروسی اعلام کرده بود که سایت‌های غنی‌سازی هسته‌ای جمهوری اسلامی توسط بازرسان آژانس مورد بازدید قرار خواهند گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/76651" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76650">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOU3tkXdMMyg4xRZzRi00KuFKuF8scUiVR8_qRkQUsiCV5tJblqcukOaVHckirLRFtcmX1QVsaBeRz0NDKbPgJFVjZJti0WcKImHvEjifd_m867NP27m--Ike8OErEdia_xujBkclkpGornbpXKzsAt8cMGBbthmvYEW7-5BXWpISq84cU1ODvOnTMss6si-Wxa6h75Q93nL-5pBj1zUr05X3IwXqkBu362S9xd8pnG7K-4bZD_LPzdkCxNQJK-v8uSp7ZEuQXbtZltVRmYYJvqPucMeCYwYocPQU7zI24Cxs0bAfBeBefL6FWe_YOtDpt7Fqsi2LbLdVKVQZWx_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا، روز چهارشنبه در دیدار با رئیس امارات متحده عربی در ابوظبی درباره تفاهم‌نامه ایالات متحده با ایران گفت‌وگو کرد.
در بیانیه سخنگوی وزات خارجه آمریکا آمده که روبیو در دیدار با محمد بن زاند آل نهیان و دیگر مقام‌های ارشد اماراتی «درباره یادداشت تفاهم رئیس‌جمهور ترامپ با ایران، تلاش‌ها برای تضمین عبور کامل و ایمن کشتی‌ها از ‌تنگه هرمز و اهمیت صلح و ثبات در منطقه» گفت‌وگو کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/76650" target="_blank">📅 16:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76649">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1bpq2CGGxomjzwwYLoNY3CJo2nYSlzCeOS8LhHLNVM-0poXWl9RjTfElKPnpWVhq7gOMbIG5UxXHarpCr-p8HK9Bu5HHD1VmObAR6GmHEfrYubmBwo0xKsdMnv6Ax6_YDvSqjuNvuUBF51rxx1ex1TVm2t1AGsNb4IWpdeDVFSwg1vRyhnxGt8BtS5scLsSO6BpmtESW8BChX_ZdRJEX3lvWrXKpZtB-i3fM677pxxb-6yqM0ddrdo9NoL8IW56VePCUlOufnpCDgAYt50_rn9MTKXWzA6QDQpSYZrMY6hijSTA_w7UUS8sUaseEx2yOiudQytQ9dk7Vg2HXcbndw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامران غضنفری، نماینده تهران در مجلس، ضمن انتقاد از تداوم تعطیلی صحن علنی، به خبرگزاری ایلنا گفت که قالیباف طی چهار ماه گذشته بدون هیچ مبنای قانونی از برگزاری جلسات علنی جلوگیری کرده است.
این نماینده مجلس، وجود مصوبه شورای عالی امنیت ملی برای تعطیلی مجلس را «دروغ» خواند و گفت تعطیلی صحن با هدف جلوگیری از مخالفت نمایندگان با روند مذاکرات و پذیرش آتش‌بس صورت گرفته است.
او ادامه داد: «نمایندگان هم از یکی دو ماه پیش از قالیباف خواسته‌اند که اگر چنین مصوبه‌ای وجود دارد، آن را به ما نشان دهید، اما او هیچ چیزی نشان نداده است. بنابراین، این ادعا کاملا کذب و دروغ است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/76649" target="_blank">📅 16:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76648">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s0WE9dk84oQpn_dRsClF0-cjtyUmmetqkbM-8L0wfuGJSN8HMCNZZ6_5An-KPJTV9Pv5uVUxhMXmaMqehfzsz5j2wIvr1mBZ599s87PVnzv9LrXhcA2hoz-wf0MrL6a2BUAdRdBYC97U0C3rxNqtultsdv4AvQm-j57ilCvarLAmEURL4CIN7oc6qcZ6ww40CJcq4RgURbnlUhh1SdSBj87_2xNuD2vGWrRywWppjkEaQk6nQpOa5M-nPT6YzkYzu0ApK9kuudAEbCWCOwbFnnfTnA18B8xYMxqUYVHyC_wvozRykfB0UOTIruVJ1GNGvCGSp2gwhcaVR8m9XpmvAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران به آمریکا اطلاع داده است که، برخلاف گزارش‌های دردسرساز فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای، و هیچ نوع هزینه دیگری از هیچ‌گونه‌ای از سوی ایران برای کشتی‌هایی که از تنگه هرمز عبور می‌کنند مطالبه یا دریافت نمی‌شود.
اگر این اطلاعات نادرست باشد، مذاکرات فوراً پایان خواهد یافت!
علاوه بر این، هیچ پولی از سوی آمریکا به ایران داده نشده، یا از پول‌های خودشان برایشان آزاد نشده است.
ما بخشی از پول آن‌ها را، که کاملاً تحت کنترل ماست، برای خرید ذرت، گندم، سویا، و چیزهای دیگر، در اختیار کشاورزان و دامداران خودمان قرار خواهیم داد.
غذا در ایران به‌شدت مورد نیاز است، و ما آن را منحصراً از ایالات متحده برایشان خریداری خواهیم کرد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/76648" target="_blank">📅 16:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76638">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jhOcITc3CzqCv2P6sCKuOrXM0SWXRXQ6ZNW0ZqHaVVlNmX5mlZZQb-rdUiL0EATIPPvlm0JrYAAke3V4P-Fd2ZHyoKqLs_uljyFqbjjDJk_XzcCXFD90ADySa2UR6Agbq6hqtYpZbqVMyRN2_x6lyW0t8Oda_4jv7LJDhS48D-SpFEum83mpxTG5Y3y6I_OWxJAdskoxUwu1Gml05vNjOaQWrC4ly8fxOZPYFbnhBdolGo0va54KQoebL195nCO1HNfNPxUa4iXG3bg2vNsBr6oIsnrgyLQ8KQ50H-lLrUg2a95-UOzKdtceauO6HBIxs1KjL9gwvxSJU9d9z90QLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rQO9MB_ke37kRKpsefjOFlhtfrPuI1JQGOtSMPmHZWH09Pmrk9xQbaJ58S1IRS7BeasKOX2xQOs_5K0wM0Kic9ijoWDjt66s0RTyTX04Rpnx08H9GhZNxNnjHCJ9xcZDNUe2O3g66ZpU-XkuVNfhiiY0_Mzb-ckvn1cNlkUZfsqLQQ6mvgH7U7ugLTUTqgpxb3lbPX40UyyT76AxN_QEFOJN0JU2zogzgikna39Cad-JZmiVCN-3LDiJYeF6k9QUOb7USOrB4blQHkLnbG7JQvimmNxMWUycHrefPSr_YOkKfW3E3NRC3uXLG8liCYtZTQrwhmQx0Jp9DuyVIhH2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DkuJ8DljUMOAouYJYlepYWiQmyrCPUKtfHXHi7Si7FgX_TgrZM6eTLcaBUJegtfj_o98mF3CWDV9jV1HfbmfLCm1KtTiVS07UcCGLnrxK1qkxru88Wr-8OF17MPWH5tyu8wjP_YZ4oqX3ghIVlfhdrU-xNR-lmqbKh_yAMP7u1amCIOTVL2QkySSKlOGZRzXgBKeZ9qrdzuB8TsX8rp1NoFFJFZfVDVCfLNPN3z7WQ89M8NPZkm73v9LsbjwRuEn2bwe7h_R8KaivuKsSvQtXGk32fH6CWgPKQKUleNbvbx22KzCXk8ednAvHePpsZcqHcgtsup94TAcYInNJzD8pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qz5mr2HzoapYfA1cEGLcBOgM2bIbmzXlBC3tSu_CsGmaehB-t3MQDf7PBqsiG7JyDWWerMuTh4au9w7emLA0ZtYmrJ8UfTP55gXMvEkONyo27Awfj7U3pUp5CFiPWAD5jqFNFa8_Rq-Sil08kULSkL9r8vJsC8gXNwyy07zyRzeOHyVtwJ4SOy2BPBnru2eFI3JlpgJzqi-KL3Bbu_0a74sn-7Dt-XkMWA_y00EVh6f1NOPwZyGS1G9OKanQte1WhqYNp-8wFhJbEAa5ZMXKfnHeTinDd4FYvzauUk3Ty1gkQUxG4XBMG25YLldkTR9gtnxd8OeHlvMz9WAqrpd78Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U2P4Tqz9rXxBmPtPz-ZJ9sWOzNbfF0iww_N95ZpPUKrPNGLRSTPl-PynppFMZL9qoQ0gEFTFB32hu39kgf6lmZE8vZWYkx35UTpwx6PHJldNv_xkheX08tYHpS-EkA1jTlrGGWebhVOfLzudV5nYGZ60tpLYLefPk402VQO6XH9L0dKKOqOn7UeLuMSKttiNrE3bAXZK1UahAvOXmmZAXOYIs6VygeUy5tp0jXV73BAnmfLKhoFPpxDYys2UmRCzJZ4gKeiQxbaLKMXLINubC1cNZGZ2HTlcWx6LuSnOqX8oNGShNO6vebMSqC1MSdo0h17YGn7oXb4OE41ZaC0C6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUb_fmqwJaQkc-wUdb6p8P3hK5ykKIWmzXJ8sPsDblejqgJ8eCmifM2QVUEYvtpwv2s42KtpviS7CBiyYz_Q1yJD4OafMC-QRpm99usMsGRnkZeXNJPqdlMMg6pemf2RzE1oHpwWjC1oq72uOwaZu4ACX55HJHJIyDFZD6RVpTMF8mfWunLg1A5X2lx2GkE2dA_bEUWpVmKVp4Wt9DU05YGUOIyqOxLjB6XP6ZNXrCL9a64_KEFl3v3LrIp7Iv-INX_ZjP46nDLiTOdw2qTXdsKFH_Tbx3VlbmN-HkTL1Fr8qq1bKaKmInxAVXUBgPNyAGB-wrcrFPRZQbarM-L_ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Exi6G-vQ0WU-2WrUc1luZj235udqMMfyGpv9n2ake0tOnppqERc7bhOb_Ri40yK1WqIkmBp9Cd_BMF4nmM05TdoijZI75TfG0kXIWqMWczPoTyOuK4ZXii1Jdq7U9WYjL1Dvk1uVDLRT51yhQO2WC1e92cUYZxsYixCg_1Co3u37Uh5h-0oCl0spWJ8_-IPEiEcb1Qi534XZjV4M3CyiRoImYcuiS_vgI7b5bG-shCbikElR1TlIDY6qGRXd3BeGTDRMnSFpW14guEjYOaKZVdENT5jFT5QH_VJylj5HvpUvnOAg4wT1KAQsX8zcFALOGOJCI98t0ssdp5P-K2oItw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dDEbj3Cdand9a13azIm7yNro6m_5CbJ177X4GwIHcXQWbf0l9NcR2qdgoO3pwd5qwszx7l9j2Uz3Bj_yF3NIimVql6mhVoypvMWNEk22O9kwhC6yjvq024l-TcS0VstzizUxVog65E1IqWOjL6g9C0IiwMsQIePPuagXjULSWR_Df5gpiYcnbipqWCyEkucgK7_Bfe8soXsVG7jfubYRZaKnphwseJ4--Hibamz8Wu6CpqYbPMaqUJv-1AT3XjC9gus__kLJoyJR3bv_xlZ3l9Rr4LhX2IHp8QyevQ6AxD6vP6OYqAW5G0J5gsgEK2D5xXWnIyiCfcoJi-sUz1EZlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M1dFcpQZAhDlEae38GNMkneBkOjlApz-kIFpzNWz20nSju6tJcNTuqxwUWlfxzIVSnnbUNpJZM2FDed2T-ztZC2y3uRYFrE2mienRgFt6WmbguBCzn-KzC9unvHZ4E3c2KpnhtPRij6HSi7RLPZqAv-sKUB6JGS7gKr8X77EjXWoQ-jbktvn_fnE51MHz8uJYrrfSU0Zyr48F0Rn_V_P8b3CmbKFaflD3jfWWXABldAICvz8wi4KM6we3CB4W9s_92j8P0Isr8CzLWyi4q4GghT8hESyiIZfy5ovC-3whi9ZD9WkcrBbgw4F23sNjnRvWY8mwI1DpiuTyyvAc4kusA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uA1GPwo4E93VcFm1pjSC1NxjZR3MydITxQ1jNE_em0C3g1Rl-aUg5TcnNNxI-hTuTXQh9-fkdDvSNbGNNPKCiIAWurFalctHESvdW7FzzyWfTL90awzEA1bugl8719OqrPjsmlWWufWAFhhIoCtfXZ8-e2xpZH2BIIGetFdMzqhCR4Pf7BrNxfQ713cEWtFakmSfcah1DfG4awfzQvR7lok_RskEKRGpF6efdISO2vbzmBFy4xSbDZeZizKgJdxU4s9XsVSvTGlzs4lobgVx5rYhNoLlqg_KuZctNwomCaznfFTXwgjSDtR3rNZ59Ryz3rOov6HTV8s7CttVL9j0Bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔴
مرور قربانیان اعتراضات خرداد ۱۳۸۸
‏اعتراضات خرداد ۱۳۸۸ که در اعتراض به نتایج انتخابات ریاست جمهوری سال ۱۳۸۸ شکل گرفت، جانباختگان زیادی برجای گذاشت، بنیاد برومند تا کنون ۱۳۸ نفر از این افراد را که مرتبط با این اعتراضات کشته، ناپدید یا اعدام شدند را در نقشه اعتراضات خود ثبت کرده است. برای اطلاعات بیشتر در مورد این قربانیان به سایت بنیاد برومند مراجعه کنید.
اگر شما هم اطلاعاتی در مورد قربانیان اعتراضات دارید با ما در میان بگذارید.
‏لینک نقشه تعاملی اعتراضات:
https://www.iranrights.org/projects/protestmap/fa/
@IranRights</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/76638" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76637">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=oLfB2gNTOuDRmCMFw_D_YIiop576Fpo6_GiXbJW4y9BsBK129u0S832dSamalOyOnGsk9ysM6DKhbRokBc7e8dBGbqeEcajYoQdLrNkl8aYx4KkT8r7T_lxqCsKaw161MerHwQIc23HVhcs8O4xPwDrzTJSEgothahYMkTtJo5FatqNf4E-DZSOU24js6N3goiZJL-zbKAnp4CsY20EdN6Er2J_40t0g0g5AJoUUIIvuOzanDKvf69hcbceqqEz6Ed_0Zv-9G7EpNrMIzoVbm0yFDmDb1D12RipmLgdJxYIVzk2uY0jjkQB1np2nDEVHeaNAZvdQAike2O_2fXrZ9g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=oLfB2gNTOuDRmCMFw_D_YIiop576Fpo6_GiXbJW4y9BsBK129u0S832dSamalOyOnGsk9ysM6DKhbRokBc7e8dBGbqeEcajYoQdLrNkl8aYx4KkT8r7T_lxqCsKaw161MerHwQIc23HVhcs8O4xPwDrzTJSEgothahYMkTtJo5FatqNf4E-DZSOU24js6N3goiZJL-zbKAnp4CsY20EdN6Er2J_40t0g0g5AJoUUIIvuOzanDKvf69hcbceqqEz6Ed_0Zv-9G7EpNrMIzoVbm0yFDmDb1D12RipmLgdJxYIVzk2uY0jjkQB1np2nDEVHeaNAZvdQAike2O_2fXrZ9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ترامپ پست کرده
متن صدایی که ازش شنیده میشه به تشخیص ماشین:
از سال ۱۹۷۹، زمان می‌گذرد.
ایران در ۴۷ سال گذشته هر سال آمریکایی‌ها را کشته است.
۱۶۰ گروگان کشته شده‌اند.
۱۸۰ حمله از سوی ایران به آمریکایی‌ها.
رؤسای جمهور پیشین با سازش با ایران، ۱.۷ میلیارد دلار نقد به آن پرداخت کردند و در حالی که ایران به دنبال سلاح هسته‌ای بود، از اعمال تحریم‌ها خودداری کردند.
این می‌تواند ۱۱ بمب هسته‌ای یا موشکی بسازد که به زودی ممکن است به خاک آمریکا برسد.
تولید قریب‌الوقوع یک سلاح هسته‌ای آن‌قدر نزدیک است که آرامش‌بخش نیست.
ایران چه زمانی به سلاح هسته‌ای دست خواهد یافت؟
هرگز.
متشکریم، رئیس‌جمهور ترامپ.
realDonaldTrump
پست دیگری که در واکنش به تصویب طرح توقف جنگ در سنا نوشته:
ترجمه ماشین: بنابراین، من ایران را در گوشه رینگ گیر انداخته‌ام، آماده زمین خوردن، حاضر است عملاً هر چیزی به ما بدهد، و برای نخستین بار در دهه‌ها، حسابی برای ایالات متحده و رئیس‌جمهورش، یعنی من، احترام قائل شده؛ آن‌وقت سنای آمریکا تصمیم می‌گیرد رأی‌گیری بدزمان‌بندی‌شده و بی‌معنایی درباره قانون اختیارات جنگی برگزار کند و به حامی شماره یک تروریسم در جهان بگوید که ایالات متحده کاری را که من با آن‌ها می‌کنم دوست ندارد و من باید متوقف شوم، و با این کار به دشمن کمک و آسایش رسانده است.
چهار بازنده جمهوری‌خواه همراه با دموکرات‌های احمق رأی دادند، و ایران از افراد من پرسید: «همه این‌ها یعنی چه؟»
این سناتورها همین حالا کار مرا دشوارتر کرده‌اند، اما من آن را انجام خواهم داد، به هر طریق ممکن، چون من همیشه کار را انجام می‌دهم!
رئیس‌جمهور DJT
realDonaldTrump
در واکنش به:
سنای آمریکا که در اختیار جمهوری‌خواهان است، روز سه‌شنبه از طرحی قانونی برای توقف اقدام نظامی آمریکا علیه ایران حمایت کرد.
سنا با ۵۰ رای موافق در برابر ۴۸ رای مخالف به این قطعنامه مشترک رای داد.
این طرح پیشتر در اوایل ماه جاری در مجلس نمایندگان آمریکا نیز تصویب شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/76637" target="_blank">📅 06:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76636">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zt0eM1TurLItHgPaCdZEBDZC-R_zIjZWx7DJ_FIqMBHKYiAfSTNS_hmdfKOpVD5c_FxMDJTPL7lLykD4Ay4q41QSZiXO5GfDA2wzHsbd0wsK266OUD3CkP5ATvs8O_tXmPg2Qlf3fr3scQ6BbaL1xw2Ckd2-GTXtHjfZDSKNotIC6D_hxPa2vjdRElcgUceNLKba4BvlPnlqOeXsqSj0j0nddgnvv0N8AaFec8zpQUgoM5JWdpgIVOT5Yq_IjLQGYfpJFhnkC1dSkmi0fg1wC1liLzi01BzU9NtHNL9tsIQ4YVpZ2CegR-ex9sR132qFm0rCYBe2eyX--iuI1t0MUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ProtesterCrow
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76636" target="_blank">📅 03:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76635">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oFbNGwSoRotRFKlrRxJklQ-mhazf1z4iTMSNHHrheoSidL_RUyaJwX9BhtMO0Ezpb6RviLqUabeRqaWFsxuRgnnoUWsFSDKNmbG-Zb8D1P5eJ6y-W3y6lcbQTJLvwDi2yq-WXTu8zP5EKued7rx-S03QLXmxe2NI7mL_wsXIGoxVcplynBlcK5evAOCs2hjNGkM3XLCiSkOpeI44NgrtASa53GnHMRH66zfky6Pv2_eO2m7mQosgMHbPT_Gqx5Q3gHvfI663mM6YSEigFS0tz1bR_AcPo2IIknUWYSG9l11dJj_gpecGRl1W0YszA8QIyePKcqDA6g4XSMpnKwcPkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنرانی ترامپ در پنسیلوانیا
جملات مرتبط با ایران به تشخیص ماشین:
ما به یک توافق صلح تاریخی با ایران دست پیدا کردیم تا درگیری در تنگه هرمز را پایان دهیم.
راستی، دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد. جای بسیار زیبایی است. این بیشترین مقدار نفت در تاریخ این تنگه است. هرگز چنین چیزی ندیده‌اید. به آن می‌گویند فوران نفت.
مهم‌تر از همه، داریم یک چیز بسیار مهم را تضمین می‌کنیم؛ چون دلیل انجام این کار همین بود. من به همین دلیل این کار را کردم. ۹۹ درصدش برای همین بود: ایران هرگز سلاح هسته‌ای نخواهد داشت.
اما یادتان باشد، این آسان نبود. ما ۴۷ سال رئیس‌جمهور و افراد دیگر داشتیم؛ کشورهای دیگر هم بودند. ما تنها کسانی نیستیم که هیچ کاری نکردند. آنها قلدر خاورمیانه بودند. حالا داریم ایران را بدون نیروی دریایی، بدون نیروی هوایی، بدون پدافند ضدهوایی، بدون توان موشکی، و بدون برنامه هسته‌ای باقی می‌گذاریم.
ما آنها را بدون هیچ ظرفیت هسته‌ای باقی می‌گذاریم، و آنها با این موافقت کرده‌اند. و رابطه‌مان هم خیلی خوب پیش می‌رود، هرچند اگر اخبار جعلی را بخوانید، هیچ‌وقت نمی‌فهمید. فکرش را بکنید، اخبار جعلی.
آنها ارتش ندارند، نیروی دریایی ندارند، نیروی هوایی ندارند، پدافند ضدهوایی ندارند. ما می‌توانیم هر وقت بخواهیم بر فراز تهران پرواز کنیم. هیچ‌کس کاری به ما نخواهد کرد. بعد اخبار جعلی را می‌خوانم که می‌گویند اوضاع آنها خیلی خوب است. اوضاعشان خیلی خوب نیست.
اما اقتصاد ایران خرد شده و پایه صنعتی دفاعی‌شان چنان به‌شدت آسیب دیده که بازسازی آن سال‌های زیادی طول خواهد کشید. سال‌های بسیار زیاد. حالا ما داریم تلاش می‌کنیم به توافقی برسیم که منصفانه باشد.
یادتان باشد، ما مجبور شدیم این مسیر انحرافی را برویم. مجبور شدیم سراغ ایران برویم. نمی‌شود اجازه داد آنها خاورمیانه و ما را منفجر کنند؛ اگر چنین چیزی ممکن باشد. ما زودتر به آنجا می‌رسیدیم، اما آنها اسرائیل را منفجر می‌کردند، کل خاورمیانه را منفجر می‌کردند. اگر می‌خواهید اقتصاد بد ببینید، آن اقتصاد بد است.
یادتان باشد، نفت ما، در میانه این درگیری، از دوران جو خواب‌آلود بایدن هم ارزان‌تر بود. و ما داریم یک آتش را خاموش می‌کنیم. بایدن، کلینتون، بوش، همه‌شان، باراک حسین اوباما ـ اسمش را شنیده‌اید؟ اسم باراک حسین اوباما را شنیده‌اید؟ ـ هیچ‌کدامشان کاری نکردند.
اوباما به آنها ۱.۷ میلیارد دلار پول نقد سبز داد، یادتان هست؟ با یک ۷۴۷. آنها انبوهی از پول نقد را با هواپیما بردند. ۱.۷ میلیارد دلار. صدها میلیارد دلار به آنها دادند و فکر کردند می‌توانند با رشوه آنها را به صلح بکشانند.
تنها چیزی که آنها می‌فهمند همان چیزی است که این آقایان ردیف جلو می‌فهمند: چکش. چون اگر نگاه کنید به کاری که آنها کردند ـ به کاری که ما با ظرفیت هسته‌ای‌شان با آن بمب‌افکن‌های B-2 کردیم ـ آن یک چکش بود. در واقع اسمش را هم گذاشتیم چکش. عملیات چکش.
دمبوکرات‌ها به نفع داشتن سلاح هسته‌ای توسط ایران رأی دادند. و علیه بودجه نظامی رأی دادند. اما من آن را دور زدم.
ایران، ما آنها را از پا درآوردیم. در یک هفته، اساساً از نظر نظامی تمام شده بود. کشوری بسیار بزرگ‌تر، و با ایدئولوژی‌ای بسیار متفاوت. ایدئولوژی مسلمانان کمی با ایدئولوژی کاتولیک‌ها فرق دارد. ما کاتولیک‌ها و مسلمانان را داریم؛ کمی متفاوت‌اند.
... ونزوئلا عالی بوده و ایران هم عالی بوده/خواهد بود، اگر عاقل باشند. وگرنه مجبور می‌شویم کار را تمام کنیم، که کمتر از یک هفته طول خواهد کشید. اما فکر می‌کنم آنها مشکلی نخواهند داشت. آنها کاری را که باید انجام دهند انجام خواهند داد، چون ما باید این کار را تمام‌شده ببینیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76635" target="_blank">📅 00:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76634">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=aqwam12AS3iaJSLouARf1RxiOXaslDqaTAOtmaaEYHk9CETpvM1-ls2pcxyBWrmcTsaVG0dqkLTJVuzAbdNS0B2t9HxILx4_lIAW4SNkSs5ZTbdY3YuonRXCuVjD9GXM9UOOMH4dWnBaADTorr2DeljIt_nlA9kLXkjAenj8ARSr8FCiyJ-3WZn8wYV4fzVoM1CJW_CgJnS9GPs5v_j9e22Q_elKaDVRFYeV-HqpNMfmPXrorVVwgIMkp2vN_JPKeoez-kXnu6IOke3EV16fxsvaoGxz6Y6Ct6nViVI07i4M-2N0-TQ6WwZiAwfNP89JlDshr4SqcJp8Vp5f82p6Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=aqwam12AS3iaJSLouARf1RxiOXaslDqaTAOtmaaEYHk9CETpvM1-ls2pcxyBWrmcTsaVG0dqkLTJVuzAbdNS0B2t9HxILx4_lIAW4SNkSs5ZTbdY3YuonRXCuVjD9GXM9UOOMH4dWnBaADTorr2DeljIt_nlA9kLXkjAenj8ARSr8FCiyJ-3WZn8wYV4fzVoM1CJW_CgJnS9GPs5v_j9e22Q_elKaDVRFYeV-HqpNMfmPXrorVVwgIMkp2vN_JPKeoez-kXnu6IOke3EV16fxsvaoGxz6Y6Ct6nViVI07i4M-2N0-TQ6WwZiAwfNP89JlDshr4SqcJp8Vp5f82p6Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آذر عظیما، خواننده پیشکسوت موسیقی ایران و از نخستین خوانندگان برنامه «گل‌ها»، در ۹۹ سالگی در اصفهان درگذشت.
آذرمیدخت عظیما سراج‌پور که بیشتر با نام آذر عظیما شناخته می‌شد، متولد ۱۳۰۶ در اصفهان بود و فعالیت هنری خود را از سال ۱۳۳۳ با رادیو ایران آغاز کرد.
نخستین اثر او ساخته‌ای از ابوالحسن صبا با شعری از ابوالحسن ورزی بود. او همچنین از نخستین هنرمندانی بود که در مجموعه برنامه‌های ماندگار «گل‌ها» حضور یافت و نخستین برنامه «یک شاخه گل» را با همراهی ویولن ابوالحسن صبا و سنتور فرامرز پایور اجرا کرد.
آذر عظیما در طول فعالیت هنری خود آثار متعددی را در برنامه‌های «گلهای صحرایی» و دیگر برنامه‌های رادیویی اجرا کرد. قطعه «راه شیراز» از شناخته‌شده‌ترین آثار اوست که با ارکستر فارابی به رهبری همسرش، زنده‌یاد مرتضی حنانه، آهنگساز و رهبر ارکستر، اجرا شد.
از آذر عظیما به عنوان نخستین بانوی آوازخوان اصفهان نیز یاد می‌شود. او روز دوم تیر ۱۴۰۵ در ۹۹ سالگی درگذشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76634" target="_blank">📅 23:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76633">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=UnYI0KxYnhLon-L-2pbDVPz98_o5-7VXZqWO7gTVhCaejRKs9roOdpJZeY10A_EuvWF67Dw2-mBqWalcB667cZDXNoA5FHz_MGtD2NQayV6BN-wJ2t0OQdMYZS6kvH6v1LS3tqQ0qNqNYl6bu2wvn3IHdeISkjRVwPhvCFrdfrISrIrmz_uERF-qDZMPI1-p5CCzwlsfhQbkQTvUxvUpCCAtlgBkTh9WObtgt5O2b0urtvXPc9T0Fd1lgpuO7oxTwup7sb7ytwyveoA2rQTh8TGnmEfTPHji6_MkXSYxEeTmZ1FhAxIbJKikN8QVxMFrBB9WCKL5X0JGVgAQPNMonw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=UnYI0KxYnhLon-L-2pbDVPz98_o5-7VXZqWO7gTVhCaejRKs9roOdpJZeY10A_EuvWF67Dw2-mBqWalcB667cZDXNoA5FHz_MGtD2NQayV6BN-wJ2t0OQdMYZS6kvH6v1LS3tqQ0qNqNYl6bu2wvn3IHdeISkjRVwPhvCFrdfrISrIrmz_uERF-qDZMPI1-p5CCzwlsfhQbkQTvUxvUpCCAtlgBkTh9WObtgt5O2b0urtvXPc9T0Fd1lgpuO7oxTwup7sb7ytwyveoA2rQTh8TGnmEfTPHji6_MkXSYxEeTmZ1FhAxIbJKikN8QVxMFrBB9WCKL5X0JGVgAQPNMonw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی بالا رو منابع دولتی با این شرح منتشر کردند:
"تشریح جزئیات اقتصادی تفاهم‌نامه ایران و آمریکا از زبان رئیس‌کل بانک مرکزی"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76633" target="_blank">📅 23:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76632">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRI75wZDZcvQ_ht41QbadpMS9O3w4dAPudvKXqHUY6NR8jkm3v-xYqwME2MdS_Lq58Y3jNuR32pxFXPw-IJfXUEZY-yxee54iDBH2ZzJ88itmNTCEfgA_pmp_3j_04r61UhKnjgwLk8HqfpiugCdKgtbDqAylcOHKeuaL4NE8wf_kp8aY-bpBzQneOxV54ZNg1cd-QodwXe7wpwXGl096OmPu5hpgrgjd6BkKnNNNw-bLZOePSkdVm7qQpUKdNiwX8UMkNODWKgKpAZK0XmDuX18fX4A1XRRzw1XlyrXDsnA78XJ3ZyZiXkflK0GHROO_tnxf5BsgfZHl9JfMp-ZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده، در حضور خبرنگاران در ابوظبی گفت که جمهوری اسلامی ایران به دلایل سیاسی و داخلی خود، موافقت با بازرسی‌های هسته‌ای آژانس بین‌المللی انرژی اتمی در نشست سوئیس را تکذیب می‌کند.
روبیو گفت:
ما می‌دانیم آن‌ها با چه مواردی موافقت کرده‌اند. من نمی‌دانم چرا مجبورند این حرف‌ها را بزنند. سیاست داخلی یا مسائل درون‌مرزی آن‌ها هرچه که هست، خودشان باید با آن کنار بیایند. اما ما می‌دانیم متعهد به انجام چه کارهایی شده‌اند؛ حالا یا آن را انجام می‌دهند یا خیر.
وزیر خارجه آمریکا در پایان تاکید کرد: «اگر آن‌ها به تعهدات خود عمل کنند، فرآیند رو به جلو حرکت خواهد کرد، اما اگر از انجام آن سر باز زنند، رئیس‌جمهوری (ترامپ) باید تصمیمات جدیدی اتخاذ کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76632" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76631">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=KmLA54tjHIZ884I0ESf6IHKeb2NbdscWPp3tkJzey-3ObL-pOuH4SoGxI5Ywu6Xgfe_DhMJh3TLL2pArGkR5Zcaleengx6hC7_e9HFpe6R9-NzjbV78rF2jBDenlYVMQWNf5jxYEhXCkI8hUv50Fiuv_f6u5QFvvjWkDd3ah3Bf14PcXE_lGjK38nde8qFy4kR8v5QKl1LzxhMQoN9XWqz5vUGK5ESDGQM-SsfHCnRVYiUzU132Vc6LuSUfuGHLaDzOeLYysQMofncxRM_o41EGhAmkyRnV_1Q9y4Xkyv3CRPhxnMb2PqvXDjmE8sTVnD2pQNpiKE2aGaHyWflMZwA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=KmLA54tjHIZ884I0ESf6IHKeb2NbdscWPp3tkJzey-3ObL-pOuH4SoGxI5Ywu6Xgfe_DhMJh3TLL2pArGkR5Zcaleengx6hC7_e9HFpe6R9-NzjbV78rF2jBDenlYVMQWNf5jxYEhXCkI8hUv50Fiuv_f6u5QFvvjWkDd3ah3Bf14PcXE_lGjK38nde8qFy4kR8v5QKl1LzxhMQoN9XWqz5vUGK5ESDGQM-SsfHCnRVYiUzU132Vc6LuSUfuGHLaDzOeLYysQMofncxRM_o41EGhAmkyRnV_1Q9y4Xkyv3CRPhxnMb2PqvXDjmE8sTVnD2pQNpiKE2aGaHyWflMZwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
خبرنگار:
آقای رئیس‌جمهور، وزارت جنگ برای جنگ ایران ۸۰ میلیارد دلار درخواست کرده است. فکر می‌کنید آمریکایی‌ها در شرایطی که بسیاری از نظر مالی تحت فشارند، از این حمایت می‌کنند؟
...
آنها فقط از این حمایت نمی‌کنند، بلکه آن را مطالبه می‌کنند، چون اجازه نخواهند داد ایران سلاح هسته‌ای داشته باشد.
می‌خواهید دردسر ببینید؟ بگذارید آنها سلاح هسته‌ای داشته باشند.
ما در قبال ایران خیلی خوب پیش می‌رویم. آنها نابود شده‌اند و ما داریم با آنها توافق می‌کنیم. باید ببینیم همه‌چیز چطور پیش می‌رود.
همین حالا، همان‌طور که احتمالاً دیروز شنیدید، ۱۹ میلیون بشکه نفت عبور کرد. این بزرگ‌ترین رقم در تاریخ تنگه است؛ تنگه هرمز.
بازار سهام ما به‌شدت بالا رفته و قیمت نفت در حال سقوط است. امروز برای لحظه‌ای به ۷۰ دلار برای هر بشکه رسیدیم ــ در واقع فکر می‌کنم از آن هم پایین‌تر خواهد رفت. این پایین‌تر از زمانی است که شروع کردیم.
و واقعاً شگفت‌انگیز بوده است. نکته اصلی این است که ایران سلاح هسته‌ای نخواهد داشت.
خبرنگار:
ایران؛ ایرانی‌ها می‌گویند هیچ سفر برنامه‌ریزی‌شده‌ای برای بازرسان آژانس بین‌المللی انرژی اتمی وجود ندارد. آیا این بخشی از توافق شماست؟
ترامپ:
اشتباه می‌کنند. خودشان می‌دانند اشتباه می‌کنند. به ما در داخل گفتند که این را قطعی کرده‌ایم: بازرسی صددرصدی.
و اگر حق با آنها بود، همین حالا جلسات را لغو می‌کردم.
خبرنگار:
و ایران می‌گوید درباره آن توافقی وجود ندارد. از نگاه شما، آقای رئیس‌جمهور، آن بازرسان واقعاً چه زمانی روی زمین خواهند بود؟
ترامپ:
در زمان مناسب. عجله‌ای نیست، اما در زمان مناسب روی زمین خواهند بود.
خبرنگار:
آقای رئیس‌جمهور، به متحدان خودتان که از توافق با ایران انتقاد کرده‌اند چه می‌گویید؟
ترامپ:
خب، فکر می‌کنم هر کسی که از آن انتقاد کرده، در موضع بدی قرار دارد؛ حتی اگر از دوستان ما باشد.
چون ما ایران را در موقعیتی قرار داده‌ایم که هیچ‌کس تا حالا قرار نداده بود. رؤسای جمهور دیگر باید ۴۷ سال پیش این کار را می‌کردند.
ما ایران را در موقعیتی قرار داده‌ایم که ارتشش کاملاً از بین رفته، رهبری‌اش از بین رفته، رادارش از بین رفته؛ همه‌چیزش از بین رفته است.
آنها موقعیت مذاکره خوبی ندارند.
اما با وجود این، پولی که از ایران خارج می‌کنیم، قرار است به کشاورزان ما برسد تا ذرت، سویا و گندم بگیرند؛ باید پول زیادی باشد.
چون آنها مشکل گرسنگی دارند، مشکل غذا دارند، مشکل دارو دارند و مشکلات زیادی دارند. تورم هم دارند. تورمشان همین حالا به ۳۰۰ درصد رسیده است.
بنابراین مشکلات زیادی دارند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/76631" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76630">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N15dFzw8ZU7vXzXty6bs8YGcBFVBYnMLLj6E-6eulPcTfHT7rXonFwUlnAC1dWP4M-p3T7NAhNzZNDVN6NzuGNPRxoEEvA18AeNE7DFPY2qJLkQoXzm23R9BP3MwBrEp77iIHghcUkfH_OkGoFyOrJfqeiva5c8lSZmMEbFc6d39pE7OynhKvrCpFg4CqizgF8qFscAi68Rh3z8uEnTNL_3vYWJ6ajT5P4PDpE53l7lylPXw8drbIA1EudQnUPgxO9vJEB2lHw52DO19ub-nETqm7S6THUjW2oTdWqRRZM1QWK1Lx96tly_Hz3gLvKSpOsPfErP4l6G4ozq_pqf82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، سه‌شنبه به شبکه ان‌اچ‌کی ژاپن گفت بازرسی از تاسیسات هسته‌ای ایران انجام خواهد شد و هرچه زودتر آغاز شود بهتر است.
او افزود اولویت اصلی آژانس، شناسایی و تایید محل نگهداری اورانیوم با غنای بالا است.
گروسی گفت آژانس بین‌المللی انرژی اتمی به‌زودی با مقام‌های جمهوری اسلامی درباره زمان‌بندی و جزییات بازرسی‌ها گفت‌وگو خواهد کرد.
او تاکید کرد آژانس این بازرسی‌ها را به‌طور مستقل انجام می‌دهد و نیازی به نظارت یا کمک دیگران ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/76630" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76629">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PvIyaUOFoauzZhJs2DZ-W1HgocOa98NpqdbReojvDQ34566T3gmC10prbOvmXMJ49DD-RI1tHY7vBpgN2LtckYjh1QTqwj5JK5b0N3BprsK58RPVAWMBI1N1chkdXbdaDOvEttzK_N3yM92A0Hg8KLxEECYpn79zTImMGEUNZyWIaNQG98YVNdwpYLiMu_w5e-W5lF2kBr_gjAdXjnFQbxlT_e4tkk5k8fpQ-59W4C0Fyygx-OaRY75R2DnA4EmayftiJdY7fr1bCd09uDUgs0wGV1TEK98DOrRCp9lMhzqQbMK1BjxU4_wBa2eEJOOWsBFrX8HNVR4MsAEa6pyrTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه آمریکا می‌گوید تا زمانی که گروه‌های نیابتی مورد حمایت ایران به حملات موشکی ادامه دهند، دستیابی به صلح پایدار در منطقه غیرممکن است.
مارکو روبیو که به امارات متحده عربی سفر کرده است، روز سه‌شنبه دوم تیرماه افزود این موضوع «در زمان مناسب» مورد رسیدگی قرار خواهد گرفت.
او همچنین تأکید کرد هیچ کشوری حق ندارد بر تنگه هرمز عوارض یا هزینه‌ای تحمیل کند، چرا که این آبراه یک مسیر بین‌المللی است و بر اساس قوانین موجود بین‌المللی حفاظت می‌شود.
تنگهٔ هرمز از زمان آغاز حملات آمریکا و اسرائیل به ایران در ۹ اسفند پارسال، از سوی سپاه پاسداران مسدود شده بود و تنها هفته گذشته پس از توافق اولیه بین تهران و واشینگتن برای پایان دادن به جنگ تا حدودی بازگشایی شد.
وزیر خارجه آمریکا در مورد لبنان که برقراری آتش‌بس در این کشور بخشی از توافق بین تهران و واشینگتن است، گفت که ما قرار است مستقیماً با دولت لبنان به توافق برسیم.
روبیو تصریح کرد که «آینده لبنان را مردم لبنان تعیین می‌کنند و پرونده لبنان از هرگونه توافق با ایران جداست».
@
VahidHeadline
فرماندهی مرکزی ایالات متحده،
سنتکام
، با انتشار تصویری از ناو هواپیمابر «یواس‌اس جورج اچ. دبلیو. بوش»، در شبکه ایکس نوشت که این ناو در
دریای عرب
در حال فعالیت است.
سنتکام افزود دو ناو هواپیمابر آمریکا همچنان در خاورمیانه مستقر هستند و نیروهای آمریکایی حضور خود را حفظ کرده و در حالت آماده‌باش و مراقبت کامل قرار دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76629" target="_blank">📅 19:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76628">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5986282857.mp4?token=WcTjnwxIgwrL5R2C5RwYUptNHz58Zip_dt8gUQJwsWVXmfc7CtFE0sP_En_8S2J8FgmYTFw5seaYGs1FgEb9k3MMY_KyQEtHImJMvK5J3UB7qtF81rzUr05_S4HFGUHbxLPUFSx5hjKJI0RyZUYahdNmD3cpJKhQRLoZ2edkKVYUNarCkf546okfuOidMvvIKhwkdO86RVJy4gvHbN0grZ2f2OjIejP4f8cL3pZ8R1ttWR4UVc3TxkkbuUE8M9K-_IBXm5metRU15DbN7kkKY9fsvaM8NlWmm7sIwx3wk2FfJGVJTqQwMDU-5S_BT05og4k2Mr715tROidWvpdd5JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5986282857.mp4?token=WcTjnwxIgwrL5R2C5RwYUptNHz58Zip_dt8gUQJwsWVXmfc7CtFE0sP_En_8S2J8FgmYTFw5seaYGs1FgEb9k3MMY_KyQEtHImJMvK5J3UB7qtF81rzUr05_S4HFGUHbxLPUFSx5hjKJI0RyZUYahdNmD3cpJKhQRLoZ2edkKVYUNarCkf546okfuOidMvvIKhwkdO86RVJy4gvHbN0grZ2f2OjIejP4f8cL3pZ8R1ttWR4UVc3TxkkbuUE8M9K-_IBXm5metRU15DbN7kkKY9fsvaM8NlWmm7sIwx3wk2FfJGVJTqQwMDU-5S_BT05og4k2Mr715tROidWvpdd5JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر پاکستان روز سه‌شنبه دوم تیرماه گفت که در مورد موشک‌های بالستیک نباید استاندارد دوگانه‌ای وجود داشته باشد و تأکید کرد ایران همان حقی را برای در اختیار داشتن آن‌ها دارد که سایر کشورها دارند.
شهباز شریف همچنین به خبرنگاران گفت که در تفاهم‌نامه مورد توافق میان ایران و ایالات متحده هیچ اشاره‌ای به موشک‌های بالستیک نشده، زیرا این موضوع اساساً در آن مذاکرات مطرح نبوده است.
پیشتر برخی رسانه‌ها از قول نخست‌وزیر پاکستان مدعی شده بودند که او گفته است موضوع موشک‌های بالستیک تهران از جمله محورهای مذاکره بین ایران و آمریکا است.
در واکنش به این ادعا، خبرگزاری فارس نزدیک به سپاه پاسداران نوشت که اظهارات نخست‌وزیر پاکستان، «کاملاً اشتباه و احتمالا ناشی از بی‌اطلاعی است».
به نوشته این خبرگزاری، پاکستان در حال حاضر نقش چندانی در میانجی‌گری این مذاکرات ندارد و اظهارات شهباز شریف بیشتر برای پررنگ‌نمایی نقش واسطه‌گری این کشور مطرح شده است.
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76628" target="_blank">📅 18:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76627">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ai_P6SqJ_OttwH929y13j8awGCBWyePUe3eNTaSjLkzbobofwVwMQlgfws-DWr6itm19LDG2qPNNwifKgLlgjcwA4jqrfOqdhnWTNDtfB5lccfb7B_o2XBl8FPVjYz36sD0S08DAcFX1EGHSBbHbR7rSCpg4KpGlhVo8nLEbaCLVBFX-tbp-m6sr_5fYNwrhPLtvqEUePR5Yn1XvR2BOe6NCu7cjFaGjqiMK-UUdSRIVwfp8fXWijj2p-p78VRRRpU31cdr-mJ1WDcu5ZxbXBjmZeVGnXCrpIO7PCBOy4yYrjshD360XZt-4htqmnfHIPyJRVGUJVjW5ky9dmdo47Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثریا طالبی، مادر امیرحسین موسوی، فعال فضای مجازی مشهور به «جیمز بی‌دین» که از آذرماه ۱۴۰۳ در بازداشت به‌سر می‌برد، می‌گوید پس از پخش گزارش تلویزیونی از فرزندش در جریان جنگ ۱۲ روزه، اتهام «همکاری با دول متخاصم» به پرونده او افزوده شده است. مهر ۱۴۰۴ صداوسیما با پخش ویدئویی از اعترافات اجباری امیرحسین موسوی، او را به «جاسوسی و همکاری اطلاعاتی و امنیتی با اسرائیل» متهم کرد.
پس از آن امیرحسین موسوی که با نام کاربری «جیمز بی‌دین» در شبکه‌های اجتماعی فعالیت می‌کرد، با انتشار نامه‌ای سرگشاده از زندان اوین اعلام کرده که تمام اتهامات مطرح‌شده علیه او «نادرست و تحریف‌شده» است. آقای موسوی نوشته که پس از ۱۴۸ روز انفرادی، بازداشت همسرش و تهدید به تکرار شکنجه‌ها، وادار به انجام مصاحبه‌ای اجباری شده است.
ثریا طالبی، مادر امیرحسین موسوی، در گفت‌وگو با «امتداد» با اشاره به وضعیت پرونده فرزندش گفت که امیرحسین موسوی از ۲۸ آذر ۱۴۰۳ در بازداشت است و خانواده او همچنان در «بلاتکلیفی کامل» به سر می‌برند.
به گفته او، فرزندش هنگام سفر به کیش در فرودگاه مهرآباد بازداشت شد و خانواده تا مدت‌ها از محل نگهداری و نهاد بازداشت‌کننده او اطلاعی نداشتند.
مادر این فعال توییتری همچنین گفت امیرحسین موسوی حدود شش ماه در سلول انفرادی نگهداری شده و پس از انتقال به بند عمومی، از او مصاحبه تصویری گرفته شده است. او مدعی شد به فرزندش گفته بودند این ویدئو صرفاً برای آرشیو ضبط می‌شود و در صورت همکاری، طی چند روز با وثیقه آزاد خواهد شد.
به گفته طالبی، در زمان تشکیل پرونده، اتهام‌های «اجتماع و تبانی علیه امنیت کشور»، «فعالیت تبلیغی علیه نظام» و «توهین به مقدسات» علیه فرزندش مطرح شده بود.
او افزود پس از جنگ ۱۲ روزه و پخش بخشی از این مصاحبه در بخش خبری ۲۰:۳۰ صداوسیما، اتهام «همکاری با دولت متخاصم» نیز به پرونده اضافه شده است.
طالبی با انتقاد از نحوه انتشار این ویدئو گفت: «فیلم به‌صورت تقطیع‌شده پخش شد؛ به شکلی که این تصور ایجاد می‌شد که امیرحسین در زمان جنگ اطلاعاتی را در اختیار دشمن قرار داده است، در حالی که او در همان زمان در زندان بود.»
او همچنین از شکایت خانواده علیه برنامه ۲۰:۳۰ و رسانه‌هایی که این ویدئو را بازنشر کرده‌اند خبر داد و گفت این شکایت در حال رسیدگی است.
مادر امیرحسین موسوی با رد اتهام‌های مطرح‌شده علیه فرزندش تاکید کرد: «انگ وطن‌فروشی به امیرحسین نمی‌چسبد. او یک فعال توییتری بوده و اگر کسی با ادعای ارتباط با اسرائیل برایش پیام فرستاده، بلافاصله آن حساب را مسدود کرده است.»
بر اساس اعلام وکیل پرونده، جلسه رسیدگی به اتهامات امیرحسین موسوی روز ۱۳ تیرماه در شعبه ۱۵ دادگاه انقلاب به ریاست قاضی ابوالقاسم صلواتی برگزار خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/76627" target="_blank">📅 18:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76626">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pLRIarr2kXyv99u8m4qMIoNOxZE9EP3KYqo059U02f7LHI8fOwqGvi2bpzU1ZTJdCnL251mQDUIStP88ANxmCxCSoQpS_qwXpPbLkrXQSiKX4eAPIN8GkGRxY-a-1C8ff4wTXynsAGnoXkyq0ZTe9IVodesMHARK4q1JTPae98CtoYlERhKPGqpAnPXsu-00SCh2P_Wqd2TscUaAbMo23BYcGOb54bA4YSh3cxfAFx9yPuBRj4QFdPZaal2EbBBcIRWDtQkbaMk8MMnGYLSsaPslIS-TO6IeTSKnr0uGp-u_9o54MjDD2oqTgzg5va3WmWNMJi7_HKAlbUDarZtgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/76626" target="_blank">📅 18:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76622">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O314dk-UMFJLn-Ru4vAcHkVHt_-e2TbE_wNJ6j4n6oZejHwzK8D7wi4curgACCwmykEoYTOyigdU4bt20Xtd8aIyLhq9YxzrlyKOMI4L1QA5aZl0XluX9mZ49aeyRVq7y1OsdqSKW-iX0O3Ksq6c1Voa6-7TSKWBFYmctH2Ahj7htq4mh1O5Q_L86Wjep5_WYaLJy-PPSxGhKKjFASDK8sz8844M0K74BuVVIdVhb0HLDIaqtmvzfl6YQyxkUrhwZsyr-9eORHJVh8Fnpcjb4noRz0ttIBqsIwzWTsrRQV-NdnTzNtTUn6kNpimCNHNIswqIYXYnehMtEquRF3Z0-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EO5PLb_Bwd1MuaLmKM5yTTCce0AFx6hC_WAD_dfnjLitYiiv0bK38EN6y-_b1m1ZBxfjJ8nFGkipYQm1AB25gJqhEl32O26IMNxVU0B8u5ar_5VOF5tWWdz5lDMxInyXMQh1o0dbL-W8LQeOAsUk4ankCRORQH_luJvIIqLJIYoGVJ9sLAvoirKzLNrADre9TsjzuUpDHHsZeL6gCCANcW3nZALUxRkNs_CajiWzg6w3DnLdsGoMxyPeUGK02gioZGf9_PT-JcNE0_EY0uViZbmcf-3Lv1BvoJzM2U4Jz7gNs2w9r6J7o3PGb4yi4RaNzRBue7xnGVAwcNI7QstfpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KvkW1jvbyOj2V1Xql-QxQ5GvDd5DHX5qq12LzFJ6wy2wNIY2IFhIMOTeLeS-AxyGpUG1FrIeQ2RB8ivq0o592lds8ElZgsie5G76rjVkow5Q0Q-_TwNwQ04MyszD0vLyFjgSHVLVRrk8rx3_0q-Qr8jRLB5BNXDWhRDW5sZQ_-s-WxNdG2l0dgG7o_pjChYV8T17w-Ah3Oba-fLWCiGGA-sy-VR30Gl3kTKiYfPNujAkGHt8M3y9vVTmg12YLe6gw4GvRZ-NjXzWtKYCtshLR5iJwqtnJy_wpTxkvPAbB2kku4555glN-CEA6_OqkLRAj_Ns0lG3eo3ZOmLBI0AFtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M36jKEW5kW4sA-hvdecs7KxHlS5QGQd4hpQCl2rTa1Wjwby8nmY3IulHN1r90DncmWM-SEnyzrl-N1X1icR8mHXF08AbfmTgk0IR5y4KsPkfamaK1tYDSZUzsC_57UnECsvyHVDiqeMODei6qOya8ov5hDWiQAm91avatgI_sDqIp_XOKD5zS7d3Mv0b4HU5NCGVfN55CIRKEyGyJH5C_wZQoRF0VIo9_LA7Fr9CK9yuZtZ45V2ZaOgyXRAZrG6mcfCdcyvDaNCtQm9UbBXTY5v3bfXotFdeIAGhwGlT5ogwB14Mf8ASOB4AsZnIOZEsF2Yt9wOYxK5bqJ47h1tOVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گزارش‌های کاربران از بروز اختلال شدید و قطعی در سامانه‌های آنلاین و پایانه‌های فروشگاهی (POS) برخی بانک‌های کشور از جمله بلوبانک، بانک کشاورزی، بانک ملت و بانک رفاه حکایت دارد. این اختلال‌ها موجب شده مشتریان در انجام تراکنش‌های مالی، خریدهای روزمره و استفاده از خدمات غیرحضوری با مشکل جدی مواجه شوند.
@
VahidHeadline
گزارش‌های مختلف کاربران در شبکه‌های اجتماعی حاکی از اختلال گسترده در خدمات بانکی چند بانک بزرگ ایران در روز سه‌شنبه، دوم تیر است.
بر اساس این گزارش‌ها، پرداخت الکترونیک و انتقال وجوه در چند بانک بزرگ مانند ملی، تجارت، صادرات و ملت با اختلال همراه است.
خبرگزاری‌های فارس و تسنیم، نزدیک به سپاه پاسداران با تأیید این اختلال‌ها از احتمال حمله سایبری به مرکز خدمات پشتیبان خبر داده‌اند.
در همین رابطه شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، با تأیید انجام حملات سایبری، گفته است که «شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است.»
این برای دومین بار طی دو هفته گذشته است که خدمات بانکی در ایران دچار احتلال می‌شود.
چندین بانک ایران اواسط خردادماه هم با قطع ارتباط و خدمات روبرو شدند که به گفته مسئولان دولتی به دلیل حملات سایبری به زیر ساخت‌های خدماتی بانک‌ها بود.
تاکنون گزارشی از عامل این حملات سایبری منتشر نشده است.
@
VahidHeadline
آپدیت:
پیام‌های مختلفی دریافت می‌کنم با نظریه‌های توطئه که فکر می‌کنند بازار ارز و طلا و...  قراره نوسان داشته باشند و نمی‌خوان کسی بتونه خرید و فروش کنه و...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/76622" target="_blank">📅 17:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76621">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YG2beWskw0P1v_urs3PGmuYik_4L7HwCQ-sNbTjMyeKhq2DcLH4WORM74cn88spV_23bExoawRqOW2cZjlap1egs8RJlZGCHhw2mY090vmikmjGd8usDBqci-_3ByeYFkkJFHTWvC01Ox7_TvEIMh7gx5nF-46exNlolq-nYaKp0Ipk3pg2yQ5DZKD8HZdYdho2i2KirJdnRVWYAMsBUlXOFWQkon-wTkso31RrutyapSa6iHSvC3lHvkZJotNHmXuspr1Mr9O-87MRpDYzyrOQw8rCD9KGu5YvF1znQGjGrUHQZp2hXcAHffRN1F_AisbTHjg3YwqwhSnGsQOwJOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمان و ایران روز سه‌شنبه دوم تیرماه توافق کردند گفت‌وگوها درباره نحوه اداره آینده کشتیرانی در تنگهٔ هرمز، از جمله خدمات دریایی در این آبراه راهبردی و هزینه‌های مرتبط با آن، را ادامه دهند.
به گزارش خبرگزاری رویترز، در بیانیه‌ مشترکی که پس از مذاکرات مسقط منتشر شد، دو کشور اعلام کردند یک کارگروه مشترک با مشارکت وزارتخانه‌های خارجه تشکیل خواهد شد تا این گفت‌وگوها را پیگیری کند و همچنین با دیگر کشورهای ساحلی و طرف‌های مرتبط رایزنی خواهند کرد.
این اقدام به نظر می‌رسد اجرای بندی از تفاهم‌نامه‌ای باشد که هفته گذشته بین ایران و آمریکا امضا شد و بر اساس آن، ایران موظف است با عمان و دیگر کشورهای ساحلی خلیج فارس درباره مدیریت آینده کشتیرانی و خدمات دریایی در این تنگه، که مسیر حیاتی برای انتقال نفت جهان است، گفت‌وگو کند.
این توافق پس از سفر محمدباقر قالیباف، رئیس مجلس شورای اسلامی، و عباس عراقچی، وزیر خارجه ایران، به عمان اعلام شد. این دو مقام ایرانی با سلطان هیثم بن طارق، پادشاه عمان، دیدار کردند و با وزیر خارجه این کشور، سید بدر البوسعیدی، نیز گفت‌وگو داشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/76621" target="_blank">📅 17:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76619">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GdIhd-HsgOwgAmc45_qYDS-adGeWvnPHdWGsB_DfXnJK14PtdSebWdMtTrQV_vqS00N0msEB5JWAGbkc4NZe09_6haeZyqTNSJ7XOyIX7XUFu8UdHCq8DIEZzAvi2VCBbX8QngyIpDvMn2k9-8em4wVrv7Fr5M-Fta7VIGBcesCxa-3QLxSIL0cmIeXfcqezjyPvLWRbio6QR5tnMsDtwnNgXg7w1Y5wmJ4RmDvkrn40RDYEWkwQL9RTHmv1RBCyMCiU0p6P7TNyWRsh24pW3kSiqJGtDKQ3pMBcASxcs5DbcxbhzelMWgUY-HJweUjsIi1BAiHHRZ0jZtjAVH_0ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31a8d92068.mp4?token=DhXz9ZcXYmaQlmPeQzFYB4kAH1F0AiS-bxlboF1lRmy6X1Mn4WpcB6ElqnsXSLhB_72nr52SHwhpfd3ERSt7d1sAqDmeqK6IWSuoLwgPFnBpAxEry1Qwc1lFlSeREbQJ_D7wUNvOB7ujFDiNg8bQLJ8dvJn3X4WJqj_9KWWdmY9euc1iK4ULr4i8XLOnu0O6LUNN5VzyZJlMwb__Ge8sxBZX9Dj_dsKxXOKoP7aBHPVoL1F0OSlmcSDgT3HDMIlX9Ldr8XSQa9uzdsbVhue6RcBkvtT8XFl_4nJSE3Q2cym5q-CTdXNonroN7vvHv9zROONssCcZrmpwS0kxAxnwcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31a8d92068.mp4?token=DhXz9ZcXYmaQlmPeQzFYB4kAH1F0AiS-bxlboF1lRmy6X1Mn4WpcB6ElqnsXSLhB_72nr52SHwhpfd3ERSt7d1sAqDmeqK6IWSuoLwgPFnBpAxEry1Qwc1lFlSeREbQJ_D7wUNvOB7ujFDiNg8bQLJ8dvJn3X4WJqj_9KWWdmY9euc1iK4ULr4i8XLOnu0O6LUNN5VzyZJlMwb__Ge8sxBZX9Dj_dsKxXOKoP7aBHPVoL1F0OSlmcSDgT3HDMIlX9Ldr8XSQa9uzdsbVhue6RcBkvtT8XFl_4nJSE3Q2cym5q-CTdXNonroN7vvHv9zROONssCcZrmpwS0kxAxnwcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کامران غضنفری، نماینده مجلس شورای اسلامی، در شبکه اجتماعی ایکس از برنامه شماری از نمایندگان برای «تحصن» مقابل ساختمان این نهاد در اعتراض به ادامه تعطیلی آن خبر داد.
او نوشت که «چنان‌چه مجلس بسته باشد، تا باز شدن مجلس، در همان‌جا تحصن خواهیم کرد.»
شماری از نمایندگان مجلس به تعطیلی این نهاد طی ماه‌های بعد از حملات اسرائیل و آمریکا به ایران در نهم اسفند ۱۴۰۴، اعتراض دارند.
حمید رسایی، یکی دیگر از نمایندگان مجلس شورای اسلامی، یکشنبه ۳۱ خرداد با انتقاد از ادامه تعطیلی مجلس گفته بود در صورت ادامه تعطیلی، همراه برخی نمایندگان مقابل ساختمان مجلس جلسه برگزار خواهد کرد.
حسین صمصامی، دیگر نماینده مجلس شورای اسلامی، نیز در پیامی جداگانه در شبکه ایکس، نسبت به ادامه تعطیلی صحن علنی اعتراض کرده و نوشته است: «بیش از ۱۰۰ روز از تعطیلی صحن مجلس می‌گذرد و نکتۀ تاسف‌بار آن است که در سامانه قانونگذاری، امکان ثبت استیضاح وزیر و صدور بیانیه مسدود شده است.»
انتقادها در این زمینه به خصوص از سوی نمایندگان نزدیک به جبهه پایداری با پررنگ‌شدن نقش محمدباقر قالیباف در مذاکرات با آمریکا، افزایش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 207K · <a href="https://t.me/VahidOnline/76619" target="_blank">📅 17:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76618">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0ZrJLRSrN9HdmNavPVUPqcLXhDC1NmbJ9BuP35kHev4xemKvxL9pdCk_kRobYjA9ovSpeR0Ot3ucqzMV2kJhk5vl93K7sbPNgMuMfs4rPxpvKETZb6nxbjDGRj-h2MN3wa743XUU8sadLKjBka33zJj67sMWIfqww55AcQKQ49jj3UH7S45MPSnS_A64L9B-RaoF32o10bLb2J0rbFdK_e2_nZ-qUxB4X8pqEI0Ir_1dw7Hyv2JGCHr3wIvIwrctJyWYKqBtLVmTGhPtoemHe6n1O4jVs0l8qi3hVqo9H2oKpX041d2Mb76CdGdPEEZFm3W5E8uu7ixf8M9NvS4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانون فیلمسازان مستقل ایران، ایفما، در بیانیه‌ای نسبت به احتمال اعدام علی صفری، بازیگر تئاتر و دانشجوی دانشگاه فرهنگ و هنر هشدار داد.
این کانون با ابراز نگرانی از طرح اتهام «محاربه» علیه او، از مراکز سینمایی و نهادهای بین‌المللی خواست تا برای نجات این هنرمند و سایر هنرمندان در بند، «فشارها بر رژیم ایران و قوه قضائیه آن را بیشتر کنند».
به نوشته این نهاد، علی صفری، بازیگر جوان و ۲۳ ساله تئاتر و دانشجوی دانشگاه فرهنگ و هنر در جریان اعتراضات سراسری ایران در تاریخ ۱۸ دی ماه ۱۴۰۴در شهر کرج بازداشت شد و «تاکنون اطلاعات روشنی درباره‌ی روند پرونده‌ و وضعیت این بازیگر منتشر نشده است، اما اتهام «محاربه» در تاریخ ۹ بهمن ۱۴۰۴ به طور رسمی به او تفهیم شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/76618" target="_blank">📅 17:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76616">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cjvyJthsCAuRZgWYvGLCYssFQU5GhQKGCBpIt1i0WPJVXMmXL4KDECEvpE_G6F8biVP6-yxJvV11vhV7AFzAAHZFZUW35MUkVkrJANtSOBULxOYgNAuYSJac63O_QKNWF_h4DJKOe4uCxQ70ARsrfO5APCrhonj42MzW_s8Vi9RsbKhb20ja1dMOOYs4SVerY6ppKVypWYVCUXhvgWSnI2CvBKmxI6INYgqe2Lgz4ohEJCV-lCDQ41S5vXBvKC6o_sM-egSOCThbWGcd4N3Lkk8r7WbjFGw7KpmjfD8Il-8hnE-U_R8Yqn5eLs9ktu6GStZ3Tq4rm-384pKn4yQMwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/11113460cd.mp4?token=ZKoUepa435cpmMl1NZxQs3jMhOy5ckcSso0EOh9KOSTFl_DVtV-tswtEGU8FqJM8Zl5RgCxV0gqDMhfxQIwkr7SRa2UYgmeNRSrDOowKtdaT3HYXSndOWHB768rUG5knczQS-bXEzKWhA5lIS9dNn2WSU29XpXJRuOlRA70nofGTVOFyfpW1ns2L3zKEE1qAjsZF6nov_In80RefvXcC5ir76H2v8snVebp2SsHTRssYmTdXh6Ej-3v3l5MuXAYeStCJxHWT9eYHAMayiUHhhC5VJmNd2wgRtMxkrW-xbp6As-8hkyn2tiIX1OkUSC6-_WAd57iJZ4hqRwN0x5l6uA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/11113460cd.mp4?token=ZKoUepa435cpmMl1NZxQs3jMhOy5ckcSso0EOh9KOSTFl_DVtV-tswtEGU8FqJM8Zl5RgCxV0gqDMhfxQIwkr7SRa2UYgmeNRSrDOowKtdaT3HYXSndOWHB768rUG5knczQS-bXEzKWhA5lIS9dNn2WSU29XpXJRuOlRA70nofGTVOFyfpW1ns2L3zKEE1qAjsZF6nov_In80RefvXcC5ir76H2v8snVebp2SsHTRssYmTdXh6Ej-3v3l5MuXAYeStCJxHWT9eYHAMayiUHhhC5VJmNd2wgRtMxkrW-xbp6As-8hkyn2tiIX1OkUSC6-_WAd57iJZ4hqRwN0x5l6uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز سه‌شنبه دوم تیرماه بار دیگر تکرار کرد که ایران با بالاترین سطح بازرسی‌های هسته‌ای از تأسیسات خود موافقت کرده و این بازرسی‌ها «تا ابد» است.
دونالد ترامپ در پستی در شبکهٔ اجتماعی خود، تروث سوشال، نوشت که با وجود اعتراض‌ها و «ادعاهای نادرست» ایران، و «هم‌زمان با جار و جنجال رسانه‌های جعلی که هر کاری می‌کنند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهند»، ایران «به‌طور کامل و تمام‌عیار با بالاترین سطح بازرسی‌های هسته‌ای برای مدت طولانی در آینده (تا ابد!!!) موافقت کرده است».
به گفتهٔ او، این امر «صداقت هسته‌ای» را تضمین خواهد کرد. «اگر با این موضوع موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد!»
نخستین بار، جی‌دی ونس معاون رئیس‌جمهور آمریکا بود که روز اول تیرماه خبر داد ایران با بازرسی از تأسیسات هسته‌ایش موافقت کرده و این امر ممکن است در هفته جاری رخ دهد.
با این حال، مقام‌های جمهوری اسلامی بویژه سخنگوی وزارت خارجه ایران هرگونه بازرسی آژانس از تأسیسات هسته‌ای را رد کرده‌اند.
@
VahidHeadline
پست‌های ترامپ، ترجمه ماشین:
با وجود اعتراض‌ها و اظهارات دروغین آن‌ها در خلاف این موضوع، همراه با هیاهوی مداوم اخبار جعلی، که هر کاری می‌کند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهد، ایران به‌طور کامل و تمام‌وکمال با بالاترین سطح بازرسی‌های هسته‌ای برای مدت بسیار طولانی در آینده، یعنی تا ابد، موافقت کرده است!!!
این کار «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این موضوع موافقت نکرده بودند، هیچ مذاکره بیشتری در کار نبود!
بر اساس این موضوع و سایر امتیازهای بزرگی که ایران در حال دادن آن‌هاست، من موافقت کرده‌ام اجازه بدهم تنگه هرمز باز بماند، بدون هیچ محاصره دریاییِ دیگری. با این حال، همه کشتی‌ها در جای خود باقی می‌مانند تا اگر لازم شد، محاصره دوباره برقرار شود؛ چیزی که در حال حاضر بسیار بعید به نظر می‌رسد.
پول و/یا تحریم‌هایی که وزارت خزانه‌داری آمریکا آزاد می‌کند، به حساب امانی منتقل می‌شود که تحت کنترل ایالات متحده آمریکاست و صرفاً برای خرید غذا و تجهیزات پزشکی از ایالات متحده استفاده خواهد شد، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما.
این‌ها چیزهایی هستند که ایران به‌شدت به آن‌ها نیاز دارد. این یک بحران انسانی است و من احساس می‌کنم لازم است همین حالا، پیش از آنکه خیلی دیر شود، کمک کنیم.
گفت‌وگوها به‌خوبی پیش می‌رود!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد؛ رکوردی بی‌سابقه در تمام دوران. قیمت نفت به‌شدت در حال سقوط است و جهان جای بسیار امن‌تری شده است!!!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/76616" target="_blank">📅 17:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76615">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M9GwX2DnOY-NzLvoCrbtntvC1jAYZpws-6wasI3-TLA8TYUdrQesMhKslyP5fh9ewmP8cbT8Z6LNJmKybhOzueJCIEVW_DZTLiCP5_oQ_BqNbPKpQ6ie4RtwVUN9Tp01sjYM4qMPzEOrrh6UsT7-T6iZSO2vbPmjcLDvZOTHI-4xfH-PlJPw0ARydjwspJ0X4fXP7JjzZhiyqWJX8bvGlzw4u9QTI6AELXxczw_MSAig7MPL4PJ5NNa1VI2hqRqSItXd2DUR7jPtew5rGDZirOfdvN6imyxakANQJ9U5YqD8IZAQoUh2FSMsxsLJRfV72FhQfTJ_p1Vbn1xqmI0gSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر سه‌شنبه دوم تیرماه گزارش داد قیمت  [نان یارانه‌ای، نان یارانه‌دار] در تهران و ورامین افزایش یافته و در برخی موارد به حدود دو برابر نرخ‌های پیشین رسیده است.
بر اساس این گزارش، قیمت‌های جدید از سوی استانداری ابلاغ شده و از امروز روی دستگاه‌های نانینو در نانوایی‌ها اعمال شده است.
بر اساس نرخ‌های تازه، قیمت نان لواش به دو هزار و ۷۰۰ تومان، بربری به ۱۰ هزار تومان و سنگک به ۱۵ هزار و ۵۰۰ تومان رسیده است.
محمدجواد کرمی، رئیس کارگروه آرد و نان اتاق اصناف ایران، نیز افزایش قیمت نان را تایید کرده است.
در ورامین نیز رئیس اتحادیه نانوایان از افزایش ۹۰ تا ۱۰۰ درصدی قیمت نان خبر داد.
بر این اساس، قیمت نان لواش از هزار و ۴۰۰ تومان به دو هزار و ۷۰۰ تومان، تافتون از دو هزار و ۳۰۰ تومان به چهار هزار و ۵۰۰ تومان، بربری از پنج هزار و ۳۰۰ تومان به ۱۰ هزار تومان و سنگک از هفت هزار و ۴۰۰ تومان به ۱۵ هزار و ۵۰۰ تومان افزایش یافته است.
مسئولان صنفی افزایش هزینه‌های تولید، از جمله دستمزد کارگران، خمیرمایه، حمل‌ونقل و اجاره‌بها را دلیل این افزایش قیمت عنوان کرده‌اند.
رئیس اتحادیه نانوایان ورامین نیز گفته است اصلاح قیمت‌ها با هدف ادامه فعالیت نانوایی‌ها و حفظ روند تولید و عرضه نان انجام شده است.
این افزایش قیمت در حالی اعمال شده است که نان از مهم‌ترین کالاهای مصرفی خانوارهای ایرانی محسوب می‌شود و در برخی اقلام، نرخ‌های جدید نسبت به قیمت‌های قبلی نزدیک به دو برابر شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/76615" target="_blank">📅 17:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76611">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HWn3raMoWajPGXAwI2Rdv_sJzV4RmaQNJx0cQZqF5DUI-iG8Q72ywcV0fE28enLfm9y-OBTnTJ6e-1ETlh6rafbvp8EYMYGO7xsnReNurEci8MV9jKNNUdThidWkte1AoIgUMq-lciDxzzGkYiEoSOWUEPpXGl9gaQuL4snTYuKKF3vNDaRe5qMolRPG060Qk87RdHkNTFRJ3P8By6rbiRHK2lSawyN6VSs98_ExjJ2X8ZAeDIaxkinDJxHnv5ys8qx43yUIOjZ-l0I3SIoLs1yMc7hq6WjQrGAFiL4r-PdYHooHjrR0U_WZ26ScfI7WmC7U3j1QviPnYjstGI21Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XAItGqTBIspc0EBg6vtDiTN_CvT679E9Kze6NEpW25NOSgKLvUkLfGtDBdiukjf_U-8sB9hc7OBPyBWhIyegkOb4UoNfRgdGH6Y1tUEdhr4slBai5nhfW028rm5v_Xa2LnhNUamF8bvHY6EaK3B_s4JcGfPHO_GX7EEvKHNbFDjWD3aC38Ar9VVApJcgtZkxu7XcOrh__BKcp6hi13qeu6D8uRZBlzqq8FxkBR5GMsHcQuMEj6rLy-q14Mr3JSqZFH8xxgmmh_HFEpMinF4MQlGMkCagj83S_BGtx1fg7CwEyeP5fJKNoJCVoWCMRctQi1W4PbKJhf6cW0l8RbJTyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iqTi1nteVAJUY9uV_SeX-qiyJEGwQIjdflmmjBRBiCNIwExwUfZufy-YPJPj2EEcdwV7pU8C0T1T0jfd88AvyCkXyKJN6fEu7oJyjRFBd0v4t8EoQQ0r69rafmMxNoNrcYqzXcOHaoIQ7HyqugdqSrt-9PvXD04DUsfl3mvsqjNC9kWkUCKQtdSiOlHHFvpu2Jmi5HJRu3xHaWNIK7coeGGxYfeFFOU4NR3Gh7IqFheZUr-msulojwsV_APDZsYiBgWCBnUc2JywhWb46-CQtq6s3fpDBoaJmrdqj7o-IBHjgdjF6N039uiIsUS9DU-3paQmSIpiYTEuwZadKusPQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b0b4e3582.mp4?token=SXElRxYGPNNHEreE8uBI9_Uoo-7tDb6_0gqF2ZSJ5gd5VTMwInlzUpY5Kn647sZKq3Q21-JjxjCQHwLbNeTerUbYN8eld0KX6_W6X3dYncKIJJk9kfmZJ24Z0VB_Dfrv0S9_isWQdSP9Vha6fv-7i29Yk4u0mfav2IsQKCeBxUhh8u6ppo91jxCuJoB32O0-03hsQxRF9N8UrdQHATKG0m64-APnh5ThxSp7XcM_ioEudpmry37CcTNpq3f5X-TRZFCemi0rcgsMGgcHIsnfoDpg214L7MeoP2Z_wloioAVt24p8uVEyeiL4oZED1HubqMQpnswuVNPVw43FgA5NJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b0b4e3582.mp4?token=SXElRxYGPNNHEreE8uBI9_Uoo-7tDb6_0gqF2ZSJ5gd5VTMwInlzUpY5Kn647sZKq3Q21-JjxjCQHwLbNeTerUbYN8eld0KX6_W6X3dYncKIJJk9kfmZJ24Z0VB_Dfrv0S9_isWQdSP9Vha6fv-7i29Yk4u0mfav2IsQKCeBxUhh8u6ppo91jxCuJoB32O0-03hsQxRF9N8UrdQHATKG0m64-APnh5ThxSp7XcM_ioEudpmry37CcTNpq3f5X-TRZFCemi0rcgsMGgcHIsnfoDpg214L7MeoP2Z_wloioAVt24p8uVEyeiL4oZED1HubqMQpnswuVNPVw43FgA5NJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«امیرمحمد هموله» ۲۴ ساله، ساکن شهرک صدف شهریار، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ بر اثر اصابت گلوله به ناحیه سر به شدت مجروح شد.
او پس از تیراندازی به بیمارستان نور شهریار منتقل شد و حدود ۵۰ روز در کما تحت درمان بود، اما سرانجام در روز هشتم اسفندماه ۱۴۰۴ بر اثر شدت جراحات جان خود را از دست داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76611" target="_blank">📅 17:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76603">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Hs-FkuVBu53KdfPl-tRDcIKtDlqPm6zxbdOFMR7GZQMqAzrjXpk8ngDwLP3wSShozn2ts0a5rL58nWfRVefMZIzTdO-CB4JqXDLSCZR1U9xHZQfb5Mkz8xoMxhTwlykZRK-erQcZCjim4-GzdZdjNV4WNX-HULKuaHTLDB7H_pjCKXC3T-ugunXZGs4H8rsG0Pqc4u2Y_o-goikPt-VI9J4re7Hgda0RJcXuZVEFjoBMJU8pMcCcbfjOvaZmhsaokrTe9oPzeny5DbpIa1sLnuVAvZGMXw7diyJ4ZhvYxWGGENGA4WPUihMHMhk5mEHm6M1UvV2apMg_gTzdHQ8VLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V0sf8n5vOL1D4oG4XZ7JSjeUK3wICqqy4njTF0cLv1A2A0cucHt2sTus9Tid8Nz1JPyEGfLWWCOdLuhMm7CLtyESudvHPGgJTKlVyjRbobaSQUEcC2mZyFIzSmmVSG3VNyynmfd0z5Ujpsf7mbw56-u3zbKn5ObQxeyKRFKkHexe46gNkQD8oKZeKwm-yjDwoxo9uHQOJ-d2HyExjNDD_WNR4cBlh3ZfUihJ0xqCVB8Q_WG6JhBBTUZ9xuu2gDgyBlPozQCmMR2-FMgSCs83YY9E4iLlBRko3gdKJW9acnE3H3DParRPnJVDVGd_fJHyZGopd6wlcbEbwMyKNQoDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X-bdoIxEAoggI-VQU1etfEds2eicfl34yAC29yQaCfrbcgKxlb8UPex5UPi5CHjZ8eZOEy7uoKzFdpzvAvx-tpYgd0JdvCiwCHxGtMbskGXZzApVEAujW3gOw8Sw-QbKpgm0URtDM_vfHZ21zHy1OeOsAjzska4Ankee7rVBYZ8Rxq_63d1ccHJbMXzKdh_DMv9FZOyREDXdxSbo-u3RFKBMcvzuRRxSmYiQEmLGKAA6g1282dsocrS0bcdK5UwPw9LbmzxfaB-QWB8OHbubKBr7eZWmd2jYBIale2ftzetCCjwPuDu0iBiNdaGnt-7AHRItZTrKVLxvqQHgCBPuqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tVHFDLlFwJpMZdbJB8rb_uwAJwr6hbZY8DhlVRNpaCoFGTXCYDj0qrJfF9mY3i9o3q28C7A99h-jgXcskMG4SSBISxOdWtomitrruF7PLXsy_lX7eTVFEiDQbaVw3SooQv8DALXR3XF5197WEaAKY1T5esMW7hhfjKpzXlXqEqpzRnZCyxH0P1ieSQnJXGLnv6LrHPEdwSYKHwJfvqmthoJ_OaEgWdv_QV6u2BmrvR27u76A8O6gEVOIFmoqAvTnQcaQdp_mHsjUKs1lxU-Ek5Zblt56uffmMlkKCYckJ86oDDVsP4uIrVDssPS5iYDJCbhe_iL4JndtekAdiV7AMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vKd-1G6s4UOr8MIxahBoEfNaKMxlXQ7pJucZ5SxsxY8rRCatdmhL_L9XRlBk-Q0so7fe0D7v-a6z_X4o1QyvG_90vGUUtG_4pxtZM5nOBZsEhFUlvBQall_8CcMETq3MODpq6SUgyvmzcs9IXEMm9P4s546qi1t9UHzAV_6-xo1QPFrwF7sMLQKzc2YJ0poyXFZGHzPdI2gIOa58PeGOTyrdysaQVrVry-PmHW84pdIPOULmlOQ19JcF_KN9JJYqru92SL9WZ5a6jZ541SrIi-dyKFLITv0EgOmtr5IWZ14VwZfA4GpAMiLZixosTQybgNh6fkqCLzmvBGhsIOzYsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f17OK4BSafM19wiGHgaG_pX8YplNuSULuX21n-Yopm_Zl-0JW06YMPRqStlT_Aqj4_ZjWQ_7-TD-pVStgN0diOxuw4adl-edJluiCXrkCv-iHyyn8_Z79SmzG1IDTEdIsHLbQilzhhtv8WMvJwiHm3al_mhH3kDDoxA2vpIo4-kb-pr0jhupwf8NBfI5APpOz7U7qd7TnC5RN36CdLuhPgGS4UFeuZbzfQHrEzAdOYnDfF64_e0thxPf0O2W0WrrU-w-0rm1frGHSGGwVy-DJ5oKsis8Ym6zcaqkqw0VNVE_fn1WMMaG4YbuzTit6vbgfedZTU62T9hwnwUihK0JTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T_NFewh2kMocl8Oy232KXrxUkofvNMEqdUEUH45COgSwyhHDRFLdNSn9iCYM25LYoAo8W_VnvoN8DdaQjxsMe4UG74tWoq0sVSkWHqY8TNRN-pgSr4pxUEI98qZmalCePDylr04rmmJ2OmzKm4re-7Z0jEZ3rVIPKCumdJmNU1PxB-Ujdss3k8siyuH5QaroQ0mjoiM_FX7k241rcKMfYvcxWJkvHRt0KiKPb9g0gjyDR_E6IxmczgOyAsGWO3GcOGZRpAbxXmSvvhYL14cvF9RvKwL7OaCqFzIWa1i8dD3KxfC-MkQLAFnhAb80kiDei8oxyOdPjd7SOzDr0DiYnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D5kqo2gp4gq5I8fuf5iw8EonFaGoicpZBHktA-F9FKIZSoz1wNfxOb2bIrsv1owZ57HpVGp3DpP9kJSlg_t7xxK_VKfHTRoQkpRkBYOso94UkE1nxthjiGUkebp76rAt4nvQAI3LduJ_NjfCWrnA6PfukQrXUmUnaEFR2rO0R0EUy_V7ieZgVRa8U1Bpef998VT7jBe3tsfuIt4tAihq7tm9_gDtvutJtTqMc5e6vmFwvJ4zSf48Xkn8SfKYLFrzawvQIsT2quj6tBwC_cIw89Dg6qBeJOF9r33v8zUapATxxDVA0CeN8wGcz_HpqPAl6IAjghR2Qiky3dHen9Iv-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ پشت سر هم پست کرد + ترجمه ماشینی
دونالد ترامپ، رئیس جمهوری آمریکا، دوشنبه عصر نتایج چندین نظرسنجی مختلف درباره توافق با جمهوری اسلامی را منتشر کرد.
از جمله یک نظرسنجی مشترک «سی‌بی‌اس نیوز» و «شرکت یوگاو» می‌گوید که به عقیده ۸۰درصد جمهوری‌خواهان، این تفاهم‌نامه «بهتر» برای آمریکا، و یا «خوب» برای هر دو کشور، است.
در یک نظرسنجی دیگر، ۶۷ درصد می‌گویند از تفاهم‌نامه اخیر صلح میان دو دولت حمایت می‌کنند.
در نظرسنجی دیگری نیز ۴۷درصد گفته‌اند که این تفاهم‌نامه اثر مثبتی روی نرخ تورم و توانایی مالی خرید مردم آمریکا خواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76603" target="_blank">📅 02:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76602">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXP4rleh7dgvyIw7SEX5BuwczHOmD2W7wK7SXwcrw04eJCKvowHLOXehrmduudU-YBD3n-5AF4QVllP36SP_YWzeOOSMJbHMHIcBRirlbDJzYaXl6GWov1zDjCmKXKBdL8pFrAu1n-FzXEoHllFK4xxVLENEheVt0TTyHbtxLIOR2CtcNEtnIoExljLi7GX7xgYMhnCxhtzBaDFWiI5ljJkA7d8qGdXg1nYvm6UYqFDxWyScECyR2QFCd-cmJv3IIA8DJsSrpBPIPtUz-pgmGL41p3_HZwM9nnWvR3ZT8ueIgY2XPENcSiHhKlnLYj0WtW_kQURH-fXmB8dCML2-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، سرپرست تیم مذاکره‌کننده جمهوری اسلامی ایران، در واکنش به صحبت یکی از مجری‌های صداوسیما با انتشار پیامی در اکس نوشت: «در یکی از برنامه‌های صداوسیما دیدم که گفتند کاش فرودگاه مهرآباد را می‌بستند تا تیم مذاکره‌کننده به سوئیس نرود. به آن عزیزان می‌گویم اگر به سوئیس نمی‌رفتیم، هر لحظه خون بیشتری از مسلمانان و شیعیان لبنان ریخته می‌شد.»
پیش از این، روز شنبه، یکی از مجری‌های صداوسیما گفته بود: «در کنار بستن تنگه هرمز باید فرودگاه مهرآباد را هم می‌بستیم تا مسئولان برای مذاکره نروند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76602" target="_blank">📅 02:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76601">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ: اوضاع ما  ‏در مورد تنگه هرمز خیلی خوب است.
‏دیروز نفت بیشتری از هر زمان دیگری از تنگه عبور کرد؛ بیش از   ‏هر مقداری که تاکنون از تنگه عبور کرده است.
‏احتمالاً این را می‌بینید.  ‏ما با یک فوران نفت روبه‌رو هستیم.
‏تنگه کاملاً باز است.   ‏این را می‌دانید.
‏خواهیم دید همه این‌ها چطور پیش می‌رود.
‏اما ما دو چیز داریم.
‏ما یک تنگه باز داریم و کشوری داریم که   ‏هرگز سلاح هسته‌ای نخواهد داشت.
‏هیچ‌وقت، هرگز، سلاح هسته‌ای نخواهد داشت.
ویدیوی بالا:
به تشخیص ماشین، حدود ۱۱ دقیقه از نشست خبری ارتباط مستقیم با ایران داشت.
متن فارسی اون دقایق
ترامپ در پاسخ به سوالی در مورد تنش‌های احتمالی در تنگه هرمز گفت
تا زمانی که ایران به ما احترام بگذارد، نمی‌خواهم بگویم از ما بترسند، تا زمانی که احترام بگذارند اوضاع خوب خواهد بود. 8:15
@
VahidHeadline
دونالد ترامپ، رئیس‌جمهوری آمریکا، دوشنبه عصر گفت اگر جمهوری اسلامی «به توافق خود عمل نکند یا اگر رفتار مناسبی نداشته باشد، من کاری را که باید انجام دهم انجام خواهم داد.»
5:00
ترامپ: نیویورک تایمز جعلی گفت، اوه، وضعیت تقریباً همان چیزی است که چهار ماه پیش بود. نه، چهار ماه پیش، آنها یک نیروی دریایی داشتند، دقیقاً ۱۵۹ کشتی. آن از بین رفته است. کل نیروی دریایی از بین رفته است. آنها ۲۵۰ هواپیما داشتند، همه از بین رفته‌اند. ضدهوایی آن‌ها از بین رفته است. رادار آنها از بین رفته است... همه چیز از بین رفته است. رهبران آنها از بین رفته‌اند. کل کشورشان از بین رفته است...»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76601" target="_blank">📅 00:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76600">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=cLZ7ZWlz6QWxGTgH2mR097FWg6PkEA8-YJGFP1CD0eQj3KTgbemFfS6TVMsm2xdhcE2eDC2SQDsgcrucR9mzqVXJaGx2Mu_U5ElkdLMhiq_m1kDTvtC_mF8bYaKZlzdPujC_u3MVOMbUZfiVohVMku5nrpLUs71_VwhEuuOOAn9siYEHp8qNJqtwPtQ4A6UdDcoh6oDGkwcuw1HgUVbXQohfjrDfrfHbM_8pVJxnHrEYzNpGykoknImnsrKV5r-tCcpIW_AHUoeIk2NbtgIHJ3D_gmNH3rY-X5j7KZWWGZ2m9bdL6LS7pHPfB8M7GUL2ALQZ5Z0nMPXtXxayBh2MtA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=cLZ7ZWlz6QWxGTgH2mR097FWg6PkEA8-YJGFP1CD0eQj3KTgbemFfS6TVMsm2xdhcE2eDC2SQDsgcrucR9mzqVXJaGx2Mu_U5ElkdLMhiq_m1kDTvtC_mF8bYaKZlzdPujC_u3MVOMbUZfiVohVMku5nrpLUs71_VwhEuuOOAn9siYEHp8qNJqtwPtQ4A6UdDcoh6oDGkwcuw1HgUVbXQohfjrDfrfHbM_8pVJxnHrEYzNpGykoknImnsrKV5r-tCcpIW_AHUoeIk2NbtgIHJ3D_gmNH3rY-X5j7KZWWGZ2m9bdL6LS7pHPfB8M7GUL2ALQZ5Z0nMPXtXxayBh2MtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی دی ونس، ونس هنگام ترک سوئیس، ترجمه ماشین:
🔸
سازوکاری ایجاد کردیم تا مطمئن شویم نه‌تنها تنگه هرمز باز است، بلکه باز خواهد ماند.
🔸
قیمت بنزین همچنان کاهش خواهد یافت.
🔸
سازوکار درستی ایجاد کردیم تا آتش‌بس منطقه‌ای تضمین شود و درگیری‌های اجتناب‌ناپذیری که پیش می‌آید مدیریت شود.
🔸
ایرانی‌ها اجازه داده‌اند بازرسان تسلیحاتی، بازرسان هسته‌ای، پس از مدت‌ها وارد کشورشان شوند.روشن است که ما این رژیم بازرسی را تقویت خواهیم کرد تا مطمئن شویم آنها هرگز به سلاح هسته‌ای دست پیدا نمی‌کنند.
🔸
بخش زیادی از تیممان را آنجا گذاشتیم. ایرانی‌ها هم بخش زیادی از تیمشان را در آن اقامتگاه گذاشتند تا کار را ادامه دهند.
🔸
این دارد بنیانی می‌گذارد برای چیزی که می‌تواند خاورمیانه‌ای واقعاً دگرگون‌شده باشد.
...
خبرنگار: آقا، خیلی سریع؛ دیروز لحظه‌ای بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما دست ندادید و بعد او از اتاق خارج شد. آیا احساس کردید به شما بی‌اعتنایی شده؟ آیا فکر کردید این کار از طرف آنها عمدی بود؟ شما آن اتفاق را چطور تفسیر کردید؟
باور کنید، در چند ماه گذشته زمان زیادی را با ایرانی‌ها سروکار داشته‌ام. گاهی آنها را به‌عنوان مذاکره‌کننده‌هایی بسیار گیج‌کننده می‌بینم.
اما ببینید، ما یک نشست خبری کوچک داشتیم.
آنها آشکارا در ایران از همان حمایت‌های
متمم اول قانون اساسی
که ما در ایالات متحده آمریکا داریم برخوردار نیستند.
ما با شما صحبت کردیم و بعد چند جلسه واقعاً خوب داشتیم. چیزی که برایم کمی خنده‌دار بود این بود که بعد از آن جلسه اولیه، نوعی توفان در شبکه‌های اجتماعی شکل گرفت که همه می‌گفتند ایرانی‌ها می‌خواهند بروند. و بعد ما حدود ۹ ساعت دیگر با آنها صحبت کردیم.
بنابراین فقط به رسانه‌ها توصیه می‌کنم کمی به آنچه از شبکه‌های اجتماعی ایرانی می‌بینید بی‌اعتماد باشند.
آنها می‌توانند مذاکره‌کننده‌های گیج‌کننده‌ای باشند، اما احساس می‌کنیم در حال پیشرفت هستیم. ممنون از شما.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/76600" target="_blank">📅 22:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76599">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sstfUxOMtxenrDYTAM1RdMOB9RekrnPGuQvDzw7F_zGNZlkuIv7gv_5u5u4urV9Z2pC-4-2QMmSpsA2lrxMCjB3k16oktauPctDjXafSAXy-5hArr7kViqZYSmmai7qz8Urz2aZQpHpNzy9FjCaEfmimiDxiHQsRSxYCwl0KJrp1v8NcFHGirsJwzQAi0JuP9-sXp-S-vYmjHB8N8I5rnib_iCjV4Cy90UMTr8zZ6kieHWAlbROmKYp3bNJXG0ELeSKjKjsGA6ykCNTfHyzWky4c899uINYT1AMphZp8YimKjpPAwvCh7Zi96sOsETLsgyxEPh5b_8jT5CDeFlVCtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
همه کاملا آگاه‌اند که ایران موافقت خواهد کرد که برای تضمین «صداقت هسته‌ای» در بلندمدت، بازرسی‌های گسترده تسلیحاتی انجام شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76599" target="_blank">📅 20:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76598">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFHQK8rnDJXshLtJ832wLDKq6NnEdH7GIiABkTOi9KaWJG14HHSOG525zeRBYf2y2-tV2tmFCeitt-k849bRDb357bwSxY4ufoxJnxNGOgAv3-Xnm8Hw15p1KgHE1XYKwz0k-6CA3iyLIeEgsOIyMv3QnN1InmAxGjv0GJt7VFIjKXDyIITydSe23Da4KQm_AW8zI60ZHmdHSjNqKG5egOJWM3QzMAw4fcP59mvdsHeThJU0BYHzdQOhaYnetzB8O-UtmNeXpyT_i-hpts7WlCw74mKD6QhUhBOt1oUNEq0KRoVoJ89T-nb0oROyig5w3zqv8D2qLtywRkpdKox6gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز دوشنبه، رسانه‌ها خبر دادند که محمدباقر قالیباف، رئیس مجلس و رئیس هیئت مذاکره ایران، که تازه از سوئیس به تهران بازگشته بود بلافاصله برای دیداری دیگر به مسقط، پایتخت عمان، رفته است.
به نوشته روزنامه هم‌میهن، قالیباف در سفر به عمان به همراه عباس عراقچی،‌ وزیر خارجه، قرار است با هیثم بن طارق، سلطان عمان دیدار کرده و در زمینه ارتقای همکاری‌های دوجانبه و تشریک مساعی «برای تثبیت ترتیبات ایرانی»‌ برای اداره تنگه هرمز گفت‌وگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76598" target="_blank">📅 20:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76597">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eyG9I5N2h_XGbLYWFNE5KbWqT-cbrP_xYfucGYuQUgt98RU4539yYA4ZFHNk0phL9Vs7-G6igg70BGtFtE5PaQ5l1JvwLejWAw-6KVkJQq2hWRTHGnLz1YrhVyk9jncGh6nSI3sSGTf1dF8cgFQ5u3fK3mnpbk--UBPjDxTTI7Yq5PKv3o0qL3EuyQ9N1KZ3qWDRQwSt6XYLk967pxMHnooZ3eaOciawsdnARi0J3FCQ0feAxMz66jP6T2wINCBei74D0rK7Kerw78IxtJrN6l5xTHRdr5Dtm0acUNPwC6uNSuiPXj8Vc-PG6jRBGLhPyYJwj60Exe9KXPC2aHyAYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک منبع آگاه نوشت اظهارات جی‌دی ونس، معاون رییس‌جمهوری آمریکا، درباره بازگشت بازرسان آژانس به ایران کذب است و در مذاکرات سوئیس هیچ صحبتی درباره حضور بازرسان در کشور نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76597" target="_blank">📅 20:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76596">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f94ec11a35.mp4?token=pFKdOl0eH3eqe3Ovv499_GkneKkZOLDYZnVcphEp-Us4XRsST_BVPBXTGxDqDU6tqsEnjpiO0iRLq7wZQKvmyWLrmOUrtf7m49SclR2YeKp3Mzy9gKSSrgBk3wuveguJ6FdUD8YNPt4KZjBx_wNlDjiLHHqcowM1EBddjjA3AD3Oj4wEZcnv3jbowlqLYwJG-dbNtI9QSsED6kBjm-Ri5Dxp-_zPGFavpoSHmmxH8i5US5hDO_ynJEpwA4DdDEnZhSVv-geAnTXELx_-weXaVfthd4sekxnbBUg26NGf43KesSbSGywQNC7pDT9wQB1WA4plrU32xerP9yQlBxL07A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f94ec11a35.mp4?token=pFKdOl0eH3eqe3Ovv499_GkneKkZOLDYZnVcphEp-Us4XRsST_BVPBXTGxDqDU6tqsEnjpiO0iRLq7wZQKvmyWLrmOUrtf7m49SclR2YeKp3Mzy9gKSSrgBk3wuveguJ6FdUD8YNPt4KZjBx_wNlDjiLHHqcowM1EBddjjA3AD3Oj4wEZcnv3jbowlqLYwJG-dbNtI9QSsED6kBjm-Ri5Dxp-_zPGFavpoSHmmxH8i5US5hDO_ynJEpwA4DdDEnZhSVv-geAnTXELx_-weXaVfthd4sekxnbBUg26NGf43KesSbSGywQNC7pDT9wQB1WA4plrU32xerP9yQlBxL07A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تا وقتی که لازم باشد در جنوب لبنان خواهیم ماند
بنیامین نتانیاهو اعلام کرد که موضع و دستورش به وزیر دفاع اسرائیل تغییر نکرده است.
نخست‌وزیر اسرائیل نوشت: «نیروهای ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم علیه خود یا ساکنان شمال را دارند.»
او تاکید کرد که ارتش اسرائیل «هیچ محدودیتی در این زمینه ندارد.»
نتانیاهو بار دیگر تکرار کرد که ارتش اسرائیل «تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهد ماند.»
در مذاکرات ایران و آمریکا در سوئیس، هر دو کشور تاکید کردند که حفظ آتش‌بس در لبنان از موضوعات محوری است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76596" target="_blank">📅 18:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76595">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QJl2UMBfKtO2f9sEn1p2fEAWVtmcFa7WSCLLQqAPp6cYAaTCiz4OGoRrRAPhieZQfJTWrls-bgy6esnru_b1HTBliN8yz6SyIrdLivNtBBQlEpJIvN3oetKOcwFM9hKyB_e5eyf3XQpDk51K52ZqU1X-B6k3mc5q3LYAijcMGUDrlt1MAKK1oV_-S7jF8h88_0j5NQ1p4rgZcAwZrf08mBpsOqxdW6t1DEYxdGLY_T4RBEKsM-85yUtBXTGl-J2a3lyEBHyyMy7n9hUDV6GL8KiGjNXHVH4uCPVSWA_kYLbhPDMULcCaT87avLH1zGPwsF2N18oIC8L87su-v4jl7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا با صدور مجوز عمومی، تولید، فروش، حمل و تخلیه نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران را تا ۳۰ مرداد مجاز اعلام کرد.
بر اساس این مجوز، تمامی معاملات و خدماتی که برای تولید، فروش و انتقال این محصولات ضروری هستند، از جمله بیمه، مدیریت کشتی، تامین خدمه، سوخت‌رسانی، ثبت و پرچم‌گذاری کشتی‌ها و عملیات نجات دریایی، مجاز خواهند بود. این مجوز همچنین شامل کشتی‌هایی می‌شود که پیشتر تحت تحریم‌های مرتبط با جمهوری اسلامی قرار گرفته بودند.
در متن مجوز آمده است که واردات نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران به آمریکا نیز، در صورتی که بخشی از فرایند فروش، تحویل یا تخلیه مجاز باشد، امکان‌پذیر خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76595" target="_blank">📅 16:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76594">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F8VlO_CLVCOGTT9SJ9EWzE0sX4wPOWet9U5ehjpW8PgBNDlJ72YqukEUGU-TaTi9q4o2WTbR18bxnjydJDIzt-KyJ-2ynReNoMdFcs39x6O1UqwUKM4XbS3nsVFoRKivUMqGVHmiupcqbIXyELl4Ko9x6SNjsoKBQ_SnjvvzTocrmeSmsNpy7DUpitEvkJPGPdieR-phHzPGljatJ9xRbNi8YxFCFbc3JeN3PeJ5kshUR9OK7RfXbJGGl__LF3Pc3EOqlFrJA-kVViZnnP2ysOWgMP0iAa7B4B51vqsRORoaESU18KWRy4U7mJs3KOCuqXfOiaa809OEyXQGUGcVTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس گزارش هرانا  در خردادماه ۱۲۷ حکم اعدام اجرا شده، ۱۹ نفر به اعدام محکوم شده‌اند و حکم اعدام ۱۲ نفر نیز تایید شده است.
هرانا همچنین از ثبت ۸۰۹ مورد بازداشت در حوزه آزادی بیان و صدور مجموعا ۴۹۳۳ ماه حبس، ۷۶۶ ضربه شلاق و ۵۱ میلیون تومان جزای نقدی برای ۸۰ شهروند خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76594" target="_blank">📅 16:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76588">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PsMAzA50Mge7HPNW2mhLTrYWUWBdoCQ7_SJLAf_WFFzRwVs34mqsADfWPP6Dtzo1pD-JKWSRK694qWPgAEfQTJ0FiIHBZjYnKHdwJ5BfeUXgZGst3tlDRzYVkfRX-eQGBbxpNqaTRtchyJF3KTPXOLyMiYj6juoupfx8hzi56l9RRVkJ5fMEwTo_jzQ343ua1h2UEX1oIboVxMRJo6WMrndSLkzqRrZx-rBKEAVFefLeHFxWgWi2hVeZ1k7qedHtFEXEByb07svKqZOPmVR6TvvYxIrSTvMq9xiohctVOlnEarv7T7HTPq95rO_naF6pJlKJPUMP5Ku6s0c4bVir3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sEO_iO3jC3FoGWgJjrAcqQnekrAYlYGB_63zUj6hKy0K6X39kWM2OV-JlPkSfIlnWWIREUW2glXAJUk4pGpCrFk00uSfGmlRYA7PH6hooh-o17MjCmJpsisiYIYhvQZC2kAbKhRLqEiCea3fcm9Im-jn3ERx9Fb1D0Flg93tUE6--YLGRM7rqjVF2zkv4gI0gZj4xEkB58oGwmGB16dEby9giWkfU8uyp60IWc1Rt_ADoR8iXwInssGF9qWzFMKNjZlkwVAF8PsfuT49dKXbCdI7Et-7hg3xVUEdcqcmBgbs4CEXxLVLtc6QI3_DBqlzE9JvQWRNVAHhr-zOXyvSJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bJe_uNxQ3CIWwMhHPOyy19wZPoZrV7q-rQxh3LAVFL9KGwjE9GhWhuK4cYhbDUBlwlWHboXfoJg9YrAtteR8Qg-reOedenkUC-Gm9C85ADVe--IgfKx91ja0l5bu4g_6lxljKKitURtjLqq-4VcE-t_dPlbELulxxoHj6nZj4OukAR0ZTGPXsY8WXU_eAbUCNTzFTvy7CNBhTFHM9KQUHAG9X73ePnHOY4RW3gmji7kwDAkCjO4jDrbDGTynWAoa4ZuWxVNS1GgzIigQJ8DE25yaWwgSOIRV8kT7xoRUYeUqKXOUHli6XxlOpHNlIGWGqF1yvLwyzWgY2mXi1GrGdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pkpQ5sx5uHmjVMyQfS0cgu9afmKO2l5uWAGAYF1J8LpUZdpIY9L59_JOibqDeFulVWFiJXJnzMZKj-SneP8uHCRXKxennjLRSZ9ABWENvCuBqNfF21X74s_xLy0Qmok7XLRTCqGol4dJE5GB4Ues2nplr48wT7Jug86byss7me5C9KZkzzhR0ymoF-rpjSb57i_3nlxOr1fSSDBAfVv_ACKgFPrUnLXZTW1XnJA9820doyAkpd4Na_YzRXzVZaOi5ofNCsygizlE8K7L7c2QOb-OJmsk-rvjSPjaFXi_LD2cJ6v-EsSz31ezEtN6dyxyaQE8mzMbeBmAwvGy9Icm8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N7ipB1RyNVIi6skN1K1UMAK6LKPOsYSG_WyCs3m_nlf1h-ryx-e8BchY6vYmNo4EHKxSLS8xO3DK5hQxxn1Dwq76_SHomRD2O-S_mGeJeZZeWFsMBSzfrZ9bFyyDwUbXyWrf9vBFqGT0-Q1XJVSz9c1mnC2jzceh5ioGVBstnMyKz8Q_MNAHky3NDkojJ2Wt_aH__81kg1oS6gAe4ThyKG-DeYn-VnSceJr860j7PJaLcWeHaApAV4xYN6CVUmZ0n7WLJWuEp4Lv0OvqE4nCISQnnXOQ-37nnnmi9TY-GEkKbpTJwGpxpTY7_AGEaWI2nF3JvtAz9JeovNBnC0naYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a45f8c601.mp4?token=L1cAfD5D9ahFmrvMBncTs07FYPQJ6V3DpOisMucaMBFu1DpwG8UdKz_LjCAluP9VxvjJQ0RUEB5c4HuyaPIsBWyuhuzaxwkTsQPrevSZBcA23bc0PCXcCEJyh5yIZ-1Fb1O9joFQSFZmbe_-ZZCxdHe2bXyZIQznOOF5ms0herPgfh3rFhckFTsPci9ZSv-df1pSag7DjK1v02hMBtm10B0BwVpiSRFdP2T8tE2Lj7bnNNst3VOTXbg6rwq2RAmWfm0dPosWowoSAFt1A-EGDdyAtT88y0D8tvK9swn5t2nqmIvrXnTtbUyPzTAVQ_o3IxCYRJUqcesao_bS4lZuvw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a45f8c601.mp4?token=L1cAfD5D9ahFmrvMBncTs07FYPQJ6V3DpOisMucaMBFu1DpwG8UdKz_LjCAluP9VxvjJQ0RUEB5c4HuyaPIsBWyuhuzaxwkTsQPrevSZBcA23bc0PCXcCEJyh5yIZ-1Fb1O9joFQSFZmbe_-ZZCxdHe2bXyZIQznOOF5ms0herPgfh3rFhckFTsPci9ZSv-df1pSag7DjK1v02hMBtm10B0BwVpiSRFdP2T8tE2Lj7bnNNst3VOTXbg6rwq2RAmWfm0dPosWowoSAFt1A-EGDdyAtT88y0D8tvK9swn5t2nqmIvrXnTtbUyPzTAVQ_o3IxCYRJUqcesao_bS4lZuvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجه جمهوری اسلامی گزارش داد «تحریم صادرات نفت و پتروشیمی تعلیق و محاصره دریایی برداشته شد.»
علاوه بر این، عباس عراقچی اعلام کرد برخی از دارایی‌های مسدود شده آزاد و طرح بزرگ بازسازی و پیشرفت اقتصادی ایران اجرایی شد.»
آقای عراقچی این موارد را در پستی در حساب کاربری خود در شبکه اجتماعی ایکس اعلام کرده است.
@
VahidHeadline
معاون رئیس‌جمهوری آمریکا اعلام کرد که در گفت‌وگوها با حکومت ایران پیشرفت حاصل شده و جمهوری اسلامی با ورود بازرسان هسته‌ای به این کشور موافقت کرده است.
جِی‌دی ونس، روز دوشنبه در سوئیس گفت که گفت‌وگوها درباره بازرسی‌ها ممکن است از همین هفته آغاز شود. ونس درباره زمان آغاز کار بازرسان هسته‌ای در ایران تأکید کرد: «احتمالاً همین هفته، شاید از امروز.»
معاون رئیس‌جمهوری آمریکا افزود: «ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم. گفت‌وگوهای فنی در هفته‌ها و روزهای آینده ادامه خواهد یافت».
@
VahidHeadline
معاون رییس‌جمهوری آمریکا، گفت یکی از اهداف واشینگتن در مذاکرات، ایجاد سازوکاری برای نحوه استفاده از دارایی‌های مسدودشده ایران در صورت آزادسازی آنها بوده است.
او گفت هدف این سازوکار آن است که اطمینان حاصل شود منابع مالی آزادشده به مردم ایران کمک می‌کند و صرف حمایت از فعالیت‌های «تروریستی» نمی‌شود.
ونس افزود جرد کوشنر با همکاری مقام‌های قطری طرحی را ارائه کرده است که بر اساس آن، در صورت آزادسازی دارایی‌های مسدودشده ایران، ایالات متحده و قطر بر نحوه مصرف این منابع نظارت خواهند داشت و باید آن را تایید کنند.
به گفته معاون رییس‌جمهوری آمریکا، این منابع مالی برای خرید محصولات کشاورزی آمریکایی از جمله سویا، ذرت و گندم اختصاص خواهد یافت تا در اختیار مردم ایران قرار گیرد.
@
VahidOOnLine
جی‌دی ونس، معاون رییس‌جمهوری ایالات متحده، در پاسخ به سوالی درباره تهدید تیم مذاکره‌کننده جمهوری اسلامی به ترک میز مذاکره، گفت: «آن‌ها تهدید کردند که مذاکرات را ترک خواهند کرد، یا دست‌کم در شبکه‌های اجتماعی چنین تهدیدهایی مطرح شد. اما ما دیروز تا مدت‌ها بعد از ساعت یک بامداد در حال مذاکره بودیم، بنابراین آن‌ها جلسه را ترک نکردند.»
@
VahidOOnLine
گزارش‌ها از سوئیس حاکی از ادامۀ مذاکرات فنی ایران و ایالات متحده، به ریاست کاظم غریب آبادی، معاون وزیر خارجه ایران، است.
رسانه‌های جمهوری اسلامی نوشته‌اند که قرار است دوطرف روز دوشنبه اول تیرماه در مورد سازوکارهای اجرای یادداشت تفاهم اسلام‌آباد و تشکیل گروه‌های فنی مربوطه با یکدیگر گفت‌و‌گو کنند.
با این حال تیم اصلی مذاکره‌کننده ایران به ریاست محمدباقر قالیباف، رئیس مجلس شورای اسلامی، سوئیس را به مقصد تهران ترک کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76588" target="_blank">📅 16:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76587">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GjV3wXTOvlCi1YmH2OV1oIUYTcRllTweJOcpTuLKA7zOe4ZIFsdf-iwq1YlFPUIw1KeQS4ygT5G_0AjTRTDtlVM7hdnUUugtL2gz8rQ0jx_JKhsB0jDbduk5eFwsmlbu7fBGAv0SgzdYR7Fcz18JTYoAzYW6UW5uutKLikmjAlN9AaJv3JuPZYDqN49Ky8si3ekQqKyLJ2_GPuW6e2FCvWQYSxEevGsHWbT1P14s3z8HGlT0XkEGTEMCx8n6hbOOFegJLFlqna6wlGFhlQGdlBu3NT-hrBvFWjDqgrDUdafaVtkdwtWg1KYNh2n6QOZZ7LQ8PhiMq57v6F9CU2FgPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میانجی‌ها اعلام کردند ایران و ایالات متحده روز دوشنبه اول تیرماه توافق کردند خطوط ارتباطی مستقیمی برای باز نگه داشتن تنگه راهبردی هرمز و پایان دادن به درگیری‌ها در لبنان ایجاد کنند.
بنا بر گزارش‌ها دو طرف از طریق تشکیل یک کمیته عالی مذاکرات، بر سر یک نقشه راه برای دستیابی به توافق نهایی ظرف ۶۰ روز به توافق رسیدند  همچنین قرار شد گفت‌وگوهای فنی از همین هفته در بورگن‌اشتوک درباره همه موضوعات ادامه یابد.
در بیانیه مشترک دو کشور میانجی یعنی پاکستان و قطر آمده است که: «طرف‌ها با تشکیل یک کمیته عالی موافقت کردند که مسئول نظارت سیاسی بر روند میانجی‌گری خواهد بود. مذاکره‌کنندگان ارشد به‌طور منظم به این کمیته گزارش خواهند داد و گروه‌های کاری مسئول موضوعات هسته‌ای، تحریم‌ها و نیز گروه نظارت و حل‌وفصل اختلافات را هدایت خواهند کرد تا اجرای مؤثر تفاهم‌نامه و دیگر مسائل تضمین شود. کمیته عالی بر سر یک نقشه راه برای دستیابی به توافق نهایی ظرف ۶۰ روز به توافق رسیده است؛ نقشه‌ای که زمینه را برای آغاز فوری گفت‌وگوهای فنی بیشتر فراهم می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/76587" target="_blank">📅 05:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76586">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i5Dp6v56HZtfef6uNt4nWeAmBR3xIiKjPfN2F0XTxD6Gp6AVNYyNTNBxa4883Arkm6QwGahlBpr7HV6NgCYOS-ARKsungufsff21pGXjNNXBt59eZPMdrIkaVgHsHcMklusc2yNghvQENWeYyjNrB_KijwXeCNYd_qJ0vEdcBnCO1BV-9rGHv3fM3wb7RlKZGw8fBo3Bo4R_BpGm5MjG6_B1SZl0kXajO9q93e_IyDR8LDzqsLFNPq6uoq2LuQCpv0hHEUKZ49jhod6tn8rP99F1T1XsbDJoViHDeq66HJtHSICQ_taknvdtvm7lR622HLRYmxk3ywoJJrYEnl3vlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف با فوتبال، ترجمه ماشین: ما این‌طور از سرزمین‌مان محافظت می‌کنیم. mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76586" target="_blank">📅 05:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76584">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/izzHsm2o5DhyunTRlTCWxNbjKQI_aJSOYK2n-r4S21PDuIA0ODGJiJoli2BgLiKlBnZz0-CRk7rzCk4Vg3fMSBX-oDTA7BB7J0oVai7QAa6-v-OnxFq8nS8kEWj0L4J1VFFX8E1vaLwBjd-CFNEeemfqGDQ6Xcrs7fa6k2msVIARFIjUBDUbOOIbvRtZ_6-aOHYk45jaeXMt4mmKFLdSTrgLBOJIYBQUI_ghJglGgX66-IG0q-K9nlaG3irN3cbL3PWREzKEgod0zR69NG-jGWUX8xpwgrbyYO7NorWiQZHejTiVNZyX_5CZ23Whp9pdidTrzUoFud-mU_nHhZiRig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uvmsqCGCMy5zlXpVTd4TwSc46EwdDJdzW22PrFamE3GzdIzE0E_F7cAvIxNh0ChNknyQFvu2RPJgqO_nn3H3jtRvSvkjjmfOcA11-uWDLG8Yxdly62iZIM9dMDC5hILWG5KgX7YlHDX99Ru8Umy3KPi_7LMFq9WnxOYgy5hHPINPB926dh9mTnwHGkcHqFkKPTNbyfMI42fkrpxhSkuZI9dfotea87BrW1yB8mCAumHImOKuHAANglaP169uVj59x3QSHxCLM3jBewmXkbSDHXCvJ1Wum3lErwbNhrTTxXVISjSdnxvEtJ_hE7C6xwc1byrqkDa_NQu5OB0tEQcH9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی، اعلام کرد مذاکرات سوئیس با «پیشرفت‌های خوبی» همراه بوده و گفت‌وگوهایی درباره پایان جنگ در همه جبهه‌ها از جمله لبنان، فروش نفت ایران، آزادسازی دارایی‌های مسدودشده و سازوکار عبور کشتی‌ها از تنگه هرمز انجام شده است.
او گفت درباره صدور مجوزهای لازم برای فروش نفت و آزادسازی دارایی‌ها پیشرفت حاصل شده و قرار است سازوکاری برای موضوع تنگه هرمز نیز تدوین شود.
بقایی همچنین تایید کرد هیات جمهوری اسلامی پس از انتشار آنچه «اظهارنظر تهدیدآمیز آمریکا» خواند، از ادامه نشست چهارجانبه خودداری کرد و مذاکرات از طریق میانجی‌های قطری و پاکستانی ادامه یافت.
به گفته او، تهران بر اجرای تعهدات طرف مقابل، به‌ویژه در زمینه آتش‌بس و تعهدات اقتصادی، تاکید کرده است.
بقایی افزود گروه‌های فنی دوشنبه مذاکرات خود را برای بررسی جزییات اجرای تفاهم‌نامه ادامه می‌دهند و قطر و پاکستان نیز متنی را به‌عنوان جمع‌بندی توافقات حاصل‌شده در جریان ۱۸ ساعت مذاکره منتشر خواهند کرد.
@
VahidOOnLine
تسنیم به نقل از بیانیه مشترک قطر و پاکستان گزارش داد که نخستین جلسه مذاکرات نمایندگان جمهوری اسلامی و آمریکا در بورگن اشتوک سوئیس و با میانجی‌گری پاکستان و قطر به پایان رسیده است.
در این بیانیه فضای مذاکرات «سازنده» و روند پیشرفت «دلگرم‌کننده» عنوان شده است.
به گزارش تسنیم، طرفین با ایجاد یک کمیته عالی رتبه موافقت کرده‌اند که نظارت سیاسی بر میانجیگری را بر عهده خواهد داشت.
براساس این گزارش، «مذاکره‌کنندگان ارشد به طور منظم به کمیته عالی رتبه گزارش می‌دهند و گروه‌های کاری متمرکز بر هسته‌ای، تحریم‌ها و یک گروه نظارت و حل اختلاف را برای اطمینان از اجرای مؤثر تفاهم‌نامه و سایر موارد رهبری می‌کنند.
کمیته عالی رتبه بر سر نقشه راهی برای دستیابی به توافق نهایی ظرف ۶۰ روز توافق کرده است که زمینه را برای آغاز فوری مذاکرات فنی بیشتر فراهم می‌کند.»
تسنیم می‌افزاید: علاوه بر این، یک خط ارتباطی بین طرفین برای مدت ذکر شده در بند ۵ تفاهم‌نامه ایجاد شده است تا از حوادث و سوءتفاهم‌ها با هدف عبور ایمن کشتی‌های تجاری از تنگه هرمز جلوگیری شود.
@
VahidOOnLine
عباس عراقچی بامداد دوشنبه، با انتشار پیامی در اکس از پیشرفت‌های حاصل‌شده برای پایان دادن به جنگ لبنان در پی میانجی‌گری خستگی‌ناپذیر پاکستان و قطر خبر داد. وزیر خارجه جمهوری اسلامی نوشت: «صادرات نفت و پتروشیمی معاف شده، محاصره برداشته شده، برخی از دارایی‌های مسدود شده آزاد شده و طرح بزرگ بازسازی و توسعه برای ایران آغاز شده است». عراقچی با این حال تاکید کرد که اولین آزمون واقعی و جدی این دستاوردها، عملکرد «سلول مدیریت منازعه لبنان» خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76584" target="_blank">📅 05:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76583">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcZkWKpqjns7qGJZa0YWbKrdbUXmtSsromuNd5Sj5nyybYShF1sQQ5jcd1hHtIN72sMoZhLOWHyqVG7_FCuzkHIRQmhi2fXOHMKbE3lf5gCmowOsFZpdw09PSA52zM1QYZZgyWt-1ugwnAGn4Y9Vzm_1w5mQo-fw2K3uh3yQOw5DB_oPqJIN3-8YpTEtVCOefIME8VU0GGOacLLp9m1XGRVIhozUXcM6LBJQkIxcQS2JTW9VEy32J5nfjV__nrvWdKmHu_EJE5W5RG0evt4exNtRx7ZzEPEK87_tBtE7Sa1-ZTo_ASVNtXO8d6_tgzm5Oms_pSCLRCENvMQVKiw4MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا اعلام کرد مارکو روبیو، وزیر خارجه این کشور، از دو روز دیگر، یعنی ۲۳ ژوئن (دوم تیر) در سفری دو روزه به خاورمیانه به امارات متحده عربی، کویت و بحرین سفر خواهد کرد.
در این سفر، آقای روبیو درباره مجموعه‌ای از اولویت‌های منطقه‌ای گفت‌وگو خواهد کرد؛ از جمله:
تفاهم‌نامه میان آمریکا و ایران
تلاش‌ها برای تضمین عبور کامل، آزاد و ایمن کشتی‌ها از تنگه هرمز
اهمیت حفظ صلح و ثبات در منطقه
وزیر خارجه آمریکا همچنین در بحرین با اعضای شورای همکاری خلیج فارس دیدار خواهد کرد تا درباره اولویت‌های مشترک کشورهای منطقه گفت‌وگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76583" target="_blank">📅 01:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76582">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bbwFO5t4jz3_8nuqAsTGUN-EYxdZB3BbuBNLaKSGkf_SCA18JJI-qdq_UwwOqB3CiAdGUu9liKxK1nKt7-pZkA2IX3FqB-fOf2GFy7WCPpPUJSMDgU2oT5P1jUEcMLWX9Y_Of2N0I2xQh4vNNz1KZlhmhnNIIuDF1QAaJHkqKw2O1EY5CXO88kgw8kXXOta8YhknRUV2LcPPOCV1WyFcTS4Kmzl8ZaW-J8WipawxOVlNUjekmjPN_3NglC9pzAh5prwEfSV9jYTSmx-Wd_ziPCkOM512gsclCN1V4Hi3Jvz-TSrB0IF7EGdPXbmpK1SApO-E1jMRW9ywjcmAzEjm0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف با فوتبال، ترجمه ماشین:
ما این‌طور از سرزمین‌مان محافظت می‌کنیم.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76582" target="_blank">📅 01:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76581">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rMq_GaJKUyR1_ROdBXsFZ5i5aXPHKfQRKEk6gs7qIyWjFgOrRncQcGVYFTwUNY6_Kvwa8MOiVWx7cn3mH1khB6RoL5O8KBw1qK8DN0mOHkN1riYerNgUD6aWEmkz7XHJDo4lJkPl01WrAhgOzNPjnMnA1m5jsd3OBdoZvCFqgvGgsp8MRqTH8gDhX-CC7aCx1Kp001QVgNefreZ7E03cUMhAZ4krUnHNZHDockwEBVy7xf631CTy1ojVCk-05uCod6ZORlnLV-GJf5mPVoGJ2t_FQ8n_YM3jnk4-jkC4g8UTVNVF852Td2F7aqlqZIAGttIMGaqEccZWz0HYJFNDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو پست ترامپ علیه نیویورک‌تایمز درباره اخبار جنگ:
تیتر نیویورک‌تایمزِ فاسد و رو به سقوط این است: «بعد از تقریباً چهار ماه جنگ چه چیزی تغییر کرده؟ تحلیلگران می‌گویند نه چندان زیاد.»
واقعاً؟ ارتش آن‌ها از کار افتاده، نیروی دریایی‌شان از بین رفته، نیروی هوایی‌شان از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آن‌ها تقریباً نابود شده، دو رده بالای رهبرانشان از میان رفته‌اند، تورمشان به ۲۵۰ درصد رسیده، اقتصادشان درهم شکسته، به سربازانشان حقوق پرداخت نمی‌شود، تنگه هرمز باز است، نفت با شدت در جریان است، و بازار سهام و اشتغال در آمریکا به بالاترین رکوردهای خود رسیده‌اند. این‌هاست آنچه تغییر کرده، ای ترسوهای فاسد و بی‌اخلاق، و حتی بیشتر از این‌ها!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
نحوه پوشش خبرها درباره ایرانِ بسیار ضربه‌خورده و آسیب‌دیده از سوی نیویورک‌تایمزِ فاسد و رو به افول، از طریق «واقعیت‌های» جعلی و ساختگی، به نظر من «خیانت‌آمیز» است. من همه گزارش‌های دروغین و مضحک آن‌ها را به شکایت چندمیلیارددلاری‌ام علیهشان اضافه خواهم کرد. آن‌ها مجرم‌اند!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76581" target="_blank">📅 00:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76571">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z8btV0i_yEGCid6y6Sdcf92A_aXBDW5ROGxsfGfJ2kMeUUyE6GzW4UgQVeLMck-OWst8ZAm0OYtK4b9k0vsoySDbEyfuXY-Xca1jDCgwxufzcf3b-SyYT_jkR4D-S8E8Q8YlY1LpQ821rkEZ2QoUijQ2r7DfCOE_GT9tVgtZ9QnDO8VNKlf86PhoLdrDc-jDEY82tmUN1HidNhtCkkktUtAqHY0CaqEnKSVTEUv-yaJjX5y81fbeYiHBY4-oepcJwDcDzO2L6S6CB3TVasi9oOb-8R3dyHG6bySONYR3G9KPSLVFgrc7xul4w2mfBDxzzWonzPDrBtLc5Bd0-_k8Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DRQKyOgeplLrgb1_iBsc67Py9dfV5St8H9h8z661Z77EdlzJNO_hhvnowUKpHMvXo6oPpGCcg8Fq2lGxGvmnWXKscNDTheVrSYLCX91Eed3FzY4dyJVbZhCT4rwwKc6o9Yz3uTPFrudiepD555m69K6FycSjZ_4uS4_JwGdfOgkp0ekdGWtbwftaCiQB0g-GvVGgwFeegn9IzAcIzjJpxvNXOws3eg4Ilo1PsP3G7zyzXVYRLUbO_smJl74Rb54vX4K8Jyw_Bakmy5kvuYgzyxEDe9FVviD2SdaAerf0hpjbJ_FfbHVWoOn42xBgO8Wh_-LQDjJPAMZMznZuucsXeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hFeUF6sQrhq9Tf8RTigKXgy_P7E7Yy7d1rXxMuW-4T7Nez62LJpidppZR82f9tPjR2kQU499O0x7fIpmfFTuOAeNnzU-nxCagmziNJx0_bSvUg9QLk6xv3Uz7rqmKBbB7fCFGsI3UXPubHvww4kdKlU9CLmjK8366p53B2l3nCIkHmqOodpYYQZ8QsVQ42VE3VKoYX8duLHDWjsxwlMTQjVd5IbH6l8NLUfPINIs23TMEzDDC1LSh5Bl_1Gh1D15RU1h9_Iw3iL6P3Ts62em_hwjML5JpajSJmCCWARhi9fqBFGqr_7P4cUCSZGDBQXZoqdT7pYPtSTIl057dDItGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rwKeQTuryvQ7M5WHwS7n-bNFBjH3HfPtrGrrpK08gBcnGy2QtBAyShMseXJLHLOtZGrub3K-A5Z1Pr4L1rkR1ByTevkdQwpOh05jKYMnmSrI1IeKGZrnLDj-BuJXtOqF2ZxNK3XL36L6UDV3T_nZ9Amzx4g00_SMFIwjLaV5eYvQyvThFQRQB1XHP9gTlJoPEomiePZ0eWXWx41GCYfBk7adezr5h7BsRkZuHngRRmCg2YnBLF0jz3l0n9s6WcfnI72Y4t6ycp7hsET-Zg5sjCwvNhgpZ3YVu_ram2gLticI7NnkwMHEe09yBch-HY4HO6govrWL0n4Axpco9ZNJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rBZQht5T22QptEL9gqtyvN_J5HQmrYSKk0bPcrtT4AohqbnA_1rSJU4fF7PUwws-r5-ufNjuZ4IVVIXbnxbidK3LKXG_TTxNZ_I3V0N3SdrYlLdIGjLXsMUmbwMawjdJHose4mhEphs1Ray9rQOCiBBe9PZBArdZi_blIUA8m89beRciHs5M7fajkKQvffMevATWM1RSSqLRGxhN6OvWPvHxb2tZtl_l8bUwtP0O7_MWZRrZq_q6LW_uGkK6HWQV8FKxPm9CXlNW0aFtWIQbIlB2AfPR-iMZKNiJubLTjctf6LXqoBMgeT6Bwb0wjy2c0aS9aB_MPNqcVrsd2MkTyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L1OGDtiEmJyBmk6RhSapXgApSdiROW9y8cqtqdLoJjRLChI5eCQQRSVr971vK4pUM3tR31jXBNfXepbPGFTeJaPzUSPLUr8Ysz0Cv1ZjUM7AQJzvAhai4ho1ZYeItKVxkOQM6wjdzk77Segm7_Y9Ap9SCSVk9OCIBSxtpboG6IljsHy5ECGDVaf0M2pMBGkkjW_WbEMCaycBsCflhBtPmuO-cC3o3G2QQ0WJS4FtwqCAORx8cTaeksqUCxreKvo5rYY-x4oghdpl696V3tClUWhmxDPOBL8-NI3xSs2IznIdlOmtcDxJLeHhcbi8ToCArTe-YgGiQ44YSOJntZlLGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PH1Bj4mt7kT0rfBdmWvspEvmqEJAFRAQubFGPjAIcNjQqjxCMJKq3-_j-CwVbwQcxEwIB1R61b3iqRlfXFeVmx6lBN50pgPqcOza8nmvuJoGXRUtw3OibM_KtF-c7xrtrBdgO3v3F5ePm1RZSvg3MrIPe5Qo7J3yQa67HIMG1nY0G_pOHW3uNJMeIaY2-utHJ5zzYR1wroTGe00hz9T8ZzV1F5xvAxkLZ5Zr_PvllyvK-vaiNuqyT0Dw1bvofQJqWQ617Yzow1g1qX85leyzvu0j1yvkK8brXxy5yukyP2dJ2dAAULDJwASAN2OUb545Ae_Qi4nV3tHQ4dlBXKftUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ecd58481d.mp4?token=jJNTVm1K0qgzpuK2IWUAD6ujKWklF1ISLYiE5Uz7A1PF8vd6sBekGw4XUKYKO_effAZgMH8h165uQObQX0pe3rBYaqQSciI0Gy7QI3vGPr9B4P4bswXnuXpW9AktjyxOfCy1Y4mhOUhqrAXflJn-U608ZJ2ejUEdXtZHC7Sa3gvWxVt5Ps7NUUiFHctSiPWVpROpRaLPJeZsZiMvUtS7tvx2uFNIg3Jrmv6hp-hq9EsQQ0mLMpAODL8SJ95XDacPX0uFKejTd_MsRxmls2A_SH4UX9wJZ0dwM0QSfORGlWx-tDg1LS1aHWgjKtfpVi9l_34NnYqXZ1Xhrak_JvSKHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ecd58481d.mp4?token=jJNTVm1K0qgzpuK2IWUAD6ujKWklF1ISLYiE5Uz7A1PF8vd6sBekGw4XUKYKO_effAZgMH8h165uQObQX0pe3rBYaqQSciI0Gy7QI3vGPr9B4P4bswXnuXpW9AktjyxOfCy1Y4mhOUhqrAXflJn-U608ZJ2ejUEdXtZHC7Sa3gvWxVt5Ps7NUUiFHctSiPWVpROpRaLPJeZsZiMvUtS7tvx2uFNIg3Jrmv6hp-hq9EsQQ0mLMpAODL8SJ95XDacPX0uFKejTd_MsRxmls2A_SH4UX9wJZ0dwM0QSfORGlWx-tDg1LS1aHWgjKtfpVi9l_34NnYqXZ1Xhrak_JvSKHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال ایران در دومین دیدار خود در مرحله گروهی جام جهانی ۲۰۲۶، با ارائه یک نمایش دفاعی، در ورزشگاه سوفای لس‌آنجلس مقابل بلژیک به تساوی بدون گل دست یافت.
مدافع بلژیک در دقیقه ۶۶ از زمین اخراج شد و این تیم ۱۰ نفره به بازی ادامه داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/76571" target="_blank">📅 00:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76570">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q-0veZjnhhd1SgragV827O5jWz12kBpRTW-4uvrymjhZYUoSTq72xLZ2qasheI8bQSNTRmmul3zxrUeqpST7qnRSZOHOxKjK520RwEcUKW7D2qXwEhkrDBgF9__8GTY4nPeVHsr_1HDqtADQU5xvxenC0yJlhv0MGWAUTNyq7GC67Vv32hVgpTUfu2ZJMkU7eYpaNl91496BiJKkkRqFm4zfe9-deKjDBwgI-I4XL7fQ8Or6BT0fbTrRnvUXtarNRUuQtmnQZIgpuSHCY9dTolqJyWsGxI5TSIzf6zNM4xvPLoTt2lzKOHlpyOSUenKKA2fhqGH2xDOJxRKxRzbi1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
بعد از آن‌که تریلیون‌ها دلار خرج ناتو کردیم، ایتالیا و نخست‌وزیرش حتی فکرِ درگیر شدن با جمهوری اسلامی ایران و تهدید هسته‌ای بسیار جدی آن را هم نمی‌کنند. دهه‌هاست که ما از آن‌ها دفاع می‌کنیم، اما وقتی پای آزمون به میان می‌آید، آن‌ها برای دفاع از ما و بقیه جهان حاضر نیستند. خوب نیست!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76570" target="_blank">📅 23:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76569">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mYfRCqrvCWyIiRUuSJHdyV_XytGWEC89AUzSxDY1QDU7UnLNMvmP5KRgI4r5qed2MwC3J7uFwiHaatKKxmsw9MaGVl1c0koulzgAvySqAf-3-IMYfz3QiNNbt_zMEjn5SPdvv-j5hi3W17C9OG78MJ_oXqXxnUZthS8UC-il0t1kM-BuMWKIurt7gCTIHmfYUyCxvuBFK6tyC9DAxaRZaRoawY2ZpEoruZ3Pz9hHJOBEmJRhV2HqZ8LQ6SxhMQ1XP-aR9ib4iAgGvLZountF-COYkwVVr7dgXrMc4sgDz56qrI23cDUiC1tl2R1Pq0MITPj6wwwcQrA2e0Ecrbrgpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ک مقام ایرانی یکشنبه شب ۳۱ خردادماه به خبرگزاری رویترز گفت مذاکرات میان ایران و آمریکا در بورگن‌اشتوک سوئیس متوقف شده، اما پایان نیافته است. این مقام جزئیات بیشتری درباره علت توقف گفت‌وگوها یا زمان از سرگیری آن ارائه نکرد.
این اظهارات در حالی مطرح می‌شود که گزارش‌های متناقضی درباره وضعیت مذاکرات منتشر شده است. پیش‌تر باراک داوید، خبرنگار آکسیوس و کانال ۱۲ اسرائیل، در شبکه اجتماعی اکس به نقل از یک دیپلمات حاضر در مذاکرات نوشت که هیئت ایرانی محل مذاکرات را ترک نکرده و گفت‌وگوها همچنان ادامه دارد. با این حال، خبرگزاری ایرنا دقایقی بعد به نقل از یک مقام هیئت مذاکره‌کننده جمهوری اسلامی گزارش داد که مقام‌های ایرانی پس از دومین دیدار با هیئت قطری، محل مذاکرات را ترک کرده‌اند.
@
VahidOOnLine
خبرگزاری ایرنا، رسانه دولت جمهوری اسلامی، گزارش داد هیات جمهوری اسلامی پس از دیدار با هیات قطری، ساختمان محل مذاکرات در سوئیس را ترک کرده است.
هم‌زمان، یک منبع نزدیک به هیات مذاکره‌کننده جمهوری اسلامی به شبکه سی‌ان‌ان گفت گفت‌وگوهای میان جمهوری اسلامی و آمریکا در سوئیس متوقف شده است، اما پایان نیافته است.
به گفته این منبع، گفت‌وگوهای غیرعلنی همچنان ادامه دارد تا طرف‌ها به میز گفت‌وگو بازگردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76569" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76568">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LyUgaQqi3lFDfeEB0WkoH5oOVr_aFQ1jp7ZXjNYFAfDS89upnllpIWCJkNShklIEAKU8g8mzvU-_334gRDbvg9nt-eOIRsTyhef7W7rr2rFKkIKs1FogrcMBfrtbBM3V-L2MaGPmlgexQ0TP4AYXZmKopofHXiQmaChRSiGEAtf7LWkEkxQ_Ov40uzZw4-b3dgFkpP0GBUxmc8TbAatRwinyW5JPWed044ikhvfThKrqSfMiHYRWwTUMqTKChhou2LO_hT7gTehWtXZoMqXdTeciegbdIoaayO-nmOQIolA5B-CMR2Pc2DObmijisAXYKl9RHvi3YuDGjwvYweszvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
هیئت مذاکره‌کنندهٔ ایرانی در اعتراض به تهدیدهای ترامپ محل مذاکره را ترک کرد.
"
ادعای فارس و تسنیم به نقل از "یک منبع نزدیک به تیم مذاکره‌کننده"
پیش‌تر در
اکانت قالیباف
همچین توییتی منتشر شده بود:
با خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم.
بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند، این ماییم که عمل می‌کنیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76568" target="_blank">📅 20:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76567">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eIoV7TOnxOmCO5MMGbKsrhuahZ28i415VMAOZ0zu7LNlLnTuvHDNyNswUGAhyBoo_ST-LDCRep7gvIaOWvn7DIOGz8gtxiV7wrn_QBy_3ekzwYz3XXywwwfYQhOd76Ibv2-9Un8QdF-gHNhkGhhg2DCQQWh1PQf0w85-9LanxuSv3dlN7jmNZBhftfdjmymwTWZWFcX2N8UGz1TSfswersdi3qbbOnhfzwMsmj3asj54P-vm-Lkv_rpZ2_tQDiHaL5f6ydkLaK7L_69Gxerrm9IkLwCqXrdwLiMr1oKoLwexBYYc4vfqpxtyRrrKKUxFsaezgJ9fXDZwYRQ4FJIW5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در واکنش به اظهارات مسعود پزشکیان، رییس دولت جمهوری اسلامی، درباره ناچار شدن آمریکا به پذیرش تفاهم‌نامه میان دو کشور، هشدار داد که تهران باید در مواضع و رفتار خود تجدیدنظر کند.
ترامپ در گفت‌وگو با فاکس‌نیوز گفت: بهتر است مراقب حرف زدنش باشد. بهتر است رفتارش را اصلاح کند، وگرنه ما کنترل بقیه کشور را هم به دست خواهیم گرفت.
این اظهارات پس از آن مطرح شد که مسعود پزشکیان روز یکشنبه ۳۱ خرداد گفت: آنچه مسلم است از حق غنی‌سازی اورانیوم هرگز کوتاه نخواهیم آمد و طرف مقابل نیز ناچار است آن را بپذیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76567" target="_blank">📅 19:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76566">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dtj8ilNwQ2O1sDrSeZQNfF8RpZU7ncuru8LHnHIP_n_OM-U0Y73TUZnh2UK16rDdQHqfqO-wPpui2aqxSq1GImlzk6aOTXYtn-kkPuK3hApUbS4EUPAmYIJJd0MO8raoL7uWDk0eZ3CURAWTgouZuSzDctaHP2I2XJt3QqxXWA5fKztNn-fYKrLoSPISWsMVl1sGdQI2lRKxyNNbJexyPeGrW81LEnn73cmI_aJ3D-7EqrfhwfA_xFZq2JCCdCfxFQvm_A1_JOuQtXYZ2COJLuUwKbfL4R9uKLVJRpunQkvXQAhY00Pzr8Y0UVoUekSdctDQT_lMyzk4VfBj9mLffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، اعلام کرد همزمان با برگزاری مذاکرات در سوئیس، به مقام‌های جمهوری اسلامی درباره هرگونه اقدام برای بستن تنگه هرمز هشدار داده است.
او در گفتگو با شبکه فاکس‌نیوز گفت این هشدار شنبه شب به تهران منتقل شده و تاکید کرد در صورت چنین اقدامی، ایران با پیامدهای سنگینی مواجه خواهد شد.
ترامپ همچنین گفت به مقام‌های ایرانی گفته‌ام که اگر تنگه هرمز بسته شود، «دیگر کشوری نخواهند داشت و حتی امکان بازگشت به کشور خود را هم از دست خواهند داد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76566" target="_blank">📅 17:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76565">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LpLZ8rJ3iWt8GcfHvrpzwozXGChZAH-ILNjCIu2yChNUrFnCLHCwU0HckfUfRQFxL5yye6iqSX88_G9IBsdg_wMnYPwc9GBnah8uZzZ3RJICJdLFcYdNmDcWOJDoZFaPxr7JpLmtp_W2KnirST11lVHVRNwAQoA1ebBrbB1OiXVnm5xCba1pus7Chn-POQ6rWevI_rr4pJNTbjEsMn28sYgHfTMpYkiOQDp298WdRUYiWZuEWPmLiT-RQt6_KVaQwYlyw00LfuGSMp3pfpyyGNL9665AGkyttihYHjIB-na7gMTv6QLAYQdfbioVUDVGKLMd4SLqGMASez9hGeoomQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران باید فوراً جلوی نیروهای نیابتیِ بسیار پرهزینه‌اش در لبنان را بگیرد تا دیگر دردسر درست نکنند.
اگر این کار را نکنند، دوباره به ایران ضربه‌ای بسیار سنگین خواهیم زد؛ درست مثل هفته گذشته، اما این بار شدیدتر!!!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76565" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76564">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e1422ca156.mp4?token=KFEkwlz9c1o_O0jEdqWfVVWcFhBO2uC_6YutghV6RTNQM-IytBp60SdDRktfP2tSvkVG8pzJiFMSVIKJgu-VzAc2hrVBHneOg3FiGqBK7wBGWkayFpuw5q7kxu89hbN-f8paeN_1BEZxab4uAVsE1L8qoUHzU-TjziUIfNOE9yhlPd8Mx_gaGQUlCiI2PgpEwlIJdCgtwFxb3XaAn6ESzSjsi56gNETrWDHfqzn-G6tdh8B66FHBAaekEW4DmFofNnLt4Wp9HC3NW0fWvz1c9Pi2RS_fdIa14n_6R_ahcnnIfIVeMSAD5bwLtFJGonjwSLeOZMNV1NQg-3KA-OSrxA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e1422ca156.mp4?token=KFEkwlz9c1o_O0jEdqWfVVWcFhBO2uC_6YutghV6RTNQM-IytBp60SdDRktfP2tSvkVG8pzJiFMSVIKJgu-VzAc2hrVBHneOg3FiGqBK7wBGWkayFpuw5q7kxu89hbN-f8paeN_1BEZxab4uAVsE1L8qoUHzU-TjziUIfNOE9yhlPd8Mx_gaGQUlCiI2PgpEwlIJdCgtwFxb3XaAn6ESzSjsi56gNETrWDHfqzn-G6tdh8B66FHBAaekEW4DmFofNnLt4Wp9HC3NW0fWvz1c9Pi2RS_fdIa14n_6R_ahcnnIfIVeMSAD5bwLtFJGonjwSLeOZMNV1NQg-3KA-OSrxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس و عراقچی در یک قاب
خبرگزاری تسنیم به نقل از یک منبع نزدیک به تیم مذاکره‌کننده جمهوری اسلامی گزارش داد که هیات آمریکایی و برگزارکنندگان نشست ژنو قصد داشتند پیش از آغاز مذاکرات چندجانبه، مراسم عکس مشترک و صحنه دست دادن میان هیات‌های جمهوری اسلامی و آمریکا برگزار شود اما محمدباقر قالیباف مخالف کرده است.
به گفته این منبع، محمدباقر قالیباف، رییس مجلس جمهوری اسلامی، با این تشریفات مخالفت کرد و اعلام کرد اعضای هیات جمهوری اسلامی در مراسم عکس مشترک با هیات آمریکایی حضور نخواهند داشت.
این منبع افزود در پی مخالفت هیات جمهوری اسلامی و خودداری آن از حضور در این مراسم، پخش مستقیم و برنامه عکس مشترک لغو شد و پس از آن هیات جمهوری اسلامی وارد محل برگزاری مذاکرات شد.
به گفته این منبع، هیات آمریکایی از هیات جمهوری اسلامی پنج دقیقه فرصت خواست تا خبرنگاران محل مذاکرات را ترک کنند. او افزود مراسم پیش از آغاز مذاکرات، بدون حضور هیات جمهوری اسلامی برگزار شد.
@
VahidOOnLine
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، روز یکشنبه در آغاز مذاکرات ایالات متحده و ایران در سوئیس، این گفت‌وگوها را «تاریخی» خواند و تأکید کرد ایالات متحده آماده است روابط خود با ایران را به شکل بنیادین متحول کند.
ونس در حالی که در کنار نخست‌وزیران پاکستان و قطر ایستاده بود، در اقامتگاه بورگن‌اشتوک در کنار دریاچه لوتسرن گفت: «این یک دیدار تاریخی است. پیش از این هیچوقت رهبران ایران و آمریکا در چنین سطح بالایی با یکدیگر دیدار نکرده‌اند.»
تصاویر و ویدئوهای منتشر شده از محل نشست نشان می‌دهد هنگام حضور معاون رئیس‌جمهور آمریکا در اتاق محل مذاکرات، عباس عراقچی، وزیر خارجه ایران، نیز حضور دارد.
معاون رئیس‌جمهور آمریکا درباره اهداف مذاکره با ایران گفت: «آنچه رئیس‌جمهور از ما خواسته این است که فصل تازه‌ای را آغاز کنیم تا روابط خود با مردم ایران را متحول کنیم و دست دوستی را به سوی آن‌ها دراز کنیم. پیامی که به مردم ایران می‌گوید اگر رهبران شما حاضر باشند از نقش‌آفرینی به عنوان عامل بی‌ثباتی منطقه دست بردارند، و اگر حاضر باشند در بلندمدت از جاه‌طلبی‌های هسته‌ای خود صرف‌نظر کنند، آنگاه ایالات متحده آماده است روابط خود با آن کشور را به شکل بنیادین دگرگون کند.»
او ادامه داد: «این بدون تردید هدف ماست.»
ونس همچنین گفت: «ما تنها در چند ساعت گذشته پیشرفت‌های بزرگی داشته‌ایم و انتظار دارم در ساعت‌های پیش رو نیز پیشرفت‌های بیشتری حاصل شود.»
او با اشاره به اراده ایالات متحده برای «متحول کردن» خاورمیانه، افزود: «ایران در گذشته یکی از عوامل بی‌ثباتی منطقه بوده است. اکنون آینده‌ای را می‌بینیم که در آن همه بتوانند برای پیشبرد صلح و رفاه برای همگان با یکدیگر همکاری کنند.»
@
VahidHeadline
جی‌دی ونس پیش از آغاز مذاکرات اعلام کرد واشینگتن طی ماه‌های اخیر بیش از هر کشور دیگری برای توقف درگیری‌ها در لبنان تلاش کرده و این روند را ادامه خواهد داد.
او با تأکید بر اینکه «صلح آسان نیست» گفت رسیدن به توافق نیازمند تلاش و «بده‌بستان» میان طرف‌هاست و افزود هدف آمریکا تنها صلح با ایران نیست، بلکه دستیابی به ثبات در کل منطقه دنبال می‌شود.
ونس همچنین مذاکرات جاری را «آغاز یک گفتگوی فنی» توصیف کرد که قرار نیست همه اختلافات را یک‌باره حل کند، اما فرصتی فراهم می‌کند تا طرف‌ها برای نخستین‌بار درباره مسائل اصلی به‌صورت مستقیم گفتگو کنند.
به گفته او، حضور رهبران سیاسی برای تعیین چارچوب مذاکرات و حمایت از تیم‌های فنی است و با وجود چالش‌های پیش‌رو، طرف‌ها با انگیزه برای ادامه مسیر آماده هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/76564" target="_blank">📅 16:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76562">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/12a29862bf.mp4?token=sdh3rPV3UFk7vXgRWu-O1Fam61PAdVAGp6f20WTo1icyAjkkMRqV67EqWxTHzbuWysVfPuWxKR83Z4fJpQEiNIiNfTAL72IujCDIc0UHupgNy8jVhhcA-nk-gHwTTlIY94yUBIxsMcbAGPZqmK9YIgJ7_A7M6VaLMMudQyIM9Jkn0b8_GSZFELMiSxLilgRHrhEMCtOdk5fXjkpQRprIgC_cRlHXYTytEDKnJAU1EhxkeAKCo5Z_I7JBF8X7SvLuV6nNl_pm-Z678dv8X-wZCp1nC_jWBk6qX4yOmrzE8gJn4dB5uf7OuNpZZgbCEMdj01hrMpektrDUw339aDoAMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/12a29862bf.mp4?token=sdh3rPV3UFk7vXgRWu-O1Fam61PAdVAGp6f20WTo1icyAjkkMRqV67EqWxTHzbuWysVfPuWxKR83Z4fJpQEiNIiNfTAL72IujCDIc0UHupgNy8jVhhcA-nk-gHwTTlIY94yUBIxsMcbAGPZqmK9YIgJ7_A7M6VaLMMudQyIM9Jkn0b8_GSZFELMiSxLilgRHrhEMCtOdk5fXjkpQRprIgC_cRlHXYTytEDKnJAU1EhxkeAKCo5Z_I7JBF8X7SvLuV6nNl_pm-Z678dv8X-wZCp1nC_jWBk6qX4yOmrzE8gJn4dB5uf7OuNpZZgbCEMdj01hrMpektrDUw339aDoAMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، همزمان با برگزاری مذاکرات مستقیم میان ایران و آمریکا در سوئیس، گفت همه نظامیان در شورای امنیت ملی موافق مذاکره بوده‌اند.
او در جلسه‌ای به مناسبت تشکیل بسیج اساتید در دانشگاه تهران، در میان صدای اعتراض عده‌ای از حاضران گفت: «همه امضا کرده‌اند که این راه را باید برویم. حالا هر کسی می‌خواهد تفرقه ایجاد کند، این گوی و این میدان.»
او با اشاره به نظر فرماندهان نظامی در شورای امنیت ملی گفت: «فرمانده قرارگاه [خاتم الانبیاء]، فرمانده ارتش و سپاه، و نهادهای امنیتی همه بودند و همه یک حرف زدند و همه متحد بودند و همه آن چیزی را که می‌خواستیم عمل کنیم را امضا کردند.»
این سخنان پزشکیان در پی افزایش انتقاد اصولگرایان تندرو از دولت در پی انتشار نامه منسوب به مجتبی خامنه‌ای صورت می‌گیرد.
آقای پزشکیان همچنین با تاکید بر نقش دولت در حمایت از نظامیان در دوران جنگ گفت: «۲۰ میلیون بشکه نفت که مال دولت بود را به هوافضای سپاه دادیم. ارزهایی که داشتیم را به این عزیزان دادیم.»
@
VahidHeadline
مسعود پزشکیان، رییس‌ دولت جمهوری اسلامی، گفت نگرانی اصلی او این است که دولت نتواند رضایت مردم را جلب کند و نارضایتی‌ها به اعتراض‌های خیابانی منجر شود.
پزشکیان گفت: «از آنچه می‌ترسم این است که نتوانیم به مردم به درستی خدمت بدهیم، ناراضی شوند و به خیابان بیایند و اعتراض کنند. آن وقت ابهت ما فرو می‌ریزد.»
او افزود مهم‌ترین قدرت جمهوری اسلامی، وحدت مردم است و مسئولان نباید اجازه دهند کمبودها، کسری‌ها و نواقص باعث نارضایتی مردم شود. به گفته پزشکیان، بروز چنین وضعیتی موجب «خوشحالی دشمنان» خواهد شد.
@
VahidOOnLine
بعضی از جملات پزشکیان به انتخاب خبرگزاری دانشجو، وابسته بسیج:
🔸
اظهارات عجیب پزشکیان: من از این میترسم که نتوانیم مردم راضی کنیم و به خیابان بیایند اعتراض کنند
🔸
تمام مفاد تفاهم‌نامه امضا شده بین ایران و آمریکا به نفع ماست و دستاوردهای این گفت‌وگو و مذاکره عیان خواهد بود.
🔸
ترامپی که ما را از انجام بسیاری از کارها منع ‌می‌کرد، در سخنرانی اخیر خود تمام آن‌ها را حق مردم و ملت دانست.
🔸
۶ میلیارد دلار پول ما در قطر برخواهد گشت.نتانیاهو اولین ناراضی از مذاکرات است.
🔸
تنها نکته آمریکا این است که ما بمب اتم نداشته باشیم، این موردی است که رهبر شهید هم بارها فرمودند ما بمب اتم نمی‌خواهیم. آمریکا گفت همین را بنویس و امضا کن، ما هم امضا کردیم.
🔸
شورای عالی امنیت ملی در وحدت و انسجام تصمیم گرفت؛ همه یک حرف زدند و متحد بودند
🔸
مواضع ترامپ ۱۸۰ درجه نسبت به گذشته عوض شده/ آنها پذیرفتند که حق ملت ایران را نمی‌توانند نادیده بگیرند/ قاعده عوض شده است
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76562" target="_blank">📅 16:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76561">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWJ9-90YY9FAYieUQRH8L1WCfop0EpTXClFg150DS_4qChfOHlsG0aYbMa_2E76JK7odiu42oI1VF9xUXNEiNOHWTSytXeF2j5SXWoMsvYIRYkB1kzOmRFyk-azCTk3TV7a-iqb4aVoWVeO1cmzFvCEqBSjizA9pWZBfF_lv4YGD5CWXAZXFuSv5YEt1bI_p8RcpnUkfJMTMTOcvBi_3S0aQwa5PSLvq9hAuxgTM9B9TFLVUWKxjv4dcv-aWrG49jGfxCHDs8JBiLTKGNsvfwX6i6PcyHlM2jg8U8KTIbOy07JAgdEDx-Rgv2AGSSS5lQFZJDl4JsJJUhlqCKXOmQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از دو منبع منطقه‌ای آگاه گزارش داده است که آمریکا می‌خواهد نخستین دور گفت‌وگوها با ایران با دعوت تهران از بازرسان سازمان ملل برای بازدید از تاسیسات هسته‌ای ایران پایان یابد.
به گفته این منابع، این تاسیسات پیش‌تر هدف حملات آمریکا و اسرائیل قرار گرفته‌اند و آخرین بازدید بازرسان از آنها پیش از جنگ قبلی، در ژوئن ۲۰۲۵، انجام شده بود.
اکسیوس می‌گوید: «آمریکا در مقابل آماده است به ایران اجازه دهد به بخشی از دارایی‌های مسدودشده خود دسترسی پیدا کند؛ از جمله حسابی به ارزش شش میلیارد دلار در قطر.»
بر اساس این گزارش، ایران می‌تواند از این پول برای خرید کالاهای بشردوستانه استفاده کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/76561" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76560">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSbaZ9w3IkexphPaj3BblJQuOJj8vR2ny22n9TKCYF65xWcoXY4LfH1zg26fRMdQz5qHswdZqI1qQiIg0dC4AVdRWNv6GmxQwyCPRMAt4iOBAH3mFPPyhpiLkfx6RHiE6lgJAQLaz5OzJ4FOgfx9FVzSkJzCtVrOenxEz-6pZI7ME9vU0fSU9eh3AAPbiKDtjDQpEuHrebVDVvQ3cEs0XWgnr0Te59FN1tT_4_A47uMhRKxy3ffBdFXZ3lCXuO6voITDr61S2OJUKlorXmDKJY30T4Cb3LhOka946Ix4B-mvbNzbWfNhM2lWZcNYaTf8EqEr0xo_YeiXz83K25agEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام‌های بهداشتی در غزه می‌گویند که دست‌کم ۱۰ فلسطینی در حملات هوایی و تیراندازی نیروهای اسرائیلی در چند حمله جداگانه کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/76560" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76559">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYK03NJ1WdusWc5-6t4ve2ZOTsXiswyu_HWYOtF7ziSVta_8DjBoPI-Krqi0s0Igbqfsch7RPlhXI1SHUSutlgPRNxSEwOXT_aWliJYc26ZUFxsJJWvv22F2pWyg7o032idUuel3jtY1GRMQ-N_WDU3BIPlsJ8EDc4uQMZIuT5AcTug_XcIebB8ay9xdrP4688U9ybWFKUlWHgCY9BJSZNIvOwxlwtP8CfyVMFNwaHpEQA_boBlkfkEz3h1aafMmG6vv-0nVWoO7N-MsQNPSGDXJpb0b7bf2KYPzNW0lEWawDC-1J6luftIkQdCB82tWqlBe4G7RuEdJ43lfvJXAVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از هزار دانشجو و فارغ‌التحصیل دانشگاه صنعتی شریف با امضای نامه‌ای سرگشاده خطاب به محمدرضا تجریشی، رییس این دانشگاه، نسبت به آنچه «تشدید فضای امنیتی» و گسترش برخوردهای انضباطی با دانشجویان خوانده‌اند اعتراض کردند و خواستار پاسخگویی مدیریت دانشگاه شدند.
انجمن اسلامی دانشجویان دانشگاه صنعتی شریف تاکید کرد که بیش از هزار نفر این نامه را امضا کرده‌اند. انتشار این نامه یک روز پس از رسانه‌ای شدن صدور احکام اخراج برای شماری از دانشجویان شریف صورت گرفت.
امضاکنندگان در این نامه نوشته‌اند که در ماه‌های اخیر دست‌کم ۳۰ پرونده در کمیته انضباطی دانشگاه تشکیل شده و ۱۳ دانشجو با احکام بدوی تعلیق یا اخراج مواجه شده‌اند. به گفته آنان، احکام سه دانشجو نیز در مرحله تجدیدنظر تایید شده است.
نویسندگان نامه تأکید کرده‌اند که آنچه در دانشگاه می‌گذرد، ادامه «روندی نگران‌کننده» است که به دلیل نبود واکنش مؤثر از سوی مدیریت دانشگاه، هر روز ابعاد گسترده‌تری پیدا می‌کند. آنها همچنین نسبت به افزایش سرخوردگی دانشجویان، گسترش بی‌اعتمادی در فضای دانشگاه و آسیب دیدن اعتبار علمی دانشگاه صنعتی شریف هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/76559" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76556">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iHFARvbEF6ZDvGJRcHrzC89XhB5GQvkX4HQHjuRBAfqE2rDKT3XC5JukQCjgQWfROjSonImXdtOq6kZ78q3tSGaChg4T6AC-0rD9jginTWUigiyfIX-PdDJaRru_EPmur_dvHNFrxNQvU9upZvMxOMrAmEOFtzuuyt3k4_WUyfALPkufKJaIhZjtIaicfpOG5YPKbR9pLKNZ0YcwdWx_qrY-XQDe2ubQF3tQ64pF7142Nm0cUFH71r6lw8Vvej2bUA9E89k410zcBEhHFiXDyzXNolVyLS0bKTgvOCNZ_wLa7LtrGn1JY9ETTC0YuDVj3OoWo45yF6dePzsPZLzEjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MjU6HGizyYoVskfK2kp8drJrQEY75Lm5TNNyiMYbooW7rcznnhtRooVQfjyV4Xq0HMao29OSjkxQt5LxrxlyNW1zHhHCaAeRHqj8rtOhSXQ3yjjhvOaIY-o7B8JzeRoSCayl_AU_s2QVyDs9GbPyiyNfQ1ohcX7q3_2gXeymxsSpblb3cGR3uBb3_LbebtokEaQz20oY21LcIATd3vsxu0advn0cUo_4OEXtRSxtgPhf091-C7Z-Boz9Mbgqbxc3PkowHoD91MbSm4geSx81Bul1aI4vR_kcXYv7ZaN9bi-PbOakbsNGHyoSsfl9Npv4CnPuFTXFtSGDtJeA4vJrbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
جواد علیکردی، وکیل دادگستری زندانی، توسط شعبه اول دادگاه انقلاب مشهد به ۱۸ سال حبس، انفصال دائم از حرفه وکالت، دو سال تبعید به سراوان و دو سال منع خروج از کشور محکوم شد. جلسه رسیدگی به اتهامات او در ۲۰ خرداد ۱۴۰۵ برگزار شده بود.
🔸
به گزارش خبرگزاری هرانا، آقای علیکردی از بابت اتهام «اجتماع و تبانی برای اقدام علیه امنیت ملی» به پنج سال حبس و از بابت اتهام «فعالیت تبلیغی برخلاف امنیت ملی» به ۱۳ سال حبس محکوم شده است. پرونده او پیش‌تر در شعبه ۹۰۲ دادسرای مشهد مورد رسیدگی قرار گرفته و پس از صدور کیفرخواست به دادگاه انقلاب ارجاع شده بود.
🔸
جواد علیکردی در ۲۱ آذر ۱۴۰۴ توسط نیروهای امنیتی در مشهد بازداشت شد. او ابتدا به یکی از بازداشتگاه‌های امنیتی منتقل و سپس به زندان وکیل‌آباد مشهد انتقال یافت.
🔸
آقای علیکردی برادر خسرو علیکردی، وکیل دادگستری و مدافع حقوق بشر است که در آذر ۱۴۰۴ به شکل مشکوکی درگذشت. وی پیش‌تر نیز در پرونده‌ای جداگانه با اتهامات سیاسی و امنیتی محکوم شده بود که اجرای بخشی از احکام صادره
علیه او به حالت تعلیق درآمده بود.
@IranRights</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76556" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76555">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JUhbjCCp08wQ7KtQsTaw1jmEQgfkGOlQPau9dhwegxat0lKq92cwY8iQHdHehdAW7h_vZ3lc8B1qEtKWuuCZ9hmuzxNywpjR1V9ys3OM7Fl_lW7KoS5SwhuUqm64FPxRK30H4V3XTFyF5hG3GaSvgfBMlZG639cNzvoPviGqkHQbd_Sa7Ad3cuCLbTcj5nPc5D8WP6fn65tOB3bhaOeQMsJ3xbMl58LLHjUyu27XRm6VZFxpN32SeejKKJ6eLaW34TJHLf3sMREXp8Lv-VSFf2dSFCtVQz8YYTKTCXLdG4RZgEflyNLKAIogHehf0oGMxeIU2XXssPm252tiH6-uhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: هیچ‌گونه عوارضی در تنگه هرمز وجود نخواهد داشت مگر به نفع آمریکا
ترجمه ماشین:
در دوره ۶۰ روزه آتش‌بس، در تنگه هرمز
هیچ عوارضی در کار نخواهد بود
،
و پس از پایان دوره ۶۰ روزه نیز
هیچ عوارضی پرداخت نخواهد شد
؛
مگر آن‌که، در صورت تکمیل نشدن توافق، این عوارض
از سوی ایالات متحده و به نفع آمریکا
وضع شود؛
آن هم بابت خدماتی که این کشور به عنوان «فرشته نگهبان» کشورهای خاورمیانه ارائه داده، برای جبران هزینه‌های گذشته، حال و آینده.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/76555" target="_blank">📅 22:56 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
