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
<img src="https://cdn4.telesco.pe/file/eGCcVIhc5idjFcTHcrG7wHZ0E2jMGu3CZrrrg8XRiRSciVrF66qW6WlSo3AXQ_j_zHm0OXv8uBhDI69T2cQmpRETezG7DoN1b9edTKAMHyS5gLcwSUj4l6yVSc3gdkv9pvYMCaPNXySRXajpHGti6dipebq93ksMG8cyIy69C3RctMuAoLhBCaFdw898yYaOFVN3_d1RI0lXErO-MsD6qOOOgZ5u_RT74ZQhoqRW5DGGRXpmy_Bwlu1IvE3dVJYUoXGOkCl18g6ID8-wSSuoNQ1rxfx4-sCwZIqyg9iCORQb6FV_Ehh7zoMJleA8-Ykx21Yce0SP3VKHi0OUoyaACQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 444K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 07:35:43</div>
<hr>

<div class="tg-post" id="msg-21026">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">عراقچی می‌گوید اساساً چیزی به نام
«آتش‌بس ۶۰روزه برای تمدید
بعد از نقض آن توسط آمریکا
وجود ندارد»
و تفاهم اسلام‌آباد از نگاه ایران
پایان جنگ بوده، نه آتش‌بس ۶۰روزه
. با این حال، اگر مبنا را همان دوره ۶۰روزه و پایان آن در
۱۷ اوت
بگیریم، با فرض ساعت ۰۰:۰۰ واشنگتن، موعد پایان آن در ایران
ساعت ۷:۳۰ صبح ؛ یکشنبه
(اگر مبنا آغاز روز) و
دوشنبه ۲۶ مرداد
(اگر مبنا پایان روز) باشد پایان میابد
@WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/21026" target="_blank">📅 23:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21025">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قطر ادعای ایران دربارهٔ به اسارت گرفته شدن سه خلبان ایرانی توسط این کشور را قاطعانه تکذیب کرد
و گفت تهران تاکنون به دعوت دوحه برای اعزام هیئتی به قطر و بررسی جزئیات عملیات جست‌وجو و نجات پاسخ نداده است.
سوخو-۲۴ ایران روز ۱۱ اسفند ۱۴۰۴ برای انجام مأموریتی علیه یک پایگاه نظامی در قطر اعزام شدند و هنگام بازگشت هدف پدافند قرار گرفتند.
بر اساس روایت ایران، چهار خلبان این دو جنگنده اجکت کردند که یکی از آن‌ها، مجید کاظمی، کشته شد و سه نفر دیگر به نام‌های جواد صالحی، عبدالمجید دشتیان و عمران به‌روشیان «زنده توسط نیروهای قطری به اسارت گرفته شدند».
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21025" target="_blank">📅 22:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21024">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دیدبان اتاق جنگ : سیریک هرشب قبل اینکه بزنن یک ساعت برق قطع میکنن بعد که وصل کردن شروع میکنن شلیک
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21024" target="_blank">📅 22:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21023">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گزارش صدای ۳ انفجار/شلیک در‌ سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21023" target="_blank">📅 22:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21022">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏دونالد ترامپ در تروث‌سوشال ویدیویی را منتشر کرد که در آن بهنام طالب‌لو، مدیر ارشد برنامه ایران در بنیاد دفاع از دموکراسی‌ها، بر تاثیر محاصره دریایی آمریکا در کاهش صادرات نفت ایران تاکید کرده و می‌گوید محدود کردن حکومت ایران از نظر بودجه‌ای پس از پایان درگیری‌ها، در کنار محاصره، به آمریکا اجازه می‌دهد از دلار به‌عنوان یک سلاح استفاده کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21022" target="_blank">📅 22:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21021">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21021" target="_blank">📅 21:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21020">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اندی بیکر، یکی از نزدیک‌ترین چهره‌های امنیتی به جی‌دی ونس، در هفته‌های آینده کاخ سفید را ترک می‌کند.
بیکر که سال‌ها مشاور امنیت ملی ونس بوده و در دولت ترامپ نیز در تصمیم‌گیری‌های مهم سیاست خارجی و امنیت ملی نقش داشته،
مستقیماً در مذاکرات آمریکا و ایران حضور داشت
و به جناح مخالف جنگ شناخته می‌شد.  خروج او در حالی رخ می‌دهد که جنگ ایران همچنان موضوعی حساس است؛ هرچند دلیل رسمی برای رفتنش، تمایل به وقت بیشتر با خانواده و سرمایه گزاری های شخصی عنوان شده ، همچنین
در مورد شایعه افشای اطلاعات محرمانه نیز اتهام مستندی علیه بیکر منتشر نشده، اما با توجه به دسترسی او به پرونده‌های حساس و نقش مستقیمش در مذاکرات، این گمانه‌زنی درباره علت واقعی خروجش مطرح شده است
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21020" target="_blank">📅 19:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21019">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مارک لوین : من قویاً معتقدم که پرزیدنت ترامپ باید از نتانیاهو حمایت کند، چون در مقطعی برای ادامه مقابله با ایران به او نیاز خواهد داشت. به احتمال زیاد، نتانیاهو در هر صورت پیروز خواهد شد. اما بر اساس اطلاعات منابع من، در دیدار آنها هیچ توطئه یا زدوبندی در کار نبوده است. آکسیوس این گزارش‌های منفی را با هدف تأثیرگذاری بر سیاست‌گذاری و انتخابات اسرائیل، از دیدگاهی چپ‌گرایانه و افراطی، در زمان‌بندی خاصی منتشر می‌کند.
همچنین نتانیاهو بر اساس آخرین نظرسنجی‌ای که در انتخابات قبلی واقعاً نتیجه را درست پیش‌بینی کرده بود، وضعیت خوبی دارد. آن نظرسنجی را پیدا می‌کنم و جداگانه منتشر خواهم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21019" target="_blank">📅 19:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21018">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بیانیه دفتر نتانیاهو : امروز صبح، حزب‌الله توافق آتش‌بس در لبنان را نقض کرد، زمانی که به سربازان ما در منطقه امنیتی که از شهرک‌های اسرائیلی واقع در نزدیکی مرز محافظت می‌کند، حمله کرد. در این حمله، سه تن از سربازان ما به شدت مجروح شدند. ارتش اسرائیل با بمباران مقر فرماندهی حزب‌الله که دستور حمله را صادر کرده بود، پاسخ داد
…
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21018" target="_blank">📅 18:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21017">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">واشنگتن پست : هیچ توافق خوب و قابل‌قبولی با ایران نمی‌توان منعقد کرد!
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21017" target="_blank">📅 17:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21016">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اردوغان به شبکه الجزیره: اولویت ما بازگشایی تنگه هرمز است، زیرا ادامه بسته بودن آن به نفع هیچ‌کس نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21016" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21015">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ستاد کل نیروهای مسلح ایران اعلام کرده است سه خلبان ایرانی به نام‌های
جواد صالحی، عبدالمجید دشتیان و عمران به‌روشیان
که در جریان حملات اسفندماه جنگنده‌های سوخو-۲۴ آنها سقوط کرده، زنده مانده و حدود شش ماه است در
قطر به اسارت نیروهای قطری
درآمده‌اند. محمد باقرزاده، فرمانده کمیته جست‌وجوی مفقودین، گفته این خلبانان هنگام بازگشت از یک مأموریت رزمی پس از هدف قرار گرفتن جنگنده‌ها توسط پدافند، اجکت کرده‌اند. او با استناد به کنوانسیون سوم ژنو خواستار دسترسی کمیته بین‌المللی صلیب سرخ به آنها شده و گفته قطر تاکنون اجازه تماس یا دیدار خلبانان با خانواده‌ها و مقام‌های ایرانی را نداده است.
قطر تاکنون به این ادعا واکنش رسمی نشان نداده است
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21015" target="_blank">📅 16:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21014">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8PDtk261_wBo-N8BXJMrk5zfKHN44-00yQvooYsIaS6rf1Wt5lZF0ulaeBkWOlvZ7Z9ED3BJNy9uWxtB2KFIGnxUspLgIRIKLB167Lod_mhK-XdcLxBbski49QHau0jeVEm_ESwsJueTLZX7DEtXCAZu1SAamuanOJy7vS2Xn5pauwWpqxATm_BU3I6bKV6v36PmkcZ0Ra8gH3UdJXhuxHCcNszrlYjQu8nf_RILb-DNoxz1OL1JCGov4hY7WLNuc9p9RoxeYtarDn-5eRm-CBQDZG-F9OCYTcefwJi6TgfUBuia3wXCJjosvK-0du1GzJSXkYU846GW1HPtg402w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : اندازه هواپیما هایی که ما در اتاق جنگ زیاد سروکار داریم
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21014" target="_blank">📅 15:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21013">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21013" target="_blank">📅 14:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21012">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبرنگار الجزیره: ۳ حمله هوایی اسرائیل بامداد امروز، مناطق اطراف شهر النبطیه الفوقا و حومه شهر انصار در منطقه النبطیه را هدف قرار داد. @WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21012" target="_blank">📅 12:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21011">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKnmYm7G1La0rFvKjC-efuh_o1To-1kwsHIJ-jCZFqalVGGwP1oHOFgqFRxR3HApwkcCLDicikkCbB4gmmUNEGcRkwroamesWKXzMGWMFq2Uk45-UC5m8N3qYsws84GxF6bXLqCJVjujXZoJYxVXxWdbVW9I6GrgeS5wxBI00ruETKnpgsZzhMfu5QsP3WCDgVJNWquUuqNh_zg62wDI_xJ-l5pBwllnLIM7mh7b5u29XtE0JzOkrJhn_HfAgTRNAbNdoMo7mkLAYEuMoM9xP0Nn0zDfY0K2onpREUvNhghhF_8Htz_BP8FbgxW4EE-5PZk69-xMDQvotm2IUWp3Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : دیوار فولادی، محاصره
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21011" target="_blank">📅 11:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21010">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFzEjA_J7lPQXbFyotLq7Gwvnsy8HK-LeiYRWbCMoHxKUKxYk_-jPbQ17DoCUtorLI3FcEpDIu2wuarg9_lDHCT-rb2c4BIbnK8QNQG3GqNVGwiGCjb603wHPcSDNpJM1ambiI_flCgQCUK2pXjUr9aIQo16ellOfG_ERonkE8ivWosMnRy_dcJfUzRNO9YaKM04jJlUMGq6U1YGc1CLVfo18RoKF5o-K5XNKNcxrLpwlnulPymr0lnXalIe7Z05oWA4HeqRSUGobVXjnj5hQ6CycHes0z4uiZQlW5qcKprKeLXO8qDdYx4mN7B3V8FY0-_17c_laIbYX4POqrUJtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۲ : تصاویر ماهواره‌ای منتشر شده توسط رویترز: دو لکه نفتی در نزدیکی جزایر قشم و سیری ایران در خلیج فارس مشاهده شد، در حالی که حملات مکرر به کشتی‌ها در این منطقه ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21010" target="_blank">📅 11:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21009">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مستند دیدنی
«جاسوس ۲»
از کانال ۱۴ اسرائیل ، که در آن با مأموران سپاه مصاحبه میشود !
با زیرنویس فارسی
، پیش تر قسمت اول را برای شما قرار داده بودم… از دست ندید…
🌐
@WarRoom
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21009" target="_blank">📅 11:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21008">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7Pp1tfGgqRKfFX0vxdwsUcFBZjJePniOvjU7mTLhfotOgyxN2xcYq6KCyPSSxnqO8AsZLNnID4WhszhKI7j4MEV_TQCqVUSqGrF9fW7-Ube2IA77k3ykhvHdXurN-rTsf0R4ma2-LkzVDfeZuHF272ukyZQRLBHtKHi4ORWSNEIuPNfkcBulHEbLUv5eknyhKh2ZvCIT5Y-omWijwK3-0Rg8Uv5ssPIGBE988AI5xHExipX8G-6hYKcmIP0bzAg_kOMioTgOc9px_l-qgPt6BLuJm2Zgq-MPOgZ8MQA7FBPXjXa8_baesRKO19Bx6q1PDr9wEsdeB8u2Gv4uvFoqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : خط جدید ترابری لاجستیکی نظامی آمریکا و کد عملیات «مووسی MOOSE» نشان میدهد در جنگ بعدی پایان دهنده کار، آمریکا بر روی پایگاه خود در قاهره حسابی ویژه ای باز کرده و مرکز پشتیبانی عملیات خواهد بود هم نزدیکی به منطقه هم فاصله دورتری نسبت به کشورهای حاشیه خلیج فارس…
سفر قاهره تازه شروع شده…
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21008" target="_blank">📅 10:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21007">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خبرنگار الجزیره: ۳ حمله هوایی اسرائیل بامداد امروز، مناطق اطراف شهر النبطیه الفوقا و حومه شهر انصار در منطقه النبطیه را هدف قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21007" target="_blank">📅 10:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21006">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-mmll4d4qs6u8woeRNAtk35ZKaYT8KxCTsb-eaKuzb9OGA00xYyKClT0F4yqMZitOj1E_fTyG5BLfqYtZ0UkpbIURFHjWjrYlBolgV6y5uMFcXWyI7IKV5rfLPO6u9IFIsCFckpK6MA8gupooUfDUVf_dTERueWn_eC5xtAQ0RlPftX4smRwTY3S5PXk_qNbUIiyC00nvVnDxFZZTETpzaL9Pjq6WelX40WYWYIomJS3RBx17-sKj-obTowM_t21nHaqpH6Ua8O2U9oFHY9BNP2jOZP1sheg_pcU8-sW3eduyS1WBEbFa1nXKqItxGbGns4k6DeIGPu74GIBWGKXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏UKMTO گزارش تأیید شده‌ای مبنی بر برخورد یک پرتابه ناشناخته به بدنه یک کشتی فله‌بر دریافت کرده است. خدمه در سلامت گزارش شده‌اند، هیچ ارزیابی خسارتی گزارش نشده است و در حال حاضر تأثیر زیست‌محیطی آن مشخص نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21006" target="_blank">📅 09:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21005">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ادعای نیویورک‌تایمز: مشکل تأمین و تدارکات ناو آبراهام لینکلن پس از آن آغاز شد که ایران، به پایگاه نیروی دریایی آمریکا در بحرین آسیب شدیدی وارد کرد و یک مرکز لجستیکی مهم را از کار انداخت
سپس پنتاگون مرکز تأمین و پشتیبانی منطقه‌ای خود را به دیه‌گو گارسیا منتقل کرد که ۳۵۴۰ کیلومتر از ناو‌های آمریکایی فعال در دریای عمان، فاصله دارد
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21005" target="_blank">📅 09:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21004">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYJPLY2_8JqnId7GHQYu0B5DZYGrt370Q2Muqf5LOJjZyRKhskIGp7Y2q1LiTHR6DDlIQVzJvNIKlVTjpaZsb6HsbHZ52gF4nPGhyPMRuhoUIJKbZm5wDK5fA9taTIflkwXAXcqEKIRCM8_NslEdYfpr5NRLcTmCmq6h2GY6_MKW146C13krdv6JxVadXt9W9akTdTPIBsBox6OG7oLHau_wqFz2kj-z4eVPGrjvfrE9LRp0KmTaFX-mGKC07g-BehrnMeSB8bNRN8H1VMGe2NjR4PMIHbHjOvQy1mB-4knQcCqgoLjQb25tW-MpRF8F42MvNL7n_WXa701B1r2ScA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس نیوز : آقای معاون رئیس‌جمهور، یک لحظه به توافق نزدیک هستیم، لحظه بعد می‌گوییم قرار است حسابی آنها را بمباران کنیم. یک لحظه تنگه هرمز باز است، لحظه بعد بسته است. مطمئنم این نگرانی و سرخوردگی داخل کاخ سفید هم وجود دارد. می‌دانم پیش‌بینی کردن دشوار است،…</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21004" target="_blank">📅 03:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21003">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ در مورد ایران: به زودی تنگه هرمز را جزو قلمرو ایالات متحده اعلام خواهم کرد.  ایران به شدت شکست خورده است. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21003" target="_blank">📅 03:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21002">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sH1LRbA3vEvy2XK82WKqv-6WTvR4KHXSLQI7le2uwQiUFLpAJMdKIPBlDHnBb3P7zUZ2TWDsVk1wavyG-JJPScRoef79uODNmMbuRjeWWaE_rcCQnG_pbQCT9nW5mpEl_Q561WR_Y7qJpTjwqDx2qI7psnJ7Oc7ccyLEJ3RZBEZjVUcqWe23J5kYBWvMQDgaxTkt-Z-8ZFoFKDgOvwvvXWaw8s1Hx6twtm_hRQQ2E9IgBepd0lqT_CogIoTbK0KYWCx3qSR37468r-o_Xv-a5pM_SCFgfLDpTM59jIuDoBO0xr-RsFqKmB1q3Ty7fk9QePc24HEKSluFwYcPkSmvjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهار هواپیمای C130 سوپر هرکولس از آمریکا به انگلستان و یک C5Mسوپر گالاکسی، یک راست از آمریکا به خاورمیانه میآیند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21002" target="_blank">📅 02:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21001">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وقوع زمین‌لرزه ۷.۴ ریشتری در اندونزی!
دو زمین‌لرزه جدید با قدرت های ۶.۱ و ۶.۶ ریشتر نیز دقایقی بعد رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21001" target="_blank">📅 02:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21000">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvxmYFqsbKchMVCvP8jytaoSoDKker2bi2ChvkI64TeXKvm6rpkugOF4Dwzwm8lccW-ckXVUp3xXWVyEcDkV7koodTXEspLFjTT5yTvs9LouM2m8vHKb4vlbXVgpm3hmTy4w3j7g7sUmRpSIKxn92prfez9J6zzsgwVLQy1j_ecxFQG3d3XjALeYc1crOxW0jm8a9GEmhnOKE07vHa6fc8DV6XS0VV0mC_GtEOszOKNa44hLBfUJU4Z8x7tFQn8zfXlUjHr8MVAmOrUz0LGCS5FFjsTMlWFteQXjMMNws0ZJxozrgPdmuAADcPU6gsqvGMgGfO_eLgT3Bzp-o23dig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای هشدار زودهنگام E3B-Sentry با رادار AWACS هم راه با ۴ سوخترسان هم اکنون در منطقه خلیج فارس انجام مأموریت میکنند
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21000" target="_blank">📅 01:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20999">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">@WarRoom
مسیر من</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20999" target="_blank">📅 01:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20998">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from………..</strong></div>
<div class="tg-text">درود یاشار
شما بیشتر خرف های جاوید نام روح الله زم رو بیشتر قبول دارین یا استاد مانوک خدایخشیان؟
ممنون میشم جواب بدی</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20998" target="_blank">📅 01:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20997">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">@WarRoom
مسیر ما</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20997" target="_blank">📅 01:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20996">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">@WarRoom
مقدمه</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20996" target="_blank">📅 00:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20995">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ: تمام کشورهای منطقه در شرایطی شبیه به محاصره قرار دارند، زیرا ایران به عنوان یک کشور زورگو در خاورمیانه شناخته می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20995" target="_blank">📅 00:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20994">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d76eba2226.mp4?token=Ofbpbh_O49I86p8a30_cZkmIIQ_VAeO0kt-plpxTumKL6KkqUgmPyJGCUvSt2Xif67WbpzQRtwtuiTL64FW_Dk4xtuAcJMMLCeqyDYDH4cLu1TDiWrLbziP5tKBuXUZPtcOBy4nR_xv8_dShhk2J-bcg9Kfyj0XdnaZDgFPhb8OtAr1SoT_CsIPYdeJv6gMU1uTjftgVqcMpnzXzLnx45f9rrO3m_Y84aTDTKm7KH_detR3KtXiR_jU9qgiqVF3bjt0ihckA0Oi4RUZrLDgGfmYk1-pvyahTD2UNATkIFtuzkQ80CzNiIpSec2UxyXKroQOwxEC6-LRBLeUCAYMZ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d76eba2226.mp4?token=Ofbpbh_O49I86p8a30_cZkmIIQ_VAeO0kt-plpxTumKL6KkqUgmPyJGCUvSt2Xif67WbpzQRtwtuiTL64FW_Dk4xtuAcJMMLCeqyDYDH4cLu1TDiWrLbziP5tKBuXUZPtcOBy4nR_xv8_dShhk2J-bcg9Kfyj0XdnaZDgFPhb8OtAr1SoT_CsIPYdeJv6gMU1uTjftgVqcMpnzXzLnx45f9rrO3m_Y84aTDTKm7KH_detR3KtXiR_jU9qgiqVF3bjt0ihckA0Oi4RUZrLDgGfmYk1-pvyahTD2UNATkIFtuzkQ80CzNiIpSec2UxyXKroQOwxEC6-LRBLeUCAYMZ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20994" target="_blank">📅 00:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20993">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZ4R9a6AkVAXaofXe86McPR-tX9QZEr1WcupmIormq7TZRQ0pmZedCJTSD0hl6MCQ2z-LaAn0CRyuJ675tQu0N_ezH0eS3mAC8bTriMCb4EYJo8jZFJRWCxxiY70v8buospQFJBJ70dltLoDXv1A751Cm_uHvDIDMhSvMxxqhy472K0lDcdY7_qBj8g-90_5a0R9HvpAquWQ8HAJuMfMWf8coOg9LESURDteuUbWXzGTAgfjvnbVykqhqPtUjJXEaTI2sG1pFSLwQYE5SgQ8U5gK5zGTThwzvzMDxLapj3zoaeoMJP9H4NeJEizGbrOX7bGAvKcQgh9vDnAqiQz3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگست در اتاق جنگ  در حال شنیدن گزارش نیروهای مستقر در خط مقدم فرماندهی مرکزی آمریکا (سنتکام) در حوزه‌های هوایی، زمینی و دریایی، از جمله ناو هواپیمابر
USS Abraham Lincoln
، هستم.آمریکایی‌های شگفت‌انگیزی که در حال انجام یک مأموریت تاریخی هستند.
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20993" target="_blank">📅 00:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20992">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e4825bc3.mp4?token=vBXEMCLyXK49lBzUTJZvZeAF0jbt4Wvt3M-OIrZUnBealCDC1Xw4jA_cZf5ypalyQmEYTLrKyPEUPrboOJoRFjfFIxT0lRxhQvb8zsUsvk806TxFmVNjbNMQNWdxR-3SP6PHb18cIVt6ew4JQJCHam7repwMDGZWqdkL6Xem1L_0yiNxtyXbPKvL81ftRi_RT9QLzGCxBdYOaefFYyDAKdzklKVZGjOOy7VtTw5zFFk5KMmdei9aq4aABXv8SAhcr7zvI7sRcsX4uDypmbFaRmEc4S0t2xocJmf31auVYLCVMrJsvCY1s4dxEu81HTj6zh7U0d79AsFwg0eTft0YuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e4825bc3.mp4?token=vBXEMCLyXK49lBzUTJZvZeAF0jbt4Wvt3M-OIrZUnBealCDC1Xw4jA_cZf5ypalyQmEYTLrKyPEUPrboOJoRFjfFIxT0lRxhQvb8zsUsvk806TxFmVNjbNMQNWdxR-3SP6PHb18cIVt6ew4JQJCHam7repwMDGZWqdkL6Xem1L_0yiNxtyXbPKvL81ftRi_RT9QLzGCxBdYOaefFYyDAKdzklKVZGjOOy7VtTw5zFFk5KMmdei9aq4aABXv8SAhcr7zvI7sRcsX4uDypmbFaRmEc4S0t2xocJmf31auVYLCVMrJsvCY1s4dxEu81HTj6zh7U0d79AsFwg0eTft0YuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
ما قادر به نابودی کل کشور هستیم. ما نمی‌خواهیم این کار را انجام دهیم.
ما تحریم‌های اقتصادی علیه آنها داریم که هیچ کس قبلاً نداشته است.
اگر آنها حمله کنند، ما ۱۰۰ برابر سخت‌تر پاسخ خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20992" target="_blank">📅 00:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20991">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ: ایران همچنان موشک‌هایی دارد، اما این بخش کوچکی از موشک‌هایی است که قبلاً در اختیارش بود.
تولید موشک‌ها در ایران 82 درصد کاهش یافته و توانایی‌های تولیدی آن‌ها تا حد زیادی از بین رفته است.
نرخ تورم در ایران به 350 درصد رسیده و ارزش پول آنها هیچ است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20991" target="_blank">📅 00:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20990">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ: آن‌ها رهبری ندارند. ما رده‌های اول، دوم و سوم آن‌ها را از بین برده‌ایم. این یکی از مشکلات من است، زیرا کسی وجود ندارد که بتوان با او مذاکره کرد.
ما رادارها و تمام تجهیزات اطلاعاتی پیشرفته و مدرن ایران را نابود کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20990" target="_blank">📅 00:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20989">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ در مورد ایران:
آنها ۲۱۲ هواپیمای بسیار خوب داشتند که برخی از آنها به طرز درخشانی از طریق اوباما از ایالات متحده خریداری شده بودند.
همه هواپیماهای آنها از بین رفته‌اند.
یکی از مشکلات ایران این است که کسی برای مذاکره وجود ندارد. این یک مشکل است.
این تنها کشور در جهان است که هیچ کس نمی‌خواهد رئیس جمهور شود.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20989" target="_blank">📅 23:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20988">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ: هیچ کس نمی‌داند که ما در ایران تا چه حد موفق بوده‌ایم.
می‌دانید چه کسی می‌داند که ما در ایران تا چه حد موفق بوده‌ایم؟ خود ایران.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20988" target="_blank">📅 23:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20987">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ : به همکارانم گفتم: «ما باید سفری به خاورمیانه داشته باشیم، زیرا باید از یک فاجعه بالقوه، یک آتش بسیار بزرگ که مثل آن را قبلاً ندیده‌اید، جلوگیری کنیم.»
وقتی مجبورید برای بنزین خود کمی بیشتر هزینه کنید، من هرگز عذرخواهی نخواهم کرد. من کار درستی انجام دادم.
یک کشور بسیار بد، نباید سلاح هسته‌ای داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20987" target="_blank">📅 23:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20986">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ درباره ایران:
جنگ با ایران، خدمت بزرگی به جهان است و ما کار فوق‌العاده‌ای انجام می‌دهیم.
من هرگز عذرخواهی نخواهم کرد، من کار درستی انجام میدهم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20986" target="_blank">📅 23:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20985">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ: اگر ایران به ما حمله کند، ما با صد برابر قدرت بیشتر پاسخ خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20985" target="_blank">📅 23:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20984">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ: ما نمی‌توانیم اجازه دهیم که ایران به مسیر فعلی خود ادامه دهد. اگر ما آن‌ها را با بمب‌افکن‌های B-2 مورد حمله قرار نمی‌دادیم، آن‌ها سلاح هسته‌ای به دست می‌آوردند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20984" target="_blank">📅 23:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20983">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ درباره ایران: من هرگز عذرخواهی نخواهم کرد، من کار درستی انجام دادم.
ایران، بدترین حامی تروریسم در جهان است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20983" target="_blank">📅 23:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20982">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ در مورد ایران: آمریکا قرار است زین پس هزینه بسیار کمی برای بنزین بپردازد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20982" target="_blank">📅 23:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20981">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ درباره ایران: محاصره اقتصادی، دیواری فولادی است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20981" target="_blank">📅 23:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20980">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acb3349271.mp4?token=wBljB5Z_wazM3dKElYZDzEpB2qRwiI9fYBqQY8hi8rXKz687vP0axbV-mEiOK7UlXO1uy7sf_QciG70os8e7sV1IsV6FlPxiEWO2414nu0tm0axiHlyKUu5F3D4Cy8TMVSwMoLjdowin_M17NmvL47M5LMJVI2b2jey-FV3tqYhC6dqBqWxwh-s2A2hgn6WQsAjHjDIBsDcOJTyNPpp7XwcZI8VzD1sv9719FGwsv7q0l0CxGqVgQniPpoVwV0MjyOH2AZ3ZFGkj3eQ1krsoVKJgUPQDUky9_zNn3BrYOwlC1Z5YdMimajCYho-NvdflOqVgNYRpy817I6xdE2e8ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acb3349271.mp4?token=wBljB5Z_wazM3dKElYZDzEpB2qRwiI9fYBqQY8hi8rXKz687vP0axbV-mEiOK7UlXO1uy7sf_QciG70os8e7sV1IsV6FlPxiEWO2414nu0tm0axiHlyKUu5F3D4Cy8TMVSwMoLjdowin_M17NmvL47M5LMJVI2b2jey-FV3tqYhC6dqBqWxwh-s2A2hgn6WQsAjHjDIBsDcOJTyNPpp7XwcZI8VzD1sv9719FGwsv7q0l0CxGqVgQniPpoVwV0MjyOH2AZ3ZFGkj3eQ1krsoVKJgUPQDUky9_zNn3BrYOwlC1Z5YdMimajCYho-NvdflOqVgNYRpy817I6xdE2e8ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران: به زودی تنگه هرمز را جزو قلمرو ایالات متحده اعلام خواهم کرد.
ایران به شدت شکست خورده است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20980" target="_blank">📅 23:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20979">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">لحظاتی پیش حمله هوایی اسرائیل به المنصوری در جنوب لبنان انجام شد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20979" target="_blank">📅 23:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20978">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کاخ سفید: به مجازات ایران و فلج کردن اقتصاد آن ادامه می‌دهیم. ابزارهای بیشتری برای اعمال فشار علیه ایران در اختیار داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20978" target="_blank">📅 22:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20977">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آنا کلی، معاون سخنگوی کاخ سفید، درباره ناو هواپیمابر لینکلن:
رئیس جمهور ترامپ بیش از هر کسی به سربازان اهمیت می‌دهد.
به یاد داشته باشید که جو بایدن تمرکز را از جنگجویان به سیاست‌های حمایت از نیروهای دفاعی تغییر داد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20977" target="_blank">📅 22:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20976">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">به گزارش کانال 13 اسرائیل، اسرائیل قصد داشته به مواضع ترکیه در سوریه حمله کند، اما ترامپ مداخله کرده و مانع آن حمله شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20976" target="_blank">📅 22:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20975">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ced329bda.mp4?token=VizXhZBtOF71cqOtthpOJgo9NXYCwSwUDI8k_yI0ouc6JZVuhoYzuwqzYgNEVAqQIe4Xb1PrE0yeAu25EiXFqar31ziAmLniSDlTLFWuR4awSpw3vkMa3wgxrmTJpWGc00YdXinFX5_0cD7W0hUC6ZD_jAjy33mzzpDSeTFzVkQnziuC7aug4F6DsdLztPXpyjK-YktmuKqrb4__4hAkd8bkZCGljrlYaA0Rosh3uBGCBlxZC4txA-GueglT3S1iWVww7o8Koc4w8KbTmYzQOzIVHi1mqLS19kbUudx86KwW-iW90D4HHe_X6GpJw93BeAFRAiJMuD7oKtqE8VjNKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ced329bda.mp4?token=VizXhZBtOF71cqOtthpOJgo9NXYCwSwUDI8k_yI0ouc6JZVuhoYzuwqzYgNEVAqQIe4Xb1PrE0yeAu25EiXFqar31ziAmLniSDlTLFWuR4awSpw3vkMa3wgxrmTJpWGc00YdXinFX5_0cD7W0hUC6ZD_jAjy33mzzpDSeTFzVkQnziuC7aug4F6DsdLztPXpyjK-YktmuKqrb4__4hAkd8bkZCGljrlYaA0Rosh3uBGCBlxZC4txA-GueglT3S1iWVww7o8Koc4w8KbTmYzQOzIVHi1mqLS19kbUudx86KwW-iW90D4HHe_X6GpJw93BeAFRAiJMuD7oKtqE8VjNKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های اسرائیلی با انتشار این ویدیو می‌گویند برخلاف تصور رایج، بخش زیادی از پرواز جنگنده‌های اسرائیلی بر فراز ایران نه پرتنش و پیچیده، بلکه شبیه یک پرواز عادی است. به ادعای آن‌ها، اطلاعات لحظه‌ای از موقعیت سامانه‌های پدافندی در اختیار خلبانان قرار می‌گیرد؛ تا جایی که این تصاویر از آسمان تهران، بیشتر به یک پرواز معمولی شباهت دارد تا مأموریتی در دل خاک دشمن
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20975" target="_blank">📅 21:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20974">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">امشب تا صبح بیدارم
🙌🏾
روال هر هفته</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20974" target="_blank">📅 21:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20973">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سیریک گزارش صدای انفجار/پرتاب موشک/پهپاد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20973" target="_blank">📅 21:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20972">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1310e64db.mp4?token=Tw25ezmLJULVju8LrWHy5dw6VsroJ56gSlMNq2U_DiysqGk_lXBPAz9BzJHk77zcnQkiMHaoKUjKU90Lm-0pdg3en1J7PTesNPKI5nXjnHot56RD-SxGuZnhC9FWAzQG86lrvlSqMAjioTeV4OpVGbWeJXVYCPQR9pwFyC4vnTcV7x9afn1UH--Jx5sels2MW9ySTsnozKp04OCKNoQIWWh4mJopWOw5Vt0-OE83MLJTP5jhH8C-WMb33tNsZayCqSf8NTcCYrefUPS0ibbAPR58UkycbxjLvJHCrx_fRh08MZk2NOUy2fUGNRVbBS9GWSSD8a780HvdeTSPhePw8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1310e64db.mp4?token=Tw25ezmLJULVju8LrWHy5dw6VsroJ56gSlMNq2U_DiysqGk_lXBPAz9BzJHk77zcnQkiMHaoKUjKU90Lm-0pdg3en1J7PTesNPKI5nXjnHot56RD-SxGuZnhC9FWAzQG86lrvlSqMAjioTeV4OpVGbWeJXVYCPQR9pwFyC4vnTcV7x9afn1UH--Jx5sels2MW9ySTsnozKp04OCKNoQIWWh4mJopWOw5Vt0-OE83MLJTP5jhH8C-WMb33tNsZayCqSf8NTcCYrefUPS0ibbAPR58UkycbxjLvJHCrx_fRh08MZk2NOUy2fUGNRVbBS9GWSSD8a780HvdeTSPhePw8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : این کشتی با یک کشتی یکسان (جرج واشنگتن) جایگزین میشود
خبرنگار: خانواده‌های نظامیان نگرانند از شرایط ناو لینکلن
ترامپ : «نه، آن‌ها نگران نیستند.»
خبرنگار: آیا این استقرار نظامی بیش از حد طولانی شده است؟
ترامپ: «نه، نه، نه؛ حتی نزدیک به آن هم نیست که بگوییم بیش از حد طولانی شده است.»
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20972" target="_blank">📅 21:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20971">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfefd33ebd.mp4?token=HV8LgVk92WtgeL8iQKSt00VNiVI0gzc8mlarFoWdd6bU6XSB0jLmIEfzz3LFKQCbSTsrxuRolvZQ2V6R2qxmwagJKjKMk1or2Uj7behNza9UpZ_rbRq1e5MsiAWrnnpxXwXdavqEMUFnVnmPDWYzukDE1cwdc1tEolgdEqefLoLMQyxgu6sTjSuK9Hyzl5AMRhji3BpapAWmg7GaCrved5bYDsorEcsFt7an_kk2KdgSK6DGuhN8Q4tKTmMo5dz5ri9X9b9Ac3ZVsaExetDef20c9D8ud-Z_Ihz0MDCzGeTMBiE22P8gnQZIMAfJpv2a8ZII6oaeTvd2os1YXa74sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfefd33ebd.mp4?token=HV8LgVk92WtgeL8iQKSt00VNiVI0gzc8mlarFoWdd6bU6XSB0jLmIEfzz3LFKQCbSTsrxuRolvZQ2V6R2qxmwagJKjKMk1or2Uj7behNza9UpZ_rbRq1e5MsiAWrnnpxXwXdavqEMUFnVnmPDWYzukDE1cwdc1tEolgdEqefLoLMQyxgu6sTjSuK9Hyzl5AMRhji3BpapAWmg7GaCrved5bYDsorEcsFt7an_kk2KdgSK6DGuhN8Q4tKTmMo5dz5ri9X9b9Ac3ZVsaExetDef20c9D8ud-Z_Ihz0MDCzGeTMBiE22P8gnQZIMAfJpv2a8ZII6oaeTvd2os1YXa74sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های رژیم : دود مشاهده شده تو جنوب تهران مربوط به آتش زدن ضایعات پلاستیکیه ( عمو پلاستیکیاهو )
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20971" target="_blank">📅 21:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20970">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">داعش شروع به تهدید علیه اسپانیا کرد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20970" target="_blank">📅 20:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20969">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79dd6977b1.mp4?token=N--94gfdHZ_K0vya5NrijoSEb3m9oCHHxEryh8BSehZiBWTpnF98PPrN88UwcZ_bL5d4xr7e_jkfg3RUzW2V8yI5NaEh1x56ORqk_TDOt9L9U58qPYzD753LSLXdrGMeWBu-CwK4yeEFdJPHd9PkMjqk-EbtnuKkP6rt1nfkMdz4OOC6PWIE4V6yV2tlSfoVKRoh-dAUn1epaq5iaIlfKj9jqMCoNjruYDuZyOEpa9299Oncrvzbe2BovRNa436Gk7RAIIPWZPqcQWJ-g2gWFh-1GqOzSFJkwv9bPePFESQMiPwf_3HNYNl_ScJabgsBeHrEtyrum1LKnAkIP72cvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79dd6977b1.mp4?token=N--94gfdHZ_K0vya5NrijoSEb3m9oCHHxEryh8BSehZiBWTpnF98PPrN88UwcZ_bL5d4xr7e_jkfg3RUzW2V8yI5NaEh1x56ORqk_TDOt9L9U58qPYzD753LSLXdrGMeWBu-CwK4yeEFdJPHd9PkMjqk-EbtnuKkP6rt1nfkMdz4OOC6PWIE4V6yV2tlSfoVKRoh-dAUn1epaq5iaIlfKj9jqMCoNjruYDuZyOEpa9299Oncrvzbe2BovRNa436Gk7RAIIPWZPqcQWJ-g2gWFh-1GqOzSFJkwv9bPePFESQMiPwf_3HNYNl_ScJabgsBeHrEtyrum1LKnAkIP72cvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیوزمکس: وقتی یک دموکرات می‌گوید «ایران هیچ‌وقت قوی‌تر از این نبوده»، واکنش شما چیست؟
وزیر خزانه‌داری بسنت: آنها بی‌اطلاع، دیوانه و فاقد هرگونه درک از چیزی هستند که درباره آن صحبت می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20969" target="_blank">📅 17:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20968">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">واشنگتن‌پست: ترامپ حتی در برابر کنگره نیز دست بالا را دارد
واشنگتن‌پست در تحلیلی می‌نویسد قدرت رئیس‌جمهور آمریکا در تصمیم‌گیری درباره جنگ، طی دهه‌ها افزایش یافته و کنگره عملاً ابزار محدودی برای متوقف کردن رئیس‌جمهور دارد. حتی اگر در آینده هر دو مجلس کنگره علیه جنگ رأی دهند، رئیس‌جمهور می‌تواند در برابر چنین تصمیم‌هایی مقاومت کند و در صورت تبدیل شدن آن به قانون، از
حق وتو
استفاده کند؛ وتویی که تنها با رأی دوسوم هر دو مجلس قابل لغو است.
این تحلیل در عمل نشان می‌دهد که
نتیجه انتخابات میان‌دوره‌ای به‌تنهایی لزوماً اختیار ترامپ برای ادامه یا پایان دادن به جنگ را از بین نمی‌برد
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20968" target="_blank">📅 16:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20967">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وزارت جنگ ایالات متحده با شرکت‌های "بوئینگ" و "آر‌تی‌اکس" قرارداد بست تا تولید قطعات یدکی موشک‌های SM-3 را افزایش دهد.
این موشک‌ها برای رهگیری موشک‌های بالیستیک در خارج از جو زمین طراحی شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20967" target="_blank">📅 16:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20966">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoZxyJdV7LLCILDtl28MQ1oCVhxuJWOgPXKOYkHiL_2VmX6_RKWFbZ0L3BNVpceqy2WVDduZXqO3FBmnyB0efrlSkg8W9S4CvGXb3dpksSgS98xoftVvz7JZ9iy4A7oc7BiY4VQCfcbFMmdbZ6xCrNNTb6OEItjucg7sYJgYzW-WW1GIHU9Ta6EUehr0p0yv7QC92Ss8EOrfcCCSI-CPpaM4qzNPnCxPEiD3M_FOqytvSmWsq_mSr2-ZdVTHDko_aFPUjck3fERVGby705v91hcBfylkT5zBNSM5_L3-d6m5_iTJACXnyS9-QEPGj6ox_BGuGNYBzv1U9d4H6eKTZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ در تروث :
نیوزمکس : ایالات متحده با انزوای اقتصادی بی‌سابقه‌ای به ایران ضربه خواهد زد
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20966" target="_blank">📅 15:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20965">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ادعای وال‌استریت‌ژورنال:
ایران و عمان در حال نهایی کردن پیش‌نویس توافقی برای بازگشایی تنگه هرمز بودند که به تهران اجازه نظارت بر کشتی‌هایی که وارد خلیج فارس می‌شوند را می‌دهد، اما اجازه نمی‌دهد عوارض یا هزینه‌های خدمات دریافت کند.
طرفین در مورد نکات اصلی پیش‌نویس که یک خط ورودی در نزدیکی ایران و یک خط خروجی در نزدیکی عمان ایجاد می‌کند  توافق کرده‌اند و آن را با آمریکا، کشورهای منطقه و رهبران ارشد ایران به اشتراک گذاشته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20965" target="_blank">📅 15:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20964">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اکسیوس : به گفته دو نفری که اخیراً با ترامپ درباره نتانیاهو گفت‌وگو کرده‌اند، ترامپ گفته است: “بی‌بی بزرگ‌ترین دشمن خودش است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20964" target="_blank">📅 15:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20963">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اکسیوس : دونالد ترامپ با وجود درخواست‌های مکرر، هنوز از حمایت رسمی بنیامین نتانیاهو در آستانه انتخابات ۲۷ اکتبر اسرائیل خودداری کرده است. در حالی که نظرسنجی‌ها نشان می‌دهد ائتلاف نتانیاهو از اکثریت لازم برای تشکیل دولت فاصله دارد و رقبای او پیشتاز هستند، اختلافات واشنگتن و تل‌آویو بر سر ایران، غزه، لبنان و سیاست‌های منطقه‌ای افزایش یافته است. مقام‌های آمریکایی می‌گویند ترامپ از برخی تصمیم‌های نتانیاهو ناراضی است و ضعف او در نظرسنجی‌ها نیز تمایل رئیس‌جمهور آمریکا برای ورود به رقابت انتخاباتی اسرائیل را کاهش داده است. با این حال، کاخ سفید همچنان امیدوار است دولت اسرائیل در اجرای طرح صلح غزه، مذاکرات منطقه‌ای و برنامه‌های آمریکا برای توافق احتمالی میان اسرائیل و عربستان همکاری کند
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20963" target="_blank">📅 15:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20962">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e612920df0.mp4?token=GuPgeSqiA-ae-4ySpB656n3IqFkQj-TX3ESc_f4gKa9pbXugCqxjYcwu2JI4VaRyoRnB90lTI0qB1OkdfFVPtN8xOl-G1oIhPd3V9gDyEbwWQRns_NRjQsgqui-O4MOPQ7687yZGoxnhPlKoFqwSaC4l__W3SjMFUj_pgBNPzIf7hsAzzUgfRGbQGscfGPgFjPHa-BwtkFelqv27zRmAHug1quIMFO2Qew21A0RT8iVVCPJh6Z0oAVLFsEpp-aB_sm9f1OYxTd6NTEf3nICnghIYbSrqhTXt3ynZD9iFRs8Fln1enfhcHu4uc94SGcUntlEIYpESOFEQ6Pas4Y2ZxIur_sByQU9zM9zNT1WUqegDhkGd2TfGTyB6LQLmfjfNJO5xiqFS1tUeJpfVp0KLlceumqWXlIUFikRaz4jy6R6Bkm-LSXWHKrkJhY0hVYDB5et3EhHR2Byso-CWFOoj8rNKjQSKg2mcvxZE965VxvzEjztwg8WLH2AClw9SVv_K_LaWjNNCEw5VuAd_O2YtD9R_J0n86WTEEoJ5XcmsnLzM2wyZ4Vz9yjd0SdJvrak6dz7uKof7SxRdhk-qiXvRdgRS5xglEqKmhqdVae9-28ewDuWcghV44pA5PT2LpkriMPwb9bDPtdyzO-sMY9CTAUQZwdlB1A5BChnIzNYlTIU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e612920df0.mp4?token=GuPgeSqiA-ae-4ySpB656n3IqFkQj-TX3ESc_f4gKa9pbXugCqxjYcwu2JI4VaRyoRnB90lTI0qB1OkdfFVPtN8xOl-G1oIhPd3V9gDyEbwWQRns_NRjQsgqui-O4MOPQ7687yZGoxnhPlKoFqwSaC4l__W3SjMFUj_pgBNPzIf7hsAzzUgfRGbQGscfGPgFjPHa-BwtkFelqv27zRmAHug1quIMFO2Qew21A0RT8iVVCPJh6Z0oAVLFsEpp-aB_sm9f1OYxTd6NTEf3nICnghIYbSrqhTXt3ynZD9iFRs8Fln1enfhcHu4uc94SGcUntlEIYpESOFEQ6Pas4Y2ZxIur_sByQU9zM9zNT1WUqegDhkGd2TfGTyB6LQLmfjfNJO5xiqFS1tUeJpfVp0KLlceumqWXlIUFikRaz4jy6R6Bkm-LSXWHKrkJhY0hVYDB5et3EhHR2Byso-CWFOoj8rNKjQSKg2mcvxZE965VxvzEjztwg8WLH2AClw9SVv_K_LaWjNNCEw5VuAd_O2YtD9R_J0n86WTEEoJ5XcmsnLzM2wyZ4Vz9yjd0SdJvrak6dz7uKof7SxRdhk-qiXvRdgRS5xglEqKmhqdVae9-28ewDuWcghV44pA5PT2LpkriMPwb9bDPtdyzO-sMY9CTAUQZwdlB1A5BChnIzNYlTIU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیپلر
: ترافیک دریایی از تنگه هرمز در ۱۳ اوت افزایش یافت و ۱۳ عبور تایید شده ثبت شد که نشان‌دهنده رشد ۴۴ درصدی نسبت به روز قبل (۹ عبور) است. نه کشتی از طرح یک‌جانبه ایران استفاده کردند، هیچ عبوری در سیستم جداسازی ترافیک هرمز تایید نشد و چهار مسیر نامشخص باقی ماند.
فعالیت در باب‌المندب پایدارتر بود و ۲۹ عبور تایید شده ثبت شد که ۴ درصد بیشتر از ۲۸ عبور روز قبل است. هجده کشتی وارد دریای سرخ شدند و ۱۱ کشتی از آن خارج شدند، در حالی که دو عبور تاریک ثبت شد. در طول روز هیچ حمله جدید تایید شده‌ای به کشتی‌ها گزارش نشد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20962" target="_blank">📅 14:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20961">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f327dcc92.mp4?token=e0n1UwfKTznR2sGqPWSCL26VU8aULS2sLsMcjtVgKq9hYUX4cMTwRQ2rxK-fSXFsJ_hwF5ntN5i25_-6qmh-CHRB9e0xWdPyNugyc-hCxedsMYiwWQ-OLZDZNb9YICp0rkOiJy08SgFcNwSJSDiH1lDQFOb1KW0oicVMO_t0UpfOAWCt7NRxRnkqTcbF0NaJSGgW7NN66WbyJLlr8q3wZTEXFiqELoVBafyGDE82TKYvmpOuBVuIoFSR1lxGN58j6urJRizv8hQeQ_fDamao58mgeRx4h7m52wqPW5tSCaQYc_N-q9ngzJCVlLmRVibZT2slsWg86RvmwYEEsTbbdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f327dcc92.mp4?token=e0n1UwfKTznR2sGqPWSCL26VU8aULS2sLsMcjtVgKq9hYUX4cMTwRQ2rxK-fSXFsJ_hwF5ntN5i25_-6qmh-CHRB9e0xWdPyNugyc-hCxedsMYiwWQ-OLZDZNb9YICp0rkOiJy08SgFcNwSJSDiH1lDQFOb1KW0oicVMO_t0UpfOAWCt7NRxRnkqTcbF0NaJSGgW7NN66WbyJLlr8q3wZTEXFiqELoVBafyGDE82TKYvmpOuBVuIoFSR1lxGN58j6urJRizv8hQeQ_fDamao58mgeRx4h7m52wqPW5tSCaQYc_N-q9ngzJCVlLmRVibZT2slsWg86RvmwYEEsTbbdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش اسرائیل در حال انفجار ساختمان‌ها در منطقه روستای شیعه‌نشین مرکبا در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20961" target="_blank">📅 13:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20960">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">از امشب ۳ شب مست میکنم
😂
🙌🏾</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20960" target="_blank">📅 12:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20959">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBoYTSDbmM-zhvNkadVnRZEgSQAlsv_GKxhjlmMl5xWULa10V1WBMeqPMTdAAJcOOiQTJopNgeGTKS0t0aHD2kG95EvGCk43P1o7wefI6CdhzROK5sxbyyn7OV8ePArxQ5BVbhiTZpCWDYUmOhqfg0F9DI9Gs0NecNhRxpaVk_KARv-x_YdyhlIdH0VNKPztlN-9lRQZR7iQ3AWMKCgNJ8QsXbu52WqsnM81TLPQ0Pqp702kDtVD8h0fjlYNXPxcj5bgFhHW9ugqEIFmrlFRQ0pq_vKNViez6FZwPEOyIbxaUGO1dUlqxR5G_4AwheXRUhUf5edXEhTBiI4s-D_RAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
بر اساس گزارش‌های دریافتی این سازمان از مراجع نظامی، یک نفتکش هنگام عبور خروجی از تنگه هرمز هدف یک پهپاد (UAV) قرار گرفته است. این شناور دچار خسارت جزئی شده، اما تمامی اعضای خدمه در سلامت هستند و حضور همه آن‌ها تأیید شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20959" target="_blank">📅 11:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20958">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‎ اتاق جنگ با یاشار : فلورا جون سر گردنه
هم مسیر شدن ناو هواپیمابر جورج
واشنگتن با یک کشتی کارگو ایرانی به نام «فلورا»که بسیار زیاد شبیه به عکس کاور مجله اکونومیک ۲۰۲۶ است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20958" target="_blank">📅 11:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20957">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5efb82e574.mp4?token=TI06CWZB9XD5V4c6tGDQrMx-4Fc74PQlR1iHtX-yNACNut7Gs-WkDsB-jvgsQHehvTNmpEO6UR3ZDbnVKwUuEw9Dttq87kqollmK9GsKdXrYo4x6RROHqOZniCv-4z2XU0igtx0m0RlDBxOhIDnSt_kLcN-AEPJW4FdGkaDCrY9lEOhuCm1bqatcEJrjgzCVG2j-junaRB5LO6sI6641Sc8qpeFpwtS3dmh0e_g-POD2If5K0Bbfg9kNz8AYMohsS5OXyxAiDODVtK2YE41tnr3EJZGDYYypI4npGeu1K0JCt4NNyg7jH7nCpYNUcp_HQV740LCJJKf3aFTDtmK6xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5efb82e574.mp4?token=TI06CWZB9XD5V4c6tGDQrMx-4Fc74PQlR1iHtX-yNACNut7Gs-WkDsB-jvgsQHehvTNmpEO6UR3ZDbnVKwUuEw9Dttq87kqollmK9GsKdXrYo4x6RROHqOZniCv-4z2XU0igtx0m0RlDBxOhIDnSt_kLcN-AEPJW4FdGkaDCrY9lEOhuCm1bqatcEJrjgzCVG2j-junaRB5LO6sI6641Sc8qpeFpwtS3dmh0e_g-POD2If5K0Bbfg9kNz8AYMohsS5OXyxAiDODVtK2YE41tnr3EJZGDYYypI4npGeu1K0JCt4NNyg7jH7nCpYNUcp_HQV740LCJJKf3aFTDtmK6xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویکتور دیویس هنسون
تاریخ‌دان، نویسنده و تحلیلگر سیاسی محافظه‌کار آمریکایی و پژوهشگر ارشد مؤسسه هوور است. او از حامیان شناخته‌شده دونالد ترامپ به شمار می‌رود، کتابی در دفاع از ترامپ نوشته و دیدگاه‌هایش در رسانه‌های محافظه‌کار آمریکا بازتاب گسترده‌ای دارد, وی پیشنهاد کرده است ترامپ از شاهزاده رضا پهلوی حمایت کند و زمینه تشکیل یک دولت ایرانی در تبعید تحت رهبری ایشان و با مشارکت ایرانیان را برای جایگزینی رژیم جمهوری اسلامی را فراهم سازد.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20957" target="_blank">📅 09:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20956">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">هشدار خزانه‌داری آمریکا: تحریم‌های «بی‌سابقه» علیه ایران از هفته آینده
اسکات بسنت، وزیر خزانه‌داری آمریکا، اعلام کرد دولت ترامپ هفته آینده از بسته‌ای جدید از تحریم‌ها و اقدامات اقتصادی علیه ایران رونمایی می‌کند که به گفته او «در تاریخ بی‌سابقه» خواهد بود. جزئیات این اقدامات قرار است هفته آینده به‌صورت رسمی منتشر شود. این بسته بخشی از تشدید سیاست «فشار حداکثری» واشنگتن است و انتظار می‌رود بر مسدود کردن مسیرهای دور زدن تحریم‌ها، ناوگان سایه و کانال‌های مالی و ارزی ایران تمرکز داشته باشد؛ اقدامی که با هدف افزایش فشار اقتصادی بر تهران پیش از هر تحول دیپلماتیک یا نظامی دنبال می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20956" target="_blank">📅 09:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20955">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حقیقت یاب سنتکام در جواب به رسانه های رژیم :  ناو هواپیمابر «یو‌اس‌اس آبراهام لینکلن» همچنان یکی از بالاترین نرخ‌های تمدید خدمت خدمه را در میان تمام ناوهای هواپیمابر نیروی دریایی ایالات متحده دارد؛ این نرخ ۸۴.۴ درصد است. ملوانان و تفنگداران دریایی گروه رزمی ناو هواپیمابر آبراهام لینکلن، پس از بیش از ۲۶۰ روز حضور در دریا، انجام ۱۰ هزار پرواز و مصرف ۱.۵ میلیون پوند مهمات، همچنان مقاوم و مصمم باقی مانده‌اند. هیچ‌یک از نیروهای نظامی حاضر در این ناو هواپیمابر جان خود را از دست نداده‌اند و تنها ملوانی که در ۳ اوت به دریا افتاد، به‌سرعت و در سلامت کامل پیدا و نجات داده شد. گزارش‌های گسترده و نادرست درباره مأموریت تاریخی آبراهام لینکلن، در حق زنان و مردان نظامی ما و خانواده‌هایشان بی‌انصافی است
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20955" target="_blank">📅 03:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20954">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">هم اکنون حملات شدید پهپادی جمهوری اسلامی به مواضع گروه های کورد در اربیل عراق
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20954" target="_blank">📅 03:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20953">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">چند گزارش داشتم از صدای تیر اندازی سمت غرب (محدوده آزادی)
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20953" target="_blank">📅 02:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20952">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ به فاکس نیوز ‌: محاصره دریایی ایالات متحده در تنگه هرمز کاملاً برقرار است و «یک دیوار فولادی» است.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20952" target="_blank">📅 02:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20951">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EinHX2Qz1DR_lv3c2Twkd48ws6wC5kRvvW1h5RUfHRMfQD7prTtEUEipmBRzbtqbXtr0RV8dANoeBmDHblykPwpL6e5ySz_Mi66gsf-dACmx1_bj05-DiUJP3VSde3vENJQN80hesE7Xuuoe714gDzLqbajDVxgosA26sBMZGCwZ0pmEnok1bib58CDWxLCrQzW3c1SamzHepNpsPTHMYuJHbgcScmaIjiLYbsEH9Yr5YMxyj5r5sne-X8QSaQsMXfOO9gjCEExiF4fvxO1Zu2vCvik1FRMk0WyMdOSpbzSR_z5GEGEP5RTSoUPgltEJfi_fDlGtBNzpbZdz1f5JoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای F/A-18C هورنت معمولی نسل اول برای تفنگداران دریایی آمریکا، از سمت تنگه هرمز با ترانسپوندر روشن( فعال بودن سیستم شناسایی و ارسال اطلاعات موقعیت ) با یک چرخش در ابوظبی فرود آمد.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20951" target="_blank">📅 02:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20950">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بعد از مدتها حتی‌ اطراف تنگه هم سوخترسان دیده نمیشه عجیبه…</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20950" target="_blank">📅 01:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20949">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50455ef10.mp4?token=hyJsDvQXe5EQbTh7YgdC5ynk2u3tmsy0EyrsydgGmtPS4P9477yPIBjvBnCIsNPF-xd4xbtIqWWiSHz-WxdVMqtM4PQMh5VTLI0z_e8JgxYesKcyF-ltuJF_mhF1jgipdWJwdiV2xp93_mgfVhQOpSBw5TQVNQbULqJodtKIOxHNO9cGy73gofX1693KzGU35fnZucphqJ8ziDt_AdFKSM4xBBUgXCTE0a_7dmxD7ytnULp6MFB456oLvYDSCtZxpRkPu1waNYtg_GfdToQtUa5EYd2lPQLzPAaDAJ1ctonazNJgSQzr98dhc3Ni9f5MZcV9SevGt5NcuObfy9M-bKiIyL5ycSABGSC94wI9_Swk21GCSDj2PhI1h9lf0LP9vKDXAjWQWWuXtU11mSg8gyT8zwhydcdUzIDCfnxWTqm-8JPUtmaZxrpDJqeBglkNCP3b7DBB2ZOZuTgcPKK2RP_KRcvEdPKOqe8IJhLy6REPSXoYhYRNha8GI7YRzuvEs_aPYBAJVNFP1eVupAm42f99U7LzMMSFvJOR-z1Riaqs2lo2J-8vQKrQcvvkROThd0DyDw75CBNZ2FyC00ydZ1Ffw62FzmoRqcnLIsBKNcfNBa-Jq7t8aUGCgBiAvoHZBhjYitpf4C8Jy0DVLSSLTMSi-OVc99IQTyhVhu66TMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50455ef10.mp4?token=hyJsDvQXe5EQbTh7YgdC5ynk2u3tmsy0EyrsydgGmtPS4P9477yPIBjvBnCIsNPF-xd4xbtIqWWiSHz-WxdVMqtM4PQMh5VTLI0z_e8JgxYesKcyF-ltuJF_mhF1jgipdWJwdiV2xp93_mgfVhQOpSBw5TQVNQbULqJodtKIOxHNO9cGy73gofX1693KzGU35fnZucphqJ8ziDt_AdFKSM4xBBUgXCTE0a_7dmxD7ytnULp6MFB456oLvYDSCtZxpRkPu1waNYtg_GfdToQtUa5EYd2lPQLzPAaDAJ1ctonazNJgSQzr98dhc3Ni9f5MZcV9SevGt5NcuObfy9M-bKiIyL5ycSABGSC94wI9_Swk21GCSDj2PhI1h9lf0LP9vKDXAjWQWWuXtU11mSg8gyT8zwhydcdUzIDCfnxWTqm-8JPUtmaZxrpDJqeBglkNCP3b7DBB2ZOZuTgcPKK2RP_KRcvEdPKOqe8IJhLy6REPSXoYhYRNha8GI7YRzuvEs_aPYBAJVNFP1eVupAm42f99U7LzMMSFvJOR-z1Riaqs2lo2J-8vQKrQcvvkROThd0DyDw75CBNZ2FyC00ydZ1Ffw62FzmoRqcnLIsBKNcfNBa-Jq7t8aUGCgBiAvoHZBhjYitpf4C8Jy0DVLSSLTMSi-OVc99IQTyhVhu66TMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز : آقای معاون رئیس‌جمهور، یک لحظه به توافق نزدیک هستیم، لحظه بعد می‌گوییم قرار است حسابی آنها را بمباران کنیم. یک لحظه تنگه هرمز باز است، لحظه بعد بسته است. مطمئنم این نگرانی و سرخوردگی داخل کاخ سفید هم وجود دارد. می‌دانم پیش‌بینی کردن دشوار است، اما اجازه دهید بپرسم:
این ماجرا چگونه تمام می‌شود؟ اگر و زمانی که مسئله ایران تمام شود، وضعیت چگونه خواهد بود؟
جی‌دی ونس:
خب ویل، چیزی که با اطمینان می‌توانم بگویم این است که فکر می‌کنم این ماجرا با
قرار گرفتن ایالات متحده در موضعی قدرتمندتر
پایان خواهد یافت؛ در شرایطی که ایران
سلاح هسته‌ای نداشته باشد
و
تنگه هرمز دوباره به وضعیتی بازگردد که قیمت نفت و گاز برای مردم آمریکا باثبات باشد
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20949" target="_blank">📅 00:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20948">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ونس، معاون رئیس جمهور آمریکا: آمریکا ابزارهای زیادی برای مقابله با ایران در اختیار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20948" target="_blank">📅 00:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20947">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اکسیوس : جرد کوشنر، فرستاده ویژه رئیس جمهور ترامپ، قرار است هفته آینده به اسرائیل سفر کند و با نتانیاهو دیدار کند
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20947" target="_blank">📅 23:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20946">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رویترز : ترامپ در آستانه یک جنگ پیچیده‌تر قرار دارد و به نظر نمی‌رسد که این مسئله او را رها کند.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20946" target="_blank">📅 22:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20945">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گزارش صدای انفجار‌ سیریک ، پرتاب موشک/پهپاد به سمت تنگه هرمز @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20945" target="_blank">📅 22:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20944">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اصفهانی معاون پزشکیان:
تغییر قیمت بنزین در کرمان به‌دلیل برخی بی‌تدبیری‌ها متوقف شد.
۱۴ میلیون لیتر بنزین در هر روز کم داریم
دولت برای بنزین برنامه دارد و روزهای آخر تصمیم‌گیری در مورد آن است.
ما ۳ برنامۀ جدی داریم و هرکدام از آن‌ها نهایی شود، قبل از اجرا آن را به مردم توضیح می‌دهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20944" target="_blank">📅 22:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20943">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/737fe5f83b.mp4?token=ePGxew61gGLJngFcZ3iCf2Fvks0tJS6Dwj2Q9WDXcazDOL8P-h5bXEIje-gCU52Khy_8Ja6qThDgCn7v11F38-OQ9EdZ5dOYM22ewtBI4lz3MSZos3MfT2chh85nCSsu7dfwZek3OoJMU0Ar8PY2CD52QMC2q4zQl1PIH9LOHNHSIH1ZA_jp6QizAqIZuhJnnPKiH4AyjLIviAmMoRGKMK9qWbfnQT4l94JcRAHZUF_oh5-aokuBnpf2Rla0UREHJ6YMu0lKLBh_sNWKhPuAQYIwaNucIJiffcy3uXe4Rcymwu70pq79FHTuvugG3z6CcATt-sOYuFNRg9CcSX5_Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/737fe5f83b.mp4?token=ePGxew61gGLJngFcZ3iCf2Fvks0tJS6Dwj2Q9WDXcazDOL8P-h5bXEIje-gCU52Khy_8Ja6qThDgCn7v11F38-OQ9EdZ5dOYM22ewtBI4lz3MSZos3MfT2chh85nCSsu7dfwZek3OoJMU0Ar8PY2CD52QMC2q4zQl1PIH9LOHNHSIH1ZA_jp6QizAqIZuhJnnPKiH4AyjLIviAmMoRGKMK9qWbfnQT4l94JcRAHZUF_oh5-aokuBnpf2Rla0UREHJ6YMu0lKLBh_sNWKhPuAQYIwaNucIJiffcy3uXe4Rcymwu70pq79FHTuvugG3z6CcATt-sOYuFNRg9CcSX5_Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست به نیوز مکس : گزارش‌های مربوط به تخریب شرایط در ناو هواپیمابر ابراهام لینکلن کاملاً تحریف‌شده است و  هیچ کم و کسری وجود ندارد
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20943" target="_blank">📅 21:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20942">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سی‌بی‌اس: فقط یک ملوان در پی حادثه از عرشه هواپیمابر آمریکایی "یو‌اس‌اس لینکلن" در اوایل ماه آگوست(۲هفته پیش) به داخل دریا سقوط کرد. این ملوان توسط یک بالگرد جستجو و نجات نجات یافت و پس از دریافت درمان توسط بخش پزشکی، از کشتی منتقل شد تا مراقبت‌های پزشکی بیشتری دریافت کند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20942" target="_blank">📅 21:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20941">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntaXkEhJYgD0bXKW0LjNrIOzRyw05J2dRFcOPcyXAEmlgary8jHkFi7wNepWYXhFpl6XAutTzvbBKOiGTBVWEya4hFdLzztszliKZmLtAKJDVeejzsU7GcIH6c4vYbKB0Qkrw7CqCLIfeYYh2-TSWi1Z8pFztNUAG4cjfDOx9B3oDGQsxmGBpaoG9OR-vr-8NPJZINbGB2JWL0LRlLe0LJkQPlz-hCMKIucnN_noqLbIM7SBIMXMMbIG2vepeEhCUEUB9Taz7Rib7Y-elFtWVsfk53qq7Y4qA6V_tcnrwB_5x4dwomWzn1RxS2m-cB99vCjKwqkPa1rxsSMDvDbyXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ با ارسال این عکس نوشت برایم، من در منطقه ای زندگی می‌کنم که همه عرزشی هستند. دقایقی پیش در کرج رعد و برق مهیبی زد. بلافاصله اکثر این ساختمان ها برقهایشان را از ترس حمله هوایی خاموش کردند. اینها از ترس شب و روز ندارند. خودشان هم میدانند به زودی کارشان تمام است. به مردم بگو ناآمید نشوند ، پیروزی نزدیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20941" target="_blank">📅 21:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20940">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یک منبع دیپلماتیک به شبکه خبری ام تی وی لبنان اعلام کرد که مقامات رسمی در بیروت، اطلاعیه مهمی دریافت کرده‌اند مبنی بر اینکه مقامات سیاسی اسرائیل، به ارتش اسرائیل اجازه داده‌اند تا منطقه علی طاهر در ارتفاعات نبطیه را کاملا منفجر کند (گفته میشود در این منطقه صدها نفر از نیروهای حزب‌الله و سپاه پاسداران در تونل‌هایی به دام افتاده‌اند)، انتظار می‌رود به زودی این انفجارها رخ دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20940" target="_blank">📅 21:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20939">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کانال ۱۳ اسرائیل : فرمانده سنتکام، برد کوپر به مقامات اسرائیلی گفته که در تلاشه تا جنگ علیه ایران رو از سر بگیرن چون معتقد است که این جنگ موضع ایران رو در مذاکرات هم تغییر میدهد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20939" target="_blank">📅 20:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20938">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سنتکام قصد دارد یک نیروی جدید پهپادی به نام
«فالکون استرایک»
تشکیل دهد؛ نیرویی چندملیتی که نیروهای آمریکایی و کشورهای منطقه را در یک ساختار مشترک کنار هم قرار می‌دهد. هدف این نیرو استفاده از
پهپادهای تهاجمی یک‌طرفه
(پهپادهایی که پس از حمله به هدف خود نیز از بین می‌روند و شبیه مهمات سرگردان یا «پهپاد انتحاری» هستند) در سه حوزه
هوا، سطح دریا و زیر آب
است. این طرح زیر نظر فرماندهی عملیات ویژه آمریکا شکل می‌گیرد و بر تجربه گروه
«اسکورپیون استرایک»
ساخته می‌شود؛ گروهی که طبق این گزارش، پهپادهای آن پیش‌تر در عملیات علیه ایران استفاده شده‌اند. سنتکام اکنون از کشورهای منطقه دعوت کرده به «فالکون استرایک» بپیوندند تا یک
توان مشترک و یکپارچه پهپادی در سراسر خاورمیانه
برا عملیات ایجاد کنند
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20938" target="_blank">📅 20:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20937">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">از تنگه صدای پول های بلوکه شده میاد
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20937" target="_blank">📅 20:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20936">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گزارش صدای انفجار‌ سیریک ، پرتاب موشک/پهپاد به سمت تنگه هرمز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20936" target="_blank">📅 20:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20935">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-pZ5xF-DVjQQ5Wt6-mPVzyGNhQdxWmYDrwC7hw__HIxWAPMnJI8BC8SbIg4On2L_1L4g6vU31kM03zC4z9qmES_EcGf0NxGFOLSTHhVF3e3RW6qrAaDrHcKK4x5R4XiunHHkvssJ-03dnR7y5OaEQLvo6CKrxUgB8veVz-to99RnEDvbppRBX-JoD755rzxr3Nt7J4c_wIFsoCc512VFrRV6urC9NfN0X5wzQ0fswLpqZVkCsD7VicbszA6O_SYDYVZdKhlx9w0NjATG3Pe95JQ_mYHdaJ9Z7NHjC0Ht20_t6HSxzw_a5MDIMlRrgCVji-BZeybM0YV70Ky-6Qz_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هگست وزیر جنگ ، امروز در پاناما و پس از دیدار با خدمه ناوشکن USS Gridley گفت :
محاصره وابسته به حضور یک ناو یا یگان خاص نیست؛ نیروها می‌توانند یکی‌یکی تعویض و جایگزین شوند و بنابراین از نظر نظامی آمریکا می‌تواند آن را برای مدت نامحدود ادامه دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20935" target="_blank">📅 20:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20934">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خبرگزاری حوثی‌ها «سبا» به نقل از یک منبع نظامی گزارش داد که حوثی‌ها با استفاده از دو پهپاد به پالایشگاه شرکت آرامکو در منطقه جیزان عربستان سعودی حمله کردند. همچنین اعلام شد: «این حمله در پاسخ به نقض حریم هوایی یمن توسط سعودی در مناطق صعده و حجه انجام شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20934" target="_blank">📅 19:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20933">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کانال ۱۴ اسرائیل:  رئیس ستاد کل نیروهای مسلح اسرائیل ، ایال زمیر، به وزرای کابینه اعلام کرد که محاصره دریایی ایران بسیار موثر بوده است. طبق ارزیابی‌های اولیه ایالات متحده، مقامات ارشد اکنون بر این باورند که تداوم این فشار شدید اقتصادی هم‌زمان با وخامت سریع بحران مالی داخلی در تهران ،مؤثرترین راهبرد برای وادار کردن رژیم به تسلیم یا زمینه‌سازی برای فروپاشی آن است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20933" target="_blank">📅 19:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20932">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">@WarRoom
بالون</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20932" target="_blank">📅 19:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20931">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee29e07a01.mp4?token=SdcQG9qhFS4f4m5dhBYzhqJaSs0LXzOctc53rdOdQsxvHoDX0VRk9OEhBOD0Dr4OHuhNMi9IJ-uSKSDibzZtreuLo3O9A-Jn8ris3brzkfUGP0hWBhUysbSneaqS9r7NNZSuTTXqv58lFhq4tM3xs81j8BKumqlDtkbf27ee9_JRMVdA4WJepQAwjts3G3p0dKWycnwkV3qLpHrXdJMsYub4DLe6B9QYsecireCZQQgz6pDbxRagjUbd4puXLr7UMTBbCCFiXC3ekcJI6z5JBPWgjE4pn2MnR40hXn1TItUgN7nVpbV4fihnluhPZklGB8c6UTa35QPhNdpHZmsdkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee29e07a01.mp4?token=SdcQG9qhFS4f4m5dhBYzhqJaSs0LXzOctc53rdOdQsxvHoDX0VRk9OEhBOD0Dr4OHuhNMi9IJ-uSKSDibzZtreuLo3O9A-Jn8ris3brzkfUGP0hWBhUysbSneaqS9r7NNZSuTTXqv58lFhq4tM3xs81j8BKumqlDtkbf27ee9_JRMVdA4WJepQAwjts3G3p0dKWycnwkV3qLpHrXdJMsYub4DLe6B9QYsecireCZQQgz6pDbxRagjUbd4puXLr7UMTBbCCFiXC3ekcJI6z5JBPWgjE4pn2MnR40hXn1TItUgN7nVpbV4fihnluhPZklGB8c6UTa35QPhNdpHZmsdkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20931" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20929">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : جوجی‌جون ، ناو هواپیمابر جورج واشنگتون و اسکورتش به سمت منطقه می آیند
🚨
🚨
🚨
کارهای اداری یادتون نره⁩ https://www.instagram.com/reel/Db-HXkWoJz-/?igsh=NHNmZ3ZhYnhhdDJi</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20929" target="_blank">📅 19:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20928">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وال استریت ژورنال : ایالات متحده در بحبوحه تنش‌های جنگ با ایران، ناو هواپیمابر جورج واشنگتون را به خاورمیانه می‌فرستد
@WarRoom
یاشار : خیلی عقبید
😁</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20928" target="_blank">📅 19:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20927">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a73c9be9f.mp4?token=QqKyiqpf_q-J96AYU-ftVetkPIp-squ4hLj4gtYQSMXoYOawtvgrcfF11j4Nb8jlSptts-3IZsOcDJKVljnmIvsBo92-tonn_bMMw4fux7IMTLPejYBKc6w3LVEMlseSIJzU1KyZGtsoQe7DmaYv-q8wDxK_MlYEQvFHwXzQJOUeUQMT99yioubELumRBU3IYmOjVhhQxKLnXsKVC1iOmqL5aVnKwYOflwote1VTbCjHHYAEB5QPQhT9adegBYb-D4sZMSaPgwkDZmlX7c2tgM8L-nFavbXfaQuW2PThAprGFYCJFcMXnkWosRdNgskA2oSt0p3byzz_FWazp4YoETzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a73c9be9f.mp4?token=QqKyiqpf_q-J96AYU-ftVetkPIp-squ4hLj4gtYQSMXoYOawtvgrcfF11j4Nb8jlSptts-3IZsOcDJKVljnmIvsBo92-tonn_bMMw4fux7IMTLPejYBKc6w3LVEMlseSIJzU1KyZGtsoQe7DmaYv-q8wDxK_MlYEQvFHwXzQJOUeUQMT99yioubELumRBU3IYmOjVhhQxKLnXsKVC1iOmqL5aVnKwYOflwote1VTbCjHHYAEB5QPQhT9adegBYb-D4sZMSaPgwkDZmlX7c2tgM8L-nFavbXfaQuW2PThAprGFYCJFcMXnkWosRdNgskA2oSt0p3byzz_FWazp4YoETzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رابرت اف کندی جونیور:
دانا وایت گفته که او هیچ‌وقت ندیده ترامپ آب بنوشد. او فقط نوشابه رژیمی دایت‌کُک می‌نوشد.
او از هر آدم دیگری که تا حالا دیده‌ام، انرژی بیشتری دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20927" target="_blank">📅 18:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20926">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">جمهوری اسلامی از طریق ترکیه به سوریه اطلاع داد که در صورت دخالت ارتش سوریه در لبنان علیه حزب‌الله، صدها نقطه در سراسر سوریه، از جمله کاخ ریاست‌جمهوری، با پهپادها و موشک‌ها مورد هدف قرار خواهند گرفت.
یک تحلیل اخیر هم صراحتاً می‌گوید ترکیه واشنگتن را متقاعد کرده که از دولت احمد الشرع(پیش‌تر با نام ابومحمد الجولانی)در رویارویی با حزب‌الله در لبنان استفاده نکند.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20926" target="_blank">📅 18:37 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
