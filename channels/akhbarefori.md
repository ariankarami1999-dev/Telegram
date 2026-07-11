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
<img src="https://cdn4.telesco.pe/file/QpmZhgW3Oo61YG57OTGI19WIx3K8XlK3z1QpG-rhYy2ndHUDgbGgVVlzQeqpZOu5C_RRKsEvkrVCand1HpKUyKydVHFK-xPZDEYail3zpYBMKFj76lYopZsNWmF3-y1g0LvWwt4luOBY0aO98KDqit3zpcumvntSXYy0YeALRAq_nW4hNPgxGBx5iVRz08cMTu4DsioFoMKF5hxH_LVyOD8VoQneQzB31ChGjd843hySFuVLX0fCOx3z24US8QXKjX8isnCVuy6Rt8bDpi0DoBz6YO-h4obbIalDXloRrL8HWEEEIaiWu34ylSp4OEDPC_yN13-4JYq_scK_wQRSjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.44M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 10:37:55</div>
<hr>

<div class="tg-post" id="msg-669670">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28d4e2e16f.mp4?token=hHPjtANzIED6p0dLiiBpBM2O6Bb00j590XWzi9iWD5WX48hgcU9TyrbMycYyMQB5VP83zqyw4fgYpiJs-3dAm5m8PYo4iOie6q7lhHGD12q_2oyy-kzx24Am3DaDrJyENP-cR7VyW3TSx6QlJCmAvfYSrXvMyCfH4Q3ohN28_r-0fsoIf4Cs65YiZPWYDKMP9VAosIJedhTTKjZmfDQ3JvTyPG2Vn5QuorMUpWthv-aZNkc3w4wXJmRUVoWR7iXrgAuTdQ2Zxv4wIkbOpCBOeVWFgD0QpDHk4jEgI-CXequizjJpJguFC3zyXyd2uhYfCgLUbLbQVKpk0DBIDUUBkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28d4e2e16f.mp4?token=hHPjtANzIED6p0dLiiBpBM2O6Bb00j590XWzi9iWD5WX48hgcU9TyrbMycYyMQB5VP83zqyw4fgYpiJs-3dAm5m8PYo4iOie6q7lhHGD12q_2oyy-kzx24Am3DaDrJyENP-cR7VyW3TSx6QlJCmAvfYSrXvMyCfH4Q3ohN28_r-0fsoIf4Cs65YiZPWYDKMP9VAosIJedhTTKjZmfDQ3JvTyPG2Vn5QuorMUpWthv-aZNkc3w4wXJmRUVoWR7iXrgAuTdQ2Zxv4wIkbOpCBOeVWFgD0QpDHk4jEgI-CXequizjJpJguFC3zyXyd2uhYfCgLUbLbQVKpk0DBIDUUBkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دریاچه یخ زده در قله سبلان
#اخبار_اردبیل
در فضای مجازی
👇
@akhbarardebill</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/akhbarefori/669670" target="_blank">📅 10:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669669">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPBpmFk2CBZvNm6TDd7V4CWYtF6sb-9AUhz-Cxgb9fzXD6d8YVmbuiFKAc0ZkuAH9DKBTEOIogJcU-QrIKXekGriJB0S0b4ZgeG3V-VvAUimfhvrJWuCmBNFqs7HNakERF94q99HRW4bnOjMG7hZKtIi7-YJjUFE4ueETU3PS3zTIu_zeVabx_3uWg_TQBPvzQp2lOGVhHGdzhYUAoxp9ylKKlDpAhBIvWawooh_o-k9AopAsWgGmWObRRQPxtAV_77RS1Kimvqb6nxgLkK_mqGc348D3TvMTeFYn52GwDZ4J0mOxZugRxfGx33LpYT91F4Avun61bdkxnQafYzvkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوگواره بدرقه یار
▪️
از تمامی هنرمندان، عکاسان، اصحاب رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود تا با ارسال آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور در سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» شرکت نمایند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگو تایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبر فوری ارسال کنند.
▪️
به برگزیدگان هر بخش، جوایز ارزنده‌ و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق آیدی
@Badraghe_yar
در تمام پیام‌رسان‌ها ارسال کنید
برای کسب اطلاعات بیشتر به کانال رسمی سوگواره در تمامی پیام رسان‌ها مراجعه کنید
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/669669" target="_blank">📅 10:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669667">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">#باید_برخاست
♦️
ثبت رکورد ۹.۵ میلیون سفر رایگان در مشهد | بار سنگین جابه‌جایی عزاداران «آقای شهید ایران » روی دوش اتوبوسرانی
🔹
محمدرضا قلندر شریف، شهردار مشهدمقدس، از اجرای گسترده‌ترین طرح خدمت‌رسانی ناوگان حمل‌ونقل عمومی در تاریخ این کلان‌شهر همزمان با مراسم تشییع و تدفین پیکر مطهر رهبر شهید امت خبر داد.
🔹
وی با اعلام این خبر افزود: در جریان این عملیات بزرگ، ۹ میلیون و ۵۰۰ هزار سفر رایگان طی چهار روز به ثبت رسید.
🔹
شهردار مشهدمقدس با تشریح اقدامات سازمان اتوبوسرانی در ایام برگزاری مراسم تشییع و تدفین «قائد شهید امت» اظهار کرد: سازمان اتوبوسرانی مشهد با به‌کارگیری تمام توان فنی و اجرایی خود، نقشی محوری در جابه‌جایی خیل عظیم عزاداران ایفا کرد.
🔹
قلندر شریف با اشاره به حجم بی‌سابقه خدمت‌رسانی گفت: در این عملیات که یکی از گسترده‌ترین طرح‌های تاریخ اتوبوسرانی مشهد محسوب می‌شود، ۲ هزار و ۱۵۰ دستگاه اتوبوس به‌صورت شبانه‌روزی در بازه زمانی ۱۶ تا ۲۰ تیرماه، وظیفه جابه‌جایی زائران و مجاوران را بر عهده داشتند و خدمات‌رسانی در این ایام به طور کامل رایگان ارائه شد.
🔹
وی افزود: ناوگان اتوبوسرانی مشهد با ثبت ۶۵ ساعت خدمت‌رسانی بی‌وقفه، موفق شد رکورد بیش از ۹ میلیون و ۵۰۰ هزار سفر را تنها در چهار روز به ثبت برساند که نشان‌دهنده عمق برنامه‌ریزی و آمادگی عملیاتی این سازمان است.
🔹
شهردار مشهدمقدس، اهم اقدامات انجام شده را این‌گونه برشمرد: راه‌اندازی خطوط ویژه در محدوده حرم مطهر رضوی و خدمت‌رسانی فعال از ۱۲ پارک‌سوار و ۹ پارکینگ برون‌شهری، حمایت ویژه از خط یک قطار شهری با اختصاص ۱۵۰ دستگاه اتوبوس برای تخلیه سریع ایستگاه‌ها از مهم‌ترین فعالیت‌ها بود.
🔹
وی افزود: تدارکات فنی و سوختی با تأمین و مدیریت بیش از یک میلیون و ۳۰۰ هزار لیتر سوخت مازاد برای پایداری ناوگان و آماده‌باش کامل بخش‌های فنی جهت رفع عیوب احتمالی در کوتاه‌ترین زمان، به خوبی انجام شد.
🔹
همچنین به گفته وی، پایش مستمر از طریق سامانه‌های هوشمند نظارتی و اجرای گسترده برنامه فضاآرایی ناوگان جهت اطلاع‌رسانی مطلوب به زائران صورت گرفت.
🔹
وی با اشاره مشکل پیش آمده برای راه آهن باتوجه شیطنت دشمن جنایتکار، در اوج خدمت رسانی به شرکت کنندگان مراسم تشییع با اعزام ۵۱ دستگاه اتوبوس به ایستگاه راه آهن ابومسلم در نزدیکی ملک آباد برای انتقال مسافرین قطار به مشهد وارد عمل شد و موجب رضایتمندی این زائران عزیز را هم فراهم کرد.
🔹
قلندر شریف در پایان با قدردانی از تلاش‌های جهادی معاون عمران ،حمل ونقل شهرداری ومدیرعامل سازمان اتوبوسرانی وتمامی پرسنل و رانندگان خدوم وپرتلاش ناوگان  اتوبوسرانی مشهدمقدس، خاطرنشان کرد: هدف اصلی ما فراهم‌سازی بستری ایمن و روان برای حضور میلیون‌ها عزادار عاشق در این رویداد عظیم معنوی بود که به لطف الهی و هماهنگی تمامی بخش‌های شهرداری، این میزبانی با بالاترین کیفیت و بدون اختلال به انجام رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/669667" target="_blank">📅 10:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669666">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
گزارش ماینرهای غیرمجاز چقدر پاداش دارد؟
🔹
هم‌زمان با تشدید برخورد با استخراج غیرمجاز رمزارز، شهروندان می‌توانند مراکز دارای ماینرهای غیرمجاز را گزارش کنند و با توجه به تعداد دستگاه‌های شناسایی‌ شده، تا سه میلیون تومان به ازای هر دستگاه مشمول پاداش می‌شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/akhbarefori/669666" target="_blank">📅 10:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669663">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GLhmRg47uODxIwxTms2qPlrqwZqNnmuJyvjeWmD1scUnQVjC8ws_X2kQSUrlEAvhI0IpwvpugR6IYrRhaXXZ7ENpkKZDq8x_5YO1K0GhuM-w-6L4t8ixllPexTe5uKDg-RHeGGoJTNWBqRQC1rffyE-sqFXQLIexE0pHVF48EVUk4OjyieMXIbGywdabs_xSXfB-02LstlUxWHmkU0PVD515P68Eil0KFsog6gMprBGBOs4fUXR0Ut0a200KzlBboQ8PEb12OZ1fk6ObfAxSP0DtBmrOOIRSLBLUGIMNRDWiEDusgXxoe_wncyuo2FQReTpSGIv6ffdliIDJAcrDLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BVIdcvZ-QEUwEb_AxwlN-7XQqP267wED7mrcQWVx2TPuZyoYVLbVEgCGxWZkwOtvoCRLIHSElA6AexBOFROWBP0SOxIHg6sf2x11YMj4hAyro6u_4AVwPHyUTirbnIbq2GjSDJ7R393pq2TsyoWsd3UTdemjdrgKpfd1KB6s_7y6rs-cExMp6n2J9nZTrF3hcDu42ya8757K5eMi2eNMrpXyxCRkgSvSG8crqpkIMAwT_bZrrq5CilbeF90alB8sNqs7PPmaxLUhTRb3lNSWBoD4NB__ZDfyfPDT7vOPuCOlyTRWJoJziZQkbxIn6pwzxVGUDbTHlmghB481wfgNng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HpODiRUFXgMU54b-rVzgFBag9sFOQbfYW4squFNvMWMOgTP5lP1mzuO1ZTF_jwrvBaanX_8vxI8w8djeWuwBYr0lrkj73EjfyQXA-03Md-T9_vVmYpXl-wcVv40uvTX8GdzAnKXmev88APa8ls-C8rjQxEb3oGiEa4G4v4TH33Op22rd_CdnCchJ9hkL1I1rM1m-e_dE4K5_qLTuHJRAg7C2S8NQ0_4Uh6Yr6XFEVYEWCJAQBj5Pu5jILE6Q9lxX5sEELOuNyrJnpiCXj7eDIMLJ9OCoJdj9pgvi9i6bRSyHWlngIViadbYw-w0ODcLni7NbgIQksOeZOb488cyh0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
یک‌بار برای همیشه؛ تفاوت اعتماد به‌نفس و عزت‌نفس چیه؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/akhbarefori/669663" target="_blank">📅 10:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669662">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d6d0b0d32.mp4?token=IJEJDhWX1G8u7S-GZH7pN3UJRbX_qb30RrJil1VVsjsALXnFkJz1sfia6ohlXOxbj01ZyVrxg576Uul525UBtdavRAY7vZe42ahHgzMBx8XE7XymHX6AF7riC8e0kjB7GhUHA45OSkLRi9lhJP0z9gI3xNBbnvOgBrdt8S4uLS1yy4d5PpK8bJ1XKFsjaUSh4PyAEslv2qIB6c7cUcJBHo6ceWUbzRUPyK40-1SKtKPlODzrkoooPyA7G1OoY0Ve379CZ9fEeZn-nBXvm0HlwzyqA1kLBCfY7BZHMtYE72uicoKasif7VP342kPIIFi4-_8NjQc12myKjyEVKfXrew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d6d0b0d32.mp4?token=IJEJDhWX1G8u7S-GZH7pN3UJRbX_qb30RrJil1VVsjsALXnFkJz1sfia6ohlXOxbj01ZyVrxg576Uul525UBtdavRAY7vZe42ahHgzMBx8XE7XymHX6AF7riC8e0kjB7GhUHA45OSkLRi9lhJP0z9gI3xNBbnvOgBrdt8S4uLS1yy4d5PpK8bJ1XKFsjaUSh4PyAEslv2qIB6c7cUcJBHo6ceWUbzRUPyK40-1SKtKPlODzrkoooPyA7G1OoY0Ve379CZ9fEeZn-nBXvm0HlwzyqA1kLBCfY7BZHMtYE72uicoKasif7VP342kPIIFi4-_8NjQc12myKjyEVKfXrew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رنج کودکان فلسطینی برای رسیدن به آب
🔹
در نوار غزه که بیش از ۸۰ درصد زیرساخت‌های آب و فاضلاب آن تخریب شده، کودکان نقشی تعیین‌کننده در تأمین آب آشامیدنی خانواده‌های خود پیدا کرده‌اند.
🔹
آنها ساعتها در صف‌های طولانی منتظر می‌مانند و گاهی با خطرات جانی مانند حملات هوایی  مواجه می‌شوند. این در حالی است که ۷۰ درصد خانواده‌ها حتی به حداقل آب در روز دسترسی ندارند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/669662" target="_blank">📅 10:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669661">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
بررسی اروپا برای دادن عوارض در هرمز
روزنامه گاردین:
🔹
اروپا در حال بررسی پیشنهادهایی است که ممکن است اجازه دریافت عوارض و هزینه‌های ناوبری در تنگه هرمز را بدهد. البته اروپا در صورتی مایل به پرداخت عوارض است که این عوارض اجباری نباشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/669661" target="_blank">📅 10:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669660">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yg45yChodfzx6nUeIbKLoxg1ZU1dVh-Z92uw0tUtpiWTrGIke2TOv87vJOYSnS-YQcUk8EWi8rMXqatKx8HOB6johDUTFc2R3iFG6zWST0pQWTqm2uvrpD6o2RsMDPvKWGsQgoAl0cyC10WmkD-DL4_xmf_XPBE3qk39BRiB2nA4RhYco_Y7ai7SCbBsvhqQ0afMAmJf6ylIWUosfwY7Lj34LHz0HBuvycwRtLkQtp99XR9YJKr5-HDrDQXEmncagZf4hb3YSDDB7apCbPzYyQ70TkxQcKfnn52UxrjF9GxFYwE7oNp8o8JJFKe354WPgbPxI-hxyUnq0e7OqWJ0aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام رزمندگان پای لانچر به مردم: خدا را شکر که جای خالی ما را در تشییع امام شهید پر کردید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/669660" target="_blank">📅 10:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669659">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZMUcGJ04FxLu5QohDnvW_0_9Khk2Z6AwXaUs4nv4QEoI6dpJ7enxKQjGXSP4DxApTMSfqsZKN6cR4pubEFzYOr9ZOVVi1EjR-RZUI5OBz_9sv7UBpQhddni2B2eksdHtsNzLZip8DVEjiS2VVU_sUG_Yxm5OWc8W5gPfueol2LL8JGSKz51_4CXqaoJk1x7QVUS_bQKMvyDryDGVhd0rCSgHWMUvG-Hsf3I6UxBxExWjqKKLiuepkpUep5cz_Y-rNBz2mrqq9HNuGPH7JNU2tuRysoHzg7H05gGI0YJ6pVkzFbQn9U2oitgx4o6NhCO3Ny4_jvcv_hua1SGV9uamQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترفندهای طلایی برای از بین بردن انواع لکه؛ این راهنما را ذخیره کنید
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/669659" target="_blank">📅 10:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669658">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZZkLtbTBNibpBkxz_kavbSSwa8R2aHHO0NV0jUKFPR_TylEGFd0d8KyHPwd5A0pE9Tz2fgALL2Uu5_ifuafnHgoaYFM0NGTs6RRWJv4kehcKGHs0kA_TB-sHC_RDone2kDkaoE1l1c0wTDOg9qSXamJ05-F1rD-jr-yBGbOM09wvoifFD3D_PolkEMM2cWlVd17N8NopqGcPfA8rR8v3bndh8CZUz9Q-wnBcfuzoGbwkMaxVEAoMQUejx35OR4xwYGR4Q3-w1LrkUEQlwRyuLOXXkFh72sHdrqDlXgqJGb2eu9I4BnhJLQh7hvLSRLLT8ExqSC2uNZgF1UIWcdoGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏨
اقامت لوکس در هتل ۵
⭐
سی نور مشهد با تخفیف ویژه
✨
فقط برای مدت محدود:
✅
تا ۴۰٪ تخفیف واقعی روی انواع اتاق‌ها
✅
اقامت ۳ شب، شب چهارم رایگان
✅
صبحانه، های‌فود و فولبرد
✅
ترانسفر رایگان از منزل در تهران (شرایط ویژه)
✅
استقبال فرودگاهی و راه‌آهن
✅
سرویس رایگان رفت‌وبرگشت به حرم مطهر
✅
شارژ اختصاصی خودروهای برقی
🎁
ظرفیت اتاق‌ها محدود است و رزرو با این قیمت تا تکمیل ظرفیت انجام می‌شود.
📞
همین حالا تماس بگیرید و قیمت ویژه را استعلام کنید:
☎️
مشهد: 05132021021
☎️
تهران: 02144673863</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/669658" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669657">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
خبرگزاری دانشجو این ویدیو را از پاکدشت منتشر کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/669657" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669656">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc4f495813.mp4?token=te4CebcTf2GWtOKo7kOx851kG1EIjFaPP_VuM0iX-5n4GvaEOYiuYLhCzih9LexkxulslfbA5H7e9WtOgwK91bUojLmUMhgWLE8ESQ805rb1XG-d4pNNTqGgqSdQ9mp3Rs6vgQMEA_zr078hWd5N2s-NzmwdXOqWtxfrMbx_rmMCp9oP5cNvjSMDF5ATUxDzaxS5Y0Ec5HeLf5f04L3PaTAsossiMehz3lKzccYGnIjmyXx4l50jR8B8LQpMVVbxLbJKI4CCYwlbZ8atxU8WhhCvqlrRmx1rhXtKn-SOdUdS6A0U1p6OKMdpdvLunQBrm27e9jeFLhS4ifBQk4ARbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc4f495813.mp4?token=te4CebcTf2GWtOKo7kOx851kG1EIjFaPP_VuM0iX-5n4GvaEOYiuYLhCzih9LexkxulslfbA5H7e9WtOgwK91bUojLmUMhgWLE8ESQ805rb1XG-d4pNNTqGgqSdQ9mp3Rs6vgQMEA_zr078hWd5N2s-NzmwdXOqWtxfrMbx_rmMCp9oP5cNvjSMDF5ATUxDzaxS5Y0Ec5HeLf5f04L3PaTAsossiMehz3lKzccYGnIjmyXx4l50jR8B8LQpMVVbxLbJKI4CCYwlbZ8atxU8WhhCvqlrRmx1rhXtKn-SOdUdS6A0U1p6OKMdpdvLunQBrm27e9jeFLhS4ifBQk4ARbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار محدوده شرق استان تهران
🔹
دقایقی پیش مردم در پاکدشت و قیام‌دشت از سمت شرق استان تهران صدای انفجار شنیدند. هنوز منشا و محل دقیق این انفجارها مشخص نیست‌.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/669656" target="_blank">📅 09:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669655">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8564f3ab.mp4?token=rbFnX-0m_qIlzB1NoiW9kxwmQtEBcDvCdguRgx86-o8xBcDpccZ0wwn7I7PaBFr4fykpIWcJFnOWjALoMyVwT11Ry6-75uMoio6eOVSly-mM0AOAMRGBDpT8Ym0dUrTiTqbGSQBaO11DCCf8jktdiRCOZThngAyDUZwZSEn8y8PlNxZ_6GYPgrrH1amw24VFC4W7uv6ey3Z12hcyFjdcQJYv3LBpEhAoSKDiNvG1mUF3ppn4ZXr6x_k8pbUdtz0dMPen4guDbbhhkuYEMmeTmypPxmpNfpDihAjiprpO5awPwdWMrc10HY10Xa_Ibcw4oSJQPmrw_Y5CQ_zny3ZeT6jiHy-8i_BSYZPDATX1gcSQh0tS9ZLJooNaWXpFkJY3eimcK6tmO7znGkj5zvwclXfhTrDMgd0Gp97vfo71c8_kOIEeBVi9G7SK0dgsnhd7gK31zvOcq8vVZa1enk48wOBuYVPkixFTNp0P3UtMhOv322PHz1ebrxlpptQxs8UYy2N2NV5HIelSn1ofP2QbRZan-DFxMEdzmjgUIhOAppmfeMFzf_v7H4VDmkWlGVO1y5xePTjq0RLAGsMDeshhFqH5r170BkLldetTZPKkP0IXJhITxBH-I1PQCQ5VguTe9e2O8tm7IpiDlCcxAkyhOavkF3Ft9_zZEMU6PROe9ac" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8564f3ab.mp4?token=rbFnX-0m_qIlzB1NoiW9kxwmQtEBcDvCdguRgx86-o8xBcDpccZ0wwn7I7PaBFr4fykpIWcJFnOWjALoMyVwT11Ry6-75uMoio6eOVSly-mM0AOAMRGBDpT8Ym0dUrTiTqbGSQBaO11DCCf8jktdiRCOZThngAyDUZwZSEn8y8PlNxZ_6GYPgrrH1amw24VFC4W7uv6ey3Z12hcyFjdcQJYv3LBpEhAoSKDiNvG1mUF3ppn4ZXr6x_k8pbUdtz0dMPen4guDbbhhkuYEMmeTmypPxmpNfpDihAjiprpO5awPwdWMrc10HY10Xa_Ibcw4oSJQPmrw_Y5CQ_zny3ZeT6jiHy-8i_BSYZPDATX1gcSQh0tS9ZLJooNaWXpFkJY3eimcK6tmO7znGkj5zvwclXfhTrDMgd0Gp97vfo71c8_kOIEeBVi9G7SK0dgsnhd7gK31zvOcq8vVZa1enk48wOBuYVPkixFTNp0P3UtMhOv322PHz1ebrxlpptQxs8UYy2N2NV5HIelSn1ofP2QbRZan-DFxMEdzmjgUIhOAppmfeMFzf_v7H4VDmkWlGVO1y5xePTjq0RLAGsMDeshhFqH5r170BkLldetTZPKkP0IXJhITxBH-I1PQCQ5VguTe9e2O8tm7IpiDlCcxAkyhOavkF3Ft9_zZEMU6PROe9ac" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوژه داغ اینستاگرام؛ ویدیوی بامزه و پربازدید از این دخترخانم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/669655" target="_blank">📅 09:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669654">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار محدوده شرق استان تهران
🔹
دقایقی پیش مردم در پاکدشت و قیام‌دشت از سمت شرق استان تهران صدای انفجار شنیدند. هنوز منشا و محل دقیق این انفجارها مشخص نیست‌.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/669654" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669653">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
قابلیت جدید اینستاگرام؛ اجازه ندهید از عکس‌هایتان برای هوش مصنوعی استفاده شود
🔹
اینستاگرام در اقدامی عجیب، قابلیتی اضافه کرده که با آن بقیه می‌توانند از عکس‌های شما برای ساخت تصاویر هوش مصنوعی استفاده کنند.
🔹
اگر اکانت‌تان پابلیک می‌باشد، این قابلیت به‌ صورت…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/669653" target="_blank">📅 09:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669652">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
آغاز فروش ارز اربعین با نرخ توافقی از امروز
🔹
بر اساس دستورالعمل اجرایی بانک مرکزی، زائران ایرانی بالای پنج سال می‌توانند تا سقف ۲۰۰ هزار دینار عراق را با نرخ توافقی خریداری کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/669652" target="_blank">📅 09:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669651">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLv1YjNZKXg1T2z6UhkDHq_acekLdj056fTUWYoc9eYdsyKq2kN9B_yy98PYxeFrnPVyjd-xxOqlBQbV7_uUyY72MULqZtsozmWbr0NI7uiuYFp8Nro07zkUpCNKHDtobMfk2ZMjbvBkHPciKouwHG1j9Ql_BVAHOxnj_8aFKmLabVAZdwrr7rgIC59SLUfqF_1EOLt4Os6NzxfP-gxK8FoZxOa8n6dJ9ZXfXVoERvSB_vIIBEjITD4YG3rW70SKt6plC5OeALYFYns0WySv_XYuGXgkxWZs6nOsxiICzBFXhs4nLNKbyIl4Mhr02eXiKdCMk8DnUKZhiODwtSQpmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سند خیانت حکومت امارات لو رفت
🔹
وزارت بازرگانی آمریکا سند جدیدی را منتشر کرده: تسهیل مقررات کنترل صادرات و ارتقای جایگاه صادراتی به امارات به پاس حمایت آن از تجاوز نظامی علیه ایران.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/669651" target="_blank">📅 09:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669649">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OJUD-bmaTl1bIB_1OURNHnQc_c-kYCI6AtZK8JQvLpPztlW1TOamw-m071_5HMkKL9b4Gjo3ZKPYC8oTquKFX8ij6-dO-DqGU4-ungmq0cI_FDjicyaYbXtVWdh2TRFqPeekKrA9uID1V6XnCl8Ong6FdkXbTgJQfYODFcgSKtryAAPxxT3vTirtVbQEXpGG5m0IJTGyh6G7KYMhJsH5Q5cHsqj8tizogViG8oLipCAhBdTQkzkR6ratIq9cgxdI06TYI1NQa03PxGYPao3GcOzRIXY4VxmLqtVuOX1wh8jyuc255to2B8WRNm5s1uA_sVWPgF2E46QCYzpZy9dZqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fpPDWH2jdb9MJsxokaLqpX-IYUElAV6n7-cjLcdqq3Ily1OO7psh8hLYeEgBH3OKbil4qGZ6EfSPfRhk29tVVvujV8uU8uq5jfWz0hW_oPBjx0eTmZqNqAXLIvzTsmNcexA3lP2HNkuhFg_xbe67JtoKPOaFjcT3owfa1UD4pEk2TwWXOXp2zd_bbAVlOe-G93dkaBdU81kJKA-KhWRDnvPB4gfMtLiN8F-lpzMm3Gk_YuRVY2wbIapdy6IC8iguM97zzKsPDd5XLI6-Cupx3AeIRxEuH5r3foZ6-c2GlAypII258RieFioEfGJjtvZTzQH6FLfxFr9QLu6HOtWHbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عراقچی وزیر امور خارجه با استقبال مقامات عمانی وارد مسقط شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/669649" target="_blank">📅 09:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669648">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c08c4f2cc6.mp4?token=eSFnbOwTxx0pvLY3wRjcYFJI1KjDkFOPinR-sAZeqZCqCOVLMDcOYUHrNkoJw5UcDzVN9pEcdS0zLW85VMIYHXZTVYJxM2TBoeFIQ8vLVS_KhnoiGtB9qkRP2mA1F9mcvq8XLzyU72U5mt1eGK18PmqsluMGg8kcjQu1WpoyjhD9Ixwlxnw8dh-zVAS7_RIxOmFMJa0BrMkmxtbHRcaD81s13PeerfSQq34IWwOEkd9W57ReihV0n8B0GcW_Ok8OmwC-CwMTNTqfmd-RZ9cjXyQ0xySqMEX5XUKC-9_uNEh-hBvWydWBMss-e_xDi7BAKHvN5BKGVZ1Z88kqPHNbnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c08c4f2cc6.mp4?token=eSFnbOwTxx0pvLY3wRjcYFJI1KjDkFOPinR-sAZeqZCqCOVLMDcOYUHrNkoJw5UcDzVN9pEcdS0zLW85VMIYHXZTVYJxM2TBoeFIQ8vLVS_KhnoiGtB9qkRP2mA1F9mcvq8XLzyU72U5mt1eGK18PmqsluMGg8kcjQu1WpoyjhD9Ixwlxnw8dh-zVAS7_RIxOmFMJa0BrMkmxtbHRcaD81s13PeerfSQq34IWwOEkd9W57ReihV0n8B0GcW_Ok8OmwC-CwMTNTqfmd-RZ9cjXyQ0xySqMEX5XUKC-9_uNEh-hBvWydWBMss-e_xDi7BAKHvN5BKGVZ1Z88kqPHNbnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک صبحانه سه سوته شکلاتی جذاب
🍫
😍
مواد لازم:
🔹
نان تست، نوتلا، تخم مرغ، شیر، وانیل، مخلوط شکر و دارچین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/669648" target="_blank">📅 09:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669647">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcMSVl97vLhQhmlcMfHC6pQrVo66bUxkl0Ah_vsodT7jE-hXe3uKIUfiuxs_CUL8YcI5ukzUy5hnZDh5omWLbGmEmb7Ofb2EocZ-BXe-QoaLhZS3E1WVYb-asIbdKJloiXWtBj_ePx_aYVB47Bk5UowFf1739Qmph9pOF8P03FIew--x7DzmuuUe6MnUAAqWKgG_mJ26yKANfIf_dhv9K07Oa_OxMmGZ1jn_D1xUv4lmj2Qn8yx4uHn3Z3r4i9DPlndTTBVNxszcTNI393CEsQJ3K3qcfX-yOogJjN-viDtsk3OB9Lbk0PIJVhoKwFuBFampFnqPuYimLjCaQXEoEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لوموند: تحرکات چراغ خاموش امارات به نفع آمریکا و اسرائیل
🔹
روزنامه فرانسوی لوموند فاش کرد که امارات در حال تبدیل کردن فرودگاه بربره در سومالی لند به یک پایگاه نظامی مهم راهبردی در نزدیکی تنگه باب‌المندب است؛ اقدامی که بخشی از همکاری امنیتی با آمریکا و رژیم صهیونیستی محسوب می شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/669647" target="_blank">📅 09:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669646">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
برآورد اسرائیل درباره بازگشت ایران و آمریکا به مذاکرات
شبکه‌های تلویزیونی اسرائیل:
🔹
برآوردهای اسرائیل نشان می‌دهد که ایالات متحده و ایران در حال بازگشت به مسیر دیپلماتیک هستند. به دنبال درخواست ایالات متحده، به ارتش اسرائیل دستور داده شده است که تمام عملیات «حساس» خود در جنوب لبنان را متوقف کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/669646" target="_blank">📅 09:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669645">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
نمایی متفاوت از مزار رهبر شهید و خانواده شهید ایشان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/669645" target="_blank">📅 09:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669644">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
آغاز مصاحبه آزمون ورودی دوره دکتری (Ph.D) نیمه متمرکز سال ۱۴۰۵ از امروز
🔹
ثبت‌نام و انتخاب واحد ترم تابستان دانشگاه پیام‌نور از دوشنبه ۲۲ لغایت شنبه ۲۷ تیرماه
🔹
مرکز مدیریت راه‌های کشور: جاده چالوس یک‌طرفه است
🔹
کره شمالی: آمریکا و ناتو در حال تشدید مسابقه تسلیحاتی هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/669644" target="_blank">📅 09:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669643">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMr5hEDuBfzs1pOL6qUc2AKxFi1OFigFy39NYoj7F0_Kf9mWR-cWCqkCr4YdDEneuC7Yty8zG2-f3i-zYZq0hxbsaCkSJHTczJcINBz9MqR8FlI6WKpfzfhSqiZnO0Bhq5pGgGVo6qcbTwRuEx-63l60m1NkwaIbHbIuKDCaUJH_kONDQDRd8Uf-qsb0V66nXbgZQugkpV94kqsOob22Gm2UqrnmTAzwHClnHmGD5HO0LYkVz9-vYtqkWyxluNnoqyoPRH7cayFbq_iUQhL1DAzkBn4Idmclf4tkxqm7eQgteTdJplZU1BWsoorJV7lW-MHR5uaoX__6_cfxlkgrOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش تدابیر امنیتی در اطراف کاخ سفید با دستور دولت ترامپ
🔹
سگ زرد در حال بررسی طرحی برای نصب نرده‌های دائمی جدید در اطراف کاخ سفید با هدف تشدید تدابیر امنیتی است.
🔹
این نرده‌ها قرار است در تقاطع خیابان پنسیلوانیا با خیابان‌های ۱۵ و ۱۷ واشنگتن نصب شوند تا دسترسی جمعیت و برگزاری تجمعات در نزدیکی کاخ سفید محدودتر شود. همچنین سرویس مخفی آمریکا و کاخ سفید در صورت بروز تهدیدهای امنیتی، امکان مسدود کردن این مسیرها را خواهند داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/669643" target="_blank">📅 09:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669642">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
کیهان: «پل ملک فهد» عربستان را با موشک بزنید
🔹
وقتی پل «آق‌قلا» هدف قرار می‌گیرد، باید بدون هشدار قبلی پل «ملک فهد» را هدف قرار داد. اگر به پالایشگاه‌های ما حمله می‌شود، باید به پالایشگاه‌های آنها حمله کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/669642" target="_blank">📅 09:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669641">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh00gnjogvEtZTuv3SKoj6Q7zeSqhcZOeSS4oHz3fl68X_KzStU-yeC23bF3h4m2bpvAEQVDVbFcFW8v5BneOv-MVKCtxSQfYGO6kM68-hfm_7R0oykkkauFD5Ra0hWXsnZ1sYJxqX2zZgjQsH4UCLzC0LlIq55DnMyv8cgVqWEhiLSa466i3Rk8eFshw1rRNB9gEzk687OQ5vt1oIXOmPn1eXBDudHjsIhHHW3ARduHlCVMfqh9CxzAVfbS97SEEecxvktFcnMHwUSJJzoBiZu4X3uLnUb61nEvrum3LzpeN4VH34tEek3YG-ZrVdb-7movV_6_sVaZSqtLBGStkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با خانواده روباه‌ها در قاب دوربین آشنا بشین؛ یکی از یکی بامزه‌تر و دوست‌داشتنی‌تر
🦊
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/669641" target="_blank">📅 08:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669640">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
انهدام محمولۀ انفجاری در مرز کردستان
فرمانده مرزبانی کردستان:
🔹
مرزبانان با اشراف اطلاعاتی بر تحرکات گروهک‌های تروریستی، بسته‌ای مشکوک که به‌ صورت ماهرانه‌ای جاسازی شده بود را شناسایی و کشف کردند.
🔹
در بررسی بسته ۴ قبضه نارنجک جنگی، ۸ قوطی تله انفجاری به‌همراه ساچمه‌های فلزی و کابل‌های مربوطه کشف و ضبط شد. این تجهیزات برای اقدامات خرابکارانه و ایجاد خسارت قابل استفاده بودند.
#اخبار_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/669640" target="_blank">📅 08:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669639">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63368e7741.mp4?token=UvEjcl4r0lH2ms4ejzEKyAK8YdAHhomMXi2lD7ybQIzsHDg85IvizmyaqyZSv7ZZzMPHkVYteK5a8m89PCD2cMAdyMGQvHePhfIOjeK4DATcuxZ8Jan43X0RWywj1g7wdHpXfv4V7IBGcF72Ye59voC9TM2PHJK8YFXh-UhG7Hez_8GEaqgEQMU7YhUcxVRxZO_OitxzqcV805-b4GDRbHycNsLWJDHUUvmgSQUPkf-xi9Inb_3I9HmYB20y9oQx865CLqojPienK0xq3iAcmXPAjCdvYrILTPVG5Ke1ibMwAhpJBqMLy8f3cma9pa-9oiMVVUEa2Bh6LqmMp7MkTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63368e7741.mp4?token=UvEjcl4r0lH2ms4ejzEKyAK8YdAHhomMXi2lD7ybQIzsHDg85IvizmyaqyZSv7ZZzMPHkVYteK5a8m89PCD2cMAdyMGQvHePhfIOjeK4DATcuxZ8Jan43X0RWywj1g7wdHpXfv4V7IBGcF72Ye59voC9TM2PHJK8YFXh-UhG7Hez_8GEaqgEQMU7YhUcxVRxZO_OitxzqcV805-b4GDRbHycNsLWJDHUUvmgSQUPkf-xi9Inb_3I9HmYB20y9oQx865CLqojPienK0xq3iAcmXPAjCdvYrILTPVG5Ke1ibMwAhpJBqMLy8f3cma9pa-9oiMVVUEa2Bh6LqmMp7MkTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله
۹۰۰ مار از مزرعه سیل‌زده کبرای قاتل
در چین
🔹
در پی جاری شدن سیل در یک مزرعه پرورش «کبرای قاتل» در چین، حدود ۹۰۰ مار از قفس‌ها گریخته و به ساکنان منطقه حمله کردند. شماری از ساکنان دچار مارگزیدگی شدند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/669639" target="_blank">📅 08:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669638">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phBTff5XLja0ZrwahHf0hY_srqwU-5ep42L6aH4u7YhJAoCgmfnWk9Fkcsnh2vGrrP-c4z4P8sF27OnT8K7feeabzJroaTcKHMgdBXkFZBk8p_fjqA9uOrrbfiUOrGP_yzKs6ZSvhoKieATrjuGi3MHxdwHErjF4Oqubwz91YFPjihsfZaWuC6WC25VpE4go2oZczyA46d3VirPfgQni-EWliMeJs39DTxN2dcsDqhM7PJtk2_izA2JJ2u9lgxMYD8K4B5f7ytyVVitucuUbNCUz3NQaaBau8Gs2IyLsZnyBDh0BnNRGboanvTjWAnU_vVP41K29FrwOwC9RUceZCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: نیروهای مسلح پاسدار امنیت و آرامش ایران عزیز هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/669638" target="_blank">📅 08:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669637">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کیفرخواست پرونده سرقت تجهیزات نیروگاه سد دز با ارزش تقریبی ۳۴۰ میلیارد ریال صادر شد
🔹
ولیعهد عربستان و ترامپ در تماس تلفنی، دربارهٔ آخرین تحولات منطقه گفت‌وگو کردند.
🔹
دستیار پوتین: غرب می‌خواهد دسترسی روسیه به مسیرهای دریایی را مسدود کند
🔹
هیلاری کلینتون: نظام انتخاباتی آمریکا متعلق به دوران برده‌داری است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/669637" target="_blank">📅 08:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669636">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/189cd5bfc3.mp4?token=azPtKkGOaLOgB3vq1NnQui7vOepB9gab9-DtG4CvQWgU7B6g8NGYnA1a6l1a5eZzU1uh5S3GELkr8Jjlu9CqeRs4uex6lpccLBM2RJvc1i642XMefIJdQvxD8kg45vHmCA7_22KQZo8PmGlJNc_bc1ylJX1KfdF5dn_EtTezHpCDe5F7Ja1xb_Y51u7Wv7tPWbNPIODS0LA2sqrtms8vScwhl70zkPiaw5hpMkioFv43J6dOqW14DAlFxXjDwilMOoComvRGB47qXLkbmdb1oTtZGhMEw6tM8Ayra-a3jDp3trQf3QnPnE17ON_xdHfpbfkJHFZ6hUSzNd78Jss28g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/189cd5bfc3.mp4?token=azPtKkGOaLOgB3vq1NnQui7vOepB9gab9-DtG4CvQWgU7B6g8NGYnA1a6l1a5eZzU1uh5S3GELkr8Jjlu9CqeRs4uex6lpccLBM2RJvc1i642XMefIJdQvxD8kg45vHmCA7_22KQZo8PmGlJNc_bc1ylJX1KfdF5dn_EtTezHpCDe5F7Ja1xb_Y51u7Wv7tPWbNPIODS0LA2sqrtms8vScwhl70zkPiaw5hpMkioFv43J6dOqW14DAlFxXjDwilMOoComvRGB47qXLkbmdb1oTtZGhMEw6tM8Ayra-a3jDp3trQf3QnPnE17ON_xdHfpbfkJHFZ6hUSzNd78Jss28g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم هوش مصنوعی از ترور ترامپ توسط بادیگاردش
- من خیلی بی رحمم
+ نه! تو بی رحم نیستی...
توسط قلب‌های بیدار، آن اتفاق خواهد افتاد! حتی اگر بادیگاردش باشند...!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/669636" target="_blank">📅 08:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669635">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219f605331.mp4?token=aOWJA1CYkYkkeDT4naa-KK0o62TLrZdMgh6CpeW6AM4BXI20CA385Ix09GAzo8r2Ro6GEBDC_x1Iak4CVdcAewQj6uZnnjlVg45-WPxICQtxtFMUgZYTpVpc8ktcdh7U3pIwSRSJAs50AfG-UBeYHBT4fu_5gaTjiIRBTxdtpQvvOV0F-GHmiC01A5nT7nLvh988cwwBO0DzvO72UCoTBFwyDAjy8-Bme-iabKyK0UKHUl5AZR3keInYRRMx4L8H26m9IPY1SIbyVZCvFkeg1QeLoFD056y6jqo6oLDAdVIYlTpgPcwThaa2rikYX1-gpwOQ-Q-6Rhb3TRlGLG-4hAfIST0XO0cby60JrpkMi-gwgEGE78tu2RS-9bTCAjPjefDTzPFZGNDY3bJNtHFWsdtfBhLn5v95m3odEbKlOBbcHDLmoAlpaFdVz6xx-dZjB756d7XMkc578SY1B-Y0z7lY3LlITpivBS8wEhuUU4Wh0pjHiRSys5kk_oy8MZbbJ6TrriY0qPBH4remMyQO-z0qcH_RkpEsLusZRURG7e3Ix_Z1UQDBGWuAj8ZM5KQ_7I-ZzqmuH1zHGYabMIGYMbUfS5DTr7vW4gmuqDNgLQmePzbEV0cZU6jXLdJSw3v5CZqIhhsbAmnyS_ILE2549vfrZo9AArr8Z_-xWiJDLhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219f605331.mp4?token=aOWJA1CYkYkkeDT4naa-KK0o62TLrZdMgh6CpeW6AM4BXI20CA385Ix09GAzo8r2Ro6GEBDC_x1Iak4CVdcAewQj6uZnnjlVg45-WPxICQtxtFMUgZYTpVpc8ktcdh7U3pIwSRSJAs50AfG-UBeYHBT4fu_5gaTjiIRBTxdtpQvvOV0F-GHmiC01A5nT7nLvh988cwwBO0DzvO72UCoTBFwyDAjy8-Bme-iabKyK0UKHUl5AZR3keInYRRMx4L8H26m9IPY1SIbyVZCvFkeg1QeLoFD056y6jqo6oLDAdVIYlTpgPcwThaa2rikYX1-gpwOQ-Q-6Rhb3TRlGLG-4hAfIST0XO0cby60JrpkMi-gwgEGE78tu2RS-9bTCAjPjefDTzPFZGNDY3bJNtHFWsdtfBhLn5v95m3odEbKlOBbcHDLmoAlpaFdVz6xx-dZjB756d7XMkc578SY1B-Y0z7lY3LlITpivBS8wEhuUU4Wh0pjHiRSys5kk_oy8MZbbJ6TrriY0qPBH4remMyQO-z0qcH_RkpEsLusZRURG7e3Ix_Z1UQDBGWuAj8ZM5KQ_7I-ZzqmuH1zHGYabMIGYMbUfS5DTr7vW4gmuqDNgLQmePzbEV0cZU6jXLdJSw3v5CZqIhhsbAmnyS_ILE2549vfrZo9AArr8Z_-xWiJDLhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات شنیدنی استاد دانشگاه کمبریج از دست برتر ایران در تنگه هرمز و چرایی عقب‌نشینی آمریکا از تفاهم‌نامه‌ای که به سودش نبود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/669635" target="_blank">📅 08:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669634">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14637fa412.mp4?token=ESNrGeSzhfTzgBPgJIjE1wYH8nNpOMDXxSUxG9NJl0QmLxZqb39NFBCg7GqBNQy7ZWbM_ZSqfflXTBpHh5np5dEEFcdai4AU05cm7FxgPFw6JN9xM3ADejDsZjlrU8fX8rblAkRoVT6mmjGoZdRGUG81xAAI_IJCQVyK6vtMd911wa6suuHfJ6E9b3QIH9DpK1tg9ySC-nUKjD8f80fkERxDLQOkHH6H_rE2XnKVqZbpDnL3_SjNw0I8lKxj0XRUY4jzZCFdRvQr4_FxnpN-UI5jZuAXfnAueusdTNUcnXob2BQohQzpteTiNzfdgE9WuNHBYTNm8UhXcoK7316g3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14637fa412.mp4?token=ESNrGeSzhfTzgBPgJIjE1wYH8nNpOMDXxSUxG9NJl0QmLxZqb39NFBCg7GqBNQy7ZWbM_ZSqfflXTBpHh5np5dEEFcdai4AU05cm7FxgPFw6JN9xM3ADejDsZjlrU8fX8rblAkRoVT6mmjGoZdRGUG81xAAI_IJCQVyK6vtMd911wa6suuHfJ6E9b3QIH9DpK1tg9ySC-nUKjD8f80fkERxDLQOkHH6H_rE2XnKVqZbpDnL3_SjNw0I8lKxj0XRUY4jzZCFdRvQr4_FxnpN-UI5jZuAXfnAueusdTNUcnXob2BQohQzpteTiNzfdgE9WuNHBYTNm8UhXcoK7316g3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۵ حرکت شکم روی صندلی برای تقویت عضلات مرکزی #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/669634" target="_blank">📅 08:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669633">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
امروز شنبه ۲۰ تیر؛ رسماً وارد گرم‌ترین روزهای سال شدیم
اصغری، کارشناس هواشناسی:
🔹
هشدار جدی برای شرق کشور: بادهای ۱۲۰ روزه در خراسان جنوبی (طبس، زیرکوه، سربیشه، سرایان، عشق‌آباد، بشرویه، نهبندان) و شمال سیستان و بلوچستان شدت می‌گیرد و احتمال خسارت وجود دارد. بیماران تنفسی، سالمندان و کودکان در ساعات آلوده از تردد غیرضروری خودداری کرده و حتماً از ماسک استفاده کنند.
🔹
تهران امروز برای اولین بار در ۱۴۰۵ به ۴۱–۴۲ درجه می‌رسد و اگر بشنوید قم به ۴۶ درجه رسیده، تعجب نکنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/669633" target="_blank">📅 07:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669632">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aec7675d7b.mp4?token=JDDpP6vU8jhDv3vGPO0wXcgXjB_CA9QFniY5jHbaqTp-7hrDWA2nvNYn47DCw7dacVA9UXCgRVYKs8SdYngYGg-YE44bHEwLwBviOAdoFsJorDklJWTzmhJ47ZwXcYhJNySRqY3fVRMIPJYQJ3Jxrll9W8jHw0ouNigtg83SE7o2gHPdQ0qdeFHef-tPQj3is8jBNwe5aEMqUiqCkbY1esWbtS04T7CP7jug-QNgzsdPPgWhZLyuQNA6rDfLlxWdJQavh9DA2B8Dtd5vdtMLQ7In4ioA8lieLTV5t4YZv2xx3V9OtfjXCk0hM8G3nYmhRjosFxyzIhj8XNkVhX7WHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aec7675d7b.mp4?token=JDDpP6vU8jhDv3vGPO0wXcgXjB_CA9QFniY5jHbaqTp-7hrDWA2nvNYn47DCw7dacVA9UXCgRVYKs8SdYngYGg-YE44bHEwLwBviOAdoFsJorDklJWTzmhJ47ZwXcYhJNySRqY3fVRMIPJYQJ3Jxrll9W8jHw0ouNigtg83SE7o2gHPdQ0qdeFHef-tPQj3is8jBNwe5aEMqUiqCkbY1esWbtS04T7CP7jug-QNgzsdPPgWhZLyuQNA6rDfLlxWdJQavh9DA2B8Dtd5vdtMLQ7In4ioA8lieLTV5t4YZv2xx3V9OtfjXCk0hM8G3nYmhRjosFxyzIhj8XNkVhX7WHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رامین رضاییان که ابهامات زیادی در مورد ادامه همکاری او با باشگاه استقلال وجود دارد؛ با انتشار استوری از تمرینات انفرادی در اسپانیا نوشت: خبرهای خوب بزودی از راه می‌رسند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/669632" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669631">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec98df592c.mp4?token=o74aOoFlOhP8qaeh8r6vgLDUz3OJUecJMe4wP7IHmnwPsxs86n2NBgN-dSItwhGmiql2hPmo7AKJvk90CAnmsGxXk2NHqONIPJK9tT3H9BUlKmptTEw5PlDXG4r_nL8zqfHJezbWovfrrTto8urQ-HG74c1TVIuH256-LrLVCvvyzZzVPkIwnfQfPR1XeukxTmy0Dc57xIgtdUIWgzUIOfK_wUfYqULuyjI1xtJfpGtlOvkskjbtyPEvJdIlux88mh5AzG4vINPGuHMgx5TZQk5nWR6mwsbm7XkV1P0XrUlCgrhn5TwBzbKeKYJOqLD9HSFDJUM_SsANJYmYUZqnjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec98df592c.mp4?token=o74aOoFlOhP8qaeh8r6vgLDUz3OJUecJMe4wP7IHmnwPsxs86n2NBgN-dSItwhGmiql2hPmo7AKJvk90CAnmsGxXk2NHqONIPJK9tT3H9BUlKmptTEw5PlDXG4r_nL8zqfHJezbWovfrrTto8urQ-HG74c1TVIuH256-LrLVCvvyzZzVPkIwnfQfPR1XeukxTmy0Dc57xIgtdUIWgzUIOfK_wUfYqULuyjI1xtJfpGtlOvkskjbtyPEvJdIlux88mh5AzG4vINPGuHMgx5TZQk5nWR6mwsbm7XkV1P0XrUlCgrhn5TwBzbKeKYJOqLD9HSFDJUM_SsANJYmYUZqnjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایش پهپادی دیدنی در محوطه «اهرام ثلاثه» مصر برای تمجید از میراث و عملکرد محمد صلاح
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/669631" target="_blank">📅 07:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669630">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
رونمایی چین از سلاحی که هدفش را بدون اصابت زمین‌گیر می‌کند
🔹
چین از یک سلاح مایکروویوی ۱۰۰ گیگاواتی رونمایی کرده که برای از کار انداختن پهپادها و سامانه‌های الکترونیکی طراحی شده است.
🔹
این سلاح به‌ جای انفجار، پالس‌های مایکروویوی فوق‌قدرتمند را به سمت هدف می‌فرستد تا مدارهای الکترونیکی، سامانه‌های ارتباطی و پهپادها را از کار بیندازد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/669630" target="_blank">📅 07:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669629">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rv7vVmfC354pdHaXNgFoAqECwXnY0YM5AJnHc5oEXcpEDHq5nnP4eKB_2JtmqmRbELkn5Ba_yidAHjfnN6wF8o5CBVMf5TnZ1OcuFA3IRzrWIbECXdVQfRInzURXMCqhgFULb9RUlvFGtB6JfZaMktz8yozA5CNu1zrCWxnyTGohGl8IB9PHkNRvRYwyCuxdrtggh_6HOp76GL_W5lZHP5GToetNNVEdGBHDWnhjtPeeubBuTmA51i7TXiyx-0g3y7ohd8ZSfJW8xVNns7kRRNfdWF3kxSgGoZRjnBkAHOL8DosHFQGQdeQTCegm9tjnXWumljF8v593cxHn0NMfSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان روز دوم مرحله ۱/۴ نهایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/669629" target="_blank">📅 07:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669628">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مدیرعامل توزیع برق تهران: برق ادارات پرمصرف از امروز ۲۰ تیر قطع می‌شود
🔹
فیفا به ونزوئلا پس از زلزله ویرانگر، یک‌میلیون دلار کمک خواهد کرد
🔹
شمار قربانیان دو زمین‌لرزه‌ مهیب ونزوئلا، به ۴ هزار و ۱۱۸ نفر افزایش یافت
🔹
وزیر خارجه ترکیه از سفر قریب‎الوقوع خود به کی‌یف خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/669628" target="_blank">📅 07:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669627">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbZ5KqCDizNgT_Wh98FYZTnZciCRxZ9lVaVPqU9VVjQKUOj6_PcscYYTDFPgZcMu0cF3tWxdpZ0eHzkWzIJxeAvNx3QFgNHQ0Xjj99-MhJdSvbw-MI5Pk6fP4cjAamfgdh8njbt4XYj_gRKdcC-eJfsffV8ZRXkZqRSdclZJKfcI0Zuk2yqT-uVlQ-VSAIs17vccVNKhXmfKrhd13Tskrl9U-p2dGBrBUgvC_kNaVbMsro0VMMeK30_St3X1b7qrTKSIMb-wMn1Da8i1_kR664FiwMd9T9qcBkIbd2QOwrHlTZa8rC5BUI9KKVHmGuK--jxRCzo6bfvQtbE3ZfZsdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: ایران تاکنون به تعهداتش پایبند بوده اما تنها راه، پایبندی دو طرف به تعهداتشان است
وزیر امور خارجه:
🔹
ایران تاکنون به تعهدات خود پایبند بوده است؛ برخلاف آنچه از سوی به‌اصطلاح وزیر خزانه‌داری ایالات متحده شاهدیم که با نقض بند ۹ یادداشت تفاهم، تعهدات آمریکا را زیر پا می‌گذارد.
🔹
این نقض، در ادامه سایر موارد نقض تعهدات و اقدامات نادرست آمریکا صورت گرفته است. واقعیت روشن است: تنها راه پایبندی متقابل هر دو طرف به تعهداتشان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/669627" target="_blank">📅 07:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669626">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
کالابرگ سرپرستان خانوار دارای رقم انتهایی کدملی ۳، ۴، ۵ و ۶ شارژ شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/669626" target="_blank">📅 07:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669625">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2KlrsQqkK0m3_9uUYetwogEVQQsLBNLjeXsWXUUhVo2UtkDP6BgSZYggF3dsP9Bkrubwna9OQlx5hz_nVtiaWiFavL5cx_s6nBXsJ0xPUpP03bflhetgL1cTV_FexoSiMS4TOyC30dR7bLPNCA0Aa0wm5oVe5SwOAEpfAXt4CWbB6PkjQU-r-vZ9lTomd5tnGuLi9SZZlRdhd9HQFk06_p9DN0m7GAkXOyEI6gIdu4IqNmOWc4QPvibjjbsCPRFozVetx3R7uGp2vpKNOXlEYuj4f20PDUMWn5xjIfPdtAp7GBbXs_6E0E-3brnd3KZNGjbK5ACoC08eqTu9a-12Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوک هار در پیامی سرشار از ترس و خشم، بار دیگر ایران را تهدید به حمله کرد
🔹
«هزار موشک مسلح و آماده شلیک، جمهوری اسلامی ایران را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — حمد و سپاس خدا را! »
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/669625" target="_blank">📅 07:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669624">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcOxCBcubvRf-cN9K0lDlK3vEim_zZaBCZ6MEP7CZwb4R15zMEmrMHBlVmQArW4rYlND1kWsKu5crh6yedwX169gbiFY_P3hzPpOTLyr8kKHYCVp7wz8X-dDzo-EYWDmfe_sQwEn7KsxJDFeGn7Xo5Uksf2HN5yJwAgPfcy6lTygeJOVyxnFqBpETgQZGMEnFWcJwIbhMf9UKbUH4KhTeUWcQZf7NiU0UDnPNwIoyjU8G21kOiHen3EVvWG-AI8r6qsmLjf0oVVL3KENuNshS1uEIvGRkUo4VC7HUuToU2gnu60Lsep6mC4_LIbz5O4UVcM8-16cyucE-YE_U-__CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۲۰ تیر ماه
۲۶ محرم ‌۱۴۴۸
۱۱ ژولای ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/669624" target="_blank">📅 07:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669623">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg9mvXNx2MPKd3PdaSR7MGZjhqZvKG5EixGCPsWu_qpv5yk6f-Mtt392uKA2KIbYB1uU-eZySfaPxW-JRqKaptLbU-pdKBd0EINFdX2USjYBypjKJkiM_JmXtRaH8xeOEN8LO-M1BAka-rFKZVSXCxthuvOrZJLbQdLf6o-3fp-IVO_idgCuAjjcgDOqNW_ZBveEcC3ib00FubvfyCn_aajq6qyjnaKQwnXgHMZGPMfjN217YvSQ9cwnV1GKgij-Cxnu8jZVienEwhhKW2izMvHxvk38Oul_O_V_vMc80gTN0ggWbo1ggR-umTAkKV7UfhCpOG-rXhN00uWf9M2rbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/669623" target="_blank">📅 01:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669622">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUucDoN72ia3PH7Xy0x60z4CrV7GAftqsJJ37vlJfmueVaK0HTQGzMgYnsIZMRBxKS_uMkDUfTkybKO7NYqnNEZ9h165RKo_nVdUAFgf_r6S5swZNnWJBKufGBwErK4Y3F7DoRC9Hy7_8W5ks9uKcltvp7adlQoE7gjx6KKsdGziftPL2UDjCT5VB5LybcYW6Q2_tW6s2HKbfGJGSD1v3JIfV-iWItJ0wq1-LHVwy6XtZT7lKWmNJZni6q0Yl1B0IDTzvXEKFwUsinmgdnuYxE8e2RYnQFYY8UoezX0FAW-TWq2uIQ-i8pam75el8Gx3VlUtzbddeEuMjT2TUkQDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۷ شهید و ۱۱۵ مصدوم در تجاوز آمریکا به ۶ شهر
رئیس مرکز روابط عمومی و اطلاع‌رسانی وزارت بهداشت:
🔹
در حمله هوایی آمریکا به ۶ شهر کشور در ۱۷ و ۱۸ تیر ۱۴۰۵، ۱۱۵ نفر مصدوم شدند که ۲ نفر از آنان خانم بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/akhbarefori/669622" target="_blank">📅 00:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669621">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b443f6dd0.mp4?token=jOZCrwC508d6oU1OvxDbECSSERDY51kY1aXsuYCfFp6kgalYg04pmIxNFtALBoHLMtq3adVZxiF5emYuriqmB3GKYiffer6EFVqE5J7CfQa0Exbw4p6Fd2koAduDNBrVRjb6VnbFNAPa7N3_NWoJ3UX0oFc5n55FruwyoxvXeB07RwtiY27Qn0VfS6GeZ1bYSPFW_Jg_vPtj7YzrM95KaV41AkXH9L_sdzWZp1-51wUL9Qx0HvpHZ6P6pMYtQA4RhmnoLU9ZqtlgHUkQL6OBKX8eom2nep6T4xochDYv-elwCQNYdhOt6HYMs4bgJT8_l1bhWddaiMzETiiHco7ttw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b443f6dd0.mp4?token=jOZCrwC508d6oU1OvxDbECSSERDY51kY1aXsuYCfFp6kgalYg04pmIxNFtALBoHLMtq3adVZxiF5emYuriqmB3GKYiffer6EFVqE5J7CfQa0Exbw4p6Fd2koAduDNBrVRjb6VnbFNAPa7N3_NWoJ3UX0oFc5n55FruwyoxvXeB07RwtiY27Qn0VfS6GeZ1bYSPFW_Jg_vPtj7YzrM95KaV41AkXH9L_sdzWZp1-51wUL9Qx0HvpHZ6P6pMYtQA4RhmnoLU9ZqtlgHUkQL6OBKX8eom2nep6T4xochDYv-elwCQNYdhOt6HYMs4bgJT8_l1bhWddaiMzETiiHco7ttw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خوشحالی جالب برادر خردسال یامال با او پس از پیروزی مقابل بلژیک
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/akhbarefori/669621" target="_blank">📅 00:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669620">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ادعای اکسیوس: مقام‌های آمریکایی در یک نشست توجیهی با خبرنگاران در روز جمعه اعلام کردند که دولت ترامپ از ایران می‌خواهد روز شنبه بیانیه‌ای علنی صادر کند و در آن تأیید کند که تنگه هرمز باز است و متعهد شود که حمله به کشتی‌های تجاری را متوقف خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/akhbarefori/669620" target="_blank">📅 00:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669619">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX6iBYGLMdpomV0bHAcBhBQRWRIfTIhBYycmJZsXEkoVJkK_xNK-ED82VnOZXiRJCdCBtdrwJ_LjT-tsDh59UU1ixGpWN4e0F9JYnbCbL8HMVukQ6c-5K5whhIBeIMdg0xGg4xFiPtbPZ4gGfNqESCa2tSd17zM8xaoAUiLVUNGAncLMqdz-RKGeYLatKllsdk-3vlycHOxw8TUwFs2kMBHNfTP9eSlMyTXH0CcZXFCasYeN4O3lE9hv4up8Uohi41bmyLEpsf10emaHcMb9ofIZwb8yf0dDlOrcrELfUm5D746WQRaDRL16vcXBHq-9tmTMS5hpveCjcnHuOGUjpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فرانسه - اسپانیا؛ تکرار نیمه‌نهایی یورو ۲۰۲۴ در نیمه‌نهایی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/669619" target="_blank">📅 00:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669618">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0a56bdab.mp4?token=exDPe4GA9fqGnpqEdCh564SCVuFf1rqgz5wtWXnLkfL8jU0HNib2mnEHzdd59EFX_gKV_bEQhHl09lDfAophQeQRm-7cXSRonz0D2L7I7Lb1eMckIq2fBV_mWxO7HBIu4GNNNA6dSZfBlBp6lGiTulz_tlXqkcYc2k1x8faIrToV9jBbX-J1jVpPmOh2GbhC8RkCm-d5v_Q_tHUhMrbuhUmltteSTtoG1UY_GYHeyyQMUORqtUbHgA8nrH6bdjAuNEAHa2WsE7ob-j_u80YSZGpmJRVbgLEx7Ep93mQ_5bEVkfk7BLn7ycVxANzQNJ0YQUFHLusdBjv8NW9LrFAtlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0a56bdab.mp4?token=exDPe4GA9fqGnpqEdCh564SCVuFf1rqgz5wtWXnLkfL8jU0HNib2mnEHzdd59EFX_gKV_bEQhHl09lDfAophQeQRm-7cXSRonz0D2L7I7Lb1eMckIq2fBV_mWxO7HBIu4GNNNA6dSZfBlBp6lGiTulz_tlXqkcYc2k1x8faIrToV9jBbX-J1jVpPmOh2GbhC8RkCm-d5v_Q_tHUhMrbuhUmltteSTtoG1UY_GYHeyyQMUORqtUbHgA8nrH6bdjAuNEAHa2WsE7ob-j_u80YSZGpmJRVbgLEx7Ep93mQ_5bEVkfk7BLn7ycVxANzQNJ0YQUFHLusdBjv8NW9LrFAtlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات بی‌سابقه عبدالکریم سروش درباره تشییع رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/akhbarefori/669618" target="_blank">📅 00:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669617">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427ac3b010.mp4?token=vLY9f5SBvGDKtmrXAKYdcHM2JzXKVO0Ux3XqFNEm3rUUcfAm-xUGAJgeqli7YlBrdADidkiUwGM_YChLwOuL2jDbCH_d73hHNi3cxxBgOKh6himJ2hK1x9rgTZt3Yn__iG8UqdgeA9JwEpUDL7NRaFHrzH2tVH1pHnpUb4H_-9YFvei7MiaJeOUXy1icMkP7n1LedyuNGNeIMX6b4HKLsRvrhwgKUBwWUqUMNoxAL_FTu2C2Z6ggrdhm72o72WOBddHw0K_IcboeyyaMYO8lWYseCB2lNdUvEyOVk83bZ3nl66Z22P1eVFOu5xOx09c6uzse-2GG9aYB5-uipqMcnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427ac3b010.mp4?token=vLY9f5SBvGDKtmrXAKYdcHM2JzXKVO0Ux3XqFNEm3rUUcfAm-xUGAJgeqli7YlBrdADidkiUwGM_YChLwOuL2jDbCH_d73hHNi3cxxBgOKh6himJ2hK1x9rgTZt3Yn__iG8UqdgeA9JwEpUDL7NRaFHrzH2tVH1pHnpUb4H_-9YFvei7MiaJeOUXy1icMkP7n1LedyuNGNeIMX6b4HKLsRvrhwgKUBwWUqUMNoxAL_FTu2C2Z6ggrdhm72o72WOBddHw0K_IcboeyyaMYO8lWYseCB2lNdUvEyOVk83bZ3nl66Z22P1eVFOu5xOx09c6uzse-2GG9aYB5-uipqMcnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سی‌ان‌ان با انتشار تصاویری مدعی شده که ایران در حال بازسازی برخی از سایت‌های هسته‌ای خود می‌باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/669617" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669616">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53005e601.mp4?token=m3V3EcazFoXpDJEQWPx96ldie37n4auF7stH3TAK9XEGHcRyUfQt3E7R2fTF0JX8UM21PTeIl81msAeCuvxy6mIERIXIhb_vFCnsM_L6QtPMJZeMq85_kqWtdUkX2NVOsQwecICqssTt6mzE7mzdHy7OsZCbNlM76GSoKlCAK6ci34RzFe2VySzBo9ZqprF5db9OiIzgWBv7RklooJcvplUQsEfpqqKdPG_cV5lCF2re_QtjDjORMynf_9BabqiQKpv37VSa009BlLEDMVhplYslK9FdZCE1oe9yIy3lIUcEeqeZkcQlOc2pBuTXyp7xPeJpUKb5xUnX4qIfHSpOeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53005e601.mp4?token=m3V3EcazFoXpDJEQWPx96ldie37n4auF7stH3TAK9XEGHcRyUfQt3E7R2fTF0JX8UM21PTeIl81msAeCuvxy6mIERIXIhb_vFCnsM_L6QtPMJZeMq85_kqWtdUkX2NVOsQwecICqssTt6mzE7mzdHy7OsZCbNlM76GSoKlCAK6ci34RzFe2VySzBo9ZqprF5db9OiIzgWBv7RklooJcvplUQsEfpqqKdPG_cV5lCF2re_QtjDjORMynf_9BabqiQKpv37VSa009BlLEDMVhplYslK9FdZCE1oe9yIy3lIUcEeqeZkcQlOc2pBuTXyp7xPeJpUKb5xUnX4qIfHSpOeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جلیلی: ۲۰ سال پیش یکی از مقامات اروپایی به من گفت این فشاری که به ایران می‌آورند را اگر به کشور ما بیاورند ۶ ماه هم دوام نمی‌آوریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/669616" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669615">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3acd0f9ca9.mp4?token=tzJAMJk2UcJ7Ima6A2SXP7F47XqDflec8HdqiVXu8CgLoYdbDnHgJi-cUiS5dIs_hM8-uct6f5Xo9s3_E2taP2bGtJGZUd1qQI-awAbmfyfRxHdXIagN67Ukg0ezNEJaZbvV7k3ULrfQfM9VBWog-jXOOzZYjhhh7HGdmSB8GW6aCDxf_D8-EEXJwWw8vY04xpu5GsztGt4r3_y0twzHJtkt25K_YquVjc2RY6LnKFl7D47hsgu7c9gwsTYA6LBuCuH3Js-Jj_Otw5lyFuW_CYVzThido0liLpJ7Mp4pkE-yLaNzHOOux8y1V5hgpJ4orGBA1L9y4jV8P1e0alQRAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3acd0f9ca9.mp4?token=tzJAMJk2UcJ7Ima6A2SXP7F47XqDflec8HdqiVXu8CgLoYdbDnHgJi-cUiS5dIs_hM8-uct6f5Xo9s3_E2taP2bGtJGZUd1qQI-awAbmfyfRxHdXIagN67Ukg0ezNEJaZbvV7k3ULrfQfM9VBWog-jXOOzZYjhhh7HGdmSB8GW6aCDxf_D8-EEXJwWw8vY04xpu5GsztGt4r3_y0twzHJtkt25K_YquVjc2RY6LnKFl7D47hsgu7c9gwsTYA6LBuCuH3Js-Jj_Otw5lyFuW_CYVzThido0liLpJ7Mp4pkE-yLaNzHOOux8y1V5hgpJ4orGBA1L9y4jV8P1e0alQRAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فاکس نیوز: بر خلاف ادعای آمریکا، کشتی‌ها از مسیر تعیین شده ایران عبور می‌کنند
🔹
فرماندهی مرکزی نیروهای دریایی ایالات متحده اعلام کرده مسیر جنوبی تنگه هرمز همچنان باز است و گسترش یافته است. به گفته ایالات متحده، سایر مسیرها محافظت‌ شده نیستند.
🔹
اما دیروز ۲۲ کشتی از تنگه هرمز عبور کردند. تنها ۱ کشتی از مسیر عمانی عبور کرد و اکثر آنها (۲۱ کشتی) مسیر تعیین‌ شده توسط ایران را انتخاب کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/669615" target="_blank">📅 00:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669614">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aehbyQRWtQZDdYsQXs5b0LMZSHPY_5hYlTyZPQvLtDuzJSkoUAkMJaOcOKTnCGOXeDcC4HoTdr0VPun58ttBMZs59zPg4X-PHfkfGK3WomOwDCgb_viZl4126liDQgT47tONnVjbSORYo3TRJVyX5MFawyO5VlIkJ_2RDKSGYRTFdYb4DaPt6XgG7ZdbV5ManeGVWgMEh8kVfzLvg_HUK7GqQ1Hhts4vL37_XhNRaimLMHcZwIaf70YaZ0lRgGIky6gZnT7yAY4dSbOo1cvIh2-00ix4rjOMQjFf--Zln8g3TyRl5GMT9OzC2-IEBYxed4U5i_LxFWDdG_pUyPDQQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل دوم اسپانیا به بلژیک در دقیقه ۸۸
🇪🇸
2️⃣
🏆
1️⃣
🇧🇪
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا     #بیمه_پارسیان #بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/669614" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669613">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4767632a1.mp4?token=kLrs_SUQue1UNhq7kwa756x7rZBOVSK0pLaD3USTQO1R3z970JnD_o0laay55WuRsyCoUzoeZnNMbR4X--KCW9Hc7r7DZscWv7QWHVG3FcaNqysXhjWGioejngYMRrXDOovNX9uLco6e2_Ikxn0boEjUr0tgh7fWGzkXpPnhC6hruzlkpIHHB1WvLa6O-6gu_732Ny2Fkn3FZdqtAIDTxW_NYv9Vk8pG7cNmF3_iM85zK1PLcIj1yVqS2Kx17Vd9gNkCExIc9HA4uWdBMH8zYOxfy0ho0HUQkD1GT1r2a0lPmij39Big3hzctPLiftwFsZg9wV1BTLuiuvalI6uFzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4767632a1.mp4?token=kLrs_SUQue1UNhq7kwa756x7rZBOVSK0pLaD3USTQO1R3z970JnD_o0laay55WuRsyCoUzoeZnNMbR4X--KCW9Hc7r7DZscWv7QWHVG3FcaNqysXhjWGioejngYMRrXDOovNX9uLco6e2_Ikxn0boEjUr0tgh7fWGzkXpPnhC6hruzlkpIHHB1WvLa6O-6gu_732Ny2Fkn3FZdqtAIDTxW_NYv9Vk8pG7cNmF3_iM85zK1PLcIj1yVqS2Kx17Vd9gNkCExIc9HA4uWdBMH8zYOxfy0ho0HUQkD1GT1r2a0lPmij39Big3hzctPLiftwFsZg9wV1BTLuiuvalI6uFzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم اسپانیا به بلژیک در دقیقه ۸۸
🇪🇸
2️⃣
🏆
1️⃣
🇧🇪
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/669613" target="_blank">📅 00:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669612">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLtqmLGmuV3YZ9kx2dkb7IyhjlCOn2w7U2bEHNniyGCirpNwezKXL9jvoyWVq4tW3ybZ9hPMN_AQ_ObsmfaPxT91HGDmPEW-uOxpVDF0PdHhtSjuFH4sO2bbn9dQdRgGIHze4odfObNVVCfAnysp0nSPKK1zkJE6dhTz8sW1Rm7CT89Espg4o-t1NaTBnLj_L9GzwhJZcf4teuCev9EQyL1GBCHsaAU1DGm6N7flZ70G5d5bWp7QVuFEsDJ3qV5GWORDZsMJA0e01GBaCpbTG_TlsH9AHTwejFsTZSZQhDtvPdubrvfMSFW52a_RFGl3uY3qINnfRarYgDe5kP3nsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا تحریم‌های جدیدی علیه ایران اعمال کرد  دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا:
🔹
اسامی ۸ فرد و ۶ شرکت را در فهرست تحریم‌های مرتبط با ایران قرار داده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/669612" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669611">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2pQkhd9xOs_lbusBGIYoc7GKRF8NlCkszYLCet1K6D6nrb6vV0su0CHEpsVfRHanufW8XFcBeq_-yzvQtT5d1_HnGv4MWyg_eq_CJ2PfO9x96lA9xJuCbcwKpMxrOqdgFGizQGG7jMegAjkA2AlYgTtswNmOJGM0hNbCu072xgn9ALmhVR7YugKT81hfbDZ45eiDF6K6xvOKNnmsnrdNouTR--AXYXRKN4qsQ93x3p1KLCcjU2M5gKJ5IBVUpE5zWQP_MVCsN4UOJg8w44iWKFzUVj1M-aU5rBcTRgio9gnXApDi1V49bDl9KLyBDnci8vG1x-Bla9xdswrJMuhaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علی ربیعی: تخریب پزشکیان و قالیباف در این مقطع، فقط یک خطای سیاسی نیست؛ انحراف جهت مبارزه از دشمن متجاوز به داخل کشور است
دستیار امور اجتماعی رئیس جمهور:
🔹
امروز هرکس مدیران درگیرِ مقاومت، معیشت و دیپلماسی را هدف می‌گیرد، آگاهانه یا ناآگاهانه همان انسجامی را می‌زند که دشمن نتوانست در میدان بشکند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/669611" target="_blank">📅 00:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669610">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY1L6ceJkPU-ba94b1P2a-EDPJNQabAbpJ0Ui_YE5T4EeOJ1bOKeeqijJoTrfapBXihLsjMYXMjO0K1NZ8Euq4wfC1vWc1LF-t0_VeM533Zk8VSSXK1cIVs5jxcBcHm9R-83e3p3eRhVnpIF1c2VFpSVGeam_JCHQVwC9IP9l61e4-Nb7a8WnTiu4Q7mm3itpEQ4nZunPNROoaNcE-lnqbPiQi3BqdZw4XfCK19g6dzJ4h2j4XbQn8iwSAHPtR1wFEK6p5ff8t14R3BM_YzwU9OSLNfQArfk2HRC60-cou9iK-6K4rdNqOY8oOepSldT46VKx90Ew0g4mft6xp1PoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آقای ترامپ! روزی در برابر اراده و قضاوت ملت ایران پاسخگو خواهی بود؛ از خشم این ملت آزاده، هیچ راه گریزی برای تو نیست
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/669610" target="_blank">📅 00:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669609">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPosWiO6X3Z36Z_gwOnQDhHfgsazhYWppoZY8D7-hlMszvTAOM5vRSBfsc38yH3c8zGUjfbMoy7awLXH0_1u4HWggqibQJHfPwZcFoaynH8nqqjrdtfLM9fqBrlXL2OOdnVs-c4QQyIaQlG2d3JlgdTPNjUrI-TYVDqZslUcoeBiGZ1AtTnify6OoknnTje0v9lkcXS-IoPhMeRLb8aUJiQtn7UU5stNW9fpfS2gFkaTdDB75i-gO8DXfeoqsI9IzcjljH0ZLQPba99oiXrakOVOY6oKpApU1ICvB7Hz3pI8Z3A5qkcWnM1Yp3MGA3eEGbL6NyOeTKJ78e4y-MdvJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/669609" target="_blank">📅 00:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669608">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
بقائی: نقض تعهدات آمریکا با اقدام متقابل ایران روبه‌رو خواهد شد
🔹
سفر عراقچی به عمان با محور تنگه هرمز و ایمنی کشتیرانی انجام می‌شود. ایران بر اجرای مسئولیت‌های خود در تأمین ایمنی تردد دریایی در تنگه هرمز مصمم است.
🔹
همکاری ایران و عمان برای تسهیل تردد ایمن کشتی‌ها در تنگه هرمز ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/669608" target="_blank">📅 23:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669607">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eaca53d8f.mp4?token=j6pnz2ESbcIMWiYPrlYitRPVOmhY2FImfD_iGXTVdzSj8x3OyhE1-ej5_IwtrE3VAOz99jGuN3f7uvNh0tciM6aUJRFQXwpj0j7QMtYAc5E-lkvKpg7QCRvwAj_xSV6Aja9RJrR71BsUJfrkJBRX9yeCf_n0bEjoVbIfInUXQ26mBdionPNjO6TcVSrPP1UairmqxIEb8zYcTkWJvBdMXKfLkOCwsCnxEGd-qTvkfPOqtWDs361CMcrDGJw0UqqI6r7aX5Yoo7zSDPV93khh9VIE0rHdBlzHnNGuD-fA7KUnlbzaqlLMT3wwETzBfbR9dNFm7RXmLF8j3hZx1o2VBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eaca53d8f.mp4?token=j6pnz2ESbcIMWiYPrlYitRPVOmhY2FImfD_iGXTVdzSj8x3OyhE1-ej5_IwtrE3VAOz99jGuN3f7uvNh0tciM6aUJRFQXwpj0j7QMtYAc5E-lkvKpg7QCRvwAj_xSV6Aja9RJrR71BsUJfrkJBRX9yeCf_n0bEjoVbIfInUXQ26mBdionPNjO6TcVSrPP1UairmqxIEb8zYcTkWJvBdMXKfLkOCwsCnxEGd-qTvkfPOqtWDs361CMcrDGJw0UqqI6r7aX5Yoo7zSDPV93khh9VIE0rHdBlzHnNGuD-fA7KUnlbzaqlLMT3wwETzBfbR9dNFm7RXmLF8j3hZx1o2VBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ایران اجازه بازرسی از تاسیسات آسیب دیده ناشی از حملات آمریکا و رژیم صهیونیستی را نمی‌دهد و قطعنامه ۲۲۳۱ عملا وجاهت حقوقی ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/669607" target="_blank">📅 23:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669606">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a959e28379.mp4?token=IJqwOdZBh2WixCWIJscXkIqv2HWy--deKfJBwEoJhWDGvRpJopLU_EqPaSRQJS7UhFjyPgJXtacDMaCn71WcWtPzFJZJOh3EoyJWyKBxMG06LAKkFLi9D5cmMiWdLrl062JuLkIGr_o56wsNegunQN6U2FQ4BkXDfOJhYoM6-5gYb1xot1uYRTDnBIVf_15FQ-acH5BI7Zb3xzsqU1qYB54SHeYasCXqmAQUP1Md3MLBLPmZ-GXhkDTPCThmgNTsBHmo3LyPXzhwcjkcOdn0yRNAluBM9WRGpk51DLnC-p8bd-pyTg0LkzGMcufN9km5hlxekMyeE5zw1z6gOoX3Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a959e28379.mp4?token=IJqwOdZBh2WixCWIJscXkIqv2HWy--deKfJBwEoJhWDGvRpJopLU_EqPaSRQJS7UhFjyPgJXtacDMaCn71WcWtPzFJZJOh3EoyJWyKBxMG06LAKkFLi9D5cmMiWdLrl062JuLkIGr_o56wsNegunQN6U2FQ4BkXDfOJhYoM6-5gYb1xot1uYRTDnBIVf_15FQ-acH5BI7Zb3xzsqU1qYB54SHeYasCXqmAQUP1Md3MLBLPmZ-GXhkDTPCThmgNTsBHmo3LyPXzhwcjkcOdn0yRNAluBM9WRGpk51DLnC-p8bd-pyTg0LkzGMcufN9km5hlxekMyeE5zw1z6gOoX3Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ما هیچ درخواستی برای مذاکره با آمریکا نداشتیم اما سفر میانجی را به ایران پذیرفتیم
سخنگوی وزارت خارجه:
🔹
پیمان‌شکنی آمریکا یک عادت است؛ با خودشان هم لجاجت می‌کنند. آمریکا چند بند یادداشت تفاهم را نقض کرد.
🔹
آمریکا تفاهم‌نامه را نقض کرده و ما هیچ تعهدی را بدون مابه‌ ازا اجرا نمی‌کنیم. رویکرد ما تعهد در برابر تعهد است. اگر طرف مقابل تعهداتش را نقض متقابلا ایران همان کار را انجام خواهد داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/669606" target="_blank">📅 23:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669605">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ادعای خبرنگار الجزیره: احتمال برگزاری دیداری بین ایران و آمریکا وجود دارد که مکان آن ممکن است ژنو، اسلام‌آباد یا دوحه باشد
🔹
برگزاری این دیدار منوط به موفقیت میانجی‌ها و توافق بر سر فعال‌سازی باقی‌ ماندهٔ مفاد تفاهم‌نامه است؛ پروندهٔ تنگهٔ هرمز نیز ممکن است به این دیدار موکول شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/669605" target="_blank">📅 23:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669604">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d9d9fc2bf.mp4?token=k7u5BDvaKHwkJ4C0Vkjf0DUeIF2kghQJ1Qv2sxJwI_UnQAl5_qpOcRoo7k5XA85q96Wmue6t3_ETfICaHgGRI-nN521uMfNyFY6uLkuH3gtb7kNRnNyM7QGHwWNtZggZKIEEx1eioNPw3dQACryLRe9PNDED5NYCj8ecttkhHU-DIgFyZO7GeCa5q4sz3Nm20PpOqkwx3UdLjQcl_YffoK9fc0glNg46j8Zu7hwa4HJwu8AMIHwB664SnYIKWtSsIUt1hG0RVn_mSu1MD0ZUQcGNTnL58QQeXdLGtegf0Tqk3MVipmCyq28AOhNBGD7cP4I9s36ohRb3J8dDXjg9jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d9d9fc2bf.mp4?token=k7u5BDvaKHwkJ4C0Vkjf0DUeIF2kghQJ1Qv2sxJwI_UnQAl5_qpOcRoo7k5XA85q96Wmue6t3_ETfICaHgGRI-nN521uMfNyFY6uLkuH3gtb7kNRnNyM7QGHwWNtZggZKIEEx1eioNPw3dQACryLRe9PNDED5NYCj8ecttkhHU-DIgFyZO7GeCa5q4sz3Nm20PpOqkwx3UdLjQcl_YffoK9fc0glNg46j8Zu7hwa4HJwu8AMIHwB664SnYIKWtSsIUt1hG0RVn_mSu1MD0ZUQcGNTnL58QQeXdLGtegf0Tqk3MVipmCyq28AOhNBGD7cP4I9s36ohRb3J8dDXjg9jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در سال ۲۰۱۹ جز جوکرهای عراقی مخالف ایران بود و اکنون برای امام شهید اشک میریزد و صحبت‌های شنیدنی دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/669604" target="_blank">📅 23:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669603">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
دولت وابسته به ریاض در یمن: از ایران به شورای امنیت شکایت می‌کنیم
🔹
عبدالله العلیمی، عضو تشکیلات موسوم به «شورای ریاستی یمن» که توسط دولت سعودی تشکیل شده است، شکست محاصره یمن توسط هواپیمای ماهان را «نقض حاکمیت» یمن توصیف کرد و گفت که شورای ریاستی این موضوع را در شورای امنیت سازمان ملل مطرح خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/669603" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669602">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c645673a2.mp4?token=VLb090RC8MhYF09sbhVo-4NLslQhFIy4GHag6iU_NUHnP17TWbQabwqKLmY8mlE8TfXQAcE8YVd900b12bUdveDzm424KhIVT915K_AUm3q15I6k9jlh5OrZf_93AMbfim6kulVBGpwm024qnGtzZMfP2IN3fR8C1seisPA4CaBm57NxK93Hzj8a9amOVopPKvo5h04ckSxEKOu3BCdHyMpRlbwuoNhT7SADviDt2LNTJRa8Fnt1G_vmi3X3xTK-XYnCHny0Yy6u-KQ0OshIVoy3G48EmWfYSPMBUpzOaLinMv4zLHkTNS0UpauyJtQOwDa1sA3CcSRD5FZBaH8nLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c645673a2.mp4?token=VLb090RC8MhYF09sbhVo-4NLslQhFIy4GHag6iU_NUHnP17TWbQabwqKLmY8mlE8TfXQAcE8YVd900b12bUdveDzm424KhIVT915K_AUm3q15I6k9jlh5OrZf_93AMbfim6kulVBGpwm024qnGtzZMfP2IN3fR8C1seisPA4CaBm57NxK93Hzj8a9amOVopPKvo5h04ckSxEKOu3BCdHyMpRlbwuoNhT7SADviDt2LNTJRa8Fnt1G_vmi3X3xTK-XYnCHny0Yy6u-KQ0OshIVoy3G48EmWfYSPMBUpzOaLinMv4zLHkTNS0UpauyJtQOwDa1sA3CcSRD5FZBaH8nLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازگشت مردان آهنین به تلویزیون با یک سورپرایز
🔹
سری جدید مسابقات مردان آهنین با اجرای آیدین ختایی که از شرکت کنندگان قدیمی این برنامه است و حضور فرامرز خودنگاه، رضا قرایی و محراب فاطمی به زودی از شبکه سه پخش می‌شود
🔹
مردان آهنین هر شب ساعت ۲۰ از شبکه سه پخش می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/669602" target="_blank">📅 23:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669601">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993c03098e.mp4?token=nlCbxjaTYZIaRRa4cuSXlPTIxyAHm5mQLmDxbtt1VAbmHENDL8TuQFMQTvVWmBecyqAke6B23gakBFqTvfiu2aGNbtEUk8jv9EbWXcltXag2WHpTzY3cQ6ktWJN3NiW2tbbTgLiYOx-a1UTdx-sMy6oR2_CKE8ToTFMeoD0F6d4UjInbv2C_Pgh1AnVu3Ga1rgGy2rBkuzt3WXl4IzO5IrVSaubByAlRP0oEU4Tay_xAGZeHXB613QawjtLEpdeWNncgZekS-CVpCnfUz-xZRXKhvh84q2rNrxnRKqh5CM5aNGi1qrvDWqR9nlKXVzDKbLERGzTV_f6smZcMyaImkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993c03098e.mp4?token=nlCbxjaTYZIaRRa4cuSXlPTIxyAHm5mQLmDxbtt1VAbmHENDL8TuQFMQTvVWmBecyqAke6B23gakBFqTvfiu2aGNbtEUk8jv9EbWXcltXag2WHpTzY3cQ6ktWJN3NiW2tbbTgLiYOx-a1UTdx-sMy6oR2_CKE8ToTFMeoD0F6d4UjInbv2C_Pgh1AnVu3Ga1rgGy2rBkuzt3WXl4IzO5IrVSaubByAlRP0oEU4Tay_xAGZeHXB613QawjtLEpdeWNncgZekS-CVpCnfUz-xZRXKhvh84q2rNrxnRKqh5CM5aNGi1qrvDWqR9nlKXVzDKbLERGzTV_f6smZcMyaImkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در پتروپالایشگاه پلدختر
🔹
عصر امروز حادثه آتش‌سوزی در یک مینی‌پالایشگاه در پلدختر رخ داد؛ به‌دلیل ماهیت مواد اشتعال‌زا و گستردگی حریق، عملیات مهار با دشواری مواجه شده و نیروهای امدادی و آتش‌نشانی با وجود استقرار در محل، به‌دلیل شدت شعله‌ها…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/669601" target="_blank">📅 23:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669600">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca181b0c6.mp4?token=SrPtQEklICtcuyFf3y1q-9hR8nU_GzRxe6kn8QjH3K-ANkwCmFwd3DTCVo9KgP6JL421cI2rq4qCvVskVgpOaPvwgEXdWVGh96veTLLY9qEtnL5qoE0hNq3pvwPRlkp3ABa3N-Sf0SyRbxaw81RegjLvEXqI2FL3Nsv121UmaYpnUGFpEJtNGFQdF76raa7fFHvRPSx_yclyu7yq1trlaglmIs27REqZGlKK48cXpNo0vDesf8rSYBIF7nK9D1BY0Xcwb0tHx2MLglXJLVaCoKJwLeC3YZYNpGOMrjdTv4QaSNDXPMcnIGzJW5n9SBFx7Xmb3MyNTDaeSZHsUI23gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca181b0c6.mp4?token=SrPtQEklICtcuyFf3y1q-9hR8nU_GzRxe6kn8QjH3K-ANkwCmFwd3DTCVo9KgP6JL421cI2rq4qCvVskVgpOaPvwgEXdWVGh96veTLLY9qEtnL5qoE0hNq3pvwPRlkp3ABa3N-Sf0SyRbxaw81RegjLvEXqI2FL3Nsv121UmaYpnUGFpEJtNGFQdF76raa7fFHvRPSx_yclyu7yq1trlaglmIs27REqZGlKK48cXpNo0vDesf8rSYBIF7nK9D1BY0Xcwb0tHx2MLglXJLVaCoKJwLeC3YZYNpGOMrjdTv4QaSNDXPMcnIGzJW5n9SBFx7Xmb3MyNTDaeSZHsUI23gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اسپانیا بالاخره گل خورد
؛ گل اول بلژیک به اسپانیا توسط دکتلاره در دقیقه ۴۱
🇪🇸
1️⃣
🏆
1️⃣
🇧🇪
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/669600" target="_blank">📅 23:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669599">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6c6e5b928.mp4?token=cZhYZuKs1oRE_osybQekcIW_lF_M1Q7Zhz_wqGx4BUcZEThWo-rowcGk_obalxDi_oiFAvv8n5FAmqmTeREaxIi9lkWBqRDrNQVJ-cIrhf8ol__0Sr1t6XfRb_rvNNzAyF_LJo1_WXTrF_dvCFOp6WAPx4e-gu-aFn-2rFtv7kRIW-yPDH4h1WLxSNbZhyGvjf3LERg3u5CbAk6hf_71Ve_HnZv7Cx4y-Fv5zFR8ULMzl0uYhCicF96X5yUEHDp2sYoZjR6K6Yc5d2hYij-90Wa5mThINRYP8jvAtb8eD7VRH8dWpuCAGK5pcJEsDGPG5lZzfmKuhtkewiyeoDZUAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6c6e5b928.mp4?token=cZhYZuKs1oRE_osybQekcIW_lF_M1Q7Zhz_wqGx4BUcZEThWo-rowcGk_obalxDi_oiFAvv8n5FAmqmTeREaxIi9lkWBqRDrNQVJ-cIrhf8ol__0Sr1t6XfRb_rvNNzAyF_LJo1_WXTrF_dvCFOp6WAPx4e-gu-aFn-2rFtv7kRIW-yPDH4h1WLxSNbZhyGvjf3LERg3u5CbAk6hf_71Ve_HnZv7Cx4y-Fv5zFR8ULMzl0uYhCicF96X5yUEHDp2sYoZjR6K6Yc5d2hYij-90Wa5mThINRYP8jvAtb8eD7VRH8dWpuCAGK5pcJEsDGPG5lZzfmKuhtkewiyeoDZUAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پست جدید عمو فیتیله‌ای: بازی از لحظه‌ای شروع میشه که دیالوگ تموم میشه
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/669599" target="_blank">📅 23:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669598">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a51b25b24c.mp4?token=quQF0OpHy3HKixcl2oTwHFqNTiz2fKmghHmF-xbpO8QHdIS1f8keEodrvZVUPgSZRfzwSyEzBqU2TfAp2uMq-SamvmwJTe4d4IMZFzu9FORTG0prQj9O4HpWeNFc-AU0vyIDpG9qJw4prDyLch1pU7FDc2muYg6U_COZp7NJsXbkoo50tEZJAj_Cox4xzV9zP1JgYn2K3DlRIe9XvA10QfbZFTpe1MwOs-VBUuMWjn25C0ePvdgAIU6_nf9WngwuMWz4Gf_bEQhdAH52otRyd_Ti0jdXHBABEotKiy1WMR0kcMw0QXiho3tiwwMf0uC9hWlEupXbcFZGWepzrjv2zKYVWSs4QkSMqHPTjZQkljdTzeU31SjG-WDU322oublKlIaLgTae1OghR570kFqsfjX76A8p9qbcuyufuULVRQEalL-meROG-JDUmqSxHQ9gKPLs_o_OgumjyJL3ZC14Ow2_obeZtPhmFhMLSSbVi6KlUEmwR65S974QqoIA1sZonIVEH8s9P-Okj1GjeUdR4eV7f6YKft_64qbzAAUJ6n1JsPPEa0xjVrymvCvS50r5a5YqZB1KR0KOy2e62C9pg9dzje8TZ9YNJ23f9u425YyRKGLIF1IU5vL9_lvDbUK3Z4R4zIz1upz34x_NR-lGUSqUWFcAA5zo7mvM5XZGyes" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a51b25b24c.mp4?token=quQF0OpHy3HKixcl2oTwHFqNTiz2fKmghHmF-xbpO8QHdIS1f8keEodrvZVUPgSZRfzwSyEzBqU2TfAp2uMq-SamvmwJTe4d4IMZFzu9FORTG0prQj9O4HpWeNFc-AU0vyIDpG9qJw4prDyLch1pU7FDc2muYg6U_COZp7NJsXbkoo50tEZJAj_Cox4xzV9zP1JgYn2K3DlRIe9XvA10QfbZFTpe1MwOs-VBUuMWjn25C0ePvdgAIU6_nf9WngwuMWz4Gf_bEQhdAH52otRyd_Ti0jdXHBABEotKiy1WMR0kcMw0QXiho3tiwwMf0uC9hWlEupXbcFZGWepzrjv2zKYVWSs4QkSMqHPTjZQkljdTzeU31SjG-WDU322oublKlIaLgTae1OghR570kFqsfjX76A8p9qbcuyufuULVRQEalL-meROG-JDUmqSxHQ9gKPLs_o_OgumjyJL3ZC14Ow2_obeZtPhmFhMLSSbVi6KlUEmwR65S974QqoIA1sZonIVEH8s9P-Okj1GjeUdR4eV7f6YKft_64qbzAAUJ6n1JsPPEa0xjVrymvCvS50r5a5YqZB1KR0KOy2e62C9pg9dzje8TZ9YNJ23f9u425YyRKGLIF1IU5vL9_lvDbUK3Z4R4zIz1upz34x_NR-lGUSqUWFcAA5zo7mvM5XZGyes" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز فصل دوم «سرآشپز»/ ادامه رقابت بزرگ آشپزی در شبکه سه
🔹
پس از استقبال مخاطبان از فصل نخست مسابقه تلویزیونی «سرآشپز»، فصل دوم این برنامه به زودی روی آنتن می‌رود.
🔹
این مسابقه با محوریت رقابت آشپزان و نمایش مهارت، خلاقیت و فرهنگ غذایی ایرانی تولید شده است.
🔹
سرآشپز در حالی آماده بازگشت به آنتن می‌شود که موفقیت فصل نخست و استقبال مخاطبان، زمینه‌ساز ادامه این رقابت تلویزیونی شده و انتظار می‌رود فصل جدید نیز با همان رویکرد سرگرم‌کننده و رقابتی، مورد توجه علاقه‌مندان قرار گیرد.
🔹
این برنامه از شنبه پس از اخبار ساعت ۲۲ از شبکه سه پخش می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/669598" target="_blank">📅 23:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669597">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
رییس دانشگاه علوم پزشکی مشهد: هیچ حادثه منجر به فوت در مراسم تشییع رهبر شهید رخ نداد
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/669597" target="_blank">📅 23:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669596">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50cfe83713.mp4?token=ub96Cic6SYtHBDyKm1QE4EYsLoTtF2cxT_3Vh_OeVtQOU9sXxcD3g3QgzGBA-OVpyiZcfZXVQYsxv4Xo9Xd507sshPxRBJtZnXsrRrrF5-6eEupd5F7SQR2ppnDiss2gLeGTOiDJMqXEn-t3TKGhXFMG0ciaXJY0cIx5x_VkKwZ5yNONoxcxKSjnGx0zw8vtV06rdwYElznzsCzPLGw3chY3FgPPTKDWcMa7EIuMsK8OxAbUCXxHWp4lwY76RdLQbmOzV7q-GDzjUzMbC8OW-bhLNPnbspjWU3NhyTtXeh4KEsg8R39xgEy12OZ2MgAcyG5KiAY6p2kT5sQ1xaGtsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50cfe83713.mp4?token=ub96Cic6SYtHBDyKm1QE4EYsLoTtF2cxT_3Vh_OeVtQOU9sXxcD3g3QgzGBA-OVpyiZcfZXVQYsxv4Xo9Xd507sshPxRBJtZnXsrRrrF5-6eEupd5F7SQR2ppnDiss2gLeGTOiDJMqXEn-t3TKGhXFMG0ciaXJY0cIx5x_VkKwZ5yNONoxcxKSjnGx0zw8vtV06rdwYElznzsCzPLGw3chY3FgPPTKDWcMa7EIuMsK8OxAbUCXxHWp4lwY76RdLQbmOzV7q-GDzjUzMbC8OW-bhLNPnbspjWU3NhyTtXeh4KEsg8R39xgEy12OZ2MgAcyG5KiAY6p2kT5sQ1xaGtsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول اسپانیا به بلژیک توسط روئیس
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/669596" target="_blank">📅 23:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669595">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2efc7721ca.mp4?token=CWJMkH9pqi0MbNnn5XfS_N1NmHBxhuYwrb9QhDPSekzh6634X7JnBi_sED6o6ncmyS_5km8AlqJOuTAWPvwsIAhYH3XM9A6JIL_DKKv3tWBif0kTlTzD9GoPwdsupKrIO8OhMNLfS8FZewd7yegDqPKWxa1IyiXJHZ9b3QGgVqC484j3e--wZVA1M8xX7vy8m-seIXPqLDIY1YOqaLru_p2a8ojAi9p2Ai1TcPemb6a2GQOSqXNOqflQbqu2_9LcDMJbB_FyH_JLdYM2JFjVsFp66rcToKmMBcEHouQBK30mBZdSYWZi61vm76wrFmwKbP-je1e17Lq9BBhcPuBo9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2efc7721ca.mp4?token=CWJMkH9pqi0MbNnn5XfS_N1NmHBxhuYwrb9QhDPSekzh6634X7JnBi_sED6o6ncmyS_5km8AlqJOuTAWPvwsIAhYH3XM9A6JIL_DKKv3tWBif0kTlTzD9GoPwdsupKrIO8OhMNLfS8FZewd7yegDqPKWxa1IyiXJHZ9b3QGgVqC484j3e--wZVA1M8xX7vy8m-seIXPqLDIY1YOqaLru_p2a8ojAi9p2Ai1TcPemb6a2GQOSqXNOqflQbqu2_9LcDMJbB_FyH_JLdYM2JFjVsFp66rcToKmMBcEHouQBK30mBZdSYWZi61vm76wrFmwKbP-je1e17Lq9BBhcPuBo9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جلیلی: باطل‌ترین جبهه در مقابل جبهه حق ایران ایستاده و آنچه پیروزی را رقم می‌زند تاب‌آوری یا همان صبر است
جلیلی:
🔹
جمهوریت و همراهی مردم با نظام بسیار ارزشمند است و باید در همه زمینه‌ها ارتقا پیدا کند. معیشت بدون امنیت و دفاع از ملت به دست نمی‌آید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/669595" target="_blank">📅 23:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669594">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zm5PYKl3ZHOnJT2LRagZEfNRLKPXmsuAt1dOWqr38kyLNmw0vSM5MBUP4VUlr99VyEUpkmMfu8a82Z9z5Fd1g8VgpLYOFjUUySUeSzX-NxDVQNjiglilS-o575dihvDIuoYvlEp8058ygTR_gUzaf6ChVE5K1hLwg0Ug6eSrl4Vhyj_8fPLaArs1lAQ8t2ypLez_sr5HQvQJlJarbAgxtWKYTEBIaq9jijipmus5chfykutdNfSTcHUaxb6_X_4PzeUp00nPJ7hzrzRbS1oGl4E40-cToktZ42ejw6a8-P5DZM5J6yJbjbQ5YHgSsEmE8Zh3DfR8aLgzJ5hU0bKqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده ۲۰۰ میلیون تومان صندوق طلای رز ترنج شوید
🟢
این بار، ترکیب شما می‌تواند برنده ۲۰۰ میلیون تومان صندوق طلای رز ترنج شود.
همزمان با روزهای پایانی جام جهانی، شرکت ترنج مسابقه‌ای ویژه برگزار می‌کند.
🟢
با عضویت در کانال تلگرام ترنج، علاوه‌بر دریافت جزئیات و اخبار این مسابقه، با تحلیل‌ها، دیدگاه‌ها و دنیای مالی از نگاه شرکت ترنج نیز بیشتر آشنا خواهید شد.
🟢
به زودی جزئیات رقابت، اطلاع‌رسانی خواهد شد.
🔗
جهت عضویت در کانال تلگرام ترنج اینجا کلیک کنید.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/669594" target="_blank">📅 23:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669593">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
حزب‌الله با مذاکره مستقیم با اسرائیل مخالفت کرد
🔹
ابراهیم الموسوی، عضو فراکسیون وفاداری به مقاومت در پارلمان لبنان، اعلام کرد حزب‌الله «توافق چارچوب» را رد می‌کند و آن را مغایر با قانون اساسی لبنان می‌داند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/669593" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669592">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCKnmhgIcXWfh-Ku00vkprN2d_1bPRlk7TBjly8blAP70fe1TUTpnh_fNb0_xmb1Ilbp_wQP-Ghmr5frNn_FullZr8WvX65Snjlbt_SCHnSBUsTFl3XDulwvBsmRDacrabIhIu2D2IjYuIXgXsoqoaRETslJhxdtylsUsmyXUnjCXU-8jXt_xKcx4bVmHe10M4WYZiaPdzkj4VZ74bEPk0PYeur054Lxbv43ck4BCGkPVwcQRbfcd-ER9Ns2tsigplXb3d5Rz_OBt6PrnKA7w99sl69_0sITyK1NwfFFzSrmfHz74By04_Wuqmp1j92DcvZRkjGRVgCPZgRJ1BlqOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کیسه‌ زباله‌های عروسی تیلور سوئیفت دونه‌ای ۲۵ دلار فروخته شدن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/669592" target="_blank">📅 22:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669591">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
جزئیات آتش‌سوزی نیروگاه تبریز؛ شایعه حمله تکذیب شد
اطلاعیه اداره‌کل مدیریت بحران استانداری آذربایجان شرقی:
🔹
به اطلاع مردم عزیز می‌رساند، حوالی ساعت ۲۱ امروز جمعه ۱۹ تیرماه ۱۴۰۵، نقطه اتصال یکی از واحد‌های نیروگاه حرارتی تبریز به شبکه برق سراسری، به خاطر مشکل فنی دچار آتش‌سوزی شده که عوامل نیروگاه تبریز، برق منطقه‌ای و آتش‌نشانی تبریز، بلافاصله در مکان مورد نظر حاضر و حریق را اطفا کرده‌ و در حال حاضر در حال لکه‌گیری هستند.
🔹
همچنین تاکید می‌شود، از لحاظ پایداری شبکه برق، هیچ مشکلی وجود ندارد و مشکل پیش آمده برای واحد مذکور، در کوتاه‌ترین زمان ممکن، رفع خواهد شد. تصریح می‌شود، شایعات مبنی بر تهاجم دشمن به نیروگاه تبریز کذب و جعلی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/669591" target="_blank">📅 22:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669590">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91e36e4e81.mp4?token=SoalG4c92pcyJPSmVsgV8uWmIqYoX3Preh425GxmECg-ii-uez7YI8H0d3X5GYCZrS9PDzEiQ-MXVGFYfVO3Y0rYA2pA5RdHLEoxb7QXij0Jnc6G81YSGH0Iz4nB1iIwlwNaQ_JolE7kB_jt6JRtTcPhbeAAV7meF5cHULMIBXOloHvDZqXasWGQdCXJhlNs6hMNIZhUPpXQlFOTPJY6uIOnZrbF5FfEF1N3K1U172h3AFybCiGRMiL8S8lW627aR3DS-xI6BjS8vMKwiOZQ0gBQLVc2gkSjnxwDGAb8lN7ySESzENToNLX_64UIAzXverStUblcb0lgTSsL2vPYpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91e36e4e81.mp4?token=SoalG4c92pcyJPSmVsgV8uWmIqYoX3Preh425GxmECg-ii-uez7YI8H0d3X5GYCZrS9PDzEiQ-MXVGFYfVO3Y0rYA2pA5RdHLEoxb7QXij0Jnc6G81YSGH0Iz4nB1iIwlwNaQ_JolE7kB_jt6JRtTcPhbeAAV7meF5cHULMIBXOloHvDZqXasWGQdCXJhlNs6hMNIZhUPpXQlFOTPJY6uIOnZrbF5FfEF1N3K1U172h3AFybCiGRMiL8S8lW627aR3DS-xI6BjS8vMKwiOZQ0gBQLVc2gkSjnxwDGAb8lN7ySESzENToNLX_64UIAzXverStUblcb0lgTSsL2vPYpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جلیلی: رهبر شهید کاری کرد که کسی نتواند مثل جنگ جهانی دوم ایران را اشغال کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/669590" target="_blank">📅 22:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669589">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
عراقچی، فردا شنبه ۲۰ تیرماه در رأس هیاتی دیپلماتیک به عمان سفر خواهد کرد
🔹
قرار است در این سفر درباره مناسبات دوجانبه و تحولات منطقه، به‌ویژه وضعیت تنگه هرمز، گفت‌وگو و تبادل نظر شود./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/669589" target="_blank">📅 22:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669588">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
گفتگوی تلفنی سران ایران و پاکستان
پزشکیان:
🔹
برخی بازیگران درصدد برهم زدن روندهای موجود و جلوگیری از استقرار آرامش در منطقه هستند. انتظار طبیعی آن است که سایر طرف‌ها نیز به تعهدات خود پایبند باشند و از اتخاذ مواضع یا اقداماتی که موجب تضعیف اعتماد و پیچیده‌تر شدن روندهای دیپلماتیک می‌شود، پرهیز کنند. احترام متقابل و التزام عملی به تعهدات، پیش‌شرط هر توافق پایدار و موفق است
شهباز شریف:
🔹
پاکستان آماده ادامه نقش‌آفرینی برای کاهش تنش‌ها و پیشبرد روندهای دیپلماتیک است. منطقه بیش از هر زمان دیگری نیازمند صلح، ثبات و همکاری است و پاکستان مصمم است در این مسیر، رایزنی‌ها و همکاری‌های خود با جمهوری اسلامی ایران را با جدیت ادامه دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/669588" target="_blank">📅 22:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669587">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDo6pfvyu9dVrJ3pEEwINTXpz276QasILlQJM5azmgmSu2ohEupSmm9FSbdMtRGbXOVAxZFU95wIhStit3pAAq9Rem9GvS5JW1BmZnSyH-TeBwfhNI-XGK4TQeET5PXQHLFXEjbA_YKWc_kkpLNbqxXJS4xNTY6U5su6U1Jh7uinoOvTfYiv-V3QtpmyyLxLq1YHV1hos9zxXCGK8QdAX4IThqEtIO17awq-Ck8PPNvx2XVc4-kNo3myTk2szulUVpVus7fj73leBw0k8_KHIc7_qjEllYLiQ88spByV1EJuVIfl-cgOoY9o7uvZYbBOpz0_n0N4u-MytOd3ujWdmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش رئیس مرکز ارتباطات آستان قدس رضوی به حواشی رخ داده پیرامون نماز رهبر شهید انقلاب در حرم رضوی
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/669587" target="_blank">📅 22:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669585">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nc86peZXjyA0aGN14uxw6tk0Au5GlWxObHfDytLpAW66bd7pOWMK42GsvyTJOGlomq6JIggeEf4DSPu926Qi9LRB4nBlIO-HaGFnk1A6-YVtrYtZoCQVcuDu4h_u-QWm3Xu4u-RaJZrni33YWOGzG_sR_K2WCFh34HuBguHKCsoXT8g5TYpDkV_nhpydLjTUyS2QfxuGz42qaOOxznMRfd_au05LEj2VizJA3_ZFGHHS_AFqL-Sl0mDSsP3Ma13ZADm8WoqVy30i9it43pq99LOJ2PVRnqmnUjxadSzc9g4gg7HyX6wjSjZuF5SdmSgSWGI7ZxfgrRwUwBWMCEmgCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار | شروع مجدد جنگ و نوسان شدید طلا
⚠️
در جنگ دوازده روزه و هم در جنگ چهل روزه طلا ریزش بسیار شدیدی را تجربه کرد
❗️
این دفعه مجدد جنگ شروع بشود آیا قیمت طلا به گرمی
1
4
میلیون می‌رسد و دوباره قمیت
ملک
شدیداً رشد می‌کند؟
تحلیل تخصصی منتشر شد!! روی لینک زیر کلیک کن و تحلیل رو ببین تا دوباره ضرر نکنی.
⬇️
⬇️
⬇️
دریافت رایگان تحلیل طلا و ملک</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/669585" target="_blank">📅 22:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669584">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
هاکان فیدان، وزیر امور خارجه ترکیه، درباره ایران: وقتی صحبت‌های ترامپ را شنیدیم، برداشت ما این بود که او واقعاً منظور این را ندارد که آتش‌بس به پایان رسیده است
🔹
فکر می‌کنم او اساساً به این اشاره داشت که در واقع یک اقدام تلافی‌جویانه در پاسخ به آنچه بین ایران و ایالات متحده در جریان بود، صورت گرفته است. به نظر من در مورد نحوه اجرای عبور از تنگه هرمز، عدم ارتباط و سوءتفاهم بین دو طرف وجود داشت. آنها نیاز به ارتباط بهتر و مکانیسم‌های بهتری برای رفع تعارض دارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/669584" target="_blank">📅 22:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669583">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xu7OVR3B8wIU2j8PBIqsWSoQm-Pts0RJF2l62WnEIxznpnfcca7lJbXj7wy7WpKlw5oKU6P7Vql_nthSyHbOXhiEUcedxX-pPxOnbcI4SwxIG5HS89d0D2lNQqQPX6hVrF1j-rcbRNopSTjytv-VMXu-PZMlCV9X1YQLotbZLj1kK7A7YVCrxpHeS2AIUIhQ-w4jOpDFYACzco5N_5-fWHoah8O2sIAXeaZ54qEsS7NLP89NaNobIRJ6QpflUBN8HxfxvxZWPcIha_Imw-uDuJ373C8qjU2SVZ2U7pv2UqiZwdhhIy19s3mP9s5rq4HVam9YmPUDXD6nMm9MrpQXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش غریب‌آبادی به نقش امارات در تجاوز آمریکا به ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/669583" target="_blank">📅 22:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669582">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
آمریکا دیدار زهران ممدانی با سفیر ایران را لغو کرد
فاکس‌نیوز:
🔹
یک مقام ارشد در دولت آمریکا گفت که زهران ممدانی شهردار نیویورک، برنامه دیدار با امیرسعید ایروانی سفیر ایران در سازمان ملل را داشت که ظاهراً وزارت امور خارجه آمریکا وارد عمل شده و این دیدار لغو شد.
🔹
این مداخله گزارش‌ شده، دومین مورد شناخته‌ شده در هفته‌های اخیر است که دولت ترامپ در مورد تماس‌های دولت ممدانی با رهبران خارجی وارد عمل می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/669582" target="_blank">📅 22:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669581">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6a3bb02e4.mp4?token=MkrV3QvwCYw1t2NSQ_OjtXqavEU6jzdSSnoUzx2WHo5_xTKSNatC7goz3XHVTIBLYfDoOjCl9-xGmFK2drUGjeFCr_Xy2u0XZO5SHmTwAgAXfdtSgpESlSqhIwG21ZodVOwWl7hpmqs0OeU2jIYchA4wewq2_mUeOcB6hYo9x5etFrK6JwCCZuE8ArMhV1E-CMJ_yVH_TfhgJC_-CqHlEvJX3DKPdU7jXmpFbnNpOT9aWrx-fEhmPVLpiWRG4_5HXi6ysiW6vATLbdTBkuuUBwDxvU3gkxvL_V83CcoJYW4YeVdfs3akfnyT48-rnCWl0zthvPs8WWqtuqELWdltEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6a3bb02e4.mp4?token=MkrV3QvwCYw1t2NSQ_OjtXqavEU6jzdSSnoUzx2WHo5_xTKSNatC7goz3XHVTIBLYfDoOjCl9-xGmFK2drUGjeFCr_Xy2u0XZO5SHmTwAgAXfdtSgpESlSqhIwG21ZodVOwWl7hpmqs0OeU2jIYchA4wewq2_mUeOcB6hYo9x5etFrK6JwCCZuE8ArMhV1E-CMJ_yVH_TfhgJC_-CqHlEvJX3DKPdU7jXmpFbnNpOT9aWrx-fEhmPVLpiWRG4_5HXi6ysiW6vATLbdTBkuuUBwDxvU3gkxvL_V83CcoJYW4YeVdfs3akfnyT48-rnCWl0zthvPs8WWqtuqELWdltEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به رهبر شهید ایران سلام / سایه سیدمجتبی مستدام
🔹
شعار ملت غیور ایران در حرم مطهر امام رضا علیه‌السلام در مراسم بزرگداشت رهبر شهید انقلاب و شهدای خانواده ایشان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/669581" target="_blank">📅 22:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669580">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acad787b0d.mp4?token=J1ybx6KUGCo_LG_nz4qy_pLPbu_qtHmuPYCHEuYBlxUElXApfvtxAqoZzYBgSupsMFKcn6Nd0DACOxIh_FYK1ieGC56EUe9MfF2eHEInFDU2Z7s_7ZwERlCw5ChgqWOYtgb5wvL-EGV3g-f5JdVZZGUgvtCsI9e151dkf3yXAFFlLrmGWibKprYT-Rr_cO8ztbzw5P8qRvtIrOz12ynmX8EpCM-HL4OZA3S-LUqXOKiL4RdMqU3R8KEy1sY_Ac6xDWPFMBGHsOM2pbNgRJKgfaYaF2-xFJ-TtbxXhnK0gN1m_beZOFBwPEndfumaOpk1SH6MSBmjZycbI4WYA2oRWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acad787b0d.mp4?token=J1ybx6KUGCo_LG_nz4qy_pLPbu_qtHmuPYCHEuYBlxUElXApfvtxAqoZzYBgSupsMFKcn6Nd0DACOxIh_FYK1ieGC56EUe9MfF2eHEInFDU2Z7s_7ZwERlCw5ChgqWOYtgb5wvL-EGV3g-f5JdVZZGUgvtCsI9e151dkf3yXAFFlLrmGWibKprYT-Rr_cO8ztbzw5P8qRvtIrOz12ynmX8EpCM-HL4OZA3S-LUqXOKiL4RdMqU3R8KEy1sY_Ac6xDWPFMBGHsOM2pbNgRJKgfaYaF2-xFJ-TtbxXhnK0gN1m_beZOFBwPEndfumaOpk1SH6MSBmjZycbI4WYA2oRWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید علی خمینی: تا وقتی که رهبری معظم انقلاب در مورد پایان تجمعات چیزی نگویند، تجمعات خیابانی ادامه خواهد داشت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/669580" target="_blank">📅 22:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669579">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
آقا، دیگه شدی همسایه امام رضا(ع)...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/669579" target="_blank">📅 22:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669578">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4255ffdaab.mp4?token=rLlxTyKrnRY-bwYYwzVVSZOi_n-WwmOZlkgiFdDffr3TWf_iJgCLbyQ79aceJlUO-LhyOLDpCTXYI4ePnIIDcuEao0ukgcxdxH90MTlh03m-7rzBRigNKby8zrkDU9GOymzmVeQmAjzcPKX_2SlUODg0SEUj7P4Fz9Ju_8sH28LCU9aZ5LcLK8G2yoVe_4JLcTvjfYwqdZUOGqWer3cRj827tPjw91yASpo2_OeWQ4olrxR2Qe2Deo-qvMf9CWZqaVMN-lu3cthZSwNzO3MixfV6G6FRS5QEmOpYSYw2EYPgJQd05ojUmFygV5hkXGKMPq0erXecHBhbYAppElT1bHiL4Sq5ACw3TLi1iDPxtzJjF-_d7cqm7c6ettqI7qk5Bk8m_H_Mm6bbXRHk2UhcElSs4R32xnI5mBSglDp_YhPP2CAqPQpMVJCJXr313EwAda0yKsmnnFy-_qufU4hVll19rBu2aLW0yPx1MzOpuh3iTP12V5cOaGBzByDxEQxUTQnAxWSul79d1ZNZnvWvC2HekBUiMLoq1gZMS3ucgz10PuWfqz9531ISod7IBqzRjxchVu88Nu4Pod85JHeeOTgBHgE0zUizLckfFM0KH2hQkQqK17BPtde6Ry-eyKitTeBRv27XX3LTTeHBTPNNFc5ohpM5DemmxVkuupPltac" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4255ffdaab.mp4?token=rLlxTyKrnRY-bwYYwzVVSZOi_n-WwmOZlkgiFdDffr3TWf_iJgCLbyQ79aceJlUO-LhyOLDpCTXYI4ePnIIDcuEao0ukgcxdxH90MTlh03m-7rzBRigNKby8zrkDU9GOymzmVeQmAjzcPKX_2SlUODg0SEUj7P4Fz9Ju_8sH28LCU9aZ5LcLK8G2yoVe_4JLcTvjfYwqdZUOGqWer3cRj827tPjw91yASpo2_OeWQ4olrxR2Qe2Deo-qvMf9CWZqaVMN-lu3cthZSwNzO3MixfV6G6FRS5QEmOpYSYw2EYPgJQd05ojUmFygV5hkXGKMPq0erXecHBhbYAppElT1bHiL4Sq5ACw3TLi1iDPxtzJjF-_d7cqm7c6ettqI7qk5Bk8m_H_Mm6bbXRHk2UhcElSs4R32xnI5mBSglDp_YhPP2CAqPQpMVJCJXr313EwAda0yKsmnnFy-_qufU4hVll19rBu2aLW0yPx1MzOpuh3iTP12V5cOaGBzByDxEQxUTQnAxWSul79d1ZNZnvWvC2HekBUiMLoq1gZMS3ucgz10PuWfqz9531ISod7IBqzRjxchVu88Nu4Pod85JHeeOTgBHgE0zUizLckfFM0KH2hQkQqK17BPtde6Ry-eyKitTeBRv27XX3LTTeHBTPNNFc5ohpM5DemmxVkuupPltac" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای منتظرانت، صدای خونخواهی‌ است...
🔹
لحظاتی از شعرخوانی حاج محمدرضا طاهری در مراسم بزرگداشت رهبر شهید انقلاب.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/669578" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669577">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
مدیریت جهادی شهرداری در ابر رویداد تشییع امام شهیدامت، جلوه‌ای از خدمت‌رسانی بی‌وقفه و تکلیف مدارانه بود
🔹
شهردار مشهد مقدس، با تقدیر از تلاش‌های مجموعه همکاران خدوم و ولایتمدار شهرداری مشهد در برگزاری باشکوه و بدون حادثه مراسم تشییع قائد شهید امت، گفت: همدلی، برنامه‌ریزی دقیق و حضور شبانه‌روزی همکاران شهرداری موجب شد بزرگ‌ترین اجتماع مردمی بدون هیچ حادثه‌ای برگزار شود و مشهد جلوه‌ای شایسته از خدمت‌رسانی در سطح ملی و بین‌المللی به نمایش بگذارد.
🔹
شهردار مشهد مقدس با قدردانی ویژه از معاون خدمات و محیط زیست شهری شهرداری مشهد و تمامی مدیران، معاونان، مدیران ستادی و مدیران عامل سازمان‌های حوزه معاونت خدمات شهری اظهار کرد: مجموعه مدیریت شهری در این دوره با وجود همه پیچیدگی‌ها و چالش‌ها، با روحیه جهادی و انقلابی خدمات ارزشمندی ارائه کرده است.
🔹
قلندر شریف افزود: سه سال و دو ماه گذشته یکی از خاص‌ترین دوره‌های مدیریت شهری بوده که با اتفاقات متعدد، بحران‌ها و شرایط پیچیده همراه شد و اوج آن، برگزاری یک ابررویداد ملی در مشهد بود.
🔹
برگزاری مراسمی بزرگ با برنامه‌ریزی دقیق و بدون حادثه
🔹
وی ادامه داد: برگزاری این اجتماع عظیم بدون حادثه افتخاری برای مجموعه مدیریت شهری است. تغییرات متعدد در محل، مسیر و نحوه برگزاری مراسم نیز با هدف افزایش ایمنی وامنیت مردم عزیزمان انجام شد و خوشبختانه برنامه‌ریزی دقیق موجب شد این ابر رویداد با آرامش و رضایت مردم به پایان برسد.
🔹
شهردار مشهد  مقدس تصریح کرد: بخش اعظم واصلی اقدامات اجرایی، خدماتی و پشتیبانی مراسم توسط شهرداری مشهد انجام شد؛ از نظافت گسترده شهری پس از حضور میلیونی مردم در خیابان امام رضا(ع) تا فضاسازی، خدمات محیط زیست شهری، حمل‌ونقل، ایمنی و پشتیبانی‌های مختلف.
🔹
قلندر شریف همچنین از تلاش کارکنان حوزه‌های خدمات شهری، فضای سبز، آتش‌نشانی، ایمنی، پشتیبانی و حمل‌ونقل قدردانی کرد و گفت: در این رویداد بسیاری از اقدامات فراتر از وظایف معمول شهرداری انجام شد و مدیریت شهری برای جلوگیری از ایجاد مشکل برای مردم وارد میدان شد.
🔹
وی با اشاره به کمک‌رسانی شهرداری به راه آهن بدنبال اقدام خصمانه دشمن اظهار کرد: در اوج فعالیت اتوبوسرانی مشهد برای جابجایی مردم عزیزمان درشهر مشهد برای عزیمت به محل مراسم تشییع ، شرایطی بوجود آمد که نیاز فوری به جابه‌جایی مسافران راه آهن ایجاد شد، بیش از ۵۰ دستگاه اتوبوس شهرداری مشهد در مدت کوتاهی برای پشتیبانی اعزام شدند تا رضایتمندی مردم حاصل شود.
🔹
شهردار مشهد مقدس تأکید کرد: برنامه‌ریزی این مراسم از ماه‌ها قبل آغاز شد و با تشکیل ستادها و کمیته‌های تخصصی در شهرداری ، وظایف تقسیم شد. در روزهای پایانی نیز مسئولیت کمیته ایمنی به شهرداری واگذار شد و این مجموعه با مدیریت دقیق، وظایف خود را به انجام رساند.
🔹
وی افزود: مشهد شهری متفاوت است و به برکت وجود امام رضا(ع)، هم زائران، هم مجاوران و هم خادمان این شهر مورد عنایت قرار دارند و امیدواریم خدمتگزاران شهر امام رضا(ع) همواره در مسیر خدمت به مردم موفق و سربلند باشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/669577" target="_blank">📅 22:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669576">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b90fcdbbf.mp4?token=RtMs4A0977zC95yNPWtIR5pR7C5jLub91b9SefIrNZFB6H9e6LA6Vu7vntjBhgFzxtYG9g8LyrFQj2MZJuK2lY-XsTPcDtkJQog_v2CGLojLAiTePBykaT9jMqDrJWa4GNV3uLbnDfqreX_ElUZoAQ1PQMSdV0o_ew8-tfqG9iFPoyzStVq-k-6VDjEU25GUAI3ffd7WFnJ7b-A3cIOL4LBWZpCosCp5AtJ94-Sjm5Gn4_mVVoNnOha18Du5YT_j51sATnzsNZ3lPZuOHhHZ7r34WZGR36JBy4vrlvqcj0nFUu81la-N0fcPCBSeOtDBuKfZQtDacxZKZ5YgwqWyng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b90fcdbbf.mp4?token=RtMs4A0977zC95yNPWtIR5pR7C5jLub91b9SefIrNZFB6H9e6LA6Vu7vntjBhgFzxtYG9g8LyrFQj2MZJuK2lY-XsTPcDtkJQog_v2CGLojLAiTePBykaT9jMqDrJWa4GNV3uLbnDfqreX_ElUZoAQ1PQMSdV0o_ew8-tfqG9iFPoyzStVq-k-6VDjEU25GUAI3ffd7WFnJ7b-A3cIOL4LBWZpCosCp5AtJ94-Sjm5Gn4_mVVoNnOha18Du5YT_j51sATnzsNZ3lPZuOHhHZ7r34WZGR36JBy4vrlvqcj0nFUu81la-N0fcPCBSeOtDBuKfZQtDacxZKZ5YgwqWyng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید علی خمینی: هرکس بخواهد مذاکره کند برای اینکه با آمریکا به صلح برسد او خائن است
🔹
هرکس پیام دوستی به آمریکا بفرستد دهانش خبیث و نجس است.
🔹
مشکل ما با آمریکا از زمان کودتای ۲۸ مرداد آغاز شد و الان ما با آمریکا پدرکشتگی پیدا کرده‌ایم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/669576" target="_blank">📅 22:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669575">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeff1717a9.mp4?token=SPeFG2OZq-_Cfg2fGxXK_MxHrW0RXu7csYImTUAunTCUcnT4SzWW1Iqx_8uRHLLRQTIejIhMz4pxr0_xGn5rDB59h7JpimqhKkPScRJG2dk1ZoqaHsBPSnsFq_3Yb9_XBouTRlii0-P1GzYd8zeqj2m95wjOPkXNeNwqlOUai5S7j7qEPije8jXDUxh04bHJ-PPzvTvv38zP8zA-1pWzIjZNKFpbgJ9utvuEG6R1Gg78gV44wNT3VfqROBGHYMvhFoJ8jD5RBoFstrGPb7VcVs4U02Swe79hmBASYyf3EQD_xjji4uDJOBJPHm-eo2OQh-ryPMPs5QL7UW62Bvc9VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeff1717a9.mp4?token=SPeFG2OZq-_Cfg2fGxXK_MxHrW0RXu7csYImTUAunTCUcnT4SzWW1Iqx_8uRHLLRQTIejIhMz4pxr0_xGn5rDB59h7JpimqhKkPScRJG2dk1ZoqaHsBPSnsFq_3Yb9_XBouTRlii0-P1GzYd8zeqj2m95wjOPkXNeNwqlOUai5S7j7qEPije8jXDUxh04bHJ-PPzvTvv38zP8zA-1pWzIjZNKFpbgJ9utvuEG6R1Gg78gV44wNT3VfqROBGHYMvhFoJ8jD5RBoFstrGPb7VcVs4U02Swe79hmBASYyf3EQD_xjji4uDJOBJPHm-eo2OQh-ryPMPs5QL7UW62Bvc9VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید علی خمینی: هرکس بخواهد مذاکره کند برای اینکه با آمریکا به صلح برسد او خائن است
🔹
هرکس پیام دوستی به آمریکا بفرستد دهانش خبیث و نجس است.
🔹
مشکل ما با آمریکا از زمان کودتای ۲۸ مرداد آغاز شد و الان ما با آمریکا پدرکشتگی پیدا کرده‌ایم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/669575" target="_blank">📅 22:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669574">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65a1e19470.mp4?token=U0sGYlg38D8HOLihdcIm6jeMcbjW4I-HPtnH0axG0_SAxFT0rZzKesbh-CcI9T6X907dTKBCNx01lflQuqMQORHY93gIuQ-UyiEQz2hrVyGAsEM8chT8J7ZPYu8W0ej0TrCbfDwQysMuKN0FPk3KQZzw8LfAlChZnvh9iXMrqUtQXM7NZ6fxYTyTly4vv3vZz05BX-8m-s9w004dus5vIpJ-8rXsUAhdPOBNMrSfnoqlIEK331-JFSQ2ZWvr-ajsQPndyJeulqjGD6NASM_YHeoSiAPDruRvgIeNAxa3-3qSpAe8TOaPxanfXV3TJA0mYzKeL2v4zkv8cn7U4IKkaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65a1e19470.mp4?token=U0sGYlg38D8HOLihdcIm6jeMcbjW4I-HPtnH0axG0_SAxFT0rZzKesbh-CcI9T6X907dTKBCNx01lflQuqMQORHY93gIuQ-UyiEQz2hrVyGAsEM8chT8J7ZPYu8W0ej0TrCbfDwQysMuKN0FPk3KQZzw8LfAlChZnvh9iXMrqUtQXM7NZ6fxYTyTly4vv3vZz05BX-8m-s9w004dus5vIpJ-8rXsUAhdPOBNMrSfnoqlIEK331-JFSQ2ZWvr-ajsQPndyJeulqjGD6NASM_YHeoSiAPDruRvgIeNAxa3-3qSpAe8TOaPxanfXV3TJA0mYzKeL2v4zkv8cn7U4IKkaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید علی خمینی: هویت ما سازش‌ناپذیری با استکبار است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/669574" target="_blank">📅 22:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669573">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
آمریکا تحریم‌های جدیدی علیه ایران اعمال کرد
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا:
🔹
اسامی ۸ فرد و ۶ شرکت را در فهرست تحریم‌های مرتبط با ایران قرار داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/669573" target="_blank">📅 22:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669572">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
تلاش‌های دیپلماتیک؛ رایزنی چهارجانبه و سفر وزیر کشور پاکستان به تهران
ادعای الحدث به نقل ازمنابع آگاه:
🔹
برنامه‌ریزی‌ها برای برگزاری یک تماس تلفنی چهارجانبه میان ایران، آمریکا، پاکستان و قطر در روزهای آینده خبر می‌دهند.
🔹
همچنین شنیده‌ها حاکی از آن است که وزیر کشور پاکستان به‌زودی به تهران سفر خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/669572" target="_blank">📅 22:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669571">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f74c2f8d34.mp4?token=Cm9_66N059UFypTkFvoVQST-4368cggKl7Ch1w8yPauhv3l54R4Y90FGNEeNwhF6i2u-zwAQqqvUtzlsJRbA3ARDyot9lsMUh4JIgyPyf5Q0XqPpYvHawxCmLgfbSv1YwWRpsqnqL6L8eevgmP7g2mOKKSx8oGrKDBbPyrRfCcEfWVtkLZyxTMydDJj-W8wKuXkdWgXzpCgYGPqFAgQf9Z4GKfl8lR4NBU8fQPpa5_kTS0mr_UL74KTa7mqperfF3E9uaGIi4KGDJjFa6tdXM-Cv0agIUdGVCAYDZ7b4-RveFNyshJxg3rty6JCpIivoDTTYO8ztLwDhoiZAG3aiLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f74c2f8d34.mp4?token=Cm9_66N059UFypTkFvoVQST-4368cggKl7Ch1w8yPauhv3l54R4Y90FGNEeNwhF6i2u-zwAQqqvUtzlsJRbA3ARDyot9lsMUh4JIgyPyf5Q0XqPpYvHawxCmLgfbSv1YwWRpsqnqL6L8eevgmP7g2mOKKSx8oGrKDBbPyrRfCcEfWVtkLZyxTMydDJj-W8wKuXkdWgXzpCgYGPqFAgQf9Z4GKfl8lR4NBU8fQPpa5_kTS0mr_UL74KTa7mqperfF3E9uaGIi4KGDJjFa6tdXM-Cv0agIUdGVCAYDZ7b4-RveFNyshJxg3rty6JCpIivoDTTYO8ztLwDhoiZAG3aiLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید علی خمینی: کسانی‌که از جنگ می‌ترسیدند فهمیدند که جنگ هزینه و مشکل دارد اما ترس ندارد؛ ترس از جنگ بدتر از خود جنگ است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/669571" target="_blank">📅 21:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669570">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در پتروپالایشگاه پلدختر
🔹
عصر امروز حادثه آتش‌سوزی در یک مینی‌پالایشگاه در پلدختر رخ داد؛ به‌دلیل ماهیت مواد اشتعال‌زا و گستردگی حریق، عملیات مهار با دشواری مواجه شده و نیروهای امدادی و آتش‌نشانی با وجود استقرار در محل، به‌دلیل شدت شعله‌ها امکان نزدیک‌شدن به کانون اصلی را ندارند و تمرکز فعلی بر جلوگیری از گسترش آتش است.
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/669570" target="_blank">📅 21:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669568">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7efaa83718.mp4?token=NxnJFfY-_lIzM-9WnoK9p9hnv3uWOkeJMbiBaQsJpsnKEKtKMbiIJ3DLVuXO0JyLooZL-NXk4ZO4VtYmX0Kg1AYuyBqyJVBB5j449H_HPfwLb-95Ecsx0-xS6bnmOZCLV7JLAwaaVb0aUeFipiwi7eF8DDfDYNnrNzFLiSbwadASPvO6xhuL6vVRLqUrERTc6k_PGYHVNTJ5rt7D3HNG_LMwx3DqjwfrgHNxMW0ojIcP6ncEDo2Nnc_R6s6GrnT43yr4e_K6xwv3PE4ieSqXLkyryhonQEA6SUaps6v8UHsgEmHT_Qdh6Jn6P7Z1Bim4dVRf9pdpjYBGQNdRdmRE2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7efaa83718.mp4?token=NxnJFfY-_lIzM-9WnoK9p9hnv3uWOkeJMbiBaQsJpsnKEKtKMbiIJ3DLVuXO0JyLooZL-NXk4ZO4VtYmX0Kg1AYuyBqyJVBB5j449H_HPfwLb-95Ecsx0-xS6bnmOZCLV7JLAwaaVb0aUeFipiwi7eF8DDfDYNnrNzFLiSbwadASPvO6xhuL6vVRLqUrERTc6k_PGYHVNTJ5rt7D3HNG_LMwx3DqjwfrgHNxMW0ojIcP6ncEDo2Nnc_R6s6GrnT43yr4e_K6xwv3PE4ieSqXLkyryhonQEA6SUaps6v8UHsgEmHT_Qdh6Jn6P7Z1Bim4dVRf9pdpjYBGQNdRdmRE2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما مدعیان صف اخر هستیم
از اول مجلس امام‌مان را چیدند...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/669568" target="_blank">📅 21:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669567">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46d096a489.mp4?token=vlpGnLOdDl-budcddYYN1UUXUZ9ttMEXY1kSB8uenuEvJKlXICPnalhNDpXAOs1muzTyYXT2vjgGZFOUsAZs9loV_-xfhe1LLsmz8D9W7MYsIosIebysS1ni7-rmKKnk9kmCvnEndd2yhW2u7CiKuF8WhEaLOD1E5eH8QZHKhuBLjN-Y6raPmE9Mxu8yMRtmicL-sMXhO_DB9ZnRTFzXQnj9rJwK3eOKgORCW6GY5q8PPxHZAxy6gEE06Ck1NsxzjtHRSedTThMn5HcKGqwwfX6HYp_Gf8UKBhP1hx6u5tj_POgjWGjiVuj8GWJ3PBOTxMdWnNiI1_lZspdpDwRTig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46d096a489.mp4?token=vlpGnLOdDl-budcddYYN1UUXUZ9ttMEXY1kSB8uenuEvJKlXICPnalhNDpXAOs1muzTyYXT2vjgGZFOUsAZs9loV_-xfhe1LLsmz8D9W7MYsIosIebysS1ni7-rmKKnk9kmCvnEndd2yhW2u7CiKuF8WhEaLOD1E5eH8QZHKhuBLjN-Y6raPmE9Mxu8yMRtmicL-sMXhO_DB9ZnRTFzXQnj9rJwK3eOKgORCW6GY5q8PPxHZAxy6gEE06Ck1NsxzjtHRSedTThMn5HcKGqwwfX6HYp_Gf8UKBhP1hx6u5tj_POgjWGjiVuj8GWJ3PBOTxMdWnNiI1_lZspdpDwRTig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید علی خمینی: گفتنِ احمق به ترامپ، فحش نیست؛ این صفت اوست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/669567" target="_blank">📅 21:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669566">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b01cee5cd0.mp4?token=hrHZAbKBudGlcSS5ufqT6k7SjM3qrWRyGDIvqXLZYA8MbNlOtksnjtdp-E0NE-MiJ2ScfUrC7M-F4PpsxaEMnyQSqCfyiewTQ4yLr0CvUkPJXfjedYbDk3Tlnf6-GY5QHu_re2aSu20KzgnjCBHDQlDAj9KHlWLc6t5wV_QGiIph_lmTA9uyKDuejBZxFfUICt-_MwMHkMCM8NJRomR2pbxS-bj3837nsWO8pMXHEvDlSuOg1mXD3Ex7zGk8PU3qc-fKNkEEvSpYWrnHMZtroZtRFONyHkpsxV4AHFX0TBVmfmM_nAzJh8P5hXuFY_hTUYuFZaGGyGYFfoaoWObxHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b01cee5cd0.mp4?token=hrHZAbKBudGlcSS5ufqT6k7SjM3qrWRyGDIvqXLZYA8MbNlOtksnjtdp-E0NE-MiJ2ScfUrC7M-F4PpsxaEMnyQSqCfyiewTQ4yLr0CvUkPJXfjedYbDk3Tlnf6-GY5QHu_re2aSu20KzgnjCBHDQlDAj9KHlWLc6t5wV_QGiIph_lmTA9uyKDuejBZxFfUICt-_MwMHkMCM8NJRomR2pbxS-bj3837nsWO8pMXHEvDlSuOg1mXD3Ex7zGk8PU3qc-fKNkEEvSpYWrnHMZtroZtRFONyHkpsxV4AHFX0TBVmfmM_nAzJh8P5hXuFY_hTUYuFZaGGyGYFfoaoWObxHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرآن‌شناسی و تاریخ‌شناسی؛ از خصوصیات رهبر شهید انقلاب
🔹
لحظاتی از سخنرانی حجت‌الاسلام والمسلمین ناصر رفیعی در مراسم بزرگداشت امام مجاهد شهید و شهدای خانواده ایشان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/669566" target="_blank">📅 21:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669565">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e59948529.mp4?token=MsMENoGSwEWJ7idLUaeboamQHzYF-7Xm8PYdGhMBe6PJMC9i9j4tFs70iH6JomFuyIhG6LU08NMd0fbXdZY-f0r6K5_E08WKuBqyk4B2yXTtDYMnwW61DNt6oGx-pBwr3grOPkDU3niN_kCSjcJobGjEDgKk7vd0YsL-HqQK8qUvlkkcFSJm-RrzmZOXye0lQuJhBvbsRdshc2t0EK5D5C4fjUuVUv8u2-vFmy2YXnejRg-MrEzqp8v2TuaPaOX8tCgWEmQG3xAeTrE5bz_qU45LhpHFXLioaEzNvF8QCiCsNrNvYN3zLfPA9hgfpSvCEYPGYvw-arl_gdU3mJX3Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e59948529.mp4?token=MsMENoGSwEWJ7idLUaeboamQHzYF-7Xm8PYdGhMBe6PJMC9i9j4tFs70iH6JomFuyIhG6LU08NMd0fbXdZY-f0r6K5_E08WKuBqyk4B2yXTtDYMnwW61DNt6oGx-pBwr3grOPkDU3niN_kCSjcJobGjEDgKk7vd0YsL-HqQK8qUvlkkcFSJm-RrzmZOXye0lQuJhBvbsRdshc2t0EK5D5C4fjUuVUv8u2-vFmy2YXnejRg-MrEzqp8v2TuaPaOX8tCgWEmQG3xAeTrE5bz_qU45LhpHFXLioaEzNvF8QCiCsNrNvYN3zLfPA9hgfpSvCEYPGYvw-arl_gdU3mJX3Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید علی خمینی: آن مسئولی که بخوابد و در فکر انتقام رهبر شهید نباشد، باید به وجدان خودش شک کند #تقاص_خواهید_داد  #WillPayThePrice #خونخواهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/669565" target="_blank">📅 21:37 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
