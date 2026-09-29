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
<img src="https://cdn4.telesco.pe/file/sUayCqhsaXomu0GcDXiCvYhm0eNJ1Jv7ooLf8njMzmT-TWDuK7ExgC05MgTTEU1OUv6z_9xaccLEUPIgBPmAz-3zeqpAbw2EdY6h09BVSfjc6TxvfSnlo7odI-1_Htd5RDT2JLhVDYO9MnrDwjw72Yi8HJzHNMpnvCzqkaipBRSRcj8t2uTjRoHqIV7IS2-VxquqkQackEk-f5O6Kep2-xWrY9AEQ9qVfcU7jqjlWWEoI3fDxDOV-GIgewiDj52LARFw_9UufdE4mCDqmALiUH26fofa7qmovjE-jnvYauecmmQyX6dZrk9BvYL3hF5ORoG5zSygfJirbvN76-siag.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 477K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 12:18:18</div>
<hr>

<div class="tg-post" id="msg-24479">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اعلام کرد
عزالدین البیک، فرمانده تیپ شمال غزه در گردان‌های عزالدین قسام، در حمله اسرائیل کشته شده است.
البیک از فرماندهان ارشد نظامی حماس در شمال غزه بوده است
@WarRoom</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/withyashar/24479" target="_blank">📅 11:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24478">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نرخ دلار ۲۵۰،۱۰۰ تومان (رکورد تاریخی)
تتر  ۲۴۹،۶۰۰ تومان(رکورد تاریخی)
بیتکوین ۸۴،۰۵۶ $
انس جهانی طلا ۴،۱۴۰ $
نفت برنت ۹۸،۶۹$
@WarRoom
۱۱:۳۰ ظهر تهران</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/withyashar/24478" target="_blank">📅 11:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24477">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عراق: پرواز نجف به ایران برای یک ماه برقرار می‌شود
اما تنها شرکت هواپیمایی العراقیه، مجاز به انجام پرواز میان دو کشور است
@WarRoom</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/24477" target="_blank">📅 10:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24476">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ممباقر
: هم آمریکایی‌ها و هم سایر کشورها بدانند در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت
خطاب به ترامپ: «بچرخ تا بچرخیم
!»
@WarRoom</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/24476" target="_blank">📅 10:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24475">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اتاق جنگ با یاشار : چند فروند جنگنده اف-۲۲ رپتور طی ۳۰ دقیقه گذشته از پایگاه نیروی هوایی لنگلی به پرواز درآمده‌اند.علاوه بر این، سه فروند هواپیمای سوخت‌رسان KC-46A نیروی هوایی آمریکا با نام عملیاتی CORONET نیز به پرواز درآمده‌اند که احتمالاً در حال پشتیبانی…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/24475" target="_blank">📅 10:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24474">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فاکس‌نیوز: اسرائیل برای ازسرگیری حملات به ایران آماده است.
فاکس‌نیوز گزارش داد
اسرائیل کاتز، وزیر دفاع اسرائیل، هشدار داده است که عملیات نظامی علیه ایران ممکن است دوباره آغاز شود
و ارتش اسرائیل برای اجرای عملیات مستقل علیه ایران آمادگی دارد. کاتز پیش‌تر نیز گفته بود ارتش اهدافی را برای حمله احتمالی به ایران مشخص کرده و در حالت آماده‌باش قرار دارد. با این حال، گزارش فاکس‌نیوز به دیدگاه‌هایی در اسرائیل نیز اشاره می‌کند که از ادامه فشار و محاصره بدون بازگشت فوری به جنگ حمایت می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/24474" target="_blank">📅 09:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24473">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رویترز:
پرونده امنیتی
RAF Fairford
وارد مرحله جدیدی شده است؛ پلیس ضدتروریسم انگلیس اعلام کرده پنج مظنون، همگی شهروند بریتانیا و ساکن لندن، پس از بازداشت به قید وثیقه آزاد شده‌اند و تحقیقات درباره احتمال دخالت ایران ادامه دارد و پلیس احتمال ارتباط‌های دیگر را نیز بررسی می‌کند.سفارت ایران در لندن هرگونه ارتباط با این حادثه را رد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/24473" target="_blank">📅 09:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24472">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وال‌استریت ژورنال:
صادرات نفت خاورمیانه به‌طور محسوسی افزایش یافته و صادرات عربستان، امارات و عراق به حدود
۱۳ میلیون بشکه در روز
رسیده است؛ بخش قابل‌توجهی از جریان نفت از مسیرهای جایگزین یا با استفاده از تدابیر جدید دریایی عبور می‌کند. در مقابل، صادرات نفت ایران تحت فشار محاصره دریایی آمریکا کاهش شدیدی داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/24472" target="_blank">📅 09:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24471">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c37bfc6165.mp4?token=dn1T95CvE--4cdpjm59xhpilJeQNZ786kr4Evl1KpDR5PhNalPO_d14xr5K3a4zp5YOjs_SYTXdE1ozEvI_9cL2m5YaYxBf4UId4_blL-XnYgCS_Y_sVG5ojynQjNF3Uql1IewTPHAMdDleCP8CY1ymNF161ZNGqMTm3hQ_u9NjLIhalGc9g1oqA0dqI0tlinpvsQWZusJY0DNyJWwPaCjbJeJAkFpThFgUnEJkkX2vjEJy0sn8bJOwBh7szcXIoNGdCrT_N-B_jw0ncFVOTAEMt_lUAOdFfppoXf0j1PiRTsyMjzr7XEOXlWocHc1qTF_18bJylXXT8Xp88U4s-2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c37bfc6165.mp4?token=dn1T95CvE--4cdpjm59xhpilJeQNZ786kr4Evl1KpDR5PhNalPO_d14xr5K3a4zp5YOjs_SYTXdE1ozEvI_9cL2m5YaYxBf4UId4_blL-XnYgCS_Y_sVG5ojynQjNF3Uql1IewTPHAMdDleCP8CY1ymNF161ZNGqMTm3hQ_u9NjLIhalGc9g1oqA0dqI0tlinpvsQWZusJY0DNyJWwPaCjbJeJAkFpThFgUnEJkkX2vjEJy0sn8bJOwBh7szcXIoNGdCrT_N-B_jw0ncFVOTAEMt_lUAOdFfppoXf0j1PiRTsyMjzr7XEOXlWocHc1qTF_18bJylXXT8Xp88U4s-2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی آمریکا (سنتکام): ویدئویی از برخاست جنگنده‌های
F/A-18E/F سوپر هورنت و F-35C لایتنینگ ۲
نیروی دریایی آمریکا از ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» منتشر کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/24471" target="_blank">📅 09:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24470">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وار زون : یک فروند جاسوسی SR-71 Blackbird با شماره NASA 844، آخرین SR-71 پروازکننده در تاریخ، از محل نمایش عمومی خود در مرکز تحقیقات پرواز آرمسترانگ ناسا در پایگاه ادواردز ناپدید شده و اوایل امسال به یک آشیانه دیگر منتقل شده است. این اتفاق پس از انتشار تصویری…</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/24470" target="_blank">📅 08:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24469">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نیروی دریایی آمریکا : یک فروند هواپیما هنگام فرود روی ناو هواپیمابر «یو‌اس‌اس دوایت آیزنهاور» در نزدیکی نورفک ویرجینیا،آمریکا محل استقرار ناو در ساعت ۱۸:۱۸ روز ۲۸ سپتامبر (به وقت شرق آمریکا)
دچار سانحه
شد. دو خلبان با خروج اضطراری نجات یافتند. در این حادثه چهار ملوان نیز زخمی شدند که یکی از آن‌ها با جراحات غیرتهدیدکننده حیات به بیمارستان منتقل شد.
@WarRoom</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/24469" target="_blank">📅 08:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24468">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خبرنگار فاکس‌نیوز:
اگر ایران به سلاح هسته‌ای دست پیدا کند، تنگه هرمز و خاورمیانه چه وضعیتی پیدا خواهند کرد؟
مارکو روبیو:
ایران تلاش می‌کرد با انباشت
پهپاد، راکت و موشک
به نقطه‌ای برسد که دیگر نتوان برنامه هسته‌ای آن را از نظر نظامی متوقف کرد و سپس پشت این «سپر تسلیحات متعارف» به سمت سلاح هسته‌ای برود. ترامپ مانع رسیدن ایران به این نقطه شد؛ وضعیتی که می‌توانست
«کره شمالی در خاورمیانه»
ایجاد کند. اگر ایران سلاح هسته‌ای داشت، می‌توانست
تنگه هرمز را کنترل کرده و بر جریان انرژی جهان اثر بگذارد.
او همچنین حکومت ایران را مسئول کشتار
ده‌ها و شاید صدها هزار نفر از مردم خود
دانست و گفت داشتن سلاح هسته‌ای می‌تواند تهدیدی برای آمریکایی‌ها، اسرائیلی‌ها و دیگر کشورهای منطقه نیز باشد. روبیو تأکید کرد مشکل،
مردم ایران نیستند، بلکه «رژیم» حاکم بر کشور است
و تصمیم‌گیران اصلی را
روحانیون شیعه تندرو با دیدگاهی آخرالزمانی
توصیف کرد و تاکیید کرد تصمیم‌گیران اصلی،
آن مقام‌هایی نیستند که با کت‌وشلوار در برنامه‌هایی مانند Meet the Press حاضر می‌شوند، بلکه روحانیون شیعه رادیکال هستند.
ترامپ کاری را انجام داد که رؤسای‌جمهور پیشین آمریکا درباره آن صحبت کرده بودند اما انجام نداده بودند:
جلوگیری از دستیابی ایران به سلاح هسته‌ای.
@WarRoom</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/24468" target="_blank">📅 08:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24467">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مارکو روبیو: ایران اکنون به‌سرعت به سمت یک
فاجعه اقتصادی
پیش می‌رود؛ موضوعی غم‌انگیز، زیرا ایران کشوری با ظرفیت‌های عظیم و مردمی
باهوش، سختکوش و پرتلاش
است که از
تاریخی کهن و دستاوردهای فراوان
برخوردارند. ایران پیش از روی کار آمدن روحانیون افراطی، یکی از مرفه‌ترین کشورهای خاورمیانه بود. مسئله فقط تحمیل فشار اقتصادی بر حکومت ایران نیست؛ این حکومت طی ۳۰ سال گذشته هر زمان به درآمدی، از جمله از محل فروش نفت و گاز یا کاهش تحریم‌ها در دوره اوباما، دست یافته، آن را برای ساخت بیمارستان، جاده یا بهبود زندگی مردم هزینه نکرده است. ایران این منابع را برای
ساخت سلاح، صدور انقلاب و تأمین مالی حزب‌الله، حماس و شبه‌نظامیان شیعه در عراق
و همچنین حمایت از تروریسم و طرح‌های ترور در سراسر جهان به کار گرفته است. محدود کردن درآمد نفتی و اعمال تحریم‌ها فقط مجازات حکومت ایران نیست، بلکه مانع دسترسی آن به منابعی می‌شود که می‌تواند برای
کشتن آمریکایی‌ها و دیگران، کشتن مردم خود، ساخت سلاح، تهدید جهان و در نهایت پیشبرد برنامه تسلیحات هسته‌ای
مورد استفاده قرار گیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/24467" target="_blank">📅 08:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24466">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مارکو روبیو در مصاحبه با فاکس ترکوند ، غوغا کرده
🔥</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/24466" target="_blank">📅 08:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24465">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبرگزاری آسوشیتدپرس: ممنوعیت واردات کالاهای کانادایی به ارزش یک میلیارد دلار از سوی آمریکا اجرایی شد.
@WarRoom</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/24465" target="_blank">📅 08:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24464">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تتر ۲۴۹،۰۰۰ (رکورد تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/24464" target="_blank">📅 08:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24463">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تتر: حدود ۵۵۰ میلیون دلار USDT مرتبط با ایران را مسدود کردیم.
شرکت تتر امروز اعلام کرد در سال ۲۰۲۶ و در همکاری با مقام‌های آمریکایی، حدود
۵۵۰ میلیون دلار از دارایی‌های USDT مرتبط با بانک مرکزی ایران و شبکه‌های دور زدن تحریم‌ها
در کیف پول‌های مختلف مسدود شده است. تتر همچنین اعلام کرد با بیش از ۳۴۰ نهاد انتظامی در ۶۷ کشور همکاری دارد و تاکنون از بیش از
۲۹۰۰ تحقیقات و پرونده در سراسر جهان
پشتیبانی کرده که بیش از
۱۶۰۰ مورد آن مربوط به نهادهای آمریکایی
بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24463" target="_blank">📅 02:24 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24462">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">روبیو: من با وزیر امور خارجه عربستان سعودی درباره امنیت و ثبات منطقه‌ای، از جمله موضوعات مربوط به ایران، غزه، سودان و یمن، گفتگو کردم.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24462" target="_blank">📅 02:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24461">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وزارت خزانه آمریکا : بسند در‌ دیداری از دولت لبنان خواست تا اقداماتی را برای مختل کردن شبکه‌های مالی مرتبط با ایران و حزب‌الله انجام دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24461" target="_blank">📅 02:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24460">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6ac7d7f6.mp4?token=BM-ZAcX7Uv-oy_tU71vGO_qNGMCcLQNFzX9njUogequNClu-VYVDT4jk16IESjjB76bK1JbZ5QThdopbeSC8w-dg8CsCCcWHwvWUlu6P_8MIpbIl3rBlADVoBcqumBOaBtWvCUxB3v8xU2EbhGp6ezvb9ZVaWhKXZfIdVCWnEDwOiL0WjTAbXMgpRlVaLUxZ_4rStn8dNsA5w11avtHPYxA_VbJ3n_zOPXH1z5KAk2-oCJtiFAHCFHYh5xjw1T7BEqjhh7AMQFrJUK5i8a2AiZej9pdJTUtO3WMyTGGQ3IPO2F5AcOnQSVJAkTjjyMhBnW69GbkyWl92ztM9M-SvG2ZE2dMBHXSp_CXcDx5EbCFrE6e5ETmeOM3pw7H_-4sQisPHfqMR6fHKNEvobkKjzco07-K7R5jviJ8cit7pLw6A-5qAbIUk64tui_XAwrWpnB8OWsKvDVt-CCMT4L3yxsZvNQcpbTs6e1emG2RYdSOKMlm5OBBT_FT-IFL4PJ1sv-fdCZdqQXxEeUjaig6upMIm6gCkv9wmU47nDGgCqnNJ2fnho2U8zECEyhtX7uO42qujBW4w49vcCLH2PYtR9hniOtNA7bUm_Pdh-7pwT49aq7pG2Yrx9DUwAkwQ5Cm399XXQ_OddV18IrISe6BpGpQq87VEQAckZD1TyOaKnMo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6ac7d7f6.mp4?token=BM-ZAcX7Uv-oy_tU71vGO_qNGMCcLQNFzX9njUogequNClu-VYVDT4jk16IESjjB76bK1JbZ5QThdopbeSC8w-dg8CsCCcWHwvWUlu6P_8MIpbIl3rBlADVoBcqumBOaBtWvCUxB3v8xU2EbhGp6ezvb9ZVaWhKXZfIdVCWnEDwOiL0WjTAbXMgpRlVaLUxZ_4rStn8dNsA5w11avtHPYxA_VbJ3n_zOPXH1z5KAk2-oCJtiFAHCFHYh5xjw1T7BEqjhh7AMQFrJUK5i8a2AiZej9pdJTUtO3WMyTGGQ3IPO2F5AcOnQSVJAkTjjyMhBnW69GbkyWl92ztM9M-SvG2ZE2dMBHXSp_CXcDx5EbCFrE6e5ETmeOM3pw7H_-4sQisPHfqMR6fHKNEvobkKjzco07-K7R5jviJ8cit7pLw6A-5qAbIUk64tui_XAwrWpnB8OWsKvDVt-CCMT4L3yxsZvNQcpbTs6e1emG2RYdSOKMlm5OBBT_FT-IFL4PJ1sv-fdCZdqQXxEeUjaig6upMIm6gCkv9wmU47nDGgCqnNJ2fnho2U8zECEyhtX7uO42qujBW4w49vcCLH2PYtR9hniOtNA7bUm_Pdh-7pwT49aq7pG2Yrx9DUwAkwQ5Cm399XXQ_OddV18IrISe6BpGpQq87VEQAckZD1TyOaKnMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بن سبطی (یگال سبطی) پژوهشگر، روزنامه‌نگار و سخنگوی سابق فارسی‌زبان دولت اسرائیل: مجتبی خامنه‌ای زنده‌ست ولی هرچیزی میگه برعکسش انجام میشه ، اسرائیل منتظر درگیری بین رهبران رژیم مانند آخرای شوروی یا قیام مردمه.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24460" target="_blank">📅 02:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24459">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">عراقچی: من پس از چند ساعت به تهران باز خواهم گشت و امیدواریم که سه شنبه پاسخ نهایی را از طرف آمریکایی‌ها دریافت کنیم.
هیچ تغییری در مواضع ما در رابطه با برنامه هسته‌ای ایجاد نشده است و شرایط ما برای بازگشایی تنگه هرمز کاملاً مشخص است.باید حرف رهبر اجرا شود
ما همیشه برای جنگ آماده هستیم و همچنین چیزهایی برای گفتن در عرصه دیپلماسی داریم. موضوع فعلی که مطرح است، صرفاً تنگه هرمز است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24459" target="_blank">📅 01:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24458">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">عراقچی داره برمیگرده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/24458" target="_blank">📅 01:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24457">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/24457" target="_blank">📅 01:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24456">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دلار ۲۴۵،۰۰۰ تومان ( رکورد تاریخی ) تتر ۲۴۵،۰۰۰ تومان ( رکورد تاریخی ) دلار کف بازار ۲۵۵،۰۰۰ تومان ( رکورد تاریخی ) @WarRoom
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24456" target="_blank">📅 01:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24455">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyij6qEHRTx5HOhXhYSPLtMlAx-zMFxmNlopjvZYu_GO5M7kkYNyjkmXv2R3n8y0hpvHfgzmVmOZn1o4KscRdmp69h8E2SJwBdQ-_RPwLcgfOs8xAtG_mM91hEWsQ9CwN2SfxY6z9Q50ols79k2Mz0Ttdk1vDP54TyOXYCPwz_ZB7x_KP4v3uGVbrvCX1lWg5Jh8gbgKqroV1NoSQ5obdOP9W4eg1x6uUcgfjWkMGUBfiP7MQus2ZwQsqT6Ji6NwSuBj1KE6sVFBaZmttNN8TXQcUDvg0dmesQrJcapj975DbtyX-e7W3fIKNA9FWsE8aw1EZqTeRQgeZJ37WvmVYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «آکسیوس به‌تازگی گزارشی منتشر کرده که در آن ادعا شده من به ایران
رفع تحریم‌ها و دسترسی به دارایی‌های مسدودشده
پیشنهاد داده‌ام. این ادعا نادرست است. من
هیچ چیزی به ایران پیشنهاد ندادم!
گزارش آکسیوس، مانند بسیاری از گزارش‌های دیگر، یک
جعل
است که صرفاً برای اهداف سیاسی منتشر شده است. آنها باید
فوراً این گزارش جعلی را پس بگیرند!
»
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24455" target="_blank">📅 01:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24454">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/24454" target="_blank">📅 01:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24453">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دلار ۲۴۵،۰۰۰ تومان ( رکورد تاریخی ) تتر ۲۴۵،۰۰۰ تومان ( رکورد تاریخی ) دلار کف بازار ۲۵۵،۰۰۰ تومان ( رکورد تاریخی ) @WarRoom
🚨</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/24453" target="_blank">📅 01:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24452">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXVGdxYaW6O1DG0B5y10o3HYjC-vI6zKHRGhFuAfTXfkwolyBh594hKOGqvxBj48ZpUXElVM0LDBrbHlU16ji-mYXX1Lt76S8-tOm5Hc9JModbct6f8fWvfdqGM22FNN9yNAQTqNi4UO6SaSnWfeCQTPP3efW4cd2V4-vMfdTe_rlx2IQQtMD9rwdVcCjk6IQonZQNziTsGUKry4rCOHl1BjaNT74Zn7s8AopUPVTofAn0HcWzR06hTawfLw-Q80sbWE5omPM-bGaaTf2egrLtMUb1Qm6VkMfoI3bWsZ-EWvRkrbC7lCqYXfmSu5rnJgGQz3qwRClMsHg286qHkzcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوی باشید ، تمام دایرکت شده نا امیدی غر نزنید ، بله اجماع شکل گرفته !
@WarRoom</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/24452" target="_blank">📅 00:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24451">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">داداش یاشار کی مث قبل لایو میذاری بگی تا صبح بیداریم امشب شب خطرناکیه  چرا نمیان پیر شدیم</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/24451" target="_blank">📅 00:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24450">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from....</strong></div>
<div class="tg-text">داداش یاشار کی مث قبل لایو میذاری بگی تا صبح بیداریم امشب شب خطرناکیه
چرا نمیان پیر شدیم</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/24450" target="_blank">📅 00:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24449">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وزارت دفاع عربستان سعودی: خالد بن سلمان، وزیر دفاع عربستان، از شیخ منصور بن زاید آل نهیان، معاون رئیس امارات و رئیس دفتر ریاست‌جمهوری، برای سفر به عربستان در روز سه‌شنبه ۲۹ سپتامبر ۲۰۲۶ دعوت کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/24449" target="_blank">📅 00:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24448">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پرتاب موشک هم اکنون از هرمزگان بندرکنگ به سمت تنگه
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/24448" target="_blank">📅 00:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24447">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دفتر نتانیاهو : بنیامین نتانیاهو و همسرش روز گذشته به دعوت شیخ محمد بن زاید، رئیس امارات متحده عربی، به امارات سفر کردند. نتانیاهو در این سفر توسط رئیس شورای امنیت ملی، رئیس موساد، دبیر نظامی و مشاور سیاست خارجی همراهی می‌شد.  @WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24447" target="_blank">📅 00:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24446">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دفتر نتانیاهو : بنیامین نتانیاهو و همسرش روز گذشته به دعوت شیخ محمد بن زاید، رئیس امارات متحده عربی، به امارات سفر کردند. نتانیاهو در این سفر توسط رئیس شورای امنیت ملی، رئیس موساد، دبیر نظامی و مشاور سیاست خارجی همراهی می‌شد.
@WarRoom</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/24446" target="_blank">📅 00:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24445">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آکسیوس: پیت هگست، وزیر دفاع آمریکا، در یادداشتی به تاریخ ۲۲ سپتامبر، به پنتاگون دستور داده از
توانمندی‌های اطلاعاتی و سایبری برای مقابله با مداخله خارجی در انتخابات آمریکا
استفاده کند. این دستور شامل جمع‌آوری اطلاعات درباره تهدیدهای خارجی علیه انتخابات و انجام عملیات مشترک سایبری با وزارت امنیت داخلی است. با این حال، این دستور
شامل حضور نیروهای نظامی در محل‌های رأی‌گیری یا توقیف تجهیزات رأی‌گیری نمی‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24445" target="_blank">📅 00:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24444">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نتایج یک نظرسنجی جدید در «کانال ۱۴» نشان می‌دهد که اکثریت اسرائیلی‌ها در مورد هشدارهای پیش از ۷ اکتبر، به روایت بنیامین نتانیاهو، بیش از تحقیقات روزنامه‌نگاران اعتماد دارند؛ به‌طوری که ۵۴ درصد معتقدند این گزارش‌ها با انگیزه‌های انتخاباتی منتشر شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24444" target="_blank">📅 00:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24443">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شکایت «شین‌بت» از شبکه ۱۲ به دلیل افشای خبر سفر به امارات
سازمان امنیت داخلی اسرائیل این شبکه را متهم کرد که با افشای خبر سفر نخست‌وزیر به امارات در زمانی که هواپیمای او هنوز خارج از حریم هوایی اسرائیل بود, یعنی حدود ۵۰ دقیقه پیش از فرود , جان او را به خطر انداخته است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24443" target="_blank">📅 00:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24442">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-zecgd33Z3d-zMe7VkQ3wJOin_-O52rN6MNTUkfp93EhG0yxQ_lKPl9rl42TWxTcqDO24n0tkp0UTNcc5PLvFw3jKZX-zuU0GExu53irFE4urc3hX9Rkh_73O0q8_g3krp3ognIchJx0ZesFI2sHTTGyLTRA7I650EbWooShc4Cy2p5xxX-2CEveAudrtaRomPP6f5bqaAXoiXoF-CrID_krpYuFjcB7X8tHLp1bOFqZppRn4BPbvLuvfpEqdqLrz5V-m6g4j0W4uhBzjTys9AexElS4ZnGN5uwMPaarejx6ScGeDcG7GUIA9YiDskScITo5DeNJIN-w5mJLei7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکانت توییتر کاخ سفید: ظرف دو هفته چیزی از اقتصاد ایران باقی نخواهد ماند
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24442" target="_blank">📅 00:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24441">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4109be46a.mp4?token=rUXtsrLQHY-wMrKCEmw4801yQBolhIcAY_AqD_goVJg51LcKCkBcyfnZub0sqipBmXt9sRe-hPGh1tx6bwEh7BtXGrk5sagrhKSq2DBW9DA5yCQ51u6Ekn73j-Smn4v0jwqEl3hXMidmiGH1BlaGG5XMyMEkMAYcgyci0rjgdArUG13-2G7uKij_YuMRJPlhYPuFamoSzQQfm6yg6quzemkupwFYhlHdT90jYkP-_xOmFqlDKVz2QaFNbtoivfw_F5hDuWZJzYikB06ZF6v5HjWkvwI2kTrE8o-TsRri6b875LoqPERr_U3BencRsj1z6HxSkADkmTI3nyDnbp67jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4109be46a.mp4?token=rUXtsrLQHY-wMrKCEmw4801yQBolhIcAY_AqD_goVJg51LcKCkBcyfnZub0sqipBmXt9sRe-hPGh1tx6bwEh7BtXGrk5sagrhKSq2DBW9DA5yCQ51u6Ekn73j-Smn4v0jwqEl3hXMidmiGH1BlaGG5XMyMEkMAYcgyci0rjgdArUG13-2G7uKij_YuMRJPlhYPuFamoSzQQfm6yg6quzemkupwFYhlHdT90jYkP-_xOmFqlDKVz2QaFNbtoivfw_F5hDuWZJzYikB06ZF6v5HjWkvwI2kTrE8o-TsRri6b875LoqPERr_U3BencRsj1z6HxSkADkmTI3nyDnbp67jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا تیم شما امروز با ایران صحبت کرده است؟
ترامپ: بله.
خبرنگار: با میانجی‌ها؟
ترامپ: بله.
خبرنگار: چیز دیگری هست که بتوانید با ما در میان بگذارید؟
ترامپ: ما پیروز خواهیم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24441" target="_blank">📅 23:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24440">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تنگه صدای ناله های حسن خرسی میاد</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24440" target="_blank">📅 23:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24439">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قشم صدا میاد</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24439" target="_blank">📅 23:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24438">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نیویورک پست: به نقل از یک مسئول آمریکایی، دیدار مقامات ایرانی با کوشنر و ویتک در نیویورک، منجر به مذاکراتی از طریق واسطه‌ها درباره امکان باز شدن تنگه هرمز شد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24438" target="_blank">📅 23:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24437">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8EQKd6ekgezZFQYUW4z95vqXEIrjWvrCoQ7ZR4XM0YCQEJjpzoEhC1h_HoYZORMOmUOzPXHvJTyNi-8JPmscl0xcG6z1EMwyPAxjvwRbScF6GwK8WrdOyWgvVtZF1OYLS_cqxedWRHCvllkaYGf1McsjTWvU4zPj_xyU5zRsVtMSGyx3_zeyeWcIU-ikZtuG7VlEFBMhbsV5QnxW1Y4gVGwMXzRU3eHa2Av3SwXwXdp4d8QtnHT71HCUrk-hCgahoSPbWEIkv_FjIHCiKVQya5lh79yRylLRMIWTnddfxJwSLUBBfMt-dZqxC4fHNYmkvlP4tVwCHJsfpZaokwVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : حضور
پنج فروند هواپیمای سوخت‌رسان، یک فروند T-38A Talon (هواپیمای آموزشی جت مافوق‌صوت)، یک فروند پهپاد MQ-4C (پهپاد شناسایی و مراقبت دریایی دوربرد) و یک فروند E-3B Sentry (هواپیمای هشدار زودهنگام و کنترل هوایی)
در محدوده تنگه هرمز و خلیج فارس رصد شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24437" target="_blank">📅 23:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24436">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e37e38e4cc.mp4?token=d1kIEQc9wGiN0zTyOug0VBcHPjmtSyeRkDZXaLFvOSklQRgG6m8rqpnEJgic4TM55Jl7r63Yxy-uEjAarOr62o7p32WLkpRf-8O1lsTeA10AEkr6p-ubBo0q9IaKU-yTwdT6vZ3hnIuR_liuIoUCkhnQfjcMBKClO9ne_-55CpuFeBjN93pAL9XxlT-ihAe5RTiHA7umLO000E4iCg6_Tt2-1CfX8M2zEHWiOxwwBfwn-0x_rEqHq7SGwa63_azDsIhNAKiHsOMKfMI7SvCc1fhE4ju__s1iRxV1QdqXavS1UuEFE5RM9o0q__GzO_9ivNwfbg2Im2Y4qLne60eg1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e37e38e4cc.mp4?token=d1kIEQc9wGiN0zTyOug0VBcHPjmtSyeRkDZXaLFvOSklQRgG6m8rqpnEJgic4TM55Jl7r63Yxy-uEjAarOr62o7p32WLkpRf-8O1lsTeA10AEkr6p-ubBo0q9IaKU-yTwdT6vZ3hnIuR_liuIoUCkhnQfjcMBKClO9ne_-55CpuFeBjN93pAL9XxlT-ihAe5RTiHA7umLO000E4iCg6_Tt2-1CfX8M2zEHWiOxwwBfwn-0x_rEqHq7SGwa63_azDsIhNAKiHsOMKfMI7SvCc1fhE4ju__s1iRxV1QdqXavS1UuEFE5RM9o0q__GzO_9ivNwfbg2Im2Y4qLne60eg1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: «من وارد جنگ شدم تا جلوی چیزی را بگیرم که می‌توانست یکی از بدترین اتفاقاتی باشد که تا به حال برای جهان رخ داده؛ برای ما، اما در درجه اول برای جهان. اسرائیل همین حالا از بین رفته بود. دیگر اسرائیلی وجود نداشت، خاورمیانه‌ای وجود نداشت و بعد موشک‌ها و بمب‌ها به سمت ما و اروپا روانه می‌شدند. و من جلوی آن را گرفتم.»
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24436" target="_blank">📅 22:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24435">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcbc9a39f.mp4?token=JXL9JSPZxgKmv1CawvTl4aAjdSJnhZeoLKZG8IiHZ5JKjbDROd1sx0KSWkU2zabtQaqPbgdONhzztQvvYXJz8opTUyCyI7fQ4wooEnaPAwzzEUpDHadkr5iB_a6-1pMNNRCn8TyIc8iqPWe2XwlTNgedDnbyN6nfe8eaK35zS71mTDYiWjAjn138OpY84rf8AiJ7EkJtBM-EZjZqRPQE620DSgu4KzmMJazQhWQLd5ALT7Vx7_sgreLHeRuVIfZGBxpzt3jkObhcn1Z203ToP_fdrm-m6YMBrPYtNq78_-fAoo-h25KaI_VKjO68IwqhLf9Pk-IXiNPBa2vRSz-apQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcbc9a39f.mp4?token=JXL9JSPZxgKmv1CawvTl4aAjdSJnhZeoLKZG8IiHZ5JKjbDROd1sx0KSWkU2zabtQaqPbgdONhzztQvvYXJz8opTUyCyI7fQ4wooEnaPAwzzEUpDHadkr5iB_a6-1pMNNRCn8TyIc8iqPWe2XwlTNgedDnbyN6nfe8eaK35zS71mTDYiWjAjn138OpY84rf8AiJ7EkJtBM-EZjZqRPQE620DSgu4KzmMJazQhWQLd5ALT7Vx7_sgreLHeRuVIfZGBxpzt3jkObhcn1Z203ToP_fdrm-m6YMBrPYtNq78_-fAoo-h25KaI_VKjO68IwqhLf9Pk-IXiNPBa2vRSz-apQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: «به‌محض اینکه این جنگ تمام شود، تورم به‌طور کامل از بین خواهد رفت. کاملاً. هیچ‌کس درباره این موضوع صحبت نمی‌کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24435" target="_blank">📅 22:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24434">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2bd292496.mp4?token=OYvLL8iT_zuOW1oqohrxeqNyKlmZjpYXHsob5mG9z-X1vSfZKlz4CzRPih6bJBZJ2d67slpvOk5NB04Q6l6h9FEQd2527BTzAOZqajBDluC21GB-VwxJIwL6QC5jhq25R2EXy3cff85l4QMoKMRxd35aUZqts1X_ZnNEBkZ4ep73hF45N6B0ojNXM_a2Xwrp-ydTjefsCyZCMhQIeCnCkRQtrLbVRIXW4jq5nWOmVA1k8gxEHRc8qtSjRUCIbJyIzAoRafnt8LpWU499kFtk8glu4xplFrPIzridqDn1SF0e94LR75lUpeG8q5yp9FAm_3_YJcmD8KP_ll_IvLwxgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2bd292496.mp4?token=OYvLL8iT_zuOW1oqohrxeqNyKlmZjpYXHsob5mG9z-X1vSfZKlz4CzRPih6bJBZJ2d67slpvOk5NB04Q6l6h9FEQd2527BTzAOZqajBDluC21GB-VwxJIwL6QC5jhq25R2EXy3cff85l4QMoKMRxd35aUZqts1X_ZnNEBkZ4ep73hF45N6B0ojNXM_a2Xwrp-ydTjefsCyZCMhQIeCnCkRQtrLbVRIXW4jq5nWOmVA1k8gxEHRc8qtSjRUCIbJyIzAoRafnt8LpWU499kFtk8glu4xplFrPIzridqDn1SF0e94LR75lUpeG8q5yp9FAm_3_YJcmD8KP_ll_IvLwxgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: «اگر می‌خواهید شاهد آشوب و یک فاجعه باشید، بگذارید آنها یک شهر را با سلاح هسته‌ای هدف قرار دهند. من فقط درباره اسرائیل و بخش‌های بزرگی از خاورمیانه صحبت نمی‌کنم. بگذارید آنها با یک سلاح هسته‌ای به خود ما حمله کنند؛ خطاب به تمام آن آدم‌های احمقی که فکر می‌کنند چنین چیزی اشکالی ندارد. آنها دیوانه‌اند. هیچ شکی در این باره نیست. آنها واقعاً آدم‌های دیوانه‌ای هستند. من همیشه این را به آنها می‌گویم. می‌گویم: «مرد، تو دیوانه‌ای.»
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24434" target="_blank">📅 22:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24433">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec45ce4fdf.mp4?token=WHg816dddPHgB20C0aJPZkwVvcqmY4FnmTtzdk4R9T77BWfKE3EwfHqpq0ck1XGUhrb1o4qT7zjj87DLLoGZ7bYcmcx_dIAdyf8Vp3QXOOvklMPMsiN53D_U73u8Nxs3pS_HDFQe_NOvaom_GUf-3LIXdT6WaB2Ax-CKfYQiYKKoHpuQV70NnBMNWZ-G-ExYKeEYUnJrQkGaQhqtvKawdSoWdOGNqOjI_ZMJ1hNJI1J0nZGjAC-atHgGGJ5WKbkahECX-4ivSQUiBjiMg1Q3AdqlUP-bWGs8qd6zU45xj_aGWsY0V0nSJWPq1uf9DXFXg5wE7vQjmPinAVP4lW16Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec45ce4fdf.mp4?token=WHg816dddPHgB20C0aJPZkwVvcqmY4FnmTtzdk4R9T77BWfKE3EwfHqpq0ck1XGUhrb1o4qT7zjj87DLLoGZ7bYcmcx_dIAdyf8Vp3QXOOvklMPMsiN53D_U73u8Nxs3pS_HDFQe_NOvaom_GUf-3LIXdT6WaB2Ax-CKfYQiYKKoHpuQV70NnBMNWZ-G-ExYKeEYUnJrQkGaQhqtvKawdSoWdOGNqOjI_ZMJ1hNJI1J0nZGjAC-atHgGGJ5WKbkahECX-4ivSQUiBjiMg1Q3AdqlUP-bWGs8qd6zU45xj_aGWsY0V0nSJWPq1uf9DXFXg5wE7vQjmPinAVP4lW16Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا حادثه پایگاه RAF Fairford به ایران مرتبط است؟
ترامپ:
«ممکن است مرتبط باشد، اما باید بگویم از اینکه آنها [افراد بازداشت‌شده] را آزاد کردند،
متعجب شدم. من این کار را نمی‌کردم.
»
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24433" target="_blank">📅 22:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24432">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ: امروز از طریق واسطه‌ها با ایران گفتگو داشته‌ایم.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24432" target="_blank">📅 22:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24431">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6885716a79.mp4?token=TZ7arRvyGBYk8h3NWmADO5c6lDBmVI20YWofr5linv5Xl9ZpLFVD-30WAKQh__yXh7rTp43MfwzvuEBpa5orbHhpsKWoHmgy4pRysf4eudU3oAr9nXK5GZQj6YYMq2dUr_jzuB_qbE4MbLF-q2Az6MZu668RoCiOjev88aF1_yXJouc43--UgI3HlyvpePe7ffSCbsxYiHf3CrgLLRrjZL4OjCzkpGUuFP65x7PPjN3JljCHygfmnl4pK2OnPe_0Z3fdU3FeT4hmG9tZuTP-NKJprRxeejNaeYVjq-RuCJNjPj2cvDDtGdSqWKCrVhPYqmEzoCG7eaUl4mW3VxuAQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6885716a79.mp4?token=TZ7arRvyGBYk8h3NWmADO5c6lDBmVI20YWofr5linv5Xl9ZpLFVD-30WAKQh__yXh7rTp43MfwzvuEBpa5orbHhpsKWoHmgy4pRysf4eudU3oAr9nXK5GZQj6YYMq2dUr_jzuB_qbE4MbLF-q2Az6MZu668RoCiOjev88aF1_yXJouc43--UgI3HlyvpePe7ffSCbsxYiHf3CrgLLRrjZL4OjCzkpGUuFP65x7PPjN3JljCHygfmnl4pK2OnPe_0Z3fdU3FeT4hmG9tZuTP-NKJprRxeejNaeYVjq-RuCJNjPj2cvDDtGdSqWKCrVhPYqmEzoCG7eaUl4mW3VxuAQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ما
خیلی زود در این جنگ پیروز خواهیم شد.
این جنگ تمام خواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24431" target="_blank">📅 22:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24430">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e7e5f951.mp4?token=jUzRGcvTceE4mh4bktmWzhkBVG1kYMqVG5EYAJs_UDUc5yB5-CPHvwxN2c8jRgsnwL3Z1deQZTZYRH8XnCBGoB3rsI445mPwoKtkpoUGEw9j-Q9WIAv10hCQrE2-rnbTMUDwD9KDOGBzloQM5wEMvq9vge4wT_No1qBcUJYLmm-sRz1AkQivLUqE5bpVEainsdaLvObqJSBAqtfm06G9LeCYLX0FdY2adlH8zbBqa6FGmjhGu-sqlEiBMXsbJbvDtJuqjAf3J82bml1Pj6yghBucYImdh7G2BA5RzBfE0dV8VNL1C3vDKcDWKn1XSMFWCNEqmU4fUjUUPKuE3EbPDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e7e5f951.mp4?token=jUzRGcvTceE4mh4bktmWzhkBVG1kYMqVG5EYAJs_UDUc5yB5-CPHvwxN2c8jRgsnwL3Z1deQZTZYRH8XnCBGoB3rsI445mPwoKtkpoUGEw9j-Q9WIAv10hCQrE2-rnbTMUDwD9KDOGBzloQM5wEMvq9vge4wT_No1qBcUJYLmm-sRz1AkQivLUqE5bpVEainsdaLvObqJSBAqtfm06G9LeCYLX0FdY2adlH8zbBqa6FGmjhGu-sqlEiBMXsbJbvDtJuqjAf3J82bml1Pj6yghBucYImdh7G2BA5RzBfE0dV8VNL1C3vDKcDWKn1XSMFWCNEqmU4fUjUUPKuE3EbPDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ:«اگر جمهوری‌خواهان در مجلس نمایندگان و سنا پیروز شوند، به هر فرد بزرگسال ۵ هزار دلار پرداخت خواهیم کرد. و ما می‌توانیم این کار را انجام دهیم.
دموکرات‌ها نمی‌توانند، چون هیچ درآمدی ندارند و کشور را به سمت رکود اقتصادی خواهند برد. آنها هیچ پولی نخواهند داشت.»
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24430" target="_blank">📅 22:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24429">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQZAA4vqI3pKotLY1ArEvlVyafe4fz9ld2kyWNNBtapZFX0QI_lp71_NJOrrWUvXKnRfeAqHdGCCn6IIM57hB9miFltLn-Kw4hJYO84w970zQy7N4xVTIl7g4a-h4H3GTxXb9SNiQMJP3uKfBolYt4ji_uUklnIa4OC1g8d2k9L5CmeT_y_Q11Pcv-B0GydI3v2pG5vs_gzft4NTpOfwpyHe5y6qgSxK33GVnrKddHpl7hJWxQmpYxgM-U2H9l4iCfW-sDFfQr3IvMaZ0alWhIE4LynqfMd2IcQO-rW2lBzpLFOn9w3WVPhZNZofsx6US59cG9juQeAdxOX20W8aXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: بزرگترین کارخانه فولاد در آیووا ساخته خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24429" target="_blank">📅 22:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24428">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">باراک راوید ، آکسیوس :به گمانم ایالات متحده می‌خواهد شاهد آن باشد که ایران بازرسان آژانس بین‌المللی انرژی اتمی را دوباره دعوت کند؛ کاری که در جریان مذاکرات سوئیس متعهد به انجام آن شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24428" target="_blank">📅 21:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24427">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">امارات متحده عربی سفر نخست وزیر اسرائیل به این کشور را تکذیب کرد</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24427" target="_blank">📅 21:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24426">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70875dba60.mp4?token=PkWZdId0lH8nfzayVWihy7-43Z6RSeUn_CjEZlNX5wYAQQPzxUTJcZLg9y9yMDeg_akzJjX216yLFkz8oIkM0-d0WHJngn_NIlZXCsyZwyBwAzmmxcBPC4rv0NudNWJ37w7v2LFqcf8HDiPPIMhP-6dMKwEZt_8_1Uv0kb823dIaroEg94ZvBnEz5-5gmhKTnwlILdKz6mZ--gSdMvIe99FzR4N-Dl25yN1Aj0xvSg_8w6tuHN2A6_t-ybPSBXv1MonrAiuR_32Kpz6iQZVqccD9TdUIIo7ZWosXM10C3Tro2YpKTtVrFp6fTW5xnXqFOEOTMmBlE9IUddn0eJndPWfDtmsPbvxxr7MtGF0ei5T3_G76nDMTYpZcsEO-SMcufO02Hju7VXNgKuR40L75--5ucTNmohLNBrneTv70TvuP6gFtJlZYSCZkeglVpxd4K6i_RQX06j0dFEiuGpPTIfPixW27r1pfqPPaxem-hmxIxX8f8LaNu6idXFRQMZM8aYsahWwubFBWsauxw6va3rZEp0BpjM15TWRdRcy-6Kp2E6a1RKdiBbtt5zjKvcFF1Xfjyqgk30mC-165yODImnpE311r8V_5d5MxZnB1Svym2DVqwJJM517cT5MN_BvhNl0T8YUIdLRFzY9i4xXlk89CthafULNjcTPhxDaUMZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70875dba60.mp4?token=PkWZdId0lH8nfzayVWihy7-43Z6RSeUn_CjEZlNX5wYAQQPzxUTJcZLg9y9yMDeg_akzJjX216yLFkz8oIkM0-d0WHJngn_NIlZXCsyZwyBwAzmmxcBPC4rv0NudNWJ37w7v2LFqcf8HDiPPIMhP-6dMKwEZt_8_1Uv0kb823dIaroEg94ZvBnEz5-5gmhKTnwlILdKz6mZ--gSdMvIe99FzR4N-Dl25yN1Aj0xvSg_8w6tuHN2A6_t-ybPSBXv1MonrAiuR_32Kpz6iQZVqccD9TdUIIo7ZWosXM10C3Tro2YpKTtVrFp6fTW5xnXqFOEOTMmBlE9IUddn0eJndPWfDtmsPbvxxr7MtGF0ei5T3_G76nDMTYpZcsEO-SMcufO02Hju7VXNgKuR40L75--5ucTNmohLNBrneTv70TvuP6gFtJlZYSCZkeglVpxd4K6i_RQX06j0dFEiuGpPTIfPixW27r1pfqPPaxem-hmxIxX8f8LaNu6idXFRQMZM8aYsahWwubFBWsauxw6va3rZEp0BpjM15TWRdRcy-6Kp2E6a1RKdiBbtt5zjKvcFF1Xfjyqgk30mC-165yODImnpE311r8V_5d5MxZnB1Svym2DVqwJJM517cT5MN_BvhNl0T8YUIdLRFzY9i4xXlk89CthafULNjcTPhxDaUMZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وس استریتینگ، وزیر دفاع بریتانیا، درباره ایران:
«فکر می‌کنم حمایت از اقدام دفاعی آمریکا، کار درستی بود.
کاملاً درست است که بگوییم جنگ در ایران، جنگی نبود که ما انتخاب کرده باشیم؛ اما در عین حال، هیچ شکی نیست که ایران نیرویی شرور و مخرب است که بریتانیا، منافع ما و متحدانمان را تهدید می‌کند.»
پلیس گلاسترشر گفت ساکنانی که به‌دلیل احتمال وجود توطئه‌ای برای حمله به پایگاه هوایی سلطنتی فیرفورد (RAF Fairford)، از حدود ۸۵ خانه در اطراف این پایگاه تخلیه شده بودند، اکنون می‌توانند به خانه‌های خود بازگردند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24426" target="_blank">📅 21:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24425">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یک منبع آمریکایی به شبکه العربیه گفت: اختلافات و موانع بزرگی بین تیم‌های مذاکره‌کننده آمریکایی و ایرانی وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24425" target="_blank">📅 21:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24424">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h03QE-9VgJt1sMOtr0RR-zRHbpcEvVOwD-OOVgNT2gH3w4wM7YxiQYgm7Nq2XpqMGMCkGZ7OjpGLlHAx1UnOA-HYcHaTKMGWVD-oubCuDq4xxjKb_Dtyt3SP9pbjWJMS0yZ4zrIprxwAvYF1OItAUSb-3iCdpNpRXoJM6ArBnR9P6d6aUScX8ZjbSbVJOUl2eskzu4lUqtYVkb-6NXxQ4xyDjwSCHbAHV8nthHBxH81zY8DpflNVYr9tqTp3-oNkzxCKmRzIKdLLGCcFnS-9KvbAHfVSN9ik_pqMToYEcBqIefCJC1gDDEjZc87YvP5pWBbQKEeLrCe3SijyR85clg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
عملیات طرد اقتصادی باعث شده که ریال به رکورد‌های پایین‌تری برسد.
ما به تخریب توانایی رژیم ایران برای تأمین مالی تروریسم و توسعه سلاح هسته‌ای ادامه خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24424" target="_blank">📅 21:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24423">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ارتش اسرائیل : لحظاتی پیش، یک موشک رهگیر به سمت یک هدف هوایی مشکوک در منطقه‌ المطلة  که سربازان  ما در جنوب لبنان در حال عملیات هستند شناسایی شده بود، شلیک شد.جزئیات در حال بررسی است
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24423" target="_blank">📅 21:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24422">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کانال ۱۲ اسرائیلی:
نهادهای امنیتی اسرائیل در حال آماده‌سازی برای احتمال از سرگیری درگیری‌ها با ایران هستند
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24422" target="_blank">📅 21:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24421">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6rgUJh4bWEQZO77rQOOgMl3DqLdC1hxgAYDnpMlDsq_jG-SUj_AQ2_H5E9TlueTdoEORUoLWzPsgYJ-sxSW_FMOflg9vIWpMcPeJ7V02d92ygXWLpxAorE1kS3kIGUDqRb6pq-pNt9a4TaaPMDJ71a6qpdED5SwXFsIgeyT0gNeZ12CBYK2GFXaG1nTSGueKZVmJJGsH3ux6ZeKK8RVVpbsMDr0DI2nf--stmV9YE2Q_1K6Zc5uaFZvVigm8NEJwzeFexAgDUDkFd4WAMM8MW0MgUJQxNxlv3uaJU5FtlBq3T6he0ta_wrUlVH5fsSg_9WV7Xwy089DudubrxuwfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل:
شَدی ابوحطیرا، از تأمین‌کنندگان مالی حماس که شبکه انتقال پول «ژنو» را هدایت می‌کرد، در یک حمله هوایی دقیق در غزه کشته شد. ارتش اسرائیل مدعی است او
ده‌ها میلیون شِکِل ارز خارجی
را برای شاخه نظامی حماس منتقل کرده
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24421" target="_blank">📅 18:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24420">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مورگان اورتگاس، معاون فرستاده ویژه آمریکا در امور خاورمیانه: «سناتور لیندزی گراهام هرگز از باور به شما (مردم ایران)دست نکشید. او باور داشت که شما دوباره آزاد خواهید شد. او هرگز از تشویق رئیس‌جمهور ترامپ و وزیر خارجه روبیو برای حمایت از آنها (مردم ایران) دست نکشید.»
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24420" target="_blank">📅 18:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24419">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsIHM51IYc2T4VzbK-Qg9lCUIGD_06dNneaw9CUpFtJvChMVLQ4ex1UB7MXsqEEzaZ3ENbpk1_99_dLdNBK7Whp3X2q4hsGxvk-flqNSXn7VxB6Q9-sRYs6YD94DVp897HylolOe9SlL8b-8eVfETTJOLzKxxkhHeoqG7Gqrz76TXVnDaC8vat4yMGiK7Zf58twJq9HRb_9TlXvYTLOG2w8tOrkp5-rP8Rau2BERFzSfoONgV-UTKDvunKoyhrquaBtbVlPOhhOFn2KYEHnz9gPL-lu231ZyW_c_qEKCxGXtjd4p_h2fyztXvISqj_Nzy_wg_UL0U6QrRkJVgUMrtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا این لحظه عراقچی موفق شده یه ناو جدید اعزام کنه ۳ دسته هر کدام ۵ فروند هرکولس و ۱ اسکادران اف-۲۲ ، این است «قدرت مذاکره»
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/24419" target="_blank">📅 18:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24418">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تسنیم : عراقچی امروز با میانجی‌گران در نیویورک دیدار می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24418" target="_blank">📅 17:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24417">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">برنامه امروز دونالد ترامپ به وقت تهران: کاخ سفید اعلام کرده ترامپ امروز دوشنبه ۲۸ سپتامبر، ساعت ۱۸:۳۰ یک جلسه سیاست‌گذاری در کاخ سفید و ساعت ۲۰:۰۰ و ۲۰:۳۰ دو جلسه دیگر در دفتر بیضی خواهد داشت. سپس ساعت ۲۱:۳۰ ترامپ در دفتر بیضی مقابل خبرنگاران حاضر می‌شود و…</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24417" target="_blank">📅 17:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24416">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گزارشهای بسیار‌ از دو انفجار سنگین در تنگه هرمز
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24416" target="_blank">📅 17:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24415">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjzCXYJvxGOmHbg4wtl3-UQcIFJSFpvTrkzznNcDW06yr2xyZugk1W2SL5AeyFYfZ8rIxmrkKLyIX3BU64aMOGn_HgLj_-ujFy8EP_4jdzsf8Oih78YyXc83h29ALxgm2b5xnUo5RWTuaBn3gCsxF9l3wEjtAZKMLs8EAj4DMvSlSQ_GdsSWAxzOYMqdehX98k3MucAaSEZW6MfOTq168M7OYfrVYB79y32bRgATVbcNNFVuYnzVYarjrGA56Ph2fx7rbP3R2ssYmgfs2KWcjqqJ6sUj_4zouhV-4GXUfXH24vvdIN-k1Bkg2WOb71Q3hv-v25Huv1CqE2gGds_4jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : فلکه دوم فردیس لانچر و موشک آوردن
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24415" target="_blank">📅 17:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24414">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">برنامه امروز دونالد ترامپ به وقت تهران:
کاخ سفید اعلام کرده ترامپ امروز دوشنبه ۲۸ سپتامبر، ساعت
۱۸:۳۰
یک جلسه سیاست‌گذاری در کاخ سفید و ساعت
۲۰:۰۰
و
۲۰:۳۰
دو جلسه دیگر در دفتر بیضی خواهد داشت. سپس ساعت
۲۱:۳۰
ترامپ در دفتر بیضی مقابل خبرنگاران حاضر می‌شود و
یک اعلام رسمی مهم
خواهد داشت؛ موضوع این اعلام هنوز رسماً اعلام نشده، اما گزارش‌های منتشرشده آن را مرتبط با
هوش مصنوعی
می‌دانند. ترامپ ساعت
۲۳:۰۰
نیز با خبرنگاران رسانه‌های چاپی دیدار و گفت‌وگو خواهد کرد. شام خصوصی ترامپ با
داریو آمودی، مدیرعامل Anthropic و سازنده Claude
مربوط به شب گذشته بوده است. همچنین فردا ترامپ و مایک جانسون قرار است با مدیران شرکت‌های بزرگ هوش مصنوعی دیدار کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24414" target="_blank">📅 17:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24413">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">امروز ترامپ بیانیه ویژه ای ارائه خواهد داد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24413" target="_blank">📅 16:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24412">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24412" target="_blank">📅 16:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24410">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy5TFwBONIKUxNnrjd-fMJNE1FWb9EWDe8oGCgdMJQDDHPvs3r9xLS6aVjR2XvMT5DGgEMkazjgFu_uQIDXapJJ-64QYXmWvOMG6fxTW9NqWNm6RK1mREh6F_7boT8TrwQBUc4fOjyq6Z0ApQS5rVKCPuB5JIsYQ65k10IHuaK8EPC-K8lnsav3B8OL55bk0Iz9L91UY0BOnF8e_jtwuNMP0zVX0k0VaMTAEGyZFPlqzn5AM-yU_EIKk920WdEqJIlvmrC9RiI8UkVbU6UPRkr45kqfWAAuz2wXDjR-h15LSmyenYdK3PyeYe756JGSMPbdvVpBKVU3DWEHm3uzqhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/092268a67d.mp4?token=YKUL5TsibO--UHVClYzMpSreh0fd2tQ2RUpKyHg4xFSuDaREeqRbchuwulghAehDie0Imu_nLuf1agNF7zRc1HftlyoaTeO1f0RbyR-zOGuT1piwWCIL-gqLME84ke8hTnYuf0HYZntx28JeO6hN8Lcw4SrLeJ4PDSz7Be2n3CmbbitZrky61EB_jhunf5knL-LmmxhGCKOwQS0GCl5ZYY6JIU9gU2q2bthyueYBf73GnY-tY6Rhi-3o0dD72OYxtNtkb4FuXybZmAZZwj0G3vl32SVS4sbHjYkDtV0Dooks_3Fn0gzY6gG6UvWbV-9BpUaX8FNgmKye1BJUySyXbQuxpgOg2aqTrRa4QF1LEprX-D5v9t76DcXuopgwzdIWlvUoW80FAXSix54n9JV3OciCi0-BPcSNiuFIzi1UbmS6g5JYHGFtSLqP0mR1I5e__MWaRwYzvpQft103R_VVHCzkRQWb7yTVBcJPNKfP79fjETccA5V8d9eKfZQkxX5J8TWDyvrkD4vYSqt5HDL8glVXmXd_GwY3Nt9pNOCvGrxaUERzipN_VVxYPR9osgYvpQReQIcxntblW92W3vyWz_ZxyXpRYqGGwjrc2pyw20rvXdmBlG5Wuw2-TzChYJKwLPVHFjnzUvqJayAvd1MIOf1bYhP8yxJeU4N5zafLclk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/092268a67d.mp4?token=YKUL5TsibO--UHVClYzMpSreh0fd2tQ2RUpKyHg4xFSuDaREeqRbchuwulghAehDie0Imu_nLuf1agNF7zRc1HftlyoaTeO1f0RbyR-zOGuT1piwWCIL-gqLME84ke8hTnYuf0HYZntx28JeO6hN8Lcw4SrLeJ4PDSz7Be2n3CmbbitZrky61EB_jhunf5knL-LmmxhGCKOwQS0GCl5ZYY6JIU9gU2q2bthyueYBf73GnY-tY6Rhi-3o0dD72OYxtNtkb4FuXybZmAZZwj0G3vl32SVS4sbHjYkDtV0Dooks_3Fn0gzY6gG6UvWbV-9BpUaX8FNgmKye1BJUySyXbQuxpgOg2aqTrRa4QF1LEprX-D5v9t76DcXuopgwzdIWlvUoW80FAXSix54n9JV3OciCi0-BPcSNiuFIzi1UbmS6g5JYHGFtSLqP0mR1I5e__MWaRwYzvpQft103R_VVHCzkRQWb7yTVBcJPNKfP79fjETccA5V8d9eKfZQkxX5J8TWDyvrkD4vYSqt5HDL8glVXmXd_GwY3Nt9pNOCvGrxaUERzipN_VVxYPR9osgYvpQReQIcxntblW92W3vyWz_ZxyXpRYqGGwjrc2pyw20rvXdmBlG5Wuw2-TzChYJKwLPVHFjnzUvqJayAvd1MIOf1bYhP8yxJeU4N5zafLclk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : چند فروند جنگنده اف-۲۲ رپتور طی ۳۰ دقیقه گذشته از پایگاه نیروی هوایی لنگلی به پرواز درآمده‌اند.علاوه بر این، سه فروند هواپیمای سوخت‌رسان KC-46A نیروی هوایی آمریکا با نام عملیاتی CORONET نیز به پرواز درآمده‌اند که احتمالاً در حال پشتیبانی از انتقال جنگنده‌های رپتور به خاورمیانه هستند:
GOLD21: هواپیمای سوخت‌رسان KC-46A (شماره ثبت 17-46034)
GOLD22: هواپیمای سوخت‌رسان KC-46A (شماره ثبت 16-46021)
GOLD31: هواپیمای سوخت‌رسان KC-46A (شماره ثبت 18-46051)
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24410" target="_blank">📅 16:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24407">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4efe2963dc.mp4?token=oByrP_4I0TSEKYMOMg-iKUXbwNgF4c1V2Uz09d7sDsKbHU6N9E1S8-mT0D-AbMg_667jYNpzLIKQbu-NLajWBOm5NGv70C_dUUz3s3zOQicK8JM1bWHXlkJcHsmv68JI6XojGgpcEi3EV9fruE6TXxld2aa76W7ArJP9L8ZJ4tDjJSqmu_zRPFn5_r82BZyaxfdh8ug2xMq7EzxcWVKD5kqxdvm1LVIel4nTxP37Sj8sr66lS5ky6jOB_JSxUhnhMEwE9CfisTywPPI3KrusMC6bc7YcpUgNRcRI8lSuSyruMmzTRNRBjaVEQaQGcSo85qILVqhSwZBWVeq-NsN5uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4efe2963dc.mp4?token=oByrP_4I0TSEKYMOMg-iKUXbwNgF4c1V2Uz09d7sDsKbHU6N9E1S8-mT0D-AbMg_667jYNpzLIKQbu-NLajWBOm5NGv70C_dUUz3s3zOQicK8JM1bWHXlkJcHsmv68JI6XojGgpcEi3EV9fruE6TXxld2aa76W7ArJP9L8ZJ4tDjJSqmu_zRPFn5_r82BZyaxfdh8ug2xMq7EzxcWVKD5kqxdvm1LVIel4nTxP37Sj8sr66lS5ky6jOB_JSxUhnhMEwE9CfisTywPPI3KrusMC6bc7YcpUgNRcRI8lSuSyruMmzTRNRBjaVEQaQGcSo85qILVqhSwZBWVeq-NsN5uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراضات به گرانی دانشگاه علامه طباطبایی
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24407" target="_blank">📅 16:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24406">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A38Llg6jjf3xo06fjt5E098teKI3DQf8O46QRdzx4fCIXysqEM6giZDINCf83MxXpH8Jf_cDHR4KCin9fmjcsiVWy9Av8xrK40DQoKW5rNwtykgwBnNS7SRyIjbXo00GZt8ZoJR_YNxtHwYwnlHZQx16iRT4vpgE4UsznfSbAqm_uta7RgKFCUZ3ieMw3GoUt1octMw2llbt3NcLyhJhIrlMmMuZGl7BAA5NLawJbArJgVKzJfPav0avQUNzUVwNmlyIwp5_zoAa6d0hDbHdNs-g0WWygBlXajitxxDHY17z6R9gHTc6db6WBi_6QEQd9LVOVKgbBOrN-MByPVOJEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار ۲۴۵،۰۰۰ تومان ( رکورد تاریخی )
تتر ۲۴۵،۰۰۰ تومان ( رکورد تاریخی )
دلار کف بازار ۲۵۵،۰۰۰ تومان ( رکورد تاریخی )
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24406" target="_blank">📅 15:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24405">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQbVD6qGhA1Gz8DOl3o5iOa2dBdsQp0YvWS0IHKjaJL4gYd3pifb0YEUYka7pSJrZYL9_OxXVpqL1bGfCK5NMe97PoH1lJcOO4bXc4WXoalI9v-rY4Jyt3vVhFSNv6oJeYO28bBt-va2sfKb2Fh6-uwkrAPheOpIo4B6tCSYaJ2jTZkMLAF-WSGhM-bQGb_dqy4hIYdxI_rdSGU5vy2j6Eaq8O4pZIgy0Xz_FAVB6IKRxGe_X96Iz1Wz0a2ayouE4hH-Rog-zX5imnDeKhZKWI_73W1j8HGeY0sZiCvwwOn8P_NPuvieaz5frurdx1HCXONBWi9nZkB8-MNVtAqtPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقت یاب سنتکام:
ادعا رژیم :
یک فرمانده ارشد سپاه پاسداران امروز گفته است ایران از طریق «نیروی دریایی» خود
کنترل کامل تنگه هرمز
را در اختیار دارد. این ادعا
نادرست
است.
واقعیت:
ایران نیروی دریایی ندارد، زیرا
نیروهای آمریکایی آن را غرق کردند.
ایران همچنین کنترل تنگه هرمز را در اختیار ندارد؛ همان‌طور که
هزاران کشتی آزادانه از این تنگه عبور کرده‌اند
و تنها طی چند ماه گذشته،
بیش از یک میلیارد بشکه نفت
از این مسیر عبور کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24405" target="_blank">📅 15:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24404">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEQ3</strong></div>
<div class="tg-text">یاشار بندر عباس طرف پارک شهدا صدای دو تا انفجار اومد با فاصله 3 دقیقه از هم</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24404" target="_blank">📅 15:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24403">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گزارش صدای انفجار بندر
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24403" target="_blank">📅 15:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24402">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترکیه تودی :
پروازهای باقی‌مانده شرکت‌های هواپیمایی ایران به ترکیه نیز ممکن است
از اوایل اکتبر ۲۰۲۶ / اواسط مهر ۱۴۰۵ متوقف شود
. این رسانه به نقل از
دو منبع مطلع
گزارش داده که به‌دلیل تشدید تحریم‌های آمریکا علیه صنعت هوانوردی ایران، انتظار می‌رود تمام پروازهای شرکت‌های ایرانی به ترکیه لغو شوند. یک منبع نزدیک به صنعت هوانوردی ایران نیز این موضوع را تأیید کرده است. با این حال،
مقامات ترکیه هنوز چنین تصمیمی را رسماً اعلام نکرده‌اند
و یک منبع دیگر نیز نتوانسته این خبر را تأیید کند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24402" target="_blank">📅 14:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24401">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اینوستینگ :
بیت‌کوین امروز تا حدود
۸۳ هزار دلار
عقب‌نشینی کرد و حدود ۱.۷ درصد کاهش داشت. افزایش بازده اوراق خزانه آمریکا و نبود پیشرفت محسوس در مذاکرات ایران و آمریکا، اشتهای سرمایه‌گذاران برای دارایی‌های پرریسک را کاهش داده است. اتریوم نیز حدود ۲ درصد افت کرد و آلت‌کوین‌ها عمدتاً در مسیر نزولی قرار گرفتند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24401" target="_blank">📅 14:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24400">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رویترز:
طلا امروز حدود
۳ درصد سقوط کرد و به پایین‌ترین سطح بیش از هفت هفته اخیر رسید
؛ علت اصلی، افزایش قیمت نفت و بالا رفتن انتظارات برای افزایش نرخ بهره عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24400" target="_blank">📅 14:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24399">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اورشلیم پست:
منابع حوثی مدعی شده‌اند حملات عربستان به مناطقی در تعز تلفات سنگینی برجای گذاشته و حوثی‌ها تهدید کرده‌اند در واکنش،
پل‌های داخل عربستان
را هدف قرار دهند. اصل حمله و میزان تلفات هنوز از سوی منابع مستقل تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24399" target="_blank">📅 14:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24398">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مقوا ای آی : انقلاب اسلامی
سلطه و وابستگی ایران به قدرت‌های خارجی را پایان داد
و ایران را به کشوری مستقل تبدیل کرد. او سیدحسن نصرالله را شخصیتی کم‌نظیر دانست و گفت
پرچم او اکنون در دستان شیخ نعیم قاسم
است. وی مخالفان مقاومت لبنان را به
بی‌تدبیری و حتی خیانت
متهم کرد. خامنه‌ای ایران را
قدرت اول جهان بر اساس «محاسبات الهی»
خواند و مدعی شد دشمنان ایران پس از ضربات رزمندگان، دیگر حتی از
دریای عرب جلوتر نمی‌آیند و به‌زودی از این منطقه نیز خارج خواهند شد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24398" target="_blank">📅 14:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24397">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرگزاری
NBC:
در جزئیات تازه‌ای که امروز منتشر شده، اعلام شد در
۲۳ شهریور ۱۴۰۵ (۱۴ سپتامبر ۲۰۲۶)
، یک موشک کروز ضدکشتی ایران در
تنگه هرمز
به یک شناور حامل نیروهای آمریکایی اصابت کرده و
۸ تفنگدار دریایی آمریکا
زخمی شده‌اند. به گفته سه مقام آمریکایی، هر ۸ نفر دچار
آسیب ناشی از استنشاق دود
شده‌اند و برخی نیز علائم
ضربه مغزی و احتمال آسیب ناشی از موج انفجار
داشته‌اند. این افراد شامل ۷ سرباز و یک افسر از نیروهای تفنگدار دریایی بودند. هیچ‌یک از مجروحان وضعیت وخیمی نداشتند و هر ۸ نفر پس از مدت کوتاهی به خدمت بازگشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24397" target="_blank">📅 14:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24396">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وحیدی :  اشتراک چت جی‌پی‌تی مون رو تمدید کردیم ، یه پیغام از مقوا براتون میزارم تا ساعاتی دیگه
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24396" target="_blank">📅 13:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24395">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دلار ۲۴۴،۰۰۰ تومان (رکورد تاریخی)
تتر ۲۴۴،۰۰۰ تومان (رکورد تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24395" target="_blank">📅 13:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24393">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">در فرودگاه بین‌المللی مهرآباد تهران طی ساعات گذشته، یک فروند هواپیمای C-130 هرکولس متعلق به نیروی هوایی ارتش جمهوری اسلامی و یک فروند هواپیمای ایلیوشین-۷۶ (Il-76) متعلق به نیروی هوایی ارتش یا نیروی هوافضای سپاه پاسداران در این فرودگاه به زمین نشسته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24393" target="_blank">📅 13:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24392">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رئیس سازمان هواپیمایی کشوری با اشاره به تلاش‌های مستمر این سازمان برای احیای مسیرهای پروازی، از رایزنی با وزارت امور خارجه و ثبت شکایت رسمی نزد سازمان بین‌المللی هوانوردی غیرنظامی (ایکائو) در واکنش به محدودیت‌های اعمال‌شده علیه صنعت هوانوردی ایران خبر داد.
@WarRoom
یاشار : بدجور دارن تو باتلاق دستو پا میزنند ولی هی میرن پایین تر</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24392" target="_blank">📅 13:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24391">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نرخ دلار ۲۴۱،۰۰۰ تومان (رکورد تاریخی)  تتر  ۲۴۰،۰۰۰ تومان(رکورد تاریخی)  بیتکوین ۸۳،۱۵۸ $ انس جهانی طلا ۴،۱۶۳ $ نفت برنت ۹۸،۷۳$ @WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24391" target="_blank">📅 12:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24390">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43823eee78.mp4?token=GhGh4EpKatVaPUml3Xqi94BDc4pFW_wL_TknktQnvyX41S7wx3bHL_gAgeEExhkMD-NELFQep60AdpWGBnSpD4U-_g46aubRZkAm0kFMLopzn4pq1IXNavqlJqvk9k97j88f9ngsHbk00CaI_vtD_S9ooNTDzZPiU_3RE_uwRNEedmHcLk8LvQyutZUY0Rh_1EjKFDeccTvqLNzs9tQumPtBFE43YKMw3LWutnP8uyB6Ho18_mA8rOAXtH_UppkvN9xa3wXD2W0w4rPPcTscvwAb2aOhKY1TfS0w5S28QpHA-aEUxpXkZiWqdJ7vsKDTcAgKqbFAM1I8J9jFfDVCrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43823eee78.mp4?token=GhGh4EpKatVaPUml3Xqi94BDc4pFW_wL_TknktQnvyX41S7wx3bHL_gAgeEExhkMD-NELFQep60AdpWGBnSpD4U-_g46aubRZkAm0kFMLopzn4pq1IXNavqlJqvk9k97j88f9ngsHbk00CaI_vtD_S9ooNTDzZPiU_3RE_uwRNEedmHcLk8LvQyutZUY0Rh_1EjKFDeccTvqLNzs9tQumPtBFE43YKMw3LWutnP8uyB6Ho18_mA8rOAXtH_UppkvN9xa3wXD2W0w4rPPcTscvwAb2aOhKY1TfS0w5S28QpHA-aEUxpXkZiWqdJ7vsKDTcAgKqbFAM1I8J9jFfDVCrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏دیوید پردو، سفیر ایالات متحده در چین: شی جین پینگ در ماه مه موافقت کرد و در اینجا نیز آن را تکرار کرد که آنها از عدم وجود سلاح هسته‌ای در ایران حمایت می‌کنند، این بسیار مهم است
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24390" target="_blank">📅 12:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24389">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دریادار سیاری، از فرماندهان ارشد ارتش: «غرب تنگه هرمز و خلیج فارس تحت کنترل کامل نیروی دریایی سپاه پاسداران قرار دارد. در شرق تنگه نیز کنترل کامل در اختیار نیروی دریایی ارتش ایران است.»
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24389" target="_blank">📅 12:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24388">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رسانه های رژیم : بیژن مرتضوی به ایران بازگشت
@WarRoom
تکذیب کرد</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24388" target="_blank">📅 12:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24387">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">عراقچی : من جام خوبه نمیام ، مرسی اه @WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24387" target="_blank">📅 12:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24386">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سفیر آمریکا در اسرائیل : واشنگتن به‌زودی ساخت سفارت خود در اورشلیم را آغاز می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24386" target="_blank">📅 12:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24385">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b880b3de21.mp4?token=nAAOznrG7yiSoxgM-F-eOdRiznCw215x5MrwZCFcL4pXPyFE7pbGlQ7z9XKRye507XTlHXEs8vRYM9Xc8x5BlQw_z0CMB1Rmv6dM0ATzJ5O1Chw6kTFRuMYkeCrL0EreqiCRmzZIO1Gyqd2VytQaHJFrnFGLhiAp8aH7eEfc-_d77B2CE84iG9oE6JOrrEPJyq0iF7bmpFFC3pZN2u9arqoBoIDHBwiGgVjP_xsCU2NWdKkrAvYz81UL9dEDvKJcc8OXG19AYMYtkkA6XvBJztyO_tkrU6yDCE_Yy4gBvB1qE-p81ETVR6Sy9KWYAbGqfVPGUtBMmGLXR_Dbrx2mgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b880b3de21.mp4?token=nAAOznrG7yiSoxgM-F-eOdRiznCw215x5MrwZCFcL4pXPyFE7pbGlQ7z9XKRye507XTlHXEs8vRYM9Xc8x5BlQw_z0CMB1Rmv6dM0ATzJ5O1Chw6kTFRuMYkeCrL0EreqiCRmzZIO1Gyqd2VytQaHJFrnFGLhiAp8aH7eEfc-_d77B2CE84iG9oE6JOrrEPJyq0iF7bmpFFC3pZN2u9arqoBoIDHBwiGgVjP_xsCU2NWdKkrAvYz81UL9dEDvKJcc8OXG19AYMYtkkA6XvBJztyO_tkrU6yDCE_Yy4gBvB1qE-p81ETVR6Sy9KWYAbGqfVPGUtBMmGLXR_Dbrx2mgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحرکات نظامی امریکا در عمان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24385" target="_blank">📅 11:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24384">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رویترز : اسرائیل اعلام کرده پس از پرتاب یک
پهپاد انفجاری حزب‌الله
به سمت نیروهایش، مواضع حزب‌الله را در جنوب لبنان هدف قرار داده است.
حملات اسرائیل در مناطق مختلف جنوب لبنان از جمله
صور، نبطیه، مرجعیون و بنت جبیل
ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24384" target="_blank">📅 11:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24383">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ارتش اسرائیل اعلام کرده یک
تک‌تیرانداز حماس
را که به گفته ارتش در حال برنامه‌ریزی حملات بود، در جنوب غزه هدف قرار داده و کشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24383" target="_blank">📅 11:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24382">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رویترز:
ایران همچنان بر
طرح هفت‌روزه بازگشایی تنگه هرمز
پافشاری می‌کند و می‌گوید حاضر نیست شروط خود را کاهش دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24382" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24381">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نرخ دلار ۲۴۱،۰۰۰ تومان (رکورد تاریخی)
تتر  ۲۴۰،۰۰۰ تومان(رکورد تاریخی)
بیتکوین ۸۳،۱۵۸ $
انس جهانی طلا ۴،۱۶۳ $
نفت برنت ۹۸،۷۳$
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/24381" target="_blank">📅 10:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24380">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb747ba428.mp4?token=F4BQ6hz05TLw0BYGGmZJ-dN5fDfXifWk2vXj8ZfIVmxwxaQki5k2VcxJuozy9dzIPHb6coQ2xjQUckSFpJX3UFqXbTP0ue27cDJXqas46xC1LZqSyxaOLHOPt4TEnLwgDtQ-CVGEOZiJ2ZpKNWIMcoFg7BZwtsb4ASTL9p-_WOibzR63vFRQHqwSdJG-2zI6KiiDRdKXd9OXO54fGgdNTuY5RXmIzi3CTXT-l7oKID8xrMxnrSEr61_LnACsn6p-g2uTwthN2scq5ZAlw-7FoWmN52jg4DYTPe7O8QyBkbew5_Sta7DAnT9k9t_k92ZKpRM0wMYu1aIUjIT6Hu64uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb747ba428.mp4?token=F4BQ6hz05TLw0BYGGmZJ-dN5fDfXifWk2vXj8ZfIVmxwxaQki5k2VcxJuozy9dzIPHb6coQ2xjQUckSFpJX3UFqXbTP0ue27cDJXqas46xC1LZqSyxaOLHOPt4TEnLwgDtQ-CVGEOZiJ2ZpKNWIMcoFg7BZwtsb4ASTL9p-_WOibzR63vFRQHqwSdJG-2zI6KiiDRdKXd9OXO54fGgdNTuY5RXmIzi3CTXT-l7oKID8xrMxnrSEr61_LnACsn6p-g2uTwthN2scq5ZAlw-7FoWmN52jg4DYTPe7O8QyBkbew5_Sta7DAnT9k9t_k92ZKpRM0wMYu1aIUjIT6Hu64uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون پل ستار‌خان شیراز
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24380" target="_blank">📅 10:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24379">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007a727a10.webm?token=SkVknSoC1ZhjQocrk4aNTOw_mcddNHDkXYC2IHrVCL-8JgYEBRfcQC-FnS5-AMeq8T5KQdsi_Dqmg5ARhMsKfSXp08E9Hd8ouERTx1jeFuJFhNGn9EPLUDUQ39yL1tNNMtwAf6ropoWq92F7WCdO-IalzkinbOmc_ClhwSB1-pJt9Nkm56mI8RrdMLObuU5qKxMTUnH72abdJjPJL-cHkWSUDXH1-0im4-H79x6ZaSWjbsIz-QNnMzEhbYwv-lE97wCc6-VIfMlT9RtGN5jzCYCZ8qLhTGd-0Px63BqVL-__fnDbvZ8Dpj6AdHzr2OdSsug5vr856wTyqssf9GJAfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007a727a10.webm?token=SkVknSoC1ZhjQocrk4aNTOw_mcddNHDkXYC2IHrVCL-8JgYEBRfcQC-FnS5-AMeq8T5KQdsi_Dqmg5ARhMsKfSXp08E9Hd8ouERTx1jeFuJFhNGn9EPLUDUQ39yL1tNNMtwAf6ropoWq92F7WCdO-IalzkinbOmc_ClhwSB1-pJt9Nkm56mI8RrdMLObuU5qKxMTUnH72abdJjPJL-cHkWSUDXH1-0im4-H79x6ZaSWjbsIz-QNnMzEhbYwv-lE97wCc6-VIfMlT9RtGN5jzCYCZ8qLhTGd-0Px63BqVL-__fnDbvZ8Dpj6AdHzr2OdSsug5vr856wTyqssf9GJAfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24379" target="_blank">📅 10:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24378">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e1529c155.mp4?token=Hf0jEEK5jO_1wRXy4FFicyijkWmeMDyrMyG4QlO0jjJCIsUPLEOsXSshIt34B81IgaqK-wYs0twr5ZULBnOP-bamyYkIELzr_5EsdcZWHIPvKG0qJHdnpeNHq3unUu-6HEenlOPwfdbqSuiulj--_VbQVkJIwVp25IW1wXF0VM4jic_qwwUGlGGbnuAEGmuwmZ_A7sEYQ506DlKWcRJ4a83infTXa7kZW4iQ6DqCCLKU1rYleWhCNgxuu4LdJy0vY3efNMAn2nQUsKeS5kAhH-Yd-HMk6zVHvwTn0hnvNV7O_EmZCmq5MyfakCBvmgbogv-leyq5CxXU1dLYrfSXSwv_hN5bq-CdlJs6jM3ZNuhFV40PNGs0XXJhrFBLsbu3A4XBFrcJAIvGHrllCsUEh6NCdIeCio_zfSGUHfNhY1SGOv0R8ERFlcYACsh0v3YjhN0Yfx1dDlUhpKHMuiFLXdKw44qLgFLPx3kN3pYzOkSm1ixNtOaAzjihmyqBdIqtVTyiH7N-cVVwF9IGRrANHUQkwM8IEWAirmU8wcYQq2CFfpH6L4p7953ObDSFqzPgP6PsbGYuatw0xb2h2MvW7INNDOXXrOW0MY_oNbMux8vY21hiuXfp87dtwOQLxvKvM_a-Igp96VIUXkE0kj_0N74swjXeXFSohgnQ7Dpa180" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e1529c155.mp4?token=Hf0jEEK5jO_1wRXy4FFicyijkWmeMDyrMyG4QlO0jjJCIsUPLEOsXSshIt34B81IgaqK-wYs0twr5ZULBnOP-bamyYkIELzr_5EsdcZWHIPvKG0qJHdnpeNHq3unUu-6HEenlOPwfdbqSuiulj--_VbQVkJIwVp25IW1wXF0VM4jic_qwwUGlGGbnuAEGmuwmZ_A7sEYQ506DlKWcRJ4a83infTXa7kZW4iQ6DqCCLKU1rYleWhCNgxuu4LdJy0vY3efNMAn2nQUsKeS5kAhH-Yd-HMk6zVHvwTn0hnvNV7O_EmZCmq5MyfakCBvmgbogv-leyq5CxXU1dLYrfSXSwv_hN5bq-CdlJs6jM3ZNuhFV40PNGs0XXJhrFBLsbu3A4XBFrcJAIvGHrllCsUEh6NCdIeCio_zfSGUHfNhY1SGOv0R8ERFlcYACsh0v3YjhN0Yfx1dDlUhpKHMuiFLXdKw44qLgFLPx3kN3pYzOkSm1ixNtOaAzjihmyqBdIqtVTyiH7N-cVVwF9IGRrANHUQkwM8IEWAirmU8wcYQq2CFfpH6L4p7953ObDSFqzPgP6PsbGYuatw0xb2h2MvW7INNDOXXrOW0MY_oNbMux8vY21hiuXfp87dtwOQLxvKvM_a-Igp96VIUXkE0kj_0N74swjXeXFSohgnQ7Dpa180" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
به‌جز نفت، که قیمت آن از دوران دولت بایدن پایین‌تر است، دیگر لازم نیست نگران سلاح‌های هسته‌ای ایران باشیم، چون آنها کاملاً نابود شده‌اند.
اما به‌جز نفت، قیمت همه‌چیز در حال کاهش است و روند کاهش ادامه دارد. ما بدترین تورم تاریخ کشورمان را به ارث بردیم، اما تورم اکنون به‌سرعت در حال کاهش است. کشورمان وضعیت بسیار خوبی دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24378" target="_blank">📅 05:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24377">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4e4b6efa2.mp4?token=UUm_bTiH4Jt_V7SZ0Z7Xkid3c97E95mKjsNapIuzeWH5hgQYirTe5JlCg1xcezKwr4gt9jMZUABq9VE6ZVCHen2sN06Y-b1aHgqbFOhX2hu8jmW_U1EiyUdFAXzm-uMO-P8crvaELOYFZmFAgNXuMnsNNhQss8kKzDvTllJMFAYR6I_bKz3p_562ngCLFjd3DXz35erNhJKZmji5Hf5hUjdy6FZkpcrj11eSZf6kDEarbors7H_7hahyUWb1OCiDCJVHdXT7BIOe57paG0_cTFRJ9WdLp-Yj6nfekmWiN_56S_ZtV3p80Ih0PICDvx9eRW6s-fbYOZcWnsYZCUyhVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4e4b6efa2.mp4?token=UUm_bTiH4Jt_V7SZ0Z7Xkid3c97E95mKjsNapIuzeWH5hgQYirTe5JlCg1xcezKwr4gt9jMZUABq9VE6ZVCHen2sN06Y-b1aHgqbFOhX2hu8jmW_U1EiyUdFAXzm-uMO-P8crvaELOYFZmFAgNXuMnsNNhQss8kKzDvTllJMFAYR6I_bKz3p_562ngCLFjd3DXz35erNhJKZmji5Hf5hUjdy6FZkpcrj11eSZf6kDEarbors7H_7hahyUWb1OCiDCJVHdXT7BIOe57paG0_cTFRJ9WdLp-Yj6nfekmWiN_56S_ZtV3p80Ih0PICDvx9eRW6s-fbYOZcWnsYZCUyhVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
می‌توانید درباره حملاتی که در بریتانیا رخ داده و مظنون مهاجری که در این ارتباط بازداشت شده، اطلاعات بیشتری بدهید؟ آیا ارتباطی با ایران وجود دارد؟
دونالد ترامپ:
ما همه چیز را درباره او می‌دانیم و به‌زودی اطلاعات بیشتری درباره این موضوع خواهید شنید.
ما آنها را گرفتیم.
@WarRoom
یاشار ، تکمیلی: تمام رسانه های جهان به اتفاق میگن کاره ایران بوده حتمأ سر نخ های پیدا شده و  عملیات توسط یک زن کشاورز که به ۳ ون مشکوک میشه و گزارش میکنه لو میره</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24377" target="_blank">📅 05:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24376">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74dac714cd.mp4?token=G7-2f5jET3nCgsKGY5tTp8Hq6OMngViw0gYhCzFdor5OUlF4_qr6KPo8rwAJirHJZPGVzDICsnsZa6Ir3V8objE_xF78VVoAGrlqG6uSSMiRSHSRraNTRTtQ7LsOS1uREauNAtX6his8OY0M_O_z422yxxP8BHI-8luVa3CMOQ17x9DXNRFnmdFW-b9k2dEXHwsTGyvFO_859eefEqtaMyiQRTjAW70vVl2mPRF4HMu9CDdbirWBcsLqkWaJFuwpyELG_5w2WXceZTr7EW5k90iQU1jkp3m3bli7nwAUwwVbY82fiepFEe7-6VPAhPeSxkDjVtwBFXEkbubpBfIaSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74dac714cd.mp4?token=G7-2f5jET3nCgsKGY5tTp8Hq6OMngViw0gYhCzFdor5OUlF4_qr6KPo8rwAJirHJZPGVzDICsnsZa6Ir3V8objE_xF78VVoAGrlqG6uSSMiRSHSRraNTRTtQ7LsOS1uREauNAtX6his8OY0M_O_z422yxxP8BHI-8luVa3CMOQ17x9DXNRFnmdFW-b9k2dEXHwsTGyvFO_859eefEqtaMyiQRTjAW70vVl2mPRF4HMu9CDdbirWBcsLqkWaJFuwpyELG_5w2WXceZTr7EW5k90iQU1jkp3m3bli7nwAUwwVbY82fiepFEe7-6VPAhPeSxkDjVtwBFXEkbubpBfIaSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ژنرال جک کین به مارک لوین در فاکس نیوز:
آمریکا و اسرائیل همین حالا
توان هوایی لازم برای تغییر چشمگیر روند درگیری در داخل ایران
را در اختیار دارند.
او پیشنهاد می‌کند معترضان ایرانی علیه
مراکز سپاه پاسداران
دست به اقدام مسلحانه بزنند و همزمان هواپیماهای آمریکایی و اسرائیلی نیز از آسمان از آنها پشتیبانی کرده و
نیروهای کمکی حکومت
را هدف قرار دهند. او می‌گوید: «
ما داریم این کار را سخت‌تر از چیزی که هست می‌کنیم.
»
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24376" target="_blank">📅 04:49 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
