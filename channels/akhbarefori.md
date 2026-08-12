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
<img src="https://cdn4.telesco.pe/file/ijZjUCWOaUGUBrkIKEiBM-LB4InkCqHDMKWELpCmjfsxy8JxFwUGFngdG57_LyIojg-36d2Yw8HLDSX-KUJGfui_uvvgfNtXP_VBQmtISnAj81pi6z7Qozoiyw94bibFykJCTKqqJkHu65CJaXYFNoKgXd6cI_pPbvCLfPCO7_DjjUbla6uEe9qf-1006_dBPf7LCYzCSBXa70oB4rymLwaBjQqNNcSl3-aDmeNwJg-3aIOMAs96Un5AgIZUxgh3Zo1TGDxLERCTJI7_TYhKnmxqooRba0HBh5I_xXJFFtKH6coKxR_OOsSDYztMuWob3J1IfDWg_mLTnUCV30Ew-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.21M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 23:03:50</div>
<hr>

<div class="tg-post" id="msg-680716">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چه کسی تصمیم گرفت ما خاورمیانه باشیم
🔹
شاید تا به حال فکر نکرده باشید که چرا منطقه غرب آسیا را خاورمیانه می‌گویند.
دسیسه‌ای عجیب پشت این‌نام‌گذاری است.
و باز هم پای انگلیس در میان است.
ماجرا را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/680716" target="_blank">📅 23:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680715">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
سلیمی: ارزش تنگه هرمز بیشتر از بمب هسته‌ای است
علیرضا سلیمی عضو هیات رئیسه مجلس:
🔹
ما با تنگه هرمز می‌توانیم بحث تحریم‌ها و غرامت‌ها را حل کنیم و مقابله ‌به ‌مثل کنیم.
🔹
تنگه هرمز نعمتی است که خدا در اختیار ایران گذاشت و آمریکایی‌ها با این غلطی که کردند، مسیر رو برای ما باز کردند.
🔹
آمریکایی‌ها متخلفند، خلف وعده می‌کنند، دروغگو و فریبکارند./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/680715" target="_blank">📅 22:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680714">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
گاردین: با آتش‌بس هم میل ایران برای کشتن ترامپ کم نمی‌شود
ادعای گاردین:
🔹
تغییر پرواز مخفیانه ترامپ نشان دهنده شدت تهدید ترور از سوی ایران است. اقدامات غیرمعمول برای محافظت از رئیس جمهور در حالی که به طور بالقوه دیگران را در معرض خطر قرار می‌دهد، «ظاهر خوبی ندارد» و خطر «ضعیف» جلوه دادن او را به همراه دارد.
🔹
حتی یک آتش‌بس یا توافق صلح که به جنگ پایان دهد، «میل آنها برای کشتن ترامپ را از بین نمی‌برد»./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/akhbarefori/680714" target="_blank">📅 22:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680713">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
منابع عربی از حملات پهپادی نیروهای مسلح یمن به مزدوران سعودی در بندر المخاء خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/680713" target="_blank">📅 22:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680712">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ای قوم حق‌شناس
حی علی القصاص
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/680712" target="_blank">📅 22:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680711">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
موتورسیکلت‌های ایران چینی شد
اصغر فرضی‌پور، رئیس اتحادیه موتورسیکلت فروشان در
#گفتگو
با خبرفوری:
🔹
بیش از ۹۰ درصد موتورسیکلت‌های موجود در بازار از چین وارد می‌شوند و با نامشخص شدن مبادی ورود کالا روند تأمین قطعات با دشواری بیشتری همراه شده و این عامل نیز به افزایش قیمت دامن زده است.
🔹
تولیدکنندگان داخلی با هزاران مانع اداری و تأمین مواد اولیه مواجه هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/680711" target="_blank">📅 22:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680710">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6dvtRfvXogB501PGMRYijOV0nUalce3ck9kTUXRqdMjZO6Y8TxOWDgzFk7ohcXyCLR-xQsgxpGTIPfbOkQXQEfv4UZiTnw9urIOxo-pTkKzDcwosm_aOgZgQTEr3e0fTYhMVILl7FCcR8Nxkwo1pPs58Xl7X3rbMG119dG-wNyKTRKfJnriVVjYJQU_OJPQYOfXHu-5FRHD1GaBtq2Ov5EegUz0y4hbVXCz1gnUsIXkcoSM1eDsnw__j2z1HNFbAUDJqbgwD91hkL9FsV7bqB_ztmkjjrgP-QX7DdrjvSbMvs0ajcsvp37aL8yDke9iDTI8UFZgZQ4BwW_iTaSitQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تنگه هرمز تا پذیرش شروط ایران از طرف آمریکایی همچنان بسته است
متن کامل پیام نهاد مدیریت آبراه خلیج‌فارس:
🔹
ادعاها و توییت‌های پیاپی مسئولان آمریکایی درباره رفع انسداد تنگه هرمز، واقعیت را تغییر نمی‌دهد؛ تنگه هرمز همچنان مسدود است و تا پذیرش شروط ایران بازگشایی نخواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/680710" target="_blank">📅 22:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680709">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f05b26e0.mp4?token=AVbw7HfE3wPaqJjzWEJdwZOzPjskVKzXrHqSjxnRqXmNdDYfIev5m-0t2bfsNl5J21HQ6kguC2kyVpa-O4fafKVFjFQlSDEQ4L1Rx6166CIaLLmFYugfTnDJTIxVZrnQtxthV8O7AXWcHyvSCG27FozR6qWCNBYL87ljlt3LD_cHDcVziL9RO5IWrS0cFkEc8pAZD1q0AnJzIejCCnDNPdB4lOIbiMZP7ZXKlIs_B0kScWLX8x3aCqRVcOpwhyWpkeRBVSlmm6X1E-Y0ogzZFapTjkHpXJf1LZ_143Ei-ddLSHczrmThwsQA-Fa81ePvTQlgqcv4N9pFmlDFSaMQzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f05b26e0.mp4?token=AVbw7HfE3wPaqJjzWEJdwZOzPjskVKzXrHqSjxnRqXmNdDYfIev5m-0t2bfsNl5J21HQ6kguC2kyVpa-O4fafKVFjFQlSDEQ4L1Rx6166CIaLLmFYugfTnDJTIxVZrnQtxthV8O7AXWcHyvSCG27FozR6qWCNBYL87ljlt3LD_cHDcVziL9RO5IWrS0cFkEc8pAZD1q0AnJzIejCCnDNPdB4lOIbiMZP7ZXKlIs_B0kScWLX8x3aCqRVcOpwhyWpkeRBVSlmm6X1E-Y0ogzZFapTjkHpXJf1LZ_143Ei-ddLSHczrmThwsQA-Fa81ePvTQlgqcv4N9pFmlDFSaMQzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امضای قانون سقط تا ماه نهم؛ جشن «حق انتخاب» در حالی برگزار شد که صدای نوزاد شنیده نمی شود
🔹
لحظه امضای قانون سقط جنین حتی تا ۹ ماهگی در ایالت ماساچوست و تشویق فمینیسم ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/680709" target="_blank">📅 22:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680708">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDGPCrLngFU8NS_Ex9DqBQpngK_upIt4a4aSILEiL8lFxAsSrgrkhtDxo2LbPdBfRDT5YFmQ5Q8E-pXN0FrIneLZOrMfgzypl4CBpvPwK2aYZPjhky86Z5nL_FDEgWGenVwKns2DaAYFpKK1Rgsi3ZgHESxBMjUG0cWZbgc8C1_RQRSiBoiIw3kEqez2sd6_DXkIp-HW-yAfC6OilQh_paIrYtXKxKjG8btXreIHoLG5h168ZTCIIVmUtlQR9GdCZPq20hIZXT9kOdNy-Z4LE1l4-e1zXBw4piJ94cNe3OJ4UpgngYEVqMEBQZhoXILUbFrvq1ZW2taseL-rorxb-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای برخی منابع خبری: فرود یک هواپیمای دولتی امارات در ایران طی دو روز متوالی
🔹
یک فروند هواپیمای دولتی تشریفاتی امارات متحده عربی، از نوع بوئینگ ۷۳۷-۷۰۰ BBJ که توسط شرکت Royal Jet operated می‌شود، طی دو روز متوالی، برای مدت کوتاهی به ایران سفر کرده است.
🔹
این هواپیما در ۱۱ اوت از ابوظبی به سمت منطقه تهران پرواز کرد و حدود یک ساعت در آنجا ماند و سپس ایران را ترک کرد.
🔹
همین هواپیما در ۱۲ اوت بار دیگر وارد ایران شد و این بار در فرودگاه پیام کرج، در حدود ۴۰ کیلومتری غرب تهران، فرود آمد. هواپیما حدود ۳۰ دقیقه در فرودگاه ماند و سپس ایران را ترک کرد. /انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/680708" target="_blank">📅 22:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680706">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ماجرای تغییر مدیریت تامین اجتماعی در روز تعطیل چه بود؟
ایلنا:
🔹
در اقدامی ناگهانی، احمد میدری، وزیر تعاون، کار و رفاه اجتماعی، مصطفی سالاری را از مدیریت سازمان تأمین اجتماعی کنار گذاشت و غلامحسین محمدی، رئیس سازمان آموزش فنی‌وحرفه‌ای کشور، را جایگزین او کرد.
🔹
این جابه‌جایی در روز رحلت پیامبر اکرم (ص)، بدون اطلاع‌رسانی قبلی و در شرایطی انجام شد که هنوز توضیح رسمی و روشنی درباره دلایل برکناری مدیرعامل، ضرورت این تغییر و معیار انتخاب جانشین او منتشر نشده است.
🔹
گزارش‌های اولیه همچنین حاکی از آن است که سالاری نیز پیشاپیش در جریان این تصمیم نبوده؛ موضوعی که وزارت تعاون، کار و رفاه اجتماعی باید درباره آن شفاف‌سازی کند.
🔹
دولت باید درباره علت و فرایند این تغییر، رعایت تشریفات قانونی، معیار انتخاب مدیر جدید و برنامه او برای مواجهه با ناترازی مالی، پرداخت مستمری‌ها، بدهی‌های درمانی و مطالبات سازمان از دولت، توضیحی روشن و مسئولانه ارائه کنند.
جامعه تأمین اجتماعی حق دارد بداند چرا مدیریت مهم‌ترین نهاد بیمه‌ای کشور، آن‌هم در یکی از حساس‌ترین مقاطع مالی و اجتماعی، به این شکل تغییر کرده است.
📲
🇮🇷
✊
@AkhbareFori
| Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/680706" target="_blank">📅 22:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680705">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a80aca92.mp4?token=WaDXrb8lrw9-a78VQGOqtRyguPFAvKmyywFQ4EA162lwQKHs_NkEfo-fO8e0jDw7_fP567NvoQOEVekjgtznmv4NzHTU5nR2O4DJAUW2GjPexT6qfjUbXb_49pYfy1zbVpnBQCKivtn1fPY4u20h_ifKQ7P9TOjG3aBuwa96ZWhJqXeCuPkYD2HYdrNX4A_DTfKB1nezHHHMbft0Dx6p5MvxMqQ0vaccBojCd7YGQfI2NxP7o_wBtgiDzqokBGGc2jxAOvdSPmpbWW0oDqzOgeUmfRtertnrmHXUTmmHFmcguwtAofgvJdkSGhTVCFfaj00ul99Mp2iT9JkGr73BAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a80aca92.mp4?token=WaDXrb8lrw9-a78VQGOqtRyguPFAvKmyywFQ4EA162lwQKHs_NkEfo-fO8e0jDw7_fP567NvoQOEVekjgtznmv4NzHTU5nR2O4DJAUW2GjPexT6qfjUbXb_49pYfy1zbVpnBQCKivtn1fPY4u20h_ifKQ7P9TOjG3aBuwa96ZWhJqXeCuPkYD2HYdrNX4A_DTfKB1nezHHHMbft0Dx6p5MvxMqQ0vaccBojCd7YGQfI2NxP7o_wBtgiDzqokBGGc2jxAOvdSPmpbWW0oDqzOgeUmfRtertnrmHXUTmmHFmcguwtAofgvJdkSGhTVCFfaj00ul99Mp2iT9JkGr73BAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
غریبانه آمد، غریبانه زیست و غریبانه به شهادت رسید؛ اما قرن‌هاست که میلیون‌ها دل، در پناه گنبد طلایی‌اش آرام می‌گیرند
🔹
سالروز شهادت امام رضا (ع)، امام مهربانی‌ها و پناه دل‌های بی‌قرار، تسلیت باد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/680705" target="_blank">📅 22:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680703">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
نیویورک تایمز: ترامپ ممکن است بخواهد خاورمیانه را رها کند، اما خاورمیانه او را رها نخواهد کرد. ترامپ در آخر هفته گفت راهبرد جدیدش در قبال ایران این است که «کم‌سروصدا عمل کند»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/680703" target="_blank">📅 22:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680702">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f490de586.mp4?token=o5U_lCYVl45E_g4izwkRFEnUi1417Lc556zWthJtIjmrF2LgpHoMW2P_5ET1sX_o-fmqnYgjtZylc9crYMvgCCcwL8AmXRCDX8ZY6ECHHz9gmsp6sXgH1RAsqx5_CKDzcn5bxM_mkIYqFCU-Nj1YS4IB-hfPK818pAd_RdjUEV-ZjfyaNelOnHIUgQYCPvvvLCxXbtiryo97XJD1QT9zah9SVhqWCErQV8D36iMgs8AZJV_i8l3tHp-sfTlu9bOxzN38FrKLNzAPIjS1DCLDuZBQ0GU5S0GO9U-EpkziNa_i4P-5ih2_Me05zNJ6NPr4cxOHKkaFgkQ7s7mzYHMxFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f490de586.mp4?token=o5U_lCYVl45E_g4izwkRFEnUi1417Lc556zWthJtIjmrF2LgpHoMW2P_5ET1sX_o-fmqnYgjtZylc9crYMvgCCcwL8AmXRCDX8ZY6ECHHz9gmsp6sXgH1RAsqx5_CKDzcn5bxM_mkIYqFCU-Nj1YS4IB-hfPK818pAd_RdjUEV-ZjfyaNelOnHIUgQYCPvvvLCxXbtiryo97XJD1QT9zah9SVhqWCErQV8D36iMgs8AZJV_i8l3tHp-sfTlu9bOxzN38FrKLNzAPIjS1DCLDuZBQ0GU5S0GO9U-EpkziNa_i4P-5ih2_Me05zNJ6NPr4cxOHKkaFgkQ7s7mzYHMxFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
امام رضا(علیه السلام) ميفرمايند: "هرزائري كه مرادرغربت زيارت كند، در سه موقف هولناك به يادش هستم:
اول درهنگام سخت مرگ وجان دادن
دوم در زمان سنجش اعمال
سوم در لحظه ي عبور از  پل صراط."
@Heyate_gharar</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/680702" target="_blank">📅 22:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680701">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ایران هشتم جهان در مالکیت رمزارز؛ ۱۵ میلیون ایرانی رمزارز دارند
🔹
بر اساس گزارش TechRasa Insight، حدود ۱۵ میلیون ایرانی در سال ۱۴۰۳ مالک رمزارز بوده‌اند. این داده بیانگر این است که  ۱۶.۷ درصد جمعیت کشور، رمزارز دارند.
🔹
این نرخ حدود ۲.۴ برابر میانگین جهانی است و ایران را در میان ۳۱ کشور بررسی‌شده، در رتبه هشتم جهان قرار داده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/680701" target="_blank">📅 22:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680700">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
گاردین: چند ملوان ناو آبراهام لینکلن قصد پریدن به دریا را داشتند
🔹
خانواده‌های نظامیان و اعضای کنگره در مورد تشدید بحران سلامت روان در ناو هواپیمابر آبراهام لینکلن هشدار می‌دهند، چرا که ۵۰۰۰ ملوان و تفنگدار دریایی این ناو، استقرار بی‌سابقه‌ای را در دریا که به جنگ با ایران مرتبط است، تجربه می‌کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/680700" target="_blank">📅 22:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680699">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/907149645f.mp4?token=reiQgtbaJz_pocSYU-Cg5FRQMxSZstC677YcXNUUfRGBUUresNEKUzP0HJkZUfWX1FkdICHTosgYKbUeWk8Sr6cbwHZqZ17jjpe8O6Igbb8gtqD1Gh4L52wnaZ7j058RyJDnGidKzk0yBLEskCkt7gXiVygljqaXG77JFkQNMRGRZWjwMCLfepH-3FixdY2JIP96hkR_yrD2mUy7-FOUXRQfCVztExreTqufrHepCKqxJRr4Jeks30Vw67_9rpMRCMatfZn5kukLMjgib9eomiNWnvZRgFlovbYSjWrMd3hS0o0SxcXEI4qS7XvXAyNXckLtrZgbgBgQ3ed4Aiwk7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/907149645f.mp4?token=reiQgtbaJz_pocSYU-Cg5FRQMxSZstC677YcXNUUfRGBUUresNEKUzP0HJkZUfWX1FkdICHTosgYKbUeWk8Sr6cbwHZqZ17jjpe8O6Igbb8gtqD1Gh4L52wnaZ7j058RyJDnGidKzk0yBLEskCkt7gXiVygljqaXG77JFkQNMRGRZWjwMCLfepH-3FixdY2JIP96hkR_yrD2mUy7-FOUXRQfCVztExreTqufrHepCKqxJRr4Jeks30Vw67_9rpMRCMatfZn5kukLMjgib9eomiNWnvZRgFlovbYSjWrMd3hS0o0SxcXEI4qS7XvXAyNXckLtrZgbgBgQ3ed4Aiwk7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وندی شرمن: ترامپ برای بازگشایی تنگه هرمز ناگزیر از دادن امتیاز به ایران و لغو تحریم‌هاست
🔹
مذاکره‌کننده پیشین آمریکا در مذاکرات هسته‌ای: بعید است فشار اقتصادیِ بیشتر از سوی رئیس‌جمهور آمریکا باعث تسلیم ایران شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/680699" target="_blank">📅 22:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680697">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MHqxMw8jr9pz07TaNhDt5qEUZSBoce76lKF5A0AokLQ9nmkZS3mgOdw479viUG-b_QIow0pNi42Sgn2jIJZwd9iLNH4vJ-OnwlaCd008sN5f3JG2sQ-mQhK8TpQaWwykhdzYjcUy1w4MOc-0QvsixfWjXl5mZ1JhL3dH-szSGTrAsuNrwSSr4YrO0zQXh7wkDZb-4rNpma3TwWxVbjYQk_UCmUBDZG4gylfoSjxXrzC5zhurp-IpzosQmZQXg5QjLVdUp9jy8I9Ll7L2ILOomHsHBw-F2siF7lKQGpkjzR3DeW2a6RnWKKOyecJY7rk7I5x19xN-qEh3srJiSoUItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEd1OZ1Mu74sQE5lMU_H5S1S4UEzQbZwSHoODT5L_vXnKjFNgmK-3BgSy_jry4aOwbEyc6GLMKk5b7GuXyRU367qsKcOVqiU0b4lzyK-iwZyLfhf5Lcs7Guowms0n936hnCAsORMKZQXL_ijN2UiP_kCROEpeDIJzxFAD24awgXRYiRZIryLRRp3_4DHkhWF8clG5pGJ9avU6xicQfu6Nl9GC3EGdN-UZQumKQ8cEwu_hhwImEttmQIbT3bzhn7EN_XnnhHbvbmnx7ijRPKq6M7b4aNLWYE0H51zcEySoiXQl9NhNeElnrXxuVrH7RYGVQoRYrUi6hoaNX-GzP8brA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خورشیدگرفتگی کامل، آسمان ایسلند را تاریک کرد
🔹
سازمان رادیو و تلویزیون ملی ایسلند (RUV) تصاویر دیدنی و نادری از وقوع پدیده خورشیدگرفتگی کامل در آسمان این کشور منتشر کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/680697" target="_blank">📅 21:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680696">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4372b072f8.mp4?token=cN3DaMXdj4LNU21MgvXSdMfjO3PbY5fKMOjqEA6yZ9p0S7v79g_mDETdff1zjee5mKUuJmDLQHuxbTTlNPF-lum0k7aqiCGtemnvZbLrWvA1Jmdyt6ApJUT8c0FSk2sZTHoS7CFcqMb95CopPPdiBtINxnMcGSKuDEZ_Yts95U0umNGrCbkxSGRPboREefPsxDOzoB3621QxrGYIfY7FdaB-_rCAmlT7UNHwNqLMEiWi5tAkJFbuGeApyZxkpuFw567BKSm-7ezZJiIYoWaHBpvZhpzgfeVuZ1JBX6bNhGVn6_WDLfUzQTA4bUMT9O74tjvMFQBB7LjN2oSMdxCd2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4372b072f8.mp4?token=cN3DaMXdj4LNU21MgvXSdMfjO3PbY5fKMOjqEA6yZ9p0S7v79g_mDETdff1zjee5mKUuJmDLQHuxbTTlNPF-lum0k7aqiCGtemnvZbLrWvA1Jmdyt6ApJUT8c0FSk2sZTHoS7CFcqMb95CopPPdiBtINxnMcGSKuDEZ_Yts95U0umNGrCbkxSGRPboREefPsxDOzoB3621QxrGYIfY7FdaB-_rCAmlT7UNHwNqLMEiWi5tAkJFbuGeApyZxkpuFw567BKSm-7ezZJiIYoWaHBpvZhpzgfeVuZ1JBX6bNhGVn6_WDLfUzQTA4bUMT9O74tjvMFQBB7LjN2oSMdxCd2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده کنگره آمریکا: ترامپ بیش از حد بی‌کفایت است
جیک اوچینکلاس، نماینده کنگره آمریکا در شبکه فاکس نیوز:
🔹
می‌دانم که دونالد ترامپ برنامه شما را تماشا می‌کند، بنابراین مستقیماً خطاب به او می‌گویم: «آقای ترامپ، شما نخستین رئیس‌جمهور تاریخ آمریکا هستید که شخصاً جنگی را آغاز کرده و سپس در آن شکست خورده‌اید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/680696" target="_blank">📅 21:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680695">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
تهدید یمن به حمله به میادین نفت، برق و فرودگاه‌های عربستان
🔹
«محمد البخیتی» از رهبران جنبش انصارالله، نسبت به هدف قرار دادن میادین نفتی، فرودگاه‌ها و زیرساخت‌های برق و آب عربستان در صورت وقوع حمله همه‌جانبه از سوی ریاض هشدار داد.
🔹
البخیتی با تاکید بر اینکه عربستان خسارت‌های خود، به‌ ویژه تعداد کشته‌ شدگان را پنهان می‌کند، به یمنی‌های حاضر در اردوگاه‌های نظامی عربستان، توصیه کرد برای حفظ جان خود از این اردوگاه‌ها خارج شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/680695" target="_blank">📅 21:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680694">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: دشمن قصد حمله زمینی از مسیرهای غرب کشور، خارک و قشم را داشت که با واکنش یگان‌های نظامی و نیروهای مردمی، این نقشه در نطفه خفه شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/680694" target="_blank">📅 21:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680693">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
المیادین: کشتی‌های بزرگ به دلیل مخاطرات موجود امکان عبور از تنگه هرمز را ندارند
🔹
یک منبع سیاسی امنیتی ایرانی در گفت‌وگو با شبکه المیادین اعلام کرد که تنگه هرمز بازگشایی نشده و جمهوری اسلامی ایران هیچ تغییری در سیاست‌ها و ضوابط خود در این آبراه راهبردی اعمال نکرده است.
🔹
این منبع نسبت به هر کشتی که مقررات و دستورالعمل‌های جاری ایران در تنگه هرمز را نقض کند، هشدار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/680693" target="_blank">📅 21:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680692">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
حمله توپخانه‌ای مزدوران سعودی به مدرسه‌ای در تعز
🔹
شبکه المسیره یمن گزارش داد که مزدوران سعودی، با حملات توپخانه‌ای یک مرکز آموزشی را در جنوب استان تعز هدف قرار دادند.
🔹
این حمله، محیط مدرسه ۱۴ اکتبر در منطقه «الأعبوس» واقع در شهرستان «حیفان» را هدف قرار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/680692" target="_blank">📅 21:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680691">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5257bba3b9.mp4?token=I7LZYkka_RyKv3lO1p38Ym__IIdv0jzbBOBbxr-iiC_8AnEZHMRbefAbKp8iufFZWEcHobrOIThsN5rwXEhyNfUHLSjb5TWXCWcl3pSuwguqn45wA1VYHtCRSoiMiZ_wPc5CuHvH3b4a2Y7weryhK8Az4ttlhWFvgs5HAcE6byq29oWxXas2lCx7C5C0sWDKI-KkI6tejPSKif7tzfa9xlXSrbbzbRrkrClFs90nR5Lej38gpSSXXRiwuddGpOG2KqnyuZ1HeW0T-v5ISv3KW6Yo2lr357OrR-vK9gMZ8xjVJgtnA7tq7Ds7hVLt4G0rcoy9IfsCl1Me1r5sbWtksA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5257bba3b9.mp4?token=I7LZYkka_RyKv3lO1p38Ym__IIdv0jzbBOBbxr-iiC_8AnEZHMRbefAbKp8iufFZWEcHobrOIThsN5rwXEhyNfUHLSjb5TWXCWcl3pSuwguqn45wA1VYHtCRSoiMiZ_wPc5CuHvH3b4a2Y7weryhK8Az4ttlhWFvgs5HAcE6byq29oWxXas2lCx7C5C0sWDKI-KkI6tejPSKif7tzfa9xlXSrbbzbRrkrClFs90nR5Lej38gpSSXXRiwuddGpOG2KqnyuZ1HeW0T-v5ISv3KW6Yo2lr357OrR-vK9gMZ8xjVJgtnA7tq7Ds7hVLt4G0rcoy9IfsCl1Me1r5sbWtksA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر آخر ماه نمی‌دانید پولتان کجا خرج شده، این محتوا مخصوص شماست
#چرخ_زندگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/680691" target="_blank">📅 21:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680690">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
وال استریت ژورنال: حتی اگر آمریکا از نظر نظامی بتواند مسیر هرمز را باز نگه دارد شرکت کشتیرانی ممکن است اصلاً وارد آن مسیر نشود چون امنیتی ندارند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/680690" target="_blank">📅 21:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680689">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccad136da2.mp4?token=r6_oJAhfZvq7mjTnGZCJh1iA57ZxE29P0mx0flw87AC6A6OkFDqLPVY6vaBs6HpZc4wQ1422BH32PAdbjoV4f2oX3WBlnWqjc5uDA9O28RxYf4m3d-SPi_SsrzIxZ0WXX7PMOdrsxRNiIo9_8WI17oOrldIoDZCJ3aHN1oeRvmOX47zjCgiil2jxTJs8Z0JbjelPlyI7rtyjXDQxF0K1oUlLeyB-pO0VK2-ZHk263Ynu79ewkb-1RU-OJCl5RWfNcdG2ea1zDFEEAGmbBd5xhaiKBLpzj0YrBqi8wAPaYw57kVuTCNl2FXGh7WwXWrT7i8v5r-agLmNa17P8pSL9zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccad136da2.mp4?token=r6_oJAhfZvq7mjTnGZCJh1iA57ZxE29P0mx0flw87AC6A6OkFDqLPVY6vaBs6HpZc4wQ1422BH32PAdbjoV4f2oX3WBlnWqjc5uDA9O28RxYf4m3d-SPi_SsrzIxZ0WXX7PMOdrsxRNiIo9_8WI17oOrldIoDZCJ3aHN1oeRvmOX47zjCgiil2jxTJs8Z0JbjelPlyI7rtyjXDQxF0K1oUlLeyB-pO0VK2-ZHk263Ynu79ewkb-1RU-OJCl5RWfNcdG2ea1zDFEEAGmbBd5xhaiKBLpzj0YrBqi8wAPaYw57kVuTCNl2FXGh7WwXWrT7i8v5r-agLmNa17P8pSL9zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی از زیارت «آقای شهید ایران» در رواق دارالذکر حرم رضوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/680689" target="_blank">📅 21:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680688">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آقای ترامپ! ایران نه ژاپن است، نه ویتنام...
🔹
یک فرمول قدیمی در واشنگتن وجود دارد؛ بمباران کن، هزینه بساز، محاسبات طرف مقابل را تغییر بده و بعد پای میز مذاکره بنشین. آیا «مذاکره با بمب» در برابر ایران جواب می‌دهد؟
🔹
این ویدئو روایتی است که حالا سردمداران کاخ سفید به آن رسیده‌اند‌.
@Tv_Fori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/680688" target="_blank">📅 21:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680687">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8c4a0cde1.mp4?token=dQiJD2FJlpwOf8bMg0fYhoHGvzSSPjScZduh5t_HtfifsTuYVN4R3G_SxAe9vy8h67MKy1jwKFVWBgzgl-anLPcLVXzBPG7MMxw7r2XQ3x7k0LKSIRpdS_8cRswEdkltsOSv_sd4JHGlohmyHcgtFLMFZj-MVzCHRsaLiU74wjy5fhaUOvl6IEwyEnmHkDcxKPZY7JDPBU5rRPE8-fgGOxtzfOwZCWNYytisL-0AOjYL48zpgyb35Gsn6HPgKeslQEGdDD5qwU7wo4tmAoHoe5UG1SZGCb0u4n8iO1c2UVdm9C0SbMX3cAoD33TCSF0HZoLIUQa4t1TCYREPCEXq_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8c4a0cde1.mp4?token=dQiJD2FJlpwOf8bMg0fYhoHGvzSSPjScZduh5t_HtfifsTuYVN4R3G_SxAe9vy8h67MKy1jwKFVWBgzgl-anLPcLVXzBPG7MMxw7r2XQ3x7k0LKSIRpdS_8cRswEdkltsOSv_sd4JHGlohmyHcgtFLMFZj-MVzCHRsaLiU74wjy5fhaUOvl6IEwyEnmHkDcxKPZY7JDPBU5rRPE8-fgGOxtzfOwZCWNYytisL-0AOjYL48zpgyb35Gsn6HPgKeslQEGdDD5qwU7wo4tmAoHoe5UG1SZGCb0u4n8iO1c2UVdm9C0SbMX3cAoD33TCSF0HZoLIUQa4t1TCYREPCEXq_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاصیت تفاله قهوه که ازش بی خبری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/680687" target="_blank">📅 21:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680686">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
سخنگوی جنبش النجبا: سلاح خود را تحویل نخواهیم داد
🔹
موضوع انحصار سلاح در واقع فقط سلاح مقاومت را هدف گرفته و ناشی از فشارها و دستورهای آمریکا و اسرائیل است.
🔹
اطلاعات منتشرشده درباره تلاش برای ترور الزیدی، داستانی است که آن را باور نمی‌کنیم و هدف از طرح آن، تحریک افکار عمومی علیه گروه‌های مقاومت است.
🔹
توافق‌های اقتصادی با واشنگتن، عراق را از اشغال نظامی به اشغال اقتصادی منتقل کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/680686" target="_blank">📅 21:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680685">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
معاون وزیر کار: نقص اطلاعات فراجا، کالابرگ برخی افراد را قطع کرد
🔹
پیگیری‌ها از وزارت رفاه نشان می‌دهد کالابرگ برخی افراد حاضر در کشور به‌‌دلیل ثبت‌نشدن اطلاعات ورود در سامانه فراجا متوقف شده و وزارت رفاه پیگیر اصلاح این اطلاعات است.
🔹
افرادی که صرفاً به…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/680685" target="_blank">📅 21:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680684">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26989930eb.mp4?token=hFsF73H9HfytnuAqfZOTBYEjc8E2UFAu0BxUGwvTTgIucvJ4jDL7iCVNcIxRGBiLMrWGo9BG6Qth8dZFk4VYk08hnie2xeg0qAm3vlj3DhOSdgNGFPvQS2Ibko0bI36OG2dTd9arM9F8Z3xfWYV2kYiAj1q8wpFeOHqp4lXjeFBzC58H_rQ1BlgpuvbxZgXIsj23Lczbl3lSSPtGxVLz1gDWTnqOVNLCq1bfdaiboPA1aOycGVpJY7g4Oi-ac6QRUOiasQyFDGF8rc-49ROq067dS5JIxCFlx0k-FU_Ghs1U2ihjAnEAfCtLVBLr83yfUFk4wBtiYWyNoNf9dlzTSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26989930eb.mp4?token=hFsF73H9HfytnuAqfZOTBYEjc8E2UFAu0BxUGwvTTgIucvJ4jDL7iCVNcIxRGBiLMrWGo9BG6Qth8dZFk4VYk08hnie2xeg0qAm3vlj3DhOSdgNGFPvQS2Ibko0bI36OG2dTd9arM9F8Z3xfWYV2kYiAj1q8wpFeOHqp4lXjeFBzC58H_rQ1BlgpuvbxZgXIsj23Lczbl3lSSPtGxVLz1gDWTnqOVNLCq1bfdaiboPA1aOycGVpJY7g4Oi-ac6QRUOiasQyFDGF8rc-49ROq067dS5JIxCFlx0k-FU_Ghs1U2ihjAnEAfCtLVBLr83yfUFk4wBtiYWyNoNf9dlzTSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دادستان قشم فرمان مهار فوری آلودگی نفتی سواحل جزیره را صادر کرد
🔹
دادستان عمومی و انقلاب شهرستان قشم با ورود فوری به موضوع آلودگی نفتی مشاهده‌شده در بخش‌هایی از سواحل این جزیره، دستگاه‌های مسئول را مکلف کرد ضمن شناسایی منشأ آلودگی، عملیات مهار، جمع‌آوری…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/680684" target="_blank">📅 20:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680683">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
معاون اجرایی ارتش: بیش از ۷۵ درصد توان موشکی و پهپادی ایران دست‌نخورده است؛ ما نظامی‌ها پشت سر دیپلماسی حرکت می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/680683" target="_blank">📅 20:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680682">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
واشنگتن‌پست: بودجه بازسازی کاخ سفید ترامپ بدون اعلام عمومی به نزدیک یک میلیارد دلار افزایش یافت
🔹
روزنامه واشنگتن‌پست گزارش داد بودجه بازسازی کاخ سفید در دوره دونالد ترامپ به‌صورت «محرمانه» به نزدیک یک میلیارد دلار افزایش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/680682" target="_blank">📅 20:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680681">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDy7b53z_vZ9PnEQCI8VFUH4nsE4GCAkYcbQq5CB5PhOkPBMGCIC3uGs9nEIIEVKQqcZeODksnOpt5lM3_Or5M2B1VPsQvpKno4aplbu5s5-poo9xWCNfHWrjj4DcBqNgc1BgXD39w9K4PYL9hzjzejuRS_LXG-77MJLiiLRK69pNpMfsONLLF9qtPeygTNaAhQz1yd25OqAITq9QvgZlR9W99tQ9LUYX_d29jnzTv8QWk6gNlfNDG3eB8UzzKaSRR1cO09nsmjInKJHaNLlCQEhH3YQN0eSU1t4a69ksNi45Zk-X8m7OQew9ql_6F0DKTVgatUQu9uK5_qGsUYeCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک‌تایمز: ایران موشک‌های پیشرفته‌ای دارد که می‌تواند ناگهان تغییر مسیر دهد و سامانه‌های دفاعی آمریکا را در هم بکوبد
نیویورک‌تایمز:
🔹
آمریکایی‌ها با توان جدید ایران مجبور شدند تا ذخایر کمیاب رهگیرهای پاتریوت را بسوزانند. ایران در دور اخیر جنگ با استفاده از موشک‌های پیشرفته‌ای که می‌توانند ناگهان مسیر خود را تغییر دهند، سیستم‌های دفاعی پایگاه‌های آمریکا را در هم کوبید.
🔹
ایران با پیشرفت جنگ به دشمن ماهرتری تبدیل شده و یاد گرفته است که چگونه از پدافند هوایی ایالات متحده فرار کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/680681" target="_blank">📅 20:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680680">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
سفیر پاکستان در مسکو تاکید کرد اسلام‌آباد هیچ مخالفتی با پیوستن ایران و مصر به توافقنامه دفاعی مشترک با آنکارا و ریاض تحت عنوان توافق مکه ندارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/680680" target="_blank">📅 20:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680679">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d16aec8d.mp4?token=JzNCaUt6oitbXKImkFecTIeOsfkRvp9MT9EwBIljgEdshcJM5QEyIGjvfPe_5_bf0zFT973YVHCqF33i6H_NronHfj7DII3UHYq49558-ACC6yuBY9bi0mnP7fKEXyKPXyid287WFYVS5gr-k9zkvhb16e93wVU7PBRj0MYWodNGiogu0AQ3ZikE5mFOZq6YWh_0bRL8r8ieteaY00xKefTPMuRoCJWee58_5miHTfM8vG8_xfEbwiaup2J9_mWkt8KSU1ISbS02x5exOLw0zPOaa2r2SqtqsEl1EVW2lefxA9JTjLZaF0nMcNB2GF14HdDeE30AtrHvuv2RDAAzvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d16aec8d.mp4?token=JzNCaUt6oitbXKImkFecTIeOsfkRvp9MT9EwBIljgEdshcJM5QEyIGjvfPe_5_bf0zFT973YVHCqF33i6H_NronHfj7DII3UHYq49558-ACC6yuBY9bi0mnP7fKEXyKPXyid287WFYVS5gr-k9zkvhb16e93wVU7PBRj0MYWodNGiogu0AQ3ZikE5mFOZq6YWh_0bRL8r8ieteaY00xKefTPMuRoCJWee58_5miHTfM8vG8_xfEbwiaup2J9_mWkt8KSU1ISbS02x5exOLw0zPOaa2r2SqtqsEl1EVW2lefxA9JTjLZaF0nMcNB2GF14HdDeE30AtrHvuv2RDAAzvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشتار در مهدکودک مینه‌سوتا؛ ۳ نفر از جمله یک کودک کشته شدند
🔹
پلیس آمریکا اعلام کرد در پی یک حمله چاقویی در یک مهدکودک در ایالت مینه‌سوتا، یک مرد، یک زن و یک کودک جان خود را از دست داده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/680679" target="_blank">📅 20:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680675">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjlc9FeDTgT5yyeUdrBurzUroXgbwFNEa1LM7gj6lvsTKCtIg1ZqKifM1qpbA2-Yc1rql3ogn7jgNW4bkI4cf-A8MQ1fXWWSJ9tTdIwgbozNp9WKB42B1DF2f4s_GrUCNcU4G2-OZWqToDNKztJZBCMpAYEqjDVei4U8FIy_XTszhXPHvCcTl5bHYF92V_PSmmXRvME3vZd02WM7-ynSQgbNTcbxl0E5ZbeesDBnhcChi9Upec9WqDLH-NV8OYJE2FBGCzXozshnbdJLyAOHw22aiHB2GbPRA1s3FB1iVwl1aOGA4MAe9eQ7mmSL_RJbw1YZ1nxrxgs8JYOk1CTL3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YGdiKXY5ZAxFELoqWOC1lq8ENTKi-n-jqRkLLZJhfvIdaCUM5jaEQaYsQA55xgkyLkdEnWLVu46HKLSvMUCwoL8t1NP3EBZGe3IH1k9twXV3KWmnviDSlNScPDZ9sv9XTjZfsz2b89Miy9Be1QMAdO-DN9Zq-WujE1LhQDmHTCEMmcn9BJawsSv9VOlOpsatDmNqaPaJSSdcZxznBfxtuqf7pd8DIZ3wHCcBAss8jHFSSHK34j7uMUKMbO5GSgwD3T--etc-1EWZrKtfkjlo0z9krrMa6Wra3KfJ_RUmjijW4AIPJ6-HBGAEwP7DuZHPMPWpmt2THQiO1KoIFq823w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hfuBGowukYEbYKIcYweKTVmEpiX_HYoejFLbL9Lmc7RGCC7MFjTyiUkrLLK5Sgc1kbsiGpAKbs8rxJQB8iVAyHYmq_CB41Yjv5BWdcehZtVC-lJYXzF4-SeY4r1JbXcxDKLM5KgAV1aLxI2bfulHGtmCRavcqevCeOanrTP7_egK_PuQl-as9k5YDz7S3lwcmtmom1_I0mVK4s_I2CbW9dwvQ06dEgNrXAXQH6I7rQln5vPZO3pDacpyLAIAYVd4e9eTzVYgLL2h9a59LCGaNNn2w4NBMdfaQ875cO3XCJ1xAPAGLlzu9iWcNxKQGQiaGWZBMOKj-539SU3Uwg0JZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hXLJTyHkg6sVEqsGEd6klHUzGxkowI2BDMqxRHhHanpMybHgYLBUv8DVgb848UY2LbVfOIrGl2t3CRYD75WDQO7EAnpGGGPNK6_Sszf40tKV7QBV6xbXId4ECdtJC8ruh9m23HwUVTyTV9PSgzBGbdJGfx4LjZkNchVW4KFSarDMKiUOT_Bcx3xh_6avsJfeUbEavy63oKMKcxwhNr7R4FAmwMkjNJo9yBEObwGLaAy6km51B8cRnpM2dpGhLmeSwlZPBDBFNIhnKotaNlqgO-tCfcFSx61wakeXvJGgQ-hdcdwKhm74IecR51kcCDwRUr2tp8QHOnHs4p6BdJaDMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اوباش صهیونیست قرآن را پاره و به آن اهانت‌ کردند
🔹
شهرک‌نشینان صهیونیست عصر امروز حین حمله و تخریب یکی از خانه‌ها در منطقه «بیر قوزا»، در شهرک «بیتا»، واقع در جنوب نابلس، قرآن کریم را پاره کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/680675" target="_blank">📅 20:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680674">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
ازدحام جمعیت درجوار آرامگاه آقای شهید ایران، رواق دارالذکر همزمان با شب شهادت امام رضا علیه السلام
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/680674" target="_blank">📅 20:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680673">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVYu03ykvExcFGDBfFxQ3Zsk9HKbsWqVCRH64vYpAEuMUA1qLXe1xnq1fWwQO-op7JKLS8u6DMwshIxPJ5OJPbWu-4r06LDadiMGsmuoL2RHKI4S6hIiQlKcw_gQxoDUfybQiPsVx84JsBYNyWqugplYeLWw3ChEtjRtat4gF9HNTKg3KQHFNvPMg0CIjxclHQD46iQE6maKCWm1qRNXrlt3LnYHmxuEXPl852bv3GbMHw0sw_IKs8bhmnVmL8Y1dTz7eP60jQZ1ElyUkBSyz8iD_W_K4Nw5Wfjd5P0ppt0Kv4lq7epHnW_f-wCcUbn-6n1-PieyCbh9lXhSo5fuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
♦️
روضه خوانی مرحوم استاد ایرج خواجه امیری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/680673" target="_blank">📅 20:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680672">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAH2wl5kHKiKCykFv5gujiRQw7oxTVLmUkUBsM40wslqtyu1UpOvN07m39tIfTyItAB_MUZeRqNyaAJBxHEeZWc2i_VYiTIH3RHNM9ZsuCpSzCAdSV3yOnzAE0K3x-g7uhp0fOd3CfaOqATv6AilQA0gk-5DZ3vKbzZfhFvLa9o3YJRiij161zNPXHnGa9Tkc-NClkF8wDsrH9xe9axRxqG90P-lxF9R6cI1W0-oXPv7zZZlzrzaJB_9oczn3L74COoLUREV1OtL-aLeKa_GSTUIPR7vDCBRdgeRfBmt-HxMCX66IxZzPtmIxb84tiIna2XNF12RfBzQUfqG7Q_VxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: هرجا قانون در برابر قدرت سکوت کند، آنچه فرو می‌ریزد صرفاً یک پل یا نیروگاه نیست؛ بلکه اعتماد بشریت به امکان حاکمیت قانون در روابط بین‌الملل است
سخنگوی وزارت خارجه:
🔹
امروز، ۱۲ اوت، سالروز تصویب چهار کنوانسیون ژنو در سال ۱۹۴۹ است؛ کنوانسیون‌هایی که هسته اصلی معاهدات بین‌المللی مربوط به قواعد بنیادین حقوق مخاصمات مسلحانه را تشکیل می‌دهند؛ قواعدی همچون «انسانیت»، «تفکیک»، «ضرورت نظامی»، «تناسب» و ممنوعیت «رنج غیرضروری» که با هدف متمدن‌کردن بشریت و انسانی‌تر کردن جنگ وضع شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/680672" target="_blank">📅 20:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680671">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXAoZhyaaY1te26VpOzbte0bQ0vWFZTWrVYJzjhe2ZHKY2BeftirbkcxMddQDcLwkmjAUuVipOA3cTn89T6uYQUtfYBxCCgTuLurWIHl2w6VPduzbIaybNn4m_1ine2kv5GBglQLvgLGBnGZjVgxtrtoqncdhw_qhQxJVNXqtaA8lnRCR2j66nT5N2RNarQ2naLAuGnwQNa1RobHaT0zLsok6QnbLFAZ8lOFBBAcPZVts5ztOHmxsvBPZdu-hTtb03727Bu_lyV5VvTA5cF9ncLCrkJUcwc7AQHBWgX11xO6bCbrdb5b0oXToEv85PwiU2bEAgpNBu8dULqCkBYm4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سوپرمارکت‌ها چه می‌فروشند و سودشان کجاست؟
🔹
بر اساس گزارش سالانه بازارهای خرده فروشی، لبنیات با سهم ۲۰.۴ درصد، صدرنشین است. خواروبار و کالاهای اساسی با ۱۹.۴ درصد و شیرینی و تنقلات با ۱۶.۶ درصد در رتبه‌های بعدی قرار دارند.
🔹
نوشیدنی‌ها ۱۴.۱ درصد، شوینده و بهداشتی ۱۳.۶ درصد، دخانیات ۹.۳ درصد، یخچالی و انجمادی ۴.۲ درصد و لوازم مصرفی ۲.۴ درصد از بازار را به خود اختصاص داده‌اند. چهار گروه نخست روی‌هم‌رفته بیش از ۷۰ درصد بازار سوپرمارکتی را در اختیار دارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/680671" target="_blank">📅 20:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680670">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
وال‌استریت ژورنال به نقل کپلر: از میان ۱۶۶ مورد عبور و مرور دریایی، تنها دو کشتی از مسیرهای تحت حمایت آمریکا استفاده کرده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/680670" target="_blank">📅 20:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680669">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
بنزین ۸۷ هزار تومانی در کرمان عرضه می‌شود
🔹
معاون هماهنگی امور عمرانی استاندار کرمان از آغاز عرضه بنزین با نرخ تمام‌شده پالایشگاهی به مبلغ هر لیتر ۸۷ هزار و ۲۰۰ تومان از بامداد پنجشنبه (۲۱ مردادماه) در ۲۰۴ جایگاه سوخت استان خبر داد.
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/680669" target="_blank">📅 20:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680666">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uoIL9AqECrDm_-SBn_l7gdgIB-gN-dJHLRlGYUsXVIVt6EbrAtP2vz1Fo0Li77oU78yovPLbK8ZY7boQgxViLCo_1NIihuPNuXCOzMRhBsbd0plMRqXCxjHojhGuocjY5dNKQV-3sGdAfshgcOFBqs7FrkTlKaN5szeFdhwPv3Rqco81Q5goj1N9KfCJjjTdWjaoOj19rrk5j6YUq8ptEfyAgstneijTbEsa0_3PK3xtePIGNXpb5GA7EtQznMze7thx3YKWE3zwIOhaTij8iJzZuD1SSYkbnPwK-Ckqua-murkXgd4xkbUwWpWViVrKdsamIp98pOrHn_cRYhM_tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XmzmV2RWDx196CmPQdep8oWfIJfeWwZt7ozUv2zBmbgVMs77oM10Ao-WJQ59CCCr79nhieMVXlIk055_y1M-mu41NJFSrqsD0jMXW9v66H4RFI58nG50l3uqD1vYI_pXatezuJYH3XqpCim7VsJIqfnOecwa_Cfxdrb1OrP1cUACk_7y60xV_KZG8RWwWJBoLon6S2QkMtN-G6AL0v7dQlkOdEFHXUazoA-qNeV2wzt1_7BzwDlgCy6ILY1VS9zWAsvvEOwM6eMUL1jhY1E5dmTos2aj45J_LKMqJACmgn_EgN9kD7zTcbeBS7mK5NeO1egR57QDfif1rDs02koEnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WR3KNL92OV1qrJTfbyL2eUk60D3dPR6rudmgdPSUUkaCa6fBI98MxvXOXxeEcpQrpjHbqydfY8pMYaYqgJpYpo3fKG_Rt6-1UHbP_g9ZZCrd5j8QHwAbPhpaSOakF8qidtR7FZGPr9eft0q7hj0XO5HB2qT5HUgDR76Ileo2vpvO8grecjMHpwNAQIptKv-HMG2wWE_4EAksGXDAFYWUcliBA4YblnP2vxR0CuyF6U6xuPLQQ1-csZmytcdeGgl8D015CxM_ahrAHtOSGgnGjFD1_4osUcU8ySHW-c9M1rGElvxxxK68kNCTadzB9ElygRza9zPBt2PenXAfRNdSsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
یک قدم تا درآمد
🔹
#چرخ_زندگی یک پویش برای پیدا کردن راه‌های ساده و کم‌هزینه درآمدزایی از خونه است.
🔹
قرارِ هر هفته یک کسب‌وکار خانگی رو از صفر بررسی کنیم؛ از اینکه با چه سرمایه‌ای میشه شروع کرد تا تولید، هزینه‌ها و اولین فروش.
🔹
اینجا قرار نیست فقط ایده بدیم؛…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/680666" target="_blank">📅 20:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680664">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qzmq-KVwj37jA6i3oFqvQUXaWfEW3CzkV8f4xCoNZqXISdS2lkY6JKf6lkn33OAO7VqhYfUpWQUpMNllINwIAnvgE4TCoyFMU9GahpHlfAD6CQ-BC4AUQ-qcGzgMdZeAgbBvtzGHBxHYs556xJIw720yMgkhH7xgS6zY9hORgDpzyUMmThSsxGY5CM-XdrxlH1-SoG1fd4xdQBRugi31HFIbqzJcGoOzwf1hNPhsiLmDDEllaUGdxqTLC0yVSsqsdZDFm6v6_x-93Ae-Y-Nlw3536MZyK1rmTkRJQ4nmeEBVVHTyxWEXYx6_9suHO24GFsjzLTAaMFpdvuDY9dzC9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HPlnTTVpmYLAZHssUU3NhHHxis6JDvdCpfVqavr71OEOLHEgwdPYVkVCNhoXXd5-T4qwYN_4fifNdQvNh4A-879tQOpMFl5FcMigrFmYO_f6jb4u0BhNxl2nNRR8XSd0zXcB_MI5tYwvlxtCUtEcgbCqF2Pthce144iNKX7R5fu_-aNH53nyh846lvCPz-bpvxVOS4waZRrP0SAMPDtFfF9fK6Uxk0mH2vXqxhXXxJzcA8Pq8ypC8Qdsf3f9GLprE3m2Kml4rj5JmaNlXMH0NvE8vbKlMobH7EHRw1mGr42HXMyH-OPOZ9y2NvsxmhV5RupwW5PMSOQbLsgBERf8Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور قالیباف و عراقچی در مراسم خطبه خوانی شهادت امام رضا(ع) در حرم رضوی
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/680664" target="_blank">📅 20:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680663">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
فایننشال تایمز: تحلیل تصاویر ماهواره‌ای، داده‌های منبع باز و فیلم‌های تأیید شده نشان می‌دهد که نیروهای اسرائیلی علی‌رغم آتش‌بس با حزب‌الله، خانه‌ها، جاده‌ها، زمین‌های کشاورزی و جنگل‌ها را به‌طور سیستماتیک تخریب کرده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/680663" target="_blank">📅 20:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680661">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59fa6bf337.mp4?token=vZFXDe45DETILRDbWaTnB0kdqX0UCT53Kww6-pmOr_qMddOW1OoRigckQU7oe-K2MHwJRURLAW82wkXJTEWwC_UxFqU3GpuaexDUuWqPuXdxKzTXHOmJH3EnN2oo9gOtT1PYa_Dxtx2orT9jEE_FiKFfJ9-2XdWGAag1CxN44YmdVzZd0JlV3lz-lMd3SOhnevBmB1cK7G7Za7y-2V59TQv1IedVgzpiY3VFn2IEmuY-xWyzJC6E8i6Vfl4lEuIt_orYElFO73MyNUzz_odtvYhOQSNh3xR5Vr-3AXVLO5cGyDywgff5VBbbNjRY5b5ZfDYOnPlmhifOI7JJX6aZ-LxfCjEmz0dxtQdB8X7GHBDrcdzSrroxLJjENDvg8n4G-hZUatDwzQ38VbDg0q24e9CrITopNWKi9n6NJvMbIEkOb9W0eKeXKHIpXTbtDUxMWlaXYK1ivjMsSdwoT2o-rqYUsvplI0ww02KYSfDhvGNX1Gi5cXcEKuN3nM7iED_K02N0v2GALjrlzlzFNeVa-dUxadj-Ym0ywvNpcMxYLpgME03XyDxp-s10YDCbpG9IlkVyMUnLN2EGcqOXZU0JKou5Fex5mB6Y6bxRAfu91L09D3_CZZ3a67mD4rupY2qldI5fiFG8alCQMfkDQmDYDHSkAdRxGpN8wqJ6G_xyiwI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59fa6bf337.mp4?token=vZFXDe45DETILRDbWaTnB0kdqX0UCT53Kww6-pmOr_qMddOW1OoRigckQU7oe-K2MHwJRURLAW82wkXJTEWwC_UxFqU3GpuaexDUuWqPuXdxKzTXHOmJH3EnN2oo9gOtT1PYa_Dxtx2orT9jEE_FiKFfJ9-2XdWGAag1CxN44YmdVzZd0JlV3lz-lMd3SOhnevBmB1cK7G7Za7y-2V59TQv1IedVgzpiY3VFn2IEmuY-xWyzJC6E8i6Vfl4lEuIt_orYElFO73MyNUzz_odtvYhOQSNh3xR5Vr-3AXVLO5cGyDywgff5VBbbNjRY5b5ZfDYOnPlmhifOI7JJX6aZ-LxfCjEmz0dxtQdB8X7GHBDrcdzSrroxLJjENDvg8n4G-hZUatDwzQ38VbDg0q24e9CrITopNWKi9n6NJvMbIEkOb9W0eKeXKHIpXTbtDUxMWlaXYK1ivjMsSdwoT2o-rqYUsvplI0ww02KYSfDhvGNX1Gi5cXcEKuN3nM7iED_K02N0v2GALjrlzlzFNeVa-dUxadj-Ym0ywvNpcMxYLpgME03XyDxp-s10YDCbpG9IlkVyMUnLN2EGcqOXZU0JKou5Fex5mB6Y6bxRAfu91L09D3_CZZ3a67mD4rupY2qldI5fiFG8alCQMfkDQmDYDHSkAdRxGpN8wqJ6G_xyiwI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✂️
ریش‌تراش/ماشین اصلاح HAIR CLIPPER مدل GYT-999
تیغه استیل ضدزنگ
✅
| شارژی
🔋
| مناسب اصلاح صورت و بدن
🔸
نمایشگر LED (نمایش درصد شارژ)
📊
🔸
شارژ کامل: ۲ ساعت
⏱️
🔸
زمان استفاده: ۳ تا ۴ ساعت
🔥
🔸
شارژ با Type‑C + کابل شارژ
🔌
🔸
صفرزن و خط‌زن برای اصلاح دقیق
✨
🔸
همراه ۴ شانه اصلاح + روغن + برس نظافت
🧴
🧹
🔸
بدنه پلاستیک درجه یک
💪
🎨
ارسال رنگ رندوم می‌باشد.
💰
قیمت قبلی: 1,698,000 تومان
🔴
قیمت 1,398,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/47608/180124/</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/680661" target="_blank">📅 20:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680660">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTLC92rI3Ligwqk5Va0r0MfUufnO0G7y6uFOTkt97CwY8IIHl4SxpYqHGD6oJEz0Ivyt7QfuiyARz-s30KBUmdFBD78x7iN9Lq0W0miZcrGojSCadT1tESkYIIiFkLhmM-3f7EGpnO-bwm7OmQtlZmnPB81W-c2B_8yAJXJNj__13mQbHrCEBzMH9iQ8eBiO5UGbiKNeZ9yuF_M9CYkVt1eztIpHqiJCCFeBvvm51GJVqtKeMj9ChqsBkKDZVlWk3KoW7buQ6aZdUfRP8M3QycHwcb2rqa_Ria8g-KrI92FdK93IUU8dhKpbqpGanW7q3SZdchMi_ocjEuINXrRfVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفت‌وگوی عراقچی با وزیر کشور پاکستان در فرودگاه مشهد
🔹
عباس عراقچی، روز چهارشنبه پس از ورود به مشهد در فرودگاه شهید هاشمی‌نژاد با وزیر کشور پاکستان دیدار و گفت‌وگو کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/680660" target="_blank">📅 19:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680659">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
گزارش رویترز از عملیات «مخفیانه» بارگیری نفت عربستان در بندر ینبع
🔹
خبرگزاری رویترز به نقل از داده‌های شرکت «فورتکسا» گزارش داد که تمامی عملیات بارگیری نفت خام عربستان در بندر «ینبع» طی هفته گذشته به صورت مخفیانه و بدون اعلام رسمی مقصد یا هویت کامل محموله‌ها انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/680659" target="_blank">📅 19:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680657">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ایران را با ماشین‌حساب نمی‌شود فهمید!
🔹
شاید مسئله آمریکا، قدرت ایران نباشد؛ مسئله، اشتباه در فهم ایران باشد.
🔹
سال‌هاست واشنگتن با یک فرمول ساده به جهان نگاه می‌کند؛ فشار را بیشتر کن، هزینه مقاومت را بالا ببر، و سرانجام طرف مقابل را پای میز تسلیم بنشان.
🔹
اما ایران را نمی‌شود فقط با ماشین‌حساب سنجید.
🔹
اینجا، در کنار اقتصاد و منفعت، مفاهیمی زندگی می‌کنند که گاهی از سود و زیان مادی مهم‌ترند؛ عزت، استقلال، حافظه تاریخی و اعتبار ملی.
🔹
برای ایرانی، عقب‌نشینی زیر فشار خارجی همیشه فقط یک تصمیم سیاسی نیست. گاهی می‌تواند زخمی بر غرور جمعی تلقی شود و درست همین‌جاست که محاسبات تغییر می‌کند.
🔹
فشار بیشتر، الزاماً به تسلیم بیشتر منجر نمی‌شود.
🔹
گاهی فشار، چیزی را در جامعه بیدار می‌کند که از جنس عدد و نمودار نیست؛ حس ایستادگی.
🔹
تاریخ این سرزمین کم شاهد روزهایی نبوده که تهدید بیرونی، مردم را با همه اختلاف‌هایشان به یک نقطه نزدیک‌تر کرده باشد.
🔹
وقتی احساس شود موجودیت، استقلال یا عزت کشور هدف قرار گرفته، شکاف‌های داخلی می‌توانند رنگ ببازند و صدای دفاع از وطن بلندتر از صدای اختلاف شنیده شود.
🔹
این همان جایی است که شاید محاسبات واشنگتن به خطا می‌رود.
🔹
آن‌ها ممکن است تصور کنند هر فشار، یک ترک تازه در دیوار ایران ایجاد می‌کند؛ اما گاهی فشار، آجرهای دیوار را به هم نزدیک‌تر می‌کند.
🔹
ایران را نمی‌توان فقط با هزینه‌هایی که می‌پردازد سنجید؛ باید دید برای چه چیزی حاضر است هزینه بدهد.
🔹
شاید قدرت واقعی یک ملت، فقط در توانایی پیروزی نباشد؛ در توانایی تحمل، ایستادگی و حفظ عزت در سخت‌ترین لحظه‌ها باشد.
🔹
و اگر کسی بخواهد ایران را وادار به عقب‌نشینی کند، پیش از هر چیز باید این حقیقت ساده را بفهمد:
🔹
این سرزمین را نمی‌شود با فرمولی که برای دیگران نوشته شده، تحلیل کرد.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/680657" target="_blank">📅 19:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680656">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjDuz_vK7YTLQ0WKSYUFbvZb9Xus5sVYJ36KTzdpKDs3oliOGZNIz7DgK-5HEex7nGHJvClGxDxiDObXjvBeT1xnM25kXxUcMqQE8qN7CdoqW-Hexl7OuSxLkFw9In1SI8uMyMBy7MbIFVRC_5hBJz8C7pcSV_SZ_BXSX1ZryBLom9VQ_UC84n7NMFS5rH0dBnQek6a2sKidjliK3k_3MIYOM1W2j_f6gLQmFI5X748x2efYAjLDhiSWLFiLmdrha-pt4ailNxLlA0aUt5Tm6zwRhpHCizPRQraryNqSXa2_zqY1K33IqtXCK-wSLP0duNRoZcB_q-DTEPTZaQC8tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بارزانی: ایران آماده کمک به عراق است
رئیس اقلیم کردستان عراق:
🔹
مقامات ایرانی در جریان سفر اخیرم به تهران، آمادگی خود را برای کمک به نخست‌وزیر عراق در زمینه «تمرکز سلاح تحتِ کنترل دولت» به من ابراز داشتند.
🔹
مسئولان ایرانی مرتبط با پرونده عراق، تأکید کردند که اگر هدف کمک به یک کشور همسایه باشد، آماده همکاری هستند چرا که ثبات عراق به نفع ایران نیز خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/680656" target="_blank">📅 19:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680655">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce5db6d5d3.mp4?token=v01cDCAOEWGRl4JIaEJB0nI6e-mwS2hohAwuxlGFaz2Zz6lVQnPQRWpebglFTnxq1qW2lUnI1WiLMDj26hpMpnp1X5tKJ-bMtXbve3I57T1MQLYgdsX32ubAvLp2KWQcFHhWtMUmDWY3yGPyC24O3H9ISNKw9_u4w6gPg2xndrT4ic7Kn3lARW5xoZDDxhypYW2inIT40-641tShYRR8Nt6LMKd5fEBPuKwlERZ1Hv7dujo92gKDLAsaCxAMd3VeW0TrY6VMHkHsagXH07WGNlLh56dA9XU3oQxzXMBbSO99JKQYsKI_bzJAwd_6ZA0vsNh25eLamlgDqmGPMHJYUj9qxZtqMFhYEv9iIZ1W8hb2uH7KXGIKM33OxjWdLeP18hI3uxNnsK_2poGC_Mk00RRA-E8Di1dcFN4cDuznXJSP-R9h4Nxe_ocYXX5jXuZ6Ac2xt1Dk8o9G-tfWCwEYZO2YI6iUi4ONV9FYMl-nsB69nPm8bU9C_DPmbVRKDtr8aKPoEG--0R3DiBIPYJTAu4FC1spLtJgArjRy1dXv1btwWmlWiMqvZ9QhiZk-4r1y4MSBKBeaVtNvKebG1CPD-gCXKVqP9n0k69BUoU5Ec3Bz_9SK-lxeAyv3iQFyEjaYgLYoHuKxZMkKNvVNCR7tRL6-vN-kjm9us1XWvh78u4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce5db6d5d3.mp4?token=v01cDCAOEWGRl4JIaEJB0nI6e-mwS2hohAwuxlGFaz2Zz6lVQnPQRWpebglFTnxq1qW2lUnI1WiLMDj26hpMpnp1X5tKJ-bMtXbve3I57T1MQLYgdsX32ubAvLp2KWQcFHhWtMUmDWY3yGPyC24O3H9ISNKw9_u4w6gPg2xndrT4ic7Kn3lARW5xoZDDxhypYW2inIT40-641tShYRR8Nt6LMKd5fEBPuKwlERZ1Hv7dujo92gKDLAsaCxAMd3VeW0TrY6VMHkHsagXH07WGNlLh56dA9XU3oQxzXMBbSO99JKQYsKI_bzJAwd_6ZA0vsNh25eLamlgDqmGPMHJYUj9qxZtqMFhYEv9iIZ1W8hb2uH7KXGIKM33OxjWdLeP18hI3uxNnsK_2poGC_Mk00RRA-E8Di1dcFN4cDuznXJSP-R9h4Nxe_ocYXX5jXuZ6Ac2xt1Dk8o9G-tfWCwEYZO2YI6iUi4ONV9FYMl-nsB69nPm8bU9C_DPmbVRKDtr8aKPoEG--0R3DiBIPYJTAu4FC1spLtJgArjRy1dXv1btwWmlWiMqvZ9QhiZk-4r1y4MSBKBeaVtNvKebG1CPD-gCXKVqP9n0k69BUoU5Ec3Bz_9SK-lxeAyv3iQFyEjaYgLYoHuKxZMkKNvVNCR7tRL6-vN-kjm9us1XWvh78u4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداحافظ پهلوان آواز ایران
🥀
ایرج خواجه امیری ۱۳۱۱ - ۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/680655" target="_blank">📅 19:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680654">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
تاریخ خروج نهایی اشغالگران آمریکایی از عراق قطعی شد
🔹
شورای وزارتی امنیت ملی عراق با صدور بیانیه‌ای رسمی اعلام کرد که مأموریت ائتلاف بین‌المللی در این کشور در تاریخ ۳۰ سپتامبر به پایان می‌رسد و این زمان، ضرب‌الاجلی نهایی و غیرقابل‌تغییر است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/680654" target="_blank">📅 19:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680653">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8852f0078.mp4?token=HCfxrQDueX7EwXbGLmbrV8pZ0zjFvMt3gi6dW_lKI4HjqCqvClax3_ABPnjUjLLsM62irLw_z8cAz_TGz9sFekrvrftKi97ImE2gHZPSR5m3ZkBeF3jZNk_Jt1FBhyU8gG4c7BxqyTWe4gzpxZuJfs61RlaWmBBqL6n2wO6l2QbKmW_QKVJ12w4xbcsG63HTDXp6G7NTh7-u0UN5ezhXQz2c8AqWM3Lcxd1TsJLvWCzvqpRpYMgA4mgVQmk0gvVWqMQfGP1PSnhHK_TCWOwOuLbwLEp80fUANzVWVkRbPX-8x1w8vAjp99fpW4TUSYO1pS_aViFL0fAsxfLCDj0v5Xkuv3yJ8u6x3wMAvqUqeldC5LPZiGwRh5R_82q4ccHAEI75S4SiLAqo68KGsVcP_yEIV-iOgGybjuOuf9HDJJLWNc99u7LUjpVHFXc5fun-952jxUZJqwd37q1lhXSm--dMg1HEwttmaxBkr1znPhv7Zhr9ftJxhh68nr1cUbv9REgc6l6WiZBYP7rnuqjWgmjzr9_RhSJYXsNE6sy6Q_CW7ezOfYnRQT9K6nH4q_HOqV9Elw4y4aKf3_7HBIc9vFt0sJLU9DWhe_SHStHAi8c1FvWOWvJOAZTh7kkHerMH9M6TRjYuvcwtPS8uib48UOA0zcYW7vVJYLREb-maClU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8852f0078.mp4?token=HCfxrQDueX7EwXbGLmbrV8pZ0zjFvMt3gi6dW_lKI4HjqCqvClax3_ABPnjUjLLsM62irLw_z8cAz_TGz9sFekrvrftKi97ImE2gHZPSR5m3ZkBeF3jZNk_Jt1FBhyU8gG4c7BxqyTWe4gzpxZuJfs61RlaWmBBqL6n2wO6l2QbKmW_QKVJ12w4xbcsG63HTDXp6G7NTh7-u0UN5ezhXQz2c8AqWM3Lcxd1TsJLvWCzvqpRpYMgA4mgVQmk0gvVWqMQfGP1PSnhHK_TCWOwOuLbwLEp80fUANzVWVkRbPX-8x1w8vAjp99fpW4TUSYO1pS_aViFL0fAsxfLCDj0v5Xkuv3yJ8u6x3wMAvqUqeldC5LPZiGwRh5R_82q4ccHAEI75S4SiLAqo68KGsVcP_yEIV-iOgGybjuOuf9HDJJLWNc99u7LUjpVHFXc5fun-952jxUZJqwd37q1lhXSm--dMg1HEwttmaxBkr1znPhv7Zhr9ftJxhh68nr1cUbv9REgc6l6WiZBYP7rnuqjWgmjzr9_RhSJYXsNE6sy6Q_CW7ezOfYnRQT9K6nH4q_HOqV9Elw4y4aKf3_7HBIc9vFt0sJLU9DWhe_SHStHAi8c1FvWOWvJOAZTh7kkHerMH9M6TRjYuvcwtPS8uib48UOA0zcYW7vVJYLREb-maClU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
‏
ایرانی ساکن کانادا که شغلش قصابی است از تفاوت ذبح حلال و حرام می‌گوید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/680653" target="_blank">📅 19:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680651">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
تولید جهانی نفت کاهش می‌یابد
آژانس بین‌‌المللی انرژی:
🔹
تولید نفت جهان در سال جاری میلادی بطور متوسط چهار میلیون و ۳۰۰ هزار بشکه کاهش خواهد یافت.
🔹
سطح عرضه همچنان ۶ میلیون و ۳۰۰ هزار بشکه کمتر از مدت مشابه سال گذشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/680651" target="_blank">📅 19:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680650">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
منبع مطلع به العربیه: میانجی پاکستانی در تلاش است آتش‌بس ۶۰ روزه را تمدید کند
🔹
پاکستان تلاش می‌کند با تمدید آتش‌بس ۶۰ روزه، مسیر دیپلماتیک را باز نگه دارد.
🔹
میانجی‌ها برای رسیدگی به پرونده‌ها و مسائل حل‌نشده میان آمریکا و ایران، به زمان بیشتری نیاز دارند.
🔹
میانجی پاکستانی نسبت به تمدید دوره ۶۰ روزه آتش‌بس ابراز خوش‌بینی کرده است./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/680650" target="_blank">📅 19:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680648">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ya1nx465RKe7ARnamdBhngIZXQfhTv0IXPyQ4Wki6C0Zd1sTepgmwgC5T0Yhome1tlXoTuZjxrJcNVeF88pXrPMGEylbmXmIL4zECzO0pNQ0z5JEJciPi1i0StebLfoyzIMHK3J2Y_w053q46W83xYfAZbrkHL4lwln7vynNYKk3bqCKtpAEPb4d3ipin8rci9rD8V6WnAsodN-WqYgxNBxnSyRz0oGx8U2Th19cc27Hc9kFym6CB231s893aPmi-OhyZ4zizOkhAjqxDt_P6LQ5cVS3M-OrdXxbpFZzysjDReycbMNpLy4J6VU_-t2SX4gg70-poT9fn77nrV00oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gi5tduV4RF2tTK3eX2jDGtI8BT99BsPucx1yR_HyrUaBnew_mZ1ctjLFt5VP1G4sHyIbVWo51G8yZXOPF83cJFmRxff0wpFnmCh3aDsWVdgI6ir5p57nyWXLxpdBQozPaG-vkd7wYbI2ouBZ_f2DDKP6NndHYwKP8618am0s0XKnNUeXCJ2fTsjG46OZ9So_0UpoPPr0G6h-KkRA3q4I-0FunHt_IUrztjHKICu9Uht2QlZVu1CV3JUTyFiKeM95t4C8n01yzhW5CnelnWdOVe5kE2TeW7RF1rcWMuN1pgs-KutlH7pj7vxuW0HeuhVBTZPdnYORCfKIQNiOUGpTiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بزرگ‌ترین ناوگان و زیرساخت خودروهای گازسوز جهان
🔹
چین با ۶.۸ میلیون خودرو و ۹۰۰۰ جایگاه CNG در رتبه نخست جهان قرار دارد، اما ایران با ۴.۵ میلیون خودرو و ۸۰۰۰ جایگاه در رتبه دوم ایستاده است.
🔹
نکته قابل توجه سهم خودروهای گازسوز از کل ناوگان کشورهاست؛ ۳۱.۹ درصد از کل خودروهای ایران گازسوز هستند که بالاترین سهم را در میان تمام کشورهای جهان به خود اختصاص داده است.
🔹
کشورهای هند، پاکستان، آرژانتین، برزیل و ایتالیا نیز در رتبه‌های بعدی بزرگ‌ترین دارندگان خودروها و جایگاه‌های سوخت‌گیری CNG قرار دارند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/680648" target="_blank">📅 19:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680647">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSWmH0wdU7pgBfV0ysk711rvpJASTBnYUuYjnBK6l5kl2qQnTr1s2jzWIENyMlEm6uVi7P_Ohk52En-Xppp0gjcfe24Id-2IpgnKkrEOflmqnE9b9yslZD9x_PHAfV2-LhKJJkc6I_TPewwTw34wgwLE98NnDw1ou_g4Gazdn0HQ2J0jq6iBFM9UVb-_UYXBGnLGuU4jQPMTLKCTI4HICoB9Si2ylM8M47kIg8XHt1r51wMtSXwWcfcor1jRRQbXQCd2D6pzn3d4OXwrhZMMeFCFa4erXIj1rjCO_kwfm6JYUJ_whZXOkbJ1nqTmfCf9DqnGCBV2EqDEfwM51puaJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار نقدی: اگر روزی ایران هیچ موشکی نداشته باشد، خطرناک‌تر خواهد شد
مشاور فرمانده کل سپاه در گفتگو با شبکه پی‌بی‌اس‌ آمریکا:
🔹
ایران طی دهه‌ها فشار آمریکا ایستادگی و تمامیت ارضی خود را حفظ کرده است.
🔹
در جنگ اخیر، ضعف ارتش آمریکا را بیشتر از تصور خود دیدیم.
🔹
ملت ایران با مردم آمریکا دشمنی ندارد؛ اختلاف با حاکمیت آمریکاست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/680647" target="_blank">📅 19:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680646">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdNhCa2XNmKRDgnMKBh8SoWcItozHZuo23JrGEEy_rURtbPgpqeI_LbwA7C5G1noo_WnUIaRnvQQ4R1ZhNEPrTy_UbVPrIkbnclTN3hzZqcvje0WeItxhDvtCrh2G03x7ygA7k0yus3YwSwXini_Mo6uJrC4YAydS6TSg7SKombeqhFCFB6FEUlx9wMweqcEvTXfmsb_uFKPG5FcIG5Dn9aXdHXOIvL8lSqYiI4RbLXqyxJCULsUollk2oKQ7V1ZSljS0y61o9vZDlIR6QsfZhumz3SKc-nXXA-KBVd5c4mJ-LgbRfog6-cmsGjf1tryf9JXWsEtLyZk2TbvxFFxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فایننشال تایمز: «جی‌دی ونس» معاون رئیس‌جمهوری آمریکا، شخصاً از کی‌یف خواسته است حملات به زیرساخت‌های مرتبط با کنسرسیوم خط لوله خزر را متوقف کند
🔹
کی‌یف با درخواست دولت ترامپ موافقت کرد، زیرا در تلاش بود از آمریکا مجوز تولید موشک‌های رهگیر پاتریوت را دریافت کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/680646" target="_blank">📅 19:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680645">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mp8q9_sXgHKON83iuFVB7hxzQKDGVZC19W38ohC5h2A8bIlYm7NC8GUruE-6aVPoMEp3bUoHrjjevgCYB2dI-wwPV76QqvlC-2yuqgwYUYvN1BH5N74StEJUWIwZ2ERnca7KlbvcF3o9Sh1smgHPJfu2MkF4SzfHLXZTEQHcGxLsdJe9J3kC3E55Rn21LDJlK-TmYq7dvKAN9Uj-4RuLFc1WG5aF3UOPhrqJzVk4cd_tILPykmlnr-B_42JEyY4w_dt_FlLFqPhxv9pVz9PHoviD45TMgKN6ftkbdFnmOoPuL39otDIIHDlUANg55Vy8qJkEPpdOd817XVup88149A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
این روزها اسم آمپول‌های لاغری ( مثل مونجارو ) زیاد به گوشمون می‌خوره؛ اما این روش درمانی برای همه مناسب نیست و میتونه عوارض خطرناکی داشته باشه !
پرسشنامه زیر
توسط جمعی از پزشکان متخصص غدد و تغذیه تهیه شده تا شما با پاسخ به چند
سؤال کوتاه در کمتر از یک دقیقه متوجه بشین آیا تزریق آمپول لاغری برای شما توصیه می‌شه یا نه.
🟢
شروع ارزیابی</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/680645" target="_blank">📅 19:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680644">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
روسیه یک کشتی و نفتکش مرتبط با اوکراین را در بندر اودسا هدف گرفت.
🔹
حکومت طالبان اعلام کرد طی پنج سال گذشته حدود ۸ میلیون مهاجر به افغانستان بازگشته‌اند.
🔹
انصارالله: فقط مراکز نظامی سعودی را هدف قرار می‌دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/680644" target="_blank">📅 18:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680643">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f98dea1296.mp4?token=Syc05uMZK80xSeYKWFSIOTfH8rIDpUd4CrMKj1__o87HOXwxPOnCRb3JsvZYvxHQaAfbbQdbs7Zprpj5Xa0_NwAHsViaWy7DenFHB4hnrRw3BQt7rLDqkDzK4zd-gdMXnTTHh0I4hs5P-N6SP7wZFlZYy0eELELTAyLU9uneFdXaM_cudCHf__z-RptesiqMf7BmCqd9oS-34-u59O1Bdhz8ua892iphTA39t9RJDMAvw0zh38Yd36YaroVGTqvxb9MTWyxP3RLJwXYJ8cv79F2t-ktPB5cdTcl3w-2ktriNN1WM1lH-uyoddvE7H4GvOHftNLR62LUXKsLJ9ntcVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f98dea1296.mp4?token=Syc05uMZK80xSeYKWFSIOTfH8rIDpUd4CrMKj1__o87HOXwxPOnCRb3JsvZYvxHQaAfbbQdbs7Zprpj5Xa0_NwAHsViaWy7DenFHB4hnrRw3BQt7rLDqkDzK4zd-gdMXnTTHh0I4hs5P-N6SP7wZFlZYy0eELELTAyLU9uneFdXaM_cudCHf__z-RptesiqMf7BmCqd9oS-34-u59O1Bdhz8ua892iphTA39t9RJDMAvw0zh38Yd36YaroVGTqvxb9MTWyxP3RLJwXYJ8cv79F2t-ktPB5cdTcl3w-2ktriNN1WM1lH-uyoddvE7H4GvOHftNLR62LUXKsLJ9ntcVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدای ماندگار موسیقی ایران خاموش شد/ ایرج درگذشت
🔹
حسین خواجه‌امیری، خواننده نامدار موسیقی ایرانی که با نام هنری ایرج شناخته می‌شد، امروز چهارشنبه ۲۱ مرداد ماه در سن ۹۴ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/680643" target="_blank">📅 18:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680642">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
توهمات ترامپ ادامه دارد   رئیس‌جمهور آمریکا:
🔹
ایران نیروی دریایی یا هوایی ندارد، سربازان باقی‌مانده‌اش حقوق نمی‌گیرند و نیروهای سپاه پاسداران نابود شده‌اند. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/680642" target="_blank">📅 18:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680641">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxXHtS-cJBGLwkJxZtRyCBohSnpP8wZMpSuCna1-h6X7p2OI-Wplo3YMEQbGCoRpewq2D5mxrlZ065nMbqUh6M64_gYN9ZhbA6hBPhLTfj7xgYlLwcgrdUFumEtjOaot40nTRKchArXh5aV-o-dioLNUi9Qqd2BTw3JJc-_zDof1l9i3R2xuocDEGGRiLt21VMUmHI-Z1LFTrDt6Ng94_GaycLQYc3IjY8WGmI54e-mwzbNHrUArwpDrsMAz-9DuxIAMTEREVxM9pYNkJpJPA6_Xh6I18s5ONmG0G0-dFp-ZA7HlGXSkufF5bB6GgLzZAl-NCCODsh6KAJ_beapPlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب حجت‌الاسلام ‌والمسلمین حسین طائب به سِمت رئیس سازمان بسیج مستضعفین سپاه پاسداران
💬
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده‌ی معظّم کل قوا در حکمی حجت‌الاسلام ‌والمسلمین حسین طائب را به سِمت…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/680641" target="_blank">📅 18:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680640">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8bhXz52j-e-_Uy8L3vcOdu41pKwGQWe8mO6jykrPqpqmi13_3xObQ7xMXHAheuPVM3s9W5gU6UnAyonJMoCZW3D9IgZiX_osKqB3ybqR-5tPYKoSoz5uCOZVHltsbF_MDDA58kkscjvi4ITEkVMeYckxsj5Y-OoJoAD3LQb9fb3Jrmr0Jxa2EkGZSTNAOxCC6Q88t_H0e5UrJ5Zw1ITYLgpcZkz9MGdyqArofYrOM2Y_R9DJl42hlFdnjI3RlE1ocMZy_aLm-39YRvVjvbaFC5Qqhpz1-lduooZh7tk5Dwa8bczlKfHzSlRjguw_APQ_BWJZfjHURs5pD8v8KOzyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت کاربر خارجی: مردی که ادعا می‌شد در تونلی پنهان شده ، در دفتر کارش به شهادت رسید، در حالی که کسی که به ناوهای جنگی و جنگنده‌‌هایش می‌بالید، با کامیون حمل اشغال مواد غذایی از ترکیه گریخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/680640" target="_blank">📅 18:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680639">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yn75YOUcrvorS-O2ogc36zT82J2iis1fknDy1jnKzun26_myv-b27V4Mr0rOrzNt4lGGw7RKCe3dEH9D7NzDYNDX6Lr2Bj-YJ3bOdPTdYDDCULzw0o1f7QQhdZ0Q6n5cXz6pWVm9MH6gILP106ORnNjmVSv85EotHVDNVuCFeZ2Xk0sR72sPFgwuyz-qcAkGdkhE84zeshgcbCQ_8zFF0Q_JRe8Gl0U6kFTf__P-2qg96WQmKOUFuVGjmWq8dWXcwJgsE_4DSDX8hnmo4hhmp7fnt8IumEb3P_Or4_6o2SihmSebtPVtJDjarsUqDpbf6NNW_1eepNUjhcz7WLEfQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت‌پرده مهلت سه هفته‌ای پنتاگون به شرکت‌ها برای ساخت سلاح/ آمریکا برای جنگ با ایران باید کدام سلاح‌های خود را احیاء کند؟
🔹
بر اساس سند محرمانه‌ ای که به امضای معاون وزیر دفاع آمریکا رسیده، به شرکت‌ ها اعلام شده که «چرخه‌ های بازگشت چندساله‌» برای جبران خسارت‌ های جنگی قابل‌قبول نیست. اگرچه سخنگوی پنتاگون مستقیماً این اقدام را به جنگ با ایران مرتبط ندانسته، اما کارشناسان نظامی اجماع نظر دارند که این فراخوان اضطراری، پاسخی آشکار به تهدید جدی موجودی تسلیحات آمریکا پس از چند ماه درگیری مستقیم با ایران است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3236935</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/680639" target="_blank">📅 18:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680638">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">صدای ماندگار موسیقی ایران خاموش شد/ ایرج درگذشت
🔹
حسین خواجه‌امیری، خواننده نامدار موسیقی ایرانی که با نام هنری ایرج شناخته می‌شد، امروز چهارشنبه ۲۱ مرداد ماه در سن ۹۴ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/680638" target="_blank">📅 18:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680637">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYRhSDth7CYRfieuGl87jqO_oGlxE_iSXAnFcxcjN3cZ218P_wYmW60CmkJf43b3hy0GD6IRC768mCa5CTivM6A8DNMa7uNiBCM3NWSGyQXDkFRrJlpCE-NTvZEJtuktGc0NgEau1VnGFdjb69-GOwIPxYi8VthNhrrUgai696LiA_nZ4GoK43SK68WFA_c-BarDoaR_52tEzZuZY6IFeR8UCzMaFNFPhnibqmtwQT2XN-2B5JaakwxF585nGkL-u91AgtMk-k0orUS0LEuzoS2iBhhGmucFPWP0zHBJvBq5aCJAp2EuTxfthxhOirG9aNbCVnlkWA3ALvnrBNrsJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ متوهم در ادامه خیال‌پردازی خود درباره ایران: ایران هیچ کاری از دستش برنمی‌آید در برابر محاصره دریایی ما، و همه آن را «دیوار فولادی» توصیف می‌کنند #Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/680637" target="_blank">📅 18:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680636">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/377783ba7b.mp4?token=J1LVqeA-EqhmV9hP5KiN-NDD4T-Yxs0gAZMfLxkmgk768K1N_VIjGhdhlOUicSdRIjXdpwvSxx2NHo_pqdIG7npGbVksfnvSWPskLjezJHxO-3YQoYXk4TOUrwhQ55Tx9Sua6id4nV-bqgxjW-IKznoBAfp84ejDklR1nlXpCNGiwJ7rKJWNK1wvrcdbyGZ2XIJzb_87p4M9SxjJbgUlQCI4TzKLZ-AsYM93qhuuCMFM4PmSuaMaHh-D1bzjVCfdpA3PhXw_e2rWu-pPAq5UyAbghMM3EK96crKUUoOYqrK2j6xydtn6kqsW37otGgXq971-TbgGAQtNbnIWajdQTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/377783ba7b.mp4?token=J1LVqeA-EqhmV9hP5KiN-NDD4T-Yxs0gAZMfLxkmgk768K1N_VIjGhdhlOUicSdRIjXdpwvSxx2NHo_pqdIG7npGbVksfnvSWPskLjezJHxO-3YQoYXk4TOUrwhQ55Tx9Sua6id4nV-bqgxjW-IKznoBAfp84ejDklR1nlXpCNGiwJ7rKJWNK1wvrcdbyGZ2XIJzb_87p4M9SxjJbgUlQCI4TzKLZ-AsYM93qhuuCMFM4PmSuaMaHh-D1bzjVCfdpA3PhXw_e2rWu-pPAq5UyAbghMM3EK96crKUUoOYqrK2j6xydtn6kqsW37otGgXq971-TbgGAQtNbnIWajdQTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوگل از پیکسل ۱۱ رونمایی کرد
🔹
پیکسل ۱۱ با نمایشگر ۶.۳ اینچی Actua، تراشه Tensor G6، رم ۱۲ گیگابایتی و حافظه پایه ۲۵۶ گیگابایتی معرفی شد.
🔹
این گوشی به دوربین‌های ۴۸، ۱۳ و ۱۰.۸ مگاپیکسلی، شارژ بی‌سیم ۲۵ واتی Qi2.2 و اندروید ۱۷ مجهز است و قیمت آن از ۸۹۹ دلار آغاز می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/680636" target="_blank">📅 18:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680635">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: واشنگتن کنترل کامل تنگه هرمز را در اختیار دارد و قصد دارد این وضعیت را حفظ کند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/680635" target="_blank">📅 18:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680634">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: واشنگتن کنترل کامل تنگه هرمز را در اختیار دارد و قصد دارد این وضعیت را حفظ کند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/680634" target="_blank">📅 18:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680633">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
طلای دوضرب دختر وزنه‌بردار ایران در تاشکند
🔹
هستی صدیقی در دسته ۶۹ کیلوگرم جوانان آسیا با ثبت رکورد ۱۲۶ کیلوگرم در دوضرب به مدال طلا رسید.
🔹
هانیه شریفی نیز با مهار ۹۱ کیلوگرم در یک‌ضرب، در جایگاه هفتم قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/680633" target="_blank">📅 17:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680632">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSqHnw_BbAiwAIXBsAxpKWyD05lJsZeuV6fjXJsypg9SdQfCx1K7Ms3NNsqch_CtjSx09gLoaJu-Jp70wN10-XQnvDGTpk4i5aRnaJxCmtKUeK8BIG1kpz1n5OSntStFn70KmpG1ZSjWhXe_gZSkVE_2d0fjz5UFODETD5VG_O2v_ZS05R-BR9CMRlXsy8W_tugCVqjhv7MPYsazgKC4dJAOf-D9hX1Z72qUi0sqqNprgsP8Y9236yKwAZWBrlV-EIOam8iu0NPGoS7g5Bx16ozV7SiU17ytCKYbTo6nTGS8IWvoWqLnZITeDmX7gq2SkyzYMtaiBwELzdKMTDNB-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/680632" target="_blank">📅 17:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680631">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/897df1ea58.mp4?token=h4dJPWS5714wSHJycbhEUst-SWshIUfGiKGp1uSvHhVGtwvTA2XX361TwqmWzHTB2VCvosLzvz3gvRPk6kiS3zd0xGrT2jbouHncx_rB2mzayqVTxvRrHnOg4Vuw-5slu95w_l6GpWZcWeCFlcRZtzMcCgBTYWtT4XOTJbuRsEmSL-mI8dtebBCfoIzWa0jVRTNuvD0BaEmm01h1uWAHngZk-8R1tHIEqKFzIlDwqGqhRRuOfJeVMaIRW4mei6gb2_j9eFbu0iD285rRtdY9oZDBXWEl3IcHO43ul66T8x3kIWFIv5FzYJlQwtE9dQjRxnTinWY2v1-CMJ2sNRKFvjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/897df1ea58.mp4?token=h4dJPWS5714wSHJycbhEUst-SWshIUfGiKGp1uSvHhVGtwvTA2XX361TwqmWzHTB2VCvosLzvz3gvRPk6kiS3zd0xGrT2jbouHncx_rB2mzayqVTxvRrHnOg4Vuw-5slu95w_l6GpWZcWeCFlcRZtzMcCgBTYWtT4XOTJbuRsEmSL-mI8dtebBCfoIzWa0jVRTNuvD0BaEmm01h1uWAHngZk-8R1tHIEqKFzIlDwqGqhRRuOfJeVMaIRW4mei6gb2_j9eFbu0iD285rRtdY9oZDBXWEl3IcHO43ul66T8x3kIWFIv5FzYJlQwtE9dQjRxnTinWY2v1-CMJ2sNRKFvjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥀
پیر و جوان، کوچک و بزرگ؛ همه زائرند…
◾️
حال و هوای موکب هیئت قرار در مسیر پیاده‌رویی زائران امام رضا(ع) به سمت مشهد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/680631" target="_blank">📅 17:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680630">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
تولید نفت ایران افزایش یافت
اوپک:
🔹
تولید نفت ایران در ژوئیه، به میزان ۲۶ هزار بشکه در روز افزایش یافت و به ۲.۴۷۸ میلیون بشکه در روز رسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/680630" target="_blank">📅 17:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680629">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
آینده مبهم سفارت‌های آمریکا در منطقه
سی‌ان‌ان:
🔹
واشنگتن از سفارت‌های آمریکا در خاورمیانه خواسته برای فعالیت با کارکنان کمتر برنامه‌ریزی کنند؛ اقدامی که به گفته دیپلمات‌های سابق می‌تواند توان آمریکا برای پیشبرد اولویت‌هایش در منطقه را کاهش دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/680629" target="_blank">📅 17:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680628">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f13359cdd.mp4?token=s_2VesNMjTWJ59TktRrUbVMxI42A7sl8JfPVaqNLMEsVAc5eURzltL8248hM5VpikYev0hurKa7H-V8oMEosbZ4hx1TDw-CNt0I4MLJPuVpvSZeli72c-PW6hrgZyj-IyetKfICRdkgREvB6sFrvKqwxxKbbfsw_3IAgLA41CTZj06-joI1cDIy9RxdoFLlPxRbMRAA53H8pHzXw5OYj_YKa3N3DTs0nUdAisMerexxv8sGo4cWNXkpwbaptrxwPKUFF0UGcJdMHssuvXfRWHS-2Lklgik1E-Kk99TigcIDHovMN7EA3RQohcamRNHkMbsM1U5Kz8v84u99UqIh0Slgg_pIP1BOAkl4jcQeAkxYRI64UEW0qSWI1K7r50xlmlroTeHaCpw26m_hdQxS8AI5XOLBcJLgWXCPiH0Rkhzthhmyt6nt6O0aHhW7jy4SCFDrEuim3QMFEOKAkzM6NhWdDhISLsAfpmSHQJwE-iUv7A8dfH7LTfczrCB0RbDy3rY6yeuTYAfLZ44vLwZsmnSUarvVkc6rIDFJrds8IXs58Dlbxodr9pktca3Ymk3wjmwH0rqaormJdlnpMEt-EXWbontJfu6HcgDX3U14UJ6oHZqfu7jlhMDzdbWyPLypYcl62Yduk3HCfjH4V8JBem5G4-TzzgmBwaYf0mVrI9dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f13359cdd.mp4?token=s_2VesNMjTWJ59TktRrUbVMxI42A7sl8JfPVaqNLMEsVAc5eURzltL8248hM5VpikYev0hurKa7H-V8oMEosbZ4hx1TDw-CNt0I4MLJPuVpvSZeli72c-PW6hrgZyj-IyetKfICRdkgREvB6sFrvKqwxxKbbfsw_3IAgLA41CTZj06-joI1cDIy9RxdoFLlPxRbMRAA53H8pHzXw5OYj_YKa3N3DTs0nUdAisMerexxv8sGo4cWNXkpwbaptrxwPKUFF0UGcJdMHssuvXfRWHS-2Lklgik1E-Kk99TigcIDHovMN7EA3RQohcamRNHkMbsM1U5Kz8v84u99UqIh0Slgg_pIP1BOAkl4jcQeAkxYRI64UEW0qSWI1K7r50xlmlroTeHaCpw26m_hdQxS8AI5XOLBcJLgWXCPiH0Rkhzthhmyt6nt6O0aHhW7jy4SCFDrEuim3QMFEOKAkzM6NhWdDhISLsAfpmSHQJwE-iUv7A8dfH7LTfczrCB0RbDy3rY6yeuTYAfLZ44vLwZsmnSUarvVkc6rIDFJrds8IXs58Dlbxodr9pktca3Ymk3wjmwH0rqaormJdlnpMEt-EXWbontJfu6HcgDX3U14UJ6oHZqfu7jlhMDzdbWyPLypYcl62Yduk3HCfjH4V8JBem5G4-TzzgmBwaYf0mVrI9dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقش‌های شهاب حسینی در گذر زمان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/680628" target="_blank">📅 17:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680627">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
جزئیات آتش‌سوزی در مجتمع خلیج فارس قشم
🔹
آتش‌سوزی در یک فروشگاه تشک به‌دلیل وجود مواد سریع‌الاشتعال، پیش از اعلام حادثه گسترش زیادی پیدا کرده بود.
🔹
۱۲ نفر به‌دلیل تنگی نفس از محل خارج شدند و حریق به‌طور کامل مهار شد.
🔹
بررسی کارشناسی برای علت حادثه ادامه دارد و شواهد اولیه، رعایت نشدن برخی الزامات ایمنی را در وقوع و گسترش آتش مؤثر می‌داند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/680627" target="_blank">📅 17:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680626">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfSESJC9SA1-nwZwlr7NZTU0KGpw2p_E5OYimB5xeEhgCTdk8ndqjWC4eBh2Ybez04J20qZcnvvwnSpYtUXvpXtmLPKNej2XSeruZ04pHRyi_X5pPeMPttBgkhUxfZD6G4sNFnutFh6Ns2bj9XhMFO_jD6vDOtFcV4emQdWh2fC0X6XZrWKfuvhdcqfXhterfQLCeP6ywmI7afBEpDQAvvE3M9p5l75ZDLrNwIvdGEyGoKnGQ0EkBJrbMZnKHKyN0ZdI09b3XoZMl_HAuI7APg0Hol4mANfaXeHSIGG5tjgX_X9QD24Kq2R0vRgaEyQyrT4ikV_V-LPwKlTqDv57fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک قدم تا درآمد
🔹
#چرخ_زندگی
یک پویش برای پیدا کردن راه‌های ساده و کم‌هزینه درآمدزایی از خونه است.
🔹
قرارِ هر هفته یک کسب‌وکار خانگی رو از صفر بررسی کنیم؛ از اینکه با چه سرمایه‌ای میشه شروع کرد تا تولید، هزینه‌ها و اولین فروش.
🔹
اینجا قرار نیست فقط ایده بدیم؛ می‌خوایم ببینیم با امکاناتی که همین الان داریم، از کجا میشه شروع کرد.
#چرخ_زندگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/680626" target="_blank">📅 17:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680625">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coa9qhyWPYT4UVt64AfVQEnUfAd5As2Y3uDzAs1TP25GtTUPOYdXQvrLk-ZL__mcshULkjq_pd3jhQJz4iRoFkazoAENjdkNcCeypG2F-rjLmEsGcnG5r7LEgkmprQmf8tb76M1a39zj5cz_j_AIQ18vWTVtltQOIak7W5gwhmRGaqXmjQ7j1fm8ylrGUD4BF8unxaxrj3gT9wCLXwGpf7fu3h2Ufwzb2xtVRjbP-SFCjyYzujdWmRKEOqWJqkvKG9rxyKGsU4Hp_jfmZa74_iF6ZVXrgWF1vbLFjCbznNc17I8gnWMLqo1ZBxN8cyNNUi7gz3_OJpHsNAlxTEJE0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«خورخه مسی»، پدر لیونل مسی درگذشت
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/680625" target="_blank">📅 17:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680624">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
کویت مدعی خنثی‌سازی طرح تروریستی علیه تأسیسات حیاتی شد  وزارت کشور کویت:
🔹
دستگاه امنیت این کشور توانسته است یک طرح تروریستی برای هدف قرار دادن یکی از «تأسیسات حیاتی» را خنثی کند.
🔹
بر اساس این ادعا، فرد بازداشت‌شده آموزش‌هایی در زمینه ساخت مواد منفجره و…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/680624" target="_blank">📅 17:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680623">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
کویت مدعی خنثی‌سازی طرح تروریستی علیه تأسیسات حیاتی شد
وزارت کشور کویت:
🔹
دستگاه امنیت این کشور توانسته است یک طرح تروریستی برای هدف قرار دادن یکی از «تأسیسات حیاتی» را خنثی کند.
🔹
بر اساس این ادعا، فرد بازداشت‌شده آموزش‌هایی در زمینه ساخت مواد منفجره و پهپادها برای اجرای این طرح دریافت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/680623" target="_blank">📅 17:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680617">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iyuxoCOse6v6qSrsjIJdHpTJzTg00UYYU5gSm4uwAbc1v2SADixzjKHlRNtgkZx6M2Ave2l93YDJ3LhBQ1CmY5fLWxxRpRS2sRKHvnijSk5c98yhzKN_kaf_Q-0SmJzj0IAzNV3hREk_bPPzmg3u3up4MeMai1o3b_GsEKkjUUnYNaLyFFq4ZXDjdnFiuTFwj8P0wcsk9_s8nHM3_ORPkOovXLsAgX2Rz10233W0iCkj5nUCI-zKvUxKvk-wbMsw4y4iWbd6QGwUUhTabrfAU5vPxAvElIovphvT2_1TUZZBj6G26bh2mWhHFMkFgkq_c6BhKR0SJmXbwOAJQN-NUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvbT4hkhpjQWswOXJ3LB9yVNbeaOuoSWa9Ft8iURatIgMf7LsNebOl1V93VONrSpNog37rjbponCEUfeDuwpuFO7DDTaWXHKjpKVrcZE9NTc_t_w4Odb55K63k9ZxzVLHGrU73vBmstnn9-mSS8UXSqZAm1cLjxoi20zrJKWWOCRF7zg6pkiyuajMrI3KlACgAr4e6AoscYYsElwG0O4nkSWSaU-zb1X82xzu1jVTPN_o_p53c8OY5dZVGJ7qo4A0mQalKv1b0rUBjjPhGLXr32X7efkCYGKLgBCvYO4xlxu9f-6XZmrNjiMR4UK22nia7qKP7COR0YfsFegN_JKHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gyFk_jGY6uv5WLYSFn8z-G3hD63l5T-PH_Xh9gFIlsK5rZZv0HMR9RCdsNO5xayX9flJZrf3zKyBqKkqW91aJp1OuD57I8rVHIpALp6qqfeS3kDOXLrP6ndG9Ufrt3SsNsRqdIxoiYa4xTWCNH2eyEZzYyFYBsq7Np8ZBT1et-peU49rgfrazMOncOf6_oxYRC4qQ4Mn5FIDY4XtNgAuWIc-nL8Kxed8hX3kled76B4voyRQMEGySOTGW0f9NVhXzHCzh2gvAgbbVXgfn8z2ojR5AVUJdOVhywevp5jqR4fEIHASlv5WqypAU2U7jRkRspDBWiCLXHzUJNaN7SGmUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OI82z7qOye6GZw75YoyQmFiIZSbTbOXgLVRd4rEWJmSIhOkfJY7_Y-WWB3RIQkxAT7ZzY_jZQ6Zbrx1rFmpIttf1LnyDqAY7i60hCM3JbP10yuqGqDcYVnelrvPRQax1Nq8JQHOo-BqaLiVFu9WEFz0vwAvYQAvOUtASz0AJMNqrBApls_rLgy8Xzwp0TJsz8xw4SP6wLOXL2iGxm7NuunsBZWAP3fK5p2_ay3_HsNgs2qQ01exN-45rc2oDWwPtd2W8l9reimHHbqlGdK7ceyqyXsbBNd6l4_K5sQLJaaPoXdWyGA_ej7BGU5T3N1_A2CDuEv-7ELfQJMyOJpskJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4AniMJh88UNv7G4rWX4kUZCJTyLvtlES6dWMIs2ZybogK3eNX2V_n8ZWGJ1kB_4jo0EAz3VTZrQwVxjysQcVVgELbJqzmpuTX6mVKpKLkAeM3YiI2UVGMfyoVkG335W1LG1MCqSizxIbSxlhhe7r3cS3E8u_bQFawe56Q52719C4ckZFyX_8VCXJrUcxNnEOAWB8JIgq56k2vXq9yZKXEU0yBC4oHAa8D7I0Jvzf6CRZmXRve8OgGkNRUdlOx2TLbI69ZC4O5qxaFZMzSb0u32oPIcq33qCjVY5D8FVWoaPTk59PZX9BdjB2U02LmvriSzJ_YYpAgB27hhd7qlNgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cHhLJgA66L8reFhx3Dq9UB_uQXrxRq_sWNXaMMuUmHQgQKLvKJ-8QCld-x9j-iWAPRuswKs3KvVGiUFlr1zxs7fBqNslCzcpVQhZpnexcNGpYDhu-y4chvw2wEfDcpTmcOTv6ObuxtN81nIhhiGZFq3Q1N9BHi_Mn-J0ys2QW_ubWYwbPc_9R7Y7vRPcLP7lKxRmg0hMrT3lBuLtXcOx_ZdhJuUQ6jcPiN4SPlrO4guSs8JQpt35YyeznLSLZxJfRWhNDIH4obMFZOEaxmRAvk009wbGtzVEJm8FJ8-I2XN3E6fmmnjScfXb4Je7vI2hz8cG8ypjezd1uGHmSjpVeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حال و هوای حرم امیر مومنین(ع) در نجف اشرف در سالروز رحلت پیامبر اعظم(ص) و شهادت امام حسن مجتبی(ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/680617" target="_blank">📅 16:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680616">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
تمسخر فرار ترامپ با ماشین حمل آشغال غذا توسط جیمی فلن
🔹
فلن با کنایه این فرار ترامپ را به عنوان «طرح خروج ترامپ از جنگ با ایران» معرفی کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/680616" target="_blank">📅 16:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680615">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1faddfb66.mp4?token=FAmqYKlknD9wl74_YHiTUWT9p4mnUS2mNsVUBTTDLcYpd-FUvtmhyzJ-zuvAU9_6ZsVBBeUdN58ruc9l_ctTFV8n90Q-zVJUSnl2Gl_FWm5U2aZ701dybTezmi-bSYsCfi8WuYSHrCFT2Lgk4wJKMj3QZuRu1Gl-Yeaykmv-lkHhZkT72PXTnTcVy0yqEHCVWgOMqMcUhhoQttsgMQ6mxexw3Rted5FDnP12JsM4nS2qysiJXjJOCsAKR6RDPsB4c16rE8c8Vz7mzlrA8kiPYlco3jCbw-vBGq0Jk5SPsQZN_rDFdyVogYboc6zMOUhHaT8uXrFxU7RKfBkOOEwdUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1faddfb66.mp4?token=FAmqYKlknD9wl74_YHiTUWT9p4mnUS2mNsVUBTTDLcYpd-FUvtmhyzJ-zuvAU9_6ZsVBBeUdN58ruc9l_ctTFV8n90Q-zVJUSnl2Gl_FWm5U2aZ701dybTezmi-bSYsCfi8WuYSHrCFT2Lgk4wJKMj3QZuRu1Gl-Yeaykmv-lkHhZkT72PXTnTcVy0yqEHCVWgOMqMcUhhoQttsgMQ6mxexw3Rted5FDnP12JsM4nS2qysiJXjJOCsAKR6RDPsB4c16rE8c8Vz7mzlrA8kiPYlco3jCbw-vBGq0Jk5SPsQZN_rDFdyVogYboc6zMOUhHaT8uXrFxU7RKfBkOOEwdUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی مرگبار کشتی مسافربری نزدیک جزیره بالی در اندونزی
🔹
یک کشتی مسافربری امروز در آب‌های نزدیک جزیره بالی اندونزی دچار آتش‌سوزی شد که در پی آن یک زن ۱۹ ساله جان باخت و ۱۷۲ نفر نجات یافتند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/680615" target="_blank">📅 16:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680609">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70b1c63e05.mp4?token=KKpiRvdbExxzPjOKVCQAkGvcf-xGgHpO5O0-UwS5mTuZAdEoOvPxILwkcHZP_TWaA2bwR7NX7sCatH7A_nBCh0x3mS1TVxJfguspJBv_Q1BN9NQmaKxmC13wkRFKfpon4oZH7Cvg0Wz2biVFVUFmRP72mvijMS6H0vWq1CVbfieFKHAXllSXpANmgVCTGtrRQ11grQ9hhpjm2bjtwaM8V9hiCFdDLQQUuIStMt4IcUDuueptkWqJ3LWIo684yLRMdeApInoczc1PDQ-K305X1LA54k-hSNasYesR0WgUh7uzdsvU7iTDFi45q5ef8RoP-hu_XD25JrMkrSZfdxHh7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70b1c63e05.mp4?token=KKpiRvdbExxzPjOKVCQAkGvcf-xGgHpO5O0-UwS5mTuZAdEoOvPxILwkcHZP_TWaA2bwR7NX7sCatH7A_nBCh0x3mS1TVxJfguspJBv_Q1BN9NQmaKxmC13wkRFKfpon4oZH7Cvg0Wz2biVFVUFmRP72mvijMS6H0vWq1CVbfieFKHAXllSXpANmgVCTGtrRQ11grQ9hhpjm2bjtwaM8V9hiCFdDLQQUuIStMt4IcUDuueptkWqJ3LWIo684yLRMdeApInoczc1PDQ-K305X1LA54k-hSNasYesR0WgUh7uzdsvU7iTDFi45q5ef8RoP-hu_XD25JrMkrSZfdxHh7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
کلیپ های شهادت پیامبر اکرم (ص) و شهادت امام حسن مجتبی (ع)
🥀
در حرم رو به پنجره فولاد
گفته ام بارها حسین حسین
اربعین در طریق کرببلا
گفته ام بارها امام رضا
@Heyate_gharar</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/680609" target="_blank">📅 16:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680608">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
زمان دربی پایتخت مشخص شد
🔹
بر اساس اعلام امیرحسین روشنک مسئول کمیته مسابقات سازمان لیگ، داربی پایتخت از هفته پنجم لیگ برتر فوتبال ایران، ۱۱ و یا ۱۲ شهریور برگزار خواهد شد. البته هنوز ورزشگاه میزبان داربی مشخص نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/680608" target="_blank">📅 16:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680607">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca137496a5.mp4?token=Vsb7Khi-fyL1rJytlP9A49A0T7TlgmtKSzI3-Owa40kRAB2ahxiwn9RnNlZEpdTHdHYsr4nX7AS-wNn9VnNoZ-oMl1jNkeaonxLOKwfL9PQ1uN-42SYOQa73wWhm2XiPWOSwz8uU9VFsMx9XdYZEbwyY7DsBOc1PGj2akW58WsrCB04jZfTVSAxZEXl3-JjN9T4vIgUf0nm1qcizvU_AejSO9P2qPY287YKiEK9XzHseFJZRcl-yWC0kqXjqlAYue7gYFLjU8_gfKyyz9n7trwJRjNWNeTK9ukTIJ1nXZf0rggKl8YC3eh4WPju-tdx9eTwxytFnOcgrFFsNQgiIvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca137496a5.mp4?token=Vsb7Khi-fyL1rJytlP9A49A0T7TlgmtKSzI3-Owa40kRAB2ahxiwn9RnNlZEpdTHdHYsr4nX7AS-wNn9VnNoZ-oMl1jNkeaonxLOKwfL9PQ1uN-42SYOQa73wWhm2XiPWOSwz8uU9VFsMx9XdYZEbwyY7DsBOc1PGj2akW58WsrCB04jZfTVSAxZEXl3-JjN9T4vIgUf0nm1qcizvU_AejSO9P2qPY287YKiEK9XzHseFJZRcl-yWC0kqXjqlAYue7gYFLjU8_gfKyyz9n7trwJRjNWNeTK9ukTIJ1nXZf0rggKl8YC3eh4WPju-tdx9eTwxytFnOcgrFFsNQgiIvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط جنگنده F-۱۶ نیروی هوایی ترکیه
🔹
این سانحه در جریان یک پرواز آموزشی در استان یالووا در شمال‌غرب این کشور رخ داد.
🔹
طبق گزارش‌ها، خلبان این جنگنده جان سالم به در برده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/680607" target="_blank">📅 16:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680606">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKrAlLnWrcI9YUq2EWVo4GdYdvFtwQP0vKanbIuYVVcrAviM7jK6s3AxBPA62pD1NZQxKXX15RxZBZjiY1fEvRv4bl5sVt_Co4r7VS5IsUmrVu0s2neVjXk1D49-CVektDSyi-j5rPS2sZ0AJYqf77ubAKO_cOMiD3O0mpSXK6dp90_zU11kPqrczSqJsB1n6oICfS8cI7PVH7WkBvFNPig5F9LfXe3sSbHJbFEM3h5T9aqzQGTBXpG8aB4haow4JUb_QsyDkYCtRenGBzo7x5Ynm3eVhoBOsWA9S5cqc7bU1gbWFCf0RscPxj8WY7QyunqlVMiTnReY10Lpl-JyvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: ایران و پاکستان عقبه راهبردی یکدیگر هستند
محسن رضایی در دیدار با وزیر کشور پاکستان:
🔹
ما دولت، ارتش و ملت پاکستان را از سرمایه‌های بزرگ جهان اسلام می‌دانیم و خرسندیم که در تحولات منطقه‌ای، بیش از گذشته شاهد مشارکت و تحرکات نخست‌وزیر و فرمانده ارتش پاکستان هستیم.
🔹
ایران، پاکستان، ترکیه، عربستان، مصر و اندونزی، به‌عنوان کشورهای بزرگ جهان اسلام، وظیفه دارند در مسیر تحقق وحدت جهان اسلام گام بردارند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/680606" target="_blank">📅 16:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680605">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">صدای ماندگار موسیقی ایران خاموش شد/ ایرج درگذشت
🔹
حسین خواجه‌امیری، خواننده نامدار موسیقی ایرانی که با نام هنری ایرج شناخته می‌شد، امروز چهارشنبه ۲۱ مرداد ماه در سن ۹۴ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/680605" target="_blank">📅 16:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680604">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjedzcZ5lAyGVM17upUA5xbfMVNqlg8iqRY6JClHBZWe_UXadnWfwHlIlOscQRrGvRBAkupgrTEPmY4GQwt22hXxI0vRcDSZcXl9L8ubBnn1V-cttnvkHBa7g2FZ96vJve9CBR_hInYn0CmOlNDOmz0IDtvXkl8NjQY01H87COEFlVsyN3DMWnsMs7sHNFsvrzGH5iNi_A0wFb11r_o1NOXAjVbwlyEyEkeTwz-cEG_gtajRuuf39xMNGoHkpFiJsHmw1ES0QGI9fZnNZoWFx96n09EhUhI3N6uZhfoSIHZuorN1-bSixOgi5EajXcwjaANRtMg1G4F0qi8jtGVWyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چنگیز وثوقی، بازیگر و برادر بهروز وثوقی در بیمارستان بستری شده است  فرح‌بخش کارگردان سینما:
🔹
بیش از یک هفته است که چنگیز وثوقی به دلیل بیماری‌های قلبی و کمی عفونت و همچنین مشکلات ناشی از کهولت سن در بیمارستان است و مشغول مداوا است./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/680604" target="_blank">📅 16:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680603">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
دادستان اردبیل: افرادی که در انظار عمومی وضع پوشیدن لباس و آرایش‌شان خلاف شرع و یا موجب هتک عفت عمومی یا موجب ترویج فساد باشد، شناسایی خواهند شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/680603" target="_blank">📅 16:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680601">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFMjP6IILqWo2gsczM2tT72r1IKY7p2ZhRALm8wCmeo82PRkJTH0NNdJKWT3GgYqTplN7QzTasIFQuxD8KqllmopIXuOmoal_6cGCtgfyZz3-Fmm1KLaESZT40Vukeu4FBsOEmbhZiJluTDw6nMZGg8IbALSW_ZBkOYzoHJa1m_QS3Btpo0W7bLi_goZxqvAWPRVcfE7ilm1fHKjPfh_0Wwy1hzSzAb6TH1dzsxmrM54yhByxw9jf8nojf6uoH7WD8pQa-FLqsC32yJ5AW93SFSdGUHjsmdVACpOjIcdnZDRLTAqDPan15Fr5GCj3X_DOKM38heHRl0eT_OVxlGqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af6ed03846.mp4?token=QgwxU3y65Xii8BRmnOmZ3uwh_xBK-AUchnEzJx-2g2KqT8HXI0t2QVsqC81TN_zQTHaOz9eBxQ6wnkY2K40AchcH6aagNePYhfEboCmSKVS6xetq-RGdYjYhdhWmOVOLo2wAenPj_VWIR5VlcGkp4YPLEhm2CRheBR3glKa3dj1w8_Lu1FCW8KWRZy1DvvRE6mvUEWvndI6pRe5499YWLlC3O295H0psTwkSvdBHIxR0l18543vnGKnlXjniDSagntk6sOwH3pv9uOqmapC5Xnt-4awUu54kJAnVXJtroC-zdzXRIW7_YqAK-u_2w_VpKpz3hRIFXaJgWztYKg6lmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af6ed03846.mp4?token=QgwxU3y65Xii8BRmnOmZ3uwh_xBK-AUchnEzJx-2g2KqT8HXI0t2QVsqC81TN_zQTHaOz9eBxQ6wnkY2K40AchcH6aagNePYhfEboCmSKVS6xetq-RGdYjYhdhWmOVOLo2wAenPj_VWIR5VlcGkp4YPLEhm2CRheBR3glKa3dj1w8_Lu1FCW8KWRZy1DvvRE6mvUEWvndI6pRe5499YWLlC3O295H0psTwkSvdBHIxR0l18543vnGKnlXjniDSagntk6sOwH3pv9uOqmapC5Xnt-4awUu54kJAnVXJtroC-zdzXRIW7_YqAK-u_2w_VpKpz3hRIFXaJgWztYKg6lmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مبارزه عجیب سنگاپور با تب دنگی با کمک هوش مصنوعی
🔹
سنگاپور برای مقابله با تب دنگی، هر هفته بیش از ۱۰ میلیون پشه نر حامل باکتری Wolbachia را در شهر رها می‌کند. این پشه‌ها با ماده‌های وحشی جفت‌گیری می‌کنند، اما تخم‌های حاصل به پشه تبدیل نمی‌شوند و نسل پشه‌ها کاهش می‌یابد.
🔹
در این طرح، دوربین‌های مجهز به هوش مصنوعی میلیون‌ها پشه را اسکن و نرها را از ماده‌ها جدا می‌کنند. پشه‌های ماده‌ای که احتمالاً از سیستم عبور کنند نیز با دوز کم اشعه ایکس عقیم می‌شوند.
🔹
در نهایت پشه‌های نر با خودروهای مخصوص در مناطق مختلف رها می‌شوند تا با نرهای وحشی برای جفت‌گیری رقابت کنند؛ روشی که با هدف کاهش جمعیت پشه‌های ناقل بیماری به کار گرفته شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/680601" target="_blank">📅 16:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680600">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ef213bb96.mp4?token=VFlfEo757WwJbuAYe2yKsGtxY0pk2fqZCGMnhcUTqD93aF9tzNHUK3Y5_Ff6PZtTCwaaoeHn5XTCVvygombq4j-yVIBnRdu93zpyywmWhxcEss4-8mLZ7geTDVzBfX93heV9_MOB7tYzMcBJCqiOcNcZLWK8EsYPmU3v0_YScV1X4vmMlBKNeLHzH0HMLBFqkuPT3gyo_WGgupNcUN-cNdotsBQcig8B4DPZkZlC7z_WH1xNC7-gdfkfTxmpidTReh0vV1pPVrSO0Pnw6huEVjpMlc9F9nwOB2P0gDhaGwH79m_jlWJRuSGSshs0acWJWIduJ9I4vdgCWMNxXTKilg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ef213bb96.mp4?token=VFlfEo757WwJbuAYe2yKsGtxY0pk2fqZCGMnhcUTqD93aF9tzNHUK3Y5_Ff6PZtTCwaaoeHn5XTCVvygombq4j-yVIBnRdu93zpyywmWhxcEss4-8mLZ7geTDVzBfX93heV9_MOB7tYzMcBJCqiOcNcZLWK8EsYPmU3v0_YScV1X4vmMlBKNeLHzH0HMLBFqkuPT3gyo_WGgupNcUN-cNdotsBQcig8B4DPZkZlC7z_WH1xNC7-gdfkfTxmpidTReh0vV1pPVrSO0Pnw6huEVjpMlc9F9nwOB2P0gDhaGwH79m_jlWJRuSGSshs0acWJWIduJ9I4vdgCWMNxXTKilg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🛑
مغازه‌دارا و فروشنده‌های پوشاک، مشتریات منتظرن...
✨
مدل‌های ترند و پرفروش
💰
قیمت عمده واقعی
🚛
ارسال سریع به سراسر کشور
📦
خرید مستقیم و بدون واسطه
اگه دنبال سود بیشتر و جنس پرفروش هستی،
همین الان وارد کانال شو و لیست مدل هارو ببین
👇
🔥
تولید و پخش نیکلین (منگو سابق)
https://t.me/nikleinn
https://t.me/nikleinn
https://t.me/nikleinn
https://t.me/nikleinn</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/680600" target="_blank">📅 16:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680599">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgUSL3WhHCvli6PiGURQBMrvQZu8IzRBEI4DM1lGRnmaobA_P60mWiDqfi5pOcuh_7WH4AeYP_HWruCaXdFKKmQ6srElj9v_kZVAh71E197FIWhUpplL8MOQQwhJsBsD9Yoc1tLC9uFrgLpBU2wDAn9xdk3V_1ywp9ewOV9iar7yeRTNsW7SLtrkNfvMeOib7ibM0Bylc4NI6i4ZFwOkxJn5gafazOLV7n2xyXqEXvlhhOE11wIJT5c9bx_h3t_NVp5Uf9SDfZkDz3NLQPTalVEIRcjIDiolXkm4IFzOWoM4YVAtejOdgA0lbwHg1F3id6_MPVacqs3UWxgdIRUSDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای ماندگار موسیقی ایران خاموش شد/ ایرج درگذشت
🔹
حسین خواجه‌امیری، خواننده نامدار موسیقی ایرانی که با نام هنری ایرج شناخته می‌شد، امروز چهارشنبه ۲۱ مرداد ماه در سن ۹۴ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/680599" target="_blank">📅 16:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680598">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
یک هیات امنیتی بلندپایه عراقی فردا برای گفت‌وگو در مورد تعدادی از مسائل امنیتی به عربستان سعودی سفر خواهد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/680598" target="_blank">📅 16:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680597">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lez96oPAAQ-xZQPJUewFoDMaI7Hz2n8hePyO9ToUuLikFN9cA7LA6t1QIMgg35LPngLt8IkwGxxEVqciihVFCX_PNcgnEWwHLJP79PJSwZMsNX96AGPP8pcvrFiCh7nptj3lGx9urv_gBJm6WBLE9l-gbhVhduPb3qRZoRJoEXSM225PudZlD8B_zHL8fBdMISkoh60vkWlIyyujpwL-3BHh-h00ay2lbuVx3pd6UsnnrCHfskOeyjilBw1RC_llmaqW69ZsrlcP9qkpEwc37nbXb5w1VHR6HozNrrMTxKIYJdXpRbEo1_upfM4nmU5UyGmAzee1iKAdIsz3yF50bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین اقتصادهای جهان بر پایه سهم از تولید ناخالص داخلی
🔸
مقایسه آمار سال‌های ۱۹۹۵ و ۲۰۲۶ نشان می‌دهد ایالات متحده همچنان با سهم حدود ۲۵ درصدی، رتبه اول اقتصاد جهان را حفظ کرده است.
🔸
بزرگ‌ترین جهش متعلق به چین است که سهم خود را از ۲.۳۶ درصد در سال ۱۹۹۵ به ۱۶.۵ درصد در ۲۰۲۶ رسانده و به رتبه دوم صعود کرده است.
🔸
در مقابل، کشورهایی مثل ژاپن و آلمان با افت سهم در اقتصاد جهانی مواجه شده‌اند و هند نیز توانسته خود را به جمع ۶ اقتصاد برتر جهان برساند.
@amarfact</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/680597" target="_blank">📅 16:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680596">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrLaVF4xUneRzj1UTQex83qK32q4_c_RO7DQYkGc60Yqmg6rsCHNcpK5HZmWT6f5DnXkG6PGSG2ZYtyp13uq7VCPrL6RJFCyi44_EJR54-5nQsBKjqO9Rbac6fpSn-NxUalJkm75BUmTlqw0E3i_SRKe7HLUaj9Y5aB_IkwgzN3VuAMGTCu7qzO2HG0ROCmXw5SoThWj5kVYsOZbbBZuM4XiX_FJ8PvZOdYGGXAzJa8rZi61tRIXPZq0YBmNDuX46mE3Cgn3rCYw_yJEU9Ec7xJp6yZzcPd1XVbSKl6cB2E_Wrlo-csPhGVTWGBJNY8u5D9oCEKstHXpdfGSGrj8LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمسخر فرار ترامپ با ماشین حمل آشغال غذا توسط جیمی فلن
🔹
فلن با کنایه این فرار ترامپ را به عنوان «طرح خروج ترامپ از جنگ با ایران» معرفی کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/680596" target="_blank">📅 15:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680595">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
آماده‌باش سفارتخانه‌های آمریکا در خاورمیانه از ترس درگیری علیه ایران
🔹
شبکه خبری «سی‌ان‌ان» گزارش داد که وزارت امور خارجه آمریکا با صدور دستوری فوری، از تمامی سفارتخانه‌های خود در خاورمیانه خواسته است برنامه‌هایی را برای فعالیت با حداقل پرسنل (کادر محدود) تدوین کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/680595" target="_blank">📅 15:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680594">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tby6oJhuEpQKJaGNWT_e1SCDKchXV8YNyT35yNxAUOLR0-gXcuvOn1hqVsXAGTMaNLCFXOoaQbwowjPfmuoIIMn3ePKCjRkYj71TgkK1zjIMYLRJoHQ45HakS0uq2gmEVK_66dbAB3QqKp5AkUVpght-p2loJs6I35qszTpE-aBK_pRWA_P4tUwyljAnzUVzpyTX31ol_AjZuyS_f13oUEveR_SXdgbLiRJWT5cj2HH6hw5f3ZKcKYwodUwCtVaUgDSOSebd9wUeoziNmkDomJ7KZzlfOUyNxxDOpjIImqnKHD-mH2B3VlIjdapnl7XYWHX64hiuUOqbqfJI0nNvSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مک‌گرگور مشاور ارشد سابق وزیر دفاع آمریکا و پنتاگون: ترامپ بر هنر شکست مسلط شده است
🔹
این بحران در پاییز ضربه بسیار سختی به ما خواهد زد... ۴۰ درصد گوگرد جهان از تنگه هرمز خارج می‌شود و در حال حاضر هیچ‌کدام از آن خارج نمی‌شود.
🔹
او باید بنشیند و کتابی با عنوان هنر شکست بنویسد، چون در همین کار مهارت پیدا کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/680594" target="_blank">📅 15:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680593">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad6950c610.mp4?token=YaFniB05CV7LQFuIybsAH66DDWcGIhmztujk6FtzBRgEL3h_yzVAwQA9G3cg7aXnqaOZLbie70b91cCJmstXM1qun0e9C90p5xkrgwgsbYzXoYnvsMICP_xqq8lATkv5KzzLSTXAK89rzih4EdfFU2WlgY_mgVsG-0kJ0d8F5LWMZ_9LwS3vWIDwJ4UgdmdJhugmfJ1zEnkmcrJe2onT_kKSJno-OGOWpZ4wuOuFM2LP4ReyT1eNNhZ2RS7MwR_537iuyX964nkrU4h6AUZ2QNjnmCkC0D-ZzQv23gBP89tYS6tFfC4JEaJ4zdi_kzQqVF8_TY-lN6oWcNdAGgLEWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad6950c610.mp4?token=YaFniB05CV7LQFuIybsAH66DDWcGIhmztujk6FtzBRgEL3h_yzVAwQA9G3cg7aXnqaOZLbie70b91cCJmstXM1qun0e9C90p5xkrgwgsbYzXoYnvsMICP_xqq8lATkv5KzzLSTXAK89rzih4EdfFU2WlgY_mgVsG-0kJ0d8F5LWMZ_9LwS3vWIDwJ4UgdmdJhugmfJ1zEnkmcrJe2onT_kKSJno-OGOWpZ4wuOuFM2LP4ReyT1eNNhZ2RS7MwR_537iuyX964nkrU4h6AUZ2QNjnmCkC0D-ZzQv23gBP89tYS6tFfC4JEaJ4zdi_kzQqVF8_TY-lN6oWcNdAGgLEWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شرور قمه‌کش تهرانی دستگیر شد
🔹
شروری که با قمه‌کشی، ضرب‌وشتم شهروندان و عربده‌کشی در خیابان‌های تهران اقدام به ایجاد رعب و وحشت می‌کرد و تصاویر اقداماتش را در فضای مجازی منتشر می‌کرد، دستگیر شده و در اختیار مرجع قضایی قرار گرفت.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/680593" target="_blank">📅 15:49 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
