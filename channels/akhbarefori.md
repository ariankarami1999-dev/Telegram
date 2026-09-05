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
<img src="https://cdn4.telesco.pe/file/MwFTyyjH0Nl7IleWE3JkE1Nw6GCSCwsrt3WLeGIpKV4MtrxrxRhrMU-xrnNI2L-DzgUOvfJgoh1FXJVncpIU4FTqBXhZN-OAJs2tczfMEKnx9Y_zGhxfvSzkR3Zwf5v7fliZ1_fUHvhgiZCitYWfLL8FmDcJ7kwmkgGw7Ey22XdbAXHtYBlo1YrpuPvnFEH2ppOH57s38TuM0ZbUmApfhzuGHhCLXiy_B7qPNE9wqzB7jcHuoYg8vNtQyMhcztB8UPbDq08VgkWb68X5sE82Pe3iewz4mL57DH8bBVE7cDDKqgyN_oodlVpp9JSsZBoXZsH_io1I0gBmNYsKxSyyvg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.43M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 10:30:28</div>
<hr>

<div class="tg-post" id="msg-687340">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
حاوی تصاویر دلخراش| ویدیویی وحشتناک از یک تصادف!
🔹
هنگام عبور از حاشیه خیابان بسیار دقت کنید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/687340" target="_blank">📅 10:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687339">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مدیریت بحران استانداری اصفهان: صدای انفجار جنوب اصفهان؛ انهدام مهمات عمل‌نکرده است.
🔹
رئیس قوه قضائیه: از اعضای بریکس می‌خواهیم در کنار قانون بایستند.
🔹
انفجارهای مهیب صهیونیستی، «زوطر الشرقیه» در جنوب لبنان را به لرزه درآورد.
🇮🇷
‌
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/akhbarefori/687339" target="_blank">📅 10:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687338">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ماجرای ۱۴ سکه مهریه؛ پابند الکترونیکی جایگزین حبس می‌شود؟
عاطفه حاذق، وکیل دادگستری:
🔹
مهریه ۱۴ سکه نشده است؛ بلکه کاهش عدد ۱۱۰ به ۱۴ سکه، مربوط به ضمانت اجرای قانونی و شرایط حبس است.
🔹
به گفته او، مهریه همان مبلغ درج‌شده در عقدنامه است و زن همچنان می‌تواند تمام آن را مطالبه کند؛ ۱۴ سکه فقط به بحث ضمانت اجرای قانونی مربوط می‌شود.
🇮🇷
‌
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/akhbarefori/687338" target="_blank">📅 10:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687337">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e280b2a3f.mp4?token=jAyTeJsMHJSnFec264sBs_MqnlTM093yABZOED1x82GWtlVWkedZqu-w5cGVHgYVh_SbHsxJ4iLG9j2CJQnRnY4ZPEq7Or0AmgmccM8U59RrODAXWKf2Y-B_-ODHXW_wXrRRFVYHcIkdcRrTFAM7S0Ks_285fvWL2RUtJDciukb1B8JxZ3pTXHLvQ4p1mbB4vj8-EVCUpn8ltaKA4XqOEi4Md6bBK5M4eoIkd1u6w-QQNSeuSF4Yd2ihu3Cy-0Ds9IX4QkUKEjj4eghS1w-wnUprcvNfiErIbBeNDSazi5A0BSSk2Tck0WChfDk3FtC63wJpc_GkxDw3ji3WpRIT0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e280b2a3f.mp4?token=jAyTeJsMHJSnFec264sBs_MqnlTM093yABZOED1x82GWtlVWkedZqu-w5cGVHgYVh_SbHsxJ4iLG9j2CJQnRnY4ZPEq7Or0AmgmccM8U59RrODAXWKf2Y-B_-ODHXW_wXrRRFVYHcIkdcRrTFAM7S0Ks_285fvWL2RUtJDciukb1B8JxZ3pTXHLvQ4p1mbB4vj8-EVCUpn8ltaKA4XqOEi4Md6bBK5M4eoIkd1u6w-QQNSeuSF4Yd2ihu3Cy-0Ds9IX4QkUKEjj4eghS1w-wnUprcvNfiErIbBeNDSazi5A0BSSk2Tck0WChfDk3FtC63wJpc_GkxDw3ji3WpRIT0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین بازی ویدیویی جهان! ساخته شده در سال ۱۹۵۴
🕹
🇮🇷
‌
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/akhbarefori/687337" target="_blank">📅 10:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687336">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
رسانه آمریکایی ام اس ناو: درخواست نظامیان آمریکایی برای خروج از ارتش در اعتراض به جنگ با ایران ۶ برابر شده است
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/687336" target="_blank">📅 10:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687335">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
نفتکش ایرانی در جزیره خارک هدف حمله موشکی آمریکا قرار گرفت
🔹
بنابر گزارش منابع محلی یک نفتکش ایرانی در جزیره خارک هدف موشک نیروهای آمریکایی قرار گرفته است./ خبرگزاری‌دانشجو
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/687335" target="_blank">📅 10:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687334">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbd885974.mp4?token=u2kfAwoOISlMqc2LibIHhNr0_JI2Rs-WreIqRcIVQwLaMbhyHAMzz319Ctsz0Gs9Ay1kX_0B9nYt4r2r7qALKqLbG_QPaHa_2aIQIwhEL_sdJfEvB2w21OiYhXvlH6zfNKcATj93OWLfhunFMZHlUeOUyd1ssE7B0trKsXsYumTYH6gxGJllGntyjSQglqpdf9yImnGCKBs-OnWHzq2HSmQaqEG_njbKU5wTI8vu9PvwqmMMPqcQe_p3evX5cIwuCZ_ihOhPdU5rYwrpSQ8sV2ryX-lxALhmNF1EPiIUWM4FN29F_njOnHJcIxZg3PtzzDCqNAmsU_K6NG5_4NEeRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbd885974.mp4?token=u2kfAwoOISlMqc2LibIHhNr0_JI2Rs-WreIqRcIVQwLaMbhyHAMzz319Ctsz0Gs9Ay1kX_0B9nYt4r2r7qALKqLbG_QPaHa_2aIQIwhEL_sdJfEvB2w21OiYhXvlH6zfNKcATj93OWLfhunFMZHlUeOUyd1ssE7B0trKsXsYumTYH6gxGJllGntyjSQglqpdf9yImnGCKBs-OnWHzq2HSmQaqEG_njbKU5wTI8vu9PvwqmMMPqcQe_p3evX5cIwuCZ_ihOhPdU5rYwrpSQ8sV2ryX-lxALhmNF1EPiIUWM4FN29F_njOnHJcIxZg3PtzzDCqNAmsU_K6NG5_4NEeRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوتلاچ یک دسر ترکیه‌ای خیلی پرطرفدار و خوشمزه مناسب برای صبحانه یا میان‌وعده
😍
مواد لازم:
🔹
برنج نیم دانه ۱ لیوان
🔹
شیر ۱/۵ لیتر
🔹
آب ۱ لیتر
🔹
شکر ۲۰۰ گرم
🔹
وانیل ۱ قاشق چای‌خوری
🔹
زرده تخم مرغ ۲ عدد
🔹
نشاسته ذرت ۲۵ گرم #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/687334" target="_blank">📅 10:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687333">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b50a317b.mp4?token=GHF7rfNgX_MALevzM0mRL5ST7_RVVbLk47AH52CmEk8-7DBDNvG_q73uld3Uxw868gc9VLCyJAZWYmaKcHjJWLFMxeLdU9uwBXsQntvIqLfAE8N3kOvU7o54L84u1-YfUEAjEHC86gn7c52eoNSVoSTUaFcabnzuIUm1mhx2OFXykbaJC5DTZXLRkgkyvIQKW_Au06y3h2MYZO5sQga46NMHStNFmEH3PBaD2zkh-M0f7s-wZ45ug2zULT92_tcUjRIwZTFgIbEuC2o2DHMgBVpELQGjgK-b73lQEwxihTBq5p2r6fyyKSUCYCp0q1UNt6_zIrwTVFEybvUe90mWyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b50a317b.mp4?token=GHF7rfNgX_MALevzM0mRL5ST7_RVVbLk47AH52CmEk8-7DBDNvG_q73uld3Uxw868gc9VLCyJAZWYmaKcHjJWLFMxeLdU9uwBXsQntvIqLfAE8N3kOvU7o54L84u1-YfUEAjEHC86gn7c52eoNSVoSTUaFcabnzuIUm1mhx2OFXykbaJC5DTZXLRkgkyvIQKW_Au06y3h2MYZO5sQga46NMHStNFmEH3PBaD2zkh-M0f7s-wZ45ug2zULT92_tcUjRIwZTFgIbEuC2o2DHMgBVpELQGjgK-b73lQEwxihTBq5p2r6fyyKSUCYCp0q1UNt6_zIrwTVFEybvUe90mWyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡
𝟲𝟬% و %𝟳𝟬 تخفیف تمامی کالاها
در جشنواره پایان تابستان «چرم مَنطِـ»
➕
𝟮 میلیون تومان هدیه اسنپ‌پی
با کد: 𝐏𝐀𝐘𝐂𝐖𝐆𝐙𝟓
در تمامی شعب و سایت
👇
🌐
manteofficial.com
با اسنپ‌پی بخر، 𝐁𝐌𝐖 ببر</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/687333" target="_blank">📅 10:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687332">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره 02191551808 در ارتباط باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/687332" target="_blank">📅 09:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687331">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
چراغ سبز آمریکا به فروش میلیاردی تجهیزات نظامی به عربستان، عمان و عراق
🔹
منابع رسانه‌ای گزارش دادند که آمریکا با مجموعه‌ای از قراردادهای تسلیحاتی با عربستان سعودی، عمان و عراق به ارزش بیش از ۶ میلیارد دلار موافقت کرده است.
🇮🇷
‌
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/687331" target="_blank">📅 09:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687330">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
نفتکش ایرانی در جزیره خارک هدف حمله موشکی آمریکا قرار گرفت
🔹
بنابر گزارش منابع محلی یک نفتکش ایرانی در جزیره خارک هدف موشک نیروهای آمریکایی قرار گرفته است./ خبرگزاری‌دانشجو
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/687330" target="_blank">📅 09:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687329">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130280e12c.mp4?token=JwB3JBojn3jHjrrivUIb5to1TjdBLSEx0aNMHiTjvS4tnmSD11CjA-1NDuS2iwRQY4OZgUl6LZ_tszraNd-h0QNLqOOUFxemIDvEUjxR4AbtBQ6_BlQ7bGYmCj3GqQG5y-CBxj38KzLher1bIOPubSKK7e9t0HZzxygyr8Zk7cBQPxHG0X3ahoEr3L6FllbxhfEg9e8bKK_UaGPhoWqY6YxFCafl_EIU1R9ILVNHBXOaeFRdnvCX0vvIXlUPjkcI4WOFdnZM7ZgLNAwgTKsz7YX0x5VbpzIPxX7158iPrQr7iqBLqog-p0TbLMCVO23X8tcwauXbCDBL1C7tvZdPiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130280e12c.mp4?token=JwB3JBojn3jHjrrivUIb5to1TjdBLSEx0aNMHiTjvS4tnmSD11CjA-1NDuS2iwRQY4OZgUl6LZ_tszraNd-h0QNLqOOUFxemIDvEUjxR4AbtBQ6_BlQ7bGYmCj3GqQG5y-CBxj38KzLher1bIOPubSKK7e9t0HZzxygyr8Zk7cBQPxHG0X3ahoEr3L6FllbxhfEg9e8bKK_UaGPhoWqY6YxFCafl_EIU1R9ILVNHBXOaeFRdnvCX0vvIXlUPjkcI4WOFdnZM7ZgLNAwgTKsz7YX0x5VbpzIPxX7158iPrQr7iqBLqog-p0TbLMCVO23X8tcwauXbCDBL1C7tvZdPiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسکله بندرگز؛ قاب تماشایی خلیج گرگان
#اخبارفوری_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/687329" target="_blank">📅 09:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687328">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
عرضۀ واکسن آنفلوانزا اوایل مهر
سازمان غذا و دارو:
🔹
با وجود تأخیر تولیدکنندگان خارجی، افزایش قیمت و مشکلات نقل‌وانتقال مالی و حمل‌ونقل، واکسن آنفلوانزا از اواخر شهریور و اوایل مهر در دسترس قرار خواهد گرفت.
🇮🇷
‌
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/687328" target="_blank">📅 09:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687327">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f22774836.mp4?token=Y0tgvfezHh6DwBByOCWhZjcPlj5hwPwDtjHlJIJA7DEFJ3JUg2C44riBYyEZRWbNSWqwkjF-0OGSi-FlxdGn2bghP611CoQgWlDWK-sRStR9QAYcObCjxVXwkWUfo5U29vYIrvinEcJ7Sc-p_jzUpqiUa3QVCtvpVMOOJhkSO0p589pVhgaOWjXr2Oh4c7EWBey0yMAa1hufYlD6BRMUw-eM3GDTp8pjVWm1EAy9OcUUYwcLTlnP3Ozf-Eu5qmLhvm97IqHEJa6scawaoINaoEyt1vG6K3J3wEKaF-sfFgOxSPwyyn_K_jb9bQnRNEZnjqtJIbqF8byacEgzupWW3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f22774836.mp4?token=Y0tgvfezHh6DwBByOCWhZjcPlj5hwPwDtjHlJIJA7DEFJ3JUg2C44riBYyEZRWbNSWqwkjF-0OGSi-FlxdGn2bghP611CoQgWlDWK-sRStR9QAYcObCjxVXwkWUfo5U29vYIrvinEcJ7Sc-p_jzUpqiUa3QVCtvpVMOOJhkSO0p589pVhgaOWjXr2Oh4c7EWBey0yMAa1hufYlD6BRMUw-eM3GDTp8pjVWm1EAy9OcUUYwcLTlnP3Ozf-Eu5qmLhvm97IqHEJa6scawaoINaoEyt1vG6K3J3wEKaF-sfFgOxSPwyyn_K_jb9bQnRNEZnjqtJIbqF8byacEgzupWW3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر شهید انقلاب: همه بدانند بنده تا نفس میکشم، اجازه نخواهم داد که بیگانگان با مصالح ایران بازی کنند/ من هم که نباشم، هرکس دیگری در این مسئولیت باشد، همینطور خواهد بود/ تا اصل نورانی ولایت فقیه در قانون اساسی هست، نخواهند توانست بنای مستحکم نظام را متزلزل کنند
🔹
انتشار به مناسبت ساعت ۰۹:۴۰ صبح شنبه؛ ساعت شهادت حضرت آیت‌الله العظمی سیدعلی خامنه‌ای رضوان‌الله‌علیه
🇮🇷
‌
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/687327" target="_blank">📅 09:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687326">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0znptqbaPKlxqsThNIBlDYXfgKK4hur-E-DsHbX7ySKnNkC4PaBY2PigJDfzjC1B8nXoYHUE6H4BjTpbDJqZlotHB35q6SSCfC7OdU2N3u2GBw9_egjF1qvHittYJ58AMQWdgystL3Oi4H-nq1YnVUe4OwFiliPRuvhomzhE2VUka8lRQtav3XvICvz40KFXK96zwJP4Uyh9nIgMyoqCQRA57boA2DCEh-BxL7TyeqzcjWt4fQHX5w8KKSX_H3zWswOxbnIhu2evXUTUn01hQiArl7m5QXksXS0aq4vMkch9mIPqeVauDiJgzESWeVFc9YuSe7xcboLV2P7LkyJIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مراقب اکانت‌های بدل تلگرام باشید؛ دام فیشینگ در یک پیام
🔹
هشدار درباره شگرد جدید کلاهبرداری در تلگرام؛ هکرها با اکانت‌های مشابه و استفاده از حروف غیرانگلیسی مثل
g
، کاربران را به صفحات فیشینگ یا فایل‌های مخرب هدایت می‌کنند.
🔹
پیش از کلیک، یوزرنیم فرستنده را با دقت بررسی کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/687326" target="_blank">📅 09:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687325">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAri4dnOsswnkYuzBnYJBRfpraFoi390qJjd56_EfJr4Ch7_MFYZv6IyzAftP8YXzElOBApcProjapcpnnLPYwTtyzyHm_VIg57SCxG1sIBbuWUm-hxa7pjIjfQvDUK8xcQjh-q20v4-tTYiE2ExyMHjrFwVfZf5DT1nICROVzQ0dvcjlobDDTtIthRsmRe7xnZltz12hyZG2K4v75BUkkQ9_EVDoDyWtXoVEv_m2N1gZ86pgfMI-2PxjXX_wyy4QvxZ9krkuAFup-w54h4uWsQeD8qT8UYQcJ3EiIuC9xoKJXD7IujyHKVJwGGnPqzAsH3uFByfM6f3MVcc6XVumw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/687325" target="_blank">📅 09:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687324">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsWASrxK-HCxCAlbmxsaf-fRkS9CnRIU2LAMtou1xT0miv2RxHLDVYPd-tBVknZNdqSfdJkgs7BcARZOFVBLLFnQoO-PSNzlM4uGLP_aXXSUo7xi6hPpIBwNaWf-Bn784IhXQZBQ8__WpyhSBzEh7E-Uk33UxgyGGryI9LHu0ur9kE-dKkgokfVVL-0B9O3FbGlTNjLZLjInZWgGlsviAgxHPHS2dBGRRC1fSxN7IA3t-w6uk_jInhQOUckpnyOZGotvWgJ4CbWLOPknsSFzvjtMOIxMSZX2FLGOU87A_fGMX0y-WAx5dFUGHGKMrT1J5rblkll86cKdjRQLaJ9YYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد ۱۲۰ هزار واحدی شاخص بورس تهران
🔹
شاخص کل بورس تهران ۱۲۰ هزار واحد رشد  و به تراز ۶ میلیون و ۶۲۴ هزار واحد صعود کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/687324" target="_blank">📅 09:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687323">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06634bb837.mp4?token=kUBbru0q6KzrTY8Zpipl56hbfpwdMgOAd_jHj9RIidyg6UQaUlZJhK5A0hrQ0cOfgArR1uiYFjEXqoNwa8Az984UJusbQQIg-EErFwa7gwXxUDs-WVyWc43ARRYTvFcDQwjkndTJtkyU2VUqe98HdKbbgGA4wZPTOxROHHX1wCA4ie1NY5Q0fTCibUrnO6diQuHph0aDsokIX0v9TeyhEZ54lLBhekBRAJ3Gt58sZHXzX4swfVqAl6TwmkCCDoa7PUr984IUwR8p9O9bafXimRqr54_K-CrqZ_0P7k3gLk54e1iBODuqqQNB10jOnRNKl7geDpDBiyCydN83sSALdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06634bb837.mp4?token=kUBbru0q6KzrTY8Zpipl56hbfpwdMgOAd_jHj9RIidyg6UQaUlZJhK5A0hrQ0cOfgArR1uiYFjEXqoNwa8Az984UJusbQQIg-EErFwa7gwXxUDs-WVyWc43ARRYTvFcDQwjkndTJtkyU2VUqe98HdKbbgGA4wZPTOxROHHX1wCA4ie1NY5Q0fTCibUrnO6diQuHph0aDsokIX0v9TeyhEZ54lLBhekBRAJ3Gt58sZHXzX4swfVqAl6TwmkCCDoa7PUr984IUwR8p9O9bafXimRqr54_K-CrqZ_0P7k3gLk54e1iBODuqqQNB10jOnRNKl7geDpDBiyCydN83sSALdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلاح مخفی واشنگتن؛ از ترور سیاسی تا جنگ مواد مخدر
🔹
روایتی از جان کریاکو بازرس اسبق کمیته روابط خارجی سنا در مورد اینکه امریکایی‌ها تعمدا اجازه گسترش مواد مخدر در افغانستان را دادند تا بخش مهمی از آن به ایران و رسیه ارسال شده و جوامع این کشورها تضعیف شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/687323" target="_blank">📅 09:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687322">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55ae739fa6.mp4?token=o5U5xhC2Vf1wmkn0c2n6oDBxPVpQgsxdd68pLVtlohr0sXqFhnIBO2AHOy7qw4zuJziN5nm71NDiIr8gom-aVVy91ojvg849r6S9VkzsSL5mwjMsMfwqpgq9fOAoQuktv1sRFxuG5dZYVlmJfsaj-oZBqtxxBP9pYVzIdkrs3PLvev3E7laSGCKstVsWPpZBfOeNDm5Rx8SEj1ctwwXacI5BNm7Wqb865_h2_uHS5EIxDh2Ue9qF1C8gGakCRUPU2ptU-5SGjQ9HF7KoKN1VzbmUdepZvWMqiSFFnfEbuzR_lEk_RSuFJ8Dz5EKU5gHbWpKHSYFkutoEqDo2G5lYaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55ae739fa6.mp4?token=o5U5xhC2Vf1wmkn0c2n6oDBxPVpQgsxdd68pLVtlohr0sXqFhnIBO2AHOy7qw4zuJziN5nm71NDiIr8gom-aVVy91ojvg849r6S9VkzsSL5mwjMsMfwqpgq9fOAoQuktv1sRFxuG5dZYVlmJfsaj-oZBqtxxBP9pYVzIdkrs3PLvev3E7laSGCKstVsWPpZBfOeNDm5Rx8SEj1ctwwXacI5BNm7Wqb865_h2_uHS5EIxDh2Ue9qF1C8gGakCRUPU2ptU-5SGjQ9HF7KoKN1VzbmUdepZvWMqiSFFnfEbuzR_lEk_RSuFJ8Dz5EKU5gHbWpKHSYFkutoEqDo2G5lYaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکسی‌های هوش مصنوعی تسلا؛ بدون راننده و فرمان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/687322" target="_blank">📅 09:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687321">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
افزایش ۴۰ درصدی تقاضا برای خرید کالای دست دوم/ واردات لوازم خانگی دست‌دوم از طریق بازارچه های مرزی رونق گرفته است
🔹
جهش ۲ برابری قیمت لوازم خانگی طی یک سال اخیر، خریداران را به سمت بازار دست‌دوم سوق داده و رکود تورمی این حوزه را تشدید کرده است. فروش لوازم خانگی دست‌دوم در یک سال گذشته دست‌کم ۴۰ درصد افزایش یافته و برخی پیله‌وران بازارچه‌های مرزی نیز به واردات این کالاها از کشورهای اطراف روی آورده‌اند./ روزنامه اطلاعات
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/687321" target="_blank">📅 09:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687320">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73b3176880.mp4?token=VpXgwP73yVg29bMsoZZFNN5Qcl9yBcEFhdFNdaU7OfpT8jBbrFh7vAR4X41pI0dcAY3l4PiGkD6VP7PmGn53r_Js1W-P4diIQZOjstWedvK34NCYgdFy8GU7xqFNi0vAPNxg1sIwGMIIpf5nP6r1rTTma8Mz4rRHS6wnTLi37gO3dxt7bNCQjlk7nm5yqW5WFWEnODbZt0DhtcZRE94vTZY-m6YgvxtFGTZH1rA9enN8yHS0QE1sEWV-kSqU369_pwqGCs-J-ZC-IaQebrqab6JXYLwRd2u-1_N0TlzWXt1fEJoSOtkr0JCxbFh9r4e5kIrqWqik5kafSjZ8SFjFbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73b3176880.mp4?token=VpXgwP73yVg29bMsoZZFNN5Qcl9yBcEFhdFNdaU7OfpT8jBbrFh7vAR4X41pI0dcAY3l4PiGkD6VP7PmGn53r_Js1W-P4diIQZOjstWedvK34NCYgdFy8GU7xqFNi0vAPNxg1sIwGMIIpf5nP6r1rTTma8Mz4rRHS6wnTLi37gO3dxt7bNCQjlk7nm5yqW5WFWEnODbZt0DhtcZRE94vTZY-m6YgvxtFGTZH1rA9enN8yHS0QE1sEWV-kSqU369_pwqGCs-J-ZC-IaQebrqab6JXYLwRd2u-1_N0TlzWXt1fEJoSOtkr0JCxbFh9r4e5kIrqWqik5kafSjZ8SFjFbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس قوه قضاییه ایران در اجلاس روسای قوه قضاییه کشورهای عضو بریکس حضور پیدا کرد
🔹
حجت‌الاسلام‌والمسلمین محسنی اژه‌ای که به هند سفر کرده در روز سوم سفر خود در محل برگزار اجلاس روسای قوه قضاییه کشورهای عضو بریکس حاضر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/687320" target="_blank">📅 09:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687319">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نایب رئیس کمیسیون کشاورزی مجلس: کمبود نهاده‌های دامی نداریم
🔹
مدیرکل صنعت برق تهران: قطعی برق صنایع از سه روز به یک روز در هفته کاهش یافت؛ حذف خاموشی‌ها به‌زودی
🔹
انتخاب رشته داوطلبان آزمون کارشناسی ارشد ۱۴۰۵ دانشگاه آزاد تا ۲۰ شهریور تمدید شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/687319" target="_blank">📅 09:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687318">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
فردا کالابرگ خانوارهایی که رقم انتهای کد ملی سرپرست آنها ۰، ۱ و ۲ است و نیز خانوارهای حمایتی و نیروهای مسلح، شارژ می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/687318" target="_blank">📅 08:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687317">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
فردا کالابرگ خانوارهایی که رقم انتهای کد ملی سرپرست آنها ۰، ۱ و ۲ است و نیز خانوارهای حمایتی و نیروهای مسلح، شارژ می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/687317" target="_blank">📅 08:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687316">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ge77OwNiSflrNI5VC-peURPLVyNvZ2N-2YIckjPB4izZpIUZeLb9Jgwinqmv9XqLuIbDVNJmwxRCMKZu2cdCXTzxqhuZuxc1Vddk6YATeHXCSQbtt-9Zem14mcOx9DnB0ySnrWQ940J9gjgqWlj9Jkq1xPtl2QuEZ6dUQZK_hhqY70_J8cTz-OuG8QXtKRtFefAFkoCOvJ9i7XUc-xzY9SOpRhZ_HVInN6kSA9pQV5yinMCaTfo-1XZYSWhxJoiWeRF5_mY2YBEppnJ6PwuE_s0-xjWOjvN9kIMsxIbR5FBqcNDhOsjhSOO-TsT0Mneqxa4iRm9IU0sT87C7WTpbsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از رابرت دنیرو ۸۳ ساله در کنار دختر ۳ ساله‌اش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/687316" target="_blank">📅 08:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687315">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
انگلیس: جنگ علیه ایران اقتصاد جهانی را تحت فشار قرار داده است
وزیر دارایی انگلیس در گفت‌وگو با فایننشال تایمز:
🔹
تداوم درگیری میان آمریکا و ایران، اقتصاد ما و جهان را با چالش‌های بی‌سابقه‌ای روبرو کرده است.
🔹
آنچه در خاورمیانه در حال رخ دادن است، مستقیماً بر نرخ تورم، میزان رشد اقتصادی و هزینه‌های استقراض تأثیر منفی می‌گذارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/687315" target="_blank">📅 08:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687314">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd9d5689cd.mp4?token=Cu58DwY1rbIPOXvoZUxuxAqMgB3oozmS9Cmy8BOQENmc4ben3JKvJaxDRCCet1KH0PeD2L5LvGt75t0zbiju5ZPr7gRHP0yYGqwUZfW4WJBVXySp6KEax429b7lvI7Kl91BJK2CILhbYASDBhyBGpKKt21aiRd1yMsOw3oAjoCTL4gykljxr99GV12cNuB5XhZSnSFqa-DfulX7hp8fqszv4qKw854M5Jq8xHgpay4tobRsPuTk2sZGJZ39cFbQSPlQQW1a_TAXjjD7sVo7ncXfNODhTllFITq6nR1CJIRUOGOylknfRn2i8bty1-pp2uygbVSPaMRblAegDMp4EdJm61DhpAQ2yjQG1KlpTxbOlOMzhqr7h6lXHdJAELAyNEsxPNb6BKRWq8TntDlMXWHu__6QKbFKs1hnKWvcNSWJwHq3vzrm2I4h7_fEkU0zbgxotFUFhuA2-VHubd8E-zDbcB-laMhdFMxwPYcvfeSPE8lfBpYwFpdtNs91AaeB8j4V-UOiuTUSlYIiYS93y6dgstOSZjWz_jtLv2mcvhglC8VbVIX02ErQ-9pGPJAgeUEkDo6EtNXlbGBi_2JBK9po8C-_I0665oVZ-B7HR3DmoqlBM3dy8vbBFfob41mnPadNpeO2guTbygrbLkcdSA3JjQKdXhrm7EtA-UAKYQWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd9d5689cd.mp4?token=Cu58DwY1rbIPOXvoZUxuxAqMgB3oozmS9Cmy8BOQENmc4ben3JKvJaxDRCCet1KH0PeD2L5LvGt75t0zbiju5ZPr7gRHP0yYGqwUZfW4WJBVXySp6KEax429b7lvI7Kl91BJK2CILhbYASDBhyBGpKKt21aiRd1yMsOw3oAjoCTL4gykljxr99GV12cNuB5XhZSnSFqa-DfulX7hp8fqszv4qKw854M5Jq8xHgpay4tobRsPuTk2sZGJZ39cFbQSPlQQW1a_TAXjjD7sVo7ncXfNODhTllFITq6nR1CJIRUOGOylknfRn2i8bty1-pp2uygbVSPaMRblAegDMp4EdJm61DhpAQ2yjQG1KlpTxbOlOMzhqr7h6lXHdJAELAyNEsxPNb6BKRWq8TntDlMXWHu__6QKbFKs1hnKWvcNSWJwHq3vzrm2I4h7_fEkU0zbgxotFUFhuA2-VHubd8E-zDbcB-laMhdFMxwPYcvfeSPE8lfBpYwFpdtNs91AaeB8j4V-UOiuTUSlYIiYS93y6dgstOSZjWz_jtLv2mcvhglC8VbVIX02ErQ-9pGPJAgeUEkDo6EtNXlbGBi_2JBK9po8C-_I0665oVZ-B7HR3DmoqlBM3dy8vbBFfob41mnPadNpeO2guTbygrbLkcdSA3JjQKdXhrm7EtA-UAKYQWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک روتین حرکتی منظم می‌تونه به حمایت از سلامت تیروئید، بهبود عملکرد گوارش و کاهش بعضی علائم مرتبط با PMS کمک کنه  #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/687314" target="_blank">📅 08:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687313">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48f38265c8.mp4?token=EwAsZ9ny5djtASbzM2kC4aoN1vhGrhiiSZBzjAPg4zY7JdEFA4-Irg3NF8ejejv2nlrgLWRsa5fpoNXuIjiw4hgz7knBE_ecATAW_Y96gcSzI-KJOxpSx0GY5j2eMPWfRJb7BIZlEWHjGsxetDfmINyn-7S7EyIZep_w4UhjAuYqlTEe8JyA9nAV4irTLoesAoTJmpEnyz46xK-1W4djIDPSKyhSAjnoPe2Deux9ERy5BSngMKwk8uFljv0DP2586RtiYfvXR8H-4wB5KfoIhaw--1BM7J0lKL4ntE88yWqdmCDiJbTTGZJiEwT9RPspiOEul8tGwVZZyzLx1BN1Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48f38265c8.mp4?token=EwAsZ9ny5djtASbzM2kC4aoN1vhGrhiiSZBzjAPg4zY7JdEFA4-Irg3NF8ejejv2nlrgLWRsa5fpoNXuIjiw4hgz7knBE_ecATAW_Y96gcSzI-KJOxpSx0GY5j2eMPWfRJb7BIZlEWHjGsxetDfmINyn-7S7EyIZep_w4UhjAuYqlTEe8JyA9nAV4irTLoesAoTJmpEnyz46xK-1W4djIDPSKyhSAjnoPe2Deux9ERy5BSngMKwk8uFljv0DP2586RtiYfvXR8H-4wB5KfoIhaw--1BM7J0lKL4ntE88yWqdmCDiJbTTGZJiEwT9RPspiOEul8tGwVZZyzLx1BN1Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رانش زمین، رودخانه‌ای در نپال را مسدود کرد
🔹
رانش زمین در غرب نپال، بخشی از رودخانه چاولانی را مسدود کرده و خطر وقوع سیلاب ناگهانی در مناطق پایین‌دست را افزایش داده است. مقام‌های محلی از ساکنان خواسته‌اند در آماده‌باش باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/687313" target="_blank">📅 08:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687312">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر خارجه عمان: با وجود تهدید همیشگی جنگ، ما از میز مذاکره عقب‌نشینی نخواهیم کرد
🔹
جوی پایدار در بیشتر مناطق کشور طی ۵ روز آینده؛ رگبار و وزش باد شدید در برخی ارتفاعات.
🔹
افزایش شمار قربانیان سیل در نپال به ۱۳۴۲ نفر رسید ۴۸۹۶ نفر همچنان مفقود هستند‌.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/687312" target="_blank">📅 08:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687311">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ab3d214a.mp4?token=OCK7dTQ5_uk9Hdhny4nPCnNmiOIq3oYb2gB6SmOe4uMP_256oUPoAOoZMXHmXRSfu72mn-QojBcfBsMo_4__ehQHrw7cIDGg-V9uZz_gs_GpJxnvEkuYewE22rfcAVrVAalUC48d9jhJBk2_i5x8UwCF8HgJQXmtcI-qZDbgundi3D1bbLdF5e_zB6oqGQDPUIwjkxQuIApq5W4o7tMK63iA2Y38IjmEDRsdSEW59rDr2k_2bzKtY0-yXwrLUFBF0aKVOC27TvFEzuRJCNfZ0e5ahPFuHUl-aE0o4VhfDi1bPJY2cpu5H6PWXM5ebD8acFcFhhT1E_zS-4BFGzCIvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ab3d214a.mp4?token=OCK7dTQ5_uk9Hdhny4nPCnNmiOIq3oYb2gB6SmOe4uMP_256oUPoAOoZMXHmXRSfu72mn-QojBcfBsMo_4__ehQHrw7cIDGg-V9uZz_gs_GpJxnvEkuYewE22rfcAVrVAalUC48d9jhJBk2_i5x8UwCF8HgJQXmtcI-qZDbgundi3D1bbLdF5e_zB6oqGQDPUIwjkxQuIApq5W4o7tMK63iA2Y38IjmEDRsdSEW59rDr2k_2bzKtY0-yXwrLUFBF0aKVOC27TvFEzuRJCNfZ0e5ahPFuHUl-aE0o4VhfDi1bPJY2cpu5H6PWXM5ebD8acFcFhhT1E_zS-4BFGzCIvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از نزدیک‌ترین‌هایت شکایت نکن؛ هیچ اختلاف مالی ارزش از دست دادن خانواده را ندارد
🔹
یک وکیل روایت می‌کند که با جلوگیری از جلب برادرِ موکلش، فرصتی برای حل اختلاف مالی داد؛ چند ماه بعد، برادر فوت کرد و موکل هنگام خاکسپاری به اهمیت آن تصمیم پی برد.
🔹
توصیه او: تا جای ممکن مقابل پدر، مادر، خواهر و برادرتان نایستید؛ بعضی فرصت‌ها برای جبران دوباره برنمی‌گردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/687311" target="_blank">📅 08:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687310">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84dd2e621d.mp4?token=Am1EMsP5oz2DTL0gF_GxGUGvdYH-R20Tpxt40V59-7f4rFPB69Z3MQJa4ddM1hC1A7MaDFVDVea6UlcCwTJnS71MPBIGz8JgRDoFW4E5N7wRpfnEtOn-VZ_UaxR58elIf1Rs29dIIRGxuArLnHVWaxKyz77KAX6X0crx9wwHe7CdiiCT_fa84X9S5dEnT98yaO3RmJCG6N60SZ9TKX7ck6x9vIxrKV_Zk2wtk-fzUWvDCnlZ9Uih1MYibGL4nxJjvM_mvOEEL2XFQCx5-ycZayfFdlgHa9QPBEF1-Dkr62fbCyRsSO2tDB4c95CbYqp5edID3GrUr-VLsenQErMX-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84dd2e621d.mp4?token=Am1EMsP5oz2DTL0gF_GxGUGvdYH-R20Tpxt40V59-7f4rFPB69Z3MQJa4ddM1hC1A7MaDFVDVea6UlcCwTJnS71MPBIGz8JgRDoFW4E5N7wRpfnEtOn-VZ_UaxR58elIf1Rs29dIIRGxuArLnHVWaxKyz77KAX6X0crx9wwHe7CdiiCT_fa84X9S5dEnT98yaO3RmJCG6N60SZ9TKX7ck6x9vIxrKV_Zk2wtk-fzUWvDCnlZ9Uih1MYibGL4nxJjvM_mvOEEL2XFQCx5-ycZayfFdlgHa9QPBEF1-Dkr62fbCyRsSO2tDB4c95CbYqp5edID3GrUr-VLsenQErMX-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در پی سیل‌های ناشی از طوفان به جنوب چین، خانه‌ها زیر باران‌های سیل‌آسا تخریب می شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/687310" target="_blank">📅 07:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687309">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سرگرمی جذاب دیوید بکام با کشاورزی خانگی در عمارت ۱۲ میلیون پوندی در کاتسوولدز!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/687309" target="_blank">📅 07:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687308">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b118bed5c.mp4?token=FZB8lbgESV6jKWiLyYgMn3VvOViTX5qs1J9_p_zIpg1Ez_yOj97sYMOh6Y3DZs2-1N0VQo6j8pM3IXfs6hJbrg9MiOB0CgrqaWYH7tTm4TwXrhi1LFQdpXu5E-LReAgXrauvYBRSV0C9nw7CEnoLZqJda1LOthGU0njQtM4gbCaH8b9jjRHTqWI7s--lyXUE9FP-GCe9z49USiAML8jNzUamfpHY0DY4iLyjU-Kq0meyrSEH5YJJ7IGi-C7XrrEXq-RMN1uT8vhk_j9ZGdLqukwYXhaAGnxkWfa7r5j27kLMBjHTLl41JTbS-FqqHy4_FSQqVmhhPXujPM8-gh_JxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b118bed5c.mp4?token=FZB8lbgESV6jKWiLyYgMn3VvOViTX5qs1J9_p_zIpg1Ez_yOj97sYMOh6Y3DZs2-1N0VQo6j8pM3IXfs6hJbrg9MiOB0CgrqaWYH7tTm4TwXrhi1LFQdpXu5E-LReAgXrauvYBRSV0C9nw7CEnoLZqJda1LOthGU0njQtM4gbCaH8b9jjRHTqWI7s--lyXUE9FP-GCe9z49USiAML8jNzUamfpHY0DY4iLyjU-Kq0meyrSEH5YJJ7IGi-C7XrrEXq-RMN1uT8vhk_j9ZGdLqukwYXhaAGnxkWfa7r5j27kLMBjHTLl41JTbS-FqqHy4_FSQqVmhhPXujPM8-gh_JxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در اعتراض به قانون ممنوعیت حجاب دختران در مدارس اتریش، زنان و مردان با حجاب در اعتراضات حاضر شدند
🔹
موج اعتراض‌ها روزبه‌روز گسترده‌تر می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/687308" target="_blank">📅 07:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687307">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ناکامی اسکورت آمریکا در تنگه هرمز
🔹
نفتکش حامل گاز طبیعی مایع «الغشامیه» که تحت حمایت آمریکا در کریدور جنوبی تنگه هرمز حرکت می‌کرد، از ادامه مسیر منصرف شد و به‌جای قطر، راهی بندر فجیره امارات شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/687307" target="_blank">📅 07:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687306">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1b7553db.mp4?token=L52NBb3KGe_DpHl8ssqkvuvtS4e13t_jX_4H9QJBvf2XmBKM5RLC3-ROMivh-0jYkJsiLCU2bC3Wl1eHq0bE_wTFdacgFRd23KPRm8OQSyYcp_X0wb_3keKtjK02w8XG8kO9xdqeZQJHiWrUm2hc8cFPL41BQz-TzidsF1Gaa8Edjg9XS8KKM_jEVvONqhh2gFo_LQuKahP9m9cscP9svkioU3Xo-c5hMAqUup_-u_HgSyh2d7cPZWOon4GPBvOfHnKBbgTpXnj09nbSit7bIuN1k0UN2uaOgsU5oBqLi4LyR3Lou9sZW1U4s4BwYUZABqZ5bO_CDahB9wSZXTqycg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1b7553db.mp4?token=L52NBb3KGe_DpHl8ssqkvuvtS4e13t_jX_4H9QJBvf2XmBKM5RLC3-ROMivh-0jYkJsiLCU2bC3Wl1eHq0bE_wTFdacgFRd23KPRm8OQSyYcp_X0wb_3keKtjK02w8XG8kO9xdqeZQJHiWrUm2hc8cFPL41BQz-TzidsF1Gaa8Edjg9XS8KKM_jEVvONqhh2gFo_LQuKahP9m9cscP9svkioU3Xo-c5hMAqUup_-u_HgSyh2d7cPZWOon4GPBvOfHnKBbgTpXnj09nbSit7bIuN1k0UN2uaOgsU5oBqLi4LyR3Lou9sZW1U4s4BwYUZABqZ5bO_CDahB9wSZXTqycg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گیرافتادن چرخ‌های تانکر در آسفالت و فرونشست زمین در اصفهان
مدیریت بحران استانداری اصفهان:
🔹
شامگاه جمعه هنگام عبور یک دستگاه تانکر از خیابان شهیدان کاظمی بخشی از این خیابان فرونشست و چرخ‌های تانکر در حفرۀ ایجاد شده فرورفت.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/687306" target="_blank">📅 07:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687305">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
تحقیق در ارتش آمریکا درباره افشای اطلاعات جنگ علیه ایران
🔹
به گزارش «نیویورک‌تایمز»، مقام‌های نظامی آمریکا درباره نشت اطلاعات حساس مرتبط با جنگ علیه ایران تحقیق می‌کنند.
🔹
حدود ۵۰ عضو ستاد مشترک در این تحقیقات بررسی شده‌اند؛ محور اصلی، افشای اطلاعات درباره کاهش ذخایر مهمات حیاتی آمریکا است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/687305" target="_blank">📅 07:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687304">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqWbZYVfGQfA_4LGV8hdmHxySfnvVJTGlkOngAJjrTgNgnuVex35VGUegQxdDypyVdXQ7GPCbo7RCdfykazYvuB4Qb4RV8D6_20S2gei6H_EnLYPlRuJ4XzBEg_JulwHOxWxidaZy-3VP_kmPe-bjO-TwswfDJ50fR8pET56LnKNNlowYgjViQxCPNNQ4ihlcGIKpvAIWVot6VMroNSYt-WYbh-1awKrreYuKCWBq05KGKLh7SUDjhb2lAJa21OVlYoSGZyktI9Nmhnk78O2Ul0PizJEhCUMsd-5MHTPWTJYqRX5KqQrAewXxl-6USEbVzEOqfSnrSJ9xCzHJ98-0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۱۴ شهریور ماه
۲۳ ربیع‌الأول ‌۱۴۴۸
۵ سپتامبر ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/687304" target="_blank">📅 07:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687303">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
هیاهوی تبلیغاتی جدید وزیر خزانه‌داری آمریکا دربارۀ تحریم‌ها علیه ایران
🔹
وزیر خزانه‌داری آمریکا مدعی شد که اتحادیۀ اروپا رسما به روند «انزوای اقتصادی» علیه ایران پیوسته است.
🔹
اسکات بسنت بدون ارائه جزئیات بیشتری از این «موضع قوی و زودهنگام» قدردانی کرده…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/687303" target="_blank">📅 03:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687302">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSHFtIZa_X8ZymOjcHyST32fDWJeofpTyEVedT2wWMA7T27uuXIfeXl7db5-034xsvAWc7pZQXYa8pTNnGjway2HfI-IZ7WFT3VvZOprJuYJgZZyq5j1f-vCTQNQ0BbbfezpBGfcjIBN5eJiYjauHOc61khQwU2LnEbAU1Y9tKD-tOBLgaOFyVTSNLy0Xvm2lj9I0QmWRhIwlND39SNnK7QR9ZbfKZokr2axoHnicSN8xxmp-nN85gQoQaFF1WmQk5FokATwT3rnaLONhO4QZyCRm4hlZKOO7jdXHDM7-1TAhsepuIt1aLGDmbDTW-FTYnCz9EcQjVxolXc27XvOUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسکات ریتِر، افسر سابق اطلاعاتی آمریکایی: اگر ایرانی بودم، تأسیسات تصفیه آب شور اسرائیل را همین امروز از بین می‌بردم. اسرائیل را نابود می‌کردم
🔹
باید به موجودیت اسرائیل پایان داد. به معنای واقعی کلمه، سرطان سیاره است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/akhbarefori/687302" target="_blank">📅 01:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687301">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
آسوشیتدپرس: قیمت گازوییل در آمریکا برای نخستین بار در تاریخ به‌طور میانگین به رکورد بی‌سابقه ۵.۸۵ دلار رسید
🔹
کارشناسان نسبت به پیامدهای اقتصادی آن بر زنجیره تأمین هشدار می‌دهند. افزایش قیمت گازوییل به معنای افزایش هزینه حمل‌ونقل طیف گسترده‌ای از کالاهای روزمره است.
🔹
خریداران باید شاهد افزایش بیشتر قیمت کالاها در فروشگاه‌ها باشند.‏
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/687301" target="_blank">📅 01:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687300">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeNsHbdpuTyENaoEL572zLnVBPLWtkH9oWGPuWp3U9IbXY4z0Umb2_0XZj_pdppSjTPpFUrd7zkU3IwREiyv-x1ZD_mSbARHsBYjDQkleYgn3ScGwCnOBYIVCpRUpeQ_RMFsQQfYv8mTpZLxiwr7XesUyK1kYAsTt1jyeZp2i8YUXu7sfBl4xDgkUNJYhS6z1jApRiepgaRs6tfE6QpL4JsncRgNuUXKVRbjmjlUhle4wgCQ0JHQ4bZr8MXEbWeZV2fL97eznkbtmLM-xxwY-c-Epzcv_HHn9Zt32P6zvFuW7INDBGBmaZcEgUytyPtMS3pe1qGft2TgaqRPgE01RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
هنوز هوا سرد نشده، ولی وقت خرید کاپشنه!
🧥
کاپشن مردانه
Adidas مشکی | داخل تمام خز
💧
پارچه مموری ضدآب + خز تدی گرم و نرم
✨
کلاه‌دار، جیب‌دار و شیک
💰
الان با تخفیف، به قیمت پارسال!
📌
قبل از شروع فصل سرما بخر، چون وقتی فصلش برسه خبری از این قیمت نیست!
💰
قیمت ویژه تخفیف: فقط ۲,۱۹۸,۰۰۰ تومان!
👇
خرید:
https://memarket24.ir/product/brief/50703/180124/</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/687300" target="_blank">📅 01:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687299">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_02t3zaICeNZEeqpX2kptNAlQz_ecwKYfOwf3uCBTDFD9p_kyeCUuOFg2GhBLNrPa0R6287KEK055WzsUxw2rMn-iH9WKQfbNeAUUlum8ibvC2Qe570i7rNKEExsxTB3SWeJBVThULvq2_v94574qA9ebo3jrcfBALkyl-kVdgWhWI5idwxT176ffxEUsbBCzEkmJ7DUHORBiauF5yOclTy3T7moKBA3UDoQb5nnuA807HBL9WdHxaxy3PF-5YyTSzWGTlKwvOzEyi1PvzBgzMvJ9rUc-ggWPzcRWtiGv6ZHELDAgPhpu6FlXneF8PPUDnEMGccWycoD1knlWhZhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال آمریکایی: اگر ترامپ یک کار مثبت کرده باشد، به مردم آمریکا نشان داده اسرائیل، با وجود جمعیت ۹ میلیونی‌اش، عملاً اختیار آمریکا را دارد
🔹
ما به نتانیاهو رأی نداده‌ایم رئیس‌جمهورمان باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/687299" target="_blank">📅 01:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687298">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ادعای معاون اول ترامپ
جی‌دی ونس:
🔹
بله، قیمت بنزین در ایالات متحده بالاست، اما در همه جای دیگر جهان به مراتب بدتر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/687298" target="_blank">📅 01:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687297">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKB8qShhl02IntQiyMkILkTf_hNSWSt-GgZwtn-hh5YSftLN9QjygaV4cic8v6trcZBkxsxGqmURGicUPWCmgLcYKoMo5TJbPnH-aGtb88L7UWiydhso-pvUtDJjd7drfFNlkTwpOyYEtb4BPEqgtUVekz9ncZwdpX_qA_dzGR3KkmG_NHHg7UlpxpymykVoDciDdGWxa_hQpUfGm5BET5uuA3sd-rldCmmbMzOp_Y2J53HXRrE7bh_67lo0L7_7zNO9zjXYUdRW6QcwuQqQXG8WPmnYTloTYWKm6mgGTohIiT9VPrzUW_RpI0iP33R5tNeexzC_5kn63jXzMl4F_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: صندوق ثروت ملی ۲ تریلیون‌دلاری نروژ پیشنهاد کاهش شدید دارایی‌های خود در اوراق خزانه‌داری آمریکا را مطرح کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/687297" target="_blank">📅 01:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687295">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bfdbbddca.mp4?token=p6YC72yTtYoLMprnHofrbrFI4pVVXm-W-RAhThxcvHgbkkdNbAxjWVXjg5Ec8DmDMiRduKxnHg3cKeR1DZ2zKiAsWNsNiQMpdO1YZXCU0e_2a6o08mjhoOJKASvfFEDh-CRPW50dRl6BZjRg1biad9jgvxX0As7CzvyNPUrkRYPllMdxHrZ9m_kBsq9hgRPHZ_LyNNd-4YtXbbXyDOC4xviHOsrPnpuVOVM8h1QpBy8yyYtyyZbUDxKrKPKxAfhMTwVduoC6K2dhIc4hPD6QWYyAPePH1CzDfqT_XCTLPAacfprws2oCYLfLU0bWfGF0sUm5Cv0NqpYaIcbUuJq6WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bfdbbddca.mp4?token=p6YC72yTtYoLMprnHofrbrFI4pVVXm-W-RAhThxcvHgbkkdNbAxjWVXjg5Ec8DmDMiRduKxnHg3cKeR1DZ2zKiAsWNsNiQMpdO1YZXCU0e_2a6o08mjhoOJKASvfFEDh-CRPW50dRl6BZjRg1biad9jgvxX0As7CzvyNPUrkRYPllMdxHrZ9m_kBsq9hgRPHZ_LyNNd-4YtXbbXyDOC4xviHOsrPnpuVOVM8h1QpBy8yyYtyyZbUDxKrKPKxAfhMTwVduoC6K2dhIc4hPD6QWYyAPePH1CzDfqT_XCTLPAacfprws2oCYLfLU0bWfGF0sUm5Cv0NqpYaIcbUuJq6WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزت‌الله ضرغامی: اصولگرایان چنان از خجالت هم در می‌آیند که حاضرند یک اصلاح‌طلب پیروز شود
🔹
اصولگرایان هرچقدر که بتوانند همدیگر را نابود و تخریب می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/687295" target="_blank">📅 01:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687294">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78221dc9cd.mp4?token=Z2xwEVCERgolJkpIcgFkw9Yt9miBheGlZ7l9S8LwQa26_73zNLQQjNlPYYkvDO-lBAq4xVn995HQIXyQXBx0hu4DtLceOTfLUb8vdLVr3oMVrrG1WYNuwGbCLwiQG7jFmfJDk4GN5NpcJ4hN2a07sV8c3qSO34SxgLEEXUt2v7l8GjofvKN3AxDSwoMbNiPVS2lQCMuG0H4ExChDVqKFvD1-SsRsA4gpTUha9DXkpttcMTE9uKvul1Ecsm3eZs9IHss1FvwzJnkQpM7h-3qbNsTTr61gWeRvw4bWRRT1ub-UX5MQVcD13XIKtF9TkYUcyuDAFCCXa3HBy4vvbZikiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78221dc9cd.mp4?token=Z2xwEVCERgolJkpIcgFkw9Yt9miBheGlZ7l9S8LwQa26_73zNLQQjNlPYYkvDO-lBAq4xVn995HQIXyQXBx0hu4DtLceOTfLUb8vdLVr3oMVrrG1WYNuwGbCLwiQG7jFmfJDk4GN5NpcJ4hN2a07sV8c3qSO34SxgLEEXUt2v7l8GjofvKN3AxDSwoMbNiPVS2lQCMuG0H4ExChDVqKFvD1-SsRsA4gpTUha9DXkpttcMTE9uKvul1Ecsm3eZs9IHss1FvwzJnkQpM7h-3qbNsTTr61gWeRvw4bWRRT1ub-UX5MQVcD13XIKtF9TkYUcyuDAFCCXa3HBy4vvbZikiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش‌ها از تلفات بالا در پی حمله ناگهانی ارتش اسرائیل به یک ساختمان در شهرک الرمادیه جنوب لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/687294" target="_blank">📅 01:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687293">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur1ts_xyuC1WpZQBrkM_VubEPNNIaIbcSyjK6G62-IhPsN-l0jURstlOJV1cpPUZx5y2AcmDDifiwFVDvwtOtemn7ZXzrpBfGtQcq3ATQ0TvPyYVjrdDVrjt4qKqa8rAGNtvxsxJDK_X0_Aoe_Mjx2actlYePx_cf2NYOdLUIzErSDn_nxhOCejwQjtAgz5PczOH92wE8Kcqf78tNxzePyU78ZeVYIm15wIgobznIpxFBz7gFWwDtR0hRloZRl6EaMHiYxX0GH4bCCy36Y38cIT0QsDK1zOo-_8CVt4vWxLMIlO6sY-ryuj-T1lYOubnoNlpg1mDSges6CcaVi9geA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت «زینب عواضه» خبرنگار شبکه المنار لبنان(رسانه رسمی حزب‌الله): اعلام سیطره بر تپه علی الطاهر من را به شدت یاد اعلام سیطره بر تنگه هرمز توسط ترامپ می‌اندازد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/687293" target="_blank">📅 00:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687291">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NahMtwxnZWdC64en95DtNCHOKkPGiD0ePFL6bCVzaCE5rHjGVtWb4nGf0-h-ciBS3jxFQ5Y2ZPQLWrHEkn0jMSPTLP1hNXcFDU9nau-qPDttt7LcVBu-1_nYbrmOPOeUkHPjfPmRkMC9zYei4BaDkDf0HsbMaymN0RftBQOqVXcnP8mkaU7Zgqa0e7qea9S9fHIrXLDWdezVeAlFwyduDI6Z5Nvqy9dkt5WfjcRoGoHEXuRkCyltPx22wU8dctiHY6B0Tc4LB3VnV5amtAAXAv6Ju_8KEAeLM_w3BVPswqXJhWa_tIRqsNWmBsMx65V4wxssB0iUgKH4XQMyIivPYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: آمریکایی‌ها نباید بهای جنگ‌طلبی اسرائیل را با جان فرزندانشان بپردازند
اسماعیل بقائی سخنگوی وزارت امور خارجه در پیامی در شبکه ایکس با اشاره به مقاله منتشره در یکی از رسانه‌های اسرائیلی که در آن پیشنهاد شده است از دانشجویان بدهکار به شبکه بانکی برای سربازگیری جهت ادامه جنگ با ایران استفاده شود، نوشت:
🔹
آمریکایی‌ها، لطفا فقط یک سؤال از خودتان بپرسید: چرا باید به پسران و دختران شما وعده بخشودگی بدهی بانکی داده شود تا در ازای آن در جنگی بجنگند و کشته شوند که اسرائیل خواهان تداوم و گسترش آن است؟
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/687291" target="_blank">📅 00:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687290">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
پنتاگون از بیم ایران ردیاب‌های تبلیغاتی دستگاه‌های نظامیان را غیرفعال کرد
🔹
پنتاگون در بحبوحه نگرانی‌ها از حملات تلافی‌جویانه ایران، ردیاب‌های تبلیغاتی تلفن‌ها و رایانه‌های نیروهای آمریکایی را غیرفعال کرده است.
🔹
بر اساس گزارش‌هایی که روز جمعه منتشر شد، شاخه‌های مختلف ارتش آمریکا شناسه‌های تبلیغاتی دستگاه‌های الکترونیکی را غیرفعال کرده‌اند، زیرا نگران هستند داده‌های مربوط به موقعیت مکانی بتواند محل استقرار نیروهای آمریکایی را در اختیار ایران قرار دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/687290" target="_blank">📅 00:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687288">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCFxtooSxU1xdpFaktQcepdT_796OO8ErdUx7LOuSYEXc2ZDTRznkQT6JgEs_-5JPGYFVMBou9Jvt9GCgHRHtu5S8FtXTSowbLGsE7HpD1XFx2waHBop9bjTsfH153n-sRB0vPqE60dACpKIUwDYDtai6wa6bPNTWhS6UJ36gfFc5tgfMYsWlhted-D_QQ-6AUKj4jEECJbWUIPlYFg-yc42GAQ7MykC2SaCTzmXK2LUC7KUg_Ag2d52TDg2-ZDTfxfv3kkA4K1FxiQxmw2mxCWR0GnBQLsbqw_eFX8spYYChbtTLKqXufA4nkvGVbKfLZdCm7ZvJxAeHhdFQG7qCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/687288" target="_blank">📅 00:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687287">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7fa489704.mp4?token=spVcGH-a-o5_XlhSFRCeZyUXTOn9OCxemvml8TRxoR5bZv9oYmj9o-Y8Bo6GhTJdgg-kg91TYZ3eeksYBswAJTtToLz-R_YGQ6ayNRI9dfHZifdIG7D-ppTtYKeSESHwKEQx5e_CsJJS3tt4h5czL49JEpzAqwpo2909Ra4ZMh2FtOkNSoyUOqKFDAXaYzKiQOpUYeVWiIronJh1feJ7vv4qAWrbaxg-aqARelYffmwUXATah6rrqK5MXWAJ0ksvHV8IQAuFwGO3VsxA2V8laNpwolwbes5jUsxjQr5ZhvWq1okyxQF5nXG3ggWLryKlTq8Ztx4t73Q_CMrAZfLoZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7fa489704.mp4?token=spVcGH-a-o5_XlhSFRCeZyUXTOn9OCxemvml8TRxoR5bZv9oYmj9o-Y8Bo6GhTJdgg-kg91TYZ3eeksYBswAJTtToLz-R_YGQ6ayNRI9dfHZifdIG7D-ppTtYKeSESHwKEQx5e_CsJJS3tt4h5czL49JEpzAqwpo2909Ra4ZMh2FtOkNSoyUOqKFDAXaYzKiQOpUYeVWiIronJh1feJ7vv4qAWrbaxg-aqARelYffmwUXATah6rrqK5MXWAJ0ksvHV8IQAuFwGO3VsxA2V8laNpwolwbes5jUsxjQr5ZhvWq1okyxQF5nXG3ggWLryKlTq8Ztx4t73Q_CMrAZfLoZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی مجلس: درصورت حمله به زیرساخت‌های اقتصادی ایران، تجارت منطقه فلج می‌شود
محمدرضا محسنی‌ثانی، عضو کمیسیون امنیت ملی مجلس در گفتگو با شبکه آرتی روسیه:
🔹
مطابق طرح پیشنهادی، کنترل دائمی تنگه هرمز باید به ایران سپرده شود و در عین حال، امکان عبور و مرور را برای همه کشورها - به جز آن‌هایی که دشمن ایران تلقی می‌شوند - فراهم می‌سازد.
🔹
حمله به زیرساخت‌های اقتصادی ایران می‌تواند تجارت منطقه را فلج کرده و طناب خودکشی را به دور گردن واشنگتن تنگ‌تر کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/687287" target="_blank">📅 23:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687286">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
سوخو۳۵ با این سامانه جنگنده‌های رادارگریز را پیدا می‌کند
🔹
سوخو۳۵ برای غلبه بر این چالش، به سامانه الکترواپتیکال و جستجوگر فروسرخ پیشرفته OLS-35 مجهز شده که بدون انتشار کوچک‌ترین سیگنال راداری و کاملاً غیرفعال، امضای حرارتی اهداف هوایی را شکار می‌کند.
🔹
این سامانه با بهره‌گیری از حسگرهای حرارتی با تفکیک‌پذیری بالا، پرتوهای فروسرخ ساطع‌شده از جنگنده‌های رادارگریز را از فاصله ده‌ها کیلومتری شناسایی و قفل می‌کند. مسافت‌یاب و نشان‌گذار لیزری OLS-35 نیز قادر است تا فاصله ۲۰ کیلومتری، اطلاعات دقیق مسافت و مختصات هدف را برای سامانه‌های هدایت سلاح و کامپیوتر کنترل آتش سوخو فراهم کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/687286" target="_blank">📅 23:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687284">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JztaNUkWok0i-u6aGaZUDSQk0FG6ZdDPGtD8wcpNynErkfUsC5CbksxeiuUTa-rysI__uuqYVQ1tDaCfd3-xCMsYg4Jpf2kIviy7RG9AayBeJZnEaOT0hxIuOUwiZP0T10m0eCakxJdxUsYjvezTCoqHrLmXdAg269ZNfcE9bzd4g_aNABLhUGHrqseMidoQYXjIgHxH_32OF8uNhbL6qfbg8p3wFs2tJJbJFvlbpuYsKuM4Tp33E-i_4xH8PjoxfovgwCPgbyao5WPqDtYVpAWZW5zjXH6gxtc7UL_vnWSGSHgNiJxY0Jrvc3aZ6Vzh29QxoSppJ0cFzcV_ptZRjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پادکستر سابق کالیفرنیایی به دلیل تهدید علیه جان ترامپ بازداشت شد
وزارت دادگستری آمریکا:
🔹
نیروهای مجری قانون یک پادکستر سابق ساکن کالیفرنیا را به اتهام تهدید علیه جان رئیس‌جمهور آمریکا بازداشت کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/687284" target="_blank">📅 23:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687281">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3560fd2134.mp4?token=KjnqUat5r5Nj91qSFQzToiTPNLrIJxpb_KLOK9hM-TzvxT3ZyrG_9YefvDf5DPTIhfNNe-ZwAfybjl1hprbeDbbl4TDUSxP7We96Vndp9ILkebcifJ_VR4e4Kij4EoVgbv5Tq6mn6hGFnvZ6XKFem3f0uL6fPZ3fqNSHWTfkJkSNRDO9hNK-3mBkWCoks2pcJbmXxvIAtyFT3DJ-wl3Zc0OY85ikJuhYhT1C3WXrMjwVyPtvwvOmz3oGue6X9csaMwPxzj_-OgbkFBSavRhGOfKXC-mvV-0u1PjYl71R532jn1yJP5Py_zDUFWb6mb86EQizwQqwMJ4l6AilLkZlbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3560fd2134.mp4?token=KjnqUat5r5Nj91qSFQzToiTPNLrIJxpb_KLOK9hM-TzvxT3ZyrG_9YefvDf5DPTIhfNNe-ZwAfybjl1hprbeDbbl4TDUSxP7We96Vndp9ILkebcifJ_VR4e4Kij4EoVgbv5Tq6mn6hGFnvZ6XKFem3f0uL6fPZ3fqNSHWTfkJkSNRDO9hNK-3mBkWCoks2pcJbmXxvIAtyFT3DJ-wl3Zc0OY85ikJuhYhT1C3WXrMjwVyPtvwvOmz3oGue6X9csaMwPxzj_-OgbkFBSavRhGOfKXC-mvV-0u1PjYl71R532jn1yJP5Py_zDUFWb6mb86EQizwQqwMJ4l6AilLkZlbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«تابان فردا» یکی از ستون‌های انرژی ایران شد
/
موفقیت گروه پتروشیمی «تابان فردا» در عرضه اولیه با مشارکت ۲ میلیون و ۹ هزار نفر در بورس تهران
🔹
مهدی عبوری، مدیرعامل گروه سرمایه‌گذاری اهداف، چند روز پیش از عرضه سهام «تابان فردا» هم‌زمان با ایام هفته دولت خبر داده بود. روز ۹ شهریور، سهام «تابان فردا» عرضه شد و بیش از ۲ میلیون نفر در این عرضه مشارکت کردند.
🔹
بزرگ‌ترین عرضه اولیه تاریخ بورس ایران با تکیه بر پرتفوی بورسی حدود ۴۹۵ همت، دارایی‌های عملیاتی و زنجیره‌ای از پروژه‌های نفت، گاز و پتروشیمی برگزار شد.
🔹
«تابان فردا» دارای پروژه‌ها و مجموعه‌های متنوعی در حوزه‌های پتروشیمی، نفت و گاز است؛ مجموعه‌هایی نو و غیر مستهلک مانند پتروپالایش کنگان، دهلران و فراسکو عسلویه، همچنین «نفت جی» که یک‌پنجم (۲۰ درصد) قیر ایران را تولید می‌کند و «نفت سپاهان».
🔹
طبق برنامه شرکت، حداقل ۷۰ درصد از سود محقق‌شده میان سهام‌داران تقسیم خواهد شد. «تابان فردا» برای سال جاری سود ۲۵ همتی را محقق کرده و این رقم برای سال ۱۴۰۹ به ۳۲۱ همت خواهد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/687281" target="_blank">📅 23:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687276">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3456c18c13.mp4?token=dfEeDXUYMWZlrD65u8PbE-MttGmZ6f7mFpTUWjjvdOJ2oIa3aCqcIvQZkmmxz8YRsRC56mNeYS5TXtrowG7zai4lAd4hhqubvzhMBF5bKRICTn8gH9Q-HI0v0Vs5Qvd75bk_vBfFwzBPNC5onM_OTw8ZhuQC_-kO0Et2toOtcSwJx86AzgqPdA9QY2UANMNOVGIFwheWf0fBNiy_i-H5M0lOzFQVQ5iBXqFPsE36SU3fYYchBAvFZ7Ld5Ssc6RocLedKyC7VPIk3YDIEAaYYxgmbApXzyOlhCYRxzCbzN4K5vbTwAjE95jbBQdx1-SLOZauB0vOtZGytrOBcpnB8Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3456c18c13.mp4?token=dfEeDXUYMWZlrD65u8PbE-MttGmZ6f7mFpTUWjjvdOJ2oIa3aCqcIvQZkmmxz8YRsRC56mNeYS5TXtrowG7zai4lAd4hhqubvzhMBF5bKRICTn8gH9Q-HI0v0Vs5Qvd75bk_vBfFwzBPNC5onM_OTw8ZhuQC_-kO0Et2toOtcSwJx86AzgqPdA9QY2UANMNOVGIFwheWf0fBNiy_i-H5M0lOzFQVQ5iBXqFPsE36SU3fYYchBAvFZ7Ld5Ssc6RocLedKyC7VPIk3YDIEAaYYxgmbApXzyOlhCYRxzCbzN4K5vbTwAjE95jbBQdx1-SLOZauB0vOtZGytrOBcpnB8Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شهریور، خریدت با اسنپ‌پی BMW داره!
🚘
✨
از ۱ تا ۳۱ شهریور، با هر خرید از اسنپ‌پی، چه آنلاین، حضوری یا از شبکه‌های اجتماعی شانس برنده شدن
BMW 225L
بگیر تازه با انجام ماموریت‌ها می‌تونی شانست رو بیشتر کنی!
🔥
🎁
هر هفته به مدت ۵ هفته، ۵ برنده:
💻
مک‌بوک ایر M4 |
🪙
۵ گرم طلا |
📱
آیفون ۱۷ |
📲
گلکسی S25 FE |
🎮
PS5
با
اسنپ‌پی ۴ قسطه و تخفیف‌دار
خرید کن و شانس‌هات رو بیشتر کن.
😎
💙
https://l.snpy.ir/j5cfo
https://l.snpy.ir/j5cfo
https://l.snpy.ir/j5cfo</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/akhbarefori/687276" target="_blank">📅 23:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687275">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310606bd55.mp4?token=DYBI9cTdDIHrRC0lEG6hQtfBaWXb1n7xz2TzTCqPOZToGttIlL3E8kSOalZgH2Cu9IX4x9dWTuPVOg0oWF6yv2rONzpPXWKFLRzf3ZHPzI53y-1AdjzY1tyrjZvfT0M57odCbKixB0JfIudRVyCtVqJ942yA5boCaWsks6UzioNYiSLb2-jCntefAhpJJ1BhE9f0GoR7yLZo2CrVwy8YVJoYxl9gLNa9EdqRqLVt5MRk6LuDzaAuaux_TRZkd4DICx2qQCy1NDUhHDBTHAJTSj7HrTPntZN5QoPjsySw60VO4hWSxEHbvEeX2AQBiyVsCj4t_BRplg6M0wZhLzjUYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310606bd55.mp4?token=DYBI9cTdDIHrRC0lEG6hQtfBaWXb1n7xz2TzTCqPOZToGttIlL3E8kSOalZgH2Cu9IX4x9dWTuPVOg0oWF6yv2rONzpPXWKFLRzf3ZHPzI53y-1AdjzY1tyrjZvfT0M57odCbKixB0JfIudRVyCtVqJ942yA5boCaWsks6UzioNYiSLb2-jCntefAhpJJ1BhE9f0GoR7yLZo2CrVwy8YVJoYxl9gLNa9EdqRqLVt5MRk6LuDzaAuaux_TRZkd4DICx2qQCy1NDUhHDBTHAJTSj7HrTPntZN5QoPjsySw60VO4hWSxEHbvEeX2AQBiyVsCj4t_BRplg6M0wZhLzjUYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ  دروغگو درباره تنگه هرمز: همین حالا خطوط لوله در حال احداث هستند
🔹
مسیر جاده‌ای از طریق سوریه در حال ساخت است؛ در واقع، این مسیر باز است. مردم با کامیون‌ها از طریق سوریه عبور می‌کنند؛ کامیون‌های بسیار بزرگی که نفت حمل می‌کنند.
🔹
راه‌های جایگزین…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/687275" target="_blank">📅 22:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687274">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
نگرانی نیروی هوایی آمریکا بابت از دست دادن ده‌ها  پهپاد MQ-9 ریپر در جنگ علیه ایران
وبگاه دیفنس اسکوپ:
🔹
نیروی هوایی آمریکا روند جایگزینی پهپادهای MQ-9 ریپر را پس از تلفات جنگی در جنگ با ایران تسریع می‌کند
🔹
از دست دادن ده‌ها فروند پهپاد MQ-9A در طول جنگ با ایران، نیروی هوایی آمریکا را بر آن داشته تا برنامه‌های خود برای جایگزینی این پهپاد را بازنگری کند. مقامات اکنون به دنبال این هستند که یک جانشین ارزان‌تر را در تعداد زیاد و با سرعت بسیار بیشتری به میدان بفرستند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/akhbarefori/687274" target="_blank">📅 22:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687273">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
هشدار ایران به کره جنوبی؛ اعتبار خود را فدای آمریکا نکنید
🔹
شبکه خبری المیادین شامگاه امروز جمعه به نقل از یک مسئول بلندپایه امنیتی-سیاسی ایران گزارش داد که کره‌جنوبی نباید منافع و اعتبار خود را فدای سیاست‌های تجاوزکارانه آمریکا کند.
🔹
این مقام که اشاره‌ای به نامش نشده است: به کره‌جنوبی هشدار می‌دهیم که تهران هرگونه مشارکت این کشور علیه ایران در تنگه هرمز را به منزله مشارکت نظامی در جنگ تلقی خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/687273" target="_blank">📅 22:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687272">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار درباره ایران: من به رئیس‌جمهور شی گفتم: «لطفاً درگیر ایران نشوید»
🔹
چین واقعاً درگیر این موضوع نیست؛ دخالت چین بسیار اندک است. چین می‌تواند دخالت بسیار بیشتری داشته باشد. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/687272" target="_blank">📅 22:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687271">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ترامپ متوهم: به جنگ‌ها پایان دادم ولی به من جایزه نوبل ندادند
🔹
من به ۸ جنگ پایان دادم و هیچ اعتباری هم بابت آن نصیبم نشد. آیا جایزه نوبل را گرفتم؟ نه؛ با اینکه کسی که آن را گرفت، آن‌قدر لطف داشت که جایزه‌اش را به من تقدیم کند.
🔹
هیچ‌کس در تاریخ جایزه نوبل…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/akhbarefori/687271" target="_blank">📅 22:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687270">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b727bcb7.mp4?token=WhP1ekBWWao9ZCK3nM56qgH4c0KUBO63unULRfMFQEBIuF9DBft3Zr2CVOmTIcTebTcydbpv-bp9YSTnpnmHQHAVxw7hfFDS4IL3yBrCQLylgKdA3P27y1c_d5leJKdnRP9dLy90r1gCM1ondKZq_iY7WQVRZLRjF68jBy3sv9iNgnFnVtr3_6CC5I-CvaX0Y7kjFSOwI3E5ItpBzwDzXKbHFxwzT-58NrMiSiauaEdyGdXT0UJnW1WAjIjIClle4NvTIIaPW3DHHWvb3oO4HBQ0qO2ftdl0kPJ_OoSBY1DP4qWGqNxZ2-_3s-UFkUqJvI1VRbmHGa5hxwow6Pl2-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b727bcb7.mp4?token=WhP1ekBWWao9ZCK3nM56qgH4c0KUBO63unULRfMFQEBIuF9DBft3Zr2CVOmTIcTebTcydbpv-bp9YSTnpnmHQHAVxw7hfFDS4IL3yBrCQLylgKdA3P27y1c_d5leJKdnRP9dLy90r1gCM1ondKZq_iY7WQVRZLRjF68jBy3sv9iNgnFnVtr3_6CC5I-CvaX0Y7kjFSOwI3E5ItpBzwDzXKbHFxwzT-58NrMiSiauaEdyGdXT0UJnW1WAjIjIClle4NvTIIaPW3DHHWvb3oO4HBQ0qO2ftdl0kPJ_OoSBY1DP4qWGqNxZ2-_3s-UFkUqJvI1VRbmHGa5hxwow6Pl2-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ قمارباز: پوتین به دنبال حمله به قلمروی ناتو نیست  رئیس دولت تروریستی آمریکا:
🔹
من با پوتین صحبت می‌کنم، او را خیلی خوب می‌شناسم. پوتین به دنبال حمله به ناتو نیست. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/akhbarefori/687270" target="_blank">📅 22:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687269">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b727bcb7.mp4?token=aZ5pDWYexsEMDff1fTNuxoSY1_1HUCeLG5zoDeTNoljfhozvnP1jrb4XQRuYmM52xSfjr3FzxCGEmO3adM3WAijOdV1b3OQTt0Ba5_MV7bpRev41OHtZwpTUsjgljLpgy1O3Ii6VXQufhMHaCeXCT80J9oov41ScxnA3ceCIxTnxCM6As2fX0Yu3l8xywjbr9DxM4uE1PwrfYmtTfWwJnYCGvW4lQCnTP-NL1KDuTg58v848wcD6k5kns8Qm3WpSzxv5t5GxO5t4n0gKnv9e3_k2eZiRE2EdP8svr46lnxfaS_X65Hb1a21TjO-b5lxwOjpoYfj--9qeC5qFMAOKBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b727bcb7.mp4?token=aZ5pDWYexsEMDff1fTNuxoSY1_1HUCeLG5zoDeTNoljfhozvnP1jrb4XQRuYmM52xSfjr3FzxCGEmO3adM3WAijOdV1b3OQTt0Ba5_MV7bpRev41OHtZwpTUsjgljLpgy1O3Ii6VXQufhMHaCeXCT80J9oov41ScxnA3ceCIxTnxCM6As2fX0Yu3l8xywjbr9DxM4uE1PwrfYmtTfWwJnYCGvW4lQCnTP-NL1KDuTg58v848wcD6k5kns8Qm3WpSzxv5t5GxO5t4n0gKnv9e3_k2eZiRE2EdP8svr46lnxfaS_X65Hb1a21TjO-b5lxwOjpoYfj--9qeC5qFMAOKBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: ویتکاف و کوشنر در حال بردن پیشنهادی به مسکو برای پایان دادن به جنگ هستند #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/687269" target="_blank">📅 22:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687268">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJRpvuuWRwWWTz6RvOP_GbFSZepSK-zPkEa-ip8hPnWGOs_aroca2LDnqV_dHtHlnZUywO-2nEbQeTeT5FkazIeD_b4HfGp4OaXmwgg5megSPzsAQg5Z4m5gnhKJ0YfPbWkSmNEfgdTp1psHTcQKRpa6I9_Cc6rLkB2rtVt8j9QP17PyenYiZsH8-v7H2QSuNBbQrZdrBAHlaAP12d4Y-5GXBHf9F1Z1o4RA5KEv1K-HO1i27LWzWxpo5GVlB_74pexPyILOZpsm0PFyv4f-isUQ3MV0mOMQ093h4Sdm7rXy6l7D2crd7fLzLK-YakUdExy2cmJ6nZQskUsWGSWPwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا؛ ابر قدرت زنگ زده‌ای که کسی نباید در مورد آن حرف بزند!
‏ناو آبراهام لینکلن که قرار بود نماد قدرت دریایی آمریکا باشد، بعد از ۲۸۶ روز مأموریت با بدنه‌ای زنگ‌زده و گزارش‌هایی از شرایط سخت زندگی خدمه وارد تایلند شد. حالا گاردین گزارش داده ملوانان این ناو هم از مصاحبه با رسانه‌ها درباره شرایط آن منع شده‌اند.
به توییتر خبرفوری بپیوندید
👇
https://x.com/akhbare_fori/status/2095856638485839910?s=46</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/687268" target="_blank">📅 22:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687267">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار درباره ایران: آنها رادار نصب کردند، زیرا ما قبلاً آن را از کار انداخته بودیم. حالا ما آن را برای بار دوم از کار انداخته‌ایم، اکنون ما هیچ فعالیتی را مشاهده نمی‌کنیم #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/687267" target="_blank">📅 22:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687266">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز درباره ایران: ما همه کسانی را که در «کوه کلنگ» در حال جابه‌جایی هستند، می‌شناسیم
🔹
ما همه کسانی را که در سراسر ایران در حال جابه‌جایی هستند، می‌شناسیم و اگر اتفاق بدی بیفتد، به آنها حمله می‌کنیم؛ آن‌هم به‌شدت #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/687266" target="_blank">📅 22:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687265">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
ترامپ قمارباز مدعی شد: ممکن است به‌زودی به کوه کلنگ در ایران ضربه بزنیم #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/687265" target="_blank">📅 22:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687263">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
مدیرعامل رایتل: رقابتی با دو اپراتور دیگر نداریم/ می‌خواهیم زمین بازی را تغییر دهیم
مهدی فقیهی، مدیرعامل رایتل در
#گفتگو
با خبرفوری:
🔹
تلاش می‌کنیم زمین بازی را تغییر دهیم؛ رقابت مستقیم در بازار B2C با دو اپراتور مسلط، برای رایتل می‌تواند هزینه‌بر و دشوار باشد، بنابراین به دنبال ورود به میدان‌های جدید و خلق فرصت‌های تازه هستیم.
🔹
هدف ما این است که با هزینه کمتر و بهره‌وری بیشتر، در این میدان جدید منافع بیشتری برای سهامداران و مردم ایجاد کنیم.
🔹
با وجود تمام چالش‌های اقتصادی، وظیفه حرفه‌ای خود می‌دانیم که برای توسعه و ایفای نقش خود نهایت تلاشمان را به کار بگیریم.
🔹
وظیفه اصلی ما خدمتگزاری به مردم و ایجاد ارزش برای صنعت و ارائه خدمات به دولت است و این مسئولیت را فارغ از شرایط سیاسی و اقتصادی دنبال می‌کنیم.
گفتگوی کامل را اینجا ببینید و بخوانید
👇
khabarfoori.com/fa/tiny/news-3242716</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/687263" target="_blank">📅 22:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687262">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a67e37317b.mp4?token=kiMqM28JTnW0Ux7SQpwK3v3WSADHs0uMi8-drwrgzpxBp_V47-gX_4wPI1ujdwCGmEptIz9qlU93YYFei4u34hkpArnxZt1dc8UwHCZUNZP5CioqH4Dnz7O2KS9j6t2EEEdbNtDltyczt_3rLI-uATvmzY6zuTC6_qAjiXKXVApsUD1UpCu-XW4mCBLm9KyxCJt0AMYFUvs6k4BOMMM6Ywqejw3aHFLy4dW-2gHtx2TEMM6qvI8AfPArIESrp16SX-KRvA17DEQOJr2os8wAoMn6qv61xnUW7rejpDmQmphzscIJXIXNzy_bdFp9mY4zk7AX8RrkuxSMubt8uhxFtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a67e37317b.mp4?token=kiMqM28JTnW0Ux7SQpwK3v3WSADHs0uMi8-drwrgzpxBp_V47-gX_4wPI1ujdwCGmEptIz9qlU93YYFei4u34hkpArnxZt1dc8UwHCZUNZP5CioqH4Dnz7O2KS9j6t2EEEdbNtDltyczt_3rLI-uATvmzY6zuTC6_qAjiXKXVApsUD1UpCu-XW4mCBLm9KyxCJt0AMYFUvs6k4BOMMM6Ywqejw3aHFLy4dW-2gHtx2TEMM6qvI8AfPArIESrp16SX-KRvA17DEQOJr2os8wAoMn6qv61xnUW7rejpDmQmphzscIJXIXNzy_bdFp9mY4zk7AX8RrkuxSMubt8uhxFtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: اگر درگیری با ایران جنگ نیست، پس دقیقاً چیست؟
ادعای ترامپ:
🔹
من آن را یک «درگیری نظامی» می‌نامم، چون برای ما چیز چندان مهمی نیست؛ مسئله بزرگی نیست
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/687262" target="_blank">📅 22:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687259">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lwopulT2jwmhO-1Zkew1nEs8Ua5Clh5nfVlhS7WRdwH1puDW52_AZlB94IkTFEqYV7kxl-Gf3bEyHVLm5jYbSVblHRZjzpBsIkjR2LZa424F7fnukBZmVtMCw3MbH0rd1aENdJo_UsJ3hpR9QHeL9FDjo0bwhL12Ro8ajvmAE2OSd8aKL7nAOo_72Ycwd2z5AFJYEf_DT9NJFbvMVGKSHa0MpF5v4hDsom_t_2xWAWRDF9kqFR9nqsTVUBQx9og_FOaxoa5pB5dyeIV8CqgnhgxKKbzXsPF5NVJfjdFfmaamRF0L3_vpPvifoq7upu2ngcA6dqusvK4FxUREvRIcAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0Tn_H1-Z10cICrwzKWl_SqAcD5gXWg5jwld_vdffJxEODRT_E3TIbrCQY5JoqYHFqKU4b7zKnEvF5nU8SI_XvIvzbttRAG_vMUNzpc4eZ-nrN3A_BF4V2199h8VcnjJ6XuMGCXo0bewaS11B_HXMaoonePeui9KmCVFqNE5uT-9cqTJwP4tRFuf4gg3cyIhATupMItjJgpA8EXWOCcgq0inoftrmNd9GBYJntoTq5865m75td_byxzuwMarH3fyvJ8fEVDTcdAUOZmOhw_ts9qcd67KFMdL_zPZwRb2mzjwg1uRHRsXEG0GsIdi5Y5A7OltiG5XzxbVP8IuN6EKLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گروه محبوب ماکان بند، پایان فعالیت خود را رسما اعلام کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/687259" target="_blank">📅 22:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687258">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb552738f.mp4?token=tD4j_zE74GEORJgpSdq79P9kCZWTcfLNIPyuS-AJbUD3piD6jQCLNdwDi7b5EUcxDljTWy09O8VwfbjPEbWUDQENupjJSV2OIAmJViV4UqMC3GySfw6ZDdQWr0U0K2EWa8jHuQzRhTDl_xpLqgbmzLku_rHG8f9dPnAaS51krOPuYz1lwGu9LM1XkNW85UbRMOwuQ-kgqvhEii3gLTEsOuCNniK0jZVxREFFs8OJrlp3jFMExWzDIOmvHgsT5OqhdnFW2VNSNMzvcZcLHy7CQ9lAqmApEYYqHbw0NhWBVHeAciAXP2g-ADbmmBmGVeeJX4P2eD1XD2n9PZUZuKi4bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb552738f.mp4?token=tD4j_zE74GEORJgpSdq79P9kCZWTcfLNIPyuS-AJbUD3piD6jQCLNdwDi7b5EUcxDljTWy09O8VwfbjPEbWUDQENupjJSV2OIAmJViV4UqMC3GySfw6ZDdQWr0U0K2EWa8jHuQzRhTDl_xpLqgbmzLku_rHG8f9dPnAaS51krOPuYz1lwGu9LM1XkNW85UbRMOwuQ-kgqvhEii3gLTEsOuCNniK0jZVxREFFs8OJrlp3jFMExWzDIOmvHgsT5OqhdnFW2VNSNMzvcZcLHy7CQ9lAqmApEYYqHbw0NhWBVHeAciAXP2g-ADbmmBmGVeeJX4P2eD1XD2n9PZUZuKi4bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار:‌ اگر کشوری با ما بدرفتاری کند، ما هیچ تعهدی برای انجام هرگونه تجارت با آن‌ها نداریم #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/687258" target="_blank">📅 22:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687257">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ee5445ea.mp4?token=hgf-rgZPNRhwchHBjI05m-EuuC3Dp2OqZzrxy34Yb1xMFJiBlImkUrygbYg8Jgf8YaPFSpI4BkEkp1W_q2L8SjjqSC7NfnlSHGK75OlEVbNVqIYQH8pT0NBRTv7X54mezfrn3sWu8FkayfAgIa5zeRFBTtJn2e4MPhSZWyABQ9THV_lejnwFtuJwWlMHtmynI1vFSFGtYcA934sl9_G1vZj7Z_Yd5uX62IqzrNqTraDgv_tZ-3QUEx-JRL5XaQ5WUUeTiX2M8DKrsNidTXDkwoHSGlUp8-i1sPNZYVVPshKYCBxrQT3OuUEhrAq6YofwA8YHVMGghCLLdOQIPsNWqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ee5445ea.mp4?token=hgf-rgZPNRhwchHBjI05m-EuuC3Dp2OqZzrxy34Yb1xMFJiBlImkUrygbYg8Jgf8YaPFSpI4BkEkp1W_q2L8SjjqSC7NfnlSHGK75OlEVbNVqIYQH8pT0NBRTv7X54mezfrn3sWu8FkayfAgIa5zeRFBTtJn2e4MPhSZWyABQ9THV_lejnwFtuJwWlMHtmynI1vFSFGtYcA934sl9_G1vZj7Z_Yd5uX62IqzrNqTraDgv_tZ-3QUEx-JRL5XaQ5WUUeTiX2M8DKrsNidTXDkwoHSGlUp8-i1sPNZYVVPshKYCBxrQT3OuUEhrAq6YofwA8YHVMGghCLLdOQIPsNWqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار:‌ اگر کشوری با ما بدرفتاری کند، ما هیچ تعهدی برای انجام هرگونه تجارت با آن‌ها نداریم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/687257" target="_blank">📅 22:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687254">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbizleEIR9niTp0LWzXHnwMvG0rqo4HmDEgBq5dmJ6dAwp-4mCLOV8Mfk4GBd4zPDcAo-TMx7mwaXXdlKVy8bIll6uhgya736Goln2Q47qtSpTlYjT0q7t3TypQVQa_NPDfawaWnwYWSklDFQeQQqk2huJUdM5VOPnqUXIK6CnmnPET5yABGFBPXNq5R2f2B8vC2w_6ULmzIGdUko7_smD7Idza18o6nEbH5dxOJ7-BCoacguPeOSnagpdqrpJ_50nLPMaS8w5HLsN7geNGkOZtqs1Z4pw3aiRw3p9y2raQh8KAQBvJ5lobCxzg2seP31cKh9ZGgAfABNATYb6zXig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت بیمه تجارت‌نو از متقاضیان واجد شرایط در سراسر کشور، برای اعطای نمایندگی بیمه دعوت به همکاری می‌کند.
🔹
بدون نیاز به سرمایه اولیه
🔹
آموزش و پشتیبانی مستمر
🔹
امکان فعالیت تمام‌وقت یا پاره‌وقت
🔹
برخورداری از بیمه تکمیلی برای نماینده و خانواده
🔹
تسهیلات و طرح‌های حمایتی ویژه نمایندگان
🔹
امکان رشد و توسعه فعالیت و راه‌اندازی دفتر نمایندگی
این فرصت می‌تواند گزینه‌ای مناسب برای افراد جویای فعالیت حرفه‌ای، شاغلین، دانشجویان و علاقه‌مندان به صنعت بیمه باشد.
📌
ثبت نام مستقیم درخواست نمایندگی
👇
:
🌐
tjrt.ir/a/life-agent
ظرفیت پذیرش در برخی شهرها محدود است.</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/687254" target="_blank">📅 22:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687253">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CES9Q31kdnlpbUkS9LrEaoqDeSQBG39R8-um_sT2Lde0KLzBLjKCD7LZMowPKSI4y1iCCOuqYEwUFT_dgyPjLwzMtdsRP2DQCQH5me98LndnjoFzfzcnIzD4ihBT9YGRTbRqZTqG0eBqVOadV-Anru6oxxUF0mpHTkM3wPQZJ6T4RbYdJ9ROZEtdc-vie0GCq74LYfEi07I4hilF5ZYJWiXAY8X8WLjdK3ZfLoyoH1TGTk7KWlULbdHEIzp0XJCuaLqiHvN34SWoqak_Pee6HVkZ-_a0d1iJr-HzTTT_E7-ze7OHTI2HXpUX5qsC0tbv8RHrFbkGEgBsFENOU1wE9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند قدم تا یک فرصت دوباره برای زندگی...
یک دختر ۲۲ ساله، دور از پدر و مادرش و در بهزیستی زندگی می‌کند؛
پدری که به‌دلیل یک پرونده قتل، در انتظار اجرای حکم قصاص است.
در این پرونده، با تلاش خیرین و وساطت انجام‌شده، یکی از فرزندان مقتول رضایت داده و تنها برای جلب رضایت فرزند دیگر، ۲ میلیارد تومان  باقی مانده است.
اگر این مبلغ تأمین شود، یک پدر می‌تواند دوباره در کنار دخترش و حامی و پشتیبان او باشد.
🤍
سهم ما از این بازگشت، هرچقدر هم کوچک، مهم خواهد بود.
💳
شماره کارت: 6037997339543507
شبا: 900170000000315473984001
بانک ملی
به نام خانم محبوبه نوروزی
اگر امکان کمک ندارید، این پیام را منتشر کنید. شاید بازنشر شما، آغاز یک زندگی دوباره باشد.</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/687253" target="_blank">📅 22:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687250">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
ادعای وال‌استریت ژورنال؛ پنتاگون برای ادامه جنگ با ایران تا سال ۲۰۲۷ آماده می‌شود
🔹
ترامپ زمان تصمیم‌گیری درباره جنگ، پیامدهای انتخاباتی را در نظر نمی‌گیرد
🔹
جنگ با ایران به یکی از طولانی‌ترین دوره‌های استقرار نیروهای نیروی دریایی آمریکا در تاریخ معاصر منجر شده است
🔹
وال‌استریت ژورنال به نقل از منابع مطلع گزارش داد که پنتاگون در حال تمدید مأموریت نیروها، ناوهای جنگی و یگان‌های پدافندی آمریکا در خاورمیانه است؛ اقدامی که نشان می‌دهد واشنگتن خود را برای تداوم جنگ با ایران تا بخش قابل‌توجهی از سال ۲۰۲۷ آماده می‌کند، هرچند این حضور طولانی‌مدت فشار سنگینی بر نیروها، تجهیزات و توان عملیاتی ارتش آمریکا وارد کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/687250" target="_blank">📅 21:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687248">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔹
خبرهای داغ امروز را در وبسایت خبرفوری کلیک‌کنید
🔹
🔹
حملات پیش دستانه ایران علیه پایگاه آمریکا در اردن؟
👇
khabarfoori.com/fa/tiny/news-3242721
🔹
طلای ۱۸ عیار از ۲۳.۵ میلیون تومان عبور کرد
👇
khabarfoori.com/fa/tiny/news-3242723
🔹
رونمایی از کفش ۱۰ میلیارد تومانی در تهران | جنجال یک جفت کفش به قیمت یک خانه
👇
khabarfoori.com/fa/tiny/news-3242687
🔹
اعتراف ناخواسته ترامپ به عدم پیروزی در جنگ علیه ایران
👇
khabarfoori.com/fa/tiny/news-3242559
🔹
شهرک اکباتان مصادره شد | عکس
👇
khabarfoori.com/fa/tiny/news-3242681
🔹
خبرهای جذاب هر روز را اینجا دنبال کنید
🔹
http://khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/687248" target="_blank">📅 21:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687246">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InfgXL23ZYC2t7AEdvtwhdyHy5nRHa_FgcYyTe0EMC1uqKVVIaj0jQMQJo7DAbQBzl83XC3Txhq3gZzs5p-MhTogJT2Bu58WmUgXz55KHPkfpmn4-mV7H5Npw3vchjVeSPahlHd-kZtgUQAmzXJ_infxpOjGbIkFcBCP5KfzJcv1fJ44kE9baCSu4KCcOAYxgmCFwnNJUrk7r4x0Dx27BQNdTg2cf5XAv3LWMqIXPZVBVj9LEKuXTCwCDyDU3SHBu9N7oI5ADtEwQjxplJSf3MAnVSG7dG42kfojfaOdIhqkOiOT7WiGBHPb4wf0AbUiUdNg-MmCo7bAia8LK5n4FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تپه‌ای که می‌تواند جرقه جنگ دوباره باشد | چرا «علی‌الطاهر» به کابوس تازه اسرائیل تبدیل شده است؟
🔹
در چشم‌انداز کوهستانی جنوب لبنان، تپه مرتفع «علی‌الطاهر» به یکی از مناقشه‌برانگیزترین و حساس‌ترین خطوط تماس در درگیری‌های میان ارتش اسرائیل و نیروهای حزب‌الله تبدیل شده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3242622</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/687246" target="_blank">📅 21:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687245">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
وجود روحیه استقلال‌طلبی جوان ایرانی مظهر شکست آمریکاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/687245" target="_blank">📅 21:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687244">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
خبرها از موج انفجارهای جدید در آسمان پایگاه الازرق(محل استقرار تروریست‌های آمریکایی) در اردن حکایت می‌کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/687244" target="_blank">📅 21:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687242">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOryDIYyoO38CW1lXyorNhnl4vDOV5iJgByCPxZUzsO7UYeeHw9urDJNVhAFPGQ76cfkZYC0r-2opr3u3mQuqRcP87pjVDm_qi-N1JV-eIpoC8syzG_kicjO1zuM0jWbAFk_AJHTtO8x-A42Y48uGa3bhvD3Hk8_AIrfj0bIVnA9RoCsBF6pKG8vTRTK_suJYts5pplBhl61hLM0qsDViVBT3qMozfPGaZpU0QwcRjdzs-q8QP33u3natnK3BbzlLirwuVtEKLvm_pwBafPejnH_8i3mYYTybCciRydsB2xW6NqOxI5b2qT5cQNcYumP8zqJ-OakYEfr4OVWkLRSPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه کلیدی دو قدرت بزرگ؛ آمریکا و روسیه
🔸
بررسی آمارهای بین‌المللی نشان می‌دهد آمریکا با بودجه نظامی ۹۵۴ میلیارد دلاری (۵ برابر روسیه) و صادرات ۱.۹ تریلیون دلاری برتری اقتصادی چشمگیری دارد، اما بدهی سنگین ۱۱۵ درصدی از GDP چالش اصلی آن است.
🔸
در آن سو، روسیه با بدهی پایین ۱۸ درصدی، در ذخایر عناصر کمیاب زمین با ۲۸.۷ میلیون تن (۱۵ برابر آمریکا) دست بالا را در اختیار دارد.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/687242" target="_blank">📅 21:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687241">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COh2s3sfG_-dsBDqgEXozSDV66_JJFze_PO8Qgrxmbqia69QNpzf8PXIgw_Xmk6wbU7B_PDX-r6fhZANIfaqVGs_SUbI8jxqDR7RPqW2oO9aUzrRpezO6hXLu-T0JD3xmgkvKI8FVfQltv5vbxT4E5-AvI_6cO0clj1Ecx-t7Uy9_zbSL_tTuT4LHojZWe-ye8Z9fx9Vmp37q2GLs-1lBj47kn7iNFcvBIE72-73MeFYosQTxf6mAXOMH15ntdjPJ5eZpLDJ5D3ljUF2XnjvRddFdrRHIoRxYblPzd4NyoIimDuUfNGSoa-HpEoJDqAh5ywy7dqsCyDpKViqsUMhNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز: ارزیابی اطلاعاتی آمریکا؛ ایران برای طولانی‌کردن جنگ و تشدید درگیری آماده می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/687241" target="_blank">📅 21:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687239">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bus8vKvIFncd9ZnVVFXB0HDeix-Fi1ecm80nSdVMfIeZlIYQkiKi956oXCAIF-WtYmfgzQrrvmAkmlwcwydmdgDmL7lfJiHoxUTcMiDa9ofshKa-70fUslMQXXkvJf7DlBsdMp1HWeGKoaQ9ka42j2TdvYYN9lmfeT8rKcGFUACxlEbL_pz2jenT9BfBu6M20L-vs4jpnD78Em8tYCrI7l7iI4t3MIQ1qo1PFzpma8DyMg_6-0vHfbnm1LSqYCekVYDOYjQ_O1eljpSWzlDI-h50_EEC452Hi8MMpxPLEmLtLf_fV0qiLMpDJEFOJFrjkACyqq8vVL6uah8FUURw_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احتمال جنگ گسترده بین ایران، آمریکا و اسرائیل وجود دارد/ این نقطه، محور اصلی درگیری واشنگتن و تهران خواهد بود
🔹
یک کارشناس مسائل سیاسی با اشاره به تشدید دوباره درگیری‌ها میان ایران و آمریکا، تنگه هرمز و فشارهای اقتصادی را از مهم‌ترین محورهای تقابل دو کشور دانسته و می‌گوید: واشنگتن پس از ناکامی در دستیابی به اهداف نظامی خود، فشار اقتصادی و تهدید نظامی را همزمان دنبال می‌کند.
مشروح گفتگو را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3242652</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/akhbarefori/687239" target="_blank">📅 21:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687237">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24c21344.mp4?token=CS1Zxv--P3-DpJxnhGxbrLUe1WYM08rfP0oxC2rDcSI7h4w8AUMQ4z_aeQx1xuLMukCQwDLVggDybIpJY9K5bhODrrwRcPu1Kb9meao-OCuzLB0l7xmYyr7wLdczPZtQIPv5QFShut_j0rDYFiZ7gzJtx6d6VEu0jsenv9wh_XY-q0Uq_DXtkayRmOhaJI9VpLaCRBdLB5bs85J1m2LQ1i97gK4fdV0u0tk1OGB6WhlO2P8XoK11To02HkV4vTchGRevu8XcS4Ftgkf5G_lu64ondblULEq1PClclzFAhoPRxHl6Y6fiY4p7b5v54nH-yy-9F3xE-5GyIGzHguHQ50W3gBSPsLxW30-uD-ewCdK6AqdQ9_UNEJpVWLp469Am2ujVgHTW1XMTlSICPm9XT_If-HlYyPcTrsnWUwrWsM1X_lbIPpwok_aSNR8YT9KhyQQMiNoNTlAiEaXPWr5reGXNa6B5hNukJMZDwbnlROsacWi_Xx8RTfcLfAy1ZTIvbd__jXoCqBR-UPhEJbc7Ir__2gbEg3MC-FQb1GAAq-Ioe8FMvbIX8zdfWPfnJlWJ2kWuQC5joMepStbN_JCZ0iXmqJ2og2NcWRnL_SaNexx1VdPtgkrpPFnr6tn8DsXF4VgJSdQ_a0oge0cmE-IpCWD-WNWYd_rRaXAOshawr48" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24c21344.mp4?token=CS1Zxv--P3-DpJxnhGxbrLUe1WYM08rfP0oxC2rDcSI7h4w8AUMQ4z_aeQx1xuLMukCQwDLVggDybIpJY9K5bhODrrwRcPu1Kb9meao-OCuzLB0l7xmYyr7wLdczPZtQIPv5QFShut_j0rDYFiZ7gzJtx6d6VEu0jsenv9wh_XY-q0Uq_DXtkayRmOhaJI9VpLaCRBdLB5bs85J1m2LQ1i97gK4fdV0u0tk1OGB6WhlO2P8XoK11To02HkV4vTchGRevu8XcS4Ftgkf5G_lu64ondblULEq1PClclzFAhoPRxHl6Y6fiY4p7b5v54nH-yy-9F3xE-5GyIGzHguHQ50W3gBSPsLxW30-uD-ewCdK6AqdQ9_UNEJpVWLp469Am2ujVgHTW1XMTlSICPm9XT_If-HlYyPcTrsnWUwrWsM1X_lbIPpwok_aSNR8YT9KhyQQMiNoNTlAiEaXPWr5reGXNa6B5hNukJMZDwbnlROsacWi_Xx8RTfcLfAy1ZTIvbd__jXoCqBR-UPhEJbc7Ir__2gbEg3MC-FQb1GAAq-Ioe8FMvbIX8zdfWPfnJlWJ2kWuQC5joMepStbN_JCZ0iXmqJ2og2NcWRnL_SaNexx1VdPtgkrpPFnr6tn8DsXF4VgJSdQ_a0oge0cmE-IpCWD-WNWYd_rRaXAOshawr48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات جنجالی خبرنگار ارشد بی‌بی‌سی: ادعای تسلط ارتش اسرائیل بر تأسیسات و نقاط راهبردی حزب‌الله، اقدام انتخاباتی نتانیاهو است و هنوز منبع مستقلی آن‌را تأیید نکرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/687237" target="_blank">📅 21:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687236">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ادعای العربیه: حمله موشکی به شمال اردن گزارش شده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/687236" target="_blank">📅 21:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687235">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
مدیرعامل رایتل: با تعرفه‌های فعلی، کسب‌وکار زیان‌ده است/ هزینه تجهیزات ۴۰ تا ۵۰ درصد گران‌تر از منطقه
مهدی فقیهی، مدیرعامل رایتل در
#گفتگو
با خبرفوری:
🔹
با تعرفه‌های فعلی، کسب‌وکار ما زیان‌ده است؛ قیمت اینترنت ما یک‌شصتم تا یک‌هفتادم کشورهای منطقه است، اما تجهیزات را به دلیل تحریم‌های ظالمانه ۴۰ تا ۵۰ درصد گران‌تر می‌خریم و دخل و خرج کسب‌وکار همخوانی ندارد.
🔹
نیازمند حمایت دولت و رگولاتور هستیم؛ متأسفانه این حمایت‌ها را بسیار کمرنگ می‌بینم. انتظار داریم نهاد رگولاتوری ناملایمات با اپراتورها را کاهش دهد؛ الان فضا، فضای جریمه و برخورد نیست.
🔹
اگر جرایم ادامه پیدا کند، ما را فلج‌تر می‌کند و ارائه سرویس به مردم با مشکل مواجه می‌شود.
گفتگوی کامل را اینجا ببینید و بخوانید
👇
khabarfoori.com/fa/tiny/news-3242716</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/687235" target="_blank">📅 21:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687233">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de0709d3a.mp4?token=C81dE9yjrWtibuL6C5mjHt6uQSb5l-IGbobk-mnj1yhUo79Faqb027uguaiQpes_Sh4RGsUTwmUxKAwg4xVpx4g-CQfGMJlD3OYmXZp54qTG4AvJsOkjn-3q-zTGe4FgpkWv_Dl-YAfjNgivEJ9lCYEdwInqk1MZfQHgIgwU4wb35gr8lvA6bTAP4Nb_KHemqWjNSwyKNa2kUDhspnJ2uD5zKMCKUOk6bKgnWfXjIaj9l8aVA04q2vT8v5_5IdyWv1FKokxty_ck03c4UmcieoND53CFPh4MdUeMeCCvSivElEPqLqwpFhIZt8cog-r_OIJhIo6zevL5BU4khRgtfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de0709d3a.mp4?token=C81dE9yjrWtibuL6C5mjHt6uQSb5l-IGbobk-mnj1yhUo79Faqb027uguaiQpes_Sh4RGsUTwmUxKAwg4xVpx4g-CQfGMJlD3OYmXZp54qTG4AvJsOkjn-3q-zTGe4FgpkWv_Dl-YAfjNgivEJ9lCYEdwInqk1MZfQHgIgwU4wb35gr8lvA6bTAP4Nb_KHemqWjNSwyKNa2kUDhspnJ2uD5zKMCKUOk6bKgnWfXjIaj9l8aVA04q2vT8v5_5IdyWv1FKokxty_ck03c4UmcieoND53CFPh4MdUeMeCCvSivElEPqLqwpFhIZt8cog-r_OIJhIo6zevL5BU4khRgtfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: آن کسی هم که سطل زباله آتش زد، فرزند ماست، با وجود دشمنان، تکرار نشدن حوادث دی‌ماه نیازمند خردمندی و آگاهی مردم است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/687233" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687231">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OD8k-sZ7hsnVvmKySCrg-uuyaRxwJgko0nFvuZKwqim_krQCdZqGZGaI-toWA4ZzRANfDLwaPPuUTnFxMg9sfV0i6EWsHhU1JbOCdCqP_IjXiEuNs3FJUa_uh3kw-EH3y6ZDzlic8Af6uReX_fgeKk2Bbqnw_kI2QCNovWLV3b5Sk-4PL7_pSZMkEFgiRrydOcGofHLNjlqlI5zlrdR872VfknOAHh2qglXwAQSL3YoISt6ycOH8hHIeUSRL43Hs8jiud3seup3Y4MvENaYjqhFmoFVrIhQHtXPZSPDb_OPwOsC25lDHYkSe98caLxGAtB5RuncdLq-OAGt9ROKkFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناو زنگ زده آبراهام لینکلن، نماد فرسودگی هژمونی آمریکا
🔹
ناو هواپیمابر «آبراهام لینکلن» متعلق به نیروی دریایی آمریکا که زمانی نماد قدرت و سیطره این کشور بود، این روزها پس از ۲۸۶ روز حضور در دریا، به دلیل فرسودگی و مشکلات فنی فراوان، سرانجام روز دوم سپتامبر ناگزیر در بندر«لائم چابانگ» تایلند پهلو گرفت. دیدن زنگ زدگی و فرسودگی بر بدنه و بخش‌های مختلف این کشتی که دوربین‌ها آن را ثبت کرده‌اند، ناخودآگاه تصویری از یک هژمونی پوسیده و نخ‌نما از آمریکا در ذهن هر بیننده‌ای ایجاد می کند.
در خبرفوری بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3242717</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/687231" target="_blank">📅 20:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687228">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-text">⁨ ⁨ کسب‌وکارتون رو به فرصت‌های بیشتر وصل کنید!
✨
💫
با «شهرآسا» بانک شهر، فعالیت پذیرندگان می‌تونه مزایای بیشتری برای کسب‌وکارشون به همراه داشته باشه؛ از تسهیلات و جوایز ویژه گرفته تا امتیاز و قرعه‌کشی ماهانه.
💳
با اتصال پایانه فروشگاهی یا درگاه پرداخت اینترنتی به حساب بانک شهر، از مزایای ویژه شهرآسا بهره‌مند شوید:
🔸
تا ۷ برابر میانگین حساب دریافت تسهیلات تا سقف ۱۰۰ میلیارد ریال
🔸
جوایز نقدی و هدایای ویژه اصناف
🔸
تجهیزات جانبی ویژه
🔸
تقدیر از پذیرندگان برتر
🎯
به ازای هر ۱۰ میلیون ریال تراکنش در ماه، یک امتیاز کسب کنید و شانس خود را برای برنده‌شدن در قرعه‌کشی جوایز ارزشمند افزایش دهید.
یعنی اینجا، فعالیت بیشتر می‌تونه فرصت‌های بیشتری براتون بسازه.
🚀</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/687228" target="_blank">📅 20:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687227">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lknyHINnZt_qLJB2PnwpwkZipWH3QR0lqnjb9iprYWwGSC208I7rEaRpZ77I6vbBknNQku_Rv47SwzJOnqXcdDXW3GkumRP6Ezjaho5KhCbutoCCBi_xBSJja2voJqrD7K3s86-GymDiieGt4QpqF8ilVzZX5Po2vgJgRxMNL3PoHbYjBS0JvTHGPTRL-q8ZpQ68WCxbq8CkKRwN7lQ9fThhxkDm_o265VvDMc9fEVWCvBFeSgQZSAl12KJNgW39F3zepITviXdfVDGpPn59L60HDEBxCcM-9wTzeem_YeiF3-QIv7rkYOS3yOnSfAAiuiMvvOo122fpT6szLak4Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: کشورهای منطقه باید آینده خود را به دستان خود بسپارند
رئیس مجلس:
🔹
تأکید چین بر پرورش امنیت مشترک، اصلی را منعکس می‌کند که ایران مدت‌هاست از آن دفاع کرده است.
🔹
کشورهای منطقه باید آینده خود را به دستان خود بسپارند، و ثبات واقعی تنها از طریق معماری امنیتی جدید بومی می‌تواند به دست آید. ایران آماده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/687227" target="_blank">📅 20:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687225">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
موشک‌های ایران در آسمان اردن  جزئیات کامل
👇
khabarfoori.com/fa/tiny/news-3242721</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/687225" target="_blank">📅 20:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687224">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86f2c982f0.mp4?token=Uf7fTyeTM8MVjFqZLCRw2ZZSr0V3g4nJbQ5Rxc0WeGuSChjgBwOrlvl_S3EVijuiXqaYFyGcIQOtQAvJkpZub5IIrF1PtjWi-SNuTOCfacKv5Fn0drAOECl_qhmOKt1X9g8CB6C_YiFan3ZeqdMJ2Itw4P1PJqDU2xFytI1N5Q9ZD-Qzx95qjEAhuTx0rkJwF530S_pnAnVnDXVLInS5Mmy9a5OFWyT9AA6T8zLstdkG8fG2l_KybbD4P0tJHXTUxjzZYauUsEk9l5UVzdgPXmsW-BDdRwzp77q_rBKCMCUjA6VrRyd4IJ70exKhugB61DK6dayzBwrhsBdRR3qjlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86f2c982f0.mp4?token=Uf7fTyeTM8MVjFqZLCRw2ZZSr0V3g4nJbQ5Rxc0WeGuSChjgBwOrlvl_S3EVijuiXqaYFyGcIQOtQAvJkpZub5IIrF1PtjWi-SNuTOCfacKv5Fn0drAOECl_qhmOKt1X9g8CB6C_YiFan3ZeqdMJ2Itw4P1PJqDU2xFytI1N5Q9ZD-Qzx95qjEAhuTx0rkJwF530S_pnAnVnDXVLInS5Mmy9a5OFWyT9AA6T8zLstdkG8fG2l_KybbD4P0tJHXTUxjzZYauUsEk9l5UVzdgPXmsW-BDdRwzp77q_rBKCMCUjA6VrRyd4IJ70exKhugB61DK6dayzBwrhsBdRR3qjlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک‌های ایران در آسمان اردن
جزئیات کامل
👇
khabarfoori.com/fa/tiny/news-3242721</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/687224" target="_blank">📅 20:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687223">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">11 Ane Manaee (1403-09-16) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/687223" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه یازدهم
حجت‌الاسلام امینی‌خواه:
🔹
عمل در آیینه هستی؛ تأملی بر جایگاه و معنای آن
🔹
نورِ عمل؛ چراغی که راه‌های بسته را روشن می‌کند [4:20]
🔹
نورانیت نماز شب؛ گشایش قلب، تغییر اخلاق [4:58]
🔹
شرح صدر؛ گنجینه‌ای برای دل‌های نورانی [7:31]
🔹
علم به فایده؛ کلید رفع نیاز و رسیدن به کمال [15:31]
🔹
تشکیک وجود در اندیشه ملاصدرا؛ شعور و محبت، در تمام مراتب هستی [19:27]
🔹
تجربه‌ نزدیک به‌ مرگ؛ وقتی سنگ‌ها هم انس و تعلق دارند [22:03]
🔹
لذت‌های حیوانی؛ وقتی انسان مسیر کمال را گم می‌کند [24:48]
🔹
آنجا که اراده انسان، محض اراده خدا می‌شود [31:25]
🔹
کمال انسانی؛ جایی که هیچ قدرتی را یارای مقابله نیست [35:30]
🔹
حلال و حرام؛ نقشه‌ای برای رسیدن به کمال انسانی [42:11]
🔹
صبر؛ کلید طلایی رسیدن به کمال انسانی [46:59]
🔹
لذت حقیقی؛ در گرو بندگی و انجام وظیفه [50:50]
🔹
چادر فاطمه زهرا (سلام‌الله‌علیها)؛ نجات‌بخش خیل عظیم خلائق در عرصات قیامت [59:11]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/687223" target="_blank">📅 20:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687222">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
فروش تجمیعی شرکت‌های شستا به بیش از ۵۷۰ همت رسید/بیش از ۵۰ هزار نیروی انسانی شستا در دل جنگ پای کار ماندند
محمدرضا سعیدی، مدیرعامل شستا در
#گفتگو
با خبرفوری:
🔹
علیرغم آسیب‌های جنگ، شستا نه‌تنها تولید و پایداری خود را حفظ کرد، بلکه آن را ارتقا داد. تاب‌آوری کشور در دل جنگ با تلاش نیروی انسانی شستا تقویت شد
🔹
یاد و خاطره ۴ شهید والامقام شستا را گرامی می‌دارم و از تلاش همه مدیران و کارکنان این مجموعه بزرگ تقدیر می‌کنیم
گفتگوی کامل را اینجا ببینید و بخوانید
👇
khabarfoori.com/fa/tiny/news-3242509</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/687222" target="_blank">📅 20:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687221">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
خبرهایی درباره حمله به پایگاه‌های آمریکا در اردن
🔹
منابع خبری گزارش دادند پایگاه‌های آمریکا در اردن هدف حمله قرار گرفته است.
🔹
این منابع گفتند در پی این حملات، صدای چندین انفجار مهیب در مناطق مختلفی از اردن شنیده شده است.
🔹
منابع اردنی اما مدعی شدند این موشک‌ها…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/687221" target="_blank">📅 20:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687220">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
شنیده شدن انفجارهای قوی در اردن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/687220" target="_blank">📅 20:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687217">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
شنیده شدن صدای چندین انفجار در اردن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/687217" target="_blank">📅 20:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687216">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171f23100d.mp4?token=PqgBlhmUEZVWJ4Gf6rSxVQhKEJ5GKRWOYtN_42QV9VvNef1u2e4KUJHvQDxQZpbd6wYbGtlNN5TVOiHgT4Jy1yB26Y-PECtjfG673m-GSAMv4dMTLPtmcGjF0qqNIQ3DwS3r7QoyIdjsFDaQsDYYg6kGyu-EVc0d6gGhok660pZ-Y38wWtCMs2ZHJpuhSLFxxFoiWuG5MYFm3dIT0aO2nIVjMt20UhOx7xDYNJNOqs6t1xGRbRoxB9f2Vv3aTAWCBbR2KHs_cpqqp_JriVG4pXWuU9iOdl1b2lsnhnkDbabfTYX82BoyyzAQiTTNkHGWMnfZhXam6GaXciQ0AGtA9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171f23100d.mp4?token=PqgBlhmUEZVWJ4Gf6rSxVQhKEJ5GKRWOYtN_42QV9VvNef1u2e4KUJHvQDxQZpbd6wYbGtlNN5TVOiHgT4Jy1yB26Y-PECtjfG673m-GSAMv4dMTLPtmcGjF0qqNIQ3DwS3r7QoyIdjsFDaQsDYYg6kGyu-EVc0d6gGhok660pZ-Y38wWtCMs2ZHJpuhSLFxxFoiWuG5MYFm3dIT0aO2nIVjMt20UhOx7xDYNJNOqs6t1xGRbRoxB9f2Vv3aTAWCBbR2KHs_cpqqp_JriVG4pXWuU9iOdl1b2lsnhnkDbabfTYX82BoyyzAQiTTNkHGWMnfZhXam6GaXciQ0AGtA9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: ماجرای قلب نشان دادن سخنگوی دولت به خبرنگاران چه بود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/687216" target="_blank">📅 20:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687215">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
شنیده شدن صدای چندین انفجار در اردن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/687215" target="_blank">📅 20:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687213">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/338f0b7bb5.mp4?token=TZCnhVy45A24vKQFjl2MA8LGhE5iOsb_Slt9lxipbmJQ9tU14MoTdskNyljYKk4H4nkPgnd2dizpVqJTUcYF5KOa7FU40pbFHUxRHQ7BVTE9QDoLcUrRUu3rj_0Vo3sRVz20E140w5sBQZ2_avUkckEp1gVwjzG2KBLs-iPI4IV9crkU7vhvOPjekjTiZ7KM_ZqkouNNcCYrYBDdkyetIsl7epWpIVPu8RJ6-Q27cfxyqdNofPq2laxg0dFNlF9J2lNMsrdvGQA76khotHZq8elLSatBXxa8nNSpoFC-TAI_TiSc-gCo8DZmIczgonW7zXpuiZK8ctIR0Ebne4gi7CVL5UFGE7PKfLmlDm0Qrn6hZ47Z3hkvHMwoHnMT0sYO23ihLiebhD3QR_Tlv7u_JuHsqTVFsjsBhGSlwLu5HbiSi29kRgAchSz-38QGEdrdVLzfn0XjOVQg4pUWfBLprj5kP6Cl2ALrB-gKYWJWl_iRoy_48VS4qjfsoJCywRnV-pLYR8jaJWlL31lOh0CYqUf7__rg64Etg3AgML0S5XSQudZkbFoP773dlhPRPTfseflcTC25CvxLBOxFcv3OnA6I8Bw9rMheoPC-Ipo8Pz5uVXuSlVjj8iO0m08OMksR7j8s4x5Q6825LugtIM_6XoNFFUcz6eWRWalRKZko3SI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/338f0b7bb5.mp4?token=TZCnhVy45A24vKQFjl2MA8LGhE5iOsb_Slt9lxipbmJQ9tU14MoTdskNyljYKk4H4nkPgnd2dizpVqJTUcYF5KOa7FU40pbFHUxRHQ7BVTE9QDoLcUrRUu3rj_0Vo3sRVz20E140w5sBQZ2_avUkckEp1gVwjzG2KBLs-iPI4IV9crkU7vhvOPjekjTiZ7KM_ZqkouNNcCYrYBDdkyetIsl7epWpIVPu8RJ6-Q27cfxyqdNofPq2laxg0dFNlF9J2lNMsrdvGQA76khotHZq8elLSatBXxa8nNSpoFC-TAI_TiSc-gCo8DZmIczgonW7zXpuiZK8ctIR0Ebne4gi7CVL5UFGE7PKfLmlDm0Qrn6hZ47Z3hkvHMwoHnMT0sYO23ihLiebhD3QR_Tlv7u_JuHsqTVFsjsBhGSlwLu5HbiSi29kRgAchSz-38QGEdrdVLzfn0XjOVQg4pUWfBLprj5kP6Cl2ALrB-gKYWJWl_iRoy_48VS4qjfsoJCywRnV-pLYR8jaJWlL31lOh0CYqUf7__rg64Etg3AgML0S5XSQudZkbFoP773dlhPRPTfseflcTC25CvxLBOxFcv3OnA6I8Bw9rMheoPC-Ipo8Pz5uVXuSlVjj8iO0m08OMksR7j8s4x5Q6825LugtIM_6XoNFFUcz6eWRWalRKZko3SI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از معنای پردازش تدریجی هیجانی در روانشناسی
🔹
ذهن مثل همان شن‌هاست، وقتی آسیب می‌بیند، نیاز به زمان و تکرار دارد تا خودش را دوباره شکل بدهد به شرطی که در جریان بمونه و رهاش نکند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/687213" target="_blank">📅 20:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687212">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/687212" target="_blank">📅 19:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687211">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gl7jQ1p6hJ6hTjoqsHqWtYN_-TOqH8rSu5fOyRByXoH80uTEISHfNIJGbscmC358KJWCeFxqrdOpNbHlHKPu9mRrnA-tOr94KRHQKVb3uJYeXngzMO-kNhmjopysp9p2y4i1oe7qgc9FpwHLXMcmNQBSW7pA_q8TAVqQMhmzKR51PZNtIRRgJ4NC_kenQs4n9j_xV_wh9ooR-U_5gN7XxmE_idEdF7HO_IgQym_rJ_T5nPlC3b6NSZuaPYUwt18ZP-e64IJzvVbV6hbqEWguuzrRr0-tttqrdhNNw5WiAUt9SKMulQJfgrxF1GUutfeI2na9y-pKzSQ1e3Q8P9Hstg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشاوره رایگان پزشکی برای متقاضیان کاهش وزن با آمپول‌های لاغری
🔹
با توجه به سیر صعودی مصرف خودسرانه آمپول های لاغری و با همکاری شرکت های دانش بنیان دوراپزشکی ، این امکان فراهم شده تا افرادی که قصد استفاده از آمپول های لاغری را دارند به صورت کاملا رایگان و آنلاین توسط پزشک ویزیت شوند.
🔹
کاربران در این سامانه با تکمیل فرم کوتاه ارزیابی، شرایط خود را از نظر BMI، سوابق بیماری و داروهای مصرفی بررسی کرده و سپس با مشاوره رایگان توسط پزشک از شرایط مصرف آمپول های لاغری با خبر می شوند.
👈
شروع ارزیابی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/687211" target="_blank">📅 19:46 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
