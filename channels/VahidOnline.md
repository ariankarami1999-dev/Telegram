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
<img src="https://cdn1.telesco.pe/file/bs6rbOrc1r1zqLuhaYfbYL2o1N9o_ZgIBy9dpn3-X93_fLgm5jKCjJFhb6gerKUI5h9IPGdtNtt8mkq9qDyKUOzwGnn8EdagLn_5G_OcSCck_kCs-wPv8_aBS49rN-8DxBwqdz_3GqDnS-t0G422qwoqs1u7BWfwE3eHB6vEaQh9V0EuSoa6a2yAoDc7Xgc5n4JK0-YamVF9KBDz_CJVIAL_h7oMqNJgXYGv7itS-VxRRqGA9JwNG9Ns1uXTO-hnv39Q0CSdGArUtn1cYZ9Gb1cskG1NdjXdjXRnsCly2MQWhwbdH9RM8V4nTIfGgpQ9fVJL11mllW_I6QYFvl-8gQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.4M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 02:05:02</div>
<hr>

<div class="tg-post" id="msg-78454">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5bb8WOoUVKUwcnZ5Fbrbab4_pCGZceE3MAH9liuQseYN9VRoAB30qAW3RQQ7ZbYMRcN9C63u41A5XpbGgAkPuJ1VFj5LHFxbgVRXH_m6S9tzp-hpQ-3lpXVqjzZx0tX9XtpUITshpRxOQFEceA5eMcaVNUZ92tuxAuBY4bxIoE-MBEIe04tp87vv0bZ_1tbGz39bmLv-qDRqQ9_Lz6AiLQaZgOFrJVsfH9FWwubQzfoSCq7LWQLqt7MXebHRVUvVQsicBOMT09XkIxdoQ7HAmTG2UE9scKbfes9DUSwCB7D4BZxf_-gZfhdm3Ci9denSyyl9AkRem-9rErwA10ahQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی دبیر شورای عالی امنیت ملی جمهوری اسلامی، شامگاه شنبه ۲۸ شهریورماه در شبکه اجتماعی ایکس نوشت ۷ شرط ایران برای آغاز «هر مذاکره‌ای» به دولت آمریکا اعلام شده است.
رضایی در این پیام نوشت: «پیام تهران روشن و بدون ابهام است؛ اگر واشنگتن می‌خواهد از مخمصه‌ای که خود ساخته خارج شود و بیش از این در آن گرفتار نشود، راهی جز پذیرش حقوق و شروط ایران ندارد.»
ساعاتی پیش از انتشار این پیام، رسانه‌های دولتی ایران به نقل از گفتگوی محسن رضایی با شبکه الجزیر گزارش کردند، ارتباط میان تهران و واشنگتن به وسیله میانجی‌گران قطری و پاکستانی ادامه دارد و شروط تهران برای بازگشت به مذاکرات به کاخ سفید اعلام شده است.
رضایی با اعلام آنکه تهران منتظر پاسخ واشنگتن است گفته بود، پایان دادن به جنگ در همه جبهه‌ها، آزادسازی دارایی‌های مسدود شده ایران و پایان محاصره دریایی شروط ایران برای آمریکا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/VahidOnline/78454" target="_blank">📅 23:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78453">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cSx37eznbA9FZyZZDbWbHE_8lDSuoAGCPJlLUdsmvuNygwX4clqMHbPYkexx8DH0ejI-Yt83pDokVVxttnK4gt2h0hg_uflSbgM_grjOWN8wLVScg7MtTQGEeHbeBb7hQR95TtSBbj9g3XYcQGZY6OAWfPyZF-08DqsEeLJ8M2EttGkXqA_sD_a6melBuNG9Bhfm92LAuF7iu-KExrRcJIDwQv-7hDASHA3ek9C4iGmu521OiQbzllDZFhhjpVoxXs1k101HQweC4vvLYsaNExHdt2pwQayKrCBD3lzSSW_Udtux1yuo4JoSGj1daRdSlF9gyAAqpnGR6IMrmb9JNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هاکان فیدان، وزیر خارجه ترکیه، گفت در پی حملات حوثی‌ها، عربستان سعودی ممکن است در برخی زمینه‌های فنی نیازهای نظامی داشته باشد و ترکیه برای پاسخ به این نیازها در چارچوب «ائتلاف دفاعی مکه» با عربستان سعودی و پاکستان مشکلی ندارد.
فیدان شنبه ۲۸ شهریور در گفت‌وگو با شبکه «ان‌تی‌وی ترکیه» گفت حملات به تمامیت ارضی و حاکمیت عربستان سعودی جدی است و ترکیه در چارچوب توافق میان سه کشور در کنار عربستان سعودی قرار دارد.
او همچنین گفت عربستان سعودی تمایلی به ورود به جنگ آمریکا و جمهوری اسلامی ندارد و کشاندن این کشور به این درگیری «غیرقابل قبول» است.
فیدان در پاسخ به پرسشی درباره ارزیابی برخی منابع اسرائیلی و ایرانی مبنی بر اینکه «ائتلاف مکه» تنها روی کاغذ است، گفت: «ما به این حرف‌ها می‌خندیم. ائتلاف مکه به یک سازوکار بسیار تاثیرگذار و تغییردهنده معادلات تبدیل خواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/VahidOnline/78453" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78452">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/205953bb15.mp4?token=DlDsdwTuBN3MefC1q5jJ_z_TZpblvfjdxV9E3piFTuWXRvtuwfSfAc-VIPU3YJplgTBOjfz-MoqwTMGKsq2zvX2nowA2RdJQxzsEiFwIQaWMsdvFS7b5E92hcwEefXCB1_JRO70EzUQ7vJVLo5uW-mtiCKXCrzoLL6bdYqyccn3xkYUkGcVYnZ4wCZAnafcCU14nJvn3rKQPmap7Vl2zbd2t43UzIlQqOQCcnfm2-3BELR7Mn7I1U0C45EOxHBTA8GK0KTBkbE1J7bTR84_r00Op0Tv3GZbXuhu3wd_R6VxFNSNNnZ4quO57Irc1kvIMXN0QigkLG7D1TBP6BNf-Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/205953bb15.mp4?token=DlDsdwTuBN3MefC1q5jJ_z_TZpblvfjdxV9E3piFTuWXRvtuwfSfAc-VIPU3YJplgTBOjfz-MoqwTMGKsq2zvX2nowA2RdJQxzsEiFwIQaWMsdvFS7b5E92hcwEefXCB1_JRO70EzUQ7vJVLo5uW-mtiCKXCrzoLL6bdYqyccn3xkYUkGcVYnZ4wCZAnafcCU14nJvn3rKQPmap7Vl2zbd2t43UzIlQqOQCcnfm2-3BELR7Mn7I1U0C45EOxHBTA8GK0KTBkbE1J7bTR84_r00Op0Tv3GZbXuhu3wd_R6VxFNSNNnZ4quO57Irc1kvIMXN0QigkLG7D1TBP6BNf-Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، روز شنبه ۲۸ شهریور، در پیامی ویدیویی خطاب به شرکت‌کنندگان در «مجمع گفتگوی جهانی ۲۰۲۶» به میزبانی انجمن سیاست خارجی اندونزی، با انتقاد از رویکردهای مداخله‌جویانه در خاورمیانه تاکید کرد که دهه‌ها حضور و فشار نظامی نه‌تنها کمکی به ثبات نکرده، بلکه چرخه‌ای بی‌پایان از تنش را رقم زده است.
عراقچی گفت، ریشه بحران‌های منطقه را باید در یک حقیقت تلخ جست‌وجو کرد؛ چرا که سال‌ها مداخله خارجی، فشارهای همه‌جانبه نظامی و درگیری‌های پی‌درپی اثبات کرده است که مداخله نظامی امنیت نمی‌آفریند و اعمال فشار و زورگویی هرگز به صلح ختم نمی‌شود.
عراقچی در ادامه این سخنرانی ویدیویی خاطرنشان کرد که در شرایط کنونی، جنگ به‌جای آنکه آخرین راه‌حل باشد، عملا به ابزاری معمول در روابط بین‌الملل تبدیل شده است. رویکردی که نتیجه‌ای جز عادی‌سازی خشونت و تداوم الگوی درگیری و تقابل دائمی در منطقه به همراه نداشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/78452" target="_blank">📅 16:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78451">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpk_EYQokkmxGFFv9IEoRJfb_19UW_sQLeyjqCW9o9_ZsxYTp-5TlQx3wvrtDpG8kjVqPVsywapq4wrYfsW4M76Q-BQP0lYvAQ9oLVkK_TSbHw626iPqltfPkBeRGigDfTuEMS_Cevkf98wnBaxRSOYiLk4JeiWyj94YhP7I1a7Noj-fiOjJlW3ZwEPrjlE9_E_UaNd6I-lNQP1raCCGwCMaETinNVNRhYyWlKN6jjwuzS_p3OwS3VYidON8Hz-8fgBQ_eZDromUDJB3j62RcP1wHBkMt2jsdqhnmRHv38UjhmsKDpeqnh8cSw2vZPdAixKCqp7IXOfkUx6sL2wtPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادستانی تهران اعلام کرد علیه عوامل و دست‌اندرکاران برگزاری مسابقه دو در بوستان ولایت اعلام جرم کرده و پرونده قضایی تشکیل داده است. دادستانی مدعی است که در این رقابت «موازین قانونی و شرعی رعایت نشده بود».
مسابقه دو ۱۰ کیلومتری بامداد جمعه ۲۷ شهریور با حضور زنان و مردان برگزار شد. انتشار تصاویر شماری از شرکت‌کنندگان زن بدون حجاب، رقابت را به موضوع بحث در شبکه‌های اجتماعی تبدیل کرد.
بنابر گزارش خبرگزاری فارس، برگزارکنندگان اعلام کرده‌اند مسابقه با مجوز وزارت کشور و هیئت دوومیدانی استان تهران انجام شده است.
هیئت دوومیدانی تهران گفته پیش از آغاز رقابت از شرکت‌کنندگان تعهد کتبی برای رعایت «حجاب و شئونات اسلامی» گرفته شده بود.
حبیب ستوده‌نژاد، مدیرکل ورزش استان تهران، به خبرگزاری تسنیم گفت مجوز رویداد از شورای تأمین استان صادر شده بود و با ورزشکارانی که «خاطی» شناخته شوند برخورد قانونی و انضباطی می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/78451" target="_blank">📅 16:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78450">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udHySe2qi2ZMpfv50yrHPZfqJa-D8E6-aiZLt3zNHcSRYjMrVxBzbMm29Ja6EbptjDgyqCIrJqILrJZLH6kyLv49WwNzc5Vnjht78LpvdEQJGR_SAK-pPGQKuzD35I1kUsPix5YNO6MDhfdMy4znyPlSebIki50jUzk_Tm4ll4s5ywnTks0TrgXEDJHfeuYEmfhbjkxoHUe5Yj9Trh4ZvQJkh6uzRxy6-SVR9fRWL7sN4fEc_YDEiJegNkwAauWrGYxy9pStyF0J3s6Qr0n--YlqQURj2KLPvXjZ1xDFs7Uq2GRy4miyTYov5K7ZqP-mBS8FhAf4-rrRgSEvT9V5sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد تنظیم مقررات و نظارت بانکی ترکیه مجوز فعالیت شعبه «بانک ملت» ایران در استانبول را لغو کرده است؛ تصمیمی که پس از توقف پروازهای شرکت هواپیمایی ماهان میان ایران و ترکیه و مداخله نهاد ناظر در مدیریت یک بانک تحریم‌شده دیگر اتخاذ می‌شود.
براساس اطلاعیه منتشر شده در روزنامه رسمی ترکیه، هیات نظارت بانکی این کشور روز جمعه ۲۷ شهریور ۱۴۰۵ لغو مجوز «شعبه مرکزی ترکیه بانک ملت مستقر در استانبول» را تصویب کرده است. این تصمیم روز شنبه ۲۸ شهریور در روزنامه رسمی ترکیه منتشر شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/78450" target="_blank">📅 16:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78449">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eA3ceXp8DFwXoY-je2FVqyymgunGTVzKPOixpW42w7KJIsItqh8Mdv1I-RtNxJxQ15q8PIqHQ9lirmptxXGfscGcCEMJe4JDNeaIEk9f17tgc2ClUT_oi47tJZrU4fCcrrIKlEskIIsd0EGEUWjlzneWneCseHcpe1Quginc9UdZ3d-7Z2E53Fp-JA4QBYounZ2B8OMcFI8q5AXwaBOfKkFnTiPFf6nSkUSs_flLi6-YRwImEZ6L9ZTgZMlJrQ3surn7ZUf6YwhT6h7ZJiA5vsMXFnuhRBkLv0zat8oyUpPRTkaLVxrjrOJPtOr0kZaxoR25TFQhGdwtSDKKeB5XRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده، روز جمعه ۲۷ شهریور و اندکی پس از تایید کنگره در هفته جاری، لایحه‌ای را امضا کرد که مجوز اعمال تحریم‌های جدیدی را برای تحت فشار قرار دادن روسیه بر سر جنگ در اوکراین صادر می‌کند.
این قانون همچنین تحریم‌های مرتبط با ایران را نیز تمدید می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/78449" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78448">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJCsLHuJdxHf5fDwz8V8GTRYZVKKDJnwag6I7hP8mwPjieh-leLh4I8h7ZyrJT3k2dDH0uOLgBbNAwr4De34XfvukiIw26C0I-xhVenS1jtJ7ZURwz6-RgV-7WR4q0SoafZhPlTrmgl72-b7WlhLy9TPBHRyS4_L02_fQYLXnRCoQvezI-I3KfeUUlTDW8oW30nsDjaJ_4igFjHIhP9VccxHEQwHCHxg6TrQcyNAkyhYq1eps7pcWRCBPsOcAir_aZIXH8bRvVQQxDXvWe-4ofTm2BZ8FLZu38xy2apIvIgwusT3OrUQuw1Oa2Qrsc-OcotCb4CJxiBvGZRzt5tlQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اعدام «حسین پدران» با اتهام «جاسوسی و همکاری اطلاعاتی به نفع اسرائیل» خبر داده است.
براساس گزارش رسانه‌های حکومتی در روز شنبه ۲۸ شهریور ۱۴۰۵، حکم اعدام پدران پس از رد فرجام‌خواهی و تایید در دیوان عالی کشور اجرا شده است. محل و زمان دقیق اجرای حکم اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/78448" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78447">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cajxZws99EpjuNCE7ApPnvJTY_zm2QtOQVoDOa_M4nr_sYlm4_R3yfF_V0kGznxi1_pSgOn2kc_XfI8Bwyvezb7CfiOQGFn-uOolCbbY9mkX4cHVt6IRtudbA8nGj4U-ZrGrtwTUaVbRqvl0zryZFiYuH_nh1azuJS2SnHKRnqC8IIlsWU70_mDDWpm5g0rEAVbhMx-7RDjaR-jMQY9fjqUHV7aKd_7kj95y_Q6oZA0Cvu0yxZ2JI6MaNzTtTREvMtEp_ieBOcedLn9Ma16_tHyKDVwJrpnkFHacSmH_9QiO2vsuib2vMVklbOc_xgLCK3pWuw1OCT9Yrka_c6_TPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث‌سوشال اعلام کرد آمریکا با دانمارک و گرینلند به توافقی دست یافته است که کنترل دایمی امنیت و تمامی نیازهای دیگر در گرینلند را در اختیار آمریکا قرار می‌دهد و به تمامی نگرانی‌های متعدد ایالات‌متحده رسیدگی می‌کند. او گفت این توافق هیچ هزینه‌ای برای آمریکا نخواهد داشت.
دفتر نخست‌وزیری دانمارک نیز اعلام کرد انتظار می‌رود که گرینلند، دانمارک و آمریکا هفته آینده توافقی را برای تقویت امنیت در منطقه قطب شمال و اقیانوس اطلس شمالی امضا کنند.
ترامپ گفت: «از این پس هیچ دشمنی از سوی آمریکا نمی‌تواند بدون تایید کتبی صریح ما در گرینلند پایگاه ایجاد کند، حضور نظامی داشته باشد یا سرمایه‌گذاری‌های حساس انجام دهد.»
پیت هگست، وزیر جنگ آمریکا، نیز گفت: «ما بلافاصله روند حضور نظامی گسترده در بخش مناسبی از گرینلند را آغاز خواهیم کرد؛ بخش‌های مناسب زیادی برای این منظور وجود دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78447" target="_blank">📅 04:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78446">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/da1aa0c490.mp4?token=Wm40UQKFLK6v5i7h1Ga9DibQqbiV0i7ayQTv5uw4WI7EuHikOga-TM_QXYB8OB3SN_x4tFrIwOV2StPlU0tZNDQtAONPL8vRUAccffERXdTtJIDgxbXkyazzgDDq2Tc4ii6mPyep0gI2_5D2yRoKDpJRpNGrUPvNW_UkxofEpMXpq7N44oV6xpZtaMjBrVkhppJr6ZDXQ2Vd185mT8XhZTaQlJqUDlw4uXMrhhf0KKi9l82CN4SLG2fYmsymto0pwcwR_SFLxgdZxI3IW1QGDSVmqnWjmq4fE05oNSwqpr3r3s5TixLJLPoq9WRCATEqI3Ymd7kxAWFJ_lH3N2-gUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/da1aa0c490.mp4?token=Wm40UQKFLK6v5i7h1Ga9DibQqbiV0i7ayQTv5uw4WI7EuHikOga-TM_QXYB8OB3SN_x4tFrIwOV2StPlU0tZNDQtAONPL8vRUAccffERXdTtJIDgxbXkyazzgDDq2Tc4ii6mPyep0gI2_5D2yRoKDpJRpNGrUPvNW_UkxofEpMXpq7N44oV6xpZtaMjBrVkhppJr6ZDXQ2Vd185mT8XhZTaQlJqUDlw4uXMrhhf0KKi9l82CN4SLG2fYmsymto0pwcwR_SFLxgdZxI3IW1QGDSVmqnWjmq4fE05oNSwqpr3r3s5TixLJLPoq9WRCATEqI3Ymd7kxAWFJ_lH3N2-gUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه ۲۷ شهریور در گفتگو با خبرنگاران در کاخ سفید گفت جلوگیری از دستیابی ایران به سلاح هسته‌ای موضوعی است که به آن «بسیار افتخار» می‌کند و ایران دیگر سلاح هسته‌ای نخواهد داشت.
ترامپ با اشاره به افزایش هزینه سوخت گفت تحقق این هدف ممکن است مستلزم آن باشد که مردم برای مدتی هزینه بیشتری بپردازند.
او افزود: «اگر مردم می‌توانستند بین قیمت پایین‌تر بنزین و اجازه دادن به ایران برای داشتن سلاح هسته‌ای رأی بدهند، فکر می‌کنم نتیجه با اختلاف بسیار زیادی روشن بود. مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد.»
رئیس‌جمهوری آمریکا همچنین گفت انتظار دارد جنگ با ایران «به‌زودی» پایان یابد و پیش‌بینی کرد پس از پایان جنگ، قیمت بنزین به سطح پیش از درگیری بازگردد و «شاید حتی پایین‌تر» برود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78446" target="_blank">📅 04:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78444">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=nSR5aBRSNejWszKGhpbTzZP0b_30gYUDa34YTmpUKdpqHEtcnXOsRNo5ssbVNxaRdRWe3JZd9WUi0gyDcFGlP74810bP0QUsRx5H2trHhNyrrQy6SCIQPvSmcX6A7WP71bxBqZLmzjP7PIQuk4cNSW4GZXE4epZBSUhtPP5uHRmsn4Mouu193TKS56RjFyMoQ6Og_mTNscdV5bCQB7A6jS0In6sB8hvvxEBkxzE5ujVEaXuprPUfSup4fCPuHkOdfvgqP-5het3VNlXse2_yJHRj1D3s7400ZKPuKEeHRlrsxZpSzVWmZWqlzzPELgd9iZvnN0JQONlBMItf1KjZeA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=nSR5aBRSNejWszKGhpbTzZP0b_30gYUDa34YTmpUKdpqHEtcnXOsRNo5ssbVNxaRdRWe3JZd9WUi0gyDcFGlP74810bP0QUsRx5H2trHhNyrrQy6SCIQPvSmcX6A7WP71bxBqZLmzjP7PIQuk4cNSW4GZXE4epZBSUhtPP5uHRmsn4Mouu193TKS56RjFyMoQ6Og_mTNscdV5bCQB7A6jS0In6sB8hvvxEBkxzE5ujVEaXuprPUfSup4fCPuHkOdfvgqP-5het3VNlXse2_yJHRj1D3s7400ZKPuKEeHRlrsxZpSzVWmZWqlzzPELgd9iZvnN0JQONlBMItf1KjZeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان با برگزاری
رزمایش "جان‌فدایان"
تصاویر بالا رو هم تولید کردند:
مسابقه دوی ۱۰ کیلومتر تهران روز جمعه ۲۷ شهریور با حضور گسترده زنان برگزار شد.
در تصاویر منتشرشده از این رویداد، زنان با پوشش‌های متنوع و اختیاری[تر از قبل] دیده می‌شوند.
رقابت امروز در «بوستان ولایت» و در دو بخش جداگان زنان و مردان انجام شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78444" target="_blank">📅 16:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78434">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IPKK7I0Qs7jehbrbBX2uElK7n14LjYr9_FPvbxURQzlA86yH-RY7DTjamojzY0Se95CD3MhnZz6gykRGgzu0vWpO6oPQoyGMs0D38zU9NKlwZJW8aiF_SnRIgj-MNgg2rKXuU7Sm1qQ1EsQx-0Z9jErATy_nEJXF7hcCc8UqGZ_Ez72xNL4k6egwvLYuA4lRPa6Y2iACnA8NKEOofk3TP8LsXhKqgOfir8B87nWZFnU1sJRj_DBMFl8heqKnWTyNFFH70baOBd4o5ry825WD2Me4VOeIrIQf-tVrzK_7HbPHtamNWHZXcgva04bzd9DV-bgh27Ksg0rEnIZgLlQAwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S-UPMZgOe6rYAGWNgEawdJokzHFZJoYr7dRUZ-fEPFeccLfkSI_0rVLulEX_KDJajyMCBiXhQYBZrTulXDpKR49FDoVBN_bxaqkdKjThf7UrkQhLr29g4_aHjL8vsM0l0LEJTqSpVIW-cpigNRjPl0KiTKGwysc3d-nNOJhQACpL2-CUFRFTCGZ2PUdyJDhmXYKykrWCYyJdL9XnO5hLAPZcEgt5YQ09qvIDuw4HUTf-CwUkqjnrSo6MRLtjjIykY17EMshoU9aXiBs4AWrY1aY4taukPHHLMjUP_5WNiVN6Z9fnyV53QXlnuNiTEiOgDYHIGsfceOsQdlolTuSJWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J1qQ7WzG1sKSiRzrRsneYv4c8YSQHQ7zp0Le6qvefJbwrGFwJH5Xp0IdCAYA0N_MEbZ7NuWnU3cbn-rvkOmv5OwArmB8Pohx3htmsJPZxGNLu5KuyBJZJ2OoXbnxss1QXnKt78A44ZFgOPXURoDw1RnPFf8EGoUFNmbhXC6HzmTUpy8Vm4htnsPICfD5jB5VhQZDP24UDrZjzwCys47Nir2sP9XtUBhP6COolE_Ln7IdocW3vhM_Af0nU_AP4vyp6QOZtOWsDJSYPOGyORViWruLqtdvaetoTeSIkJM2VHE5AkQD2WuirBTMuBsgOAP9P87AaEd26HaFXYNocT3etw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sqyrnxxdHK3HziiqJxYo2CxNNNsK8RCXcck89B_q2VZksbZC2uMNwmJ5QZ89xkoFQkgLJZSEvgWMjd2jUJM6aVxb0v7GFFkvNadhSWd9mGeeKaz6TsgLKrB6wj7JEgCvVRGWWJzJBObWpSRHkRQsnFJmxZiCyvgfN8Ht3BQBlgI_3IPFPv4uf_Iao4KGq62HRRPQHUEzJ-joq-GaFUupvvNNQzrUYWv836gX1PZaJ8sAFsmwHjiZbrr-6YUeuNzuJ2l5t5_lhPqkQp6rim53XxLkJYPt_a2LYTfnMa0hmenWP-0zt04dZga0moxgowAX7vgYxJdw3KHuTQb6DJUM_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v1fepQ6UDv8lPTzF1Zor7YzpiTIfiFsiZgDjTgZzql2RmK9ASioxJcvVmMNKt_YP0Vfcbxnn0cPyE1YiZ6tG_mAjcJt2rasCihhMZ3DEPe_KlgTV6DK_5TXKv0pF2mJSD-zGC7jNAHqNUuv0Ad5RhOFGoTieUFZkrqcvVhO6Kw7xVs_p_3eohBcWm4iU_fIueaymeVp-Lx3dtojoi9GdJD8bbGXqVxyk_5KmFaoODEByqjJ62z1QxqaNjQ4_xBUlSydcJirR7FjsLrKWsrQnXS5duhc3YtHa9zv5pqZZowQCBk_BSLM7mqXWdBq5EG7trtFEvu8Q_AL02DbIOC3oNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e40dc6c35c.mp4?token=k1b9vv07qGn-TauHpJdoAo2yCvpvwI7ziiVezF1yJaaEmopP_Ld1akvUR7xXdwQuhqy5ZxbIbhDo76uNoreG_tAdCdH6HrK29l2LVgPFhKirEiZQSc3tbLUbjSHrDOdHpdwsFar1sOGm4uSrlgfVnzymOtvAytJB1GRrtkwtkXlJLSLmF7E_iAdOGAYwjfCNAfdI181p_HhodvJgQilitpxq5k2ZtZ4AMK8glQn-kyJQOYehyzU8V0l8zInTIim_HFfIgHtjJidx5LYGEBTf1ROXW0emgUAF-sgLtbd4Eqw16zxb842qUNUZs3D_mnqcX6MdVtaxOsL6TUqSgaYymw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e40dc6c35c.mp4?token=k1b9vv07qGn-TauHpJdoAo2yCvpvwI7ziiVezF1yJaaEmopP_Ld1akvUR7xXdwQuhqy5ZxbIbhDo76uNoreG_tAdCdH6HrK29l2LVgPFhKirEiZQSc3tbLUbjSHrDOdHpdwsFar1sOGm4uSrlgfVnzymOtvAytJB1GRrtkwtkXlJLSLmF7E_iAdOGAYwjfCNAfdI181p_HhodvJgQilitpxq5k2ZtZ4AMK8glQn-kyJQOYehyzU8V0l8zInTIim_HFfIgHtjJidx5LYGEBTf1ROXW0emgUAF-sgLtbd4Eqw16zxb842qUNUZs3D_mnqcX6MdVtaxOsL6TUqSgaYymw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین طائب، رئیس سازمان بسیج مستضعفین، اعلام کرد صدها هزار نفر از ثبت‌نام‌کنندگان پویش حکومتی «جان‌فدا» در تهران سازماندهی شده‌اند و روند الحاق آنها به گردان‌ها و یگان‌های دفاعی جمهوری اسلامی آغاز شده است.
طائب روز جمعه ۲۷ شهریور در جریان رزمایش موسوم به «۳۱۳ هزار نفری جان‌فدایان ایران» در تهران گفت برای این افراد دوره‌های آموزشی مقدماتی و تکمیلی در حوزه‌های زمینی، هوایی و دریایی در نظر گرفته شده است.
این رزمایش از صبح جمعه در مسیر میدان امام حسین تا میدان انقلاب تهران برگزار شد.
@
VahidHeadline
حسین طائب، رییس سازمان بسیج، جمعه ۲۷ شهریور در همایش «جانفدایان ایران» اعلام کرد نیروهای آمریکایی «به‌زودی با شکست از منطقه خارج خواهند شد.»
رییس سازمان بسیج گفت: «جمهوری اسلامی از تمام ظرفیت‌های راهبردی و تنگه‌های دفاعی خود، از جمله تنگه هرمز، با قاطعیت حراست کرده و دشمن را وادار به تسلیم خواهد کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78434" target="_blank">📅 16:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78433">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nts3a1Z8wfHHXszJXD-lAw84HBKd4Eyux3EQwmB9mCAQiuO701nHwP17Xl1AQaUlhe9wJvZxK_Tr8LjJstcLs0gC2B_UFp8TbrTNK7xHMN0aRA8MCBzh_cr8LHBU-dmEmWIAxc1cba-Ywo8yAoedv0B-CicMJtCdze-VG5wYDqMN4MEIjR32PXBb-XOnYGxJvZ-ZFz1QVKJow2DwtIXUkQ0jdWtjui8CEOIoSzqEP135q5Th71iQ5mhTzd_D_cV36qlDTIXoQVdd8o69s5wLuYQ_eEZjB7qo2blYmNpzx-dNZeh29rqC6rvaeomeWqxRJsFUYLXxhYnw7O4fRz5MOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور کره جنوبی اعزام نیرو یا تجهیزات نظامی به خاورمیانه را در صورتی که به مشارکت سئول در جنگ منجر شود رد کرد، اما گفت کشورش ممکن است برای حفاظت از کشتیرانی تجاری و انتقال نفت در منطقه نقش بیشتری بر عهده بگیرد.
لی جائه میونگ روز جمعه ۲۷ شهریور در یک نشست خبری گفت: «هیچ اعزامی که به ورود یا مشارکت در جنگ منجر شود، انجام نخواهد شد.» او تأکید کرد کره جنوبی برای چنین هدفی «به هیچ شکلی» تجهیزات نظامی اعزام نخواهد کرد.
او در عین حال گفت سئول باید مانند دیگر کشورها «حداقل اقدامات لازم» را برای حفاظت از کشتی‌های تجاری، انتقال نفت خام و امنیت شهروندان خود انجام دهد.
دولت کره جنوبی در هفته‌های اخیر در حال بررسی احتمال اعزام نیرو یا تجهیزات نظامی برای کمک به تأمین امنیت کشتیرانی در تنگه هرمز بود.
دونالد ترامپ، رئیس‌جمهور آمریکا، از سئول به دلیل آنچه حمایت ناکافی از تلاش‌های آمریکا در ارتباط با جنگ ایران خوانده، انتقاد کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/78433" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78432">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qEk8VmVpQamPIxtQK-1zwIfb9Vu5rlq2AmDCinAgHfCkmjP4A7FrzyQWKcRAi_2kBUYnv7cEaz4KK9PBGcuyyf6Gra8ofzsdhgxLcMsUevVt3TIzHcKXLkA_K76Jxej0FfgUSCHNkmwnjzlhEeVYwIn26Z5NnZSjrSO2fWJkt-b_rhh4qk54BkvxMPEksELnfruGWXhmh2JtsySz1J6_pdZZAzVIRZlsUPzNQcOf0T-H19AgLstLfA6YYX5yYPD_LoT8SIlGJa118Eo47WU19h7nW18VuY3ytwhQd9Rqgoldp9WssEXQhI7-mlOC3wR-nCEa_l7fhkqv0Uuf004e0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد یک نفتکش با پرچم توگو را هنگام عبور از تنگه هرمز هدف قرار داده و مدعی شد این شناور پس از اصابت و آتش‌سوزی متوقف شده است.
@
VahidHeadline
UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی درباره وقوع یک حادثه در تنگه هرمز دریافت کرده است.
افسر امنیتی شرکت (CSO) یک شناور گزارش داده است که یک نفتکش با پرتابه‌ای ناشناس مورد اصابت قرار گرفته و این برخورد باعث آتش‌سوزی در عرشه شده که اکنون مهار و خاموش شده است.
گزارش شده که همه خدمه در سلامت هستند و در حال حاضر تأثیرات زیست‌محیطی این حادثه تأیید نشده است.
UK_MTO
در گزارشی دیگر نوشتند:
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) یک گزارش تأییدشده اما با تأخیر زمانی درباره حادثه‌ای دریافت کرده است که در ۱۶ سپتامبر ۲۰۲۶ رخ داده و طی آن یک نفتکش هنگام خروج از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
گزارش شده که خدمه در سلامت هستند. گزارشی درباره ارزیابی خسارات و تأثیرات زیست‌محیطی منتشر نشده است.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/78432" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78431">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRyiQ598I0un321Tlsg9mr1YhFyxgc7tsKX1TVVoY1oIfS0Vi-u-aqGXx-7YGGWpboQe56crYkzNXrgaKjx8V6qZEJ2Hpv9zkG3Ur79HV_upYqiViwvkV1hzbCCLA_gwo31mGJ55sXMUI_N8dUmJCiY6nmwiG4AVk3Y44hpZH6zdn1X3tupNXAKg_hmD4d010k9NmTc_jesGeelUFnf1jiAvRMAOrhIiblkkeb90ePgQuN-oceLU4TgK2V4_Sh0ki213m7Sb9wVcLe-Lv9v1fNojeirPmlbC4bjd3wQf5WFXVPSzkWPWSWJjNexJclSVYT7vF3ma3FY6aY4a2Pb7Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد کرمی‌اسد، جانشین پلیس راهور فراجا از جان‌باختن بیش از ۱۶۰۹ نفر در تصادفات جاده‌های برون‌شهری در شهریورماه خبر داد.
به گفته این مقام فراجا، این آمار به‌طور میانگین به بیش از ۵۰ نفر در روز می‌رسد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/78431" target="_blank">📅 15:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78426">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ph4EiguTQGz08yCzR9cpRqDymzrccu4NkEuTi5-V6VQXw7febVKhVraQRuFh4yPTnvzb77jQYvGNYzpEDVZHMdLdWEfXpO98E2yWf8iFnA_AJXAuJIZf6AlujQHKzBUwb7y9VDmexnkmLW7FwMJiofWi9Eqhq6M3ei-I7RmC1IFgsiXH34mBT6E0eP2ujw6M-AdO8xWlZ1BGNHz0rUqDO4J7P-deIN5Ebfhi3c6M5eS5_82Aa5lx86mjL8Ux6FLeymkssTTaNGiXmPKhAeX_-mrhoWiXkCdSffDZNaGK25m9mygQ71fuLodJu59icWhnEeUwM8IQz-OtulFDpypYSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e616598ff4.mp4?token=n2vVT950JFSdNWWGaQPtIR1D_9XYFKbjbnHzSrYD7gVHp-XWIksaeVV3ZINNJ2Y1R7GAwoeIhCEigNczT6ABgtIe3iAsfMHnwJupvnU8Y2O5pHNRsrh5EkBV82K60na5ncAVnxebA5dMeERzTr3pRq5AzXFU6SWQOMVPnSWRqzTYFU3YBgrXcr1OFZCc-Gg6GknxOzr7Q_ArGZxesH7gJUVQixDwdCZ61-m5DbMvyeocdW-vP5QB-_R3yYeGsmnKmuh2MNCVRMDvQiNFGhFZwHST5iWMz7V4dYwBPl10CW7cipEYdF2M0KfETdkYRdOieAZuvZLOMxfsibpdGV2Xbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e616598ff4.mp4?token=n2vVT950JFSdNWWGaQPtIR1D_9XYFKbjbnHzSrYD7gVHp-XWIksaeVV3ZINNJ2Y1R7GAwoeIhCEigNczT6ABgtIe3iAsfMHnwJupvnU8Y2O5pHNRsrh5EkBV82K60na5ncAVnxebA5dMeERzTr3pRq5AzXFU6SWQOMVPnSWRqzTYFU3YBgrXcr1OFZCc-Gg6GknxOzr7Q_ArGZxesH7gJUVQixDwdCZ61-m5DbMvyeocdW-vP5QB-_R3yYeGsmnKmuh2MNCVRMDvQiNFGhFZwHST5iWMz7V4dYwBPl10CW7cipEYdF2M0KfETdkYRdOieAZuvZLOMxfsibpdGV2Xbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با انتشار ویدئوها و تصاویر مختلفی در شبکه‌های اجتماعی از وقوع درگیری مسلحانه در بامداد جمعه ۲۷ شهریور در شهر زاهدان، خبرگزاری برنا از کشته شدن یک مأمور نیروی انتظامی در این درگیری خبر داد.
ساعتی بعد خبرگزاری فارس اعلام کرد که در جریان این درگیری دو نفر از مهاجمان کشته شدند و یک نفر از آن‌ها دستگیر شده است.
وب‌سایت «حال‌وش» هم که اخبار سیستان و بلوچستان را منتشر می‌کند، می‌گوید از حوالی ساعت ۳۰ دقیقه بامداد جمعه در محدوده خیابان دانشگاه و اطراف خیابان دانشجو زاهدان به مدت دو ساعت تیراندازی رگباری رخ داد و سرنشینان یک خودرو پژو ۴۰۵ هدف حمله قرار گرفتند.
این رسانه به نقل از منابع خود همچنین افزود در این درگیری «یک فرد مسلح، سه نیروی نظامی و دو زن رهگذر مجروح شدند و چندین آمبولانس به محدوده خیابان دانشگاه و اطراف خیابان دانشجو اعزام و در برخی خیابان‌ها ایست‌های بازرسی برپا شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78426" target="_blank">📅 06:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78425">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxbVc_PhXV2vXfgJPbSJNNFv04FaeAWP1ODgWI_4xjt-tjnVSCOc0LNupluEmtjh1JRPJcV4C2q5TAlcAyauGOzj-iFSW51wN4kugpE9S300BmHBHjybFFxkd0yJZsjfFZ9ydyjF7eu-iQW6YveIEeGX1ZjO9HmPICkdvVtmsCsPx5Ot55tCjQ4vJuo9qE9y1ImTcMfDO8VjvG6SX-_e2KGqnzEoHMblVXGD7aOYu5UtVzH1saWhOtpO4yFOQD-uPhmJ9N8Rbe4FYGeoJ6fL3guCxDYSvD_K1x6Z-Nkz4VCLZxdlZW6wFFHNQyzOvtQVq5KxkFHA09shkYQvvbfFJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران بامداد جمعه ۲۷ شهریور در بیانیه‌ای اعلام کرد نفتکش «ترند» با پرچم کشور توگو، شب گذشته هنگام تلاش برای عبور از تنگه هرمز هدف قرار گرفته و پس از آتش‌سوزی متوقف شده است.
سپاه پاسداران در این بیانیه گفت که این نفتکش قصد «عبور غیرقانونی» از این آبراه بین‌المللی را داشته و هشدار داده است شناورهایی که به این شکل عبور کنند، با «نابودی» روبه‌رو خواهند شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78425" target="_blank">📅 02:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78424">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NGYGYlibuPs9csrbcPpQ9Tk8LwxfEjqyhRTaP-7_zsdj-pN877ZC37fri0fyu4F1ZYhKrlFr1sgKB1xKWuL-R9B-au6AMU_vfCUPsC80QOHkhm-8patL1WKp79Khg0kg8DBCRBNvWlqNhZYwbyvxY9sR3Xyp17VdpI0Q2K-O2OHByRNX-DpIXtPsMT0hMwQi6MAx-CsS8ge91pbRatqNEt0hCD2TtEuOg_aTjo30YxU6BSWHgRtCTJ8iq2-uqMVe4cPk6Jmf0hM-OI1ebM8mgOf-t6EepsQGdsjPpeQZe_VMl_PGOWS87O9pcnfEEzGJl4BVxr345mJqT6WMkG_2Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا  گزارشی از یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایل دریایی شمال‌شرقی خصبِ عمان، دریافت کرده است. گزارش شده که خدمه در سلامت هستند. تا زمان انتشار این گزارش، هیچ پیامد زیست‌محیطی تأیید نشده است. مقامات در حال تحقیق هستند.
به شناورها توصیه می‌شود با احتیاط تردد کنند و هرگونه فعالیت مشکوک را به UKMTO گزارش دهند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78424" target="_blank">📅 23:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78423">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iCRc5gjz1in9tSwFaiB09v_FXRpoMTniZ22tsypT8Ue1Y-SL6Eis0cSsb1gaG0AjmffNHVNIQgVr6U3Xrf4xLRCp-A5F4dVvR5tgOa-zn-CLbrImhNNMcU_b0eqWg0jbpowepNAAkeP0_OMcKg5jQsZcNqm-hv9XzsCOWeDwgCji6f4E0_1m7VsA7XKzx4S-65ylwi8xZASeEYc7GjTs1DTluKXqfVs4qRK93DYA3elNtG3nIHWcmIrdH7OYQczbzwj2esYdjw1aHDTweaqFjLn_A_OoHv89DpKglX_gyTTAgiXB8H_4kfhN5VCekvNRpUW1KR5rKxAM2dXE1tTgKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس می‌گوید در جنگ ایران به یک دوراهی بزرگ نزدیک می‌شود
ترجمه ماشین:
رئیس‌جمهور ترامپ روز پنج‌شنبه به اکسیوس گفت که در جنگ ایران به نقطه‌ای حساس نزدیک می‌شود و باید تصمیم بگیرد آیا برای پایان دادن به درگیری، حملات گسترده را از سر بگیرد یا نه.
▪️
«تصمیم بزرگی پیش رو دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر اتفاقی ممکن است برای من بیفتد.»
چرا مهم است:
اگرچه ترامپ پیش از این نیز تهدیدهای مشابهی مطرح کرده، اظهارات تازه او در آستانه دیداری برنامه‌ریزی‌شده در روز سه‌شنبه با رهبران شش کشور خلیج فارس در حاشیه مجمع عمومی سازمان ملل متحد در نیویورک بیان شده است.
▪️
این دیدار می‌تواند مرحله بعدی جنگ را شکل دهد، از جمله اینکه آیا بار دیگر برای دیپلماسی تلاش شود یا اقدامات نظامی تشدید شود. اگر ترامپ بخواهد عملیات رزمی گسترده را از سر بگیرد، به همراهی متحدان منطقه‌ای خود نیاز خواهد داشت.
▪️
رئیس‌جمهور در روزهای اخیر چند بار گفته است که جنگ به‌زودی پایان خواهد یافت. برخی مقام‌های آمریکایی هشدار می‌دهند که این درگیری به بن‌بستی ناپایدار و «نه جنگ، نه صلح» رسیده است و معتقدند اگر تا آن زمان توافقی حاصل نشود، ترامپ ممکن است پس از انتخابات میان‌دوره‌ای دوباره به عملیات رزمی گسترده روی آورد.
آنچه او می‌گوید:
ترامپ در این مصاحبه روشن کرد که می‌خواهد از نشست سازمان ملل برای شنیدن مستقیم نظر متحدان منطقه‌ای درباره گام‌های بعدی جنگ استفاده کند.
▪️
ترامپ گفت: «می‌خواهم بفهمم در چه وضعیتی هستند و اوضاعشان چطور است. ما خیلی از آن‌ها محافظت کرده‌ایم.»
▪️
کشورهای شرکت‌کننده عربستان سعودی، امارات متحده عربی، قطر، بحرین، کویت و عمان هستند.
▪️
ترامپ از گفتن اینکه تصمیمش درباره مسیر پیش رو را قبل یا بعد از انتخابات میان‌دوره‌ای خواهد گرفت، خودداری کرد.
زمینه خبر:
در اوایل اوت، ترامپ پس از آن از ازسرگیری عملیات رزمی گسترده خودداری کرد که عربستان سعودی و قطر ابراز نگرانی کردند ایران در اقدامی تلافی‌جویانه تأسیسات نفت و گاز عربستان را بمباران کند.
▪️
از آن زمان، ترامپ رویکردی «کم‌سروصدا» در پیش گرفته است: تعلیق مذاکرات با ایران، آغاز کارزار تازه تحریم‌های اقتصادی، ادامه محاصره دریایی بنادر ایران و متمرکز کردن ارتش آمریکا بر بازگشایی تنگه هرمز و افزایش جریان نفت به بازار جهانی انرژی.
▪️
ارتش آمریکا عبور نفتکش‌ها و کشتی‌های حامل گاز از تنگه را به‌طور قابل‌توجهی افزایش داده است. با این حال، ترافیک همچنان پایین‌تر از سطح پیش از جنگ است و قیمت نفت نیز همچنان بالاست.
وضعیت فعلی:
به گفته مقام‌های آمریکایی، ترامپ و پیت هگست، وزیر دفاع، به ارتش دستور داده‌اند سطح نیروهای خود در خاورمیانه را تا پایان سال حفظ کند تا برای احتمال بازگشت به نبرد تمام‌عیار آماده بماند.
▪️
این مقام‌ها می‌گویند ترامپ باید به‌زودی درباره مسیر پیش رو تصمیم بگیرد، بخشی از دلیل آن این است که ارتش آمریکا نمی‌تواند خیلی بیشتر در وضعیت فعلیِ انتظار باقی بماند. یکی از این مقام‌ها گفت: «بالاخره در مقطعی باید تصمیم بگیرید که هدف نهایی چیست.»
▪️
ترامپ به اکسیوس گفت از اینکه محاصره دریایی مانع صادرات نفت ایران شده، بسیار راضی است. او گفت: «از وقتی شروع کردیم، حتی یک کشتی هم به ایران نرفته است. تلاش کردند و ما آن‌ها را منفجر کردیم.»
▪️
رئیس‌جمهور افزود که ایران مستقیماً با آمریکا در تماس است و گفت ایرانی‌ها همچنان خواهان دستیابی به توافق هستند.
تصویر کلی:
کاخ سفید همچنین در حال کار روی یک راهبرد پس از جنگ است که خواستار تلاشی منطقه‌ای برای مهار ایران و هم‌زمان گسترش عادی‌سازی روابط میان اسرائیل و همسایگانش است.
▪️
هرچند این طرح هنوز در مراحل ابتدایی تدوین قرار دارد، هدف آن هدایت رویکرد آمریکا در خاورمیانه پس از پایان جنگ ایران و در دو سال پایانی دوره ریاست‌جمهوری ترامپ است. دو رویداد بزرگ بر این برنامه‌ریزی سایه انداخته‌اند: انتخابات ۲۷ اکتبر در اسرائیل و انتخابات میان‌دوره‌ای آمریکا در نوامبر.
چه چیزی را باید زیر نظر داشت:
وقتی از ترامپ پرسیده شد آیا هفته آینده در نیویورک با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد، گفت: «شاید.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78423" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78422">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9zuG-zpnRHofguS29bfFNzgScxNA8ltY0MwBBYL11Amwg4kqAT37yKSjFEjSlc-Xv6JwBs9xaIRwIC12vdy-O9a1_Wcql9ajEDaNGArWL9hzqZ4jiCEPi2z8TcviM93aNWFVv7GIyqD3hM04DfgKLB0DGIV1kctKc_GGrjLuRpv14Ivj0ZF8js6-Pco4M_CdXz5-2vfxXH31-xjmmY4htLjOUByjTMFm-7FcsH3qePy-LI_LaTK6-5Ulj4vJaZioYpn7d5BuEz2zY36aAgGHPAQuUgeEJTbjssMrPlEHhLT3HxTH4h9SZ8AoH-yXuyQZfZtU27QlTTauGc_wBqAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس نیوز پنج‌شنبه ۲۶ شهریور به نقل از مقام‌های آمریکایی گزارش داد نیروهای جمهوری اسلامی در روزهای اخیر دست‌کم دو پهپاد ام‌کیو-۱ آمریکا را سرنگون کردند.
مقام‌های آمریکایی که به شرط فاش نشدن نامشان با سی‌بی‌اس نیوز گفت‌وگو کردند، مشخص نکردند این پهپادها در کدام بخش منطقه سرنگون شدند و از کدام مدل ام‌کیو-۱ بودند.
این پهپادها برای ماموریت‌های اطلاعاتی، شناسایی و نظارتی طراحی شده‌اند و قابلیت حمل موشک‌های هلفایر را نیز دارند. سی‌بی‌اس نیوز نوشت این پهپادها در تنگه هرمز می‌توانند برای نظارت مستمر بر آبراه، رصد فعالیت‌های نظامی جمهوری اسلامی و شناسایی تهدیدها علیه نیروهای آمریکا و کشتیرانی تجاری به کار گرفته شوند.
بر اساس گزارش دفتر بودجه کنگره آمریکا، از آغاز جنگ آمریکا علیه جمهوری اسلامی دست‌کم ۲۴ پهپاد ام‌کیو-۹ ریپر به ارزش تقریبی ۷۲۰ میلیون دلار از دست رفته‌اند. یک پهپاد ام‌کیو-۴سی تریتون به ارزش حدود ۱۵۰ میلیون دلار نیز منهدم شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78422" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78420">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GYlZmovQAjlsf2CwJP0V2dXAmUUJLZU1YnDEtAfEryVzh_GqfdKfTTW_PSrTb7Zh0wdW0b8-TFHldNYVIaIs3RNi-dN-lBzPdCcDDifkNY600Y-wxQz4ygB9jYunOdCJvUbunt6tW5a-Dit0qWr2ZY1lilRVTQhDxquMjh-PSfexdAkGuVOkQoDlXjHM3yEArvpVjz7oirLwd_mmIdye-op7acMcg2JUnbmc5L7qi6Qvy0BRDnEqaufeNZMdQ8zreDLzowE5-ptAva_KSX13MyV3LzlMi9mAKM_EkKjrxx7Z5ut3HiAOIWyMACjvD7VKV7BsD6gCf1K448wcQaVLQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37ae7c8ac7.mp4?token=vg44WQ-PlSYC3jlqOn5JvgqY7f7HX0hmoWjo9mGOEz-IfBFXGQVoG-92QhqsOwnAwkq4QMZhYw-aTSY6AGXtsqXyJDfMMwbQPxHBii1EPyXKwuDhwz7mMI4cqYoM4vyKRxqGFRUAYRA4EO9XkOrkMAVQ6fv_P_ErifniclGuw-Zj9lCP0mVU2gTynoex9UzkIbCdYcVr8mZU-f7Pq0T1cTgHlGm6eeSdVXxrYGQs6AR8BcL8w5ZeJQnz9t4imib7PJ3UtqpdW2MPpGevIFqsa6WLZeTS0Dq4C9w4wG_0wqG_Ft5mrOZzagbu_X42xR7LmJIp7YWJtOacW222PTtSqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37ae7c8ac7.mp4?token=vg44WQ-PlSYC3jlqOn5JvgqY7f7HX0hmoWjo9mGOEz-IfBFXGQVoG-92QhqsOwnAwkq4QMZhYw-aTSY6AGXtsqXyJDfMMwbQPxHBii1EPyXKwuDhwz7mMI4cqYoM4vyKRxqGFRUAYRA4EO9XkOrkMAVQ6fv_P_ErifniclGuw-Zj9lCP0mVU2gTynoex9UzkIbCdYcVr8mZU-f7Pq0T1cTgHlGm6eeSdVXxrYGQs6AR8BcL8w5ZeJQnz9t4imib7PJ3UtqpdW2MPpGevIFqsa6WLZeTS0Dq4C9w4wG_0wqG_Ft5mrOZzagbu_X42xR7LmJIp7YWJtOacW222PTtSqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز پنجشنبه ۲۶ شهریورماه در مراسم تقدیر از کارکنان برگزیده شاباک در بیت‌المقدس گفت اسرائیل بخش عمده ماموریت خود در برابر جمهوری اسلامی و گروه‌های متحد آن را انجام داده، اما این ماموریت هنوز به پایان نرسیده است. او گفت توانایی ایران و متحدانش برای آسیب رساندن به اسرائیل به‌شدت کاهش یافته است.
نتانیاهو با اشاره به ادامه عملیات اسرائیل گفت: «هنوز کارهایی برای تکمیل باقی مانده است و ما آن را به پایان خواهیم رساند.» او سپس تاکید کرد که اسرائیل حماس را از بین خواهد برد و در مورد جمهوری اسلامی گفت: «حکومت ایران را شکست خواهیم داد. آن را سرنگون خواهیم کرد؛ سرنگون خواهد شد.» او همچنین گفت اسرائیل به اقدامات خود علیه حزب‌الله ادامه خواهد داد.
نخست‌وزیر اسرائیل همچنین گفت خواست ایران و گروه‌های متحدش برای نابودی اسرائیل از بین نرفته، اما به گفته او، توانایی آن‌ها برای تحقق این هدف به‌شدت تضعیف شده است. این اظهارات در مراسم تقدیر از کارکنان برگزیده شاباک برای سال ۲۰۲۵ مطرح شد که با حضور اسحاق هرتزوگ، رئیس‌جمهوری اسرائیل، و داوید زینی، رئیس شاباک، برگزار شد.
@
VahidOOnLine
یسرائیل کاتز، وزیر دفاع اسرائیل، در شبکه اجتماعی اکس نوشت کارزار نظامی اسرائیل هنوز پایان نیافته و این کشور «اهداف مهمی» در برابر ایران و جبهه‌های دیگر دارد.
او گفت اسرائیل برای دستیابی به این اهداف «با قدرت نظامی و تدبیر سیاسی» اقدام خواهد کرد.
کاتز روز پنجشنبه ۲۶ شهریورماه با اشاره به غزه گفت سیاستی که همراه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دنبال می‌کند بر سلب توانایی گروه‌های جهادی برای حفظ قلمرو، زیرساخت‌ها، فرماندهان و تجدید قوا متمرکز است. او افزود اسرائیل این رویکرد را در غزه، لبنان و شمال کرانه باختری اجرا کرده است.
وزیر دفاع اسرائیل همچنین گفت این کشور فرماندهان «سپاه فلسطین» در ایران را هدف قرار داده و اجازه نخواهد داد ایران یا هیچ طرف دیگری حماس را دوباره مسلح کند. او تاکید کرد اسرائیل به عملیات خود برای تحقق اهداف امنیتی و جلوگیری از تکرار حمله‌ای مشابه هفتم اکتبر ادامه خواهد داد.
کاتز همچنین رجب طیب اردوغان، رئیس‌جمهوری ترکیه، را خطاب قرار داد و گفت اگر می‌خواهد به همفکرانش در غزه کمک کند، می‌تواند آن‌ها را به آنتالیا دعوت کند، اما «قدم به غزه نخواهد گذاشت».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/78420" target="_blank">📅 21:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78419">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UD2dB18V9emo-uGq2bBCgoA1y7r-h-lIo0CJnKGKfnFQrKMjvNTRj_aWl6CXaA5Y3odiLBtaZxTsvAqauMDiOE65owRXPea7V2v-qd5qK2Z7fySDx12P4d22LBa0YcFQFK4goZfzQn6m40rV8-MchUWL2iaACHfzypDWgKDd28WM-clBejGm0pUoizf0Xga5UMiodu-6691ICTdOJ-YLrlubPn0z2S5v-xGYLRZnE455wKTtTaUYBqp1rsIasfv4kxOi1jTqaSyLMexwQ5Vteg6tO9mOyMmXFZSyN50p22cJ8530gQ2WbUFBem9Efzt3vyffzUur8YgfKh2UfS5UTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیات حقیقت‌یاب مستقل بین‌المللی سازمان ملل درباره ایران در تازه‌ترین گزارش خود اعلام کرد دلایل معقولی برای این باور وجود دارد که آمریکا در جریان جنگ با جمهوری اسلامی، در دو حمله هوایی به ایران مرتکب «جنایت جنگی» شده است. بر اساس این گزارش، این حملات دست‌کم ۱۷۸ غیرنظامی، از جمله زنان و کودکان، را کشت.
این هیات در گزارشی که به شورای حقوق بشر سازمان ملل ارائه شد، حملات آمریکا و اسرائیل به ایران در ۹ اسفند ۱۴۰۴ را بررسی کرد و به این نتیجه رسید که آمریکا در دو مورد حملاتی بدون تمایز انجام داده که به کشته یا زخمی شدن غیرنظامیان و آسیب به اماکن غیرنظامی منجر شده است.
بر اساس یافته‌های هیات حقیقت‌یاب، در یکی از این موارد، موشک‌های تاماهاوک به دبستان شجره طیبه در میناب اصابت کردند. این هیات اعلام کرد این مدرسه به وضوح قابل شناسایی بوده و در این حمله بیش از ۱۵۰ نفر، از جمله حدود ۱۲۰ کودک، کشته شدند.
در موردی دیگر، آمریکا با استفاده از موشک‌های تهاجمی دقیق، ساچمه‌های تنگستن را بر فراز یک مجموعه ورزشی و منطقه مسکونی در لامرد پراکنده کرد. بر اساس گزارش، این حمله ۲۲ زن و مرد غیرنظامی را کشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78419" target="_blank">📅 21:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78418">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAUpfTUcWAOWB6ABsnha1b49FWy_UAcPQ_-LgZXZ4L5vD2WpcV6Jm-iX94sMYywK41hLl8O1FneSsiEMclrBNQzOVMMJ9SigpIcGTzyPIG1IS9T-TocggzMlxb32frqu5GMo3dOu6W6DtKi2kL2dCnfiylwflZZkL__dvcoVwYtG9qrG1I_VViBHnweO7ZLUxn6RUp-xh0bBmyM3HnK6cnTTnqWtB_BubC4G115V75Covz-xqXRYaH1r3nPJwGi5HeKAbV7iqLmGxQBhbDAbg3qqi4sY4rbz2Qa6Q7oTNROk_Gd1Zxbufdnt531l5g3g424g8JsQ20lgoWuhGJvW3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه و چین روز پنجشنبه، ۲۶ شهریور، در نشست شورای امنیت سازمان ملل متحد، پیش‌نویس قطعنامه پیشنهادی ایالات متحده برای تمدید ماموریت هیات کارشناسان کمیته تحریم‌های ۱۷۳۷ علیه جمهوری اسلامی ایران را وتو کردند.
این نشست با ابتکار فرانسه که در ماه سپتامبر ریاست دوره‌ای شورای امنیت را بر عهده دارد، در چارچوب دستورکار «منع اشاعه» برگزار شد. در جریان رای‌گیری میان ۱۵ عضو شورای امنیت، این قطعنامه ۱۱ رای مثبت کسب کرد، اما با مخالفت صریح (وتو) مسکو و پکن و همچنین رای ممتنع پاکستان و سومالی مواجه شد. برای تصویب یک قطعنامه در این شورا، علاوه بر کسب حداقل ۹ رای موافق، وتو نکردن اعضای دائم الزامی است.
دیپلمات‌ها پیش‌تر از مخالفت قطعی روسیه و چین با این طرح خبر داده بودند. مسکو و پکن معتقدند که با انقضای قطعی قطعنامه ۲۲۳۱ برجام در اکتبر ۲۰۲۵، تمامی سازوکارهای تحریمی پیشین از جمله کمیته ۱۷۳۷ فاقد هرگونه اعتبار و اثر حقوقی هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/78418" target="_blank">📅 18:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78417">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/caed21affc.mp4?token=v2YhjwpQ4D680xvpgZ1DPg9aKRSNumzObVW_Vgtomhyxu-RknKzncAMaa8gEg26aBm2jPLz4lUQH4y1dYlr0HHEXxAdfn5l0tVR16rpDXqNF11gw467Fx2nNmMwmrUTxRp_boxyCeV0F6FVAj0nU4cuiw8a6vAM0YbMJpA57KT-kuaffBepEmskhJdQYOu3gpK5d4HtqqaCYW5FaRNgBXMDkSEdFb7nsU8BoDxNMH7zENWzw-SRe9h6yMIzhbuSy71OcGGyFiDB5xuhGWtR9mNQWgCnl89fe_H43orj2IRy6KReino7saJlIQbiIsoJ-z6PJPOD8Dp3lpS3w5PCuRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/caed21affc.mp4?token=v2YhjwpQ4D680xvpgZ1DPg9aKRSNumzObVW_Vgtomhyxu-RknKzncAMaa8gEg26aBm2jPLz4lUQH4y1dYlr0HHEXxAdfn5l0tVR16rpDXqNF11gw467Fx2nNmMwmrUTxRp_boxyCeV0F6FVAj0nU4cuiw8a6vAM0YbMJpA57KT-kuaffBepEmskhJdQYOu3gpK5d4HtqqaCYW5FaRNgBXMDkSEdFb7nsU8BoDxNMH7zENWzw-SRe9h6yMIzhbuSy71OcGGyFiDB5xuhGWtR9mNQWgCnl89fe_H43orj2IRy6KReino7saJlIQbiIsoJ-z6PJPOD8Dp3lpS3w5PCuRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
خشونت و آزار جنسی)
ویدیو نشان می‌دهد ماموران فرماندهی انتظامی جمهوری اسلامی ایران یک نوجوان را مورد ضرب و شتم و آزار جنسی قرار داده‌اند.
این ویدیو خشم بسیاری از کاربران را برانگیخته است. برخی  گفته‌اند که «وقتی پلیس مقابل دوربین دست به چنین کارهایی می‌زند، معلوم نیست در بازداشتگاه و پشت درهای بسته چه به سر بازداشت‌شدگان می‌آورد.»
فرمانده انتظامی آذربایجان شرقی گفته که این اتفاق ۱۴ خرداد ۱۴۰۵ در جریان یک نزاع خیابانی در تبریز رخ داده است.
برخی هم با اشاره به انتشار این ویدیو در چهارمین سالگرد کشته شدن مهسا (ژینا) امینی در بازداشت گشت ارشاد، به تداوم خشونت پلیس در سایه نبود قوانین بازدارنده اشاره کرده‌اند.
پس از پربازدید شدن این ویدیو، فرمانده انتظامی استان آذربایجان شرقی گفت که ماموران حاضر در ویدیو «تنبیه انضباطی» شده‌اند.
علی محمدی به خبرگزاری فارس گفت که این افراد «تنبیه و انتظار خدمت» شده‌اند و «اقدامات تنبیهی تکمیلی» در مورد آنها در دست اقدام است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78417" target="_blank">📅 17:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78416">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nsLfLCLEW9S4V8tVBGZJVHCrl2eeLP31LrJp1tisOjYpTj-NbTRqfnlNaxsf2j8Qsvm4Ou7RPe-q_GuUKjGXgR6IPDYhvGDEDXuwXwH1KN4ZFmlI3bCq5hJb4wyS8sfLaoKTvLIxPy-F61drZiIPF5SGYc5r8MEpyyEyBZSC3HI4dVeECutybCNl4vvt6mE2WP8pskCcnyZdJAKhtH7RkuRL9fKcCRMi3U-gF9tTou_-tLkM9Fg3rOP1m1_8qCqOYAF6I5rpD-u3xe2j6ZdosRYrwZfHKCo_3iWy5p8v8PPrdnnElIGHfrj-VIU09pPkKv3jlQ0jELp9wPeiwtvILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، مدعی شده است جمهوری اسلامی مستقیما با دولت او تماس گرفته و «بسیار» خواهان دستیابی به توافق با ایالات متحده است. او همچنین ابراز امیدواری کرده جنگ نزدیک به پایان باشد.
ترامپ بامداد پنج‌شنبه ۲۶ شهریور ۱۴۰۵، پس از ورود به ایالت کارولینای شمالی، در پاسخ به پرسش خبرنگاران درباره مرحله کنونی جنگ گفت: «امیدوارم به پایان جنگ نزدیک شده باشیم.»
او سپس درباره احتمال دستیابی به توافق با جمهوری اسلامی گفت: «آن‌ها می‌خواهند توافق کنند و خواهیم دید چگونه پیش می‌رود.» ترامپ در پاسخ به این پرسش که آیا پیام ایران از طریق میانجی‌ها منتقل شده یا تماس مستقیمی صورت گرفته است، گفت این تماس «مستقیم» بوده، اما درباره زمان، سطح و محتوای آن توضیح بیشتری نداد.
رییس‌جمهوری آمریکا ساعاتی بعد در یک گردهمایی انتخاباتی در شهر گاستونیا در کارولینای شمالی، بار دیگر گفت جنگ با ایران به‌زودی پایان خواهد یافت و «پایان واقعا خوبی» خواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78416" target="_blank">📅 03:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78415">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OobBm4D-arffUNO-G9hqrOah3SY0rfspKZHb3IQt5QtNcQYwOnhM6i94mz3t7_MNvKVW9uV2AUUQBX_oizuLwLh-282r8t69EkbrNJeQrhim6OqdHRaE4-EWz1WyC6VSrTn1h0ZCYnz0-dOZghPwwXERkaYaflHNToOXYWaYx3CX_CqsmIhsy1oUN7NwkBNKIuPNN-bRJuXE2OrmTPfajwCN8yoXDLEUEWjA1vtU4JZfULgLYd4Bn9ehBaDKOwcU9DPfDXI6ofuJw71yOgfVZe_gkQ0eOm-NcIel0trVQWP29d08wIWtNC1GF6ZIMadtYHKT1X--tKcAq2cEfjw_yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت هواپیمایی ماهان چهارشنبه ۲۵ شهریور در اطلاعیه‌ای اعلام کرد پروازهای این شرکت در مسیر تهران-مسقط-تهران از ۲۶ شهریور، برابر با ۱۷ سپتامبر، تا اطلاع ثانوی لغو خواهد شد.
ماهان دلیل لغو این پروازها را اعلام مراجع هوانوردی عمان عنوان کرد.
این شرکت همچنین در اطلاعیه‌ای جداگانه اعلام کرد بنا بر اعلام مراجع هوانوردی ترکیه، پروازهای ماهان از ایران به مقصد ترکیه، شامل استانبول، آنکارا و بالعکس، از ۳۰ شهریور، برابر با ۲۱ سپتامبر، تا اطلاع ثانوی لغو خواهد شد.
ماهان افزود آخرین پروازهای این شرکت در مسیرهای تهران-استانبول، تهران-آنکارا و بالعکس روز ۲۹ شهریور انجام خواهد شد.
خبرگزاری عصر ایران نیز سه‌شنبه ۲۴ شهریور به نقل از یک منبع آگاه گزارش داده بود دولت گرجستان در پی تحریم‌های جدید آمریکا، پرواز همه شرکت‌های هواپیمایی ایرانی به این کشور را از دوشنبه آینده متوقف می‌کند.
عصر ایران افزود بررسی این رسانه از چند آژانس گردشگری نشان می‌دهد فروش تورهای گرجستان نیز تنها تا یکشنبه ۲۹ شهریور انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/78415" target="_blank">📅 17:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78414">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cn7Y62AbMEP4qoQDL5ucmtQjkD85ls3T4Ki9WY2FmtWK_hTIncBWkub_i8JxKmn3nrB8wYQf2Bry9LL7Co1WICVU2U3mDqmcwLh3X-Tl6xFApdXEiVUItt3rQUelLsfmz24tixkVUo4jGQ2OwQyg0bDHW0JKgh7N9jw3AuYvIvxBkF3tWy4ybRZpirhlfovcZaqxlw9cApjmt017E3L7Bv1_SQv_3oCW2Kur306ZtHZ2om_I1_OfQd65MIDonfdu9EudoK4JfqTOgT95-9R4lg3BooSii2FNS5OnOntz-UwovouGth1lsgjZ0ko5abaeZpLwZxAtBAVQ0hpZQRT-8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل قدیانی، زندانی سیاسی محبوس در زندان اوین، روایت جمهوری اسلامی درباره نقش «تروریست‌های وابسته به بیگانگان» در کشتن معترضان دی‌ماه ۱۴۰۴ را رد کرد و نیروهای حکومتی را مسئول «قتل عام» آن‌ها دانست.
قدیانی در بیانیه‌ای که روز ۲۴ شهریور از بند هفت زندان اوین نوشته، با اشاره به راهپیمایی ۲۲ بهمن و تجمعات حکومتی ماه‌های گذشته پرسیده است اگر عاملان تیراندازی به معترضان، آن‌گونه که حکومت می‌گوید، «تروریست» بوده‌اند، چرا در تجمعات حکومتی که در امنیت برگزار شده‌اند، اثری از آنها نبوده است.
او از رسانه‌ها و نهادهای حقوق بشری خواسته است درباره این تناقض در روایت جمهوری اسلامی پرسشگری کنند و نوشته است: «تروریستی در کار نبوده و نیست و قاتلان [...] همان نیروهای [...] حاکمیت‌اند.»
قدیانی همچنین در این بیانیه علی خامنه‌ای و پسرش مجتبی خامنه‌ای را مسئول این «جنایت سهمگین» دانسته و نیروهای حکومتی را به تیراندازی به معترضان متهم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78414" target="_blank">📅 17:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78413">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8_FEdV2AlGMgNdPVgoU9aXtfJP1k17j8g1JDOGmUCQNjicl3mYfE24lafMRbbXaNPKFLZ7w8sdM9bZc7_Yg4LOgcbNzFVdwhO64ncxTBC1s9vQgCowu1vrqK1Qj-MLhrS6TKlEfkL1MfZ6W80h7pnyBYOy_7luxQrcSV-xdx1tPVHVt0dSQQ1K-jb2BZBaq5xARbFOFHFlZ9Ufg_wJvhJAyKkV668xqqMfVq3CYdbe2g8Dwwi3H6ZD-tUhJCG9W4nxbKgSroUw5bKIUPVL31AZQz3Y8qZc1hr-t978598f3V3kzexw-yGZlLnhUi4NKyQ_flgV1PNOIsxDc4lprVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین با صدور بیانیه‌ای اعلام کرد که وانگ ئی، وزیر امور خارجه این کشور، روز چهارشنبه در دیدار با عباس عراقچی در پکن گفت:
چین، ایران و ایالات متحده را تشویق می‌کند تا عقلانیت خود را حفظ کرده، خویشتن‌داری نشان دهند، به یادداشت تفاهم اسلام‌آباد بازگردند و «در گفتگوهای ماهوی درباره مسائل مورد علاقه طرفین مشارکت کنند.
براساس این گزارش، وانگ با بیان اینکه چین «نمی‌خواهد شاهد سرایت بیشتر تنش‌های منطقه‌ای به یمن و دریای سرخ باشد» افزود: «ما از همه طرف‌ها می‌خواهیم اقدامات موثری برای بازگشایی هرچه سریع‌تر تنگه هرمز انجام دهند.»
وانگ همچنین گفت که سیاست چین در قبال ایران همواره ثابت و پایدار بوده و چین مایل است ارتباطات و هماهنگی‌های خود را با تهران تقویت کند.
@
VahidOOnLine
عباس عراقچی، وزیر خارجه جمهوری اسلامی، چهارشنبه، ۲۵ شهریور در سفر به پکن با وانگ یی، وزیر خارجه چین، دیدار کرد و بر گسترش روابط تهران و پکن در چارچوب مشارکت جامع راهبردی تاکید کرد.
عراقچی شرایط کنونی منطقه را ناشی از حملات نظامی آمریکا و اسرائیل به ایران دانست و از مواضع چین در محکوم کردن اقدامات این دو کشور قدردانی کرد.
او گفت: «جمهوری اسلامی ضمن آمادگی کامل برای دفاع مقتدرانه از حاکمیت ملی و تمامیت سرزمینی و صیانت از امنیت و منافع ملی ایران در مقابل متجاوزان، از راه‌حل‌های دیپلماتیک که حقوق ملت ایران را تامین کند، استقبال می‌کند.»
عراقچی همچنین گفت شرایط منطقه پس از جنگ ایران تغییر کرده است و در نظم جدید منطقه‌ای که با گفت‌وگو و همکاری کشورهای منطقه همراه خواهد بود، جایی برای حضور و دخالت نیروهای خارجی وجود ندارد.
او با اشاره به آنچه نقض مکرر تعهدات از سوی آمریکا خواند، گفت جمهوری اسلامی خواهان بازگشت آرامش به منطقه و روابط دوستانه با همسایگان است و در همین راستا گفت‌وگو با کشورهای منطقه را آغاز کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78413" target="_blank">📅 17:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78412">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dc-AEkZn5GyzEneR5phDU0cWj6tLLOCGFPx3hCXa5MtXkeUnhReE1ypA9_-U2DYjqUF1fgi2cuMfzggEEKwpESDzuKbTm4A1TITcngvmCtm6sXJuLqZuGlNwgWrqPf9l-gXv1eV1Cw3r80W5ecpXtjywA2EZ76kJ918mamTWyYlm1lWaS2iBnrEzZcA6xSEvxJfWEir6HnGfjeT7YTtkvW0ZiskWAJsCm3moG6ZNR1FZqpW6FPS5bl5BB3BvZZspMihPEnH090NTlMdaCwgpQRIRH70YVZBVMPUW6thmYr6CMUaYojVJYf88jQurh3L_IZISGyQt57y8H97Yn16huA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز روز چهارشنبه ۲۵ شهریورماه به نقل از پنج منبع آگاه گزارش کرد که مقام‌های ایالات متحده آخر هفته گذشته (روزهای شنبه یا یکشنبه) با نمایندگان شورشیان حوثی مورد حمایت جمهوری اسلامی ایران، دیدار کرده‌اند.
براساس این گزارش سه تن از این منابع که خواستند نامشان فاش نشود گفتند این دیدار که رسانه‌ای نشده بود، در سفارت آمریکا در مسقط برگزار شد. دو منبع دیگر نیز اشاره کردند که دولت عمان، به عنوان میانجی باسابقه منطقه‌ای، به برگزاری این نشست کمک کرده است.
دونالد ترامپ در سال ۲۰۲۵ و پس از بازگشت به قدرت حوثی‌ها را در فهرست «سازمان‌های تروریستی خارجی» قرار داد و هرگونه حمایت از این گروه را جرم‌انگاری کرد.
ترامپ روز شنبه گفت حوثی‌ها با دولت او تماس تلفنی داشته و از ایالات متحده خواسته‌اند از جنگ یمن دور بماند. جی‌دی ونس، معاون رئیس‌جمهوری هم روز دوشنبه بدون ارائه جزئیات تاکید کرد که ایالات متحده در تماس مستقیم با این گروه است.
دو منبع آگاه اعلام کردند در این نشست که به گفته یکی از آن‌ها روز یکشنبه برگزار شد، حوثی‌ها به مقام‌های آمریکایی گفته‌اند قصد حمله به شناورهای آمریکایی را ندارند و به آتش‌بس سال ۲۰۲۵ با آمریکا متعهد هستند.
یکی از این منابع که یک یمنی است، گفت این گروه همچنین اعلام کرده‌اند که به کشتی‌های اسرائیلی یا هرگونه کشتی تجاری دیگر، به‌جز کشتی‌های متعلق به عربستان سعودی، حمله نخواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78412" target="_blank">📅 17:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78411">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhlqsM2UttVzAQdGTu8kJLeu8Z20JSev0i8T0Nd3i_S-0hNrhBF87t-_ZAX3PzE-PxncskpBU5Bs5amBXWxpU5BeDJ97On7OAGdMHHfEKsUQTic2gAf9rpWFuaqkF-mXp1jZRfNV86Cv5_Ajos_XW1PDz1c5lrzt9a5cpuTak_CvktyLbDPFonuI4e-Xhi0-6nGbd1CVOGsgxo2SVh4lxhjGKvMVriqLBJwxJ4uZR_WINqprto7m_rJqTO5Dyf3uJKZ0ONJKQ3595RD90wanleX7T1NL7dKiYwyReRprc5mQj_S7gdatRE7e46MsXg__quYBpf4D244ax5K1DFOezg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«جی‌دی ونس‌»، معاون رییس‌جمهوری آمریکا، گفته است جنگ با جمهوری اسلامی طی «یکی دو ماه آینده» وارد مرحله‌ای کاملا متفاوت خواهد شد و واشنگتن در مرحله بعدی باید مانع بازسازی توانایی‌های هسته‌ای و نظامی حکومت ایران شود.
ونس همچنین با پیش‌بینی «دونالد ترامپ» همراه شده است که جنگ پس از انتخابات میان‌دوره‌ای آمریکا پایان خواهد یافت؛ هرچند توضیح نداده منظور از «مرحله متفاوت» تشدید عملیات نظامی، کاهش درگیری‌ها یا آغاز روندی دیپلماتیک است.
معاون رییس‌جمهوری آمریکا در گفت‌وگو با نیویورک‌پست که روز سه‌شنبه ۲۴ شهریور ۱۴۰۵ منتشر شد، گفت: «نمی‌توانیم آینده را پیش‌بینی کنیم، اما فکر می‌کنم رییس‌جمهوری درست می‌گوید که این مسئله طی یکی دو ماه آینده وارد مرحله‌ای کاملا متفاوت خواهد شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/78411" target="_blank">📅 17:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78410">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WsaHvLvIUionpnesaai_V9dBZYcDmGy_MBC0jqosDtNJX7_I6SxJKA9_6iBf_zh4Dj6yYUNWFByiE4t1MZN1T2ZWLLeIotPfrhpn19qbnjDC8REHAsP5C3gHfUBc9p9cu0S52J2fxBzZD-l0htiJyntndprWObjtvetVZU1BdOGQI0irQ5FHuSYa8ZIio3WNuMnXUO4w_jJ-WXACewGcOaHRGEQ-WbawPE2iQfvydeHYn8_FwiHWHoTJxwriOaziiZCAd-CxRZvDGPB3DP4pUOQ-eWoa4eEjhws8lFlUcZVWnC7DKpPqatIeLjJRmgF3oKtAz2kBtA16SnxiO78wvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین قشقایی، همسرش سارا شمسایی و ابوالفضل قشقایی، برادر حسین، از معترضان دی‌ماه، پنجشنبه ۱۹ شهریور بازداشت شدند.
حسین قشقایی و سارا شمسایی در لاهیجان به دست نیروهای وزارت اطلاعات بازداشت و به اراک منتقل شده‌اند.
محل دقیق نگهداری آنها مشخص نیست و احتمال می‌رود در بازداشتگاه اداره اطلاعات اراک باشند.
ابوالفضل قشقایی نیز همان روز در زرندیه ساوه بازداشت و به اراک منتقل شد. به گفته یک منبع مطلع، ماموران هنگام بازداشت با خشونت وارد منزل شدند و گوشی‌های تلفن، تبلت و لپ‌تاپ اعضای خانواده را با خود بردند.
حسین قشقایی با اتهام‌هایی از جمله «فعالیت تبلیغی علیه نظام»، «اغوا و تحریک به جهت برهم زدن امنیت کشور به جنگ و کشتار»، «نشر اکاذیب در فضای مجازی» و «اجتماع و تبانی علیه امنیت ملی» روبه‌رو است.
درباره اتهام ابوالفضل تاکنون اطلاعاتی به خانواده اعلام نشده و پرونده این سه نفر هنوز به شعبه‌ای ارجاع نشده است.
از دی‌ماه، سیم‌کارت‌های حسین و سارا و حساب بانکی حسین نیز مسدود شده بود. آنها ماه گذشته به دادسرای عمومی و انقلاب زرندیه احضار شده بودند، اما در مهلت پنج‌روزه تعیین‌شده حاضر نشدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/78410" target="_blank">📅 17:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78405">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=qGt4FZDfXJTV2Y1fEwVjMgLx_R2wWus6wQDdJAOCmcvVleBSoFlmMb1t4l_EAD_nQZ0_Octk2TOvT61zDnTnf-AkZhVRh8cdYqo9jSlHoxphGzzuWaSEM-9hewqCe5QomxNHiPi1xh_BtuwMI_gObnEUUyEfMy3qM0XDM_i2LfW3PeVayHzCOBmnAyNxo1kriiYxktLzUBswmKF71geHebdmycBJb9AZQa8eQCkJ8t23QVWfaJkl7rKXbW_dDOKJH7vprXLwLigPz0B2LxI-qiJD--gmfFCy16uvaqxY2sx17oSS4ZIl0BaHKWNriq59D21U_PU0T3TctmER0hJXmYSCICtLhOcxeLP71J1_lqULw-YUyuw_62wYps84tpPKlLFCt2GgYo7PXUp-XZHm9W_ymw2JaJadViOigdR8LJdowAB83ivBo3IqYaYjoVnBqV6isdPD30MFVfrl0mWa3IiCQR7T-sOtHQsB2cKOk4rOM440xxCtD-mvg8mUvsf7aZPVaW93TQ30gWqWm-gmnZD5tKRHJ5MJQR2SabFDF2P3OCZs0K8Pn6Qu2rB2sttL0w1exi0fvnSm3BzW1Be5YQhUMBB2iq4tYQydKf5HQbK-Jk7135pbx7Nu-LcFDq-p_t8DUCQI5mBb1a5E8FYBY0FjMlHgpx53LZxmwAmV1HI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=qGt4FZDfXJTV2Y1fEwVjMgLx_R2wWus6wQDdJAOCmcvVleBSoFlmMb1t4l_EAD_nQZ0_Octk2TOvT61zDnTnf-AkZhVRh8cdYqo9jSlHoxphGzzuWaSEM-9hewqCe5QomxNHiPi1xh_BtuwMI_gObnEUUyEfMy3qM0XDM_i2LfW3PeVayHzCOBmnAyNxo1kriiYxktLzUBswmKF71geHebdmycBJb9AZQa8eQCkJ8t23QVWfaJkl7rKXbW_dDOKJH7vprXLwLigPz0B2LxI-qiJD--gmfFCy16uvaqxY2sx17oSS4ZIl0BaHKWNriq59D21U_PU0T3TctmER0hJXmYSCICtLhOcxeLP71J1_lqULw-YUyuw_62wYps84tpPKlLFCt2GgYo7PXUp-XZHm9W_ymw2JaJadViOigdR8LJdowAB83ivBo3IqYaYjoVnBqV6isdPD30MFVfrl0mWa3IiCQR7T-sOtHQsB2cKOk4rOM440xxCtD-mvg8mUvsf7aZPVaW93TQ30gWqWm-gmnZD5tKRHJ5MJQR2SabFDF2P3OCZs0K8Pn6Qu2rB2sttL0w1exi0fvnSm3BzW1Be5YQhUMBB2iq4tYQydKf5HQbK-Jk7135pbx7Nu-LcFDq-p_t8DUCQI5mBb1a5E8FYBY0FjMlHgpx53LZxmwAmV1HI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی فراخوان ائتلاف نیروهای سیاسی کردستان ایران، همزمان با چهارمین سالگرد قتل حکومتی مهسا ژینا امینی و آغاز جنبش «زن، زندگی، آزادی»، کسبه و بازاریان شماری از شهرهای کردنشین اعتصاب کردند و مغازه‌های خود را بسته نگه داشتند.
از صبح تا ظهر چهارشنبه ۲۵ شهریور، اعتصاب و بسته بودن مغازه‌ها و بازار در دست‌کم ۲۰ شهر، از جمله ارومیه، اشنویه، بانه، بوکان، بیجار، پاوه، پیرانشهر، ثلاث باباجانی، جوانرود، دیواندره، روانسر، سقز، سنندج، قروه، کامیاران، کرمانشاه، کرند، مریوان، مهاباد و میاندوآب گزارش شده است.
@
VahidOOnLine
وب‌سایت‌ها و منابع خبری مختلف که اخبار کردستان را منتشر می‌کنند، از جمله هانا، کردپا، کولبرنیوز، زاگرس ۲۴ و شبکه حقوق بشر کردستان نیز گزارش‌ها و تصاویری از تعطیلی مغازه‌ها در شهرهای مختلف کردنشین منتشر کردند.
در همین حال تصاویر و گزارش‌های مختلفی از برقراری فضای امنیتی شدید و استقرار نیروهای نظامی و انتظامی با سلاح‌های سنگین در شهرهای مختلف کردنشین منتشر شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78405" target="_blank">📅 17:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78399">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UFxYiDfMahcB0TMNr7mw5Nsp45FF6LR9ZJXEnVpQa75cbVOS9EUJWvKZtUDjOlggoTG672uAPSN0h3UxZDuczpDeY9-xqKgGZrTulDr5Q5nx2Vr7F_BFpPRMTb3VPKEBW4-SF-YhzscoPMVr23iE05mSNaGna_oJvoEkIsQDArkyFcengpXR8nsAH0GFpFXorRCSYA2Ro5AiI_P8ivI0RyWZ6oFL3-XOPX_8pl9AIw_yWzUpef2TDxqAopmnAsTfeP3fQytivxdaCUm1tBW9dTCcRhZkGE16Vk3qRA9r-HKTkfExa3D0ErnGyAhezTmdjzF0xc4cSyWmJI3If99PQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kn75cP4Pp-pktvWUQpI-MEBVNPC5f1LZPLQbZA6lhf_tpHUDZ_xV_pITdqqm49ZYcMiAJ-PX3w8ouhy9-Fx0_hJHsuDDqahDcRHf4cfSXbcAwMas1qyI63wlGCIdiKCNd8_5-wzkQDlu1e1H7CVgWQfk1erfD0FFGS-Zxd-5AhJUAl4Tq6Cr16l3gKteN9OYZ_LLWj1yYmvQk7Qw_huveJLIb4RERj1LviDluFwc7ghDiHW3PCJRMR5_KzccMG9-BsezZXhaSMsI6FSYXLIbQ17Ohn7CBOvtoOMZ_rJ9zSp9kXMqo6Fd29ALsxihcBk-ffc3iKlfg3qhdJp_AeuAog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fMniRjj2xPt5Fwpku4cxRD8Y-IclNJaWYXyVM30mrjaHZmi7-2iaNXUF_zLp7JCx-vRqaidiUHvnLk9iRdYTW3DTkwk-lVDVyqyV2zkhwseDT76C63sj34UmMIJqEcb9em8ctRLhtMeyCVSAbqZsYEzErhkGFafVsKjwj57LKm3IDTE-MG0mCnjx-NsQ_SX-QH_50R0ZbnxKBLuA_IWnOEs91EtvOyYJYGhAQiXE0R8tgk_u1eIC8zcvxaH5Ic_6esSrQzFdzP-AJlh4HIMf6SOfbgHZSEOjI2wI8CO8Sq3ybqafbJsuMw_6yCi5JPsaDlJFJvzjv9q4s9itZaOW4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UDPi5eouZqptbPHKX8Ex-QHnKK54hhFDSyWLqWQdoWT3SxskjL9rq3esFTbJ5nB02Eg11t1dGQQl-gLB65sXZvXyGkPcnU-GxUlh9PZRBjCdCfzvq7TO_Gq02ggJAsrC3Pu5oSWTvraL0WQb3r1wxu8iDOSv5XegXUL5FM5ZlnptzYchgJMCYZSYU4n9KSSPI80aJyrf2C2Mtvm3mmSvKnlN7s5nLBWbyI-tHXij6ILCX3FgNKmyuhEBJOKDxNeGCYHfVz3-7hIRxPG5g2Cnbm93oUnEezcPyPackJGYlhTp9ndc6orTyYY0qnuWZ5b0isZF49C3WNeU1iq5CWSBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pll6F3C2Nmf-FUsOqLFiNPJjMgO3U9lwowUhW87nYsIbXDKtnLVnLtwRDbjy4HHGgmU9dKSnM2O3bCHVANZpOF_3pzWRxYTMAfLXdikwfwkvY4FLmxcFM5_LSwSia8bI6_Ih33s08j-kIc4pIo_JB4Up-uRlSumUgJa0UAr8IdoFprrCpW14xNSaLLMxgndo2OPSEbsdAtODh3QtL7ZSPFpDuixoZ3xkKZH0ha1Oyj4aro6K6jOCAWjezyvWFlqJYr1upFKwDlIhNhbbhlu7-kY3p-48p9b2gLwSqw44mZuTlHvUDa4_oyhQaJ7BRTA2eVItUiblRQhVbxQzt3midw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Etd_Exvq3NX485hBIVe-Py_dPzHF4azUlTzA4c24IhtHO2iLRTI_ccSi-E3TMnazhPDop8oN3MMBgmpuSdOcfyFLp_2gI6E0dCMiMR-9f2iWWVQRjNkimHi6WNwD9kSYxAUo2AdVVNqT7IDPqt_iyBIyCyoASWi06OB73zcCPV6KcY2enzNWmGQIJeZKdAV8Vxy3Pqv9gFlmFRqYiic-VhKFUPkbDFoznD0vJcwhs_6cH0pNpt21AzXfMO-uKBTevexTs3u55yyu7l6W5s1WWGuJcrjkgN-yEkxyrCV30iL73QAmbvqLhdJaGxGTEe0EBMUMjYZ88Bzq9pdP7cjR6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سی‌بی‌اس‌نیوز گزارش داد تصاویر جدیدی که به‌طور اختصاصی به دست آورده، برای نخستین بار گستردگی خسارت حملات موشکی و پهپادی جمهوری اسلامی به چند موضع نظامی آمریکا در خاورمیانه را نشان می‌دهد.
این تصاویر را نظامیان آمریکایی در اختیار سی‌بی‌اس‌نیوز قرار داده‌اند. یکی از آنها گفت خسارت گسترده به پایگاه‌های آمریکا به اطلاع مردم این کشور نرسیده است.
در تصویری از پایگاه هوایی شاهزاده سلطان در عربستان سعودی، یک هواپیمای چهارموتوره بویینگ ای-۳ سنتری دیده می‌شود که موشک به بخش عقبی آن اصابت کرده و دم هواپیما از بدنه سوخته جدا شده است.
تصاویر دیگری از این پایگاه، ساختمان‌ها و آسایشگاه‌هایی را نشان می‌دهند که بخش‌های داخلی آنها تخریب شده است.
سی‌بی‌اس‌نیوز همچنین از ثبت خسارت‌های مشابه در کمپ بوهرینگ در کویت خبر داد؛ پایگاهی که محل استقرار و آماده‌سازی نیروهای زمینی، خودروهای زرهی و شماری از هواپیماهای ارتش آمریکاست.
پنتاگون به درخواست سی‌بی‌اس‌نیوز برای اظهارنظر درباره این گزارش پاسخ نداد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78399" target="_blank">📅 04:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78398">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zj9TNEZVsJg_-eoCZr_3rxNj8u4W1xRfWGVM_KhSe09Ez8Rm6zUglc8LLNTD9xZjNZqOj9HwCntK0jQ2UjxVmtHrgjLdd3V4uvlKFMPNxmqpF7JNO9Q6Rbhx27eoMO6G97WxSWtlS2I470_NhAcTCUQrkBjYt1YvGOBJEWxYYzVXmXlxegJFGK7rGqEu-ihmZmt8AyvJhVZteUE2SuRJkLqIjYY4MNJ9rVkfqHx7zThghI7SLSnWQiVsA-YErILCq8IEnqiLtPeANGxgaXCGPCa9FUqiKw4V5-vMP5VpzWPpEwzuXmJKBRAR4SAg8VELJwFLaWrMKoBSjOku9ZTNzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی در یمن اعلام کرد پدافند هوایی این ائتلاف یک فروند پهپاد پرتاب‌شده از سوی حوثی‌ها را که قصد ورود به حریم هوایی مکه را داشت، رهگیری و منهدم کرده است.
به گزارش خبرگزاری رویترز، ترکی المالکی، سخنگوی ائتلاف، در بیانیه‌ای گفت این دومین تلاش حوثی‌ها برای هدف قرار دادن مکه بوده است.
به گفته ائتلاف، پیش از این نیز حدود ۹ سال قبل یک فروند موشک بالستیک به سوی مکه شلیک شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78398" target="_blank">📅 03:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78397">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rdVvudxUeCgVvQxyR5zGah3r7HgdbqXjpgiJ4Czufxbtm-yArf7bb5KfDCK-k-47znCkCFFSZ723necQqf1P_I9xOYZep6jmI7vhAGwyiCLI9QmlAqTXc7y9VUpBXz46AF2XsW89CrtgEmU15O-vx-OQsK8XdYCkfxOl7ridQJyY4omNVV4HKJVOLhUAipwvnolVMckA6Rg8ILAbToU6Fviy_u32q_zb910d0i-0wTcw9DT9YgflWD86Cpw9Y3FBPypPjGqA2MXpbElP7ewUEZctuOkEsaRMtWUS84ftjuh7ZTLtLYQIueoyuz_a-OSbnALkbIaQw5Gs-oVgmCkv5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از دو مقام اسرائیلی گزارش داد فرماندهان ارشد نظامی آمریکا، اسرائیل، عربستان سعودی، امارات متحده عربی، بحرین، کویت، قطر، اردن و مصر هفته گذشته در نشستی محرمانه در آلمان درباره جنگ با جمهوری اسلامی و تنش‌های منطقه گفت‌وگو کردند.
اکسیوس گزارش داد نشست محرمانه فرماندهان نظامی در آلمان به ابتکار برد کوپر، فرمانده سنتکام، برگزار شد.
به گزارش اکسیوس، برد کوپر در نشست محرمانه آلمان، فرماندهان نظامی اسرائیل و کشورهای عربی را در جریان برنامه آمریکا برای افزایش تردد کشتی‌ها در تنگه هرمز قرار داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78397" target="_blank">📅 21:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78396">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=UnOUrK6xZfGi6EFBAciSxS9_impIt9ZnzKgPak0ae9Q8CfQWEjBJPvN7CLjgmyVLgXJ75PUtd39w_5oIX6Wapu_ZlTV39Y-EwskVN_gG8XeKp3-UpSIkDh2AfdjNmHLDpHA6ZTQoIiHJf0xq1XwlixXrzfBjZiM6gFBhvmatHfkFi3iMTxPacNJ6hcvWpcGg_6oRP52jONyn1c8xrT3DeUL4wFu6z8zfQppJlftWOKBX2L0DVSXBFNhMt3x18PD93Lc7zaQcmyqS-IEm2iKsSmzLLmSNbSwSMN8cJQFnBTrhglxX8XQb4NyyCibI_pD04D6qoee9GUfKCmX034QpLA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=UnOUrK6xZfGi6EFBAciSxS9_impIt9ZnzKgPak0ae9Q8CfQWEjBJPvN7CLjgmyVLgXJ75PUtd39w_5oIX6Wapu_ZlTV39Y-EwskVN_gG8XeKp3-UpSIkDh2AfdjNmHLDpHA6ZTQoIiHJf0xq1XwlixXrzfBjZiM6gFBhvmatHfkFi3iMTxPacNJ6hcvWpcGg_6oRP52jONyn1c8xrT3DeUL4wFu6z8zfQppJlftWOKBX2L0DVSXBFNhMt3x18PD93Lc7zaQcmyqS-IEm2iKsSmzLLmSNbSwSMN8cJQFnBTrhglxX8XQb4NyyCibI_pD04D6qoee9GUfKCmX034QpLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده در جلسه سالانه درباره وضعیت اقتصادی آمریکا و سیستم مالی بین‌المللی با دفاع از سیاست‌های دولت دونالد ترامپ در قبال ایران، گفت رئیس‌جمهوری آمریکا اقدامی را انجام داده که به گفته او، رؤسای‌جمهور پیشین آمریکا سال‌ها از انجام آن خودداری کرده بودند.
اسکات بسنت با اشاره به جمهوری اسلامی گفت: رژیمی که خود را وقف شعار "مرگ بر آمریکا" کرده و به‌دنبال دستیابی به سلاح هسته‌ای برای تحقق همین هدف است، اکنون با سیاستی متفاوت از سوی آمریکا روبه‌رو شده است.
او افزود: تحت رهبری رئیس‌جمهور ترامپ، آمریکا دیگر صرفا در حال مدیریت تهدید ایران نیست؛ ما در حال پایان دادن به آن هستیم.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78396" target="_blank">📅 21:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78395">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OV90SK_R31ME2__3n7jtN2jz_FmuNfdSez_Kso7s08wP3djJ3E2x4V91UQTbGboANvAfrT5qmqVg_tsNzG2Tf4dGj3MozH4NynD9gu0d1YEc4Sr1N4qHeRcypE8KuqjXo7iZJQC1vYXqZQdonfZaVQnUPtuVWjiavx_ebner14r_o6BFIJpIj1jJ8NRNSEcrzs20HHKqmdYGpjMLrVHm3_tdfOuX-QBPzwRLNzHQPznwpW3shfegrbHGtRImb7-gLgNAwF9sokMoPhW2MgqeEGb_MU8mw7iW7tDrdyWdf3Kn-MttcSJoqAzQlY4EcfTOMhpJLN6eNEIqDuERe-EsZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درباره خبری که تسنیم با شرح
حمله به قایق‌های صیادی
منتشر کرده بود:
وبسایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد ارتش ایالات متحده روز دوشنبه ۲۳ شهریور ۱۴۰۵، دو قایق کوچک ایرانی را پس از تلاش نیروهای سپاه پاسداران برای تصرف یک پهپاد نیروی دریایی آمریکا در تنگه هرمز منهدم کرده است.
به گزارش اکسیوس، نیروهای سپاه با استفاده از این قایق‌ها تلاش کردند یک شناور بدون‌سرنشین آمریکایی را که برای گشت‌زنی در تنگه هرمز مورد استفاده قرار می‌گیرد، تصرف کنند.
پس از شناسایی این تلاش، یک پهپاد آمریکایی دو موشک به سمت قایق‌ها شلیک کرد که به انهدام آنها و کشته‌شدن بیشتر سرنشینان منجر شد.
تیم هاوکینز، سخنگوی سنتکام، تلاش نیروهای ایرانی برای تصرف شناور آمریکایی را تایید کرد و گفت این قایق‌ها «تلاش کردند یک شناور سطحی بدون‌سرنشین آمریکا را تصرف کنند، اما پس از واکنش قاطع نیروهای سنتکام موفق نشدند». او تأکید کرد این شناور همچنان تحت کنترل عملیاتی ارتش آمریکا قرار دارد.
این در حالی است که رسانه‌های ایران حمله به دو قایق را به شکل حمله پهپادی به «قایق‌های صیادی» گزارش کرده‌اند.
به نوشته اکسیوس، این دو قایق در نزدیکی بندر کرگان و جزیره لارک در استان هرمزگان هدف قرار گرفتند و احمد نفیسی، معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان، حمله را به ارتش آمریکا نسبت داده و از مفقود شدن شماری از صیادان و آغاز عملیات جست‌وجو و نجات خبر داده است.
این حادثه در شرایطی رخ داده که ارتش آمریکا تلاش می‌کند با افزایش تردد کشتی‌های تجاری در تنگه هرمز، عبور و مرور دریایی در این مسیر را به وضعیت عادی نزدیک کند.
یک مقام آمریکایی به اکسیوس گفت ارتش آمریکا و کشورهای عربی خلیج فارس در ماه‌های اخیر تردد نفتکش‌ها از تنگه را در طول روز نیز آغاز کرده‌اند، در حالی که پیش‌تر این عبورها عمدتا شبانه انجام می‌شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78395" target="_blank">📅 19:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78394">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=Ehejt1SnIkCu8WatQDCl3Gy5qEu-cd0eSS8YJsQOIetkSBB5-RQXXtS4lQyW2nY724vYErYRqhOopZDyWfyBZTvOk5mzN-3eM2jtVsDG0J2b9ZWS_3EEtQJfwIfseDAuLPmZbKNs4JWFugMF5W_SpV6dSZLBojWVvpjEfRWP2McBR9pY9iVwOkOWRmQKMoaMg2lOHLDQ5Q_TKnEFwS1sOBMPtDFl1qRrRPd06lmQdYBMSXeFzYsLpE235o_XoaFbMPI3VGijwlZMlPP7U-giFuQ_PMaVxfz8Vg8tTiY_uuZfoorL2W39gKLRFUD4OEaeUlrKLE_eV9Fhlz94gbaABQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=Ehejt1SnIkCu8WatQDCl3Gy5qEu-cd0eSS8YJsQOIetkSBB5-RQXXtS4lQyW2nY724vYErYRqhOopZDyWfyBZTvOk5mzN-3eM2jtVsDG0J2b9ZWS_3EEtQJfwIfseDAuLPmZbKNs4JWFugMF5W_SpV6dSZLBojWVvpjEfRWP2McBR9pY9iVwOkOWRmQKMoaMg2lOHLDQ5Q_TKnEFwS1sOBMPtDFl1qRrRPd06lmQdYBMSXeFzYsLpE235o_XoaFbMPI3VGijwlZMlPP7U-giFuQ_PMaVxfz8Vg8tTiY_uuZfoorL2W39gKLRFUD4OEaeUlrKLE_eV9Fhlz94gbaABQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیوی منتشرشده در خبرگزاری رکنا، لحظات پراضطراب داخل هواپیمای بوئینگ ۷۳۷ شرکت سپهران را نشان می‌دهد که دوشنبه ۲۳ شهریور پس از برخاستن از فرودگاه مشهد به مقصد کرمانشاه، با ترکیدگی لاستیک مواجه شد و با گزارش آسیب به موتور، مجبور شد به فرودگاه مشهد بازگردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78394" target="_blank">📅 17:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78393">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GQtsvCaPk3XPs9EqVnIia1C5dhIQQojEUqt677zRo5VS6Y2ESXmNjxYQd5fq7C_b7iaWegsY_7VRLK1mfcDX7wDpD1hLeZ-ngu510_ZxO-SGrxguI75NEd1Y-kGYmE7Mv2yAdl74FCMtdQv8dZrP2QojIDyuwP4w44iyo28BOazOcsiCWNkm7jsBmgK37xqDA7Cc4QitCllZ_RCSo0NqMHWW4vGmSGzCVovMcZpWfyynrw_SDJOoBJ6Zm9STakVKVqmbTi5u28b23D3BV8J0WRAVUZyMW6Cu2cJ3nIuyTUvtJhTwaBGUWv7rVagOKevT2ZRO0Wwu6nJasj-wWCShDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر رئیسیان، وکیل دادگستری روز سه‌شنبه ۲۴ شهریورماه با انتشار پیامی در اکس، از تشکیل پرونده کیفری برای رضا درمیشیان، کارگردان سینما و تئاتر ایران خبر داد.
به گفته رئیسیان، سپاه با شکایت از رضا درمیشیان  به اتهام تبلیغ علیه نظام پرونده قضایی تشکیل داده رسیدگی به شکایت از او در شعبه هفتم دادگاه انقلاب تهران در جریان  است.»
رئیسیان با اعلام این خبر گفت در دادسرا برای رضا درمیشیان قرار جلب صادر شده و سپاه پاسداران به عنوان شاکی، تقاضای توقیف اموال او را کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78393" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78392">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vnt354CgIcRMfUcGxkgewKYZXVJQx7F4kjkgb_io-zg1GYMJQ43mN5Ri8jLik7WGgvA8igLIjmrMcHh3H1OBVFdHc4CBSfuN0qxSlTn9vbaIMDakLn-fEFFr92k8DrFxySsReQfg_hx2di4ijNkJDI-m3KlHYlqLCTkhIjBiBgMpDDOh_EHRQYZTB_pSmqIhPhPYYQePK08A35nOJ8G7bpLi_w2GSRB_wxfM3DUvUwphw4LmAMz6LiVOb7-DzjrjggMYE3liM4UUCTMlr1UGM9fP29bM8iQ65N5q9V_4VUeK3pow69p3W6aNfC_w6-ZO8H6Pa9Gf_NQythYm8HP95Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استودیوی «کارگاه» با انتشار عکسی از آزادی «آریا کسایی»، طراح گرافیک و یکی از بنیان‌گذاران این استودیو، پس از نزدیک به دوماه بازداشت خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78392" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78391">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e_FW92HuEquXWUoNXVWRoDVQJnpQQhNqvvENhX3Ld5NYh8EltNl_CMt99kS156v-Dn5EVmrY9-KdpUkk-ITERG6imuYR8LeAP3FT3UfaQQPMSXe3p56_ZGu9GIl1haoIEXIMLXEGbeCtTPM-pR32-yFsXK7w8dTZZXgEczTh3DwPoY0qQ4aBGYz4N9RxfsMHNRLkiJTlOFxttLQs5loKHe3bch46eFjCcvLCKBaSSFYkW2smIZ1zwoXBYRTMpdmtAu98rpg7gXtEKINRhrX2tLyFZwforyfGc4xZfFwV0h8qYG9nExsNNk-elSww4_KfU9TGWTzAcoUj8-sm0GdMUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس تهران می‌گوید فردی را بازداشت کرده است که شامگاه دوشنبه ۲۳ شهریور به سمت «جمعیت حاضر» در میدان پونک تهران سه کوکتل مولوتوف پرتاب کرده بود.
میدان پونک از جمله میدان‌های تهران است که از زمان آغاز جنگ ۴۰ روزه تجمعات شبانهٔ حکومتی در آن برگزار می‌شود.
بر اساس بیانیه‌ای که فرماندهی نیروی انتظامی تهران منتشر کرده، «این فرد حوالی ساعت ۲۱:۳۰ از بالای ساختمانی به سمت جمعیت سه کوکتل مولوتوف پرتاب کرده و پس از آن گریخته است».
در این بیانیه ادعا شده که این فرد «قصد خروج غیرقانونی از مرزهای غربی کشور داشته اما ماموران با شلیک گلوله از ناحیه پای راست او را دستگیر و به بیمارستان منتقل کردند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78391" target="_blank">📅 15:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78390">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/utDGtejroSQU_8iCpAyBUjZ2NCUX5SQJdDqSrb4MUPtJc_iP6gMk6xgmLcWMQLvDzPIYwJsJ3p6EKneiXlizwLz5e4d_6OyPkQ0kj4kAaEeAuK9jeMmFypOTFvUAHgBq3WfMgWFN9BSISPPMA6m98DdnSvVCv2O3NAQBp-ccOoGZhHZbUOIdu4PrKn8FmTFmHHmj3YrvxPQkJ38VGQol314bznQq-5alam2bOgOjE3kKsVPqhGyV9ikmPbn9XoFCK0Qv9gL8fIW4gCgqUy2_9QeZ0sxupWS3R0V5vKewfVZ5k94fapQGDxRQEMGlzIoQtKPolYTcPVrzdKhVSa33eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش رسمی آمریکا از هزینه‌ها و خسارت‌های جنگ با ایران منتشر شد
یک گزارش رسمی نهادهای نظارتی دولت آمریکا می‌گوید جنگ با ایران به «کمبودهای راهبردی» در ذخایر برخی تسلیحات پیشرفتهٔ ایالات متحده منجر شده است.
نخستین گزارش رسمی نهادهای بازرسی دولت آمریکا دربارهٔ عملیات «خشم حماسی» که روز دوشنبه ۲۳ شهریور به‌طور عمومی منتشر شد، می‌گوید مصرف گستردهٔ تسلیحات در جنگ با ایران «به کمبودهای راهبردی در موجودی‌ها منجر شده و گلوگاه‌های پایهٔ صنعتی برای تأمین مجدد مهمات را آشکار کرده است».
بر اساس این ارزیابی، پنتاگون برای مقابله با این مشکل در تلاش است روند خرید تسلیحات و زمان تولید را کاهش دهد و ذخایر مواد و قطعات حیاتی و برخی مهمات را افزایش دهد تا در شرایط اضطراری امکان افزایش سریع تولید وجود داشته باشد.
این گزارش همچنین نشان می‌دهد آمریکا تا ۲۹ ژوئن (۸ تیر) حدود ۳۳ میلیارد و ۴۰۰ میلیون دلار برای جنگ هزینه کرده است. نزدیک به دو سوم این مبلغ مربوط به مهمات مصرف‌شده بوده و ۳ میلیارد و ۷۰۰ میلیون دلار به تجهیزات از دست‌رفته اختصاص داشته است. بر اساس این گزارش، ۷ میلیارد و ۴۰۰ میلیون دلار دیگر نیز در ردیف سایر هزینه‌ها قرار گرفته است.
پیت هگست، وزیر دفاع آمریکا، اواخر ژوئیه (اوایل مرداد) هزینهٔ جنگ تا آن زمان را ۳۷ میلیارد و ۵۰۰ میلیون دلار اعلام کرده بود. شبکهٔ ان‌بی‌سی نیوز نیز پیشتر به نقل از مقام‌ها و افراد مطلع از برآوردهای داخلی گزارش داده بود که با احتساب هزینه‌های گسترده‌تر، رقم واقعی جنگ می‌تواند به ۸۰ تا ۱۰۰ میلیارد دلار رسیده باشد.
دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه و همزمان با انتشار گزارش ارزیابی «عملیات خشم حماسی»، در شبکهٔ اجتماعی تروث سوشال نوشت آمریکا اکنون بیش از هر زمان دیگری در تاریخ خود تسلیحات پیشرفته تولید می‌کند و این تجهیزات به‌طور روزانه در اختیار نیروهای آمریکایی در خاورمیانه و دیگر مناطق قرار می‌گیرند
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78390" target="_blank">📅 15:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78389">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQ7_pVn5LA-NErRNepeQ4OTfMMLhFxs9tS20RSqQNK3lLB_IIj1b3HpUK1dSyoAxm4VPJmkUi-WwH2yDdh4RwuAiVjveqKAA9cxzShWZeJQuvEuQKvAeYNbBrRfNFPbdPVxyOSQY9ehw20EYdCrBHwchd2GXl-Ku-ag9mMcezMGTptYUlgzDzCbj5jr0qsq6PQSr0SDVja8mm7k0SOQWQIe8q3mgUx2VXtV8f0hbQ-KjZjZoSF3x_CDLzH7C0y5mmi175ZXIwJa7vWRa6q9A9Pp-_YzBGDEGhdE3OyC_ZLTOoE-Qc6s5fPsq4D2GSJIVVRc1OzfDFYIWzgBltM6nsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پروژه امنیتی با نام «علاج» با انتشار اطلاعات شخصی شماری از ایرانیان خارج از کشور، از شهروندان خواسته است افراد بیشتری را شناسایی و به این سامانه گزارش کنند. صداوسیمای جمهوری اسلامی نیز به تبلیغ این پروژه پرداخته؛ پروژه‌ای که مشخص نیست چه نهاد امنیتی یا حکومتی آن را اداره می‌کند و اطلاعات هویتی منتشرشده در آن از چه طریقی به دست آمده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/78389" target="_blank">📅 15:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78383">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MwSw1vFg085qE4gnvwfkfqjYtNfS0vPJehTqKtN0n83Q0PC6QaMIhlI90KklwUARpMTq6H8jHsPSqGIBn1RVLpKZnbzuRBn38_c8a9GrW2qI2Mp_tRYdAmHMsGNJECcpH1MJzRlRcgV5Qe0lfbYGLP0RKzs-6XuK5c4Sz9VFMAvb2wMY1ijhUY2oCDSb-b4SWzn-D5n49S19rS7gv0JN4VcMiT702sD0Hn9GcBJbW_WFr1rfKEldp6c_x9BoC1-h-OsXxsa-WXo0KrPiGX9XRtc_-k1Teu1u6aF4_Kp8FbT8kbe94coMb11Bii3s7h3ks4cEeQedxoRnD8o5eo5GKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Uv5gX5O9gleKxqi1mX5frIoMtP5xm7ONr_SScbAmPb0jMtnGitw0I4fM0TV5vXggU3MeJiriVXjrJia8-dU4ZUSXt_UIFqD4VpNrkbygwtltGa4XtCsIUQrr_L-BZuIQSFMYunq25axT7NiYjWHyLdcKyomA5uv1bwu8mIYLGy5WPJIzpRhpr7l3eF8kiRLjCyAd7EqZgLRGXeiAGyDYYctlea_xvNYneqga9vnBruPj3LCNmQxW5Vg6oCWVuNV1djfT4YjkkFMIv_B0eePI4b4gIby7XCcEf_fF4CtVlDu9RZWBeKHaibTMfu89JVtM4CBJzfKpXo8h8xUezOrqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IWkd4kXzAo-kQ0EZcY4tpJ7g8nvGPL7uRRbZ95iwaNcNcrSxasrTQTVQC3gANmGuKSX1W00t3vSuqqpySTveIjgFOXh3GnAkGeUpY4-1YSlSTY76SqJ1C4Q1kqpRiY0-FTF8vorNJh6IG8TnMYkIzsFPtK-SgkQCwKlF0nX9dMcG2kj_pwNKQBIugYtC0li3klBILbzSw-X2TjYCREnMgLnrb5_8G18OxprapcZo7XkBqza_Zof9CrBJdhtYRu9gs_gMeKYPjlPqwUHHJHnzOKLc5H2q-rrRSN3pRzHxYlAu4UKMbUL9VY1coXanKuMv2zHH_IVqv_fJSJ_dzoaZ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u0mc0SelzRw5jHbMbEkFtjis7rjmrX1pO7l59pCWuVqPREP2dkEcHnXmsJeYXxx-4ex5bOTy8etPYd27wIWmWmg5FIdnmFfvK4qH8ZaEoH_DmDFW5vZswenelFoMiJMToxHmJO7Pa4r0ZpA4EU4rCr1gj-WNiEbEzQF2mnBd219Xd2z23yq-Llq7I3CHMwqW8gpnSAPwmTU9cVh6SYuhu79bH8htn7_cr5qskMWiqA2i6PXQyapbZMg704-VhpigrDl8UKlnE_PjToYREjq-O8O3Tl4y4nMR2qcqbxyk0cV5Xg08YSqH7dhXfGmJpZFOifhpzt8PDXG3_enhkF5dgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d7MvS8HSART-SWBynMDHMPpHRqYnl7GUYEWyr5Z874rji7NurkiVXP2Z-_pc0kNjWAZ210B3UlYSSAgyrxwbNIQpRIMw5K4XRb5SPsqQ14oqlw0JYAnarkuNE6-qryEXpt8twYGPtOZHcZyL0hlv_xDJi8ccbIxASWLrt43jBTBMRicEZfnj4tyicQ5Xtqf1DEvEAxjBXtPWid-t21AA7TutPA9P6Rnotx4NGn1ujRD5elLiREtqhuaGud5ZeKF0qQSp8lo3joYinRxkJwNb2wUIgu9UiKsu7anbixRI5LfEw-Wiplw3OZi-iHGFA0RXi9t3_ekoy4aNyH9bx_8sAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YPLpdlIC2tvQnc1ODkrhCHw3120kCGd9MPMtEecPorrfK5s6VfoZ2HCKJJdtQtL8aiI9zfrRczwxlCSYEks5k_Fn-D8R0ChZf0aOxIF6g7X9qpLhL8JUx_Wmxks2nXxzrwfjpnApnC2MtnkfqVRTnQlVwJCvup91-1XSJgudnVabrxvNOiMzvqvYd1U5iT98zAAn3YOhmCmnhnz6MX6_0eWtiV_NhjZ7D_pS4W738hM2nIznmfS2DhlKcMsuXZ68Bc8Eb5c5pu2hhe2ad5IqYl_hv47b39xExV535KewZh5YCRmyX8MLc1eFUEE--rrwOfrYuoZNAMEIBnupmBQIrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«پویش جان‌فدا»، کارزاری وابسته به نهادهای تبلیغاتی سپاه پاسداران، ارسال پیامک برای ثبت‌نام شهروندان در دوره‌های «آموزش نظامی و امدادی» و سازماندهی آن‌ها در قالب «گردان‌های مردمی» را آغاز کرده است.
در پیامکی که برای شماری از شهروندان ارسال شده از مخاطبان خواسته شده از ساعت ۱۷ سه‌شنبه ۲۴شهریور برای شرکت در «دوره‌های آموزش نظامی و امدادی یگان‌های مردمی جان‌فدا» ثبت‌نام کنند.
پویش «جان‌فدا» از ۸فروردین۱۴۰۵ با محوریت «قرارگاه فرهنگی و اجتماعی قرب بقیه‌الله»، از نهادهای وابسته به سپاه پاسداران، راه‌اندازی شد. سامانه‌های اینترنتی، پیامکی، تلفنی و ثبت‌نام حضوری برای جذب افراد بالای ۱۲ سال در این پویش در نظر گرفته شده بود.
@
VahidHeadline
دیروز کلی پیام دریافت کرده بودم از شهروندانی که می‌گفتند در این پویش ثبت‌نام نکرده‌اند ولی اون پیامک براشون ارسال شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/78383" target="_blank">📅 15:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78382">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Amx8ftlczabuoukdisVr5pUt5-pavgSXw5gDighWvNQf23dJRpdWy5rrXc3rPLoLe4nMgjuvyjwZUsb21FJvEr2Cg5WWcEGMwwX14EUhImUPv5Kl_zuBm3DqYVXS2-lmK50Uw3--AmGfPiLKccg5mGiaxmCGQ3u1L1ads4ABiUVQALhlzJsEgvkZoKn2n2E_YYPCZ-68VqcxQRBfzhUmZ883yOl_f1BBGByXZDiErmRxkXYPnFSrzqEgeF_mk37l992c1vL-gHxHatoNnB2RrCyM676fLCPUKB83jqvIHe9x9MaS35qrSUVdG8FQrFmYhLaASzaKghgBHGfobnuxIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌دادگاه فدرال آمریکا روز دوشنبه، ۲۳ شهریورماه، به عدم اجرای دستور دولت دونالد ترامپ برای محدود کردن مدت اقامت دانشجویان و خبرنگاران خارجی در ایالات متحده حکم داد.
‌این دستور که به گفته قاضی دادگاه به دلیل «استدلال‌های بسیار ضعیف» دولت صادر شده، قرار بود روز سه‌شنبه به دست وزارت امنیت داخلی آمریکا اجرا شود.
‌بر اساس قانونی که دولت ترامپ سعی دارد به اجرا بگذارد، روادید دانشجویان خارجی و روادید افرادی که با برنامه‌های فرهنگی در آمریکا اقامت می‌گیرند، به چهار سال محدود می‌شود.
‌این قانون همچنین می‌گوید که روادید خبرنگاران نیز نباید از ۲۴۰ روز فراتر رود.
‌هر سه گروه، بر اساس قانونی که اکنون دادگاه جلو اجرای آن را گرفته، برای اقامت بیشتر باید بار دیگر اقدام کرده و روادید خود را تمدید کنند.
‌به گفته قاضی دادگاه فدرال، اجرای قانون جدید تعداد دانشجویان خارجی و روزنامه‌نگاران و خبرنگاران در ایالات متحده را به شکل قابل توجهی «محدود خواهد کرد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/78382" target="_blank">📅 15:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78381">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Df1no3rIEttb-5q5nqP38mGQX_PPiTe4DjOhcUYvBp2UTkLYKnoeeXzBluNSpo1uKnV_UhRwJz8ItylXcbpw-IEKg_CQSJjiFwmjYEwWQXWWLg1J-qxE-7IYMkzpno8zspH_iPpAEvcD7be5_tl9RFg5TXbs5QRfKBmxWN1SOnX9QrvIYf-OZeDTud4gMQ9tEGma9bwlUP0spnKb-bTlPxw_lo6YP13-3MWjDf4x0d9P1mq7reSUZ91Kdbh75m1XDoedsdK1fWwhNSZ4zhHwRzHyfNFMn9yOAx9oqnhu1VmGwZiuw9jXwKwZdueFiC_rN4Wti4_9g5M9YesiC88m8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه اتریش اعلام کرد برای سفر محمد اسلامی، رئیس سازمان انرژی اتمی جمهوری اسلامی، درخواست معافیت از ممنوعیت سفر سازمان ملل داده بود، اما درخواست رد شد.
بنابر اعلام این وزارتخانه، رئیس شورای امنیت سازمان ملل به وین اطلاع داد که درخواست به دلیل نبود اجماع رد شده است.
وزارت امور خارجه اتریش افزود با توجه به تعهدات بین‌المللی این کشور، ورود اسلامی امکان‌پذیر نیست.
اسلامی در راه وین برای شرکت در کنفرانس عمومی سالانه آژانس بین‌المللی انرژی اتمی بود که اجازه حضور پیدا نکرد. او از سال ۲۰۲۱ در همه کنفرانس‌های عمومی آژانس شرکت کرده بود.
ممنوعیت سفر از سازوکار «اسنپ‌بک» ناشی می‌شود که تحریم‌های سازمان ملل علیه جمهوری اسلامی را بازگرداند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/78381" target="_blank">📅 15:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78380">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r_cK_47TttvFqG8oynxpB_zzdOO4Ip1dDWShjiOi8gO682TUmm3sjLFg0wv8WdMYP5cV23o5kLgDYG57thtXb7-p8CquhjnLanMABdBdKipyZd3RC1FXNaYfThA9_CBppgqLtL-0Gjbh-pfBk3MhEz8z70vrUvoXIr4v3L5mwSU7HAJc1d5AHN148phOtp2lVZzECZb54S7Zyt7FUxtQcaLVoojariIeLI-7fvNUocqkttqZBGqyd8ULQxhXYhdY80_5Y1Hs59c9b68bRQ-AO2mhO27IprkUf5U_lrEKrvhIjPkWRxWNXQCyaakFYGZ1PqIhauskAmdQBTbHWwuBBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش الغایا پس از حمله در سواحل عمان و آتش‌سوزی در موتورخانه، به یکی از بنادر این کشور یدک‌کشی می‌شود.
بر پایه گزارش رویترز به نقل از مقام‌های عمانی، ۲۳ خدمه از شناور تخلیه شده‌اند و دو نفر همچنان مفقودند.
روایت‌ها درباره علت حادثه متناقض است.
سپاه پاسداران اعلام کرد الغایا با پرچم پاناما هنگام عبور از «منطقه ممنوعه» جنوب تنگه هرمز با مین دریایی برخورد کرده است.
فرماندهی مرکزی آمریکا ادعا را نادرست خواند و گفت شناور «ماه گذشته با موشک ایرانی زده شد و از کار افتاد».
سازمان بین‌المللی دریانوردی گزارش داده بود الغایا روز شنبه آسیب دید، بدون آنکه علت را مشخص کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/78380" target="_blank">📅 15:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78379">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vw4EaIsg1yRPU25ZsJBJ6UFrR1VIkSzFLjXLfuYOZn1jkY-wR_0mZHNuJvwKe1WMe9SF01qGsClgUbzzCDJM56NG2SoM6u-IoVvTnQ4-GCZSNbRG6QgFqY2m32oAEEjHNiiNC3yZKlC7VmZ3oFphK9xeW3gu67e2Tf948-iaxYKP01rKMiTtg9ci9WlP4Jzu_OV8xswjgv8v4v5ckldDQR7z1VvriPit_qL846fCRdpNX1VmXBNiNs2yGB7z_LGTLzjprMqSu0WLB_AEoBazq4rkK-FSDN7e4seLnMb7VH4ShH3W1IFHHYXUiBJKiSfrrpzAC2TZ36ZXOjV1irY2xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست‌کم ۱۰۰ معترض در ۱۳ استان ایران در خطر اعدام هستند
سازمان "حقوق بشر ایران" اعلام کرد دست‌کم ۱۰۰ نفر از بازداشت‌شدگان اعتراضات دی‌ماه در ۱۳ استان ایران با حکم اعدام روبه‌رو هستند؛ بیشترین شمار این افراد با ۴۶ نفر مربوط به استان اصفهان است.
بر اساس فهرست منتشرشده، پس از اصفهان، ۲۲ نفر در استان‌های تهران و البرز قرار دارند.
همچنین ۱۰ نفر در فارس، هفت نفر در خراسان رضوی، پنج نفر در مرکزی، سه نفر در یزد و دو نفر در سمنان در این فهرست ثبت شده‌اند. در استان‌های خراسان شمالی، گیلان، اردبیل، ایلام و قزوین نیز هر کدام یک نفر با حکم اعدام روبه‌رو است.
این سازمان می‌گوید فهرست منتشرشده تنها شامل معترضانی است که دست‌کم در مرحله بدوی حکم اعدام دریافت کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/78379" target="_blank">📅 15:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78378">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pkTAGmL0X5Zk-Pq3mFhBLStV-SgsDLt_jx8yatpitm8yVEKW3IIFp89bQjqNN0ie69Cea1mDmuC3f48eQr382vbM3EG_urj7Mdx3E2Yu03a3UhtTTVh-76CrYsPPcpcI7NJ3oBL5UeOgnLAeOmljDriYaUZIVx7W7FY3nC9q41dyuyXsl4yLnctoAQwNCaurppYcbzfPAUKmPEPo2jj-q6zuOfeZKLrnsi2cOBXtbSMHfQq2L5QYZyvoDSrZ-QY71L-KmJ9eG7CtDUnZC5JDSo2oWXViJ-oNcLrF5Fdwoy0iko-38fshm9g9B4c811GNRAfkebtcTiQklF9VqnOzQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، شامگاه دوشنبه ۲۳ شهریور ۱۴۰۵، از حمله پهپادی به دو «قایق صیادی» در حوالی بندر کرگان در آب‌های خلیج فارس خبر داد.
بر اساس این گزارش، در پی این حمله که تسنیم آن را به «آمریکا» نسبت داده، تعدادی از صیادان حاضر در این دو قایق مفقود شده‌اند.
عملیات جست‌وجو و امداد رسانی برای یافتن مفقود شدگان آغاز شده و نیروهای امدادی و دستگاه‌های مسوول در محدوده حادثه در حال جست‌وجو و نجات هستند.
تسنیم نوشته است جزییات بیشتر درباره این حادثه و وضعیت صیادان پس از دریافت گزارش‌های رسمی اعلام خواهد شد.
@
VahidHeadline
آپدیت:
اکسیوس: آمریکا دو قایق سپاه پاسداران را منهدم کرد
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78378" target="_blank">📅 03:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78377">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v5ro6hwiShxKblY6s9STiKAWZUd30coxkld4UZNL2hU2BKtgdqrlvQ1fclh7NTcvDo3pcldWwN0QOG7LLsEdd888VvErOT2Sx1slb1Ay0GUfnAaMJHgmnrjsBdnrxm_dvnc6-1eKCqyPfGxLmQu1xcn9fFNAqXDGvtHt0sr-GkBatH13ATmN8Wi76wGX9bhS1ijzc5TpaGjbAyUUBqUC55PJ5A0-CtcuGsWfEFQaxhNFOp67d7j7gqXdlEXmh8jKfwI5hzpGiqtg2sTOPXbMokIYnTSUo-gLLDt-7dZ-epQwUbINMME_22W3ZgTof06Q9JCh05yFbP4_IiZH2cNlgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی نیروی دریایی سپاه می‌گوید یک ابرنفتکش که به گفتهٔ آن قصد عبور از «منطقهٔ ممنوعه در جنوب تنگهٔ هرمز» را داشت، «بر اثر برخورد با مین دریایی منفجر شد».
خبرگزاری‌های ایران شامگاه دوشنبه ۲۳ شهریور با انتشار بیانیه سپاه، نام این ابرنفتکش را «اِل گایا» به شماره دریانوردی «۹۳۲۵۳۳۶» اعلام کرده و افزودند که «تلاش برای مهار آتش بی‌نتیجه بوده و کل نفتکش در شعله‌های آتش گرفتار شده است».
فرماندهی مرکزی آمریکا (سنتکام) این ادعا را «نادرست» خوانده و گفته که نفتکش «اِل‌ گایا» که با پرچم پاناما حرکت می‌کرد، ماه گذشته هدف موشک ایران قرار گرفت و از کار افتاد.
@
VahidHeadline
پست سنتکام، ترجمه ماشین:
🚫
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است یک نفتکش با پرچم پاناما اخیراً در تنگه هرمز با یک مین دریایی برخورد کرده است. این ادعا کذب است.
✅
واقعیت: نفتکش «El Gaia» با پرچم پاناما ماه گذشته هدف یک موشک ایرانی قرار گرفت و از کار افتاد. آخر هفته گذشته، ایران بار دیگر این نفتکش را در حالی که در آب‌های ساحلی عمان قرار داشت، با یک پهپاد هدف قرار داد. این نفتکش در حال حاضر توسط یکی از شرکای منطقه‌ای یدک‌کش می‌شود.
ادعای کذب سپاه پاسداران نمونه دیگری از دروغ‌ها و تلاش‌های آن برای ارعاب است؛ آن هم در حالی که می‌کوشد مانع تردد کشتی‌های تجاری در تنگه شود
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78377" target="_blank">📅 23:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78375">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G7A0bzbcmShNduKyqTS2asyHF6qGrvbASCnOj8n5VxjXyNgrJRr-aRj4hHX14LWdmJpstdwfNb4161_tu-DiwndN4VvsGn_PZhVhbatNXQJtQP612osb5sTm1AC6Vn8aB-UVvTdU-A_in_YCJEs2bH1KnrA3cJjrRd2cZd2rN4NlPmgC1db10mTyiWilMiffjGzhEvQxRs7Od60t8JyNl9VbI7pjbjTm_BdYPCDSubLw_kx0CuO0OM9Hm7WC7A8V8TxPHKObTqJREXyEg6KwiwnZxkZRubChSt55WIjFNCOVtQgXcW51yWwUNuCuD2qmTvYgdlYIX_q3X9OSpoj99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rGoJ3mN86TuiskLUlZ8JQGDlwwDqnFRiJBcn4Gr74d6SlDxAtLvjXFG-ocaHg0DRFqNO4_dA5EY8Z1L9nMPK5dFOcdrByX5QNJZK3SVO9Mv9dV0Cdu8-x8iZB5Bj7cFT7LiGkEHxwH3ssGxQNg3lWcNyKpoDGW8xfUklXO4Hx5Em1hNarXPWql1VMw5aBk5rKMkWW_uUABoXfhqYEGhs9sJAl_cCkzMb78cS-_JXY8-Ckm16FLP355Sxlzv_3U3TLxZPWyZVZXDoNiM2zCceZ4AXGGB7beZPZCJ8W8hgRni1PoJ7dA78cpH9gzxb8TRTS-oVQETDULfTHc7sXbLC1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پیامی در شبکه اجتماعی تروث سوشال تاکید کرد که افزایش قیمت‌ها در سراسر آمریکا ناشی از سیاست‌های جو بایدن و دولت او بوده است.
او نوشت که حتی بهای نفت نیز در دوران بایدن بالاتر از سطح کنونی بوده و دولت او مانع از دستیابی جمهوری اسلامی ایران به سلاح هسته‌ای نیز شده است.
ترامپ با اشاره به اینکه قیمت سایر کالاها به شدت در حال کاهش است، افزود که بهای نفت نیز به محض پایان یافتن درگیری نظامی با ایران—که به گفته وی زمان زیادی تا آن باقی نمانده است—مانند یک سنگ سقوط خواهد کرد.
در دوران ریاست‌جمهوری بایدن، به‌دنبال وقوع جنگ روسیه و اوکراین و بحران‌های بازار انرژی، قیمت نفت در بهار ۲۰۲۲ به بالاترین سطح خود رسید؛ به طوری که قیمت نفت برنت تا حدود ۱۲۷ دلار برای هر بشکه افزایش یافت.
@
VahidOOnLine
رئیس‌جمهور آمریکا در شبکه اجتماعی تروث سوشال از کشورهای جهان خواست پس از پایان درگیری‌ها، هزینه‌های ایالات متحده را برای حمایت از کشتی‌ها و کمک به عبور محموله‌های نفتی از تنگه هرمز بازگردانند.
ترامپ با اشاره به اینکه نفت در حال عبور از این آبراه است، تاکید کرد کشورهایی که هیچ کمکی به آمریکا نکرده‌اند، باید خسارات و هزینه‌های این اقدامات را جبران کنند؛ زیرا واشنگتن این ماموریت را بیشتر به نفع دیگران انجام می‌دهد تا خودش.
پیش‌تر کریس رایت، وزیر انرژی آمریکا، اعلام کرده بود میانگین تعداد محموله‌های نفتی که با حمایت نیروی دریایی این کشور از تنگه هرمز عبور می‌کنند، رو به افزایش است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78375" target="_blank">📅 23:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78374">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C7vMLK9P3i44JylXF1xOXqFDmHKiHgCy3uZSOWn5MjPMdD7eJPH19a1ujgDpO2-xu2CGJRi73Kxz-7jNe2Of58dk5k9sS-Ffk_DLx-8_QM-0VHDa2yIPVxbDO-PNPdVJQJtk2rcy7hBtHUMXoUw53azA-KA-VdRq9e3JhiaOJrNl9ZLLLiIzg_LeUZ3rWWbFCDKXZgWnw5HiM1D6aYAxoucfpKHUplMCmDFdu_s0AjKb1jrsBLj8bw5dmJfl1xNdvvMQWfesY9u9hxWn8VthT2uh8Q0h-MNLCtsVHA-hOHN5cov_U5k2K9iRci8T2yUd6vefQ-qaSyQ5mDU4J_CVCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایرانِ شکست‌خورده می‌خواهد خیلی سریع و به‌شدت به توافق برسد.
من تصمیم خواهم گرفت که آیا ایالات متحده آمریکا وارد مذاکره بشود یا نه — ایده‌ای که نسبت به آن آمادگی داریم. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
ترامپ نوشت: کشور در حال ورشکسته‌شدن ایران می‌خواهد سریع و به‌شدت به توافق برسد. من تعیین خواهم کرد که آیا ایالات متحده آمریکا وارد این داستان خواهد شد یا نه؛ چیزی که ما نسبت به آن نگاه باز داریم.
پس از انتشار این پست قیمت نفت اندکی کاهش یافت.
اظهارنظر اخیر رئیس‌جمهور ایالات متحده در حالی است که ایران گفته برنامه‌ای برای مذاکره با آمریکا ندارد و شروط متعددی را برای توافق با واشینگتن اعلام کرده است.
در همین حال، اسکات بسنت، وزیر خزانه‌داری آمریکا در راستای برنامه فشار اقتصادی بر ایران موسوم به «عملیات طرد اقتصادی» از همه افشاگران خواست تا چنانچه اطلاعاتی درباره «تسهیل‌گران تروریسم ایران» دارند در اختیار وزارتخانه تحت امرش قرار دهند.
او با انتشار پیامی در شبکهٔ اجتماعی ایکس خطاب به کسانی که در سراسر دنیا اطلاعاتی درباره شریان‌های حیاتی اقتصاد ایران دارند، نوشت: «این شانس شماست. اگر اطلاعات قابل پیگیری برای وزارت خزانه‌داری دارید، ممکن است واجد شرایط دریافت جایزه باشید، صرف‌نظر از این‌که کجا زندگی می‌کنید یا چه کسی فیش حقوقی شما را امضا می‌کند. اگر چیزی دیدید، بگویید».
او همچنین بار دیگر تاکید کرد که وزارت خزانه‌داری آمریکا عملیات طرد اقتصادی را «برای قطع تمام شریان‌های مالی رژیم ایران و حامیانش» آغاز کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78374" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78372">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=OX18vYB9KtaGcLNf3ftqnF96NnxC_aOLFrr0ecH4o5t2s24VpQn4-vmd3OTedkFk8obtfvxbxJCDMheH1VKL7__n5D0g-PTP3C9t71RZ5ljDVqrdnMdNYOJnV06z4y4omtl7HmxBNRhpgpU95Ldpk-Uz3AMO6EcgVu2KjouRHwoNmxjz1oDdw_i1DvZPrM00dbPae0OThJKH_nD6M28GsACsWQDZkOsx-FJ4ZhzGfzaqyv-vBMjX452-B5cSm1ijOUpECRRXJlHR_nzP41qzjm_kb5Hf0hdy-6ONU1hnPMZW-jRNqqBfoNX5DL7rQjx6kJEjYyX-HYkxvOXdubiDUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=OX18vYB9KtaGcLNf3ftqnF96NnxC_aOLFrr0ecH4o5t2s24VpQn4-vmd3OTedkFk8obtfvxbxJCDMheH1VKL7__n5D0g-PTP3C9t71RZ5ljDVqrdnMdNYOJnV06z4y4omtl7HmxBNRhpgpU95Ldpk-Uz3AMO6EcgVu2KjouRHwoNmxjz1oDdw_i1DvZPrM00dbPae0OThJKH_nD6M28GsACsWQDZkOsx-FJ4ZhzGfzaqyv-vBMjX452-B5cSm1ijOUpECRRXJlHR_nzP41qzjm_kb5Hf0hdy-6ONU1hnPMZW-jRNqqBfoNX5DL7rQjx6kJEjYyX-HYkxvOXdubiDUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رشت، حامیان حکومت شبانه به آشکده سحرخیزان حمله کردند.
در ویدیویی که آشکده سحرخیزان منتشر کرده بود، عبارت "آش برای افراد با حجاب رایگان است"، به دیوار نصب شده بود و در چرخش دوربین، چندین مرد محجبه در صف ایستادند.
همین بهانه‌ای شد برای یورش و تخریب مغازه.
این اتفاق یکشنبه، ۲۲ شهریور ۴۰۵ رخ داد.
دادستان بلافاصله علیه آن اعلام جرم کرد و مدیر رستوران بازداشت و خود رستوران پلمب شد. ولی انگار این واکنش از نظر لباس شخصی‌ها کافی نبود و دیشب ریختن رستوران رو تخریب کردند.
via
pkhwshhal
,
yaghma_fashkham
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78372" target="_blank">📅 18:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78371">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشگاه تهران - دانشجو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYTya7AGSmmjLwzExk_6FajAsto58B3o8CA2XM5Qo202z3Nj5SgKNmekgIMhcMMfMjhV4eb1LCOIe325AFbIzL5HpjdU_46H9DdpmUr3H_s9Hvm-S7lNaeLMp1VJe6ZnvAhtyVxVqSovHgXSIzibnUOsEWhCy7Ttc7jf3TlNvtKv_nCVvgxUhA8YNKLEHFgCbPK1QN3jtyi_0hUSox4X8ukrhylAvKnK11ZOY1_tgTKihZL9NGiDja_GGtHzbz3lMSvMrCGCQcpwI8RsJ7rYTF7M8O-X6_RLy_pzz6AvCumZWGFWzBBZrP6YT_tt6RVebFiiSVLnaeiYu3zi_6HD1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
اتهام «بغی» برای محمدپارسا گلچین، دانشجوی دانشگاه تهران و دارندهٔ مدال طلای المپیاد!
بنابر گزارش‌های رسیده به تهران-دانشجو،
#محمدپارسا_گلچین
، دانشجوی ورودی ۱۴۰۳ کارشناسی ادبیات دانشگاه تهران و دارندهٔ مدال طلای المپیاد ادبی، به «عضویت در گروه
باغی
» متهم شده است.
همچنین، «اجتماع و تبانی علیه امنیت داخلی» و «اقدام تبلیغی بر خلاف امنیت ملی» دیگر اتهاماتی‌ست که به این دانشجوی نخبه وارد گشته است. او در جهت دفاع برابر عناوین مذکور، به شعبهٔ ۲۶۸ بازپرسی دادسرای عمومی و انقلاب مشهد احضار شده است.
محمدپارسا گلچین، شنبه ۲۲ فروردین ۱۴۰۵ به همراه جمعی ۱۸ نفره از دانشجویان در جریان یک بازدید دوستانه، توسط مامورین مسلح و به‌طرز خشونت‌آمیزی بازداشت شده بود
. پرونده سایر بازداشت‌شدگان نیز در جریان است و در انتظار دریافت حکم و احضاریه هستند. درصورت دریافت اطلاعات تکمیلی، گزارش پرونده‌های سایر دانشجویان متعاقبا در تهران-دانشجو منتشر خواهد شد.
#سرکوب
#بازداشت
#دانشجوی_زندانی
دانشگاه تهران-دانشجو
اینستاگرام
🆔
@Daneshjo_UT</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78371" target="_blank">📅 17:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78370">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=Mym0NNl6c_lMQTAxm6Ieck5B4ZAj_UOHS-rDZp9ZACii0huzUENM9Zk5WB1zSGx-EvUCOELjF-IWFTCp2lssYd23I4vZQ3wjEZV-rXQF7aFgRfRR7rSxV-Z0vSYpBYxF_2HSljkCsWVwGKiZu3e_u4t0O2MdbXs6KYY5xr0EQJ13LaFTEfRV2PJs_cz728bicrngtSsmMZvkgo3CUCZmUI6y_ysiZJM0-dk42LAxBiXwXN7GH3dgI0_Ppo1PNmY8Iep1xt0XK2ySDGZUvqOXxLjWP1z-J2pzGVYVnJHlkWt2q2w7K1B67zwQj3xOuCyN1oUftFDBTfdNCp4Yhi31JA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=Mym0NNl6c_lMQTAxm6Ieck5B4ZAj_UOHS-rDZp9ZACii0huzUENM9Zk5WB1zSGx-EvUCOELjF-IWFTCp2lssYd23I4vZQ3wjEZV-rXQF7aFgRfRR7rSxV-Z0vSYpBYxF_2HSljkCsWVwGKiZu3e_u4t0O2MdbXs6KYY5xr0EQJ13LaFTEfRV2PJs_cz728bicrngtSsmMZvkgo3CUCZmUI6y_ysiZJM0-dk42LAxBiXwXN7GH3dgI0_Ppo1PNmY8Iep1xt0XK2ySDGZUvqOXxLjWP1z-J2pzGVYVnJHlkWt2q2w7K1B67zwQj3xOuCyN1oUftFDBTfdNCp4Yhi31JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفحه اینستاگرام رستوران «دستپخت بی بی» در تهران، به دلیل انتشار یک استوری با نوشته «هیچی کتلت بی بی نمیشه» به همراه موسیقی متن «بی بی گل» از معین، به اتهام «انتشار محتوای مجرمانه»، با دستور قضایی مسدود شد.
پیش‌تر نیز در سال ۱۴۰۱ نواب ابراهیمی، آشپز، در پی انتشار دستور پخت کتلت در اینستاگرام خود همزمان با سالگرد کشته شدن قاسم سلیمانی، بازداشت شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/78370" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78368">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RRW5ILFPT3LyCt0x8qJSCCkPo9DTVyTo6ihwiBfQ7ZiUakn390rlcE8HxcFw-1cQUd2vrgt5kE-LWHCmAajR8r-glCQwJkv0RVQMUxi2fSbyCa38L0t7UFjxjh2uZvME1gt4EYhPjXdRty5g9BZnI9GR_8zESrs6CkcIliWtk5IpmbK3do6iiAzvhs4O0gKInK3AxQJiokEMe0pwvUCa3TU0PZl0oxpAu8bwoMaFUCZ_bpA9HiYaku09sb74suJBvoo7oIgXtjbD7WDHuscTU0mlaQo0OpY9HSOu-bHQsn9wB_RZve4NhcVhfXiwWYwVoj-3K-VnZULqAq_ZzLgxag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/taC91rn4Vd-DSFe7FdBzjndoBHI0UUor2rD0rEn09unqQKYhbp8xfVQWjx2CW52QB_5z9_Qg2Jjxn3FymOWU4BC7ekmNwg4SDM6VZCoXLgLiBcdQSjC5Lnmw-xOTwYaLv8bAlHHUMIUpeemFUPijSJW3HUYF_tk9a9Vsu9gqlt02k6AeQhycS16Q5rNw-Gxyk7l9gTjm3SiHcUeUw167LaZdc21DQWwshqcdpo-DOpoyCiEpy83YXfrhtRwTy-xVKwd4baJ7HpclVE9vOfWHE9b_Obb0_dDCC4BHXyDHZAPfFYtviAmB1ZE_A6BbznYUtVblernZb2yA43d36Sa6AQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«یحیی سریع»، سخنگوی نظامی حوثی‌های مورد حمایت جمهوری اسلامی، از انجام عملیاتی گسترده با ده‌ها پهپاد و موشک بالستیک علیه اهداف نظامی در منطقه خمیس مشیط عربستان سعودی خبر داد.
سریع گفت پایگاه هوایی «ملک خالد» در این منطقه هدف حمله قرار گرفته و آشیانه‌های جنگنده‌ها، رادارها، باندهای پرواز و انبارهای مهمات از جمله اهداف حوثی‌ها بوده‌اند.
سخنگوی نظامی حوثی‌ها این عملیات را پاسخی به حملات هوایی عربستان سعودی به یمن دانست.
@
VahidHeadline
«محمد بن سلمان»، ولیعهد عربستان سعودی، امروز دوشنبه ۲۳شهریور۱۴۰۵ در جده با دریاسالار «برد کوپر»، فرمانده فرماندهی مرکزی آمریکا، سنتکام، دیدار و درباره تحولات اخیر منطقه گفت‌وگو کرد.
خبرگزاری «رویترز» به نقل از رسانه‌های دولتی عربستان سعودی گزارش داد این دیدار در شرایطی انجام شده که درگیری میان عربستان و حوثی‌های مورد حمایت جمهوری اسلامی در یمن شدت گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/78368" target="_blank">📅 16:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78367">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_xmH_DpXEwZ5KSYQN-YkjZ2nSSi4mUyiGbU61obRQnu0iv8c9DYQQrY_UZDLQdJpmFdBWC-E5B3pBsmeSQN7PV0HV1hnwmZwiqNcxiyQrAwZk3g6qdHvDychQKGtJ7nEwWHZLxn0F1ICRD4fO-WmiGh4xEiQWrTAqjKtjyvrg8PAwRACaFOjaLf-_UVLmWprZL5kZ3mPQEGSmgaXwAzrFglkwiiy4eygCbGfNONXJPTkOzGnOPe4zj2Y7nX2IwP_0w52hh0YNCD9MQ2D04joz7BHBf1qY4mgqM43hMBPROIr-mqNlE37OuqnRLdXXBT0noi-2fdu4Ca5swPxk3xFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین امروز دوشنبه ۲۳شهریور۱۴۰۵ گزارش‌ها درباره کمک نهادهای چینی به جمهوری اسلامی برای هدف قرار دادن یک پایگاه نظامی آمریکا در اردن را تکذیب کرد.
خبرگزاری رویترز به نقل از وزارت امور خارجه چین گزارش داد پکن «قاطعانه با این اتهامات بی‌اساس مخالف است».
این واکنش پس از آن مطرح شد که روزنامه «وال‌استریت جورنال» به نقل از مقام‌های آمریکایی که نام‌شان فاش نشده است، گزارش داد جمهوری اسلامی پیش از حمله موشکی ۱۷شهریور به پایگاه «موفق‌السلطی» در اردن، تصاویر ماهواره‌ای این پایگاه را از نهادهایی در چین دریافت کرده بود.
در حمله موشکی جمهوری اسلامی به این پایگاه نظامی آمریکا، سه نظامی آمریکایی کشته شدند.
براساس گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی نام نهادهای چینی را که گفته می‌شود تصاویر ماهواره‌ای پایگاه را در اختیار جمهوری اسلامی قرار داده‌اند، اعلام نکرده‌اند. این مقام‌ها همچنین دولت چین را به مشارکت یا دخالت مستقیم در این اقدام متهم نکرده‌اند.
«دونالد ترامپ»، رییس‌جمهوری آمریکا، نیز روز یکشنبه ۲۲شهریور۱۴۰۵ به گزارش‌ها درباره دسترسی جمهوری اسلامی به تصاویر ماهواره‌ای یک پایگاه نظامی آمریکا در اردن از طریق نهادهای چینی واکنش نشان داد.
ترامپ گزارش مربوط به دستیابی جمهوری اسلامی به این تصاویر، پیش از حمله‌ای را که به کشته شدن سه نظامی آمریکایی منجر شد، «کم‌اهمیت» دانست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78367" target="_blank">📅 16:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78365">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rof6776BhV8ZkNj7W_-ITKZT8_rU44lN3cKPplucNilhuCKAT3khzDHiZznPDv6jDOr-1AVdXHRCMZV-Q8PbjSt7N1ina_L-ZHE2sceDOVPgY5Kg328N-UamdTprZvZMr3KIryzETmYRhxCMkZPvU11PtlVB16qIpDAHLXzys7eEolNmScq7VIz8jhJrlEAQJeEkJC0fk5muSY4_hErxhZTqmQk4fu3Iy4uXs5XlK7aA_3IoAEHMeLZ-lRq7uS8vzHdRNZaoJlD5sgk76JvOhRwqse38SmBEFEkKTyFBggY-VuSFuqzw8CLZklgsmabCFBbQPNLM43aYKVmZJ_O2jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jv1RX0ADNBJTg47r2nYCvJH-7kajWe8zI-hfRaOFjC4cVTyl27MXTYlGHolTj4z3DGqqJ9DjkLSbIqLCUg5jLBvFgHJaPkYZ34nnnC-WKlNOPxDmx6t4Njs0XgjIbpYPn1IqafKQf1hNhxu0fYUiZcyPrUQd_74gaJ7TehUwarZtgQmoZ9Td3U2Sp8otltDzgIA7YNcONiSOsIC9TIvKztu4lvySd2Xgoo7roiM0V4ujqfCOsYM3aZJzXYuswPUnd7jwJnAYcAHyq2orBq12cuq6X91jYOX3VOh2DOX2-Wi21YPEguIPVwShcLYzckSZk2PXWqL89OwRgfSdOeKYTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز دوشنبه و پس از اعلام خبر صادر نشدن ویزا برای محمد اسلامی، رئیس سازمان انرژی اتمی ایران برای شرکت در نشست مجمع عمومی آژانس بین‌المللی انرژی هسته‌ای در وین، از احضار کاردار اتریش در تهران خبر داد.
بقایی با اعلام این خبر گفت می‌دانیم که این تصمیم تحت فشار آمریکا گرفته شده است اما این واقعیت، چیزی از مسئولیت اتریش کم نمی‌کند.
@
VahidOOnLine
پیش‌تر:
به گفته یک مقام آگاه که با اسوشیتدپرس گفتگو کرده، محمد اسلامی، رییس سازمان انرژی اتمی ایران، برای نخستین بار در چند سال گذشته احتمالا در نشست سالانه کشورهای عضو نهاد ناظر هسته‌ای سازمان ملل متحد در وین شرکت نخواهد کرد، زیرا از سفرهای بین‌المللی منع شده است.
این مقام گفت اتریش از کمیته تحریم‌های سازمان ملل خواسته بود برای اسلامی معافیت از ممنوعیت سفر صادر شود، اما این درخواست پذیرفته نشد.
این مقام که اجازه اظهارنظر درباره این موضوع حساس را نداشت، به شرط ناشناس ماندن صحبت کرد.
اتریش به عنوان میزبان سازمان ملل متحد در وین می‌تواند برای مقام‌های تحریم‌شده درخواست معافیت از ممنوعیت سفر کند تا آنها بتوانند در نشست‌های بین‌المللی سازمان ملل حضور یابند.
به نوشته این خبرگزاری آمریکایی، حضور نیافتن اسلامی در کنفرانس آژانس بین‌المللی انرژی اتمی نشانه دیگری از وخیم‌تر شدن سریع روابط ایران و کشورهای غربی است.
از زمانی که اسرائیل و آمریکا در جریان جنگ ۱۲روزه به تاسیسات هسته‌ای ایران حمله کردند، جمهوری اسلامی اجازه دسترسی بازرسان آژانس به تاسیسات هسته‌ای آسیب‌دیده در این حملات را نداده است؛ این در حالی است که تهران بر اساس تعهدات خود در چارچوب پیمان منع گسترش سلاح‌های هسته‌ای، از نظر حقوقی موظف به همکاری با آژانس است.
آژانس همچنین نتوانسته است وضعیت ذخایر اورانیوم ایران با غنای نزدیک به سطح مورد نیاز برای ساخت سلاح هسته‌ای را راستی‌آزمایی کند.
تحریم‌های سازمان ملل که دوباره برقرار شدند، شامل ممنوعیت سفر، تحریم تسلیحاتی متعارف، محدودیت‌های مربوط به توسعه موشک‌های بالستیک، مسدود کردن دارایی‌ها و ممنوعیت تولید فناوری‌های مرتبط با برنامه هسته‌ای است.
با وجود اظهارات این مقام درباره احتمال عدم حضور اسلامی در کنفرانس، خبرگزاری دولتی ایرنا روز شنبه گزارش داد که اسلامی تهران را به مقصد وین ترک کرده است تا در کنفرانس آژانس شرکت کند و با نمایندگان کشورهای مختلف دیدار داشته باشد.
مقام‌های ارشد کشورهای عضو آژانس بین‌المللی انرژی اتمی قرار است از دوشنبه تا جمعه در مقر این نهاد در وین گرد هم بیایند.
آنها درباره بودجه آژانس تصمیم‌گیری و آن را تصویب خواهند کرد و درباره دیگر مسائل سیاست‌گذاری، از جمله پادمان‌های هسته‌ای در خاورمیانه، گفت‌وگو خواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/78365" target="_blank">📅 16:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78364">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NYHt4T9uigyioriGxKxLVO8NdjaPVgpZ5mXBoFEN8tDe_x6WUBrVGLdbTpRu7bkSgjmcvWMWM3hI101STMG6qK4cBSVs7FgrGR1nHiEH9vRZAHOWkQfpL3Er3rVg7_ZHs2dkQ5mfbf9YIQcwHxkmQ8YeFGNIplzhLRk40UZ4BG-uDVHKQx-IgWLYfw3VUAvTHcyYztFXw3lkUobbmCwI_b8kPcPEl_HAXE0t4Gd082H7YBMpAq3t01G9dnucodSGfPJX0I9RnR90BbAhYyeyXZArNE7KCYG9k6i0u720UbhEWrMY_bbJ-b7lrttailXB5enjf1MetAJAkGOJmMDlQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آستانه چهارمین سالگرد قتل حکومتی مهسا ژینا امینی از اصفهان، رشت، فومن، مشهد و نیشابور ‌خبر از تشدید فشار برای تحمیل حجاب اجباری و حضور دوباره گشت ارشاد، حجاب‌بان‌ها و نیروهای لباس‌شخصی در خیابان‌ها می‌دهند.
یک شهروند گفت در میدان علیخانی اصفهان ون گشت ارشاد مستقر شده‌ است و ماموران «بدون تذکر قبلی»، زنانی را که حجاب اجباری ندارند بازداشت می‌کنند و با خود می‌برند.
شهروند دیگری فضای اصفهان را «به شدت امنیتی» توصیف کرد و گفت نیروهای گشت ارشاد در مناطقی چون جلفا، مرداویج، چهارباغ و میدان نقش جهان مستقر شده‌اند و با زنان بدون شال و روسری، برخورد می‌کنند.
یکی دیگر نوشت: «در اصفهان دیگر ون گشت ارشاد نیست، اتوبوس است. با اتوبوس دختران را جمع می‌کنند و می‌برند.
...
در مشهد نیز شامگاه ۲۲ شهریور، نیروهای مسلح وارد پارک ملت شدند و به زنان تذکر حجاب دادند.
شماری از شهروندان از رشت گزارش دادند برخوردهای قهری درباره حجاب اجباری در این شهر شدت گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78364" target="_blank">📅 16:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78362">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=qGtYyBuxEvRXYzFd59ryz-S-XeYAAdtjYEMdHsUiNN15F_6rtBk_c-aV2OcmFTBIF1qCucpPHqF9l_m5qMmMzkQi27oBB-LGAPsmrusnQuMQKLbZjNqNQoSfjkZ9BdQh2TaLLZ2eUUzj7bu9-Xx1p9yfkLK4iAIVMREWQu5zwklmdS2cRodDVdPaz5Cmx3-yWZpI_a2w9U2VQDaN6C8b88EgNx0yLoTGdJzVta1RCGoUfwvlTHF8boS8JrMAhm8SN8KvT6YNUD_yTpU73ffUikaGs2IWyX-0a5eayOoTusok9CMvzKPub2yblPllv871AXkLPDiytsAFFw941Keoqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=qGtYyBuxEvRXYzFd59ryz-S-XeYAAdtjYEMdHsUiNN15F_6rtBk_c-aV2OcmFTBIF1qCucpPHqF9l_m5qMmMzkQi27oBB-LGAPsmrusnQuMQKLbZjNqNQoSfjkZ9BdQh2TaLLZ2eUUzj7bu9-Xx1p9yfkLK4iAIVMREWQu5zwklmdS2cRodDVdPaz5Cmx3-yWZpI_a2w9U2VQDaN6C8b88EgNx0yLoTGdJzVta1RCGoUfwvlTHF8boS8JrMAhm8SN8KvT6YNUD_yTpU73ffUikaGs2IWyX-0a5eayOoTusok9CMvzKPub2yblPllv871AXkLPDiytsAFFw941Keoqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ویدیوی نجات خلبان آمریکایی در ایران
۲- یک نفر از ۷ نفر سوت موشک که داره به سمتشون میاد رو می فهمه.
سعی می کنه به نفراتش خبر بده اما نمی دونه کدوم طرف بدوئه. در نهایت یک انفجار هر ۷ نفر رو می بلعه.
A_z_im
سی‌بی‌اس پس از پنج ماه با یکی از دو افسر ارتش آمریکا گفتگو کرده است که در نیمه فروردین‌ماه هواپیمایشان در اطراف اصفهان سرنگون شد.
این افسر که براوو معرفی شده، لحظه برخورد موشک دوش‌پرتاب با جنگنده اف-۱۵ آنها را مانند برخورد یک قطار باری توصیف کرد و گفت به همراه خلبان که در این گزارش «آلفا» معرفی شده، تلاش کردند هواپیما را نجات دهند اما خیلی زود دریافتند که امکان نجات هواپیما نیست و باید خروج اضطراری انجام دهند.
پس از خروج اضطراری (ایجکت)، آلفا و براوو در حالی روی زمین در بیابان ناهموار در ایران فرود آمدند که حدود هشت کیلومتر از یکدیگر فاصله داشتند و هرکدام تنها بودند.
آلفا سالم فرود آمد، اما براوو خوش‌شانس بود که زنده ماند.
براوو گفت: چتر نجاتم در حمله اولیه آسیب دیده بود. یک لحظه به بالا نگاه کردم و دیدم چتری وجود ندارد؛ ترسناک‌ترین چیزی بود که در تمام عمرم دیده بودم. همان‌جا مکث کردم و دعا کردم: «خداوندا، اراده تو انجام شود. اما اگر قرار است از این ماجرا جان سالم به در ببرم، به کمک نیاز دارم.»
او در پاسخ به این پرسش که «فکر می‌کنید هنگام برخورد با زمین با چه سرعتی حرکت می‌کردید؟» گفت: براساس توضیحاتی که دادم و جراحاتی که داشتم، متخصصان معتقدند با سرعتی بین ۱۱۳ تا ۱۶۱ کیلومتر در ساعت با زمین برخورد کردم.
او افزود: یک معجزه در روزگار مدرن بود. باور دارم این اتفاق گواهی بر لطف خداوند در زندگی من است که باعث شد از آن لحظه عبور کنم؛ به‌گونه‌ای که هرچند دچار جراحت شدم، اما آسیب‌های فاجعه‌باری که می‌توانست توانایی‌ام برای زنده‌ماندن را از بین ببرد، متحمل نشدم.
این سقوط باعث شکستگی کمر براوو شد. او همچنین دست و شانه‌اش شکست، مچ پایش پیچ خورد و سر و صورتش بر اثر بریدگی و خراش خون‌آلود شد.
براوو گفت، مجروح بودم، اما همه ما آموزش دیده‌ایم که با شرایطی که با آن مواجه می‌شویم سازگار شویم و بر آنها غلبه کنیم. با وجود جراحات، تا جایی که می‌توانستم سریع از محل فرودم دور شدم.
براوو به سی‌بی‌اس گفت امن‌ترین جایی که می‌توانست به آن برود، ارتفاعات بود.
بنابراین با وجود شکستگی استخوان‌هایش تصمیم گرفت از مسیر کوه بالا برود و خود را به خط‌الرسی در ارتفاع حدود ۲۱۰۰ متر، برساند.
@
VahidOOnLine
چیزی که می‌بینم رسانه‌ها و کاربران فارسی‌زبان دقت نمی‌کنن اینه که این مصاحبه نمی‌گه که افسر آمریکایی با دست و پای شکسته کوه ۷ هزار پایی رو بالا رفته؛ بلکه می‌گه خودش رو به ارتفاع ۷ هزارپایی رسونده. بین این دو تا خیلی فرق هست.
در نظر داشته باشید که خود اصفهان بین ۱۶۰۰ تا ۲۰۰۰ متر از سطح دریا فاصله داره. یعنی ممکنه ایشون فقط با صد متر صعود خودش رو به ارتفاع ۷ هزار پایی برسونه.
Ardeshir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/78362" target="_blank">📅 08:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78361">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Opivj9WU2ApnFybIkaMFPLC4PsHXDNI3-Dqy22989SppLwyr2XLL3eIZiyusDEhIYyNmv4sVdBVX0jp7IkdAtVKtH6BDu3OobHb0nFn47WutuiVTZJ6jQtAlCQBmLkMwv8yQKoMLobQHpkUZ4xw8giyagDaiNYSgbWzTF3YzP9e_M0A7C-68ZhrViPTc5TJgB4mDtHsBLPZXBpuVGMbmUQOVhd2C-ndas4XO-REZbOFYrag0fedaPgMhzq2uGQX4J4trzDNHFYR7eat0SiiUyaHGWAIbCvK01I0ya77L6eYK2sa_zw4ntJzbX88P0F6DTx_5cF38p0SDqqyPdqcZ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه عمان از تعویق‌ نشست ایران و کشورهای حوزه خلیج فارس و منطقه خبر داد؛ نشستی که قرار بود روز دوشنبه ۲۳ شهریور در شهر صلاله عمان با محوریت وضعیت تنگه هرمز برگزار شود.
بدر بوسعیدی، وزیر خارجه عمان، روز یکشنبه ۲۲ شهریور در شبکه ایکس نوشت که این نشست «به منظور دستیابی به اجماع» به تعویق افتاده است.
او تاکید کرد عمان همچنان به تقویت گفت‌وگوهایی که به «ثبات و همکاری پایدار در منطقه» کمک کند، متعهد است.
عباس عراقچی، وزیر خارجه جمهوری اسلامی، پیشتر گفته بود که روز دوشنبه در نشست هشت‌جانبه وزرای خارجه کشورهای ساحلی خلیج فارس و دریای عمان در صلاله شرکت خواهد کرد.
قرار بود در این نشست درباره طرح ایران و عمان برای ایجاد سازوکاری جهت تردد امن کشتی‌ها در تنگه هرمز گفت‌وگو شود.
تعویق این نشست در حالی اعلام شده است که آمریکا پیشتر تاکید کرده بود در مذاکرات مربوط به تنگه هرمز مشارکت نخواهد کرد و هرگونه مذاکره مستقیم با جمهوری اسلامی را بر پرونده هسته‌ای متمرکز می‌کند.
مقام‌های آمریکایی به کشورهای منطقه گفته‌اند واشنگتن درباره وضعیت تنگه هرمز مذاکره نخواهد کرد و موضوع اصلی مذاکرات احتمالی با تهران باید برنامه هسته‌ای جمهوری اسلامی باشد.
مارکو روبیو، وزیر خارجه آمریکا، نیز پیشتر گفته بود تنگه هرمز نباید تحت کنترل جمهوری اسلامی باشد و آمریکا برای تضمین امنیت کشتیرانی در این مسیر اقدام خواهد کرد.
در مقابل، جمهوری اسلامی و عمان تلاش کرده‌اند کشورهای منطقه را در گفت‌وگو درباره سازوکار تردد کشتی‌ها در تنگه هرمز وارد کنند.
قرار بود نتایج رایزنی‌های تهران و مسقط درباره مسیرهای امن کشتیرانی در این نشست به کشورهای منطقه ارایه شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78361" target="_blank">📅 22:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78360">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0c_FGt4Bgaf3LUdA31ouPvYlv_YeC0XcueBji7PoJof20Ud-g6JaAGYyUyFsIDcB3mOk1i3-cPKpC28LwGHqIxL0lO_rK1bg79hmONe4XrbYmYvZp13vR9eSIEAwkpTg_dUKJuKgoc8vyoeBs4HvL0zwOa6Jz88N3ODCQdC2msu76m3zFQtZAYBIPynX5Tqcv3XRjNW1Q0iURg7dQ7GQE0FCI7d_0TF35Mef9GIpo5zqoiGVpFe38ZFIeNxaA8BL2krFiHWUZIYGGUJBRx5yFbvO4DWGTtwj_x8-7ifEgFT_a7cBPZok8shDI9dRFcP-0_EzGNAYp1e-huPrV8VLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه نیویورک تایمز روز یکشنبه ۲۲ شهریور ماه در گزارشی به نقل از چند مقام ایرانی نوشت، مسعود پزشکیان، پس از حمله نیروهای سپاه پاسداران به سه کشتی تجاری در تنگه هرمز در اوایل تیرماه گذشته، به‌شدت خشمگین شده و این اقدام را «بی‌پروایانه و غیرمسئولانه» خوانده است.
این حمله‌ها که منجر به آتش‌سوزی یک نفت‌کش حامل گاز مایع قطر و آسیب به شناورهای دیگر شد، درست زمانی رخ داد که ایران به توافقی با ایالات متحده برای پایان دادن به درگیری‌ها نزدیک شده بود.
بر اساس این گزارش که فرناز فصیحی به نقل از مقامات ایرانی نوشته است، پزشکیان پس از آگاهی از این ماجرا با احمد وحیدی، فرمانده کل سپاه پاسداران، تماس گرفته و با لحنی تند خواستار پاسخگویی شده است. با این حال، وحیدی ضمن سلب مسئولیت و ابراز بی‌اطلاعی، به رئیس‌جمهوری اعلام کرده که نه مجوزی برای این اقدام صادر کرده و نه شورای عالی امنیت ملی از این عملیات مطلع بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78360" target="_blank">📅 22:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78358">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/930e263d13.mp4?token=XZf_cdk7dE9MbpSiyqU58hzghLOxp7xfJiTkuXMKACh5ZFjYVGIm0RI7pQ6ryYYHuJOYHqPAaTLoiwG8pDliU0I0Qpm_a03bDQrqtpAgxkQFXfnfxEiaaTAUAks1-9AOBg92UX2edtZQq_1AqHqnHXzuGzDK1tJuqfI6B_4EeiEAaBBKwULtaow37oCMV1dDR8mjbk3-85bGZbxHk9zE2EJ7R50YLcK0h7UrC-zzZvFIpTh671Q5zrJj_s7maWjTe5cnKxHYfe5pXaWTYXmLTLO2Bs9tLrw4oNftwvdU1zc3mnbej2AT1oOSo96x8vwA6m7z3_7GDHWC6DbntimIYg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/930e263d13.mp4?token=XZf_cdk7dE9MbpSiyqU58hzghLOxp7xfJiTkuXMKACh5ZFjYVGIm0RI7pQ6ryYYHuJOYHqPAaTLoiwG8pDliU0I0Qpm_a03bDQrqtpAgxkQFXfnfxEiaaTAUAks1-9AOBg92UX2edtZQq_1AqHqnHXzuGzDK1tJuqfI6B_4EeiEAaBBKwULtaow37oCMV1dDR8mjbk3-85bGZbxHk9zE2EJ7R50YLcK0h7UrC-zzZvFIpTh671Q5zrJj_s7maWjTe5cnKxHYfe5pXaWTYXmLTLO2Bs9tLrw4oNftwvdU1zc3mnbej2AT1oOSo96x8vwA6m7z3_7GDHWC6DbntimIYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز پیش، پس از اعلام نرخ سوم بنزین در ایران، تصاویری واقعی در شبکه‌های اجتماعی منتشر شده بود درباره اینکه بعضی از تلمبه‌ها در جایگاه‌های سوخت (پمپ بنزین) امکان نمایش همه ارقام بنزین ۱۰ هزارتومنی رو ندارند و مجبور شدند در ادامه نمایشگر یک صفر بچسبونند روی بدنه تلمبه.
حالا محمدباقر قالیباف، رئیس "مجلس شورای اسلامی" در «ایران»، اون انیمیشن رو پست کرده.
ولی درباره قیمت سوخت در یک کشور دیگه:
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78358" target="_blank">📅 21:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78357">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fiubxrc6g_CjRlr7YCISvOkMfPHhtWAO42pphyf9xQU7Zg278zu-xfKXhY_RDOdo7-uEzRvdgp1LCxUGuWhVmkkHe4gZqZ7jObaoSzKkgRkZ9L50u2rhUjPd4Bxbhcf936WN3Imqzq0qroQhFvx6x_PPusOGVlXABp2xJvFvVtbJn6ZQLhVWZW_XZ5hdeJ0FW0M_S2fRS7EWEqpURKjMnKY13bSHNFPExRDcRfVEg-kM2McdQ6n6VFVIc1P1-tUsoccvj2AxBcsOKKryCEP2Z7fmEQWrjObkWI-NecwDlS0kOBHy0cH3fB5w1OkeaLut2Ez1vwPLQmYSa-0MfpfjKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین رسولی‌نسب، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در شاندیز، به اتهام «محاربه» از سوی دادگاه انقلاب مشهد به اعدام محکوم شده است. او در حال حاضر در زندان وکیل‌آباد مشهد نگهداری می‌شود.
خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، روز یکشنبه ۲۲ شهریور ۱۴۰۵، گزارش داد حسین رسولی‌نسب به «محاربه از طریق مشارکت در تخریب اموال عمومی» و «اجتماع و تبانی علیه امنیت کشور» متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78357" target="_blank">📅 18:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78355">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iV1ix0ug2ra0cJUWzLwinnkG9prFqAunCIxayMLcufUtAx945QLFH7Pu4IbkJ31xOW1S1ou4V-RWsSvsK2UEDVRiqr88RUG3VoCUkaAIdBO0FPX8aBAib88yuSagIsibXemGfM6699iQoYN2hMtenjNWonDIVMQGsBhygZldt2xssy-rKgy1NhBauFlGJlmNq4FEie0pYanVx-DBPspkUHpdYTpP3lf3C8rL3K-5p2F5aEKrYmyVE83VgIV2xdLcTpSh4IhEb8UZH-NMNe-T-Av-iqUu_Sz9BDQaKd7L9a3rIqU-ihfM2TPqIFLrw0xxW5ooPwLIP_He0WRwMMjKkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q5ko8mtuJU-qlCisnaI9WYgiNjKBfyALbFkdrl14NRh0HqY-ygbLfP8vk8BIwGxTkE5D8JJjNRlwjT2syK2vmihxBgTo6oh_X_WeMFn-I3LlIXfqyCvvTyYj6qx9bs7AlMxYv9huGi6VTS3bt0NwFimr3eIeW7cF4sOcUWtWy1AyKEnMhIdaaqhH0LpUTEqd1hcrSRI7J2e1rJkYJmiI504xEo10GyGP5jOCSFk7WBg-jSKRHJEkDdoPMXkPDQQUwYg_8iEd0mxxcqCFVG8aujcw3Qugoihcx4qpxcpdZci2qL_5Emqub8GR_idx0xypLKv7Oh42ND5xyq_bIUmJkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان ثبت احوال: در کارت ملی‌های جدید از هوش مصنوعی و بلاکچین استفاده کرده‌ایم
quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78355" target="_blank">📅 18:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78354">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NM3gtMiXTRHSStuwV3o1hYQMjParQgmQtaS2k-HvatxxWlT5Aw96QSRtrG9aNG7KJiIPfyH8vUc8J7GJJkf4cjlt1awJ100TV6NoGltbSnU7aPzz-2EWSMAT-MJIXJyCmS1_N03VZcUrIEnxKOEsfy8SmZG1xCrJ4ELuf_mIkCfrPUvrj1SXAhXFpgJJIU9mZ4j1nB6dVQENaMExvy6IGg4FU7mAkFuVSKMwNbM-uR3kQ6G-EICeav8CFmjwu062qCbE1VxmE0VTjcJT098SuedISdy_c-66-NhVQk3Qa5QTqb8CMkjly2LSJy0M9frTCCa9vAoU3ELQ-83SQ_Ygpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز یکشنبه ۲۲ شهریور۱۴۰۵، گفت «موضوع ایران» ممکن است پیش از انتخابات میان‌دوره‌ای آمریکا پایان یابد، اما در هر صورت جنگ با ایران بلافاصله پس از این انتخابات تمام خواهد شد.
ترامپ در جریان سفر به ایرلند و در حاشیه مسابقات گلف اوپن ایرلند، درباره احتمال توافق با جمهوری اسلامی گفت ایران به‌شدت خواهان توافق است و به‌طور مداوم با آمریکا تماس می‌گیرد، اما واشنگتن تنها توافقی را می‌پذیرد که به گفته او «درست» و مطلوب باشد.
او همچنین در پاسخ به پرسشی درباره دیدار وزرای خارجه کشورهای خلیج فارس و دریای عمان با ایران گفت این موضوع برای آمریکا اهمیتی ندارد و تصمیم درباره دیدار با جمهوری اسلامی به خود این کشورها مربوط است.
قرار است این نشست روز دوشنبه در عمان برگزار شود. ایران می‌گوید یکی از موضوعات مورد گفت‌وگو در این نشست، مسیر جدید تردد در تنگه هرمز خواهد بود.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز بار دیگر گفته است شرط ایران برای بازگشایی تنگه هرمز، بازگشت آمریکا به تعهدات خود در تفاهم‌نامه اسلام‌آباد است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78354" target="_blank">📅 17:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78352">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WKjYeU2-EEMpq49hGaWHgeMQhxSbJoAxYz8_DESv69joYlznin1XZJMDc5bZ_X9t6JpE1lmk7o5UfpmfNy32F58vCVU9_FQ9JeTQBaLxm7XaSHVhuUJsd_I-kFW4F-sbZbpm8-VDEAdB8Qu4ORUK70JEvgO_O2zHJvpsOjXhfOCqhenxtPNwfgI4QvSNJM8BQx-oDnOf5Pe6W4hGkMVNAj0bOwqc_00uYEbXwZygURes39H-01ES7TRrHb2L0tovYcu9po2dH8u6O3-Ls3swgLguRFDl2zmgGJkhRqoxmtJYYPAOajpjGWldqFiQhc3a4b7pPjhsqbvAg7Q1EJZbOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WdoLXGtYCWL3LW54oM6vlN2Ik9HfoT8i4FVamkk6iant13Z6YqRzaI0y_XKe9RZgaKh4_e8HP3_5-79xiRsnwKFoj_ndhCV9mpWbjq0w_sSr8gPBF6Xt32MQ1AAGuSV9A8AQ6ldH9kJHBOmlLWQ7hQ1GlTXLR1CtXNAxropycq4F5ySZyBIp8KoClp_YYU1TiLTaDHEhY5eqmL7-ecI4NfnPJeRd5i8LCMcQDkVILt3Zl8eTQxPn8TJJPeYWcjiGokewdvqxccqC34D617ejr0jmWC1ErwcvLFfMfALl27vFUS_QOlpZKy0R4caMvdEPTOSRrvMWK2JW3E51JpWBMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) روز شنبه، با صدور یک هشدار امنیتی، از هدف قرار گرفتن یک کشتی در تنگه هرمز خبر داد.
این نهاد نظارتی دریایی اعلام کرد: «گزارشی مبنی بر وقوع یک حادثه در محدوده تنگه هرمز دریافت شده است. یک کشتی هنگام عبور از تنگه هرمز هدف اصابت یک پرتابه ناشناس قرار گرفته است.»
@
VahidOOnLine
امیر تیموری، فرماندار شهرستان قشم، اعلام کرد یک کشتی تجاری حدود ساعت ۵ صبح امروز در محدوده جزیره هنگام و ساحل شیب‌دراز جزیره قشم هدف قرار گرفته است.
به گفته فرماندار قشم، در این حادثه یک نفر کشته و سه نفر دیگر مجروح شده‌اند.
تیموری عامل این حمله را آمریکا اعلام کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78352" target="_blank">📅 15:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78351">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=dYSgHyEeWBpJeq90qms4SjfgqwoLlB7zaJZm5eiuBbfJNLBEotGOsOb0Wfr9LYL7UpkbIEU37Rud2-AQDZUjuMXTdCHVRg_WHJ3Ff9PrF9AEdifTsZ9rUb-Ft3rEUqUzATlWCx_RVDn3SRBB7ddDn9egTKUYziUosyOwcGhp6mBuGj3qRm3vd74I3mKCYXc59uGuTGiQSYGADl27hdwJAjuz0CjQp5tnUspGFWp314H6OgGyNJRhE7j_8WMXxFJlH8SJYppL3mFYIsinJalhtZxV4qGvfrPqlIYKZWfHEJ0vpiKuWcuPeYgRnSc87Dij7sjqBK8YRKRetH0HYJyoFYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=dYSgHyEeWBpJeq90qms4SjfgqwoLlB7zaJZm5eiuBbfJNLBEotGOsOb0Wfr9LYL7UpkbIEU37Rud2-AQDZUjuMXTdCHVRg_WHJ3Ff9PrF9AEdifTsZ9rUb-Ft3rEUqUzATlWCx_RVDn3SRBB7ddDn9egTKUYziUosyOwcGhp6mBuGj3qRm3vd74I3mKCYXc59uGuTGiQSYGADl27hdwJAjuz0CjQp5tnUspGFWp314H6OgGyNJRhE7j_8WMXxFJlH8SJYppL3mFYIsinJalhtZxV4qGvfrPqlIYKZWfHEJ0vpiKuWcuPeYgRnSc87Dij7sjqBK8YRKRetH0HYJyoFYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تور اجبارى اتاق شلاق براى "عبرت" متهمان
یکی از شهروندان با ارسال ویدیویی که مخفیانه از اتاق اجرای احکام شلاق ثبت کرده، مشاهدات و تجربه مستقیم خود را با بنیاد عبدالرحمن برومند در میان گذاشته است؛ روایتی که به‌زودی در قالب یک شهادت‌نامه تفصیلی منتشر خواهد شد.
او درباره انگیزه خود از انتشار این ویدیو پس از چند سال می‌گوید:
«آنچه در جریان بازداشت و صدور این حکم بر من گذشت، در برابر حجم بی‌پایان ظلم و بی‌عدالتی شاید اهمیتی نداشته باشد؛ آنچه برای من اهمیت دارد، تاباندن نور بر گوشه‌ای از این سازوکار مخوف است تا همگان ببینند مردم ایران برای داشتن یک زندگی معمولی با چه مجازات‌های تحقیرآمیزی روبرو می‌شوند.»
@
IranRights
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78351" target="_blank">📅 15:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78350">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=YgZWUD4eR-jPYEBR4aFeTISKBGPMqTavMRJj-7yXNUYQZjrJ8agvjeJdqxiWbIaJBnRN1gYKpoRWQPjyawW4j14EChPv7Qs06uXeYrJnsuTodGHgcfNbu6f4JkPamuTjcqJmhRNT4tduZUtYx92weWNVwIGQ__fmjLBNJzge_L2Vk3eSHEZYzqynYa0OrRfu-eIyH_aU6EVdsymzuwMUbn6HHsEqF-zWUWe5sNi0-XAp-koBdBqTvnvk96Co-grVrcFxPZZkXeyHARBZ-N6DTj5-UuD6tzkIj7DD8J5pP3vA1WnDJkCxMhMf-YuTA56cB_UZ_mpV5-jXB-yf3A47Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=YgZWUD4eR-jPYEBR4aFeTISKBGPMqTavMRJj-7yXNUYQZjrJ8agvjeJdqxiWbIaJBnRN1gYKpoRWQPjyawW4j14EChPv7Qs06uXeYrJnsuTodGHgcfNbu6f4JkPamuTjcqJmhRNT4tduZUtYx92weWNVwIGQ__fmjLBNJzge_L2Vk3eSHEZYzqynYa0OrRfu-eIyH_aU6EVdsymzuwMUbn6HHsEqF-zWUWe5sNi0-XAp-koBdBqTvnvk96Co-grVrcFxPZZkXeyHARBZ-N6DTj5-UuD6tzkIj7DD8J5pP3vA1WnDJkCxMhMf-YuTA56cB_UZ_mpV5-jXB-yf3A47Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهوری آمریکا در جریان دیدار با مایکل مارتین، نخست‌وزیر ایرلند، در دوبلین بر اعمال کنترل مقتدرانه و یک «محاصره دریایی باورنکردنی» بر تنگه هرمز تاکید کرد و گفت این اقدامات مانع از جهش شدید بهای جهانی نفت شده است.
دونالد ترامپ همچنین گفت نیروهای سنتکام به‌طور میانگین روزانه ۲۵ شناور و قایق را متوقف و توقیف می‌کنند؛ اقداماتی که به گفته او بیشتر آن‌ها در تاریکی شب و در جریان گشت‌های شبانه انجام می‌گیرد.
این در حالی است فرماندهی مرکزی آمریکا، سنتکام،
امروز
اعلام کرد طی ۶۰ روز گذشته و از زمان ازسرگیری «محاصره دیوار فولادی» ایران، مسیر ۱۰۰ کشتی تجاری را تغییر داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/78350" target="_blank">📅 23:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78349">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUEBfETqG9Q6HBeIlfgzWpWfr5DOZT2FDvMW7_pNcbxWFL8Fnn0lV9_4lEEmenYzR7sraUMSjhgwxyrH9RGaV_27kD47MbPJ5JM4PPsb3rINv-wAP7N9V2WLBFfb9RownDarwJsoE-rWj-QOy2GTxHbR8MJbnZ2MT30cOwsm5s9fOdN8trbgeSf3WGCfRFB6TpnTh8MnmG8N0OtycCREa1fWwKAcfCcVYiU8atVsh1MoimRcl3AUBKnjcpYS_SyTIjFkDDfKOcQ4xUy0iY1uVYtcsD78OPBcprUA0MfhaFWt-GkoDnHieVim0BZl6RslYNMB3iHjeIsducwk0VA6sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واژگونی یک دستگاه اتوبوس حامل کارگران مجتمع مس سرچشمه، در صبح شنبه ۲۱ شهریور، یک کشته و ۳۸ مصدوم برجا گذاشت.
سید محسن مرتضوی، رییس مرکز فوریت‌های پزشکی رفسنجان، با تایید این خبر گفت ۳۸ مصدوم این حادثه برای دریافت خدمات درمانی به بیمارستان منتقل شده‌اند. به گفته او، بررسی‌های اولیه نشان می‌دهد ورود یک دستگاه ون به مسیر حرکت اتوبوس باعث انحراف و سپس واژگونی آن شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78349" target="_blank">📅 21:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78348">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b10cD4tA-JgJPt6sC69fQQL4K0Ta3-UHLspDmCXWV4HTJboLQI6dqHucpctyDucpGBVuf1sMpV23Ss3gdQhPtXgMO_FxJueuOavNVu8xtAUh8qU0H6QT8PHK8S_zcvsVYGa4pP0Og2m0_dZp69rufgKKuGeb7ScxOPUf94qAv6bIplPP03-y3q1DwUD1ldJv_Xl5KHnVqsEhntt8YK0DEHHzZWhmwnxpgVw5nhbYwLbNv_Lwr_I1NwPtm55q7yisLipAbEpamR1YYjBF7yIQZwlJOqvf_ATw0uzGb6lxT3HVu8M1rL-EMLnTFfkGByWWHgHpZfJBna5i6xk2OA1eyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع امنیتی عراق به خبرگزاری فرانسه گفتند نیروهای امنیتی این کشور سکوهای پرتاب پهپاد را منطقه دورافتاده الطیب در استان میسان در جنوب عراق و در نزدیکی مرز با ایران کشف کرده‌اند.
همزمان خبرگزاری رویترز به نقل از دو منبع نظامی در عراق اعلام کرد این منطقه مرزی پس از کشف سکوهای پرتاب پهپاد بسته شده است.
کشف این سکوها پس از حمله به خط لوله نفت عربستان سعودی انجام شده است؛ حمله‌ای که ریاض و بغداد گفته‌اند از خاک عراق انجام شده است. بغداد روز شنبه گذرگاه‌های مرزی شلمچه و چذابه را نیز بسته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/78348" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78347">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FG-RFBVNiWrD0Jh18quAmcuQyPEdsXIQZZIDDDGwHNuw4pBYJgEDvLJjBPJuR7cgrUegqcV5_3LA1vWLWaXltRjon4JyoH4Nkr8jPpueDD0YBK_rKuW6QU4eyE_T5Gtup9X83b5uJMBJZmGCWPkRy-a3j1uYuRT556X7inmB49jCmQSgFvU7RI934q4-q-4k-Kh10qLwWL6zigL5-Mf-tyQSfbXgwgAIs46Ku9HvHSNXvf8co-uCT9dmRX99PLqVdeZ9BE1nwVAf0I2a0j-NudR48H9VoIkpxIPPNmwRXHE3T_YvVzlxQl98ILwgQbJAMum9bEZsP1m8ne6BDAp03Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، به نقل از یک منبع آگاه گزارش داد تفاهم نهایی جمهوری اسلامی و عمان درباره مسیرهای جدید کشتیرانی، به معنای بازگشایی تنگه هرمز نیست و باز شدن این تنگه به اجرای هفت شرط تهران از سوی آمریکا بستگی دارد.
این منبع گفت تهران و مسقط پس از گفت‌وگوهای فنی و دیپلماتیک، در اوایل شهریور درباره جزییات مسیرهای جدید ورود به خلیج فارس و خروج از آن به توافق نهایی رسیدند و قرار است این تفاهم به‌زودی با حضور وزیران خارجه کشورهای منطقه اعلام شود.
بر اساس این گزارش، تفاهم تنها میان جمهوری اسلامی و عمان است و کشورهای دیگر، از جمله عراق و کشورهای ساحلی خلیج فارس، برای اطلاع از جزییات مسیرها و ترتیبات تردد در نشست حضور خواهند داشت.
مهر نوشت مسیر ورود به خلیج فارس به‌طور کامل و بخشی از مسیر خروج از آن در آب‌های سرزمینی ایران قرار خواهد داشت و تردد در این مسیرها بر اساس ترتیبات تعیین‌شده از سوی جمهوری اسلامی انجام خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78347" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78346">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=cSfqBZCfLwu_ng9Uk5wVRHdOIAfPAPCvobv0yKkEra_svShlNsOmRWL5C9bdmCKGptMdbazSDXJ4nAM14y2qCHF_fF-LP-LexFAPK_SZcJCMIQr6_SZz_5xDHz_9KnqyZm0EfkAkXwLwPKeNjs65V7oh7nz739T_DL8WA4YZ3v2jRxPgaUGsMls9KY180Mouy7UAT_YYzZv4oH4u0qLHQ8rJlGDijpAMWbloWv7MwqICKYg3YhBXn22m7e9rSe67ULc3cLI27zmemtmBSH6Krm1TqLsoS-d7VHZEh2hHBVwtWyczEV5XJBZQ2DiI1Xo5-eG7ZIiiExNxZ8-INgIHPw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=cSfqBZCfLwu_ng9Uk5wVRHdOIAfPAPCvobv0yKkEra_svShlNsOmRWL5C9bdmCKGptMdbazSDXJ4nAM14y2qCHF_fF-LP-LexFAPK_SZcJCMIQr6_SZz_5xDHz_9KnqyZm0EfkAkXwLwPKeNjs65V7oh7nz739T_DL8WA4YZ3v2jRxPgaUGsMls9KY180Mouy7UAT_YYzZv4oH4u0qLHQ8rJlGDijpAMWbloWv7MwqICKYg3YhBXn22m7e9rSe67ULc3cLI27zmemtmBSH6Krm1TqLsoS-d7VHZEh2hHBVwtWyczEV5XJBZQ2DiI1Xo5-eG7ZIiiExNxZ8-INgIHPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت امور خارجه، روز شنبه ۲۱ شهریور ماه گفت اطلاعات تهران نشان می‌دهد حمله موشکی آمریکا به لامرد از خاک یکی از کشورهای حاشیه جنوبی خلیج فارس نیز انجام شده است.
اسماعیل بقایی در گفتگو با رسانه‌های دولتی ایران گفت این موضوع نشان می‌دهد آمریکا «برخلاف همه قواعد و اصول حقوق بین‌الملل» از خاک و حاکمیت ملی کشورهای دیگر برای حمله به ایران استفاده کرده است.
او تاکید کرد ایرانیان این موضوع را پیگیری خواهند کرد.
بقایی همچنین گفت برخی کشورهای همسایه، برخلاف «اصل حسن همجواری»، اجازه داده‌اند از قلمرو آنها برای حمله به ایران و «ارتکاب جنایت جنگی علیه مردم» استفاده شود.
در نهم اسفند ۱۴۰۴، یک سالن ورزشی در لامرد فارس، مورد حمله دو موشک قرار گرفت که منجر به کشته شدن حداقل ۲۱ نفر، از جمله ۴ کودک، و زخمی شدن ۱۰۰ نفر شد. این حمله اندکی پس از حمله هوایی به مدرسه شجره طیبه میناب رخ داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/78346" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78345">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcaLr9jStebvPwCTKAA1KSVpRmyFQml-3bjUjK3Pw4MF7yFdw5gdVrtNXAFl9gCaZsbOQwYnRRU40SFLp4zcwXWznGJo-P1uTGg1DEEWdz6OjAf7dRwL5VA2XkVC79L5v3ZqKJ28MFs7GZLjHhlUqs_EaEaQ6nwqP7MC-MLOPMzPOAqiF1jOaanSLvLb5nEJNFVSaIPGKoQk2atiKOGs4uab_hbmm9bqM8dDT2-xvJZ_oNlFuWHMrLH7ARZ-eaUXwa0ss8pZsQrjVJG-U0URm7iRpy7WK12v8rXvjR3NTuDCPsCQLUvA8DrveffW-7YHGTXVFg0Wz_GGAQrt6jAHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت احتمالاً جمهوری اسلامی مسئول حمله هوایی به عربستان سعودی بوده که به تعطیلی خط لوله شرق به غرب انجامید.
او روز شنبه در دوبلین و در پاسخ به پرسش خبرنگاران درباره مسئولیت ایران گفت: «فکر می‌کنم مسئول‌اند، احتمالاً خودشان‌اند.»
ترامپ افزود با محمد بن سلمان، ولیعهد عربستان، گفت‌وگو کرده و او را «دوست خوب» خواند.
رئیس‌جمهوری آمریکا همچنین گفت حوثی‌های همسو با جمهوری اسلامی با دولت او تماس گرفته‌اند و اعلام کرده‌اند نمی‌خواهند آمریکا مستقیماً وارد درگیری شود.
او گفت: «آنها به‌مراتب ترجیح می‌دهند ما درگیر نباشیم و بیشتر شناورها را عبور می‌دهند. فقط یک کشور هست که از آن راضی نیستند و ترتیبش را می‌دهیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78345" target="_blank">📅 15:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78344">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=Q9EOvBHHt6TX-qjg-RhzLb6f-2ggm7H_y0raVLAYN1CJbquqlZL-AhjWL2GAp5xXFBZHmQJ6SabiqeFF_1FLj4X29fIbot_e1DX2VINv-z7sn6n8ppbr1UzkMO3KKwSiIomiGSULx60iQ5tHP8UTa-zAvLh5LdxHtnm8IEMF2fOqi1R3FhsaPPuzzT7u9WgGwOFlorrAVik9jHx-4URPmS7Ng-CU80dNTAOuvw0g_b709pVJZrfokuiLm_-nXBcAqxxK76D2hpE533rUXAwbC6zYPr0vo5RXHZuYE0YyH9D_930s6QrYLEussz-J_pCibx8J0Ap7h-N7eJCvI_BOzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=Q9EOvBHHt6TX-qjg-RhzLb6f-2ggm7H_y0raVLAYN1CJbquqlZL-AhjWL2GAp5xXFBZHmQJ6SabiqeFF_1FLj4X29fIbot_e1DX2VINv-z7sn6n8ppbr1UzkMO3KKwSiIomiGSULx60iQ5tHP8UTa-zAvLh5LdxHtnm8IEMF2fOqi1R3FhsaPPuzzT7u9WgGwOFlorrAVik9jHx-4URPmS7Ng-CU80dNTAOuvw0g_b709pVJZrfokuiLm_-nXBcAqxxK76D2hpE533rUXAwbC6zYPr0vo5RXHZuYE0YyH9D_930s6QrYLEussz-J_pCibx8J0Ap7h-N7eJCvI_BOzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای منتشرشده در رسانه‌های اجتماعی نشان‌دهنده ازدحام در خروجی مرز بازرگان است.
برخی گزارش‌ها دلیل اختلال در تردد از این گذرگاه مرزی را «محدودیت‌های ظرفیت پذیرش در سمت ترکیه» عنوان می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78344" target="_blank">📅 15:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78343">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBMQ2dAEj2BNfas5028lYo5liv3HPwKnHp26EmBBgwCvxNwLkUSW-R8wc3PoxnzQulVRBdmbqiT_gAudzY1Gf4m5FIuqP4tLVtqd9O64vrqPxGlMoFtTp9SUGQJ9jXb8IfJM8-owqcrwHVujoQVeugQXcFQAjG5LXPGLlKvp49-6bcDVWUcYU24hbHDorpxGk2YfMnQr9gGQIiJfQfpSEmqUWUiUuTVWgiG0XEhl7JyUc_0WJnDYt90cvvcLjyTfnUWBhSQdME248AW81UJqe9oY3tRKqm1AdcvU6nWrl5vXKNxkjBjMdOxjYnmKjObDLPCXIzJ9ac2CEokBwF0ufg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون استاندار خوزستان اعلام کرد مرز چذابه نیز همچون شلمچه از بامداد امروز با اعلام مقام‌های عراق تا اطلاع ثانوی بسته شد. بنابر اعلام ولی‌الله حیاتی، هیچ تردد کالا و مسافری از این مرزها انجام نمی‌شود.
ساعتی پیش رویترز بع نقل از دو منبع امنیتی نوشت عراق پس از تازه‌ترین حملات پهپادی صورت‌گرفته به عربستان سعودی، دستور بستن گذرگاه مرزی شلمچه بین عراق و ایران را به عنوان یک اقدام احتیاطی صادر کرد.
مرز چذابه در استان میسان عراق قرار دارد و دفتر نخست‌وزیری عراق بامداد شنبه فرمانده عملیاتش را برکنار کرد. این برکناری پس از آن انجام شد که تحقیقات تأیید کرد آخرین حملات پهپادی به عربستان سعودی از خاک عراق انجام شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78343" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78341">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mmkZMHWJfLcD-vIgtEt0JJWoQvXz7qMWZMvtCQRzbOQZVcOD6GBIePgNKIQB-ZWmDLPbhghKNLo3lNbdLxkbAhjVigNTsuhqnVQfeu37Dg9T9Q6jounFNtjcZQSGEWSH-hPwf73f8Di8aMXAf7T6Z1Fwuo2qQzeIjRkEsavHSg74JKtR3xzqw2VNP3rQzHCAdsHLvTRo5dnOdx6RjEhcfL_lRW5SwbcP-Ykf4GKYAWX_S2VbdPouJoQjiULmCxGVz2Gdrxl8-aGoXhZWVdAobWBal4nYTZ0mIxgD0CUtWQMPPEZXSJULwFmnsqUMHnaGiSo0tmA59KBn6zsYWI4INw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lqLASEQFV75BHSrOllDMQbA2mCaFOVGING3wYIzA12FMwL_i2m7zVxB3vA2NBIU9jRxlOzH6OVsEoaLpUGgU3nlVVB5dNDpiYmwN8tMjLkYyguYfSodZ0avsxLDfDhE3ljJKg07jd2L5SBGZYPeMP9UeycgVU5FSDyvuHcV75G-_vz97o6P9l3VtZ_w9T4GlAQnfDNFcuojp9XKlrVuA3tQs-Of8zmhDX8yk3Uf-k2bL4NQHhEzgqkMmEm54LcTYIP9fBqNWMLO4MS5rtK0YG1m1TC-orGn_XQPEplydYpmlUUzFClZNos_jj0_VY3b-Dh0BHKjRLavdKsZcjfJLCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درگیری میان نیروهای نظامی و امنیتی جمهوری اسلامی و افراد مسلح در منطقه «بخشان» سراوان، پس از بیش از هفت ساعت همچنان ادامه دارد. «شیوار نیوز» از حمله به نیروهای حکومتی از دو محور، شکسته‌شدن بخشی از حلقه محاصره و خروج شماری از افراد مسلح از محدوده درگیری خبر داده است.
این درگیری حدود ساعت چهار بامداد شنبه ۲۱ شهریور ۱۴۰۵ و پس از محاصره یک خانه مسکونی آغاز شد. شبکه اسناد حقوق بشر بلوچستان پیش‌تر از استقرار گسترده نیروهای نظامی و امنیتی و استفاده از سلاح‌های سبک و سنگین در این منطقه خبر داده بود.
براساس اطلاعات منتشر شده از سوی شیوار نیوز، نیروهای نظامی و امنیتی پس از آغاز درگیری، محدوده حضور افراد مسلح را محاصره و مسیرهای منتهی به محل را مسدود کردند. بااین‌حال، در ادامه افرادی از خارج محدوده محاصره، نیروهای حکومتی را از دو محور هدف قرار دادند.
@
VahidHeadline
قرارگاه قدس نیروی زمینی سپاه پاسداران اعلام کرد در جریان درگیری با افراد مسلح در شهرستان سراوان در استان سیستان و بلوچستان، سه نفر از نیروهای سپاه کشته شده‌اند.
بر اساس اطلاعیه این قرارگاه، این سه نفر با عنوان «پاسداران گمنام امام زمان» معرفی شده‌اند.
قرارگاه قدس همچنین اعلام کرد که تا پیش از ظهر روز شنبه، چهار نفر از افراد مسلح ناشناس نیز در جریان این درگیری کشته شده‌اند.
این اطلاعیه جزئیات بیشتری درباره هویت افراد مسلح، گروه یا سازمان وابسته به آنها، محل دقیق درگیری و چگونگی آغاز درگیری منتشر نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/78341" target="_blank">📅 15:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78340">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jhUXEyJ9myWzbAj5G_4jOc3R-ErPDQSUHOX8MUD4YYZyLEJuyrJhMdM7b3ccrzycmH00XInQcLL6qP636RT0XRmYHebz8ka5CMgMZLcZKCw92wdj5zp9pH8tno_Z0aDWxzZSwnhXq8aQK5rq5ueB4OUazyv-HtbPr2kJOKMPmNJqYZf4WXB_0JEMdCSJXTz1mt67MQoRMcInomg0skNv02AsnnO_a7f-KSWdK3HmcKBNlPJYChICTEKTxsObn2G1ITL8lWd0Um-MjQl8MdLdhJgSK9-IqkYfzXHimAOZNilAOUtq01AmwKUNG6mdJvltEPwuDtpgsTqWOY6FnQW0LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سودا ابراهیمی شمس‌آبادی، بلاگر ۳۳ ساله اهل بندرعباس، که از ۹ فروردین در بازداشت به سر می‌برد، به اعدام محکوم شده است.
بر اساس این اطلاعات، شعبه سوم دادگاه انقلاب بندرعباس به ریاست قاضی خواجه‌حسنی، سودا ابراهیمی شمس‌آبادی را با اتهام‌هایی از جمله «توهین به رهبری»، «فعالیت رسانه‌ای و تبلیغی برخلاف امنیت ملی»، «اقدام اطلاعاتی و امنیتی به نفع دولت‌های متخاصم» و «عکسبرداری و ارسال تصاویر برای رسانه‌های فارسی‌زبان خارج از کشور» به اعدام محکوم کرده است.
دادگاه همچنین او را به دو تا پنج سال حبس، محرومیت از برخی خدمات دولتی و مصادره اموال محکوم کرده است.
حکم اعدام سودا ابراهیمی شمس‌آبادی روز اول شهریور به وکیل او ابلاغ شده است.
بر اساس اطلاعات رسیده، ابراهیمی شمس‌آبادی در جریان دوران بازداشت، به مدت ۲۰ روز در سلول انفرادی نگهداری شده و در دوران بازجویی تحت فشار شدید قرار داشته است. خانواده او در این مدت از محل نگهداری و وضعیتش اطلاعی نداشتند.
قاضی خواجه‌حسنی که این حکم را صادر کرده پیشتر در سال ۱۴۰۲ از سوی مقام‌های قوه قضاییه در زمینه‌هایی از جمله صدور بیشترین احکام و جدیت در انجام کار مورد تقدیر به عنوان قاضی نمونه قرار گرفته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78340" target="_blank">📅 15:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78337">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LpEjFW9XCSRc5DK1407XYxLTI6VG6wAYDMSzNma8ONUkzPxQqmP8xuOaX3F-K0E824kBRXvNylSc3GpoPk35JTwBEUsCYVLLIpkvZ2jaZ5LycvplwzWSlKmqtFmu6X42c3goMhHexxsMoL3oh7tpyyBHD5bjvc_KVxf-xKa0tj-i_2bKU2KyuMuXTQvmT89uFjakW8Z3BBGET8ypW6qRqbMS9Ltbfe3BD7gyIDaJw8W1Ph3TKgJABBX6HfkmQUnVVLKwWA4aShTYtWKJolNgyBJqdkrYzqv2lvV1LfGoleqO43m5QrADxXcMIAGv2U1iufcK6DhqZSpqSJc5IrQmmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e-w7jrZQSed09WHRmXBaaeklUB5t0OEIECSOZA59fXDxNbA3uxcifYzVjc2Jan2p9XWtKRXGru6IXrvRwoyaU03AIfqbwxc-law2Vr7L6AfnNvOUi87X0olk2-ptKWwTCtjMi-5CjWbZqktBUMIpYp_cvFJizu520Zgz8HgN22paGeLw783ZKvCIKmEv2lkcb3z_5whphhluFpJ2Dc-ZfMGF0rM60sl9kahPd19bdg_ljvm7r1ZoWdkbFGkCBoTgdXPmC-cqBCYGDDqGUfHR7h_moupwPgi0YscX8PJZ_9_E_LpW9Xj0yYzi2A4cpWAyH6Z2S9Y5GTb3uo6SwelQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EUkNeazAVRsq1OO9UvDrmelVpNjeUIL1i1pvUYyIStt5J_dl-B-lGYc032etSslvRzvQrXtCsblp5w-3n2-Kootvog2kYTzcgpgL9j8JfvIk5BLB3Twlk-0xvhLdq8TmcxnBZTwy2w1TUFQhvtX2OPsQuqLXoXTrVI0Lyf6EUIp6YZBYYh-SlT94JyTsG3kJ_hkLAV4Mrlv1IrNtj6viNHF8NKe1x__ukGl9BuQg_bxQm0DBL4cjqodQF_twjcw9I-VeL8FAszAnMbrDoZzhtbZkfAaWYBOmLsErXXwYW9cBDi2YteX3-Cfvy0fFhfb4jDd5bwWVW-peqlDlFA21Ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت انرژی عربستان سعودی روز جمعه ۲۰ شهریور با انتشار بیانیه‌ای اعلام کرد که خط لوله انتقال نفت «شرق-غرب» (واقع در مناطق ریاض و مدینه) صبح پنجشنبه هدف چندین حمله قرار گرفته است.
در این بیانیه آمده است که به دنبال این حملات، عملیات انتقال نفت در خط لوله مذکور به صورت احتیاطی متوقف شد.
این رویداد همچنین منجر به مصدومیت تعدادی از افراد شد که خدمات درمانی و مراقبت‌های پزشکی لازم به آن‌ها ارائه گردید.
@
VahidOOnLine
وزارت خارجه عربستان سعودی اعلام کرد خط لوله نفتی شرق به غرب این کشور با پهپادهایی که از عراق پرتاب شده بودند، هدف حمله قرار گرفت.
وزارت خارجه عربستان سعودی افزود بنا به درخواست نخست‌وزیر عراق، در این مرحله تصمیم گرفته است اقدام تلافی‌جویانه انجام ندهد.
@
VahidOOnLine
خبرگزاری رویترز گزارش کرده که بغداد دستور تعطیلی گذرگاه مرزی شلمچه میان عراق و ایران را صادر کرده است.
دو منبع امنیتی عراقی به این خبرگزاری اعلام کردند که عراق این گذرگاه را به عنوان اقدامی احتیاطی و در پی حمله پهپادی از مبدأ عراق به خط لوله نفت شرق-غرب عربستان سعودی، بسته است.
گذرگاه مرزی شلمچه یکی از مسیرهای زمینی اصلی میان ایران و عراق است.
براساس گزارش‌ها پهپاد شلیک شده به عربستان از استان میسان عراق شلیک شده است. این استان در قسمت جنوب شرقی عراق و هم مرز با ایران است که مرکز اداری آن شهر عماره است.
@
VahidHeadline
رویترز نوشت: به گفته این دو منبع، عملیاتی گسترده برای تعقیب و پیگرد عاملان این حمله به عربستان در جریان است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/78337" target="_blank">📅 05:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78336">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78336" target="_blank">📅 22:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78335">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b03z06xdhQx2kUgMN0iqIZzKn4MYOBHAiWmLr51c4BWMPNGtH9bwQpRthtztXXNnVAm8C4U2qvgN5a-dQPpmsSt8qe1_7TgeQVLAjjETV4a5JVztxsYqnKk9OdnLAO4gUIk4XpFwttDPVLyJzra6QKPp86JL0iaOUJ-NseV2quFF6iTEgrQXYc9JLBA0JskEosN4M2-_8AjPDsKqHjMA_G9R1iuAQDp-Cy493oe9GPOlZChAGxqnUwD2tzHLytGGN9F_JHCWlCn2yGv4l4dmEVa-rhUr6H4S2FCj0de03PixzBZm2m5t1MMhNtVFMXdC9bBpHnSUmUcMBfKg7SCUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس دولت چهاردهم جمهوری اسلامی که به هند سفر کرده است روز جمعه ۲۰شهریور۱۴۰۵ در پایتخت این کشور اذعان کرد که فشارهای آمریکا بر ایران به مرحله «دشوار و خطرناک» رسیده است.
او با اشاره به این که جهان امروز در یکی از «پیچیده‌ترین مقاطع خود» است، خواستار «همکاری عملیاتی» کشورهای عضو بریکس شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/78335" target="_blank">📅 20:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78334">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=V2Dm7dOeorEZ-oh1EU_2HvNphHmsqJDW2ba4ZDAMR0hrBNZxRQ9X-RkFwAGN95ROPR1wFRy0lmvvtrXcCqAjANwbFAfih0eXciyYjEGhN2M4YRdvaoJQ_HDmbKtAmIFXxBrMXQ1j4jQ1N5NuOx7tKWHEn3euSFgH6WecSjCpEKK6_Y-vLnnAVwt8CavW4EdOEcFOtySFOHRmzAwqE2Rvq1UAqHAdfHNjmikr99eAM4AhUEEcDGAbQhx1lLhspzdK1D3nDsEnxwEbqeB5xPxtujwI6tkluw25ow5VBNDvfNbVnl2bDGR9iF9bVJgXzCwCttB6e62UlMUBVBzlUP44Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=V2Dm7dOeorEZ-oh1EU_2HvNphHmsqJDW2ba4ZDAMR0hrBNZxRQ9X-RkFwAGN95ROPR1wFRy0lmvvtrXcCqAjANwbFAfih0eXciyYjEGhN2M4YRdvaoJQ_HDmbKtAmIFXxBrMXQ1j4jQ1N5NuOx7tKWHEn3euSFgH6WecSjCpEKK6_Y-vLnnAVwt8CavW4EdOEcFOtySFOHRmzAwqE2Rvq1UAqHAdfHNjmikr99eAM4AhUEEcDGAbQhx1lLhspzdK1D3nDsEnxwEbqeB5xPxtujwI6tkluw25ow5VBNDvfNbVnl2bDGR9iF9bVJgXzCwCttB6e62UlMUBVBzlUP44Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواهر امیرمحمد شاه‌کرمی با انتشار ویدیویی در صفحه اینستاگرام خود، از حضورش در مکانی خبر داد که به گفته او، برادرش آخرین لحظات حضورش در آنجا را پیش از بازداشت سپری کرده بود.
او در توضیح این ویدیو نوشت: «۱۸ شهریور، برگشتم به همان خیابانی که آخرین نگاه‌های برادرم آنجا بود؛ تا صدایش را از همان‌جا دوباره بلند کنم. این‌بار ایستادم برای صدا زدن نام امیرمحمد شاه‌کرمی.»
در این ویدیو، خواهر امیرمحمد با در دست داشتن تصویری از برادرش، نام او را در همان خیابان فریاد می‌زند.
امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، در ۱۸ دی‌ماه در شهر قدس بازداشت شد و پیکر او حدود ۶۰ روز بعد به خانواده‌اش تحویل داده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/78334" target="_blank">📅 17:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78333">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/957af9390d.mp4?token=c42VMGJOc2Vkeyf95rHEymqcg1l6xjPNeF1U6x0UPpXKT7BHK9EbYWZF8cfZKGkDkCduk-heaVU80dhIT7sh2p1DgWKQ1IXWTmYREFWtiWM1Ihqx8bsXwUI3KveD5zZdtilHF1KYRiYwV3w2Gi0M5wcLYPygd9YhTfn0tvdg1JGG8BsNuX4CWX0-FSckbPJ_yqGZQ-iouerp960PVV7dHGoUJHhebtJo_60NuZ-6uKCeUMiNqS693jqMCmGCjolGHR_f2TYJ8gGZGTOd00n8VMzMOzqOydDebCg-jZfnbySgTqOYP9WVyIX2g-E79gmrB_29Pven7O1kKk_7-xWBjA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/957af9390d.mp4?token=c42VMGJOc2Vkeyf95rHEymqcg1l6xjPNeF1U6x0UPpXKT7BHK9EbYWZF8cfZKGkDkCduk-heaVU80dhIT7sh2p1DgWKQ1IXWTmYREFWtiWM1Ihqx8bsXwUI3KveD5zZdtilHF1KYRiYwV3w2Gi0M5wcLYPygd9YhTfn0tvdg1JGG8BsNuX4CWX0-FSckbPJ_yqGZQ-iouerp960PVV7dHGoUJHhebtJo_60NuZ-6uKCeUMiNqS693jqMCmGCjolGHR_f2TYJ8gGZGTOd00n8VMzMOzqOydDebCg-jZfnbySgTqOYP9WVyIX2g-E79gmrB_29Pven7O1kKk_7-xWBjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تسلیحات کشف‌شده در علی الطاهر را ایران برای حزب‌الله فرستاده بود
نخست‌وزیر اسرائیل روز جمعه ۲۰ شهریور اعلام کرد نیروهای اسرائیلی در جریان عملیات در ارتفاعات علی الطاهر در جنوب لبنان، مقادیر زیادی تسلیحات را از زیرساخت‌های حزب‌الله خارج کرده‌اند.
بنیامین نتانیاهو با اشاره به تسلیحات کشف‌شده گفت: «مقادیر بسیار زیادی سلاح از آنجا خارج کردیم که سال‌ها توسط ایران سازماندهی و تامین مالی شده بود.»
ارتش اسرائیل پیشتر با انتشار ویدیویی اعلام کرده بود، نیروهایش پس از به دست گرفتن کنترل عملیاتی ارتفاعات علی الطاهر، زیرساخت‌های زیرزمینی و روی زمین را منهدم کرده‌اند. به گفته ارتش اسرائیل، این شبکه بیش از دو کیلومتر امتداد داشت و شامل ده‌ها راکت، موشک و پهپاد و همچنین موشک‌های ضدتانک، مین و مواد منفجره بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78333" target="_blank">📅 17:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78332">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iD1j9M8zuSa1Spm2mKaTWDXszyrZleYlSD_OSlXDzYBQT4fc94jtxlBuXc-Il8OiDVK2aZoU_lYIyNz72HRuzXmK7hCJ6zO3OsW2l8pb0VtMtPK5zrhKkhSw02644UsqL4ud-TG9MX43CH0XSkaXnU8l1eby-jitWTUbVmIBvluzPjLFLxvbp4-jHcktCeZZ2LoicpWAGLfRYPKVybxnYV8SxQ6J74h1uOBrm-sOT4wYX0p9M9YiARrCkt_MDOUJA-pSVmocSb88csaUekPdSsBtMBxcL9KR426_nR4GXLWfQNsFyfaimxUhcDNqoc_I3g2_HkZynO_gSWAWnz5MHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، گزارش‌های رسانه‌ای مبنی بر آسیب‌دیدن هواپیماهای آمریکایی در جریان حملات موشکی اخیر جمهوری اسلامی به اردن را رد کرد.
او پنج‌شنبه ۱۹ شهریور در مصاحبه با شبکه نیوزنیشن، در پاسخ به سؤالی درباره این گزارش‌ها، گفت: «نه. هیچ خسارتی وارد نشده است. هیچ اتفاقی نیفتاده است.»
کمی قبل از اظهارات ترامپ، شبکه خبری فاکس به نقل از یک مقام ارشد آمریکایی نوشته بود که موشک‌های بالستیک ایرانی در جریان حمله گسترده موشکی سه‌شنبه، ۱۷ شهریور، به هواپیماهای جنگی آمریکا مستقر در اردن، آسیب زده‌اند.
فاکس‌نیوز این خبر را به گزارش جنیفر گریفین، خبرنگار ارشد خود منتشر کرده است.
شبکۀ خبری سی‌بی‌اِس برای نخستین‌بار این موضوع را منتشر کرده بود که در جریان حملات موشکی ایران به پایگاه نیروهای آمریکایی در اردن، «چندین هواپیمای نظامی ایالات متحده، آسیب دیده‌اند».
ارتش اردن روز چهارشنبه ۱۸ شهریورماه با صدور بیانیه‌ای گفته بود که ایران در طول شب قبل، ۲۰ موشک بالستیک به سمت اردن شلیک کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78332" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78331">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iKVm3ESUjTr5bNvdENM0VjD3akap8ED7qcOEnJxolyt0_lwZajb7G0FoliiMGUB3QyjWAodO_wyA5elW5ijHZkrPL-kixJu9On9kKLrl_UOkQXNhDp3hOFVS2Ye8iFT9IN18jWQ_EzRQtCJREfMv2rBTqTm7AjIcd_t7iSvV7RbnkvfiU3RkhF3t3te2NFYH05OGPqwxLJwzEYhmS3CvpZXnsBfM9mrXWwOF2IGXqBcUXQpin0qMXBurNHamE7Kg6lrz5wUt5nax22KjK32uLT6N8zgVvY05qi4JUivWHAUCMtu91RkxRzqvQVW9yM0eEx5rp-Ow0O53uLUaLOVPaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت آمریکایی «آنتروپیک» اعلام کرده است که سه عملیات مرتبط با حکومت ایران را شناسایی و مختل کرده که در آن‌ها از مدل هوش مصنوعی «کلود» برای تولید و انتشار محتوای تبلیغاتی، طراحی سامانه‌های نظارتی و تهیه اطلاعات مرتبط با هدف‌گیری نیروهای دریایی آمریکا استفاده شده است.
این شرکت روز پنج‌شنبه ۱۹ شهریور در تازه‌ترین گزارش اطلاعات تهدید خود، مجموعه‌ای از موارد سوءاستفاده از مدل‌های هوش مصنوعی آنتروپیک را تشریح کرد. این گزارش فعالیت‌های شناسایی‌شده و مختل‌شده از دسامبر ۲۰۲۵ تا اوت ۲۰۲۶ را پوشش می‌دهد و علاوه بر ایران، مواردی مرتبط با چین، روسیه و کشورهای دیگر را نیز بررسی کرده است.
بر اساس این گزارش، آنتروپیک حساب‌هایی را شناسایی و مسدود کرده که از «کلود» برای اجرای عملیات نفوذ با هدف تاثیرگذاری بر افکار عمومی استفاده می‌کردند. سه مورد از این عملیات به عوامل همسو با حکومت جمهوری اسلامی مرتبط بوده است.
آنتروپیک می‌گوید هر یک از این عملیات از سوی فرد یا مجموعه‌ای انجام شده که یا مستقیما در یک نهاد تبلیغاتی حکومتی ایران فعالیت داشته یا به نمایندگی از چنین نهادی کار می‌کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78331" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78330">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBxDLw9zoTdkCH2DDAB4rhiMwUXEwJ9gpG6SiuAqQYmTjoEewglkzqnOAi1mvY9iZK4B2OUu3T1d0RYQ2loZmx_6_YFfWDcK8ZGmyk3efxvWZ8ZC5yZKsnxxviftScgHlVGTFohsPU32ewg0zZUl28OVutMBIIyKnjgmjpSfKstukN-JCHqowh4q65Mpm3Vs831X8kkttwigXHi0ElgSrxB_9fevKhZa3LSo0dXK0E1wxoj1boNObxEaVxUZRCpx5u0EzKtnZ7jEqJnMYh7twE4YJICMKBhVpym7YiFI0QV6tk8QC9DFE--T_spHWxD-4FKErHxZvjHOsgK9YCMuuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت مخابرات ایران با انتشار اطلاعیه‌ای در سامانه کدال (سامانه اطلاعات جامع شرکت‌های پذیرفته شده فهرست شده در بورس) اعلام کرد هزینه مکالمه تلفن ثابت با تلفن‌های همراه از روز جمعه ۲۰ شهریور ۴۵ درصد افزایش می‌یابد.
به گزارش انتخاب، بر اساس این اطلاعیه، سقف هزینه مکالمه تلفن ثابت با تلفن همراه از ۶۲۵ ریال به ۹۰۶ ریال افزایش یافته است. این تغییر در پی ابلاغ دستورالعمل افزایش هزینه تماس تلفن ثابت با تلفن همراه، تماس میان تلفن‌های همراه و پیامک اعمال می‌شود.
شرکت مخابرات ایران اعلام کرد میزان دقیق تاثیر این افزایش بر درآمد شرکت هنوز مشخص نیست و آثار مالی آن در گزارش‌های دوره‌ای منتشر خواهد شد.
این شرکت در خردادماه نیز هزینه ثابت ماهانه تلفن ثابت را ۴۵ درصد افزایش داده بود. هزینه ثابت ماهانه مشترکان خانگی در تهران و کلان‌شهرها به ۴۳ هزار و ۵۰۰ تومان، در مراکز استان‌ها به ۳۲ هزار و ۶۲۵ تومان و در سایر شهرها به ۲۴ هزار و ۶۵۰ تومان رسیده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/78330" target="_blank">📅 17:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78329">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=A12CKwu-9XgxytECa71l3r1E_U-VP-LqKRJ9EbW3MMM3gvzlIh7T81yQlXEKDqgISY--7YHPjPneS2oLSdvXutf2Y7bDk-SRVCnrdc7HtUo7JS7r494dt54P1724xH_mgzYafrSBAI-khiLjD6KXVic4VtFwDYACTvI3oLe0WO0FPtoOJ-y1olIGOxlWDqD2Da9XnpAU_I7ZGytvVw8dSKH9tJC9ofZdSGwBbn3I_GgZ20EGg_pXmXqk-iDwMaIb-K4jLBJ6b5h9HzK5elyqDtfwod-hhg4V_qevYvL9DnLzWOYFQZSIbLz0y8XwLfSySRQgdZnge45RaINcIjVnVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=A12CKwu-9XgxytECa71l3r1E_U-VP-LqKRJ9EbW3MMM3gvzlIh7T81yQlXEKDqgISY--7YHPjPneS2oLSdvXutf2Y7bDk-SRVCnrdc7HtUo7JS7r494dt54P1724xH_mgzYafrSBAI-khiLjD6KXVic4VtFwDYACTvI3oLe0WO0FPtoOJ-y1olIGOxlWDqD2Da9XnpAU_I7ZGytvVw8dSKH9tJC9ofZdSGwBbn3I_GgZ20EGg_pXmXqk-iDwMaIb-K4jLBJ6b5h9HzK5elyqDtfwod-hhg4V_qevYvL9DnLzWOYFQZSIbLz0y8XwLfSySRQgdZnge45RaINcIjVnVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی زارعی دوز دره سی، زندانی سیاسی و یکی از آسیب دیدگان اعتراضات سراسری ۱۴۰۱ که در زندان قزلحصار کرج محبوس است، توسط شعبه ۲۳ دادگاه انقلاب تهران از بابت اتهام «افساد فی‌الارض» به اعدام محکوم شده است.  بر اساس اطلاعات دریافتی هرانا، حکم اعدام آقای زارعی دوزدره‌سی…</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78329" target="_blank">📅 17:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78328">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/78328" target="_blank">📅 07:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78327">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-fXFNUj37OaiduHUZE6QgmCKZu_FMfml1fi6QT6qD9xwk58COR5mMBZlZjd7Ht5GOZyZxuFLBRSpq1dZ4Ezp360Lw5U_J1G5xsXtVrrOgoGTrdB9iIRwXXd9Pi_vJx8thV2hWK1XjMjAsXxbCoK23eUDuATwvtf5shU32wRVryx3ds7GNHnQxAZclsoC4UlzY3Mn3huefZdwo1W1srknV5rjbtq_UmYBq4RBhQaDi5edSBR4NPXJ9YsJI-i8oycR3h5Ozg9M4m3kHigZ-Jrwu0DQ9xHOLXbRHHvRKQxmFbUm9ndGH215B7m_yrKYCiQt3-ya36_fkM8IBM5AJDqFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا در دومین شب گردهمایی انتخاباتی میان‌دوره‌ای جمهوری‌خواهان که در دالاس در حال برگزاری است، بار دیگر، تنگه هرمز را «تنگه ترامپ» خواند و گفت «ما تنگه ترامپ را کنترل می‌کنیم». رئیس‌جمهوری آمریکا بار دیگر تاکید کرد که هرگز نمی‌توانیم به ایران اجازه دهیم سلاح هسته ای داشته باشد و نخواهد داشت. او گفت که ایران در حال عقب‌نشینی از همه جا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78327" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78326">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MF_t59ddxDCXLv51o4a51mHIwZ1TIghZC373Z33Mz7fCt-AFmG9WVpbde54IlD97yBslmSZb75Q1i2FKk_slxeLiRi2gRJaQZpIFsMRo4_Ahy9qd2d3nJVhnQvsFQzuuPnLlNEKpvXN6yUFD6foZXSiSN1zWCdpXKYRKxdgyx3BG1FPb8M95wRZJPvo9pDqmoJY-u14a3DitdhZX6Q1StEoU7-mrNC4Oy9IEkGXOkGIYkiT1qeMVGzntofQh2A6Z8C3lG2NIB_xQkZssEwzREoPAVVvHLnpRDLgwiyY1S-QkshgKNAKgf4XXn2k6k8ZYSDLKF06MAw6yOnZOM3n2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هانگ کائو، سرپرست وزارت نیروی دریایی آمریکا، به اپک تایمز گفت نیروهای جمهوری اسلامی خسارت گسترده‌ای به پایگاه پشتیبانی نیروی دریایی آمریکا در بحرین، محل استقرار ناوگان پنجم این کشور، وارد کرده‌اند.
کائو در توضیح استقرار اخیر ناو هواپیمابر یواس‌اس آبراهام لینکلن و الزامات لجستیکی عملیات طولانی‌مدت گفت خسارت واردشده به پایگاه بحرین بر امکان پشتیبانی از این ناو تاثیر گذاشته است.
او گفت: «خدمه این ناو جایی برای پهلو گرفتن نداشتند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78326" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78325">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7iFPIYZAWwHX59wLXee524-qLR0GW_jkzuUe-pYtOAzFxtiEP535dxm6XncccR0WZVmoLHi-TJxt_VRgS6vXaKNBsY0fUhRfFOSJd_ubDoade2Vs1ijOl18O0_Ttmpj-Yas8DvC6CA8Yx4hoXjfZrDXlfl-MH3yENzRlRIZcGWjcvaPiGlSrijSm25tOVAg3N52upe1EgTi6D97n4PF115JKEJaAT1zTgbID2gLNhsg_uQDnPbTlFg6cX7RCGNmWRdB7EluEfVN28xSiWN9Z2IjzyRG-5JkY0XIJHdEcF6o-4E7YMFOMngWtw8TYFlPZlAxaHs0fq31MLYCfDd-mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت پنج‌شنبه ۱۹ شهریور هم‌زمان با تشدید درگیری‌ها در منطقه و افزایش نگرانی‌ها درباره اختلال در عرضه انرژی، بیش از شش درصد جهش کرد و نفت برنت به ۱۰۷ دلار و ۶۳ سنت در هر بشکه رسید. نفت خام وست تگزاس اینترمدیت نیز از مرز ۱۰۰ دلار عبور کرد.
بر اساس داده‌های اویل‌پرایس، قیمت نفت موربان با بیش از پنج درصد افزایش به ۱۲۲ دلار و ۴۸ سنت رسید و سبد نفتی اوپک نیز با بیش از چهار درصد افزایش، ۱۱۲ دلار و ۲۵ سنت قیمت‌گذاری شد.
افزایش قیمت‌ها پس از حملات به نفتکش‌ها در خلیج فارس و دریای عمان و پیشروی حوثی‌ها در سواحل دریای سرخ رخ داد. رویترز گزارش داد تصرف بندر مخا و پیشروی حوثی‌ها به سوی جزایر حنیش، نگرانی‌ها درباره امنیت تنگه باب‌المندب و مسیر صادرات نفت عربستان سعودی را افزایش داده است.
هم‌زمان، تردد کشتی‌ها از تنگه هرمز به‌شدت کاهش یافته و داده‌های اولیه نشان می‌دهد ۱۸ شهریور تنها هفت کشتی از این آبراه عبور کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78325" target="_blank">📅 03:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78324">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=dir4eqCbcOvH0jjnCPrhg4qUOVQsa4OH0uNqeQJf9PTgBLAcu_4Lm_SzE73Gkp3zipqBbrdmA3H1hlrovpYeNe4KP3XnkNfZ5aPYvddiM6abCPiz793XBhr2PMIs4b5Cd3E_RhnIgczcxSWFGyuE-1vyYIu5Vm1xcibsXjr50mCs-g43fNWXwiKJGEnOVrCdaeasVH_t3ir1nn4Wb_fNxH9dq7lhTCiV3johiRwDFmRDmrI4Fejv14QkqDj1NaS0SfyeZHuCJnko0U2tiVmOWdCC4mtvtcUMFPV5zowWkrlgJ7mxGnym6zxt0xOqTZgvwwUh93Rp26cFh0P1FjVKDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=dir4eqCbcOvH0jjnCPrhg4qUOVQsa4OH0uNqeQJf9PTgBLAcu_4Lm_SzE73Gkp3zipqBbrdmA3H1hlrovpYeNe4KP3XnkNfZ5aPYvddiM6abCPiz793XBhr2PMIs4b5Cd3E_RhnIgczcxSWFGyuE-1vyYIu5Vm1xcibsXjr50mCs-g43fNWXwiKJGEnOVrCdaeasVH_t3ir1nn4Wb_fNxH9dq7lhTCiV3johiRwDFmRDmrI4Fejv14QkqDj1NaS0SfyeZHuCJnko0U2tiVmOWdCC4mtvtcUMFPV5zowWkrlgJ7mxGnym6zxt0xOqTZgvwwUh93Rp26cFh0P1FjVKDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتشار ویدیویی در شبکه اجتماعی ایکس نوشت
:
امشب بزرگ‌ترین پایگاه ایران در خارج از ایران، یعنی تونل‌های علی‌الطاهر در لبنان را نابود کردیم. در حال تکمیل مأموریت هستیم. سال نو مبارک!
پیش‌تر ارتش اسرائیل اعلام کرد شبکه تونلی حزب‌الله در ارتفاعات علی‌الطاهر را با استفاده از بیش از هزار و ۱۰۰ تن مواد منفجره تخریب کرده است.
به گفته ارتش، در این تونل‌ها که طول آن‌ها بیش از دو کیلومتر اعلام شده، ده‌ها موشک، راکت، پهپاد، سلاح‌های سبک، موشک‌های ضدزره، صدها مین و مقادیر زیادی مواد منفجره کشف شده است.
بر اساس اعلام ارتش اسرائیل، با انهدام این سایت، عملیات تخریب شبکه‌ای متشکل از هشت تونل به طول مجموع ۵٫۴ کیلومتر در منطقه علی‌الطاهر و قلعه شقیف تکمیل شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78324" target="_blank">📅 01:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78323">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tbweF43UUvJvOGJamUA75AGCgYofT-ejUQxJynjR-J1VNe_Ehqk1v3JK6FyxFaHF-zVsFgadSi7wjBcnLZGE5W908mFYx7szfO1nujz1rpra8_fALMo2N-Igy3h0O3UTnJXZcaNTga0f3nS_J9KYcbv4558-glaImjQVtS8xkMnAyb8D2BPRzTD6CgP-T4C0Ah0Eug8p5EGK1iehqFPQyQUvz4mgt6SOvUS_5vvxXbI35kFZXyqwVCUFtMoEMMxvKF3oLDre0ipFtgiN02bfdnhRsLKtiLeYy_1qZ5V2hULaWvZT6DiAo2xULG5MJeMjj9cAnD_vKbuHCiOa-dP9Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا، یوکی‌ام‌تی‌او، عصر پنج‌شنبه به وقت واشنگتن از برخورد چند «پرتابه» به دو شناور در نزدیکی سواحل عمان خبر داد.
بر اساس این گزارش، این برخوردها در فاصله چهار مایل دریایی غرب شهر خصب، در استان مسندم عمان، روی داده است.
طبق این گزارش، کاپیتان یک شناور اعلام کرد که شاهد آن بود که چهار پرتابه نامشخص به دو شناور نامشخص اصابت کردند.
در پی این اصابت‌ها، یکی از شناورها دچار آتش‌سوزی شد و از وضعیت شناور دوم اطلاعی در دست نیست.
مقامات عمانی در حال بررسی این واقعه هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78323" target="_blank">📅 01:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78322">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=K3h_ZdieMR4Qn21UM0lFl9iaQSCFai6IhjBzTwgWbz89-5qlvch8EQDtV2RNf0C-UKDGIzqkYfE19jUR6dkNHaRIMLh-sWafzY_UBaNztvxQ9SF4z5Vd2LufZrs1Vty68sXnSYh1m-Ca2eDonbOtfDsPVf6ZK_Hv_AMd5IQjxhOxFpMgt5gvvUXZLz6KmFLaKNpHtWxS7IaidzC3aVXDoSFUBB-yiItUe8OzQnQV3rnXLaPEn2oAQN-E2ABBdiM7D2ZrW-Zknuu2QVoGDw1Q4_mlCZvsiAxwryoO5psBMK2ANsATDx9IOhiuNe3KMjrOaLTYKQiFG2eTNPwaAkj58Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=K3h_ZdieMR4Qn21UM0lFl9iaQSCFai6IhjBzTwgWbz89-5qlvch8EQDtV2RNf0C-UKDGIzqkYfE19jUR6dkNHaRIMLh-sWafzY_UBaNztvxQ9SF4z5Vd2LufZrs1Vty68sXnSYh1m-Ca2eDonbOtfDsPVf6ZK_Hv_AMd5IQjxhOxFpMgt5gvvUXZLz6KmFLaKNpHtWxS7IaidzC3aVXDoSFUBB-yiItUe8OzQnQV3rnXLaPEn2oAQN-E2ABBdiM7D2ZrW-Zknuu2QVoGDw1Q4_mlCZvsiAxwryoO5psBMK2ANsATDx9IOhiuNe3KMjrOaLTYKQiFG2eTNPwaAkj58Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران روز پنجشنبه ۱۹ شهریورماه تصاویری منتشر کرد که به گفته این نیرو، هدف قرار دادن یک شناور بدون‌سرنشین آمریکایی در ورودی تنگه هرمز را نشان می‌دهد. سپاه اعلام کرد این شناور با شماره بدنه ۵۸۳۸ و از نوع «سیل‌درون» بوده است.
علی عظمایی، فرمانده نیروی دریایی سپاه پاسداران، گفت این شناور بدون‌سرنشین «جاسوسی» متعلق به ارتش آمریکا در تنگه هرمز مورد اصابت قرار گرفته است. او همچنین گفت: «تنگه هرمز مسدود و تحت اشراف اطلاعاتی و کنترل هوشمند ماست و هرگونه تحرک خصمانه مورد هدف قرار می‌گیرد.»
نیروی دریایی سپاه در بیانیه‌ای اعلام کرد ارتش آمریکا طی روزهای گذشته شناورهای بدون‌سرنشین خود را به تنگه هرمز اعزام کرده است. مقام‌های آمریکایی تاکنون درباره این گزارش اظهارنظری نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78322" target="_blank">📅 22:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78321">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nj7gEPN8F0g-URriX2yp5mfvFy1nRpC3LhHjSuhR5bP-BErV8gaf5EwCd7IExGXdL69gao_zlu6npaYuIUwzyj6CIJ2PFd1JGzaWTgw5_0Ob2UIjONvXDPOg83uTxsqNmRWMqQBAPkBwLoMLUQJNe17-xnsDRvyGzwCYdrsQ7AvmhGN8MzwraZcphrjlD3VFMS9AZhgtmSNIw1Qy5afu39Ltp6d51h5ispky4PFH6nyzsuMSc8RnciNhBPwTVxKFXuz-DcBfJHMJFvCcRrhKnpYwhmfWYhb9nFM_CX4trsa1IFdLXCUT_ocZvSgc3WTeAgDfdfUlfcy8uCfpq9wR3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، روز پنجشنبه ۱۹ شهریور در گفتگو با بلومبرگ اعلام کرد این سازمان بر اساس تصاویر ماهواره‌ای، شاهد تحرکات ساخت‌وساز در سایت بسیار مستحکم «کوه کلنگ‌گزلا» (Pickaxe Mountain) در جنوب مجتمع اصلی غنی‌سازی ایران بوده است.
گروسی با اشاره به اینکه بازرسان آژانس هنوز موفق به بازرسی از داخل این تونل‌های عمیق نشده‌اند، گفت: «نشانه زنده از تحرکات در اطراف این سایت ساخت‌وساز وجود دارد، اما اطلاعات دقیقی از فعالیت‌های درون آن در دست نیست.» او یادآور شد که ایران پیش‌تر قصد خود را برای انتقال تجهیزات به زیر کوه جهت «مصون‌سازی در برابر حملات» اعلام کرده بود.
این اظهارات در پی ارجاع پرونده هسته‌ای ایران به شورای امنیت سازمان ملل مطرح می‌شود. بر اساس گزارش‌ها، آژانس از ژوئن ۲۰۲۵ و پس از حملات نظامی آمریکا و اسرائیل به تاسیسات هسته‌ای ایران، امکان راستی‌آزمایی وضعیت ذخایر اورانیوم با غنای بالا را نداشته است.
دونالد ترامپ، رئیس‌جمهوری آمریکا، بار دیگر با اشاره به این سایت زیرزمینی، نسبت به هرگونه اقدام ایران هشدار داد و در یک تجمع انتخاباتی گفت: «ما متوجه فعالیت‌های مختصری در کوه کلنگ شده‌ایم. به ایران توصیه می‌کنم دست از پا خطا نکند، چرا که مجبور خواهیم شد ضربه بسیار سختی به آن‌ها وارد کنیم.»
از سوی دیگر، سی‌ان‌ان روز گذشته به نقل از منابع خود گزارش داد که ایالات متحده در حال توسعه سلاحی با نفوذ بیشتر با قابلیت تخریب اهدافی در زمین‌های سخت مانند کوه کلنگ‌گزلا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/78321" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78320">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUUn85QuIKs28OpabSe6pWfPommqq2gjd23C89WJifJWKdc138lia_9T_v3cGqyUJT0oFd1ZrSMAJAuhe0byOmV0_onehI1R_r4_LbM2IsBsjTO0J02MRf5HABDf1HmOhzyXhmzT7jxK7ak2ViIxoseX8TL8VAK5HkCtdUIFwluPjYhlErw9a-LSTD9pQljX7KUcncVKIRQuJFbejggBtYTXCJDiSnBTKKEU5Stl-FZJtQC5JQSImNjs2k3I0MS7xY6L2PSNDWWdEDWet0J19qnAc55cxP0d3etwqdTK-jykzSSmVstPLJ0ACS2a0VHM2aU-rOfgTFTX5pc_tydEPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه قبل ماموران امنیتی به منزل خانواده «کیاوش میرقاسمی» از کشته‌شدگان اعتراضات دی‌ماه۱۴۰۴ یورش برده و «سمانه عصاران» مادر او را بازداشت کردند.
به‌‌دنبال تشدید فشارها بر خانواده میرقاسمی حالا صفحه اینستاگرامی مادر او از دسترس خارج و کنترل آن به اجبار به دست نهادهای امنیتی افتاده است.
تمامی پست‌های پیشین این صفحه حذف شده و تنها یک پست به دستور مقامات قضایی در این صفحه قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78320" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78319">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toMUgLoyvq3tBVS7WLFGW61_UR27Q1n9k63Yiw7-wQ6Pv9e4jS8kro3nTah-K2tuZEBL6z3_5uysATMDfRT5ZlkOW7K6LTdY-llL08F3HnRjZnhPCp5DfdHjY-j_56Z9GD3Ce-9wugNtXammEIHjDl1YXYy83jvt_P2UEoPR75C2wEejGQuTdLQYSmByDW9-8mwDYR7D9SgcubaQpdYO_25v_3il0_uwieF2j6-C9c3bE5c-5Ax2SiY9NWCbAI7ZrV7jMI6pBDkLCfPy71MYAcz7Jl6lEHjdHylBnVbD9psqFeaKGqUAEZPLIlPS4Q_Zl-Qo-QsC0JqGBPdiZZrXRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس بریتانیا دو نفر را به ظن ارتکاب جرائم مرتبط با ایران و نقض قانون امنیت ملی بریتانیا بازداشت کرد.
این دو فرد در لندن پایتخت بریتانیا و در جریان تحقیقات مربوط به فعالیت‌های مرتبط با ایران بازداشت شده‌اند.
پلیس متروپولیتن لندن با صدور بیانیه‌ای تأکید کرد که این تحقیقات، با هیچ‌یک از حوادث ماه‌های اخیر که در اماکن و ساختمان‌های مربوط به یهودیان و جامعۀ ایرانیان مقیم بریتانیا رخ داده بود، ارتباطی ندارد.
هنوز جزئیات بیشتری از هویت افراد بازداشتی یا ماهیت اتهام‌های منسوب به آنها منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78319" target="_blank">📅 18:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78317">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MATtVoWRvqdOGuDDqQCYGvW4MZoGAIHMEaDdaSF5UlRekZh6aO8Baz8afbB0frgwRDGBMy73B-h6pOBg9CQU6l8s_8Hj7US1VFQGrpK3iS9H-edpqpgQY7zl_0FSBZ7x0q0kv6RaUjTkpiI0kdeqvsOZ3v3A1BozDJeyj8b7hZ-_1PaFnAylX7M5fPEeyEuQF9vmJUHL9RlPBFvg26t3VMj5MMEvHcC4V0u3mf5pWDYbNMr47LJY-jlpMDMA2kM3VDSBAZ9PPsBQugT32miuNg-HMGB3Nid2lpdaF1dNJfSnhcmNYilbe-rrIb3qFgGNikpmZdzjM97tps1eyzv9sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a8adZQlgxx0hDEYcdhzi9sJdFTVNV4iSXlxM2nPEKPZsBt-BP8115SEi5nxOD6_GHm8FzzkElsneTDzjCswL_ue_WhwtUEe045d8dftAZQ8vDWm1pSLuzgJfX1HYyPDuwJNY8dyx2d0KDDF0SGdWG_FXVTSievQ3O5mN-FuWdHSSjNadb-sxC3xZGkF7ua9hDDQMpcSiGT8IPDGXV-4uOBhrrnZgypBbZs9CxbgdK83t5UCv16-u9oj7u1R6gF7K3-OeEBhlq334kXpZ0DiGJsyCeakF3ySUlycLABMvuIHh3Bgwu5StDszWS6KGuhgm2It9Bz8ru5xjLxHoc1laQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اکانتش در توییتر:
MaryamAzimih
مریم عظیمی، مهندس ایرانی اپل، که پیش‌تر از بازداشت و انتقال خود با چشم‌بند در خودروی نیروهای اطلاعاتی جمهوری اسلامی در مشهد و تصور مرگ قریب‌الوقوع نوشته بود، در مراسم جهانی رونمایی اپل، یکی از فناوری‌های جدید دوربین آیفون ۱۸ پرو و پرومکس را معرفی کرد.
عظیمی در ویدیوی از پیش ضبط‌شده اپل به‌عنوان مهندس کیفیت تصویر معرفی شد.
او در بخش مربوط به دوربین آیفون ۱۸ پرو، قابلیتی به نام «تصویر مرجع اپل» را ارائه کرد.
اپل دوربین این مدل را پیشرفته‌ترین دوربین خود تا امروز توصیف کرده است.
حضور عظیمی از دو جهت در میان ایرانیان مورد توجه قرار گرفت: نقش او در توسعه فناوری تصویربرداری در یکی از بزرگ‌ترین شرکت‌های جهان و مخالفت علنی‌اش با جمهوری اسلامی، از جمله روایت شخصی او از دوران بازداشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78317" target="_blank">📅 17:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78315">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZyDq0Ne4AWNKo6Q5799pHkoIt045a3fQ0JVg9qMZMfP1ujDUBjPsuvf__co7qiPpqWhAS4ndhCH42ES9aDPxiMorA8nmCMFB0-49o-KNisttsT21Y4-EZndDVJEUqSuTXUroF7o1-idfq_UphC3mN7wTlMqqNmLGiIcq4XT7HSvYuDR6tRpOtYkMlJxSRJJUOucl3_oU-mQHm4zy0ebKyuoG2EW96rxM59Yc6pUqg7rQHMHsiHmTNDzA9ZdQmANLB-wyEiMKKh9CPL2YNK_sHNY0RuK0wQhYxFjhPczAmY6XOY0eefpgAztqbcTjw1fc34X6xUkR0-SnoSNGCV25yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hOmeI76W7bMC2teFza7f_yw7FhFL8Rk-t2uoFzxwtFVR68YyvgU3OCSWnWHn7hnm2arScScx6BveE0lB2HEoW7jpEPFPq2h3mbIhHJMsqRizSBf6qi39I-KqK_0SxXRDz_kfBa6a8zqvsbY8Bpo8k8cVeV3MjMq-MgQw7qB4C9qJmNNcwfpKdmxJXFIPoVvqKoAf8yQ4JB8FWW4MqdNZwdzi0msGvInFAGoMdG33QFv7BDvUC05YGQVS7QZ0bxOnYu8TJQE0qyV_YBydt_dgba6Lfh8fvlFv7HVafUzFTCQiUFjtzo8DrzI5ebx5RhDG-J7scuRrOOqSY1jMjr9p7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78315" target="_blank">📅 16:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78314">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lx24J27Sn1K20vJouFzYH4O5tTqhK9eZXBIGQ0tozwUYyjOY1NUElZtGabwiJeLzbqX9lEVRJ4uY1M1qpxRATL69KpXufQL2Wq8T_F9GQgh8D89wG-2W57UF9IFWHah8QZOTzMqkSQDu1p-d1wFRGrfbMybKGx8KuduVCjtpuxG0TYlSII6ZshOSu2AOvdGfPBcsbBWDyAzyi2c_8Mr9HbNdMfBtpL3Df1141Ic_ZciGhme-kOdO6nYnVJFpLuQGm7Q61HbvkUjIgIFcUz7mfFtXJts8GZkaK3-ySrMbBD0Kbs3Ij7kvJIqQoijWqVy2oLIooHcdr3AhI3fc-kzhwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند افزایش روزانه قیمت ارز در بازار تهران روز پنجشنبه ۱۹ شهریور (۱۰ سپتامبر) ادامه یافت و بهای دلار به ۲۳۵ هزار و ۷۰۰ تومان رسید.
dw_persian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78314" target="_blank">📅 16:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78313">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcPldkt7JI5k5K_k6Wrsm4E01zZDaBvpcjGIFPaV2brp-3Z7VN05zJN-Djxk6xNO_v55r_qOIGYYM0PXUigZ-yZilU8CiqWHj52UZMCSoMef34OYL-0HpQQcRpo3x4ZhQ7V3iHonVWzyJ0tQJ-p4CiSgWwdQIn2fnvdf_pGc-bHvm0HdwUuJnIYLBndAtow3NVT0Zk94yIyoCjtgo3os6P6Jn_xywMPHFxJxJafJNUFec-RPtAE3jpCy2QS3NIdKNeEZHr0CFPWBHryt0UlKymwzZ7DHdyiZbv7Um8GY37IwH0Ow8bokVr1SbrjX00v-njfcWXDThfGgjA_FSCdDvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی افزایش تنش‌ها در خاورمیانه، قیمت نفت شاخص برنت روز پنج‌شنبه از ۱۰۲ دلار عبور کرد که نسبت به روز گذشته حدود یک درصد و نسبت به ابتدای ماه حدود ۸ درصد رشد نشان می‌دهد.
طبق برآورد اداره اطلاعات انرژی آمریکا، ماه گذشته تولید روزانه نفت ایران به خاطر اعمال مجدد محاصره دریایی آمریکا ۸۰۰ هزار بشکه نسبت به ماه ژوئیه افت کرده، اما هم‌زمان تشدید حملات جمهوری اسلامی به کشتی‌ها در تنگه هرمز و آغاز حملات حوثی‌ها در دریای سرخ و باب‌المندب به نفتکش‌های عربستان نیز باعث شده متوسط تولید روزانه نفت کشورهای عرب منطقه در ماه گذشته ۹۴۰ هزار بشکه نسبت به ماه ژوئیه کاهش یابد.
مجموع تولید نفت ایران و کشورهای عرب منطقه در ماه گذشته ۶.۷ میلیون بشکه کمتر از دوران پیش از جنگ خاورمیانه بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78313" target="_blank">📅 16:19 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
