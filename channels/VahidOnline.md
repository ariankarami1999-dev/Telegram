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
<img src="https://cdn1.telesco.pe/file/TXJVEELWGCLELyETIQ0P3RuH3SgwYTZIJP4PKXTxwiiH_FrM_TfZ9uGFhNoAmL4HW3DiNpH9plNpxkdEOOZPYY7ZNb_Y24vqjZV3DzyzBW9ruSZXV3Pt0zr6zEE2EXVCDnPQhfT99_89HXi1x6WKIB8XU-xCJUlZEdP617Q1gmWN3XEyMJEYqzSm5bgurLfffc5eCN8p7QZG8HwVZQHcaM0xQAUZIHn2TOwj3xz-V0umtL_SU1lr8LIxgO3OGmuIiij9d5EGrdCmHlpEc2dLlNOc3oyLHf8ApY9G4h2nMu5xpJ02xccpO1E10IkzsQImVeb6jbr7ecHuoPFSJEGipQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.35M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 20:30:22</div>
<hr>

<div class="tg-post" id="msg-76629">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q-HsdfJkXlJ-7-9bzLHjsaixdOdtUP8VxQBDjhZRKnDFNgvPJK3oxD0QLadUlLDT_9CEuxcYUEvYlZbsH43mQCJJIj7Z9dgm2V9kY9B9dFvBeF9Re196ioh7dkt1ikselsfzdJHni3wcy6br4wYDToVFX6RT6fmkiPj47gEu94AweHLwmqzV6ZIegMmVvAA3BMM9gEfwsnlKxYnJPvIy7pGAhij4VN4ZuLIDPZuOua1lD40ebNGqtrhnkn9HiMBUQwxEmNoUjlXJTwZ9UPETYdPk8vAC7B4gKY6VJ-YReEND6hNfJKOpCjkGfbKJvKx8SOqQbTDnKDBkuQ0LPGac7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/VahidOnline/76629" target="_blank">📅 19:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76628">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pw9XvsNzaAWFAXPOTMzRvqrWyu4ESc0__sJjAKnXl_i5CMFbmTOEYf54bglzpV2wf8iU4yBAYILic4jh01Ba19sAhc-StdVMV73145IOjM4iZRRixUZ7G4qPkvux6hVHHSfxmyGs9sD3LwEKso34FaFNVR0rT9zwBXVlZ9owzvzxObwfLqRM1oT_hRsDUYW69p4kZfAEiDJBaiNYedN_Wn-e7ZflLURKuCI71o-ZLtJnDNLf6V3yDOyM1IsBAqgy0r-gBb6YfeMG2MICvkcHUla41gZOIQZAjQpTjMHTQPQbUTt5m_otXYQlFmrCiLA7-BrcAYoKWArlQOKQ33gcug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر پاکستان روز سه‌شنبه دوم تیرماه گفت که در مورد موشک‌های بالستیک نباید استاندارد دوگانه‌ای وجود داشته باشد و تأکید کرد ایران همان حقی را برای در اختیار داشتن آن‌ها دارد که سایر کشورها دارند.
شهباز شریف همچنین به خبرنگاران گفت که در تفاهم‌نامه مورد توافق میان ایران و ایالات متحده هیچ اشاره‌ای به موشک‌های بالستیک نشده، زیرا این موضوع اساساً در آن مذاکرات مطرح نبوده است.
پیشتر برخی رسانه‌ها از قول نخست‌وزیر پاکستان مدعی شده بودند که او گفته است موضوع موشک‌های بالستیک تهران از جمله محورهای مذاکره بین ایران و آمریکا است.
در واکنش به این ادعا، خبرگزاری فارس نزدیک به سپاه پاسداران نوشت که اظهارات نخست‌وزیر پاکستان، «کاملاً اشتباه و احتمالا ناشی از بی‌اطلاعی است».
به نوشته این خبرگزاری، پاکستان در حال حاضر نقش چندانی در میانجی‌گری این مذاکرات ندارد و اظهارات شهباز شریف بیشتر برای پررنگ‌نمایی نقش واسطه‌گری این کشور مطرح شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/VahidOnline/76628" target="_blank">📅 18:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76627">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5_r044ELHUkDAcz2zJNWFGI7V5V_QsNL5PU-hJsK5fgA5dPoIrTgcwAUqrRbogjSXR8GOdMlNkhry4qJsbLjiwurjChblqTnn5q8OiJ7yp7aoaQeYImT3JBrnk12T9yyzSd9LyBBUyciAYvY7KcgGoDCqp5dX68eeOiDWp3fM41ZJO0AmknC_fozKptTrfO2ftrCpBqAL5xInvu7EliDxKc3nmH9gEYFLDnm5qOUyibKv6V_JTVIr92HcmG0aXYHW3QCaEIyhjXwW5TgKdSbRzuOhbGOAj89swftHk2M3oNIuKbqj1gx0b9-3r1gjaHFknkiOwotVA3ZmB26P7-5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/VahidOnline/76627" target="_blank">📅 18:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76626">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bQDskjYqEcxnk7j0qSDxOgJS1wEuXQjyB75BD0zOeYaw-UTRnvOSQNWa2aqOFet_OukPyhvZLDCCSe8eoiqdNl5ARd0NMT8HFm484G2BKJAcycNkovSn85DyeXs8BxzvvorlprWz_J2BTL33o4naMXWfEnhHFn74FxB3GH0yiuryg-e7EsBbY-8xUxvh0QJthmmPYTujwm_j29uXld-nIK1Lz3q_hHPts24QsTU0AmdOqxw6GkILWXtyIMBPKbLAbRzk_y_v6Q5kFi4UKr_2r_mpTn0NXNXaieuvxg_s-lh0h6YE4965o9eRXQSzBoCSz1yS_H_eL9NlHQSYUU0-Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/VahidOnline/76626" target="_blank">📅 18:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76622">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ja7m_jAkmLgNcoi0VpuFZAxG8JFXpI2U3TZWQEm1dRIm3tZt8ipQv3ywg8ax1NlmCGOol2FTKBtqhZ1Gv9Tq9ngD5OCDCrNPYFxilRRY9jEfL35z_7ma1a8Pfy2PRr_Jbdu_mGRESDpjhxxDzCfvlLNW3b5YtsdRYrtIl7nsEfH9ZR4AJL3ifoXcUTm_bu6Gb2crPBcxoSB-AZ0T50FnLjo0yJJra05C8JGg-Xf5xNTfQ7r2YKXZWP6cODZAyg32RsZQr_RZE8pp-Fo2ISE609MSEMxP65PBSE2ZYJkXKUDgz3hEqxN5iwQFDTImUyMN1nTKpLlwx1OB6gU6tbx_xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bqS4vzAAqgxtqsWgCCxswLO6C57y5-Yq6dNsZ6Zm8hI7bamrQDnD-fbV7daEzTUQ0IkkOHnKeUhBhZ35lFkJIFXMIHLStP3LV1g0bc_22cGRkYw4Y_2ajWoXUURhM8LF7rRMCgCukFnjPZbMXiSu-uV-ZGb8bn2kT5PnBYq77yCUIOjTnzbCj983YTQjUQqI7Q4QOXjqrh-glYKphhG0GBTeGwyY6pVhxyh6bRlr93WcdwRly9MF6YrRyOLhCyBUOyU2eitjfFrGz7GOTDTafAsUU6Q11zUVjDnbl6BUrzpZgfuBO8eqbfccwOiEpw81cxbL6qDsp6tfK_ZAlJH96Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JP9ih1vyD2GRQLLLwoh6w56qyUyC_czetc5bkyMDJ4In099nbpkd5_km1avUIg1ZfyZtj6Yx2UYK3V6YroAW3ZDjIbYeQCnKC0aC0w3yi6dfWVtRg-JCzzwDD3vBdHKlnEoWDATmJn07eXqXmmJjW9WQc0iDYCIzXB29W80zWVIthGA2_YIZ4sdBakLg97_vQQA19EghcLDsU1QcGI9QyRHyM2CrIW8pbG-wjt-Lv1p4B5ZiWuDaMQhGTcq5JcUFXwRyj0L77Mfz9wfwVmY9_VYm_IxCRESg4c3_Cy-9hVczo1B8qXl7526pX9y3xv9LEgCUdo39jYu_imxIywji3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PWGuGKLSZYPVx00Qk2wpfS4yw1JQvMKe2so0odBbWI1l60CFgG5q_BIqA_caM4BEy68hnvIuWW8ZAuimM9vjrDLPZwnWXZ-rmK2cFxvFKWSnsvpbpuI2-dI5cfwxULyUwLwb_B98W4I-vmCyB7rzlYeZOomKWPYk9rCAL8fZBQKib8E_VeEQ2hc6Imb4QSTX8DZhLeEUcbaJwI6Scl6A_8GZ15qBKO3P2Iq2Xu0PvDrVDPyFSj-9d5LejosJsye53IBrUSf0UDz1KGvhcg2UHD7fPnwvrP0UtpWM0-pO5JsUe0VVQ9N6sYTxNPZyf-zIGp19QrQnPI3R0p62E60n9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 133K · <a href="https://t.me/VahidOnline/76622" target="_blank">📅 17:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76621">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP-pg3NvJtBzECsN9jI2iTUiUZ1KCu--TEff-BYcK57jjpdQYy1KGCjucXhyZf0e5rGId8FK7lAPY1kIR6zBp2ze620ECSd8fauQH3dyiEoX9piaGtPe_lEtRLQNFfpKWu8jFStbCPVfhuBCdmzHjEv9bxOWIRkeeFiLgIJ1qPxuJwon6CVJNCf_hFOObBzxfGK0P2HMDK-7z9Cul9EEsg6j_SBsanF0n5ZVACZUmC6V-OHFXZ2tkBbcwb5SUaw7RsIWm8UD0c_Zv36d-xlz2pemfVZTmXQkk8Gs3OaThxgIWUb5_00GWptuYX_nZ6sbunspuvG4TsDbX-Uuo1G0hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمان و ایران روز سه‌شنبه دوم تیرماه توافق کردند گفت‌وگوها درباره نحوه اداره آینده کشتیرانی در تنگهٔ هرمز، از جمله خدمات دریایی در این آبراه راهبردی و هزینه‌های مرتبط با آن، را ادامه دهند.
به گزارش خبرگزاری رویترز، در بیانیه‌ مشترکی که پس از مذاکرات مسقط منتشر شد، دو کشور اعلام کردند یک کارگروه مشترک با مشارکت وزارتخانه‌های خارجه تشکیل خواهد شد تا این گفت‌وگوها را پیگیری کند و همچنین با دیگر کشورهای ساحلی و طرف‌های مرتبط رایزنی خواهند کرد.
این اقدام به نظر می‌رسد اجرای بندی از تفاهم‌نامه‌ای باشد که هفته گذشته بین ایران و آمریکا امضا شد و بر اساس آن، ایران موظف است با عمان و دیگر کشورهای ساحلی خلیج فارس درباره مدیریت آینده کشتیرانی و خدمات دریایی در این تنگه، که مسیر حیاتی برای انتقال نفت جهان است، گفت‌وگو کند.
این توافق پس از سفر محمدباقر قالیباف، رئیس مجلس شورای اسلامی، و عباس عراقچی، وزیر خارجه ایران، به عمان اعلام شد. این دو مقام ایرانی با سلطان هیثم بن طارق، پادشاه عمان، دیدار کردند و با وزیر خارجه این کشور، سید بدر البوسعیدی، نیز گفت‌وگو داشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/VahidOnline/76621" target="_blank">📅 17:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76619">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LYB3pXLkXO3ZcKd9UUDqzUprq-PJCSub0uHAXogsOBVd7UnobHyqr_gy12czqTv85agL3uj0EP6qA2ShZvD6M1gAGSA4zFql0H02PxIHNWuB1ra19Q7apWBm_kN3qt7am1aR8dG3ELWT5dcFwFqhNWPJFVU8Iteipf2j7iRJ7L-liDQe-ma6Icynud9c9FqNVyeHTL9egRkxndQnzJ0Zo1ZuAofPwd5wp4-siGJmfuXO1-a6IyA6HVZwz4-LanrEqri9rE80lL4nIlhRczEh0poquOubz3KxtjMidj_cHYSe-jeBPtJVSQkOSKxmF1MkArzfuE3DGUJ2VDeyqMLrcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31a8d92068.mp4?token=gvCAQL44LR_RuU0p8EoiFSvhN2mxJyylAv0K82OATxjCTxwOMx7POsp0DRoRIL9cN56qnvlgzEucHP00IXEnuDB6KmIKgRLC6JORaxJ90G52n5pdGE2BCO5aGgOhaAHuV94AkHsvM8KNaPKj2Rb9gvhxF8dR5DwR71ygMVZkLHe9ZKpUx9O7R9zPf9dCDqi1bJY0WoRLVPrjrYh_gUWYm--X4LeKhIZsGDuMtauqlZFBAXwfxN55JCoAnX10PLBPC4-3lvy_cXZkepJrcBdGhzr0nRTmSMRLIU1nZQDcKHN-rKCQWTVkmvAUmh-YoFXtaB3ZhY9RHT-FhHEmiYRKPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31a8d92068.mp4?token=gvCAQL44LR_RuU0p8EoiFSvhN2mxJyylAv0K82OATxjCTxwOMx7POsp0DRoRIL9cN56qnvlgzEucHP00IXEnuDB6KmIKgRLC6JORaxJ90G52n5pdGE2BCO5aGgOhaAHuV94AkHsvM8KNaPKj2Rb9gvhxF8dR5DwR71ygMVZkLHe9ZKpUx9O7R9zPf9dCDqi1bJY0WoRLVPrjrYh_gUWYm--X4LeKhIZsGDuMtauqlZFBAXwfxN55JCoAnX10PLBPC4-3lvy_cXZkepJrcBdGhzr0nRTmSMRLIU1nZQDcKHN-rKCQWTVkmvAUmh-YoFXtaB3ZhY9RHT-FhHEmiYRKPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 112K · <a href="https://t.me/VahidOnline/76619" target="_blank">📅 17:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76618">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F17QZvxP9UgBTWo2kE_ZMu-0Tm7OYRSq7egcjXGWprmIVfX9OHvYLFfz1wtOiJ4toDuVNOLhdWg9bXlxvHiGif6juh6jD5d9NMiimY_25xXRl-AD4SGUsRgTHnYULVnb2WqkgaQMdEg-mW6KuUTdJU9sgatmCV2ajlmyzhuvkca7c3iy0AJtjQ5OO7kPgm1RfWgZ4aCU-x2ByLGIA8ptAAiYRS1DpIyiadxHC_ADg81U5HmrooTfcpu7G78-45vqOjVbEEKJ56j_fGF2VWboj4STKO5gQuX8op7mXeyxYA-_9PrjayoqBaLGmLl636Tz-78vyy6CPzgrPcTlxe0g7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانون فیلمسازان مستقل ایران، ایفما، در بیانیه‌ای نسبت به احتمال اعدام علی صفری، بازیگر تئاتر و دانشجوی دانشگاه فرهنگ و هنر هشدار داد.
این کانون با ابراز نگرانی از طرح اتهام «محاربه» علیه او، از مراکز سینمایی و نهادهای بین‌المللی خواست تا برای نجات این هنرمند و سایر هنرمندان در بند، «فشارها بر رژیم ایران و قوه قضائیه آن را بیشتر کنند».
به نوشته این نهاد، علی صفری، بازیگر جوان و ۲۳ ساله تئاتر و دانشجوی دانشگاه فرهنگ و هنر در جریان اعتراضات سراسری ایران در تاریخ ۱۸ دی ماه ۱۴۰۴در شهر کرج بازداشت شد و «تاکنون اطلاعات روشنی درباره‌ی روند پرونده‌ و وضعیت این بازیگر منتشر نشده است، اما اتهام «محاربه» در تاریخ ۹ بهمن ۱۴۰۴ به طور رسمی به او تفهیم شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/VahidOnline/76618" target="_blank">📅 17:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76616">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IvSvj1vxa-EETvMOvCN-Mxo-Z5DahfWmGJ1r2ZnHOcbraI_130Xey8ki-g7PDAHEuDZqhPmWk5sQRe45kv5jnAJdC0deE3IPg4tNmwd6kHXZ_2iUpmG6zZLcpUDryBFiU3t1c3QD5XZsdPgX9dMHPVNX2c-PWYi0SYj_MU3AfcRJOfbQ6pxQfsqVnyLNNjP9QycUwzydbKYEwbkDmTzv4ONp40MU6sr9HW3dlR48esPX9nWdtZGZobRBwmb4aQ8ww9Xy0lyWdgf_NVH6JyCyzpj08ELE_C5aHRjQaWXU8NiXxrAEVGvwHkGXEvjLN2L1zuDfSPfhAp2sJXMCmAIvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/11113460cd.mp4?token=ngzWEpkcJJ193ucMcQK8E3aWFW2H5nbDD16-O3H8KcAESTcV8TD82DXcHfboLQr_zaFcKL7N3-5REr8oBCVN8jUaeShduzax5pXL1uJMbstjy3GRQC30NrYikIkXTimRw8Yv7cZp8TxXKNY8lBbX50JXxhJuz8g6oK7PVbBKJP4eGiqnX582Fj8N8fTKVZorGlo0ASNp7vnjqMtfBHXyYLdPOeHl5Bw3vBdUsfWlbgB7nMtXyB7cMN4S9mcPAJDKFx-tW5UI7k5GwhiS-YEVRGyDJ1NO9cMPXLaNqfhgHIVRHviT01Hc6Nc8X2q8orUnobYiDHcDWTIpEe2ZBl6nzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/11113460cd.mp4?token=ngzWEpkcJJ193ucMcQK8E3aWFW2H5nbDD16-O3H8KcAESTcV8TD82DXcHfboLQr_zaFcKL7N3-5REr8oBCVN8jUaeShduzax5pXL1uJMbstjy3GRQC30NrYikIkXTimRw8Yv7cZp8TxXKNY8lBbX50JXxhJuz8g6oK7PVbBKJP4eGiqnX582Fj8N8fTKVZorGlo0ASNp7vnjqMtfBHXyYLdPOeHl5Bw3vBdUsfWlbgB7nMtXyB7cMN4S9mcPAJDKFx-tW5UI7k5GwhiS-YEVRGyDJ1NO9cMPXLaNqfhgHIVRHviT01Hc6Nc8X2q8orUnobYiDHcDWTIpEe2ZBl6nzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 111K · <a href="https://t.me/VahidOnline/76616" target="_blank">📅 17:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76615">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ojApWp5xtJEwTsQbZH6hQMaXM2VmbZVCoGf9EXOo9DJCm815gdWmrmXWWmb5HpYy6kmf9T9ZZSI1B3k_YVInL6cFua8ZpMb3xEFIGDBGWedvYDMlCa04CzQp68dMzkJ8Cky4VEnH0GFzTFwauewjf9ZPTWDShtHlQ9jZ8fRU9RNFv-fcK0XdvUavvABFJ0hiyjxHshAliDYAUkGoD0dUGBgypdXbJ0i4bTOtgtkEndo41bkSXqaltKLJRlFSK6Li5sRifb9vTcaKjN7cUu6h-KvlOyCzXMWnQ4rZ6ZMSU7IMKioZCrxkmXpHlM6G73e0_iN8MYGZxhKl6AiXLxfWww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر سه‌شنبه دوم تیرماه گزارش داد قیمت انواع نان در تهران و ورامین افزایش یافته و در برخی موارد به حدود دو برابر نرخ‌های پیشین رسیده است.
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
<div class="tg-footer">👁️ 131K · <a href="https://t.me/VahidOnline/76615" target="_blank">📅 17:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76611">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IxIMmR_6BgbUJSOaxWvZgmYsH2ZfXfs1mV8Dg46kKa1BpnQ9lI3b92zaaHh1y5ktxE7ikrQtCxvmChecjAxXQA34m7cvswd5_9ea5kxN0ZpkbLFVIOWUHtzwf9hqhqvK8iPvPRkfZprfZHGtqglzx0obxWKpC-87keTin11dJ_FsJ-ZIOcZHoTHO3W59taQSZEhwZyIwh4ecNJ9T8FB6h6wK1Uab9mylKT6ZmF3w2Q6155JMBopSWQqVd7h7INSoFqU14KShUZJgdsyVG2tuMdQOx69J3DpW3Kxril4rorPw0LbapBFgbmJlwyC88DZ4XWtSwjb1Ag-2eQo3O0Um5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HHmnG9EyDcBMApT5-3y2qMdupC6pZem4oadxmc11gWCd_fWT0jpWdXKzt9H8WfoSP3Nh0hv-6xx8qMm5EOZ63ElaJeU4-EBOTG64xzeTrH746MPm17rvWhICjCWR37KUzEucJbknzfRtUsbDDSonTnEWe0ET6-g_N6J5SGvFhGJx78gWoHAUIAjTO9aqeWs45GtU-FUppGJIeHe2X4hJ4Ccq3XqAggd4VWKcD3dbQQMZQVOa2lGM2mp8fGqCSyiqcoxGSV0atp_Z4vVgiFxT_ziVPLUZzcNHnpAbkXNDZZbqdUr8P5eg3tnLsY044GxRVl1hzxiHGoFmyd0qAHfCzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TBU3tV9_K3zIgThnVZ4Dr_ThzGVZndOyWqUJyTfeqVd8cnS6pcTVFmFx2m6_XUpddc8btTHIU7TmJJoHwpfKn9XraQELCH1WV83C87OV1i1LFGqt-Dpq4Q_gI5y4KKwjlmJ1ezDisin-qlCRm3mX1gEMD5S-w4yVjXlMLLMHhPkNb_KqIQEDpQQ9hX4yS5904cm2IEN0gr6XLBC5Tuw1U6-Jt2Tp445XqRuZYPSdO5-PykeitLuzLIGI_rVlmFTt5iXQ4yIbeeCvBM4Fsc0f77UeHOZ96WXhWeofcxlXK8oK35235runOtQ5Rw5K-enWjLNMC2YeDu6djpz-Kxrq5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b0b4e3582.mp4?token=aUnLwqXN25PCnHssBU_3_4kDoQlzEjnwxReYpBgkV7M__fs-WV6jyNLPlBzzJRJD0x5JU_nqYz7TB6QWUNqn7yZgrXwCt1N-ya4qUpSUpIep7ljnDGZ2KhaptGyY16yOUMtF46cqPwycgYoImcZxmwxEpx7ZsCWTXf7aygFnnxpKpaKmf3e1ptr2-zp_3qhxrc9S-JK0FUtuoifz78O2Ie7_z71D-ZHU6BUp6MytysRSVauyTEOW1VDUXlS6ugnwAiFc6giAH1WDlolHisNbEdmIMAxqojobNyIxiKIbJju608Vgv2WWDujRwr4mF7mNvpaxaiIyAFXVLltXsPXTmA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b0b4e3582.mp4?token=aUnLwqXN25PCnHssBU_3_4kDoQlzEjnwxReYpBgkV7M__fs-WV6jyNLPlBzzJRJD0x5JU_nqYz7TB6QWUNqn7yZgrXwCt1N-ya4qUpSUpIep7ljnDGZ2KhaptGyY16yOUMtF46cqPwycgYoImcZxmwxEpx7ZsCWTXf7aygFnnxpKpaKmf3e1ptr2-zp_3qhxrc9S-JK0FUtuoifz78O2Ie7_z71D-ZHU6BUp6MytysRSVauyTEOW1VDUXlS6ugnwAiFc6giAH1WDlolHisNbEdmIMAxqojobNyIxiKIbJju608Vgv2WWDujRwr4mF7mNvpaxaiIyAFXVLltXsPXTmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«امیرمحمد هموله» ۲۴ ساله، ساکن شهرک صدف شهریار، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ بر اثر اصابت گلوله به ناحیه سر به شدت مجروح شد.
او پس از تیراندازی به بیمارستان نور شهریار منتقل شد و حدود ۵۰ روز در کما تحت درمان بود، اما سرانجام در روز هشتم اسفندماه ۱۴۰۴ بر اثر شدت جراحات جان خود را از دست داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/VahidOnline/76611" target="_blank">📅 17:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76603">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YzbVp-AXifei49CNPkRZMxhYmjlp87yW66S1Bjtf2r0f-UI_sLVfDyC3oPvM1i2VJb8gDIz9S_oDkrc-Y7KFP8sbdGZc-xJ4pR68gN502sRdaRqhC9DgO3MTu5MempbAhN4w9n7uq_hJZ27xPK8Zq3wB7yCPLKDHkf8vDpXshq3HWKvL02PQqbGEzfI9jBTJ9G6EmT2Q8sb_s353DPYkkfF0wNjTOEKfhW58Y6FT9WGGsoYNTLmIA9dQ9A1N90bPjIlWYWm5FhpQL8NE1ZZ823dM1edPiK357erYke9Lmo1uMGC7jZenYXOeWdyWBSclr7DjY3pE5-0oVP1kvyf0Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c0F1idn0LeceLCLvCOwEapGqT-nvSMUx6cbsb7k78ReKqSIoYxXo0WD5TXHhsG80YSTUaSC-5yKEoobpXCezbU2vWnuPmhho1el1n3x5JT11fq14UxrTa4VYHAN_c1QTLs6hRyYZN9FcuVMZ9a_hYMN58elHCXlXVW3L1rRmYfsodqsCDv2GJZMhLPcpLeIE1Mvny-XnppWggoPCophHSEGe3_6nfoqzaOjx33_TqGUW9rnLnSEkK5AtbhJ0JC07WK5wpVvZjjPqIiq0yKZ0fsb1sHiBJS5YXFxvdNrfAgJMR46BxT0mmsrF2BJIy7mJwXSwPu8s95XQuefXt-xrnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mYCVbNh74LL89B6HBjccXM9a9nuZEwiSpyGLRITzB7XFfLrwQxGylWOl_uI4AEKXaxaBM7hnEoKR7Hp5hr1cjAiUN3NITnY06dVferH0pXBdTsXQm9vvehRS4qmLOR57rt-Crmspt6_GMl8IsAaU-8L4M1U5jKYZidCKjKCWc-qVCgXR4M1UDrM8tU0TUZH1Ypk7XWS_q4EPvUdakmVH8cw2b0saeUYT5wm_JXqyylK7397lN42yEna7s8KL7q9-xzdQQlVS2xa8H-hGCngxss62JUBcHyes3LVRRd9NB9FbzuqUVPLDvT8bvLWZw0ndlzhvWHjvTeoOaINHp1SwxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZhJsEV7O6gz2cZSDkULi4E-OBGdEUM2bLvEPIr640arpKHzupqNwnEpiAy_guFROkKFY_3SxkT-IzVo8HBzSfGf3ZdAEqFif-CxKy85KENYrkW9AMxNfzLfTavKstAl6HlsQptcOJ2jMcpSSCKUwHmS9bj9xEKxwCSmyGTk6ioeljTODxr3mTJJKcdXxknxiAb2Twd0Txh8UoTqQ68v7JF8KfUefO7-SLvC_aQIlFmf9xldDxRQLsDJErgNQESy1wMhqqeV9GvC8JqP9PJ2gKgRbDQMmh9q9upTiiTjCBwJsCDN_LXKCgC5hZmXjoqbjJVRFwtNz2Q2Wk2uu531smg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hwcCnyR3VRkENX98OlzD40QWcNfdxcRsMplFjeEidAuQJki3zGXvRoOa143QyDw6UZz6fhX3JyhmAnyCTzxb9LAc_jI82Ki5gfVa8ECpq0Rs3Ta9GqXZzcSQrFa0svZYBdah8CnymO4QAOW71CWXJJEsU-3hwD00ejM_e75N6Etlx2j-0NbpdRiW__zoOkcMYaqvWdyM7NCAEiAmB6q4NUA_2je8ZjEuuRqG1PADpnOqFXiks3RP8a5SkcaG4a8NVpw8D3DGKd4OX3tvvNg7YlTNBmHFuYPZaJVnO-mJKai16l8fo0XcpsEspmgXbUoNxrMCBJhY5IXtcUSknQnvIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S2xgY3Ogg_TWHYW7ImIQsui6q7nTizBsCghDRnec0C9g4-CF8VnN7eLMP9Bm83FNjoR9fCEeOuh9HWZR9CUOK_zvjUbe8DnHTB6llxk4vOxOQoEl9YezwA7-uLvHjoK_Umu99WG7nE30OCXFyStOkn7rGMN4bG0Wt2KNjNejsQDzo-o9nZpjEk2JgL6maKIAzCQzzI_DfStnyBH8h4FtYIFauoa1oZ0DQJ9A9xM52FS6qjsBMmvvR4wEGupgpPFlZptvtJ5Vq6TGQpiNorAG_8sSa-z-tsoMzps5C9Rs_lOENOlXTQFR_Cr5b0erA_Rv1dI02O8XVfgxX5j1R9pMUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iRvM_fgeikUXVI4dPJrF8-FW7QMCojYug0GJCGnibt2Fmuvny4qyiYHMnrnD1Lt9hyUgGsXcZui18oMmfPD9hAkIRBe_AghHdJVfcUznRurGtQP28KLOHQdyY8J4BfKQLrP2oPUylcXIsdxB-PEXizmFHVbE6I0SZpRBG6vBvZy59F09PVtf8oS0U7WVw1Sqdt3ELOFEtdi3Neq1acFEpITT0kcJOFj1Ksikg2L2fbFrAfaKVsH38Mi0i7lW5LBYI3eo3w7947EFGojE6NdSuauUwRWxjj0jvai1JU0sOx0iQ9cylgnsnKNQbLAUgw3zYwmgJrGximxwtfqJnoYgXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n15bnOGiIjbxwXZtzf9VzgkPQwk9LtH9B0mN9ubuevR0ONqc20OuaOpfoIDeor_gQRyARv0wXEbH5XSoPwhr7M-7em-onf3GTDjtoOu40BHXgdDZ3U9NbeLp-qjwiwnZ3uAZnnB3Kyw_INCcPmQKlrhwYxzP6g7Tp0FaK8f1Ni5toxYpYgGUtKumvuD0qCNqRaq04zt4Usr2Z6wVnokfPjll7no6Be0OGNoOq9UH0wwZrtwtbvtRYpX64D99jdFwAYjqMSoAn-VHgx7eFD5OuO3P1ykASKrAQIKJ1VeB76SdiE4HRFUSiRCaxw0fSkhwqS3h_BX296PfofrREev2cQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76603" target="_blank">📅 02:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76602">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WavEG0ZwnLSuuKPxMbC2Fp561OSY3EBz-Gn71zMQurS0qrLZDZ3ZVpyv9kOXW-w3UBLhuklvO_ZehZkyBnxQ7aetUS1DpNmKpnOInsx3okQS165Vm10G1ihUZSNfsq5TnrT4HAKl7pAD7JKDxwAG5TSO2Gi2nQgjXtkSeOtDITiwBCClC70u0qSZzPlW9TfPwoTxN4bRDt8vtWCKPa_S_N2mYCoTwyai57KjP-hr6LrmfIX3iwlufVUFlcVOB13ujNlAzRsDk27yRmQHN1TjwMWstCcKYu7J0B3LywKg3ZTf683N2H-ik0wPax7MiZhhYvxoQ2J2WwuMr_YEXABYGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، سرپرست تیم مذاکره‌کننده جمهوری اسلامی ایران، در واکنش به صحبت یکی از مجری‌های صداوسیما با انتشار پیامی در اکس نوشت: «در یکی از برنامه‌های صداوسیما دیدم که گفتند کاش فرودگاه مهرآباد را می‌بستند تا تیم مذاکره‌کننده به سوئیس نرود. به آن عزیزان می‌گویم اگر به سوئیس نمی‌رفتیم، هر لحظه خون بیشتری از مسلمانان و شیعیان لبنان ریخته می‌شد.»
پیش از این، روز شنبه، یکی از مجری‌های صداوسیما گفته بود: «در کنار بستن تنگه هرمز باید فرودگاه مهرآباد را هم می‌بستیم تا مسئولان برای مذاکره نروند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/76602" target="_blank">📅 02:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76601">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76601" target="_blank">📅 00:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76600">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=Z3HTDLxNUobIWaO11sZJSnA3jDTgTs_aMT6jmg_I1V_n0kmsyFsgu1_v_flWYchlxvCgUAn7UzR9BusNnmbQhR1ZIbdTx8Cm0CzDyDqoxmuG-Riao-5t01uphdko8tODiEZt2nMjDKXWxlGuFZGcuG20y23p9bVMdq5hdP0wnIC-SPEcNhfCRWKWXw17Oj5UZAD18ew9Wo0EaGa8IBDQj911YB92CtZ2vV4uGyTY6rWpRY_IUvS4SCmCNrvkeYTkECK93lM0FdVfNHCqww0fG8R-ir3me-sAVw9vUTmpLEBJPAd7r06NXrshKrrERJOX1ifxIM9zbCBE8eSsJv_mfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=Z3HTDLxNUobIWaO11sZJSnA3jDTgTs_aMT6jmg_I1V_n0kmsyFsgu1_v_flWYchlxvCgUAn7UzR9BusNnmbQhR1ZIbdTx8Cm0CzDyDqoxmuG-Riao-5t01uphdko8tODiEZt2nMjDKXWxlGuFZGcuG20y23p9bVMdq5hdP0wnIC-SPEcNhfCRWKWXw17Oj5UZAD18ew9Wo0EaGa8IBDQj911YB92CtZ2vV4uGyTY6rWpRY_IUvS4SCmCNrvkeYTkECK93lM0FdVfNHCqww0fG8R-ir3me-sAVw9vUTmpLEBJPAd7r06NXrshKrrERJOX1ifxIM9zbCBE8eSsJv_mfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/76600" target="_blank">📅 22:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76599">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W-pf-hYx6A1tYt4xuMe3aA2h1mscXpeK_Yf9W_G9nlLdk3UGNpc69h0pjfprBj6bVgl3Qmc9a6LQaRQWckWqIHV16NUxTNUCDI_PHB5sDStJoOiFO5otyxQ7UqdaC_t9HWJAm8UmTd8gYf-jJsYZ11Otieu2IvdVUo8IIrww25s02C6CFZbeobK6mrgLfAy-KGC571SjBkj7wosaNyUMgUivZIr4UIuvSMQHE7pHfwbuVlw6BsWPLMIAUcGWFwC8dScQFVyI_0LTIuTWF5HBYc7BVrAkR1v4UG2OwYha-taebMJ7Wz-qWGKU5kCyiWXNM-CETdCbuDNalPfoA1kUtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
همه کاملا آگاه‌اند که ایران موافقت خواهد کرد که برای تضمین «صداقت هسته‌ای» در بلندمدت، بازرسی‌های گسترده تسلیحاتی انجام شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76599" target="_blank">📅 20:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76598">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqO49Xbvs8_s4vZvhFJ1--6-2thxXDx9OKUuUCAUEG1jlUmMj2se4NzjbglFkJHJUw3HSDxHSMdOOYnwsUR61YXoa8vCh7WX9CeRUkrf2U14ac6iC2Qaaj6vjV4CbJ3Nj3BILwWftMCZilcOA10FJIQDA0DlxfKYm3ByUxXdjltDc0kLVhxqJe5s9X6H3buV_qH7y-ROzLt2RLlPjtcXYLBGOqbj-SkRA9WTEMu0yPiqpW3EOsmSuTAvAwQydyOQIQoak5apCfNXKnomZTVx4T3tBDzF9kLL5BNyn0wJG1mwpffT7wKbTzBLyh83j4qI5Mc8AuK-9oCS5Qt57RFxhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز دوشنبه، رسانه‌ها خبر دادند که محمدباقر قالیباف، رئیس مجلس و رئیس هیئت مذاکره ایران، که تازه از سوئیس به تهران بازگشته بود بلافاصله برای دیداری دیگر به مسقط، پایتخت عمان، رفته است.
به نوشته روزنامه هم‌میهن، قالیباف در سفر به عمان به همراه عباس عراقچی،‌ وزیر خارجه، قرار است با هیثم بن طارق، سلطان عمان دیدار کرده و در زمینه ارتقای همکاری‌های دوجانبه و تشریک مساعی «برای تثبیت ترتیبات ایرانی»‌ برای اداره تنگه هرمز گفت‌وگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76598" target="_blank">📅 20:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76597">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l4V87FsK1vXXAfzksFMEWts2uWYNfIHa9dkUxNbwfHNGqg35Ee3YEhpTwDItzPa54NTiLLIprJsT5jrlayrqH5R-PcOmRV9pAvKuPQ18xo1TpKUqW73ub1KXqmDRgSOyYVgAcsH5srThM3aAsyZGJfA4b16CqmLdc9YY1EqeFdlJFi5vZ98p041_RS-NcJosLlp1KvOFx2jpXFmFUgawx6S9Xf0285t-b9XvXzP4aIWPgV6Tvc7VpQc2hKfbHMHPMaaQ-unZKDUoGVuUPACAGc5QCaESuBQxPfqeD72EdP_TVkZ2h5whQi8IvcaJKUWNg5LwsYyurUBytgYH8JP2tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک منبع آگاه نوشت اظهارات جی‌دی ونس، معاون رییس‌جمهوری آمریکا، درباره بازگشت بازرسان آژانس به ایران کذب است و در مذاکرات سوئیس هیچ صحبتی درباره حضور بازرسان در کشور نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/76597" target="_blank">📅 20:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76596">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f94ec11a35.mp4?token=TVAJC0K2VwqvumDVbxRdexPzpD-6WX_cSEXlQg3RI3RlKVgXTRNLX5GndUur-fQGK6DA2_3hhA1AFU4RSZaBdkonJ1qy4Bum-A-oYv1PTg130Evvh96ienVr4tGcarS5CO1dJFITrHRXrQ26fINDqwRif8iCtE5gwk4QIda2G3n6MCuJsvgwn3CRDUyq5gqYroc0BYv3YGgvFyKX3KFef-e5SbdQ1X4qpCCrZ8v6Ev6IQF2JYo-LDUerHByHQQQhTCwd4-2SDa-JOao1Vs36dCOlWPRJCO-z7imUQh2rEulXKfruoB82LvfFeQmtQq2g8YA2DffwzfHXDcSR-P1Q1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f94ec11a35.mp4?token=TVAJC0K2VwqvumDVbxRdexPzpD-6WX_cSEXlQg3RI3RlKVgXTRNLX5GndUur-fQGK6DA2_3hhA1AFU4RSZaBdkonJ1qy4Bum-A-oYv1PTg130Evvh96ienVr4tGcarS5CO1dJFITrHRXrQ26fINDqwRif8iCtE5gwk4QIda2G3n6MCuJsvgwn3CRDUyq5gqYroc0BYv3YGgvFyKX3KFef-e5SbdQ1X4qpCCrZ8v6Ev6IQF2JYo-LDUerHByHQQQhTCwd4-2SDa-JOao1Vs36dCOlWPRJCO-z7imUQh2rEulXKfruoB82LvfFeQmtQq2g8YA2DffwzfHXDcSR-P1Q1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/76596" target="_blank">📅 18:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76595">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/smt70yobdCPMKl6yhBY30ibFBr5bHoLzdHT-6xCeMxiUNFGdb4DPJkLfI3tSPLqfCAKGYQRw4f1obQzi_ZKo8BDqmUq5V3kzm8jl1rA5O2Jan7lMRAH-mTZ_FECUVI16fJv-F-5aHMIeeZYOQOhKsflZJ9W-RCm6uyOt6R3wdjTIC0h9iQJx3BxVJ5CQKf932Z1SpTwpkdbDd36-U2JLtx_8xda8Kkg3EcYlqtmxAsC2ub7_LaDaumvdFvN_R5R641mQubBl837MvMR8l0wEb3CJh375I0VXjc4YpC7Dno-4Lxo_uBVUPy1kNfJ-sKsrDSpBARjuMEUPagpAWZnMXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا با صدور مجوز عمومی، تولید، فروش، حمل و تخلیه نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران را تا ۳۰ مرداد مجاز اعلام کرد.
بر اساس این مجوز، تمامی معاملات و خدماتی که برای تولید، فروش و انتقال این محصولات ضروری هستند، از جمله بیمه، مدیریت کشتی، تامین خدمه، سوخت‌رسانی، ثبت و پرچم‌گذاری کشتی‌ها و عملیات نجات دریایی، مجاز خواهند بود. این مجوز همچنین شامل کشتی‌هایی می‌شود که پیشتر تحت تحریم‌های مرتبط با جمهوری اسلامی قرار گرفته بودند.
در متن مجوز آمده است که واردات نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران به آمریکا نیز، در صورتی که بخشی از فرایند فروش، تحویل یا تخلیه مجاز باشد، امکان‌پذیر خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76595" target="_blank">📅 16:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76594">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jjc_Lro62NXQhk3YCFMuMJ1D2wPtoVhOgh0ft9eJWuvfhvUWRpyT-ERfP6HUFLJiJYVlVSbatID1-Ik1zNhfPnlA-NIvz3iVIFA55_7gzNTe1uDPqhQjHApuRX5kMIIpZ-83MbHjpElgPphLOPjky-UrN2wojdWWTmANZHbboDa543A6rjCOKbb9faYyxrxYHRDv5OIVRaBVCHVLCFLijHG6wypvzDEH_zakXNB1g7PdubjOI-F4Uca8Kt4kBp4Sr4GoYRSbeQLCHrlzMdwtedE-3Wl-qbczYMp9HDxKRW_8xt6AOWchVCNigOTBenZdki3cxgT8o5Nv5MWaRnqhBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس گزارش هرانا  در خردادماه ۱۲۷ حکم اعدام اجرا شده، ۱۹ نفر به اعدام محکوم شده‌اند و حکم اعدام ۱۲ نفر نیز تایید شده است.
هرانا همچنین از ثبت ۸۰۹ مورد بازداشت در حوزه آزادی بیان و صدور مجموعا ۴۹۳۳ ماه حبس، ۷۶۶ ضربه شلاق و ۵۱ میلیون تومان جزای نقدی برای ۸۰ شهروند خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/76594" target="_blank">📅 16:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76588">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jGo_4ZDuhHXQJo16XVV67qb-_noCFML7qLf3LWDUfhyU8wxQc2c6DQN6rSiMmyY1j_6X4Hd29Qclvi004UHdRkk3NhQ5CTTI0BHK_aYH0A9KUHI__DqElnHTfvF4k9mLBS_jchggUPGTO8wz2q9NbcTfrXnmm06brDmtaO1hF8vR5thUOktqJb9BusdcfLTLYNtvR1J8kiTbHDAMVU8jJsWrdsAkomD62aEN1sNkgUfK3RU2NX2Ajit8Uf6zoaIW1lA7Flp9MUyNYVJa5_rCeHwgOjtVdjpnyjG1Sxps-VG1ZeHsrw3I26Edi1Urh-Ld0DCNzWMEqou2XyahZta4HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tLZRMCh2aAyKR4VBnt0UVc-_f5CFMOSvc1Y_oGMglucnBP92Nrp0J3wlDk-BH7y1sHB9r4j5HrAwsKlXbFcy1UiRRZj7h7mnPs6PVnZp3DVuoxD8gJHFwMWSDJ2mtGvS6DVQLILrz_tMnKUQAlF7tXnhu9pppeJKyFzpzpK57YYlw6o573pGwnKHJvCqb4YUaY6t0gFix1IaPlSdDzxKqRVZ4JeQoCccUuSdSvlseP3mt3eMQMuWhaz_bThlYaEdxScsMhUcucmlggRBaXkreTPev3tLzStTmUKdfJ8Po7oabZawt2OhaeoTtw5GGZUk_2uhFYSEi_81xbtntMQgfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kh4HKYpZaSGRgd44bQEGwpzHV47m3pSlS8n35BdxtYN4jquHkrb6r7B7G-_IRqF-HVyJ0BloPsy03nm644xzz8EInhL6jT3P6FimD620kGjhC-BzL4YxFLYi_Ua3eKbDifq7ZVfkYa0y3TVcteNu54S8rpSquD7VaNJOiPqf9pkQbFuyVI5J7xj3dBnIhq2czL-yJSZqNhUDmeysVyHqxPurB5GOXYQWenKHKv9jBSbi6d0NRMVoZFMFRMFTUfpBiddQ8y9fnbpFcndvEs54Y12UPsYczKY6XM9DdJEXv1zY-sMZCVvflmGT1xReJgOm6xFNTYgIR0KQqi-kcE5W4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sHg46OV9_PUuI_zLY9-iGJkcKN6ty0nLqpZzTpircTei4eyhVRPnxv0-QePkNB8dl1QXX1fT9BErwDBP4HtT9_LJV21lpqXNT-YNFVvwYyloTKa4TlIv6xj2wSW9lgLrkYDjB5h4AIvrlNfizq-IWDNwJr6DOmJqdmlO3vxfOJzWPTeJWXLiXj59MTaRD0SW3tN9dE_CjTQsqhL48cnn1MbnFa9hApfDr1jRwd2ubz04zRZrYvXqGq4-p_F7JGnP7vS7yw1k5y3e5xS9M_nQAxcSzgogZwhdVE-EDlOplW416lqBEMinCHj2dBgSJ24QMFOmDIWKp3lr6qRf2UwGug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Jobra6NIZw705gXlF72CLFIYsrWNx4Nfs2TDJFwuGp94R4NVDzbHYVulqoWIHkZoJyzZwf_BQXTB5hsOv3LQSG18iwt4B_-3vFJKvIGJ10wgDYBzkraycGeMpidPBAqSeW51mz5McZzEPzpDCCKU-xuTjlgDu-5SPT9I_54yF2_Jh_lkFebROHzvOGSUHMs8qYqBILK_k0FzyFuTjjWR-9SlGUOGoox-OzEjOrA0sMFSfHxdMXcQ-r96QI8q2i22Ft2gw4SOXWco6SMgpWQzBANjrAgtMMG_AiZ0NKU7WfgDizbuOIzF2IlxRte6qdFKKDto6O3MqbzBSCazsnnA5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a45f8c601.mp4?token=ptjjtl8utP4sjj6EB2by2he25Ci-sxRDFjuefCdte9LzmpxWoUdR1aKerYeJX_MP0jqbmc6JCnM-AGvB1VfMG8X5-XCFzu_ShL06ua-byrsm2JCK7I2ogJm5RjP38e5FA5L8oc3jAmuhtarKRMuXgJHg7MCioupB7XvfMV62c-4PkZswvD3g4qpDG64ksCUlw423cZ4vZ-yQyEweCIr6L0C9hd87kNEah28Q1R6JV9zBNm3buMzup4KSfjAy93KaF5kyQSSTYFG6bQ5KT2JesGfX3gbaeTKA0UNrvm9y0L7tpZnUDwBzO1aY-7q3amfb6_MmoPL7wTo9jlrIyhAvTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a45f8c601.mp4?token=ptjjtl8utP4sjj6EB2by2he25Ci-sxRDFjuefCdte9LzmpxWoUdR1aKerYeJX_MP0jqbmc6JCnM-AGvB1VfMG8X5-XCFzu_ShL06ua-byrsm2JCK7I2ogJm5RjP38e5FA5L8oc3jAmuhtarKRMuXgJHg7MCioupB7XvfMV62c-4PkZswvD3g4qpDG64ksCUlw423cZ4vZ-yQyEweCIr6L0C9hd87kNEah28Q1R6JV9zBNm3buMzup4KSfjAy93KaF5kyQSSTYFG6bQ5KT2JesGfX3gbaeTKA0UNrvm9y0L7tpZnUDwBzO1aY-7q3amfb6_MmoPL7wTo9jlrIyhAvTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/76588" target="_blank">📅 16:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76587">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dkb6XBY_seUwyknl5fEjxR1xeIb-FzkO8Niw7A2OALHoYEjF9H4Cq_AeAyapDYwJQ1z4BzDATeV_0gf7TZa_LEjEz8-lhtpJ8r-8G_aA31r8OnUkpOvHKKraziCljTBF0U9YxgZQF-bVcUoXQae86u03lXXLGomC4MHIv3lsCcNOtRiIeXOZ_jkV9wT_zgc4CadmYRoWPXPa5iVK0Lar3axD0mMiDS1MkeT8dQL7oc7QzbGz9Z67OT0cszqOJW7mJAq7O94xmoah04o_1mKz6Am1uPObbvW8snC7cu0vuXVx8V5cZMelEA3FM3BfxR1B3AanT013A-OhDXmgYWGQsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میانجی‌ها اعلام کردند ایران و ایالات متحده روز دوشنبه اول تیرماه توافق کردند خطوط ارتباطی مستقیمی برای باز نگه داشتن تنگه راهبردی هرمز و پایان دادن به درگیری‌ها در لبنان ایجاد کنند.
بنا بر گزارش‌ها دو طرف از طریق تشکیل یک کمیته عالی مذاکرات، بر سر یک نقشه راه برای دستیابی به توافق نهایی ظرف ۶۰ روز به توافق رسیدند  همچنین قرار شد گفت‌وگوهای فنی از همین هفته در بورگن‌اشتوک درباره همه موضوعات ادامه یابد.
در بیانیه مشترک دو کشور میانجی یعنی پاکستان و قطر آمده است که: «طرف‌ها با تشکیل یک کمیته عالی موافقت کردند که مسئول نظارت سیاسی بر روند میانجی‌گری خواهد بود. مذاکره‌کنندگان ارشد به‌طور منظم به این کمیته گزارش خواهند داد و گروه‌های کاری مسئول موضوعات هسته‌ای، تحریم‌ها و نیز گروه نظارت و حل‌وفصل اختلافات را هدایت خواهند کرد تا اجرای مؤثر تفاهم‌نامه و دیگر مسائل تضمین شود. کمیته عالی بر سر یک نقشه راه برای دستیابی به توافق نهایی ظرف ۶۰ روز به توافق رسیده است؛ نقشه‌ای که زمینه را برای آغاز فوری گفت‌وگوهای فنی بیشتر فراهم می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76587" target="_blank">📅 05:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76586">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cZdaBN-VeXuwTUuWIlFwXwPt7baDt8gwVPHjwn8voiv79bLT0A9eHCqWZu4ExhG8GVdQ0BPnwshPQcJTalE7yJFcJjS3wlYKXcE8lD6TYkbTRhl3o51xc9wHTPWvy156PXhxZwIGeEE7Uo0_ZcJoBNV89jAd40BZ9NSCtFJ27Q8uLlyenelfS4UdLQyVc27-Dn0py1pwjMk20fYHkw2uK9YqaHq30OxiDl15WLKnRyAttD8wA4kbfou8_nG8HvCblSveBQNI0DNATCRrkpyoN45sJiC4eyatiAy-75ERw5iz64OBAUtu03bJWlLtgl5T7viVSRnWLd6FqcbuFYZ5EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف با فوتبال، ترجمه ماشین: ما این‌طور از سرزمین‌مان محافظت می‌کنیم. mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76586" target="_blank">📅 05:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76584">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KLh0Y5uaYPViWm7jcdCJvsL9KnaKk7yTv5cLGF4G4BbKT1sCHDP34h7ucsSIMyxszRzblSTulCVA_XebAbuzHPnhb3UgRBvUgG0zwSugNljU1dgxx2G2Xgv9ZoGcfzkm-jhAn6IEuyCqsaQDL1IokSJBkTD3JH0_ZnZXTsHRtXetg5sfoYJh_UJXH68fdv34lqfNVZz9mk7qEeTz9Ex39oFXGF-Ci-7VkikOYwI6XDL_xxp85s-TchIfaftr4c5j9y0ROBKwAv0Bwsyvg_ITKpsNzQbLANYaXdqJVhf6unuynWt0EZP45m4LHpv-aFVfuBOUX0SkUX9JyTJiIim4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T5H_VGRVrD7vxsVirQ5SONrQLicat5Zu5klQuYQA1g0OQls0M4vGTyjLgkllq9_Rx4BiZwuvteHFemFD4hy-nEHipFETrcPj_2jqznpz1HdOGyMHBhmi-kwO8E3JZoAV_jaS5M9j42LQ7jhTN8nye0Xl16BYom6RjlmqadU-yVCGT4YyKqIZ0x9dJ6wp0EjUa6zHKi13I5YsxCsvRGyCtCMJz4iunDFhOnzZL0jzIehsYPpGUMUkkqDU6HODzqUPlxlmxWITONwFv_390QD-qUN-s1TqlI5eeWPwtnvBAUnRqZt-CwlVZmJG0th2OU1Ju7vIjGGqpJvMmerITBmgMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76584" target="_blank">📅 05:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76583">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aI8DOsDGTxk-yNDSOsHWluVL38NE6tUeVi00tB1mekxBDwBiVFtiWPuo1lHr1hVTKhWBrdhyBOx49H2ZbmIUFaYe7sGcHre22YeCd3OcB855B918GgrUBelqdWMUc_L5d02LOn1pE90zJ5wg67H64ul--MAofQzX8dpAI4bVA8DOYz1vbwLE-hFQm44zTsEhFpdhwHwtCAN4Tdqi0UYYqy80SAfhXayRZ7T98aAu_eVRzpXAww9sICb199xf1qw9Ges03psjpmx-uCVYK7L3zoRrRbXAsq6X8c7BurImJyodA7zNbBS5xxfvZn9XNYSktflMII39cHzMt3Kb-R7NNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/76583" target="_blank">📅 01:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76582">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WC2Ap0Q57MhldZgntUGcAyol2BUNP0l35OB7cVxHIF_cKbBS3sGhHW1hUXY40If-7d3fvk3oSi0dnuZlO6_DsfBIuTHppzKN2SHbaqYRCdr9lbT50mNDovgOhr03WHai7GReppKz3Z-WS-Un9hSY_r1gXOPARv10DuhpioXoXSE-jF0hn0nDggYgpdkvcdRhDzqttscWbYmTtOnoceJ29Cy0riGHCa5ERaCcxVqWtW4V2czIP7bbaE_z-5286kqV_X25o8PgWw0pbdjjHLaQvDsBovJocG3CMgUvW6_sWOPv3rTOm1Lf5NdCEPv4ULi_sq19QY3m5Ka-lhDK3lGLYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف با فوتبال، ترجمه ماشین:
ما این‌طور از سرزمین‌مان محافظت می‌کنیم.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/76582" target="_blank">📅 01:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76581">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/obz810yIheyrK0yy8Ykq19wADD41b-jomhjTxL8L9S2H2AZ8iSo4sfrcSCZnOtH8FJ2JKPqqQlS8y4GmEH6xmirX4kc4yp49sn5hr8NFGPBaIyEW4hnhyPTzkzFjgRjnHfNKVJaENyqbw_wR7u8Ci8PIv-b02zsKjElpHL-eW3q1K7Djuy-CZInoZHqnv8kLec2Jcb3HEagZgXVGx8o9ZDn7gkA6UUSyvd04KJCYeEjQKiaxOmh0eDzE8d0e_NA9iHhwf-XiCDgv7Nm4yB_6GAKbtACGVrHyu076NV86kR4ARcksSH0wBBZNGMPfWuy4eSlYblYx4RelrDoy3888Yg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76581" target="_blank">📅 00:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76571">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eTFNb-_qgBTfg7sW3mhUvnAGY51LNLG-_fU64kg6AIpP9oOkJ_XCAGsMwo3-VgZCjjuVkFdO2yzcEJoC89kOdnzHFMAPCbw9Q0ZvNCqggTCsCBisDuXd_NpGoIH3Gof-QNZRtqycpymp-D2TAZdFA1bzQKA34mj5vzUyZZlcRmNTlFwPujIXzkuxYZZn0AxpejkABrKoEC8HI4rLJ91vE7bpyYv_rQbBrOP_D-MnX7zYMI_xRgc4jgaL0UWazdDopzWwTctPhQdQZREAlOWls0Ty7w3ZWPDFNs3LMb_NzJietwAyeRyyqa7cq60VHrhvEGfVv1odGvb1TaLk19ArUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GG0npwgv1cBTAo15eG6-WEPeRQ5RkzyxAO1_Aoe0fBuiovxl9o39jlsM964KlplED4kNYmBywPX7mU7aEKa4unaQiztNQzcZXT0iXnharThrFgVHpIOegIrgbOCuuTVOn7-kIGvetLgKlT0QbxFw7RDhbzYv5ch44D0368nch_w0wzoghrSwRCOafRjlPFvw-Zg5pTX1j8Oxk15gC5l4aZAqrf6Vyf13zbfjuQgtyKRSVXmQfEOnBIronT7jJISeJJD7tV8qvsIR4WnhSYY76HupB1rJbVA54kGzV0Qz2Ui1nlqT3DW3xSucpou8NOiJyVh984ZgnJ2DK_VGkxLadA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EevuOBGbDHDFkaM0WoyEra3_C3FdixEGhibeaBVM8I9QG7gVxTD_s36ZFFX1z6nC5xCqMnyXunCWlmjO8_K73vZh2UKl9wXimCKtWMZemQOYin2zrASGEtW6nvzrmBnC9_nBplR83inblizsAiJexJDdAANTkzj6Qlq_8SSbi4s2edajJSu7AdKRwcmWnCqRU81nK_oJazGAqzJRkJVn6cBM2TmIlJpmaDeddbriJLFfrXGct3diHy0X3Q3GpG4oWvJD4-zkrksSfAfm4wWd5YiysDrfbnbx5LUTxVR_JCvVDN0Sl4oQfjy--LjEJGee6A0V71SdOq_N8eeOrw-xDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qLNe-MrIxdvPytWaZiyia2Uo7mP0N_Xf_L19itTvA7rnTtU6_gBfLWRANvml2XJlLUGme8fwdzU6vWTorepGK0Yim5UF4T2OyMQcD1OwnlqR_welKbiV1b3oWb6D516imIwQxwXGJcv4vW0G1_9_p_ojbHqrobToomMTZGuVzme-jpr6JPMxBIZvzSUe7PX84zdFtFjWL-M2Q9oKp3qU4HxsigIUCISH96l4Zrw6qRAQdoUBk9jdjBU4514Gat6pcH6gE3NBsH-e_vCNarowhxzCYAQlItokK4qGv1bRpRPVzBmlbEtqH5oHAAp8CDUjo0pw0EALzawNbFYoTQ0HXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d4Eb0lXQDsSPOTUpchIS_3M5Jaur-5GlGe78BvA7kv-l6vSrwAW7E9FL-t6wC3_PYU2hGC4IMNKZl_3YJp65dRag6svt4QXPlU0tU1w0G2JUw7CHeR8cJkRmyOk2_HzCpvwXGrTJgxkHYf15zGHISRcQ7bfFOJk11EiAixtvMNNPQloPL8_KRNY0-y_AvcXrLMfSzeqLTd9MymLEmr2-nf6jcGmvvJjdaRHW60OZM_A4aOaQ2Oy1_s1wstYXtDckCIbzXSYSm9xl01Zxu8Af4H9DzqTerix7MmsJOD-6-abKAeadIzVnZnkHxpXNAHA8K2AgTyd2hhSDOXdbKX4tVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vwLzbb5yA0D7hyWRX00mbiEOfxXGwERMICy0DCFUt4Lg4HQyzEfOb0zD7S4Su_e5P4EmCGY2wDgL_GiCDqkYCF_PD-Eh1GevtuNUMQik22wQXjdMBgu5B8Ja66_1MgzW-A1XVanaEugp2m9HCulHEO1uvgKueOajQascaWhCguPP3QeKrgLXxkXJCrx5zNdpDsqAbQ9KQdnAy09Ew_fWEpHdN1NRFOogbgxpJQlj34WT6ihFoLmO-tCgQC0CGK9wydFGK6NB4DbvKB5S6UR7x8DFK3OCKdEnFdx8gcCPTt_BkV-Mu1SFxItc__3Ct19-231S_Xt42RwmZNCSsjXVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XHxhgxG7j8_uCltr5dAOViq8Yf-5KbXUt39frWgKO4p3e3kISuuL1mTk7EGVws0mgFlr9JMocc3VQvDfwigAR2BsZ9YfUvemWs1keh2E43dqwHPDeO39vvEzZkudC5gRO6sAgvn4ZkpDLu8g33EyiyKf8dvoDnxH-gOXXr6KhnFUwB5dyESiYP0AICbqmzgdP8gICUK-4MJ9YNeqLcJo3mgSA7Y-yDiyx_MTGmP6S20uxbL8ceGTVoSgpFZF_JMfsO7jHFZYAXjOzG3k3kA0KKM-c7tGXeNQBdWsNyBrbiTYljwnH7offikxDhfTi5FpYCHTBprJpCdqQZog8Pw6Hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ecd58481d.mp4?token=cmu98cNKZBc9DPgk2dhVC7XJ2s0G_fCtBe7iB8j7mMefEINmsm65Yjcv_XgT3zLl0li6xSsWt3cSfmQC0Idm34k98MnCkYHUfANR1KKP1ViSkSxsyVTSYRft5lQdiatQIwW1tnB9hG2mLpSRXb7UEMX3zn9dOkazAggWU8JV9SDABB2aOOZjRhAho5pKRFg8rRBG7KHo4__6RXMSrrpTFrpjJDDFa4M0KwpLRQLWh1sCm7_sRSFzb8UV83rVxnm9ye4VCTQw1N-g1aCtvpSj1zmNjZ2QbNR_0GQLoeLgLZFbiePGnGC7IbhVdJGg5pq8ol6gFxnC_IUQHkq-Ggg1VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ecd58481d.mp4?token=cmu98cNKZBc9DPgk2dhVC7XJ2s0G_fCtBe7iB8j7mMefEINmsm65Yjcv_XgT3zLl0li6xSsWt3cSfmQC0Idm34k98MnCkYHUfANR1KKP1ViSkSxsyVTSYRft5lQdiatQIwW1tnB9hG2mLpSRXb7UEMX3zn9dOkazAggWU8JV9SDABB2aOOZjRhAho5pKRFg8rRBG7KHo4__6RXMSrrpTFrpjJDDFa4M0KwpLRQLWh1sCm7_sRSFzb8UV83rVxnm9ye4VCTQw1N-g1aCtvpSj1zmNjZ2QbNR_0GQLoeLgLZFbiePGnGC7IbhVdJGg5pq8ol6gFxnC_IUQHkq-Ggg1VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال ایران در دومین دیدار خود در مرحله گروهی جام جهانی ۲۰۲۶، با ارائه یک نمایش دفاعی، در ورزشگاه سوفای لس‌آنجلس مقابل بلژیک به تساوی بدون گل دست یافت.
مدافع بلژیک در دقیقه ۶۶ از زمین اخراج شد و این تیم ۱۰ نفره به بازی ادامه داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/76571" target="_blank">📅 00:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76570">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GlrbsEwKG8wmrrbqvutJS9jqPAtZ_ddKmAG65GvOi6cRc8LDtfCwl3ekwwqoDviudQdc-0ORdLnAz9ZP3RlIebclHidLeG3_G2MOfjZTF1Gy_bqQjfBokF27LItn7Rs34SibUv0VI5VmGjanMBSTE9ljG4wbPfy5BTIp2jHuY4SfOiWDV7H7IxW7WP2SyEFu2q_D7u-1aCB4gTEbd_vF9brk5UPqAZGSo8oFULo6PPRFjhCzG6XIOFHoNc6g8qHgTSy6JYXqeqxdbd8_fbLNUlGTB3BlcDfp58Ofbt-bm2gjivDFFoNnCvTa6521FS2i_wE74RlKVQlcDAtsB_8A5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
بعد از آن‌که تریلیون‌ها دلار خرج ناتو کردیم، ایتالیا و نخست‌وزیرش حتی فکرِ درگیر شدن با جمهوری اسلامی ایران و تهدید هسته‌ای بسیار جدی آن را هم نمی‌کنند. دهه‌هاست که ما از آن‌ها دفاع می‌کنیم، اما وقتی پای آزمون به میان می‌آید، آن‌ها برای دفاع از ما و بقیه جهان حاضر نیستند. خوب نیست!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76570" target="_blank">📅 23:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76569">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KtkGGuNnHLQHQJ9mYjNibZtY8A7x3jGzOxnpcAXi9JxaPkP4yowH58oV61sG-H4vDkB0VIMXyQvbWItRnizW9AqNZhfl-t9CFSmOk3NOpupoVjlrLuOWVksBvnkVnyrjXdas0mltRqsSoxKU9Q4qaHcTY9qZD21ALyvv32He2SKN41Gc4eVnvBDvIHVbBxjlWfZbqmCyr1n3ZRqcNVtnfFhb7k174W2qC2xzIVbZpkrHXCXe5pmv5XDPNWu0lZhY8cNEGS87e0S2cCYHp9QwO4A0XrasuNfaanfo-zkD2jYvb9ZbIk6U6IgILL2A0hKpdb8PQ97wkOqCg5jOy8Y7vA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76569" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76568">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k7Gdyc9Qq_E-Mx1FBKMXrNzboVEtuPOexPHw4KftXWRVWBj8Fl39h0kxTK3ebqjyPB4xnd9IuG1qjnmGcxtNmKWPnTJq3CmYu9Ln3_HzOcUq1OdXnufrgXHbUP1iQVRn2NWYEh2OeKIuzyf3kLafk1DLEb5sbOvS8VKx5Dh2CZf2RVpsQuwC9QZExQKQPCHY6_Oy5xdFoyrOqnLcfA8a9VCDAy1s0THY76x3tPmCLcOQbn-gIgwh0Xf8vcbIBXkW63m3aYopX3UVsboKgl0RdN6-TxpxUb8cjWdZBX-a1XiH6S8m61z3mCuKhn4tSUEWIQ_q1bKncI9P54Fm36Nm-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/76568" target="_blank">📅 20:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76567">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tm6smOd89REa6wXY7Eo-jQdoe9rSBFD9KoisoZpKMJ_mSm1-mAyXZKHlKFcOJX1eyoHLTJOLLG67KPD24ZPUhWkDMt0aoLcHPRh60rmMbMknUO8U8gPRUGY4utov-M3co-gJwtaZzgt7fMPGEz3G9d2W4ItJXjS043fvEa0naZAQtF-LCiNhYCXqGSVl0xMaQnrTSQdcoi0sfd6YctNJZeYK7Eu0pXeIcmchkEbVIJ2dJ26rFsTkfEoXXWymhUzmIXjPXX04kIcjK9xzpcCo-Fpw6P059Do_lowqB9lkudH8T8viVRDtJBAwCoN7Zw5L0lN0p91HfCG6DwGcuAHB9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در واکنش به اظهارات مسعود پزشکیان، رییس دولت جمهوری اسلامی، درباره ناچار شدن آمریکا به پذیرش تفاهم‌نامه میان دو کشور، هشدار داد که تهران باید در مواضع و رفتار خود تجدیدنظر کند.
ترامپ در گفت‌وگو با فاکس‌نیوز گفت: بهتر است مراقب حرف زدنش باشد. بهتر است رفتارش را اصلاح کند، وگرنه ما کنترل بقیه کشور را هم به دست خواهیم گرفت.
این اظهارات پس از آن مطرح شد که مسعود پزشکیان روز یکشنبه ۳۱ خرداد گفت: آنچه مسلم است از حق غنی‌سازی اورانیوم هرگز کوتاه نخواهیم آمد و طرف مقابل نیز ناچار است آن را بپذیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76567" target="_blank">📅 19:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76566">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JW1qdQfzj8LBV_kHB1Tw_f6jaBJZl-pw6jNaPjG7z2yPziubmxE4AAviuw3PFnJeoCgNlPuZ1_uP5oxnhtijNHVorKJnQIAdLFFUikGAkMG2lXz6O6gCKMRf1h27tfLGIuIDYscJf-dEh_d5MhkFq_Nc6JQhoh5nEux08Zy_XA9pEKGSOmLUoE-eYhZ2ZOLlG_TMQUh4bQ_SEMx_7dyDY5pveV0EXCiWO4D_VKWPJlXOkHnZI83EvAM4Yk3nTL1vFF-ZO1srfUA-MtJcOO32spMr5kahbMlP-cLdHYNnNRXWlm_99FbGVTyGC3a6pHvBeUlH6T9sUUHsn6iO9-O0GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، اعلام کرد همزمان با برگزاری مذاکرات در سوئیس، به مقام‌های جمهوری اسلامی درباره هرگونه اقدام برای بستن تنگه هرمز هشدار داده است.
او در گفتگو با شبکه فاکس‌نیوز گفت این هشدار شنبه شب به تهران منتقل شده و تاکید کرد در صورت چنین اقدامی، ایران با پیامدهای سنگینی مواجه خواهد شد.
ترامپ همچنین گفت به مقام‌های ایرانی گفته‌ام که اگر تنگه هرمز بسته شود، «دیگر کشوری نخواهند داشت و حتی امکان بازگشت به کشور خود را هم از دست خواهند داد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/76566" target="_blank">📅 17:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76565">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z6n-XjEmEvCWGVvSpJbkOdO-LTpEW0aLMk7kELuoqKME-uRTmptWJAA97QSsJeqjHqdSEmz4PKX7jO-bkzw_J8VuZVG8vZk3Ah3DtNbOK82A3EEjkA4s9PPceub3jLArhLc9B-EGW3yblYJeP51o3s-Tx-6o1ZCkxe0zJ_7x4ZAkL-fQ34LiAXMnII8W-1dNwQjUO6NkZpH3SNjtMukAGOLdwtY7eTeuuvc5pJRESA1mB512iRX28r1mP6XmnJtOOIug67_UIWpYHsZc6pPOmB2Zg4kUZg1CjhfXlnuGvFbtgsTm5Z4-ScArhUMfuTZZz-8t7Ijv1cipyAysI3rECQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران باید فوراً جلوی نیروهای نیابتیِ بسیار پرهزینه‌اش در لبنان را بگیرد تا دیگر دردسر درست نکنند.
اگر این کار را نکنند، دوباره به ایران ضربه‌ای بسیار سنگین خواهیم زد؛ درست مثل هفته گذشته، اما این بار شدیدتر!!!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76565" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76564">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e1422ca156.mp4?token=M_1b1Q7Z2Piidv_vUW38ghvtDkMq8bScPuVzbaWjFzE9JzKIn3GQlI6D8LvWyNkFUBSW9ug8oaxIzgrkayiyJ3R7NQweWg-1HpbtKxQAJ6kez2zt7wh1jOtNo_F2s8Y8pcA4eoXSb4mDm8HdSVhhJ3a_GaR2U-rjpcOrfdOisJ9yQQOx8OI-qRty_2580g6NPYGKZ0vjQ97xNu325ZGvObkDfMhvpU1hl9NIkGXpm0XvuxrIH3JaBG1hEmcunJccjoBtlfuhQvkMGmIv1AsNCZ1kRT6D0N_Qow0AmdDb-V7sIUmbN0yDKBUOhGqkAhjksJl76opGp48YCMbTU7X3YA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e1422ca156.mp4?token=M_1b1Q7Z2Piidv_vUW38ghvtDkMq8bScPuVzbaWjFzE9JzKIn3GQlI6D8LvWyNkFUBSW9ug8oaxIzgrkayiyJ3R7NQweWg-1HpbtKxQAJ6kez2zt7wh1jOtNo_F2s8Y8pcA4eoXSb4mDm8HdSVhhJ3a_GaR2U-rjpcOrfdOisJ9yQQOx8OI-qRty_2580g6NPYGKZ0vjQ97xNu325ZGvObkDfMhvpU1hl9NIkGXpm0XvuxrIH3JaBG1hEmcunJccjoBtlfuhQvkMGmIv1AsNCZ1kRT6D0N_Qow0AmdDb-V7sIUmbN0yDKBUOhGqkAhjksJl76opGp48YCMbTU7X3YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76564" target="_blank">📅 16:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76562">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/12a29862bf.mp4?token=fvpGTTtHJcaJQjbnnI1qIp5ANj84raKL6xNwigbXabvOf85SuNjJ4xsEvy3n_iH_eLTWjqmjcrNgqC_T7oUkJW8vpYpyEKDwA9XV0JvoM5zZq77qPBsOhWDZpqEQqMUwwI2rZlLVHp5pdxz9AVMJx-1Bb485F3y-ZeUwSpb6Z3HAAj5cvkl7Ys06HNPw4tsg7C73fydVKpPbmh2O-ivrvPZ3pAZfaC5PKuDI5O_dM7kOWiHLtI5bPS85f7-uBdZy4bz0eR9pwrj9wx4A8Ub4b0HhPkt_Z5R6FzfWXC3DTHrrEiXQOoWupe8Cmcp0x7LVBHdgp1lYv2nftr2rg5Br2w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/12a29862bf.mp4?token=fvpGTTtHJcaJQjbnnI1qIp5ANj84raKL6xNwigbXabvOf85SuNjJ4xsEvy3n_iH_eLTWjqmjcrNgqC_T7oUkJW8vpYpyEKDwA9XV0JvoM5zZq77qPBsOhWDZpqEQqMUwwI2rZlLVHp5pdxz9AVMJx-1Bb485F3y-ZeUwSpb6Z3HAAj5cvkl7Ys06HNPw4tsg7C73fydVKpPbmh2O-ivrvPZ3pAZfaC5PKuDI5O_dM7kOWiHLtI5bPS85f7-uBdZy4bz0eR9pwrj9wx4A8Ub4b0HhPkt_Z5R6FzfWXC3DTHrrEiXQOoWupe8Cmcp0x7LVBHdgp1lYv2nftr2rg5Br2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/76562" target="_blank">📅 16:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76561">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDesrABdvek01id_QffamHMPzb7GG29A06dSSMEgZqzWp8R2zDgdk7ZWQdJilOLKIp9RUaZ63U2TnyeGD3FfhJTDHKGJFvQrSNJ0WBf0MVKFOqyQ959aAamUEYlJkEhUe2tc1u_z2iMedSRVQFUL7cuPxERaiLx60moLzJdIgIkNPIHl5lBVl0-fpBBcmzwDnxOfsalnqSi0-3rNmJImZmAUyuVQr_JcEtZQGaioBwrpZnWeWHCS_9jJwijNfBXJmA11KGxnF5IcvWWC5lyTSgo8LiNJwcc1yzap1kkW5wSyNOWq_hExo2dE37gzfpc6bP54Erta6yRN7yaMNAXjlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از دو منبع منطقه‌ای آگاه گزارش داده است که آمریکا می‌خواهد نخستین دور گفت‌وگوها با ایران با دعوت تهران از بازرسان سازمان ملل برای بازدید از تاسیسات هسته‌ای ایران پایان یابد.
به گفته این منابع، این تاسیسات پیش‌تر هدف حملات آمریکا و اسرائیل قرار گرفته‌اند و آخرین بازدید بازرسان از آنها پیش از جنگ قبلی، در ژوئن ۲۰۲۵، انجام شده بود.
اکسیوس می‌گوید: «آمریکا در مقابل آماده است به ایران اجازه دهد به بخشی از دارایی‌های مسدودشده خود دسترسی پیدا کند؛ از جمله حسابی به ارزش شش میلیارد دلار در قطر.»
بر اساس این گزارش، ایران می‌تواند از این پول برای خرید کالاهای بشردوستانه استفاده کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/76561" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76560">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7zP7gX3U3-ktNrBI_LPWxy4kSeWWKN8Hic3ssMExOyyOAsoIF5lNhaK2yoHilUCDi2YlRIEHcZBGjlZKrynT5jvuTazeGCjMnRgDGCGvF2N4_ozXjbWuNntLbWIhuPQFz0EHjSoSEzVmUs2_Q4RGzNKBELl_wL5mMHkoaSjTLIHH6ZdAbIlfaFxs0pds3DkucxFfD_IAv4x9sS-7VQfiGA1NTGOryi3j74jcqI6wX4BRkRZBHjE0rVAB6ARE_lvNdSOh4buav5CKYrh5oQQNit57LX3_qeD7u9WiaprbRw9FeJSEkiZD47y6VNJr_lU0rj0crEWHtn2O-oxKlxRIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام‌های بهداشتی در غزه می‌گویند که دست‌کم ۱۰ فلسطینی در حملات هوایی و تیراندازی نیروهای اسرائیلی در چند حمله جداگانه کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/76560" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76559">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCEZkBnI_UD2eQzNCTgnaqnpVH8Zrzh14KloSbMuD-2B5IB3EyFKpnqC9yKiwQSx7HvaA8OiAVD8oly17OdrQ81xXfeKOePiRpZR7nsCHflGWfll0FCW_NNPiwMeiqGmsQpNmpWKNxzUiG1kZJHYLyVVaFHTzv7r7PWfecO3_BmljNX-rSDU8SnQX_L927eEDmCE6xEMff0niYIFKWIaB59LxVRJY173r-_KGm5pvB9RyHYxliq9Tg2Sl_cnYOd34PlMdAN0bStoKYYuuNM4AWishRjG1iKlVkzXO3UHa5yFHqNLs2QUroTOcmw6PGuDTBW4058lmPpS5Lu9HLWxzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از هزار دانشجو و فارغ‌التحصیل دانشگاه صنعتی شریف با امضای نامه‌ای سرگشاده خطاب به محمدرضا تجریشی، رییس این دانشگاه، نسبت به آنچه «تشدید فضای امنیتی» و گسترش برخوردهای انضباطی با دانشجویان خوانده‌اند اعتراض کردند و خواستار پاسخگویی مدیریت دانشگاه شدند.
انجمن اسلامی دانشجویان دانشگاه صنعتی شریف تاکید کرد که بیش از هزار نفر این نامه را امضا کرده‌اند. انتشار این نامه یک روز پس از رسانه‌ای شدن صدور احکام اخراج برای شماری از دانشجویان شریف صورت گرفت.
امضاکنندگان در این نامه نوشته‌اند که در ماه‌های اخیر دست‌کم ۳۰ پرونده در کمیته انضباطی دانشگاه تشکیل شده و ۱۳ دانشجو با احکام بدوی تعلیق یا اخراج مواجه شده‌اند. به گفته آنان، احکام سه دانشجو نیز در مرحله تجدیدنظر تایید شده است.
نویسندگان نامه تأکید کرده‌اند که آنچه در دانشگاه می‌گذرد، ادامه «روندی نگران‌کننده» است که به دلیل نبود واکنش مؤثر از سوی مدیریت دانشگاه، هر روز ابعاد گسترده‌تری پیدا می‌کند. آنها همچنین نسبت به افزایش سرخوردگی دانشجویان، گسترش بی‌اعتمادی در فضای دانشگاه و آسیب دیدن اعتبار علمی دانشگاه صنعتی شریف هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/76559" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76556">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xb6WYNHlT9qRJo9A7tjDhjOJRw6Z11TkJhiAHoiZmeaED5R5jqnH0QZrnenrK5Yi-iGmblAm1B93nA0Gd_61vIAUprujIvOKh8ziN199d6FDNJrvf5EuaviRSAf0ehLdiVF4af9TIFfAVEVxeOziJdCHBbSKH7Fd22aKWXlr3O0rV_p4ZdkfbKp8APuCMrb69M0vFMypWX6WwDZPdO6LHsXVResvhtObDPTo10OqTXFFORa4PjTFqoem2trEtl71-5_ZlVt69R9S7Hj8ZJEvdgiUhNIKn4pN1xfA-xqe8Z3WlIwUM9p8eg52iTUr0l89662sJAifoTfd0BfB_eTmyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5Ufa5v8QTs0IZ2oqM6lSt7nASaRg2II7wOm7k4O_ud40d-vZmdGeB2vCn4OCweHcph0Mf0cynvcJ1yLA6Rwlgkia5T2Gx3mBWF5tib3F6YJRBs9VjvBNEIKacTTdkAojn2SAt2_V6heIbDddgGH2Dc4SSr0sR0QkmPSrLYakowQnTcZzaKtx1t-Nh4hVqcOxrbkH2jyCmejmPFgRqBY2K4LP-64pbgIWY_JZswis8AUXuibB2HveSJcJ_dH6aEnVzpBOmHcfLjN9dFp6OHx8G4Rma6OuHiz0g6LbD9MQ5GXDxvIFalch2-fd04fQMmpQcluKEUJIEBnKo4MEPnkoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/76556" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76555">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a9CQpboaw2oZZJ-iojM5AqGu4tI5La96PtHXpLn-mbY3AvO-lkkc8_QFnARGdunpCGd9XqUjIdXT5EW9TTCeJqc0Xioeb9qd6SfJRfnfBPURvZPndPjUjWc87OaPsnyUpq8oL8O2ERSyIWrGGv_TyXutFarqtDyEvKC61JCkak6QKRjJ9V_Rd-L0YI_cZtK1IVcYT0xuDjyIG5QS8M40eM_lshnZ0g-Nyz3wjuElsA87p1Jtxn7zHY78xbYJHW5QlDId8eMoE42OEYCpcmtOTvPW-yxmGgGlFjUPaGffW39VKm0UYriD-WjP-U6KRY983NnYb0GEnxTA8J-wN2llTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/76555" target="_blank">📅 22:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76554">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/35770a9ed5.mp4?token=brZ1TSvklYTiiP7f-7G9xLD-7HodOQJEZR3z7iqlIStGKPPg9iHpk5-Yg_Q-iPOzyHTahs0_DlZAK-U4gGAG-7wOdpaB0VPXftMIpldlOUMEKv8yNmO-a6dsyO8aU6qzT8XJBU21atkYVtGTSLwVDWY7O-GJ-gzhgCVeN1tV_vQRZ13CYGn_mD0WqdE8ZZ5gSPeut23hA_6A5sBEvFkeMx-Ss8DC7cIw_8wmoLStUE6ZWhvGzNnuQ_zGKcHINuyKxoswbx4lQITRPPkct2dYq4aChsOMOTk_-QgNfxi4UW0ihsmHNGseVMfFOa-6msVYbabxvE5p8Yc1T0gK5iPJLy37MwH3Vt4iHo8trqPYuc10KgSJBq0M0oFCrxpL6c5xxLykhN1juXmUbaGZBlGGAMEeQgtr1hFDwUU8pLk2HVMnGHMRTvDk-5paDCbLCJuJBwX8jFETqNTjEP6uzZexGWDDUfm5OW8zrRQuZOkeKAs74fXgTcwPK9Py6aBv5-07o-pSwYpDq8srbzGnQ6QFTYoodEpS_wqy0ZP_e94M6WiUGxulMpBSGZyc95xtFXdwe9YW0fs9lNHFT_qCcUPdna8N8IhPSP-gGs0GErVrYKmNcKoFyGkK9Ik-84OgC83ief2tqcxoQonGLbRa0pLhp2Y73frGbpUqRclfi3InA9I" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/35770a9ed5.mp4?token=brZ1TSvklYTiiP7f-7G9xLD-7HodOQJEZR3z7iqlIStGKPPg9iHpk5-Yg_Q-iPOzyHTahs0_DlZAK-U4gGAG-7wOdpaB0VPXftMIpldlOUMEKv8yNmO-a6dsyO8aU6qzT8XJBU21atkYVtGTSLwVDWY7O-GJ-gzhgCVeN1tV_vQRZ13CYGn_mD0WqdE8ZZ5gSPeut23hA_6A5sBEvFkeMx-Ss8DC7cIw_8wmoLStUE6ZWhvGzNnuQ_zGKcHINuyKxoswbx4lQITRPPkct2dYq4aChsOMOTk_-QgNfxi4UW0ihsmHNGseVMfFOa-6msVYbabxvE5p8Yc1T0gK5iPJLy37MwH3Vt4iHo8trqPYuc10KgSJBq0M0oFCrxpL6c5xxLykhN1juXmUbaGZBlGGAMEeQgtr1hFDwUU8pLk2HVMnGHMRTvDk-5paDCbLCJuJBwX8jFETqNTjEP6uzZexGWDDUfm5OW8zrRQuZOkeKAs74fXgTcwPK9Py6aBv5-07o-pSwYpDq8srbzGnQ6QFTYoodEpS_wqy0ZP_e94M6WiUGxulMpBSGZyc95xtFXdwe9YW0fs9lNHFT_qCcUPdna8N8IhPSP-gGs0GErVrYKmNcKoFyGkK9Ik-84OgC83ief2tqcxoQonGLbRa0pLhp2Y73frGbpUqRclfi3InA9I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نبویان: مجتبی خامنه‌ای نامه داده بود که چرا شروط من رو در مذاکره رعایت نکردید؟
07:20
صدا و سیما: افشای مکاتبات مجتبی خامنه‌ای از سوی نبویان در شبکه خبر پیگرد قضایی دارد
صداوسیمای جمهوری اسلامی ایران اظهارات محمود نبویان، نایب‌رئیس کمیسیون امنیت ملی مجلس، در شبکه خبر پیرامون مذاکرات پیش رو بین ایران و آمریکا را «مصداق تخلف قانونی و مستوجب پیگرد قضایی» عنوان و اعلام کرد «مدیرکل مربوطهٔ این شبکه استعفا کرده است».
محمود نبویان، که به جناح تندرو موسوم به «پایداری» تعلق دارد، روز شنبه ۳۰ خرداد با خواندن بخش‌هایی از متن‌هایی که گفت مکاتبات مجتبی خامنه‌ای با هیئت مذاکره‌کننده است، مدعی شد رهبر جمهوری اسلامی در مراحل مختلف با روند مذاکرات و بندهای متن‌های گوناگون مرتبط با مذاکرات مخالف بوده است.
این گفت‌وگو پیش از آن‌که نبویان به متن نهایی تفاهم‌نامه برسد، قطع شد و موجی از واکنش‌ها را در میان دیگر چهره‌ها و فعالان رسانه‌ای جمهوری اسلامی در پی داشت.
صداوسیما در بیانیهٔ خود اعلام کرد نبویان در اظهاراتش «اشارهٔ ناقص و مخدوش به برخی اسناد دارای طبقه‌بندی» داشته و سعید آجورلو، عضو تیم رسانه‌ای هیئت مذاکره‌کننده و از چهره‌های نزدیک محمدباقر قالیباف، نیز او را به «تحریف عمدی متون» با هدف «فرار از پاسخگویی درباره ادعاهای نادرست قبلی» متهم کرد.
محمود نبویان، ۲۳ خرداد ماه، در آستانهٔ امضای تفاهم‌نامهٔ ایران و آمریکا، در یک برنامهٔ زنده در یک خبرگزاری نزدیک به سپاه، متنی را که مدعی بود تفاهم‌نامهٔ ایران و آمریکا است، روخوانی و از برخی بندهای آن به‌شدت انتقاد کرده بود.
نبویان یکی از اعضای گروهی بود که پس از اعلام آتش‌بس جنگ ۴۰ روزه، همراه هیئت مذاکره‌کنندهٔ با آمریکا به اسلام‌آباد رفته بود.
مجتبی خامنه‌ای، که پس از اعلام رهبری هنوز هیچ صدا و تصویری از او منتشر نشده، پس از امضای تفاهم‌نامه توسط رؤسای جمهور ایران و آمریکا در پیامی مکتوب اعلام کرد «نظر دیگری» داشته اما «با تعهدی» که پزشکیان به او داده، مسئولیت آن را بر عهده مسعود پزشکیان، رئیس شورای عالی امنیت ملی، و دیگر اعضای این شورا گذاشته است.
@
VahidHeadline
حمید رسایی با انتشار ویدیوی بالا نوشت:
نبویان در آنتن زنده شبکه خبر، در حال تشریح جزئیات نامه‌های رد و بدل‌شده میان رهبر معظم انقلاب و شورای عالی امنیت ملی بود که پخش برنامه به بهانه میان‌برنامه به صورت کامل متوقف شد!
ما که از یادداشت‌های آن امام شهید در این باره اطلاع پیدا نکردیم ولی گوشه‌ای از یادداشت‌های امام حاضر توسط آقای نبویان در حال پخش از سیما بود مانع آن شدند!
صدا و سیما:
🔹
روابط عمومی معاونت سیاسی صداوسیما: به استحضار مخاطبان محترم شبکه خبر می‌رساند اظهارات یک نماینده مجلس دعوت‌شده به برنامه امروز زنده این شبکه و اشاره ناقص و مخدوش وی به برخی اسناد دارای طبقه‌بندی و مکاتبات مسئولان عالی کشور، مصداق تخلف قانونی و مستوجب پیگرد قضایی است و سازمان صداوسیما پیگیری‌های لازم را در این خصوص در دستور کار قرار می‌دهد.
🔹
شبکه خبر ضمن ابراز تاسف بابت بی‌توجهی مهمان مذکور به قواعد اخلاقی و الزامات آنتن زنده، به اطلاع می‌رساند مدیریت این شبکه ضمن پذیرش استعفای مدیرکل مربوطه، برخوردهای انضباطی لازم را به دلیل بی‌توجهی به الزامات برنامه‌های زنده و سهل‌انگاری در مدیریت حرفه‌ای به عمل خواهد آورد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/76554" target="_blank">📅 21:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76552">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bUQCnvy-PimIBtQps5Vyg2lv4GWJqLvH9ytrm3txg2t8oofU-JeQgQrQfIeZRq7pff4cPe-eVUwyVgDhWfBqzYQd2FBEK_tFySct_W7wufraqWEDArP5banGq_HDJNEWYoAzELrrkOeL1MA4cEGV0m4ucu_udTIFHM-AnVT94xNG5UA1Dqo0JDqc3vKzqMiKQj4LS7A9rvp3P7lCkWd3BjoZj1EFhwz7pkrN3TN8nxcHYfSSV4pqk1rJ8278F5_Xw5TPqxbDUe1kzNtbNmSrhAp6jcDWbGq9jIRLsbsa3EaIs7pQ8oUtvXb6AQTmjnfyxVG8u42tn6Z_WdGYaZ-owA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WT2UQ9CBPoelAD6zM4USxchU7l9yfwtg5_mejCiajFxi06GeBterPYBKsqH7EJQ7nfdO1XAHaaGCPyKLmG2KR2QqoQv3pchCJ0tEzvM4AxSgvR6NCZyjS2-ic0cnZLTq3_GEOBbY_si902IACVGac-qKZQr7ppLv_PmLAeyWHbfKTV8UXrBuk0mzVzvh87he9nZnpUOd024cIcPqQ4Uw6OiKmHtGlmdHy9sPd3rAlUPnqJFhMTkrNsZg_kDW2kuLzC3mGY4zdo5zDkbtusBKJZpSDKCQERnk-lQNLAIDekdJsnkFuPq-IMXsWTgp4XAwNpNLpF4n7yPBjsh5KqhREw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ در تروث سوشال نوشت: محبوبیت ملونی در ایتالیا به شدت کاهش یافته، شاید به این دلیل که او و ناتو در جریان ماموریت جلوگیری از دستیابی ایران به سلاح هسته‌ای، به ایالات متحده پشت کردند.
ایتالیا حتی اجازه استفاده از باندهای پروازی خود را به ما نداد که یک مانع لوجستیکی بزرگ بود؛ آن هم در حالی که آمریکا سالانه صدها میلیارد دلار برای محافظت از ایتالیا و دیگر متحدان ناتو هزینه می‌کند.
رئیس‌جمهوری آمریکا در پایان با لحنی تحقیرآمیز تاکید کرد: اکنون که ایالات متحده ایران را از نظر نظامی شکست داده، او می‌خواهد برای بالا بردن آمار محبوبیتش دوباره با ما رفیق شود؛ اما نه، ممنون!
@
VahidOOnLine
جورجیا ملونی، نخست‌وزیر ایتالیا، با انتشار بیانیه‌ای تند در صفحه اینستاگرام خود، به هجمه‌های اخیر دونالد ترامپ پاسخ داد و حملات کلامی رئیس‌جمهوری آمریکا را «بی‌دلیل و بی‌معنی» خواند.
ملونی در این پیام خطاب به ترامپ نوشت: «محبوبیت من به هیچ‌وجه به رابطه با شما بستگی ندارد و دوستی با شما نیز کمکی به آن نکرده است. محبوبیت من حاصل توانایی‌ام در دفاع از منافع ملی ایتالیاست؛ یعنی همان کاری که همواره انجام داده‌ام.»
نخست‌وزیر ایتالیا همچنین با دفاع از تصمیم خود در جریان جنگ اخیر و عدم اجازه به آمریکا برای استفاده از پایگاه‌های نظامی این کشور، افزود: «نحوه استفاده از پایگاه‌های نظامی آمریکا در خاک ما، تابع توافق‌نامه‌های متقابلی است که ما همیشه به آن‌ها احترام گذاشته‌ایم. تا زمانی که من نخست‌وزیر هستم، این توافقات نباید نقض شوند؛ چرا که ایتالیا یک کشور مستقل و دارای حق حاکمیت باقی می‌ماند.»
ملونی در پایان نوشت: «در هر صورت، میزان محبوبیت من اصلا به شما مربوط نیست. پیشنهاد می‌کنم شما روی محبوبیت خودتان تمرکز کنید.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76552" target="_blank">📅 19:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76551">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/smThNq3bFK332X38wAVRTirWYm6UQp8dM9vExyT7_Qr9OWGUScYwjPh7zhQRjQWoa3gW48dBIs2aOEEqhTR9dQl-p1dsMAk0bZXR5V-1-bVRbkN71OtEQbkovUa0NYfAkU0_3RfcY3cPghAqNSZlnHR5R-YkyXnjC7sVZomTQ_j7VGpXS9D38iCwi9ZnLMl_CvVpGioM7wF7JyaRJZFpH6Ke-YucYT3QeOJUJuRlR3uL28ocITWA8cJ8CyudYcNylDc-mhCYR45RVBGsEaPiSzfzeJeiNHaFpQvHUlf3ZZpO3-pLa9CgHiVy-hbU39mnMTlYIZHrXajcLItbbiKMCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران گزارش دادند که هیات مذاکره‌کننده جمهوری اسلامی به ریاست محمدباقر قالیباف و با حضور عباس عراقچی، عازم سوئیس شده است.
بر اساس این گزارش، عبدالناصر همتی، رییس کل بانک مرکزی و علی باقری کنی، معاون بین‌الملل دبیرخانه شورای عالی امنیت ملی نیز در این سفر حضور خواهند داشت.
همچنین کاظم غریب‌آبادی، معاون و اسماعیل بقائی، سخنگوری وزارت خارجه و حمید بورد، معاون وزیر نفت نیز این افراد را همراهی می‌کنند.
پیش‌تر وزارت خارجه پاستان اعلام کرد که مذاکرات فنی میان جمهوری اسلامی و آمریکا، یکشنبه در سوئیس آغاز خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76551" target="_blank">📅 18:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76550">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cagKKuExJ4E8sFBIptwRCJn7NePiEzPQ00OtQeuGrUWAy0P4hVNmIMsANh_yWGiM0RrwTrsJxN-Pe9GEmu4rihkxwfRpZPxNo5brqWK7Fer1sr9iCjoTt1gjOp7P66Lf9_f2cmwhFeMuFfrLuLv7QqBh1B70e2zlmrB1uJ9S9V1T-D9XwbfAyS--tWKAM205iYvwEWDHZ4qvVqoBdjoudv8fvnGbAxMe4ievpbMog6WYCd7F9Kegbl4LfI3XCUl9fR5QIlIt9J83muzxAmDFzToFaSzdrhdoizczGg1Xh6Vxwd81-syl58IFseNbHq-MYSPx5FDNkEMEXbrQWyFJ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: تنگه هرمز باز است
پست اکانت فرماندهی مرکزی ایالات متحده،
ترجمه ماشین:
عبور کشتی‌های تجاری از تنگه باز هرمز
تامپا، فلوریدا — تردد کشتی‌های تجاری در تنگه هرمز در ۲۰ ژوئن افزایش یافت؛ همزمان نیروهای آمریکایی به عملیات خود در منطقه کلی ادامه دادند تا از آزادی کشتیرانی حمایت کنند.
امروز عبور امن از این آبراه بین‌المللی همچنان برقرار بود و ۵۵ کشتی تجاری از آن عبور کردند؛ کشتی‌هایی که حجم زیادی بار و بیش از ۱۷ میلیون بشکه نفت را به بازارهای جهانی منتقل کردند.
مرکز مشترک اطلاعات دریایی این هفته اطلاعیه‌ای صادر کرد و در آن عبور امن همه کشتی‌ها را در یک مسیر تعیین‌شده تأیید کرد؛ مسیری که از ادعاهای خودسرانه درباره الزامات یا هرگونه مانع، آزاد است. جزئیات مربوط به عبور امن را می‌توان در اینجا دید:
ukmto.org
نیروهای آمریکایی همچنان در منطقه حضور دارند و هوشیارند تا اطمینان حاصل کنند که همه جنبه‌های توافق با ایران رعایت، اجرا و به‌طور کامل برقرار و لازم‌الاجرا باقی می‌ماند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76550" target="_blank">📅 18:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76548">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31b632aa9b.mp4?token=YRMAdzYnQpsUEtzs09aHzMgkZF_x-K-kyrXOjZ9nnf6ojbUxTnrdc7l0D8NpJ4Q2jl8-Y_Lirj2O9IzlrSqJCny7TL-ELRkBRfT2JqxnZrmLHN8wT1ox99LFJUMeOrCN-q-I5Qr_AaRTos8NNRGCeJAojT7ttj11aAe1czkbCRNwbop5SCyibzsQ5rizX-MfrUrLnD7wlhIBNSzr2A_8V4xIfOVAnJA9CaW24qcrWTZ6WPM-jDuF28eD6uzJ_WD-fa2ziNBXcYFYp1fDpqIpUvAMSqMBskiA_dz5FV5_IjOKKi9Iue-jvRFEA2bRVvJN_Bj-Fs1NhLtAJfz34prgrg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31b632aa9b.mp4?token=YRMAdzYnQpsUEtzs09aHzMgkZF_x-K-kyrXOjZ9nnf6ojbUxTnrdc7l0D8NpJ4Q2jl8-Y_Lirj2O9IzlrSqJCny7TL-ELRkBRfT2JqxnZrmLHN8wT1ox99LFJUMeOrCN-q-I5Qr_AaRTos8NNRGCeJAojT7ttj11aAe1czkbCRNwbop5SCyibzsQ5rizX-MfrUrLnD7wlhIBNSzr2A_8V4xIfOVAnJA9CaW24qcrWTZ6WPM-jDuF28eD6uzJ_WD-fa2ziNBXcYFYp1fDpqIpUvAMSqMBskiA_dz5FV5_IjOKKi9Iue-jvRFEA2bRVvJN_Bj-Fs1NhLtAJfz34prgrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی در شبکه‌های اجتماعی پربازدید شده که مادر مانی صفرپور، جوان کشته‌شده در اعتراضات دی‌ماه، را در حال سوگواری برای فرزندش در کنار یک دستۀ عزاداری نشان می‌دهد.
عکس پسرش را بالای دست گرفته و می‌گوید «پسرم، پسرم».
مانی صفر‌پور، جوان ۱۸ سالۀ لاهیجانی، ۱۸ دی‌ماه ۱۴۰۴ با شلیک نیروهای حکومتی در محلۀ سلسبیل تهران کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/76548" target="_blank">📅 18:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76547">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rQ9XqaK-zjxbbuSITouwfKH_q4ZJIZ4hI4no8xT58b6dWer57TPYilDoyxGh_Rfku8I1pMmVKGfmnMRfL5KeqjRqVb83RAnkN2k9odmu1n281GblL5zVUJybNN8sHpafOiQtcUMBpxfSLcRIOYZRxGMPOWy7qGjLNKWtXhtmUDc5_F_-cLmy7yZi2eElFC4LhRTBK-g7S0nIk2cmtnUMxnKDdJELMm6xCtLfkrTCwzVytl0xK2x672jXEzMccy5-zPOnwerb-RAJXCe9vBqdqiPRMV7IN48VMyDG1o617RZR_B8oxEulqcJ2AtxhieHkWRd7RGf_CPpqWGPvd80duQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد تنگه هرمز در واکنش به «نقض تعهدات امریکا در اجرای آتش‌بس» و «حملات اسرائیل در لبنان»، به روی همه شناورها بسته شد.
نیروی دریایی سپاه همچنین از شناورها خواست به تنگه هرمز نزدیک نشوند و هشدار داد در غیر این صورت، امنیت آن‌ها به خطر خواهد افتاد.
قرارگاه مرکزی خاتم‌الانبیا، واحدی از سپاه پاسداران هم اعلام کرد تنگه هرمز به‌دلیل «بدعهدی و پیمان‌شکنی» امریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه، به روی تردد کشتی‌ها بسته شده است.
قرارگاه مرکزی خاتم‌الانبیا روز شنبه اضافه کرد این گام اول «پاسخ به عهدشکنی دشمن» است و در صورت ادامه این وضعیت، گام‌های بعدی برای «پایبند کردن دشمن به اجرای تعهدات»، برنامه‌ریزی و اقدام خواهد شد.
خبرگزاری فارس، وابسته به سپاه پاسداران به نقل از یک منبع نظامی در نیروی دریایی سپاه، عصر شنبه اعلام کرد که تنگه هرمز از دقایقی پیش به‌طور کامل بسته شده است.
حملات اسرائیل به جنوب لبنان در روز شنبه دست‌کم ۱۰ کشته بر جا گذاشته است. اسرائیل اعلام کرد این حملات در واکنش به پرتاب گلوله‌هایی از سوی حزب‌الله، گروه مورد حمایت جمهوری اسلامی، انجام شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/76547" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76546">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f6wVXXuAaoQj4aiL-bG8cKdJD3jx6gHDtUln-QcELsrvjTlCin9UmrA5oaqcTt-E4Kg0tF7XyelVRDBk5pup1TTkecVMSKhndyclXNBhFlxWTKwrjUAMiItuGUDWYAso5ErKqBxuwfNxB47FO4U8_g0leRrCStosK7c_wmUJG3AcxueMAcVnQzFcY79akxudAl2VFmBfmr5JeL8aCA4n0b1XdkZIfTS3XFoJiSaqXrf8Y8L2g_bHdenF0BGJfLdA0q6HftWHD1kwoTDSrdmlYknJbM1jxKzaE-f8gb8j-IR4x-RYciqvKmwQSHH7kJsMt5rvdyA2AUjlvila8EzxiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهوری آمریکا، روز شنبه ۳۰ خرداد در گفتگو با فاکس‌نیوز اعلام کرد که استیو ویتکاف، فرستاده ویژه ترامپ و جرد کوشنر، داماد او، «چند ساعتی است» که در سوئیس حضور دارند و مشغول بررسی «برخی از ابعاد فنی این مذاکرات» با ایران هستند. به گفته ونس، کوشنر و ویتکاف در گزارش‌های خود تاکید کرده‌اند که «امور به خوبی پیش می‌رود.»
ونس همچنین از احتمال ورود میانجی‌های قطری و پاکستانی به سوئیس برای پیوستن به این گفتگوها خبر داد و افزود: «قطری‌ها و پاکستانی‌ها می‌خواهند مطمئن شوند که ما این کار را به شیوه درست انجام می‌دهیم، بنابراین من تلاش می‌کنم به این روند احترام بگذارم.»
معاون ترامپ که سفر خود به سوئیس را در اواخر پنج‌شنبه شب به تعویق انداخته بود، بار دیگر تاکید کرد که انتظار دارد طی دو روز آینده عازم این کشور شود. او با این حال خاطرنشان کرد که هماهنگی‌های این سفر «همواره یک رقص هماهنگی ظریف دیپلماتیک است.» این مذاکرات که پیش‌تر قرار بود روز جمعه برگزار شود، پس از وقفه‌ای کوتاه دوباره در آستانه ازسرگیری است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/76546" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76545">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sY1-L86ZEfTp6Nje9SfSwqA7P8Lz145xK3iu-DKcCd_1mteseeFZ5C1tD8Xg3NYJ3EOUWiRQHtPaAESyz8u1eEGiTZ2tEN5lu4lCWm4bb1DoZ-YIDoQSkhZeEEb_9gZaDywQm2LMycpXgpVc5LS8ClSp0Vcr_LXy5j2Rd8TqTcmGc9IQx4BKKVXi097lJoal7AMw_laE-mdMnq0FyaIluN5nih8ehRI5YZhEELP4SZfENa5iJSH2GfaWrGEf-pHyghleeYQUueyGFw-ilsM6udjbop1mh7Sa0aYvd46Q2Ul9UidLeMw4L5Wcv-9u54Obwnw42HzNANpOm7MS5Fgo8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«طاها نظری» معترض ۱۸ساله که پیشتر به‌دلیل حضور در اعتراضات ۱۸ و ۱۹دی۱۴۰۴ بازداشت شده بود، پس از  تشکیل جلسه رسیدگی به پرونده، به ۵سال حبس تعزیری محکوم شده است.
ماموران اطلاعات شاهرود، در فروردین ۱۴۰۵، طاها نظری را شناسایی و به صورت تلفنی احضار کردند. بعد از مراجعه به محل، این جوان ۱۸ساله به‌صورت موقت بازداشت و تحت فشار برای پذیرش اتهاماتی نظیر «ارتباط با تلویزیون‌های فارسی‌زبان و فیلم‌برداری از اعتراضات» به او نسبت داده شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/76545" target="_blank">📅 17:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76543">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fsERlmHkh5ObDML7LhMDgNGMRBsMwEMCjxTAeNNGfChj5T8zhfyyEclKnz1govn2VRa7qVtZPTN5A8fIfJPf8E8oLQYyrbNzrzejesInu22z8WLwF1cQvyuFBPEQ8pxOvrb67MPtnk2-Jv9ZSzOqnUrlG7Va6wPlCJfHf87BtrHAtvPFnemAsiH2uoYSbVfD1ffysvh_hL2by3-Fg6jj5XKdWH8ZW4zuWkrtA-gxz9TUFhbED-dCYJB7Z1SEccLIj4vp7iv3-FtkodiTmgVZdFlspiMmieNjOX6VkvfijndtLLvjcELF17wYqFTNGLgUXzy3ax03bWyJs-Nkvf9_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nortHowgdBxl8l0AjTrVKGvPV_pFu9kqLlD-tmhDxfbEy0BXIuTUb7lNBmwmVRocpJEpSYgaF-mwI5B6xsrbRLibYyK4dcjaGaOftZwOa9gusnITERehZxdOcOIQAC9-dRC6xNcsMlK-rYVM0JLE5zALl5G-lOAu3Hdt5SfDRlz1fj48PDYxPe9t4ZocodH41ghpUhfNlrcrYBp5hw3nnb8aL92-UQpZtXeAL6kXVF6QPM1xhVYKYMGpQSzaUgiMWWKDZ_wq1fRPaGnOMzT2oUFo9yamnpryEN1e7jhiNR7vwxireN_jC2FzRDHlDu4Qr_qLwwxE3EIu1JeYO5daJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت دلار و دیگر ارزهای خارجی که در پی نتیجه موقت مذاکرات ایران و آمریکا کاهش یافته بود بار دیگر افزایشی شد.
روز شنبه، ۳۰ خردادماه، قیمت دلار آمریکا در بازار به ۱۶۲ هزار و ۵۰۰ تومان رسید. قیمت یک یوروی اروپا نیز در این روز به ۱۸۶ هزار و ۴۰۰ تومان رسید.
این در حالی است که در طی روند کاهشی قیمت ارزهای خارجی در بازار آزاد ایران، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان رسیده و قیمت سکه طلا هم در محدوده ۱۶۰ میلیون تومان اعلام شده بود.
روزنامه هم‌میهن روز شنبه قیمت سکه امامی را در بازار طلای ایران ۱۶۹ میلیون تومان گزارش کرد.
از زمان اعلام تفاهم‌نامه ایران و آمریکا در تلاش برای پایان جنگ، قیمت ارزهای خارجی و سکه طلا در بازار آزاد ایران شاهد کاهش قابل توجهی بود.
@
VahidHeadline
حسین صمصامی، عضو کمیسیون اقتصادی مجلس شورای اسلامی، در گفت‌وگو با سایت خبری تابناک افشا کرد که در هفت سال گذشته بیش از ۱۳۰ میلیارد دلار ارز حاصل از صادرات به کشور بازنگشته است.
این در حالی است که حکومت برای بازگرداندن ۲۴ میلیارد دلار دارایی مسدودشده کشور وارد چانه‌زنی فراوان با دولت ایالات متحده شده است، امری که نشان می‌دهد تا چه حد به این پول نیاز دارد.
در این میان بیشترین میزان عدم بازگشت ارز صادرات مربوط به سال ۱۴۰۴ است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/76543" target="_blank">📅 17:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76541">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WIvbfXjW-LzBaCiURfHiPPmnOgbWKt21z_1StwIDzslH_jKKNb-FWaHARTm-1jgYRNHGfcNRu1ZhWoFtnuwJD1B4dcBp9YKNqb6uSojx-DBTbTbK6bE9YkqNnW4kJwMplhpfgN9Qy2nMjjsBZom39EgiwKvUgHKIIyCdUjnd5YDk0tsooS1Vbm8PlqtVQQMR9leKoVp863Nk8ri1DLUqcP3klG4HQF4OnMOf8BOSl6Qu5fZFCEycWD33W_4VhMnK9KsPlc8EkMCMh8ap9tYnsTEbJcwSJazBCriqOmG4C_FHiS7oDsWBCpN48U0lNavnAdmsUnH4ym3O9GyN1eYKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddbc33926c.mp4?token=oM84l3vUHBD5kllv-V-W1DhGQ-grIW8pJ-ohx7wiYOAbifkKNN5Mk4mIfqP62qjlb5CFWR1jj9KRGnYIG2ZlEGzDHlcc-EzRDxv4fQGRohay3tVRiP6MDfkl6J3sSkzP_LHNDnNme0t9iee8iRLUEMZB14920hCbrbE6I8ToKn1m717hfxa1gtr6umQNA-uxhec4-2uvDZbC6a5QbwhJT8zTf9TC852rSJzdZJGvHI9GI-Xiv3LcEMe7TvcXB-1XP36I4pyK0i1KjCHfygbDBFwvaCabwQnauBlLg3gKqpH6zSPFhlBFPkTz4f4V-lSTVJCwBVyePHPYKpm7Baar1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddbc33926c.mp4?token=oM84l3vUHBD5kllv-V-W1DhGQ-grIW8pJ-ohx7wiYOAbifkKNN5Mk4mIfqP62qjlb5CFWR1jj9KRGnYIG2ZlEGzDHlcc-EzRDxv4fQGRohay3tVRiP6MDfkl6J3sSkzP_LHNDnNme0t9iee8iRLUEMZB14920hCbrbE6I8ToKn1m717hfxa1gtr6umQNA-uxhec4-2uvDZbC6a5QbwhJT8zTf9TC852rSJzdZJGvHI9GI-Xiv3LcEMe7TvcXB-1XP36I4pyK0i1KjCHfygbDBFwvaCabwQnauBlLg3gKqpH6zSPFhlBFPkTz4f4V-lSTVJCwBVyePHPYKpm7Baar1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که هاجر نادری، مادر متین پرویزی، در صفحۀ شخصی خود منتشر کرده است او را در کنار آرامگاه پسرش نشان می‌دهد که می‌گوید «من به پسرم فقط یاحسین و تشنگی را یاد ندادم، به او یاد دادم که جلوی حرف زور بایستد»
خانم نادری در ادامه با شرح کشته شدن فرزندش در اعتراضات ۱۸ دی‌ماه می‌گوید امسال محرم برای فرزندان میهن که «ناجوانمردانه کشته شدند» عزاداری خواهد کرد و ادامه می‌دهد که «می‌دانم امام حسین هم برای این جوانان عزاداری خواهد کرد»
متین پرویزی ۱۸ دی‌ماه سال گذشته در سبزه‌میدان زنجان با شلیک گلوله جنگی نیروهای حکومتی به سرش کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/76541" target="_blank">📅 17:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76540">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTl3nSQkP52QmlBRknGxwQMuiOjaISqlNqpqf2j59YHHBSWz4WY4Z2Gw5xtmYITJnYrJNwYTuHlp_Lev861BInedaBMjfRpuJJm7S0s66z4u9LMEvoDncorxsv7ObIQbAc1dNDyco_DdJ-GOyhdWxQ-09bpHpgFefabdydRhNmywAbGt0MCeyeDCJHFW9BeSS3Pw2YIOFdbCFqRVbHeSYMLfcKoOFQe67UA0Tt_Zt6eixAtB9FAWAN80fZI-As6C4R-2oX_RcsCM5jReSGrgniaN_hmvp_I8Nxs4-qVflv_hGkY8oQW8HcIwsW-g34dxMSC-64fY0wBDmjeEmimj8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن نقوی، وزیر کشور پاکستان، صبح امروز وارد مشهد شد.
ایرنا به نقل از منابع خبری در استانداری خراسان رضوی گفته است که او سپس برای گفتگو با مقامات عازم تهران خواهد شد.
بر اساس گزارش‌ها وزیر کشور پاکستان قرار است در این سفر در مورد از سرگیری مذاکرات مستقیم بین آمریکا و ایران در سوئیس، با مقامات ایران گفتگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/76540" target="_blank">📅 17:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76539">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATzYublnqjXOs6pqDeNdExYxqAWSJUpNrXj6SffxHYttN5Co1s69p6yN0THQ0x1yZ9G7IVQEZIWlQw6UudNEbrYUopzvZNeZS17f9fu77srdQ8jXp13wWj_lsfDBRQwzC9DgBcxiXBsgqOznEGK_rycLRe4ajLFDrojgiJqr_g6zB-BgRuoMh91Ws0BlNYGPzS5m5meNZC34nL5vCP0C6_pu0ELWG2FnUkMYbe2Lk61WzBH6Agk1BGWFGHbh84zaTtAvgfIHn-q7Zb37dtJ4kWBHjteygkTuHXoFWBJjsVPu6qR9WfjEklb5-Gxlp4EJTBlYAWNdfeAvRwDF1JXuww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز اطلاع‌رسانی پلیس استان لرستان از پلمب یک واحد صنفی و معرفی فرد متخلف به مرجع قضایی خبر داده و اعلام کرده است این اقدام پس از آن صورت گرفته که به گفته این نهاد، واحد مذکور «ضمن عدم رعایت قوانین و مقررات، اقدام به هنجارشکنی» کرده بود.
این در حالی است که تنها سه روز پیش نیز مرکز اطلاع‌رسانی پلیس لرستان از پلمپ پنج کافه‌رستوران و سفره‌خانه سنتی در سطح استان خبر داده بود. در آن گزارش، دلیل برخورد با این اماکن، اجرای طرح موسوم به «ارتقای امنیت اخلاقی و اجتماعی» و آنچه «هنجارشکنی» عنوان شده، اعلام شده بود.
در هفته‌های اخیر و هم‌زمان با فروکش کردن فضای امنیتی ناشی از تنش‌های بیرونی، گزارش‌هایی از افزایش تمرکز نهادهای انتظامی و قضایی بر حوزه‌های مرتبط با سبک زندگی شهروندان منتشر شده است؛ روندی که به نظر می‌رسد بار دیگر کسب‌وکارهایی مانند کافه‌ها، رستوران‌ها، فضاهای موسیقی، پوشش و نوع تعاملات اجتماعی را هدف قرار داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/76539" target="_blank">📅 17:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76537">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f49d58cd5c.mp4?token=iwYdftr9Qgi3m27_8GBhvq8OZ8fQhEMr41Qt5pxu_4OViK8-IPkF4YoX6AeS7cX_K7VTFM-eH7JL9z59wYWg2vuhspSQn2DwpUYGh_LO3AAn1Z2q3CAo2FN7BFMcAL0DUmyTmvpHIZrBYXMNjkgqNq9Ozr0njLjO-Q9cyLCMEkRor5RHXRJGFHdk89XcCNmWQYM4XTNbw-iZlb2Uy3aqz3x38SADqU_CdtJAIfcUlwc5_xJ7fy6jw9q0vZ9IsTrnUhnpOELFv0sXW5x0PFoGgbP3QNPf8U11C5ae-Eddw-f8uHDlt4QxMJ7zth4PU9_PCxpNSSJOGfkfcMa5csnBtw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f49d58cd5c.mp4?token=iwYdftr9Qgi3m27_8GBhvq8OZ8fQhEMr41Qt5pxu_4OViK8-IPkF4YoX6AeS7cX_K7VTFM-eH7JL9z59wYWg2vuhspSQn2DwpUYGh_LO3AAn1Z2q3CAo2FN7BFMcAL0DUmyTmvpHIZrBYXMNjkgqNq9Ozr0njLjO-Q9cyLCMEkRor5RHXRJGFHdk89XcCNmWQYM4XTNbw-iZlb2Uy3aqz3x38SADqU_CdtJAIfcUlwc5_xJ7fy6jw9q0vZ9IsTrnUhnpOELFv0sXW5x0PFoGgbP3QNPf8U11C5ae-Eddw-f8uHDlt4QxMJ7zth4PU9_PCxpNSSJOGfkfcMa5csnBtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع‌های اعتراضی زنان به فعالیت‌های معدنی حوالی دو روستا در استان‌های کرمان و سیستان‌وبلوچستان با حضور نیروی انتظامی به خشونت کشیده شد.
بر اساس گزارش‌ها زنان روستای پشموکی از توابع فاریاب استان کرمان روز ۲۷ خرداد در ادامه اعتراضات مردمی نسبت به نحوه واگذاری و بهره‌برداری از معدن کرومیت پشموکی تجمع کرده بودند.
گفته شده که نیروی انتظامی علاوه بر ضرب‌وشتم معترضان، شماری از آن‌ها را بازداشت کرد.
هم‌چنین منابع بلوچ گزارش داده‌اند که زنان روستای سرسیاه از توابع تفتان استان سیستان‌وبلوچستان هم روز ۲۶ خرداد در اعتراض به گسترش فعالیت‌های معدن طلای تفتان و پیامدهای آن بر زندگی مردم منطقه تجمع کرده بودند.
در ویدئویی که منتشر شده شنیده می‌شود که مأموران نیروی انتظامی با خشونت، تهدید، توهین و واژه‌های تحقیرآمیز با این زنان برخورد کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/76537" target="_blank">📅 17:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76535">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nZVlQr44Zot-4mxux5ilzcRa_W1di2YvSLwhEnv0h7-CVMsg4b4k5T1BsllpzTpJ8DfJZhr7tmudW796-dkcEJV5K8wH8lgehN-JBZxLcXXM-p4M1_nm10pkY-vvqVSOxRFFlwdqqEaZ02Ml11vmrwQxl-_V721EZ06ImV2x6uNW-4tcw4hQotMB1_V2SCf8G_MRH6hnvXVFlOe7J56hZFgg6Rz-iziKZ1mNGat7fmkGUV7Nicl7Slu-lkKfPRfH4bd4e5rGq38Aa4wB59B35GRsDT01zlAoUxpzBH8gcev0yCsplJUv-0ibGN1XcZRLj-ES_l_mz70vVMOZnQjvzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v5QXqTdzV_bVvxfxHO6RWpPBHiwXVetNFlrt2-JNiVXPPBb81ZlLCktObOF9f8432ytoYCnNFt82hgnwXcfbku4_9UO_8zgbJmvJeg66MhYhnYbwnJZuK8aTqmqfIde85AzEUHOCgZAtHVMvWSZ-0YK9lycpvn6qYMuZET0roPchM4LLi22F7MXcV0lsqgboHkWAxhyio00zXgyZQjmD3TmxouCvNed8nY2-1HV4w2hSibhtdadMA8EkiQ9rFcZv9X6FmgX2KBVsz9-Q75scyz6dzDdk_MtMob3fjP9EPe5CUqd7Pv-U71EBHsUajO32y-I5jw5plQ-QNrQr2hOuUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک مقام آمریکایی به اکسیوس گفت: استیو ویتکاف، فرستاده کاخ سفید، در حال سفر به سوئیس است، جایی که انتظار می‌رود دور اول مذاکرات با ایران در مورد توافق هسته‌ای احتمالی برگزار شود.
به نوشته اکسیوس، قرار بود مذاکرات جمعه ۲۹ خرداد آغاز شود، اما به دلیل درگیری بین اسرائیل و حزب‌الله در لبنان به تعویق افتاد.
@
VahidOOnLine
خبرنگار اکسیوس به نقل از یک منبع آگاه، روز شنبه اعلام کرد: «عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، در حال برنامه‌ریزی برای سفر به سوئیس در روز شنبه است.هرچند این برنامه همچون گذشته ممکن است تغییر کند.»
این خبرنگار به نقل از منبعی در یکی از کشورهای میانجی فاش کرد که عراقچی روز جمعه به چند تن از همتایان خود گفته است: «موضوع آتش‌بس در لبنان برای ایران یک مسئله حیاتی است و حکم برد یا باخت (تعیین‌کننده سرنوشت) را برای مذاکرات ایران و آمریکا دارد.»
خبرنگار اکسیوس همچنین به نقل از یک منبع دوم از میان کشورهای واسط افزود: «ایرانی‌ها صراحتا تأکید کرده‌اند که می‌خواهند پیش از سفر به سوئیس، شاهد برقراری و تثبیت کامل آتش‌بس باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76535" target="_blank">📅 04:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76534">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e1550d193.mp4?token=swrfmr0oCHBpotqoCPNs8aYy0k4fV02HAN-1d1saXebyBVJxvoilN_MmVCctsU8RwY1SIRnUVX9Kf_ZjKvHgyQkXnUdKf71EW5Vw1HJBxeLy5ZkDpEQWcxXzUQPEmY5yVgsNyMTcVmFSeu7D61or5lTwB97bgCwYTNH2uRqRvP5JcY-IkVamEFveHa0qyvZzQzMTuqzfkOSYskgwfrXLpYaQLYhmMJ-63S6_-I2-ISAtiIC1n7r_DAFnU1Dil-EKA8ZDtnVVM1DrGpjCa9D9h5XryA7l2pSKHtVybSqHJ9i3uugjDqFYNNU5-3ywkfAes3k7pHVwD943jirNL5eN4g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e1550d193.mp4?token=swrfmr0oCHBpotqoCPNs8aYy0k4fV02HAN-1d1saXebyBVJxvoilN_MmVCctsU8RwY1SIRnUVX9Kf_ZjKvHgyQkXnUdKf71EW5Vw1HJBxeLy5ZkDpEQWcxXzUQPEmY5yVgsNyMTcVmFSeu7D61or5lTwB97bgCwYTNH2uRqRvP5JcY-IkVamEFveHa0qyvZzQzMTuqzfkOSYskgwfrXLpYaQLYhmMJ-63S6_-I2-ISAtiIC1n7r_DAFnU1Dil-EKA8ZDtnVVM1DrGpjCa9D9h5XryA7l2pSKHtVybSqHJ9i3uugjDqFYNNU5-3ywkfAes3k7pHVwD943jirNL5eN4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو بخش مربوط به ایران از مصاحبه امروز ترامپ
متن کامل این بخش‌ها:
https://telegra.ph/trump-06-19
بعضی از جملات همان متن:
ترامپ: و من آیت‌الله را کشتم. یک مقام سپاه هم بود. و متأسفانه به آیت‌الله دیگر هم آسیب جدی زدم. به شما بگویم، من او را ملاقات نکردم، با او صحبت نکردم، اما دیگران درباره‌اش حرف می‌زدند. او شجاعت خاصی دارد، چون به‌شدت آسیب دیده است.
با وجود همه این‌ها، نمی‌توانید بگویید بی‌خیال. من ارتششان را نابود کردم. نمی‌خواهم این را نادیده بگیرند.
برای کسانی که می‌گویند شاید من به‌اندازه کافی سخت نگرفتم، باید بگویم من ارتششان را نابود کردم. بزرگ‌ترین پلشان را زدم، چون دیر در جلسه حاضر شدند. گفتند این کار خیلی قشنگی نبود. من گفتم پل جورج واشنگتن؟ سه دقیقه‌ای نابودش کردم. خارک را زدم، همه چیز را، جز یک چیز. گفتم به لوله‌ها دست نزنید، چون نمی‌خواهم به اقتصاد جهان آسیب بزنم.
بنابراین فکر می‌کنم خیلی سخت گرفتیم. به کسانی گوش ندهید که می‌گویند می‌توانست سخت‌تر باشد. کل ارتششان از بین رفته است.
پرسشگر: چطور تغییر رژیم است وقتی هنوز خامنه‌ای جوان‌تر و خیلی از مقام‌های سپاه آنجا هستند؟
چون افراد متفاوتی هستند. خامنه‌ای جوان‌تر با پدرش فرق دارد. افرادی هستند که بسیار کمتر از دو گروه قبلی رادیکال‌اند؛ و من هر دو گروه قبلی را می‌شناختم.
اما به این فکر کنید: همه آن‌ها رفته‌اند. بعد می‌گویند چرا سخت‌تر نگرفتی؟ تنها راهی که می‌توانم سخت‌تر بگیرم این است که دو یا سه هفته دیگر وارد شوم و آن‌ها را شدیداً بمباران کنم. اما این چه چیزی برای ما به دست می‌آورد؟ تنگه هرمز باز نخواهد ماند. فرض کنید این کار را می‌کردم. فرض کنید تصمیم می‌گرفتم این کار را بکنم. الآن بازار سهام ما فوق‌العاده بالاست. قیمت نفت در حال سقوط است. قیمت نفت تقریباً همان جایی است که قبل از شروع کار من بود. تفاوت بزرگ این است که ایران هرگز سلاح هسته‌ای نخواهد داشت. آن‌ها هرگز سلاح هسته‌ای نخواهند داشت، روشن است؟ خیلی واضح و ساده است.
آیا می‌دانید در دو ماه گذشته، من کشتی‌های زیادی را از آنجا خارج می‌کردم و کسی خبر نداشت؟ می‌دانید چرا خبر نداشتند؟ چون ما رادارشان را از کار انداختیم. همه تجهیزات دفاعی‌شان را زدیم. آن‌ها قادر به دیدن نبودند. هفته گذشته، یک شب ۲۵ کشتی داشتیم، یک شب ۲۲ کشتی، یک شب ۱۹ کشتی، یک شب ۲۱ کشتی. هر شب، همه این کشتی‌ها بیرون می‌رفتند.
ایرانی‌ها مردم بسیار باهوشی‌اند. نوعی نبوغ ابتدایی دارند، اما باهوش‌اند. منظورم این است که باید جلوی آن‌ها را می‌گرفتم، چون اگر سلاح هسته‌ای داشتند، از آن استفاده می‌کردند. می‌خواستید ببینید؟ بگذارید چند شهر را در جایی منفجر کنند؟ مثلاً اسرائیل را منفجر می‌کردند.
اگر من نبودم، اسرائیل امروز وجود نداشت. چون من توافق باراک حسین اوباما، یعنی برجام را لغو کردم؛ توافقی که مسیری به سوی سلاح هسته‌ای بود. آن‌ها پنج سال پیش به آن رسیده بودند. به نظر من، در همان هفته اول از آن استفاده می‌کردند. اسرائیل دیگر با ما نبود. اگر من آن کار را نکرده بودم، اسرائیل سال‌ها پیش از بین رفته بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/76534" target="_blank">📅 01:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76533">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsDf3KAVY3XUM7ozIapvQNdicyBggVI8pO3rEg0J5mrSwWp-D-4SuMvoapz2N_JGqpbdY8vZM2ezwPEXmdMePicIiJtmrzC11fgvG_wNQIe7Jefdpi1GeAoXsRreI40KngDK0Wj59w7-5GUbMAB7NjC4SwmgBjhE6DzC2TlAeRaIBihjaz9sJU7VBKMT0Qo3ynL14lrDbqktpF3uZdVLsHxKz7F61-52bhvGcuGAdd3mxM1t5wIBs4surCCoCz8-xR1bG9dRqVmPuO9ri49dvn9-VzoAdpsT625S-tsHn5pvdnyr7R3b58su2umxArWbNUz1vbHPmvPR5VKwCbRbLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ، رئیس‌جمهوری آمریکا، در مصاحبه‌ای با برنامه «آکسیوس شو» با دفاع از تصمیم خود برای شروع عملیات نظامی در ایران، مقام‌های جمهوری اسلامی را «بسیار باهوش» و «نابغه‌های بدوی» توصیف کرد و هشدار داد که آن‌ها در عین حال بسیار غیرقابل‌پیش‌بینی هستند.
ترامپ با اشاره به مداخله نظامی اخیر ایالات متحده گفت: «من مجبور به اقدام شدم تا جلوی آن‌ها را بگیرم؛ چون اگر سلاح هسته‌ای داشتند، حتما از آن استفاده می‌کردند و با منفجر کردن چند شهر، از جمله در اسرائیل، هرج‌ومرجی واقعی به راه می‌انداختند.»
او با تاکید بر اینکه اگر اقدام او در لغو برجام نبود، اسرائیل سال‌ها پیش نابود شده بود، توافق دوران اوباما را مسیری هموار برای دستیابی جمهوری اسلامی ایران به بمب اتم دانست. ترامپ همچنین با ابراز شگفتی از زمان‌بندی تقابل با ایران افزود: «چیزی که مرا غافلگیر کرد این بود که آن‌ها این‌قدر منتظر ماندند. آن‌ها صبر کردند تا من به قدرت بازگردم؛ البته این کارشان عمدی نبود. هیچ‌کس، حتی با وجود سلاح‌سازی ساختار حکومتی علیه من، فکر نمی‌کرد بازگردم، اما من با خروشی بزرگ‌تر از قبل بازگشتم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76533" target="_blank">📅 22:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76525">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشجویان متحد</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lost6xdtlEk3Wz3fGs3iKpJVAe9_pqo5v9_cMnWx_Yegak_q0L4VRIgg3-jCTU3bWRcLdjSvbPOoXiIkoX3umtO81SSdAIx2vKj_K2iYukbV0KgPXLI_vcnBw_p9kX81EvTvoslOYTkPHNtuYMFGMVyFl4RQhZOEo1pnHp-4evhqDZHEWIpAvHANTqHgLbERm6GRtBhQw8LUMP3ajYNYFCzM0ez4w4_5UrKJVl9CBScbP262DIfPiJQkqZqoG8EC1SwxhEevOEUG8xSI4WsHrA3V2VCYIsho5YQm4QWPnatXOt5pAtxJE_H2yoimL_lsJcIQnq0sjLM7qQ7usHbXIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CA0bOyDnuCVsUe8JNwWVpUsExuAV8I3h_tk806qS_cQD4LB2OhFCNq__cAoCMbEmn2eDPxUC1VzbLA4iBLzhwVZRZ5H5hzJrQ2AWG7yDKJ31H4vO9iawhIkQhUPf084oKXkaEAPuIiJUT1dOsq6c_0uyTttUDbRLDFT4_069cfamcWINRJ8M75pbbp966f_RtSwvAblPlYRpqp6dbFi8HSVb-euHhIc1O-shQnsu41XWvVRxzjOKVc_79P7dKkon3SSKrnyl9YHC6OPmLi_9s3WrupUubTC1uc6K3siEAdu8yPRUJWLrQQTtBXzzWO8I8STnzBrSlEaGQ0ubWg2Qhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pyhpO1YMghv9uo6zXHgQbcmoTu6aTa1zJo8x3oHhXZZo8OT15DIpDvnlwiVEK0h_HLu_pKuIM283Omz-GIVY3_j5zVZ6a_h-DNwBkJFxOicI2jxLbli3rabG0UxrLu__3-KkrSzPAdt3uoUPsOAAZ8NFghyDQO1mS_Io9tosT7_czdfH8Cx4MFN2WLZokKM5GfqmIU49A2Ua9KeMSjLGXMQtraSjXIMmWriq3XFwpHeHJOHx_Q8N5ifwMyB3E_RRZ-ajgq6vq0hTjMD18dWSXyznB1d9veca9Fne1MXLbiFogyOBuespLv8mNo9kYYX6XNC1P63DJNOgN4RowzjmWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H_ll9a7i1i50yoVk4flVHXO3MRiAFsRUhoSZbMFcDwbbdzI5SsiGQ03H-_pCSaL72q2Ljb8Qwp6Zt6fM7thtyJ4hqG-WmLiIsV_6Ft8N3_76QPFK9uP1TGwAWrCHAUZ4HNg5oEWjC1CQWSIMvK38gmR82ZDraIcAAV2mE5OMxYG-40XzPuV6xNiQkqiSq5A3EpsUjmcT8hk3eazMLNqvneA_0dPIvWxORUK6MPRXra2JXR8rZB44YZ8S7XNO1kCkyuk89dZBFyg6k1tIpm4SXuS9SqbMYZzk727d_guud8dVkh_PpSQCYWs1l_Hja9_rtUGFIg5VV_vmm14XVIuHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CHW8x8EmPGwrwVjVmtaz5IiLrDyag3GMA67J0_Qd-Rjqh63m3C1CduqWugihCxS9LGjUF1VpGMXQI16OClM_5rKbpKrJe4LI_ahSKudIKwUYdD5knlP7gocvXz4dNo6BQVX55MSVpyCJb-Zo7zpoX_NIC1J0Gftb-jZj0cJPRNa8yZD-nLRJxZlxoHIREPdP-6EG_mo0Yqb2UsQYnp-aSBNFrG-kwsLCBc2Riun4fU7YS2YYFbiCWQvRCrg5zg3Ex_zjRa2z0xA3THendRNDia_gq7_W2sAaIEJPR8S52PryN8fHy5UTQNjFLIxT0BUaikuvdKAlOCn3sJ5mbFzxwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IZuDez90CwSz7p1w3VY6gGDVLkbIOATizvLidcxKzlmvRMa76tbK8DdbO9U3gECTL-IQHI2TzkA7JcTyS0D_lFnFMu0Q_co8PivVfDtyD4pwB2cpza-JCOX14ipkyD3FpCPnZQldB5q1MIXplHokEMgq96N6tUyuB88Oz36oz653eLHNaeustHzLG3jcxycQ3ZfJ_VhQv8AO2PzvXkdsqmSeenFw0PVnm7tjNg_P0dUNU0S8UR-iyATdT4tUOnltxp6WoeYFDmZJKkHG4eQK6Xdh_bVvsV69yRJM1EffUDEmE-CfNF_PbRVzbtw-hoi_6Xbzmq8dlUti9ZJnQBTvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qtnUx8Td6023Z-zMPxVGHDj3APocXLWe_qv8YKBVGqgpIxaxhvwmEG7aX5-nViC_3kD3T_4LtrpjLmV8T00E5yvmQyKeF6Z7SLr04Dq6yEvGk-EBsNA17kwuSLvJ1V21I-vZ24GlXwjnHRS6VKAXP_RpdShA-kJB1yM5AU6BB6TKttPF3AMloq4uw41viyWBqlVcp0zKqX4CbbOMnCBG8HicyvxNTs-5qlDkcOEzI_Qk_BCiT6xdfoazVHSRP4C3ADPKXCnKjPy2gTrKc5rGXHW5msutd3mDDIVDJuNxSD2yWVO2C_0Uavuveunqd-UlgdSBsr96X16Bd31p-KbCDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j0Jwn7TzKtCrYVsQf7rvLEwRve5P7KOdbfG8FN13D96xUG5bEnKdpRW3aNOaSyafRo8RdSVRv5lsy-E41w8KNkX29E2Qa3C196lwNkqymvNe0JhfesBUhfoD273OcBGEnEBb8gA1VVZ0hrbzhFiZZzsZdc4VfEuOfFlg-07q5vqinaip6hOyRJ3Z7n7qJhvgKibpn5GIxjEmWjD6M9BjJjiEW8Imyh98egjNBGvTbW99VVHgp35WwZhOCovd3YcqmP39Iz3gpzpEdAby9uWctu-p5gFRcuSr4l5BqePUEd33-i5eWIJEnBU9ucTkQUcvkQSJ7ODt8qADno1vn0XDig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭕️
صدور حکم اخراج برای هفت دانشجوی دانشگاه شریف؛ صدور حکم غیابی برای یکی از دانشجویان بازداشتی؟
🔻
بر اساس گزارش‌های رسیده به دانشجویان متحد، کمیته انضباطی دانشگاه شریف، برای هفت دانشجوی این دانشگاه حکم بدوی اخراج صادر شده است. اسامی دانشجویان به شرح زیر است:
🔻
رضا دالمن، ورودی کارشناسی ارشد ۱۴۰۳ مهندسی کامپیوتر: اخراج و چهار سال محرومیت از تحصیل
🔻
فاطمه خاکپور، ورودی کارشناسی ۱۴۰۳ شیمی: اخراج
🔻
حسین شادمان، ورودی کارشناسی ارشد ۱۴۰۴ مهندسی صنایع: اخراج
🔻
سپنتا سعیدی، ورودی کارشناسی ۱۴۰۴ مهندسی کامپیوتر: اخراج و پنج سال محرومیت از تحصیل
🔻
مسیحا باقری، ورودی کارشناسی ۱۴۰۲ مهندسی کامپیوتر: اخراج
🔻
فریبرز کهن‌زاد، ورودی کارشناسی ۱۴۰۰ مهندسی برق(تغییر رشته به مهندسی صنایع): اخراج و پنج سال محرومیت از تحصیل
🔻
پرنیان خدابخشی، ورودی کارشناسی ۱۴۰۲ مهندسی و علم مواد: اخراج و پنج سال محرومیت از تحصیل
🔻
همچنین در برخی رسانه‌ها خبر صدور حکم اخراج برای «آریانا کوچکی»، ورودی کارشناسی ۱۴۰۰ مهندسی صنایع، نیز منتشر شده است. هر چند بر اساس گزارش‌هایی که به دست ما رسیده، ایشان در حال حاضر بازداشت هستند و خبری در مورد برگزاری کمیته بدوی ایشان نداریم. هر چند صدور حکم غیابی برای دانشجویان بازداشتی در جمهوری اسلامی، پدیده تازه‌ای نیست.
🔻
لازم به ذکر است از میان هفت نفر یاد شده، کمیته سه تن(سپنتا سعیدی، حسین شادمان، مسیحا باقری) با محوریت فعالیت در شبکه‌های اجتماعی و کمیته چهار تن دیگر با محوریت اعتراضات اسفندماه برگزار شده است.
ارتباط با ما:
@Public_anjmotahed
🆔
@anjmotahed</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76525" target="_blank">📅 22:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76524">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ba856aba9d.mp4?token=uGB9J7LVNoTUXN3YFlp6rn5j9AtNUPfy_qmT4nbHEq9H2e-8Sr-izhr3Y7yOe2zCJuzYLcnDW3CQXshSsFlVYC0wQ-V_72RiG4mTn_LEeihJ73p4_kGBra8aDfO6CnhtQOsCmMTtLPjJFCAtKBxSXMIQhHE-F1kjWZXVYme8RXA2KMZr263dSFLPO56HIy7rdtEhBElF3VKR4-jcvsJMWiF6VFwUC1ns_e6NJkogNiYFBihQGqNwhXZWkmxOjG0ZT7qAca2pabWwi5Smk93UmxoxwgjQlOu1gtqgR4Qg2OocZf0XMQWievnX3MItX-P_JxBZnmlW1ZQvJOXhmId67g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ba856aba9d.mp4?token=uGB9J7LVNoTUXN3YFlp6rn5j9AtNUPfy_qmT4nbHEq9H2e-8Sr-izhr3Y7yOe2zCJuzYLcnDW3CQXshSsFlVYC0wQ-V_72RiG4mTn_LEeihJ73p4_kGBra8aDfO6CnhtQOsCmMTtLPjJFCAtKBxSXMIQhHE-F1kjWZXVYme8RXA2KMZr263dSFLPO56HIy7rdtEhBElF3VKR4-jcvsJMWiF6VFwUC1ns_e6NJkogNiYFBihQGqNwhXZWkmxOjG0ZT7qAca2pabWwi5Smk93UmxoxwgjQlOu1gtqgR4Qg2OocZf0XMQWievnX3MItX-P_JxBZnmlW1ZQvJOXhmId67g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه جی‌دی ونس با زیرنویس فارسی
گفت‌وگو با:
الی بث استاکی، مجری و مفسر محافظه‌کار مسیحی آمریکایی، میزبان پادکست Relatable در شبکه BlazeTV
برنامه‌ای که در آن از زاویه‌ای مذهبی و راست‌گرایانه به سیاست، فرهنگ، خانواده و مسائل اجتماعی آمریکا می‌پردازد.
او در میان مخاطبان اوانجلیکال و محافظه‌کار آمریکا چهره‌ای شناخته‌شده است و در این گفت‌وگو با جی‌دی ونس، معاون رئیس‌جمهور آمریکا، درباره ایمان، خانواده، سیاست داخلی، اسرائیل و توافق با ایران صحبت می‌کند.
یک ساعت درباره مسیحی زندگی کردن
حرف زدند
و ده دقیقه درباره نقش و نفوذ اسرائیل در سیاست آمریکا و توافق با ایران برای مخاطبی از اون نوع
اینجوری می‌پرسه: می‌خواهید یک مادر معمولی چه بداند؟
متن این دقایق:
https://telegra.ph/JDVance-06-19
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/76524" target="_blank">📅 22:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76523">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvpCUqIxfClUPgj1Vj4HxnZ5VMZ9qWMZppwsizX113JE2FFlQYxPd_4SPwNukGkEfym1KtEwnybLE61Ebr-ki7R9aCf_6cqstJ7BbcWKlCPTFB4GwAjFezoKrMFxQv1Z4HYefH9moL9z2AOZvZZA1dy3ArMH7H46Fx44r2R5Y21kq8TM5qTsdtynTCHQ2axGUyoCO4E1KOPrEm2vZYnMTYS3jJLytY4JIFgh9buIcIZ8ROUrjbis9HeArBY9mIs6AN2hTD93iMXKsu_Z64RCfiQz9The_bcUEsj82MKDh0SezhIzSgafKo1dKczGHw8nNmAt_YJThVtcVNz0l3ZHxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در یک گفت‌وگوی تلفنی با شبکه ان‌بی‌سی نیوز گفت که روز جمعه با مقام‌های اسرائیلی صحبت کرده و از آن‌ها خواسته است با گروه حزب‌الله بر سر آتش‌بس توافق کنند.
بر اساس مطلبی که خبرنگار این شبکه در شبکه ایکس منتشر کرد، ترامپ به این مقام‌ها گفته است: «بعضی وقت‌ها فقط باید آرام بگیرید و از عقلتان استفاده کنید.»
این خبرنگار همچنین افزود که ترامپ مشخص نکرد آیا مستقیماً با ‌بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفت‌وگو کرده است یا خیر.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76523" target="_blank">📅 22:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76522">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iV2cj-KFsXwzKWXd5FHBMw9tQDHhzkK39r6mank8vq-x6CpGLmbD_qP3VeENKul-u61Zz5FkMTCRoGTzvZl7Iswx_ZrH5UQW1pvTKAJQ7OAjYQCxprxwuq6hxD0xOPb3BFXf5A8fK6pZ8bgt97HyNDKvCMVvo9W-5sLcYvpOwJJOlFbrNqt96hmKVYVM10mAbKqxcZNhackx1zLK6g2EIcMtmAsesV6sVV4gXXwd6vaZSsFMGK7nmZQccgNJk5rXPDq8XBDocQ5IQv1ITQaI1zgfOEMlWsGGUSMFw8TD4TebSDiMCzs2mva3kqUK6YhblQ7Pe1DB0GXgvfj2dqZN0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نعیم قاسم، دبیرکل حزب‌الله لبنان، گفت: «تا زمانی که توان ایستادگی داریم، چرا باید تسلیم شویم؟.»
او تحویل سلاح‌های حزب‌الله را رد کرد و افزود این سلاح‌ها برای مقابله با اسرائیل هستند.
نعیم قاسم همچنین گفت که ما تصمیمی «به سبک کربلا» گرفتیم و این تصمیم همچنان به قوت خود باقی است.
دبیرکل حزب‌الله لبنان ادامه داد: «ما وحدت نیروهای مقاومت را حفظ کرده‌ایم و وحدت جنبش امل، حزب‌الله و سایر نیروها همچنان در کنار ما برقرار است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76522" target="_blank">📅 20:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76521">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOjCxhizMUE_wv1jkGUlazRbXqXpMu-AfeLccvpCh57UX6bl7BOtWaL-CdrxkoLELmis7oSN2rAhRpx49GpdAw5StHwyEnJa58BMYoOtxb-iAVBGmjjitNPo4b5UObVhNqr2TdDpXOCPzBY7x0Hcq1zx45xbzQse6XP95iyj4ixnuNDY3USuEQsRVzoXNxeRwwypIib8h0PBEvoMQ7WxPcA9nQODdukY0B8_edMDIdM8Gjhr1kbkcIPtaZXIqTeN3SFXFIBLUBspWRsTCvR60d7O2ctRqqgPnL6JPHikHzFS4Ex8BjJO5VCL8E5h-cwoI41G1gaCTFpx4el54-ysdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت خارجه ایران، روز جمعه دعوت جمهوری اسلامی از بازرسان آژانس بین‌المللی انرژی اتمی برای حضور در ایران و انجام بازرسی از تاسیسات هسته‌ای را رد کرد.
او گفت: «بازرسی از تاسیساتی که دسترسی آژانس به آنها به‌دلیل حملات نظامی متوقف گردید، منوط به روند مذاکرات و نتیجه آن خواهد بود.»
پیشتر جی‌دی ونس، معاون رئیس جمهور آمریکا پس از اعلام توافق اخیر در گفت‌وگو با شبکه ان‌بی‌سی گفته بود که بر اساس تفاهم‌نامه میان واشینگتن و تهران، بازرسان آژانس بین‌المللی انرژی اتمی «قطعاً» به ایران بازخواهند گشت.
اسماعیل بقائی همچنین گفت در حال برنامه‌ریزی برای برگزاری یک نشست طی روزهای آینده هستیم.
نشست بین نمایندگان ایران و ایالات متحده که قرار بود جمعه در سوئیس برگزار شود، لغو شد.
سخنگوی وزارت خارجه جمهوری اسلامی اعلام کرد: «با توجه به اینکه امضای متن یادداشت تفاهم در بامداد ۲۸ خرداد به صورت دیجیتالی انجام شد، برگزاری نشست مزبور در سوئیس فوریت ندارد.»
او همچنین گزارش‌ها درباره بسته شدن تنگه هرمز را «بی‌اساس» دانست و گفت کشتیرانی در این مسیر در حال انجام است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76521" target="_blank">📅 18:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76520">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCn02Pw7hpSP1PpuPNSfUeOdLA8_P5_viAEytkrgFsi3ro4lqBPJEhstytmjZhOX5OvcnWJEGTe6sgiGE80H3EAD0OvCVzj0XMIS_-9B1GvlMJfZzIZdeXyCK9mO4SGokznshEExq3AmkAuEm3KsTv3LlNRG8Y5xmbK4aR6TkjrD2ijm23xlZnhK6sjcj7dGZSvlhLqWj_pK7u8i9FYqmz5PKI5kg8tRAtHxpekI18UXuWHsIhaBHn2v0JYks0GpkyKX-dodh520mHieHGnLwldnRkBd1ZvAmPrTEXMZNF98sk-kYkPkHJwn0QnglDmLmkMqgtff9BnRtTSCkdaK-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی به رویترز گفت که اسرائیل و حزب‌الله بر سر یک آتش‌بس توافق کرده‌اند که قرار است از ساعت چهار بعدازظهر روز جمعه به وقت محلی آغاز شود.
این مقام که نخواست نامش فاش شود، افزود که مذاکره‌کنندگان آمریکایی و قطری با کمک ایران این توافق را نهایی کرده‌اند.
این مقام همچنین گفت: «درک ما این است که پس از تبادل آتش امروز، اسرائیل و حزب‌الله اکنون در وضعیت آتش‌بس قرار دارند.»
شبکه العربیه نیز به نقل از یک مقام آمریکایی از توافق برای برقراری آتش‌بس بین اسرائیل و حزب‌الله از جمعه خبر داد.
این در حالی است که نخست‌وزیر اسرائیل ساعتی پیش اعلام کرد نیروهای نظامی این کشور تا هر زمان که لازم باشد، در خاک لبنان باقی می‌مانند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/76520" target="_blank">📅 17:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76518">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BSLtOOigbFpPGtXDPbPScA6oDr-TvYU8gSbLlGhihlRqRqyF1926UAfkRskbI9PIguhdBFnlQq6neFCZxeaa9ldHNBQkcjlFv9poy5cdDD1UhtRx-B1PAZ2y6kqorLy5iKSXUY4_Z9lyNrksUV59YcMkF9ysd8hstDg2d2i89wI0ySwjs9UU2ss5K_B_pphPZHZewWsIxTIOo2vbJ6dpQFjmUBoHRm5ov7FmmGnlHBl-eBBehMEnLo1wMEMaqQ-S6dd8HQkwe8N0TDYoYDc95RS2hkVVAhAvPDu0uP52TfQFYTT2ujkMrnmDjhcQe_57FwCM_JLuonXeDGL4Gq5Mzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/957528437f.mp4?token=WcLNI5xfTeuzbJ0hGzuIVb4u2YwInSKkzadxFHMct4e28LdA4UX1ZGomJmaCBM2jac2pTpk33E-_LTycIFG9wDnAvVcXVLm49Kxo-D7zDjcWRzHpFTCbefr0GBx212GhnmneyR2vYLQzhTF0AKdPE7nz0bMDLNEZwieRPF2iffCCJehuW7hudXkPfz1DnDg7C19Qn2H8BrU5xg7OrGwPTH2sd219lg6BwDZVHPTSQHMroHrhbgeH2i2Yr5B9WWorapjFs-tcrXbgTx-ShEZ3m3lxWR6y-k8kmucaTZy4P1N5myW3O78d9-_93h6ib87XFzIriC-G2UHjsh0VnRvrJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/957528437f.mp4?token=WcLNI5xfTeuzbJ0hGzuIVb4u2YwInSKkzadxFHMct4e28LdA4UX1ZGomJmaCBM2jac2pTpk33E-_LTycIFG9wDnAvVcXVLm49Kxo-D7zDjcWRzHpFTCbefr0GBx212GhnmneyR2vYLQzhTF0AKdPE7nz0bMDLNEZwieRPF2iffCCJehuW7hudXkPfz1DnDg7C19Qn2H8BrU5xg7OrGwPTH2sd219lg6BwDZVHPTSQHMroHrhbgeH2i2Yr5B9WWorapjFs-tcrXbgTx-ShEZ3m3lxWR6y-k8kmucaTZy4P1N5myW3O78d9-_93h6ib87XFzIriC-G2UHjsh0VnRvrJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر امور خارجه ایتالیا روز جمعه اعلام کرد در واکنش به گزارش‌ها درباره اظهارات دونالد ترامپ سفر برنامه‌ریزی‌شده خود به ایالات متحده را لغو می‌کند.
آنتونیو تایانی در شبکه اکس نوشت: «سخنان شدیدا توهین‌آمیز رئیس‌جمهوری ترامپ… به همه مردم ایتالیا اهانت می‌کند.»
به گزارش شبکه ایتالیایی «لا۷» ترامپ درباره دیدار خود با ملونی در نشست گروه هفت گفته بود: «ملونی آن‌قدر می‌خواست با من عکس بگیرد که فقط از روی دلسوزی با او موافقت کردم.»
@
VahidOOnLine
جورجیا ملونی، نخست‌وزیر ایتالیا، در واکنش به اظهارات اخیر دونالد ترامپ، رئیس‌جمهوری آمریکا، این سخنان را «کاملاً ساختگی» خواند و گفت از نحوه رفتار او با متحدان «مبهوت و شگفت‌زده» شده است.
او تاکید کرد: «نمی‌دانم چرا رئیس‌جمهور ایالات متحده این‌گونه با متحدان خود رفتار می‌کند» و افزود این نخستین‌بار نیست که چنین مواضعی از سوی ترامپ مطرح می‌شود.
ملونی همچنین این رویکرد را «مایه تاسف» دانست و گفت او قاطعیتی را که در برابر دشمنان غرب نشان نمی‌دهد، در قبال برخی رهبران متحد خود به کار می‌گیرد.
نخست‌وزیر ایتالیا در پایان تأکید کرد: «یک چیز را باید به خاطر بسپارد؛ من و ایتالیا هرگز التماس نمی‌کنیم.»
در ادامه این تنش‌ها، آنتونیو تایانی، وزیر امور خارجه ایتالیا، نیز اعلام کرد سفر برنامه‌ریزی‌شده خود به آمریکا را لغو کرده و این اظهارات را «توهین به مردم ایتالیا» خواند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/76518" target="_blank">📅 17:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76517">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکمیته پیگیری وضعیت بازداشت‌شدگان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9aVmh8JHDgI5mjeQzSxCHUKJcoTEZngrl9PK_XeySMkffOT4IEX2KRlRFk7FLPWXwj5tLPZMugIqawLelbJazItmCyaDge1CXMeK8iR7CY-pp_DVJwPtHFZ81WsmysOSi_z9aM39-aWW82tviP2msTbpkKJGbUHPztKmJukNLHDPWfFFZjmXf4hDG0rcDSq-MPj_iDSDIOCby67emjsyd04oOs4jPEL09KRyoXN1EaRDXiJJuMvXf4Z3kn-MjLtEC3IVxyNRw5j--KeUH4Wo4wyLcv5Zyv4Gq34j68aRRgvXYT3TZqVZAxbpE_ReFPC-MmXV2V_RGujvQ6u2-Uyfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅️
#محمد_نوروزی
، شهروند افغانستانی ساکن ایران، که در روز ۲۵ دی‌ماه ۱۴۰۴، در منزل مسکونی‌اش دستگیر شده بود، توسط دادگاه به شش‌سال زندان محکوم شد.
🔹️
طبق گزارش رسیده به کمیته پیگیری، محمد نوروزی پس از بازداشت به آگاهی ملارد منتقل شده و پس از ۴ روز همراه با ضرب‌وشتم فیزیکی به زندان قزلحصار منتقل شد. او طی این مدت مدام تهدید می‌شد که رد مرز شده و از ایران اخراج خواهد شد.
🔹️
او در نهایت با قرار وثیقه یک میلیارد تومانی از زندان آزاد شد و سپس توسط دادگاه به اتهام "اجتماع و تبانی و تبلیغ علیه نظام" به شش سال زندان محکوم شد.
این حکم هم‌اکنون در مرحله تجدیدنظر قرار دارد.
🆔️
@Followupiran</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/76517" target="_blank">📅 17:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76516">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aX8Zn3e95WgZz1HEnFj2XLwXI_gxCD1s4e9dsZSXeHouW7jCkcUfr9HyGyOgAlESDAwYn1oALeKaVx3KmVZNz0cCgsPZ0Jsoty6UZAO1PPCBobh-7OsklHbjbjaZYuwimWS92G5UUks3zVw-BnTlc9RFoOETv6P1Ct2kUlyyGI9-kiprUTBvnQvWvXkcSF_3qJ45uTWngXOCM9jw3RE3x1CxCvqDIqiTWQ2GjozddpAHwefya0NRJ27BmGO9pGWp3F9p4R9E5NNG9lHXJitcSBkKOKy_a50D_zVOGwgdLzGO9qQp2yNVC-jJHxaCPoDHSfNm889hdk3cWRA3yh7ySw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز جمعه بار دیگر گفت که نیروهای اسرائیلی «تا هر زمان که لازم باشد» در لبنان باقی خواهند ماند و وعده داد که حزب‌اللهِ مورد حمایت ایران برای حملاتش «بهای بسیار سنگینی» خواهد پرداخت.
او روز پنجشنبه، ساعاتی بعد از امضای تفاهم‌نامه پایان دادن به جنگ توسط ایران و آمریکا، نیز بر ادامه حضور ارتش اسرائیل در مناطقی از جنوب لبنان تأکید کرده بود.
نتانیاهو در بیانیه روز جمعه که پس از اعلام کشته شدن چهار سرباز اسرائیلی در لبنان از سوی ارتش منتشر شد، گفت: «اسرائیل حمله به سربازان یا قلمرو خود را تحمل نخواهد کرد و بابت این حملات بهای بسیار سنگینی از حزب‌الله خواهد گرفت.»
او افزود: «اسرائیل تا هر زمان که برای حفاظت از جوامع شمالی لازم باشد، در منطقه امنیتی جنوب لبنان باقی خواهد ماند.»
یسرائیل کاتز، وزیر دفاع، نیز گفته بود که ارتش در لبنان خواهد ماند و افزود که به هر حمله‌ای «با نیروی قابل توجه» پاسخ خواهد داد.
لبنان اعلام کرده بر اثر حملات اسرائیل در سراسر این کشور ۱۸ نفر کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/76516" target="_blank">📅 17:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76515">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q51fAPbqyoBjUTL-BhAisorejLpg-wrLIxtLUU0XOeZGI9Ofc_DQBWv8Jo5s-51YiagFIOYGLiRg32Rfppiu3NVPhA1KkpEPXkRjPE--qcvptvevb33t24moMRX9MSkhtgNUaCDzeMezGQ7RyY_eiEOEaReTMvflwEQm2TZiBIzfRrQ-5T_j0mttvEEdFL4hnapVplKeJKrjZ3MDEsib1d6lSfowSOlpghPoWh9rXHX95tx4BVilRM6W4u0ngemmrUDGGj3qGqI8OoAX_aZjuJPKIK4MSDZblbRq0YbifnFdMdSmodzLYIi5RWTuzpKm5kPVxIygF-cjPIs75xDrLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینعلی شهریاری، رییس کمیسیون بهداشت و درمان مجلس جمهوری اسلامی، در گفت‌وگو با دیده‌بان ایران، با اشاره به ادامه «تعطیلی مجلس» گفت: «مجلس را بستند تا هر آنچه خواستند امضا کنند.»
او با تاکید بر اینکه تفاهم‌نامه با آمریکا در نهایت باید به تصویب مجلس برسد، افزود: گذشت آن زمان که برجام را در ۲۰ دقیقه در مجلس تصویب کردند. ما یک بار از این موضوع آسیب دیده‌ایم و نباید دوباره همان اتفاق تکرار شود.
شهریاری همچنین از اظهارات عباس عراقچی، وزیر خارجه جمهوری اسلامی، درباره احتمال رقیق‌سازی اورانیوم غنی‌شده انتقاد کرد و گفت موضوع هسته‌ای نباید در مذاکرات مطرح شود، زیرا به گفته او «جزو خطوط قرمز» جمهوری اسلامی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/76515" target="_blank">📅 17:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76514">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jAsCUon2wpXSfWEv5mQYhCvVHTHFF6f8KUj-o4EJryDCj3zzFKflcDNeEEOb8voyopKcnZbJxjy0Ln65T7zDwZ62PY4aOmq-1l0kkQkFGa_LY2v6BtAWDcWAGR5Osd8esh_Z510wHZ3pxYsakKvmfTYsVXJt8f0uhqo6343ywCkKIZKQ23G6M8SFy8hOieQ2AFOhors0Ujc1_DWV5EIW9I6gX07mfMYg5p2Q2kx3_xKJeL2sGtqqJO9ggr6jqCgACrqpP35ZXd8YokG022OQPzHV1QjSV5k9uuGNTOS02yv4ML7IJeKVA90Jo78_zl2zmPd0_8vFUkd8Yh0eOw2X-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام پیشین مرتبط با تحریم های ایران درباره «صندوق ۳۰۰ میلیارد دلاری»: پیش نیازش لغو همه تحریم هاست که دکمه روشن و خاموش ندارد
میعاد ملکی، مدیر پیشین «دفتر هدف‌گذاری تحریم‌های خزانه‌داری آمریکا» در یادداشتی درباره موضوع «صندوق ۳۰۰ میلیارد دلاری» برای ایران که بسیاری از کارشناسان درباره آن ابراز تردید کرده‌اند، می‌نویسد: با کنار گذاشتن موضوع معافیت/مجوز نفتی و نگرانی‌های مربوط به عدم اعمال تحریم‌های جدید، باتوجه به الزامات برای اجرای واقعی بند ۶ (صندوق بازسازی ۳۰۰ میلیارد دلاری) و بند ۷ (لغو همه تحریم‌ها) به این نتیجه می‌رسیم که مذاکره‌کنندگان آمریکایی یا می‌دانستند که توافق نهایی ناممکن است، یا این یادداشت تفاهم فقط تصمیم‌گیری را به آینده موکول می‌کند.
ملکی که خود در طراحی تحریم‌ها علیه حکومت ایران نقش داشته در این یادداشت می‌نویسد: این چیزی است که «اجرای کامل» در عمل، فراتر از امتیازهای هسته‌ای، به آن نیاز دارد:
بند ۶ — صندوق ۳۰۰ میلیارد دلاری:
صدور معافیت ریاست‌جمهوری از تحریم‌های الزامی بخش ساخت‌وساز ایران طبق ماده ۱۲۴۵ قانون IFCA (معافیت‌های ۱۸۰ روزه قابل تمدید که در هر دوره نیازمند اطلاع‌رسانی به کنگره هستند).
خارج کردن سپاه از فهرست سازمان‌های تروریستی خارجی (FTO)، زیرا در غیر این صورت سرمایه‌گذاران با خطر مسئولیت کیفری به دلیل «حمایت مادی» مواجه خواهند بود و هیچ مجوزی این مشکل را برطرف نمی‌کند.
استفاده از معافیت مبتنی بر منافع ملی در قانون ISA (قانون تحریم های ایران) برای سرمایه‌گذاری در بخش انرژی و نفت.
در نتیجه، هیچ نهاد سرمایه‌گذاری حاضر نیست میلیاردها دلار سرمایه را بر پایه معافیت‌های شش‌ماهه قابل تمدید متعهد کند.
بند ۷ — لغو همه تحریم‌ها:
ماده ۱۰۴ قانون CISADA (قانون جامع تحریم‌ها، پاسخگویی و واگذاری سرمایه‌گذاری‌های مرتبط با ایران) رئیس‌جمهور اختیار معافیت ندارد؛ تحریم‌ها الزامی هستند و لغو آن‌ها مستلزم تصویب قانون جدید در کنگره است.
ماده ۱۲۴۵ قانون NDAA (قانون مجوز دفاع ملی آمریکا) معافیت‌های ۱۲۰ روزه قابل تمدید که در هر دوره نیازمند ارائه گزارش اجباری به کنگره هستند.
تعیین بخش مالی ایران به عنوان «نگرانی پول‌شویی» تحت ماده ۳۱۱ قانون پاتریوت: این موضوع نیازمند مقررات‌گذاری جداگانه از سوی شبکه مقابله با جرائم مالی وزارت خزانه‌داری آمریکا (FinCEN) است و صرفا از طریق دفتر کنترل دارایی‌های خارجی (OFAC) حل نمی‌شود.
تحریم‌های مرتبط با تروریسم، حقوق بشر و موارد همپوشان با پرونده روسیه: هر کدام مستلزم اقدامات حقوقی مستقل و جداگانه هستند.
ملکی در ادامه می‌نویسد: «لغو همه تحریم‌ها» یک دکمه روشن و خاموش نیست، بلکه پروژه‌ای چندساله در حوزه قانون‌گذاری و مقررات‌گذاری است و کنگره نیز در آن حق رای دارد. و این پرسش مطرح است که چگونه می‌توان اتحادیه اروپا را وادار کرد محدودیت‌های مرتبط با ایران را که در چارچوب پرونده‌های مربوط به روسیه وضع شده‌اند، لغو کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/76514" target="_blank">📅 17:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76513">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/am7Bilx3Oye9FKlrI5_Xoohy-VpFG7Xif6U1ZmqLtoC7GRQq5ZJeHdRDkvP6fANBV8N9l8Ftoo4UkyzelepCXRu2TcdfRU91seh4DasSfOoIhKwRFXWCrtwYRxSUSUko6CyLAukNkuDJfHiMDWmP0uOA6Xes4nOTSBnqDCqKj9dh38HdbuI0O-LXvwwP2cktAiVggc3csA9Fpf268rHG99fm6DAh9vpLCKl8oVtEkh6GRJJgeNoypMItNUp9ic4AWavHpqjklZK-4EYfae5QhT8yQKxznOT2V-ozHvstptkSfVIP2ExZp58fUVY9jjaoZuO6uQv6xB_NzhFZY_febA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه هاآرتص در تحلیلی نوشت توافق دونالد ترامپ با جمهوری اسلامی، برخلاف انتظار بنیامین نتانیاهو، نه‌تنها به تقویت موقعیت سیاسی او منجر نشد، بلکه شکاف بی‌سابقه‌ای میان واشینگتن و تل‌آویو ایجاد کرده و نخست‌وزیر اسرائیل را در آستانه انتخابات با بحرانی تازه روبه‌رو کرده است.
روزنامه هاآرتص در تحلیلی نوشت نتانیاهو امیدوار بود سفر ترامپ به اسرائیل و حمایت علنی رییس‌جمهوری آمریکا، مهم‌ترین برگ برنده او در انتخابات پیش‌رو باشد.
به نوشته این روزنامه، نتانیاهو انتظار داشت این سفر پس از «پیروزی کامل» بر جمهوری اسلامی، سقوط حکومت ایران و انتقال ذخایر اورانیوم غنی‌شده برگزار شود، اما اکنون نه‌تنها هیچ‌یک از این اهداف محقق نشده، بلکه ترامپ تقریباً هر روز با اظهاراتی تحقیرآمیز از نخست‌وزیر اسرائیل انتقاد می‌کند.
هاآرتص افزود توافق آمریکا و جمهوری اسلامی در اسرائیل به‌طور گسترده «فاجعه‌بار» تلقی می‌شود، زیرا ترامپ برخلاف وعده‌های اولیه خود، جنگ را بدون تحقق اهداف اعلام‌شده پایان داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/76513" target="_blank">📅 17:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76512">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_s8XnOdg2GANP8rIEcry3Ykf0vxW11tQ7NbIju_XBNRk4N12e-uw58YENz_rWiUgQ-qwd6t7ro6YAAkacUiNWiaybwrE9T0ZeYth-uX3BFnJXBCKLFJsR8BMrdRoVtJUrkkJsjLHVPSOwkcPDd8vZl4__CWysPWF9L0lA_1DuBwELN693KpZezsnzTkwt6x_Aerlj18OPlIuNmTiak9y4GtmwL_CS5VfHdD2pzKk28XsMofz9WHxtEkN76i_0W_8D95KyzuKfMOr7rX8SShfIG9r1FVqC3nS2j-PgRk6trDjQIxGh0tCt588HxKxEYcHsYr5NwDOehHkJpydfZzzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«معین بصیری» ۲۱ ساله، ساکن شهرک اندیشه تهران، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ هدف شلیک مستقیم قرار گرفت و جان خود را از دست داد.
به گفته منابع آگاه، گلوله از نقطه‌ای مرتفع و از روی پشت‌بام شلیک شده و به قلب معین اصابت کرده است.
او در پی این جراحت جان باخت و پیکرش پس از انتقال به کهریزک، به بهشت زهرا منتقل شد.
نزدیکانش می‌گویند پیکر معین بصیری را از بهشت زهرا تحویل گرفتند و مراسم خاکسپاری او روز ۲۱ دی‌ماه برگزار شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/76512" target="_blank">📅 17:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76511">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vjcnr-jwXh-ojmrccQvCROa-ik2guJFnz9OeG_Cx4bfJLT0ZKWXWWcTJm_Tut0qwlKgX1nRYnAMzS3H1NsRpOC_cUjNdex_cBMqgy-VACdh6cRHnJKWLyZuvg339pOEFUJcns2zD_wMK9g3uYK6y1Y5gE_1p-p9Xsl2Mn2tokqrjinauCB4jvEY_zu8tmOIhhCyH_sfcrYhnFUh01P861dBa1CyHVlfxrgVXR4WVk705P0ZFLLhQOmr71kd9El9xzFz1-PgN5uUjHnsPT6KXtiorBLpee7A0sz6rjChtNKUXrRNga9aByThXmn8u_Osx1MUTD_BrYrkK_Ajd4YzxwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های ترامپ، ترجمه ماشین:
«جنگ، ایران را تضعیف کرده است! ایران دیگر نه نیروی هوایی دارد، نه نیروی دریایی، نه تجهیزات ضدهوایی، نه رادار، و عملاً هیچ چیز دیگری هم ندارد؛ با این حال دموکرات‌های احمق می‌گویند ایران الان از چهار ماه پیش وضع بهتری دارد. اصلاً می‌توانید تصور کنید کسی با چنین حرفی قسر در برود؟ بعضی‌ها چقدر می‌توانند احمق باشند؟؟؟
رئیس‌جمهور، دی‌جی‌تی»
realDonaldTrump
«ما از سرِ درماندگی دیدار نکردیم؛ ایران بود که از سرِ درماندگی آمد. کارشان تمام است! این ۶۰ روز را هم طی می‌کنیم. هیچ پولی گیرشان نمی‌آید، حتی ده سنت!»
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/76511" target="_blank">📅 17:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76509">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g_qhMHYjZoWGPpP3F7md-Te0x_n-KorDa2W65zh4VM-dkV7wuR2UtmTyLFSxiTFiO6GYJcl28BBoaf6xzU_MDOVUhiubrOd27fHy94xIJavA-0iVCdWLVhmx1aAQzYmwL2KUTTqV1Wsg0o9E_ajvcNuc-q2QAxdUcdEeZXVCkXz6RBtsugTYfIfzWkcIPnZitNwEiDmjGPfIDvE04MB6wa1LWY1hIPWq9QaI54JLr5ytDvRKQy6LrH5Z9fDRk5Wm5DUNhMnZwrbmBe83rUT98Ses6MbVfcm69LH5w_TThrSDQqwgAwVcBSIIcQciH4ivLko_FGtjQsqd2oAWjHXSPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hGpN9X15MRK5yF4mT0p2X5CV4AEQLqpcJfQLn0fHm5cWGZ3AjZVc6IelBsj8igJ_kxiVdPGBAZ0zKG8q_GQ_8Ipwnhomsoph9hPXcvlliaXx9X_bWggMocSGJhV5aGj53yzhSXdzhOZQKKpOfHqErPZEXw97rUDYo0zY_1FuUds44sQx9LERKaj9On1wFPvH2-GeVO2RNTb5-zwqwe5WimncL8_zjAZF3JrIDkwZ8fp3U5ZlwsnbhbyAwz4iZyC-efY8ezzYHGhtevG7F_zjcsapmHzGgTtQlyEVP982-BvUThMZOhunKp2tM40xqUXC8gZG35Xk61O-Whj2qNhHUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزیر خارجه فرانسه می‌گوید پاریس تا زمانی که اطمینان حاصل نکند مذاکرات درباره برنامه هسته‌ای تهران انتظاراتش را برآورده می‌کند، با لغو تحریم‌های شورای امنیت سازمان ملل متحد علیه ایران موافقت نخواهد کرد.
ژان نوئل بارو روز جمعه ۲۹ خرداد این موضوع را اعلام کرد. فرانسه یکی از اعضای دارای حق وتوی شورای امنیت سازمان ملل است.
بارو گفت تا زمانی که مذاکرات آمریکا با ایران به ابهامات مربوط به برنامه موشک‌های بالستیک جمهوری اسلامی و حمایت تهران از نیروهای نیابتی پاسخ ندهد، ثباتی در منطقه برقرار نخواهد شد.
او افزود: «ما به یک تغییر اساسی در رویکرد ایران نیاز داریم.»
@
VahidHeadline
وزیر خارجه فرانسه: کشتار معترضان دی‌ماه را فراموش نکنیم، مردم ایران بزرگ‌ترین قربانیان جنگ بودند
بارو که با تلویزیون «فرانس انفو» مصاحبه می‌کرد در پاسخ به پرسشی درباره سیاست فرانسه پس از «امضای تفاهم‌نامه پایان جنگ» ایران و آمریکا در قبال تهران گفت: «مردم ایران، بزرگ‌ترین قربانیان این جنگ بودند. آن‌ها از یک سو گرفتار سرکوبند و از سوی دیگر به رویشان بمب ریخته می‌شود. ما کشتار ژانویه (دی‌ماه) را که در آن خشونت دولتی بدون تمایز، معترضان مسالمت‌آمیز را هدف قرار داد، فراموش نمی‌کنیم.»
فرانسه حملات نظامی آمریکا و اسرائیل به جمهوری اسلامی را «غیرقانونی» توصیف و بارها اعلام کرد که در این جنگ شرکت نمی‌کند.
دونالد ترامپ تفاهم‌نامه پایان جنگ با ایران را در کاخ ورسای و در حضور امانوئل مکرون امضا کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 198K · <a href="https://t.me/VahidOnline/76509" target="_blank">📅 17:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76508">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phdpdthokTZvf0F8ODDpfEH_5e6joEMxLIu5mqdUB9Bvm2to8BtRTGSJjFplyB0p_riNSk9VvAdtmQdBvnoS76kVXI1a0ypzHTaUe7zGMkm14WNH2JOjgsN_t58f0Lc2wODT_rSQG3r5F99lz3_LDo1pUbOvI83i70MHDIc3fae2DB69XuDcztQx6IE6tJGN-BUudLy7tNpwz-bMYG0pGrt3SA2MhM6ObG2BxtScpjZGTTSEJxVWIbQBS5PF91imoi-y3xG27oQPMEq9rE4bT395U1SoB30tEFgCytsSv80-btCZ4pZ9gIO7BdeLbrzU2jOCQO4nehpEdf1aLK-Xcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال از قول منابع آگاه گزارش داده که طبق توافق پایان جنگ، ایران حق دسترسی به شش میلیارد دلار منابع مسدود شده در قطر برای واردات اقلام انسان‌دوستانه و غیرتحریمی از خود آمریکا خواهد داشت.
به گفته یک دیپلمات آگاه از جزئیات توافق، این منابع مالی به‌صورت مرحله‌ای و در بازه زمانی آتش‌بس تمدیدشده ۶۰ روزه آزاد خواهد شد و تنها برای خرید کالاهای آمریکایی قابل استفاده خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 190K · <a href="https://t.me/VahidOnline/76508" target="_blank">📅 17:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76505">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ETqUKFq7txcuRjvR6NgqBN3WbqEg9cYkSvwSxtYXu-rxVhf9ainc0YOLbkYSUE2QwOaEQNE0QgyLHoSsEzi6crY9EFPQxatUnDsLHCvS9OkBb30hrktnT2AKQE70vPFUjzZfWSuHH2HOPJiwOeVS9wyGFz1uPR9ny7OLuSx3EqulOSFVlEy-bFiUHBebqwU4FZDHvKm9ETeOMAqoA-Wxm3-IWxgJEsxP2jkJxJdg_EQOk_3qcfSSt79qRoMVdXQV7An5mql6IIHOqsEwsALdU_K9jkITIql4GjBaqh0fDMcMzN2NQtnYWA-zgO0IpSXliFaoQHeaA0NDRZvwIlVn_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dRDlQqF8XfUK3vh1LGUmsZlgRys187qovgFFiAf7BucxrZiLjE37vDjhHHlL5d-P3u-2-6sH95S2xMqmhYsABVb5oofKRqUJauYuWjVHmZQTd4T7c1XyZkftKsb2rNii8-nSB976MQI3cWsDt4zbxdmaHT-JFOS1PgrAxwpa9nn7qwAFEM6On8dLL9GT5s2cvRrqlUbQ6I_uPseyb_m5hnSqsVQRI1J0UAq3_V0_FVJaXGsyNveSJFZOkbV3hl3bdJr6oCsRKLLA1_stRzsDwAghMKd_8n1ew3U1DFztOwanLdNBO_b8r2WACCgi2vLcEJl7TiaVTqaGvvV3gUCQBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Un6oyGBKGlb-pzzajAKoTjkPiW_5wBsvXkIS-NYe991wX9eS56Q4x6EvTabbHTz1TmcOMdkTX82vIJC5k1KQOBbF76udYZBJWJb_x2TUbJkKUCMqWPuC-6uzV4gWcaa4SjfLbshr-eRGeUMSS5PllAus3jolOOTP6mJeqwnHH9gXxykEJdOdouaOa0_WQYlpe9F3_kPwM__iFJnHE-Y3DEWBZaSAwm1C8yj0Ms45bpBDsX5US5guDl0-4UHxdi-RsHCyp5f6BWJ8YbAOHsuCigfnQ9Yrq1dUfbSPujTbWK7mY3T_ZVxWUQTTnRbjbnyI0EEpgylmrKC_BF4yWw90Hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
بيكر علی حسن‌پور را بعد از ۱۰۴ روز به خانواده
‏تحويل دادند
‏
🔸
⁧
#علی_حسن‌پور
⁩ در ۲۵ خرداد ۱۳۸۸ در خیابان آزادی تهران بر اثر اصابت گلوله به سر کشته شد. خانواده او پس از ۱۰۴ روز سرگردانی، سرانجام پیکر وی را میان اجساد مجهول‌الهویه پزشکی قانونی کهریزک شناسایی کردند.
🔸
اعتراضات خرداد ۱۳۸۸ که در اعتراض به نتایج انتخابات ریاست جمهوری سال ۱۳۸۸ شکل گرفت، جانباختگان زیادی برجای گذاشت، بنیاد برومند تا کنون ۱۳۸ نفر از این افراد را که مرتبط با این اعتراضات کشته، ناپدید یا اعدام شدند را در نقشه اعتراضات خود ثبت کرده است.
🔸
علی حسن پور یکی از این افراد است. سرگذشت کامل او را در یادبود امید بخوانید:
https://www.iranrights.org/fa/memorial/story/61687/ali-hassanpur
@IranRights</div>
<div class="tg-footer">👁️ 187K · <a href="https://t.me/VahidOnline/76505" target="_blank">📅 17:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76504">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lA3MzLzZfi7xHX1iXE6KlYqd0aW-Wd6PJnVxP0tLyVHfOGqjNqFG4X2xQBPhiW7DBhk5I8FyNxLGMbQrQ6n1Y66N7wYvjPy3HAf1x1GTXX7pKBfrqD2Q_TaqYujzRSuDcbn3y2_hDIhIy1U-D0MCG6xUGPQFlqUnwhWed5O_4wyK4jGCr0VN73DxIzI3YT1wcTdgvswkPfDRu9KSn5RNrTgsIBLmuEP0s9eIanz4pgG2qjoBqks78i5CeBxDmbkJNl4pBrgt7AUB7imtKEtR7guQOCImanvK_tzX23sulJtjESohbBwioMFVjAgc3V2ETpRA9_nDYB7EYkJwNue8Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ملی لبنان می‌گوید در حملات اسرائیل به شهرک‌های شرقیه، حاروف، کفررمان، کفرجوزو کفرصیر در جنوب این کشور دست‌کم ۱۶ نفر کشته شده‌اند.
به گزارش رسانه‌های محلی لبنان، از ساعات اولیه بامداد امروز، حملات توپخانه‌ای ارتش اسرائیل به شهر نبطیه و مناطق اطراف آن ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 203K · <a href="https://t.me/VahidOnline/76504" target="_blank">📅 17:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76503">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKuqnEUYmNLje3Pw_CcFT-U0-a7PuBNb_-a18SNvjGINedRSWPuSfZ-TYp5263WEeaLVFJZ6d43Vz6BNOdUXmVVIPc9tNUsoOAkA6_dPvFV1LRyIcZEBAbJw5pELZ-D4gTCHJLTw9cj9zjUn7zsChefk7ZduA5c9i10yCNXgL9H7RVi5RFIfYT4h2O6ac1fupTqChCJG62fPyl4Emmytn5u06NQ-wUkrEDGWMJfsj8r1i-xUummU-EQpZJ6ouc-oo77L0SWm31QWxmvTcr6A--sayBaQ-jGaixUQCVuv-FKCxMLwLGE2RIiTtcN90dYwQ1YbDI-5jkzQ22JumTFmBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی اعلام کاخ سفید مبنی بر لغو سفر معاون دونالد ترامپ به سوئیس، وزارت خارجه این کشور اروپایی رسما خبر لغو سفر هیئت آمریکایی و لغو مذاکرات تهران و واشینگتن در روز جمعه را تأیید کرد.
لغو آغاز فوری مذاکرات بین دو کشور متخاصم تنها یک روز پس از امضا و رسمی شدن تفاهم‌نامه‌ای رخ می‌دهد که یکی از مهم‌ترین بندهای آن ۶۰ روز فرصت برای مذاکره درباره فعالیت هسته‌ای ایران است. قرار بود این ۶۰ روز بلافاصله در روز جمعه آغاز شود.
اما خبرگزاری تسنیم، نزدیک به سپاه پاسداران، روز پنج‌شنبه خبر داد که مذاکره‌کنندگان ایرانی پیش از آغاز دور بعدی گفت‌وگوهای صلح نیاز دارند نشانه‌هایی از اجرای توافق موقت از سوی آمریکا مشاهده کنند و هنوز تأییدی درباره سفر هیئت ایرانی به ژنو وجود ندارد.
در پی این انتشار این خبر بود که سخنگوی کاخ سفید هم در بیانیه‌ای که پنج‌شنبه شب منتشر شد، اعلام کرد ونس و هیئت آمریکایی آماده بودند به محض نهایی شدن برنامه مذاکرات، عازم شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/76503" target="_blank">📅 17:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76502">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XdkxkvIwmbqrnZl9xJJsIf-W02rXMlGLGfeb82kBciYzPt5B8i7LFgp2XbjchfXzayDrsTwLqmSfOIXl0kU4Ti9GZE6WTd9dQ5lNlheW5f4lkX0_lb7i92KDIeLAc8qNFirKZm-G7WXu3YC6I4L7yglb43O8bfbt46eR3FHwYgaZRt8kudsbvKwJMiz0pzJau4wdg94rAm0TxPFsRXGfKAySRLpIsRq1MF8GeZ2x9qHBBi1nxX4_t4Kt2Cek-W_fwJvIMX38Xj8wrucnxEufzFc1Cgtz2BgvaRxjKOP8xSVd_sr_SJS6jxLfljQdpcU9RZhD3qdxUV-yINVvcem6Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود قنبری‌راد، متخصص امنیت شبکه و از کارکنان یکی از شرکت‌های تهران، با اتهاماتی از جمله «اجتماع و تبانی علیه امنیت ملی»، «جمع‌آوری اطلاعات طبقه‌بندی‌شده» و «ارائه اطلاعات به اسرائیل» روبه‌رو شده است.
بر اساس گزارش‌ها، محمود قنبری‌راد، شهروندی ۴۰ ساله و متأهل، اردیبهشت‌ماه سال جاری در منزل شخصی خود بازداشت شده است.
یک منبع مطلع به دویچه‌وله گفته بود که او هیچ سابقه فعالیت سیاسی یا مدنی نداشته و به‌عنوان متخصص امنیت شبکه مشغول به کار بوده است.
گزارش‌ها حاکی است که او در تماس تلفنی از زندان، پرونده خود را «ساختگی» توصیف کرده و گفته است که برای پذیرش اتهامات تحت فشار قرار دارد. همچنین اعلام شده که وی از زمان بازداشت تاکنون از دسترسی به وکیل محروم بوده است.
بر اساس اطلاعات منتشرشده، محمود قنبری‌راد ابتدا حدود یک ماه در زندان اوین نگهداری شده و سپس به زندان فشافویه منتقل شده است.
همچنین گفته شده که او از نوعی اختلال عصبی رنج می‌برد و خانواده‌اش نسبت به وضعیت جسمی و حقوقی او ابراز نگرانی کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76502" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76501">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qnXn72raxz7oAzYReXHmBVSpl43Tdr3SBPiytuddBuibxBz4bS8DfeUeoEAGBwSfwEyPjvqWft-fXvc2SB82Gg4VntHh3wxq4YJPtOVDmNk9bmD3bNcwm6uxNm8RuC4f8_QYKlmVQkpwVWZRwF0WQxNDuDOAIvhH-2IFxQSc_ABdZrNDWo39Lk26sA2_b5RL7yokR5EvfDw_jrnp_fNPjYZ9UtxZ5gG3QLzv4WfGS8j-6M599wxF6J_FwjjNQXPsEOd3v-n3hq1fFkCq8oNsQCTtyOfSv1MeN8mIT-pu64lwu3UqiQDwDfiMj2dQiHI5HrjUc3V2wFQYxHTXO003ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تصویری از امضای تفاهم‌نامه میان واشنگتن و تهران  را
منتشر
کرد.
این تصویر مربوط به مراسم امضای تفاهم‌نامه در کاخ ورسای فرانسه است؛ جایی که ترامپ در حاشیه سفر خود به فرانسه و پس از پایان نشست سران گروه ۷ (G7) حضور داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76501" target="_blank">📅 05:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76500">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d26gTlZJ9M1uIGHMAyAwaEA360XdssYlHO9JO5UJV_B08pPRaancBWBXr70GR16Q9wcCfXKFhB4UMeaU9zgve59Q9UJs4uY4ozB_nVDSFySjYzoT-vbpi63l8MA26APF0X7sFQW3jjgwzGB1o9H3ZVy77AxvgOGXwA7NbrEa9cgrsmE_WhshFvO4CnVu5ACutKgJdWz_Q0XNnSYUj0PWFl2tTU4thF6_s50tO2VCZenv8KDRJ1F3LwqsALCuC566qDFDv8NZnEOHKbFyaf4BgP7CoKJ37dHMJ6QWM9UGnjV37VmY282xlv9RcW4hBFixFYnh1jXAKFJkI_QPyCWI1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در«گفتگو ی تصویری با اکسیوس» گفت یادداشت تفاهم امضاشده با حکومت ایران را می‌توان «نوعی تسلیم کامل» از سوی تهران دانست.
او این اظهارات را در پاسخ به پرسشی درباره تفاوت میان خواسته پیشین خود برای «تسلیم بی‌قیدوشرط» و مفاد تفاهم‌نامه مطرح کرد.
مجری آکسیوس در این مصاحبه به ترامپ یادآوری کرد که در آغاز درگیری‌ها گفته بود تنها «تسلیم بی‌قیدوشرط» را از ایران خواهد پذیرفت، اما یادداشت تفاهم امضاشده چنین تصویری را نشان نمی‌دهد. ترامپ در پاسخ گفت: «خب، احتمالا در واقع تسلیم بی‌قیدوشرط است. فکر می‌کنم همین‌طور باشد.»
رئیس‌جمهوری آمریکا همچنین با اشاره به جنگ اخیر گفت ایالات متحده ایران را «کاملا از نظر نظامی شکست داده است». او با تمجید از توان نظامی آمریکا افزود واشینگتن توانست محاصره دریایی موثری علیه ایران اعمال کند و هیچ کشتی‌ای نتوانست از آن عبور کند.
ترامپ همچنین گفت پس از جنگ با ایران، محدودیتی برای قدرت خود نمی‌بیند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76500" target="_blank">📅 05:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76499">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BcVyHU0KZasf9F2AiRn4SP2ARvCRTq2J5b3x78dt6TVgDQuTOP4jcREsIkTE9Gn4IniPYwdF5ht5Nk2RNXkMmLkeKbTnouFqqCuKginjaV1Bh9VroDzb7FAEsd4KUILOR-6FaHak1Rh4PHI2ger4hzUb_0OJrBP3y4NpnxDGvoDtybdHnUZ9WED5S2qU0tKVA3vHpOg8yDZgVrld17hkPTrYuggsA23PMfU3_7ZXhhmWACSPxr-GUUClLDgQGcrwcj5wipxX2Unoozv59gWXrg-cr_E1jt4c6Fu_eoag06XLlzF5KWxoAydswzvPTqVb0ArxHYXzAbXcDQ5nl8zupw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر جی‌دی ونس، معاون ترامپ، در اطلاعیه‌ای اعلام کرد که او سفر خود به سوئیس برای شرکت در مذاکرات با جمهوری اسلامی را لغو کرد، زیرا برنامه‌های مربوط به گفت‌وگوهای فنی پیش رو هنوز نهایی نشده است و تدارکات و هماهنگی‌های این مذاکرات ساده یا قابل پیش‌بینی نیست.
در این اطلاعیه آمده است: «برنامه‌های مربوط به گفت‌وگوهای فنی پیش رو هنوز نهایی نشده است و هیات آمریکایی آماده بود در نخستین فرصت ممکن عازم شود، اما تدارکات و هماهنگی‌های این مذاکرات هرگز ساده یا قابل پیش‌بینی نبوده است. در حال حاضر، معاون رییس‌جمهوری امشب عازم سفر نخواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76499" target="_blank">📅 05:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76498">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BdQnDAaXcp0bqjmgmLjXLETgr1XGCq6r0s1facGHAwwIElWTmiqPaEY3a2lW1UBuKsp53ASOihNV0ZbJkDobYgAQEuxr7Z9DoiDGccJN-viQZructTCqy42km-upHUrzZafcZ940_gfYEUSxRbTQhlAfCAiByO0STL_-x4wBmQX8kq1vnD4L_G71P7sei5OpE9nzrsGvpFxn-b-V6VCuTxddDxiiPZtMvZitUyGXLGBezjAHUNTn13YsP6b0INYY72COprP2W_v-bYtERhhqJclifsDflnk6cDQtHoVtCpjOyW6MsxCpSpKsjmZ1aiJBWRpKGpCWz3NWusXq0iS7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری آسوشیتدپرس گزارش داد استیو ویتکاف، فرستاده دونالد ترامپ، پنجشنبه‌شب در نشستی غیرعلنی با قانون‌گذاران آمریکایی اعلام کرده است تهران از آژانس بین‌المللی انرژی اتمی برای بازرسی از تاسیسات هسته‌ای خود دعوت خواهد کرد و روند شناسایی محل نگهداری مواد غنی‌شده را آغاز می‌کند.
بر اساس این گزارش، ویتکاف به رهبران کنگره و اعضای کمیته‌های امنیت ملی گفته است تفاهم‌نامه میان آمریکا و ایران هیچ توافق جانبی نداشته است. با این حال، تهران و آژانس بین‌المللی انرژی اتمی نامه‌ای جداگانه تنظیم کرده‌اند که در آن دعوت از بازرسان آژانس و ادامه همکاری‌های نظارتی مطرح شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76498" target="_blank">📅 00:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76497">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GA2KwJpdBNsvwj0oQTF6cJBEyijcF92Fs-Op_-CAJJngcSqtIxhqiqnmcaNdZvv84jd799OAuOfF2HbRFk8xyEand4f5ESqt0xFOd3MAhHcDpg94vMarW71GpaMpWb5u8kS5UMv7-JpMTjdfpnDPDjt2upWjoGG8Qztd4o6nHIgwweVzWH5bXnz2QfZDeDXvHBjFqU2l2uVQHObDZfIQnzhNcWVcPnc1fG3pcaiKHynISWFxxVvSDMWMHgBw_a-ylAObRM3KCc7zqVtREkqkL9WiUN5f5vSXMmCeRQl9KiVG2zq7aPlIARkIiVCZWovAQKwR5bhrowWv-bvIao0oCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کایا کالاس، مسئول سیاست خارجه اتحادیه اروپا، گفت هنوز برای بحث درباره لغو تحریم‌های اتحادیه اروپا علیه ایران زود است و این موضوع پس از دستیابی به یک توافق هسته‌ای با ایران بررسی خواهد شد.
او پیش از نشست رهبران کشورهای عضو اتحادیه اروپا به خبرنگاران گفت: «زمانی که شرایط فراهم شود، کشورهای عضو درباره مناسب بودن لغو تحریم‌ها گفت‌وگو خواهند کرد، اما هنوز به آن مرحله نرسیده‌ایم.»
اتحادیه اروپا در حال حاضر مجموعه‌ای از تحریم‌های چندجانبه علیه بیش از ۷۰۰ فرد و نهاد در ایران اعمال کرده است که شامل ممنوعیت سفر و مسدود شدن دارایی‌ها می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76497" target="_blank">📅 00:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76496">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7PS6qUeTDGfjKMQrJwR8b6GIM-bvXOtVXuyD0Knkbe4ptFXO1pIEdxbQimChQBBPH5h1rTmHK9vRYlPx67VrUbXH6K2IAzOSefz5ji8f1CsLPcMZICP2aU1ZOunFFIZ8iRrMFZRfbbzWGCW1v_UTKg1Dysxhnhfu1eRK9zPb15NftOBsBvkHkILM0LdhRis9IBrIblUTIdVN8NIOdz4P9WtwEMUc1Y8QOPf5JCF2tsBx0KM-ehHL2YboWplOzCXRKNqFhwWt2fEs0D0m2jyf3FvPMJgBA75CoCmys3JfhkrsP5fSbGBJ03Q3cKawpcdTYkDWXoPpoONTpK_aU4R5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المیادین به نقل از یک منبع آگاه گزارش داد هیات مذاکره‌کننده جمهوری اسلامی به دلیل ادامه حملات اسرائیل به جنوب لبنان، سفر خود به سوئیس برای آغاز نخستین دور مذاکرات ۶۰ روزه را به حالت تعلیق درآورده است.
المیادین افزود: تهران پیش‌تر به آمریکا و میانجی‌ها اطلاع داده بود که پرونده لبنان در ادامه یا توقف مذاکرات نقشی محوری دارد و هشدار داده است حملات اسرائیل تا عمق ۱۰ کیلومتری خاک لبنان نقض یادداشت تفاهم و توافق چارچوب است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76496" target="_blank">📅 23:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76495">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b4ezogS2spVJzU_qb7ENqgk8MY82jZzjdMK8PMI5vCMds6iUbh4Lk0IFNNgx0VdVh-I-oZ4iNI9SPMNxHgzcwjaMOmjMlNAHHKPMcQyFsdgXZLKoGJmoT4ZNhKs1B3thsSCZQKtWFscGolb9JIMWNJeEJe_O7PCQjlsEyuLs7v_NKYGf9gV1yB4Scg6ZfyGJvHYodD88Y2LymKrMc4tWWOUI6lv4e9KOZnj2n3SlkdvTDaSjOza7JIjiZ7vYIdKfqgGb1CdWQqrtA_poYExPfMr1Z3a6VsvGptuxJmIm4zPJSnJvitmOeYk-QkxYKOq4zeBV_ub92ZJlZtzY-0w_IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت کاخ سفید:
رئیس‌جمهور دونالد ج. ترامپ تهدیدی را حل کرد که واشنگتن چهل سال صرف مدیریت آن کرده بود: ایران هرگز سلاح هسته‌ای نخواهد داشت.
یک پیروزی برای آمریکا.
🇺🇸
WhiteHouse
ترجمه با هوش مصنوعی به تصویر اضافه شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/76495" target="_blank">📅 22:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76494">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U-UEhgJPzjW3NKsM-IdDEsryKNIRtYWUr_99DyseQTE0u6FqDojEDMbtmhz4gE9R2nZzpfVZ4fD-35rZ4-Ea7g99DDgriOgeeBYe1IEqq31h-gETy8YS7v0knmLqaHI8zJu4t8JQ5_hwx9emSaYyUHwYTp0IjjuBjZUSrzu34oB6rR5DnFLx_I-dVsUwXLu1kh2JbCDq9JkRVeGNEH6YVnX33D7On1X7VQr7jo9zObEDiPO1pyGeGVRkP9PXEgnvp4FHc7AuCPJ1DD_RVTO2HWT5w5wxZ8KTCB5VTt0g-paQqV4_VfzBwI6pB-WtsqNaYX4L-rMHtREycdOQMPDJKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">'
بیانیه شورای عالی امنیت ملی
'
منابع حکومتی:
🔹
در اجرای بند ۵ یادداشت تفاهم اسلام‌آباد، کشتی‌های تجاری متقاضی عبور از تنگه هرمز باید درخواست خود را به مدیریت آبراه خلیج فارس (PGSA .ir) ارسال نمایند.
🔹
به موجب یادداشت تفاهم اسلام‌آباد، به مدت شصت روز، هیچ‌گونه هزینه‌ای از متقاضیان اخذ نخواهد شد و این هزینه‌ها توسط دولت جمهوری اسلامی ایران تأمین می‌گردد.
🔹
بر این اساس به مدیریت آبراه خلیج فارس دستور داده شده است، در جهت تحقق اهداف تفاهم‌نامه درخواست‌ها را با سرعت و اولویت رسیدگی و پاسخ دهد.
🔹
با توجه به شرایط خاص و وجود برخی مخاطرات ایمنی در مسیر عبور و به دلیل لزوم حصول اطمینان از تردد ایمن و جلوگیری از حوادث دریایی، لازم است کشتی‌ها در مسیر و زمان اعلامی به آنها عبور نمایند تا به تدریج، امکان تردد افزایش یابد.
🔹
ترتیبات اجرایی و جزییات فنی عبور از تنگه هرمز از طریق مدیریت آبراه خلیج فارس اعلام می‌گردد.
🔹
در خصوص سایر موضوعات، از جمله مین‌زدایی، اقدامات لازم مطابق بند ۵ یادداشت تفاهم اسلام‌آباد انجام خواهد شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/76494" target="_blank">📅 22:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76493">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OUJSScKEae7FHQSuWNJJChae9x6yiAtKcXy3_6US9Na8TzJJjERaIJo7V5iYCjVrA3MccH58I2PrXAzLqaxhCQzC7Nv9kjUtpEAflprSb79r7Ck4huCg6JEMgIhOLSQP5wvhKRovmvFHaY9FuHMrC3KYCB9o5bv5rZp7UfKpauJeX9c4EaTofQ6L2KVaqkGaZy2Q8fjrvh0nuGqCIoUgyqVyhn4IERQXVC3CWuNlMw1r3u8QaLZixselEoZWF6rkgvgZXkbcPY8aEYSzPDesRk-wmHmAavKnECQzU2-V2ypIFUMWBw-EQoLL4YSCLzklvi1uvMRAVNH_R9sdw1bGBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: انتظار آتش‌بس کامل در همه جبهه‌ها از جمله لبنان را دارم
ترجمه ماشین:
ایالات متحده به صلح متعهد است و ما همه در منطقه خاورمیانه را تشویق می‌کنیم که به تعهد خود برای فراهم کردن امکان پیشرفت زیبای مذاکرات ما پایبند بمانند.
بازارها از آنچه در حال رخ دادن است استقبال می‌کنند: قیمت نفت به‌شدت پایین آمده و سهام به‌شدت بالا رفته است.
ما انتظار آتش‌بس کامل در همه جبهه‌ها، از جمله لبنان، حزب‌الله و اسرائیل را داریم.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76493" target="_blank">📅 22:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76492">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPourostad وحید پوراستاد🔷(Vahid Pourostad)</strong></div>
<div class="tg-text">« پیام منتسب به مجتبی خامنه‌ای در واقع نوعی فاصله‌گذاری حساب‌شده با تفاهم ایران و آمریکا است. مجتبی خامنه‌ای رهبر جمهوری اسلامی اجازه امضا را داده، اما مسئولیت سیاسی و اجرایی آن را بر دوش پزشکیان و شورای عالی امنیت ملی گذاشته است.
پیام همزمان رو به داخل و بیرون نوشته شده است. در داخل می‌گوید رهبر با رضایت کامل وارد این مسیر نشده و دولت باید پاسخگوی نتیجه باشد. در برابر آمریکا هم این سیگنال را می‌فرستد که تفاهم، زیر فشار ترامپ و دولت او به‌معنای عقب‌نشینی قطعی نیست؛ بلکه مشروط است و اگر شروط ایران محقق نشود، موافقت نهایی رهبر با توافق نهایی هم تضمین‌شده نخواهد بود.
در واقع متن، بیش از آن‌که اعلام رضایت از توافق باشد، تلاشی برای حفظ دست بالا در مرحله بعدی است: هم مسیر مذاکره باز می‌گذارد، هم امکان عقب‌نشینی تبلیغاتی حفظ می‌شود, هم به واشینگتن گفته می‌شود که فشار بیشتر ضرورتا به انعطاف بیشتر ایران منجر نخواهد شد»
@pourostadv</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/76492" target="_blank">📅 22:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76491">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FFClguOLbRTsIo8CrhSfoDVE8hbUeQH9jk2hCBYTkCy_Qj4WKHTHjwr_FY7o7Lq6phhEPoB40oNZoY6bzk25VIBByRJXnuko-QTZ9fc-D-DIyv_VxdPEA_9uSSWDWfDPFuGQ6qzX9HdXrReRZugRgKSomrlo5aIEkNpPDanwhyIIP10cS5HEQ8JMuWyc9VsyhN35JOqh6BtCEsoQmzRSSSg7nMyge9fgUAzRJor7KtO7ulRwI2U6o9CAejqZyST3PriV4RWI2tIP1iO5Tx948y1AvAuljRqFbxUosIyScPpKMrABDKCf6Z1LoAmrlIqMonC5ozjnvT-bmJWHm_c8og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسئول
گردن‌نگیر
جوان شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76491" target="_blank">📅 21:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76490">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kf-y2MeSSu-wNRGqsYsmX4pOWx1ssfvUd4MzHAcJMQBNaw4eZuebDpJ5OspulrV668Ih5-ia6Cskglx11ysQzu-bn2ahixS3RPWjWhqM0z6X6ZyMggPLkNabLV0B53XPqxXFopNzP3lwTLIK-JqTIw9RA0Sgzcsy3G6-xaNDQQ7q2ZxcZz5oe1X29nXYojj3F-1kuDAohRWwuZ031bqFyd1saXTfxYXJ-dn37V-kIttZud1N_ePvsN8xqn92onNfR9L85nFgG3B11MGlBMUfVV9_zDWwYbl0jgsyrwHruGx7s3UvHa1JHQkl8tqNAC_9hJJBGI5f14ZPVMto4DNgew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران پنج‌شنبه شب متن پیام مکتوبی منسوب به مجتبی خامنه‌ای را منتشر کردند که در آن رهبر جمهوری اسلامی درباره امضای تفاهم‌نامه میان ایران و آمریکا گفته است که «نظر دیگری» داشته و مسئولیت آن را بر عهده مسعود پزشکیان، رئیس شورای عالی امنیت ملی، و دیگر اعضای این شورا دانسته است.
در این پیام درباره توافق با ایالات متحده آمده است:
«بنده علی‌الاصول، نظر دیگری داشتم ولی از باب تعهدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیت ملی از طرف خود و سایر اعضا در پاسداشت حقوق ملت ایران و جبهه مقاومت به بنده دادند و تصریح به قبول مسئولیت آن نمودند، اجازه آن را صادر نمودم‌.»
در این پیام به تفاهمنامه اخیر به عنوان «تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و آمریکا» اشاره و گفته شده است که رهبر جمهوری اسلامی و مردم از این لحظه «منتظر تحقق شروط گفته ‌شده» خواهند بود.
در این پیام آمده که مذاکرات حضوری آینده «به معنی پذیرش نظر دشمن نخواهد بود.»
VahidOOnLine
در تیتر و متن نامه و خبرهایی که درباره‌اش تولید میشه بسیار تاکید دارند که این تفاهم‌نامه‌ای بین پزشکیان و ترامپه و نمی‌گن بین ایران و آمریکا
در واکنش‌ها از کوچک‌نمایی نقش
قالیباف
یا محافظت ازش با سپر کردن پزشکیان هم میگن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/76490" target="_blank">📅 21:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76489">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/liPntDEjao60TPf5UL4_cRukW0HrvsHF08PXvZE8NRY4FUxQq91rfU_r8zlNgDRFGolFpMHfIveluDz4bf7X98WIVnOPDqr2DMv_Ep5lliYPBUW7J9gwcw79zwH2b0HwWJM06yWWQ7021zSTwGLe48nzKVsNAdKvlJIYQBOWmvw5b1-9Jm07zE4zlzb3VUvsdjEM6VdhgOB_2DH3203pkXyMfdQDbrsF0opmB5X1UQYQrDDepfCjkWinZRXqsmxC_BcHLdCkTS4eHk-mI_eUmfYpuLOxlhqV2t4SIkqm0ZTKoHZC0jy9lnJ3YyuxqwJnxbOTZIbAhaxevbFULJKvPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
هیچ پرداخت ۳۰۰ میلیارد دلاری از سوی آمریکا به ایران در کار نیست.
این خبر جعلی است!
تنها چیزی که نصیب آمریکا شده، موفقیت، کاهش قیمت نفت و پیروزی است.
بازار سهام را ببینید.
تبلیغات «دُمکرات‌ها» در جریان است!!!
رئیس‌جمهور دی‌جی‌تی
(توضیح: Dumocrat بازی زبانی تحقیرآمیز با Democrat است؛ از ترکیب ضمنیِ dumb به معنی «احمق» و Democrat. در ترجمه می‌شود چیزی مثل «دُمکرات‌ها» یا «دموکرات‌های احمق» آورد، بسته به لحن مورد نظر.)
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76489" target="_blank">📅 20:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76488">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sfyctYjtJN637deeuoiEnoi_74peY1b8N3YZ4e6vKjEQzph0riLdK7KCBWxb5zzeyYM2r-t8DjY_or9u7GudDX37__-L9oZy6g7A23rCxdjrD6ogabAdL3GJ4pchSTsNm6XwQbslRk82PH1_gUnoQRfbQktmscnjX4VglAbRj7o3CClUisam0ONt4FnkCcoNjGSoXyZwcTzzxffqd94_r2DNbfnrgkoGl_clzaa5-pxbN1klG5t1z7anUtfh4BdpnVzrmLqdDYx5X81kCGMIklMFZDra9s853SqB4dKedYLGqb3t4-3UhaCXQH_QTKI_SmrtngSBw4s5dlP002GSvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام پایان محاصره دریایی
پست سنتکام، فرماندهی مرکزی ایالات متحده، ترجمه ماشین:
امروز، نیروهای آمریکا مطابق دستور رئیس‌جمهور، محاصره‌ی همه‌ی رفت‌وآمدهای دریایی به مقصد بنادر و مناطق ساحلی ایران و از مبدأ آن‌ها را رفع کردند.
نیروهای آمریکایی مانع عبور کشتی‌ها به سوی بنادر ایران در خلیج فارس و خلیج عمان، یا خروج از آن‌ها، نمی‌شوند.
همه‌ی تلاش‌های نظامی آمریکا برای اجرای محاصره متوقف شده است.
کشتی‌های بزرگ نیروی دریایی ما در منطقه‌ی کلی باقی خواهند ماند تا اطمینان حاصل شود که همه‌ی جنبه‌های توافق رعایت، اجرا و به‌طور کامل لازم‌الاجرا و مؤثر باقی می‌ماند.
CENTCOM
البته سنتکام ننوشته خلیج «فارس»
🔄
آپدیت:
توییت رو ویرایش کردند و در نسخه جدید اون جمله مربوط به خلیج فارس رو کلا حذف کردند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76488" target="_blank">📅 20:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76487">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pOV714BjXRXqXlzTVvv3ARiXkUjJE8VAN_5ba27rumIJcsJlN0F3B-1S8yTkYtYVb1idVFT-gL_0SEsaroVd3ciEGdNxm4xyAD9kc5L9dJiKtkp-da-f0LP1Nq8Sd8r0lH_41AsAhbrbxH7t5-ESW6OoWFWbPDZK3Y7UdHTlrTDxa-qFA6O7SwFI_YXUMBqQTauM-TckVEsXaWa5Bq5R9z5BbOJ-jHa30mUAKCHUPYyBdZzMUer5MfLDhxJmcLLnt8MPZjDc5m4jr6ui_G1vehYr65-ftQEndhGCFSquXxCJCQ4VU-qqdNyK7SKW2viXJZ2HylBQ-Xak9A5b15sE8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این توییت ۹ سال پیش ترامپ داره توجه می‌گیره: ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار. realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76487" target="_blank">📅 20:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76485">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90d4e8375c.mp4?token=CoiGXWtMC7airHX3QuAOZwrZG3u-u-bUhjd58ngq7XHYQLT3nGNHNB39exi5epmLHwtlGoaTBtOnlIvtm51W5NoV2l4E17smKAg0nMlrenxiMU9X2oK9_zOlEf78A4LpM3GDWlNaqJyqnEmgR7bbLdU7K7i9Ml_Zmd-2a-EPj1br1emVzV-Px4q8jT4NMbXfXvzhodSd9TlTv5juoVkW3dnqUzxngJcmZwyTZ5H91GTvOh_N31Bex_7keqOIYvaK_iNb7fFZ2zMd4l0C4EQgRTIyox99_J_qe_BLjIZdp2B-Afl36YoL9-fmIOGV4vLzbShB8wkoFhsY6EtEBLx_BA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90d4e8375c.mp4?token=CoiGXWtMC7airHX3QuAOZwrZG3u-u-bUhjd58ngq7XHYQLT3nGNHNB39exi5epmLHwtlGoaTBtOnlIvtm51W5NoV2l4E17smKAg0nMlrenxiMU9X2oK9_zOlEf78A4LpM3GDWlNaqJyqnEmgR7bbLdU7K7i9Ml_Zmd-2a-EPj1br1emVzV-Px4q8jT4NMbXfXvzhodSd9TlTv5juoVkW3dnqUzxngJcmZwyTZ5H91GTvOh_N31Bex_7keqOIYvaK_iNb7fFZ2zMd4l0C4EQgRTIyox99_J_qe_BLjIZdp2B-Afl36YoL9-fmIOGV4vLzbShB8wkoFhsY6EtEBLx_BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی در ایران که ریاست هیئت مذاکره‌کننده ایرانی با نمایندگان آمریکا را برعهده داشت، عصر چهارشنبه در مصاحبه‌ای مفصل با تلویزیون حکومتی در ایران به نهایی شدن تفاهمنامه میان تهران و واشنگتن واکنش نشان داد و آن را موفقیتی بسیار بزرگتر از مقابله نظامی با ایالات متحده دانست.
او در مورد دستاوردهای ایران گفت: «هر آنچه را که با اقدام نظامی می‌خواستیم به دست بیاوریم، چندین برابر آن را از طریق مذاکره گرفتیم؛ اصلا قابل قیاس نبود. هر جنگی ممکن است پیروزی‌هایی داشته باشد، اما اگر این پیروزی‌ها در نهایت به یک سند حقوقی و سیاسی منجر و ثبت نشود، هیچ منفعتی نخواهد داشت.»
او در بخشی از صحبت‌های خود درباره انتقام کشته شدن علی خامنه‌ای گفت: «همان‌طور که خونخواهی امام حسین، ظهور امام زمان است، خونخواهی رهبر شهید هم آزادی قدس است... صد نتانیاهو بند کفش امام شهید ما هم نمی‌شود.»
قالیباف در مورد وضعیت تنگه هرمز هم گفت: «تنگه هرمز هرگز به شرایط قبل بازنخواهد گشت. البته این به آن معنا نیست که ما در تنگه هرمز بخواهیم برخلاف قوانین بین‌المللی و مقررات دریانوردی عمل کنیم.»
@
VahidHeadline
قالیباف در مصاحبه‌ای که همزمان با انتشار مفاد تفاهم‌نامه تهران و واشنگتن از صداوسیما پخش شد، گفت برای حضور در مذاکرات با دولت دونالد ترامپ تمایلی نداشت و به دلیل نقش ترامپ در کشتن قاسم سلیمانی، «کراهت شدید» برای ورود به این روند احساس می‌کرد. او افزود که با وجود این مخالفت شخصی، به درخواست مقام‌های جمهوری اسلامی مسئولیت مذاکرات را پذیرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/76485" target="_blank">📅 20:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76484">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPkKQ2QfGzVhRea8idR7p8-WHgoebYg5TiM8Tdiv4HivM5xW06lRWUhy0nOwZw7U1DE8m08gvJijJUQoUVuFIRyL0t-QOIkvir08KH843PS887pJcOCnBbTuJEmWCN8xcCbyWschDCgr0w_JhYs-6oPeFeAPbllvc5JRmRRRYTTeDKT53TFeFmWSR-nqKrvJHUpffbbVqaACCjC0bopn_UM8GYfSUrsmbweJ7JdVTGKlw4qkzhzGVbZKFEtEB4ESsuC2iVtHwd7uCBR5vCzTsuOvit173eD52GRDzWpwAtL1rH0XWRdyHOzRW4on7Cn3TYfmIUDFSUv-Z6CYomE8Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، یک روز بعد از امضای تفاهم‌نامه ایران و آمریکا در نخستین موضع‌گیری خود اعلام کرد که نیروهای اسرائیلی از جنوب لبنان عقب‌نشینی نخواهند کرد و تا هر زمان که لازم باشد منطقه حائل امنیتی خود را در آنجا حفظ خواهند کرد.
این اظهارات پس از آن مطرح شد که دونالد ترامپ، رئیس‌جمهور آمریکا، طی روزهای اخیر از عملیات اسرائیل علیه حزب‌الله لبنان انتقاد کرد و آن را بیش از حد «تهاجمی» دانست.
نتانیاهو در یک مراسم رسمی گفت: «ما امنیت و رونق را به شهرهای شمالی بازخواهیم گرداند.»
او افزود: «این امر مستلزم حفظ منطقه امنیتی در جنوب لبنان است؛ مستلزم آن است که آنجا را ترک نکنیم، تا زمانی که نیازهای امنیتی اسرائیل چنین ایجاب کند.»
رسانه‌های رسمی لبنان پیش‌تر گفتند که در حملات صبح پنجشنبه ارتش اسرائیل به جنوب لبنان، ساعاتی بعد از امضای تفاهم ایران و آمریکا، سه نفر کشته شدند.
از سوی دیگر، یک مقام ارشد اسرائیلی پنجشنبه به خبرگزاری رویترز گفت که اسرائیل «در حال انجام مذاکراتی سرسختانه» با ایالات متحده دربارهٔ موضوع ادامه استقرار نیروهای اسرائیلی در جنوب لبنان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/76484" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76483">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شروع سخنرانی جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
🔸
دیشب، ۱۲.۵ میلیون بشکه نفت از تنگه هرمز عبور کرد.
این بالاترین میزان از آغاز درگیری است.
🔸
ایرانی‌ها برای دومین شب متوالی به هیچ کشتی‌ای در تنگه هرمز شلیک نکردند. تا این لحظه، آنها به تعهد خود پایبند بوده‌اند.
سنتکام اجازه داده است که دوازده کشتی از محاصره دریایی ما عبور کنند، بنابراین ما نیز به تعهد خود عمل می‌کنیم.
🔸
شما چیزهایی درباره ۳۰۰ میلیارد دلار یا ۲۴ میلیارد دلار، یا این یا آن عدد یا مقدار پول خواهید شنید، و واقعیت ساده این است که تنها راهی که ایرانی‌ها به هیچ یک از این منابع دست پیدا کنند — حتی یک سنت، به هر حال، از ایالات متحده آمریکا تحت هیچ شرایطی — اما
تنها راهی که آن‌ها می‌توانند از این معامله بهره‌مند شوند این است که کاملاً مطیع باشند و رفتار خود را تغییر دهند.
اگر ایرانی‌ها رفتار خود را تغییر ندهند، برنامه نظامی و هسته‌ای آن‌ها همچنان نابود خواهد شد؛ اگر رفتار خود را تغییر دهند، آنگاه رابطه‌ای تحول‌آفرین با خاورمیانه خواهند داشت.
این یک برد-برد برای ماست.
🔸
در ایران تقسیمات واقعی وجود دارد.
آنچه دیده‌ایم این است که عمل‌گرایان در حال پیروزی در بحث هستند.
🔸
من کسانی را دیده‌ام که به این توافق شک دارند — افرادی می‌گویند ایرانی‌ها هرگز رفتار خود را تغییر نخواهند داد.
خب، شاید این درست باشد، و اگر چنین باشد، آن‌ها هیچ‌کدام از مزایای این معامله را به دست نمی‌آورند. اما آیا ارزش امتحان کردن ندارد؟
🔸
می‌گویم دوره ۶۰ روزه رسماً امروز شروع شده است.
پس بله، توافق دیروز شروع شد — ما امروز ساعت ۶۰ روزه را شروع خواهیم کرد.
🔸
تمام چیزی که رئیس‌جمهور دیروز گفت این است که، البته، کشورها حق دفاع از خود را کنار نمی‌گذارند.
اسرائیل حق دفاع از خود را کنار نمی‌گذارد اگر حزب‌الله به اسرائیل راکت یا پهپاد شلیک کند.
ایرانی‌ها حق دفاع از خود در کشورشان را کنار نمی‌گذارند، اما
ما انتظار داریم که به عنوان بخشی از توافق نهایی، آن‌ها نتوانند موشک‌هایی بسازند که بتواند به طور گسترده کل جهان را تهدید کند،
و این همان چیزی است که رئیس‌جمهور ایالات متحده دیروز گفت. و ببینید، خیلی ساده است: نمی‌توانید به کشوری — چه اسرائیل، چه ایران — بگویید که حق دفاع از خود را نداشته باشد.
🔸
خبرنگار: رئیس‌جمهور ترامپ دیروز گفت که اگر مذاکرات این دور به مشکل بخورد، شما را مقصر خواهد دانست. آیا نگرانید که او شما را به عنوان مقصر معرفی کند؟
جی‌دی ونس: نه، اصلاً. فکر می‌کنم رئیس‌جمهور شوخی می‌کرد، همان‌طور که اغلب این کار را می‌کند.
🔸
جی‌دی ونس درباره تنگه هرمز:
ما هرگز نمی‌خواهیم این اتفاق دوباره بیفتد، درست است؟ این موضوع مربوط به عوارض نیست.
این درباره اطمینان از این است که تنگه‌ها هرگز به عنوان نقطه گلوگاهی برای اقتصاد جهانی استفاده نشوند.
صادقانه بگویم، این چیزی نیست که ایرانی‌ها بخواهند.
🔸
جی‌دی ونس درباره برداشتن تحریم‌ها:
صادقانه بگویم، ما این را به عنوان امتیاز بزرگی به ایرانی‌ها نمی‌دیدیم — ایران... این را به عنوان امتیاز به آن‌ها نمی‌دید، چون چیزی که مانع فروش نفت آن‌ها می‌شد تحریم‌ها نبود.
آن‌ها بدون هیچ تخفیفی مقدار زیادی نفت می‌فروختند، چون تحریم‌ها اساساً بی‌اثر بودند.
در آن زمان، کاری که تحریم‌ها انجام دادند این بود که سیستم مالی ایران را به نوعی به سیستم بانکداری سایه‌ای منتقل کردند.
با برداشتن تحریم‌ها، ما در واقع قادر خواهیم بود کمی ببینیم که سیستم مالی آن‌ها پول را کجا می‌فرستد و از کجا دریافت می‌کند. این یک مزیت واقعی است.
🔸
آنچه به برخی از منتقدان توافق که شنیده‌ام می‌گویم، کسانی که می‌گویند «خب، ایران تمام این مزایا را به دست خواهد آورد».
تکرار می‌کنم آنچه را که گفته‌ام و احتمالاً باید چندین بار تکرار کنم: مزیتی که ایرانی‌ها به دست می‌آورند و قبلاً نداشتند چیست؟ و پاسخ هیچ است.
آنها هیچ چیزی به دست نمی‌آورند مگر اینکه رفتار خود را تغییر دهند. اگر رفتارشان را تغییر دهند، این چیزی است که باید جشن گرفت.
🔸
هیچ‌کس نمی‌تواند حق دفاع از خود یک کشور دیگر را نادیده بگیرد — اسرائیل حق دارد از خود دفاع کند.
اما اساساً، اسرائیلی‌ها، درست مانند همه‌ی مردم دیگر، باید به این روند صلح که اساساً برای آن‌ها و کل منطقه مفید است، احترام بگذارند.
🔸
در انتقاد از اسرائیل: به نظر می‌رسد که ما درست در آستانه یک پیشرفت بزرگ در توافق هستیم، و ناگهان یک انفجار بزرگ در یک مرکز جمعیتی غیرنظامی در بیروت رخ می‌دهد و بسیاری از افرادی که هیچ ارتباطی با حزب‌الله ندارند جان خود را از دست می‌دهند. این قابل قبول نیست.
🔸
توافق هسته‌ای اوباما اجازه غنی‌سازی داد — توافق ما این اجازه را نمی‌دهد.
توافق اوباما اجازه انباشت مواد با درجه تسلیحاتی را داد؛ توافق ما در واقع به نابودی آن انبار مواد غنی‌شده منجر می‌شود.
توافق اوباما بیش از یک میلیارد دلار پول آمریکایی به آنها داد؛ این توافق هیچ دلار پول آمریکایی به آنها نمی‌دهد.
🔸
آنها تعهدات هسته‌ای بسیار مشخصی داده‌اند.
آنها متعهد به نابودی ذخیره بسیار غنی‌شده‌ای شده‌اند که در اختیار دارند.
اما نکته دوم، تنها کاری که ما انجام داده‌ایم برداشتن محاصره در تنگه است — که اساساً آن را به وضعیتی که قبل از درگیری بود بازمی‌گرداند.
🔸
خانم‌ها و آقایان، کلمات مهم نیستند، ما درباره تأیید صحت صحبت می‌کنیم.
🔸
فرض کنیم — دو سال بعد، آن‌ها آنچه را که ما باید در برنامه هسته‌ای ببینیم انجام داده‌اند و تحریم‌ها را طبق توافق آزاد می‌کنیم.
سپس تصمیم می‌گیرند که برنامه هسته‌ای را دوباره بسازند.
البته در این صورت، آن تحریم‌ها دوباره باز خواهند گشت.
و به همین دلیل است که این موضوع واقعاً شبیه یک دکمه تنظیم است: هرچه رفتار خوبشان را افزایش دهند، ما می‌توانیم تسهیلات اقتصادی را افزایش دهیم؛ اگر رفتار خوبشان را کاهش دهند، می‌توانیم آن را قطع کنیم.
🔸
آنچه واقعاً اتفاق افتاد این است که ما یکشنبه یادداشت تفاهم را امضا کردیم. این موضوع شرایط توافق را تثبیت کرد.
ایرانی‌ها به ما آمدند و گفتند: «ما دوست داریم متن را تا جمعه منتشر نکنیم.» من واقعاً این را درک نمی‌کردم—می‌خواستم متن را فوراً منتشر کنم. اما برای اینکه با آنها کنار بیاییم، گفتیم: «باشه، ما تا جمعه صبر می‌کنیم.»
و سپس در طول دوشنبه و سه‌شنبه، در حالی که رئیس‌جمهور در نشست جی۷ بود، شاید رهبران خارجی با ایرانی‌ها صحبت می‌کردند و آنها را تشویق می‌کردند که این کار را انجام دهند.
ما قطعاً به آنها می‌گفتیم:
«ما تمایل شما برای عدم انتشار متن تا جمعه را درک می‌کنیم، اما می‌دانید که ما در یک نظام دموکراتیک زندگی می‌کنیم. مردم آمریکا می‌خواهند متن این توافق را ببینند. ما قطعاً دوست داریم هر چه زودتر آن را منتشر کنیم.»
و بنابراین آنها تصمیم گرفتند که رئیس‌جمهورشان آن را امضا کند، رئیس‌جمهور ما آن را امضا کند، و سپس متن را به عنوان یک سند امضا شده فوراً منتشر کنند.
🔸
اینکه فکر کنیم فروش چند میلیون دلار نفت قرار است اقتصاد ایران را به طور بنیادین تغییر دهد، درست نیست.
🔸
در مورد وجوه مسدود شده، مقدار پول — صادقانه بگویم نمی‌دانم.
اعدادی بیش از ۱۰۰ میلیارد دلار شنیده‌ام. در واقع اعدادی بیش از ۲۰۰ میلیارد دلار هم شنیده‌ام.
بیشتر آن در حساب‌های ایالات متحده نیست؛ بیشتر آن یا در خلیج فارس است، یا در اروپا، یا جای دیگری.
اما مقدار دقیق پول را نمی‌دانم — مقدار زیادی است.
🔸
من گزارش‌هایی دیده‌ام — نمی‌دانم این از کجا آمده — که قطری‌ها میلیاردها دلار و دارایی‌های ایرانی را آزاد کرده‌اند.
این اصلاً درست نیست. برای قطری‌ها غیرممکن است که بدون موافقت ما این کار را انجام دهند، و قطعاً بدون اینکه ما ببینیم.
🔸
درباره موشک‌های ایرانی:
توانایی آن‌ها در پرتاب موشک به طور قابل توجهی کاهش یافته است.
آیا این توانایی صفر شده؟ خیر. اما به طور قابل توجهی کاهش یافته است.
ما آن مأموریت را رها نکرده‌ایم. ما آن را به انجام رسانده‌ایم.
🔸
خدا را شکر. خوشحالم که پاپ چیزهای مثبتی درباره تفاهم‌نامه ما گفته است.
🔸
آنچه ما می‌گوییم این است که
نیروها را به سطح قبل از درگیری بازمی‌گردانیم،
قصد نداریم چند گروه ناو هواپیمابر اضافی را آنجا نگه داریم.
ایرانی‌ها این را نمی‌خواهند؛ صادقانه بگویم، ما هم این را نمی‌خواهیم.
🔸
خبرنگار: چه کسی آن صندوق ۳۰۰ میلیارد دلاری برای ایران را تأمین مالی می‌کند؟
جی‌دی ونس: تمایل زیادی از سوی دنیای عرب و حتی خارج از دنیای عرب وجود دارد که اگر ایران رفتار مناسبی داشته باشد، واقعاً در آن دخالت کنند.
🔸
کمی به توانایی رئیس‌جمهور ایمان داشته باشید، با توجه به اینکه او ما را تا اینجا رسانده است، می‌تواند ما را به گام نهایی برساند.
🔸
دونالد جی. ترامپ تنها رئیس دولتی در سراسر جهان است که در این لحظه نسبت به ملت اسرائیل همدردی دارد.
اگر من در کابینه دولت اسرائیل بودم، شاید به تنها متحد قدرتمندی که در سراسر جهان دارم حمله نمی‌کردم.
🔸
در سه ماه گذشته، دو سوم سلاح‌های دفاعی که از اسرائیل محافظت کرده‌اند، توسط دست‌های آمریکایی ساخته شده و با مالیات‌های آمریکایی پرداخت شده‌اند.
مشکل اسرائیل دونالد جی. ترامپ نیست، و هر کسی در اسرائیل که فکر می‌کند بزرگ‌ترین مشکلشان رئیس‌جمهور ایالات متحده است، باید بیدار شود و واقعیت وضعیت کشورشان را درک کند.
🔸
خبرنگار: چه چیزی مانع ایران می‌شود که در آینده برنامه هسته‌ای خود را بازسازی و از سر بگیرد؟
جی‌دی ونس: اول از همه، آنها باید پول زیادی به دست آورند تا بتوانند برنامه هسته‌ای خود را بازسازی کنند
.
c-span
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/76483" target="_blank">📅 19:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76482">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3SkOtgZmsfmXYbGyzQYO4GG58nM7Py9N0-RYAOdidZin4hSMpB2oKcZdvsQXp5b4EUi5ZCPDUgkNbQI8O4R91XLb6TBWCGwN4sQ_04N2VEPNSFCf6oUiuMA7Ubf4B4XZRXvI6boXJM4I6pYNfT9LqMJVzuQRDZCNt5BqVAQjZEO42p4hE6rWv3Z8mkjvjHi-GsZcqcSxq5r2yhDcUDRideUAl94GizRaeMFvk_qcynZGzIcnw0qfHrwQHPOQbEmdp2b6qniM67nl1TVe2nub8gWgKWtyOy1HxhzkHTrPXdWz3E_5Vt_cMvm4bKiA84UTI0_Fbcv1bxT0Y7_3wFlQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر کشور و رییس سازمان امور اجتماعی ایران می‌گوید به افرادی که در تجمعات شبانه «دوقطبی‌سازی» می‌کردند، در یک نامه به طور «محرمانه» تذکر داده است.
«محمد بطحایی»، بدون اشاره به نام این افراد گفته است که «مورد اول مربوط به یک سازمان و تشکل سازمانی بود و در دو مورد دیگر به‌صورت فردی، نامه‌ محرمانه و البته همراه با احترام و تکریم برای افراد مورد نظر ارسال شده است.»
پس از اینکه گفته شد ایران و آمریکا به امضای تفاهم‌نامه‌ای برای رسیدن به یک توافق پایدار نزدیک هستند، برخی مخالفان این توافق که از چهره‌های نزدیک به جبهه پایداری، تشکل سیاسی اصولگرا و تندرو در ایران هستند، علیه «عباس عراقچی» و «محمدباقر قالیباف» شعار دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/76482" target="_blank">📅 18:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76481">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fUIgSDoiVfoYhXXawl61tlryOA5D4cT4PHdpuuEgts5kLCrA5PewOU4WstWbg6kzTCzdOelvUcFPlwFbcNQ3QfR8S75uT6rVC44FONlH1P2E56M4W3Jo04_9hiEcClWeqgIqgFz7AowYzzako0d0Ye1olcEVK2CZAIjMm1YUn6WwjqKRY5Sv0BxoRhD_Vh9nJwnIUJ5JDIrJBtXK-DzBxtYMzT7KekUBtgvTpfzwlhO_Ese1PR0_-JIDCwraWt9ycQ55YLL30Bwa_NrEUzGsV6c5ItojF_qPxYRyCV654dMXWdjmNoj2FX-obvpp5McgupjqQlIbSAccbNty80dMUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرنا: به پاکستان گفته شده "نیازی به برگزاری نشست حضوری در سوئیس نیست"
ننوشتند کی گفته:
منابع دیپلماتیک پاکستان گفتند که سفر برنامه ریزی شده شهباز شریف نخست وزیر این کشور به سوئیس لغو شده است.
این منابع مدعی شدند که از آنجایی که یادداشت تفاهم اسلام‌آباد از سوی رئیس جمهوری اسلامی ایران و رئیس دولت ایالات متحده به امضا رسیده است، به طرف پاکستانی اعلام شد ‌که اکنون نیازی به برگزاری نشست حضوری در سوئیس نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/76481" target="_blank">📅 17:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76480">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k_Co3rhh5C7If9nqZppkpE5QYyYtDk_m8Aq9PIemnUr2yXbUq2GnpOyASxgHbx0Ml9bSEw-ROYOozYeZfHrXnChBmXHPCYVYRMLsMs9UDAtVadbfOPG0ptGsnPfpvhREspuS_OEuBeP-xnfNUXVeH6e278zajtKB6LI9VAiSkPX3XQAvIv5LUj6ezjffXuSPDyjg3BZ5u6T3Cb5KlLRv9RRoGmk34lnHqas8Z87MgttOqDPTpcAzBLDAvMNaNWM3DB0Be6NsxSGyV1n-wLUDY3dWDPSfTbIPW3_icBs7mNY48AJKfW9W9ED4r8wO2ahylwmV2Zxrm_g3VJFiXwDMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ ترجمه ماشین:
«نفت در جریان است، ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد، جهان امن خواهد بود! بازارهای سهام غرش‌کنان پیش می‌روند، مشاغل در سطح رکورد هستند، و قیمت‌ها در حال کاهش‌اند؛ مقرون‌به‌صرفه شدن! کشور ما مثل هیچ‌وقتِ دیگر قدرتمند، امن و محترم است. «خواهش می‌کنم!» رئیس‌جمهور دی‌جی‌تی»
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76480" target="_blank">📅 17:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76479">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D1F8QFYt8eKN79FWy0GapO3J5KUqUAZILxSllRywNzs1ekGbvgL2EBrYN3qWbwH30UKgdWA6jahwGDxgv3KKMRSCCG94hO-lV544x-dgWxYmjRS4DCh6VBUdRlM6-htZdFmPjiVBOy1dN6C67-7-alfhC-5lJq8TkAZSP38ZQGt5iOmgGQLomJj3qnazSzTtXh4CjIH14l-A_yLHA3BPfDZ3tXLPhSOQwq8H4JKDaK8ZVnLf6Hj1B1GOMEg3G0GVl66PjeTqR9p_TmlMl0WoZGUoJsdi_b8lpxC9t7noJpffQM9HRBtzdpC42Q8DJfYzp3IxHBpdzQF9e18elX5d1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست چند دقیقه پیش ترامپ: "پاپ لئو از توافق صلح آمریکا و ایران تمجید کرد."
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/76479" target="_blank">📅 16:37 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
