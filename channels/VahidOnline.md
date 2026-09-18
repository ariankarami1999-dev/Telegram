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
<img src="https://cdn1.telesco.pe/file/qjGSm_7rwnSNmYOJHtVnbYMhCO5LStcok0MSb6WQm4GWYnW7snzCC0HREB7hcRActfkqVWjLc1SZbVWRkH9IvuqnqXuM2dqVQnuckm9U5gtHI95q4t9wqJ-uj_weAajzxtvLOcWxR1K5gwOw8nPB2KgeBn7VWIUckIE6NIWIJnQUcIk1dBmxZ7kmT61SX6w_iX_APkhyGZaIf5gl77en7GF-xEPq4wawLAP3ykZU1xYndqUfqL-hXVjAFz8MlLB8NtJA21M5BnQjIgylshQNI6DYvVqz9_sj4kNw37zcphiBNW270Tva0vQg3upPN9_9yYiLdvVkbHTQPE0a4tGYJw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.4M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 05:52:39</div>
<hr>

<div class="tg-post" id="msg-78425">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3Qekq9icDmVgzAbWPi74UzNogNZLdzgoh3KV_oz7qJMtZTGOrp6M_bpjGpgt0vmOJOwMNPY1Ub5iX_8yhWGqBB0IEI5jHGMn4hCSG6qxU7UXzUV0BhjmXNVmR-9aeeKA4qsm5xMJP5W-h1CbMtoGu0h_Pd4tB6sNnk--W89PtbyUbMQJx9XqprfHdYzBmxTjEwu1vTCYWzfDMsByEjFn9udDiwRqRGd7RYFHQsdTwcjnphZdg6qDXPrScqFSZN8FYKAB_jPjtQAjaSplspkauU18d6mt-eV3XrCRhv2Mx-VZCONlLjWBtB-1EV-V7T8GO_pYLygb_rGJ7wASjYEiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران بامداد جمعه ۲۷ شهریور در بیانیه‌ای اعلام کرد نفتکش «ترند» با پرچم کشور توگو، شب گذشته هنگام تلاش برای عبور از تنگه هرمز هدف قرار گرفته و پس از آتش‌سوزی متوقف شده است.
سپاه پاسداران در این بیانیه گفت که این نفتکش قصد «عبور غیرقانونی» از این آبراه بین‌المللی را داشته و هشدار داده است شناورهایی که به این شکل عبور کنند، با «نابودی» روبه‌رو خواهند شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/VahidOnline/78425" target="_blank">📅 02:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78424">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eQGZENOv__w246AKts-YnozSbxnbKmxvBPV2231hzPv1aPdThRLbyUcrXvlqyCoOjh_Lutv6belzI9ia05O2jzZzm9su7UKhrG5ATsof-CmjJCmnYWXTju8RxqpUfccFgmV4-YrWY-pRwaZgH1F1U9hGmjLT5934Bo-miu97ZclNHkdIyX_RJTNKdnOrMvrS6pddIcha-VfkO4Ro6e-YG0yi9s8kRpM6GJDGizh2VutGan1LvODTY4D8SHtmzbDlVR4bvdmf8SK59zq3yEuOJ5BY_ulWHFO3npBT-PqwqYwUQgZUQo8dmOMK31a0je4DPOsJMPk-oinyct0gTShIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا  گزارشی از یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایل دریایی شمال‌شرقی خصبِ عمان، دریافت کرده است. گزارش شده که خدمه در سلامت هستند. تا زمان انتشار این گزارش، هیچ پیامد زیست‌محیطی تأیید نشده است. مقامات در حال تحقیق هستند.
به شناورها توصیه می‌شود با احتیاط تردد کنند و هرگونه فعالیت مشکوک را به UKMTO گزارش دهند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/78424" target="_blank">📅 23:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78423">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TLfNllgU35EgV96UNQHs6wBKQe_mwbri4emRdRbEiJkfKpwXKJvCW-Mok6wyIi_KxfhkTv_z9AVOmOYXpHmB5V222nGb7AEx5EKfrXTja3KAj7TUbwDPfFLKdUTV7R0kocVYJdiXzSHnKFSMpb6vPbutTlVWK-7uxNKjB545T2VWoat6Pr3MTIhfMwFE7O7TI3YMUHusKfQ_J_HiMSoLrDqiZrMzccrZjdYh4nCtWuhSXvyNeb_ng65kjCRFPiXJNsv8IM5EBSIIc_mCHZfTWfLKp-WUE51Ci1jRZ5eqJDm7Z9g5vmD_ewnL8HMiNY2v9Xm5-myBHwR5c--PN-7_rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/78423" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78422">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Py-scO-UyjwiiEdH7_yac-m1wBnN6kvU5CH7Io6lJrpVX6D8-RlH2MfMw4dHpEFkRxKoR4WnDG1FXvqtqCjCwANYir01zlE0t4iyymCe5PPc7jDBoTlzNUwTqI32iyMeZ6l2JBYmWEakqsg9b-fXAD9z1fBUi_Cz1GkAdWd0RkGVAVdUewAEHr5H8Ul_9n1Cq99eSst3ERhagTOEDUgW6jkUpXBpfT9Y881aKOcgHGz2vWEjloPE8qgCWMJAgUpRoxubiMdg6OhjR4PATEqKE7qfYxr6tbiKnHyw_zHHLQwyuUnMhK72VsSwel0nuw_ruMSftmUCsYvkTzr1Daq8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس نیوز پنج‌شنبه ۲۶ شهریور به نقل از مقام‌های آمریکایی گزارش داد نیروهای جمهوری اسلامی در روزهای اخیر دست‌کم دو پهپاد ام‌کیو-۱ آمریکا را سرنگون کردند.
مقام‌های آمریکایی که به شرط فاش نشدن نامشان با سی‌بی‌اس نیوز گفت‌وگو کردند، مشخص نکردند این پهپادها در کدام بخش منطقه سرنگون شدند و از کدام مدل ام‌کیو-۱ بودند.
این پهپادها برای ماموریت‌های اطلاعاتی، شناسایی و نظارتی طراحی شده‌اند و قابلیت حمل موشک‌های هلفایر را نیز دارند. سی‌بی‌اس نیوز نوشت این پهپادها در تنگه هرمز می‌توانند برای نظارت مستمر بر آبراه، رصد فعالیت‌های نظامی جمهوری اسلامی و شناسایی تهدیدها علیه نیروهای آمریکا و کشتیرانی تجاری به کار گرفته شوند.
بر اساس گزارش دفتر بودجه کنگره آمریکا، از آغاز جنگ آمریکا علیه جمهوری اسلامی دست‌کم ۲۴ پهپاد ام‌کیو-۹ ریپر به ارزش تقریبی ۷۲۰ میلیون دلار از دست رفته‌اند. یک پهپاد ام‌کیو-۴سی تریتون به ارزش حدود ۱۵۰ میلیون دلار نیز منهدم شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 207K · <a href="https://t.me/VahidOnline/78422" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78420">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J5RngI6l6GA_2uASuhg7dR7oMv26nkxSuLnvgNJVlPw4EBZazSZmfPjVi4oPBLKK2sAih5DXec1HGasx2LBJsiHgjeFsXvNNr2nUiaS4Y0u-4zuqnVMPFjrifw6egZ7aIW9yvLuqQ8sj4MpUcY0eWpV_e-zuZRSmfmViXe9W4BCO3bESfIh6-5jrjuovn5RW-CQ65X9hKtEgeiEqj4fdH9QNPvvxlkFilO0yVr-Fzgpwk0_UwQDDuJ0R5zBLq_8hhuYcSPLdOQDI3dB8gFA-q-GDpNHjbCN6yf9NP5ubnZZ-sXNocO8yPd0yoJXRh143z-tp_p6A4IaaKnVW88nucg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37ae7c8ac7.mp4?token=Zx3P34BEOIA4y3xY5vrl-iMxN_p05p-qfQmFBwbAYh4v5SGeb-t8T4mhrV_rZDckpR0RK2V17w915I67Y3G4laqY3PKHeI3McVL5tdudfjdJhnoTVHpG0hGwWfVfU7DaCe0cIlGDXfIRZ8YJmtNXdX_JCZPzX3uRwliQiRlVc-clvZmXcHaBf6vmbnwGdy7o2h1AWLqET7NajjgxDZmxqIN25D8g4F8ejWeIjTMg7tn0UXI8gKYLb8spJCpMaNe8GeKs-2go5PDMcnyYBJfL-h6iUL9AgOikiGqM2Ne6FDUl7QwkCDym6VQ6uFy_fqi7xcdJjnpe6usq-QpsGi6h7g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37ae7c8ac7.mp4?token=Zx3P34BEOIA4y3xY5vrl-iMxN_p05p-qfQmFBwbAYh4v5SGeb-t8T4mhrV_rZDckpR0RK2V17w915I67Y3G4laqY3PKHeI3McVL5tdudfjdJhnoTVHpG0hGwWfVfU7DaCe0cIlGDXfIRZ8YJmtNXdX_JCZPzX3uRwliQiRlVc-clvZmXcHaBf6vmbnwGdy7o2h1AWLqET7NajjgxDZmxqIN25D8g4F8ejWeIjTMg7tn0UXI8gKYLb8spJCpMaNe8GeKs-2go5PDMcnyYBJfL-h6iUL9AgOikiGqM2Ne6FDUl7QwkCDym6VQ6uFy_fqi7xcdJjnpe6usq-QpsGi6h7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/78420" target="_blank">📅 21:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78419">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbJ654k8b3ZNIIk7Lndv0soTy2tyRBoOUu_XWPWOfGJMANIazkvIE0qvHsNd9VqveBRhmS6nRe8Q-mnyoR-bKXFi2Cqbp8TUbz6uEy7w4XwkVfJcoFRD1qU1maSVhU5xs-nw7QOHifGEOznkcYTIzltp5byoGzreFpETvUYpf6ksxHrwqt8chEQ-QoPiv6QEy7kqNZ7OisA1qW1NgqIZZvOlkvhwQyzybzVG3wJ_OIomZKOpVaEXPZ8IXWFjfGpHbSt6k-_3Ou4qUgkgAikxp0uZ-P1_06aKWJoM8nLPLmOvrxa4nNAl5FQOs2bl6_C2_HUnftzo-rVetwNjKtL3TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیات حقیقت‌یاب مستقل بین‌المللی سازمان ملل درباره ایران در تازه‌ترین گزارش خود اعلام کرد دلایل معقولی برای این باور وجود دارد که آمریکا در جریان جنگ با جمهوری اسلامی، در دو حمله هوایی به ایران مرتکب «جنایت جنگی» شده است. بر اساس این گزارش، این حملات دست‌کم ۱۷۸ غیرنظامی، از جمله زنان و کودکان، را کشت.
این هیات در گزارشی که به شورای حقوق بشر سازمان ملل ارائه شد، حملات آمریکا و اسرائیل به ایران در ۹ اسفند ۱۴۰۴ را بررسی کرد و به این نتیجه رسید که آمریکا در دو مورد حملاتی بدون تمایز انجام داده که به کشته یا زخمی شدن غیرنظامیان و آسیب به اماکن غیرنظامی منجر شده است.
بر اساس یافته‌های هیات حقیقت‌یاب، در یکی از این موارد، موشک‌های تاماهاوک به دبستان شجره طیبه در میناب اصابت کردند. این هیات اعلام کرد این مدرسه به وضوح قابل شناسایی بوده و در این حمله بیش از ۱۵۰ نفر، از جمله حدود ۱۲۰ کودک، کشته شدند.
در موردی دیگر، آمریکا با استفاده از موشک‌های تهاجمی دقیق، ساچمه‌های تنگستن را بر فراز یک مجموعه ورزشی و منطقه مسکونی در لامرد پراکنده کرد. بر اساس گزارش، این حمله ۲۲ زن و مرد غیرنظامی را کشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 192K · <a href="https://t.me/VahidOnline/78419" target="_blank">📅 21:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78418">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGH2Uvhqn5ytTGVUuBMsUkBCABQtPXfqExJo6tP6kocUU4NlsM8x9OSaw4E4_GVNS0I5ZoPXIfbR-8ENl7SuQamGt22qXMt2PE0dW9uzpqQyNHAjshfPnORzm_oyy8JLjFdgyZhIeiWysLeJZF_BkqYfFF_FsJZuGWJUDChrW4dvL0McMaTseBOB2Z4nymlpQgo7zGNqU-umDKM0CCfhzjU-idos7unBlmaPv_SWVNM1LRe1CkQUhj6Pn4p44IQSd7ff73Il1kvUBiIHKtqbSYoz5H7lL1twZDSQCW3DPSFQ6AkYV7SwTD-tGwUZQGTsHxnsu_7y8ZbGJDtA7QXCbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه و چین روز پنجشنبه، ۲۶ شهریور، در نشست شورای امنیت سازمان ملل متحد، پیش‌نویس قطعنامه پیشنهادی ایالات متحده برای تمدید ماموریت هیات کارشناسان کمیته تحریم‌های ۱۷۳۷ علیه جمهوری اسلامی ایران را وتو کردند.
این نشست با ابتکار فرانسه که در ماه سپتامبر ریاست دوره‌ای شورای امنیت را بر عهده دارد، در چارچوب دستورکار «منع اشاعه» برگزار شد. در جریان رای‌گیری میان ۱۵ عضو شورای امنیت، این قطعنامه ۱۱ رای مثبت کسب کرد، اما با مخالفت صریح (وتو) مسکو و پکن و همچنین رای ممتنع پاکستان و سومالی مواجه شد. برای تصویب یک قطعنامه در این شورا، علاوه بر کسب حداقل ۹ رای موافق، وتو نکردن اعضای دائم الزامی است.
دیپلمات‌ها پیش‌تر از مخالفت قطعی روسیه و چین با این طرح خبر داده بودند. مسکو و پکن معتقدند که با انقضای قطعی قطعنامه ۲۲۳۱ برجام در اکتبر ۲۰۲۵، تمامی سازوکارهای تحریمی پیشین از جمله کمیته ۱۷۳۷ فاقد هرگونه اعتبار و اثر حقوقی هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/78418" target="_blank">📅 18:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78417">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/caed21affc.mp4?token=gmuFX9WZDu_ZEXynaFYlYPp_yBROraESvSdCREtsx-zJJv00h9n5yr6ATo-g6-1BcCYgPtLqFGY-YZisoVLTIWlnDeE3HiAt_a5jRsmq9_b17RQlFhGWfDpLPD7VzMoy26rL2XnXLZp0zMI_Muxb8mFOiJuiPWd5Oj4dQmLDQB1kQ4Pn3c0-v1fTi2DqXapQ0joXrdMK_7SkTxGPgUgkaQmMv5fmO3mdefEcBDSHFSNYiljSieLqjdfjyE_ZVa8_DEPOsrR6l-FQmAVyUTGTp1q8he0XzkofuHcW2nKux7vbqZ-YhgeZIGKKMpf7y5iN77u9xJQQ9jRq7yGH5GJnwg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/caed21affc.mp4?token=gmuFX9WZDu_ZEXynaFYlYPp_yBROraESvSdCREtsx-zJJv00h9n5yr6ATo-g6-1BcCYgPtLqFGY-YZisoVLTIWlnDeE3HiAt_a5jRsmq9_b17RQlFhGWfDpLPD7VzMoy26rL2XnXLZp0zMI_Muxb8mFOiJuiPWd5Oj4dQmLDQB1kQ4Pn3c0-v1fTi2DqXapQ0joXrdMK_7SkTxGPgUgkaQmMv5fmO3mdefEcBDSHFSNYiljSieLqjdfjyE_ZVa8_DEPOsrR6l-FQmAVyUTGTp1q8he0XzkofuHcW2nKux7vbqZ-YhgeZIGKKMpf7y5iN77u9xJQQ9jRq7yGH5GJnwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/78417" target="_blank">📅 17:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78416">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MJraw3AhuIDT-vttPT2t8kZutxtNsfBhIFHLNBJaYKTInfM4WrkCa661z5pfHvCw_3-ghRBmlVoTP_lXdn_VkeiJPW4kQ8c8r8sdjREc8vJlOaVOzMEwhzspZZwEapIoKJuf3kkknenxx2uRl2gRbC81dqboB2fkEDcmtBM95zhNOJaGWSlzrsirLDgwfgMr4slUBoOW3hMByylMUYu_kfE-4ZFoEWR_v_qvub1I7gsxJkeUfZvEeHW8dD41tW-X9Q8siduOO_Y1WqjjLvA3L2R5YqdLc3ZH6gBCSBewNfU-CDuxjCR1AcDc3oRAPlPGB9dv2F8CMg9LA-NeyR7Dag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، مدعی شده است جمهوری اسلامی مستقیما با دولت او تماس گرفته و «بسیار» خواهان دستیابی به توافق با ایالات متحده است. او همچنین ابراز امیدواری کرده جنگ نزدیک به پایان باشد.
ترامپ بامداد پنج‌شنبه ۲۶ شهریور ۱۴۰۵، پس از ورود به ایالت کارولینای شمالی، در پاسخ به پرسش خبرنگاران درباره مرحله کنونی جنگ گفت: «امیدوارم به پایان جنگ نزدیک شده باشیم.»
او سپس درباره احتمال دستیابی به توافق با جمهوری اسلامی گفت: «آن‌ها می‌خواهند توافق کنند و خواهیم دید چگونه پیش می‌رود.» ترامپ در پاسخ به این پرسش که آیا پیام ایران از طریق میانجی‌ها منتقل شده یا تماس مستقیمی صورت گرفته است، گفت این تماس «مستقیم» بوده، اما درباره زمان، سطح و محتوای آن توضیح بیشتری نداد.
رییس‌جمهوری آمریکا ساعاتی بعد در یک گردهمایی انتخاباتی در شهر گاستونیا در کارولینای شمالی، بار دیگر گفت جنگ با ایران به‌زودی پایان خواهد یافت و «پایان واقعا خوبی» خواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78416" target="_blank">📅 03:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78415">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ByjKHIf2sYcxfcFiavxgPJLeYQzT1TNKrioFo1AkN7uo4DNE0K4K1R3U2GOx7m3urf6TbhDONFI9ShUcKGG9UzA4U53xjlUoWo2IS---wam1bPcqMwk-2PwJbGKnTNZBXBN620c2myXWBJOOWRs4Am5VYeHqBVuORHQXWYv8Hux0mMjiCon9mBU0jITnzMUr4oZDrEXwsanwEPoWY8fbMQbU1sVJ5BMba0nL93eRdigFBBV1j3MzP5Je6hPQFQs1Q9GU7u7uBhV0SOX-epRR3XQ7vaoZfE7WZuFoNvz6z4zi8ncahZvbCVdVQ9jk2loD8DUwu55H1nWfXtmbvF-b0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/78415" target="_blank">📅 17:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78414">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/US7M1H9v8AUgiUaoLsJ03Yl0BVXQTjV1JDp2eDEm5iixMyRoQmm1c_0RFnBgwBKb0hpIXyrNfnuJG7hoNXMdIFDXGn8R8OyaKW0pI-y-1n4n5svN1gN7AH69v-yWFWdCqTuQqW6V1L01g8XfPH-4-X5XbPlQ7nl4IJgoUAO8sdY8mYC6M7lkN7O7DgMYoKQ5Mq8HlmVQdmFTK3uVEP2vYT1r8qASYFoX6fBNYXJCY2p0bOzsLEJwxIOMdlxRt4RRRatty-dp5pp_FV2-fz4CIj7G4h80EHQqxhlTznWO8yyFDEuP4jCVGtW8_zxyiUgYNUqpXItzFQs36L8YpYFpsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل قدیانی، زندانی سیاسی محبوس در زندان اوین، روایت جمهوری اسلامی درباره نقش «تروریست‌های وابسته به بیگانگان» در کشتن معترضان دی‌ماه ۱۴۰۴ را رد کرد و نیروهای حکومتی را مسئول «قتل عام» آن‌ها دانست.
قدیانی در بیانیه‌ای که روز ۲۴ شهریور از بند هفت زندان اوین نوشته، با اشاره به راهپیمایی ۲۲ بهمن و تجمعات حکومتی ماه‌های گذشته پرسیده است اگر عاملان تیراندازی به معترضان، آن‌گونه که حکومت می‌گوید، «تروریست» بوده‌اند، چرا در تجمعات حکومتی که در امنیت برگزار شده‌اند، اثری از آنها نبوده است.
او از رسانه‌ها و نهادهای حقوق بشری خواسته است درباره این تناقض در روایت جمهوری اسلامی پرسشگری کنند و نوشته است: «تروریستی در کار نبوده و نیست و قاتلان [...] همان نیروهای [...] حاکمیت‌اند.»
قدیانی همچنین در این بیانیه علی خامنه‌ای و پسرش مجتبی خامنه‌ای را مسئول این «جنایت سهمگین» دانسته و نیروهای حکومتی را به تیراندازی به معترضان متهم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78414" target="_blank">📅 17:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78413">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tics1YWgGNV0984osQCrKzsN0fzZL6cuqal1Wvy5Nv7kajXScoOxR8qwxD_a9nUalpyj6uEmqF3UgkteKEmoCsK1ITT6Kyu_VYHT3UTQDeZRM69gWEMqqVV5iw8_I5q_mV-aX2tx7lUMKn2IoshGOMIBzFL7rWbex6vlK7fsynQn_OxMcOkMeF7__dg94YUeYJhAMbs0eBt2pIQccQGlzG2hbxF16H_UCkzzsZ6wiJtHGO5mWQ7q7y1qwlHMI-umbeIxcp-W4vf6Mz-B7uuRxpiSet-5fc8P1XKOlN1LYcnAzfDkSyAhP-UgxBM6BWz0YPJIJbQicc1k1x0-EtNL4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/78413" target="_blank">📅 17:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78412">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IDovM2hmW7Bm3rxhc6-tBtkpWGqcGN2oQlD6UxJ6BC_j7Kwhy-jIURQiM59OS7Unm2-hpdAV4kgofLmRgawE__6CZQRrD5pJDthJAEzRcmrlFTBpthHjwO-2epbq_lE-pppyfCLmV94PJoQthntcBf-02X4Rk97HQVvR1gsITXwV5GW_bz32MhZWYR8en1X44xkJq8UHaTW_LJBh3VXrev5IS9HmEeX85yEEn2TuKcKHxmXnmgiZX8ejFh-vjIKV9uzYAoztPz8ckI0HUfBE1KZ2i_1s_OxHbVzdSjSkPdF1MjAO4-aloPc-cNUx5PX3t9ZK5O9urG2rdPBRjf4SGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/78412" target="_blank">📅 17:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78411">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6Dkm9hn40K66w2lS0yp3fXj0APH4TsgYhPupy4f6qk34qmwRjDKW0bY1EfvOUlWj4zxJpABDe5zI7m_49gsnach7ZAoRDoOAY9abf6Ed6A6ZZEbEYIROg-q3zWoULhN9HJRiZQvNdq2Cn9ue1tS2tsnqYVQe2YCL48NW4Xy280fOfbLFhISrTKjXs3mav-o4Q3BTsHkHYVaarpbJgaKAPf-5T7LOh0bmEi1qwiSRS79jk0yTYGevZ8lcE84cn7GONiOM-N3NTeu2H_MquZBO4K7WEd1-Zfd6mKHIinj-6RaDsfN-7CDxugdV1My9ygZZVWGWq0dpsX5wv1p1sS9Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«جی‌دی ونس‌»، معاون رییس‌جمهوری آمریکا، گفته است جنگ با جمهوری اسلامی طی «یکی دو ماه آینده» وارد مرحله‌ای کاملا متفاوت خواهد شد و واشنگتن در مرحله بعدی باید مانع بازسازی توانایی‌های هسته‌ای و نظامی حکومت ایران شود.
ونس همچنین با پیش‌بینی «دونالد ترامپ» همراه شده است که جنگ پس از انتخابات میان‌دوره‌ای آمریکا پایان خواهد یافت؛ هرچند توضیح نداده منظور از «مرحله متفاوت» تشدید عملیات نظامی، کاهش درگیری‌ها یا آغاز روندی دیپلماتیک است.
معاون رییس‌جمهوری آمریکا در گفت‌وگو با نیویورک‌پست که روز سه‌شنبه ۲۴ شهریور ۱۴۰۵ منتشر شد، گفت: «نمی‌توانیم آینده را پیش‌بینی کنیم، اما فکر می‌کنم رییس‌جمهوری درست می‌گوید که این مسئله طی یکی دو ماه آینده وارد مرحله‌ای کاملا متفاوت خواهد شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/78411" target="_blank">📅 17:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78410">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q44gdnWpc0AycId_FNyU9F2l5V02pJ9H_dmBtkpw4dKtyuAttIvtc1hn2qnFSia21XHhiNvUpRjyqG-8UTsSUBhRa5Wkb0H79PWexjM_c-IUoJr29dOy_HbBOIOXG7UDvPkUEt9puL9hLflmsQNL65koOtTp5CDB2-V2Z8ApL4YS3KAXMmgfKv9tiuCaId2rNkAeeXrcKkJssijMQomtOeA7aef-xzg7hB7AZ8DREnCInl3lG_vy00GvwzMHkHDPGqOnbLMtYSKTAhSjadLVOas-O7d0UQTvkTdQvPRbNRrU0ybwWMxDOfOKm9paSQ6VSbOwYqs_0wYiYVMXmHaZ_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/78410" target="_blank">📅 17:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78405">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=KIdmCSBQt3yOpTVQcbmlId0D6HGPI85g2qXhuav3RAQIn0fvXOZ4RWJWQgbOKXCOKOytpekPgriVXD4RDx2OVyydscSivNvBGsLDYWJ2u1E2ehJij_szHhux6OGJzk1rGjUzgoCQ8lcnpwgFLY1y_M7OcPktHaPpsiZJ7O-abkhaV1RqwwfF6L7j-pZj1dghGJQcbB6Lfu8HaoRHwofYd_5LmFRX1frvk99sE4_QBjwr5IbUQGVw_BHBRiUkYCxoo5N6ogMuYIMXpKt9jpbSQ6XOeEdiuXom_OqmB1AK3Yv07IIiSi4wfy1t6eGbS6n-X-RFgyPyCf6QMYypzr7QzK388GdntEvsF85htNmMOsBP74yv3HcrK_xUlUB3FW6mcrD3jcyr__Q_6Eng-WtoURtpS2d4i48lz0lu-_OyEkX5jI2Sk2es3JtuJppcd8o4JtumNRJJFBtMT-Q3WmLm_opU3hceaJU7ThTkFzV0RfWDAExvM0ca5vb7V6lGg1O6-V2-jomZrX2RiZACzi52GmEkfUOp8HFdaBXOEkuJl_a3EMtA3x9n-NHl6nghGdzkDBEBjIlfixeFVARvd5mqzJOaVadgDyal9sKdBM22puWewbCIFmNgoUUrAb5b7Fn05vUVgPEt0T0xkpXenAFRWSk6peD1w9LVLWySpnNtC04" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=KIdmCSBQt3yOpTVQcbmlId0D6HGPI85g2qXhuav3RAQIn0fvXOZ4RWJWQgbOKXCOKOytpekPgriVXD4RDx2OVyydscSivNvBGsLDYWJ2u1E2ehJij_szHhux6OGJzk1rGjUzgoCQ8lcnpwgFLY1y_M7OcPktHaPpsiZJ7O-abkhaV1RqwwfF6L7j-pZj1dghGJQcbB6Lfu8HaoRHwofYd_5LmFRX1frvk99sE4_QBjwr5IbUQGVw_BHBRiUkYCxoo5N6ogMuYIMXpKt9jpbSQ6XOeEdiuXom_OqmB1AK3Yv07IIiSi4wfy1t6eGbS6n-X-RFgyPyCf6QMYypzr7QzK388GdntEvsF85htNmMOsBP74yv3HcrK_xUlUB3FW6mcrD3jcyr__Q_6Eng-WtoURtpS2d4i48lz0lu-_OyEkX5jI2Sk2es3JtuJppcd8o4JtumNRJJFBtMT-Q3WmLm_opU3hceaJU7ThTkFzV0RfWDAExvM0ca5vb7V6lGg1O6-V2-jomZrX2RiZACzi52GmEkfUOp8HFdaBXOEkuJl_a3EMtA3x9n-NHl6nghGdzkDBEBjIlfixeFVARvd5mqzJOaVadgDyal9sKdBM22puWewbCIFmNgoUUrAb5b7Fn05vUVgPEt0T0xkpXenAFRWSk6peD1w9LVLWySpnNtC04" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/78405" target="_blank">📅 17:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78399">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b6m5YOeYvCmDtRTgP2ViWxjwV1bCmUWl8B8E0T5nyILzXK-qNVQEsyFlQj9LmBWHGjtffWhzEgQwOgEORo4B7Z_Hj37b1-r3OMZdLerP8I7XonfUWHdzafu43zM6F4zb4xYdoReIZlh7w1t0LxRC7UtHBNfbtWMsNXQfOVL6qqZF9mnrn2DKMgfGJRgANXdS91qlLYYfuMXhJ64VoDihd9Oi5eAmAcSp7w43O2ZBb5i35joJimrOKYQPTe_PG3ce7KVJeIlYawPoDxuhjflRxjAd5P4UpKSyK1vayQALFKnKX5AdNy5ewmnO_xvyxI45PQAED3Bx6geoYACQfFEPKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sUrIrUFXBeLVlBk7fTSVD0ENiPVe3y-D2poECjhBFrrsuRudpqLKxuKf4fMWPGqWiMdVoZqMID7yhW_wYlqnweCU4PAj6lnRnPiRojyqZC1FD7bMj-m_RdqfgCX0QtJ5t5rWRx-ZSAjbQmeYfw8VmOYAay5kgydHwprfBa22vb_ng1IjQwSA8TV3mdfIGrqWQb8oWxTD1mAxWhTGQF9HoYiIyBoqmA3hVkvpuAVH7RLLtydriTqneIbFW81Y0co6aa1YdVnL4J03IsXDLgMT38e0dnT7CGPhlOprIVDMKf3KCkH88jZHj2wTkNc0kBvDfBOLTLIKcSuRUq16P2v4jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NiObqe8rrsJdL-rE5LfFeCyc88biqNnVymlMGTAdu9MrS9GflO0zn-JtPXFAFT-RNLi8jzv0pRCYmWGh5CvGSt-JQzZocBAmtzHrLK01jLCFsokvRLwsfGWe-flh9Ar8aB_RC7rcpYLLWIJFWYZEZnAQjckgl7xrP6Y3Zxp5sz86QyScwKjnEKaW3Qpv40N7LhlkFiikOl4vJ_HrCrtF3ekCTgnDctN2jslv-1S4FY9I6uj0n0s0HHiTOhNY1Qm2pgyN5rjm05HKSwEMDvrHyim5qw7mhYG59HIRs4idQ85sKDMTNYNdmV9TP3BNc-2BB2hm7ZAXnjpW46WqAKltBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cCelNVNR_i3shEB9Q4B7l3R5fqDXMTpRw72r8oP4aufEO2IU9GS3_8Ki5k3kcbbT_D1eQv5esurP-pwg9ji5QF5gfuy63st5xxo9FNx5fAAc-Nw6w9uVvs9UcJgpbkL66H8mZ8xNlzfpLUmlKeffkWwlAUf0MvxOMEGnw7aFkwT13g-seaFZFIFWgoSE2nsRWfJq6JfsWJR9FIGGc-aGBgFep44Tr5LmPPXVKl6t60rpE1h649ioUL_gWcVrFpqcx6mL951mkNpDikhRknxA0wa8E_ANJZXfYUjryLxvobGlTmhMLcaXS53ov1IsVzbaYegL_tVLxQrFbfZ0cSyucg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rUAvbcS8oCmqvq-SW0c3KN1oENW2yuI_WUwtfU9zusMIZqK2FWWXq52k9wTfgN4JOIxxqWpPp8PT6g0oCXQACCGbcXHhEruESbwKZEMTbUISYlfxyOsi4k6eVCKhodS_7Hj2Kz_IT1pL_Ymp7onOiZoG6w9dTMjExZ8PFqGZmN3AJ0J1wcuPV27fqFx78gFyBAFu8d3EdPjAJ3q-wfNfMPcrhKpdusyge6WZgDy0JJ2tRaxo0T9Gzm1MzVh5uGMKGosuhTc3-fadfPgtOVl66_AMN-u6zflSEZjs8q7CmT8bd7yhyFwpt4glbmAfvakPtrEUFQLZ1jnDS821w09xCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GGZvMX9ktJyZbuNC7QrRl3jkf-2JhRUV4lvpH8oP9E-RyP0qz2khjNTcoWX2qOKueIIJKpB4-sd3sX_aXo0_pOXCX0HmxfC_Kp46txc48gPpnRRw9OhwaHQOdVnqxuCV28JEwVwjzDC8MoSesGXoTrvt90uClrs7RnCAySud2pI7pFHEgGgrUGYL_8pGcPcgi8CwLhWAsSRuOsq8RHw3-PNOU3-ixyHDRxXL6bPj4QeVotep0HkWOLpmAbxDY2TzMSO-qKEYGkPhL56Mdjount55rtEhDeWaReVAVAp_N4LWzZaaYJH10Qow9O7DsQoaV3oWdE_iuOzFIGwA0TpyKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78399" target="_blank">📅 04:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78398">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cF4DMEdrMMk_lzG2fZCbjA0fYRvLIZjCAkiYvWg69nNKbJuBl_kRVwfWiv4OezvRzAkMN2bdzaF8ME0UZi3TZZcAeaIJX6KMATpcMnfyHhosJZUhERNCKdc6NldGQr_ZL8ZR24kVpBQgmVZQ6CyFt9zVyPGfPqGKt9T2ACEJf7HJNe22zzXsiscj9H0tz7j7XW_QOZeMhVSIsjHIXJA9yq1eyCudykv4369JRh2FMzoRxEG5fbbuTCypdhQMxSF9FSSw87G_SDOi9zK5yIof4DC0qNld-e25W_jyhv_mPuTekugLcJpbQ70vH35_RMJJp_lWV680S3zl09bw9fUz8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی در یمن اعلام کرد پدافند هوایی این ائتلاف یک فروند پهپاد پرتاب‌شده از سوی حوثی‌ها را که قصد ورود به حریم هوایی مکه را داشت، رهگیری و منهدم کرده است.
به گزارش خبرگزاری رویترز، ترکی المالکی، سخنگوی ائتلاف، در بیانیه‌ای گفت این دومین تلاش حوثی‌ها برای هدف قرار دادن مکه بوده است.
به گفته ائتلاف، پیش از این نیز حدود ۹ سال قبل یک فروند موشک بالستیک به سوی مکه شلیک شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78398" target="_blank">📅 03:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78397">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jAi1MamEUa9euBKO49KLMky24G8CRf8m9ZkDvG6a-NhX-tBEZSBbSKs4XGL8UboD_5msKPAHG8V81pWoz1iE5bwG883NjdTNTH6qU5kLK9qJ0JqjzYN-eNVFa2A35jowcn6YS4E7lbe-a2-FLiemfoy_l9TpvFdklf4E8aUoob4XMnnJCbmcOlFzw0W4KZ1C2fxMyHZh5iv4N2gGoZcIkJ-eC2C5q-4DxwX4hznVnionJYwmu7f0OzvAB_SmCsWl4LYz9imcpLLgx9d6URwhCjWRKYK62zg-i1dEjF4QaTyxYYzWEFz1RO62PS1UbkcVMoJtkl9_rEKZXScqmoTYQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از دو مقام اسرائیلی گزارش داد فرماندهان ارشد نظامی آمریکا، اسرائیل، عربستان سعودی، امارات متحده عربی، بحرین، کویت، قطر، اردن و مصر هفته گذشته در نشستی محرمانه در آلمان درباره جنگ با جمهوری اسلامی و تنش‌های منطقه گفت‌وگو کردند.
اکسیوس گزارش داد نشست محرمانه فرماندهان نظامی در آلمان به ابتکار برد کوپر، فرمانده سنتکام، برگزار شد.
به گزارش اکسیوس، برد کوپر در نشست محرمانه آلمان، فرماندهان نظامی اسرائیل و کشورهای عربی را در جریان برنامه آمریکا برای افزایش تردد کشتی‌ها در تنگه هرمز قرار داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78397" target="_blank">📅 21:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78396">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=Nua1_pAB9Z0yPeIjZvtOxBFT1593VZJQ_R-hJBIH6ywUZZ3nQhxE5KikcnhBp2eqsmztpejWrtMiX4nxp8IYJQACyAS-aWozW1gP_tDqPpsSi_FV5nD9SC2kJqSgUzyPy9AlU9Qoo1FxD_MQ0-c-P5ik4gPoyE2iinIQqVc_KjWezYwjjGt4bj74RIPKiBxp_YGCBZtMI1rl1dOHILwYpDGszKPA-Vx3astVp1rY1x2j2X1Bih6Gn5sw2j18YE6_PR65wSKPkXSosNyTKGZQHjc5B5xO52Be-qfpVFMOxaXe0OGktGpdKA8pNfJ6YXlxzjIKPRIRZMEm0KEcbuobRA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=Nua1_pAB9Z0yPeIjZvtOxBFT1593VZJQ_R-hJBIH6ywUZZ3nQhxE5KikcnhBp2eqsmztpejWrtMiX4nxp8IYJQACyAS-aWozW1gP_tDqPpsSi_FV5nD9SC2kJqSgUzyPy9AlU9Qoo1FxD_MQ0-c-P5ik4gPoyE2iinIQqVc_KjWezYwjjGt4bj74RIPKiBxp_YGCBZtMI1rl1dOHILwYpDGszKPA-Vx3astVp1rY1x2j2X1Bih6Gn5sw2j18YE6_PR65wSKPkXSosNyTKGZQHjc5B5xO52Be-qfpVFMOxaXe0OGktGpdKA8pNfJ6YXlxzjIKPRIRZMEm0KEcbuobRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده در جلسه سالانه درباره وضعیت اقتصادی آمریکا و سیستم مالی بین‌المللی با دفاع از سیاست‌های دولت دونالد ترامپ در قبال ایران، گفت رئیس‌جمهوری آمریکا اقدامی را انجام داده که به گفته او، رؤسای‌جمهور پیشین آمریکا سال‌ها از انجام آن خودداری کرده بودند.
اسکات بسنت با اشاره به جمهوری اسلامی گفت: رژیمی که خود را وقف شعار "مرگ بر آمریکا" کرده و به‌دنبال دستیابی به سلاح هسته‌ای برای تحقق همین هدف است، اکنون با سیاستی متفاوت از سوی آمریکا روبه‌رو شده است.
او افزود: تحت رهبری رئیس‌جمهور ترامپ، آمریکا دیگر صرفا در حال مدیریت تهدید ایران نیست؛ ما در حال پایان دادن به آن هستیم.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78396" target="_blank">📅 21:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78395">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eFjFhgvQHDTbo_ySehUX8hBUb69zRfnXzOz40mUA4NwBtI5xWj5Q_VKI-5uPTc3YYYSfNGnxGtYqI5mL0jUpF-greKg2D8hYn0w_LL1VgxFQsGg29LWr4nRgS0BfzlsTYBeEC6q6eqmNy-uUPUvdaYtVWCb0Fpuqr9U9jIBH8xc_Vw1ABPcWAtjUQJUyT6Y8-M_OK2GDEcBqA6ljSXMGt6gemuoUkVQ_FQnT8rfwTs-eCA896hQfxxHArIrFJydKloEN-6yqcU1l7odlMx51fL2olTEQ9wmhERTSY1-pY44Dx3C8AD6bhWupw3RpnoQ_d1P0R7d7qrPtOTD_Vwr2Fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78395" target="_blank">📅 19:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78394">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=PhN3SSXViHcZ82BGpEBtEMrG6TK0xJ9EvkPMx63bjnWZm-Sx8YpY0IyHw2rwF96Z7Z4IhTmSv4EeQSdoV48s8TFVCwtpBeAZNiyp1xAoJFgZK95IickdECK4HX4pkGZYYVMh1naZEVK5jX4PXc5I6lwa8EcuW9MraDCOuJqFvwWoCqlJV6BFURCDwyvrZB4edVdg9KO5u_xlQA6HE9O4B0ghYydUKJ2c-28M6Bjd5nTi5GxS0Jwg73NpkjfCUBGArR62UZKLD6nzaCWiWYduuuGL7wm_ulGChcyPCL6A9ZFxj5kWMG10uASfmD-xkcOP1wwArO9G_XpaxpjAdiZRPw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=PhN3SSXViHcZ82BGpEBtEMrG6TK0xJ9EvkPMx63bjnWZm-Sx8YpY0IyHw2rwF96Z7Z4IhTmSv4EeQSdoV48s8TFVCwtpBeAZNiyp1xAoJFgZK95IickdECK4HX4pkGZYYVMh1naZEVK5jX4PXc5I6lwa8EcuW9MraDCOuJqFvwWoCqlJV6BFURCDwyvrZB4edVdg9KO5u_xlQA6HE9O4B0ghYydUKJ2c-28M6Bjd5nTi5GxS0Jwg73NpkjfCUBGArR62UZKLD6nzaCWiWYduuuGL7wm_ulGChcyPCL6A9ZFxj5kWMG10uASfmD-xkcOP1wwArO9G_XpaxpjAdiZRPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیوی منتشرشده در خبرگزاری رکنا، لحظات پراضطراب داخل هواپیمای بوئینگ ۷۳۷ شرکت سپهران را نشان می‌دهد که دوشنبه ۲۳ شهریور پس از برخاستن از فرودگاه مشهد به مقصد کرمانشاه، با ترکیدگی لاستیک مواجه شد و با گزارش آسیب به موتور، مجبور شد به فرودگاه مشهد بازگردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78394" target="_blank">📅 17:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78393">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rH-aoiMTGaG6D7GaTZxM9k1O4NS9qyYKH7GM53LAjEWejrrwz2YtodM6S73sqAffl4SXJ0Skst5AQgecDycwo4rAKXx6qe2d72ObbhpO78EDUPIfZfQPI136wM2HsNDv-YZk636KYR5-LhFGd9n0eU9Qf8HS9s_BdkNuUQTAnAetC8gMcEuniUIkJieoFRDEnl7tpuCuasvHHGht60yyooRB7I4WiW46YIzS8HbYIXqFo16fjzKVTTzO9H-kwjAYxMlEctbwAOk8YdPl5ze7opPurDjCz4xCksgF6RMj5wVoxIo1RY1R6cl_Ep2OIoElOGnISHoi_Gd7eG1fuOZO0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر رئیسیان، وکیل دادگستری روز سه‌شنبه ۲۴ شهریورماه با انتشار پیامی در اکس، از تشکیل پرونده کیفری برای رضا درمیشیان، کارگردان سینما و تئاتر ایران خبر داد.
به گفته رئیسیان، سپاه با شکایت از رضا درمیشیان  به اتهام تبلیغ علیه نظام پرونده قضایی تشکیل داده رسیدگی به شکایت از او در شعبه هفتم دادگاه انقلاب تهران در جریان  است.»
رئیسیان با اعلام این خبر گفت در دادسرا برای رضا درمیشیان قرار جلب صادر شده و سپاه پاسداران به عنوان شاکی، تقاضای توقیف اموال او را کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78393" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78392">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyEU17Ox04A81t9LpdfcgkoWeKn2VAhMsF_xHi-aYfBfGsxZkp8YlzANLxPsCrusq5fQb2viYSH6ZzI0JRILAr8tLU0b88G7Xd_6JXcnROhNZq9AgfZHj5VXcIvxavF5AAVfE2WctdROS9lcfpW2uDb5pGDLiXwMtEiPo7q6s5qA6VMM3RQTI9DjL_EI7_3m0VbqheMB9iHBuxTE120-VcVo822OcxQWy9o--GtNPAVlZB4r89XfvBAJAn1jdEBmrWoTSmISnaAJ3QjnuMNAgxZO3Sw1WrV8O9RbsXPcjJHyW290P0c5dSSGsdvtiTrwZ8EVoq1VIfu3hA4FZT1Bxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استودیوی «کارگاه» با انتشار عکسی از آزادی «آریا کسایی»، طراح گرافیک و یکی از بنیان‌گذاران این استودیو، پس از نزدیک به دوماه بازداشت خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/78392" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78391">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SdC0-0jLq7gbSEYeExWbFAX1v-iKM4fajVpAfiNFjRLFx19UbwCbFyRXWlvt9msdDbsHaRbz39DOm8TKgjHWaOXM14jmGw20wP7OE_jZ0XDHvkF2y-RQTzl30UbhefFzTAl2aiBseyTH1iBNx2Ow6513TIHzIYvjb54FsZAyPvvcxQQn-IbvKqjGFLr9fJkFJzFHwwKBqZyB5NAK9EbAQZ81sDxU_bzh_c75hg7fB27J-MkRSEihaf1tL6XNegBfsWLMWdNvQfhcS-I9g06bZBvCGVV6_u-1Or1lHfB57Qjrlv5Bh-hBGjY2Jp0VrlG0uIf6JaFxq24rTIFfX8az1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس تهران می‌گوید فردی را بازداشت کرده است که شامگاه دوشنبه ۲۳ شهریور به سمت «جمعیت حاضر» در میدان پونک تهران سه کوکتل مولوتوف پرتاب کرده بود.
میدان پونک از جمله میدان‌های تهران است که از زمان آغاز جنگ ۴۰ روزه تجمعات شبانهٔ حکومتی در آن برگزار می‌شود.
بر اساس بیانیه‌ای که فرماندهی نیروی انتظامی تهران منتشر کرده، «این فرد حوالی ساعت ۲۱:۳۰ از بالای ساختمانی به سمت جمعیت سه کوکتل مولوتوف پرتاب کرده و پس از آن گریخته است».
در این بیانیه ادعا شده که این فرد «قصد خروج غیرقانونی از مرزهای غربی کشور داشته اما ماموران با شلیک گلوله از ناحیه پای راست او را دستگیر و به بیمارستان منتقل کردند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/78391" target="_blank">📅 15:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78390">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bKQ1Bc6kNlwVy9C6T6kKtpeUA7gqzqUK933BArbtyrgFktL-DDHpkwe2dWdV_YVpQNLeDQ1EUx9LJTQpzQ35VKM-YPaYWmNPD2z2d3JP6isR2TcNwjguTdIIr698bKJ3KPvBjHCo2tNsNvwOP5mM_yTDnUHJs_FzJdOFmtsKMQnG0PdcvwdujIynElxl9ZzmgeXuWnft_rmLt9BDUGFtdzobbtPT0wsfT1tlkuUwWaDZ7XoLH0ZMNQz10assMfYAZ0bZRpC2llyrEUxp7ujQIwdfEcsS5R7g_XWb9aK5DArSgqmBjAYoZtyERjKUnfvG49drkvzY6F-8IcXbPuFVmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/78390" target="_blank">📅 15:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78389">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJ1SSIknxkTeYIuR1CuRgAcerZIPY9IZs0bVtSi7Dn5Ibw3pP2vbc6FimAF7puJCasE51VKYGzjOCUbPGdrtlwHrWDIhG1ZzhhSsEguJEAcOscsCEObWn0GiSEAtILIoeShyqNNMKgdWM1dGfWkOidlMPK4ZiB4XmpLhJtDl4E2QFUoLHqz3-yhDjj5CqPZO-BSw4FllINo-HmSG4hWGqaBmd0C4TokvpYGRZu0Sm0XEWrHpPpipNh3DFZ424-TfDwpyXCxmDqORf-AxB-UtGMz0Zl3ZO2I6cfHceOPkAs5-ppdPiCIGVtoDAubLTEStpBmsuEnfUQfqWEydoQEgvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پروژه امنیتی با نام «علاج» با انتشار اطلاعات شخصی شماری از ایرانیان خارج از کشور، از شهروندان خواسته است افراد بیشتری را شناسایی و به این سامانه گزارش کنند. صداوسیمای جمهوری اسلامی نیز به تبلیغ این پروژه پرداخته؛ پروژه‌ای که مشخص نیست چه نهاد امنیتی یا حکومتی آن را اداره می‌کند و اطلاعات هویتی منتشرشده در آن از چه طریقی به دست آمده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/78389" target="_blank">📅 15:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78383">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RVClgxR1pXDhGoBsHjWRK9l--hdVB_Kq1OtOrFlg6kklMjuPI8FdtXspvR72yjHnU8mGjwv7HXqgHUgOFNFGo_nL6s-B3TYBAa-bvSbMXy4msG4hM9Y3KJ9hLfWzlOjCfsk8k0c8-0C05DLl3o3PMt8e7DyLNdwmkfuAVL8mwYd0NkQBBEOM-l6xhGsaAqNk3IfKE0PAmaAVXjLq_HCumfhIbyKjcy0pUO1JU82ke1jzHDUCC96Ht6YVx0ikvyCbDmOdBW8Cce0XZnWnsKBZ1Jg2eBXPf1VKKUe230ExZu8aQ5GwNkykePdyHwEfp5vf1BNBAPkOcFoYCSpv9mHU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d1zmPT4VgEOXicJDvgcUOFqAjLGu4bvfIW1paxi8Ck53VNU_lQj2xf3w00rqb_mbMKo1DT8sV-_ur6F0zgx0tjb1Ml8eXezy_A1msvR6Vc9PEUbB12SHnIeZG02Ckkpsb9uLEfBEJSuvCVSTrDxO-m-0VYpt1XMZFFybPe5zf6QtkVvwhG1Z6-tHnYOMWVnTWyagEXFvtXu4ZQ_rr2d-aVpdSmQWdnCcUGMlOrU85Ou8YWo6-HViMi1LzjhyGt-hpGwUX4mKW-YGNFfRsp7f1xDjdt8MDj2rt35F_Ve94miJodVrT4GytH8m545w0fwVALfOmwTa6EsRp1gtwFh-7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HXFqXme2PJOhqo6w_lwrYS4WC0VsDIXzsVqNsLxIAo1QaeqKfg52m-p8UvgpkDEifKr6C59sbWXdObKv7sf02TD6hKfROuQ1t9DYLtUB0Qp4o1HBoi22tQ2zs5mknyjCBMV44x-88EIaK4HbirjVdbt6guyKU9Tf3Riz-HLEX2zl3eNgzSDqUe4UycifFJpbs00WJoOPL3f9Tx9E9OaYuTFBJRgYpLDkk4AdWhSJIGkWRo055vTK-Q0kV2BiWLgZZUXJXrwqBz_SgInEhyu2p6dAjp68WAERciv8ocYsC_YCoUbJTqXc9CoXH6Ajr3bMKHT4L0DGUaxKLU-P9RjVcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LpmOmulE3lDagiZWJNm4mLiGp_FYY1D6rIQTV5VrHFLO8LgbqF-vPIXt8F3G_CsQ95qx4H-8fxVEa1lB6msBoVusvzJQAatACuzZHKHo9QUb5WO5WxKd1jjmyO7Otuxvmau-r9wLQ4nwU5tZpMIKDX72xPxJC50qZE2k83Kpn4NB1GRFGAbNyJGiIMKgRDlCIumkSFt1GQ2DT2arfPzVHkKXHHxYiYqUL0m2SPoophbOSdd8F_Fe28IwR45_pZaCn6Hgmu68-uXgnJyHvNnRxzVokJITDwIhLCGpV3caxb9lFjPf004WEpt7kcB7v4GRRV74Q057XKVClzoP1ZnnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uB5oxP5DDv0YOV_oWVijowoSaggyBl3Djq7aEC_tMDoYwKy-1sn5qT0qdoicY7KvJP18XdNyYwvIWbLXn6VtTQe0rJrZlen2BUC6n6d8lnb3iI-Qg_RMe4jzOvx9IWEhBs-hRsLmV1rb5VEHmzKI8Lqnw28DUAS0yuU7W5PoPmo4sAYb3apw918E09rl0qFffPOcQBDImwAdsRbXTL7n-Y2mHmjvz85_3ETg2j_ZtJtdtb484nraV70bjtFiE8JXlSyseVZFnD7cCzzLw32p66ct2wPhhTOL2fAo2Zlpmlhc-tzMuwxEd6JP1pVV0vhrQXliHgw9MqukQ_58phC7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aS8gdPRgfwVgHxfPUUAbw7BCrnxg6SVFga1Hpb_P_lMb6qAf7us0c626igxvdYWkQ8rEvZ9h8PUGxMh6c9-DN1F_WxZ3v5r4fcXeYcmvM0kMB7eVFsRRmaS0V8rkf44qEHJlEGXbxyrPq1vSFxE-ki-BlGRtcddO253ZI83aYTfLQnnURISMA9yQpItRhBVp4IOyZNCjM8RuExbHChACzBMQOCcmglgvBu6bpS6ru9xKsB5hxvSlcqG-8r_rdh739iK3kUyAaUzrdiFfV9Fz9Tk66CYpa2WfS7em0WCqOZjqRBXWQsn59x6gAD2T1VcvMq7uyw6mD0N8ucppUZSGtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«پویش جان‌فدا»، کارزاری وابسته به نهادهای تبلیغاتی سپاه پاسداران، ارسال پیامک برای ثبت‌نام شهروندان در دوره‌های «آموزش نظامی و امدادی» و سازماندهی آن‌ها در قالب «گردان‌های مردمی» را آغاز کرده است.
در پیامکی که برای شماری از شهروندان ارسال شده از مخاطبان خواسته شده از ساعت ۱۷ سه‌شنبه ۲۴شهریور برای شرکت در «دوره‌های آموزش نظامی و امدادی یگان‌های مردمی جان‌فدا» ثبت‌نام کنند.
پویش «جان‌فدا» از ۸فروردین۱۴۰۵ با محوریت «قرارگاه فرهنگی و اجتماعی قرب بقیه‌الله»، از نهادهای وابسته به سپاه پاسداران، راه‌اندازی شد. سامانه‌های اینترنتی، پیامکی، تلفنی و ثبت‌نام حضوری برای جذب افراد بالای ۱۲ سال در این پویش در نظر گرفته شده بود.
@
VahidHeadline
دیروز کلی پیام دریافت کرده بودم از شهروندانی که می‌گفتند در این پویش ثبت‌نام نکرده‌اند ولی اون پیامک براشون ارسال شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/78383" target="_blank">📅 15:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78382">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daGvOoWNmlMMNeWzzB2xkoTbcdIf3C5xmr1F3dJUqriKUq8u_32dwN8ktSMMdJGjovr1pqaw6rUxxeyVRw0k3uXyWz2nrvecfbPEwb20r6zgjbdOORFxFofLgMv9nUcpdBatViS-F8Tq9XBz_A6RsHo-RYc9a6pjHqwiO_6EUC9CYOPucw5mwSHgtwHnw_NmGHKlZBHac3nsAZjwUWLoOnk_VPiWlgV7f3nrwOEJZ4KySPaXyi_1Q9Ti8eh3u4QodtAm-6I2UeFSselUniPbqHPMEZ061xTnhzOJOfnnHCWk4PmrzdbhtJff2VTiUtMe2DCZZJVmdy5jXMTBUkgl6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/78382" target="_blank">📅 15:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78381">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siuKVLB437dkpLzbRCRaMPY7IIRr9ZwBWIAYWF0jWdGeeagz8c7C6Mw-qzALmNV63i1iGBAp1H8d6jDai--iiIVfgvaqPYA6qKhAH30VaXFESx69mAX7Ft8wS4lErGSY7U8LtflExhgWk3a7bTg7Ora2mgN-MQnK2owtVRNxOLqwFfM3enn55reSs_XBX81cWwZUtAoIN7BZpbiPbidO6crb-WE1fjkBHvmntOU1T6eIgC4_IVAIhQFCucUGQxOUuMuwtxPsosJiT0vPtyY3zammSJzMZ-BmaK5eoQZ9ckf2m8JcT_VcgwC_PfhzKQfNyxlajGdP_9T0AH9k4pqcyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه اتریش اعلام کرد برای سفر محمد اسلامی، رئیس سازمان انرژی اتمی جمهوری اسلامی، درخواست معافیت از ممنوعیت سفر سازمان ملل داده بود، اما درخواست رد شد.
بنابر اعلام این وزارتخانه، رئیس شورای امنیت سازمان ملل به وین اطلاع داد که درخواست به دلیل نبود اجماع رد شده است.
وزارت امور خارجه اتریش افزود با توجه به تعهدات بین‌المللی این کشور، ورود اسلامی امکان‌پذیر نیست.
اسلامی در راه وین برای شرکت در کنفرانس عمومی سالانه آژانس بین‌المللی انرژی اتمی بود که اجازه حضور پیدا نکرد. او از سال ۲۰۲۱ در همه کنفرانس‌های عمومی آژانس شرکت کرده بود.
ممنوعیت سفر از سازوکار «اسنپ‌بک» ناشی می‌شود که تحریم‌های سازمان ملل علیه جمهوری اسلامی را بازگرداند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/78381" target="_blank">📅 15:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78380">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Aee150LCMa-By1HmDE3GHyPQVwhB8vjnxmSB8Fw2H7lUaGXZrkmZnLbGDi6xV_NuHQjjPheTmHzKsiq3xYeOAfl5pkZ7EjW37YDw3Dcedf7Zsg2LTD3grvTGSP0AuldTIQstS1Oo7A9jTL6EOShvIxfHoTCl3-Xy1kgoAxMDIIElc3QQlZMmVzspaYmziwdZo_30hMQBnz38HMbe-mtixsYiS0FWwOiap1vzZw3IR7f9kyWHBVBFdEtcCUs20lJStLs-QI1wif4oisZokK4PpaAjFG_sQ9fig4mJ5Cvh-U-_zV8TMHrNvUvTSMZ8aSitr6zZYc5S5K20axZFoWHKbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/78380" target="_blank">📅 15:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78379">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pvY4XSWldj7f72DTzSWanoTes2ueK8ZCfdkIRNP32lkgDzv6mVIu2sn6eSV6bI_he81nMzU_CzD4cZ8dz0_CZRiOQLxMr7ATY8aXOSy2vAKMrx0bSnkgMzyPDvlo9hJZn5E-0ZBFfohqtcv6W6TpI0yzS2Cs9aP7pQm3HAigl-2JrNodwb_VstupJSYUL2XK3dC0Li2Pw2-N5nwly7zOwPgvRaNNmjkNxoq5W4n01WVly4lV4pSGNB6MOVGO41_uV9K-Zzxn7encHnks7gE6T52sqm9VIEfGMtFbbz-Y29nhN6QOQsTwxJmYj-ANnN67bU06-bpgjPMRmo1Tkhrm7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست‌کم ۱۰۰ معترض در ۱۳ استان ایران در خطر اعدام هستند
سازمان "حقوق بشر ایران" اعلام کرد دست‌کم ۱۰۰ نفر از بازداشت‌شدگان اعتراضات دی‌ماه در ۱۳ استان ایران با حکم اعدام روبه‌رو هستند؛ بیشترین شمار این افراد با ۴۶ نفر مربوط به استان اصفهان است.
بر اساس فهرست منتشرشده، پس از اصفهان، ۲۲ نفر در استان‌های تهران و البرز قرار دارند.
همچنین ۱۰ نفر در فارس، هفت نفر در خراسان رضوی، پنج نفر در مرکزی، سه نفر در یزد و دو نفر در سمنان در این فهرست ثبت شده‌اند. در استان‌های خراسان شمالی، گیلان، اردبیل، ایلام و قزوین نیز هر کدام یک نفر با حکم اعدام روبه‌رو است.
این سازمان می‌گوید فهرست منتشرشده تنها شامل معترضانی است که دست‌کم در مرحله بدوی حکم اعدام دریافت کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78379" target="_blank">📅 15:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78378">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TYzWu4Dx_E3uqjKMoaWoEmN9KE0JyrRDkiSifbdXXnamS6X4cacjjLJBZK_Ir9GODWLNbeEl6DnPwXvCtq4qOkJnMxKA9EempYGUHYTCpWaWUvkbNTAtCi2TrX5o9YphzUdrOGaInKrcxve7wgWewwf9-i8mSSm8Ff_wFoFrd0GN7HsfdFewfp2-Us-6Pfw75bIxutnSNqWBu2YDJPJ02RCxc4LXx9VibwzNBXM8dV_AQ5Hb5O0mLtYjtdz8K2IMtqHTQz8WsNkACst50KTjyOh4Tv5G0_hPT_l2f71FsvB4eCfakGiUFT741JRi4Xk8vPqP67qc9s2sNzTpcANOgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78378" target="_blank">📅 03:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78377">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gW-ajtggEoCrqRjzESd_Xe_epNB4eIKwjaZxwFyArSyF4soC1vUjOQWWFaWcNFxiQTjzA9dZ7U-290JTYRiXtzL_xtEN3hJMrQvJrQ4g4JumD5k8dN-OAmJT2CHRiTwQynlv32ogHrsmXJicBVJbBvDacX_afEeRUaWEbhwpgNWiy9XRi_NKC0oAv5LE91gRwiQ5JBBRr_YjxAZYW8yzqVhd1FtrNceZR9RBOTPOQ8RM8DiT-wqg2QnwqdXf0atq7lneBimg64tss1kV_Q-Tcg7lYcpqKW6fjFRYqptUu_7JF2W7c0nTSGvualHzr8WXN8u36LGqx1B4LYhTKCgzdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78377" target="_blank">📅 23:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78375">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hs2agcmW5QmFnhb8cX44w_8CHdDebEkJglYYJnHZjsbbDaZibwUaZ3o3ZSJgjw9LarWnfsFZagcTIRsfv258VEPO4VqkKYmkaRo8mdQkWrC5-R7kJx5S6AH8z2Mzr3lHNO6-liTq-RQ1Ud3Hz9q8mxT3AAFK977xhBdphWbYUxjjpFV5k2ZUKR7ydaK3gkAWJdJbOxkzZxLMVDXdhzE4fiUwY8nbuSptD3fviBW3WxfEe6rlNOyKKyOyxBTHSetjuTm_k-HuYgt2URHJqppsHsERcLa-AdLDLjvwOBnUFAxlRfYfX4_6iw8yH38ZB29Istsfbd1RsJNU-zCiNvuKCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PcVl6z-ZvFTr1PY4W5NGaivxBH72CCy3CmCe3MyeTdcWkcTefiM1n0RkjQeOy65fNCDzhLTaWmt1yL4DgewccSaCq1QWFHggY0CxqeU4rmdhPdVoX8kttMpGushG2VVSZDKFAzI_U7ENAZDBRWh47ckL_0hYAtyuOGjbQ6TfuMziGmffmKegTmVlzurvBFRS44IHo9peeJXBMGU7w38KcJIAJWOkFIZZngam1yNdw8iyOYzVZ2mY7vMGK59fXc3LxkNS875reyEsg7FidcovGEqX5RHHsmH0Ynh9MiNFLO4xms6Twx511Zi6K4s0aF0uFfLA352i9ViGRGRUrqT6Pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78375" target="_blank">📅 23:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78374">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qoHWDqWeyOeh0yDFY6GavGRkFcCFh6INPwT3lXTIVt_joKcaBIwwL5RfDpk-yy51jMLd9d5Ei3x7lSsJadpoF8TJuzwd6aNyFWcmnHyjPIkIetDxAFFI53fUOu-eNXxGzvLp8576zTLtSjQqeZQqaMjk6GgFkI3Slu1cMxuGDg6zltVa_SzThSlTBOqhTYMpTtXVABiW8OFu9Cd_dJdp7ozQZODuVjfw4QpCePd5r-CloywufdXaDARbqK_um051m5BxIBLCU3csujXdMmm9aIQ_Tuk3Qk0tdPEJ5GniWhuXGJs0DJJpCY7uZhVFUA2yMqfGZcmWsFE3khm_R3g4EQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78374" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78372">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=UEZ-F6Eu6t6fHBkBEBQL2txlyFm2u4VFYHTQyi4kW82HDS82eWSrC819PdWtM55mtW1o1g1Bp6TO78CXdmVDHVixKbsojIJo5_mW6-yKVez3HtLDEbXuuIqyZW0HV2huuzZSGDm_eBYaCaKfcJBBWal-0wEAONjnDnrECwp-8UZpAlCky-blNJdo7xx0F2HYOWjdcoDtBAX3nypAuSDclBhpVRHB-0OiVALimJWrkrmCXflsR90m1s4COtl31H7FWN-zYhPh8jPOV_GMySsbBLfdbRjF30rRBM7t5Cf4BiZYVedWPJBKogRlwX__e-tRruIcyJ0QkWS6mA_5sTQ40Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=UEZ-F6Eu6t6fHBkBEBQL2txlyFm2u4VFYHTQyi4kW82HDS82eWSrC819PdWtM55mtW1o1g1Bp6TO78CXdmVDHVixKbsojIJo5_mW6-yKVez3HtLDEbXuuIqyZW0HV2huuzZSGDm_eBYaCaKfcJBBWal-0wEAONjnDnrECwp-8UZpAlCky-blNJdo7xx0F2HYOWjdcoDtBAX3nypAuSDclBhpVRHB-0OiVALimJWrkrmCXflsR90m1s4COtl31H7FWN-zYhPh8jPOV_GMySsbBLfdbRjF30rRBM7t5Cf4BiZYVedWPJBKogRlwX__e-tRruIcyJ0QkWS6mA_5sTQ40Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78372" target="_blank">📅 18:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78371">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشگاه تهران - دانشجو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGwSzFysw_BVvEyBahnMW15nH1kj4hn5XAyzGZe3FkWL7teCuEMoW7G78eYeMTfNhP8P6-fLAIWu5kcZzbeT6rfgRaAy07tTDJgsOARBsxM0M0JubSW7YprCN45RAzrg3UC2pEyDeuVNg27pl5TY-mC2KUD8rswAroA7preoZHUmaw_iXauYSzolBWIpIqvPaX1UkXy7YbEKCRyPibZUiA2C_MriSRlwvkTrT80e0QH0tmVco1UXM5OI3S1_6ZA3jeBPmDl75QZGBqc652uFadTlQOWV4AhESgITVzZB_h-V2-qzwxobd7l4mlIHski8lD_wVEA5dLTTL4YCjyiYXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78371" target="_blank">📅 17:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78370">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=Oyj6eQrXgTk1s1q6mD4Kq_hRPbxVZghdAjEiJ3HQUICz2voYlSYUCzFR0FPnBDoZXiCLg1FQnV4rf3lasp_R0UUR0IqNJyKbRh4pfoIxGzswfTvYbJ6SBzoi9vou15Lql-bhVLDZAPpBY1Xoa55-WPnxsnQXSPdoDP2dawzG1fP2PRznUu91IgXd-QQ8u-ETqHEaXZ4nzC-uWcBnF8Q3-OQ-O1GZnld5OI-nBdtc39lEKAA4f6ZsTdF1kzYKdy_XtOyHQ8XpQh2fRJNBlkGmr_-ZJVj9HOnN2GxSolEfN2MkRMqN68QQYWi435eyC1_nwC8V6DCUonVM0VxRjwjXsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=Oyj6eQrXgTk1s1q6mD4Kq_hRPbxVZghdAjEiJ3HQUICz2voYlSYUCzFR0FPnBDoZXiCLg1FQnV4rf3lasp_R0UUR0IqNJyKbRh4pfoIxGzswfTvYbJ6SBzoi9vou15Lql-bhVLDZAPpBY1Xoa55-WPnxsnQXSPdoDP2dawzG1fP2PRznUu91IgXd-QQ8u-ETqHEaXZ4nzC-uWcBnF8Q3-OQ-O1GZnld5OI-nBdtc39lEKAA4f6ZsTdF1kzYKdy_XtOyHQ8XpQh2fRJNBlkGmr_-ZJVj9HOnN2GxSolEfN2MkRMqN68QQYWi435eyC1_nwC8V6DCUonVM0VxRjwjXsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفحه اینستاگرام رستوران «دستپخت بی بی» در تهران، به دلیل انتشار یک استوری با نوشته «هیچی کتلت بی بی نمیشه» به همراه موسیقی متن «بی بی گل» از معین، به اتهام «انتشار محتوای مجرمانه»، با دستور قضایی مسدود شد.
پیش‌تر نیز در سال ۱۴۰۱ نواب ابراهیمی، آشپز، در پی انتشار دستور پخت کتلت در اینستاگرام خود همزمان با سالگرد کشته شدن قاسم سلیمانی، بازداشت شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78370" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78368">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JpaheruHRqzGVHvdEgx88ZmgVGP5ZqafjtdS6IbnzLV3mBgzfkCF-7q_SBzLppID1WameHo5Qy2aBIgq_Bmn0iptdCRd-oJkdIRtdXS9w_bI4IPek74-aa12FK3k0lWpmRD4BwUMMN3Z9rkWJo8ARbHFZ4lsMYk18PAiE-BJDo27_Q7ZdE6NL96YGe6PGWL7R0qEvAAENE1sOrFieVC_z3kNfT9GiMdiFzRakZmfhkYma5hy0inFQNuhgrPdPX_Lz0So8iWU4fATwHxJU-iLNe0G3nYmw0Z11POOl2eKEYh40Ls2IxyjYQYGFwfXrU6TZMVF1PBqK_NoxLVmLDdzpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OJCGU_LR_9JtEoDubeBuYuhTuDy9qOBWatZaKPzT8fFExFYfS-FBbVSEaWmi9J6oCQ6glZldkndCBq4FrS6BsUPtBhfl_Zizn_8h-345IPg3fhmSslSGSpEFZ9HcHdh_KvVUwGruTkVWMPiq2dExW8ZQ3FXYsYTlb5EdtwxAo0uHJoI1WJsqCAM2twtKM-_xPNqt51Ym1p60GRR4DbNhqSsmuYTDO0MRW9FITjKLala7pgruHz-Ee0rSWMTA8W0iRqiHU6_o92L_BWhN_2Op_I7bckt6wROEmwfvC6pkuGfhueX9X3Tqy0u8JcF0EB27Z1sbz8DBuC57rM4e_hEzYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/78368" target="_blank">📅 16:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78367">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szbPc8xo-Fk8CcAAwJ9_QZNlCgLcSzWGIo1FBFj7vXf2k8tf6ma0S_UFXj4oRei5xAdGU8CiuOJsAA1atb2QbKml8T6esw2AbS7K5bG-O5VlV0u8ceMUFXWE7X33DckAshJZr_eX7tAYKWe2RP_tsTpZXo_tuogsAGkLwI4y6wuHMEuEWnGAPfr4RCOI6DJ6KGGJWElUgK3tE0XsBZdN2p1yHa9MA5-vwjMTlZcjEy3IxXkUIQXRoxH1X2CyPc06eRyTQBjSRcF4-o74rxI8qeuY7X5g7BartpONQhWf25dXTEiWfGE55lilT7ow-uc-6eQ99Lg9ZSPsRdn-Bos8cQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78367" target="_blank">📅 16:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78365">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G343oGk2c_jC37j0vobi8pEdkUFOHGrn3Igmet517WYszNTLBj5zxVHpOY_mfp9zfWNld8HT88bA4vMREmsFCZv3Ga4HyvXqUbS5MQY4AJaubASmve32cdNrmulG0A2QUKU8JDSL4FZprH-3-s59mITU7u08_cZugUujYgd9qlzDoSpv4oZxLCmK52XbN-xGu39t_RixKxY5qT_3UUX-5CSdq_L_aoX6Ocwngr9v9ZRWODC5xd7EPAFFtDzhcQovw6zcfqpOlX7yYjJFd0e3NP_KnVJsWwUOSVWrtCo0X21O-Tq6XTRQui_M8sYLNACV_h22pz0A19aEyjfJG7MeRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g9pYPYfj_-Gtf_DBB855QLtjixJyvbyZNH1Dj_A-8i3F5rJgKs-OSKDzgwb_KKL0zp0TRZHo4XX-Hcrg4GxRfVK_SDEVNCtz8lESIYPW1CWw50wUz10ZVI9mtL3LXOnq2CMVReLZQigzHuNAYx_d6tc_Ajkre56vN89RWMvqKwAFeA3OuJDVs8Q1YIVLMVfxcMtuZgKjSvL5Guz9vVUIC7NrnaGC_tt8zlfV549xrcby2GIu_joJAk_Q5UZZbEfZu2hm4Wo-ojP_huY9v4WuDYR2DkO8frs9g_D9tcmrkiX9WAb__p3lHe8sXcDr1_X4UL3E5VtmMaUUPDu68CfzHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/78365" target="_blank">📅 16:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78364">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LlPivDV6bZf6Kgv5SXdZDS_DcJoOcrz9JZR1ot9Xywn_oLx0wP5X0-BGuutcUMGPWrOZnlynUjJIDPhnEfZC-QK_PR5oleIJ5slBH_hNMXToqv9QkK31W6zgWQes19SWRyGy100DBb5L6rU4zrCn684Gqe9e7mZnkdEdXsnYzEHnXgtsDZh-NlbAXd9UTu8Jqi7wuP6uD-pLpOlbwdDRhLWyVYf9-m0qNhQJCPAi9LFn_1DWNKjTUcXmD27kH5QAyvUZrdiPNs7VhzzxEkyOeL6YLdnIbmTvGcnFy_HyK8PRQ3faNc18kEK75BT-k2nUCPvEKfGwHjs6-BueXNCsxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78364" target="_blank">📅 16:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78362">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=BWPXmwgy7W8Le30vzDNUvoo2FzE8grTuZh9YbauChe9uuIndN6pPgp7_kSXT_sqlLMS8UhKUfHGqUk7WWn5z9-nbeFjpLt7cjsSLG3eoG-H8KC-diDeMI_JOzyt9nB7sp3niNbESrKSYEPIOQ2xuoyVl0x69hZbXY5hVpAYNCntzzu3x0SsaDooudDl2d_sFQpKRqo3zze9RET3EvbWQPzpaG-9Tu_KVWF2hTohL6YE4PAqSaK1F93rTynQSNcC21PhYP_J-Ir0GCCdWaroBrb16yBoTJC8z1OCKn4Sr9e5Hkue1QMDzbfn74v2ldi-yOQREMPIJkP2wKEJYtjEPnA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=BWPXmwgy7W8Le30vzDNUvoo2FzE8grTuZh9YbauChe9uuIndN6pPgp7_kSXT_sqlLMS8UhKUfHGqUk7WWn5z9-nbeFjpLt7cjsSLG3eoG-H8KC-diDeMI_JOzyt9nB7sp3niNbESrKSYEPIOQ2xuoyVl0x69hZbXY5hVpAYNCntzzu3x0SsaDooudDl2d_sFQpKRqo3zze9RET3EvbWQPzpaG-9Tu_KVWF2hTohL6YE4PAqSaK1F93rTynQSNcC21PhYP_J-Ir0GCCdWaroBrb16yBoTJC8z1OCKn4Sr9e5Hkue1QMDzbfn74v2ldi-yOQREMPIJkP2wKEJYtjEPnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/78362" target="_blank">📅 08:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78361">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ezqaDM8scQotP7fmaYe9jyxDXrQjVWLKM3v93Cjz0dFe2fEgAHUY_uIeWkXflmdBiVwIu-UbtnfC9WXT2Il0g87jSAFSwPI8mqde-bTS5puzmsfkN7GeXcq3LQDleiZDJQsds0o5uxxSBIYl_tUdkk5xp4aeZtuYavBDS5g3Cr1sw-9X2L9SvNc-moNrkatfpfsvwbEapK3g_J1nmgiy7JnJ_QDoVh6QhyKfNkxQU5VNr8YsCoI38b8lAczqx6oH3jc5C0bvPCPtHDHEA4EvgD4RNyriaLoW8AKz_qHEXAssrz6H8aHD3kirxFvr0LYWbdqkBOlDldKl71sDdrWJgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78361" target="_blank">📅 22:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78360">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6Nco5PpMXXCxKCaGZSrxtNj9DkxiVcfjxcgtyaaPw6f3TpCZqgeA3g360BknP0CeVhAwjLULJ47Pd2keIR88ZaL-KUaTSugBqtKdP0cAwE9YDC8DgQl_UqmSDnYgHcgEkM4Hz7aZqyE-OKUiaU8FpJ2h6eVTcl9mKG0HNWt5yPwtNrFLG-SEiyyBC0NYh144MTjYJFjdKuzJqlmm1AKTPOhiT4NZKAJKtmhdFDhQBvWfi2IwwUJ3s49A-V6Jmbi6IsiMz1z16O9Ua0Riwwlw7F1rigpfk6d_5bMecd9Kta-cQytyghTJCgvPUhUp8Z_AY10GC3A52BSEWA-KAwGTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه نیویورک تایمز روز یکشنبه ۲۲ شهریور ماه در گزارشی به نقل از چند مقام ایرانی نوشت، مسعود پزشکیان، پس از حمله نیروهای سپاه پاسداران به سه کشتی تجاری در تنگه هرمز در اوایل تیرماه گذشته، به‌شدت خشمگین شده و این اقدام را «بی‌پروایانه و غیرمسئولانه» خوانده است.
این حمله‌ها که منجر به آتش‌سوزی یک نفت‌کش حامل گاز مایع قطر و آسیب به شناورهای دیگر شد، درست زمانی رخ داد که ایران به توافقی با ایالات متحده برای پایان دادن به درگیری‌ها نزدیک شده بود.
بر اساس این گزارش که فرناز فصیحی به نقل از مقامات ایرانی نوشته است، پزشکیان پس از آگاهی از این ماجرا با احمد وحیدی، فرمانده کل سپاه پاسداران، تماس گرفته و با لحنی تند خواستار پاسخگویی شده است. با این حال، وحیدی ضمن سلب مسئولیت و ابراز بی‌اطلاعی، به رئیس‌جمهوری اعلام کرده که نه مجوزی برای این اقدام صادر کرده و نه شورای عالی امنیت ملی از این عملیات مطلع بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78360" target="_blank">📅 22:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78358">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/930e263d13.mp4?token=utYgi4N_3K7dkQOyDguHd4S80k4Rpy7uCKgHJi7cyj5p5Uc4hoaG1wNdTA2IXCkIMH4nRjO5t6oUG4nlvHptxiO-oRBc8EB_hY8XmLJWGZW6s7ePDhpjv3RNcf9f75Wud-24OjD6VGE0Iu-oT9v14BmL0u_ao-QIeaDQJmLgcVK-jymGd9owDRjKTKz9LTMMM0KUY05gVbwx4N1RrkX-c2Fv9udNgh-dZOx0Gd-e1kEz28fl2OXk51s_k6G3KaBj6GjIraKQ5wxpnGoTU7RAQ1JPwFBd8dCCpSOAOc55TvQoiLHKMHe_LujOpi08J0Ez1rh96wDHZP4LYDyiRKP2jA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/930e263d13.mp4?token=utYgi4N_3K7dkQOyDguHd4S80k4Rpy7uCKgHJi7cyj5p5Uc4hoaG1wNdTA2IXCkIMH4nRjO5t6oUG4nlvHptxiO-oRBc8EB_hY8XmLJWGZW6s7ePDhpjv3RNcf9f75Wud-24OjD6VGE0Iu-oT9v14BmL0u_ao-QIeaDQJmLgcVK-jymGd9owDRjKTKz9LTMMM0KUY05gVbwx4N1RrkX-c2Fv9udNgh-dZOx0Gd-e1kEz28fl2OXk51s_k6G3KaBj6GjIraKQ5wxpnGoTU7RAQ1JPwFBd8dCCpSOAOc55TvQoiLHKMHe_LujOpi08J0Ez1rh96wDHZP4LYDyiRKP2jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز پیش، پس از اعلام نرخ سوم بنزین در ایران، تصاویری واقعی در شبکه‌های اجتماعی منتشر شده بود درباره اینکه بعضی از تلمبه‌ها در جایگاه‌های سوخت (پمپ بنزین) امکان نمایش همه ارقام بنزین ۱۰ هزارتومنی رو ندارند و مجبور شدند در ادامه نمایشگر یک صفر بچسبونند روی بدنه تلمبه.
حالا محمدباقر قالیباف، رئیس "مجلس شورای اسلامی" در «ایران»، اون انیمیشن رو پست کرده.
ولی درباره قیمت سوخت در یک کشور دیگه:
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78358" target="_blank">📅 21:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78357">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luhcLWFGowYu8JPUqGQXPODuPyvrxHHq-wjDj5qr7kN_ilcrTRUObW7ROEb9XBJKa7Qfpp2wFZGswbRuTbLymO9UUmJymNZtFlbIKhJG_IXUxfE3nSZrEWHfKau2-JEe0IrJC2ppyAc-zjcRDomL6ZmCPCB16_qkivQKvgt9ONr1MxOnUESWqhhBAHXfgsY6qPGvUmpP1KAHciZrqgSUBXrQ1tuEmPirWVONM2_CrXv78txiHTO1L93EQ84l584W_ZO3cOMfSo0tGD-c-qUC6WV_dVr8symXke6qLtmv4YDpIBOvBvM1x9STbars4PMjLmSgp0l5qWsqkY4v5kc5fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین رسولی‌نسب، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در شاندیز، به اتهام «محاربه» از سوی دادگاه انقلاب مشهد به اعدام محکوم شده است. او در حال حاضر در زندان وکیل‌آباد مشهد نگهداری می‌شود.
خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، روز یکشنبه ۲۲ شهریور ۱۴۰۵، گزارش داد حسین رسولی‌نسب به «محاربه از طریق مشارکت در تخریب اموال عمومی» و «اجتماع و تبانی علیه امنیت کشور» متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78357" target="_blank">📅 18:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78355">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/isFKOeSCjypPB73S6-TBd7XZRVN4ijBF0mtD2i3DS0NCBQZk_kxY9AHYQMekML0qgPBaJ28pVc8vCE8uPkAY3aaIa58NZulllHkSyOU5EQC7qaMhJxioRWTqBsDr_ln07GruzSgluxtrFdLyedeeZVU2mO4JDdLmPE9mSOPagTPc1W5HEtWBrWH3DHm36lSLuV4ByVYmgVeI5bHeOMdi4RETZVl-J01qG6ssZ1KWPBu0UqOJkLedBrVGen3ibb5yV1ocWjEk_zxVOB7Kfcp0Bxvvo7TG412XIOTHFgIx25ilhBZPR3tLY5y5OR7d1IhITONg2tBPeQKCqWp4yMhANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QE7fm2tP5hGKjbqUlGwmLLezCLLjkQRARq5pFkbgN3lsD_JWkryguRUu3Nrf92afMa-kURAa4RawgDQPSHvWFZYoxgS8tAbmfQT8lMaOVDw0P99_DpfOnwfibYdvZnd-_qu427Cj2Nf5mXs4oQ0HuvK8Pne9ZFSsm4SkzNvT8SD3IwKYONHFhPrQuxlCO483EaQb_cofQOmEo7wxasHzPX0xenYxMaoHQxqSB6tFaJfw-wa8NIZ4G_EKfP5aQbpd9CFWRyhd6Rr6ZU5xi1GqzmAyd--5ynnmpipuDdSBnJ0moODK1nwiR6oaRo8176KtPYnoSDVqvDkEFZXBM4gzCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان ثبت احوال: در کارت ملی‌های جدید از هوش مصنوعی و بلاکچین استفاده کرده‌ایم
quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78355" target="_blank">📅 18:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78354">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eV9SYXKd8d6pu2uFD14MPWPa02ZleQcfXLe9yg1hNTTGhyWqMFS2KQMylizEd5pogRMsipZdQE8Yyxq6YtomKX9QzovxsuzktkdSVdexoHG2PYPZtWqcZ_nHkno66ubVdlYOl_5oSLIEcGVBs58ghFNZfidIyNPzLNjIk_Y9uHQOfFa2lMKtdZ8APhbsn_hJUT-6M4oWo__DUCcmqVJDjzPXuMrZFyZwEI7eY69tGvuRiwvwdqwNbWGEyTLjrv2FOazLvpPDuv14EpX_ZaJG3_a4fdM9bTvXRmb3ZZg9qwN_us8Ra6rwdEjN1UlMLh4_bSOh_giaAeLBHrprHuVLFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز یکشنبه ۲۲ شهریور۱۴۰۵، گفت «موضوع ایران» ممکن است پیش از انتخابات میان‌دوره‌ای آمریکا پایان یابد، اما در هر صورت جنگ با ایران بلافاصله پس از این انتخابات تمام خواهد شد.
ترامپ در جریان سفر به ایرلند و در حاشیه مسابقات گلف اوپن ایرلند، درباره احتمال توافق با جمهوری اسلامی گفت ایران به‌شدت خواهان توافق است و به‌طور مداوم با آمریکا تماس می‌گیرد، اما واشنگتن تنها توافقی را می‌پذیرد که به گفته او «درست» و مطلوب باشد.
او همچنین در پاسخ به پرسشی درباره دیدار وزرای خارجه کشورهای خلیج فارس و دریای عمان با ایران گفت این موضوع برای آمریکا اهمیتی ندارد و تصمیم درباره دیدار با جمهوری اسلامی به خود این کشورها مربوط است.
قرار است این نشست روز دوشنبه در عمان برگزار شود. ایران می‌گوید یکی از موضوعات مورد گفت‌وگو در این نشست، مسیر جدید تردد در تنگه هرمز خواهد بود.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز بار دیگر گفته است شرط ایران برای بازگشایی تنگه هرمز، بازگشت آمریکا به تعهدات خود در تفاهم‌نامه اسلام‌آباد است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78354" target="_blank">📅 17:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78352">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gcc1MGAAdXhY7KFKnSeyUB3H5SotjIHkRGF1KcVUd3jkQbbE15heTWZdWU-w0XAM09HN3JjX-RjmGbFHdyEr6Dso5yhj41sZjcgye8q1eEi7DRRREgQm1ZDC7xSRIDuwMIJXTSGSx3tM7wRb1i1gx2XxAhFriYgED0SZtjC0-sWq-Vyofh5tuO3TBA74TYzzAO2C25Zlzxj3Gx46DxQQugCv3gPfcQMyDSjc31qSwuctvvsDqVR41YX98VwEaVq9iJZQ2ko2NoCHQScL-YWpE8jeBCUuVQHt31nN09d3PWP7PjIn6GsJRgQ6om2piZWgftI3WiSHMCsUhp7bwwj1LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WIM-55CtOP4VLnk9m-sM3CeOtNe0Y6BHupsM7bWIQduWgzCy8fEY_I31PlrSMz7fXG9sPAaGWscMIQbtCpzvwM0yXc2jOvLDrkYKmpZhu0BOGWo75AreXpgwrLjuKCMQXbqhoM8XvKXSVccGHI1lu0coDBgO7VWf66PA0GHmxSLd-zQNrbId1J8YdSD_dfz6d-sQi08ALL7yMUNMj3Fncc2L7dz4Q9Uut_HwLHDKtndtwzNPR0hv_Bsyr4qtMM3pM6FUai7kR1FpuOz2QiWzVJU2NPHrTM1dpW-O1wSm4DyRm22Je9iFwUS1p5m4nyNx095HMkNNi9bVzom_yhZAKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/78352" target="_blank">📅 15:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78351">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=fNghBii58WyjzPYWcRism7hqBdcTseiccnrdQimH-tvdyIP2C1qAGsPcrnwWkhuTnBlZuvFhGux3zEDZowj4ON0aI-jgz_qOgxiNd8PpQFJ5QTi5g3VE2P8cZzSWV-pVecGxVBVvVgrtEXPiC3BDnY-y-KEtU1EHc5cz7BiF913XvNcIyoUy8ewBfZYLtuPYGH7muRKjLkAMX5YV1YAUmoZWr1b-dDbJKwC77DUoeZkzSZEpmTOcYTEd7ex4PfGRUYzkTXAtdZwxbW9Bf7urAzPpnq_3kN_SdeKhPvgHDKWFrUAWbwDyCX7uckMGA-GXx7rXzTYAKpL6ihbLOWqhsoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=fNghBii58WyjzPYWcRism7hqBdcTseiccnrdQimH-tvdyIP2C1qAGsPcrnwWkhuTnBlZuvFhGux3zEDZowj4ON0aI-jgz_qOgxiNd8PpQFJ5QTi5g3VE2P8cZzSWV-pVecGxVBVvVgrtEXPiC3BDnY-y-KEtU1EHc5cz7BiF913XvNcIyoUy8ewBfZYLtuPYGH7muRKjLkAMX5YV1YAUmoZWr1b-dDbJKwC77DUoeZkzSZEpmTOcYTEd7ex4PfGRUYzkTXAtdZwxbW9Bf7urAzPpnq_3kN_SdeKhPvgHDKWFrUAWbwDyCX7uckMGA-GXx7rXzTYAKpL6ihbLOWqhsoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تور اجبارى اتاق شلاق براى "عبرت" متهمان
یکی از شهروندان با ارسال ویدیویی که مخفیانه از اتاق اجرای احکام شلاق ثبت کرده، مشاهدات و تجربه مستقیم خود را با بنیاد عبدالرحمن برومند در میان گذاشته است؛ روایتی که به‌زودی در قالب یک شهادت‌نامه تفصیلی منتشر خواهد شد.
او درباره انگیزه خود از انتشار این ویدیو پس از چند سال می‌گوید:
«آنچه در جریان بازداشت و صدور این حکم بر من گذشت، در برابر حجم بی‌پایان ظلم و بی‌عدالتی شاید اهمیتی نداشته باشد؛ آنچه برای من اهمیت دارد، تاباندن نور بر گوشه‌ای از این سازوکار مخوف است تا همگان ببینند مردم ایران برای داشتن یک زندگی معمولی با چه مجازات‌های تحقیرآمیزی روبرو می‌شوند.»
@
IranRights
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78351" target="_blank">📅 15:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78350">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=Qz2DDBNaZZijNBcmWXpUuwwWEFMgNbbJSc-B4eVffO0UjBqRp6j00jGWUvymtlNVCu85GX-mFHOXqBXRS0GhCkmXW9-7m_eYWXlUld1Qp7t0BMfI89uub25FOwJwdD91Og5tJIRTXLnwIXD895skQskqr3y8fD84ZMlmMB6_OmjvthYwX7hBNQKh36Ss2SOJLCZb2SYdVNDu0mR0NsZ8m9p3oojZmuoalkfBetQ0Izfgm8wLgnyAeRwH-VLbLuY4IXnU8qH2gz2h2oNf-3b3hbQitUOB1jxHLTGDzY9-Qn_KXwL846eWOlJIarxFXM3mbdaRT6GDwLyCjtpFZ3zYMA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=Qz2DDBNaZZijNBcmWXpUuwwWEFMgNbbJSc-B4eVffO0UjBqRp6j00jGWUvymtlNVCu85GX-mFHOXqBXRS0GhCkmXW9-7m_eYWXlUld1Qp7t0BMfI89uub25FOwJwdD91Og5tJIRTXLnwIXD895skQskqr3y8fD84ZMlmMB6_OmjvthYwX7hBNQKh36Ss2SOJLCZb2SYdVNDu0mR0NsZ8m9p3oojZmuoalkfBetQ0Izfgm8wLgnyAeRwH-VLbLuY4IXnU8qH2gz2h2oNf-3b3hbQitUOB1jxHLTGDzY9-Qn_KXwL846eWOlJIarxFXM3mbdaRT6GDwLyCjtpFZ3zYMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78350" target="_blank">📅 23:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78349">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pj5QDx0jKJNBIlkc_QU_2Z7PV9ImyL1NTYng-icLWysBNIe74Gp7MfWuRElLj3Uo-GUejxCWWg6c-Bfq6XdY6-543Us8Jy08ONMNtJTjroxBMf_9ycVZxdwQKrQUHxG4cBiDRf5UxugreOHndA7C9Oq3YrK5crVUusRugmmFi11mg1hv9HGS5ZIxo1s20BmE01Z4QVrpTAdodkKH1pmOmhCii_VLEms0lZjM8QDdFRWVVGTlMpN8VlZBW-WnQxAoCjKwYAXeJhAgrKkPMufLNzgtQetr6m0d5ORE_KbOQXWxaVsH2kI-tlcu32ObhvdSkkPhwySUFiBQDzuXB3c7Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واژگونی یک دستگاه اتوبوس حامل کارگران مجتمع مس سرچشمه، در صبح شنبه ۲۱ شهریور، یک کشته و ۳۸ مصدوم برجا گذاشت.
سید محسن مرتضوی، رییس مرکز فوریت‌های پزشکی رفسنجان، با تایید این خبر گفت ۳۸ مصدوم این حادثه برای دریافت خدمات درمانی به بیمارستان منتقل شده‌اند. به گفته او، بررسی‌های اولیه نشان می‌دهد ورود یک دستگاه ون به مسیر حرکت اتوبوس باعث انحراف و سپس واژگونی آن شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78349" target="_blank">📅 21:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78348">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eApidByAGyeYbcGXk57UQ7y_l1p6d13TJ6ZYiQ-lW27h1jHMAd7OuPdo3vVAyhQQT1TIYJBe9mwEhDqoXUK8Z_edNhpCHxWewfzF9QUh2UQxEE9ihUsL06c-X3xGsn3XZS23YlSjpBRdbkNLqSS8X37fPnwd-8TGi9YwYQohWDdw5-VoX3eV34Brdm4UBjkuG9MRALfJwEcNjej-yPm0IvKIoO8DrTQ25NEI1HTHQnkL0O71-3QfeXoyDAfYirUXg4xB3Xg8mFrJX2ADDcsDjjKIVO9OWNOSHGQnDZKZi4TPKjhxwpR6eKhRgjdfF0Tex22xaVYx3YGrgyl2ERx5xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع امنیتی عراق به خبرگزاری فرانسه گفتند نیروهای امنیتی این کشور سکوهای پرتاب پهپاد را منطقه دورافتاده الطیب در استان میسان در جنوب عراق و در نزدیکی مرز با ایران کشف کرده‌اند.
همزمان خبرگزاری رویترز به نقل از دو منبع نظامی در عراق اعلام کرد این منطقه مرزی پس از کشف سکوهای پرتاب پهپاد بسته شده است.
کشف این سکوها پس از حمله به خط لوله نفت عربستان سعودی انجام شده است؛ حمله‌ای که ریاض و بغداد گفته‌اند از خاک عراق انجام شده است. بغداد روز شنبه گذرگاه‌های مرزی شلمچه و چذابه را نیز بسته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78348" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78347">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoikL_kErqF6cgLRgEiG-1XcyVWamKoiS4LPgrNsn--QdpCAIJnpVFo1EY5Hrbm77WcwdxYFtIVTC6I9rckZsoeWJ7BpIgBTjDqA9Ri-b9BSlsIEGwz1x409BFiIHE6JaPk16L4LpFgJ_K2o3k_Tp3xK23-mndVpKpxHJcZEf23zAvWCnUTU1mQyr-_qbs6VKLk9gt5t9lTCk1yoczUyaZy9WHokEL0hlS4QwUvgbbyFcP-PlTJLv6bH6NA_2sqYsp-ccDtchegC2CAGd2AhVWIDNVvxjKhq3NtfXW5wpPFPxjdO8wDDchuH1DJeGxLiNwCj_1R09_U9SIGJx_ePMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، به نقل از یک منبع آگاه گزارش داد تفاهم نهایی جمهوری اسلامی و عمان درباره مسیرهای جدید کشتیرانی، به معنای بازگشایی تنگه هرمز نیست و باز شدن این تنگه به اجرای هفت شرط تهران از سوی آمریکا بستگی دارد.
این منبع گفت تهران و مسقط پس از گفت‌وگوهای فنی و دیپلماتیک، در اوایل شهریور درباره جزییات مسیرهای جدید ورود به خلیج فارس و خروج از آن به توافق نهایی رسیدند و قرار است این تفاهم به‌زودی با حضور وزیران خارجه کشورهای منطقه اعلام شود.
بر اساس این گزارش، تفاهم تنها میان جمهوری اسلامی و عمان است و کشورهای دیگر، از جمله عراق و کشورهای ساحلی خلیج فارس، برای اطلاع از جزییات مسیرها و ترتیبات تردد در نشست حضور خواهند داشت.
مهر نوشت مسیر ورود به خلیج فارس به‌طور کامل و بخشی از مسیر خروج از آن در آب‌های سرزمینی ایران قرار خواهد داشت و تردد در این مسیرها بر اساس ترتیبات تعیین‌شده از سوی جمهوری اسلامی انجام خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78347" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78346">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=ZJsw60DdMiUMtVOtl_l-17sP9G-AeNNkhSIJPrHPNUj4Wx8WB81yvVxFz4c-eF_LH-rOam9wYGv-RWIqz02jJdebTuHlhXTroqYRgBTZp9Wty7AyKafioFaBsLVzYzPO9_yhDnb5uuhkQdgLS-QfzDh-SZ4EfGTxEdSQiE7o-9EkZvweRGM8S7fywVNi1PWqZetG18HrW_Hu8jWGNUW8mtQKdlz_872cjVJKdRE3EGXMFnb93-j3JiYEB3o0mI-Cji6JG_nQCQWu7vag4carfmsrXEkINhU1Y_CRsxdR2SCfGV6fnnn1aT-zFSyf491Lz4duDOoNrZoJmJfWjELSyg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=ZJsw60DdMiUMtVOtl_l-17sP9G-AeNNkhSIJPrHPNUj4Wx8WB81yvVxFz4c-eF_LH-rOam9wYGv-RWIqz02jJdebTuHlhXTroqYRgBTZp9Wty7AyKafioFaBsLVzYzPO9_yhDnb5uuhkQdgLS-QfzDh-SZ4EfGTxEdSQiE7o-9EkZvweRGM8S7fywVNi1PWqZetG18HrW_Hu8jWGNUW8mtQKdlz_872cjVJKdRE3EGXMFnb93-j3JiYEB3o0mI-Cji6JG_nQCQWu7vag4carfmsrXEkINhU1Y_CRsxdR2SCfGV6fnnn1aT-zFSyf491Lz4duDOoNrZoJmJfWjELSyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78346" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78345">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiWBnwU3qhXOOVa2iOmsFIftJVwMCOwXpHPm25sVMylyAtGNMwz4VtINsYnu-1afcfz_U-nwq1MpbN6F-wMqOJ1IzZIGULMJbMgjudkKPMSO9BX5HRm55fvYCpCidfkFAy3g90feWMJESkMthrd8iCYBL6x0uhayXq4PGFd8A0dE6VPLJk0AcGJdWy3S7ASgQnPAdokcW6bH2kE9HphSXlSlZQLM4Qw-n_TtZdN1RtHgk2oK1JJgr8JQt9yxOBmLHZCpHKl1vu_3RDGgDJYvW_QP2WxRAghAUF1ic9sljGxX2XnARE1pZpeOO3L7kd_IUZ29QVSiUr3lYka-iayFeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت احتمالاً جمهوری اسلامی مسئول حمله هوایی به عربستان سعودی بوده که به تعطیلی خط لوله شرق به غرب انجامید.
او روز شنبه در دوبلین و در پاسخ به پرسش خبرنگاران درباره مسئولیت ایران گفت: «فکر می‌کنم مسئول‌اند، احتمالاً خودشان‌اند.»
ترامپ افزود با محمد بن سلمان، ولیعهد عربستان، گفت‌وگو کرده و او را «دوست خوب» خواند.
رئیس‌جمهوری آمریکا همچنین گفت حوثی‌های همسو با جمهوری اسلامی با دولت او تماس گرفته‌اند و اعلام کرده‌اند نمی‌خواهند آمریکا مستقیماً وارد درگیری شود.
او گفت: «آنها به‌مراتب ترجیح می‌دهند ما درگیر نباشیم و بیشتر شناورها را عبور می‌دهند. فقط یک کشور هست که از آن راضی نیستند و ترتیبش را می‌دهیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78345" target="_blank">📅 15:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78344">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=b4TMR1OgHoWYX4GZCiMWGi6z2ugVoE15Nn7lL9KE4k_McuY9k8Gwpy2_qjWs_ea1LYNdC3R9jGWJCtr9JvySyrIVVPrRo0uYXdeLGdDHdyMUFnLlkDvFeWzeNKRBkUu9Kt4elysvI-EyhllFpnln-7tMGE-nxyv_KhAQpwxdCsiZGSdhO4xNWg-Uw-F-ig5iYrsoXa7Ibad8d_f4gnZoD_9mAVnMluDw7Pz46vVSvDrS4dTTXinOE2boKe3pQgicIlqCDknXm_qWVJL_qXmA1fSSWomhbddUuaEDOm0tMKfY9GW9S_AUoKajeTnLSqySwYv2aqTWUym0p8w13Dyc5g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=b4TMR1OgHoWYX4GZCiMWGi6z2ugVoE15Nn7lL9KE4k_McuY9k8Gwpy2_qjWs_ea1LYNdC3R9jGWJCtr9JvySyrIVVPrRo0uYXdeLGdDHdyMUFnLlkDvFeWzeNKRBkUu9Kt4elysvI-EyhllFpnln-7tMGE-nxyv_KhAQpwxdCsiZGSdhO4xNWg-Uw-F-ig5iYrsoXa7Ibad8d_f4gnZoD_9mAVnMluDw7Pz46vVSvDrS4dTTXinOE2boKe3pQgicIlqCDknXm_qWVJL_qXmA1fSSWomhbddUuaEDOm0tMKfY9GW9S_AUoKajeTnLSqySwYv2aqTWUym0p8w13Dyc5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای منتشرشده در رسانه‌های اجتماعی نشان‌دهنده ازدحام در خروجی مرز بازرگان است.
برخی گزارش‌ها دلیل اختلال در تردد از این گذرگاه مرزی را «محدودیت‌های ظرفیت پذیرش در سمت ترکیه» عنوان می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78344" target="_blank">📅 15:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78343">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFBPUHCxjQY68l_9xVdLnyvXpf2sSmU2zZbnfnSpq0TtG55YmhyWq26AMmaOE9pmB66X6anwuJ30Us0oObKBvQAE2oprb0QLHCXYguel5Y28N2bM_ZSuSv44E0XSx9eoi3L_KtW2HMHe8MVekI-QF3WoK4VcqzhoQW3OsEjeAI2vn6otNiZH0cSfHTmshRBWE6NXxWIBSrOAQb-sFioTcFI0X1JWnkYQHyltruEr_KPc7Dw5pfJFNmT2xH1yCSnfJGXhE6I9UaPW9nm0r1NfzE8akGFkizWFlTUFbkWnNu70Gp2mMBw_USVt3cbc8qaXcnXs6ENQ38jX_gefgaVlsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون استاندار خوزستان اعلام کرد مرز چذابه نیز همچون شلمچه از بامداد امروز با اعلام مقام‌های عراق تا اطلاع ثانوی بسته شد. بنابر اعلام ولی‌الله حیاتی، هیچ تردد کالا و مسافری از این مرزها انجام نمی‌شود.
ساعتی پیش رویترز بع نقل از دو منبع امنیتی نوشت عراق پس از تازه‌ترین حملات پهپادی صورت‌گرفته به عربستان سعودی، دستور بستن گذرگاه مرزی شلمچه بین عراق و ایران را به عنوان یک اقدام احتیاطی صادر کرد.
مرز چذابه در استان میسان عراق قرار دارد و دفتر نخست‌وزیری عراق بامداد شنبه فرمانده عملیاتش را برکنار کرد. این برکناری پس از آن انجام شد که تحقیقات تأیید کرد آخرین حملات پهپادی به عربستان سعودی از خاک عراق انجام شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78343" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78341">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d6s9YOBLEXJYcgJd-MNcObONfO-3C2kL71F3hk9j1GoGm4qaeb1M1yeocVjB-xHG38-UPKLkiYS_FyHzq7KKHypNYwROAVfTNiboJoK_-_AwoNZO-ANN_pyFaZaKesEX29Fs7o7svtjB75dugspmskmzO_HP8hdsgqZvMyybVf_887eKYRdx9KVAd8bLtwvn2S6Cq2QjYJdS8AF8wD_e0kR_q7TwwY0iAKofwKJ9Uj9L55eu8DYSPlnkI7hLXV7iLshUv-M9TejBpkqdeaZfwSJ-GaRicfAkzM6Z7-E-Cb3wHxyCknCmW7InZXex_jlefcSFFJLlQ6FoQXWBPSGVqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lgHtOeVR1-sXDGSWN93ec5hRT0Um7e0aQW_Y4elpQNix3dRLXMvzkgCzxoobTtJcH8oaQcbNdiB7m1y5_c-bMWrsfzxeVn34kVq8E2axKOm6ShNmkUVzyqdsULOAdD6AKI2IaZ7r2PmCp7LrLFhD793hgzrExTemBviWADhjQKPFHHXy6MJJvm7K2xw8DXoH0Y0p-cn7EFFLrLewPM2ZcJKjA3bzCIFJZOWLqSnzuacurbxVXzrtfTz_x0hB6TBpFb3w7-3RyNwVQQGIr9BQSK9n_z4rHVNzX_i6zUUy8l8hNpqhOaMbzTUnvarw7vutfYo38vWqEs5pVrJNFdZQmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/78341" target="_blank">📅 15:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78340">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pP8T_mA51oHzEee6aPzsNFB8elOLECgbXjiXSrCfOoC0AUBo2iR4w6T0z-QTHAIpR7CXh0DY7bTm31u3UMa869QokT7uwhmtZQFONSHch2KTKRetY25hbUtwTtwDedG87HE6z1EWRIF-c2fWCCl6sDe8tgraNMvQ3NicNfoCWLm8M9e7E8vYViqwxwy5fRkrctiJ8_Wv-FqOkFdqhF2sHqoahq6uo5vcJS3JvGR_ozX3JjCcjuffOAdJSZtyMnCaDPvNkk-4oP-s6aDj8hZFg3Tk0vbBHrZjMoE9ms77PzowDwiok6mvFe73CftfTdKKlQ1OtWw0VkH0Q12QbXFxTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78340" target="_blank">📅 15:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78337">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AoMy192i0Q_KYGZ2EeCcgFNoHCjZCFVzZbaTkDtB6IUBVY-KYpq6vNCLUWtWQmQ57maIq69TFVxEvQsTVDzCyBfcVDtqSZe2UyzXKWL-yciiLCy3RMGhmFqnIWsx6qMOzq3_5saO2muJ2C2Uy73z0N4C-WHeVXIP3pDRr_TByzXdszcLN7DDUTAeObNAsymo-hcbByukIBv-kB6TEM4ResyTdGYfezOpW3erU1BcVJR1AK5KEMmZ6g9o8knqv6D9aocXPSLvViPzQaV0rAfs4PFnwR_3-XsuuvprR1tHEocdDZXQKsKfKevapexldN2GQs9zi2YtQAxZeo0zAJpVxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d70-WMKwH9gqRTF4LvKw6uYT_q2-QJh1GDVZ-a-Sn7VuDf8VpZ-2Ja-IWDW1iZyfk8dpGnX_nGvl5KEaWG_lZxG6eaYRXeD8PEYiNg47XYnCkw0uR4FAaGND-gmbeKxXizHN7aBLzO4MYhp0muKxxGN8iSv1eggDrjJ4H9CqnTZcRv_aBKsG2eJwL779BLditMRhh6FpEXHyKUoUqA8V3JQV5_YUcG4AROQd3cIShxJ7W63gP0eG-a7vuihyYmu4BAvG8elq-UwGo470LMGqyCJdyCQm4kkWBOY8fkX4h_YhD8c6SmAAO-a6bN9R-zYex5cWnub1aZETC7aDpkxP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E5inxQ7iTs7GglVKuIIwT8TDaCO4dpmQu7pZmwsFcJpA34JFE-cuA27QlSiWpplSQIgDC8lEvtNS3Vco5pUcEYxdbOmcXLBZpRsIlNCfbGlDp2LN-IYdqaX9OB1KkExO-uj28MRQraJsw-w0jBEbmW4mLCuF78N0EEUOGuROeaATHTBEFSYE6tq6TaXXCxzAGcqz0GuuOft2db1Fz2z5nD4vXZUP9zoruiS49vMp199AQmpGOVJibauYmw3kC26k2kg0k7hNJ5iD5RoiqjJOtiDUwverkYWUEqfp2Fhb8ji_o5F8whUl9nebXyKQR4XGvrs__hYpn5XeCsR_yuAPeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/78337" target="_blank">📅 05:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78336">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/78336" target="_blank">📅 22:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78335">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFB_vUGIHNY07IdlFScQp5VXAY_q3LwbCuKF3sCtOwl3fyF5XIBbJklw58kbFOAKXZvG2r3ubxJJXQqImj2FTJmdyH5uu22jDsVAwpNxw72UBhLFBTQrowm8v2pywAVdzYVEwrpFkhDdbKA4ALLnrgnsrc0jotIiPe9R_nczCum7St4gWbTFHjmctNJKTKJUSpxaPNTExXuwLZmqIk68S47Q4-zcFYxXFGUovoWKTDCRL2ICDaT3eI79XRoNOxJfAlays1dXgSwQ7I6WzUohaNtuZeyrksKtcjiYr10zwxzzLzoIO5FtVcYHjLFjE89LYnM2fU8sM1QIVRZIUwsByg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس دولت چهاردهم جمهوری اسلامی که به هند سفر کرده است روز جمعه ۲۰شهریور۱۴۰۵ در پایتخت این کشور اذعان کرد که فشارهای آمریکا بر ایران به مرحله «دشوار و خطرناک» رسیده است.
او با اشاره به این که جهان امروز در یکی از «پیچیده‌ترین مقاطع خود» است، خواستار «همکاری عملیاتی» کشورهای عضو بریکس شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78335" target="_blank">📅 20:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78334">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=OIkSLdJCzFhSWDUOLeH1ZGFJEdzVeXrEuXe1nsdj3rbDza0HXnilj_qLI3cyrz1_r5i3Bs7UNakKhIAs_USCkaV-H9301XmxkTT6vy813JOM2xbtlnDBD7EGcFGh_iWrn6mO7Z-899G46P0YPvvDNcSl5s9XsdwDcxexnfflgXTuWNnyUg_eYIUsgt6OvdFertNxlvmBOCci8_DhaLGcNv1EaKvKEo2R3B3PMQunOy2VILePvRYpll0IdtMDusa95oxbDzekx0BwCXrvfMrtuHFnsEgOnRmfhpnTz1_XD4WvvJk1q16FdfpnswJylfqLbghf8KL-t4sF-nbI4ozs8g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=OIkSLdJCzFhSWDUOLeH1ZGFJEdzVeXrEuXe1nsdj3rbDza0HXnilj_qLI3cyrz1_r5i3Bs7UNakKhIAs_USCkaV-H9301XmxkTT6vy813JOM2xbtlnDBD7EGcFGh_iWrn6mO7Z-899G46P0YPvvDNcSl5s9XsdwDcxexnfflgXTuWNnyUg_eYIUsgt6OvdFertNxlvmBOCci8_DhaLGcNv1EaKvKEo2R3B3PMQunOy2VILePvRYpll0IdtMDusa95oxbDzekx0BwCXrvfMrtuHFnsEgOnRmfhpnTz1_XD4WvvJk1q16FdfpnswJylfqLbghf8KL-t4sF-nbI4ozs8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواهر امیرمحمد شاه‌کرمی با انتشار ویدیویی در صفحه اینستاگرام خود، از حضورش در مکانی خبر داد که به گفته او، برادرش آخرین لحظات حضورش در آنجا را پیش از بازداشت سپری کرده بود.
او در توضیح این ویدیو نوشت: «۱۸ شهریور، برگشتم به همان خیابانی که آخرین نگاه‌های برادرم آنجا بود؛ تا صدایش را از همان‌جا دوباره بلند کنم. این‌بار ایستادم برای صدا زدن نام امیرمحمد شاه‌کرمی.»
در این ویدیو، خواهر امیرمحمد با در دست داشتن تصویری از برادرش، نام او را در همان خیابان فریاد می‌زند.
امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، در ۱۸ دی‌ماه در شهر قدس بازداشت شد و پیکر او حدود ۶۰ روز بعد به خانواده‌اش تحویل داده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78334" target="_blank">📅 17:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78333">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/957af9390d.mp4?token=rFqM2s1UVtjDAwjFdy1zhZQCYDWSAHl4GGPQ0vcndAlb666bajiWnAf-uuNDTxZaOxq4gcRBvOd_WX1_GGsu280zxiYe9fdm1PK1lS_LuVkM7pHbCptkMBx5ZyF1W5F2hczQFtwgZLoEB5nr2BDTTrB7tnbF4jLWp6LkVT5rZs1zodeu4K4smY5oMgm3lwnv6ai5S8wT11p4ikMHF89ZmpUeyrK839vx3lXja5gbysBvRjDJiWAgqLHLsdK85MGbWY6b3uikQt3TA-RfpDvBHJp6LwkZ74YzH-bVw0qv6iZ2rHWPauOBJydH3VcTJ6MwGhNyeGNq976URZE0xMyxvA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/957af9390d.mp4?token=rFqM2s1UVtjDAwjFdy1zhZQCYDWSAHl4GGPQ0vcndAlb666bajiWnAf-uuNDTxZaOxq4gcRBvOd_WX1_GGsu280zxiYe9fdm1PK1lS_LuVkM7pHbCptkMBx5ZyF1W5F2hczQFtwgZLoEB5nr2BDTTrB7tnbF4jLWp6LkVT5rZs1zodeu4K4smY5oMgm3lwnv6ai5S8wT11p4ikMHF89ZmpUeyrK839vx3lXja5gbysBvRjDJiWAgqLHLsdK85MGbWY6b3uikQt3TA-RfpDvBHJp6LwkZ74YzH-bVw0qv6iZ2rHWPauOBJydH3VcTJ6MwGhNyeGNq976URZE0xMyxvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تسلیحات کشف‌شده در علی الطاهر را ایران برای حزب‌الله فرستاده بود
نخست‌وزیر اسرائیل روز جمعه ۲۰ شهریور اعلام کرد نیروهای اسرائیلی در جریان عملیات در ارتفاعات علی الطاهر در جنوب لبنان، مقادیر زیادی تسلیحات را از زیرساخت‌های حزب‌الله خارج کرده‌اند.
بنیامین نتانیاهو با اشاره به تسلیحات کشف‌شده گفت: «مقادیر بسیار زیادی سلاح از آنجا خارج کردیم که سال‌ها توسط ایران سازماندهی و تامین مالی شده بود.»
ارتش اسرائیل پیشتر با انتشار ویدیویی اعلام کرده بود، نیروهایش پس از به دست گرفتن کنترل عملیاتی ارتفاعات علی الطاهر، زیرساخت‌های زیرزمینی و روی زمین را منهدم کرده‌اند. به گفته ارتش اسرائیل، این شبکه بیش از دو کیلومتر امتداد داشت و شامل ده‌ها راکت، موشک و پهپاد و همچنین موشک‌های ضدتانک، مین و مواد منفجره بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78333" target="_blank">📅 17:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78332">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIAT5Hwvkjg-esXr88At1ku7Hv5VQpgZW7XubmnixEdLOyQm3r565bGaxWue5Xu1-5IeSSiADTDQ0hg3Rw8lWZe8MqW1wUbsPX5iNq0vjCBsS9w1m8QrSFFLZCW_aZ-sR4IVbAWqNwd43-wmcQWXZSuCbedAxH4XRHkppxL7ey6D3ZmCjm9GIZuH5e9HNL0Tyw3Xy5qNC_VFAi9bVJ-kqsrV3Pg3d58Jy-9gPqmcwBgUtR9jxKw16oLyes8_GLjVDUqXh7Cwex7M5wLBOtHvlPOzMCZ_uMvpZYy9snQ4MfABuWiKShvOltx-AC3DnBqlyuiYBlJPOl8-EAaKB-EoxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/78332" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78331">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tiyHSEkS8DytOcQeX-p1ZcpGihjZWH_mWsxwEm8ypcY7FnwCF5a6jD1gi2BmK8Ye97DDa1ymwIE0mqk7u0Vq1dExWRuvL6yeBwgazVu-pe2O74ffduRFpTasAhA5wLnScRGtkX9I7F-vHLGLRwon0K9q_K71ve3yIjKcGp8Snf5_U2MhLiF2z0pB8Qcd7kdi-WYERg4hw1vpdD1LGGiK48weSaHJa0p2XWJxOpMdGA4CDDng684dBewhG9mi-D7_z5-sb3IEVmx2IPTJDjDrJJQl_2DKXwWqXkw5SivYJLbdfgFGpxvCsA7wF347mPdAI48lzyOcVNXTscdzbgwiqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت آمریکایی «آنتروپیک» اعلام کرده است که سه عملیات مرتبط با حکومت ایران را شناسایی و مختل کرده که در آن‌ها از مدل هوش مصنوعی «کلود» برای تولید و انتشار محتوای تبلیغاتی، طراحی سامانه‌های نظارتی و تهیه اطلاعات مرتبط با هدف‌گیری نیروهای دریایی آمریکا استفاده شده است.
این شرکت روز پنج‌شنبه ۱۹ شهریور در تازه‌ترین گزارش اطلاعات تهدید خود، مجموعه‌ای از موارد سوءاستفاده از مدل‌های هوش مصنوعی آنتروپیک را تشریح کرد. این گزارش فعالیت‌های شناسایی‌شده و مختل‌شده از دسامبر ۲۰۲۵ تا اوت ۲۰۲۶ را پوشش می‌دهد و علاوه بر ایران، مواردی مرتبط با چین، روسیه و کشورهای دیگر را نیز بررسی کرده است.
بر اساس این گزارش، آنتروپیک حساب‌هایی را شناسایی و مسدود کرده که از «کلود» برای اجرای عملیات نفوذ با هدف تاثیرگذاری بر افکار عمومی استفاده می‌کردند. سه مورد از این عملیات به عوامل همسو با حکومت جمهوری اسلامی مرتبط بوده است.
آنتروپیک می‌گوید هر یک از این عملیات از سوی فرد یا مجموعه‌ای انجام شده که یا مستقیما در یک نهاد تبلیغاتی حکومتی ایران فعالیت داشته یا به نمایندگی از چنین نهادی کار می‌کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/78331" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78330">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUf5NEdquBo0y6AELY0u0RZeDqF4Hn1mCcvunyBCa5ScU9mUWUWoWYXnmcSBP_yLI1aEYpLk_rWsYw-lMUTLmOAiJeJzQdKgIC6MjDoxaMApKItnIEFgCP6Rbs1WdqMF8FwTH3gD4qbeDK7xC_VWcR0LxcCCowZF5slaFFns5qgmpRhwB097FFVGuDHbQDrqvz3HTJwUtE0xDKPIsWdU-PoSK5kAOiBQynj3DOpDKdc_0hcMV2oRyCL211jusTvwmZond4iRWt77zC8s8WGBnEM6dJrJQE-UX-zJv7nuqgAFeCVcc0lmu51mIz73ARV4wMgzqHn4QcZgluRMjdR90g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت مخابرات ایران با انتشار اطلاعیه‌ای در سامانه کدال (سامانه اطلاعات جامع شرکت‌های پذیرفته شده فهرست شده در بورس) اعلام کرد هزینه مکالمه تلفن ثابت با تلفن‌های همراه از روز جمعه ۲۰ شهریور ۴۵ درصد افزایش می‌یابد.
به گزارش انتخاب، بر اساس این اطلاعیه، سقف هزینه مکالمه تلفن ثابت با تلفن همراه از ۶۲۵ ریال به ۹۰۶ ریال افزایش یافته است. این تغییر در پی ابلاغ دستورالعمل افزایش هزینه تماس تلفن ثابت با تلفن همراه، تماس میان تلفن‌های همراه و پیامک اعمال می‌شود.
شرکت مخابرات ایران اعلام کرد میزان دقیق تاثیر این افزایش بر درآمد شرکت هنوز مشخص نیست و آثار مالی آن در گزارش‌های دوره‌ای منتشر خواهد شد.
این شرکت در خردادماه نیز هزینه ثابت ماهانه تلفن ثابت را ۴۵ درصد افزایش داده بود. هزینه ثابت ماهانه مشترکان خانگی در تهران و کلان‌شهرها به ۴۳ هزار و ۵۰۰ تومان، در مراکز استان‌ها به ۳۲ هزار و ۶۲۵ تومان و در سایر شهرها به ۲۴ هزار و ۶۵۰ تومان رسیده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/78330" target="_blank">📅 17:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78329">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=Jla50H7UvFINFXAydsThNfeBcfxdw_n20nfnt2vFX9rcgYCnEIKQYLKq-8b5OwHZ0Sv8Y7EpoZN9O5ZVanQYzqnvZmEBGyHhcWBm72lx3wZqUz98CvrKbxDCo0a1L0d6DLWS_hmCaTkNEOREhBBA1xmOyjKTfaS7jxgjghFVjXlDcwTv-3rv_tFgRGWRCAE4e_DOtiQCiq1bwRU6tMQn3FzMF3r7tLFB4TtX7TfS60Nhvr1Hvvj9NMozOGam6dwVoB62SNKNQC16Dp0-GBaiXzmPqNMrg-aR1MUMhC-uc8uKs5npD585dqg0ZAmjEKptGveFrnHPp9aT4h8RqexPig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=Jla50H7UvFINFXAydsThNfeBcfxdw_n20nfnt2vFX9rcgYCnEIKQYLKq-8b5OwHZ0Sv8Y7EpoZN9O5ZVanQYzqnvZmEBGyHhcWBm72lx3wZqUz98CvrKbxDCo0a1L0d6DLWS_hmCaTkNEOREhBBA1xmOyjKTfaS7jxgjghFVjXlDcwTv-3rv_tFgRGWRCAE4e_DOtiQCiq1bwRU6tMQn3FzMF3r7tLFB4TtX7TfS60Nhvr1Hvvj9NMozOGam6dwVoB62SNKNQC16Dp0-GBaiXzmPqNMrg-aR1MUMhC-uc8uKs5npD585dqg0ZAmjEKptGveFrnHPp9aT4h8RqexPig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی زارعی دوز دره سی، زندانی سیاسی و یکی از آسیب دیدگان اعتراضات سراسری ۱۴۰۱ که در زندان قزلحصار کرج محبوس است، توسط شعبه ۲۳ دادگاه انقلاب تهران از بابت اتهام «افساد فی‌الارض» به اعدام محکوم شده است.  بر اساس اطلاعات دریافتی هرانا، حکم اعدام آقای زارعی دوزدره‌سی…</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78329" target="_blank">📅 17:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78328">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78328" target="_blank">📅 07:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78327">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNhjfjAoD5RGIjE92HmruU65xiJ7djxzwECwgQ6rEaGFjutWcYlvXaB2tLNHid7nWvw3zogdhjFr4REXMfHZz_c2OLY5ljCY7mln8uZnP3vo_J3B0YdUapvctQPKjveaeoQ6zE2ObFkKX8iN1-19DF39E9OAVQda-INhwPddIggQcZ-Iy28VyQMh18ynZC4hUqwtuVW_xKXIsOFVOC6blrItO7d0_68alWxqJ8HmGals3Y9sWWana6_r6wds-nKCHkwzNmQV3nISyiCvqaR947JWeAGdTx4xg12oKSVOpE1CgtDY4RfawnmVrfGKj068VNowSgxOFHn1Wb4O5Dzx-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا در دومین شب گردهمایی انتخاباتی میان‌دوره‌ای جمهوری‌خواهان که در دالاس در حال برگزاری است، بار دیگر، تنگه هرمز را «تنگه ترامپ» خواند و گفت «ما تنگه ترامپ را کنترل می‌کنیم». رئیس‌جمهوری آمریکا بار دیگر تاکید کرد که هرگز نمی‌توانیم به ایران اجازه دهیم سلاح هسته ای داشته باشد و نخواهد داشت. او گفت که ایران در حال عقب‌نشینی از همه جا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78327" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78326">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0OvQcMVz5ex0UmrRJsZqMxrVkgFC88HJApRUsQ4JaHmZi3yoPDvxM67AnOlZYo9nXEkaQxgHHHFiZ9Cban2IzX-reubowIUzdoArRRDw_6BiGcZCd_JxtcyazaD8U5FZAlQPBl-N3PjXY5Zr5D7IDbxHSvubXB9D8WICxtS289mpJ5VWrHCiPvj3tyq-36gDJ5xGIZ6eUYepTZsjjxlgGKGk0j03VDZzfKIT6l17fDFIqqIdjaknOLnfgniNo76TSuB6ANz6i-KjoVz50jmmiwGXqyUQpTgBCppI4ERitnDf_B4uCb7JjjFrV3xe48t6xnKA_xQ_TTaNn2Vrhbm0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هانگ کائو، سرپرست وزارت نیروی دریایی آمریکا، به اپک تایمز گفت نیروهای جمهوری اسلامی خسارت گسترده‌ای به پایگاه پشتیبانی نیروی دریایی آمریکا در بحرین، محل استقرار ناوگان پنجم این کشور، وارد کرده‌اند.
کائو در توضیح استقرار اخیر ناو هواپیمابر یواس‌اس آبراهام لینکلن و الزامات لجستیکی عملیات طولانی‌مدت گفت خسارت واردشده به پایگاه بحرین بر امکان پشتیبانی از این ناو تاثیر گذاشته است.
او گفت: «خدمه این ناو جایی برای پهلو گرفتن نداشتند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78326" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78325">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Loel6a-1jRvLf9kknU1mE8J3IPuh9BhfcLBB0vlssx9D0ttk6CgYBplWMUOkMz5UTJ7ZVpYpc1Ayif7UTnIGxCiueKsIUUs5L3PdyDBhTPp5fmCimZpREcC5G86L3H37lXoxKdiUPH2SlKAAWZ6K2cJDBY52U9CLUP1LnolQz-xvuMHbMTR3Ox4m6OvGQag1bgVtm9VzDS8FesqSz_qXg4UqsLJi8J1DAmR7EpxlOGlD4UznsGof0Uf0mkTsYiNWu6NbVzN0w1mM3hiqrxeohXMjtJqTH9FhN6WUT88DQsF3e_F9g7XBX-y0DVsnAm31mJ8zg_-IKJbe1nkzQyeUug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت پنج‌شنبه ۱۹ شهریور هم‌زمان با تشدید درگیری‌ها در منطقه و افزایش نگرانی‌ها درباره اختلال در عرضه انرژی، بیش از شش درصد جهش کرد و نفت برنت به ۱۰۷ دلار و ۶۳ سنت در هر بشکه رسید. نفت خام وست تگزاس اینترمدیت نیز از مرز ۱۰۰ دلار عبور کرد.
بر اساس داده‌های اویل‌پرایس، قیمت نفت موربان با بیش از پنج درصد افزایش به ۱۲۲ دلار و ۴۸ سنت رسید و سبد نفتی اوپک نیز با بیش از چهار درصد افزایش، ۱۱۲ دلار و ۲۵ سنت قیمت‌گذاری شد.
افزایش قیمت‌ها پس از حملات به نفتکش‌ها در خلیج فارس و دریای عمان و پیشروی حوثی‌ها در سواحل دریای سرخ رخ داد. رویترز گزارش داد تصرف بندر مخا و پیشروی حوثی‌ها به سوی جزایر حنیش، نگرانی‌ها درباره امنیت تنگه باب‌المندب و مسیر صادرات نفت عربستان سعودی را افزایش داده است.
هم‌زمان، تردد کشتی‌ها از تنگه هرمز به‌شدت کاهش یافته و داده‌های اولیه نشان می‌دهد ۱۸ شهریور تنها هفت کشتی از این آبراه عبور کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78325" target="_blank">📅 03:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78324">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=pqsNLDNb0lAC_iMLL-LYMId6Wcnj2BXpZPkilwTLpOGJ5yPBRfspgbE3GPFUpL26eNlwc_M_BRg71o8xLFtFSDYbtBOAFHWSi0f5y7mW8w2O8pJFA6AoqNJbQhn9Rb-uyWmIvNwJ13vP2vGyM6udMiW28dektkFQ7IO30YiAv2Tb6M9Zr7Ud0jEV_s8MSWbRPDqX33SuM42_xn_Y6AdDmVrk8HK2KKPAMXKOHaNTIvI9fG2Hb7lD9A4_9uIl8_AqAcAc72HyHu_BsP-tjxxZZjv_D-xenwPn0NCl7oyo1WdNDBB2-Io13BzsclIo_aKhHV7E3ZQ-zrMfMwCZxslFTA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=pqsNLDNb0lAC_iMLL-LYMId6Wcnj2BXpZPkilwTLpOGJ5yPBRfspgbE3GPFUpL26eNlwc_M_BRg71o8xLFtFSDYbtBOAFHWSi0f5y7mW8w2O8pJFA6AoqNJbQhn9Rb-uyWmIvNwJ13vP2vGyM6udMiW28dektkFQ7IO30YiAv2Tb6M9Zr7Ud0jEV_s8MSWbRPDqX33SuM42_xn_Y6AdDmVrk8HK2KKPAMXKOHaNTIvI9fG2Hb7lD9A4_9uIl8_AqAcAc72HyHu_BsP-tjxxZZjv_D-xenwPn0NCl7oyo1WdNDBB2-Io13BzsclIo_aKhHV7E3ZQ-zrMfMwCZxslFTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78324" target="_blank">📅 01:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78323">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WarTS1TwyoqiyCJrUT5vKpFgYdQcSX5bb3UZtclNGXU5mL6NxMP6a0dKIgD1Cld3sU99bMeg42T6UXY7ygDW7cRrb6bKiqXQnZLTg0dSCVVd1_MltrksWW5-I7L4T6q88kdeZuCU-H7ixRcqTrNzabumot79RAkbdsqZHXJF-QN29rjzFbruW1VzFtf4Ct3TSipFectf2zerNaaKxnbsskxUd40NxI9jUJu2iXbFRYCIA38IcqeQZ_QrrRRPU1WSLXrR4HTPEeMojSfgUTtuzCfyS88xric_IbdYHzdcPol-jiyybpPiLfyLkbKxreOieVTXU0LWUddXXjO_o3IJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا، یوکی‌ام‌تی‌او، عصر پنج‌شنبه به وقت واشنگتن از برخورد چند «پرتابه» به دو شناور در نزدیکی سواحل عمان خبر داد.
بر اساس این گزارش، این برخوردها در فاصله چهار مایل دریایی غرب شهر خصب، در استان مسندم عمان، روی داده است.
طبق این گزارش، کاپیتان یک شناور اعلام کرد که شاهد آن بود که چهار پرتابه نامشخص به دو شناور نامشخص اصابت کردند.
در پی این اصابت‌ها، یکی از شناورها دچار آتش‌سوزی شد و از وضعیت شناور دوم اطلاعی در دست نیست.
مقامات عمانی در حال بررسی این واقعه هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78323" target="_blank">📅 01:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78322">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=MgZhb-zpcEIi1MxyCmyqw4m0hFAzWSLGKhWoYGLwhG4gcEhQZ0ECWOR4GeIoXv3sDCx89esg5jnKlWi-KKc7m2Au48hp6wZOrSlcb5nZUm9Lmefbtr1i13q5QKEPv27yrHrwMn48y4WTQlYhhOkcdxzz_8G2VhooD6F8QW4VRGCRIKgAr52Zhnt10O8gW2fwNwpq8IaI5CtAWh-NEPxyk9ofNnOZmcqdPXOJVLDvRtEjc7mwBz3Ug8noy2rvPf9fsYTFYo_faozcRiGbK-dFwXfQVAgYFnkXYJC5RafMyvPfF1daif0zEugotAiRR6cNzqi22BRCZWNpnAKrh-JTGg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=MgZhb-zpcEIi1MxyCmyqw4m0hFAzWSLGKhWoYGLwhG4gcEhQZ0ECWOR4GeIoXv3sDCx89esg5jnKlWi-KKc7m2Au48hp6wZOrSlcb5nZUm9Lmefbtr1i13q5QKEPv27yrHrwMn48y4WTQlYhhOkcdxzz_8G2VhooD6F8QW4VRGCRIKgAr52Zhnt10O8gW2fwNwpq8IaI5CtAWh-NEPxyk9ofNnOZmcqdPXOJVLDvRtEjc7mwBz3Ug8noy2rvPf9fsYTFYo_faozcRiGbK-dFwXfQVAgYFnkXYJC5RafMyvPfF1daif0zEugotAiRR6cNzqi22BRCZWNpnAKrh-JTGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران روز پنجشنبه ۱۹ شهریورماه تصاویری منتشر کرد که به گفته این نیرو، هدف قرار دادن یک شناور بدون‌سرنشین آمریکایی در ورودی تنگه هرمز را نشان می‌دهد. سپاه اعلام کرد این شناور با شماره بدنه ۵۸۳۸ و از نوع «سیل‌درون» بوده است.
علی عظمایی، فرمانده نیروی دریایی سپاه پاسداران، گفت این شناور بدون‌سرنشین «جاسوسی» متعلق به ارتش آمریکا در تنگه هرمز مورد اصابت قرار گرفته است. او همچنین گفت: «تنگه هرمز مسدود و تحت اشراف اطلاعاتی و کنترل هوشمند ماست و هرگونه تحرک خصمانه مورد هدف قرار می‌گیرد.»
نیروی دریایی سپاه در بیانیه‌ای اعلام کرد ارتش آمریکا طی روزهای گذشته شناورهای بدون‌سرنشین خود را به تنگه هرمز اعزام کرده است. مقام‌های آمریکایی تاکنون درباره این گزارش اظهارنظری نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78322" target="_blank">📅 22:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78321">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iz8Z4SjycE_KoXzk3t7FaTCpwav-1V6Xl9W4IZLv4za_Ix57ZrXPKk214JFDsobBsP2PFMIzZzs6OsPtlnJuuBiN5MrDE_o3WpEHtioX08UFqpnlkUy9_pNoYuwpHf7cEbkQLi769DRlbFckj3Rjuix4BEtnWTNVUm2425xb-kIZNepKzM3A5aO-XgviLrM2SnMhDBdreTcylft_leEl_IWr5D5qwpAdC6wdthZAm7RZomslRksfhDiJ_Nr1YTWP2RbO_C4BeruzHEzwIjJ7dnJC_YqZy_Cy9i_BoUkzsh63XK84AyXmfLRUMIrdo6DpV_xrz8Q2qurtEAC4gmhZNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، روز پنجشنبه ۱۹ شهریور در گفتگو با بلومبرگ اعلام کرد این سازمان بر اساس تصاویر ماهواره‌ای، شاهد تحرکات ساخت‌وساز در سایت بسیار مستحکم «کوه کلنگ‌گزلا» (Pickaxe Mountain) در جنوب مجتمع اصلی غنی‌سازی ایران بوده است.
گروسی با اشاره به اینکه بازرسان آژانس هنوز موفق به بازرسی از داخل این تونل‌های عمیق نشده‌اند، گفت: «نشانه زنده از تحرکات در اطراف این سایت ساخت‌وساز وجود دارد، اما اطلاعات دقیقی از فعالیت‌های درون آن در دست نیست.» او یادآور شد که ایران پیش‌تر قصد خود را برای انتقال تجهیزات به زیر کوه جهت «مصون‌سازی در برابر حملات» اعلام کرده بود.
این اظهارات در پی ارجاع پرونده هسته‌ای ایران به شورای امنیت سازمان ملل مطرح می‌شود. بر اساس گزارش‌ها، آژانس از ژوئن ۲۰۲۵ و پس از حملات نظامی آمریکا و اسرائیل به تاسیسات هسته‌ای ایران، امکان راستی‌آزمایی وضعیت ذخایر اورانیوم با غنای بالا را نداشته است.
دونالد ترامپ، رئیس‌جمهوری آمریکا، بار دیگر با اشاره به این سایت زیرزمینی، نسبت به هرگونه اقدام ایران هشدار داد و در یک تجمع انتخاباتی گفت: «ما متوجه فعالیت‌های مختصری در کوه کلنگ شده‌ایم. به ایران توصیه می‌کنم دست از پا خطا نکند، چرا که مجبور خواهیم شد ضربه بسیار سختی به آن‌ها وارد کنیم.»
از سوی دیگر، سی‌ان‌ان روز گذشته به نقل از منابع خود گزارش داد که ایالات متحده در حال توسعه سلاحی با نفوذ بیشتر با قابلیت تخریب اهدافی در زمین‌های سخت مانند کوه کلنگ‌گزلا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78321" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78320">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhZLCPObEXwxrVfNJNppRzHJA0PcmaXAaiwbUcAkFGnEq4kJuHn-c6qIm8A4cSoup2s4vYgs2qTbPBmyZXykU2krY-OIW6ee5Fpg7KP33CDK29GoXjhooMow4ckhBU52bpHn3LgCN-q_iiJVY0XwguSv7YXkO6QiQn-EQaevAK0M36s7KeajeRK4kDJkpaXFyLp9oJlsK3WC2QNFcl4AwSJNAo9mCX7U_SDqcFyoNdxZi9tsD7xGzt_OsZSVDgkzY0_orQt3e2xkJ0eqpYaAmrCr7ZQ6k3gALB5Zbelb521Bvw_q4ibo7766FlOd3WZROkGVpjmnlkMvi48U9mrNMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه قبل ماموران امنیتی به منزل خانواده «کیاوش میرقاسمی» از کشته‌شدگان اعتراضات دی‌ماه۱۴۰۴ یورش برده و «سمانه عصاران» مادر او را بازداشت کردند.
به‌‌دنبال تشدید فشارها بر خانواده میرقاسمی حالا صفحه اینستاگرامی مادر او از دسترس خارج و کنترل آن به اجبار به دست نهادهای امنیتی افتاده است.
تمامی پست‌های پیشین این صفحه حذف شده و تنها یک پست به دستور مقامات قضایی در این صفحه قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78320" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78319">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la0TZmICf0iLqxZTK5Qhi45lSxmGMRvft0yGr_4RR6NcUro7bbPZk5NadmP6vJFAbn-0A2U5Z04dmMZuokrL1k3xP-TuscOQ40xT5Pl5zz_J3vYEfqr-1cK-Urv5LDl6RE2Kwif0uoPhWnsYoFHCocPr7op-on-x6zw2X0LOEjeruJqclVEC55KpE4UPQwhl23VasI2bGqvSEDv7mKXsW1s7-hK77RRXqDWBCYw5P2Ljoc0qrHYvwMBhkBkdpHfcwPh8EOlnbxRxHg3ctlCDKeiRDjkwQh81-tRWtsXKqxWt4_oN6_V8Na1EOfEXpPuaPT8jSSHgdrQAzE_tcgbCzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس بریتانیا دو نفر را به ظن ارتکاب جرائم مرتبط با ایران و نقض قانون امنیت ملی بریتانیا بازداشت کرد.
این دو فرد در لندن پایتخت بریتانیا و در جریان تحقیقات مربوط به فعالیت‌های مرتبط با ایران بازداشت شده‌اند.
پلیس متروپولیتن لندن با صدور بیانیه‌ای تأکید کرد که این تحقیقات، با هیچ‌یک از حوادث ماه‌های اخیر که در اماکن و ساختمان‌های مربوط به یهودیان و جامعۀ ایرانیان مقیم بریتانیا رخ داده بود، ارتباطی ندارد.
هنوز جزئیات بیشتری از هویت افراد بازداشتی یا ماهیت اتهام‌های منسوب به آنها منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78319" target="_blank">📅 18:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78317">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J9zgJpxH5h4MwM5q_N7uVp98e7BXCl1r1WR5PUmjT-sAoU3xQqGmBYCUuES5c5vMHL2SZJh1wYPoK0W3zFv0UnleKl2t4IbZ1hSNScPpnvpS8f7UkMKbyx8WOoYwD8LtTnclKsCtSK2-h7CIlPcKLrfUHh3KbzkCRIegmL9EZaG4z8lSBNmipQKTgbNJutmgFcSivuh_vt_AdipYAI6wSB1GXwoR42niehps3yu4ZbmecqGKiAGopsJSADlBgmh_5ymp8tG43cQQGST55_5IDCmsr910YDxpU7Y553pgk7ACwR53gePkWc5-eSv9q2Pc_Mnmfm8vNd3YcG0EPw4LfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DhWEinn53XWjP5Jc7rvPUV753yOCbU0ZGHys0FEXtwHaUna7HtG5mY1ykEShFuP9Egq9438VoqRnIt2n2WqorR-DSwMZzr3E-ow8_5txq2epHbd58u7zGqHZq9xuKqbfR8FPT9tHhdfkDKtE3foUrA95UZTlG_wXlZ43C7nZSCINL4HX_2_0j1w8TSDEFlNtgNkZe3XHc0WTN9K8jL_hHcDhqbTSJO8Bsna4EZG9bIvLg-Sg-CB70nnCVnPsnam5Uh6ihrBa2DFMjIeEcH5CYDiI0kbtW3-_z9uF6Pz724v3e0PxQbEapGdr6XmxLm86OUv5YR-XSRW2NV-W0Pu15w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/78317" target="_blank">📅 17:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78315">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eHeRj02rh5vPmOzIF6evn0BFaK22TcoVDxgSTi1iRWrHjj9UUfzwWIBfDFwnh8SmdkBiuzPEnQzWsYSmjOr6oy0EBqWoL4v3iltHWF2T3cuqoCHl0m_Xh5cu6QxmBvwpwh1gW8wiuzgETfFNGY_paZFHVXYcsQ7bQhy6vPPn06wrR7w8CZLoWBYRuXHtljtfJt6Z3IkMPvmpoZSD9NTWIzDZzZv14eC6clgETC9-qsGXKM4EjB_arJQh9oO0y_4OArI_s_SrCog3FCcgxhPXXRa7jn_nnApIEQXWYkmDzvq0V3viIUVU2JjiFQF9xFDfFJABcgPTBo3t3I9nIcEulA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XE3IwVjovx2S-S-hETWTs-MNFDMDEOYWCFyezAC3yxxuKjODr53T_0FKooMiPGqjmrayTswvN_WDioXyF6K9wXkFmdn0cUny1u6y8IcG0f-FEXf_GMlXURV0yeEnNaJtDsdNwL0iNz-7ewwGR5NM1_GEh7IjCF-RyM5FMvSGbdDtcnJt8cTvoPsVAoVgk7XEFGzZJEEkK-upgBsJe6ndOQhtwmE693AGhEPr5tvsb4k34FFpfMf2MRZGwwQITcFACGQuvhTOrSJp-DVlLwxa5FOKQ4q0MVZeLhmS2755R0MZy9W5FDJE_h2kDUMDcuW7bhCpDAxnUIRP6h8woWtdJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78315" target="_blank">📅 16:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78314">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h17c6RZ9IJBkBlufnQ_i99pqvS9twGXt7KE_fHsdiQmfpfbzRj9WZo_FsCXMw6wN9dNBz9FK850u9z8tmjmkM1Oqk8APx_6kXzvAqrKvVCbTABNxqG9PDzFzCD6i8GUhh_eUu5HfaNKF5pJHeMaGyZdm-6bFX30NfNC1n6eKz44dXPZ4gY1usXnuPvpj3YDpIzHFjfych0wWj0gqwrCPk4URDSFih1ZXwRxqfjXQ0yKQR16Gc20-YgbQrzaGcQBVY9mJxwROykJ04T6ncUWh-eSK5b4jCfMgCCHPKwmXUIMcH5Moa7jhZrN3FOn0ymcqap3KUK1T4aSR783oEhuqJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند افزایش روزانه قیمت ارز در بازار تهران روز پنجشنبه ۱۹ شهریور (۱۰ سپتامبر) ادامه یافت و بهای دلار به ۲۳۵ هزار و ۷۰۰ تومان رسید.
dw_persian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78314" target="_blank">📅 16:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78313">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGcT1dHvRYFt1gQfBVSK1GsFQtu72Ty99VmlOIFkjYu6cQsKBxlu1_QD0G0NlhDrrLI0MvcahvvX2xbWDxpbI1a5kb0ooSHdzyLQwxnCeAmMVJ4jrOHdulK60UTLB38oh4_ujujxpdmuzINF99FXn8c27brOw0R-khQZqPuXgUtWitkKpvCtp99pF_FCQ8X9ZzmKZ_vdJ4SqKlyzglKxSoOfi3D4PBtNC_jaOwRFnFMvpUMMLcfBiDx_ZkQeXbPRG8TxdUqI5clNZg-vG9wpwQguTjBYChfQyau6GYqtHxAq0a_o9WHi7bIKBoTRKZhNTT1MubZguvx53o0KrbjoxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی افزایش تنش‌ها در خاورمیانه، قیمت نفت شاخص برنت روز پنج‌شنبه از ۱۰۲ دلار عبور کرد که نسبت به روز گذشته حدود یک درصد و نسبت به ابتدای ماه حدود ۸ درصد رشد نشان می‌دهد.
طبق برآورد اداره اطلاعات انرژی آمریکا، ماه گذشته تولید روزانه نفت ایران به خاطر اعمال مجدد محاصره دریایی آمریکا ۸۰۰ هزار بشکه نسبت به ماه ژوئیه افت کرده، اما هم‌زمان تشدید حملات جمهوری اسلامی به کشتی‌ها در تنگه هرمز و آغاز حملات حوثی‌ها در دریای سرخ و باب‌المندب به نفتکش‌های عربستان نیز باعث شده متوسط تولید روزانه نفت کشورهای عرب منطقه در ماه گذشته ۹۴۰ هزار بشکه نسبت به ماه ژوئیه کاهش یابد.
مجموع تولید نفت ایران و کشورهای عرب منطقه در ماه گذشته ۶.۷ میلیون بشکه کمتر از دوران پیش از جنگ خاورمیانه بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/78313" target="_blank">📅 16:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78312">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4TV1bdRx3EfZXXwCnIPX6mIYsWCJKi2nqMaw3gO-9DV59d0AgnJGeUuN1ZzDnpVgZBSPsN7SBcaGn9o252_K69u5rU7tL6unaVLAgmd8C2HH7t9tGn565aL6-Kr9xIdRzMjxWllbxvTmnuJrn-pfbfPl5_TRPd5ms6kstFVmPQr48FgrFEyV42fj4yMyN7LQvqDg53T3AcL2bdhZLbm43T11-Z4iY0YWGp0Rp2GVZi15Tp5a31QVbs-_fsD0vs1bNj4NVXTsohgReumxageRNSha_gv91S-DNw6tlUs9CwWzbMm1rMzKB-6J5-zaOLw-D6FQjqq7BHrdkhpwvgMig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع ارشد ایرانی و سه فرد مطلع می‌گوید حکومت ایران با استفاده از سازوکاری شبیه تهاتر و با دور زدن تحریم‌ها، در حال وارد کردن میلیاردها دلار کالا از جمله تجهیزات نظامی از چین است.
در این گزارش که روز پنجشنبه ۱۹ شهریور منتشر شد، منابعی که نام‌شان اعلام نشده گفته‌اند بر اساس این سازوکار تجاری مخفی، نفت ایران در ازای اعتبار برای واردات از چین در سال‌های اخیر، یک شریان حیاتی مالی برای تهران همزمان با افزایش فشارهای اقتصادی و نظامی ایالات متحده فراهم کرده است.
آن‌ها گفته‌اند که این سازوکار همچنین به چین، بزرگ‌ترین واردکنندهٔ نفت خام جهان، کمک کرده است تا به نفت تخفیف‌دار ایران دسترسی داشته باشد.
به نوشتهٔ رویترز و به نقل از منابع طرف گفت‌وگو با آن، ایران از این سازوکار برای خرید دارو، وسایل نقلیه و تجهیزات ارتباطی از چین نیز استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/78312" target="_blank">📅 16:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78311">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=EV5LQTmR0Ch6Z1wBzCqa4xgJkz7JcJ7K8eAqPPvJn-CSuXRw7FDXtqS2qL4-Yg3l5posOM36bBa7s8ykD4KzDkLmYdkZhx_NUvnZNx7A2rhJzR2dIHAsmAfWZv1JiDj99PrDzhKlTUnPKiHCXVRMwElTYBzYuAYGHJA4kYmixTcsSFAGfekh-tc52mS30AKg8onpsiO3fhtvfI64NKGUHyOMS7ds0ZfHKMyWq1lJfGsd9r5FNv24r5y4AOvFCUyalK0E9PlXbdpPy_Pe_ZZCvBGYVEZKf_Ak3FDdxd4ouWhWBD3DFYmVQdLErehiKrmiJIzcEkRIFEO-XTIx_lmkyg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=EV5LQTmR0Ch6Z1wBzCqa4xgJkz7JcJ7K8eAqPPvJn-CSuXRw7FDXtqS2qL4-Yg3l5posOM36bBa7s8ykD4KzDkLmYdkZhx_NUvnZNx7A2rhJzR2dIHAsmAfWZv1JiDj99PrDzhKlTUnPKiHCXVRMwElTYBzYuAYGHJA4kYmixTcsSFAGfekh-tc52mS30AKg8onpsiO3fhtvfI64NKGUHyOMS7ds0ZfHKMyWq1lJfGsd9r5FNv24r5y4AOvFCUyalK0E9PlXbdpPy_Pe_ZZCvBGYVEZKf_Ak3FDdxd4ouWhWBD3DFYmVQdLErehiKrmiJIzcEkRIFEO-XTIx_lmkyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تخریب «کاروانسرای روس‌ها» در سبزوار:
quotes
خانه واجد ارزش تاریخی «تومانیان» معروف به «پادگان روس‌ها» در سبزوار روز چهارشنبه در روز روشن با لودر تخریب شد و اعتراض گسترده فعالان میراث فرهنگی را به همراه داشت.
تصاویر منتشر شده در شبکه‌های اجتماعی نشان می‌دهد که یک دستگاه لودر روز چهارشنبه ۱۸ شهریور بخشی از یک بنای تاریخی معروف به «پادگان روس‌ها» در سبزوار را تخریب کرده است.
«پادگان روس‌ها» یا خانه «تومانیان» در سبزوار با وجود آنکه در فهرست آثار ملی ثبت نشده بود اما از سوی میراث فرهنگی به عنوان یک بنای واجد ارزش تاریخی اعلام شده بود.
معماری این بنا متعلق به دوره پهلوی اول بوده و در زمان اشغال ایران توسط روس‌ها، ارتش روسیه مدتی در این بنا مستقر شده و به همین دلیل به «پادگان روس‌ها» مشهور شده است.
مجتبی کاویان، مدیرکل میراث فرهنگی و مدیر پایگاه بافت تاریخی سبزوار در گفت‌وگو با صدای میراث گفت: این اثر بدون هماهنگی و بدون مجوز میراث فرهنگی تخریب شده و اعلام جرم علیه تخریب کنندگان این اثر واجد ارزش تاریخی قطعی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78311" target="_blank">📅 16:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78309">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ac8H8giI6fWgLL5ivnqELislMoEsNfrayPdxMx1vdM5E16pBUh0I4fp9bvZxMzCZrRy9nowQv0-TxNLckDLUVTVtl0Gcej0srrCSBy1vAO2mTLcsteEJ4yShCsZ4CKQ2_gMc9DRGfkWBDy7V1FEvXcI149SRhVRmcPs0s5KFr40d1kgAbogyakhKgzGXc12O5inuxyeDvjre7daDNY8NF7y34TgcMxKenrROYm5P4mozilNgHnjH0Sk9W0I9VgKF4_ypNiMdrwpi_kHz8-1yj7jaN56ruW-jGV1kmlxmL9q8bwhiuK4hn7md8wDZIPpvHZ6UEcaZyDncp7lPPQQT7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dJ9BcWdvFL3h6uJNDJWNz3CPCur5tBJ7PLFWuGP9pDZjfiTloAQC3I4SrvDdNon2wyM4qol31ySzp5htQVRk3X3gwpJDEmzG-AACpTQyswb5VjM6vEBAbFkQC5zUzKBPh_UZAEmRl0f1K6ArHHFWQ-03B1M_PMFz7TVwQNSU4whkK3B-JQg0S4kMhb97KY5NOCeMpn5eYXJ6qZ-oylkof7Kbi1RPP9RCKsiqikSwQ3cTEHBmkA0BTLHuzKRisUrAek4NDoMPjWFquo3bTFs204ZnlhT4Ade0Wef_Rrlf68yho4qtvp0W02J0erKh5pxYHfs9ZKoRU1k-wqVMFEiwpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ از مشاهده «تحرکاتی» در کوه کلنگ‌گزلا خبر داد و به جمهوری اسلامی ایران هشدار داد: «توصیه می‌کنم ایران زرنگ‌بازی درنیاورد، زیرا مجبور خواهیم شد بسیار سخت به آن حمله کنیم.»
ترامپ در ادامه از حاضران پرسید آیا ایران باید سلاح هسته‌ای داشته باشد و پس از پاسخ منفی جمعیت گفت دولت‌های پیشین دهه‌ها تلاش کرده‌اند جمهوری اسلامی را از دستیابی به سلاح هسته‌ای منصرف کنند، اما به گفته او، مقام‌های جمهوری اسلامی ایران «زبان گفتگو را نمی‌فهمند.آن‌ها فقط یک چیز را می‌فهمند و اکنون به مقدار زیادی از همان نصیبشان می‌شود».
@
VahidOOnLine
رییس‌جمهوری آمریکا، در گردهمایی جمهوری‌خواهان در دالاس گفت جنگ با جمهوری اسلامی مدت کوتاهی پس از انتخابات میان‌دوره‌ای سوم نوامبر پایان خواهد یافت و تهران خواهان توافق با دموکرات‌ها است.
ترامپ برجام را «یکی از بدترین توافق‌ها» خواند و گفت جمهوری اسلامی در مسیر دستیابی به سلاح هسته‌ای قرار داشت.
او افزود: «اگر من برجام را لغو نکرده بودم و اگر با بمب‌افکن‌های زیبای بی-۲ آنها را هدف قرار نداده بودیم، اکنون سلاح هسته‌ای داشتند.»
ترامپ گفت در آن صورت مجبور بود با رهبر جمهوری اسلامی تماس بگیرد و بگوید: «جناب رهبر، حالتان چطور است قربان؟ کاری هست که بتوانیم برایتان انجام دهیم؟»
ترامپ در ادامه تاکید کرد: «ما نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. موضوع بسیار ساده است. نمی‌توانیم اجازه دهیم آنها سلاح هسته‌ای داشته باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78309" target="_blank">📅 06:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78308">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78308" target="_blank">📅 06:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78307">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78307" target="_blank">📅 06:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78306">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78306" target="_blank">📅 06:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78305">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پیام‌های دریافتی:
سلام الان ساعت ۰۰:۲۵ قشم صدای انفجار اومد
قشم صدای انفجار اومد
وحید قشم بد زدن تمام خونه لرزید
#قشم
00:24 نوزدهم شهریور
صدای انفجار و لرزش
قشم صدای شدید
شیشه ها لرزید
موج انفجار شدید همین الان قشم 00:25
وحید قشم یه صدایی اومد
شیشه ها لرزید
صدای یک انفجار بندرعباس
وحید جان انفجار شدید ساعت 12:25 قشم
سلام صدای وحشتناک باعث لرزش شیشه خونه شد
سلام قشمو بد زد کل ساختمون لرزید
همین الان نزدیک قشم صدا انفجار اومد.
خونه لرزید.
صدای انفجار به بندرعباس رسید لب ساحل نمیدونم کجا زدن
درود به آقا وحید شبت بخیر ساعت 0:25 انفجار سنگین از سمت دریا نمیدونم قشم بود یا جای دیگه ولی بندرعباس به شدت حس شد
قشم لرزید
موجش قوی بود
شدید بود خیلی
توی دریا بود انگار
سلام داداش وحید .صدای انفجار مهیب در قشم شنیدیم
خیلی مهیب بود ..
۰۰:۲۶ بندرعباس انفجار رخ داد
فقط صدا نبود
در و پنجرها هم تکون خوردن
صداش انقدر جدید بود ما داریم میگردیم میگیم لابد اسانسور ساختمونمون ول شده
🤦‍♀️
صدای انفجار در خونه لرزيد قشم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78305" target="_blank">📅 00:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78304">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/692967643d.mp4?token=Coz-CDAlpYwWoRplCrM-7m3n0OT1hF5cQbeKmITSMauYAuc7rYdXXRytwgvbPEjX2Ugbrfx5X4C4JT9UGu7z8sLXRoI3M0pGnj7paro81qLu3A5zZwNOqMrwkymbulz3eH5cRI4prEwzts8YIRqJqj2xPbUkwjeu0ha_JFPpEpW8Ph5fEwG8In6AvFPm_m-qA4fXXMKK2WmGpIN8srAPZNh4RmnHkBxRqKM2EvHmXCJDbKpTB1pcc-AOPlyfQEWZwEQnRyLvVqRluEYgpKvJEg7JD-JDjI5376jRQzPmhpgFIYKIPld0AT_iGANreQ43MBCJJHftC55thes6gr8TdA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/692967643d.mp4?token=Coz-CDAlpYwWoRplCrM-7m3n0OT1hF5cQbeKmITSMauYAuc7rYdXXRytwgvbPEjX2Ugbrfx5X4C4JT9UGu7z8sLXRoI3M0pGnj7paro81qLu3A5zZwNOqMrwkymbulz3eH5cRI4prEwzts8YIRqJqj2xPbUkwjeu0ha_JFPpEpW8Ph5fEwG8In6AvFPm_m-qA4fXXMKK2WmGpIN8srAPZNh4RmnHkBxRqKM2EvHmXCJDbKpTB1pcc-AOPlyfQEWZwEQnRyLvVqRluEYgpKvJEg7JD-JDjI5376jRQzPmhpgFIYKIPld0AT_iGANreQ43MBCJJHftC55thes6gr8TdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز چهارشنبه ۱۸ شهریور گفت که از دید او جنگ با ایران «بلافاصله» بعد از انتخابات میان‌دوره‌ای آمریکا پایان خواهد یافت.
دونالد ترامپ پیش از عزیمت به سمت شهر دالاس برای شرکت در اجلاس حزب جمهوری‌خواه به خبرنگاران گفت: «فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام خواهد شد. چون آن‌ها (ایران) دیگر نمی‌توانند دوام بیاورند».
ترامپ درباره وضعیت ایران افزود: «آن‌ها مستأصل هستند و تلاش می‌کنند بر انتخابات تأثیر بگذارند».
ترامپ در پاسخ به پرسشی درباره حملات گسترده طرفین در اطراف تنگهٔ هرمز گفت: «حملات توسط ما انجام شد. ما ۹ نفتکش آن‌ها را زدیم. قرار است حملات بیشتری انجام شود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/78304" target="_blank">📅 23:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78303">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/739c863db9.mp4?token=R9APe20rB9iclewojaffTaqOZveIhvd0WTsxe5P22hkXHCLCXprDz_zG8ywBDZDTGDPKio12r6pA_1gkNFvNR3uh5e4fFDG7DoOwE7HLbgTKJQ0n-hJ61YQ315a5sd8q3YAo14uQvcccD-k4Vp6_Dy2ILLvhzh8i4Od_9DN8Q_0kSnHAqGn3XCE7H_meCSHHDqdkdgGeFWektILcLZPdNLSEpKEd4sznypAELFLa8zT9ifHtIoE4PIdibYVQIy5WnH8DkEeCc6yX3WxOCsMZjl03LUPx9v4jWsIH4BR-kSh-8NifrbWR2rn_fdMyvglK7bCdPjPBjgBLxormh9BJPw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/739c863db9.mp4?token=R9APe20rB9iclewojaffTaqOZveIhvd0WTsxe5P22hkXHCLCXprDz_zG8ywBDZDTGDPKio12r6pA_1gkNFvNR3uh5e4fFDG7DoOwE7HLbgTKJQ0n-hJ61YQ315a5sd8q3YAo14uQvcccD-k4Vp6_Dy2ILLvhzh8i4Od_9DN8Q_0kSnHAqGn3XCE7H_meCSHHDqdkdgGeFWektILcLZPdNLSEpKEd4sznypAELFLa8zT9ifHtIoE4PIdibYVQIy5WnH8DkEeCc6yX3WxOCsMZjl03LUPx9v4jWsIH4BR-kSh-8NifrbWR2rn_fdMyvglK7bCdPjPBjgBLxormh9BJPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامعلی حداد عادل می‌گوید حکومت فعلا نمی‌تواند «به علت شرایط جنگ آن‌طور که باید وارد جبهه حجاب» شود.
این عضو شورای عالی انقلاب فرهنگی و مجمع تشخیص مصلحت نظام در ادامه می‌گوید شرایط کنونی کشور از نظر حجاب «بسیار سخت‌تر از سال ۶۰ است که شروع به کار کرده بودیم».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78303" target="_blank">📅 21:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78302">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c9ZBpwlk3XHxtqLSa5nMc5D7PwCg9pd-mw9Nd6N-ROBs3moMuQtCWXCDJRFRVF3GYmI_JvZ_sCdybpfapMCJXIUYSLkJowo74jq_fSt67FSAapjmhbe8VULE5ktbCSiXgzhd1SkPPiqkF6onAvqueK15rUD4zo82Z8eDtzOEznhDD47NSWoeUnP18mSrZrH91UGKufZ507OeoeKxFsNRtbENofuJlYMkItq5CiQOofrvODYdGGmqmk2OMo8qP3W-P2WPUprZqphEb0e-RI4H6s0H9ibutUgFZe4ypf5lVWicsVp30Ycz01HkWhy2-_5KHtvkgp5lf_U1K5-RxO-nCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز روز چهارشنبه ۱۸ شهریور به نقل از منابع دیپلماتیک گزارش داد که شورای حکام آژانس بین‌المللی انرژی اتمی با صدور قطعنامه‌ای، پرونده ایران را به دلیل نقض تعهدات منع اشاعه هسته‌ای، پس از ۲۰ سال به شورای امنیت سازمان ملل متحد ارجاع داده است.
این قطعنامه جدید در پی قطعنامه پیشین شورای حکام در ۱۲ ژوئن سال گذشته صادر شد؛ فهرستی از موارد «پایبند نبودن» ایران به تعهداتش که درست یک روز پیش از آغاز حملات هوایی اسرائیل و متعاقبا ایالات متحده به تاسیسات هسته‌ای ایران تصویب شده بود.
بر اساس قوانین و الزامات حقوقی، گزارش رسمی این نقض تعهدات به شورای امنیت سازمان ملل، مستلزم تصویب دومین قطعنامه از سوی این شورای ۳۵ عضوی بود که اکنون به سرانجام رسیده است. این اقدام می‌تواند مسیر را برای بازگشت تحریم‌های بین‌المللی و افزایش فشارهای دیپلماتیک بر تهران هموارتر کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78302" target="_blank">📅 20:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78301">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ue1V0-x0z59WqY92a8TwFQeLNotVcSKSvoBoDjrrjaz2RNql-6JtsxFkzERl_iAqrDdPsAclO_TgeGgGFEDagJVwKciI4EnYE3DlVSyGQrTlfPopFkn7hXWQ-ghIxBo9YA0_rAnJdw9PHx33vBXcRo7pPiUcK1sB4C-gsCuqMs2_8KD_bsKgb7azORwZ8cAGqx0kN01Qw96ppZWzzvDeGYwqV2KZTJ6E89Vd_fbgVXuxaw6smLBZtCintE28x0d-UmqEpVX02m6M6DP5MHLVUhjpZr7JkJnPT4EUQxj0dsZ97b7ZbxX71o11v8hv_n6_HSf8A5SavVmLjDpXVkaRpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: 'شناور آمریکایی در تنگه هرمز، سمت جزیره سلامه خصب عمان، چهارشنبه ۱۸ شهریور'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78301" target="_blank">📅 19:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78300">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5c510746f.mp4?token=g73Ta6ZF5-wXl7kjmmsWkRty9vjvwiIT8Tk8R_dHyP9cvYYoU1fUimij-odR1c7niqCg77X_s_WAgqtMHwzUG_NWtFg2ehoMrDObnKGyO5KsVXQcxRxPE2WMmE7AZ3JvaQo_NChxKmYKGjrBQdyV0LouppHLqR0TKiXkGygQBe-wYSLY3QKgPNcrnMzdXApPOXScuJMOo_F3DWk0-NPDZKKmZsq8XimjpyZjsBB2w-RLZLxd8LmswBCQufDU4cqA3EsVsBFjKVVlJ-hJHU1iI2Y20J-QZq75QMHY068GML14dZiLWwe32dYR9kCIFmOtCtWsQ88Zkd5e78wNl3P54g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5c510746f.mp4?token=g73Ta6ZF5-wXl7kjmmsWkRty9vjvwiIT8Tk8R_dHyP9cvYYoU1fUimij-odR1c7niqCg77X_s_WAgqtMHwzUG_NWtFg2ehoMrDObnKGyO5KsVXQcxRxPE2WMmE7AZ3JvaQo_NChxKmYKGjrBQdyV0LouppHLqR0TKiXkGygQBe-wYSLY3QKgPNcrnMzdXApPOXScuJMOo_F3DWk0-NPDZKKmZsq8XimjpyZjsBB2w-RLZLxd8LmswBCQufDU4cqA3EsVsBFjKVVlJ-hJHU1iI2Y20J-QZq75QMHY068GML14dZiLWwe32dYR9kCIFmOtCtWsQ88Zkd5e78wNl3P54g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با حضور در قله جبل‌الشیخ (حرمون) و اشاره به تسلط بر مناطق مرزی سوریه و لبنان، هدف اصلی کارزارهای نظامی جاری این کشور در منطقه را شکست و سرنگونی رژیم ایران عنوان کرد.
نتانیاهو در پیامی ویدیویی، به حضور نیروهای نظامی اسرائیل در مناطق مرزی سوریه و لبنان اشاره کرد و گفت: ما اجازه نخواهیم داد هیچ گروه تروریستی در مرزهای ما مستقر شود. این یکی از دستاوردهای عظیم ماست، اما کار اصلی هنوز باقی مانده است.
نخست‌وزیر اسرائیل با ابراز اطمینان از دستیابی به این هدف افزود: کار اصلی ما شکست دادن و تضعیف کامل رژیم ایران است. ما بسیار به این هدف نزدیک هستیم و می‌دانیم که کل این محور سرانجام سقوط خواهد کرد و ما این کار را انجام خواهیم داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78300" target="_blank">📅 18:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78299">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p7BXXvCxXhfWNavEMdGWVKytcmJ9El0UEZa3UyrN1YF6b_IPUabx0kCaMbU-QVz-8rCQCO7W3VjeUcVkIc0iwm9wHn_Ug6FZ_E8TUv-K7DqjjghuqC6Eb-nCN-1L8xn4N9L79yFhWCILK8GMRmH3fDBiRn0BnPjFpcrSbQc0uqpNOYW2ME2NnmJaCxmzkooWI5HCCHn9CPsVJ1HwL_2ZFuqScWAEAktJGyg-Gb00v6RSQ7O5-yrPaQ6h9QJx-oqrmbwGfzdwp_Io2IJT_qDCfKs1D8GpG7ha3IFJ21woRE30o406Yc6dQER3sl59viO72eGYmF91iD1hDxrOx4REHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه پاسداران برای پایان وضعیت کنونی و بازگشایی تنگه هرمز از آمریکا خواست جنگ و تهدیدها را متوقف کند، اسرائیل از لبنان عقب‌نشینی کند، محاصره یمن پایان یابد، ۲۴ میلیارد دلار از دارایی‌های مسدودشده ایران آزاد شود و مداخله در برنامه‌های هسته‌ای و موشکی جمهوری اسلامی متوقف شود.
حسین محبی، سخنگوی سپاه پاسداران، روز چهارشنبه ۱۸ شهریورماه گفت اگر آمریکا خواهان پایان وضعیت کنونی است، باید ضمن «توقف کامل جنگ» از تهدید دوباره دست بکشد.
محبی در بخش دیگری از سخنانش تهدید کرد که در صورت ادامه حملات، پاسخ سپاه گسترده‌تر خواهد بود و گفت: «اگر دشمن دو یا سه هدف ما را بزند، ما با ۲۰ هدف پاسخ محکم می‌دهیم.» او همچنین گفت جنگ کنونی برای نخستین‌بار «آسیب‌های راهبردی» را مستقیما به آمریکا منتقل کرده است.
این اظهارات در حالی مطرح شد که با تداوم محاصره دریایی ایران، صادرات نفت از طریق تنگه هرمز متوقف شده و فشار تحریم‌های مضاعف دولت ترامپ، باعث تورم کم‌سابقه در ایران و رسیدن قیمت دلار به ۲۳۳هزار تومان شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78299" target="_blank">📅 16:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78298">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kmxz9KhidpSx4adMO1ZEXq-YqCGidZwKIUHKVH9w8x4JU5b97Ik156nBXDTBbHGkkZ3EceduLeybIMh-uHCCEezEyTL9Utc7h0QmmuYSyYQB4z8vHH6jCOOQ6TTPaj-CBbc3MttWJZefAQvQWzBJB3bJL89O9enNro9YbciRw-Bo9FbTd15CYiJRVOCKeoCnqbBS5dqya1vgmx8HOsd01lmW94VgmDlIqcldIHwLfArDjzA5yhs5-jfYrrK4F6HUWtPa5u1atxgA4ftYLOaNtq4yaSvxwX5lTsdqQQpUabhSEQ_foN0aue6nZq1GF1WLA_WLB-bz9jXit_VEY6ndSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ارزهای خارجی در بازار آزاد ایران روز چهارشنبه ۱۸ شهریور ۱۴۰۵ رکورد تازه‌ای ثبت کرد و نرخ دلار آمریکا از ۲۳۲ هزار تومان گذشت.
برخی وب‌سایت‌های اعلام قیمت ارز نرخ دلار را در معاملات ظهر چهارشنبه تا ۲۳۵ هزار و ۵۰۰ تومان نیز گزارش کردند.
هم‌زمان قیمت یورو از ۲۷۱ هزار تومان و پوند بریتانیا از ۳۱۵ هزار تومان فراتر رفت. این افزایش‌ها در حالی ادامه دارد که ریال طی دو هفته گذشته بیش از ۱۵ درصد ارزش خود را در برابر دلار از دست داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78298" target="_blank">📅 16:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78297">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKpezGzYZ0awU9-SN6YCal2PpY1XlND2isOFtrBytYz89v1Jzolowsb2AMcJbwjcxaLekUQWDQA6jcNAkxc1NQnzLeFuTOMLY16VP_AP0xEPs9DfZVEeTEYcTewTesaNByr4QRrMeATbPqs9b0_YMA94YY9biDttajFpeL2-DNCRZBN2jETr3fyNJJOwh6qffswzkQFcirOjCdXsJE6mxvJemWIVIv-SUEbUZkiX0MxNQ14_cyBH0JkrbhxJUOlx0qjsR6KI4MG4wNPpoktLxEzeoqevctxVYkgVhogXa6XxqIyLmj-ZAXiRKm3qrzdXmLN1Cc4sEiEKnExGYkRG9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت خام برنت برای نخستین بار از دوم مرداد به ۱۰۰ دلار در هر بشکه رسید و بار دیگر وارد محدوده سه‌رقمی شد.
افزایش قیمت نفت و ارز در شرایطی رخ داده است که درگیری‌ها در خلیج فارس و منطقه ادامه دارد. شامگاه سه‌شنبه ۱۷ شهریور، آمریکا اعلام کرد پس از حملات موشکی ناموفق جمهوری اسلامی به دو ناو جنگی این کشور در خلیج فارس، پنج نفتکش مرتبط با سپاه پاسداران را منهدم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/78297" target="_blank">📅 16:20 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
